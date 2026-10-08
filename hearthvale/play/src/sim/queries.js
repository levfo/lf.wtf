// owner: core
// Section 3.11 and section 7: every get*View and suggestSite. Read-only: views are plain objects built on each call.
import { BUILDINGS, BUILDING_KEYS } from '../config/buildings.js';
import { RESOURCES, RESOURCE_KEYS, TRADE_KEYS } from '../config/resources.js';
import { ECONOMY, UPGRADES } from '../config/economy.js';
import { EVENTS } from '../config/events.js';
import { MILESTONES, TUTORIAL } from '../config/milestones.js';
import { TIERS } from '../config/tiers.js';
import { MAP } from '../config/map.js';
import { TIME } from '../config/index.js';
import { TERRAIN, TERRAIN_NAME, idx, inBounds, buildingById } from './state.js';
import { footprintOf, neighbours4, planRoad, isRoadable, resourceTilesNear, connectedRoadCount } from './world.js';
import { storageCap, canAfford, quotePrice, haulFactor, seasonFactor, weatherFactor, upgradeFactor,
  farmFertility } from './economy.js';
import { populationSummary, foodDemand, cohortOf } from './population.js';
import { activeEffect, defenceOf } from './events.js';
import { tierChecks, tutorialStatus } from './progress.js';
import { validatePlacement, validateRoadPoints } from './commands.js';

const round1 = (v) => Math.round(v * 10) / 10;
// One decimal, with a whole number shown without ".0" (section 7.4: "Working: 7 food a day").
const fmtAmount = (v) => (Number.isInteger(round1(v)) ? String(Math.round(v)) : round1(v).toFixed(1));
const seasonIndex = (day) => Math.floor((day % TIME.daysPerYear) / TIME.daysPerSeason);
const yearOf = (day) => Math.floor(day / TIME.daysPerYear) + 1;
const tilesOf = (b) => footprintOf(b.type, b.x, b.y, b.rot).tiles;
const NAMES_MAX = 8;
const SITE_RANGE = 16; // section 3.11: suggestion range around the Hall door (no config key)
// Build menu tab of each category (buildMenu.js), for the "(Build > Housing)" wording of the goal line (section 7.7).
const TAB_NAME = { housing: 'Housing', food: 'Food', materials: 'Materials', crafts: 'Crafts', services: 'Services',
  defence: 'Defence', special: 'Special' };

// Names of the first NAMES_MAX citizens in list.
const namesOf = (list) => list.slice(0, NAMES_MAX).map((c) => c.name);

// Output of a producer on full crew, before factors (section 7.4). Null for non-producers.
function outputOf(state, b, def) {
  if (def.produces) {
    const fert = def.needs?.kind === 'farm' ? farmFertility(state, tilesOf(b)) : 1;
    return { resource: def.produces.resource, perDayFull: def.produces.perDay * fert };
  }
  if (def.recipe) return { resource: 'goods', perDayFull: def.recipe.out.goods * def.recipe.batchesPerDay };
  return null;
}

// Factors of section 5.4 for one building right now. efficiency is 0 for non-producers.
function factorsOf(state, b, def, out) {
  const crew = def.crew > 0 ? b.crew / def.crew : 0;
  const haul = haulFactor(b.roadSteps);
  const season = seasonFactor(b.type, seasonIndex(state.day));
  const weather = weatherFactor(state.weather.kind, b.type);
  const upgrade = upgradeFactor(state, b.type);
  const efficiency = out ? crew * haul * season * weather * upgrade : 0;
  return { factors: { crew, haul, season, weather, upgrade }, efficiency };
}

// First matching status of section 7.4. Returns [status, statusText].
function statusOf(state, b, def, out, eff) {
  if (b.stage === 'building') {
    const who = b.builders === 0 ? ' (waiting for builders)' : ` (${b.builders} builders)`;
    return ['building', `Under construction: ${Math.floor(b.progress * 100)}%${who}`];
  }
  if (b.priority === 'paused') return ['paused', 'Paused by you. Upkeep still due.'];
  if (!b.connected) return ['noRoad', 'Idle: no road connection to the Town Hall.'];
  const need = def.needs;
  if (need?.kind === 'terrain' && resourceTilesNear(state, tilesOf(b), need.radius, TERRAIN[need.terrain.toUpperCase()]).length === 0) {
    return ['noResource', `Idle: no ${need.terrain} left within ${need.radius} tiles.`];
  }
  if (def.recipe && (state.stock.wood < def.recipe.in.wood || state.stock.iron < def.recipe.in.iron)) {
    return ['noInput', `Idle: needs ${def.recipe.in.wood} wood and ${def.recipe.in.iron} iron in stock.`];
  }
  if (def.crew > 0 && b.crew === 0) return ['noCrew', 'Idle: no workers. Workers are assigned at dawn.'];
  if (out) {
    if (b.crew < def.crew) return ['working', `Working at ${Math.round((100 * b.crew) / def.crew)}% crew (${b.crew} of ${def.crew}).`];
    return ['working', `Working: ${fmtAmount(out.perDayFull * eff)} ${out.resource} a day.`];
  }
  return ['ready', def.readyText];
}

