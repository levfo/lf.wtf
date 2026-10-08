// owner: population
// Section 3.7 exports, and the population steps of section 8: consumption (8.4), homeless move-in, aging,
// deaths, births, migration and militia (8.11), and happiness and exodus (8.12). Jobs follow 4.2 and 5.2.
// Pure: no DOM, no random source other than rng.js, no wall-clock time, no trigonometry or exponentials.
// Tunable numbers come from src/config.
import { TIME } from '../config/index.js';
import { ECONOMY } from '../config/economy.js';
import { POPULATION as P, NAMES } from '../config/population.js';
import { BUILDINGS } from '../config/buildings.js';
import { emit, citizenById } from './state.js';
import { rand, randInt, pick, chance } from './rng.js';

const YEAR = TIME.daysPerYear;
const WINTER = 3;
// Cadence of the militia stall warning (section 8.11: days divisible by 10). A presentation cadence, not a
// balance number, so it has no config key yet; see issuesForOthers.
const STALL_WARN_EVERY = 10;
// The stat that counts each cause of death in killCitizen.
const DEATH_STAT = { age: 'oldAgeDeaths', famine: 'famineDeaths', plague: 'plagueDeaths', fire: 'fireDeaths', raid: 'raidDeaths' };
const mean = (list) => Math.floor(list.reduce((a, b) => a + b, 0) / list.length);
// Typical start age per cohort in whole years: the floored mean of its start ages (section 5.1).
const TYPICAL_YEARS = { child: mean(P.startYears.children), adult: mean(P.startYears.adults), elder: mean(P.startYears.elders) };

const seasonOf = (day) => Math.floor((day % YEAR) / TIME.daysPerSeason);
const plagueOn = (state) => state.schedule.plagueStart >= 0 && state.day >= state.schedule.plagueStart
  && state.day < state.schedule.plagueUntil;
// Active effects of one kind: until > day, the rule of activeEffect in events.js.
const activeCount = (state, kind) => state.effects.filter((e) => e.kind === kind && e.until > state.day).length;
const staffedCount = (state, type) => state.buildings.filter((b) => b.type === type && b.stage === 'complete' && b.crew > 0).length;
const isDwelling = (b) => b.stage === 'complete' && (BUILDINGS[b.type]?.beds ?? 0) > 0;
const isEligible = (c) => cohortOf(c.ageDays) === 'adult' && !c.militia;

// Residents per dwelling id, from the citizens' homeId.
function residentCounts(state) {
  const counts = new Map();
  for (const c of state.citizens) if (c.homeId !== 0) counts.set(c.homeId, (counts.get(c.homeId) ?? 0) + 1);
  return counts;
}

// Whole units owed today from a fractional flow; the remainder carries to the next day (section 8.4).
function takeWhole(state, key, amount) {
  const t = state.carry[key] + amount;
  const whole = Math.floor(t);
  state.carry[key] = t - whole;
  return whole;
}

// Appends a citizen with the next id and returns it. Field order matches the save format.
function addCitizen(state, ageDays, homeId, name) {
  const c = { id: state.nextCitizenId, name: name ?? pick(state, NAMES), ageDays, homeId, workId: 0, militia: false };
  state.nextCitizenId += 1;
  state.citizens.push(c);
  return c;
}

const moodFactor = (happy) => {
  for (const [below, factor] of P.birthMood) if (happy < below) return factor;
  return 1;
};

// Annual natural death chance for a whole number of years, from the age bands (section 5.6).
function hazardAt(years) {
  for (const [lo, hi, rate] of P.hazardByYears) if (years >= lo && years <= hi) return rate;
  return 0;
}

// True when a complete Well stands within plagueWellRadius tiles (Chebyshev, between footprints) of the home.
function nearWell(home, wells) {
  if (!home) return false;
  const r = P.plagueWellRadius;
  return wells.some((w) => {
    const dx = Math.max(0, home.x - w.x, w.x - (home.x + home.w - 1));
    const dy = Math.max(0, home.y - w.y, w.y - (home.y + home.h - 1));
    return Math.max(dx, dy) <= r;
  });
}

export function cohortOf(ageDays) {
  if (ageDays < P.childUntilYears * YEAR) return 'child';
  if (ageDays >= P.elderFromYears * YEAR) return 'elder';
  return 'adult';
}

