# Digital SAT Domain B3: Data Analysis

**Weight:** ~15% of SAT Math (5-7 of 44 questions)
**Calculator:** Desmos available on all questions

**Domain cross-references:** B1 (Algebra) for linear models and direct/inverse variation | B2 (Advanced Math) for exponential growth/decay models | B4 (Geometry & Trig) for geometric probability, volume ratios

## Blueprint Mapping

| College Board Skill | Weight | Section(s) |
|---|---|---|
| Ratios, rates, proportional relationships, units | 20-30% of B3 | B3.1 |
| Percentages | 15-20% of B3 | B3.2, B3.2.5 |
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
| Expected value | $E(X) = \sum x_i \cdot P(x_i)$ |
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

### [Medium] Currency Exchange
1 USD = 0.85 EUR. 1 EUR = 130 JPY. How many JPY for 50 USD?

$50 \times 0.85 = 42.5 \text{ EUR}$; $42.5 \times 130 = 5,\!525 \text{ JPY}$

❌ **Wrong direction:** Dividing by exchange rate when multiplication is correct.

### [Medium] Scale Drawing
Blueprint: 1 in = 3 ft. Room measures 4.5 in on blueprint. Actual area in ft$^2$ if width on blueprint is 3 in?

Length: $4.5 \times 3 = 13.5 \text{ ft}$; Width: $3 \times 3 = 9 \text{ ft}$. Area: $13.5 \times 9 = 121.5 \text{ ft}^2$

❌ **Linear scale applied to area:** $4.5 \times 3 \times 3 = 40.5$ - each dimension scales separately, so the linear scale is used once per dimension, not once total.

### [Medium] Recipe Proportion
Recipe for 4 servings: 2 cups flour. How much flour for 7 servings?

$\frac{2}{4} = \frac{x}{7} \implies x = 3.5 \text{ cups}$

❌ **Additive:** Adding 3 servings worth: $2 + 3 \times 0.5 = 3.5$ works here but only by coincidence. Always use proportion.

### [Medium] Square Unit Conversion
A 4 ft × 6 ft garden. Area in square inches?

$4 \times 6 = 24 \text{ ft}^2$; $24 \times 144 = 3,\!456 \text{ in}^2$

❌ **Linear conversion:** Converting 24 ft to 288 in and calling it area - 288 in is a length, not area.

### [Medium] Density
A block has mass 2,340 g and volume 260 cm$^3$. Density?

$\frac{2340}{260} = 9$ g/cm$^3$

### [Medium] Weighted Average
12 students scored 80, 8 scored 90. Class average?

$\frac{12 \times 80 + 8 \times 90}{20} = \frac{1680}{20} = 84$

❌ **Unweighted:** $(80+90)/2 = 85$ ignores group sizes.

### [Medium] Average Speed (Equal Distances)
100 miles at 50 mph, then 100 miles at 30 mph. Average speed?

Time: $100/50 = 2$ h, $100/30 \approx 3.33$ h. Total: $200/5.33 \approx 37.5$ mph.

❌ **Arithmetic mean:** $(50+30)/2 = 40$ mph - wrong; times differ.

### [Medium] Dimensional Analysis - Speed
A car goes 60 mph for 45 minutes. Distance in miles?

Time in hours: $45/60 = 0.75$ h. Distance: $60 \times 0.75 = 45$ mi

❌ **Unit mismatch:** $60 \times 45 = 2,\!700$ - mph times minutes gives nonsense units.

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

### [Hard] Dimensional Analysis - Pressure
Force 500 N applied to area 0.02 m$^2$. Pressure in N/m$^2$?

$P = F/A = 500/0.02 = 25,\!000 \text{ N/m}^2$

❌ **Unit error:** $500/0.02 = 10$ if treating area as 2 instead of 0.02.

### [Very Hard] Weighted Average with Unknown Group Size
Class A avg = 85 ($n=24$), Class B avg = 70. Combined avg = 78. How many in Class B?

$\frac{24 \times 85 + x \times 70}{24 + x} = 78$  
$2040 + 70x = 1872 + 78x$  
$x = 21$

❌ **Simple average:** Assuming combined avg = $(85+70)/2 = 77.5$. Actual combined avg tilts toward the larger group.

### [Very Hard] Average Speed (Different Distances)
30 miles at 15 mph then 20 miles at 10 mph. Average speed?

Time: $30/15 = 2$ h, $20/10 = 2$ h. Total: $50/4 = 12.5$ mph.

⚡ Here the two segments happen to take equal time, so the answer equals the arithmetic mean $(15+10)/2 = 12.5$ - but always compute total distance / total time. Don't rely on the shortcut.

### [Easy] Direct Variation
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

### [Easy] Dollars per Square Foot (Compound Unit)
Carpet costs \$3.50 per square foot. A room is 12 ft by 10 ft. How much does carpet for the room cost?

Area: $12 \times 10 = 120$ ft$^2$.  
Cost: $120 \times 3.50 = \$420$.

❌ **Rate applied to a length:** $3.50 \times 12 = 42$ treats the price as per-foot. The unit is per SQUARE foot, so it multiplies an area (ft$^2$), never a length (ft).

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

