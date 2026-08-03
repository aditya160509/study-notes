#!/usr/bin/env python3
"""Surgical expansion of sat_b3_data.md - every insertion asserts a unique anchor.
Preserves ALL existing content (verified line-by-line at the end)."""
import sys

PATH = "/Users/adityabalaji/Documents/Codex/sat/sat_b3_data.md"

with open(PATH, "r", encoding="utf-8") as f:
    orig = f.read()

orig_lines = orig.split("\n")

# ---------------- content blocks (raw strings: backslashes are literal) ----------------

S00 = r"""## 0. Most Common Question Types on the Actual Exam

Domain B3 gives you 5-7 of the 44 Math questions (~15%). Based on the official College Board Assessment Framework (Table A36) and released digital SAT items, these archetypes show up over and over. Master this list first, then drill the sections.

| # | Question type (official testing point) | Where | One-line strategy |
|---|----------------------------------------|-------|-------------------|
| 1 | Percent change, repeated percent change, discounts/markup/tax/interest | B3.2 | Convert every change to a multiplier; multiply multipliers, never add percents |
| 2 | Unit conversion with derived units (density, speed, population density, square/cubic units) | B3.1 | Write conversion factors as fractions that cancel; square/cube the factor for area/volume |
| 3 | Mean, median, range comparison; effect of outliers; SD interpretation without calculation | B3.3 | Mean follows outliers, median resists them; SD is about spread around the center |
| 4 | Conditional probability from a two-way table ("given that", "among", "of those who") | B3.5 | Denominator = total of the condition group, never the grand total |
| 5 | Margin of error and inference: which conclusion is supported | B3.6 | Statistic ± MoE = plausible range for the parameter; "exactly" is always wrong |
| 6 | Scatterplot line of best fit: interpret slope or y-intercept, or predict | B3.4 | Read from the line, not the points; slope = per-unit change |
| 7 | Study design: random sample vs random assignment, confounding variables | B3.7 | Random selection generalizes; random assignment implies causation |

Frequency notes from the official framework:
- Ratios/rates/units (B3.1) plus percentages (B3.2) together account for roughly half of B3 questions (Table 23: B3.1 is 20-30% of the domain, B3.2 is 15-20%).
- Grid-in answers are common for percent change and unit conversion questions, so practice entering exact decimals and fractions.
- The framework says "infrequently": given a probability, determine an unknown number in a two-way table (reverse probability). It is rare, but it does appear - see B3.5.
- B3.6 and B3.7 (inference and study design) are the most predictable points on the exam: the answer hinges on one or two keywords ("randomly selected" vs "randomly assigned", "plausibly" vs "exactly").

---
"""

# ---- formula sheet additions ----
S01 = r"""| Percent error | $\frac{|\text{estimated} - \text{actual}|}{\text{actual}} \times 100\%$ (divide by actual, not estimate) |
| Simple interest | $I = Prt$; total $= P(1 + rt)$ |
"""
S02 = r"""| Scale factor property | If $x$ changes by factor $k$, a proportional $y$ changes by the same factor $k$ |
| Derived units (product) | e.g., kilowatt-hours = power (kW) × time (h) |
| Derived units (quotient) | e.g., population density = population ÷ area |
"""
S03 = r"""| Relative frequency | $\frac{\text{category frequency}}{\text{total}}$ - an empirical probability |
| Area model | $P(\text{event}) = \frac{\text{area of favorable region}}{\text{total area}}$ |
| Reverse probability | Given $P(A|B)$ and total of $B$: cell count $= P(A|B) \times (\text{total of } B)$ |
"""
S04 = r"""| Median position (odd $n$) | $\frac{n+1}{2}$-th value of the sorted data |
| Median position (even $n$) | average of the $\frac{n}{2}$-th and $\left(\frac{n}{2}+1\right)$-th values |
"""

# ---- B3.1 ----
S05 = r"""# B3.1 Ratios, Rates, Proportional Relationships, and Units

## B3.1.1 Core Concepts: Definitions and Methods
"""
S06 = r"""

**Universal method for ratio/rate/unit problems (4 steps):**
1. Identify the two quantities and the relationship (direct proportion, inverse proportion, or derived unit).
2. Write the conversion factors (or the ratio) as fractions that carry their units; cancel units before calculating.
3. For area, square the conversion factor; for volume, cube it.
4. Check that the answer has the units the question asks for, then sanity-check magnitude (a mile is large, a liter is small).

**Scale factor property (official testing point):** when two quantities are in a proportional relationship and one changes by a factor $k$, the other changes by the same factor $k$. If $x$ doubles, a proportional $y$ doubles. This is often faster than cross-multiplying.

**Derived units from products and quotients (official testing point):**
- Product-derived: kilowatt-hours = power (kW) × time (h) - energy consumed by an appliance.
- Quotient-derived: population density = population ÷ area, speed = distance ÷ time, fuel economy = miles ÷ gallon.
- The SAT hides the math inside the units: convert the unit correctly and the arithmetic becomes trivial.

**Desmos tip:** type the whole conversion as one expression and let Desmos do the arithmetic, e.g. `30 * 1.609 / 3.785` for miles per gallon to km per liter. Desmos handles the decimals; you must supply the conversion factors.
"""
S07 = r"""## B3.1.2 Worked Examples by Difficulty
"""
S08 = r"""### [Easy] Direct Variation
$y$ varies directly with $x$. When $x = 3$, $y = 12$. What is $y$ when $x = 7$?

$k = \frac{y}{x} = \frac{12}{3} = 4$, so $y = 4x$ and $y = 4(7) = 28$.

❌ **Inverse setup:** $xy = 36$, giving $y = 36/7$ - direct variation uses $y = kx$, not $xy = k$.

### [Medium] Scale Factor Property
The number of gallons of paint needed is proportional to the wall area painted. 3 gallons cover 900 ft$^2$. How many gallons cover 2,100 ft$^2$?

Scale factor: $\frac{2100}{900} = \frac{7}{3}$. Gallons scale by the same factor: $3 \times \frac{7}{3} = 7$ gallons. (Or cross-multiply: $\frac{3}{900} = \frac{g}{2100} \implies g = 7$.)

❌ **Additive reasoning:** "2,100 is 1,200 more, so add 4 gallons" - the relationship is multiplicative, not additive.

### [Medium] Population Density (Derived Unit)
A city has 1,200,000 people spread over 480 km$^2$. What is the population density?

$\frac{1{,}200{,}000}{480} = 2{,}500$ people per km$^2$.

❌ **Unit mismatch:** writing "2,500 people per m$^2$" - the answer must carry the same area unit as the data (km$^2$).

### [Hard] Kilowatt-Hours (Derived Unit from a Product)
A 1,200-watt appliance runs 2.5 hours per day for 30 days. At $0.15 per kilowatt-hour, what is the total cost?

Power: $1200 \text{ W} = 1.2 \text{ kW}$.  
Energy: $1.2 \times 2.5 \times 30 = 90$ kWh.  
Cost: $90 \times 0.15 = \$13.50$.

❌ **Unit slip:** using 1,200 kW instead of 1.2 kW gives \$13,500 - watts must be converted to kilowatts before multiplying by hours.

### [Hard] Multidimensional Unit Conversion
A car gets 30 miles per gallon. Convert this to kilometers per liter. (1 mile = 1.609 km; 1 gallon = 3.785 L.)

$\frac{30 \text{ mi}}{1 \text{ gal}} \times \frac{1.609 \text{ km}}{1 \text{ mi}} \times \frac{1 \text{ gal}}{3.785 \text{ L}} = \frac{30 \times 1.609}{3.785} \approx 12.75$ km/L.

❌ **One-direction conversion:** converting only the miles or only the gallons - in a derived unit, both units must be converted.

### [Very Hard] Inverse Variation with Percent
$x$ and $y$ vary inversely. If $x$ increases by 25%, by what percent does $y$ change?

$x$ becomes $1.25x$. Since $xy = k$, $y$ becomes $\frac{k}{1.25x} = 0.8y$, a decrease of 20%.

❌ **Same-factor error:** "y increases by 25% too" - inverse variation multiplies $y$ by the reciprocal $\frac{1}{1.25} = 0.8$, not by 1.25.

### [Very Hard] Derived Unit in Two Steps
A pool is filled at 20 gallons per minute. How many cubic feet of water enter per hour? (1 ft$^3$ $\approx$ 7.48 gallons.)

Per hour: $20 \times 60 = 1{,}200$ gal/h.  
Convert: $\frac{1{,}200}{7.48} \approx 160.4$ ft$^3$ per hour.

❌ **Forgetting the hour:** answering 2.67 ft$^3$ (per minute) when the question asks per hour - always check the time unit in the answer.

"""