export function isFertile(citizen) {
  if (citizen.militia || cohortOf(citizen.ageDays) !== 'adult') return false;
  return citizen.ageDays >= P.fertileMinYears * YEAR && citizen.ageDays < (P.fertileMaxYears + 1) * YEAR;
}

export function populationSummary(state) {
  const out = {
    total: state.citizens.length, children: 0, adults: 0, elders: 0, employed: 0, unemployed: 0, homeless: 0,
    militia: 0, beds: 0, freeBeds: 0, fertile: 0, eligibleAdults: 0,
  };
  for (const c of state.citizens) {
    const cohort = cohortOf(c.ageDays);
    if (cohort === 'child') out.children += 1;
    else if (cohort === 'elder') out.elders += 1;
    else out.adults += 1;
    if (c.militia) out.militia += 1;
    if (c.workId > 0) out.employed += 1;
    if (c.homeId === 0) out.homeless += 1;
    if (isFertile(c)) out.fertile += 1;
    if (isEligible(c)) {
      out.eligibleAdults += 1;
      if (c.workId === 0) out.unemployed += 1;
    }
  }
  const counts = residentCounts(state);
  for (const b of state.buildings) {
    if (!isDwelling(b)) continue;
    const beds = BUILDINGS[b.type].beds;
    out.beds += beds;
    out.freeBeds += Math.max(0, beds - (counts.get(b.id) ?? 0));
  }
  return out;
}

export function dwellingFreeBeds(state, building) {
  const beds = BUILDINGS[building.type]?.beds ?? 0;
  if (beds <= 0) return 0;
  return Math.max(0, beds - (residentCounts(state).get(building.id) ?? 0));
}

// Clears every job, then fills crew slots in fill order (4.2). Elders queue ahead of adults for taverns and chapels.
export function assignJobs(state) {
  for (const c of state.citizens) c.workId = 0;
  for (const b of state.buildings) b.crew = 0;
  const adults = state.citizens.filter(isEligible);
  const elders = state.citizens.filter((c) => cohortOf(c.ageDays) === 'elder' && !c.militia);
  const queues = {
    adult: adults,
    adultOrElder: elders.concat(adults),
    militia: state.citizens.filter((c) => c.militia),
  };
  const cursor = { adult: 0, adultOrElder: 0, militia: 0 };
  // Priority buildings first, then by crewPriority, then by id. Paused and unfinished buildings take no crew.
  const order = state.buildings
    .filter((b) => b.stage === 'complete' && b.priority !== 'paused' && (BUILDINGS[b.type]?.crew ?? 0) > 0)
    .sort((a, b) => (a.priority === 'priority' ? 0 : 1) - (b.priority === 'priority' ? 0 : 1)
      || BUILDINGS[a.type].crewPriority - BUILDINGS[b.type].crewPriority || a.id - b.id);
  let filled = 0;
  let open = 0;
  for (const b of order) {
    const def = BUILDINGS[b.type];
    const role = def.crewRole;
    if (!(role in queues)) continue;
    let got = 0;
    while (got < def.crew && cursor[role] < queues[role].length) {
      const c = queues[role][cursor[role]];
      cursor[role] += 1;
      if (c.workId === 0) {
        c.workId = b.id;
        got += 1;
      }
    }
    b.crew = got;
    filled += got;
    open += def.crew - got;
  }
  return { filled, open, unemployed: adults.filter((c) => c.workId === 0).length };
}

export function foodDemand(state) {
  let need = 0;
  for (const c of state.citizens) need += P.foodPerCitizen[cohortOf(c.ageDays)];
  return need * P.rations[state.policies.rations];
}

export function goodsDemand(state) {
  return state.citizens.length * P.goodsPerCitizen;
}

export function fuelDemand(state) {
  return seasonOf(state.day) === WINTER ? state.citizens.length * P.fuelPerCitizenWinter : 0;
}

