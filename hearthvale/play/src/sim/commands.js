// owner: core
// Section 3.10 and section 6: applyCommand, validatePlacement, validateRoadPoints. Pure; never throws.
import { BUILDINGS } from '../config/buildings.js';
import { RESOURCE_KEYS } from '../config/resources.js';
import { ECONOMY, UPGRADES } from '../config/economy.js';
import { TIME } from '../config/index.js';
import { TERRAIN, idx, inBounds, buildingById, ensureRuntime } from './state.js';
import { footprintOf, footprintSize, neighbours4, refreshNetwork, touchesWater, resourceTilesNear,
  isBuildableLand } from './world.js';
import { canAfford, spend, refund, applyTrade, applyCaravanDeal, farmFertility } from './economy.js';
import { computeHappiness } from './population.js';
import { startFestival } from './events.js';
import { checkTutorial, sandboxContinue, skipTutorial } from './progress.js';

const COMMANDS = ['placeBuilding', 'placeRoad', 'removeRoad', 'demolish', 'setPriority', 'setPolicy', 'trade',
  'acceptOffer', 'scout', 'festival', 'buyUpgrade', 'continueSandbox', 'skipTutorial'];
const WON = 'The Royal Charter is complete. Continue in sandbox to keep building.';
const LOST = 'The game is over. Start a new kingdom or load a save.';
const MISSING = 'That command is missing information';
const POLICY_VALUES = { tax: ['low', 'normal', 'high'], rations: ['half', 'normal', 'full'], draftRate: ['off', 'light', 'full'] };
const POLICY_LABEL = { tax: 'Taxes', rations: 'Rations', draftRate: 'Draft' };
const PRIORITY_LABEL = { normal: 'Normal', priority: 'Priority', paused: 'Paused' };
const NEED_SUBJECT = { lumberCamp: 'A lumber camp', quarry: 'A quarry', mine: 'A mine' };
const TRADE_DONE_UNITS = 10; // section 6.2 notes: a sell of this many wood sets tutorial.tradeDone (no config key)

const isObj = (v) => v !== null && typeof v === 'object' && !Array.isArray(v);
const isInt = (v) => Number.isInteger(v);
const has = (obj, key) => typeof key === 'string' && Object.prototype.hasOwnProperty.call(obj, key);
const done = (message, id) => (id === undefined ? { ok: true, reason: null, message } : { ok: true, reason: null, id, message });
const refuse = (reason) => ({ ok: false, reason });
const fromDelegate = (r) => (r.ok ? done(r.message) : refuse(r.reason));
// Marks a map or building view stale so renderers rebuild (section 4.9). Commands always bump both.
const bump = (state, key) => { state.rev[key] += 1; };

// Footprint tile is placeable for this type: in bounds, explored, empty, no road, and right terrain.
function tileGood(state, type, t) {
  if (!inBounds(state, t.x, t.y)) return false;
  const i = idx(state, t.x, t.y);
  const m = state.map;
  if (m.explored[i] === 0 || m.building[i] !== 0 || m.road[i] !== 0) return false;
  return type === 'farm' ? (m.terrain[i] === TERRAIN.GRASS || m.terrain[i] === TERRAIN.MEADOW) : isBuildableLand(m.terrain[i]);
}