// Upgrade rows shared by the building and kingdom views (section 7.4 and 7.8).
function upgradeRows(state, filter) {
  return Object.keys(UPGRADES).filter(filter).map((key) => {
    const u = UPGRADES[key];
    const owned = state.upgrades[key] === true;
    let reason = null;
    if (owned) reason = 'Already bought';
    else if (u.tier > state.tier) reason = `Needs the ${TIERS[u.tier].name} tier`;
    else reason = canAfford(state, u.cost);
    return { key, name: u.name, text: u.text, cost: { ...u.cost }, tier: u.tier, owned, available: reason === null && !owned, reason };
  });
}

export function getCatalog(state) {
  return BUILDING_KEYS.map((type) => {
    const def = BUILDINGS[type];
    const singleton = type === 'royalCharter' && state.buildings.some((b) => b.type === 'royalCharter');
    let lockReason = null;
    if (def.tier > state.tier) lockReason = `Unlocks at the ${TIERS[def.tier].name} tier`;
    else if (singleton) lockReason = 'The Royal Charter is already built or underway';
    return {
      type, name: def.name, category: def.category, tier: def.tier, tierName: TIERS[def.tier].name,
      unlocked: lockReason === null, lockReason, cost: { ...def.cost }, affordable: canAfford(state, def.cost) === null,
      buildDays: def.days, upkeep: def.upkeep, crew: def.crew, crewRole: def.crewRole, w: def.w, h: def.h, beds: def.beds,
      produces: def.produces ? { resource: def.produces.resource, perDay: def.produces.perDay } : null,
      tooltip: def.tooltip, needsText: def.needsText,
    };
  });
}

export function getTileView(state, x, y) {
  if (!inBounds(state, x, y)) return null;
  const i = idx(state, x, y);
  const m = state.map;
  const code = m.terrain[i];
  const bid = m.building[i];
  const bld = bid === 0 ? null : buildingById(state, bid);
  const grassy = code === TERRAIN.MEADOW || code === TERRAIN.GRASS;
  const { ok, reason } = validateRoadPoints(state, [{ x, y }]);
  const buildable = BUILDING_KEYS.filter((type) => validatePlacement(state, type, x, y, 0).ok).map((type) => BUILDINGS[type].name);
  return {
    x, y, explored: m.explored[i] === 1, terrain: TERRAIN_NAME[code], terrainCode: code, height: m.height[i] / 255,
    fertility: grassy ? farmFertility(state, [{ x, y }]) : null, deposit: m.deposit[i],
    road: m.road[i] === 0 ? 'none' : (m.road[i] === 2 ? 'bridge' : 'road'), connected: state.net.connected[i] === 1,
    buildingId: bid, buildingType: bld ? bld.type : null, buildingName: bld ? BUILDINGS[bld.type].name : null,
    canRoad: { ok, reason }, buildable,
  };
}

export function getBuildingView(state, id) {
  const b = buildingById(state, id);
  if (!b) return null;
  const def = BUILDINGS[b.type];
  const out = b.stage === 'complete' ? outputOf(state, b, def) : null;
  const { factors, efficiency } = factorsOf(state, b, def, out);
  const [status, statusText] = statusOf(state, b, def, out, efficiency);
  const working = status === 'working';
  const residents = state.citizens.filter((c) => c.homeId === b.id);
  const workers = state.citizens.filter((c) => c.workId === b.id);
  const refund = {};
  for (const k of ['wood', 'stone', 'iron', 'goods', 'gold']) refund[k] = Math.floor((def.cost[k] || 0) * ECONOMY.demolishRefund);
  const recipeIn = def.recipe ? def.recipe.in : null;
  return {
    id: b.id, type: b.type, name: def.name, category: def.category, x: b.x, y: b.y, rot: b.rot, w: b.w, h: b.h,
    stage: b.stage, progress: b.progress,
    daysLeft: b.stage === 'building' ? Math.ceil((1 - b.progress) * def.days) : 0,
    builders: b.builders, priority: b.priority, crew: b.crew, crewNeeded: def.crew, status, statusText, efficiency,
    factors,
    production: out ? { resource: out.resource, perDayFull: out.perDayFull, perDayNow: working ? out.perDayFull * efficiency : 0 } : null,
    inputs: recipeIn ? { wood: { need: recipeIn.wood, have: state.stock.wood }, iron: { need: recipeIn.iron, have: state.stock.iron } } : {},
    roadSteps: b.roadSteps, connected: b.connected,
    residents: { count: residents.length, names: namesOf(residents) },
    workers: { count: workers.length, names: namesOf(workers) },
    beds: def.beds, upkeep: def.upkeep, cost: { ...def.cost }, buildDays: def.days,
    canDemolish: b.type !== 'townHall' && b.type !== 'royalCharter', demolishRefund: refund,
    tooltip: def.tooltip, upgrades: upgradeRows(state, (key) => UPGRADES[key].target === b.type)
      .map((u) => ({ key: u.key, name: u.name, text: u.text, cost: u.cost, owned: u.owned, available: u.available, reason: u.reason })),
  };
}

