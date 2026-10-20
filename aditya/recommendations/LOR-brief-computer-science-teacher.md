# Notes for My Recommendation Letter: Computer Science

*Aditya Balaji*

Thank you for writing my recommendation. Below are some details about my work and a few example passages in case they help. Please use whatever is useful and leave out the rest.

---

## About me

- **Name:** Aditya Balaji
- **School:** JBCN International School, Mumbai (Cambridge International: AS and A Levels, Cambridge IPQ)
- **Graduating:** 2027
- **Intended field:** Computer Science, with strong interests in mathematics, economics and research
- **First deadline:** 1 November 2026 (MIT and other Early Action schools). Stanford and others follow in January.
- **Submitted through:** Common App teacher evaluation. The same letter goes to every university, so it works best without naming a specific one.

## Why I asked you

You have seen how I work with code and systems more closely than anyone else at school. My other recommendation comes from my IPQ supervisor and focuses on my research, so this letter can focus on how I build and think as a computer scientist. Together, the two letters cover both sides of my work.

## At a glance

- **Strongest points:** five complete working systems (NEXUS Exchange, ATLAS, Glassbox, Daedalus, Future Lab), three of them used by other people; research peer reviewed at a Q1 journal.
- **Words that may fit:** independent, rigorous, a builder, curious, generous with what he knows.
- **A structure that works well:** opening → one moment from class → projects and their scale → understanding of his own work → working with others → response to feedback → closing. About 500–800 words.

---

## 1. Opening

**Points you may find useful:**
- How I compare with other students you have taught in Computer Science
- That my projects are complete working systems, not class exercises
- That other people use what I build

> *Example 1:* "Aditya is one of the most independent students I have taught in Computer Science. He takes ideas well past the syllabus and turns them into complete systems that other people use."

> *Example 2:* "Few students I have taught combine Aditya's technical ambition with the same care about whether their work is actually correct."

## 2. How I approach a problem

**Points you may find useful:**
- I like to understand why a method works before I rely on it.
- I split a large system into parts I can test on their own.
- I think about how a system will be used and what could go wrong before I build it.
- I learned software architecture, databases, machine learning, statistics and AI agent design on my own, as my projects needed them.
- Any question or discussion from your class that you remember.

> *Example:* "Aditya thinks about a system the way an engineer does. He asks how it will be used, where it might fail, and how he will know whether it works, before he writes much code."

## 3. My projects, explained simply

### NEXUS Exchange: a stock exchange built from scratch
- **What it does:** it recreates how a real stock exchange works. Buyers and sellers send orders, and an "order book" matches them by price and time, the way the NSE or NASDAQ does.
- **The traders:** nine different kinds of automated traders, such as market makers, trend followers and long-term investors, each with their own strategy, trade against each other.
- **Speed:** the matching engine handles orders in a few microseconds.
- **Realism:** the market it produces shows the same patterns economists see in real markets, such as sudden large price moves and calm periods followed by volatile ones.
- **Testing:** 672 automated tests check that each part behaves correctly. I ran 10,200 simulations to study when attention makes prices unstable.
- **Extras:** a trading agent that learns by reinforcement learning, and models that predict when the market might suddenly lose liquidity.
- **Write-up:** an architecture paper explaining the design, published on SSRN.

### ATLAS (QUANT360): a quantitative research platform
- **What it does:** a full research terminal where you can test an investment idea, study how markets behave and build a portfolio.
- **Eight modules:**
  - **Regimes:** detects whether the market is calm, trending or in crisis.
  - **Research:** tests whether an event really caused a price change, using methods economists use.
  - **Screener:** ranks companies by quality, value and other factors.
  - **Machine learning:** builds prediction models with checks so they don't just memorise the past.
  - **Volatility:** measures and forecasts risk.
  - **Factors:** explains what drives a stock's returns.
  - **PCA:** finds hidden patterns shared across many stocks.
  - **Portfolio:** builds portfolios and stress-tests them.
- **Care with data:** it only uses information that was available at each moment in time, so results aren't accidentally based on the future. It also accounts for companies that disappeared.
- **Users:** real people, including a CS graduate, use it for their own analysis.

### Glassbox: an AI agent that investigates server outages
- **What it does:** when a website or service breaks, it works out why, much as an on-call engineer would.
- **How it works:** it receives the alert, checks the system's metrics, looks at recent code changes to see which one may have caused the problem, searches the team's instructions (runbooks) for the relevant fix, and sends a short report with evidence for each conclusion.
- **Reliability:** every number in the report comes straight from the system's own data, so the AI is never allowed to make up figures.
- **Evaluation:** I set up 15 test incidents where the real cause was known. A simple rule-based approach found the cause 13% of the time and the full agent found it 87% of the time.
- **Built with:** professional tools including a monitoring system, a database, a task queue and a dashboard.

### Daedalus: an engineering platform for our STEM Racing team
- **What it does:** acts as the team's "digital wind tunnel," predicting airflow and race time for a car design before it is made.
- **Features:**
  - It checks that units and calculations are consistent.
  - It explores many design options at once.
  - It shows how uncertain each prediction is.
  - It finds the best trade-offs when improving one thing makes another worse.
  - It flags designs that break competition rules.
  - It shows the car in 3D.
- **Use:** the team uses it for real design decisions.