// PlacementCheck (section 3.10). Checks run in section 6.2 order; reason is the first failure, or null.
export function validatePlacement(state, type, x, y, rot) {
  const r = isInt(rot) ? ((rot % 4) + 4) % 4 : 0;
  const size = typeof type === 'string' && has(BUILDINGS, type) ? footprintSize(type, r) : { w: 0, h: 0 };
  const base = { type, x, y, rot: r, w: size.w, h: size.h, tiles: [], cost: {}, affordable: false, costReason: null,
    adjacentRoad: false, connected: false, yieldPerDay: null };
  const fails = (reason) => ({ ...base, ok: false, reason });
  if (typeof type !== 'string' || !has(BUILDINGS, type) || BUILDINGS[type].category === 'infra') return fails('Unknown building type');
  const def = BUILDINGS[type];
  base.cost = { ...def.cost };
  if (type === 'townHall' && state.buildings.some((b) => b.type === 'townHall')) return fails('Only one Town Hall');
  if (type === 'royalCharter' && state.buildings.some((b) => b.type === 'royalCharter')) {
    return fails('The Royal Charter is already built or underway');
  }
  if (def.tier > state.tier) return fails(`${def.name} unlocks at the ${TIME.tierNames[def.tier]} tier`);
  if (!isInt(x) || !isInt(y)) return fails('That spot is off the map');
  const tiles = footprintOf(type, x, y, r).tiles;
  base.tiles = tiles.map((t) => ({ x: t.x, y: t.y, ok: tileGood(state, type, t) }));
  if (tiles.some((t) => !inBounds(state, t.x, t.y))) return fails('That spot is off the map');
  const m = state.map;
  const at = (t) => idx(state, t.x, t.y);
  base.yieldPerDay = def.produces
    ? { resource: def.produces.resource, amount: def.needs?.kind === 'farm' ? def.produces.perDay * farmFertility(state, tiles) : def.produces.perDay }
    : null;
  if (tiles.some((t) => m.explored[at(t)] === 0)) return fails('That tile is unexplored. Scout this area first');
  if (tiles.some((t) => m.building[at(t)] !== 0)) return fails('A building is here. Pick an empty tile.');
  if (tiles.some((t) => m.road[at(t)] !== 0)) return fails('A road runs through that spot. Pick an empty tile.');
  const terr = tiles.map((t) => m.terrain[at(t)]);
  if (type === 'farm') {
    if (terr.some((c) => c !== TERRAIN.GRASS && c !== TERRAIN.MEADOW)) return fails('Farms need grass or meadow under every tile. Pick a green spot.');
  } else if (terr.some((c) => c === TERRAIN.MOUNTAIN || c === TERRAIN.RIVER || c === TERRAIN.LAKE)) {
    return fails('Mountains and water cannot hold buildings');
  } else if (terr.some((c) => !isBuildableLand(c))) {
    return fails('Build on grass, meadow or hill, not forest, stone or iron');
  }
  const need = def.needs;
  if (need?.kind === 'farm' && terr.filter((c) => c === TERRAIN.MEADOW).length < need.minMeadow) {
    return fails(`A farm needs at least ${need.minMeadow} meadow tiles`);
  }
  if (need?.kind === 'water' && !touchesWater(state, tiles)) return fails('A fishery needs river or lake water next to it');
  if (need?.kind === 'terrain' && resourceTilesNear(state, tiles, need.radius, TERRAIN[need.terrain.toUpperCase()]).length < need.min) {
    return fails(`${NEED_SUBJECT[type]} needs at least ${need.min} ${need.terrain} tiles within ${need.radius} tiles`);
  }
  const around = tiles.flatMap((t) => neighbours4(t.x, t.y, state.width, state.height));
  base.adjacentRoad = around.some((nb) => m.road[idx(state, nb.x, nb.y)] !== 0);
  base.connected = around.some((nb) => {
    const j = idx(state, nb.x, nb.y);
    return m.road[j] !== 0 && state.net.connected[j] === 1;
  });
  // Cost is read before the link check so an unconnected spot reports its true cost. Refusal order: link, then cost.
  const costReason = canAfford(state, def.cost);
  base.costReason = costReason;
  base.affordable = costReason === null;
  if (!base.connected) return fails('Needs a road connection to the Town Hall. Lay a road to this spot first.');
  if (costReason !== null) return fails(costReason);
  return { ...base, ok: true, reason: null };
}

// Tiles of the Town Hall footprint, as indices (roads may join the Hall).
function hallIndices(state) {
  const set = new Set();
  for (const b of state.buildings) {
    if (b.type !== 'townHall') continue;
    for (const t of footprintOf(b.type, b.x, b.y, b.rot).tiles) set.add(idx(state, t.x, t.y));
  }
  return set;
}

