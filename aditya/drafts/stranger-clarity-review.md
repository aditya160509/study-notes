# Stranger-Clarity Review (read as an admissions officer with no finance, stats or CS)

Source file `final draft essay.md` was NOT edited. Every edit below is quote then replacement. [CONFIRM] = the replacement adds or reshapes a fact, so check it is true. Word counts use whitespace-separated words on a scratch copy with all edits applied.

## Grades (harsh, out of 10)

| Essay | Now | After edits | Main problem |
|---|---|---|---|
| Common App | 9.0 | 9.2 | "syntax", "the model" never explained |
| UIUC experience | 7.5 | 9.0 | "random seeds", "tuning" |
| UIUC goals | 7.0 | 8.8 | "model validation", "backtested", "cheat", "safeguard", "stock-return findings" |
| UIUC stats | 7.0 | 8.8 | "significant", "independent", "Driscoll-Kraay", "Time Series" |
| UW-Madison | 7.8 | 9.0 | "Monte Carlo", "benchmarks", "validate", "tuned", "quant finance", "reward luck over skill" reads wrong |
| Purdue opportunities | 8.0 | 9.0 | "data cleaning", "outages", "same reason" has no clear referent, "Boiler Quant" |
| Purdue why CS | 7.8 | 9.0 | "herd" undefined, "error analysis", "research computing cluster" |
| UMass why | 8.2 | 9.0 | "causal methods", "real interventions" |
| UMass why CS | 7.0 | 8.8 | "XGBoost", "trading volume" |
| UMass community | 9.0 | 9.0 | Clean. No edit |
| VT community | 9.0 | 9.1 | "the second call" vague |
| VT inclusion | 8.2 | 9.0 | "Quant Finance Club" undefined |
| VT leadership | 8.3 | 9.0 | "drag", "sat at it" |
| VT goal | 8.3 | 9.0 | "survivorship bias" leads the sentence before it is explained |

Whole-set notes: no em dashes anywhere, no AI-tell words found. Standards 13 to 16 all hold (no implied placements, no "found" for "estimated" problems). Recurring stranger-traps to watch if you add anything later: investor attention, herd, trading volume, tuned, model, validate, benchmark. "NEXUS" is always explained on first use, good.

## Common App (648 words, limit 650; locked, so only two tiny swaps, zero net words)

1. "This time AI wrote only the syntax I hate; I decided what it built. Months later, the model estimated a threshold"
   -> "This time AI wrote only the routine code; I decided what it built. Months later, my statistical model estimated a threshold"
   Why: "syntax" is a programmer word; "the model" appears from nowhere. Count after: 648.
Other ideas rejected: explaining "earnings" or "stock jumped" (the Nvidia example already does it), and extra words (no room).

## UIUC (3 essays, about 150 each)

### Experience (151 -> 149)
2. "After tuning, one run matched all nine. Then I reran it with ten random seeds, and only six did. Changing how the program drew random numbers, nothing about the traders, dropped one run to five. I had tuned a lucky run, not a market. Now every result I report lists the seeds it failed on."
   -> "After adjusting the traders, one run matched all nine. Then I ran it ten times, each with different random luck, and only six runs matched. Changing the luck alone dropped one setup to five. I had tuned a lucky run, not a market. Now every result I report lists the runs it failed."
   Why: "seeds" is the exact jargon your teachers flagged. "Luck" is plain and keeps the story true. Ending still lands on an action.

### Goals (149 -> 152, about 150 is fine)
3. "I want to work in model validation, checking a bank's risk or pricing models before anyone acts on them. I met the idea in Harvey, Liu and Zhu's paper arguing that most published stock-return findings are likely false,"
   -> "I want to work in model validation: checking the math a bank uses to judge risk before anyone acts on it. I met the idea in Harvey, Liu and Zhu's paper arguing that most published findings about stock prices are likely false,"
4. "I read company filings and earnings-call transcripts and backtested trading strategies. The ones that looked best on past charts usually rested"
   -> "I read company reports and tested trading strategies on past prices. The best-looking ones usually rested"