export function getPlacementPreview(state, type, x, y, rot) {
  const check = validatePlacement(state, type, x, y, rot);
  const known = typeof type === 'string' && Object.prototype.hasOwnProperty.call(BUILDINGS, type);
  return { ...check, buildDays: known ? BUILDINGS[type].days : 0 };
}

export function getRoadPlan(state, toX, toY) {
  const refusal = (reason) => ({ ok: false, reason, points: [], cost: { wood: 0, stone: 0 }, bridges: 0, length: 0, costReason: null });
  if (!inBounds(state, toX, toY)) return refusal('That spot is off the map');
  const i = idx(state, toX, toY);
  const m = state.map;
  if (m.explored[i] === 0) return refusal('That tile is unexplored. Scout this area first');
  if (m.terrain[i] === TERRAIN.MOUNTAIN) return refusal('Mountains cannot carry roads');
  if (m.terrain[i] === TERRAIN.LAKE) return refusal('Lakes cannot carry roads');
  if (m.building[i] !== 0) return refusal('A building is in the way. Route the road around it.');
  if (m.road[i] !== 0) return refusal('A road is already here. Drag from empty grass.');
  const path = planRoad(state, toX, toY);
  if (path === null) return refusal('No clear route from the Town Hall');
  const bridges = path.bridges;
  const land = path.points.length - bridges;
  const cost = {
    wood: land * BUILDINGS.road.cost.wood + bridges * BUILDINGS.bridge.cost.wood,
    stone: bridges * BUILDINGS.bridge.cost.stone,
  };
  return { ok: true, reason: null, points: path.points, cost, bridges, length: path.points.length, costReason: canAfford(state, cost) };
}

const SANDBOX_GOAL = 'Sandbox goal: grow to 150 people, then keep happiness at 70 for 48 days (Golden Year).';

// The type of a step's first site marker (step 1's is the farm its gold ring marks), or null when the step has none.
function firstSiteType(step) {
  const m = step.markers.find((k) => k.startsWith('site:'));
  return m ? m.slice('site:'.length) : null;
}

// Suggested sites by type for one objective. suggestSite is the costly search, and a step can name a type twice, so each
// type is searched once.
function siteReader(state) {
  const seen = new Map();
  return (type) => {
    if (!seen.has(type)) seen.set(type, suggestSite(state, type));
    return seen.get(type);
  };
}

// World markers of a step (section 7.7): door, suggested sites, and incomplete buildings of that type.
function markersOf(state, step, siteOf) {
  const out = [];
  for (const m of step.markers) {
    if (m === 'door') {
      out.push({ x: MAP.door.x, y: MAP.door.y, kind: 'door' });
    } else if (m.startsWith('site:')) {
      const type = m.slice(5);
      const site = siteOf(type);
      if (site) out.push({ x: site.x, y: site.y, kind: 'site' });
      for (const b of state.buildings) {
        if (b.type === type && b.stage === 'building') out.push({ x: b.x, y: b.y, kind: 'target' });
      }
    }
  }
  return out;
}

// The building key a running step asks for (section 7.7): the type of its first site marker, read from the config step.
// A road step has a 'door' marker, where its road starts. It counts road tiles, not buildings, so it has no key, even
// though its road ends at a site marker. Null too when the step has no site marker.
function buildingKeyOf(step) {
  if (step.markers.includes('door')) return null;
  return firstSiteType(step);
}

// Finished buildings of one type (the count a counted step shows, as progress.js counts it).
const completeOf = (state, type) => state.buildings.filter((b) => b.type === type && b.stage === 'complete').length;

// The next line for a ring whose spot has no road link yet (section 7.7): the road comes first. Step 1 keeps its road
// count, and a counted step keeps its finished count. Both are counted as progress.js counts them (section 5.8).
function unlinkedNext(state, step, type) {
  if (step === 1) {
    const base = Number.isInteger(state.tutorialBaseline) && state.tutorialBaseline > 0 ? state.tutorialBaseline : 0;
    const need = Math.max(0, TUTORIAL.steps[0].need - base);
    const have = Math.min(need, Math.max(0, connectedRoadCount(state) - base));
    return `Next: lay a road to the gold ring first (${have} of ${need} road tiles)`;
  }
  const need = TUTORIAL.steps[step - 1].need;
  const count = need === undefined ? '' : ` (${Math.min(need, completeOf(state, type))} of ${need})`;
  return `Next: lay a road to the gold ring first, then build a ${BUILDINGS[type].name} on it${count}`;
}

