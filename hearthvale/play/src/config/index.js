// owner: foundation
// Section 5.1 (TIME) and the CONFIG aggregate (section 3.1). Imports sibling config files only.
import { BUILDINGS } from './buildings.js';
import { RESOURCES } from './resources.js';
import { ECONOMY, UPGRADES } from './economy.js';
import { POPULATION } from './population.js';
import { EVENTS } from './events.js';
import { MILESTONES, TUTORIAL } from './milestones.js';
import { TIERS } from './tiers.js';
import { MAP } from './map.js';

export const TIME = {
  dayRealSeconds: 5, daysPerSeason: 12, seasonsPerYear: 4, daysPerYear: 48,
  speeds: [0, 0.2, 0.4, 0.6],
  maxDaysPerFrame: 3, logCap: 120,
  seasonNames: ['Spring', 'Summer', 'Autumn', 'Winter'],
  tierNames: ['Hamlet', 'Village', 'Town', 'Kingdom'],
};

export const CONFIG = Object.freeze({
  time: TIME,
  map: MAP,
  resources: RESOURCES,
  buildings: BUILDINGS,
  economy: ECONOMY,
  upgrades: UPGRADES,
  population: POPULATION,
  events: EVENTS,
  milestones: MILESTONES,
  tutorial: TUTORIAL,
  tiers: TIERS,
});
