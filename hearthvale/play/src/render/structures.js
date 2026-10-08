// owner: render-structures
// Section 9.4: building meshes (one InstancedMesh per building type and part), construction scaffolds that rise with
// progress (lerped by dayFrac) and bob while builders work, wheat that follows the season and sways when staffed,
// flags that wave, windmill sails on farms, the red "!" on idle buildings, the completion pop and the placement ghost.
// PRESENT holds presentation values from section 9.4; they shape the look only and are not balance numbers.
import * as THREE from 'three';
import { BUILDINGS } from '../config/buildings.js';
import { TERRAIN } from '../sim/state.js';
import { PALETTE } from './palette.js';
import { getModels, rotationOf, rotateOffset, groundHeight, seasonOf, setActiveState } from './models.js';

const PRESENT = {
  capBuilding: 128, capScaffold: 256, capWheat: 1024, capFlag: 128, capSails: 128, capSprites: 32,
  bobAmp: 0.04, scaffoldMin: 0.06, popTime: 0.6, popStart: 0.85, popPeak: 1.1,
  punchTime: 0.25, punchScale: 0.06, shakeTime: 0.3, shakeAmp: 0.08,
  flagSway: 0.22, sailSpeed: 1.2, sailIdle: 0.15, wheatSway: 0.08,
  wheatHeight: [1.0, 1.35, 1.6, 0.6], wheatColour: [PALETTE.grass, PALETTE.meadow, PALETTE.gold, 0x9b8a5a],
  spriteSize: 0.5, spriteBob: 0.06, spriteLift: 0.35, ghostOpacity: 0.45, slabOpacity: 0.5,
};
const AXIS_Y = new THREE.Vector3(0, 1, 0), AXIS_Z = new THREE.Vector3(0, 0, 1);
const UNIT = new THREE.Vector3(1, 1, 1), NO_TURN = new THREE.Quaternion();
const NEEDS_CODE = { forest: TERRAIN.FOREST, stone: TERRAIN.STONE, iron: TERRAIN.IRON };
const TAU = Math.PI * 2;
// Scratch objects, reused so that sync and update allocate nothing per frame.
const _p = new THREE.Vector3(), _s = new THREE.Vector3(), _q = new THREE.Quaternion(), _q2 = new THREE.Quaternion();
const _m = new THREE.Matrix4(), _o = new THREE.Matrix4(), _t = new THREE.Matrix4(), _c = new THREE.Color();
const hash01 = (n) => (Math.imul(n | 0, 2654435761) >>> 0) / 4294967296;
const tr = (o) => _t.makeTranslation(o[0], o[1], o[2]);

// Mean ground height under a footprint: the base a building stands on.
function baseHeight(state, x, y, w, h) {
  let sum = 0, n = 0;
  for (let j = y; j < y + h; j++) {
    for (let i = x; i < x + w; i++) {
      if (i < 0 || j < 0 || i >= state.width || j >= state.height) continue;
      sum += groundHeight(state, j * state.width + i);
      n++;
    }
  }
  return n ? sum / n : 0;
}

// True when a tile of the needed kind with deposit left lies within `radius` of the footprint.
function resourceLeft(state, b, needs) {
  const code = NEEDS_CODE[needs.terrain], r = needs.radius;
  let n = 0;
  for (let y = b.y - r; y < b.y + b.h + r; y++) {
    for (let x = b.x - r; x < b.x + b.w + r; x++) {
      if (x < 0 || y < 0 || x >= state.width || y >= state.height) continue;
      const i = y * state.width + x;
      if (state.map.terrain[i] === code && state.map.deposit[i] > 0) n++;
    }
  }
  return n >= needs.min;
}

// The idle rules of section 7.4, read from state: no road, no workers, missing inputs, no resource left.
function isIdle(state, b) {
  const cfg = BUILDINGS[b.type];
  if (b.priority === 'paused') return false;
  if (!b.connected || (cfg.crew > 0 && b.crew === 0)) return true;
  if (cfg.recipe && Object.keys(cfg.recipe.in).some((r) => state.stock[r] < cfg.recipe.in[r])) return true;
  return !!cfg.needs && cfg.needs.kind === 'terrain' && !resourceLeft(state, b, cfg.needs);
}

