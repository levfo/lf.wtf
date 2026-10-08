// owner: render-world
// Section 9.2: the orbit camera. Target, yaw and pitch, a gliding focus and a damped zoom.
import * as THREE from 'three';

const TARGET0 = 32.5;                 // the Town Hall tile centre (world x and z)
const YAW0 = 35 * Math.PI / 180;      // camera south-east of the Hall
const PITCH0 = 48 * Math.PI / 180;
const DISTANCE0 = 34;
const FOV = 42;
const DIST_MIN = 18;
const DIST_MAX = 60;
const PITCH_MIN = 0.35;
const PITCH_MAX = 1.2;
const TARGET_MIN = -2;
const TARGET_MAX = 66;
const GLIDE_SECONDS = 1.5;
const ZOOM_RATE = 10;                 // damping rate of the zoom, per second
const NEAR = 0.5;
const FAR = 600;                      // beyond the sky dome (radius 380) seen from the orbit
const TAU = Math.PI * 2;

function clamp(v, lo, hi) {
  return v < lo ? lo : (v > hi ? hi : v);
}

function aspectOf(w, h) {
  return w > 0 && h > 0 ? w / h : 1;
}

function easeInOut(u) {
  return u * u * (3 - 2 * u);
}

export function createCamera(canvas, cssWidth, cssHeight) {
  const three = new THREE.PerspectiveCamera(FOV, aspectOf(cssWidth, cssHeight), NEAR, FAR);
  const s = {
    tx: TARGET0,
    tz: TARGET0,
    yaw: YAW0,
    pitch: clamp(PITCH0, PITCH_MIN, PITCH_MAX),
    dist: DISTANCE0,
    goal: DISTANCE0,
    glide: null,
  };

  function clampTarget() {
    s.tx = clamp(s.tx, TARGET_MIN, TARGET_MAX);
    s.tz = clamp(s.tz, TARGET_MIN, TARGET_MAX);
  }

  // Position = target + distance * (sin(yaw) cos(pitch), sin(pitch), cos(yaw) cos(pitch)), looking at the target.
  function place() {
    const cp = Math.cos(s.pitch);
    three.position.set(
      s.tx + s.dist * Math.sin(s.yaw) * cp,
      s.dist * Math.sin(s.pitch),
      s.tz + s.dist * Math.cos(s.yaw) * cp,
    );
    three.lookAt(s.tx, 0, s.tz);
    three.updateMatrixWorld();
  }

  place();

  return {
    update(dt) {
      const step = dt > 0 ? dt : 0;
      if (s.glide) {
        const g = s.glide;
        g.t += step;
        const u = Math.min(1, g.t / g.dur);
        const e = easeInOut(u);
        s.tx = g.fx + (g.tx - g.fx) * e;
        s.tz = g.fz + (g.tz - g.fz) * e;
        if (u >= 1) s.glide = null;
      }
      s.dist += (s.goal - s.dist) * (1 - Math.exp(-step * ZOOM_RATE));
      clampTarget();
      place();
    },

    focusTile(x, y, seconds) {
      if (!Number.isFinite(x) || !Number.isFinite(y)) return;
      const dur = typeof seconds === 'number' && seconds >= 0 ? seconds : GLIDE_SECONDS;
      const tx = clamp(x + 0.5, TARGET_MIN, TARGET_MAX);
      const tz = clamp(y + 0.5, TARGET_MIN, TARGET_MAX);
      if (dur === 0) {
        s.glide = null;
        s.tx = tx;
        s.tz = tz;
        place();
        return;
      }
      s.glide = { fx: s.tx, fz: s.tz, tx, tz, t: 0, dur };
    },

    panBy(dxTiles, dyTiles) {
      if (!Number.isFinite(dxTiles) || !Number.isFinite(dyTiles)) return;
      s.glide = null;
      const rx = Math.cos(s.yaw);       // screen right on the ground
      const rz = -Math.sin(s.yaw);
      const fx = -Math.sin(s.yaw);      // screen up on the ground
      const fz = -Math.cos(s.yaw);
      s.tx += dxTiles * rx + dyTiles * fx;
      s.tz += dxTiles * rz + dyTiles * fz;
      clampTarget();
      place();
    },

    rotateBy(radians) {
      if (!Number.isFinite(radians)) return;
      s.yaw = ((s.yaw + radians) % TAU + TAU) % TAU;
      place();
    },

    zoomBy(factor) {
      if (!(factor > 0)) return;
      s.goal = clamp(s.goal * factor, DIST_MIN, DIST_MAX);
    },

    setViewport(cssWidth, cssHeight) {
      three.aspect = aspectOf(cssWidth, cssHeight);
      three.updateProjectionMatrix();
    },

    yaw() {
      return s.yaw;
    },

    distance() {
      return s.dist;
    },

    target() {
      return { x: s.tx, z: s.tz };
    },

    three,
  };
}