// Section 8.4: food, goods and firewood are eaten in whole units; shortages set flags and events.
export function consumptionDay(state, events) {
  const food = foodDemand(state);
  const whole = takeWhole(state, 'food', food);
  const eaten = Math.min(state.stock.food, whole);
  state.stock.food -= eaten;
  state.ledger.consumed.food += eaten;
  state.flags.fedFrac = whole > 0 ? eaten / whole : 1;
  state.flags.famine = eaten < whole;
  if (state.flags.famine) {
    state.stats.famineDays += 1;
    emit(state, events, { type: 'famine', kind: 'bad', amount: whole - eaten, text: `The valley went hungry: ${whole - eaten} food short.` });
  }
  const goods = takeWhole(state, 'goods', goodsDemand(state));
  const goodsEaten = Math.min(state.stock.goods, goods);
  state.stock.goods -= goodsEaten;
  state.ledger.consumed.goods += goodsEaten;
  const fuel = takeWhole(state, 'fuel', fuelDemand(state));
  const burned = Math.min(state.stock.wood, fuel);
  state.stock.wood -= burned;
  state.ledger.consumed.wood += burned;
  if (burned < fuel) {
    state.flags.cold = true;
    state.stats.coldDays += 1;
    emit(state, events, { type: 'cold', kind: 'warn', amount: fuel - burned, text: `No firewood for ${fuel - burned} wood: the cold bites.` });
  }
  // Food warning (8.4 step 4, R2-05). The gate is unchanged: gross cover under foodWarnCoverDays, a net deficit today
  // (food eaten minus the food farms made today) and the cadence. The day count is the food left over that net
  // deficit, so farms count. The top-bar day count is specified to use the same net deficit (R2-03 c).
  const deficit = state.ledger.consumed.food - state.ledger.produced.food;
  const cover = state.stock.food / Math.max(1, food);
  if (cover < ECONOMY.foodWarnCoverDays && deficit > 0 && state.day - state.schedule.foodWarnDay >= ECONOMY.foodWarnEvery) {
    const days = Math.floor(state.stock.food / deficit);
    emit(state, events, { type: 'foodWarning', kind: 'warn', text: `Food is running out: about ${days} days of cover left. Build a Farm, or set Rations to Half (Kingdom > Policies).` });
    state.schedule.foodWarnDay = state.day;
  }
}

// Section 5.6 cause table, in exact key order. target = clamp(base + sum of values, min, max).
export function computeHappiness(state) {
  const sum = populationSummary(state);
  const cfg = P.causes;
  const food = foodDemand(state);
  const cover = state.stock.food / Math.max(1, food);
  const fed = state.flags.fedFrac;
  const u = sum.unemployed / Math.max(1, sum.eligibleAdults);
  const policies = state.policies;
  const season = seasonOf(state.day);
  const taverns = staffedCount(state, 'tavern');
  const chapels = staffedCount(state, 'chapel');
  const causes = [];
  const add = (key, label, value, detail) => causes.push({ key, label, value, detail });
  const coverText = `Food covers ${cover.toFixed(1)} days`;
  if (cover >= cfg.food.wellFedDays) add('food', 'Food', cfg.food.wellFed, coverText);
  else if (fed < 1) add('food', 'Food', cfg.food.shortMax * (1 - fed), `Short today: ${Math.round(fed * 100)}% of food met`);
  else add('food', 'Food', 0, coverText);
  const homeless = sum.homeless;
  add('homes', 'Homes', homeless === 0 ? cfg.homes.none : Math.max(cfg.homes.min, cfg.homes.perHomeless * homeless),
    homeless === 0 ? 'Everyone has a bed' : `${homeless} ${homeless === 1 ? 'person sleeps' : 'people sleep'} in tents`);
  const jobs = u <= cfg.jobs.lowRate ? cfg.jobs.lowBonus
    : u <= cfg.jobs.midRate ? 0 : Math.max(cfg.jobs.min, -(u - cfg.jobs.midRate) * cfg.jobs.perPoint);
  add('jobs', 'Jobs', jobs, `Unemployed ${sum.unemployed} of ${sum.eligibleAdults} adults (${Math.round(u * 100)}%)`);
  add('rations', 'Rations', cfg.rations[policies.rations], `Rations: ${policies.rations}`);
  add('tax', 'Taxes', cfg.tax[policies.tax], `Tax rate: ${policies.tax}`);
  add('amenity', 'Taverns and chapels', cfg.amenity.each * (Math.min(cfg.amenity.max, taverns) + Math.min(cfg.amenity.max, chapels)),
    `${taverns} tavern${taverns === 1 ? '' : 's'} and ${chapels} chapel${chapels === 1 ? '' : 's'} staffed`);
  const goods = state.stock.goods;
  add('goods', 'Goods', goods >= cfg.goods.plentyAt ? cfg.goods.plenty : goods < cfg.goods.shortBelow ? cfg.goods.short : 0,
    `${goods} goods in stock`);
  add('season', 'Season', cfg.season[season], TIME.seasonNames[season]);
  const festival = activeCount(state, 'festival') > 0;
  add('festival', 'Festival', festival ? cfg.festival : 0, festival ? 'A festival is lifting spirits' : 'No festival under way');
  const harvest = activeCount(state, 'harvest') > 0;
  add('harvest', 'Harvest fair', harvest ? cfg.harvest : 0, harvest ? 'Harvest fair in the valley' : 'No harvest fair');
  const plague = plagueOn(state);
  add('plague', 'Plague fear', plague ? cfg.plague : 0, plague ? 'Plague in the valley' : 'No plague');
  const wins = activeCount(state, 'raidWin');
  const losses = activeCount(state, 'raidLoss');
  add('raid', 'Raids', wins * cfg.raidWin + losses * cfg.raidLoss,
    wins + losses === 0 ? 'No recent raids' : `${wins} repelled and ${losses} suffered recently`);
  const scare = activeCount(state, 'fireScare') > 0;
  add('fire', 'Fire scare', scare ? cfg.fireScare : 0, scare ? 'Recent fire' : 'No fire scare');
  const drought = activeCount(state, 'drought') > 0;
  add('drought', 'Drought', drought ? cfg.drought : 0, drought ? 'Drought in the valley' : 'No drought');
  const draft = policies.draftRate;
  add('draft', 'Conscription', draft === 'light' ? cfg.draft.light : draft === 'full' ? cfg.draft.full : 0, `Draft: ${draft}`);
  add('cold', 'No firewood', state.flags.cold ? cfg.cold : 0, state.flags.cold ? 'Winter with no firewood' : 'Firewood is in');
  add('debt', 'Treasury short', state.flags.debt ? cfg.debt : 0, state.flags.debt ? "Today's upkeep was not paid" : 'Upkeep paid');
  let total = P.happiness.base;
  for (const c of causes) total += c.value;
  return { target: Math.min(P.happiness.max, Math.max(P.happiness.min, total)), causes };
}

