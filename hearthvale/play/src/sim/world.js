// owner: foundation
// Section 3.4: map generation (section 5.10), footprints, the road network and road planning. Pure.
import { TERRAIN, ensureRuntime, inBounds } from './state.js';
import { mulberry32, hash2 } from './rng.js';
import { BUILDINGS } from '../config/buildings.js';
import { MAP } from '../config/map.js';

const DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1]];
const ROADABLE = [TERRAIN.GRASS, TERRAIN.MEADOW, TERRAIN.FOREST, TERRAIN.HILL, TERRAIN.STONE, TERRAIN.IRON, TERRAIN.RIVER];
const sq = (v) => v * v;
const hasType = (type) => Object.prototype.hasOwnProperty.call(BUILDINGS, type);
const forEachTile = (width, height, fn) => {
  for (let y = 0; y < height; y += 1) for (let x = 0; x < width; x += 1) fn(y * width + x, x, y);
};

export function footprintSize(type, rot) {
  if (!hasType(type)) return { w: 0, h: 0 };
  const b = BUILDINGS[type];
  return rot === 1 || rot === 3 ? { w: b.h, h: b.w } : { w: b.w, h: b.h };
}

export function footprintOf(type, x, y, rot) {
  const { w, h } = footprintSize(type, rot);
  const tiles = [];
  for (let dy = 0; dy < h; dy += 1) for (let dx = 0; dx < w; dx += 1) tiles.push({ x: x + dx, y: y + dy });
  return { w, h, tiles };
}

export function neighbours4(x, y, width, height) {
  return DIRS.map(([dx, dy]) => ({ x: x + dx, y: y + dy }))
    .filter((p) => p.x >= 0 && p.y >= 0 && p.x < width && p.y < height);
}

export function isBuildableLand(terrainCode) {
  return terrainCode === TERRAIN.GRASS || terrainCode === TERRAIN.MEADOW || terrainCode === TERRAIN.HILL;
}

export function isRoadable(terrainCode) {
  return ROADABLE.includes(terrainCode);
}

// Value noise on integer lattice hashes, bilinear with smoothstep. No trigonometry.
function valueNoise(x, y, cell, salt) {
  const gx = x / cell;
  const gy = y / cell;
  const ix = Math.floor(gx);
  const iy = Math.floor(gy);
  const fx = gx - ix;
  const fy = gy - iy;
  const ux = fx * fx * (3 - 2 * fx);
  const uy = fy * fy * (3 - 2 * fy);
  const a = hash2(ix, iy, salt);
  const b = hash2(ix + 1, iy, salt);
  const c = hash2(ix, iy + 1, salt);
  const d = hash2(ix + 1, iy + 1, salt);
  const top = a + (b - a) * ux;
  const bottom = c + (d - c) * ux;
  return top + (bottom - top) * uy;
}

// Distinct noise stream per layer k of the seed.
const layerSalt = (seed, k) => (seed + Math.imul(k + 1, 0x9E3779B1)) >>> 0;

