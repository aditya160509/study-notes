# 📊 Chapter 2: The Poisson Distribution — 9709 Probability & Statistics 2
> Rule → Method Table → Justification → 4 Examples (all via Question) → Watch Out → Past Paper Ref

## How To Use This Chapter

1.  **Rule:** Start each subsection by boxing the single $$ formula — no prose, just the LaTeX. Copy it to your formula sheet verbatim.
2.  **When / Justification (⭐):** Read the ⭐ box before you calculate. It gives the exact examiner sentence for "justify Poisson" or "justify approximation" — learn it word-for-word for the 1–2 justification marks.
3.  **Method Table:** Follow the numbered `Step | What To Do` in order — every Poisson question in 9709 S2 is one of these 4–6 step routines. Tick off each row as you write.
4.  **4 Examples — All as Questions:** Each method is showcased 4 times via a *question* with a full stepped solution (every algebra step is its own `$$` line). Do Example 1 (coursebook easy), then 2 (past-paper medium), then 3 (hard — combined intervals / sums), then 4 (trap — justification + wording trap). Cover your answer and redo.
5.  **Watch Out! + Past Paper Ref:** Read the `⚠️ Watch Out!` after the 4 examples — it is the trap that loses the last mark. Log the Past Paper Ref (e.g. `9709/62/O/N/23 Q1`) and attempt that paper under timed conditions.

---

# PART 1: Introduction to Poisson — The Basic Poisson Model

*One parameter, mean = variance = $\lambda$, events occur singly, independently, at random, at constant rate. This is the engine for every other section.*

## 1.1 The Poisson PMF, Mean and Variance

**The Rule**

$$P(X=r) = \frac{e^{-\lambda}\lambda^{r}}{r!},\quad r=0,1,2,\dots \quad \text{with } E(X)=\lambda,\; Var(X)=\lambda$$

> ⭐ **Justification Box — When to use $Po(\lambda)$ and what to write for marks**
> *Conditions (need all 4 for "suitable model" marks):* `Events occur singly, independently, at random, at a constant rate in a fixed interval of time/space.`
> *Data check sentence (2 marks):* `Mean $\approx$ variance ($0.70$ and $0.76$ / $1.70$ and $1.61$) so Poisson is suitable; use mean $\lambda$ as parameter because for Poisson $E(X)=Var(X)=\lambda$.`
> *Exact sentence to write:* **"The events occur singly and independently at random at a constant rate. The mean $\approx$ variance, so $Po(\lambda)$ is a suitable model."**
> *If mean $\neq$ variance:* Write **"Mean and variance are not close / not equal, so Poisson is NOT suitable."**

**Method Table — Basic Poisson Probability**

| Step | What To Do |
|------|------------|
| 1 | Identify or calculate $\lambda$ (= mean). State $X\sim Po(\lambda)$. |
| 2 | Write the exact probability statement: $P(X=r)$, $P(X\le r)$, $P(X>r)=1-P(X\le r)$, etc. |
| 3 | Apply PMF: for single $r$ use $\frac{e^{-\lambda}\lambda^{r}}{r!}$; for cumulative sum $r=0$ to $k$. Factor $e^{-\lambda}$ to speed up: $e^{-\lambda}\left(1+\lambda+\frac{\lambda^{2}}{2!}+\dots\right)$. |
| 4 | Evaluate to 3 s.f. (or 4 d.p. if asked). Interpret in context if required. |
| 5 | Justification check: if asked "suitable model?" quote the 4 conditions + mean $\approx$ variance. |

#### Example 1 — Easy — Coursebook Worked Example 2.1(a) — single value

> **Question:** Calls to a hotline follow $Po(6)$ per minute. Find $P(X=9)$.

**Solution — showcasing Method Table:**

$$X\sim Po(6)$$

$$P(X=9)=\frac{e^{-6}6^{9}}{9!}$$

$$e^{-6}=0.00247875\dots$$

$$6^{9}=10\,077\,696$$

$$9! = 362\,880$$

$$P(X=9)=0.00247875\times\frac{10\,077\,696}{362\,880}$$

$$P(X=9)=0.0688\;(3\text{ s.f.})$$

*Past Paper Ref: Coursebook §2.1 Worked Example 2.1 — template for every "exactly $r$" question.*

#### Example 2 — Medium — Past Paper 9709/62/O/N/23 style — cumulative

> **Question:** [9709/62/O/N/23 Q1 adapted] The number of typing errors per page is $Po(1.7)$ (minor injuries clinic model). In a random sample of 1 page, find $P(X\le 3)$ and hence comment on $P(X\ge 4)$.

**Solution:**

$$X\sim Po(1.7)$$

$$P(X\le 3)=P(X=0)+P(X=1)+P(X=2)+P(X=3)$$

$$P(X=0)=\frac{e^{-1.7}1.7^{0}}{0!}=e^{-1.7}=0.18268$$

$$P(X=1)=\frac{e^{-1.7}1.7^{1}}{1!}=0.31056$$

$$P(X=2)=\frac{e^{-1.7}1.7^{2}}{2!}=0.26398$$

$$P(X=3)=\frac{e^{-1.7}1.7^{3}}{3!}=0.14959$$

$$P(X\le 3)=0.18268+0.31056+0.26398+0.14959$$

$$P(X\le 3)=0.9068$$

$$P(X\ge 4)=1-P(X\le 3)$$

$$P(X\ge 4)=1-0.9068=0.0932$$

*Past Paper Ref: 9709/62/O/N/23 Q1; also 9709/72/Q6 June 2016 — cumulative Poisson.*

#### Example 3 — Hard — Sum of Poissons / combined count

> **Question:** A lion rescue centre rescues $L\sim Po(5)$ lions and $T\sim Po(3)$ tigers per week independently. Let $A=L+T$. Find $P(A=2)$ (a) by combining distributions and (b) verify by the long method (enumerate cases).

**Solution:**

$$L\sim Po(5),\; T\sim Po(3),\; L\perp T$$

$$A=L+T\sim Po(5+3)=Po(8)$$

$$P(A=2)=\frac{e^{-8}8^{2}}{2!}$$

$$P(A=2)=e^{-8}\times\frac{64}{2}$$

$$P(A=2)=e^{-8}\times 32$$

$$P(A=2)=0.00033546\times 32$$

$$P(A=2)=0.0107$$

*Verification (long way — enumerate):*

$$P(A=2)=P(L=0)P(T=2)+P(L=1)P(T=1)+P(L=2)P(T=0)$$

$$P(L=0)=e^{-5},\;P(T=2)=\frac{e^{-3}3^{2}}{2!}$$

$$P(L=1)=5e^{-5},\;P(T=1)=3e^{-3}$$

$$P(L=2)=\frac{e^{-5}5^{2}}{2!},\;P(T=0)=e^{-3}$$

$$P(A=2)=e^{-8}\left(\frac{9}{2}+15+\frac{25}{2}\right)$$

$$P(A=2)=e^{-8}\times 32=0.0107\;\checkmark$$

*Past Paper Ref: Coursebook §3.4 illustration + 9709/73 Q6 June 2015 Cross-topic Q4 (Poisson sums).*

#### Example 4 — Trap — Justify the model + "at least" wording

> **Question:** A fire station receives on average 1 call per hour. (a) State assumptions to model calls as $Po(1)$. Are they reasonable at 3 a.m. vs 3 p.m.? (b) Find $P(\text{at least 1 call in an hour})$.

**Solution:**

$$X\sim Po(1)\text{ if calls occur singly, independently, at random, at constant rate}$$

$$\text{(a) Assumptions: singly, independently, at random, constant rate }(\lambda=1\text{/hour})$$

$$\text{Reasonable at 3 a.m.: rate may be lower — constant-rate assumption doubtful}$$

$$\text{At 3 p.m. rate similar to average — more reasonable; but independence may fail if one incident triggers multiple calls}$$

$$P(X\ge 1)=1-P(X=0)$$

$$P(X=0)=\frac{e^{-1}1^{0}}{0!}=e^{-1}$$

$$P(X=0)=0.3679$$

$$P(X\ge 1)=1-0.3679$$

$$P(X\ge 1)=0.632$$

*Trap: $P(\text{at least 1}) = 1-P(0)$, NOT $P(1)$. Examiners dock for $P(X>1)=1-P(X\le1)$ confusion. Also must quote all 4 conditions for the justification mark — "at random" alone scores 0.*

> ⚠️ **Watch Out! — Part 1**
> $P(X> r)$ vs $P(X\ge r)$ vs $P(X\le r)$: `more than 1` $=1-P(X\le1)$; `at least 1` $=1-P(X=0)$; `fewer than 3` $=P(X\le2)$. Always translate English to $\le$/$\ge$/$=$ first. And mean = variance is a *necessary* check — if data give $\bar{x}=3.4$, $s^{2}=6.1$, Poisson is unsuitable however "rare" the events feel.

---

# PART 2: Adapting Poisson for Different Intervals — Scaling $\lambda$

*Rate language: "mean $\lambda$ per interval". Change interval → scale $\lambda$ proportionally. This is where 70% of Poisson marks lie.*

## 2.1 Scaling $\lambda$ with Interval Length / Time / Area

**The Rule**

$$\lambda_{\text{new}} = \lambda_{\text{old}}\times\frac{\text{new interval}}{\text{old interval}} = (\text{rate per unit})\times(\text{new length})$$

> ⭐ **Justification Box — Scaling**
> *Write:* **"Events occur at a constant (uniform) rate, so mean is proportional to interval length. $\lambda_{\text{new}}=\lambda_{\text{old}}\times(\text{new}/\text{old})$."**
> *Example sentence:* "Average $2$ per $5$ min $\Rightarrow$ average $12$ per $30$ min, so $X\sim Po(12)$ for 30 min."
> *Non-integer $\lambda$ is allowed:* $\lambda=1.6$, $0.4$, $2.4$ etc. — do not round.
> *If rate not constant (rush hour, seasonality):* state Poisson unsuitable after scaling.

**Method Table — Interval Scaling**

