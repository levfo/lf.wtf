// owner: foundation
// Section 5.6: population, happiness causes and first names.

export const POPULATION = {
  childUntilYears: 12, elderFromYears: 60, fertileMinYears: 18, fertileMaxYears: 39,
  startYears: { children: [2, 5, 8, 11], adults: [17, 20, 23, 26, 29, 32, 35, 38], elders: [62, 71] },
  foodPerCitizen: { child: 0.5, adult: 1.0, elder: 0.8 },
  rations: { half: 0.6, normal: 1.0, full: 1.25 },
  goodsPerCitizen: 0.05, fuelPerCitizenWinter: 0.1,
  hazardByYears: [[0, 11, 0], [12, 44, 0.002], [45, 59, 0.006], [60, 69, 0.06], [70, 79, 0.12], [80, 999, 0.22]],
  elderWinterFactor: 1.5,
  famineDeathRate: 0.03, famineVulnerableFactor: 1.5,
  plagueDeathRate: 0.008, plagueChildFactor: 1.5, plagueElderFactor: 2.0,
  plagueWellFactor: 0.6, plagueWellRadius: 4, plagueClinicFactor: 0.6,
  fireDeathChance: 0.15,
  birthBase: 0.012, birthSeason: [1.15, 1.0, 0.9, 0.7], birthCooldown: 60, birthPlagueFactor: 0.5,
  birthMood: [[30, 0.2], [50, 0.6], [70, 1.0], [Infinity, 1.4]],
  immigration: {
    minHappy: 45, perPoint: 0.02, max: 0.25, foodCoverDays: 6,
    groupWeights: [0.5, 0.85, 1.0], childChance: 0.2, adultYears: [18, 34], childYears: [3, 9],
  },
  emigration: { belowHappy: 35, base: 0.03 },
  exodus: { happy: 10, days: 30, warnDays: 15 },
  homelessMovePerDay: 4,
  militia: { recruitPerDay: 2, ironPerRecruit: 2, share: { off: 0, light: 0.10, full: 0.25 } },
  happiness: { start: 50, base: 50, smoothing: 0.25, min: 0, max: 100 },
  causes: {
    food: { wellFedDays: 3, wellFed: 6, shortMax: -12 },
    homes: { none: 3, perHomeless: -1.5, min: -10 },
    jobs: { lowRate: 0.10, midRate: 0.30, lowBonus: 2, perPoint: 40, min: -10 },
    rations: { half: -6, normal: 0, full: 3 },
    tax: { low: 4, normal: 0, high: -6 },
    amenity: { each: 3, max: 2 },
    goods: { plentyAt: 20, plenty: 3, shortBelow: 5, short: -3 },
    season: [0, 2, 1, -4],
    festival: 10, harvest: 5, plague: -8, raidWin: 3, raidLoss: -6, fireScare: -4, drought: -3,
    draft: { light: -2, full: -6 },
    cold: -8, debt: -5,
  },
};

export const NAMES = [
  'Ada', 'Bram', 'Cass', 'Dov', 'Elin', 'Fen', 'Gwen', 'Hal', 'Ines', 'Jory', 'Kit', 'Lark', 'Mara',
  'Nell', 'Oren', 'Pell', 'Quin', 'Rhea', 'Sol', 'Tamsin', 'Ulric', 'Vera', 'Wren', 'Yara', 'Zed',
  'Aldo', 'Bette', 'Cato', 'Dara', 'Edda', 'Fynn', 'Greta', 'Hugo', 'Iris', 'Jonah', 'Kasia', 'Leif',
  'Maren', 'Nico', 'Orla', 'Piers',
];
