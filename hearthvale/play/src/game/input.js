// owner: app
// Section 9.8: pointer, wheel and keyboard input. Game changes go through the controller and the UI actions. Camera
// moves call renderer.camera directly, because the camera is view state, not game state.

const DRAG_PX = 5;             // a press that moves less than this is a click (section 9.8)
const ROTATE_PER_PX = 0.01;    // radians per pixel of right-drag (section 9.2)
const WHEEL_BASE = 1.1;        // wheel zoom factor is WHEEL_BASE ** (delta / 100) (section 9.2)
const KEY_ZOOM = 1.15;         // one + or - press
const KEY_PAN = 0.4;           // held pan speed, in camera distances per second
const KEY_TURN = 1.6;          // held Q and E, radians per second
const MAX_STEP = 0.25;         // longest step used for held keys, seconds
const PAN_KEYS = new Map([['KeyW', [0, 1]], ['ArrowUp', [0, 1]], ['KeyS', [0, -1]], ['ArrowDown', [0, -1]],
  ['KeyA', [-1, 0]], ['ArrowLeft', [-1, 0]], ['KeyD', [1, 0]], ['ArrowRight', [1, 0]]]);
const TOOL_KEYS = new Map([['KeyR', 'road'], ['KeyV', 'scout'], ['KeyX', 'demolish']]);
const NOT_TEXT = /^(button|checkbox|radio|range|submit|reset|color|file)$/;

// Game keys are ignored while focus is in a text field (the seed box, for one).
const typing = (t) => !!t && (t.isContentEditable || t.tagName === 'TEXTAREA' || t.tagName === 'SELECT' ||
  (t.tagName === 'INPUT' && !NOT_TEXT.test(t.type)));

// R2-01: a button inside an open overlay or panel takes Space and Enter itself (section 9.8). The overlays and panels are the
// elements whose ids start with overlay- or panel- (section 9.9); the hidden attribute marks one that is closed.
const isButton = (t) => !!t && t.tagName === 'BUTTON';
const isPanelButton = (t) => {
  if (!isButton(t)) return false;
  const panel = t.closest('[id^="overlay-"], [id^="panel-"]');
  return panel !== null && !panel.hidden;
};