| Step | What To Do |
|------|------------|
| 1 | Extract given rate: $\lambda_{\text{given}}$ per $t_{\text{given}}$ (minutes, metres, pages, weeks). |
| 2 | Scale to question interval: $\lambda_{\text{new}}=\lambda_{\text{given}}\times t_{\text{new}}/t_{\text{given}}$. State new $X\sim Po(\lambda_{\text{new}})$. |
| 3 | Translate English to inequality ($P(X= r)$, $P(X\le r)$, $P(X>r)$ etc.). |
| 4 | Compute via PMF / cumulative (factor $e^{-\lambda_{\text{new}}}$). |
| 5 | For "no events in $n$ intervals" either do $X\sim Po(n\lambda)$ with $P(X=0)$ OR $[P(X=0\text{ in 1 interval})]^{n}$ — both give $e^{-n\lambda}$. Show one method clearly. |

#### Example 1 — Easy — Coursebook Worked Example 2.3(a)

> **Question:** People arrive at a post office at average $2$ per $5$ min. Find $P(3\text{ arrivals in }10\text{ min})$.

**Solution:**

$$\lambda_{5}=2$$

$$\lambda_{10}=2\times\frac{10}{5}=4$$

$$X\sim Po(4)\text{ for 10 min}$$

$$P(X=3)=\frac{e^{-4}4^{3}}{3!}$$

$$P(X=3)=e^{-4}\times\frac{64}{6}$$

$$P(X=3)=0.018315\times 10.6667$$

$$P(X=3)=0.195\;(3\text{ s.f.})$$

*Coursebook §2.2 Worked Example 2.3(a).*

#### Example 2 — Medium — Past Paper 9709/73/Q7 June 2014 — Lost Property

> **Question:** [9709/73/Q7 June 2014] Items handed in to Lost Property follow $Po(4.0)$ per week (7 days). Find (a) $P(\text{exactly }2\text{ in 1 day})$, (b) $P(\text{at least }4\text{ in 10 days})$.

**Solution:**

$$\lambda_{7\text{ days}}=4.0$$

$$\lambda_{1\text{ day}}=4.0\times\frac{1}{7}=0.571428\dots$$

$$X_{1}\sim Po(0.5714)$$

$$P(X_{1}=2)=\frac{e^{-0.5714}(0.5714)^{2}}{2!}$$

$$P(X_{1}=2)=e^{-0.5714}\times\frac{0.3265}{2}$$

$$P(X_{1}=2)=0.5647\times0.1633$$

$$P(X_{1}=2)=0.0922$$

$$\lambda_{10\text{ days}}=4.0\times\frac{10}{7}=5.71428$$

$$X_{10}\sim Po(5.7143)$$

$$P(X_{10}\ge 4)=1-P(X_{10}\le 3)$$

$$P(X_{10}\le 3)=e^{-5.7143}\left(1+5.7143+\frac{5.7143^{2}}{2!}+\frac{5.7143^{3}}{3!}\right)$$

$$P(X_{10}\le 3)=e^{-5.7143}\times(1+5.7143+16.326+31.097)$$

$$P(X_{10}\le 3)=0.00330\times54.137$$

$$P(X_{10}\le 3)=0.1787$$

$$P(X_{10}\ge4)=1-0.1787$$

$$P(X_{10}\ge4)=0.821$$

*Past Paper Ref: 9709/73/Q7 June 2014 — classic 7-day → 1-day → 10-day scaling.*

#### Example 3 — Hard — Two intervals + reverse-find

> **Question:** Faults in cloth occur at $1.6$ per metre. Find (a) $P(\text{no flaws in }5\text{ m})$, (b) $P(\text{≥2 flaws in }2.5\text{ m})$. (c) If $P(\text{no flaws in }L\text{ m})=0.20$, find $L$.

**Solution:**

$$\lambda_{1}=1.6$$

$$\lambda_{5}=1.6\times5=8.0$$

$$X_{5}\sim Po(8)$$

$$P(X_{5}=0)=\frac{e^{-8}8^{0}}{0!}=e^{-8}$$

$$P(X_{5}=0)=0.000335$$

$$\lambda_{2.5}=1.6\times2.5=4.0$$

$$X_{2.5}\sim Po(4)$$

$$P(X_{2.5}\ge2)=1-P(X_{2.5}\le1)$$

$$P(X_{2.5}\le1)=e^{-4}\left(1+4\right)$$

$$P(X_{2.5}\le1)=e^{-4}\times5$$

$$P(X_{2.5}\le1)=0.018315\times5=0.0916$$

$$P(X_{2.5}\ge2)=1-0.0916$$

$$P(X_{2.5}\ge2)=0.908$$

$$P(\text{no flaw in }L)=e^{-1.6L}=0.20$$

$$-1.6L=\ln 0.20$$

$$L=\frac{\ln 0.20}{-1.6}$$

$$L=\frac{-1.6094}{-1.6}$$

$$L=1.01\text{ m }(3\text{ s.f.})$$

*Past Paper Ref: Coursebook Exercise 2B Q3 + 9709/71/Q4 Nov 2013 style reverse interval.*

#### Example 4 — Trap — Manager bonus: "no breakages in 6 weeks"

> **Question:** Breakages per week $Po(0.8)$. Manager pays bonus if no breakages in 6 consecutive weeks. Find $P(\text{bonus paid})$. Trap: explain why $P(X=0\text{ in 6 weeks})$ via $Po(4.8)$ equals $[P(X=0\text{ in 1 week})]^{6}$.

**Solution:**

$$\lambda_{1}=0.8,\;X_{1}\sim Po(0.8)$$

$$P(X_{1}=0)=e^{-0.8}=0.449329$$

$$\text{Method A: }P(\text{0 in 6 weeks})=[P(X_{1}=0)]^{6}$$

$$P=(e^{-0.8})^{6}=e^{-4.8}$$

$$P=0.00823$$

$$\text{Method B: }X_{6}\sim Po(0.8\times6)=Po(4.8)$$

$$P(X_{6}=0)=\frac{e^{-4.8}4.8^{0}}{0!}=e^{-4.8}$$

$$P(X_{6}=0)=0.00823$$

*Trap: Students do $6\times P(X=0\text{ in 1 week})=6e^{-0.8}$ (linear, wrong) or forget independence. Both methods valid — pick ONE and state it. Non-integer $\lambda$ is fine.*

> ⚠️ **Watch Out! — Part 2**
> Scaling trap: "per 5 minutes → per second" means $\lambda/300$, not $\lambda\times300$. Always write $\lambda_{\text{new}}=\lambda_{\text{old}}\times(\text{new}/\text{old})$ as a fraction first. And "exactly 0 in 6 weeks" via $Po(6\lambda)$ is NOT $6\times P(\text{0 in 1 week})$.

---

# PART 3: Poisson as Approximation to Binomial — $B(n,p)\approx Po(np)$

*When $n$ large, $p$ small, counting successes is Poisson-like: $np$ is the Poisson mean.*

## 3.1 Binomial → Poisson Approximation

**The Rule**

$$X\sim B(n,p),\; n>50,\; p<0.1,\; np\le 5\ (\text{or }np<10\text{ with }n\text{ large})\;\Rightarrow\; X\approx Po(\lambda=np),\; P(X=r)\approx\frac{e^{-\lambda}\lambda^{r}}{r!}$$

> ⭐ **Justification Box — Binomial → Poisson (exact sentences for 2 marks)**
> *For approximation:* **"$n$ is large ($>50$) and $p$ is small ($<0.1$) and $np$ is small / $<5$, so $B(n,p)\approx Po(np)$ with $\lambda=np$."**
> *Variant examiners accept:* "$n$ large, $p$ small, mean $np$ moderate / small."
> *For Poisson → Binomial derivation context:* "Poisson is limiting case of binomial as $n\to\infty$, $p\to0$, $np=\lambda$ constant."
> *If conditions fail:* "Poisson approximation NOT suitable because $p$ not small / $np$ too large / $n$ not large enough."

**Method Table — $B\to Po$**

| Step | What To Do |
|------|------------|
| 1 | Check conditions: state $n$, $p$, compute $\lambda=np$. Verify $n$ large, $p$ small, $\lambda\le5$ (or $<10$). Quote the justification sentence. |
| 2 | Set approximating distribution: $X\approx Po(\lambda)$ with $\lambda=np$. |
| 3 | Translate question probability to Poisson: $P(X\le k)$, $P(X>k)$ etc. using approximating $\lambda$. |
| 4 | Compute via $e^{-\lambda}\lambda^{r}/r!$ cumulative. |
| 5 | If asked "exact vs approximate" compare: comment that Poisson approximation improves as $n$ increases and $p$ decreases. |

#### Example 1 — Easy — Coursebook Worked Example 2.5

> **Question:** A company produces components with $0.4\%$ faulty. Hari buys 1000 components. Using a suitable approximation find $P(\text{more than 5 faulty})$.

**Solution:**

$$X\sim B(1000,0.004)$$

$$n=1000>50,\;p=0.004<0.1,\;np=4<5$$

$$\text{So }X\approx Po(4)$$

$$P(X>5)=1-P(X\le5)$$

$$P(X\le5)=e^{-4}\left(1+4+\frac{4^{2}}{2!}+\frac{4^{3}}{3!}+\frac{4^{4}}{4!}+\frac{4^{5}}{5!}\right)$$

$$P(X\le5)=e^{-4}\left(1+4+8+10.6667+10.6667+8.5333\right)$$

$$P(X\le5)=e^{-4}\times42.8667$$

$$P(X\le5)=0.018315\times42.8667$$

$$P(X\le5)=0.7851$$

$$P(X>5)=1-0.7851$$

$$P(X>5)=0.215$$

*Coursebook §2.3 Worked Example 2.5.*

#### Example 2 — Medium — Past Paper 9709/62/M/J/2020 style — rare gene

> **Question:** [9709/62/M/J/2020 adapted — 9709/52 basis; also 9709/62/O/N/24 Q1 style] In a population 1 in $50\,000$ has a certain gene. In a random sample of $150\,000$ people, using a suitable approximation find $P(\text{more than 2 have the gene})$.

**Solution:**

$$X\sim B(150000,0.00002)$$

$$p=\frac{1}{50000}=0.00002$$

$$n=150000,\;p=0.00002<0.1,\;np=3<5$$

$$X\approx Po(3)$$

$$P(X>2)=1-P(X\le2)$$

$$P(X\le2)=e^{-3}\left(1+3+\frac{3^{2}}{2!}\right)$$

$$P(X\le2)=e^{-3}\left(1+3+4.5\right)$$

$$P(X\le2)=e^{-3}\times8.5$$

$$P(X\le2)=0.049787\times8.5$$

$$P(X\le2)=0.4232$$

$$P(X>2)=1-0.4232$$

$$P(X>2)=0.577$$

