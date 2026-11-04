# Stage 3b extraction brief (shared)

User selected all candidates scoring 7 or higher (56 sources). Extract their insights so they can join the library.

## Before you start
- Working directory: /home/user/comm-models. Read docs/stage1-schema.md (output schema and the ONLY valid category and subcategory ids), docs/taxonomy.md, and data/stage3/candidates-<your-category>.json (the earlier assessment of your sources).
- Load ALL existing insights so you do not duplicate them: python3 -c "import json,glob;[print(i['id'],'|',i['name'],'|',i['explanation'][:160]) for f in sorted(glob.glob('data/stage1/*.json')+glob.glob('data/stage3/extracted/*.json')) for i in json.load(open(f))['insights']]"

## How many insights
- Extract every relevant, high-quality insight a source genuinely contributes. No fixed count: a paper might give 1, a book might give 8. Use high-confidence judgement.
- Do NOT add an insight that restates an existing one. If a source mainly strengthens, corrects, or qualifies an existing insight, record it under supports_existing instead (see below). Only add a new insight when it adds a distinct idea, technique, or a materially different recommendation.
- For research papers, an insight must state the practical takeaway for an ordinary professional, plus the finding behind it and its limits.

## Output: one file per source
data/stage3/extracted/<source_id>.json, using the stage1 schema exactly, with these additions:
- book.source_type: book | peer-reviewed paper | meta-analysis | review article | practitioner article
- book.core: false
- top-level supports_existing: [{"insight_id": "existing id", "relation": "supports | qualifies | contradicts", "note": "one or two sentences: what this source adds to that insight, with the finding"}]
- top-level verification: {"date": "2026-11-04", "sources_read": [urls], "still_unverified": []}
- Insight ids: <source_id>-01, -02, ... source_id is short kebab-case (for example rogers-busy-readers, giurge-bohns-2021).
- If a source contributes no new insight, still write the file with insights: [] and its supports_existing entries.

## Sources and evidence
- Read the actual source where legally available: open-access PDFs, publisher previews, author sites, abstracts, reputable summaries and interviews. The WebFetch tool does not work here. Use WebSearch, and read pages with plain curl through Bash (curl -sS -L -m 20 URL) with no custom user-agent header. Save downloads in a new directory under /tmp/claude-0/-home-user/1ec87173-3360-5f6f-b529-8b6cc7d13422/scratchpad/stage3b-<category>/ and extract text with python3 -I. Skip sites returning 403 or captchas. Never use pirated copies or paywall mirrors.
- Confidence: High = replicated research or strong consensus; Medium = credible expert or case evidence; Low = plausible but thinly supported. Flag single-anecdote, pop-psychology, unreplicated, contested, not-confirmed-in-book as appropriate. Integrity: if a supporting paper lists Francesca Gino as coauthor, keep it with an integrity note.
- Scope: US context only; do not add cross-cultural material. Known unfilled gaps (status updates, aging parents) stay gaps: do not write thin insights to fill them.

## Rules
- Original paraphrase only; never quote more than a short phrase (under 10 words).
- Worked examples are your own realistic scenarios, professional and personal where it fits.
- No em dashes (U+2014), en dashes (U+2013), or emojis anywhere.
- Do not fabricate findings, numbers, or citations. Unverified details go in still_unverified.
- Validate every file with python3 json.load, check category ids against docs/stage1-schema.md, and grep for U+2014 and U+2013.
- Reply with a short summary: per source, new insights added (names, confidence) and supports_existing count; and anything you could not access.

## Assignments (by category agent)

### conversations (7)
- The state of research on leader humor (Dejun Tony Kong, Cecily D. Cooper, John J. Sosik, 2019; review article)
- A meta-analysis of positive humor in the workplace (Jessica Mesmer-Magnus, David J. Glew, Chockalingam Viswesvaran, 2012; meta-analysis)
- The Extended Transportation-Imagery Model: A Meta-Analysis of the Antecedents and Consequences of Consumers' Narrative Transportation (Tom van Laer, Ko de Ruyter, Luca M. Visconti et al., 2014; meta-analysis)
- Meta-analytic evidence for the persuasive effect of narratives on beliefs, attitudes, intentions, and behaviors (Kurt Braddock, James Price Dillard, 2016; meta-analysis)
- The Liking Gap in Conversations: Do People Like Us More Than We Think? (Erica J. Boothby, Gus Cooney, Gillian M. Sandstrom et al., 2018; peer-reviewed paper)
- The Surprise of Reaching Out: Appreciated More Than We Think (Peggy J. Liu, SoYon Rim, Lauren Min et al., 2023; peer-reviewed paper)
- Quantifying collective intelligence in human groups (Christoph Riedl, Young Ji Kim, Pranav Gupta et al., 2021; meta-analysis)

