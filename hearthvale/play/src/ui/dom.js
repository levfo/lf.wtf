// owner: ui-shell
// The static DOM ids from DESIGN section 9.9 (ARCHITECTURE 9.9). Each exists exactly once in index.html.

export const DOM_IDS = Object.freeze([
  // Stage
  'game-stage', 'game-canvas', 'world-markers', 'tooltip', 'toasts', 'debug-line', 'tool-hint', 'controls-strip',
  // Top bar (hud-status, the line under it, is in index.html and here, but not yet in ARCHITECTURE 9.9)
  'hud-top', 'hud-status', 'hud-date', 'hud-tier', 'res-food', 'res-wood', 'res-stone', 'res-iron', 'res-goods', 'res-gold',
  'hud-pop', 'hud-happy', 'speed-0', 'speed-1', 'speed-2', 'speed-3', 'btn-help', 'btn-mute', 'btn-menu',
  // Toolbar
  'toolbar', 'btn-build', 'btn-road', 'btn-scout', 'btn-demolish', 'btn-kingdom', 'btn-save', 'btn-load',
  // Objective
  'objective', 'objective-step', 'objective-text', 'objective-next', 'objective-show', 'objective-bar',
  // Camera
  'cam-pad', 'cam-rotate-left', 'cam-rotate-right', 'cam-zoom-in', 'cam-zoom-out', 'cam-home',
  // Build
  'panel-build', 'build-tabs', 'build-grid', 'build-rotate', 'build-close',
  // Info
  'panel-info', 'info-title', 'info-body', 'info-priority', 'info-focus', 'info-demolish', 'info-close',
  // Kingdom
  'panel-kingdom', 'kingdom-tabs', 'tab-overview', 'tab-people', 'tab-economy', 'tab-market', 'tab-policies',
  'tab-goals', 'tab-log', 'kingdom-body', 'kingdom-close',
  // Overlays
  'overlay-boot', 'boot-message',
  'overlay-start', 'seed-input', 'seed-random', 'btn-new', 'btn-continue', 'btn-howto', 'btn-settings-start',
  'overlay-pause', 'btn-resume', 'btn-pause-save', 'btn-pause-load', 'btn-pause-help', 'btn-pause-settings',
  'btn-pause-skip', 'btn-pause-restart', 'btn-pause-title',
  'overlay-end', 'end-title', 'end-body', 'btn-end-sandbox', 'btn-end-new', 'btn-end-load', 'btn-end-title',
  'overlay-help', 'help-close', 'help-controls', 'help-goals', 'help-terms',
  'overlay-settings', 'setting-sound', 'setting-debug', 'settings-close',
  'overlay-confirm', 'confirm-text', 'confirm-yes', 'confirm-no',
]);

// Looks up every static id. `els` is keyed by the exact id string; `missing` lists the ids that were not found.
export function collectEls(doc) {
  const els = {};
  const missing = [];
  for (const id of DOM_IDS) {
    const node = doc && typeof doc.getElementById === 'function' ? doc.getElementById(id) : null;
    if (node) els[id] = node;
    else missing.push(id);
  }
  return { els, missing };
}