# ---- B3.2 ----
S09 = r"""# B3.2 Percentages

## B3.2.1 Core Concepts: Definitions and Methods
"""
S10 = r"""## B3.2.2 Worked Examples by Difficulty
"""
S11 = r"""

**Universal 4-step method for any percent problem:**
1. Write the base (the "old" or "original" amount) in words - it is the denominator of any change.
2. Decide the operation: "of" = multiply; "change" = $\frac{\text{new} - \text{old}}{\text{old}}$; "more/less than" = multiply by $1 \pm p/100$.
3. Convert the percentage to a multiplier or a decimal first; never carry the % sign through the calculation.
4. Sanity check: an increase over 100% gives a multiplier above 2; a discount always gives a multiplier below 1.

**Percent error (error margin percentage) - official testing point:** $\frac{|\text{estimated} - \text{actual}|}{\text{actual}} \times 100\%$. Always divide by the actual (true) value, and use absolute value so the error is nonnegative. The SAT asks this as "percent error", "error margin", or "how far off is the estimate".

**Percentages greater than or equal to 100% (official testing point):** 100% of a number is the number itself; 150% of a number is 1.5 times it. An increase of 150% means the new value is 250% of the old (multiplier 2.5); a "200% increase" triples the value.

**Simple interest:** $I = Prt$ where $P$ is the principal, $r$ is the annual rate as a decimal, $t$ is time in years; total $= P(1 + rt)$. Compound interest (see Compound growth above) uses $A = P(1+r)^n$. The wording decides: "simple interest" says so explicitly; "compounded annually" means compound.

**Desmos tip:** chain multipliers in one line: `150 * 1.30 * 0.85` for a 30% markup followed by a 15% discount; `45 / 0.75` for reverse percent.
"""
S12 = r"""### [Easy] Percent Error
An estimate of 45 is made for a value that is actually 50. What is the percent error?

$\frac{|45 - 50|}{50} = \frac{5}{50} = 10\%$.

❌ **Wrong base:** $\frac{5}{45} \approx 11.1\%$ - percent error divides by the actual value, not the estimate.

### [Easy] Percent Greater than 100
A value increases from 40 to 100. What is the percent increase?

$\frac{100 - 40}{40} = \frac{60}{40} = 150\%$. The new value is 250% of the old.

❌ **"Doubled" error:** "100 is 2.5 times 40, so a 250% increase" - a 250% increase would make the value $40 \times 3.5 = 140$. The increase is 150%.

### [Medium] Tip
A meal costs $65. An 18% tip is added. What is the total?

Tip: $65 \times 0.18 = 11.70$. Total: $65 + 11.70 = \$76.70$. Or directly: $65 \times 1.18 = \$76.70$.

❌ **Adding the percent:** $65 + 18 = 83$ - 18% of the bill is not 18 dollars.

### [Medium] Error Margin with Wording
A measurement has a percent error of 5%. The actual value is 200. What is the largest possible measured value?

$200 \times 1.05 = 210$.

❌ **Off-by-one:** "200 + 5 = 205" - 5% of 200 is 10, so the error allowance is 10 units, not 5.

### [Hard] Simple vs Compound Interest
$1,000 is invested at 5% per year for 2 years. Compare the totals under simple interest vs interest compounded annually.

Simple: $1000(1 + 0.05 \times 2) = \$1{,}100$.  
Compound: $1000(1.05)^2 = \$1{,}102.50$.  
Compounding earns an extra $2.50 - interest on the first year's interest.

❌ **Treating them the same:** over longer periods compounding grows much faster; "compounded annually" vs "simple interest" changes the calculation.

### [Very Hard] Percent Error in a Chain
A company predicted $230{,}000 in sales but actual sales were $200{,}000. By what percent did the prediction miss the actual? The next year, actual sales rise by 25%. What is the new actual?

Error: $\frac{|230{,}000 - 200{,}000|}{200{,}000} = 15\%$ overestimate.  
Next year: $200{,}000 \times 1.25 = \$250{,}000$.

❌ **Mixing bases:** computing the error against the prediction ($\frac{30{,}000}{230{,}000} \approx 13\%$) and applying the 25% growth to the prediction - percent error always uses the actual as base, and the growth applies to the actual.

### [Very Hard] Repeated Percent Change with Unknown Original
After a 15% discount and then an additional 20% discount on the discounted price, an item sells for $51. What was the original price?

Combined multiplier: $0.85 \times 0.80 = 0.68$.  
Original: $\frac{51}{0.68} = \$75$.

❌ **Sequential add-back:** $51 \times 1.15 = 58.65$ then $\times 1.20$ - forward discounts apply to shrinking bases, so the reverse is a single division by the product of the multipliers.

"""

