# Code

> A project is completed when there is nothing left to remove from it.

This document represents a minimalist philosophical overlay that applies to ANY language-specific coding standards. We start with the language's conventions (PEP 8 for Python, etc.) and then apply these additional fanatic constraints focused on semantic purity and minimalism.

"Know the rules well, so you can break them effectively."

## Class Design

* Reject false managers (Manager, Handler, Processor, Helper, Util)
* Objects embody domain concepts, not procedural operations
* Only use "-er" suffixes when management is the actual domain responsibility
* If you need a "Manager", the managed object should manage itself
* Classes are nouns that can act, not verbs in disguise. A ChapterManager is idiotic - it's a Book. A UserManager is nonsense - it's User.create(). Reserve managerial names only for true domain managers like MemoryManager where management is the actual job.

## Format

### Indentation

Use tabs only (1 byte per indent) We don't care about editors or viewers. A "good cyberspace citizen" won't waste bytes on visual formatting. Fix the editor, don't mess up the code. Tabs are semantically correct for indentation.

### Alignment

Do not use extra spaces inside code to visually align values — alignment is the job of indentation, not spacing.

### Comments

No comments or docstrings. If the code needs a comment to be understood, the code is unclear — fix the code, not the explanation. Comments are a symptom, not a cure.

### Blank Lines

* No blank lines inside functions/methods
* One blank line between functions/methods
* Two blank lines between classes. Blank lines are visual crutches for poor structure. These minimal separations are courtesy exceptions only - if editors displayed functions/classes clearly, we'd remove them entirely. If you need blank lines inside functions, your function is too complex.

### If Statements

Keep `if` statements on separate lines with proper indentation, never crammed onto a single line. Outside Python, single‑line `if` bodies are written without surrounding braces — the line break alone ends the block.

### String Quotes

* Double quotes for user-facing strings
* Single quotes for code/internal strings
* Double quotes are more visually "disturbing" - reserve for "official" content (constants, user data, URLs). Single quotes are for minor, internal operations. We intentionally mix them for semantic distinction.

### Method Chaining

One method per line for clarity. Remove horizontal complexity by making dependencies explicit. Each operation should be visible and intentional.

### Line Length

Pragmatic approach (no strict limit, but avoid extreme lengths). Artificial limits add nothing - let the code dictate its form. Readability comes from good structure, not arbitrary line breaks.

## Variable Naming Rules

### 1. Judgment Over Rules

Readability is the only real test — a name is correct if the reader understands it instantly, without needing a comment.

Short-lived variables in a tight, obvious scope may use a single or double letter (`p` for a `Psalm` used two lines later, `i` for a loop index). The moment a variable lives long enough that you'd forget what it stands for, name it properly (`psalm_number`, not `nr`, not `n`).

Abbreviations are fine when they're unambiguous to any reader without a comment (`idx`, `nr`). They're wrong when they're cryptic or could mean several things (`ctx` — context? controller? contact?) or mangled beyond recognition (`ctrl_prmtl_hndlr`). "Rules are made to be broken" — use your brain, not a letter-count.

### 2. No Underscores Unless Required

A variable name with underscore is valid only when both parts represent independent concepts that can exist separately. Valid: audio_file, font_size, red_car. Invalid: book_num, current_page, paragraph_obj.

### 3. Formatting Conventions

snake_case for multi-word variables/functions (all lowercase). CamelCase for classes.

### 4. Philosophy

Treat code like mathematical notation — concise and context-aware. Every character must earn its place. `c = library.book.chapter` is cleaner than redundant `chapter = library.book.chapter`.

## Markdown

* Use asterisk for bulletpoint character
* Use proper markdown headers (`#`, `##`)

## Error Handling

* Specific exceptions only (no bare `except:`)
* Handle expected errors, let unexpected ones propagate
* Remove unnecessary error handling that obscures real problems. Don't catch what you can't handle.
