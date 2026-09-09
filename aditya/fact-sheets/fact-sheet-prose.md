# Aditya Balaji — Teacher Fact Sheet

## Academic profile

### Student overview

Aditya Balaji is a Cambridge International student at JBCN International School in Mumbai. His academic interests include Computer Science, Mathematics, Further Mathematics, Economics, Physics, artificial intelligence, data science, and quantitative finance. These interests are closely connected: he is drawn to problems involving complex systems, mathematical modelling, human behaviour, and the design of reliable software.

### Academic interests

- **Mathematics:** probability, statistics, optimisation, differential equations, linear algebra, and mathematical modelling.
- **Computer Science:** algorithms, software architecture, data engineering, machine learning, and agentic systems.
- **Economics and finance:** market behaviour, volatility, market microstructure, behavioural finance, and quantitative modelling.
- **Artificial intelligence:** how models learn, why they generalise, and how AI systems can be tested and made more reliable.

### Learning approach

Aditya learns best when he can understand why a method works and then apply it to a real problem. When he encounters a difficult question, he breaks it into smaller parts, teaches himself the missing material, builds an initial model or system, tests it, and revises it when the evidence exposes a weakness. This approach has shaped both his academic work and his independent projects.

### The shortest accurate description

Aditya is a self-directed builder-researcher. He learns difficult material when a real problem requires it, builds tools rather than stopping at ideas, and keeps revising when evidence or criticism exposes a weakness.

### Three themes that connect his work

1. **Mechanism:** He wants to understand why something works, not only reproduce a method.
2. **Evidence:** He tests ideas against data, simulations, robustness checks, or real users.
3. **Usefulness:** He tries to make research or software understandable and useful to someone beyond himself.

### Strongest evidence to mention

- Corresponding-author research on investor-attention thresholds across 22 equity markets, submitted to *Borsa Istanbul Review* and taken through peer review.
- A quantitative-research platform used by another CS graduate for analysis.
- Daedalus, an engineering decision platform used by his STEM Racing team for real design trade-offs.
- NEXUS Exchange, an agent-based market simulator used to test an empirical finding through an independent computational model.
- Quant Finance Club, which he founded and developed into a 25–30-member organisation with a 13-week curriculum and a working market simulation.
- Teaching and community work that required consistency and adaptation, not just one-off participation.

### How to describe him credibly

The most useful recommendation will include one or two specific moments: a time Aditya changed his method after criticism, explained a difficult idea to others, helped a team make a decision, or stayed with a project after the initial result failed. His work is technically ambitious, but the more revealing point is how he responds when ambition meets error, ambiguity, or resistance.

Avoid describing him only as “passionate,” “hardworking,” or “good at coding.” Those words are less informative than describing what he built, what went wrong, what he changed, and how other people were affected by his work.

## Who I am

I am a student at JBCN International School in Mumbai, studying the Cambridge International curriculum. My academic interests sit between Computer Science, Mathematics, Further Mathematics, Economics, Physics, artificial intelligence, data science, and quantitative finance. I do not think of these as separate interests. I am most interested in problems where they overlap: how people and algorithms behave in markets, how mathematical models can explain complex systems, how software can help people make decisions, and how evidence can distinguish an attractive idea from a reliable one.

I learn best when I can understand why something works and then use that understanding to build or test something. I am not satisfied with memorising a method if I do not understand its assumptions. When I encounter a difficult question, I usually break it into smaller questions, teach myself the missing material, build an initial model or system, test it, investigate what fails, and revise it. This is the way I have approached both my academic work and my independent projects.

I am strongly self-directed. Many of my most important projects began as questions I had become interested in rather than as school assignments. I have learned statistics, causal inference, financial modelling, machine learning, software architecture, data engineering, and agentic AI systems because those were the tools I needed for the problems I wanted to investigate. I enjoy the process of learning enough of a new subject to make something real with it.

My central habit is turning curiosity into a working system. I have written research papers, built quantitative-finance platforms, created market simulators, developed engineering software for my STEM Racing team, designed an autonomous incident-response system, founded student clubs, taught rural children, and used football and Fantasy Premier League as contexts for analysis. The subjects vary, but the underlying process is consistent: I ask a question, make the question precise, build something that can produce evidence, and try to understand the limitations of the result.

## Academic interests

Mathematics is one of the foundations of my work. I am especially interested in linear algebra, probability, statistics, optimisation, differential equations, and mathematical modelling. Further Mathematics has given me tools that I have used in independent work, including matrices, eigenvalues, diagonalisation, Taylor series, and ordinary differential equations. I enjoy mathematics most when it is not just an exercise but a language for understanding a real mechanism.

