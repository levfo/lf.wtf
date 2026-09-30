// Runs only on the routes listed in /_routes.json: the build tools, the translation data and the repo's own
// notes, which live in the repo root because the repo root is the site. They are not part of the website,
// so they answer 404 instead of being served. Every other path is served as a static file and never reaches this.
export async function onRequest({ request, env }) {
  const page = await env.ASSETS.fetch(new URL('/404', request.url));
  return new Response(request.method === 'HEAD' ? null : page.body, {
    status: 404,
    headers: {
      'content-type': 'text/html; charset=utf-8',
      'cache-control': 'no-store',
      'x-robots-tag': 'noindex',
    },
  });
}