⚡ "Increase **by**" vs "increase **to**" are the same mathematically (both multiply). But "increase by 15 **percentage points**" means addition, not multiplication - common trap.

## B3.2.2 Worked Examples by Difficulty

### [Easy] Percent of Number
15% of 200? $0.15 \times 200 = 30$

### [Easy] Percent Change
Price $80 → $92. Percent increase?

$\frac{92-80}{80} = \frac{12}{80} = 15\%$

❌ **Wrong base:** $12/92 \approx 13\%$ (dividing by new value).

### [Easy] Percent Language - "increase to"
A value increases to 115% of original. Original = 200. New value?

$200 \times 1.15 = 230$

❌ **Addition:** 200 + 115 = 315. "Increases to 115%" means the new value is 115% of old.

### [Medium] Reverse Percent
After 25% off, shirt costs $45. Original price?

$45 / 0.75 = 60$

❌ **Add-back error:** $45 \times 1.25 = 56.25$ - 25% of 60 $\neq$ 25% of 45.

### [Medium] Percent of Percent
40% of items are red. Of those, 30% have stripes. % of all items that are red with stripes?

$0.40 \times 0.30 = 0.12 = 12\%$

❌ **Addition:** 40% + 30% = 70%. ❌ **Wrong ratio:** $30/40 = 75\%$ (finding what % of red items have stripes, not % of all items).

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

### [Hard] Reverse Percent with Two Steps
After 20% off then 10% off discounted price, laptop costs $720. Original?

Combined multiplier: $0.80 \times 0.90 = 0.72$. Original: $720 / 0.72 = \$1,\!000$

❌ **Sequential add-back:** $720 \times 1.20 = 864$, then $864 \times 1.10 = 950.40$ - discounts apply to different bases when going forward.

### [Hard] Reverse Percent - Tax
Price including 8% tax is $54. Pre-tax price?

$54 / 1.08 = 50$

❌ **Wrong operation:** $54 \times 0.92 = 49.68$ - 8% of 54 $\neq$ 8% of pre-tax price.

### [Very Hard] Mixed Successive Rates
Stock up 10%, up 20%, down 15%. Net percent change?

$1.10 \times 1.20 \times 0.85 = 1.122$ → 12.2% increase

❌ **Additive:** 10% + 20% - 15% = 15%. Actual net is 12.2%.

### [Very Hard] Find Annual Rate
Population 5,000 → 7,000 over 3 years. Annual growth rate?

$(1+r)^3 = 7000/5000 = 1.4$  
$1+r = \sqrt[3]{1.4} \approx 1.119$ → $r \approx 11.9\%$

❌ **Dividing total growth:** $7000/5000/3 \approx 0.133$ - ignores compounding. Actual rate is lower because compounding accelerates growth.

### [Very Hard] Reverse Percent - Profit and Loss
A store sells an item for $207, making a 15% profit on cost. Cost?

Selling price = cost × 1.15. Cost = $207 / 1.15 = 180

❌ **Wrong base:** $207 \times 0.15 = 31.05$, $207 - 31.05 = 175.95$ - profit is 15% of cost, not 15% of selling price.

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

---

# B3.2.5 Percentage Language - Precision on the SAT

The SAT tests whether you understand what each percent phrase actually means. The same numbers can produce different answers depending on wording.

## B3.2.5.1 The 7 Key Wording Patterns

### 1. "X% of" - Direct percentage of a quantity
$p\% \text{ of } N = \frac{p}{100} \times N$

15% of 200 = 30. 30 is 15% of 200.

### 2. "X% more than" / "X% less than" - Multiplier change
"15% more than 200" = $200 \times 1.15 = 230$  
"15% less than 200" = $200 \times 0.85 = 170$

❌ **Addition error:** 200 + 15 = 215. Percent more means multiply, not add.

### 3. "Increase by X%" vs "increase to X% of original"
Both mean the same: multiply by $(1 + p/100)$.  
"Increase by 15%" → multiply by 1.15.  
"Increase to 115% of original" → also multiply by 1.15.

❌ **Interpretation error:** "Increase to 115%" does NOT mean +115% (which would be ×2.15).

### 4. "Increase by X percentage points" - NOT the same
Rate goes from 4% to 6%.  
"Increase by 2 percentage points" = 4% + 2pp = 6%.  
Percent change = $(6-4)/4 = 50\%$.

❌ **Mixing concepts:** "Increased by 2%" could mean +2 pp or +2% relative. The SAT uses "percentage points" for the additive version.

### 5. "What percent of A is B?" / "B is what percent of A?"
Formula: $B/A \times 100\%$.  
"What percent of 200 is 30?" → $30/200 = 15\%$.  
"30 is what percent of 200?" → same: $30/200 = 15\%$.

### 6. "Percent change" vs "percent of"
Percent change: $(new - old)/old \times 100\%$.  
Percent of: $part/whole \times 100\%$.  
Different formulas, different questions.