// Section 8.12: happiness moves a quarter of the way to target; exodus counts days under 10.
export function happinessDay(state, events) {
  const { target, causes } = computeHappiness(state);
  const hp = P.happiness;
  const next = state.happiness + (target - state.happiness) * hp.smoothing;
  state.happiness = Math.min(hp.max, Math.max(hp.min, next));
  state.happinessTarget = target;
  state.happinessCauses = causes;
  state.exodusDays = state.happiness < P.exodus.happy ? state.exodusDays + 1 : 0;
  if (state.exodusDays === P.exodus.warnDays) {
    emit(state, events, { type: 'exodusWarning', kind: 'warn', text: `The people are leaving: happiness has been under ${P.exodus.happy} for ${P.exodus.warnDays} days.` });
  }
}

// Section 8.11 aging: every citizen gains a day; children who reach the adult age are reported once.
export function agingDay(state, events) {
  const boundary = P.childUntilYears * YEAR;
  let ofAge = 0;
  for (const c of state.citizens) {
    c.ageDays += 1;
    if (c.ageDays === boundary) ofAge += 1;
  }
  if (ofAge > 0) {
    emit(state, events, { type: 'comeOfAge', kind: 'info', amount: ofAge, text: `${ofAge} ${ofAge === 1 ? 'child has' : 'children have'} come of age.` });
  }
}

// Removes a citizen and updates the death stats and ledger. Emits nothing itself: deathsDay reports one event per
// cause per day, and events.js reports fire and raid deaths in its own events. `events` keeps the section 3.7 signature.
export function killCitizen(state, citizenId, cause, events) {
  const i = state.citizens.findIndex((c) => c.id === citizenId);
  if (i < 0 || !Object.prototype.hasOwnProperty.call(DEATH_STAT, cause)) return false;
  state.citizens.splice(i, 1);
  state.stats.died += 1;
  state.stats[DEATH_STAT[cause]] += 1;
  state.ledger.died += 1;
  return true;
}

