# lf.wtf

Levi Foster's site. Plain static HTML, no build step, no framework.

    /                 Levi Foster — bio, work, links (Person schema lives here)
    /frmt/            FRMT, film simulation for iPhone
    /frmt/privacy     
    /modul8/          MODUL8, glitch art for iPhone
    /modul8/privacy   
    robots.txt        
    sitemap.xml       every real URL; update lastmod when a page changes
    _headers          Cloudflare Pages: security headers + immutable asset caching
    _redirects        Cloudflare Pages: kills the old WordPress /sample-page/

## Deploying

Cloudflare Pages builds straight from this repo. There is no build command and no
output directory — the repo root *is* the site. Push to `main` and it is live in
about thirty seconds, with the previous deploy one click away in the Pages dashboard.

## Conventions worth keeping

Each page carries its own JSON-LD. The Person node is defined once, on the home page,
at `https://lf.wtf/#levifoster`; the app pages reference that same @id as their author
rather than redeclaring it, so Google sees one entity across the site instead of three
lookalikes. If you add a page, reference the same @id.

`sameAs` on that Person node is the load-bearing part for ranking on the name. Only add
profiles that genuinely belong to Levi — a wrong one weakens the whole set.

Images are committed at their final display size. There is no image pipeline, so resize
before adding rather than relying on CSS to scale a large file down.