// Completion pop: 0.85 to 1.10 over the first half of popTime, then 1.10 to 1.00.
function popScale(t) {
  const u = t / PRESENT.popTime;
  return u < 0.5 ? PRESENT.popStart + (PRESENT.popPeak - PRESENT.popStart) * u * 2 : PRESENT.popPeak + (1 - PRESENT.popPeak) * (u - 0.5) * 2;
}

// White "!" on a red disc, drawn into a 32 by 32 texture (no DOM).
function exclamationTexture() {
  const n = 32, data = new Uint8Array(n * n * 4);
  for (let y = 0; y < n; y++) {
    for (let x = 0; x < n; x++) {
      const dx = x - 15.5, dy = y - 15.5, disc = dx * dx + dy * dy <= 196;
      const mark = disc && ((Math.abs(dx) < 2.6 && y >= 9 && y <= 23) || dx * dx + (y - 5.5) * (y - 5.5) <= 9);
      const c = mark ? [255, 255, 255] : disc ? [0xb8, 0x32, 0x2a] : [0, 0, 0];
      data.set([c[0], c[1], c[2], disc ? 255 : 0], (y * n + x) * 4);
    }
  }
  const tex = new THREE.DataTexture(data, n, n);
  tex.magFilter = THREE.LinearFilter;
  tex.minFilter = THREE.LinearFilter;
  tex.needsUpdate = true;
  return tex;
}

