// owner: foundation
// Section 3.5 and section 10: save format, deterministic serialization, base64 codecs and SaveError.
import { createEmptyState, ensureRuntime, validateState, STAT_KEYS } from './state.js';
import { refreshNetwork } from './world.js';

export const SAVE_VERSION = 1;
export const SAVE_FORMAT = 'hearthvale-save';
const CORRUPT_TEXT = 'That save file is damaged and cannot be loaded.';

export class SaveError extends Error {
  constructor(code, message) {
    super(message);
    this.name = 'SaveError';
    this.code = code;
  }
}

const corrupt = () => new SaveError('CORRUPT', CORRUPT_TEXT);
const isObj = (v) => v !== null && typeof v === 'object' && !Array.isArray(v);
const val = (v, d) => (v === undefined ? d : v);
// Version migrations, applied in order from the file's version up to SAVE_VERSION. Version 1 has none.
export const MIGRATIONS = {};

const RES = ['food', 'wood', 'stone', 'iron', 'goods', 'gold'];
const TRADE = ['food', 'wood', 'stone', 'iron', 'goods'];
const CARRY = ['food', 'goods', 'fuel', 'tax', 'upkeep'];
const SCHEDULE = ['raidDay', 'raidStrength', 'raidWarnedDay', 'plagueStart', 'plagueUntil', 'plagueNextAllowed',
  'plaguePopStart', 'plagueDeathBase', 'floodStart', 'droughtStart', 'goldenDays', 'plagueMendingDay', 'foodWarnDay', 'lastDefence'];
const UPGRADE_KEYS = ['cropRotation', 'forestry', 'deepShafts'];
const TUTORIAL = ['step', 'done', 'skipped', 'tradeDone'];
const FLAGS = ['famine', 'cold', 'debt', 'fedFrac'];
const BUILDING = ['id', 'type', 'x', 'y', 'rot', 'w', 'h', 'stage', 'progress', 'builders', 'stalled', 'priority',
  'crew', 'acc', 'cooldown', 'connected', 'roadSteps', 'createdDay', 'lastHarvestDay'];
const CITIZEN = ['id', 'name', 'ageDays', 'homeId', 'workId', 'militia'];

// Copies the listed keys in the listed order, so the text never depends on insertion order.
const pick = (src, keys) => Object.fromEntries(keys.map((k) => [k, src[k]]));
const ledgerRec = (l) => ({
  produced: pick(l.produced, RES), consumed: pick(l.consumed, RES), lost: pick(l.lost, RES),
  ...pick(l, ['tax', 'upkeepDue', 'upkeepPaid', 'born', 'died', 'arrived']),
});

// Deterministic JSON text: the same state always gives the same text, and no timestamps are written.
export function serializeState(state) {
  const s = state;
  const milestones = Object.fromEntries(Object.keys(s.milestones).sort().map((k) => [k, s.milestones[k]]));
  const map = {};
  for (const k of ['terrain', 'height', 'deposit', 'road', 'building', 'explored']) map[k] = encodeBytes(s.map[k]);
  return JSON.stringify({
    format: SAVE_FORMAT,
    saveVersion: SAVE_VERSION,
    state: {
      version: s.version, seed: s.seed, rng: s.rng, width: s.width, height: s.height, day: s.day, map,
      buildings: s.buildings.map((b) => pick(b, BUILDING)),
      citizens: s.citizens.map((c) => pick(c, CITIZEN)),
      nextBuildingId: s.nextBuildingId, nextCitizenId: s.nextCitizenId, nextOfferId: s.nextOfferId, nextEffectId: s.nextEffectId,
      stock: pick(s.stock, RES), carry: pick(s.carry, CARRY), price: pick(s.price, TRADE),
      priceTarget: pick(s.priceTarget, TRADE), tradedToday: pick(s.tradedToday, TRADE), tradeDay: s.tradeDay,
      ledger: ledgerRec(s.ledger), lastLedger: ledgerRec(s.lastLedger),
      policies: pick(s.policies, ['tax', 'rations', 'draftRate']), weather: pick(s.weather, ['kind', 'untilDay']),
      effects: s.effects.map((e) => pick(e, ['id', 'kind', 'until', 'value'])),
      offers: s.offers.map((o) => pick(o, ['id', 'kind', 'resource', 'amount', 'unitPrice', 'expires'])),
      nextCaravanDay: s.nextCaravanDay, schedule: pick(s.schedule, SCHEDULE),
      happiness: s.happiness, happinessTarget: s.happinessTarget,
      happinessCauses: s.happinessCauses.map((c) => pick(c, ['key', 'label', 'value', 'detail'])),
      exodusDays: s.exodusDays, tier: s.tier, tierDay: s.tierDay, tutorial: pick(s.tutorial, TUTORIAL), tutorialBaseline: s.tutorialBaseline, milestones,
      festivalDay: s.festivalDay, flags: pick(s.flags, FLAGS), upgrades: pick(s.upgrades, UPGRADE_KEYS),
      stats: pick(s.stats, STAT_KEYS), lastOverflow: pick(s.lastOverflow, RES),
      log: s.log.map((l) => pick(l, ['day', 'kind', 'text'])),
      outcome: {
        status: s.outcome.status, reason: s.outcome.reason, day: s.outcome.day,
        causes: s.outcome.causes.map((c) => pick(c, ['key', 'label', 'value'])),
      },
    },
  });
}

