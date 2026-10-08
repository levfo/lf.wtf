// owner: foundation
// Section 5.7: weather, disasters and threats. Weight keys are written in the canonical roll order
// (clear, rain, storm, snow) so that a weighted roll in key order matches section 8.1 b.

export const EVENTS = {
  weather: {
    seasonWeights: [
      { clear: 50, rain: 35, storm: 15 },
      { clear: 60, rain: 25, storm: 15 },
      { clear: 45, rain: 35, storm: 20 },
      { clear: 40, storm: 15, snow: 45 },
    ],
    minDays: 2, extraDays: 3,
  },
  fire: {
    startDay: 15, chance: 0.006, winterChance: 0.012, minDwellings: 3,
    containRadius: 5, containChance: 0.7, scareDays: 5,
  },
  flood: { season: 0, startDay: 20, minPop: 15, chance: 0.02, warnDays: 2, durationDays: 6 },
  drought: { season: 1, startDay: 12, chance: 0.02, warnDays: 1, durationDays: 12 },
  plague: {
    startDay: 60, minPop: 25, chanceBySeason: [0.010, 0.015, 0.015, 0.005],
    warnDays: 2, durationDays: 14, cooldownDays: 40, mendingFrac: 0.2,
  },
  raid: {
    firstDay: 26, gapMin: 24, gapMax: 34, strengthBase: 2, strengthEvery: 40, strengthMax: 8,
    towerDefence: 2, towerMax: 4, barracksDefence: 3, barracksMax: 2,
    lootPerUnmet: 0.15, lootMax: 0.45, lootKinds: ['food', 'wood', 'stone', 'goods', 'gold'],
    casualtiesPerUnmet: 2,
    warnWithTower: 2, warnWithout: 4, winDays: 5, lossDays: 7,
  },
  festival: { cost: { gold: 30, food: 20 }, durationDays: 4, happy: 10, cooldownDays: 8 },
  harvestFair: { season: 2, dayOfSeason: 5, durationDays: 3, happy: 5 },
};
