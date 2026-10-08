// owner: render-world
// Section 9.3: terrain chunks with vertex colours, roads and bridges, animated water, and instanced trees and rocks.
import * as THREE from 'three';
import { TERRAIN } from '../sim/state.js';
import { getSeasonInfo } from '../sim/queries.js';
import { getModels } from './models.js';
import { PALETTE, SEASON_TINT } from './palette.js';

const CHUNK = 16, LEVEL = 2.2 / 255, WATER_Y = 0.32, BED_Y = 0.2, MOUNTAIN_LIFT = 0.35, ROAD_LIFT = 0.03;
const BRIDGE_Y = WATER_Y + 0.05, FOG_LEVEL = 0.45, FLAT = 0.06, WINTER = 3, CAP_TREE = 2048, CAP_ROCK = 1024;
const SOLVE_SWEEPS = 240, SOLVE_TOL = 1e-4, TAU = Math.PI * 2;
const col = (hex) => new THREE.Color(hex);
const C = {
  grass: col(PALETTE.grass), meadow: col(PALETTE.meadow), flower: col(PALETTE.meadowFlower), forest: col(PALETTE.forestFloor),
  stone: col(PALETTE.stone), iron: col(PALETTE.iron), rust: col(PALETTE.rust), mountain: col(PALETTE.mountain),
  snow: col(PALETTE.snow), river: col(PALETTE.river), lake: col(PALETTE.lake), road: col(PALETTE.road),
  bridge: col(PALETTE.bridge), canopy: col(PALETTE.canopy), canopyAutumn: col(PALETTE.canopyAutumn), pine: col(PALETTE.pine),
};
const TINT_GRASS = SEASON_TINT.map((t) => col(t.grass));
const TINT_CANOPY = SEASON_TINT.map((t) => col(t.canopy));
const WHITE = col(0xffffff);
const SHADE = col(0xffffff).multiplyScalar(FOG_LEVEL);
const LAND = new Set([TERRAIN.GRASS, TERRAIN.MEADOW, TERRAIN.FOREST, TERRAIN.HILL, TERRAIN.STONE, TERRAIN.IRON]);
const GREEN = new Set([TERRAIN.GRASS, TERRAIN.MEADOW, TERRAIN.FOREST, TERRAIN.HILL]);

// Integer hash in [0, 1), for deterministic per-tile variation.
function hash01(x, y, k) {
  let h = Math.imul(x, 374761393) ^ Math.imul(y, 668265263) ^ Math.imul(k, 1442695041);
  h = Math.imul(h ^ (h >>> 13), 1274126177);
  return ((h ^ (h >>> 16)) >>> 0) / 4294967296;
}

// Corner heights (CW = W + 1 per row) whose 2x2 average equals each tile's own height, so the surface passes through
// every tile centre and heightAt matches the base height formula. Cyclic projection from a nearest-tile start.
function solveCorners(W, H, tileH) {
  const CW = W + 1;
  const c = new Float64Array(CW * (H + 1));
  for (let y = 0; y <= H; y++) for (let x = 0; x <= W; x++) c[y * CW + x] = tileH[Math.min(y, H - 1) * W + Math.min(x, W - 1)];
  for (let s = 0; s < SOLVE_SWEEPS; s++) {
    let worst = 0;
    for (let y = 0; y < H; y++) {
      for (let x = 0; x < W; x++) {
        const a = y * CW + x, b = a + CW, t = tileH[y * W + x];
        const r = 4 * t - (c[a] + c[a + 1] + c[b] + c[b + 1]);
        c[a] += r / 4; c[a + 1] += r / 4; c[b] += r / 4; c[b + 1] += r / 4;
        worst = Math.max(worst, Math.abs(r));
      }
    }
    if (worst < SOLVE_TOL) break;
  }
  return c;
}

