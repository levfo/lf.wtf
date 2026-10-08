// owner: render-structures
// Section 9.4: villagers as instanced parts (torso, legs, head and two arms). Each citizen with a home and a job walks
// the road route between the two doors (getRoadRoute); idle citizens wander near the Town Hall, militia stand at the
// Barracks (or the Hall), and homeless people sleep in a tent camp north of the Hall. update allocates nothing.
// PRESENT holds presentation values from section 9.4; they are not balance numbers.
import * as THREE from 'three';
import { PALETTE } from './palette.js';
import { getCitizenViews, getRoadRoute } from '../sim/queries.js';
import { getModels, groundHeight, walkHeight } from './models.js';

const PRESENT = {
  speed: 1.4, bobHz: 4, bobAmp: 0.03, swing: 0.5, armPivot: 0.18, armY: 0.55,
  childScale: 0.6, idleRadius: 0.3, wanderRate: 0.35, ringMin: 2.2, ringSpan: 1.2, militiaRing: 1.4,
  tentRadius: 2.6, tentStep: 0.42, tentCap: 64,
};
const TAU = Math.PI * 2;
const WALK = 0, IDLE = 1, MILITIA = 2;
const AXIS_X = new THREE.Vector3(1, 0, 0), AXIS_Y = new THREE.Vector3(0, 1, 0);
const IDENTITY = new THREE.Quaternion();
const _root = new THREE.Vector3(), _p = new THREE.Vector3(), _v = new THREE.Vector3(), _sc = new THREE.Vector3();
const _c = new THREE.Color(), _q = new THREE.Quaternion(), _qh = new THREE.Quaternion(), _qa = new THREE.Quaternion();
const _m = new THREE.Matrix4();
const ARM_L = [0, 0, 0], ARM_R = [0, 0, 0]; // arm pivots, set from PRESENT once below
ARM_L[0] = PRESENT.armPivot; ARM_L[1] = PRESENT.armY; ARM_R[0] = -PRESENT.armPivot; ARM_R[1] = PRESENT.armY;
const hash01 = (n) => (Math.imul(n | 0, 2654435761) >>> 0) / 4294967296;

// Writes one part's matrix: the root position and heading, the part's offset scaled and turned, and an optional swing.
function put(mesh, k, root, qh, s, o, qLocal) {
  _v.set(o[0] * s, o[1] * s, o[2] * s).applyQuaternion(qh);
  _p.copy(root).add(_v);
  _q.copy(qh);
  if (qLocal) _q.multiply(qLocal);
  _sc.set(s, s, s);
  mesh.setMatrixAt(k, _m.compose(_p, _q, _sc));
}

// Tile index of a world point, clamped to the map.
function tileOf(state, x, z) {
  const ix = Math.min(state.width - 1, Math.max(0, Math.floor(x)));
  const iz = Math.min(state.height - 1, Math.max(0, Math.floor(z)));
  return iz * state.width + ix;
}

// Door of a building: the first road tile beside its footprint, preferring a connected one. South edge first.
function findDoor(state, b) {
  if (!b) return -1;
  const ring = [];
  for (let x = b.x; x < b.x + b.w; x++) ring.push([x, b.y + b.h], [x, b.y - 1]);
  for (let y = b.y; y < b.y + b.h; y++) ring.push([b.x + b.w, y], [b.x - 1, y]);
  let fallback = -1;
  for (const [x, y] of ring) {
    if (x < 0 || y < 0 || x >= state.width || y >= state.height) continue;
    const i = y * state.width + x;
    if (state.map.road[i] === 0) continue;
    if (state.net && state.net.connected[i]) return i;
    if (fallback < 0) fallback = i;
  }
  return fallback;
}

