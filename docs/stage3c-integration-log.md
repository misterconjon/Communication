# Stage 3c integration log

Date: 2026-11-04. Inputs: 137 core insights (`data/stage1/`) and 110 extracted insights from 56 added sources (`data/stage3/extracted/`). After integration the library holds **246 insights** (137 core, 109 added) from 65 sources. `python3 scripts/build_library.py` runs with no errors or warnings.

## 1. De-duplication

Method: every added insight was compared with every other added insight and with the 137 core insights by name, explanation, steps, when-to-use and underlying research. An insight was merged only when it carried the same core idea and the same practical advice as another. Where two insights shared a theme but differed in mechanism, evidence or what the reader should do, both were kept and linked.

### 1.1 Merges (1)

| Removed id | Kept id | Reason |
|---|---|---|
| `ury-positive-no-03` (Back Your No With a Plan B) | `fisher-ury-getting-to-yes-05` (Know Your BATNA Before You Negotiate) | Same core idea and advice: know your best alternative that does not depend on the other side's agreement before you negotiate or refuse. Getting to Yes is the original source of the concept (Ury coauthored both books and describes Plan B as BATNA applied to refusals), and the kept entry is High confidence with research support; the removed entry was Medium and not separately tested. Its unique detail (the interest, power and right questions; keep Plan B in reserve; state consequences as a warning, not a threat) is carried over as a `supports` entry in `ury-positive-no.json`. The kept insight is already tagged `difficult/saying-no`. No other `supports_existing` entry pointed to the removed id. |

### 1.2 Candidate overlaps reviewed and kept as separate insights

| Pair | Decision | Why they are not duplicates |
|---|---|---|
| `levin-dormant-ties-2011-01` / `liu-2023-01` | complementary | Levin: reconnect for advice, because dormant ties give novel ideas efficiently. Liu: reach out with no request, because recipients appreciate it more than senders expect. Different purpose, mechanism and advice. |
| `boothby-2018-01` / `franco-platonic-01` | complementary | Boothby is the original liking-gap research (High). Franco cites it as one of three parts of a friendship-making technique (repeated contact, assume liking, initiate). |
| `boothby-2018-01` / `how-to-know-a-person-04` | complementary | Both show miscalibrated social forecasts, but about different things (how much you were liked versus how awkward deep talk will be). |
| `berger-catalyst-01` / `miller-rollnick-mi-2023-01` | complementary | Berger gives a diagnostic of five barriers (REDUCE); MI is a questioning method that elicits the person's own reasons. |
| `berger-catalyst-04` / `feeley-anker-aloe-2012-01` | tension | Berger: ask for less and move in steps. Door-in-the-face: ask for more, then retreat. The meta-analysis shows the retreat wins verbal yeses but little follow-through. |
| `cohen-bradford-influence-without-authority-01` / `connect-12`, `gabarro-kotter-managing-your-boss-01` | complementary | Exchange of currencies with people you cannot direct, versus balance of influence in a relationship, versus mutual dependence with your boss. |
| `kluger-listening-2024-02` / `kalla-broockman-2020-01`, `miller-rollnick-mi-2023-01` | complementary | Listening alone loosens views (lab), trading stories shifts attitudes (field), and eliciting change talk drives behavior change (clinical). Grouped in a new convergent concept. |
| `bailenson-zoom-fatigue-01` / `shockley-camera-fatigue-01` | complementary | Bailenson: four causes of fatigue and personal settings to fix them. Shockley: field experiment supporting camera-optional norms for hosts. |
| `bailenson-zoom-fatigue-01` / `communicate-with-mastery-12` | tension | Schramm urges amplifying signals on video; Bailenson argues that the effort of exaggerated cues is itself a cause of fatigue. |
| `jamieson-2018-01` / `think-faster-talk-smarter-03` | complementary | Same family (reappraise arousal rather than suppress it), but Jamieson adds the challenge-versus-threat mechanism, the resources check and a stress mindset, and does not rely on the excitement label. Kept both; the convergent concept records the overlap. |
| `bodie-2010-01` / `think-faster-talk-smarter-02` | complementary | Abrahams' ABCs are symptom categories with quick fixes; Bodie matches treatment families to the source and adds skills training as an anxiety treatment. |
| `kruger-epley-2005-01` / `communicate-with-mastery-09`, `supercommunicators-12` | complementary | The research behind both core insights, plus a distinct technique (reread in the opposite voice; move tone-dependent content to voice). |
| `lewicki-apologies-2016-01` / `think-faster-talk-smarter-12` | complementary | AAA is a ready script; Lewicki ranks components by tested effect and says to drop the forgiveness request. |
| `guyer-vocal-confidence-01` / `communicate-with-mastery-13` | tension | Agree on falling intonation and lower pitch; disagree on pace (Guyer: brisk; Schramm: slower). |
| `rogers-busy-readers-04` / `schneider-2018-signaling-01` | complementary | Both say to mark only what matters, but one is about skimming busy readers (field tests), the other about comprehension in explanations, diagrams and spoken signposting (learning meta-analysis). |
| `rogers-norton-artful-dodger-01` / `think-faster-talk-smarter-11` | complementary | Research on why restating the question and fluency matter, versus the ADD answer structure. |
| `miller-rollnick-mi-2023-02` / `connect-09` | complementary | Inquiry before advice versus how to give advice once it is wanted (ask, offer, ask). |
| `overall-mcnulty-2017-01` / `gottman-seven-principles-01` | tension | Gentle start-up versus evidence that direct opposition produces change for serious problems. |
| `franco-platonic-02` / `connect-05` | complementary | Raise issues early (timing) versus how to open with a friend (lead with value). |
| `gottman-seven-principles-04` / `connect-14` | complementary | Small repairs mid-conflict backed by everyday goodwill, versus repairing a major rupture. |
| `berger-catalyst-06` / `cialdini-influence-2021-02` | complementary | Multiple independent corroborating voices versus descriptive peer norms. |
| `thompson-mind-heart-negotiator-01` / `fisher-ury-getting-to-yes-03` | complementary | Test the fixed-pie assumption (research) versus separate inventing from deciding (method). |
| `mesmer-magnus-2012-01` / `humor-seriously-14` | complementary | Coping humor aimed at the situation (independent meta-analysis) versus leaders shaping a levity culture. |

