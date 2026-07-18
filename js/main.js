// Google Analytics 4 — G-79VB543KCT
(function(){
  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=G-79VB543KCT';
  document.head.appendChild(s);
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  window.gtag = gtag;
  gtag('js', new Date());
  gtag('config', 'G-79VB543KCT');
})();

// MPW Custom Analytics
(function(){
  var s = document.createElement('script');
  s.src = '/js/mpw-analytics.js';
  document.head.appendChild(s);
})();

/* =================================================
   MusicProductionWiki.com — main.js v3 + Search
   =================================================  */

'use strict';

(function () {

  /* ------------------------------------------------
     SEARCH INDEX — all 317 articles
     ------------------------------------------------ */
  const SEARCH_INDEX = [
    { title: "Ableton Live 12 Review", url: "/articles/ableton-live-12-review", tags: "daw ableton review" },
    { title: "Ableton Live 12 vs 11", url: "/articles/ableton-live-12-vs-11", tags: "daw ableton comparison" },
    { title: "Ableton Live 12 vs FL Studio 21", url: "/articles/ableton-live-12-vs-fl-studio-21", tags: "daw ableton fl studio comparison" },
    { title: "Ableton Live Beginner's Guide", url: "/articles/ableton-live-beginners-guide", tags: "daw ableton beginners guide" },
    { title: "Ableton Live Review", url: "/articles/ableton-live-review", tags: "daw ableton review" },
    { title: "Ableton Live Tips and Tricks", url: "/articles/ableton-live-tips-and-tricks", tags: "daw ableton tips tricks techniques" },
    { title: "Ableton Push 3 Review", url: "/articles/ableton-push-3-review", tags: "ableton push 3 review hardware gear" },
    { title: "Ableton Push 3 Standalone Review", url: "/articles/ableton-push-3-standalone-review", tags: "hardware push standalone review" },
    { title: "Ableton Push 3 vs Maschine MK3", url: "/articles/ableton-push-3-vs-maschine-mk3", tags: "comparison push maschine hardware" },
    { title: "Ableton vs Logic Pro for Beginners", url: "/articles/ableton-vs-logic-pro-for-beginners", tags: "ableton logic pro beginners comparison daw" },
    { title: "Ableton vs Pro Tools", url: "/articles/ableton-vs-pro-tools", tags: "comparison daw ableton pro tools" },
    { title: "Adam Audio T5V Review", url: "/articles/adam-audio-t5v-review", tags: "adam audio monitors review gear" },
    { title: "Adam Audio T7V Review", url: "/articles/adam-audio-t7v-review", tags: "adam audio monitors review gear" },
    { title: "AI Chord Progression Tools", url: "/articles/ai-chord-progression-tools", tags: "ai chord tools music" },
    { title: "AI Music Production Tools: Complete Guide", url: "/articles/ai-music-production-tools-complete-guide", tags: "ai music production tools guide" },
    { title: "AI Stem Separation Guide", url: "/articles/ai-stem-separation-guide", tags: "ai stem separation guide" },
    { title: "Akai MPK Mini MK4 Review", url: "/articles/akai-mpk-mini-mk4-review", tags: "akai mpk mini midi controller review gear" },
    { title: "AKG C414 Review", url: "/articles/akg-c414-review", tags: "akg c414 microphone review gear" },
    { title: "AKG C414 XLII Review", url: "/articles/akg-c414-xlii-review", tags: "akg c414 xlii microphone review gear" },
    { title: "ASCAP vs BMI", url: "/articles/ascap-vs-bmi", tags: "pro royalties ascap bmi comparison music business" },
    { title: "Audio Interface Buying Guide", url: "/articles/audio-interface-buying-guide", tags: "audio interface buying guide gear" },
    { title: "Audio Interface vs Mixer", url: "/articles/audio-interface-vs-mixer", tags: "audio interface mixer comparison gear" },
    { title: "Auto-Tune vs Melodyne", url: "/articles/auto-tune-vs-melodyne", tags: "pitch correction autotune melodyne comparison" },
    { title: "Best AI Mixing Plugins 2026", url: "/articles/best-ai-mixing-plugins-2026", tags: "ai mixing plugins best 2026" },
    { title: "Best Audio Interface for Home Studio", url: "/articles/best-audio-interface-home-studio", tags: "audio interface home studio gear buying guide" },
    { title: "Best Audio Interfaces 2026", url: "/articles/best-audio-interfaces-2026", tags: "audio interfaces best 2026 gear" },
    { title: "Best Audio Interfaces for Guitarists", url: "/articles/best-audio-interfaces-for-guitarists", tags: "audio interfaces guitarists best gear" },
    { title: "Best Audio Interfaces Under $200", url: "/articles/best-audio-interfaces-under-200", tags: "audio interfaces budget best gear" },
    { title: "Best Budget Studio Gear 2026", url: "/articles/best-budget-studio-gear-2026", tags: "budget studio gear best 2026" },
    { title: "Best Compressor Plugins", url: "/articles/best-compressor-plugins", tags: "compressor plugins best buying guide" },
    { title: "Best DAW for Beginners", url: "/articles/best-daw-for-beginners", tags: "daw beginners best buying guide" },
    { title: "Best DAW for Hip Hop", url: "/articles/best-daw-for-hip-hop", tags: "daw hip hop best buying guide" },
    { title: "Best DAW for Beginners 2026", url: "/articles/best-daw-for-beginners-2026", tags: "daw beginners best 2026" },
    { title: "Best Free VST Plugins", url: "/articles/best-free-vst-plugins", tags: "free vst plugins best buying guide" },
    { title: "Best Laptops for Music Production", url: "/articles/best-laptops-for-music-production", tags: "laptops music production best gear" },
    { title: "Best Microphone for Home Studio", url: "/articles/best-microphone-home-studio", tags: "microphone home studio best gear buying guide" },
    { title: "Best MIDI Controllers", url: "/articles/best-midi-controllers", tags: "midi controllers best buying guide gear" },
    { title: "Best MIDI Controllers 2026", url: "/articles/best-midi-controllers-2026", tags: "midi controllers best 2026 gear" },
    { title: "Best Plugins for Beginners", url: "/articles/best-plugins-for-beginners", tags: "plugins beginners best buying guide" },
    { title: "Best Reverb Plugins", url: "/articles/best-reverb-plugins", tags: "reverb plugins best buying guide" },
    { title: "Best Studio Headphones for Music Production", url: "/articles/best-studio-headphones-music-production", tags: "headphones studio best gear buying guide" },
    { title: "Best Studio Monitors for Home Studio", url: "/articles/best-studio-monitors-home-studio", tags: "studio monitors home studio best gear buying guide" },
    { title: "Best Studio Monitors Under $500", url: "/articles/best-studio-monitors-under-500", tags: "studio monitors budget best gear" },
    { title: "Best Suno AI Prompts", url: "/articles/best-suno-ai-prompts", tags: "suno ai prompts best guide" },
    { title: "Best Vocal Microphones", url: "/articles/best-vocal-microphones", tags: "vocal microphones best buying guide gear" },
    { title: "Beyerdynamic DT 990 Pro Review", url: "/articles/beyerdynamic-dt-990-pro-review", tags: "beyerdynamic headphones review gear" },
    { title: "Bitwig Studio Review", url: "/articles/bitwig-studio-review", tags: "bitwig studio daw review" },
    { title: "Can You Copyright AI Music?", url: "/articles/can-you-copyright-ai-music", tags: "ai music copyright law music business" },
    { title: "Compressor Settings Guide", url: "/articles/compressor-settings-guide", tags: "compressor settings guide techniques" },
    { title: "Condenser vs Dynamic Microphone", url: "/articles/condenser-vs-dynamic-microphone", tags: "condenser dynamic microphone comparison gear" },
    { title: "DAW Comparison Guide", url: "/articles/daw-comparison-guide", tags: "daw comparison guide" },
    { title: "DistroKid vs TuneCore", url: "/articles/distrokid-vs-tunecore", tags: "distrokid tunecore distribution comparison music business" },
    { title: "Dynamic EQ vs Multiband Compression", url: "/articles/dynamic-eq-vs-multiband-compression", tags: "dynamic eq multiband compression comparison techniques" },
    { title: "EQ Cheat Sheet", url: "/articles/eq-cheat-sheet", tags: "eq cheat sheet guide techniques" },
    { title: "FabFilter Pro-C2 Review", url: "/articles/fabfilter-pro-c2-review", tags: "fabfilter compressor review plugins" },
    { title: "FabFilter Pro-DS Review", url: "/articles/fabfilter-pro-ds-review", tags: "fabfilter de-esser review plugins" },
    { title: "FabFilter Pro-L2 Review", url: "/articles/fabfilter-pro-l2-review", tags: "fabfilter limiter review plugins" },
    { title: "FabFilter Pro-MB Review", url: "/articles/fabfilter-pro-mb-review", tags: "fabfilter multiband compressor review plugins" },
    { title: "FabFilter Pro-Q3 Review", url: "/articles/fabfilter-pro-q3-review", tags: "fabfilter eq review plugins" },
    { title: "FabFilter Pro-R Review", url: "/articles/fabfilter-pro-r-review", tags: "fabfilter reverb review plugins" },
    { title: "FabFilter Pro-R2 Review", url: "/articles/fabfilter-pro-r2-review", tags: "fabfilter reverb review plugins" },
    { title: "FL Studio Beginner's Guide", url: "/articles/fl-studio-beginners-guide", tags: "fl studio beginners guide daw" },
    { title: "FL Studio Review", url: "/articles/fl-studio-review", tags: "fl studio review daw" },
    { title: "FL Studio Tips and Tricks", url: "/articles/fl-studio-tips-and-tricks", tags: "fl studio tips tricks techniques daw" },
    { title: "FL Studio vs Ableton", url: "/articles/fl-studio-vs-ableton", tags: "fl studio ableton comparison daw" },
    { title: "FL Studio vs Logic Pro", url: "/articles/fl-studio-vs-logic-pro", tags: "fl studio logic pro comparison daw" },
    { title: "FL Studio vs Pro Tools", url: "/articles/fl-studio-vs-pro-tools", tags: "fl studio pro tools comparison daw" },
    { title: "Focusrite Scarlett 2i2 Review", url: "/articles/focusrite-scarlett-2i2-review", tags: "focusrite scarlett audio interface review gear" },
    { title: "Focusrite Scarlett Solo Review", url: "/articles/focusrite-scarlett-solo-review", tags: "focusrite scarlett audio interface review gear" },
    { title: "Focusrite Scarlett vs Apollo Twin", url: "/articles/focusrite-scarlett-vs-apollo-twin", tags: "focusrite scarlett apollo twin comparison gear" },
    { title: "Frequency Masking Explained", url: "/articles/frequency-masking-explained", tags: "frequency masking explained techniques" },
    { title: "GarageBand vs Logic Pro", url: "/articles/garageband-vs-logic-pro", tags: "garageband logic pro comparison daw" },
    { title: "GarageBand vs FL Studio", url: "/articles/garageband-vs-fl-studio", tags: "garageband fl studio comparison daw" },
    { title: "Gain Staging Guide", url: "/articles/gain-staging-guide", tags: "gain staging guide techniques" },
    { title: "Headphones vs Studio Monitors", url: "/articles/headphones-vs-studio-monitors", tags: "headphones studio monitors comparison gear" },
    { title: "Home Recording Studio Setup", url: "/articles/home-recording-studio-setup", tags: "home studio setup recording gear guide" },
    { title: "How Music Royalties Work", url: "/articles/how-music-royalties-work", tags: "royalties music business how streaming" },
    { title: "How to Build a Fanbase", url: "/articles/how-to-build-a-fanbase", tags: "fanbase build how to music business marketing" },
    { title: "How to Build a Home Recording Studio", url: "/articles/how-to-build-a-home-recording-studio", tags: "home recording studio build how to gear" },
    { title: "How to Copyright Your Music", url: "/articles/how-to-copyright-your-music", tags: "copyright music law how to music business" },
    { title: "How to Distribute Music", url: "/articles/how-to-distribute-music", tags: "distribute music distribution how to music business" },
    { title: "How to EQ a Mix", url: "/articles/how-to-eq-a-mix", tags: "eq mix how to techniques" },
    { title: "How to EQ Drums", url: "/articles/how-to-eq-drums", tags: "eq drums how to techniques mixing" },
    { title: "How to Get a Record Deal", url: "/articles/how-to-get-a-record-deal", tags: "record deal music business how to" },
    { title: "How to Get More Streams on Spotify", url: "/articles/how-to-get-more-streams-on-spotify", tags: "spotify streams how to music business marketing" },
    { title: "How to Get Music on Spotify", url: "/articles/how-to-get-music-on-spotify", tags: "spotify music distribution how to music business" },
    { title: "How to License Your Music", url: "/articles/how-to-license-your-music", tags: "license music how to music business sync" },
    { title: "How to Make a Beat: Beginner's Guide", url: "/articles/how-to-make-a-beat-beginners-guide", tags: "beat making beginners how to techniques" },
    { title: "How to Make Lo-Fi Beats", url: "/articles/how-to-make-lo-fi-beats", tags: "lo-fi beats how to techniques making" },
    { title: "How to Make Money from Music", url: "/articles/how-to-make-money-from-music", tags: "money music income how to music business" },
    { title: "How to Make Money with AI Music", url: "/articles/how-to-make-money-with-ai-music", tags: "ai music money income how to" },
    { title: "How to Make Trap Beats", url: "/articles/how-to-make-trap-beats", tags: "trap beats how to techniques making" },
    { title: "How to Master a Song", url: "/articles/how-to-master-a-song", tags: "mastering how to master song techniques complete guide" },
    { title: "How to Master a Song at Home", url: "/articles/how-to-master-a-song-at-home", tags: "mastering at home how to techniques" },
    { title: "How to Mix Music: Beginner's Guide", url: "/articles/how-to-mix-music-beginners-guide", tags: "mixing music beginners how to techniques guide" },
    { title: "How to Mix Vocals", url: "/articles/how-to-mix-vocals", tags: "vocals mixing how to techniques" },
    { title: "How to Promote Music Independently", url: "/articles/how-to-promote-music-independently", tags: "promote music independently marketing how to music business" },
    { title: "How to Record Vocals at Home", url: "/articles/how-to-record-vocals-at-home", tags: "record vocals home studio how to techniques" },
    { title: "How to Use Auto-Tune", url: "/articles/how-to-use-autotune", tags: "autotune auto-tune how to techniques pitch" },
    { title: "How to Use Compression on Vocals", url: "/articles/how-to-use-compression-on-vocals", tags: "compression vocals how to techniques" },
    { title: "How to Use EQ on Drums", url: "/articles/how-to-use-eq-on-drums", tags: "eq drums how to techniques mixing" },
    { title: "How to Use Reverb in a Mix", url: "/articles/how-to-use-reverb-in-a-mix", tags: "reverb mix how to techniques" },
    { title: "iZotope Neutron Guide", url: "/articles/izotope-neutron-guide", tags: "izotope neutron mixing ai guide plugins" },
    { title: "iZotope Ozone 11 Review", url: "/articles/izotope-ozone-11-review", tags: "izotope ozone mastering review plugins" },
    { title: "iZotope RX Guide", url: "/articles/izotope-rx-guide", tags: "izotope rx audio repair guide plugins" },
    { title: "iZotope RX vs Waves Clarity", url: "/articles/izotope-rx-vs-waves-clarity", tags: "izotope rx waves clarity comparison plugins" },
    { title: "JBL 305P MkII Review", url: "/articles/jbl-305p-mkii-review", tags: "jbl studio monitors review gear" },
    { title: "KRK Rokit 5 G4 Review", url: "/articles/krk-rokit-5-g4-review", tags: "krk rokit monitors review gear" },
    { title: "LANDR vs iZotope Ozone", url: "/articles/landr-vs-izotope-ozone", tags: "landr izotope ozone mastering comparison ai" },
    { title: "Limiter vs Compressor", url: "/articles/limiter-vs-compressor", tags: "limiter compressor comparison techniques" },
    { title: "Logic Pro Beginner's Guide", url: "/articles/logic-pro-beginners-guide", tags: "logic pro beginners guide daw" },
    { title: "Logic Pro Review", url: "/articles/logic-pro-review", tags: "logic pro review daw" },
    { title: "Logic Pro Tips and Tricks", url: "/articles/logic-pro-tips-and-tricks", tags: "logic pro tips tricks techniques daw" },
    { title: "Logic Pro vs Ableton Live", url: "/articles/logic-pro-vs-ableton-live", tags: "logic pro ableton comparison daw" },
    { title: "Loopmasters Review", url: "/articles/loopmasters-review", tags: "loopmasters samples review" },
    { title: "Mastering Chain Guide", url: "/articles/mastering-chain-guide", tags: "mastering chain guide techniques" },
    { title: "MIDI Keyboard vs Pad Controller", url: "/articles/midi-keyboard-vs-pad-controller", tags: "midi keyboard pad controller comparison gear" },
    { title: "Mixing in Headphones Guide", url: "/articles/mixing-in-headphones-guide", tags: "mixing headphones guide techniques" },
    { title: "Mixing in Mono Guide", url: "/articles/mixing-in-mono-guide", tags: "mono mixing guide techniques" },
    { title: "Mixing Workflow Guide", url: "/articles/mixing-workflow-guide", tags: "mixing workflow guide techniques" },
    { title: "Music Contracts Explained", url: "/articles/music-contracts-explained", tags: "contracts music business law explained" },
    { title: "Music Copyright and Fair Use Explained", url: "/articles/music-copyright-fair-use-explained", tags: "copyright fair use music law explained" },
    { title: "Music Distribution Explained", url: "/articles/music-distribution-explained", tags: "music distribution explained music business" },
    { title: "Music Licensing Explained", url: "/articles/music-licensing-explained", tags: "music licensing explained music business" },
    { title: "Music Licensing for YouTube", url: "/articles/music-licensing-for-youtube", tags: "licensing youtube music business" },
    { title: "Music Metadata Explained", url: "/articles/music-metadata-explained", tags: "metadata music explained music business" },
    { title: "Music Publishing Deals Explained", url: "/articles/music-publishing-deals-explained", tags: "publishing deals music business explained" },
    { title: "Music Publishing Explained", url: "/articles/music-publishing-explained", tags: "publishing music business explained royalties" },
    { title: "Music Streaming Royalties Explained", url: "/articles/music-streaming-royalties-explained", tags: "streaming royalties music business explained" },
    { title: "Music Sync Licensing Guide", url: "/articles/music-sync-licensing-guide", tags: "sync licensing music business guide tv film" },
    { title: "Music Theory for Producers", url: "/articles/music-theory-for-producers", tags: "music theory producers guide techniques" },
    { title: "Native Instruments Komplete Kontrol Review", url: "/articles/native-instruments-komplete-kontrol-review", tags: "komplete kontrol native instruments review gear hardware" },
    { title: "Native Instruments Maschine MK3 Review", url: "/articles/native-instruments-maschine-mk3-review", tags: "maschine native instruments review gear hardware" },
    { title: "Neumann TLM 103 Review", url: "/articles/neumann-tlm-103-review", tags: "neumann tlm 103 microphone review gear" },
    { title: "Neumann TLM 103 vs Rode NT1", url: "/articles/neumann-tlm-103-vs-rode-nt1", tags: "neumann rode microphone comparison gear" },
    { title: "Parallel Compression Explained", url: "/articles/parallel-compression-explained", tags: "parallel compression explained techniques" },
    { title: "Parallel Compression Techniques", url: "/articles/parallel-compression-techniques", tags: "parallel compression techniques guide" },
    { title: "Presonus Studio One Review", url: "/articles/presonus-studio-one-review", tags: "presonus studio one daw review" },
    { title: "Pro Tools Beginner's Guide", url: "/articles/pro-tools-beginners-guide", tags: "pro tools beginners guide daw" },
    { title: "Pro Tools Review", url: "/articles/pro-tools-review", tags: "pro tools review daw" },
    { title: "Pro Tools vs Logic Pro", url: "/articles/pro-tools-vs-logic-pro", tags: "pro tools logic pro comparison daw" },
    { title: "Reaper DAW Review", url: "/articles/reaper-daw-review", tags: "reaper daw review" },
    { title: "Reaper vs Ableton", url: "/articles/reaper-vs-ableton", tags: "reaper ableton comparison daw" },
    { title: "Record Label Contracts Explained", url: "/articles/record-label-contracts-explained", tags: "record label contracts explained music business" },
    { title: "Rode NT1 Review", url: "/articles/rode-nt1-review", tags: "rode nt1 microphone review gear" },
    { title: "Rode NT1 vs NT1-A", url: "/articles/rode-nt1-vs-nt1-a", tags: "rode nt1 nt1-a microphone comparison gear" },
    { title: "Rode PodMic Review", url: "/articles/rode-podmic-review", tags: "rode podmic microphone review gear podcast" },
    { title: "Sample Rate and Bit Depth Explained", url: "/articles/sample-rate-bit-depth-explained", tags: "sample rate bit depth explained glossary" },
    { title: "Scarlett Solo vs Scarlett 2i2", url: "/articles/scarlett-solo-vs-scarlett-2i2", tags: "scarlett focusrite audio interface comparison gear" },
    { title: "Serum 2 Review", url: "/articles/serum-2-review", tags: "serum 2 synthesizer review plugins" },
    { title: "Serum Synthesizer Review", url: "/articles/serum-synthesizer-review", tags: "serum synthesizer review plugins" },
    { title: "Serum vs Vital", url: "/articles/serum-vs-vital", tags: "serum vital synthesizer comparison plugins" },
    { title: "Shure SM58 Review", url: "/articles/shure-sm58-review", tags: "shure sm58 microphone review gear" },
    { title: "Shure SM7B Review", url: "/articles/shure-sm7b-review", tags: "shure sm7b microphone review gear" },
    { title: "Shure SM7B vs SM7dB", url: "/articles/shure-sm7b-vs-sm7db", tags: "shure sm7b sm7db microphone comparison gear" },
    { title: "Sidechain Compression Guide", url: "/articles/sidechain-compression-guide", tags: "sidechain compression guide techniques" },
    { title: "SM7B vs Rode NT1", url: "/articles/sm7b-vs-rode-nt1", tags: "sm7b rode microphone comparison gear" },
    { title: "Sony MDR-7506 Review", url: "/articles/sony-mdr-7506-review", tags: "sony headphones review gear" },
    { title: "Sony WH-1000XM5 for Music Production", url: "/articles/sony-wh-1000xm5-review", tags: "sony headphones review gear" },
    { title: "Sound Design Basics", url: "/articles/sound-design-basics", tags: "sound design basics techniques guide" },
    { title: "Sound Design for EDM", url: "/articles/sound-design-for-edm", tags: "sound design edm techniques guide" },
    { title: "Spotify vs Apple Music for Artists", url: "/articles/spotify-vs-apple-music-for-artists", tags: "spotify apple music comparison artists music business" },
    { title: "Spotify vs SoundCloud for Artists", url: "/articles/spotify-vs-soundcloud-for-artists", tags: "spotify soundcloud comparison artists music business" },
    { title: "SSL 2+ Review", url: "/articles/ssl-2-plus-review", tags: "ssl audio interface review gear" },
    { title: "Steinberg Cubase Review", url: "/articles/steinberg-cubase-review", tags: "cubase steinberg daw review" },
    { title: "Steinberg UR22C Review", url: "/articles/steinberg-ur22c-review", tags: "steinberg ur22c audio interface review gear" },
    { title: "Suno AI Review 2026", url: "/articles/suno-ai-review-2026", tags: "suno ai review 2026 ai music" },
    { title: "Suno vs Udio", url: "/articles/suno-vs-udio", tags: "suno udio ai music comparison" },
    { title: "Synthesizer Basics Guide", url: "/articles/synthesizer-basics-guide", tags: "synthesizer basics guide techniques" },
    { title: "Universal Audio Apollo Twin Review", url: "/articles/universal-audio-apollo-twin-review", tags: "universal audio apollo interface review gear" },
    { title: "Udio AI Review", url: "/articles/udio-ai-review", tags: "udio ai review ai music" },
    { title: "Valhalla Room Review", url: "/articles/valhalla-room-review", tags: "valhalla reverb review plugins" },
    { title: "Valhalla Room vs Lexicon", url: "/articles/valhalla-room-vs-lexicon", tags: "valhalla lexicon reverb comparison plugins" },
    { title: "Vocal Chain Guide", url: "/articles/vocal-chain-guide", tags: "vocal chain guide techniques mixing" },
    { title: "Vocal Compression Guide", url: "/articles/vocal-compression-guide", tags: "vocal compression guide techniques" },
    { title: "Waves Abbey Road Plugins Review", url: "/articles/waves-abbey-road-plugins-review", tags: "waves abbey road plugins review" },
    { title: "Waves Gold Bundle Review", url: "/articles/waves-gold-bundle-review", tags: "waves gold bundle review plugins" },
    { title: "Waves Plugins Guide", url: "/articles/waves-plugins-guide", tags: "waves plugins guide" },
    { title: "Waves Renaissance Compressor Review", url: "/articles/waves-renaissance-compressor-review", tags: "waves renaissance compressor review plugins" },
    { title: "Waves SSL E-Channel Review", url: "/articles/waves-ssl-e-channel-review", tags: "waves ssl channel strip review plugins" },
    { title: "What Is a Compressor Used For?", url: "/articles/what-is-a-compressor-used-for", tags: "compressor used for what is techniques" },
    { title: "What Is a DAW?", url: "/articles/what-is-a-daw", tags: "daw what is glossary" },
    { title: "What Is a Mastering Engineer?", url: "/articles/what-is-a-mastering-engineer", tags: "mastering engineer what is music business" },
    { title: "What Is a Music Manager?", url: "/articles/what-is-a-music-manager", tags: "music manager what is music business" },
    { title: "What Is a Music Producer?", url: "/articles/what-is-a-music-producer", tags: "music producer what is music business" },
    { title: "What Is a Music Sync Supervisor?", url: "/articles/what-is-a-music-sync-supervisor", tags: "music sync supervisor what is music business" },
    { title: "What Is a Sample Pack?", url: "/articles/what-is-a-sample-pack", tags: "sample pack what is glossary" },
    { title: "What Is a Synthesizer?", url: "/articles/what-is-a-synthesizer", tags: "synthesizer what is glossary" },
    { title: "What Is a VST3 Plugin?", url: "/articles/what-is-a-vst3-plugin", tags: "vst3 plugin what is glossary" },
    { title: "What Is an Audio Interface Used For?", url: "/articles/what-is-audio-interface-used-for", tags: "audio interface used for what is gear" },
    { title: "What Is Compression in Music Production?", url: "/articles/what-is-compression-music-production", tags: "compression music production what is techniques" },
    { title: "What Is Dynamic Range in Music?", url: "/articles/what-is-dynamic-range-in-music", tags: "dynamic range music what is glossary" },
    { title: "What Is EQ in Music Production?", url: "/articles/what-is-eq-music-production", tags: "eq equalizer music production what is techniques" },
    { title: "What Is the Frequency Spectrum?", url: "/articles/what-is-frequency-spectrum", tags: "frequency spectrum what is techniques" },
    { title: "What Is Gain Staging?", url: "/articles/what-is-gain-staging", tags: "gain staging what is techniques" },
    { title: "What Is LUFS Explained", url: "/articles/what-is-lufs-explained", tags: "lufs explained what is mastering" },
    { title: "What Is Mastering Music?", url: "/articles/what-is-mastering-music", tags: "mastering music what is techniques" },
    { title: "What Is Mid-Side Processing?", url: "/articles/what-is-mid-side-processing", tags: "mid side processing what is techniques" },
    { title: "What Is MIDI?", url: "/articles/what-is-midi", tags: "midi what is glossary" },
    { title: "What Is Mixing?", url: "/articles/what-is-mixing", tags: "mixing what is techniques glossary" },
    { title: "What Is Music Arrangement?", url: "/articles/what-is-music-arrangement", tags: "music arrangement what is techniques" },
    { title: "What Is Reverb in Music Production?", url: "/articles/what-is-reverb-music-production", tags: "reverb music production what is techniques" },
    { title: "What Is Sampling in Music?", url: "/articles/what-is-sampling-in-music", tags: "sampling music what is glossary" },
    { title: "What Is Saturation in Music Production?", url: "/articles/what-is-saturation-music-production", tags: "saturation music production what is techniques" },
    { title: "What Is Spatial Audio?", url: "/articles/what-is-spatial-audio", tags: "spatial audio what is glossary" },
    { title: "What Is Suno AI?", url: "/articles/what-is-suno-ai", tags: "suno ai what is guide" },
    { title: "What Is Udio AI?", url: "/articles/what-is-udio-ai", tags: "udio ai what is guide" },
    { title: "What Is a VST Plugin?", url: "/articles/what-is-vst-plugin", tags: "vst plugin what is glossary" },
    { title: "What Is White Noise in Music Production?", url: "/articles/what-is-white-noise-music-production", tags: "white noise music production what is glossary" },
    { title: "Work for Hire Music Explained", url: "/articles/work-for-hire-music-explained", tags: "work for hire music explained music business" },
    { title: "Yamaha HS5 Review", url: "/articles/yamaha-hs5-review", tags: "yamaha hs5 monitors review gear" },
    { title: "Yamaha HS5 vs KRK Rokit 5 G5", url: "/articles/yamaha-hs5-vs-krk-rokit-5-g5", tags: "yamaha hs5 krk rokit monitors comparison gear" },
    { title: "Yamaha HS8 Review", url: "/articles/yamaha-hs8-review", tags: "yamaha hs8 monitors review gear" },
  
    { title: "808", url: "/bible/808", tags: "808 production bible reference production" },
    { title: "Additive Synthesis", url: "/bible/additive-synthesis", tags: "additive synthesis synthesis bible reference production" },
    { title: "ADSR", url: "/bible/adsr", tags: "adsr synthesis bible reference production" },
    { title: "Air Frequency", url: "/bible/air", tags: "air frequency frequency bible reference production" },
    { title: "Air Frequency EQ", url: "/bible/air-frequency-eq", tags: "air frequency eq frequency bible reference production" },
    { title: "Analog", url: "/bible/analog", tags: "analog signal processing bible reference production" },
    { title: "Arpeggiator", url: "/bible/arpeggiator", tags: "arpeggiator synthesis bible reference production" },
    { title: "Arrangement", url: "/bible/arrangement", tags: "arrangement music theory bible reference production" },
    { title: "Attack", url: "/bible/attack", tags: "attack dynamics bible reference production" },
    { title: "Attack and Release", url: "/bible/attack-release", tags: "attack and release dynamics bible reference production" },
    { title: "Audio Interface", url: "/bible/audio-interface", tags: "audio interface recording bible reference production" },
    { title: "Audio Routing", url: "/bible/audio-routing", tags: "audio routing mixing bible reference production" },
    { title: "Audio Track", url: "/bible/audio-track", tags: "audio track mixing bible reference production" },
    { title: "Automation", url: "/bible/automation", tags: "automation mixing bible reference production" },
    { title: "Automation Clip", url: "/bible/automation-clip", tags: "automation clip production bible reference production" },
    { title: "Aux Send", url: "/bible/aux-send", tags: "aux send mixing bible reference production" },
    { title: "Beat Making", url: "/bible/beat-making", tags: "beat making production bible reference production" },
    { title: "Bell Curve", url: "/bible/bell-curve", tags: "bell curve frequency bible reference production" },
    { title: "Bit Depth", url: "/bible/bit-depth", tags: "bit depth signal processing bible reference production" },
    { title: "Boom Bap", url: "/bible/boom-bap", tags: "boom bap production bible reference production" },
    { title: "Bounce", url: "/bible/bounce", tags: "bounce mixing bible reference production" },
    { title: "BPM", url: "/bible/bpm", tags: "bpm music theory bible reference production" },
    { title: "Breakdown", url: "/bible/breakdown", tags: "breakdown music theory bible reference production" },
    { title: "Bridge", url: "/bible/bridge", tags: "bridge music theory bible reference production" },
    { title: "Buffer Size", url: "/bible/buffer-size", tags: "buffer size recording bible reference production" },
    { title: "Bus", url: "/bible/bus", tags: "bus mixing bible reference production" },
    { title: "Bus Compression", url: "/bible/bus-compression", tags: "bus compression dynamics bible reference production" },
    { title: "Call and Response", url: "/bible/call-and-response", tags: "call and response music theory bible reference production" },
    { title: "Chop", url: "/bible/chop", tags: "chop production bible reference production" },
    { title: "Chord", url: "/bible/chord", tags: "chord music theory bible reference production" },
    { title: "Chord Progression", url: "/bible/chord-progression", tags: "chord progression music theory bible reference production" },
    { title: "Chorus", url: "/bible/chorus", tags: "chorus time-based bible reference production" },
    { title: "Chorus", url: "/bible/chorus-section", tags: "chorus music theory bible reference production" },
    { title: "Clip", url: "/bible/clip", tags: "clip recording bible reference production" },
    { title: "Clip Gain", url: "/bible/clip-gain", tags: "clip gain signal processing bible reference production" },
    { title: "Clipping", url: "/bible/clipping", tags: "clipping signal processing bible reference production" },
    { title: "Clocking", url: "/bible/clocking", tags: "clocking signal processing bible reference production" },
    { title: "Compression", url: "/bible/compression", tags: "compression dynamics bible reference production" },
    { title: "Compression Ratio", url: "/bible/compression-ratio", tags: "compression ratio dynamics bible reference production" },
    { title: "Condenser Microphone", url: "/bible/condenser-microphone", tags: "condenser microphone recording bible reference production" },
    { title: "Convolution Reverb", url: "/bible/convolution-reverb", tags: "convolution reverb time-based bible reference production" },
    { title: "DAW", url: "/bible/daw", tags: "daw production bible reference production" },
    { title: "DAW Workflow", url: "/bible/daw-workflow", tags: "daw workflow production bible reference production" },
    { title: "dBFS", url: "/bible/dbfs", tags: "dbfs signal processing bible reference production" },
    { title: "De-Esser", url: "/bible/de-esser", tags: "de-esser dynamics bible reference production" },
    { title: "Decay", url: "/bible/decay", tags: "decay synthesis bible reference production" },
    { title: "Delay", url: "/bible/delay", tags: "delay time-based bible reference production" },
    { title: "Detune", url: "/bible/detune", tags: "detune synthesis bible reference production" },
    { title: "DI Box", url: "/bible/di-box", tags: "di box recording bible reference production" },
    { title: "Digital", url: "/bible/digital", tags: "digital signal processing bible reference production" },
    { title: "Distortion", url: "/bible/distortion", tags: "distortion signal processing bible reference production" },
    { title: "Dithering", url: "/bible/dithering", tags: "dithering mastering bible reference production" },
    { title: "Drill", url: "/bible/drill", tags: "drill production bible reference production" },
    { title: "Drop", url: "/bible/drop", tags: "drop music theory bible reference production" },
    { title: "Dynamic EQ", url: "/bible/dynamic-eq", tags: "dynamic eq dynamics bible reference production" },
    { title: "Dynamic Microphone", url: "/bible/dynamic-microphone", tags: "dynamic microphone recording bible reference production" },
    { title: "Dynamic Range", url: "/bible/dynamic-range", tags: "dynamic range dynamics bible reference production" },
    { title: "Envelope", url: "/bible/envelope", tags: "envelope synthesis bible reference production" },
    { title: "Eq", url: "/bible/eq", tags: "eq frequency bible reference production" },
    { title: "Exciter", url: "/bible/exciter", tags: "exciter dynamics bible reference production" },
    { title: "Expansion", url: "/bible/expansion", tags: "expansion dynamics bible reference production" },
    { title: "Fader", url: "/bible/fader", tags: "fader mixing bible reference production" },
    { title: "Feedback", url: "/bible/feedback", tags: "feedback signal processing bible reference production" },
    { title: "FET Compressor", url: "/bible/fet-compressor", tags: "fet compressor dynamics bible reference production" },
    { title: "Filter", url: "/bible/filter", tags: "filter frequency bible reference production" },
    { title: "Flanger", url: "/bible/flanger", tags: "flanger time-based bible reference production" },
    { title: "FM Synthesis", url: "/bible/fm-synthesis", tags: "fm synthesis synthesis bible reference production" },
    { title: "Freeze", url: "/bible/freeze", tags: "freeze mixing bible reference production" },
    { title: "Frequency", url: "/bible/frequency", tags: "frequency frequency bible reference production" },
    { title: "Frequency Masking", url: "/bible/frequency-masking", tags: "frequency masking frequency bible reference production" },
    { title: "Fundamental Frequency", url: "/bible/fundamental", tags: "fundamental frequency frequency bible reference production" },
    { title: "Gain", url: "/bible/gain", tags: "gain signal processing bible reference production" },
    { title: "Gain Reduction", url: "/bible/gain-reduction", tags: "gain reduction dynamics bible reference production" },
    { title: "Gain Staging", url: "/bible/gain-staging", tags: "gain staging mixing bible reference production" },
    { title: "Gain Structure", url: "/bible/gain-structure", tags: "gain structure mixing bible reference production" },
    { title: "Glue", url: "/bible/glue", tags: "glue mixing bible reference production" },
    { title: "Granular Synthesis", url: "/bible/granular-synthesis", tags: "granular synthesis synthesis bible reference production" },
    { title: "Graphic EQ", url: "/bible/graphic-eq", tags: "graphic eq frequency bible reference production" },
    { title: "Groove", url: "/bible/groove", tags: "groove music theory bible reference production" },
    { title: "Hall Reverb", url: "/bible/hall-reverb", tags: "hall reverb time-based bible reference production" },
    { title: "Harmonic", url: "/bible/harmonic", tags: "harmonic signal processing bible reference production" },
    { title: "Harmonic Distortion", url: "/bible/harmonic-distortion", tags: "harmonic distortion frequency bible reference production" },
    { title: "Harmony", url: "/bible/harmony", tags: "harmony music theory bible reference production" },
    { title: "Headroom", url: "/bible/headroom", tags: "headroom mixing bible reference production" },
    { title: "High-Pass Filter", url: "/bible/high-pass-filter", tags: "high-pass filter frequency bible reference production" },
    { title: "Hook", url: "/bible/hook", tags: "hook music theory bible reference production" },
    { title: "Humanization", url: "/bible/humanization", tags: "humanization mixing bible reference production" },
    { title: "Impedance", url: "/bible/impedance", tags: "impedance signal processing bible reference production" },
    { title: "Instrument Track", url: "/bible/instrument-track", tags: "instrument track mixing bible reference production" },
    { title: "Integrated Loudness", url: "/bible/integrated-loudness", tags: "integrated loudness mastering bible reference production" },
    { title: "Interval", url: "/bible/interval", tags: "interval music theory bible reference production" },
    { title: "Intro", url: "/bible/intro", tags: "intro music theory bible reference production" },
    { title: "Key", url: "/bible/key", tags: "key music theory bible reference production" },
    { title: "Knee", url: "/bible/knee", tags: "knee dynamics bible reference production" },
    { title: "Latency", url: "/bible/latency", tags: "latency recording bible reference production" },
    { title: "Layering", url: "/bible/layering", tags: "layering mixing bible reference production" },
    { title: "LFO", url: "/bible/lfo", tags: "lfo synthesis bible reference production" },
    { title: "Limiting", url: "/bible/limiting", tags: "limiting dynamics bible reference production" },
    { title: "Linear Phase EQ", url: "/bible/linear-phase-eq", tags: "linear phase eq frequency bible reference production" },
    { title: "Lo-Fi", url: "/bible/lo-fi", tags: "lo-fi production bible reference production" },
    { title: "Loudness", url: "/bible/loudness", tags: "loudness mastering bible reference production" },
    { title: "Loudness Matching", url: "/bible/loudness-matching", tags: "loudness matching mixing bible reference production" },
    { title: "Loudness Normalization", url: "/bible/loudness-normalization", tags: "loudness normalization mastering bible reference production" },
    { title: "Loudness War", url: "/bible/loudness-war", tags: "loudness war mastering bible reference production" },
    { title: "Low-Pass Filter", url: "/bible/low-pass-filter", tags: "low-pass filter frequency bible reference production" },
    { title: "LUFS", url: "/bible/lufs", tags: "lufs mastering bible reference production" },
    { title: "Makeup Gain", url: "/bible/makeup-gain", tags: "makeup gain dynamics bible reference production" },
    { title: "Master Limiter", url: "/bible/master-limiter", tags: "master limiter dynamics bible reference production" },
    { title: "Mastering", url: "/bible/mastering", tags: "mastering mastering bible reference production" },
    { title: "Melody", url: "/bible/melody", tags: "melody music theory bible reference production" },
    { title: "Meter", url: "/bible/meter", tags: "meter music theory bible reference production" },
    { title: "Microphone Placement", url: "/bible/microphone-placement", tags: "microphone placement recording bible reference production" },
    { title: "Mid-Side EQ", url: "/bible/mid-side-eq", tags: "mid-side eq frequency bible reference production" },
    { title: "Mid-Side Processing", url: "/bible/mid-side-processing", tags: "mid-side processing mixing bible reference production" },
    { title: "MIDI", url: "/bible/midi", tags: "midi production bible reference production" },
    { title: "Mix Bus", url: "/bible/mix-bus", tags: "mix bus mixing bible reference production" },
    { title: "Mix Translation", url: "/bible/mix-translation", tags: "mix translation mixing bible reference production" },
    { title: "Mixing", url: "/bible/mixing", tags: "mixing mixing bible reference production" },
    { title: "Mode", url: "/bible/mode", tags: "mode music theory bible reference production" },
    { title: "Modulation", url: "/bible/modulation", tags: "modulation time-based bible reference production" },
    { title: "Mono Compatibility", url: "/bible/mono-compatibility", tags: "mono compatibility mixing bible reference production" },
    { title: "Mud", url: "/bible/mud", tags: "mud frequency bible reference production" },
    { title: "Multiband Compression", url: "/bible/multiband-compression", tags: "multiband compression dynamics bible reference production" },
    { title: "Music Theory", url: "/bible/music-theory", tags: "music theory music theory bible reference production" },
    { title: "Noise Floor", url: "/bible/noise-floor", tags: "noise floor signal processing bible reference production" },
    { title: "Noise Gate", url: "/bible/noise-gate", tags: "noise gate dynamics bible reference production" },
    { title: "Notch Filter", url: "/bible/notch-filter", tags: "notch filter frequency bible reference production" },
    { title: "Octave", url: "/bible/octave", tags: "octave music theory bible reference production" },
    { title: "Optical Compressor", url: "/bible/optical-compressor", tags: "optical compressor dynamics bible reference production" },
    { title: "Oscillator", url: "/bible/oscillator", tags: "oscillator synthesis bible reference production" },
    { title: "Outro", url: "/bible/outro", tags: "outro music theory bible reference production" },
    { title: "Overdrive", url: "/bible/overdrive", tags: "overdrive signal processing bible reference production" },
    { title: "Panning", url: "/bible/panning", tags: "panning mixing bible reference production" },
    { title: "Parallel Compression", url: "/bible/parallel-compression", tags: "parallel compression dynamics bible reference production" },
    { title: "Parallel Processing", url: "/bible/parallel-processing", tags: "parallel processing mixing bible reference production" },
    { title: "Parametric EQ", url: "/bible/parametric-eq", tags: "parametric eq frequency bible reference production" },
    { title: "Patch", url: "/bible/patch", tags: "patch mixing bible reference production" },
    { title: "PDC", url: "/bible/pdc", tags: "pdc recording bible reference production" },
    { title: "Peak", url: "/bible/peak", tags: "peak signal processing bible reference production" },
    { title: "Phantom Power", url: "/bible/phantom-power", tags: "phantom power recording bible reference production" },
    { title: "Phase", url: "/bible/phase", tags: "phase signal processing bible reference production" },
    { title: "Phase Cancellation", url: "/bible/phase-cancellation", tags: "phase cancellation signal processing bible reference production" },
    { title: "Phaser", url: "/bible/phaser", tags: "phaser time-based bible reference production" },
    { title: "Phonk", url: "/bible/phonk", tags: "phonk production bible reference production" },
    { title: "Ping-Pong Delay", url: "/bible/ping-pong-delay", tags: "ping-pong delay time-based bible reference production" },
    { title: "Pitch", url: "/bible/pitch", tags: "pitch music theory bible reference production" },
    { title: "Pitch Shifting", url: "/bible/pitch-shifting", tags: "pitch shifting time-based bible reference production" },
    { title: "Plate Reverb", url: "/bible/plate-reverb", tags: "plate reverb time-based bible reference production" },
    { title: "Plugin", url: "/bible/plugin", tags: "plugin synthesis bible reference production" },
    { title: "Polar Pattern", url: "/bible/polar-pattern", tags: "polar pattern recording bible reference production" },
    { title: "Polyrhythm", url: "/bible/polyrhythm", tags: "polyrhythm music theory bible reference production" },
    { title: "Portamento", url: "/bible/portamento", tags: "portamento synthesis bible reference production" },
    { title: "Pre-Delay", url: "/bible/pre-delay", tags: "pre-delay time-based bible reference production" },
    { title: "Preamp", url: "/bible/preamp", tags: "preamp recording bible reference production" },
    { title: "Presence", url: "/bible/presence", tags: "presence frequency bible reference production" },
    { title: "Q Factor", url: "/bible/q-factor", tags: "q factor frequency bible reference production" },
    { title: "Quantization", url: "/bible/quantization", tags: "quantization production bible reference production" },
    { title: "Ratio", url: "/bible/ratio", tags: "ratio dynamics bible reference production" },
    { title: "Recording", url: "/bible/recording", tags: "recording recording bible reference production" },
    { title: "Reference Mastering", url: "/bible/reference-mastering", tags: "reference mastering mastering bible reference production" },
    { title: "Reference Track", url: "/bible/reference-track", tags: "reference track mixing bible reference production" },
    { title: "Release", url: "/bible/release", tags: "release dynamics bible reference production" },
    { title: "Resonance", url: "/bible/resonance", tags: "resonance frequency bible reference production" },
    { title: "Return Track", url: "/bible/return-track", tags: "return track mixing bible reference production" },
    { title: "Reverb", url: "/bible/reverb", tags: "reverb time-based bible reference production" },
    { title: "Rhythm", url: "/bible/rhythm", tags: "rhythm music theory bible reference production" },
    { title: "RMS", url: "/bible/rms", tags: "rms signal processing bible reference production" },
    { title: "Room Reverb", url: "/bible/room-reverb", tags: "room reverb time-based bible reference production" },
    { title: "Sample Flip", url: "/bible/sample-flip", tags: "sample flip production bible reference production" },
    { title: "Sample Rate", url: "/bible/sample-rate", tags: "sample rate signal processing bible reference production" },
    { title: "Sampling", url: "/bible/sampling", tags: "sampling production bible reference production" },
    { title: "Saturation", url: "/bible/saturation", tags: "saturation signal processing bible reference production" },
    { title: "Scale", url: "/bible/scale", tags: "scale music theory bible reference production" },
    { title: "Send and Return", url: "/bible/send-return", tags: "send and return mixing bible reference production" },
    { title: "Shelf EQ", url: "/bible/shelf", tags: "shelf eq frequency bible reference production" },
    { title: "Shelving EQ", url: "/bible/shelving-eq", tags: "shelving eq frequency bible reference production" },
    { title: "Shimmer Reverb", url: "/bible/shimmer-reverb", tags: "shimmer reverb time-based bible reference production" },
    { title: "Short-Term Loudness", url: "/bible/short-term-loudness", tags: "short-term loudness mastering bible reference production" },
    { title: "Sidechain", url: "/bible/sidechain", tags: "sidechain dynamics bible reference production" },
    { title: "Sidechain Compression", url: "/bible/sidechain-compression", tags: "sidechain compression dynamics bible reference production" },
    { title: "Signal Chain", url: "/bible/signal-chain", tags: "signal chain mixing bible reference production" },
    { title: "Slapback Delay", url: "/bible/slapback-delay", tags: "slapback delay time-based bible reference production" },
    { title: "Sound Design", url: "/bible/sound-design", tags: "sound design synthesis bible reference production" },
    { title: "Space", url: "/bible/space", tags: "space mixing bible reference production" },
    { title: "Spring Reverb", url: "/bible/spring-reverb", tags: "spring reverb time-based bible reference production" },
    { title: "Stem", url: "/bible/stem", tags: "stem mixing bible reference production" },
    { title: "Stem Mastering", url: "/bible/stem-mastering", tags: "stem mastering mastering bible reference production" },
    { title: "Stereo Imaging", url: "/bible/stereo-imaging", tags: "stereo imaging mixing bible reference production" },
    { title: "Stereo Width", url: "/bible/stereo-width", tags: "stereo width mixing bible reference production" },
    { title: "Sub Frequency", url: "/bible/subfrequency", tags: "sub frequency frequency bible reference production" },
    { title: "Subtractive Synthesis", url: "/bible/subtractive-synthesis", tags: "subtractive synthesis synthesis bible reference production" },
    { title: "Summing", url: "/bible/summing", tags: "summing mixing bible reference production" },
    { title: "Swing", url: "/bible/swing", tags: "swing music theory bible reference production" },
    { title: "Syncopation", url: "/bible/syncopation", tags: "syncopation music theory bible reference production" },
    { title: "Tempo Sync", url: "/bible/tempo-sync", tags: "tempo sync music theory bible reference production" },
    { title: "Tension & Release", url: "/bible/tension-release", tags: "tension & release music theory bible reference production" },
    { title: "The Pocket", url: "/bible/the-pocket", tags: "the pocket music theory bible reference production" },
    { title: "Threshold", url: "/bible/threshold", tags: "threshold dynamics bible reference production" },
    { title: "Timbre", url: "/bible/timbre", tags: "timbre music theory bible reference production" },
    { title: "Time Signature", url: "/bible/time-signature", tags: "time signature music theory bible reference production" },
    { title: "Time Stretching", url: "/bible/time-stretching", tags: "time stretching time-based bible reference production" },
    { title: "Transient", url: "/bible/transient", tags: "transient dynamics bible reference production" },
    { title: "Transient Shaper", url: "/bible/transient-shaper", tags: "transient shaper dynamics bible reference production" },
    { title: "Transient Shaping", url: "/bible/transient-shaping", tags: "transient shaping dynamics bible reference production" },
    { title: "Trap", url: "/bible/trap", tags: "trap production bible reference production" },
    { title: "Tremolo", url: "/bible/tremolo", tags: "tremolo time-based bible reference production" },
    { title: "True Peak", url: "/bible/true-peak", tags: "true peak mastering bible reference production" },
    { title: "True Peak Limiting", url: "/bible/true-peak-limiting", tags: "true peak limiting mastering bible reference production" },
    { title: "Tube Compressor", url: "/bible/tube-compressor", tags: "tube compressor dynamics bible reference production" },
    { title: "Unison", url: "/bible/unison", tags: "unison synthesis bible reference production" },
    { title: "VCA Compressor", url: "/bible/vca-compressor", tags: "vca compressor dynamics bible reference production" },
    { title: "Velocity", url: "/bible/velocity", tags: "velocity synthesis bible reference production" },
    { title: "Verse", url: "/bible/verse", tags: "verse music theory bible reference production" },
    { title: "Vibrato", url: "/bible/vibrato", tags: "vibrato time-based bible reference production" },
    { title: "Vocal Production", url: "/bible/vocal-production", tags: "vocal production recording bible reference production" },
    { title: "Vocoder", url: "/bible/vocoder", tags: "vocoder synthesis bible reference production" },
    { title: "VST", url: "/bible/vst", tags: "vst synthesis bible reference production" },
    { title: "Waveform", url: "/bible/waveform", tags: "waveform signal processing bible reference production" },
    { title: "Wavetable", url: "/bible/wavetable", tags: "wavetable synthesis bible reference production" },
    { title: "Wavetable Synthesis", url: "/bible/wavetable-synthesis", tags: "wavetable synthesis synthesis bible reference production" },
    { title: "Wet/Dry", url: "/bible/wet-dry", tags: "wet/dry mixing bible reference production" },
    { title: "White Noise", url: "/bible/white-noise", tags: "white noise signal processing bible reference production" },
    { title: "808 Sub Bass Tuner", url: "/tools/808-sub-bass-tuner", tags: "808 sub bass tuner tool calculator reference production" },
    { title: "ADSR Visualizer", url: "/tools/adsr-visualizer", tags: "adsr visualizer tool calculator reference production" },
    { title: "AI Copyright Strength", url: "/tools/ai-copyright-strength", tags: "ai copyright strength tool calculator reference production" },
    { title: "AI Music DDEX Checker", url: "/tools/ai-music-ddex-checker", tags: "ai music ddex checker tool calculator reference production" },
    { title: "AI Music Rights Navigator", url: "/tools/ai-music-rights-navigator", tags: "ai music rights navigator tool calculator reference production" },
    { title: "Arrangement Timer", url: "/tools/arrangement-timer", tags: "arrangement timer tool calculator reference production" },
    { title: "Attack Release Calculator", url: "/tools/attack-release-calculator", tags: "attack release calculator tool calculator reference production" },
    { title: "Chord Key Reference", url: "/tools/chord-key-reference", tags: "chord key reference tool calculator reference production" },
    { title: "Delay Time Calculator", url: "/tools/delay-time-calculator", tags: "delay time calculator tool calculator reference production" },
    { title: "EQ Problem Solver", url: "/tools/eq-problem-solver", tags: "eq problem solver tool calculator reference production" },
    { title: "Frequency Conflict Detector", url: "/tools/frequency-conflict-detector", tags: "frequency conflict detector tool calculator reference production" },
    { title: "Frequency Eq Reference", url: "/tools/frequency-eq-reference", tags: "frequency eq reference tool calculator reference production" },
    { title: "Gain Reduction Calculator", url: "/tools/gain-reduction-calculator", tags: "gain reduction calculator tool calculator reference production" },
    { title: "Gain Staging Reference", url: "/tools/gain-staging-reference", tags: "gain staging reference tool calculator reference production" },
    { title: "Headroom Calculator", url: "/tools/headroom-calculator", tags: "headroom calculator tool calculator reference production" },
    { title: "LFO Sync Calculator", url: "/tools/lfo-sync-calculator", tags: "lfo sync calculator tool calculator reference production" },
    { title: "LUFS Target Reference", url: "/tools/lufs-target-reference", tags: "lufs target reference tool calculator reference production" },
    { title: "Mastering Signal Chain", url: "/tools/mastering-signal-chain", tags: "mastering signal chain tool calculator reference production" },
    { title: "Mix Bus Headroom Reference", url: "/tools/mix-bus-headroom-reference", tags: "mix bus headroom reference tool calculator reference production" },
    { title: "Mix Bus Signal Flow", url: "/tools/mix-bus-signal-flow", tags: "mix bus signal flow tool calculator reference production" },
    { title: "Note To Frequency", url: "/tools/note-to-frequency", tags: "note to frequency tool calculator reference production" },
    { title: "Parallel Processing Calculator", url: "/tools/parallel-processing-calculator", tags: "parallel processing calculator tool calculator reference production" },
    { title: "Pitch Correction Reference", url: "/tools/pitch-correction-reference", tags: "pitch correction reference tool calculator reference production" },
    { title: "Pre Delay Reverb Calculator", url: "/tools/pre-delay-reverb-calculator", tags: "pre delay reverb calculator tool calculator reference production" },
    { title: "Pre Delivery Checklist", url: "/tools/pre-delivery-checklist", tags: "pre delivery checklist tool calculator reference production" },
    { title: "Reverb Type Selector", url: "/tools/reverb-type-selector", tags: "reverb type selector tool calculator reference production" },
    { title: "RT60 Calculator", url: "/tools/rt60-calculator", tags: "rt60 calculator tool calculator reference production" },
    { title: "Sample Rate Bit Depth Guide", url: "/tools/sample-rate-bit-depth-guide", tags: "sample rate bit depth guide tool calculator reference production" },
    { title: "Saturation Character Reference", url: "/tools/saturation-character-reference", tags: "saturation character reference tool calculator reference production" },
    { title: "Saturation Harmonic Reference", url: "/tools/saturation-harmonic-reference", tags: "saturation harmonic reference tool calculator reference production" },
    { title: "Sidechain Compression Designer", url: "/tools/sidechain-compression-designer", tags: "sidechain compression designer tool calculator reference production" },
    { title: "Sidechain Ducking Reference", url: "/tools/sidechain-ducking-reference", tags: "sidechain ducking reference tool calculator reference production" },
    { title: "Stereo Field Mono Checker", url: "/tools/stereo-field-mono-checker", tags: "stereo field mono checker tool calculator reference production" },
    { title: "Stereo Width M/S", url: "/tools/stereo-width-ms", tags: "stereo width ms tool calculator reference production" },
    { title: "Suno Credits Calculator", url: "/tools/suno-credits-calculator", tags: "suno credits calculator tool calculator reference production" },
    { title: "Suno Prompt Optimizer", url: "/tools/suno-prompt-optimizer", tags: "suno prompt optimizer tool calculator reference production" },
    { title: "Synthesis Parameter Reference", url: "/tools/synthesis-parameter-reference", tags: "synthesis parameter reference tool calculator reference production" },
    { title: "Synthesis Type Selector", url: "/tools/synthesis-type-selector", tags: "synthesis type selector tool calculator reference production" },
    { title: "Tempo Key Chord Reference", url: "/tools/tempo-key-chord-reference", tags: "tempo key chord reference tool calculator reference production" },
    { title: "Transient Shaper Reference", url: "/tools/transient-shaper-reference", tags: "transient shaper reference tool calculator reference production" },
    { title: "Vocal Chain Builder", url: "/tools/vocal-chain-builder", tags: "vocal chain builder tool calculator reference production" },
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
        let score = 0;
        words.forEach(word => {
          if (article.title.toLowerCase().includes(word)) score += 3;
          else if (haystack.includes(word)) score += 1;
        });
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

    const dropdown = document.createElement('div');
    dropdown.className = 'search-dropdown';
    dropdown.setAttribute('role', 'listbox');
    dropdown.setAttribute('aria-label', 'Search results');
    formEl.style.position = 'relative';
    formEl.appendChild(dropdown);

    if (!document.getElementById('search-dropdown-styles')) {
      const style = document.createElement('style');
      style.id = 'search-dropdown-styles';
      style.textContent = `
        .search-dropdown { display: none; position: absolute; top: calc(100% + 6px); left: 0; right: 0; background: var(--bg-elevated, #1a2332); border: 1px solid var(--teal, #00d4a8); border-radius: 10px; z-index: 999; overflow: hidden; box-shadow: 0 8px 32px rgba(0,0,0,0.4); min-width: 280px; }
        .search-dropdown.open { display: block; }
        .search-result-item { display: block; padding: 10px 14px; color: var(--text-primary, #e2e8f0); text-decoration: none; font-size: 0.88rem; font-family: var(--font-body, 'Outfit', sans-serif); border-bottom: 1px solid rgba(255,255,255,0.06); transition: background 0.15s; cursor: pointer; }
        .search-result-item:last-child { border-bottom: none; }
        .search-result-item:hover, .search-result-item.focused { background: rgba(0, 212, 168, 0.12); color: var(--teal, #00d4a8); }
        .search-no-results { padding: 12px 14px; color: var(--text-secondary, #8899aa); font-size: 0.85rem; font-family: var(--font-body, 'Outfit', sans-serif); }
        .search-dropdown-label { padding: 8px 14px 4px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.08em; color: var(--teal, #00d4a8); font-weight: 600; }
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
      results.forEach((article) => {
        const a = document.createElement('a');
        a.className = 'search-result-item';
        a.href = (article.url.startsWith("/") ? window.location.origin + article.url : article.url);
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

    formEl.addEventListener('submit', (e) => {
      e.preventDefault();
      const q = inputEl.value.trim();
      if (q.length >= 2) {
        const results = searchArticles(q);
        showResults(results);
      }
    });

    document.addEventListener('click', (e) => {
      if (!formEl.contains(e.target)) hideResults();
    });

    inputEl.addEventListener('blur', () => {
      setTimeout(hideResults, 200);
    });
  }

  /* ------------------------------------------------
     INIT ALL SEARCH FORMS ON PAGE
     ------------------------------------------------ */
  const desktopInput = document.getElementById('siteSearch');
  const desktopForm = desktopInput ? desktopInput.closest('.search-form') : null;
  buildSearchUI(desktopInput, desktopForm);

  const mobileInput = document.getElementById('mobileSearch');
  const mobileForm = mobileInput ? mobileInput.closest('.search-form') : null;
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

/* ------------------------------------------------
   OLD-STRUCTURE MOBILE NAV TOGGLE
   ------------------------------------------------ */
(function() {
  var oldToggle = document.querySelector('.mobile-nav-toggle');
  var oldNav = document.getElementById('mainNav');
  if (!oldToggle || !oldNav) return;
  oldToggle.addEventListener('click', function() {
    var isOpen = oldNav.classList.toggle('open');
    oldToggle.setAttribute('aria-expanded', String(isOpen));
    oldToggle.textContent = isOpen ? '✕' : '☰';
    document.body.style.overflow = isOpen ? 'hidden' : '';
  });
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && oldNav.classList.contains('open')) {
      oldNav.classList.remove('open');
      oldToggle.setAttribute('aria-expanded', 'false');
      oldToggle.textContent = '☰';
      document.body.style.overflow = '';
    }
  });
  oldNav.querySelectorAll('a').forEach(function(link) {
    link.addEventListener('click', function() {
      oldNav.classList.remove('open');
      oldToggle.setAttribute('aria-expanded', 'false');
      oldToggle.textContent = '☰';
      document.body.style.overflow = '';
    });
  });
  document.addEventListener('click', function(e) {
    if (oldNav.classList.contains('open') && !oldNav.contains(e.target) && e.target !== oldToggle) {
      oldNav.classList.remove('open');
      oldToggle.setAttribute('aria-expanded', 'false');
      oldToggle.textContent = '☰';
      document.body.style.overflow = '';
    }
  });
})();

/* ============================================================
   NAV LINK ABSOLUTE PATH FIX
   ============================================================ */
(function fixNavLinks() {
  const fixMap = {
    'index.html': '/', '../index.html': '/',
    'about.html': '/about.html', '../about.html': '/about.html',
    'categories/reviews.html': '/categories/reviews.html', '../categories/reviews.html': '/categories/reviews.html',
    'categories/comparisons.html': '/categories/comparisons.html', '../categories/comparisons.html': '/categories/comparisons.html',
    'categories/ai-music.html': '/categories/ai-music.html', '../categories/ai-music.html': '/categories/ai-music.html',
    'categories/daws.html': '/categories/daws.html', '../categories/daws.html': '/categories/daws.html',
    'categories/plugins.html': '/categories/plugins.html', '../categories/plugins.html': '/categories/plugins.html',
    'categories/gear.html': '/categories/gear.html', '../categories/gear.html': '/categories/gear.html',
    'categories/techniques.html': '/categories/techniques.html', '../categories/techniques.html': '/categories/techniques.html',
    'categories/music-business.html': '/categories/music-business.html', '../categories/music-business.html': '/categories/music-business.html',
    'categories/glossary.html': '/categories/glossary.html', '../categories/glossary.html': '/categories/glossary.html',
    'css/style.css': '/css/style.css', '../css/style.css': '/css/style.css',
    'js/main.js': '/js/main.js', '../js/main.js': '/js/main.js'
  };
  document.querySelectorAll('nav a, header a, .site-nav a, .breadcrumb a').forEach(function(a) {
    const href = a.getAttribute('href');
    if (href && fixMap[href]) a.setAttribute('href', fixMap[href]);
  });
  document.querySelectorAll('link[rel="stylesheet"]').forEach(function(link) {
    const href = link.getAttribute('href');
    if (href && fixMap[href]) link.setAttribute('href', fixMap[href]);
  });
})();

/* mpw-sidebar-ra-disabled-s17 — disabled S17 */
if(false) {
/* ── SIDEBAR RELATED ARTICLES WIDGET ────────────────────────────────── */
(function() {
  const aside = document.querySelector('aside');
  if (!aside) return;
  const relatedH2 = Array.from(document.querySelectorAll('article h2')).find(h =>
    h.textContent.toLowerCase().includes('related')
  );
  if (!relatedH2) return;
  const cards = relatedH2.parentElement
    ? Array.from(relatedH2.parentElement.querySelectorAll('a[href]'))
    : Array.from((relatedH2.nextElementSibling || document.createElement('div')).querySelectorAll('a[href]'));
  if (!cards.length) return;
  const links = cards.slice(0, 4).map(a => {
    const rawText = a.textContent.trim().replace(/Read article\s*→/gi, '').replace(/AI Music|Techniques|Reviews|Comparisons|Gear|Plugins/g, '').trim();
    const title = rawText.substring(0, 55) + (rawText.length > 55 ? '…' : '');
    return '<li><a href="' + a.getAttribute('href') + '">' + title + '</a></li>';
  }).join('');
  const widget = document.createElement('div');
  widget.className = 'sidebar-widget';
  widget.innerHTML = '<div class="sidebar-widget-header"><h2 class="sidebar-widget-title">Related Articles</h2></div>'
    + '<div class="sidebar-widget-body"><ul class="sidebar-list" style="padding:0.25rem 0">' + links + '</ul></div>';
  aside.appendChild(widget);
})();
}

/* ---- LAYOUT FIXES ---- */
(function applyLayoutFixes() {
  function fix() {
    const aside = document.querySelector('.article-layout aside');
    if (aside && !aside.classList.contains('article-sidebar')) {
      aside.classList.add('article-sidebar');
    }
    const dropdown = document.querySelector('.search-dropdown');
    if (dropdown) {
      dropdown.style.right = '0';
      dropdown.style.left = 'auto';
      dropdown.style.overflow = 'visible';
    }
    const headerInner = document.querySelector('.header-inner');
    if (headerInner) headerInner.style.overflow = 'visible';
    if (window.innerWidth <= 900 && aside) {
      aside.style.display = 'none';
    }
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', fix);
  } else {
    fix();
  }
  window.addEventListener('resize', function() {
    const aside = document.querySelector('.article-layout aside');
    if (aside) aside.style.display = window.innerWidth <= 900 ? 'none' : '';
  });
})();
