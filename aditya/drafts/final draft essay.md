# Final Essays (Early Action 2026–27)

Single source for the Common App essay and every EA supplement. Essay.docx in Downloads is built from this file.

## Common App Personal Statement

The journal's email arrived two weeks early, during a computer science class. My friend Veer grabbed my phone and read the screen in his announcer voice: "Decision on your manuscript." Nobody sees my results before I do, so I took it back, meaning to open it at home, alone. I lasted until the stairs, friends leaning in. Rejected, with ten reviewer comments. Nobody leaned in after that.

"It's fine," my friends said, as I say to everyone, and I hated hearing it because it sounded like pity for my own mistake. At home, I put on Bhaja Govindam, a Sanskrit hymn that keeps calling the listener mudhamate, foolish mind. Somehow, being insulted in Sanskrit is the calmest part of my day. That night, for once, I agreed with it. I had been warned twice, and both times I had listened only to the half I liked.

In my tenth-grade board exam, I knew the logic but couldn't write a line of code. Around me, pens kept moving. Afterward I cried, barely spoke for three days, and told my older brother I would never study computer science like him. That summer, he pasted our syllabus into an AI tool, and a notes site built itself on the screen. He said I could use it as long as I understood what it built. I heard "use it."

In eleventh grade, I wanted to know why two companies could report strong earnings while only one stock jumped. I asked AI what researchers had found and drafted a paper around its answers. The sentences were mine. The ideas weren't. My research teacher asked me to explain it as if he knew nothing, and I couldn't.

I started over with data from 21 markets. This time AI wrote only the code I hate typing; I decided what it built. Months later, my model found that once trading hits about 1.4 times its usual level, a market starts to swing. Proud of it, I told my teacher I was ready to send it to a journal. "Take your time," he said. "Learn what a journal wants. Know the question. Understand the content." I heard "take your time" and spent it on the model.

The first journal rejected the paper without review, and only then did I read what it publishes. The second sent it to reviewers, and I was happier than I let anyone see. Its decision was the email on the stairs. One reviewer found the idea "interesting," my introduction "really difficult to follow," and my equations "really confusing for the audience." That stung, because out loud I could explain it. I had walked my friends through it with Nvidia: if everyone watches the same stock, when does attention make its price swing? They got it. On the page, I had written for the one reader who already understood it: me.

I reread the paper the way a stranger would, one claim at a time, and cut whatever I couldn't defend. I had crammed in too many questions, so I kept one. For days I looked for reasons to keep the results that answered the others, because each had felt like proof I was serious. Just before midnight, I moved them into a file called results.docx.

In the car, my father always plays the same hymn and explains it word by word. When he reaches mudhamate, I cut in: "Foolish mind. I know." He smiles and explains it anyway, in case I've forgotten I'm being called a fool.

I rewrote the paper for a reader who knows nothing, every number after the sentence that explains it. Before opening eight months of new data, I wrote down my tests so I couldn't bend them. One failed. It stayed in the paper. I sent it to the same journal again, and I still reload the portal.

Now, when my father reaches mudhamate, I let him finish.

## University of Illinois Urbana-Champaign

### Experience related to your major

I built a stock market that does not exist. In NEXUS, simulated traders trade with one another. Some copy the crowd, some chase rising prices, some always take the other side.

I needed it because my research found that prices swing more once investor attention passes a certain level, and history cannot be rerun to test why. I reran a simulated market 10,200 times.

The hardest question was whether a fake market behaves like a real one. Real markets show nine patterns, like rare huge jumps and wild days arriving in bunches. After tuning, one run matched all nine. Only six of ten fresh random draws matched all nine. Changing just how the program drew its random numbers dropped the perfect run to five of nine. What I had tuned was one lucky run, which says little about a market. Now every result I report lists the runs it failed.

### Goals after graduating

Harvey, Liu and Zhu argue that most published ways to predict stock returns are probably false, because researchers publish the lucky ones. After Illinois, I want to work in quantitative trading, on the systems that decide whether an idea survives a real market.

As an intern at a Mumbai finance firm, I backtested trading strategies, and the best-looking ones quietly assumed there would be no stop-losses, or that a pattern which held for five years would hold for the sixth. Nobody had written those assumptions down, so I began listing them.

CS 425, Distributed Systems, would teach me how an exchange decides which of two simultaneous orders goes first, and CS 442, Trustworthy Machine Learning, how a model can be fooled and how to detect it. My co-author on both of my journal papers is at Illinois, which is a large part of why I want to study there.

### Second-choice major