## 2. Related-insight links added to `data/learning-path.json`

Complementary (37): levin-dormant-ties-2011-01 + liu-2023-01; levin-dormant-ties-2011-01 + rajkumar-weak-ties-2022-01; boothby-2018-01 + franco-platonic-01; boothby-2018-01 + how-to-know-a-person-04; hall-2019-01 + franco-platonic-01; berger-catalyst-01 + miller-rollnick-mi-2023-01; berger-catalyst-04 + cialdini-influence-2021-04; berger-catalyst-06 + cialdini-influence-2021-02; cohen-bradford-influence-without-authority-01 + connect-12; cohen-bradford-influence-without-authority-01 + gabarro-kotter-managing-your-boss-01; cialdini-influence-2021-01 + king-social-chemistry-02; kluger-listening-2024-02 + kalla-broockman-2020-01; kluger-listening-2024-02 + miller-rollnick-mi-2023-01; miller-rollnick-mi-2023-02 + connect-09; miller-rollnick-mi-2023-03 + fisher-ury-getting-to-yes-06; bailenson-zoom-fatigue-01 + shockley-camera-fatigue-01; jamieson-2018-01 + think-faster-talk-smarter-03; bodie-2010-01 + think-faster-talk-smarter-02; savitsky-gilovich-2003-01 + think-faster-talk-smarter-02; kruger-epley-2005-01 + communicate-with-mastery-09; kruger-epley-2005-01 + supercommunicators-12; keysar-henly-2002-01 + made-to-stick-01; lewicki-apologies-2016-01 + think-faster-talk-smarter-12; gottman-seven-principles-03 + think-faster-talk-smarter-16; gottman-seven-principles-04 + connect-14; franco-platonic-02 + connect-05; high-dillard-2012-01 + how-to-know-a-person-10; mesmer-magnus-2012-01 + humor-seriously-14; rogers-busy-readers-04 + schneider-2018-signaling-01; rogers-norton-artful-dodger-01 + think-faster-talk-smarter-11; thompson-mind-heart-negotiator-01 + fisher-ury-getting-to-yes-03; minto-pyramid-principle-02 + think-faster-talk-smarter-07; mroz-allen-2018-meetings-01 + rogelberg-meetings-02; braddock-dillard-2016-01 + van-laer-2014-01; feinberg-willer-2019-01 + made-to-stick-11; givi-kirk-2024-01 + ury-positive-no-01; morrison-2014-voice-03 + gabarro-kotter-managing-your-boss-03.