### difficult (5)
- SPIKES: A Six-Step Protocol for Delivering Bad News: Application to the Patient with Cancer (Walter F. Baile, Robert Buckman, Renato Lenzi et al., 2000; peer-reviewed paper)
- An Exploration of the Structure of Effective Apologies (Roy J. Lewicki, Beth Polin, Robert B. Lount Jr., 2016; peer-reviewed paper)
- Saying No: The Negative Ramifications From Invitation Declines Are Less Severe Than We Think (Julian Givi, Colleen P. Kirk, 2024; peer-reviewed paper)
- Pushing in the Dark: Causes and Consequences of Limited Self-Awareness for Interpersonal Assertiveness (Daniel R. Ames, Abbie S. Wazlawek, 2014; peer-reviewed paper)
- The Power of a Positive No: How to Say No and Still Get to Yes (William Ury, 2007; book)

### foundations (7)
- Psychological Interventions for the Fear of Public Speaking: A Meta-Analysis (Omid V. Ebrahimi, Stale Pallesen, Robin M. F. Kenter et al., 2019; meta-analysis)
- A racing heart, rattling knees, and ruminative thoughts: Defining, explaining, and treating public speaking anxiety (Graham D. Bodie, 2010; review article)
- Optimizing stress responses with reappraisal and mindset interventions: an integrated model (Jeremy P. Jamieson, Alia J. Crum, J. Parker Goyer et al., 2018; review article)
- Self-talk as a regulatory mechanism: How you do it matters (Ethan Kross, Emma Bruehlman-Senecal, Jiyoung Park et al., 2014; peer-reviewed paper)
- The illusion of transparency and the alleviation of speech anxiety (Kenneth Savitsky, Thomas Gilovich, 2003; peer-reviewed paper)
- Speakers' overestimation of their effectiveness (Boaz Keysar, Anne S. Henly, 2002; peer-reviewed paper)
- A meta-analysis of how signaling affects learning with media (Sascha Schneider, Maik Beege, Steve Nebel et al., 2018; meta-analysis)

### influence (7)
- Influence, New and Expanded: The Psychology of Persuasion (Robert B. Cialdini, 2021; book)
- The Door-in-the-Face Persuasive Message Strategy: A Meta-Analysis of the First 35 Years (Thomas Hugh Feeley, Ashley E. Anker, Ariel M. Aloe, 2012; meta-analysis)
- Influence Without Authority (3rd edition) (Allan R. Cohen, David L. Bradford, 2017; book)
- Motivational Interviewing: Helping People Change and Grow (4th edition), with the Lundahl et al. (2010) meta-analysis (William R. Miller, Stephen Rollnick, 2023; book)
- The Catalyst: How to Change Anyone's Mind (Jonah Berger, 2020; book)
- Reducing Exclusionary Attitudes Through Interpersonal Conversation: Evidence From Three Field Experiments (Joshua L. Kalla, David E. Broockman, 2020; peer-reviewed paper)
- Moral reframing: A technique for effective and persuasive communication across political divides (Matthew Feinberg, Robb Willer, 2019; review article)

### personal-life (7)
- The Seven Principles for Making Marriage Work (revised edition) (John M. Gottman, Nan Silver, 2015; book)
- What do you do when things go right? The intrapersonal and interpersonal benefits of sharing positive events (Shelly L. Gable, Harry T. Reis, Emily A. Impett et al., 2004; peer-reviewed paper)
- A Review and Meta-Analysis of Person-Centered Messages and Social Support Outcomes (Andrew C. High, James Price Dillard, 2012; meta-analysis)
- How many hours does it take to make a friend? (Jeffrey A. Hall, 2019; peer-reviewed paper)
- Platonic: How the Science of Attachment Can Help You Make and Keep Friends (Marisa G. Franco, 2022; book)
- Skilled Support Within Intimate Relationships (Eshkol Rafaeli, Marci E. J. Gleason, 2009; review article)
- What type of communication during conflict is beneficial for intimate relationships? (Nickola C. Overall, James K. McNulty, 2017; review article)

