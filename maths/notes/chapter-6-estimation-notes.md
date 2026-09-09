# 📊 Chapter 6: Estimation — 9709 S2

> **Rule → Method Table → Justification → 4 Examples (all via Question) → Watch Out**
>
> **What this chapter is:** using *sample* statistics ($\bar{x}, s^2, \hat{p}$) to infer *population* parameters ($\mu, \sigma^2, p$). You never know $\mu$; you estimate it. Two tools: **hypothesis tests** (is $\mu = \mu_0$?) and **confidence intervals** (where does $\mu$ lie?).
>
> **Syllabus split:** (1) Unbiased estimates  (2) Hypothesis test of mean  (3) CI for mean  (4) CI for proportion  (5) Mixed / traps

---

## How To Use: 5 Steps

| Step | Action | What you do |
|:---:|---|---|
| **1** | **Rule** | Read the boxed formula — LaTeX, exact syllabus form |
| **2** | **Decision Table** | Choose path: known vs unknown $\sigma$, large $n$, mean vs proportion, one- vs two-tail, CI vs test |
| **3** | **Method Table** | Follow `Step | What To Do` — numbered, no skipping |
| **4** | **Justification** | Write the sentence that earns the method mark: $E(\hat{U})=U$, reject/fail wording, CI interpretation |
| **5** | **Watch Out** | Check the trap before moving on |

> Every example is a **Question** with full `\$\$` working. Examiner wording is reproduced verbatim in decision/justification banks.

---

## PART 1: Unbiased Estimates — $\bar{x}$ for $\mu$, $s^2$ for $\sigma^2$

### 1.0 Rule

An estimator $\hat{U}$ is **unbiased** for parameter $U$ iff:

$$E(\hat{U}) = U$$

For a random sample $x_1,\dots,x_n$ from a population with mean $\mu$ and variance $\sigma^2$:

$$\text{Unbiased estimate of } \mu \text{ is } \bar{x} = \frac{1}{n}\sum x_i$$

$$\text{Unbiased estimate of } \sigma^2 \text{ is } s^2 = \frac{1}{n-1}\sum (x_i-\bar{x})^2$$

Equivalent computational forms (all identical — pick the one matching your data layout):

$$s^2 = \frac{1}{n-1}\left(\sum x_i^2 - n\bar{x}^2\right) = \frac{1}{n-1}\left(\sum x_i^2 - \frac{(\sum x_i)^2}{n}\right) = \frac{1}{n-1}\sum (x-\bar{x})^2$$

For grouped / frequency data:

$$s^2 = \frac{1}{n-1}\left(\sum f x^2 - \frac{(\sum f x)^2}{n}\right)$$

> **Key identity:** Sample (biased) variance $= \frac{1}{n}\sum(x-\bar{x})^2$ satisfies $E(V)=\frac{n-1}{n}\sigma^2$. Multiplying by $\frac{n}{n-1}$ removes the bias: $s^2 = \frac{n}{n-1}V$.

| Quantity | Symbol | Formula | Unbiased? |
|---|---|---|---|
| Sample mean | $\bar{x}$ | $\frac{\sum x}{n}$ | ✅ Yes, $E(\bar{X})=\mu$ |
| Sample variance (biased) | $V$ | $\frac{1}{n}\sum(x-\bar{x})^2$ | ❌ No, $E(V)=\frac{n-1}{n}\sigma^2$ |
| Unbiased variance estimator | $s^2$ | $\frac{n}{n-1}V$ | ✅ Yes, $E(s^2)=\sigma^2$ |
| Calculator $\sigma_{n-1}$ | $s$ | $\sqrt{s^2}$ | This IS the unbiased one — use `s` or `σ_{n-1}` on Casio |

### 📋 Decision Box — Which variance to use?

| Situation | What the question says | What to compute | Common trap |
|---|---|---|---|
| **"Find the variance"** (no qualifier) and data IS the whole population | "The 30 nests are the population" | Divides by $n$: $\frac{1}{n}(\sum x^2 - (\sum x)^2/n)$ | — |
| **"Unbiased estimate of variance"** / **"Estimate population variance"** from a sample | "Random sample of 30 nests", "estimate" | Divides by $n-1$: $\frac{1}{n-1}(\sum x^2 - (\sum x)^2/n)$ | Dividing by $n$ loses the mark |
| **Grouped frequency** | Table with $f$ | Use $\sum fx$, $\sum fx^2$ in same $n-1$ formula | Forgetting $f$ weights |
| **Calculator** | Any | `MENU → Statistics → σ_{n-1}` gives $s$ directly; `σ_n` gives biased | Mixing them up — label which you used |

### 📋 Justification Box — Unbiased sentence

> **To write:** *"$\bar{x}$ is an unbiased estimate of $\mu$ because $E(\bar{X})=\mu$"* or *" $s^2$ is unbiased for $\sigma^2$ because $E(s^2)=\sigma^2$"*
>
> **Why $n-1$:** $E(V)=\frac{n-1}{n}\sigma^2 \neq \sigma^2$, so $E\left(\frac{n}{n-1}V\right)=\sigma^2$.

### Method Table — Unbiased estimates

| Step | What To Do | Formula / Action |
|:---:|---|---|
| 1 | Identify $n$ | Count data points; for frequency table $n=\sum f$ |
| 2 | Compute $\bar{x}$ | $\bar{x} = \sum x / n$ (or $\sum fx / n$) — this IS the unbiased estimate of $\mu$ |
| 3 | Compute $s^2$ | $s^2 = \frac{1}{n-1}\left(\sum x^2 - \frac{(\sum x)^2}{n}\right)$ — show both sums |
| 4 | If needed, $s$ | $s = \sqrt{s^2}$ — state "unbiased estimate of $\sigma$ is $s$" |
| 5 | Check | $s^2 > V$ always (since $n/(n-1)>1$); if $s^2 < V$ you swapped $n$ and $n-1$ |

---

#### Example 1.1 — Easy — Raw sums (Coursebook Worked Example 6.1)

> **Question:** A conservationist samples 30 Melodious lark nests. The numbers of eggs $m$ satisfy $\sum m = 66$ and $\sum m^2 = 162$. Find unbiased estimates of the population mean and variance.

**Solution:**

$$\bar{m} = \frac{\sum m}{n} = \frac{66}{30} = 2.20$$

This is the unbiased estimate of $\mu$.

$$s^2 = \frac{1}{n-1}\left(\sum m^2 - \frac{(\sum m)^2}{n}\right) = \frac{1}{29}\left(162 - \frac{66^2}{30}\right)$$

$$66^2 = 4356,\quad \frac{4356}{30}=145.2,\quad 162-145.2 = 16.8$$

$$s^2 = \frac{16.8}{29} = 0.579\;(3\text{ s.f.})$$

> **Answer:** $\hat{\mu} = 2.20$, $\hat{\sigma}^2 = 0.579$. If the question had asked for the variance *of the 30 nests as a population* it would be $16.8/30 = 0.560$ — dividing by $n$ not $n-1$. The unbiased estimate is always slightly larger.

**What the examiner wants:** both sums shown, division by $n-1=29$ not $n=30$, and the sentence "$\bar{m}$ is unbiased for $\mu$ since $E(\bar{M})=\mu$".

---

#### Example 1.2 — Medium — Frequency table (Coursebook Worked Example 6.2)

> **Question:** Numbers of tiger cubs in 24 litters: $c=1,2,3,4$ with frequencies $f=2,7,12,3$ (>4 has $f=0$). Find unbiased estimates of mean and variance. [9709/62/M/J/18 adaptation]

**Solution:**

$$n = \sum f = 2+7+12+3 = 24$$

$$\sum fc = 1(2)+2(7)+3(12)+4(3)=2+14+36+12 = 64$$

$$\bar{c} = \frac{64}{24} = \frac{8}{3}=2.67\;(3\text{ s.f.})$$

$$\sum fc^2 = 1^2(2)+2^2(7)+3^2(12)+4^2(3)=2+28+108+48=186$$

$$s^2 = \frac{1}{23}\left(186 - \frac{64^2}{24}\right) = \frac{1}{23}\left(186 - \frac{4096}{24}\right)$$

$$\frac{4096}{24}=170.667,\quad 186-170.667=15.333$$

$$s^2 = \frac{15.333}{23}=0.667\;(3\text{ s.f.}),\qquad s=0.816$$

> **Answer:** $\hat{\mu} = 2.67$, $\hat{\sigma}^2=0.667$. Grouped formula is essential — do not compute variance of $c$ values 1,2,3,4 alone.

**What the examiner wants:** $n=\sum f$ identified, $fc$ and $fc^2$ columns, division by $n-1=23$.

---

#### Example 1.3 — Hard — Large summarised sample linking to later CI (Past paper style: 9709/72/O/N/14 Q4)

> **Question:** For 60 hot drinks, volumes $v$ ml have $\sum v = 17280$, $\sum v^2 = 5\,015\,000$.
> (a) Find unbiased estimates of $\mu$ and $\sigma^2$.
> (b) Hence estimate the standard error of $\bar{V}$.

**Solution:**

$$(a)\quad \bar{v} = \frac{17280}{60}=288.0\text{ ml}$$

$$s^2 = \frac{1}{59}\left(5\,015\,000 - \frac{17280^2}{60}\right)$$

$$17280^2 = 298\,598\,400,\quad \frac{17280^2}{60}=4\,976\,640$$

$$5\,015\,000-4\,976\,640=38\,360,\quad s^2 = \frac{38360}{59}=650.2$$

$$s = \sqrt{650.2}=25.50$$

$$(b)\quad \text{SE}(\bar{V}) = \frac{s}{\sqrt{n}} = \frac{25.50}{\sqrt{60}} = \frac{25.50}{7.746}=3.29\text{ ml}$$

> If this were a 95% CI question, the interval would be $\bar{v} \pm 1.96\times\text{SE} = 288.0 \pm 6.45$.

**What the examiner wants:** $n-1=59$ not 60; SE uses $s$ not $\sigma$; 3 s.f.

---

#### Example 1.4 — Trap — Population vs unbiased (Exam trap — the $n$ vs $n-1$ distinction)

> **Question:** A class of 8 students have heights (cm): 162, 165, 170, 168, 172, 164, 169, 171.
> (i) Find the variance of the heights of *these 8 students*.
> (ii) If these 8 are regarded as a random sample from a larger population, find an unbiased estimate of the population variance.
> Explain why answers differ.

**Solution:**

$$n=8,\quad \sum x =1341,\quad \bar{x} =167.625$$

$$\sum x^2 = 162^2+165^2+170^2+168^2+172^2+164^2+169^2+171^2$$

$$=26244+27225+28900+28224+29584+26896+28561+29241=224\,875$$

$$\sum(x-\bar{x})^2 = \sum x^2 - n\bar{x}^2 =224\,875 - 8(167.625)^2$$

$$167.625^2=28098.14,\quad 8(28098.14)=224785.1,\quad \text{SS}=89.875$$

$$(i)\quad \text{Population of 8: } V = \frac{89.875}{8}=11.23$$

$$(ii)\quad \text{Unbiased estimate: } s^2 = \frac{89.875}{7}=12.84$$

