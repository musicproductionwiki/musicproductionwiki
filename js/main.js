/* ===================================================
   MusicProductionWiki.com — main.js v3 + Search
   =================================================== */
'use strict';
(function () {

  /* ------------------------------------------------
     SEARCH INDEX — all 118 articles
     ------------------------------------------------ */
  const SEARCH_INDEX = [
    { title: "Ableton Live Beginner's Guide", url: "/articles/ableton-live-beginners-guide.html", tags: "daw ableton beginners guide" },
    { title: "Ableton Live Review", url: "/articles/ableton-live-review.html", tags: "daw ableton review" },
    { title: "Ableton Push 3 Standalone Review", url: "/articles/ableton-push-3-standalone-review.html", tags: "hardware push standalone review" },
    { title: "Ableton Push 3 vs Maschine MK3", url: "/articles/ableton-push-3-vs-maschine-mk3.html", tags: "comparison push maschine hardware" },
    { title: "Ableton vs Pro Tools", url: "/articles/ableton-vs-pro-tools.html", tags: "comparison daw ableton pro tools" },
    { title: "AI Chord Progression Tools", url: "/articles/ai-chord-progression-tools.html", tags: "ai chord tools music" },
    { title: "AI Music Production Tools: Complete Guide", url: "/articles/ai-music-production-tools-complete-guide.html", tags: "ai music production tools guide" },
    { title: "AI Stem Separation Guide", url: "/articles/ai-stem-separation-guide.html", tags: "ai stem separation guide" },
    { title: "ASCAP vs BMI", url: "/articles/ascap-vs-bmi.html", tags: "pro royalties ascap bmi comparison music business" },
    { title: "Auto-Tune vs Melodyne", url: "/articles/auto-tune-vs-melodyne.html", tags: "pitch correction autotune melodyne comparison" },
    { title: "Best Audio Interface for Home Studio", url: "/articles/best-audio-interface-home-studio.html", tags: "audio interface home studio gear buying guide" },
    { title: "Best DAW for Beginners", url: "/articles/best-daw-for-beginners.html", tags: "daw beginners best buying guide" },
    { title: "Best Free VST Plugins", url: "/articles/best-free-vst-plugins.html", tags: "free vst plugins best buying guide" },
    { title: "Best Microphone for Home Studio", url: "/articles/best-microphone-home-studio.html", tags: "microphone home studio best gear buying guide" },
    { title: "Best Plugins for Beginners", url: "/articles/best-plugins-for-beginners.html", tags: "plugins beginners best buying guide" },
    { title: "Best Studio Headphones for Music Production", url: "/articles/best-studio-headphones-music-production.html", tags: "headphones studio best gear buying guide" },
    { title: "Best Studio Monitors for Home Studio", url: "/articles/best-studio-monitors-home-studio.html", tags: "studio monitors home studio best gear buying guide" },
    { title: "Best Suno AI Prompts", url: "/articles/best-suno-ai-prompts.html", tags: "suno ai prompts best guide" },
    { title: "Beyerdynamic DT 990 Pro Review", url: "/articles/beyerdynamic-dt-990-pro-review.html", tags: "beyerdynamic headphones review gear" },
    { title: "Can You Copyright AI Music?", url: "/articles/can-you-copyright-ai-music.html", tags: "ai music copyright law music business" },
    { title: "Condenser vs Dynamic Microphone", url: "/articles/condenser-vs-dynamic-microphone.html", tags: "condenser dynamic microphone comparison gear" },
    { title: "DistroKid vs TuneCore", url: "/articles/distrokid-vs-tunecore.html", tags: "distrokid tunecore distribution comparison music business" },
    { title: "FabFilter Pro-C2 Review", url: "/articles/fabfilter-pro-c2-review.html", tags: "fabfilter compressor review plugins" },
    { title: "FabFilter Pro-Q3 Review", url: "/articles/fabfilter-pro-q3-review.html", tags: "fabfilter eq review plugins" },
    { title: "FL Studio vs Ableton", url: "/articles/fl-studio-vs-ableton.html", tags: "fl studio ableton comparison daw" },
    { title: "FL Studio vs Logic Pro", url: "/articles/fl-studio-vs-logic-pro.html", tags: "fl studio logic pro comparison daw" },
    { title: "Focusrite Scarlett Solo Review", url: "/articles/focusrite-scarlett-solo-review.html", tags: "focusrite scarlett audio interface review gear" },
    { title: "Headphones vs Studio Monitors", url: "/articles/headphones-vs-studio-monitors.html", tags: "headphones studio monitors comparison gear" },
    { title: "Home Recording Studio Setup", url: "/articles/home-recording-studio-setup.html", tags: "home studio setup recording gear guide" },
    { title: "How Music Royalties Work", url: "/articles/how-music-royalties-work.html", tags: "royalties music business how streaming" },
    { title: "How to Copyright Your Music", url: "/articles/how-to-copyright-your-music.html", tags: "copyright music law how to music business" },
    { title: "How to Distribute Music", url: "/articles/how-to-distribute-music.html", tags: "distribute music distribution how to music business" },
    { title: "How to EQ Drums", url: "/articles/how-to-eq-drums.html", tags: "eq drums how to techniques mixing" },
    { title: "How to Get a Record Deal", url: "/articles/how-to-get-a-record-deal.html", tags: "record deal music business how to" },
    { title: "How to Get Music on Spotify", url: "/articles/how-to-get-music-on-spotify.html", tags: "spotify music distribution how to music business" },
    { title: "How to Make a Beat: Beginner's Guide", url: "/articles/how-to-make-a-beat-beginners-guide.html", tags: "beat making beginners how to techniques" },
    { title: "How to Make Money from Music", url: "/articles/how-to-make-money-from-music.html", tags: "money music income how to music business" },
    { title: "How to Make Money with AI Music", url: "/articles/how-to-make-money-with-ai-music.html", tags: "ai music money income how to" },
    { title: "How to Make Trap Beats", url: "/articles/how-to-make-trap-beats.html", tags: "trap beats how to techniques making" },
    { title: "How to Master a Song", url: "/articles/how-to-master-a-song.html", tags: "mastering how to master song techniques complete guide" },
    { title: "How to Mix Music: Beginner's Guide", url: "/articles/how-to-mix-music-beginners-guide.html", tags: "mixing music beginners how to techniques guide" },
    { title: "How to Mix Vocals", url: "/articles/how-to-mix-vocals.html", tags: "vocals mixing how to techniques" },
    { title: "How to Promote Music Independently", url: "/articles/how-to-promote-music-independently.html", tags: "promote music independently marketing how to music business" },
    { title: "How to Use Compression on Vocals", url: "/articles/how-to-use-compression-on-vocals.html", tags: "compression vocals how to techniques" },
    { title: "How to Use Reverb in a Mix", url: "/articles/how-to-use-reverb-in-a-mix.html", tags: "reverb mix how to techniques" },
    { title: "iZotope Neutron Guide", url: "/articles/izotope-neutron-guide.html", tags: "izotope neutron mixing ai guide plugins" },
    { title: "iZotope Ozone 11 Review", url: "/articles/izotope-ozone-11-review.html", tags: "izotope ozone mastering review plugins" },
    { title: "iZotope RX Guide", url: "/articles/izotope-rx-guide.html", tags: "izotope rx audio repair guide plugins" },
    { title: "iZotope RX vs Waves Clarity", url: "/articles/izotope-rx-vs-waves-clarity.html", tags: "izotope rx waves clarity comparison plugins" },
    { title: "LANDR vs iZotope Ozone", url: "/articles/landr-vs-izotope-ozone.html", tags: "landr izotope ozone mastering comparison ai" },
    { title: "Logic Pro Beginner's Guide", url: "/articles/logic-pro-beginners-guide.html", tags: "logic pro beginners guide daw" },
    { title: "Logic Pro Review", url: "/articles/logic-pro-review.html", tags: "logic pro review daw" },
    { title: "Logic Pro vs Ableton Live", url: "/articles/logic-pro-vs-ableton-live.html", tags: "logic pro ableton comparison daw" },
    { title: "MIDI Keyboard vs Pad Controller", url: "/articles/midi-keyboard-vs-pad-controller.html", tags: "midi keyboard pad controller comparison gear" },
    { title: "Mixing in Mono Guide", url: "/articles/mixing-in-mono-guide.html", tags: "mono mixing guide techniques" },
    { title: "Music Contracts Explained", url: "/articles/music-contracts-explained.html", tags: "contracts music business law explained" },
    { title: "Music Copyright and Fair Use Explained", url: "/articles/music-copyright-fair-use-explained.html", tags: "copyright fair use music law explained" },
    { title: "Music Licensing for YouTube", url: "/articles/music-licensing-for-youtube.html", tags: "licensing youtube music business" },
    { title: "Music Metadata Explained", url: "/articles/music-metadata-explained.html", tags: "metadata music explained music business" },
    { title: "Music Publishing Deals Explained", url: "/articles/music-publishing-deals-explained.html", tags: "publishing deals music business explained" },
    { title: "Music Publishing Explained", url: "/articles/music-publishing-explained.html", tags: "publishing music business explained royalties" },
    { title: "Music Streaming Royalties Explained", url: "/articles/music-streaming-royalties-explained.html", tags: "streaming royalties music business explained" },
    { title: "Music Sync Licensing Guide", url: "/articles/music-sync-licensing-guide.html", tags: "sync licensing music business guide tv film" },
    { title: "Music Theory for Producers", url: "/articles/music-theory-for-producers.html", tags: "music theory producers guide techniques" },
    { title: "Native Instruments Maschine MK3 Review", url: "/articles/native-instruments-maschine-mk3-review.html", tags: "maschine native instruments review gear hardware" },
    { title: "Neumann TLM 103 Review", url: "/articles/neumann-tlm-103-review.html", tags: "neumann tlm 103 microphone review gear" },
    { title: "Neumann TLM 103 vs Rode NT1", url: "/articles/neumann-tlm-103-vs-rode-nt1.html", tags: "neumann rode microphone comparison gear" },
    { title: "Parallel Compression Explained", url: "/articles/parallel-compression-explained.html", tags: "parallel compression explained techniques" },
    { title: "Reaper vs Ableton", url: "/articles/reaper-vs-ableton.html", tags: "reaper ableton comparison daw" },
    { title: "Rode NT1 Review", url: "/articles/rode-nt1-review.html", tags: "rode nt1 microphone review gear" },
    { title: "Sample Rate and Bit Depth Explained", url: "/articles/sample-rate-bit-depth-explained.html", tags: "sample rate bit depth explained glossary" },
    { title: "Scarlett Solo vs Scarlett 2i2", url: "/articles/scarlett-solo-vs-scarlett-2i2.html", tags: "scarlett focusrite audio interface comparison gear" },
    { title: "Serum Synthesizer Review", url: "/articles/serum-synthesizer-review.html", tags: "serum synthesizer review plugins" },
    { title: "Serum vs Vital", url: "/articles/serum-vs-vital.html", tags: "serum vital synthesizer comparison plugins" },
    { title: "Shure SM7B Review", url: "/articles/shure-sm7b-review.html", tags: "shure sm7b microphone review gear" },
    { title: "Sidechain Compression Guide", url: "/articles/sidechain-compression-guide.html", tags: "sidechain compression guide techniques" },
    { title: "SM7B vs Rode NT1", url: "/articles/sm7b-vs-rode-nt1.html", tags: "sm7b rode microphone comparison gear" },
    { title: "Sony MDR-7506 Review", url: "/articles/sony-mdr-7506-review.html", tags: "sony headphones review gear" },
    { title: "Sound Design Basics", url: "/articles/sound-design-basics.html", tags: "sound design basics techniques guide" },
    { title: "Spotify vs Apple Music for Artists", url: "/articles/spotify-vs-apple-music-for-artists.html", tags: "spotify apple music comparison artists music business" },
    { title: "Spotify vs SoundCloud for Artists", url: "/articles/spotify-vs-soundcloud-for-artists.html", tags: "spotify soundcloud comparison artists music business" },
    { title: "SSL 2+ Review", url: "/articles/ssl-2-plus-review.html", tags: "ssl audio interface review gear" },
    { title: "Suno vs Udio", url: "/articles/suno-vs-udio.html", tags: "suno udio ai music comparison" },
    { title: "Universal Audio Apollo Twin Review", url: "/articles/universal-audio-apollo-twin-review.html", tags: "universal audio apollo interface review gear" },
    { title: "Valhalla Room Review", url: "/articles/valhalla-room-review.html", tags: "valhalla reverb review plugins" },
    { title: "Valhalla Room vs Lexicon", url: "/articles/valhalla-room-vs-lexicon.html", tags: "valhalla lexicon reverb comparison plugins" },
    { title: "Waves Renaissance Compressor Review", url: "/articles/waves-renaissance-compressor-review.html", tags: "waves renaissance compressor review plugins" },
    { title: "Waves SSL E-Channel Review", url: "/articles/waves-ssl-e-channel-review.html", tags: "waves ssl channel strip review plugins" },
    { title: "What Is a Compressor Used For?", url: "/articles/what-is-a-compressor-used-for.html", tags: "compressor used for what is techniques" },
    { title: "What Is a Music Manager?", url: "/articles/what-is-a-music-manager.html", tags: "music manager what is music business" },
    { title: "What Is an Audio Interface Used For?", url: "/articles/what-is-audio-interface-used-for.html", tags: "audio interface used for what is gear" },
    { title: "What Is Audio Mastering?", url: "/articles/what-is-audio-mastering.html", tags: "audio mastering what is techniques" },
    { title: "What Is Compression in Music Production?", url: "/articles/what-is-compression-music-production.html", tags: "compression music production what is techniques" },
    { title: "What Is EQ in Music Production?", url: "/articles/what-is-eq-music-production.html", tags: "eq equalizer music production what is techniques" },
    { title: "What Is Gain Staging?", url: "/articles/what-is-gain-staging.html", tags: "gain staging what is techniques" },
    { title: "What Is Mastering Music?", url: "/articles/what-is-mastering-music.html", tags: "mastering music what is techniques" },
    { title: "What Is MIDI?", url: "/articles/what-is-midi.html", tags: "midi what is glossary" },
    { title: "What Is Reverb in Music Production?", url: "/articles/what-is-reverb-music-production.html", tags: "reverb music production what is techniques" },
    { title: "What Is Saturation in Music Production?", url: "/articles/what-is-saturation-music-production.html", tags: "saturation music production what is techniques" },
    { title: "What Is Suno AI?", url: "/articles/what-is-suno-ai.html", tags: "suno ai what is guide" },
    { title: "What Is a VST Plugin?", url: "/articles/what-is-vst-plugin.html", tags: "vst plugin what is glossary" },
    { title: "FL Studio Review", url: "/articles/fl-studio-review.html", tags: "fl studio review daw" },
    { title: "Pro Tools Review", url: "/articles/pro-tools-review.html", tags: "pro tools review daw" },
    { title: "Ableton Push 3 Review", url: "/articles/ableton-push-3-review.html", tags: "ableton push 3 review hardware gear" },
    { title: "Native Instruments Komplete Kontrol Review", url: "/articles/native-instruments-komplete-kontrol-review.html", tags: "komplete kontrol native instruments review gear hardware" },
    { title: "Waves Abbey Road Plugins Review", url: "/articles/waves-abbey-road-plugins-review.html", tags: "waves abbey road plugins review" },
    { title: "FL Studio vs Pro Tools", url: "/articles/fl-studio-vs-pro-tools.html", tags: "fl studio pro tools comparison daw" },
    { title: "Ableton vs Logic Pro for Beginners", url: "/articles/ableton-vs-logic-pro-for-beginners.html", tags: "ableton logic pro beginners comparison daw" },
    { title: "Dynamic EQ vs Multiband Compression", url: "/articles/dynamic-eq-vs-multiband-compression.html", tags: "dynamic eq multiband compression comparison techniques" },
    { title: "How to Use EQ on Drums", url: "/articles/how-to-use-eq-on-drums.html", tags: "eq drums how to techniques mixing" },
    { title: "How to Record Vocals at Home", url: "/articles/how-to-record-vocals-at-home.html", tags: "record vocals home studio how to techniques" },
    { title: "What Is the Frequency Spectrum?", url: "/articles/what-is-frequency-spectrum.html", tags: "frequency spectrum what is techniques" },
    { title: "How to Use Auto-Tune", url: "/articles/how-to-use-autotune.html", tags: "autotune auto-tune how to techniques pitch" },
    { title: "Music Distribution Explained", url: "/articles/music-distribution-explained.html", tags: "music distribution explained music business" },
    { title: "How to Build a Fanbase", url: "/articles/how-to-build-a-fanbase.html", tags: "fanbase build how to music business marketing" },
    { title: "Music Licensing Explained", url: "/articles/music-licensing-explained.html", tags: "music licensing explained music business" },
    { title: "Best MIDI Controllers", url: "/articles/best-midi-controllers.html", tags: "midi controllers best buying guide gear" },
    { title: "Best Vocal Microphones", url: "/articles/best-vocal-microphones.html", tags: "vocal microphones best buying guide gear" },
  ];

  /* ------------------------------------------------
     SEARCH FUNCTION
     ------------------------------------------------ */
  function searchArticles(query) {
    if (!query || query.trim().length < 2) return [];
    const q = query.toLowerCase().trim();
    const words = q.split(/\s+/);

    return SEARCH_INDEX
      .map(article => {
        const haystack = (article.title + ' ' + article.tags).toLowerCase();
        // Score: title match scores higher than tag match
        let score = 0;
        words.forEach(word => {
          if (article.title.toLowerCase().includes(word)) score += 3;
          else if (haystack.includes(word)) score += 1;
        });
        // Boost exact title start matches
        if (article.title.toLowerCase().startsWith(q)) score += 5;
        return { ...article, score };
      })
      .filter(a => a.score > 0)
      .sort((a, b) => b.score - a.score)
      .slice(0, 8);
  }

  /* ------------------------------------------------
     BUILD SEARCH DROPDOWN UI
     ------------------------------------------------ */
  function buildSearchUI(inputEl, formEl) {
    if (!inputEl || !formEl) return;

    // Create dropdown container
    const dropdown = document.createElement('div');
    dropdown.className = 'search-dropdown';
    dropdown.setAttribute('role', 'listbox');
    dropdown.setAttribute('aria-label', 'Search results');
    formEl.style.position = 'relative';
    formEl.appendChild(dropdown);

    // Inject styles
    if (!document.getElementById('search-dropdown-styles')) {
      const style = document.createElement('style');
      style.id = 'search-dropdown-styles';
      style.textContent = `
        .search-dropdown {
          display: none;
          position: absolute;
          top: calc(100% + 6px);
          left: 0;
          right: 0;
          background: var(--bg-elevated, #1a2332);
          border: 1px solid var(--teal, #00d4a8);
          border-radius: 10px;
          z-index: 999;
          overflow: hidden;
          box-shadow: 0 8px 32px rgba(0,0,0,0.4);
          min-width: 280px;
        }
        .search-dropdown.open { display: block; }
        .search-result-item {
          display: block;
          padding: 10px 14px;
          color: var(--text-primary, #e2e8f0);
          text-decoration: none;
          font-size: 0.88rem;
          font-family: var(--font-body, 'Outfit', sans-serif);
          border-bottom: 1px solid rgba(255,255,255,0.06);
          transition: background 0.15s;
          cursor: pointer;
        }
        .search-result-item:last-child { border-bottom: none; }
        .search-result-item:hover,
        .search-result-item.focused {
          background: rgba(0, 212, 168, 0.12);
          color: var(--teal, #00d4a8);
        }
        .search-no-results {
          padding: 12px 14px;
          color: var(--text-secondary, #8899aa);
          font-size: 0.85rem;
          font-family: var(--font-body, 'Outfit', sans-serif);
        }
        .search-dropdown-label {
          padding: 8px 14px 4px;
          font-size: 0.7rem;
          text-transform: uppercase;
          letter-spacing: 0.08em;
          color: var(--teal, #00d4a8);
          font-weight: 600;
        }
      `;
      document.head.appendChild(style);
    }

    let currentFocus = -1;
    let resultsItems = [];

    function showResults(results) {
      dropdown.innerHTML = '';
      currentFocus = -1;

      if (results.length === 0) {
        dropdown.innerHTML = '<div class="search-no-results">No articles found — try different keywords</div>';
        dropdown.classList.add('open');
        return;
      }

      const label = document.createElement('div');
      label.className = 'search-dropdown-label';
      label.textContent = results.length + ' article' + (results.length !== 1 ? 's' : '') + ' found';
      dropdown.appendChild(label);

      results.forEach((article, i) => {
        const a = document.createElement('a');
        a.className = 'search-result-item';
        a.href = article.url;
        a.textContent = article.title;
        a.setAttribute('role', 'option');
        dropdown.appendChild(a);
      });

      resultsItems = dropdown.querySelectorAll('.search-result-item');
      dropdown.classList.add('open');
    }

    function hideResults() {
      dropdown.classList.remove('open');
      currentFocus = -1;
    }

    // Input handler
    let debounceTimer;
    inputEl.addEventListener('input', () => {
      clearTimeout(debounceTimer);
      const q = inputEl.value.trim();
      if (q.length < 2) { hideResults(); return; }
      debounceTimer = setTimeout(() => {
        const results = searchArticles(q);
        showResults(results);
      }, 150);
    });

    // Keyboard navigation
    inputEl.addEventListener('keydown', (e) => {
      if (!dropdown.classList.contains('open')) return;

      if (e.key === 'ArrowDown') {
        e.preventDefault();
        currentFocus = Math.min(currentFocus + 1, resultsItems.length - 1);
        resultsItems.forEach((el, i) => el.classList.toggle('focused', i === currentFocus));
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        currentFocus = Math.max(currentFocus - 1, 0);
        resultsItems.forEach((el, i) => el.classList.toggle('focused', i === currentFocus));
      } else if (e.key === 'Enter') {
        if (currentFocus >= 0 && resultsItems[currentFocus]) {
          e.preventDefault();
          window.location.href = resultsItems[currentFocus].href;
        }
      } else if (e.key === 'Escape') {
        hideResults();
        inputEl.blur();
      }
    });

    // Prevent form submit from reloading page
    formEl.addEventListener('submit', (e) => {
      e.preventDefault();
      const q = inputEl.value.trim();
      if (q.length >= 2) {
        const results = searchArticles(q);
        showResults(results);
      }
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
      if (!formEl.contains(e.target)) hideResults();
    });

    // Close on input focus loss (with delay for click)
    inputEl.addEventListener('blur', () => {
      setTimeout(hideResults, 200);
    });
  }

  /* ------------------------------------------------
     INIT ALL SEARCH FORMS ON PAGE
     ------------------------------------------------ */
  const desktopInput = document.getElementById('siteSearch');
  const desktopForm  = desktopInput ? desktopInput.closest('.search-form') : null;
  buildSearchUI(desktopInput, desktopForm);

  const mobileInput = document.getElementById('mobileSearch');
  const mobileForm  = mobileInput ? mobileInput.closest('.search-form') : null;
  buildSearchUI(mobileInput, mobileForm);

  /* ------------------------------------------------
     MOBILE MENU
     ------------------------------------------------ */
  const menuToggle = document.getElementById('menuToggle');
  const mobileNav = document.getElementById('mobileNav');
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
    if (href === currentPath || (currentPath.includes(href) && href !== '/' && href !== '#')) {
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
      const progress = docHeight > 0 ? (window.scrollY / docHeight) * 100 : 0;
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
    backToTop.classList.toggle('visible', window.scrollY > 500);
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
    const sidebarTocList = document.querySelector('.toc-list');
    if (sidebarTocList && headings.length > 0) {
      sidebarTocList.innerHTML = '';
      headings.forEach(h => {
        const li = document.createElement('li');
        const a = document.createElement('a');
        a.href = '#' + h.id;
        a.textContent = h.textContent;
        li.appendChild(a);
        sidebarTocList.appendChild(li);
      });
    }
    const tocLinks = document.querySelectorAll('.toc-list a');
    if (tocLinks.length > 0) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const id = entry.target.id;
            tocLinks.forEach(link => {
              link.parentElement.classList.toggle('active', link.getAttribute('href') === '#' + id);
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
    const words = articleBody.innerText.trim().split(/\s+/).length;
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
        const top = target.getBoundingClientRect().top + window.scrollY - 24;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  /* ------------------------------------------------
     NEWSLETTER FORM
     ------------------------------------------------ */
  document.querySelectorAll('.newsletter-form-js').forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const emailInput = form.querySelector('input[type="email"]');
      const btn = form.querySelector('.btn-newsletter');
      if (!emailInput || !emailInput.value.trim()) return;
      btn.textContent = 'Subscribing…';
      btn.disabled = true;
      setTimeout(() => {
        btn.textContent = '✓ You\'re in!';
        btn.style.background = 'var(--teal-dim)';
        emailInput.value = '';
        setTimeout(() => {
          btn.disabled = false;
          btn.textContent = 'Subscribe Free';
          btn.style.background = '';
        }, 5000);
      }, 900);
    });
  });

  /* ------------------------------------------------
     EXTERNAL LINKS
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
