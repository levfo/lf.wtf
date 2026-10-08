// owner: foundation
// Section 3.3 and section 4: state schema and defaults, runtime helpers and validation. Pure.
import { RESOURCES, RESOURCE_KEYS, TRADE_KEYS } from '../config/resources.js';
import { CONFIG, TIME } from '../config/index.js';

export const TERRAIN = { GRASS: 0, MEADOW: 1, FOREST: 2, HILL: 3, MOUNTAIN: 4, RIVER: 5, LAKE: 6, STONE: 7, IRON: 8 };
export const TERRAIN_NAME = ['grass', 'meadow', 'forest', 'hill', 'mountain', 'river', 'lake', 'stone', 'iron'];

// Every key of state.stats in section 4.5 order.
export const STAT_KEYS = [
  'born', 'died', 'immigrated', 'emigrated', 'raidsRepelled', 'raidsLost', 'raidDeaths', 'fires', 'fireDeaths',
  'plagues', 'plagueDeaths', 'floods', 'droughts', 'famineDeaths', 'oldAgeDeaths', 'harvested', 'goodsMade',
  'ironMined', 'goldEarned', 'goldSpent', 'tradedUnits', 'caravans', 'famineDays', 'debtDays', 'coldDays',
  'built', 'overflow', 'peakPopulation',
];

const STATE_VERSION = 1; // equals SAVE_VERSION in save.js
const MAX_U32 = 0xFFFFFFFF;
const ROADABLE = [TERRAIN.GRASS, TERRAIN.MEADOW, TERRAIN.FOREST, TERRAIN.HILL, TERRAIN.STONE, TERRAIN.IRON, TERRAIN.RIVER];
const RESOURCE_TERRAIN = [TERRAIN.FOREST, TERRAIN.STONE, TERRAIN.IRON];
const WEATHER_KINDS = ['clear', 'rain', 'storm', 'snow'];
const EFFECT_KINDS = ['festival', 'harvest', 'raidWin', 'raidLoss', 'fireScare', 'drought', 'flood'];
const SCHEDULE_KEYS = [
  'raidDay', 'raidStrength', 'raidWarnedDay', 'plagueStart', 'plagueUntil', 'plagueNextAllowed',
  'plaguePopStart', 'plagueDeathBase', 'floodStart', 'droughtStart', 'goldenDays', 'plagueMendingDay', 'foodWarnDay',
  'lastDefence', // R2-08: integer, default 0; additive, so SAVE_VERSION stays 1 (10.6)
];
const CARRY_KEYS = ['food', 'goods', 'fuel', 'tax', 'upkeep'];
const LEDGER_TOTALS = ['tax', 'upkeepDue', 'upkeepPaid', 'born', 'died', 'arrived'];
const PRIORITIES = ['normal', 'priority', 'paused'];
const MAP_ARRAYS = [
  ['terrain', Uint8Array], ['height', Uint8Array], ['deposit', Uint16Array],
  ['road', Uint8Array], ['building', Uint16Array], ['explored', Uint8Array],
];

const isObj = (v) => v !== null && typeof v === 'object' && !Array.isArray(v);
const isFin = (v) => typeof v === 'number' && Number.isFinite(v);
const perRes = (value) => Object.fromEntries(RESOURCE_KEYS.map((k) => [k, value]));
const newLedger = () => ({
  produced: perRes(0), consumed: perRes(0), lost: perRes(0),
  tax: 0, upkeepDue: 0, upkeepPaid: 0, born: 0, died: 0, arrived: 0,
});
// Raid strength for a day (section 5.7): min(strengthMax, strengthBase + floor(day / strengthEvery)).
const raidStrengthOf = (day) => {
  const r = CONFIG.events.raid;
  return Math.min(r.strengthMax, r.strengthBase + Math.floor(day / r.strengthEvery));
};