### 7. "On average" / "estimated" / "predicted" / "approximately"
These indicate the answer is a rounded estimate, not exact. The SAT uses these to signal that the test-taker should use the model, not raw data.

## B3.2.5.2 Worked Examples by Difficulty

### [Easy] Wording Distinction
A store advertises "Pay 30% less than the original price of $50." How much do you pay?

$50 \times 0.70 = 35$

❌ **Wrong direction:** $50 \times 1.30 = 65$ - "less than" means decrease, not increase.

### [Medium] Wording Trap
Population increases by 150% over 10 years. Original = 20,000. Final?

$20,\!000 \times 2.50 = 50,\!000$ (increase of 150% means final = 250% of original)

❌ **Half-increase:** $20,\!000 \times 1.50 = 30,\!000$ - that's a 50% increase, not 150%.

### [Hard] Triple Wording
Company profits: Year 1 = $2M. Year 2 = 40% more than Year 1. Year 3 = 25% less than Year 2. Year 3 profit?

Year 2: $2 \times 1.40 = 2.8$ M  
Year 3: $2.8 \times 0.75 = 2.1$ M

❌ **Chain without multipliers:** $2 \times (1 + 0.40 - 0.25) = 2.3$ M.

---

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
- **Standard deviation:** Average distance from mean. Conceptual only on SAT - you compare, not compute.
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

✅ The max (100) is far beyond Q3+1.5×IQR = $40 + 1.5\times20 = 70$. The whisker likely stops at 70, and 100 is marked as an outlier.

❌ **Ignoring the fence:** "The whisker goes to 100, so there are no outliers" - whiskers typically extend to the last non-outlier point.

### [Medium] Outlier Effect
Mean = 50, median = 48. Add value 200.

✅ Mean increases significantly; median changes little or not at all.

❌ **Mean-median confusion:** Saying both increase equally.

### [Medium] SD Comparison (No Numbers)
Set A: [10, 10, 10, 10, 10]. Set B: [0, 5, 10, 15, 20]. Which has larger SD?

✅ Set B. All values in A equal the mean (SD = 0).

❌ **Range-SD confusion:** "Set A has range 0, set B has range 20" - a set can have large range but small SD if most values cluster near the mean.

### [Medium] IQR and Outlier Detection
5, 7, 8, 9, 10, 12, 15, 22. Is 22 an outlier?

$Q_1 = (7+8)/2 = 7.5$, $Q_3 = (12+15)/2 = 13.5$, IQR = 6  
Upper fence: $13.5 + 1.5 \times 6 = 22.5$

Since 22 < 22.5, it's **not** an outlier.

❌ **Intuition only:** "22 seems far so it must be an outlier." The 1.5×IQR rule provides a specific criterion.

### [Medium] Histogram - Which Interval Contains Median?

| Interval | Frequency |
|----------|-----------|
| 0-10     | 4         |
| 10-20    | 8         |
| 20-30    | 12        |
| 30-40    | 6         |

Total n = 30. Median position = 15th value. Cumulative: 4, 12, 24. The 15th falls in 20-30.

❌ **Equal groups error:** "Half the intervals are below 20-30, so median is in 20-30" - it's about cumulative frequency, not number of intervals.

### [Medium] Histogram - Estimate Percentage Above Threshold

| Score Range | Students |
|-------------|----------|
| 50-60       | 5        |
| 60-70       | 10       |
| 70-80       | 20       |
| 80-90       | 12       |
| 90-100      | 3        |

What percentage scored 80 or above? $(12+3)/50 = 15/50 = 30\%$

❌ **Counting only one bin:** "12 students scored 80-90, so 24%" - includes only 80-90 bin, misses 90-100.

### [Hard] Distribution Shape - Bimodal
A class has scores clustered around 65 and around 95, with nothing in between. Shape?

✅ Bimodal - two distinct peaks. Mean might be ~80, but no student scored near 80.

❌ **Calling it symmetric:** Symmetric means mirrored; bimodal means two separated clusters.

### [Hard] SD Interpretation - Conceptual
Two histograms with same range. A has most values near center; B is uniform across the range. Which has larger SD?

✅ B. Uniformly spread values are farther from the mean on average than values clustered at center.

❌ **Range-SD confusion:** "Same range means same SD" - range only uses extremes; SD uses every value's distance from mean.

### [Hard] Effect of Removing a Value
Mean of 10 numbers = 20. Remove 5. New mean?

Sum = 200. New sum = 195. New mean = $195/9 = 21.67$

❌ **Intuition error:** Guessing mean stays at 20 or changes to 22.5.

### [Hard] Data Transformation
All values × 3, then +10. Original mean = 20, range = 8. New mean and range?

