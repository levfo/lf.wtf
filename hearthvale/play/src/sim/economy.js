// owner: economy
// Section 3.6 exports, plus the daily steps 8.2 (construction), 8.3 (production), spoilage (8), finance (10) and prices (11).
// Consumption (8.4) is population.js (section 3.7). Pure: no page, clock, random source or forbidden Math functions.
import { CONFIG, TIME } from '../config/index.js';
import { ECONOMY, UPGRADES } from '../config/economy.js';
import { BUILDINGS } from '../config/buildings.js';
import { RESOURCES, RESOURCE_KEYS, TRADE_KEYS } from '../config/resources.js';
import { TERRAIN, emit, ensureRuntime, idx, inBounds } from './state.js';
import { footprintOf, resourceTilesNear } from './world.js';

// Contract numbers with no key in src/config (sections 3.6, 4.3, 5.4, 5.8, 8.2). Reported in contractDeviations.
const OVERFLOW_WARN_DAYS = 3;   // 3.6: one overflow warning per resource in this many days
const STALL_DAYS = 2;           // 8.2: a site warns once it has gone this many days with no builder
const STALL_WARN_EVERY = 3;     // 8.2: stall warnings fall only on days divisible by this
const TREND_UP = 1.02;          // 5.4: trend is 'up' when the target is above price x 1.02
const TREND_DOWN = 0.98;        // 5.4: trend is 'down' when the target is below price x 0.98
const FERTILITY = { meadow: 1, grass: 0.6 };   // 3.6 and 4.3: fertility of one farm tile
const TUTORIAL_WOOD_SALE = 10;  // 5.8 step 5: selling this much wood or more sets tutorial.tradeDone
// Extracting buildings draw from one terrain; a tile that runs dry becomes the terrain in DEPLETED (4.3).
const RES_TERRAIN = { forest: TERRAIN.FOREST, stone: TERRAIN.STONE, iron: TERRAIN.IRON };
const DEPLETED = { forest: TERRAIN.GRASS, stone: TERRAIN.GRASS, iron: TERRAIN.HILL };

const byId = (a, b) => a.id - b.id;
const clamp = (v, lo, hi) => Math.min(hi, Math.max(lo, v));
const lname = (r) => RESOURCES[r].name.toLowerCase();
const seasonOf = (day) => Math.floor((day % TIME.daysPerYear) / TIME.daysPerSeason);
const effectActive = (state, kind) => state.effects.some((e) => e.kind === kind && e.until > state.day);
const completeOf = (state, type) => state.buildings.filter((b) => b.type === type && b.stage === 'complete');
// Cohort boundaries from config (section 5.6): child under 12 years, elder from 60, adult in between.
const cohortAt = (ageDays) => {
  if (ageDays < CONFIG.population.childUntilYears * TIME.daysPerYear) return 'child';
  if (ageDays >= CONFIG.population.elderFromYears * TIME.daysPerYear) return 'elder';
  return 'adult';
};
// Adds a sim event and its log line. Callers without an events list still get the log line.
const note = (state, events, ev) => emit(state, events || [], ev);

// Stock cap for any resource (5.4): base, plus 200 per complete Storehouse (max 4), plus 200 food per Granary (max 2).
export function storageCap(state, resource) {
  let cap = ECONOMY.capBase + ECONOMY.capPerStorehouse * Math.min(ECONOMY.maxStorehouses, completeOf(state, 'storehouse').length);
  if (resource === 'food') cap += ECONOMY.granaryFoodCap * Math.min(ECONOMY.maxGranaries, completeOf(state, 'granary').length);
  return cap;
}

// Books lost stock and warns at most once per resource every OVERFLOW_WARN_DAYS days (lastOverflow).
function loseStock(state, events, resource, lost) {
  state.ledger.lost[resource] += lost;
  state.stats.overflow += lost;
  if (state.day - state.lastOverflow[resource] >= OVERFLOW_WARN_DAYS) {
    state.lastOverflow[resource] = state.day;
    note(state, events, {
      type: 'overflow', kind: 'warn', amount: lost, resource,
      text: `Storage full: ${lost} ${lname(resource)} lost. Build a Storehouse for more room.`,
    });
  }
}

// Adds whole units up to the cap; the excess is lost. Returns the amount actually added.
export function stockAdd(state, resource, amount, events) {
  if (!RESOURCE_KEYS.includes(resource) || !(amount > 0)) return 0;
  const want = Math.floor(amount);
  const room = Math.max(0, storageCap(state, resource) - state.stock[resource]);
  const added = Math.min(want, room);
  state.stock[resource] += added;
  if (want > added) loseStock(state, events, resource, want - added);
  return added;
}

