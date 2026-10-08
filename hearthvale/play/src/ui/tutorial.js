// owner: ui-panels
// Objective banner (ARCHITECTURE 9.6): step, banner, next line, progress bar, the "Show me" button and world labels.
// Labels sit just above their marker tiles, clear of the gold ring, and follow the camera every animation frame while markers exist.
// Show me flashes the labels once the camera glide ends. A new step, or a new kingdom, pulses its tool button.
import { pct } from './format.js';

// A target is a site under construction: the label says no action is needed (R1-09).
const LABEL = { door: 'Start here', site: 'Build here', target: 'Under construction' };
const LABEL_STYLE = 'position:absolute;left:0;top:0;transform:translate(-50%,-130%);padding:3px 9px;' +
  'border-radius:999px;background:var(--amber);color:var(--on-amber);font:600 13px/1.2 var(--font-text);' +
  'white-space:nowrap;box-shadow:var(--shadow);pointer-events:none;';
// Each label sits this many CSS pixels above its tile centre, so the whole gold ring shows under it (presentation only).
const LIFT_PX = 24;
// The "Step N of 6:" that opens each TUTORIAL banner (config/milestones.js). The counter is shown once, in #objective-step.
const STEP_PREFIX = /^Step \d+ of \d+:\s*/;
// Added to step 1's next line while the clock waits for the road (R1-09; the clock starts when the road is done, 9.7).
const CLOCK_LINE = 'The clock starts when this road is done.';

// Timing in ms (the glide is the controller's GLIDE, 1.5 s) and colours from DESIGN section 11.
const GLIDE_MS = 1500, FLASH_MS = 3000, PULSE_MS = 700;
const REDUCED = '(prefers-reduced-motion: reduce)';
const PARCHMENT = '#f4ecd8', AMBER = '#e0a23b', CLEAR = 'rgba(224,162,59,0)';
// Frames set the outline colour and, unless reduced, the scale. scale is its own CSS property, so a label keeps its
// translate transform.
const RING = { outlineStyle: 'solid', outlineWidth: '3px', outlineOffset: '2px' };
const FLASH = [{ scale: 1, outlineColor: CLEAR, offset: 0 }, { scale: 1.2, outlineColor: PARCHMENT, offset: 0.12 },
  { scale: 1.08, outlineColor: PARCHMENT, offset: 0.25 }, { scale: 1.08, outlineColor: PARCHMENT, offset: 0.8 },
  { scale: 1, outlineColor: CLEAR, offset: 1 }];
const PULSE = [{ scale: 1, outlineColor: CLEAR }, { scale: 1.12, outlineColor: AMBER, offset: 0.5 },
  { scale: 1, outlineColor: CLEAR }];
// Reduced motion: the same outline, held still, with no scale.
const STILL_FLASH = [{ outlineColor: PARCHMENT }, { outlineColor: PARCHMENT }];
const STILL_PULSE = [{ outlineColor: AMBER }, { outlineColor: AMBER }];

