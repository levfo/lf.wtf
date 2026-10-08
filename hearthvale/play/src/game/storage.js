// owner: app
// Section 9.10 and section 10.1: every browser storage read and write goes through here. Each call returns
// {ok, value?, reason?} and never throws. A blocked or full store gives the player-facing reason; the game keeps running.
// R2-01: two saves. The latest save is the newest write, from autosave or from a manual save (which also becomes the
// latest), so Continue reads it. The manual save has its own key, so autosave never overwrites it, and Load reads it.

const SAVE_KEY = 'hearthvale.save';            // the latest save: the newest write, autosave or manual
const PREV_KEY = 'hearthvale.save.prev';       // the latest save before the last write
const MANUAL_KEY = 'hearthvale.save.manual';   // the last manual save (Save button, Ctrl+S, pause menu)
const SETTINGS_KEY = 'hearthvale.settings';
const DEFAULTS = Object.freeze({ sound: true, debugLine: false });
const BLOCKED = 'Browser storage is blocked, so this kingdom cannot be saved. The game keeps running.';
const FULL = 'Browser storage is full. Free some space and try again.';

// Keeps only the known settings keys with the right types, so a damaged value falls back to the defaults.
const known = (obj) => {
  const out = {};
  if (obj && typeof obj.sound === 'boolean') out.sound = obj.sound;
  if (obj && typeof obj.debugLine === 'boolean') out.debugLine = obj.debugLine;
  return out;
};

const reasonOf = (err) => (err && (['QuotaExceededError', 'NS_ERROR_DOM_QUOTA_REACHED'].includes(err.name)
  || err.code === 22 || err.code === 1014) ? FULL : BLOCKED);

// win: the window (anything with a localStorage property). The store is null when the browser blocks it.
export function createStorage(win) {
  const store = () => {
    try {
      return win && win.localStorage ? win.localStorage : null;
    } catch (err) {
      return null;
    }
  };

  // {ok: true, value} when present; {ok: false, reason: null} when absent; {ok: false, reason} when blocked.
  function read(key) {
    const s = store();
    if (!s) return { ok: false, reason: BLOCKED };
    try {
      const value = s.getItem(key);
      return value === null ? { ok: false, reason: null } : { ok: true, value };
    } catch (err) {
      return { ok: false, reason: reasonOf(err) };
    }
  }

  // Always returns a value: the defaults when nothing is stored or the store is blocked.
  function readSettings() {
    const r = read(SETTINGS_KEY);
    if (!r.ok && r.reason) return { ok: false, reason: r.reason, value: { ...DEFAULTS } };
    let parsed = {};
    try {
      if (r.ok) parsed = known(JSON.parse(r.value));
    } catch (err) {
      parsed = {};
    }
    return { ok: true, value: { ...DEFAULTS, ...parsed } };
  }

  // The latest save moves to the previous slot first, so one failed write never loses the last good save.
  function writeLatest(text) {
    const s = store();
    if (!s) return { ok: false, reason: BLOCKED };
    try {
      const old = s.getItem(SAVE_KEY);
      if (old !== null) s.setItem(PREV_KEY, old);
      s.setItem(SAVE_KEY, String(text));
      return { ok: true };
    } catch (err) {
      return { ok: false, reason: reasonOf(err) };
    }
  }

  return {
    readSave: () => read(SAVE_KEY),
    readPrev: () => read(PREV_KEY),
    readManual: () => read(MANUAL_KEY),
    readSettings,

    // Autosave (R2-01): writes the latest save only. The manual save is not touched.
    writeSave: (text) => writeLatest(text),

    // Manual save (R2-01): its own slot first, so a failed first write changes nothing. The latest save follows, so
    // Continue finds the manual save too.
    writeManual(text) {
      const s = store();
      if (!s) return { ok: false, reason: BLOCKED };
      try {
        s.setItem(MANUAL_KEY, String(text));
      } catch (err) {
        return { ok: false, reason: reasonOf(err) };
      }
      return writeLatest(text);
    },

    // Merges obj into the stored settings, so the sound and debug writes never overwrite each other.
    writeSettings(obj) {
      const s = store();
      if (!s) return { ok: false, reason: BLOCKED };
      try {
        const next = { ...readSettings().value, ...known(obj) };
        s.setItem(SETTINGS_KEY, JSON.stringify(next));
        return { ok: true, value: next };
      } catch (err) {
        return { ok: false, reason: reasonOf(err) };
      }
    },
  };
}