### Future Lab: a simulated stock market for teaching
- **What it does:** a market of about 150 fictional companies across 15 industries, each with its own financial statements.
- **How prices move:** each company has a "true value" based on management, competitive advantage, financial strength, cash flow and growth. Its price moves around that value and is pulled back towards it over time.
- **Use:** members of the Quant Finance Club learn valuation by analysing these companies. It is live online.

> *Example:* "The scale of Aditya's work is unusual. His projects are complete systems with testing, documentation and real users, the kind of work I would expect from a university team rather than a school student."

## 4. My research

- **Investor attention and market volatility (corresponding author):** across 21 national markets over eleven years, volatility rises sharply once trading passes about 1.39 times its normal level. It went through full peer review at *Borsa Istanbul Review*, a Q1 journal where most authors are university researchers, and has been revised and resubmitted.
- **Fantasy Premier League as a behavioural market (corresponding author):** shows that millions of players reward luck over skill. Submitted to the *Journal of Sports Economics*.
- **PhenoSync (sole author):** shows blueberries and their bee pollinator drifting out of sync by about 4.57 days a year, using NASA satellite, climate and biodiversity data. Entered in the Oxford Saïd Business School Climate Challenge.
- **NEXUS architecture paper:** published on SSRN.
- **Cambridge IPQ:** on whether high-frequency trading makes market crises worse.

> *Example:* "Alongside his software, Aditya does serious research. His paper on investor attention has been through full peer review at a Q1 international journal, and he has further work in economics and ecology. His programming and his research feed each other: he built a market simulator partly to test his own findings."

## 5. Understanding my own work

**Points you may find useful:**
- I use AI coding tools, and I'm open about it. I treat them like a fast assistant, not the designer.
- I decide the structure of each system, what each part is responsible for, and what tests it has to pass.
- I can explain why I chose one design over another, such as why Glassbox takes its numbers only from real data instead of letting the AI produce them.
- When something breaks, I trace the cause myself.
- My projects connect: the simulator tests my research, the research platform is used by other people, and the teaching market came from the club.

> *Example:* "Aditya uses modern tools openly, but the thinking is his. Whenever I have asked him about one of his systems, he has been able to explain how it is structured, why he made each major choice, and what he would change."

## 6. Working with others

**Points you may find useful:**
- I founded the Quant Finance Club (25–30 members), wrote its 13-week course and built Future Lab for it.
- When the first sessions were too technical, I changed them to games and simulations so members could work things out themselves.
- I built Daedalus for my STEM Racing team.
- I raised ₹25,000 for a rural school and taught mathematics and English to about 50 students there.

> *Example:* "Aditya shares what he knows. When the first sessions of the club he founded proved too technical, he redesigned them until the members could reason through the problems themselves."

## 7. Response to feedback

**Points you may find useful:**
- I take criticism seriously and use it to improve the work.
- When reviewers gave detailed comments on my research paper, I restructured it and resubmitted it.
- I would rather know a weakness early than defend a first version.

> *Example:* "Aditya responds to criticism by improving the work, not by defending it."

> *Growth example:* "His ambition sometimes leads him to take on many projects at once, and he has been learning to prioritise."

## 8. Closing

> *Example 1:* "Aditya is among the very best students I have taught. He will bring curiosity, rigour and a habit of building things that work to any community he joins. I recommend him with enthusiasm and without reservation."

> *Example 2:* "He is one of the top few students I have encountered in my career, and I give him my highest recommendation."

---

## Moments you might remember

These are only reminders. A short scene from your own memory, in your own words, is usually the strongest part of a letter.
- A question I asked in class that went beyond the syllabus
- A time you questioned my design or code, and what I did next
- A time I helped a classmate with a problem or explained an idea
- Conversations about NEXUS, ATLAS, Glassbox or Daedalus, and how I explained my choices
- How my coding developed over the time you have taught me

## Links, if useful

Admissions readers welcome a brief look at a student's actual work.
- Future Lab (live): future-lab-terminal.vercel.app
- NEXUS Exchange architecture paper: SSRN
- I'm happy to show you any of my projects or send screenshots or code.

---

## A possible full letter

*Just one way it could come together. Please change it freely.*

> Aditya is one of the most independent students I have taught in Computer Science. He takes ideas well past the syllabus and turns them into complete systems that other people use.
>
> Aditya thinks about a system the way an engineer does. Before he writes much code, he asks how it will be used, where it might fail and how he will know whether it works. [A moment from class.]
>
> The scale of his work is unusual. He built NEXUS Exchange, a working stock exchange in which nine kinds of automated traders compete, backed by 672 automated tests and an architecture paper on SSRN. His research platform, ATLAS, is used by other people for their own analysis, and our STEM Racing team relies on Daedalus, the engineering tool he built, for real design decisions. For Glassbox, an AI agent that investigates server outages, he set up his own test of 15 incidents and reported honestly how it compared with a simple baseline. Alongside this, his research on investor attention has been through full peer review at a Q1 international journal.
>
> Aditya uses modern tools openly, but the thinking is his. Whenever I have asked him about one of his systems, he has been able to explain how it is structured, why he made each major choice, and what he would change.
>
> He also shares what he knows. He founded the school's Quant Finance Club, wrote its course and built a simulated market for it, and when the first sessions proved too technical, he redesigned them until members could reason through problems themselves. He responds to criticism by improving the work, not by defending it. His ambition sometimes leads him to take on many projects at once, and he has been learning to prioritise.
>
> Aditya is among the very best students I have taught in my career. He will bring curiosity, rigour and a habit of building things that work to any community he joins. I recommend him with enthusiasm and without reservation.
