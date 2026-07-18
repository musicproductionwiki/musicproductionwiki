// S229-A: the .html fold.
//
// Netlify's redirect matcher has no generic pattern for this -- measured on
// deploy-preview-267: splat+suffix never matches, and placeholder+suffix
// (/articles/:slug.html) matches every single segment and emits ":slug"
// literally, looping all 678 articles. Explicit per-slug works but costs
// 754 rules against a 1000-rule ceiling and a rule per future article.
//
// This does the same job with no ceiling and no per-article step.

const EXCLUDE = new Set([
  // GSC site-verification. Redirecting this loses the Search Console property,
  // which is the instrument every traffic decision on this site depends on.
  "/googlee1fd3189ee9743f8.html",
]);

export default async (request) => {
  const url = new URL(request.url);
  const p = url.pathname;

  if (!p.endsWith(".html")) return;          // pass through
  if (EXCLUDE.has(p)) return;                // pass through
  if (p.startsWith("/Templates/")) return;   // pass through

  let out = p.slice(0, -5);                  // strip ".html"
  if (out.endsWith("/index")) out = out.slice(0, -5);  // /bible/index.html -> /bible/
  if (out === "/index" || out === "") out = "/";       // /index.html -> /

  url.pathname = out;
  return Response.redirect(url.toString(), 301);
};

export const config = { path: "/*" };