// The next line of a running step (section 7.7). progress.js gives the counted line (tutorialStatus), which uses the same
// counts as the completion check, and it decides the line of step 5 too. When the step's first ring has no road link,
// the road comes first instead.
function nextLineOf(state, step, def, siteOf) {
  const type = firstSiteType(def);
  const site = type === null ? null : siteOf(type);
  if (site !== null && !validatePlacement(state, type, site.x, site.y, site.rot).connected) return unlinkedNext(state, step, type);
  return tutorialStatus(state).next;
}

// "build A or B (Build > Tab)": the names of the builds and the Build menu tab they sit under (section 7.7).
function buildText(types) {
  const tabOf = (t) => TAB_NAME[BUILDINGS[t].category];
  const tabs = [...new Set(types.map(tabOf))];
  if (tabs.length === 1) return `build ${types.map((t) => BUILDINGS[t].name).join(' or ')} (Build > ${tabs[0]})`;
  return `build ${types.map((t) => `${BUILDINGS[t].name} (Build > ${tabOf(t)})`).join(' or ')}`;
}

// What a player builds or sets to clear one unmet tier check (section 5.9 keys). A build is named only once its tier is
// unlocked, so the goal never names a locked build.
function checkAction(state, key) {
  const unlocked = (types) => types.filter((t) => BUILDINGS[t].tier <= state.tier);
  if (key === 'pop' || key === 'buildings') return buildText(unlocked(['cottage', 'townhouse']));
  if (key === 'happy') {
    const tax = 'set Taxes to low (Kingdom > Policies)';
    const amenity = unlocked(['tavern', 'chapel']);
    return amenity.length > 0 ? `${buildText(amenity)}, or ${tax}` : tax;
  }
  if (key.startsWith('has:')) return buildText([key.slice('has:'.length)]);
  if (key.startsWith('any:')) return buildText(key.slice('any:'.length).split(','));
  return 'build more (Build menu)';
}

// The goal line after the tutorial: the next tier with its unmet checks, each with the build or policy that clears it, or
// the Charter at Kingdom tier (section 7.7).
function goalText(state) {
  if (state.tier >= TIERS.length - 1) return 'Build the Royal Charter (Kingdom tier)';
  const next = TIERS[state.tier + 1];
  const unmet = tierChecks(state, state.tier + 1).filter((c) => !c.ok)
    .map((c) => `${c.label} ${Math.floor(c.have)} of ${c.need}: ${checkAction(state, c.key)}`);
  return unmet.length > 0 ? `Next goal: reach the ${next.name} tier (${unmet.join('; ')})` : `Next goal: reach the ${next.name} tier`;
}

export function getObjective(state) {
  const t = state.tutorial;
  const total = TUTORIAL.steps.length;
  const done = t.done === true;
  const skipped = t.skipped === true;
  const step = done ? total + 1 : t.step;
  const sandboxGoal = state.outcome.status === 'won' || state.outcome.status === 'sandbox' ? SANDBOX_GOAL : null;
  if (done) {
    const goal = goalText(state);
    return {
      step, total, done, skipped, title: 'Tutorial complete', banner: TUTORIAL.doneBanner, next: goal, markers: [], goal,
      sandboxGoal, buildingKey: null,
    };
  }
  // The running step's next line comes from progress.js (tutorialStatus), with the two rules of nextLineOf. Each site is
  // searched once, and its markers and next line both read that search.
  const def = TUTORIAL.steps[step - 1];
  const siteOf = siteReader(state);
  return {
    step, total, done, skipped, title: `Step ${step} of ${total}`, banner: def.banner, next: nextLineOf(state, step, def, siteOf),
    markers: markersOf(state, def, siteOf), goal: '', sandboxGoal, buildingKey: buildingKeyOf(def),
  };
}

const WEATHER_LABEL = { clear: 'Clear', rain: 'Rain', storm: 'Storm', snow: 'Snow' };
const EFFECT_LABEL = { festival: 'Festival', harvest: 'Harvest fair', raidWin: 'Raid repelled', raidLoss: 'Raid losses',
  fireScare: 'Fire scare', drought: 'Drought', flood: 'Flood' };

// Festival row of the kingdom view: the same checks, in the same order, as the festival command.
function festivalView(state) {
  const fest = EVENTS.festival;
  const day = state.day;
  const tavern = state.buildings.some((b) => b.type === 'tavern' && b.stage === 'complete');
  const cooldownLeft = Math.max(0, fest.cooldownDays - (day - state.festivalDay));
  let reason = null;
  if (!tavern) reason = 'A festival needs a finished Tavern';
  else if (cooldownLeft > 0) reason = `Festivals are ${fest.cooldownDays} days apart. Wait ${cooldownLeft} more ${cooldownLeft === 1 ? 'day' : 'days'}`;
  else reason = canAfford(state, fest.cost);
  const active = activeEffect(state, 'festival');
  return { canHold: reason === null, reason, cooldownLeft, cost: { ...fest.cost }, activeUntil: active ? active.until : null };
}

