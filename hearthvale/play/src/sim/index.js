// owner: core
// Section 3.12, section 7.1 (createNewGame) and section 8 (the daily tick). The public API of the simulation.
import { CONFIG } from '../config/index.js';
import { BUILDINGS } from '../config/buildings.js';
import { RESOURCE_KEYS, TRADE_KEYS } from '../config/resources.js';
import { MAP } from '../config/map.js';
import { POPULATION, NAMES } from '../config/population.js';
import { createEmptyState, ensureRuntime, validateState, emit, idx, buildingById } from './state.js';
import { generateMap, footprintOf, refreshNetwork, connectedRoadCount } from './world.js';
import { pick } from './rng.js';
import { dailyEvents, raidStrengthFor } from './events.js';
import { constructionDay, productionDay, spoilageDay, financeDay, pricesDay } from './economy.js';
import { assignJobs, consumptionDay, computeHappiness, happinessDay, agingDay, deathsDay, birthsDay,
  migrationDay, homelessDay, militiaDay } from './population.js';
import { tierDay, milestonesDay, tutorialDay, outcomeDay } from './progress.js';

export { CONFIG, TIME } from '../config/index.js';
export { TERRAIN, TERRAIN_NAME } from './state.js';
export { SAVE_VERSION, SAVE_FORMAT, SaveError, serializeState, deserializeState } from './save.js';
export { applyCommand, validatePlacement } from './commands.js';
export { getCatalog, getTileView, getBuildingView, getPlacementPreview, getRoadPlan, getObjective, getKingdomView,
  getRoadRoute, getCitizenViews, getSeasonInfo, suggestSite, getBuildableTiles } from './queries.js';

const zeros = () => Object.fromEntries(RESOURCE_KEYS.map((k) => [k, 0]));
// A ledger with every flow at zero (section 4.3).
const freshLedger = () => ({
  produced: zeros(), consumed: zeros(), lost: zeros(), tax: 0, upkeepDue: 0, upkeepPaid: 0, born: 0, died: 0, arrived: 0,
});

// Fresh kingdom for a seed (section 7.1). Throws only if the built state fails validation (an internal bug).
export function createNewGame({ seed, width = MAP.width, height = MAP.height } = {}) {
  const state = createEmptyState({ seed, width, height });
  const m = generateMap(seed, width, height);
  state.map.terrain.set(m.terrain);
  state.map.height.set(m.height);
  state.map.deposit.set(m.deposit);
  state.map.explored.set(m.explored);
  for (const p of m.starterRoad) state.map.road[idx(state, p.x, p.y)] = 1;
  const off = Math.floor(MAP.hallSize / 2);
  const x0 = m.hall.x - off;
  const y0 = m.hall.y - off;
  const hall = footprintOf('townHall', x0, y0, 0);
  state.buildings.push({
    id: 1, type: 'townHall', x: x0, y: y0, rot: 0, w: hall.w, h: hall.h, stage: 'complete', progress: 1, builders: 0,
    stalled: 0, priority: 'normal', crew: 0, acc: 0, cooldown: 0, connected: true, roadSteps: 0, createdDay: 0, lastHarvestDay: -1,
  });
  for (const t of hall.tiles) state.map.building[idx(state, t.x, t.y)] = 1;
  const starts = [...POPULATION.startYears.children, ...POPULATION.startYears.adults, ...POPULATION.startYears.elders];
  const hallBeds = BUILDINGS.townHall.beds;
  starts.forEach((years, k) => {
    const id = k + 1;
    state.citizens.push({
      id, name: pick(state, NAMES), ageDays: years * CONFIG.time.daysPerYear, homeId: id <= hallBeds ? 1 : 0, workId: 0, militia: false,
    });
  });
  state.stats.peakPopulation = state.citizens.length;
  state.schedule.raidStrength = raidStrengthFor(CONFIG.events.raid.firstDay);
  refreshNetwork(state);
  // The starter network's connected road count. The tutorial counts only road laid beyond it (tutorialBaseline).
  state.tutorialBaseline = connectedRoadCount(state);
  assignJobs(state);
  state.happinessCauses = computeHappiness(state).causes;
  state.happiness = POPULATION.happiness.start;
  state.happinessTarget = POPULATION.happiness.start;
  ensureRuntime(state);
  const errors = validateState(state);
  if (errors.length > 0) throw new Error(`createNewGame built an invalid state: ${errors.join('; ')}`);
  return state;
}

// Reports buildings that lost their road connection this day (section 8 steps 2 and 4).
function cutOffEvents(state, events, ids) {
  for (const id of ids) {
    const b = buildingById(state, id);
    const name = b ? BUILDINGS[b.type].name : 'A building';
    emit(state, events, { type: 'cutOff', kind: 'warn', text: `${name} has lost its road to the Town Hall.`, id });
  }
}

const signed = (n) => `${n >= 0 ? '+' : '-'}${Math.abs(n)}`;

// Runs the dawn of state.day (section 8 steps 1 to 24), then advances the day. Returns the day's events.
export function runDay(state) {
  ensureRuntime(state);
  const events = [];
  // Step 1: dawn bookkeeping.
  state.lastLedger = state.ledger;
  state.ledger = freshLedger();
  if (state.tradeDay !== state.day) {
    for (const k of TRADE_KEYS) state.tradedToday[k] = 0;
    state.tradeDay = state.day;
  }
  state.flags.famine = false;
  state.flags.cold = false;
  state.flags.debt = false;
  state.rev.buildings += 1;
  state.rev.citizens += 1;
  // Steps 2 to 4: network, events, network again (a flood may wash out a bridge).
  cutOffEvents(state, events, refreshNetwork(state).cutOff);
  dailyEvents(state, events);
  cutOffEvents(state, events, refreshNetwork(state).cutOff);
  // Steps 5 to 11: construction, jobs, production, spoilage, consumption, finance, prices.
  constructionDay(state, events);
  assignJobs(state);
  productionDay(state, events);
  spoilageDay(state, events);
  consumptionDay(state, events);
  financeDay(state, events);
  pricesDay(state);
  // Steps 12 to 19: people.
  homelessDay(state, events);
  agingDay(state, events);
  deathsDay(state, events);
  birthsDay(state, events);
  migrationDay(state, events);
  militiaDay(state, events);
  assignJobs(state);
  happinessDay(state, events);
  // Steps 20 to 23: progress and outcome.
  tierDay(state, events);
  milestonesDay(state, events);
  tutorialDay(state, events);
  outcomeDay(state, events);
  // Step 24: digest and the day counter.
  const led = state.ledger;
  const food = led.produced.food - led.consumed.food - led.lost.food;
  const gold = led.produced.gold - led.consumed.gold - led.lost.gold;
  emit(state, events, {
    type: 'digest', kind: 'info',
    text: `Day ${state.day + 1}: food ${signed(food)}, gold ${signed(gold)}, ${led.born} born, ${led.died} died, ${led.arrived} arrived.`,
  });
  state.day += 1;
  return events;
}

// Runs whole days. Returns [] for a non-integer or negative count, or once the game is won or lost.
export function advanceDays(state, days) {
  if (!Number.isInteger(days) || days < 0) return [];
  if (state.outcome.status === 'won' || state.outcome.status === 'lost') return [];
  const all = [];
  for (let k = 0; k < days; k += 1) {
    for (const ev of runDay(state)) all.push(ev);
    if (state.outcome.status === 'won' || state.outcome.status === 'lost') break;
  }
  return all;
}