Most of the mathematics in my research arrived when a result needed defending. In my paper on investor attention across 21 markets, the first test treated each country as separate, so I switched to Driscoll-Kraay standard errors because markets tend to fall together, and later corrected for the number of things I had tested. Both fixes worked, but I learned them from other researchers' papers and could not have derived either one myself. That gap is the reason Mathematics is my second choice. At Illinois, MATH 461, Probability Theory, would give me the theory behind the tests I already run, and MATH 415, Applied Linear Algebra, the structure underneath the factor models I built for ATLAS. I would rather understand why a method holds than keep borrowing it and hoping the assumptions fit.

## University of Wisconsin–Madison

### Why UW–Madison and Computer Sciences

Most of my projects started as an argument with a number. My research paper found that stock prices start swinging more once trading passes a certain level. The numbers said the jump was real, but they said nothing about who was causing it.

So I built a market to find out. NEXUS is a program in which nine kinds of simulated traders buy and sell from one another, and every vague idea about investors had to become a rule about what each trader can see, how long it remembers and whom it copies. My paper said it in four words, "traders copy each other," but NEXUS made me decide how quickly they copy and when they stop, and each choice could break the market. My first version let traders copy forever, and within a few simulated days every one was buying the same stock. When people asked how the traders talk to one another in real time, my answer came out vague, so I wrote a paper on NEXUS's architecture to find out whether I knew. Writing code is the most honest test I have found of whether I understand something. That is why I want to study Computer Sciences.

I did most of that work alone, and the gaps showed up after I had built on them. I taught myself statistics only when a result needed defending. At Madison I want the foundations first. STAT 340 teaches Monte Carlo simulation, the formal version of running NEXUS thousands of times, and COMP SCI 532, Matrix Methods in Machine Learning, covers the math behind the prediction models I added to it.

I would join Traders at Wisconsin. I founded my school's market club and wrote its course; here I want to be the new member. My other paper found that Fantasy Premier League managers rush to buy players who just got lucky. I would bring that finding to the Sports Analytics Club and see whether it survives people who know sports data better than I do.

I most want to work on Professor Frederic Sala's question. His Sprocket Lab works on data-centric AI and has built benchmarks, and I keep running into the problem they address, how to know a model works when mine did not. After tuning NEXUS, one run matched all nine real-market patterns I checked, and I called it done. Only six of ten fresh runs matched all nine. I want to learn to design a test a model cannot be tuned to pass, because tuning until it passed is exactly what I did. That is also why Data Science is my second major.

WISCURDS, the Data Science Institute's research program, pairs undergraduates with a mentor on open-ended data problems. My climate project, PhenoSync, tracks whether blueberry bloom and its bumblebee pollinator are drifting apart. It taught me how much of research is cleaning other people's data and admitting where it runs out. I would rather learn the next lesson from a mentor than from a reviewer.

## Purdue University

### Opportunities at Purdue

EPICS (Engineering Projects in Community Service) is the Purdue program I would join first, because it supplies something my projects have always lacked, which is a user who did not build the system. Its teams design for nonprofit partners over several semesters, and a partner who is not a programmer judges software by whether it actually helps. Until now, the only person evaluating my work has been me, which made every flaw easy to excuse.

The same question runs through the research of Professor Ming Yin, who studies how people act on a machine's advice. Her work on second opinions in AI-assisted decisions found that showing one made people follow wrong AI advice less often, but also made them dismiss correct advice more often. That finding applies directly to Glassbox, the tool I built to diagnose why an application fails. Every figure it reports cites its evidence, on the assumption that evidence helps an engineer catch a wrong diagnosis. I have never tested that assumption, and the citations may simply make a wrong answer more persuasive. Her lab is where I would learn to design that experiment properly.

Outside the classroom, I would join Boiler Quant, Purdue's quantitative trading club. Having founded a similar club at school and written its course, I would value arriving as the least experienced member of a team with projects already underway, where people who understand markets better than I do can expose the flaws in my strategies before a real market does.

### Why Computer Science

"Investors herd" (they copy the crowd) is an easy sentence to write. My research paper, on how investor attention affects stock prices, leaned on it to explain the level of trading at which prices start swinging. Statistics could show that the jump was real, but not what behavior produced it.

So I built NEXUS, a simulated market where my guesses had to run as code. In code, "investors herd" needed actual numbers, such as how many investors, whom they copy and for how long. My sentence had skipped all three. My first version let traders copy forever, and within a few simulated days every one of them was buying the same stock. I chose Computer Science because code shows me which parts of an explanation I skipped.

I chose West Lafayette for the Computational Science and Engineering track, which teaches computational methods for modeling complex systems, the work NEXUS already demanded. I adjusted NEXUS until its prices matched real market data, a method I took from papers without knowing what it rested on. CS 31400, Numerical Methods, which the track requires and which covers how errors grow in calculations, would show me. In The Data Mine, I would run projects on Purdue's shared supercomputers with students who read the same data differently. And CS 37300, Data Mining and Machine Learning, would let me open up the machine-learning models I added to NEXUS and see whether they learned that investors herd, or only that prices move together.