// One attempt for seed s: terrain, heights, deposits and explored flags. plat marks the Hall platform.
function buildRaw(s, width, height) {
  const n = width * height;
  const terrain = new Uint8Array(n);
  const deposit = new Uint16Array(n);
  const explored = new Uint8Array(n);
  const heights = new Uint8Array(n);
  const plat = new Uint8Array(n);
  const elev = new Float64Array(n);
  const E = MAP.elevation;
  const R = MAP.river;
  const edge = MAP.edgeWidth;
  const half = width / 2;
  const isEdge = (x, y) => x < edge || y < edge || x >= width - edge || y >= height - edge;
  const d2hall = (x, y) => sq(x - MAP.hall.x) + sq(y - MAP.hall.y);
  const platR2 = sq(MAP.hallPlatform.radius);
  const rnd = mulberry32(s);
  const span = MAP.timber.max - MAP.timber.min + 1;
  forEachTile(width, height, (i, x, y) => {
    let e = 0;
    E.cells.forEach((cell, k) => { e += E.weights[k] * valueNoise(x, y, cell, layerSalt(s, k)); });
    const d2 = d2hall(x, y);
    e -= E.bowl * Math.sqrt(d2) / half;
    elev[i] = e;
    let t = TERRAIN.GRASS;
    if (isEdge(x, y) || e > MAP.mountainAt) t = TERRAIN.MOUNTAIN;
    else if (e > MAP.hillAt) t = TERRAIN.HILL;
    if (d2 <= platR2) {
      plat[i] = 1;
      t = TERRAIN.GRASS;
      elev[i] = MAP.hallPlatform.height;
    }
    terrain[i] = t;
  });
  // River: one column per row, jittering by -1, 0 or 1 and clamped. Never on the edge rim.
  let rx = R.startX;
  for (let y = 0; y < height; y += 1) {
    if (y > 0) rx = Math.min(R.maxX, Math.max(R.minX, rx + Math.floor(rnd() * 3) - 1));
    for (let k = 0; k < R.width; k += 1) {
      const x = rx + k;
      if (x < width && !isEdge(x, y) && !plat[y * width + x]) terrain[y * width + x] = TERRAIN.RIVER;
    }
  }
  forEachTile(width, height, (i, x, y) => {
    if (!isEdge(x, y) && !plat[i] && sq(x - MAP.lake.x) + sq(y - MAP.lake.y) <= sq(MAP.lake.radius)) terrain[i] = TERRAIN.LAKE;
  });
  forEachTile(width, height, (i, x, y) => {
    if (terrain[i] === TERRAIN.GRASS && !plat[i] && valueNoise(x, y, MAP.meadow.cell, layerSalt(s, 3)) >= MAP.meadow.min) {
      terrain[i] = TERRAIN.MEADOW;
    }
  });
  forEachTile(width, height, (i, x, y) => {
    if (terrain[i] === TERRAIN.GRASS && !plat[i] && x < R.minX && valueNoise(x, y, MAP.forest.cell, layerSalt(s, 4)) >= MAP.forest.min) {
      terrain[i] = TERRAIN.FOREST;
      deposit[i] = MAP.timber.min + Math.floor(rnd() * span);
    }
  });
  forEachTile(width, height, (i, x, y) => {
    if (terrain[i] === TERRAIN.HILL && !plat[i] && valueNoise(x, y, MAP.stone.cell, layerSalt(s, 5)) >= MAP.stone.min) {
      terrain[i] = TERRAIN.STONE;
      deposit[i] = MAP.stoneDeposit;
    }
  });
  forEachTile(width, height, (i, x, y) => {
    if (terrain[i] === TERRAIN.HILL && !plat[i] && x >= MAP.iron.minX && valueNoise(x, y, MAP.iron.cell, layerSalt(s, 6)) >= MAP.iron.min) {
      terrain[i] = TERRAIN.IRON;
      deposit[i] = MAP.ironDeposit;
    }
  });
  forEachTile(width, height, (i, x, y) => {
    explored[i] = d2hall(x, y) <= sq(MAP.exploredRadius) ? 1 : 0;
    const h = terrain[i] === TERRAIN.MOUNTAIN ? Math.max(elev[i], MAP.mountainAt) : elev[i];
    heights[i] = Math.round(Math.min(1, Math.max(0, h)) * 255);
  });
  return { terrain, height: heights, deposit, explored, plat };
}

// Tiles reachable from the Hall centre over non-mountain, non-lake tiles.
function reachMask(terrain, width, height) {
  const reach = new Uint8Array(width * height);
  const q = [MAP.hall.y * width + MAP.hall.x];
  reach[q[0]] = 1;
  for (let k = 0; k < q.length; k += 1) {
    const i = q[k];
    const x = i % width;
    for (const nb of neighbours4(x, (i - x) / width, width, height)) {
      const j = nb.y * width + nb.x;
      if (!reach[j] && terrain[j] !== TERRAIN.MOUNTAIN && terrain[j] !== TERRAIN.LAKE) {
        reach[j] = 1;
        q.push(j);
      }
    }
  }
  return reach;
}