export function mountTutorial(ctx) {
  const { doc, els, controller } = ctx;
  const win = doc.defaultView || null;
  const layer = els['world-markers'];
  const banner = els['objective'];
  const pool = [];
  let placed = [];
  let renderer = null;
  let frame = 0;
  let flashTimer = 0;
  let flashes = [];
  let pulses = [];
  let shownStep = 0;
  let shownGame = null;

  els['objective-show'].addEventListener('click', () => {
    controller.cameraAction('focusObjective');
    clearTimeout(flashTimer);
    flashes.forEach((a) => a.cancel());
    flashes = [];
    flashTimer = setTimeout(flashLabels, GLIDE_MS);
  });

  // The banner belongs to a running kingdom. It starts hidden (the title screen) and update() shows it once an
  // objective arrives. The hidden attribute also takes the Show me button out of the tab order while hidden.
  function setBannerShown(shown) {
    const hidden = !shown;
    if (banner.hidden !== hidden) banner.hidden = hidden;
  }
  setBannerShown(false);

  // Moves each placed label to its tile on screen, LIFT_PX above the tile centre. Labels whose tile is off screen are hidden.
  function place() {
    if (!renderer || typeof renderer.worldToScreen !== 'function') return;
    for (const m of placed) {
      const p = renderer.worldToScreen(m.x, m.y);
      const left = p.x + 'px';
      const top = (p.y - LIFT_PX) + 'px';
      m.label.hidden = !p.visible;
      if (m.label.style.left !== left) m.label.style.left = left;
      if (m.label.style.top !== top) m.label.style.top = top;
    }
  }

  function loop() {
    frame = 0;
    if (!placed.length || !win) return;
    place();
    frame = win.requestAnimationFrame(loop);
  }

  function labelAt(i) {
    if (!pool[i]) {
      const el = doc.createElement('div');
      el.className = 'world-label';
      el.style.cssText = LABEL_STYLE;
      el.hidden = true;
      layer.appendChild(el);
      pool[i] = el;
    }
    return pool[i];
  }

  function setLabels(markers, r) {
    if (r) renderer = r;
    const list = (Array.isArray(markers) ? markers : []).filter((m) => LABEL[m.kind]);
    placed = list.map((m, i) => {
      const label = labelAt(i);
      if (label.textContent !== LABEL[m.kind]) label.textContent = LABEL[m.kind];
      return { label, x: m.x, y: m.y };
    });
    pool.forEach((el, i) => {
      if (i >= placed.length) el.hidden = true;
    });
    place();
    if (placed.length && win && !frame) frame = win.requestAnimationFrame(loop);
  }

  // Reduced motion is read at each cue, so a changed system setting applies to the next cue.
  const reduced = () => !!(win && win.matchMedia && win.matchMedia(REDUCED).matches);
  // One element.animate() cue with the ring style in every frame. Null when the browser has no Web Animations API.
  const cue = (el, frames, options) => (el && el.animate
    ? el.animate(frames.map((f) => ({ ...RING, ...f })), { fill: 'none', ...options }) : null);

  // Show me: every visible label gets a bright outline and a short scale-up, for about 3 s.
  function flashLabels() {
    flashTimer = 0;
    const frames = reduced() ? STILL_FLASH : FLASH;
    const live = placed.filter((m) => !m.label.hidden);
    flashes = live.map((m) => cue(m.label, frames, { duration: FLASH_MS })).filter(Boolean);
  }

  // A new step pulses its tool button three times: step 1 the Road button, steps 2 to 6 the Build button.
  function pulse(el) {
    const a = reduced() ? cue(el, STILL_PULSE, { duration: PULSE_MS * 3 })
      : cue(el, PULSE, { duration: PULSE_MS, iterations: 3 });
    if (a) pulses.push(a);
  }
  function stopPulses() {
    pulses.forEach((a) => a.cancel());
    pulses = [];
  }

  // The next line. While step 1 waits for the road (speed 0), it says the clock starts when the road is done. The speed is
  // read from the pressed speed button, which hud.js sets on every update, so this module needs no speed argument.
  function nextText(o) {
    const base = (o.done ? o.goal : o.next) || '';
    const waiting = !o.done && o.step === 1 && els['speed-0'].getAttribute('aria-pressed') === 'true';
    return waiting ? (base ? base.replace(/[.!?]?\s*$/, '. ') : '') + CLOCK_LINE : base;
  }

  // objective: Objective from the KingdomView (section 7.7), or null when no kingdom is running. Without one the
  // banner and its world labels are hidden. renderer: the renderer, for worldToScreen.
  function update(o, r) {
    if (!o) {
      setBannerShown(false);
      setLabels([], r);
      stopPulses();
      shownStep = 0;
      shownGame = null;
      return;
    }
    setBannerShown(true);
    els['objective-step'].textContent = o.title || '';
    // The counter is already in #objective-step, so the banner's own "Step N of 6:" prefix is not written again.
    els['objective-text'].textContent = String(o.banner || '').replace(STEP_PREFIX, '');
    els['objective-next'].textContent = nextText(o);
    const frac = o.total > 0 ? Math.min(1, o.step / o.total) : 0;
    els['objective-bar'].style.width = pct(frac);
    // The controller replaces the state object on a new, continued or loaded kingdom, which also starts a step.
    const game = controller.getState();
    if (o.step !== shownStep || game !== shownGame) {
      shownStep = o.step;
      shownGame = game;
      stopPulses();
      if (!o.done) pulse(els[o.step === 1 ? 'btn-road' : 'btn-build']);
    }
    setLabels(o.markers, r);
  }

  return { update };
}
