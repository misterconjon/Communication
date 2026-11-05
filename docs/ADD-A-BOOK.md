# Add a book to the Communication Field Guide

This is the standard procedure for adding a book (or a paper) to the library. Follow it exactly, whether you are a person or a Claude agent. It exists so that a source added a year from now meets the same research, credibility, de-duplication and categorization standards as the original 65.

Two modes:

- **Single book**: one agent does Steps 1 to 8.
- **Batch (several books at once)**: one research agent per book does Steps 1 to 5 in parallel; then one integration agent does Steps 6 to 8 for all of them together (because parallel agents cannot see each other's new entries).

A copy-ready agent prompt for each mode is at the end of this file.

---

## Ground rules

1. **Copyright.** Read only legally accessible material: publisher pages, previews and excerpts, the author's own site, articles, talks, podcasts and interviews, reputable reviews and summaries, open-access papers and abstracts. Never use pirated copies, paywall mirrors or unauthorized uploads, even if a search result offers one. Write everything in original paraphrase. Never quote more than a short phrase (under 10 words), and quote sparingly.
2. **Traceability.** Every insight cites where it came from (book and chapter where verifiable) and the research behind it, if any.
3. **Honest credibility.** Rate evidence, not popularity. A famous book built on anecdote gets Medium or Low ratings and the right flags.
4. **No redundancy.** The library grows by adding distinct ideas. A source that mainly repeats an existing idea strengthens that entry instead (Step 4).
5. **Style.** No em dashes (U+2014), en dashes (U+2013) or emojis anywhere. Plain, direct sentences. US context.
6. **Do not fabricate.** If a detail (edition, page, statistic, study) cannot be verified, leave it out or list it under `verification.still_unverified`.
7. **Stable ids.** Never rename or renumber an existing insight id. Readers' saved and practiced marks depend on them.

## Web access in this environment

- The WebFetch tool may not resolve hosts here. Use WebSearch to find sources, and read pages with plain curl through Bash: `curl -sS -L -m 20 URL`. Do not set a custom user-agent header or otherwise work around bot checks.
- Save downloads into a new directory in the session scratchpad (for example `<scratchpad>/add-<book-id>/`), keep scripts elsewhere, and extract text with `python3 -I`.
- Skip any site that returns 403, 429 or a captcha. Use another source.
- Good sources, in rough order of value: publisher excerpt PDFs and "look inside" pages; the author's site, newsletter and companion materials (discussion guides, workbooks); long interviews and podcast transcripts where the author explains the frameworks; talks; reputable reviews that cite pages; the peer-reviewed studies the book relies on (abstracts at least).

---

## Step 1. Confirm the book and check it is not already here

1. Confirm title, subtitle, all authors, first publication year, publisher, current edition, ISBN-13 and page count from the publisher or a library catalog.
2. Choose a `book_id`: short kebab-case, for example `crucial-conversations`.
3. Check the library does not already contain it and whether earlier research assessed it:
   ```bash
   grep -il "<distinctive title words>" data/stage1/*.json data/stage3/extracted/*.json data/additions/*.json
   grep -il "<distinctive title words>" data/stage3/candidates-*.json docs/stage2-synthesis.md
   ```
   If a candidate file assessed it, read that assessment and build on it.

## Step 2. Research the book thoroughly

1. **Map the book.** Find the table of contents (publisher page, catalog record, excerpt). List every named framework, model, technique and core argument, chapter by chapter. This list is your coverage checklist.
2. **Read the best available legal sources** for each item on the checklist (see the source list above). Prefer the author's own words in interviews over third-party summaries.
3. **Check the evidence.** For each framework, find what it rests on: the author's research, cited studies, clinical or field practice, or anecdote. Look up the named studies (abstract at least) and any published critique or replication. Note author credentials and any commercial interest (for example, a training business built on the book).
4. **Record what you read** (URLs) for the `verification.sources_read` list.

## Step 3. Load the existing library before writing anything

```bash
python3 -c "import json;L=json.load(open('artifact/library.json'));[print(i['id'],'|',i['name'],'|',i.get('takeaway','')) for i in L['insights']]"
```
Read the full entry (`explanation`, `steps`) for any existing insight that looks close to an idea from your book.

## Step 4. Decide: new insight or supporting evidence

For each item on your checklist:

| Situation | Action |
|---|---|
| Same core idea **and** same practical advice as an existing entry | Do **not** add an insight. Add a `supports_existing` entry with `relation: "supports"` that names the existing id and says what this book adds (a sharper method, a better example, extra evidence). |
| Same topic, but the book **changes or limits** the advice (different conditions, different steps, a caveat) | Add `supports_existing` with `relation: "qualifies"`. If the difference is large enough to change what a reader would do, also add it as a new insight and say how it differs in the explanation. |
| The book **disagrees** with an existing entry | Add `supports_existing` with `relation: "contradicts"` and explain the disagreement. Add a new insight only if the book's alternative is itself useful advice. |
| A **distinct** idea, technique or framework not in the library | Add a new insight. |
| The book's **signature framework** (the thing it is known for) | Always add it as its own insight, even if parts overlap existing entries. Explain how it relates to them, and add `supports_existing` links for the overlapping parts. |
| Minor, obvious or weakly supported point | Leave it out, and note it in `research_notes` as skipped with the reason. |

**Comprehensiveness test:** when you finish, every named framework from your checklist is either a new insight, a `supports_existing` link, or listed in `research_notes` as skipped with a reason. A typical book yields 6 to 15 new insights. There is no quota: include every genuinely useful, well-sourced idea and nothing padded.

## Step 5. Write the source file

Copy `docs/entry-template.json` to `data/additions/<book-id>.json` and fill it in. Field standards:

### Book block
- `source_type`: `book` (or `peer-reviewed paper`, `meta-analysis`, `review article`, `practitioner article`). `core`: `false`.
- `author_credibility`: 2 to 4 sentences on credentials, track record, research basis and any commercial interest.
- `evidence_base`: how the book supports its claims, honestly.
- `legal_access`: where a reader can legally preview or borrow it.

### Each insight
| Field | Standard |
|---|---|
| `id` | `<book-id>-01`, `-02`, and so on |
| `name` | Short and memorable; use the book's own name for a named framework (for example "STATE My Path") |
| `takeaway` | One sentence, 10 to 22 words, stating the advice itself. Never "The book says..." or "Research shows...". This shows in every result list, so it must stand alone |
| `skill_type` | `technique` (a concrete method you do), `framework` (a named multi-part structure or model), `mental model` (a way of seeing a situation that changes your choices) |
| `explanation` | One plain-language paragraph, about 80 to 160 words: what it is, why it works, and where it comes from |
| `when_to_use` | The specific moments it helps, and when not to use it if relevant |
| `worked_example` | An original, realistic scenario with sample wording. Use professional and personal settings where the idea applies to both |
| `steps` | For techniques and frameworks: 3 to 7 concrete, ordered actions a reader could follow tomorrow. Empty for pure mental models |
| `common_mistakes` | 2 to 4 specific ways people get it wrong |
| `categories` | See the categorization guide below. Primary placement first |
| `situations` | 2 to 4 short, realistic scenario labels |
| `source.citation` | Author, title, chapter (and pages if verified) |
| `source.underlying_research` | Named studies with authors and year, verified at least by abstract. Say "Practitioner experience; no direct empirical test" when that is the truth. If you link research the book does not itself cite, say so |
| `source.urls` | Pages you actually read |
| `confidence` | `High`, `Medium` or `Low` (rubric below) |
| `confidence_rationale` | One to three sentences justifying the rating |
| `flags` | Any of `single-anecdote`, `pop-psychology`, `unreplicated`, `contested`, `not-confirmed-in-book`; empty list if none |

### Confidence rubric
- **High**: the specific advice rests on replicated research or strong expert consensus (for example a meta-analysis, or multiple independent studies). A famous author is not enough.
- **Medium**: credible expert practice, case evidence, or a single good study; the idea is consistent with research but the specific method is untested.
- **Low**: plausible but thinly supported: one anecdote, an untested typology, or a claim with weak or contradicted evidence.
- If a supporting paper lists Francesca Gino as a coauthor, keep it but add an integrity note in `confidence_rationale` (user decision).

### Also include
- `supports_existing`: as decided in Step 4. Each `note` states concretely what this book adds.
- `verification`: `{"date": "YYYY-MM-DD", "sources_read": [...], "still_unverified": [...]}`
- `research_notes`: your coverage checklist outcome, including skipped items and why.

## Categorization guide

Every insight gets 1 to 3 category tags. The first tag is its primary home: the place a reader would most expect to find it. Add a second or third only if a reader would genuinely look for it there too. Over-tagging dilutes the filters. Valid ids are also listed in `docs/stage1-schema.md`; the build rejects anything else.

| Category id | Subcategory ids and what belongs there |
|---|---|
| `foundations` | `mindset` (beliefs about communicating: connection over perfection, curiosity); `audience-goals` (analyzing who you are talking to and what you want); `anxiety` (managing nerves and stress); `spontaneous-speaking` (thinking and speaking on the spot, improv); `message-structures` (general-purpose structures such as What, So What, Now What) |
| `relationships` | `rapport`; `trust-vulnerability` (self-disclosure, building trust); `listening` (active, reflective, looping); `question-design` (what and how to ask); `empathy` (understanding others' perspectives and feelings); `nonverbal` (reading and sending body and voice cues); `networking` |
| `personal-life` | `partners`; `family` (including parenting); `friendships`; `supporting-distress` (comforting someone who is struggling); `repair` (recovering a relationship after a rupture) |
| `conversations` | `small-talk`; `storytelling`; `humor`; `group-dynamics` (conversations among several people); `introductions` |
| `professional` | `meetings`; `status-updates`; `executive-communication` (talking to senior leaders); `managing-up`; `negotiation` |
| `written-digital` | `email`; `chat`; `proposals-memos`; `executive-writing`; `clarity-structure` (making writing clear and skimmable); `video-calls`; `async`; `tone-misreading` |
| `influence` | `framing`; `credibility`; `persuasive-structure`; `memorable-messages`; `overcoming-resistance`; `reciprocity` |
| `difficult` | `conflict` (disagreements and heated moments); `bad-news`; `giving-feedback`; `receiving-feedback`; `saying-no`; `apologies`; `boundaries` |
| `public-speaking` | `structure`; `delivery` (voice, body, slides); `qa`; `impromptu`; `virtual` |

Every category also has `situations` ("Situations in practice"). Use it only for an insight that is itself a scenario-specific playbook.

Placement rules of thumb:
- Place by **what the reader is trying to do**, not by the book's genre. A listening technique from a conflict book goes in `relationships/listening` first, and `difficult/conflict` second if it is mainly taught for conflict.
- A technique for a **heated moment** belongs in `difficult/conflict`; the same technique for **everyday understanding** belongs in `relationships`.
- **Feedback** methods: giving goes in `difficult/giving-feedback`; hearing it goes in `difficult/receiving-feedback`.
- **Self-regulation** in the moment (staying calm, pausing) goes in `foundations/anxiety` if it is about nerves, and `difficult/conflict` if it is about anger or defensiveness.
- **Presentation** craft goes in `public-speaking`; **persuasion** logic goes in `influence`, even when it is delivered in a talk.
- Before finalizing, compare your tags with 3 to 5 existing entries on the same theme (search `artifact/library.json`) and stay consistent with them.

## Step 6. Validate

```bash
python3 -c "import json;json.load(open('data/additions/<book-id>.json'))"
grep -nP '[\x{2013}\x{2014}]' data/additions/<book-id>.json   # must print nothing
python3 scripts/build_library.py                            # must print no ERROR; fix every WARNING about your file
```
Also confirm, using `scripts/build_library.py` output or a quick script, that every `supports_existing.insight_id` exists and every insight has a `takeaway`.

## Step 7. Integrate into the guide (integration agent in batch mode)

1. **Cross-book de-duplication.** When several books were added together, compare their new insights with each other using the Step 4 rules. Merge true duplicates into the stronger or more original entry by converting the weaker one into a `supports_existing` link. Never renumber ids, and repoint any links to a removed id.
2. **Related links.** In `data/learning-path.json` `related_insights`, add `{"ids": [...], "relation": "complementary"}` for entries that work well together and `"tension"` for entries that pull against each other.
3. **Learning path.** Add only the strongest and most foundational new insights to the right stage in `data/learning-path.json` (a few per book at most). Place each after the entries it depends on.
4. **Situation playbooks.** In `data/situations.json`, add a new insight's id to a playbook step only where it genuinely improves that step (and add it to that playbook's `insight_ids`). Propose a new playbook only for a high-value moment not yet covered.
5. **Takeaways.** Each new insight carries its own `takeaway` field; no separate file edit is needed.

## Step 8. Build, test, publish, record

1. `python3 scripts/build_library.py`, with no ERROR or WARNING lines.
2. Smoke test in a headless browser:
   ```bash
   cd artifact && python3 -m http.server 8765 &
   node scripts/smoke_test.js http://localhost:8765/index.html
   ```
   It must report no errors, no horizontal overflow, and the new sources and counts.
3. Republish the artifact to the same URL (listed in README.md), passing `files: {"library.json": "artifact/library.json"}`.
4. Update `PROGRESS.md` (what was added, counts, anything unverified) and commit with a message such as `Add <book title>`; push.

---

## Agent prompt: single book or batch research agent (Steps 1 to 6)

> You are adding one book to the Communication Field Guide in /home/user/comm-models. Read docs/ADD-A-BOOK.md in full and follow Steps 1 to 6 exactly. Book: "<title>" by <author>. Book id: <book-id>. Write only data/additions/<book-id>.json (and scratch files in your scratchpad). Other agents may be adding other books in parallel; do not edit any other data file. Reply with: verified metadata; the coverage checklist with the outcome for each item (new insight id, supports_existing link, or skipped with reason); each new insight's name, skill type, primary category and confidence; and what you could not access.

## Agent prompt: batch integration agent (Steps 7 to 8, without publishing)

> You are the integration agent for a batch of books just added to the Communication Field Guide in /home/user/comm-models: <list of data/additions files>. Read docs/ADD-A-BOOK.md and follow Step 7, then Step 8 parts 1 and 2 (build and smoke test). Write a log of every merge, link, path placement and playbook change to docs/additions-log-<date>.md. Reply with a summary of merges, final insight count, path and playbook changes, and test results.
