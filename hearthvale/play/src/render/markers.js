// owner: render-structures
// Section 9.4: objective rings (gold with a dark outline, scale 0.9 to 1.1 at 1.2 Hz), the hover tile, the gold outline
// under the selected building, road preview tiles (green when ok, red when not) and the ghost outline. Heights come from
// models.js groundAt. Change R1-15: while a building is armed, a small green dot with a dark halo marks each tile the
// armed type can be placed on.
import * as THREE from 'three';
import { PALETTE } from './palette.js';
import { groundAt, groundHeight } from './models.js';
// The one approved render-to-queries edge (R1-15): getBuildableTiles only reads the state it is given.
import { getBuildableTiles } from '../sim/queries.js';

// ringIn and ringOut: the gold band, from the tile's own edge outward. haloOut: the outer edge of the dark outline.
const PRESENT = { ringCap: 16, ringIn: 0.5, ringOut: 0.72, haloOut: 0.82, ringLift: 0.1, ink: 0x2b2622, roadCap: 128, pulseHz: 1.2, pulseAmp: 0.1, lift: 0.05, hoverAlpha: 0.35, roadAlpha: 0.5, frameWidth: 0.08, armedDot: 0.14, armedHalo: 0.2, armedAlpha: 0.85, armedHaloAlpha: 0.5 };
const NO_TURN = new THREE.Quaternion(), UNIT = new THREE.Vector3(1, 1, 1);
const _m = new THREE.Matrix4(), _p = new THREE.Vector3(), _s = new THREE.Vector3(), _c = new THREE.Color();

// Outline of a tile rectangle (x0..x1, z0..z1 in tile units): a ring lying flat on the ground.
function frameGeometry(x0, z0, x1, z1, t) {
  const rect = (a, b, c, d) => new THREE.Path().moveTo(a, b).lineTo(c, b).lineTo(c, d).lineTo(a, d).lineTo(a, b);
  const shape = new THREE.Shape(rect(x0, z0, x1, z1).getPoints());
  shape.holes.push(rect(x0 + t, z0 + t, x1 - t, z1 - t));
  return new THREE.ShapeGeometry(shape).rotateX(Math.PI / 2); // shape y becomes world z
}