$$E(V)=\tfrac{7}{8}\sigma^2\neq\sigma^2\text{ so }V\text{ is biased; }E(s^2)=\sigma^2\text{ so }s^2\text{ is unbiased.}$$

> $s^2 = \frac{n}{n-1}V = \frac{8}{7}\times 11.23 = 12.84$ — always larger. In an exam, the word **"estimate"** or **"sample"** signals $n-1$; **"these data are the population"** signals $n$.

**What the examiner wants:** two different answers, explicit $n$ vs $n-1$ justification, and the sentence distinguishing biased from unbiased.

#### Example 1.5 — Extra — Unbiased variance: the $n-1$ trap with a small sample (NEW — 9709/62/O/N/19 Q2 style & 9709/71/M/J/22 Q2 adaptation)

> **Question:** A random sample of $n=15$ onion bulbs has masses $x$ g with $\sum x = 187.5$ and $\sum x^2 = 2354.25$.
> (a) Find unbiased estimates of the population mean $\mu$ and population variance $\sigma^2$.
> (b) A candidate calculates the variance as $10.5/15 = 0.700$. Identify the error and give the correct value. Explain why the two values differ.
> [Adapted 9709/62/O/N/19 Q2; 9709/71/M/J/22 Q2]

**Solution:**

$$\bar{x} = \frac{\sum x}{n} = \frac{187.5}{15} = 12.50\text{ g}$$

This is the unbiased estimate of $\mu$ because $E(\bar{X}) = \mu$.

$$\text{SS} = \sum x^2 - \frac{(\sum x)^2}{n} = 2354.25 - \frac{187.5^2}{15}$$

$$187.5^2 = 35156.25,\quad \frac{187.5^2}{15} = 2343.75,\quad \text{SS} = 2354.25 - 2343.75 = 10.50$$

$$(a)\quad s^2 = \frac{\text{SS}}{n-1} = \frac{10.50}{14} = 0.750\;(3\text{ s.f.})$$

$$s = \sqrt{0.750} = 0.866\text{ g}$$

So $\hat{\mu}=12.5$ g, $\hat{\sigma}^2 = 0.750$ g$^2$ (and $\hat{\sigma}=0.866$ g). These are unbiased because $E(\bar{X})=\mu$ and $E(s^2)=\sigma^2$.

$$(b)\quad V = \frac{\text{SS}}{n} = \frac{10.50}{15} = 0.700$$

The candidate divided by $n$ — this is the **biased** sample variance $V$ with $E(V)=\frac{n-1}{n}\sigma^2 = \frac{14}{15}\sigma^2 \neq \sigma^2$. The unbiased estimator must divide by $n-1$:

$$s^2 = \frac{n}{n-1}V = \frac{15}{14}\times 0.700 = 0.750$$

$$E(V)=\tfrac{14}{15}\sigma^2\;,\; E(s^2)=\sigma^2\;.\;\text{ Numerically }s^2>V\text{ always because }n/(n-1)>1.$$

> **Answer:** (a) $\hat{\mu}=12.5$, $\hat{\sigma}^2=0.750$; (b) 0.700 is the biased variance (uses $\div n$); correct unbiased value is $0.750$ ($\div 14$). In the exam the phrase **"estimate the population variance"** signals $\div(n-1)$ — dividing by $n$ loses the accuracy mark.

**What the examiner wants:** both $\sum x$ and $\sum x^2$ shown, explicit $n-1=14$, and the sentence distinguishing $E(s^2)=\sigma^2$ from $E(V)=\frac{14}{15}\sigma^2$. Calculator check: Casio `\sigma_{n-1}=0.866` ($s$), `\sigma_n=0.837` ($\sqrt{V}$) — use the former.

---

> ⭐ **Watch Out! — Part 1**
> - **$n$ vs $n-1$:** "Estimate population variance" $\Rightarrow \div(n-1)$. "Variance of the sample/data" as a self-contained population $\Rightarrow \div n$. One word changes the denominator — circle "estimate" in the question. **Numerically:** $s^2 = \frac{n}{n-1}V$, so $s^2 > V$ always — if your $s^2 < V$ you swapped them.
> - **Calculator:** Casio `σ_n` = biased ($V$), `σ_{n-1}` = unbiased ($s$). Using the wrong one loses the accuracy mark even if method is right. Show the formula to earn method marks if calculator value is wrong.
> - **Frequency tables:** Must use $\sum f x$ and $\sum f x^2$, not $\sum x$. A common error is averaging the distinct values 1,2,3,4 instead of weighting by $f$.
> - **Small $n$ trap:** With $n=15$, the difference between $\div 15$ and $\div 14$ is $\approx 7$% — examiners deliberately pick small $n$ to make the error visible. With $n=60$ the difference is only $1.7$% and harder to spot — still costs the mark.

---

## PART 2: Hypothesis Testing of the Population Mean

### 2.0 Rule

We test $H_0: \mu = \mu_0$ against $H_1: \mu \neq \mu_0$ (two-tail), $\mu > \mu_0$ (upper one-tail), or $\mu < \mu_0$ (lower one-tail).

For sample mean $\bar{x}$ from sample size $n$:

**Known variance $\sigma^2$ (or $n$ small but population normal with known $\sigma$):**

$$z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}},\qquad \bar{X} \sim N\!\left(\mu_0,\frac{\sigma^2}{n}\right)\text{ under }H_0$$

**Unknown variance, large $n$ ($n\ge 30$ approx; CLT applies):**

$$z = \frac{\bar{x} - \mu_0}{s/\sqrt{n}},\qquad s^2 = \frac{1}{n-1}\left(\sum x^2 - \frac{(\sum x)^2}{n}\right)$$

> In either case $z \sim N(0,1)$ approximately (exactly if population normal with known $\sigma$). Compare $|z|$ to critical value $z^*$ or compare $p$-value to $\alpha$.

### 📋 Decision Box — Which test?

| Question gives | $n$ | Distribution assumption | Variance to use | Test statistic | Normal approx justified by |
|---|---|---|---|---|---|
| $\sigma$ known + "normally distributed" | Any $n$ | Population is $N(\mu,\sigma^2)$ | $\sigma$ (given) | $z=\frac{\bar{x}-\mu_0}{\sigma/\sqrt n}$ | Exact (population normal) |
| $\sigma$ known + $n$ large | $n\ge 30$ | Any (CLT) | $\sigma$ (given) | Same $z$ | CLT |
| $\sigma$ unknown + $n$ large | $n\ge 30$ | Any (CLT) | $s$ (unbiased est.) | $z=\frac{\bar{x}-\mu_0}{s/\sqrt n}$ | CLT — this is the common S2 case |
| $\sigma$ unknown + $n$ small | $n<30$ | Must be told "normally distributed" | $s$ | $z\approx\frac{\bar{x}-\mu_0}{s/\sqrt n}$ (syllabus treats as $z$; not $t$) | Assumed normality + large-$n$ approximation is weaker — still use $z$ in 9709 |

> **9709 convention:** There is **no $t$-distribution** in this syllabus. Even with unknown $\sigma$ and moderate $n$, you use the normal $z$ with $s$ replacing $\sigma$ provided $n$ is "large" (≥30). If $n<30$ the question will *give* $\sigma$ or state normality so you use $\sigma$.

### 📋 Decision Box — One-tail vs Two-tail

| Wording in question | $H_1$ | Type | Critical $z^*$ at 5% | At 1% | At 10% |
|---|---|---|---|---|---|
| "has **increased** / is **greater than** / **more than**" | $\mu > \mu_0$ | Upper one-tail | $+1.645$ | $+2.326$ | $+1.282$ |
| "has **decreased** / is **less than** / **fewer than**" | $\mu < \mu_0$ | Lower one-tail | $-1.645$ | $-2.326$ | $-1.282$ |
| "has **changed** / is **different from** / **not equal to** / two-sided" | $\mu \neq \mu_0$ | Two-tail | $\pm 1.96$ | $\pm 2.576$ | $\pm 1.645$ |
| "whether the claim is **valid** / **correct**" (no direction) | $\mu \neq \mu_0$ | Two-tail | $\pm 1.96$ at 5% | — | — |

### 📋 Significance Level Table — When to reject

| Method | Reject $H_0$ when | Fail to reject when | Exact sentence to write |
|---|---|---|---|
| **Critical value** | $\|z\| > z^*$ (two-tail) or $z > z^*$ (upper) or $z < -z^*$ (lower) | Otherwise | ✅ *"Since $|z|=… > z^*=…$, the result is significant at the $\alpha$% level. There is sufficient evidence to reject $H_0$ and conclude [context, e.g. the mean has increased]."* |
| **$p$-value** | $p < \alpha$ | $p \ge \alpha$ | ✅ *" $p = … < \alpha = …$ so reject $H_0$. Sufficient evidence that …"* |
| **Fail** | — | — | ✅ *"Since $|z|=… < z^*$ (or $p=… > \alpha$), there is **insufficient** evidence to reject $H_0$ at the $\alpha$% level. There is no evidence that [context]. We **do not accept** $H_0$, we **fail to reject** it."* |

> **Language that loses marks:** "Accept $H_0$" (never accept — you *fail to reject*), "Prove $H_0$ is true/false" (you only have evidence for/against), "$p=0.04$ therefore significant so $H_1$ is true" (say *sufficient evidence to reject $H_0$*).

### 📋 Method Table — Hypothesis test for mean

| Step | What To Do | Detail |
|:---:|---|---|
| 1 | State hypotheses | $H_0:\mu=\mu_0$, $H_1:\mu > / < / \neq \mu_0$ — define $\mu$ in context |
| 2 | Choose one/two-tail | Use wording table above; state "one-tailed test at $\alpha$%" |
| 3 | Compute $\bar{x}$ and SE | $\bar{x} = \sum x/n$, SE $=\sigma/\sqrt n$ (known) or $s/\sqrt n$ (large sample unknown) |
| 4 | Test statistic | $z = (\bar{x} - \mu_0)/\text{SE}$ — show substitution |
| 5 | Critical value or $p$ | Look up $z^*$ (or compute $p = 1-\Phi(\|z\|)$ etc.) — state value |
| 6 | Decision | Compare; use exact reject/fail sentence from table |
| 7 | Context + assumptions | "Assume random sample and [population normal / $n$ large so CLT applies / $\sigma$ same]" |

---

#### Example 2.1 — Easy — Known variance, one-tail (Coursebook Worked Example 6.3)

> **Question:** Masses of cucumbers are $N(310, 22^2)$ g. A new plant food claims to increase mass. A sample of $n=40$ cucumbers grown with the new food has $\bar{x} = 316$ g. Test at 5% significance whether the food increases mass. Assume $\sigma$ unchanged.

**Solution:**

$$H_0:\mu = 310,\quad H_1:\mu > 310\qquad\text{(one-tailed, "increase")}$$

$$\text{Under }H_0,\ \bar{X} \sim N\!\left(310,\frac{22^2}{40}\right),\quad \text{SE}=\frac{22}{\sqrt{40}}=\frac{22}{6.3249}=3.4785$$

$$z = \frac{316-310}{3.4785}= \frac{6}{3.4785}=1.725$$

$$\text{Critical value at 5% one-tail: } z^* = \Phi^{-1}(0.95)=1.645$$

$$1.725 > 1.645 \implies \text{reject }H_0\text{ at 5% level}$$

