// owner: app
// Section 9.10: boot. Checks WebGL and the page ids, builds the modules, wires controller events to the UI, binds input,
// and sets the ?debug=1 hook. Only this file connects the modules to each other.
import { collectEls } from './ui/dom.js';
import { mountHud } from './ui/hud.js';
import { mountToasts } from './ui/toasts.js';
import { mountMenus } from './ui/menus.js';
import { mountBuildMenu } from './ui/buildMenu.js';
import { mountInfoCard } from './ui/infoCard.js';
import { mountKingdomPanel } from './ui/kingdomPanel.js';
import { mountTutorial } from './ui/tutorial.js';
import { createRenderer } from './render/renderer.js';
import { createController } from './game/controller.js';
import { bindInput } from './game/input.js';
import { createStorage } from './game/storage.js';
import { createAudio } from './game/audio.js';
import { advanceDays, getBuildingView, getTileView, getPlacementPreview, getObjective, getKingdomView,
  getCatalog } from './sim/index.js';

const WEBGL_TEXT = 'This game needs WebGL. Try current Chrome, Edge or Firefox with hardware acceleration on.';

function showBoot(doc, text) {
  const start = doc.getElementById('overlay-start');
  const overlay = doc.getElementById('overlay-boot');
  const msg = doc.getElementById('boot-message');
  if (start) start.hidden = true;
  if (msg) msg.textContent = text;
  if (overlay) overlay.hidden = false;
  else doc.body.textContent = text;
}

function hasWebGL(doc) {
  try {
    const probe = doc.createElement('canvas');
    return !!(probe.getContext('webgl2') || probe.getContext('webgl'));
  } catch (err) {
    return false;
  }
}