Tension (7): berger-catalyst-04 + feeley-anker-aloe-2012-01 (ask for less versus ask big then retreat); bailenson-zoom-fatigue-01 + communicate-with-mastery-12 (amplify cues versus reduce cue effort); guyer-vocal-confidence-01 + communicate-with-mastery-13 (brisk versus slower pace); overall-mcnulty-2017-01 + gottman-seven-principles-01 (direct opposition versus gentle start-up); gable-2004-01 + franco-platonic-03 (enthusiastic response versus honest mixed feelings to a friend's good news); high-dillard-2012-01 + rafaeli-gleason-2009-02 (name feelings explicitly versus keep support invisible); braddock-dillard-2016-01 + made-to-stick-12 (stories have small effects versus stories as a powerful tool).

## 3. Learning-path additions (37; path now 129 insights)

| Stage | Added (in path order) | Count |
|---|---|---|
| 1 Foundations | `savitsky-gilovich-2003-01` (after calming the body), `ebrahimi-2019-01` (after acting before ready) | 2 |
| 2 Listening | `kluger-listening-2024-01` (after attention), `bond-depaulo-2006-01`, `hall-nonverbal-2019-01` (after reading people less accurately than you think) | 3 |
| 3 Conversation | `boothby-2018-01` (after deep talk), `gottman-seven-principles-02` (after the levity check), `gable-2004-01`, `liu-2023-01` (after appreciation, before ending) | 4 |
| 4 Clarity | `keysar-henly-2002-01` (after curse of knowledge), `minto-pyramid-principle-01` (after parachute in), `rogers-busy-readers-02`, `rogers-busy-readers-03`, `kruger-epley-2005-01` (after ABC writing), `giurge-bohns-2021-01` (after pause-verify-iterate) | 6 |
| 5 Influence | `van-laer-2014-01` (after stories), `cialdini-influence-2021-01`, `cohen-bradford-influence-without-authority-01` (after credibility), `feinberg-willer-2019-01`, `miller-rollnick-mi-2023-01`, `kalla-broockman-2020-01` (after identity, closing the stage) | 6 |
| 6 Difficult | `morrison-2014-voice-01` (after pinches), `gottman-seven-principles-01`, `overall-mcnulty-2017-01` (after find the layer), `baile-spikes-2000-01` (after preparing for the hardest conversations), `lewicki-apologies-2016-01` (after AAA), `ury-positive-no-01`, `givi-kirk-2024-01` (before boundaries), `high-dillard-2012-01` (before presence over fixing) | 8 |
| 7 Mastery | `rogers-norton-artful-dodger-01` (after ADD), `guyer-vocal-confidence-01` (after delivery recipe), `mroz-allen-2018-meetings-01`, `rogelberg-meetings-05`, `bailenson-zoom-fatigue-01` (after group leadership), `fisher-ury-getting-to-yes-01`, `thompson-mind-heart-negotiator-01`, `fisher-ury-getting-to-yes-05` (before the canvas) | 8 |

Of the 37, 16 are High confidence; the rest are Medium and were chosen to fill a documented gap. Rationales were updated for all seven stages, and purposes for Stages 3 to 7. Stage 3 now lists `personal-life` among its categories.

## 4. Convergent concepts

New (6): "Pushing hardens resistance: draw out their reasons and listen" (High); "Interests over positions, and the pie is rarely fixed" (High); "Reciprocity and exchange drive influence without authority" (Medium); "Busy readers: fewer ideas, one ask, visible structure" (High); "Good meetings are designed, not just run" (Medium, partly lineage); "In close relationships, be direct about problems but gentle with the person" (Medium, with an internal tension).

Extended with added-source ids: Social fears and self-perceptions are miscalibrated; Reframe anxiety rather than suppress it; Make stories and specifics do the work (now High); Apologize specifically and own it; Presence and inquiry before advice when someone is struggling (now High); Identity shapes what people hear; Lead with the core point and cut the preamble (now High); Reusable message structures; Ask rather than infer other minds; Looping and paraphrasing; Express appreciation more than feels necessary; Raise small issues early and make expectations explicit; Practice, record and reflect.

## 5. Gap status

| Gap | Status | Filled by |
|---|---|---|
| written-digital/async | partly filled | giurge-bohns-2021-01, rogers-busy-readers-01, -03, kruger-epley-2005-01 (documentation culture still thin) |
| written-digital/proposals-memos | filled | minto-pyramid-principle-01, -02, -03, rogers-busy-readers-02, -04 |
| written-digital/executive-writing | filled | minto-pyramid-principle-01, -02, rogers-busy-readers-02, -05 |
| public-speaking/virtual | partly filled | bailenson-zoom-fatigue-01, shockley-camera-fatigue-01 (no virtual presenting guide) |
| written-digital/video-calls | filled | bailenson-zoom-fatigue-01, shockley-camera-fatigue-01 |
| difficult/saying-no | filled | ury-positive-no-01, -02, givi-kirk-2024-01, ames-wazlawek-2014-01, fisher-ury-getting-to-yes-05 |
| influence/reciprocity | filled | cialdini-influence-2021-01, cohen-bradford-influence-without-authority-01, -02, feeley-anker-aloe-2012-01, king-social-chemistry-02 |
| conversations/introductions | partly filled | boothby-2018-01, liu-2023-01, cialdini-influence-2021-03, rogelberg-meetings-06 |
| difficult/bad-news | filled | baile-spikes-2000-01, -02, morrison-2014-voice-03, gabarro-kotter-managing-your-boss-03 (layoff communication not covered) |
| difficult/boundaries | filled | ury-positive-no-01, givi-kirk-2024-01, ames-wazlawek-2014-01, -02 |
| personal-life/supporting-distress | filled | high-dillard-2012-01, rafaeli-gleason-2009-01, -02, baile-spikes-2000-01 |
| personal-life/friendships | filled | hall-2019-01, franco-platonic-01, -02, liu-2023-01, boothby-2018-01, gable-2004-02 |
| personal-life/family | partly filled | gottman-seven-principles-02, overall-mcnulty-2017-02, miller-rollnick-mi-2023-01, gable-2004-01 (no parenting source) |
| personal-life/partners | filled | gottman-seven-principles-01 to -05, overall-mcnulty-2017-01, -02, gable-2004-01 |
| professional/negotiation | filled | fisher-ury-getting-to-yes-01, -05, thompson-mind-heart-negotiator-01 to -04 |
| relationships/nonverbal | filled | bond-depaulo-2006-01, -02, hall-nonverbal-2019-01, guyer-vocal-confidence-01 |
| professional/meetings | filled | mroz-allen-2018-meetings-01, rogelberg-meetings-01, -02, -05, riedl-2021-01 |
| professional/status-updates | **unfilled (user decision)** | none; gabarro-kotter-managing-your-boss-03 and mroz-allen-2018-meetings-01 touch it as secondary tags |
| personal-life/family: aging parents | **unfilled (user decision)** | none; recorded as its own gap entry |
| public-speaking/qa | filled | rogers-norton-artful-dodger-01, -02, bitterly-schweitzer-deflection-01 |
| influence/framing | filled | feinberg-willer-2019-01, berger-catalyst-03, thompson-mind-heart-negotiator-02, cialdini-influence-2021-02 |
| conversations/humor | partly filled | mesmer-magnus-2012-01 (one correlational meta-analysis) |
| conversations/storytelling | filled | braddock-dillard-2016-01, van-laer-2014-01, kalla-broockman-2020-01 |

Each gap entry in `data/learning-path.json` now carries `status`, `filled_by` and, where useful, `status_note`.
