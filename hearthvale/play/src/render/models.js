// owner: render-structures
// Section 9.4: procedural low-poly models, built once and cached by getModels().
// Every entry is {parts: [{geometry, color, offset: [x, y, z]}], width, depth, height, ...anchors}.
// offset is the centre of the part. Building models stand on the ground (y = 0) at the centre of their rot-0
// footprint: x runs along w, z runs along h, and doors face +z (south). Use rotationOf(rot) for the Y turn.
// Only BoxGeometry, ConeGeometry, CylinderGeometry and SphereGeometry are used.
import * as THREE from 'three';
import { PALETTE } from './palette.js';
import { BUILDINGS } from '../config/buildings.js';
import { TERRAIN } from '../sim/state.js';

// Presentation values for the terrain height rule (mirrors terrain.js; render only, never read by the sim).
const LEVEL = 2.2 / 255, MOUNTAIN_LIFT = 0.35, BED_Y = 0.2, BRIDGE_Y = 0.37, ROAD_LIFT = 0.03;

// Colours that PALETTE does not name (presentation only).
const LOCAL = {
  window: 0x4d6a78, door: 0x5a3a22, brick: 0x8a4b3a, sack: 0xd9c79a, hole: 0x1c1714,
  legs: 0x3b3328, leather: 0x3b3328, skin: 0xe8b98d, horse: 0x6b4a2b, soil: 0x4a3424,
};

const QUARTER = Math.PI / 4; // yaw that turns a 4-sided cone into a square pyramid with edges on the axes

const box = (w, h, d) => new THREE.BoxGeometry(w, h, d);
const cyl = (rTop, rBottom, h, seg) => new THREE.CylinderGeometry(rTop, rBottom, h, seg);
const ball = (r, ws, hs) => new THREE.SphereGeometry(r, ws, hs);
const cone = (r, h, seg, yaw = 0) => {
  const g = new THREE.ConeGeometry(r, h, seg);
  if (yaw) g.rotateY(yaw);
  return g;
};
const part = (geometry, color, x, y, z) => ({ geometry, color, offset: [x, y, z] });
// Cone radius for a square pyramid roof over a square of half-width `half` (corners sit just past the walls).
const pyramid = (half) => half * Math.SQRT2 * 1.06;
// Joins {geometry, offset} items into one BufferGeometry, so a single InstancedMesh can draw the whole shape.
function mergeGeometry(items) {
  const pos = [], nor = [], idx = [];
  let base = 0;
  for (const it of items) {
    const g = it.geometry.clone();
    g.translate(it.offset[0], it.offset[1], it.offset[2]);
    const p = g.attributes.position, n = g.attributes.normal;
    for (let i = 0; i < p.count; i++) {
      pos.push(p.getX(i), p.getY(i), p.getZ(i));
      nor.push(n.getX(i), n.getY(i), n.getZ(i));
    }
    if (g.index) for (let i = 0; i < g.index.count; i++) idx.push(g.index.getX(i) + base);
    else for (let i = 0; i < p.count; i++) idx.push(base + i);
    base += p.count;
    g.dispose();
  }
  const out = new THREE.BufferGeometry();
  out.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  out.setAttribute('normal', new THREE.Float32BufferAttribute(nor, 3));
  out.setIndex(idx);
  return out;
}
// Season index 0..3 for a day: 12 days per season, 48 per year (section 5.1).
export function seasonOf(day) {
  return Math.floor((day % 48) / 12);
}

