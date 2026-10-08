// owner: ui-shell
// Start, pause, end, help, settings and confirm overlays (ARCHITECTURE 9.5). Every control works with the mouse alone.
import { fmt, signed } from './format.js';

const OVERLAYS = {
  start: 'overlay-start', pause: 'overlay-pause', end: 'overlay-end',
  help: 'overlay-help', settings: 'overlay-settings', confirm: 'overlay-confirm',
};
const NAMES = Object.keys(OVERLAYS);
const FOCUS = { start: 'btn-new', end: 'btn-end-new', help: 'help-close', settings: 'setting-sound', confirm: 'confirm-no' };
const SPEEDS = ['speed-0', 'speed-1', 'speed-2', 'speed-3'];
const SEED_MAX = 4294967295;
const RESTART_TEXT = 'Start a new kingdom? The kingdom you are playing is not saved, so its progress is lost.';

// Help content (DESIGN sections 8 and 10). Plain text, no balance numbers.
const CONTROLS = [
  ['Select, place, confirm', 'Left click', 'Enter, at the hovered tile'],
  ['Build', 'Build button, then a card, then a tile', 'B, then a card, then click'],
  ['Lay a road', 'Road button, then left-drag along tiles', 'R, then drag'],
  ['Scout', 'Scout button, then click the fog', 'V, then click'],
  ['Demolish', 'Demolish button, click a building, then confirm', 'X, then click'],
  ['Cancel a tool or close', 'Right click', 'Escape'],
  ['Pan the camera', 'Middle-drag, or left-drag with no tool', 'W, A, S, D or arrow keys'],
  ['Rotate the camera', 'Right-drag, or the camera pad', 'Q, E'],
  ['Zoom', 'Mouse wheel, or the camera pad', '+ and -'],
  ['Recentre on the Town Hall', 'Home button in the camera pad', 'Home'],
  ['Show the objective', 'Show me button', 'F'],
  ['Rotate the ghost', 'Rotate button in the build panel', 'G'],
  ['Pause and speed', 'Buttons II, 1x, 2x and 3x in the top bar', 'Space; 1, 2, 3'],
  ['Kingdom panel', 'Kingdom button', 'K (P for policies, T for market)'],
  ['Help', 'Help button', 'H'],
  ['Save and load', 'Save and Load buttons', 'Ctrl+S, Ctrl+L'],
  ['Pause menu', 'Menu button', 'Escape, with nothing open'],
  ['Mute', 'Sound button', 'M'],
];
const GOALS = [
  ['Tutorial', 'The objective banner at the top of the screen names the next step. Gold rings show where to build.'],
  ['Tiers', 'The kingdom grows from Hamlet to Village, Town and Kingdom. The Overview tab of the Kingdom panel lists what the next tier needs.'],
  ['Royal Charter', 'Build the Royal Charter at Kingdom tier to win. It needs wood, stone, iron, goods and a large gold reserve, and it takes many days to finish.'],
  ['Sandbox', 'After the Charter, the kingdom plays on with no loss checks. The Goals tab sets the next goal.'],
  ['Keeping people', 'Keep food stocked through winter, give everyone a bed, keep people in work, and keep happiness up.'],
  ['Losing', 'The kingdom ends when the valley is empty, or when happiness stays very low for too long and the people leave.'],
];
const TERMS = [
  ['Connected', 'A building or road reached by road from the Town Hall.'],
  ['Staffed', 'Has its workers.'],
  ['Upkeep', 'Gold a building costs each day. Paused buildings still cost upkeep.'],
  ['Beds', 'Places to sleep. Homeless people have no bed and sleep in a tent.'],
  ['Crew and workers', 'People assigned to a building. Builders are the unemployed adults and the Town Hall clerks who build sites.'],
  ['Priority and Paused', 'Staffing options for a building. Priority is filled first. Paused stops production.'],
  ['Haul', 'The output penalty for long roads.'],
  ['Happiness', "The kingdom's mood, moved by its causes. The People tab lists each cause."],
  ['Exodus', 'Happiness stays very low for too long, and the people leave.'],
  ['Caravan', 'A trader who brings offers for a few days.'],
  ['Raid and defence', 'Bandit attacks, and what stops them: militia, watchtowers and barracks.'],
  ['Season, weather and threats', 'Seasons, weather, plague, fire, flood and drought.'],
  ['Tier and Charter', 'Tiers are Hamlet, Village, Town and Kingdom. The Royal Charter is the building that wins the game.'],
];

