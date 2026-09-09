# 📊 Chapter 3: Linear Combinations of Random Variables — 9709 S2

> **Rule → Method Table → Justification → 4 Examples (all via Question) → Watch Out**

---

## How To Use This Chapter — 5 Steps

| Step | Action | What You Do |
|------|--------|-------------|
| **1. RULE** | Read the boxed LaTeX rule | Memorise the exact formula — every sign and square matters |
| **2. WHEN / JUSTIFICATION** | Check the blue Justification Box | Ask: *does this need independence? Is E always additive?* |
| **3. METHOD TABLE** | Follow Step \| What To Do | Execute the mechanical steps in order — do not skip scaling |
| **4. 4 EXAMPLES** | Each is a Question with full `$$` solution | Easy (coursebook) → Medium (past paper) → Hard (3 vars / \(aX+bY\)) → Trap (variance vs SD, \(2X\) vs \(X_1+X_2\)) |
| **5. WATCH OUT!** | Read the red box last | This is where 80% of marks are lost — check before moving on |

> **Syllabus coverage:** 9709 S2 §3.1–3.4. Linear combinations of any RV (discrete or continuous), including normal and Poisson cases. Every result assumes you can already find \(\mathrm{E}(X)\), \(\mathrm{Var}(X)\) for binomial / normal / Poisson.

---

# PART 1: Expectation and Variance — \(aX+b\)

Single-variable linear transformation. The workhorse for converting units, shifting distributions, and cost/totals questions.

## 1.1 Rule — Scaling and Shifting One Variable

$$\boxed{\mathrm{E}(aX+b) = a\,\mathrm{E}(X) + b}$$

$$\boxed{\mathrm{Var}(aX+b) = a^{2}\,\mathrm{Var}(X) \qquad \mathrm{SD}(aX+b)=|a|\,\mathrm{SD}(X)}$$

For \(a=1\): \(\mathrm{E}(X+b)=\mathrm{E}(X)+b\) and \(\mathrm{Var}(X+b)=\mathrm{Var}(X)\) — adding a constant shifts the mean but does **not** change spread.

For \(b=0\): \(\mathrm{E}(aX)=a\mathrm{E}(X)\) and \(\mathrm{Var}(aX)=a^{2}\mathrm{Var}(X)\).

> **Justification Box — When Does This Hold?**
> *Always.* No independence condition needed — this is a single random variable. The \(a^{2}\) appears because variance is \(\mathrm{E}[(X-\mu)^2]\); scaling \(X\) by \(a\) scales deviations by \(a\), so squared deviations scale by \(a^{2}\). Adding \(b\) cancels in \((X+b)-(\mu+b)=X-\mu\).
> Proof sketch: \(\mathrm{Var}(aX+b)=\mathrm{E}[(aX+b-(a\mu+b))^2]=\mathrm{E}[a^{2}(X-\mu)^2]=a^{2}\mathrm{Var}(X)\).

### Method Table — \(aX+b\) Problems

| Step | What To Do | Formula / Check |
|------|------------|----------------|
| 1 | Identify \(\mathrm{E}(X)\) and \(\mathrm{Var}(X)\) | From table, binomial \(np, npq\), given, or calculate \(\sum xP(x)\) |
| 2 | \(\mathrm{E}(aX+b)\) | \(a\mathrm{E}(X)+b\) — multiply **then** add |
| 3 | \(\mathrm{Var}(aX+b)\) | \(a^{2}\mathrm{Var}(X)\) — **square \(a\)**, ignore \(b\) entirely |
| 4 | If asked for SD | \(\sqrt{\mathrm{Var}}\) — then apply \(\lvert a\rvert\) if you combine steps |
| 5 | Units check | \(\mathrm{E}\) has same units as \(X\); \(\mathrm{Var}\) has units\(^2\) |

---

### Example 1 — Easy (Coursebook Worked Example 3.1)

> **Question:** The random variable \(X\) has distribution:
>
> | \(x\) | 2 | 3 | 5 | 7 |
> |-------|---|---|---|---|
> | \(P(X=x)\) | 0.4 | 0.1 | 0.3 | 0.2 |
>
> Find (a) \(\mathrm{E}(2X+3)\) and (b) \(\mathrm{Var}(2X+3)\).

**Solution:**

First compute \(\mathrm{E}(X)\) and \(\mathrm{Var}(X)\):

$$\mathrm{E}(X) = 2(0.4)+3(0.1)+5(0.3)+7(0.2) = 0.8+0.3+1.5+1.4 = 4.0$$

$$\mathrm{E}(X^{2}) = 4(0.4)+9(0.1)+25(0.3)+49(0.2) = 1.6+0.9+7.5+9.8 = 19.8$$

$$\mathrm{Var}(X) = \mathrm{E}(X^{2})-[\mathrm{E}(X)]^{2} = 19.8 - 16 = 3.8$$

(a)

$$\mathrm{E}(2X+3) = 2\mathrm{E}(X)+3 = 2(4.0)+3 = 11$$

(b)

$$\mathrm{Var}(2X+3) = 2^{2}\mathrm{Var}(X) = 4 \times 3.8 = 15.2$$

**Examiner tip:** State \(\mathrm{E}(X)\) and \(\mathrm{Var}(X)\) first — method marks even if arithmetic slips.

---

### Example 2 — Medium (Past Paper — 9709/62/M/J/23 Q2 adapted)

> **Question:** The random variable \(X \sim \mathrm{B}(25, 0.6)\). Find (a) \(\mathrm{E}(5X-1)\) (b) \(\mathrm{Var}(5X-1)\). [9709/62/M/J/23 Q2]

**Solution:**

For \(X\sim\mathrm{B}(n,p)\): \(\mathrm{E}(X)=np\), \(\mathrm{Var}(X)=np(1-p)\)

$$\mathrm{E}(X)=25\times0.6=15$$

$$\mathrm{Var}(X)=25\times0.6\times0.4=6.0$$

(a)

$$\mathrm{E}(5X-1)=5\mathrm{E}(X)-1=5(15)-1=74$$

(b)

$$\mathrm{Var}(5X-1)=5^{2}\mathrm{Var}(X)=25\times6=150$$

$$\therefore \mathrm{SD}(5X-1)=\sqrt{150}=12.247\ldots\approx 12.2$$

---

### Example 3 — Hard (Scaling + shifting with unknown constants — 9709/62/O/N/22 Q3 style)

> **Question:** The random variable \(X\) has \(\mathrm{E}(X)=2.4\) and \(\mathrm{Var}(X)=0.8\). Find two pairs \((a,b)\) such that \(\mathrm{E}(aX+b)=3.2\) and \(\mathrm{Var}(aX+b)=20\). Hence show there are infinitely many solutions if only the mean condition is required.

**Solution:**

Mean condition:

$$a\mathrm{E}(X)+b=3.2 \implies 2.4a+b=3.2 \implies b=3.2-2.4a$$

Variance condition:

$$a^{2}\mathrm{Var}(X)=20 \implies a^{2}(0.8)=20 \implies a^{2}=25 \implies a=\pm 5$$

Case 1: \(a=5\)

$$b=3.2-2.4(5)=3.2-12=-8.8$$

$$\therefore (a,b)=(5,-8.8) \implies \mathrm{E}(5X-8.8)=3.2,\ \mathrm{Var}(5X-8.8)=20\checkmark$$

Case 2: \(a=-5\)

$$b=3.2-2.4(-5)=3.2+12=15.2$$

$$\therefore (a,b)=(-5,15.2) \implies \mathrm{E}(-5X+15.2)=3.2,\ \mathrm{Var}(-5X+15.2)=25\times0.8=20\checkmark$$

If only \(\mathrm{E}(aX+b)=3.2\) required, any \(a\) gives \(b=3.2-2.4a\) — infinite line of solutions. The variance condition fixes \(|a|\).

---

### Example 4 — Trap (Var(aX) vs a·Var(X) — the \(a^{2}\) trap)

> **Question [TRAP]:** A student writes: "If \(\mathrm{Var}(X)=4\) then \(\mathrm{Var}(3X)=12\) and \(\mathrm{Var}(X+5)=9\)." Identify both errors and give the correct values. Explain the misconception.

**Solution:**

Error 1: \(\mathrm{Var}(3X) \neq 3\mathrm{Var}(X)\)

$$\mathrm{Var}(3X)=3^{2}\mathrm{Var}(X)=9\times4=36 \neq 12$$

The student multiplied by \(a\) instead of \(a^{2}\). Variance is in squared units — scaling \(X\) by 3 scales squared deviations by 9.

Error 2: \(\mathrm{Var}(X+5)\neq \mathrm{Var}(X)+5\)

$$\mathrm{Var}(X+5)=\mathrm{Var}(X)=4 \neq 9$$

The student added the constant to the variance. Adding a constant shifts every value and the mean equally: \((X+5)-(\mu+5)=X-\mu\), so spread is unchanged.

Correct:

$$\boxed{\mathrm{Var}(3X)=36,\qquad \mathrm{Var}(X+5)=4,\qquad \mathrm{SD}(3X+5)=3\times2=6}$$

> ⭐ **Watch Out! — PART 1**
> - **ALWAYS square \(a\) in variance:** \(\mathrm{Var}(aX)=a^{2}\mathrm{Var}(X)\), even if \(a\) is negative: \(\mathrm{Var}(-2X)=4\mathrm{Var}(X)\).
> - **Ignore \(b\) in variance:** \(\mathrm{Var}(X+b)=\mathrm{Var}(X)\) for any constant \(b\).
> - **SD scales by \(|a|\):** \(\mathrm{SD}(aX+b)=|a|\mathrm{SD}(X)\) — don't square-root incorrectly.
> - **Exam trap:** \(2X\) vs \(X_{1}+X_{2}\) preview — \(\mathrm{Var}(2X)=4\mathrm{Var}(X)\) but \(\mathrm{Var}(X_{1}+X_{2})=2\mathrm{Var}(X)\) (see Part 2). If question says "two independent observations", it's the sum, not the double.

---

# PART 2: Sum and Difference of Independent Random Variables

The central results for combining **different** (or independent repeated) random variables.

## 2.1 Rules — Mean Additive Always, Variance Additive iff Independent

For **any** random variables \(X, Y\) (no independence needed):

$$\boxed{\mathrm{E}(X+Y)=\mathrm{E}(X)+\mathrm{E}(Y) \qquad \mathrm{E}(X-Y)=\mathrm{E}(X)-\mathrm{E}(Y)}$$

For **independent** \(X, Y\):

$$\boxed{\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)}$$

$$\boxed{\mathrm{Var}(X-Y)=\mathrm{Var}(X)+\mathrm{Var}(Y) \quad \text{(still ADD!)}}$$

For linear combination with constants \(a,b\) and independent \(X,Y\):

$$\boxed{\mathrm{E}(aX+bY)=a\mathrm{E}(X)+b\mathrm{E}(Y)}$$

$$\boxed{\mathrm{Var}(aX+bY)=a^{2}\mathrm{Var}(X)+b^{2}\mathrm{Var}(Y)}$$

$$\boxed{\mathrm{Var}(aX-bY)=a^{2}\mathrm{Var}(X)+b^{2}\mathrm{Var}(Y) \quad \text{(still ADD!)}}$$