Mean: $3 \times 20 + 10 = 70$. Range: $3 \times 8 = 24$ (adding constant doesn't change range).

❌ **Range addition:** $3 \times 8 + 10 = 34$ - range is a difference, not a single value.

### [Hard] Duplicate Every Observation
Dataset: [4, 8, 12]. Duplicate each value: [4, 4, 8, 8, 12, 12]. How do mean and SD change?

✅ Mean unchanged (still 8). SD unchanged (same relative spread).

❌ **Double-count intuition:** "More data means less spread" - duplicating doesn't change the distribution.

### [Very Hard] SD Comparison from Dot Plots
Symmetric distributions. A has values at 10(1), 11(2), 12(3), 13(4), 14(3), 15(2), 16(1). B has 10(2), 11(2), 12(3), 13(4), 14(3), 15(2), 16(2). Which has larger SD?

✅ B has more mass at extremes (10, 16) and less near center (12, 14) relative to A.

❌ **Visual misjudgment:** All symmetric distributions do not have the same SD. Spread depends on concentration around center.

### [Easy] Missing Value from the Mean
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

### [Easy] Interpret Slope in Context (Medicine)
A drug trial: $y = -3x + 120$ predicts blood pressure (mmHg) $x$ hours after dose.

✅ Each hour after dose, predicted blood pressure drops by 3 mmHg.

❌ **Reversal:** "Blood pressure decreases by 3 mmHg per hour before the dose."

### [Medium] Using Model to Predict
Line of best fit $y = 0.8x + 3$. Predicted $y$ when $x = 10$?

$0.8(10) + 3 = 11$

✅ Use the **line**, not a nearby data point. If the actual point at $(10, 12)$ exists, prediction is still 11.

### [Medium] Residual Interpretation
Actual point at $x=8$ has $y=15$, model predicts $y=13$. Residual?

$15 - 13 = 2$ (positive, model underestimates)

❌ **Sign error:** $13-15 = -2$ (reversing actual and predicted). ❌ **Meaning error:** "Point below line, so residual is positive."

### [Medium] Non-Zero Axis Bar Chart
$y$-axis starts at 90. Year 1 bar = 100, Year 2 bar = 110. Percent increase?

$(110-100)/100 = 10\%$

❌ **Scale illusion:** "The bar doubled in height so profit doubled." Visual difference is exaggerated. Read the values.

### [Medium] Estimate from Graph (Improvement 37)
Scatterplot: points roughly linear. At $x=5$, the line of best fit passes through $y\approx 17$. Best estimate for $y$ when $x=5$?

✅ 17 (read from the fitted line).

❌ **Using nearest point:** "The closest point to $x=5$ has $y=15$, so the answer is 15" - use the line, not individual points.

### [Medium] Best Estimate (Improvement 42)
A scatterplot shows a roughly linear relationship. Which is the best estimate for the $y$-intercept?
A) 2   B) 5   C) 8   D) 12

✅ Look at where the line of best fit crosses $x=0$. Estimate visually.

❌ **Guessing without reading:** Picking the smallest value just because the line looks low.

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

### [Hard] Compare Residual Plots (Improvement 10)
Residual plot A: random scatter. Residual plot B: U-shaped curve. Which model is appropriate?

✅ Model A (random residuals = linear fit is appropriate).

❌ **Equal treatment:** "Both have small residuals so both are good" - shape matters more than magnitude.

### [Hard] Correlation Coefficient
Points tightly clustered around a downward-sloping line. Most likely $r$?

✅ $r \approx -0.92$ (strong negative)

❌ **Sign error:** Choosing 0.92 when slope is negative. ❌ **Weak correlation:** Choosing $-0.15$ - points are too tightly clustered.

### [Hard] Nonlinear Model Selection
Temperature readings: rise quickly then level off. Best model?

✅ Logarithmic or quadratic with a maximum. The data is not linear (rate decreases).

❌ **Linear assumption:** "Temperature increases over time, so linear" - the rate of increase changes, so linear is wrong.

### [Hard] Interpret Parameter (Improvement 44)
$C = 0.25m + 10$ predicts cab fare ($C$) for $m$ miles. Interpret 0.25 and 10.

✅ 0.25 = $0.25 per mile (slope). 10 = $10 initial fare (y-intercept).

❌ **Swapped:** "10 is cost per mile, 0.25 is the base fare" - slope is per-unit, intercept is base.

### [Hard] Influential Point (Improvement 13)
Scatterplot: most points cluster near (5, 10) with one point at (20, 40). Removing which point changes the line most?

✅ (20, 40) - it's far from the center of the x-values, so it pulls the line.

❌ **Outlier-only focus:** Removing an outlier at (6, 2) near the mean x barely changes the line - an outlier far from the x-center is influential.

### [Very Hard] Model Selection
Population 50,000 in 2010. Each year $\approx$ 1.5$\times$ previous. Which model?

✅ Exponential ($y = a \cdot b^x$ with $b > 1$)

❌ **Linear:** "It increases each year" - the multiplier (1.5×) signals multiplicative, not additive growth.

### [Very Hard] Exponential Model Parameters
$P = 500(1.08)^t$ predicts bacteria population $t$ hours after start.

✅ Initial: 500. Growth factor: 1.08 (8% increase per hour).

❌ **Decay confusion:** "Grows by 1.08 per hour" - 1.08 is a multiplier, not an additive amount. ❌ **Coefficient confusion:** "500 is the population after 1 hour."