export function mountMenus(ctx) {
  const { doc, els, controller, audio, storage, actions } = ctx;
  const win = doc.defaultView;
  const loadTip = els['btn-load'].title;
  let pausedSpeed = null;
  let confirmResolve = null;
  let loadPoll = 0;

  const shown = (name) => !els[OVERLAYS[name]].hidden;
  // Opening the start overlay sets data-title on body; the CSS then shows only the title panel, the hint and Help, Sound, Menu.
  const setShown = (name, open) => {
    els[OVERLAYS[name]].hidden = !open;
    if (name === 'start') doc.body.toggleAttribute('data-title', open);
  };
  const on = (id, fn) => els[id].addEventListener('click', fn);
  const ok = (r) => !!(r && r.ok);
  const reasonOf = (r, fallback) => (r && r.reason) || fallback;
  const el = (tag, cls, text) => {
    const node = doc.createElement(tag);
    if (cls) node.className = cls;
    if (text != null) node.textContent = text;
    return node;
  };
  const dl = (pairs) => {
    const list = el('dl', 'pairs');
    for (const [term, text] of pairs) list.append(el('dt', '', term), el('dd', '', text));
    return list;
  };
  const focus = (id) => {
    if (els[id]) els[id].focus({ preventScroll: true });
  };
  const setStatus = (text) => {
    els['overlay-start'].querySelector('.menu-status').textContent = text || '';
  };
  const num = (v) => signed(v, Number.isInteger(v) ? 0 : 1);
  const currentSpeed = () => {
    const n = SPEEDS.findIndex((id) => els[id].getAttribute('aria-pressed') === 'true');
    return n < 0 ? 1 : n;
  };

  // One check for a saved kingdom: {has, reason}. The reason is set only when browser storage is blocked or unreadable.
  function saveState() {
    try {
      const r = storage.readSave();
      return {
        has: !!(r && r.ok && typeof r.value === 'string' && r.value.length > 0),
        reason: r && !r.ok && r.reason ? r.reason : '',
      };
    } catch (err) {
      return { has: false, reason: 'Browser storage could not be read.' };
    }
  }

  // Load (toolbar) greys out with the same reason as Continue. Autosave can make the first save during play, so while
  // none exists, Load is checked again every second.
  function refreshLoad() {
    const { has, reason } = saveState();
    const load = els['btn-load'];
    const label = has ? 'Load' : 'Load: no saved kingdom yet';
    load.disabled = !has;
    load.setAttribute('aria-label', label);
    const tip = has ? loadTip : reason || label;
    if (load.title !== tip) load.title = tip;
    if (has && loadPoll) {
      win.clearInterval(loadPoll);
      loadPoll = 0;
    } else if (!has && !loadPoll) {
      loadPoll = win.setInterval(refreshLoad, 1000);
    }
  }

  function refreshStart() {
    const { has, reason } = saveState();
    const cont = els['btn-continue'];
    const label = has ? 'Continue' : 'Continue: no saved kingdom yet';
    Object.assign(cont, {
      disabled: !has,
      textContent: label,
      title: has ? 'Load the latest saved kingdom' : reason || 'Start and save a kingdom first',
    });
    cont.setAttribute('aria-label', label);
    const note = els['overlay-start'].querySelector('.menu-note');
    note.textContent = reason;
    note.hidden = reason === '';
    refreshLoad();
  }

  function refreshSettings() {
    let debug = false;
    try {
      const r = storage.readSettings();
      debug = !!(r && r.ok && r.value && r.value.debugLine === true);
    } catch (err) {
      debug = false;
    }
    els['setting-sound'].checked = !audio.isMuted();
    els['setting-debug'].checked = debug;
  }

  function fillEnd() {
    const kv = controller.getKingdomView();
    const o = kv.outcome || {};
    const s = kv.stats || {};
    const pop = kv.population || {};
    const won = o.status === 'won';
    els['end-title'].textContent = won ? 'The Crown is raised'
      : o.reason === 'exodus' ? 'The people have left.' : 'The valley is empty.';
    els['btn-end-sandbox'].hidden = !won;
    const body = els['end-body'];
    body.replaceChildren(
      el('p', '', won ? 'The Royal Charter is complete.' : 'The kingdom ended on ' + (kv.dateText || '') + '.'),
      dl([
        ['Tier', (kv.tier && kv.tier.name) || ''],
        ['People', fmt(pop.total) + ' now, ' + fmt(pop.peak) + ' at the peak'],
        ['Buildings finished', fmt(s.built)],
        ['Born and died', fmt(s.born) + ' born, ' + fmt(s.died) + ' died'],
        ['Raids', fmt(s.raidsRepelled) + ' repelled, ' + fmt(s.raidsLost) + ' suffered'],
        ['Gold earned', fmt(s.goldEarned)],
      ]),
    );
    const causes = Array.isArray(o.causes) ? o.causes.slice(0, 3) : [];
    if (causes.length > 0) {
      body.append(el('p', 'end-sub', 'Worst happiness causes'), dl(causes.map((c) => [c.label, num(c.value)])));
    }
  }

  // Opening the pause menu stops the clock and remembers the speed for Resume.
  function openPause() {
    if (shown('pause') || shown('start') || shown('end')) return;
    const kv = controller.getKingdomView();
    const status = kv.outcome ? kv.outcome.status : 'playing';
    if (status !== 'playing' && status !== 'sandbox') return;
    pausedSpeed = currentSpeed();
    controller.setSpeed(0);
    els['btn-pause-skip'].hidden = !!(kv.objective && kv.objective.done);
    setShown('pause', true);
    focus('btn-resume');
  }

  function closePause(resume) {
    const prev = pausedSpeed;
    pausedSpeed = null;
    setShown('pause', false);
    if (resume && prev !== null) controller.setSpeed(prev);
  }

  function closeConfirm(yes) {
    setShown('confirm', false);
    const resolve = confirmResolve;
    confirmResolve = null;
    if (resolve) resolve(yes === true);
  }

  function confirm(text) {
    closeConfirm(false);
    els['confirm-text'].textContent = text == null ? '' : String(text);
    setShown('confirm', true);
    focus(FOCUS.confirm);
    return new Promise((resolve) => {
      confirmResolve = resolve;
    });
  }

  function show(name) {
    if (!OVERLAYS[name]) return;
    // Help toggles: a second press (the Help buttons, or the H key that main.js routes through here) closes the overlay.
    if (name === 'help' && shown('help')) return hide('help');
    if (name === 'pause') return openPause();
    if (name === 'start') refreshStart();
    if (name === 'end') fillEnd();
    if (name === 'settings') refreshSettings();
    setShown(name, true);
    focus(FOCUS[name]);
  }

  function hide(name) {
    if (!OVERLAYS[name]) return;
    if (name === 'pause') closePause(true);
    else if (name === 'confirm') closeConfirm(false);
    else setShown(name, false);
  }

  // Used after a new game or a load. The controller sets the speed, so the menu does not restore one.
  function hideAll() {
    pausedSpeed = null;
    for (const name of NAMES) setShown(name, false);
    closeConfirm(false);
  }

  function startNew() {
    const raw = String(els['seed-input'].value || '').trim();
    if (raw !== '' && (!/^\d+$/.test(raw) || Number(raw) > SEED_MAX)) {
      setStatus('The seed must be a whole number from 0 to ' + fmt(SEED_MAX) + ', or empty for a random seed.');
      return;
    }
    setStatus('');
    const r = controller.newGame(raw === '' ? null : Number(raw));
    if (ok(r)) hideAll();
    else setStatus(reasonOf(r, 'The kingdom could not be started.'));
  }

  function buildHelp() {
    const rowOf = (cells, tag) => {
      const row = el('tr');
      for (const c of cells) row.append(el(tag, '', c));
      return row;
    };
    const table = el('table', 'help-table');
    table.append(el('thead'), el('tbody'));
    table.querySelector('thead').append(rowOf(['Action', 'Mouse', 'Keys'], 'th'));
    table.querySelector('tbody').append(...CONTROLS.map((cells) => rowOf(cells, 'td')));
    els['help-controls'].replaceChildren(table);
    els['help-goals'].replaceChildren(dl(GOALS));
    els['help-terms'].replaceChildren(dl(TERMS));
  }

  // Confirm is modal: Escape answers No here, before the global Escape handler cancels a tool.
  doc.addEventListener('keydown', (e) => {
    if (e.key !== 'Escape' || !shown('confirm')) return;
    e.preventDefault();
    e.stopPropagation();
    closeConfirm(false);
  }, true);

  on('btn-new', startNew);
  els['seed-input'].addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      els['btn-new'].click();
    }
  });
  on('seed-random', () => {
    els['seed-input'].value = String(Math.floor(Math.random() * (SEED_MAX + 1)));
    setStatus('');
  });
  on('btn-continue', () => {
    const r = controller.continueGame();
    if (ok(r)) {
      hideAll();
    } else {
      setStatus(reasonOf(r, 'The saved kingdom could not be loaded.'));
      refreshStart();
    }
  });
  for (const id of ['btn-howto', 'btn-help', 'btn-pause-help']) on(id, () => show('help'));
  for (const id of ['btn-settings-start', 'btn-pause-settings']) on(id, () => show('settings'));
  on('btn-menu', () => show('pause'));
  on('btn-resume', () => hide('pause'));
  on('btn-pause-save', () => controller.saveGame());
  on('btn-pause-load', () => {
    if (ok(controller.loadGame())) hideAll();
  });
  on('btn-pause-title', () => {
    closePause(false);
    show('start');
  });
  on('btn-pause-restart', () => {
    confirm(RESTART_TEXT).then((yes) => {
      if (yes && ok(controller.newGame(null))) hideAll();
    });
  });
  on('btn-pause-skip', () => {
    if (ok(controller.dispatch({ type: 'skipTutorial' }))) els['btn-pause-skip'].hidden = true;
  });
  on('btn-end-sandbox', () => {
    if (ok(controller.dispatch({ type: 'continueSandbox' }))) setShown('end', false);
  });
  on('btn-end-new', () => {
    if (ok(controller.newGame(null))) hideAll();
  });
  on('btn-end-load', () => {
    if (ok(controller.loadGame())) hideAll();
  });
  on('btn-end-title', () => {
    setShown('end', false);
    show('start');
  });
  on('help-close', () => hide('help'));
  on('settings-close', () => hide('settings'));
  on('confirm-yes', () => closeConfirm(true));
  on('confirm-no', () => closeConfirm(false));
  els['setting-sound'].addEventListener('change', () => {
    audio.toggleMute();
    els['setting-sound'].checked = !audio.isMuted();
  });
  els['setting-debug'].addEventListener('change', () => actions.setDebug(els['setting-debug'].checked));

  buildHelp();
  for (const name of NAMES) setShown(name, name === 'start');
  refreshStart();

  return {
    show,
    hide,
    hideAll,
    isOpen: (name) => OVERLAYS[name] !== undefined && shown(name),
    confirm,
  };
}