// Section 8.11 deaths, per citizen in ascending id: natural (annual / 48), then famine, then plague.
export function deathsDay(state, events) {
  const winter = seasonOf(state.day) === WINTER;
  const famine = state.flags.famine;
  const plague = plagueOn(state);
  const byId = new Map(state.buildings.map((b) => [b.id, b]));
  const wells = state.buildings.filter((b) => b.type === 'well' && b.stage === 'complete');
  const clinic = staffedCount(state, 'clinic') > 0;
  const killed = { age: 0, famine: 0, plague: 0 };
  for (const id of state.citizens.map((c) => c.id)) {
    const c = citizenById(state, id);
    if (c === null) continue;
    const cohort = cohortOf(c.ageDays);
    let annual = hazardAt(Math.floor(c.ageDays / YEAR));
    if (cohort === 'elder' && winter) annual *= P.elderWinterFactor;
    if (annual > 0 && chance(state, annual / YEAR)) {
      killCitizen(state, id, 'age', events);
      killed.age += 1;
      continue;
    }
    if (famine) {
      const p = P.famineDeathRate * (1 - state.flags.fedFrac) * (cohort === 'adult' ? 1 : P.famineVulnerableFactor);
      if (p > 0 && chance(state, p)) {
        killCitizen(state, id, 'famine', events);
        killed.famine += 1;
        continue;
      }
    }
    if (plague) {
      let p = P.plagueDeathRate * (cohort === 'child' ? P.plagueChildFactor : cohort === 'elder' ? P.plagueElderFactor : 1);
      if (c.homeId !== 0 && nearWell(byId.get(c.homeId), wells)) p *= P.plagueWellFactor;
      if (clinic) p *= P.plagueClinicFactor;
      if (chance(state, p)) {
        killCitizen(state, id, 'plague', events);
        killed.plague += 1;
      }
    }
  }
  const lines = { age: 'Natural causes took', famine: 'Hunger took', plague: 'Plague took' };
  for (const cause of ['age', 'famine', 'plague']) {
    if (killed[cause] > 0) {
      emit(state, events, { type: 'citizenDied', kind: 'bad', amount: killed[cause], text: `${lines[cause]} ${killed[cause]}.` });
    }
  }
}

// Section 8.11 births: each dwelling in ascending id, two fertile adults, a free bed, cooldown 0 and no famine.
export function birthsDay(state, events) {
  const season = seasonOf(state.day);
  const plague = plagueOn(state);
  const mood = moodFactor(state.happiness);
  let born = 0;
  for (const b of state.buildings) {
    if (!isDwelling(b)) continue;
    if (b.cooldown > 0) b.cooldown -= 1;
    if (b.cooldown !== 0 || state.flags.famine) continue;
    const living = state.citizens.filter((c) => c.homeId === b.id);
    if (living.filter(isFertile).length < 2 || dwellingFreeBeds(state, b) < 1) continue;
    let p = P.birthBase * P.birthSeason[season] * mood;
    if (plague) p *= P.birthPlagueFactor;
    if (chance(state, p)) {
      addCitizen(state, 0, b.id);
      b.cooldown = P.birthCooldown;
      born += 1;
    }
  }
  if (born > 0) {
    state.stats.born += born;
    state.ledger.born += born;
    emit(state, events, { type: 'citizenBorn', kind: 'good', amount: born, text: born === 1 ? 'A child was born.' : `${born} children were born.` });
  }
  state.stats.peakPopulation = Math.max(state.stats.peakPopulation, state.citizens.length);
}

// The complete dwelling with the most free beds; ties go to the lower id (buildings are in ascending id order).
function bestDwelling(state) {
  const counts = residentCounts(state);
  let best = null;
  let bestFree = 0;
  for (const b of state.buildings) {
    if (!isDwelling(b)) continue;
    const free = BUILDINGS[b.type].beds - (counts.get(b.id) ?? 0);
    if (free > bestFree) {
      best = b;
      bestFree = free;
    }
  }
  return best;
}

// A group of 1, 2 or 3 newcomers, trimmed to the free beds. Groups of two or more may include children.
function immigrate(state, events, room) {
  const im = P.immigration;
  const roll = rand(state);
  const size = roll < im.groupWeights[0] ? 1 : roll < im.groupWeights[1] ? 2 : 3;
  const group = Math.min(size, room);
  let arrived = 0;
  for (let k = 0; k < group; k += 1) {
    const child = size >= 2 && chance(state, im.childChance);
    const span = child ? im.childYears : im.adultYears;
    const ageDays = randInt(state, span[0] * YEAR, span[1] * YEAR + YEAR - 1);
    const home = bestDwelling(state);
    if (home === null) break;
    addCitizen(state, ageDays, home.id);
    arrived += 1;
  }
  if (arrived > 0) {
    state.stats.immigrated += arrived;
    state.ledger.arrived += arrived;
    state.stats.peakPopulation = Math.max(state.stats.peakPopulation, state.citizens.length);
    emit(state, events, { type: 'immigration', kind: 'good', amount: arrived, text: arrived === 1 ? 'A newcomer arrives.' : `${arrived} newcomers arrive.` });
  }
}

