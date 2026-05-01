/* ===================================================
   MusicProductionWiki.com — main.js v3
   =================================================== */

'use strict';

(function () {

  /* ------------------------------------------------
     MOBILE MENU
  ------------------------------------------------ */
  const menuToggle = document.getElementById('menuToggle');
  const mobileNav  = document.getElementById('mobileNav');

  if (menuToggle && mobileNav) {
    menuToggle.addEventListener('click', () => {
      const open = mobileNav.classList.toggle('open');
      menuToggle.classList.toggle('open', open);
      menuToggle.setAttribute('aria-expanded', String(open));
      document.body.style.overflow = open ? 'hidden' : '';
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobileNav.classList.contains('open')) {
        mobileNav.classList.remove('open');
        menuToggle.classList.remove('open');
        menuToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    });
  }

  /* ------------------------------------------------
     ACTIVE NAV LINK
  ------------------------------------------------ */
  const currentPath = window.location.pathname;
  document.querySelectorAll('.nav-list a').forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;
    if (href === currentPath ||
        (currentPath.includes(href) && href !== '/' && href !== '#')) {
      link.classList.add('active');
    }
  });

  /* ------------------------------------------------
     READING PROGRESS BAR
  ------------------------------------------------ */
  const progressBar = document.getElementById('readingProgress');
  if (progressBar) {
    const updateProgress = () => {
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress  = docHeight > 0 ? (window.scrollY / docHeight) * 100 : 0;
      progressBar.style.width = Math.min(progress, 100) + '%';
      progressBar.setAttribute('aria-valuenow', Math.round(progress));
    };
    window.addEventListener('scroll', updateProgress, { passive: true });
    updateProgress();
  }

  /* ------------------------------------------------
     BACK TO TOP BUTTON
  ------------------------------------------------ */
  let backToTop = document.getElementById('backToTop');

  if (!backToTop) {
    backToTop = document.createElement('button');
    backToTop.id = 'backToTop';
    backToTop.setAttribute('aria-label', 'Back to top');
    backToTop.innerHTML = '↑';
    document.body.appendChild(backToTop);
  }

  const toggleBackToTop = () => {
    if (window.scrollY > 500) {
      backToTop.classList.add('visible');
    } else {
      backToTop.classList.remove('visible');
    }
  };

  window.addEventListener('scroll', toggleBackToTop, { passive: true });
  toggleBackToTop();

  backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  /* ------------------------------------------------
     AUTO-GENERATE TABLE OF CONTENTS
  ------------------------------------------------ */
  const articleBody = document.querySelector('.article-body');

  if (articleBody) {
    const headings = Array.from(articleBody.querySelectorAll('h2'));

    headings.forEach((h, i) => {
      if (!h.id) {
        h.id = 'section-' + (h.textContent.trim()
          .toLowerCase()
          .replace(/[^a-z0-9]+/g, '-')
          .replace(/^-|-$/g, '') || 'section-' + i);
      }
    });

    // Build inline TOC
    const inlineTocContainer = document.querySelector('.toc-inline-list');
    if (inlineTocContainer && headings.length > 0) {
      inlineTocContainer.innerHTML = '';
      headings.forEach(h => {
        const li = document.createElement('li');
        const a  = document.createElement('a');
        a.href        = '#' + h.id;
        a.textContent = h.textContent;
        li.appendChild(a);
        inlineTocContainer.appendChild(li);
      });
    }

    // Build sidebar TOC
    const sidebarTocList = document.querySelector('.toc-list');
    if (sidebarTocList && headings.length > 0) {
      sidebarTocList.innerHTML = '';
      headings.forEach(h => {
        const li = document.createElement('li');
        const a  = document.createElement('a');
        a.href        = '#' + h.id;
        a.textContent = h.textContent;
        li.appendChild(a);
        sidebarTocList.appendChild(li);
      });
    }

    // Scroll spy
    const tocLinks = document.querySelectorAll('.toc-list a');
    if (tocLinks.length > 0) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const id = entry.target.id;
            tocLinks.forEach(link => {
              link.parentElement.classList.toggle(
                'active',
                link.getAttribute('href') === '#' + id
              );
            });
          }
        });
      }, { rootMargin: '-80px 0px -65% 0px' });

      headings.forEach(h => observer.observe(h));
    }
  }

  /* ------------------------------------------------
     ESTIMATED READ TIME
  ------------------------------------------------ */
  const readTimeEl = document.querySelector('.read-time-auto');
  if (readTimeEl && articleBody) {
    const words   = articleBody.innerText.trim().split(/\s+/).length;
    const minutes = Math.max(1, Math.round(words / 200));
    readTimeEl.textContent = minutes + ' min read';
  }

  /* ------------------------------------------------
     SMOOTH ANCHOR SCROLL
  ------------------------------------------------ */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const id = anchor.getAttribute('href').slice(1);
      if (!id) return;
      const target = document.getElementById(id);
      if (target) {
        e.preventDefault();
        const offset = 24;
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  /* ------------------------------------------------
     FILTER TAGS
  ------------------------------------------------ */
  document.querySelectorAll('.filter-tag').forEach(tag => {
    tag.addEventListener('click', () => {
      const group = tag.closest('.filter-tags');
      if (!group) return;
      group.querySelectorAll('.filter-tag').forEach(t => t.classList.remove('active'));
      tag.classList.add('active');
    });
  });

  /* ------------------------------------------------
     NEWSLETTER FORM
  ------------------------------------------------ */
  document.querySelectorAll('.newsletter-form-js').forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const emailInput = form.querySelector('input[type="email"]');
      const btn        = form.querySelector('.btn-newsletter');
      if (!emailInput || !emailInput.value.trim()) return;

      btn.textContent = 'Subscribing…';
      btn.disabled    = true;

      setTimeout(() => {
        btn.textContent      = '✓ You\'re in!';
        btn.style.background = 'var(--teal-dim)';
        emailInput.value     = '';
        const nameInput = form.querySelector('input[name="name"]');
        if (nameInput) nameInput.value = '';
        setTimeout(() => {
          btn.disabled         = false;
          btn.textContent      = 'Subscribe to The Producer\'s Briefing';
          btn.style.background = '';
        }, 5000);
      }, 900);
    });
  });

  /* ------------------------------------------------
     EXTERNAL LINKS — open in new tab
  ------------------------------------------------ */
  document.querySelectorAll('a[href^="http"]').forEach(link => {
    if (!link.hostname || link.hostname !== window.location.hostname) {
      link.setAttribute('target', '_blank');
      link.setAttribute('rel', 'noopener noreferrer');
    }
  });

  /* ------------------------------------------------
     COPYRIGHT YEAR
  ------------------------------------------------ */
  const yearEl = document.getElementById('copyrightYear');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

})();
