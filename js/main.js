/* ===================================================
   MusicProductionWiki.com -- main.js v4 + Full Search (314 articles)
   =================================================== */
'use strict';

(function () {

  /* ------------------------------------------------
     SEARCH INDEX -- all 314 articles
  ------------------------------------------------ */
  const SEARCH_INDEX = [
  { title: "Ableton Live 12 Review", url: "/articles/ableton-live-12-review.html", tags: "ableton daw review" },
  { title: "Ableton Live 12 vs 11", url: "/articles/ableton-live-12-vs-11.html", tags: "ableton daw comparison" },
  { title: "Ableton Live 12 vs FL Studio 21", url: "/articles/ableton-live-12-vs-fl-studio-21.html", tags: "ableton fl studio daw comparison" },
  { title: "Ableton Live Beginner's Guide", url: "/articles/ableton-live-beginners-guide.html", tags: "ableton daw beginners guide" },
  { title: "Ableton Live Review", url: "/articles/ableton-live-review.html", tags: "ableton daw review" },
  { title: "Ableton Live Tips and Tricks", url: "/articles/ableton-live-tips-and-tricks.html", tags: "ableton daw tips techniques" },
  { title: "Ableton Push 3 Review", url: "/articles/ableton-push-3-review.html", tags: "ableton push hardware review gear" },
  { title: "Ableton Push 3 Standalone Review", url: "/articles/ableton-push-3-standalone-review.html", tags: "ableton push standalone hardware review" },
  { title: "Ableton Push 3 vs Maschine MK3", url: "/articles/ableton-push-3-vs-maschine-mk3.html", tags: "ableton push maschine comparison hardware" },
  { title: "Ableton vs Logic Pro for Beginners", url: "/articles/ableton-vs-logic-pro-for-beginners.html", tags: "ableton logic pro beginners comparison daw" },
  { title: "Ableton vs Pro Tools", url: "/articles/ableton-vs-pro-tools.html", tags: "ableton pro tools comparison daw" },
  { title: "Adam Audio T5V Review", url: "/articles/adam-audio-t5v-review.html", tags: "adam audio studio monitors review gear" },
  { title: "Adam Audio T7V Review", url: "/articles/adam-audio-t7v-review.html", tags: "adam audio studio monitors review gear" },
  { title: "AI Chord Progression Tools", url: "/articles/ai-chord-progression-tools.html", tags: "ai chord tools music" },
  { title: "AI Music Production Tools: Complete Guide", url: "/articles/ai-music-production-tools-complete-guide.html", tags: "ai music production tools guide" },
  { title: "AI Stem Separation Guide", url: "/articles/ai-stem-separation-guide.html", tags: "ai stem separation guide" },
  { title: "Akai MPK Mini MK4 Review", url: "/articles/akai-mpk-mini-mk4-review.html", tags: "akai mpk mini midi controller review gear" },
  { title: "AKG C414 Review", url: "/articles/akg-c414-review.html", tags: "akg c414 microphone review gear" },
  { title: "AKG C414 XLII Review", url: "/articles/akg-c414-xlii-review.html", tags: "akg c414 xlii microphone review gear" },
  { title: "ASCAP vs BMI", url: "/articles/ascap-vs-bmi.html", tags: "ascap bmi royalties music business comparison" },
  { title: "Audio Interface Buying Guide", url: "/articles/audio-interface-buying-guide.html", tags: "audio interface buying guide gear" },
  { title: "Audio Interface vs Mixer", url: "/articles/audio-interface-vs-mixer.html", tags: "audio interface mixer comparison gear" },
  { title: "Auto-Tune vs Melodyne", url: "/articles/auto-tune-vs-melodyne.html", tags: "autotune melodyne pitch correction comparison plugins" },
  { title: "Best AI Mixing Plugins 2026", url: "/articles/best-ai-mixing-plugins-2026.html", tags: "ai mixing plugins best 2026 roundup" },
  { title: "Best Audio Interface for Home Studio", url: "/articles/best-audio-interface-home-studio.html", tags: "audio interface home studio best gear" },
  { title: "Best Audio Interfaces 2026", url: "/articles/best-audio-interfaces-2026.html", tags: "audio interfaces best 2026 roundup gear" },
  { title: "Best Audio Interfaces for Guitarists", url: "/articles/best-audio-interfaces-for-guitarists.html", tags: "audio interfaces guitarists best gear roundup" },
  { title: "Best Audio Interfaces Under $200", url: "/articles/best-audio-interfaces-under-200.html", tags: "audio interfaces budget best gear roundup" },
  { title: "Best Budget Studio Gear 2026", url: "/articles/best-budget-studio-gear-2026.html", tags: "budget studio gear best 2026 roundup" },
  { title: "Best Compressor Plugins", url: "/articles/best-compressor-plugins.html", tags: "compressor plugins best roundup" },
  { title: "Best DAW for Beginners", url: "/articles/best-daw-for-beginners.html", tags: "daw beginners best buying guide" },
  { title: "Best DAW for Hip-Hop", url: "/articles/best-daw-for-hip-hop.html", tags: "daw hip hop best buying guide" },
  { title: "Best EQ Plugins", url: "/articles/best-eq-plugins.html", tags: "eq plugins best roundup" },
  { title: "Best Free DAWs 2026", url: "/articles/best-free-daws-2026.html", tags: "free daw best 2026 roundup" },
  { title: "Best Free VST Plugins", url: "/articles/best-free-vst-plugins.html", tags: "free vst plugins best roundup" },
  { title: "Best Headphones for Mixing", url: "/articles/best-headphones-for-mixing.html", tags: "headphones mixing best gear roundup" },
  { title: "Best Headphones Under $100", url: "/articles/best-headphones-under-100.html", tags: "headphones budget best gear roundup" },
  { title: "Best Laptops for Music Production", url: "/articles/best-laptops-for-music-production.html", tags: "laptops music production best gear roundup" },
  { title: "Best Microphone for Home Studio", url: "/articles/best-microphone-home-studio.html", tags: "microphone home studio best gear roundup" },
  { title: "Best Microphones for Home Studio 2026", url: "/articles/best-microphones-for-home-studio-2026.html", tags: "microphones home studio best 2026 roundup" },
  { title: "Best MIDI Controllers", url: "/articles/best-midi-controllers.html", tags: "midi controllers best gear roundup" },
  { title: "Best Plugins for Beginners", url: "/articles/best-plugins-for-beginners.html", tags: "plugins beginners best roundup" },
  { title: "Best Plugins for Hip-Hop Production", url: "/articles/best-plugins-for-hip-hop-production.html", tags: "plugins hip hop best roundup" },
  { title: "Best Plugins for Mixing 2026", url: "/articles/best-plugins-for-mixing-2026.html", tags: "plugins mixing best 2026 roundup" },
  { title: "Best Plugins for Vocals 2026", url: "/articles/best-plugins-for-vocals-2026.html", tags: "plugins vocals best 2026 roundup" },
  { title: "Best Studio Headphones for Music Production", url: "/articles/best-studio-headphones-music-production.html", tags: "studio headphones music production best gear" },
  { title: "Best Studio Headphones Under $100", url: "/articles/best-studio-headphones-under-100.html", tags: "studio headphones budget best gear" },
  { title: "Best Studio Monitors 2026", url: "/articles/best-studio-monitors-2026.html", tags: "studio monitors best 2026 roundup gear" },
  { title: "Best Studio Monitors for Home Studio", url: "/articles/best-studio-monitors-home-studio.html", tags: "studio monitors home studio best gear" },
  { title: "Best Studio Monitors Under $1000", url: "/articles/best-studio-monitors-under-1000.html", tags: "studio monitors budget best gear roundup" },
  { title: "Best Studio Monitors Under $300", url: "/articles/best-studio-monitors-under-300.html", tags: "studio monitors budget best gear roundup" },
  { title: "Best Studio Monitors Under $500", url: "/articles/best-studio-monitors-under-500.html", tags: "studio monitors budget best gear roundup" },
  { title: "Best Suno AI Prompts", url: "/articles/best-suno-ai-prompts.html", tags: "suno ai prompts best guide" },
  { title: "Best Vocal Microphones", url: "/articles/best-vocal-microphones.html", tags: "vocal microphones best gear roundup" },
  { title: "Best VST Plugins for Beginners", url: "/articles/best-vst-plugins-for-beginners.html", tags: "vst plugins beginners best roundup" },
  { title: "Beyerdynamic DT 990 Pro Review", url: "/articles/beyerdynamic-dt-990-pro-review.html", tags: "beyerdynamic headphones review gear" },
  { title: "Bus Compression Guide", url: "/articles/bus-compression-guide.html", tags: "bus compression guide techniques mixing" },
  { title: "Can You Copyright AI Music?", url: "/articles/can-you-copyright-ai-music.html", tags: "ai music copyright law music business" },
  { title: "Can You Copyright Suno AI Music?", url: "/articles/can-you-copyright-suno-ai-music.html", tags: "suno ai music copyright law music business" },
  { title: "Compression Ratio Explained", url: "/articles/compression-ratio-explained.html", tags: "compression ratio explained glossary techniques" },
  { title: "Condenser vs Dynamic Microphone Guide", url: "/articles/condenser-vs-dynamic-microphone-guide.html", tags: "condenser dynamic microphone comparison guide gear" },
  { title: "DistroKid Review 2026", url: "/articles/distrokid-review-2026.html", tags: "distrokid review music distribution" },
  { title: "DistroKid vs CD Baby", url: "/articles/distrokid-vs-cd-baby.html", tags: "distrokid cd baby distribution comparison music business" },
  { title: "DistroKid vs TuneCore", url: "/articles/distrokid-vs-tunecore.html", tags: "distrokid tunecore distribution comparison music business" },
  { title: "Dynamic EQ vs Multiband Compression", url: "/articles/dynamic-eq-vs-multiband-compression.html", tags: "dynamic eq multiband compression comparison techniques" },
  { title: "Ear Training for Music Producers", url: "/articles/ear-training-for-music-producers.html", tags: "ear training music producers techniques guide" },
  { title: "EQ Cheat Sheet", url: "/articles/eq-cheat-sheet.html", tags: "eq cheat sheet reference guide techniques" },
  { title: "FabFilter Pro-C2 Review", url: "/articles/fabfilter-pro-c2-review.html", tags: "fabfilter compressor review plugins" },
  { title: "FabFilter Pro-Q 4 Review", url: "/articles/fabfilter-pro-q-4-review.html", tags: "fabfilter eq review plugins" },
  { title: "FabFilter Pro-Q3 Review", url: "/articles/fabfilter-pro-q3-review.html", tags: "fabfilter eq review plugins" },
  { title: "FabFilter Pro-Q3 vs Pro-Q4", url: "/articles/fabfilter-pro-q3-vs-pro-q4.html", tags: "fabfilter eq comparison plugins" },
  { title: "FL Studio Review", url: "/articles/fl-studio-review.html", tags: "fl studio daw review" },
  { title: "FL Studio vs Ableton", url: "/articles/fl-studio-vs-ableton.html", tags: "fl studio ableton comparison daw" },
  { title: "FL Studio vs Logic Pro", url: "/articles/fl-studio-vs-logic-pro.html", tags: "fl studio logic pro comparison daw" },
  { title: "FL Studio vs Pro Tools", url: "/articles/fl-studio-vs-pro-tools.html", tags: "fl studio pro tools comparison daw" },
  { title: "Focusrite Scarlett 2i2 Gen 4 Review", url: "/articles/focusrite-scarlett-2i2-gen-4-review.html", tags: "focusrite scarlett audio interface review gear" },
  { title: "Focusrite Scarlett 4i4 Gen 4 Review", url: "/articles/focusrite-scarlett-4i4-gen-4-review.html", tags: "focusrite scarlett audio interface review gear" },
  { title: "Focusrite Scarlett Solo Review", url: "/articles/focusrite-scarlett-solo-review.html", tags: "focusrite scarlett solo audio interface review gear" },
  { title: "Focusrite Scarlett Solo vs 2i2", url: "/articles/focusrite-scarlett-solo-vs-2i2.html", tags: "focusrite scarlett solo 2i2 comparison gear" },
  { title: "Headphones vs Studio Monitors", url: "/articles/headphones-vs-studio-monitors.html", tags: "headphones studio monitors comparison gear" },
  { title: "Home Recording Studio Setup Guide", url: "/articles/home-recording-studio-setup.html", tags: "home recording studio setup guide gear" },
  { title: "Home Studio Acoustic Treatment Guide", url: "/articles/home-studio-acoustic-treatment-guide.html", tags: "acoustic treatment home studio guide techniques" },
  { title: "Home Studio Acoustic Treatment", url: "/articles/home-studio-acoustic-treatment.html", tags: "acoustic treatment home studio techniques guide" },
  { title: "How Music Royalties Work", url: "/articles/how-music-royalties-work.html", tags: "royalties music business how streaming" },
  { title: "How to Arrange a Song", url: "/articles/how-to-arrange-a-song.html", tags: "arrange song how to techniques music production" },
  { title: "How to Build a Fanbase", url: "/articles/how-to-build-a-fanbase.html", tags: "fanbase build how to music business marketing" },
  { title: "How to Build a Home Recording Studio", url: "/articles/how-to-build-a-home-recording-studio.html", tags: "build home recording studio how to gear guide" },
  { title: "How to Build a Plugin Chain", url: "/articles/how-to-build-a-plugin-chain.html", tags: "plugin chain build how to techniques" },
  { title: "How to Build Tension and Drops in EDM", url: "/articles/how-to-build-tension-and-drops-in-edm.html", tags: "edm tension drops build how to techniques" },
  { title: "How to Collaborate Online as a Producer", url: "/articles/how-to-collab-online-as-a-producer.html", tags: "collaborate online producer how to music business" },
  { title: "How to Copyright Your Music", url: "/articles/how-to-copyright-your-music.html", tags: "copyright music law how to music business" },
  { title: "How to Develop Your Sound as a Producer", url: "/articles/how-to-develop-your-sound-as-a-producer.html", tags: "develop sound producer how to techniques" },
  { title: "How to Distribute Music", url: "/articles/how-to-distribute-music.html", tags: "distribute music distribution how to music business" },
  { title: "How to EQ Vocals", url: "/articles/how-to-eq-vocals.html", tags: "eq vocals how to techniques mixing" },
  { title: "How to Finish Beats You Start", url: "/articles/how-to-finish-beats-you-start.html", tags: "finish beats producer how to techniques" },
  { title: "How to Get a Record Deal", url: "/articles/how-to-get-a-record-deal.html", tags: "record deal music business how to" },
  { title: "How to Get More Streams on Spotify", url: "/articles/how-to-get-more-streams-on-spotify.html", tags: "spotify streams how to music business marketing" },
  { title: "How to Get Music on Spotify", url: "/articles/how-to-get-music-on-spotify.html", tags: "spotify music distribution how to music business" },
  { title: "How to Get Sync Licensing Deals", url: "/articles/how-to-get-sync-licensing-deals.html", tags: "sync licensing deals how to music business" },
  { title: "How to Get Your Music Licensed for TV", url: "/articles/how-to-get-your-music-licensed-for-tv.html", tags: "music licensed tv sync how to music business" },
  { title: "How to License Your Music", url: "/articles/how-to-license-your-music.html", tags: "license music how to music business" },
  { title: "How to Make a Beat: Beginner's Guide", url: "/articles/how-to-make-a-beat-beginners-guide.html", tags: "beat making beginners how to techniques" },
  { title: "How to Make a Beat", url: "/articles/how-to-make-a-beat.html", tags: "make beat how to techniques hip hop" },
  { title: "How to Make a Lo-Fi Sample Pack", url: "/articles/how-to-make-a-lo-fi-sample-pack.html", tags: "lo-fi sample pack how to music business" },
  { title: "How to Make Afrobeats", url: "/articles/how-to-make-afrobeats.html", tags: "afrobeats how to make techniques genre" },
  { title: "How to Make Amapiano", url: "/articles/how-to-make-amapiano.html", tags: "amapiano how to make techniques genre" },
  { title: "How to Make Ambient Music", url: "/articles/how-to-make-ambient-music.html", tags: "ambient music how to make techniques genre" },
  { title: "How to Make Cinematic Music", url: "/articles/how-to-make-cinematic-music.html", tags: "cinematic music how to make techniques genre" },
  { title: "How to Make Cinematic Sound Design", url: "/articles/how-to-make-cinematic-sound-design.html", tags: "cinematic sound design how to make techniques" },
  { title: "How to Make Country Music", url: "/articles/how-to-make-country-music.html", tags: "country music how to make techniques genre" },
  { title: "How to Make Drill Music", url: "/articles/how-to-make-drill-music.html", tags: "drill music how to make techniques genre" },
  { title: "How to Make Drum and Bass", url: "/articles/how-to-make-drum-and-bass.html", tags: "drum and bass how to make techniques genre" },
  { title: "How to Make EDM", url: "/articles/how-to-make-edm.html", tags: "edm how to make techniques genre electronic" },
  { title: "How to Make House Music", url: "/articles/how-to-make-house-music.html", tags: "house music how to make techniques genre" },
  { title: "How to Make Hyperpop", url: "/articles/how-to-make-hyperpop.html", tags: "hyperpop how to make techniques genre" },
  { title: "How to Make Lo-Fi Beats", url: "/articles/how-to-make-lo-fi-beats.html", tags: "lo-fi beats how to make techniques" },
  { title: "How to Make Lo-Fi Hip-Hop", url: "/articles/how-to-make-lo-fi-hip-hop.html", tags: "lo-fi hip hop how to make techniques genre" },
  { title: "How to Make Lo-Fi Music", url: "/articles/how-to-make-lofi-music.html", tags: "lofi music how to make techniques genre" },
  { title: "How to Make Money from Music", url: "/articles/how-to-make-money-from-music.html", tags: "money music income how to music business" },
  { title: "How to Make Money with AI Music", url: "/articles/how-to-make-money-with-ai-music.html", tags: "ai music money income how to" },
  { title: "How to Make Money with Music Production", url: "/articles/how-to-make-money-with-music-production.html", tags: "money music production income how to music business" },
  { title: "How to Make Money with Suno AI", url: "/articles/how-to-make-money-with-suno-ai.html", tags: "suno ai money income how to" },
  { title: "How to Make Music in a Genre You Don't Know", url: "/articles/how-to-make-music-in-a-genre-you-dont-know.html", tags: "genre music how to make techniques" },
  { title: "How to Make Music That Translates on Any System", url: "/articles/how-to-make-music-that-translates-on-any-system.html", tags: "music translation systems how to techniques mixing" },
  { title: "How to Make Phonk Music", url: "/articles/how-to-make-phonk-music.html", tags: "phonk music how to make techniques genre" },
  { title: "How to Make Pluggnb Music", url: "/articles/how-to-make-pluggnb.html", tags: "pluggnb music how to make techniques genre" },
  { title: "How to Make R&B Music", url: "/articles/how-to-make-rnb-music.html", tags: "rnb music how to make techniques genre" },
  { title: "How to Make Trap 808s from Scratch", url: "/articles/how-to-make-trap-808s-from-scratch.html", tags: "trap 808 how to make techniques hip hop" },
  { title: "How to Make Trap Beats", url: "/articles/how-to-make-trap-beats.html", tags: "trap beats how to make techniques hip hop" },
  { title: "How to Make Your First Sample Pack", url: "/articles/how-to-make-your-first-sample-pack.html", tags: "sample pack how to make music business" },
  { title: "How to Master a Song at Home", url: "/articles/how-to-master-a-song-at-home.html", tags: "mastering home how to techniques" },
  { title: "How to Master a Song", url: "/articles/how-to-master-a-song.html", tags: "mastering how to master song techniques" },
  { title: "How to Mix Bass", url: "/articles/how-to-mix-bass.html", tags: "bass mixing how to techniques" },
  { title: "How to Mix Drums in a DAW", url: "/articles/how-to-mix-drums-in-a-daw.html", tags: "drums daw mixing how to techniques" },
  { title: "How to Mix Drums", url: "/articles/how-to-mix-drums.html", tags: "drums mixing how to techniques" },
  { title: "How to Mix in Dolby Atmos", url: "/articles/how-to-mix-in-dolby-atmos.html", tags: "dolby atmos mixing how to techniques spatial audio" },
  { title: "How to Mix in Headphones", url: "/articles/how-to-mix-in-headphones.html", tags: "headphones mixing how to techniques" },
  { title: "How to Mix Music: Beginner's Guide", url: "/articles/how-to-mix-music-beginners-guide.html", tags: "mixing music beginners how to techniques guide" },
  { title: "How to Mix Strings", url: "/articles/how-to-mix-strings.html", tags: "strings mixing how to techniques orchestral" },
  { title: "How to Mix Vocals: Advanced Guide", url: "/articles/how-to-mix-vocals-advanced.html", tags: "vocals mixing advanced how to techniques" },
  { title: "How to Mix Vocals", url: "/articles/how-to-mix-vocals.html", tags: "vocals mixing how to techniques" },
  { title: "How to Price Your Beats", url: "/articles/how-to-price-your-beats.html", tags: "price beats how to music business" },
  { title: "How to Promote Music Independently", url: "/articles/how-to-promote-music-independently.html", tags: "promote music independently marketing how to music business" },
  { title: "How to Promote Music on Spotify", url: "/articles/how-to-promote-music-on-spotify.html", tags: "spotify promote music marketing how to music business" },
  { title: "How to Promote Music on TikTok", url: "/articles/how-to-promote-music-on-tiktok.html", tags: "tiktok promote music marketing how to music business" },
  { title: "How to Read a Music Contract", url: "/articles/how-to-read-a-music-contract.html", tags: "music contract read how to music business law" },
  { title: "How to Record a Podcast", url: "/articles/how-to-record-a-podcast.html", tags: "podcast record how to techniques audio" },
  { title: "How to Record Acoustic Guitar", url: "/articles/how-to-record-acoustic-guitar.html", tags: "acoustic guitar record how to techniques" },
  { title: "How to Record Drums at Home", url: "/articles/how-to-record-drums-at-home.html", tags: "drums home record how to techniques" },
  { title: "How to Record Drums", url: "/articles/how-to-record-drums.html", tags: "drums record how to techniques" },
  { title: "How to Record Electric Guitar", url: "/articles/how-to-record-electric-guitar.html", tags: "electric guitar record how to techniques" },
  { title: "How to Record Vocals at Home", url: "/articles/how-to-record-vocals-home-studio.html", tags: "vocals home studio record how to techniques" },
  { title: "How to Register Your Music", url: "/articles/how-to-register-your-music.html", tags: "register music how to music business copyright" },
  { title: "How to Sell Beats Online", url: "/articles/how-to-sell-beats-online.html", tags: "sell beats online how to music business" },
  { title: "How to Transition Between Songs in a DJ Set", url: "/articles/how-to-transition-between-songs-in-a-dj-set.html", tags: "dj transition songs how to techniques" },
  { title: "How to Use a Limiter", url: "/articles/how-to-use-a-limiter.html", tags: "limiter how to use techniques mastering" },
  { title: "How to Use Automation in Your DAW", url: "/articles/how-to-use-automation-in-your-daw.html", tags: "automation daw how to use techniques" },
  { title: "How to Use Auto-Tune Creatively", url: "/articles/how-to-use-autotune-creatively.html", tags: "autotune creative how to use techniques" },
  { title: "How to Use Auto-Tune in Ableton", url: "/articles/how-to-use-autotune-in-ableton.html", tags: "autotune ableton how to use techniques" },
  { title: "How to Use Auto-Tune in FL Studio", url: "/articles/how-to-use-autotune-in-fl-studio.html", tags: "autotune fl studio how to use techniques" },
  { title: "How to Use Auto-Tune", url: "/articles/how-to-use-autotune.html", tags: "autotune how to use techniques pitch correction" },
  { title: "How to Use Compression: Beginner's Guide", url: "/articles/how-to-use-compression-beginners.html", tags: "compression beginners how to use techniques" },
  { title: "How to Use Compression on Drums", url: "/articles/how-to-use-compression-on-drums.html", tags: "compression drums how to use techniques" },
  { title: "How to Use Compression on Vocals", url: "/articles/how-to-use-compression-on-vocals.html", tags: "compression vocals how to use techniques" },
  { title: "How to Use EQ on Drums", url: "/articles/how-to-use-eq-on-drums.html", tags: "eq drums how to use techniques mixing" },
  { title: "How to Use Groove and Swing in Music", url: "/articles/how-to-use-groove-and-swing-in-music.html", tags: "groove swing music how to use techniques" },
  { title: "How to Use MIDI in Your DAW", url: "/articles/how-to-use-midi-in-your-daw.html", tags: "midi daw how to use techniques" },
  { title: "How to Use Multiband Compression", url: "/articles/how-to-use-multiband-compression.html", tags: "multiband compression how to use techniques" },
  { title: "How to Use Pitch Shifting Creatively", url: "/articles/how-to-use-pitch-shifting-creatively.html", tags: "pitch shifting creative how to use techniques" },
  { title: "How to Use Reverb in a Mix", url: "/articles/how-to-use-reverb-in-a-mix.html", tags: "reverb mix how to use techniques" },
  { title: "How to Use Reverb on Drums", url: "/articles/how-to-use-reverb-on-drums.html", tags: "reverb drums how to use techniques" },
  { title: "How to Use Reverb on Vocals", url: "/articles/how-to-use-reverb-on-vocals.html", tags: "reverb vocals how to use techniques" },
  { title: "How to Use Send Effects", url: "/articles/how-to-use-send-effects.html", tags: "send effects how to use techniques mixing" },
  { title: "How to Use Suno AI", url: "/articles/how-to-use-suno-ai.html", tags: "suno ai how to use guide" },
  { title: "How to Use Vocal Effects", url: "/articles/how-to-use-vocal-effects.html", tags: "vocal effects how to use techniques" },
  { title: "How to Use Vocoders and Talk Boxes", url: "/articles/how-to-use-vocoders-and-talk-boxes.html", tags: "vocoder talk box how to use techniques" },
  { title: "iZotope Neutron Guide", url: "/articles/izotope-neutron-guide.html", tags: "izotope neutron mixing guide plugins" },
  { title: "iZotope Ozone 11 Review", url: "/articles/izotope-ozone-11-review.html", tags: "izotope ozone mastering review plugins" },
  { title: "iZotope Ozone 12 Review", url: "/articles/izotope-ozone-12-review.html", tags: "izotope ozone mastering review plugins" },
  { title: "iZotope RX 11 Review", url: "/articles/izotope-rx-11-review.html", tags: "izotope rx audio repair review plugins" },
  { title: "iZotope RX Guide", url: "/articles/izotope-rx-guide.html", tags: "izotope rx audio repair guide plugins" },
  { title: "iZotope RX vs Waves Clarity", url: "/articles/izotope-rx-vs-waves-clarity.html", tags: "izotope rx waves clarity comparison plugins" },
  { title: "Kali Audio LP-6 V2 Review", url: "/articles/kali-audio-lp-6-v2-review.html", tags: "kali audio studio monitors review gear" },
  { title: "Klipsch R-41PM Review", url: "/articles/klipsch-r41pm-review.html", tags: "klipsch studio monitors review gear" },
  { title: "Kontakt 7 vs Kontakt 8", url: "/articles/kontakt-7-vs-kontakt-8.html", tags: "kontakt native instruments comparison plugins" },
  { title: "KRK Rokit 5 G5 Review", url: "/articles/krk-rokit-5-g5-review.html", tags: "krk rokit studio monitors review gear" },
  { title: "KRK Rokit 5 G5 vs Yamaha HS5", url: "/articles/krk-rokit-5-g5-vs-yamaha-hs5.html", tags: "krk yamaha studio monitors comparison gear" },
  { title: "LANDR vs iZotope Ozone", url: "/articles/landr-vs-izotope-ozone.html", tags: "landr izotope ozone mastering comparison ai" },
  { title: "Logic Pro 11 vs 10", url: "/articles/logic-pro-11-vs-10.html", tags: "logic pro comparison daw" },
  { title: "Logic Pro Beginner's Guide", url: "/articles/logic-pro-beginners-guide.html", tags: "logic pro beginners guide daw" },
  { title: "Logic Pro Review 2026", url: "/articles/logic-pro-review-2026.html", tags: "logic pro review daw 2026" },
  { title: "Logic Pro vs Ableton Live", url: "/articles/logic-pro-vs-ableton-live.html", tags: "logic pro ableton comparison daw" },
  { title: "Logic Pro vs GarageBand", url: "/articles/logic-pro-vs-garageband.html", tags: "logic pro garageband comparison daw apple" },
  { title: "Logic Pro vs Pro Tools", url: "/articles/logic-pro-vs-pro-tools.html", tags: "logic pro pro tools comparison daw" },
  { title: "Lossless Audio Explained", url: "/articles/lossless-audio-explained.html", tags: "lossless audio explained glossary" },
  { title: "MIDI Keyboard vs Pad Controller", url: "/articles/midi-keyboard-vs-pad-controller.html", tags: "midi keyboard pad controller comparison gear" },
  { title: "MIDI vs Audio Explained", url: "/articles/midi-vs-audio-explained.html", tags: "midi audio explained glossary techniques" },
  { title: "Mixing EQ Guide", url: "/articles/mixing-eq-guide.html", tags: "mixing eq guide techniques" },
  { title: "Mixing: Headphones vs Studio Monitors", url: "/articles/mixing-headphones-vs-studio-monitors.html", tags: "mixing headphones studio monitors comparison" },
  { title: "Mixing Headroom Explained", url: "/articles/mixing-headroom-explained.html", tags: "mixing headroom explained techniques glossary" },
  { title: "Mixing in Mono Guide", url: "/articles/mixing-in-mono-guide.html", tags: "mono mixing guide techniques" },
  { title: "MOTU M2 Review", url: "/articles/motu-m2-review.html", tags: "motu m2 audio interface review gear" },
  { title: "Music Contracts Explained", url: "/articles/music-contracts-explained.html", tags: "contracts music business law explained" },
  { title: "Music Copyright and Fair Use Explained", url: "/articles/music-copyright-fair-use-explained.html", tags: "copyright fair use music law explained" },
  { title: "Music Distribution Explained", url: "/articles/music-distribution-explained.html", tags: "music distribution explained music business" },
  { title: "Music Licensing Explained", url: "/articles/music-licensing-explained.html", tags: "music licensing explained music business" },
  { title: "Music Licensing for YouTube", url: "/articles/music-licensing-for-youtube.html", tags: "licensing youtube music business" },
  { title: "Music Metadata Explained", url: "/articles/music-metadata-explained.html", tags: "metadata music explained music business" },
  { title: "Music Producer Branding Guide", url: "/articles/music-producer-branding-guide.html", tags: "producer branding guide music business" },
  { title: "Music Producer Contract Guide", url: "/articles/music-producer-contract-guide.html", tags: "producer contract guide music business law" },
  { title: "Music Producer Morning Routine", url: "/articles/music-producer-morning-routine.html", tags: "producer morning routine music business productivity" },
  { title: "Music Producer Passive Income Guide", url: "/articles/music-producer-passive-income-guide.html", tags: "producer passive income guide music business" },
  { title: "Music Producer Portfolio Guide", url: "/articles/music-producer-portfolio-guide.html", tags: "producer portfolio guide music business" },
  { title: "Music Producer Rate Card Guide", url: "/articles/music-producer-rate-card-guide.html", tags: "producer rate card pricing guide music business" },
  { title: "Music Producer Social Media Strategy", url: "/articles/music-producer-social-media-strategy.html", tags: "producer social media strategy music business marketing" },
  { title: "Music Producer vs Beatmaker", url: "/articles/music-producer-vs-beatmaker.html", tags: "music producer beatmaker comparison music business" },
  { title: "Music Production Burnout", url: "/articles/music-production-burnout.html", tags: "music production burnout mental health producer" },
  { title: "Music Production for Beginners", url: "/articles/music-production-for-beginners.html", tags: "music production beginners guide how to" },
  { title: "Music Production on iPad 2026", url: "/articles/music-production-on-ipad-2026.html", tags: "music production ipad 2026 guide mobile" },
  { title: "Music Publishing Deals Explained", url: "/articles/music-publishing-deals-explained.html", tags: "publishing deals music business explained royalties" },
  { title: "Music Publishing Explained", url: "/articles/music-publishing-explained.html", tags: "publishing music business explained royalties" },
  { title: "Music Streaming Royalties Explained", url: "/articles/music-streaming-royalties-explained.html", tags: "streaming royalties music business explained" },
  { title: "Music Sync Licensing Guide", url: "/articles/music-sync-licensing-guide.html", tags: "sync licensing music business guide tv film" },
  { title: "Music Theory for Producers", url: "/articles/music-theory-for-producers.html", tags: "music theory producers guide techniques" },
  { title: "Native Instruments Komplete 15 Review", url: "/articles/native-instruments-komplete-15-review.html", tags: "native instruments komplete review plugins" },
  { title: "Native Instruments Komplete Kontrol Review", url: "/articles/native-instruments-komplete-kontrol-review.html", tags: "komplete kontrol native instruments review gear hardware" },
  { title: "Native Instruments Maschine MK3 Review", url: "/articles/native-instruments-maschine-mk3-review.html", tags: "maschine native instruments review gear hardware" },
  { title: "Native Instruments Maschine Plus Review", url: "/articles/native-instruments-maschine-plus-review.html", tags: "maschine plus native instruments review gear hardware" },
  { title: "Neumann TLM 103 Review", url: "/articles/neumann-tlm-103-review.html", tags: "neumann tlm 103 microphone review gear" },
  { title: "Neumann TLM 103 vs Rode NT1", url: "/articles/neumann-tlm-103-vs-rode-nt1.html", tags: "neumann rode microphone comparison gear" },
  { title: "Neumann TLM 103 vs U87", url: "/articles/neumann-tlm-103-vs-u87.html", tags: "neumann microphone comparison gear" },
  { title: "Parallel Compression Explained", url: "/articles/parallel-compression-explained.html", tags: "parallel compression explained techniques mixing" },
  { title: "PreSonus Studio One Review", url: "/articles/presonus-studio-one-review.html", tags: "presonus studio one daw review" },
  { title: "Pro Tools Beginner's Guide", url: "/articles/pro-tools-beginners-guide.html", tags: "pro tools beginners guide daw" },
  { title: "Pro Tools Review", url: "/articles/pro-tools-review.html", tags: "pro tools review daw" },
  { title: "Reaper Review 2026", url: "/articles/reaper-review-2026.html", tags: "reaper daw review 2026" },
  { title: "Reaper vs Ableton", url: "/articles/reaper-vs-ableton.html", tags: "reaper ableton comparison daw" },
  { title: "Recording in a Small Room", url: "/articles/recording-in-a-small-room.html", tags: "small room recording how to techniques acoustics" },
  { title: "Rode NT1 5th Gen Review", url: "/articles/rode-nt1-5th-gen-review.html", tags: "rode nt1 microphone review gear" },
  { title: "Rode NT1 Review", url: "/articles/rode-nt1-review.html", tags: "rode nt1 microphone review gear" },
  { title: "Rode NT1 vs AT2020", url: "/articles/rode-nt1-vs-at2020.html", tags: "rode nt1 at2020 microphone comparison gear" },
  { title: "Rode PodMic Review", url: "/articles/rode-podmic-review.html", tags: "rode podmic microphone review gear podcast" },
  { title: "Rode PodMic USB Review", url: "/articles/rode-podmic-usb-review.html", tags: "rode podmic usb microphone review gear podcast" },
  { title: "Sample Rate and Bit Depth Explained", url: "/articles/sample-rate-bit-depth-explained.html", tags: "sample rate bit depth explained glossary" },
  { title: "Scarlett 2i2 vs 4i4", url: "/articles/scarlett-2i2-vs-4i4.html", tags: "focusrite scarlett 2i2 4i4 comparison gear" },
  { title: "Scarlett 2i2 vs SSL 2+", url: "/articles/scarlett-2i2-vs-ssl-2-plus.html", tags: "focusrite scarlett ssl audio interface comparison gear" },
  { title: "Scarlett Solo vs Scarlett 2i2", url: "/articles/scarlett-solo-vs-scarlett-2i2.html", tags: "focusrite scarlett solo 2i2 comparison gear" },
  { title: "Serum 2 Review", url: "/articles/serum-2-review.html", tags: "serum 2 synthesizer review plugins" },
  { title: "Serum 2 vs Vital", url: "/articles/serum-2-vs-vital.html", tags: "serum vital synthesizer comparison plugins" },
  { title: "Serum Synthesizer Review", url: "/articles/serum-synthesizer-review.html", tags: "serum synthesizer review plugins" },
  { title: "Serum vs Vital", url: "/articles/serum-vs-vital.html", tags: "serum vital synthesizer comparison plugins" },
  { title: "Shure MV7+ Review", url: "/articles/shure-mv7-plus-review.html", tags: "shure mv7 plus microphone review gear podcast" },
  { title: "Shure MV7 Review", url: "/articles/shure-mv7-review.html", tags: "shure mv7 microphone review gear podcast" },
  { title: "Shure SM58 Review", url: "/articles/shure-sm58-review.html", tags: "shure sm58 microphone review gear" },
  { title: "Shure SM7B Review", url: "/articles/shure-sm7b-review.html", tags: "shure sm7b microphone review gear broadcast" },
  { title: "Shure SM7dB vs SM7B", url: "/articles/shure-sm7db-vs-sm7b.html", tags: "shure sm7db sm7b microphone comparison gear" },
  { title: "Sidechain Compression Guide", url: "/articles/sidechain-compression-guide.html", tags: "sidechain compression guide techniques" },
  { title: "SM7B vs Rode NT1", url: "/articles/sm7b-vs-rode-nt1.html", tags: "sm7b rode microphone comparison gear" },
  { title: "Sony MDR-7506 Review", url: "/articles/sony-mdr-7506-review.html", tags: "sony headphones review gear" },
  { title: "Sound Design Basics", url: "/articles/sound-design-basics.html", tags: "sound design basics techniques guide synthesis" },
  { title: "Splice vs Loopmasters", url: "/articles/splice-vs-loopmasters.html", tags: "splice loopmasters samples comparison music business" },
  { title: "Spotify vs Apple Music for Artists", url: "/articles/spotify-vs-apple-music-for-artists.html", tags: "spotify apple music comparison artists music business" },
  { title: "Spotify vs SoundCloud for Artists", url: "/articles/spotify-vs-soundcloud-for-artists.html", tags: "spotify soundcloud comparison artists music business" },
  { title: "SSL 2+ Review", url: "/articles/ssl-2-plus-review.html", tags: "ssl audio interface review gear" },
  { title: "SSL 2 vs SSL 2+", url: "/articles/ssl-2-vs-ssl-2-plus.html", tags: "ssl audio interface comparison gear" },
  { title: "Steinberg Cubase Review", url: "/articles/steinberg-cubase-review.html", tags: "cubase steinberg daw review" },
  { title: "Studio Monitor Placement Guide", url: "/articles/studio-monitor-placement-guide.html", tags: "studio monitor placement guide acoustics gear" },
  { title: "Suno AI Beginner's Guide", url: "/articles/suno-ai-beginners-guide.html", tags: "suno ai beginners guide how to" },
  { title: "Suno AI Review 2026", url: "/articles/suno-ai-review-2026.html", tags: "suno ai review 2026" },
  { title: "Suno AI vs Udio", url: "/articles/suno-vs-udio.html", tags: "suno udio ai music comparison" },
  { title: "Udio Beginner's Guide", url: "/articles/udio-beginners-guide.html", tags: "udio ai beginners guide how to" },
  { title: "Udio Review 2026", url: "/articles/udio-review-2026.html", tags: "udio ai review 2026" },
  { title: "Universal Audio Apollo Twin Review", url: "/articles/universal-audio-apollo-twin-review.html", tags: "universal audio apollo interface review gear" },
  { title: "Universal Audio Volt 276 Review", url: "/articles/universal-audio-volt-276-review.html", tags: "universal audio volt audio interface review gear" },
  { title: "Valhalla Room Review", url: "/articles/valhalla-room-review.html", tags: "valhalla reverb review plugins" },
  { title: "Valhalla Room vs Lexicon", url: "/articles/valhalla-room-vs-lexicon.html", tags: "valhalla lexicon reverb comparison plugins" },
  { title: "Vocal Compression Guide", url: "/articles/vocal-compression-guide.html", tags: "vocal compression guide techniques" },
  { title: "Vocal Tuning Guide", url: "/articles/vocal-tuning-guide.html", tags: "vocal tuning guide techniques pitch correction" },
  { title: "Waves Abbey Road Plugins Review", url: "/articles/waves-abbey-road-plugins-review.html", tags: "waves abbey road plugins review" },
  { title: "Waves Gold Bundle Review", url: "/articles/waves-gold-bundle-review.html", tags: "waves gold bundle plugins review" },
  { title: "Waves Plugins Guide", url: "/articles/waves-plugins-guide.html", tags: "waves plugins guide review" },
  { title: "Waves Renaissance Compressor Review", url: "/articles/waves-renaissance-compressor-review.html", tags: "waves renaissance compressor review plugins" },
  { title: "Waves SSL E-Channel Review", url: "/articles/waves-ssl-e-channel-review.html", tags: "waves ssl channel strip review plugins" },
  { title: "What Is a Compressor Used For?", url: "/articles/what-is-a-compressor-used-for.html", tags: "compressor used for what is techniques glossary" },
  { title: "What Is a DAW?", url: "/articles/what-is-a-daw.html", tags: "daw what is glossary beginners" },
  { title: "What Is a Mastering Engineer?", url: "/articles/what-is-a-mastering-engineer.html", tags: "mastering engineer what is music business glossary" },
  { title: "What Is a Music Manager?", url: "/articles/what-is-a-music-manager.html", tags: "music manager what is music business glossary" },
  { title: "What Is a Music Producer?", url: "/articles/what-is-a-music-producer.html", tags: "music producer what is glossary music business" },
  { title: "What Is a Sample Pack?", url: "/articles/what-is-a-sample-pack.html", tags: "sample pack what is glossary music production" },
  { title: "What Is a Synthesizer?", url: "/articles/what-is-a-synthesizer.html", tags: "synthesizer what is glossary music production" },
  { title: "What Is a VST3 Plugin?", url: "/articles/what-is-a-vst3-plugin.html", tags: "vst3 plugin what is glossary" },
  { title: "What Is an Audio Interface Used For?", url: "/articles/what-is-audio-interface-used-for.html", tags: "audio interface used for what is gear glossary" },
  { title: "What Is Compression in Music Production?", url: "/articles/what-is-compression-music-production.html", tags: "compression music production what is techniques glossary" },
  { title: "What Is Dynamic Range in Music?", url: "/articles/what-is-dynamic-range-in-music.html", tags: "dynamic range music what is glossary techniques" },
  { title: "What Is EQ in Music Production?", url: "/articles/what-is-eq-music-production.html", tags: "eq equalizer music production what is techniques glossary" },
  { title: "What Is the Frequency Spectrum?", url: "/articles/what-is-frequency-spectrum.html", tags: "frequency spectrum what is techniques glossary" },
  { title: "What Is Gain Staging?", url: "/articles/what-is-gain-staging.html", tags: "gain staging what is techniques glossary" },
  { title: "What Is LUFS Explained", url: "/articles/what-is-lufs-explained.html", tags: "lufs loudness what is explained glossary mastering" },
  { title: "What Is Mastering Music?", url: "/articles/what-is-mastering-music.html", tags: "mastering music what is techniques glossary" },
  { title: "What Is MIDI?", url: "/articles/what-is-midi.html", tags: "midi what is glossary music production" },
  { title: "What Is Mixing in Music Production?", url: "/articles/what-is-mixing.html", tags: "mixing music production what is techniques glossary" },
  { title: "What Is Music Arrangement?", url: "/articles/what-is-music-arrangement.html", tags: "music arrangement what is glossary techniques" },
  { title: "What Is Reverb in Music Production?", url: "/articles/what-is-reverb-music-production.html", tags: "reverb music production what is techniques glossary" },
  { title: "What Is Sampling in Music?", url: "/articles/what-is-sampling-in-music.html", tags: "sampling music what is glossary techniques" },
  { title: "What Is Saturation in Music Production?", url: "/articles/what-is-saturation-music-production.html", tags: "saturation music production what is techniques glossary" },
  { title: "What Is Spatial Audio?", url: "/articles/what-is-spatial-audio.html", tags: "spatial audio what is glossary techniques dolby atmos" },
  { title: "What Is Suno AI?", url: "/articles/what-is-suno-ai.html", tags: "suno ai what is guide" },
  { title: "What Is Udio AI?", url: "/articles/what-is-udio-ai.html", tags: "udio ai what is guide" },
  { title: "What Is a VST Plugin?", url: "/articles/what-is-vst-plugin.html", tags: "vst plugin what is glossary" },
  { title: "What Is White Noise in Music Production?", url: "/articles/what-is-white-noise-music-production.html", tags: "white noise music production what is glossary" },
  { title: "Work for Hire Music Explained", url: "/articles/work-for-hire-music-explained.html", tags: "work for hire music law explained music business" },
  { title: "Yamaha HS5 Review", url: "/articles/yamaha-hs5-review.html", tags: "yamaha hs5 studio monitors review gear" },
  { title: "Yamaha HS5 vs KRK Rokit 5 G5", url: "/articles/yamaha-hs5-vs-krk-rokit-5-g5.html", tags: "yamaha hs5 krk studio monitors comparison gear" },
  { title: "Yamaha HS8 Review", url: "/articles/yamaha-hs8-review.html", tags: "yamaha hs8 studio monitors review gear" }
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
        .search-dropdown { display: none; position: absolute; top: calc(100% + 6px); right: 0; left: auto; background: var(--bg-elevated, #1a2332); border: 1px solid var(--teal, #00d4a8); border-radius: 10px; z-index: 9999; overflow: hidden; box-shadow: 0 8px 32px rgba(0,0,0,0.4); min-width: 320px; }
        .search-dropdown.open { display: block; }
        .search-result-item { display: block; padding: 10px 14px; color: var(--text-primary, #e2e8f0); text-decoration: none; font-size: 0.88rem; border-bottom: 1px solid rgba(255,255,255,0.06); transition: background 0.15s; cursor: pointer; }
        .search-result-item:last-child { border-bottom: none; }
        .search-result-item:hover, .search-result-item.focused { background: rgba(0,212,168,0.12); color: var(--teal, #00d4a8); }
        .search-no-results { padding: 12px 14px; color: var(--text-secondary, #8899aa); font-size: 0.85rem; }
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
        dropdown.innerHTML = '<div class="search-no-results">No articles found &mdash; try different keywords</div>';
        dropdown.classList.add('open');
        return;
      }
      const label = document.createElement('div');
      label.className = 'search-dropdown-label';
      label.textContent = results.length + ' article' + (results.length !== 1 ? 's' : '') + ' found';
      dropdown.appendChild(label);
      results.forEach(article => {
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
      debounceTimer = setTimeout(() => { showResults(searchArticles(q)); }, 150);
    });

    inputEl.addEventListener('keydown', (e) => {
      if (!dropdown.classList.contains('open')) return;
      if (e.key === 'ArrowDown') { e.preventDefault(); currentFocus = Math.min(currentFocus + 1, resultsItems.length - 1); resultsItems.forEach((el, i) => el.classList.toggle('focused', i === currentFocus)); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); currentFocus = Math.max(currentFocus - 1, 0); resultsItems.forEach((el, i) => el.classList.toggle('focused', i === currentFocus)); }
      else if (e.key === 'Enter' && currentFocus >= 0 && resultsItems[currentFocus]) { e.preventDefault(); window.location.href = resultsItems[currentFocus].href; }
      else if (e.key === 'Escape') { hideResults(); inputEl.blur(); }
    });

    formEl.addEventListener('submit', (e) => { e.preventDefault(); const q = inputEl.value.trim(); if (q.length >= 2) showResults(searchArticles(q)); });
    document.addEventListener('click', (e) => { if (!formEl.contains(e.target)) hideResults(); });
    inputEl.addEventListener('blur', () => { setTimeout(hideResults, 200); });
  }

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
     BACK TO TOP
  ------------------------------------------------ */
  let backToTop = document.getElementById('backToTop');
  if (!backToTop) {
    backToTop = document.createElement('button');
    backToTop.id = 'backToTop';
    backToTop.setAttribute('aria-label', 'Back to top');
    backToTop.innerHTML = '&#8679;';
    document.body.appendChild(backToTop);
  }
  window.addEventListener('scroll', () => { backToTop.classList.toggle('visible', window.scrollY > 500); }, { passive: true });
  backToTop.addEventListener('click', () => { window.scrollTo({ top: 0, behavior: 'smooth' }); });

  /* ------------------------------------------------
     AUTO-GENERATE TABLE OF CONTENTS
  ------------------------------------------------ */
  const articleBody = document.querySelector('.article-body');
  if (articleBody) {
    const headings = Array.from(articleBody.querySelectorAll('h2'));
    headings.forEach((h, i) => {
      if (!h.id) {
        h.id = 'section-' + (h.textContent.trim().toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'section-' + i);
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
            tocLinks.forEach(link => { link.parentElement.classList.toggle('active', link.getAttribute('href') === '#' + id); });
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
    readTimeEl.textContent = Math.max(1, Math.round(words / 200)) + ' min read';
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
        window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - 24, behavior: 'smooth' });
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
      btn.textContent = 'Subscribing...';
      btn.disabled = true;
      setTimeout(() => {
        btn.textContent = 'You\'re in!';
        btn.style.background = 'var(--teal-dim)';
        emailInput.value = '';
        setTimeout(() => { btn.disabled = false; btn.textContent = 'Subscribe Free'; btn.style.background = ''; }, 5000);
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

  /* ------------------------------------------------
     LAYOUT FIXES -- sidebar sticky, header overflow
  ------------------------------------------------ */
  (function applyLayoutFixes() {
    function fix() {
      const aside = document.querySelector('.article-layout aside');
      if (aside && !aside.classList.contains('article-sidebar')) aside.classList.add('article-sidebar');
      const headerInner = document.querySelector('.header-inner');
      if (headerInner) headerInner.style.overflow = 'visible';
      if (window.innerWidth <= 900 && aside) aside.style.display = 'none';
    }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fix);
    else fix();
    window.addEventListener('resize', function () {
      const aside = document.querySelector('.article-layout aside');
      if (aside) aside.style.display = window.innerWidth <= 900 ? 'none' : '';
    });
  })();

  /* ------------------------------------------------
     NAV LINK ABSOLUTE PATH FIX
  ------------------------------------------------ */
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
    };
    document.querySelectorAll('nav a, header a, .breadcrumb a').forEach(function (a) {
      const href = a.getAttribute('href');
      if (href && fixMap[href]) a.setAttribute('href', fixMap[href]);
    });
  })();

  /* ------------------------------------------------
     OLD-STRUCTURE MOBILE NAV TOGGLE
  ------------------------------------------------ */
  (function () {
    var oldToggle = document.querySelector('.mobile-nav-toggle');
    var oldNav = document.getElementById('mainNav');
    if (!oldToggle || !oldNav) return;
    oldToggle.addEventListener('click', function () {
      var isOpen = oldNav.classList.toggle('open');
      oldToggle.setAttribute('aria-expanded', String(isOpen));
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && oldNav.classList.contains('open')) {
        oldNav.classList.remove('open');
        oldToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    });
    oldNav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () { oldNav.classList.remove('open'); oldToggle.setAttribute('aria-expanded', 'false'); document.body.style.overflow = ''; });
    });
    document.addEventListener('click', function (e) {
      if (oldNav.classList.contains('open') && !oldNav.contains(e.target) && e.target !== oldToggle) {
        oldNav.classList.remove('open'); oldToggle.setAttribute('aria-expanded', 'false'); document.body.style.overflow = '';
      }
    });
  })();

  /* ------------------------------------------------
     FAQ ACCORDION
  ------------------------------------------------ */
  window.mpwFaqToggle = function(btn) {
    const item = btn.closest('.faq-accordion-item');
    if (!item) return;
    const answer = item.querySelector('.faq-accordion-a');
    const icon = item.querySelector('.faq-accordion-icon');
    const isOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-accordion-item.open').forEach(el => {
      el.classList.remove('open');
      const a = el.querySelector('.faq-accordion-a'); if (a) a.style.display = 'none';
      const ic = el.querySelector('.faq-accordion-icon'); if (ic) ic.textContent = '+';
    });
    if (!isOpen) {
      item.classList.add('open');
      if (answer) answer.style.display = 'block';
      if (icon) icon.textContent = '-';
    }
  };

})();

/* ------------------------------------------------
   SKIMLINKS affiliate monetisation
------------------------------------------------ */
(function () {
  var s = document.createElement('script');
  s.type = 'text/javascript';
  s.async = true;
  s.src = 'https://s.skimresources.com/js/302596X1790597.skimlinks.js';
  (document.head || document.body).appendChild(s);
})();