### Alternate major and campus

When I tuned NEXUS, my simulated stock exchange, one run matched all nine patterns that real markets show, and I thought the model was finished. Then I changed nothing except the way the program drew its random numbers, and the same run matched only five. I had been treating randomness as background noise when it was the part I most needed to understand, and that is why Mathematics is my alternate major.

My research has run on mathematics I picked up one tool at a time. To trust my finding that price swings jump once trading passes about 1.4 times its usual level, I learned a correction for markets that fall together and another for testing many ideas at once. I can apply both, but I could not tell you when either one breaks.

At Purdue, MA 41600, Probability, would give me the foundation I skipped, and MA 43200, Elementary Stochastic Processes, would teach me how to model orders that arrive at random, which is exactly what my simulated traders do. MA 35301, Linear Algebra II, is built on proofs, and I want that, because the factor models I built for ATLAS rest on matrix results I have used but never proved.

West Lafayette is the right campus because Mathematics and Computer Science both sit in the College of Science there, so I could keep taking computing courses and keep building NEXUS while I finally learn why the methods I depend on actually work.

## University of Massachusetts Amherst

### Why UMass Amherst?

I founded my school's quant finance club and wrote its course, and at UMass I would like to be a student again. David Jensen's Knowledge Discovery Laboratory argues that methods for finding causes should be tested against real experiments rather than synthetic data, and NEXUS, my market simulator, is precisely that kind of synthetic data: it reproduces a market's patterns without proving what causes them. Through the Early Research Scholars Program, I would aim to join his lab as a first-year and offer NEXUS as a test case whose causes are known, because I wrote them.

### Why Computer Science, and why at UMass?

I came to Computer Science through economics, wanting to know why investors copy each other. When my XGBoost model, a prediction tool I trained, ranked trading volume as its most important input, the result looked like insight. Volume, however, rises whenever prices move, so the model may have been tracking the price swing rather than its cause, and I still cannot say which. COMPSCI 240, Reasoning Under Uncertainty, and the AI concentration at UMass would teach me to make that distinction before I trust an answer simply because I like it.

### Community you belong to

Each year since 2025, I join volunteers who spend about four weeks teaching math and English to children in villages near my school. My first explanations were correct and useless. One third-grader answered "yes" to every "understood?" and handed back a blank page. When we turned multiplication into a team race, he shouted an answer first, then corrected his teammate, and asked for the next question. That was the first time I saw him ask for anything.

I stopped asking "understood?" In a UMass study group, I would hand someone the next problem and watch where they get stuck.

## Virginia Tech: Ut Prosim Profile

### Community

I had never cold-called before. In three weeks, I raised INR 22,500 (about $270) through my own campaign in a crowdfunding drive for study kits and footwear for children in nearby villages. One woman asked what would happen if the school did not need the kits. I had no answer, and she said she would give once she saw the school's own list. She gave, and after that I sent the list first.

Since 2025, I have taught them four weeks a year. One third-grader answered "yes" to every "understood?" and handed back blank pages until we made multiplication a team race.

At The Big Event, I would ask residents what they need before we arrive with a plan.

### Inclusion

My worst session in our market club was on the Black-Scholes equation. Because the three or four members who knew some finance kept nodding, I kept going. It took me an hour to notice the other twenty playing games at the back.

I was annoyed with them until I took it to my co-founder, who pointed out that we had built the session for people who already knew the subject. The next week we opened with the Monty Hall problem and worked toward probability and Bayes. A tenth-grader who had barely spoken all term insisted switching doors couldn't matter, and half the room joined the argument.

Now I watch the quiet members rather than the nodding ones.

### Leadership

Our STEM Racing team (miniature race cars) picks designs with Daedalus, the digital wind tunnel I wrote, so the team relies on my numbers. Between two designs, A looked 0.03 s faster, and my output listed every assumption so anyone could challenge it.

Jainam did. He argued that rough air behind A's front wheels made my air-resistance estimate too optimistic. When we angled the airflow 10 degrees, A's lead disappeared, while B's time moved less than 0.01 s, and B also cleared the 48 g minimum mass. We chose B, and it took us to the 2027 Nationals.

I was proudest that Jainam reran it, and I learned that my job is to make my work easy to doubt.

### Goal

My brother got me watching Formula 1 recently, and I ended up more interested in the wind tunnels than the races. I wanted to test those ideas myself, so I built Daedalus for our STEM Racing team. At the 2027 Nationals, we want a top-three finish, the Innovation Award, and a chance to represent India internationally.

Before we race, Daedalus will predict our time and seal the prediction with a digital fingerprint, so the judges can see it pass or fail. First, I have to feed it our own simulation runs. Jainam goes through my numbers looking for what's wrong, and he has already changed one of our design decisions.