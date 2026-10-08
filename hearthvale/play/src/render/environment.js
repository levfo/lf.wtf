// owner: render-world
// Section 9.3: the sky dome, exponential fog, the yearly sun arc with soft shadows, the hemisphere light,
// and rain, storm and snow particles.
import * as THREE from 'three';
import { getSeasonInfo } from '../sim/queries.js';
import { PALETTE, SEASON_TINT, fogByWeather } from './palette.js';

const FOG_DENSITY = 0.006, FOG_DENSITY_WINTER = 0.009, FOG_EASE = 2;   // fog eases toward its goal at this rate per second
const SUN_INTENSITY = 1.4, HEMI_INTENSITY = 0.9, SHADOW_MAP = 1024, SHADOW_HALF = 20, SHADOW_RADIUS = 2.5;
const SUN_RANGE = 90, SUN_ELEV0 = 0.78, SUN_ELEV_AMP = 0.34, SUN_AZ0 = 0.8, SUN_AZ_AMP = 0.5, SUN_SUMMER = 0.375;
const SEASON_COUNT = 4, WINTER = 3, HALL = 32.5, PARTICLES = 600, BOX_HALF = 22, BOX_TOP = 18;
const RAIN_LENGTH = 0.8, RAIN_SPEED = 16, SNOW_SPEED = 2.2, SNOW_DRIFT = 0.4, SKY_RADIUS = 380;
const STORM_GREY = 0x6f7d88, SNOW_WHITE = 0xf4f8fb, TAU = Math.PI * 2;

// Season grass multipliers as colours, used to dim the ground bounce light in winter.
const SEASON_GRASS = SEASON_TINT.map((t) => new THREE.Color(t.grass));
const _zen = new THREE.Color(), _hor = new THREE.Color(), _tmp = new THREE.Color();