Computer Science gives me a way to turn an idea into something executable. I enjoy designing systems, thinking about how components interact, improving performance, and making a tool useful to somebody other than myself. I am interested in both the theoretical side of computing and the engineering required to make a system reliable. A project is not complete for me merely because the interface looks good or the code runs once; I want to know whether the underlying reasoning is valid and whether the result can be tested.

Economics and finance interest me because they involve interacting people, institutions, incentives, expectations, and incomplete information. I am particularly interested in market microstructure, behavioural finance, volatility, causal inference, and the difference between an asset’s underlying value and its observed price. I like the fact that financial questions require both mathematical discipline and an understanding of human behaviour.

I am also interested in artificial intelligence, especially how neural networks learn, why large models can generalise, and how agentic systems can plan and verify actions. I do not want to use advanced terminology without understanding the mechanism beneath it. When I study a concept, I try to reduce it to something I can derive, implement, test, or explain in my own words.

## Research and independent projects

My main research project, the Global Attention Saturation Index, studies how investor attention relates to volatility across 22 international equity markets. I wanted to know whether attention behaves in a simple linear way, or whether the market changes once attention reaches a certain level. To investigate that question, I assembled a cross-market dataset, defined an attention measure, and tested for a structural threshold rather than assuming that one relationship applied everywhere.

The analysis used a Lewbel instrumental-variable strategy to address endogeneity, Driscoll-Kraay standard errors to account for dependence across markets, and synthetic-control falsification tests to examine whether the result could be explained by an unrelated pattern. I estimated a structural threshold of gamma*=1.5625, with a Hansen confidence set of [1.14, 2.50]. The paper identifies what I call the "Silence Signature": during the highest-attention regime, volatility can fall rather than continue rising. I found the pattern individually in 14 of the 22 markets studied.

I was the corresponding author of the paper, which was submitted to *Borsa Istanbul Review*. It passed desk review and completed a full peer-review round. The most valuable part of the project was learning that a result is only the beginning of research. I had to defend the design, respond to criticism, check alternative explanations, and be clear about what the data could not prove. That process changed the way I approach every later project.

I also developed a research paper on decision-making in Fantasy Premier League. I treated the game as a behavioural market in which participants make repeated choices with incomplete information. The central idea was the Behavioral Ownership Gap: the difference between the players that a rational model would select and the players that people actually own. That gap allowed me to study the cost of predictable human behaviour in a setting with public data, repeated decisions, and measurable outcomes.

I built a Fama-MacBeth panel covering 380 gameweeks and examined whether ownership patterns predicted later performance. The analysis produced a t-statistic of -57.20 and an estimated annual welfare cost of GBP 137.1 million. I then froze the model before conducting an out-of-sample validation, rather than changing the specification after seeing the result. The validation produced 105 profitable weeks out of 105 in an equity long-short replication. The paper is under review at the *Journal of Sports Economics*.

The project matters to me because it connects something I enjoy, football, with questions from economics, statistics, and decision theory. It also taught me to separate a strong backtest from a reliable finding. A model can look impressive because it has been adjusted too closely to the past; the real test is whether it continues to make sense when the data it has not seen arrives.

NEXUS Exchange is a market simulator that I used to explore whether an empirical finding could also appear in a separate computational model. I created different types of traders and tested how their behaviour affected the market. The project helped me understand that a model is valuable only when its assumptions are clear and its behaviour can be checked against reality.

I wrote a mathematical exposition titled “Why Overparameterised Neural Networks Generalise.” In the paper, I derive the Neural Tangent Kernel from first principles using mathematics available through my Further Mathematics background. I discuss the bias–variance paradox, neural networks as linear maps, gradient descent as a dynamical system, Gram matrices, eigenvalue structure, spectral bias, and why overparameterisation can result in a well-conditioned kernel. I also include a fully worked two-neuron example, calculated line by line. The project allowed me to study a frontier question in AI theory without treating the theory as a collection of words I had memorised.

PhenoSync is an open-data climate and phenology project. I combined public information about species, temperature, vegetation, and agriculture to study how seasonal changes can affect ecosystems and crops. The project gave me experience working with messy real-world data and checking whether a result remained stable when the method changed.