*Past Paper Ref: CIE Oct 2020 9709/62 Q1 (1 in 50 000 gene); also 9709/62/O/N/24 Q1 ($B(n,p)\to Po$).*

#### Example 3 — Hard — Seed mutation + conditional probability

> **Question:** A seed mutation occurs with $p=0.0004$. $12\,000$ seeds germinate. Let $X$ = number of mutated seeds. (a) Justify Poisson approximation and find $P(X\le3)$. (b) Find $P(X\le3\mid X>1)$.

**Solution:**

$$X\sim B(12000,0.0004)$$

$$n=12000>50,\;p=0.0004<0.1,\;np=4.8<5$$

$$X\approx Po(4.8)$$

$$P(X\le3)=e^{-4.8}\left(1+4.8+\frac{4.8^{2}}{2!}+\frac{4.8^{3}}{3!}\right)$$

$$P(X\le3)=e^{-4.8}\left(1+4.8+11.52+18.432\right)$$

$$P(X\le3)=e^{-4.8}\times35.752$$

$$P(X\le3)=0.0082297\times35.752$$

$$P(X\le3)=0.294$$

$$P(X\le3\mid X>1)=\frac{P(1<X\le3)}{P(X>1)}$$

$$P(1<X\le3)=P(X=2)+P(X=3)=e^{-4.8}\left(\frac{4.8^{2}}{2!}+\frac{4.8^{3}}{3!}\right)$$

$$P(1<X\le3)=e^{-4.8}\times29.952$$

$$P(1<X\le3)=0.0082297\times29.952=0.2465$$

$$P(X>1)=1-P(X\le1)=1-e^{-4.8}(1+4.8)$$

$$P(X>1)=1-0.0082297\times5.8$$

$$P(X>1)=1-0.04773=0.95227$$

$$P(X\le3\mid X>1)=\frac{0.2465}{0.95227}$$

$$P(X\le3\mid X>1)=0.259$$

*Past Paper Ref: Coursebook Exercise 2C Q7 (seed mutation 0.0004, 12 000 seeds — exact question).*

#### Example 4 — Trap — When approximation is NOT valid

> **Question:** A biased coin $p=0.4$ is tossed $n=20$ times. A student approximates $X\sim B(20,0.4)$ by $Po(8)$ to find $P(X\le2)$. Explain why this is unsuitable and find the correct $P(X\le2)$ via binomial (or explain what the Poisson gives and why it is wrong).

**Solution:**

$$X\sim B(20,0.4),\;np=8$$

$$p=0.4\not<0.1,\;np=8\not<5,\;n=20\not>50$$

$$\text{Poisson approximation NOT suitable: }p\text{ not small, }np\text{ not small, }n\text{ not large}$$

$$\text{Poisson (wrong) would give: }P(X\le2)\approx e^{-8}\left(1+8+\frac{64}{2}\right)$$

$$P_{\text{Po}}\approx e^{-8}\times41$$

$$P_{\text{Po}}\approx0.0138$$

$$\text{Correct binomial: }P(X\le2)=\sum_{r=0}^{2}\binom{20}{r}0.4^{r}0.6^{20-r}$$

$$P(X=0)=0.6^{20}=0.0000366$$

$$P(X=1)=20\times0.4\times0.6^{19}=0.000487$$

$$P(X=2)=\binom{20}{2}0.4^{2}0.6^{18}=190\times0.16\times0.0001016$$

$$P(X=2)=0.00309$$

$$P(X\le2)=0.0000366+0.000487+0.00309$$

$$P(X\le2)=0.00361$$

*Trap: Poisson approx underestimates by factor ~4 because conditions fail. Examiners award justification marks only if you cite $n$ large, $p$ small, $np$ small — vague "rare events" scores 0.*

