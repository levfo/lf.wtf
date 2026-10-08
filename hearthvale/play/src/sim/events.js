// owner: events
// Section 3.8 and sections 8.1 to 8.10: weather, season marks, plague, floods, droughts, raids, fires, caravans,
// the harvest fair, and the festival command (section 6.2). Pure: no browser globals, no clock, no random source.
import { TIME } from '../config/index.js';
import { EVENTS } from '../config/events.js';
import { ECONOMY } from '../config/economy.js';
import { RESOURCES, TRADE_KEYS } from '../config/resources.js';
import { BUILDINGS } from '../config/buildings.js';
import { POPULATION } from '../config/population.js';
import { emit } from './state.js';
import { rand, randInt, pick, chance } from './rng.js';
import { killCitizen } from './population.js';
import { spend } from './economy.js';

const AUTUMN = 2; // season index of autumn (section 5.1)
const WINTER = 3; // season index of winter (section 5.1)
const AUTUMN_NO_FARM = 'Autumn begins. No finished Farm yet: build one, or set Rations to Half (Kingdom > Policies), before winter.';
const WEATHER_ORDER = ['clear', 'rain', 'storm', 'snow']; // roll order of section 8.1 b
const WEATHER_TEXT = {
  clear: 'The skies clear.', rain: 'Rain begins to fall.', storm: 'A storm rolls in.', snow: 'Snow begins to fall.',
};
const DWELLINGS = ['cottage', 'townhouse'];
const CARAVAN_OFFERS = 2; // two offers per caravan (section 4.6)
// Raids moved out of winter land on spring days 0 to 4 (section 5.7). No config key holds this offset yet.
const SPRING_LANDING_JITTER = 4;

const seasonOf = (day) => Math.floor((day % TIME.daysPerYear) / TIME.daysPerSeason);
const dayOfSeason = (day) => day % TIME.daysPerSeason;
const completeOf = (state, type) => state.buildings.filter((b) => b.type === type && b.stage === 'complete');
const staffedOf = (state, type) => completeOf(state, type).filter((b) => b.crew >= 1);
const residentsOf = (state, homeId) => state.citizens.filter((c) => c.homeId === homeId);

function addEffect(state, kind, until, value) {
  state.effects.push({ id: state.nextEffectId, kind, until, value });
  state.nextEffectId += 1;
}

// First effect of this kind that is still running (until > day), or null.
export function activeEffect(state, kind) {
  for (const e of state.effects) if (e.kind === kind && e.until > state.day) return e;
  return null;
}

// Section 8.1: the daily event steps, in order.
export function dailyEvents(state, events) {
  effectsDay(state, events);
  weatherDay(state, events);
  seasonMark(state, events);
  plagueDay(state, events);
  floodDay(state, events);
  droughtDay(state, events);
  raidDay(state, events);
  fireDay(state, events);
  caravanDay(state, events);
  harvestFairDay(state, events);
}

// Section 8.1 a: removes effects whose until day has come. An ending drought says so; the other kinds end quietly.
export function effectsDay(state, events) {
  const keep = [];
  for (const e of state.effects) {
    if (e.until > state.day) keep.push(e);
    else if (e.kind === 'drought') emit(state, events, { type: 'droughtEnd', kind: 'info', text: 'The drought has ended.' });
  }
  state.effects.splice(0, state.effects.length, ...keep);
}

// One weighted roll (one rand) over the season's weights, walking the keys in canonical order.
function rollWeather(state, season) {
  const w = EVENTS.weather.seasonWeights[season];
  const total = WEATHER_ORDER.reduce((sum, k) => sum + (w[k] || 0), 0);
  const roll = rand(state) * total;
  let acc = 0;
  let last = 'clear';
  for (const k of WEATHER_ORDER) {
    const weight = w[k] || 0;
    if (weight <= 0) continue;
    acc += weight;
    last = k;
    if (roll < acc) return k;
  }
  return last;
}

// Section 8.1 b: when the weather's time runs out, roll a new kind and a new duration of 2 to 4 days.
export function weatherDay(state, events) {
  const w = state.weather;
  if (state.day < w.untilDay) return;
  const kind = rollWeather(state, seasonOf(state.day));
  w.untilDay = state.day + EVENTS.weather.minDays + randInt(state, 0, EVENTS.weather.extraDays - 1);
  if (kind === w.kind) return;
  w.kind = kind;
  state.rev.weather += 1;
  emit(state, events, { type: 'weather', kind: 'info', text: WEATHER_TEXT[kind] });
}

