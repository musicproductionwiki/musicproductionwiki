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
    { title: "Ableton Live 12 Review", url: "/articles/ableton-live-12-review.html", tags: "daw ableton review" },
    { title: "Ableton Live 12 vs 11", url: "/articles/ableton-live-12-vs-11.html", tags: "daw ableton comparison" },
    { title: "Ableton Live 12 vs FL Studio 21", url: "/articles/ableton-live-12-vs-fl-studio-21.html", tags: "daw ableton fl studio comparison" },
    { title: "Ableton Live Beginner's Guide", url: "/articles/ableton-live-beginners-guide.html", tags: "daw ableton beginners guide" },
    { title: "Ableton Live Review", url: "/articles/ableton-live-review.html", tags: "daw ableton review" },
    { title: "Ableton Live Tips and Tricks", url: "/articles/ableton-live-tips-and-tricks.html", tags: "daw ableton tips tricks techniques" },
    { title: "Ableton Push 3 Review", url: "/articles/ableton-push-3-review.html", tags: "ableton push 3 review hardware gear" },
    { title: "Ableton Push 3 Standalone Review", url: "/articles/ableton-push-3-standalone-review.html", tags: "hardware push standalone review" },
    { title: "Ableton Push 3 vs Maschine MK3", url: "/articles/ableton-push-3-vs-maschine-mk3.html", tags: "comparison push maschine hardware" },
    { title: "Ableton vs Logic Pro for Beginners", url: "/articles/ableton-vs-logic-pro-for-beginners.html", tags: "ableton logic pro beginners comparison daw" },
    { title: "Ableton vs Pro Tools", url: "/articles/ableton-vs-pro-tools.html", tags: "comparison daw ableton pro tools" },
    { title: "Adam Audio T5V Review", url: "/articles/adam-audio-t5v-review.html", tags: "adam audio monitors review gear" },
    { title: "Adam Audio T7V Review", url: "/articles/adam-audio-t7v-review.html", tags: "adam audio monitors review gear" },
    { title: "AI Chord Progression Tools", url: "/articles/ai-chord-progression-tools.html", tags: "ai chord tools music" },
    { title: "AI Music Production Tools: Complete Guide", url: "/articles/ai-music-production-tools-complete-guide.html", tags: "ai music production tools guide" },
    { title: "AI Stem Separation Guide", url: "/articles/ai-stem-separation-guide.html", tags: "ai stem separation guide" },
    { title: "Akai MPK Mini MK4 Review", url: "/articles/akai-mpk-mini-mk4-review.html", tags: "akai mpk mini midi controller review gear" },
    { title: "AKG C414 Review", url: "/articles/akg-c414-review.html", tags: "akg c414 microphone review gear" },
    { title: "AKG C414 XLII Review", url: "/articles/akg-c414-xlii-review.html", tags: "akg c414 xlii microphone review gear" },
    { title: "ASCAP vs BMI", url: "/articles/ascap-vs-bmi.html", tags: "pro royalties ascap bmi comparison music business" },
    { title: "Audio Interface Buying Guide", url: "/articles/audio-interface-buying-guide.html", tags: "audio interface buying guide gear" },
    { title: "Audio Interface vs Mixer", url: "/articles/audio-interface-vs-mixer.html", tags: "audio interface mixer comparison gear" },
    { title: "Auto-Tune vs Melodyne", url: "/articles/auto-tune-vs-melodyne.html", tags: "pitch correction autotune melodyne comparison" },
    { title: "Best AI Mixing Plugins 2026", url: "/articles/best-ai-mixing-plugins-2026.html", tags: "ai mixing plugins best 2026" },
    { title: "Best Audio Interface for Home Studio", url: "/articles/best-audio-interface-home-studio.html", tags: "audio interface home studio gear buying guide" },
    { title: "Best Audio Interfaces 2026", url: "/articles/best-audio-interfaces-2026.html", tags: "audio interfaces best 2026 gear" },
    { title: "Best Audio Interfaces for Guitarists", url: "/articles/best-audio-interfaces-for-guitarists.html", tags: "audio interfaces guitarists best gear" },
    { title: "Best Audio Interfaces Under $200", url: "/articles/best-audio-interfaces-under-200.html", tags: "audio interfaces budget best gear" },
    { title: "Best Budget Studio Gear 2026", url: "/articles/best-budget-studio-gear-2026.html", tags: "budget studio gear best 2026" },
    { title: "Best Compressor Plugins", url: "/articles/best-compressor-plugins.html", tags: "compressor plugins best buying guide" },
    { title: "Best DAW for Beginners", url: "/articles/best-daw-for-beginners.html", tags: "daw beginners best buying guide" },
    { title: "Best DAW for Hip Hop", url: "/articles/best-daw-for-hip-hop.html", tags: "daw hip hop best buying guide" },
    { title: "Best DAW for Beginners 2026", url: "/articles/best-daw-for-beginners-2026.html", tags: "daw beginners best 2026" },
    { title: "Best Free VST Plugins", url: "/articles/best-free-vst-plugins.html", tags: "free vst plugins best buying guide" },
    { title: "Best Laptops for Music Production", url: "/articles/best-laptops-for-music-production.html", tags: "laptops music production best gear" },
    { title: "Best Microphone for Home Studio", url: "/articles/best-microphone-home-studio.html", tags: "microphone home studio best gear buying guide" },
    { title: "Best MIDI Controllers", url: "/articles/best-midi-controllers.html", tags: "midi controllers best buying guide gear" },
    { title: "Best MIDI Controllers 2026", url: "/articles/best-midi-controllers-2026.html", tags: "midi controllers best 2026 gear" },
    { title: "Best Plugins for Beginners", url: "/articles/best-plugins-for-beginners.html", tags: "plugins beginners best buying guide" },
    { title: "Best Reverb Plugins", url: "/articles/best-reverb-plugins.html", tags: "reverb plugins best buying guide" },
    { title: "Best Studio Headphones for Music Production", url: "/articles/best-studio-headphones-music-production.html", tags: "headphones studio best gear buying guide" },
    { title: "Best Studio Monitors for Home Studio", url: "/articles/best-studio-monitors-home-studio.html", tags: "studio monitors home studio best gear buying guide" },
    { title: "Best Studio Monitors Under $500", url: "/articles/best-studio-monitors-under-500.html", tags: "studio monitors budget best gear" },
    { title: "Best Suno AI Prompts", url: "/articles/best-suno-ai-prompts.html", tags: "suno ai prompts best guide" },
    { title: "Best Vocal Microphones", url: "/articles/best-vocal-microphones.html", tags: "vocal microphones best buying guide gear" },
    { title: "Beyerdynamic DT 990 Pro Review", url: "/articles/beyerdynamic-dt-990-pro-review.html", tags: "beyerdynamic headphones review gear" },
    { title: "Bitwig Studio Review", url: "/articles/bitwig-studio-review.html", tags: "bitwig studio daw review" },
    { title: "Can You Copyright AI Music?", url: "/articles/can-you-copyright-ai-music.html", tags: "ai music copyright law music business" },
    { title: "Compressor Settings Guide", url: "/articles/compressor-settings-guide.html", tags: "compressor settings guide techniques" },
    { title: "Condenser vs Dynamic Microphone", url: "/articles/condenser-vs-dynamic-microphone.html", tags: "condenser dynamic microphone comparison gear" },
    { title: "DAW Comparison Guide", url: "/articles/daw-comparison-guide.html", tags: "daw comparison guide" },
    { title: "DistroKid vs TuneCore", url: "/articles/distrokid-vs-tunecore.html", tags: "distrokid tunecore distribution comparison music business" },
    { title: "Dynamic EQ vs Multiband Compression", url: "/articles/dynamic-eq-vs-multiband-compression.html", tags: "dynamic eq multiband compression comparison techniques" },
    { title: "EQ Cheat Sheet", url: "/articles/eq-cheat-sheet.html", tags: "eq cheat sheet guide techniques" },
    { title: "FabFilter Pro-C2 Review", url: "/articles/fabfilter-pro-c2-review.html", tags: "fabfilter compressor review plugins" },
    { title: "FabFilter Pro-DS Review", url: "/articles/fabfilter-pro-ds-review.html", tags: "fabfilter de-esser review plugins" },
    { title: "FabFilter Pro-L2 Review", url: "/articles/fabfilter-pro-l2-review.html", tags: "fabfilter limiter review plugins" },
    { title: "FabFilter Pro-MB Review", url: "/articles/fabfilter-pro-mb-review.html", tags: "fabfilter multiband compressor review plugins" },
    { title: "FabFilter Pro-Q3 Review", url: "/articles/fabfilter-pro-q3-review.html", tags: "fabfilter eq review plugins" },
    { title: "FabFilter Pro-R Review", url: "/articles/fabfilter-pro-r-review.html", tags: "fabfilter reverb review plugins" },
    { title: "FabFilter Pro-R2 Review", url: "/articles/fabfilter-pro-r2-review.html", tags: "fabfilter reverb review plugins" },
    { title: "FL Studio Beginner's Guide", url: "/articles/fl-studio-beginners-guide.html", tags: "fl studio beginners guide daw" },
    { title: "FL Studio Review", url: "/articles/fl-studio-review.html", tags: "fl studio review daw" },
    { title: "FL Studio Tips and Tricks", url: "/articles/fl-studio-tips-and-tricks.html", tags: "fl studio tips tricks techniques daw" },
    { title: "FL Studio vs Ableton", url: "/articles/fl-studio-vs-ableton.html", tags: "fl studio ableton comparison daw" },
    { title: "FL Studio vs Logic Pro", url: "/articles/fl-studio-vs-logic-pro.html", tags: "fl studio logic pro comparison daw" },
    { title: "FL Studio vs Pro Tools", url: "/articles/fl-studio-vs-pro-tools.html", tags: "fl studio pro tools comparison daw" },
    { title: "Focusrite Scarlett 2i2 Review", url: "/articles/focusrite-scarlett-2i2-review.html", tags: "focusrite scarlett audio interface review gear" },
    { title: "Focusrite Scarlett Solo Review", url: "/articles/focusrite-scarlett-solo-review.html", tags: "focusrite scarlett audio interface review gear" },
    { title: "Focusrite Scarlett vs Apollo Twin", url: "/articles/focusrite-scarlett-vs-apollo-twin.html", tags: "focusrite scarlett apollo twin comparison gear" },
    { title: "Frequency Masking Explained", url: "/articles/frequency-masking-explained.html", tags: "frequency masking explained techniques" },
    { title: "GarageBand vs Logic Pro", url: "/articles/garageband-vs-logic-pro.html", tags: "garageband logic pro comparison daw" },
    { title: "GarageBand vs FL Studio", url: "/articles/garageband-vs-fl-studio.html", tags: "garageband fl studio comparison daw" },
    { title: "Gain Staging Guide", url: "/articles/gain-staging-guide.html", tags: "gain staging guide techniques" },
    { title: "Headphones vs Studio Monitors", url: "/articles/headphones-vs-studio-monitors.html", tags: "headphones studio monitors comparison gear" },
    { title: "Home Recording Studio Setup", url: "/articles/home-recording-studio-setup.html", tags: "home studio setup recording gear guide" },
    { title: "How Music Royalties Work", url: "/articles/how-music-royalties-work.html", tags: "royalties music business how streaming" },
    { title: "How to Build a Fanbase", url: "/articles/how-to-build-a-fanbase.html", tags: "fanbase build how to music business marketing" },
    { title: "How to Build a Home Recording Studio", url: "/articles/how-to-build-a-home-recording-studio.html", tags: "home recording studio build how to gear" },
    { title: "How to Copyright Your Music", url: "/articles/how-to-copyright-your-music.html", tags: "copyright music law how to music business" },
    { title: "How to Distribute Music", url: "/articles/how-to-distribute-music.html", tags: "distribute music distribution how to music business" },
    { title: "How to EQ a Mix", url: "/articles/how-to-eq-a-mix.html", tags: "eq mix how to techniques" },
    { title: "How to EQ Drums", url: "/articles/how-to-eq-drums.html", tags: "eq drums how to techniques mixing" },
    { title: "How to Get a Record Deal", url: "/articles/how-to-get-a-record-deal.html", tags: "record deal music business how to" },
    { title: "How to Get More Streams on Spotify", url: "/articles/how-to-get-more-streams-on-spotify.html", tags: "spotify streams how to music business marketing" },
    { title: "How to Get Music on Spotify", url: "/articles/how-to-get-music-on-spotify.html", tags: "spotify music distribution how to music business" },
    { title: "How to License Your Music", url: "/articles/how-to-license-your-music.html", tags: "license music how to music business sync" },
    { title: "How to Make a Beat: Beginner's Guide", url: "/articles/how-to-make-a-beat-beginners-guide.html", tags: "beat making beginners how to techniques" },
    { title: "How to Make Lo-Fi Beats", url: "/articles/how-to-make-lo-fi-beats.html", tags: "lo-fi beats how to techniques making" },
    { title: "How to Make Money from Music", url: "/articles/how-to-make-money-from-music.html", tags: "money music income how to music business" },
    { title: "How to Make Money with AI Music", url: "/articles/how-to-make-money-with-ai-music.html", tags: "ai music money income how to" },
    { title: "How to Make Trap Beats", url: "/articles/how-to-make-trap-beats.html", tags: "trap beats how to techniques making" },
    { title: "How to Master a Song", url: "/articles/how-to-master-a-song.html", tags: "mastering how to master song techniques complete guide" },
    { title: "How to Master a Song at Home", url: "/articles/how-to-master-a-song-at-home.html", tags: "mastering at home how to techniques" },
    { title: "How to Mix Music: Beginner's Guide", url: "/articles/how-to-mix-music-beginners-guide.html", tags: "mixing music beginners how to techniques guide" },
    { title: "How to Mix Vocals", url: "/articles/how-to-mix-vocals.html", tags: "vocals mixing how to techniques" },
    { title: "How to Promote Music Independently", url: "/articles/how-to-promote-music-independently.html", tags: "promote music independently marketing how to music business" },
    { title: "How to Record Vocals at Home", url: "/articles/how-to-record-vocals-at-home.html", tags: "record vocals home studio how to techniques" },
    { title: "How to Use Auto-Tune", url: "/articles/how-to-use-autotune.html", tags: "autotune auto-tune how to techniques pitch" },
    { title: "How to Use Compression on Vocals", url: "/articles/how-to-use-compression-on-vocals.html", tags: "compression vocals how to techniques" },
    { title: "How to Use EQ on Drums", url: "/articles/how-to-use-eq-on-drums.html", tags: "eq drums how to techniques mixing" },
    { title: "How to Use Reverb in a Mix", url: "/articles/how-to-use-reverb-in-a-mix.html", tags: "reverb mix how to techniques" },
    { title: "iZotope Neutron Guide", url: "/articles/izotope-neutron-guide.html", tags: "izotope neutron mixing ai guide plugins" },
    { title: "iZotope Ozone 11 Review", url: "/articles/izotope-ozone-11-review.html", tags: "izotope ozone mastering review plugins" },
    { title: "iZotope RX Guide", url: "/articles/izotope-rx-guide.html", tags: "izotope rx audio repair guide plugins" },
    { title: "iZotope RX vs Waves Clarity", url: "/articles/izotope-rx-vs-waves-clarity.html", tags: "izotope rx waves clarity comparison plugins" },
    { title: "JBL 305P MkII Review", url: "/articles/jbl-305p-mkii-review.html", tags: "jbl studio monitors review gear" },
    { title: "KRK Rokit 5 G4 Review", url: "/articles/krk-rokit-5-g4-review.html", tags: "krk rokit monitors review gear" },
    { title: "LANDR vs iZotope Ozone", url: "/articles/landr-vs-izotope-ozone.html", tags: "landr izotope ozone mastering comparison ai" },
    { title: "Limiter vs Compressor", url: "/articles/limiter-vs-compressor.html", tags: "limiter compressor comparison techniques" },
    { title: "Logic Pro Beginner's Guide", url: "/articles/logic-pro-beginners-guide.html", tags: "logic pro beginners guide daw" },
    { title: "Logic Pro Review", url: "/articles/logic-pro-review.html", tags: "logic pro review daw" },
    { title: "Logic Pro Tips and Tricks", url: "/articles/logic-pro-tips-and-tricks.html", tags: "logic pro tips tricks techniques daw" },
    { title: "Logic Pro vs Ableton Live", url: "/articles/logic-pro-vs-ableton-live.html", tags: "logic pro ableton comparison daw" },
    { title: "Loopmasters Review", url: "/articles/loopmasters-review.html", tags: "loopmasters samples review" },
    { title: "Mastering Chain Guide", url: "/articles/mastering-chain-guide.html", tags: "mastering chain guide techniques" },
    { title: "MIDI Keyboard vs Pad Controller", url: "/articles/midi-keyboard-vs-pad-controller.html", tags: "midi keyboard pad controller comparison gear" },
    { title: "Mixing in Headphones Guide", url: "/articles/mixing-in-headphones-guide.html", tags: "mixing headphones guide techniques" },
    { title: "Mixing in Mono Guide", url: "/articles/mixing-in-mono-guide.html", tags: "mono mixing guide techniques" },
    { title: "Mixing Workflow Guide", url: "/articles/mixing-workflow-guide.html", tags: "mixing workflow guide techniques" },
    { title: "Music Contracts Explained", url: "/articles/music-contracts-explained.html", tags: "contracts music business law explained" },
    { title: "Music Copyright and Fair Use Explained", url: "/articles/music-copyright-fair-use-explained.html", tags: "copyright fair use music law explained" },
    { title: "Music Distribution Explained", url: "/articles/music-distribution-explained.html", tags: "music distribution explained music business" },
    { title: "Music Licensing Explained", url: "/articles/music-licensing-explained.html", tags: "music licensing explained music business" },
    { title: "Music Licensing for YouTube", url: "/articles/music-licensing-for-youtube.html", tags: "licensing youtube music business" },
    { title: "Music Metadata Explained", url: "/articles/music-metadata-explained.html", tags: "metadata music explained music business" },
    { title: "Music Publishing Deals Explained", url: "/articles/music-publishing-deals-explained.html", tags: "publishing deals music business explained" },
    { title: "Music Publishing Explained", url: "/articles/music-publishing-explained.html", tags: "publishing music business explained royalties" },
    { title: "Music Streaming Royalties Explained", url: "/articles/music-streaming-royalties-explained.html", tags: "streaming royalties music business explained" },
    { title: "Music Sync Licensing Guide", url: "/articles/music-sync-licensing-guide.html", tags: "sync licensing music business guide tv film" },
    { title: "Music Theory for Producers", url: "/articles/music-theory-for-producers.html", tags: "music theory producers guide techniques" },
    { title: "Native Instruments Komplete Kontrol Review", url: "/articles/native-instruments-komplete-kontrol-review.html", tags: "komplete kontrol native instruments review gear hardware" },
    { title: "Native Instruments Maschine MK3 Review", url: "/articles/native-instruments-maschine-mk3-review.html", tags: "maschine native instruments review gear hardware" },
    { title: "Neumann TLM 103 Review", url: "/articles/neumann-tlm-103-review.html", tags: "neumann tlm 103 microphone review gear" },
    { title: "Neumann TLM 103 vs Rode NT1", url: "/articles/neumann-tlm-103-vs-rode-nt1.html", tags: "neumann rode microphone comparison gear" },
    { title: "Parallel Compression Explained", url: "/articles/parallel-compression-explained.html", tags: "parallel compression explained techniques" },
    { title: "Parallel Compression Techniques", url: "/articles/parallel-compression-techniques.html", tags: "parallel compression techniques guide" },
    { title: "Presonus Studio One Review", url: "/articles/presonus-studio-one-review.html", tags: "presonus studio one daw review" },
    { title: "Pro Tools Beginner's Guide", url: "/articles/pro-tools-beginners-guide.html", tags: "pro tools beginners guide daw" },
    { title: "Pro Tools Review", url: "/articles/pro-tools-review.html", tags: "pro tools review daw" },
    { title: "Pro Tools vs Logic Pro", url: "/articles/pro-tools-vs-logic-pro.html", tags: "pro tools logic pro comparison daw" },
    { title: "Reaper DAW Review", url: "/articles/reaper-daw-review.html", tags: "reaper daw review" },
    { title: "Reaper vs Ableton", url: "/articles/reaper-vs-ableton.html", tags: "reaper ableton comparison daw" },
    { title: "Record Label Contracts Explained", url: "/articles/record-label-contracts-explained.html", tags: "record label contracts explained music business" },
    { title: "Rode NT1 Review", url: "/articles/rode-nt1-review.html", tags: "rode nt1 microphone review gear" },
    { title: "Rode NT1 vs NT1-A", url: "/articles/rode-nt1-vs-nt1-a.html", tags: "rode nt1 nt1-a microphone comparison gear" },
    { title: "Rode PodMic Review", url: "/articles/rode-podmic-review.html", tags: "rode podmic microphone review gear podcast" },
    { title: "Sample Rate and Bit Depth Explained", url: "/articles/sample-rate-bit-depth-explained.html", tags: "sample rate bit depth explained glossary" },
    { title: "Scarlett Solo vs Scarlett 2i2", url: "/articles/scarlett-solo-vs-scarlett-2i2.html", tags: "scarlett focusrite audio interface comparison gear" },
    { title: "Serum 2 Review", url: "/articles/serum-2-review.html", tags: "serum 2 synthesizer review plugins" },
    { title: "Serum Synthesizer Review", url: "/articles/serum-synthesizer-review.html", tags: "serum synthesizer review plugins" },
    { title: "Serum vs Vital", url: "/articles/serum-vs-vital.html", tags: "serum vital synthesizer comparison plugins" },
    { title: "Shure SM58 Review", url: "/articles/shure-sm58-review.html", tags: "shure sm58 microphone review gear" },
    { title: "Shure SM7B Review", url: "/articles/shure-sm7b-review.html", tags: "shure sm7b microphone review gear" },
    { title: "Shure SM7B vs SM7dB", url: "/articles/shure-sm7b-vs-sm7db.html", tags: "shure sm7b sm7db microphone comparison gear" },
    { title: "Sidechain Compression Guide", url: "/articles/sidechain-compression-guide.html", tags: "sidechain compression guide techniques" },
    { title: "SM7B vs Rode NT1", url: "/articles/sm7b-vs-rode-nt1.html", tags: "sm7b rode microphone comparison gear" },
    { title: "Sony MDR-7506 Review", url: "/articles/sony-mdr-7506-review.html", tags: "sony headphones review gear" },
    { title: "Sony WH-1000XM5 for Music Production", url: "/articles/sony-wh-1000xm5-review.html", tags: "sony headphones review gear" },
    { title: "Sound Design Basics", url: "/articles/sound-design-basics.html", tags: "sound design basics techniques guide" },
    { title: "Sound Design for EDM", url: "/articles/sound-design-for-edm.html", tags: "sound design edm techniques guide" },
    { title: "Spotify vs Apple Music for Artists", url: "/articles/spotify-vs-apple-music-for-artists.html", tags: "spotify apple music comparison artists music business" },
    { title: "Spotify vs SoundCloud for Artists", url: "/articles/spotify-vs-soundcloud-for-artists.html", tags: "spotify soundcloud comparison artists music business" },
    { title: "SSL 2+ Review", url: "/articles/ssl-2-plus-review.html", tags: "ssl audio interface review gear" },
    { title: "Steinberg Cubase Review", url: "/articles/steinberg-cubase-review.html", tags: "cubase steinberg daw review" },
    { title: "Steinberg UR22C Review", url: "/articles/steinberg-ur22c-review.html", tags: "steinberg ur22c audio interface review gear" },
    { title: "Suno AI Review 2026", url: "/articles/suno-ai-review-2026.html", tags: "suno ai review 2026 ai music" },
    { title: "Suno vs Udio", url: "/articles/suno-vs-udio.html", tags: "suno udio ai music comparison" },
    { title: "Synthesizer Basics Guide", url: "/articles/synthesizer-basics-guide.html", tags: "synthesizer basics guide techniques" },
    { title: "Universal Audio Apollo Twin Review", url: "/articles/universal-audio-apollo-twin-review.html", tags: "universal audio apollo interface review gear" },
    { title: "Udio AI Review", url: "/articles/udio-ai-review.html", tags: "udio ai review ai music" },
    { title: "Valhalla Room Review", url: "/articles/valhalla-room-review.html", tags: "valhalla reverb review plugins" },
    { title: "Valhalla Room vs Lexicon", url: "/articles/valhalla-room-vs-lexicon.html", tags: "valhalla lexicon reverb comparison plugins" },
    { title: "Vocal Chain Guide", url: "/articles/vocal-chain-guide.html", tags: "vocal chain guide techniques mixing" },
    { title: "Vocal Compression Guide", url: "/articles/vocal-compression-guide.html", tags: "vocal compression guide techniques" },
    { title: "Waves Abbey Road Plugins Review", url: "/articles/waves-abbey-road-plugins-review.html", tags: "waves abbey road plugins review" },
    { title: "Waves Gold Bundle Review", url: "/articles/waves-gold-bundle-review.html", tags: "waves gold bundle review plugins" },
    { title: "Waves Plugins Guide", url: "/articles/waves-plugins-guide.html", tags: "waves plugins guide" },
    { title: "Waves Renaissance Compressor Review", url: "/articles/waves-renaissance-compressor-review.html", tags: "waves renaissance compressor review plugins" },
    { title: "Waves SSL E-Channel Review", url: "/articles/waves-ssl-e-channel-review.html", tags: "waves ssl channel strip review plugins" },
    { title: "What Is a Compressor Used For?", url: "/articles/what-is-a-compressor-used-for.html", tags: "compressor used for what is techniques" },
    { title: "What Is a DAW?", url: "/articles/what-is-a-daw.html", tags: "daw what is glossary" },
    { title: "What Is a Mastering Engineer?", url: "/articles/what-is-a-mastering-engineer.html", tags: "mastering engineer what is music business" },
    { title: "What Is a Music Manager?", url: "/articles/what-is-a-music-manager.html", tags: "music manager what is music business" },
    { title: "What Is a Music Producer?", url: "/articles/what-is-a-music-producer.html", tags: "music producer what is music business" },
    { title: "What Is a Music Sync Supervisor?", url: "/articles/what-is-a-music-sync-supervisor.html", tags: "music sync supervisor what is music business" },
    { title: "What Is a Sample Pack?", url: "/articles/what-is-a-sample-pack.html", tags: "sample pack what is glossary" },
    { title: "What Is a Synthesizer?", url: "/articles/what-is-a-synthesizer.html", tags: "synthesizer what is glossary" },
    { title: "What Is a VST3 Plugin?", url: "/articles/what-is-a-vst3-plugin.html", tags: "vst3 plugin what is glossary" },
    { title: "What Is an Audio Interface Used For?", url: "/articles/what-is-audio-interface-used-for.html", tags: "audio interface used for what is gear" },
    { title: "What Is Compression in Music Production?", url: "/articles/what-is-compression-music-production.html", tags: "compression music production what is techniques" },
    { title: "What Is Dynamic Range in Music?", url: "/articles/what-is-dynamic-range-in-music.html", tags: "dynamic range music what is glossary" },
    { title: "What Is EQ in Music Production?", url: "/articles/what-is-eq-music-production.html", tags: "eq equalizer music production what is techniques" },
    { title: "What Is the Frequency Spectrum?", url: "/articles/what-is-frequency-spectrum.html", tags: "frequency spectrum what is techniques" },
    { title: "What Is Gain Staging?", url: "/articles/what-is-gain-staging.html", tags: "gain staging what is techniques" },
    { title: "What Is LUFS Explained", url: "/articles/what-is-lufs-explained.html", tags: "lufs explained what is mastering" },
    { title: "What Is Mastering Music?", url: "/articles/what-is-mastering-music.html", tags: "mastering music what is techniques" },
    { title: "What Is Mid-Side Processing?", url: "/articles/what-is-mid-side-processing.html", tags: "mid side processing what is techniques" },
    { title: "What Is MIDI?", url: "/articles/what-is-midi.html", tags: "midi what is glossary" },
    { title: "What Is Mixing?", url: "/articles/what-is-mixing.html", tags: "mixing what is techniques glossary" },
    { title: "What Is Music Arrangement?", url: "/articles/what-is-music-arrangement.html", tags: "music arrangement what is techniques" },
    { title: "What Is Reverb in Music Production?", url: "/articles/what-is-reverb-music-production.html", tags: "reverb music production what is techniques" },
    { title: "What Is Sampling in Music?", url: "/articles/what-is-sampling-in-music.html", tags: "sampling music what is glossary" },
    { title: "What Is Saturation in Music Production?", url: "/articles/what-is-saturation-music-production.html", tags: "saturation music production what is techniques" },
    { title: "What Is Spatial Audio?", url: "/articles/what-is-spatial-audio.html", tags: "spatial audio what is glossary" },
    { title: "What Is Suno AI?", url: "/articles/what-is-suno-ai.html", tags: "suno ai what is guide" },
    { title: "What Is Udio AI?", url: "/articles/what-is-udio-ai.html", tags: "udio ai what is guide" },
    { title: "What Is a VST Plugin?", url: "/articles/what-is-vst-plugin.html", tags: "vst plugin what is glossary" },
    { title: "What Is White Noise in Music Production?", url: "/articles/what-is-white-noise-music-production.html", tags: "white noise music production what is glossary" },
    { title: "Work for Hire Music Explained", url: "/articles/work-for-hire-music-explained.html", tags: "work for hire music explained music business" },
    { title: "Yamaha HS5 Review", url: "/articles/yamaha-hs5-review.html", tags: "yamaha hs5 monitors review gear" },
    { title: "Yamaha HS5 vs KRK Rokit 5 G5", url: "/articles/yamaha-hs5-vs-krk-rokit-5-g5.html", tags: "yamaha hs5 krk rokit monitors comparison gear" },
    { title: "Yamaha HS8 Review", url: "/articles/yamaha-hs8-review.html", tags: "yamaha hs8 monitors review gear" },
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

/* mpw-sidebar-ra-disabled-s17 — disabled S17
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
*/

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
