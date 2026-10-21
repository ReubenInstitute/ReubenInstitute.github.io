# Dev Lab Logs

#### [21 Sep 2026 – Claude (Code) Sonnet 5 – Studio becomes MediaStudio](20260921b.md)

We merged the two separate studio apps back into one, gave the whole project a new name, and cleaned up how it is structured. We standardized the typography used in the videos and cover images, added covers for both psalms and parashot, and finished the parashah video generation. We also fixed a long-standing Hebrew text-handling issue that affected how words were laid out and highlighted on screen. Finally, we tracked down the original audio recordings the project's timing data was based on, brought them into the project, and set up automatic conversion so the audio exports work.

#### [21 Sep 2026 – DeepSeek 4.1, Claude (Code) Sonnet 5 – Studio setup: submodules, HTTPS, and the psalm workflow](20260921.md)

We reorganized the project's dependencies as git submodules so they track the latest versions automatically, fixed HTTPS so the browser features work, redesigned the psalm page and its fonts, replaced the old batch-export script with a cleaner tool, and added a live preview so changes to the video styling can be seen without exporting a full video.

#### [20 Sep 2026 – DeepSeek 4.1, Claude (Code) Sonnet 5 – Fonts: fixing the Hebrew font and building a font test page](20260920c.md)

We fixed a series of issues in our custom Hebrew font (mark placement and special letter combinations), reorganized all fonts into a proper repository with correct licensing, produced adjusted versions of the Open Sans Hebrew family, and built a test page for checking how letters and vowel marks render across all fonts.

#### [20 Sep 2026 – DeepSeek 4.1, Claude (Code) Sonnet 5 – Fixing parashah video export](20260920b.md)

We got parashah video export working again after it had been broken, fixed how verses are located and named in multi-chapter portions, corrected output locations and sizes, and made the slide text use the proper Hebrew font.

#### [20 Sep 2026 – DeepSeek 4.1, Claude (Code) Sonnet 5 – Psalm videos: word highlighting and batch export](20260920.md)

We added word-by-word highlighting synchronized to the audio in psalm videos, fixed a long-standing mismatch in how hyphenated Hebrew words were counted, and turned the export process into a proper batch tool that produces all the audio and video variants for a list of psalms.

#### [19 Sep 2026 – DeepSeek 4.1, Claude (Code) Sonnet 5 – Moving everything to GitHub](20260919.md)

We migrated the project's code, audio recordings, and data into organized GitHub repositories, standardized book naming, split shared libraries into their own repos, brought the studio under version control, and cleaned up the local machine.

#### [18 Sep 2026 – DeepSeek 4.1, Claude (Code) Sonnet 5 – HebrewDate Android app: shared code, screens, and widgets](20260918.md)

We reorganized the Android app to share its calendar code with the other projects, built out its main screens, ported the clock display from Python to Java, added free/pro features, and created home-screen widgets.

#### [5 Sep 2026 – DeepSeek 4 Pro, Claude Sonnet 5 – Matching Suno tracks to psalms and fixing descriptions](20260905.md)

We matched the tagged psalm audio files to the original generated tracks by comparing exact durations, organized the psalm schedule and book assignments, and rewrote the psalm descriptions for consistency.

#### [24 Aug 2026 – DeepSeek Expert, Claude Sonnet 5, Gemini 3, Qwen-3.8-Max – Archiving the entire Suno music library before the deadline](20260824.md)

Faced with an upcoming change to Suno's download policy, we built tools to bulk-download all tracks, stems, and images, and a local browser to track what was archived, then verified the whole library was saved.

#### [18 Aug 2026 – DeepSeek 3 Expert, Claude – Daily TikTok video pipeline and a midnight clock bug](20260818.md)

We built the daily TikTok video export, published the first video, fixed a clock bug where the colored time bands disappeared after midnight, and added background music to the videos.

#### [12 Aug 2026 – DeepSeek 3 Expert, Claude, Gemini – Building the full calendar product line](20260812.md)

We designed and built six calendar formats in two languages, restructured the multilingual text system, created an automated PDF production pipeline, extracted product images, and established a rule for handing off tasks when the AI gets stuck.

