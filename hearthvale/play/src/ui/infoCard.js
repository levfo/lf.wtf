// owner: ui-panels
// Info card (ARCHITECTURE 9.6): the selected building or map tile. Actions go through controller.dispatch,
// controller.select, the camera (renderer.camera.focusTile) and actions.confirm.
import { fmt, pct, plural } from './format.js';

const RES = ['food', 'wood', 'stone', 'iron', 'goods', 'gold'];
const NEXT = { normal: 'priority', priority: 'paused', paused: 'normal' };
const LABEL = { normal: 'Normal', priority: 'Priority', paused: 'Paused' };
const TONE = { working: 'good', paused: 'warn', noRoad: 'warn', noResource: 'warn', noInput: 'warn', noCrew: 'warn' };
const NO_DEMOLISH = { townHall: 'The Town Hall cannot be demolished.', royalCharter: 'The Royal Charter cannot be demolished.' };
const NO_STAFF = { royalCharter: 'The Royal Charter has no workers to assign.' };
const NAME_OVERRIDE = { mine: 'Iron Mine' };
const DEPOSIT_WORD = { forest: 'timber', stone: 'stone', iron: 'iron' };
const PRIORITY_TIP = 'Staffing: Normal, Priority or Paused. Priority workers are assigned first at dawn. ' +
  'Paused stops the building; its upkeep is still due.';

const dec = (n) => String(Math.round(Number(n) * 10) / 10);
const cap = (s) => (s ? s.charAt(0).toUpperCase() + s.slice(1) : '');
// TileView.buildable holds display names in the sim (section 7.3 says keys). A camel-case key becomes words; a name passes through.
const keyName = (k) => (/^[a-z][A-Za-z]*$/.test(k) ? NAME_OVERRIDE[k] || cap(k.replace(/([A-Z])/g, ' $1')) : k);

function costText(cost) {
  const parts = RES.filter((k) => cost && cost[k] > 0).map((k) => fmt(cost[k]) + ' ' + k);
  return parts.length ? parts.join(', ') : 'nothing';
}

// Why an upgrade cannot be bought now, or null: a tier lock keeps the sim's text; else "Needs 10 goods (have 3)" for the
// first short resource in stock order (as canAfford). kv is the kingdom view.
function upgradeWhy(u, tier, kv) {
  if (u.owned || u.available) return null;
  const short = kv && tier <= kv.tier.id ? RES.find((k) => u.cost[k] > kv.stock[k].have) : null;
  return short ? 'Needs ' + fmt(u.cost[short]) + ' ' + short + ' (have ' + fmt(kv.stock[short].have) + ')' : u.reason || null;
}

// "Ada, Bram, and 2 more" for a {count, names} group from the building view.
function people(group) {
  if (!group.names.length) return '';
  const more = group.count - group.names.length;
  return group.names.join(', ') + (more > 0 ? ', and ' + more + ' more' : '');
}

// kv: the kingdom view, read only when an upgrade is still open (its stock and tier say why it cannot be bought).
function buildingNodes(h, v, kv) {
  const out = [h('p', { class: TONE[v.status] || null }, v.statusText)];
  if (v.stage === 'building') out.push(h('p', null, 'Done in ' + plural(v.daysLeft, 'day') + '.'));
  if (v.production) {
    const f = v.factors;
    out.push(h('p', null, 'Output: ' + dec(v.production.perDayNow) + ' ' + v.production.resource + ' a day now, ' +
      dec(v.production.perDayFull) + ' at full crew.'));
    out.push(h('p', { class: 'muted' }, 'Factors: crew ' + pct(f.crew) + ', haul ' + pct(f.haul) + ', season ' +
      pct(f.season) + ', weather ' + pct(f.weather) + ', upgrades ' + pct(f.upgrade) + '.'));
  }
  if (v.crewNeeded > 0) {
    const who = people(v.workers);
    out.push(h('p', null, 'Workers: ' + v.crew + ' of ' + v.crewNeeded + (who ? ' (' + who + ')' : '') + '.'));
  }
  out.push(h('p', null, 'Upkeep: ' + dec(v.upkeep) + ' gold a day.'));
  if (v.beds > 0) {
    const who = people(v.residents);
    out.push(h('p', null, 'Residents: ' + v.residents.count + ' of ' + v.beds + ' beds' + (who ? ' (' + who + ')' : '') + '.'));
  }
  if (v.connected && v.roadSteps > 0) out.push(h('p', { class: 'muted' }, 'Road: ' + v.roadSteps + ' steps from the Town Hall.'));
  if (!v.canDemolish) out.push(h('p', { class: 'warn' }, NO_DEMOLISH[v.type] || 'This building cannot be demolished.'));
  if (!v.crewNeeded) out.push(h('p', { class: 'muted' }, NO_STAFF[v.type] || 'No workers are needed here, so staffing does not apply.'));
  if (v.upgrades && v.upgrades.length) out.push(h('h3', null, 'Upgrades'));
  for (const u of v.upgrades || []) {
    const cost = costText(u.cost);
    const row = kv ? kv.upgrades.find((x) => x.key === u.key) : null;
    const why = u.owned ? null : upgradeWhy(u, row ? row.tier : 0, kv);
    out.push(h('div', null, h('p', null, u.name + ': ' + u.text + ' Cost: ' + cost + '.'),
      h('button', { type: 'button', 'data-act': 'upgrade', 'data-key': u.key, disabled: u.owned || !!why,
        title: u.owned ? 'Already bought. ' + u.text : u.text + ' Cost: ' + cost + '.' + (why ? ' ' + why + '.' : ''),
        'aria-label': u.owned ? u.name + ' bought' : 'Buy ' + u.name + ' for ' + cost + (why ? '. ' + why : '') },
      u.owned ? 'Bought' : why || 'Buy ' + u.name)));
  }
  return out;
}

