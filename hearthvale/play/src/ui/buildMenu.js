// owner: ui-panels
// Build panel (ARCHITECTURE 9.6): category tabs and one card per building in #build-grid.
// Reads the catalog that main.js passes in, and the stock and tutorial step from controller.getKingdomView(). Changes the
// game only through controller.setTool and controller.rotateGhost. It also listens for the 'tool' event, to know which
// building the build tool holds. It re-arms nothing: the controller keeps the building armed after a placement (R1-03).
import { fmt, plural } from './format.js';

const TABS = [
  ['housing', 'Housing'], ['food', 'Food'], ['materials', 'Materials'], ['crafts', 'Crafts'],
  ['services', 'Services'], ['defence', 'Defence'], ['special', 'Special'],
];
const FIRST_TAB = 'housing'; // the tab a fresh panel opens on
const RES = ['food', 'wood', 'stone', 'iron', 'goods', 'gold'];
const BLOCK = { style: 'display:block' };
const WARN = { class: 'warn', style: 'display:block' };
const TUT_LINE = { style: 'display:block;font-weight:700' };

const dec = (n) => String(Math.round(Number(n) * 10) / 10);

function costText(cost) {
  const parts = RES.filter((k) => cost && cost[k] > 0).map((k) => fmt(cost[k]) + ' ' + k);
  return parts.length ? parts.join(', ') : 'nothing';
}

// Same wording as the sim's canAfford: the first short resource in stock order.
function shortfall(cost, stock) {
  for (const k of RES) {
    const need = cost && cost[k] > 0 ? cost[k] : 0;
    const have = stock && stock[k] ? stock[k].have : 0;
    if (need > have) return 'Not enough ' + k + ': need ' + need + ', have ' + have;
  }
  return null;
}

function crewText(e) {
  if (!e.crew) return 'no workers';
  return e.crewRole === 'militia' ? fmt(e.crew) + ' militia' : plural(e.crew, 'worker');
}

// A tier lock names the tier and where its goal is shown (R1-03). Other locks keep the sim's text.
const GOAL = 'Kingdom > Overview lists the goal.';
const lockText = (r) => (r && r.startsWith('Unlocks at the ') ? r + '. ' + GOAL : r || null);

// The road need on a card's days line (R2-07). Every building needs a road to the Town Hall (6.2, placeBuilding check 10),
// except the Town Hall, which is placed, and the road tools, which are laid with the road tool.
const roadNote = (e) => (e.type === 'townHall' ? ''
  : e.category === 'infra' ? ', laid with the road tool' : ', needs a road to the Town Hall');

// tut: this card is the building the tutorial step asks for. It gets a gold border and a visible line.
function card(h, e, reason, pressed, tut) {
  const cost = costText(e.cost);
  const days = plural(e.buildDays, 'day') + roadNote(e);
  const crew = crewText(e);
  const label = e.name + ', costs ' + cost + ', ' + days + ', upkeep ' + dec(e.upkeep) + ', ' + crew +
    (reason ? '. ' + reason : '');
  const out = e.produces ? 'Makes ' + dec(e.produces.perDay) + ' ' + e.produces.resource + ' a day'
    : e.beds ? 'Houses ' + plural(e.beds, 'person', 'people') : null;
  return h('button', { type: 'button', 'data-type': e.type, style: tut ? 'border:2px solid var(--amber-deep)' : null,
    title: (tut ? 'Tutorial step: build this. ' : '') + (e.tooltip || label),
    'aria-label': (tut ? 'Tutorial step: ' : '') + label, 'aria-pressed': pressed ? 'true' : 'false' },
  tut ? h('span', TUT_LINE, 'Tutorial step: build this') : null,
  h('span', BLOCK, h('strong', null, e.name)),
  h('span', BLOCK, 'Cost: ' + cost),
  h('span', BLOCK, days + ', upkeep ' + dec(e.upkeep) + ' gold a day, ' + crew),
  out ? h('span', BLOCK, out) : null,
  reason ? h('span', WARN, reason) : null);
}

