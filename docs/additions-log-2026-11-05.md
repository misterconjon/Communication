# Additions integration log, 2026-11-05

Batch: `data/additions/talk-like-ted.json`, `difficult-conversations.json`, `crucial-conversations.json`, `the-next-conversation.json`, `nonviolent-communication.json` (61 new insights as delivered by the research agents). Procedure: docs/ADD-A-BOOK.md Step 7, then Step 8 parts 1 and 2. Nothing was published.

After integration the library holds **306 insights** (60 from this batch) from 70 sources, with 218 supporting links and 28 situation playbooks. `python3 scripts/build_library.py` prints no ERROR or WARNING lines, and the smoke test passes (details at the end).

## 1. Cross-book de-duplication

Method: each of the 61 new insights was compared with the other 60 and with the existing library entries on the same themes (name, takeaway, explanation, steps, when to use). An insight was merged only when the core idea and the practical advice were both the same.

### 1.1 Merges (1)

| Removed id | Kept id | Reason |
|---|---|---|
| `crucial-conversations-10` (Retake Your Pen) | `difficult-conversations-08` (Ground Your Identity) | Same idea, same advice: when criticism feels like a verdict on your worth, secure your own sense of self first so you can look calmly for what is true in it. Difficult Conversations (1999) is the original source and the fuller entry (concrete steps, the three identity questions). Retake Your Pen is new in the 2021 third edition, Low confidence, with no steps. The removed entry became a `supports` link in `crucial-conversations.json`. That link keeps its unique content: Grenny's point that you are responsible for your own psychological safety, and its caveat about abuse and physical danger. The book's existing `supports` link to `connect-07` stays (its note no longer names the removed id). `research_notes` records that the id is retired. Nothing else pointed to the removed id: no `supports_existing`, learning-path, related-link or playbook references. No ids were renumbered. |

### 1.2 Candidate overlaps reviewed and kept as separate insights

