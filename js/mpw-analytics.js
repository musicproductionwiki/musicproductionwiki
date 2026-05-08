/**
 * MPW Analytics — Custom Event Tracking
 * Version: 1.0 — May 2026
 * 
 * Tracks granular user behavior for data collection and monetization.
 * Works alongside GA4. All data sent via gtag() events.
 * 
 * SETUP: Add your GA4 Measurement ID to main.js before this loads.
 * Then add <script src="../js/mpw-analytics.js"></script> to every page.
 * 
 * EVENTS TRACKED:
 * 1. Site search queries
 * 2. Article read depth (25%, 50%, 75%, 100%)
 * 3. Affiliate link clicks
 * 4. Internal link clicks
 * 5. Time on page milestones
 * 6. FAQ interactions
 * 7. Newsletter signup attempts
 * 8. Category browsing
 * 9. Brand page visits
 * 10. Dictionary term lookups (when Bible is live)
 */

(function() {
  'use strict';

  // ── SAFETY CHECK ──────────────────────────────────────────
  // Only run if gtag is available (GA4 loaded)
  function gtag_safe(event, params) {
    if (typeof gtag === 'function') {
      gtag('event', event, params);
    }
    // Also log to console in dev mode for debugging
    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
      console.log('[MPW Analytics]', event, params);
    }
  }

  // ── UTILITY ───────────────────────────────────────────────
  function getArticleSlug() {
    const path = window.location.pathname;
    const match = path.match(/\/articles\/([^/]+)\.html/);
    return match ? match[1] : null;
  }

  function getCategory() {
    // Try to extract category from breadcrumb or meta
    const breadcrumb = document.querySelector('.breadcrumb-current');
    if (breadcrumb) return breadcrumb.textContent.trim();
    const cat = document.querySelector('meta[name="article-category"]');
    if (cat) return cat.getAttribute('content');
    return 'unknown';
  }

  function getPageType() {
    const path = window.location.pathname;
    if (path.includes('/articles/')) return 'article';
    if (path.includes('/categories/')) return 'category';
    if (path === '/' || path === '/index.html') return 'homepage';
    if (path.includes('/dictionary') || path.includes('/bible')) return 'dictionary';
    return 'other';
  }

  // ── 1. SITE SEARCH TRACKING ───────────────────────────────
  function initSearchTracking() {
    // Track searches on the site search input
    const searchInputs = document.querySelectorAll(
      '#search-input, .search-input, input[type="search"], input[placeholder*="Search"]'
    );

    searchInputs.forEach(function(input) {
      let searchTimer;
      let lastQuery = '';

      input.addEventListener('input', function() {
        clearTimeout(searchTimer);
        const query = this.value.trim();

        // Only track after 3+ chars and 800ms pause (user finished typing)
        if (query.length >= 3 && query !== lastQuery) {
          searchTimer = setTimeout(function() {
            lastQuery = query;
            gtag_safe('mpw_search', {
              search_term: query,
              search_length: query.length,
              page_type: getPageType(),
              page_path: window.location.pathname
            });
          }, 800);
        }
      });

      // Track when search is submitted
      const form = input.closest('form');
      if (form) {
        form.addEventListener('submit', function(e) {
          const query = input.value.trim();
          if (query) {
            gtag_safe('mpw_search_submit', {
              search_term: query,
              page_path: window.location.pathname
            });
          }
        });
      }
    });
  }

  // ── 2. ARTICLE READ DEPTH TRACKING ───────────────────────
  function initScrollTracking() {
    if (getPageType() !== 'article') return;

    const slug = getArticleSlug();
    const category = getCategory();
    const milestones = [25, 50, 75, 100];
    const reached = {};

    function getScrollPercent() {
      const doc = document.documentElement;
      const body = document.body;
      const scrollTop = doc.scrollTop || body.scrollTop;
      const scrollHeight = doc.scrollHeight || body.scrollHeight;
      const clientHeight = doc.clientHeight;
      return Math.round((scrollTop / (scrollHeight - clientHeight)) * 100);
    }

    let scrollTimer;
    window.addEventListener('scroll', function() {
      clearTimeout(scrollTimer);
      scrollTimer = setTimeout(function() {
        const pct = getScrollPercent();
        milestones.forEach(function(m) {
          if (pct >= m && !reached[m]) {
            reached[m] = true;
            gtag_safe('mpw_read_depth', {
              article_slug: slug,
              article_category: category,
              depth_percent: m,
              page_path: window.location.pathname
            });
          }
        });
      }, 200);
    });
  }

  // ── 3. AFFILIATE LINK CLICK TRACKING ─────────────────────
  function initAffiliateTracking() {
    // Affiliate domains to watch
    const affiliateDomains = [
      'pluginboutique.com',
      'sweetwater.com',
      'amazon.com',
      'amazon.co.uk',
      'loopmasters.com',
      'pluginfox.com',
      'jvz',
      'aff.',
      'affiliate'
    ];

    document.addEventListener('click', function(e) {
      const link = e.target.closest('a');
      if (!link) return;

      const href = link.href || '';
      const isAffiliate = affiliateDomains.some(function(domain) {
        return href.includes(domain);
      });

      // Also catch placeholder affiliate links
      const isPlaceholder = href.includes('#affiliate') ||
                            link.getAttribute('data-affiliate') ||
                            link.classList.contains('affiliate-link');

      if (isAffiliate || isPlaceholder) {
        const productName = link.textContent.trim().substring(0, 100);
        const destination = isPlaceholder ? 'placeholder' : new URL(href).hostname;

        gtag_safe('mpw_affiliate_click', {
          article_slug: getArticleSlug(),
          article_category: getCategory(),
          product_name: productName,
          affiliate_destination: destination,
          link_url: href,
          page_path: window.location.pathname
        });
      }
    });
  }

  // ── 4. INTERNAL LINK CLICK TRACKING ──────────────────────
  function initInternalLinkTracking() {
    document.addEventListener('click', function(e) {
      const link = e.target.closest('a');
      if (!link) return;

      const href = link.href || '';
      const isInternal = href.includes('musicproductionwiki.com') ||
                         href.startsWith('/') ||
                         href.startsWith('./') ||
                         href.startsWith('../');
      const isAffiliate = href.includes('#affiliate');

      if (isInternal && !isAffiliate && href !== '#') {
        const linkText = link.textContent.trim().substring(0, 100);
        gtag_safe('mpw_internal_click', {
          from_slug: getArticleSlug(),
          from_category: getCategory(),
          link_text: linkText,
          link_destination: href,
          page_path: window.location.pathname
        });
      }
    });
  }

  // ── 5. TIME ON PAGE MILESTONES ────────────────────────────
  function initTimeTracking() {
    if (getPageType() !== 'article') return;

    const slug = getArticleSlug();
    const category = getCategory();
    const timeMilestones = [30, 60, 120, 180, 300]; // seconds
    const reached = {};

    timeMilestones.forEach(function(seconds) {
      setTimeout(function() {
        if (!reached[seconds] && !document.hidden) {
          reached[seconds] = true;
          gtag_safe('mpw_time_on_page', {
            article_slug: slug,
            article_category: category,
            seconds_on_page: seconds,
            page_path: window.location.pathname
          });
        }
      }, seconds * 1000);
    });
  }

  // ── 6. FAQ INTERACTION TRACKING ───────────────────────────
  function initFaqTracking() {
    // Track FAQ accordion opens
    document.addEventListener('click', function(e) {
      const faqToggle = e.target.closest('.faq-question, .faq-toggle, [data-faq]');
      if (!faqToggle) return;

      const questionText = faqToggle.textContent.trim().substring(0, 150);
      gtag_safe('mpw_faq_open', {
        article_slug: getArticleSlug(),
        question_text: questionText,
        page_path: window.location.pathname
      });
    });
  }

  // ── 7. NEWSLETTER TRACKING ────────────────────────────────
  function initNewsletterTracking() {
    // Track newsletter form interactions
    const nlForms = document.querySelectorAll(
      '.newsletter-form, form[id*="newsletter"], form[class*="newsletter"]'
    );

    nlForms.forEach(function(form) {
      // Track when email field is focused (intent)
      const emailInput = form.querySelector('input[type="email"]');
      if (emailInput) {
        emailInput.addEventListener('focus', function() {
          gtag_safe('mpw_newsletter_focus', {
            page_type: getPageType(),
            page_path: window.location.pathname
          });
        });
      }

      // Track submission
      form.addEventListener('submit', function() {
        gtag_safe('mpw_newsletter_submit', {
          page_type: getPageType(),
          article_slug: getArticleSlug(),
          page_path: window.location.pathname
        });
      });
    });
  }

  // ── 8. CATEGORY PAGE TRACKING ─────────────────────────────
  function initCategoryTracking() {
    if (getPageType() !== 'category') return;

    // Track filter button clicks
    document.addEventListener('click', function(e) {
      const filterBtn = e.target.closest('.filter-btn, .cat-filter, [data-filter]');
      if (!filterBtn) return;

      gtag_safe('mpw_category_filter', {
        filter_name: filterBtn.textContent.trim(),
        category: getCategory(),
        page_path: window.location.pathname
      });
    });
  }

  // ── 9. BRAND PAGE TRACKING ────────────────────────────────
  function initBrandTracking() {
    const path = window.location.pathname;
    const brandMatch = path.match(/\/brands\/([^/]+)/);
    if (!brandMatch) return;

    const brandName = brandMatch[1];
    gtag_safe('mpw_brand_view', {
      brand_name: brandName,
      page_path: path
    });
  }

  // ── 10. PAGE VIEW ENRICHMENT ──────────────────────────────
  // Send enriched page view data beyond what GA4 collects by default
  function initEnrichedPageView() {
    const slug = getArticleSlug();
    const pageType = getPageType();

    // Get read time from article if available
    const readTime = document.querySelector('.read-time, [data-read-time]');
    const readTimeVal = readTime ? readTime.textContent.trim() : null;

    gtag_safe('mpw_page_view_enriched', {
      page_type: pageType,
      article_slug: slug || null,
      article_category: slug ? getCategory() : null,
      estimated_read_time: readTimeVal,
      page_path: window.location.pathname,
      referrer: document.referrer || 'direct',
      screen_width: window.screen.width,
      is_mobile: window.innerWidth < 768
    });
  }

  // ── 11. COPY LINK TRACKING ────────────────────────────────
  function initShareTracking() {
    document.addEventListener('click', function(e) {
      const shareBtn = e.target.closest('[class*="share"], [id*="share"], .copy-link');
      if (!shareBtn) return;

      const platform = shareBtn.classList.contains('share-twitter') ||
                       shareBtn.textContent.includes('X') ? 'twitter' :
                       shareBtn.classList.contains('share-reddit') ? 'reddit' :
                       shareBtn.textContent.includes('Copy') ? 'copy_link' : 'unknown';

      gtag_safe('mpw_share', {
        share_platform: platform,
        article_slug: getArticleSlug(),
        article_category: getCategory(),
        page_path: window.location.pathname
      });
    });
  }

  // ── INITIALIZE ALL TRACKING ───────────────────────────────
  function init() {
    try { initEnrichedPageView(); } catch(e) {}
    try { initSearchTracking(); } catch(e) {}
    try { initScrollTracking(); } catch(e) {}
    try { initAffiliateTracking(); } catch(e) {}
    try { initInternalLinkTracking(); } catch(e) {}
    try { initTimeTracking(); } catch(e) {}
    try { initFaqTracking(); } catch(e) {}
    try { initNewsletterTracking(); } catch(e) {}
    try { initCategoryTracking(); } catch(e) {}
    try { initBrandTracking(); } catch(e) {}
    try { initShareTracking(); } catch(e) {}
  }

  // Run after DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