// Null when every resource in the cost is in stock; else the reason for the first short resource in key order.
export function canAfford(state, cost) {
  for (const r of RESOURCE_KEYS) {
    const need = (cost && cost[r]) || 0;
    if (need > 0 && state.stock[r] < need) return `Not enough ${lname(r)}: need ${need}, have ${state.stock[r]}`;
  }
  return null;
}

// Deducts a cost when it is affordable. Returns the refusal reason, or null after spending.
export function spend(state, cost) {
  const reason = canAfford(state, cost);
  if (reason !== null) return reason;
  for (const r of RESOURCE_KEYS) state.stock[r] -= (cost && cost[r]) || 0;
  return null;
}

// Gives back floor(cost x fraction) of each resource, never past the cap.
export function refund(state, cost, fraction) {
  for (const r of RESOURCE_KEYS) {
    const add = Math.floor(((cost && cost[r]) || 0) * fraction);
    if (add > 0) state.stock[r] += Math.min(add, Math.max(0, storageCap(state, r) - state.stock[r]));
  }
}

// Output factor for road distance from the Town Hall door (4.3): full to 5 steps, 1.5% less per extra step, floor 0.6.
export function haulFactor(steps) {
  if (!(steps >= 0)) return 0;
  return clamp(1 - ECONOMY.haulPerStep * Math.max(0, steps - ECONOMY.haulFree), ECONOMY.haulFloor, 1);
}

// Season factor from the table in 5.4; 1 for types that have no row.
export function seasonFactor(type, season) {
  const row = ECONOMY.seasonFactors[type];
  const v = row ? row[season] : undefined;
  return v === undefined ? 1 : v;
}

// Weather factor for a building type (5.4): rain has a farm row; storm and snow apply to outdoor types.
export function weatherFactor(kind, type) {
  const table = ECONOMY.weatherFactors[kind];
  if (!table) return 1;
  if (table[type] !== undefined) return table[type];
  if (table.outdoor !== undefined && ECONOMY.outdoorTypes.includes(type)) return table.outdoor;
  return 1;
}

// Product of the factors of bought upgrades that target this building type (5.5).
export function upgradeFactor(state, type) {
  let f = 1;
  for (const key of Object.keys(UPGRADES)) {
    if (UPGRADES[key].target === type && state.upgrades[key] === true) f *= UPGRADES[key].factor;
  }
  return f;
}

// Average fertility of a farm's tiles: meadow counts 1.0, grass 0.6 (4.3).
export function farmFertility(state, tiles) {
  if (!tiles || tiles.length === 0) return 0;
  let meadow = 0;
  let grass = 0;
  for (const t of tiles) {
    const k = state.map.terrain[idx(state, t.x, t.y)];
    if (k === TERRAIN.MEADOW) meadow += 1;
    else if (k === TERRAIN.GRASS) grass += 1;
  }
  return (meadow * FERTILITY.meadow + grass * FERTILITY.grass) / tiles.length;
}

// Buy and sell prices from the stored price and target (5.4). Non-tradable resources quote zero.
export function quotePrice(state, resource) {
  const base = RESOURCES[resource] ? RESOURCES[resource].base : 0;
  if (!TRADE_KEYS.includes(resource)) return { buy: 0, sell: 0, trend: 'flat', target: base, base };
  const price = state.price[resource];
  const target = state.priceTarget[resource];
  let trend = 'flat';
  if (target > price * TREND_UP) trend = 'up';
  else if (target < price * TREND_DOWN) trend = 'down';
  return {
    buy: Math.ceil(price * ECONOMY.buyMarkup),
    sell: Math.max(1, Math.floor(price * ECONOMY.sellMarkdown)),
    trend, target, base,
  };
}

// The Market checks shared by trade and caravan deals (6.2): a complete Market, then one with a worker.
function marketReason(state) {
  const markets = completeOf(state, 'market');
  if (markets.length === 0) return 'Trading needs a complete Market';
  if (!markets.some((m) => m.crew > 0)) return 'The Market needs at least one worker';
  return null;
}

