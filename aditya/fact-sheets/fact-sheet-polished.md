# Aditya Balaji — Information for Teacher Recommendations

## How I learn and work

I learn best when I can move between theory and implementation. I might begin by reading about a mathematical idea, then write a small program to see how it behaves, then return to the theory when the result raises a new question. Building something exposes gaps in my understanding quickly. It forces me to decide what a term means, what assumptions I am making, and what the output actually represents.

My usual process is to begin with a broad question, break it into smaller questions, identify the relevant mathematics and data, build a first version, test it, and investigate whatever does not behave as expected. I do not regard a project as complete simply because the code runs or the presentation looks polished. I want to know whether the result is reproducible, whether the assumptions are visible, whether alternative explanations have been considered, and whether another person could understand the reasoning.

I am comfortable teaching myself unfamiliar material. I have learned new statistical methods, machine-learning techniques, financial models, software frameworks, and research practices because a project required them. I do not always learn in a linear way. Sometimes I begin with an ambitious question and work backwards to the foundations I need. This can make the early stages messy, but it also helps me connect ideas that are usually taught separately.

I respond well to questions that make me defend an assumption. I appreciate being asked what evidence would change my mind, what the limitations of a model are, or whether I can explain a technical idea without relying on jargon. Those questions often lead me to understand my own work more clearly.

## My GASI paper: studying when investor attention changes market behaviour

One of my main research projects is the Global Attention Saturation Index, or GASI. I designed an empirical measure of investor-attention thresholds across 22 international equity markets. The project investigates whether the relationship between investor attention and volatility changes after attention reaches a particular level.

The central difficulty was that attention and market behaviour can influence one another. To address this endogeneity problem, I used a Lewbel instrumental-variable strategy. I estimated a structural threshold of γ*=1.5625 and calculated a Hansen confidence set of [1.14, 2.50]. I used Driscoll–Kraay standard errors to account for cross-sectional dependence and conducted synthetic-control falsification tests to examine whether the result could be explained by an unrelated pattern.

The paper documents what I call the “Silence Signature,” a volatility-suppression effect that appears during peak-attention regimes. I confirmed the pattern individually in 14 of the 22 markets studied. I was the corresponding author of the resulting paper, which was submitted to *Borsa Istanbul Review*, a Q1 journal. The paper passed desk review and completed a full peer-review round. I am currently preparing a resubmission.

The project taught me that research is not simply the process of finding an interesting result. The result has to survive questions about design, measurement, assumptions, robustness, and interpretation. Peer review also taught me that criticism is not necessarily a rejection of the whole project. It can identify the exact place where an argument needs to become more precise.

## My Behavioral Ownership Gap paper: turning a sports hobby into research

I developed the concept of the Behavioral Ownership Gap while studying Fantasy Premier League. The concept measures the divergence between optimal player ownership and actual player ownership. Rather than treating Fantasy Premier League only as a game, I studied it as a behavioural market system in which participants make repeated decisions using incomplete information and a particular information architecture.

I built a Fama–MacBeth panel covering 380 gameweeks and recovered a t-statistic of -57.20. I estimated an annual welfare cost of £137.1 million and designed a frozen out-of-sample validation model. In an equity long-short replication, the model produced 105 profitable weeks out of 105. I was the corresponding author, and the paper is currently under review at the *Journal of Sports Economics*.

This project reflects one of the ways I think. I enjoy sport as a participant and fan, but I also become interested in the structures beneath it: how information is distributed, how people respond to incentives, how beliefs influence decisions, and how repeated choices can be studied statistically. I like finding serious questions inside familiar activities.

## My NEXUS Exchange project: building a simulated market

I engineered NEXUS Exchange, an agent-based financial-market simulator. I designed nine behaviourally distinct trader archetypes and used Numba JIT compilation and multiprocessing to run 10,200 Monte Carlo simulations. I estimated a structural threshold using the Simulated Method of Moments and recovered γ*=1.5625, independently corroborating the threshold from GASI through a different methodology.

I tested the simulator against nine canonical market stylised facts, including fat tails, volatility clustering, and autocorrelation structure. I used jump-filtered ARCH LM testing following the approach associated with Andersen, Bollerslev, and Diebold. The system also includes an adversarial reinforcement-learning market maker trained with PPO, liquidity-fragility prediction using XGBoost and LSTM models, and a FastAPI inference server.

NEXUS was valuable because it allowed me to examine whether an empirical finding could emerge from a separate model of interacting agents. It also showed me that complexity is not the same as realism. A model with many components is not automatically useful. It must be validated against known behaviour, and its assumptions must remain understandable enough to examine.

## My neural-network paper: explaining why large models can still learn

I wrote a mathematical exposition titled “Why Overparameterised Neural Networks Generalise.” The paper examines the apparent tension between the size of modern neural networks and the expectation that a model with too many parameters should overfit.

I derive the Neural Tangent Kernel from first principles using mathematics available through my Further Mathematics background. The paper discusses the bias–variance paradox, neural networks as linear maps, gradient descent as a dynamical system, Gram matrices, eigenvalue structure, spectral bias, and the relationship between overparameterisation and conditioning. I also include a fully worked two-neuron example, calculated line by line.

This project was important because it allowed me to approach an advanced AI-theory question without treating advanced vocabulary as a substitute for understanding. I wanted to know what the objects in the theory meant, how they were related, and whether I could explain the mechanism with mathematics I had genuinely learned.

## My PhenoSync project: connecting environmental change to economic risk

I built PhenoSync, an open-data pipeline for studying phenological mismatch. Phenological mismatch concerns changes in the timing of biological events and the possibility that species, crops, and environmental conditions no longer align as they previously did.

The pipeline integrates GBIF species-occurrence data, NASA MODIS land-surface-temperature and NDVI data, NOAA GHCND climate records, and FAOSTAT agricultural data. I estimated an OLS slope of 4.57 days per year of phenological shift, with R²=0.83 and p=0.0003. I tested the result with a seven-framework robustness battery involving Kendall, Spearman, Mann–Kendall, permutation, and jackknife tests.

I also designed a PMI-severity crop-exposure model that translates phenological mismatch into economic value-at-risk indicators. I was the sole author from conception through manuscript drafting and entered the work into the Oxford Saïd Business School Climate Challenge. The project combined environmental science, statistics, data engineering, and economics, and showed me how a data pipeline can connect a scientific observation to a practical risk question.

## My Cambridge research qualification and finance internship

I completed Cambridge International IPQ 9980, an independent research qualification. My 4,982-word report investigated whether high-frequency algorithmic trading destabilises markets during periods of stress. I completed the research design, empirical analysis, research log, and bibliography according to Cambridge’s formal assessment criteria.

The IPQ gave me practice in structuring a long investigation, narrowing a broad topic into a researchable question, documenting decisions, and evaluating evidence. It also helped me understand that independent work still requires discipline: a project needs a clear scope, a defensible method, and a conclusion that does not claim more than the evidence supports.

I completed a three-month internship at MalkansView, a stock-market research firm, working approximately 35 hours per week. I spent roughly 140 hours learning how to analyse company fundamentals, apply analytical frameworks to real market data, and understand how research contributes to investment decisions. The experience gave me exposure to a supervised professional environment outside my self-directed projects and helped me see how research is used when decisions have practical consequences.

## My ATLAS / QUANT360 platform

