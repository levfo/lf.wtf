// owner: foundation
// Section 5.8: milestones (one-time awards) and the six-step tutorial.

export const MILESTONES = [
  { key: 'founded', name: 'Founded', text: 'Your first building is finished.', gold: 20 },
  { key: 'harvest', name: 'First harvest', text: 'A farm brought in food.', gold: 20 },
  { key: 'roof', name: 'Under a roof', text: 'Every citizen has a bed (10 or more people).', gold: 25 },
  { key: 'trade', name: 'First trade', text: 'You made a deal at the market or with a caravan.', gold: 15 },
  { key: 'watch', name: 'Watch kept', text: 'A raid was repelled.', gold: 40 },
  { key: 'winter', name: 'Winter holds', text: 'Food lasted through a winter.', gold: 30 },
  { key: 'lanterns', name: 'Lanterns lit', text: 'The first festival was held.', gold: 20 },
  { key: 'iron', name: 'Iron flows', text: 'Ten iron mined.', gold: 0 },
  { key: 'mending', name: 'Mending', text: 'The plague passed with most people alive.', gold: 25 },
  { key: 'village', name: 'Village', text: 'Reached the Village tier.', gold: 0 },
  { key: 'town', name: 'Town', text: 'Reached the Town tier.', gold: 0 },
  { key: 'kingdom', name: 'Kingdom', text: 'Reached the Kingdom tier.', gold: 0 },
  { key: 'golden', name: 'Golden Year', text: 'Happiness 70 or more for 48 sandbox days.', gold: 100 },
  { key: 'crown', name: 'The Crown is raised', text: 'The Royal Charter is complete.', gold: 0 },
];

export const TUTORIAL = {
  steps: [
    {
      id: 1,
      banner: 'Step 1 of 6: Lay a road from the Town Hall to the gold Build here ring, where the Farm goes.',
      next: 'Next: join the road to the gold Build here ring for the Farm ({have} of {need} road tiles)',
      need: 6, markers: ['door', 'site:farm'],
    },
    {
      id: 2,
      banner: 'Step 2 of 6: Build a Farm from Build > Food on the gold Build here ring. It needs wood and a road.',
      next: 'Next: place a Farm from Build > Food, with wood and a road beside it.',
      markers: ['site:farm'],
    },
    {
      id: 3,
      banner: 'Step 3 of 6: Build 2 Cottages from Build > Housing, with wood, stone and a road. Six people are in tents.',
      next: 'Next: finish 2 Cottages from Build > Housing ({have} of 2). Each needs wood, stone and a road.',
      need: 2, markers: ['site:cottage'],
    },
    {
      id: 4,
      banner: 'Step 4 of 6: Build a Lumber Camp from Build > Materials on the gold ring, then wait for construction.',
      next: 'Next: a finished Lumber Camp by the forest (Build > Materials), with a road and a worker.',
      markers: ['site:lumberCamp'],
    },
    {
      id: 5,
      banner: 'Step 5 of 6: Build a Market from Build > Services, then sell 10 wood for gold in Kingdom > Market.',
      next: 'Next: a finished Market with a worker, then Sell 10 on Wood (Kingdom > Market).',
      markers: ['site:market'],
    },
    {
      id: 6,
      banner: 'Step 6 of 6: Riders were seen in the hills. Build a Watchtower (Build > Defence) with a road and a worker.',
      next: 'Next: a staffed Watchtower on the gold ring (Build > Defence), with a road and a worker.',
      markers: ['site:watchtower'],
    },
  ],
  doneBanner: 'Tutorial complete. Next goal: reach the Village tier.',
  forceStep6Day: 20,
};