// Fresh state with section 4 defaults. No buildings or citizens; index.js fills the map and the start.
export function createEmptyState({ seed, width, height }) {
  const n = width * height;
  const s = seed >>> 0;
  const pop = CONFIG.population;
  const startPop = pop.startYears.children.length + pop.startYears.adults.length + pop.startYears.elders.length;
  const raid = CONFIG.events.raid;
  const state = {
    version: STATE_VERSION, seed: s, rng: s, width, height, day: 0,
    map: {
      terrain: new Uint8Array(n), height: new Uint8Array(n), deposit: new Uint16Array(n),
      road: new Uint8Array(n), building: new Uint16Array(n), explored: new Uint8Array(n),
    },
    buildings: [], citizens: [],
    nextBuildingId: 2, nextCitizenId: startPop + 1, nextOfferId: 1, nextEffectId: 1,
    stock: Object.fromEntries(RESOURCE_KEYS.map((k) => [k, RESOURCES[k].start])),
    carry: Object.fromEntries(CARRY_KEYS.map((k) => [k, 0])),
    price: Object.fromEntries(TRADE_KEYS.map((k) => [k, RESOURCES[k].base])),
    priceTarget: Object.fromEntries(TRADE_KEYS.map((k) => [k, RESOURCES[k].base])),
    tradedToday: Object.fromEntries(TRADE_KEYS.map((k) => [k, 0])),
    tradeDay: -1, ledger: newLedger(), lastLedger: newLedger(),
    policies: { tax: 'normal', rations: 'normal', draftRate: 'off' },
    weather: { kind: 'clear', untilDay: 0 },
    effects: [], offers: [], nextCaravanDay: -1,
    schedule: {
      raidDay: raid.firstDay, raidStrength: raidStrengthOf(raid.firstDay), raidWarnedDay: -1,
      plagueStart: -1, plagueUntil: -1, plagueNextAllowed: CONFIG.events.plague.startDay,
      plaguePopStart: 0, plagueDeathBase: 0, floodStart: -1, droughtStart: -1, goldenDays: 0,
      plagueMendingDay: -1, foodWarnDay: -99, lastDefence: 0,
    },
    happiness: pop.happiness.start, happinessTarget: pop.happiness.start, happinessCauses: [], exodusDays: 0,
    tier: 0, tierDay: 0,
    tutorial: { step: 1, done: false, skipped: false, tradeDone: false },
    tutorialBaseline: 0,
    milestones: {}, festivalDay: -999,
    flags: { famine: false, cold: false, debt: false, fedFrac: 1 },
    upgrades: { cropRotation: false, forestry: false, deepShafts: false },
    stats: Object.fromEntries(STAT_KEYS.map((k) => [k, k === 'peakPopulation' ? startPop : 0])),
    lastOverflow: perRes(-99),
    log: [],
    outcome: { status: 'playing', reason: null, day: null, causes: [] },
  };
  ensureRuntime(state);
  return state;
}

export function idx(state, x, y) {
  return y * state.width + x;
}

export function inBounds(state, x, y) {
  return Number.isInteger(x) && Number.isInteger(y) && x >= 0 && y >= 0 && x < state.width && y < state.height;
}

// Appends to the log (cap TIME.logCap, oldest dropped) without an event.
export function addLog(state, kind, text) {
  state.log.push({ day: state.day, kind, text });
  const extra = state.log.length - TIME.logCap;
  if (extra > 0) state.log.splice(0, extra);
}

// Creates a sim event, adds it to events and to the log, and returns it.
export function emit(state, events, ev) {
  const e = { type: ev.type, kind: ev.kind, text: ev.text, day: state.day };
  for (const key of ['x', 'y', 'id', 'amount', 'resource']) if (ev[key] !== undefined) e[key] = ev[key];
  events.push(e);
  addLog(state, e.kind, e.text);
  return e;
}

export function buildingById(state, id) {
  return state.buildings.find((b) => b.id === id) || null;
}

export function citizenById(state, id) {
  return state.citizens.find((c) => c.id === id) || null;
}

// Creates rev and net when absent (after load and creation). Never recomputes the network.
export function ensureRuntime(state) {
  if (!state.rev) state.rev = { map: 0, buildings: 0, citizens: 0, weather: 0 };
  if (!state.net) {
    const n = state.width * state.height;
    const dist = new Int16Array(n);
    dist.fill(-1);
    state.net = { connected: new Uint8Array(n), dist };
  }
}

// Returns violation strings; an empty array means the state is valid. Never throws.
export function validateState(state) {
  const out = [];
  try {
    checkState(state, out);
  } catch (e) {
    out.push(`state is malformed: ${e.message}`);
  }
  return out;
}