I built ATLAS, also called QUANT360, as a full-stack quantitative research platform. I designed modules for regimes, research, screening, machine learning, volatility, factors, PCA, and portfolio construction. The research module includes causal-identification tools such as Callaway–Sant’Anna difference-in-differences, regression discontinuity, instrumental variables, and event studies.

The volatility module includes HAR-RV, the GARCH family, statistical jump models, and Diebold–Yilmaz connectedness measures. The machine-learning module includes combinatorial purged cross-validation, the deflated Sharpe ratio, Double Machine Learning, meta-labelling, and hierarchical risk parity. I also implemented point-in-time fundamental data handling, IC–IR weighted composite scoring, QMJ factor construction, and survivorship-bias disclosure.

I deliberately constrained the platform to free data sources, including yfinance, FRED, and the Ken French Data Library. I spent significant time vectorising the core analytics and removing computational bottlenecks. ATLAS is used by a CS graduate for real analysis, which is meaningful to me because I want my projects to be useful rather than merely impressive in description.

## My Daedalus engineering platform

I designed and shipped Daedalus as a solo developer for my STEM Racing team. It is a full-stack engineering research and decision-making platform that the team uses for real competition-related design trade-offs.

Daedalus supports dimensional and unit validation, provenance tracking, design-space exploration, Monte Carlo sensitivity analysis, uncertainty and robustness analysis, multi-objective Pareto optimisation, scenario comparison, equation traceability, and 3D visualisation. I used Next.js, React, TypeScript, Python, FastAPI, PostgreSQL, and Three.js.

The most important difference between Daedalus and a purely personal project was that other people needed to rely on it. I had to think about how clearly results were communicated, whether assumptions could be traced, and whether the software could support a decision under practical constraints. It taught me that technical sophistication has value only when it helps a real user make a better decision.

## My Zeus and Glassbox SRE systems

I built Zeus as an agentic goal-decomposition pipeline. It includes importance-weighted memory decay, directed-acyclic-graph execution visualisation, Playwright browser automation, and an end-to-end loop from a natural-language prompt to verified real-world task execution. The system reduced token usage by approximately 35%.

I was interested in how an AI agent could break a broad goal into smaller actions, retain the right information, use external tools, and verify that the task had actually been completed. This project brought together software design, planning, memory, automation, and evaluation.

I also engineered Glassbox SRE, an autonomous incident-response system. Prometheus or Alertmanager alerts enter a FastAPI webhook and Redis queue, after which a LangGraph investigation runs parallel nodes for commit correlation, runbook retrieval, and impact estimation. The system uses OpenAI-driven diff analysis, pgvector retrieval, and Prometheus data. It produces an evidence-cited incident brief, posts findings to Slack, and generates postmortems stored in Postgres and displayed through a React/Vercel dashboard.

I designed Glassbox so that the language model would not invent important figures. Impact numbers come directly from Prometheus, and postmortem timelines are reconstructed from stored event timestamps. I built a 15-scenario evaluation harness with seeded ground-truth commits. A deterministic heuristics-only baseline reached 13.3% top-one accuracy, while the full LangGraph system reached 86.7%. This project reinforced my belief that AI systems must be evaluated with explicit tests instead of trusted because their outputs sound confident.

## My Quant Finance Club and Future Lab

I founded and run the Quant Finance Club, which has approximately 25–30 members. I designed a 13-week curriculum covering markets, valuation, and quantitative methods. My goal was to create a space where students could interact with financial ideas rather than only encounter them as definitions.

The club’s flagship project is Future Lab, a simulated stock market containing approximately 150 companies across 15 industries. I designed an intrinsic-value engine based on financial quality and a price-driver engine that models factors such as earnings surprises, news sentiment, and institutional flow. Prices can deviate from intrinsic value but are pulled back toward it using an Ornstein–Uhlenbeck mean-reversion process.

Future Lab is configuration-driven: weights, coefficients, and formula parameters are stored in the database so the simulation can be recalibrated without changing the underlying code. It also supports timeline branching, allowing users to explore alternate futures from a particular point in the market’s history. Building the club and the platform has taught me that leadership is not only having an idea. It involves designing a structure, communicating it, preparing consistently, and making it possible for other people to participate.

I also co-founded and co-hosted a sports-analysis club. I initiated meetings and helped maintain a consistent space that members continued returning to. This experience taught me that leadership can be quiet and practical. A group often depends less on a title than on somebody who keeps showing up, prepares something useful, and creates continuity.

## My sport, service, and community work

I play football and have participated as a goalkeeper through the IAYP physical-recreation component. Goalkeeping requires concentration, anticipation, accountability, and the ability to recover quickly after a mistake. I enjoy the combination of physical participation and analysis, which is one reason I have also explored sports behaviour through Fantasy Premier League data.

I completed the IAYP Bronze and Silver Awards. My Silver programme combined community service, football goalkeeping, and a 26-week quantitative-research skills project focused on AI, machine-learning models, and quantitative-trading strategies. The programme required consistency over time rather than a single short-term achievement.

I taught foundational Mathematics and English to more than 50 underprivileged rural children through a rural education programme. I had to adapt my explanations when students did not understand the first version of a lesson. This changed how I think about communication. Knowing a subject is not the same as being able to teach it; an explanation is successful only when the other person can use the idea.

I also raised more than ₹25,000 through crowdfunding to provide study kits, clothing, and footwear to underprivileged children in rural villages. The experience showed me that community service is often built from practical work: outreach, coordination, logistics, and repeated follow-through. I value that kind of work because its impact is direct even when it is not visible or glamorous.

## My personal growth and intellectual integrity

One of the most important experiences in my development involved my early use of AI tools. After my tenth-grade Computer Science board examination, I had decided that coding was the one thing I would never do. Later, AI tools made difficult coding problems appear accessible, and I began using them to reach material I could not yet solve independently.

At first, I became too focused on speed. During my first research paper, I submitted work that I could not properly defend. My teacher discovered the gap and told me that he expected better from me. I found the experience deeply uncomfortable because I knew, even before being questioned, that I had optimised for a finished product instead of genuine understanding.

I did not stop using AI tools. I changed what I allowed them to do. They can help me draft, search, or suggest possibilities, but they cannot make the final intellectual decision for me. I check the reasoning, test the code, investigate the sources, and make sure I can reconstruct the important parts without assistance. My standard is whether I can explain and defend the work if somebody removes every tool and asks me to begin again.

That standard was tested by research results that did not match my expectations and by journal rejections. I cleaned data, changed variables, reran models, and checked my code from different directions. Sometimes I hoped that a coding error would explain an unexpected result, because finding a mistake would have been easier than accepting that the hypothesis might be wrong. I learned to treat a null result as information and to separate the value of careful work from the publication outcome.

I am still developing. My ambition can lead me to take on too many demanding projects at once. I can move faster than my understanding if I do not deliberately slow down, and I sometimes hold myself to a standard that makes delegation or early communication difficult. I am working on prioritising better, asking for help earlier, explaining uncertainty sooner, and distinguishing useful perfectionism from unnecessary perfectionism.

## What I would like my teachers to understand about me

I hope my teachers will describe me through specific examples rather than broad adjectives. The most useful examples would show how I respond to a difficult question, how I learn material independently, how I handle an unexpected result, how I use criticism, how I explain technical work, or how I make a project useful to other people.

I am not simply a coding student or a finance student. I am a student who becomes absorbed by complex systems and then learns whatever is necessary to investigate or build them. Markets, neural networks, climate, engineering, sport, and education may seem like separate areas, but they are connected by my interest in mechanisms, evidence, modelling, and communication.