// Building definitions (rot-0 footprint). Anchors: chimney (smoke top), flag (pole base), hub (windmill).
const BUILDERS = {
  townHall: () => ({
    parts: [
      part(box(2.4, 1.2, 2.4), PALETTE.plaster, 0, 0.6, 0),
      part(cone(pyramid(1.2), 0.9, 4, QUARTER), PALETTE.roofRed, 0, 1.65, 0),
      part(box(0.5, 0.8, 0.06), LOCAL.door, 0, 0.4, 1.21),
      part(box(0.3, 0.32, 0.06), LOCAL.window, -0.8, 0.8, 1.21),
      part(box(0.3, 0.32, 0.06), LOCAL.window, 0.8, 0.8, 1.21),
    ],
    flag: [0, 2.1, 0],
  }),
  cottage: () => ({
    parts: [
      part(box(0.7, 0.5, 0.7), PALETTE.plaster, 0, 0.25, 0),
      part(cone(pyramid(0.35), 0.42, 4, QUARTER), PALETTE.roofRed, 0, 0.71, 0),
      part(box(0.12, 0.4, 0.12), LOCAL.brick, 0.2, 0.8, -0.16),
      part(box(0.16, 0.26, 0.04), LOCAL.door, 0, 0.13, 0.36),
    ],
    chimney: [0.2, 1.0, -0.16],
  }),
  townhouse: () => ({
    parts: [
      part(box(1.7, 1.1, 1.7), PALETTE.plaster, 0, 0.55, 0),
      part(cone(pyramid(0.85), 0.7, 4, QUARTER), PALETTE.roofSlate, 0, 1.45, 0),
      part(box(0.2, 0.5, 0.2), LOCAL.brick, 0.5, 1.35, -0.5),
      part(box(0.3, 0.3, 0.04), LOCAL.window, -0.45, 0.7, 0.87),
      part(box(0.3, 0.3, 0.04), LOCAL.window, 0.45, 0.7, 0.87),
      part(box(0.26, 0.5, 0.05), LOCAL.door, 0, 0.27, 0.87),
    ],
    chimney: [0.5, 1.6, -0.5],
  }),
  farm: () => ({
    parts: [
      part(box(1.1, 0.7, 0.9), PALETTE.timber, -0.3, 0.35, -0.35),
      part(cone(pyramid(0.55), 0.45, 4, QUARTER), PALETTE.roofRed, -0.3, 0.925, -0.35),
      part(cyl(0.1, 0.14, 1.0, 6), PALETTE.plaster, 0.6, 0.5, 0.55),
      part(cone(0.16, 0.2, 6), PALETTE.roofSlate, 0.6, 1.1, 0.55),
    ],
    hub: [0.6, 0.92, 0.7],
  }),
  fishery: () => ({
    parts: [
      part(box(1.3, 0.5, 0.8), PALETTE.timber, -0.15, 0.25, 0),
      part(box(1.44, 0.12, 0.96), PALETTE.thatch, -0.15, 0.56, 0),
      part(box(0.6, 0.05, 0.5), LOCAL.soil, 0.8, 0.03, 0),
    ],
  }),
  lumberCamp: () => ({
    parts: [
      part(box(1.1, 0.6, 1.0), PALETTE.timber, -0.35, 0.3, -0.35),
      part(cone(pyramid(0.55), 0.4, 4, QUARTER), PALETTE.thatch, -0.35, 0.8, -0.35),
      part(box(0.7, 0.22, 0.3), PALETTE.trunk, 0.6, 0.11, 0.55),
      part(box(0.7, 0.22, 0.3), PALETTE.trunk, 0.6, 0.33, 0.55),
    ],
  }),
  quarry: () => ({
    parts: [
      part(box(1.1, 0.5, 0.9), PALETTE.stone, -0.35, 0.25, -0.3),
      part(box(0.7, 0.36, 0.6), PALETTE.stone, 0.5, 0.18, 0.45),
      part(box(0.1, 1.0, 0.1), PALETTE.timber, 0.5, 0.5, -0.5),
      part(box(0.7, 0.08, 0.08), PALETTE.timber, 0.15, 0.96, -0.5),
    ],
  }),
  mine: () => ({
    parts: [
      part(cone(0.8, 0.5, 6), PALETTE.iron, 0.25, 0.25, 0.25),
      part(box(0.9, 0.75, 0.12), PALETTE.timber, -0.35, 0.375, 0.62),
      part(box(0.5, 0.55, 0.14), LOCAL.hole, -0.35, 0.3, 0.66),
    ],
  }),
  workshop: () => ({
    parts: [
      part(box(1.5, 0.9, 1.2), PALETTE.plaster, -0.2, 0.45, -0.2),
      part(cone(pyramid(0.75), 0.55, 4, QUARTER), PALETTE.roofSlate, -0.2, 1.175, -0.2),
      part(box(0.22, 0.7, 0.22), LOCAL.brick, 0.4, 1.0, -0.45),
      part(box(0.5, 0.25, 0.3), PALETTE.iron, 0.45, 0.125, 0.5),
    ],
    chimney: [0.4, 1.35, -0.45],
  }),
  market: () => ({
    parts: [
      part(box(1.6, 0.5, 0.7), PALETTE.timber, 0, 0.25, 0.4),
      part(box(1.9, 0.06, 1.9), PALETTE.roofRed, 0, 1.0, 0),
      part(box(0.08, 1.0, 0.08), PALETTE.timber, -0.85, 0.5, -0.85),
      part(box(0.5, 0.35, 0.5), PALETTE.thatch, -0.45, 0.175, 0.4),
    ],
  }),
  tavern: () => ({
    parts: [
      part(box(1.6, 0.95, 1.4), PALETTE.plaster, 0, 0.475, 0),
      part(cone(pyramid(0.8), 0.6, 4, QUARTER), PALETTE.roofRed, 0, 1.25, 0),
      part(box(0.6, 0.3, 0.05), PALETTE.gold, 0, 0.7, 0.74),
      part(box(0.2, 0.5, 0.2), LOCAL.brick, -0.5, 1.2, -0.45),
      part(box(0.28, 0.3, 0.04), LOCAL.window, 0.4, 0.55, 0.72),
    ],
    chimney: [-0.5, 1.45, -0.45],
  }),
  chapel: () => ({
    parts: [
      part(box(1.2, 1.0, 1.6), PALETTE.plaster, 0, 0.5, 0),
      part(box(1.3, 0.25, 1.7), PALETTE.roofSlate, 0, 1.125, 0),
      part(cone(0.36, 1.0, 8), PALETTE.roofSlate, 0, 1.75, -0.25),
      part(box(0.07, 0.3, 0.07), PALETTE.gold, 0, 2.4, -0.25),
    ],
  }),
  storehouse: () => ({
    parts: [
      part(box(1.8, 1.0, 1.4), PALETTE.timber, 0, 0.5, 0),
      part(cone(pyramid(0.9), 0.5, 4, QUARTER), PALETTE.roofSlate, 0, 1.25, 0),
      part(box(0.5, 0.4, 0.5), PALETTE.thatch, -0.55, 0.2, 0.55),
    ],
  }),
  granary: () => ({
    parts: [
      part(cyl(0.7, 0.7, 1.4, 10), LOCAL.sack, -0.2, 0.7, -0.2),
      part(cone(0.74, 0.5, 10), PALETTE.roofSlate, -0.2, 1.65, -0.2),
      part(box(0.8, 0.5, 0.9), PALETTE.timber, 0.55, 0.25, 0.4),
    ],
  }),
  well: () => ({
    parts: [
      part(cyl(0.32, 0.36, 0.45, 8), PALETTE.stone, 0, 0.225, 0),
      part(cyl(0.26, 0.26, 0.02, 8), PALETTE.river, 0, 0.46, 0),
      part(box(0.06, 0.6, 0.06), PALETTE.timber, -0.28, 0.75, 0),
      part(box(0.06, 0.6, 0.06), PALETTE.timber, 0.28, 0.75, 0),
      part(cone(0.4, 0.25, 4, QUARTER), PALETTE.thatch, 0, 1.17, 0),
    ],
  }),
  watchtower: () => ({
    parts: [
      part(box(0.5, 1.6, 0.5), PALETTE.stone, 0, 0.8, 0),
      part(box(0.7, 0.1, 0.7), PALETTE.timber, 0, 1.65, 0),
      part(cone(pyramid(0.42), 0.35, 4, QUARTER), PALETTE.roofRed, 0, 1.875, 0),
    ],
    flag: [0, 2.05, 0],
  }),
  barracks: () => ({
    parts: [
      part(box(1.9, 0.9, 1.1), PALETTE.stone, 0, 0.45, -0.2),
      part(box(2.0, 0.2, 1.2), PALETTE.roofRed, 0, 1.0, -0.2),
      part(box(0.6, 0.6, 0.06), PALETTE.timber, 0, 0.3, 0.37),
      part(box(0.7, 0.45, 0.4), PALETTE.iron, 0.6, 0.225, 0.7),
    ],
    flag: [0.8, 1.1, -0.2],
  }),
  clinic: () => ({
    parts: [
      part(box(1.6, 0.9, 1.4), PALETTE.plaster, 0, 0.45, 0),
      part(cone(pyramid(0.8), 0.5, 4, QUARTER), PALETTE.roofRed, 0, 1.15, 0),
      part(box(0.1, 0.36, 0.05), PALETTE.bandit, 0, 0.65, 0.73),
      part(box(0.36, 0.1, 0.05), PALETTE.bandit, 0, 0.65, 0.73),
    ],
  }),
  royalCharter: () => ({
    parts: [
      part(box(2.2, 1.4, 2.2), PALETTE.stone, 0, 0.7, 0),
      part(cone(pyramid(1.1), 0.9, 4, QUARTER), PALETTE.roofRed, 0, 1.85, 0),
      part(cyl(0.3, 0.32, 2.4, 10), PALETTE.stone, 1.0, 1.2, 1.0),
      part(cone(0.36, 0.6, 10), PALETTE.roofSlate, 1.0, 2.7, 1.0),
      part(box(0.35, 0.22, 0.35), PALETTE.gold, 0, 2.41, 0),
    ],
    flag: [1.0, 3.0, 1.0],
  }),
};