// Loads a save: JSON, format, version, migrations, rebuild, runtime, network and validation.
export function deserializeState(text) {
  let doc;
  try {
    doc = JSON.parse(text);
  } catch (e) {
    throw corrupt();
  }
  if (!isObj(doc) || doc.format !== SAVE_FORMAT) throw new SaveError('FORMAT', 'That is not a Hearthvale save.');
  const ver = doc.saveVersion;
  if (!Number.isInteger(ver) || ver < 1) throw corrupt();
  if (ver > SAVE_VERSION) {
    throw new SaveError('VERSION', `Save is from a newer version (${ver}). This build reads version ${SAVE_VERSION}.`);
  }
  let plain = doc.state;
  for (let v = ver; v < SAVE_VERSION; v += 1) {
    if (typeof MIGRATIONS[v] !== 'function') throw corrupt();
    plain = MIGRATIONS[v](plain);
  }
  return rebuild(plain);
}

// Fills a missing field with its default: objects merge key by key; arrays and scalars are taken as they are.
function fillDeep(src, def) {
  if (src === undefined) return def;
  if (!isObj(def) || !isObj(src)) return src;
  return Object.fromEntries(Object.keys(def).map((k) => [k, fillDeep(src[k], def[k])]));
}

function rebuild(p) {
  try {
    if (!isObj(p) || !Number.isInteger(p.seed)) throw corrupt();
    const W = p.width;
    const H = p.height;
    if (!Number.isInteger(W) || !Number.isInteger(H) || W < 1 || H < 1 || !isObj(p.map)) throw corrupt();
    const base = createEmptyState({ seed: p.seed, width: W, height: H });
    const n = W * H;
    const dec = (k, C) => (p.map[k] === undefined ? new C(n) : decodeBytes(p.map[k], C, n));
    const s = {
      version: SAVE_VERSION, seed: p.seed, rng: val(p.rng, base.rng), width: W, height: H, day: val(p.day, 0),
      map: {
        terrain: dec('terrain', Uint8Array), height: dec('height', Uint8Array), deposit: dec('deposit', Uint16Array),
        road: dec('road', Uint8Array), building: dec('building', Uint16Array), explored: dec('explored', Uint8Array),
      },
      buildings: Array.isArray(p.buildings) ? p.buildings.map((r) => pick(r, BUILDING)) : [],
      citizens: Array.isArray(p.citizens) ? p.citizens.map((r) => pick(r, CITIZEN)) : [],
      nextBuildingId: val(p.nextBuildingId, base.nextBuildingId), nextCitizenId: val(p.nextCitizenId, base.nextCitizenId),
      nextOfferId: val(p.nextOfferId, base.nextOfferId), nextEffectId: val(p.nextEffectId, base.nextEffectId),
      stock: fillDeep(p.stock, base.stock), carry: fillDeep(p.carry, base.carry), price: fillDeep(p.price, base.price),
      priceTarget: fillDeep(p.priceTarget, base.priceTarget), tradedToday: fillDeep(p.tradedToday, base.tradedToday),
      tradeDay: val(p.tradeDay, base.tradeDay), ledger: fillDeep(p.ledger, base.ledger),
      lastLedger: fillDeep(p.lastLedger, base.lastLedger), policies: fillDeep(p.policies, base.policies),
      weather: fillDeep(p.weather, base.weather), effects: val(p.effects, base.effects), offers: val(p.offers, base.offers),
      // R2-08: schedule fills key by key from createEmptyState, so a save without schedule.lastDefence reads 0 (10.6).
      nextCaravanDay: val(p.nextCaravanDay, base.nextCaravanDay), schedule: fillDeep(p.schedule, base.schedule),
      happiness: val(p.happiness, base.happiness), happinessTarget: val(p.happinessTarget, base.happinessTarget),
      happinessCauses: val(p.happinessCauses, base.happinessCauses), exodusDays: val(p.exodusDays, base.exodusDays),
      tier: val(p.tier, base.tier), tierDay: val(p.tierDay, base.tierDay), tutorial: fillDeep(p.tutorial, base.tutorial),
      tutorialBaseline: val(p.tutorialBaseline, base.tutorialBaseline),
      milestones: isObj(p.milestones) ? { ...p.milestones } : base.milestones,
      festivalDay: val(p.festivalDay, base.festivalDay), flags: fillDeep(p.flags, base.flags),
      upgrades: fillDeep(p.upgrades, base.upgrades), stats: fillDeep(p.stats, base.stats),
      lastOverflow: fillDeep(p.lastOverflow, base.lastOverflow), log: val(p.log, base.log),
      outcome: fillDeep(p.outcome, base.outcome),
    };
    ensureRuntime(s);
    refreshNetwork(s);
    if (validateState(s).length > 0) throw corrupt();
    return s;
  } catch (e) {
    if (e instanceof SaveError) throw e;
    throw corrupt();
  }
}

