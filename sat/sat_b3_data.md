# Digital SAT Domain B3: Data Analysis

**Weight:** ~15% of SAT Math (5-7 of 44 questions)
**Calculator:** Desmos available on all questions

**Domain cross-references:** B1 (Algebra) for linear models and direct/inverse variation | B2 (Advanced Math) for exponential growth/decay models | B4 (Geometry & Trig) for geometric probability, volume ratios

## Blueprint Mapping

| College Board Skill | Weight | Section(s) |
|---|---|---|
| Ratios, rates, proportional relationships, units | 20-30% of B3 | B3.1 |
| Percentages | 15-20% of B3 | B3.2 |
| One-variable data: center, spread, shape | 15-20% of B3 | B3.3 |
| Two-variable data: scatterplots, models, residuals | 15-20% of B3 | B3.4 |
| Probability & conditional probability | 10-15% of B3 | B3.5 |
| Inference: MoE, confidence intervals, sampling | 10-15% of B3 | B3.6 |
| Evaluating claims & study design | 10-15% of B3 | B3.7 |

---

# 0. Most Common Question Types on the Actual Exam

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

# 1. Complete Formula Sheet

## Ratios, Rates & Units

| Concept | Formula |
|---------|---------|
| Proportion | $\frac{a}{b} = \frac{c}{d} \implies ad = bc$ |
| Unit rate | $\frac{\text{quantity}}{\text{one unit of }b}$ |
| Density | $\frac{\text{mass}}{\text{volume}}$ or $\frac{\text{population}}{\text{area}}$ |
| Direct/inverse variation | $y = kx$ / $y = \frac{k}{x}$ |
| Average speed | $\frac{\text{total distance}}{\text{total time}}$ (not arithmetic mean of speeds) |
| Weighted average | $\frac{\sum w_i x_i}{\sum w_i}$ |
| Scale factor property | If $x$ changes by factor $k$, a proportional $y$ changes by the same factor $k$ |
| Derived units (product) | e.g., kilowatt-hours = power (kW) × time (h) |
| Derived units (quotient) | e.g., population density = population ÷ area |

## Percentages

| Concept | Formula |
|---------|---------|
| Percent of number | $p\% \text{ of } x = \frac{p}{100} \times x$ |
| Percent change | $\frac{\text{new} - \text{old}}{\text{old}} \times 100\%$ |
| Multiplier (increase) | $1 + \frac{p}{100}$ |
| Multiplier (decrease) | $1 - \frac{p}{100}$ |
| Reverse percent | $\text{original} = \frac{\text{final}}{\text{multiplier}}$ |
| Compound growth | $A = P(1 + r)^n$ |
| Successive changes | Multiply all multipliers, never add |
| Percentage points vs % | 4% → 6% = +2 pp, +50% relative |
| Percent error | $\frac{|\text{estimated} - \text{actual}|}{\text{actual}} \times 100\%$ (divide by actual, not estimate) |
| Simple interest | $I = Prt$; total $= P(1 + rt)$ |

## One-Variable Statistics

| Concept | Formula / Rule |
|---------|---------------|
| Mean | $\bar{x} = \frac{\sum x_i}{n}$ |
| Median | Middle of sorted data (avg of two middle if even $n$) |
| Mode | Most frequent value(s); a data set can have one mode, multiple modes, or no mode |
| Range | $\max - \min$ |
| IQR | $Q_3 - Q_1$ |
| Outlier (1.5×IQR) | Below $Q_1 - 1.5\times\text{IQR}$ or above $Q_3 + 1.5\times\text{IQR}$ |
| Sum given mean | $\text{sum} = \bar{x} \times n$ |
| Adding constant $c$ to all | Mean/median $+c$; SD/IQR/range unchanged |
| Multiplying all by $c$ | Mean/median/SD/IQR/range $\times |c|$ |
| Median position (odd $n$) | $\frac{n+1}{2}$-th value of the sorted data |
| Median position (even $n$) | average of the $\frac{n}{2}$-th and $\left(\frac{n}{2}+1\right)$-th values |

## Two-Variable Data

| Concept | Formula / Rule |
|---------|---------------|
| Linear model | $y = mx + b$ |
| Residual | $\text{actual} - \text{predicted}$ (positive = above line = model underestimates) |
| Quadratic model | $y = ax^2 + bx + c$ (one turn) |
| Exponential growth | $y = a \cdot b^x$ with $b > 1$ |
| Exponential decay | $y = a \cdot b^x$ with $0 < b < 1$ |

## Probability

| Concept | Formula |
|---------|---------|
| Basic | $P(E) = \frac{\text{favorable}}{\text{total}}$ |
| Complement | $P(\text{not }A) = 1 - P(A)$ |
| Addition rule | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| Conditional | $P(A\|B) = \frac{P(A \cap B)}{P(B)}$ |
| Independence | $P(A\|B) = P(A)$ or $P(A \cap B) = P(A) \times P(B)$ |
| Mutually exclusive | $P(A \cap B) = 0$, so $P(A \cup B) = P(A) + P(B)$ |
| "At least one" | $P(\text{at least one}) = 1 - P(\text{none})$ |
| Relative frequency | $\frac{\text{category frequency}}{\text{total}}$ - an empirical probability |
| Area model | $P(\text{event}) = \frac{\text{area of favorable region}}{\text{total area}}$ |
| Reverse probability | Given $P(A|B)$ and total of $B$: cell count $= P(A|B) \times (\text{total of } B)$ |

## Inference & Study Design

| Concept | Rule |
|---------|------|
| Random selection | Generalize to population |
| Random assignment | Claim causation |
| Margin of error | Statistic $\pm$ MoE = plausible range for parameter |
| Larger sample | Smaller MoE |
| Observational study | Association only |
| Experiment | Causation possible |

---

# B3.1 Ratios, Rates, Proportional Relationships, and Units

## B3.1.1 Core Concepts: Definitions and Methods


**Unit conversion:** Write conversion factors as fractions that cancel. Square/cubic units require squaring/cubing the conversion factor.

$60 \frac{\text{mi}}{\text{h}} \times \frac{5280 \text{ ft}}{1 \text{ mi}} \times \frac{1 \text{ h}}{3600 \text{ s}} = 88 \frac{\text{ft}}{\text{s}}$

$1 \text{ ft}^2 = (12 \text{ in})^2 = 144 \text{ in}^2 \qquad 1 \text{ yd}^3 = (3 \text{ ft})^3 = 27 \text{ ft}^3$

**Part-to-part vs part-to-whole:** If boys:girls = 3:2, total parts = 5. Boys = $3/5$, girls = $2/5$ of total. Value of one part = total ÷ 5.

**Weighted average:** Use when groups have different sizes. $\frac{\sum w_i x_i}{\sum w_i}$

**Average speed:** Total distance ÷ total time. ❌ **Not** the arithmetic mean of speeds. ⚡ When distances are equal but speeds differ, average speed is the harmonic mean (less than arithmetic mean).

**Density:** $\text{mass} = \text{density} \times \text{volume}$. Works same way for population density (population = density × area). (See B4 for volume formulas and geometry reference.)


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

## B3.1.2 Worked Examples by Difficulty

### [Easy] Unit Rate
A car travels 240 miles on 8 gallons. Fuel efficiency?

$\frac{240}{8} = 30$ mpg

### [Easy] Proportion
If 3 pounds cost $5.40, how much do 7 pounds cost?

$\frac{3}{5.40} = \frac{7}{x} \implies x = 12.60$

❌ **Wrong base:** Reversing the proportion ($3/5.40 = x/7$). Keep same units in both numerators.

### [Easy] Map Scale
Map scale 1:50,000. Distance on map is 4 cm. Actual distance in km?