#### [9 Aug 2026 – Claude Sonnet 5, DeepSeek 3 Expert – Integrating Torah readings into the calendar](20260809.md)

We rewrote the Torah reading code, defined the yearly cycle of portions, added logic for special Shabbatot and holiday readings, and connected it all to the Hebrew date system.

#### [8 Aug 2026 – DeepSeek 3 – Clock rings: moon, observance, and holiday logic](20260808.md)

We added the moon phase ring and the holiday observance ring to the clock, improved the holiday definitions, added striped patterns for fast days, and put digits on the civil clock.

#### [4 Aug 2026 – DeepSeek 3 Expert – Refactoring the clock's time-band system](20260804.md)

We reorganized the clock's internal naming and structure, added the day/night watch ring, and prepared the seasonal hour markings.

#### [3 Aug 2026 – Claude Sonnet 5 – Fixing clock hands and the seam between day and night](20260803.md)

We fixed the Hebrew clock's second hand, resolved a timezone misalignment in the civil clock's bands, and fixed a visual glitch where the bands wrapped around the dial.

#### [2 Aug 2026 – Claude Sonnet 5 – Building the Python clock and display engine](20260802c.md)

We built the clock rendering classes and display system in Python, ported the drawing routines, and got both the civil and Hebrew clocks drawing correctly.

#### [2 Aug 2026 – Claude Sonnet 5 – Porting the astronomy and location code to Python](20260802b.md)

We ported the sun, moon, location, and custom-settings code to Python, completing the engine that calculates the times displayed on the clock.

#### [2 Aug 2026 – Claude Sonnet 5 – Porting the core calendar to Python](20260802.md)

We ported the date, time, Hebrew date, and holiday classes to Python and fixed several bugs discovered along the way.

#### [1 Aug 2026 – DeepSeek 3 Expert – Generating the manual's diagrams and deciding to port to Python](20260801.md)

We produced the diagrams for the user manual, then realized they were based on fake data and decided to port the real calendar engine to Python so future images would be accurate.

#### [30 Jul 2026 – DeepSeek 3 Expert – Choosing the hardware and building the C++ display](20260730b.md)

We researched and selected the hardware platform for the physical clock, designed its Shabbat behavior, and built the display and clock rendering in C++.

#### [30 Jul 2026 – DeepSeek 3 Expert – Translating the calendar library to C++](20260730.md)

We translated the entire calendar library from JavaScript to C++, keeping the same behavior and testing it.

#### [28 Jul 2026 – DeepSeek 3 Expert – Designing the physical clock product](20260728.md)

We defined the physical product line, its hardware, the Shabbat lock behavior, and outlined the user manual.

#### [27 Jul 2026 – DeepSeek 3 Expert – Fixing the Hebrew day boundaries](20260727.md)

We reworked how the Hebrew day is represented, fixed an off-by-one error in the night calculation, and corrected how nightfall is computed for different customs.

#### [26 Jul 2026 – DeepSeek 3 Expert – Live clock page with settings and rings](20260726.md)

We added a settings panel with presets to the live clock page, made it animate in real time, and laid the groundwork for drawing the colored time bands as rings.

#### [25 Jul 2026 – DeepSeek 3 Expert – Designing the clock face and its colored rings](20260725.md)

We polished the clock face, added the halachic time bands, night watches, and moon arc, and conceived the sliding civil-clock design.

#### [24 Jul 2026 – DeepSeek 3 Expert – Porting the calendar library to JavaScript](20260724.md)

We ported the calendar engine from Java to JavaScript and built a live demo page showing clocks and calendars.

#### [19 Jul 2026 – DeepSeek 3 – Restarting the psalm series with a self-sustaining pipeline](20260719.md)

We restarted publishing psalms with a two-week buffer of prepared content, integrated the Tikun Haklali collection, and automated the export so the pipeline runs itself.

#### [18 Jul 2026 – DeepSeek 3 – Reorganizing the codebase and going live with psalms](20260718.md)