### [Very Hard] Prediction vs Extrapolation (Improvement 12)
Data ranges from $x=10$ to $x=50$. Best-fit line $y=2x+5$. Predict $y$ when $x=100$.

✅ The prediction is $2(100)+5 = 205$, but this is **extrapolation** - $x=100$ is far outside the data range. The linear relationship may not hold.

❌ **Blind trust:** "The math says 205, so 205 is the answer" - the SAT expects you to recognize extrapolation as less reliable.

### [Very Hard] Multi-Concept: Scatterplot + Percent Increase (Improvement 28)
Scatterplot of years vs tuition. Line of best fit: $y=500x+8000$, where $x=0$ at 2010.
A) What is the predicted tuition in 2020 ($x=10$)?
B) What is the percent increase from 2010 to 2020?

A) $500(10)+8000 = 13,\!000$  
B) $(13000-8000)/8000 = 5000/8000 = 62.5\%$ increase

❌ **Part A only:** Computing the predicted value but forgetting to answer the percent change part. ❌ **Wrong base:** $(13000-8000)/13000 \approx 38.5\%$ - percent change always uses original value as base.

### [Very Hard] Interpret Residual (Improvement 43)
A linear model predicts crop yield from rainfall. One point: actual yield = 45, predicted = 40. Residual = 5.

✅ The model underestimates yield at that rainfall level by 5 units.

❌ **Direction error:** "The model overestimates yield by 5" - positive residual = underestimate.

### [Medium] Which r Matches the Scatterplot
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

---

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

### [Easy] Expected Value - Insurance (Improvement 16)
Insurance: $200 premium. 2% chance of $5,000 claim. Expected profit?

$E(\text{claim}) = 0.02 \times 5000 = 100$  
Expected profit: $200 - 100 = 100$

❌ **Ignoring premium:** "Expected profit is -4800" - confusing premium with profit.

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

### [Medium] "Among" = Conditional
Among those who failed, proportion who did not study?

$P(\text{not studied}|\text{failed}) = 50/70 = 5/7$

❌ **Wrong denominator:** $50/80$ (total not studied instead of total failed).

### [Medium] Counting Intuition (Improvement 15)
A restaurant offers 3 appetizers, 4 entrees, 2 desserts. How many different 3-course meals?

$3 \times 4 \times 2 = 24$

❌ **Addition:** $3 + 4 + 2 = 9$ - choices multiply, not add. For each appetizer you can pair any entree and any dessert.

### [Medium] Complement - "None" (Improvement 17)
Probability a driver has an accident in a year = 0.15. P(no accident in 3 years, assuming independence)?

$(0.85)^3 \approx 0.614$

❌ **Linear:** $1 - 3 \times 0.15 = 0.55$ - probabilities multiply, not add.

### [Hard] Tree Diagram - With Replacement
Bag: 3 red, 2 blue. Draw 2 with replacement. P(at least one red)?

$P(\text{both blue}) = (2/5)^2 = 4/25$  
$P(\text{at least one red}) = 1 - 4/25 = 21/25$

❌ **Wrong complement:** $1 - (3/5)^2$ - that computes "at least one blue," not "at least one red."

### [Hard] Independence Check
From the table above: Are passing and studying independent?

$P(\text{passed}) = 130/200 = 0.65$  
$P(\text{passed}|\text{studied}) = 100/120 \approx 0.833$

Since $0.833 \neq 0.65$, they are **dependent**.

❌ **Assuming independence** because both probabilities are high. Independence requires equality.

### [Hard] Expected Value - Business Decision (Improvement 16)
Product launch: 60% chance of $500K profit, 30% chance of $200K profit, 10% chance of $1M loss. Expected profit?

$E = 0.6 \times 500 + 0.3 \times 200 + 0.1 \times (-1000) = 300 + 60 - 100 = 260$K

❌ **Ignoring loss:** $0.6 \times 500 + 0.3 \times 200 = 360$K - the 10% loss probability matters.

### [Hard] Complement - "At most one" (Improvement 17)
Probability of rain on any day = 0.3, independent. P(at most one rainy day in 3 days)?

$P(0) = (0.7)^3 = 0.343$  
$P(1) = 3 \times (0.3)(0.7)^2 = 3 \times 0.147 = 0.441$  
$P(\text{at most one}) = 0.343 + 0.441 = 0.784$

❌ **Complement shortcut:** $1 - P(\text{at least 2})$ is possible but harder to compute directly. Summing $P(0)+P(1)$ is simpler.

### [Hard] Counting - How Many Outcomes? (Improvement 15)
A 4-digit PIN uses digits 0-9. Digits can repeat. How many possible PINs?

$10 \times 10 \times 10 \times 10 = 10,\!000$

❌ **Permutation formula:** $10 \times 9 \times 8 \times 7 = 5,\!040$ - that's without replacement (no repeats). The problem allows repeats.

### [Very Hard] Bayes' Theorem
60% employed. Of employed, 40% have degree. Of unemployed, 20% have degree. P(employed | degree)?

Out of 100 adults: employed = 60, unemployed = 40.  
Degree & employed: $60 \times 0.40 = 24$  
Degree & unemployed: $40 \times 0.20 = 8$  
Total with degree: $24+8 = 32$