export function createCitizens(scene, capacity = 512) {
  const models = getModels();
  const group = new THREE.Group();
  group.name = 'citizens';
  scene.add(group);
  const material = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.9, metalness: 0, flatShading: true });
  const meshes = [];
  const makeMesh = (geometry, cap) => {
    const m = new THREE.InstancedMesh(geometry, material, cap);
    m.instanceColor = new THREE.InstancedBufferAttribute(new Float32Array(cap * 3), 3);
    Object.assign(m, { count: 0, visible: false, frustumCulled: false, castShadow: true });
    group.add(m);
    meshes.push(m);
    return m;
  };
  const [TORSO, LEGS_PART] = models.citizenBody.parts;
  const torso = makeMesh(TORSO.geometry, capacity), legs = makeMesh(LEGS_PART.geometry, capacity);
  const head = makeMesh(models.citizenHead.parts[0].geometry, capacity);
  const arms = makeMesh(models.citizenArm.parts[0].geometry, capacity * 2);
  const tentCloth = makeMesh(models.tent.parts[0].geometry, PRESENT.tentCap);
  const tentDoor = makeMesh(models.tent.parts[1].geometry, PRESENT.tentCap);
  const SKIN = models.citizenHead.parts[0].color, LEGS = LEGS_PART.color;

  let list = [], hallX = 0, hallZ = 0;

  function sync(state) {
    const views = getCitizenViews(state);
    const byId = new Map(state.buildings.map((b) => [b.id, b]));
    const doors = new Map();
    const doorOf = (id) => {
      if (!doors.has(id)) doors.set(id, findDoor(state, byId.get(id)));
      return doors.get(id);
    };
    const hall = state.buildings.find((b) => b.type === 'townHall') || null;
    const hallDoor = hall ? doorOf(hall.id) : -1;
    hallX = hall ? hall.x + hall.w / 2 : 0;
    hallZ = hall ? hall.y + hall.h / 2 : 0;
    const barracks = state.buildings.filter((b) => b.type === 'barracks' && b.stage === 'complete');
    const routes = new Map();
    list = [];
    let homeless = 0, militiaNo = 0;
    for (const v of views) {
      if (list.length >= capacity) break;
      const c = {
        scale: v.cohort === 'child' ? PRESENT.childScale : 1, phase: hash01(v.id) * TAU,
        shirt: v.militia ? PALETTE.iron : PALETTE.shirts[v.id % PALETTE.shirts.length],
        mode: IDLE, route: null, ax: 0, az: 0, ay: 0, face: 0,
      };
      if (v.homeId === 0) homeless++;
      if (v.militia) {
        c.mode = MILITIA;
        const b = barracks.length ? barracks[militiaNo % barracks.length] : null;
        const cx = b ? b.x + b.w / 2 : hallX, cz = b ? b.y + b.h / 2 : hallZ, a = militiaNo * 0.9;
        c.ax = cx + PRESENT.militiaRing * Math.cos(a);
        c.az = cz + PRESENT.militiaRing * Math.sin(a);
        militiaNo++;
      } else {
        const home = v.homeId ? doorOf(v.homeId) : hallDoor;
        const work = v.workId ? doorOf(v.workId) : -1;
        if (home >= 0 && work >= 0) {
          const key = home + ':' + work;
          if (!routes.has(key)) {
            const path = getRoadRoute(state, home, work);
            routes.set(key, path && path.length >= 2 ? Int32Array.from(path) : null);
          }
          const r = routes.get(key);
          if (r) { c.mode = WALK; c.route = r; }
        }
        if (c.mode === IDLE) {
          const t = hash01(v.id * 3 + 1) * TAU, r = PRESENT.ringMin + hash01(v.id * 7 + 2) * PRESENT.ringSpan;
          c.ax = hallX + r * Math.cos(t);
          c.az = hallZ + r * Math.sin(t);
        }
      }
      if (c.mode !== WALK) {
        c.ay = groundHeight(state, tileOf(state, c.ax, c.az));
        c.face = Math.atan2(hallX - c.ax, hallZ - c.az);
      }
      list.push(c);
    }
    list.forEach((c, i) => {
      torso.setColorAt(i, _c.setHex(c.shirt));
      legs.setColorAt(i, _c.setHex(LEGS));
      head.setColorAt(i, _c.setHex(SKIN));
      arms.setColorAt(2 * i, _c.setHex(c.shirt));
      arms.setColorAt(2 * i + 1, _c.setHex(c.shirt));
    });
    // Tent camp: one tent per two homeless people, fanned across the north side of the Hall.
    const tents = Math.min(PRESENT.tentCap, Math.ceil(homeless / 2));
    for (let t = 0; t < tents; t++) {
      const a = -Math.PI / 2 + (t - (tents - 1) / 2) * PRESENT.tentStep;
      const r = PRESENT.tentRadius + (t % 2) * 0.6;
      const x = hallX + r * Math.cos(a), z = hallZ + r * Math.sin(a);
      _root.set(x, groundHeight(state, tileOf(state, x, z)), z);
      put(tentCloth, t, _root, IDENTITY, 1, models.tent.parts[0].offset, null);
      put(tentDoor, t, _root, IDENTITY, 1, models.tent.parts[1].offset, null);
      tentCloth.setColorAt(t, _c.setHex(models.tent.parts[0].color));
      tentDoor.setColorAt(t, _c.setHex(models.tent.parts[1].color));
    }
    [[torso, list.length], [legs, list.length], [head, list.length], [arms, 2 * list.length], [tentCloth, tents], [tentDoor, tents]].forEach(([m, n]) => {
      m.count = n;
      m.visible = n > 0;
      m.instanceMatrix.needsUpdate = true;
      m.instanceColor.needsUpdate = true;
    });
    update(0, 0, state);
  }

  // Poses every citizen from the clock. Walkers ping-pong along their route at PRESENT.speed tiles a second.
  function update(dt, time, state) {
    void dt;
    if (list.length === 0) return;
    const W = state.width;
    for (let i = 0; i < list.length; i++) {
      const c = list[i];
      let x, y, z, heading, swing = 0, lift = 0;
      if (c.mode === WALK) {
        const r = c.route, n = r.length, cycle = 2 * (n - 1);
        const u = ((time * PRESENT.speed + c.phase) % cycle + cycle) % cycle;
        const back = u > n - 1;
        const dist = back ? cycle - u : u;
        const k = Math.min(Math.floor(dist), n - 2), f = dist - k, a = r[k], b = r[k + 1];
        const ax = (a % W) + 0.5, az = Math.floor(a / W) + 0.5, bx = (b % W) + 0.5, bz = Math.floor(b / W) + 0.5;
        x = ax + (bx - ax) * f;
        z = az + (bz - az) * f;
        const ya = walkHeight(state, a), yb = walkHeight(state, b);
        y = ya + (yb - ya) * f;
        heading = Math.atan2(back ? ax - bx : bx - ax, back ? az - bz : bz - az);
        const ph = time * PRESENT.bobHz * TAU + c.phase;
        lift = PRESENT.bobAmp * Math.abs(Math.sin(ph));
        swing = PRESENT.swing * Math.sin(ph);
      } else {
        const wander = c.mode === IDLE ? PRESENT.idleRadius : 0;
        const t = time * PRESENT.wanderRate + c.phase;
        x = c.ax + wander * Math.cos(t);
        z = c.az + wander * Math.sin(t);
        y = c.ay;
        heading = c.mode === IDLE ? Math.atan2(-Math.sin(t), Math.cos(t)) : c.face;
      }
      _root.set(x, y + lift, z);
      _qh.setFromAxisAngle(AXIS_Y, heading);
      put(torso, i, _root, _qh, c.scale, TORSO.offset, null);
      put(legs, i, _root, _qh, c.scale, LEGS_PART.offset, null);
      put(head, i, _root, _qh, c.scale, models.citizenHead.parts[0].offset, null);
      put(arms, 2 * i, _root, _qh, c.scale, ARM_L, _qa.setFromAxisAngle(AXIS_X, swing));
      put(arms, 2 * i + 1, _root, _qh, c.scale, ARM_R, _qa.setFromAxisAngle(AXIS_X, -swing));
    }
    torso.instanceMatrix.needsUpdate = true;
    legs.instanceMatrix.needsUpdate = true;
    head.instanceMatrix.needsUpdate = true;
    arms.instanceMatrix.needsUpdate = true;
  }

  return {
    sync,
    update,
    dispose() {
      scene.remove(group);
      for (const m of meshes) m.dispose();
      material.dispose();
    },
  };
}
