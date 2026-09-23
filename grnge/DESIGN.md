# /grnge

The app's own language on a web page: a photocopied zine taped together on a dark table. Not a
variation on the site's paper and serif, and not /cyano's coated sheet.

| Token | Value | Where it comes from |
|---|---|---|
| `--toner` | `#0E0E0D` | the app's ground, exactly |
| `--paper` | `#EEEBE3` | its canvas and copy |
| `--signal` | `#FF4B1F` | the one loud colour: what is on, selected or primary |
| `--riot` | `#FF3EA5` | the second pop, used sparingly |
| `--dust` | `#9C988E` | quiet text on the dark ground only; it fails contrast on paper |
| `--ink` | `#55524B` | quiet text on paper |

Rules, taken from the app rather than invented for the page:

- **Toner and paper, and one orange.** Orange marks the one thing to press and the small labels
  that need to be found. Pink appears in the wordmark, one headline tile and the prints themselves.
- **Paper is torn, not cut.** Every paper sheet has a jagged top and bottom edge, drawn by one SVG
  mask in the CSS. Prints are taped on with a strip of masking tape and sit a degree or two off
  straight. Grain on both grounds comes from a tiled SVG noise, drawn once.
- **Type is cut from different sources.** Anton for display, Space Mono in capitals for labels,
  Special Elite for filenames like grnge_0048, Rubik Mono One and Rock Salt only inside the
  wordmark and the headline tiles. Archivo for reading. All from Google Fonts; Rock Salt is
  requested with `text=G`, because the wordmark's second G is all it draws.
- **The wordmark is five letters from five sources**, as `Wordmark.swift` builds it, and stays
  Latin in every language.
- **The headline is cut into ransom tiles at runtime**, as `RansomText.swift` does it: words where
  the language spaces them, single characters in Chinese and Japanese, punctuation stuck to what it
  follows. The `<h1>` keeps its text for anything that reads it; the tiles are `aria-hidden`. The
  split happens in the script because `tools/i18n.py` translates the heading as one string.
- **CJK pages load the app's CJK display face for their script and no other**: Dela Gothic One
  for Japanese, Black Han Sans for Korean, ZCOOL QingKe HuangYou for Chinese. Body text falls back
  to each script's own system face, Japanese first to Hiragino and Yu Gothic, so Japanese is never
  set in a Chinese face.
- **Committed to dark.** The app has no light mode.

Pictures are real output. The five effect tiles are one row of the engine's contact sheet; the
feature prints are the canvas cropped out of simulator screenshots, with the app's controls and
overlays left outside the crop so they read in every language. The hero print is the app's own home
card print, recoloured from one bit to toner and paper.

The copy is written for the stranger: what they get, in their terms. No line explains how the
effects are made, and nothing on the page uses the copier's trademark.