# ---- B3.2.5 ----
S13 = r"""## B3.2.5.1 The 7 Key Wording Patterns
"""
S14 = r"""## B3.2.5.2 Worked Examples by Difficulty
"""

# ---- B3.3 ----
S15 = r"""## B3.3.1 Measures of Center
"""
S16 = r"""## B3.3.2 Distribution Shape
"""
S17 = r"""## B3.3.3 Measures of Spread
"""
S18 = r"""## B3.3.4 Effect of Transformations
"""
S19 = r"""## B3.3.5 Reading Displays
"""
S20 = r"""## B3.3.6 Comparing Distributions: Center and Spread (Official Testing Point)

The framework explicitly tests comparing distributions, including:
- **Different means, same standard deviation:** two data sets can be centered far apart (different location) yet have identical spread. Example: A = {90, 100, 110} and B = {40, 50, 60} both have SD of 10 but means of 100 and 50. The histogram of B is the histogram of A shifted left - same shape, different location.
- **Same mean, different standard deviations:** A = {95, 100, 105} and B = {50, 100, 150} both have mean 100, but B is far more spread out (larger SD).
- **Rule of thumb:** when comparing two distributions, center (mean or median) describes location; SD, IQR, and range describe spread. A comparison question is answered by naming which property changed: "the new histogram has the same spread but a smaller mean".

**Outliers (official testing point):** an outlier is a value far from the rest of the data. It pulls the mean toward it, barely moves the median, and inflates the range and SD. If a question asks which measure is "least affected" or "most resistant", the answer is the median (or mode); if it asks which is "most affected", the answer is the mean (or range).

**Method for "which set has larger SD" questions:** sketch or visualize the dot plot or histogram, locate the center, then ask: on average, how far are the values from the center? More values far from the center = larger SD. Never compare ranges alone, and never try to compute - the SAT only asks for comparison.

## B3.3.7 Worked Examples by Difficulty
"""
S21 = r"""### [Easy] Missing Value from the Mean
The mean of 5 numbers is 12. Four of them are 8, 10, 14, and 16. What is the fifth number?

Sum: $5 \times 12 = 60$. Known sum: $8 + 10 + 14 + 16 = 48$. Fifth: $60 - 48 = 12$.

❌ **Averaging the knowns:** "mean of 8, 10, 14, 16 is 12, so the fifth is 12" - works here only by coincidence; always use sums.

### [Easy] Mode with Ties
Find the mode(s) of {2, 2, 3, 3, 4, 7} and of {1, 5, 8, 9}.

{2, 2, 3, 3, 4, 7} has two modes: 2 and 3. {1, 5, 8, 9} has no mode - every value occurs once.

❌ **Forcing one answer:** "the mode is 2" - a data set can have multiple modes or none.

### [Medium] Combined Mean
The mean of 6 numbers is 10, and the mean of 4 other numbers is 15. What is the mean of all 10 numbers?

Total sum: $6 \times 10 + 4 \times 15 = 120$. Mean: $\frac{120}{10} = 12$.

❌ **Simple average:** $\frac{10 + 15}{2} = 12.5$ - groups of different sizes must be weighted by size.

### [Medium] Different Means, Same SD
Histogram A is centered at 60 with most values between 55 and 65. Histogram B is centered at 30 with most values between 25 and 35. Which has the larger mean? Which has the larger SD?

A has the larger mean (60 > 30). The SDs are essentially the same - both spread about 5 units around their centers.

❌ **Conflating center and spread:** "A is higher, so it must be more spread out" - location and spread are independent properties.

### [Medium] Effect of an Outlier (Numerical)
Find the mean and median of {2, 3, 4, 5, 100}.

Mean: $\frac{114}{5} = 22.8$. Median: 4 (the middle of the sorted list).

❌ **Saying the median "also jumps":** the median stays 4 - the outlier at 100 only moved the mean.

### [Hard] Adding a Value that Raises the Mean
The mean of 5 numbers is 8. One more number is added and the mean becomes 9. What was the added number?

Old sum: $5 \times 8 = 40$. New sum: $6 \times 9 = 54$. Added number: $54 - 40 = 14$.

❌ **Guess and check:** raising the mean of 6 values by 1 requires a total increase of 6, so the new value must be 14, not 9.

### [Hard] Mean Equals Median
For {3, 5, 7, x} with $x \geq 7$, find $x$ so that the mean equals the median.

Median: $\frac{5 + 7}{2} = 6$. Mean: $\frac{15 + x}{4} = 6 \implies x = 9$.

❌ **Assuming x is the largest:** if $x$ came out below 7, the sorted order (and the median) would change - check consistency after solving.

### [Very Hard] Same Mean, Different SD
Set A = {95, 100, 105}; Set B = {50, 100, 150}. Both have mean 100. Which has the larger standard deviation?

B. In A every value is within 5 of the mean; in B the values are 50 away from the mean.

❌ **Equal means = equal spread:** the mean says nothing about the SD; spread depends on distances from the mean, not on the mean itself.

### [Very Hard] Which Measure is Least Affected by an Outlier?
In a data set, one value is replaced by a much larger value. Which measure changes the least?

The median (and the mode). The mean, range, and SD all respond to the change.

❌ **"The range":** the range uses only the extremes, so replacing the maximum with a bigger maximum changes the range dramatically - it is not resistant.

"""