My strongest qualities are initiative, technical curiosity, persistence, mathematical ambition, and a growing commitment to intellectual honesty. My most important personal development has been learning that finished work is not the same as understood work. I want to study a field where mathematics, computing, data, and real-world systems meet, and I want my work to be ambitious, technically sound, useful, and defensible.

## My projects explained in simple language

The following explanations are written in simpler language so that a teacher who is not a specialist in quantitative finance, machine learning, or software engineering can understand what I actually did and why it matters.

### What I learned at MalkansView

At MalkansView, I worked in a stock-market research environment rather than only studying markets through books or personal projects. I spent approximately three months and around 140 hours learning how analysts examine companies, understand their fundamentals, interpret financial information, and turn research into an investment view.

In simple terms, I learned how to ask whether a company is financially strong, how its business works, what could make it grow or decline, and whether the market price reflects that information. I also saw that professional research is not just about having an opinion. It involves organising evidence, comparing companies, questioning assumptions, and communicating a conclusion clearly enough for someone else to use.

The internship was important because much of my other work is self-directed. At MalkansView, I had to work within a supervised professional setting and understand how research is done when it has practical consequences. It helped me connect the models I studied independently with the decisions real analysts have to make.

### What my GASI paper is about

GASI began with a question: does investor attention affect markets in the same way at every level, or is there a point at which the relationship changes? For example, if very few people are watching a market, small changes in attention might matter a great deal. But if almost everybody is already paying attention, additional attention might have a different effect.

I studied this question across 22 international stock markets. I collected and organised the relevant data, designed a statistical framework, and tried to separate attention from other factors that could influence volatility. This is difficult because attention and market movements can affect each other. A market move may attract attention, while attention may also influence the market move.

To handle this problem, I used an instrumental-variable method and estimated a threshold at which the relationship appeared to change. The threshold estimate was γ*=1.5625, with a Hansen confidence set of [1.14, 2.50]. I used statistical corrections for dependence across markets and conducted falsification tests to check whether the finding could be explained by something unrelated.

The paper describes a pattern I named the “Silence Signature.” In simple terms, markets sometimes appeared less volatile during periods of extremely high attention, which is counterintuitive because we often assume that more attention automatically means more instability. I found the pattern separately in 14 of the 22 markets. The significance of the project is not that one number proves a universal law; it is that I designed a way to investigate a difficult question, tested the result in multiple settings, and presented the limitations honestly.

The paper was submitted to *Borsa Istanbul Review*, a Q1 journal. It passed the initial desk review and went through a complete peer-review round. I am preparing a resubmission. For a teacher, the most important part of this activity may be the process: I took an abstract question, learned advanced methods independently, worked through criticism, and continued after the first version was not accepted immediately.

### What my Behavioral Ownership Gap paper is about

The Behavioral Ownership Gap project began with Fantasy Premier League. Fantasy Premier League is a game in which participants choose football players for their teams, and player ownership reflects what thousands or millions of participants believe will happen. I became interested in the difference between what a mathematically optimal strategy might select and what participants actually select.

I developed a way to measure that difference and treated the game as a behavioural market. Participants respond to recent performances, reputation, social influence, information available on the platform, and their own beliefs. Their choices may therefore be systematically different from the choices suggested by a model using expected performance and risk.

I built a panel covering 380 gameweeks and used a Fama–MacBeth approach to examine the relationship between ownership behaviour and outcomes. The analysis produced a t-statistic of -57.20. I estimated a possible annual welfare cost of £137.1 million and then designed a frozen out-of-sample test rather than adjusting the model after seeing the results.

The out-of-sample replication produced 105 profitable weeks out of 105. I understand that a result like this needs careful interpretation and further scrutiny, which is why I focused on freezing the model and separating the validation period from the period used to develop the idea. The paper is under review at the *Journal of Sports Economics*.

This activity shows that I do not separate my academic identity from my personal interests. I enjoy football, but I also enjoy asking what data can reveal about how people make decisions. I am happiest when a familiar activity opens the door to a deeper question.

### What my NEXUS Exchange project does

NEXUS Exchange is my attempt to build a market from the bottom up. Instead of using only historical data, I created different types of simulated traders and allowed them to interact. Some traders respond to trends, some respond to value, some provide liquidity, some react to volatility, and some behave more aggressively.

The purpose was to ask whether realistic market patterns could emerge from the interactions of different decision-making rules. I created nine trader archetypes and ran 10,200 Monte Carlo simulations. Monte Carlo simulation means repeatedly running a model with varying random conditions so that we can study the range of outcomes rather than relying on one run.

I also used NEXUS to independently test the threshold I found in GASI. Through the Simulated Method of Moments, the simulator recovered γ*=1.5625. This mattered to me because the same structural result appeared through a separate method. I also tested whether the simulated market displayed known features of real markets, such as extreme price movements, volatility that clusters over time, and predictable patterns in correlations.

The simulator includes a reinforcement-learning market maker, a model that predicts liquidity fragility, and a FastAPI server that allows other systems to interact with the simulation. In plain terms, I built not just a single experiment but a reusable environment for asking questions about markets.

The personal significance of NEXUS is that it made me confront the difference between building something impressive and building something credible. A simulator can have many layers and still be unrealistic. I therefore spent substantial effort validating its behaviour rather than only adding features.

### What my neural-network paper explains

My paper on overparameterised neural networks addresses a question that initially seems paradoxical. A model with more parameters than data points might appear likely to memorise the data and fail on new examples. Yet modern neural networks can be extremely large and still generalise well.

I wrote a mathematical explanation of this problem using concepts I could derive from my Further Mathematics background. I explained neural networks as linear maps, described gradient descent as a dynamical system, studied Gram matrices and eigenvalues, and used the Neural Tangent Kernel to examine the behaviour of a network during training.

I also explained spectral bias, the tendency for learning processes to capture smoother and simpler patterns before more complicated ones. I included a two-neuron example and worked through the calculations step by step rather than presenting only a final formula.

The project demonstrates how I approach material that is beyond my formal level. I did not begin with the expectation that I already knew enough. I began with a question, identified the mathematical pieces I needed, studied them, and assembled them into an explanation. I enjoy this kind of work because it requires both technical precision and the ability to communicate an abstract idea clearly.

### What my ATLAS platform does

ATLAS, or QUANT360, is a quantitative research platform that I built from scratch. A simple way to describe it is as a workbench for studying investments and financial data. It brings together tools that are often found separately: data screening, factor analysis, volatility analysis, machine learning, causal research, portfolio construction, and regime analysis.

For example, the platform can help study whether a factor is associated with returns, whether volatility behaves differently in different regimes, whether an event appears to have caused a change, and how a portfolio might be constructed while accounting for risk. I implemented methods such as GARCH models, Double Machine Learning, difference-in-differences, instrumental variables, event studies, hierarchical risk parity, and meta-labelling.

The important part is not simply that I used sophisticated names. I had to understand how each method works, what data it needs, what assumptions it makes, and what can go wrong. I also had to build the supporting infrastructure: data handling, interfaces between modules, performance improvements, and protections against issues such as look-ahead bias and survivorship bias.

I deliberately relied on free sources such as yfinance, FRED, and the Ken French Data Library. This forced me to work within realistic data limitations. I optimised the code so that the analysis could run efficiently, and the platform is now used by a CS graduate for real analysis. That external use is one of the strongest indicators that the project became a usable tool rather than remaining a private experiment.