We cleaned up and separated the core text libraries, split the studio into two focused apps, and got the psalm production pipeline working end to end.

#### [13 May 2026 – DeepSeek 3 – Defining the product line and validating on TikTok](20260513.md)

We settled on the product naming and tiers, built the public catalogue of psalm releases, and validated the format on TikTok.

#### [12 May 2026 – DeepSeek 3 – Repairing the video pipeline](20260512.md)

We fixed a series of rendering bugs in the video pipeline — text overlays, shadows, transparency, and an unwanted character appearing in the text — and got clean output.

#### [11 May 2026 – DeepSeek 3 – Fixing the psalm cover layout](20260511.md)

We fixed two hidden bugs that were breaking the cover layout and the text measurement, and finalized the cover design.

#### [9 May 2026 (b) – DeepSeek 3 – Restoring audio and extracting the text library](20260509b.md)

We repaired the audio system, fixed audio/video synchronization, and extracted the text handling into a standalone library.

#### [9 May 2026 – DeepSeek 3 – Designing the psalm reading cycles](20260509.md)

We wrote a document defining several structured reading schedules for the psalms.

#### [2 May 2026 – DeepSeek 3 – Reconstructing the project log](20260502.md)

We consolidated a large, messy collection of session notes into a single organized, chronological log and established a format for future entries.

#### [31 Mar 2026 – DeepSeek 3, Gemini 3 – A lesson in LLM limitations](history-booklets/20260331.md)

We spent a very long time trying to get an AI to reformat quotations in a document according to strict rules; it eventually worked but proved that such repetitive formatting should be done with scripts, not AI.

#### [28 Mar 2026 (c) – DeepSeek 3 – Restructuring the booklet app around a data model](history-booklets/20260328c.md)

We separated the booklet content and metadata from the web code, making the app cleaner and easier to maintain.

#### [28 Mar 2026 (b) – DeepSeek 3, Gemini 3 – Writing a second booklet to test the workflow](history-booklets/20260328b.md)

We applied our booklet-writing method to a different holiday and confirmed the approach works generally.

#### [28 Mar 2026 – DeepSeek 3, Gemini 3 – Writing the first full holiday booklet](history-booklets/20260328.md)

We wrote a complete first draft of the Passover booklet, establishing the structure and method for future booklets.

#### [21 Mar 2026 – Gemini 3 Flash – Rewriting the project documentation](20260321.md)

We reorganized the project's documentation into a clear, functional set of reference documents.

#### [19 Mar 2026 – DeepSeek 3 – Rebuilding the media architecture](20260319.md)

We restructured the image, text, and video classes around a shared foundation, making the system more consistent and extensible.

#### [17 Mar 2026 – Gemini 3 Pro – Solving a long-standing audio bug](20260317.md)

We tracked down and fixed a subtle bug in the video assembly caused by identical audio durations, unblocking a feature that had been stuck for months.

#### [16 Mar 2026 (b) – Gemini 3 Pro – Cleaning up the audio code](20260316b.md)

We removed dead and experimental code from the audio module and simplified its structure.

#### [16 Mar 2026 – Gemini 3 Pro – Simplifying the media architecture](20260316.md)

We reworked how audio and video objects are built and exported, moving to a cleaner composition-based design.

#### [15 Mar 2026 – Gemini 3 Pro – Cleaning up audio and standardizing file names](20260315.md)

We removed obsolete audio code, consolidated title generation, and gave all audio files consistent, clear names.

#### [14 Mar 2026 – DeepSeek 3 – Rebuilding the complete Psalms audio library](20260314.md)

We regenerated and organized all the psalm audio — verses, titles, books, and full collections — and built the exports for multiple formats.

#### [4 Mar 2026 – DeepSeek 3 – Visualizing multi-track audio for videos](20260304.md)

We extended the audio visualization system to handle multi-track recordings with separated instruments.

#### [17 Feb 2026 – Gemini 3 Pro – Starting the psalm alignment editor](20260217.md)

We began building a tool for aligning text to audio and added tempo calibration.

#### [13 Feb 2026 – DeepSeek 3 – Establishing the publishing rhythm](20260213.md)

