// owner: events
// Section 3.9 and section 8.13, with the values of sections 5.8 and 5.9: tiers, milestones, the six-step tutorial,
// the win and lose outcome, and the sandbox commands. Pure: no browser globals, no clock, no random source.
import { TIME } from '../config/index.js';
import { TIERS } from '../config/tiers.js';
import { MILESTONES, TUTORIAL } from '../config/milestones.js';
import { BUILDINGS, BUILDING_KEYS } from '../config/buildings.js';
import { POPULATION } from '../config/population.js';
import { emit } from './state.js';
import { connectedRoadCount } from './world.js';
import { stockAdd } from './economy.js';

// Section 5.8 thresholds that config/milestones.js does not hold yet. They move into config once foundation adds them.
const ROOF_PEOPLE = 10;
const IRON_MINED = 10;
const GOLDEN_HAPPY = 70;
const GOLDEN_DAYS = 48;
const GOLDEN_PEOPLE = 150; // the Golden Year counts only with this many people (DESIGN 7.4 sandbox goal)
const OUTCOME_CAUSES = 3; // the causes named on the end screen
const TIER_MILESTONE = ['', 'village', 'town', 'kingdom']; // milestone key set when a tier is reached (section 8.13)
const UNCOUNTED = ['townHall', 'road', 'bridge']; // not counted by the "buildings" tier check (section 5.9)
const LAST_STEP = TUTORIAL.steps.length;
// The day-20 riders warning (section 8.13). It leads with the current step's "Step N of 6:" prefix.
const RIDERS_WARNING = 'Riders were seen in the hills. Finish this step, then build a Watchtower.';

const completeCount = (state, type) => state.buildings.filter((b) => b.type === type && b.stage === 'complete').length;

// The starter network's road tiles (state.tutorialBaseline, set once at new game). A save without a valid count starts at 0.
const baselineOf = (state) => (Number.isInteger(state.tutorialBaseline) && state.tutorialBaseline > 0 ? state.tutorialBaseline : 0);

// The one road count the tutorial uses (section 5.8, step 1): connected road tiles minus the baseline, never below 0.
function tutorialRoadCount(state) {
  return Math.max(0, connectedRoadCount(state) - baselineOf(state));
}

// Road tiles step 1 still asks for. Its six connected tiles include the baseline, so the player lays six minus the
// baseline, never below 0: four more after the usual two-tile starter (DESIGN.md section 2).
function tutorialRoadNeed(state) {
  return Math.max(0, TUTORIAL.steps[0].need - baselineOf(state));
}

// Value of one tier check key (section 5.9). Happiness counts whole points, so floor(happiness) >= need is exact.
function checkHave(state, key) {
  if (key === 'pop') return state.citizens.length;
  if (key === 'buildings') return state.buildings.filter((b) => b.stage === 'complete' && !UNCOUNTED.includes(b.type)).length;
  if (key === 'happy') return Math.floor(state.happiness);
  if (key.startsWith('has:')) return completeCount(state, key.slice(4));
  if (key.startsWith('any:')) return key.slice(4).split(',').reduce((n, type) => n + completeCount(state, type), 0);
  return 0;
}

// Checks of TIERS[tierId] with what the kingdom has now (section 5.9). An unknown tier has no checks.
export function tierChecks(state, tierId) {
  const tier = TIERS[tierId];
  if (!tier) return [];
  return tier.checks.map((c) => {
    const have = checkHave(state, c.key);
    return { key: c.key, label: c.label, have, need: c.need, ok: have >= c.need };
  });
}

// Section 8.13: one tier at most per day, and tiers never drop.
export function tierDay(state, events) {
  const next = state.tier + 1;
  if (next >= TIERS.length) return;
  if (state.tier > 0 && state.tierDay === state.day) return;
  if (!tierChecks(state, next).every((c) => c.ok)) return;
  state.tier = next;
  state.tierDay = state.day;
  state.milestones[TIER_MILESTONE[next]] = state.day;
  const unlocked = BUILDING_KEYS.filter((k) => BUILDINGS[k].tier === next).map((k) => BUILDINGS[k].name);
  emit(state, events, { type: 'tier', kind: 'good', text: `Reached the ${TIERS[next].name} tier. Unlocked: ${unlocked.join(', ')}.` });
}