export function createStructures(scene) {
  const models = getModels();
  const group = new THREE.Group();
  group.name = 'structures';
  scene.add(group);

  const material = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.92, metalness: 0, flatShading: true });
  const all = [], dirty = new Set();
  const touch = (m) => dirty.add(m);
  const makeMesh = (geometry, cap) => {
    const m = new THREE.InstancedMesh(geometry, material, cap);
    m.instanceColor = new THREE.InstancedBufferAttribute(new Float32Array(cap * 3), 3);
    Object.assign(m, { count: 0, visible: false, frustumCulled: false, castShadow: true, receiveShadow: true });
    group.add(m);
    all.push(m);
    return m;
  };
  const flush = () => {
    for (const m of dirty) { m.instanceMatrix.needsUpdate = true; m.instanceColor.needsUpdate = true; }
    dirty.clear();
  };

  // One InstancedMesh per building type and part, then the scaffold, flags, sails and wheat.
  const types = {};
  for (const type of Object.keys(models.buildings)) {
    const def = models.buildings[type];
    types[type] = { def, meshes: def.parts.map((p) => makeMesh(p.geometry, PRESENT.capBuilding)), n: 0 };
  }
  const scaffold = makeMesh(models.scaffold.parts[0].geometry, PRESENT.capScaffold), SCAFFOLD_COLOUR = models.scaffold.parts[0].color;
  const [POLE, CLOTH] = models.banner.parts;
  const flagPole = makeMesh(POLE.geometry, PRESENT.capFlag), flagCloth = makeMesh(CLOTH.geometry, PRESENT.capFlag);
  const sails = makeMesh(models.windmillSails.parts[0].geometry, PRESENT.capSails);
  const wheat = makeMesh(models.wheatTuft.parts[0].geometry, PRESENT.capWheat);
  const TUFT = models.wheatTuft.parts[0].offset;

  // Idle markers: pooled sprites, created on demand.
  const spriteMat = new THREE.SpriteMaterial({ map: exclamationTexture(), depthTest: false, depthWrite: false, transparent: true });
  const sprites = [], spriteBaseY = [];
  const spriteAt = (i) => {
    if (!sprites[i]) {
      const s = new THREE.Sprite(spriteMat);
      s.scale.set(PRESENT.spriteSize, PRESENT.spriteSize, 1);
      s.renderOrder = 10;
      group.add(s);
      sprites[i] = s;
    }
    return sprites[i];
  };

  // Placement ghost: a translucent footprint (unrotated) and a translucent building turned by rot.
  const ghostMat = new THREE.MeshStandardMaterial({ color: PALETTE.ghostOk, roughness: 0.9, transparent: true, opacity: PRESENT.ghostOpacity, depthWrite: false, flatShading: true });
  const slabMat = new THREE.MeshBasicMaterial({ color: PALETTE.ghostOk, transparent: true, opacity: PRESENT.slabOpacity, depthWrite: false });
  const ghostRoot = new THREE.Group(), ghostModel = new THREE.Group();
  const ghostSlab = new THREE.Mesh(new THREE.BoxGeometry(1, 0.04, 1), slabMat);
  ghostRoot.add(ghostSlab, ghostModel);
  ghostRoot.visible = false;
  group.add(ghostRoot);

  let last = null, mapRev = -1, time = 0, ghostKey = '', ghostCx = 0, ghostCz = 0, ghostBase = 0, ghostCol = PALETTE.ghostOk;
  let punchT = null, shakeT = null, recs = new Map(), lastProgress = new Map(), pops = new Map();
  let scaffoldRecs = [], flagRecs = [], tuftRecs = [], sailRecs = [];

  // Writes the matrices and colours of one complete building, scaled by s about its base.
  function writeComplete(rec, s) {
    const t = types[rec.type];
    _p.set(rec.cx, rec.base, rec.cz);
    _q.setFromAxisAngle(AXIS_Y, rotationOf(rec.rot));
    _s.set(s, s, s);
    const root = _m.compose(_p, _q, _s);
    t.meshes.forEach((m, i) => {
      const part = t.def.parts[i];
      m.setMatrixAt(rec.k, _o.multiplyMatrices(root, tr(part.offset)));
      m.setColorAt(rec.k, _c.setHex(part.color).multiplyScalar(rec.tint));
      touch(m);
    });
  }

  function writeScaffold(rec, dayFrac) {
    const progress = rec.prev + (rec.now - rec.prev) * dayFrac;
    const bob = rec.builders > 0 ? PRESENT.bobAmp * Math.abs(Math.sin(dayFrac * Math.PI * 4)) : 0;
    _p.set(rec.cx, rec.base + bob, rec.cz);
    _s.set(rec.w, Math.max(PRESENT.scaffoldMin, progress) * rec.height, rec.h);
    scaffold.setMatrixAt(rec.k, _m.compose(_p, NO_TURN, _s));
    touch(scaffold);
  }

  function writeFlag(f, angle) {
    _q.copy(f.turn).multiply(_q2.setFromAxisAngle(AXIS_Y, angle));
    _m.compose(f.at, _q, UNIT);
    flagPole.setMatrixAt(f.k, _o.multiplyMatrices(_m, tr(POLE.offset)));
    flagCloth.setMatrixAt(f.k, _o.multiplyMatrices(_m, tr(CLOTH.offset)));
    touch(flagPole);
    touch(flagCloth);
  }

  function writeSail(s) {
    _q.copy(s.turn).multiply(_q2.setFromAxisAngle(AXIS_Z, s.angle));
    sails.setMatrixAt(s.k, _m.compose(s.at, _q, UNIT));
    touch(sails);
  }

  function writeTuft(tf, sway) {
    _q.setFromAxisAngle(AXIS_Z, sway);
    _p.set(tf.x, tf.base, tf.z);
    _s.set(1, tf.sy, 1);
    wheat.setMatrixAt(tf.k, _o.multiplyMatrices(_m.compose(_p, _q, _s), tr(TUFT)));
    touch(wheat);
  }

  function sync(state) {
    last = state;
    setActiveState(state);
    mapRev = state.rev.map;
    const season = seasonOf(state.day);
    recs = new Map();
    scaffoldRecs = []; flagRecs = []; tuftRecs = []; sailRecs = [];
    const idle = [], nextProgress = new Map();
    for (const t of Object.values(types)) t.n = 0;
    for (const b of state.buildings) {
      const def = models.buildings[b.type];
      if (!def) continue;
      const t = types[b.type];
      const base = baseHeight(state, b.x, b.y, b.w, b.h);
      const cx = b.x + b.w / 2, cz = b.y + b.h / 2;
      nextProgress.set(b.id, b.progress);
      if (b.stage === 'building') {
        if (scaffoldRecs.length < PRESENT.capScaffold) {
          const rec = { k: scaffoldRecs.length, cx, cz, base, w: b.w, h: b.h, height: def.height, prev: lastProgress.get(b.id) || 0, now: b.progress, builders: b.builders };
          scaffoldRecs.push(rec);
          scaffold.setColorAt(rec.k, _c.setHex(SCAFFOLD_COLOUR));
          writeScaffold(rec, 0);
        }
        continue;
      }
      if (t.n >= PRESENT.capBuilding) continue;
      const rec = { id: b.id, type: b.type, k: t.n++, cx, cz, base, rot: b.rot, tint: 0.94 + 0.12 * hash01(b.id) };
      recs.set(b.id, rec);
      writeComplete(rec, 1);
      if (def.flag && flagRecs.length < PRESENT.capFlag) {
        const a = rotateOffset(def.flag, b.rot);
        const f = { k: flagRecs.length, at: new THREE.Vector3(cx + a[0], base + a[1], cz + a[2]), turn: new THREE.Quaternion().setFromAxisAngle(AXIS_Y, rotationOf(b.rot)), phase: hash01(b.id) * TAU };
        flagRecs.push(f);
        flagPole.setColorAt(f.k, _c.setHex(POLE.color));
        flagCloth.setColorAt(f.k, _c.setHex(CLOTH.color));
        writeFlag(f, 0);
      }
      if (b.type === 'farm') {
        const staffed = b.crew > 0, phase = hash01(b.id) * TAU;
        for (const sx of [-1, 1]) {
          for (const sz of [-1, 1]) {
            if (tuftRecs.length >= PRESENT.capWheat) break;
            const tf = { k: tuftRecs.length, x: cx + (sx * b.w) / 4, z: cz + (sz * b.h) / 4, base, sy: PRESENT.wheatHeight[season], staffed, phase };
            tuftRecs.push(tf);
            wheat.setColorAt(tf.k, _c.setHex(PRESENT.wheatColour[season]));
            writeTuft(tf, 0);
          }
        }
        if (sailRecs.length < PRESENT.capSails) {
          const h = rotateOffset(models.farm.hub, b.rot);
          const s = { k: sailRecs.length, at: new THREE.Vector3(cx + h[0], base + h[1], cz + h[2]), turn: new THREE.Quaternion().setFromAxisAngle(AXIS_Y, rotationOf(b.rot)), angle: phase, staffed };
          sailRecs.push(s);
          sails.setColorAt(s.k, _c.setHex(PALETTE.timber));
          writeSail(s);
        }
      }
      if (idle.length < PRESENT.capSprites && isIdle(state, b)) idle.push({ x: cx, y: base + def.height + PRESENT.spriteLift, z: cz });
    }
    for (const t of Object.values(types)) for (const m of t.meshes) { m.count = t.n; m.visible = t.n > 0; touch(m); }
    [[scaffold, scaffoldRecs.length], [flagPole, flagRecs.length], [flagCloth, flagRecs.length], [sails, sailRecs.length], [wheat, tuftRecs.length]].forEach(([m, n]) => { m.count = n; m.visible = n > 0; touch(m); });
    idle.forEach((p, i) => { const s = spriteAt(i); s.position.set(p.x, p.y, p.z); spriteBaseY[i] = p.y; s.visible = true; });
    for (let i = idle.length; i < sprites.length; i++) sprites[i].visible = false;
    lastProgress = nextProgress;
    flush();
  }

  function setGhost(g) {
    if (!g || !models.buildings[g.type] || !last) { ghostRoot.visible = false; ghostKey = ''; return; }
    const r = (g.rot | 0) & 3, cfg = BUILDINGS[g.type];
    const fw = r & 1 ? cfg.h : cfg.w, fh = r & 1 ? cfg.w : cfg.h;
    const key = g.type + ':' + r;
    if (key !== ghostKey) {
      ghostKey = key;
      ghostModel.clear();
      for (const p of models.buildings[g.type].parts) {
        const m = new THREE.Mesh(p.geometry, ghostMat);
        m.position.set(p.offset[0], p.offset[1], p.offset[2]);
        ghostModel.add(m);
      }
      ghostModel.rotation.y = rotationOf(r);
    }
    ghostCx = g.x + fw / 2;
    ghostCz = g.y + fh / 2;
    ghostBase = baseHeight(last, g.x, g.y, fw, fh);
    ghostSlab.scale.set(fw, 1, fh);
    ghostSlab.position.set(0, 0.02, 0);
    ghostCol = g.ok ? PALETTE.ghostOk : PALETTE.ghostBad;
    ghostRoot.position.set(ghostCx, ghostBase, ghostCz);
    ghostRoot.visible = true;
  }

  function update(dt, events, dayFrac) {
    time += dt;
    if (last && last.rev.map !== mapRev) sync(last); // placing or demolishing bumps rev.map, not rev.buildings (4.9)
    for (const ev of events) {
      if (ev.type !== 'buildingComplete') continue;
      const id = ev.id || (last && ev.x !== undefined ? last.map.building[ev.y * last.width + ev.x] : 0);
      if (id) pops.set(id, 0);
    }
    for (const [id, t0] of pops) {
      const t = t0 + dt, rec = recs.get(id);
      if (!rec || t >= PRESENT.popTime) { pops.delete(id); if (rec) writeComplete(rec, 1); }
      else { pops.set(id, t); writeComplete(rec, popScale(t)); }
    }
    for (const rec of scaffoldRecs) writeScaffold(rec, dayFrac);
    for (const f of flagRecs) writeFlag(f, Math.sin(time * 2.6 + f.phase) * PRESENT.flagSway);
    for (const s of sailRecs) { s.angle += dt * (s.staffed ? PRESENT.sailSpeed : PRESENT.sailIdle); writeSail(s); }
    for (const tf of tuftRecs) if (tf.staffed) writeTuft(tf, Math.sin(time * 2.2 + tf.phase) * PRESENT.wheatSway);
    if (punchT !== null) { punchT += dt; if (punchT >= PRESENT.punchTime) punchT = null; }
    if (shakeT !== null) { shakeT += dt; if (shakeT >= PRESENT.shakeTime) shakeT = null; }
    if (ghostRoot.visible) {
      const scale = punchT === null ? 1 : 1 + PRESENT.punchScale * Math.sin((punchT / PRESENT.punchTime) * Math.PI);
      const shake = shakeT === null ? 0 : PRESENT.shakeAmp * Math.sin(shakeT * 60) * (1 - shakeT / PRESENT.shakeTime);
      const col = shakeT === null ? ghostCol : PALETTE.ghostBad;
      ghostRoot.position.set(ghostCx + shake, ghostBase, ghostCz);
      ghostRoot.scale.setScalar(scale);
      ghostMat.color.setHex(col);
      slabMat.color.setHex(col);
    }
    sprites.forEach((s, i) => { if (s.visible) s.position.y = spriteBaseY[i] + PRESENT.spriteBob * Math.sin(time * 4 + i); });
    flush();
  }

  return {
    sync,
    setGhost,
    update,
    punchGhost() { punchT = 0; },
    shakeGhost() { shakeT = 0; },
    buildingAt(state, x, y) {
      if (!state || x < 0 || y < 0 || x >= state.width || y >= state.height) return null;
      const id = state.map.building[y * state.width + x];
      return id > 0 ? id : null;
    },
    dispose() {
      scene.remove(group);
      for (const m of all) m.dispose();
      for (const m of [material, ghostMat, slabMat, spriteMat]) m.dispose();
      spriteMat.map.dispose();
    },
  };
}