$4 \times 50,\!000 = 200,\!000 \text{ cm} = 2 \text{ km}$

❌ **Unit mismatch:** Reporting 200,000 without converting cm to km.

### [Medium] Square Unit Conversion
A 4 ft × 6 ft garden. Area in square inches?

$4 \times 6 = 24 \text{ ft}^2$; $24 \times 144 = 3,\!456 \text{ in}^2$

❌ **Linear conversion:** Converting 24 ft to 288 in and calling it area - 288 in is a length, not area.

### [Medium] Weighted Average
12 students scored 80, 8 scored 90. Class average?

$\frac{12 \times 80 + 8 \times 90}{20} = \frac{1680}{20} = 84$

❌ **Unweighted:** $(80+90)/2 = 85$ ignores group sizes.

### [Medium] Average Speed (Equal Distances)
100 miles at 50 mph, then 100 miles at 30 mph. Average speed?

Time: $100/50 = 2$ h, $100/30 \approx 3.33$ h. Total: $200/5.33 \approx 37.5$ mph.

❌ **Arithmetic mean:** $(50+30)/2 = 40$ mph - wrong; times differ.

### [Hard] Multi-Step Unit Conversion with Density
A prism 0.5 m × 0.3 m × 0.2 m has density 2.5 g/cm$^3$. Mass in kg?

Volume: $0.5 \times 0.3 \times 0.2 = 0.03 \text{ m}^3$  
Convert: $0.03 \times (100)^3 = 30,\!000 \text{ cm}^3$  
Mass: $30,\!000 \times 2.5 = 75,\!000 \text{ g} = 75 \text{ kg}$

❌ **Cubic conversion:** Using 100 instead of $100^3$ gives 3 cm$^3$ instead of 30,000.

### [Hard] Inverse Variation
$y$ varies inversely with $x$. When $x=4$, $y=6$. Find $y$ when $x=3$.

$k = xy = 24$, so $y = \frac{24}{3} = 8$

❌ **Direct variation:** Cross-multiplying $4/6 = 3/y$ instead of $4/6 = y/3$.

### [Easy] Direct Variation
$y$ varies directly with $x$. When $x = 3$, $y = 12$. What is $y$ when $x = 7$?

$k = \frac{y}{x} = \frac{12}{3} = 4$, so $y = 4x$ and $y = 4(7) = 28$.

❌ **Inverse setup:** $xy = 36$, giving $y = 36/7$ - direct variation uses $y = kx$, not $xy = k$.

### [Hard] Kilowatt-Hours (Derived Unit from a Product)
A 1,200-watt appliance runs 2.5 hours per day for 30 days. At $0.15 per kilowatt-hour, what is the total cost?

Power: $1200 \text{ W} = 1.2 \text{ kW}$.  
Energy: $1.2 \times 2.5 \times 30 = 90$ kWh.  
Cost: $90 \times 0.15 = \$13.50$.

❌ **Unit slip:** using 1,200 kW instead of 1.2 kW gives \$13,500 - watts must be converted to kilowatts before multiplying by hours.

### [Medium] Compound Unit Conversion - mph to ft/s
A car drives at 60 miles per hour. What is the speed in feet per second? (1 mile = 5,280 ft.)

$60 \frac{\text{mi}}{\text{h}} \times \frac{5280 \text{ ft}}{1 \text{ mi}} \times \frac{1 \text{ h}}{3600 \text{ s}} = \frac{60 \times 5280}{3600} = 88 \frac{\text{ft}}{\text{s}}$

❌ **Partial conversion:** converting miles to feet but leaving the time in hours ($316{,}800$ ft/h) - the hour must also be converted, because the target unit is per SECOND.

### [Medium] Cubic Unit Conversion
A storage shed has volume 4 yd$^3$. What is the volume in cubic feet?

$4 \times (3)^3 = 4 \times 27 = 108$ ft$^3$

❌ **Linear factor:** $4 \times 3 = 12$ ft$^3$ - the conversion factor 3 must be cubed because the unit is yd$^3$, not yd.

### [Hard] Compound Unit - Dollars per Square Foot with Conversion
Wallpaper costs \$2.25 per square foot. A wall is 8 ft by 9 ft. What is the cost in dollars per square yard, and what is the total cost for the wall?

Per yd$^2$: $2.25 \times 9 = \$20.25$ per yd$^2$ (since 1 yd$^2$ = 9 ft$^2$).  
Area: $8 \times 9 = 72$ ft$^2$; cost: $72 \times 2.25 = \$162$.

❌ **Area unit error:** converting the wall to $72/3 = 24$ yd$^2$ using the linear factor 3 - area conversions use $3^2 = 9$, so the wall is $72/9 = 8$ yd$^2$. The total cost comes out the same ($8 \times 20.25 = 162$) only if you pair each unit consistently: dollars per square yard must multiply square yards, never square feet.

---

# B3.2 Percentages

## B3.2.1 Core Concepts: Definitions and Methods


**Multiplier method:** Convert every percent change to a multiplier. Chain multipliers for successive changes. Never add percentages.

- 15% increase: $\times 1.15$. 15% decrease: $\times 0.85$.
- Two 10% increases: $1.10 \times 1.10 = 1.21$ (21% increase, **not** 20%).
- A $p\%$ increase then $p\%$ decrease always nets a loss: $1.20 \times 0.80 = 0.96$ (4% loss, **not** 0%).

**Reverse percent:** Original = final ÷ multiplier. ❌ Never multiply the discounted price by the opposite percent.

**Compound growth:** $A = P(1+r)^n$ where $r$ is rate per period as decimal, $n$ is number of periods.

**Percentage points vs %:** 4% → 6% = +2 pp, +50% relative change. Percent of percent: 30% of 40% = $0.30 \times 0.40 = 12\%$, **not** subtraction or addition.


**Universal 4-step method for any percent problem:**
1. Write the base (the "old" or "original" amount) in words - it is the denominator of any change.
2. Decide the operation: "of" = multiply; "change" = $\frac{\text{new} - \text{old}}{\text{old}}$; "more/less than" = multiply by $1 \pm p/100$.
3. Convert the percentage to a multiplier or a decimal first; never carry the % sign through the calculation.
4. Sanity check: an increase over 100% gives a multiplier above 2; a discount always gives a multiplier below 1.

**Percent error (error margin percentage) - official testing point:** $\frac{|\text{estimated} - \text{actual}|}{\text{actual}} \times 100\%$. Always divide by the actual (true) value, and use absolute value so the error is nonnegative. The SAT asks this as "percent error", "error margin", or "how far off is the estimate".

**Percentages greater than or equal to 100% (official testing point):** 100% of a number is the number itself; 150% of a number is 1.5 times it. An increase of 150% means the new value is 250% of the old (multiplier 2.5); a "200% increase" triples the value.

**Simple interest:** $I = Prt$ where $P$ is the principal, $r$ is the annual rate as a decimal, $t$ is time in years; total $= P(1 + rt)$. Compound interest (see Compound growth above) uses $A = P(1+r)^n$. The wording decides: "simple interest" says so explicitly; "compounded annually" means compound.

**Desmos tip:** chain multipliers in one line: `150 * 1.30 * 0.85` for a 30% markup followed by a 15% discount; `45 / 0.75` for reverse percent.

### Percentage Language - Exact Wording Matters

SAT uses precise wording. Each phrase changes the calculation:

