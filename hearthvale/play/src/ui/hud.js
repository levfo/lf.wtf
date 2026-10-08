// owner: ui-shell
// Always-on HUD (ARCHITECTURE 9.5): top bar, status line under it, toolbar tools, camera pad, tool hint, debug line,
// controls strip and the data-tip tooltip. Reads views only and changes the game through the controller.
import { fmt, signed, plural, dateLabel } from './format.js';

const TIP_DELAY_MS = 400;
const STRIP_MS = 90000;
// The strip shows the standard hint on the title screen and while the Road or Build tool is on; otherwise it says how to
// turn the Road tool on. H is the Help key (input.js binds KeyH; the ? key is unbound).
const STRIP_TEXT = 'Drag: road. Right-drag: turn. Wheel: zoom. H Help: all keys.';
const STRIP_ROAD_TEXT = 'Click Road (or press R), then drag to lay roads.';
// Raid lines in kingdom.log: the warning ("Riders spotted: ...") and the result ("Raid repelled: ...", "Raid! ...").
const RAID_LOG = /^(Raid\b|Riders spotted)/;
const RES = ['food', 'wood', 'stone', 'iron', 'goods', 'gold'];
const RES_NAME = { food: 'Food', wood: 'Wood', stone: 'Stone', iron: 'Iron', goods: 'Goods', gold: 'Gold' };
const TOOL_BTN = { build: 'btn-build', road: 'btn-road', scout: 'btn-scout', demolish: 'btn-demolish' };
// A chip with no net figure yet (day 1: no day has ended) shows an em dash and no unit.
const NO_FIGURE = '—';
// Thresholds come from the view (foodWarnDays); this module imports no config (section 2.4). format.js is the exception.
const TREND_DAYS = 3;   // the happiness word compares today with this many days earlier
const TREND_EPS = 0.5;  // a change of half a point or less over that window reads as steady (the value shows whole points)

// Player-facing wording for the low-food fix, the Paused word and the full-stock tips (DESIGN 10). No numbers: the cap and
// the cover come from the view.
const LOW_FOOD_FIX = 'Build a Farm, or set Rations to Half (Kingdom > Policies).';
const PAUSED_TEXT = ' Paused';
const PAUSED_TIP = 'The clock is stopped. Space or a speed button starts it again.';
// What is lost while a stock stays at its cap.
const FULL_TIP = 'Full: while it stays at the cap, anything more that comes in is lost. ' +
  'Spend it, or build a Storehouse to raise the cap.';
const FULL_TIP_FOOD = 'Full: while it stays at the cap, food that comes in is lost. ' +
  'A Granary raises the food cap, and a Storehouse raises every cap.';

const dec1 = (v) => (Number.isFinite(Number(v)) ? Number(v).toFixed(1) : '0.0');
const digitsOf = (v) => (Number.isInteger(v) ? 0 : 1);
const causeText = (c) => c.label + ' ' + signed(c.value, digitsOf(c.value)) + (c.detail ? ': ' + c.detail : '');

// The largest happiness causes by size. Zero causes are left out; ties keep the order of the causes list.
function biggestCauses(causes, n) {
  if (!Array.isArray(causes)) return [];
  return causes
    .map((c, i) => ({ c, i }))
    .filter(({ c }) => c && typeof c.value === 'number' && c.value !== 0)
    .sort((a, b) => Math.abs(b.c.value) - Math.abs(a.c.value) || a.i - b.i)
    .slice(0, n)
    .map(({ c }) => c);
}

// The most negative happiness cause, or null when none is negative.
function worstCause(causes) {
  const negative = (Array.isArray(causes) ? causes : []).filter((c) => c && typeof c.value === 'number' && c.value < 0);
  return negative.reduce((worst, c) => (!worst || c.value < worst.value ? c : worst), null);
}

// The food cover in days, or null when there is no figure. coverDays is null when food income covers use (R2-03). The null
// check comes before Number(), because Number(null) is 0 and would read as no food at all.
function coverOf(k) {
  const raw = (k.food || {}).coverDays;
  if (raw === null || raw === undefined) return null;
  const n = Number(raw);
  return Number.isFinite(n) ? n : null;
}