function threatView(state, season) {
  const sch = state.schedule;
  const day = state.day;
  const defence = defenceOf(state);
  const plagueActive = sch.plagueStart >= 0 && day >= sch.plagueStart && day < sch.plagueUntil;
  const drought = activeEffect(state, 'drought');
  return {
    raid: { day: sch.raidDay, strength: sch.raidStrength, warned: sch.raidWarnedDay >= 0, defence, unmet: Math.max(0, sch.raidStrength - defence) },
    plague: { active: plagueActive, warned: sch.plagueStart >= 0 && day < sch.plagueStart, daysLeft: plagueActive ? sch.plagueUntil - day : 0 },
    flood: { warned: sch.floodStart >= 0, active: activeEffect(state, 'flood') !== null },
    drought: { warned: sch.droughtStart >= 0, active: drought !== null, daysLeft: drought ? drought.until - day : 0 },
    fireRisk: season === 3 ? 'high' : (season === 2 ? 'normal' : 'low'),
  };
}

// Autumn and winter: farm output over the winter, against the food stock (section 4.8).
function winterView(state, season) {
  const visible = season >= 2;
  const demand = foodDemand(state);
  let winterOutput = 0;
  for (const b of state.buildings) {
    if (b.type !== 'farm' || b.stage !== 'complete' || !b.connected) continue;
    const def = BUILDINGS.farm;
    winterOutput += def.produces.perDay * farmFertility(state, tilesOf(b)) * Math.min(1, b.crew / def.crew)
      * haulFactor(b.roadSteps) * seasonFactor('farm', 3) * upgradeFactor(state, 'farm');
  }
  const needFood = Math.max(0, Math.round(ECONOMY.winterNeedDays * demand - ECONOMY.winterNeedDays * winterOutput));
  return {
    visible, needFood, haveFood: state.stock.food, ok: state.stock.food >= needFood,
    daysLeft: visible ? TIME.daysPerYear - (state.day % TIME.daysPerYear) : null,
  };
}

function caravanView(state) {
  return state.offers.map((o) => {
    const name = RESOURCES[o.resource].name;
    const expiresIn = o.expires - state.day;
    const verb = o.kind === 'sell' ? 'Sells' : 'Buys';
    return {
      id: o.id, kind: o.kind, resource: o.resource, resourceName: name, amount: o.amount, unitPrice: o.unitPrice,
      total: o.amount * o.unitPrice, expiresIn,
      text: `${verb} ${o.amount} ${name.toLowerCase()} at ${o.unitPrice} each (${expiresIn} ${expiresIn === 1 ? 'day' : 'days'} left)`,
    };
  });
}

// Trade gate: a complete Market with at least one worker (section 4.6).
function tradeView(state) {
  const markets = state.buildings.filter((b) => b.type === 'market' && b.stage === 'complete');
  let reason = null;
  if (markets.length === 0) reason = 'Trading needs a complete Market';
  else if (!markets.some((b) => b.crew > 0)) reason = 'The Market needs at least one worker';
  return { open: reason === null, reason, limit: ECONOMY.tradeLimitPerDay, used: { ...state.tradedToday } };
}

function stockView(state) {
  const ll = state.lastLedger;
  const stock = {};
  for (const k of RESOURCE_KEYS) {
    stock[k] = {
      have: state.stock[k], cap: storageCap(state, k), net: ll.produced[k] - ll.consumed[k] - ll.lost[k],
      produced: ll.produced[k], consumed: ll.consumed[k], lost: ll.lost[k],
    };
  }
  return stock;
}

// The per-resource net flow, keyed by resource: stock[k].net (section 7.8), read from lastLedger. lastLedger is copied at the
// start of each runDay (section 4.1), so the net is 0 until the second day has run (day 1 shows 0).
function netOf(stock) {
  return Object.fromEntries(RESOURCE_KEYS.map((k) => [k, stock[k].net]));
}

// Whole days the food stock lasts at the food deficit (section 7.8). The deficit is the food demand (foodDemand, the figure
// food.demandPerDay reports) minus the food made on the last day (lastLedger.produced.food). Demand is used, not food eaten,
// because eating is capped by the stock: on an empty day the eaten food is 0, which would hide the famine (the cover reads 0).
// Null when production at least covers demand, so nothing runs out. Spoilage and overflow are losses, not made food, so they
// are not in the deficit. The food warning (population.js, section 8.4) still counts food eaten, so the two day counts can differ.
function foodCoverDays(state, demand) {
  const deficit = demand - state.lastLedger.produced.food;
  return deficit > 0 ? Math.floor(state.stock.food / deficit) : null;
}