| Phrase | Meaning | Example |
|--------|---------|---------|
| "increase by 15%" | multiply by 1.15 | 100 → 115 |
| "increase to 115%" | multiply by 1.15 | 100 → 115 |
| "increase by 15 percentage points" | add 15 pp | 30% → 45% |
| "15% of 200" | 0.15 × 200 | 30 |
| "15% more than 200" | 1.15 × 200 | 230 |
| "15% less than 200" | 0.85 × 200 | 170 |
| "what percent of 200 is 30" | 30/200 = 15% | 15% |
| "what percent is 30 of 200" | same | 15% |
| "30 is what percent of 200" | same | 15% |
| "30 is 15% of what number" | 30/0.15 = 200 | 200 |
| "percent change from 80 to 92" | (92-80)/80 = 15% | 15% increase |
| "percent difference" | $\frac{\|a-b\|}{(a+b)/2}$ | rarely on SAT |

| "on average" / "estimated" / "predicted" | use the model, not raw data (rounded estimate) | model prediction |
⚡ "Increase **by**" vs "increase **to**" are the same mathematically (both multiply). But "increase by 15 **percentage points**" means addition, not multiplication - common trap.

### [Medium] Wording Trap
Population increases by 150% over 10 years. Original = 20,000. Final?

$20,\!000 \times 2.50 = 50,\!000$ (increase of 150% means final = 250% of original)

❌ **Half-increase:** $20,\!000 \times 1.50 = 30,\!000$ - that's a 50% increase, not 150%.

## B3.2.2 Worked Examples by Difficulty

### [Easy] Percent Change
Price $80 → $92. Percent increase?

$\frac{92-80}{80} = \frac{12}{80} = 15\%$

❌ **Wrong base:** $12/92 \approx 13\%$ (dividing by new value).

### [Medium] Reverse Percent
After 25% off, shirt costs $45. Original price?

$45 / 0.75 = 60$

❌ **Add-back error:** $45 \times 1.25 = 56.25$ - 25% of 60 $\neq$ 25% of 45.

### [Medium] Percentage Points vs Percent
Interest rate rises from 4% to 6%. Change in percentage points vs percent change?

pp change: 6% - 4% = +2 pp. Relative change: $(6-4)/4 = 50\%$ increase.

❌ **Confusion:** Saying "increased by 2%" when it's 2 pp (relative increase is 50%).

### [Hard] Successive Percent Change
Mark up 40%, then discount 25% off marked price. Final as % of original?

$1.40 \times 0.75 = 1.05 = 105\%$

❌ **Additive:** 40% - 25% = 15% increase. Actual net is 5%.

### [Hard] Compound Growth
Population 10,000 grows 3%/year. After 4 years?

$10,\!000 \times (1.03)^4 \approx 11,\!255$

❌ **Simple growth:** $10,\!000 \times (1 + 4 \times 0.03) = 11,\!200$ - ignores compounding.

### [Very Hard] Find Annual Rate
Population 5,000 → 7,000 over 3 years. Annual growth rate?

$(1+r)^3 = 7000/5000 = 1.4$  
$1+r = \sqrt[3]{1.4} \approx 1.119$ → $r \approx 11.9\%$

❌ **Dividing total growth:** $7000/5000/3 \approx 0.133$ - ignores compounding. Actual rate is lower because compounding accelerates growth.

### [Easy] Percent Error
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

### [Hard] Simple vs Compound Interest
$1,000 is invested at 5% per year for 2 years. Compare the totals under simple interest vs interest compounded annually.

Simple: $1000(1 + 0.05 \times 2) = \$1{,}100$.  
Compound: $1000(1.05)^2 = \$1{,}102.50$.  
Compounding earns an extra $2.50 - interest on the first year's interest.

❌ **Treating them the same:** over longer periods compounding grows much faster; "compounded annually" vs "simple interest" changes the calculation.

# B3.3 One-Variable Data: Distributions and Measures

## B3.3.1 Measures of Center

- **Mean:** $\bar{x} = \frac{\sum x_i}{n}$. Pulled toward outliers and skew.
- **Median:** Middle of sorted data (avg of two middle if even $n$). Resistant to outliers.
- **Weighted mean:** $\frac{\sum f_i x_i}{\sum f_i}$ where $f_i$ = frequencies.

## B3.3.2 Distribution Shape

SAT tests shape recognition from graphs (histograms, dot plots) - not just naming shapes but understanding their implications.

| Shape | Description | Mean vs Median | Real example |
|-------|-------------|---------------|--------------|
| Symmetric | Mirrored left-right | Mean $\approx$ Median | Heights, IQ scores |
| Skewed right | Long tail to the right | Mean > Median | Income, house prices |
| Skewed left | Long tail to the left | Mean < Median | Test scores with few very low scores |
| Bimodal | Two distinct peaks | Mean may fall between peaks (misleading) | Heights of men and women combined |
| Uniform | All bars roughly equal height | Mean $\approx$ Median | Rolling a fair die many times |
| Cluster | Values concentrated in one area | Mean near cluster center | Most students score 70-80 |
| Gap | Empty interval between data | Depending on gap location | Two separate age groups |

⚡ **Bimodal rule:** When you see two peaks, the mean can be a terrible summary. A person whose height equals the mean may not represent either group.

## B3.3.3 Measures of Spread

- **Range:** max − min. Not resistant.
- **IQR:** $Q_3 - Q_1$. Resistant. Measures spread of middle 50%.
- **Standard deviation:** typical spread of values around the mean (larger SD = values tend to lie farther from the mean). Conceptual only on SAT - you compare, not compute.
  - All values identical: SD = 0
  - Values clustered near mean: small SD
  - Values spread far from mean: large SD
  - Adding same constant to all: SD unchanged
  - Multiplying all by $c$: SD × $|c|$
- **Outlier (1.5×IQR):** Below $Q_1 - 1.5 \times \text{IQR}$ or above $Q_3 + 1.5 \times \text{IQR}$.

**IQR - step-by-step (5 steps):**
1. Sort the data from smallest to largest.
2. Find the median (the middle value for odd $n$; the average of the two middle values for even $n$).
3. Split the sorted list at the median into a lower half and an upper half (for odd $n$, the median itself belongs to neither half).
4. $Q_1$ = median of the lower half; $Q_3$ = median of the upper half.
5. $\text{IQR} = Q_3 - Q_1$. The IQR is the spread of the middle 50% of the data and is not affected by extreme values.

⚡ In Desmos: `quartile(L, 3) - quartile(L, 1)` gives the IQR of a list $L$ in one step. The SAT asks you to compute IQR only from small lists or box plots, so practice the 5 steps by hand.

## B3.3.4 Effect of Transformations

| Transform | Mean | Median | SD | Range | IQR |
|-----------|------|--------|----|-------|-----|
| Add $c$ to all | $+c$ | $+c$ | Same | Same | Same |
| Multiply all by $c$ | $\times c$ | $\times c$ | $\times |c|$ | $\times |c|$ | $\times |c|$ |
| Remove an outlier | Shifts toward rest | Little change | Decreases | Decreases | Little change |
| Duplicate every value | Same | Same | Same | Same | Same |
| Double sample size | Unchanged | Unchanged | Unchanged | May increase | May increase |

## B3.3.5 Reading Displays

- **Box plot:** Shows min, $Q_1$, median, $Q_3$, max. Box = IQR (middle 50%). Whiskers extend to min/max (or 1.5×IQR fences). Compare medians for center, IQR for spread, whisker lengths for outliers.
- **Histogram:** Bar height = frequency. To find median, find bin where cumulative frequency crosses 50%. Estimate mean by assuming values at bin center. Estimate percentage above a threshold by summing bin frequencies above that value. ❌ **Bar chart vs histogram:** Bar charts = categorical data (gaps between bars). Histograms = numerical data (bars touch, no gaps).
- **Dot plot:** Each dot = one data point. Good for small datasets.
- **Stemplot:** Shows individual values while preserving order.
- **Comparative box plots:** Two box plots side by side → compare their medians, IQRs, ranges.