const B64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';

function toBase64(raw) {
  let out = '';
  for (let i = 0; i < raw.length; i += 3) {
    const b = i + 1 < raw.length ? raw[i + 1] : 0;
    const c = i + 2 < raw.length ? raw[i + 2] : 0;
    const k = (raw[i] << 16) | (b << 8) | c;
    out += B64[(k >> 18) & 63] + B64[(k >> 12) & 63]
      + (i + 1 < raw.length ? B64[(k >> 6) & 63] : '=') + (i + 2 < raw.length ? B64[k & 63] : '=');
  }
  return out;
}

function fromBase64(text) {
  if (typeof text !== 'string' || text.length % 4 !== 0 || !/^[A-Za-z0-9+/]*={0,2}$/.test(text)) throw corrupt();
  const out = new Uint8Array((text.length / 4) * 3 - (text.endsWith('==') ? 2 : (text.endsWith('=') ? 1 : 0)));
  let o = 0;
  for (let i = 0; i < text.length; i += 4) {
    const v = [0, 1, 2, 3].map((j) => (text[i + j] === '=' ? 0 : B64.indexOf(text[i + j])));
    const k = (v[0] << 18) | (v[1] << 12) | (v[2] << 6) | v[3];
    for (const byte of [(k >> 16) & 255, (k >> 8) & 255, k & 255]) {
      if (o < out.length) out[o++] = byte;
    }
  }
  return out;
}

// Standard base64 of the little-endian bytes of a Uint8Array or Uint16Array. Explicit byte split, no views.
export function encodeBytes(bytes) {
  const wide = bytes instanceof Uint16Array;
  const raw = new Uint8Array(wide ? bytes.length * 2 : bytes.length);
  for (let i = 0; i < bytes.length; i += 1) {
    if (wide) {
      raw[2 * i] = bytes[i] & 255;
      raw[2 * i + 1] = (bytes[i] >> 8) & 255;
    } else {
      raw[i] = bytes[i] & 255;
    }
  }
  return toBase64(raw);
}

// Reverse of encodeBytes. Ctor is Uint8Array or Uint16Array. When expected is given, the length must match.
export function decodeBytes(text, Ctor, expected) {
  const raw = fromBase64(text);
  let out;
  if (Ctor === Uint16Array) {
    if (raw.length % 2 !== 0) throw corrupt();
    out = new Uint16Array(raw.length / 2);
    for (let i = 0; i < out.length; i += 1) out[i] = raw[2 * i] | (raw[2 * i + 1] << 8);
  } else if (Ctor === Uint8Array) {
    out = raw;
  } else {
    throw new TypeError('decodeBytes expects Uint8Array or Uint16Array');
  }
  if (expected !== undefined && out.length !== expected) throw corrupt();
  return out;
}