export function getKingdomView(state) {
  const info = getSeasonInfo(state);
  const ll = state.lastLedger;
  const stock = stockView(state);
  const ps = populationSummary(state);
  const demand = foodDemand(state);
  const prices = {};
  for (const k of TRADE_KEYS) prices[k] = quotePrice(state, k);
  const tier = state.tier;
  const hasNext = tier < TIERS.length - 1;
  const milestones = MILESTONES.map((m) => {
    const done = Object.prototype.hasOwnProperty.call(state.milestones, m.key);
    return { key: m.key, name: m.name, text: m.text, done, day: done ? state.milestones[m.key] : null };
  });
  const buildingCounts = {};
  for (const key of Object.keys(BUILDINGS)) {
    if (BUILDINGS[key].category !== 'infra') buildingCounts[key] = { complete: 0, building: 0 };
  }
  for (const b of state.buildings) {
    const c = buildingCounts[b.type];
    if (c) c[b.stage === 'complete' ? 'complete' : 'building'] += 1;
  }
  return {
    day: info.day, year: info.year, dayOfSeason: info.dayOfSeason, season: info.season, seasonName: info.name, dateText: info.dateText,
    weather: {
      kind: state.weather.kind, label: WEATHER_LABEL[state.weather.kind], untilDay: state.weather.untilDay,
      daysLeft: Math.max(0, state.weather.untilDay - state.day),
    },
    stock,
    net: netOf(stock),
    money: { income: ll.tax, upkeepDue: ll.upkeepDue, upkeepPaid: ll.upkeepPaid, net: ll.tax - ll.upkeepPaid },
    prices,
    population: {
      total: ps.total, children: ps.children, adults: ps.adults, elders: ps.elders, employed: ps.employed,
      unemployed: ps.unemployed, homeless: ps.homeless, militia: ps.militia, beds: ps.beds, freeBeds: ps.freeBeds,
      fertile: ps.fertile, peak: state.stats.peakPopulation,
    },
    happiness: {
      value: Math.round(state.happiness), exact: state.happiness, target: Math.round(state.happinessTarget),
      causes: state.happinessCauses.map((c) => ({ key: c.key, label: c.label, value: c.value, detail: c.detail })),
    },
    food: { demandPerDay: round1(demand), coverDays: foodCoverDays(state, demand), fedFraction: state.flags.fedFrac },
    foodWarnDays: ECONOMY.foodWarnCoverDays,
    tier: {
      id: tier, name: TIERS[tier].name, nextName: hasNext ? TIERS[tier + 1].name : null,
      nextChecks: hasNext ? tierChecks(state, tier + 1) : [],
    },
    policies: { tax: state.policies.tax, rations: state.policies.rations, draftRate: state.policies.draftRate },
    festival: festivalView(state),
    threats: threatView(state, info.season),
    defence: {
      militia: state.citizens.filter((c) => c.militia).length,
      towers: state.buildings.filter((b) => b.type === 'watchtower' && b.stage === 'complete' && b.crew >= 1).length,
      barracks: state.buildings.filter((b) => b.type === 'barracks' && b.stage === 'complete' && b.crew >= 1).length,
      total: defenceOf(state),
    },
    effects: state.effects.filter((e) => e.until > state.day).map((e) => ({
      kind: e.kind, label: EFFECT_LABEL[e.kind], daysLeft: e.until - state.day, value: e.value,
    })),
    caravans: caravanView(state),
    trade: tradeView(state),
    upgrades: upgradeRows(state, () => true),
    winter: winterView(state, info.season),
    objective: getObjective(state),
    milestones,
    outcome: {
      status: state.outcome.status, reason: state.outcome.reason, day: state.outcome.day,
      causes: state.outcome.causes.map((c) => ({ key: c.key, label: c.label, value: c.value })),
    },
    stats: { ...state.stats },
    log: state.log.slice(-60).map((l) => ({ day: l.day, kind: l.kind, text: l.text })),
    buildingCounts,
  };
}

export function getCitizenViews(state) {
  return state.citizens.map((c) => ({
    id: c.id, name: c.name, cohort: cohortOf(c.ageDays), ageYears: Math.floor(c.ageDays / TIME.daysPerYear),
    homeId: c.homeId, workId: c.workId, militia: c.militia,
  }));
}

export function getSeasonInfo(state) {
  const day = state.day;
  const season = seasonIndex(day);
  const dayOfSeason = day % TIME.daysPerSeason;
  const year = yearOf(day);
  const name = TIME.seasonNames[season];
  return {
    day, year, season, name, dayOfSeason, daysLeft: TIME.daysPerSeason - dayOfSeason - 1,
    dateText: `${name} ${dayOfSeason + 1}, Year ${year}`,
  };
}

