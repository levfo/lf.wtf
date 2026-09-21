# /kippu

The app's default theme, Shinkansen, on a web page. Not a variation on the site's look and not a
copy of /dollop's: the same rules as the app, in the app's colours.

| Token | Value | Where it comes from |
|---|---|---|
| `--paper` | `#F3F6FA` | the app's paper, exactly |
| `--ink` | `#000000` | its outlines and type |
| `--card` | `#FFFFFF` | the face of a card |
| `--cobalt` | `#1E56D9` | the primary: buttons, the ticket, the Plus tag |
| `--lime` | `#B5E61D` | right, and the one thing worth highlighting |
| `--coral` | `#E63946` | wrong, and nothing else |

Rules, taken from the app rather than invented for the page:

- **Borders are 4px, solid ink, square.** Nothing has a radius.
- **Shadows are hard and offset, never blurred.** 12px for a title card, 4px for anything
  else, and the shadow is part of the layout: an element carries a right and bottom margin
  the size of its own drop, so nothing sits in the space the shadow falls into. This was a
  real bug in the app before it was a rule here.
- **Display type is the system face at black weight, uppercase, tracked.** That is the app's
  headline style and the store slides' too. No webfont is loaded.
- **Labels are monospace, uppercase, letter-spaced.** Anything that names rather than speaks.
- **The ticket** in the header is the icon, tilted the way it is on the store's first slide.
- **Committed to light.** The app has six other themes, but the listing is shot in this one.

The hero carries a small kana check, ten characters with four readings each, because the app's
exercises are the product and a reader should be able to try one. It uses the app's own colours
for right and wrong and its own press-into-the-shadow button. Every string it speaks lives in a
hidden block in the markup, since `tools/i18n.py` does not read inside a `<script>`.

The copy is written for the stranger: what they get, in their terms. No line states an internal
decision or a baseline any language app has. The FAQ answers are word for word what the FAQPage
schema carries, so the two cannot drift.
