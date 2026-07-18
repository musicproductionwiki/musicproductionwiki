// S229-A: the .html fold.
//
// Netlify's redirect matcher has NO generic pattern for this. Measured on
// deploy-preview-267, not assumed:
//   /*.html -> /:splat        200 -- splats are trailing-only, never matched
//   /tools/*.html             200 -- same construct, same non-match
//   /articles/:slug.html      301 -> literal "/articles/:slug". Netlify reads
//                             :name to the next '/', so the placeholder was
//                             named "slug.html", captured nothing, and matched
//                             EVERY single segment under /articles/ -- including
//                             the extensionless canonicals. A self-referential
//                             loop across 678 pages. A 301 in the status column
//                             is not a working redirect. Read the target.
//   explicit per-slug         301 -- works, but 754 rules against a 1000 ceiling
//                             and one more per article, forever.
//
// So: this. No ceiling, no per-article step, and it lives in the repo where
// RULE #0 still holds.
//
// PASSTHROUGH is GENERATED from netlify.toml by mpw_s229a_edge2.py. Edge
// functions run BEFORE redirect rules, so any path a rule claims by name must
// be left alone or the rule is unreachable -- that is how 13 rename redirects
// became dead ends on the first probe. DO NOT hand-edit this list; regenerate it.

// Derived from netlify.toml -- includes the GSC site-verification file, whose
// redirection would cost us the Search Console property.
const PASSTHROUGH = new Set([
  "/articles/condenser-vs-dynamic-microphone.html",
  "/articles/fabfilter-pro-q4-review.html",
  "/articles/gain-staging-guide.html",
  "/articles/how-to-automate-in-fl-studio.html",
  "/articles/how-to-eq-drums.html",
  "/articles/how-to-use-reverb.html",
  "/articles/logic-pro-review.html",
  "/articles/sample-rate-guide.html",
  "/articles/serum-vs-vital.html",
  "/articles/valhalla-room-review-2026.html",
  "/articles/vocal-chain-explained.html",
  "/articles/what-is-audio-mastering.html",
  "/articles/what-is-headroom.html",
  "/bible/bible-index.html",
  "/categories/gear.html",
  "/googlee1fd3189ee9743f8.html",
]);

export default async (request) => {
  const url = new URL(request.url);
  const p = url.pathname;

  if (!p.endsWith(".html")) return;          // not ours
  if (PASSTHROUGH.has(p)) return;            // a redirect rule owns this path
  if (p.startsWith("/Templates/")) return;   // not served

  let out = p.slice(0, -5);
  if (out.endsWith("/index")) out = out.slice(0, -5);
  if (out === "/index" || out === "") out = "/";

  url.pathname = out;
  return Response.redirect(url.toString(), 301);
};

export const config = { path: "/*" };
