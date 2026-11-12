# University of Maryland (UMD): Supplemental Essay Lab (2026-27 cycle)

Applicant: Aditya Balaji (Mumbai, India; international CS/AI applicant).
Purpose of this file: exact prompts, what UMD readers say they want, real examples, technique patterns, UMD-specific hooks, pitfalls, and a line-by-line audit of the current draft at `supplements/us/umd/essays.md`. Nothing here duplicates the generic technique files (supplemental-essay-lab 01 to 12); every quote carries a URL.

Format note: UMD asks for **six short answers, 650 characters each** (roughly 100 words), not six 650-word essays. The character cap is the hardest constraint in this file and every technique bullet below reflects it. The sixth prompt is a full multi-sentence question, not a sentence starter.

---

## 1. OFFICIAL 2026-27 PROMPTS

**Status of the official source.** UMD's own essay page, `https://admissions.umd.edu/apply/essay-questions`, lists only the Common App personal essay (the seven 650-word options). It does not publish the six short answers, and the six short answers sit in the Common App Questions tab for UMD, not the Writing tab. GradGPT states this directly: "UMD's own admissions site does not currently list them, but they are still required and unchanged for 2026-27" (`https://www.gradgpt.com/blog/umd-supplemental-essays`). **UNVERIFIED (against the official essay page): the six short-answer prompts are third-party-sourced, because UMD does not publish them on `admissions.umd.edu`. Confirm each in the live Common App before submitting.**

One exception: **the diversity prompt is published by UMD itself**, on the admissions office's Commitment to Diversity page (quoted verbatim in Section 2). That is the only one of the six confirmed directly against a UMD-owned page.

### The six prompts (verbatim, third-party sources)

Confirmed word for word by College Essay Guy, "How to Write the University of Maryland Supplemental Essays: Examples + Guide 2026/2027" (last updated 08/12/2026, `https://www.collegeessayguy.com/blog/university-of-maryland-supplemental-essays`); GradGPT, "UMD Supplemental Essays 2026-27: All Six Short Answers" (updated September 2, 2026, `https://www.gradgpt.com/blog/umd-supplemental-essays`); and Next Admit, "How to Write the University of Maryland Supplemental Essays 2026–2027" (September 21, 2026, `https://nextadmit.com/blog/how-to-write-the-umd-supplemental-essays/`).

1. "If I could travel anywhere, I would go to…" (650 characters)
2. "The most interesting fact I ever learned from research was…" (650 characters)
3. "In addition to my major, my academic interests include…" (650 characters)
4. "My favorite thing about last Tuesday was…" (650 characters)
5. "Something you might not know about me is…" (650 characters)
6. "Because we know that diversity benefits the educational experience of all students, the University of Maryland values diversity in all of its many forms. This includes (but is not limited to) racial, socio-economic, gender, geographical, and sexual orientation. We are interested in hearing about your own individual life experiences. In a few sentences, will you please describe how you have learned, grown, been inspired or developed skills through one or more components of diversity." (650 characters)

### The "last Monday" vs "last Tuesday" discrepancy (Prompt 4)

Clastify's archive shows UMD rotates the day each cycle: "My favorite thing about last Thursday was…" (2023/2024), "My favorite thing about last Friday was…" (2024/2025), and "My favorite thing about last Monday was…" (2025/2026). Source: Clastify, "University of Maryland at College Park Supplemental Essay Examples," `https://www.clastify.com/supplement/university-of-maryland-at-college-park`.

Because the day changes yearly, 2025-26 sources (CollegeVine, College Essay Advisors, Clastify) are not evidence for 2026-27. For 2026-27 the sources split: College Essay Guy (updated 08/12/2026), GradGPT (September 2, 2026), Next Admit (September 21, 2026), Ivy Coach, and College Advisor print **"last Tuesday"**, while College Transitions (August 20, 2026, claiming the questions "carry over unchanged") and Halo Admit print **"last Monday."** The majority of the most recently updated guides say "last Tuesday." **UNVERIFIED (exact day). Best-supported 2026-27 wording appears to be "last Tuesday"; confirm in the portal before finalizing.** A wrong day is a one-word fix, so it does not block drafting.