$P(\text{employed}|\text{degree}) = 24/32 = 0.75$

❌ **Reversed probability:** Computing $P(\text{degree}|\text{employed}) = 0.40$ instead. The question conditions on "has a degree."

### [Very Hard] Expected Value with Negative Outcomes
Outcome A: win $5 (P=0.5), B: win $10 (P=0.3), C: lose $2 (P=0.2). Expected value?

$E = 5 \times 0.5 + 10 \times 0.3 + (-2) \times 0.2 = 2.5 + 3.0 - 0.4 = 5.1$

❌ **Ignoring negative:** Computing $5 \times 0.5 + 10 \times 0.3 + 0 \times 0.2 = 5.5$.

### [Easy] Independent Events Multiplication
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

## B3.6.3 Sample Size Reasoning

| Change | Effect on MoE | Effect on precision |
|--------|---------------|-------------------|
| Double sample size | MoE ÷ √2 (decreases) | More precise |
| Quadruple sample size | MoE ÷ 2 | Much more precise |
| Halve sample size | MoE × √2 (increases) | Less precise |
| Increase confidence level | MoE increases | Less precise |
| Decrease confidence level | MoE decreases | More precise |

⚡ MoE is proportional to $1/\sqrt{n}$. Doubling sample size does NOT halve MoE - it reduces it by a factor of about 1.4.

## B3.6.4 Sampling Methods

| Method | Random? | When to use |
|--------|---------|-------------|
| Simple random sample (SRS) | ✅ | Every member equally likely |
| Stratified (groups → random from each) | ✅ | Population has distinct subgroups |
| Systematic (every $k$th) | ✅ (if start random) | Ordered list available |
| Cluster (randomly select entire groups) | ✅ | Groups are natural, cost-effective |
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

### [Easy] Identifying Sampling Method
Randomly select 30 students from each grade (9-12). What method?

✅ Stratified random sampling.

❌ **Simple random sample:** "Randomly select 30 from the entire school" - but the method first divides by grade.

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

### [Medium] MoE Range Application
Mean commute = 34 min, MoE $\pm 3$ min. Which conclusion is justified?

✅ Population mean plausibly between 31 and 37 minutes.

❌ "All employees commute between 31 and 37 min" - MoE applies to the mean, not individuals. ❌ "34 min is the exact mean" - it's an estimate.

### [Medium] Identifying Bias
Website polls readers: 70% support Position A. Most valid criticism?

✅ The sample is self-selected (voluntary response bias).

❌ "Sample too small" - size matters less than representativeness. ❌ "MoE not given" - MoE doesn't fix bias from non-representative samples.

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
B) The true proportion of adults who exercise regularly could be 42%.
C) The true proportion of adults who exercise regularly is exactly 36%.
D) The true proportion of adults who exercise regularly is plausibly between 31% and 41%.

✅ C - "exactly" is not supported for sample estimates.

❌ **A/B:** Both 38% and 42% fall within [31%, 41%].

### [Hard] Sample Size and MoE
Poll of 400: 54% support. To reduce MoE, the pollster should:

✅ Increase sample size.

❌ "Increase MoE" - makes estimates less precise. ❌ "Poll wider area without changing sample size" - changes the population, not precision.

### [Hard] Sample Size Reasoning (Improvement 19)
Poll A: n=500, MoE $\pm 4\%$. Poll B: n=2,000, same population. MoE for B?

MoE is inversely proportional to $\sqrt{n}$. $\sqrt{2000/500} = \sqrt{4} = 2$. So MoE for B $\approx \pm 2\%$.

❌ **Linear:** "4× the sample = 1/4 the MoE = ±1%" - MoE scales with $1/\sqrt{n}$, not $1/n$.

### [Hard] Plausibility Judgment
Poll A: 300 residents, 62%, $\pm 5\%$. Poll B: 1,200 residents, 58%, $\pm 3\%$. What's supported?

A range: [57%, 67%]. B range: [55%, 61%]. Overlap: 57-61%.

✅ Plausible true support is between 57% and 61%.

❌ "Poll A is more accurate because 62% > 58%" - accuracy is about MoE/sample size, not the point estimate.

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

### [Hard] Bias - Question Wording
Survey asks: "Do you support the common-sense policy to improve our schools?" Results: 85% support. What bias?

✅ Question wording bias - the phrase "common-sense" leads respondents toward supporting.

❌ **Sample size:** 85% support is not necessarily wrong because of the sample size - it's the question phrasing that's biased.

### [Hard] Bias Type
Email survey on employee satisfaction, 15% response rate. Most concerning bias?

✅ Nonresponse bias. The 85% who didn't respond may have systematically different satisfaction.

❌ **Voluntary response** - this is technically nonresponse. ❌ **Undercoverage** - everyone got the email.

### [Hard] Explain Why Conclusion is Invalid (Improvement 47)
A study asks 100 people at a gym about exercise habits and concludes: "Americans exercise at least 3 times per week." Why is this conclusion invalid?

