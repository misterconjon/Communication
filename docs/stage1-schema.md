# Stage 1 shared output schema

Each book agent writes one JSON file: data/stage1/<book_id>.json

```json
{
  "book": {
    "book_id": "kebab-case-id",
    "title": "", "subtitle": "", "authors": [""],
    "year": 0, "publisher": "", "edition": "",
    "isbn": "",
    "author_credibility": "2-4 sentences: credentials, research basis, possible biases",
    "evidence_base": "How the book supports its claims (peer-reviewed research, case studies, anecdote)",
    "legal_access": [{"type": "publisher preview | library | author excerpt | interview | summary", "url": "", "note": ""}]
  },
  "insights": [
    {
      "id": "<book_id>-01",
      "name": "Short memorable name",
      "skill_type": "mental model | technique | framework",
      "explanation": "One plain-language paragraph, original paraphrase",
      "when_to_use": "",
      "worked_example": "A concrete, realistic scenario (original, not copied from the book)",
      "common_mistakes": ["", ""],
      "steps": ["Only for techniques/frameworks: concrete step-by-step use"],
      "categories": [{"category": "category-id", "subcategory": "subcategory-id"}],
      "situations": ["Short scenario labels where this applies, e.g. 'Asking a manager for a raise'"],
      "source": {"citation": "Author, Title, chapter or part if known", "underlying_research": "Named study/researcher the author relies on, if any", "urls": [""]},
      "confidence": "High | Medium | Low",
      "confidence_rationale": "Why this rating; flag single anecdotes, pop claims, or unreplicated findings",
      "flags": ["single-anecdote | pop-psychology | unreplicated | contested | none"]
    }
  ],
  "research_notes": "What sources you actually read, what you could not access, uncertainties"
}
```

## Confidence
- High: replicated research or strong consensus.
- Medium: credible expert or case evidence.
- Low: plausible but thinly supported.

## Category and subcategory ids
- foundations: mindset, audience-goals, anxiety, spontaneous-speaking, message-structures, situations
- relationships: rapport, trust-vulnerability, listening, question-design, empathy, nonverbal, networking, situations
- personal-life: partners, family, friendships, supporting-distress, repair, situations
- conversations: small-talk, storytelling, humor, group-dynamics, introductions, situations
- professional: meetings, status-updates, executive-communication, managing-up, negotiation, situations
- written-digital: email, chat, proposals-memos, executive-writing, clarity-structure, video-calls, async, tone-misreading, situations
- influence: framing, credibility, persuasive-structure, memorable-messages, overcoming-resistance, reciprocity, situations
- difficult: conflict, bad-news, giving-feedback, receiving-feedback, saying-no, apologies, boundaries, situations
- public-speaking: structure, delivery, qa, impromptu, virtual, situations