### What my Daedalus platform does

Daedalus is a platform I designed for my STEM Racing team. The team has to make engineering decisions involving trade-offs. A design may be lighter but less robust, faster but more difficult to manufacture, or stronger but heavier. These decisions cannot always be resolved by choosing the biggest value in one column.

Daedalus helps the team explore those trade-offs. It checks units and dimensions, tracks where values came from, runs Monte Carlo simulations, studies sensitivity to uncertain inputs, compares scenarios, and identifies Pareto-optimal designs. A Pareto-optimal design is one where improving one important objective would require sacrificing another.

The platform also supports equation traceability and 3D visualisation. I built it using Next.js, React, TypeScript, Python, FastAPI, PostgreSQL, and Three.js. The team relies on it for real design decisions, which made the project more demanding than building a personal demo. I had to make the output understandable to people who were not thinking about the code itself.

Daedalus shows the practical side of my personality. I like making tools that reduce confusion for a group. I also enjoy the responsibility that comes with software being used by other people: if the system is unclear or wrong, it affects their decisions.

### What my Zeus system does

Zeus is an agentic system that breaks a broad goal into smaller tasks. If a user gives the system a complex instruction, the system organises the work into a directed acyclic graph, decides which steps depend on which others, manages memory, and uses browser automation when necessary.

The system includes importance-weighted memory decay. In simple terms, it tries to retain information that remains important while allowing less useful information to fade. It also includes Playwright automation and a verification loop so that the agent does not merely claim that it completed an action; it checks the result.

I reduced token use by approximately 35%. This project interests me because it combines software architecture with questions about how an intelligent system should organise information. I am interested not only in making agents more capable but also in making them more efficient, inspectable, and reliable.

### What my Glassbox SRE system does

Glassbox SRE is an autonomous site-reliability engineering system. In plain terms, it helps investigate what went wrong when a production software system raises an alert.

The system receives alerts through Prometheus and Alertmanager, places them into a queue, and launches a LangGraph investigation. One part examines recent code changes to identify likely causes. Another retrieves relevant runbooks. A third measures the impact directly from monitoring data. The results are combined into an incident brief with evidence, and the system can generate a postmortem afterward.

I intentionally designed the system so that the language model would not invent important measurements. The impact numbers come from Prometheus, and the incident timeline comes from stored timestamps. I then created 15 test scenarios with known ground-truth commits. The full agent achieved 86.7% top-one accuracy, compared with 13.3% for a deterministic baseline.

This project demonstrates my preference for measurable engineering. I do not want to say that an AI system is intelligent simply because it produces fluent text. I want to compare it against a baseline, define what success means, and identify which part of the architecture creates the improvement.

### What my PhenoSync project does

PhenoSync studies the timing of biological events. Plants may flower, fruit, or mature at different times as climate conditions change. If these changes occur at different rates across species or agricultural systems, the timing of ecological relationships can become misaligned.

I built a pipeline combining species records, satellite measurements, climate observations, and agricultural data. I estimated a shift of 4.57 days per year and checked the result through several statistical frameworks. I then tried to connect the scientific pattern to a practical question: how might this mismatch affect crops and the economic value at risk?

The project shows that I am interested in consequences, not only measurements. I wanted to understand how an environmental change could move through a system and become a risk for agriculture, businesses, and communities. It also required me to work with messy public data, which is very different from working with a clean classroom dataset.

## My activities beyond the main projects

My activity list is broad, but the activities fall into several connected groups: independent research, software building, leadership, service, sport, and professional exploration.

My MalkansView internship gave me professional exposure to finance. The Quant Finance Club gave me a leadership and teaching role. The sports-analysis club allowed me to build a community around one of my interests. IAYP gave structure to my service, physical recreation, and research-development goals. My rural education work made me responsible for whether another person actually understood a lesson. My crowdfunding work made me responsible for practical logistics and delivery.

The research entries show a progression. The Cambridge IPQ was a formal independent qualification. GASI developed into a journal-submitted empirical paper. The Behavioral Ownership Gap applied quantitative research to sport. NEXUS tested a market idea through simulation. PhenoSync extended my work into climate and agricultural risk. The neural-network paper allowed me to explore mathematical AI theory.

The software entries also show a progression. ATLAS is a broad quantitative platform. Zeus studies agentic planning and memory. Daedalus applies software to engineering decisions. Glassbox SRE applies AI to operational reliability. Future Lab uses software to create an interactive learning environment for financial concepts.

## The kind of person I am

I am naturally curious, but my curiosity is not passive. When something interests me, I want to open it up and see how it works. I want to know what is inside the black box, which assumptions are hidden, and whether the output survives testing.

I am ambitious and often set myself goals that are larger than what is immediately comfortable. I have had to learn that ambition is useful only when it is supported by patience and discipline. A project can be technically impressive and still be weak if I have not understood its foundations. My development has been the process of becoming more deliberate about that distinction.

I am persistent, but not because every project goes smoothly. I have experienced failed experiments, null results, rejection, bugs, and periods in which progress was difficult to see. I have continued because I enjoy understanding a problem, even when the outcome is not immediately rewarding.

I am independent, but I do not want my work to exist only for me. The projects I value most are the ones that another person can use: ATLAS is used for analysis, Daedalus is used by my STEM Racing team, Future Lab is used by club members, and my teaching work was useful only if the students could apply what I explained.

I can be intense about work. Once I become absorbed by a question, I may spend longer on it than I originally intended. This helps me persist through difficult problems, but it can also lead me to take on too much. I am learning to manage that intensity, communicate earlier, and choose depth deliberately rather than trying to pursue every interesting direction at once.

I am not naturally motivated by doing something simply because it is expected. I am motivated when I can see the purpose of the work or the question behind it. Once I understand why something matters, I can be extremely committed. This is why I often do more with an open-ended research question than with a narrow task that has no room for interpretation.

I am also more reflective than I may initially appear. The experience with AI tools forced me to examine not only what I had produced but what I actually knew. Since then, I have become more concerned with whether I can stand behind my work. I want to be able to explain my reasoning without hiding behind software, advanced vocabulary, or a polished result.

## How I work with other people

I tend to contribute to groups by making them more capable. I may build a tool, prepare a curriculum, organise a meeting, explain a difficult idea, or handle the practical work that allows a project to continue. I do not always lead through loudness or formal authority. I often lead by creating something useful and maintaining it consistently.

My experience teaching rural children taught me to change my communication based on the learner. My experience with the Quant Finance Club taught me to structure material for a group with different levels of background knowledge. My experience with Daedalus taught me to design for users. My sports-analysis club taught me that people need consistency if a community is going to last.

I appreciate collaborators who challenge my assumptions. I can become attached to an interesting idea, so a good question from another person can help me separate the idea I like from the evidence I actually have. I am learning that collaboration is not only dividing tasks; it is allowing another person to improve the way I see the problem.

## How my interests fit together

At first glance, my activities may seem to cover too many topics: stock markets, neural networks, climate, engineering, football, rural education, and agentic software. The common thread is that I am drawn to systems where many parts interact and where a simple explanation is often inadequate.

In finance, I study how attention, beliefs, and incentives interact. In neural networks, I study how optimisation and mathematical structure produce generalisation. In climate research, I study how environmental changes propagate into biological and economic consequences. In engineering, I study how uncertain inputs create design trade-offs. In sport, I study how people make decisions under pressure and incomplete information. In software, I build tools that make these systems easier to analyse or operate.

