# Communication Field Guide

A personal library of communication mental models, techniques and frameworks for professional and personal life, in person and in writing. Every insight is traced to a source and rated for confidence.

## Live library

https://claude.ai/artifact/FDcPSSEmH8d4tLwoTYf5MW (private to the owner until shared from the page's Share menu)

## What is here

| Path | Contents |
|---|---|
| `artifact/index.html` | Interactive, searchable library (single-file interface) |
| `artifact/library.json` | Data layer the interface reads; generated, do not edit by hand |
| `artifact/README.md` | How to view the library and how to add a book |
| `docs/entry-template.json` | Template for adding a book or paper |
| `data/stage1/` | Deep-dives on the nine core books (verified against primary sources) |
| `data/stage3/candidates-*.json` | Expansion research: candidate sources per category with credibility assessments |
| `data/stage3/extracted/` | Insights from the 56 added sources the user approved |
| `data/additions/` | Put new books here (see artifact/README.md) |
| `data/learning-path.json` | Seven-stage learning path and cross-book synthesis data |
| `docs/taxonomy.md` | Locked category structure |
| `docs/stage1-schema.md` | Data schema and the valid category ids |
| `docs/stage2-synthesis.md` | Cross-book synthesis memo |
| `docs/stage3-shortlist.md` | Ranked shortlist of expansion sources |
| `scripts/build_library.py` | Validates all data and builds `artifact/library.json` |
| `PROGRESS.md` | Stage status, decisions, open questions, next steps |

## Core books

1. Think Faster, Talk Smarter, Matt Abrahams (2023)
2. Improv Wisdom, Patricia Ryan Madson (2005)
3. Made to Stick, Chip Heath and Dan Heath (2007)
4. Communicate with Mastery, JD Schramm with Kara Levy (2020)
5. Humor, Seriously, Jennifer Aaker and Naomi Bagdonas (2021)
6. Talk, Alison Wood Brooks (2025)
7. Supercommunicators, Charles Duhigg (2024)
8. Connect, David Bradford and Carole Robin (2021)
9. How to Know a Person, David Brooks (2023)

Books 1 to 6 are Matt Abrahams's Fivebooks communication list (his own book plus his five picks), confirmed against fivebooks.com.

## Confidence legend

- **High**: replicated research or strong consensus.
- **Medium**: credible expert or case evidence.
- **Low**: plausible but thinly supported.

Credibility flags: `single-anecdote`, `pop-psychology`, `unreplicated`, `contested`, `not-confirmed-in-book`.

## Copyright

Insights are original paraphrases of principles and techniques. No passage is reproduced beyond a short phrase. Sources were read only where legally accessible (publisher previews and excerpts, author materials, open-access papers, abstracts, reputable summaries and interviews).

## Rebuild

```bash
python3 scripts/build_library.py
```
