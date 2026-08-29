# /dollop

Paper, ink, and one yellow. The page is the app's own language, not a variation on the site's.

`lf.wtf` is warm paper and a serif. `/frmt` is the inside of a camera bag. `/cyano` is a coated
sheet in Prussian blue. `/dollop` is a **printed sheet**: flat white stock, hard black rules, one
saturated yellow, and shadows that are offset rather than blurred, because a blurred shadow implies
a light source and this design has none.

| Token | Value | Where it comes from |
|---|---|---|
| `--paper` | `#FCFAF6` | the game's background, exactly |
| `--ink` | `#0C0A0E` | its outlines and type |
| `--yellow` | `#FFE900` | its one accent, used for one thing per screen |
| `--board` | `#EFECE4` | the canvas the paint sits on |
| `--blue` | `#0067C0` | phthalo blue, as the pigment model renders it |
| `--sun` | `#F8E000` | cadmium yellow, likewise |
| `--green` | `#007E54` | what the two make, computed rather than chosen |

Rules, all taken from the app rather than invented for the page:

- **Borders are 4px, solid ink, and never rounded.** Nothing on this page has a radius.
- **Shadows are `8px 8px 0`, in ink.** Never blurred, never soft, never coloured.
- **A shadow is also the minimum gap.** It falls into the space below and to the right of its own
  element, so anything stacked has to clear 8px or it sits in the shadow of the thing above it.
  This was a real bug in the app's menus before it was a rule here.
- **Display type is `ui-rounded`**, which is SF Pro Rounded on Apple devices and therefore the same
  face as the wordmark inside the game. No webfont is loaded; a device without it falls back to the
  system sans and the page still reads.
- **Labels are `ui-monospace`, uppercase, letter-spaced.** Anything that names rather than speaks.
- **Committed to light.** The app forces light mode because the whole look is paper, and a page
  that inverted it would be showing something the product is not.

The colors in the hero are not picked to look right. The page carries the same eight pigment control
points the app carries, expands them to sixteen bands with the same smoothstep, mixes them in K/S
under Kubelka-Munk and converts through the CIE 1931 observer, in the browser. Targets are built the
way the game builds them, by inverting a whole number recipe over the tray, which is what guarantees
every one of them is reachable. That is the page's one argument and it must not be faked: a CSS
gradient claiming that blue and yellow make green would be the right claim with the wrong evidence.

Two consequences worth keeping. The board is a `<canvas>` marked `aria-hidden`, and everything it
says goes through a `role="status"` line underneath, so the demonstration is narrated rather than
silent. And every string it speaks lives in a hidden block in the markup, because `tools/i18n.py`
refuses to read inside a `<script>` and anything left in there would have shipped in English to ten
languages.