export function bindInput({ canvas, controller, renderer, doc, actions }) {
  const win = doc.defaultView;
  const cam = () => renderer.camera;
  const held = new Set();
  let tool = 'select';           // follows the controller's tool events
  let mode = 'title';            // follows the controller's mode events
  let hoverTile = null;
  let press = null;              // {id, button, x, y, ax, ay, moved}: ax, ay is the last point the view followed
  let last = null;               // timestamp of the previous frame, null before the first
  let spaceHeld = false;         // R2-01: a Space press paused or resumed the clock; its keyup must not click a button
  let raf = 0;
  const offs = [
    controller.on('tool', (t) => { tool = t.tool; }),
    controller.on('mode', (m) => { mode = m; }),
  ];

  // A pixel moves the view by the ground distance it covers at the target depth (the view spans 2 d tan(fov/2)).
  function panPixels(dx, dy) {
    const c = cam();
    const per = (2 * Math.tan((c.three.fov * Math.PI) / 360) * c.distance()) / Math.max(1, canvas.clientHeight);
    c.panBy(-dx * per, dy * per);
  }

  function onDown(e) {
    if (press) return;
    press = { id: e.pointerId, button: e.button, x: e.clientX, y: e.clientY, ax: e.clientX, ay: e.clientY, moved: false };
    if (e.button === 1) e.preventDefault();
    try {
      canvas.setPointerCapture(e.pointerId);
    } catch (err) {
      // capture is optional; the drag still works inside the canvas
    }
  }

  function onMove(e) {
    hoverTile = renderer.pickTile(e.clientX, e.clientY);
    controller.hover(hoverTile);
    if (!press || press.id !== e.pointerId) return;
    if (!press.moved && Math.hypot(e.clientX - press.x, e.clientY - press.y) >= DRAG_PX) press.moved = true;
    if (!press.moved) return;
    const dx = e.clientX - press.ax;
    const dy = e.clientY - press.ay;
    if (press.button === 2) cam().rotateBy(dx * ROTATE_PER_PX);
    else if (press.button === 1 || (press.button === 0 && tool !== 'road')) panPixels(dx, dy);
    else return;   // a road drag only moves the preview
    press.ax = e.clientX;
    press.ay = e.clientY;
  }

  function onUp(e) {
    if (!press || press.id !== e.pointerId) return;
    const p = press;
    press = null;
    if (p.button === 0 && (!p.moved || tool === 'road')) {
      controller.click(renderer.pickTile(e.clientX, e.clientY));
    } else if (p.button === 2 && !p.moved) {
      if (tool !== 'select') controller.setTool('select');
      else controller.select(null);
    }
  }

  function onCancel(e) {
    if (press && press.id === e.pointerId) press = null;
  }

  function onLeave() {
    if (!press) {
      hoverTile = null;
      controller.hover(null);
    }
  }

  function onWheel(e) {
    e.preventDefault();
    cam().zoomBy(WHEEL_BASE ** (e.deltaY / 100));
  }

  function onKey(e) {
    if (typing(e.target) || e.altKey) return;
    const code = e.code;
    if (e.ctrlKey || e.metaKey) {
      if (code === 'KeyS' || code === 'KeyL') {
        e.preventDefault();
        if (code === 'KeyS') controller.saveGame();
        else controller.loadGame();
      }
      return;
    }
    if (PAN_KEYS.has(code) || code === 'KeyQ' || code === 'KeyE') {
      held.add(code);
      e.preventDefault();
      return;
    }
    if (code === 'Equal' || code === 'NumpadAdd') {
      e.preventDefault();
      cam().zoomBy(1 / KEY_ZOOM);
      return;
    }
    if (code === 'Minus' || code === 'NumpadSubtract') {
      e.preventDefault();
      cam().zoomBy(KEY_ZOOM);
      return;
    }
    // R2-01: Space pauses or resumes in play (section 9.8). A focused button outside an open overlay or panel must not also
    // click on this press, so the press is consumed here, held repeats included. A button inside an open panel keeps Space.
    if (code === 'Space' && mode === 'play' && !isPanelButton(e.target)) {
      e.preventDefault();
      spaceHeld = true;
      if (!e.repeat) controller.togglePause();
      return;
    }
    if (e.repeat) return;
    if (code === 'Escape') {
      e.preventDefault();
      actions.escape();
      return;
    }
    if (code === 'F3') {
      e.preventDefault();
      actions.toggleDebug();
      return;
    }
    if (code === 'KeyH') {
      actions.showHelp();
      return;
    }
    if (code === 'KeyM') {
      actions.toggleMute();
      return;
    }
    if (code === 'Home') {
      e.preventDefault();
      controller.cameraAction('home');
      return;
    }
    if (mode !== 'play') return;
    // A focused button takes Enter itself, so the game does not act twice (a toolbar button still works from the keyboard).
    // A button inside an open panel takes Space too (R2-01: Space elsewhere pauses, above).
    if ((code === 'Enter' && isButton(e.target)) || (code === 'Space' && isPanelButton(e.target))) return;
    if (code === 'Enter') {
      e.preventDefault();
      controller.click(hoverTile);
    } else if (code === 'Digit1' || code === 'Digit2' || code === 'Digit3') {
      controller.setSpeed(Number(code.slice(5)));
    } else if (code === 'KeyB') {
      actions.toggleBuild();
    } else if (code === 'KeyK') {
      actions.toggleKingdom();
    } else if (code === 'KeyP') {
      actions.toggleKingdom('policies');
    } else if (code === 'KeyT') {
      actions.toggleKingdom('market');
    } else if (code === 'KeyG') {
      controller.rotateGhost();
    } else if (code === 'KeyF') {
      controller.cameraAction('focusObjective');
    } else if (TOOL_KEYS.has(code)) {
      const want = TOOL_KEYS.get(code);
      controller.setTool(tool === want ? 'select' : want);
    }
  }

  function onKeyUp(e) {
    held.delete(e.code);
    // R2-01: the keyup of a Space press that paused or resumed the clock must not click the focused button (Firefox clicks
    // a button on keyup, so the keydown's preventDefault alone is not enough).
    if (e.code === 'Space' && spaceHeld) {
      spaceHeld = false;
      e.preventDefault();
    }
  }

  // Held keys pan and turn the camera every frame.
  function tick(now) {
    raf = win.requestAnimationFrame(tick);
    const dt = last === null ? 0 : Math.min(MAX_STEP, Math.max(0, (now - last) / 1000));
    last = now;
    if (held.size === 0) return;
    let px = 0;
    let py = 0;
    let turn = 0;
    for (const code of held) {
      const v = PAN_KEYS.get(code);
      if (v) {
        px += v[0];
        py += v[1];
      } else if (code === 'KeyQ') {
        turn -= 1;
      } else if (code === 'KeyE') {
        turn += 1;
      }
    }
    const c = cam();
    if (px !== 0 || py !== 0) {
      const step = KEY_PAN * c.distance() * dt;
      c.panBy(px * step, py * step);
    }
    if (turn !== 0) c.rotateBy(turn * KEY_TURN * dt);
  }

  const onContext = (e) => e.preventDefault();
  const onBlur = () => {
    held.clear();
    spaceHeld = false;   // a keyup lost to the blur must not leave the flag set
  };
  canvas.addEventListener('pointerdown', onDown);
  canvas.addEventListener('pointermove', onMove);
  canvas.addEventListener('pointerup', onUp);
  canvas.addEventListener('pointercancel', onCancel);
  canvas.addEventListener('pointerleave', onLeave);
  canvas.addEventListener('wheel', onWheel, { passive: false });
  canvas.addEventListener('contextmenu', onContext);
  doc.addEventListener('keydown', onKey);
  doc.addEventListener('keyup', onKeyUp);
  win.addEventListener('blur', onBlur);
  raf = win.requestAnimationFrame(tick);

  return {
    dispose() {
      canvas.removeEventListener('pointerdown', onDown);
      canvas.removeEventListener('pointermove', onMove);
      canvas.removeEventListener('pointerup', onUp);
      canvas.removeEventListener('pointercancel', onCancel);
      canvas.removeEventListener('pointerleave', onLeave);
      canvas.removeEventListener('wheel', onWheel);
      canvas.removeEventListener('contextmenu', onContext);
      doc.removeEventListener('keydown', onKey);
      doc.removeEventListener('keyup', onKeyUp);
      win.removeEventListener('blur', onBlur);
      win.cancelAnimationFrame(raf);
      for (const off of offs) off();
    },
  };
}