// Buys or sells up to the daily limit at the current quote (6.2 trade row).
export function applyTrade(state, resource, mode, amount) {
  const limit = ECONOMY.tradeLimitPerDay;
  if (!TRADE_KEYS.includes(resource)) return { ok: false, reason: 'You can only trade food, wood, stone, iron or goods' };
  if (mode !== 'buy' && mode !== 'sell') return { ok: false, reason: 'Choose buy or sell' };
  if (!Number.isInteger(amount) || amount < 1 || amount > limit) return { ok: false, reason: `Trade 1 to ${limit} at a time` };
  const marketWhy = marketReason(state);
  if (marketWhy !== null) return { ok: false, reason: marketWhy };
  const name = lname(resource);
  const used = state.tradeDay === state.day ? state.tradedToday[resource] : 0;
  if (used + amount > limit) return { ok: false, reason: `Daily trade limit reached for ${name} (${limit} a day)` };
  const q = quotePrice(state, resource);
  const stock = state.stock[resource];
  let message;
  if (mode === 'buy') {
    const cap = storageCap(state, resource);
    if (stock + amount > cap) return { ok: false, reason: `Storage full: ${name} has room for ${Math.max(0, cap - stock)}` };
    const cost = amount * q.buy;
    if (state.stock.gold < cost) return { ok: false, reason: `Not enough gold: need ${cost}, have ${state.stock.gold}` };
    state.stock.gold -= cost;
    state.stock[resource] += amount;
    state.stats.goldSpent += cost;
    message = `Bought ${amount} ${name} for ${cost} gold.`;
  } else {
    if (stock < amount) return { ok: false, reason: `Not enough ${name}: need ${amount}, have ${stock}` };
    const gain = amount * q.sell;
    state.stock[resource] -= amount;
    state.stats.goldEarned += stockAdd(state, 'gold', gain, []);
    if (resource === 'wood' && amount >= TUTORIAL_WOOD_SALE) state.tutorial.tradeDone = true;
    message = `Sold ${amount} ${name} for ${gain} gold.`;
  }
  if (state.tradeDay !== state.day) {
    for (const k of TRADE_KEYS) state.tradedToday[k] = 0;
    state.tradeDay = state.day;
  }
  state.tradedToday[resource] += amount;
  state.stats.tradedUnits += amount;
  return { ok: true, reason: null, message };
}

// Accepts an open caravan offer (6.2 acceptOffer row). The offer leaves the list on success.
export function applyCaravanDeal(state, offerId) {
  const offer = state.offers.find((o) => o.id === offerId);
  if (!offer || state.day >= offer.expires) return { ok: false, reason: 'That offer has expired' };
  const marketWhy = marketReason(state);
  if (marketWhy !== null) return { ok: false, reason: marketWhy };
  const r = offer.resource;
  const name = lname(r);
  const total = offer.amount * offer.unitPrice;
  const stock = state.stock[r];
  const cap = storageCap(state, r);
  let message;
  if (offer.kind === 'sell') {
    if (state.stock.gold < total) return { ok: false, reason: `Not enough gold: need ${total}, have ${state.stock.gold}` };
    if (stock + offer.amount > cap) return { ok: false, reason: `Storage full: ${name} has room for ${Math.max(0, cap - stock)}` };
    state.stock.gold -= total;
    state.stock[r] += offer.amount;
    state.stats.goldSpent += total;
    message = `Deal done: ${offer.amount} ${name} for ${total} gold.`;
  } else {
    if (stock < offer.amount) return { ok: false, reason: `Not enough ${name}: need ${offer.amount}, have ${stock}` };
    state.stock[r] -= offer.amount;
    state.stats.goldEarned += stockAdd(state, 'gold', total, []);
    message = `Sold ${offer.amount} ${name} to the caravan for ${total} gold.`;
  }
  state.stats.tradedUnits += offer.amount;
  state.offers.splice(state.offers.indexOf(offer), 1);
  return { ok: true, reason: null, message };
}

// Step 5 (8.2): unemployed eligible adults and Town Hall clerks build sites, two builders per site at most.
// Progress is kept as whole builder-days over days, so a 3-day site with 1 builder per day finishes on day 3.
export function constructionDay(state, events) {
  ensureRuntime(state);
  const hall = state.buildings.find((b) => b.type === 'townHall');
  const hallId = hall ? hall.id : 0;
  let builders = 0;
  for (const c of state.citizens) {
    if (c.workId === 0) {
      if (!c.militia && cohortAt(c.ageDays) === 'adult') builders += 1;
    } else if (c.workId === hallId) {
      builders += 1;
    }
  }
  const sites = state.buildings.filter((b) => b.stage === 'building').sort(byId);
  for (const site of sites) {
    const def = BUILDINGS[site.type];
    const use = Math.min(ECONOMY.buildersPerSite, builders);
    builders -= use;
    site.builders = use;
    if (use === 0) {
      site.stalled += 1;
      if (site.stalled >= STALL_DAYS && state.day % STALL_WARN_EVERY === 0) {
        note(state, events, {
          type: 'stall', kind: 'warn', id: site.id, x: site.x, y: site.y,
          text: `${def.name} has no builders. Set the Town Hall to Priority, or pause another building.`,
        });
      }
      continue;
    }
    site.stalled = 0;
    const days = Math.max(1, def.days);
    const units = Math.round(site.progress * days) + use;
    site.progress = Math.min(1, units / days);
    if (units >= days) {
      site.stage = 'complete';
      site.progress = 1;
      site.builders = 0;
      state.stats.built += 1;
      note(state, events, { type: 'buildingComplete', kind: 'good', id: site.id, x: site.x, y: site.y, text: `${def.name} finished.` });
    }
  }
  if (sites.length > 0) state.rev.buildings += 1;
}

