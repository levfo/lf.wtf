// owner: ui-shell
// Toast messages in #toasts (ARCHITECTURE 9.5). At most four show. A click dismisses one.
// A repeat of the same text within REPEAT_MS adds an "x2" badge instead of a new toast. A bad toast about a raid, famine,
// plague, fire, flood or a death stays until it is clicked and never folds into a count. The controller passes only the
// kind and the text, so the text names the event (the sim's wording, ARCHITECTURE 7.9). A caller may also pass Infinity.

const MAX_VISIBLE = 4;
const REPEAT_MS = 10000;
const TTL_MS = { good: 5000, info: 5000, warn: 5000, bad: 6000 };
const ICON = { good: '✓', info: 'i', warn: '!', bad: '✕' };
const WORD = { good: 'Done', info: 'Note', warn: 'Warning', bad: 'Problem' };
// Raid ("Raid! ..."), famine ("The valley went hungry", "Hunger took"), plague, fire ("A fire destroyed a home",
// "... burned down"), flood ("The river flooded"), and deaths ("... died.", "Natural causes took").
const STICKY_BAD = /^Raid\b|went hungry|^Hunger took|plague|\bfire\b|burned down|flood|\b(died|took)\b/i;

export function mountToasts(ctx) {
  const doc = ctx.doc;
  const box = ctx.els['toasts'];
  const live = [];

  function dismiss(item) {
    const i = live.indexOf(item);
    if (i < 0) return;
    live.splice(i, 1);
    clearTimeout(item.timer);
    item.el.remove();
  }

  // A lifetime that is not finite (a sticky toast) sets no timer, so it stays until clicked.
  function arm(item, ms) {
    clearTimeout(item.timer);
    item.timer = Number.isFinite(ms) ? setTimeout(() => dismiss(item), ms) : 0;
  }

  function label(item) {
    const count = item.count > 1 ? ' (x' + item.count + ')' : '';
    return WORD[item.kind] + ': ' + item.text + count + '. Click to dismiss.';
  }

  // kind: good, info, warn or bad (anything else counts as info). ttlMs overrides the default lifetime.
  function show(kind, text, ttlMs) {
    const k = Object.prototype.hasOwnProperty.call(TTL_MS, kind) ? kind : 'info';
    const msg = text == null ? '' : String(text).trim();
    if (msg === '') return;
    const now = Date.now();
    const sticky = k === 'bad' && STICKY_BAD.test(msg);
    const ms = sticky ? Infinity : ttlMs > 0 ? ttlMs : TTL_MS[k];
    const again = sticky ? undefined : live.find((t) => t.kind === k && t.text === msg && now - t.at <= REPEAT_MS);
    if (again) {
      again.count += 1;
      again.at = now;
      again.badge.textContent = 'x' + again.count;
      again.badge.hidden = false;
      again.el.setAttribute('aria-label', label(again));
      arm(again, ms);
      return;
    }
    const el = doc.createElement('button');
    el.type = 'button';
    el.className = 'toast toast-' + k;
    el.title = 'Click to dismiss';
    const icon = doc.createElement('span');
    icon.className = 'toast-icon';
    icon.setAttribute('aria-hidden', 'true');
    icon.textContent = ICON[k];
    const body = doc.createElement('span');
    body.className = 'toast-text';
    body.textContent = msg;
    const badge = doc.createElement('span');
    badge.className = 'toast-count';
    badge.hidden = true;
    el.append(icon, body, badge);
    const item = { el, kind: k, text: msg, count: 1, at: now, badge, timer: 0, sticky };
    el.setAttribute('aria-label', label(item));
    el.addEventListener('click', () => dismiss(item));
    live.push(item);
    box.append(el);
    // Over the limit, the oldest toast that can go is dismissed first: a sticky one only when nothing else is showing.
    while (live.length > MAX_VISIBLE) dismiss(live.find((t) => !t.sticky) || live[0]);
    arm(item, ms);
  }

  return { show };
}