## B3.3.6 Comparing Distributions: Center and Spread (Official Testing Point)

The framework explicitly tests comparing distributions, including:
- **Different means, same standard deviation:** two data sets can be centered far apart (different location) yet have identical spread. Example: A = {90, 100, 110} and B = {40, 50, 60} both have SD of 10 but means of 100 and 50. The histogram of B is the histogram of A shifted left - same shape, different location.
- **Same mean, different standard deviations:** A = {95, 100, 105} and B = {50, 100, 150} both have mean 100, but B is far more spread out (larger SD).
- **Rule of thumb:** when comparing two distributions, center (mean or median) describes location; SD, IQR, and range describe spread. A comparison question is answered by naming which property changed: "the new histogram has the same spread but a smaller mean".

**Outliers (official testing point):** an outlier is a value far from the rest of the data. It pulls the mean toward it, barely moves the median, and inflates the range and SD. If a question asks which measure is "least affected" or "most resistant", the answer is the median (or mode); if it asks which is "most affected", the answer is the mean (or range).

**Method for "which set has larger SD" questions:** sketch or visualize the dot plot or histogram, locate the center, then ask: on average, how far are the values from the center? More values far from the center = larger SD. Never compare ranges alone, and never try to compute - the SAT only asks for comparison.

## B3.3.7 Worked Examples by Difficulty

### [Easy] Mean
Scores: 72, 85, 90, 65, 88. Mean? $\frac{400}{5} = 80$

### [Easy] Median
12, 7, 9, 14, 3. Median? Sorted: 3, 7, 9, 12, 14 → 9

If even n (3, 7, 9, 12): median = $(7+9)/2 = 8$. ❌ **Forgetting to sort.**

### [Easy] Box Plot - Compare Medians
Box plot A: median = 50, IQR = 20. Box plot B: median = 65, IQR = 15.

✅ Group B has higher center (median 65 > 50) and less variability (IQR 15 < 20).

❌ **Overinterpretation:** "All students in B scored higher than all in A" - medians compare centers, not individual values.

### [Medium] Mean with Frequency Table

| Score | Freq |
|-------|------|
| 70    | 3    |
| 80    | 5    |
| 90    | 2    |

Mean = $\frac{3\times70 + 5\times80 + 2\times90}{10} = \frac{790}{10} = 79$

❌ **Ignoring frequencies:** $(70+80+90)/3 = 80$.

### [Medium] Box Plot - Outlier Detection
Box plot: min=10, Q1=20, median=30, Q3=40, max=100. What does the whisker tell you?

✅ The max (100) is far beyond Q3+1.5×IQR = $40 + 1.5\times20 = 70$. 100 is marked as an outlier.

❌ **Ignoring the fence:** "The whisker goes to 100, so there are no outliers" - whiskers typically extend to the last non-outlier point.

### [Medium] Histogram - Which Interval Contains Median?

| Interval | Frequency |
|----------|-----------|
| 0-10     | 4         |
| 10-20    | 8         |
| 20-30    | 12        |
| 30-40    | 6         |

Total n = 30. Median position = 15th value. Cumulative: 4, 12, 24. The 15th falls in 20-30.

❌ **Equal groups error:** "Half the intervals are below 20-30, so median is in 20-30" - it's about cumulative frequency, not number of intervals.

### [Hard] Distribution Shape - Bimodal
A class has scores clustered around 65 and around 95, with nothing in between. Shape?

✅ Bimodal - two distinct peaks. Mean might be ~80, but no student scored near 80.

❌ **Calling it symmetric:** Symmetric means mirrored; bimodal means two separated clusters.

### [Hard] SD Interpretation - Conceptual
Two histograms with same range. A has most values near center; B is uniform across the range. Which has larger SD?

✅ B. Uniformly spread values are farther from the mean on average than values clustered at center.

❌ **Range-SD confusion:** "Same range means same SD" - range only uses extremes; SD uses every value's distance from mean.

### [Hard] Data Transformation
All values × 3, then +10. Original mean = 20, range = 8. New mean and range?

Mean: $3 \times 20 + 10 = 70$. Range: $3 \times 8 = 24$ (adding constant doesn't change range).

❌ **Range addition:** $3 \times 8 + 10 = 34$ - range is a difference, not a single value.

### [Medium] Different Means, Same SD
Histogram A is centered at 60 with most values between 55 and 65. Histogram B is centered at 30 with most values between 25 and 35. Which has the larger mean? Which has the larger SD?

A has the larger mean (60 > 30). The SDs are essentially the same - both spread about 5 units around their centers.

❌ **Conflating center and spread:** "A is higher, so it must be more spread out" - location and spread are independent properties.

### [Medium] Effect of an Outlier (Numerical)
Find the mean and median of {2, 3, 4, 5, 100}.

Mean: $\frac{114}{5} = 22.8$. Median: 4 (the middle of the sorted list).

❌ **Saying the median "also jumps":** the median stays 4 - the outlier at 100 only moved the mean.

### [Very Hard] Same Mean, Different SD
Set A = {95, 100, 105}; Set B = {50, 100, 150}. Both have mean 100. Which has the larger standard deviation?

B. In A every value is within 5 of the mean; in B the values are 50 away from the mean.

❌ **Equal means = equal spread:** the mean says nothing about the SD; spread depends on distances from the mean, not on the mean itself.

### [Very Hard] Which Measure is Least Affected by an Outlier?
In a data set, one value is replaced by a much larger value. Which measure changes the least?

The median . The mean, range, and SD all respond to the change.

❌ **"The range":** the range uses only the extremes, so replacing the maximum with a bigger maximum changes the range dramatically - it is not resistant.

---

# B3.4 Two-Variable Data: Scatterplots and Models

## B3.4.1 Core Concepts: Definitions and Methods


- **Scatterplot:** Each point = $(x, y)$. Look for direction, form, strength.
- **Correlation:** Positive ($x$↑ → $y$↑), negative ($x$↑ → $y$↓), none.
- **Correlation coefficient $r$:** $-1 \leq r \leq 1$. Closer to $\pm 1$ = stronger linear relationship.
- **Linear model:** $y = mx + b$.
  - **Slope:** Change in predicted $y$ per 1-unit increase in $x$.
  - **$y$-intercept:** Predicted $y$ when $x = 0$.
- **Residual:** Actual $-$ predicted.
  - Positive: point above line, model **underestimates**.
  - Negative: point below line, model **overestimates**.
- **Residual plot:** Random scatter around zero → linear model fits well. Curved/U-shaped pattern → linear model inappropriate. Fan shape (wider spread as $x$ increases) → variance not constant.
⚡ On test day, if a residual plot shows obvious curvature, immediately consider a quadratic model - the SAT loves this inference.
- **Influential point:** A point whose removal would substantially change the slope or intercept. Not all outliers are influential - an outlier near the mean $x$ barely changes the line.


**Correlation vs causation (flagged gap):** a scatterplot or fitted model only ever shows association. Never answer "the increase in $x$ causes the increase in $y$" unless the context describes random assignment in an experiment. The SAT plants this trap in two-variable data questions too, not only in B3.6 and B3.7.

**Compare linear and exponential growth (official testing point):**
- Linear: the same amount is added each step (constant first differences). $y = mx + b$.
- Exponential: the same factor multiplies each step (constant ratios). $y = a \cdot b^x$.
- Given a table, compute consecutive differences and ratios: constant differences → linear; constant ratios → exponential. Given a graph, a straight line → linear; a curve that steepens or flattens → exponential.
- Classic question: two quantities start at the same value, one grows by a fixed amount per year, the other by a fixed percent per year. The exponential one eventually overtakes - even a modest percent beats a fixed amount over enough time.

**Desmos tip:** enter the data as a table ($x_1$, $y_1$) and fit both `y_1 ~ m x_1 + b` and `y_1 ~ a * b^{x_1}`. The model whose $R^2$ is closer to 1 is the better fit; compare the two $R^2$ values directly.

## B3.4.2 Choosing a Model

| Pattern | Model |
|---------|-------|
| Constant rate of change | Linear |
| One max/min (one turn) | Quadratic |
| Multiplicative growth/decay | Exponential |
| Approaches a limit | Logarithmic (rare on SAT) |

Context clues: "constant rate" = linear, "doubles each year" = exponential, "reaches maximum" = quadratic. If the data shows a curve, look at the residual plot - random scatter confirms the model; curvature suggests a different model.

## B3.4.3 Prediction: Interpolation vs Extrapolation

- **Interpolation:** Predicting within the observed $x$ range. More reliable.
- **Extrapolation:** Predicting outside the observed $x$ range. Less reliable - the relationship may change outside the data range.
- SAT tests whether you recognize that a prediction is unreasonable because $x$ is outside the data range.

## B3.4.4 Reading Graphs

- **Line graph:** Slope between points = rate of change. Flat = no change.
- **Bar chart:** Check $y$-axis scale. ❌ Non-zero axes exaggerate visual differences. Always read numerical values.
- **Scatterplot with fitted line:** Read predicted values from the line, not from individual points. "Based on the line of best fit" = use the line.

## B3.4.5 Worked Examples by Difficulty

### [Easy] Interpreting Slope
$y = 2.5x + 10$ predicts test score ($y$) from hours studied ($x$). Interpret slope.

✅ Each additional hour studied predicts a 2.5-point increase.

❌ **Variable reversal:** "Each additional point predicts 2.5 more hours studied."

### [Medium] Using Model to Predict
Line of best fit $y = 0.8x + 3$. Predicted $y$ when $x = 10$?

$0.8(10) + 3 = 11$

✅ Use the **line**, not a nearby data point. If the actual point at $(10, 12)$ exists, prediction is still 11.

### [Medium] Residual Interpretation
Actual point at $x=8$ has $y=15$, model predicts $y=13$. Residual?

$15 - 13 = 2$ (positive, model underestimates)

❌ **Sign error:** $13-15 = -2$ (reversing actual and predicted). ❌ **Meaning error:** "Point below line, so residual is positive."

### [Medium] Best Model (Improvement 41)
Data: (1, 3), (2, 6), (3, 12), (4, 24). Which model fits best?
A) Linear   B) Quadratic   C) Exponential   D) Logarithmic