// True when any tile lies within radius (square) of a river tile.
function nearRiver(state, tiles, radius) {
  return tiles.some((t) => {
    for (let y = t.y - radius; y <= t.y + radius; y += 1) {
      for (let x = t.x - radius; x <= t.x + radius; x += 1) {
        if (inBounds(state, x, y) && state.map.terrain[idx(state, x, y)] === TERRAIN.RIVER) return true;
      }
    }
    return false;
  });
}

// Lumber, quarry and mine output: draws whole units from the nearest deposit tiles in index order.
// Returns how many units came out of the ground.
function extract(state, b, def, tiles, events) {
  const res = def.produces.resource;
  const need = def.needs;
  const list = resourceTilesNear(state, tiles, need.radius, RES_TERRAIN[need.terrain]);
  const have = list.reduce((sum, i) => sum + state.map.deposit[i], 0);
  const n = Math.min(Math.floor(b.acc), have);
  let left = n;
  for (const i of list) {
    if (left === 0) break;
    const take = Math.min(left, state.map.deposit[i]);
    state.map.deposit[i] -= take;
    left -= take;
    if (state.map.deposit[i] === 0) state.map.terrain[i] = DEPLETED[need.terrain];
  }
  b.acc = Math.min(b.acc - n, 1);
  if (n > 0) {
    stockAdd(state, res, n, events);
    state.ledger.produced[res] += n;
    if (res === 'iron') state.stats.ironMined += n;
  }
  return n;
}

// Workshop batches, limited by the accumulator and by each input in stock (8.3). Outputs go through stockAdd.
function craft(state, b, recipe, events) {
  let batches = Math.floor(b.acc);
  for (const k of Object.keys(recipe.in)) batches = Math.min(batches, Math.floor(state.stock[k] / recipe.in[k]));
  if (batches > 0) {
    for (const k of Object.keys(recipe.in)) {
      const used = recipe.in[k] * batches;
      state.stock[k] -= used;
      state.ledger.consumed[k] += used;
    }
    for (const k of Object.keys(recipe.out)) {
      const made = recipe.out[k] * batches;
      stockAdd(state, k, made, events);
      state.ledger.produced[k] += made;
      if (k === 'goods') state.stats.goodsMade += made;
    }
  }
  b.acc = Math.min(b.acc - batches, 1);
}

// Step 7 (8.3): every complete, connected, unpaused, staffed producer adds to its accumulator and pays out whole units.
export function productionDay(state, events) {
  ensureRuntime(state);
  const season = seasonOf(state.day);
  const drought = effectActive(state, 'drought');
  const flood = effectActive(state, 'flood');
  const producers = state.buildings
    .filter((b) => b.stage === 'complete' && b.connected && b.priority !== 'paused' && b.crew > 0)
    .sort(byId);
  let harvested = 0;
  let mapChanged = false;
  for (const b of producers) {
    const def = BUILDINGS[b.type];
    if (!def || (!def.produces && !def.recipe)) continue;
    const tiles = footprintOf(b.type, b.x, b.y, b.rot).tiles;
    let e = clamp(b.crew / def.crew, 0, 1) * haulFactor(b.roadSteps) * seasonFactor(b.type, season)
      * weatherFactor(state.weather.kind, b.type) * upgradeFactor(state, b.type);
    if (b.type === 'farm') {
      if (drought) e *= ECONOMY.droughtFarmFactor;
      if (flood && nearRiver(state, tiles, ECONOMY.floodRiverRadius)) e *= ECONOMY.floodFarmFactor;
    }
    if (def.recipe) {
      b.acc += def.recipe.batchesPerDay * e;
      craft(state, b, def.recipe, events);
    } else if (def.needs && def.needs.kind === 'terrain') {
      b.acc += def.produces.perDay * e;
      if (extract(state, b, def, tiles, events) > 0) mapChanged = true;
    } else {
      const fertility = b.type === 'farm' ? farmFertility(state, tiles) : 1;
      b.acc += def.produces.perDay * fertility * e;
      const res = def.produces.resource;
      const n = Math.floor(b.acc);
      if (n > 0) {
        stockAdd(state, res, n, events);
        state.ledger.produced[res] += n;
      }
      b.acc = Math.min(b.acc - n, 1);
      if (b.type === 'farm' && n > 0) {
        state.stats.harvested += n;
        b.lastHarvestDay = state.day;
        harvested += n;
      }
    }
  }
  if (harvested > 0) {
    note(state, events, { type: 'harvest', kind: 'good', amount: harvested, resource: 'food', text: `The harvest brought in ${harvested} food.` });
  }
  if (mapChanged) state.rev.map += 1;
}