// Section 8.1 c: the first day of each season. Autumn with no finished Farm warns and names the fix.
function seasonMark(state, events) {
  if (dayOfSeason(state.day) !== 0) return;
  const season = seasonOf(state.day);
  if (season === AUTUMN && completeOf(state, 'farm').length === 0) {
    emit(state, events, { type: 'season', kind: 'warn', text: AUTUMN_NO_FARM });
    return;
  }
  const text = season === 0
    ? `Spring begins. Year ${Math.floor(state.day / TIME.daysPerYear) + 1}.`
    : `${TIME.seasonNames[season]} begins.`;
  emit(state, events, { type: 'season', kind: 'good', text });
}

// Section 8.5: the plague is warned, starts, and ends. Only one plague is pending or running at a time.
export function plagueDay(state, events) {
  const s = state.schedule;
  const P = EVENTS.plague;
  const day = state.day;
  if (s.plagueStart >= 0 && day >= s.plagueUntil) {
    const deaths = state.stats.plagueDeaths - s.plagueDeathBase;
    if (deaths < P.mendingFrac * s.plaguePopStart) s.plagueMendingDay = day;
    emit(state, events, { type: 'plagueEnd', kind: 'good', text: `The plague passed. ${deaths} died.` });
    s.plagueNextAllowed = s.plagueUntil + P.cooldownDays;
    s.plagueStart = -1;
    s.plagueUntil = -1;
    return;
  }
  if (s.plagueStart >= 0 && day === s.plagueStart) {
    state.stats.plagues += 1;
    emit(state, events, { type: 'plagueStart', kind: 'bad', text: 'The plague has reached the valley.' });
    return;
  }
  if (s.plagueStart >= 0) return; // already warned or running
  if (day < s.plagueNextAllowed || day < P.startDay || state.citizens.length < P.minPop) return;
  if (!chance(state, P.chanceBySeason[seasonOf(day)])) return;
  s.plagueStart = day + P.warnDays;
  s.plagueUntil = s.plagueStart + P.durationDays;
  s.plaguePopStart = state.citizens.length;
  s.plagueDeathBase = state.stats.plagueDeaths;
  emit(state, events, { type: 'plagueWarning', kind: 'warn', text: `Sickness is near. Plague arrives in ${P.warnDays} days.` });
}

// Removes one random bridge (road 2) from the map, with its road tile gone. Returns false when there is none.
function washBridge(state) {
  const bridges = [];
  for (let i = 0; i < state.map.road.length; i += 1) if (state.map.road[i] === 2) bridges.push(i);
  if (bridges.length === 0) return false;
  state.map.road[pick(state, bridges)] = 0;
  state.rev.map += 1;
  return true;
}

// Section 8.6: floods come in spring, after a warning, and can wash out a bridge.
export function floodDay(state, events) {
  const s = state.schedule;
  const F = EVENTS.flood;
  const day = state.day;
  if (s.floodStart >= 0 && day === s.floodStart) {
    addEffect(state, 'flood', day + F.durationDays, 0);
    state.stats.floods += 1;
    const washed = chance(state, ECONOMY.floodBridgeWashChance) && washBridge(state);
    s.floodStart = -1;
    const text = washed ? 'The river flooded the riverside fields. A bridge washed out.' : 'The river flooded the riverside fields.';
    emit(state, events, { type: 'flood', kind: 'bad', text });
    return;
  }
  if (s.floodStart >= 0 || activeEffect(state, 'flood')) return; // warned or running
  if (seasonOf(day) !== F.season || day < F.startDay || state.citizens.length < F.minPop) return;
  if (!chance(state, F.chance)) return;
  s.floodStart = day + F.warnDays;
  emit(state, events, { type: 'floodWarning', kind: 'warn', text: 'The river is rising.' });
}