### Character limit

All six are "650 characters" each, confirmed by every 2026-27 guide above. College Essay Guy: "Note that the below prompts are max 650 characters (not words) each. 650 characters is generally around 100 words." (`https://www.collegeessayguy.com/blog/university-of-maryland-supplemental-essays`). This is one of the tightest limits in US applications.

---

## 2. WHAT THIS SCHOOL'S READERS SAY THEY WANT

Official UMD admissions language (verbatim, UMD-owned pages).

From the review-process page, `https://admissions.umd.edu/apply/admission-review-process-factors`:

> "At UMD, we value all of your strengths and talents. We know there is more to you than grades and SAT scores. While they are important, we also want to know about your interests and background and what makes you unique."
> `https://admissions.umd.edu/apply/admission-review-process-factors`

> "Our admission process has one mission: to identify applicants, who as individuals and as a group, will enrich and benefit from the campus learning environment and the entire student body."
> `https://admissions.umd.edu/apply/admission-review-process-factors`

The review page lists "Written expression of ideas (as demonstrated in the essay)" among the 23-plus factors and states "the essay" is read as one of those factors (`https://admissions.umd.edu/apply/admission-review-process-factors`).

From the admissions office's own Commitment to Diversity page, which publishes the diversity prompt and explains what readers want from it, `https://admissions.umd.edu/student/umds-commitment-to-diversity`:

> "The key component we are searching for is authenticity."
> `https://admissions.umd.edu/student/umds-commitment-to-diversity`

> "We try to get to know students better through the information provided in their letters of recommendation, essays, and responses to our short answer questions."
> `https://admissions.umd.edu/student/umds-commitment-to-diversity`

> "We are trying to find out how students' curiosity, interests, experiences and even challenges may have shaped what they will contribute to UMD both inside and outside the classroom."
> `https://admissions.umd.edu/student/umds-commitment-to-diversity`

> "With this question, we are hoping to learn more about how diversity has shaped each student and its impact on how they've learned and grown."
> `https://admissions.umd.edu/student/umds-commitment-to-diversity`

From the same page, the university president's statement (quoted by the admissions office):

> "The educational value of campus diversity is one we will not sacrifice."
> `https://admissions.umd.edu/student/umds-commitment-to-diversity`

Admissions-reader framing from an experienced reviewer (Next Admit; Ivy League consultants):

> "The admissions officers at UMD ask these questions to learn about who you are as a person. Because of this, you can and should bring your authentic self to the page. Humor is welcome in these responses, as long as you still appropriately answer the question at hand."
> `https://nextadmit.com/blog/how-to-write-the-umd-supplemental-essays/`

**BLOCKED.** No named, individual UMD admissions officer has a verbatim, attributable statement about the six short answers that I could locate and confirm. UMD's reader voice on these prompts lives in the institutional pages quoted above. I will not invent a named officer or reconstruct a quote.

---

## 3. ACCEPTED EXAMPLES

### Guide-published example responses (verbatim)

Source: College Essay Guy, `https://www.collegeessayguy.com/blog/university-of-maryland-supplemental-essays`. These are the full example responses the guide prints for five of the six prompts. **UNVERIFIED (admitted vs. illustrative): the guide does not state that these are accepted student submissions, so treat them as model responses, not confirmed admits.** All are within the 650-character cap.

Prompt 1 ("If I could travel anywhere, I would go to…"):

> "I would go to the U.S Open in 1972 to watch defending champion Billie Jean King defeat Kerry Melville in straight sets. Afterwards, I would follow King as she advocates for pay parity between female and male athletes to learn how to effectively campaign and advocate for social justice causes. In observing King, I would love to channel her confidence in pushing against social norms to address the sexualization of women and young girls in sports."
> `https://www.collegeessayguy.com/blog/university-of-maryland-supplemental-essays`

Prompt 2 ("The most interesting fact I ever learned from research was…"):

