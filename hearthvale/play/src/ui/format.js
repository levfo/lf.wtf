// owner: ui-shell
// Number and text helpers for the UI. Display only; the simulation never imports this file.
// dateLabel reads TIME from config (ARCHITECTURE 5.1), so its wording matches the sim's dateText. Section 2.4 lists no such import.
import { TIME } from '../config/index.js';
const GROUP = /\B(?=(\d{3})+(?!\d))/g;

function group(digits) {
  return digits.replace(GROUP, ',');
}

function finite(n) {
  const v = Number(n);
  return Number.isFinite(v) ? v : 0;
}

// Integer with thousands separators: 1234 -> "1,234", -5 -> "-5".
export function fmt(n) {
  const r = Math.round(finite(n));
  return (r < 0 ? '-' : '') + group(String(Math.abs(r)));
}

// Signed number with an explicit sign: 6 -> "+6", -12.5 with digits 1 -> "-12.5", zero -> "0".
export function signed(n, digits = 0) {
  const d = Number.isInteger(digits) && digits > 0 ? digits : 0;
  let scale = 1;
  for (let i = 0; i < d; i++) scale *= 10;
  const v = finite(n);
  const mag = Math.round(Math.abs(v) * scale) / scale;
  if (mag === 0) return (0).toFixed(d);
  const text = mag.toFixed(d);
  const dot = text.indexOf('.');
  const whole = dot < 0 ? text : text.slice(0, dot);
  const rest = dot < 0 ? '' : text.slice(dot);
  return (v < 0 ? '-' : '+') + group(whole) + rest;
}

// Fraction 0..1 to a whole percentage: 0.42 -> "42%".
export function pct(x) {
  return Math.round(finite(x) * 100) + '%';
}

// Count and word: plural(1, 'day') -> "1 day", plural(3, 'day') -> "3 days".
// The word gets an s unless pluralWord is given (for irregular plurals, such as 'person' and 'people').
export function plural(n, word, pluralWord) {
  const count = Math.round(finite(n));
  const label = count === 1 ? word : pluralWord || word + 's';
  return fmt(count) + ' ' + label;
}

// The sim's date wording for a day: 0 -> "Spring 1, Year 1", 71 -> "Summer 12, Year 2". Not a number gives ''.
export function dateLabel(day) {
  const n = day === null || day === undefined || day === '' ? NaN : Number(day);
  if (!Number.isFinite(n)) return '';
  const d = Math.max(0, Math.floor(n));
  const dayOfYear = d % TIME.daysPerYear;
  const dayOfSeason = dayOfYear % TIME.daysPerSeason;
  const season = (dayOfYear - dayOfSeason) / TIME.daysPerSeason;
  const year = Math.floor(d / TIME.daysPerYear) + 1;
  return TIME.seasonNames[season] + ' ' + (dayOfSeason + 1) + ', Year ' + year;
}