export function createEnvironment(scene, renderer) {
  renderer.shadowMap.enabled = true;

  const hemi = new THREE.HemisphereLight(PALETTE.hemiSky, PALETTE.hemiGround, HEMI_INTENSITY);
  const sun = new THREE.DirectionalLight(PALETTE.sun, SUN_INTENSITY);
  sun.castShadow = true;
  sun.shadow.mapSize.set(SHADOW_MAP, SHADOW_MAP);
  Object.assign(sun.shadow.camera, { left: -SHADOW_HALF, right: SHADOW_HALF, top: SHADOW_HALF, bottom: -SHADOW_HALF, near: 1, far: SUN_RANGE * 2 + 40 });
  sun.shadow.camera.updateProjectionMatrix();
  Object.assign(sun.shadow, { radius: SHADOW_RADIUS, bias: -0.0008, normalBias: 0.02 });   // radius: PCF soft edge
  sun.target.position.set(HALL, 0, HALL);
  scene.add(hemi, sun, sun.target);

  const fog = new THREE.FogExp2(PALETTE.horizon, FOG_DENSITY);
  scene.fog = fog;

  // Sky dome: the horizon colour at the rim, the zenith colour overhead. It is drawn without fog.
  const skyGeo = new THREE.SphereGeometry(SKY_RADIUS, 24, 12);
  const skyPos = skyGeo.attributes.position, skyCount = skyPos.count;
  const skyColours = new Float32Array(skyCount * 3);
  skyGeo.setAttribute('color', new THREE.BufferAttribute(skyColours, 3));
  const skyMat = new THREE.MeshBasicMaterial({ vertexColors: true, side: THREE.BackSide, fog: false, depthWrite: false });
  const sky = new THREE.Mesh(skyGeo, skyMat);
  Object.assign(sky, { frustumCulled: false, renderOrder: -1 }).position.set(HALL, 0, HALL);
  scene.add(sky);
  let skyKind = null;

  function paintSky(kind) {
    _zen.set(PALETTE.skyZenith);
    _hor.set(fogByWeather(kind));
    if (kind === 'storm') _zen.lerp(_tmp.set(STORM_GREY), 0.6);
    else if (kind === 'rain') _zen.lerp(_tmp.set(STORM_GREY), 0.35);
    else if (kind === 'snow') _zen.lerp(_tmp.set(SNOW_WHITE), 0.45);
    for (let i = 0; i < skyCount; i++) {
      const up = Math.min(1, Math.max(0, skyPos.getY(i) / SKY_RADIUS));
      _tmp.copy(_hor).lerp(_zen, Math.sqrt(up));
      skyColours.set([_tmp.r, _tmp.g, _tmp.b], i * 3);
    }
    skyGeo.attributes.color.needsUpdate = true;
  }

  // Weather particles in a box around the Town Hall, from a seeded generator so runs repeat.
  let seed = 982451653;
  const rnd = () => {
    seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0;
    return seed / 4294967296;
  };
  const px = new Float32Array(PARTICLES), py = new Float32Array(PARTICLES), pz = new Float32Array(PARTICLES);
  const phase = new Float32Array(PARTICLES);
  const respawn = (i) => {
    px[i] = HALL + (rnd() * 2 - 1) * BOX_HALF;
    py[i] = BOX_TOP;
    pz[i] = HALL + (rnd() * 2 - 1) * BOX_HALF;
  };
  for (let i = 0; i < PARTICLES; i++) {
    respawn(i);
    py[i] = rnd() * BOX_TOP;
    phase[i] = rnd() * TAU;
  }

  const rainPos = new Float32Array(PARTICLES * 6);
  const rainGeo = new THREE.BufferGeometry().setAttribute('position', new THREE.BufferAttribute(rainPos, 3));
  const rain = new THREE.LineSegments(rainGeo, new THREE.LineBasicMaterial({
    color: PALETTE.rain, transparent: true, opacity: 0.55, depthWrite: false,
  }));
  const snowPos = new Float32Array(PARTICLES * 3);
  const snowGeo = new THREE.BufferGeometry().setAttribute('position', new THREE.BufferAttribute(snowPos, 3));
  const snow = new THREE.Points(snowGeo, new THREE.PointsMaterial({
    color: PALETTE.snow, size: 0.16, sizeAttenuation: true, transparent: true, opacity: 0.9, depthWrite: false,
  }));
  for (const obj of [rain, snow]) {
    obj.frustumCulled = false;
    obj.visible = false;
    scene.add(obj);
  }

  function updateParticles(kind, dt, time) {
    const rainOn = kind === 'rain' || kind === 'storm';
    rain.visible = rainOn;
    snow.visible = kind === 'snow';
    if (rainOn) {
      const storm = kind === 'storm', lean = storm ? 0.6 : 0.15;
      const count = storm ? PARTICLES : Math.floor(PARTICLES * 0.6);
      rainGeo.setDrawRange(0, count * 2);
      for (let i = 0; i < count; i++) {
        py[i] -= RAIN_SPEED * dt;
        if (py[i] < 0) respawn(i);
        rainPos.set([px[i] + lean * RAIN_LENGTH, py[i] + RAIN_LENGTH, pz[i], px[i], py[i], pz[i]], i * 6);
      }
      rainGeo.attributes.position.needsUpdate = true;
    }
    if (snow.visible) {
      for (let i = 0; i < PARTICLES; i++) {
        py[i] -= SNOW_SPEED * dt;
        if (py[i] < 0) respawn(i);
        px[i] += Math.sin(time * 0.8 + phase[i]) * SNOW_DRIFT * dt;
        snowPos.set([px[i], py[i], pz[i]], i * 3);
      }
      snowGeo.attributes.position.needsUpdate = true;
    }
  }

  return {
    update(state, dt, time, dayFrac) {
      const step = dt > 0 ? dt : 0;
      const info = getSeasonInfo(state);
      // Days per season come from the view: today's index in the season plus the days left after it.
      const perSeason = info.dayOfSeason + info.daysLeft + 1;
      const df = Number.isFinite(dayFrac) ? dayFrac : 0;
      const yearFrac = (info.season + (info.dayOfSeason + df) / perSeason) / SEASON_COUNT;

      // A smooth sun arc over the year: high in summer, low in winter, drifting in azimuth. No jumps at a day boundary.
      const elev = SUN_ELEV0 + SUN_ELEV_AMP * Math.cos(TAU * (yearFrac - SUN_SUMMER));
      const az = SUN_AZ0 + SUN_AZ_AMP * Math.sin(TAU * yearFrac);
      const ce = Math.cos(elev);
      sun.position.set(HALL + SUN_RANGE * ce * Math.cos(az), SUN_RANGE * Math.sin(elev), HALL + SUN_RANGE * ce * Math.sin(az));

      const kind = state.weather ? state.weather.kind : 'clear';
      if (kind !== skyKind) {
        skyKind = kind;
        paintSky(kind);
      }
      const k = 1 - Math.exp(-step * FOG_EASE);
      fog.color.lerp(_tmp.set(fogByWeather(kind)), k);
      fog.density += ((info.season === WINTER ? FOG_DENSITY_WINTER : FOG_DENSITY) - fog.density) * k;
      hemi.groundColor.set(PALETTE.hemiGround).multiply(SEASON_GRASS[info.season]);
      updateParticles(kind, step, time);
    },

    dispose() {
      scene.remove(hemi, sun, sun.target, sky, rain, snow);
      scene.fog = null;
      for (const o of [skyGeo, skyMat, rainGeo, rain.material, snowGeo, snow.material]) o.dispose();
      if (sun.shadow.map) sun.shadow.map.dispose();
    },
  };
}