// Section 5.8 checks for one milestone key. Tier keys are set by tierDay, so they are checked here only as a fallback.
function milestoneMet(state, key) {
  const st = state.stats;
  const sc = state.schedule;
  const day = state.day;
  switch (key) {
    case 'founded': return state.buildings.some((b) => b.stage === 'complete' && b.type !== 'townHall');
    case 'harvest': return st.harvested >= 1;
    case 'roof': return state.citizens.length >= ROOF_PEOPLE && !state.citizens.some((c) => c.homeId === 0);
    case 'trade': return st.tradedUnits >= 1;
    case 'watch': return st.raidsRepelled >= 1;
    case 'winter': return day % TIME.daysPerYear === 0 && day > 0 && state.stock.food > 0;
    case 'lanterns': return state.festivalDay >= 0;
    case 'iron': return st.ironMined >= IRON_MINED;
    case 'mending': return sc.plagueMendingDay >= 0;
    case 'village': return state.tier >= TIERS[1].id;
    case 'town': return state.tier >= TIERS[2].id;
    case 'kingdom': return state.tier >= TIERS[3].id;
    case 'golden': return sc.goldenDays >= GOLDEN_DAYS;
    case 'crown': return state.outcome.status === 'won' || state.outcome.status === 'sandbox';
    default: return false;
  }
}

// Section 8.13: the sandbox Golden Year counter, then one-time awards in config order, each paid through stockAdd.
// The counter rises only on sandbox days with GOLDEN_PEOPLE people or more and happiness at GOLDEN_HAPPY or more;
// any other day resets it to 0.
export function milestonesDay(state, events) {
  const sc = state.schedule;
  const goldenToday = state.outcome.status === 'sandbox' && state.happiness >= GOLDEN_HAPPY && state.citizens.length >= GOLDEN_PEOPLE;
  sc.goldenDays = goldenToday ? sc.goldenDays + 1 : 0;
  for (const m of MILESTONES) {
    if (state.milestones[m.key] !== undefined || !milestoneMet(state, m.key)) continue;
    state.milestones[m.key] = state.day;
    if (m.gold > 0) state.stats.goldEarned += stockAdd(state, 'gold', m.gold, events);
    emit(state, events, { type: 'milestone', kind: 'good', text: `Milestone: ${m.name}. +${m.gold} gold.`, amount: m.gold });
  }
}

// Section 5.8 step completion checks.
function stepDone(state, step) {
  switch (step) {
    case 1: return tutorialRoadCount(state) >= tutorialRoadNeed(state);
    case 2: return state.buildings.some((b) => b.type === 'farm');
    case 3: return completeCount(state, 'cottage') >= TUTORIAL.steps[2].need;
    case 4: return state.buildings.some((b) => b.type === 'lumberCamp' && b.stage === 'complete' && b.crew >= 1);
    case 5: return completeCount(state, 'market') > 0 && state.tutorial.tradeDone;
    case 6: return state.buildings.some((b) => b.type === 'watchtower' && b.stage === 'complete' && b.crew >= 1);
    default: return false;
  }
}

// {have, need} of a counted step's next line, with have capped at need. Step 1 counts road tiles, step 3 finished cottages.
function stepCount(state, id) {
  const need = id === 1 ? tutorialRoadNeed(state) : TUTORIAL.steps[id - 1].need;
  const have = id === 1 ? tutorialRoadCount(state) : completeCount(state, 'cottage');
  return { have: Math.min(have, need), need };
}

// Moves the tutorial one step when the current step's check passes (section 8.13). Finishing step 6 ends the tutorial.
// Emits the tutorial event for the move and returns true; returns false and changes nothing otherwise.
function advanceStep(state, events) {
  const t = state.tutorial;
  if (t.done || t.step > LAST_STEP || !stepDone(state, t.step)) return false;
  if (t.step === LAST_STEP) {
    t.step = LAST_STEP + 1;
    t.done = true;
    emit(state, events, { type: 'tutorial', kind: 'good', text: TUTORIAL.doneBanner });
  } else {
    t.step += 1;
    emit(state, events, { type: 'tutorial', kind: 'good', text: TUTORIAL.steps[t.step - 1].banner });
  }
  return true;
}

// Section 8.13: a finished step moves on with a good toast, and each step moves only when its own objective is done.
// Step 6 finishing ends the tutorial. On forceStep6Day an unfinished tutorial sends one riders warning that names the
// current step; the step stays where it is and never jumps.
export function tutorialDay(state, events) {
  let moved = advanceStep(state, events);
  while (moved) moved = advanceStep(state, events);
  const t = state.tutorial;
  if (!t.done && t.step < LAST_STEP && state.day === TUTORIAL.forceStep6Day) {
    emit(state, events, { type: 'tutorial', kind: 'warn', text: `Step ${t.step} of ${LAST_STEP}: ${RIDERS_WARNING}` });
  }
}

