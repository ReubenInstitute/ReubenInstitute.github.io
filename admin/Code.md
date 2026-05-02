# Code

> A project is completed when there is nothing left to remove from it.

This document represents a minimalist philosophical overlay that applies to ANY language-specific coding standards. We start with the language's conventions (PEP 8 for Python, etc.) and then apply these additional fanatic constraints focused on semantic purity and minimalism.

## Class Design

* Reject false managers (Manager, Handler, Processor, Helper, Util)
* Objects embody domain concepts, not procedural operations
* Only use "-er" suffixes when management is the actual domain responsibility
* If you need a "Manager", the managed object should manage itself
* Classes are nouns that can act, not verbs in disguise. A ChapterManager is idiotic - it's a Book. A UserManager is nonsense - it's User.create(). Reserve managerial names only for true domain managers like MemoryManager where management is the actual job.

## Format

### Indentation

Use tabs only (1 byte per indent) We don't care about editors or viewers. A "good cyberspace citizen" won't waste bytes on visual formatting. Fix the editor, don't mess up the code. Tabs are semantically correct for indentation.

### Comments

* Only when code is unclear (explain architecture, not obvious operations) · Avoid comments that state what the code does. Comments are failures of expression - remove the need for them. If you need comments to explain what your code does, write clearer code.

### Blank Lines

* No blank lines inside functions/methods
* One blank line between functions/methods
* Two blank lines between classes. Blank lines are visual crutches for poor structure. These minimal separations are courtesy exceptions only - if editors displayed functions/classes clearly, we'd remove them entirely. If you need blank lines inside functions, your function is too complex.

### String Quotes

* Double quotes for user-facing strings
* Single quotes for code/internal strings
* Double quotes are more visually "disturbing" - reserve for "official" content (constants, user data, URLs). Single quotes are for minor, internal operations. We intentionally mix them for semantic distinction.

### Method Chaining

One method per line for clarity. Remove horizontal complexity by making dependencies explicit. Each operation should be visible and intentional.

### Line Length

Pragmatic approach (no strict limit, but avoid extreme lengths). Artificial limits add nothing - let the code dictate its form. Readability comes from good structure, not arbitrary line breaks.

## Variable Naming Rules

### 1. Single Letter Preference

Use single letters for short-lived variables in tight scopes. Use maximum two letters for slightly longer-lived temporary variables. If code becomes complex or conflicts arise, expand names minimally to restore clarity. Never use abbreviations longer than two letters. Valid: p, ch, x, y. Invalid: para, chnl, paragraph.

### 2. No Underscores Unless Required

A variable name with underscore is valid only when both parts represent independent concepts that can exist separately. Valid: audio_file, font_size, red_car. Invalid: book_num, current_page, paragraph_obj.

### 3. No Abbreviations

A variable name must use complete words only with no abbreviations. Valid: directory, paragraph, chapter. Invalid: dir, para, chap.

### 4. No Non-Words

A variable name must consist only of valid words from the language. Valid: start_verse, end_verse, hebrew_name. Invalid: startverse, endverse, hebrewname.

### 5. Formatting Conventions

snake_case for multi-word variables/functions (all lowercase). CamelCase for classes.

### 6. Philosophy

Treat code like mathematical notation — concise and context-aware. Every character must earn its place. `c = library.book.chapter` is cleaner than redundant `chapter = library.book.chapter`.

## Error Handling

* Specific exceptions only (no bare `except:`)
* Handle expected errors, let unexpected ones propagate
* Remove unnecessary error handling that obscures real problems. Don't catch what you can't handle.
