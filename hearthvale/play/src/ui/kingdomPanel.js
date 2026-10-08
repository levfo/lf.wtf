// owner: ui-panels
// Kingdom panel (ARCHITECTURE 9.6): seven tabs over the KingdomView. Every action goes through controller.dispatch,
// so the controller toasts each success message and each refusal reason.
import { dateLabel, fmt, plural, signed } from './format.js';

const TABS = ['overview', 'people', 'economy', 'market', 'policies', 'goals', 'log'];
const RES = ['food', 'wood', 'stone', 'iron', 'goods', 'gold'];
const TRADE = ['food', 'wood', 'stone', 'iron', 'goods'];
const AMOUNTS = [10, 50];
const WORD = { up: 'rising', down: 'falling', flat: 'steady' };
const NO_WORKER = 'The Market needs at least one worker';
// The label a blocked trade control carries (R2-06 a): the path to a Market, or the worker the Market needs.
const TRADE_SHORT = { 'Trading needs a complete Market': 'Build a Market from Build > Services, then wait for it to finish.',
  [NO_WORKER]: 'Needs a worker' };
// Policy key -> the happiness cause it moves (ARCHITECTURE 5.6), so each policy row can show its number (R1-14 b).
const EFFECT = { tax: 'tax', rations: 'rations', draftRate: 'draft' };
const TONE = { good: 'good', warn: 'warn', bad: 'bad', info: 'muted' };
const ROW = { style: 'margin:6px 0' };
const BUTTONS = { style: 'display:flex;flex-wrap:wrap;gap:6px' };
// [key, heading, {value: [button label, description]}]. Rations use the game's "Half rations" wording throughout.
const POLICIES = [
  ['tax', 'Tax', { low: ['Low taxes', 'Low taxes: better mood, less gold.'], normal: ['Normal taxes', 'Normal taxes.'],
    high: ['High taxes', 'High taxes: more gold, lower mood.'] }],
  ['rations', 'Rations', { half: ['Half rations', 'Half rations: people eat less and grow unhappy.'],
    normal: ['Normal rations', 'Normal rations.'], full: ['Full rations', 'Full rations: people eat more and are content.'] }],
  ['draftRate', 'Draft', { off: ['No draft', 'No draft.'], light: ['Light draft', 'A light draft: some adults take up arms.'],
    full: ['Full draft', 'A full draft: many adults take up arms.'] }],
];

const cap = (s) => (s ? s.charAt(0).toUpperCase() + s.slice(1) : '');
const dec = (n) => String(Math.round(Number(n) * 10) / 10);
const tone = (n) => (n > 0 ? 'good' : n < 0 ? 'bad' : 'muted');

// "Needs 10 goods (have 3)" for the first short resource in stock order (as the sim's canAfford), or null when affordable.
function shortText(cost, stock) {
  for (const k of RES) {
    const need = cost && cost[k] > 0 ? cost[k] : 0;
    const have = stock && stock[k] ? stock[k].have : 0;
    if (need > have) return 'Needs ' + fmt(need) + ' ' + k + ' (have ' + fmt(have) + ')';
  }
  return null;
}

// Why an upgrade cannot be bought now, or null. A tier lock keeps the sim's text; otherwise the short resource.
function upgradeWhy(u, tier, kv) {
  if (u.owned || u.available) return null;
  if (tier > kv.tier.id) return u.reason || null;
  return shortText(u.cost, kv.stock) || u.reason || null;
}

// Why the festival button is off, or null. Same order as the sim: tavern, then cooldown, then gold and food.
function festivalWhy(kv) {
  const f = kv.festival;
  if (f.canHold) return null;
  const tavern = kv.buildingCounts.tavern && kv.buildingCounts.tavern.complete > 0;
  return tavern && f.cooldownLeft <= 0 ? shortText(f.cost, kv.stock) || f.reason : f.reason;
}

function costText(cost) {
  const parts = RES.filter((k) => cost && cost[k] > 0).map((k) => fmt(cost[k]) + ' ' + k);
  return parts.length ? parts.join(', ') : 'nothing';
}

function tierLine(t) {
  return 'Tier: ' + t.name + (t.nextName ? '. Next: ' + t.nextName + '.' : '. Highest tier reached.');
}