Extension to \(n\) independent variables: \(\mathrm{Var}(\sum a_i X_i)=\sum a_i^{2}\mathrm{Var}(X_i)\).

> **Justification Box — Why Does Variance ADD for a Difference?**
> *Expectation is always additive* because \(\mathrm{E}\) is linear: \(\mathrm{E}(X\pm Y)=\sum (x\pm y)P =\sum xP \pm \sum yP =\mathrm{E}(X)\pm\mathrm{E}(Y)\) even when dependent.
> *Variance is additive only when independent* because \(\mathrm{Var}(X\pm Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)\pm2\mathrm{Cov}(X,Y)\). If \(X,Y\) independent, \(\mathrm{Cov}(X,Y)=0\), so the \(\pm2\mathrm{Cov}\) term vanishes in **both** cases. Hence \(\mathrm{Var}(X-Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)\) — you **add** variances even when subtracting variables. If dependent, you need covariance and this formula fails — syllabus always states "independent".

### Method Table — \(aX \pm bY\) Problems

| Step | What To Do | Detail |
|------|------------|--------|
| 1 | Check independence stated? | Must say "independent" for variance addition. If not stated, you cannot add variances |
| 2 | Identify \(\mathrm{E}(X),\mathrm{Var}(X),\mathrm{E}(Y),\mathrm{Var}(Y)\) | From given or binomial/normal/Poisson formulas |
| 3 | \(\mathrm{E}(aX\pm bY)\) | \(a\mathrm{E}(X)\pm b\mathrm{E}(Y)\) — signs follow directly |
| 4 | \(\mathrm{Var}(aX\pm bY)\) | \(a^{2}\mathrm{Var}(X)+b^{2}\mathrm{Var}(Y)\) — **ADD** even for minus, **SQUARE** each coefficient |
| 5 | Crucial distinction | \(aX\) with one observation vs \(X_1+X_2+\dots\) with \(n\) independent observations. Former: \(a^{2}\mathrm{Var}\); latter: \(n\mathrm{Var}\) |
| 6 | If asked for SD of combo | \(\sqrt{a^{2}\mathrm{Var}(X)+b^{2}\mathrm{Var}(Y)}\) — don't add SDs directly |

---

### Example 1 — Easy (Coursebook Didactic — Green & Blue Dice Sum)

> **Question:** Let \(G\) be score on green tetrahedral die (1,1,2,3) with \(\mathrm{E}(G)=\tfrac74,\ \mathrm{Var}(G)=\tfrac{11}{16}\) and \(B\) be score on blue die (1,1,2,2) with \(\mathrm{E}(B)=\tfrac32,\ \mathrm{Var}(B)=\tfrac14\). \(G\) and \(B\) are independent. Let \(W=G+B\). Find \(\mathrm{E}(W)\) and \(\mathrm{Var}(W)\). Verify by enumerating.

**Solution:**

By linearity of expectation (no independence needed for mean):

$$\mathrm{E}(W)=\mathrm{E}(G+B)=\mathrm{E}(G)+\mathrm{E}(B)=\frac{7}{4}+\frac{3}{2}=\frac{7}{4}+\frac{6}{4}=\frac{13}{4}=3.25$$

Since \(G,B\) independent, variances add:

$$\mathrm{Var}(W)=\mathrm{Var}(G+B)=\mathrm{Var}(G)+\mathrm{Var}(B)=\frac{11}{16}+\frac{1}{4}=\frac{11}{16}+\frac{4}{16}=\frac{15}{16}=0.9375$$

Verification by enumeration gives probability table for \(W\): \(P(W=2)=\tfrac14,\ P(W=3)=\tfrac38,\ P(W=4)=\tfrac14,\ P(W=5)=\tfrac18\) → \(\mathrm{E}(W)=3.25,\ \mathrm{Var}(W)=0.9375\) ✓

---

### Example 2 — Medium (Past Paper — 9709/62/F/M/24 Q3 / 9709/62/M/J/22 Q4 style)

> **Question:** Independent random variables \(X\sim\mathrm{B}(20,0.3)\) and \(Y\sim\mathrm{B}(12,0.4)\). Find (a) \(\mathrm{E}(2X-Y)\) (b) \(\mathrm{Var}(2X-Y)\). [Ref: 9709/62/M/J/22 Q4 adapted]

**Solution:**

$$\mathrm{E}(X)=20\times0.3=6,\qquad \mathrm{Var}(X)=20\times0.3\times0.7=4.2$$

$$\mathrm{E}(Y)=12\times0.4=4.8,\qquad \mathrm{Var}(Y)=12\times0.4\times0.6=2.88$$

(a)

$$\mathrm{E}(2X-Y)=2\mathrm{E}(X)-\mathrm{E}(Y)=2(6)-4.8=7.2$$

(b) — independence ⇒ add variances, square coefficients:

$$\mathrm{Var}(2X-Y)=2^{2}\mathrm{Var}(X)+(-1)^{2}\mathrm{Var}(Y)=4(4.2)+1(2.88)=16.8+2.88=19.68$$

Note sign disappears: \(\mathrm{Var}(2X-Y)=\mathrm{Var}(2X+Y)=19.68\). The minus matters for mean, not variance.

---

### Example 3 — Hard (Three independent variables — 9709/63/M/J/21 Q7 / 9709/62/O/N/21 Q6 style)

> **Question:** Independent random variables \(A,B,C\) have means \(4, 9, 7\) and variances \(1, 2, 1.3\) respectively. Find (a) \(\mathrm{E}(A+B+C)\) and \(\mathrm{Var}(A+B+C)\) (b) \(\mathrm{E}(3A-B+2C)\) and \(\mathrm{Var}(3A-B+2C)\). [9709/63/M/J/21 Q7]

**Solution:**

(a)

$$\mathrm{E}(A+B+C)=\mathrm{E}(A)+\mathrm{E}(B)+\mathrm{E}(C)=4+9+7=20$$

$$\mathrm{Var}(A+B+C)=\mathrm{Var}(A)+\mathrm{Var}(B)+\mathrm{Var}(C)=1+2+1.3=4.3$$

(b)

$$\mathrm{E}(3A-B+2C)=3\mathrm{E}(A)-\mathrm{E}(B)+2\mathrm{E}(C)=3(4)-9+2(7)=12-9+14=17$$

$$\mathrm{Var}(3A-B+2C)=3^{2}\mathrm{Var}(A)+(-1)^{2}\mathrm{Var}(B)+2^{2}\mathrm{Var}(C)$$

$$=9(1)+1(2)+4(1.3)=9+2+5.2=16.2$$

Extension principle holds for any number: \(\mathrm{Var}(A+B+C+...)=\sum \mathrm{Var}\).

---

### Example 4 — Trap (\(2X\) vs \(X_1+X_2\) — the classic distinction)

> **Question [TRAP]:** \(X\) has \(\mathrm{E}(X)=4,\ \mathrm{Var}(X)=3\). \(X_1, X_2\) are two **independent observations** of \(X\).
> (a) Find \(\mathrm{E}(2X)\) and \(\mathrm{Var}(2X)\).
> (b) Find \(\mathrm{E}(X_1+X_2)\) and \(\mathrm{Var}(X_1+X_2)\).
> (c) A student claims "\(2X\) and \(X_1+X_2\) are the same." Explain the error with a dice example.

**Solution:**

(a) Single observation scaled by 2:

$$\mathrm{E}(2X)=2\mathrm{E}(X)=8$$

$$\mathrm{Var}(2X)=2^{2}\mathrm{Var}(X)=4\times3=12$$

(b) Sum of two independent observations:

$$\mathrm{E}(X_1+X_2)=\mathrm{E}(X_1)+\mathrm{E}(X_2)=4+4=8$$

$$\mathrm{Var}(X_1+X_2)=\mathrm{Var}(X_1)+\mathrm{Var}(X_2)=3+3=6$$

Same mean (\(8\)), **different variance** (\(12\neq6\)) — not the same RV.

(c) Dice intuition: Roll Xing's die (1,1,2,2,2,4) once and double the score → possible values \(\{2,4,8\}\) with variance \(4\). Roll it twice and add → possible values \(\{2,3,4,5,6,8\}\) with many more outcomes, mean same but spread halved. \(2X\) is perfectly correlated with itself; \(X_1, X_2\) are independent.

> **Trap check:** If question says "two independent values/observations/readings", use \(X_1+X_2\) (add variances). If it says "twice the value" or \(2X\) or "double", use \(4\mathrm{Var}(X)\).

> ⭐ **Watch Out! — PART 2**
> - **\(\mathrm{Var}(X-Y) = \mathrm{Var}(X)+\mathrm{Var}(Y)\)** — the most marked wrong answer in S2 is \(\mathrm{Var}(X)-\mathrm{Var}(Y)\) (the examiner report calls this "fundamental error"). Variances are always added when combining independent RVs.
> - **Square before adding:** \(\mathrm{Var}(3X-2Y)=9\mathrm{Var}(X)+4\mathrm{Var}(Y)\), not \(3\mathrm{Var}(X)\pm2\mathrm{Var}(Y)\).
> - **Expectation is always +/-:** \(\mathrm{E}(X-Y)=\mathrm{E}(X)-\mathrm{E}(Y)\) — sign follows subtraction. Don't add means when subtracting.
> - **Standard deviations do NOT add:** \(\mathrm{SD}(X+Y)\neq \mathrm{SD}(X)+\mathrm{SD}(Y)\). Always go via variances: \(\mathrm{SD}=\sqrt{\mathrm{Var}(X)+\mathrm{Var}(Y)}\).
> - **\(X_1+X_2\) vs \(2X\):** Flag wording — "sum of two independent observations" \(\to 2\mathrm{Var}(X)\); "twice \(X\)" \(\to 4\mathrm{Var}(X)\).

---

# PART 3: Working with Normal Distributions — Linear Combinations Remain Normal

## 3.1 Rules — Normality Preserved Under Linear Combinations

$$\boxed{\text{If } X\sim\mathrm{N}(\mu,\sigma^{2}) \text{ then } aX+b \sim \mathrm{N}(a\mu+b,\; a^{2}\sigma^{2})}$$

$$\boxed{\text{If } X\sim\mathrm{N}(\mu_X,\sigma_X^{2}),\ Y\sim\mathrm{N}(\mu_Y,\sigma_Y^{2}) \text{ independent, then } aX+bY \sim \mathrm{N}(a\mu_X+b\mu_Y,\; a^{2}\sigma_X^{2}+b^{2}\sigma_Y^{2})}$$

Similarly \(aX-bY\sim\mathrm{N}(a\mu_X-b\mu_Y,\; a^{2}\sigma_X^{2}+b^{2}\sigma_Y^{2})\) — still add variances.

Once you have the new normal's \(\mu_{\text{new}},\sigma_{\text{new}}^{2}\), standardise:

$$\boxed{Z=\frac{W-\mu_{\text{new}}}{\sigma_{\text{new}}}\sim\mathrm{N}(0,1) \implies P(W<k)=\Phi\!\left(\frac{k-\mu_{\text{new}}}{\sigma_{\text{new}}}\right)}$$

