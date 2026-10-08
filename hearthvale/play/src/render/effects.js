// owner: render-structures
// Section 9.4 and DESIGN section 11: pooled particles (dust, smoke, flames, water, sheaves, confetti, plague haze and
// lanterns), the raid's red banner and four bandit riders, and chimney smoke from homes, workshops and taverns.
// Sound cues belong to audio.js; this module only draws. PRESENT holds presentation values, not balance numbers.
import * as THREE from 'three';
import { PALETTE } from './palette.js';
import { TERRAIN } from '../sim/state.js';
import { getModels, groundAt, groundHeight, rotateOffset, setActiveState } from './models.js';

const PRESENT = {
  bitCap: 96, glowCap: 4, hazeCap: 16, riderCap: 4, rideTime: 6, flagTime: 3, smokeRate: 0.4,
  smokeTypes: ['cottage', 'townhouse', 'workshop', 'tavern'], gravity: 9, sheafTime: 0.8, sheafCount: 6,
  dustCount: 6, burstCount: 8, confettiCount: 30, hazeCount: 6, lanternTime: 3,
};
const TAU = Math.PI * 2, AXIS_Y = new THREE.Vector3(0, 1, 0);
// Presentation-only variety from a counter hash: deterministic and independent of the simulation (rule 4).
let rseed = 0;
const rnd = () => { rseed += 1; return (Math.imul(rseed, 2654435761) >>> 0) / 4294967296; };
const ZERO = new THREE.Matrix4().makeScale(0, 0, 0);
const CONFETTI = [PALETTE.gold, PALETTE.bandit, PALETTE.river, PALETTE.meadow, 0xffffff];
const _m = new THREE.Matrix4(), _p = new THREE.Vector3(), _s = new THREE.Vector3(), _v = new THREE.Vector3();
const _q = new THREE.Quaternion(), _qh = new THREE.Quaternion(), _root = new THREE.Vector3(), _c = new THREE.Color();
const NO_TURN = new THREE.Quaternion();
const std = () => new THREE.MeshStandardMaterial({ roughness: 0.9, flatShading: true });

// A pool of particles drawn as one InstancedMesh; every slot starts hidden (zero scale).
function makePool(geometry, material, cap) {
  const mesh = new THREE.InstancedMesh(geometry, material, cap);
  mesh.instanceColor = new THREE.InstancedBufferAttribute(new Float32Array(cap * 3), 3);
  mesh.frustumCulled = false;
  const list = Array.from({ length: cap }, (_, idx) => {
    mesh.setMatrixAt(idx, ZERO);
    return { idx, alive: false, x: 0, y: 0, z: 0, vx: 0, vy: 0, vz: 0, g: 0, age: 0, life: 1, s0: 0, s1: 0, spin: 0, sp: 0 };
  });
  return { mesh, list, dirty: false };
}

// Writes one part of a figure: the root position and heading, the part's offset scaled and turned by the heading.
function place(mesh, k, root, qh, s, o) {
  _v.set(o[0] * s, o[1] * s, o[2] * s).applyQuaternion(qh);
  _p.copy(root).add(_v);
  _s.set(s, s, s);
  mesh.setMatrixAt(k, _m.compose(_p, qh, _s));
}

