// owner: foundation
// Section 5.4 (ECONOMY and seasonal factors) and section 5.5 (UPGRADES).

export const ECONOMY = {
  capBase: 500, capPerStorehouse: 200, maxStorehouses: 4,
  granaryFoodCap: 600, maxGranaries: 2,
  spoilAbove: 250, spoilRate: 0.02,
  priceReversion: 0.25, priceMin: 0.4, priceMax: 2.5,
  scarcityBase: 1.5, scarcitySlope: 1.2, scarcityMin: 0.5, scarcityMax: 1.5,
  eventFactor: { drought: { food: 1.3 } },
  buyMarkup: 1.15, sellMarkdown: 0.85,
  tradeLimitPerDay: 50,
  caravanFirstDays: 6,
  caravanGapMin: 10, caravanGapMax: 16,
  caravanOfferDays: 6,
  caravanAmounts: [10, 20, 30],
  caravanSellFactor: 0.75,
  caravanBuyFactor: 1.3,
  caravanMinPop: 10,
  taxBase: { adult: 0.45, elder: 0.2 },
  taxRates: { low: 0.6, normal: 1.0, high: 1.5 },
  haulFree: 5, haulPerStep: 0.015, haulFloor: 0.6,
  demolishRefund: 0.5,
  buildersPerSite: 2,
  scoutCost: 5, scoutRange: 10, scoutRevealRadius: 4,
  maxRoadPoints: 60,
  foodWarnCoverDays: 10, foodWarnEvery: 10,
  winterNeedDays: 12,
  floodFarmFactor: 0.5, floodRiverRadius: 3, floodBridgeWashChance: 0.3,
  droughtFarmFactor: 0.6,
  outdoorTypes: ['farm', 'fishery', 'lumberCamp', 'quarry', 'mine'],
  seasonFactors: {
    farm: [1.0, 1.0, 1.2, 0.6], fishery: [1, 1, 1, 0.5], lumberCamp: [1, 1, 1, 0.6],
    quarry: [1, 1, 1, 1], mine: [1, 1, 1, 0.7], workshop: [1, 1, 1, 1],
  },
  weatherFactors: { rain: { farm: 1.1 }, storm: { outdoor: 0.5 }, snow: { outdoor: 0.8 } },
  priceSeason: {
    food: [1.0, 1.0, 0.85, 1.25], wood: [1, 1, 1, 1.1], stone: [1, 1, 1, 1],
    iron: [1, 1, 1, 1], goods: [1, 1, 1.1, 1],
  },
};

export const UPGRADES = {
  cropRotation: {
    key: 'cropRotation', name: 'Crop Rotation', cost: { gold: 60, goods: 10 }, tier: 1,
    target: 'farm', factor: 1.15, text: 'Farms yield 15% more.',
  },
  forestry: {
    key: 'forestry', name: 'Forestry', cost: { gold: 50, iron: 10 }, tier: 1,
    target: 'lumberCamp', factor: 1.2, text: 'Lumber camps yield 20% more.',
  },
  deepShafts: {
    key: 'deepShafts', name: 'Deep Shafts', cost: { gold: 80, stone: 30, iron: 20 }, tier: 2,
    target: 'mine', factor: 1.25, text: 'Mines yield 25% more.',
  },
};