I completed the Cambridge IPQ 9980 as an independent research qualification. My 4,982-word report investigated whether high-frequency algorithmic trading destabilises financial markets during periods of stress. I completed the research design, empirical analysis, research log, and bibliography according to Cambridge’s formal assessment criteria. The IPQ gave me experience with a structured independent investigation and helped me understand the difference between an interesting topic and a properly designed research question.

## Selected projects

### Quantitative research platform

I developed a quantitative-research platform that brings together market screening, portfolio analysis, volatility models, factor research, and machine learning. It began as a way to organise my own work, but it grew into a system another CS graduate could use for real analysis. I paid attention to point-in-time data, survivorship bias, out-of-sample testing, and the difference between a promising backtest and a result that deserves trust. The technical work mattered because it gave the research a reliable base; the real achievement was turning a collection of methods into something another person could inspect, question, and use.

### Daedalus - STEM Racing decision platform

For my STEM Racing team, I created Daedalus, a platform that helps us compare design choices. It checks units, records where inputs come from, explores alternatives, and shows how a decision changes when assumptions move. The system combines a Next.js and React interface with a Python and FastAPI backend, a PostgreSQL database, and 3D visualisation. I did not build it as a technical display piece; teammates use it when an actual design decision has to be made. That forced me to make complicated analysis readable, traceable, and useful under time pressure.

### Zeus and Glassbox SRE

I explored two practical applications of AI. Zeus breaks broad goals into smaller actions, uses browser automation when needed, and checks whether the task was actually completed. Glassbox SRE investigates software incidents by connecting alerts, code changes, runbooks, and system data into an evidence-based report. I designed the second system so important numbers come from monitoring data rather than from the language model's guesswork, then tested it against seeded incidents. These projects pushed me toward a view of AI that is both ambitious and demanding: a system should do useful work, but it should also show where its conclusions came from.

## Leadership, sport, and service

I founded and run the Quant Finance Club, which has approximately 25–30 members. I designed a 13-week curriculum covering markets, valuation, and quantitative methods. The club’s flagship project is Future Lab, a simulated stock market containing approximately 150 companies across 15 industries. I designed an intrinsic-value engine based on financial quality and a price-driver engine that models earnings surprises, news sentiment, institutional flow, and other factors. Prices are tethered to intrinsic value using an Ornstein–Uhlenbeck mean-reversion process, allowing them to deviate from fair value while remaining structurally connected to it.

Future Lab is configuration-driven. The weights, coefficients, and formula parameters are stored in the database, so the simulation can be recalibrated without changing the code. It also supports timeline branching, allowing users to explore alternate futures from a particular point in the market’s history. I built it not only as a technical project but as a way for other students to interact with financial concepts rather than only hearing about them.

I co-founded and co-hosted a sports-analysis club. My responsibility was not limited to having the original idea; I helped initiate meetings and maintain a consistent space that members continued returning to. This taught me that leadership is often based on reliability rather than a formal title. A group becomes meaningful when somebody keeps showing up, prepares something useful, and creates enough continuity for other people to participate.

I play football and have participated as a goalkeeper through the IAYP physical-recreation component. Goalkeeping requires concentration, anticipation, accountability, and recovery after mistakes. I enjoy the relationship between sport and analysis, which is one reason I became interested in Fantasy Premier League behaviour. Sport is both something I participate in and a setting through which I explore decision-making and incentives.

I completed the IAYP Bronze and Silver Awards. My Silver programme combined community service, football goalkeeping, and a 26-week quantitative-research skills project focused on AI, machine-learning models, and quantitative-trading strategies. I also taught foundational Mathematics and English to more than 50 underprivileged rural children. I learned that teaching is not successful merely because I have explained something; it is successful when the student has understood it. I had to adapt the lessons and delivery when a method did not work.

Through a crowdfunding initiative, I raised more than INR 25,000 to provide study kits, clothing, and footwear to underprivileged children in rural villages. This experience showed me that community work is often made up of logistics, outreach, and repetitive follow-through rather than one dramatic moment. I value that kind of practical work because it produces a direct benefit for somebody else.

## Coursework and academic qualifications

My Cambridge International coursework includes Mathematics, Further Mathematics, Computer Science, Economics, Physics, and English General Paper. I also completed the Cambridge IPQ 9980, an independent research qualification. My 4,982-word report examined whether high-frequency algorithmic trading can destabilise financial markets during periods of stress. The IPQ gave me experience with designing a research question, managing evidence, keeping a research log, and writing to formal academic criteria.

## Internship and practical experience

