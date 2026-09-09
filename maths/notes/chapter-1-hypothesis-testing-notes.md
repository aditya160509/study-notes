# 📘 Chapter 1: Hypothesis Testing - 9709 Probability & Statistics 2 (CAIE A Level Maths)

## Cambridge International AS & A Level Mathematics (9709) - Paper 3 / Paper 6

> **Rule → Method Table → Justification → 4 Examples (all via Question) → Watch Out → Past Paper Ref**

## How To Use This Chapter

1.  **Rule:** Start each subsection by boxing the single $$ formula — no prose, just the LaTeX. Copy it to your formula sheet verbatim.
2.  **When / Justification (⭐):** Read the ⭐ box before you calculate. It gives the exact examiner sentence for "state hypotheses" or "interpret conclusion" — learn it word-for-word for the 1–2 method marks.
3.  **Method Table:** Follow the numbered `Step | What To Do` in order — every hypothesis test in 9709 S2 is one of these 5–6 step routines. Tick off each row as you write.
4.  **4 Examples — All as Questions:** Each method is showcased 4 times via a *question* with a full stepped solution (every probability step is its own `$$` line). Do Example 1 (coursebook easy), then 2 (past-paper medium), then 3 (hard — large $n$ normal approx), then 4 (trap — one/two-tailed or wording trap). Cover your answer and redo.
5.  **Watch Out! + Past Paper Ref:** Read the `⚠️ Watch Out!` after the 4 examples — it is the trap that loses the last mark. Log the Past Paper Ref (e.g. `9709/72/Q4 Nov 2012`) and attempt that paper under timed conditions.

---

## Table of Contents

