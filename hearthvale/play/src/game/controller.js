// owner: app
// Section 9.7: the controller. It owns the kingdom, the clock, the tools and the frame loop. Only this module calls
// advanceDays, speed and dayFrac, and only it writes saves (through storage.js, inside try/catch).
import { TIME, SaveError, createNewGame, advanceDays, applyCommand, serializeState, deserializeState, getBuildingView,
  getPlacementPreview, getRoadPlan, getKingdomView, getObjective, getSeasonInfo } from '../sim/index.js';
import { idx, inBounds } from '../sim/state.js';
import { BUILDINGS } from '../config/buildings.js';
import { ECONOMY } from '../config/economy.js';
import { MAP } from '../config/map.js';
import { RESOURCE_KEYS } from '../config/resources.js';

// Presentation values, not balance. src/config holds only sim tables, so they are named here.
const DT_CAP = 0.25, UPDATE_EVERY = 0.25, AUTOSAVE_EVERY = 60, BACKDROP_SEED = 2026, TITLE_SPIN = 0.05;
const HOME_DIST = 34, OPEN_DIST = 60, GLIDE = 1.5, HOME_SECONDS = 1, TURN_STEP = 0.3, ZOOM_STEP = 0.85, PUFFS = 12;
const FRAME_REACH = 8;   // tiles: a marker this far from the Show me site pulls the view back to HOME_DIST
const SEED_MAX = 4294967295, RANDOM_SEED_MAX = 999999;
const TOOLS = ['select', 'build', 'road', 'demolish', 'scout'];
const CUE_FOR_COMMAND = new Map([['placeBuilding', 'build'], ['placeRoad', 'build'], ['trade', 'coin'],
  ['acceptOffer', 'coin'], ['buyUpgrade', 'coin'], ['festival', 'festival']]);
const CUE_FOR_EVENT = new Map([['milestone', 'coin'], ['harvest', 'harvest'], ['citizenBorn', 'birth'], ['tier', 'tier'],
  ['season', 'season'], ['plagueStart', 'plague'], ['festival', 'festival'], ['harvestFair', 'festival']]);
const TEXT = {
  noKingdom: 'Start a new kingdom first.', noSave: 'There is no saved kingdom yet.', saved: 'Game saved.',
  noKingdomToSave: 'There is no kingdom to save yet. Start a new kingdom first.',
  damaged: 'That save file is damaged and cannot be loaded.', backup: 'Latest save was damaged. Loaded the save before it.',
  manualBackup: 'Manual save was damaged. Loaded the latest save instead.',
  loaded: 'Kingdom loaded. The clock is paused.',
  firstRoad: 'Lay the road from the Town Hall to the gold ring to start the clock.',
  clockRunning: 'Clock running. Space pauses.', paused: 'Clock paused. Space resumes.',
  save: 'The kingdom could not be saved.', start: 'The kingdom could not be started.',
  storage: 'Browser storage could not be used.',
  seed: 'The seed must be a whole number from 0 to 4,294,967,295, or empty for a random seed.',
};
const DEMOLISH_NO = { townHall: 'The Town Hall cannot be demolished', royalCharter: 'The Royal Charter cannot be demolished' };
const ROAD_IDLE = 'Drag from empty grass to lay road. Rivers become bridges.';

const isBuilding = (t) => typeof t === 'string' && Object.hasOwn(BUILDINGS, t);
const sameTile = (a, b) => (a && b ? a.x === b.x && a.y === b.y : a === b);
const sentence = (s) => (/[.!?]$/.test(String(s).trim()) ? String(s).trim() : `${String(s).trim()}.`);
const count = (n, word) => `${n} ${word}${n === 1 ? '' : 's'}`;
const costText = (c) => RESOURCE_KEYS.filter((k) => c && c[k] > 0).map((k) => `${c[k]} ${k}`).join(', ') || 'nothing';
const result = (ok, reason, message) => (ok ? { ok, reason: null, message } : { ok, reason });
const bad = (reason) => ({ ok: false, reason });

// Which sound plays for a sim event (section 9.10).
function cueFor(ev) {
  if (ev.type === 'raid') return ev.kind === 'bad' ? 'raid' : 'good';
  if (ev.type === 'outcome') return ev.kind === 'good' ? 'win' : ev.kind === 'bad' ? 'lose' : null;
  if (CUE_FOR_EVENT.has(ev.type)) return CUE_FOR_EVENT.get(ev.type);
  return ['good', 'warn', 'bad'].includes(ev.kind) ? ev.kind : null;
}