// Breadth-first search over road tiles (bridges included) from one tile index to another, both inclusive.
export function getRoadRoute(state, fromIdx, toIdx) {
  const road = state.map.road;
  const n = road.length;
  if (!Number.isInteger(fromIdx) || !Number.isInteger(toIdx) || fromIdx < 0 || toIdx < 0 || fromIdx >= n || toIdx >= n) return null;
  if (road[fromIdx] === 0 || road[toIdx] === 0) return null;
  const W = state.width;
  const prev = new Int32Array(n).fill(-1);
  const seen = new Uint8Array(n);
  const q = [fromIdx];
  seen[fromIdx] = 1;
  for (let k = 0; k < q.length && seen[toIdx] === 0; k += 1) {
    const i = q[k];
    const x = i % W;
    for (const nb of neighbours4(x, (i - x) / W, W, state.height)) {
      const j = nb.y * W + nb.x;
      if (seen[j] === 0 && road[j] !== 0) {
        seen[j] = 1;
        prev[j] = i;
        q.push(j);
      }
    }
  }
  if (seen[toIdx] === 0) return null;
  const path = [];
  for (let i = toIdx; i !== -1; i = prev[i]) path.unshift(i);
  return path;
}

// Ordering of suggestion candidates (section 3.11): farms by fertility, then distance to the Hall door, then y, x, rot. Road
// links are not in the order, so a road tile never reorders the candidates; the ring moves only when a road covers it.
const cmpCandidate = (a, b) => (a.fert - b.fert) || (a.d2 - b.d2) || (a.y - b.y) || (a.x - b.x) || (a.rot - b.rot);
// validatePlacement's refusal for a spot that is valid but has no road link yet (section 6.2 step 10).
const LINK_REASON = 'Needs a road connection to the Town Hall. Lay a road to this spot first.';
// A placement that is valid, or whose only failure is the road link or the cost (section 3.11). Such a spot shows as a
// suggestion or an armed dot before the road or the money exists.
const fixableLater = (v) => v.ok || v.reason === LINK_REASON || (v.costReason !== null && v.reason === v.costReason);

// Indices of the tiles 4-adjacent to tile i, inside the map.
function adjacentIdx(i, W, H) {
  const x = i % W;
  const y = (i - x) / W;
  return [x > 0 ? i - 1 : -1, x < W - 1 ? i + 1 : -1, y > 0 ? i - W : -1, y < H - 1 ? i + W : -1].filter((j) => j >= 0);
}

// Steps from the road network, or the Hall footprint, to each tile a road may use: planRoad's search (world.js), run once
// per call for every candidate. Open tiles are explored, roadable, and free of buildings and roads. -1 where none reaches.
function roadSteps(state) {
  const W = state.width;
  const H = state.height;
  const m = state.map;
  const conn = state.net.connected;
  const hall = new Uint8Array(W * H);
  for (const b of state.buildings.filter((hb) => hb.type === 'townHall')) {
    for (const t of footprintOf(b.type, b.x, b.y, b.rot).tiles) if (inBounds(state, t.x, t.y)) hall[idx(state, t.x, t.y)] = 1;
  }
  const open = (i) => m.explored[i] === 1 && isRoadable(m.terrain[i]) && m.building[i] === 0 && m.road[i] === 0;
  const touches = (i) => adjacentIdx(i, W, H).some((j) => (m.road[j] !== 0 && conn[j] === 1) || hall[j] === 1);
  const steps = new Int32Array(W * H).fill(-1);
  const queue = [];
  for (let i = 0; i < W * H; i += 1) {
    if (open(i) && touches(i)) { steps[i] = 0; queue.push(i); }
  }
  for (let k = 0; k < queue.length; k += 1) {
    for (const j of adjacentIdx(queue[k], W, H)) {
      if (steps[j] < 0 && open(j)) { steps[j] = steps[queue[k]] + 1; queue.push(j); }
    }
  }
  return steps;
}

// Tiles 4-adjacent to a footprint, outside it, that a road reaches within one placeRoad command (at most maxRoadPoints
// tiles, the route included). Nearest first, then by index.
function besideTargets(state, tiles, steps) {
  const fp = new Set(tiles.map((t) => idx(state, t.x, t.y)));
  const near = tiles.flatMap((t) => adjacentIdx(idx(state, t.x, t.y), state.width, state.height));
  return [...new Set(near)].filter((j) => !fp.has(j) && steps[j] >= 0 && steps[j] < ECONOMY.maxRoadPoints)
    .sort((a, b) => steps[a] - steps[b] || a - b);
}

// Whether an unlinked footprint has a road plan: getRoadPlan (the planner the player and the balance bot use) gives a
// route to a tile beside it that stays off the footprint, and validateRoadPoints accepts that route. Cost is not part
// of the plan, as in the marker rule of section 3.11.
function hasRoadPlan(state, cand) {
  const W = state.width;
  const fp = new Set(cand.tiles.map((t) => idx(state, t.x, t.y)));
  return cand.beside.some((j) => {
    const plan = getRoadPlan(state, j % W, Math.floor(j / W));
    if (!plan.ok || plan.points.some((p) => fp.has(idx(state, p.x, p.y)))) return false;
    const road = validateRoadPoints(state, plan.points);
    return road.reason === null || road.reason === canAfford(state, road.cost);
  });
}