✅ Exponential. Each $y$ is roughly 2× the previous.

❌ **Linear pick:** "The points increase, so it's linear" - the increase accelerates (3→6→12→24), signaling multiplicative growth.

### [Hard] Interpreting $y$-intercept in Context
$y = 3t + 50$ predicts plant height (cm) $t$ days after planting.

✅ When planted ($t=0$), predicted height is 50 cm.

❌ **No-context:** "When $x=0$, $y=50$" without saying what $x$ and $y$ represent.

### [Hard] Residual Pattern
Residual plot shows a U-shaped curve. What does this mean?

✅ A linear model is inappropriate - a quadratic model would fit better.

❌ **Ignoring pattern:** "Residuals are all small, so the model is good." Shape (not just size) matters.

### [Hard] Nonlinear Model Selection
Temperature readings: rise quickly then level off. Best model?

✅ Logarithmic. The data rises quickly then levels off (growth rate falls toward zero). A quadratic with a maximum would rise and then fall, not level off.

❌ **Linear assumption:** "Temperature increases over time, so linear" - the rate of increase changes, so linear is wrong.

### [Very Hard] Prediction vs Extrapolation (Improvement 12)
Data ranges from $x=10$ to $x=50$. Best-fit line $y=2x+5$. Predict $y$ when $x=100$.

✅ The prediction is $2(100)+5 = 205$, but this is **extrapolation** - $x=100$ is far outside the data range. The linear relationship may not hold.

❌ **Blind trust:** "The math says 205, so 205 is the answer" - the SAT expects you to recognize extrapolation as less reliable.

### [Medium] Compare Linear and Exponential Growth (Table)

| Year | 0 | 1 | 2 | 3 |
|------|---|---|---|---|
| Value | 100 | 115 | 130 | 145 |

Is the growth linear or exponential?

First differences: 15, 15, 15 - constant, so linear: $y = 100 + 15t$.

❌ **"It grows, so exponential"** - growth alone is not enough; constant addition is linear, constant multiplication is exponential.

### [Hard] Exponential Model from Two Points
A quantity grows exponentially and passes through (0, 5) and (2, 20). What is its value at $x = 3$?

$y = a \cdot b^x$ with $a = 5$ (the value at $x = 0$). Then $5b^2 = 20 \implies b^2 = 4 \implies b = 2$.  
$y(3) = 5 \cdot 2^3 = 40$.

❌ **Linear interpolation:** "between 20 and 40, so 30" - exponential growth is multiplicative, so the value at $x = 3$ is $20 \times 2 = 40$, not a midpoint.

# B3.5 Probability and Conditional Probability

## B3.5.1 Core Concepts: Definitions and Methods


**Two-way tables** are the primary SAT probability tool.

| | Category X | Not X | Total |
|---|-----------|-------|-------|
| Category Y | a | b | a+b |
| Not Y | c | d | c+d |
| Total | a+c | b+d | n |

- Joint: $P(Y \cap X) = a/n$
- Marginal: $P(Y) = (a+b)/n$
- Conditional: $P(Y|X) = a/(a+c)$ - denominator is total of the condition.

**Decision tree for conditional:** "Given that" → denominator is the group after "given." "Among" → denominator is the group after "among." "Of the [group]" → denominator is that group.

| Phrase | Denominator |
|--------|-------------|
| "Given that B occurred" | Total of B |
| "Among those who failed" | Total who failed |
| "Of the students who studied" | Total who studied |
| "If it is known that..." | The known condition |

**Trigger words for conditional:** "given that," "among those who," "of the [group]," "if it is known that."

**Independence:** $P(A|B) = P(A)$ or $P(A \cap B) = P(A) \times P(B)$.

**Mutually exclusive:** $P(A \cap B) = 0$, so $P(A \cup B) = P(A) + P(B)$.

**Complement problems:**  
- "At least one": $P(\text{at least one}) = 1 - P(\text{none})$. ❌ Don't sum individual probabilities.
- "At most one": $P(\text{at most one}) = P(0) + P(1)$. Don't try to subtract.
- "Exactly one": $P(\text{exactly one of }A,B) = P(A) + P(B) - 2P(A \cap B)$.
- "None": $P(\text{none}) = 1 - P(\text{at least one})$.


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

## B3.5.2 Worked Examples by Difficulty

### [Easy] Simple Probability
Bag: 3 red, 5 blue, 2 green. P(blue)?

$\frac{5}{3+5+2} = \frac{5}{10} = \frac{1}{2}$

### [Easy] Complement - "At least one" (Improvement 17)
Roll a fair die twice. P(at least one 6)?

$P(\text{no 6}) = (5/6)^2 = 25/36$  
$P(\text{at least one 6}) = 1 - 25/36 = 11/36$

❌ **Adding:** $1/6 + 1/6 = 2/6 = 1/3$ - double-counts the (6,6) outcome.

### [Medium] Tree Diagram - Without Replacement (Improvement 14)
Bag: 3 red, 2 blue. Draw 2 without replacement. P(both red)?

$P(R_1) = 3/5$. $P(R_2|R_1) = 2/4 = 1/2$.  
$P(\text{both red}) = (3/5) \times (1/2) = 3/10$

