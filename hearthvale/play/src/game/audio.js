// owner: app
// Section 9.10 and DESIGN section 12: every cue is synthesized with WebAudio, so there are no audio files. The
// AudioContext is created by unlock() on the first pointer down. Mute is saved through storage.writeSettings.

const MAX_VOICES = 8;   // at most eight cues sound at once (DESIGN section 12)
const MASTER = 0.5;     // master gain when sound is on

// One oscillator envelope. Returns the time it ends, in seconds from its start.
function tone(ac, out, t, { type, from, to = from, at = 0, dur, vol }) {
  const o = ac.createOscillator();
  const g = ac.createGain();
  const s = t + at;
  o.type = type;
  o.frequency.setValueAtTime(from, s);
  if (to !== from) o.frequency.exponentialRampToValueAtTime(to, s + dur);
  g.gain.setValueAtTime(0.0001, s);
  g.gain.exponentialRampToValueAtTime(vol, s + Math.min(0.01, dur / 4));
  g.gain.exponentialRampToValueAtTime(0.0001, s + dur);
  o.connect(g);
  g.connect(out);
  o.start(s);
  o.stop(s + dur + 0.02);
  return at + dur;
}

// A short burst of white noise with a decaying envelope (the build thud).
function burst(ac, out, t, dur, vol) {
  const n = Math.max(1, Math.floor(ac.sampleRate * dur));
  const buf = ac.createBuffer(1, n, ac.sampleRate);
  const data = buf.getChannelData(0);
  for (let i = 0; i < n; i++) data[i] = Math.random() * 2 - 1;
  const src = ac.createBufferSource();
  const g = ac.createGain();
  src.buffer = buf;
  g.gain.setValueAtTime(vol, t);
  g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
  src.connect(g);
  g.connect(out);
  src.start(t);
  src.stop(t + dur + 0.02);
  return dur;
}

const seq = (ac, out, t, list) => Math.max(0, ...list.map((s) => tone(ac, out, t, s)));
const arpeggio = (ac, out, t, freqs, step, type) =>
  seq(ac, out, t, freqs.map((f, i) => ({ type, from: f, at: i * step, dur: 0.22, vol: 0.12 })));
const chord = (ac, out, t, freqs, bend, type) =>
  seq(ac, out, t, freqs.map((f) => ({ type, from: f, to: f * bend, dur: 0.9, vol: 0.07 })));

// Each cue takes (context, output, start time) and returns how long it sounds.
const CUES = {
  click: (ac, o, t) => seq(ac, o, t, [{ type: 'square', from: 1200, dur: 0.015, vol: 0.05 }]),
  build: (ac, o, t) => Math.max(
    seq(ac, o, t, [{ type: 'sine', from: 90, to: 60, dur: 0.25, vol: 0.3 }]),
    burst(ac, o, t, 0.12, 0.08),
  ),
  coin: (ac, o, t) => seq(ac, o, t, [
    { type: 'square', from: 988, dur: 0.06, vol: 0.07 },
    { type: 'square', from: 1319, at: 0.06, dur: 0.06, vol: 0.07 },
  ]),
  harvest: (ac, o, t) => seq(ac, o, t, [{ type: 'triangle', from: 660, to: 990, dur: 0.3, vol: 0.18 }]),
  good: (ac, o, t) => seq(ac, o, t, [
    { type: 'triangle', from: 880, dur: 0.08, vol: 0.16 },
    { type: 'sine', from: 1760, at: 0.08, dur: 0.3, vol: 0.1 },
  ]),
  warn: (ac, o, t) => seq(ac, o, t, [
    { type: 'square', from: 440, dur: 0.09, vol: 0.09 },
    { type: 'square', from: 440, at: 0.14, dur: 0.09, vol: 0.09 },
  ]),
  bad: (ac, o, t) => seq(ac, o, t, [{ type: 'sawtooth', from: 90, to: 60, dur: 0.35, vol: 0.12 }]),
  error: (ac, o, t) => seq(ac, o, t, [{ type: 'sawtooth', from: 220, to: 180, dur: 0.12, vol: 0.1 }]),
  raid: (ac, o, t) => seq(ac, o, t, [
    { type: 'sawtooth', from: 110, to: 70, dur: 0.6, vol: 0.16 },
    { type: 'sawtooth', from: 196, at: 0.1, dur: 0.45, vol: 0.07 },
    { type: 'sawtooth', from: 294, at: 0.1, dur: 0.45, vol: 0.05 },
  ]),
  plague: (ac, o, t) => seq(ac, o, t, [{ type: 'sine', from: 110, to: 98, dur: 0.8, vol: 0.16 }]),
  birth: (ac, o, t) => seq(ac, o, t, [
    { type: 'sine', from: 1046, dur: 0.6, vol: 0.12 },
    { type: 'sine', from: 2093, dur: 0.4, vol: 0.04 },
  ]),
  festival: (ac, o, t) => arpeggio(ac, o, t, [523, 659, 784, 1046], 0.09, 'triangle'),
  tier: (ac, o, t) => arpeggio(ac, o, t, [523, 659, 784, 1046], 0.1, 'triangle'),
  win: (ac, o, t) => chord(ac, o, t, [523, 659, 784], 1.06, 'triangle'),
  lose: (ac, o, t) => chord(ac, o, t, [392, 311, 262], 0.94, 'sine'),
  season: (ac, o, t) => seq(ac, o, t, [
    { type: 'sine', from: 1318, dur: 0.5, vol: 0.09 },
    { type: 'sine', from: 1567, at: 0.12, dur: 0.4, vol: 0.06 },
  ]),
};

export function createAudio({ storage }) {
  let ctx = null;
  let master = null;
  let muted = readMuted();
  let busy = [];   // end times (AudioContext seconds) of the cues still sounding

  function readMuted() {
    try {
      const r = storage.readSettings();
      return !!(r && r.value && r.value.sound === false);
    } catch (err) {
      return false;
    }
  }

  // Creates the context once. Returns null when WebAudio is missing or refuses to start.
  function context() {
    if (ctx) return ctx;
    const Make = globalThis.AudioContext || globalThis.webkitAudioContext;
    if (!Make) return null;
    try {
      ctx = new Make();
      master = ctx.createGain();
      master.gain.value = muted ? 0 : MASTER;
      master.connect(ctx.destination);
    } catch (err) {
      ctx = null;
      master = null;
    }
    return ctx;
  }

  function unlock() {
    const ac = context();
    if (ac && ac.state === 'suspended') ac.resume().catch(() => {});
  }

  function play(cue) {
    const make = Object.prototype.hasOwnProperty.call(CUES, cue) ? CUES[cue] : null;
    if (!make || muted) return;
    const ac = context();
    if (!ac || ac.state === 'closed') return;
    const now = ac.currentTime;
    busy = busy.filter((end) => end > now);
    if (busy.length >= MAX_VOICES) return;
    try {
      busy.push(now + make(ac, master, now));
    } catch (err) {
      // a cue that fails to synthesize stays silent
    }
  }

  function setMuted(next) {
    muted = !!next;
    if (master) master.gain.value = muted ? 0 : MASTER;
    try {
      storage.writeSettings({ sound: !muted });
    } catch (err) {
      // the setting still applies for this visit
    }
  }

  return {
    unlock,
    play,
    toggleMute: () => setMuted(!muted),
    isMuted: () => muted,
    setMuted,
  };
}
