# B3 Optional Appendix (enrichment - not core SAT)

Reference formula: $E(X) = \sum x_i \cdot P(x_i)$ (see expected-value worked examples below)

- **Influential point:** A point whose removal would substantially change the slope or intercept. Not all outliers are influential - an outlier near the mean $x$ barely changes the line.

---

### [Hard] Correlation Coefficient
Points tightly clustered around a downward-sloping line. Most likely $r$?

✅ $r \approx -0.92$ (strong negative)

❌ **Sign error:** Choosing 0.92 when slope is negative. ❌ **Weak correlation:** Choosing $-0.15$ - points are too tightly clustered.

---

### [Hard] Influential Point (Improvement 13)
Scatterplot: most points cluster near (5, 10) with one point at (20, 40). Removing which point changes the line most?

✅ (20, 40) - it's far from the center of the x-values, so it pulls the line.

❌ **Outlier-only focus:** Removing an outlier at (6, 2) near the mean x barely changes the line - an outlier far from the x-center is influential.

---

### [Medium] Which r Matches the Scatterplot
A scatterplot shows points tightly clustered around a line that rises from left to right. Which is the most likely correlation coefficient?
A) -0.9   B) -0.2   C) 0.4   D) 0.9

✅ D. Tight clustering around a rising line = strong positive correlation.

❌ **Sign error:** choosing -0.9 because "the points look strong" - the line rises, so $r$ must be positive.

---

### [Easy] Expected Value - Insurance (Improvement 16)
Insurance: $200 premium. 2% chance of $5,000 claim. Expected profit?

$E(\text{claim}) = 0.02 \times 5000 = 100$  
Expected profit: $200 - 100 = 100$

❌ **Ignoring premium:** "Expected profit is -4800" - confusing premium with profit.

---

### [Medium] Counting Intuition (Improvement 15)
A restaurant offers 3 appetizers, 4 entrees, 2 desserts. How many different 3-course meals?

$3 \times 4 \times 2 = 24$

❌ **Addition:** $3 + 4 + 2 = 9$ - choices multiply, not add. For each appetizer you can pair any entree and any dessert.

---

### [Hard] Expected Value - Business Decision (Improvement 16)
Product launch: 60% chance of $500K profit, 30% chance of $200K profit, 10% chance of $1M loss. Expected profit?

$E = 0.6 \times 500 + 0.3 \times 200 + 0.1 \times (-1000) = 300 + 60 - 100 = 260$K

❌ **Ignoring loss:** $0.6 \times 500 + 0.3 \times 200 = 360$K - the 10% loss probability matters.

---

### [Hard] Counting - How Many Outcomes? (Improvement 15)
A 4-digit PIN uses digits 0-9. Digits can repeat. How many possible PINs?

$10 \times 10 \times 10 \times 10 = 10,\!000$

❌ **Permutation formula:** $10 \times 9 \times 8 \times 7 = 5,\!040$ - that's without replacement (no repeats). The problem allows repeats.

---

### [Very Hard] Bayes' Theorem
60% employed. Of employed, 40% have degree. Of unemployed, 20% have degree. P(employed | degree)?

Out of 100 adults: employed = 60, unemployed = 40.  
Degree & employed: $60 \times 0.40 = 24$  
Degree & unemployed: $40 \times 0.20 = 8$  
Total with degree: $24+8 = 32$

$P(\text{employed}|\text{degree}) = 24/32 = 0.75$

❌ **Reversed probability:** Computing $P(\text{degree}|\text{employed}) = 0.40$ instead. The question conditions on "has a degree."

---

### [Very Hard] Expected Value with Negative Outcomes
Outcome A: win $5 (P=0.5), B: win $10 (P=0.3), C: lose $2 (P=0.2). Expected value?

$E = 5 \times 0.5 + 10 \times 0.3 + (-2) \times 0.2 = 2.5 + 3.0 - 0.4 = 5.1$

❌ **Ignoring negative:** Computing $5 \times 0.5 + 10 \times 0.3 + 0 \times 0.2 = 5.5$.

---

## B3.6.3 Sample Size Reasoning

| Change | Effect on MoE | Effect on precision |
|--------|---------------|-------------------|
| Double sample size | MoE ÷ √2 (decreases) | More precise |
| Quadruple sample size | MoE ÷ 2 | Much more precise |
| Halve sample size | MoE × √2 (increases) | Less precise |
| Increase confidence level | MoE increases | Less precise |
| Decrease confidence level | MoE decreases | More precise |

⚡ MoE is proportional to $1/\sqrt{n}$. Doubling sample size does NOT halve MoE - it reduces it by a factor of about 1.4.

---

| Stratified (groups → random from each) | ✅ | Population has distinct subgroups |
| Systematic (every $k$th) | ✅ (if start random) | Ordered list available |
| Cluster (randomly select entire groups) | ✅ | Groups are natural, cost-effective |

---

### [Hard] Sample Size Reasoning (Improvement 19)
Poll A: n=500, MoE $\pm 4\%$. Poll B: n=2,000, same population. MoE for B?

MoE is inversely proportional to $\sqrt{n}$. $\sqrt{2000/500} = \sqrt{4} = 2$. So MoE for B $\approx \pm 2\%$.

❌ **Linear:** "4× the sample = 1/4 the MoE = ±1%" - MoE scales with $1/\sqrt{n}$, not $1/n$.

---

### [Medium] Confidence Level Interpretation
A 95% confidence interval for the mean height of adult men is (173, 177) cm. Which statement is correct?
A) 95% of adult men are between 173 and 177 cm tall.
B) The method produces intervals that capture the true mean about 95% of the time.
C) There is a 95% chance the true mean is 175 cm.
D) The sample mean is between 173 and 177 cm.

✅ B. Confidence describes the method across repeated sampling.

❌ **A:** the interval is about the mean, not individual heights. ❌ **C:** no single value inside an interval carries a probability. ❌ **D:** the sample mean is the center (175), a single number, not a range.

---

### [Hard] Quadruple the Sample Size
A poll of 100 voters has a margin of error of ±8%. If the pollster instead surveys 400 voters (same population), what is the approximate margin of error?

MoE scales with $\frac{1}{\sqrt{n}}$: $\sqrt{\frac{400}{100}} = 2$, so the new MoE is $\frac{8\%}{2} = \pm 4\%$.

❌ **Linear scaling:** "4 times the sample means 1/4 the error = ±2%" - MoE is inversely proportional to the square root of the sample size.

---

### [Medium] Placebo Effect
In a drug trial, 30% of patients in the placebo group reported improvement. What does this show?

The placebo effect: belief in treatment can produce real reported improvement. This is why the drug must outperform the placebo, not just outperform nothing.

❌ **"The placebo group is useless"** - the placebo group is essential: it measures improvement caused by expectation, which the drug group's improvement must exceed.

---

### [Medium] Why Double-Blind?
Why do well-designed trials keep both patients and researchers unaware of who received the drug?

It prevents biased reporting (patients who expect improvement report more) and biased assessment (researchers who expect the drug to work evaluate outcomes differently).

❌ **"To protect patient privacy"** - blinding is about eliminating bias in reporting and measurement, not confidentiality.

---

### [Hard] Blocking by Gender
A study of a new exercise program blocks subjects by gender, then randomly assigns half of each gender to the program and half to control. Why block?

Gender may affect both participation and outcomes. Blocking guarantees each treatment group has balanced gender, removing gender as a confounding variable before analysis.

❌ **"Blocking replaces random assignment"** - blocking is used WITHIN random assignment; it reduces variability from a known confounder but does not remove the need for random assignment.
