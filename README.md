# lf.wtf

Levi Foster's site. Plain static HTML, no build step, no framework.

    /                 Levi Foster as element Lf: a periodic table of his work, a readout, and a full
                      specification list (Person, ProfilePage and ItemList schema live here)
    /frmt/            FRMT, film simulation for iPhone
    /frmt/privacy     
    /modul8/          MODUL8, glitch art for iPhone
    /modul8/privacy   
    /cyano/           CYANO, cyanotype for iPhone
    /cyano/privacy    
    /harmony/         Harmony Palette, colour harmony for iPhone
    /harmony/privacy  
    /dollop/          Dollop, a colour mixing game for iPhone
    /dollop/privacy   
    /kippu/           Kippu, Japanese for a trip and the JLPT N5, for iPhone and iPad
    /kippu/privacy    
    /grnge/           GRNGE, black-and-white photo prints for iPhone
    /grnge/privacy    
    /carmeet/         Carmeet, the browser car meet (the game itself runs at carmeet.lf.wtf)
    /hive/            Hive, the hosted MCP hub for AI agents (the product itself runs at hive.lf.wtf)
    /hearthvale/      Hearthvale, a sub-project: a 3D kingdom builder made by AI agents on Claude Haiku 5.5
    /hearthvale/play/ the game itself, a copy of the Hearthvale repo's index.html, src/ and styles/ (English only)
    /system-memory/   System Memory, a sub-project: an AI short film made with Claude Code and the Krea MCP (the film is embedded from YouTube)
    robots.txt        
    sitemap.xml       every real URL; update lastmod when a page changes
    _headers          Cloudflare Pages: security headers + immutable asset caching
    _redirects        Cloudflare Pages: kills the old WordPress /sample-page/

## Deploying

Cloudflare Pages builds straight from this repo. There is no build command and no
output directory — the repo root *is* the site. Push to `main` and it is live in
about thirty seconds, with the previous deploy one click away in the Pages dashboard.

### What is not served

The repo root is the site, so everything in it would be public. `functions/_middleware.js` answers 404
for the paths listed in `_routes.json` (`tools/`, `content/`, `functions/`, `README.md`, `.gitignore`,
`_routes.json`) and only those paths run it, so it costs nothing on normal page views. Add a path there
when you add a folder that is not part of the website. `404.html` is the not-found page, which also
means an unknown URL gets a real 404 instead of the home page.

## Conventions worth keeping

Each page carries its own JSON-LD. The Person node is defined once, on the home page,
at `https://lf.wtf/#levifoster`; the app pages reference that same @id as their author
rather than redeclaring it, so Google sees one entity across the site instead of three
lookalikes. If you add a page, reference the same @id.

`sameAs` on that Person node is the load-bearing part for ranking on the name. Only add
profiles that genuinely belong to Levi — a wrong one weakens the whole set.

Images are committed at their final display size. There is no image pipeline, so resize
before adding rather than relying on CSS to scale a large file down.

## The home page

The home page draws Levi as element Lf in a periodic table of twelve works. The table tiles are
plain links, so it works without JavaScript; a small script fills the readout from the matching row
of the specification list below it, which is also what search engines and the translation tool read.
Change a work by editing its row in the specification list and its tile together.

The faint falling glyphs in the Lf tile are drawn on a canvas. Their ink follows
`assets/lf-rain-map-2.png`, a 216 x 200 brightness map made from Levi's portrait (subject cut out of
the black backdrop, darker features carry more ink). Under the immutable asset rule a new map needs a
new file name. With reduced motion the canvas draws one still frame.

`lf-rain-map-1.png` and `og-lf.png` are burned: they were requested while the deploy that added them was
still propagating, so the edge cached the old home page under those names for a year. Do not reuse
them, and do not fetch a new asset URL until the page that references it is live on lf.wtf.

Fonts are self-hosted under `assets/fonts/` (Schibsted Grotesk and DM Mono for the home page, Saira
for Carmeet, Archivo, Space Grotesk and IBM Plex Mono for Hive, the same three faces the Hive app uses), all SIL Open
Font License, latin subset.

## The Hive page

`/hive/` borrows the Hive app's identity rather than the site's: its sage, ink and orange tokens, the
seven-cell lattice mark, and the three-part rule under the header, so a visitor arriving from
hive.lf.wtf recognises the product. The hero lattice is that mark scaled up into six agents around an
orange hub; a small script sends a message through it every few seconds, pauses off screen, and does
nothing at all under reduced motion. The message log beside it is ordinary list markup, so the
translations reach it. Its translations come from one JSON file per locale in `tools/lang/hive_*.json`,
folded together by `tools/lang/hive.py`.
