# REBUILD SPEC - Draft 10 (peak version)

REBUILD, do not polish. The user's feedback (essay-lab/feedback.md) rejects the current
structure's emphasis. Draft 9's mirror architecture is superseded by the "gap" motif + brand below.

## Read this before writing (in order)
1. essay-lab/feedback.md - THE operative directive (user voice notes + GPT conversation, 36KB, read all the way through)
2. essay-lab/materialv2.md - corrected ground truth (facts only, never invent)
3. fact-sheets/fact-sheet-polished.md - facts bank (22 markets, 10,200 sims, teacher quote, etc.)
4. drafts/essay-draft-9.md - the current best (603w, verified). Rebuild FROM it; it is not sacred.
5. essay-lab/09-famous-all-ivy-essays.md - READ MARTIN ALTENBURG'S ESSAY CAREFULLY (first 40 lines). It is the voice model: natural, unpolished, contradictory, sensory, never announces its conclusion.
6. essay-lab/10-ao-expert-analysis.md - Theme 8 = how AOs detect AI essays (flat rhythm, generic beats, over-optimization, absence of specificity, explicit moral endings). Write so no detector flags you.
7. essay-lab/08-accepted-essay-databases.md + 11-unresolved-struggle-essays.md - skim for natural-English calibration ("Breaking Into Cars", "Three Trees", CEG Prompt-3 essay).

## THE BRAND (this is the whole point - feedback.md lines 334-374, 620-660, 1566-1570)
NOT "kid who learned responsible AI use."
NOT "kid who overcame coding difficulties."
BRAND: **someone who compulsively reaches beyond what he can currently do, discovered both the
power and the danger of bridging that distance too quickly, and is learning to demand understanding
without losing the audacity to reach.**

The recurring motif IS THE GAP (feedback.md lines 682-694):
- Exam: gap between thought and code
- AI: bridge across the gap
- Misuse: hiding the gap
- Research: discovering another gap (knowing vs communicating to a particular audience)
- Peer review: someone else locating the gap
Never explain this motif out loud. Let the reader feel it.

## OPERATIVE CHANGES from feedback.md (cut / keep / rewrite)

### CUT (feedback.md lines 118-157, 202-207, user voice notes line 1)
- "Five of us were building something for the research club" - ALL of it (five of us / only one who knew / took the lead / wrote most of it)
- The whole "publish somewhere real" paragraph ("I told him I was going to publish somewhere real. I was seventeen...") - ALL of it. No defense, no competence-establishing right after failure.
- "I go back. I'm still going back." ending - CUT (user: "not something I would remember")
- The journal-submission tutorial details: scope mismatch → another journal → desk pass → structure as a process list. SHRINK to what each rejection did to thinking.

### KEEP + COMPRESS
- Exam opening (pens moving fast, pages flipped, nothing on yours, wanted to cry) but fold ¶2 (theory paper) INTO ¶1 in 15-25 words: "I could explain concepts. I couldn't make the code appear." (feedback 60-80)
- Brother moment = THE IGNITION, give him slightly MORE presence (feedback 84-97). User voice note: brother showed him a website "that could build stuff"; reaction: "Wait. I can tell it what I'm trying to make?" (Lovable UNNAMED - tools never named)
- "At what point does attention become too much and harm the market?" - KEEP EXACTLY (feedback 206-213)
- The fast, polite, generic rejection - KEEP but convert to the FIT insight: "I thought a good piece of work should speak for itself. It didn't." + McDonald's analogy IF it fits naturally (user's own image, keep close to his phrasing) (feedback 226-245)
- Second round: got the audience right, then someone interrogated HOW HE BUILT THE ARGUMENT - another layer, keep compressed (feedback 234-245)
- "The one thing I swore off in that exam hall is most of what I do now" - KEEP (user: "this is good")
- R&R: IMPROVE (feedback 248-279). "I'm answering them one at a time" is administrative. The reviewer is another version of the teacher: "Explain this." Except now he can. Show the reader the different questions he asks now ("What haven't I explained well enough that made this question possible?") - behavior, not announcement.

### REWRITE
- ¶4 overreach (feedback 100-116): the intellectual turn must be exact - "AI initially let you express things you understood but couldn't code. Eventually you realized it could also let you produce things you didn't understand at all." That's the essay's first major turn. "I used it for work I had no business attempting" is too weak.
- Teacher scene (feedback 118-157): brutally compressed. "Something happened. It came back flagged, high percentage. I told him the truth before he asked: it was mostly AI, and I hadn't tried. He didn't yell. He just looked at me a second too long and said he'd expected better. That was worse than yelling. If he'd asked me to explain my own paper, I would have had nothing to say." - "earned the right to call it mine" idea belongs here or right after (feedback 156).
- Gita (feedback 282-305): expand to 35-50 words, the RELATIONSHIP not the citation: "I'd heard it growing up, it didn't mean much to me then. Rejection changed what I understood it to mean." Verse itself: "you have a right to your actions, never to their fruits" (paraphrase, correct for a 17-year-old).
- Ending (feedback 308-332, 1388-1408): completely replaced. He still reaches too far - that's part of him. What changed: he no longer confuses reaching something with understanding it. DO NOT resolve the contradiction. No fake profundity. Final sentence must not be twice as poetic as the preceding 600 words. Leave cognitive residue - the idea extends past the page.

## HARD CONSTRAINTS (binding, unchanged)
1. Under 650 words; target 585-605.
2. Never name in the essay: the journal (Borsa Istanbul Review), quartile (Q1), tools (ChatGPT/Lovable), project names (GASI/NEXUS/ATLAS/Daedalus), the checker, the verse source (Bhagavad Gita stays generic - "a line I'd heard growing up"), the teacher's name, the brother's name (Krishna stays "my brother").
3. No em dashes anywhere - use " - " with spaces.
4. No AI-tell words: multifaceted, underscore, unwavering, pivotal, profound, transformative, resilience, passion, "this experience shaped who I am" constructions, "I realized/learned" pivots.
5. No manufactured texture - every concrete detail traces to materialv2.md / fact-sheet-polished.md / user's voice notes in feedback.md line 1. Known usable: twenty-two markets, seventeen, pens moving fast / pages flipped, "wrote whatever came into my mind" (user's exam memory), intense room full of peers, brother showing a build-site, McDonald's analogy, cold form-letter wording ("not a good match with the current scope").
6. Teacher = "he", counselor = "she" (if counselor appears at all - she may be cut entirely for space; brother can carry the ignition alone. Privilege the brother.)
7. Staccato short-sentence device: max 2-3 uses, teacher scene + one other moment only.
8. Verification PASS required after writing: python3 ~/.hermes/skills/productivity/university-application-writing/scripts/verify-essay-draft.py <your file>
9. No resolution, no "I learned", no sainthood, no "youngest/first/prestigious" flexes.

## OUTPUT
Write the finished essay to the path in your task. Plain essay text only (title line optional),
~585-605 words. Then run the verifier and report: final word count + verify output + where you
applied each operative change (cut publish-paragraph, folded theory into ¶1, replaced ending, etc.)
+ what feedback.md directive you could NOT satisfy and why.