| Candidates | Decision | Why they are not duplicates |
|---|---|---|
| "Story you tell yourself": `crucial-conversations-05` / `-06` vs `difficult-conversations-03` / `-07` vs `the-next-conversation-01` | kept, linked | CC-05 works on your own interpretation (facts versus story, Path to Action). CC-06 questions three specific self-justifying stories. DC-03 is about learning the other person's story. DC-07 is about naming and sharing your feelings. TNC-01 uses disproportion as the signal to get curious about the other person's hidden struggle. They are related but each gives different advice. A new convergent concept groups them. |
| Intent vs impact: `difficult-conversations-05` vs `connect-03` (existing) | kept, linked complementary | DC is the original source. It adds the accused side of the exchange (acknowledge the impact before explaining what you meant, own mixed motives) and Heen's "assume you do not know". `connect-03` is a core entry and cannot be removed. No other insight in this batch duplicates it. |
| Feelings vs judgments: `difficult-conversations-07` vs `nonviolent-communication-03` (and `connect-06`) | kept, linked | DC-07 is a broad method: find your feelings, check the story behind them, share them as feelings rather than verdicts. NVC-03 is a narrow translation technique for pseudo-feelings (ignored, manipulated) and adds the need behind the feeling. |
| "I" language and lowering defenses: `the-next-conversation-15` vs `nonviolent-communication-01` / `-02` vs `crucial-conversations-07` (STATE) | kept, linked | TNC-15 is three wording swaps ("I" not "you", "what" not "why", acknowledge first). NVC-01 is the four-part observation, feeling, need, request structure. NVC-02 is the camera test for observations. STATE is a five-part sequence that ends in a tentative conclusion. Each is a distinct signature tool. STATE and NVC-02 are linked as a tension (state your conclusion versus strip evaluations). |
| Openings: `the-next-conversation-13` / `-16` vs `difficult-conversations-10` vs `crucial-conversations-03` / `-04` | kept, linked | TNC-13 frames one topic, a desired outcome and the other person's agreement. TNC-16 covers logistics and leading with the point. DC-10 opens with a neutral description of the difference. CC-03 and CC-04 repair safety and misread intent. TNC-16 and DC-10 are linked as a tension (lead with your point versus open from the neutral third story). TNC-16 and SPIKES are also linked as a tension (no cushion versus checking what the person already knows). |
| Defensiveness when receiving feedback: `the-next-conversation-14` vs `difficult-conversations-08` vs `nonviolent-communication-05` (and `crucial-conversations-10`) | merged CC-10 only; others kept and linked | TNC-14 is an in-the-moment sequence (breathe, let the words drop, get curious). DC-08 is identity work. NVC-05 chooses where to put your attention (your needs, then theirs). A new convergent concept groups them. |
| Goals before a hard talk: `crucial-conversations-01` vs `difficult-conversations-09` vs `the-next-conversation-02` (and `talk-wood-brooks-12`) | kept, linked complementary | CC-01 checks your motive mid-conversation and refuses the Fool's Choice. DC-09 decides whether to raise an issue at all and offers three purposes you can control. TNC-02 adds conversational values as a compass that holds up when the other person behaves badly. |
| `difficult-conversations-04` (And Stance) vs `crucial-conversations-01` (Fool's Choice) | kept, linked | The And Stance is about holding two stories, two sets of feelings or a complex self-image at once. The Fool's Choice is about finding an option that serves both candor and the relationship. |
| `nonviolent-communication-10` (anger) vs `crucial-conversations-05` | kept, linked | Both locate the cause of anger in interpretation, but NVC traces it to an unmet need and CC to an unchecked story. |
| `the-next-conversation-04` vs `think-faster-talk-smarter-02`, `gottman-seven-principles-03` | kept, linked | The research agent already recorded a `supports` link to TFTS-02. TNC-04 is a different three-part sequence for provocation rather than for speaking nerves. |
| `talk-like-ted-07` vs `minto-pyramid-principle-01`, `made-to-stick-03` | kept, linked | The message map is a speaking tool that produces versions of different lengths. Its `supports` link to Minto was already recorded. |

## 2. Recategorization (13 insights changed; 7 primary placements moved)

The Categorization guide was applied to all 61 (now 60) insights, and each was compared with existing entries on the same theme (`connect-03`, `connect-04`, `connect-06`, `connect-07`, `talk-wood-brooks-12`, `supercommunicators-01` and `-03`, `ury-positive-no-01`, `connect-13`, `gottman-seven-principles-01`). Every new insight has 1 to 3 tags, with the primary first.

| Id | Before | After | Reason |
|---|---|---|---|
| `crucial-conversations-04` Contrasting | conflict, giving-feedback | **giving-feedback**, conflict | It is most often used proactively, just before a point that could sting. The reader's goal is to deliver a concern without being misheard. |
| `crucial-conversations-09` CPR | conflict, giving-feedback, repair | **giving-feedback**, conflict, repair | It decides which concern to raise (incident, pattern or relationship), so it is a feedback-giving choice. |
| `difficult-conversations-04` And Stance | conflict, mindset, family | **foundations/mindset**, conflict | It is a mental model that runs through the whole book. The family tag only reflected one example. |
| `difficult-conversations-05` Intent vs impact | conflict, giving-feedback, empathy | **giving-feedback**, conflict, receiving-feedback | Matches `connect-03` (primary giving-feedback). Half the technique covers being accused, which is receiving feedback. |
| `difficult-conversations-09` Choose your purpose | conflict, audience-goals | **foundations/audience-goals**, conflict | Goal-setting before a conversation. Matches `the-next-conversation-02` and `talk-wood-brooks-12`. |
| `the-next-conversation-13` Frame the conversation | conflict, meetings, giving-feedback | **foundations/message-structures**, giving-feedback, meetings | A general-purpose opening structure (Fisher's Rule 3) for any important conversation, not only conflict. |
| `the-next-conversation-15` Lower their defenses | conflict, question-design, giving-feedback | **giving-feedback**, conflict, question-design | It is used when raising a problem with someone's work or behavior. |
| `crucial-conversations-01` Start with Heart | conflict, mindset | conflict, **audience-goals** (second) | "What do I really want" is goal analysis, not a belief about communicating. |
| `difficult-conversations-07` Have your feelings | conflict, empathy | conflict, giving-feedback, empathy | Uses the same tag set as `connect-06` and `nonviolent-communication-03` on the same theme. |
| `nonviolent-communication-03` Pseudo-feelings | conflict, empathy, partners | conflict, giving-feedback, empathy | Same as above. It applies to work as much as to partners. |
| `difficult-conversations-10` Third story | conflict, partners, giving-feedback | conflict, giving-feedback, partners | Reordered so the more likely second home comes first. |
| `nonviolent-communication-13` Mediate | conflict, meetings, family | conflict, **group-dynamics**, family | Mediating between two or more people is group dynamics. It is not specific to meetings. |
| `the-next-conversation-16` Start difficult conversations right | bad-news, giving-feedback, meetings | bad-news, giving-feedback | The meetings tag was diluting the filter. |

Kept as is after review: listening techniques were already primary in `relationships/listening` (`crucial-conversations-08`, `nonviolent-communication-07`). Receiving-feedback entries were already in `difficult/receiving-feedback` (`difficult-conversations-08`, `nonviolent-communication-05`, `the-next-conversation-14`). Saying no, boundaries and apologies were already correct (`the-next-conversation-11`, `-12`, `-08`). Anger and defensiveness regulation (`crucial-conversations-05`, `nonviolent-communication-10`, `the-next-conversation-03`, `-04`) stays in `difficult/conflict`, as the guide requires for anger rather than nerves. `foundations/anxiety` remains a secondary tag on `the-next-conversation-04`. The Talk Like TED placements were all consistent with the existing public-speaking entries.

Primary placement by book after the change:

| Book | Insights | `difficult/conflict` primary before | After |
|---|---|---|---|
| Difficult Conversations | 12 | 11 | 8 |
| Crucial Conversations | 12 (was 13) | 7 of 13 | 5 |
| The Next Conversation | 16 | 7 | 6 |
| Nonviolent Communication | 13 | 5 | 5 |

The remaining conflict primaries in Difficult Conversations (three conversations, learning stance, explore stories, contribution, feelings, third story, speak for yourself, take the lead) are all taught specifically for disagreements, so `difficult/conflict` is the reader's real home for them.

## 3. Quality pass

All 60 remaining takeaways were checked against the 10 to 22 word rule and the requirement to state the advice itself. Explanations were checked for length (80 to 160 words) and clarity, and steps for concreteness. Facts and sources were left unchanged.

Takeaways rewritten (5):
- `talk-like-ted-01`: was phrased as a question. Now: "Make every talk emotional, novel and memorable: touch the heart, teach something new, and present it unforgettably."
- `crucial-conversations-02`: now says what silence or violence signals (lost safety), not only what to spot.
- `crucial-conversations-06`: now names the victim, villain and helpless stories, so it stands alone.
- `crucial-conversations-07`: "tell your story as a story" was cryptic. Now: "To raise a risky concern, share facts first, then your tentative conclusion, ask their view, and invite them to challenge it."
- `difficult-conversations-09`: "never to change them" became "not to change them" (less absolute, same meaning).

Explanations fixed (5):
- `the-next-conversation-04`, `-13`, `-15`: each opened with a sentence fragment, which is now a full sentence.
- `the-next-conversation-07` (171 words, now 151): removed a sentence on mild rude comments that repeats `the-next-conversation-05`.
- `the-next-conversation-12` (171 words, now within 160): removed one redundant sentence and tightened the presence and purpose sentence.

Every other insight passed. All takeaways are 10 to 22 words, all explanations are 160 words or fewer, techniques and frameworks have 3 to 7 steps, and mental models have none or a few.

## 4. Related links added to `data/learning-path.json` (52 groups: 44 complementary, 8 tension)

Complementary:
- crucial-conversations-05 + difficult-conversations-07 + nonviolent-communication-10 (three ways to work back from a strong feeling)
- crucial-conversations-06 + difficult-conversations-03 + the-next-conversation-01 + how-to-know-a-person-06 (curiosity about the other person's story)
- crucial-conversations-06 + think-faster-talk-smarter-16 (CLEAR borrows the villain-story question)
- crucial-conversations-06 + difficult-conversations-06 (your role, the contribution map)
- difficult-conversations-05 + connect-03 (intent and impact, original and core)
- difficult-conversations-05 + crucial-conversations-04 (misread intent, contrasting)
- difficult-conversations-07 + nonviolent-communication-03 + connect-06 (feelings, not disguised judgments)
- nonviolent-communication-01 + crucial-conversations-07 + connect-04 + gottman-seven-principles-01 (scripts for raising a concern)
- the-next-conversation-15 + nonviolent-communication-01
- nonviolent-communication-02 + connect-04
- the-next-conversation-13 + difficult-conversations-10 + crucial-conversations-04 (openings)
- the-next-conversation-16 + connect-04 (no praise sandwich)
- crucial-conversations-03 + how-to-know-a-person-12 + supercommunicators-11 (safety before substance)
- the-next-conversation-14 + difficult-conversations-08 + nonviolent-communication-05 + connect-07 (receiving criticism)
- crucial-conversations-01 + difficult-conversations-09 + the-next-conversation-02 + talk-wood-brooks-12 (goals before a hard talk)
- difficult-conversations-04 + think-faster-talk-smarter-16 ("and" not "but")
- difficult-conversations-04 + crucial-conversations-01 (refuse either-or)
- difficult-conversations-02 + supercommunicators-03 (learning conversation, original and later)
- difficult-conversations-01 + supercommunicators-01 + talk-wood-brooks-14 (layered models of a hard conversation)
- difficult-conversations-06 + connect-08
- crucial-conversations-08 + nonviolent-communication-07 + supercommunicators-07 (reflecting back)
- nonviolent-communication-07 + high-dillard-2012-01 + connect-09 (empathy before advice)
- difficult-conversations-12 + kluger-listening-2024-02
- crucial-conversations-02 + ury-positive-no-02 (silence and violence, the three-A trap)
- nonviolent-communication-04 + fisher-ury-getting-to-yes-01 (needs and interests)
- nonviolent-communication-06 + connect-15; nonviolent-communication-06 + overall-mcnulty-2017-02; nonviolent-communication-11 + overall-mcnulty-2017-02 (coercion buys compliance, not change)
- the-next-conversation-04 + think-faster-talk-smarter-02 + kross-2014-01 (breath and self-talk)
- the-next-conversation-03 + gottman-seven-principles-03 (ignition and flooding)
- the-next-conversation-11 + givi-kirk-2024-01
- the-next-conversation-12 + connect-13
- the-next-conversation-08 + lewicki-apologies-2016-01 + think-faster-talk-smarter-12 (apologies, giving and receiving)
- the-next-conversation-06 + guyer-vocal-confidence-01
- the-next-conversation-10 + talk-wood-brooks-09
- crucial-conversations-11 + rogelberg-meetings-02; crucial-conversations-12 + mroz-allen-2018-meetings-01; crucial-conversations-13 + rogelberg-meetings-05
- crucial-conversations-09 + connect-05
- nonviolent-communication-13 + supercommunicators-11
- talk-like-ted-07 + minto-pyramid-principle-01 + made-to-stick-03
- talk-like-ted-04 + communicate-with-mastery-20; talk-like-ted-05 + made-to-stick-05; talk-like-ted-01 + made-to-stick-02

Tension:
- crucial-conversations-07 + nonviolent-communication-02 (state your tentative conclusion versus strip evaluations and state needs)
- the-next-conversation-16 + difficult-conversations-10 (lead with the point versus open with the neutral third story)
- the-next-conversation-16 + baile-spikes-2000-01 (skip the cushion versus check what they already know first)
- the-next-conversation-11 + ury-positive-no-01 (a bare no versus Yes, No, Yes with an alternative)
- nonviolent-communication-12 + talk-wood-brooks-10 (no trait praise versus give the compliment you are holding back)
- the-next-conversation-07 + fisher-ury-getting-to-yes-06 (confront an insult versus redirect attacks onto the problem)
- talk-like-ted-03 + braddock-dillard-2016-01 (emotion-led persuasion versus modest measured effects of stories)
- talk-like-ted-04 + improv-wisdom-02 (rehearse heavily versus drop the script)

All 52 groups are new; none duplicates an existing related link.

Convergent concepts:
- New ids added to 14 existing concepts: Feedback: behavior and impact; A learning stance in disagreement; Looping and paraphrasing; Apologize specifically; Match the kind of conversation; Make stories and specifics do the work; Reusable message structures; Lead with the core point; Practice, record and reflect; Raise small issues early; Interests over positions; Express appreciation; Presence and inquiry before advice; Pushing hardens resistance. The feedback concept's disagreement note now records the STATE versus NVC difference.
- 2 new concepts: "Separate what happened from the story you tell about it" (connect-03, crucial-conversations-05, -06, difficult-conversations-05, -07, nonviolent-communication-02, -10, the-next-conversation-01) and "Steady your sense of self before taking in criticism" (difficult-conversations-08, the-next-conversation-14, nonviolent-communication-05, connect-07, think-faster-talk-smarter-05). Both are rated Medium.

## 5. Learning path (12 added; the path now holds 141 insights)

| Stage | Added (position) | Book |
|---|---|---|
| 2 Listening | `nonviolent-communication-07` (after inquiry before advice, `connect-09`) | NVC |
| 4 Clarity | `talk-like-ted-07` (after the pyramid, `minto-pyramid-principle-01`) | TED |
| 6 Difficult | `the-next-conversation-14` (after `connect-07`, receiving feedback) | TNC |
| 6 Difficult | `difficult-conversations-02`, `difficult-conversations-01`, `crucial-conversations-05` (after the voice research, `morrison-2014-voice-01`: stance, map, then facts versus story) | DC, DC, CC |
| 6 Difficult | `the-next-conversation-13` (after real feelings, `connect-06`: frame the opening) | TNC |
| 6 Difficult | `crucial-conversations-07`, `nonviolent-communication-01` (after behavior plus impact, `connect-04`) | CC, NVC |
| 6 Difficult | `crucial-conversations-03` (after receptiveness, `talk-wood-brooks-09`, before group norms) | CC |
| 6 Difficult | `the-next-conversation-12` (after `connect-13`, boundaries) | TNC |
| 7 Mastery | `talk-like-ted-04` (after vocal confidence, `guyer-vocal-confidence-01`) | TED |

By book: Difficult Conversations 2, Crucial Conversations 3, Nonviolent Communication 2, The Next Conversation 3, Talk Like TED 2. Each item is placed after the entries it depends on. For example, STATE comes after Master My Stories and after behavior plus impact. The rationales for Stages 2, 4, 6 and 7 were updated to mention the additions.

## 6. Situation playbooks (`data/situations.json`)

New ids were added to a step only where they sharpen it. A sentence was added to that step's `detail` so the reader sees what the insight contributes. Each playbook's `insight_ids` list was kept in sync with its steps (the build and a check script confirm it).

| Playbook | Step | Added |
|---|---|---|
| Giving critical feedback to a peer | Separate what they did from your guesses | crucial-conversations-05 |
| | Set up a private conversation with goodwill | the-next-conversation-13, crucial-conversations-04 |
| | Name the behavior and your real feeling | nonviolent-communication-02 |
| | Agree on a small experiment | crucial-conversations-12 |
| Receiving harsh feedback | Steady your body | the-next-conversation-14, difficult-conversations-08 |
| | Listen for the bottom line | nonviolent-communication-05 |
| | Accept the impact as real | difficult-conversations-05 |
| Saying no to extra work | Say the no plainly, then offer an alternative | the-next-conversation-11 (bare no only when nothing needs negotiating; the tension is recorded in `evidence_note`) |
| Setting a boundary with a family member | State the limit directly | the-next-conversation-12 |
| | Hold steady | the-next-conversation-12 (follow through on the consequence; `evidence_note` updated) |
| Delivering bad news to your manager | Match the format / ask for a private slot | the-next-conversation-16 |
| | Signal the news, then say it plainly | the-next-conversation-16 |
| A tense conflict with your partner | Be direct about the problem | nonviolent-communication-01 |
| | Take a real break if either of you floods | the-next-conversation-04 |
| | Agree a step and a time to revisit | nonviolent-communication-04 |
| Presenting to executives | One-sentence core | talk-like-ted-07 |
| | Rehearse the first minute and do a dry run | talk-like-ted-04 |
| Giving a toast | Choose one concrete story | talk-like-ted-03 |
| | Rehearse the opening | talk-like-ted-04 |
| Talking across a political disagreement | Aim for understanding | the-next-conversation-10 |
| | Speak with visible openness | the-next-conversation-10 |
| Handling a hostile question in Q&A | Breathe and hear the whole question | the-next-conversation-05 |
| Running a meeting that wanders | Agenda as questions | crucial-conversations-11 |
| | Close each question with an owner and a date | crucial-conversations-12 |
| Supporting a grieving friend | Name the feeling | nonviolent-communication-07 |

Deliberately not added: `talk-like-ted-03` (open with a story before the data) to Presenting to executives, because executives want the answer first; the playbook already leads with the answer.

New playbook (1): **A heated disagreement with a coworker** (`heated-disagreement-with-a-coworker`, category `difficult`, professional). No existing playbook covered an in-the-moment conflict at work; the only conflict playbooks were for partners and politics. It has seven steps:
1. Catch your own ignition: the-next-conversation-04, -03, gottman-seven-principles-03
2. Check your story against the facts: crucial-conversations-05, -06
3. Decide what you really want: crucial-conversations-01, difficult-conversations-09
4. Restore safety: crucial-conversations-03, -04, -02
5. Get curious about their story and say it back: difficult-conversations-03, crucial-conversations-08, supercommunicators-07
6. Share your view as your view: crucial-conversations-07, the-next-conversation-15
7. Map contributions and agree who does what by when: difficult-conversations-06, crucial-conversations-12

It also includes example wording, pitfalls and an evidence note: all Medium practitioner frameworks, with independent support only for some underlying ideas.

## 7. Build and smoke test

- `python3 scripts/build_library.py`: `Wrote artifact/library.json: 70 sources, 306 insights, 218 supporting links, 28 situations`. No ERROR or WARNING lines. No em or en dashes.
- Extra checks: every id in related links, convergent concepts, the learning path and playbooks exists. Every playbook's `insight_ids` matches the union of its step ids. No reference to `crucial-conversations-10` remains outside the merge notes.
- `node scripts/smoke_test.js http://localhost:8765/index.html`: desktop and phone both `ok: true` (306 insights and 306 rows, 70 sources and 70 cards, 28 situations and 28 cards, 7 stages, 8 home hits, no horizontal overflow). Errors: none.

Not done (out of scope for this run): publishing (Step 8.3), and the PROGRESS.md update and commit (Step 8.4).