> "Did you know William Shakespeare created the terms "wild goose chase," "kill with kindness," and "apple of my eye"? I didn't until a few years ago. In the research process for a paper on Shakespeare's legacy, I became fascinated by his immense contributions to the English language. Having read a Shakespearean play and poems every year for the last several years, I was well aware of his impact on the Western canon of theater and literature, but the sheer number of his coinages and idioms that we still use today shocked me. As an actor, I've been in many shows but never in a Shakespearean play–something I hope to explore at Maryland."
> `https://www.collegeessayguy.com/blog/university-of-maryland-supplemental-essays`

Prompt 3 ("In addition to my major, my academic interests include…"):

> "From Stromae to Matisse to Tintin, I love French culture. Growing up in London and living in Europe, I was surrounded by many people speaking different European languages. After studying Latin for five years, I began Italian and French and continue to improve in both of them, practicing my French fluency in class and furthering my Italian conversational skills at home. My love for languages has also led to my increasing curiosity about the art of different cultures and how a culture's language and art help to make a society distinct. I hope to minor in French and to further develop my understanding of the Francophone world."
> `https://www.collegeessayguy.com/blog/university-of-maryland-supplemental-essays`

Prompt 4 ("My favorite thing about last Tuesday was…"):

> "Playing tennis with my best friend. Even though we aren't related by blood, we are practically twins. He and I frequently have fun debates, the most recent being whether the Comic Sans or Times New Roman font is better. We explore our school town of Bethesda during our open lunches; each day is a little adventure. I feel so lucky to spend time with him, whether that entails tennis or some other activity."
> `https://www.collegeessayguy.com/blog/university-of-maryland-supplemental-essays`

Prompt 5 ("Something you might not know about me is…"):

> "On the underside of my right forearm, I have a tattoo. Drawn in black ink are two intricate curves, the eating disorder recovery symbol, there to remind me every day of my resilience, strength, and bravery. It serves as a message to myself to rely on my resources and support system. Additionally, it symbolizes the support of my family, who sat with me when I got the tattoo, just as they were with me through every hardship that it represents. No one is immune to adversities, but when storms come, I am able to look at my arm and remember that I've endured this before, and I got through it last time, so I can do it again."
> `https://www.collegeessayguy.com/blog/university-of-maryland-supplemental-essays`

Prompt 6 (diversity):

> "My homeschool classroom was a melting pot. My classmates came from all over the world: some were children of Ecuadorian and Pakistani immigrants, while others grew up on army bases. My perspective broadened when we met at each other's houses, eating different cuisines and observing each other's diverse familial structures. From witnessing the struggles to put down roots in military families and the challenges faced by kids whose parents hardly spoke English, I developed deeper empathy for my friends whose experiences differed from my own. Since then, the ability to see the world through the eyes of another has been an incredible asset to me."
> `https://www.collegeessayguy.com/blog/university-of-maryland-supplemental-essays`

Additional Prompt 2 and Prompt 6 examples are printed in the same guide (a Belward Farm sustainability answer, and an Arabic/Armenian traditions answer). Same source, same "model response" status (`https://www.collegeessayguy.com/blog/university-of-maryland-supplemental-essays`).

### Real-student answer (Reddit, r/UMD)

Source: r/UMD thread "UMD short question," `https://www.reddit.com/r/UMD/comments/hfijve/umd_short_question/`. One applicant's posted answer about travel, quoted verbatim:

> "I want to travel to El Salvador and Honduras to see where my family came from and just see the culture, food, and environment there."

The same thread's OP gives the practical advice: "you just have to put some of your personality down on paper so that you're not just a statistic." **UNVERIFIED (admitted status): Reddit user, unconfirmed.**

### Paywalled (title only)

Clastify hosts real past-applicant UMD supplements for application years 2023/2024 through 2025/2026, across all six prompts. Bodies render only behind account access, so only the prompt titles are shown here. `https://www.clastify.com/supplement/university-of-maryland-at-college-park`.

### Flagged as NOT real

GradGPT's UMD page gives prompt-by-prompt strategy but no applicant samples (`https://www.gradgpt.com/blog/umd-supplemental-essays`). Research.com's UMD guide prints invented "weak/strong" illustrations, not submissions (`https://research.com/student-guides/admissions-and-applications/umd-supplemental-essays-examples-tips-and-common-mistakes`). Neither is an accepted-essay source.