The consistent qualities across these activities are curiosity, modelling, experimentation, persistence, and communication. I want to understand complex ideas well enough to make them concrete. I want to test claims rather than simply repeat them. I want to build things that other people can use. I also want to become more disciplined about explaining uncertainty and recognising the boundaries of my conclusions.

## Specific details my teachers may use in a letter

A teacher could describe me as a student who repeatedly creates work beyond the requirements of the curriculum and teaches himself the material needed to do it. A teacher could describe the unusual combination of theoretical and practical ability in my work: I can study eigenvalues and neural-network theory, then build a full-stack platform or simulation that uses mathematical ideas in practice.

A teacher could describe my response to failure. I have had to revise research after peer review, continue after rejection, investigate null results, and debug large systems. The important point is not that I always succeed on the first attempt. I do not. The important point is that I generally become more rigorous after something fails.

A teacher could describe my growth in intellectual ownership. My early mistake with AI tools taught me that producing an answer quickly is not the same as understanding it. I now care deeply about being able to reconstruct, explain, and defend my work.

A teacher could describe my leadership through infrastructure and consistency. I have founded clubs, designed a curriculum, built a market simulation, sustained meetings, and created software that others use. My leadership is often expressed through making participation easier and giving other people something concrete to work with.

A teacher could describe my range without presenting it as random. I am not collecting activities simply to appear busy. I pursue different fields because they help me examine different versions of the same underlying questions about systems, behaviour, evidence, and decision-making.

The most accurate summary is that I am a self-directed builder-researcher. I become interested in difficult systems, learn whatever is necessary to study them, build tools or models that make the questions testable, and keep revising until I can explain what I have done honestly. I am still learning how to balance ambition with sustainability, but I am serious about becoming someone whose work is both technically ambitious and intellectually trustworthy.

## My full activity list, explained in context

### 1. My internship at MalkansView

My internship at MalkansView was my closest experience to working inside a professional finance environment. Before the internship, most of my understanding of markets came from independent reading, datasets, simulations, and personal projects. At MalkansView, I saw how financial research operates when the purpose is not only to learn but to support an actual investment decision.

I learned to look at a company as a business rather than as a ticker symbol. That meant considering its revenue, costs, competitive position, management, growth prospects, financial quality, and risks. I also learned that a good research process requires the analyst to distinguish facts from interpretation and interpretation from prediction. The experience gave me a more realistic understanding of the discipline required in finance and helped me think more carefully about how my own platforms could support research.

### 2. My Sports Analysis Hub

I co-founded and co-hosted a sports-analysis club because I wanted to create a space where people could discuss sport beyond simply saying that a player was good or bad. I was interested in tactics, decision-making, statistics, player roles, and the way evidence can change an opinion.

The most important responsibility was consistency. It is easy to announce a club or have one interesting discussion. It is more difficult to keep arranging meetings, prepare material, and create enough continuity that members want to return. This experience shaped my understanding of leadership. I learned that leadership is often visible in the work that happens before and after the meeting: preparation, follow-up, and making sure other people have a reason to participate.

### 3. My IAYP Bronze and Silver Awards

The IAYP programme gave structure to several parts of my life that I was developing separately. It required me to maintain commitments over time in community service, physical recreation, and skills development. I completed the Bronze and Silver levels and received the corresponding medals.

For the Silver Award, my skills project involved a 26-week programme of quantitative research. I studied artificial intelligence, machine-learning models, and quantitative-trading strategies. The value of the project was not only the subject matter. It required me to sustain progress over many weeks, record what I was learning, and continue when the work became less exciting than it had been at the beginning.

My physical-recreation activity was football goalkeeping. Goalkeeping is a position where concentration and responsibility are unavoidable. A mistake may be immediately visible, but the goalkeeper still has to recover and remain focused on the next decision. That experience connects with how I approach research and engineering: I try to learn from an error without allowing it to determine the quality of the rest of the work.

### 4. My Fund Your Dream crowdfunding work

Through the Fund Your Dream initiative, I helped raise more than ₹25,000 for children in rural villages. The money supported study kits, clothing, and footwear. The activity required outreach, communication, coordination, and practical follow-through.

This was a useful contrast to my technical projects. Software and research often provide an intellectual challenge, but service requires attention to what people actually need. A solution is only useful if it reaches the intended person in a form that helps them. The experience made me more aware of the unglamorous work behind impact and of the responsibility involved in handling other people’s trust.

### 5. My Rural Education Programme

I taught foundational Mathematics and English to more than 50 underprivileged rural children. I had to work with students who did not all have the same educational background, confidence, or pace of learning.

The experience changed my understanding of explanation. Before teaching, I sometimes assumed that if I understood an idea and described it clearly, the communication had succeeded. Teaching showed me that the learner’s response is the real test. I had to change the pace, use different examples, simplify the language, repeat key ideas, and sometimes abandon an explanation that was not working.

This lesson has influenced the way I present technical work. I now try to separate understanding from performance. A person may be able to repeat a definition without understanding it, just as a program may produce an output without the underlying model being reliable. Teaching made me more patient and more attentive to the difference between appearing clear and actually being understood.

### 6. My GASI research paper

GASI is my most developed empirical research project. At a high level, it asks whether investor attention has a threshold effect. Instead of assuming that attention has one simple relationship with volatility, I tried to determine whether the market behaves differently below and above a particular level.

The work required me to learn and apply methods for endogeneity, threshold estimation, cross-sectional dependence, and falsification. It also required me to be careful about language. A statistical relationship does not automatically prove a causal mechanism. I had to distinguish the result I observed from the broader explanation I proposed for it.

The paper’s journey through desk review and peer review also became an education in professional research. A submission is not an endpoint. Reviewers may question the data, the method, the interpretation, or the way the result is framed. Responding well requires more than defending the original idea; it requires understanding which criticism is valid and improving the paper without losing its central question.

### 7. My Behavioral Ownership Gap paper

The Behavioral Ownership Gap paper grew out of my interest in Fantasy Premier League. I wanted to study why the choices made by participants might systematically diverge from what a model would consider optimal. The project treats ownership as a measurable behavioural phenomenon rather than a simple reflection of player quality.

I used a large panel of gameweeks and designed an out-of-sample validation process. The key principle was to avoid changing the model after seeing the validation results. That separation matters because a model can look successful if it is repeatedly adjusted to fit the same data used to judge it.

This project is a good example of my tendency to take ordinary interests seriously. I do not think a subject has to look prestigious before it can produce a meaningful question. The quality of a project comes from the clarity of the question, the care of the method, and the honesty of the interpretation.

### 8. My Zeus system

Zeus is a software system for decomposing broad goals into smaller tasks. A person can express an objective in natural language, but carrying it out may require several dependent actions. Zeus represents those actions as a directed acyclic graph, manages the relevant memory, uses browser automation when necessary, and checks whether the requested outcome has actually occurred.

I built Zeus because I was interested in the difference between an AI system that generates plausible text and an AI system that completes a real task. A useful agent must understand the objective, plan the sequence, use tools, retain important context, and verify its result. The approximately 35% reduction in token use came from making the system more selective about what it retained and processed.

This project reflects my interest in efficiency and structure. I am not interested in adding complexity for its own sake. I want each component to have a reason to exist and to improve the reliability or efficiency of the whole system.

### 9. My ATLAS / QUANT360 platform

ATLAS is the project that most clearly demonstrates my interest in building infrastructure rather than isolated experiments. It brings together a large set of tools that a quantitative researcher might need, from data screening and factor construction to volatility modelling, machine learning, causal inference, and portfolio analysis.