✅ The sample is from a gym (not representative of all Americans), and it's a convenience sample.

❌ "Sample too small" - 100 can be adequate if representative; the problem is who was sampled, not how many.

### [Very Hard] Sampling + Assignment
Randomly select 1,000 adults, randomly assign half to fitness program, half to control. Fitness group has lower cholesterol. Valid conclusions?

✅ Generalization (random selection) + causation (random assignment). This is the gold standard.

### [Very Hard] Misleading Inference
50 patients (not randomly selected) get treatment; 50 different patients (not randomly selected) are control. Treatment group has better outcomes. Main flaw?

✅ Without random assignment, the groups may differ in confounding variables. The difference could be due to pre-existing differences, not the treatment.

❌ "No control group" - there is one, but it's not equivalent. ❌ "Sample too small" - size < lack of randomization.

### [Very Hard] Evaluate Study (Improvement 45)
A company claims its product reduces headaches based on a study where 100 volunteers who used the product reported fewer headaches than 100 non-volunteers who did not. What is the most serious flaw?

✅ Volunteers self-selected into groups - no random assignment. Those who chose to use the product may differ in other ways.

❌ "Not enough people" - 200 is fine. The issue is self-selection bias and lack of randomization.

### [Easy] Sample Mean Estimates Population Mean
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
| Video gamers have faster reflexes | Gaming | Reflex speed | Age (younger people game more AND have faster reflexes) |
| More firefighters → more damage | Firefighters | Property damage | Fire size (more firefighters for bigger fires) |
| Ice cream sales → drownings | Ice cream | Drownings | Temperature (hot → more ice cream AND more swimming) |
| Yoga reduces back pain | Yoga | Back pain | Exercise frequency (yoga-doers may exercise more overall) |
| Students in tutoring score higher | Tutoring | Grades | Prior achievement (higher-achieving students seek tutoring) |
| Pet owners have lower stress | Pet ownership | Stress | Income (higher income → more likely to own pets AND less stress) |
| Night-shift workers have more accidents | Night shift | Accidents | Fatigue (not night shift itself) |
| Multivitamin users are healthier | Multivitamins | Health | Education/income (higher SES → more supplement use AND better health) |

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

### [Medium] Random Assignment → Causation
100 volunteers randomly assigned to new drug or placebo. Drug group has fewer symptoms. Conclusion?

✅ The drug causes symptom reduction (random assignment controls for confounding).

❌ "The drug works in the general population" - volunteers aren't a random sample, so generalization is limited. But the causal claim itself is justified.

### [Medium] Confounding Variable
Students who take SAT prep courses score higher. Critic argues those students are already more motivated. What is this?

✅ A confounding variable (motivation) that could explain the association without prep courses causing higher scores.

### [Medium] Experiment - Education (Improvement 21)
A school compares test scores: one class uses a new curriculum, another uses the old. The teacher chose which class gets which. Main flaw?

✅ Teacher bias in assignment - the teacher may have put stronger students in the new curriculum class. No random assignment.

❌ "The curriculum is ineffective" - can't conclude anything because groups weren't equivalent.

### [Medium] Experiment - Marketing (Improvement 21)
An company emails two ad designs to randomly selected halves of its customer list. Design A gets more clicks. Conclusion?

✅ Design A is more effective (random assignment of customers to ad designs).

❌ "Design A will work for all customers" - generalization depends on whether the customer list is representative of the target audience.

### [Hard] Identifying Bias in Study Design
50,000 people followed for 10 years - those who chose to take vitamins had better health outcomes. Main limitation?

✅ Confounding: Vitamin-takers may also exercise more, eat better, have higher income. Can't separate vitamin effect from these factors.

❌ "Sample too large" - large sample doesn't fix lack of randomization. ❌ "No control group" - there's an implicit control group (non-takers), but it's not equivalent.

### [Hard] Experiment - Exercise (Improvement 21)
100 volunteers randomly assigned: 50 to running program, 50 to no exercise. The running group had more injuries. Can we conclude running causes injuries?

✅ Yes - random assignment controls for confounding. Running causes more injuries under these conditions.

❌ "Runners were more injury-prone to begin with" - random assignment makes the groups equivalent at the start.

### [Hard] Confounding Variable
A study finds that students who eat breakfast score higher on tests. An education researcher argues that family income is a confounding variable. Explain.

✅ Higher-income families are more likely to provide breakfast AND have educational resources. Breakfast may not cause higher scores - income confounds the relationship.

❌ "Breakfast directly improves brain function" - possible but not proven by the study; the confounder offers an alternative explanation.

### [Very Hard] Matching Design to Conclusion
Study 1: Survey 5,000 randomly selected adults. Finds 7-8 hr sleepers score higher on memory tests.

Study 2: Randomly assign 200 adults to 6 or 8 hrs sleep for a week. 8-hr group scores higher.

Which conclusions are supported?

✅ Study 1: Association in the population (random selection), not causation. ✅ Study 2: Sleep duration causes memory difference (random assignment). Generalization limited (200 volunteers, not random sample).