---

## 4. TECHNIQUE PATTERNS

Each bullet is anchored to a quoted line and reflects the 650-character compression.

- **Finish the sentence in the first line, then spend the rest on why.** "the job is to finish the sentence in the first line and then add one detail that only you could write. Specific beats impressive on every one of these." (`https://www.gradgpt.com/blog/umd-supplemental-essays`)
- **The destination is not the answer; the reason is.** "what's most important here is *not* the destination, and *not* the journey, but the explanation behind it." (`https://www.collegeessayguy.com/blog/university-of-maryland-supplemental-essays`)
- **At 650 characters, one fact plus one turn is the whole essay.** "State the fact plainly in the first sentence, then say where you found it and what it changed about how you think." (`https://www.gradgpt.com/blog/umd-supplemental-essays`)
- **Name interests that sit outside the major, with a detail each.** "One or two real interests with a detail each read better than four listed nouns." (`https://www.gradgpt.com/blog/umd-supplemental-essays`)
- **Take "last Tuesday" literally and keep the moment small.** "Do not upgrade a boring Tuesday into an achievement; the honesty is the answer." (`https://www.gradgpt.com/blog/umd-supplemental-essays`)
- **Prompt 5 is the free space; write it last.** "Because this is what we'd consider the 'free space,' consider brainstorming topics for each of the other 5 UMD prompts first, and come back to this one last." (`https://www.collegeessayguy.com/blog/university-of-maryland-supplemental-essays`)
- **The six answers are read as one set, so no repeats.** "Admissions is reading all six as a collection, not each one individually!" (`https://www.collegeadvisor.com/essay-guides/university-of-maryland-supplemental-essays/`)
- **The diversity answer must end on a skill, not a belief.** "The verbs in the prompt (learned, grown, inspired, developed skills) are the rubric, so end on the skill." (`https://www.gradgpt.com/blog/umd-supplemental-essays`)
- **Cut filler phrases before the character count does it for you.** "cut filler phrases such as 'I have always been passionate about,' 'from a young age,' 'I truly believe,' and 'in today's society.' These phrases take up space without adding evidence." (`https://research.com/student-guides/admissions-and-applications/umd-supplemental-essays-examples-tips-and-common-mistakes`)
- **Every answer must pass the swap test.** "if your response could be copied into another student's application without much changing, it is too generic." (`https://research.com/student-guides/admissions-and-applications/umd-supplemental-essays-examples-tips-and-common-mistakes`)
- **Humor is allowed only if it still answers the prompt.** "Humor is welcome in these responses, as long as you still appropriately answer the question at hand." (`https://nextadmit.com/blog/how-to-write-the-umd-supplemental-essays/`)

---

## 5. SCHOOL-SPECIFIC HOOKS FOR A CS/AI APPLICANT

Every URL below was fetched or search-verified as live on 15 Oct 2026. No course number or professor is invented. Note: UMD's short answers are mostly personal, so hooks belong mainly in Prompt 3 (academic interests) and, lightly, in the diversity answer, not crammed into all six.

**CMSC courses (verified numbers and titles).** UMD's graduate course catalog lists, among others, CMSC421 "Introduction to Artificial Intelligence" (3 credits), CMSC422 "Introduction to Machine Learning," and CMSC643 "Principles of Machine Learning." Catalog: `https://academiccatalog.umd.edu/graduate/courses/cmsc`.

**CLIP Lab (Computational Linguistics and Information Processing).** Official page: `https://info.umd.edu/centers-and-labs/clip`. Verbatim: "The CLIP Laboratory at the University of Maryland is engaged in designing algorithms and methods that allow computers to effectively and efficiently perform human language-related tasks." And: "CLIP is a lab within the University of Maryland Institute for Advanced Computer Studies (UMIACS), located in the Brendan Iribe Center for Computer Science and Engineering." Relevant to an AI applicant who works with language data: "deep learning, human-in-the-loop machine learning, multilingual text processing and low-resource languages, machine translation, and summarization."