# ---- B3.4 ----
S22 = r"""# B3.4 Two-Variable Data: Scatterplots and Models

## B3.4.1 Core Concepts: Definitions and Methods
"""
S23 = r"""## B3.4.2 Choosing a Model
"""
S24 = r"""## B3.4.3 Prediction: Interpolation vs Extrapolation
"""
S25 = r"""## B3.4.4 Reading Graphs
"""
S26 = r"""## B3.4.5 Worked Examples by Difficulty
"""
S27 = r"""

**Correlation vs causation (flagged gap):** a scatterplot or fitted model only ever shows association. Never answer "the increase in $x$ causes the increase in $y$" unless the context describes random assignment in an experiment. The SAT plants this trap in two-variable data questions too, not only in B3.6 and B3.7.

**Compare linear and exponential growth (official testing point):**
- Linear: the same amount is added each step (constant first differences). $y = mx + b$.
- Exponential: the same factor multiplies each step (constant ratios). $y = a \cdot b^x$.
- Given a table, compute consecutive differences and ratios: constant differences → linear; constant ratios → exponential. Given a graph, a straight line → linear; a curve that steepens or flattens → exponential.
- Classic question: two quantities start at the same value, one grows by a fixed amount per year, the other by a fixed percent per year. The exponential one eventually overtakes - even a modest percent beats a fixed amount over enough time.

**Desmos tip:** enter the data as a table ($x_1$, $y_1$) and fit both `y_1 ~ m x_1 + b` and `y_1 ~ a * b^{x_1}`. The model whose $R^2$ is closer to 1 is the better fit; compare the two $R^2$ values directly.
"""
S28 = r"""### [Medium] Which r Matches the Scatterplot
A scatterplot shows points tightly clustered around a line that rises from left to right. Which is the most likely correlation coefficient?
A) -0.9   B) -0.2   C) 0.4   D) 0.9

✅ D. Tight clustering around a rising line = strong positive correlation.

❌ **Sign error:** choosing -0.9 because "the points look strong" - the line rises, so $r$ must be positive.

### [Medium] Compare Linear and Exponential Growth (Table)

| Year | 0 | 1 | 2 | 3 |
|------|---|---|---|---|
| Value | 100 | 115 | 130 | 145 |

Is the growth linear or exponential?

First differences: 15, 15, 15 - constant, so linear: $y = 100 + 15t$.

❌ **"It grows, so exponential"** - growth alone is not enough; constant addition is linear, constant multiplication is exponential.

### [Hard] Compare Linear and Exponential Growth (Same Start)
Function A starts at 100 and adds 50 each year. Function B starts at 100 and grows by 40% each year. Which is larger after 5 years?

A: $100 + 5 \times 50 = 350$.  
B: $100(1.4)^5 \approx 537.8$.  
B overtakes A between year 3 (250 vs 274.4) and year 4 (300 vs 384.16).

❌ **Short-horizon intuition:** A is ahead early (150 vs 140 after year 1), but the exponential multiplier compounds and wins by year 5.

### [Hard] Exponential Model from Two Points
A quantity grows exponentially and passes through (0, 5) and (2, 20). What is its value at $x = 3$?

$y = a \cdot b^x$ with $a = 5$ (the value at $x = 0$). Then $5b^2 = 20 \implies b^2 = 4 \implies b = 2$.  
$y(3) = 5 \cdot 2^3 = 40$.

❌ **Linear interpolation:** "between 20 and 40, so 30" - exponential growth is multiplicative, so the value at $x = 3$ is $20 \times 2 = 40$, not a midpoint.

### [Very Hard] Association Flag in Scatterplot Context
A scatterplot of ice cream sales vs drowning incidents shows a strong positive correlation. Which conclusion is valid?

✅ Sales and drownings are associated; a third variable (hot weather) likely drives both. Correlation alone never supports "ice cream causes drownings".

❌ **Causal claim:** "selling ice cream leads to more drownings" - without an experiment (random assignment), only association is supported.

"""