const isInt = (v, min = 0) => Number.isInteger(v) && v >= min;
const allInts = (o, keys, min = 0) => isObj(o) && keys.every((k) => isInt(o[k], min));
// Pushes "label.key msg" for every key of obj where ok(value) is false.
const badKeys = (out, label, obj, keys, ok, msg) => {
  for (const k of keys) if (!ok(obj?.[k])) out.push(`${label}.${k} ${msg}`);
};
const WHOLE = 'must be a whole number of 0 or more';

function checkState(s, out) {
  const need = (cond, msg) => { if (cond) out.push(msg); };
  if (!isObj(s)) { out.push('state is not an object'); return; }
  need(s.version !== STATE_VERSION, 'version is not 1');
  need(!isInt(s.width, 1) || !isInt(s.height, 1), 'width and height must be positive whole numbers');
  if (out.length) return;
  const n = s.width * s.height;
  need(!isInt(s.seed) || s.seed > MAX_U32, 'seed is not a uint32');
  need(!isInt(s.rng) || s.rng > MAX_U32, 'rng is not a uint32');
  need(!isInt(s.day), 'day must be a whole number of 0 or more');
  need(!isObj(s.map), 'map is missing');
  if (out.length) return;
  for (const [k, C] of MAP_ARRAYS) need(!(s.map[k] instanceof C) || s.map[k].length !== n, `map.${k} has the wrong size or type`);
  if (out.length) return;
  // Economy.
  badKeys(out, 'stock', s.stock, RESOURCE_KEYS, (v) => isInt(v), WHOLE);
  badKeys(out, 'carry', s.carry, CARRY_KEYS, (v) => isFin(v) && v >= 0 && v < 1, 'must be in [0, 1)');
  badKeys(out, 'price', s.price, TRADE_KEYS, (v) => isFin(v) && v > 0, 'must be positive');
  badKeys(out, 'priceTarget', s.priceTarget, TRADE_KEYS, (v) => isFin(v) && v > 0, 'must be positive');
  badKeys(out, 'tradedToday', s.tradedToday, TRADE_KEYS, (v) => isInt(v), WHOLE);
  need(!isInt(s.tradeDay, -1), 'tradeDay must be -1 or a day');
  for (const led of [s.ledger, s.lastLedger]) {
    need(!isObj(led) || !['produced', 'consumed', 'lost'].every((f) => allInts(led[f], RESOURCE_KEYS)) || !allInts(led, LEDGER_TOTALS), 'a ledger is invalid');
  }
  need(!['low', 'normal', 'high'].includes(s.policies?.tax) || !['half', 'normal', 'full'].includes(s.policies?.rations)
    || !['off', 'light', 'full'].includes(s.policies?.draftRate), 'a policy setting is unknown');
  need(!WEATHER_KINDS.includes(s.weather?.kind) || !isInt(s.weather?.untilDay), 'weather is invalid');
  need(!Array.isArray(s.effects) || !Array.isArray(s.offers), 'effects and offers must be lists');
  for (const e of Array.isArray(s.effects) ? s.effects : []) {
    need(!isInt(e.id, 1) || e.id >= s.nextEffectId || !EFFECT_KINDS.includes(e.kind) || !isInt(e.until) || !isFin(e.value), 'an effect is invalid');
  }
  for (const o of Array.isArray(s.offers) ? s.offers : []) {
    need(!isInt(o.id, 1) || o.id >= s.nextOfferId || !['sell', 'buy'].includes(o.kind) || !TRADE_KEYS.includes(o.resource)
      || !isInt(o.amount, 1) || !isInt(o.unitPrice, 1) || !isInt(o.expires), 'an offer is invalid');
  }
  need(!isInt(s.nextCaravanDay, -1), 'nextCaravanDay must be -1 or a day');
  badKeys(out, 'schedule', s.schedule, SCHEDULE_KEYS, (v) => Number.isInteger(v), 'must be a whole number');
  // Progress, people and records.
  need(!isFin(s.happiness) || s.happiness < 0 || s.happiness > 100, 'happiness must be in 0..100');
  need(!isFin(s.happinessTarget) || s.happinessTarget < 0 || s.happinessTarget > 100, 'happinessTarget must be in 0..100');
  need(!Array.isArray(s.happinessCauses), 'happinessCauses must be a list');
  need(!isInt(s.exodusDays), `exodusDays ${WHOLE}`);
  need(!isInt(s.tier) || s.tier > 3, 'tier must be 0 to 3');
  need(!isInt(s.tierDay) || !isInt(s.festivalDay, -999), 'tierDay and festivalDay must be days');
  need(!isInt(s.tutorial?.step, 1) || s.tutorial.step > 7, 'tutorial.step must be 1 to 7');
  badKeys(out, 'tutorial', s.tutorial, ['done', 'skipped', 'tradeDone'], (v) => typeof v === 'boolean', 'must be true or false');
  need(!isInt(s.tutorialBaseline), `tutorialBaseline ${WHOLE}`);
  need(!isObj(s.milestones) || Object.keys(s.milestones).some((k) => !CONFIG.milestones.some((m) => m.key === k) || !isInt(s.milestones[k])), 'a milestone is invalid');
  badKeys(out, 'flags', s.flags, ['famine', 'cold', 'debt'], (v) => typeof v === 'boolean', 'must be true or false');
  need(!isFin(s.flags?.fedFrac) || s.flags.fedFrac < 0 || s.flags.fedFrac > 1, 'flags.fedFrac must be in [0, 1]');
  badKeys(out, 'upgrades', s.upgrades, Object.keys(CONFIG.upgrades), (v) => typeof v === 'boolean', 'must be true or false');
  badKeys(out, 'lastOverflow', s.lastOverflow, RESOURCE_KEYS, (v) => isInt(v, -99), 'is invalid');
  badKeys(out, 'stats', s.stats, STAT_KEYS, (v) => isInt(v), WHOLE);
  need(!Array.isArray(s.log) || s.log.some((l) => !isObj(l) || !isInt(l.day) || typeof l.text !== 'string'), 'log entries are invalid');
  need(!['playing', 'won', 'sandbox', 'lost'].includes(s.outcome?.status), 'outcome.status is unknown');
  need(!Array.isArray(s.outcome?.causes), 'outcome.causes must be a list');
  checkTiles(s, out);
  checkBuildings(s, out);
  checkCitizens(s, out);
}