5. "In my research, I limited my testing program to information that existed on each day, so it could not cheat. In Glassbox, my software-failure tool, I blocked invented numbers. No one has tested either safeguard."
   -> "In my research, my test program could use only what was known on each past day, so it could not peek ahead. In Glassbox, my tool for diagnosing software crashes, I stopped the AI from stating numbers it invented. No one has tested either check."
   [CONFIRM] Glassbox's "invented numbers" are numbers the AI made up (I assumed so, since Purdue calls Glassbox an AI tool).
6. "Illinois would teach me to design real checks. CS 442, Trustworthy Machine Learning, teaches how models get fooled, so I can hunt for the failures my own rules miss."
   -> "At Illinois, CS 442, Trustworthy Machine Learning, teaches how learning programs get fooled, so I can hunt for failures my own rules miss."
   Why: removes "backtested", "cheat", "safeguard", "pricing models". Paying for the cut sentence: CS 442 line already says what Illinois adds.

### Second-choice major (134 -> 148)
7. "my first test said the jump in price swings was significant. But it treated each country's market as independent, and markets fall together: when New York drops, Mumbai usually follows. So I switched to Driscoll-Kraay standard errors, which allow for that."
   -> "my first test said the jump in price swings was too big to be luck. But it treated each country's market as separate, and markets fall together: when New York drops, Mumbai usually follows. So I switched to a method that allows for this (Driscoll-Kraay standard errors)."
   Why: the plain claim comes first, the technical name is a bracket a stranger can skip but a statistician sees.
8. "STAT 410 and then STAT 429, Time Series Analysis, would teach me"
   -> "STAT 410 and then STAT 429, Time Series Analysis, the study of data that changes over time, would teach me"

## UW-Madison (481 -> 492, limit 500)

9. "STAT 340, Data Science Modeling II, teaches Monte Carlo simulation, the formal version of running NEXUS thousands of times, and COMP SCI 532 covers the math under the machine-learning models I added to it."
   -> "STAT 340, Data Science Modeling II, teaches simulation with random chance, the formal version of running NEXUS thousands of times, and COMP SCI 532 covers the math behind the machine-learning models, programs that learn patterns from data, that I added to it."
10. "asks the question I keep meeting, how to validate models, and builds benchmarks to test them. I want to learn how a test is designed so that the model being tested cannot simply be tuned to pass it, which is exactly what I did to NEXUS."
   -> "asks the question I keep meeting, how to check that a model really works, and builds benchmarks, standard tests that models are graded on. I want to learn how to design a test that the model cannot simply be adjusted to pass, which is exactly what I did to NEXUS."
11. "Traders at Wisconsin, the quant finance club."
   -> "Traders at Wisconsin, the student club for math-driven trading." [CONFIRM] description matches the club.
12. "And my other paper asks whether the millions of people who play Fantasy Premier League, a game built on the English soccer league, reward luck over skill."
   -> "And my other paper asks whether Fantasy Premier League, a game millions play built on the English soccer league, rewards luck more than skill."
   Why: the old sentence says the players reward luck, which is nonsense; the game does.
Prompt coverage: both "why Madison" and "why CS" are answered and Madison-only items are named. Flow and ending are strong; no change.

## Purdue

### Opportunities (249 -> 250, limit 250; one word of slack is thin, so recount if you edit again)
13. "I would bring Python data cleaning and dashboards, and the habit" -> "I would bring Python for cleaning messy data and building charts, and the habit"
14. "Professor Ming Yin's research draws me for the same reason." -> "Professor Ming Yin's research on how people use AI advice draws me for the same reason."
   Why: the old "same reason" had no clear subject.