// Positions of one tile quad (x..x+1, y..y+1) at heights h00, h10, h01, h11, written at float offset p.
const quad = (pos, p, x, y, h00, h10, h01, h11) => pos.set([x, h00, y, x + 1, h10, y, x, h01, y + 1, x + 1, h11, y + 1], p);
// Two upward-facing triangles for the quad whose first vertex is v, written at index offset q.
const quadIndex = (idx, q, v) => idx.set([v, v + 2, v + 1, v + 1, v + 2, v + 3], q);
// One colour on the four vertices of a tile (or water quad) at float offset base.
function put(arr, base, c) {
  for (let k = 0; k < 4; k++) arr.set([c.r, c.g, c.b], base + k * 3);
}
const geometryOf = (pos, colour, idx) => new THREE.BufferGeometry()
  .setAttribute('position', new THREE.BufferAttribute(pos, 3))
  .setAttribute('color', new THREE.BufferAttribute(colour, 3))
  .setIndex(new THREE.BufferAttribute(idx, 1));

// Model shapes allowed by section 9.4: a parts list or {parts}. Each part is {geometry, color, offset}.
const partsOf = (v) => (Array.isArray(v) ? v : ((v && v.parts) || [])).filter((p) => p && p.geometry);
// Trees: a list of variants, each a parts list. A single parts list is accepted too.
function treeVariants(v) {
  const out = (Array.isArray(v) ? v : ((v && v.variants) || [])).map(partsOf).filter((p) => p.length > 0);
  return out.length > 0 || partsOf(v).length === 0 ? out : [partsOf(v)];
}