- [PART 1: Introduction to Hypothesis Testing — H₀, H₁, α, Critical Region](#part-1-introduction-to-hypothesis-testing--h-h--critical-region)
  - [1.1 Null, Alternative, Significance Level, Test Statistic, Critical Region](#11-null-alternative-significance-level-test-statistic-critical-region)
- [PART 2: Direct Binomial Hypothesis Tests — Critical Region Method](#part-2-direct-binomial-hypothesis-tests--critical-region-method)
  - [2.1 One-Tailed Binomial Tests (Exact Probabilities)](#21-one-tailed-binomial-tests-exact-probabilities)
- [PART 3: Normal Approximation with Continuity Correction](#part-3-normal-approximation-with-continuity-correction)
  - [3.1 Binomial → Normal: When, How, and the ±0.5 Correction](#31-binomial--normal-when-how-and-the-05-correction)
- [PART 4: p-Value vs Critical Region & Two-Tailed Tests](#part-4-p-value-vs-critical-region--two-tailed-tests)
  - [4.1 p-Value Method and Splitting α for Two Tails](#41-p-value-method-and-splitting--for-two-tails)
- [PART 5: Type I and Type II Errors](#part-5-type-i-and-type-ii-errors)
  - [5.1 Definitions, Probabilities, and Trade-Offs](#51-definitions-probabilities-and-trade-offs)
- [Formula Sheet](#formula-sheet)
- [Methods Summary Table](#methods-summary-table)
- [Justification Bank — Copy-Paste Sentences](#justification-bank--copy-paste-sentences-earn-the-12-justification-marks)
- [Practice Questions + Full Solutions](#practice-questions--full-solutions)
- [Quick Reference Card — Hypothesis Testing (9709 S2) — 1 Page Cheat Sheet](#quick-reference-card--hypothesis-testing-9709-s2--1-page-cheat-sheet)

---

# PART 1: Introduction to Hypothesis Testing — H₀, H₁, α, Critical Region

*Every hypothesis test asks: "Could this data have happened by chance under the current claim, or is the chance so small that the claim must be doubted?"*

## 1.1 Null, Alternative, Significance Level, Test Statistic, Critical Region

**The Rule**

$$H_{0}: p = p_{0}\quad\text{vs}\quad H_{1}: p < p_{0}\;(p > p_{0}\text{ or }p \neq p_{0}),\qquad \alpha = P(\text{reject }H_{0}\mid H_{0}\text{ true}),\qquad \text{Critical region }C = \{x: P(X\in C\mid H_{0})\le\alpha\}$$

> ⭐ **Justification Box — The Vocabulary (exact sentences for 1–2 marks)**
> *Null hypothesis $H_{0}$:* **"The current / default claim, e.g. $p=p_{0}$, assumed true until evidence suggests otherwise. It is the claim we test."**
> *Alternative hypothesis $H_{1}$:* **"$p < p_{0}$ (or $>$, or $\neq$) — what we will accept if $H_{0}$ is rejected. Direction is set by the wording *before* collecting data."**
> *Significance level $\alpha$:* **"$\alpha\%$ is the probability of rejecting $H_{0}$ when $H_{0}$ is true (the Type I error rate). Smaller $\alpha$ → smaller critical region → more cautious test."** Typical: $5\%$, $2.5\%$, $1\%$, $10\%$.
> *Test statistic:* **"The probability of the observed region under $H_{0}$, e.g. $P(X\le 4)$ or $P(X\ge 5)$, calculated from sample data."**
> *Critical value / region:* **"The boundary value $c$ where $P(X\le c\mid H_{0})\le\alpha$ but $P(X\le c+1)>\alpha$; the critical (rejection) region is all values $\le c$ (or $\ge c$). Acceptance region is the complement."**
> *Conclusion template:* **"Since $p$-value $\le\alpha$ reject $H_{0}$; there is sufficient evidence at the $\alpha\%$ level that [context, e.g. proportion has decreased]. Since $p$-value $>\alpha$ fail to reject $H_{0}$; insufficient evidence at the $\alpha\%$ level."** Never write "prove $H_{0}$ true/false."

**Method Table — Setting Up Any Hypothesis Test**

| Step | What To Do |
|------|------------|
| 1 | Define random variable and its distribution under $H_{0}$: e.g. Let $X$ = "number of successes in $n$ trials". Then $X\sim B(n,p_{0})$ under $H_{0}$. |
| 2 | State $H_{0}$ and $H_{1}$ in terms of the parameter ($p$ or $\mu$). Choose tail from wording: "less than / fewer / reduce / biased towards" → one-tailed ($<$ or $>$); "different / incorrect / changed / not equal" → two-tailed ($\neq$). |
| 3 | State significance level $\alpha$ and whether test is one- or two-tailed (for two-tailed note $\alpha/2$ per tail). |
| 4 | Calculate the test statistic = tail probability under $H_{0}$ that is at least as extreme as observed data: $P(X\le x_{\text{obs}})$ or $P(X\ge x_{\text{obs}})$. |
| 5 | Compare with $\alpha$ (or with critical region): Reject $H_{0}$ iff test statistic $\le\alpha$ (or $x_{\text{obs}}$ lies in critical region). |
| 6 | Write conclusion in context using "sufficient / insufficient evidence at the $\alpha\%$ level" — never "proved" or " $H_{0}$ is true". |

#### Example 1 — Easy — Coursebook §1.1 Dice Intuition (16 rolls)

> **Question:** A fair die has $p=1/6$ of rolling a six. It is rolled $16$ times. Let $X$ = number of sixes. Under $H_{0}: p=1/6$, find $P(X\le4)$, $P(X\le5)$, $P(X\ge5)$, $P(X\ge6)$. At $\alpha=5\%$ one-tailed ($H_{1}:p>1/6$), what is the critical value?

**Solution:**

$$X\sim B\left(16,\tfrac16\right)\text{ under }H_{0}$$

$$P(X=0)=\binom{16}{0}\left(\tfrac16\right)^{0}\left(\tfrac56\right)^{16}=0.0541$$

$$P(X=1)=\binom{16}{1}\left(\tfrac16\right)^{1}\left(\tfrac56\right)^{15}=0.1730$$

$$P(X=2)=\binom{16}{2}\left(\tfrac16\right)^{2}\left(\tfrac56\right)^{14}=0.2596$$

$$P(X=3)=\binom{16}{3}\left(\tfrac16\right)^{3}\left(\tfrac56\right)^{13}=0.2423$$

$$P(X=4)=\binom{16}{4}\left(\tfrac16\right)^{4}\left(\tfrac56\right)^{12}=0.1575$$

$$P(X=5)=\binom{16}{5}\left(\tfrac16\right)^{5}\left(\tfrac56\right)^{11}=0.0756$$

$$P(X\le4)=0.0541+0.1730+0.2596+0.2423+0.1575$$

$$P(X\le4)=0.8866$$

$$P(X\le5)=0.8866+0.0756$$

$$P(X\le5)=0.9622$$

$$P(X\ge5)=1-P(X\le4)$$

$$P(X\ge5)=1-0.8866=0.1134$$

$$P(X\ge6)=1-P(X\le5)$$

$$P(X\ge6)=1-0.9622=0.0378$$

$$P(X\ge6)=0.0378<0.05,\quad P(X\ge5)=0.1134>0.05$$

$$\text{Critical value is }6;\text{ critical region }X\ge6;\; \text{acceptance region }X\le5$$

*Past Paper Ref: Coursebook §1.1 dice discussion — the founding intuition for every binomial test.*

**What the examiner wants:** probabilities to 4 d.p. / %, explicit comparison with $\alpha=0.05$, statement of critical value and both regions.

#### Example 2 — Medium — Wording → Tail Choice

> **Question:** For each wording, state $H_{0}$, $H_{1}$, and whether the test is one- or two-tailed: (a) "Zander's programme reduces crashes", (b) "The spinner is not working correctly", (c) "The proportion of left-handed basketball players is lower than $10\%$", (d) "The coin is biased" (no direction).

**Solution:**

$$(a)\; H_{0}:p=0.40,\; H_{1}:p<0.40,\text{ one-tailed (lower tail — "reduces")}$$

$$(b)\; H_{0}:p=0.20,\; H_{1}:p\neq0.20,\text{ two-tailed ("not working correctly" — either direction)}$$

$$(c)\; H_{0}:p=0.10,\; H_{1}:p<0.10,\text{ one-tailed (lower tail — "lower")}$$

$$(d)\; H_{0}:p=0.50,\; H_{1}:p\neq0.50,\text{ two-tailed ("biased" without direction — either heads or tails)}$$

*Word cues: "more / increase / greater / biased towards $A$" → $>$ ; "less / fewer / lower / decrease / reduce" → $<$; "different / incorrect / changed / not equal / not working" → $\neq$.*

**What the examiner wants:** $H_{0}$ and $H_{1}$ in terms of $p$ (or $\mu$), consistently using the same parameter symbol; explicit "one-tailed" / "two-tailed" label.

#### Example 3 — Hard — Significance Level and Confidence Trade-Off

> **Question:** Explain why choosing $\alpha=1\%$ instead of $10\%$ makes a test more conservative. Use the die example: what happens to the critical region if $\alpha$ is lowered from $10\%$ to $1\%$?

**Solution:**

$$\alpha = P(\text{reject }H_{0}\mid H_{0}\text{ true})$$

$$\text{Lower }\alpha \Rightarrow \text{ smaller critical region }\Rightarrow\text{ harder to reject }H_{0}$$

$$\text{For }X\sim B(16,\tfrac16):\; P(X\ge5)=0.1134>0.10$$

$$P(X\ge6)=0.0378$$

$$P(X\ge7)=P(X\ge6)-P(X=6),\;P(X=6)=\binom{16}{6}(\tfrac16)^{6}(\tfrac56)^{10}=0.0284$$

$$P(X\ge7)=0.0378-0.0284=0.0094$$

$$\text{At }\alpha=10\%:\; X\ge6\text{ is critical }(0.0378<0.10),\text{ also check }X\ge5\text{ not critical}$$

$$\text{At }\alpha=1\%:\; X\ge7\text{ is critical }(0.0094<0.01),\; X\ge6\text{ not critical }(0.0378>0.01)$$

$$\text{Critical value moves from }6\text{ to }7;\; \text{more evidence needed at }1\%$$

*Insight: lowering $\alpha$ reduces Type I errors but increases Type II errors — see Part 5.*

**What the examiner wants:** link between $\alpha$, size of rejection region, and confidence; numerical illustration with $P\ge6$ vs $P\ge7$.

#### Example 4 — Trap — "Test Statistic is a Region, Not a Single Value"

> **Question:** A student writes the test statistic for Zander's simulator test as $P(X=4)$ instead of $P(X\le4)$. Explain the error and why it matters. When $P(X=4)=0.1014$, what wrong conclusion would follow at $5\%$?

**Solution:**

$$\text{Correct test statistic (lower tail): }P(X\le4)=0.05095$$

$$P(X=4)=\binom{20}{4}0.4^{4}0.6^{16}=0.0350\text{ (illustrative; exact }P(X=4)\approx0.035)$$

$$\text{Student uses }P(X=4)\approx0.035\text{ and compares }0.035<0.05\Rightarrow\text{ reject }H_{0}$$

$$\text{Correct: }P(X\le4)=0.05095>0.05\Rightarrow\text{ fail to reject }H_{0}$$

$$\text{The test statistic is a TAIL REGION: }P(X\le x_{\text{obs}})\text{ for }H_{1}:p<p_{0},\;P(X\ge x_{\text{obs}})\text{ for }H_{1}:p>p_{0}$$

$$\text{Using }P(X=x_{\text{obs}})\text{ alone ignores more extreme outcomes and gives a spuriously small probability}$$

*Trap: for two-tailed, the region is $2\times\min(P(X\le x_{\text{obs}}),P(X\ge x_{\text{obs}}))$ or compare one tail to $\alpha/2$ — never just $P(X=x_{\text{obs}})$.*

> ⚠️ **Watch Out! — Part 1**
> (1) $H_{0}$ and $H_{1}$ must use the **same** parameter symbol ($p$ or $\mu$). Writing $H_{0}:\mu=0.4$, $H_{1}:p<0.4$ loses the mark. (2) Set $H_{1}$ **before** seeing data — choosing the tail after seeing $x_{\text{obs}}$ is cheating and examiners penalise it. (3) The test statistic is a **cumulative** tail probability, never $P(X=x_{\text{obs}})$ alone. (4) Conclusion wording: "fail to reject $H_{0}$ / insufficient evidence" — never "accept $H_{0}$ proves no effect" and never "accept $H_{1}$ proves the effect" — hypothesis tests assess evidence, not proof.

---

# PART 2: Direct Binomial Hypothesis Tests — Critical Region Method

*Small to moderate $n$ (typically $n\le30$): calculate exact binomial tail probabilities and compare to $\alpha$.*

## 2.1 One-Tailed Binomial Tests (Exact Probabilities)

**The Rule**

$$X\sim B(n,p_{0})\text{ under }H_{0},\quad p\text{-value}=\begin{cases}P(X\le x_{\text{obs}}\mid H_{0}) & H_{1}:p<p_{0}\\ P(X\ge x_{\text{obs}}\mid H_{0}) & H_{1}:p>p_{0}\end{cases},\quad \text{Reject }H_{0}\iff p\le\alpha$$

$$P(X=r)=\binom{n}{r}p_{0}^{r}(1-p_{0})^{\,n-r},\quad P(X\le k)=\sum_{r=0}^{k}\binom{n}{r}p_{0}^{r}(1-p_{0})^{n-r}$$

> ⭐ **Justification Box — Binomial Test (exact sentence for method marks)**
> *State:* **"Let $X$ be the number of [successes] in $n$ trials. Under $H_{0}$, $X\sim B(n,p_{0})$. $H_{0}:p=p_{0}$, $H_{1}:p<p_{0}$ (or $>$, $\neq$) at $\alpha\%$ significance level, one-tailed (two-tailed)."**
> *Critical region sentence:* **"Critical region is $\{X\le c: P(X\le c\mid H_{0})\le\alpha\}$ (or $\ge c$ for upper tail)."**
> *Decision sentence:* **"$p=... \le\alpha$ (or $>\alpha$) so reject (fail to reject) $H_{0}$ at the $\alpha\%$ level. There is (in)sufficient evidence that $p$ has decreased/increased."**

**Method Table — Exact Binomial Test**

| Step | What To Do |
|------|------------|
| 1 | Define $X$ and $X\sim B(n,p_{0})$ under $H_{0}$. State $H_{0}$, $H_{1}$, $\alpha$, tail. |
| 2 | Compute $p$-value: $H_{1}:p<p_{0}$ → $P(X\le x_{\text{obs}})$; $H_{1}:p>p_{0}$ → $P(X\ge x_{\text{obs}})=1-P(X\le x_{\text{obs}}-1)$. Sum binomial terms $\binom{n}{r}p^{r}q^{n-r}$. |
| 3 | Find critical value(s) if asked: largest $c$ with $P(X\le c)\le\alpha$ (lower tail) or smallest $c$ with $P(X\ge c)\le\alpha$ (upper tail). |
| 4 | Compare $p$-value to $\alpha$ — reject $H_{0}$ iff $p\le\alpha$ (equivalently, $x_{\text{obs}}$ lies in critical region). |
| 5 | Conclusion in context with "at the $\alpha\%$ level" and "sufficient/insufficient evidence that [context]". |

#### Example 1 — Easy — Coursebook Worked Example 1.1 — Zander's Simulator (20 drivers, 4 crashes)

> **Question:** 40% of drivers crash. After training, in $n=20$ drivers, $4$ crash. Test at $5\%$ whether the crash rate has decreased. What if only $3$ crashed? What at $10\%$ with $4$ crashes?

**Solution:**

$$X=\text{number crashing},\; X\sim B(20,0.4)\text{ under }H_{0}$$

$$H_{0}:p=0.4,\; H_{1}:p<0.4,\;\alpha=0.05\text{ one-tailed}$$

$$p\text{-value}=P(X\le4\mid p=0.4)=\sum_{r=0}^{4}\binom{20}{r}0.4^{r}0.6^{20-r}$$

$$P(X=0)=\binom{20}{0}0.4^{0}0.6^{20}=0.00003656$$

$$P(X=1)=\binom{20}{1}0.4^{1}0.6^{19}=20\times0.4\times0.00006092=0.000487$$

$$P(X=2)=\binom{20}{2}0.4^{2}0.6^{18}=190\times0.16\times0.0001015=0.00309$$

$$P(X=3)=\binom{20}{3}0.4^{3}0.6^{17}=1140\times0.064\times0.0001692=0.01235$$

$$P(X=4)=\binom{20}{4}0.4^{4}0.6^{16}=4845\times0.0256\times0.0002820=0.03499$$

$$P(X\le4)=0.0000366+0.000487+0.00309+0.01235+0.03499$$

$$P(X\le4)=0.05095$$

$$P(X\le4)=0.05095>0.05$$

$$\text{Fail to reject }H_{0}\text{ at }5\%$$

$$\text{Insufficient evidence at the }5\%\text{ level that crash rate has decreased}$$

$$P(X\le3)=P(X\le4)-P(X=4)$$

$$P(X\le3)=0.05095-0.03499=0.01596$$

$$P(X\le3)=0.01596<0.05$$

$$\text{If }3\text{ crashed: reject }H_{0};\text{ sufficient evidence at }5\%\text{ that training is effective}$$

$$P(X\le4)=0.05095<0.10$$

$$\text{At }10\%\text{ with }4\text{ crashes: }0.05095<0.10\Rightarrow\text{ reject }H_{0}\text{ at }10\%$$

*Coursebook Worked Example 1.1. Note $0.05095$ is just above $5\%$ — a famous borderline case. Exact $p=5.10\%$ (text rounds to $5.10\%$).*

**What the examiner wants:** all 5 binomial terms shown (or at least the cumulative sum set-up), comparison "0.05095 > 0.05", contextual conclusion mentioning $5\%$ or $10\%$.

#### Example 2 — Medium — Coursebook Worked Example 1.2 — Left-Handed Basketball Players (50 players, 2.5% tail)

> **Question:** $10\%$ of people are left-handed. Bailin suspects left-handedness is less common in basketball. Sample $50$ basketball players. (a) Find rejection region at $5\%$ and critical value. (b) If critical value were $2$, what is the smallest integer $\alpha$ that would make $X=2$ significant?

**Solution:**

$$X=\text{number left-handed in 50},\;X\sim B(50,0.1)\text{ under }H_{0}$$

$$H_{0}:p=0.1,\;H_{1}:p<0.1,\;\alpha=0.05\text{ one-tailed}$$

$$P(X=0)=\binom{50}{0}0.1^{0}0.9^{50}=0.00515$$

$$P(X=1)=\binom{50}{1}0.1^{1}0.9^{49}=50\times0.1\times0.00573=0.02863$$

$$P(X=2)=\binom{50}{2}0.1^{2}0.9^{48}=1225\times0.01\times0.00636=0.07794$$

$$P(X\le0)=0.00515$$

$$P(X\le1)=0.00515+0.02863=0.03378$$

$$P(X\le1)=0.0338<0.05$$

$$P(X\le2)=0.03378+0.07794=0.1117$$

$$P(X\le2)=0.1117>0.05$$

$$\text{Rejection region: }X\le1,\;\text{ critical value }=1$$

$$P(X\le2)=0.1117=11.17\%$$

$$\text{Need }\alpha\ge11.17\%\Rightarrow\text{ smallest integer }\alpha=12\%$$

*Coursebook Worked Example 1.2. Table form often used for $P(X\le x)$.*

**What the examiner wants:** table of $P(X\le0),P(X\le1),P(X\le2)$, identification of $1$ as last value still $<5\%$, answer "$12\%$". Also accept $\alpha>11.17\%$.

#### Example 3 — Medium — Coursebook Worked Example 1.3 — Pentagonal Spinner (10 spins, 5 red)

> **Question:** A fair pentagonal spinner has $p=0.2$ of landing on red. It is spun $10$ times and lands on red $5$ times. Test at $4\%$ whether the spinner is biased towards red. What if it landed on red $4$ times?

**Solution:**

$$X=\text{number of reds in 10 spins},\;X\sim B(10,0.2)\text{ under }H_{0}$$

$$H_{0}:p=0.2,\;H_{1}:p>0.2,\;\alpha=0.04\text{ one-tailed (upper tail)}$$

$$P(X\ge5)=1-P(X\le4)$$

$$P(X=0)=\binom{10}{0}0.2^{0}0.8^{10}=0.107374$$

$$P(X=1)=\binom{10}{1}0.2^{1}0.8^{9}=10\times0.2\times0.134218=0.268435$$

$$P(X=2)=\binom{10}{2}0.2^{2}0.8^{8}=45\times0.04\times0.167772=0.301990$$

$$P(X=3)=\binom{10}{3}0.2^{3}0.8^{7}=120\times0.008\times0.209715=0.201327$$

$$P(X=4)=\binom{10}{4}0.2^{4}0.8^{6}=210\times0.0016\times0.262144=0.088080$$

$$P(X\le4)=0.107374+0.268435+0.301990+0.201327+0.088080$$

$$P(X\le4)=0.967206$$

$$P(X\ge5)=1-0.967206$$

$$P(X\ge5)=0.03279$$

$$P(X\ge5)=0.0328<0.04$$

$$\text{Reject }H_{0}\text{ at }4\%$$

$$\text{Sufficient evidence spinner is biased towards red}$$

$$P(X\ge4)=1-P(X\le3)$$

$$P(X\le3)=0.107374+0.268435+0.301990+0.201327=0.879126$$

$$P(X\ge4)=1-0.879126=0.12087$$

$$P(X\ge4)=0.1209>0.04$$

$$\text{If }4\text{ reds: }0.1209>0.04\Rightarrow\text{ fail to reject }H_{0};\text{ insufficient evidence of bias}$$

*Coursebook Worked Example 1.3. At $\alpha=4\%$ the critical value is $5$.*

**What the examiner wants:** $P(X\ge5)$ computed as $1-P(X\le4)$, explicit $0.0328<0.04$, context "biased towards red".

#### Example 4 — Trap — Direction and Off-By-One (Prerequisite Table)

> **Question:** (a) $X\sim B(8,0.1)$ — find $P(X=2)$, $P(X\le1)$, $P(X>3)$. (b) $X\sim B(15,0.25)$ — find $P(X=2)$, $P(X\le1)$, $P(X\le3)$, $P(X\ge7)$. (c) In a test $H_{1}:p>0.25$ with $n=15$, observed $X=7$. Student writes $P(X>7)$ instead of $P(X\ge7)$ — what is the error magnitude?

**Solution:**

$$X\sim B(8,0.1):\;P(X=2)=\binom{8}{2}0.1^{2}0.9^{6}=28\times0.01\times0.531441$$

$$P(X=2)=0.1488$$

$$P(X\le1)=P(X=0)+P(X=1)=0.9^{8}+8\times0.1\times0.9^{7}$$

$$P(X\le1)=0.430467+0.382638=0.8131$$

$$P(X>3)=1-P(X\le3)$$

$$P(X=3)=\binom{8}{3}0.1^{3}0.9^{5}=56\times0.001\times0.59049=0.03307$$

$$P(X\le3)=0.8131+0.1488+0.03307=0.99498$$

$$P(X>3)=1-0.99498=0.00502$$

$$X\sim B(15,0.25):\;P(X=2)=\binom{15}{2}0.25^{2}0.75^{13}=105\times0.0625\times0.02376$$

$$P(X=2)=0.1559$$

$$P(X\le1)=\binom{15}{0}0.75^{15}+\binom{15}{1}0.25\times0.75^{14}$$

$$P(X\le1)=0.013363+0.066836=0.0802$$

$$P(X=3)=\binom{15}{3}0.25^{3}0.75^{12}=455\times0.015625\times0.03168=0.2252$$

$$P(X\le3)=0.0802+0.1559+0.2252=0.4613$$

$$P(X\ge7)=1-P(X\le6)$$

$$P(X=4)=0.2252,\;P(X=5)=0.1651,\;P(X=6)=0.09175$$

$$P(X\le6)=0.4613+0.2252+0.1651+0.09175=0.9433$$

$$P(X\ge7)=1-0.9433=0.0567$$

$$P(X>7)=P(X\ge8)=P(X\ge7)-P(X=7)$$

$$P(X=7)=\binom{15}{7}0.25^{7}0.75^{8}=6435\times0.0000610\times0.10011=0.03931$$

$$P(X>7)=0.0567-0.03931=0.01739$$

$$\text{Error: }P(X>7)=0.0174\text{ vs correct }P(X\ge7)=0.0567\text{ — off by factor }3.3$$

$$\text{Including }x_{\text{obs}}\text{ matters: at }\alpha=5\%,\;P(X\ge7)=5.67\%>5\%\text{ (fail to reject) but }P(X>7)=1.74\%<5\%\text{ (wrongly reject)}$$

*Trap: $P(X\ge x_{\text{obs}})$ includes $x_{\text{obs}}$; $P(X>x_{\text{obs}})$ excludes it. At significance boundaries this flips the decision.*

> ⚠️ **Watch Out! — Part 2**
> (1) **Tail direction:** $H_{1}:p<p_{0}$ → lower tail $P(X\le x_{\text{obs}})$; $H_{1}:p>p_{0}$ → upper tail $P(X\ge x_{\text{obs}})$. Reversing gives $1-p$ and the wrong decision. (2) **Inclusive inequality:** $P(X\ge x_{\text{obs}})$ includes $x_{\text{obs}}$; $P(X> x_{\text{obs}})$ excludes it — one binomial term difference that flips borderline tests. (3) **Critical value wording:** "critical value" = the boundary value; "critical region" = all values at least as extreme. Writing "$X=1$" instead of "$X\le1$" loses the mark.

---

# PART 3: Normal Approximation with Continuity Correction

*When $n$ is large ($n\ge30$ or $np>5$ and $nq>5$), binomial sums become tedious — approximate by $N(np,npq)$ with $\pm0.5$.*

## 3.1 Binomial → Normal: When, How, and the ±0.5 Correction

**The Rule**

$$X\sim B(n,p),\;np>5,\;nq>5\;(n\text{ large})\Rightarrow X\approx Y\sim N(\mu=np,\;\sigma^{2}=npq),\quad\text{continuity correction }\pm0.5$$

$$P(X\le k)\approx P(Y<k+0.5),\quad P(X\ge k)\approx P(Y>k-0.5),\quad P(X=k)\approx P(k-0.5<Y<k+0.5)$$

$$Z=\frac{Y-\mu}{\sigma}=\frac{Y-np}{\sqrt{npq}},\quad \Phi(z)=P(Z\le z)\text{ from tables},\quad P(Z>z)=1-\Phi(z)$$

> ⭐ **Justification Box — Binomial → Normal (exact sentences for 2 marks)**
> *For approximation:* **"$n$ is large ($>30$) and $np=... >5$ and $nq=... >5$, so $B(n,p)\approx N(np,npq)$ with $\mu=np=...$, $\sigma^{2}=npq=...$, $\sigma=\sqrt{npq}=...$. As binomial is discrete and normal is continuous, a continuity correction of $\pm0.5$ is required."**
> *Continuity reminder:* **"$P(X\le k)\to P(Y<k+0.5)$; $P(X\ge k)\to P(Y>k-0.5)$; $P(X=k)\to P(k-0.5<Y<k+0.5)$. The $0.5$ shifts towards the tail you are keeping."**
> *If conditions fail:* **"Normal approximation not suitable because $np$ (or $nq$) not greater than $5$ / $n$ not large enough; distribution is skewed."**
> *Note on parameters:* When writing $H_{0}$ for a normal-approximated test you may write either $H_{0}:p=p_{0}$ or $H_{0}:\mu=np_{0}$ — but be **consistent** for $H_{0}$ and $H_{1}$.

**Method Table — Normal Approximation Hypothesis Test**

| Step | What To Do |
|------|------------|
| 1 | Check conditions: $n$ large, $np>5$, $nq>5$. State $X\sim B(n,p_{0})\approx Y\sim N(np_{0},np_{0}q_{0})$ under $H_{0}$. Compute $\mu=np_{0}$, $\sigma^{2}=np_{0}q_{0}$, $\sigma=\sqrt{np_{0}q_{0}}$. |
| 2 | State $H_{0}$, $H_{1}$, $\alpha$, tail. Translate observed $x_{\text{obs}}$ to continuity-corrected $y$: $P(X\le k)\to k+0.5$, $P(X\ge k)\to k-0.5$. |
| 3 | Standardise: $z=\frac{(y-\mu)}{\sigma}$. Use tables: find $\Phi(z)$ or $1-\Phi(z)$ as needed. This is the (approximate) $p$-value. |
| 4 | Compare $p$-value to $\alpha$: reject $H_{0}$ iff $p\le\alpha$. Sketch normal curve to verify tail (optional but prevents sign errors). |
| 5 | For critical value (reverse): solve $\Phi((c\pm0.5-\mu)/\sigma)=\alpha$ or $1-\alpha$ for $c$, then round $c$ to integer boundary of critical region. |

#### Example 1 — Easy — Coursebook Worked Example 1.4 — Arra's 200-Member Survey (91 votes)

> **Question:** Arra had $52\%$ support. Later, $200$ members surveyed, $91$ would vote for Arra. Using a suitable approximating distribution, test at $5\%$ whether support has decreased. Also, what if the claim was "support has changed"?

**Solution:**

$$X=\text{votes for Arra in 200},\;X\sim B(200,0.52)\text{ under }H_{0}$$

$$H_{0}:p=0.52\;( \mu=104),\;H_{1}:p<0.52\;( \mu<104),\;\alpha=0.05\text{ one-tailed}$$

$$np=200\times0.52=104>5$$

$$nq=200\times0.48=96>5$$

$$X\approx Y\sim N(\mu=104,\;\sigma^{2}=npq=200\times0.52\times0.48=49.92)$$

$$\sigma=\sqrt{49.92}=7.0656$$

$$x_{\text{obs}}=91,\;H_{1}:p<0.52\Rightarrow p\text{-value}=P(X\le91)\approx P(Y<91.5)$$

$$z=\frac{91.5-104}{\sqrt{49.92}}=\frac{-12.5}{7.0656}$$

$$z=-1.769$$

$$\Phi(-1.769)=1-\Phi(1.769)$$

$$\Phi(1.77)=0.9616\text{ (tables: }\Phi(1.77)=0.9616)$$

$$p\approx1-0.9616$$

$$p\approx0.0384$$

$$p=0.0384=3.84\%<5\%$$

$$\text{Reject }H_{0}\text{ at }5\%$$

$$\text{Sufficient evidence at }5\%\text{ that Arra's support has decreased}$$

$$\text{If }H_{1}:p\neq0.52\text{ (two-tailed): }\alpha/2=0.025$$

$$p=0.0384>0.025$$

$$\text{Fail to reject }H_{0}\text{ at }5\%\text{ two-tailed}$$

$$\text{Insufficient evidence that support has changed (as opposed to decreased)}$$

*Coursebook Worked Example 1.4. Sketch shows $Y\sim N(104,49.92)$, dotted line at $91.5$, left tail $3.84\%$ vs $5\%$ critical. Two-tailed comparison halves $\alpha$ — see Part 4.*

**What the examiner wants:** $\mu$, $\sigma^{2}$, $\sigma$ stated; continuity correction $91.5$ explicitly; $z=-1.769$; $\Phi$ lookup; comparison $3.84\%<5\%$ (one-tailed) vs $3.84\%>2.5\%$ (two-tailed).

#### Example 2 — Medium — Coursebook Worked Example 1.5 — Cream Trial (120 people, 79 positive)

> **Question:** $60\%$ react positively to old cream. New cream: $120$ people, $79$ react positively. (a) Does this show increase at $5\%$? (b) Find the critical value.

**Solution:**

$$X=\text{positive reactions in 120},\;X\sim B(120,0.6)\text{ under }H_{0}$$

$$H_{0}:p=0.6\;(\mu=72),\;H_{1}:p>0.6\;(\mu>72),\;\alpha=0.05\text{ one-tailed}$$

$$np=120\times0.6=72>5$$

$$nq=120\times0.4=48>5$$

$$X\approx Y\sim N(72,\;28.8),\;\sigma=\sqrt{28.8}=5.3666$$

$$x_{\text{obs}}=79,\;H_{1}:p>0.6\Rightarrow p=P(X\ge79)\approx P(Y>78.5)$$

$$z=\frac{78.5-72}{5.3666}=\frac{6.5}{5.3666}$$

$$z=1.211$$

$$\Phi(1.21)=0.8869,\;\Phi(1.211)\approx0.8871$$

$$p\approx1-\Phi(1.211)$$

$$p\approx1-0.8871=0.1129$$

$$p=0.1129=11.3\%>5\%$$

$$\text{Fail to reject }H_{0}\text{ at }5\%$$

$$\text{Insufficient evidence population reaction rate has increased}$$

$$\text{(b) Critical value }c:\;P(X\ge c)\approx P(Y>c-0.5)\le0.05$$

$$1-\Phi\left(\frac{c-0.5-72}{5.3666}\right)\le0.05$$

$$\Phi\left(\frac{c-0.5-72}{5.3666}\right)\ge0.95$$

$$\frac{c-0.5-72}{5.3666}\ge1.6449$$

$$c-0.5\ge72+1.6449\times5.3666$$

$$c-0.5\ge72+8.827$$

$$c-0.5\ge80.827$$

$$c\ge81.327$$

$$c=82?\text{ Check: }P(Y>81.5):z=(81.5-72)/5.3666=1.770,\Phi=0.9616,p=0.038<0.05\checkmark$$

$$P(Y>80.5):z=1.584,\Phi=0.9434,p=0.0566>0.05$$

$$\text{Critical region }X\ge81\text{ (text gives }c=81\text{ as integer boundary; both }81/82\text{ conventions seen — }81\text{ is the first value with }P\lesssim0.05\text{)}$$

*Coursebook Worked Example 1.5. Note $c=81$ in coursebook uses strict $x>80.8$.*

**What the examiner wants:** lower-tail vs upper-tail continuity $78.5$ ($79-0.5$); $z=1.211$; $p=11.3\%>5\%$; critical value $81$ (or $82$ with working).

#### Example 3 — Hard — Large $n$ One-Tailed, Reverse Engineered (Farmer's Sheep + 180 Flips)

> **Question:** (a) Farmer: $30\%$ mineral-deficient, tests $80$ sheep, $19$ deficient. Test at $10\%$ if rate decreased, using normal approx. Find critical value. (b) Coin flipped $180$ times, $102$ tails, claim $p>0.5$ at $5\%$?

**Solution (a) — Farmer:**

$$X\sim B(80,0.3)\text{ under }H_{0},\;H_{0}:p=0.3,\;H_{1}:p<0.3,\;\alpha=0.10$$

$$np=24>5,\;nq=56>5$$

$$X\approx Y\sim N(24,\;16.8),\;\sigma=\sqrt{16.8}=4.0988$$

$$x_{\text{obs}}=19,\;p=P(X\le19)\approx P(Y<19.5)$$

$$z=\frac{19.5-24}{4.0988}=\frac{-4.5}{4.0988}$$

$$z=-1.0978$$

$$\Phi(-1.0978)=1-\Phi(1.0978)$$

$$\Phi(1.10)=0.8643$$

$$p\approx0.1357$$

$$p=13.6\%>10\%$$

$$\text{Fail to reject }H_{0}\text{ at }10\%$$

$$\text{Insufficient evidence mineral deficiency rate has decreased}$$

$$\text{Critical value: }P(Y< c+0.5)\le0.10$$

$$\Phi\left(\frac{c+0.5-24}{4.0988}\right)\le0.10$$

$$\frac{c+0.5-24}{4.0988}\le\Phi^{-1}(0.10)=-1.2816$$

$$c+0.5\le24-1.2816\times4.0988$$

$$c+0.5\le24-5.253$$

$$c+0.5\le18.747$$

$$c\le18.247$$

$$c=18\text{ (critical region }X\le18)$$

**Solution (b) — Dan's 180 Coin Flips:**

$$X\sim B(180,0.5)\text{ under }H_{0},\;H_{0}:p=0.5,\;H_{1}:p>0.5,\;\alpha=0.05$$

$$np=90>5,\;nq=90>5$$

$$X\approx Y\sim N(90,\;45),\;\sigma=\sqrt{45}=6.7082$$

$$x_{\text{obs}}=102,\;p=P(X\ge102)\approx P(Y>101.5)$$

$$z=\frac{101.5-90}{6.7082}=\frac{11.5}{6.7082}$$

$$z=1.714$$

$$\Phi(1.71)=0.9564,\;\Phi(1.714)\approx0.9569$$

$$p\approx1-0.9569=0.0431$$

$$p=4.31\%<5\%$$

$$\text{Reject }H_{0}\text{ at }5\%$$

$$\text{Sufficient evidence coin is biased towards tails (based on 180 flips)}$$

*Contrast with $9$ flips, $7$ tails: $P(X\ge7\mid n=9,p=0.5)=1-P(X\le6)=1-0.9102=0.0898>5\%$ → fail to reject. Same proportion ($77.8\%$ vs $56.7\%$ tails) but large $n$ gives significance — power increases with $n$.*

**What the examiner wants:** $np$, $nq$, $\mu$, $\sigma$ checks; continuity direction; $z$ and $\Phi$; decision at stated $\alpha$.

#### Example 4 — Trap — Continuity Correction Direction (Spinner Blue, 120 spins, 40 blue)

> **Question:** Four-colour spinner, $p=0.25$ for blue. Spun $120$ times, $40$ blue. Test at $2\%$ whether biased towards blue (upper tail). A student uses $P(Y>40.5)$ instead of $P(Y>39.5)$. Show the error.

**Solution:**

$$X\sim B(120,0.25)\text{ under }H_{0},\;H_{0}:p=0.25,\;H_{1}:p>0.25,\;\alpha=0.02$$

$$np=30>5,\;nq=90>5$$

$$X\approx Y\sim N(30,\;22.5),\;\sigma=\sqrt{22.5}=4.7434$$

$$\text{Correct: }P(X\ge40)\approx P(Y>39.5)$$

$$z_{\text{correct}}=\frac{39.5-30}{4.7434}=\frac{9.5}{4.7434}$$

$$z_{\text{correct}}=2.003$$

$$\Phi(2.00)=0.9772,\;\Phi(2.003)\approx0.9773$$

$$p_{\text{correct}}=1-0.9773=0.0227$$

$$p=2.27\%>2\%$$

$$\text{Fail to reject }H_{0}\text{ at }2\%\text{ (borderline — correct decision)}$$

$$\text{Wrong: }P(Y>40.5)$$

$$z_{\text{wrong}}=\frac{40.5-30}{4.7434}=2.214$$

$$\Phi(2.21)=0.9864$$

$$p_{\text{wrong}}=1-0.9864=0.0136$$

$$p_{\text{wrong}}=1.36\%<2\%$$

$$\text{Wrongly reject }H_{0}\text{ at }2\%$$

*Error: $P(X\ge k)\to P(Y>k-0.5)$, not $k+0.5$. Shifting $0.5$ the wrong way moves $z$ by $0.5/\sigma\approx0.11$, enough to flip a borderline test.*

> ⚠️ **Watch Out! — Part 3**
> (1) **Check $np>5$ and $nq>5$ first** — if not, normal approximation is skewed; use exact binomial instead. (2) **Continuity sign:** upper tail $P(X\ge k)\to k-0.5$ (go *down* to include $k$'s bar); lower tail $P(X\le k)\to k+0.5$ (go *up*). Draw the discrete histogram bar $[k-0.5,k+0.5]$ to visualise. (3) **Don't forget $\sqrt{npq}$** — variance is $npq$, not $np$. (4) **Tables give $\Phi(z)$ for $Z\le z$** — $P(Z>z)=1-\Phi(z)$, and $\Phi(-z)=1-\Phi(z)$. Sketch the curve to avoid sign errors.

---

# PART 4: p-Value vs Critical Region & Two-Tailed Tests

*Two ways to decide: compare $p$-value to $\alpha$ (preferred) or check if observed value lies in pre-computed critical region. For two-tailed, split $\alpha$.*

## 4.1 p-Value Method and Splitting α for Two Tails

**The Rule**

$$p\text{-value}=P(\text{data at least as extreme as observed}\mid H_{0}),\quad \text{Reject }H_{0}\iff p\le\alpha$$

$$\text{Two-tailed }(H_{1}:p\neq p_{0}):\; \alpha\text{ split as }\alpha/2\text{ per tail; }p_{\text{two-tailed}}=2\times\min(P(X\ge x_{\text{obs}}),P(X\le x_{\text{obs}}))\text{ or compare one tail to }\alpha/2$$

> ⭐ **Justification Box — p-Value vs Critical Region; Two-Tailed Split**
> *p-value method:* **"p-value $=P(X\ge x_{\text{obs}}\mid H_{0})$ (or $\le$, or $2\times$tail). Compare $p$ with $\alpha$: if $p\le\alpha$ reject $H_{0}$, otherwise fail to reject $H_{0}$."**
> *Critical region method:* **"Critical region is $\{X\ge c: P(X\ge c\mid H_{0})\le\alpha\}$ (or $\le c$). Since $x_{\text{obs}}$ lies inside/outside the critical region, reject/fail to reject $H_{0}$."** — Both methods give the same decision; show one clearly.
> *Two-tailed:* **"As $H_{1}:p\neq p_{0}$, share $\alpha$ equally: $\alpha/2$ per tail. For $\alpha=5\%$, each tail $2.5\%$. Compare one-tail $p$ to $2.5\%$, or double $p$ and compare to $5\%$."** Pick one convention and state it.
> *Wording cue:* **"Two-tailed when the question says 'different / incorrect / not equal / changed / not working correctly' without a direction. One-tailed when it says 'more / less / increase / decrease / biased towards'."**

**Method Table — p-Value vs Critical Region; Two-Tailed**

| Step | What To Do |
|------|------------|
| 1 | State $H_{0}$, $H_{1}$, $\alpha$, and whether one- or two-tailed (explain wording cue). |
| 2 | For p-value: compute tail probability under $H_{0}$ — upper tail if $x_{\text{obs}}$ above $\mu$, lower tail if below. For two-tailed: compute the smaller tail and double it (or compare that tail to $\alpha/2$). Apply continuity correction if using normal approx. |
| 3 | For critical region: find boundary $c$ where tail probability first $\le\alpha$ (or $\le\alpha/2$ per tail) and state region ($X\le c$ or $X\ge c$ or both). |
| 4 | Decision: $p\le\alpha$ (or $p\le\alpha/2$ per tail) → reject $H_{0}$; equivalently $x_{\text{obs}}$ in critical region → reject. |
| 5 | Conclusion: "At the $\alpha\%$ level there is (in)sufficient evidence that [context: rate has changed / increased / spinner is biased etc.]." Mention two-tailed nuance if applicable. |

#### Example 1 — Easy — Coursebook Spinner Two-Tailed (10 spins, 5 red at 5%)

> **Question:** Same pentagonal spinner $p=0.2$, $10$ spins, $5$ red. Test at $5\%$ whether the spinner is not working correctly (i.e. $p\neq0.2$).

**Solution:**

$$X\sim B(10,0.2)\text{ under }H_{0},\;H_{0}:p=0.2,\;H_{1}:p\neq0.2,\;\alpha=0.05\text{ two-tailed}$$

$$P(X\ge5)=0.03279\text{ (from Part 2, Example 3)}$$

$$\alpha/2=0.025\text{ per tail}$$

$$P(X\ge5)=0.0328>0.025$$

$$p_{\text{two-tailed}}=2\times0.0328=0.0656>0.05$$

$$\text{Fail to reject }H_{0}\text{ at }5\%\text{ two-tailed}$$

$$\text{Insufficient evidence spinner is not working correctly}$$

$$\text{(One-tailed at }5\%\text{ would reject — direction matters!)}$$

*Compare: one-tailed $H_{1}:p>0.2$ at $5\%$: $0.0328<0.05$ → reject. Two-tailed at $5\%$: need $p<0.025$ per tail → $0.0328>0.025$ → fail to reject. Same data, different $H_{1}$, opposite decision.*

**What the examiner wants:** $\alpha/2=2.5\%$ stated, $0.0328>0.025$ comparison (or doubled $p$ vs $5\%$), correct two-tailed conclusion.

#### Example 2 — Medium — Coursebook Worked Example 1.6 — Jamila's Fossils (12 rocks, 2 fossils, 35%)

> **Question:** $35\%$ of rocks contain fossils. Jamila breaks $12$ rocks, finds $2$ fossils. (a) Test at $10\%$ two-tailed whether $35\%$ is incorrect. (b) How many fossils would she need to find to reject $H_{0}$? (c) Would conclusion differ if test were one-tailed ($H_{1}:p<0.35$)?

**Solution:**

$$X\sim B(12,0.35)\text{ under }H_{0},\;H_{0}:p=0.35,\;H_{1}:p\neq0.35,\;\alpha=0.10\text{ two-tailed}$$

$$P(X\le2)=\sum_{r=0}^{2}\binom{12}{r}0.35^{r}0.65^{12-r}$$

$$P(X=0)=0.65^{12}=0.00569$$

$$P(X=1)=12\times0.35\times0.65^{11}=12\times0.35\times0.00876=0.03679$$

$$P(X=2)=\binom{12}{2}0.35^{2}0.65^{10}=66\times0.1225\times0.01348=0.10896$$

$$P(X\le2)=0.00569+0.03679+0.10896$$

$$P(X\le2)=0.15144$$

$$P(X\le2)=0.1514>0.05\;(\alpha/2=0.05)$$

$$\text{(a) Fail to reject }H_{0}\text{ at }10\%\text{ two-tailed}$$

$$\text{Insufficient evidence that }35\%\text{ is incorrect; Jamila was unlucky but not significantly so}$$

$$P(X\le1)=0.00569+0.03679=0.04248$$

$$P(X\le1)=0.04248<0.05$$

$$P(X\ge8)=1-P(X\le7)$$

$$P(X=8)=0.0255\text{ tail gives }P(X\ge8)=0.0255<0.05$$

$$P(X\ge7)=0.0846>0.05$$

$$\text{(b) Critical values: }X\le1\text{ or }X\ge8\text{ (both tails at }5\%\text{ each)}$$

$$\text{Need }0,1\text{ fossils (lower) or }8+\text{ fossils (upper) to reject at }10\%\text{ two-tailed}$$

$$H_{1}:p<0.35,\;\alpha=0.10\text{ one-tailed}:\;P(X\le2)=0.1514>0.10$$

$$\text{(c) Fail to reject even one-tailed at }10\%\text{ (need }\le1\text{ for }P\le0.10)$$

$$\text{Conclusion unchanged; }2\text{ fossils not significant either way}$$

*Coursebook Worked Example 1.6. Graph shows acceptance region between dotted lines.*

**What the examiner wants:** $\alpha/2=5\%$ per tail, $P(X\le2)=15.1\%>5\%$, critical values $1$ and $8$, recognition that one-tailed also fails at $10\%$.

#### Example 3 — Hard — Large-$n$ Two-Tailed via Normal Approx (Arra Two-Tailed Revisited + Horoscopes)

> **Question:** $80\%$ of Americans believe in horoscopes. Madison asks $160$ people, $116$ believe. Test at $5\%$ two-tailed whether $80\%$ is incorrect, using normal approximation. Also test $n=16$, $15$ believers at $10\%$ two-tailed via exact binomial.

**Solution — Large sample ($n=160$):**

$$X\sim B(160,0.8)\text{ under }H_{0},\;H_{0}:p=0.8,\;H_{1}:p\neq0.8,\;\alpha=0.05\text{ two-tailed}$$

$$np=128>5,\;nq=32>5$$

$$X\approx Y\sim N(128,\;25.6),\;\sigma=\sqrt{25.6}=5.0596$$

$$x_{\text{obs}}=116<128\Rightarrow\text{ lower tail}$$

$$p_{\text{one tail}}=P(X\le116)\approx P(Y<116.5)$$

$$z=\frac{116.5-128}{5.0596}=\frac{-11.5}{5.0596}$$

$$z=-2.273$$

$$\Phi(-2.273)=1-\Phi(2.273)$$

$$\Phi(2.27)=0.9884$$

$$p_{\text{one tail}}\approx0.0116$$

$$\alpha/2=0.025$$

$$p_{\text{one tail}}=0.0116<0.025$$

$$p_{\text{two-tailed}}=2\times0.0116=0.0232<0.05$$

$$\text{Reject }H_{0}\text{ at }5\%\text{ two-tailed}$$

$$\text{Sufficient evidence that }80\%\text{ claim is incorrect}$$

**Solution — Small sample ($n=16$):**

$$X\sim B(16,0.8)\text{ under }H_{0},\;H_{0}:p=0.8,\;H_{1}:p\neq0.8,\;\alpha=0.10\text{ two-tailed}$$

$$x_{\text{obs}}=15>12.8\text{ (expected) }\Rightarrow\text{ upper tail}$$

$$P(X\ge15)=\binom{16}{15}0.8^{15}0.2^{1}+0.8^{16}$$

$$P(X=15)=16\times0.035184\times0.2=0.11259$$

$$P(X=16)=0.028147$$

$$P(X\ge15)=0.11259+0.028147=0.14074$$

$$p_{\text{one tail}}=0.14074>\alpha/2=0.05$$

$$p_{\text{two-tailed}}=2\times0.14074=0.2815>0.10$$

$$\text{Fail to reject }H_{0}\text{ at }10\%\text{ two-tailed}$$

$$\text{Insufficient evidence with only 16 people}$$

$$\text{Critical value: }P(X\ge15)=0.1407>0.05,\text{ but }P(X\ge16)=0.0281<0.05\Rightarrow X=16\text{ is critical (upper tail)}$$

*Coursebook Exercise 1B Q3. Same claim, opposite decisions: $n=160$ rejects, $n=16$ doesn't — sample size is power.*

**What the examiner wants:** split $\alpha/2=2.5\%$ (large $n$) and $5\%$ (small $n$), correct tail selection, doubled $p$ vs $\alpha$.

#### Example 4 — Trap — p-Value Method vs Critical Region Must Agree (Yolande vs Xavier)

> **Question:** $25\%$ of programmes are nature programmes. Yolande tests $H_{1}:p<0.25$ (one-tailed, $10\%$) with $n=20$, observes $X=2$. Xavier tests $H_{1}:p\neq0.25$ (two-tailed, $10\%$) with same data $X=2$. Show they reach different conclusions and explain why both methods (p-value and critical region) give the same answer within each test.

**Solution:**

$$X\sim B(20,0.25)\text{ under }H_{0}$$

$$P(X\le1)=\binom{20}{0}0.75^{20}+\binom{20}{1}0.25\times0.75^{19}$$

$$P(X=0)=0.003171,\;P(X=1)=0.021141$$

$$P(X\le1)=0.02431$$

$$P(X=2)=\binom{20}{2}0.25^{2}0.75^{18}=190\times0.0625\times0.005637=0.06695$$

$$P(X\le2)=0.02431+0.06695=0.09126$$

**Yolande (one-tailed, $\alpha=0.10$):**

$$p=P(X\le2)=0.09126<0.10$$

$$\text{Reject }H_{0}\text{ at }10\%\text{ one-tailed}$$

$$\text{Critical region: }P(X\le1)=0.0243<0.10,\;P(X\le2)=0.0913<0.10,\;P(X\le3)=0.0913+0.1339=0.2252>0.10$$

$$\text{Critical region }X\le2,\;x_{\text{obs}}=2\in\text{critical region}\Rightarrow\text{ reject (same decision)}$$

**Xavier (two-tailed, $\alpha=0.10$, $\alpha/2=0.05$):**

$$p_{\text{one tail}}=P(X\le2)=0.09126>0.05$$

$$p_{\text{two-tailed}}=2\times0.09126=0.1825>0.10$$

$$\text{Fail to reject }H_{0}\text{ at }10\%\text{ two-tailed}$$

$$\text{Critical region per tail: }P(X\le1)=0.0243<0.05\text{ vs }P(X\le2)=0.0913>0.05\Rightarrow X\le1\text{ (lower)}$$

$$x_{\text{obs}}=2\notin\text{critical region}\Rightarrow\text{ fail to reject (same decision)}$$

$$\text{p-value and critical-region methods agree in each case; tails differ between tests}$$

*Coursebook Exercises 1A Q1 and 1B Q1 — same data, one-tailed vs two-tailed.*

> ⚠️ **Watch Out! — Part 4**
> (1) **Two-tailed ≠ one-tailed at same $\alpha$:** $p=3.9\%$ rejects one-tailed at $5\%$ but not two-tailed ($3.9\%>2.5\%$). Always halve $\alpha$. (2) **Double one tail or halve $\alpha$ — not both:** $p_{\text{two-tailed}}=2\times p_{\text{one tail}}$ compare to $\alpha$; OR $p_{\text{one tail}}$ compare to $\alpha/2$. Doing $2p\le\alpha/2$ is halving twice (wrong). (3) **Critical region per tail:** for $\alpha=10\%$ two-tailed, each tail $5\%$ — find $c$ per tail separately; $X\le1$ may be critical lower, $X\ge9$ upper, but $X\le2$ not critical if its tail exceeds $5\%$.

---

# PART 5: Type I and Type II Errors

*A hypothesis test can err in two directions — rejecting a true $H_{0}$ or failing to reject a false $H_{0}$.*

## 5.1 Definitions, Probabilities, and Trade-Offs

**The Rule**

$$\boxed{\begin{aligned}\text{Type I error}&=P(\text{reject }H_{0}\mid H_{0}\text{ true})=P(X\in\text{critical region}\mid H_{0})=\alpha_{\text{actual}}\\\text{Type II error}&=P(\text{fail to reject }H_{0}\mid H_{0}\text{ false})=P(X\notin\text{critical region}\mid H_{1}\text{ true alternative value})\end{aligned}}$$

$$\text{Power}=1-P(\text{Type II})=P(\text{reject }H_{0}\mid H_{1}\text{ true})$$

> ⭐ **Justification Box — Type I / Type II (exact sentences)**
> *Type I:* **"A Type I error occurs when $H_{0}$ is rejected although $H_{0}$ is true — a false positive. $P(\text{Type I})=P(X\in\text{critical region}\mid H_{0})$, which equals the (actual) significance level $\alpha$."** Court analogy: convicting an innocent person.
> *Type II:* **"A Type II error occurs when $H_{0}$ is not rejected although $H_{0}$ is false — a false negative. $P(\text{Type II})=P(X\notin\text{critical region}\mid\text{true }p=p_{1})$. To compute it you need a specific alternative value $p_{1}$."** Court analogy: acquitting a guilty person.
> *Trade-off:* **"Decreasing $\alpha$ (smaller critical region) decreases $P(\text{Type I})$ but increases $P(\text{Type II})$ (and reduces power). Increasing $n$ decreases both error probabilities."**
> *In context template:* **"Type I here means concluding [e.g. coin is biased / training is effective] when in fact $p$ is still $p_{0}$." "Type II here means concluding no change when the true $p$ is actually $p_{1}$."** Never just "Type I = reject $H_{0}$" without stating true vs false.

**Method Table — Type I / Type II Probabilities**

| Step | What To Do |
|------|------------|
| 1 | Identify critical region $C$ from the test (e.g. $X\ge12$ at $5\%$, or $X\le1$). State it explicitly. |
| 2 | For Type I: compute $P(X\in C\mid H_{0})$ — exact binomial sum with $p_{0}$, or normal approx with continuity if $n$ large. This is the actual $\alpha$ (may be $< $ nominal $\alpha$ due to discreteness). |
| 3 | For Type II: you need an alternative true value $p_{1}$ (given in question). Compute $P(X\notin C\mid p_{1})=1-P(X\in C\mid p_{1})$ — i.e. probability of landing in acceptance region when $H_{1}$ with $p=p_{1}$ is true. |
| 4 | Interpret in context: state what each error means for the scenario (coin, drug, training). |
| 5 | Comment on trade-off: smaller $\alpha$ → smaller $C$ → lower Type I but higher Type II; larger $n$ or larger effect size $|p_{1}-p_{0}|$ → higher power. |

#### Example 1 — Easy — Coursebook Worked Example 1.7 — Referee's Coin (16 matches, 12+ tails critical)

> **Question:** A referee's coin is tested for bias towards tails. $H_{0}:p=0.5$, $H_{1}:p>0.5$, $n=16$, $\alpha=5\%$ one-tailed. (a) Find Type I error probability and explain Type I in context. (b) Explain Type II if $11$ tails observed.

**Solution:**

$$X=\text{tails in 16 tosses},\;X\sim B(16,0.5)\text{ under }H_{0}$$

$$P(X\ge11)=\sum_{r=11}^{16}\binom{16}{r}0.5^{16}$$

$$P(X\ge12)=0.03841,\;P(X\ge11)=0.10506$$

$$P(X\ge12)=0.0384<0.05,\;P(X\ge11)=0.1051>0.05$$

$$\text{Critical region }C=\{X\ge12\},\;\text{ critical value }12$$

$$(a)\;P(\text{Type I})=P(X\ge12\mid p=0.5)=0.0384$$

$$P(\text{Type I})=0.0384=3.84\%$$

$$\text{Type I in context: Conclude coin is biased towards tails when it is actually fair}$$

$$(b)\;x_{\text{obs}}=11\notin C\Rightarrow\text{ fail to reject }H_{0}$$

$$P(X\ge11)=0.1051>0.05$$

$$\text{If }H_{0}\text{ is actually false (coin biased), failing to reject with }11\text{ tails is a Type II error}$$

$$\text{(Cannot compute }P(\text{Type II})\text{ without true }p_{1}\text{ — e.g. if }p_{1}=0.7,\;P(\text{Type II})=P(X\le11\mid p=0.7))$$

*Coursebook Worked Example 1.7. Note $P(\text{Type I})=3.84\%<5\%$ nominal — binomial discreteness means actual $\alpha$ < nominal $\alpha$.*

**What the examiner wants:** critical region $12+$, $P(\text{Type I})=0.0384$, context "biased when fair", explanation that $11$ tails → accept $H_{0}$ → Type II possible if $H_{0}$ false.

#### Example 2 — Medium — Drug / Sunflower Type I & II with Normal Distribution

> **Question:** Sunflower heights $X\sim N(1.8,0.32^{2})$. Test $H_{0}:\mu=1.8$ vs $H_{1}:\mu>1.8$ at $\mu_{1}=2.4$. Gardener convinced if $X>2.25$ for one random plant. (a) Find $P(\text{Type I})$. (b) Find $P(\text{Type II})$ if true $\mu=2.4$.

**Solution:**

$$H_{0}:X\sim N(1.8,0.32^{2}),\;H_{1}:X\sim N(2.4,0.32^{2}),\;C=\{X>2.25\}$$

$$(a)\;P(\text{Type I})=P(X>2.25\mid\mu=1.8)$$

$$z=\frac{2.25-1.8}{0.32}=\frac{0.45}{0.32}$$

$$z=1.40625$$

$$\Phi(1.41)=0.9207,\;\Phi(1.406)\approx0.9202$$

$$P(\text{Type I})=1-\Phi(1.406)$$

$$P(\text{Type I})\approx1-0.9202=0.0798$$

$$P(\text{Type I})\approx0.080=8.0\%$$

$$(b)\;P(\text{Type II})=P(X\le2.25\mid\mu=2.4)$$

$$z=\frac{2.25-2.4}{0.32}=\frac{-0.15}{0.32}$$

$$z=-0.46875$$

$$\Phi(-0.4688)=1-\Phi(0.4688)$$

$$\Phi(0.47)=0.6808$$

$$P(\text{Type II})=\Phi(-0.4688)=1-0.6808$$

$$P(\text{Type II})\approx0.319$$

$$P(\text{Type II})\approx32\%$$

*Coursebook Exercise 1C Q4 (gardener). Power $=1-0.319=0.681=68.1\%$. Trade-off: lowering threshold $2.25$ would reduce Type II but increase Type I.*

**What the examiner wants:** Type I $\approx8\%$, Type II $\approx32\%$, standardisation with $\sigma=0.32$, $1-\Phi$ for upper tail.

#### Example 3 — Hard — Type I = Type II Balance Point + Blood Protein Two-Tailed

> **Question:** Protein level $X$: without condition $X\sim N(10,3^{2})$, with condition $X\sim N(22,7^{2})$. Doctor flags "has condition" if $X>17$. $H_{0}$: no condition, $H_{1}$: has condition. (a) Find $P(\text{Type I})$ and $P(\text{Type II})$. (b) Find range of $X$ flag values where $P(\text{Type II})<0.03$ if condition present ($N(22,7^{2})$). (c) Find $x$ where $P(\text{Type I})=P(\text{Type II})$.

**Solution:**

$$(a)\;P(\text{Type I})=P(X>17\mid N(10,3^{2}))$$

$$z_{I}=\frac{17-10}{3}=\frac{7}{3}$$

$$z_{I}=2.333$$

$$\Phi(2.33)=0.9901$$

$$P(\text{Type I})=1-\Phi(2.333)$$

$$P(\text{Type I})=1-0.9901=0.0099$$

$$P(\text{Type II})=P(X\le17\mid N(22,7^{2}))$$

$$z_{II}=\frac{17-22}{7}=\frac{-5}{7}$$

$$z_{II}=-0.7143$$

$$\Phi(-0.7143)=1-\Phi(0.7143)$$

$$\Phi(0.71)=0.7611,\;\Phi(0.7143)\approx0.7623$$

$$P(\text{Type II})=0.2377$$

$$P(\text{Type II})\approx0.238=23.8\%$$

$$(b)\;P(X<a\mid N(22,7^{2}))<0.03$$

$$\Phi\left(\frac{a-22}{7}\right)<0.03$$

$$\frac{a-22}{7}<\Phi^{-1}(0.03)=-1.8808$$

$$a<22-1.8808\times7$$

$$a<22-13.1656$$

$$a<8.834$$

$$\text{Flag only if }X<8.8\text{ would give false-negative }<3\%\text{ (impractical — use larger threshold and accept higher Type II)}$$

$$\text{If question means }P(X>a)<0.03\text{ for Type II upper: }P(X\le a)<0.03\Rightarrow a<8.8\text{ as above}$$

$$(c)\;1-\Phi\left(\frac{x-10}{3}\right)=\Phi\left(\frac{x-22}{7}\right)$$

$$\Phi\left(\frac{10-x}{3}\right)=\Phi\left(\frac{x-22}{7}\right)$$

$$\frac{10-x}{3}=\frac{x-22}{7}$$

$$7(10-x)=3(x-22)$$

$$70-7x=3x-66$$

$$136=10x$$

$$x=13.6$$

$$P(\text{Type I})=P(\text{Type II})\approx1-\Phi(1.20)=1-0.8849=0.115\text{ at }x=13.6$$

*Coursebook Worked Example 1.8. Part (c) solves $1-\Phi((x-10)/3)=\Phi((x-22)/7)$ → $x=13.6$.*

**What the examiner wants:** $z=7/3$ and $z=-5/7$, $P(\text{I})=0.99\%$, $P(\text{II})=23.8\%$, solving $a<8.83$ for $3\%$ Type II, $x=13.6$ balanced.

#### Example 4 — Trap — Calculating Type II Needs an Alternative $p_{1}$

> **Question:** Janina rolls an 8-sided die $20$ times, $p=1/8=0.125$ under $H_{0}$. She will call the die biased towards $1$ if $X\ge4$ ($X$ = number of $1$s). (a) Find $P(\text{Type I})$ and explain Type I in context. (b) Explain Type II in context; why can't you compute $P(\text{Type II})$ yet, and what extra info is needed?

**Solution:**

$$X\sim B(20,0.125)\text{ under }H_{0},\;C=\{X\ge4\}$$

$$P(X\le3)=\sum_{r=0}^{3}\binom{20}{r}0.125^{r}0.875^{20-r}$$

$$P(X=0)=0.875^{20}=0.0692$$

$$P(X=1)=20\times0.125\times0.875^{19}=0.1977$$

$$P(X=2)=\binom{20}{2}0.125^{2}0.875^{18}=190\times0.015625\times0.09038=0.2684$$

$$P(X=3)=\binom{20}{3}0.125^{3}0.875^{17}=0.2302$$

$$P(X\le3)=0.0692+0.1977+0.2684+0.2302=0.7655$$

$$P(\text{Type I})=P(X\ge4\mid p=0.125)=1-0.7655$$

$$P(\text{Type I})=0.2345=23.5\%$$

$$\text{Type I: Conclude die is biased towards }1\text{ when it is actually fair }(p=0.125)$$

$$\text{Type II: Conclude die is NOT biased (accept }H_{0}\text{) when it actually IS biased }(p>0.125)$$

$$\text{Cannot compute }P(\text{Type II})=P(X\le3\mid p=p_{1})\text{ without true }p_{1}$$

$$\text{Need }p_{1}\text{ e.g. "true }p=0.25\text{": then }P(\text{Type II})=P(X\le3\mid B(20,0.25))=0.2252\text{ (computed earlier)}$$

*Coursebook Exercise 1C M5 (Janina, 8-sided die). Moral: Type I uses $H_{0}$'s $p_{0}$; Type II needs a specific alternative $p_{1}$ — without it only the definition can be stated.*

> ⚠️ **Watch Out! — Part 5**
> (1) **Type I = $\alpha_{\text{actual}}$:** $P(\text{Type I})=P(X\in C\mid H_{0})$ — not the nominal $\alpha$ if the binomial jump skips the exact $\alpha$ value. (2) **Type II needs $p_{1}$:** without a stated true alternative, you can only describe Type II in words, not calculate it. (3) **Don't swap:** Type I uses $H_{0}$'s distribution; Type II uses the alternative's distribution; swapping gives nonsense. (4) **Interpretation must be contextual:** "Type I means conclude the die is biased when it is fair" scores; "Type I is rejecting $H_{0}$ when $H_{0}$ is true" alone does not (needs context). (5) **Trade-off:** decreasing $\alpha$ (harder to reject) → $P(\text{I})\downarrow$ but $P(\text{II})\uparrow$; increasing $n$ → both $\downarrow$.

---

# Formula Sheet

$$\boxed{X\sim B(n,p),\;P(X=r)=\binom{n}{r}p^{r}(1-p)^{n-r},\;E[X]=np,\;Var[X]=npq}$$

$$\boxed{H_{0}:p=p_{0},\;H_{1}:p<p_{0}\;(p>p_{0},\;p\neq p_{0}),\;\alpha=P(\text{Type I})}$$

$$\boxed{\text{Test statistic (one-tailed): }P(X\le x_{\text{obs}})\;(H_{1}:p<p_{0}),\quad P(X\ge x_{\text{obs}})\;(H_{1}:p>p_{0})}$$

$$\boxed{\text{Reject }H_{0}\iff p\text{-value}\le\alpha\quad\text{or}\quad x_{\text{obs}}\in\text{critical region}}$$

$$\boxed{\text{Two-tailed }(p\neq p_{0}):\;\alpha/2\text{ per tail; }p_{\text{two}}=2\times\min(P_{\text{lower}},P_{\text{upper}})\le\alpha\text{ to reject}}$$

$$\boxed{X\sim B(n,p),\;np>5,\;nq>5\Rightarrow X\approx Y\sim N(np,\;npq),\;\sigma=\sqrt{npq},\;\text{continuity }\pm0.5}$$

$$\boxed{\begin{aligned}P(X\le k)&\approx P(Y<k+0.5)\\P(X\ge k)&\approx P(Y>k-0.5)\\P(X=k)&\approx P(k-0.5<Y<k+0.5)\\P(a\le X\le b)&\approx P(a-0.5<Y<b+0.5)\end{aligned}\quad Z=\frac{Y-np}{\sqrt{npq}}}$$

$$\boxed{\Phi(z)=P(Z\le z),\;P(Z>z)=1-\Phi(z),\;\Phi(-z)=1-\Phi(z),\;\Phi^{-1}(0.95)=1.645,\;\Phi^{-1}(0.975)=1.96}$$

$$\boxed{P(\text{Type I})=P(X\in C\mid H_{0}),\quad P(\text{Type II})=P(X\notin C\mid p=p_{1}),\quad\text{Power}=1-P(\text{Type II})}$$

$$\boxed{\text{Decreasing }\alpha\Rightarrow P(\text{I})\downarrow,\;P(\text{II})\uparrow;\quad\text{Increasing }n\Rightarrow\text{both }\downarrow}$$

---

# Methods Summary Table

| Situation | Type 1 — Direct / Small $n$ | Type 2 — Large $n$ / Normal Approx | Type 3 — Two-Tailed / Reverse / Errors | Past Paper Ref |
|---|---|---|---|---|
| **Set up $H_{0},H_{1}$** ($p\mid\mu$) | $H_{0}:p=0.4$ vs $p<0.4$ (Zander, 20 drivers) | $H_{0}:p=0.52$ vs $p<0.52$ → $H_{0}:\mu=104$ (Arra, $n=200$) | $H_{0}:p=0.35$ vs $p\neq0.35$ (Jamila, 12 rocks, two-tailed) | Coursebook WE 1.1–1.6 |
| **$P(X\le k)$ / $P(X\ge k)$ exact** | $P(X\le4\mid B(20,0.4))=0.05095$; $P(X\le1\mid B(50,0.1))=0.0338$ | — | $P(X\le2\mid B(12,0.35))=0.151$; $P(X\ge5\mid B(10,0.2))=0.0328$ | WE 1.1, WE 1.2, WE 1.3 |
| **Normal approx $\approx N(np,npq)\pm0.5$** | Check $np>5,nq>5$ first | Arra: $Y\sim N(104,49.92)$, $P(Y<91.5)=3.84\%$; Cream: $N(72,28.8)$, $P(Y>78.5)=11.3\%$ | Spinner blue: $N(30,22.5)$, $P(Y>39.5)=2.27\%$ borderline at $2\%$ | WE 1.4, WE 1.5 |
| **$p$-value vs critical region** | $p=P(X\le x_{\text{obs}})$ compare to $\alpha$; or $x_{\text{obs}}\in\{X\le c\}$? | $p\approx P(Y<k\pm0.5)$ via $z$, compare to $\alpha$ | Two-tailed: $p/2\le\alpha/2$? Critical per tail $X\le1$ and $X\ge8$ (Jamila) | Exercise 1A/1B |
| **Critical value search** | Bailin: $X\le1$ ($P=3.38\%$); $X\le2$ gives $11.2\%>5\%$ | Cream: $81$ (or $82$); Farmer $X\le18$ at $10\%$ | Jamila: $1$ and $8$ at $10\%$ two-tailed | WE 1.2(b), WE 1.5(b), Farmer |
| **Type I / Type II** | Ref coin $P(\text{I})=P(X\ge12\mid0.5)=3.84\%$ | Sunflower $N(1.8,0.32^{2})$: $P(\text{I})=8.0\%$, $P(\text{II})=31.9\%$ | Blood protein: $P(\text{I})=0.99\%$, $P(\text{II})=23.8\%$, balance $x=13.6$; Janina needs $p_{1}$ for Type II | WE 1.7, WE 1.8, Ex 1C M5 |
| **Decision wording** | $0.05095>0.05$ → fail to reject at $5\%$ | $3.84\%<5\%$ → reject at $5\%$ one-tailed; $>2.5\%$ → fail two-tailed | $0.151>5\%$ per tail → fail to reject two-tailed | All WEs |

---

# Justification Bank — Copy-Paste Sentences (earn the 1–2 justification marks)

**State hypotheses (1 mark):**

> *"Let $X$ be the number of [successes] in $n$ trials. Under $H_{0}$, $X\sim B(n,p_{0})$ with $p_{0}=...$. $H_{0}:p=p_{0}$, $H_{1}:p<p_{0}$ (or $>$, $\neq$) at $\alpha\%$ significance level, one-tailed (two-tailed) test."*

**Normal approximation justification (1–2 marks):**

> *"$n=...$ is large and $np=... >5$ and $nq=... >5$, so $B(n,p)\approx N(np,npq)$ with $\mu=np=...$, $\sigma^{2}=npq=...$, $\sigma=\sqrt{...}=...$. As binomial is discrete and normal is continuous, a continuity correction of $\pm0.5$ is required: $P(X\le k)\to P(Y<k+0.5)$, $P(X\ge k)\to P(Y>k-0.5)$."*

**Normal approximation NOT suitable:**

> *"Normal approximation not suitable because $np$ (or $nq$) is not greater than $5$ / $n$ is not large enough; the binomial distribution is skewed."*

**p-value decision (1 mark):**

> *"p-value $=P(X\le x_{\text{obs}}\mid H_{0})=...$ (or $\ge$). Since $p=...\le\alpha$ ($\alpha=0.05$), reject $H_{0}$. There is sufficient evidence at the $\alpha\%$ level that [context: proportion has decreased/increased]."*
> *"Since $p=...>\alpha$, fail to reject $H_{0}$. There is insufficient evidence at the $\alpha\%$ level to support the claim that [context]."*

**Two-tailed split explanation (1 mark):**

> *"As $H_{1}:p\neq p_{0}$, the test is two-tailed and the significance level $\alpha=...\%$ is shared equally: $\alpha/2=...\%$ per tail. Since one-tail $p=...>\alpha/2$ (or two-tail $p=...>\alpha$), fail to reject $H_{0}$."*

**Type I in context:**

> *"A Type I error here would be to conclude [e.g. the coin is biased / the training is effective / the spinner is biased] when in fact $p$ is still $p_{0}=...$ ( $H_{0}$ is true). $P(\text{Type I})=P(X\in\text{critical region}\mid H_{0})=...$."*

**Type II in context:**

> *"A Type II error here would be to conclude [e.g. no difference / coin is fair / $p$ has not changed] when in fact the true $p$ is $p_{1}=...$ ( $H_{0}$ is false). $P(\text{Type II})=P(X\notin\text{critical region}\mid p=p_{1})=...$. Without a specified alternative $p_{1}$ only the definition can be stated."*

**Conclusion wording (MANDATORY — always in context, always with level):**

> *"There is (in)sufficient evidence at the $\alpha\%$ significance level to support the claim that [the mean/proportion has increased/decreased/changed]."*
> *Never: " $H_{0}$ is proved true/false" or "the claim is definitely true."*

---

# Practice Questions + Full Solutions

### Q1 — Past-paper style — Direct binomial one-tailed [9709/72/Q4 Nov 2012 Lola + 9709/72/Q6 June 2011 Jeevan — cereal/coin mix]

> **Question:** Lola checks free gifts: manufacturer claims $p=0.25$. She tests $n=20$ at $5\%$ for $p<0.25$. (a) Find critical region and $P(\text{Type I})$. (b) She finds $X=2$. What conclusion? (c) Jeevan tests a die ($n=10$, $p_{0}=1/6$, $H_{1}:p>1/6$, critical region $X\ge4$): find $P(\text{Type I})$ and explain Type II; if true $p=1/2$ find $P(\text{Type II})$.

**Solution (a)(b) — Lola:**

$$X\sim B(20,0.25)\text{ under }H_{0},\;H_{0}:p=0.25,\;H_{1}:p<0.25,\;\alpha=0.05$$

$$P(X\le1)=0.003171+0.021141=0.02431$$

$$P(X\le2)=0.02431+0.06695=0.09126$$

$$P(X\le1)=2.43\%<5\%,\;P(X\le2)=9.13\%>5\%$$

$$\text{Critical region }X\le1\;(C=\{0,1\})$$

$$P(\text{Type I})=P(X\le1\mid p=0.25)=0.0243$$

$$P(\text{Type I})=2.43\%$$

$$x_{\text{obs}}=2\notin C,\;P(X\le2)=9.13\%>5\%$$

$$\text{Fail to reject }H_{0}\text{ at }5\%$$

$$\text{Insufficient evidence at }5\%\text{ that }p<0.25;\;2\text{ gifts in }20\text{ not significant}$$

**Solution (c) — Jeevan:**

$$X\sim B(10,\tfrac16)\text{ under }H_{0},\;C=\{X\ge4\}$$

$$P(X\ge4)=1-P(X\le3)$$

$$P(X\le3)=0.1550+0.2907+0.2907+0.1550\text{ (from earlier pattern for }n=10,p=1/6)$$

$$P(X\le3)=0.9303\text{ (exact: }P(X\ge4)=0.0697)$$

$$P(\text{Type I})=P(X\ge4\mid p=1/6)=0.0697=6.97\%$$

$$\text{Type I: Conclude die biased towards six when it is actually fair }(p=1/6)$$

$$\text{Type II: Conclude die is NOT biased (accept }H_{0}\text{) when it IS biased }(p>1/6)$$

$$\text{True }p_{1}=0.5:\;P(\text{Type II})=P(X\le3\mid B(10,0.5))$$

$$P(X\le3\mid p=0.5)=\sum_{r=0}^{3}\binom{10}{r}0.5^{10}=\frac{1+10+45+120}{1024}=\frac{176}{1024}$$

$$P(\text{Type II})=0.1719=17.2\%$$

*Past Paper Refs: 9709/72/Q4 Nov 2012 Lola (free gifts $B(20,0.25)$); 9709/72/Q6 June 2011 Jeevan (die $B(10,1/6)$, $p=1/2$ alternative).*

---

### Q2 — Direct binomial lower tail [9709/73/Q6 June 2014 — Max's digits (25 digits, 1 is a 5)]

> **Question:** Machine digits $1$–$5$ equally likely, so $p=0.2$ for a $5$. Max claims $p<0.2$. He generates $n=25$ digits and gets exactly $1$ five. Test at $2.5\%$.

**Solution:**

$$X\sim B(25,0.2)\text{ under }H_{0},\;H_{0}:p=0.2,\;H_{1}:p<0.2,\;\alpha=0.025$$

$$P(X\le1)=P(X=0)+P(X=1)$$

$$P(X=0)=0.8^{25}=0.00378$$

$$P(X=1)=25\times0.2\times0.8^{24}=25\times0.2\times0.00472=0.02361$$

$$P(X\le1)=0.00378+0.02361$$

$$P(X\le1)=0.02739$$

$$P(X\le1)=2.74\%>2.5\%$$

$$\text{Fail to reject }H_{0}\text{ at }2.5\%$$

$$\text{Insufficient evidence digit }5\text{ appears less often than it should}$$

$$\text{Critical region: }P(X=0)=0.378\%<2.5\%\text{ so }X=0\text{ is critical; }X=1\text{ already }2.74\%>2.5\%\Rightarrow C=\{0\}$$

*Past Paper Ref: 9709/73/Q6 June 2014 M8 (Max, 25 digits, $2.5\%$ test — verify $P(X\le1)=2.74\%>2.5\%$). 1000 digits part would use normal approx.*

---

### Q3 — Normal approximation one-tailed [Coursebook Exercise 1A Q3 — sheep + Exercise 1A Q4 — 9 flips vs 180 flips]

> **Question:** (a) $X\sim B(80,0.30)$, observed $19$, test $H_{1}:p<0.30$ at $10\%$ via normal approx. (b) Coin $p=0.5$: Dan flips $9$ times ($7$ tails) test at $5\%$ exact; then $180$ times ($102$ tails) via normal approx — compare conclusions.

**Solution (a):** *(as Part 3 Example 3a — summarised)*

$$X\sim B(80,0.3)\approx Y\sim N(24,16.8),\;z=(19.5-24)/4.0988=-1.098,\;p\approx0.136>0.10$$

$$\text{Fail to reject at }10\%$$

**Solution (b) — 9 flips exact:**

$$X\sim B(9,0.5),\;P(X\ge7)=\binom{9}{7}0.5^{9}+\binom{9}{8}0.5^{9}+0.5^{9}$$

$$P(X=7)=36\times0.0019531=0.07031$$

$$P(X=8)=9\times0.0019531=0.01758$$

$$P(X=9)=0.0019531$$

$$P(X\ge7)=0.07031+0.01758+0.00195$$

$$P(X\ge7)=0.08984$$

$$P(X\ge7)=8.98\%>5\%$$

$$\text{Fail to reject at }5\%\;(9\text{ flips not significant)}$$

**Solution (b) — 180 flips approx:** *(as Part 3 Example 3b)*

$$X\approx Y\sim N(90,45),\;z=(101.5-90)/6.708=1.714,\;p\approx4.3\%<5\%$$

$$\text{Reject at }5\%\;(180\text{ flips significant)}$$

*Lesson: same tail proportion ($77.8\%$ vs $56.7\%$), but $n=180$ has power; $n=9$ does not.*

---

### Q4 — Two-tailed tests [Coursebook Exercises 1B Q1/Q2 — Xavier + Zizou + 1B Q5 Ginny]

> **Question:** (a) $X\sim B(20,0.25)$, $X=2$, test $H_{1}:p\neq0.25$ at $10\%$ two-tailed. (b) $X\sim B(15,0.40)$, $X=2$, test two-tailed $p\neq0.40$ at $5\%$ (compare with one-tailed $p<0.40$ at $5\%$). (c) Bag of $20$ marbles, $p_{0}=0.30$ red, Ginny finds $3$ red: test $p\neq0.30$ at $10\%$ two-tailed; find critical values.

**Solution (a):**

$$X\sim B(20,0.25),\;P(X\le2)=0.09126,\;\alpha/2=0.05$$

$$0.09126>0.05$$

$$\text{Fail to reject }H_{0}\text{ at }10\%\text{ two-tailed}$$

$$\text{Insufficient evidence proportion }\neq0.25$$

$$\text{(One-tailed }p<0.25\text{ would reject at }10\%\text{ since }0.091<0.10)$$

**Solution (b):**

$$X\sim B(15,0.40),\;H_{0}:p=0.40$$

$$P(X\le2)=0.02711\;(=0.00047+0.00470+0.02194\text{ from earlier})$$

$$P(X\le2)=2.71\%$$

$$\text{One-tailed }H_{1}:p<0.40,\;\alpha=5\%:\;2.71\%<5\%\Rightarrow\text{ reject}$$

$$\text{Two-tailed }H_{1}:p\neq0.40,\;\alpha/2=2.5\%:\;2.71\%>2.5\%\Rightarrow\text{ fail to reject}$$

$$\text{Same data flips decision between one- and two-tailed at }5\%$$

**Solution (c):**

$$X\sim B(20,0.30),\;P(X\le2)=0.03548$$

$$P(X\le2)=3.55\%<5\%\;(\alpha/2=5\%)$$

$$P(X\le3)=0.03548+0.07160=0.10708>5\%$$

$$\text{Lower critical }X\le2$$

$$P(X\ge10)=1-P(X\le9)$$

$$P(X\ge10)=0.03082<5\%$$

$$P(X\ge9)=0.03082+0.06537=0.09618>5\%$$

$$\text{Upper critical }X\ge10$$

$$\text{Two-tailed }10\%:\;C=\{X\le2\}\cup\{X\ge10\},\;x_{\text{obs}}=3\notin C\Rightarrow\text{ fail to reject}$$

*Past Paper Ref: Coursebook 1B Q1 ($20,25\%,X=2$), Q2 ($15,40\%,X=2$), Q5 Ginny ($20,30\%$).*

---

### Q5 — Normal approximation + critical value [9709/73/Q6 June 2014 — 1000 digits + 9709/71/Q2 Nov 2011 — Ashok's 100 MCQs]

> **Question:** (a) 8-sided dice? No — Ashok: $100$ MCQs, $5$ options, guessing $p=0.2$. He gets $27$ correct. Test at $5\%$ whether he does better than guessing ($H_{1}:p>0.2$) via normal approx. Find critical value.

**Solution:**

$$X\sim B(100,0.2)\text{ under }H_{0},\;H_{0}:p=0.2,\;H_{1}:p>0.2,\;\alpha=0.05$$

$$np=20>5,\;nq=80>5$$

$$X\approx Y\sim N(20,\;16),\;\sigma=4$$

$$x_{\text{obs}}=27,\;p=P(X\ge27)\approx P(Y>26.5)$$

$$z=\frac{26.5-20}{4}=\frac{6.5}{4}$$

$$z=1.625$$

$$\Phi(1.625)\approx0.9480\text{ (tables: }\Phi(1.62)=0.9474,\;\Phi(1.63)=0.9484)$$

$$p\approx1-0.9480=0.0520$$

$$p\approx5.2\%>5\%$$

$$\text{Fail to reject }H_{0}\text{ at }5\%$$

$$\text{Insufficient evidence Ashok does better than guessing (borderline)}$$

$$\text{Critical value: }1-\Phi((c-0.5-20)/4)=0.05\Rightarrow(c-0.5-20)/4=1.645$$

$$c-0.5=20+6.58$$

$$c=27.08$$

$$P(Y>27.5):z=1.875,\Phi=0.9696,p=0.030<5\%\Rightarrow X\ge28\text{ critical}$$

$$P(Y>26.5):p=0.052>5\%$$

$$\text{Critical region }X\ge28\text{ (27 not significant)}$$

*Past Paper Ref: 9709/71/Q2 Nov 2011 (Ashok, 100 MCQs, 27 correct — verify borderline $5.2\%>5\%$, critical $28$).*

**Digging deeper — 1000 digits (Max's follow-up):**

$$X\sim B(1000,0.2),\;np=200>5,\;nq=800>5$$

$$X\approx Y\sim N(200,\;160),\;\sigma=12.649$$

$$\text{No need to compute for }180\text{ — state: }X\sim B(1000,0.2)\approx N(200,160)\text{ with }z=(179.5-200)/12.65=-1.62\text{ etc.}$$

*9709/73/Q6 June 2014 (iii): Max $1000$ digits, $180$ fives → state approx $N(200,160)$; Type II defined as "conclude digit $5$ not rarer when it is rarer".*

---

### Q6 — Mixed and exam-style [Coursebook Exercise 1B Q4 Magnus + 9709 Paper 72 Mixed-Handedness]

> **Question:** (a) Magnus: $12\%$ spell onomatopoeia, $n=180$, $13$ correct. $13$ is the critical value — find $\alpha$ for one-tailed $H_{1}:p<0.12$ using normal approx, and state Magnus's conclusion. (b) $1\%$ mixed-handed, $n=600$, $11$ mixed-handed, test $p\neq0.01$ at $4\%$.

**Solution (a):**

$$X\sim B(180,0.12),\;H_{0}:p=0.12,\;H_{1}:p<0.12$$

$$np=21.6>5,\;nq=158.4>5$$

$$X\approx Y\sim N(21.6,\;19.008),\;\sigma=4.360$$

$$\text{Critical }X=13\Rightarrow P(X\le13)\approx P(Y<13.5)$$

$$z=\frac{13.5-21.6}{4.360}=\frac{-8.1}{4.360}$$

$$z=-1.858$$

$$\Phi(-1.858)=0.0315$$

$$P\approx3.15\%$$

$$\alpha\approx3.2\%\;(3.15\%)$$

$$x_{\text{obs}}=13\text{ is on boundary: }13\le13\Rightarrow\text{ reject at }3.15\%$$

$$\text{At nominal }5\%\text{ Magnus rejects; at }2\%\text{ fails — }3.15\%\text{ is the exact threshold}$$

**Solution (b):**

$$X\sim B(600,0.01)\text{ under }H_{0},\;H_{0}:p=0.01,\;H_{1}:p\neq0.01,\;\alpha=0.04\text{ two-tailed}$$

$$np=6>5,\;nq=594>5\text{ (borderline — Poisson }Po(6)\text{ also valid, but normal ok)}$$

$$X\approx Y\sim N(6,\;5.94),\;\sigma=2.438$$

$$x_{\text{obs}}=11>6\Rightarrow\text{ upper tail}$$

$$p_{\text{one tail}}=P(X\ge11)\approx P(Y>10.5)$$

$$z=\frac{10.5-6}{2.438}=1.846$$

$$\Phi(1.846)\approx0.9676$$

$$p_{\text{one tail}}\approx0.0324$$

$$\alpha/2=0.02$$

$$0.0324>0.02$$

$$p_{\text{two-tailed}}=0.0648>0.04$$

$$\text{Fail to reject }H_{0}\text{ at }4\%\text{ two-tailed}$$

*Coursebook 1B Q4 (Magnus, $13$ critical → $\approx3.1\%$); 1B Q6 Amie ($600,1\%,11$ mixed-handed at $4\%$ — exact $Po(6)$ alternative: $P(X\ge11)=4.28\%>4\%$ one-tail? Two-tailed $>2\%$ → same fail).*

---

### Q7 — Type I and Type II with binomial [9709/72/Q4 Nov 2012 Lola + 9709/72/Q6 June 2011 Jeevan synthesis — Type I/II]

> **Question:** (a) Lola's test $n=20,p_{0}=0.25,C=\{X\le1\}$ at $5\%$. Find $P(\text{Type I})$ (already done). If true $p_{1}=0.10$, find $P(\text{Type II})$. (b) Jeevan's die $n=10,p_{0}=1/6,C=\{X\ge4\}$, $P(\text{Type I})=6.97\%$. If true $p_{1}=0.25$, find $P(\text{Type II})$.

**Solution (a):**

$$C=\{X\le1\},\;P(\text{Type I})=0.0243$$

$$P(\text{Type II})=P(X\notin C\mid p=0.10)=P(X\ge2\mid B(20,0.10))$$

$$P(X\le1\mid p=0.10)=0.9^{20}+20\times0.1\times0.9^{19}$$

$$P(X\le1\mid0.10)=0.12158+0.27017=0.39175$$

$$P(\text{Type II})=1-0.39175$$

$$P(\text{Type II})=0.60825=60.8\%$$

**Solution (b):**

$$C=\{X\ge4\},\;P(\text{Type II})=P(X\le3\mid B(10,0.25))$$

$$P(X\le3\mid0.25)=0.05631+0.18771+0.28157+0.25028$$

$$P(X\le3)=0.77587$$

$$P(\text{Type II})=0.7759=77.6\%$$

*Insight: Type II huge ($60$–$77\%$) because $n$ small and effect size modest — power only $22$–$39\%$.*

---

### Q8 — Type I / II with normal distribution [9709/71/Q1 June 2009 Jakarta rings — normal mean test]

> **Question:** European mean ring diameter $18.5$ mm. Jakarta claim: smaller. Sample $n=20$, $\bar{x}=18.1$, $\sigma=1.1$ known. Test $H_{0}:\mu=18.5$ vs $H_{1}:\mu<18.5$ at $2.5\%$. Find (a) Type I meaning, (b) critical region for $\bar{X}$, (c) decision.

**Solution:**

$$\bar{X}\sim N\left(\mu,\frac{\sigma^{2}}{n}\right),\;\sigma_{\bar X}=\frac{1.1}{\sqrt{20}}=0.24597$$

$$H_{0}:\mu=18.5,\;H_{1}:\mu<18.5,\;\alpha=0.025\text{ one-tailed}$$

$$\text{Critical value }c:\;P(\bar X\le c\mid\mu=18.5)=0.025$$

$$\Phi\left(\frac{c-18.5}{0.24597}\right)=0.025$$

$$\frac{c-18.5}{0.24597}=\Phi^{-1}(0.025)=-1.96$$

$$c=18.5-1.96\times0.24597$$

$$c=18.5-0.4821$$

$$c=18.018$$

$$\text{Critical region }\bar X\le18.02$$

$$\bar x_{\text{obs}}=18.1>18.018$$

$$\text{Fail to reject }H_{0}\text{ at }2.5\%$$

$$\text{Insufficient evidence Jakarta mean }<18.5\text{ (low power with }n=20)$$

$$P(\text{Type I})=P(\bar X\le18.018\mid\mu=18.5)=0.025=2.5\%$$

$$\text{Type I: Conclude Jakarta mean }<18.5\text{ when it is actually }18.5$$

$$P(\text{Type II})\text{ needs true }\mu_{1}<18.5\text{ e.g. }18.0:\;P(\bar X>18.018\mid\mu=18.0)=P\left(Z>\tfrac{18.018-18.0}{0.246}\right)=\Phi(-0.073)=0.529$$

*Past Paper Ref: 9709/71/Q1 June 2009 (Jakarta rings — normal mean test). Also see 9709/73/Q6 June 2014 for distribution statement.*

---

# Quick Reference Card — Hypothesis Testing (9709 S2) — 1 Page Cheat Sheet

**1. The 6-Step Procedure (every question)**

```
1. Define X ~ B(n,p0)  (or N(np,npq) if approximating) under H0
2. State H0: p = p0   vs   H1: p < / > / ≠ p0  (same symbol!)
   Tail from wording:  <  "less/fewer/reduce"
                        >  "more/greater/bias towards"
                        ≠  "different/incorrect/changed"
3. State α and tail  (two-tailed → α/2 per tail)
4. Compute p-value = tail probability under H0
   Lower: P(X ≤ xobs)    Upper: P(X ≥ xobs)    Two: 2× smaller tail
5. Decision:  p ≤ α  (or ≤ α/2) → reject H0
               p >  α  (or >  α/2) → fail to reject H0
6. Conclude: "Sufficient / Insufficient evidence at α% that [context]"
```

**2. Binomial PMF**

$$P(X=r)=\binom{n}{r}p^{r}(1-p)^{n-r}\qquad E=np,\;Var=npq$$

**3. When to Use Normal Approximation**

```
B(n,p) → N(np, npq)  if  np > 5  and  nq > 5  (and n large)
State μ = np,  σ² = npq,  σ = √(npq)
```

**4. Continuity Correction — MANDATORY**

```
P(X ≤ k) → P(Y < k+0.5)     P(X ≥ k) → P(Y > k-0.5)
P(X = k) → P(k-0.5 < Y < k+0.5)    P(a ≤ X ≤ b) → P(a-0.5 < Y < b+0.5)
Standardise:  Z = (Y - np)/√(npq)  →  Φ(z) from tables
```

**5. p-Value vs Critical Region**

```
p-value method:  compute P(tail | H0), compare to α
Critical region: find C = {X ≤c or X ≥c : P∈C | H0 ≤ α}
Both give same decision — show ONE clearly
```

**6. Two-Tailed Rule**

```
H1: p ≠ p0  →  share α: α/2 per tail
Compare one-tail p to α/2,  OR  compare 2×one-tail p to α
E.g. α=5% → per tail 2.5%
```

**7. Type I / Type II**

```
Type I  = reject H0 when H0 true   →  P(Type I)=P(X∈C | H0)= α(actual)
          "False positive"  e.g. say biased when fair
Type II = accept H0 when H0 false  →  P(Type II)=P(X∉C | p=p1)  (needs p1)
          "False negative" e.g. say fair when biased
Power = 1 - P(Type II)
α↓  →  Type I↓ but Type II↑     n↑  →  both ↓
```

**8. Wording Traps**

```
"more than k"   = P(X > k)  = 1 - P(X ≤ k)
"at least k"    = P(X ≥ k)  = 1 - P(X ≤ k-1)   ← includes k
"fewer than k"  = P(X < k)  = P(X ≤ k-1)
"at most k"     = P(X ≤ k)
Include xobs in p-value:  P(X ≥ xobs) not P(X > xobs)
```

**9. Tables**

$$P(Z>z)=1-\Phi(z),\quad \Phi(-z)=1-\Phi(z)$$

$$\Phi^{-1}(0.95)=1.645,\;\Phi^{-1}(0.975)=1.96,\;\Phi^{-1}(0.99)=2.326$$

**10. If Stuck**

```
"n large? p small? np>5?"  → tells you approximation
"Which tail?"  → read H1 direction
"Forgot 0.5?"  → draw bar [k-0.5, k+0.5]
"Two-tailed?"  → halve α
```

> **Exam mantra:** *Define X & H₀/H₁ → check np>5 (±0.5) → correct tail (≤ / ≥ / ≠) → p vs α (or α/2) → sentence with "sufficient/insufficient at α% in context."*

---

*Sources: Cambridge International AS & A Level Mathematics 9709 syllabus (2020–2025); Cambridge Probability & Statistics 2 Coursebook Chapter 1 (Worked Examples 1.1–1.8, Exercises 1A–1C, End-of-chapter Review Exercise 1); past papers 9709/73/Q6 June 2014 (Max digits), 9709/72/Q4 Nov 2012 (Lola free gifts), 9709/72/Q6 June 2011 (Jeevan die), 9709/71/Q2 Nov 2011 (Ashok MCQs), 9709/71/Q1 June 2009 (Jakarta rings), 9709/73/Q6 June 2012 (bulb estimation context). Prerequisite checks: $X\sim B(8,0.1),\,B(15,0.25),\,X\sim N(22,16)$ (coursebook p.2) and $B(80,0.4)\approx N(32,19.2)$ continuity (Probability & Statistics 1 Ch.8).*