// Measures a model from its parts: width (x), depth (z) and height (top of the highest part).
function finish(def) {
  const all = new THREE.Box3();
  const one = new THREE.Box3();
  const at = new THREE.Vector3();
  for (const p of def.parts) {
    p.geometry.computeBoundingBox();
    one.copy(p.geometry.boundingBox).translate(at.set(p.offset[0], p.offset[1], p.offset[2]));
    all.union(one);
  }
  const size = all.getSize(new THREE.Vector3());
  def.width = size.x;
  def.depth = size.z;
  def.height = all.max.y;
  return def;
}

let cache = null;

// Cached model definitions. Building types are flat keys (getModels().cottage.parts) and also under .buildings.
// tree: an array of three {parts} variants. rock, wheatTuft, scaffold, tent, citizenBody, citizenHead,
// citizenArm, banner, rider, windmillSails: {parts}. scaffold and windmillSails are each one merged part.
export function getModels() {
  if (cache) return cache;
  const models = { buildings: {} };
  for (const key of Object.keys(BUILDERS)) {
    const def = finish(BUILDERS[key]());
    def.key = key;
    def.footprint = { w: BUILDINGS[key].w, h: BUILDINGS[key].h };
    models[key] = def;
    models.buildings[key] = def;
  }
  const armGeometry = box(0.08, 0.3, 0.08);
  armGeometry.translate(0, -0.15, 0); // pivot at the shoulder: the arm hangs below the origin
  models.tree = [
    finish({ parts: [part(cyl(0.06, 0.07, 0.5, 5), PALETTE.trunk, 0, 0.25, 0), part(cone(0.42, 0.95, 6), PALETTE.pine, 0, 0.95, 0)] }),
    finish({ parts: [part(cyl(0.06, 0.07, 0.45, 5), PALETTE.trunk, 0, 0.225, 0), part(ball(0.42, 6, 5), PALETTE.canopy, 0, 0.8, 0)] }),
    finish({ parts: [part(cyl(0.05, 0.06, 0.35, 5), PALETTE.trunk, 0, 0.175, 0), part(cone(0.3, 1.1, 5), PALETTE.canopy, 0, 0.9, 0)] }),
  ];
  models.rock = finish({ parts: [part(ball(0.28, 5, 4), PALETTE.stone, 0, 0.2, 0)] });
  models.wheatTuft = finish({ parts: [part(cone(0.1, 0.42, 4), PALETTE.meadow, 0, 0.21, 0)] });
  // Unit scaffold: four corner posts from 0 to 1 and a top plank at 1. Structures scales it to the footprint and progress.
  const scaffoldItems = [[-0.45, -0.45], [0.45, -0.45], [-0.45, 0.45], [0.45, 0.45]].map(([x, z]) => ({ geometry: cyl(0.035, 0.035, 1, 4), offset: [x, 0.5, z] }));
  scaffoldItems.push({ geometry: box(1, 0.05, 1), offset: [0, 1, 0] });
  models.scaffold = finish({ parts: [part(mergeGeometry(scaffoldItems), PALETTE.timber, 0, 0, 0)] });
  models.tent = finish({ parts: [part(cone(0.63, 0.7, 4, QUARTER), LOCAL.sack, 0, 0.35, 0), part(box(0.22, 0.32, 0.03), LOCAL.door, 0, 0.16, 0.3)] });
  models.citizenBody = finish({ parts: [part(box(0.28, 0.34, 0.18), PALETTE.shirts[0], 0, 0.42, 0), part(box(0.22, 0.26, 0.16), LOCAL.legs, 0, 0.13, 0)] });
  models.citizenHead = finish({ parts: [part(box(0.2, 0.2, 0.2), LOCAL.skin, 0, 0.7, 0)] });
  models.citizenArm = finish({ parts: [part(armGeometry, PALETTE.shirts[0], 0, 0, 0)] });
  models.banner = finish({ parts: [part(cyl(0.018, 0.018, 0.7, 4), PALETTE.timber, 0, 0.35, 0), part(box(0.36, 0.22, 0.02), PALETTE.banner, 0.2, 0.6, 0)] });
  models.rider = finish({
    parts: [
      part(box(0.56, 0.3, 0.24), LOCAL.horse, 0, 0.42, 0),
      part(box(0.18, 0.2, 0.16), LOCAL.horse, 0.38, 0.56, 0),
      part(box(0.5, 0.12, 0.18), LOCAL.legs, 0, 0.12, 0),
      part(box(0.2, 0.3, 0.18), LOCAL.leather, -0.05, 0.85, 0),
      part(ball(0.1, 6, 4), LOCAL.skin, -0.05, 1.12, 0),
      part(box(0.22, 0.06, 0.12), PALETTE.bandit, -0.05, 0.99, 0),
    ],
  });
  models.windmillSails = finish({ parts: [part(mergeGeometry([{ geometry: box(1.1, 0.09, 0.03), offset: [0, 0, 0] }, { geometry: box(0.09, 1.1, 0.03), offset: [0, 0, 0] }]), PALETTE.timber, 0, 0, 0)] });
  cache = models;
  return models;
}