The challenge was not only implementing individual algorithms. I had to make the modules work together, manage data correctly through time, avoid accidental look-ahead, and make the results interpretable. A financial model can appear successful simply because it has unknowingly used information that would not have been available at the time of the decision. I therefore had to think about point-in-time data and survivorship bias as part of the engineering, not as an afterthought.

I also had to improve performance. Research becomes much less useful if every experiment takes too long to run. I vectorised core calculations and removed bottlenecks so that the platform could support repeated analysis. The fact that a CS graduate uses ATLAS gives me evidence that the project has practical value and can be understood by someone outside myself.

### 10. My neural-network exposition

The neural-network paper is different from my market projects because it is primarily theoretical. I did not begin with a dataset or a product requirement. I began with a conceptual problem: how can a highly overparameterised model generalise instead of simply memorising?

I wrote the paper to force myself to understand the mathematical structure rather than rely on explanations that were too advanced or too compressed. I used familiar mathematical tools to build toward the Neural Tangent Kernel and explain how the behaviour of a neural network can be approximated during training.

The work required patience because the most difficult part was often not the final formula but the transition between ideas. I had to ensure that each section prepared the reader for the next one. This is one reason the project matters for a recommendation letter: it shows my interest in theory, my willingness to teach myself beyond the syllabus, and my effort to communicate advanced concepts carefully.

### 11. My IAYP quantitative-research project

The quantitative-research component of IAYP was a sustained learning project rather than a single finished product. Over 26 weeks, I studied AI, machine learning, and quantitative-trading strategies. The long duration required me to maintain a routine and continue learning even when I did not have an immediate external deadline.

This activity helped establish the foundation for later projects such as ATLAS and NEXUS. It gave me time to become familiar with the vocabulary and basic methods before trying to use them in larger systems. It also helped me realise that independent learning is more successful when it is documented and organised rather than treated as a sequence of disconnected discoveries.

### 12. My NEXUS Exchange project

NEXUS is both a software project and a research instrument. The software lets me construct a market with different kinds of agents. The research purpose is to see whether interactions between those agents can generate patterns that resemble real financial markets.

The nine trader archetypes represent different decision rules rather than nine copies of the same trader. Running 10,200 simulations allowed me to examine whether the result was stable across many random conditions. The validation against nine stylised facts made the project more demanding than simply producing a visually convincing simulation.

NEXUS also includes a market maker using reinforcement learning, a liquidity-fragility prediction system, and an inference server. These additions mean that the project contains both a research environment and a working software architecture. It required me to think about modelling, computational efficiency, machine learning, APIs, and evaluation at the same time.

### 13. My Daedalus platform

Daedalus was built for a team rather than for an abstract user. The STEM Racing team needs to make decisions involving multiple objectives and uncertain inputs. The platform helps turn those decisions into something that can be explored systematically.

For example, instead of choosing a design based on one estimated value, the team can examine how the design behaves when the inputs vary. It can see which assumptions matter most, compare alternative scenarios, and identify designs that offer a reasonable balance between competing objectives. Provenance and equation traceability make it possible to see where a result came from.

This project demonstrates that I care about decision quality, not only prediction accuracy. A good tool should help people understand the trade-off they are making and the uncertainty around it.

### 14. My PhenoSync project

PhenoSync expanded my interests beyond finance and computing into climate and environmental systems. The basic question is how changes in climate and biological timing can create mismatches that affect agriculture.

The project required me to integrate several open datasets that were collected for different purposes and may not align perfectly. I had to think about measurement, geography, time, missing data, and robustness. The final economic-risk model was an attempt to make the result more useful to decision-makers: a change in biological timing is scientifically interesting, but understanding how it might affect crop exposure gives the research a practical consequence.

### 15. My NEXUS agentic-architecture paper

Alongside building NEXUS, I wrote a paper about the agentic architecture behind the system. It examines persistent project memory, intent routing, safety hooks, cost telemetry, and parallel agent fleets.

This paper allowed me to step back from implementation and analyse the design principles. I was interested in how a collection of agents could work together without losing track of the user’s intent, exceeding resource limits, or taking unsafe actions. The paper reflects my habit of turning practical building experience into a more general framework that can be explained to someone else.

### 16. My PhenoSync research paper

The PhenoSync paper is the written research version of the broader pipeline. Writing it required me to move from code and results to an argument that a reader could follow. I had to explain why the question mattered, how the data were assembled, what the statistical model measured, how robustness was tested, and what the economic-risk interpretation did and did not claim.

The writing process taught me that a technically strong project can still be difficult to understand if the narrative is not organised. I therefore try to make the question, method, result, and limitation clear before introducing additional complexity.

### 17. My Cambridge IPQ 9980

The IPQ gave me experience working within a formal research framework. I investigated whether high-frequency trading destabilises markets during stress periods and produced a 4,982-word report with research design, analysis, a research log, and bibliography.

Unlike a completely self-defined project, the IPQ required me to meet an external qualification standard. It helped me learn how to plan a long investigation, maintain a record of decisions, and write a conclusion that was proportionate to the evidence. It was also an early step toward the more advanced independent research I later undertook.

### 18. My Glassbox SRE system

Glassbox SRE applies my interest in AI agents to a practical software problem: investigating production incidents. When a system fails, an engineer needs more than a generated explanation. They need to know what changed, what the impact is, which runbook applies, and what evidence supports the conclusion.

I designed the system around that requirement. It gathers evidence from code changes, runbooks, and monitoring data and then produces a brief that cites the relevant findings. The evaluation harness allowed me to measure whether the architecture actually improved incident diagnosis. The large difference between the baseline and the full system gave me a way to isolate the value of reasoning and tool use.

### 19. My Quant Finance Club and Future Lab

The Quant Finance Club is my clearest leadership activity. I did not only join an existing organisation; I founded the club, attracted members, designed a curriculum, and created a substantial project for them to engage with.

Future Lab makes financial ideas interactive. Instead of asking students to read about intrinsic value, mean reversion, industry differences, or market sentiment, it gives them a simulated environment in which they can see how those concepts influence prices. I designed the system so that its assumptions and parameters could be changed, which allows students to explore how different models produce different outcomes.

The club has also taught me that leadership involves translation. I may understand a technical concept, but the club is successful only if other students can understand and use it. I have had to think about sequencing, pacing, examples, and how much complexity is appropriate for a group.

## My final personal portrait

I am a person who is energised by difficult questions and by the feeling that a complicated system is beginning to make sense. I enjoy the moment when an abstract idea becomes a model, when a model becomes code, and when the code produces evidence that can be questioned.

I am independent, but I am not indifferent to other people. The best outcomes of my work are the moments when another person benefits from it: a student understands a mathematical idea, a club member engages with a market simulation, a racing teammate uses a design tool, or another researcher uses a platform for analysis.

I am ambitious, but my ambition has become more thoughtful over time. Earlier, I was tempted by speed and by the appearance of reaching a level before I had earned the understanding. My later work has been shaped by the opposite standard: I want to understand the foundations, test the result, accept criticism, and be able to defend the work without hiding behind a tool.

I am persistent because I care about the question, not because every result confirms what I hoped. I have learned to tolerate uncertainty, rejection, debugging, and slow progress. I still find those experiences difficult, but I no longer see them as evidence that the work was pointless.