**Maryland Cybersecurity Center (MC2).** Official page: `https://cyber.umd.edu/about`. Verbatim: "The Maryland Cybersecurity Center (MC2) is a unique, multidisciplinary research and education powerhouse focused on theoretical and applied cryptography, data-driven security, human-computer interaction and security, network and wireless security, machine learning and security, blockchain and cryptocurrency security, and programming languages security." Also: "In 2019, the Maryland Cybersecurity Center moved into the Brendan Iribe Center for Computer Science and Engineering."

**ACES (Advanced Cybersecurity Experience for Students).** Official page: `https://aces.umd.edu/`. Verbatim: "The Advanced Cybersecurity Experience for Students (ACES) includes a living-learning program and an academic minor for exceptional undergraduate students of all majors. Part of the UMD Honors College, ACES was launched in Fall 2013 with the help of a major gift from our founding sponsor, Northrop Grumman." The page states figures current as of the page: "185 Students currently enrolled in the ACES living-learning program" and "121 Students currently pursuing the ACES Minor."

**Carillon Communities.** Official page: `https://carillon.umd.edu/`. Verbatim: "Carillon Communities is a living-learning program where students translate their *curiosity* into action using *creative problem solving* and *teamwork*." Named communities on the page include "Constitutional Rights" and "iGive." (Prior research also lists a Health Justice community; treat named-community detail as verify-before-use.)

**UMIACS (University of Maryland Institute for Advanced Computer Studies).** Home: `http://umiacs.umd.edu/`. It is the umbrella that houses CLIP and MC2 and, per MC2's page, "has more than 80 faculty and 200 graduate students that represent 15 departments and six colleges and schools on the UMD campus" (`https://cyber.umd.edu/about`).

**Terrapin Hackers (hackathon club).** Source: UMD CS, "CS Club Preview 2015," `https://www.cs.umd.edu/article/2015/09/cs-club-preview-2015`. Verbatim: "Terrapin Hackers: the Terrapin Hackers are an organization that helps students interested in going to hackathons meet other people and get involved... The club also hosts Hacktorials where students lead workshops to teach you some aspect of design or engineering. They even have their own design space, Collider." (Older article; confirm the club is still active before naming it.)

**Bitcamp (UMD hackathon).** Source: same UMD CS article, `https://www.cs.umd.edu/article/2015/09/cs-club-preview-2015`. Verbatim: "Bitcamp: it's not only an awesome hackathon, but a great chance to get involved with planning a large event. Bitcamp is a student run hackathon." A separate UMD CS item references the event at `https://www.cs.umd.edu/node/15627`.

**Honors College programs (for the "academic interests" hook, if used).** UMD's University Honors list includes ACES, Digital Cultures and Creativity, Gemstone, Honors Global Challenges and Solutions, Honors Humanities, Integrated Life Sciences, Interdisciplinary Business Honors, and University Honors (via the Office of Undergraduate Studies).

**NOT FOUND / do not use:** a UMD "MAX Lab" could not be verified; searches returned an unrelated Indian healthtech company. If an AI/ML lab name is needed, safer verified substitutes are CLIP and MC2 (above), or the Maryland Robotics Center (RAAS Lab, Robotics, Autonomy, and Sensing, led by Pratap Tokekar). **UNVERIFIED (MAX Lab): do not cite it.**

---

## 6. PITFALLS FOR THIS SCHOOL

