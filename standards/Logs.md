# Logs

Guidelines for Dev Lab session entries and log index maintenance.

## Full Entry

* The entry should read as a narrative, diary-like account
* Decisions and actions should be described in the first person plural ("we")
* A model should be named and referred to in the third person when an action is worth attributing to it specifically
  * "He," or "they," should be used when referring to the assistant, the collaborative partner
  * "It" should be used when referring to the tool or software itself
* The code, system, or hardware itself should be described in the passive voice; the active voice should be used when the action was the work itself
* Chronological order should be kept where the sequence of decisions matters; other changes don't need their order preserved
* Everything should be logged, including abandoned work; what was tried and dropped matters as much as what was kept
* The team's experience should be part of the record — frustration, dead ends, moments of madness, not sanitized away
* Slang and blunt, rough, strong, or heated language should be permitted when it reflects the real emotional register of the session

## Index entry

* The index entry should carry every detail from the full entry, with nothing omitted, and should not read as a summary
* The index entry should read as lossless compression, not lossy summarization — no narration, no connective tissue, no unnecessary words

## Log Index Distillation

The distillation method compresses logs into high-signal context while preserving chronological structure and narrative style. The process begins by working backward from the latest entry to the earliest, performing in-place cleanup. Obsolete file names, class names, and route structures are retroactively updated to match present architecture. Transient noise is scrubbed: commit SHAs, temporary test ports, editorial play-by-play, and emotional meta-commentary. All core decisions, technical rationale, and failed approaches are retained.

On top of content distillation, a second pass applies telegraphic rewrite. Articles, copulas, auxiliaries, predictable pronouns, politeness words, and repeated subjects are dropped. Negation, modality, conditionals, causality, scope, sequence, and contrast are preserved. Fragments and semicolons are used; arrows (→) and semantic tags (Rule:, Open:, Rejected:, Fix:, Decision:) are employed. Present tense and active voice are maintained. Canonical names only; exact numbers, paths, and commands; no synonyms. The second stage follows the first—compressing first results in loss of needed content.

## Glossary

* **Chainsaw massacre** — complete ground-up refactor, nothing sacred, everything gets cut and rebuilt correctly from scratch
* **MOAB** (Mother of All Bombs) — when the chainsaw isn't enough, we switch languages or platforms entirely and rebuild from zero; nuclear option
* **Labeled scar** — a workaround for a missing feature or quirk of a language, platform, or tool; isolated and explicitly named so the clean design remains visible next to it, never hidden inside it