### professional (6)
- The Surprising Science of Meetings: How You Can Lead Your Team to Peak Performance (Steven G. Rogelberg, 2019; book)
- Do We Really Need Another Meeting? The Science of Workplace Meetings (Joseph E. Mroz, Joseph A. Allen, Dana C. Verhoeven et al., 2018; review article)
- Getting to Yes: Negotiating Agreement Without Giving In (Roger Fisher, William Ury, Bruce Patton, 1981; book)
- The Mind and Heart of the Negotiator (7th edition) (Leigh L. Thompson, 2020; book)
- Managing Your Boss (John J. Gabarro, John P. Kotter, 1980; practitioner article)
- Employee Voice and Silence (Elizabeth W. Morrison, 2014; review article)

### public-speaking (6)
- Nonverbal Overload: A Theoretical Argument for the Causes of Zoom Fatigue (Jeremy N. Bailenson, 2021; peer-reviewed paper)
- The Fatiguing Effects of Camera Use in Virtual Meetings: A Within-Person Field Experiment (Kristen M. Shockley, Allison S. Gabriel, Daron Robertson et al., 2021; peer-reviewed paper)
- The Economic and Interpersonal Consequences of Deflecting Direct Questions (T. Bradford Bitterly, Maurice E. Schweitzer, 2020; peer-reviewed paper)
- The Artful Dodger: Answering the Wrong Question the Right Way (Todd Rogers, Michael I. Norton, 2011; peer-reviewed paper)
- Speech Rate, Intonation, and Pitch: Investigating the Bias and Cue Effects of Vocal Confidence on Persuasion (Joshua J. Guyer, Leandre R. Fabrigar, Thomas I. Vaughan-Johnston, 2019; peer-reviewed paper)
- Dominance and Prestige: Meta-Analytic Review of Experimentally Induced Body Position Effects on Behavioral, Self-Report, and Physiological Dependent Variables (Robert Körner, Lukas Röseler, Astrid Schütz et al., 2022; meta-analysis)

### relationships (7)
- Nonverbal Communication (Judith A. Hall, Terrence G. Horgan, Nora A. Murphy, 2019; review article)
- Accuracy of Deception Judgments (Charles F. Bond Jr., Bella M. DePaulo, 2006; meta-analysis)
- A Meta-analytic Systematic Review and Theory of the Effects of Perceived Listening on Work Outcomes (Avraham N. Kluger, Michael Lehmann, Herman Aguinis et al., 2024; meta-analysis)
- High-quality listening behaviors linked to social connection between strangers (Taylor N. West, Sara Huston, Kylie R. Chandler et al., 2025; peer-reviewed paper)
- Dormant Ties: The Value of Reconnecting (Daniel Z. Levin, Jorge Walter, J. Keith Murnighan, 2011; peer-reviewed paper)
- A Causal Test of the Strength of Weak Ties (Karthik Rajkumar, Guillaume Saint-Jacques, Iavor Bojinov et al., 2022; peer-reviewed paper)
- Social Chemistry: Decoding the Patterns of Human Connection (Marissa King, 2021; book)

### written-digital (4)
- Writing for Busy Readers: Communicate More Effectively in the Real World (Todd Rogers, Jessica Lasky-Fink, 2023; book)
- You don't need to answer right away! Receivers overestimate how quickly senders expect responses to non-urgent work emails (Laura M. Giurge, Vanessa K. Bohns, 2021; peer-reviewed paper)
- Egocentrism over e-mail: Can we communicate as well as we think? (Justin Kruger, Nicholas Epley, Jason Parker et al., 2005; peer-reviewed paper)
- The Pyramid Principle: Logic in Writing and Thinking (Barbara Minto, 1987; book)