// Walks points in order (section 6.2 placeRoad). cost and newTiles are returned whole or not at all.
export function validateRoadPoints(state, points) {
  const cost = { wood: 0, stone: 0 };
  const out = (reason, newTiles = []) => ({
    ok: reason === null, reason, cost, bridges: newTiles.filter((t) => t.bridge).length, count: newTiles.length, newTiles,
  });
  const list = Array.isArray(points) ? points : [];
  if (list.length === 0) return out('Pick at least one tile');
  if (list.length > ECONOMY.maxRoadPoints) return out(`Roads can be at most ${ECONOMY.maxRoadPoints} tiles at once`);
  const m = state.map;
  const hall = hallIndices(state);
  const accepted = new Set();
  const newTiles = [];
  for (const p of list) {
    if (!isObj(p) || !isInt(p.x) || !isInt(p.y) || !inBounds(state, p.x, p.y)) return out('That spot is off the map');
    const i = idx(state, p.x, p.y);
    if (m.explored[i] === 0) return out('That tile is unexplored. Scout this area first');
    if (m.terrain[i] === TERRAIN.MOUNTAIN) return out('Mountains cannot carry roads');
    if (m.terrain[i] === TERRAIN.LAKE) return out('Lakes cannot carry roads');
    if (m.building[i] !== 0) return out('A building is in the way. Route the road around it.');
    if (m.road[i] !== 0 || accepted.has(i)) continue;
    const linked = neighbours4(p.x, p.y, state.width, state.height).some((nb) => {
      const j = idx(state, nb.x, nb.y);
      return (m.road[j] !== 0 && state.net.connected[j] === 1) || hall.has(j) || accepted.has(j);
    });
    if (!linked) return out('Roads must join the Town Hall or an existing road');
    accepted.add(i);
    newTiles.push({ x: p.x, y: p.y, bridge: m.terrain[i] === TERRAIN.RIVER });
  }
  if (newTiles.length === 0) return out('A road is already here. Drag from empty grass.');
  for (const t of newTiles) {
    const c = t.bridge ? BUILDINGS.bridge.cost : BUILDINGS.road.cost;
    cost.wood += c.wood || 0;
    cost.stone += c.stone || 0;
  }
  return out(canAfford(state, cost), newTiles);
}

// Wrong JS types in a payload (section 6.1 check 4). Ranges that are not types are checked by the command.
function payloadMissing(cmd) {
  switch (cmd.type) {
    case 'placeBuilding':
      return typeof cmd.buildingType !== 'string' || !isInt(cmd.x) || !isInt(cmd.y)
        || (cmd.rot !== undefined && (!isInt(cmd.rot) || cmd.rot < 0 || cmd.rot > 3));
    case 'placeRoad': {
      const hasPts = cmd.points !== undefined;
      const hasXY = cmd.x !== undefined || cmd.y !== undefined;
      if (hasPts === hasXY) return true;
      if (hasPts) return !Array.isArray(cmd.points) || cmd.points.some((p) => !isObj(p) || !isInt(p.x) || !isInt(p.y));
      return !isInt(cmd.x) || !isInt(cmd.y);
    }
    case 'removeRoad':
    case 'scout':
      return !isInt(cmd.x) || !isInt(cmd.y);
    case 'demolish':
      return !isInt(cmd.id);
    case 'acceptOffer':
      return !isInt(cmd.offerId);
    case 'setPriority':
      return !isInt(cmd.id) || typeof cmd.value !== 'string';
    case 'setPolicy':
      return typeof cmd.key !== 'string' || typeof cmd.value !== 'string';
    case 'trade':
      return typeof cmd.resource !== 'string' || typeof cmd.mode !== 'string' || !isInt(cmd.amount);
    case 'buyUpgrade':
      return typeof cmd.key !== 'string';
    default:
      return false;
  }
}

// Runs the tutorial's step checks at once after a placement or a sale, so a finished step shows without waiting
// for dawn (section 5.8). checkTutorial logs each move through emit, the same path the dawn pass uses, so the move reaches
// state.log. It moves one step per call; the loop takes every step the action finished, in order, and stops when no step moves.
function tutorialNow(state) {
  let moved = checkTutorial(state);
  while (moved.length > 0) moved = checkTutorial(state);
}

function placeBuilding(state, cmd) {
  const rot = cmd.rot === undefined ? 0 : cmd.rot;
  const c = validatePlacement(state, cmd.buildingType, cmd.x, cmd.y, rot);
  if (!c.ok) return refuse(c.reason);
  const def = BUILDINGS[cmd.buildingType];
  spend(state, def.cost);
  const id = state.nextBuildingId;
  state.nextBuildingId += 1;
  state.buildings.push({
    id, type: cmd.buildingType, x: cmd.x, y: cmd.y, rot, w: c.w, h: c.h, stage: 'building', progress: 0, builders: 0,
    stalled: 0, priority: 'normal', crew: 0, acc: 0, cooldown: 0, connected: false, roadSteps: -1,
    createdDay: state.day, lastHarvestDay: -1,
  });
  for (const t of c.tiles) state.map.building[idx(state, t.x, t.y)] = id;
  refreshNetwork(state);
  bump(state, 'map');
  bump(state, 'buildings');
  tutorialNow(state);
  return done(`${def.name} started: ${def.days} days of work.`, id);
}