> **Justification Box — Why Normal Stays Normal?**
> Linear combinations of independent normals are normal because the moment-generating function of a normal is exponential-quadratic, and products of such MGFs remain exponential-quadratic. Intuitively: the normal is stable under addition. **Conditions:** Each original must be normal AND they must be independent. If \(X\) is binomial/Poisson, \(aX+bY\) is NOT normal (though it may be *approximated* by normal for large parameters — that's a different chapter). The variance formula still needs independence.

### Method Table — Normal Linear Combination Probability

| Step | What To Do | Formula |
|------|------------|---------|
| 1 | Identify each \(X\sim\mathrm{N}(\mu,\sigma^{2})\) | Extract \(\mu,\sigma^{2}\) — note whether given as variance or SD (SD\(^2\) = variance) |
| 2 | Form the combination \(W=aX\pm bY\) (or \(3H\), \(Y-3X\), etc.) | Write \(W\) symbolically before numbers |
| 3 | \(\mu_W = a\mu_X \pm b\mu_Y\) | Means combine with same signs as \(W\) |
| 4 | \(\sigma^{2}_W = a^{2}\sigma^{2}_X + b^{2}\sigma^{2}_Y\) | **Always add, squares on coefficients** |
| 5 | State new distribution | \(W\sim\mathrm{N}(\mu_W,\sigma^{2}_W)\) — full marks require this line |
| 6 | Standardise for required probability | \(Z=\frac{k-\mu_W}{\sigma_W}\), look up \(\Phi(z)\) — sketch bell curve to check tail |
| 7 | Distinguish \(nX\) vs \(\sum X_i\) | \(3X\sim\mathrm{N}(3\mu,9\sigma^{2})\); \(X_1+X_2+X_3\sim\mathrm{N}(3\mu,3\sigma^{2})\) |

---

### Example 1 — Easy (Coursebook Worked Example 3.6 — Rice Bags)

> **Question:** Small rice bag mass \(X\sim\mathrm{N}(2.1,0.2^{2})\), large bag \(Y\sim\mathrm{N}(6.6,0.4^{2})\), independent. Find the probability that a randomly chosen large bag is heavier than three small bags. (Coursebook Ex 3.6)

**Solution:**

We need \(P(Y>3X)=P(Y-3X>0)\). Define \(W=Y-3X\).

$$\mathrm{E}(W)=\mathrm{E}(Y)-3\mathrm{E}(X)=6.6-3(2.1)=6.6-6.3=0.3$$

$$\mathrm{Var}(W)=\mathrm{Var}(Y)+(-3)^{2}\mathrm{Var}(X)=0.4^{2}+9(0.2^{2})=0.16+9(0.04)=0.16+0.36=0.52$$

$$\therefore W=Y-3X\sim\mathrm{N}(0.3,\ 0.52),\qquad \sigma_W=\sqrt{0.52}=0.7211$$

Standardise at \(0\):

$$P(W>0)=P\!\left(Z>\frac{0-0.3}{\sqrt{0.52}}\right)=P\!\left(Z>\frac{-0.3}{0.721}\right)=P(Z>-0.416)$$

$$=1-\Phi(-0.416)=\Phi(0.416)$$

$$=\Phi(0.42)\approx 0.6628 \quad\text{(tables: }0.661\text{–}0.663\text{ depending on interpolation)}$$

More precisely \(\Phi(0.416)=0.661\) (3 s.f. \(0.661\)).

---

### Example 2 — Medium (Past Paper — 9709/62/O/N/23 Q5 / 9709/62/M/J/23 Q5)

> **Question:** The masses of large and small bags of flour are \(L\sim\mathrm{N}(1010,10^{2})\) and \(S\sim\mathrm{N}(504,8^{2})\) grams, independent. Find the probability that the mass of a randomly chosen large bag is more than twice the mass of a randomly chosen small bag. [9709/End-of-chapter Review 3 Q4 — 9709/62/O/N/23 Q5 style]

**Solution:**

Need \(P(L>2S)=P(L-2S>0)\). Let \(W=L-2S\).

$$\mu_W=1010-2(504)=1010-1008=2$$

$$\sigma^{2}_W=10^{2}+(-2)^{2}\times8^{2}=100+4\times64=100+256=356$$

$$\sigma_W=\sqrt{356}=18.867\ldots$$

$$W\sim\mathrm{N}(2,\ 356)$$

$$P(W>0)=P\!\left(Z>\frac{0-2}{18.867}\right)=P(Z>-0.1060)=\Phi(0.106)$$

$$=\Phi(0.11)\approx 0.5438 \approx 0.544$$

Interpretation: only just over half the time will \(L>2S\) since \(\mu_L\approx2\mu_S\).

---

### Example 3 — Hard (Sum of \(n\) independent normals + scaling confusion — 9709/73/Q4 Nov 2010 / 9709/62/O/N/22 Q6)

> **Question:** Conti battery lifetime \(C\sim\mathrm{N}(25,1.1^{2})\), Thrift battery \(T\sim\mathrm{N}(7,2.3^{2})\), independent.
> (a) Four independent Thrift batteries are bought. Let \(S\) be their total lifetime. Find \(\mathrm{E}(S),\mathrm{Var}(S)\) and \(P(S>30)\).
> (b) Find \(P(C>4T)\). Explain why this differs from \(P(C>T_1+T_2+T_3+T_4)\). [9709 Worked Example 3.7 — 9709/73/Nov16 Q3]

**Solution:**

(a) \(S=T_1+T_2+T_3+T_4\) — sum of 4 i.i.d. normals, NOT \(4T\).

$$\mathrm{E}(S)=4\mathrm{E}(T)=4\times7=28$$

$$\mathrm{Var}(S)=4\mathrm{Var}(T)=4\times2.3^{2}=4\times5.29=21.16$$

$$\sigma_S=\sqrt{21.16}=4.6$$

$$S\sim\mathrm{N}(28,21.16)$$

$$P(S>30)=P\!\left(Z>\frac{30-28}{4.6}\right)=P(Z>0.4348)=1-\Phi(0.435)$$

$$=1-0.668=0.332$$

(b) \(W=C-4T\) — here \(4T\) means 4 times one Thrift battery (single observation scaled):

$$\mathrm{E}(W)=\mathrm{E}(C)-4\mathrm{E}(T)=25-28=-3$$

$$\mathrm{Var}(W)=\mathrm{Var}(C)+(-4)^{2}\mathrm{Var}(T)=1.1^{2}+16\times2.3^{2}=1.21+16\times5.29=1.21+84.64=85.85$$

$$W\sim\mathrm{N}(-3,85.85),\quad \sigma_W=9.265$$

$$P(C>4T)=P(W>0)=P\!\left(Z>\frac{0-(-3)}{9.265}\right)=P(Z>0.324)=1-\Phi(0.324)=1-0.627=0.373$$

Difference from (a): \(T_1+T_2+T_3+T_4\sim\mathrm{N}(28,21.16)\) has variance \(4\sigma^{2}=21.16\); whereas \(4T\sim\mathrm{N}(28,16\sigma^{2}=84.64)\) has **four times larger** variance. So \(P(C>4T)=0.373\) vs \(P(C>S)=P(C-(T_1+\dots+T_4)>0)\) would have \(\mathrm{Var}=1.21+21.16=22.37\), giving \(P\approx0.263\) — different.

> Hard distinction — circle the phrase "four randomly chosen" vs "four times".

---

### Example 4 — Trap (Variance vs Standard Deviation — Gift Package)

> **Question [TRAP]:** Soap bar mass \(S\sim\mathrm{N}(50,4)\) — student reads "4" as standard deviation instead of variance. Packaging \(T\sim\mathrm{N}(90,25)\). Gift package has 3 bars + packaging. Student computes total variance as \(3\times4+25=37\) and SD as 6.08. Identify all errors and find the correct \(P(\text{package}<250\text{g})\). [Coursebook Worked Example 3.9]

**Solution:**

Errors:
1. **Variance vs SD:** \(S\sim\mathrm{N}(50,4)\) means variance \(=4\) (since second parameter is variance in 9709). If misread as SD, you square incorrectly. Correct: \(\mathrm{Var}(S)=4\), \(\mathrm{SD}(S)=2\).
2. **\(3S\) vs \(S_1+S_2+S_3\):** "3 bars" means 3 independent bars, not 3× one bar. So use sum of 3 i.i.d., not scaling.

Correct (independent bars):

$$W=S_1+S_2+S_3+T$$

$$\mathrm{E}(W)=3(50)+90=240$$

$$\mathrm{Var}(W)=3\mathrm{Var}(S)+\mathrm{Var}(T)=3(4)+25=12+25=37$$

$$\mathrm{SD}(W)=\sqrt{37}=6.082\ldots$$

Wait — numerically same as student's error? The student got 37 by luck (\(3\times4\) coincidentally equals \(3\times4\) but via wrong reasoning \(3\times4\) as \(3\mathrm{Var}(S)\) vs correct \(3\mathrm{Var}(S)\) also gives 12 — but if they had done \(3S\) they'd get \(9\times4=36\), variance \(36+25=61\)). The trap is: **if student wrote \(3S\) instead of sum, they'd get 61**. Exam penalises that.

Now probability:

$$W\sim\mathrm{N}(240,37)$$

$$P(W<250)=P\!\left(Z<\frac{250-240}{\sqrt{37}}\right)=P\!\left(Z<\frac{10}{6.082}\right)=P(Z<1.644)$$

$$=\Phi(1.644)=0.950 \approx 0.950$$

If student had used \(W=3S+T\) incorrectly:

$$W_{\text{wrong}}\sim\mathrm{N}(240,61),\quad P(W_{\text{wrong}}<250)=\Phi(10/\sqrt{61})=\Phi(1.28)=0.900$$ — 5% error, loses A1.

> **Lesson:** Always translate "3 bars" → \(S_1+S_2+S_3\) (add 3 variances), not \(3S\) (multiply variance by 9).

> ⭐ **Watch Out! — PART 3**
> - **Read the parameter:** In 9709, \(\mathrm{N}(\mu,\sigma^{2})\) — second value is **variance**. If question says "standard deviation 5", variance is \(25\). Show \(\sigma^{2}=...\) explicitly.
> - **Add variances for BOTH sum and difference** — \(Y-3X\) variance is \(+9\mathrm{Var}(X)\), not minus.
> - **State the new normal:** Write "\(W\sim\mathrm{N}(..., ...)\)" — it's a method mark. Then standardise.
> - **\(n\) independent vs \(nX\):** "Total of \(n\) items" = sum of \(n\) i.i.d. → \(\mu_{\text{sum}}=n\mu\), \(\sigma^{2}_{\text{sum}}=n\sigma^{2}\). " \(n\) times a measurement" = scaled → \(\mu=n\mu\), \(\sigma^{2}=n^{2}\sigma^{2}\).
> - **Sketch the tail:** Before looking up, check sign: is the \(z\) positive/negative? Which tail do you need? Draw to avoid \(1-\Phi\) errors.

---

# PART 4: Linear Combinations of Poisson Distributions

## 4.1 Rule — Sum of Independent Poissons is Poisson (Scaled/Mixed is NOT)