export function createMarkers(scene) {
  const group = new THREE.Group();
  group.name = 'markers';
  scene.add(group);

  // The gold ring and its dark outline share one transform per marker. They are drawn without the depth test: the
  // ground is faceted and can rise well above the tile height beside a site, which would hide a ring lying on it.
  // The outline keeps the gold legible on meadow.
  const ringGeo = new THREE.RingGeometry(PRESENT.ringIn, PRESENT.ringOut, 32).rotateX(-Math.PI / 2);
  const rings = new THREE.InstancedMesh(ringGeo, new THREE.MeshBasicMaterial({ color: PALETTE.gold, transparent: true, opacity: 1, depthWrite: false, depthTest: false, side: THREE.DoubleSide }), PRESENT.ringCap);
  Object.assign(rings, { count: 0, visible: false, frustumCulled: false });
  const haloGeo = new THREE.RingGeometry(PRESENT.ringOut, PRESENT.haloOut, 32).rotateX(-Math.PI / 2);
  const halo = new THREE.InstancedMesh(haloGeo, new THREE.MeshBasicMaterial({ color: PRESENT.ink, transparent: true, opacity: 0.85, depthWrite: false, depthTest: false, side: THREE.DoubleSide }), PRESENT.ringCap);
  Object.assign(halo, { count: 0, visible: false, frustumCulled: false });
  let ringList = [], sig = '';

  const tileGeo = new THREE.PlaneGeometry(1, 1).rotateX(-Math.PI / 2);
  const hover = new THREE.Mesh(tileGeo, new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: PRESENT.hoverAlpha, depthWrite: false }));
  const road = new THREE.InstancedMesh(tileGeo, new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: PRESENT.roadAlpha, depthWrite: false }), PRESENT.roadCap);
  road.instanceColor = new THREE.InstancedBufferAttribute(new Float32Array(PRESENT.roadCap * 3), 3);
  Object.assign(road, { count: 0, visible: false, frustumCulled: false });
  hover.visible = false;
  group.add(halo, rings, hover, road);

  const frames = [0, 1].map(() => {
    const mesh = new THREE.Mesh(new THREE.BufferGeometry(), new THREE.MeshBasicMaterial({ transparent: true, opacity: 0.9, depthWrite: false }));
    mesh.visible = false;
    group.add(mesh);
    return { mesh, key: '' };
  });
  // Outline of a set of tiles, sitting just above the highest of them.
  const frame = (f, tiles, colour) => {
    if (!tiles || tiles.length === 0) { f.mesh.visible = false; f.key = ''; return; }
    const xs = tiles.map((t) => t.x), ys = tiles.map((t) => t.y);
    const x0 = Math.min(...xs), y0 = Math.min(...ys), x1 = Math.max(...xs) + 1, y1 = Math.max(...ys) + 1;
    const key = [x0, y0, x1, y1].join(',');
    if (key !== f.key) {
      f.key = key;
      f.mesh.geometry.dispose();
      f.mesh.geometry = frameGeometry(x0, y0, x1, y1, PRESENT.frameWidth);
    }
    f.mesh.material.color.setHex(colour);
    f.mesh.position.y = Math.max(...tiles.map((t) => groundAt(t.x + 0.5, t.y + 0.5))) + PRESENT.lift;
    f.mesh.visible = true;
  };

  // Armed building (R1-15): a green dot with a dark halo on each tile the armed type can be placed on. getBuildableTiles
  // reads the placement rules, so the dots are rebuilt only when something that decides placement changes: the map or the
  // buildings (rev counters), the stock (costs), the tier or the outcome. The meshes hold a full map of dots and are made
  // once per map size, so rebuilding writes matrices and never allocates.
  const armedDotGeo = new THREE.CircleGeometry(PRESENT.armedDot, 14).rotateX(-Math.PI / 2);
  const armedEdgeGeo = new THREE.RingGeometry(PRESENT.armedDot, PRESENT.armedHalo, 14).rotateX(-Math.PI / 2);
  const armedDotMat = new THREE.MeshBasicMaterial({ color: PALETTE.ghostOk, transparent: true, opacity: PRESENT.armedAlpha, depthWrite: false });
  const armedEdgeMat = new THREE.MeshBasicMaterial({ color: PRESENT.ink, transparent: true, opacity: PRESENT.armedHaloAlpha, depthWrite: false });
  const armed = { dots: null, edges: null, cap: 0, state: null, type: '', stamp: '', count: 0 };
  const armedMeshes = () => [armed.dots, armed.edges].filter(Boolean);
  const armedStamp = (state) => {
    const s = state.stock;
    return [state.rev.map, state.rev.buildings, state.tier, state.outcome.status, s.food, s.wood, s.stone, s.iron, s.goods, s.gold].join(',');
  };
  // Makes both meshes hold at least n instances. A smaller pair is replaced, not resized; geometry and materials are shared.
  const armedCapacity = (n) => {
    if (n <= armed.cap) return;
    for (const m of armedMeshes()) { group.remove(m); m.dispose(); }
    armed.dots = new THREE.InstancedMesh(armedDotGeo, armedDotMat, n);
    armed.edges = new THREE.InstancedMesh(armedEdgeGeo, armedEdgeMat, n);
    for (const m of armedMeshes()) { Object.assign(m, { count: 0, visible: false, frustumCulled: false }); group.add(m); }
    armed.cap = n;
  };
  const showArmed = (on) => {
    for (const m of armedMeshes()) { m.count = on ? armed.count : 0; m.visible = on && armed.count > 0; }
  };
  // a is {state, type} while a building is armed, else null. Hiding keeps the cached dots for the next arming.
  function setArmed(a) {
    if (!a || !a.state || typeof a.type !== 'string') { showArmed(false); return; }
    const { state, type } = a;
    const stamp = armedStamp(state);
    if (state !== armed.state || type !== armed.type || stamp !== armed.stamp) {
      const tiles = getBuildableTiles(state, type);
      armedCapacity(state.width * state.height);
      tiles.forEach((t, i) => {
        // Tile index t: its centre, at the tile's own ground height (the same height groundAt reads for that tile).
        _p.set((t % state.width) + 0.5, groundHeight(state, t) + PRESENT.lift, Math.floor(t / state.width) + 0.5);
        _m.compose(_p, NO_TURN, UNIT);
        armed.dots.setMatrixAt(i, _m);
        armed.edges.setMatrixAt(i, _m);
      });
      armed.dots.instanceMatrix.needsUpdate = true;
      armed.edges.instanceMatrix.needsUpdate = true;
      Object.assign(armed, { state, type, stamp, count: tiles.length });
    }
    showArmed(true);
  }

  return {
    // Tutorial markers {x, y, kind}. Rewritten only when the list changes.
    set(markers) {
      const items = (markers || []).slice(0, PRESENT.ringCap);
      const next = items.map((m) => `${m.x},${m.y},${m.kind}`).join('|');
      if (next === sig) return;
      sig = next;
      ringList = items.map((m) => ({ x: m.x + 0.5, z: m.y + 0.5 }));
      rings.count = halo.count = ringList.length;
      rings.visible = halo.visible = ringList.length > 0;
    },
    update(dt, time) {
      void dt;
      if (ringList.length === 0) return;
      const s = 1 + PRESENT.pulseAmp * Math.sin(2 * Math.PI * PRESENT.pulseHz * time);
      _s.set(s, s, s);
      ringList.forEach((r, i) => {
        _p.set(r.x, groundAt(r.x, r.z) + PRESENT.ringLift, r.z);
        _m.compose(_p, NO_TURN, _s);
        rings.setMatrixAt(i, _m);
        halo.setMatrixAt(i, _m);
      });
      rings.instanceMatrix.needsUpdate = true;
      halo.instanceMatrix.needsUpdate = true;
    },
    // {hover, selectedTiles, roadPreview, ghostTiles, ghostOk, armed}: hover is {x, y} or null; the rest are tile lists.
    // armed is {state, type} while a building is armed (R1-15), else null or absent.
    overlay(o) {
      hover.visible = !!o.hover;
      if (o.hover) hover.position.set(o.hover.x + 0.5, groundAt(o.hover.x + 0.5, o.hover.y + 0.5) + PRESENT.lift, o.hover.y + 0.5);
      frame(frames[0], o.selectedTiles, PALETTE.gold);
      frame(frames[1], o.ghostTiles, o.ghostOk ? PALETTE.ghostOk : PALETTE.ghostBad);
      const tiles = (o.roadPreview || []).slice(0, PRESENT.roadCap);
      tiles.forEach((t, i) => {
        _p.set(t.x + 0.5, groundAt(t.x + 0.5, t.y + 0.5) + PRESENT.lift, t.y + 0.5);
        road.setMatrixAt(i, _m.compose(_p, NO_TURN, UNIT));
        road.setColorAt(i, _c.setHex(t.ok ? PALETTE.ghostOk : PALETTE.ghostBad));
      });
      road.count = tiles.length;
      road.visible = tiles.length > 0;
      road.instanceMatrix.needsUpdate = true;
      road.instanceColor.needsUpdate = true;
      setArmed(o.armed);
    },
    dispose() {
      scene.remove(group);
      ringGeo.dispose();
      haloGeo.dispose();
      tileGeo.dispose();
      for (const m of [rings, halo, road]) { m.material.dispose(); m.dispose(); }
      hover.material.dispose();
      for (const f of frames) { f.mesh.geometry.dispose(); f.mesh.material.dispose(); }
      for (const m of armedMeshes()) m.dispose();
      armedDotGeo.dispose(); armedEdgeGeo.dispose(); armedDotMat.dispose(); armedEdgeMat.dispose();
    },
  };
}