function placeRoad(state, cmd) {
  const points = cmd.points !== undefined ? cmd.points : [{ x: cmd.x, y: cmd.y }];
  const r = validateRoadPoints(state, points);
  if (!r.ok) return refuse(r.reason);
  spend(state, r.cost);
  for (const t of r.newTiles) state.map.road[idx(state, t.x, t.y)] = t.bridge ? 2 : 1;
  refreshNetwork(state);
  bump(state, 'map');
  bump(state, 'buildings');
  tutorialNow(state);
  const tail = r.bridges > 0 ? `, ${r.cost.stone} stone` : '';
  return done(`Road laid: ${r.count} ${r.count === 1 ? 'tile' : 'tiles'} (${r.cost.wood} wood${tail})`);
}

// Removing a road is refused when it cuts off a complete or in-progress building that is connected now.
function removeRoad(state, cmd) {
  const { x, y } = cmd;
  if (!inBounds(state, x, y)) return refuse('That spot is off the map');
  const i = idx(state, x, y);
  const old = state.map.road[i];
  if (old === 0) return refuse('No road there');
  const before = state.buildings.filter((b) => b.connected).map((b) => b.id);
  state.map.road[i] = 0;
  refreshNetwork(state);
  const cut = before.filter((id) => !buildingById(state, id)?.connected).length;
  if (cut > 0) {
    state.map.road[i] = old;
    refreshNetwork(state);
    return refuse(`Removing this road would cut off ${cut} ${cut === 1 ? 'building' : 'buildings'}`);
  }
  bump(state, 'map');
  bump(state, 'buildings');
  return done('Road removed.');
}

function demolish(state, id) {
  const b = buildingById(state, id);
  if (!b) return refuse('Nothing to demolish there');
  if (b.type === 'townHall') return refuse('The Town Hall cannot be demolished');
  if (b.type === 'royalCharter') return refuse('The Royal Charter cannot be demolished');
  const def = BUILDINGS[b.type];
  const before = { ...state.stock };
  refund(state, def.cost, ECONOMY.demolishRefund);
  const parts = RESOURCE_KEYS.filter((k) => state.stock[k] > before[k]).map((k) => `${state.stock[k] - before[k]} ${k}`);
  for (const t of footprintOf(b.type, b.x, b.y, b.rot).tiles) state.map.building[idx(state, t.x, t.y)] = 0;
  state.buildings.splice(state.buildings.indexOf(b), 1);
  for (const c of state.citizens) {
    if (c.homeId === id) c.homeId = 0;
    if (c.workId === id) c.workId = 0;
  }
  refreshNetwork(state);
  bump(state, 'map');
  bump(state, 'buildings');
  bump(state, 'citizens');
  return done(`${def.name} demolished. Refund: ${parts.length > 0 ? parts.join(', ') : 'nothing'}`);
}

function setPriority(state, id, value) {
  const b = buildingById(state, id);
  if (!b) return refuse('That building no longer exists');
  if (!has(PRIORITY_LABEL, value)) return refuse('Priority must be normal, priority or paused');
  if (b.type === 'royalCharter') return refuse('The Royal Charter has no workers to assign');
  b.priority = value;
  bump(state, 'buildings');
  return done(`${BUILDINGS[b.type].name} is now ${PRIORITY_LABEL[value]}.`);
}

// Sets a policy (section 6.2). The happiness target and causes are recomputed at once (section 5.6), so the Kingdom view
// shows the new cause now. The happiness value itself still moves only at dawn (section 8.12).
function setPolicy(state, key, value) {
  if (!has(POLICY_VALUES, key)) return refuse('Unknown policy');
  if (!POLICY_VALUES[key].includes(value)) return refuse(`Unknown setting for ${key}`);
  state.policies[key] = value;
  const { target, causes } = computeHappiness(state);
  state.happinessTarget = target;
  state.happinessCauses = causes;
  return done(`${POLICY_LABEL[key]} set to ${value}.`);
}