export function createController({ canvas, renderer, storage, audio, doc, confirm }) {
  const win = doc.defaultView;
  const cam = renderer.camera;
  const listeners = new Map();
  let state = null, mode = 'title', speed = 0, lastSpeed = 1, dayAcc = 0, clock = 0;
  // A new kingdom waits at speed 0 for its first road. It is released once: when the Objective step moves past step 1,
  // or by a speed choice.
  let awaitingRoad = false;
  let tool = 'select', toolType = null, rot = 0, selection = null, hover = null;
  // Two holds on the red-spot reason in the tool hint. A refused placement keeps its reason: refusal = {reason, x, y} for
  // the refused tile, shown while the pointer stays on that tile. It ends at the next successful action or when the pointer
  // enters another tile. A tool change does not end it. A successful action hides the preview's red reason on reasonTile
  // (the tile the pointer was on; null when it was off the map) until the pointer enters another tile. A refusal always
  // shows its reason again.
  let refusal = null, reasonHidden = false, reasonTile = null;
  // R2-01: the last successful placement, {type, name, x, y}. The hint names it while the pointer stays on that tile.
  let placed = null;
  let ghost = null, roadPreview = null, roadPlan = null, hint = '', cache = { kingdom: null, objective: null };
  let pending = [], fps = 60, advanceMs = 0, drawCalls = 0, started = false, rafId = 0, last = null;
  let updateAcc = 0, autoAcc = 0, autoWarned = false, settleAt = null;

  const emit = (name, payload) => {
    for (const fn of [...(listeners.get(name) || [])]) {
      try { fn(payload); } catch (err) { console.error(err); }
    }
  };
  const say = (kind, text) => emit('toast', { kind, text });
  const refuse = (reason) => (say('bad', reason), bad(reason));
  const inPlay = () => mode === 'play' && ['playing', 'sandbox'].includes(state.outcome.status);
  const over = () => state !== null && ['won', 'lost'].includes(state.outcome.status);
  const buildingId = (t) => state.map.building[idx(state, t.x, t.y)];
  // Hides the red-spot reason until the pointer enters a tile other than reasonTile (see setHover).
  function hideReason() {
    reasonHidden = true;
    reasonTile = hover ? { x: hover.x, y: hover.y } : null;
  }
  // Storage calls never throw out of here: a failure becomes a reason.
  const stored = (fn) => {
    try {
      const r = fn();
      return r && typeof r === 'object' ? r : { ok: false, reason: null };
    } catch (err) {
      return bad(TEXT.storage);
    }
  };

  // R2-01: manual is the manual save (Save, Ctrl+S, the pause menu), which has its own slot. Otherwise it is the autosave,
  // which writes the latest slot only, so it never overwrites the manual save.
  function writeSave(manual) {
    let text;
    try { text = serializeState(state); } catch (err) { return bad(TEXT.save); }
    const r = stored(() => (manual ? storage.writeManual(text) : storage.writeSave(text)));
    return r.ok ? { ok: true } : bad(r.reason || TEXT.save);
  }

  function autosave() {
    const r = writeSave(false);
    if (!r.ok && !autoWarned) {
      autoWarned = true;
      say('warn', `Autosave did not work. ${r.reason}`);
    }
  }

  // A stored save decoded: {ok, state}, or {ok: false, reason} with the SaveError message when the save is damaged.
  function decode(text) {
    try {
      return { ok: true, state: deserializeState(text) };
    } catch (err) {
      return bad(err instanceof SaveError ? err.message : TEXT.damaged);
    }
  }

  // Continue (R2-01) reads the latest save, the newest write. When it is damaged, the save before it is read, with a warning.
  // The latest save's error stands otherwise.
  function readLatest() {
    const latest = stored(() => storage.readSave());
    if (!latest.ok) return bad(latest.reason || TEXT.noSave);
    const first = decode(latest.value);
    if (first.ok) return first;
    const prev = stored(() => storage.readPrev());
    const before = prev.ok ? decode(prev.value) : null;
    return before && before.ok ? { ...before, notice: TEXT.backup } : first;
  }

  // Load (R2-01) reads the manual save. With none yet it reads the latest save, which is what the Load button checks for.
  // A damaged manual save gives way to the latest save, with a warning.
  function readManualOrLatest() {
    const manual = stored(() => storage.readManual());
    if (!manual.ok) return readLatest();
    const first = decode(manual.value);
    if (first.ok) return first;
    const latest = readLatest();
    return latest.ok ? { ...latest, notice: TEXT.manualBackup } : first;
  }

  const setMode = (next) => {
    if (mode !== next) {
      mode = next;
      emit('mode', next);
    }
  };
  const setSpeedRaw = (n) => {
    if (speed !== n) {
      speed = n;
      emit('speed', n);
    }
  };
  function setSpeed(n) {
    if (!Number.isInteger(n) || n < 0 || n >= TIME.speeds.length || mode !== 'play' || (n > 0 && over())) return;
    if (n > 0) lastSpeed = n;
    if (n !== speed) {
      if (awaitingRoad && n > 0) say('good', TEXT.clockRunning);   // a new kingdom's first clock start gets one toast
      awaitingRoad = false;   // the player has chosen the clock, so the first-road start no longer applies
    }
    setSpeedRaw(n);
  }
  function togglePause() {
    if (mode !== 'play') return;
    if (speed === 0) setSpeed(lastSpeed || 1);
    else { lastSpeed = speed; setSpeedRaw(0); }
  }
  // A raid warning stops the clock at every speed (1x, 2x and 3x), so the player can react. The warn toast stays. Space
  // resumes at the speed that was running. Caravans and the other events never call this.
  // R2-01: the clock stops with a line that says how to resume. Space returns to lastSpeed, the speed that was running.
  function pauseForWarning() {
    if (speed === 0) return;
    lastSpeed = speed;
    setSpeedRaw(0);
    say('info', TEXT.paused);
  }

  // The ghost or the road preview for the hovered tile.
  function refreshPreview() {
    ghost = null;
    roadPreview = null;
    roadPlan = null;
    if (mode !== 'play' || !hover) return;
    if (tool === 'build' && toolType) {
      const p = getPlacementPreview(state, toolType, hover.x, hover.y, rot);
      ghost = { type: toolType, x: hover.x, y: hover.y, rot, ok: p.ok, reason: p.ok ? null : p.reason };
    } else if (tool === 'road') {
      roadPlan = getRoadPlan(state, hover.x, hover.y);
      roadPreview = (roadPlan.ok ? roadPlan.points : [hover]).map((p) => ({ x: p.x, y: p.y, ok: roadPlan.ok }));
    }
  }

  function scoutReason(x, y) {
    if (state.map.explored[idx(state, x, y)] === 1) return 'That area is already explored';
    let near = Infinity;
    state.map.explored.forEach((e, j) => {
      if (e === 1) near = Math.min(near, Math.max(Math.abs((j % state.width) - x), Math.abs(Math.floor(j / state.width) - y)));
    });
    if (near > ECONOMY.scoutRange) return `Scouts can only reach ${ECONOMY.scoutRange} tiles beyond your land`;
    return state.stock.gold < ECONOMY.scoutCost ? `Scouting costs ${ECONOMY.scoutCost} gold; you have ${state.stock.gold}` : null;
  }

  // The tool hint line: what the tool does, or the reason for a red spot. A refusal's reason comes first while it is held
  // (refusal). While reasonHidden (after a successful action), a red spot shows the tool's plain line instead of its reason.
  function hintText() {
    if (mode !== 'play') return '';
    if (refusal && hover && sameTile(hover, refusal)) return sentence(refusal.reason);
    if (tool === 'build') {
      if (!toolType) return 'Pick a building in the Build panel, then click a tile.';
      const name = BUILDINGS[toolType].name;
      const turn = 'The Rotate button or G turns it.';
      // R2-01: the tile is occupied after a placement, so the hint names the next action, not the move-over line.
      if (placed && placed.type === toolType && hover && sameTile(hover, placed)) {
        return `Placed the ${placed.name}. Click another empty tile to place again, or press Select.`;
      }
      if (!ghost || (!ghost.ok && reasonHidden)) return `Move over the valley to place the ${name}. ${turn}`;
      return ghost.ok ? `Click to place the ${name}. ${turn}` : sentence(ghost.reason);
    }
    if (tool === 'road') {
      if (!roadPlan) return ROAD_IDLE;
      if (!roadPlan.ok) return reasonHidden ? ROAD_IDLE : sentence(roadPlan.reason);
      if (roadPlan.costReason) return reasonHidden ? ROAD_IDLE : sentence(roadPlan.costReason);
      return `Click to lay ${count(roadPlan.length, 'road tile')} for ${roadPlan.cost.wood} wood.`;
    }
    if (tool === 'demolish') {
      const idle = 'Click a building to demolish it. You get half its cost back.';
      if (!hover) return idle;
      const id = buildingId(hover);
      const v = id > 0 ? getBuildingView(state, id) : null;
      if (v && v.canDemolish) return `Click to demolish the ${v.name}. You get half its cost back.`;
      if (reasonHidden) return idle;
      return v ? sentence(DEMOLISH_NO[v.type]) : 'Nothing to demolish on this tile.';
    }
    if (tool === 'scout') {
      const idle = `Click the fog to scout it for ${ECONOMY.scoutCost} gold.`;
      if (!hover) return idle;
      const why = scoutReason(hover.x, hover.y);
      if (!why) return `Click to scout this area for ${ECONOMY.scoutCost} gold.`;
      return reasonHidden ? idle : sentence(why);
    }
    return 'Click a building or a tile to see what it is.';
  }

  // Kingdom views are read once per update tick, so the frame never waits on them. A new kingdom's clock starts once: on
  // the first tick where the Objective view's step is past step 1, which means the first road is done (section 7.7). The
  // clock is paused until then, so the step has to move on the road command itself, not at dawn.
  function refreshCache() {
    cache.kingdom = getKingdomView(state);
    cache.objective = cache.kingdom.objective;
    if (awaitingRoad && cache.objective.step > 1) {
      awaitingRoad = false;
      if (inPlay() && speed === 0) { setSpeedRaw(1); say('good', TEXT.clockRunning); }
    }
    refreshPreview();
    hint = hintText();
  }

  function introGlide() {
    cam.zoomBy(OPEN_DIST / HOME_DIST);
    cam.focusTile(MAP.hall.x, MAP.hall.y, GLIDE);
    settleAt = clock + GLIDE;
  }

  // Makes a new or loaded state the current kingdom, paused. The tool, selection and hover reset.
  function adopt(next) {
    state = next;
    tool = 'select'; toolType = null; rot = 0; hover = null; selection = null; refusal = null; reasonHidden = false;
    reasonTile = null; placed = null;
    pending = []; dayAcc = 0; autoAcc = 0; settleAt = null; awaitingRoad = false;
    renderer.setState(state);
    setMode('play');
    refreshCache();
    emit('selection', null);
    emit('tool', { tool, type: toolType, cause: 'reset' });
    setSpeedRaw(0);
  }

  // manual: Load (the manual save first). Otherwise Continue (the latest save). Either way the kingdom is adopted paused.
  function loadKingdom(manual) {
    const r = manual ? readManualOrLatest() : readLatest();
    emit('loaded', r.ok ? { ok: true } : { ok: false, reason: r.reason });
    if (!r.ok) return refuse(r.reason);
    adopt(r.state);
    say(r.notice ? 'warn' : 'good', r.notice || TEXT.loaded);
    return result(true, null, TEXT.loaded);
  }

  // Manual save (Save button, Ctrl+S, pause menu). Success is a good toast. With no kingdom in play it is an info toast,
  // because there is nothing to save. A storage failure is a bad toast with its reason.
  function saveGame() {
    if (mode !== 'play') {
      say('info', TEXT.noKingdomToSave);
      emit('saved', { ok: false, reason: TEXT.noKingdomToSave });
      return result(false, TEXT.noKingdomToSave);
    }
    const r = writeSave(true);
    if (r.ok) say('good', TEXT.saved);
    else say('bad', r.reason);
    emit('saved', r.ok ? { ok: true } : { ok: false, reason: r.reason });
    return r.ok ? result(true, null, TEXT.saved) : result(false, r.reason);
  }

  function newGame(seed) {
    const s = seed === null || seed === undefined ? 1 + Math.floor(Math.random() * RANDOM_SEED_MAX) : seed;
    if (!Number.isInteger(s) || s < 0 || s > SEED_MAX) return refuse(TEXT.seed);
    let next;
    try { next = createNewGame({ seed: s }); } catch (err) { return refuse(TEXT.start); }
    adopt(next);
    awaitingRoad = true;   // paused until the first road is laid (DESIGN section 2)
    introGlide();
    say('good', `A new kingdom begins in the valley (seed ${s}).`);
    say('info', TEXT.firstRoad);
    return result(true, null, `New kingdom started (seed ${s}).`);
  }

  // The visual events for a placement: one dust puff per tile, at most PUFFS along a road.
  function placedEvents(cmd) {
    const pts = cmd.type === 'placeBuilding' ? [cmd] : cmd.points || [cmd];
    const step = Math.max(1, Math.ceil(pts.length / PUFFS));
    return pts.filter((_, i) => i % step === 0).map((p) => ({ type: 'placed', kind: 'info', text: '', day: state.day, x: p.x, y: p.y }));
  }

  // The tile a placement aims at: the single tile, or the last point of a road path (the target, section 3.4).
  const aimOf = (cmd) => (Array.isArray(cmd.points) && cmd.points.length > 0 ? cmd.points[cmd.points.length - 1] : cmd);

  // Every command from the tools and panels. The objective step is read before and after each one. The tutorial's step
  // checks run inside a placement or a sale (checkTutorial, through applyCommand), and their events never reach the
  // controller. So a successful command that moved the step gets its one toast here, with the banner the dawn pass would
  // use (section 9.7). A skip sets the step to 7 but is not a move: its own message is the toast. The dawn pass toasts only
  // the moves it makes itself, so no change is toasted twice.
  function dispatch(cmd) {
    if (mode !== 'play') return refuse(TEXT.noKingdom);
    const type = cmd && cmd.type;
    const placing = type === 'placeBuilding' || type === 'placeRoad';
    const stepBefore = getObjective(state).step;
    const r = applyCommand(state, cmd);
    if (r.ok) {
      const stepAfter = getObjective(state);
      refusal = null;
      hideReason();   // a successful action ends the refusal and hides the red-spot reason on this tile until the pointer moves
      if (r.message) say('good', r.message);
      if (CUE_FOR_COMMAND.has(type)) audio.play(CUE_FOR_COMMAND.get(type));
      if (type === 'festival') pending.push({ type, kind: 'good', text: r.message, day: state.day });
      if (placing) pending.push(...placedEvents(cmd));
      // One good toast when the step moved forward, after the command's own message. A command that finishes several steps
      // shows the final banner once. A skip is excluded: it sets the step to 7 with skipped set, and its message is its toast.
      if (stepAfter.step > stepBefore && !stepAfter.skipped) { say('good', stepAfter.banner); audio.play('good'); }
      // R2-01: the hint names the placed building while the pointer stays on its tile (hintText, setHover). A demolish clears
      // the tile again, so the hint no longer applies.
      if (type === 'placeBuilding' && isBuilding(cmd.buildingType)) {
        placed = { type: cmd.buildingType, name: BUILDINGS[cmd.buildingType].name, x: cmd.x, y: cmd.y };
      } else if (type === 'demolish') {
        placed = null;
      }
      // A placement keeps the building armed: the tool and its type stay, and the event says why it was sent (section 9.7).
      if (type === 'placeBuilding' && tool === 'build') emit('tool', { tool, type: toolType, cause: 'placed' });
      if (type === 'continueSandbox') setSpeed(1);
    } else {
      say('bad', r.reason);
      audio.play('error');
      reasonHidden = false;   // a refusal always shows its reason
      if (placing) {
        const at = Array.isArray(cmd.points) && cmd.points[0] ? cmd.points[0] : cmd;
        pending.push({ type: 'refused', kind: 'info', text: r.reason, day: state.day, x: at.x, y: at.y });
        const aim = aimOf(cmd);
        refusal = { reason: r.reason, x: aim.x, y: aim.y };   // held in the tool hint until the next success or a move
      }
    }
    refreshPreview();
    return r;
  }

  // A click, or the release of a road drag, with the current tool on tile (x, y).
  function click(tile) {
    if (mode !== 'play' || !tile) return;
    const { x, y } = tile;
    const id = buildingId(tile);
    if (tool === 'select') select(id > 0 ? { kind: 'building', id } : { kind: 'tile', x, y });
    else if (tool === 'build') { if (toolType) dispatch({ type: 'placeBuilding', buildingType: toolType, x, y, rot }); }
    else if (tool === 'road') {
      const plan = getRoadPlan(state, x, y);
      dispatch(plan.ok ? { type: 'placeRoad', points: plan.points } : { type: 'placeRoad', x, y });
    } else if (tool === 'demolish') {
      const v = id > 0 ? getBuildingView(state, id) : null;
      if (!v) dispatch({ type: 'demolish', id: 0 });
      else if (!v.canDemolish) dispatch({ type: 'demolish', id: v.id });
      else confirm(`Demolish ${v.name}? Refund: ${costText(v.demolishRefund)}.`).then((yes) => yes && dispatch({ type: 'demolish', id: v.id }));
    } else if (tool === 'scout') dispatch({ type: 'scout', x, y });
  }

  function select(sel) {
    let next = null;
    if (sel && sel.kind === 'tile' && Number.isInteger(sel.x) && Number.isInteger(sel.y) && inBounds(state, sel.x, sel.y)) {
      next = { kind: 'tile', x: sel.x, y: sel.y };
    } else if (sel && sel.kind === 'building' && Number.isInteger(sel.id) && sel.id > 0) {
      next = { kind: 'building', id: sel.id };
    }
    selection = next;
    emit('selection', next);
  }

  // Entering another tile ends both holds on the red-spot reason (see refusal and reasonHidden).
  function setHover(tile) {
    const valid = mode === 'play' && tile && Number.isInteger(tile.x) && Number.isInteger(tile.y);
    const next = valid ? { x: tile.x, y: tile.y } : null;
    if (reasonHidden && next && !sameTile(next, reasonTile)) reasonHidden = false;
    if (refusal && next && !sameTile(next, refusal)) refusal = null;
    if (placed && !sameTile(next, placed)) placed = null;   // R2-01: the placement hint ends when the pointer moves
    if (!sameTile(next, hover)) { hover = next; refreshPreview(); }
  }

  // Sets the tool and emits it. cause says why the tool moved: 'placed' when a placement keeps the building armed (emitted by
  // dispatch, the tool does not change), 'reset' when a new or loaded kingdom takes over, null otherwise. main.js reads it.
  // A tool change does not touch the refusal reason, so it stays on screen.
  function applyTool(name, asked, cause) {
    tool = name;
    toolType = name === 'build' && isBuilding(asked) ? asked : null;
    refreshPreview();
    emit('tool', { tool, type: toolType, cause });
  }

  // A build tool keeps its type when it is opened again without one.
  function setTool(name, opts) {
    if (!TOOLS.includes(name)) return;
    const asked = opts && typeof opts === 'object' && 'type' in opts ? opts.type : tool === 'build' ? toolType : null;
    applyTool(name, asked, null);
  }

  // Show me (7.7): centre on the step's site, the marker to build on. Another marker farther than FRAME_REACH tiles
  // from it (the Hall door, on step 1) pulls the view back to HOME_DIST, so every marker stays in the frame.
  function focusObjective() {
    const markers = cache.objective ? cache.objective.markers : [];
    const site = markers.find((m) => m.kind === 'site') || markers[0];
    if (!site) { cam.focusTile(MAP.hall.x, MAP.hall.y, GLIDE); return; }
    cam.focusTile(site.x, site.y, GLIDE);
    const reach = Math.max(...markers.map((m) => Math.max(Math.abs(m.x - site.x), Math.abs(m.y - site.y))));
    if (reach > FRAME_REACH && cam.distance() < HOME_DIST) cam.zoomBy(HOME_DIST / cam.distance());
  }

  function cameraAction(name) {
    if (name === 'left') cam.rotateBy(-TURN_STEP);
    else if (name === 'right') cam.rotateBy(TURN_STEP);
    else if (name === 'in') cam.zoomBy(ZOOM_STEP);
    else if (name === 'out') cam.zoomBy(1 / ZOOM_STEP);
    else if (name === 'home') cam.focusTile(MAP.hall.x, MAP.hall.y, HOME_SECONDS);
    else if (name === 'focusObjective') focusObjective();
  }

  // Runs whole days while the clock is running (section 9.7). Returns the sim events of this frame.
  function advance(dt) {
    const events = [];
    const t0 = performance.now();
    dayAcc += dt * TIME.speeds[speed];
    for (let ran = 0; dayAcc >= 1 && ran < TIME.maxDaysPerFrame; ran++) {
      const evs = advanceDays(state, 1);
      dayAcc -= 1;
      events.push(...evs);
      emit('day', evs);
      let warned = false;
      for (const ev of evs) {
        if (ev.kind !== 'info') say(ev.kind, ev.text);
        if (ev.type === 'raidWarning') warned = true;
        const cue = cueFor(ev);
        if (cue) audio.play(cue);
      }
      // The warn toast stays up. The clock stops here, and no further day runs in this frame.
      if (warned) pauseForWarning();
      if (over() || warned) break;
    }
    if (dayAcc >= 1) dayAcc = 0.999;
    advanceMs = performance.now() - t0;
    if (over()) {
      setSpeedRaw(0);
      const o = state.outcome;
      emit('outcome', { status: o.status, reason: o.reason, day: o.day, causes: o.causes.slice() });
    }
    return events;
  }

  function frame(now) {
    rafId = win.requestAnimationFrame(frame);
    const real = last === null ? 0 : Math.max(0, (now - last) / 1000);
    last = now;
    const dt = Math.min(DT_CAP, real);
    clock += dt;
    if (settleAt !== null && clock >= settleAt) { settleAt = null; cam.zoomBy(HOME_DIST / OPEN_DIST); }
    if (mode === 'title') cam.rotateBy(TITLE_SPIN * dt);
    if (real > 0) fps += (1 / real - fps) * 0.1;
    const events = inPlay() ? advance(dt) : [];
    updateAcc += dt;
    if (updateAcc >= UPDATE_EVERY) {
      updateAcc = 0;
      refreshCache();
      emit('update', { kingdom: cache.kingdom, objective: cache.objective, speed, tool, toolType, hint });
    }
    autoAcc += real;
    if (autoAcc >= AUTOSAVE_EVERY) {
      autoAcc = 0;
      if (inPlay()) autosave();
    }
    const queued = pending;
    pending = [];
    renderer.frame({
      state, dt, time: clock, dayFrac: dayAcc, hover: mode === 'play' ? hover : null,
      selectedId: selection && selection.kind === 'building' ? selection.id : null, ghost, roadPreview,
      // The armed building (section 9.1, change R1-15): {state, type} while the Build tool is on with a type, else null.
      // It uses the same play gate as the ghost, so the armed dots and the ghost agree.
      armed: mode === 'play' && tool === 'build' && toolType ? { state, type: toolType } : null,
      markers: mode === 'play' && cache.objective ? cache.objective.markers : [],
      events: events.concat(queued), speed, season: getSeasonInfo(state).season,
    });
    drawCalls = renderer.stats().drawCalls;
  }

  return {
    // Shows the title over a backdrop kingdom: not advanced, camera turning slowly, the opening glide.
    start() {
      if (started) return;
      started = true;
      state = createNewGame({ seed: BACKDROP_SEED });
      renderer.setState(state);
      refreshCache();
      introGlide();
      emit('mode', mode);
      rafId = win.requestAnimationFrame(frame);
    },
    newGame, continueGame: () => loadKingdom(false), loadGame: () => loadKingdom(true), saveGame, setSpeed, togglePause,
    dispatch, setTool,
    rotateGhost() { rot = (rot + 1) % 4; refreshPreview(); },
    select, hover: setHover, click, cameraAction,
    getState: () => state,
    getKingdomView: () => getKingdomView(state),
    perf: () => ({ fps: Math.round(fps), advanceMs, drawCalls, day: state ? state.day : 0 }),
    on(name, fn) {
      if (typeof fn !== 'function') return () => {};
      if (!listeners.has(name)) listeners.set(name, new Set());
      listeners.get(name).add(fn);
      return () => listeners.get(name)?.delete(fn);
    },
    dispose() {
      if (rafId) win.cancelAnimationFrame(rafId);
      rafId = 0;
      started = false;
      listeners.clear();
    },
  };
}