### [Very Hard] Matching Design to Conclusion 2
Study A: Randomly sample 1,000 adults, measure TV hours and BMI, find positive correlation.
Study B: Randomly assign 100 adults to 2 hrs or 5 hrs of daily TV for 3 months, measure BMI change.

Which claims are supported?

✅ Study A: Association between TV time and BMI in the population (random sample, no assignment).  
✅ Study B: TV time causes BMI change (random assignment, but limited generalization because 100 volunteers aren't random sample of population).

❌ Study A: "More TV causes higher BMI" - no random assignment, so association only.

### [Medium] Placebo Effect
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

---

# 9. The 22 Data Analysis Traps

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

### Trap 9: Confusing $P(A|B)$ with $P(B|A)$
Usually different. Check the condition word carefully - "given that B" $\neq$ "given that A."

### Trap 10: Confusing Percentage Points with Percent Change
4% → 6% = +2 pp, +50% relative. Different quantities.

### Trap 11: Percent Change on Wrong Base
25% discount then 20% off: the 20% applies to the already-discounted price. Reverse percent = divide by multiplier, not multiply.

### Trap 12: Misreading Graph Scale
Non-zero $y$-axes, unequal bin widths, misleading visual impressions. Always read axis labels and values.

### Trap 13: Confusing Range with SD
Large range + small SD possible (most values cluster near mean with a few extremes). SD measures spread of entire distribution.

### Trap 14: Forgetting the Complement in "At Least One"
$P(\text{at least one}) = 1 - P(\text{none})$. Compute complement, don't sum individual probabilities.

### Trap 15: Confusing Study Design
Random selection $\neq$ random assignment. Selection $\rightarrow$ generalize. Assignment → causation. Don't mix them up.

### Trap 16: "Increase by" vs "increase to" vs "percentage points"
"Increase by 15%" = ×1.15. "Increase to 115%" = ×1.15 (same). But "increase by 15 percentage points" = +15 pp (different). SAT uses all three.

### Trap 17: Extrapolation Blindness
Predicting outside the data range using the same model. The relationship may change. "Based on the data" vs "outside the range" - recognize when a prediction is extrapolation.

### Trap 18: Misinterpreting "On average" / "Predicted" / "Estimated"
These words signal the answer is from a model, not exact. "Predicted score = 80" $\neq$ "actual score = 80." The words are clues, not noise.

### Trap 19: Confusing the Residual Sign
Residual = actual − predicted. Positive = above line = model underestimates. Negative = below line = model overestimates. ✅ Remember: "Actual minus predicted" or "A − P."

### Trap 20: Assuming Independence Without Checking
$P(A|B) = P(A)$ is the definition. Visual inspection of a two-way table is not enough - compute both probabilities. High values $\neq$ dependent or independent.

### Trap 21: Percent Error on the Wrong Base
Percent error divides by the actual value, not the estimate: $\frac{|E - A|}{A}$. An estimate of 90 for an actual 100 is a 10% error, not 11.1%.

### Trap 22: Reverse Probability - Confusing Condition and Cell
Given $P(A|B)$, the cell count is $P(A|B) \times$ (total of B). Never multiply by the grand total - the condition group size is the denominator.

---

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
- **$R^2$ value:** If $R^2 < 0.7$, linear may be a poor fit.
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
- **Delete a table:** Click the x on the table header.

## Quick Calculations

- **Percentages:** Chain multipliers directly: `150 * 1.30 * 0.85` for 30% markup then 15% discount.
- **Statistics:** `L = [12, 7, 9, 14, 3]` → `mean(L)`, `median(L)`, `stdev(L)`.
- **Unit conversion:** Type directly: `60 * 5280 / 3600`.
- **Probability fractions:** `100/120` → Desmos returns $5/6$ in fraction form.
- **Reverse percent:** `45 / 0.75` → 60 (original price before 25% off).
- **Expected value:** `10*0.3 + 0*0.7 - 5` → net expected value with cost.
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
| Not checking $R^2$ | Low $R^2$ → try a different model type |
| Forgetting $x$ range context | Predictions outside data range may be meaningless |
| Not computing residuals | Residual plot reveals whether linear model is appropriate |
| Ignoring the residual plot shape | Random = good; curved = bad |

---

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

### [Hard] Best Estimate (Improvement 42)
A box plot: min=10, Q1=25, median=40, Q3=55, max=80. Which is the best estimate of the mean?
A) 10   B) 25   C) 45   D) 80

✅ C - the mean is typically near the median for roughly symmetric distributions. The median is 40, and the data is fairly symmetric (whiskers are 15 and 25, box is 15 each side), so 45 is the closest.

❌ **A or D:** Min and max are extreme values, not estimates of center.

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

## B3 at a Glance (Final Revision Reference)

### Formulas by Priority

| Priority | What |
|----------|------|
| `[CORE]` | Mean, median, mode, range, IQR, percent change, probability, proportion, unit conversion |
| `[MEMORIZE]` | SD interpretation (no calc), outlier rule, weighted average, conditional probability, expected value, margin of error, compound growth, sampling vs bias types |
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