// Guarantee counts over reachable tiles, and whether every guarantee is met.
function tally(raw, width, height) {
  const reach = reachMask(raw.terrain, width, height);
  const g = MAP.guarantees;
  const c = { meadow: 0, forest: 0, stone: 0, iron: 0 };
  forEachTile(width, height, (i, x, y) => {
    if (!reach[i]) return;
    const d2 = sq(x - MAP.hall.x) + sq(y - MAP.hall.y);
    const t = raw.terrain[i];
    if (t === TERRAIN.MEADOW && d2 <= sq(g.meadowRadius)) c.meadow += 1;
    else if (t === TERRAIN.FOREST && d2 <= sq(g.forestRadius)) c.forest += 1;
    else if (t === TERRAIN.STONE && d2 <= sq(g.stoneRadius)) c.stone += 1;
    else if (t === TERRAIN.IRON && d2 >= sq(g.ironMinDist) && d2 <= sq(g.ironMaxDist)) c.iron += 1;
  });
  c.ok = c.meadow >= g.meadowWithin9 && c.forest >= g.forestWithin12 && c.stone >= g.stoneWithin12 && c.iron >= g.ironCount;
  return c;
}

// Forced fallback after every attempt failed. Opens interior mountains near the Hall, then converts
// lowland and hill tiles. Never touches the platform, the edge rim, river or lake.
function carve(raw, width, height, s) {
  const { terrain, deposit, plat } = raw;
  const rnd = mulberry32(s);
  const g = MAP.guarantees;
  const n = width * height;
  const TG = TERRAIN.GRASS;
  const TH = TERRAIN.HILL;
  const d2 = (i) => sq((i % width) - MAP.hall.x) + sq(Math.floor(i / width) - MAP.hall.y);
  const edge = MAP.edgeWidth;
  const openR2 = sq(g.ironMaxDist);
  forEachTile(width, height, (i, x, y) => {
    const interior = x >= edge && y >= edge && x < width - edge && y < height - edge;
    if (interior && terrain[i] === TERRAIN.MOUNTAIN && d2(i) <= openR2) terrain[i] = TH;
  });
  const reach = reachMask(terrain, width, height);
  const pool = (test) => {
    const list = [];
    for (let i = 0; i < n; i += 1) if (reach[i] && !plat[i] && test(i)) list.push(i);
    return list.sort((a, b) => d2(a) - d2(b) || a - b);
  };
  const count = (test) => {
    let c = 0;
    for (let i = 0; i < n; i += 1) if (reach[i] && test(i)) c += 1;
    return c;
  };
  const within = (t, r) => (i) => terrain[i] === t && d2(i) <= sq(r);
  const deposits = { [TERRAIN.STONE]: MAP.stoneDeposit, [TERRAIN.IRON]: MAP.ironDeposit };
  const make = (i, to) => {
    terrain[i] = to;
    if (to === TERRAIN.FOREST) deposit[i] = MAP.timber.min + Math.floor(rnd() * (MAP.timber.max - MAP.timber.min + 1));
    else deposit[i] = deposits[to] || 0;
  };
  const fill = (list, want, to) => {
    const take = list.slice(0, Math.max(0, want));
    for (const i of take) make(i, to);
    return take.length;
  };
  let need = g.meadowWithin9 - count(within(TERRAIN.MEADOW, g.meadowRadius));
  if (need > 0) need -= fill(pool(within(TG, g.meadowRadius)), need, TERRAIN.MEADOW);
  if (need > 0) fill(pool(within(TH, g.meadowRadius)), need, TERRAIN.MEADOW);
  need = g.forestWithin12 - count(within(TERRAIN.FOREST, g.forestRadius));
  if (need > 0) {
    const east = (i) => (i % width >= MAP.river.minX ? 1 : 0);
    const forest = pool(within(TG, g.forestRadius)).sort((a, b) => east(a) - east(b) || d2(a) - d2(b) || a - b);
    need -= fill(forest, need, TERRAIN.FOREST);
  }
  if (need > 0) fill(pool(within(TH, g.forestRadius)), need, TERRAIN.FOREST);
  need = g.stoneWithin12 - count(within(TERRAIN.STONE, g.stoneRadius));
  if (need > 0) need -= fill(pool(within(TH, g.stoneRadius)), need, TERRAIN.STONE);
  if (need > 0) fill(pool(within(TG, g.stoneRadius)), need, TERRAIN.STONE);
  const inIron = (i) => d2(i) >= sq(g.ironMinDist) && d2(i) <= sq(g.ironMaxDist);
  need = g.ironCount - count((i) => terrain[i] === TERRAIN.IRON && inIron(i));
  if (need > 0) {
    const iron = pool((i) => (terrain[i] === TH || terrain[i] === TG) && i % width >= MAP.iron.minX && inIron(i));
    iron.sort((a, b) => (terrain[a] === TH ? 0 : 1) - (terrain[b] === TH ? 0 : 1) || d2(a) - d2(b) || a - b);
    fill(iron, need, TERRAIN.IRON);
  }
}