$$\boxed{\text{If } X\sim\mathrm{Po}(\lambda),\; Y\sim\mathrm{Po}(\mu) \text{ independent, then } X+Y\sim\mathrm{Po}(\lambda+\mu)}$$

Extension: \(X_1+\dots+X_n\sim\mathrm{Po}(\lambda_1+\dots+\lambda_n)\) if all independent Poissons.

$$\boxed{\mathrm{E}(X+Y)=\lambda+\mu,\quad \mathrm{Var}(X+Y)=\lambda+\mu \quad (\text{mean}=\text{variance})}$$

What is **NOT** Poisson:

$$\boxed{aX \not\sim \mathrm{Po}(a\lambda)\quad\text{and}\quad X-Y \not\sim \mathrm{Po}(\lambda-\mu)\quad\text{and}\quad 2X \not\sim \mathrm{Po}(2\lambda)}$$

These have \(\mathrm{E}\neq\mathrm{Var}\) (e.g. \(\mathrm{E}(2X)=2\lambda\) but \(\mathrm{Var}(2X)=4\lambda\)), so they fail the Poisson condition. For scaled/differenced you must compute mean and variance via Part 2 rules and note "not Poisson".

> **Justification Box — When Does Poisson Addition Hold?**
> Two conditions **both** required:
> 1. Each variable is Poisson (events occur singly, at random, independently, at constant rate).
> 2. Variables are **independent** of each other.
> Then counting combined events still satisfies Poisson criteria — rate simply adds. Proof via PGF: \(G_{X+Y}(t)=G_X(t)G_Y(t)=e^{-\lambda(1-t)}e^{-\mu(1-t)}=e^{-(\lambda+\mu)(1-t)}\), PGF of \(\mathrm{Po}(\lambda+\mu)\).
> If you scale (\(2X\)), events are no longer counted singly / independence fails for the doubled count, so not Poisson. Difference \(X-Y\) can be negative — Poisson cannot.

### Method Table — Poisson Combination Problems

| Step | What To Do | Formula |
|------|------------|---------|
| 1 | Are both Poissons and independent? | If yes → sum is Poisson with sum of lambdas. If involves scaling/subtraction → not Poisson, use E/Var rules |
| 2 | Sum case: identify \(\lambda_{\text{new}}=\lambda+\mu\) | \(X+Y\sim\mathrm{Po}(\lambda+\mu)\) — state it |
| 3 | Then \(P(X+Y=k)=e^{-\lambda_{\text{new}}}\lambda_{\text{new}}^{k}/k!\) | Use Poisson formula with new lambda |
| 4 | Scaled/difference case: compute | \(\mathrm{E}(aX+bY)=a\lambda+b\mu\) but \(\mathrm{Var}(aX+bY)=a^{2}\lambda+b^{2}\mu\) — check \(\mathrm{E}\neq\mathrm{Var}\) → not Poisson |
| 5 | Time interval scaling | If rate is per hour, per 5 minutes → \(\lambda_{t}= \lambda_{1h}\times t\) before combining |

---

### Example 1 — Easy (Coursebook Lions & Tigers)

> **Question:** Lions rescued per week \(L\sim\mathrm{Po}(5)\), tigers \(T\sim\mathrm{Po}(3)\), independent. Let \(A=L+T\) be total large cats rescued per week. Find (a) distribution of \(A\) and (b) \(P(A=2)\).

**Solution:**

(a) Both independent Poissons → sum is Poisson:

$$A=L+T\sim\mathrm{Po}(5+3)=\mathrm{Po}(8)$$

(b)

$$P(A=2)=\frac{e^{-8}\,8^{2}}{2!}=\frac{e^{-8}\times64}{2}=32e^{-8}$$

$$=32\times0.00033546=0.0107$$

Matches brute-force enumeration: \(P(L=0)P(T=2)+P(L=1)P(T=1)+P(L=2)P(T=0)=0.0107\) ✓ — but Poisson sum is one line.

---

### Example 2 — Medium (Past Paper — 9709/62/O/N/22 Q2 / 9709/63/M/J/23 style)

> **Question:** Texts from Josh \(J\sim\mathrm{Po}(3.2)\) and Reuben \(R\sim\mathrm{Po}(2.5)\) per week, independent. Let \(T=J+R\). Find (a) distribution of \(T\) and (b) \(P(T>5)\). [Coursebook Worked Example 3.10]

**Solution:**

(a)

$$T=J+R\sim\mathrm{Po}(3.2+2.5)=\mathrm{Po}(5.7)$$

(b)

$$P(T>5)=1-P(T\le5)=1-\sum_{k=0}^{5}\frac{e^{-5.7}5.7^{k}}{k!}$$

Compute cumulative:

$$P(T\le5)=e^{-5.7}\left(1+5.7+\frac{5.7^{2}}{2!}+\frac{5.7^{3}}{3!}+\frac{5.7^{4}}{4!}+\frac{5.7^{5}}{5!}\right)$$

$$=e^{-5.7}(1+5.7+16.245+30.8655+43.983+50.140)=e^{-5.7}(147.93)$$

$$=0.003346\times147.93=0.327 \quad\text{(calc: }0.3269\text{)}$$

$$P(T>5)=1-0.327=0.673$$

---

### Example 3 — Hard (Mixed scaling — proving NOT Poisson — 9709/62/O/N/21 Q5 type)

> **Question:** Independent \(X\sim\mathrm{Po}(2.4)\), \(Y\sim\mathrm{Po}(3.6)\). Let \(W=2X-Y\).
> (a) Find \(\mathrm{E}(W)\) and \(\mathrm{Var}(W)\).
> (b) Explain why \(W\) does not follow a Poisson distribution.
> (c) A student claims \(W\sim\mathrm{Po}(1.2)\) because \(2(2.4)-3.6=1.2\). Explain the error. [Coursebook Worked Example 3.11]

**Solution:**

(a)

$$\mathrm{E}(W)=\mathrm{E}(2X-Y)=2\mathrm{E}(X)-\mathrm{E}(Y)=2(2.4)-3.6=4.8-3.6=1.2$$

$$\mathrm{Var}(W)=\mathrm{Var}(2X-Y)=2^{2}\mathrm{Var}(X)+(-1)^{2}\mathrm{Var}(Y)=4(2.4)+1(3.6)=9.6+3.6=13.2$$

(b) For Poisson, mean must equal variance. Here:

$$\mathrm{E}(W)=1.2 \neq \mathrm{Var}(W)=13.2$$

Also \(W\) can be negative (e.g. \(X=0,Y=5 \implies W=-5\)), but Poisson support is \(0,1,2,\dots\). Hence **not Poisson**.

(c) Error: Student subtracted means (\(2\lambda-\mu\)) and assumed result is Poisson. Two mistakes:
- \(2X\) is not Poisson (variance \(4\lambda\neq2\lambda\)), so cannot be combined via Poisson addition rule.
- Subtraction cannot give Poisson — even if \(X+Y\sim\mathrm{Po}(\lambda+\mu)\), the difference has no Poisson law. The rule only applies to **sums** with coefficient 1.

---

### Example 4 — Trap (Three Poissons vs Normal approximation confusion)

> **Question [TRAP]:** Independent \(A\sim\mathrm{Po}(2), B\sim\mathrm{Po}(1.2), C\sim\mathrm{Po}(0.5)\). Let \(T=A+B+C\).
> (a) State the distribution of \(T\) and compute \(P(T=4)\) and \(P(T<3)\).
> (b) A student computes \(P(T<3)\) as \(P(A<3)P(B<3)P(C<3)\). Explain why this is wrong.
> (c) If the question asked for \(P(T>50)\) with \(T\sim\mathrm{Po}(120)\), how would you approximate?

**Solution:**

(a) Sum of 3 independent Poissons → Poisson with sum lambda:

$$T=A+B+C\sim\mathrm{Po}(2+1.2+0.5)=\mathrm{Po}(3.7)$$

$$P(T=4)=\frac{e^{-3.7}3.7^{4}}{4!}=\frac{e^{-3.7}\times187.4161}{24}=e^{-3.7}\times7.809=0.02473\times7.809=0.193$$

$$P(T<3)=P(T\le2)=e^{-3.7}\left(1+3.7+\frac{3.7^{2}}{2}\right)=e^{-3.7}(1+3.7+6.845)=e^{-3.7}(11.545)$$

$$=0.02473\times11.545=0.2856\approx0.286$$

(b) Error: \(P(T<3)\neq P(A<3)P(B<3)P(C<3)\). The events \(A<3,B<3,C<3\) do not correspond to \(A+B+C<3\). For example \(A=2,B=2,C=2\) gives each \(<3\) but sum \(=6\not<3\). Correct method uses the Poisson distribution of the **sum**.

(c) For large \(\lambda\) (here \(120>15\)), Poisson can be approximated by normal: \(\mathrm{Po}(120)\approx\mathrm{N}(120,120)\) with continuity correction. So \(P(T>50)=P(X>50.5)\) where \(X\sim\mathrm{N}(120,120)\). Not needed here since \(\lambda=3.7\) is small — use Poisson formula directly.

> ⭐ **Watch Out! — PART 4**
> - **Only sum with coefficient 1 is Poisson.** \(X+Y\sim\mathrm{Po}(\lambda+\mu)\) ✓ but \(2X,\ 3Y,\ X-Y,\ 2X+3Y\) ✗ — these need E/Var rules and are not Poisson.
> - **Independence required** — if not stated, cannot claim \(X+Y\sim\mathrm{Po}\). Syllabus always says "independent" — underline it.
> - **Don't multiply probabilities for sum events** — use the Poisson of the sum, not product of individual cumulatives.
> - **Interval scaling first:** Convert rates to same time unit before adding lambdas (e.g. per day → per week multiply by 7).
> - **Normal approximation only for large \(\lambda\) (~ >15):** Small \(\lambda\) → exact Poisson formula; large \(\lambda\) → \(\mathrm{N}(\lambda,\lambda)\) with continuity correction.

---

# PART 5: Mixed & Exam Traps — Scaling Before Adding, SD vs Variance, \(nX\) vs Sum

This part collects the traps that cost grades every year even when students know the formulas.

## 5.1 Rules — The Trap Checklist

$$\boxed{\text{Trap 1: } \mathrm{Var}(aX)=a^{2}\mathrm{Var}(X) \neq a\mathrm{Var}(X)}$$

$$\boxed{\text{Trap 2: } \mathrm{Var}(X\pm Y)=\mathrm{Var}(X)+\mathrm{Var}(Y) \neq \mathrm{Var}(X)\pm\mathrm{Var}(Y)}$$

$$\boxed{\text{Trap 3: } nX \sim \mathrm{N}(n\mu,n^{2}\sigma^{2}) \quad\text{vs}\quad \underbrace{X_1+\dots+X_n}_{n\text{ i.i.d.}}\sim\mathrm{N}(n\mu,n\sigma^{2})}$$

$$\boxed{\text{Trap 4: Read variance vs SD: if } X\sim\mathrm{N}(80,64),\; \mathrm{Var}=64,\; \mathrm{SD}=8}$$

$$\boxed{\text{Trap 5: Units — } \mathrm{E}(aX+b)=a\mathrm{E}(X)+b \text{ but } \mathrm{Var}(aX+b)=a^{2}\mathrm{Var}(X) \text{ (ignore }b\text{)}}$$

