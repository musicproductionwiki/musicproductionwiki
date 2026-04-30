/* ===================================================
   MusicProductionWiki.com — Main JS
   =================================================== */

'use strict';

(function () {

  // ---- Mobile Menu ----
  const menuToggle = document.getElementById('menuToggle');
  const mobileNav = document.getElementById('mobileNav');

  if (menuToggle && mobileNav) {
    menuToggle.addEventListener('click', () => {
      const open = mobileNav.classList.toggle('open');
      menuToggle.classList.toggle('open', open);
      menuToggle.setAttribute('aria-expanded', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });

    // Close on ESC
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobileNav.classList.contains('open')) {
        mobileNav.classList.remove('open');
        menuToggle.classList.remove('open');
        menuToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    });
  }

  // ---- Active Nav Link ----
  const navLinks = document.querySelectorAll('.nav-list a');
  const currentPath = window.location.pathname;
  navLinks.forEach(link => {
    if (link.getAttribute('href') === currentPath ||
        (currentPath.includes(link.getAttribute('href')) && link.getAttribute('href') !== '/')) {
      link.classList.add('active');
    }
  });

  // ---- TOC Scroll Spy ----
  const tocLinks = document.querySelectorAll('.toc-list a');
  if (tocLinks.length > 0) {
    const headings = Array.from(tocLinks).map(link => {
      const id = link.getAttribute('href').slice(1);
      return document.getElementById(id);
    }).filter(Boolean);

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.getAttribute('id');
          tocLinks.forEach(link => {
            const li = link.parentElement;
            li.classList.toggle('active', link.getAttribute('href') === '#' + id);
          });
        }
      });
    }, { rootMargin: '-80px 0px -60% 0px' });

    headings.forEach(h => observer.observe(h));
  }

  // ---- Filter Tags ----
  const filterTags = document.querySelectorAll('.filter-tag');
  filterTags.forEach(tag => {
    tag.addEventListener('click', () => {
      const group = tag.closest('.filter-tags');
      group.querySelectorAll('.filter-tag').forEach(t => t.classList.remove('active'));
      tag.classList.add('active');
      // Placeholder for real filtering logic
    });
  });

  // ---- Newsletter Form ----
  const newsletterForms = document.querySelectorAll('.newsletter-form-js');
  newsletterForms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const emailInput = form.querySelector('input[type="email"]');
      const btn = form.querySelector('.btn-newsletter');
      if (!emailInput || !emailInput.value) return;

      btn.textContent = 'Subscribing...';
      btn.disabled = true;

      // Simulate API call
      setTimeout(() => {
        btn.textContent = '✓ You\'re subscribed!';
        btn.style.background = '#00b892';
        emailInput.value = '';
        const nameInput = form.querySelector('input[name="name"]');
        if (nameInput) nameInput.value = '';
      }, 1000);
    });
  });

  // ---- Smooth anchor scroll ----
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const id = anchor.getAttribute('href').slice(1);
      const target = document.getElementById(id);
      if (target) {
        e.preventDefault();
        const offset = 80;
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  // ---- Reading progress bar (article pages) ----
  const progressBar = document.getElementById('readingProgress');
  if (progressBar) {
    window.addEventListener('scroll', () => {
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = docHeight > 0 ? (window.scrollY / docHeight) * 100 : 0;
      progressBar.style.width = Math.min(progress, 100) + '%';
    }, { passive: true });
  }

})();