> ⚠️ **Watch Out! — Part 3**
> Approximation direction: $B\to Po$ uses $\lambda=np$ (NOT $npq$). And the $np<5$ guideline is stricter than the textbook's $np<10$ — in exams state `$n$ large ($>50$), $p$ small ($<0.1$), $np$ small ($<5$)' to guarantee marks. Also don't forget to write `$\approx$' not `$=$' when approximating.

---

# PART 4: Normal Approximation to Poisson — $Po(\lambda)\approx N(\lambda,\lambda)$

*For large $\lambda$ the Poisson histogram looks normal — use $N(\lambda,\lambda)$ with continuity correction $\pm0.5$.*

## 4.1 Normal Approximation with Continuity Correction

**The Rule**

$$X\sim Po(\lambda),\ \lambda>15\ (\text{or }>10\text{ if question says so})\Rightarrow X\approx Y\sim N(\lambda,\lambda),\; \text{with continuity correction }P(X\le k)\approx P(Y<k+0.5),\; P(X\ge k)\approx P(Y>k-0.5)$$

> ⭐ **Justification Box — Normal → Poisson (exact sentences)**
> *For approximation:* **"$\lambda$ is large ($>15$, equivalently $>10$ with guidance), so $Po(\lambda)\approx N(\lambda,\lambda)$ with continuity correction."**
> *Continuity reminder:* **"Poisson is discrete, normal is continuous, so continuity correction $\pm0.5$ required."**
> *Write the corrected inequality explicitly:* $P(X\ge 40)\approx P(Y>39.5)$, $P(X\le 40)\approx P(Y<40.5)$, $P(a\le X\le b)\approx P(a-0.5<Y<b+0.5)$.
> *If $\lambda\le15$:* "Normal approximation NOT suitable because $\lambda$ not large enough; Poisson skewed."

**Method Table — $Po\to N$**

| Step | What To Do |
|------|------------|
| 1 | Check $\lambda>15$ (or $>10$ if exam says). State $X\sim Po(\lambda)\approx Y\sim N(\lambda,\lambda)$. Note mean = $\lambda$, variance = $\lambda$ (so sd = $\sqrt{\lambda}$). |
| 2 | Apply continuity correction: translate $P(X\le k)\to P(Y<k+0.5)$, $P(X\ge k)\to P(Y>k-0.5)$, $P(X=k)\to P(k-0.5<Y<k+0.5)$, $P(a\le X\le b)\to P(a-0.5<Y<b+0.5)$. |
| 3 | Standardise: $Z=\frac{(Y-\mu)}{\sigma}=\frac{Y-\lambda}{\sqrt{\lambda}}$. |
| 4 | Use normal tables / $\Phi$: $P(Z<z)=\Phi(z)$, $P(Z>z)=1-\Phi(z)$. Combine for interval probabilities. |
| 5 | Interpret: state probability to 3 s.f., comment on approximation quality (larger $\lambda$ → better). |

#### Example 1 — Easy — Coursebook Worked Example 2.6(a) — single value

> **Question:** Turtles lay eggs $X\sim Po(60)$ per nest. Using normal approximation find $P(X=50)$.

**Solution:**

$$X\sim Po(60),\;\lambda=60>15$$

$$X\approx Y\sim N(60,60),\;\sigma=\sqrt{60}=7.74597$$

$$P(X=50)\approx P(49.5<Y<50.5)$$

$$z_{1}=\frac{49.5-60}{\sqrt{60}}=\frac{-10.5}{7.74597}$$

$$z_{1}=-1.356$$

$$z_{2}=\frac{50.5-60}{\sqrt{60}}=\frac{-9.5}{7.74597}$$

$$z_{2}=-1.226$$

$$P(49.5<Y<50.5)=\Phi(-1.226)-\Phi(-1.356)$$

$$\Phi(-1.226)=1-\Phi(1.226)=1-0.8899=0.1101$$

$$\Phi(-1.356)=1-\Phi(1.356)=1-0.9125=0.0875$$

$$P(X=50)\approx0.1101-0.0875$$

$$P(X=50)\approx0.0226$$

*Coursebook §2.4 Worked Example 2.6(a). Exact Poisson $=0.0270$ — normal underestimates slightly at tails.*

#### Example 2 — Medium — Past Paper 9709/62/O/N/23 Q1 + 9709/62/F/M/23

> **Question:** [9709/62/O/N/23 Q1] $X\sim Po(25)$. Use normal approximation to find $P(X>30)$. [9709/62/O/N/24 variant: $X\sim Po(42)$ find $P(X>50)$ etc.]

**Solution:**

$$X\sim Po(25),\;\lambda=25>15$$

$$X\approx Y\sim N(25,25),\;\sigma=5$$

$$P(X>30)=1-P(X\le30)\approx1-P(Y<30.5)$$

$$z=\frac{30.5-25}{5}=\frac{5.5}{5}$$

$$z=1.10$$

$$\Phi(1.10)=0.8643$$

$$P(Y<30.5)=\Phi(1.10)=0.8643$$

$$P(X>30)\approx1-0.8643$$

$$P(X>30)\approx0.136$$

*Past Paper Ref: 9709/62/O/N/23 Q1 (exact: $X\sim Po(25)$, $P(X>30)$ via $N(25,25)$); same technique in 9709/62/N/24 Q1.*

#### Example 3 — Hard — Large interval scaling + normal approx

> **Question:** Microorganisms $117$ per ml. Find $P(\text{>1200 in 10 ml})$. Threats $5$ per day — find $P(140\text{ to }152\text{ inclusive in 30 days})$. (Two hard normal approx in one.)

**Solution — Microorganisms:**

$$\lambda_{1\text{ ml}}=117$$

$$\lambda_{10\text{ ml}}=117\times10=1170$$

$$X\sim Po(1170),\;\lambda=1170\gg15$$

$$X\approx Y\sim N(1170,1170),\;\sigma=\sqrt{1170}=34.205$$

$$P(X>1200)\approx P(Y>1200.5)$$

$$z=\frac{1200.5-1170}{34.205}=\frac{30.5}{34.205}$$

$$z=0.8917$$

$$\Phi(0.8917)=0.8137$$

$$P(Y>1200.5)=1-0.8137$$

$$P(X>1200)\approx0.186$$

**Solution — Threats:**

$$\lambda_{1\text{ day}}=5$$

$$\lambda_{30\text{ days}}=150$$

$$X\sim Po(150)\approx Y\sim N(150,150),\;\sigma=12.247$$

$$P(140\le X\le152)\approx P(139.5<Y<152.5)$$

$$z_{1}=\frac{139.5-150}{12.247}=\frac{-10.5}{12.247}=-0.8574$$

$$z_{2}=\frac{152.5-150}{12.247}=\frac{2.5}{12.247}=0.2041$$

$$\Phi(z_{2})=\Phi(0.2041)=0.5809$$

$$\Phi(z_{1})=\Phi(-0.8574)=1-\Phi(0.8574)=1-0.8044=0.1956$$

$$P(139.5<Y<152.5)=0.5809-0.1956$$

$$P(140\le X\le152)\approx0.385$$

*Past Paper Refs: Coursebook Exercise 2D Q3 (117 per ml → 10 ml); End-of-chapter Review Exercise 2 Q3(c) (threats 30 days); also 9709/71/Q3 June 2009 avalanches.*

#### Example 4 — Trap — Continuity correction direction

> **Question:** $X\sim Po(38)$ models tea lights per day. How many tea lights $k$ must be available so $P(X\le k)\ge0.98$? Use normal approximation. Trap: show the $\pm0.5$ matters.

**Solution:**

$$X\sim Po(38),\;\lambda=38>15$$

$$X\approx Y\sim N(38,38),\;\sigma=\sqrt{38}=6.1644$$

$$P(X\le k)\approx P(Y<k+0.5)\ge0.98$$

$$\Phi\left(\frac{k+0.5-38}{6.1644}\right)\ge0.98$$

$$\Phi^{-1}(0.98)=2.0537$$

$$\frac{k+0.5-38}{6.1644}\ge2.0537$$

$$k+0.5\ge38+2.0537\times6.1644$$

$$k+0.5\ge38+12.66$$

$$k+0.5\ge50.66$$

$$k\ge50.16$$

$$k=51\text{ tea lights (minimum integer)}$$

*Without correction: $(k-38)/6.1644\ge2.0537\Rightarrow k\ge50.66\Rightarrow k=51$ — same here but often off by 1. For inclusive upper tail $P(X\ge k)$ use $k-0.5$.*

> ⚠️ **Watch Out! — Part 4**
> Continuity correction is ALWAYS $\pm0.5$ away from the discrete value TOWARDS the tail you are keeping. $P(X\le k)\to k+0.5$, $P(X\ge k)\to k-0.5$, $P(X=k)\to [k-0.5, k+0.5]$, $P(a\le X\le b)\to [a-0.5, b+0.5]$. Forgetting it loses 1 mark; applying it backwards (e.g. $k-0.5$ for $\le$) loses 2. And $\Phi$ tables give $\Phi(z)$, not $1-\Phi(z)$ — draw the normal curve.

---

# PART 5: Hypothesis Testing with Poisson — Critical Region & $p$-Value

*Single observation from $Po(\lambda)$. Test if rate has changed — exactly like binomial tests in Ch 1 but with Poisson pmf or normal approx for large $\lambda$.*

## 5.1 One- and Two-Tailed Tests, Type I/II Errors

**The Rule**

$$H_{0}:\lambda=\lambda_{0}\quad\text{vs}\quad H_{1}:\lambda>\lambda_{0}\ (\text{or }<,\neq),\quad p\text{-value}=P(X\ge x_{\text{obs}}\mid H_{0})\text{ or }P(X\le x_{\text{obs}}\mid H_{0}),\quad\text{Reject }H_{0}\iff p\le\alpha$$

$$ \text{For }H_{1}:\lambda\neq\lambda_{0}:\ \alpha\text{ split: compare }p/2\text{ or double }p\text{ vs }\alpha,\text{ equivalently compare }P(X\ge x_{\text{obs}}) \text{ with }\alpha/2$$

> ⭐ **Justification Box — Poisson Hypothesis Test (copy-paste sentences)**
> *Null/Alternative:* **"$H_{0}:\lambda=\lambda_{0}$, $H_{1}:\lambda>\lambda_{0}$ (or $<$, $\neq$) where $\lambda$ is the mean rate per [interval]."**
> *Test choice:* **"Single observation from $Po(\lambda)$; test at $\alpha\%$ significance level, one-tailed (or two-tailed if $\neq$)."**
> *Critical region method:* "Critical region is $\{X\ge c: P(X\ge c\mid H_{0})\le\alpha\}$ (or $\le$ for left tail)."
> *$p$-value method (preferred):* **"p-value $=P(X\ge x_{\text{obs}}\mid H_{0})=...$ Compare with $\alpha$: if $p\le\alpha$ reject $H_{0}$, otherwise fail to reject $H_{0}$."**
> *Conclusion sentence (MANDATORY):* **"There is (in)sufficient evidence at the $\alpha\%$ level to support the claim that the mean rate has increased/decreased/changed."** — never "prove $H_{0}$ true/false."
> *Normal approx for large $\lambda_{0}n$:* "Mean $>15$ so $Po(\lambda_{0}n)\approx N(\lambda_{0}n,\lambda_{0}n)$ with continuity correction."

**Method Table — Poisson Hypothesis Test**

| Step | What To Do |
|------|------------|
| 1 | State $H_{0}:\lambda=\lambda_{0}$ and $H_{1}$ with direction ($>$, $<$, $\neq$). State $X\sim Po(\lambda_{0})$ under $H_{0}$ (scale $\lambda_{0}$ to observed interval if needed). |
| 2 | Choose significance level $\alpha$ and tail: one-tailed if question says "increase/decrease/more/fewer", two-tailed if "change/different/not equal" (split $\alpha/2$). |
| 3 | Compute $p$-value: if $H_{1}:>$ then $p=P(X\ge x_{\text{obs}}\mid H_{0})=1-P(X\le x_{\text{obs}}-1)$; if $<$ then $p=P(X\le x_{\text{obs}})$; if $\neq$ then $p=2\times\min(P(X\ge x_{\text{obs}}),P(X\le x_{\text{obs}}))$ or compare one tail to $\alpha/2$. For large $\lambda_{0}n$ use normal approx with $\pm0.5$. |
| 4 | Decision rule: Reject $H_{0}$ iff $p\le\alpha$ (or $p\le\alpha/2$ per tail for two-tailed). |
| 5 | Conclusion in context: "Reject / Fail to reject $H_{0}$ at $\alpha\%$ level. There is (in)sufficient evidence that the mean [rate] has [increased/decreased/changed]." Comment on Type I/II if asked. |

#### Example 1 — Easy — Coursebook Worked Example 2.8(a) — one-tailed

> **Question:** Accidents occur at $7$ per month. After traffic measures, $2$ accidents in the next month. Test at $5\%$ if measures reduced accidents.

**Solution:**

$$H_{0}:\lambda=7,\;H_{1}:\lambda<7,\;X\sim Po(7)\text{ under }H_{0},\;\alpha=0.05\text{ one-tailed}$$

$$x_{\text{obs}}=2,\;p\text{-value}=P(X\le2\mid\lambda=7)$$

$$P(X\le2)=e^{-7}\left(1+7+\frac{7^{2}}{2!}\right)$$

$$P(X\le2)=e^{-7}\left(1+7+24.5\right)$$

$$P(X\le2)=e^{-7}\times32.5$$

$$P(X\le2)=0.00091188\times32.5$$

$$p=0.0296$$

$$p=0.0296<0.05=\alpha$$

$$\text{Reject }H_{0}\text{ at }5\%\text{ level}$$

$$\text{There is sufficient evidence that the mean number of accidents has decreased / measures are effective}$$

*Coursebook §2.5 Worked Example 2.8(a).*

#### Example 2 — Medium — Past Paper 9709/72/Q7 Nov 2010 + 9709/71/Q7 June 2010 — scaled interval + large $\lambda$ normal approx

> **Question:** [9709/73/Q7 Nov 2010] House sales $Po(0.8)$ per week. After publicity, total sales in 3 weeks = $5$. Test at $5\%$ if mean increased. [Also white blood cells $Po(5.2)$ → count $2$ — test if decreased, and Type I/II.]

**Solution — House sales:**

$$H_{0}:\lambda=0.8\text{/week},\;H_{1}:\lambda>0.8,\;\alpha=0.05\text{ one-tailed}$$

$$\lambda_{3\text{ weeks}}=0.8\times3=2.4$$

$$X_{3}\sim Po(2.4)\text{ under }H_{0}$$

$$x_{\text{obs}}=5,\;p=P(X\ge5)=1-P(X\le4)$$

$$P(X\le4)=e^{-2.4}\left(1+2.4+\frac{2.4^{2}}{2!}+\frac{2.4^{3}}{3!}+\frac{2.4^{4}}{4!}\right)$$

$$P(X\le4)=e^{-2.4}\left(1+2.4+2.88+2.304+1.3824\right)$$

$$P(X\le4)=e^{-2.4}\times9.9664$$

$$P(X\le4)=0.090718\times9.9664=0.9041$$

$$p=1-0.9041$$

$$p=0.0959$$

$$p=0.0959>0.05$$

$$\text{Fail to reject }H_{0}\text{ at }5\%\text{ level}$$

$$\text{Insufficient evidence that mean weekly sales have increased}$$

*Critical region check: $P(X\ge6)=0.0357\le0.05$ so critical region $X\ge6$; observed $5$ not in it — consistent.*

**Solution — White blood cells (Type I/II):**

$$H_{0}:\lambda=5.2,\;H_{1}:\lambda<5.2,\;\alpha=0.10$$

$$P(X\le2\mid\lambda=5.2)=e^{-5.2}\left(1+5.2+\frac{5.2^{2}}{2}\right)$$

$$P(X\le2)=e^{-5.2}\times19.72$$

$$P(X\le2)=0.005516\times19.72=0.1088$$

$$p=0.1088>0.10\Rightarrow\text{Fail to reject at }10\%$$

$$\text{Type I error (here) = reject }H_{0}\text{ when true mean still }5.2;\;P(\text{Type I})=P(X\le1\mid\lambda=5.2)=0.0342\text{ (critical region }X\le1)$$

*Past Paper Refs: 9709/73/Q7 Nov 2010 (house sales $Po(0.8)$); 9709/71/Q7 June 2010 (white blood cell $Po(5.2)$).*

#### Example 3 — Hard — 6-month follow-up with normal approx + changing significance

> **Question:** Same road accidents $7$ per month. Over 6 months, $32$ accidents observed. (a) Test at $5\%$ if measures still effective ($H_{1}:\lambda<7$/month). (b) What if $\alpha=10\%$?

**Solution:**

$$H_{0}:\lambda=7\text{/month},\;H_{1}:\lambda<7,\;\alpha=0.05$$

$$\lambda_{6}=7\times6=42$$

$$X_{6}\sim Po(42),\;\lambda=42>15\Rightarrow X_{6}\approx Y\sim N(42,42)$$

$$x_{\text{obs}}=32,\;p\approx P(Y<32.5)\text{ (continuity)}$$

$$z=\frac{32.5-42}{\sqrt{42}}=\frac{-9.5}{6.4807}$$

$$z=-1.466$$

$$\Phi(-1.466)=1-\Phi(1.466)$$

$$\Phi(1.466)=0.9287$$

$$p\approx1-0.9287$$

$$p\approx0.0713$$

$$p=0.0713>0.05$$

$$\text{Fail to reject }H_{0}\text{ at }5\%:\text{ insufficient evidence measures reduce accidents}$$

$$p=0.0713<0.10$$

$$\text{Reject }H_{0}\text{ at }10\%:\text{ sufficient evidence at }10\%\text{ level}$$

*Coursebook Worked Example 2.8(b) — shows how conclusion flips with $\alpha$. Also illustrates large $\lambda$ → normal approx mandatory.*

#### Example 4 — Trap — Two-tailed test + Type I/II wording

> **Question:** Machine faults $1.5$ per week. After overhaul, $28$ faults in $26$ weeks. (a) Test at $5\%$ if mean has changed (two-tailed, use normal approx). (b) What is meant by Type I error here? (c) What extra info needed for Type II?

**Solution:**

$$H_{0}:\lambda=1.5\text{/week},\;H_{1}:\lambda\neq1.5,\;\alpha=0.05\text{ two-tailed}$$

$$\lambda_{26}=1.5\times26=39$$

$$X_{26}\sim Po(39)\approx Y\sim N(39,39),\;\sigma=6.245$$

$$x_{\text{obs}}=28$$

$$p_{\text{lower}}\approx P(Y<28.5)$$

$$z=\frac{28.5-39}{6.245}=\frac{-10.5}{6.245}$$

$$z=-1.681$$

$$\Phi(-1.681)=0.0464$$

$$\text{Two-tailed }p\approx2\times0.0464$$

$$p\approx0.0928$$

$$p=0.0928>0.05$$

$$\text{Fail to reject }H_{0}\text{ at }5\%\text{ two-tailed}$$

$$\text{Insufficient evidence that mean rate has changed}$$

$$\text{Type I error: conclude mean has changed when in fact it is still }1.5\text{/week (false positive)}$$

$$\text{For }P(\text{Type II})\text{ need true alternative value of }\lambda\text{ (e.g. }\lambda=1.1\text{/week) to compute }P(\text{accept }H_{0}\mid H_{1}\text{ true})$$

*Past Paper Ref: Coursebook Exercise 2E Q3 (1.5/week, 28 in 26 weeks) + End-of-chapter Review Exercise 2 Q5 (Type I/II: $P(X\ge\dots)$ vs $P(X\le\dots)$). Trap: two-tailed comparison is with $\alpha/2=0.025$ per tail, not $\alpha=0.05$ — halving forgotten = wrong decision.*

> ⚠️ **Watch Out! — Part 5**
> Hypothesis test traps: (1) For $H_{1}:\lambda>\lambda_{0}$ use $P(X\ge x_{\text{obs}})$ (include $x_{\text{obs}}$), for $<$ use $P(X\le x_{\text{obs}})$. Off-by-one loses the mark. (2) Two-tailed: compare $p$-value to $\alpha$, NOT $\alpha/2$ if you already doubled $p$ — pick ONE convention and stick to it. (3) Wording: never "accept $H_{0}$" as proof — write "fail to reject $H_{0}$ / insufficient evidence". Examiners penalise "prove no change".

---

# Formula Sheet

$$\boxed{P(X=r)=\frac{e^{-\lambda}\lambda^{r}}{r!},\quad r=0,1,2,\dots}$$

$$\boxed{E(X)=\lambda,\qquad Var(X)=\lambda,\qquad \sigma=\sqrt{\lambda}}$$

$$\boxed{\lambda_{\text{new}}=\lambda_{\text{old}}\times\frac{t_{\text{new}}}{t_{\text{old}}}}$$

$$\boxed{X\sim B(n,p),\;n\text{ large},\;p\text{ small},\;np<5\Rightarrow X\approx Po(\lambda=np):\;P(X=r)\approx\frac{e^{-np}(np)^{r}}{r!}}$$

$$\boxed{X\sim Po(\lambda),\;\lambda>15\Rightarrow X\approx Y\sim N(\lambda,\lambda):\;Z=\frac{Y-\lambda}{\sqrt{\lambda}},\; \text{continuity }\pm0.5}$$

$$\boxed{\begin{aligned}P(X\le k)&\approx P(Y<k+0.5)\\ P(X\ge k)&\approx P(Y>k-0.5)\\ P(X=k)&\approx P(k-0.5<Y<k+0.5)\\ P(a\le X\le b)&\approx P(a-0.5<Y<b+0.5)\end{aligned}}$$

$$\boxed{H_{0}:\lambda=\lambda_{0},\;p=P(X\ge x_{\text{obs}}\mid H_{0})\text{ or }P(X\le x_{\text{obs}}\mid H_{0}),\;\text{Reject }H_{0}\iff p\le\alpha\;(p\le\alpha/2\text{ per tail if two-tailed})}$$

$$\boxed{X\sim Po(\lambda),\;Y\sim Po(\mu),\;X\perp Y\Rightarrow X+Y\sim Po(\lambda+\mu),\quad E(aX+bY)=a\lambda+b\mu,\;Var(aX+bY)=a^{2}\lambda+b^{2}\mu\;(aX+bY\text{ NOT Poisson unless }a=b=1)}$$

---

# Methods Summary Table

| Formula / Situation | Type 1 — Single value / Direct | Type 2 — Interval / Cumulative / Combined | Type 3 — Reverse / Hypothesis / Approx | Past Paper Ref |
|---|---|---|---|---|
| **$P(X=r)=e^{-\lambda}\lambda^{r}/r!$** $X\sim Po(\lambda)$ | $P(X=3)$ exactly; $P(X=0)$ | $P(X\le k)$, $P(X\ge k)$, $P(a\le X\le b)$ via sum | Find $k$ s.t. $P(X\le k)\ge p$; inventory / tea lights stock | 9709/72 Q6 June 2016 (hair dryers); 9709/73 Q7 June 2014 (Lost Property $Po(4.0)$) |
| **$\lambda_{\text{new}}=\lambda_{\text{old}}\times\text{new}/\text{old}$** (scaling) | 1 km → 2 km (5→10 potholes) | Faults per 5 m, per 2.5 m; calls per 5 min → per 20 min | Reverse: find $L$ s.t. $P(\text{0 in }L)=0.20$; bonus $[P_{0}]^{n}$ vs $Po(n\lambda)$ | 9709/71 Q4 Nov 2013 (radioactive $0.7$ per 150 min); Coursebook 2B Q3 (cloth $1.6$/m) |
| **$X+Y\sim Po(\lambda+\mu)$** (sum of independent Poissons) | $L+T$ per week $Po(8)$ | $P(L+T\le k)$ over $n$ days (standard+off-road safari $0.8$/$2.7$) | $P(X=1\mid X+Y=5)$ conditional; $V=2X+Y$ not Poisson | 9709/73 Q6 June 2015 (checkouts $0.7$/$0.5$ per min); 9709/62/O/N/23 Q5 style |
| **$B(n,p)\approx Po(np)$** ($n>50$, $p<0.1$, $np<5$) | $p=0.004$, $n=1000$ → $Po(4)$ | Rare gene $1/50000$, $n=150k$ → $Po(3)$; seed $0.0004$, $n=12k$ → $Po(4.8)$ | Justify approx / show unsuitable ($p=0.4$); conditional $P(X\le3\mid X>1)$ | 9709/62/O/N/24 Q1; 9709/62/M/J/2020 Q1 (gene); Coursebook 2C Q7 |
| **$Po(\lambda)\approx N(\lambda,\lambda)$** $\lambda>15$, $\pm0.5$ | $P(X=50)$ where $X\sim Po(60)$ via $N(60,60)$ | $P(140\le X\le152)$ over 30 days via $N(150,150)$; $P(X>1200)$ over 10 ml | Find $k$ s.t. $P(X\le k)\ge0.98$; solve for $\lambda$ from $\Phi$ | 9709/62/O/N/23 Q1 ($Po(25)>30$); Coursebook 2D Q3 (117/ml → 1170/10 ml) |
| **Hypothesis test** $H_{0}:\lambda=\lambda_{0}$ | One-tailed $7$/month → $2$ in 1 month | Scaled: $0.8$/week → $5$ in 3 weeks; $42$ in 6 months via $N(42,42)$ | Two-tailed $1.5$/week → $28$ in 26 weeks; Type I/II error probabilities | 9709/73 Q7 Nov 2010 (house sales $Po(0.8)$); 9709/71 Q7 June 2010 (blood $Po(5.2)$); Coursebook 2.5 Ex 2.8 |

---

# Justification Bank — Copy-Paste Sentences (earn the 1–2 justification marks)

**Poisson model suitable (need all 4 + mean≈variance):**
> *"The events occur singly and independently at random at a constant (uniform) average rate in a fixed interval of time/space. The sample mean $\approx$ sample variance ($\bar{x}=...$, $s^{2}=...$), so $Po(\lambda)$ with $\lambda=\bar{x}$ is a suitable model."*

**Poisson NOT suitable:**
> *"The mean and variance are not approximately equal / not equal, so $Po(\lambda)$ is not a suitable model."* OR *"Events do not occur at a constant rate / not independently (e.g. traffic lights cause clustering; one fault makes another more likely), so Poisson unsuitable."*

**Binomial → Poisson approximation:**
> *" $n=...$ is large ($>50$), $p=...$ is small ($<0.1$) and $np=...$ is small ($<5$, moderate), so $B(n,p)\approx Po(np)$ with $\lambda=np=...$."*

**Binomial → Poisson NOT suitable:**
> *"Poisson approximation not suitable because $p$ is not small / $np$ is not small / $n$ is not large enough."*

**Normal → Poisson approximation:**
> *"$ \lambda=...$ is large ($>15$), so $Po(\lambda)\approx N(\lambda,\lambda)$ with $\lambda=...$, $\sigma=\sqrt{\lambda}=...$. As Poisson is discrete and normal is continuous, a continuity correction of $\pm0.5$ is required."*

**Hypothesis test opening:**
> *"Let $X$ be the number of [events] in [interval]. Under $H_{0}$, $X\sim Po(\lambda_{0}[ \times\text{interval}])$. $H_{0}:\lambda=\lambda_{0}$, $H_{1}:\lambda>\lambda_{0}$ (or $<$, $\neq$) at $\alpha\%$ significance level, one-tailed (two-tailed)."*

**Hypothesis test decision (p-value method):**
> *"p-value $=P(X\ge x_{\text{obs}}\mid H_{0})=...$ Since $p=...\le\alpha$ ($\alpha=0.05$), reject $H_{0}$. There is sufficient evidence at the $\alpha\%$ level that the mean rate has increased/decreased."*
> *"Since $p=...>\alpha$, fail to reject $H_{0}$. There is insufficient evidence at the $\alpha\%$ level to support the claim that the mean rate has changed."*

**Type I / Type II in context:**
> *"Type I error: reject $H_{0}$ when $H_{0}$ is true — conclude rate has changed when it has not. $P(\text{Type I})=\alpha$ (or $P(X\in\text{critical region}\mid H_{0})$)."*
> *"Type II error: fail to reject $H_{0}$ when $H_{0}$ is false — conclude no change when the rate has actually changed. $P(\text{Type II})=P(X\notin\text{critical region}\mid\lambda=\lambda_{1})$."*

---

# Practice Questions + Full Solutions

### Q1 — Past-paper style — Poisson basic + scaling [9709/72/Q6 June 2016 hair dryers + 9709/73/Q7 June 2014 Lost Property mix]

> **Question:** Hair dryers demand $X\sim Po(3.4)$ per week. (a) Find $P(\text{exactly }5\text{ in 2 weeks})$. (b) Shop has 4 dryers at start of week. Find $P(\text{enough for week})$. (c) Find smallest $k$ so $P(\text{enough})\ge0.90$.

**Solution:**

$$X_{1}\sim Po(3.4)$$

$$X_{2}\sim Po(3.4\times2)=Po(6.8)$$

$$P(X_{2}=5)=\frac{e^{-6.8}6.8^{5}}{5!}$$

$$P(X_{2}=5)=e^{-6.8}\times\frac{6.8^{5}}{120}$$

$$6.8^{5}=14593.18$$

$$P(X_{2}=5)=0.0011138\times121.61$$

$$P(X_{2}=5)=0.135$$

$$P(\text{enough with 4})=P(X_{1}\le4)=e^{-3.4}\left(1+3.4+\frac{3.4^{2}}{2}+\frac{3.4^{3}}{6}+\frac{3.4^{4}}{24}\right)$$

$$P(X_{1}\le4)=e^{-3.4}\left(1+3.4+5.78+6.5507+5.5681\right)$$

$$P(X_{1}\le4)=e^{-3.4}\times22.2988$$

$$P(X_{1}\le4)=0.033373\times22.2988$$

$$P(X_{1}\le4)=0.744$$

$$P(X_{1}\le5)=P(X_{1}\le4)+\frac{e^{-3.4}3.4^{5}}{5!}$$

$$\frac{e^{-3.4}3.4^{5}}{120}=0.033373\times\frac{454.35}{120}=0.1264$$

$$P(X_{1}\le5)=0.744+0.1264=0.870$$

$$P(X_{1}\le6)=0.870+\frac{e^{-3.4}3.4^{6}}{720}$$

$$\frac{e^{-3.4}3.4^{6}}{720}=0.033373\times\frac{1544.8}{720}=0.0716$$

$$P(X_{1}\le6)=0.870+0.0716=0.9416$$

$$P(X_{1}\le6)=0.9416\ge0.90$$

$$k=6\text{ dryers}$$

---

### Q2 — Interval scaling + sum of Poissons [9709/73/Q6 June 2015 checkouts + 9709/62/O/N/23 style]

> **Question:** Checkout A: customers $0.7$/min, Checkout B: $0.5$/min, independent. Find (a) $P(\text{exactly 3 at A in 5 min})$, (b) $P(\text{>3 total at A+B in 2 min})$.

**Solution:**

$$\lambda_{A,1}=0.7,\;\lambda_{A,5}=0.7\times5=3.5$$

$$X_{A,5}\sim Po(3.5)$$

$$P(X_{A,5}=3)=\frac{e^{-3.5}3.5^{3}}{3!}$$

$$P(X_{A,5}=3)=e^{-3.5}\times\frac{42.875}{6}$$

$$P(X_{A,5}=3)=0.030197\times7.1458$$

$$P(X_{A,5}=3)=0.216$$

$$\lambda_{A+B,1}=0.7+0.5=1.2\text{/min},\;\lambda_{A+B,2}=2.4$$

$$X_{AB}\sim Po(2.4)$$

$$P(X_{AB}>3)=1-P(X_{AB}\le3)$$

$$P(X_{AB}\le3)=e^{-2.4}\left(1+2.4+\frac{2.4^{2}}{2}+\frac{2.4^{3}}{6}\right)$$

$$P(X_{AB}\le3)=e^{-2.4}\left(1+2.4+2.88+2.304\right)$$

$$P(X_{AB}\le3)=e^{-2.4}\times8.584$$

$$P(X_{AB}\le3)=0.090718\times8.584=0.7787$$

$$P(X_{AB}>3)=1-0.7787$$

$$P(X_{AB}>3)=0.221$$

---

### Q3 — Binomial → Poisson [9709/62/O/N/24 Q1 + Coursebook 2C Q7]

> **Question:** A seed mutation $p=0.0004$, $12\,000$ seeds. (a) Justify Poisson approximation and find $P(X\le3)$. (b) A factory has $1\%$ defective buttons, $120$ buttons sampled, $3$ defective found. Test at $2\%$ if defective rate $>1\%$? Use Poisson approximation.

**Solution (a) — same as Part 3 Example 3:**

$$X\sim B(12000,0.0004),\;n=12000>50,\;p=0.0004<0.1,\;np=4.8<5$$

$$X\approx Po(4.8)$$

$$P(X\le3)=e^{-4.8}\left(1+4.8+\frac{4.8^{2}}{2}+\frac{4.8^{3}}{6}\right)=0.294$$

*(Steps as before: $e^{-4.8}=0.0082297$, sum $=35.752$, product $=0.294$.)*

**Solution (b) — Buttons:**

$$X\sim B(120,0.01),\;n=120>50,\;p=0.01<0.1,\;np=1.2<5$$

$$X\approx Po(1.2),\;H_{0}:p=0.01\;(\lambda=1.2),\;H_{1}:p>0.01,\;\alpha=0.02$$

$$p\text{-value}=P(X\ge3\mid\lambda=1.2)=1-P(X\le2)$$

$$P(X\le2)=e^{-1.2}\left(1+1.2+\frac{1.44}{2}\right)$$

$$P(X\le2)=e^{-1.2}\times2.92$$

$$P(X\le2)=0.3010\times2.92=0.8786$$

$$p=1-0.8786$$

$$p=0.1214$$

$$p=0.1214>0.02$$

$$\text{Fail to reject }H_{0}\text{ at }2\%\text{ level}$$

$$\text{Insufficient evidence defective rate }>1\%$$

---

### Q4 — Normal approx to Poisson [9709/62/O/N/23 Q1 ($Po(25)$) + 9709/62/O/N/24 variant]

> **Question:** $X\sim Po(25)$. Use normal approximation to find (a) $P(X>30)$, (b) $P(20\le X\le28)$.

**Solution:**

$$X\sim Po(25)\approx Y\sim N(25,25),\;\sigma=5$$

$$P(X>30)\approx P(Y>30.5)$$

$$z=\frac{30.5-25}{5}=1.10$$

$$\Phi(1.10)=0.8643$$

$$P(Y>30.5)=1-0.8643$$

$$P(X>30)\approx0.136$$

$$P(20\le X\le28)\approx P(19.5<Y<28.5)$$

$$z_{1}=\frac{19.5-25}{5}=-1.10$$

$$z_{2}=\frac{28.5-25}{5}=0.70$$

$$\Phi(z_{2})=\Phi(0.70)=0.7580$$

$$\Phi(z_{1})=\Phi(-1.10)=0.1357$$

$$P(19.5<Y<28.5)=0.7580-0.1357$$

$$P(20\le X\le28)\approx0.622$$

---

### Q5 — Hypothesis test — scaled + normal approx [9709/73/Q7 Nov 2010 + Coursebook 2.8(b)]

> **Question:** Breakdowns $3.1$ per 12-week period. (a) Find $P(\text{exactly 4 in 18 weeks})$. (b) Officer monitors 15 weeks, will conclude rate decreased if $<3$ accidents total. Find $P(\text{Type I error})$. (c) If true rate is now $0.1$/week, find $P(\text{Type II error})$.

**Solution:**

$$\lambda_{12}=3.1,\;\lambda_{18}=3.1\times\frac{18}{12}=4.65$$

$$X_{18}\sim Po(4.65)$$

$$P(X_{18}=4)=\frac{e^{-4.65}4.65^{4}}{4!}$$

$$P(X_{18}=4)=e^{-4.65}\times\frac{467.56}{24}$$

$$P(X_{18}=4)=0.009557\times19.482$$

$$P(X_{18}=4)=0.186$$

$$H_{0}:\lambda=3.1/12\text{ weeks }=0.2583\text{/week},\;H_{1}:\lambda<0.2583,\;\alpha\text{ from critical region }X_{15}<3$$

$$\lambda_{15}=3.1\times\frac{15}{12}=3.875$$

$$X_{15}\sim Po(3.875)\text{ under }H_{0}$$

$$P(\text{Type I})=P(X_{15}\le2\mid\lambda=3.875)=e^{-3.875}\left(1+3.875+\frac{3.875^{2}}{2}\right)$$

$$P(\text{Type I})=e^{-3.875}\times12.3828$$

$$P(\text{Type I})=0.02065\times12.3828$$

$$P(\text{Type I})=0.256$$

*If $\alpha$ is defined by the officer's rule (reject if $<3$), this 0.256 is the actual significance level.*

$$P(\text{Type II})=P(X_{15}\ge3\mid\lambda_{\text{true}}=0.1\times15=1.5)$$

$$P(\text{Type II})=1-P(X_{15}\le2\mid\lambda=1.5)$$

$$P(X_{15}\le2\mid1.5)=e^{-1.5}\left(1+1.5+\frac{2.25}{2}\right)$$

$$P(X_{15}\le2)=e^{-1.5}\times3.625$$

$$P(X_{15}\le2)=0.22313\times3.625=0.8088$$

$$P(\text{Type II})=1-0.8088$$

$$P(\text{Type II})=0.191$$

---

### Q6 — Mixed interval + hypothesis test conclusion wording [9709/71/Q4 Nov 2013 + 9709/71/Q3 June 2009 avalanches]

> **Question:** Radioactive particles $Po(0.7)$ per 150 min. Find (a) $P(\text{≤2 in 10 hours})$, (b) longest $T$ min so $P(\text{0 in }T)\ge0.99$. (c) Avalanches $8$ per year — in 20 years, $P(\text{<137})$ (normal approx).

**Solution:**

$$\lambda_{150}=0.7$$

$$10\text{ hours}=600\text{ min},\;\lambda_{600}=0.7\times\frac{600}{150}=2.8$$

$$X_{600}\sim Po(2.8)$$

$$P(X\le2)=e^{-2.8}\left(1+2.8+\frac{2.8^{2}}{2}\right)$$

$$P(X\le2)=e^{-2.8}\times7.72$$

$$P(X\le2)=0.06081\times7.72$$

$$P(X\le2)=0.469$$

$$P(\text{0 in }T)=e^{-0.7T/150}\ge0.99$$

$$-\frac{0.7T}{150}\ge\ln0.99$$

$$T\le\frac{-150\ln0.99}{0.7}$$

$$T\le\frac{150\times0.01005}{0.7}$$

$$T\le2.15\text{ min}$$

$$\lambda_{1\text{ year}}=8,\;\lambda_{20}=160$$

$$X_{20}\sim Po(160)\approx Y\sim N(160,160),\;\sigma=12.649$$

$$P(X<137)=P(X\le136)\approx P(Y<136.5)$$

$$z=\frac{136.5-160}{12.649}=\frac{-23.5}{12.649}$$

$$z=-1.858$$

$$\Phi(-1.858)=0.0315$$

$$P(X<137)\approx0.0315$$

*Past Paper Ref: 9709/71/Q4 Nov 2013 (radioactive $Po(0.7/150$ min scaling); 9709/71/Q3 June 2009 avalanches $Po(160)$ normal approx). Q6 was truncated in earlier draft — now completed with full avalanche normal-approx steps and proper conclusion.*

---

### Q7 — NEW — Poisson sum conditioned on total — Binomial conditional [9709/62/O/N/19 Q5 + 9709/73/Q6 June 2015 style]

> **Question:** [9709/73/Q6 June 2015 adapted; 9709/62/O/N/19 Q5 style] Emails to inbox A arrive $X\sim Po(3)$ per hour and to inbox B $Y\sim Po(2)$ per hour, independently. Given that $5$ emails arrived in total in one hour ($X+Y=5$), find $P(X=2\mid X+Y=5)$. Also find $P(X\ge 3\mid X+Y=6)$.

**Rule — Conditional Poisson:** If $X\sim Po(\lambda)$, $Y\sim Po(\mu)$, $X\perp Y$, then $S=X+Y\sim Po(\lambda+\mu)$ and

$$X\mid S=n \sim B\left(n,\,p=\frac{\lambda}{\lambda+\mu}\right),\quad P(X=k\mid S=n)=\binom{n}{k}p^{k}(1-p)^{n-k}$$

> ⭐ **Method Table — Poisson conditioned on sum:** 1) Add rates $S\sim Po(\lambda+\mu)$; 2) Identify $p=\lambda/(\lambda+\mu)$; 3) Conditional is binomial $B(n,p)$; 4) Compute binomial probability; 5) No $\perp$ → not binomial.

**Solution (a) — $P(X=2\mid S=5)$:**

$$X\sim Po(3),\;Y\sim Po(2),\;X\perp Y$$

$$S=X+Y\sim Po(5)$$

$$p=\frac{\lambda_{X}}{\lambda_{X}+\lambda_{Y}}=\frac{3}{5}=0.6$$

$$X\mid S=5 \sim B(5,0.6)$$

$$P(X=2\mid S=5)=\binom{5}{2}0.6^{2}0.4^{3}$$

$$\binom{5}{2}=10$$

$$P(X=2\mid S=5)=10\times0.36\times0.064$$

$$P(X=2\mid S=5)=10\times0.02304$$

$$P(X=2\mid S=5)=0.2304$$

*Check via definition (long way):*

$$P(X=2\mid S=5)=\frac{P(X=2)P(Y=3)}{P(S=5)}$$

$$P(X=2)=\frac{e^{-3}3^{2}}{2!},\;P(Y=3)=\frac{e^{-2}2^{3}}{3!},\;P(S=5)=\frac{e^{-5}5^{5}}{5!}$$

$$P(X=2\mid S=5)=\frac{e^{-5}\cdot 9/2\cdot 8/6}{e^{-5}\cdot3125/120}=\frac{12}{52.0833}=0.2304\;\checkmark$$

**Solution (b) — $P(X\ge3\mid S=6)$:**

$$X\mid S=6\sim B(6,0.6)$$

$$P(X\ge3\mid S=6)=1-P(X\le2)$$

$$P(X\le2)=\binom{6}{0}0.4^{6}+\binom{6}{1}0.6\cdot0.4^{5}+\binom{6}{2}0.6^{2}0.4^{4}$$

$$P(X=0)=0.004096$$

$$P(X=1)=6\times0.6\times0.01024=0.036864$$

$$P(X=2)=15\times0.36\times0.0256=0.13824$$

$$P(X\le2)=0.004096+0.036864+0.13824$$

$$P(X\le2)=0.1792$$

$$P(X\ge3\mid S=6)=1-0.1792$$

$$P(X\ge3\mid S=6)=0.8208$$

*Past Paper Ref: 9709/73/Q6 June 2015 (sum of Poissons → conditional binomial); Coursebook §3.4 Review Exercise 2 Q4 ($X\perp Y$ conditional); 9709/62/O/N/19 Q5 variant — examiners hide the binomial inside a Poisson total.*

> ⚠️ **Watch Out! — Conditional:** $P(X=k\mid X+Y=n)\neq P(X=k)$. Always divide by $P(S=n)$. And $p=\lambda/(\lambda+\mu)$, not $\mu/(\lambda+\mu)$ — label which variable is the “success”. If $X$ and $Y$ not independent, result fails.

---

### Q8 — NEW — Two-interval hypothesis test with normal approximation [9709/71/Q3 June 2009 + 9709/73/Q7 Nov 2010 style — scaled $\lambda$ + $Po\to N$]

> **Question:** [9709/71/Q3 June 2009 adapted — avalanches/delivery style; 9709/72/Q7 Nov 2010 scaling] A call centre receives on average $18$ calls per hour ($Po(18)$). Over a $2$-hour peak period, $52$ calls are logged. (a) Test at $5\%$ whether the mean has increased, using a normal approximation with continuity correction. (b) If the observer had monitored $30$ hours and observed $620$ calls, test at $1\%$ (two-tailed) whether the rate has changed.

**Rule — Large-$\lambda$ hypothesis test:** $X\sim Po(\lambda_{0})$, $\lambda_{0}>15 \Rightarrow X\approx Y\sim N(\lambda_{0},\lambda_{0})$, $p\approx P(Y> x_{\text{obs}}-0.5)$ for $H_{1}:\lambda>\lambda_{0}$; reject if $p\le\alpha$.

> ⭐ **Method Table — Two-interval + normal approx test:** 1) Scale $\lambda_{0}$ to observed interval: $\lambda_{\text{test}}=\lambda_{\text{per unit}}\times t$; 2) State $H_{0},H_{1},\alpha$, tail; 3) Justify $Po\to N$ ($\lambda>15$); 4) Continuity correction $x_{\text{obs}}-0.5$ (upper) / $+0.5$ (lower) / $\pm0.5$ (interval); 5) Standardise $z=(y-\lambda)/\sqrt{\lambda}$, $\Phi$, $p$-value, decision sentence.

**Solution (a) — $2$-hour increase test (one-tailed):**

$$H_{0}:\lambda=18\text{/hour},\;H_{1}:\lambda>18,\;\alpha=0.05\text{ one-tailed}$$

$$\lambda_{2}=18\times2=36$$

$$X_{2}\sim Po(36)\text{ under }H_{0},\;\lambda=36>15$$

$$X_{2}\approx Y\sim N(36,36),\;\sigma=\sqrt{36}=6$$

$$x_{\text{obs}}=52,\;p\approx P(Y>51.5)$$

$$z=\frac{51.5-36}{6}=\frac{15.5}{6}$$

$$z=2.583$$

$$\Phi(2.58)=0.9951,\;\Phi(2.583)\approx0.9951$$

$$p\approx1-\Phi(2.583)$$

$$p\approx1-0.9951=0.0049$$

$$p=0.0049<0.05$$

$$\text{Reject }H_{0}\text{ at }5\%$$

$$\text{Sufficient evidence mean calls per hour has increased in peak period}$$

*Exact Poisson check (for reference): $P(X\ge52\mid\lambda=36)=1-P(X\le51)=0.0062$ — normal approx $0.0049$ is close; both reject. Without correction $z=2.667$, $p=0.0038$ — still reject but loses accuracy mark.*

**Solution (b) — $30$-hour two-tailed change test:**

$$H_{0}:\lambda=18\text{/hour},\;H_{1}:\lambda\neq18,\;\alpha=0.01\text{ two-tailed}$$

$$\lambda_{30}=18\times30=540$$

$$X_{30}\sim Po(540)\approx Y\sim N(540,540),\;\sigma=\sqrt{540}=23.2379$$

$$x_{\text{obs}}=620$$

$$z=\frac{619.5-540}{23.2379}=\frac{79.5}{23.2379}$$

$$z=3.421$$

$$\Phi(3.42)=0.99969$$

$$p_{\text{upper}}=1-\Phi(3.421)=0.00031$$

$$\text{Two-tailed }p\approx2\times0.00031$$

$$p\approx0.00062$$

$$p=0.00062<0.01$$

$$\text{Reject }H_{0}\text{ at }1\%\text{ two-tailed}$$

$$\text{Sufficient evidence rate has changed (increased)}$$

*Past Paper Ref: 9709/71/Q3 June 2009 (avalanches $Po(8)$ → $Po(160)$ normal approx); 9709/73/Q7 Nov 2010 (scaled interval test); Coursebook Worked Example 2.8(b) ($Po(42)$ 6-month normal test) — this Q8 merges both ideas: scale $\lambda$ first, then $Po\to N$ for the test.*

> ⚠️ **Watch Out! — Two-interval normal test:** Scale $\lambda$ BEFORE you check $\lambda>15$. $18$/hour is borderline, but $36$/2 h and $540$/30 h are clearly large — cite the scaled $\lambda$, not the hourly one. Continuity is $51.5$ not $52$ for $P(X\ge52)$; forgetting $0.5$ is the common $1$-mark loss on $Po\to N$ hypothesis questions.

---

### Q9 — NEW — Rare-event $B\to Po$ with Type I / Type II error probabilities [9709/62/O/N/24 Q1 + 9709/62/M/J/2020 gene + Coursebook 2C Q7 synthesis]

> **Question:** [9709/62/O/N/24 Q1 style; 9709/62/M/J/2020 rare-gene basis] A vaccine side-effect occurs with probability $p=0.003$. In a trial of $n=800$ patients, let $X$ be the number with side-effects. (a) Justify a Poisson approximation and state its parameter. (b) The trial will flag “elevated risk” if $X\ge6$. Find $P(\text{Type I error})$ under $H_{0}:p=0.003$. (c) If the true $p$ is $0.006$, find $P(\text{Type II error})$ under the same rule, and comment.

**Rule — Rare-event test with $B\to Po$:** $X\sim B(n,p)$, $n$ large, $p$ small $\Rightarrow X\approx Po(np)$; hypothesis $H_{0}:p=p_{0}$ becomes $H_{0}:\lambda=np_{0}$; Type I $=P(X\in\text{critical region}\mid H_{0})$, Type II $=P(X\notin\text{critical region}\mid H_{1}\text{ true})$.

> ⭐ **Method Table — $B\to Po$ Type I/II:** 1) Check $n>50$, $p<0.1$, $np<5$; state $X\approx Po(np)$; 2) Define critical region $C=\{X\ge c\}$ (or $\le c$) and state $\alpha_{\text{actual}}=P(X\in C\mid\lambda_{0})$; 3) Compute Type I via $Po(\lambda_{0})$; 4) For Type II, recompute $\lambda_{1}=np_{1}$ under true $p_{1}$, then $P(\bar{C}\mid\lambda_{1})=P(X<c\mid\lambda_{1})$; 5) Power $=1-$Type II.

**Solution (a) — Justification:**

$$X\sim B(800,0.003)$$

$$n=800>50,\;p=0.003<0.1,\;np=2.4<5$$

$$\text{So }X\approx Po(2.4)$$

$$P(X=r)\approx\frac{e^{-2.4}2.4^{r}}{r!}$$

*Sentence for marks: “$n$ is large ($>50$), $p$ is small ($<0.1$) and $np=2.4$ is small ($<5$), so $B(800,0.003)\approx Po(2.4)$.”*

**Solution (b) — Type I ($H_{0}$ true):**

$$H_{0}:p=0.003\;(\lambda_{0}=2.4),\;C=\{X\ge6\}$$

$$P(\text{Type I})=P(X\ge6\mid\lambda=2.4)=1-P(X\le5)$$

$$P(X\le5)=e^{-2.4}\left(1+2.4+\frac{2.4^{2}}{2!}+\frac{2.4^{3}}{3!}+\frac{2.4^{4}}{4!}+\frac{2.4^{5}}{5!}\right)$$

$$P(X\le5)=e^{-2.4}\left(1+2.4+2.88+2.304+1.3824+0.66355\right)$$

$$P(X\le5)=e^{-2.4}\times10.62995$$

$$P(X\le5)=0.090718\times10.62995$$

$$P(X\le5)=0.9643$$

$$P(\text{Type I})=1-0.9643$$

$$P(\text{Type I})=0.0357$$

*Actual $\alpha=0.0357$ (not $0.05$) — the rule $X\ge6$ achieves $3.6\%$ significance; $X\ge5$ would give $P=0.0959$ which exceeds $5\%$, so $6$ is the correct $5\%$ critical value.*

**Solution (c) — Type II (true $p=0.006$):**

$$\text{True }p_{1}=0.006\Rightarrow\lambda_{1}=800\times0.006=4.8$$

$$X\mid p_{1}\approx Po(4.8)$$

$$P(\text{Type II})=P(X\le5\mid\lambda=4.8)$$

$$P(X\le5)=e^{-4.8}\left(1+4.8+\frac{4.8^{2}}{2}+\frac{4.8^{3}}{6}+\frac{4.8^{4}}{24}+\frac{4.8^{5}}{120}\right)$$

$$P(X\le5)=e^{-4.8}\left(1+4.8+11.52+18.432+22.1184+21.2337\right)$$

$$P(X\le5)=e^{-4.8}\times78.1041$$

$$P(X\le5)=0.0082297\times78.1041$$

$$P(X\le5)=0.6426$$

$$P(\text{Type II})=0.643$$

$$\text{Power}=1-P(\text{Type II})=0.357$$

*Comment: Even though true rate doubled ($2.4\to4.8$), the test has only $36\%$ power at $n=800$ — $64\%$ Type II risk. To reduce Type II, increase $n$, raise $\alpha$, or lower critical value (at cost of higher Type I). This trade-off is the examiner’s favourite “explain Type I vs Type II” follow-up (cf. 9709/71/Q7 June 2010; Coursebook Exercise 2E Q3; Review Exercise 2 Q5).*

*Past Paper Ref: 9709/62/O/N/24 Q1 ($B\to Po$ rare event); 9709/62/M/J/2020 Q1 (1 in $50\,000$ gene, $B\to Po$); Coursebook Exercise 2C Q7 (seed $0.0004$, $n=12\,000$); hypothesis Type I/II: 9709/73/Q7 Nov 2010 house sales + 9709/71/Q7 June 2010 blood cells.*

> ⚠️ **Watch Out! — Rare-event Type I/II:** Do NOT use exact binomial $\binom{800}{r}0.003^{r}0.997^{800-r}$ — write the Poisson approximation explicitly and use $e^{-\lambda}$ sums. Type I is under $H_{0}$ ($\lambda_{0}$), Type II under the stated true $\lambda_{1}$ — swapping them is the classic zero. And $P(\text{Type I})$ is the actual $\alpha$ of the rule, not the nominal $5\%$ you targeted when picking $c$.

---

# Quick Reference Card — Poisson (9709 S2) — 1 Page Cheat Sheet

**1. Poisson PMF & Mean=Variance**

$$P(X=r)=\frac{e^{-\lambda}\lambda^{r}}{r!}\quad E(X)=\lambda\quad Var(X)=\lambda\quad \sigma=\sqrt{\lambda}\quad X\sim Po(\lambda)$$

**2. When is Poisson Suitable? (write this!)**

```
Singly, independently, at random, at constant rate in fixed interval
+ Mean ≈ Variance  → use mean as λ
If not → NOT suitable
```

**3. Interval Scaling (most common!)**

$$\lambda_{\text{new}}=\lambda_{\text{old}}\times\frac{\text{new interval}}{\text{old interval}}$$

Examples: $2/5\text{ min}\to12/30\text{ min}$; $4.0/7\text{ days}\to0.571/1\text{ day}$; $0.7/150\text{ min}\to2.8/600\text{ min}$

**4. Sum of Independent Poissons**

$$X\sim Po(\lambda), Y\sim Po(\mu), X\perp Y \Rightarrow X+Y\sim Po(\lambda+\mu)$$

BUT $2X\sim\text{NOT Poisson}$; $Var(aX+bY)=a^{2}\lambda+b^{2}\mu$

**5. Binomial → Poisson**

$$B(n,p)\approx Po(np)\quad\text{if }n>50,\;p<0.1,\;np<5$$

Sentences: "n large, p small, np small"

**6. Normal → Poisson**

$$Po(\lambda)\approx N(\lambda,\lambda)\quad\text{if }\lambda>15\;(>10\text{ with guidance})$$

Continuity correction — MANDATORY:

```
P(X ≤ k) → P(Y < k+0.5)
P(X ≥ k) → P(Y > k-0.5)
P(X = k) → P(k-0.5 < Y < k+0.5)
P(a ≤ X ≤ b) → P(a-0.5 < Y < b+0.5)
Standardise: Z = (Y - λ)/√λ → Φ
```

**7. Hypothesis Test — Decision in 3 lines**

```
H0: λ = λ0            H1: λ >/< / ≠ λ0
p = P(X ≥ xobs | H0)  (or ≤ for <, double for ≠)
Reject H0 iff p ≤ α  (p ≤ α/2 per tail if two-tailed + doubled)
Conclude: "Sufficient / Insufficient evidence at α% that mean has increased/decreased/changed"
```

**8. p-value vs Critical Region**

```
p-value method: compute P(X ≥ xobs) directly, compare to α
Critical region: find c s.t. P(X ≥ c) ≤ α, reject if xobs ∈ region
For two-tailed: split α → α/2 per tail
```

**9. Wording Traps**

```
"more than k"   = P(X > k)  = 1-P(X ≤ k)
"at least k"    = P(X ≥ k)  = 1-P(X ≤ k-1)
"fewer than k"  = P(X < k)  = P(X ≤ k-1)
"at most k"     = P(X ≤ k)
Include xobs in p-value:  P(X ≥ xobs) not P(X > xobs)
```

**10. Formula You Must Not Forget**

$$\Phi(z)\text{ from tables; }P(Z>z)=1-\Phi(z);\; \Phi(-z)=1-\Phi(z)$$

```
If stuck on scaling: write λ_new = λ_old × (new/old) as fraction FIRST
If stuck on approval: ask "n large? p small? λ large?" — answer gives the method
If stuck on correction: draw normal curve, shade discrete bar at k ±0.5
```

> **Exam mantra:** *Scale λ first, then choose method (Poisson / B→Po / Po→N), then correct (±0.5), then decide (p ≤ α ?).*

---

*Sources: Cambridge International AS & A Level Mathematics 9709 syllabus (2020-2025); Cambridge Probability & Statistics 2 Coursebook Chapter 2 (Worked Examples 2.1–2.8, Exercises 2A–2E, End-of-chapter Review Exercise 2); past papers 9709/62/O/N/23 Q1, 9709/62/O/N/24 Q1, 9709/73/Q7 June 2014, 9709/72/Q6 June 2016, 9709/71/Q4 Nov 2013, 9709/71/Q3 June 2009, 9709/73/Q7 Nov 2010, 9709/71/Q7 June 2010, 9709/62/M/J/2020, 9709/73/Q6 June 2015.*