// Reveals the explored disc around (x, y) for 5 gold (section 6.2 scout row).
function scout(state, x, y) {
  if (!inBounds(state, x, y)) return refuse('That spot is off the map');
  const m = state.map;
  if (m.explored[idx(state, x, y)] === 1) return refuse('That area is already explored');
  let near = Infinity;
  for (let j = 0; j < m.explored.length; j += 1) {
    if (m.explored[j] === 1) {
      const dx = Math.abs((j % state.width) - x);
      const dy = Math.abs(Math.floor(j / state.width) - y);
      near = Math.min(near, Math.max(dx, dy));
    }
  }
  if (near > ECONOMY.scoutRange) return refuse(`Scouts can only reach ${ECONOMY.scoutRange} tiles beyond your land`);
  if (state.stock.gold < ECONOMY.scoutCost) return refuse(`Scouting costs ${ECONOMY.scoutCost} gold; you have ${state.stock.gold}`);
  spend(state, { gold: ECONOMY.scoutCost });
  const R = ECONOMY.scoutRevealRadius;
  for (let dy = -R; dy <= R; dy += 1) {
    for (let dx = -R; dx <= R; dx += 1) {
      if (dx * dx + dy * dy <= R * R && inBounds(state, x + dx, y + dy)) m.explored[idx(state, x + dx, y + dy)] = 1;
    }
  }
  bump(state, 'map');
  return done(`Scouts charted the land around (${x}, ${y}).`);
}

function buyUpgrade(state, key) {
  if (!has(UPGRADES, key)) return refuse('Unknown upgrade');
  const u = UPGRADES[key];
  if (state.upgrades[key]) return refuse(`${u.name} is already bought`);
  if (u.tier > state.tier) return refuse(`${u.name} needs the ${TIME.tierNames[u.tier]} tier`);
  const reason = spend(state, u.cost);
  if (reason !== null) return refuse(reason);
  state.upgrades[key] = true;
  return done(`${u.name} bought. ${u.text}`);
}

function dispatch(state, cmd) {
  switch (cmd.type) {
    case 'placeBuilding': return placeBuilding(state, cmd);
    case 'placeRoad': return placeRoad(state, cmd);
    case 'removeRoad': return removeRoad(state, cmd);
    case 'demolish': return demolish(state, cmd.id);
    case 'setPriority': return setPriority(state, cmd.id, cmd.value);
    case 'setPolicy': return setPolicy(state, cmd.key, cmd.value);
    case 'trade': {
      const r = applyTrade(state, cmd.resource, cmd.mode, cmd.amount);
      if (r.ok && cmd.mode === 'sell') {
        if (cmd.resource === 'wood' && cmd.amount >= TRADE_DONE_UNITS) state.tutorial.tradeDone = true;
        tutorialNow(state);   // a sale can finish step 5, so the banner moves in this action, as a placement's does
      }
      return fromDelegate(r);
    }
    case 'acceptOffer': {
      const offer = state.offers.find((o) => o.id === cmd.offerId);
      const r = applyCaravanDeal(state, cmd.offerId);
      if (r.ok && offer?.kind === 'buy') tutorialNow(state);   // the caravan buys from the player: a sale, as above
      return fromDelegate(r);
    }
    case 'scout': return scout(state, cmd.x, cmd.y);
    case 'festival': return fromDelegate(startFestival(state, []));
    case 'buyUpgrade': return buyUpgrade(state, cmd.key);
    case 'continueSandbox': return fromDelegate(sandboxContinue(state));
    case 'skipTutorial': return fromDelegate(skipTutorial(state));
    default: return refuse('Unknown command');
  }
}

// Applies one player command (section 6). Refusals change nothing. Never throws.
export function applyCommand(state, cmd) {
  try {
    ensureRuntime(state);
    if (!isObj(cmd) || !COMMANDS.includes(cmd.type)) return refuse('Unknown command');
    const status = state.outcome.status;
    if (status === 'won' && cmd.type !== 'continueSandbox') return refuse(WON);
    if (status === 'lost') return refuse(LOST);
    if (payloadMissing(cmd)) return refuse(MISSING);
    return dispatch(state, cmd);
  } catch (e) {
    return refuse(MISSING);
  }
}