function launch(doc, els) {
  const win = doc.defaultView;
  const canvas = els['game-canvas'];
  const storage = createStorage(win);
  const audio = createAudio({ storage });
  const renderer = createRenderer(canvas);
  const ui = {};
  let mode = 'title', tool = 'select', speed = 0, selection = null, debugOn = false;
  const viewOf = (sel) => (sel.kind === 'building' ? getBuildingView(controller.getState(), sel.id)
    : getTileView(controller.getState(), sel.x, sel.y));
  // The first Market's view, for the Kingdom panel's worker line (null when none stands).
  const marketViewOf = () => {
    const s = controller.getState();
    const m = s.buildings.find((b) => b.type === 'market');
    return m ? getBuildingView(s, m.id) : null;
  };

  // Cross-panel actions (section 9.10), called by keys, buttons and UI modules.
  const actions = {
    toggleBuild() {
      if (ui.buildMenu.isOpen()) {
        ui.buildMenu.close();
        if (tool === 'build') controller.setTool('select');
        return;
      }
      ui.buildMenu.update(getCatalog(controller.getState()));
      ui.buildMenu.open();
      controller.setTool('build');
    },
    toggleKingdom(tab) {
      ui.kingdomPanel.toggle(tab);
      if (ui.kingdomPanel.isOpen()) ui.kingdomPanel.update(controller.getKingdomView(), marketViewOf());
    },
    showHelp: () => ui.menus.show('help'),
    escape() {
      // Escape cancels the tool and closes the Build panel too. With the tool at select, it closes the top layer (below).
      if (tool !== 'select') {
        controller.setTool('select');
        if (ui.buildMenu.isOpen()) ui.buildMenu.close();
        return undefined;
      }
      const open = ['confirm', 'settings', 'help', 'pause'].find((n) => ui.menus.isOpen(n));
      if (open) return ui.menus.hide(open);
      if (ui.kingdomPanel.isOpen()) return ui.kingdomPanel.close();
      if (ui.buildMenu.isOpen()) return ui.buildMenu.close();
      return mode === 'play' ? ui.menus.show('pause') : undefined;
    },
    toggleMute: () => audio.toggleMute(),
    setDebug(on) {
      debugOn = !!on;
      ui.hud.setDebugVisible(debugOn);
      const r = storage.writeSettings({ debugLine: debugOn });
      if (!r.ok) ui.toasts.show('warn', r.reason);
    },
    toggleDebug: () => actions.setDebug(!debugOn),
    confirm: (text) => ui.menus.confirm(text),
  };

  const controller = createController({ canvas, renderer, storage, audio, doc,
    confirm: (text) => ui.menus.confirm(text) });
  const ctx = { doc, els, controller, renderer, audio, storage, actions };
  Object.assign(ui, {
    hud: mountHud(ctx), toasts: mountToasts(ctx), menus: mountMenus(ctx), buildMenu: mountBuildMenu(ctx),
    infoCard: mountInfoCard(ctx), kingdomPanel: mountKingdomPanel(ctx), tutorial: mountTutorial(ctx),
  });

  // Controller events drive the UI. Nothing else subscribes.
  controller.on('mode', (m) => { mode = m; doc.body.dataset.mode = m; });
  controller.on('speed', (n) => { speed = n; });
  // The Build panel closes when the player picks road, scout or demolish, and when a new or loaded kingdom takes over
  // (cause 'reset'). A placement keeps the building armed (cause 'placed') and the panel open. Escape, another tool and B
  // disarm the building, and Escape and B close the panel through actions.
  controller.on('tool', (t) => {
    tool = t.tool;
    ui.buildMenu.setSelected(t.tool === 'build' ? t.type : null);
    const pickedOther = t.tool !== 'build' && t.tool !== 'select';
    if (pickedOther || t.cause === 'reset') ui.buildMenu.close();
  });
  controller.on('selection', (sel) => {
    selection = sel;
    ui.infoCard.show(sel);
    if (sel) ui.infoCard.update(viewOf(sel));
  });
  controller.on('toast', (t) => ui.toasts.show(t.kind, t.text));
  controller.on('outcome', () => { ui.menus.hideAll(); ui.menus.show('end'); });
  controller.on('loaded', (r) => { if (r.ok) ui.menus.hideAll(); });
  controller.on('update', (p) => {
    // The title screen keeps the HUD and the objective blank; the backdrop kingdom is not shown there.
    if (mode === 'play') {
      ui.hud.update(p.kingdom, p.speed, p.tool, controller.perf(), p.hint);
      ui.tutorial.update(p.objective, renderer);
    }
    if (ui.kingdomPanel.isOpen()) ui.kingdomPanel.update(p.kingdom, marketViewOf());
    if (ui.buildMenu.isOpen()) ui.buildMenu.update(getCatalog(controller.getState()));
    if (selection) ui.infoCard.update(viewOf(selection));
    if (tool === 'build' && !ui.buildMenu.isOpen()) controller.setTool('select');
  });

  debugOn = !!storage.readSettings().value.debugLine;
  ui.hud.setDebugVisible(debugOn);
  els['btn-build'].addEventListener('click', () => actions.toggleBuild());
  els['btn-kingdom'].addEventListener('click', () => actions.toggleKingdom());
  bindInput({ canvas, controller, renderer, doc, actions });

  // Sound starts on the first gesture; every button plays the click cue.
  doc.addEventListener('pointerdown', () => audio.unlock(), { capture: true, once: true });
  doc.addEventListener('keydown', () => audio.unlock(), { capture: true, once: true });
  doc.addEventListener('click', (e) => {
    if (e.target && e.target.closest && e.target.closest('button')) audio.play('click');
  }, true);
  const resize = () => renderer.resize(canvas.clientWidth, canvas.clientHeight);
  win.addEventListener('resize', resize);
  resize();
  controller.start();

  if (new URLSearchParams(win.location.search).get('debug') === '1') {
    const st = () => controller.getState();
    win.__hearthvale = {
      get state() { return st(); },
      views: {
        kingdom: () => getKingdomView(st()),
        building: (id) => getBuildingView(st(), id),
        tile: (x, y) => getTileView(st(), x, y),
        placement: (type, x, y, rot) => getPlacementPreview(st(), type, x, y, rot),
        objective: () => getObjective(st()),
      },
      commands: {
        dispatch: (cmd) => controller.dispatch(cmd),
        // Paused only; returns the event count, or -1 while the clock runs.
        advance: (days) => (mode === 'play' && speed === 0 ? advanceDays(st(), days).length : -1),
        setSpeed: (n) => controller.setSpeed(n),
        newGame: (seed) => controller.newGame(seed),
        save: () => controller.saveGame(),
        load: () => controller.loadGame(),
        tool: (name, type) => controller.setTool(name, { type }),
      },
    };
  }
}

function boot() {
  const doc = document;
  if (!hasWebGL(doc)) return showBoot(doc, WEBGL_TEXT);
  const { els, missing } = collectEls(doc);
  if (missing.length > 0) {
    return showBoot(doc, `Hearthvale could not find these parts of the page: ${missing.join(', ')}. Reload the page.`);
  }
  try {
    launch(doc, els);
  } catch (err) {
    console.error(err);
    const text = err && err.message ? err.message : String(err);
    showBoot(doc, /webgl/i.test(text) ? WEBGL_TEXT : `Hearthvale could not start: ${text}`);
  }
  return undefined;
}

boot();