# ---- B3.5 ----
S29 = r"""# B3.5 Probability and Conditional Probability

## B3.5.1 Core Concepts: Definitions and Methods
"""
S30 = r"""## B3.5.2 Worked Examples by Difficulty
"""
S31 = r"""

**Relative frequency:** the proportion of a category in a data display, $\frac{\text{category frequency}}{\text{total}}$. It is an empirical probability - the framework treats "relative frequency, probabilities, and conditional probabilities" as one family of skills.

**Area model (official representation):** when outcomes are equally likely and represented by area, $P(\text{event}) = \frac{\text{area of favorable region}}{\text{total area}}$. Used for dartboards, shaded squares in grids, and spinner sectors. Compute the areas with geometry, then divide.

**Reverse probability (official testing point, appears infrequently):** the SAT sometimes gives you a probability and asks you to find a missing cell in a two-way table. Method: write the probability equation with the unknown, then solve. Example: if $P(\text{passed}|\text{studied}) = 0.75$ and 80 students studied, then the number who studied and passed is $0.75 \times 80 = 60$.

**Method for two-way table probability (5 steps):**
1. Locate the condition word ("given that", "among", "of those who") - it names the denominator group.
2. Read the row or column total for that group from the table.
3. Read the cell where the condition group and the target event intersect.
4. Divide: $\frac{\text{intersection cell}}{\text{condition group total}}$.
5. If the probability is given instead, multiply it by the group total to recover the cell.

**Organize by type (as the framework does):**
- Independent events: the occurrence of one does not change the probability of the other. $P(A \cap B) = P(A)P(B)$.
- Dependent events: the probability of the second changes because the first removed an outcome (drawing without replacement).
- Mutually exclusive events: cannot happen together, $P(A \cap B) = 0$; they are automatically dependent (unless one has probability 0).
- Complements: $P(\text{not } A) = 1 - P(A)$; "at least one" = $1 - P(\text{none})$.

**Desmos tip:** type probabilities as fractions, e.g. `100/120`, and read the exact fraction; for a reverse-probability cell, just multiply: `0.75 * 80`.
"""
S32 = r"""### [Easy] Independent Events Multiplication
$P(A) = 0.4$ and $P(B) = 0.5$, with A and B independent. What is $P(A \text{ and } B)$?

$0.4 \times 0.5 = 0.2$.

❌ **Adding:** $0.4 + 0.5 = 0.9$ - that is only correct for mutually exclusive events; independent events multiply.

### [Easy] Mutually Exclusive
$P(A) = 0.3$ and $P(B) = 0.4$, with A and B mutually exclusive. What is $P(A \text{ or } B)$?

$0.3 + 0.4 = 0.7$ (no overlap to subtract).

❌ **Subtracting an overlap:** $0.3 + 0.4 - P(A)P(B)$ - mutually exclusive means $P(A \cap B) = 0$, so there is no overlap term.

### [Medium] Area Model Probability
A square dartboard of side 20 cm has a shaded circle of radius 5 cm at its center. A dart lands uniformly at random. What is the probability it lands in the shaded region?

$\frac{\pi(5)^2}{20^2} = \frac{25\pi}{400} = \frac{\pi}{16} \approx 0.196$.

❌ **Length ratio:** $\frac{5}{20} = 0.25$ - area probabilities use area ratios, so the radius must be squared (and $\pi$ included).

### [Medium] Reverse Probability - Find the Cell
In a survey, 120 students were asked whether they studied for a test. Of those who studied, 80% passed. How many students both studied and passed?

$0.80 \times 120 = 96$ students.

❌ **Using the grand total:** $0.80 \times 200$-style setups need a grand total that is not given; here the condition group is given (120 studied), so multiply the conditional probability by 120.

### [Hard] Reverse Probability - Unknown Cell in a Two-Way Table
In a group of 400 people, 160 are female. If $P(\text{prefers A}|\text{female}) = 0.4$, how many females prefer A?

$0.4 \times 160 = 64$ females.

❌ **Using the grand total:** $0.4 \times 400 = 160$ - the condition is "female", so the denominator group is 160, not 400.

### [Hard] Exactly One
$P(A) = 0.5$, $P(B) = 0.4$, $P(A \cap B) = 0.2$. What is the probability that exactly one of A or B occurs?

$P(A) + P(B) - 2P(A \cap B) = 0.5 + 0.4 - 0.4 = 0.5$.

❌ **Addition rule shortcut:** $0.5 + 0.4 - 0.2 = 0.7$ is $P(A \text{ or } B)$ (at least one), which double-counts the both case.

### [Very Hard] Reverse Probability Determining Frequency (Official)
A two-way table has 200 students. The probability that a randomly chosen student passed given that the student did homework is 0.8, and 80 students did homework. The probability that a student passed given that the student did not do homework is 0.3. How many students passed in total?

Passed and did homework: $0.8 \times 80 = 64$.  
Did not do homework: $200 - 80 = 120$; passed: $0.3 \times 120 = 36$.  
Total passed: $64 + 36 = 100$.

❌ **Blending the probabilities:** averaging 0.8 and 0.3, or multiplying either by 200 - each conditional probability must be applied to its own condition group size.

"""

# ---- B3.6 ----
S33 = r"""# B3.6 Inference from Sample Statistics

## B3.6.1 Core Concepts: Definitions and Methods
"""
S34 = r"""## B3.6.2 Confidence Intervals - What's Plausible?
"""
S35 = r"""## B3.6.3 Sample Size Reasoning
"""
S36 = r"""## B3.6.4 Sampling Methods
"""
S37 = r"""## B3.6.5 Sources of Bias
"""
S38 = r"""## B3.6.6 Wording Traps
"""
S39 = r"""## B3.6.7 Worked Examples by Difficulty
"""
S40 = r"""

**Method for any margin-of-error conclusion question (4 steps):**
1. Compute the interval: statistic ± MoE.
2. The interval describes the population parameter (the true proportion or true mean) - never the sample, never individuals.
3. "Plausibly", "could be", "approximately" are correct; "exactly", "certainly", "definitely" are wrong.
4. Generalization is valid only to the population the sample was randomly drawn from.

**Confidence level interpretation:** "95% confidence" describes the method, not the data: if the sampling process were repeated many times, about 95% of the resulting intervals would capture the true parameter. It does NOT mean "95% of the population falls in this range", and it does not assign a probability to any single interval.

**Sample mean and sample proportion (official testing point):** the sample mean $\bar{x}$ is the best estimate of the population mean $\mu$; the sample proportion $\hat{p}$ is the best estimate of the population proportion $p$. To estimate a total for a population of size $N$: $\hat{p} \times N$.

**Which population can results extend to? (official testing point):** results extend only to the population the sample was drawn from. A random sample of registered voters in Ohio extends to registered voters in Ohio - not to all Americans, and not to all Ohioans (some are not registered).
"""
S41 = r"""### [Easy] Sample Mean Estimates Population Mean
A random sample of 300 commuters has a mean commute of 28 minutes. What is the best estimate of the mean commute for all commuters?

28 minutes. The sample mean is the estimate of the population mean.

❌ **Inventing a range:** adding or subtracting a margin of error that was not given - without MoE, the single best estimate is the sample mean itself.

### [Medium] Confidence Level Interpretation
A 95% confidence interval for the mean height of adult men is (173, 177) cm. Which statement is correct?
A) 95% of adult men are between 173 and 177 cm tall.
B) The method produces intervals that capture the true mean about 95% of the time.
C) There is a 95% chance the true mean is 175 cm.
D) The sample mean is between 173 and 177 cm.

✅ B. Confidence describes the method across repeated sampling.

❌ **A:** the interval is about the mean, not individual heights. ❌ **C:** no single value inside an interval carries a probability. ❌ **D:** the sample mean is the center (175), a single number, not a range.

### [Hard] Quadruple the Sample Size
A poll of 100 voters has a margin of error of ±8%. If the pollster instead surveys 400 voters (same population), what is the approximate margin of error?

MoE scales with $\frac{1}{\sqrt{n}}$: $\sqrt{\frac{400}{100}} = 2$, so the new MoE is $\frac{8\%}{2} = \pm 4\%$.

❌ **Linear scaling:** "4 times the sample means 1/4 the error = ±2%" - MoE is inversely proportional to the square root of the sample size.

### [Hard] Estimate a Population Total
A random sample of 250 students from a school of 2,000 finds that 40 ride bikes to school. Approximately how many students in the whole school ride bikes?

$\frac{40}{250} = 0.16$; $0.16 \times 2{,}000 = 320$ students.

❌ **Reversed proportion:** setting up $\frac{40}{x} = \frac{250}{2000}$ - keep the sample ratio equal to the population ratio: $\frac{40}{250} = \frac{x}{2000}$.

### [Very Hard] Which Population Can the Results Extend To?
A study randomly samples 500 registered voters in Ohio and finds 52% approve of a policy, MoE ±4%. To which population can the result be generalized?

Registered voters in Ohio - the population from which the sample was drawn.

❌ **"All Americans"** - the sampling frame was Ohio registered voters. ❌ **"All Ohioans"** - unregistered residents were not in the sampling frame.

"""