// Section 8.6: droughts come in summer, after a one-day warning.
export function droughtDay(state, events) {
  const s = state.schedule;
  const D = EVENTS.drought;
  const day = state.day;
  if (s.droughtStart >= 0 && day === s.droughtStart) {
    addEffect(state, 'drought', day + D.durationDays, 0);
    state.stats.droughts += 1;
    s.droughtStart = -1;
    emit(state, events, { type: 'drought', kind: 'warn', text: 'A drought has begun. Farms yield less.' });
    return;
  }
  if (s.droughtStart >= 0 || activeEffect(state, 'drought')) return; // warned or running
  if (seasonOf(day) !== D.season || day < D.startDay || !chance(state, D.chance)) return;
  s.droughtStart = day + D.warnDays;
  emit(state, events, { type: 'droughtWarning', kind: 'warn', text: 'The sky is brass.' });
}

// Section 5.7: raid strength for a day, min(strengthMax, strengthBase + floor(day / strengthEvery)).
export function raidStrengthFor(day) {
  const R = EVENTS.raid;
  return Math.min(R.strengthMax, R.strengthBase + Math.floor(day / R.strengthEvery));
}

// Section 5.7: militia plus staffed watchtowers (up to towerMax) and staffed barracks (up to barracksMax).
export function defenceOf(state) {
  const R = EVENTS.raid;
  const militia = state.citizens.filter((c) => c.militia).length;
  const towers = Math.min(R.towerMax, staffedOf(state, 'watchtower').length);
  const barracks = Math.min(R.barracksMax, staffedOf(state, 'barracks').length);
  return militia + R.towerDefence * towers + R.barracksDefence * barracks;
}

// Section 5.7: repelled when defence reaches the strength; otherwise the difference is unmet.
export function raidOutcome(defence, strength) {
  return { repelled: defence >= strength, unmet: Math.max(0, strength - defence) };
}

// Section 5.7: one stock, chosen by rand, loses min(lootMax, lootPerUnmet * unmet) of itself, floored.
function loot(state, unmet) {
  const R = EVENTS.raid;
  const kind = pick(state, R.lootKinds);
  const share = Math.min(R.lootMax, R.lootPerUnmet * unmet);
  const lost = Math.floor(state.stock[kind] * share);
  state.stock[kind] -= lost;
  state.ledger.lost[kind] += lost;
  return { kind, lost };
}

// Section 5.7: non-militia citizens chosen by rand die. Returns how many died.
function casualties(state, count, events) {
  const pool = state.citizens.filter((c) => !c.militia);
  let deaths = 0;
  for (let n = 0; n < count && pool.length > 0; n += 1) {
    const at = randInt(state, 0, pool.length - 1);
    const [victim] = pool.splice(at, 1);
    if (killCitizen(state, victim.id, 'raid', events)) deaths += 1;
  }
  return deaths;
}

// Section 8.7: the next raid is 24 to 34 days on; one that lands in winter moves to early spring.
function scheduleNextRaid(state) {
  const s = state.schedule;
  const R = EVENTS.raid;
  let next = s.raidDay + randInt(state, R.gapMin, R.gapMax);
  if (seasonOf(next) === WINTER) {
    next = (Math.floor(next / TIME.daysPerYear) + 1) * TIME.daysPerYear + randInt(state, 0, SPRING_LANDING_JITTER);
  }
  s.raidDay = next;
  s.raidStrength = raidStrengthFor(next);
  s.raidWarnedDay = -1;
}

// Section 8.7: applies the outcome of the scheduled raid, then schedules the next one.
export function resolveRaid(state, events) {
  const s = state.schedule;
  const R = EVENTS.raid;
  const C = POPULATION.causes;
  const strength = s.raidStrength;
  const defence = defenceOf(state);
  const out = raidOutcome(defence, strength);
  if (out.repelled) {
    state.stats.raidsRepelled += 1;
    addEffect(state, 'raidWin', state.day + R.winDays, C.raidWin);
    emit(state, events, { type: 'raid', kind: 'good', text: `Raid repelled: ${strength} bandits met defence ${defence}.` });
  } else {
    state.stats.raidsLost += 1;
    addEffect(state, 'raidLoss', state.day + R.lossDays, C.raidLoss);
    const { kind, lost } = loot(state, out.unmet);
    const deaths = casualties(state, Math.floor(out.unmet * R.casualtiesPerUnmet), events);
    if (deaths > 0) state.rev.citizens += 1;
    emit(state, events, {
      type: 'raid',
      kind: 'bad',
      text: `Raid! ${strength} bandits met defence ${defence}: ${lost} ${RESOURCES[kind].name.toLowerCase()} stolen, ${deaths} died.`,
      resource: kind,
      amount: lost,
    });
  }
  scheduleNextRaid(state);
}

