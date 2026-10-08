// owner: foundation
// Section 5.9: tier requirements. Check keys: pop, buildings, happy, has:<type>, any:<a>,<b>.

export const TIERS = [
  { id: 0, name: 'Hamlet', checks: [] },
  { id: 1, name: 'Village', checks: [
    { key: 'pop', label: 'People', need: 25 },
    { key: 'buildings', label: 'Buildings', need: 8 },
    { key: 'happy', label: 'Happiness', need: 45 },
  ] },
  { id: 2, name: 'Town', checks: [
    { key: 'pop', label: 'People', need: 50 },
    { key: 'buildings', label: 'Buildings', need: 18 },
    { key: 'happy', label: 'Happiness', need: 52 },
    { key: 'has:market', label: 'Market', need: 1 },
    { key: 'has:workshop', label: 'Workshop', need: 1 },
    { key: 'has:tavern', label: 'Tavern', need: 1 },
    { key: 'has:storehouse', label: 'Storehouse', need: 1 },
    { key: 'any:watchtower,barracks', label: 'Watchtower or Barracks', need: 1 },
  ] },
  { id: 3, name: 'Kingdom', checks: [
    { key: 'pop', label: 'People', need: 90 },
    { key: 'buildings', label: 'Buildings', need: 32 },
    { key: 'happy', label: 'Happiness', need: 58 },
    { key: 'has:storehouse', label: 'Storehouses', need: 2 },
    { key: 'has:mine', label: 'Iron Mine', need: 1 },
    { key: 'has:granary', label: 'Granary', need: 1 },
    { key: 'has:clinic', label: 'Clinic', need: 1 },
    { key: 'has:chapel', label: 'Chapel', need: 1 },
    { key: 'has:watchtower', label: 'Watchtower', need: 1 },
    { key: 'has:market', label: 'Market', need: 1 },
    { key: 'has:tavern', label: 'Tavern', need: 1 },
    { key: 'has:workshop', label: 'Workshop', need: 1 },
  ] },
];