# ---- B3.7 ----
S42 = r"""# B3.7 Evaluating Statistical Claims & Study Design

## B3.7.1 Core Framework: Observational Studies vs Experiments
"""
S43 = r"""## B3.7.2 Confounding Variables - Quick Recognition
"""
S44 = r"""## B3.7.3 Experimental Design Terminology
"""
S45 = r"""## B3.7.4 Worked Examples by Difficulty
"""
S46 = r"""

**Method for any study-design question (4-step checklist):**
1. Was there random selection from a population? → yes = can generalize (to that population only).
2. Was there random assignment to treatment/control? → yes = can claim causation.
3. Both? → gold standard: generalize AND causation (within the studied population).
4. Neither? → association only; name the confounding variable that offers an alternative explanation.

**Correlation vs causation (flagged gap):** a correlation (or association) does NOT imply causation without random assignment. Every answer choice that says "causes" must be backed by an experiment; every observational study supports only "is associated with".

**The confounding-variable test:** a variable is confounding only if it plausibly affects BOTH the treatment choice AND the outcome. If it affects only one of them, it is not confounding.
"""
S47 = r"""### [Medium] Placebo Effect
In a drug trial, 30% of patients in the placebo group reported improvement. What does this show?

The placebo effect: belief in treatment can produce real reported improvement. This is why the drug must outperform the placebo, not just outperform nothing.

❌ **"The placebo group is useless"** - the placebo group is essential: it measures improvement caused by expectation, which the drug group's improvement must exceed.

### [Medium] Why Double-Blind?
Why do well-designed trials keep both patients and researchers unaware of who received the drug?

It prevents biased reporting (patients who expect improvement report more) and biased assessment (researchers who expect the drug to work evaluate outcomes differently).

❌ **"To protect patient privacy"** - blinding is about eliminating bias in reporting and measurement, not confidentiality.

### [Hard] Blocking by Gender
A study of a new exercise program blocks subjects by gender, then randomly assigns half of each gender to the program and half to control. Why block?

Gender may affect both participation and outcomes. Blocking guarantees each treatment group has balanced gender, removing gender as a confounding variable before analysis.

❌ **"Blocking replaces random assignment"** - blocking is used WITHIN random assignment; it reduces variability from a known confounder but does not remove the need for random assignment.

### [Hard] Generalization vs Causation Together
200 volunteers are randomly assigned to a new diet or a control diet. The diet group loses more weight. What can be concluded?

The diet causes greater weight loss for these participants (random assignment). Generalization to all adults is limited because participants were volunteers, not a random sample.

❌ **"Nothing can be concluded"** - random assignment does justify the causal claim; only the generalization is limited.

"""

# ---- traps ----
S48 = r"""# 9. The 22 Data Analysis Traps
"""
S49 = r"""### Trap 21: Percent Error on the Wrong Base
Percent error divides by the actual value, not the estimate: $\frac{|E - A|}{A}$. An estimate of 90 for an actual 100 is a 10% error, not 11.1%.

### Trap 22: Reverse Probability - Confusing Condition and Cell
Given $P(A|B)$, the cell count is $P(A|B) \times$ (total of B). Never multiply by the grand total - the condition group size is the denominator.

"""

# ---- desmos quick calcs ----
S50 = r"""- **Percent error:** `abs(45 - 50) / 50` → 0.10 (multiply by 100 for %).
- **Reverse probability cell:** if $P(A|B) = 0.8$ and the B total is 120, compute `0.8 * 120` → 96 (the missing cell).
- **Compare linear vs exponential fits:** fit both `y_1 ~ m x_1 + b` and `y_1 ~ a * b^{x_1}`, then compare the two $R^2$ values.
- **Missing value from a mean:** `5 * 12 - (8 + 10 + 14 + 16)` → 12 (the unknown fifth value).
"""

# ---- mixed review ----
S51 = r"""**16. [Hard] Percent Error**
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

"""

