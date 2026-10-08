// owner: foundation
// Section 5.3: resources, base prices and starting stock. Key order is the order used everywhere (costs, stock, saves).

export const RESOURCES = {
  food: { key: 'food', name: 'Food', base: 3, tradable: true, start: 300 },
  wood: { key: 'wood', name: 'Wood', base: 3, tradable: true, start: 300 },
  stone: { key: 'stone', name: 'Stone', base: 4, tradable: true, start: 200 },
  iron: { key: 'iron', name: 'Iron', base: 8, tradable: true, start: 30 },
  goods: { key: 'goods', name: 'Goods', base: 12, tradable: true, start: 20 },
  gold: { key: 'gold', name: 'Gold', base: 1, tradable: false, start: 150 },
};

export const RESOURCE_KEYS = ['food', 'wood', 'stone', 'iron', 'goods', 'gold'];

export const TRADE_KEYS = ['food', 'wood', 'stone', 'iron', 'goods'];