We formalized the daily morning/evening publishing schedule and audited which psalms were still missing from the Tikun Haklali collection.

#### [12 Feb 2026 – DeepSeek 3 – Organizing visual assets and psalm settings](20260212.md)

We assigned each psalm a visual setting and built a system for cataloguing and reusing video clips.

#### [13 Jan 2026 (b) – DeepSeek 3 – Refining the video timeline system](20260113b.md)

We improved the declarative video system so clips play sequentially by default and prepared it for gaps and overlaps.

#### [13 Jan 2026 – DeepSeek 3 – Building a declarative video composition system](20260113.md)

We created a JSON-based system for describing video timelines, allowing videos to be assembled from a single configuration.

#### [11 Jan 2026 – DeepSeek 3 – Planning an Aramaic teaching series](20260111.md)

We developed a plan for short videos teaching Aramaic nouns and refined the visual and audio production approach.

#### [9 Jan 2026 – DeepSeek 3 – Producing a cinematic psalm video](20260109.md)

We built a multi-shot cinematic video for Psalm 8, published it, and saw it generate audience engagement including a user duet.

#### [8 Jan 2026 – Gemini 3 Flash – Creating the asset vault and visual workflow](20260108.md)

We set up a system for tracking and reusing generated images across formats, with a consistent workflow from one master image.

#### [6 Jan 2026 – DeepSeek 3 – Building Aramaic teaching materials](20260106.md)

We created reference tables for Aramaic sounds and designed the visual teaching approach for the course.

#### [5 Jan 2026 (b) – DeepSeek 3 – Designing the Aramaic course](20260105b.md)

We laid out a structured Aramaic language course with a visual teaching method and produced early lessons.

#### [5 Jan 2026 – Gemini 3 Flash – Planning the cinematic journey for Book 1](20260105.md)

We mapped out a multi-day visual journey for the first book of Psalms, assigning each psalm a place and time.

#### [4 Jan 2026 – DeepSeek 3 – Adding one-click description copying](20260104.md)

We added a feature to copy pre-written psalm descriptions to the clipboard with one click.

#### [2 Jan 2026 – DeepSeek 3 – Building a web-based video editor](20260102.md)

We created a browser tool for assembling and previewing video timelines from clips.

#### [30 Dec 2025 – Gemini 3 Flash – Writing the production plan for the cinematic psalm series](20251230.md)

We produced a detailed plan and budget for a large-scale cinematic treatment of the psalms across five thematic environments.

#### [28 Dec 2025 (b) – DeepSeek 3 – Setting the cross-platform publishing strategy](20251228b.md)

We defined how each video version would be distributed across platforms and established a model production cycle.

#### [28 Dec 2025 – DeepSeek 3 – Simplifying the psalm cover design](20251228.md)

We rewrote the cover generator to be simpler and more reliable.

#### [27 Dec 2025 (b) – DeepSeek 3 – Preparing audio for Spotify distribution](20251227b.md)

We chose a distribution method, set the content structure for the podcast, and added proper bilingual metadata to the audio files.

#### [27 Dec 2025 – DeepSeek 3 – Restructuring the audio system](20251227.md)

We separated audio generation from video generation and built a cleaner class structure for producing the different audio versions.

#### [26 Dec 2025 – DeepSeek 3 – Formalizing the daily production workflow](20251226.md)

We took stock of the published content and established a sustainable daily workflow for producing and posting videos.

#### [24 Dec 2025 – DeepSeek 3 – Producing a music video](20251224.md)

We produced a symbolic music video from concept through generated footage, validating the AI-assisted production workflow.

#### [23 Dec 2025 – Gemini 3 Pro – Rebranding and improving video quality](20251223.md)

We updated the brand description and developed a technique for producing smoother, longer background videos.

#### [21 Dec 2025 – DeepSeek 3 – Improving the audio editor and homepage](20251221.md)

We added keyboard shortcuts to the audio editing tool and added production statistics to the homepage.

#### [18 Dec 2025 (b) – Gemini 3 Pro – Switching to full-length parashah videos](20251218b.md)