// Section 8.7 (R2-04 b): with no defence and no Watchtower staffed or under construction, the warning names the build
// time. A Watchtower started now is too late for a raid fewer days away than that.
function watchtowerFix(state, untilRaid) {
  const W = BUILDINGS.watchtower;
  const underWay = state.buildings.some((b) => b.type === 'watchtower' && b.stage === 'building');
  if (underWay || staffedOf(state, 'watchtower').length > 0) return '';
  const build = `${W.days} ${W.days === 1 ? 'day' : 'days'}`;
  return untilRaid < W.days
    ? ` A Watchtower takes ${build}: too late for this raid.`
    : ` A Watchtower takes ${build}: start one now. It needs a road.`;
}

// Section 8.7 (R2-04 e): a fall in defence since the previous day logs one warning. The value is kept every day.
function defenceDrop(state, events) {
  const s = state.schedule;
  const now = defenceOf(state);
  if (now < s.lastDefence) {
    emit(state, events, { type: 'defenceWarning', kind: 'warn', text: `Defence fell from ${s.lastDefence} to ${now}.` });
  }
  s.lastDefence = now;
}

// Section 8.7: warnings two days ahead with a staffed watchtower, one day ahead without; then the raid resolves.
// untilRaid counts the days the player sees after this tick (runDay adds the day after the events, and the top-left
// raid line counts the same way), so the riders line and that line give the same number.
export function raidDay(state, events) {
  const s = state.schedule;
  const R = EVENTS.raid;
  const day = state.day;
  const untilRaid = s.raidDay - (day + 1);
  const towered = staffedOf(state, 'watchtower').length > 0;
  defenceDrop(state, events);
  if ((untilRaid === R.warnWithTower && towered) || (untilRaid === R.warnWithout && s.raidWarnedDay < 0)) {
    s.raidWarnedDay = day;
    const unit = untilRaid === 1 ? 'day' : 'days';
    const defence = defenceOf(state);
    // With no defence at all, the warning also names the build time of a watchtower (watchtowerFix).
    const fix = defence === 0 ? watchtowerFix(state, untilRaid) : '';
    emit(state, events, {
      type: 'raidWarning',
      kind: 'warn',
      text: `Riders spotted: raid in ${untilRaid} ${unit}, strength ${s.raidStrength}. Defence ${defence}.${fix}`,
    });
  }
  if (day === s.raidDay) resolveRaid(state, events);
}

// Centre-to-centre Chebyshev distance, compared in half tiles so that 2 by 2 footprints stay exact.
function centreWithin(a, b, radius) {
  const dx = Math.abs((2 * a.x + a.w - 1) - (2 * b.x + b.w - 1));
  const dy = Math.abs((2 * a.y + a.h - 1) - (2 * b.y + b.h - 1));
  return Math.max(dx, dy) <= 2 * radius;
}

// Section 8.8: the home is removed from the map, its residents face the fire, and survivors lose their bed.
function burn(state, events, home) {
  const F = EVENTS.fire;
  const P = POPULATION;
  for (let dy = 0; dy < home.h; dy += 1) {
    for (let dx = 0; dx < home.w; dx += 1) {
      const i = (home.y + dy) * state.width + home.x + dx;
      if (state.map.building[i] === home.id) state.map.building[i] = 0;
    }
  }
  const at = state.buildings.indexOf(home);
  if (at >= 0) state.buildings.splice(at, 1);
  state.rev.map += 1;
  state.rev.buildings += 1;
  emit(state, events, {
    type: 'buildingDestroyed', kind: 'bad', text: `${BUILDINGS[home.type].name} burned down.`, x: home.x, y: home.y, id: home.id,
  });
  let deaths = 0;
  for (const c of residentsOf(state, home.id)) {
    if (chance(state, P.fireDeathChance) && killCitizen(state, c.id, 'fire', events)) deaths += 1;
    else c.homeId = 0;
  }
  state.rev.citizens += 1;
  state.stats.fires += 1;
  addEffect(state, 'fireScare', state.day + F.scareDays, P.causes.fireScare);
  const text = deaths > 0 ? `A fire destroyed a home. ${deaths} died.` : 'A fire destroyed a home. Everyone got out.';
  emit(state, events, { type: 'fire', kind: 'bad', text, x: home.x, y: home.y, id: home.id, amount: deaths });
}