I am still learning how to manage the scale of my interests. I can become excited by too many questions at once and take on more than is sensible. I am working on prioritisation, communication, collaboration, and sustainable pacing. I do not want to lose the intensity that makes me curious, but I want to direct it more deliberately.

The clearest description of me is therefore not simply “interested in Computer Science” or “interested in finance.” I am a student who uses mathematics and computing to investigate complex systems, uses research to test ideas, and uses building to make those ideas concrete. I care about ambitious work, but I care just as much about understanding, evidence, usefulness, and intellectual honesty.

## A complete plain-English guide to my work

This section explains my projects in ordinary language. The technical names are included for accuracy, but the important questions are simpler: What was I trying to understand? What did I build? What did I learn? How does the work show who I am?

### How I begin a project

I usually begin with a question rather than a technology. I might wonder why people react differently to the same information, why a market behaves unexpectedly, why an AI system gives an unreliable answer, or how a team can make a better engineering decision.

I then work backwards from the question. I decide what evidence would help, what kind of model might represent the situation, what mathematics I need, what data are available, and what software would allow me to test the idea. This is why my projects use different tools. The tools change, but my process remains similar: question, model, build, test, revise, explain.

I try to make the result useful beyond the original question. A research idea can become a simulation. A simulation can become an educational platform. A technical concept can become a clear explanation. I enjoy moving between those forms because each one reveals something different about the idea.

### MalkansView in simple terms

At MalkansView, I learned how analysts investigate companies before making financial decisions. I studied a company’s business, financial health, growth prospects, competitive position, and risks. I also saw how analysts organise information and decide which evidence matters most.

The internship showed me that finance is not only about numbers or predictions. A company is a real organisation with customers, employees, competitors, management, and changing circumstances. The numbers are evidence about that organisation, not the whole organisation itself.

The experience also gave me a professional comparison for my independent work. When I work alone, I control the question, method, and pace. At MalkansView, I had to work within an existing process, absorb feedback, and understand how another person evaluates research. It made my later financial projects more practical and more careful.

### GASI in simple terms

GASI asks whether investor attention has a tipping point. If very few people are watching a market, a small increase in attention may change trading behaviour. If everyone is already watching, additional attention may have a different effect. I wanted to test whether the relationship between attention and market volatility changes at a particular level.

I studied 22 international markets and built a statistical model to examine this question. The difficult part was that attention and market movement can influence one another. A price change may attract attention, while attention may also affect prices. I therefore had to design the study carefully so I would not mistake one consequence for another.

The main result was a threshold estimate and a pattern I named the “Silence Signature.” During periods of peak attention, volatility appeared to be suppressed rather than automatically amplified. This was counterintuitive, which made it worth investigating. I tested the pattern across individual markets and used additional checks to see whether it might be an accident of one dataset or one model.

The paper passed desk review at *Borsa Istanbul Review* and completed a full peer-review round. I am preparing a resubmission. The most important lesson was that research does not end when an interesting number appears. I had to defend the data, the method, the interpretation, and the limits of the conclusion.

### The Behavioral Ownership Gap in simple terms

The Fantasy Premier League paper asks why real participants may make different choices from the choices suggested by a model. A player may be popular because of reputation, a recent performance, social influence, or media attention. A model may judge the player using expected performance, price, fixtures, risk, and available alternatives.

I created a way to measure the difference between those two kinds of choice and studied the pattern over 380 gameweeks. I treated the Fantasy Premier League as a behavioural market: people repeatedly make decisions using imperfect information, and their decisions create measurable outcomes.

I designed a separate out-of-sample period to test the model after developing it. This matters because a model can look successful if it is repeatedly adjusted to fit the same data used to judge it. The project taught me to be cautious around unusually strong results and to separate development from validation.

This project also shows how my personal interests become academic questions. I enjoy football, but I am also interested in information, incentives, judgement, and behaviour. I like finding serious questions inside familiar activities.

### NEXUS Exchange in simple terms

NEXUS is a simulated market built from the behaviour of its participants. Instead of beginning only with historical price charts, I created different kinds of traders and allowed them to interact. Some traders follow trends, some look for prices that seem too high or too low, some provide liquidity, and others react to changes in risk.

I ran thousands of simulations because a single simulation can produce an interesting pattern by chance. I wanted to see whether the behaviour appeared repeatedly under different random conditions. I compared the simulated market with known features of real markets, such as sudden extreme price movements and periods in which volatility stays high.

NEXUS also allowed me to test the central GASI finding through a different route. Recovering the same threshold in a separate model does not prove the original result, but it gives the idea another form of support and helps identify what kinds of behaviour might produce it.

The project taught me that complexity is not the same as realism. A simulator can have many components and still fail to represent the real world. Validation matters more than the number of features.

### My neural-network paper in simple terms

My neural-network paper begins with a puzzle. A model with an enormous number of adjustable parts seems as if it should memorise its training examples and fail on new examples. Yet many large neural networks perform well on data they have not seen.

I wrote the paper to understand why this can happen. I used mathematics to describe what happens to a neural network during learning and explained how its behaviour can sometimes be approximated by a simpler mathematical object called the Neural Tangent Kernel.

The paper discusses how a network represents information, how gradient descent changes it, how eigenvalues affect learning, and why simpler or smoother patterns may be learned before complicated ones. I included a small two-neuron example and worked through it line by line so the reader would not have to accept a general statement without seeing the mechanism.

This project shows how I respond to material beyond the syllabus. I do not want to repeat an advanced explanation without understanding it. I want to rebuild enough of the argument that I can explain what each part means, where the approximation applies, and what questions remain open.

### PhenoSync in simple terms

PhenoSync studies changes in the timing of biological events. Plants, crops, insects, and other species respond to temperature and seasons. If different parts of an ecosystem change at different speeds, events that used to happen together may no longer line up.

I combined species records, satellite observations, weather information, and agricultural data. The sources were collected for different purposes, so they did not automatically fit together. I had to consider dates, locations, missing information, and differences in measurement.

The project found a measurable shift in biological timing and then asked what it could mean for agriculture. I did not want to stop at describing an environmental change. I wanted to explore how it might create exposure for crops and become an economic risk that decision-makers could understand.

PhenoSync taught me that data analysis begins before the model. If the data are not aligned, a sophisticated statistical method cannot rescue the conclusion. It also taught me that a scientific result becomes more useful when its possible consequences are explained clearly.

### ATLAS in simple terms

ATLAS is a large workbench for studying financial data. Instead of creating a separate small script for every question, I built one platform containing tools for studying companies, markets, risk, portfolios, and possible causes of changes.

The platform can help investigate which company characteristics relate to returns, how risk changes over time, whether an event appears to affect a market, and how a portfolio might be constructed. It also includes methods for distinguishing a relationship from a possible cause.

The difficult part was making the tools trustworthy together. A model can appear successful if it accidentally uses information from the future. A historical test can also look better if it ignores companies that later disappeared. I therefore had to think about the timing and quality of data as part of the engineering.

I also improved the platform’s speed so that it could support repeated analysis. ATLAS is used by a CS graduate for real work, which matters to me because I want my software to be useful outside my own computer.

### Daedalus in simple terms

Daedalus helps my STEM Racing team make engineering decisions when there is no single perfect design. A design may be lighter but less robust, faster but harder to manufacture, or stronger but heavier. Improving one objective can make another objective worse.

The platform lets us vary uncertain inputs, compare scenarios, see which assumptions matter most, and identify balanced designs. It records where values came from and how calculations were made, so a teammate can trace a result back to the relevant equation or assumption.

