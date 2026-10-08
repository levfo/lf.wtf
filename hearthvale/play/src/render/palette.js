// owner: render-world
// Section 9.3: the palette, season tints and weather fog. Shared by every render module; read-only to the others.

export const PALETTE = Object.freeze({
  skyZenith: 0x8ccbe8, horizon: 0xf4e6c4, fog: 0xf4e6c4,
  grass: 0x86b85a, meadow: 0xb9d46a, meadowFlower: 0xf2d16b, forestFloor: 0x5f8f4b,
  canopy: 0x3d7a3c, canopyAutumn: 0xd8833a, pine: 0x2f5d3a, trunk: 0x7a5234,
  stone: 0xa4a9b0, iron: 0x6e7480, rust: 0xc0673c, mountain: 0x8d909b, snow: 0xf2f5f7,
  river: 0x3fa2d8, lake: 0x2f8ec6,
  plaster: 0xf2e6cc, roofRed: 0xb44b3c, roofSlate: 0x5d6b7a, thatch: 0xd6b05c, timber: 0x8b5a34, banner: 0xe7b13e,
  road: 0x8a7a64, bridge: 0xa0764a,
  sun: 0xfff1d6, hemiSky: 0xbfe3ff, hemiGround: 0x6b5a3c,
  gold: 0xe0b04a, ghostOk: 0x7fd67a, ghostBad: 0xe0584a, bandit: 0xb8322a, rain: 0xa9c7da,
  shirts: Object.freeze([0xc0583e, 0x3e7bb0, 0xd9a441, 0x6d9b5a, 0x8a6fb4]),
});

// Season multipliers for grass and canopy, indexed by season (0 spring, 1 summer, 2 autumn, 3 winter).
// White leaves the base colour unchanged. Autumn canopy uses PALETTE.canopyAutumn as its base colour.
export const SEASON_TINT = Object.freeze([
  Object.freeze({ grass: 0xffffff, canopy: 0xffffff }),
  Object.freeze({ grass: 0xf4f7c4, canopy: 0xe9f2d4 }),
  Object.freeze({ grass: 0xe8cc7a, canopy: 0xffffff }),
  Object.freeze({ grass: 0xa8b08c, canopy: 0xd6dfe0 }),
]);

const FOG_BY_WEATHER = Object.freeze({
  clear: PALETTE.horizon, rain: 0xc9d3d6, storm: 0x9aa4ac, snow: 0xe6ecef,
});

// Fog and horizon colour for a weather kind (clear, rain, storm, snow). Unknown kinds use the clear horizon.
export function fogByWeather(kind) {
  return Object.prototype.hasOwnProperty.call(FOG_BY_WEATHER, kind) ? FOG_BY_WEATHER[kind] : PALETTE.horizon;
}