// Pure function of its arguments. Tries seeds seed, seed + 1, ... until the guarantees hold.
export function generateMap(seed, width, height) {
  const attempts = MAP.attempts;
  let raw = null;
  let last = seed >>> 0;
  let a = 0;
  for (; a < attempts; a += 1) {
    last = (seed + a) >>> 0;
    raw = buildRaw(last, width, height);
    if (tally(raw, width, height).ok) break;
  }
  const forced = a === attempts;
  if (forced) carve(raw, width, height, last);
  return {
    terrain: raw.terrain,
    height: raw.height,
    deposit: raw.deposit,
    explored: raw.explored,
    hall: { x: MAP.hall.x, y: MAP.hall.y },
    door: { x: MAP.door.x, y: MAP.door.y },
    starterRoad: MAP.starterRoad.map((p) => ({ x: p.x, y: p.y })),
    attempt: forced ? attempts - 1 : a,
    forced,
  };
}

// Recomputes state.net and every building's connected and roadSteps. Returns the complete buildings cut off.
export function refreshNetwork(state) {
  ensureRuntime(state);
  const W = state.width;
  const H = state.height;
  const road = state.map.road;
  const conn = state.net.connected;
  const dist = state.net.dist;
  const before = state.buildings.map((b) => b.connected === true);
  conn.fill(0);
  dist.fill(-1);
  const q = [];
  const visit = (j, d) => { conn[j] = 1; dist[j] = d; q.push(j); };
  // The Town Hall footprint is the root: roads beside it are the door road, at road step 1.
  const halls = state.buildings.filter((b) => b.type === 'townHall').flatMap((b) => footprintOf(b.type, b.x, b.y, b.rot).tiles);
  for (const t of halls) {
    for (const nb of neighbours4(t.x, t.y, W, H)) {
      const j = nb.y * W + nb.x;
      if (road[j] !== 0 && conn[j] === 0) visit(j, 1);
    }
  }
  for (let k = 0; k < q.length; k += 1) {
    const i = q[k];
    const x = i % W;
    for (const nb of neighbours4(x, (i - x) / W, W, H)) {
      const j = nb.y * W + nb.x;
      if (road[j] !== 0 && conn[j] === 0) visit(j, dist[i] + 1);
    }
  }
  const cutOff = [];
  state.buildings.forEach((b, k) => {
    if (b.type === 'townHall') {
      b.connected = true;
      b.roadSteps = 0;
    } else {
      let best = -1;
      for (const t of footprintOf(b.type, b.x, b.y, b.rot).tiles) {
        for (const nb of neighbours4(t.x, t.y, W, H)) {
          const j = nb.y * W + nb.x;
          if (conn[j] === 1 && (best < 0 || dist[j] < best)) best = dist[j];
        }
      }
      b.roadSteps = best;
      b.connected = best >= 0;
    }
    if (before[k] && !b.connected && b.stage === 'complete') cutOff.push(b.id);
  });
  return { cutOff };
}