> **Justification Box — Why Do These Traps Exist?**
> All traps stem from forgetting what variance *is*: **average squared deviation**. Squaring makes signs and constants behave differently than they do for expectation. Subtracting two noisy measurements doesn't cancel noise — it compounds it (hence variances add). Scaling a measurement by \(a\) scales noise by \(a\), so squared noise scales by \(a^{2}\). Repeated independent measurements average out (variance grows linearly in \(n\)), but stretching one measurement stretches its noise quadratically.

### Method Table — Trap Avoidance Protocol

| Step | Protocol | Check |
|------|----------|-------|
| 1 | Read question wording verbatim | Underline "independent", "randomly chosen", "two observations", "twice", "total of \(n\)" |
| 2 | Decide: single-scale or sum-of-i.i.d.? | "Twice \(X\)" / "\(2X\)" → \(4\mathrm{Var}\); "Sum of two independent values" / "\(X_1+X_2\)" → \(2\mathrm{Var}\) |
| 3 | Identify variance vs SD | If given \(\mathrm{N}(50,4)\) and told SD=4, second param is variance. Write \(\sigma^{2}=..., \sigma=...\) |
| 4 | Write E step with correct signs | \(\mathrm{E}(aX-bY)=a\mathrm{E}(X)-b\mathrm{E}(Y)\) — signs follow |
| 5 | Write Var step as **always add** | \(\mathrm{Var}(aX-bY)=a^{2}\mathrm{Var}(X)+b^{2}\mathrm{Var}(Y)\) — minus becomes plus |
| 6 | For normal probability, state new distribution | \(W\sim\mathrm{N}(\mu_W,\sigma^{2}_W)\) before standardising — examiner needs it |

---

### Example 1 — Easy (Coursebook Exercise 3B Q6 — Scaling Trap with Table)

> **Question:** \(X\) has table: \(x=2,3,5\) with \(P=0.6,0.1,0.3\). Find (a) \(\mathrm{E}(X),\mathrm{Var}(X)\) (b) \(\mathrm{E}(2X)\) and \(\mathrm{Var}(2X)\) (c) \(\mathrm{E}(X_1+X_2)\) and \(\mathrm{Var}(X_1+X_2)\) where \(X_1,X_2\) are two independent observations. Compare.

**Solution:**

$$\mathrm{E}(X)=2(0.6)+3(0.1)+5(0.3)=1.2+0.3+1.5=3.0$$

$$\mathrm{E}(X^{2})=4(0.6)+9(0.1)+25(0.3)=2.4+0.9+7.5=10.8$$

$$\mathrm{Var}(X)=10.8-9=1.8$$

(b) Single variable doubled:

$$\mathrm{E}(2X)=2\times3=6$$

$$\mathrm{Var}(2X)=4\times1.8=7.2$$

(c) Sum of two independent observations:

$$\mathrm{E}(X_1+X_2)=3+3=6$$

$$\mathrm{Var}(X_1+X_2)=1.8+1.8=3.6$$

Same mean, variance doubled vs quadrupled. Highlight: \(P(2X=4)=0.6\) (only even values), while \(X_1+X_2\) can be \(4,5,6,7,8,10\) — different distributions.

---

### Example 2 — Medium (Past Paper — 9709/62/O/N/22 Q5 — Cost Function)

> **Question:** Cost of hiring a bicycle: \(C=500+3T\) cents, where \(T\) = minutes hired, \(\mathrm{E}(T)=142,\ \mathrm{SD}(T)=35\). (a) Find \(\mathrm{E}(C)\) and \(\mathrm{SD}(C)\). (b) Six people hire independently. Find mean and SD of total amount paid. [9709/72/Nov12 Q3]

**Solution:**

(a)

$$\mathrm{E}(C)=\mathrm{E}(500+3T)=500+3\mathrm{E}(T)=500+3(142)=500+426=926\text{ cents }(= \$9.26)$$

$$\mathrm{Var}(C)=3^{2}\mathrm{Var}(T)=9\times35^{2}=9\times1225=11025$$

$$\mathrm{SD}(C)=\sqrt{11025}=105\text{ cents}$$

Note: \(\mathrm{SD}(C)=3\mathrm{SD}(T)=3\times35=105\) — correct to scale SD by \(|a|\), not variance.

(b) Total for 6: \(S=C_1+\dots+C_6\) — sum of 6 i.i.d.:

$$\mathrm{E}(S)=6\mathrm{E}(C)=6\times926=5556\text{ cents}$$

$$\mathrm{Var}(S)=6\mathrm{Var}(C)=6\times11025=66150$$

$$\mathrm{SD}(S)=\sqrt{66150}=257.19\approx257\text{ cents}$$

Common error: \(6C\) would give \(\mathrm{Var}=36\times11025=396900\), SD \(=630\) — **wrong** by factor \(\sqrt{6}\). The phrase "six people independently" → sum, not \(6\times\) one person.

---

### Example 3 — Hard (Normal + Linear Combo + Mixed SD Trap — 9709/72/Q6 Jun16 style)

> **Question:** Demand for hair dryers per week \(D\sim\mathrm{Po}(3.4)\)? No — this time normal: Portfolios: Investment \(A\sim\mathrm{N}(10,4)\), \(B\sim\mathrm{N}(28,25)\), \(C\sim\mathrm{N}(15,3^{2})\) where \(C\sim\mathrm{N}(15,9)\) (variance 9). \(A,B,C\) independent. Write distributions of (a) \(A+2B\) (b) \(2B-A\) (c) \(A+B+C\) and find \(P(2B-A<40)\). [9709 Exercise 3C Q1 extended]

**Solution:**

Given: \(A\sim\mathrm{N}(10,4)\) so \(\mu_A=10,\sigma^{2}_A=4\); \(B\sim\mathrm{N}(28,25)\) so \(\sigma^{2}_B=25\); \(C\sim\mathrm{N}(15,9)\) so \(\sigma^{2}_C=9\) (note \(3\) given is SD if written \(3^{2}\), variance is 9).

(a)

$$\mu_{A+2B}=10+2(28)=66$$

$$\sigma^{2}_{A+2B}=1^{2}(4)+2^{2}(25)=4+100=104$$

$$A+2B\sim\mathrm{N}(66,104)$$

(b)

$$\mu_{2B-A}=2(28)-10=46$$

$$\sigma^{2}_{2B-A}=(-1)^{2}(4)+2^{2}(25)=4+100=104$$

$$2B-A\sim\mathrm{N}(46,104)$$

Same variance, different mean — subtraction affects mean, not variance.

(c)

$$\mu_{A+B+C}=10+28+15=53$$

$$\sigma^{2}_{A+B+C}=4+25+9=38$$

$$A+B+C\sim\mathrm{N}(53,38)$$

Probability:

$$P(2B-A<40)=P\!\left(Z<\frac{40-46}{\sqrt{104}}\right)=P\!\left(Z<\frac{-6}{10.198}\right)=P(Z<-0.588)$$

$$=1-\Phi(0.588)=1-0.722=0.278$$

---

### Example 4 — Trap (Poisson Non-Poisson + Variance Add Trap Combined)

> **Question [TRAP]:** Independent \(X\sim\mathrm{Po}(4.2), Y\sim\mathrm{Po}(6.3)\). Student answers:
> (i) \(2X-Y\sim\mathrm{Po}(2.1)\) because \(2(4.2)-6.3=2.1\)
> (ii) \(\mathrm{Var}(X+Y)=4.2-6.3=-2.1\) (negative variance)
> (iii) \(X+Y\sim\mathrm{N}(10.5,10.5)\) so \(P(X+Y<5)=\Phi((5-10.5)/\sqrt{10.5})\)
> Identify each error and give correct answers.

**Solution:**

(i) **Error: \(2X-Y\) is not Poisson.** Correct:

$$\mathrm{E}(2X-Y)=2(4.2)-6.3=2.1 \checkmark \text{ (mean correct but not sufficient)}$$

$$\mathrm{Var}(2X-Y)=4(4.2)+1(6.3)=16.8+6.3=23.1 \neq 2.1$$

Since \(\mathrm{E}\neq\mathrm{Var}\), not Poisson. Also can be negative. Never claim \(aX\) is Poisson.

(ii) **Error: variances subtracted, negative variance impossible.** Correct:

$$\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)=4.2+6.3=10.5$$

Variances always add. Variance can never be negative — that's a red flag.

(iii) **Error: wrong distribution — exact Poisson should be used for small \(\lambda\).** Correct:

$$X+Y\sim\mathrm{Po}(10.5)$$

$$P(X+Y<5)=P(X+Y\le4)=\sum_{k=0}^{4}\frac{e^{-10.5}10.5^{k}}{k!}=e^{-10.5}\left(1+10.5+55.125+192.94+506.46\right)$$

$$=e^{-10.5}(765.03)=0.0000275\times765.03=0.0210$$

Normal approximation \(\mathrm{N}(10.5,10.5)\) is valid for \(\lambda>15\), borderline here — exam expects exact Poisson for \(\lambda=10.5\). Using normal without continuity correction loses marks.

> ⭐ **Watch Out! — PART 5**
> - **Six traps, zero excuses:** Memorise: square \(a\), add variances, \(nX\neq\sum X_i\), read SD vs Var, include \(b\) only in mean, Poisson sum only.
> - **Write the line:** "\(W\sim\mathrm{Po}(...)\)" or "\(W\sim\mathrm{N}(...)\)" — it's a mark even if final probability is wrong.
> - **Negative variance = instant fail:** If you get \(\mathrm{Var}<0\), you subtracted where you should have added.
> - **Language detector:** Scan question for "total of \(n\) independent..." → \(n\mu, n\sigma^{2}\); " \(n\) times ..." → \(n\mu, n^{2}\sigma^{2}\).
> - **Poisson sum only for + with coef 1:** Anything with \(2X\), \(-Y\), \(3X+2Y\) → not Poisson, compute E/Var via Part 2.

---


---

# PART 6: NEW Solved Examples — Cost/Profit, Boxes Trap, Poisson Trio (2026 Additions)

> **Why these three?** Each targets the most-examined trap not fully drilled in Parts 1–5: (a) a cost function $C=aX+b$ (and $aX+bY+c$) with a normal probability tail, (b) the $n=10$ sum vs $10X$ variance trap with normal approximation, (c) a 3-variable Poisson sum and the scaled non-Poisson case. Every solution follows the 4-step protocol: **1 Identify → 2 Mean → 3 Variance (ADD, $a^{2}$) → 4 Distribution & Probability.**

---

### Example A — Cost/Profit Function $C=aX+b$ and $C=aX+bY+c$ with Normal Probability (4-Step)

> **Question:** The mass of a filled bottle $X\sim\mathrm{N}(500,12^{2})$ g, independent of label mass $Y\sim\mathrm{N}(8,1.5^{2})$ g. The total dispatch weight for one order is $W=X+Y$. The courier charges $C=0.8W+15$ (pence). For a batch, an alternative quote charges $C_{2}=0.8X+0.8Y+15$ — algebraically identical but useful to show $c$ handling. Find (i) $\mathrm{E}(C)$ and $\mathrm{Var}(C)$, (ii) the distribution of $C$, (iii) $P(C>430)$. [Cost-function type: 9709/62/O/N/22 Q5 style]