This project taught me to design for a real user. The team does not need a complicated system for its own sake. It needs information that is understandable and useful under practical constraints. I therefore had to think about communication as carefully as computation.

### Zeus in simple terms

Zeus is an attempt to make an AI system better at carrying out a complicated objective. A broad request often contains several smaller actions, and some actions cannot begin until earlier ones are complete.

Zeus organises those actions, decides which information is important to retain, uses browser automation, and checks whether the requested outcome actually occurred. I wanted to move beyond a system that produces plausible text toward a system that completes and verifies a real sequence of actions.

The project also made me think about limits. An agent should not retain every piece of information forever, use every available tool without a reason, or claim success without checking. The design therefore combines planning, memory, efficiency, and verification.

### Glassbox SRE in simple terms

Glassbox SRE helps investigate software failures. When a production system raises an alert, an engineer needs to know what changed, what might be responsible, how many users are affected, and what should be done next.

I built a system that gathers evidence for those questions. It examines recent code changes, searches technical instructions, reads monitoring information, estimates impact, and produces an incident report. It can then create a postmortem so the organisation can learn from the failure.

I designed the system so the AI would not invent important figures. Measurements come from monitoring data, and the timeline comes from recorded events. I also created test cases with known answers and compared the complete system with a simpler baseline.

This project shows my attitude toward AI. I am excited by what AI can do, but I do not want to trust it merely because its language sounds confident. I want to know what evidence it used, how it arrived at a conclusion, and whether it performs better than a simpler approach.

### Future Lab in simple terms

Future Lab is a simulated stock market I built for the Quant Finance Club. It gives students a way to see how companies, industries, information, and expectations can influence prices.

The system creates companies with different financial characteristics and places them in different industries. It estimates an underlying value and allows the market price to move around that value as new information appears. A price can therefore become too high or too low for a period of time without moving randomly.

I made the assumptions changeable so students can explore different scenarios. They can see what happens when growth matters more, when an industry is more sensitive to financial strength, or when prices return to fair value more quickly. Future Lab is therefore both a software project and a teaching tool.

## Other work that matters to my development

### Independent learning

A large part of my education happens outside formal classes. I read research papers, study documentation, compare implementations, and write small experiments to understand unfamiliar concepts. I often learn a simple version first and then return to the advanced material once I have something concrete to connect it to.

Independent learning gives me freedom, but it also means I have to decide what to learn next. I have had to recognise when I am missing a foundation, narrow a project when it becomes too broad, and distinguish useful difficulty from unnecessary complication.

### Writing and documentation

I write because writing forces me to decide what I actually believe. Code can contain many features, but a paper needs a question, an argument, evidence, and a conclusion that does not claim more than the evidence supports.

I document my systems so that I can return to them and so that another person can understand them. Documentation includes the purpose of a project, its assumptions, its limitations, and the way its components connect. This habit has helped me become more precise and has made me more aware that a system is not truly usable if only its creator understands it.

### Connecting subjects

My independent work gives me reasons to return to school subjects. Matrices and eigenvalues become useful when I study neural networks. Statistics becomes useful when I analyse market behaviour or climate data. Economics becomes useful when I study incentives and value. Physics and engineering become useful when I think about uncertainty and design trade-offs. English becomes useful when I explain a complex project to someone without the same technical background.

I therefore do not see my subjects as isolated boxes. I want to understand how they work together when a real problem is too complicated for one subject alone.

## How my activity list fits together

My activity list is broad, but it is not random. The research entries show my development from formal independent investigation to original papers, simulations, and interdisciplinary work. The technology entries show my development from learning to build software to designing systems that other people can use. The leadership entries show that I do not only work alone; I create clubs, curricula, and tools for other students.

The service entries show a different side of me. Teaching rural children required patience and adaptation. Fundraising required practical follow-through. IAYP required consistency over time. Football gave me a physical activity that demanded concentration and recovery.

Together, these activities show a person who likes understanding systems but also cares about usefulness. I do not want my work to remain an abstract exercise. I want it to teach somebody, support a teammate, help a club, improve a decision, or make a difficult idea easier to understand.

## My final personal portrait

I am curious, but my curiosity is active. When something interests me, I want to open it up and understand how it works. I want to know what assumptions are hidden, which parts are uncertain, and whether the result survives testing.

I am ambitious, but I have learned that ambition has to be supported by patience. Earlier, I sometimes wanted to reach a difficult result before I had earned the understanding underneath it. My later work has been shaped by a different standard: I want to understand the foundations, test the result, accept criticism, and explain the work without hiding behind a tool or a technical phrase.

I am persistent because I care about the question, not because every result confirms what I hoped. I have experienced failed experiments, null results, bugs, rejection, and slow progress. I still find those experiences difficult, but I no longer see them as proof that the work was pointless.

I am independent, but I am not detached from other people. The work I value most is work that another person can use: a student understands a mathematical idea, a club member explores a market simulation, a racing teammate uses a design platform, or another researcher uses a quantitative tool.

I am still learning how to manage the number of questions I want to pursue. I can take on too many demanding projects and sometimes hold myself to a standard that makes communication harder than it needs to be. I am working on prioritisation, collaboration, earlier communication, and sustainable pacing.

The best description of me is not simply that I am interested in Computer Science or finance. I am a student who uses mathematics and computing to investigate complex systems, uses research to test ideas, and uses building to make those ideas concrete. I care about ambitious work, but I care just as much about understanding, evidence, usefulness, clarity, and intellectual honesty.

## Teacher-ready summary of my activities

My MalkansView internship introduced me to professional company and market research and showed me how analysis supports real financial decisions.

My Sports Analysis Hub showed me that I can turn an interest in sport into a consistent community and lead through preparation and reliability.

My IAYP Bronze and Silver Awards show that I can sustain long-term commitments across community service, physical recreation, and independent learning.

My Fund Your Dream work shows that I have participated in practical service involving fundraising, coordination, and delivery of useful materials.

My rural education work shows that I can teach patiently, adapt explanations, and focus on whether another person has actually understood.

My GASI paper shows that I can develop an original question, learn advanced methods independently, analyse data across several markets, respond to peer review, and continue after criticism.

My Behavioral Ownership Gap paper shows that I can connect a personal interest in football to a serious question about behaviour, information, and decision-making.

Zeus shows that I can design an AI system around planning, memory, tool use, efficiency, and verification rather than only text generation.

ATLAS shows that I can build a broad research platform and make it useful to another researcher.

My neural-network exposition shows that I can teach myself advanced mathematical ideas and explain them from first principles.

My IAYP quantitative-research project shows that I can maintain a learning commitment over 26 weeks.

NEXUS shows that I can turn a market theory into a simulation, run large experiments, and check the simulation against known patterns.

Daedalus shows that I can build software for real users and support engineering decisions involving uncertainty and trade-offs.

PhenoSync shows that I can combine environmental data, statistical analysis, and economic interpretation in one project.

My NEXUS architecture paper shows that I can step back from implementation and explain the general principles behind a system.

My PhenoSync paper shows that I can turn a data pipeline into a coherent written research argument.

My Cambridge IPQ shows that I can complete a formal independent research qualification with a structured report and documented process.

Glassbox SRE shows that I care about measuring whether an AI system works and designing it so that important claims are supported by evidence.

The Quant Finance Club and Future Lab show that I can found an organisation, design a curriculum, build an educational platform, and help other students engage with difficult ideas.