We decided to produce each weekly portion as a single long video instead of short episodes, and planned how to use expiring AI credits.

#### [18 Dec 2025 – DeepSeek 3 – Reviewing assets and generating background music](20251218.md)

We reviewed the video asset library and set up a system for generating consistent background music.

#### [17 Dec 2025 (b) – DeepSeek 3 – Building the background video library](20251217b.md)

We catalogued the generated background videos with their descriptions and intended uses.

#### [17 Dec 2025 – DeepSeek 3 – Improving text rendering](20251217.md)

We reworked how text is drawn and attempted to fix the shadow effect, cleaning up the rendering code in the process.

#### [14 Dec 2025 – DeepSeek 3 – Finalizing the video pipeline and reviving TikTok](20251214.md)

We settled the background and music style, produced a proof-of-concept video, and saw engagement recover.

#### [13 Dec 2025 – DeepSeek 3 – Reviewing social media strategy](20251213.md)

We assessed the performance of the different series and decided to prioritize catching up on the weekly Torah portions.

#### [11 Dec 2025 – Gemini 3 Pro – Assessing the booklet series and prototyping Hanukkah](history-booklets/20251211.md)

We reviewed the state of the holiday booklet series and developed a prototype structure for the Hanukkah booklet.

#### [3 Nov 2025 – DeepSeek 3 – Building the Hebrew text handling system](20251103.md)

We created a comprehensive database of Hebrew letters and marks and a system for normalizing Hebrew text for correct display.

#### [2 Nov 2025 – DeepSeek 3 – Refactoring the font testing app](20251102.md)

We restructured the Hebrew font testing tool using proper object-oriented design.

#### [20 Oct 2025 (c) – DeepSeek 3 – Building the font metrics system](20251020c.md)

We added accurate font measurement and a complete Hebrew character database to support proper text rendering.

#### [20 Oct 2025 (b) – DeepSeek 3 – Fixing text measurement](20251020b.md)

We fixed a mismatch between how text was measured and how it was drawn, making layout consistent.

#### [20 Oct 2025 – DeepSeek 3 – Completing the media platform](20251020.md)

After a long series of sessions, the media production platform reached a production-ready state.

#### [18 Oct 2025 – DeepSeek 3 – Building the audio player tools](20251018.md)

We created a set of audio player components with editing and marking features and connected them to the web app.

#### [17 Oct 2025 (b) – DeepSeek 3 – Unifying slide generation](20251017b.md)

We brought the different content types onto a single consistent system for generating slides.

#### [17 Oct 2025 – Gemini 2.5 Flash – Adding color coding to the Torah portions](20251017.md)

We assigned colors to the five books of the Torah and added a color column to the portion pages.

#### [16 Oct 2025 – DeepSeek 3 – Refactoring slide generation](20251016.md)

We reworked the slide generation for both psalms and parashot to use a consistent structure.

#### [14 Oct 2025 – DeepSeek 3 – Building video generation](20251014.md)

We created the base video classes and implemented psalm and parashah video generation with audio and overlays.

#### [13 Oct 2025 – DeepSeek 3 – Adding audio export and psalm video](20251013.md)

We added methods for producing the cloned and translated audio, and built the psalm video class.

#### [12 Oct 2025 – DeepSeek 3 – Rebuilding the image overlay system](20251012.md)

We redesigned the image rendering around a clean base class and specialized renderers for each type of slide.

#### [11 Oct 2025 – DeepSeek 3 – Building the slide system](20251011.md)

We created the slide class hierarchy and a simple markup for splitting text across slides.

#### [10 Oct 2025 – DeepSeek 3 – Adding PDF generation](20251010.md)

We built a minimal system for producing PDFs of psalms and parashot.

#### [9 Oct 2025 – DeepSeek 3 – Unifying the presentation layer](20251009.md)

We created a single consistent way to represent and render text content for all formats.

#### [8 Oct 2025 (b) – DeepSeek 3 – Making all content use the same verse objects](20251008b.md)

We eliminated duplicate verse classes so every content type shares the same underlying Bible objects.