- **Generic praise for UMD.** "Writing generic praise about UMD" is listed as a top mistake because "It shows little research and does not reveal much about you." (`https://research.com/student-guides/admissions-and-applications/umd-supplemental-essays-examples-tips-and-common-mistakes`)
- **Repeating the activities list.** "Repeating the activities list" hurts because "It wastes limited space on information already available elsewhere." (`https://research.com/student-guides/admissions-and-applications/umd-supplemental-essays-examples-tips-and-common-mistakes`)
- **Sounding impressive instead of honest.** "Trying to sound impressive instead of honest... can make the response feel inflated or unnatural." (`https://research.com/student-guides/admissions-and-applications/umd-supplemental-essays-examples-tips-and-common-mistakes`)
- **AI-polished but vague prose.** "Using AI-generated phrasing without revision... can produce polished but vague responses that lack personal texture." (`https://research.com/student-guides/admissions-and-applications/umd-supplemental-essays-examples-tips-and-common-mistakes`)
- **A quirk with no reflection.** "A quirky topic without reflection may feel random." (`https://research.com/student-guides/admissions-and-applications/umd-supplemental-essays-examples-tips-and-common-mistakes`)
- **Overused travel cliches.** College Advisor warns against "cliches that are overused, such as 'I would travel to another time period.'" (`https://www.collegeadvisor.com/essay-guides/university-of-maryland-supplemental-essays/`)
- **Being too general on Prompt 1.** "Avoid being too general by stating the name of a continent or a country. Instead, choose a city, town, or even neighborhood." (`https://www.collegeadvisor.com/essay-guides/university-of-maryland-supplemental-essays/`)
- **A diversity answer that states a belief but shows no change.** The UMD prompt's verbs are "learned, grown, been inspired or developed skills"; a response that "just says what you believe" is exactly what the official page does not ask for (`https://admissions.umd.edu/student/umds-commitment-to-diversity`).
- **Filler openers that eat the character budget.** "cut filler phrases such as 'I have always been passionate about,' 'from a young age'..." (`https://research.com/student-guides/admissions-and-applications/umd-supplemental-essays-examples-tips-and-common-mistakes`)
- **Ignoring the character limit.** "Ignoring the character limit... Important words may be cut off in the application portal." (`https://research.com/student-guides/admissions-and-applications/umd-supplemental-essays-examples-tips-and-common-mistakes`)

---

## 7. AUDIT OF MY CURRENT DRAFT

File audited line by line: `supplements/us/umd/essays.md` (status as written: Draft 1). Six responses exist. No rewrite is given below; weak lines are quoted verbatim. Facts needing verification are listed at the end.

### Response 1: "If I could travel anywhere": Grade: B

The core choice is a widely used destination and trope, which is the risk College Advisor flags for this prompt (overused travel answers, `https://www.collegeadvisor.com/essay-guides/university-of-maryland-supplemental-essays/`). The saving line is the honest turn: "I know it is a wall with half a trolley stuck in it. I would still run at it," which shows self-aware voice and answers the "why." But the ending repeats material that appears in Prompt 5: "Then I'd find the nearest South Indian restaurant, because no trip is complete without idli-sambar." Since the six answers are "read all six as a collection, not each one individually" (`https://www.collegeadvisor.com/essay-guides/university-of-maryland-supplemental-essays/`), spending the closing line of Prompt 1 on the same idli-sambar motif as Prompt 5 is a repetition cost. The response also reveals little about the CS/AI side of the applicant, which is acceptable here but means the space could carry one more distinctive detail rather than a second food reference. Craft is fine; distinctiveness and non-repetition hold it at B.

### Response 2: "The most interesting fact I ever learned from research": Grade: A

This is the strongest of the six. It states the fact plainly, names the dataset ("Across 21 markets, Borsa Istanbul had the second-lowest share of attention surges preceded by foreign markets: about 10%, against 28% for its peers"), and delivers a genuine turn: "I expected foreign investors to drive it. The data said the story was local." That is exactly the pattern the prompt rewards, "State the fact plainly in the first sentence, then say where you found it and what it changed about how you think" (`https://www.gradgpt.com/blog/umd-supplemental-essays`), and it matches verified activity #1 (the 21-market Borsa Istanbul Review paper). It is also specific enough that no other applicant could sign it, which passes the swap test (`https://research.com/student-guides/admissions-and-applications/umd-supplemental-essays-examples-tips-and-common-mistakes`). Held from A+ only because the exact figures (10%, 28%, "second-lowest," 21 markets) must be checked against the paper before submission.

### Response 3: "In addition to my major, my academic interests include": Grade: A-

Names an interest outside the major (behavioral economics) and connects it to something the applicant actually builds: "every system I build eventually runs into people copying people: investors follow trades, and club members follow the most confident answer in the room." That is a real interdisciplinary link, which the prompt values. The Monty Hall detail, "The ten-door Monty Hall game is my favorite way to turn a quiet room into an argument," is concrete and voiced. Minor deduction: it lists essentially one field plus a puzzle, and neither gets a UMD anchor; one sentence tying behavioral economics to a verified course or lab would use the remaining space without adding a list. Strong, but with unused fit potential.

