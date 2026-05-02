# Log

## Tags

* **Business** – monetisation, subscriptions, pricing, and financial strategy.
* **Brand** – institutional persona, identity.
* **Social** – social‑media platforms, audience growth, analytics, engagement tactics, and cross‑platform strategy.
* **Community** – follower interactions, community regulation, moderation policy, and Shabbat observance.
* **Web** – public‑facing website components, such as the scripture browser and online platform.
* **Media** – audio, image, and video production pipelines, overlays, publishing, and visual assets.
* **PsalmSeries** – the daily Psalms video series.
* **ParashahSeries** – the weekly Torah portion video series.
* **Piyutim** – liturgical poetry and music videos.
* **AramaicClass** – the Aramaic language course.
* **HistoryBooklets** – the Halakhah, Haggadah, History booklet series.
* **Studio** – the unified internal production environment (editing, generation, and content‑creation tools).
* **Font** – Hebrew typography, font testing, rendering fixes, and the FontStudio tool.
* **Code** – internal scripts, platform builds, parsers, and any code that doesn’t yet belong to a more specific label.
* **Libraries** – released, reusable library packages (Hebrew date, sun/moon, sensors, etc.).
* **Android** – mobile application development.
* **Documentation** – project logs, writing, formatting, and archival of the Institute’s work.
* **General** – meta‑discussions, workflow, project management, and any topic not yet covered by another label.

## Sessions

#### [2 May 2026 – 📖 DeepSeek 3 – Project log reconstructed and formatted](20260502.md)