// typeOf(name) gives the building key for a buildable display name, or null (R1-07).
function tileNodes(h, t, typeOf) {
  const out = [];
  if (!t.explored) out.push(h('p', { class: 'muted' }, 'This area is fogged. Scout it to see what is here.'));
  if (t.fertility !== null && t.fertility !== undefined) out.push(h('p', null, 'Fertility: ' + pct(t.fertility) + '.'));
  if (t.deposit > 0) out.push(h('p', null, 'Left to take: ' + fmt(t.deposit) + ' ' + (DEPOSIT_WORD[t.terrain] || 'resource') + '.'));
  if (t.road === 'none') {
    out.push(h('p', null, 'Road: none. ' + (t.canRoad.ok ? 'A road can go here.' : t.canRoad.reason + '.')));
  } else {
    out.push(h('p', null, (t.road === 'bridge' ? 'Bridge' : 'Road') +
      (t.connected ? ', connected to the Town Hall.' : ', not connected to the Town Hall.')));
  }
  if (t.buildingId) out.push(h('p', null, 'Building here: ' + t.buildingName + '.'));
  const buildable = t.buildable || [];
  if (buildable.length) {
    out.push(h('p', null, 'You can build here:'), h('ul', null, buildable.map((name) => {
      const type = typeOf(name);
      const text = 'Build ' + name + ' here';
      return h('li', null, type ? h('button', { type: 'button', 'data-act': 'place', 'data-type': type,
        title: 'Place a ' + name + ' on this tile.', 'aria-label': text }, text) : name);
    })));
  } else if (!t.buildingId) out.push(h('p', { class: 'muted' }, 'Nothing can be built on this tile yet.'));
  return out;
}