// Y rotation for a building rotation 0..3 (rot 1 turns a model a quarter turn). Matches footprintSize in world.js.
export function rotationOf(rot) {
  return -(rot | 0) * Math.PI / 2;
}

// Rotates a local [x, y, z] offset by a building rotation. Returns a new array.
export function rotateOffset(offset, rot) {
  const a = rotationOf(rot);
  const c = Math.cos(a), s = Math.sin(a);
  return [offset[0] * c + offset[2] * s, offset[1], -offset[0] * s + offset[2] * c];
}

// Ground height of tile index i, the same rule as terrain.js (bed clamp for water, mountain lift, bridge deck).
export function groundHeight(state, i) {
  const t = state.map.terrain[i];
  if (state.map.road[i] === 2) return BRIDGE_Y;
  let h = state.map.height[i] * LEVEL;
  if (t === TERRAIN.MOUNTAIN) h += MOUNTAIN_LIFT;
  else if (t === TERRAIN.RIVER || t === TERRAIN.LAKE) h = Math.min(h, BED_Y);
  return h;
}

// Surface height a walker stands on: ground, plus the road lift on road tiles.
export function walkHeight(state, i) {
  return groundHeight(state, i) + (state.map.road[i] === 1 ? ROAD_LIFT : 0);
}

// The state structures last synced. Markers and effects get no state from the renderer, so they read ground heights here.
let activeState = null;
export function setActiveState(state) {
  activeState = state;
}

// Ground height at a world point (the tile under it). 0 before any state has been synced.
export function groundAt(x, z) {
  if (!activeState) return 0;
  const ix = Math.min(activeState.width - 1, Math.max(0, Math.floor(x)));
  const iz = Math.min(activeState.height - 1, Math.max(0, Math.floor(z)));
  return groundHeight(activeState, iz * activeState.width + ix);
}