// Tiles of terrainCode with deposit > 0 within Chebyshev radius of any tile. Ascending index order.
export function resourceTilesNear(state, tiles, radius, terrainCode) {
  const found = new Set();
  for (const p of tiles) {
    for (let y = p.y - radius; y <= p.y + radius; y += 1) {
      for (let x = p.x - radius; x <= p.x + radius; x += 1) {
        if (!inBounds(state, x, y)) continue;
        const i = y * state.width + x;
        if (state.map.terrain[i] === terrainCode && state.map.deposit[i] > 0) found.add(i);
      }
    }
  }
  return [...found].sort((a, b) => a - b);
}

export function touchesWater(state, tiles) {
  return tiles.some((p) => neighbours4(p.x, p.y, state.width, state.height).some((nb) => {
    const k = state.map.terrain[nb.y * state.width + nb.x];
    return k === TERRAIN.RIVER || k === TERRAIN.LAKE;
  }));
}

function passable(m, i) {
  return m.explored[i] === 1 && isRoadable(m.terrain[i]) && m.building[i] === 0 && m.road[i] === 0;
}

// Shortest path of new road tiles from the network (or the Hall footprint) to (toX, toY).
export function planRoad(state, toX, toY) {
  if (!inBounds(state, toX, toY)) return null;
  ensureRuntime(state);
  const W = state.width;
  const H = state.height;
  const m = state.map;
  const conn = state.net.connected;
  const ti = toY * W + toX;
  if (m.road[ti] !== 0) return { points: [], bridges: 0 };
  if (!passable(m, ti)) return null;
  const hallMark = new Uint8Array(W * H);
  for (const b of state.buildings.filter((hb) => hb.type === 'townHall')) {
    for (const t of footprintOf(b.type, b.x, b.y, b.rot).tiles) if (inBounds(state, t.x, t.y)) hallMark[t.y * W + t.x] = 1;
  }
  const prev = new Int32Array(W * H).fill(-1);
  const seen = new Uint8Array(W * H);
  const q = [];
  forEachTile(W, H, (i, x, y) => {
    if (!passable(m, i)) return;
    const touches = neighbours4(x, y, W, H).some((nb) => {
      const j = nb.y * W + nb.x;
      return (m.road[j] !== 0 && conn[j] === 1) || hallMark[j] === 1;
    });
    if (touches) {
      seen[i] = 1;
      q.push(i);
    }
  });
  for (let k = 0; k < q.length && seen[ti] === 0; k += 1) {
    const i = q[k];
    const x = i % W;
    for (const nb of neighbours4(x, (i - x) / W, W, H)) {
      const j = nb.y * W + nb.x;
      if (seen[j] === 0 && passable(m, j)) {
        seen[j] = 1;
        prev[j] = i;
        q.push(j);
      }
    }
  }
  if (seen[ti] === 0) return null;
  const path = [];
  for (let i = ti; i !== -1; i = prev[i]) path.unshift(i);
  let bridges = 0;
  const points = path.map((i) => {
    if (m.terrain[i] === TERRAIN.RIVER) bridges += 1;
    const x = i % W;
    return { x, y: (i - x) / W };
  });
  return { points, bridges };
}

export function connectedRoadCount(state) {
  ensureRuntime(state);
  let c = 0;
  for (let i = 0; i < state.map.road.length; i += 1) {
    if (state.map.road[i] !== 0 && state.net.connected[i] === 1) c += 1;
  }
  return c;
}