// Element factory bound to a document: h(tag, attrs, ...kids). Attributes set to false, null or undefined are skipped.
function factory(doc) {
  return function h(tag, attrs, ...kids) {
    const node = doc.createElement(tag);
    if (tag === 'p') node.setAttribute('style', 'margin:3px 0');
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

export function mountInfoCard(ctx) {
  const { doc, els, controller, actions } = ctx;
  const h = factory(doc);
  const panel = els['panel-info'];
  const title = els['info-title'];
  const body = els['info-body'];
  const prio = els['info-priority'];
  const focus = els['info-focus'];
  const demolish = els['info-demolish'];
  const DEMOLISH = { text: demolish.textContent, title: demolish.getAttribute('title'), label: demolish.getAttribute('aria-label') };
  let sel = null; // {kind: 'tile', x, y} or {kind: 'building', id}, or null
  let view = null; // the BuildingView or TileView for sel, from the last update
  // TileView.buildable holds display names (queries.js), so each name maps back to its building key. The keys come from the
  // kingdom view, and keyName turns each key into the display name the sim uses.
  let keyOf = null;
  const typeOf = (name) => {
    if (!keyOf) keyOf = new Map(Object.keys(controller.getKingdomView().buildingCounts).map((t) => [keyName(t), t]));
    return keyOf.get(name) || null;
  };

  function hideCard() {
    sel = null;
    view = null;
    panel.hidden = true;
  }

  function paintBody(nodes) {
    const fresh = doc.createElement('div');
    for (const n of nodes) fresh.appendChild(n);
    morphKids(body, fresh);
  }

  function renderNow() {
    const isTile = sel.kind === 'tile';
    title.textContent = isTile ? cap(view.terrain) + ' at ' + view.x + ', ' + view.y : view.name + ' (#' + view.id + ')';
    const kv = !isTile && (view.upgrades || []).some((u) => !u.owned) ? controller.getKingdomView() : null;
    paintBody(isTile ? tileNodes(h, view, typeOf) : buildingNodes(h, view, kv));
    prio.hidden = isTile;
    focus.hidden = isTile;
    demolish.hidden = isTile;
    if (!isTile) {
      // A disabled control says why on the control itself, and in its title and aria-label.
      const noStaff = !view.crewNeeded;
      const staffWhy = NO_STAFF[view.type] || 'No workers are needed here, so staffing does not apply.';
      prio.textContent = noStaff ? 'No workers' : LABEL[view.priority] || 'Normal';
      prio.setAttribute('aria-label', noStaff ? 'Staffing priority: no workers here. ' + staffWhy : 'Staffing priority: ' + prio.textContent);
      prio.setAttribute('title', noStaff ? staffWhy : PRIORITY_TIP);
      prio.disabled = noStaff;
      const noDemolish = !view.canDemolish;
      const demolishWhy = NO_DEMOLISH[view.type] || 'This building cannot be demolished.';
      demolish.textContent = noDemolish ? 'Cannot demolish' : DEMOLISH.text;
      demolish.setAttribute('title', noDemolish ? demolishWhy : DEMOLISH.title);
      demolish.setAttribute('aria-label', noDemolish ? 'Demolish this building: ' + demolishWhy : DEMOLISH.label);
      demolish.disabled = noDemolish;
    }
  }

  // s: {kind: 'tile', x, y}, {kind: 'building', id} or null. The card fills in on the next update().
  function show(s) {
    if (!s || (s.kind !== 'tile' && s.kind !== 'building')) {
      hideCard();
      return;
    }
    sel = s;
    view = null;
    title.textContent = '';
    paintBody([]);
    prio.hidden = true;
    focus.hidden = true;
    demolish.hidden = true;
    panel.hidden = false;
  }

  // v: the view for the current selection (getBuildingView or getTileView). null means the subject is gone.
  function update(v) {
    if (!sel) return;
    if (!v) {
      controller.select(null);
      hideCard();
      return;
    }
    view = v;
    renderNow();
  }

  prio.addEventListener('click', () => {
    if (!sel || sel.kind !== 'building' || !view) return;
    controller.dispatch({ type: 'setPriority', id: view.id, value: NEXT[view.priority] || 'normal' });
  });
  focus.addEventListener('click', () => {
    if (!sel || sel.kind !== 'building' || !view) return;
    ctx.renderer.camera.focusTile(Math.floor(view.x + view.w / 2), Math.floor(view.y + view.h / 2));
  });
  demolish.addEventListener('click', async () => {
    if (!sel || sel.kind !== 'building' || !view || !view.canDemolish) return;
    const v = view;
    const ok = await actions.confirm('Demolish ' + v.name + '? Refund: ' + costText(v.demolishRefund) + '.');
    if (!ok) return;
    const r = controller.dispatch({ type: 'demolish', id: v.id });
    if (r && r.ok && sel && sel.kind === 'building' && sel.id === v.id) {
      controller.select(null);
      hideCard();
    }
  });
  els['info-close'].addEventListener('click', () => {
    controller.select(null);
    hideCard();
  });
  body.addEventListener('click', (e) => {
    const b = pick(e.target, body, 'data-act');
    const act = b && b.getAttribute('data-act');
    if (act === 'upgrade') controller.dispatch({ type: 'buyUpgrade', key: b.getAttribute('data-key') });
    else if (act === 'place' && sel && sel.kind === 'tile' && view) {
      controller.dispatch({ type: 'placeBuilding', buildingType: b.getAttribute('data-type'), x: view.x, y: view.y, rot: 0 });
    }
  });

  panel.hidden = true;
  return { show, update };
}