// The same step checks as tutorialDay, run on demand. commands.js calls it after each placement, so a finished step shows
// at once rather than at dawn. Each call moves at most one step. A call that changes nothing returns [] and writes no
// log line, which lets the caller loop until no step moves. Otherwise returns the tutorial event it emitted (also
// written to state.log).
export function checkTutorial(state) {
  const events = [];
  advanceStep(state, events);
  return events;
}

// Next lines of steps 4 and 5 (R2-04 f), read from what is placed: the Lumber Camp, and the Market until its sale is made.
// null keeps the config line: nothing of the step is placed yet, or the step is another one. A sale finishes step 5 inside
// its own command (commands.js tutorialNow), so no line here reports a sale as done.
function placedNext(state, id) {
  if (id === 4) {
    const camps = state.buildings.filter((b) => b.type === 'lumberCamp');
    if (camps.some((b) => b.stage === 'complete' && b.crew < 1)) return 'Give the Lumber Camp a worker (Kingdom > People).';
    return camps.some((b) => b.stage === 'building') ? 'The Lumber Camp is under construction.' : null;
  }
  if (id !== 5) return null;
  const markets = state.buildings.filter((b) => b.type === 'market');
  if (markets.length === 0) return 'Build a Market from Build > Services.';
  if (!markets.some((b) => b.stage === 'complete')) return 'Finish the Market.';
  return 'Sell 10 wood at Kingdom > Market.';
}

// Section 3.9: the banner, next line and marker kinds of the current step (or the done banner).
export function tutorialStatus(state) {
  const t = state.tutorial;
  const step = t.done ? null : TUTORIAL.steps[t.step - 1] || null;
  if (!step) {
    return { step: t.step, total: LAST_STEP, done: t.done, skipped: t.skipped, banner: TUTORIAL.doneBanner, next: '', markerKinds: [] };
  }
  let next = step.next;
  if (step.need !== undefined) {
    const { have, need } = stepCount(state, step.id);
    next = next.replace('{have}', String(have)).replace('{need}', String(need));
  }
  const placed = placedNext(state, step.id);
  if (placed !== null) next = placed;
  return { step: t.step, total: LAST_STEP, done: false, skipped: t.skipped, banner: step.banner, next, markerKinds: step.markers.slice() };
}

// The most negative happiness causes, as {key, label, value} (section 7.8 outcome). Lost games name only negative causes.
function topCauses(state, negativeOnly) {
  return state.happinessCauses
    .map((c, i) => ({ key: c.key, label: c.label, value: c.value, i }))
    .filter((c) => !negativeOnly || c.value < 0)
    .sort((a, b) => a.value - b.value || a.i - b.i)
    .slice(0, OUTCOME_CAUSES)
    .map(({ key, label, value }) => ({ key, label, value }));
}

function lose(state, events, reason, text) {
  state.outcome.status = 'lost';
  state.outcome.reason = reason;
  state.outcome.day = state.day;
  state.outcome.causes = topCauses(state, true);
  emit(state, events, { type: 'outcome', kind: 'bad', text });
}

// Section 8.13: the win is checked first. Loss checks run only while the game is still playing (not in sandbox).
export function outcomeDay(state, events) {
  const o = state.outcome;
  if (o.status !== 'playing') return;
  if (state.buildings.some((b) => b.type === 'royalCharter' && b.stage === 'complete')) {
    o.status = 'won';
    o.reason = 'crowned';
    o.day = state.day;
    o.causes = topCauses(state, false);
    state.milestones.crown = state.day;
    emit(state, events, { type: 'outcome', kind: 'good', text: 'The Royal Charter is complete. The Crown is raised.' });
    return;
  }
  if (state.citizens.length === 0) lose(state, events, 'extinct', 'The valley is empty.');
  else if (state.exodusDays >= POPULATION.exodus.days) lose(state, events, 'exodus', 'The people have left.');
}

// Section 6.2 continueSandbox row.
export function sandboxContinue(state) {
  if (state.outcome.status !== 'won') return { ok: false, reason: 'The kingdom has not been crowned yet' };
  state.outcome.status = 'sandbox';
  return { ok: true, reason: null, message: 'Sandbox mode: the kingdom plays on.' };
}

// Section 6.2 skipTutorial row. Skipping also sets the step to 7 (finished), as section 4.1 defines.
export function skipTutorial(state) {
  if (state.tutorial.done) return { ok: false, reason: 'The tutorial is already finished' };
  state.tutorial.done = true;
  state.tutorial.skipped = true;
  state.tutorial.step = LAST_STEP + 1;
  return { ok: true, reason: null, message: "Tutorial skipped. Your goals are in the Kingdom panel's Goals tab." };
}
