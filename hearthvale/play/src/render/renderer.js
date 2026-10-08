// owner: render-world
// Section 9.1: the renderer. Owns the scene and the WebGL renderer, and runs the per-frame call order.
import * as THREE from 'three';
import { getSeasonInfo } from '../sim/queries.js';
import { BUILDINGS } from '../config/buildings.js';
import { createCamera } from './camera.js';
import { pickGround } from './picking.js';
import { createTerrain } from './terrain.js';
import { createEnvironment } from './environment.js';
import { createStructures } from './structures.js';
import { createCitizens } from './citizens.js';
import { createMarkers } from './markers.js';
import { createEffects } from './effects.js';
import { PALETTE } from './palette.js';

const MAX_PIXEL_RATIO = 2;
const EXPOSURE = 1.05;

const _proj = new THREE.Vector3();

function pixelRatio() {
  return Math.min(globalThis.devicePixelRatio || 1, MAX_PIXEL_RATIO);
}

function findBuilding(state, id) {
  for (const b of state.buildings) {
    if (b.id === id) return b;
  }
  return null;
}

// Tiles of a w by h footprint anchored at x, y.
function footprint(x, y, w, h) {
  const out = [];
  for (let dy = 0; dy < h; dy++) {
    for (let dx = 0; dx < w; dx++) out.push({ x: x + dx, y: y + dy });
  }
  return out;
}

// Ghost footprint: the config size at rot 0, swapped when rot is 1 or 3.
function ghostTiles(ghost) {
  const def = BUILDINGS[ghost.type];
  if (!def) return [];
  const swap = ghost.rot === 1 || ghost.rot === 3;
  return footprint(ghost.x, ghost.y, swap ? def.h : def.w, swap ? def.w : def.h);
}

function overlayFor(input, state) {
  let selectedTiles = [];
  if (input.selectedId !== null && input.selectedId !== undefined) {
    const b = findBuilding(state, input.selectedId);
    if (b) selectedTiles = footprint(b.x, b.y, b.w, b.h);
  }
  const ghost = input.ghost || null;
  // Armed building (change R1-15): markers.js takes {state, type} while the build tool is armed, and null otherwise, which
  // hides the dots and keeps their cache. The state is the one this frame draws, so the dots always come from that map.
  const a = input.armed;
  const armed = a && typeof a.type === 'string' ? { state, type: a.type } : null;
  return {
    hover: input.hover || null,
    selectedTiles,
    roadPreview: input.roadPreview || [],
    ghostTiles: ghost ? ghostTiles(ghost) : [],
    ghostOk: ghost ? !!ghost.ok : false,
    armed,
  };
}

export function createRenderer(canvas) {
  const gl = new THREE.WebGLRenderer({ canvas, antialias: true });
  gl.setPixelRatio(pixelRatio());
  gl.toneMapping = THREE.ACESFilmicToneMapping;
  gl.toneMappingExposure = EXPOSURE;
  gl.shadowMap.enabled = true;
  // PCFSoftShadowMap was removed in three 0.186 (it warns and falls back). PCF with a shadow radius gives the soft edge.
  gl.shadowMap.type = THREE.PCFShadowMap;
  gl.setClearColor(PALETTE.horizon, 1);

  let cssW = canvas.clientWidth || globalThis.innerWidth || 1280;
  let cssH = canvas.clientHeight || globalThis.innerHeight || 720;
  gl.setSize(cssW, cssH, false);

  const scene = new THREE.Scene();
  const camera = createCamera(canvas, cssW, cssH);
  const environment = createEnvironment(scene, gl);
  const structures = createStructures(scene);
  const citizens = createCitizens(scene);
  const markers = createMarkers(scene);
  const effects = createEffects(scene);

  let state = null;
  let terrain = null;
  let seen = null;
  let frameMs = 0;

  function setState(s) {
    state = s;
    seen = null;
    if (!terrain) {
      terrain = createTerrain(s);
      scene.add(terrain.group);
    }
  }

  return {
    setState,

    frame(input) {
      const t0 = performance.now();
      const s = input.state;
      if (!s) return;
      if (s !== state) setState(s);
      const dt = input.dt > 0 ? input.dt : 0;
      const time = Number.isFinite(input.time) ? input.time : 0;
      const dayFrac = Number.isFinite(input.dayFrac) ? input.dayFrac : 0;
      const season = Number.isInteger(input.season) ? input.season : getSeasonInfo(s).season;
      const rev = s.rev;
      const events = input.events || [];

      environment.update(s, dt, time, dayFrac);
      camera.update(dt);

      const fresh = seen === null || seen.state !== s;
      if (fresh || rev.map !== seen.map || season !== seen.season) terrain.refresh(s);
      if (fresh || rev.buildings !== seen.buildings) structures.sync(s);
      if (fresh || rev.map !== seen.map || rev.buildings !== seen.buildings || rev.citizens !== seen.citizens) {
        citizens.sync(s);
      }
      seen = { state: s, map: rev.map, buildings: rev.buildings, citizens: rev.citizens, season };

      structures.setGhost(input.ghost || null);
      for (const ev of events) {
        if (ev.type === 'placed') structures.punchGhost();
        else if (ev.type === 'refused') structures.shakeGhost();
      }
      structures.update(dt, events, dayFrac);
      citizens.update(dt, time, s);

      markers.set(input.markers || []);
      markers.update(dt, time);
      markers.overlay(overlayFor(input, s));

      effects.handle(events, s);
      effects.update(dt);

      gl.render(scene, camera.three);
      frameMs = performance.now() - t0;
    },

    resize(cssWidth, cssHeight) {
      if (!(cssWidth > 0) || !(cssHeight > 0)) return;
      cssW = cssWidth;
      cssH = cssHeight;
      gl.setPixelRatio(pixelRatio());
      gl.setSize(cssWidth, cssHeight, false);
      camera.setViewport(cssWidth, cssHeight);
    },

    pickTile(clientX, clientY) {
      if (!state || !terrain) return null;
      const r = canvas.getBoundingClientRect();
      if (!(r.width > 0) || !(r.height > 0)) return null;
      const nx = ((clientX - r.left) / r.width) * 2 - 1;
      const ny = 1 - ((clientY - r.top) / r.height) * 2;
      const hit = pickGround(camera.three, nx, ny, (x, y) => terrain.heightAt(x, y));
      if (!hit || hit.x < 0 || hit.y < 0 || hit.x >= state.width || hit.y >= state.height) return null;
      return hit;
    },

    worldToScreen(x, y) {
      const h = terrain ? terrain.heightAt(x, y) : 0;
      _proj.set(x + 0.5, h, y + 0.5).project(camera.three);
      const sx = (_proj.x * 0.5 + 0.5) * cssW;
      const sy = (0.5 - _proj.y * 0.5) * cssH;
      const visible = _proj.z > -1 && _proj.z < 1 && sx >= 0 && sx <= cssW && sy >= 0 && sy <= cssH;
      return { x: sx, y: sy, visible };
    },

    camera,

    stats() {
      return { drawCalls: gl.info.render.calls, triangles: gl.info.render.triangles, frameMs };
    },

    dispose() {
      environment.dispose();
      structures.dispose();
      markers.dispose();
      effects.dispose();
      if (typeof citizens.dispose === 'function') citizens.dispose();
      if (terrain) {
        scene.remove(terrain.group);
        terrain.group.traverse((o) => {
          if (o.geometry) o.geometry.dispose();
          if (o.material) o.material.dispose();
        });
        terrain = null;
      }
      gl.dispose();
    },
  };
}
