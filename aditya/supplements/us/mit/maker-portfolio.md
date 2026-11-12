# MIT Maker Portfolio: Draft 1

**What MIT asks for (verify on mitadmissions.org before submitting):** an optional portfolio, submitted through SlideRoom, plus a short written description of each project. Show the process, not just the final product: what you built, what broke, and how you fixed it. Each project needs a 1-2 minute video, or else photos or screenshots with captions. Be clear about what you did alone versus with others. Deadline: the same as EA (1 Nov), so the video has to be recorded this month.

## Project 1: NEXUS Exchange (lead project)

**One line:** I built a working stock exchange from scratch, filled it with nine kinds of autonomous traders, and used it to test my own research.

**Why I built it:** My investor-attention paper found that volatility jumps once trading passes about 1.4x normal. Real markets can't be rerun, so I couldn't test *why*. I built a market I could rerun.

**What I built (alone):**
- A matching engine with a live order book. A first Python version was too slow for research-scale runs. I rewrote the core in compiled Python (Numba), which brought the median order time to 6.5 µs and batch throughput to 10M+ orders/sec, a 46x speedup.
- Nine trader types, including herders, momentum traders, attention-limited traders and market makers, interacting on that order book.
- A validator that checks whether the simulated market behaves like a real one. Calibrated runs pass 9 of 9 standard real-market patterns (fat tails, volatility clustering and others); the average across seeds is 8.2 of 9.
- 10,200 simulations run in parallel.

**What failed and what I learned:** The first engine was correct but too slow to answer anything. Speed turned out to be a research requirement, not a luxury. NEXUS also put its attention threshold at 1.56, outside my paper's 95% interval (1.16-1.48). I report that honestly: the simulator supports the mechanism, not the exact number.

**Video plan (90 s):** 0-15 s, the question. 15-45 s, a live run, with the order book filling and prices moving. 45-70 s, the speed benchmark and the before/after rewrite. 70-90 s, the threshold result and the honest gap.

## Project 2: Daedalus (STEM Racing / F1 in Schools)

**One line:** I built the engineering software our team uses to decide which car design is worth making before we manufacture it.

**What I built (alone, for the team):**
- An airflow model trained on our CFD results that predicts the aerodynamics of new designs without a fresh simulation each time.
- A race-time simulator for the 20 m track, so every design variable maps to a predicted race time.
- Predictive scrutineering, which flags designs likely to break competition rules before any part is made.
- Stress tests on edge cases and uncertainty, giving a worst case and a failure probability for each design.
- Traceability: clicking any result shows its equation, inputs, units and assumptions.

**What the team did vs what I did:** [Fill in: who designed the car, who ran the CFD, and what decisions the team made using Daedalus.]

**Video plan (60-90 s):** walk through one design change and how its predicted race time and rule check update; then compare one prediction with a real measurement, if there is one.

## Before submitting
- [ ] Record both videos (screen capture is fine; narrate in your own voice).
- [ ] Scrub AGENTS.md and AI audit files from any linked repo.
- [ ] Daedalus: add one real decision the team made using it.
- [ ] Keep every number identical to the activity list.