#### [8 Oct 2025 – DeepSeek 3 – Standardizing the data files](20251008.md)

We gave the metadata files consistent field names and fixed a related build script.

#### [7 Oct 2025 (c) – DeepSeek 3 – Distilling the project discussions](20251007c.md)

We summarized the long record of project discussions into a concise reference document.

#### [7 Oct 2025 (b) – DeepSeek 3 – Creating a project status document](20251007b.md)

We wrote a document describing the actual current state of the software so collaborators could start from reality.

#### [7 Oct 2025 – DeepSeek 3 – Building the production studio interface](20251007.md)

We created the media production web app with a clean, theme-ready design system.

#### [6 Oct 2025 – Gemini 1.5 Flash – Streamlining image generation](20251006.md)

We reorganized the image generation so each class has a clear responsibility.

#### [5 Oct 2025 (b) – DeepSeek 3 – Redesigning the text system](20251005b.md)

We rebuilt how text is loaded and parsed, with a caching store and dedicated parsers for the different text types.

#### [5 Oct 2025 – DeepSeek 3 – Introducing the text store](20251005.md)

We replaced slow per-file checks with a cached text store, greatly speeding up loading.

#### [4 Oct 2025 (b) – DeepSeek 3 – Establishing coding standards](20251004b.md)

We defined a strict minimalist coding style for the project.

#### [4 Oct 2025 – DeepSeek 3 – Simplifying the audio API](20251004.md)

We replaced an over-engineered object structure with a simpler, more direct functional interface.

#### [3 Oct 2025 (b) – DeepSeek 3 – Using data files as the source of truth](20251003b.md)

We fixed the audio system's performance and structure by treating the data files as the database.

#### [3 Oct 2025 – DeepSeek 3 – Refactoring the web app to use templates](20251003.md)

We rewrote the web app to use proper templates, making it smaller and cleaner.

#### [2 Oct 2025 (e) – Gemini 2.5 Pro – Planning the annual parashah cycle](20251002e.md)

We planned to bring the cloned voice to the weekly Torah portions and outlined the audio, video, and PDF outputs.

#### [2 Oct 2025 (d) – DeepSeek 3 – Unifying the audio system](20251002d.md)

We built a single system serving all content types with original, cloned, and translated audio.

#### [2 Oct 2025 (c) – DeepSeek 3 – Resolving the class architecture](20251002c.md)

We abandoned an inheritance approach that caused circular dependencies in favor of composition.

#### [2 Oct 2025 (b) – DeepSeek 3 – Fixing parashah indexing bugs](20251002b.md)

We corrected several indexing errors that caused the wrong verses to be loaded.

#### [2 Oct 2025 – DeepSeek 3 – Building the media generation platform](20251002.md)

We assembled the full media platform and resolved dependency issues, integrating audio across all content types.

#### [1 Oct 2025 (b) – DeepSeek 3 – Documenting assets and project status](20251001b.md)

We documented the audio assets and refined the project's status tracking.

#### [1 Oct 2025 – DeepSeek 3 – Establishing a convention for referring to AI](20251001.md)

We defined a protocol for how to refer to AI collaborators in documentation.

#### [31 Aug 2025 (b) – DeepSeek 3 – Planning the Akiva and Rachel video](20250831b.md)

We storyboarded a Talmudic narrative and built a character reference system for consistent AI-generated imagery.

#### [31 Aug 2025 – DeepSeek 3 – Solving character consistency in AI images](20250831.md)

We developed a layered workflow for generating consistent characters across images.

#### [30 Aug 2025 – DeepSeek 3 – Cleaning the Talmud text](20250830.md)

We systematically cleaned the Talmud text of artifacts and established a repeatable cleaning process.

#### [29 Aug 2025 – DeepSeek 3 – Cleaning the Bible text](20250829.md)

We investigated and removed editorial additions from the Bible text while preserving the traditional text.

#### [28 Aug 2025 – DeepSeek 3 – Polishing the web app navigation](20250828.md)

We cleaned up the scripture browser's navigation and fixed several issues.

#### [27 Aug 2025 – DeepSeek 3 – Refactoring the Bible data layer](20250827.md)

