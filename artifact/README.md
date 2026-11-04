# Communication Field Guide: interactive library

`index.html` is the interface. `library.json` is the data layer. The page reads `library.json` from the same folder at load time, so adding books or insights never requires changing the interface.

## Viewing it

- Published: open the claude.ai artifact link listed in the repository README.
- Locally: browsers block `fetch` from `file://`, so serve the folder:
  ```bash
  cd artifact && python3 -m http.server 8000
  ```
  then open http://localhost:8000.

## What the page does

- **Library**: free-text search plus filters for category, subcategory, book or source, confidence level, skill type (mental model, technique, framework) and origin (core book or added source). Click an entry to open it: explanation, when to use it, worked example, steps, common mistakes, situations, confidence and its rationale, credibility flags, source citation and the research behind it, and other sources that support or qualify it.
- **Learning path**: the seven-stage sequence from the Stage 2 synthesis.
- **Sources**: every core book and added source with a credibility note; click through to its entries.
- Every entry has a stable link: `#insight-<id>`.

## Add a book

1. **Copy the template.** Copy `docs/entry-template.json` to `data/additions/<book-id>.json`. Use a short kebab-case id, such as `crucial-conversations`.
2. **Fill in the book details.** Complete the `book` block. Set `"core": false` for anything outside the original nine books.
3. **Write the insights.** Add one object per insight to `insights`. Give each a unique id (`<book-id>-01`, `<book-id>-02`, and so on).
   - Write explanations and examples in your own words. Quote no more than a short phrase.
   - `skill_type` must be `mental model`, `technique` or `framework`.
   - `confidence` must be `High` (replicated research or strong consensus), `Medium` (credible expert or case evidence) or `Low` (plausible but thinly supported). Explain the rating in `confidence_rationale`.
   - `categories` must use the ids listed in `docs/stage1-schema.md`. One insight can sit in several categories.
   - Optional `flags`: `single-anecdote`, `pop-psychology`, `unreplicated`, `contested`, `not-confirmed-in-book`.
4. **Avoid duplicates.** If the new book mainly repeats or strengthens an idea already in the library, do not add a new insight. Add an entry to `supports_existing` that points to the existing insight id and explains what the book adds. To find existing ids, search the library page; each entry's link ends with its id.
5. **Rebuild the data file.**
   ```bash
   python3 scripts/build_library.py
   ```
   The script validates every file. It stops with an ERROR if an id is duplicated, a category id is unknown, a required field is missing, or the file contains an em or en dash. It prints a WARNING for links that point to ids that do not exist.
6. **Optional: add it to the learning path.** Add the new insight ids at the right position in `data/learning-path.json` and rebuild.
7. **Commit.** Commit the new file and the rebuilt `artifact/library.json`. If the artifact is published, republish it so viewers get the new data.

## Data format of library.json

| Key | Contents |
|---|---|
| `taxonomy` | Categories, each with subcategories (ids and display names) |
| `sources` | One record per book or paper: title, authors, year, publisher, source type, core flag, credibility and evidence notes, legal access links |
| `insights` | One record per insight, as in the template, plus `source_id` and `supporting_evidence` (links from other sources) |
| `learning_path.stages` | Ordered stages, each with title, purpose, rationale and ordered `insight_ids` |
| `convergent_concepts`, `related_insights` | Cross-book synthesis from Stage 2 |

Do not edit `library.json` by hand. It is regenerated from the files in `data/`.