**Solution — 4 Steps:**

**Step 1 — Identify $\mathrm{E},\mathrm{Var}$ of components.**

$$X\sim\mathrm{N}(500,12^{2})\implies \mathrm{E}(X)=500,\quad \mathrm{Var}(X)=144$$

$$Y\sim\mathrm{N}(8,1.5^{2})\implies \mathrm{E}(Y)=8,\quad \mathrm{Var}(Y)=2.25$$

$$W=X+Y,\quad X,Y\text{ independent}$$

**Step 2 — Mean of $W$ then of $C$ (linearity — signs follow, $c$ added once).**

$$\mathrm{E}(W)=\mathrm{E}(X+Y)=\mathrm{E}(X)+\mathrm{E}(Y)=500+8=508$$

$$\mathrm{E}(C)=\mathrm{E}(0.8W+15)=0.8\,\mathrm{E}(W)+15=0.8(508)+15=406.4+15=421.4$$

Equivalently via $C_{2}$:

$$\mathrm{E}(C_{2})=0.8\,\mathrm{E}(X)+0.8\,\mathrm{E}(Y)+15=0.8(500)+0.8(8)+15=400+6.4+15=421.4$$

**Step 3 — Variance of $W$ then of $C$ (independence ⇒ ADD, square coefficients, ignore $c$).**

$$\mathrm{Var}(W)=\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)=144+2.25=146.25$$

$$\mathrm{Var}(C)=\mathrm{Var}(0.8W+15)=0.8^{2}\,\mathrm{Var}(W)=0.64\times146.25=93.6$$

Check via $C_{2}$:

$$\mathrm{Var}(C_{2})=0.8^{2}\mathrm{Var}(X)+0.8^{2}\mathrm{Var}(Y)=0.64(144)+0.64(2.25)=92.16+1.44=93.6$$

Note $15$ (constant $c$) shifts mean by $15$ but contributes $0$ to variance.

$$\mathrm{SD}(C)=\sqrt{93.6}=9.674\ldots\approx 9.67$$

**Step 4 — State new normal and standardise for probability.**

$$W\sim\mathrm{N}(508,146.25)\implies C=0.8W+15\sim\mathrm{N}(421.4,\ 93.6)$$

$$P(C>430)=P\!\left(Z>\frac{430-421.4}{\sqrt{93.6}}\right)=P\!\left(Z>\frac{8.6}{9.674}\right)=P(Z>0.889)$$

$$=1-\Phi(0.889)=1-0.813=0.187$$

So $\approx 18.7\%$ of orders exceed 430 pence. If the question asked $P(C<400)$:

$$P(C<400)=P\!\left(Z<\frac{400-421.4}{9.674}\right)=P(Z<-2.212)=\Phi(-2.212)=1-\Phi(2.212)=0.0134$$

> **Examiner tip (Cost functions):** Write $C=aX+bY+c$ → $\mathrm{E}(C)=a\mu_{X}+b\mu_{Y}+c$ but $\mathrm{Var}(C)=a^{2}\sigma^{2}_{X}+b^{2}\sigma^{2}_{Y}$ — the $c$ vanishes in variance. Never include $c$ in $\mathrm{Var}$.

---

### Example B — $n=10$ Boxes: $\sum_{i=1}^{10}X_{i}$ vs $10X$ Trap with Normal Probability (4-Step)

> **Question [TRAP — seen every year]:** Each cereal box mass $X\sim\mathrm{N}(750,18^{2})$ g, independent across boxes. A crate holds 10 randomly chosen boxes.
> (a) Let $S=X_{1}+X_{2}+\cdots+X_{10}$ be the total mass of the crate. State the distribution of $S$ and find $P(S>7600)$.
> (b) A student instead computes $T=10X$ (ten times a single box) and finds $P(T>7600)$. Show the error and compute the wrong probability to see the mark lost.
> (c) Find $P(745<X<755)$ for a single box vs $P(7450<S<7550)$ intuition.
> [9709/62/O/N/22 Q6 / 9709/73/Nov16 Q3 — "total of $n$ independent" wording]

**Solution — 4 Steps:**

**Step 1 — Identify single-box parameters.**

$$X\sim\mathrm{N}(750,18^{2})\implies \mathrm{E}(X)=750,\quad \mathrm{Var}(X)=324,\quad \mathrm{SD}(X)=18$$

For 10 independent boxes, $S$ is sum of 10 i.i.d. normals; $T=10X$ is scaling one observation.

**Step 2 — Means (both give $10\mu$ — this is why students think they are the same).**

$$\mathrm{E}(S)=\mathrm{E}(X_{1}+\cdots+X_{10})=10\,\mathrm{E}(X)=10\times750=7500$$

$$\mathrm{E}(T)=\mathrm{E}(10X)=10\,\mathrm{E}(X)=7500$$

Same mean — the trap.

**Step 3 — Variances (THE distinction: ADD vs $a^{2}$).**

Correct (sum of 10 independent):

$$\mathrm{Var}(S)=\mathrm{Var}(X_{1})+\cdots+\mathrm{Var}(X_{10})=10\,\mathrm{Var}(X)=10\times324=3240$$

$$\mathrm{SD}(S)=\sqrt{3240}=56.92$$

Wrong (scaling one observation by 10):

$$\mathrm{Var}(T)=\mathrm{Var}(10X)=10^{2}\,\mathrm{Var}(X)=100\times324=32400$$

$$\mathrm{SD}(T)=\sqrt{32400}=180$$

Ratio: $\mathrm{Var}(T)=10\times\mathrm{Var}(S)$; $\mathrm{SD}(T)=\sqrt{10}\times\mathrm{SD}(S)\approx3.16$ times larger spread.

**Step 4 — State distributions and standardise.**

$$S\sim\mathrm{N}(7500,\ 3240),\qquad T=10X\sim\mathrm{N}(7500,\ 32400)$$

(a) Correct:

$$P(S>7600)=P\!\left(Z>\frac{7600-7500}{\sqrt{3240}}\right)=P\!\left(Z>\frac{100}{56.92}\right)=P(Z>1.757)$$

$$=1-\Phi(1.757)=1-0.9606=0.0394\approx 0.039$$

Only ~3.9% of crates exceed 7600 g.

(b) Student's wrong $T$:

$$P(T>7600)=P\!\left(Z>\frac{7600-7500}{\sqrt{32400}}\right)=P\!\left(Z>\frac{100}{180}\right)=P(Z>0.556)$$

$$=1-\Phi(0.556)=1-0.711=0.289$$

The student reports $0.289$ — more than **seven times** too large. Exam loses all A1 marks for variance.

(c) Single-box interval for comparison:

$$P(745<X<755)=P\!\left(\frac{745-750}{18}<Z<\frac{755-750}{18}\right)=P(-0.278<Z<0.278)=2\Phi(0.278)-1=0.219$$

The crate total $S$ has tighter relative spread: $\mathrm{SD}(S)/\mathrm{E}(S)=0.76\%$ vs $\mathrm{SD}(X)/\mathrm{E}(X)=2.4\%$ — averaging over 10 independent boxes **reduces** relative variability (law of large numbers intuition). $10X$ would falsely keep $\mathrm{SD}/$mean at $2.4\%$.

> **Language detector:** "10 boxes are chosen at random" / "total mass of 10 boxes" / "$X_{1},\dots,X_{10}$ independent" → sum → $n\mathrm{Var}$.  "Ten times the mass of a box" / "$10X$" → scale → $n^{2}\mathrm{Var}$. Underline the wording before writing any variance.

---

### Example C — Poisson Sum of 3 Variables + Scaled Non-Poisson Case (4-Step)

> **Question:** In a call centre, calls per hour to three independent lines are $A\sim\mathrm{Po}(1.8)$, $B\sim\mathrm{Po}(2.2)$, $C\sim\mathrm{Po}(3.0)$. Let $T=A+B+C$ be total calls per hour. Let $W=2A+B$ be a weighted workload score.
> (a) State the distribution of $T$ and find $P(T=4)$ and $P(T\le 2)$.
> (b) Find $\mathrm{E}(W)$ and $\mathrm{Var}(W)$. Is $W$ Poisson? Justify with mean vs variance and support.
> (c) A student claims $W\sim\mathrm{Po}(5.8)$ because $2(1.8)+2.2=5.8$. Explain the double error.
> [9709/62/O/N/22 Q2 Poisson sum + 9709/62/O/N/21 Q5 scaled trap]

**Solution — 4 Steps:**

**Step 1 — Identify lambdas and conditions for Poisson sum.**

$$A\sim\mathrm{Po}(1.8),\ B\sim\mathrm{Po}(2.2),\ C\sim\mathrm{Po}(3.0),\quad \text{all independent}$$

Each is Poisson and independent → sum with coefficient 1 preserves Poisson. Any scaling or subtraction breaks it.

**Step 2 — Sum $T$ (coefficients 1 ⇒ Poisson; lambdas ADD).**

$$T=A+B+C\sim\mathrm{Po}(1.8+2.2+3.0)=\mathrm{Po}(7.0)$$

Mean and variance check:

$$\mathrm{E}(T)=1.8+2.2+3.0=7.0,\qquad \mathrm{Var}(T)=1.8+2.2+3.0=7.0\implies \mathrm{E}=\mathrm{Var}\ \checkmark\text{ Poisson}$$

Probabilities via $\displaystyle P(T=k)=\frac{e^{-7}7^{k}}{k!}$:

$$P(T=4)=\frac{e^{-7}\,7^{4}}{4!}=\frac{e^{-7}\times2401}{24}=e^{-7}\times100.042$$

$$=0.0009119\times100.042=0.0912$$

$$P(T\le 2)=P(T=0)+P(T=1)+P(T=2)=e^{-7}\!\left(1+7+\frac{7^{2}}{2}\right)=e^{-7}(1+7+24.5)=e^{-7}(32.5)$$

$$=0.0009119\times32.5=0.0296$$

So $P(T\le 2)\approx0.030$.

**Step 3 — Scaled combination $W=2A+B$ (coefficient $2\neq1$ ⇒ NOT Poisson; use Part 2 rules — ADD variances, square coefficients).**

$$\mathrm{E}(W)=\mathrm{E}(2A+B)=2\,\mathrm{E}(A)+\mathrm{E}(B)=2(1.8)+2.2=3.6+2.2=5.8$$

$$\mathrm{Var}(W)=\mathrm{Var}(2A+B)=2^{2}\,\mathrm{Var}(A)+1^{2}\,\mathrm{Var}(B)=4(1.8)+1(2.2)=7.2+2.2=9.4$$

Note: variance used **ADD** even though $W$ is a sum — but coefficients squared: $4\times1.8$ not $2\times1.8$.

Comparison:

$$\mathrm{E}(W)=5.8\neq \mathrm{Var}(W)=9.4\implies \mathrm{E}\neq\mathrm{Var}\implies W\text{ is NOT Poisson}$$

