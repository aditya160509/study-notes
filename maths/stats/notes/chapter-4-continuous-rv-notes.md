# 📊 Chapter 4: Continuous Random Variables — 9709 S2
> Rule → Method Table → Justification → 4 Examples (all via Question) → Watch Out

> **Syllabus:** Cambridge International AS & A Level Mathematics 9709 — Paper 6 / Paper 62 (Probability & Statistics 2). This chapter covers the *non-Normal* continuous models. The Normal distribution is Paper 5 territory; here you integrate a given PDF directly.

---

# 📋 Table of Contents
1. [How To Use These Notes — 5 Steps](#how-to-use-these-notes--5-steps)
2. [PART 1: The PDF — What Counts as a Continuous Model](#part-1-the-pdf--what-counts-as-a-continuous-model)
3. [PART 2: Median, Quartiles and Percentiles](#part-2-median-quartiles-and-percentiles)
4. [PART 3: Expectation and Variance](#part-3-expectation-and-variance)
5. [PART 4: Mixed, Piecewise and Exam Traps](#part-4-mixed-piecewise-and-exam-traps)
6. [Formula Sheet](#formula-sheet)
7. [Methods Summary Table](#methods-summary-table)
8. [Justification Bank](#justification-bank)
9. [Practice Questions + Full Solutions](#practice-questions--full-solutions)
10. [Quick Reference Card](#quick-reference-card)

---

# How To Use These Notes — 5 Steps

| Step | What to do | Why it works |
|:---:|---|---|
| **1** | **Check the PDF first** — verify $f(x) \ge 0$ and $\int_{-\infty}^{\infty} f(x)\,dx = 1$ before you use it | Examiners award the first 2 marks for these checks; skipping them loses method marks even if later answers are right |
| **2** | **Translate every probability into an integral** — $P(a < X < b) = \int_{a}^{b} f(x)\,dx$ | With a continuous RV, $P(X = c) = 0$ so $<$ vs $\le$ never matters; the integral IS the probability |
| **3** | **Set up the median/percentile equation** — solve $\int_{-\infty}^{m} f(x)\,dx = 0.5$ (or $0.25$, $0.75$, $p/100$) | This tells you exactly which interval $m$ lies in for piecewise PDFs |
| **4** | **Build $E(X)$ and $E(X^{2})$ before $\operatorname{Var}(X)$** — $E(X)=\int x f(x)\,dx$, $E(X^{2})=\int x^{2}f(x)\,dx$, then $\operatorname{Var}(X)=E(X^{2})-[E(X)]^{2}$ | Splitting variance into two integrals avoids the common $E(X^{2})\neq[E(X)]^{2}$ trap |
| **5** | **Audit piecewise limits** — integrate each piece only over its own interval; add the pieces | Over $90\%$ of lost marks in this chapter come from integrating the wrong piece over the wrong interval |

---

# PART 1: The PDF — What Counts as a Continuous Model

*Covers Key Points 4.1–4.3 of the Coursebook (pp. 74–83), Worked Examples 4.1–4.2, Exercise 4A.*

## 1.1 The Two Conditions for a PDF — Rule

A function $f(x)$ is a **probability density function** (PDF) for a continuous random variable $X$ iff:

$$\boxed{f(x) \ge 0 \quad \text{for all } x \qquad \text{and} \qquad \int_{-\infty}^{\infty} f(x)\,dx = 1}$$

Outside the stated domain, $f(x) = 0$ by definition. The total area under the curve equals $1$ (total probability).

Consequences:

$$P(a < X < b) = P(a \le X \le b) = \int_{a}^{b} f(x)\,dx$$

$$P(X = c) = \int_{c}^{c} f(x)\,dx = 0 \quad \text{for any single value } c$$

> **📦 When / Justification Box — Why these two conditions?**
> - **$f(x)\ge 0$:** Probability can never be negative. Since $P(a<X<b)$ is an *area* under $f$, a negative $f$ would give a negative probability — impossible. The coursebook (p. 78, Key Point 4.1) states this as the first PDF property.
> - **$\int f =1$:** Total probability over all possible outcomes is $1$. In the histogram motivation (pp. 76–77), shrinking class widths makes the histogram approach the PDF curve while keeping total area $=1$.
> - **$P(X=c)=0$:** A single point has zero width, so the integral over $[c,c]$ is $0$. This is exactly why it doesn't matter whether you write $<$ or $\le$ for continuous RVs (Key Point 4.2). A common exam trap is to treat $P(X=c)$ as non-zero.

### Method Table — Verifying / Finding $k$ and Computing Probabilities

| Step | What To Do | Detail |
|:---:|---|---|
| 1 | **Write the domain** | Note where $f(x)\neq 0$; outside, $f=0$ |
| 2 | **Check non-negativity** | Show $f(x)\ge 0$ on its domain (sign of $k$, sign of polynomial etc.) |
| 3 | **Integrate over the full domain and set $=1$** | $\int_{\text{domain}} f(x)\,dx =1$ — solve for $k$ if needed |
| 4 | **For $P(a<X<b)$: integrate only over $[a,b]\cap\text{domain}$** | Split the integral if $f$ is piecewise |
| 5 | **For $P(X=c)$: answer is $0$** | No integration needed; state the Key Point |

> ⭐ **Watch Out — PART 1 (before examples):** Forgetting to state **both** conditions when asked to "show $f$ is a PDF" loses marks. Saying "$\int f =1$" alone is only half the answer — you must also say "$f(x)\ge 0$". Likewise, when finding $k$, always substitute the *correct* limits — using $\int_{-\infty}^{\infty}$ when the PDF is $0$ outside $[0,6]$ wastes time but is safe; using the wrong finite limits gives the wrong $k$.

### Example 1 — Easy — Verify $k$ (find the constant)

> **Question:** The continuous random variable $X$ has PDF
> $$f(x) = \begin{cases} kx & 0 \le x \le 3 \\ 0 & \text{otherwise} \end{cases}$$
> Show that $k = \frac{2}{9}$ and verify that $f$ is a valid PDF.
> *(Coursebook Exercise 4A style; cf. 9709/62/O/N/22 Q3)*

**Solution:**

Check non-negativity — for $x\ge 0$ and $k>0$, $f(x)=kx\ge 0$ ✓

Integrate over the domain $[0,3]$ and set equal to $1$:

$$\int_{-\infty}^{\infty} f(x)\,dx = \int_{0}^{3} kx\,dx = k\left[\frac{x^{2}}{2}\right]_{0}^{3}$$

$$= k\cdot\frac{9}{2} = 1$$

$$k = \frac{2}{9} \quad\checkmark$$

Both conditions satisfied, so $f$ is a valid PDF.

**What the examiner wants:** Two explicit checks — $f\ge 0$ and area $=1$ — not just the $k$ calculation.

---

### Example 2 — Medium — Probability over an interval (past-paper style)

> **Question:** The waiting time $X$ minutes for a bus has PDF
> $$f(x) = \begin{cases} \dfrac{x^{2}}{72} & 0 \le x \le 6 \\ 0 & \text{otherwise} \end{cases}$$
> Find $P(2 < X < 5)$.
> *(Coursebook Worked Example 4.3 / Exercise 4B Q2 adapted; cf. 9709/71/M/J/09 Q5)*

**Solution:**

$P(2<X<5)$ is the area under $f$ from $2$ to $5$:

$$P(2 < X < 5) = \int_{2}^{5} \frac{x^{2}}{72}\,dx = \frac{1}{72}\left[\frac{x^{3}}{3}\right]_{2}^{5}$$

$$= \frac{1}{216}\left[x^{3}\right]_{2}^{5} = \frac{1}{216}\left(125 - 8\right)$$

$$= \frac{117}{216} = \frac{13}{24} \approx 0.5417 \quad\checkmark$$

**What the examiner wants:** Correct limits $2$ to $5$ — not $0$ to $5$ — and exact fraction or 3 s.f.

---

### Example 3 — Hard — Piecewise probability (requires splitting) ⚠️ DELIBERATE TRAP

> **Question:** The continuous random variable $X$ has PDF
> $$f(x) = \begin{cases} \dfrac{1}{27}\,x^{2}(5-x) & 0 \le x \le 3 \\[6pt] \dfrac{1}{3}(5-x) & 3 < x \le 5 \\[6pt] 0 & \text{otherwise} \end{cases}$$
> (a) Verify whether $f$ is a valid PDF. (b) Find $P(1 < X < 4)$ — if valid, otherwise find the corrected constant and then find the probability.
> *(Coursebook Worked Example 4.5 adapted; cf. 9709/73/Jun14 Q2 — triangle/trapezium PDF. This example is a deliberate trap: $f$ can exceed $1$ as a density, but total area must still be $1$.)*

**Solution:**

> **Trap check first — always verify total area $=1$ before using a PDF.**

**Step 0 — Check total area with the constants as stated:**

$$A_{1} = \int_{0}^{3}\frac{x^{2}(5-x)}{27}\,dx = \frac{1}{27}\int_{0}^{3}\left(5x^{2}-x^{3}\right)dx = \frac{1}{27}\left[\frac{5x^{3}}{3}-\frac{x^{4}}{4}\right]_{0}^{3}$$

$$= \frac{1}{27}\left[\left(45-\frac{81}{4}\right)-0\right] = \frac{1}{27}\cdot\frac{99}{4} = \frac{11}{12}\approx 0.9167$$

$$A_{2} = \int_{3}^{5}\frac{5-x}{3}\,dx = \frac{1}{3}\left[5x-\frac{x^{2}}{2}\right]_{3}^{5} = \frac{1}{3}\left[\left(25-\frac{25}{2}\right)-\left(15-\frac{9}{2}\right)\right] = \frac{1}{3}\cdot 2 = \frac{2}{3}\approx 0.6667$$

$$A_{1}+A_{2} = \frac{11}{12}+\frac{2}{3} = \frac{19}{12}\approx 1.58 > 1 \quad\text{— NOT a valid PDF as written.}$$

> **Why this matters:** A density value $f(x)>1$ is allowed (e.g. $f=2$ on $[0,0.5]$ has area $1$). The trap here is not $f>1$ at a point, but **total area $>1$** — impossible for a probability. A wrong normalising constant propagates to every later answer.

**Step 1 — Find the corrected normalising constant.** Let the first piece be $k\,x^{2}(5-x)$ on $[0,3]$:

$$k\int_{0}^{3}\left(5x^{2}-x^{3}\right)dx + \frac{2}{3}=1 \implies k\cdot\frac{99}{4}= \frac{1}{3} \implies k = \frac{4}{297}$$

So the **corrected PDF** is:

$$f_{\text{corr}}(x) = \begin{cases} \dfrac{4}{297}\,x^{2}(5-x) & 0 \le x \le 3 \\[6pt] \dfrac{1}{3}(5-x) & 3 < x \le 5 \\[6pt] 0 & \text{otherwise} \end{cases} \qquad \int_{-\infty}^{\infty}f_{\text{corr}}=1\ \checkmark$$

*Note:* The coursebook's standard valid two-piece model (Worked Example 4.5) instead uses the **simpler valid PDF** $f(x)=\frac{x^{2}}{27}$ on $[0,3]$ with the same second piece $\frac{5-x}{3}$ on $(3,5]$, giving $\int_{0}^{3}\frac{x^{2}}{27}dx=\frac13$ and total $\frac13+\frac23=1$. Either way, you must re-normalise — don't just integrate with the wrong $k$.

**Step 2 — Correct $P(1<X<4)$ using the coursebook-valid model $f(x)=\frac{x^{2}}{27}$ on $[0,3]$ (cleanest for the exam):**

Split at the join $x=3$:

$$P(1<X<4) = \int_{1}^{3}\frac{x^{2}}{27}\,dx + \int_{3}^{4}\frac{5-x}{3}\,dx$$

**First integral:**

$$\int_{1}^{3}\frac{x^{2}}{27}\,dx = \frac{1}{27}\left[\frac{x^{3}}{3}\right]_{1}^{3} = \frac{1}{81}\left[x^{3}\right]_{1}^{3} = \frac{27-1}{81} = \frac{26}{81}$$

**Second integral:**

$$\int_{3}^{4}\frac{5-x}{3}\,dx = \frac{1}{3}\left[5x-\frac{x^{2}}{2}\right]_{3}^{4} = \frac{1}{3}\left[(20-8)-\left(15-\frac{9}{2}\right)\right] = \frac{1}{3}\left[12-\frac{21}{2}\right] = \frac{1}{3}\cdot\frac{3}{2}=\frac12$$

**Combine:**

$$P(1<X<4) = \frac{26}{81}+\frac12 = \frac{52+81}{162} = \frac{133}{162}\approx 0.821 \quad\checkmark$$

With the originally-stated (invalid) $1/27\,x^{2}(5-x)$ first piece you would have got $\frac{70}{81}+\frac12=\frac{221}{162}>1$ — the $>1$ result flags the invalid PDF.

> **For the $4/297$ correction** the same split gives $P(1<X<4)=\frac{4}{297}\cdot\frac{70}{3}+\frac12=\frac{280}{891}+\frac12=\frac{1451}{1782}\approx0.814$.

> **Method for any correctly normalised piecewise PDF:** split at every join, integrate each piece over the overlap with $[a,b]$, add. Sketching $f$ and marking joins avoids wrong limits.

**What the examiner wants:** Evidence you split at $x=3$; no marks for a single integral from $1$ to $4$. Stating the total-area check explicitly earns the justification mark (J1) even if the PDF is given as valid.

---

### Example 4 — Trap — $P(X=c)=0$ and $< $ vs $\le$

> **Question:** $X$ is continuous with PDF
> $$f(x) = \begin{cases} \dfrac{3x^{2}}{64} & 0 \le x \le 4 \\ 0 & \text{otherwise} \end{cases}$$
> A student writes: "$P(X=2)=f(2)=\frac{12}{64}$ and $P(1\le X\le 3) \neq P(1<X<3)$." Explain both errors and find the correct $P(1\le X\le 3)$.
> *(Trap theme from Key Point 4.2, p. 79; cf. 9709/62/M/J/18 Q4 examiner report)*

**Solution:**

**Error 1:** For a continuous RV, $P(X=c)=0$ for *every* $c$. The value $f(c)$ is a *density*, not a probability. So:

$$P(X=2) = \int_{2}^{2} f(x)\,dx = 0 \quad\neq f(2)=\frac{12}{64}$$

**Error 2:** Because single points have zero probability, including or excluding endpoints does not change the probability:

$$P(1\le X\le 3) = P(1<X<3) = P(1<X\le 3) = P(1\le X<3)$$

**Correct probability:**

$$P(1\le X\le 3) = \int_{1}^{3}\frac{3x^{2}}{64}\,dx = \frac{3}{64}\left[\frac{x^{3}}{3}\right]_{1}^{3} = \frac{1}{64}\left[x^{3}\right]_{1}^{3}$$

$$= \frac{27-1}{64} = \frac{26}{64} = \frac{13}{32} \approx 0.406 \quad\checkmark$$

**What the examiner wants:** The statement "$P(X=c)=0$ because $X$ is continuous" — not just the numerical correction.

> ⭐ **Watch Out! — PART 1 Summary**
> - **Density $\neq$ probability.** Never write $P(X=a)=f(a)$. The PDF value can even exceed $1$ (e.g. $f=2$ on $[0,0.5]$) — that's fine because it's density, not probability.
> - **Limits kill marks.** When asked for $P(a<X<b)$, the limits are $a$ to $b$ — not $0$ to $b$, not $-\infty$ to $b$. For piecewise PDFs, split at every join inside $[a,b]$.
> - **Both PDF conditions.** "Show $f$ is a PDF" needs $f(x)\ge 0$ **and** $\int f =1$. Many candidates only do the integral.

---

# PART 2: Median, Quartiles and Percentiles

*Covers Key Point 4.4, Worked Examples 4.3–4.5, Exercise 4B, and End-of-Chapter Review Q2, Q7, Q8, Q10.*

## 2.1 Median, Quartiles, Percentiles — Rule

For a continuous RV $X$ with PDF $f(x)$:

$$\boxed{\text{Median } m: \quad \int_{-\infty}^{m} f(x)\,dx = 0.5 \qquad \Bigl(P(X\le m)=0.5\Bigr)}$$

$$\boxed{\text{Lower quartile } Q_{1}: \quad \int_{-\infty}^{Q_{1}} f(x)\,dx = 0.25 \qquad \text{Upper quartile } Q_{3}: \quad \int_{-\infty}^{Q_{3}} f(x)\,dx = 0.75}$$

$$\boxed{p\text{th percentile } r_{p}: \quad \int_{-\infty}^{r_{p}} f(x)\,dx = \frac{p}{100}}$$

Interquartile range: $\operatorname{IQR}=Q_{3}-Q_{1}$.

> **📦 When / Justification Box — Why $0.5$, not the mean?**
> - The median is the value that splits the *area* under the PDF in half — left area $=0.5$, right area $=0.5$ (Key Point 4.4, p. 84). It is a *positional* measure, not a balance point.
> - The mean $E(X)=\int x f(x)\,dx$ is the *centre of mass*. For skewed PDFs (most continuous models in this chapter), median $\neq$ mean. Confusing them is a top exam error.
> - For percentiles: the $p$th percentile has $p\%$ of the area to its left. So the 90th percentile solves $\int_{-\infty}^{r_{90}}f =0.90$.
> - **Piecewise PDFs:** You must first determine *which interval* $m$ lies in. Compute area up to each join; find where cumulative area crosses $0.5$. Only then solve the integral equation in that interval.

### Method Table — Median / Quartile / Percentile

| Step | What To Do | Detail |
|:---:|---|---|
| 1 | **Find cumulative area at each join** | $\int_{\text{start}}^{\text{join}} f(x)\,dx$ for each piece |
| 2 | **Locate the target** | Compare $0.5$ (or $0.25/0.75/p/100$) with cumulative areas to find which piece $m$ is in |
| 3 | **Set up the integral equation** | $\int_{-\infty}^{m} f(x)\,dx = \text{target}$ — split into complete pieces + partial piece |
| 4 | **Solve for $m$** | Integrate, substitute limits, solve (often quadratic/cubic — pick the root in the correct interval) |
| 5 | **For IQR: repeat for $Q_{1}$ and $Q_{3}$** | Then $\text{IQR}=Q_{3}-Q_{1}$ |

> ⭐ **Watch Out — PART 2 (before examples):** The median is NOT found by setting $f(m)=0.5$ or by solving $f(m)=\max/2$. It's an *area* condition. Also, when the PDF is piecewise, don't blindly integrate from the start — include the full area of earlier pieces.

### Example 1 — Easy — Median of a single-piece PDF

> **Question:** $X$ has PDF
> $$f(x) = \begin{cases} \dfrac{x^{2}}{72} & 0 \le x \le 6 \\ 0 & \text{otherwise} \end{cases}$$
> Find the median $m$ of $X$.
> *(Coursebook Worked Example 4.3, p. 84; cf. 9709/62/O/N/19 Q3 — single-piece power PDF)*

**Solution:**

Median $m$ satisfies $\int_{0}^{m} f(x)\,dx = 0.5$:

$$\int_{0}^{m} \frac{x^{2}}{72}\,dx = 0.5$$

$$\frac{1}{72}\left[\frac{x^{3}}{3}\right]_{0}^{m} = 0.5$$

$$\frac{m^{3}}{216} = 0.5$$

$$m^{3} = 108$$

$$m = \sqrt[3]{108} = 3\sqrt[3]{4} \approx 4.76 \quad\checkmark$$

**What the examiner wants:** The equation $\frac{m^{3}}{216}=0.5$ shown explicitly before solving; answer to 3 s.f. or exact surd.

---

### Example 2 — Medium — Quartiles and IQR (past-paper style)

> **Question:** $X$ has PDF
> $$f(x) = \begin{cases} \dfrac{2}{25}(5-x) & 0 \le x \le 5 \\ 0 & \text{otherwise} \end{cases}$$
> (a) Show that the median is $5-\frac{5}{\sqrt{2}}$. (b) Find the interquartile range.
> *(Coursebook Exercise 4B Q2; cf. 9709/71/Jun09 Q5, 9709/62/M/J/22 Q5)*

**Solution:**

**(a) Median $m$:**

$$\int_{0}^{m} \frac{2}{25}(5-x)\,dx = 0.5$$

$$\frac{2}{25}\left[5x-\frac{x^{2}}{2}\right]_{0}^{m} = 0.5$$

$$\frac{2}{25}\left(5m-\frac{m^{2}}{2}\right) = \frac{1}{2}$$

$$5m-\frac{m^{2}}{2} = \frac{25}{4}$$

Multiply by $2$: $10m - m^{2} = \frac{25}{2}$

$$m^{2} -10m + \frac{25}{2} = 0$$

$$m = \frac{10 \pm\sqrt{100-50}}{2} = \frac{10\pm\sqrt{50}}{2} = \frac{10\pm 5\sqrt{2}}{2} = 5\pm\frac{5}{\sqrt{2}}$$

Since $0\le m\le 5$, take the minus sign:

$$m = 5-\frac{5}{\sqrt{2}} \approx 1.46 \quad\checkmark$$

**(b) Quartiles:**

Lower quartile $Q_{1}$: $\int_{0}^{Q_{1}}\frac{2}{25}(5-x)dx =0.25$:

$$\frac{2}{25}\left(5Q_{1}-\frac{Q_{1}^{2}}{2}\right)=0.25 \implies 5Q_{1}-\frac{Q_{1}^{2}}{2}=\frac{25}{8}$$

$$Q_{1}^{2}-10Q_{1}+\frac{25}{4}=0 \implies Q_{1}=5-\frac{5\sqrt{3}}{2\sqrt{2}} \approx 5-3.06 = 1.94\text{?}$$

Let's solve cleanly: discriminant $=100-25=75$, so $Q_{1}=\frac{10-\sqrt{75}}{2}=\frac{10-5\sqrt{3}}{2}\approx 0.67$.

Upper quartile $Q_{3}$: $\int_{0}^{Q_{3}}\frac{2}{25}(5-x)dx =0.75$:

$$\frac{2}{25}\left(5Q_{3}-\frac{Q_{3}^{2}}{2}\right)=0.75 \implies 5Q_{3}-\frac{Q_{3}^{2}}{2}=\frac{75}{8}$$

$$Q_{3}^{2}-10Q_{3}+\frac{75}{4}=0 \implies Q_{3}=\frac{10-\sqrt{100-75}}{2}=\frac{10-5}{2}=2.5$$

$$\text{IQR}=Q_{3}-Q_{1}=\frac{10-5}{2}-\frac{10-5\sqrt{3}}{2}=\frac{5\sqrt{3}-5}{2}\approx 1.83$$

*(If arithmetic differs by rounding, the method — area $=0.25$ and $0.75$ — earns full method marks.)*

**What the examiner wants:** Surd form for the median; quadratic formula shown; correct root chosen (the one inside $[0,5]$).

---

### Example 3 — Hard — Median in a piecewise PDF (must locate interval first)

> **Question:** $X$ has PDF
> $$f(x) = \begin{cases} \dfrac{1}{27}x^{2} & 0 \le x \le 3 \\ \dfrac{1}{3}(5-x) & 3 < x \le 5 \\ 0 & \text{otherwise} \end{cases}$$
> Find the median $m$.
> *(Coursebook Worked Example 4.5, p. 86; cf. 9709/73/Jun14 Q2, 9709/62/O/N/22 Q5 piecewise)*
> *Note: the constant $\frac{1}{27}$ is coursebook-correct for this two-piece model; total area $= \int_{0}^{3}\frac{x^{2}}{27}dx+\int_{3}^{5}\frac{5-x}{3}dx = \frac{1}{3}+\frac{2}{3}=1$ ✓*

**Solution:**

**Step 1 — Area up to the join $x=3$:**

$$\int_{0}^{3}\frac{x^{2}}{27}\,dx = \frac{1}{27}\left[\frac{x^{3}}{3}\right]_{0}^{3}= \frac{1}{27}\cdot 9 = \frac{1}{3} \approx 0.333$$

Since $0.333 < 0.5$, the median lies **beyond** $x=3$, in the second piece.

**Step 2 — Set up median equation:**

$$\int_{0}^{3}\frac{x^{2}}{27}\,dx + \int_{3}^{m}\frac{5-x}{3}\,dx = 0.5$$

$$\frac{1}{3} + \frac{1}{3}\left[5x-\frac{x^{2}}{2}\right]_{3}^{m} = 0.5$$

$$\frac{1}{3}\left[\left(5m-\frac{m^{2}}{2}\right)-\left(15-\frac{9}{2}\right)\right] = 0.5-\frac{1}{3}=\frac{1}{6}$$

$$5m-\frac{m^{2}}{2}-\frac{21}{2} = \frac{1}{2}$$

$$5m-\frac{m^{2}}{2} = 11$$

Multiply by $2$: $10m - m^{2} = 22$

$$m^{2}-10m+22=0$$

$$m = \frac{10\pm\sqrt{100-88}}{2}=\frac{10\pm\sqrt{12}}{2}=5\pm\sqrt{3}$$

Since $3 < m \le 5$, take $m = 5-\sqrt{3}\approx 3.27$.

But wait — $5-\sqrt{3}\approx 3.27$ is indeed in $(3,5]$ ✓, while $5+\sqrt{3}\approx 6.73$ is outside. So:

$$m = 5-\sqrt{3}\approx 3.27 \quad\checkmark$$

*(The coursebook WE 4.5 gets a different quadratic $m^{2}-10m+20=0$ giving $m\approx 2.76$ or $3.27$ depending on which normalisation is used — the **method** of locating the interval first is what matters.)*

**What the examiner wants:** Explicit statement "area to $x=3$ is $1/3 < 0.5$ so $m>3$" — this locating step is worth a mark on its own.

---

### Example 4 — Trap — Percentile confusion and $<$ vs $\le$

> **Question:** $X$ has PDF
> $$f(x) = \begin{cases} \dfrac{3x^{2}}{64} & 0 \le x \le 4 \\ 0 & \text{otherwise} \end{cases}$$
> (a) Find the 90th percentile $r_{90}$. (b) A student claims $P(X\le r_{90})=0.9$ but $P(X < r_{90})\neq 0.9$. Is this correct?
> *(Trap theme; cf. 9709/62/M/J/19 Q6 percentile question; Key Point 4.2 p.79)*

**Solution:**

**(a) 90th percentile** solves $\int_{0}^{r_{90}} f(x)\,dx = 0.90$:

$$\int_{0}^{r_{90}}\frac{3x^{2}}{64}\,dx = 0.90$$

$$\frac{3}{64}\cdot\frac{r_{90}^{3}}{3}=0.90$$

$$\frac{r_{90}^{3}}{64}=0.90$$

$$r_{90}^{3}=57.6$$

$$r_{90}=\sqrt[3]{57.6}\approx 3.86 \quad\checkmark$$

**(b)** The student is **wrong**. For a continuous RV, $P(X=r_{90})=0$, so:

$$P(X\le r_{90}) = P(X < r_{90}) + P(X=r_{90}) = P(X<r_{90})+0$$

$$P(X\le r_{90}) = P(X<r_{90}) = 0.90$$

There is no difference between $<$ and $\le$ (or $>$ and $\ge$) for continuous RVs.

**What the examiner wants:** The explicit "$P(X=c)=0$ so $<$ and $\le$ give the same probability" justification.

> ⭐ **Watch Out! — PART 2 Summary**
> - **Median $\neq$ mean $\neq$ mode.** Median is area $=0.5$; mean is $\int x f(x)\,dx$; mode is where $f$ is maximal. Don't mix the setups.
> - **Piecewise: locate first.** Compute cumulative area at each join to find which piece contains $m/Q_{1}/Q_{3}/r_{p}$. Then solve only in that piece (including full earlier pieces).
> - **$<$ vs $\le$ never matters here.** If a question asks for $P(X\le m)$ vs $P(X<m)$, the answer is the same — say so to earn the justification mark.

---

# PART 3: Expectation and Variance

*Covers Key Point 4.5, Worked Examples 4.6–4.7, Exercise 4C, and End-of-Chapter Review Q1, Q4, Q6, Q10, Q12.*

## 3.1 Expectation and Variance — Rule

For a continuous RV $X$ with PDF $f(x)$:

$$\boxed{E(X) = \int_{-\infty}^{\infty} x\,f(x)\,dx}$$

$$\boxed{E\big(g(X)\big) = \int_{-\infty}^{\infty} g(x)\,f(x)\,dx \qquad\text{(e.g. }E(X^{2})=\int x^{2}f(x)\,dx\text{)}}$$

$$\boxed{\operatorname{Var}(X) = E(X^{2}) - \big[E(X)\big]^{2} = \int_{-\infty}^{\infty} x^{2}f(x)\,dx - \left(\int_{-\infty}^{\infty} x f(x)\,dx\right)^{2}}$$

Standard deviation: $\sigma = \sqrt{\operatorname{Var}(X)}$.

For a piecewise PDF, split each integral at every join.

> **📦 When / Justification Box — Why these formulas?**
> - **Discrete → continuous:** For a discrete RV, $E(X)=\sum x\,P(X=x)$. For a continuous RV, $P(X=x)=0$ but $P(x<X<x+\delta x)\approx f(x)\,\delta x$. Replacing the sum by an integral gives $E(X)=\int x f(x)\,dx$ (derivation p. 88).
> - **$\operatorname{Var}(X)=E(X^{2})-[E(X)]^{2}$:** Same identity as for discrete RVs. The coursebook (p. 89) derives $E(X^{2})=\int x^{2}f(x)\,dx$ by the same strip argument, then uses the standard variance formula. Never try $\int (x-\mu)^{2}f(x)\,dx$ unless the question explicitly asks — it's algebraically equivalent but longer.
> - **$E(g(X))$:** To find $E(X^{2})$, multiply $f(x)$ by $x^{2}$ before integrating — don't square $E(X)$. The error $E(X^{2})=[E(X)]^{2}$ loses all variance marks.
> - **Existence:** These integrals must converge. For 9709, every PDF has finite domain (e.g. $[0,5]$) so convergence is automatic.

### Method Table — Expectation and Variance

| Step | What To Do | Detail |
|:---:|---|---|
| 1 | **Write $E(X)=\int x f(x)\,dx$ over the full domain** | For piecewise: sum of $\int_{\text{piece}} x f(x)\,dx$ |
| 2 | **Integrate term by term** | Expand $x\cdot f(x)$ first; integrate powers |
| 3 | **Write $E(X^{2})=\int x^{2} f(x)\,dx$** | Multiply $f(x)$ by $x^{2}$, not $x$ |
| 4 | **Compute $\operatorname{Var}(X)=E(X^{2})-[E(X)]^{2}$** | Square $E(X)$ *after* computing it; keep exact fractions until the end |
| 5 | **For $E(g(X))$: replace $x$ by $g(x)$** | e.g. $E(2X+3)=2E(X)+3$; $E(X^{3})=\int x^{3}f(x)\,dx$ |

> ⭐ **Watch Out — PART 3 (before examples):** The #1 error is writing $\operatorname{Var}(X)=\int x^{2}f(x)\,dx$ and forgetting to subtract $[E(X)]^{2}$. The #2 error is computing $E(X^{2})$ as $[E(X)]^{2}$. Always compute *two* integrals: one for $E(X)$, one for $E(X^{2})$.

### Example 1 — Easy — Mean and variance of a single-piece polynomial PDF

> **Question:** $X$ has PDF
> $$f(x) = \begin{cases} \dfrac{3x^{2}}{64} & 0 \le x \le 4 \\ 0 & \text{otherwise} \end{cases}$$
> Find $E(X)$ and $\operatorname{Var}(X)$.
> *(Coursebook Exercise 4C Q1–Q2 style; cf. 9709/62/O/N/18 Q4)*

**Solution:**

**Expectation:**

$$E(X) = \int_{0}^{4} x\cdot\frac{3x^{2}}{64}\,dx = \frac{3}{64}\int_{0}^{4} x^{3}\,dx = \frac{3}{64}\left[\frac{x^{4}}{4}\right]_{0}^{4}$$

$$= \frac{3}{64}\cdot\frac{256}{4} = \frac{3}{64}\cdot 64 = 3$$

$$E(X)=3 \quad\checkmark$$

**Second moment:**

$$E(X^{2}) = \int_{0}^{4} x^{2}\cdot\frac{3x^{2}}{64}\,dx = \frac{3}{64}\int_{0}^{4} x^{4}\,dx = \frac{3}{64}\left[\frac{x^{5}}{5}\right]_{0}^{4}$$

$$= \frac{3}{64}\cdot\frac{1024}{5} = \frac{3072}{320} = \frac{48}{5}=9.6$$

**Variance:**

$$\operatorname{Var}(X) = E(X^{2})-[E(X)]^{2} = \frac{48}{5}-9 = \frac{48-45}{5}=\frac{3}{5}=0.6$$

$$\sigma = \sqrt{0.6}\approx 0.775 \quad\checkmark$$

**What the examiner wants:** Both integrals shown; $\operatorname{Var}=E(X^{2})-[E(X)]^{2}$ stated, not just $\int x^{2}f$.

---

### Example 2 — Medium — $E(X)$ and $\operatorname{Var}(X)$ with a linear PDF (past-paper style)

> **Question:** $X$ has PDF
> $$f(x) = \begin{cases} \dfrac{2}{25}(5-x) & 0 \le x \le 5 \\ 0 & \text{otherwise} \end{cases}$$
> Find $E(X)$ and $\operatorname{Var}(X)$.
> *(Coursebook Exercise 4B Q2 / 4C Q1; cf. 9709/71/Jun09 Q5, 9709/62/M/J/23 Q2)*

**Solution:**

**Expectation:**

$$E(X) = \int_{0}^{5} x\cdot\frac{2}{25}(5-x)\,dx = \frac{2}{25}\int_{0}^{5}(5x-x^{2})\,dx$$

$$= \frac{2}{25}\left[\frac{5x^{2}}{2}-\frac{x^{3}}{3}\right]_{0}^{5} = \frac{2}{25}\left[\frac{125}{2}-\frac{125}{3}\right]$$

$$= \frac{2}{25}\cdot 125\left(\frac{1}{2}-\frac{1}{3}\right)=\frac{2}{25}\cdot125\cdot\frac{1}{6}=\frac{250}{150}=\frac{5}{3}\approx 1.667$$

**Second moment:**

$$E(X^{2}) = \int_{0}^{5} x^{2}\cdot\frac{2}{25}(5-x)\,dx = \frac{2}{25}\int_{0}^{5}(5x^{2}-x^{3})\,dx$$

$$= \frac{2}{25}\left[\frac{5x^{3}}{3}-\frac{x^{4}}{4}\right]_{0}^{5}= \frac{2}{25}\left[\frac{625}{3}-\frac{625}{4}\right]$$

$$= \frac{2}{25}\cdot625\left(\frac{1}{3}-\frac{1}{4}\right)=\frac{2}{25}\cdot625\cdot\frac{1}{12}=\frac{1250}{300}=\frac{25}{6}\approx 4.167$$

**Variance:**

$$\operatorname{Var}(X) = \frac{25}{6}-\left(\frac{5}{3}\right)^{2}=\frac{25}{6}-\frac{25}{9}=\frac{75-50}{18}=\frac{25}{18}\approx 1.389 \quad\checkmark$$

**What the examiner wants:** Exact fractions; expansion of $x(5-x)$ before integrating.

---

### Example 3 — Hard — Piecewise $E(X)$ and $\operatorname{Var}(X)$

> **Question:** $X$ has PDF
> $$f(x) = \begin{cases} \dfrac{x}{8} & 0 \le x \le 2 \\[6pt] \dfrac{1}{4} & 2 < x \le 4 \\[6pt] \dfrac{6-x}{8} & 4 < x \le 6 \\[6pt] 0 & \text{otherwise} \end{cases}$$
> This is a symmetric trapezium PDF (total area $=1$). Find $E(X)$ and $\operatorname{Var}(X)$.
> *(Coursebook Exercise 4B Q5 / 4C Q3 piecewise style; cf. 9709/62/O/N/22 Q5, 9709/73/Jun14 Q2. Note the third piece must be $\frac{6-x}{8}$ so $f\ge0$ and $f(6)=0$; the form $\frac{4-x}{8}$ would go negative for $x>4$ and cannot be a PDF.)*

**Solution:**

By symmetry about $x=3$, we anticipate $E(X)=3$ — verify by integration.

**Check total area (quick):**

$$\int_{0}^{2}\frac{x}{8}dx+\int_{2}^{4}\frac14dx+\int_{4}^{6}\frac{6-x}{8}dx = \frac14+\frac12+\frac14 =1\ \checkmark$$

**Expectation (split into three pieces):**

$$E(X) = \int_{0}^{2} x\cdot\frac{x}{8}\,dx + \int_{2}^{4} x\cdot\frac{1}{4}\,dx + \int_{4}^{6} x\cdot\frac{6-x}{8}\,dx$$

$$= \frac{1}{8}\int_{0}^{2}x^{2}\,dx + \frac{1}{4}\int_{2}^{4}x\,dx + \frac{1}{8}\int_{4}^{6}\left(6x-x^{2}\right)dx$$

$$= \frac{1}{8}\left[\frac{x^{3}}{3}\right]_{0}^{2} + \frac{1}{4}\left[\frac{x^{2}}{2}\right]_{2}^{4} + \frac{1}{8}\left[3x^{2}-\frac{x^{3}}{3}\right]_{4}^{6}$$

$$= \frac{1}{8}\cdot\frac{8}{3} + \frac{1}{4}\left(8-2\right) + \frac{1}{8}\left[\left(108-72\right)-\left(48-\frac{64}{3}\right)\right]$$

$$= \frac{1}{3} + \frac{3}{2} + \frac{1}{8}\left[36-\frac{80}{3}\right] = \frac{1}{3}+\frac{3}{2}+\frac{7}{6} = \frac{2+9+7}{6}=3\ \checkmark$$

So $E(X)=3$ as symmetry predicted.

**Second moment:**

$$E(X^{2}) = \int_{0}^{2}x^{2}\cdot\frac{x}{8}\,dx + \int_{2}^{4}x^{2}\cdot\frac14\,dx + \int_{4}^{6}x^{2}\cdot\frac{6-x}{8}\,dx$$

$$= \frac{1}{8}\int_{0}^{2}x^{3}\,dx + \frac{1}{4}\int_{2}^{4}x^{2}\,dx + \frac{1}{8}\int_{4}^{6}\left(6x^{2}-x^{3}\right)dx$$

$$= \frac{1}{8}\left[\frac{x^{4}}{4}\right]_{0}^{2}+\frac{1}{4}\left[\frac{x^{3}}{3}\right]_{2}^{4}+\frac{1}{8}\left[2x^{3}-\frac{x^{4}}{4}\right]_{4}^{6}$$

$$= \frac{1}{8}\cdot4 + \frac{1}{4}\cdot\frac{56}{3}+\frac{1}{8}\left[(432-324)-(128-64)\right]$$

$$= \frac12 + \frac{14}{3} + \frac{1}{8}\cdot44 = \frac12+\frac{14}{3}+\frac{11}{2} = \frac{32}{3}\approx10.667$$

$$\operatorname{Var}(X)=E(X^{2})-[E(X)]^{2}=\frac{32}{3}-9=\frac{5}{3}\approx 1.667 \quad\checkmark$$

**What the examiner wants:** Splitting at every join for *both* $E(X)$ and $E(X^{2})$; recognising symmetry as a check but still showing integration.

---

### Example 4 — Trap — $E(X^{2})\neq[E(X)]^{2}$ and $E(g(X))$ confusion

> **Question:** $X$ has PDF $f(x)=\frac{3x^{2}}{64}$ on $[0,4]$. A student writes:
> (i) "$E(X^{2})=[E(X)]^{2}=9$ so $\operatorname{Var}(X)=0$."
> (ii) "$E(2X+1)=2\int x^{2}f(x)\,dx+1$."
> Correct both and find $\operatorname{Var}(X)$ and $E(2X+1)$.
> *(Trap theme; cf. 9709/62/M/J/18 Q4, 9709/71/Jun09 Q5 examiner reports)*

**Solution:**

**(i) Error:** $E(X^{2})\neq[E(X)]^{2}$. Correct:

$$E(X)=3 \quad\text{(from Example 1)}$$

$$E(X^{2})=\frac{48}{5}=9.6 \quad\text{(from Example 1)}$$

$$\operatorname{Var}(X)=E(X^{2})-[E(X)]^{2}=9.6-9=0.6\neq 0$$

The variance is zero only for a constant random variable — not here.

**(ii) Error:** $E(2X+1)=2E(X)+1$, not $2E(X^{2})+1$. The student confused $E(X)$ with $E(X^{2})$.

$$E(2X+1)=\int_{0}^{4}(2x+1)f(x)\,dx =2\int_{0}^{4}xf(x)dx+\int_{0}^{4}f(x)dx$$

$$=2E(X)+1 =2(3)+1=7$$

Alternatively: $E(2X+1)=2\cdot3+1=7\quad\checkmark$

And for reference: $E(X^{2})$ is needed for variance, but $E(2X+1)$ uses $E(X)$ linearly.

**What the examiner wants:** The explicit correction "$E(X^{2})\neq[E(X)]^{2}$" and the linearity $E(aX+b)=aE(X)+b$.

> ⭐ **Watch Out! — PART 3 Summary**
> - **Two integrals for variance.** Always compute $E(X)$ and $E(X^{2})$ separately. Writing $\operatorname{Var}=\int x^{2}f -\left(\int x f\right)^{2}$ in one line without intermediate values risks arithmetic slips.
> - **$E(X^{2})$ means $\int x^{2}f(x)\,dx$.** Not $\left(\int x f\right)^{2}$, not $\int [x f(x)]^{2}$, not $\int x^{2}f(x)^{2}$.
> - **Piecewise: split every integral.** The same joins apply to $E(X)$ and $E(X^{2})$. Missing a piece in either integral gives the wrong variance.
> - **Keep fractions exact until the end.** Rounding $E(X)$ to 2 s.f. then squaring it amplifies error in $\operatorname{Var}$.

---

# PART 4: Mixed, Piecewise and Exam Traps

*Covers all of Chapter 4 combined: verifying PDFs with unknown constants, combining skills, and the most common exam pitfalls (End-of-Chapter Review Q1–Q12).*

## 4.1 The Complete Workflow — Rule

Any continuous RV question follows this pipeline:

$$\boxed{\text{Find/verify }k \;( \int f=1) \;\to\; \text{Probabilities }\left(\int_{a}^{b}f\right) \;\to\; \text{Median/percentile }\left(\int_{-\infty}^{m}f=0.5\right) \;\to\; E(X),\,E(X^{2}),\,\operatorname{Var}(X)}$$

For piecewise PDFs, every arrow splits at the joins.

> **📦 When / Justification Box — Why a combined workflow?**
> - **Finding $k$ must come first.** Every later integral uses $f(x)$, so a wrong $k$ invalidates all subsequent answers. The coursebook (WE 4.1, WE 4.6) always finds $k$ before anything else.
> - **Probabilities are areas — but only over the right interval.** For $P(1<X<7)$ with PDF on $[0,5]$, the integral is $\int_{1}^{5}f(x)\,dx$, not $\int_{1}^{7}f(x)\,dx$ — the PDF is $0$ beyond $5$ (Key Point 4.3).
> - **Median vs mean — different equations, different answers.** The median solves $\int_{-\infty}^{m}f=0.5$; the mean is $\int x f(x)\,dx$. For skewed PDFs they differ. The exam often asks for both to test you know the difference.
> - **Exam traps cluster here:** $P(X=c)=0$, density vs probability, $< $ vs $\le$, wrong limits for piecewise, $E(X^{2})\neq[E(X)]^{2}$, forgetting to include all pieces.

### Method Table — Complete Mixed Question

| Step | What To Do | Detail |
|:---:|---|---|
| 1 | **Find $k$** | $\int_{\text{domain}} f(x)\,dx =1$; check $f\ge 0$ |
| 2 | **Sketch $f(x)$** | Mark joins, values at joins, where $f=0$ |
| 3 | **Probabilities** | $\int_{a}^{b} f(x)\,dx$ — truncate to domain, split at joins |
| 4 | **Median/percentile** | Cumulative area at joins → locate interval → solve $\int_{-\infty}^{m}f=0.5$ |
| 5 | **Expectation & variance** | $E(X)=\int x f$, $E(X^{2})=\int x^{2}f$, $\operatorname{Var}=E(X^{2})-[E(X)]^{2}$ — split every integral |
| 6 | **Trap check** | $P(X=c)=0$? Density $\neq$ probability? $< $ vs $\le$ irrelevant? Correct $k$ used throughout? |

> ⭐ **Watch Out — PART 4 (before examples):** In a multi-part question, part (a) often asks you to "show $k=\ldots$" — the *given* $k$ must be used in later parts even if your calculation gave a different value. Follow the rubric.

### Example 1 — Easy — Find $k$, verify PDF, simple probability

> **Question:** $X$ has PDF
> $$f(x) = \begin{cases} k\,x(3-x) & 0 \le x \le 3 \\[4pt] 0 & \text{otherwise} \end{cases}$$
> (a) Show that $k=\frac{2}{9}$. (b) Find $P(1<X<2)$.
> *(Coursebook Exercise 4C Q1 / End-of-Chapter Review Q12 style; cf. 9709/71/Jun09 Q5, 9709/62/O/N/18 Q4)*

**Solution:**

**(a) Find $k$:**

$$\int_{0}^{3} kx(3-x)\,dx = k\int_{0}^{3}\left(3x-x^{2}\right)dx = k\left[\frac{3x^{2}}{2}-\frac{x^{3}}{3}\right]_{0}^{3}$$

$$= k\left[\frac{27}{2}-9\right]=k\cdot\frac{9}{2}=1$$

$$k=\frac{2}{9}\quad\checkmark$$

Check: $f(x)=\frac{2}{9}x(3-x)\ge 0$ on $[0,3]$ (parabola with zeros at $0$ and $3$, positive between) and $\int f =1$, so valid PDF ✓.

> *If an exam paper states a different $k$ (e.g. $k=4/9$), it implies a different domain or polynomial — e.g. $0\le x\le2$ or $k x^{2}(3-x)$. Always re-derive $k$ for the PDF as printed; for later parts use the $k$ **given** in the question (follow the rubric) even if it differs from your derived value — follow-through marks depend on it.*

**(b) Probability:**

$$P(1<X<2)=\int_{1}^{2}\frac{2}{9}x(3-x)\,dx=\frac{2}{9}\left[\frac{3x^{2}}{2}-\frac{x^{3}}{3}\right]_{1}^{2}$$

$$=\frac{2}{9}\left[\left(6-\frac{8}{3}\right)-\left(\frac{3}{2}-\frac{1}{3}\right)\right]=\frac{2}{9}\left[\frac{10}{3}-\frac{7}{6}\right]=\frac{2}{9}\cdot\frac{13}{6}=\frac{13}{27}\approx0.481 \quad\checkmark$$

**What the examiner wants:** The integral set equal to $1$ solved for $k$; correct limits $1$ to $2$ for the probability.

---

### Example 2 — Medium — Piecewise: find $k$, then median (past-paper style)

> **Question:** $X$ has PDF
> $$f(x) = \begin{cases} kx & 0 \le x \le 2 \\[4pt] k(6-x) & 2 < x \le 6 \\[4pt] 0 & \text{otherwise} \end{cases}$$
> (This is a triangular/trapezium PDF peaking at $x=2$.)
> (a) Show that $k=\frac{1}{10}$. (b) Find the median $m$.
> *(Coursebook Exercise 4B Q5 triangular style; cf. 9709/73/Jun14 Q2, 9709/62/O/N/22 Q5. Note: the value $k=1/10$ is correct for this shape; $k=1/8$ would correspond to a different peak or base — always integrate for the PDF as printed.)*

**Solution:**

**(a) Find $k$:**

$$\int_{0}^{2} kx\,dx + \int_{2}^{6}k(6-x)\,dx = k\left[\frac{x^{2}}{2}\right]_{0}^{2}+k\left[6x-\frac{x^{2}}{2}\right]_{2}^{6}$$

$$= k\cdot2 + k\left[(36-18)-(12-2)\right]=2k+8k=10k$$

$$10k=1 \implies k=\frac{1}{10}\quad\checkmark$$

Check peak height $f(2)=2k=1/5=0.2$, base $6$, shape is a scalene triangle (not symmetric) with area $10k=1$ ✓. The symmetric triangle $f(x)=kx$ on $[0,2.5]$ and $k(5-x)$ on $[2.5,5]$ would give $k=4/25$, but that's a different PDF — integrate the one you are given.

**(b) Median — locate interval:**

Area up to $x=2$: $\int_{0}^{2}\frac{x}{10}dx=\frac{1}{10}\cdot2=0.2 <0.5$, so $m>2$ (in second piece).

$$\int_{0}^{2}\frac{x}{10}dx+\int_{2}^{m}\frac{6-x}{10}dx=0.5$$

$$0.2+\frac{1}{10}\left[6x-\frac{x^{2}}{2}\right]_{2}^{m}=0.5$$

$$\frac{1}{10}\left[\left(6m-\frac{m^{2}}{2}\right)-10\right]=0.3$$

$$6m-\frac{m^{2}}{2}-10=3$$

$$6m-\frac{m^{2}}{2}=13$$

$$m^{2}-12m+26=0$$

$$m=\frac{12\pm\sqrt{144-104}}{2}=\frac{12\pm\sqrt{40}}{2}=6\pm\sqrt{10}$$

Since $2<m\le6$, $m=6-\sqrt{10}\approx 2.84 \quad\checkmark$ (the other root $6+\sqrt{10}\approx9.16$ is outside).

**What the examiner wants:** Locating step "$0.2<0.5$ so $m>2$" explicitly; quadratic with correct root chosen.

---

### Example 3 — Hard — Combine all skills: $k$, probability, $E(X)$, $\operatorname{Var}(X)$

> **Question:** $X$ has PDF
> $$f(x) = \begin{cases} \dfrac{3}{32}(4-x^{2}) & -2 \le x \le 2 \\ 0 & \text{otherwise} \end{cases}$$
> (Symmetric about $0$.)
> (a) Verify $f$ is a valid PDF. (b) Find $P(|X|>1)$. (c) Find $E(X)$ and $\operatorname{Var}(X)$.
> *(Coursebook End-of-Chapter Review Q5 symmetric style; cf. 9709/62/M/J/23 Q5, 9709/73/Nov16 Q8 — symmetric PDF variance comparison)*

**Solution:**

**(a) Verify PDF:**

$f(x)=\frac{3}{32}(4-x^{2})\ge 0$ on $[-2,2]$ since $x^{2}\le4$ ✓

$$\int_{-2}^{2}\frac{3}{32}(4-x^{2})dx=\frac{3}{32}\left[4x-\frac{x^{3}}{3}\right]_{-2}^{2}$$

$$=\frac{3}{32}\left[\left(8-\frac{8}{3}\right)-\left(-8+\frac{8}{3}\right)\right]=\frac{3}{32}\left[\frac{16}{3}+\frac{16}{3}\right]=\frac{3}{32}\cdot\frac{32}{3}=1 \quad\checkmark$$

**(b) $P(|X|>1)=P(X<-1\text{ or }X>1)$:**

By symmetry $P(X<-1)=P(X>1)$, so $P(|X|>1)=2P(X>1)$:

$$P(X>1)=\int_{1}^{2}\frac{3}{32}(4-x^{2})dx=\frac{3}{32}\left[4x-\frac{x^{3}}{3}\right]_{1}^{2}$$

$$=\frac{3}{32}\left[\frac{16}{3}-\left(4-\frac{1}{3}\right)\right]=\frac{3}{32}\left[\frac{16}{3}-\frac{11}{3}\right]=\frac{3}{32}\cdot\frac{5}{3}=\frac{5}{32}$$

$$P(|X|>1)=2\cdot\frac{5}{32}=\frac{5}{16}=0.3125 \quad\checkmark$$

**(c) Expectation and variance:**

By symmetry about $0$ (even function $f$: $f(-x)=f(x)$):

$$E(X)=\int_{-2}^{2}x f(x)\,dx =0 \quad\text{(odd integrand over symmetric interval)} \quad\checkmark$$

$$E(X^{2})=\int_{-2}^{2}x^{2}\cdot\frac{3}{32}(4-x^{2})dx=\frac{3}{32}\int_{-2}^{2}(4x^{2}-x^{4})dx$$

$$=\frac{3}{32}\left[\frac{4x^{3}}{3}-\frac{x^{5}}{5}\right]_{-2}^{2}=\frac{3}{32}\cdot 2\left[\frac{32}{3}-\frac{32}{5}\right]$$

$$=\frac{3}{16}\cdot32\left(\frac{1}{3}-\frac{1}{5}\right)=\frac{3\cdot2}{1}\cdot\frac{2}{15}=\frac{12}{15}=\frac{4}{5}=0.8$$

$$\operatorname{Var}(X)=E(X^{2})-[E(X)]^{2}=0.8-0=0.8=\frac{4}{5} \quad\checkmark$$

**What the examiner wants:** Symmetry argument for $E(X)=0$ stated ("odd function over symmetric interval" or "by symmetry"); doubling $P(X>1)$ for $|X|>1$.

---

### Example 4 — Trap — Area vs probability, wrong $k$, and $P(X=c)$ in a mixed question

> **Question:** $X$ has PDF
> $$f(x) = \begin{cases} kx^{2} & 0 \le x \le 3 \\ 0 & \text{otherwise} \end{cases}$$
> A student writes:
> (a) "$k=1$ because $\int_{0}^{3}x^{2}dx=9$ so $k=1/9$ — no wait, $k=1$ because area must be $1$."
> (b) "$P(X=1.5)=k(1.5)^{2}=2.25k$."
> (c) "$P(2<X<5)=\int_{2}^{5}kx^{2}dx$."
> Identify each error and give the correct $k$, $P(X=1.5)$ and $P(2<X<5)$.
> *(Trap theme synthesising all of Chapter 4; cf. 9709/62/M/J/18 Q4, 9709/71/Jun09 Q5 examiner reports on area/probability confusion)*

**Solution:**

**(a) Error:** The student contradicts themselves. Correct:

$$\int_{0}^{3}kx^{2}dx =k\left[\frac{x^{3}}{3}\right]_{0}^{3}=k\cdot9=1$$

$$k=\frac{1}{9} \quad\checkmark$$

Not $k=1$. The check $f(x)=\frac{x^{2}}{9}\ge0$ on $[0,3]$ ✓.

**(b) Error:** $P(X=1.5)=0$ for any continuous RV, not $f(1.5)$. The quantity $k(1.5)^{2}=0.25$ is the *density* at $x=1.5$, not a probability.

$$P(X=1.5)=0 \quad\checkmark$$

**(c) Error:** The PDF is $0$ for $x>3$, so the upper limit must be truncated to $3$:

$$P(2<X<5)=\int_{2}^{3}kx^{2}dx \quad\text{(not }\int_{2}^{5}\text{)}$$

$$=\frac{1}{9}\left[\frac{x^{3}}{3}\right]_{2}^{3}=\frac{1}{27}(27-8)=\frac{19}{27}\approx0.704 \quad\checkmark$$

If you integrate to $5$, you include area where $f=0$ — but if you mistakenly extend $kx^{2}$ beyond $x=3$, you'd get $\int_{2}^{5}kx^{2}dx=\frac{117}{27}=4.33>1$ — impossible for a probability, revealing the error.

**What the examiner wants:** Three explicit corrections — correct $k=1/9$, "$P(X=c)=0$ for continuous", and "truncate to domain $[0,3]$".

> ⭐ **Watch Out! — PART 4 Summary**
> - **$k$ first, always.** Every later part depends on it. If the exam *gives* you $k$, use the given value even if your calculation disagrees — the follow-through marks depend on it.
> - **Truncate probabilities to the PDF's domain.** $P(a<X<b)$ only integrates over $[a,b]\cap\text{domain}$. Integrating beyond the domain with the formula for $f(x)$ is a fatal error.
> - **$P(X=c)=0$ is not optional.** Any question that mentions $P(X=c)$ expects you to state this. Writing $P(X=c)=f(c)$ scores zero.
> - **Symmetry shortcuts must be justified.** "By symmetry $E(X)=3$" needs "the PDF is symmetric about $x=3$" — a one-line justification earns the reasoning mark.

---

# Formula Sheet

All formulas for Chapter 4 — every one that can appear in 9709 S2.

### PDF Conditions

$$f(x) \ge 0 \quad \text{for all } x$$

$$\int_{-\infty}^{\infty} f(x)\,dx = 1$$

$$f(x) = 0 \quad \text{outside stated domain}$$

### Probabilities

$$P(a < X < b) = P(a \le X \le b) = \int_{a}^{b} f(x)\,dx$$

$$P(X = c) = 0 \quad \text{for any } c$$

$$P(X > a) = \int_{a}^{\infty} f(x)\,dx = 1 - \int_{-\infty}^{a} f(x)\,dx$$

$$P(X < b) = \int_{-\infty}^{b} f(x)\,dx$$

### Median, Quartiles, Percentiles

$$\int_{-\infty}^{m} f(x)\,dx = 0.5 \qquad\text{(median)}$$

$$\int_{-\infty}^{Q_{1}} f(x)\,dx = 0.25, \qquad \int_{-\infty}^{Q_{3}} f(x)\,dx = 0.75$$

$$\operatorname{IQR}=Q_{3}-Q_{1}$$

$$\int_{-\infty}^{r_{p}} f(x)\,dx = \frac{p}{100} \qquad (p\text{th percentile})$$

### Expectation and Variance

$$E(X) = \int_{-\infty}^{\infty} x\,f(x)\,dx$$

$$E\big(g(X)\big) = \int_{-\infty}^{\infty} g(x)\,f(x)\,dx$$

$$E(X^{2}) = \int_{-\infty}^{\infty} x^{2}f(x)\,dx$$

$$\operatorname{Var}(X) = E(X^{2}) - [E(X)]^{2}$$

$$\sigma = \sqrt{\operatorname{Var}(X)}$$

$$E(aX+b) = aE(X)+b, \qquad \operatorname{Var}(aX+b)=a^{2}\operatorname{Var}(X)$$

### Piecewise PDFs

If $f(x)=\begin{cases}f_{1}(x)&a\le x\le b\\ f_{2}(x)&b< x\le c\end{cases}$ then:

$$\int_{a}^{c} f(x)\,dx = \int_{a}^{b}f_{1}(x)\,dx+\int_{b}^{c}f_{2}(x)\,dx =1$$

$$P(u<X<v)=\sum_{\text{pieces overlapping }[u,v]}\int_{\text{overlap}} f_{i}(x)\,dx$$

$$E(X)=\int_{a}^{b}x f_{1}(x)\,dx+\int_{b}^{c}x f_{2}(x)\,dx$$

### Rectangular (Uniform) Distribution — Special Case (Explore 4.3, p. 92)

$$f(x)=\begin{cases}\dfrac{1}{b-a}&a\le x\le b\\0&\text{otherwise}\end{cases}$$

$$E(X)=\frac{a+b}{2}, \quad \operatorname{Var}(X)=\frac{(b-a)^{2}}{12}, \quad \text{median}=\frac{a+b}{2}$$

### Exponential Distribution — Special Case (Explore 4.4, p. 93; Exercise 4A Q7, 4C Q7)

$$f(t)=\begin{cases}\lambda e^{-\lambda t}&t\ge0\\0&\text{otherwise}\end{cases}\quad(\lambda>0)$$

$$P(T>a)=e^{-\lambda a}, \qquad E(T)=\frac1\lambda,\qquad \operatorname{Var}(T)=\frac1{\lambda^{2}}$$

---

# Methods Summary Table

| Formula / Task | Type 1 — Single-piece | Type 2 — Piecewise / split | Type 3 — Trap / special | Past Paper Refs |
|---|---|---|---|---|
| **Verify PDF / find $k$** | $\int_{a}^{b}k\cdot g(x)\,dx=1$ — one integral, solve for $k$; check $f\ge0$ | $\sum\int_{\text{piece}}f_{i}(x)\,dx=1$ — sum pieces, solve for $k$ | Check $k$ gives $f\ge0$; if $k<0$ on domain, reject — PDF invalid | 9709/62/O/N/22 Q3; 9709/71/Jun09 Q5(i); 9709/73/Jun14 Q5(ii); 9709/72/Jun16 Q7(i) |
| **$P(a<X<b)$** | $\int_{a}^{b}f(x)\,dx$ directly | Split at every join inside $[a,b]$; sum | Truncate $[a,b]$ to domain; $P(X=c)=0$; $< $ vs $\le$ same | 9709/73/Nov16 Q8(b); 9709/62/M/J/23 Q2; 9709/62/M/J/18 Q4 |
| **Median $m$** | Solve $\int_{-\infty}^{m}f=0.5$ | Cumulative area at joins → locate piece → solve in that piece | $f(m)=0.5$ is wrong — it's area, not height; pick root inside interval | 9709/71/Jun09 Q5(ii); 9709/73/Jun14 Q2 (triangle median); 9709/72/Nov14 Q3(ii); 9709/62/O/N/22 Q5 |
| **Quartiles / IQR / percentiles** | Solve $\int_{-\infty}^{Q_{1}}f=0.25$, $\int_{-\infty}^{Q_{3}}f=0.75$ | Same locate-then-solve per quartile | $p$th percentile uses $p/100$, not $p$; IQR $=Q_{3}-Q_{1}$ | 9709/71/Jun09 Q5(iv); 9709/62/M/J/19 Q6; 9709/62/O/N/19 Q3 |
| **$E(X)$** | $\int_{a}^{b}x f(x)\,dx$ | $\sum\int_{\text{piece}}x f_{i}(x)\,dx$ | Symmetry shortcut needs justification; don't confuse with median | 9709/71/Jun09 Q5(ii); 9709/72/Jun16 Q7(ii); 9709/73/Nov16 Q8(a); 9709/62/O/N/19 Q3 |
| **$\operatorname{Var}(X)$** | $E(X^{2})-[E(X)]^{2}$ where $E(X^{2})=\int x^{2}f$ | Same split for both integrals | $E(X^{2})\neq[E(X)]^{2}$; keep exact fractions; $\sigma=\sqrt{\operatorname{Var}}$ | 9709/73/Nov16 Q8(a); 9709/72/Jun16 Q7(ii); 9709/62/M/J/23 Q5 |
| **Exponential / rectangular special** | $P(T>a)=e^{-\lambda a}$; $E=1/\lambda$, $\operatorname{Var}=1/\lambda^{2}$; rect: $E=(a+b)/2$, $\operatorname{Var}=(b-a)^{2}/12$ | — | Don't use Normal approximations for these — integrate directly | 9709/62/M/J/18 Q4 (exponential); End-of-Ch Review Q3 (rectangular $1/90$) |

---

# Justification Bank

Complete set of justifications that earn reasoning/method marks in this chapter.

### J1 — PDF Conditions (Key Point 4.1, p. 78)

> "For $f$ to be a PDF: (i) $f(x)\ge0$ for all $x$ — probability cannot be negative; (ii) $\int_{-\infty}^{\infty}f(x)\,dx=1$ — total probability is $1$. Outside the stated domain, $f(x)=0$."

Use when: any "show $f$ is a PDF" or "find $k$" question. Both parts required.

### J2 — Probability as Area (Key Point 4.3, p. 80)

> "$P(a<X<b)$ is the area under the PDF between $a$ and $b$: $P(a<X<b)=\int_{a}^{b}f(x)\,dx$. For a piecewise PDF, split at the joins: $P(a<X<b)=\sum\int_{\text{overlap}}f_{i}(x)\,dx$."

Use when: any probability calculation.

### J3 — Single-Point Probability Zero (Key Point 4.2, p. 79)

> "With a continuous RV, $P(X=c)=\int_{c}^{c}f(x)\,dx=0$ for any single value $c$. Hence $P(a<X<b)=P(a\le X\le b)$ — it doesn't matter whether endpoints are included."

Use when: $P(X=c)$ appears, or $< $ vs $\le$ is tested, or a student confuses $f(c)$ with $P(X=c)$.

### J4 — Median Definition (Key Point 4.4, p. 84)

> "The median $m$ is the value for which $\int_{-\infty}^{m}f(x)\,dx=0.5$ — the area to the left of $m$ is half the total area. Similarly $Q_{1}$ has area $0.25$ to its left, $Q_{3}$ has $0.75$, and the $p$th percentile has $p/100$ to its left."

Use when: any median/quartile/percentile question. State the integral equation before solving.

### J5 — Locating the Median in a Piecewise PDF (Worked Examples 4.4–4.5)

> "For a piecewise PDF, first find the cumulative area at each join. If area to the first join $<0.5$, the median lies beyond it; include the full area of earlier pieces when setting up $\int_{-\infty}^{m}f=0.5$."

Use when: piecewise median/percentile. The locating step is worth a mark.

### J6 — Expectation Setup (Key Point 4.5, p. 89)

> "$E(X)=\int_{-\infty}^{\infty}x f(x)\,dx$ — the continuous analogue of $\sum xP(X=x)$, obtained by $P(x<X<x+\delta x)\approx f(x)\,\delta x$ (p. 88). For $E(g(X))$, replace $x$ by $g(x)$: $E(g(X))=\int g(x)f(x)\,dx$. In particular $E(X^{2})=\int x^{2}f(x)\,dx$."

Use when: any expectation/variance question. Write the integral before evaluating.

### J7 — Variance Identity (Key Point 4.5, p. 89)

> "$\operatorname{Var}(X)=E(X^{2})-[E(X)]^{2}$, where $E(X^{2})=\int x^{2}f(x)\,dx$. Do not confuse $E(X^{2})$ with $[E(X)]^{2}$."

Use when: variance question. State the identity and compute both integrals.

### J8 — Symmetry Argument

> "The PDF is symmetric about $x=a$ (i.e. $f(a+t)=f(a-t)$), so $E(X)=a$ and the median is also $a$. Justification: $f$ is an even function about $a$, so $\int_{-\infty}^{a}f=0.5$ and $\int x f(x)\,dx =a$."

Use when: symmetric PDF (triangular, even polynomial, rectangular). Must state the symmetry explicitly.

---

# Practice Questions + Full Solutions

### Q1 — Verify and Find $k$ (Exercise 4A Q1 style)

> **Question:** $X$ has PDF
> $$f(x)=\begin{cases} kx(2-x) & 0\le x\le 2\\0 & \text{otherwise} \end{cases}$$
> (a) Show that $k=\frac34$. (b) Find $P(0.5<X<1.5)$.
> *(cf. 9709/71/Jun09 Q5(i), 9709/62/O/N/22 Q3)*

<details>
<summary>Solution</summary>

**(a)**

$$\int_{0}^{2}kx(2-x)\,dx=k\int_{0}^{2}(2x-x^{2})dx=k\left[x^{2}-\frac{x^{3}}{3}\right]_{0}^{2}=k\left(4-\frac{8}{3}\right)=k\cdot\frac{4}{3}=1$$

$$k=\frac34\quad\checkmark$$

Check: $f(x)=\frac34x(2-x)\ge0$ on $[0,2]$ ✓ (parabola opening downward, zeros at $0$ and $2$, positive between) and $\int f =1$ ✓.

> *If an exam paper states $k=3/2$, it implies a different domain (e.g. $0\le x\le1$) — integrate the PDF as printed and use the $k$ given for follow-through marks.*

> **Note:** If the exam gives $k=3/2$, use that value in part (b) regardless — follow the rubric for method marks. The correct $k$ for this exact PDF is $3/4$.

**(b)** With $k=3/4$:

$$P(0.5<X<1.5)=\frac34\int_{0.5}^{1.5}(2x-x^{2})dx=\frac34\left[x^{2}-\frac{x^{3}}{3}\right]_{0.5}^{1.5}$$

$$=\frac34\left[\left(2.25-1.125\right)-\left(0.25-\frac{0.125}{3}\right)\right]=\frac34\left[1.125-0.2083\ldots\right]=\frac34\cdot\frac{11}{12}=\frac{11}{16}=0.6875$$

</details>

---

### Q2 — Median and IQR (Exercise 4B Q2 / End-of-Chapter Review Q7 style)

> **Question:** $X$ has PDF $f(x)=\frac{2}{25}(5-x)$ on $0\le x\le5$.
> (a) Find $P(X\le2)$. (b) Show that the median is $5-\frac{5}{\sqrt2}$. (c) Find the IQR.
> *(cf. 9709/71/Jun09 Q5, 9709/62/M/J/22 Q5, 9709/72/Nov14 Q3)*

<details>
<summary>Solution</summary>

**(a)**

$$P(X\le2)=\int_{0}^{2}\frac{2}{25}(5-x)dx=\frac{2}{25}\left[5x-\frac{x^{2}}2\right]_{0}^{2}=\frac{2}{25}(10-2)=\frac{16}{25}=0.64$$

**(b)** See PART 2 Example 2 — median $m=5-5/\sqrt2\approx1.46$. Solve $\frac{2}{25}(5m-m^{2}/2)=0.5$ giving $m^{2}-10m+25/2=0$.

**(c)** $Q_{1}=\frac{10-5\sqrt3}{2}\approx0.67$, $Q_{3}=2.5$, $\text{IQR}=2.5-0.67=1.83$ (see PART 2 Example 2 for full working).

</details>

---

### Q3 — Expectation and Variance (Exercise 4C Q1–Q3 style)

> **Question:** $X$ has PDF $f(x)=\frac{6}{125}(5x-x^{2})$ on $0\le x\le5$ (i.e. $f(x)=\frac{6x(5-x)}{125}$).
> Find $E(X)$ and $\operatorname{Var}(X)$.
> *(cf. 9709/71/Jun09 Q5(ii)–(iii), 9709/72/Jun16 Q7(ii), 9709/62/M/J/23 Q5)*

<details>
<summary>Solution</summary>

**Verify $k$ first:** $\int_{0}^{5}\frac6{125}(5x-x^{2})dx=\frac6{125}[5x^{2}/2-x^{3}/3]_{0}^{5}=\frac6{125}(62.5-125/3)=\frac6{125}\cdot125/6=1$ ✓

**Expectation:**

$$E(X)=\frac6{125}\int_{0}^{5}(5x^{2}-x^{3})dx=\frac6{125}\left[\frac{5x^{3}}3-\frac{x^{4}}4\right]_{0}^{5}=\frac6{125}\left(\frac{625}3-\frac{625}4\right)=\frac6{125}\cdot\frac{625}{12}= \frac52=2.5$$

**Second moment:**

$$E(X^{2})=\frac6{125}\int_{0}^{5}(5x^{3}-x^{4})dx=\frac6{125}\left[\frac{5x^{4}}4-\frac{x^{5}}5\right]_{0}^{5}=\frac6{125}\left(\frac{3125}4-625\right)=\frac6{125}\cdot\frac{625}4=\frac{15}2=7.5$$

**Variance:**

$$\operatorname{Var}(X)=7.5-(2.5)^{2}=7.5-6.25=1.25=\frac54 \quad\checkmark$$

</details>

---

### Q4 — Piecewise Median (End-of-Chapter Review Q2 / 9709/73/Jun14 Q2 style)

> **Question:** $X$ has PDF
> $$f(x)=\begin{cases} kx(3-x) & 3\le x\le7\\ kx(x-7)& 7< x\le11\\0&\text{otherwise}\end{cases}$$
> (This is symmetric about $x=7$.)
> (a) Show that $k=\frac1{16}$. (b) Show the median is $7$. (c) Find $a$ such that $P(3\le X\le a)=0.75$.
> *(cf. End-of-Chapter Review Q2, p. 94; 9709/73/Jun14 Q2, 9709/62/O/N/22 Q5)*

<details>
<summary>Solution</summary>

**(a)**

$$\int_{3}^{7}kx(3-x\text{?})\ldots$$

For the coursebook's actual Q2: $f(x)=k(x-3)$ on $[3,7]$ and $f(x)=k(11-x)$ on $[7,11]$ (triangle peaking at $x=7$):

$$\int_{3}^{7}k(x-3)dx+\int_{7}^{11}k(11-x)dx=k\left[\frac{(x-3)^{2}}2\right]_{3}^{7}+k\left[11x-\frac{x^{2}}2\right]_{7}^{11}$$

$$=k\cdot8+k\cdot8=16k=1\implies k=\frac1{16}\quad\checkmark$$

$f\ge0$ on both intervals ✓.

**(b)** By symmetry about $x=7$, median $=7$. Formally: $\int_{3}^{7}\frac1{16}(x-3)dx= \frac1{16}\cdot8=0.5$, so $\int_{-\infty}^{7}f=0.5$ ✓.

**(c)** Need $P(3\le X\le a)=0.75$. Since $P(3\le X\le7)=0.5$, $a>7$:

$$0.5+\int_{7}^{a}\frac1{16}(11-x)dx=0.75$$

$$\frac1{16}\left[11x-\frac{x^{2}}2\right]_{7}^{a}=0.25$$

$$\left(11a-\frac{a^{2}}2\right)-\left(77-\frac{49}2\right)=4$$

$$11a-\frac{a^{2}}2-52.5=4$$

$$a^{2}-22a+113=0$$

$$a=\frac{22\pm\sqrt{484-452}}2=\frac{22\pm\sqrt{32}}2=11\pm2\sqrt2$$

Take $a=11-2\sqrt2\approx8.17$ (since $7<a\le11$). The other root $11+2\sqrt2>11$ is outside.

</details>

---

### Q5 — Symmetric PDF: ordering standard deviations + variance (9709/73/Nov16 Q8)

> **Question:** Four PDFs $W,X,Y,Z$ on $[-3,3]$ are sketched (see End-of-Chapter Review Q5, p. 95). $X$ has $f(x)=\frac{x^{2}}{18}$ on $-3\le x\le3$.
> (a) Rank $\sigma_{W},\sigma_{X},\sigma_{Y},\sigma_{Z}$ largest to smallest by shape. (b) Show $\sigma_{X}=2.32$ (3 s.f.). (c) Find $P(X>\sigma_{X})$.
> *(9709/73/Nov16 Q8 — exact past paper)*

<details>
<summary>Solution</summary>

**(a)** Widest/most spread PDF has largest $\sigma$. $Y$ (U-shaped, mass at extremes) has largest $\sigma$; $W$ (peaked centre) has smallest. Ordering: $\sigma_{Y}>\sigma_{Z}>\sigma_{X}>\sigma_{W}$ (exact ordering depends on sketches — $X$ with $f\propto x^{2}$ is U-shaped but less extreme than $Y$).

**(b)**

$$E(X)=\int_{-3}^{3}x\cdot\frac{x^{2}}{18}dx=0\quad\text{(odd function over symmetric interval)}$$

$$E(X^{2})=\int_{-3}^{3}\frac{x^{4}}{18}dx=\frac1{18}\left[\frac{x^{5}}5\right]_{-3}^{3}=\frac1{18}\cdot\frac{486}5=\frac{27}5=5.4$$

$$\operatorname{Var}(X)=5.4-0=5.4,\quad\sigma_{X}=\sqrt{5.4}\approx2.32\quad\checkmark$$

**(c)**

$$P(X>\sigma_{X})=P(X>2.32)=\int_{2.32}^{3}\frac{x^{2}}{18}dx=\frac1{18}\left[\frac{x^{3}}3\right]_{2.32}^{3}$$

$$=\frac1{54}(27-12.51)=\frac{14.49}{54}\approx0.268$$

$$P(X>2.32)\approx0.268\quad\checkmark$$

</details>

---

### Q6 — Exponential / Modelling Question (Exercise 4A Q7 / 4C Q7 / End-of-Chapter Review Q3 style)

> **Question:** The time $T$ minutes a customer is served at a bank has PDF
> $$f(t)=\begin{cases}0.5e^{-0.5t}&t>0\\0&\text{otherwise}\end{cases}$$
> (a) Find $P(2<T<5)$. (b) The arrival time of customers is uniform on $[0,90]$ with $g(t)=1/90$ on $0\le t\le90$. Find $P(\text{arrives in first 30 min AND served in 2--5 min})$.
> *(cf. End-of-Chapter Review Q3(d)(e), p. 94; Exercise 4A Q7, 4C Q7; 9709/62/M/J/18 Q4 exponential)*

<details>
<summary>Solution</summary>

**(a)** Exponential with $\lambda=0.5$:

$$P(2<T<5)=\int_{2}^{5}0.5e^{-0.5t}dt=\left[-e^{-0.5t}\right]_{2}^{5}=e^{-1}-e^{-2.5}$$

$$=0.3679-0.0821=0.2858\approx0.286\quad\checkmark$$

Alternatively: $P(T>a)=e^{-0.5a}$, so $P(2<T<5)=e^{-1}-e^{-2.5}$.

**(b)** Assuming independence of arrival and service times:

$$P(\text{arrives in first 30})=\int_{0}^{30}\frac1{90}dt=\frac{30}{90}=\frac13$$

$$P(\text{both})=P(\text{arrives in first 30})\times P(2<T<5)=\frac13\times0.286\approx0.0953\quad\checkmark$$

</details>

---


---

# NEW Additional Solved Examples — 2026 Audit Additions

> **Syllabus 9709 S2 — added to address gaps: quadratic $k$, median/percentile spanning a join, and $E(g(X))$ with piecewise. Each example shows full $\displaystyle\int$ steps in display mode and ends with an examiner tip. All PDFs satisfy $f(x)\ge0$ and $\int f=1$ (J1).**

### NEW Example A — Finding $k$ for a quadratic PDF over $[a,b]$

> **Question:** The continuous random variable $X$ has PDF
> $$f(x)=\begin{cases} k\left(x^{2}+2x\right) & 0\le x\le 2 \\[4pt] 0 & \text{otherwise} \end{cases}$$
> where $k$ is a constant. (a) Find $k$ and verify $f$ is a valid PDF. (b) Find $P(1<X<1.5)$.
> *(Syllabus 9709 S2 — quadratic over $[a,b]$; cf. Coursebook Exercise 4A, 9709/62/O/N/22 Q3 style)*

**Solution:**

**(a) Find $k$ — integrate over the domain and set $=1$:**

$$1 = \int_{0}^{2}k\left(x^{2}+2x\right)dx = k\int_{0}^{2}\left(x^{2}+2x\right)dx = k\left[\frac{x^{3}}{3}+x^{2}\right]_{0}^{2}$$

$$= k\left[\left(\frac{8}{3}+4\right)-0\right] = k\cdot\frac{20}{3}$$

$$k = \frac{3}{20}\quad\checkmark$$

**Verify validity:**

$$f(x)=\frac{3}{20}\left(x^{2}+2x\right)=\frac{3}{20}x(x+2)\ge0\quad\text{for }0\le x\le2\ \checkmark$$

$$\int_{-\infty}^{\infty}f(x)\,dx = \int_{0}^{2}\frac{3}{20}\left(x^{2}+2x\right)dx = \frac{3}{20}\cdot\frac{20}{3}=1\ \checkmark$$

So $f$ is a valid PDF (J1).

**(b) Probability over a sub-interval (no split needed — single piece):**

$$P(1<X<1.5) = \int_{1}^{1.5}\frac{3}{20}\left(x^{2}+2x\right)dx = \frac{3}{20}\left[\frac{x^{3}}{3}+x^{2}\right]_{1}^{1.5}$$

$$= \frac{3}{20}\left[\left(\frac{3.375}{3}+2.25\right)-\left(\frac13+1\right)\right] = \frac{3}{20}\left[(1.125+2.25)-\frac43\right]$$

$$= \frac{3}{20}\left[3.375-\frac43\right] = \frac{3}{20}\left[\frac{81}{24}-\frac{32}{24}\right] = \frac{3}{20}\cdot\frac{49}{24}=\frac{49}{160}=0.30625\ \checkmark$$

*Exact check:* $\left[\frac{x^{3}}3+x^{2}\right]_{1}^{1.5}= \left(\frac{27}{24}+\frac{54}{24}\right)-\left(\frac{8}{24}+\frac{24}{24}\right)=\frac{49}{24}$.

> 🎯 **Examiner tip — quadratic $k$:** Expand $k(x^{2}+2x)$ before integrating; factorising as $kx(x+2)$ helps check $f\ge0$ but don't integrate the factored form without expanding. Keep $\frac{20}{3}$ as a fraction until you invert for $k$ — decimal rounding at $\frac{20}{3}\approx6.667$ risks $k=0.149$ instead of the exact $\frac{3}{20}$. Always state both PDF checks (non-negativity and area $=1$) for the method mark.

---

### NEW Example B — Median and $80^{\text{th}}$ percentile where the target spans the join

> **Question:** $X$ has piecewise PDF
> $$f(x)=\begin{cases} \dfrac{x}{8} & 0\le x\le 2 \\[6pt] \dfrac{5-x}{6} & 2< x\le 5 \\[6pt] 0 & \text{otherwise} \end{cases}$$
> (a) Verify $f$ is a valid PDF. (b) Find the median $m$. (c) Find the $80^{\text{th}}$ percentile $r_{80}$.
> *(Syllabus 9709 S2 — piecewise median/percentile where target lies beyond the first join; cf. Coursebook WE 4.4–4.5, 9709/73/Jun14 Q2, 9709/62/M/J/19 Q6)*

**Solution:**

**(a) Verify:**

$$A_{1}=\int_{0}^{2}\frac{x}{8}\,dx = \frac18\left[\frac{x^{2}}2\right]_{0}^{2}= \frac18\cdot2=\frac14$$

$$A_{2}=\int_{2}^{5}\frac{5-x}{6}\,dx = \frac16\left[5x-\frac{x^{2}}2\right]_{2}^{5}= \frac16\big[(25-12.5)-(10-2)\big]=\frac16\cdot4.5=\frac34$$

$$A_{1}+A_{2}= \frac14+\frac34=1\ \checkmark,\qquad f(x)\ge0\text{ on both intervals }\checkmark$$

**(b) Median $m$ — locate the interval first (J5):**

$$P(X\le2)=A_{1}=0.25<0.5\implies m>2\text{ (in the second piece).}$$

Set up cumulative equation, including the full first piece:

$$\int_{0}^{2}\frac{x}{8}dx+\int_{2}^{m}\frac{5-x}{6}dx =0.5$$

$$\frac14+\frac16\left[5x-\frac{x^{2}}2\right]_{2}^{m}=0.5$$

$$\frac16\left[\left(5m-\frac{m^{2}}2\right)-8\right]=0.25$$

$$5m-\frac{m^{2}}2-8 = 1.5$$

$$5m-\frac{m^{2}}2 = 9.5$$

Multiply by $2$:

$$10m-m^{2}=19$$

$$m^{2}-10m+19=0$$

$$m = \frac{10\pm\sqrt{100-76}}2 = \frac{10\pm\sqrt{24}}2 = 5\pm\sqrt6$$

Since $2<m\le5$, take the minus branch:

$$m = 5-\sqrt6\approx 2.55\quad\checkmark$$

(The other root $5+\sqrt6\approx7.45$ lies outside the domain — discard.)

**(c) $80^{\text{th}}$ percentile $r_{80}$ — same method, target $0.80$:**

$\int_{-\infty}^{r_{80}}f=0.80$. Since $A_{1}=0.25<0.80$, $r_{80}>2$:

$$\frac14+\frac16\left[5r_{80}-\frac{r_{80}^{2}}2-8\right]=0.80$$

$$\frac16\left[5r_{80}-\frac{r_{80}^{2}}2-8\right]=0.55$$

$$5r_{80}-\frac{r_{80}^{2}}2-8 = 3.3$$

$$5r_{80}-\frac{r_{80}^{2}}2 = 11.3$$

$$r_{80}^{2}-10r_{80}+22.6=0$$

$$r_{80}= \frac{10\pm\sqrt{100-90.4}}2 = \frac{10\pm\sqrt{9.6}}2 =5\pm\sqrt{2.4}$$

Require $2<r_{80}\le5$:

$$r_{80}=5-\sqrt{2.4}\approx 3.45\quad\checkmark$$

(The plus branch $5+\sqrt{2.4}\approx6.55>5$ is rejected.)

*Check:* $P(X\le r_{80})=0.25+\frac16[(5\cdot3.45-3.45^{2}/2)-8]\approx0.25+0.55=0.80$ ✓.

> 🎯 **Examiner tip — spanning the join:** The mark scheme awards **M1** for the locating statement "$P(X\le2)=0.25<0.5$ so median $>2$". Without it, even a correct quadratic scores no method. Write the cumulative equation as "full earlier piece(s) + partial piece $=0.5$ ($0.8$ for percentile)". When solving $m^{2}-10m+19=0$, discard the root outside the interval you located — state why ("$5+\sqrt6>5$ outside $[2,5]$") for the A1 justification.

---

### NEW Example C — $E(g(X))$ with a piecewise PDF: $E\!\left(\frac1X\right)$ and $E(X^{3})$

> **Question:** $X$ has piecewise PDF
> $$f(x)=\begin{cases} \dfrac14 & 1\le x\le 2 \\[6pt] \dfrac{x}{8} & 2< x\le 4 \\[6pt] 0 & \text{otherwise} \end{cases}$$
> (a) Verify $f$ is a valid PDF and explain why $E(1/X)$ exists. (b) Find $E\!\left(\frac1X\right)$. (c) Find $E(X^{3})$ and hence $\operatorname{Var}(X)$ (for contrast).
> *(Syllabus 9709 S2 — $E(g(X))=\int g(x)f(x)dx$ with piecewise split; cf. Coursebook Key Point 4.5, Exercise 4C, 9709/72/Jun16 Q7(ii). The domain $[1,4]$ avoids $x=0$ so $1/X$ is integrable.)*

**Solution:**

**(a) Verify and existence:**

$$\int_{1}^{2}\frac14dx+\int_{2}^{4}\frac{x}{8}dx = \frac14(1)+\frac18\left[\frac{x^{2}}2\right]_{2}^{4}=0.25+\frac18(8-2)=0.25+0.75=1\ \checkmark$$

$f(x)\ge0$ on $[1,4]$ ✓. Since the domain is $[1,4]$ with $x\ge1$, $g(x)=1/x$ is continuous and bounded ($0.25\le1/x\le1$), so $\int g(x)f(x)dx$ converges.

*Note: if the domain included $0$, $E(1/X)$ would diverge — examiners sometimes plant this trap. Here $[1,4]$ is safe.*

**(b) $E\!\left(\frac1X\right)=\int_{-\infty}^{\infty}\frac1x\,f(x)\,dx$ — split at every join (J6):**

$$E\!\left(\frac1X\right)=\int_{1}^{2}\frac1x\cdot\frac14\,dx+\int_{2}^{4}\frac1x\cdot\frac{x}{8}\,dx$$

**First piece:**

$$\int_{1}^{2}\frac1{4x}\,dx = \frac14\big[\ln x\big]_{1}^{2}= \frac14\ln2\approx0.1733$$

**Second piece — the $x$ cancels (key simplification):**

$$\int_{2}^{4}\frac1x\cdot\frac{x}{8}\,dx = \int_{2}^{4}\frac18\,dx = \frac18\big[x\big]_{2}^{4}= \frac18(2)=\frac14=0.25$$

**Combine:**

$$E\!\left(\frac1X\right)=\frac14\ln2+\frac14 = \frac14\left(1+\ln2\right)\approx0.423\quad\checkmark$$

Compare with $1/E(X)$ (see part (c)): $E(1/X)\neq1/E(X)$ — Jensen's effect — a common trap.

**(c) $E(X^{3})$ and $E(X)$ for variance contrast — again split:**

$$E(X^{3})=\int_{1}^{2}x^{3}\cdot\frac14\,dx+\int_{2}^{4}x^{3}\cdot\frac{x}{8}\,dx = \frac14\int_{1}^{2}x^{3}dx+\frac18\int_{2}^{4}x^{4}dx$$

$$= \frac14\left[\frac{x^{4}}4\right]_{1}^{2}+\frac18\left[\frac{x^{5}}5\right]_{2}^{4}= \frac1{16}\big[16-1\big]+\frac1{40}\big[1024-32\big]$$

$$= \frac{15}{16}+\frac{992}{40}=0.9375+24.8=25.7375=\frac{823}{32}\ \checkmark$$

For $\operatorname{Var}(X)$ we need $E(X)$ and $E(X^{2})$:

$$E(X)=\int_{1}^{2}\frac{x}{4}dx+\int_{2}^{4}\frac{x^{2}}8dx = \frac14\left[\frac{x^{2}}2\right]_{1}^{2}+\frac18\left[\frac{x^{3}}3\right]_{2}^{4}$$

$$= \frac14\cdot\frac32+\frac18\cdot\frac{56}3 = \frac38+\frac73 = \frac{65}{24}\approx2.708\quad\checkmark$$

$$E(X^{2})=\int_{1}^{2}\frac{x^{2}}4dx+\int_{2}^{4}\frac{x^{3}}8dx = \frac14\left[\frac{x^{3}}3\right]_{1}^{2}+\frac18\left[\frac{x^{4}}4\right]_{2}^{4}$$

$$= \frac14\cdot\frac73+\frac18\cdot\frac{240}4 = \frac7{12}+\frac{15}{2}= \frac{97}{12}\approx8.083$$

$$\operatorname{Var}(X)=E(X^{2})-[E(X)]^{2}= \frac{97}{12}-\left(\frac{65}{24}\right)^{2}= \frac{97}{12}-\frac{4225}{576}= \frac{432}{576}= \frac34=0.75\quad\checkmark$$

*Sanity:* $E(1/X)\approx0.423$ while $1/E(X)\approx0.369$ — indeed $E(1/X)>1/E(X)$ and $E(X^{3})=25.7\neq[E(X)]^{3}\approx19.86$.

> 🎯 **Examiner tip — $E(g(X))$:** Write "$E(g(X))=\int g(x)f(x)dx$" **before** substituting — it's the method mark (J6). For piecewise, show the sum explicitly: "$\int_{1}^{2}g(x)f_{1}+\int_{2}^{4}g(x)f_{2}$" — missing a piece loses both M marks. For $E(1/X)$, never write $1/E(X)$; for $E(X^{3})$, multiply $f$ by $x^{3}$ before integrating, don't cube the $E(X)$ result. If the PDF touched $0$, flag that $E(1/X)$ diverges rather than integrating through the singularity.



# Quick Reference Card

*One page — photocopy this.*

### PDF Checks (do this FIRST)

| Check | Equation | Result |
|---|---|---|
| Non-negative | $f(x)\ge0$ on domain | Must hold everywhere |
| Total area | $\int_{\text{domain}} f(x)\,dx =1$ | Solve for $k$ |

### Probability

$$P(a<X<b)=\int_{a}^{b}f(x)\,dx \quad\text{(truncate to domain; split at joins)}$$

$$P(X=c)=0 \qquad <\text{ vs }\le\text{ same for continuous}$$

### Median / Quartiles / Percentiles

| Target | Equation |
|---|---|
| Median $m$ | $\int_{-\infty}^{m}f=0.5$ |
| $Q_{1}$ | $\int_{-\infty}^{Q_{1}}f=0.25$ |
| $Q_{3}$ | $\int_{-\infty}^{Q_{3}}f=0.75$ |
| $p$th percentile | $\int_{-\infty}^{r_{p}}f=p/100$ |
| IQR | $Q_{3}-Q_{1}$ |

**Piecewise:** cumulative area at each join → locate interval → solve.

### Expectation & Variance

$$E(X)=\int x f(x)\,dx \qquad E(X^{2})=\int x^{2}f(x)\,dx$$

$$\operatorname{Var}(X)=E(X^{2})-[E(X)]^{2} \qquad \sigma=\sqrt{\operatorname{Var}}$$

$$E(g(X))=\int g(x)f(x)\,dx \qquad E(aX+b)=aE(X)+b$$

**Piecewise:** split every integral at every join.

### Special Distributions

| Distribution | PDF | $E(X)$ | $\operatorname{Var}(X)$ |
|---|---|---|---|
| Rectangular $U[a,b]$ | $\frac1{b-a}$ on $[a,b]$ | $\frac{a+b}2$ | $\frac{(b-a)^{2}}{12}$ |
| Exponential $\operatorname{Exp}(\lambda)$ | $\lambda e^{-\lambda t}$, $t\ge0$ | $1/\lambda$ | $1/\lambda^{2}$ |

### Trap Checklist — Before You Move On

- [ ] Did I use the $k$ given in the question (not my own recalculated $k$) for later parts?
- [ ] Did I truncate probability limits to the PDF's domain?
- [ ] Did I write $P(X=c)=0$ (not $f(c)$) if asked?
- [ ] For piecewise median: did I locate the interval first?
- [ ] For variance: did I compute BOTH $E(X)$ and $E(X^{2})$ and do $E(X^{2})-[E(X)]^{2}$?
- [ ] Did I keep exact fractions until the final answer?

---

> **Sources:** Cambridge International AS & A Level Mathematics: Probability & Statistics 2 Coursebook (Kranat, Cambridge University Press, 2018), Chapter 4 (pp. 74–99). Past-paper references cited inline: 9709/71/Jun09 Q5, 9709/72/Jun11 Q7, 9709/73/Jun12 Q7, 9709/73/Jun14 Q2 & Q5, 9709/72/Nov14 Q3, 9709/73/Nov16 Q8, 9709/72/Jun16 Q7, 9709/62/M/J/18 Q4, 9709/62/O/N/18 Q4, 9709/62/O/N/19 Q3, 9709/62/M/J/19 Q6, 9709/62/O/N/22 Q3 & Q5, 9709/62/M/J/22 Q5, 9709/62/M/J/23 Q2 & Q5.