// The food line (R2-06 b, 7.8). The days are the view's cover figure, the one the top bar and status line read: the stock over
// the last day's food deficit (food eaten minus food made). The Kingdom view has no daily deficit field, so the line shows
// the days alone. It never takes a deficit from stock.food.net, which also counts lost food. A null figure reads as not
// running short.
function foodText(k) {
  const days = k.food.coverDays;
  if (typeof days === 'number' && Number.isFinite(days)) {
    return 'Food lasts ' + (days < 1 ? 'less than a day' : plural(days, 'day')) + '.';
  }
  return 'Food is not running short at the current net rate.';
}

// Food has recovered (R2-06 d): no shortage (a null figure), or a cover figure at the warning threshold or above.
function foodRecovered(k) {
  const days = k.food.coverDays;
  if (days === null) return true;
  return typeof days === 'number' && Number.isFinite(days) && days >= k.foodWarnDays;
}

function checkItems(h, checks) {
  return checks.map((c) => h('li', { class: c.ok ? 'good' : 'muted' },
    c.label + ': ' + fmt(c.have) + ' of ' + fmt(c.need) + (c.ok ? ' (met)' : '')));
}

function checkList(h, checks) {
  return checks.length ? [h('h3', null, 'Tier checklist'), h('ul', null, checkItems(h, checks))] : [];
}

// The date cell of a log row: the sim's wording from dateLabel, then the day number in parentheses, as the top bar shows it
// ("Spring 1, Year 1 (Day 1)"). A day that is not a number gives an empty cell.
function dayCell(day) {
  const when = dateLabel(day);
  return when ? when + ' (Day ' + (Number(day) + 1) + ')' : '';
}

// Rows of log entries (already newest first): {day, kind, text}.
function logTable(h, rows) {
  return h('table', null,
    h('thead', null, h('tr', null, h('th', null, 'Date'), h('th', null, 'What happened'))),
    h('tbody', null, rows.map((e) => h('tr', null, h('td', null, dayCell(e.day)),
      h('td', { class: TONE[e.kind] || 'muted' }, e.text)))));
}

function overview(h, k) {
  const r = k.threats;
  const d = k.defence;
  const dist = r.raid.day - k.day;
  const plague = r.plague.active ? 'Plague: ' + plural(r.plague.daysLeft, 'day') + ' left.'
    : r.plague.warned ? 'Plague: a warning is out.' : 'Plague: none.';
  const drought = r.drought.active ? 'Drought: ' + plural(r.drought.daysLeft, 'day') + ' left; farms yield less.'
    : r.drought.warned ? 'Drought: due tomorrow.' : 'Drought: none.';
  const flood = r.flood.active ? 'Flood: the river is high; riverside farms yield less.'
    : r.flood.warned ? 'Flood: the river is rising.' : 'Flood: none.';
  return [
    h('p', null, k.dateText + '. ' + tierLine(k.tier)),
    ...checkList(h, k.tier.nextChecks),
    h('h3', null, 'Threats'),
    h('p', null, 'Raid: ' + (dist <= 0 ? 'today' : 'in ' + plural(dist, 'day')) + ', strength ' + r.raid.strength +
      ', defence ' + r.raid.defence + (r.raid.warned ? '. Riders are on the way.' : '.')),
    h('p', null, 'Defence ' + d.total + ': militia ' + d.militia + ', watchtowers ' + d.towers + ', barracks ' + d.barracks + '.'),
    h('p', null, plague),
    h('p', null, drought),
    h('p', null, flood),
    h('p', null, 'Fire risk: ' + r.fireRisk + '.'),
    h('h3', null, 'Recent news'),
    logTable(h, k.log.slice(-6).reverse()),
  ];
}

