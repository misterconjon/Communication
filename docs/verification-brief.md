# Stage 1b verification brief (shared by all verification agents)

Network access is now open. The Stage 1 file for your book was written from search snippets only, because page fetches were blocked. Your job is to verify and correct it against primary and reputable sources you can now actually read (publisher pages and previews, Google Books, the author's own site, articles and interviews, Stanford GSB, HBR, the cited peer-reviewed papers or their abstracts, reputable reviews).

For each insight in the file:
1. Confirm the idea actually appears in the book (or the author's own material). If you cannot confirm it, keep it but add the flag "not-confirmed-in-book" and say so in confidence_rationale. If it is clearly wrong or misattributed, fix or remove it and log it.
2. Check underlying_research: confirm each study exists and supports the claim as stated (read the abstract at least). Correct citations (authors, year, journal). Remove any "not confirmed as cited" caveat only if you confirm the book cites it.
3. Re-assess the confidence rating against the standard (High: replicated research or strong consensus; Medium: credible expert or case evidence; Low: plausible but thinly supported). Change it only with a stated reason.
4. Add chapter or part references to source.citation where you can verify them.
5. Fill book metadata gaps (edition, ISBN, pages) only if verified.
6. Add genuinely important insights that were missed, if well sourced, in the same schema.

Rules:
- Original paraphrase only. Never quote more than a short phrase (under 10 words). Do not use pirated full-text copies.
- No em dashes, en dashes, or emojis anywhere.
- Keep the schema in docs/stage1-schema.md exactly. Keep existing ids; new insights continue the numbering.
- Add a top-level "verification" object: {"date": "2026-11-04", "sources_read": [urls], "changes": ["id: what changed and why"], "still_unverified": ["..."]}.
- Keep user decisions: retain all Low-confidence insights (flagged); keep Gino-coauthored studies with an integrity note rather than downgrading.

Validate with python3 json.load and grep for U+2014 and U+2013 before finishing. Reply with a short summary: insights confirmed, changed, added, removed, confidence changes, and what is still unverified.