$$p\text{-value}=1-\Phi(1.725)=1-0.9577=0.0423 <0.05\text{ confirms}$$

> **Conclusion:** There is sufficient evidence at the 5% level to reject $H_0$ and conclude the plant food increases the mean mass. (Equivalently: significant evidence supporting the producer's claim.)

**Assumptions:** Random sample; population normal with known $\sigma=22$ unchanged.

---

#### Example 2.2 — Medium — Known variance, two-tail (Coursebook Worked Example 6.4 — 9709/72/June/12 style)

> **Question:** Burn times of candles are $N(\mu, 5.7^2)$ min. Manufacturer claims $\mu=250$. A random sample of 10 candles has times: 245, 247, 236, 255, 250, 239, 241, 252, 251, 243. Test at 5% whether the claim is valid. State assumptions.

**Solution:**

$$H_0:\mu=250,\ H_1:\mu\neq250\quad\text{(two-tailed — "whether valid", no direction)}$$

$$\bar{x} = \frac{245+247+236+255+250+239+241+252+251+243}{10}=\frac{2459}{10}=245.9$$

$$\text{SE}=\frac{5.7}{\sqrt{10}}=\frac{5.7}{3.1623}=1.8028$$

$$z = \frac{245.9-250}{1.8028}=\frac{-4.1}{1.8028}=-2.275$$

$$\text{Critical values at 5% two-tail: } \pm\Phi^{-1}(0.975)=\pm1.96$$

$$|z|=2.275 > 1.96 \implies \text{reject }H_0\text{ at 5%}$$

$$p = 2(1-\Phi(2.275))=2(0.0114)=0.0228 <0.05$$

> **Conclusion:** Sufficient evidence at 5% to reject $H_0$; the mean burn time differs from 250 min — doubt the manufacturer's claim. Assumptions: random sample; burn times normally distributed with $\sigma=5.7$; $n$ small but normality given.

---

#### Example 2.3 — Hard — Large sample, unknown variance (Coursebook Worked Example 6.5 — Past paper 9709/73/June/15 Q3 style)

> **Question:** A researcher believes students underestimate 1 minute. 42 students estimate 60 s; summarised times $x$ s have $\sum x =2471$, $\sum x^2 =146801$. Test at 10% if students underestimate. What advice would you give?

**Solution:**

$$H_0:\mu=60,\ H_1:\mu<60\quad\text{(one-tailed lower — "underestimate")}$$

$$\bar{x} = \frac{2471}{42}=58.833$$

$$s^2 = \frac{1}{41}\left(146801-\frac{2471^2}{42}\right)=\frac{1}{41}\left(146801-145367.64\right)=\frac{1433.36}{41}=34.96$$

$$s=\sqrt{34.96}=5.913,\quad \text{SE}=\frac{s}{\sqrt{42}}=\frac{5.913}{6.4807}=0.9124$$

$$z = \frac{58.833-60}{0.9124}=\frac{-1.167}{0.9124}=-1.279$$

Wait — recalculate with coursebook $s^2=34.73$ (rounding): using $s^2=34.73,\ s=5.893,\ \text{SE}=0.9093$:

$$z = \frac{58.833-60}{0.9093}=-1.283$$

$$\text{Critical at 10% one-tail lower: } z^*=-\Phi^{-1}(0.90)=-1.282$$

$$z=-1.283 < -1.282\implies\text{just reject }H_0\text{ at 10% (borderline)}$$

$$p=\Phi(-1.283)=0.0997 <0.10$$

> **Conclusion:** Just sufficient evidence at 10% to reject $H_0$ and support "underestimate". However $z$ is extremely close to the critical value ($-1.283$ vs $-1.282$) — result is borderline. **Advice:** collect more data / repeat with larger $n$ before concluding firmly. (Coursebook advises: "values very close; do more tests".)

**Why $s$:** $n=42$ large, $\sigma$ unknown, CLT justifies $z$ with $s$.

---

#### Example 2.4 — Trap — One vs two tail changes the verdict (Classic exam trap)

> **Question:** A machine dispenses pesto with mean 380 g, variance $6.4$ ($ \sigma =2.53$ g). A sample of 10 jars has mean 378.7 g. The weekly check is whether the mean has **reduced**. Test at 5%:
> (a) correctly as a one-tailed test.
> (b) Show what happens if you mistakenly use a two-tailed test. [Adapted 9709/62/Nov/08]

**Solution:**

$$(a)\ H_0:\mu=380,\ H_1:\mu<380\quad\text{one-tail lower (has "reduced")}$$

$$\text{SE}=\frac{\sqrt{6.4}}{\sqrt{10}}=\frac{2.5298}{3.1623}=0.800$$

$$z=\frac{378.7-380}{0.800}=\frac{-1.3}{0.800}=-1.625$$

$$\text{Critical one-tail 5%: }-1.645.\quad -1.625 > -1.645$$

> **Fail to reject** $H_0$ at 5% (one-tail). Insufficient evidence that mean has reduced. $p=\Phi(-1.625)=0.0521>0.05$.

$$(b)\ \text{If two-tailed: } H_1:\mu\neq380,\quad z^*=\pm1.96$$

$$|z|=1.625 <1.96\implies\text{also fail to reject — but for the wrong reason.}$$

> **Trap illustration reversed:** If $\bar{x}$ had been 378.3, $z=-2.125$: one-tail rejects ($-2.125<-1.645$) but two-tail also just rejects ($2.125>1.96$) — still same verdict. To see the trap clearly, suppose $\bar{x}=378.5,\ z=-1.875$: one-tail **rejects** ($-1.875<-1.645$) but two-tail **fails** ($1.875<1.96$). **Choosing the wrong tail can flip the conclusion.** Always let the *wording* ("has reduced" = one-tail) decide, not the data.

**What the examiner wants:** explicit $H_1$ with direction, correct $z^*$ matched to tail, and the sentence distinguishing "fail to reject" from "accept".

> ⭐ **Watch Out! — Part 2**
> - **Tail choice must be made BEFORE seeing data.** Seeing $\bar{x} < \mu_0$ and then choosing a lower-tail test is cheating. The question wording decides: "increase/decrease" = one-tail, "different/changed/valid" = two-tail.
> - **$s$ vs $\sigma$:** If the question *gives* $\sigma$ (or $\sigma^2$), use it even if you can compute $s$. If it does *not* give $\sigma$ and $n$ is large, compute $s$. Using $s$ when $\sigma$ is given loses the method mark.
> - **Never "accept $H_0$":** The correct phrase is *"fail to reject $H_0$"* or *"insufficient evidence to reject $H_0$"*.
> - **$n$ small + $\sigma$ unknown:** In 9709, if $n<30$ and $\sigma$ unknown, the question will be about a CI not a test, or will state normality and expect you to still use $z$ with $s$ as an approximation. Do not invent a $t$-test.

---

## PART 3: Confidence Intervals for the Population Mean

### 3.0 Rule

A $100(1-\alpha)$% confidence interval for $\mu$ is:

**Known variance $\sigma^2$:**

$$\bar{x} \pm z^*\frac{\sigma}{\sqrt n}$$

**Large sample, unknown variance (use $s^2$):**

$$\bar{x} \pm z^*\frac{s}{\sqrt n},\qquad s^2=\frac{1}{n-1}\left(\sum x^2-\frac{(\sum x)^2}{n}\right)$$

where $z^* = \Phi^{-1}(1-\alpha/2)$:

| Confidence level | $1-\alpha$ | $\alpha$ | $z^*$ | Use |
|---|---|---|---|---|
| 90% | 0.90 | 0.10 | $1.645$ | $\Phi^{-1}(0.95)$ |
| 95% | 0.95 | 0.05 | $1.960$ | $\Phi^{-1}(0.975)$ |
| 98% | 0.98 | 0.02 | $2.326$ | $\Phi^{-1}(0.99)$ |
| 99% | 0.99 | 0.01 | $2.576$ | $\Phi^{-1}(0.995)$ |
| 99.8% | 0.998 | 0.002 | $3.090$ | $\Phi^{-1}(0.999)$ |

> **Interpretation (examiners check this wording):** *"We are 95% confident that the true population mean $\mu$ lies in this interval"* or *"If many such intervals were constructed, about 95% would contain the true $\mu$."* **Not:** "95% of the data lie in the interval" (wrong) or "There is a 95% probability $\mu$ is in this *particular* interval once computed" (technically $\mu$ is fixed — the randomness is in the sampling procedure).

### 📋 Decision Box — CI for mean: which $z^*$ and which SE?

| Information | SE | $z^*$ | CI |
|---|---|---|---|
| $\sigma$ given, any $n$ (normal pop.) | $\sigma/\sqrt n$ | From confidence level | $\bar{x} \pm z^*\sigma/\sqrt n$ |
| $\sigma$ unknown, $n\ge 30$ | $s/\sqrt n$ | Same $z^*$ | $\bar{x} \pm z^* s/\sqrt n$ |
| Spec says "large sample" | $s/\sqrt n$ | Same | Always $s$, never $\sigma$ |

### 📋 Decision Box — CI ↔ Hypothesis test link (favourite exam question)

| Situation | CI result | Test conclusion at same $\alpha$ |
|---|---|---|
| $\mu_0$ **inside** CI | $\mu_0 \in (\bar{x} \pm z^*\text{SE})$ | **Fail to reject** $H_0:\mu=\mu_0$ at $\alpha$% (two-tail) |
| $\mu_0$ **outside** CI | $\mu_0 \notin$ CI | **Reject** $H_0$ at $\alpha$% |
| One-tail test vs two-sided CI | CI is two-sided — only directly matches two-tail test | For one-tail at 5%, compare with 90% two-sided CI (5% in one tail each side gives 10% total outside) |

> Example: 95% CI is $(62.9, 82.1)$ and $H_0:\mu=80$. Since $80$ is inside the CI, a two-tail test at 5% fails to reject $H_0$.

### Method Table — CI for mean

| Step | What To Do |
|:---:|---|
| 1 | Compute $\bar{x}$ |
| 2 | Compute SE: $\sigma/\sqrt n$ or $s/\sqrt n$ (state which) |
| 3 | Find $z^*$ from confidence level (1.645 / 1.96 / 2.326 / 2.576) |
| 4 | Margin $= z^*\times\text{SE}$ |
| 5 | CI $= (\bar{x} - \text{margin},\ \bar{x} + \text{margin})$ — 3 s.f. |
| 6 | Interpretation sentence (see Justification Box) |
| 7 | If asked "does this support claim $ \mu = \mu_0$?", check if $\mu_0$ inside CI |

---

#### Example 3.1 — Easy — Known variance, 95% CI (Coursebook Worked Example 6.6)

> **Question:** Pond water organisms per 100 ml are $N(\mu,12^2)$. Six samples give: 56, 102, 48, 74, 88, 67.
> (a) Find a 95% CI for $\mu$.
> (b) Vegetation should be removed if $\mu>80$. Advise Adam. [Coursebook 6.6]

**Solution:**

$$\bar{x} = \frac{56+102+48+74+88+67}{6}=\frac{435}{6}=72.5$$

$$\text{SE}= \frac{\sigma}{\sqrt n}= \frac{12}{\sqrt6}= \frac{12}{2.4495}=4.899$$

$$z^*_{95\%}=1.96$$

$$\text{margin}=1.96\times4.899=9.602$$

$$\text{CI}=72.5\pm9.60=(62.9,\ 82.1)\;(3\text{ s.f.})$$

> **Interpretation:** We are 95% confident the true mean number of organisms per 100 ml lies between 62.9 and 82.1.
>
> **(b)** The value 80 lies inside the CI (just below the upper limit 82.1). So although $\bar{x}=72.5<80$, the CI shows the true mean *could* exceed 80. Advise Adam to remove some vegetation and/or take more samples to narrow the interval.

**Link to test:** A two-tail test of $H_0:\mu=80$ at 5% would fail to reject (80 inside 95% CI).

---

#### Example 3.2 — Medium — 99% CI, small $n$ with known $\sigma$ (Coursebook Worked Example 6.7)

> **Question:** Sweets are labelled 100 g, $\sigma=5$ g. A sample of 10 packets has mean 103.8 g. Find a 99% CI for $\mu$ and comment on whether the machine needs adjustment.

**Solution:**

$$\text{SE}= \frac{5}{\sqrt{10}}=1.5811,\quad z^*_{99\%}=2.576$$

$$\text{margin}=2.576\times1.5811=4.073$$

$$\text{CI}=103.8\pm4.07=(99.7,\ 107.9)$$

> **Interpretation:** 99% confident the true mean lies in (99.7, 107.9) g.
>
> **Comment:** The advertised 100 g lies inside the CI (just above the lower bound 99.7). At 99% confidence we cannot rule out that the true mean is below 100 g — consumers might be getting less than advertised. Machine may need adjustment; a 95% CI $(100.7,106.9)$ would exclude 100 g and give stronger evidence it is over-filling, illustrating how confidence level affects the conclusion.

---

#### Example 3.3 — Hard — Large sample, unknown variance, plus width→$\alpha$ (Coursebook Worked Example 6.8 + Exercise 6C Q5/6 style)

> **Question:** 60 strawberries have $\sum x=972$, $\sum x^2=17304.78$.
> (a) Find a 90% CI for $\mu$.
> (b) An $\alpha$% CI based on this sample has width 3.65 g. Find $\alpha$. [9709/73/June/15 style]

**Solution:**

$$\bar{x} = 972/60=16.20$$

$$s^2=\frac{1}{59}\left(17304.78-\frac{972^2}{60}\right)=\frac{1}{59}(17304.78-15746.4)=\frac{1558.38}{59}=26.413$$

$$s=5.139,\quad \text{SE}=5.139/\sqrt{60}=5.139/7.746=0.6634$$

$$(a)\ z^*_{90\%}=1.645,\ \text{margin}=1.645\times0.6634=1.091$$

$$\text{90% CI}=16.20\pm1.09=(15.1,\ 17.3)$$

$$(b)\ \text{Width}=2z^*\text{SE}=3.65\implies z^*=\frac{3.65}{2\times0.6634}=\frac{3.65}{1.3268}=2.751$$

$$\Phi(2.751)=0.9970\implies 1-\Phi=0.0030\text{ in one tail}$$

$$\text{Two tails }=2(0.0030)=0.0060\implies \alpha = 1-0.0060 = 0.994 = 99.4\%$$

> **Check:** 99% CI would have $z^*=2.576$, width $2(2.576)(0.6634)=3.42$ — so 3.65 is slightly wider, hence $\alpha$ slightly above 99%, consistent with 99.4%.

---

#### Example 3.4 — Trap — CI contains $\mu_0$ so fail to reject (Exam trap — CI vs test consistency)

> **Question:** A doctor tests low-fat burgers; fat per burger is $N(\mu,1.3^2)$ g. A sample of 15 burgers has mean 9.20 g (fictional mean for illustration).
> (a) Compute a 99% CI for $\mu$.
> (b) The manufacturer claims $\mu=8$ g. Use the CI to test this at 1% (two-tail). Explain why CLT was not needed. [9709 Paper 72 Q4 June 2011]

**Solution:**

$$\text{SE}=1.3/\sqrt{15}=1.3/3.873=0.3356,\quad z^*_{99\%}=2.576$$

$$\text{margin}=2.576\times0.3356=0.8645$$

$$(a)\ \text{CI}=9.20\pm0.865=(8.34,\ 10.06)$$

$$(b)\ 8\notin(8.34,10.06)\implies\text{reject }H_0:\mu=8\text{ at 1% (two-tail).}$$

> **Sentence:** "Since 8 lies outside the 99% CI, there is sufficient evidence at the 1% level to reject $H_0$ and conclude the mean differs from 8 g (it appears higher)."

> **CLT not needed:** Population is stated as normally distributed, so $\bar{X}$ is exactly normal for any $n$ — no need for CLT. CLT is needed only when population distribution is unknown/non-normal and $n$ is large.

> **Trap variant:** If the CI had been $(7.5, 9.1)$, then $8\in$ CI $\implies$ fail to reject $H_0$ at 1%. Many candidates incorrectly write "accept $H_0$, so $\mu=8$ is proved" — correct is "insufficient evidence to reject $H_0$".

---

#### Example 3.5 — Extra — 95% vs 99% CI: known $\sigma$ vs unknown $s$ (NEW — 9709/62/M/J/20 Q5 & 9709/71/O/N/18 Q6; 9709/62/O/N/19 Q5 adaptation)

> **Question:** 
> (a) Breaking strengths (N) of cables are $N(\mu, 8.0^2)$. A sample of $n=25$ cables has mean $\bar{x}=72.4$ N. Find 95% and 99% CIs for $\mu$ using the known $\sigma$.
> (b) A second survey measures $n=64$ packets with $\sum x = 4620.8$, $\sum x^2 = 337716.7$. Find a 95% CI for $\mu$ using the unbiased estimate $s$. Compare the margins with (a) and explain why $s$ is used.
> [9709/62/M/J/20 Q5; 9709/71/O/N/18 Q6; 9709/62/O/N/19 Q5]

**Solution:**

$$(a)\ \text{Known }\sigma=8.0,\ n=25,\ \text{SE}=\frac{\sigma}{\sqrt{n}} = \frac{8.0}{\sqrt{25}} = \frac{8.0}{5}=1.600$$

$$z^*_{95\%}=1.96,\quad \text{margin}_{95}=1.96\times1.600 = 3.136$$

$$95\%\ \text{CI}=72.4\pm3.14 = (69.3,\ 75.5)\;(3\text{ s.f.})$$

$$z^*_{99\%}=2.576,\quad \text{margin}_{99}=2.576\times1.600 = 4.122$$

$$99\%\ \text{CI}=72.4\pm4.12 = (68.3,\ 76.5)$$

> 99% interval is $4.12/3.14 = 1.31\times$ wider — higher confidence $\Rightarrow$ wider (less precise). Both use $\sigma$ because population is normal with **given** variance; $n=25$ is small but normality is stated so $\bar{X}\sim N(\mu,\sigma^2/n)$ exactly — CLT not needed.

$$(b)\ n=64,\quad \bar{x}=\frac{4620.8}{64}=72.20$$

$$\text{SS}=\sum x^2-\frac{(\sum x)^2}{n}=337716.7-\frac{4620.8^2}{64}$$

$$4620.8^2=21351790.24,\quad \frac{4620.8^2}{64}=333621.72,\quad \text{SS}=337716.7-333621.72=4094.98$$

$$s^2=\frac{\text{SS}}{n-1}=\frac{4094.98}{63}=64.999\approx65.0,\quad s=\sqrt{65.0}=8.062$$

$$\text{SE}=\frac{s}{\sqrt{n}}=\frac{8.062}{8}=1.0078$$

$$\text{margin}_{95}=1.96\times1.0078=1.975$$

$$95\%\ \text{CI}=72.20\pm1.98=(70.2,\ 74.2)$$

> **Comparison:** Margin in (b) ($1.98$) is smaller than in (a) ($3.14$) because $n$ is larger ($64$ vs $25$), even though $s\approx\sigma$. Width $\propto 1/\sqrt{n}$. Here $s$ is used because $\sigma$ was **not given** and $n=64\ge30$ so CLT justifies $z$ with $s$: $\bar{X}\approx N(\mu,\sigma^2/n)$ and $s^2$ is unbiased for $\sigma^2$. In 9709 there is **no $t$-distribution** — even with unknown variance you use $z^*=1.96$ with $s$.

**What the examiner wants:** (a) $\sigma/\sqrt{n}$ not $s/\sqrt{n}$ when $\sigma$ is given; (b) compute $s^2$ with $\div(n-1)=63$ and then $s/\sqrt{n}$; explicit $z^*=1.96$ and $2.576$; interpretation "We are 95% confident the true mean lies in …".

---

#### Example 3.6 — Extra — Sample size for a prescribed CI width (NEW — 9709/71/M/J/19 Q6 & 9709/62/F/M/22 Q6 adaptation)

> **Question:** A factory wants a 95% CI for the mean diameter $\mu$ of bolts.
> (a) If $\sigma=4.5$ mm is known, how large must $n$ be so that the 95% CI has width at most $3.0$ mm?
> (b) A pilot of $n_0=30$ gives $s=5.2$ mm. Using $s$ as a planning value, find $n$ for a 99% CI of width at most $2.0$ mm.
> (c) Explain the trap if a candidate uses width where margin is required.
> [9709/71/M/J/19 Q6; 9709/62/F/M/22 Q6; 9709/71/O/N/17 Q5]

**Solution:**

$$\text{For mean: }\text{width}=2z^*\text{SE}=2z^*\frac{\sigma}{\sqrt{n}},\quad \text{margin }m=z^*\frac{\sigma}{\sqrt{n}}=\frac{\text{width}}{2}$$

$$\text{Hence } n = \left(\frac{z^*\sigma}{m}\right)^2 = \left(\frac{2z^*\sigma}{w}\right)^2.\ \text{Always round UP to next integer.}$$

$$(a)\ 95\%:\ z^*=1.96,\ \sigma=4.5,\ w=3.0\implies m=1.50$$

$$n = \left(\frac{1.96\times4.5}{1.50}\right)^2 = \left(\frac{8.82}{1.50}\right)^2 = (5.88)^2 = 34.57$$

$$n = 35\text{ (round up)}$$

$$\text{Check: }\text{width}=2(1.96)(4.5/\sqrt{35})=2(1.96)(0.7607)=2.98<3.0\checkmark,\; n=34\text{ gives }3.03>3.0.$$

$$(b)\ 99\%:\ z^*=2.576,\ s=5.2,\ w=2.0\implies m=1.00$$

$$n = \left(\frac{2.576\times5.2}{1.00}\right)^2 = (13.395)^2 = 179.43$$

$$n = 180\text{ (round up)}$$

$$\text{Planning note: this uses pilot }s\approx\sigma;\text{ if }n\text{ is much larger than pilot, CLT guarantee strengthens.}$$

$$(c)\ \text{Trap: width }\neq\text{ margin. If you set }z^*\sigma/\sqrt{n}=w\text{ instead of }w/2,\text{ you get }n\text{ too small by factor }4:$$

$$n_{\text{wrong}} = \left(\frac{1.96\times4.5}{3.0}\right)^2 = (2.94)^2 = 8.64\to9\text{ — far too small, gives width }5.96\approx2w.$$

> **Exam tip:** "Within $\pm1.5$ mm" $\Rightarrow$ margin $1.5$; "width $3.0$ mm" $\Rightarrow$ margin $1.5$. Underline the word. For proportions the same formula holds with $\sigma\to\sqrt{\hat{p}(1-\hat{p})}$: $n=(z^*/m)^2\hat{p}(1-\hat{p})$ — see Part 4, Example 4.4.

**What the examiner wants:** $w=2m$ halved before substitution, correct $z^*$ matched to confidence level, final $n$ rounded **up** (not to nearest), and check that width $\propto 1/\sqrt{n}$ so halving width needs $4\times n$.

---

> ⭐ **Watch Out! — Part 3**
> - **$z^*$ for CI vs $z^*$ for test:** 95% CI uses $1.96$ (two-sided, 2.5% each tail). A one-tail test at 5% uses $1.645$ — do not mix them. A 95% CI corresponds to a two-tail test at 5%, not a one-tail test at 5%.
> - **Wider $\Rightarrow$ less precise:** 99% CI is wider than 95% CI (more confident but less precise). Some candidates think "higher confidence = narrower" — opposite.
> - **Width $\propto 1/\sqrt n$:** Doubling $n$ does *not* halve the width; it divides by $\sqrt2$. To halve the width you need $4\times$ the sample size.
> - **Interpretation mark:** "95% of data in interval" = 0/1. Required: "95% of intervals constructed this way contain the true mean" or "We are 95% confident the true mean lies in…"

---

## PART 4: Confidence Intervals for the Population Proportion

### 4.0 Rule

For a large random sample of size $n$, with sample proportion $\hat{p} = r/n$:

$$\hat{p} \text{ is unbiased for } p,\quad \hat{p} \approx N\!\left(p,\frac{p(1-p)}{n}\right)\approx N\!\left(\hat{p},\frac{\hat{p}(1-\hat{p})}{n}\right)$$

An approximate $100(1-\alpha)$% CI for $p$ is:

$$\hat{p} \pm z^*\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

where $z^*$ is the same table as for means (1.645, 1.96, 2.576…).

> **Conditions:** $n$ large, $n\hat{p} >5$ and $n(1-\hat{p})>5$ (so normal approx to binomial is valid). **No continuity correction** for CI (syllabus explicitly: do not apply it).

### 📋 Decision Box — Proportion CI

| Given | Compute | SE | CI |
|---|---|---|---|
| $r$ successes in $n$ trials | $\hat{p} = r/n$ | $\sqrt{\hat{p}(1-\hat{p})/n}$ | $\hat{p} \pm z^*\text{SE}$ |
| CI is $(a,b)$ and you need $n$ | $\hat{p} = (a+b)/2$, margin $=(b-a)/2$ | margin $=z^*\text{SE}$ | Solve $z^*\sqrt{\hat{p}(1-\hat{p})/n}=$ margin for $n$ or $z^*$ |
| Asked "how large must $n$ be for width $w$?" | Width $=2z^*\sqrt{\hat{p}(1-\hat{p})/n}$ | Rearrange | $n = \left(\frac{2z^*}{w}\right)^2\hat{p}(1-\hat{p})$ (or with margin $m=w/2$: $n=(z^*/m)^2\hat{p}(1-\hat{p})$) |

### 📋 Method Table — CI for proportion

| Step | What To Do |
|:---:|---|
| 1 | $\hat{p} = r/n$ (exact fraction → decimal 3 s.f. at end) |
| 2 | SE $= \sqrt{\hat{p}(1-\hat{p})/n}$ |
| 3 | $z^*$ from confidence level |
| 4 | Margin $=z^*\times\text{SE}$ |
| 5 | CI $= (\hat{p} - \text{margin},\ \hat{p} + \text{margin})$ — truncate to $[0,1]$ if needed |
| 6 | Interpretation + check against threshold (e.g. 0.5 for election, 0.7 for "easy" Sudoku) |
| 7 | State: "We are $\alpha$% confident the true proportion lies in…" |

---

#### Example 4.1 — Easy — 95% CI for proportion (Opinion poll — Sofia/Diego in coursebook)

> **Question:** In a poll of 200 people, 108 say they will vote for Sofia and 92 for Diego.
> (a) Find a 95% CI for the proportion voting for Sofia.
> (b) Can we be confident Sofia will win? [Coursebook §6.4]

**Solution:**

$$\hat{p} = 108/200 = 0.54$$

$$\text{SE}= \sqrt{\frac{0.54(1-0.54)}{200}}=\sqrt{\frac{0.2484}{200}}=\sqrt{0.001242}=0.03525$$

$$z^*_{95\%}=1.96,\ \text{margin}=1.96\times0.03525=0.0691$$

$$\text{CI}=0.54\pm0.069=(0.471,\ 0.609)$$

> **(b)** For Sofia to win, $p>0.5$. The CI straddles 0.5 (lower limit 0.471 < 0.5 < 0.609), so we cannot be 95% confident she will win — the true proportion could be below half. Larger $n$ needed for a narrower interval (see next example).

---

#### Example 4.2 — Medium — 99% CI and threshold crossing (Coursebook Worked Example 6.9)

> **Question:** A Sudoku is "easy" if >70% solve it in <10 min. In a sample of 120 people, 87 solve it in <10 min.
> (a) Find a 99% CI for the true proportion. Classify the Sudoku.
> (b) 200 such 99% CIs are constructed. How many are expected to contain the true $p$? [Coursebook 6.9]

**Solution:**

$$\hat{p} =87/120=0.725$$

$$\text{SE}= \sqrt{\frac{0.725(0.275)}{120}}=\sqrt{\frac{0.199375}{120}}=\sqrt{0.0016615}=0.04077$$

$$z^*_{99\%}=2.576,\ \text{margin}=2.576\times0.04077=0.1050$$

$$\text{CI}=0.725\pm0.105=(0.620,\ 0.830)$$

> **Classify:** Threshold 0.70 lies inside the CI (0.62 < 0.70 < 0.83), so although sample >70%, we cannot be 99% confident it is "easy" — could be "average". At 90% ($z^*=1.645$, margin 0.067, CI 0.658–0.792) it still straddles 0.70 — still ambiguous.

$$(b)\ 99\%\text{ of 200 }=0.99\times200=198\text{ intervals expected to contain true }p.$$

---

#### Example 4.3 — Hard — Inverse: CI given, find $n$ and $\alpha$ (Past paper 9709 Paper 71 Q2 June 2010)

> **Question:** 87 people have high-speed internet. A CI for the true proportion is $0.1129 < p < 0.1771$.
> (i) Find $n$ (and hence $\hat{p}$).
> (ii) This is an $\alpha$% CI. Find $\alpha$. [9709/71/June/10 Q2]

**Solution:**

$$(i)\ \text{Midpoint } \hat{p} = \frac{0.1129+0.1771}{2}= \frac{0.29}{2}=0.145$$

$$\text{Margin}=0.1771-0.145=0.0321$$

But $\hat{p} = r/n =87/n \implies n=87/0.145=600$.

Check: SE $=\sqrt{0.145(0.855)/600}=\sqrt{0.123975/600}=\sqrt{0.00020663}=0.01437$

$$(ii)\ \text{margin}=z^*\text{SE}\implies 0.0321 = z^*(0.01437)\implies z^*=2.233$$

$$\Phi(2.233)=0.9872\implies \text{one-tail }1-\Phi=0.0128,\ \text{two-tail}=0.0256$$

$$\alpha = 1-0.0256 =0.9744 =97.4\%$$

> Common check: 95% margin would be $1.96(0.01437)=0.0282$ (too narrow), 99% margin $2.576(0.01437)=0.0370$ (too wide) — so $\alpha$ between 95% and 99%, consistent with 97.4%.

---

#### Example 4.4 — Trap — Sample size needed for given width (Coursebook Worked Example 6.10 + Past paper trap)

> **Question:** A college wants to be 90% confident that the estimated proportion of students who own a car is within 5% of the true proportion. A pilot suggests $\hat{p} \approx 0.8$ (or worst-case 0.5 if no pilot). How many students must be surveyed?
> (a) Using $\hat{p}=0.8$.
> (b) Using the conservative $\hat{p}=0.5$ (maximises variance).
> (c) A candidate writes: "Width 0.05 so margin 0.05". Identify the error.

**Solution:**

$$90\%:\ z^*=1.645,\ \text{margin}=z^*\sqrt{\hat{p}(1-\hat{p})/n}=0.05$$

$$(a)\ \hat{p}=0.8:\ 1.645\sqrt{0.16/n}=0.05\implies \sqrt{0.16/n}=0.030395$$

$$0.16/n=0.0009239\implies n=0.16/0.0009239=173.1\implies n=174$$

$$(b)\ \hat{p}=0.5:\ 1.645\sqrt{0.25/n}=0.05\implies \sqrt{0.25/n}=0.030395$$

$$0.25/n=0.0009239\implies n=270.6\implies n=271$$

> Conservative answer is larger — if unsure of $p$, use 0.5 to guarantee the width.

$$(c)\ \textbf{Trap: } \text{Width}=2\times\text{margin}. \text{ If "within 5%" means margin }0.05,\text{ correct. If question says "width 0.05" then margin }0.025\text{ and }n\text{ is }4\times\text{ larger. Many candidates halve/do not halve incorrectly.}$$

$$\text{For width }0.05\text{ with }\hat{p}=0.8:\ 2(1.645)\sqrt{0.16/n}=0.05\implies n=\left(\frac{3.29}{0.05}\right)^2(0.16)=693$$

> **Exam tip:** "within 5%" = margin 0.05; "width 10%" = margin 0.05. Underline the word in the exam.

> ⭐ **Watch Out! — Part 4**
> - **$\hat{p}$ vs $p$:** CI uses $\hat{p}$ in the SE ($\sqrt{\hat{p}(1-\hat{p})/n}$), not the unknown $p$. Some candidates try to solve for $p$ inside the SE — wrong; plug in $\hat{p}$.
> - **No continuity correction** for proportion CIs (syllabus says do not apply). For hypothesis tests of binomial counts you would, but not here.
> - **Bounds:** Proportion CI must lie in $[0,1]$. If calculation gives $(-0.02, 0.18)$, truncate to $(0,0.18)$ and note the approximation is poor (conditions $n\hat{p}>5$ may fail).
> - **Width vs margin:** "Width 0.03" = $2z^*\text{SE}=0.03$; "within 0.03" = $z^*\text{SE}=0.03$. Misreading doubles/halves $n$ by factor 4.

---

## PART 5: Mixed / Exam Traps — Choosing the Right Tool

### 5.0 Rule

Every estimation question is one of four types:

| Q type | Key phrase | Formula | $z^*$ source |
|---|---|---|---|
| **Unbiased estimate** | "estimate of population mean/variance" | $\bar{x},\ s^2$ with $n-1$ | — |
| **Test of mean** | "test whether mean has changed/increased" + $\alpha$% | $z=(\bar{x}-\mu_0)/(\sigma/\sqrt n)$ or $s/\sqrt n$ | Significance level $\alpha$ |
| **CI for mean** | "confidence interval for the mean" + % | $\bar{x} \pm z^*(\sigma/\sqrt n$ or $s/\sqrt n)$ | Confidence level |
| **CI for proportion** | "proportion ... confidence interval" | $\hat{p} \pm z^*\sqrt{\hat{p}(1-\hat{p})/n}$ | Confidence level |

### 📋 Master Decision Table — $z$ vs $s$, mean vs proportion, test vs CI

| Step | Question | If YES | If NO |
|:---:|---|---|---|
| 1 | Is it a **proportion** ($r$ out of $n$ successes)? | Go to Part 4: $\hat{p} \pm z^*\sqrt{\hat{p}(1-\hat{p})/n}$ | It's a **mean** — continue |
| 2 | Does question say **"confidence interval"**? | CI for mean: $\bar{x} \pm z^*\text{SE}$ | It's a **test** — continue |
| 3 | Does question give **$\sigma$** (variance known)? | Use $\sigma$ in SE for CI or test | Use $s$ ($n$ must be large, $\ge30$) |
| 4 | Is test **one-tail** ("increase/decrease") or **two-tail** ("change/different")? | One-tail $z^*=1.645$ (5%) | Two-tail $z^*=1.96$ (5%) |
| 5 | Is $n$ **large** ($\ge30$) when $\sigma$ unknown? | CLT justifies normal $z$ | Must be told population is normal |

### 📋 Trap Matrix — The 6 mistakes that cost the most marks

| Trap | Wrong | Right | Cost |
|---|---|---|---|
| **$n$ vs $n-1$** | $s^2$ with $\div n$ | Unbiased $\Rightarrow \div(n-1)$ | 1–2 A marks |
| **$\sigma$ vs $s$** | Compute $s$ when $\sigma$ given | Use given $\sigma$; only compute $s$ when $\sigma$ unknown + large $n$ | M mark |
| **One vs two tail** | Default to two-tail | Let wording decide | Wrong $z^*$, wrong conclusion |
| **CI level vs test level** | 95% CI $z^*=1.645$ | 95% CI $z^*=1.96$; 5% one-tail test $z^*=1.645$ | Interval wrong |
| **Width vs margin** | margin = width | margin = width/2 | $n$ wrong by factor 4 |
| **"Accept $H_0$"** | "Accept $H_0$, so $\mu=\mu_0$" | "Fail to reject $H_0$; insufficient evidence" | Language mark |

### Method Table — Mixed (exam strategy)

| Step | What To Do |
|:---:|---|
| 1 | Read question twice; underline: **sample / population / estimate / test / confidence interval / proportion / mean / increased vs changed** |
| 2 | Write $n$, $\sum x$, $\sum x^2$ or $r,n$ — list what you know |
| 3 | Decide row in Master Decision Table |
| 4 | Write hypotheses (if test) or $z^*$ (if CI) *before* calculating |
| 5 | Calculate SE, then $z$ or CI — show every substitution |
| 6 | Decision: compare to $z^*$ or check if $\mu_0$ inside CI — use exact sentence |
| 7 | Context + assumption: "random sample", "normal pop. or $n$ large so CLT", "$\sigma$ assumed same" |

---

#### Example 5.1 — Easy — Identify the type (Mixed recognition)

> **Question:** For each, state the type and write the correct $z^*$ or formula (no calculation):
> (a) $n=80$, $\sum x=158.14$, $\sum x^2=314.094$, "investigate whether bags are underweight" at 5%.
> (b) Same data, "find a 90% confidence interval for the mean".
> (c) 24 sub-standard out of 120 jeans, "find a 98% CI for the proportion sub-standard".
> (d) Battery lives $n=15$, $\sigma=1.3$ known, "find a 99% CI for $\mu$".

**Solution:**

$$(a)\ \text{Test of mean, }\sigma\text{ unknown, }n=80\text{ large: }H_0:\mu=2,\ H_1:\mu<2\text{ (one-tail lower, "underweight")},\ z^*=-1.645,\ z=(\bar{x}-\mu_0)/(s/\sqrt n)$$

$$(b)\ \text{CI for mean, }s\text{ unknown: }\bar{x}\pm z^*s/\sqrt n,\ z^*_{90\%}=1.645,\ s^2=\tfrac{1}{79}(\sum x^2-(\sum x)^2/80)$$

$$(c)\ \text{CI for proportion: }\hat{p}=24/120=0.20,\ \text{CI}=\hat{p}\pm z^*\sqrt{\hat{p}(1-\hat{p})/n},\ z^*_{98\%}=2.326$$

$$(d)\ \text{CI for mean, }\sigma\text{ known, }n=15\text{ small but normal given: }\bar{x}\pm z^*\sigma/\sqrt n,\ z^*_{99\%}=2.576$$

> **Examiner tip:** Part (a) is one-tail (lower) because "underweight" is directional; a common error is to use two-tail ($z^*=1.96$) and get a different verdict.

---

#### Example 5.2 — Medium — CI contains $\mu_0$ vs outside (9709/73/Q3/Nov/10 style)

> **Question:** Sweets have masses $N(\mu,1.0^2)$ g. A sample of 65 sweets has mean 29.6 g. A manufacturer claims $\mu=30$ g.
> (i) Find a 99% CI for $\mu$.
> (ii) Use it to comment on the claim.
> (iii) Another 99% CI from a different 65 sweets leads to the opposite conclusion. Explain how, assuming $\mu$ unchanged. [9709/73/Nov/10 Q3]

**Solution:**

$$\text{SE}=1.0/\sqrt{65}=1.0/8.0623=0.1240,\quad z^*_{99\%}=2.576$$

$$\text{margin}=2.576\times0.1240=0.3195$$

$$(i)\ \text{CI}=29.6\pm0.32=(29.28,\ 29.92)$$

$$(ii)\ 30\notin(29.28,29.92)\implies\text{reject }H_0:\mu=30\text{ at 1% (two-tail). Sufficient evidence mean differs from 30 g (appears lower).}$$

$$(iii)\ \text{99% of such intervals contain true }\mu,\text{ but 1% do not. The second sample is one of the 1% whose interval fails to contain }\mu\text{ (or contains 30 by chance). This is sampling variability — different random samples give different }\bar{x}\text{ and hence different CIs.}$$

> **Not a contradiction:** CIs are random intervals; $\mu$ is fixed. About 1 in 100 99% CIs will miss $\mu$.

---

#### Example 5.3 — Hard — Large-sample test with summarised data (9709/71/Nov/13 Q3 & 9709/72/Nov/14 style)

> **Question:** A pilot flew 50 weeks; distances $x$ km have $\sum x=143300$, $\sum x^2=410900000$. Past mean was 2850 km. Test at 5% whether mean has changed. [9709/71/Nov/13 Q3]

**Solution:**

$$H_0:\mu=2850,\ H_1:\mu\neq2850\quad\text{(two-tail — "changed")}$$

$$\bar{x} =143300/50=2866$$

$$s^2=\frac{1}{49}\left(410900000-\frac{143300^2}{50}\right)=\frac{1}{49}(410900000-410697800)=\frac{202200}{49}=4126.53$$

$$s=64.24,\ \text{SE}=64.24/\sqrt{50}=64.24/7.071=9.085$$

$$z=\frac{2866-2850}{9.085}=\frac{16}{9.085}=1.761$$

$$z^*_{5\%\text{ two-tail}}=\pm1.96,\quad |z|=1.761<1.96\implies\text{fail to reject }H_0$$

$$p=2(1-\Phi(1.761))=2(0.0392)=0.0784>0.05$$

> **Conclusion:** Insufficient evidence at 5% to reject $H_0$; no evidence mean has changed. $n=50$ large, $\sigma$ unknown, CLT justifies $z$ with $s$. Must state "random sample".

---

#### Example 5.4 — Trap — Choosing $z$ vs $t$ logic, and misreading CI as test (Ultimate trap synthesis)

> **Question:** An exam board states: "We are 95% confident the true mean lies in $(15.1,17.3)$." A student says: "So there is a 95% chance this particular interval contains $\mu$, and 95% of students scored in it, and we used a $t$-distribution because $n=60$."
> Identify all 3 errors and give the correct statements. Then: if this CI was used to test $H_0:\mu=16.0$ vs $H_1:\mu\neq16.0$ at 5%, what is the verdict?

**Solution:**

$$1.\ \text{"95% chance this interval contains }\mu\text{" — Wrong nuance. Correct: "If many intervals were constructed this way, about 95% would contain }\mu\text{." Once computed, the interval either does or does not contain }\mu\text{; the 95% is the long-run procedure, not a probability for the fixed interval. Exam wording: "We are 95% confident the true mean lies in…"}$$

$$2.\ \text{"95% of students scored in it" — Wildly wrong. CI is for }\mu\text{ (the mean), not for individual data. About 95% of *sample means* from repeated samples would lie within }1.96\text{ SE of }\mu\text{, not 95% of raw scores.}$$

$$3.\ \text{"We used }t\text{-distribution" — Wrong for 9709. Syllabus has no }t\text{. With }n=60\text{ large, we use }z\text{ with }s\text{ (CLT). Even with }n\text{ small, if }\sigma\text{ known we use }z\text{ with }\sigma\text{. Never }t\text{ in this exam.}$$

$$\text{Verdict on }H_0:\mu=16.0\text{: }16.0\in(15.1,17.3)\implies\text{fail to reject }H_0\text{ at 5% two-tail. Insufficient evidence mean differs from 16.0.}$$

> If $H_0:\mu=18.0$, then $18.0\notin$ CI $\implies$ reject at 5%.

> ⭐ **Watch Out! — Part 5 (Mixed)**
> - **Always write $H_0/H_1$ first.** It forces you to choose one/two-tail correctly and reminds you what $\mu_0$ is.
> - **"Large sample" in 9709 means $n\ge30$ (rule of thumb); coursebook says CLT usable for $n>50$ always, but for the test/CI with $s$ the threshold is ~30. If $n=40$ and $\sigma$ unknown, you *are* expected to compute $s$ and use $z$.**
> - **CI interpretation loses the easiest mark in the paper.** Memorise: *"We are 95% confident the true (population) mean/proportion lies in this interval"* — must say "true" or "population" and must say "confident" not "probability" for the realised interval.
> - **Link: CI ↔ two-tail test only.** A 95% CI corresponds to a 5% two-tail test. Do not use a 95% CI to make a one-tail test decision without adjusting (one-tail 5% ↔ 90% two-sided CI).

---

## Formula Sheet

### Unbiased Estimates

$$\bar{x} = \frac{\sum x}{n}=\frac{\sum fx}{n}\quad\text{(unbiased for }\mu\text{)},\qquad E(\bar{X})=\mu$$

$$s^2 = \frac{1}{n-1}\sum(x-\bar{x})^2 = \frac{1}{n-1}\left(\sum x^2-n\bar{x}^2\right)=\frac{1}{n-1}\left(\sum x^2-\frac{(\sum x)^2}{n}\right)\quad\text{(unbiased for }\sigma^2\text{)}$$

$$s^2 = \frac{1}{n-1}\left(\sum fx^2-\frac{(\sum fx)^2}{n}\right)\quad\text{(grouped)},\qquad E(s^2)=\sigma^2$$

$$\text{SE}(\bar{X})=\frac{\sigma}{\sqrt n}\ (\sigma\text{ known}),\qquad \widehat{\text{SE}}=\frac{s}{\sqrt n}\ (\sigma\text{ unknown, large }n)$$

### Hypothesis Test for Mean

$$H_0:\mu=\mu_0,\quad H_1:\begin{cases}\mu\neq\mu_0&\text{two-tail}\\\mu>\mu_0&\text{upper one-tail}\\\mu<\mu_0&\text{lower one-tail}\end{cases}$$

$$z = \frac{\bar{x}-\mu_0}{\sigma/\sqrt n}\quad(\sigma\text{ known}),\qquad z = \frac{\bar{x}-\mu_0}{s/\sqrt n}\quad(\sigma\text{ unknown, large }n)$$

$$\text{Reject }H_0\text{ if }|z|>z^*\ (\text{two-tail}),\ z>z^*\ (\text{upper}),\ z<-z^*\ (\text{lower}),\text{ or }p<\alpha$$

### Confidence Intervals

**Mean:**

$$\text{CI}_{\,1-\alpha}(\mu)=\bar{x}\pm z^*\frac{\sigma}{\sqrt n}\quad(\sigma\text{ known}),\qquad \bar{x}\pm z^*\frac{s}{\sqrt n}\quad(\sigma\text{ unknown, large }n)$$

**Proportion (large $n$, approx):**

$$\hat{p} = r/n,\quad \text{CI}_{\,1-\alpha}(p)=\hat{p}\pm z^*\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

### $z^*$ Values (memorise 3, derive the rest)

| Level | 90% | 95% | 98% | 99% | 99.8% |
|---|---|---|---|---|---|
| Two-sided CI / two-tail test | $1.645$ | $1.96$ | $2.326$ | $2.576$ | $3.090$ |
| One-tail test at same $\alpha$ | $1.282$ (10%) | $1.645$ (5%) | $2.054$ (2%) | $2.326$ (1%) | — |

> **How to get any $z^*$:**  For $100(1-\alpha)$% CI, $z^*=\Phi^{-1}(1-\alpha/2)$. For one-tail test at $\alpha$%, $z^*=\Phi^{-1}(1-\alpha)$. Examples: 95% CI $\Phi^{-1}(0.975)=1.96$; 5% upper one-tail $\Phi^{-1}(0.95)=1.645$.

### Sample Size (from CI width)

$$\text{Width}=2z^*\text{SE},\quad \text{margin}=z^*\text{SE}$$

$$\text{Mean: } n=\left(\frac{z^*\sigma}{m}\right)^2\text{ or }\left(\frac{z^*s}{m}\right)^2,\qquad \text{Proportion: } n=\left(\frac{z^*}{m}\right)^2\hat{p}(1-\hat{p})$$

where $m$ is the **margin** (half-width). If given width $w$, $m=w/2$.

---

## Methods Summary TABLE

| Formula | When to use | Type 1: Estimate / Compute | Type 2: Test (reject/fail) | Type 3: Interpret / Link | Past paper ref |
|---|---|---|---|---|---|
| $\bar{x} =\sum x/n$ | Unbiased for $\mu$ | Compute $\bar{x}$ as estimate | — | $E(\bar{X})=\mu$ justification | 9709/72/O/N/14 Q4ii; 9709/71/Nov/13 Q3i |
| $s^2=\frac{1}{n-1}(\sum x^2-(\sum x)^2/n)$ | Population variance unknown, sample data given | Divide by $n-1$, not $n$ | — | Distinguish $V$ (biased) vs $s^2$ (unbiased) | 9709/73/June/15 Q4; Coursebook Ex 6.1 |
| $z=\frac{\bar{x}-\mu_0}{\sigma/\sqrt n}$ | Test mean, $\sigma$ known, population normal | Compute $z$, compare to $z^*$ | Reject if $|z|>z^*$ or $p<\alpha$ | One vs two tail wording | 9709/73/Q6/Nov/15 (parcels $\mu=2.60$); 9709/73/Q6/June/12 (Samir) |
| $z=\frac{\bar{x}-\mu_0}{s/\sqrt n}$ | Test mean, $\sigma$ unknown, $n$ large ($\ge30$) | Compute $s$ first, then $z$ | Same decision rule; CLT justification | Borderline $z\approx z^*$ advice | 9709/71/Nov/13 Q3 (pilot); Coursebook Ex 6.5 ($n=42$) |
| $\bar{x}\pm z^*\sigma/\sqrt n$ | CI for mean, $\sigma$ known | Plug $\sigma$, $z^*$ by level | Check if $\mu_0$ inside CI $\leftrightarrow$ test | "We are $X$% confident true $\mu$ lies in…" | 9709/73/Q4/Nov/16 (batteries); 9709/73/June/12 Q6 (candle) |
| $\bar{x}\pm z^*s/\sqrt n$ | CI for mean, $\sigma$ unknown, large $n$ | Compute $s$, then CI | Width $\to\alpha$ (Ex 6.8b) | Relationship width $\propto 1/\sqrt n$ | 9709/72/Nov/14 Q4 (households food); Cross-topic 5 (pistons) |
| $\hat{p}\pm z^*\sqrt{\hat{p}(1-\hat{p})/n}$ | CI for proportion, large $n$ | $\hat{p}=r/n$, SE as above | $p_0$ inside CI $\leftrightarrow$ fail to reject | Compare CI to threshold (0.5, 0.7…) | 9709/71/June/10 Q2 (internet $0.1129<p<0.1771$); 9709/62/F/M/23 (200 students, 23% cars, 93% CI) |
| $n=(z^*/m)^2\hat{p}(1-\hat{p})$ | Sample size for desired margin $m$ | Solve for $n$ | — | Width vs margin trap; conservative $\hat{p}=0.5$ | Coursebook Ex 6.10 (90% within 5%, $n=173$) |

---

## Justification Bank

Copy these sentences verbatim — they earn M/A marks for interpretation.

| Situation | Sentence to write |
|---|---|
| **Unbiased mean** | "$\bar{x}$ is an unbiased estimate of $\mu$ because $E(\bar{X})=\mu$." |
| **Unbiased variance** | "$s^2=\frac{1}{n-1}\sum(x-\bar{x})^2$ is unbiased for $\sigma^2$ because $E(s^2)=\sigma^2$, whereas $V=\frac1n\sum(x-\bar{x})^2$ has $E(V)=\frac{n-1}{n}\sigma^2\neq\sigma^2$." |
| **Assumptions for test/CI (small $n$, $\sigma$ known)** | "Assume the sample is random and the population is normally distributed with known variance $\sigma^2$ / standard deviation $\sigma$." |
| **Assumptions for large $n$, $\sigma$ unknown** | "Assume the sample is random; $n$ is large so by the Central Limit Theorem $\bar{X}\approx N(\mu,\sigma^2/n)$ and $s^2$ is a good estimate of $\sigma^2$." |
| **CI interpretation (mean)** | "We are 95% confident that the true population mean $\mu$ lies in the interval $(a,b)$. If many such intervals were constructed, about 95% would contain the true $\mu$." |
| **CI interpretation (proportion)** | "We are 99% confident that the true population proportion $p$ lies in $(a,b)$." |
| **CI decision** | "Since $\mu_0=…$ lies [inside/outside] the 95% confidence interval, there is [insufficient/sufficient] evidence at the 5% level (two-tail) to reject $H_0$." |
| **Necessity of CLT** | "CLT was needed because the population distribution is not known to be normal and $n$ is large, so $\bar{X}$ is approximately normal. When the population is already normal, CLT is not needed — $\bar{X}$ is exactly normal." |

## Decision Bank

| Decision | Condition | Exact wording (use this) |
|---|---|---|
| **Reject $H_0$ (critical value)** | $\|z\|>z^*$ (two-tail) or $z>z^*$ (upper) or $z<-z^*$ (lower) | "Since $\|z\|=…>z^*=…$, the result is significant at the $\alpha$% level. There is sufficient evidence to reject $H_0$ and conclude [direction, e.g. the mean has increased / differs from $\mu_0$]." |
| **Reject $H_0$ ($p$-value)** | $p<\alpha$ | "Since $p=…<\alpha=…$, reject $H_0$ at the $\alpha$% level. Sufficient evidence that [context]." |
| **Fail to reject $H_0$** | $\|z\|\le z^*$ or $p\ge\alpha$ | "Since $\|z\|=…<z^*=…$ (or $p=…>\alpha$), the result is not significant at the $\alpha$% level. There is insufficient evidence to reject $H_0$. There is no evidence that [context]. We do not accept $H_0$." |
| **CI contains $\mu_0$** | $\mu_0\in$ CI | "Since $\mu_0$ lies inside the $100(1-\alpha)$% CI, we fail to reject $H_0:\mu=\mu_0$ at the $\alpha$% level (two-tail). The data are consistent with $\mu=\mu_0$." |
| **CI excludes $\mu_0$** | $\mu_0\notin$ CI | "Since $\mu_0$ lies outside the CI, we reject $H_0$ at the $\alpha$% level. Data suggest $\mu\neq\mu_0$." |
| **Type I error** | Reject true $H_0$ | "Probability of Type I error $=\alpha$ (significance level). Occurs when we reject $H_0$ even though it is true." |
| **Type II error** | Fail to reject false $H_0$ | "Type II error: failing to reject $H_0$ when $H_1$ is true. e.g. concluding no increase when there really is one." |

---

## Practice Questions + Full Solutions (6)

### Q1 — Unbiased estimates (9709 style — summarised data)

> **Question:** A random sample of 44 chilli plants has total yield $x$ g with $\sum x =842$, $\sum x^2=16364$. Find unbiased estimates of $\mu$ and $\sigma^2$, and the estimated standard error of $\bar{X}$. [Coursebook Exercise 6C Q3]

**Solution:**

$$\bar{x} =842/44=19.136\approx19.1$$

$$s^2=\frac{1}{43}\left(16364-\frac{842^2}{44}\right)=\frac{1}{43}(16364-16112.82)=\frac{251.18}{43}=5.841$$

$$s=2.417,\quad \text{SE}=s/\sqrt{44}=2.417/6.633=0.3644$$

> Answers: $\hat{\mu}=19.1$ g, $\hat{\sigma}^2=5.84$, $\widehat{\text{SE}}=0.364$.

---

### Q2 — Hypothesis test, known variance, one-tail (Past paper 9709/73/Q6/Nov/15 Q7)

> **Question:** Parcel weights $W\sim N(\mu,0.2^2)$ kg, previously $\mu=2.60$. Suspicion $\mu$ has **increased**. A sample of 75 parcels has mean 2.64 kg. Test at 5%. [9709/73/Nov/15 Q6i]

**Solution:**

$$H_0:\mu=2.60,\ H_1:\mu>2.60\quad\text{one-tail upper}$$

$$\text{SE}=0.2/\sqrt{75}=0.2/8.660=0.023094$$

$$z=(2.64-2.60)/0.023094=0.04/0.023094=1.732$$

$$z^*_{5\%\text{ one-tail}}=1.645,\quad 1.732>1.645\implies\text{reject }H_0$$

$$p=1-\Phi(1.732)=0.0416<0.05$$

> **Conclusion:** Sufficient evidence at 5% that mean weight has increased. Assumptions: random sample, $W$ normal with $\sigma=0.2$ unchanged.

---

### Q3 — Hypothesis test, large sample, unknown variance, two-tail (Past paper 9709/71/Nov/13 Q3)

> **Question:** Weekly food expenditure $x$ dollars for 150 households: $\sum x=19035$, $\sum x^2=4054716$. Past mean was not given — test whether population mean differs from 120 dollars at 5% (fictional $\mu_0$ to illustrate). [Adapted 9709/72/Nov/14 Q4iii]

**Solution:**

$$H_0:\mu=120,\ H_1:\mu\neq120$$

$$\bar{x}=19035/150=126.90$$

$$s^2=\tfrac1{149}(4054716-19035^2/150)=\tfrac1{149}(4054716-2415541.5)=\tfrac{1639174.5}{149}=11001.8$$

$$s=104.89,\ \text{SE}=104.89/\sqrt{150}=104.89/12.247=8.566$$

$$z=(126.9-120)/8.566=6.9/8.566=0.805,\quad z^*=\pm1.96$$

$$|0.805|<1.96\implies\text{fail to reject }H_0\text{ at 5%}$$

> Insufficient evidence mean differs from 120. $n=150$ large, CLT justifies $z$ with $s$.

---

### Q4 — CI for mean, large sample + interpretation (Past paper 9709/72/Nov/14 Q4a style + 9709/73/June/15 Q4)

> **Question:** 60 bags of pet food have $\sum x=117$ kg, $\sum x^2=232.72$ kg$^2$.
> (a) Find unbiased estimates of $\mu$ and $\sigma^2$.
> (b) Find a 98% CI for $\mu$.
> (c) The label says 2.00 kg. Does the CI support that the mean is 2.00 kg? [Coursebook Exercise 6C Q6]

**Solution:**

$$(a)\ \bar{x}=117/60=1.95$$

$$s^2=\tfrac1{59}(232.72-117^2/60)=\tfrac1{59}(232.72-228.15)=\tfrac{4.57}{59}=0.07746$$

$$(b)\ s=0.2783,\ \text{SE}=0.2783/\sqrt{60}=0.2783/7.746=0.03593$$

$$z^*_{98\%}=2.326,\ \text{margin}=2.326(0.03593)=0.08358$$

$$\text{CI}=1.95\pm0.0836=(1.87,\ 2.03)$$

$$(c)\ 2.00\in(1.87,2.03)\implies\text{fail to reject }H_0:\mu=2.00\text{ at 2% (since 98% CI ↔ 2% two-tail). Insufficient evidence mean differs from 2.00 kg.}$$

> Wording: "We are 98% confident the true mean lies in (1.87, 2.03) kg."

---

### Q5 — CI for proportion, inverse $\alpha$ (Past papers 9709/71/June/10 Q2 + 9709/62/F/M/23)

> **Question:** In a survey of 250 students, 92 use a certain app.
> (a) Find a 95% CI for the true proportion.
> (b) If a 98% CI were constructed, would it be wider or narrower? Give the interval.
> (c) How large must $n$ be to be 95% confident that $\hat{p}$ is within 0.03 of $p$? [Coursebook Exercise 6D Q2 + 9709/62/F/M/23 variant]

**Solution:**

$$(a)\ \hat{p}=92/250=0.368$$

$$\text{SE}=\sqrt{0.368(0.632)/250}=\sqrt{0.232576/250}=\sqrt{0.0009303}=0.03050$$

$$z^*_{95\%}=1.96,\ \text{margin}=1.96(0.03050)=0.0598$$

$$\text{CI}=0.368\pm0.060=(0.308,\ 0.428)$$

$$(b)\ z^*_{98\%}=2.326,\ \text{margin}=2.326(0.03050)=0.0709,\ \text{CI}=0.368\pm0.071=(0.297,\ 0.439)$$

> Wider (higher confidence ⇒ wider interval, less precise).

$$(c)\ \text{margin}=0.03=z^*\sqrt{\hat{p}(1-\hat{p})/n}\implies 1.96\sqrt{0.368(0.632)/n}=0.03$$

$$\sqrt{0.232576/n}=0.015306\implies 0.232576/n=0.00023427\implies n=992.6\implies n=993$$

> If no pilot $\hat{p}$ given, conservative $n=(1.96/0.03)^2(0.25)=1067$.

---

### Q6 — Mixed trap: CI vs test consistency + Type I/II context (9709/73/Q7/June/13 + 9709 Paper 71 Q5 Nov 2011)

> **Question:** Weekly profit is $N(\mu,4500^2)$. Historically $\mu=34600$ dollars. After a change, 90 weeks have mean 35400. The question is whether profit has **increased**.
> (a) Test at 5% (one-tail). State assumptions. Was CLT needed?
> (b) State the probability of a Type I error.
> (c) If true $\mu$ is now 36500, find the probability of a Type II error for the test in (a).
> (d) Give a 95% CI for $\mu$ based on the 90 weeks and verify consistency with (a). [9709/73/June/13 Q7]

**Solution:**

$$(a)\ H_0:\mu=34600,\ H_1:\mu>34600\quad\text{one-tail upper}$$

$$\text{SE}=4500/\sqrt{90}=4500/9.4868=474.34$$

$$z=(35400-34600)/474.34=800/474.34=1.686$$

$$z^*_{5\%\text{ one-tail}}=1.645,\quad 1.686>1.645\implies\text{reject }H_0\text{ at 5%}$$

> Assumptions: random sample, weekly profits independent and normally distributed (or $n=90$ large), $\sigma=4500$ unchanged. CLT not strictly needed if normality assumed; but with $n=90$ large, CLT would justify normality of $\bar{X}$ even without — either answer accepted if justified.

$$(b)\ P(\text{Type I})=\alpha=0.05$$

$$(c)\ \text{Rejection threshold for }\bar{X}:\ \bar{x}^*=\mu_0+z^*\text{SE}=34600+1.645(474.34)=34600+780.3=35380.3$$

$$\text{Under true }\mu=36500,\ \bar{X}\sim N(36500,474.34^2)$$

$$P(\text{Type II})=P(\bar{X}<35380.3\mid\mu=36500)=P\left(Z<\frac{35380.3-36500}{474.34}\right)=P(Z<-2.360)$$

$$=\Phi(-2.360)=0.0091=0.91\%$$

> Very small Type II risk here because true mean far above threshold.

$$(d)\ 95\%\text{ CI (two-sided) uses }z^*=1.96:\ \text{margin}=1.96(474.34)=929.7$$

$$\text{CI}=35400\pm929.7=(34470,\ 36330)$$

> Check consistency: A 90% two-sided CI (which matches a 5% one-tail test) uses $z^*=1.645$, margin $780.3$, CI $(34620, 36180)$. Lower bound $34620>34600$ so $34600$ outside 90% CI ⇒ reject one-tail at 5%, consistent with (a). The 95% two-sided CI contains 34600 (34470 < 34600 < 36330), so a 5% two-tail test would fail to reject — illustrating that a one-tail test is more powerful for a directional claim.

> ⭐ **Trap to avoid:** 95% CI $(34470,36330)$ contains 34600, so naive "CI contains $H_0$ so fail to reject" would be wrong for the *one-tail* question. The matching CI for a 5% one-tail test is 90% two-sided (or 95% one-sided). Always match tail to CI level.

---

## Quick Reference Card (1 page — print this)

```
┌─────────────────────────────────────────────────────────────────────┐
│  CHAPTER 6 — ESTIMATION — QUICK REFERENCE                           │
├─────────────────────────────────────────────────────────────────────┤
│  UNBIASED ESTIMATES                                                 │
│   x̄ = Σx/n ,  s² = 1/(n-1)·(Σx²-(Σx)²/n) ,  SE = s/√n  (or σ/√n)    │
│   E(x̄)=μ ,  E(s²)=σ²   •  s² = n/(n-1)·V  (>V always)              │
│   Calculator: use σ_{n-1} (=s), not σ_n                              │
├─────────────────────────────────────────────────────────────────────┤
│  HYPOTHESIS TEST FOR MEAN                                           │
│   H0: μ=μ0  H1: μ≠μ0 (two-tail)  μ>μ0 (upper)  μ<μ0 (lower)          │
│   z = (x̄-μ0)/(σ/√n)  if σ known                                     │
│   z = (x̄-μ0)/(s/√n)  if σ unknown & n≥30 (CLT)                     │
│   Compare |z| to z*  or  p to α                                    │
│   z* (two-tail): 90%1.645  95%1.96  98%2.326  99%2.576  99.8%3.090    │
│   z* (one-tail 5%): upper +1.645  lower -1.645  (1% ±2.326)        │
│   |z|>z* or p<α → REJECT H0  ("sufficient evidence")                │
│   else → FAIL TO REJECT ("insufficient evidence") — never "accept" │
├─────────────────────────────────────────────────────────────────────┤
│  CONFIDENCE INTERVALS                                               │
│   Mean (σ known):    x̄ ± z*·σ/√n                                     │
│   Mean (σ unknown):  x̄ ± z*·s/√n   (n large)                        │
│   Proportion:        p̂ ± z*·√[p̂(1-p̂)/n]  , p̂=r/n  (approx, no CC)  │
│   z* by confidence: 90%1.645  95%1.96  98%2.326  99%2.576              │
│   Interpretation: "We are _% confident true μ/p lies in (a,b)"     │
│   Link: μ0 inside CI → fail to reject H0 (two-tail same α)         │
│         μ0 outside   → reject H0                                    │
├─────────────────────────────────────────────────────────────────────┤
│  DECISION FLOW                                                      │
│   Proportion? → p̂±z*√[p̂(1-p̂)/n]                                     │
│   Mean CI?    → x̄±z*·SE  (σ if given, else s)                       │
│   Mean test?  → z=(x̄-μ0)/SE  → compare to z* (tail by wording)     │
│   "increase/decrease" = one-tail │ "changed/different" = two-tail   │
├─────────────────────────────────────────────────────────────────────┤
│  TRAPS TO CIRCLE                                                    │
│   "estimate" → ÷(n-1)  │  "population is these data" → ÷n           │
│   Given σ → use σ (don't compute s)  │  Width = 2·margin            │
│   Higher confidence → WIDER interval (less precise)                  │
│   n×4 needed to halve width (width ∝ 1/√n)                           │
│   No t-distribution in 9709 S2 — always z                            │
└─────────────────────────────────────────────────────────────────────┘
```

---

> **Past paper refs used (≥8):**
> 9709/62/F/M/23 (200 students, 23% cars, 93% CI proportion) · 9709/71/June/10 Q2 (internet, 0.1129<p<0.1771) · 9709/73/Q4/Nov/16 Q4 (tablet battery, n from significance) · 9709/73/Q6/Nov/15 Q6 (parcels, Type II, 2.60→2.68) · 9709/71/Nov/13 Q3 (pilot distance, n=50) · 9709/72/Nov/14 Q4 (households, food) · 9709/73/June/13 Q7 (profit, Type I/II) · 9709/72/June/11 Q4 (burgers, CLT) · 9709/73/Nov/10 Q3 (sweets, 99% CI 29.28–29.92) · Coursebook Worked Examples 6.1–6.10 + Exercises 6A–6D.

*End of Chapter 6 — Estimation. Next: Cross-topic 2 / Practice Paper.*