function people(h, k) {
  const p = k.population;
  const s = k.stats;
  const m = k.happiness;
  const causes = m.causes.slice().sort((a, b) => (a.value === 0) - (b.value === 0) || Math.abs(b.value) - Math.abs(a.value));
  return [
    h('h3', null, 'Population'),
    h('p', null, fmt(p.total) + ' people: ' + fmt(p.children) + ' children, ' + fmt(p.adults) + ' adults, ' + fmt(p.elders) + ' elders.'),
    h('p', null, 'Jobs: ' + fmt(p.employed) + ' employed, ' + fmt(p.unemployed) + ' unemployed.'),
    h('p', null, 'Beds: ' + fmt(p.freeBeds) + ' free of ' + fmt(p.beds) + '. Homeless: ' + fmt(p.homeless) + '. Militia: ' + fmt(p.militia) + '.'),
    h('p', null, 'Since founding: births ' + fmt(s.born) + ', deaths ' + fmt(s.died) + ', arrivals ' + fmt(s.immigrated) + '.'),
    h('h3', null, 'Happiness'),
    h('p', null, 'Mood ' + fmt(m.value) + ' of 100, heading to ' + fmt(m.target) + '.'),
    h('table', null,
      h('thead', null, h('tr', null, h('th', null, 'Cause'), h('th', { class: 'num' }, 'Value'), h('th', null, 'Detail'))),
      h('tbody', null, causes.map((c) => h('tr', null, h('td', null, c.label),
        h('td', { class: 'num ' + tone(c.value) }, signed(c.value, Number.isInteger(c.value) ? 0 : 1)),
        h('td', null, c.detail))))),
  ];
}

function economy(h, k) {
  const m = k.money;
  const w = k.winter;
  const rows = RES.map((r) => {
    const s = k.stock[r];
    return h('tr', null, h('td', null, cap(r)), h('td', { class: 'num' }, fmt(s.have)), h('td', { class: 'num' }, fmt(s.cap)),
      h('td', { class: 'num ' + tone(s.net) }, signed(s.net)), h('td', { class: 'num' }, fmt(s.produced)),
      h('td', { class: 'num' }, fmt(s.consumed)), h('td', { class: 'num' }, fmt(s.lost)));
  });
  const winter = w.visible ? [
    h('h3', null, 'Winter reserve'),
    h('p', { class: w.ok ? 'good' : 'warn' }, w.ok
      ? 'Food covers the winter: ' + fmt(w.haveFood) + ' of ' + fmt(w.needFood) + ' needed.'
      : 'Short of winter food: ' + fmt(w.haveFood) + ' of ' + fmt(w.needFood) + ' needed. Add farms, or set Rations to Half (Kingdom > Policies).'),
    typeof w.daysLeft === 'number' ? h('p', { class: 'muted' }, plural(w.daysLeft, 'day') + ' until spring.') : null,
  ] : [];
  return [
    h('h3', null, 'Stock'),
    h('table', null,
      h('thead', null, h('tr', null, h('th', null, 'Resource'), h('th', { class: 'num' }, 'Stock'), h('th', { class: 'num' }, 'Cap'),
        h('th', { class: 'num' }, 'Net'), h('th', { class: 'num' }, 'Made'), h('th', { class: 'num' }, 'Used'), h('th', { class: 'num' }, 'Lost'))),
      h('tbody', null, rows)),
    h('p', null, foodText(k)),
    h('p', null, 'Gold: ' + fmt(m.income) + ' tax a day. Upkeep ' + fmt(m.upkeepPaid) + ' paid of ' + fmt(m.upkeepDue) +
      ' due. Net ' + signed(m.net) + ' a day.'),
    ...winter,
    h('h3', null, 'Upgrades'),
    ...k.upgrades.map((u) => {
      const cost = costText(u.cost);
      const why = u.owned ? null : upgradeWhy(u, u.tier, k);
      return h('div', ROW,
        h('p', null, u.name + ': ' + u.text + ' Cost: ' + cost + '.'),
        h('button', { type: 'button', id: 'upgrade-buy-' + u.key, 'data-act': 'upgrade', 'data-key': u.key,
          title: u.owned ? 'Already bought. ' + u.text : u.text + ' Cost: ' + cost + '.' + (why ? ' ' + why + '.' : ''),
          'aria-label': u.owned ? u.name + ' bought' : 'Buy ' + u.name + ' for ' + cost + (why ? '. ' + why : ''),
          disabled: u.owned || !!why }, u.owned ? 'Bought' : why || 'Buy'));
    }),
  ];
}