15. "I read her paper on second opinions in AI-assisted decisions expecting a second opinion could only help." -> "I read her paper on second opinions in AI-assisted decisions expecting them to only help."
16. "I know the over-trusting side: when I first used AI, I trusted what it built because it was fast, not because I understood it." -> "I know over-trusting: I first trusted what AI built for me because it was fast, not because I understood it."
17. "In Glassbox, my AI tool for diagnosing software outages, every number cites its evidence, but I have never tested whether that helps an engineer catch a wrong diagnosis or only makes a wrong one sound convincing." -> "In Glassbox, my AI tool for diagnosing why an app goes down, every number cites its evidence, but I never tested whether that helps an engineer catch a wrong diagnosis or only makes it sound convincing."
18. "I would also join Boiler Quant, Purdue's quantitative finance club. I founded a similar club at school, so this time I would rather join a team with a project already going and have people who know more try to break my trading models."
   -> "I would join Boiler Quant, Purdue's club for math-driven trading. I founded a similar club at school, so this time I would join a team with a project already going and let people who know more try to break my strategies." [CONFIRM] club description.

### Why CS (249 -> 249)
19. "\"Investors herd\" is an easy sentence to write." -> "\"Investors herd\" (they copy the crowd) is an easy sentence to write."
20. "To make NEXUS realistic, I adjusted it until its prices matched real market data, a method I took from papers" -> "I adjusted NEXUS until its prices matched real market data, a method I took from papers"
21. "my sentence had skipped all three" is fine. Delete "actually": "which parts of an explanation I never actually made" -> "which parts of an explanation I never made"
22. "which covers error analysis, would show me." -> "which covers how small errors grow in calculations, would show me." [CONFIRM] matches CS 31400 syllabus.
23. "Purdue's research computing cluster" -> "Purdue's shared supercomputers" (and "learn to run projects" -> "run projects"). [CONFIRM] the Data Mine does use Purdue's research computers.

## UMass

### Why UMass (100 -> 99, hard limit 100)
24. "argues that causal methods should be tested on real interventions, not invented data." -> "argues that methods for finding causes need real experiments, not invented data." [CONFIRM] still fair to Jensen's position.

### Why CS (94 -> 98)
25. "Then my XGBoost model, a common prediction tool, ranked trading volume as its most important input." -> "Then a prediction model I trained on market data ranked trading volume, the amount traded, as its most important input."

### Community (100, no edit). Exactly at the limit and already clear. Do not touch.

## Virginia Tech (hard limit 120)

### Community (119 -> 119)
26. "the second call," -> "calling donors again," [CONFIRM] the follow-up was to donors.

### Inclusion (118 -> 116)
27. "In my school's Quant Finance Club, I was the one leaving people out. At first, the same four or five people answered everything." -> "In the school club I founded to study markets with math, I was the one leaving people out. The same four or five people answered everything."
28. "I took it to the other founders, and we saw that we were teaching" -> "The other founders and I saw we were teaching"

### Leadership (120 -> 119)
29. "Between two designs, A looked" -> "Of two designs, A looked"
30. "my drag estimate too optimistic" -> "my air-resistance estimate too optimistic"
31. "B also cleared the rules' 48 g minimum mass; A sat at it." -> "B had room above the rules' 48 g minimum; A had none."
Kept "I learned my job is to make my work easy to doubt": best line, short, shows a change.

### Goal (119 -> 119)
32. "The toughest so far is survivorship bias: my results may describe only managers who stayed all season, so next I test those who quit." -> "The toughest so far: my results may describe only managers who stayed all season, called survivorship bias, so next I test those who quit."

## Final word counts (changed essays)

Common App 648 (limit 650) | UIUC experience 149 | UIUC goals 152 | UIUC stats 148 | UW 492 (limit 500) | Purdue opportunities 250 (limit 250) | Purdue why CS 249 | UMass why 99 | UMass CS 98 | UMass community 100 (unchanged) | VT community 119 | VT inclusion 116 | VT leadership 119 | VT goal 119

## Things I did not change, on purpose

- "investor attention" and "price swings": explained by how the essays use them, and the Common App already makes them concrete with Nvidia. Adding glosses everywhere would cost words with no gain.
- UW "Data Science Modeling II" and COMP SCI 532: course names, tied to NEXUS, fine as is.
- All endings. They already show an action.
