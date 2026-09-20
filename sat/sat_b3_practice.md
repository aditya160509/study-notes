# B3 Practice Set

# 11. Mixed Interpretation Questions

These combine multiple B3 concepts. Every SAT test has questions like these - they're not purely one topic.

### [Medium] Estimate from Graph (Improvement 37)
A scatterplot shows study hours vs test scores with a line of best fit. A student studied 6.5 hours. The line passes near the point (6.5, 82). What is the best estimate of this student's score?

✅ 82 (read from the line or nearest point on the line).

❌ **Averaging nearby points:** Using (6, 80) and (7, 85) to compute (80+85)/2 = 82.5 - the line already provides the best estimate.

### [Medium] Best Conclusion (Improvement 38)
A study of 400 randomly selected adults finds: 55% prefer Brand A, MoE $\pm 4\%$. Which conclusion is best supported?
A) The proportion of all adults who prefer Brand A is exactly 55%.
B) Between 51% and 59% of the 400 adults prefer Brand A.
C) Between 51% and 59% of all adults prefer Brand A.
D) Brand A is preferred by a majority of adults.

✅ C - CI applies to the population parameter.

❌ **A:** "Exactly" is wrong for sample estimates. ❌ **B:** The sample already knows it found 55%. ❌ **D:** "Majority" (>50%) is plausible but not the best supported conclusion - the CI range is more precise.

### [Medium] Which Statement is NOT Supported? (Improvement 39)
A scatterplot with a line of best fit shows donation amount (x) and fundraising total (y). The line has equation $y = 3x + 500$ for $0 \leq x \leq 100$. Which is NOT supported?
A) For each additional dollar donated, fundraising total increases by about $3.
B) When no donations are made, the predicted fundraising total is $500.
C) For a donation of $200, the predicted total is $1,100.
D) The relationship between donation amount and fundraising total is approximately linear.

✅ C - $x=200$ is outside the data range ($0 \leq x \leq 100$), making this an extrapolation.

❌ **A:** Correct interpretation of slope. ❌ **B:** Correct interpretation of $y$-intercept. ❌ **D:** The line of best fit suggests an approximately linear relationship (within range).

### [Medium] Which Graph Matches Data? (Improvement 40)
A dataset: symmetric, mean=50, median=50, SD=10. Which histogram matches?
A) Peak at 30, tail to the right
B) Two peaks at 30 and 70
C) Symmetric peak at 50, spread from 30 to 70
D) Uniform from 40 to 60

✅ C - symmetric with center at 50 and spread of about ±20.

❌ **A:** Skewed right. ❌ **B:** Bimodal. ❌ **D:** Uniform, not clustered.

### [Hard] Best Model (Improvement 41)
Data points form a clear U-shape. Which model is appropriate?
A) Linear
B) Quadratic
C) Exponential
D) Logarithmic

✅ Quadratic - U-shape means one minimum (or maximum), which is quadratic.

❌ **Linear:** A U-shape is not linear. The rate of change is not constant.

### [Hard] Interpret Residual (Improvement 43)
A linear model predicts home prices. For a 2,000 sq ft home, actual price = $350K, predicted = $330K. Interpret the residual.

✅ Residual = +$20K. The model underestimates the price for this home size.

❌ **Sign error:** "The model overestimates by $20K" - positive residual = actual > predicted = underestimate.

### [Hard] Interpret Parameter (Improvement 44)
$P = 50 + 2t$ predicts power output (watts) at t seconds. Interpret 50 and 2.

✅ 50 = initial power output at t=0. 2 = increase of 2 watts per second.

❌ **Swapped:** "50 is the rate of increase, 2 is the starting value."

### [Hard] Evaluate Study (Improvement 45)
A company surveys customers who called its support line. 90% reported being satisfied. Can the company claim 90% of all customers are satisfied?

✅ No - only customers who called were surveyed (convenience sample). Customers who never called may have different satisfaction levels.

❌ "90% is high enough to prove satisfaction" - the sample is biased toward those who sought support.