// Terrain codes, roads and bridges, deposits and explored flags, tile by tile.
function checkTiles(s, out) {
  const m = s.map;
  const n = s.width * s.height;
  for (let i = 0; i < n; i += 1) {
    const t = m.terrain[i];
    const r = m.road[i];
    if (t > TERRAIN.IRON) out.push(`map.terrain[${i}] is not a terrain code`);
    if (r > 2) out.push(`map.road[${i}] is not 0, 1 or 2`);
    if (r !== 0) {
      if (!ROADABLE.includes(t)) out.push(`road on unroadable terrain at ${i}`);
      if (r === 2 && t !== TERRAIN.RIVER) out.push(`bridge not on a river at ${i}`);
      if (r === 1 && t === TERRAIN.RIVER) out.push(`river tile without a bridge at ${i}`);
      if (m.building[i] !== 0) out.push(`road under a building at ${i}`);
    }
    if (m.explored[i] > 1) out.push(`map.explored[${i}] is not 0 or 1`);
    if (!RESOURCE_TERRAIN.includes(t) && m.deposit[i] !== 0) out.push(`deposit on a non-resource tile at ${i}`);
  }
}

function checkBuildings(s, out) {
  const need = (cond, msg) => { if (cond) out.push(msg); };
  const m = s.map;
  const n = s.width * s.height;
  const ids = new Set();
  let lastId = 0;
  let halls = 0;
  let charters = 0;
  let footprintTiles = 0;
  for (const b of s.buildings) {
    if (!isObj(b) || !Object.prototype.hasOwnProperty.call(CONFIG.buildings, b.type)) { out.push('a building has an unknown type'); continue; }
    const def = CONFIG.buildings[b.type];
    need(!Number.isInteger(b.id) || b.id < 1 || ids.has(b.id) || b.id <= lastId, `building id ${b.id} is missing, repeated or out of order`);
    ids.add(b.id);
    lastId = b.id;
    need(b.stage !== 'building' && b.stage !== 'complete', `building ${b.id} has an unknown stage`);
    need(!Number.isInteger(b.rot) || b.rot < 0 || b.rot > 3, `building ${b.id} has an invalid rotation`);
    const swap = b.rot === 1 || b.rot === 3;
    const w = swap ? def.h : def.w;
    const h = swap ? def.w : def.h;
    need(b.w !== w || b.h !== h, `building ${b.id} footprint ${b.w}x${b.h} does not match ${w}x${h}`);
    need(!Number.isInteger(b.x) || !Number.isInteger(b.y), `building ${b.id} has no position`);
    if (Number.isInteger(b.x) && Number.isInteger(b.y)) {
      for (let dy = 0; dy < h; dy += 1) {
        for (let dx = 0; dx < w; dx += 1) {
          const x = b.x + dx;
          const y = b.y + dy;
          if (x < 0 || y < 0 || x >= s.width || y >= s.height) { out.push(`building ${b.id} lies off the map`); continue; }
          need(m.building[y * s.width + x] !== b.id, `building ${b.id} is missing from the map at ${x},${y}`);
          footprintTiles += 1;
        }
      }
    }
    need(!(b.progress >= 0 && b.progress <= 1), `building ${b.id} progress must be in [0, 1]`);
    need(b.stage === 'complete' && b.progress !== 1, `building ${b.id} is complete but progress is not 1`);
    need(!PRIORITIES.includes(b.priority), `building ${b.id} has an unknown priority`);
    need(!isInt(b.builders) || b.builders > 2, `building ${b.id} has invalid builders`);
    need(!isInt(b.stalled) || !isInt(b.crew) || !isInt(b.cooldown), `building ${b.id} has invalid stalled, crew or cooldown`);
    need(!(isFin(b.acc) && b.acc >= 0), `building ${b.id} has invalid acc`);
    need(typeof b.connected !== 'boolean', `building ${b.id} has invalid connected`);
    need(!isInt(b.roadSteps, -1), `building ${b.id} has invalid roadSteps`);
    need(!Number.isInteger(b.createdDay) || !Number.isInteger(b.lastHarvestDay), `building ${b.id} has invalid day fields`);
    if (b.type === 'townHall') halls += 1;
    if (b.type === 'royalCharter') charters += 1;
  }
  need(halls !== 1, 'there must be exactly one Town Hall');
  need(charters > 1, 'there can be only one Royal Charter');
  need(!Number.isInteger(s.nextBuildingId) || s.nextBuildingId <= lastId, 'nextBuildingId must be above every building id');
  let occupied = 0;
  for (let i = 0; i < n; i += 1) {
    if (m.building[i] === 0) continue;
    occupied += 1;
    need(!ids.has(m.building[i]), `map.building[${i}] points at a missing building ${m.building[i]}`);
  }
  need(occupied !== footprintTiles, 'map.building does not match the building footprints');
}