function market(h, k, mv) {
  const t = k.trade;
  const status = t.open ? 'Trading is open: up to ' + t.limit + ' of each resource a day.' : (t.reason || 'Trading is closed') + '.';
  // While trading is closed, each control says why: its label becomes the short reason, and its title and aria-label
  // carry the full reason.
  const why = t.open ? null : (t.reason || 'Trading is closed') + '.';
  const short = t.open ? null : TRADE_SHORT[t.reason] || t.reason || 'Trading closed';
  const rows = TRADE.map((r) => {
    const pr = k.prices[r];
    const buttons = [];
    for (const mode of ['buy', 'sell']) {
      for (const n of AMOUNTS) {
        buttons.push(h('button', { type: 'button', id: 'trade-' + mode + '-' + n + '-' + r, 'data-act': 'trade',
          'data-mode': mode, 'data-amount': n, 'data-resource': r,
          title: cap(mode) + ' ' + n + ' ' + r + '. ' + (why || 'Limit ' + t.limit + ' a day.'),
          'aria-label': cap(mode) + ' ' + n + ' ' + r + (why ? '. ' + why : ''), disabled: !t.open },
        short || cap(mode) + ' ' + n));
      }
    }
    return h('div', ROW,
      h('p', null, h('strong', null, cap(r)), ': ' + (WORD[pr.trend] || 'steady') + '. Buy price ' + fmt(pr.buy) +
        ' gold per unit, sell price ' + fmt(pr.sell) + ' gold per unit. Base price ' + fmt(pr.base) + ' gold per unit. ' +
        'Traded today: ' + fmt(t.used[r]) + ' of ' + t.limit + ' units.'),
      h('div', BUTTONS, buttons));
  });
  const offers = k.caravans.length ? k.caravans.map((c) => h('div', ROW, h('p', null, c.text),
    h('button', { type: 'button', id: 'accept-offer-' + c.id, 'data-act': 'accept', 'data-id': c.id,
      title: 'Accept: ' + c.text + (why ? '. ' + why : ''), 'aria-label': 'Accept offer: ' + c.text + (why ? '. ' + why : ''),
      disabled: !t.open }, short || 'Accept')))
    : [h('p', { class: 'muted' }, 'No caravan offers right now.')];
  // The Market's workers from its building view (ARCHITECTURE 7.4): assigned now, of the crew it needs. No Market placed
  // (mv null), no line.
  const workers = mv && mv.workers ? [h('p', { class: mv.workers.count > 0 ? 'good' : 'warn' },
    'Market: ' + fmt(mv.workers.count) + ' of ' + plural(mv.crewNeeded, 'worker') + ' assigned.')] : [];
  // With no worker in the Market (the trade gate says so), the status also says how many are free and where to staff it.
  const p = k.population;
  const free = 'Free workers: ' + fmt(p.unemployed) + ' (' + fmt(p.employed) + ' employed). ';
  const staff = t.reason === NO_WORKER ? [h('p', { class: 'warn' }, free + 'Workers are assigned at dawn. To staff the Market ' +
    'first, click it on the map and set its staffing to Priority.')] : [];
  return [h('p', { class: t.open ? 'good' : 'warn' }, status), ...workers, ...staff, h('h3', null, 'Prices'), ...rows,
    h('h3', null, 'Caravans'), ...offers];
}

// The setting's effect besides mood, in numbers from the Kingdom view (R1-14 b): food use a day under rations, gold a day
// from tax, and the militia count under the draft.
const EFFECT_NOW = {
  tax: (k) => 'Tax: ' + fmt(k.money.income) + ' gold a day at this setting.',
  rations: (k) => 'Food use: ' + dec(k.food.demandPerDay) + ' a day at this setting.',
  draftRate: (k) => 'Militia: ' + plural(k.population.militia, 'person', 'people') + ' at this setting.',
};