❌ **With-replacement error:** $(3/5) \times (3/5) = 9/25$ - removal changes the probability for the second draw.

### [Medium] Two-Way Table Probability

| | Passed | Failed | Total |
|---|--------|--------|-------|
| Studied | 100 | 20 | 120 |
| Not studied | 30 | 50 | 80 |
| Total | 130 | 70 | 200 |

P(passed)? $130/200 = 0.65$

❌ **Wrong total:** Using studied total (120) instead of grand total.

### [Medium] Conditional Probability
Given a student studied, P(passed)?

$P(\text{passed}|\text{studied}) = 100/120 = 5/6 \approx 0.833$

❌ **Grand total:** $100/200 = 0.5$. ❌ **Reversed condition:** $100/130 \approx 0.769$ (that's $P(\text{studied}|\text{passed})$).

### [Hard] Independence Check
From the table above: Are passing and studying independent?

$P(\text{passed}) = 130/200 = 0.65$  
$P(\text{passed}|\text{studied}) = 100/120 \approx 0.833$

Since $0.833 \neq 0.65$, they are **dependent**.

❌ **Assuming independence** because both probabilities are high. Independence requires equality.

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

### [Very Hard] Reverse Probability Determining Frequency (Official)
A two-way table has 200 students. The probability that a randomly chosen student passed given that the student did homework is 0.8, and 80 students did homework. The probability that a student passed given that the student did not do homework is 0.3. How many students passed in total?

Passed and did homework: $0.8 \times 80 = 64$.  
Did not do homework: $200 - 80 = 120$; passed: $0.3 \times 120 = 36$.  
Total passed: $64 + 36 = 100$.

❌ **Blending the probabilities:** averaging 0.8 and 0.3, or multiplying either by 200 - each conditional probability must be applied to its own condition group size.

---

# B3.6 Inference from Sample Statistics

## B3.6.1 Core Concepts: Definitions and Methods


- **Population:** Entire group of interest. **Sample:** Subset measured.
- **Sample statistic** → estimate of **population parameter**.
- **Margin of error:** $\pm$ value indicating plausible range for the true parameter.
- **Confidence interval:** (statistic $-$ MoE, statistic $+$ MoE).
- **Random sample** → enables generalization to population.
- **Larger sample** → **smaller MoE** → more precise estimate.
- MoE applies to the **parameter**, not individuals. "Plausibly" is correct; "exactly" / "certainly" are wrong.
- **Confidence interval interpretation:** The parameter plausibly falls in this range. ❌ Not: "95% of individual values fall in this range."
- ❌ A large biased sample is still biased. Size $\neq$ representativeness.


**Method for any margin-of-error conclusion question (4 steps):**
1. Compute the interval: statistic ± MoE.
2. The interval describes the population parameter (the true proportion or true mean) - never the sample, never individuals.
3. "Plausibly", "could be", "approximately" are correct; "exactly", "certainly", "definitely" are wrong.
4. Generalization is valid only to the population the sample was randomly drawn from.

**Confidence level interpretation:** "95% confidence" describes the method, not the data: if the sampling process were repeated many times, about 95% of the resulting intervals would capture the true parameter. It does NOT mean "95% of the population falls in this range", and it does not assign a probability to any single interval.

**Sample mean and sample proportion (official testing point):** the sample mean $\bar{x}$ is the best estimate of the population mean $\mu$; the sample proportion $\hat{p}$ is the best estimate of the population proportion $p$. To estimate a total for a population of size $N$: $\hat{p} \times N$.

**Which population can results extend to? (official testing point):** results extend only to the population the sample was drawn from. A random sample of registered voters in Ohio extends to registered voters in Ohio - not to all Americans, and not to all Ohioans (some are not registered).

## B3.6.2 Confidence Intervals - What's Plausible?

Given a CI of (31, 37):
- Values **inside** the interval are plausible for the parameter.
- Values **outside** the interval are less plausible.
- The **statistic itself** (e.g., 34) is always plausible.
- No single value inside is "more likely" than another (SAT doesn't test this nuance).

## B3.6.4 Sampling Methods

| Method | Random? | When to use |
|--------|---------|-------------|
| Simple random sample (SRS) | ✅ | Every member equally likely |
| Convenience (whoever is easiest) | ❌ | Never - always biased |
| Voluntary response (call-in, online polls) | ❌ | Only strong opinions respond |

## B3.6.5 Sources of Bias

| Bias | Description | Example |
|------|-------------|---------|
| Undercoverage | Part of population has reduced chance of being sampled | Phone survey misses people without phones |
| Nonresponse | Selected individuals don't respond; their views may differ | 15% response rate on email survey |
| Voluntary response | Only those with strong opinions respond | Online poll, call-in show |
| Question wording | Leading/confusing questions skew results | "Do you support the popular policy?" |
| Interviewer bias | Interviewer's presence or characteristics influence answers | Different responses to same-gender vs different-gender interviewers |
| Timing bias | When the survey is conducted affects results | Polling support for a policy right after a related news event |
| Social desirability | Respondents give socially acceptable answers | Underreporting drug use, overreporting voting |

## B3.6.6 Wording Traps

SAT uses specific wording that changes how you interpret the result:

| Phrase | Meaning |
|--------|---------|
| "approximately 42%" | Rounded estimate |
| "about 42%" | Rounded estimate |
| "estimated 42%" | Not exact |
| "predicted to be 42%" | Based on a model |
| "on average, 42%" | Mean value |
| "typical value" | Median or mode (context dependent) |
| "plausibly between 38% and 46%" | MoE interpretation |
| "exactly 42%" | ❌ Wrong for sample estimates |

## B3.6.7 Worked Examples by Difficulty

### [Easy] Interpreting Margin of Error
Survey of 500 randomly selected adults: 42% support, MoE $\pm 4\%$. Plausible range for true proportion?

$42\% \pm 4\% = [38\%, 46\%]$

❌ **Individual error:** "Between 38-46% of surveyed adults support it" - survey already found exactly 42%. ❌ **Exactness error:** "Exactly 42% of all adults support it."

### [Easy] Best Conclusion (Improvement 38)
Survey: 62% of 500 randomly selected voters favor Candidate X, MoE $\pm 4\%$. Which is best supported?
A) Exactly 62% of all voters favor Candidate X.
B) Between 58% and 66% of all voters favor Candidate X.
C) Candidate X will definitely win.
D) Between 58% and 66% of the 500 surveyed voters favor Candidate X.

✅ B - the CI applies to the population parameter, not the sample.

❌ **A:** "Exactly" is wrong for sample estimates. ❌ **C:** MoE implies uncertainty, not certainty. ❌ **D:** The sample already gave exactly 62%.

### [Medium] Estimating Population Total
Random sample of 200 students (school has 1,500): 60 own a car. Approximate total car owners?

$60/200 = 0.30$; $0.30 \times 1500 = 450$

❌ **Proportionality error:** Setting up $60/x = 200/1500$ instead of $60/200 = x/1500$.

### [Medium] Confidence Interval - Which Values Plausible? (Improvement 18)
A study gives 95% CI for mean blood pressure: (122, 138). Which statement is correct?
A) 95% of patients have BP between 122 and 138.
B) The true mean BP is plausibly between 122 and 138.
C) There is a 95% chance the true mean is exactly 130.
D) The sample mean BP is between 122 and 138.

✅ B - CI describes plausible values for the parameter.

❌ **A:** CI is about mean, not individual values. ❌ **C:** No single value has a probability attached.