function checkCitizens(s, out) {
  const need = (cond, msg) => { if (cond) out.push(msg); };
  const homes = new Set(s.buildings.filter((b) => isObj(b) && CONFIG.buildings[b.type]?.beds > 0).map((b) => b.id));
  const ids = new Set(s.buildings.map((b) => b.id));
  let lastId = 0;
  for (const c of s.citizens) {
    if (!isObj(c)) { out.push('a citizen record is not an object'); continue; }
    need(!Number.isInteger(c.id) || c.id < 1 || c.id <= lastId, `citizen id ${c.id} is missing or out of order`);
    lastId = Number.isInteger(c.id) ? c.id : lastId;
    need(typeof c.name !== 'string' || c.name.length === 0, `citizen ${c.id} has no name`);
    need(!isInt(c.ageDays), `citizen ${c.id} has an invalid age`);
    need(!isInt(c.homeId) || (c.homeId > 0 && !homes.has(c.homeId)), `citizen ${c.id} has a dangling homeId`);
    need(!isInt(c.workId) || (c.workId > 0 && !ids.has(c.workId)), `citizen ${c.id} has a dangling workId`);
    need(typeof c.militia !== 'boolean', `citizen ${c.id} has invalid militia`);
  }
  need(!Number.isInteger(s.nextCitizenId) || s.nextCitizenId <= lastId, 'nextCitizenId must be above every citizen id');
}
