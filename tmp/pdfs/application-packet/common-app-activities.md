**Working draft** | Ranked activity entries with expanded descriptions.

This copy includes the current position, organization, 150-character entry, and supporting full description. Time commitments are not included because the current ranked file does not set final hours and weeks.

## 1. Corresponding Author, Lead Researcher

**Organization:** Borsa Istanbul Review: peer reviewed, revised & resubmitted

**Common App description (147/150 characters)**

> Discovered when market attention turns dangerous: past 1.39x normal trading, volatility surges; showed it holds across 21 global markets & 11 years

## 2. Creator & Solo Developer

**Organization:** Independent project: NEXUS Exchange; architecture paper on SSRN

**Common App description (146/150 characters)**

> Engineered a stock exchange from zero: 9 kinds of autonomous traders compete on a live order book clearing 10M+ orders/sec; ran 10,200 experiments

## 3. Creator & Solo Developer

**Organization:** Independent project: QUANT360 (ATLAS) quant research platform

**Common App description (148/150 characters)**

> Engineered ATLAS, a full quant research terminal: test any trading idea, decode market regimes, build & stress-test portfolios with ML; 3 real users

## 4. Creator & Solo Developer

**Organization:** Independent project: Glassbox incident-response agent

**Common App description (150/150 characters)**

> Engineered an AI agent that investigates server outages like a senior engineer: traces each failure through metrics, code & runbooks, citing each clue

## 5. Founder, Lead Instructor

**Organization:** Quant Finance Club (school) + Future Lab mock market

**Common App description (148/150 characters)**

> Founded 25-30 member quant club & built its trading floor: a 150-company simulated stock market; wrote the 13-week course members learn valuation in

## 6. Corresponding Author, Researcher

**Organization:** Journal of Sports Economics: submitted

**Common App description (150/150 characters)**

> Caught millions of fantasy football players rewarding luck over skill: equal-chance players who happened to score drew 1.3pp more owners the next week

## 7. Sole Author, Researcher

**Organization:** Independent project: PhenoSync; Oxford Saïd Business School Climate Challenge

**Common App description (150/150 characters)**

> Found blueberries & their bee pollinator drifting 4.57 days/yr apart, overlap down ~99% since 2016, by fusing NASA satellite, NOAA climate & GBIF data

## 8. Solo Developer

**Organization:** School STEM Racing Team: Daedalus engineering platform

**Common App description (149/150 characters)**

> Engineered our F1 team's digital wind tunnel: predicts airflow & race time from CFD, stress-tests edge cases, flags rule breaks before parts are made

## 9. Fundraiser & Volunteer Teacher

**Organization:** Rural school near Abhinav School: fundraising & teaching

**Common App description (149/150 characters)**

> Raised INR 25,000 for a rural school; taught its 50 top students algebra & English, reworking lessons into games until they solved problems on their own

## 10. Equity Research Intern

**Organization:** MalkansView (stock research firm)

**Common App description (148/150 characters)**

> Worked a live equity research desk: read real-time market data, dissected company financials, built & stress-tested strategies, ran a mock portfolio

## Alternate option for activity 10: Sports Analysis Hub

**Position:** Co-Founder

**Common App description (131/150 characters)**

> Co-founded Sports Analysis Hub; hosted consistent tactical/stat prep; sustained community members returned to; led through presence

Co-founded and co-hosted Sports Analysis Hub to discuss sport beyond "player good/bad" — tactics, decision-making, statistics, player roles, evidence changing opinions. Initiated and sustained meetings; prepared material so members kept returning after novelty faded. Learned that leadership is often the work before/after the meeting.

\newpage

# Expanded Activity Descriptions

## 1. Corresponding Author, Lead Researcher - Borsa Istanbul Review: peer reviewed, revised & resubmitted

Built a 21-market panel (2015-2025) using abnormal trading volume as an attention measure, cross-checked against Google search and Wikipedia pageviews. Forward volatility rises nonlinearly, with a transition near 1.39x normal volume (95% interval 1.16-1.48) that can be located using past data only. Surges preceded by attention abroad stay volatile longer, read as context rather than contagion. Borsa Istanbul is among the least internationally preceded markets and follows the lira instead. Went through full peer review at Borsa Istanbul Review (Q1), was rejected, rebuilt the paper, and resubmitted. Corresponding author.

## 2. Creator & Solo Developer - Independent project: NEXUS Exchange; architecture paper on SSRN

Built an agent-based stock market with nine trader types, calibrated to real data (simulated method of moments). Calibrated runs match nine standard real-market patterns (9/9 on the calibrated seed, 8.2/9 average across seeds), including fat tails and volatility clustering. Matching engine: ~145K orders/sec per call, p50 latency 6.7 microseconds; 672 tests, 92% coverage. Ran a 10,200-simulation sweep of the attention threshold. Adds a curriculum-trained reinforcement-learning market maker and XGBoost/LSTM liquidity-fragility models. SSRN architecture paper covers the agent layer.

## 3. Creator & Solo Developer - Independent project: QUANT360 (ATLAS) quant research platform