// The tutorial's first ring is a farm (its type in step 1, section 5.8), and steps 1 and 2 show it as the gold ring.
const firstRingType = (state, type) => type === firstSiteType(TUTORIAL.steps[0]) && state.tutorial.step <= 2 && !state.tutorial.done;

// Road tiles from the Town Hall (section 3.11): 1 for a tile beside the Hall, 2 beyond it, and so on, over explored tiles
// that a road can use and that hold no building. Roads do not block the walk, so the depths do not move as roads are laid.
// -1 where no walk reaches.
function hallDepths(state) {
  const W = state.width;
  const H = state.height;
  const m = state.map;
  const depth = new Int32Array(W * H).fill(-1);
  const queue = [];
  for (const b of state.buildings.filter((hb) => hb.type === 'townHall')) {
    for (const t of footprintOf(b.type, b.x, b.y, b.rot).tiles) {
      if (!inBounds(state, t.x, t.y)) continue;
      const i = idx(state, t.x, t.y);
      depth[i] = 0;
      queue.push(i);
    }
  }
  for (let k = 0; k < queue.length; k += 1) {
    for (const j of adjacentIdx(queue[k], W, H)) {
      if (depth[j] < 0 && m.explored[j] === 1 && m.building[j] === 0 && isRoadable(m.terrain[j])) {
        depth[j] = depth[queue[k]] + 1;
        queue.push(j);
      }
    }
  }
  return depth;
}

// The fewest road tiles from the Hall to a tile beside a footprint (hallDepths), or Infinity when none is reached.
function reachOf(state, tiles, depth) {
  const fp = new Set(tiles.map((t) => idx(state, t.x, t.y)));
  let best = Infinity;
  for (const t of tiles) {
    for (const j of adjacentIdx(idx(state, t.x, t.y), state.width, state.height)) {
      if (!fp.has(j) && depth[j] >= 1 && depth[j] < best) best = depth[j];
    }
  }
  return best;
}

// Best valid placement of this type (section 3.11), ranked by farm fertility, then distance to the Hall door (cmpCandidate).
// An unlinked spot needs a road plan (hasRoadPlan), so no marker points at a spot that no road can reach. The tutorial's
// first ring also lies within the tutorial road need: no more than TUTORIAL.steps[0].need road tiles from the Hall.
export function suggestSite(state, type) {
  if (typeof type !== 'string' || !Object.prototype.hasOwnProperty.call(BUILDINGS, type) || BUILDINGS[type].category === 'infra') return null;
  const def = BUILDINGS[type];
  const door = MAP.door;
  const rots = def.w === def.h ? [0] : [0, 1];
  const isFarm = def.needs?.kind === 'farm';
  const depth = firstRingType(state, type) ? hallDepths(state) : null;
  let steps = null;
  const pool = [];
  for (let y = door.y - SITE_RANGE; y <= door.y + SITE_RANGE; y += 1) {
    for (let x = door.x - SITE_RANGE; x <= door.x + SITE_RANGE; x += 1) {
      for (const rot of rots) {
        const v = validatePlacement(state, type, x, y, rot);
        if (!fixableLater(v)) continue;
        if (depth !== null && reachOf(state, v.tiles, depth) > TUTORIAL.steps[0].need) continue;
        const dx = x - door.x;
        const dy = y - door.y;
        const cand = { x, y, rot, conn: v.connected ? 0 : 1, fert: isFarm ? -farmFertility(state, v.tiles) : 0, d2: dx * dx + dy * dy, tiles: v.tiles };
        if (!v.connected) {
          steps = steps || roadSteps(state);
          cand.beside = besideTargets(state, v.tiles, steps);
          if (cand.beside.length === 0) continue;
        }
        pool.push(cand);
      }
    }
  }
  pool.sort(cmpCandidate);
  const pick = pool.find((cand) => cand.conn === 0 || hasRoadPlan(state, cand));
  return pick ? { x: pick.x, y: pick.y, rot: pick.rot } : null;
}

// Tile indices, ascending, where a placement of this type at rot 0 is valid or fails only on the road link or the cost
// (fixableLater, section 3.11). Infra and unknown types have none. The armed-building dots read it (change R1-15, R2-03 b).
export function getBuildableTiles(state, type) {
  if (typeof type !== 'string' || !Object.prototype.hasOwnProperty.call(BUILDINGS, type) || BUILDINGS[type].category === 'infra') return [];
  const out = [];
  for (let y = 0; y < state.height; y += 1) {
    for (let x = 0; x < state.width; x += 1) {
      if (fixableLater(validatePlacement(state, type, x, y, 0))) out.push(idx(state, x, y));
    }
  }
  return out;
}