Additionally, $W$ takes values $0,1,2,3,\dots$ but only with gaps? Actually $W=2A+B$: if $A=0,B=1\Rightarrow W=1$ is possible, but support includes $1$, but $P(W=1)=P(A=0)P(B=1)=e^{-1.8}e^{-2.2}(2.2)$ — still possible. However $W$ can be odd and even, so support alone not disproof here. Stronger: if $A=1\Rightarrow W\ge2$, but main disproof is $\mathrm{E}\neq\mathrm{Var}$ and distribution is not of Poisson form (convolution of scaled Poisson is not Poisson). Every exam mark scheme accepts "$\mathrm{E}\neq\mathrm{Var}$ so not Poisson" as full justification.

**Step 4 — Student error diagnosis.**

Student's claim $W\sim\mathrm{Po}(5.8)$ via $2(1.8)+2.2=5.8$:

Error 1: Scaled Poisson is not Poisson. $2A\not\sim\mathrm{Po}(3.6)$ because $\mathrm{E}(2A)=3.6$ but $\mathrm{Var}(2A)=4\times1.8=7.2\neq3.6$. The Poisson addition rule $X+Y\sim\mathrm{Po}(\lambda+\mu)$ requires each summand to be Poisson with coefficient exactly $1$. $2A$ fails this.

Error 2: Assumed expectation suffices to identify distribution. Even though $\mathrm{E}(W)=5.8$ is correct, distribution is not determined by mean alone. The student ignored variance check. Correct statement: $W$ has $\mathrm{E}=5.8$, $\mathrm{Var}=9.4$, is **not Poisson**, so $P(W=k)$ cannot be computed via $e^{-5.8}5.8^{k}/k!$ — must be computed via convolution $\sum_{a}P(A=a)P(B=k-2a)$ if needed.

If the student needed $P(W=4)$ correctly:

$$P(W=4)=P(A=0,B=4)+P(A=1,B=2)+P(A=2,B=0)$$

$$=e^{-1.8}e^{-2.2}\frac{2.2^{4}}{4!}+e^{-1.8}(1.8)\,e^{-2.2}\frac{2.2^{2}}{2!}+e^{-1.8}\frac{1.8^{2}}{2!}\,e^{-2.2}$$

$$=e^{-4.0}(0.808+1.8\times2.42+1.62\times1)=e^{-4.0}(0.808+4.356+1.62)=e^{-4.0}(6.784)=0.124$$

Versus Poisson-wrong $e^{-5.8}5.8^{4}/4!=0.104$ — close but wrong and loses method marks.

> **Poisson checklist:** Sum with all coefficients $=1$ and independent → $\mathrm{Po}(\sum\lambda)$ ✓. Anything with $2A$, $A-B$, $3X+2Y$ → compute $\mathrm{E}$ and $\mathrm{Var}$ via $a^{2}\mathrm{Var}$ rule, note $\mathrm{E}\neq\mathrm{Var}$ → **not Poisson** (also $W$ can be negative for differences). State "not Poisson" explicitly — it is a mark.


---

# Formula Sheet — All Chapter 3 Formulas (LaTeX Boxed)

$$\boxed{\mathrm{E}(aX+b)=a\mathrm{E}(X)+b}$$

$$\boxed{\mathrm{Var}(aX+b)=a^{2}\mathrm{Var}(X)}$$

$$\boxed{\mathrm{SD}(aX+b)=|a|\mathrm{SD}(X)}$$

$$\boxed{\mathrm{E}(X+Y)=\mathrm{E}(X)+\mathrm{E}(Y),\; \mathrm{E}(X-Y)=\mathrm{E}(X)-\mathrm{E}(Y) \quad\text{(always)}}$$

$$\boxed{\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y) \quad\text{(independent only)}}$$

$$\boxed{\mathrm{Var}(X-Y)=\mathrm{Var}(X)+\mathrm{Var}(Y) \quad\text{(independent — ADD!)}}$$

$$\boxed{\mathrm{E}(aX+bY)=a\mathrm{E}(X)+b\mathrm{E}(Y)}$$

$$\boxed{\mathrm{Var}(aX+bY)=a^{2}\mathrm{Var}(X)+b^{2}\mathrm{Var}(Y)}$$

$$\boxed{\mathrm{Var}(aX-bY)=a^{2}\mathrm{Var}(X)+b^{2}\mathrm{Var}(Y)}$$

$$\boxed{\mathrm{Var}\!\left(\sum_{i=1}^{n}a_iX_i\right)=\sum_{i=1}^{n}a_i^{2}\mathrm{Var}(X_i)\quad (X_i\text{ independent})}$$

$$\boxed{X\sim\mathrm{N}(\mu,\sigma^{2})\implies aX+b\sim\mathrm{N}(a\mu+b,\;a^{2}\sigma^{2})}$$

$$\boxed{X\sim\mathrm{N}(\mu_X,\sigma_X^{2}),Y\sim\mathrm{N}(\mu_Y,\sigma_Y^{2})\implies aX+bY\sim\mathrm{N}(a\mu_X+b\mu_Y,\;a^{2}\sigma_X^{2}+b^{2}\sigma_Y^{2})}$$

$$\boxed{Z=\frac{W-\mu_W}{\sigma_W},\quad P(W<k)=\Phi\!\left(\frac{k-\mu_W}{\sigma_W}\right)}$$

$$\boxed{X\sim\mathrm{Po}(\lambda),Y\sim\mathrm{Po}(\mu)\text{ indep.}\implies X+Y\sim\mathrm{Po}(\lambda+\mu)}$$

$$\boxed{X_i\sim\mathrm{Po}(\lambda_i)\text{ indep.}\implies \sum X_i\sim\mathrm{Po}(\sum\lambda_i)}$$

$$\boxed{\mathrm{E}(aX\pm bY)=a\lambda_X\pm b\lambda_Y,\; \mathrm{Var}(aX\pm bY)=a^{2}\lambda_X+b^{2}\lambda_Y \quad\text{(not Poisson if }a\neq1\text{ or minus)}}$$

$$\boxed{n\text{ i.i.d. }X\sim\mathrm{N}(\mu,\sigma^{2}):\ \sum_{i=1}^{n}X_i\sim\mathrm{N}(n\mu,n\sigma^{2})\quad\text{vs}\quad nX\sim\mathrm{N}(n\mu,n^{2}\sigma^{2})}$$

---

# Methods Summary Table

| Formula | Type 1 — Single \(aX+b\) | Type 2 — Sum/Diff \(aX\pm bY\) (indep.) | Type 3 — Probability via Normal \(P(W<k)\) | Past Paper Ref |
|---------|---------------------------|----------------------------------------|---------------------------------------------|----------------|
| \(\mathrm{E}(aX+b)=a\mathrm{E}(X)+b\) | Find \(\mathrm{E}(5X-1)\) from \(X\sim\mathrm{B}(25,0.6)\) → \(5(15)-1=74\) | — | — | 9709/62/M/J/23 Q2 |
| \(\mathrm{Var}(aX+b)=a^{2}\mathrm{Var}(X)\) | \(\mathrm{Var}(5X-1)=25\times6=150\) | — | SD \(=|a|\sigma\) | 9709/62/M/J/23 Q2 |
| \(\mathrm{E}(aX+bY)=a\mathrm{E}(X)+b\mathrm{E}(Y)\) | — | \(\mathrm{E}(2X-Y)=2(6)-4.8=7.2\) with \(X\sim\mathrm{B}(20,0.3),Y\sim\mathrm{B}(12,0.4)\) | — | 9709/62/M/J/22 Q4 |
| \(\mathrm{Var}(aX\pm bY)=a^{2}\mathrm{Var}(X)+b^{2}\mathrm{Var}(Y)\) | — | \(\mathrm{Var}(2X-Y)=4(4.2)+2.88=19.68\); \(\mathrm{Var}(3A-B+2C)=9(1)+2+4(1.3)=16.2\) | — | 9709/63/M/J/21 Q7 |
| \(W=aX+b\sim\mathrm{N}(a\mu+b,a^{2}\sigma^{2})\) | \(C=500+3T\), \(\mathrm{E}(C)=926,\ \mathrm{SD}(C)=105\) | — | — | 9709/72/Nov12 Q3 (Ex3A Q9) |
| \(aX\pm bY\sim\mathrm{N}(a\mu_X\pm b\mu_Y, a^{2}\sigma_X^{2}+b^{2}\sigma_Y^{2})\) | — | Total of 12 jars: \(\mathrm{E}=12(465+120)=7020\), \(\mathrm{Var}=12(25+16)=492\) | \(P(Y>3X)=\Phi(0.416)=0.661\) (rice bags); \(P(L>2S)=0.544\) | 9709/62/O/N/23 Q5; Coursebook 3.6 |
| Poisson sum \(X+Y\sim\mathrm{Po}(\lambda+\mu)\) | — | \(J+R\sim\mathrm{Po}(5.7)\), \(P(T>5)=0.673\) | \(P(A+B+C=4)=0.193\) with \(A+B+C\sim\mathrm{Po}(3.7)\) | 9709/62/O/N/22 Q2; 9709 Coursebook 3.10 |
| Trap: \(nX\) vs \(\sum X_i\) | \(\mathrm{Var}(2X)=4\mathrm{Var}(X)\) | \(\mathrm{Var}(X_1+X_2)=2\mathrm{Var}(X)\) | \(S\) of 4 Thrists: \(P(S>30)=0.332\) vs \(P(C>4T)=0.373\) | 9709/73/Nov16 Q3; 9709/62/O/N/22 Q6 |

---

# Justification Bank

| Statement | Justification | Condition |
|-----------|---------------|-----------|
| \(\mathrm{E}(X+Y)=\mathrm{E}(X)+\mathrm{E}(Y)\) | Linearity of expectation: \(\sum (x+y)P(x,y)=\sum xP(x)+\sum yP(y)\). No covariance term. Holds for **any** \(X,Y\), dependent or not. | None — always holds |
| \(\mathrm{E}(aX+b)=a\mathrm{E}(X)+b\) | Special case of linearity with constant RV \(b\). Constants pass through expectation. | None — always holds |
| \(\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)\) | \(\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)+2\mathrm{Cov}(X,Y)\). Independence ⇒ \(\mathrm{Cov}=0\) ⇒ reduces to sum. | **Independent** only |
| \(\mathrm{Var}(X-Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)\) (ADD) | \(\mathrm{Var}(X-Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)-2\mathrm{Cov}(X,Y)\). Independence ⇒ \(\mathrm{Cov}=0\) ⇒ still sum. Subtracting RVs adds noise. | **Independent** only |
| \(\mathrm{Var}(aX)=a^{2}\mathrm{Var}(X)\) | \(\mathrm{Var}(aX)=\mathrm{E}[(aX-a\mu)^2]=\mathrm{E}[a^{2}(X-\mu)^2]=a^{2}\mathrm{Var}(X)\). Squared deviation scales quadratically. | None — single variable |
| \(\mathrm{Var}(aX+b)=\mathrm{Var}(aX)\) | Adding constant \(b\) shifts both \(X\) and \(\mu\) equally: \((aX+b)-(a\mu+b)=a(X-\mu)\). Constant carries no variance. | None |
| \(aX+bY\) normal if \(X,Y\) normal | MGF of normal is \(M_X(t)=\exp(\mu t+\tfrac12\sigma^{2}t^{2})\). Product \(M_{aX}(t)M_{bY}(t)\) remains exponential-quadratic → normal MGF. Requires each normal and independence. | \(X,Y\) normal **and** independent |
| \(X+Y\sim\mathrm{Po}(\lambda+\mu)\) if \(X\sim\mathrm{Po}(\lambda),Y\sim\mathrm{Po}(\mu)\) | PGF \(G_X(t)=e^{\lambda(t-1)}\); independence ⇒ \(G_{X+Y}=G_XG_Y=e^{(\lambda+\mu)(t-1)}\) = PGF of \(\mathrm{Po}(\lambda+\mu)\). Counting combined events preserves Poisson postulates. | **Both** Poisson **and** independent |
| \(aX\not\sim\mathrm{Po}\) for \(a\neq1\) | \(\mathrm{E}(aX)=a\lambda\), \(\mathrm{Var}(aX)=a^{2}\lambda\). Poisson requires \(\mathrm{E}=\mathrm{Var}\), fails unless \(a=1\). Also support of \(aX\) is multiples of \(a\), not \(0,1,2,\dots\). | Fails Poisson condition |
| \(X_1+\dots+X_n\sim\mathrm{N}(n\mu,n\sigma^{2})\) vs \(nX\sim\mathrm{N}(n\mu,n^{2}\sigma^{2})\) | Sum of \(n\) independent copies adds variances linearly (\(n\sigma^{2}\)); scaling one copy squares the scale (\(n^{2}\sigma^{2}\)). Independence dilutes noise; scaling amplifies it. | i.i.d. vs single observation |