export function createTerrain(state) {
  const group = new THREE.Group();
  const statics = new THREE.Group();   // everything rebuilt when the state object changes
  group.add(statics);
  const groundMat = new THREE.MeshStandardMaterial({ vertexColors: true, flatShading: true, roughness: 0.95 });
  const roadMat = new THREE.MeshStandardMaterial({
    vertexColors: true, flatShading: true, roughness: 0.9, polygonOffset: true, polygonOffsetFactor: -1, polygonOffsetUnits: -1,
  });
  const waterMat = new THREE.MeshStandardMaterial({ vertexColors: true, flatShading: true, roughness: 0.25, metalness: 0.05 });
  const waterTime = { value: 0 };
  waterMat.onBeforeCompile = (sh) => {
    sh.uniforms.uTime = waterTime;
    sh.vertexShader = sh.vertexShader.replace('#include <common>', '#include <common>\nuniform float uTime;')
      .replace('#include <begin_vertex>', 'vec3 transformed = vec3( position );\n'
        + 'transformed.y += 0.014 * sin( uTime * 1.3 + position.x * 0.9 + position.z * 0.7 )'
        + ' + 0.008 * sin( uTime * 2.1 - position.x * 1.7 + position.z * 1.1 );');
  };
  const dummy = new THREE.Object3D();
  const scratch = new THREE.Color();

  // Per-build state, replaced whenever the state object changes.
  let built = null, map = null, W = 0, H = 0, CW = 0;
  let tileH = null, corners = null, mtBase = 0, mtTop = 1;
  let chunks = [], waterTiles = new Int32Array(0), waterColour = null, waterAttr = null, roadGeo = null;
  let trees = [], rockSets = { stone: null, iron: null }, maxDep = { forest: 1, stone: 1, iron: 1 };
  let foliage = [], propMats = [];
  let paintedRev = -1, paintedSeason = -1;

  function disposeStatics() {
    statics.traverse((o) => { if (o.geometry) o.geometry.dispose(); });
    propMats.forEach((m) => m.dispose());
    propMats = [];
    foliage = [];
    statics.clear();
  }

  // Colour of tile i for a season, in the shared scratch colour. Snow settles on flat land in winter.
  function tileColour(i, season) {
    const t = map.terrain[i];
    const x = i % W, y = (i - x) / W;
    const c = scratch;
    switch (t) {
      case TERRAIN.GRASS: c.copy(C.grass); break;
      case TERRAIN.MEADOW: c.copy(C.meadow); if (hash01(x, y, 7) < 0.16) c.lerp(C.flower, 0.6); break;
      case TERRAIN.FOREST: c.copy(C.forest); break;
      case TERRAIN.HILL: c.copy(C.grass).lerp(C.stone, 0.45); break;
      case TERRAIN.STONE: c.copy(C.grass).lerp(C.stone, 0.7); break;
      case TERRAIN.IRON: c.copy(C.stone).lerp(C.iron, 0.6).lerp(C.rust, 0.2); break;
      case TERRAIN.MOUNTAIN:
        c.copy(C.mountain).lerp(C.snow, Math.min(1, Math.max(0, ((tileH[i] - mtBase) / Math.max(0.001, mtTop - mtBase)) * 1.6 - 0.6)));
        break;
      case TERRAIN.RIVER: c.copy(C.river); break;
      default: c.copy(C.lake); break;
    }
    if (GREEN.has(t)) c.multiply(TINT_GRASS[season]);
    if (LAND.has(t) && season === WINTER) {
      const a = y * CW + x, b = a + CW, cs = [corners[a], corners[a + 1], corners[b], corners[b + 1]];
      c.lerp(C.snow, Math.max(...cs) - Math.min(...cs) < FLAT ? 0.9 : 0.3);
    }
    c.multiplyScalar(0.96 + 0.08 * hash01(x, y, 9));
    if (!map.explored[i]) c.multiplyScalar(FOG_LEVEL);
    return c;
  }

  function paint(season) {
    for (const ch of chunks) {
      for (let y = ch.y0; y < ch.y1; y++) {
        for (let x = ch.x0; x < ch.x1; x++) put(ch.colour, ((y - ch.y0) * ch.tw + (x - ch.x0)) * 12, tileColour(y * W + x, season));
      }
      ch.attr.needsUpdate = true;
    }
    waterTiles.forEach((i, s) => put(waterColour, s * 12, tileColour(i, season)));
    waterAttr.needsUpdate = true;
  }

  // Ground chunks of CHUNK by CHUNK tiles. Four vertices per tile, so each tile keeps its own colour.
  function buildGround() {
    chunks = [];
    for (let y0 = 0; y0 < H; y0 += CHUNK) {
      for (let x0 = 0; x0 < W; x0 += CHUNK) {
        const x1 = Math.min(W, x0 + CHUNK), y1 = Math.min(H, y0 + CHUNK), tw = x1 - x0, nt = tw * (y1 - y0);
        const pos = new Float32Array(nt * 12), colour = new Float32Array(nt * 12), idx = new Uint16Array(nt * 6);
        let k = 0;
        for (let y = y0; y < y1; y++) {
          for (let x = x0; x < x1; x++, k++) {
            const a = y * CW + x, b = a + CW;
            quad(pos, k * 12, x, y, corners[a], corners[a + 1], corners[b], corners[b + 1]);
            quadIndex(idx, k * 6, 4 * k);
          }
        }
        const geo = geometryOf(pos, colour, idx);
        geo.computeVertexNormals();
        const mesh = new THREE.Mesh(geo, groundMat);
        mesh.receiveShadow = true;
        statics.add(mesh);
        chunks.push({ x0, y0, x1, y1, tw, attr: geo.attributes.color, colour });
      }
    }
  }

  // Flat quads at WATER_Y over every river and lake tile. The vertex shader waves them over time.
  function buildWater() {
    waterTiles = Int32Array.from(Array.from({ length: W * H }, (_, i) => i)
      .filter((i) => map.terrain[i] === TERRAIN.RIVER || map.terrain[i] === TERRAIN.LAKE));
    const nw = waterTiles.length;
    const pos = new Float32Array(nw * 12), idx = new Uint32Array(nw * 6);
    waterColour = new Float32Array(nw * 12);
    waterTiles.forEach((i, s) => {
      const x = i % W, y = (i - x) / W;
      quad(pos, s * 12, x, y, WATER_Y, WATER_Y, WATER_Y, WATER_Y);
      quadIndex(idx, s * 6, 4 * s);
    });
    const geo = geometryOf(pos, waterColour, idx);
    waterAttr = geo.attributes.color;
    const mesh = new THREE.Mesh(geo, waterMat);
    mesh.receiveShadow = true;
    mesh.frustumCulled = false;
    mesh.onBeforeRender = () => { waterTime.value = performance.now() / 1000; };
    statics.add(mesh);
  }

  // Roads are dark quads ROAD_LIFT above the ground; bridges are deck quads above the water.
  function fillRoads() {
    const pos = roadGeo.attributes.position.array, colour = roadGeo.attributes.color.array, idx = roadGeo.index.array;
    let k = 0;
    for (let i = 0; i < W * H; i++) {
      const r = map.road[i];
      if (!r) continue;
      const x = i % W, y = (i - x) / W, a = y * CW + x, b = a + CW, p = k * 12;
      if (r === 2) quad(pos, p, x, y, BRIDGE_Y, BRIDGE_Y, BRIDGE_Y, BRIDGE_Y);
      else quad(pos, p, x, y, corners[a] + ROAD_LIFT, corners[a + 1] + ROAD_LIFT, corners[b] + ROAD_LIFT, corners[b + 1] + ROAD_LIFT);
      put(colour, p, r === 2 ? C.bridge : C.road);
      quadIndex(idx, k * 6, 4 * k);
      k++;
    }
    roadGeo.attributes.position.needsUpdate = true;
    roadGeo.attributes.color.needsUpdate = true;
    roadGeo.index.needsUpdate = true;
    roadGeo.setDrawRange(0, k * 6);
  }

  // An instanced set: one InstancedMesh per model part, all sharing one transform and colour per instance.
  function instanceSet(parts, matOf, cap, parent) {
    const set = { cap, count: 0, meshes: parts.map((part, j) => {
      const o = part.offset || [0, 0, 0];
      const m = new THREE.InstancedMesh(part.geometry.clone().translate(o[0], o[1], o[2]), matOf(part, j), cap);
      m.castShadow = true; m.receiveShadow = true; m.frustumCulled = false; m.count = 0;
      parent.add(m);
      return m;
    }) };
    return set;
  }

  // Writes one instance into a set. Returns false when the set is full.
  function putInstance(set, x, y, h, jx, jz, sc, yaw, shade) {
    if (set.count >= set.cap) return false;
    dummy.position.set(x + 0.5 + jx, h, y + 0.5 + jz);
    dummy.rotation.set(0, yaw, 0);
    dummy.scale.setScalar(sc);
    dummy.updateMatrix();
    for (const m of set.meshes) {
      m.setMatrixAt(set.count, dummy.matrix);
      m.setColorAt(set.count, shade);
    }
    set.count++;
    return true;
  }

  // Trees and rocks are created once per build and filled here. Forests hold one to three trees by remaining timber.
  // Stone and iron hold two rocks per tile that shrink as they are quarried. Tiles under roads or buildings get none.
  function buildProps() {
    const models = getModels();
    const props = new THREE.Group();
    statics.add(props);
    const material = (colour, rough) => {
      const m = new THREE.MeshStandardMaterial({ color: colour, flatShading: true, roughness: rough });
      propMats.push(m);
      return m;
    };
    trees = treeVariants(models.tree).map((parts) => instanceSet(parts, (part) => {
      const pc = new THREE.Color(part.color !== undefined ? part.color : PALETTE.canopy);
      const isFoliage = pc.g >= pc.r;
      const mat = material(isFoliage ? C.canopy : pc, 0.9);
      if (isFoliage) foliage.push(mat);
      return mat;
    }, CAP_TREE, props));
    const rockParts = partsOf(models.rock);
    const stoneMat = material(C.stone, 0.95), ironMat = material(C.iron.clone().lerp(C.rust, 0.5), 0.95);
    rockSets = {
      stone: instanceSet(rockParts, () => stoneMat, CAP_ROCK, props),
      iron: instanceSet(rockParts, () => ironMat, CAP_ROCK, props),
    };
  }

  function fillProps() {
    for (const set of [...trees, rockSets.stone, rockSets.iron]) set.count = 0;
    for (let i = 0; i < W * H; i++) {
      const t = map.terrain[i], d = map.deposit[i];
      if (map.road[i] || map.building[i] || d <= 0) continue;
      const x = i % W, y = (i - x) / W, shade = map.explored[i] ? WHITE : SHADE;
      if (t === TERRAIN.FOREST && trees.length > 0) {
        const ratio = Math.min(1, d / maxDep.forest), k = ratio > 0.66 ? 3 : (ratio > 0.33 ? 2 : 1);
        for (let j = 0; j < k; j++) {
          const h1 = hash01(x, y, 2 * j + 1), h2 = hash01(x, y, 2 * j + 2), h3 = hash01(x, y, 40 + j);
          putInstance(trees[Math.floor(h3 * trees.length)], x, y, tileH[i], (h1 - 0.5) * 0.7, (h2 - 0.5) * 0.7,
            0.85 + 0.35 * h1, h3 * TAU, shade);
        }
      } else if (t === TERRAIN.STONE || t === TERRAIN.IRON) {
        const kind = t === TERRAIN.STONE ? 'stone' : 'iron', frac = Math.min(1, d / maxDep[kind]);
        for (let j = 0; j < 2; j++) {
          const h1 = hash01(x, y, 60 + 3 * j), h2 = hash01(x, y, 61 + 3 * j), h3 = hash01(x, y, 62 + 3 * j);
          putInstance(rockSets[kind], x, y, tileH[i] + 0.02, (h2 - 0.5) * 0.6, (h3 - 0.5) * 0.6,
            (0.35 + 0.3 * frac) * (0.8 + 0.4 * h1), h1 * TAU, shade);
        }
      }
    }
    for (const set of [...trees, rockSets.stone, rockSets.iron]) {
      for (const m of set.meshes) {
        m.count = set.count;
        m.instanceMatrix.needsUpdate = true;
        if (m.instanceColor) m.instanceColor.needsUpdate = true;
      }
    }
  }

  function buildStatic(s) {
    disposeStatics();
    map = s.map;
    W = s.width;
    H = s.height;
    CW = W + 1;
    const n = W * H;
    tileH = new Float32Array(n);
    maxDep = { forest: 0, stone: 0, iron: 0 };
    let lo = Infinity, hi = -Infinity;
    for (let i = 0; i < n; i++) {
      const t = map.terrain[i], d = map.deposit[i];
      let h = map.height[i] * LEVEL;
      if (t === TERRAIN.MOUNTAIN) {
        h += MOUNTAIN_LIFT;
        lo = Math.min(lo, h);
        hi = Math.max(hi, h);
      } else if (t === TERRAIN.RIVER || t === TERRAIN.LAKE) {
        h = Math.min(h, BED_Y);
      }
      tileH[i] = h;
      if (t === TERRAIN.FOREST) maxDep.forest = Math.max(maxDep.forest, d);
      else if (t === TERRAIN.STONE) maxDep.stone = Math.max(maxDep.stone, d);
      else if (t === TERRAIN.IRON) maxDep.iron = Math.max(maxDep.iron, d);
    }
    maxDep = { forest: maxDep.forest || 1, stone: maxDep.stone || 1, iron: maxDep.iron || 1 };
    mtBase = lo < hi ? lo : 0;
    mtTop = lo < hi ? hi : 1;
    corners = solveCorners(W, H, tileH);
    buildGround();
    buildWater();
    const roadN = n;
    roadGeo = geometryOf(new Float32Array(roadN * 12), new Float32Array(roadN * 12), new Uint32Array(roadN * 6));
    const roadMesh = new THREE.Mesh(roadGeo, roadMat);
    roadMesh.receiveShadow = true;
    roadMesh.frustumCulled = false;
    statics.add(roadMesh);
    buildProps();
    built = s;
    paintedRev = -1;
    paintedSeason = -1;
  }

  // A new state rebuilds the static meshes. A map revision repaints and refills. A season change repaints the ground
  // and recolours the foliage: green in spring, deeper in summer, orange-gold in autumn, pine-dark in winter.
  function refresh(s) {
    if (!s || !s.map || !(s.width > 0) || !(s.height > 0)) return;
    const season = getSeasonInfo(s).season;
    if (s !== built) buildStatic(s);
    const rev = s.rev ? s.rev.map : 0;
    if (rev !== paintedRev) {
      paint(season);
      fillRoads();
      fillProps();
    } else if (season !== paintedSeason) {
      paint(season);
    }
    if (season !== paintedSeason) {
      const base = season === 2 ? C.canopyAutumn : (season === WINTER ? C.pine : C.canopy);
      for (const m of foliage) m.color.copy(base).multiply(TINT_CANOPY[season]);
    }
    paintedRev = rev;
    paintedSeason = season;
  }

  function heightAt(x, y) {
    if (!tileH) return 0;
    return tileH[Math.min(H - 1, Math.max(0, Math.floor(y))) * W + Math.min(W - 1, Math.max(0, Math.floor(x)))];
  }

  refresh(state);
  return { group, refresh, heightAt };
}