export function createEffects(scene, capacity = 256) {
  const models = getModels();
  const group = new THREE.Group();
  group.name = 'effects';
  scene.add(group);

  const pools = [
    makePool(new THREE.IcosahedronGeometry(1, 0), std(), capacity),
    makePool(new THREE.BoxGeometry(1, 1, 1), std(), PRESENT.bitCap),
    makePool(new THREE.SphereGeometry(1, 6, 4), new THREE.MeshBasicMaterial(), PRESENT.glowCap),
    makePool(new THREE.IcosahedronGeometry(1, 1), new THREE.MeshStandardMaterial({ roughness: 1, flatShading: true, transparent: true, opacity: 0.32, depthWrite: false }), PRESENT.hazeCap),
  ];
  const [puffs, bits, glows, hazes] = pools;
  for (const p of pools) group.add(p.mesh);

  const riderParts = models.rider.parts;
  const riderMeshes = riderParts.map((part) => {
    const m = new THREE.InstancedMesh(part.geometry, std(), PRESENT.riderCap);
    m.instanceColor = new THREE.InstancedBufferAttribute(new Float32Array(PRESENT.riderCap * 3), 3);
    m.frustumCulled = false;
    for (let i = 0; i < PRESENT.riderCap; i++) { m.setMatrixAt(i, ZERO); m.setColorAt(i, _c.setHex(part.color)); }
    group.add(m);
    return m;
  });
  const riders = Array.from({ length: PRESENT.riderCap }, () => ({ on: false, t: 0, x0: 0, z0: 0, x1: 0, z1: 0 }));

  // The raid banner at the north edge: the pole and the red cloth, shown while the flag is up.
  const [POLE, CLOTH] = models.banner.parts;
  const banner = [POLE, CLOTH].map((part) => {
    const m = new THREE.InstancedMesh(part.geometry, std(), 1);
    m.instanceColor = new THREE.InstancedBufferAttribute(new Float32Array(3), 3);
    m.setColorAt(0, _c.setHex(part.color));
    m.setMatrixAt(0, ZERO);
    Object.assign(m, { count: 0, visible: false, frustumCulled: false });
    group.add(m);
    return m;
  });
  const [pole, cloth] = banner;

  let flagT = 0, bannerX = 0, bannerZ = 0, time = 0, lastState = null;
  const writeBanner = (m, part, g, sy) => {
    _p.set(bannerX + part.offset[0], g + part.offset[1], bannerZ + part.offset[2]);
    _s.set(1, sy, 1);
    m.setMatrixAt(0, _m.compose(_p, NO_TURN, _s));
    m.instanceMatrix.needsUpdate = true;
  };
  let smokeState = null, smokeKey = '', smokers = [];

  const hallPoint = (s) => {
    const h = s.buildings.find((b) => b.type === 'townHall');
    return h ? { x: h.x + h.w / 2, z: h.y + h.h / 2 } : { x: s.width / 2, z: s.height / 2 };
  };
  // Where an event happened: its tile, its building, or else the Town Hall.
  const pointOf = (s, ev) => {
    if (ev.x !== undefined) return { x: ev.x + 0.5, z: ev.y + 0.5 };
    const b = ev.id ? s.buildings.find((q) => q.id === ev.id) : null;
    return b ? { x: b.x + b.w / 2, z: b.y + b.h / 2 } : hallPoint(s);
  };

  function spawn(pool, x, y, z, vx, vy, vz, life, s0, s1, colour, g = 0) {
    const p = pool.list.find((q) => !q.alive);
    if (!p) return;
    Object.assign(p, { alive: true, x, y, z, vx, vy, vz, g, age: 0, life, s0, s1, spin: rnd() * TAU, sp: (rnd() - 0.5) * 6 });
    pool.mesh.setColorAt(p.idx, _c.setHex(colour));
    pool.dirty = true;
  }

  // Puffs flung out from a point: o.lift above ground, o.spread radius, o.vy upward speed, gravity o.g.
  function burst(pt, n, colours, o) {
    const y = groundAt(pt.x, pt.z) + o.lift;
    for (let i = 0; i < n; i++) {
      const a = rnd() * TAU, d = rnd() * o.spread;
      spawn(puffs, pt.x + Math.cos(a) * d, y, pt.z + Math.sin(a) * d, Math.cos(a) * 0.6, o.vy, Math.sin(a) * 0.6, o.life, o.s0, o.s1, colours[i % colours.length], o.g);
    }
  }

  // Six sheaves leave the farm that harvested last and arc to the Town Hall over 0.8 s.
  function sheaves(s) {
    let from = null;
    for (const b of s.buildings) {
      if (b.type === 'farm' && b.stage === 'complete' && (!from || b.lastHarvestDay > from.lastHarvestDay)) from = b;
    }
    const o = from ? { x: from.x + from.w / 2, z: from.y + from.h / 2 } : hallPoint(s);
    const h = hallPoint(s), T = PRESENT.sheafTime, g = PRESENT.gravity;
    const oy = groundAt(o.x, o.z) + 0.6, ty = groundAt(h.x, h.z) + 0.9;
    for (let i = 0; i < PRESENT.sheafCount; i++) {
      const j = (i - 2.5) * 0.08;
      spawn(bits, o.x + j, oy, o.z, (h.x - o.x + j) / T, (ty - oy) / T + 0.5 * g * T, (h.z - o.z) / T, T, 0.14, 0.14, 0xe3c77a, g);
    }
  }

  function confetti(s) {
    const h = hallPoint(s), y = groundAt(h.x, h.z) + 2;
    for (let i = 0; i < PRESENT.confettiCount; i++) {
      spawn(bits, h.x, y, h.z, (rnd() - 0.5) * 3, 2.5 + rnd() * 2, (rnd() - 0.5) * 3, 2.2, 0.14, 0.1, CONFETTI[i % CONFETTI.length], 4);
    }
  }

  function haze(s) {
    const h = hallPoint(s), y = groundAt(h.x, h.z) + 1;
    for (let i = 0; i < PRESENT.hazeCount; i++) {
      const a = (i / PRESENT.hazeCount) * TAU;
      spawn(hazes, h.x + Math.cos(a) * 1.2, y, h.z + Math.sin(a) * 1.2, 0, 0.12, 0, 4, 0.5, 1.5, 0x8fc98a);
    }
  }

  // A lantern drifts across the lake from its west shore to its east shore.
  function lantern(s) {
    let x0 = Infinity, x1 = -Infinity, zSum = 0, n = 0;
    for (let i = 0; i < s.map.terrain.length; i++) {
      if (s.map.terrain[i] !== TERRAIN.LAKE) continue;
      x0 = Math.min(x0, i % s.width); x1 = Math.max(x1, i % s.width);
      zSum += Math.floor(i / s.width); n++;
    }
    if (n === 0) return;
    const z = zSum / n + 0.5, T = PRESENT.lanternTime;
    spawn(glows, x0 + 0.5, groundAt(x0 + 0.5, z) + 0.5, z, (x1 - x0) / T, 0.2, 0, T, 0.16, 0.12, 0xffd27a);
  }

  // The raid: the banner goes up on the north edge and four riders cross to the Town Hall over 6 seconds.
  function raid(s) {
    const h = hallPoint(s);
    bannerX = h.x - 3; bannerZ = 0.8; flagT = PRESENT.flagTime;
    riders.forEach((r, i) => Object.assign(r, { on: true, t: 0, x0: h.x + (i - 1.5) * 1.5, z0: 0.8, x1: h.x + (i - 1.5) * 0.5, z1: h.z - 1.2 }));
  }

  // Chimney smoke sources: complete homes, workshops and taverns. Rebuilt when rev.buildings or rev.map changes.
  function refreshSmokers(s) {
    const key = s.rev.buildings + ':' + s.rev.map;
    if (s === smokeState && key === smokeKey) return;
    smokeState = s;
    smokeKey = key;
    smokers = [];
    for (const b of s.buildings) {
      const def = models.buildings[b.type];
      if (b.stage !== 'complete' || !def || !def.chimney || !PRESENT.smokeTypes.includes(b.type)) continue;
      const cx = b.x + b.w / 2, cz = b.y + b.h / 2, a = rotateOffset(def.chimney, b.rot);
      smokers.push({ x: cx + a[0], y: groundHeight(s, Math.floor(cz) * s.width + Math.floor(cx)) + a[1], z: cz + a[2], acc: 0 });
    }
  }

  function stepPool(pool, dt) {
    for (const p of pool.list) {
      if (!p.alive) continue;
      p.age += dt;
      if (p.age >= p.life) {
        p.alive = false;
        pool.mesh.setMatrixAt(p.idx, ZERO);
        pool.dirty = true;
        continue;
      }
      p.vy -= p.g * dt;
      p.x += p.vx * dt; p.y += p.vy * dt; p.z += p.vz * dt;
      const s = p.s0 + (p.s1 - p.s0) * (p.age / p.life);
      _q.setFromAxisAngle(AXIS_Y, p.spin + p.sp * p.age);
      _s.set(s, s, s);
      pool.mesh.setMatrixAt(p.idx, _m.compose(_p.set(p.x, p.y, p.z), _q, _s));
      pool.dirty = true;
    }
    if (pool.dirty) {
      pool.mesh.instanceMatrix.needsUpdate = true;
      pool.mesh.instanceColor.needsUpdate = true;
      pool.dirty = false;
    }
  }

  function stepRiders(dt) {
    riders.forEach((r, i) => {
      if (!r.on) return;
      r.t += dt;
      if (r.t >= PRESENT.rideTime) {
        r.on = false;
        for (const m of riderMeshes) { m.setMatrixAt(i, ZERO); m.instanceMatrix.needsUpdate = true; }
        return;
      }
      const u = r.t / PRESENT.rideTime;
      const x = r.x0 + (r.x1 - r.x0) * u, z = r.z0 + (r.z1 - r.z0) * u;
      _root.set(x, groundAt(x, z) + Math.abs(Math.sin(time * 10 + i)) * 0.03, z);
      _qh.setFromAxisAngle(AXIS_Y, Math.atan2(r.x1 - r.x0, r.z1 - r.z0));
      const fade = u > 0.8 ? (1 - u) / 0.2 : 1; // riders shrink away over the last fifth of the ride
      riderMeshes.forEach((m, k) => place(m, i, _root, _qh, fade, riderParts[k].offset));
      for (const m of riderMeshes) m.instanceMatrix.needsUpdate = true;
    });
  }
  const dust = (pt) => burst(pt, PRESENT.dustCount, [0xc8b48a], { lift: 0.15, spread: 0.2, vy: 0.9, life: 0.8, s0: 0.1, s1: 0.35, g: 1.5 });
  const flames = (pt) => burst(pt, PRESENT.burstCount, [0xf2b04a, 0xe0703a], { lift: 0.2, spread: 0.4, vy: 1.1, life: 0.9, s0: 0.22, s1: 0.06, g: -0.4 });
  const water = (pt) => burst(pt, PRESENT.burstCount, [PALETTE.river], { lift: 0.3, spread: 0.3, vy: 1.0, life: 0.9, s0: 0.14, s1: 0.08, g: 3 });

  return {
    handle(events, state) {
      setActiveState(state);
      lastState = state;
      for (const ev of events) {
        switch (ev.type) {
          case 'buildingComplete': case 'placed': dust(pointOf(state, ev)); break;
          case 'harvest': sheaves(state); break;
          case 'buildingDestroyed': flames(pointOf(state, ev)); break;
          case 'fire': if (ev.x !== undefined) flames(pointOf(state, ev)); break;
          case 'fireContained': water(pointOf(state, ev)); break;
          case 'raid': raid(state); break;
          case 'plagueStart': haze(state); break;
          case 'festival': case 'harvestFair': case 'milestone': case 'tier': confetti(state); break;
          case 'outcome': if (ev.kind === 'good') confetti(state); break;
          case 'citizenDied': lantern(state); break;
          default: break;
        }
      }
    },
    update(dt) {
      time += dt;
      if (lastState) {
        refreshSmokers(lastState);
        for (const r of smokers) {
          r.acc += dt * PRESENT.smokeRate;
          while (r.acc >= 1) {
            r.acc -= 1;
            spawn(puffs, r.x, r.y, r.z, 0.08, 0.35, 0, 3.2, 0.12, 0.5, 0xc9c4bb, -0.02);
          }
        }
      }
      for (const p of pools) stepPool(p, dt);
      stepRiders(dt);
      const on = flagT > 0;
      if (on) {
        flagT -= dt;
        const g = groundAt(bannerX, bannerZ);
        writeBanner(pole, POLE, g, 1);
        writeBanner(cloth, CLOTH, g, 1 + 0.15 * Math.sin(time * 25));
      }
      for (const m of banner) { m.visible = on; m.count = on ? 1 : 0; }
    },
    dispose() {
      scene.remove(group);
      for (const p of pools) { p.mesh.geometry.dispose(); p.mesh.material.dispose(); p.mesh.dispose(); }
      for (const m of riderMeshes) { m.material.dispose(); m.dispose(); }
      for (const m of banner) { m.material.dispose(); m.dispose(); }
    },
  };
}