### Response 4: "My favorite thing about last Tuesday": Grade: A-

Takes the prompt literally and keeps the moment small, which is the right instinct: "Take the question literally... the honesty is the answer" (`https://www.gradgpt.com/blog/umd-supplemental-essays`). The voice is the best in the set: "Someone starts a GeoGuessr round and we argue over which country a blurry road belongs to, then switch to Minecraft and build something nobody planned." It also lands a light value at the end: "I have learned nothing useful, which is exactly why it was my favorite part of the day." One clause is slightly garbled: "our commentary gets worse than the football." Held at A- rather than A because the payoff is tonal (learning nothing useful) rather than a specific value, and because it does not need the full character budget.

### Response 5: "Something you might not know about me": Grade: C+ (as written)

This is the response that most needs revision, and the reason is the prompt's own design. Prompt 5 is "the 'free space'... come back to this one last" precisely so it adds something the other five do not (`https://www.collegeessayguy.com/blog/university-of-maryland-supplemental-essays`). Instead, the draft's own text signals the problem: it opens with "that I will travel an unreasonable distance and wait an unreasonable time for one plate of idli-sambar at Dakshinayan in Mumbai," which is the same idli-sambar motif used as the closer of Prompt 1. It then stacks two unrelated facts in the remaining space: "I also sleep by 10:30 and wake up without an alarm, which sounds disciplined until you see how often I lose my keys." The keys line is the generic, "could be anyone" move that the swap test rejects (`https://research.com/student-guides/admissions-and-applications/umd-supplemental-essays-examples-tips-and-common-mistakes`), and the sleep/keys pairing is a mini-list of trivia rather than "one concrete example" (`https://www.gradgpt.com/blog/umd-supplemental-essays`). The fix is selection, not rewriting: choose one true thing that is not idli-sambar and not already in the file, then give it one real example. As written it is coherent prose but spends the free space on a repeat.

Note on placement: the draft's Prompt numbers run 1 travel, 2 research, 3 academic interests, 4 last Tuesday, 5 something-you-might-not-know, 6 diversity. That matches the confirmed order. The heading in the draft for item 6 is fine but the official prompt text should be pasted from the portal given the "individual" vs "own" wording difference noted in Section 1.

### Response 6: "Diversity": Grade: B (content A-; prompt-wording risk)

The narrative is strong and matches verified activity (the Rural Education Program). It shows change, not just belief, which is the prompt's rubric: "I learned that being correct is not the same as being understood," and the concrete turn "One boy who had avoided every question raised his hand for algebra because getting it right meant beating his friend." It ends on a transferable skill: "Now, before I explain anything, I ask what the other person already knows. The gap between us is information I need, not something to talk over." That is the "end on the skill" pattern (`https://www.gradgpt.com/blog/umd-supplemental-essays`) and it engages a component of diversity without claiming a listed identity, which the official UMD page explicitly permits ("we are not asking students to bare any information they are uncomfortable sharing," `https://admissions.umd.edu/student/umds-commitment-to-diversity`). Held to B overall only because the draft pastes a shortened prompt header rather than the full verbatim UMD question, and the official UMD wording differs slightly from the third-party wording (official says "your own life experiences"; guides say "your own individual life experiences"). Paste the portal version. On content alone this is A-, one of the two best in the set.

### Overall draft grade: B

Two responses are A-level on content (research; diversity) and two are A-/B+ (academic interests; last Tuesday). The set is pulled down by two specific, fixable problems: the idli-sambar motif repeats across Prompts 1 and 5, and Prompt 5 spends its free space on generic trivia. Fix those two and the set rises to A-/A. Nothing here requires a rebuild, only selection and one swap.

### Facts needing verification (do not assert until confirmed)