Built ATLAS (QUANT360) from scratch as a production system now used by a CS graduate for real analysis. Eight modules: Regime, Research, Screener, ML, Volatility, Factor, PCA, Portfolio. Research module: Callaway–Sant'Anna DiD, RD, IV, event studies. Volatility: HAR-RV, full GARCH family, Statistical Jump Models, Diebold–Yilmaz. ML: combinatorial purged CV with deflated Sharpe, Double ML, meta-labeling, hierarchical risk parity. Point-in-time fundamentals, IC–IR weighted composite scoring, full QMJ factor construction, survivorship-bias disclosure. Constrained to free data (yfinance, FRED, Ken French Data Library); extensive vectorization removed major bottlenecks.

## 4. Creator & Solo Developer - Independent project: Glassbox incident-response agent

Engineered Glassbox SRE — autonomous SRE agent. Prometheus/Alertmanager → FastAPI webhook → Redis queue → LangGraph investigation (commit correlation via OpenAI diff analysis, runbook retrieval via pgvector RAG, impact estimation directly from Prometheus). Evidence-cited brief to Slack; automated postmortems in Postgres with React/Vercel dashboard. Crucially, LLM never fabricates figures: impact numbers come straight from Prometheus, timelines from stored timestamps. Built 15-scenario evaluation harness with seeded ground-truth commits: deterministic-heuristics baseline 13% top-1, full LangGraph agent 87% — isolating reasoning pipeline's value over naive triage.

## 5. Founder, Lead Instructor - Quant Finance Club (school) + Future Lab mock market

Founded and run Quant Finance Club (25–30 members). Designed 13-week curriculum covering markets, valuation, quantitative methods — moving from equation-first to game-based entry (Monty Hall / probability games with cards/charts/simulator) after early sessions left members disengaged. Built flagship platform Future Lab — fictional market of ~150 companies across 15 industries with two-engine dynamics: Intrinsic Value (five-factor: Management Quality, MOAT, Financial Quality, FCF Quality, Growth Potential) and Price Driver (seven weighted drivers) tethered via Ornstein–Uhlenbeck mean-reversion on log valuation gap. Percentile-based financial quality scoring with industry-specific pillar weightings. Timeline branching; configuration-driven (every weight/coefficient in DB). Live at future-lab-terminal.vercel.app.

## 6. Corresponding Author, Researcher - Journal of Sports Economics: submitted

Introduced Behavioral Ownership Gap (BOG) quantifying systematic divergence between optimal and actual player ownership in the £7.5B Fantasy Premier League ecosystem, treating FPL as behavioral market microstructure under incomplete information and platform architecture. Built Fama–MacBeth panel across 380 gameweeks (t=-57.20) and identified £137.1M annual welfare cost attributable to information architecture failure. Pre-registered frozen out-of-sample validation: 105 profitable weeks out of 105 in equity long-short replication. Corresponding author; submitted to Journal of Sports Economics (Q1). First empirical paper to formally model FPL participation this way.

## 7. Sole Author, Researcher - Independent project: PhenoSync; Oxford Saïd Business School Climate Challenge

Sole author of an open pipeline that turns GBIF citizen-science records, NASA MODIS satellite phenology, NOAA climate data and FAOSTAT crop data into yearly mismatch estimates. In North American highbush blueberry, the gap between bloom and its main bumblebee pollinator widened 4.57 days/year (OLS p = 0.0003, R² = 0.83), and the chance that pollinator activity overlaps the bloom onset window fell about 99% since 2016. New adaptive first-event estimator cuts error 30x versus the naive minimum in simulation. Reports null and data-limited regions honestly. Entered the Oxford Saïd Business School Climate Challenge; manuscript prepared for Methods in Ecology and Evolution.

## 8. Solo Developer - School STEM Racing Team: Daedalus engineering platform

Designed and shipped Daedalus solo as a full-stack engineering platform the STEM Racing team actually relies on for competition trade-offs (not a demo). Features: unit/dimensional validation, provenance tracking, design-space exploration, Monte Carlo sensitivity, uncertainty/robustness analysis, multi-objective Pareto optimization, scenario comparison, equation traceability, 3D visualization. Built with Next.js/React/TypeScript, Python/FastAPI, PostgreSQL, Three.js. Team uses Daedalus for real decisions where improving one objective sacrifices another — responsibility test for clear communication.

## 9. Fundraiser & Volunteer Teacher - Rural school near Abhinav School: fundraising & teaching

Taught foundational Mathematics and English to 50+ underprivileged rural children (Abhinav School villages) through Rural Education Program, returning weekly. First explanations failed: correct description, attention lost, "understood?" produced unreliable "yes." Adapted weekly — changed example, sequence, language, and activity (team games, peer teaching) until learners could use the idea independently. Tracked literacy/numeracy gains; experience shaped how technical work is now communicated (adaptation proof for Princeton service / VT Ut Prosim).

## 10. Equity Research Intern - MalkansView (stock research firm)

Completed three-month internship at MalkansView, a stock market research firm (~140 hours, ~35 hrs/week, ~12 weeks). Analyzed company fundamentals (revenue, costs, competitive position, management, growth, financial quality, risks), distinguished facts from interpretation and interpretation from prediction, and understood how research supports actual investment decisions. Supervised professional setting contrasting with self-directed projects.