### [Medium] Which Conclusion is NOT Supported? (Improvement 39)
Study: 400 randomly selected adults, 36% exercise regularly, MoE $\pm 5\%$. Which is NOT supported?
A) The true proportion of adults who exercise regularly could be 38%.
B) The true proportion of adults who exercise regularly could be 40%.
C) The true proportion of adults who exercise regularly is exactly 36%.
D) The true proportion of adults who exercise regularly is plausibly between 31% and 41%.

✅ C - "exactly" is not supported for sample estimates.

❌ **A/B:** Both 38% and 40% fall within [31%, 41%].

### [Hard] Sample Size and MoE
Poll of 400: 54% support. To reduce MoE, the pollster should:

✅ Increase sample size.

❌ "Increase MoE" - makes estimates less precise. ❌ "Poll wider area without changing sample size" - changes the population, not precision.

### [Hard] Sampling Method Selection (Improvement 46)
A school wants to survey student opinions about lunch options. Which method best avoids bias?
A) Post a survey link on the school website.
B) Randomly select 50 students from the school roster.
C) Ask students in the cafeteria at lunch.
D) Ask the student council to distribute surveys.

✅ B - random selection from the full roster ensures every student has a chance.

❌ **A:** Voluntary response (only students who visit the website). ❌ **C:** Convenience sample (misses students not in cafeteria). ❌ **D:** Not random.

### [Hard] Bias Type (Improvement 20)
An interviewer asks: "How often do you recycle?" The majority of respondents say "always." What bias is most likely?

✅ Social desirability bias - respondents give answers they think are socially acceptable.

❌ **Nonresponse:** Everyone answered. ❌ **Undercoverage:** The question applies to all respondents.

### [Hard] Explain Why Conclusion is Invalid (Improvement 47)
A study asks 100 people at a gym about exercise habits and concludes: "Americans exercise at least 3 times per week." Why is this conclusion invalid?

✅ The sample is from a gym (not representative of all Americans), and it's a convenience sample.

❌ "Sample too small" - 100 can be adequate if representative; the problem is who was sampled, not how many.

### [Very Hard] Sampling + Assignment
Randomly select 1,000 adults, randomly assign half to fitness program, half to control. Fitness group has lower cholesterol. Valid conclusions?

✅ Generalization (random selection) + causation (random assignment). This is the gold standard.

### [Very Hard] Which Population Can the Results Extend To?
A study randomly samples 500 registered voters in Ohio and finds 52% approve of a policy, MoE ±4%. To which population can the result be generalized?

Registered voters in Ohio - the population from which the sample was drawn.

❌ **"All Americans"** - the sampling frame was Ohio registered voters. ❌ **"All Ohioans"** - unregistered residents were not in the sampling frame.

---

# B3.7 Evaluating Statistical Claims & Study Design

## B3.7.1 Core Framework: Observational Studies vs Experiments


| Study type | Key feature | Can claim |
|-----------|-------------|-----------|
| Observational study | No intervention; measures naturally occurring groups | Association only |
| Experiment (random assignment) | Subjects randomly assigned | Causation |
| Random sampling | Sample drawn randomly from population | Generalize to population |
| Convenience sample | Easy-to-reach subjects | Cannot generalize |

**Random sample vs Random assignment - The Critical Distinction**

| | Random Sample | Random Assignment |
|---|---|---|
| What it means | Everyone in population has equal chance of being selected | Subjects are randomly put into treatment or control groups |
| What it enables | Generalization to the population | Causal conclusions |
| Example | Randomly calling phone numbers | Flipping a coin to assign drug/placebo |
| SAT key | Mention of "randomly selected" → can generalize | Mention of "randomly assigned" → can infer causation |

⚡ Quick-check: If the researcher **assigns** what people do, causation is on the table. If the researcher only **observes** what people already do, only association can be claimed.

**Confounding variable:** A third variable correlated with both treatment and outcome, creating spurious association.


**Method for any study-design question (4-step checklist):**
1. Was there random selection from a population? → yes = can generalize (to that population only).
2. Was there random assignment to treatment/control? → yes = can claim causation.
3. Both? → gold standard: generalize AND causation (within the studied population).
4. Neither? → association only; name the confounding variable that offers an alternative explanation.

**Correlation vs causation (flagged gap):** a correlation (or association) does NOT imply causation without random assignment. Every answer choice that says "causes" must be backed by an experiment; every observational study supports only "is associated with".

**The confounding-variable test:** a variable is confounding only if it plausibly affects BOTH the treatment choice AND the outcome. If it affects only one of them, it is not confounding.

## B3.7.2 Confounding Variables - Quick Recognition

A confounder is always related to BOTH the treatment choice AND the outcome. If a variable is only related to one, it's not confounding.

| Scenario | Treatment | Outcome | Confounder |
|----------|-----------|---------|------------|
| Coffee drinkers live longer | Coffee | Longevity | Health-conscious lifestyle |
| Private school students score higher | Private school | Test scores | Family income / resources |
| More firefighters → more damage | Firefighters | Property damage | Fire size (more firefighters for bigger fires) |
| Ice cream sales → drownings | Ice cream | Drownings | Temperature (hot → more ice cream AND more swimming) |

## B3.7.3 Experimental Design Terminology

- **Control group:** Group receiving no treatment (or placebo) - provides a baseline for comparison.
- **Placebo:** A fake treatment with no active effect - controls for the psychological effect of receiving treatment.
- **Placebo effect:** Improvement caused by belief in treatment, not the treatment itself.
- **Blinding:** Subjects don't know which group they're in (single-blind). Both subjects and researchers don't know (double-blind) - prevents bias in reporting and assessment.
- **Blocking:** Grouping subjects by a characteristic (e.g., age, gender) before random assignment - reduces variability from known confounding variables.

## B3.7.4 Worked Examples by Difficulty

### [Easy] Generalization
Survey randomly selects 500 Texas high school students: 60% prefer online learning. Generalize to?

✅ High school students in Texas (the population sampled).

❌ "All US high school students" - sample was only from Texas. ❌ "All students" - includes middle/college not sampled.

### [Easy] Causation vs Association
People who exercise more have lower blood pressure. Can we conclude exercise causes lower BP?

✅ Not from an observational study. Confounders (diet, genetics, income) may explain the association. Correct claim: "There is an association."

### [Easy] Random Sample vs Random Assignment (Improvement 23)
A study randomly selects 500 adults and asks about sleep and GPA. Can it claim sleep affects GPA?

✅ Association only - random selection allows generalization but not causation (no random assignment).

❌ "Randomly selected means we can prove causation" - random selection $\neq$ random assignment.

### [Medium] Experiment - Drug Trial (Improvement 21)
200 patients randomly assigned to new drug or placebo. Double-blind. Drug group improves more. Conclusions?

✅ The drug causes improvement (random assignment + double-blind controls for placebo effect and bias).

❌ "The drug is safe" - the study only measured efficacy, not safety. ❌ "The drug works for everyone" - the study's scope is the tested population.

### [Medium] Confounding Variable
Students who take SAT prep courses score higher. Critic argues those students are already more motivated. What is this?

✅ A confounding variable (motivation) that could explain the association without prep courses causing higher scores.

### [Very Hard] Matching Design to Conclusion
Study 1: Survey 5,000 randomly selected adults. Finds 7-8 hr sleepers score higher on memory tests.

Study 2: Randomly assign 200 adults to 6 or 8 hrs sleep for a week. 8-hr group scores higher.

Which conclusions are supported?

✅ Study 1: Association in the population (random selection), not causation. ✅ Study 2: Sleep duration causes memory difference (random assignment). Generalization limited (200 volunteers, not random sample).

### [Hard] Generalization vs Causation Together
200 volunteers are randomly assigned to a new diet or a control diet. The diet group loses more weight. What can be concluded?