// One citizen leaves: a random homeless person first, then a random unemployed adult, then anyone.
function emigrate(state, events) {
  if (state.citizens.length === 0) return;
  const homeless = state.citizens.filter((c) => c.homeId === 0);
  const idle = state.citizens.filter((c) => isEligible(c) && c.workId === 0);
  const who = pick(state, homeless.length > 0 ? homeless : idle.length > 0 ? idle : state.citizens);
  state.citizens.splice(state.citizens.indexOf(who), 1);
  state.stats.emigrated += 1;
  emit(state, events, { type: 'emigration', kind: 'warn', id: who.id, text: `${who.name} left the valley.` });
}

// Section 8.11 migration: immigration when happy and well fed, emigration below 35.
export function migrationDay(state, events) {
  const im = P.immigration;
  const happy = state.happiness;
  if (happy >= im.minHappy && !plagueOn(state) && state.stock.food >= im.foodCoverDays * foodDemand(state)) {
    const room = populationSummary(state).freeBeds;
    if (room > 0 && chance(state, Math.min(im.max, (happy - im.minHappy) * im.perPoint))) immigrate(state, events, room);
  }
  if (happy < P.emigration.belowHappy) {
    const belowBy = P.emigration.belowHappy - happy;
    if (chance(state, P.emigration.base * belowBy / P.emigration.belowHappy)) emigrate(state, events);
  }
}

// Section 8.11 militia: the draft target follows the policy share; surplus is released (highest id first),
// and up to recruitPerDay adults are drafted (lowest id first) while iron pays for each recruit.
export function militiaDay(state, events) {
  const m = P.militia;
  const eligible = state.citizens.filter(isEligible);
  const target = Math.floor(m.share[state.policies.draftRate] * eligible.length);
  const drafted = state.citizens.filter((c) => c.militia);
  if (drafted.length > target) {
    for (const c of drafted.sort((a, b) => b.id - a.id).slice(0, drafted.length - target)) c.militia = false;
    return;
  }
  const need = target - drafted.length;
  const limit = Math.min(m.recruitPerDay, need);
  let recruits = 0;
  for (const c of eligible) {
    if (recruits >= limit || state.stock.iron < m.ironPerRecruit) break;
    c.militia = true;
    state.stock.iron -= m.ironPerRecruit;
    state.ledger.consumed.iron += m.ironPerRecruit;
    recruits += 1;
  }
  if (recruits > 0) {
    emit(state, events, { type: 'militia', kind: 'info', amount: recruits, text: `${recruits} ${recruits === 1 ? 'citizen' : 'citizens'} drafted into the militia.` });
  }
  if (recruits < need && state.stock.iron < m.ironPerRecruit && state.day % STALL_WARN_EVERY === 0) {
    emit(state, events, { type: 'stall', kind: 'warn', text: `The militia draft is stalled: each recruit needs ${m.ironPerRecruit} iron.` });
  }
}

// Section 8.11 homeless move-in: up to homelessMovePerDay people, ascending id, into the first free bed.
export function homelessDay(state, events) {
  let moved = 0;
  for (const c of state.citizens) {
    if (moved >= P.homelessMovePerDay) break;
    if (c.homeId !== 0) continue;
    const home = state.buildings.find((b) => isDwelling(b) && dwellingFreeBeds(state, b) > 0);
    if (home === undefined) break;
    c.homeId = home.id;
    moved += 1;
  }
  if (moved > 0) {
    emit(state, events, { type: 'moveIn', kind: 'good', amount: moved, text: `${moved} ${moved === 1 ? 'person moves' : 'people move'} in.` });
  }
}

// A citizen with the next id, aged to the typical start age of the cohort. Name comes from NAMES unless given.
export function newCitizen(state, cohort, homeId, name) {
  const years = TYPICAL_YEARS[cohort] ?? TYPICAL_YEARS.adult;
  return addCitizen(state, years * YEAR, homeId, name);
}