1. **Idli-sambar / Dakshinayan (Mumbai).** Confirm the restaurant exists at the stated location and that the "hour of traffic, another hour in line" detail is true. This motif appears twice and must be true.
2. **"Lose my keys" detail.** The draft's own footer flags this as possibly lifted from the Stanford drafts. Confirm it is factually true before using it in a submitted answer.
3. **Borsa Istanbul figures.** Confirm "21 markets," "second-lowest share," "about 10%," and "28% for its peers" against the paper itself, not memory. This is the load-bearing claim of the strongest response.
4. **"Ten-door Monty Hall game."** Confirm the intended variant (the classic is three doors) and that the phrasing is accurate as written.
5. **Platform 9¾ / "the studio where Harry Potter was filmed."** The filming location commonly cited is Warner Bros. Studio Tour London (Leavesden). Confirm the intended place, since the line "I know it is a wall with half a trolley stuck in it" describes the King's Cross set piece specifically.
6. **Prompt 4 day ("last Tuesday").** Confirm in the portal (Section 1).
7. **Prompt 6 exact wording.** Paste the portal version of the full diversity question; UMD's own 2023 page prints "your own life experiences" while 2026-27 guides print "individual life experiences" (`https://admissions.umd.edu/student/umds-commitment-to-diversity`; `https://www.collegeessayguy.com/blog/university-of-maryland-supplemental-essays`).
8. **Character counts.** Confirm each response is 650 characters or fewer including spaces, tested in the portal (the file's footer notes a script check, but the portal is the authority).

---

## 8. SOURCES

All URLs accessed 15 Oct 2026.

1. UMD Office of Undergraduate Admissions, "Essay Questions" (official; lists only the Common App essay): https://admissions.umd.edu/apply/essay-questions
2. UMD Office of Undergraduate Admissions, "Admission Review Process & Factors" (official): https://admissions.umd.edu/apply/admission-review-process-factors
3. UMD Office of Undergraduate Admissions, "UMD's Commitment to Diversity" (official; publishes the diversity prompt and the authenticity language): https://admissions.umd.edu/student/umds-commitment-to-diversity
4. College Essay Guy, "How to Write the University of Maryland Supplemental Essays: Examples + Guide 2026/2027" (updated 08/12/2026): https://www.collegeessayguy.com/blog/university-of-maryland-supplemental-essays
5. GradGPT, "UMD Supplemental Essays 2026-27: All Six Short Answers" (updated September 2, 2026): https://www.gradgpt.com/blog/umd-supplemental-essays
6. Next Admit, "How to Write the University of Maryland Supplemental Essays 2026–2027" (September 21, 2026): https://nextadmit.com/blog/how-to-write-the-umd-supplemental-essays/
7. College Advisor, "University of Maryland Supplemental Essays | UMD Essay Prompts": https://www.collegeadvisor.com/essay-guides/university-of-maryland-supplemental-essays/
8. Research.com, "2027 Umd Supplemental Essays: Examples, Tips, and Common Mistakes": https://research.com/student-guides/admissions-and-applications/umd-supplemental-essays-examples-tips-and-common-mistakes
9. Clastify, "University of Maryland at College Park Supplemental Essay Examples" (paywalled bodies; day-of-week archive): https://www.clastify.com/supplement/university-of-maryland-at-college-park
10. Reddit r/UMD, "UMD short question": https://www.reddit.com/r/UMD/comments/hfijve/umd_short_question/
11. UMD Graduate School course catalog, CMSC courses: https://academiccatalog.umd.edu/graduate/courses/cmsc
12. UMD College of Information, "Computational Linguistics and Information Processing (CLIP) Lab": https://info.umd.edu/centers-and-labs/clip
13. Maryland Cybersecurity Center (MC2), "About MC2": https://cyber.umd.edu/about
14. Advanced Cybersecurity Experience for Students (ACES), home: https://aces.umd.edu/
15. Carillon Communities, home: https://carillon.umd.edu/
16. UMD Institute for Advanced Computer Studies (UMIACS), home: http://umiacs.umd.edu/
17. UMD Department of Computer Science, "CS Club Preview 2015" (Terrapin Hackers, Bitcamp): https://www.cs.umd.edu/article/2015/09/cs-club-preview-2015
18. UMD Department of Computer Science, Bitcamp item: https://www.cs.umd.edu/node/15627
