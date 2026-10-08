// owner: foundation
// Section 5.10: map generation numbers. guarantees.meadowRadius, forestRadius and stoneRadius are the
// radii named in the key names of section 5.10 (9, 12, 12), kept here so no radius is hard-coded in code.

export const MAP = {
  width: 64, height: 64,
  hall: { x: 32, y: 32 }, hallSize: 3,
  door: { x: 32, y: 34 },
  starterRoad: [{ x: 32, y: 34 }, { x: 32, y: 35 }],
  exploredRadius: 14,
  elevation: { cells: [16, 8, 4], weights: [0.6, 0.3, 0.1], bowl: 0.28 },
  mountainAt: 0.56, hillAt: 0.46, edgeWidth: 2,
  hallPlatform: { radius: 3, height: 0.36 },
  meadow: { cell: 6, min: 0.56 }, forest: { cell: 5, min: 0.60 },
  stone: { cell: 4, min: 0.66 }, iron: { cell: 4, min: 0.70, minX: 42 },
  river: { startX: 40, minX: 38, maxX: 43, width: 1 },
  lake: { x: 20, y: 46, radius: 4 },
  guarantees: {
    meadowWithin9: 30, forestWithin12: 12, stoneWithin12: 6,
    ironMinDist: 10, ironMaxDist: 20, ironCount: 4,
    meadowRadius: 9, forestRadius: 12, stoneRadius: 12,
  },
  timber: { min: 100, max: 140 }, stoneDeposit: 150, ironDeposit: 100,
  attempts: 40,
};