### [Very Hard] Explain Why Conclusion is Invalid (Improvement 47)
A school finds that students who participate in sports have higher GPAs. The principal concludes: "Sports participation causes higher grades." Why is this conclusion invalid?

✅ It's an observational study - students who choose sports may differ from non-participants (motivation, time management, family support). No random assignment means causation cannot be inferred.

❌ "Not enough data" - the flaw is study design (observational, not experimental), not sample size.

---

# 12. Mixed Review - 18 Completely Mixed B3 Questions

Test yourself across all B3 topics. Covers ratios, percentages, stats, scatterplots, probability, inference, and study design.

---

**1. [Easy] Ratios**  
A recipe for 6 servings uses 2 cups of flour. How many cups for 15 servings?  
A) 4   B) 5   C) 6   D) 7

$\frac{2}{6} = \frac{x}{15} \implies x = 5$ (B)

---

**2. [Easy] Percentages**  
A shirt costs $60. It is on sale for 25% off. What is the sale price?  
A) $15   B) $35   C) $45   D) $55

$60 \times 0.75 = 45$ (C)

❌ **Add-back:** $60 - 25 = 35$ - subtracts percentage points, not percent of price.

---

**3. [Easy] Statistics**  
A dataset has values: 5, 8, 12, 15, 20. What is the median?  
A) 8   B) 10   C) 12   D) 14

Sorted: 5, 8, 12, 15, 20. Median = 12 (C)

---

**4. [Medium] Probability**  
A bag has 4 red marbles and 6 blue marbles. You draw 2 marbles with replacement. What is the probability both are red?  
A) 0.16   B) 0.24   C) 0.36   D) 0.40

$(4/10) \times (4/10) = 0.16$ (A)

❌ **Without replacement:** $(4/10) \times (3/9) \approx 0.133$ - the problem says "with replacement."

---

**5. [Medium] Scatterplots**  
A line of best fit has equation $y = 1.5x + 10$. What is the predicted $y$ when $x = 12$?  
A) 18   B) 22   C) 28   D) 30

$1.5(12) + 10 = 28$ (C)

---

**6. [Medium] Inference**  
A survey of 300 randomly selected voters finds 48% support a policy, MoE $\pm 5\%$. What is the plausible range for the true support?  
A) 43% to 53%   B) 45% to 51%   C) 48% to 53%   D) 43% to 48%

$48\% \pm 5\% = [43\%, 53\%]$ (A)

---

**7. [Medium] Study Design**  
A study randomly assigns 50 students to a new teaching method and 50 to traditional. The new method group scores higher. What can be concluded?  
A) The method causes higher scores for these students  
B) The method works for all students  
C) There is an association but not causation  
D) The study is invalid due to small sample size

✅ A - random assignment enables causal claims for the study participants.

❌ **B:** Can't generalize beyond participants (not random sample). ❌ **C:** Random assignment allows causation. ❌ **D:** 100 students is adequate for a valid experiment.

---

**8. [Medium] Box Plot**  
Box plot A: median = 60, IQR = 10. Box plot B: median = 55, IQR = 25. Which is true?  
A) A has higher center and less spread  
B) A has lower center and more spread  
C) B has higher center and less spread  
D) B has higher center and more spread  

✅ A - median 60 > 55, IQR 10 < 25.

---

**9. [Medium] Unit Conversion**  
A car travels at 30 meters per second. How many kilometers per hour?  
A) 54   B) 72   C) 90   D) 108

$30 \times 3600 / 1000 = 108$ km/h (D)

❌ **Decimal error:** $30 \times 3.6 = 108$ - the shortcut works but only if you know the conversion factor (3.6).

---

**10. [Hard] Percentages + Ratios**  
A store marks up an item by 30%, then discounts it by 20%. What is the final price as a percent of the original?  
A) 104%   B) 106%   C) 110%   D) 96%

$1.30 \times 0.80 = 1.04 = 104\%$ (A)

❌ **Additive:** $30\% - 20\% = 10\%$ gain. Actual is $104\%$, so a 4% gain, not 10%.

---

**11. [Hard] Two-Way Table Probability**