// Element factory bound to a document: h(tag, attrs, ...kids). Attributes set to false, null or undefined are skipped.
function factory(doc) {
  return function h(tag, attrs, ...kids) {
    const node = doc.createElement(tag);
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

export function mountBuildMenu(ctx) {
  const { doc, els, controller } = ctx;
  const h = factory(doc);
  const panel = els['panel-build'];
  const tabBox = els['build-tabs'];
  const grid = els['build-grid'];
  let catalog = [];
  let active = FIRST_TAB;
  let selected = null;
  let tutorialShown; // the tutorial building the tab was last set for; open() clears it, so each opening selects its tab
  let tutorialTab = null; // the tab the tutorial last chose, so a step with no building can hand it back
  let armed = null; // the building the build tool is armed with; Escape, another card, another tool or closing clears it

  tabBox.setAttribute('role', 'tablist');
  tabBox.setAttribute('aria-label', 'Building categories');
  for (const [key, label] of TABS) {
    tabBox.appendChild(h('button', { type: 'button', role: 'tab', 'data-tab': key, title: label + ' buildings',
      'aria-label': label + ' buildings' }, label));
  }
  tabBox.addEventListener('click', (e) => {
    const t = pick(e.target, tabBox, 'data-tab');
    if (t) setTab(t.getAttribute('data-tab'));
  });
  grid.addEventListener('click', (e) => {
    const c = pick(e.target, grid, 'data-type');
    if (c) controller.setTool('build', { type: c.getAttribute('data-type') });
  });
  els['build-rotate'].addEventListener('click', () => controller.rotateGhost());
  els['build-close'].addEventListener('click', () => { if (armed) controller.setTool('select'); close(); });

  const isOpen = () => !panel.hidden;

  // The armed building follows the controller's tool: a build tool arms its type, any other tool clears it. The controller
  // keeps the building armed after a placement (R1-03), so this panel never sets a tool on its own after an event.
  // close() leaves the tool alone, because main.js calls it from a tool event.
  controller.on('tool', (t) => {
    armed = t.tool === 'build' ? t.type || null : null;
  });

  function paintTabs() {
    for (const t of Array.from(tabBox.childNodes)) {
      t.setAttribute('aria-selected', t.getAttribute('data-tab') === active ? 'true' : 'false');
    }
  }

  // Only a string buildingKey (ARCHITECTURE 7.7) selects a tab or a highlight. A road step has none (null), so the tab
  // the tutorial chose before goes back to the first tab and the panel never opens on another step's tab. The tutorial's
  // tab opens when the panel opens and whenever the step moves on to another building. Between those, the player's own
  // tab choice stays.
  function render() {
    const kv = controller.getKingdomView();
    const obj = kv.objective;
    const tutorial = obj && typeof obj.buildingKey === 'string' ? obj.buildingKey : null;
    if (tutorial !== tutorialShown) {
      tutorialShown = tutorial;
      const want = tutorial ? catalog.find((x) => x.type === tutorial) : null;
      const tab = want && TABS.some(([k]) => k === want.category) ? want.category : null;
      if (tab) active = tab;
      else if (tutorialTab !== null && active === tutorialTab) active = FIRST_TAB;
      tutorialTab = tab;
    }
    paintTabs();
    const fresh = doc.createElement('div');
    for (const e of catalog) {
      if (e.category !== active) continue;
      let reason = null;
      if (!e.unlocked) reason = lockText(e.lockReason);
      else if (!e.affordable) reason = shortfall(e.cost, kv.stock);
      fresh.appendChild(card(h, e, reason, e.type === selected, e.type === tutorial));
    }
    morphKids(grid, fresh);
  }

  function setTab(key) {
    if (key === active) return;
    active = key;
    if (isOpen()) render();
  }

  function open() {
    tutorialShown = undefined;
    panel.hidden = false;
    render();
  }

  function close() {
    armed = null;
    panel.hidden = true;
  }

  // list: the catalog from getCatalog(state) (section 7.2).
  function update(list) {
    catalog = Array.isArray(list) ? list : [];
    if (isOpen()) render();
  }

  // type: the building type the build tool is placing, or null. A new type opens its category tab.
  function setSelected(type) {
    const next = typeof type === 'string' ? type : null;
    if (next !== selected) {
      selected = next;
      const e = next ? catalog.find((x) => x.type === next) : null;
      if (e && TABS.some(([k]) => k === e.category)) active = e.category;
    }
    if (isOpen()) render();
  }

  paintTabs();
  return { update, setSelected, open, close, isOpen };
}