// Gold upkeep owed each day: the sum over complete buildings, paused ones included (sections 4.2 and 4.5).
export function upkeepOwed(state) {
  let total = 0;
  for (const b of state.buildings) {
    const def = BUILDINGS[b.type];
    if (def && b.stage === 'complete') total += def.upkeep;
  }
  return total;
}

// Step 8: food above spoilAbove spoils unless a Granary stands. Stock above its cap (after a Storehouse is lost) is lost too.
export function spoilageDay(state, events) {
  ensureRuntime(state);
  if (completeOf(state, 'granary').length === 0) {
    const spoil = Math.floor(ECONOMY.spoilRate * Math.max(0, state.stock.food - ECONOMY.spoilAbove));
    if (spoil > 0) {
      state.stock.food -= spoil;
      state.ledger.lost.food += spoil;
    }
  }
  for (const r of RESOURCE_KEYS) {
    const cap = storageCap(state, r);
    if (state.stock[r] > cap) {
      const over = state.stock[r] - cap;
      state.stock[r] = cap;
      loseStock(state, events, r, over);
    }
  }
}

// Step 10: employed adults and elders pay tax (carry keeps the fraction); upkeep is paid from gold, and any shortfall is a debt day.
export function financeDay(state, events) {
  ensureRuntime(state);
  let owed = 0;
  for (const c of state.citizens) {
    if (c.workId === 0 || c.militia) continue;
    const k = cohortAt(c.ageDays);
    if (k === 'adult') owed += ECONOMY.taxBase.adult;
    else if (k === 'elder') owed += ECONOMY.taxBase.elder;
  }
  const taxed = state.carry.tax + owed * ECONOMY.taxRates[state.policies.tax];
  const taxWhole = Math.floor(taxed);
  state.carry.tax = taxed - taxWhole;
  if (taxWhole > 0) {
    state.ledger.tax += taxWhole;
    state.ledger.produced.gold += taxWhole;
    state.stats.goldEarned += stockAdd(state, 'gold', taxWhole, events);
  }
  const upkeep = state.carry.upkeep + upkeepOwed(state);
  const due = Math.floor(upkeep);
  state.carry.upkeep = upkeep - due;
  const paid = Math.min(state.stock.gold, due);
  state.stock.gold -= paid;
  state.ledger.upkeepDue += due;
  state.ledger.upkeepPaid += paid;
  state.ledger.consumed.gold += paid;
  if (due > paid) {
    state.flags.debt = true;
    state.stats.debtDays += 1;
    note(state, events, {
      type: 'debt', kind: 'warn', amount: due - paid, resource: 'gold',
      text: `Treasury short: ${due - paid} gold of upkeep was not paid.`,
    });
  }
}

// Step 11: each trade price moves 25% toward its target (base x scarcity x season x event), within 0.4 to 2.5 times base.
export function pricesDay(state) {
  const season = seasonOf(state.day);
  const drought = effectActive(state, 'drought');
  for (const r of TRADE_KEYS) {
    const base = RESOURCES[r].base;
    const ratio = state.stock[r] / storageCap(state, r);
    const scarcity = clamp(ECONOMY.scarcityBase - ECONOMY.scarcitySlope * ratio, ECONOMY.scarcityMin, ECONOMY.scarcityMax);
    let target = base * scarcity * ECONOMY.priceSeason[r][season];
    if (drought && ECONOMY.eventFactor.drought[r] !== undefined) target *= ECONOMY.eventFactor.drought[r];
    state.priceTarget[r] = target;
    const price = state.price[r] + (target - state.price[r]) * ECONOMY.priceReversion;
    state.price[r] = clamp(price, base * ECONOMY.priceMin, base * ECONOMY.priceMax);
  }
}