function policies(h, k) {
  const pol = k.policies;
  const f = k.festival;
  const causes = k.happiness.causes || [];
  const out = [];
  for (const [key, label, opts] of POLICIES) {
    const v = (causes.find((c) => c.key === EFFECT[key]) || { value: 0 }).value;
    out.push(h('h3', null, label));
    out.push(h('div', BUTTONS, Object.keys(opts).map((o) => h('button', { type: 'button',
      'data-act': 'policy', 'data-key': key, 'data-value': o, 'aria-pressed': pol[key] === o ? 'true' : 'false',
      title: opts[o][1], 'aria-label': opts[o][0] }, opts[o][0]))));
    out.push(h('p', { class: 'muted' }, opts[pol[key]][1]));
    out.push(h('p', { class: tone(v) }, label + ': ' + pol[key] + ', ' + signed(v) + ' happiness.'));
    out.push(h('p', null, EFFECT_NOW[key](k)));
    // Half rations kept on after food has recovered (R2-06 d). Display only: the setting itself does not change.
    if (key === 'rations' && pol.rations === 'half' && foodRecovered(k)) {
      out.push(h('p', { class: 'good' }, 'Food has recovered: set Rations back to Normal to regain happiness.'));
    }
  }
  const cost = costText(f.cost);
  const why = festivalWhy(k);
  out.push(h('h3', null, 'Festival'));
  out.push(h('p', null, 'A festival costs ' + cost + ' and lifts happiness for a few days.'));
  if (f.activeUntil !== null && f.activeUntil > k.day) {
    out.push(h('p', { class: 'good' }, 'A festival is running: ' + plural(f.activeUntil - k.day, 'day') + ' left.'));
  }
  out.push(h('button', { type: 'button', id: 'btn-festival', 'data-act': 'festival',
    title: 'Hold a festival: ' + cost + '.' + (why ? ' ' + why + '.' : ''),
    'aria-label': 'Hold a festival, costs ' + cost + (why ? '. ' + why + '.' : ''), disabled: !!why }, why || 'Hold a festival'));
  out.push(h('p', { class: 'muted' }, 'The harvest fair happens by itself each autumn.'));
  return out;
}

function goals(h, k) {
  const ob = k.objective;
  const t = k.tier;
  const out = [h('p', null, ob.goal)];
  if (ob.sandboxGoal) out.push(h('p', { class: 'good' }, ob.sandboxGoal));
  out.push(h('h3', null, 'Tier'), h('p', null, 'Now: ' + t.name + (t.nextName ? '. Next: ' + t.nextName + '.' : '.')));
  out.push(...checkList(h, t.nextChecks));
  out.push(h('h3', null, 'Milestones'));
  out.push(h('ul', null, k.milestones.map((m) => h('li', { class: m.done ? 'good' : 'muted' }, h('strong', null, m.name),
    ': ' + (m.done ? 'done on day ' + (m.day + 1) : 'not yet') + '. ' + m.text))));
  if (!ob.done) {
    out.push(h('button', { type: 'button', id: 'btn-goals-skip', 'data-act': 'skip',
      title: 'Skip the tutorial. Your goals stay on this tab.', 'aria-label': 'Skip tutorial' }, 'Skip tutorial'));
  }
  return out;
}

function log(h, k) {
  return [h('p', { class: 'muted' }, 'Newest first.'), logTable(h, k.log.slice().reverse())];
}

const BUILD = { overview, people, economy, market, policies, goals, log };

// Element factory bound to a document: h(tag, attrs, ...kids). Attributes set to false, null or undefined are skipped.
function factory(doc) {
  return function h(tag, attrs, ...kids) {
    const node = doc.createElement(tag);
    if (tag === 'p') node.setAttribute('style', 'margin:4px 0');
    for (const name of Object.keys(attrs || {})) {
      const v = attrs[name];
      if (v === false || v === null || v === undefined) continue;
      node.setAttribute(name, v === true ? '' : String(v));
    }
    for (const k of kids.flat(Infinity)) {
      if (k === null || k === undefined || k === false) continue;
      node.appendChild(typeof k === 'string' || typeof k === 'number' ? doc.createTextNode(String(k)) : k);
    }
    return node;
  };
}