During a three-month internship at MalkansView, a stock-market research firm, I worked with live market data and studied how analysts assess companies. I looked beyond individual price movements by considering revenue, costs, competitive position, management, growth, financial quality, and risk. The experience helped me understand how research moves from evidence to an investment decision and gave me a professional setting in which to strengthen my analytical discipline.

## Personal qualities and hobbies

People who know me well would describe me as curious, self-directed, persistent, and thoughtful. I enjoy difficult problems, but I also value the process of explaining them clearly and working with others. I play football, particularly as a goalkeeper, and I enjoy music, including playing the guitar and piano. These activities give me a balance between analysis, concentration, creativity, and teamwork.

## What I am most proud of

I am proud that I have taken ideas that began as questions and carried them far enough to become research papers, working software, or tools other people can use. The scale of some of this work goes well beyond what is normally expected from a student at my stage, but the part I value most is the responsibility behind it: learning the mathematics, checking the code, listening when someone finds a weakness, and staying with the project after the first version fails. I am also proud of the quieter work, such as teaching children, supporting a team, and creating clubs that other students could return to.

## LOR guidance for recommenders

### What I hope my letters will show

The strongest letters for me would be specific and personal rather than a list of achievements. My work often goes well beyond the usual level of independent work expected from a student of my age, but a recommender should not need to make that claim on its own. The letter should show it through one or two moments: a question that moved beyond the syllabus, a paper or project that required university-level reading, a technical problem I stayed with, or a time I changed my approach after a teacher pointed out that my first answer was incomplete.

I would also want the letters to show the person behind the work. Admissions readers should see someone who is intensely curious but still teachable, ambitious but willing to test his own ideas, and capable of working independently without becoming detached from the people around him. That combination matters more to me than a string of superlatives.

The letter should feel like it comes from someone who has actually taught or mentored me. It should use one or two moments from class, a project, a discussion, or a difficult piece of work to show how I think and how I respond when the first answer is not good enough. The strongest description of me would hold two things together: the unusual level of independence and technical ambition in my work, and the fact that I am still willing to be corrected, learn from other people, and explain my ideas clearly.

## Personal growth and intellectual integrity

One of the most important experiences in my development involved my early use of AI tools. After my tenth-grade Computer Science board examination, I had decided that coding was the one thing I would never do. Later, AI tools made coding appear accessible, and I began using them to reach problems I could not yet solve. At first, I became too focused on the speed of the result. I submitted research work that I could not defend properly, and my teacher identified the gap.

The lesson was not that AI tools were inherently wrong. The lesson was that I had allowed a tool to make a decision I did not understand. I had optimised for finished rather than understood. Since then, I have kept using AI tools, but I require myself to verify, reconstruct, and defend important work. They can help me draft, search, or suggest, but the final reasoning has to be mine. This has made me more rigorous and more honest about the difference between receiving an answer and learning something.

That standard was tested during my research work. I have worked on projects where the expected effect did not appear in the data. I cleaned the data, changed variables, reran models, and checked the code from different directions. I have also experienced rejection from journals. I continued because I learned to separate the value of doing careful work from the outcome I hoped to receive. I still want my work to be published and used, but I do not want publication, praise, or a good result to be the only reason I trust my reasoning.

I am still developing. My ambition sometimes leads me to take on too many demanding projects at once. I can move faster than my understanding if I do not deliberately slow down. I am working on communicating earlier, asking for help sooner, prioritising more effectively, and distinguishing useful perfectionism from unnecessary perfectionism. I want to preserve my curiosity and intensity while becoming more sustainable and collaborative.

## What I hope teachers understand about me

I am not simply a coding student or a finance student. I am interested in complex systems, and I learn whichever mathematics, computing, economics, science, or communication skills are necessary to investigate them. My projects may appear broad, but they are connected by the same questions: What is the mechanism? What evidence supports it? What would falsify it? Can I build something that makes the idea testable or useful?

I respond well to teachers who ask me to justify assumptions, explain technical ideas in plain language, identify limitations, and describe what would change my mind. I appreciate direct feedback, especially when it identifies a specific weakness that I can address. I may sometimes explore too many possibilities or hold myself to an unnecessarily high standard, but I care deeply about improving the quality of my work.

The most accurate description of me includes both what I have made and how I have changed. I have built substantial technical and research projects, but the more important development has been learning to take complete intellectual responsibility for them. I want to study a field where mathematics, computing, data, and real-world systems meet. I want my work to be ambitious, technically sound, useful to other people, and defensible when someone asks me to explain exactly why I believe what I believe.