# ---------------- operations ----------------
# Each op: (anchor, replacement, description)
OPS = [
    # Section 0 + formula sheet expansions
    ("# 1. Complete Formula Sheet", S00 + "# 1. Complete Formula Sheet", "insert S00 before formula sheet"),
    ("| Percentage points vs % | 4% → 6% = +2 pp, +50% relative |",
     "| Percentage points vs % | 4% → 6% = +2 pp, +50% relative |\n" + S01.rstrip("\n"), "add percent error/simple interest rows"),
    ("| Weighted average | $\\frac{\\sum w_i x_i}{\\sum w_i}$ |",
     "| Weighted average | $\\frac{\\sum w_i x_i}{\\sum w_i}$ |\n" + S02.rstrip("\n"), "add scale factor/derived unit rows"),
    ("| \"At least one\" | $P(\\text{at least one}) = 1 - P(\\text{none})$ |",
     "| \"At least one\" | $P(\\text{at least one}) = 1 - P(\\text{none})$ |\n" + S03.rstrip("\n"), "add relative frequency/area model/reverse prob rows"),
    ("| Multiplying all by $c$ | Mean/median/SD/IQR/range $\\times |c|$ |",
     "| Multiplying all by $c$ | Mean/median/SD/IQR/range $\\times |c|$ |\n" + S04.rstrip("\n"), "add median position rows"),
    # B3.1
    ("# B3.1 Ratios, Rates, Proportional Relationships, and Units\n\n## Core Concepts", S05, "B3.1 core rename"),
    ("## Examples\n\n### [Easy] Unit Rate",
     "## B3.1.2 Worked Examples by Difficulty\n\n### [Easy] Unit Rate", "B3.1 examples rename"),
    ("**Density:** $\\text{mass} = \\text{density} \\times \\text{volume}$. Works same way for population density (population = density × area). (See B4 for volume formulas and geometry reference.)",
     "**Density:** $\\text{mass} = \\text{density} \\times \\text{volume}$. Works same way for population density (population = density × area). (See B4 for volume formulas and geometry reference.)\n" + S06.rstrip("\n"),
     "B3.1 core concepts expansion"),
    ("---\n\n# B3.2 Percentages",
     S08.rstrip("\n") + "\n\n---\n\n# B3.2 Percentages", "B3.1 new examples"),
    # B3.2
    ("# B3.2 Percentages\n\n## Core Concepts", S09, "B3.2 core rename"),
    ("⚡ \"Increase **by**\" vs \"increase **to**\" are the same mathematically (both multiply). But \"increase by 15 **percentage points**\" means addition, not multiplication — common trap.\n\n## Examples",
     "⚡ \"Increase **by**\" vs \"increase **to**\" are the same mathematically (both multiply). But \"increase by 15 **percentage points**\" means addition, not multiplication — common trap.\n\n" + S10.rstrip("\n"),
     "B3.2 examples rename"),
    ("**Percentage points vs %:** 4% → 6% = +2 pp, +50% relative change. Percent of percent: 30% of 40% = $0.30 \\times 0.40 = 12\\%$, **not** subtraction or addition.",
     "**Percentage points vs %:** 4% → 6% = +2 pp, +50% relative change. Percent of percent: 30% of 40% = $0.30 \\times 0.40 = 12\\%$, **not** subtraction or addition.\n" + S11.rstrip("\n"),
     "B3.2 core concepts expansion"),
    ("---\n\n# B3.2.5 Percentage Language — Precision on the SAT",
     S12.rstrip("\n") + "\n\n---\n\n# B3.2.5 Percentage Language — Precision on the SAT", "B3.2 new examples"),
    # B3.2.5
    ("# B3.2.5 Percentage Language — Precision on the SAT\n\nThe SAT tests whether you understand what each percent phrase actually means. The same numbers can produce different answers depending on wording.\n\n## The 7 Key Wording Patterns",
     "# B3.2.5 Percentage Language — Precision on the SAT\n\nThe SAT tests whether you understand what each percent phrase actually means. The same numbers can produce different answers depending on wording.\n\n" + S13.rstrip("\n"),
     "B3.2.5 wording patterns rename"),
    ("### 7. \"On average\" / \"estimated\" / \"predicted\" / \"approximately\"\nThese indicate the answer is a rounded estimate, not exact. The SAT uses these to signal that the test-taker should use the model, not raw data.\n\n## Examples",
     "### 7. \"On average\" / \"estimated\" / \"predicted\" / \"approximately\"\nThese indicate the answer is a rounded estimate, not exact. The SAT uses these to signal that the test-taker should use the model, not raw data.\n\n" + S14.rstrip("\n"),
     "B3.2.5 examples rename"),
    # B3.3
    ("## Measures of Center", S15.rstrip("\n"), "B3.3.1 rename"),
    ("## Distribution Shape", S16.rstrip("\n"), "B3.3.2 rename"),
    ("## Measures of Spread", S17.rstrip("\n"), "B3.3.3 rename"),
    ("## Effect of Transformations", S18.rstrip("\n"), "B3.3.4 rename"),
    ("## Reading Displays", S19.rstrip("\n"), "B3.3.5 rename"),
    ("**Comparative box plots:** Two box plots side by side → compare their medians, IQRs, ranges.\n\n## Examples",
     "**Comparative box plots:** Two box plots side by side → compare their medians, IQRs, ranges.\n\n" + S20.rstrip("\n"),
     "B3.3.6 comparing distributions + B3.3.7 examples rename"),
    ("---\n\n# B3.4 Two-Variable Data: Scatterplots and Models",
     S21.rstrip("\n") + "\n\n---\n\n# B3.4 Two-Variable Data: Scatterplots and Models", "B3.3 new examples"),
    # B3.4
    ("# B3.4 Two-Variable Data: Scatterplots and Models\n\n## Core Concepts", S22, "B3.4 core rename"),
    ("## Choosing a Model", S23.rstrip("\n"), "B3.4.2 rename"),
    ("## Prediction: Interpolation vs Extrapolation", S24.rstrip("\n"), "B3.4.3 rename"),
    ("## Reading Graphs", S25.rstrip("\n"), "B3.4.4 rename"),
    ("- **Influential point:** A point whose removal would substantially change the slope or intercept. Not all outliers are influential — an outlier near the mean $x$ barely changes the line.",
     "- **Influential point:** A point whose removal would substantially change the slope or intercept. Not all outliers are influential — an outlier near the mean $x$ barely changes the line.\n" + S27.rstrip("\n"),
     "B3.4 core expansion"),
    ("- **Scatterplot with fitted line:** Read predicted values from the line, not from individual points. \"Based on the line of best fit\" = use the line.\n\n## Examples",
     "- **Scatterplot with fitted line:** Read predicted values from the line, not from individual points. \"Based on the line of best fit\" = use the line.\n\n" + S26.rstrip("\n"),
     "B3.4 examples rename"),
    ("---\n\n# B3.5 Probability and Conditional Probability",
     S28.rstrip("\n") + "\n\n---\n\n# B3.5 Probability and Conditional Probability", "B3.4 new examples"),
    # B3.5
    ("# B3.5 Probability and Conditional Probability\n\n## Core Concepts", S29, "B3.5 core rename"),
    ("\"None\": $P(\\text{none}) = 1 - P(\\text{at least one})$.\n\n## Examples",
     "\"None\": $P(\\text{none}) = 1 - P(\\text{at least one})$.\n" + S31.rstrip("\n") + "\n\n" + S30.rstrip("\n"),
     "B3.5 core expansion + examples rename"),
    ("---\n\n# B3.6 Inference from Sample Statistics",
     S32.rstrip("\n") + "\n\n---\n\n# B3.6 Inference from Sample Statistics", "B3.5 new examples"),
    # B3.6
    ("# B3.6 Inference from Sample Statistics\n\n## Core Concepts", S33, "B3.6 core rename"),
    ("## Confidence Intervals — What's Plausible?", S34.rstrip("\n"), "B3.6.2 rename"),
    ("## Sample Size Reasoning", S35.rstrip("\n"), "B3.6.3 rename"),
    ("## Sampling Methods", S36.rstrip("\n"), "B3.6.4 rename"),
    ("## Sources of Bias", S37.rstrip("\n"), "B3.6.5 rename"),
    ("## Wording Traps", S38.rstrip("\n"), "B3.6.6 rename"),
    ("| \"exactly 42%\" | ❌ Wrong for sample estimates |\n\n## Examples",
     "| \"exactly 42%\" | ❌ Wrong for sample estimates |\n\n" + S39.rstrip("\n"),
     "B3.6 examples rename"),
    ("- ❌ A large biased sample is still biased. Size ≠ representativeness.",
     "- ❌ A large biased sample is still biased. Size ≠ representativeness.\n" + S40.rstrip("\n"),
     "B3.6 core expansion"),
    ("---\n\n# B3.7 Evaluating Statistical Claims & Study Design",
     S41.rstrip("\n") + "\n\n---\n\n# B3.7 Evaluating Statistical Claims & Study Design", "B3.6 new examples"),
    # B3.7
    ("# B3.7 Evaluating Statistical Claims & Study Design\n\n## Core Framework", S42, "B3.7 core rename"),
    ("## Confounding Variables — Quick Recognition", S43.rstrip("\n"), "B3.7.2 rename"),
    ("## Experimental Design Terminology", S44.rstrip("\n"), "B3.7.3 rename"),
    ("- **Blocking:** Grouping subjects by a characteristic (e.g., age, gender) before random assignment — reduces variability from known confounding variables.\n\n## Examples",
     "- **Blocking:** Grouping subjects by a characteristic (e.g., age, gender) before random assignment — reduces variability from known confounding variables.\n\n" + S45.rstrip("\n"),
     "B3.7 examples rename"),
    ("**Confounding variable:** A third variable correlated with both treatment and outcome, creating spurious association.",
     "**Confounding variable:** A third variable correlated with both treatment and outcome, creating spurious association.\n" + S46.rstrip("\n"),
     "B3.7 core expansion"),
    ("---\n\n# 9. The 20 Data Analysis Traps",
     S47.rstrip("\n") + "\n\n---\n\n# 9. The 20 Data Analysis Traps", "B3.7 new examples"),
    # traps
    ("# 9. The 20 Data Analysis Traps", S48.rstrip("\n"), "traps retitle"),
    ("High values ≠ dependent or independent.\n\n---\n\n# 10. Desmos Strategies",
     "High values ≠ dependent or independent.\n\n" + S49.rstrip("\n") + "\n\n---\n\n# 10. Desmos Strategies", "two new traps"),
    # desmos
    ("- **Expected value:** `10*0.3 + 0*0.7 - 5` → net expected value with cost.",
     "- **Expected value:** `10*0.3 + 0*0.7 - 5` → net expected value with cost.\n" + S50.rstrip("\n"),
     "desmos quick calcs"),
    # mixed review
    ("❌ Study 1: \"Exercise prevents obesity\" — no causation from survey. ❌ Study 2: \"Exercise lowers BMI for all adults\" — participants were volunteers, not random sample.\n\n---\n\n---\n\n## B3 at a Glance (Final Revision Reference)",
     "❌ Study 1: \"Exercise prevents obesity\" — no causation from survey. ❌ Study 2: \"Exercise lowers BMI for all adults\" — participants were volunteers, not random sample.\n\n---\n\n" + S51.rstrip("\n") + "\n\n---\n\n---\n\n## B3 at a Glance (Final Revision Reference)",
     "mixed review 16-18"),
]