// The newest raid line in the kingdom log (the view keeps the last 60 entries, oldest first).
function newestRaid(log) {
  const texts = (Array.isArray(log) ? log : []).map((e) => (e && typeof e.text === 'string' ? e.text : ''));
  return texts.filter((t) => RAID_LOG.test(t)).pop() || '';
}

// Full per-day text for a stock chip, kept in its title. figure is the sim's net for the last day, or null on day 1.
function stockText(key, s, k, figure) {
  const when = figure === null ? 'No figure yet: day 1 has not ended.'
    : 'Net over the last day: ' + signed(figure) + ' (made, minus used, minus lost; trades are not in it).';
  let text = RES_NAME[key] + ': ' + fmt(s.have) + ' of ' + fmt(s.cap) + ' stored. ' + when;
  if (key === 'gold') {
    const m = k.money || {};
    text += ' Last day: taxes ' + signed(m.income) + ', upkeep ' + signed(-(Number(m.upkeepPaid) || 0)) + ' paid of ' +
      fmt(m.upkeepDue) + ' due.';
  } else {
    text += ' Last day: the sim made ' + fmt(s.produced) + ', used ' + fmt(s.consumed) + ' and lost ' + fmt(s.lost) + '.';
  }
  if (key === 'food' && k.food) {
    const cover = coverOf(k);
    text += cover === null ? ' No days of cover: the food made covers the daily need.'
      : ' Days of cover: ' + dec1(cover) + ', the ' + fmt(s.have) + ' stored over a daily need of ' +
        dec1(k.food.demandPerDay) + '.';
  }
  // At the cap, the tip says what is lost while the stock stays full.
  if (s.have >= s.cap) text += ' ' + (key === 'food' ? FULL_TIP_FOOD : FULL_TIP);
  return text;
}