| | Pass | Fail | Total |
|---|------|------|-------|
| Homework done | 80 | 20 | 100 |
| Homework not done | 30 | 50 | 80 |
| Total | 110 | 70 | 180 |

What is $P$(\text{pass | homework done})?  
A) 80/180   B) 80/100   C) 80/110   D) 80/70

$80/100 = 0.8$ (B)

❌ **Grand total:** 80/180. ❌ **Wrong condition:** 80/110 (that's $P$(\text{homework | pass})).

---

**12. [Hard] Distribution Shape**  
A histogram shows two clear peaks separated by a gap. The mean is near the middle of the range, where almost no data exists. What shape is this?  
A) Skewed right   B) Symmetric   C) Bimodal   D) Uniform

✅ Bimodal (C) - two peaks with a gap.

---

**13. [Hard] Confidence Interval**  
A 95% CI for mean weight is (145, 165). Which value is LEAST plausible for the true mean?  
A) 148   B) 155   C) 160   D) 170

✅ D - 170 is outside the interval (145, 165).

❌ **A/B/C:** All fall within the CI range.

---

**14. [Very Hard] Scatterplot + Percent Change + Inference**  
A linear model predicts sales ($y$) from advertising spend ($x$) in thousands: $y = 8x + 20$. The data ranges from $x = 0$ to $x = 50$.

A) What is the predicted sales when advertising spend is $30K?  
B) What is the predicted percent increase in sales from $x=0$ to $x=25$?

A) $8(30) + 20 = 260$ thousand  
B) At $x=0$: $y = 20$. At $x=25$: $y = 8(25) + 20 = 220$.  
Percent increase: $(220 - 20)/20 = 200/20 = 1000\%$

❌ **Part B base error:** $(220-20)/220 \approx 91\%$ - percent change always divides by original, not new.

---

**15. [Very Hard] Study Design - Evaluate Two Studies**  
Study 1: Survey 2,000 randomly selected adults. 40% exercise weekly.  
Study 2: Randomly assign 100 adults to exercise program or control. Exercise group has lower BMI.

Which conclusions are supported?

✅ Study 1: 40% of adults exercise weekly (generalization from random sample), MoE applies.  
✅ Study 2: Exercise causes lower BMI (causation from random assignment), though generalization is limited.

❌ Study 1: "Exercise prevents obesity" - no causation from survey. ❌ Study 2: "Exercise lowers BMI for all adults" - participants were volunteers, not random sample.

---

**16. [Hard] Percent Error**
A scientist estimates a population at 1,100, but the actual count is 1,000. What is the percent error of the estimate?
A) 9.1%   B) 10%   C) 11.1%   D) 110%

$\frac{|1100 - 1000|}{1000} = 10\%$ (B)

❌ **Estimate base:** $\frac{100}{1100} \approx 9.1\%$ - divide by the actual value, not the estimate.

---

**17. [Hard] Linear vs Exponential Growth**
Quantity A: 200, 240, 280, 320. Quantity B: 200, 240, 288, 345.6. Which best describes the two quantities?

A grows by a constant 40 each step (linear). B grows by 20% each step - constant ratio 1.2 (exponential).

❌ **"Both are linear because both increase"** - constant differences = linear; constant ratios = exponential.

---

**18. [Very Hard] Reverse Probability from a Table**
In a survey of 300 people, 120 are under 30. Given that a person is under 30, the probability of preferring streaming over cable is 0.75. Given that a person is 30 or older, that probability is 0.5. How many people prefer streaming?

Under 30: $0.75 \times 120 = 90$. 30 or older: $300 - 120 = 180$; $0.5 \times 180 = 90$.  
Total: $90 + 90 = 180$.

❌ **Blending the probabilities:** averaging 0.75 and 0.5, or using $0.75 \times 300$ - each conditional probability must be applied to its own group size.

---

---

---

[Hard] A sphere of radius 6 has density 2.5 g/cm$^3$. Find mass.

$V = \frac{4}{3}\pi(6)^3 = 288\pi$ cm$^3$
$m = 2.5 \cdot 288\pi = 720\pi$ grams
