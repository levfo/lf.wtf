// owner: foundation
// Section 3.2: the only randomness in the simulation. Integer arithmetic only (Math.imul, shifts).

// One mulberry32 step on the 32-bit word t; returns a float in [0, 1).
function step(t) {
  t = Math.imul(t ^ (t >>> 15), t | 1);
  t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
  return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
}

// Advances state.rng (a uint32) and returns a float in [0, 1). Uses exactly one step.
export function rand(state) {
  state.rng = (state.rng + 0x6D2B79F5) >>> 0;
  return step(state.rng);
}

// Integer in [lo, hi] inclusive. Uses rand once.
export function randInt(state, lo, hi) {
  const r = rand(state);
  const span = hi - lo + 1;
  if (span < 1) return lo;
  return lo + Math.floor(r * span);
}

// Uniform element of a non-empty array. Uses rand once.
export function pick(state, list) {
  const r = rand(state);
  return list[Math.floor(r * list.length)];
}

// True with probability p (rand(state) < p). Uses rand once.
export function chance(state, p) {
  return rand(state) < p;
}

// Local mulberry32 stream for map generation. Never touches a state object.
export function mulberry32(seed) {
  let a = seed >>> 0;
  return function next() {
    a = (a + 0x6D2B79F5) >>> 0;
    return step(a);
  };
}

// 32-bit finaliser (murmur3 style). Integer operations only.
function mix32(h) {
  h = Math.imul(h ^ (h >>> 16), 0x85EBCA6B);
  h = Math.imul(h ^ (h >>> 13), 0xC2B2AE35);
  return h ^ (h >>> 16);
}

// Float in [0, 1) from integer coordinates and a seed. Used by value noise in map generation.
export function hash2(ix, iy, seed) {
  const h = mix32(mix32((seed >>> 0) ^ Math.imul(ix | 0, 0x27D4EB2D)) ^ Math.imul(iy | 0, 0x165667B1));
  return (h >>> 0) / 4294967296;
}