# ---------------- apply ----------------
text = orig
for i, (anchor, repl, desc) in enumerate(OPS):
    cnt = text.count(anchor)
    if cnt != 1:
        print(f"FAIL op {i} ({desc}): anchor count = {cnt} (expected 1)")
        print(f"  anchor[:80] = {anchor[:80]!r}")
        sys.exit(1)
    text = text.replace(anchor, repl)
    print(f"ok {i:2d} {desc}")

# ---------------- verification ----------------
# 1. em dash / en dash check on all inserted content
blocks = [S00, S01, S02, S03, S04, S05, S06, S07, S08, S09, S10, S11, S12, S13, S14,
          S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28,
          S29, S30, S31, S32, S33, S34, S35, S36, S37, S38, S39, S40, S41, S42,
          S43, S44, S45, S46, S47, S48, S49, S50, S51]
for b in blocks:
    if "\u2014" in b or "\u2013" in b:
        print(f"DASH FAIL in block: {b[:60]!r}")
        sys.exit(1)
print("ok em/en dash check (no em dashes in inserted content)")

# 2. every original line preserved (except intentionally renamed headers)
new_lines = text.split("\n")
# headers deliberately renamed to numbered subsections (B3.x.y numbering)
ALLOWED_RENAMES = {
    "## Core Concepts", "## Examples", "## The 7 Key Wording Patterns",
    "## Measures of Center", "## Distribution Shape", "## Measures of Spread",
    "## Effect of Transformations", "## Reading Displays",
    "## Choosing a Model", "## Prediction: Interpolation vs Extrapolation",
    "## Reading Graphs",
    "## Confidence Intervals — What's Plausible?", "## Sample Size Reasoning",
    "## Sampling Methods", "## Sources of Bias", "## Wording Traps",
    "## Core Framework", "## Confounding Variables — Quick Recognition",
    "## Experimental Design Terminology", "# 9. The 20 Data Analysis Traps",
}
missing2 = [l for l in orig_lines if l not in set(new_lines)]
real_loss = [l for l in missing2 if l not in ALLOWED_RENAMES]
if real_loss:
    print(f"LOSS FAIL: {len(real_loss)} original lines not preserved, first 5:")
    for l in real_loss[:5]:
        print(f"  {l[:100]!r}")
    sys.exit(1)
if missing2:
    print(f"ok {len(orig_lines)} original lines preserved ({len(missing2)} intentional header renames)")
else:
    print(f"ok all {len(orig_lines)} original lines preserved verbatim")

# 3. LaTeX dollar parity (total count even)
n_dollars = text.count("$")
print(f"info total '$' count = {n_dollars} (should be even: {n_dollars % 2 == 0})")
if n_dollars % 2 != 0:
    print("WARN: odd dollar count - check LaTeX balance manually")

# 4. difficulty label count
import re
labels = re.findall(r"\[(Easy|Medium|Hard|Very Hard)\]", text)
print(f"info difficulty-labeled examples: {len(labels)}")

with open(PATH, "w", encoding="utf-8") as f:
    f.write(text)

print(f"DONE: {len(orig_lines)} lines -> {len(new_lines)} lines (+{len(new_lines) - len(orig_lines)})")