Took a fragmented, partially mis‑dated collection of over 80 project logs and turned them into a single, chronologically sound chronicle from July 2025 through May 2026. Anchored dates to verifiable events (11 Aug subscriptions, 2‑3 Aug Tisha B'Av fast, 14 Aug thank‑you video). Designed standardised entry format: date + model + title header, italicised tags, first‑person plural narrative, proper heading hierarchy, verbatim code blocks, `mdx-breakless-lists` for list rendering. Worked around DeepSeek parser nested‑fence bug with double‑backtick cheat. Refined tag taxonomy (PsalmSeries, ParashahSeries, AramaicClass, HistoryBooklets). Developed dual‑layer documentation architecture: `log.md` (74 KB, ~18 500 tokens) as LLM‑optimised dense summaries; individual `.md` entries (212 KB, ~54 100 tokens) as human‑readable narrative. Original source files preserved as immutable `.txt` in `orig/` (224 KB). Recovered six missing sessions from an old log snapshot (12 Feb – 19 Mar 2026), bringing the final archive to 104 session entries (99 main + 5 booklets) plus 6 originals = 110 files total. Cross‑model validation: tested `log.md` against six AI models (DeepSeek Expert/Instant, Gemini Flash/Thinking/Pro, Claude, ChatGPT, Grok); all delivered specific, technically grounded analyses referencing Golden Egg, architectural discipline, blockquote disaster as cautionary benchmark, and spiritual counter‑programming. Confirmed that `log.md` alone brings any future collaborator to full working context in a single prompt.

#### [31 Mar 2026 – 📖 DeepSeek 3, Gemini 3 – Blockquote formatting disaster, LLM limits confirmed](history-booklets/20260331.md)

Attempted strict rule‑based reformatting of all blockquotes across the bilingual Pesach booklet using two LLMs. Rules: single `>`, underscore italics, colon‑introduced speech with `&emsp;`, bold straight double quotes, nested single quotes, exact Hebrew punctuation match. Across ~14 hours: 118 prompts, 47 explicit rejections (39.8%), 27 all‑caps prompts, 189 uses of "fuck." Worst loops: 12 iterations for one Zohar quote, 11 for Song of the Sea, 9 for Talmud Sotah, 8 for Midrash Tanchuma. Final files were eventually correct, but cost was indefensible. Root cause: LLMs are probabilistic, not deterministic executors; complex formatting at scale requires scripts. Session preserved as permanent cautionary benchmark.

#### [28 Mar 2026 (c) – 📖 DeepSeek 3 – Flask app refactored with Booklets.py data model](history-booklets/20260328c.md)

Replaced raw Markdown files and inline Flask templates with a clean data layer. Built `TraditionBooklet` (metadata, language availability, text content with `english_html`/`hebrew_html` properties) and `TraditionCollection` (CSV‑driven, lookup by basename, `__getitem__`). All file ops use `pathlib.Path`. Extracted templates to external files; routes now exclusively use the data layer. Added `core` boolean field to `booklets.csv` to distinguish annual observances from life‑practice topics. Updated documentation with star‑emoji markers and full API reference. Clean separation: `Booklets.py` owns all data; `app.py` handles only requests.

#### [28 Mar 2026 (b) – 📖 DeepSeek 3, Gemini 3 – Lag BaOmer workflow validation, Parts 1–2 written](history-booklets/20260328b.md)

Tested the Pesach workflow on a minor, post‑biblical festival with thinner sources. Applied the same method: define five‑part structure, gather references, convert sources to block‑quote format, write connective narrative, polish with Gemini. Part 1 anchored the holiday in Talmudic context; Part 2 traced medieval emergence, Zohar's role, Safed revolution, halakhic codification, and Hasidic embrace. Workflow validated as robust and transferable across diverse content types.

#### [28 Mar 2026 – 📖 DeepSeek 3, Gemini 3 – Pesach booklet first draft completed](history-booklets/20260328.md)

Began with a near‑empty `pesach.en.md` skeleton; ended with a complete 12 000‑word first draft. Scope strictly Exodus narrative; Part 1–5 structure (Foundations, Evolution, Practice, Mystical Dimensions, Global Traditions) plus Tales. Gemini used as poetic renderer: bare verse lists transformed into flowing prose, blockquotes with italicised citations and em‑dash sources. Evolution spanned biblical through Hasidic sources; Practice covered full Seder guide; Mystical drew from Zohar, Arizal, Maharal, Hasidut; Global Traditions anchored on kitniyot divide, expanded to Yemenite, Ethiopian, Italian, Persian communities, closing with Mimouna and Seharane. Four classic tales framed with introduction and conclusion, unified by "Next year in Jerusalem." Workflow became template for all subsequent booklets.

#### [21 Mar 2026 – Gemini 3 Flash – Documentation refactor: 18‑file stable core, standards centralization](20260321.md)

Stripped marketing fluff from documentation, rebuilt as a functional Production Blueprint. Unified production standard: hybrid 1970s Shmuelov recordings + AI cloning (Dark Knox 2), synchronized captions, fog backgrounds, platform‑specific versions (added WhatsApp as bridge for no‑browser demographic). Series‑specific logic: Parashah into Episodes (social) and Full (study archive); Psalms into Individual, 4‑Week Cycle, Books, Master Archive; Piyutim into Master Audio, Technical Video (waveforms/stems), Artistic Music Video. IVR ecosystem: 10+2 quiz structure, weighted scoring, 0:00 Sunday hard reset; physical "handshake" verification (winners present phone to sponsor for live SMS check). Consolidated into `ReubenInstitute.md` master record.

#### [19 Mar 2026 – DeepSeek 3 – System‑wide refactor: Asset base class and media architecture rebuild](20260319.md)

Introduced `Asset` base class (`size`, `width`, `height`, `landscape`) as single source of truth for dimensions; moved to `Media.py`, deleted `Content.py`. Redesigned visual hierarchy: `Image` (single image), `Plate` (text renderer), `Slide` (container for plates), `Video` (composition). Moved `Word` to `Text.py`. Replaced all legacy slide/overlay classes with modular plates/slides (`PsalmVersePlate`, `EpisodeParagraphSlide`, etc.). Refactored Bible data classes into pure data holders. Optimised audio pipeline: cached ElevenLabs title durations in `titles.csv`, eliminating runtime `ffprobe` calls. Touched nearly every core file; foundation for word‑level highlighting and multi‑format exports.

#### [17 Mar 2026 – Gemini 3 Pro – ffmpeg‑python MP3 frame bug solved, global cache buster](20260317.md)

Diagnosed `ValueError: Encountered format('rgba') ... with multiple outgoing edges` — `ffmpeg-python` merged identical‑duration nodes, branches on selective Fade In caused crashes. Root cause: MP3 frame quantization — ElevenLabs rounds similar‑length verses to same frame count → identical float durations. Refactored `ParashahEpisodeVideo` and `ParashahVideo`: replaced `segments` with independent `video_stream`/`audio_stream`; removed `.audio.filter('atrim')` (FFmpeg reads to EOF). The fix: global cache buster in `AudioAI.py` — when loading durations from CSV, tracks each in a set; if duplicate, subtracts 1 µs (`0.000001`) until unique. Mathematically unique, physically imperceptible, non‑destructive to on‑disk CSV. Single line at the data layer eliminated months‑long blocker.

#### [16 Mar 2026 (b) – Gemini 3 Pro – Audio.py redundant classes removed, directory handling](20260316b.md)

Cleaned up `Audio.py` further: removed redundant experimental classes (`OLDPsalmsBookAudio`, `XPsalmsCompleteAudio`, `xPsalmsCompleteAudio`), duplicate methods (`Xexport_mp3`), deprecated properties (`xsegments`, `xduration`). Stripped debugging `print` statements and commented‑out legacy ID3 code. Streamlined `BibleAudio`: cleaned directory creation, removed unused `try`/`except` blocks in duration calculations. Final structure: `BibleAudio` (filesystem, timings, verse exports), `BaseAudio` (shared FFmpeg streaming/export), `PsalmAudio`, `PsalmsBookAudio`, `PsalmsCompleteAudio`, `DailyPsalmsAudio`. Lean, production‑ready.

#### [16 Mar 2026 – Gemini 3 Pro – Media architecture: pure OOP, composition, unified export()](20260316.md)

Ditched rigid inheritance hierarchy for pure OOP. Problem: paths and filename formatting scattered across code; `BaseVideo`/`BaseAudio` forced fixed sequences that broke with custom logic. Shift: artifacts own their own metadata and file paths; composition over inheritance — derived classes assemble their own internal timelines and streams; base classes reduced to "dumb printing presses" handling only final FFmpeg execution with standardised encoding. Implemented `video_stream` and `audio_stream` properties on `PsalmHebrewVideo` returning finalized FFmpeg nodes. `BaseVideo` gained new `export()` function treating streams as black boxes and writing to object‑provided path. Path, filename, and folder logic now encapsulated within classes.

#### [15 Mar 2026 – Gemini 3 Pro – Audio code cleanup, title generation, naming standardized](20260315.md)

Purged `Audio.py`: deleted obsolete classes (`OLDPsalmsBookAudio`, `XPsalmsCompleteAudio`), removed disabled `X`‑prefixed methods and commented legacy code. Consolidated scattered ElevenLabs title‑generation test scripts into a single `generate_titles.py` (main, book, daily‑cycle, individual psalm titles). Standardized file naming from mixed transliterations/functional labels to clean English: `tehilim.mp3` → `psalms.mp3`, `titleXXX.mp3` / `pXXX.mp3` → `psalmXXX.mp3`, `tehilim-fourweek-complete.mp3` → `psalms-4weeks.mp3`. Wrote `rename_titles.py` to rename existing assets. Replaced trailing‑dash convention with `‑raw` suffix (`psalm001-raw.mp3`). Killed `BaseAudio` as mandatory base; flattened `PsalmAudio` to self‑contained class with explicit `export_mp3()` and `export_raw_mp3()`.

#### [14 Mar 2026 – DeepSeek 3 – Psalms audio library completely rebuilt, multi‑format export](20260314.md)

Rebuilt entire Psalms audio library from raw cloned verses. Regenerated problematic verses; backfilled word‑level alignment for all 150 psalms; standardised text (removed curly braces, tildes, asterisks, zero‑width joiners; preserved Jerusalem spelling). Generated 150 psalm titles, 5 book titles, 28 daily titles, and master “תהילים” via ElevenLabs Dark Knox 2. Built new audio classes: `PsalmAudio` (title as first segment), `PsalmsBookAudio`, `DailyPsalmsAudio`, `PsalmsCompleteAudio` (5 h 39 min, 156 MB), `FourWeekCompleteAudio` (5 h 37 min, 155 MB). Fixed ffmpeg “Argument list too long” with pre‑exported intermediates. Unified ID3 tagging via `Media.set_id3_tags`. Transparent title background via `nullsrc + format=rgba + geq`. Planned SD card distribution for Meron community (“March 2026 Edition”).

#### [4 Mar 2026 – DeepSeek 3 – Multi‑track stem visualization for Piyut videos](20260304.md)

Extended visualisation system for Suno multi‑track stems: split `AudioVisualization` into `TrackDisplay`/`MultiTrackDisplay`. `Composition` class gained automatic stem‑folder detection and sorting. `generate_visualization` conditionally switches single/multi‑track modes while preserving backward compatibility.

#### [17 Feb 2026 – Gemini 3 Pro – Psalm‑Align Editor foundation and BPM calibration](20260217.md)

Built Psalm‑Align Editor foundation: new `/align` route and `psalm-align.html` page. Fixed temporal resolution at 12 px/s. Four‑value dashboard: Beat duration, Bar duration, Gross Beat/Bar counts. Integrated multi‑subdivision BPM tapper widget. Validated ffprobe‑to‑frontend duration passing end‑to‑end.

#### [13 Feb 2026 – DeepSeek 3 – “Imageless” videos, evening/morning rhythm, remaining Tikun Haklali](20260213.md)

Rebranded clean fog‑plus‑voice videos as “imageless.” Formalised morning/evening publishing rhythm, validated with Psalm 66 (3 900 views, 52 shares). Audited Tikun Haklali: identified four missing Psalms (42, 105, 137, 150). Sketched horizontal imageless YouTube strategy for extended watch times.

#### [12 Feb 2026 – DeepSeek 3 – Psalms visual geography, MediaLibrary with MD5 clips](20260212.md)

Locked the five‑book environmental arc into 20 canonical places with psalm assignments in `Psalms.md`, making visual identity a searchable reference. Built `MediaLibrary` system around MD5‑hashed `Clip` objects with exact fps/frame‑count metadata, CSV persistence, `set_label()` for one‑click folder reassignment, and automated thumbnail generation with disk caching. Turned a video directory into a queryable, indexed asset library.

#### [13 Jan 2026 (b) – DeepSeek 3 – Delta system and timeline refactoring](20260113b.md)

Removed mandatory `timestamp` requirement from the declarative video engine; items now play sequentially by default. Designed `delta` property (positive for gaps, negative for overlaps) for future use. Refactored into Input classes (source handling, stream splitting), Clip classes (per‑item processing), and Composition pipeline. Updated JSON schema: `timestamp` optional, `delta` added, `duration` minimum 0. Robust testing: schema validation before tests, comprehensive audio/video/mixed cases, immediate failure on errors. System handles sequential playback, multi‑clip reuse, per‑item/global fades, mixed timelines, silent/black generation. Ready for delta‑based gaps/overlaps, image/text rendering, complex transitions.

#### [13 Jan 2026 – DeepSeek 3 – Declarative video composition (JSON timeline)](20260113.md)

Designed and implemented a declarative JSON‑based video composition system. JSON schema: assets (videos, audios, images, fonts) as file‑path arrays; timeline of items with type, timestamp, duration, offset, loop; effects (fadein/fadeout, eq, loudnorm) per‑item and global; `null` for generated black/silent media, negative start times for end‑relative positioning. Two core classes: `Content` (JSON I/O, validation), `Video` (universal renderer to MP4/MP3). Specialized `AudioInput`/`VideoInput` handle duration probing, stream splitting for reuse, silent/black generation. Enables Psalms, Torah portions, Aramaic lessons, Piyutim videos from one engine. Principles: fanatically clean JSON, zero over‑engineering, separation of concerns, declarative over imperative.

#### [11 Jan 2026 – DeepSeek 3 – Aramaic noun series & production enhancements](20260111.md)

Evaluated Class 4 Pronouns draft, refined wood‑figurine specs (Avraham, Miryam, Binyamin, Rivka). Strategic pivot: new public‑facing short video series teaching Aramaic nouns (animals) by letter — letter slide + IPA sound, then video clips with Aramaic labels. Examined `animals.json` and `course.py` for safe zones and flexible positioning. Designed wooden‑arm pointing cue for "your turn" moment. Audio chain: FFmpeg `loudnorm`, compressor, equaliser, subtle reverb for AI‑cloned narration. Crafted optimized TikTok description to launch the series.

#### [9 Jan 2026 – DeepSeek 3 – Psalm 8 cinematic pipeline & TikTok duet](20260109.md)

Expanded a "calm ocean" asset table entry into a 7‑shot cinematic storyboard for Psalm 8 (POV and aerial shots, two with 0.7×/0.8× speed adjustments). Wrote `rename.py` to process downloaded assets, applying speed adjustments with `ffmpeg-python` at CRF 18. Composited clips, added Suno music, published enhanced video. Gemini blind analysis correctly identified theological themes and cinematic language. TikTok showed strong engagement and a "camel‑back" viewership curve. Organic UGC: user David Ming duetted the video to practise Psalm 117 in Hebrew. Validated the full pipeline from asset engineering through publication and impact.

#### [8 Jan 2026 – Gemini 3 Flash – Asset Vault with UUID and DNA workflow](20260108.md)

Established 3‑step Genetic workflow: Square DNA (1:1 image, locks composition) → SD Branching (Portrait 9:16, Landscape 16:9) → Final Video. Portrait = SD, Landscape = HD Master; identical duration for format‑agnostic swapping. Lean Asset Vault: custom Markdown table with simple descriptors (square, portrait, landscape) as clickable Midjourney job links; last 5‑6 characters of UUID as search key matching downloaded filenames. Ghost Ship Rule: discard AI hallucinations immediately, rewind to last clean Job ID, re‑roll extension. Integrated tables into `Psalms.md` master draft as Production Bible. Row 1 (Calm Ocean) officially Mastered.

#### [6 Jan 2026 – DeepSeek 3 – Aramaic phonetic tables & visual pedagogy](20260106.md)

Built dual‑purpose consonant tables (descriptive for learners, exact IPA for academics), vowels table, "Special Consonants" list (15 letters needing diagrams). Added `(+dagesh)/(-dagesh)` notation. Separated Teaching Assistants from Professor. Three visual style options: plasteline figurines, La Linea minimalist line art (vertical‑optimized), photo‑realistic ancient. Defined 7‑voice system: 1 Professor + 3 male TA + 3 female TA, cloned via ElevenLabs; plural voices use multiple originals with different clones. Added individual phonetic classes (vowels, begadkefat, gutturals); fixed class numbering collision. "Appearing features" principle for abstract styles.

#### [5 Jan 2026 (b) – DeepSeek 3 – Aramaic course development](20260105b.md)

Designed subscription‑based Aramaic language course with 6‑class progression: Nouns → Adjectives → Numbers → Pronouns → Verbs → Prepositions & Particles. Table‑driven pedagogy linking Hebrew script, IPA, physical actions; authentic Eastern (Babylonian) Aramaic pronunciation. Figurine‑based instruction: gender‑differentiated plasteline forms, facial features appearing only when needed, roles indicated by minimal props (crown, hammer, crook). Visual environment: professor arm + pointing stick + green chalkboard; figurine world on sterile blank floor with soft geometry, muted textures, unified material language. Teaching: spatial logic + pointing, cross‑gender reinforcement, progressive complexity. Delivered Class 3 (Numbers 1‑3 with corrected IPA) and Class 4 (Pronouns, 32‑row pointing table). Ready for pilot production.

#### [5 Jan 2026 – Gemini 3 Flash – Cinematic roadmap for Psalms Book 1](20260105.md)

91‑minute roadmap for Book 1: 5‑day, 4‑night journey (Days 11–16 min active travel, Nights 4–6 min stationary reflection). Landscape Continuity: each night belongs to preceding day's environment. Day 3 is visual heart (Psalms 23, 27 against underwater/bioluminescent backdrop). Three Tikun Haklali milestones (16, 32, 41) marked for emphasis. Night 4 campfire as emotional pivot (isolation → hope). Every Psalm itemized with role and timing for concrete production schedule.

#### [4 Jan 2026 – DeepSeek 3 – Clipboard feature for Psalm descriptions](20260104.md)

Added one‑click clipboard copying for pre‑formatted Psalm descriptions. Backend: `descriptions.md` templates parsed by `##` headers, rendered via Jinja2 with psalm context, dictionary mapping types to rendered text. Frontend: dynamic buttons per description type, JavaScript `navigator.clipboard.writeText()`. Minimal changes (~15 lines in route), no dependencies, scalable (edit Markdown file to add types). Clean separation: templates external, logic in route.

#### [2 Jan 2026 – DeepSeek 3 – Web‑based video editor for Psalm videos](20260102.md)

Timeline engine (`Editor.py`): 150 projects, `ClipItem` with timestamps/offsets; constraints (no gaps, max 2 overlaps); FFmpeg export with fade‑through‑white for adjacent clips, crossfade for overlaps, auto gap‑filling. Web interface (`editor-app.py`): project browser, timeline visualization (colored blocks), asset management with thumbnails. Streaming: segmented 10‑second chunks, smart preloading at 5‑second mark, custom events (timeupdate, segmentchange, ended). Controls: space for play/pause, timeline click to seek, real‑time time display. Accidental verse‑timestamp system: `timestamps.csv` via `BibleAudio.timestamp()`/`set_timestamp()`, ready for future audio‑synced video.

#### [30 Dec 2025 – Gemini 3 Flash – Production Bible for Psalms cinematic series](20251230.md)

Monthly budget ~462 NIS ($125): Google One AI Pro (74.9 NIS) for Braided segments, Midjourney Pro (~192 NIS) for Master Reference images enforcing five thematic colours (Blue/Green/Red/Yellow/Purple) across five months. 5.5‑hour movie from ~70 minutes unique AI Seed video. 20‑day Mosaic narrative: 5 Books paralleling Torah, each with environmental journey (Ocean, Forest, Scorched Earth, Wilderness, Mountain Ascent). Stealth Reusability Matrix: 6 tricks to stretch footage (variable offset, reverse, mirror, digital zoom 70–100%, speed ramp 70–100%, Temporal Vision Flash 2–5s glimpses). Temporal Quarantine: One‑Psalm Buffer rule — any burned timestamp range cannot reappear in current or next Psalm.

#### [28 Dec 2025 (b) – DeepSeek 3 – Cross‑platform strategy & Psalm 90 model cycle](20251228b.md)

Merged TikTok columns (C/E/O) into one; standardized version codes (001C, 001E, 001H, 001O). Split Psalms table by Book (1–5). Defined platform rules: TikTok & Instagram get all versions daily; YouTube only if final video < 4:00 (else substitute); Spotify enhanced audio; WhatsApp enhanced notifications. "Finish‑and‑forget" nightly workflow. Psalm 90 as model cycle: 090C (clean+fog) 7:30 AM, 090E (enhanced+autumn tunnel+duduk) 7:30 PM; validated by Gemini. Refactored PsalmCover applied. Landscape videos on pause; vertical/shorts priority.

#### [28 Dec 2025 – DeepSeek 3 – PsalmCover class refactoring](20251228.md)

Simplified `PsalmCover` by removing complex `Image.draw_text()` and using PIL's native `canvas.text()` with manual bounding‑box centering. Font loading via `ImageFont.truetype()`. Portrait mode only (720×1280); landscape empty placeholder. Two modes: `enhanced=False` uses `back.mp4` with color overlay and blur, `enhanced=True` uses specific psalm video. Text layout: "תהילים" at 35% height (size 120), Hebrew number centered at 53% height (size 260). Drop shadows for contrast. Design principles: right tool for job, YAGNI, KISS, separation of concerns (cover vs verse rendering).

#### [27 Dec 2025 (b) – DeepSeek 3 – Spotify distribution & bilingual ID3 tagging](20251227b.md)

Direct podcast upload chosen over music distributors for control and non‑commercial mission. Content structure: Psalms Show (Enhanced only, with AI music), Piyutim Show, Parashot Show (voice‑only). Full AI‑tool attribution (Suno, ElevenLabs, Midjourney); voice source credited to Abraham Shmuelov (1970s recording). ID3 tagging: Hebrew tags (Title, Artist, Publisher, Content Group), English tags (Composer as Suno AI v5, Genre as World Fusion #90), bilingual comment with liturgical description and credits. Python script using Mutagen for batch‑tagging and English‑transliterated filenames. Principles: mission over monetisation, transparency, control, quality, system over sprint.

#### [27 Dec 2025 – DeepSeek 3 – Audio system refactoring](20251227.md)

Separated audio generation from video generation. New class hierarchy: `BaseAudio` (abstract), `PsalmAudio` (implements for Psalms), `[planned: ParashahAudio]`. Properties: `segments` (verse clips with fades), `music` (background stream), `stream` (clean narration), `enhanced_stream` (narration+music), `duration`, `basename`. Export functions: `export_mp3()`, `export_clean_mp3()`, `export_sln()`, `export_clean_sln()`. Studio integration: route `/export-audio/psalm/<number>`, "Export Audio Files" button, auto‑redirect.

#### [26 Dec 2025 – DeepSeek 3 – Media strategy & production system](20251226.md)

Documented TikTok inventory: 34 Clean (fog+voice), 9 Enhanced (AI bg+music), 15 Old, 2 Multilingual. Coded versions: C/E/O/M. Sustainable 1.5h/day workflow producing both Clean and Enhanced versions. Random Psalm selection for curiosity. Dual daily posting: Clean 7 AM, Enhanced 7 PM across platforms. "Finish and forget" philosophy. Multi‑platform: TikTok lead, Instagram/YouTube mirroring, catch‑up legacy content. Growth: 5.6K followers, 43K weekly views (+362%), targeting 100K/28 days for subscription unlock. Next: daily random production, fill Instagram/YouTube gaps, fix FFmpeg Parashah bug, Piyutim format, monitor threshold.

#### [24 Dec 2025 – DeepSeek 3 – “Essa Einai” music video production](20251224.md)

Concept: desert campfire gathering. Symbolic shots: drone over empty desert, lone hooded nay player on cliff under stars, aerial of solitary singer by small fire, solemn crowd encircling fire, epic aerial of concentric circles (musicians, orchestra, dancing crowd). Technical: 5 GPU hours, SD renders, 12‑16s segments. Breakthrough: "scene evolution" technique — one base image, tweak prompt (remove orchestra) for consistent narrative stages. Production: concise scene descriptions → Midjourney base images → extended to video clips → composited with Suno music. Gemini blind analysis: correctly identified journey "from solitude to community," understood symbols, framed AI aesthetic as "timeless" and "epically spiritual." Validated scalable AI production workflow.

#### [23 Dec 2025 – Gemini 3 Pro – Rebranding and Sibling Loop video standard](20251223.md)

Rebranded bio from "Publishing House" to "Publishing Studio & Research Institute." Solved jittery AI video with Concatenated Triptych: 1 master prompt → 2‑3 Sibling variations (Vary Subtle) → extend each ~10s → cross‑dissolve into seamless 20s+ file. 6x GPU cost but creates permanent Asset Equity. Validated assets: Pastoral (Green Fields, Ps 84), Ascent (Stone Path, Ps 120‑134), Wilderness (Cracked Earth), Depths (Dark Ocean, Ps 130/137), Firmament (Clouds/God Rays, Ps 148/150). Burn‑down: 15 Master Loops for Texture Library (Water, Sky, Fire/Earth collections); audio punch‑in/punch‑out for defective verses only; skipping Psalm 119. Python automation: generate_loop.py with ffprobe/ffmpeg for duration calculation, overlap trimming, cross‑dissolves. Darken/Blur filter confirmed for text legibility.

#### [21 Dec 2025 – DeepSeek 3 – Audio editing improvements & homepage statistics](20251221.md)

Keyboard shortcuts for waveform editor: ←/→ 0.1s, ↑/↓ 1s, S toggles start/end markers, spacebar play/pause; auto‑focus. WaveSurfer.js fix: version uses `region.setOptions()` not `region.update()`. Homepage stats: split Parashot/Psalms counts with icons (🔊Original, 👥Cloned, 🇺🇸English), cumulative durations formatted MM:SS or H:MM:SS. Minimal changes, preserved all existing functionality.

#### [18 Dec 2025 (b) – Gemini 3 Pro – Full Parashah strategy & credit burn](20251218b.md)

Pivoted from splitting Parashot into small episodes to "Full Parashah" strategy: one 25‑minute "movie" per week, removing decision fatigue, building Library/Box Set. Roadmap: 3 full videos per week until synced with calendar (4 weeks). Credit burn: 310,000 ElevenLabs credits + 10.5 Midjourney hours expiring in 6 days. Burn list: Parashah 12 (Vayechi, season finale, top priority), Genesis Gap (5–10), Psalms 85–150 (incl. 119 for test, 121 for viral), Exodus 13–14 after bug fix. Data validation: 32.3s avg watch time (vs 5s norm), 13% completion. Insight: counter‑programming — calm spiritual medicine in noisy feed.

#### [18 Dec 2025 – DeepSeek 3 – Video asset system review & music generation](20251218.md)

Reviewed structured video asset inventory (index.md). Established music generation pipeline: Suno.md prompts combining keys/modes (lament, wisdom, praise) with instruments (drone pads, low strings, harp, ney, waterphone), constrained to serious/meditative/reverent style, no rhythm or melody. Solved Suno duplicate naming ((1),(2)) with script appending creation timestamp. Gemini analysis of generated tracks. Regeneration priorities: Emin and Phrygian prompts most successful; Ambiguous DronePads and Bbmin flagged for regeneration.

#### [17 Dec 2025 (b) – DeepSeek 3 – Background video asset library creation](20251217b.md)

Systematic inventory of AI‑generated background videos. Workflow: Midjourney generation with standardized prompts, filter.py for washed‑out aesthetic, Gemini Vision descriptions, categorization by prompt and Psalm assignment, structured markdown. 10 videos in 5 categories: Lake (3, 1 assigned), Ocean (3, 1), Waterfall (1, 1), Forest Path (2, 0), Meadow (1, 0). Complete traceability: prompt → filename → description → usage. System ready for daily production with asset rotation.

#### [17 Dec 2025 – DeepSeek 3 – Text rendering and fake shadow fix](20251217.md)

Text unreadable due to fake shadows (offset duplicate), wrong functions for purpose, over‑engineering. Renamed `text` to `draw_text(canvas, xy, text, font, color, shadow, anchor, direction)`. Removed dead `if not extreme_chars:` branch. Fixed anchor="mm" support. Slide functions renamed to `draw_*_slide()`. Overlays stripped: no Word objects, no bbox calculations, no logo shadow; hardcoded positions (logo at 306,100). Shadow saga: attempted radial shadow but letter centers filled; original 4px+MaxFilter(3)×4+GaussianBlur(3) at 75% had dark centers. Code cleanliness drastically improved; shadow still problematic.

#### [14 Dec 2025 – DeepSeek 3 – Video production pipeline & TikTok revival](20251214.md)

Midjourney prompt template finalized: `[scene description], photorealistic, cinematic, atmospheric, serene, shallow depth of field, muted palette`. FFmpeg post‑processing for washed‑out look. Psalm 70 as production proof: custom lake background, Suno music at 20% volume, AI‑cloned Hebrew narration, text overlays. BaseVideo updated with auto‑mixing (`{psalm_number:03d}.mp3`), global 0.5s fades, stereo output. TikTok revival: 1,973 views in 14h, 266 likes, 30 saves, 22 shares, watch time 19.1→20.4s, +3 followers. Formula validated: washed backgrounds + music + cloned voice. Target niche: 40% completion rate. Quality > virality.

#### [13 Dec 2025 – DeepSeek 3 – Social media strategic review: Parashah batch priority](20251213.md)

Strategic review of social media series. Parashot: 4‑5 weeks behind schedule. Psalms: 36 videos published, format misaligned with Parashot branding. Piyutim: audio tracks done via Suno AI, no video yet. Audience: 5,418 followers, stagnant retention (net −2). Decisions: immediate batch of 4‑5 full Parashah videos within 7 days; align Psalms format with Parashot; begin Piyutim video production; add Hebrew CTAs to all videos. Priority shift: timely Parashot delivery over parallel series.

#### [11 Dec 2025 – 📖 Gemini 3 Pro – HHH series assessment and Hanukkah prototype](history-booklets/20251211.md)

Took stock of HHH booklet series: mature drafts for Tu B’Shevat, Shavuot, Hanukkah, Purim; early drafts for Tefillah, Bar Mitzvah. Explored “Three Lens” framework (Legal, Narrative, Historical). Chose Hanukkah as proof of concept: structure moving from history (war, oil) to practice (customs, foods) to mysticism (Kabbalah); wove in cultural texture (boutique sufganiyot, Kurdish eggshell menorahs, Chag HaBanot); anchored primary sources (Sefer Josippon, Talmud Shabbat 21b, Bnei Yissaschar). Sketched campaign: 24‑volume curated library, seasonal shipping, possible Kickstarter.

#### [3 Nov 2025 – DeepSeek 3 – Hebrew character database and text normalization system](20251103.md)

Built Hebrew character database (`Hebrew.py`) with full Unicode definitions, `Letter`/`Diacritic` classification, property analysis. Text normalization: `normalize()` applies NFC, splits by `\P{M}\p{M}*`, reorders combining characters per rendering order. Utilities: `strip_punctuation`, `strip_cantillation`, `strip_diacritics`, `strip_hebrew_punctuation`, `strip_yy`, `strip_yhwh`, `presentation`. Font analysis system (`fontstudio.py`). Web interface with RTL styling. Achievements: proper rendering order, complete character coverage, automated font testing, multi‑level text processing pipeline.

#### [2 Nov 2025 – DeepSeek 3 – Hebrew font testing app refactored to OOP](20251102.md)

Refactored Hebrew font testing app from procedural to OOP. Class hierarchy: `Char`, `Letter` (classification: is_final, is_wide, is_begedkefet, is_guttural, can_have_dagesh, can_have_rafe, has_final_form), `Diacritic` (is_vowel, is_hataf, is_dagesh, is_rafe), `Hebrew` container. Replaced raw Unicode tuples with named constants. Fixed dagesh/rafe column logic, final form and guttural restrictions. Updated Flask app to OOP structure. Cleaner, maintainable, grammar‑aware.

#### [20 Oct 2025 (c) – DeepSeek 3 – Font metrics system with fontTools and Unicode](20251020c.md)

Extracted true font metrics (ascent, descent, linegap, units_per_em) from font files using fontTools; computed `line_spacing = ascent + descent + linegap`. Detected extreme characters for max vertical extents (letter + highest cantillation mark, letter + lowest diacritic). Built complete Hebrew Unicode database: 37 letters, 17 diacritics, 35 cantillation marks, extensive punctuation. Font class pre‑calculates metrics at init. Ready to update bbox/text methods and fix all rendering classes.

#### [20 Oct 2025 (b) – DeepSeek 3 – PIL text rendering height/linespacing fixed](20251020b.md)

Fixed `Image.text()` vs `Image.bbox()` height mismatch (bbox returned 68 px, text drew 500 px) by rewriting `text()` to use same extreme‑chars logic as `bbox()`, creating temp image with exact bbox dimensions, drawing at (0,0), auto‑clipping extreme chars. Removed arbitrary 1.3× line‑spacing multiplier; standardised on `Image.bbox()` over `canvas.textbbox()`. Key: PIL has no baseline; extreme chars needed for diacritic height; consistency between measurement and drawing critical. Files: `Image.py`, `test.py`.

#### [20 Oct 2025 – DeepSeek 3 – Media architecture completed after 52 sessions](20251020.md)

After 52 sessions, reached production‑ready launch of professional Torah video platform. All systems (text, audio, video, images) integrated and polished. Professional fades, typography, visual consistency. Scalable workflow: daily content generation now systematic. Journey: Dec 2023 storage exercise, Jul 2025 viral breakthrough, Oct 2025 professional platform. Transition from development to production.

#### [18 Oct 2025 – DeepSeek 3 – AudioPlayer class hierarchy and Flask routes](20251018.md)

Built class‑based audio player architecture: `AudioPlayer` base (play, pause, stop, seek, playPause); `SimpleAudioPlayer` (invisible playback), `VisualAudioPlayer` (waveform), `MarkerAudioPlayer` (region marking/cutting with drag/resize). Direct form updates, no event system. Routes: Psalm/Parashah audio editing, FFmpeg‑powered segment serving. Professional implementation: no `setTimeout` hacks, clean separation, dependency injection. Two‑button workflow (Save / Save & Next).

#### [17 Oct 2025 (b) – DeepSeek 3 – Bible slide generation unified to property‑based](20251017b.md)

Extended property‑based slide architecture to Articles, unifying with Psalms and Parashot. Fixed `BibleParashot.py` dummy slides, `BiblePsalms.py` mixed architecture and layout structure. Updated `app.py` and `studio.py` routes. New architecture: unified layout → slides → save(). Consistent approach across all Bible content types; no mixed architectures; clean separation of data loading vs. presentation.

#### [17 Oct 2025 – Gemini 2.5 Flash – Torah colour mapping with RGB and gradient logic](20251017.md)

Assigned RGB colours to the five books of the Torah: Genesis Royal Blue (65,105,225), Exodus Forest Green (34,139,34), Leviticus Firebrick Red (178,34,34), Numbers Gold/Yellow (255,215,0), Deuteronomy Indigo/Purple (75,0,130). Parashah gradient: inverted from light→dark to dark→light (`lightness_factor = 0.4 + (0.4 * progress)`). Integrated into Flask route `/bible/parashot/<number>` with a “צבע” column showing inline background colour.

#### [16 Oct 2025 – DeepSeek 3 – Parashot and Psalms slide generation refactored](20251016.md)

Refactored both Parashot and Psalms to consistent property‑based architecture. `BibleParashot.py`: `paragraph.slides` returned dummy `Slide` objects — fixed to return `ParashahSlide` with working `save()`. `BiblePsalms.py`: removed slide creation from `load()`; fixed `psalm.layout` to preserve verse structure; added `paragraph.layout` and `paragraph.slides` properties. Architecture: Psalm/Parashah → `layout` property → paragraph → `layout` → `slides` → `slide.save()`. `ParashahSlide`: complex `$`‑marker splitting; `PsalmSlide`: 1 verse = 1 slide. Tests confirm Psalms work.

#### [14 Oct 2025 – DeepSeek 3 – Video.py base classes, psalm/parashah episode generation](20251014.md)

Created `Video.py` with base classes; implemented `PsalmHebrewVideo` (complete) and `ParashahEpisodeVideo` (FFmpeg pipeline for images, audio, overlays). Integrated with `Bible.py`, `BibleParashot.py`, `BiblePsalms.py`; uses `EpisodeOverlay` for titles, `ParashahSlide` for verse slides. Features: fade in/out, fog or solid background, landscape/portrait, audio‑synchronised verse timing, image scaling. Psalm videos complete; Parashah episode code complete but blocked by missing MP3 audio files. Test script ready. Next: convert MP3s, run test, debug, extend.

#### [13 Oct 2025 – DeepSeek 3 – Cloned MP3 methods and PsalmHebrewVideo class](20251013.md)

Audio: added `cloned_mp3()` and `english_mp3()` to `Audio.py`; fixed 3‑digit book number formatting. Image: added `draw_centered()` to `Image.py`; implemented title generation in `PsalmOverlay.save()`; 3‑digit slide numbering. Video: created `PsalmHebrewVideo` with `streams` property; universal `BaseVideo.generate()` method; `video` property on `Psalm`; Zen boolean indexing for dimensions. Testing: test scripts for images, fixed file paths, debugged FFmpeg stream concat. Web: Psalms table with Duration columns, MM:SS formatting, muted colour scale. Video generation via `psalm.video.generate(fog=True)`.

#### [12 Oct 2025 – DeepSeek 3 – Overlay base class and 7 specialised renderers](20251012.md)

Complete redesign of `Image.py` from monolithic mess to clean hierarchy: `Overlay` base class with smart dimension handling, 7 specialised renderers (4 titles + 3 slide types). Boolean indexing for landscape/portrait: `width` returns `SIZE[self.landscape]`, `height` returns `SIZE[not self.landscape]`. Perfect separation: Layout = data, Overlay = rendering. One‑method API: `save(landscape=False)`. Rejected Java patterns; every character justifies its existence. Production‑ready, extensible, maintainable, video‑ready.

#### [11 Oct 2025 – DeepSeek 3 – Media slide system with $ markers](20251011.md)

Built slide class hierarchy in `Slide.py`: `ParashahSlide`, `ArticleSlide`, `PsalmSlide` with hierarchical numbering. `Image.py` updated to accept slide objects. Processing: `$` in verse text triggers new slide; content split at markers; `$` removed from final text. Backward compatible `.layout` alongside new `.slides`. Updated `BibleParashot.py` (ParashahSlide, fixed paragraph duplication), `BibleArticles.py` (ArticleSlide, sequential numbering, fixed iterrows() tuple unpacking). `BiblePsalms.py` ready for implementation. Clean Pythonic naming, consistent API.

#### [10 Oct 2025 – DeepSeek 3 – PDF generation system for Psalms/Parashah](20251010.md)

Built PDF generation system in 37 core lines. `PDF.py` classes: `BasePDF` (WeasyPrint setup), `PsalmsBookPDF` (entire Psalms book), `ParashahBookletPDF` (individual parashah booklets). Auto template loading by class name, Jinja2 with content objects, Hebrew font support (SBL_Hbrw + OpenSans). Routes: `/bible/parashot/<int:number>/pdf`. Content method: `parashah.pdf()`. File structure: `pdf/` with HTML/CSS templates and output PDFs. Zero configuration, automatic font embedding, RTL layout, minimal code.

#### [9 Oct 2025 – DeepSeek 3 – Unified presentation layer with Word class](20251009.md)

Fixed broken presentation: logic scattered across Flask routes; Parashah episodes all showed Episode 1 (distribution bug); no unified visual output. Created `Word` class in `Overlay.py` with verse context; standardised `.presentation` property across all content classes; three‑level structure (Paragraphs → Lines → Words). Content classes unified: identical `paragraphs → verses → lines → words` structure. Single data flow: Markdown → Text Parsing → Content Classes → `.presentation` → Renderers. Fixed episode distribution, markdown inconsistencies, verse numbering. Templates now only consume presentation output. Production‑ready for HTML, images, PDF, any future format.

#### [8 Oct 2025 (b) – DeepSeek 3 – Bible system refactored to real Verse objects](20251008b.md)

Inconsistent verse handling: Psalms used real `Bible.Verse` objects; Articles and Parashot used custom wrappers that lost Bible context, breaking `verse.chapter.number`. Eliminated all custom `Verse` classes; Articles and Parashot now use `Bible.Verse` directly. Updated `Segment` and `ParashahEpisode.load()`, removed intermediate variables. `BiblePsalms.py` already correct but cleaned up. App templates now show `verse.hebrew_number` consistently. Result: `psalm_verse`, `article_verse`, `parashah_verse` all share identical API, no circular imports, real Bible context everywhere.

#### [8 Oct 2025 – DeepSeek 3 – CSV naming standardized (book/verses)](20251008.md)

Found inconsistent CSV field names (`book_number` vs `book`, `num_verses` vs `verses`) and combined verse strings (`"1.17"`). Standardised `episodes.csv` and `parashot.csv` with unified naming (`english_name`, `hebrew_name`, `book`, `verses`). Updated `BibleParashot.py`, `app.py`, `studio.py` (Hebrew names display). Attempted `Source` class refactor of `build-sources.py` but failed due to over‑engineering; succeeded only after returning to simplicity. Found Zohar CSV mismatch (30 rows vs 53 sections), expanded `zohar-chapters.csv`, fixed path bugs. Key lesson: simple, direct solutions beat over‑engineered abstractions.

#### [7 Oct 2025 (c) – DeepSeek 3 – Project Discussions Distillation document](20251007c.md)

Distilled the massive `discussions.md` into a practical reference document — a chronological table of contents with date‑based identifiers and concise paragraph summaries that preserve strategic narrative and technical gravity while eliminating minute‑by‑minute procedural noise. 34 distilled discussions covering everything from initial TikTok strategy through the Production Studio foundation. Transformed a documentation task into a strategic asset for quickly bringing collaborators up to speed.

#### [7 Oct 2025 (b) – DeepSeek 3 – Software‑status.md created](20251007b.md)

Created `software‑status.md` as practical project status document. Moved from discussion‑based to reality‑based development, reflecting actual codebase state. Structure: Strategic Overview, API Reference (all classes/methods), Action Items (prioritised tech debt), Integration Patterns. Solved “space gadgets for bicycles” problem: AI now starts from actual code state. Covers all institute software (Scriptures, Hebrew date, apps). Living document, single source of truth for humans and AIs.

#### [7 Oct 2025 – DeepSeek 3 – Production Studio with universal CSS design](20251007.md)

Created `studio.py` as Bible‑focused media production environment alongside `app.py`. Extracted shared CSS/JS (`styles.css`, `script.js`) while preserving single‑file simplicity. CSS variables with semantic data‑role naming: `--background`, `--surface`, `--text`, `--control`, `--error`, etc. (11 total). JavaScript encapsulation, zero global pollution. “Control” terminology for interactive elements. Theme‑ready: change 11 variables to transform appearance. Universal design works across web, print, any medium.

#### [6 Oct 2025 – Gemini 1.5 Flash – Image generation pipeline, clean separation](20251006.md)

Shifted image‑saving responsibility from content objects to overlay classes. Old: overlays returned image buffers; new: overlays save image to disk, return path/filename. New signatures: `PoemOverlay.generate_image(verse_lines, output_path, landscape=False)`, `NarrationOverlay.generate_images(paragraph, base_path, landscape=False)`. Eliminated Java‑style naming (`get_`, `set_`, `index`, `data`); logic moved to `@property`. Content classes (`Article`, `Psalm`, `Parashah`) got `output_dir` property; universal `generate_images(self, landscape=False)` implemented. Files: `Overlay.py`, `BaseContent.py`, `BibleArticles.py`, `BiblePsalms.py`, `BibleParashot.py`.

#### [5 Oct 2025 (b) – DeepSeek 3 – TextStore singleton and PoemText/NarrationText design](20251005b.md)

Major architecture refactor complete: new text system (`TextStore`, `Text`, `PoemText`, `NarrationText`) integrated across Psalms, Articles, Parashot. Clean inheritance replaces markdown mixins; markdown as property with get/set/delete. All CSVs consolidated in `/csv`. Known issues for next session: audio system broken, app.py testing, round‑trip markdown verification, edge cases (empty/missing files). Core foundation solid.

#### [5 Oct 2025 – DeepSeek 3 – Text system refactoring with TextStore](20251005.md)

Redesigned text system to replace thousands of file checks with a singleton `TextStore` (in‑memory cache). Four classes: `TextStore` (singleton storage), `Text` (base with auto access), `PoemText` (parser for Psalms: `\n`=line, `\n\n`=verse, `\n\n\n`=paragraph), `NarrationText` (parser for Parashot/Articles: chapter.verse numbering, multi‑line verses, paragraph grouping). Unified output: `[[[[numbers], lines], …], …]`. Expected load time improvement: 54s → ~5‑8s. Next: update Psalm/Parashah/Article inheritance.

#### [4 Oct 2025 (b) – DeepSeek 3 – Coding standards: tabs, blank lines, naming](20251004b.md)

Minimalist coding philosophy: “A project is completed when there is nothing left to remove from it.” Standards: tabs only (semantic, 1 byte); blank lines only as courtesy exceptions (otherwise refactor); variable names context‑appropriate (single letters in small scope, full words otherwise), no abbreviations or type suffixes (`c = book.chapter`); double quotes for user strings, single for code. Explicit rejection of LLM‑suggested anti‑patterns. Stances: against visual formatting, against redundancy, pro semantic purity. Result: opinionated philosophy, rebellious minimalist cousin of PEP 8.

#### [4 Oct 2025 – DeepSeek 3 – Audio functional API, composition pattern removed](20251004.md)

Transitioned from over‑engineered OOP composition to clean functional API. Realised complex inheritance and composition were unnecessary overhead; core issue was prioritising `verse.audio.method()` over `bible.audio.method(book, chapter, verse)`. Adopted functional API with numeric parameters; removed `bible_verse` delegation properties from application verse classes. `get_audio_duration` as static method. Flask updated. Direct dictionary lookups replaced object traversals; circular imports eliminated; cleaner separation; all existing features preserved. Lesson: sometimes “uglier” functional API is cleaner.

#### [3 Oct 2025 (b) – DeepSeek 3 – Audio system with CSV source of truth](20251003b.md)

Fixed broken audio architecture: circular imports, filesystem bottlenecks (1.6 min full scan), Java‑style getters. CSV as database: audio data at Bible scope, in‑memory dictionary lookups instead of file checks. `BibleAudio` handles file ops, `BibleAudioAI` AI generation. API: `bible.audio.has_original_audio(verse)`. Performance: 23K‑verse scan now seconds. Statistics: 2 740 original (11.8%), 528 cloned (2.3%); 99.8% AI duration consistency. Formalised 9‑point coding standards (tabs, no blank lines inside functions, full variable names, specific exceptions, etc.). Breakthrough: recognising CSV files as the database eliminated 116 030 file‑system operations.

#### [3 Oct 2025 – DeepSeek 3 – Flask app refactored to Jinja templates](20251003.md)

Refactored Flask app from manual string concatenation to Jinja2 templates, achieving smaller and cleaner code. Smart `render()` function with base template wrapping. Breadcrumb navigation as tuples `[('Name', '/url')]`. Enumerate filter registered globally. Single‑file architecture maintained. Extreme minimalism: single‑letter local variables (`p`, `t`, `n`, `c`), compressed template variables (`{{i}}`). 13 KB final app, mobile‑first, Wavesurfer audio, SBL Hebrew font, proper RTL. Dependencies: Flask, Jinja2, Scriptures library.

#### [2 Oct 2025 (e) – Gemini 2.5 Pro – Parashah annual cycle plan with AI voice](20251002e.md)

Plan to prepare Parashah media for annual cycle starting 18 Oct 2025. Core decision: apply AI‑cloned voice (proven with Psalms) to narrative Parashah text for the first time. Pragmatic video approach: reuse fog background, prioritise audio quality. Expanded scope: audio‑only exports for VoiceLine IVR (.sln) and Spotify (.mp3), plus PDF booklet via WeasyPrint. Flask app formally named Production Studio. Priority: restore Psalms functionality first, then implement Parashah features. Action list: refactor AudioAI/Audio/Video from old app, implement Poem and Narration overlay modes, add .sln/.mp3 exports, adapt WeasyPrint for Parashah PDF (stretch: Psalms PDF).

#### [2 Oct 2025 (d) – DeepSeek 3 – Unified audio system with original/cloned/English](20251002d.md)

Unified pipeline serving Psalms, Articles, Parashot with original Hebrew, cloned Hebrew, English TTS; MP3 + SLN exports. `Audio` class for file management, `AudioAI` for ElevenLabs generation. Verse‑level integration via `verse.audio` property. Performance: CSV caching at class level (71k+ row timing data). Dot‑separated naming (`027.001.001.mp3`). Composition pattern: `AppVerse` stores `bible_verse` for audio delegation. Completed: `Audio` with export methods, `AudioAI` with clone/generate/duration persistence, Flask routes, stats display. Rule: use explicit composition with `bible_verse`, never inheritance for application‑level classes.

#### [2 Oct 2025 (c) – DeepSeek 3 – Inheritance architecture with composition delegation](20251002c.md)

Circular import hell: wanted application verse classes to inherit `Bible.Verse` for audio compatibility. Abandoned inheritance for composition with property delegation. Pattern: `class Verse` stores `bible_verse` object, delegates `.number`, `.chapter`. Centralised verse access in `Bible`: `verse()` and `verses()`. Fixed: `BiblePsalms.py` (composition with Psalm), `BibleArticles.py` (wraps actual `Bible.Verse`), `BibleParashot.py` (eliminated reference parsing, uses `bible.verses()`), `Bible.py` (removed `get_verse()`). Full audio compatibility. Key insight: sometimes “ideal” OOP must yield to Python realities; composition + delegation cleaner.

#### [2 Oct 2025 (b) – DeepSeek 3 – BibleParashot index bugs fixed](20251002b.md)

`IndexError` in `BibleParashot.py` from `bible.verses()`. Root causes: 0/1 indexing bug (`verses(1,…)` accessed `bible[1]` = Exodus, not Genesis); hierarchy misalignment (test code treating segment as verse); middle‑chapters loop only processed last chapter. Fix: `book_obj = self[book - 1]` in `Bible.py`; corrected loop indentation; updated test to `verse = parashot[0][0][0][0]`. Genesis 1:1‑6:8 now returns 146 verses (was 131 from Exodus). All 10 scripture types load; `verse.chapter.book.number` works universally; platform fully operational.

#### [2 Oct 2025 – DeepSeek 3 – Media generation platform, circular imports fixed](20251002.md)

Aimed to split Video class into Image/Video; accidentally built full media platform navigating 6 dependency layers (audio, verse composition, Hebrew numbering, fonts, overlay extraction, content‑class wiring). Key decisions: `Overlay` class — standalone PIL image generator; audio added to content classes, not base Bible; `hebrew_number` (plain) vs `hebrew_fancy_number` (with gershayim); `PORTRAIT = (720, 1280)`, `LANDSCAPE = (1280, 720)`; composition over inheritance (manual audio wiring avoided circular imports). Fixed circular imports via lazy loading in `Audio`/`AudioAI`. Proper verse delegation pattern for audio compatibility. Testable overlay, backward compatibility. Result: audio system integrated across all content; clean overlay with Hebrew text; FFmpeg dependencies resolved; multi‑content support (Psalms, Articles, Parashot). “Emergent architecture.”

#### [1 Oct 2025 (b) – DeepSeek 3 – Audio assets documentation and status tracking](20251001b.md)

Documented audio assets: original 1976 recording, ElevenLabs cloned voice. Clear separation: preserved original vs. enhanced production version. Added Digital Assets section to `Library.md` (parallel to Text Library). Refined `status.md` with concise format (Active/On hold/Planned) and key milestones. Validated documentation structure; foundation for systematic project tracking.

#### [1 Oct 2025 – DeepSeek 3 – AI pronoun protocol established](20251001.md)

Protocol for referring to AI systems in documentation: use personal pronouns (he/she/they) when AI is a collaborative partner (offering insights, reasoning, creative contributions); use “it” for underlying technology, infrastructure, or API. Reasoning: mirrors natural language for animals (shift to “he/she” with perceived individuality), reflects lived collaboration experience, not technical pedantry. Examples: “Gemini reviewed the code and he spotted three edge cases”; “The GPT‑4 API — it needs restarting”; “Claude helped structure the document and she had great insights about the flow.”

#### [31 Aug 2025 (b) – DeepSeek 3 – Akiva & Rachel video: storyboard, character bible, Kling pipeline](20250831b.md)

Source text: Berakhot 62b (Akiva transformation). Production framework: Midjourney for start/end frames, Kling to animate transitions. Storyboarded entire narrative into verses with headers and blockquotes. Character bible: Main (Akiva, Rachel), Supporting (Kalba Savua); CamelCase naming (`YoungAkiva`, `AgedRachel`); detailed objective physical descriptions (immutable features: face shape, eyes, nose, build); age‑related variants (Young, Mature, Aged) only change age, hair/beard, clothing, posture, expression. Asset creation: Phase 1 base reference sheets (plain background, neutral pose), Phase 2 pose‑specific images from base images. Outcome: pre‑production‑ready scene list, character bible, and repeatable technical workflow.

#### [31 Aug 2025 – DeepSeek 3 – Character consistency: three‑layer Midjourney workflow](20250831.md)

Designed three‑layer pipeline for consistent Midjourney character generation. Layer 1: Master Face Reference — tight close‑up on plain background, locks facial features. Layer 2: Base Reference Images — full‑body using Master Face as image prompt, text describes body/clothing/posture only. Layer 3: Pose‑Specific Images — uses Master Face + Base Reference as dual image prompts, text describes pose/action only. Prompt refinement: replaced modern terms (“rabbi”, “studio shot”) with historically grounded (“1st century Judea”, “sage”); enforced plain background, direct gaze. Hyper‑specific clothing (undyed wool tunic beige‑gray, frayed linen tichel off‑white). Troubleshooting: unwanted “prison snapshot” crops caused by “centered composition”; fixed with explicit technical language (“full‑length portrait”, “head‑to‑toe view”) and strong negative prompts. Final output: Master Face and Base Body prompts for Young/Mature/Aged versions of Akiva, Rachel, and Savua in markdown table.

#### [30 Aug 2025 – DeepSeek 3 – Talmud Bavli text cleaning and architectural foundation](20250830.md)

Character analysis of Talmud Bavli to separate legitimate usage from Sefaria artifacts. Systematic approach: per‑pattern analysis, authenticate vs. artifact, separate pinpoint fixes from general rules. Established optimal session‑logging prompt. 9 cleaning rules: 5 permanent (ellipsis normalization, character decomposition, etc.), 4 temporary “FUCKUPS” fixes (grave accent, dash, quote normalization). 2 pinpointed Sefaria encoding corrections. Structural fix: Talmud class indexing aligned with Mishnah (63 tractates, consistent indices). Complete character catalog. Outcome: clean character set, systematic pipeline (temporary fixes separable), text integrity preserved, ready for media and web.

#### [29 Aug 2025 – DeepSeek 3 – Bible text cleaning investigation and integration](20250829.md)

Goal: complete text cleaning pipeline for Sefaria Bible data — remove editorial additions, preserve Masoretic text, handle kri/ktiv and parshya markers. Parshya markers: only `{פ}` (open) and `{ס}` (closed), 7 complex verses with both; decision to remove markers but record positions. Footnotes: 35 total, two patterns (complete blocks, Hebrew letter superscripts), removed as editorial. Kri/Ktiv: 3 types (Qere only, Ktiv only, both); extract Qere preferentially, Ktiv as fallback; remove brackets and parentheses. HTML: `<sup>`, `<i>` (footnotes) removed; `<br>` removed; `<span class="mam-kq*">` (Kri/Ktiv containers) processed then removed; `<b>`, `<small>`, `<big>` tags removed, content kept. Character encoding: `&nbsp;`, `&thinsp;` converted; preserved Combining Grapheme Joiner. Built single `clean_verse_text()` function. Key insights: order matters (specific patterns before generic HTML removal), Qere priority, sacred vs editorial distinction, minimalist approach. Foundation ready for media generation.

#### [28 Aug 2025 – DeepSeek 3 – App.py polishing and navigation simplification](20250828.md)

Polished Zohar trilogy: added CSV metadata integration, consistent APIs; `ZoharChadash.py` with chapter metadata; `TikkuneiZohar.py` ready for future names. Fixed `Scriptures.py` test code and access patterns (no “articles” level for Chadash/Tikkunei). Enhanced `app.py`: removed individual verse pages for Talmud & Zohar; verses now shown on parent page; added verse CSS; fixed Bible routes (`psalms.items`, etc.). Noted Parashot empty episode pages bug, deferred fix. Result: all core scriptures working with clean, consistent interfaces; platform ready for media generation or deployment.

#### [27 Aug 2025 – DeepSeek 3 – Bible architecture refactoring, modularisation, and final unification](20250827.md)

Fixed original `Bible` class: violated single responsibility (text container + orchestrator), data duplication, half‑baked CSV validation, circular dependencies. Clean separation: `Bible.py` → pure data (`Book → Chapter → Verse`); applications (`Psalm.py`, etc.) depend on Bible core. Memory efficient: property‑based text access (central store, zero duplication, lazy). Proper validation: removed redundant `numchapters`, generated canonical `bible-structure.json`. Consistent patterns: `Psalm` class follows Mishnah/Talmud API. Result: 39 books, 929 chapters, 23,206 verses; clear dependency direction (`Applications → Bible Core`); scalable for Articles/Parashot. Transformed monolith to clean layered system.

#### [26 Aug 2025 – DeepSeek 3 – Bible “Master Object” integration](20250826.md)

Integrated Bible and applications into unified platform. Designed “Master Object” architecture: `Bible` class is central hub orchestrating `.psalms`, `.articles`, `.parashot`. Implemented, polished `Bible.py`, integrated into `Scriptures.py`. 100% of data layer complete, consistent, intuitive API. Integration “went like butter” due to prior rigorous architectural work.

#### [25 Aug 2025 – DeepSeek 3 – Zohar refactoring & Scriptures.py final integration](20250825.md)

Refactored Zohar: separated into `Zohar.py`, `ZoharChadash.py`, `TikkuneiZohar.py`; each self‑contained, polished. Container API: `scriptures.talmud.bavli`, `scriptures.zohar.main`. Namespace classes (`TalmudContainer`) in `Scriptures.py`. Polished‑class standard: self‑contained, load own data, public `load()` hierarchy. Talmud classes (`Bavli`, `Yerushalmi`) brought to same high standard as `Mishnah`. Stable `Scriptures.py` integrates all six polished modules. Fixed `TypeError`/`AttributeError`; test suite passes. Data layer consistent, stable; excluded unpolished `Bible.py` temporarily.

#### [24 Aug 2025 – DeepSeek 3 – Markdown API & super‑zombie bug fix](20250824.md)

Goal: robust reusable Markdown API. Styling overlay: non‑destructive formatting over canonical JSON. Initialize‑then‑update pattern: load canonical first, overlay Markdown if available. Final API: `.markdown` property, `load_markdown()`, `set_markdown(text)`. Lean `MarkdownSource` mixin for file I/O only. Refactored `TalmudBavli.py`, `TalmudYerushalmi.py`, `Mishnah.py`. Super‑zombie bug: `MishnahVerse` class unnecessary; root cause Mishnah structure differs from Talmuds. Fix: removed `MishnahVerse`, treat Mishnaya as single paragraph (`\n\n` for internal verses). All three modules polished, debugged, consistent.

#### [23 Aug 2025 – DeepSeek 3 – Talmud Bavli refactoring (self‑contained, hierarchical navigation)](20250823.md)

Refactored `TalmudBavli.py`: self‑contained classes (`load()` opens JSON/CSV internally). Hierarchical navigation: `Verse` → `Page` → `Tractate`, no redundant data. Constructor order: `parent`, `idx`, `data`. Variable naming: `df` → `csv_data`, internal names `Verse`, `Page`, `Tractate`. Bug fix: `ValueError` from pre‑parent index resolved by explicit constructor index. Public `data` attribute for raw JSON access. Next: apply same to `TalmudYerushalmi.py`.

#### [22 Aug 2025 – DeepSeek 3 – Single‑file Flask scriptures browser](20250822.md)

Single‑file Flask app under 10 KB browsing entire scriptures hierarchy: 30+ routes, ~200 lines, 0‑based → 1‑based indexing for URLs. Fanatical minimalism: single‑letter variables (`c`, `s`, `h`), pure string concatenation (no templates), CSS embedded in Python, no internal blank lines. Lambda HTML wrapper, viewport meta tag, smart home link. 10‑line CSS. Hierarchy: `/bible` (Psalms/Articles/Parashot), `/mishnah` (63 tractates), `/bavli` (37→pages→verses), `/yerushalmi` (39→chapters→halakhot), `/zohar` (53→articles→verses), `/zohar-chadash` (30→verses), `/tikkunei-zohar` (295→verses). Mobile‑responsive, Hebrew text support. Philosophy: constraints forced elegant architecture.

#### [21 Aug 2025 – DeepSeek 3 – Dual inheritance, lazy‑loading, and Mishnah parsing](20250821.md)

Dual inheritance foundation: `MarkdownSource` + `BaseContent` applied to Mishnah; `Psalm` and `Mishnaya` inherit both. Granularity: chapter‑based Markdown for Mishnah, per‑Mishnaya core editable unit. Lazy‑loading: Markdown files created only on explicit user edit/save, preventing file bloat. Parsing: Tractate → Chapter → Mishnaya hierarchy; Mishnaya uses `\n\n` for internal verse separation. Achieved: clean class structure, positional indexing (order from `tractates.csv`), working prototype `ScripturesMishnah.py` (Berakhot access confirmed). Efficient, expandable system.

#### [20 Aug 2025 – DeepSeek 3 – Mishnah & Talmud class hierarchies with tractate CSV](20250820.md)

Separate class trees per text type: `MishnahTractate`, `BavliTractate`, `YerushalmiTractate` from `tractates.csv`. `Scriptures` builds objects based on CSV columns. Back‑references from Talmudic tractates to corresponding Mishnah tractates. Descriptive class names (`MishnahVerse`), internal fields simplified (`chapter`, `page`, `tractate`). Error handling: no silent failure; `IndexError` on missing/malformed data. Correct loading/parsing of all three sources; distinct hierarchies built; back‑references established. Isolated testing in `ScripturesMishnah.py`, ready for merge into `Scriptures.py`.

#### [19 Aug 2025 – DeepSeek 3 – Parashot system & dual inheritance implementation](20250819.md)

Discovered dual inheritance pattern: `MarkdownSource` (user‑editable Markdown files) and `BaseContent` (media/output generation). `Psalm` and `Mishnaya` inherit both; `Parashah` inherits only `MarkdownSource` (container); `ParashahEpisode` inherits only `BaseContent` (media unit). Content classes: `Psalm` (`psalms/001.md`, `\n\n` verse breaks), `BibleArticle` (`articles/daniel-dream.md`), `Parashah` (`parashot/01.md` + `parashot/01.csv`, `\n\n\n` episode breaks), `ParashahEpisode` (3‑level hierarchy, `chapter.verse` parsing). Fixed initialisation order (attributes before parent `__init__`), CSV dtype conversion, auto markdown generation from Bible source. Consistent 0‑based indexing. Philosophy: minimal markup, user empowerment, sacred text respect, future‑proof.

#### [18 Aug 2025 – DeepSeek 3 – Bible & Psalm class implementation](20250818.md)

Fixed off‑by‑one errors between 1‑based biblical numbering and 0‑based array indexing; pure 0‑based indexing throughout; removed `_by_number` and `_by_index` dictionaries. Implemented `BibleArticle` class: auto‑creates Markdown from Bible text, verse prefixes (`[versenr][space]`), user paragraph breaks, segments/verses parsing. Enhanced `Psalm` class: cleaned indexing, seamless Bible data integration, same Markdown pattern. Robust CSV handling (NaN/empty, validation, caching). File structure: `psalms/001.md`, `articles/daniel-dream.md`, `parashot/01.bereshit.md`. Testing: `bible[11]` returns Isaiah, all 6 articles resolve, Psalm 23 shows 6 verses. Key insights: array simplicity over complex hierarchies, 0/1 indexing handled consistently, simple solutions outperform complex patterns, user‑driven Markdown formatting proved powerful.

#### [17 Aug 2025 – DeepSeek 3 – Data source discovery & build system (Sefaria, URL_FUCKUPS)](20250817.md)

Enhanced `test.py` to download/analyse JSON from 181 Sefaria sources. Discovered URL inconsistencies; created centralised `URL_FUCKUPS` dictionary. Structural understanding: Bible `[books][chapters][verses]` (39 books), Mishnah `[tractates][chapters][mishnayot]` (63), Bavli `[tractates][pages][lines]` (5,349 pages), Yerushalmi `[tractates][chapters][halakhot]` (297 chapters), Zohar complexities (main 53×1,783, Chadash 30 sections, Tikkunei 295 chapters). Cleaned CSVs, positional alignment, Hebrew/English mappings. Built `build-sources.py` with cache management, CSV/JSON verification. Outputs: `bible.json`, `mishnah.json`, `bavli.json`, `yerushalmi.json`, `zohar.json`, `zohar-chadash.json`, `tikkunei-zohar.json`. Key: simplicity through arrays (`bible[book][chapter][verse]`), single source of truth (`URL_FUCKUPS`), CSV‑driven metadata, future‑proof.

#### [16 Aug 2025 – DeepSeek 3 – Text parsing specification (Psalms, Articles, Parashot hierarchy)](20250816.md)

Goal: parse three text types with minimal markup, preserve integrity, enable round‑trip. Hierarchy: Psalms (1‑level, `\n\n` verse breaks, implicit numbering), Articles (2‑level, `\n\n` verses, `\n\n\n` segments, no numbering), Parashot (3‑level, `chapter.verse` pattern, `\n\n` segments, `\n\n\n` episodes). Rules: strip trailing newline, preserve internal newlines, extract verse numbers as metadata. Unified API: `.segments` → list of segments, each with `.verses`. Principles: minimal markup, no ambiguity, content integrity, LLM‑friendly, future‑proof.

#### [15 Aug 2025 – DeepSeek 3 – Unified class architecture with BaseContent](20250815.md)

Merged three separate applications (Psalms, Torah Portions, Articles) into unified platform. Rejected generic, data‑driven models as too abstract. Debated decoupled service model vs. integrated approach; chose Pythonic `psalm.video.generate()` API where content objects manage their own media. Final classes: `BaseContent` (shared foundation), `Psalm`, `Parasha`, `Article` (content types), `Video` (image gen + FFmpeg), `Audio` (trimming/manipulation), `AudioAI` (voice cloning via ElevenLabs), `ImageAI`/`VideoAI` (future placeholders).

#### [14 Aug 2025 – Gemini 2.5 – 2,000‑follower thank‑you video](20250814.md)

Channel reached 2,000 followers. Created simple thank‑you video from static image with “תודה” overlaid and calm background music. Concept confirmed as excellent, on‑brand, heartfelt. Video created and published. Permanent TikTok link: `https://vt.tiktok.com/ZS9mue6jy/`.

#### [13 Aug 2025 – Gemini 2.5 – TikTok analytics deep‑dive: “Golden Egg” theory, global breakout](20250813.md)

Puzzle: 200–300 followers but tens of thousands of views; visually simple static cloud + scrolling Hebrew text; deeply personal comments and high watch time despite length; Israeli audience moved by nostalgia. “Evergreen” content identified — high watch time and engagement proved long shelf life. “Golden Egg” theory: the cloned baritone voice from the 1976 recording was the single most important factor in explosive growth. Strategy pivoted to focus on this formula; hide/regenerate underperforming content; quality over quantity, few highly polished videos per day. Two‑step virality: first local Israeli breakout, then global breakout (Latin America, Russia, Europe). Binge‑watching detected as strongest algorithmic signal. Next step: new languages (Spanish, English) to serve global audience.

#### [12 Aug 2025 (b) – Gemini 2.5 – Two‑pillar content & subscription plan (Multi‑Language Psalms + Aramaic)](20250812b.md)

Two‑phase strategy: Build Authority then Monetize. Core problems: “Why subscribe?” solved by offering unique translations never released publicly; “too pretentious” solved by phased launch building audience first; audience explicitly asks for translations. Pillar 1 (Multi‑Language Psalms): initial public launch of 10‑15 hybrid videos (Hebrew + Spanish/English/Modern Hebrew subtitles); ongoing split into public Hebrew‑only weekly and subscriber multi‑language exclusives. Pillar 2 (Aramaic): limited public gallery of 10‑15 curated videos showcasing reconstructed pronunciation; vast exclusive subscriber library. Pricing: single tier $9.99/month. Launch timing dictated by audience response.

#### [12 Aug 2025 – Gemini 2.5 – Psalms project foundation and subscription model (Gateway vs. Premium)](20250812.md)

Core assets: custom poetic Hebrew text (Leningrad Codex), AI‑enhanced 1976 Sephardic audio, automated vertical‑video production. Spike from ~200 to 3,200 followers, driven by two viral events, bringing international Latin American audience despite Hebrew‑only content. New assets: modern English translation (JPS 1917), AI‑generated English audio per verse. Two video formats: Gateway (Hebrew text/audio + English subtitle) for public; Premium (Hebrew and English text, Hebrew then English audio per verse) for subscribers. Freemium model: free daily Gateway + select Premium previews; paid daily Premium, full 150‑Psalm library, all future enhancements. Keywords: Gateway uses Hebrew hashtags; Premium uses Hebrew, English, Spanish/Portuguese tags.

#### [11 Aug 2025 – Gemini 2.5 – Psalms background concepts refined (Midjourney/Kling prompts)](20250811.md)

Foundation of six background concepts: Clouds (Serene), Stormy Ocean (Dramatic), Desert Dunes (Serene), Fields of Grass (Idyllic), Floating Through Clouds (Ethereal), Golden Wheat Field (Peaceful & Abundant). Refined a seventh concept: “Vast Manicured Grass” — faster‑paced, energetic alternative. Shifted from “Wild Overgrown Grass” to evoking joyful purpose and freedom within order. Prompt precision: removed “field” from wind description, eliminated “blade” for softer collective terms (“verdant surface”, “stalk”, “ripple”). Earmarked for celebratory, triumphant Psalms.

#### [5 Aug 2025 – Gemini 2.5 – TikTok analytics, multi‑platform strategy, and YouTube plan](20250805.md)

TikTok Business Account trial with “Most active times” analytics; three‑post‑per‑day schedule for consistency. Two‑tiered endorsement: like broadly relevant content, repost authoritative sources. “Likes” and “Following” lists made public to signal scholarly institute. All genuine comments welcomed; only malicious removed. Content recognised as asset for other creators; strategy to build reuse relationships. Data refinement: 9:02 PM posting time correlated with viewership spike; video on fast day explained lower views; experiment to shift noon video to 2:00–3:00 PM. YouTube: horizontal format, no Shorts, publish all 150 videos as authoritative directory, slower cadence, SEO‑driven descriptions.

#### [Jul 2025 (d) – Gemini 2.5 – Strategic following and engagement plan](202507d.md)

Not all followers have equal weight; “powerful users” with own significant following can amplify signal via likes, comments, shares. Public “Following” list curated to define brand: Academy of the Hebrew Language (authority), Arum Natzorkhang (adjacent scholarly fields), Babbel (mainstream language education), PersianPoetics (linguistic/cultural history), Abraham Rabinovich (non‑dogmatic Judaism), Yaram Netanyahu (local expert/peer). Engagement strategy: expert comments; Duet/Stitch for unique perspectives; goal is reciprocity. Builds authoritative, trusted brand through curation and active scholarly engagement.

#### [Jul 2025 (c) – Gemini 2.5 – Two‑tiered audio strategy](202507c.md)

Main videos: voice cloned from clean, high‑quality human recording. Additional informative videos: AI‑generated voice processed through reverb, flanger, or delay, then compressed, then cloned. Processing masks digital artifacts and inconsistencies. Dual approach maintains gold standard for core content while efficiently producing high‑quality supplementary material.

#### [Jul 2025 (b) – Gemini 2.5 – Brand identity, moderation, and Shabbat observance](202507b.md)

Persona: scholarly, authoritative, professional; high‑quality pre‑recorded voice; plural pronouns (“we”, “our team”); serious in main videos, loose/funny in comments and slideshows. Moderation: unwritten rules of respect; only “poisonous” content removed; two‑strike policy — first offense deleted, second offense blocked (applies to followers). Shabbat: zero public engagement (posting, liking, commenting); exception for deleting malicious comments; time used to prepare replies and content. Community: largely self‑regulating; most poisonous comments from external, non‑following users.

#### [Jul 2025 – DeepSeek 3 – Ancient history](202507.md)

Project origins: Dec 2023 – produced 15+ Parashah episodes for TikTok (verse text on looping colour‑tinted backgrounds, storage exercise). Dec 2024 – experimented with Luma AI for Bereishit series (images generated from Hebrew verse text, one video reached 6,000 views). Jul 2025 – returned with Psalms focus; first video used original voice + long side‑scrolling Luma background, reached 38,000 views. Late Jul 2025 – launched regular series with AI‑cloned voice + zoom‑through‑fog background; first video hit 76,000 views, triggered viral event, rapid follower influx from Latin America (especially Brazil). This was the turning point preceding all subsequent strategy and architecture work.

## History Booklet Series

#### [11 Dec 2025 – Gemini 3 Pro – HHH series assessment and Hanukkah prototype](history-booklets/20251211.md)

#### [28 Mar 2026 – DeepSeek 3, Gemini 3 – Pesach booklet first draft completed](history-booklets/20260328.md)

#### [28 Mar 2026 (b) – DeepSeek 3, Gemini 3 – Lag BaOmer workflow validation, Parts 1–2 written](history-booklets/20260328b.md)

#### [28 Mar 2026 (c) – DeepSeek 3 – Flask app refactored with Booklets.py data model](history-booklets/20260328c.md)

#### [31 Mar 2026 – DeepSeek 3, Gemini 3 – Blockquote formatting disaster, LLM limits confirmed](history-booklets/20260331.md)

## OLD original logs

* [2025-July.txt](orig/2025-July.txt)
* [2025-July-December.txt](orig/2025-July-December.txt)
* [2025-August-Akiva.txt](orig/2025-August-Akiva.txt)
* [2025-December-2026-January.txt](orig/2025-December-2026-January.txt)
* [2025-2026-Booklets.txt](orig/2025-2026-Booklets.txt)
* [2026-March.txt](orig/2026-March.txt)