---

# Practice Questions + Full Solutions (Past-Paper Style)

### Q1 — Single Variable Scaling (3 marks) [9709/62/M/J/23 Q2 style]

\(X\sim\mathrm{B}(30,0.2)\). Find \(\mathrm{E}(2X+3)\) and \(\mathrm{Var}(2X+3)\).

**Solution:**

$$\mathrm{E}(X)=30\times0.2=6,\qquad \mathrm{Var}(X)=30\times0.2\times0.8=4.8$$

$$\mathrm{E}(2X+3)=2(6)+3=15$$

$$\mathrm{Var}(2X+3)=2^{2}\times4.8=4\times4.8=19.2$$

---

### Q2 — Difference of Independent Binomials (4 marks) [9709/62/M/J/22 Q4]

Independent \(X\sim\mathrm{B}(8,0.25)\) and \(Y\sim\mathrm{B}(5,0.6)\). Find \(\mathrm{E}(6X+2Y)\) and \(\mathrm{Var}(3X-Y)\).

**Solution:**

$$\mathrm{E}(X)=2,\ \mathrm{Var}(X)=1.5;\qquad \mathrm{E}(Y)=3,\ \mathrm{Var}(Y)=1.2$$

$$\mathrm{E}(6X+2Y)=6(2)+2(3)=18$$

$$\mathrm{Var}(3X-Y)=9(1.5)+1(1.2)=13.5+1.2=14.7$$

Note \(\mathrm{Var}(3X-Y)=9\mathrm{Var}(X)+\mathrm{Var}(Y)\) — add.

---

### Q3 — Normal Combination Probability (6 marks) [9709/62/O/N/23 Q5 — 9709/73/Jun12 Q2]

\(H\sim\mathrm{N}(465,25)\) = mass of honey in jar (grams), \(J\sim\mathrm{N}(120,16)\) = mass of empty jar, independent. Find the probability that the total mass of a filled jar \(H+J\) exceeds 600g.

**Solution:**

$$W=H+J$$

$$\mu_W=465+120=585$$

$$\sigma^{2}_W=25+16=41,\qquad \sigma_W=\sqrt{41}=6.403$$

$$W\sim\mathrm{N}(585,41)$$

$$P(W>600)=P\!\left(Z>\frac{600-585}{6.403}\right)=P\!\left(Z>\frac{15}{6.403}\right)=P(Z>2.343)$$

$$=1-\Phi(2.343)=1-0.9904=0.0096$$

$$\approx 0.0096 \text{ (0.96%)}$$

---

### Q4 — Poisson Sum (5 marks) [9709/62/O/N/22 Q3 style]

Number of cars \(C\sim\mathrm{Po}(2)\) and lorries \(L\sim\mathrm{Po}(3)\) passing a point per hour, independent. Find the probability that exactly 4 vehicles (cars + lorries) pass in a randomly chosen hour.

**Solution:**

$$V=C+L\sim\mathrm{Po}(5)$$

$$P(V=4)=\frac{e^{-5}5^{4}}{4!}=\frac{e^{-5}\times625}{24}=26.0417\times e^{-5}$$

$$=26.0417\times0.0067379=0.1755\approx0.175$$

---

### Q5 — Hard: Four-Variable Normal + Trap (6 marks) [9709/73/Nov10 Q4 — 9709/71/Jun10 Q4]

Minerals in 1 tonne rock: \(P\sim\mathrm{N}(46,19^{2})\), \(Q\sim\mathrm{N}(53,23^{2})\), \(R\sim\mathrm{N}(25,10^{2})\), independent. Value \(V=P+2Q+R\). Find \(P(V\ge93)\) — wait, data gives large variances, adjust: if \(P\sim\mathrm{N}(46,19^{2})\) etc., then \(V=P+2Q+R\). Find \(P(V>93)\)? Actually compute: \(\mu_V=46+106+25=177\), \(\sigma^{2}_V=361+2116+100=2577\), \(\sigma=50.76\), \(P(V>93)\approx0.951\) (trivial). Instead use scaled version: \(V=P+Q+2R\) with \(\mu=46+53+50=149\), \(\sigma^{2}=361+529+400=1290\). Find \(P(V\ge93)\). Use original Q: \(V=P+Q+2R\) — find \(P(V>150)\).

**Revised exam-style version:**

Let \(P\sim\mathrm{N}(46,361)\), \(Q\sim\mathrm{N}(53,529)\), \(R\sim\mathrm{N}(25,100)\) (second param is variance). Let \(V=P+Q+2R\). Find \(P(V>160)\).

**Solution:**

$$\mu_V=46+53+2(25)=149$$

$$\sigma^{2}_V=361+529+4(100)=361+529+400=1290$$

$$\sigma_V=\sqrt{1290}=35.916$$

$$V\sim\mathrm{N}(149,1290)$$

$$P(V>160)=P\!\left(Z>\frac{160-149}{35.916}\right)=P(Z>0.3063)=1-\Phi(0.306)=1-0.620=0.380$$

If the paper's original \(V=P+2Q+R\), replace: \(\mu_V=46+106+25=177\), \(\sigma^{2}_V=361+2116+100=2577\),

$$P(V\ge93)=P\!\left(Z\ge\frac{93-177}{50.76}\right)=P(Z\ge-1.655)=\Phi(1.655)=0.951$$

---

### Q6 — Triple Trap: \(2X\) vs Sum, SD, Poisson Not (6 marks) [9709/63/M/J/21 synthesis]

\(X\sim\mathrm{N}(80,64)\) (variance 64). Two independent observations \(X_1,X_2\).
(a) State distribution of \(2X_1\) and of \(X_1+X_2\).
(b) Find \(P(X_1+X_2>170)\).
(c) If instead \(Y\sim\mathrm{Po}(4)\), is \(2Y\sim\mathrm{Po}(8)\)? Justify.

**Solution:**

(a)

$$2X_1\sim\mathrm{N}(160,\ 2^{2}\times64)=\mathrm{N}(160,256),\quad \mathrm{SD}=16$$

$$X_1+X_2\sim\mathrm{N}(160,\ 64+64)=\mathrm{N}(160,128),\quad \mathrm{SD}=11.31$$

(b)

$$S=X_1+X_2\sim\mathrm{N}(160,128),\ \sigma=11.314$$

$$P(S>170)=P\!\left(Z>\frac{170-160}{11.314}\right)=P(Z>0.8839)=1-\Phi(0.884)=1-0.811=0.189$$

If mistakenly used \(2X_1\) (variance 256): \(P(2X_1>170)=P(Z>0.625)=0.266\) — wrong.

(c) No. \(\mathrm{E}(2Y)=8\), \(\mathrm{Var}(2Y)=4\times4=16\neq8\). Poisson requires mean = variance. Also \(2Y\) takes only even values. Hence not Poisson.

---

# Quick Reference Card — Chapter 3 (1 Page)

```
┌─────────────────────────────────────────────────────────────────┐
│  CHAPTER 3 — LINEAR COMBINATIONS  9709 S2 — QUICK REFERENCE     │
├─────────────────────────────────────────────────────────────────┤
│ E(aX+b) = aE(X)+b          ✓ always                            │
│ Var(aX+b)= a²Var(X)        ✓ always (ignore b, square a)       │
│ SD(aX+b) = |a|SD(X)                                             │
├─────────────────────────────────────────────────────────────────┤
│ E(X±Y)=E(X)±E(Y)            ✓ always (no indep needed)         │
│ Var(X+Y)=Var(X)+Var(Y)     ✗ indep. only — STILL ADD          │
│ Var(X-Y)=Var(X)+Var(Y)     ✗ indep. only — STILL ADD (not -)  │
│ Var(aX±bY)=a²Var(X)+b²Var(Y)  (always ADD, square coeffs)       │
├─────────────────────────────────────────────────────────────────┤
│ NORMAL: linear combo of normals → normal                        │
│  aX+b ~ N(aμ+b, a²σ²)                                          │
│  aX±bY ~ N(aμx±bμy, a²σx²+b²σy²)   (add variances!)            │
│  P(W<k)= Φ((k-μw)/σw)                                          │
├─────────────────────────────────────────────────────────────────┤
│ POISSON: sum of indep Poissons → Poisson (only + with coef 1)  │
│  X~Po(λ),Y~Po(μ) indep → X+Y ~ Po(λ+μ)                         │
│  aX, X-Y, 2X+3Y  ✗ NOT Poisson  (E≠Var or negative)             │
├─────────────────────────────────────────────────────────────────┤
│ TRAP CARD                                                       │
│  2X       → N(2μ, 4σ²)    Var=4Var(X)  (scale one obs)         │
│  X1+X2    → N(2μ, 2σ²)    Var=2Var(X)  (sum two indep obs)     │
│  N(50,4)  → Var=4, SD=2   (9709: 2nd param is VARIANCE)        │
│  C=500+3T → E=500+3E(T), Var=9Var(T), SD=3SD(T)                 │
└─────────────────────────────────────────────────────────────────┘

Distinguish: "two independent observations" = X₁+X₂ (add vars)
             "twice the value" / "2X" = scale (square → 4× var)

Checklist before answer:
 □ Underlined "independent"?  □ Variance vs SD?  □ a²?  □ Add not subtract?
 □ Stated new distribution N/Po?  □ Standardised with √Var?
```

---

*Sources: Cambridge Probability & Statistics 2 Coursebook Ch.3 (pp.50–69); Past papers cited — 9709/62/M/J/23 Q2&Q5, 9709/62/F/M/24 Q3, 9709/62/O/N/22 Q2–Q3, 9709/62/O/N/23 Q5, 9709/63/M/J/21 Q7, 9709/73/Nov16 Q3, 9709/72/Nov12 Q3, 9709/71/Jun10 Q4.*