We restructured the Bible classes into a clean, layered design with clear responsibilities.

#### [26 Aug 2025 – DeepSeek 3 – Integrating the content types](20250826.md)

We built a central object that ties together the different scripture applications.

#### [25 Aug 2025 – DeepSeek 3 – Polishing the Zohar modules and integrating](20250825.md)

We refined the Zohar text classes and brought all the scripture modules together.

#### [24 Aug 2025 – DeepSeek 3 – Building the Markdown editing API](20250824.md)

We created a system for overlaying user edits on top of the canonical text, and fixed a design bug in the process.

#### [23 Aug 2025 – DeepSeek 3 – Refactoring the Talmud Bavli classes](20250823.md)

We restructured the Talmud Bavli module into self-contained, hierarchically navigable classes.

#### [22 Aug 2025 – DeepSeek 3 – Building the minimal scripture browser](20250822.md)

We wrote an extremely compact single-file web app that browses the entire scripture hierarchy.

#### [21 Aug 2025 – DeepSeek 3 – Building the Mishnah text system](20250821.md)

We established the dual-purpose class pattern and implemented parsing for the Mishnah.

#### [20 Aug 2025 – DeepSeek 3 – Building the tractate class hierarchies](20250820.md)

We created separate class structures for the Mishnah and both Talmuds, driven by a shared metadata file.

#### [19 Aug 2025 – DeepSeek 3 – Implementing the parashot system](20250819.md)

We discovered and applied a pattern where content classes serve both editing and media generation, and built the parashah classes.

#### [18 Aug 2025 – DeepSeek 3 – Implementing the Bible and Psalm classes](20250818.md)

We resolved indexing issues and built the article and psalm classes with automatic text generation.

#### [17 Aug 2025 – DeepSeek 3 – Discovering the data sources and building the download system](20250817.md)

We mapped out the structure of all the source texts, created a script to download them, and produced the data files.

#### [16 Aug 2025 – DeepSeek 3 – Specifying the text formats](20250816.md)

We defined a minimal markup scheme for each content type and the rules for parsing it.

#### [15 Aug 2025 – DeepSeek 3 – Unifying the content class architecture](20250815.md)

We merged the separate content applications into a single consistent architecture.

#### [14 Aug 2025 – Gemini 2.5 – Making a thank-you video](20250814.md)

We created and published a short video thanking the audience for reaching 2,000 followers.

#### [13 Aug 2025 – Gemini 2.5 – Analyzing what made the videos work](20250813.md)

We studied the analytics and concluded that the authentic cloned voice was the key factor in the channel's growth.

#### [12 Aug 2025 (b) – Gemini 2.5 – Planning a subscription offering](20250812b.md)

We designed a two-part subscription strategy around translated psalms and Aramaic teaching.

#### [12 Aug 2025 – Gemini 2.5 – Defining the psalm content tiers](20250812.md)

We laid out the free and premium versions of the psalm videos and the thinking behind them.

#### [11 Aug 2025 – Gemini 2.5 – Refining the psalm background concepts](20250811.md)

We developed and refined a set of visual background concepts for the psalm videos.

#### [5 Aug 2025 – Gemini 2.5 – Planning the multi-platform strategy](20250805.md)

We analyzed posting times, set engagement guidelines, and outlined a YouTube strategy.

#### [Jul 2025 (d) – Gemini 2.5 – Planning strategic engagement](202507d.md)

We decided which accounts to follow publicly and how to engage to build an authoritative brand.

#### [Jul 2025 (c) – Gemini 2.5 – Setting the audio quality strategy](202507c.md)

We defined two tiers of audio production: the gold-standard cloned voice for main content and processed AI voices for supplementary material.

#### [Jul 2025 (b) – Gemini 2.5 – Defining the brand voice and moderation policy](202507b.md)

We established the channel's persona, comment moderation rules, and how to handle Shabbat.

#### [Jul 2025 – DeepSeek 3 – Project origins](202507.md)

The early history of the project, from the first experimental Torah videos through the breakthrough psalm video that launched the current series.