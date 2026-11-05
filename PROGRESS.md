# PROGRESS

Last updated: 2026-11-04

## Stage status
| Stage | Status |
|---|---|
| 0. Taxonomy co-design (Checkpoint 1) | Complete: taxonomy locked 2026-11-04 |
| 1. Book deep-dives (Checkpoint 2) | Approved; verification pass (1b) complete: 137 insights (6 High, 113 Medium, 18 Low) |
| 2. Cross-book synthesis | Complete: docs/stage2-synthesis.md, data/learning-path.json |
| 3. Expansion research (Checkpoint 3) | Complete: 56 sources extracted (109 new insights after 1 merge); integrated into learning path (docs/stage3c-integration-log.md) |
| 4. Interactive artifact (Checkpoint 4) | Built, tested, published: https://claude.ai/artifact/FDcPSSEmH8d4tLwoTYf5MW. Awaiting user review |
| 5. Word guide (Checkpoint 5) | Not started |
| 6. Quality assurance | Not started |

## Decisions made
- Stage 3: add all candidates scoring 7+ (option B, 56 sources).
- Papers and books: extract every relevant high-quality insight, no fixed count; no redundant insights (use supports_existing instead).
- No cross-cultural communication; US context only.
- Status updates and aging parents remain documented gaps.
- Keep all 18 Low-confidence insights, clearly flagged.
- Keep Gino-coauthored studies with an integrity note (no downgrade).
- Run verification pass (docs/verification-brief.md) before Stage 2.
- Think Faster, Talk Smarter (Abrahams) is a core book.
- Questioning and listening merged into Relationships and connection.
- Written and digital communication merged into one category.
- Foundations category added as the general starting section.
- Personal life category added.
- Every category gets a "Situations in practice" subcategory.
- Taxonomy locked (docs/taxonomy.md). Stage 1 schema: docs/stage1-schema.md.
- Depth: include all relevant insights per book (about 10, more or fewer as warranted).

## Core books (list confirmed by user 2026-11-04)
- Think Faster, Talk Smarter, Matt Abrahams
- Improv Wisdom, Patricia Ryan Madson
- Made to Stick, Chip and Dan Heath
- Communicate with Mastery, JD Schramm with Kara Levy (Wiley, 2020)
- Humor, Seriously, Jennifer Aaker and Naomi Bagdonas
- Talk: The Science of Conversation, Alison Wood Brooks
- Supercommunicators, Charles Duhigg
- Connect, David Bradford and Carole Robin
- How to Know a Person, David Brooks

## Stage 1 results
- 117 insights: 6 High, 93 Medium, 18 Low. 53 techniques, 42 mental models, 22 frameworks.
- Flags: 20 unreplicated, 12 pop-psychology, 9 single-anecdote, 9 contested.
- All files valid JSON, all category ids valid, no em or en dashes.
- Coverage gaps: async communication, saying no. Thin: reciprocity, virtual presentations, introductions, status updates, proposals and memos, apologies, boundaries.
- Source limitation: network policy blocked all page fetches; agents worked from search snippets and summaries. Studies not confirmed as cited by the book are labeled in each file.
- Integrity note: two Talk-related papers (Huang et al. 2017, Yeomans et al. 2020) list Francesca Gino as coauthor; no allegation against Brooks found.

## Stage 1b verification
- Agents read publisher extracts, author companions, workbooks and paper abstracts via curl (WebFetch tool cannot resolve hosts).
- 20 insights added, none removed, no downgrades; 2 upgrades (TFTS toast, Humor leaders) with stated reasons.
- Remaining gaps: async (0), reciprocity (1), saying no (1), virtual presenting (1), introductions (2), proposals and memos (2).
- Think Faster, Talk Smarter insight 16 (CLEAR conflict framework) comes from an updated edition announced Oct 2026.

## Library status
- 246 insights (137 core, 109 added) from 65 sources; 142 supporting-evidence links; learning path 129 insights in 7 stages.
- Partly filled gaps: async (documentation culture), virtual presenting, introductions, family (no parenting source), humor (one correlational meta-analysis). Unfilled by decision: status updates, aging parents.

## Open questions / blockers
- Fixed: docs/taxonomy.md was accidentally emptied at Stage 0 lock; restored from commit e8a68ad.
- fivebooks.com blocked by network policy; user supplied the list directly.
- GitHub repo: misterconjon/communication (connected).
- Network access opened by user 2026-11-04; Fivebooks list confirmed to match.

## Next steps
- User reviews artifact at Checkpoint 4; then Stage 5 Word guide.
