# Stage 3 expansion research brief (shared)

Goal: find additional books and credible content that fill gaps and add robustness to ONE locked category, for a library aimed at a working professional with average communication skills (professional and personal life, in person and in writing).

Read first:
- docs/taxonomy.md (locked categories)
- data/learning-path.json: the "gaps" array (filter to your category) and convergent concepts
- docs/stage2-synthesis.md: the "Coverage" and "Evidence quality" sections
- The existing core books (do NOT propose these): Think Faster Talk Smarter; Improv Wisdom; Made to Stick; Communicate with Mastery; Humor, Seriously; Talk (Wood Brooks); Supercommunicators; Connect; How to Know a Person.

Find 5 to 8 candidates for your category. Prioritize (1) peer-reviewed research and meta-analyses, (2) well-regarded practitioner books with a research base (for example Difficult Conversations, Crucial Conversations, Never Split the Difference, Influence by Cialdini, Getting to Yes, Thanks for the Feedback, Nonviolent Communication, Writing for Busy Readers, Gottman's work, Radical Candor), (3) reputable articles (HBR, academic reviews). Assess each honestly; a famous book with weak evidence should be rated as such. A candidate can be a paper or a review article, not only a book.

Web access: the WebFetch tool does not work in this session. Use WebSearch, and read pages with plain curl through Bash (curl -sS -L -m 20 URL), no custom user-agent header. Save downloads in a new directory under /tmp/claude-0/-home-user/1ec87173-3360-5f6f-b529-8b6cc7d13422/scratchpad/stage3-<category-id>/ and extract text with python3 -I. Skip sites that return 403 or captchas. Do not use pirated copies.

Output: write valid JSON to data/stage3/candidates-<category-id>.json:
{"category": "<category-id>",
 "candidates": [{
   "title": "", "authors": [""], "year": 0, "type": "book | peer-reviewed paper | meta-analysis | review article | practitioner article",
   "why_it_adds_value": "which specific gap or weak spot it fills, and what it adds beyond the core books",
   "credibility": "author credentials and track record",
   "evidence_quality": "High | Medium | Low, with reason (research base, replication, critiques)",
   "supports": [{"category": "", "subcategory": ""}],
   "key_ideas_preview": ["3 to 5 one-line paraphrased ideas it would contribute"],
   "overlap_with_core_books": "",
   "access": "legal preview, author site, open-access paper, library",
   "priority_score": 1-10,
   "sources_checked": ["urls"]
 }],
 "notes": ""}

Rules: original paraphrase only; no em dashes (U+2014), en dashes (U+2013) or emojis anywhere; do not fabricate titles, years, or findings (verify each candidate exists). Validate with python3 json.load and grep for U+2014 and U+2013. Reply with a short ranked list (title, author, score, one-line reason).