// Makes the children of `live` match `fresh`, reusing live nodes where the tag matches. Clicks and focus survive refreshes.
function morphKids(live, fresh) {
  const kids = Array.from(fresh.childNodes);
  kids.forEach((f, i) => {
    const l = live.childNodes[i];
    if (!l) live.appendChild(f);
    else if (l.nodeName !== f.nodeName) live.replaceChild(f, l);
    else if (f.nodeType === 3) {
      if (l.nodeValue !== f.nodeValue) l.nodeValue = f.nodeValue;
    } else {
      syncAttrs(l, f);
      morphKids(l, f);
    }
  });
  while (live.childNodes.length > kids.length) live.removeChild(live.lastChild);
}

function syncAttrs(live, fresh) {
  for (const a of Array.from(live.attributes)) if (!fresh.hasAttribute(a.name)) live.removeAttribute(a.name);
  for (const a of Array.from(fresh.attributes)) if (live.getAttribute(a.name) !== a.value) live.setAttribute(a.name, a.value);
}

// The nearest node from `node` up to (not including) `box` that carries attribute `name`, or null.
function pick(node, box, name) {
  for (let n = node; n && n !== box; n = n.parentNode) {
    if (n.getAttribute && n.getAttribute(name) !== null) return n;
  }
  return null;
}

export function mountKingdomPanel(ctx) {
  const { doc, els, controller } = ctx;
  const h = factory(doc);
  const panel = els['panel-kingdom'];
  const body = els['kingdom-body'];
  let view = null;
  let marketView = null;   // the Market's BuildingView, or null when no Market is placed (see update)
  let current = 'overview';

  const isOpen = () => !panel.hidden;

  function paintTabs() {
    for (const n of TABS) els['tab-' + n].setAttribute('aria-selected', n === current ? 'true' : 'false');
  }

  function render() {
    if (!view) return;
    const fresh = doc.createElement('div');
    for (const n of BUILD[current](h, view, marketView)) if (n) fresh.appendChild(n);
    morphKids(body, fresh);
  }

  function setTab(name) {
    current = name;
    paintTabs();
    body.scrollTop = 0;
    render();
  }

  // name: optional tab. Opens the panel on that tab, or keeps the current tab.
  function open(name) {
    if (TABS.includes(name)) current = name;
    paintTabs();
    panel.hidden = false;
    render();
  }

  function close() {
    panel.hidden = true;
  }

  // Closed: open on the tab. Open on another tab: switch to it. Open on the same tab (or no tab): close.
  function toggle(name) {
    const want = TABS.includes(name) ? name : null;
    if (!isOpen()) {
      open(want);
      return;
    }
    if (want && want !== current) {
      setTab(want);
      return;
    }
    close();
  }

  // v: KingdomView from the controller. m: the Market's BuildingView (getBuildingView), or null when no Market is placed.
  // Left out, m keeps the last value (the close-and-reopen and click refreshes pass only v). Re-renders only while open.
  function update(v, m) {
    if (v) view = v;
    if (m !== undefined) marketView = m;
    if (isOpen()) render();
  }

  for (const n of TABS) els['tab-' + n].addEventListener('click', () => setTab(n));
  // The X runs the same close() that Escape runs (main.js escape()), so both leave the panel in the same state.
  els['kingdom-close'].addEventListener('click', () => close());
  body.addEventListener('click', (e) => {
    const b = pick(e.target, body, 'data-act');
    if (!b) return;
    const get = (name) => b.getAttribute(name);
    const act = get('data-act');
    let cmd = null;
    if (act === 'trade') cmd = { type: 'trade', resource: get('data-resource'), mode: get('data-mode'), amount: Number(get('data-amount')) };
    else if (act === 'accept') cmd = { type: 'acceptOffer', offerId: Number(get('data-id')) };
    else if (act === 'policy') cmd = { type: 'setPolicy', key: get('data-key'), value: get('data-value') };
    else if (act === 'festival') cmd = { type: 'festival' };
    else if (act === 'upgrade') cmd = { type: 'buyUpgrade', key: get('data-key') };
    else if (act === 'skip') cmd = { type: 'skipTutorial' };
    if (!cmd) return;
    controller.dispatch(cmd);
    update(controller.getKingdomView());   // the change shows at once, not on the next update (R1-14 c)
  });

  paintTabs();
  return { open, close, toggle, update, isOpen };
}