The diet causes greater weight loss for these participants (random assignment). Generalization to all adults is limited because participants were volunteers, not a random sample.

❌ **"Nothing can be concluded"** - random assignment does justify the causal claim; only the generalization is limited.

---

# 9. The 13 Data Analysis Traps

### Trap 1: Wrong Denominator in Conditional Probability
In $P(A|B)$, denominator is total of $B$, not grand total. ✅ "Given that," "among," "of those who" = conditional.

### Trap 2: Adding Successive Percentages
10% increase then 10% decrease is **not** 0%. Multiply multipliers: $1.10 \times 0.90 = 0.99$ (1% loss).

### Trap 3: Missing Unit Conversion
Correct arithmetic, wrong units. Convert everything before calculating. Square/cube the conversion factor for area/volume.

### Trap 4: Using Data Points Instead of the Line
"Based on the line of best fit" → use the line, not individual points.

### Trap 5: Confusing Mean and Median
Mean pulled by outliers. Median is resistant. Right-skewed: mean > median. Left-skewed: mean < median.

### Trap 6: Claiming Causation from Observation
Correlation $\neq$ causation. Without random assignment, association only.

### Trap 7: Overgeneralizing Beyond the Sampled Population
Sample from Texas → can't generalize to all US. Population = the group actually sampled.

### Trap 8: Treating a Sample Statistic as Exact
MoE exists because samples are estimates. "Exactly" is wrong; "plausibly" / "approximately" is correct.

### Trap 10: Confusing Percentage Points with Percent Change
4% → 6% = +2 pp, +50% relative. Different quantities.

### Trap 11: Percent Change on Wrong Base
25% discount then 20% off: the 20% applies to the already-discounted price. Reverse percent = divide by multiplier, not multiply.

### Trap 14: Forgetting the Complement in "At Least One"
$P(\text{at least one}) = 1 - P(\text{none})$. Compute complement, don't sum individual probabilities.

### Trap 17: Extrapolation Blindness
Predicting outside the data range using the same model. The relationship may change. "Based on the data" vs "outside the range" - recognize when a prediction is extrapolation.

### Trap 19: Confusing the Residual Sign
Residual = actual − predicted. Positive = above line = model underestimates. Negative = below line = model overestimates. ✅ Remember: "Actual minus predicted" or "A − P."

# 10. Desmos Strategies

## Regression (The Key Technique)

Use the **tilde operator** (`~`) for regression.

1. Click `+` → Table. Enter $x$ in $x_1$, $y$ in $y_1$.
2. Type formula with `~` instead of `=`.

| Model | Syntax |
|-------|--------|
| Linear | `y_1 ~ mx_1 + b` |
| Quadratic | `y_1 ~ ax_1^2 + bx_1 + c` |
| Exponential | `y_1 ~ a * b^x_1` |

Read $m$, $b$ from the parameters panel. $R^2$ closer to 1 = better fit.

**Example:** Points (1,3), (2,5), (3,8), (4,11). `y_1 ~ mx_1 + b` → $m \approx 2.7$, $b \approx 0.5$. Equation: $y = 2.7x + 0.5$.

## Knowing When Linear is Inappropriate

After fitting a linear model, check:
- **Residual pattern:** Plot residuals by computing `r_1 = y_1 - (mx_1 + b)` in a new column. If `r_1` shows a curve or fan pattern, linear is inappropriate.
- **Visual check:** If the data clearly curves, try quadratic or exponential.

## Residual Workflow (Improvement 32)

1. Enter $x$ data in $x_1$, $y$ data in $y_1$.
2. Fit linear model: `y_1 ~ mx_1 + b`.
3. Add column $y_2 = y_1$ (copy $y$ values).
4. In $y_2$ column header, type `= y_1 - (mx_1 + b)` to compute residuals.
5. Plot $(x_1, y_2)$ - this is the residual plot.
6. **Random scatter** → linear model is good. **U-shape/fan** → try a different model.
7. Try quadratic: `y_1 ~ ax_1^2 + bx_1 + c`. Compare $R^2$ values.

⚡ The SAT often gives you a residual plot and asks: "Is a linear model appropriate?" If you see curvature, the answer is NO.

## Table Shortcuts (Improvement 33)

- **Enter lists directly:** `x_1 = [1, 2, 3, 4, 5]` creates a column.
- **Statistics on lists:** `mean(x_1)`, `median(x_1)`, `stdev(x_1)`, `min(x_1)`, `max(x_1)`, `quartile(x_1, 1)` for Q1.
- **Sort a list:** `sort(x_1)` returns sorted values.
- **Frequency table shortcut:** If data has frequencies, enter values in $x_1$, frequencies in $y_1$, then compute weighted mean as `total(x_1 * y_1) / total(y_1)`.
- **Edit a table:** Click any cell to edit. Add rows by pressing Tab in the last cell.

## Quick Calculations

- **Percentages:** Chain multipliers directly: `150 * 1.30 * 0.85` for 30% markup then 15% discount.
- **Statistics:** `L = [12, 7, 9, 14, 3]` → `mean(L)`, `median(L)`, `stdev(L)`.
- **Unit conversion:** Type directly: `60 * 5280 / 3600`.
- **Probability fractions:** `100/120` → Desmos returns $5/6$ in fraction form.
- **Reverse percent:** `45 / 0.75` → 60 (original price before 25% off).
- **Percent error:** `abs(45 - 50) / 50` → 0.10 (multiply by 100 for %).
- **Reverse probability cell:** if $P(A|B) = 0.8$ and the B total is 120, compute `0.8 * 120` → 96 (the missing cell).
- **Compare linear vs exponential fits:** fit both `y_1 ~ m x_1 + b` and `y_1 ~ a * b^{x_1}`, then compare the two $R^2$ values.
- **Missing value from a mean:** `5 * 12 - (8 + 10 + 14 + 16)` → 12 (the unknown fifth value).

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Using `=` instead of `~` in regression | Use `~` (tilde) - Shift + backtick |
| Typing regression before creating table | Create table first |
| Stopping at parameters | After regression, plug in target $x$ to predict $y$ |
| Ignoring the residual pattern | Curved or fan-shaped residuals → try a different model type |
| Forgetting $x$ range context | Predictions outside data range may be meaningless |
| Not computing residuals | Residual plot reveals whether linear model is appropriate |
| Ignoring the residual plot shape | Random = good; curved = bad |

---

## B3 at a Glance (Final Revision Reference)

### Formulas by Priority

| Priority | What |
|----------|------|
| `[CORE]` | Mean, median, mode, range, IQR, percent change, probability, proportion, unit conversion |
| `[MEMORIZE]` | SD interpretation (no calc), outlier rule, weighted average, conditional probability, margin of error, compound growth, sampling vs bias types |
| `[SUPPLEMENTARY]` | Direct/inverse variation, geometric probability, experimental design classification |

### Key Triggers

| See | Do |
|---|---|
| "Random sample" | Generalize to population (but no causation) |
| "Random assignment" | Causation claim allowed (but limited generalization) |
| Margin of error | CI = estimate ± MoE |
| "Predicted by model" | It's an estimate, not actual |
| Residual plot curvature | Linear model inappropriate |
| Percent change | (new − old) / old |
| Sequential discounts | Multiply multipliers, never add |
| Standard deviation comparison | More spread → larger SD |
| "Representative sample" | Check if truly random or stratified |
| Outlier | Check 1.5×IQR rule |

### Traps Quick-Check
- ✅ Percent change: divide by old, not new? Weighted average, not arithmetic? Residual = actual − predicted? Conditional probability denominator correct? Margin of error applied symmetrically? Study design: random sample vs random assignment? Mode checked when multiple values tie?

*End of Domain B3 Reference: Data Analysis*