export function mountHud(ctx) {
  const { doc, els, controller, audio } = ctx;
  const win = doc.defaultView;
  const tip = els['tooltip'];
  const strip = els['controls-strip'];
  const status = els['hud-status'];
  // #hud-date holds the date as one text node, then the Paused word as a span beside it. The date is written to its text
  // node alone, so the word stays in place.
  const dateText = doc.createTextNode('');
  const pausedWord = doc.createElement('span');
  pausedWord.hidden = true;
  pausedWord.style.color = 'var(--amber)';
  pausedWord.setAttribute('data-tip', PAUSED_TIP);
  els['hud-date'].replaceChildren(dateText, pausedWord);
  let activeTool = 'select';
  let debugOn = false;
  let trend = 'steady';
  let happyDays = [];
  let tipTimer = 0;
  let tipTarget = null;
  let tipX = 0;
  let tipY = 0;
  let stripTimer = 0;
  let armed = true;
  let lastDay = null;  // the day of the last kingdom view, so a day that goes back (a new kingdom or a load) is noticed
  let raidLine = '';   // the newest raid line from the kingdom log, kept until a newer one is logged

  const on = (id, fn) => els[id].addEventListener('click', fn);
  on('cam-rotate-left', () => controller.cameraAction('left'));
  on('cam-rotate-right', () => controller.cameraAction('right'));
  on('cam-zoom-in', () => controller.cameraAction('in'));
  on('cam-zoom-out', () => controller.cameraAction('out'));
  on('cam-home', () => controller.cameraAction('home'));
  for (let n = 0; n < 4; n++) on('speed-' + n, () => controller.setSpeed(n));
  on('btn-mute', () => {
    audio.toggleMute();
    refreshMute();
  });
  on('btn-save', () => controller.saveGame());
  on('btn-load', () => controller.loadGame());
  for (const name of Object.keys(TOOL_BTN)) {
    if (name !== 'build') on(TOOL_BTN[name], () => controller.setTool(activeTool === name ? 'select' : name));
  }

  // Tooltips: an element with data-tip shows its text in #tooltip after TIP_DELAY_MS.
  function hideTip() {
    clearTimeout(tipTimer);
    tipTimer = 0;
    tipTarget = null;
    tip.hidden = true;
  }
  function placeTip() {
    const vw = win.innerWidth;
    const vh = win.innerHeight;
    const w = tip.offsetWidth;
    const h = tip.offsetHeight;
    let x = tipX + 14;
    let y = tipY + 18;
    if (x + w > vw - 8) x = tipX - w - 14;
    if (y + h > vh - 8) y = tipY - h - 14;
    tip.style.left = Math.max(8, x) + 'px';
    tip.style.top = Math.max(8, y) + 'px';
  }
  doc.addEventListener('pointermove', (e) => {
    tipX = e.clientX;
    tipY = e.clientY;
    const t = e.target && e.target.closest ? e.target.closest('[data-tip]') : null;
    if (t === tipTarget) {
      if (!tip.hidden) placeTip();
      return;
    }
    hideTip();
    if (!t) return;
    tipTarget = t;
    tipTimer = win.setTimeout(() => {
      tip.textContent = t.getAttribute('data-tip') || '';
      tip.hidden = false;
      placeTip();
    }, TIP_DELAY_MS);
  });
  doc.addEventListener('pointerdown', hideTip);
  doc.documentElement.addEventListener('mouseleave', hideTip);
  // A mouse click should not leave the button focused, or Space would press it as well as pause.
  doc.addEventListener('click', (e) => {
    const b = e.target && e.target.closest ? e.target.closest('button') : null;
    if (b && e.detail > 0) b.blur();
  }, true);

  // The controls strip is the hint on the title screen. Its 90 s run starts with each play session, at the first
  // kingdom view after the title closes (update runs only in play). Opening the title shows the strip again.
  function showStrip(ms) {
    clearTimeout(stripTimer);
    stripTimer = ms > 0 ? win.setTimeout(() => { strip.hidden = true; }, ms) : 0;
    strip.hidden = false;
  }
  new win.MutationObserver(() => {
    if (!els['overlay-start'].hidden) {
      armed = true;
      showStrip(0);
    }
    renderStrip();
  }).observe(els['overlay-start'], { attributes: true, attributeFilter: ['hidden'] });
  renderStrip();
  showStrip(0);

  function toolName(t) {
    if (typeof t === 'string') return t;
    if (t && typeof t.tool === 'string') return t.tool;
    return 'select';
  }

  // The strip text follows the tool. The standard hint shows on the title screen and while the Road or Build tool is on;
  // with any other tool it says how to turn the Road tool on. Only the text changes here; showStrip owns the visibility.
  function renderStrip() {
    const titleOpen = !els['overlay-start'].hidden;
    const text = titleOpen || activeTool === 'road' || activeTool === 'build' ? STRIP_TEXT : STRIP_ROAD_TEXT;
    if (strip.textContent !== text) strip.textContent = text;
  }

  function renderTool(tool) {
    activeTool = toolName(tool);
    for (const name of Object.keys(TOOL_BTN)) {
      els[TOOL_BTN[name]].setAttribute('aria-pressed', activeTool === name ? 'true' : 'false');
    }
    renderStrip();
  }

  // The happiness word: the change over TREND_DAYS days, from one sample per day that this HUD keeps (the sim keeps none).
  // A day earlier than the last sample means a new kingdom or an earlier save, so the samples start again.
  function trendOf(day, exact) {
    const last = happyDays[happyDays.length - 1];
    if (last && day < last.day) happyDays = [];
    const now = happyDays[happyDays.length - 1];
    if (now && now.day === day) now.exact = exact;
    else happyDays.push({ day, exact });
    happyDays = happyDays.filter((d) => d.day >= day - TREND_DAYS);
    const delta = exact - happyDays[0].exact;
    return delta > TREND_EPS ? 'rising' : delta < -TREND_EPS ? 'falling' : 'steady';
  }

  // Keeps the newest raid line from the kingdom log. The log holds only its last 60 entries, so a line can leave it; the
  // line is then kept until a newer one is logged. A day that goes back (a new kingdom or a load) clears it.
  function trackRaid(k) {
    const day = Number(k.day);
    if (lastDay !== null && day < lastDay) raidLine = '';
    if (Number.isFinite(day)) lastDay = day;
    raidLine = newestRaid(k.log) || raidLine;
  }

  function renderKingdom(k) {
    const stock = k.stock || {};
    trackRaid(k);
    // Each chip's figure is the sim's net for the last day (stock.net: made, minus used, minus lost, from the ledger). The
    // HUD computes no change of its own. Day 1 (state.day 0) has no last day yet, so it shows a dash.
    const firstDay = k.day === 0;
    for (const key of RES) {
      const chip = els['res-' + key];
      const s = stock[key];
      if (!chip || !s) continue;
      const figure = !firstDay && typeof s.net === 'number' && Number.isFinite(s.net) ? s.net : null;
      // A stock at its cap reads "full" (its tip says what is lost while it stays full); app.css colours the value.
      const full = s.have >= s.cap;
      chip.querySelector('.chip-val').textContent = full ? 'full' : Math.round(s.have) + '/' + Math.round(s.cap);
      const rate = chip.querySelector('.chip-rate');
      rate.querySelector('.chip-num').textContent = figure === null ? NO_FIGURE : signed(figure);
      rate.querySelector('.chip-unit').hidden = figure === null;
      rate.className = 'chip-rate ' + (figure > 0 ? 'up' : figure < 0 ? 'down' : 'flat');
      chip.classList.toggle('full', full);
      chip.title = stockText(key, s, k, figure);
    }
    const p = k.population || {};
    els['hud-pop'].textContent = plural(p.total || 0, 'person', 'people');
    els['hud-pop'].setAttribute('data-tip', fmt(p.employed) + ' employed, ' + fmt(p.unemployed) +
      ' unemployed, ' + fmt(p.homeless) + ' homeless, ' + fmt(p.freeBeds) + ' free beds.');
    const h = k.happiness || {};
    const exact = typeof h.exact === 'number' ? h.exact : null;
    if (exact !== null && typeof k.day === 'number') trend = trendOf(k.day, exact);
    // The value and trend word on line one; the largest negative cause on line two, so a long name never widens the bar.
    const drag = worstCause(h.causes);
    const main = doc.createElement('span');
    main.textContent = 'Happiness ' + fmt(h.value) + ' ' + trend;
    const lines = [main];
    if (drag) {
      const cause = doc.createElement('span');
      cause.className = 'hud-cause';
      cause.textContent = drag.label + ' ' + signed(drag.value, digitsOf(drag.value));
      // The space keeps the text readable as one string; a flex column does not draw it.
      lines.push(' ', cause);
    }
    els['hud-happy'].replaceChildren(...lines);
    const top = biggestCauses(h.causes, 2);
    els['hud-happy'].setAttribute('data-tip', 'Happiness ' + fmt(h.value) + ' of 100, heading to ' + fmt(h.target) +
      '. The word shows the change over the last ' + plural(TREND_DAYS, 'day') + '.' +
      (top.length ? ' Biggest causes: ' + top.map(causeText).join('; ') + '.' : ''));
    // The date is the sim's wording (dateLabel, the same as dateText). The day number is the Log tab's (Day day + 1).
    const hasDay = typeof k.day === 'number' && Number.isFinite(k.day);
    const date = hasDay ? dateLabel(k.day) : k.dateText || '';
    dateText.data = hasDay ? date + ' (Day ' + (k.day + 1) + ')' : date;
    const tier = k.tier || {};
    els['hud-tier'].textContent = tier.name || '';
    els['hud-tier'].setAttribute('data-tip', tier.nextName ? 'Next tier: ' + tier.nextName : 'Highest tier reached');
  }

  // Status line under the top bar, in play only, at most three lines (styles/app.css). Parts in order: the next raid, from
  // the Kingdom panel's threat view (shown from the moment it is scheduled, with the Watchtower action while defence is 0);
  // food cover or the low-food warning; plague; the worst negative happiness cause with its detail; the newest raid line
  // from the kingdom log, which the line clamp drops first. With no people, the food, cause and raid parts are left out.
  function renderStatus(k) {
    const cover = coverOf(k);
    const warnDays = Number(k.foodWarnDays);
    const threats = k.threats || {};
    const raid = threats.raid || {};
    const plague = threats.plague || {};
    const alive = (k.population || {}).total !== 0;
    // The raid resolves inside the tick of its own day, so on that day it is still pending: "Raid today".
    const raidIn = typeof raid.day === 'number' && typeof k.day === 'number' ? raid.day - k.day : -1;
    const parts = [];
    if (alive && raidIn >= 0) {
      const line = (raidIn === 0 ? 'Raid today' : 'Raid in ' + plural(raidIn, 'day')) +
        ': strength ' + fmt(raid.strength) + ', defence ' + fmt(raid.defence);
      parts.push(Number(raid.defence) === 0 ? line + '. Build a Watchtower (Build > Defence).' : line);
    }
    // No figure (null) means food income covers use: no shortage, and no cover to show.
    if (alive && cover !== null && Number.isFinite(warnDays) && cover < warnDays) {
      const days = Math.floor(cover);
      // Half is the lowest ration setting, so with rations already at Half only the farm is named.
      const halfRations = (k.policies || {}).rations === 'half';
      parts.push('Low food: ' + (days < 1 ? 'less than a day' : plural(days, 'day')) + ' of cover. ' +
        (halfRations ? 'Build a Farm.' : LOW_FOOD_FIX));
    } else if (alive && cover !== null) {
      parts.push('Food: ' + cover + (cover === 1 ? ' day' : ' days') + ' of cover');
    }
    if (plague.active) parts.push('Plague: ' + plural(plague.daysLeft, 'day') + ' left');
    else if (plague.warned) parts.push('Plague: starts within 2 days');
    // The worst negative happiness cause with its detail (the top bar gives only its label and value). Only when negative.
    const worst = alive ? worstCause((k.happiness || {}).causes) : null;
    if (worst) parts.push(causeText(worst));
    if (alive && raidLine) parts.push(raidLine);
    status.textContent = parts.join(' | ');
    status.hidden = parts.length === 0;
  }

  // The Paused word beside the date: the clock is stopped (speed 0) in a kingdom still in play. The title screen is not in
  // play (its start overlay is open), and a won or lost kingdom is over, so neither shows it.
  function renderPaused(kingdom, speed) {
    const outcome = kingdom && kingdom.outcome ? kingdom.outcome.status : '';
    const running = outcome === 'playing' || outcome === 'sandbox';
    const stopped = running && Number(speed) === 0 && els['overlay-start'].hidden;
    if (pausedWord.hidden === stopped) {
      pausedWord.hidden = !stopped;
      pausedWord.textContent = stopped ? PAUSED_TEXT : '';
    }
  }

  function renderHint(hint) {
    const box = els['tool-hint'];
    const text = typeof hint === 'string' ? hint.trim() : '';
    if (box.textContent !== text) box.textContent = text;
    box.hidden = text === '';
  }

  function renderDebug(perf) {
    if (!debugOn) return;
    const p = perf || {};
    els['debug-line'].textContent = 'fps ' + fmt(p.fps) + ' | day ' + fmt(p.day) + ' | advance ' +
      (Number(p.advanceMs) || 0).toFixed(1) + ' ms | draws ' + fmt(p.drawCalls);
  }

  function refreshMute() {
    const muted = !!audio && audio.isMuted();
    const text = muted ? 'Sound off' : 'Sound on';
    const b = els['btn-mute'];
    b.querySelector('.lbl').textContent = text;
    b.setAttribute('aria-label', text);
  }

  // kingdom: KingdomView; speed: 0..3; tool: name or {tool, type}; perf: {fps, advanceMs, drawCalls, day}; hint: string.
  function update(kingdom, speed, tool, perf, hint) {
    if (kingdom) {
      renderKingdom(kingdom);
      renderStatus(kingdom);
      if (armed) {
        armed = false;
        showStrip(STRIP_MS);
      }
    }
    renderPaused(kingdom, speed);
    // Every update: the pressed speed is the one the clock runs at, so II is pressed only while paused.
    for (let n = 0; n < 4; n++) els['speed-' + n].setAttribute('aria-pressed', Number(speed) === n ? 'true' : 'false');
    renderTool(tool);
    renderHint(hint);
    renderDebug(perf);
    refreshMute();
    if (!tip.hidden && tipTarget) tip.textContent = tipTarget.getAttribute('data-tip') || '';
  }

  function setDebugVisible(on) {
    debugOn = !!on;
    els['debug-line'].hidden = !debugOn;
    if (!debugOn) els['debug-line'].textContent = '';
  }

  refreshMute();
  return { update, setDebugVisible };
}