// Section 8.8: from day 15, a chance each day (higher in winter) when three or more homes are occupied. Fire risk turns
// high on the first day of winter (section 7.8), and that day emits one warning that names the Well rule (R2-04 c).
export function fireDay(state, events) {
  const F = EVENTS.fire;
  const day = state.day;
  if (seasonOf(day) === WINTER && dayOfSeason(day) === 0) {
    emit(state, events, {
      type: 'season',
      kind: 'warn',
      text: `Fire risk is high this winter. A Well within ${F.containRadius} tiles of the homes puts out most fires (Build > Services).`,
    });
  }
  if (day < F.startDay) return;
  const homes = state.buildings.filter((b) => b.stage === 'complete' && DWELLINGS.includes(b.type) && residentsOf(state, b.id).length > 0);
  if (homes.length < F.minDwellings) return;
  if (!chance(state, seasonOf(day) === WINTER ? F.winterChance : F.chance)) return;
  const home = pick(state, homes);
  const well = completeOf(state, 'well').find((w) => centreWithin(home, w, F.containRadius));
  if (well && chance(state, F.containChance)) {
    emit(state, events, { type: 'fireContained', kind: 'good', text: 'A well put out a fire.', x: home.x, y: home.y, id: home.id });
    return;
  }
  burn(state, events, home);
}

// Section 8.9: an offer expires on its expires day. With a staffed Market, caravans arrive every 10 to 16 days.
export function caravanDay(state, events) {
  const day = state.day;
  state.offers = state.offers.filter((o) => day < o.expires);
  const markets = staffedOf(state, 'market').length;
  if (state.nextCaravanDay === -1 && markets > 0) state.nextCaravanDay = day + ECONOMY.caravanFirstDays;
  if (markets === 0 || state.citizens.length < ECONOMY.caravanMinPop || day < state.nextCaravanDay || state.offers.length > 0) return;
  for (let n = 0; n < CARAVAN_OFFERS; n += 1) {
    const kind = pick(state, ['sell', 'buy']);
    const resource = pick(state, TRADE_KEYS);
    const amount = pick(state, ECONOMY.caravanAmounts);
    const base = RESOURCES[resource].base;
    const unitPrice = kind === 'sell'
      ? Math.max(1, Math.round(base * ECONOMY.caravanSellFactor))
      : Math.round(base * ECONOMY.caravanBuyFactor);
    state.offers.push({ id: state.nextOfferId, kind, resource, amount, unitPrice, expires: day + ECONOMY.caravanOfferDays });
    state.nextOfferId += 1;
  }
  state.nextCaravanDay = day + randInt(state, ECONOMY.caravanGapMin, ECONOMY.caravanGapMax);
  state.stats.caravans += 1;
  emit(state, events, { type: 'caravan', kind: 'good', text: 'A caravan arrived with offers.' });
}

// Section 8.10: the harvest fair on autumn day 6 (index 5), when a finished Tavern stands.
export function harvestFairDay(state, events) {
  const H = EVENTS.harvestFair;
  if (seasonOf(state.day) !== H.season || dayOfSeason(state.day) !== H.dayOfSeason) return;
  if (completeOf(state, 'tavern').length === 0) return;
  addEffect(state, 'harvest', state.day + H.durationDays, H.happy);
  emit(state, events, {
    type: 'harvestFair', kind: 'good', text: `The harvest fair opens. Happiness +${H.happy} for ${H.durationDays} days.`,
  });
}

// Section 6.2 festival row. The controller creates the festival event (section 7.9), so no event is emitted here.
export function startFestival(state, events) {
  const F = EVENTS.festival;
  if (completeOf(state, 'tavern').length === 0) return { ok: false, reason: 'A festival needs a finished Tavern' };
  const since = state.day - state.festivalDay;
  if (since < F.cooldownDays) {
    const wait = F.cooldownDays - since;
    return { ok: false, reason: `Festivals are ${F.cooldownDays} days apart. Wait ${wait} more day${wait === 1 ? '' : 's'}` };
  }
  const reason = spend(state, F.cost);
  if (reason) return { ok: false, reason };
  state.festivalDay = state.day;
  addEffect(state, 'festival', state.day + F.durationDays, F.happy);
  return { ok: true, reason: null, message: `The festival lifts spirits: +${F.happy} happiness for ${F.durationDays} days.` };
}
