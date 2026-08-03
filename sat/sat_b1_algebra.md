# Digital SAT Algebra (Domain B1)

~35% of Math section - 13-15 of 44 questions. Five official testing points covering linear equations, functions, systems, and inequalities. Desmos built-in on every question.

**Domain cross-references:** B2 (Advanced Math) for quadratic/exponential systems, piecewise functions | B3 (Data Analysis) for linear models in context | B4 (Geometry & Trig) for coordinate geometry applications

---

## Most Common Question Types on the Actual Exam

These are the question formats the real Digital SAT repeatedly uses for Algebra. If you master only this list, you cover most of the 13-15 Algebra questions you will see. (Based on analysis of official College Board practice tests, the Assessment Framework, and Khan Academy's SAT course structure.)

1. **Solve a linear equation** - a straightforward "solve for $x$" with distribution and/or fractions. Expect 3-5 of these (often with a twist like solving for a coefficient instead).
2. **Create an equation from a word problem** - mechanic fee, tank draining, taxi fare. You write the equation or pick the correct one from the choices. Flat fee + rate structure.
3. **Interpret a constant or coefficient in context** - "In $C = 40h + 25$, what does the 40 represent?" The answer is always a rate or fixed amount with units. Never "the total cost."
4. **No solution / infinitely many solutions with a parameter** - "For what value of $k$ does $3(2x - 5) = 6x + k$ have no solution?" Compare coefficients AND constants. Watch the classic trap: the answer is "any $k$ except $-15$", not $k = -15$.
5. **Systems of equations** - solve and report $x + y$ (not $x$ or $y$ alone), or determine how many solutions two lines have by comparing slopes.
6. **Linear vs. exponential growth** - a table or a sentence ("increases by 3 each year" vs. "increases by 3% each year"). Constant differences = linear; constant ratios = exponential.
7. **Inequalities in context** - budget or capacity constraints. You may need to check whether a given point (order, plan, combination) satisfies the inequality - the point is "feasible" or not.
8. **Percent change word problems** - find the percent change, the new amount, or work backward to the original amount.
9. **Linear function from two points or a table** - find slope, then intercept, then evaluate or interpret.
10. **Standard form $Ax + By = C$ in context** - what each coefficient means (per-unit rates) and what $C$ is (the total), plus finding intercepts from it.

---

## Quick Reference

### Slope & Lines
| Formula | Notes |
|---|---|
| $m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\Delta y}{\Delta x}$ | Rise over run |
| $y = mx + b$ | $m$ = slope, $b$ = $y$-intercept |
| $y - y_1 = m(x - x_1)$ | Point-slope form |
| $Ax + By = C$ | $m = -\frac{A}{B}$, $y$-int $= \frac{C}{B}$, $x$-int $= \frac{C}{A}$ |
| $\frac{x}{a} + \frac{y}{b} = 1$ | $x$-int $= a$, $y$-int $= b$ |
| $y = k$ (horizontal) | $m = 0$ |
| $x = h$ (vertical) | $m$ undefined |
| Parallel: $m_1 = m_2$ | Perpendicular: $m_1 \cdot m_2 = -1$ |
| $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$ | Midpoint: $\left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$ |

### Standard Form $Ax + By = C$ in Context
| Part | Meaning in context |
|---|---|
| $A$ | Units of $C$ contributed per 1 unit of $x$ (a per-unit rate) |
| $B$ | Units of $C$ contributed per 1 unit of $y$ (a per-unit rate) |
| $C$ | The total, budget, or limit |
| Slope $-\frac{A}{B}$ | Trade-off rate: $x$ must decrease $\frac{A}{B}$ units per extra unit of $y$ |

### One-Variable Equation Types
| Simplifies to | Solutions | Type |
|---|---|---|
| $x = c$ | 1 | Conditional |
| $0 = 0$ | Infinite | Identity |
| $0 = c$ ($c \neq 0$) | 0 | Contradiction |

**One-variable solution count:** rewrite both sides as $(\text{coefficient})x + (\text{constant})$.
- Same coefficient, same constant $\Rightarrow$ infinite (identity)
- Same coefficient, different constant $\Rightarrow$ none (contradiction)
- Different coefficients $\Rightarrow$ one (conditional)

### Systems: Number of Solutions
| Condition | Solutions |
|---|---|
| $m_1 \neq m_2$ | 1 (intersecting) |
| $m_1 = m_2$, $b_1 \neq b_2$ | 0 (parallel) |
| $m_1 = m_2$, $b_1 = b_2$ | Infinite (coincident) |

Standard form: $\frac{A_1}{A_2} = \frac{B_1}{B_2} \neq \frac{C_1}{C_2} \Rightarrow 0$; all three equal $\Rightarrow \infty$.

### Inequality Rules
- ×/÷ by **negative** → **flip** the sign
- Solid boundary: $\leq, \geq$ | Dashed: $<, >$
- Shade **above** for $>/\geq$, **below** for $</\leq$
- Compound "and" = intersection; "or" = union
- **Point-in-region test:** plug the point into the inequality. True $\Rightarrow$ in the solution set; false $\Rightarrow$ outside. On the boundary line $\Rightarrow$ included only if $\leq$ or $\geq$.

### Percent Change
| Formula | Use |
|---|---|
| Percent change $= \frac{\text{new} - \text{original}}{\text{original}} \times 100\%$ | Given two amounts, find the % |
| New amount $= \text{original} \times \left(1 \pm \frac{p}{100}\right)$ | Apply a $p\%$ increase (+) or decrease (-) |
| Original $= \frac{\text{new}}{1 \pm p/100}$ | Work backward from the new amount |

### Linear vs. Exponential Growth
| Feature | Linear | Exponential |
|---|---|---|
| Repeated change | Add the same difference | Multiply by the same factor |
| Common form | $y = mx + b$ | $y = ab^x$ |
| Table test | First differences constant | Ratios constant (outputs nonzero) |
| Wording | "Increases by 3 each year" | "Increases by 3% each year", "triples", "doubles" |

### Absolute Value
$|A| = b$ ($b \geq 0$) → $A = b$ or $A = -b$
$|A| = b$ ($b < 0$) → no solution
$|A| < b$ → $-b < A < b$ (less th**and**)
$|A| > b$ → $A < -b$ or $A > b$ (**great**or)

### Direct & Inverse Variation
| Type | Equation | Constant |
|---|---|---|
| Direct | $y = kx$ | $k = y/x$ (constant ratio) |
| Inverse | $y = k/x$ or $xy = k$ | $k = xy$ (constant product) |

### Word Problem Keywords
| English | Algebra |
|---|---|
| is, equals, resulted in | $=$ |
| sum, more than, increased by, total | $+$ |
| difference, less than, decreased by | $-$ |
| times, product, each, per | $\times$ |
| divided by, per, ratio | $\div$ |
| at least, minimum, not less than | $\geq$ |
| at most, maximum, not more than | $\leq$ |
| three less than a number | $x - 3$ (not $3 - x$) |
| varies directly / is proportional to | $y = kx$ |
| varies inversely | $y = k/x$ |

### Desmos Tips for Algebra
- **One-variable equation:** Graph LHS as $y_1$, RHS as $y_2$; intersection $x$ = solution
- **System:** Graph both equations, click intersection point
- **Inequality:** Type directly (`y < 2x+1`); Desmos shades automatically
- **Absolute value:** Use `abs(x)` or `|x|` (Shift + \)
- **Parameter slider:** Use `k` in equations; drag to test values
- **Function eval:** Define `f(x) = ...` then type `f(3)`
- **Table → equation:** Enter table, type `y1 ~ mx1 + b` for regression
- **Fractions:** Parentheses: `(2x+1)/(x-3)` not `2x+1/x-3`
- **Point-in-region check:** Type the inequality, then plot the point; if it lands in the shaded region, it satisfies the inequality

---

## B1.1 Linear Equations in One Variable

**What they test:** Solving $ax + b = c$ (and variants), determining solution type (unique/none/infinite), creating equations from word problems, interpreting constants in context. On the real test, expect roughly **3-5 questions** from this testing point alone.

### B1.1.1 Solving Standard Linear Equations

**Definition in simplest terms:** A linear equation in one variable is an equation that can be written as $ax + b = c$, where $x$ is the unknown and $a$, $b$, $c$ are numbers with $a \neq 0$. Solving it means finding the value(s) of $x$ that make the equation true.

**Step-by-step method:**
1. **Distribute** - multiply through any parentheses: $a(x + b) = ax + ab$.
2. **Clear fractions** - multiply both sides by the least common denominator (LCD) if fractions are present.
3. **Combine like terms** - add/subtract same-type terms on each side.
4. **Isolate the variable** - move all $x$-terms to one side, all constants to the other.
5. **Solve** - divide both sides by the coefficient of $x$.
6. **Check** - plug the answer back in (or use Desmos). If both sides match, you are right.

**[Easy] Solve $3(x - 4) = 2x + 5$ for $x$.**

$3x - 12 = 2x + 5$ → $x = 17$

✅ **Check:** $3(17-4) = 39$, $2(17)+5 = 39$.

❌ **Trap:** $3x - 4 = 2x + 5 \to x = 9$  -  **Distribution error** (forgot to multiply $-4$ by 3).

---

**[Medium] Solve $4(y + 1) - 3y = 2(y - 3) + 5$ for $y$.**

$4y + 4 - 3y = 2y - 6 + 5$ → $y = 5$

⚡ **Desmos check:** Graph $y_1 = 4(x+1)-3x$, $y_2 = 2(x-3)+5$. Intersection at $x = 5$.

---

**[Medium] Solve $\frac{3}{4}x - \frac{1}{2} = \frac{5}{8}$.**

Multiply by 8 (LCD): $6x - 4 = 5$ → $x = \frac{3}{2}$

❌ **Trap:** $6x - \frac{1}{2} = 5 \to x = \frac{11}{12}$  -  **Partial multiplication** (only multiplied $x$ term by 8).

---

**[Medium] If $3(x - 2) + a = 5x - 6$ and $x = 4$, what is $a$?**

$3(4-2) + a = 5(4)-6$ → $6 + a = 14$ → $a = 8$

❌ **Trap:** Solving for $x$ instead of $a$  -  **Wrong variable target**.

---

**[Hard] Solve $\frac{x + 3}{2} = \frac{2x - 1}{3} + 1$ for $x$.**

Multiply by 6 (LCD): $3(x + 3) = 2(2x - 1) + 6$ → $3x + 9 = 4x - 2 + 6$ → $3x + 9 = 4x + 4$ → $x = 5$

✅ **Check:** $\frac{5+3}{2} = 4$; $\frac{10-1}{3} + 1 = 3 + 1 = 4$. ✔

❌ **Trap:** Multiplying only the fraction terms by 6 and leaving $+1$ alone  -  **every term gets multiplied by the LCD**.

⚡ **Desmos tip:** Type `(x+3)/2` as $y_1$ and `(2x-1)/3+1` as $y_2$; the intersection $x$-value is the solution. Instant check.

---

**[Very Hard] Solve $\frac{2x - 1}{5} - \frac{x - 2}{3} = \frac{1}{15}$ for $x$.**

Multiply by 15 (LCD): $3(2x - 1) - 5(x - 2) = 1$ → $6x - 3 - 5x + 10 = 1$ → $x + 7 = 1$ → $x = -6$

✅ **Check:** $\frac{-13}{5} - \frac{-8}{3} = \frac{-39 + 40}{15} = \frac{1}{15}$. ✔

❌ **Trap:** Forgetting to distribute the minus sign: $-5(x - 2)$ must give $-5x + 10$, not $-5x - 10$.

---

### B1.1.2 Identity, Conditional, and Contradiction

**Definition in simplest terms:** Every linear equation in one variable is one of three types:

- **Conditional equation** - true only for specific value(s) of the variable. Example: $2x + 3 = 7$ is true only when $x = 2$. Exactly **one solution**.
- **Identity** - true for **every** value of the variable. Example: $2(x + 3) = 2x + 6$. The two sides are algebraically equivalent - they are the same expression wearing different clothes. **Infinite solutions.**
- **Contradiction** - true for **no** value of the variable. Example: $2(x + 3) = 2x + 7$ simplifies to $6 = 7$, which is false. **No solution.**

| Type | Simplifies to | Solutions |
|---|---|---|
| **Conditional** | $x = c$ | Exactly 1 |
| **Identity** | $0 = 0$ or $5 = 5$ | All real numbers |
| **Contradiction** | $0 = 5$ or $3 = 7$ | None |

**Step-by-step method:**
1. Simplify both sides completely (distribute, combine like terms).
2. If the variable remains: **conditional** - solve normally.
3. If the variable cancels: compare the remaining constants.
   - Same constant on both sides ($0 = 0$): **identity** - infinite solutions.
   - Different constants ($0 = 5$): **contradiction** - no solution.

**Quick test:** Same $x$-coefficient + same constant → identity. Same coefficient + different constant → contradiction. Different coefficients → conditional.

**[Easy] Classify $2(x + 3) = 2x + 6$: conditional, identity, or contradiction?**

$2x + 6 = 2x + 6$ → $0 = 0$. **Identity** - true for all $x$. Plug in $x = 1$: $8 = 8$. Plug in $x = 100$: $206 = 206$. Always true.

---

**[Easy] Classify $2x + 3 = 7$: conditional, identity, or contradiction?**

$2x = 4$ → $x = 2$. **Conditional** - true only for $x = 2$.

---

**[Easy] Classify $2(x + 3) = 2x + 7$: conditional, identity, or contradiction?**

$2x + 6 = 2x + 7$ → $6 = 7$. **Contradiction** - false for every $x$, no solution.

❌ **Trap:** "The $x$'s cancel, so there's no solution" is only half right - you must check the constants. If the constants also match, it is an identity with infinite solutions, not a contradiction.

---

**[Medium] How many solutions does $4(x - 3) + 8 = 4x - 4$ have?**

$4x - 12 + 8 = 4x - 4$ → $4x - 4 = 4x - 4$ → $0 = 0$. **Identity**  -  infinite solutions.

❌ **Trap:** "They cancel, no solution"  -  **Confusing identity with contradiction**. $x$ cancels AND constants match → infinite.

---

**[Hard] If $3(2x - 5) + k = 6x - 15$ has infinitely many solutions, what is $k$?**

$6x - 15 + k = 6x - 15$. For identity: $-15 + k = -15$ → $k = 0$.

---

**[Hard] $2(px + 3) = 4x + 6$. For what $p$ does the equation have (a) one solution? (b) no solution? (c) infinite solutions?**

$2px + 6 = 4x + 6$

(a) One solution when $2p \neq 4$, i.e., $p \neq 2$.
(b) No solution requires $2p = 4$ AND $6 \neq 6$  -  impossible. **No such $p$.**
(c) Infinite when $2p = 4$ AND $6 = 6$, i.e., $p = 2$.

❌ **Trap:** Assuming every parameter can produce all three types  -  **The constant equality condition may already be decided**.

---

**[Very Hard] For what $c$ does $2(x - 3) + 5 = 2x + c$ have no solution?**

$2x - 6 + 5 = 2x + c$ → $2x - 1 = 2x + c$. $x$ coefficients match ($2 = 2$), so no solution when constants differ: any $c \neq -1$. If $c = -1$, infinite solutions.

❌ **Trap:** Writing "$c = -1$" - that is the identity value. The question asks for no solution, so the answer is **every value except** $-1$.

---

### B1.1.3 No Solution / Infinite Solutions in One Variable (Own Worked Treatment)

The SAT loves parameter questions where you decide the solution count. The method for ONE variable is different from the two-variable slope method in B1.4 - here you compare **coefficients and constants** on each side.

**Step-by-step method:**
1. Simplify both sides so each looks like $(\text{coefficient of }x)x + (\text{constant})$.
2. Compare the coefficients of $x$:
   - **Different coefficients** → exactly 1 solution (conditional).
   - **Same coefficients** → the variable cancels; now compare constants.
3. Compare the constants:
   - **Same constants** → identity, infinite solutions.
   - **Different constants** → contradiction, no solution.

In short: same coefficient + same constant = infinite; same coefficient + different constant = none; different coefficients = one.

**[Easy] How many solutions does $3x + 2 = 3x - 7$ have?**

Same coefficient ($3 = 3$), different constants ($2 \neq -7$). **No solution.** $0 = -9$ is false.

---

**[Easy] How many solutions does $2(3x + 1) = 6x + 2$ have?**

$6x + 2 = 6x + 2$. Same coefficient, same constant. **Infinite solutions** (identity).

---

**[Medium] How many solutions does $6x - 9 = 3(2x - 4)$ have?**

$6x - 9 = 6x - 12$ → $0 = -3$. Same coefficient, different constant. **No solution.**

❌ **Trap:** Saying "infinite" because both sides have $6x$  -  you must check the constants too. $-9 \neq -12$.

---

**[Hard] The equation $3(2x - 5) = 6x + k$ has no solution. What can you say about $k$?**

$6x - 15 = 6x + k$ → $-15 = k$. For **no** solution this must be a false statement: $k$ can be **any value except $-15$**.

❌ **Trap (a classic):** Answering "$k = -15$". If $k = -15$, the equation becomes $-15 = -15$, which is always true - that gives **infinitely many** solutions. "No solution" is the opposite: every $k$ except $-15$.

⚡ **Desmos tip:** Slide $k$ with a slider (type `k = 0`, then drag). Watch the two lines $y_1 = 3(2x-5)$ and $y_2 = 6x+k$: parallel (no intersection) for all $k \neq -15$; identical lines at $k = -15$.

---

**[Very Hard] The equation $ax + b = 2x + 7$ has infinitely many solutions. What are $a$ and $b$?**

For infinite solutions the two sides must be identical: $a = 2$ and $b = 7$.

**[Very Hard variant] The equation $ax + 4 = 3x + b$ has no solution. What must be true of $a$ and $b$?**

Same coefficient, different constant: $a = 3$ and $b \neq 4$.

❌ **Trap:** Only matching the $x$-coefficients and forgetting the constant condition. No solution requires BOTH: coefficients equal AND constants unequal.

---

### B1.1.4 Word Problems: Creating One-Variable Equations

**Definition in simplest terms:** Translate an English situation into an equation $ax + b = c$, solve it, and answer what was actually asked (which may not be $x$ itself).

**Step-by-step method:**
1. Read the problem twice. Identify the unknown - **define the variable** (e.g., "Let $x$ = liters of water added").
2. Find the relationship: a flat amount + a rate, or a formula (distance, mixture, age).
3. Translate the keywords into algebra (see Quick Reference keyword table).
4. Write the equation, solve it.
5. Re-read the question: does it ask for $x$, or for something built from $x$ (like $2x + 12$)?
6. Check that the answer makes sense in the story (no negative ages, no negative liters).

**[Easy] The sum of a number and 12 is 31. Find the number.**

Let $x$ = the number. $x + 12 = 31$ → $x = 19$.

✅ **Check:** $19 + 12 = 31$. ✔

---

**[Medium] A 200-liter mixture is $15\%$ salt. How many liters of pure water must be added to make it $10\%$ salt?**

Let $x$ = liters of water added. Salt before: $0.15(200) = 30$ L. Total after: $200 + x$ L.

$0.10(200 + x) = 30$ → $20 + 0.1x = 30$ → $x = 100$

❌ **Trap:** $0.15(200) + x = 0.10(200 + x)$  -  **Treating water as if it contains salt**. Water adds volume but zero salt.

---

**[Medium] A train travels 300 miles at constant speed. If the speed were 10 mph faster, the trip would take 1 hour less. Find the original speed.**

Let $r$ = original speed. Time: $\frac{300}{r}$; time at $r+10$: $\frac{300}{r+10}$.

$\frac{300}{r} - \frac{300}{r+10} = 1$ → $300(r+10) - 300r = r(r+10)$ → $r^2 + 10r - 3000 = 0$ → $(r+60)(r-50) = 0$ → $r = 50$ mph

❌ **Trap:** $\frac{240}{r} = \frac{240}{r+10} + 1$  -  **Inverse subtraction**. Faster trip takes less time → shorter time + 1 = longer time.

---

**[Hard] Jack is twice as old as Jill. In 12 years, the sum of their ages will be 75. How old is Jill now?**

Let $x$ = Jill's age. Jack = $2x$. In 12 years: Jill = $x+12$, Jack = $2x+12$.

$(x+12) + (2x+12) = 75$ → $3x = 51$ → $x = 17$

❌ **Trap:** Adding 12 to Jack but forgetting to add 12 to Jill  -  **Asymmetric future ages**.

---

**[Hard] A chemist has 40 mL of $25\%$ acid solution. How many mL of pure acid must be added to create $40\%$ acid?**

Let $x$ = mL pure acid. Acid before: $0.25(40) = 10$ mL. Total after: $40+x$ mL. Acid after: $10+x$ mL.

$0.40(40+x) = 10+x$ → $16 + 0.4x = 10 + x$ → $x = 10$

❌ **Trap:** $0.40(40+x) = 10$  -  **Forgetting added acid increases the acid amount, not just volume**. Right side must be $10+x$.

---

**[Very Hard] A tank holds 100 gallons of a $30\%$ salt solution. How many gallons must be drained and replaced with pure water so the tank is $20\%$ salt?**

Let $x$ = gallons drained (and replaced with water). Salt removed: $0.30x$ gallons. Salt remaining: $30 - 0.30x$ gallons. Total volume stays 100 gallons.

$0.20(100) = 30 - 0.30x$ → $20 = 30 - 0.3x$ → $0.3x = 10$ → $x = \frac{100}{3} \approx 33.3$ gallons

❌ **Trap:** Writing $0.30(100 - x) = 20$ and stopping - that is correct, but make sure you solve for $x$ = gallons **drained**, not the remaining volume. Also: replacing with water means the salt amount drops but total volume stays 100.

---

### B1.1.5 Parameter and Constant Interpretation

**Definition in simplest terms:** In a model like $C = mn + b$, the **coefficient** $m$ is the rate (change per unit), and the **constant** $b$ is the value of $C$ when $n = 0$ (the starting/fixed amount).

**Step-by-step method:**
1. Identify the variable and its units.
2. The number multiplying the variable = change **per one unit** of the variable.
3. The standalone constant = the value when the variable is 0.
4. State the meaning with units: "the cost, in dollars, **per hour**" - never just "the cost".

**[Easy] A taxi charges $C = 3h + 10$, where $h$ is miles driven. What does the 3 represent? What does the 10 represent?**

- 3 = the charge, in dollars, **per mile**.
- 10 = the base fare, in dollars, charged for 0 miles (the flag drop).

❌ **Trap:** Saying "3 is the total cost"  -  the coefficient is a per-unit rate, not a total.

---

**[Medium] $C = 5n + 200$ models production cost for $n$ widgets. What does 200 represent?**

Cost when $n = 0$: fixed costs (equipment, rent).

❌ **Trap:** "Cost per widget"  -  **Confusing intercept with slope**. The 5 is per-unit; 200 is fixed.

---

**[Hard] $p = 50 - 0.2q$ models price $p$ at which $q$ units sell. Interpret 50.**

When $q = 0$, $p = 50$: the price when no units are sold (maximum price).

❌ **Trap:** "Maximum number of units"  -  **Reading a zero-output as an input constraint**. The $q$-intercept (where $p = 0$) gives max quantity.

---

**[Very Hard] A drone's altitude is modeled by $h(t) = 1200 - 25t$, where $t$ is minutes after launch. Interpret the 1200, the $-25$, and find when the drone lands.**

- 1200 = starting altitude, in meters, at $t = 0$ (launch).
- $-25$ = the altitude **decreases by 25 meters per minute** (rate of descent).
- Landing: $h(t) = 0$ → $1200 - 25t = 0$ → $t = 48$ minutes.

❌ **Trap:** Saying "the drone loses 25 meters total"  -  $-25$ is the rate **per minute**. Total loss is 1200 m. The negative sign tells you the direction (decreasing).

---

## B1.2 Linear Functions

**What they test:** $f(x) = mx + b$, point-slope form, interpreting slope and intercept in context, writing equations from two points or point + rate, connecting tables/graphs/algebra. The official testing point also requires: evaluate a function for an input or find the input from an output, and write a rule given two input-output pairs or one pair + a rate of change.

### B1.2.1 Function Notation and Evaluation

**Definition in simplest terms:** $f(x)$ means "the output of function $f$ when the input is $x$." For a linear function $f(x) = mx + b$, $m$ is the slope (rate) and $b$ is the $y$-intercept (output when input is 0).

**Step-by-step method:**
- **Evaluate (input → output):** substitute the number for $x$ and compute.
- **Find input (output → input):** set $f(x)$ equal to the given output and solve for $x$.

**[Easy] If $f(x) = 3x - 5$, find $f(4)$.** → $f(4) = 3(4) - 5 = 7$

**[Medium] If $f(x) = 2x + 1$ and $f(a) = 17$, find $a$.** → $2a + 1 = 17$ → $a = 8$

**[Medium] If $f(2) = 5$ and $f(6) = 13$, find $f(x)$.**

$m = \frac{13-5}{6-2} = 2$. $f(x) = 2x + b$; $5 = 2(2) + b$ → $b = 1$. $f(x) = 2x + 1$.

❌ **Trap:** $f(2) = 5$ means $b = 5$  -  **Intercept = $f(0)$, not $f(2)$**.

---

**[Hard] If $f(x) = -4x + 9$, find the input $x$ such that $f(x) = -11$.**

$-11 = -4x + 9$ → $-4x = -20$ → $x = 5$

❌ **Trap:** Reporting $-11$ as the input  -  the output and input are swapped in the question. $f(5) = -11$, so $5$ is the input.

---

**[Very Hard] If $f(x) = 3x - 1$, what is $f(x + 2) - f(x)$?**

$f(x+2) = 3(x+2) - 1 = 3x + 6 - 1 = 3x + 5$. So $f(x+2) - f(x) = (3x + 5) - (3x - 1) = 6$.

⚡ **Insight:** The answer is always $m \times 2 = 6$: adding 2 to the input adds $2m$ to the output. This is a fast SAT pattern - no algebra needed.

---

### B1.2.2 Slope and Rate of Change

**Definition in simplest terms:** Slope measures how fast $y$ changes per 1 unit of $x$: $m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\Delta y}{\Delta x}$. The units of $m$ are (units of $y$) per (unit of $x$).

**Step-by-step method:**
1. Pick two points (or two rows of a table).
2. Subtract the $y$-values (rise), subtract the $x$-values (run), in the **same order**.
3. Divide: $m = \frac{\text{rise}}{\text{run}}$.
4. For a linear function, the rate of change is the same between **any** two points.

**[Easy] Find the slope of the line through $(1, 2)$ and $(4, 11)$.**

$m = \frac{11 - 2}{4 - 1} = \frac{9}{3} = 3$

❌ **Trap:** Computing $\frac{x_2 - x_1}{y_2 - y_1}$ (inverted)  -  slope is **rise over run**, always $\frac{\Delta y}{\Delta x}$.

---

**[Medium] The table shows a linear relationship:**

| $x$ | 1 | 3 | 5 |
|---|---|---|---|
| $y$ | 7 | 15 | 23 |

$m = \frac{15-7}{3-1} = 4$. $7 = 4(1) + b$ → $b = 3$. $f(x) = 4x + 3$.

✅ **Check:** $f(5) = 4(5) + 3 = 23$. Matches table.

❌ **Trap:** Reading $b = 7$ from the first row  -  **$b$ is $f(0)$, not the first $y$ in the table**. Compute it.

---

**[Hard] The average rate of change of a linear function $f$ between $x=2$ and $x=5$ is 3. If $f(2) = 8$, find $f(7)$.**

For linear functions, rate of change = slope everywhere. $m = 3$. $f(x) = 3x + b$; $8 = 3(2) + b$ → $b = 2$. $f(7) = 3(7) + 2 = 23$.

❌ **Trap:** Thinking rate of change depends on interval  -  **Linear functions have constant rate**.

---

**[Very Hard] A plant is 12 cm tall at day 3 and 27 cm tall at day 8. Assuming constant (linear) growth, how tall was it at day 0?**

$m = \frac{27 - 12}{8 - 3} = \frac{15}{5} = 3$ cm per day. $h(3) = 12$ → $12 = 3(3) + b$ → $b = 3$. So $h(0) = 3$ cm.

❌ **Trap:** Using day 3's height (12 cm) as the starting height  -  the intercept is the height at day 0, which must be computed by going back 3 days at 3 cm/day: $12 - 9 = 3$.

---

### B1.2.3 Point-Slope and Writing Equations

| Given | Use |
|---|---|
| Slope $m$, $y$-int $b$ | $y = mx + b$ |
| Slope $m$, point $(x_1,y_1)$ | $y - y_1 = m(x - x_1)$ |
| Two points | Find $m$, then point-slope |

**Step-by-step method:**
1. Get the slope: from the problem, or from two points via $\frac{y_2 - y_1}{x_2 - x_1}$.
2. Plug the slope and one point into $y - y_1 = m(x - x_1)$.
3. Simplify to $y = mx + b$ if needed.
4. Verify with the other point (if you had two).

**[Easy] Write the equation of the line with slope 5 through $(2, 3)$.**

$y - 3 = 5(x - 2)$ → $y = 5x - 10 + 3$ → $y = 5x - 7$

✅ **Check:** $5(2) - 7 = 3$. ✔

---

**[Medium] Line with slope $-2$ through $(3, 8)$.**

$y - 8 = -2(x - 3)$ → $y = -2x + 14$

❌ **Trap:** $y = -2x + 8$  -  **Plugging $b$ as the $y$-value of any point**. $y$-intercept is at $x = 0$.

---

**[Hard] Line through $(2, -3)$ and $(-4, 9)$.**

$m = \frac{9-(-3)}{-4-2} = \frac{12}{-6} = -2$. Using $(2,-3)$: $y+3 = -2(x-2)$ → $y = -2x + 1$.

✅ **Check:** $(-4,9)$: $-2(-4) + 1 = 9$. ✔

---

**[Medium] Equation of line with $x$-int 4 and $y$-int $-2$?**

Points: $(4,0)$ and $(0,-2)$. $m = \frac{-2-0}{0-4} = \frac{1}{2}$, $b = -2$. $y = \frac{1}{2}x - 2$.

❌ **Trap:** $y = \frac{1}{2}x + 2$  -  **Sign error on $y$-intercept**.

---

**[Very Hard] A line passes through $(3, 7)$ and $(3, -2)$. What kind of line is it, and what is its equation?**

The $x$-values are equal, so it is a **vertical line**: $x = 3$. Slope is undefined (division by zero).

❌ **Trap:** Trying to compute $m = \frac{-2 - 7}{3 - 3} = \frac{-9}{0}$ and calling it 0  -  vertical lines have **undefined** slope, not zero slope. Zero slope is horizontal ($y = k$).

---

### B1.2.4 Interpreting Slope and Intercept in Context

**Definition in simplest terms:** In a context, the **slope** is the rate - how much the output changes per 1 unit of input. The **intercept** is the starting value - the output when the input is 0. A **negative slope** means the quantity is decreasing.

**[Medium] $C = 0.35m + 45$ models car rental cost for $m$ miles. Interpret.**

$0.35$: cost per mile. $45$: flat fee (cost at 0 miles).

❌ **Trap:** Swapping them  -  **Slope is a rate; intercept is a fixed amount**.

---

**[Medium] $V = 25000 - 3000t$ models machine value after $t$ years. Interpret.**

$-3000$: annual depreciation. $25000$: initial value.

❌ **Trap:** "The machine loses $3000$ total"  -  **Annual vs. total depreciation confusion**.

---

**[Hard] Balloon height $h(t) = 300 - 4.9t^2$. Is this linear?**

No  -  quadratic. The SAT may embed a non-linear equation in a "linear" context to test recognition.

❌ **Trap:** Calling it linear because it "goes down"  -  linear requires the input to appear to the **first power only**. The $t^2$ term makes it quadratic.

---

**[Very Hard] A plane descends from 2000 m at 120 m per minute: $h(t) = 2000 - 120t$. Interpret the constants and find when it lands.**

- 2000 = altitude, in meters, at $t = 0$.
- $-120$ = descent rate, 120 meters per minute.
- Landing: $2000 - 120t = 0$ → $t = \frac{2000}{120} = 16\frac{2}{3}$ minutes.

❌ **Trap:** Answering with $t$ when asked for something else, or misreading $-120$ as "loses 120 m total"  -  it is the rate **per minute**.

---

### B1.2.5 Connected Representations (Table, Equation, Graph)

**Definition in simplest terms:** The same linear function can be shown as a table of $(x, f(x))$ pairs, an equation $f(x) = mx + b$, or a graph (a straight line). The SAT asks you to move between these: table → equation, graph → equation, equation → graph, and given conditions → equation.

**Step-by-step method:**
1. Find two points (from the table, the graph, or given conditions).
2. Compute slope $m = \frac{\Delta y}{\Delta x}$.
3. Find $b$ by plugging one point into $y = mx + b$.
4. Check against a third point / the graph's intercepts.

**[Easy] The graph of $f$ has $y$-intercept 3 and slope 2. Which equation matches?**

$f(x) = 2x + 3$.

❌ **Trap:** Writing $f(x) = 3x + 2$  -  slope and intercept are swapped. Slope is the multiplier of $x$; intercept is the standalone constant.

---

**[Medium] Which function matches the table?**

| $x$ | 0 | 2 | 4 |
|---|---|---|---|
| $f(x)$ | -3 | 5 | 13 |

$m = \frac{5-(-3)}{2-0} = 4$. $f(0) = -3$ → $b = -3$. $f(x) = 4x - 3$.

❌ **Trap:** $m = 2$ by counting $x\to y$ as 1-step ratio  -  **$x$ changed by 2, $y$ by 8, so $m = 8/2 = 4$**.

---

**[Hard] Graph passes through $(0,4)$ and $(3,10)$. Define $f$.**

$m = \frac{10-4}{3-0} = 2$, $b = 4$. $f(x) = 2x + 4$.

❌ **Trap:** $m = 6$  -  **Using run (3) as slope instead of rise/run**.

---

**[Hard] Which graph represents $f(-2) = -1$ and $f(4) = 5$?**

$m = \frac{5-(-1)}{4-(-2)} = 1$; $f(x) = x + b$; $5 = 4 + b$ → $b = 1$. Line through $(0,1)$ with slope 1.

❌ **Trap:** Picking a graph with correct points but wrong $y$-intercept  -  **$y$-intercept must be 1**.

---

**[Very Hard] A line passes through $(0, -2)$ and $(3, 4)$. Find $f(6)$.**

$m = \frac{4 - (-2)}{3 - 0} = 2$, $b = -2$. $f(x) = 2x - 2$. $f(6) = 2(6) - 2 = 10$.

⚡ **Desmos tip:** Enter the two points as a table (or just type `(0,-2)` and `(3,4)`), then type `y1 ~ mx1 + b`. Desmos fits the line and shows $m = 2$, $b = -2$. Then type `f(6)` if you defined $f(x) = 2x - 2$.

---

### B1.2.6 Writing a Rule from Two Input-Output Pairs or One Pair + Rate

**What they test (official):** "write rule given two input-output pairs or one pair + rate of change." This is a frequent SAT format.

**Step-by-step method:**
1. **Two pairs:** slope $m = \frac{y_2 - y_1}{x_2 - x_1}$, then plug one pair into $y = mx + b$ to find $b$.
2. **One pair + rate:** the rate IS the slope. Plug the pair into $y = mx + b$ to find $b$.
3. Write $f(x) = mx + b$ and answer what was asked (often evaluate at a new input).

**[Easy] $f(1) = 6$ and the rate of change is 2. Write $f(x)$.**

$m = 2$: $6 = 2(1) + b$ → $b = 4$. $f(x) = 2x + 4$.

---

**[Medium] $f(2) = 10$ and $f(5) = 22$. Write $f(x)$.**

$m = \frac{22 - 10}{5 - 2} = 4$. $10 = 4(2) + b$ → $b = 2$. $f(x) = 4x + 2$.

✅ **Check:** $f(5) = 4(5) + 2 = 22$. ✔

---

**[Hard] A taxi charges a flat fee plus \$3.50 per mile. A 10-mile trip costs \$42.50. Write the cost function $f(m)$ and find the flat fee.**

$f(m) = 3.5m + b$; $42.5 = 3.5(10) + b$ → $b = 7.5$. So $f(m) = 3.5m + 7.5$; the flat fee is \$7.50.

❌ **Trap:** Using the flat fee as the slope or treating \$42.50 as the fee  -  the per-mile rate is given; the 10-mile cost lets you solve for the **intercept**.

---

**[Very Hard] $f(3) = 14$ and $f(7) = 26$. Find $f(12)$.**

$m = \frac{26 - 14}{7 - 3} = 3$. $14 = 3(3) + b$ → $b = 5$. $f(x) = 3x + 5$. $f(12) = 3(12) + 5 = 41$.

❌ **Trap:** Finding the rule but answering with $m$ or $b$  -  re-read what the question asks for. Here it wants $f(12)$, not the function itself.

⚡ **Desmos tip:** This whole class of questions is a 20-second Desmos job: enter the two points, fit `y1 ~ mx1 + b`, read $m$ and $b$, evaluate.

---

### B1.2.7 Linear Models in Context

**Definition in simplest terms:** A linear model uses $f(x) = mx + b$ to describe a real situation: $b$ = starting amount, $m$ = change per unit of $x$.

**Step-by-step method:** Identify the starting value ($b$) and the rate ($m$) from the story, build $f(x)$, then evaluate or solve.

**[Easy] A pool starts with 1000 gallons and fills at 25 gallons per minute. Write $P(t)$ and find the amount after 10 minutes.**

$P(t) = 25t + 1000$. $P(10) = 25(10) + 1000 = 1250$ gallons.

---

**[Medium] Bacteria: 500 cells, grows 120/hr. Population after $t$ hours?**

$P(t) = 120t + 500$. $P(8) = 120(8) + 500 = 1460$.

---

**[Hard] Temperature $T = 85 - 4m$ (degrees Celsius after $m$ minutes). When does $T = 25$?**

$25 = 85 - 4m$ → $m = 15$ minutes

❌ **Trap:** Solving $85 - 4m = 0$  -  **Wrong target. Question asks $T=25$, not $T=0$**.

---

**[Very Hard] Population $P(t) = 2000 + 150t$, $t$ = years since 2020. When does it reach 5000?**

$5000 = 2000 + 150t$ → $t = 20$ → Year: $2020 + 20 = 2040$

❌ **Trap:** Answering $t = 20$ when question asks for the year  -  **Always re-read what's being asked**.

---

## B1.3 Linear Equations in Two Variables

**What they test:** $Ax + By = C$, converting between forms, parallel/perpendicular lines, interpreting intercepts and coefficients in context, writing equations from given information (two points, point + slope, point + parallel/perpendicular line).

### B1.3.1 Forms of Linear Equations

**Definition in simplest terms:** A linear equation in two variables has infinitely many solution pairs $(x, y)$ whose graph is a straight line. It can be written in several equivalent forms; the SAT expects you to move fluently between them.

| Form | Equation | Key Use |
|---|---|---|
| Slope-intercept | $y = mx + b$ | Read slope and $y$-int directly |
| Point-slope | $y - y_1 = m(x - x_1)$ | From a point and slope |
| Standard | $Ax + By = C$ | Intercepts, solving systems, context constraints |
| Intercept | $\frac{x}{a} + \frac{y}{b} = 1$ | Read $x$- and $y$-intercepts directly |

**Standard → slope-intercept:** $y = -\frac{A}{B}x + \frac{C}{B}$

**Step-by-step method (convert standard → slope-intercept):**
1. Subtract $Ax$ from both sides: $By = -Ax + C$.
2. Divide every term by $B$: $y = -\frac{A}{B}x + \frac{C}{B}$.
3. Read off $m = -\frac{A}{B}$ and $b = \frac{C}{B}$.

**[Easy] Convert $3x + 4y = 12$ to $y = mx + b$.**

$4y = -3x + 12$ → $y = -\frac{3}{4}x + 3$

❌ **Trap:** $y = 3x + 12$  -  **Dividing only the $x$ term by 4**. Every term must be divided.

---

**[Medium] Line $2x + 3y = 6$. Find slope and both intercepts.**

$m = -\frac{A}{B} = -\frac{2}{3}$. $y$-int ($x=0$): $3y=6$ → $y=2$. $x$-int ($y=0$): $2x=6$ → $x=3$.

✅ **Check:** Intercept form $\frac{x}{3} + \frac{y}{2} = 1$ confirms $(3,0)$ and $(0,2)$.

---

**[Hard] Convert $y = \frac{2}{3}x - 4$ to standard form with integer coefficients.**

Multiply by 3: $3y = 2x - 12$ → rearrange: $2x - 3y = 12$ (equivalently $-2x + 3y = -12$).

❌ **Trap:** Writing $2x - 3y = -12$ with the wrong sign  -  bring terms across correctly: $2x - 12 = 3y$ → $2x - 3y = 12$.

---

**[Very Hard] A line has $y$-intercept 5 and $x$-intercept 10. Write it in all four forms.**

Points: $(0, 5)$ and $(10, 0)$.

- **Intercept form:** $\frac{x}{10} + \frac{y}{5} = 1$
- **Standard form:** multiply by 10: $x + 2y = 10$
- **Slope-intercept:** $m = \frac{0 - 5}{10 - 0} = -\frac{1}{2}$, so $y = -\frac{1}{2}x + 5$
- **Point-slope:** $y - 5 = -\frac{1}{2}(x - 0)$

✅ **Check:** All four describe the same line: $x$-int 10, $y$-int 5. ✔

---

### B1.3.2 Parallel and Perpendicular Lines

**Definition in simplest terms:** Parallel lines have the **same slope** and never meet. Perpendicular lines meet at a right angle; their slopes are **negative reciprocals** ($m_1 \cdot m_2 = -1$): flip the fraction and change the sign.

| Slope | Perpendicular |
|---|---|
| $\frac{2}{3}$ | $-\frac{3}{2}$ |
| $-4 = -\frac{4}{1}$ | $\frac{1}{4}$ |
| $0$ (horizontal) | undefined (vertical) |

**Step-by-step method:**
1. Get the slope of the given line (convert to $y = mx + b$ if needed).
2. Parallel: use the same $m$. Perpendicular: use $m_\perp = -\frac{1}{m}$ (flip fraction, flip sign).
3. Write the new line through the given point with point-slope form, then simplify.

**[Easy] A line is parallel to $y = 4x - 1$. What is its slope? What slope would be perpendicular?**

Parallel: $4$. Perpendicular: $-\frac{1}{4}$.

❌ **Trap:** Perpendicular slope $-4$  -  must flip **and** change sign: $4 \to -\frac{1}{4}$.

---

**[Medium] Line $l$: $2x - 3y = 6$. Slope of parallel? Perpendicular?**

$y = \frac{2}{3}x - 2$. Parallel: $\frac{2}{3}$. Perpendicular: $-\frac{3}{2}$.

❌ **Trap:** $-\frac{2}{3}$ for perpendicular  -  **Flipping sign without reciprocating**.

---

**[Medium] Perpendicular to $y = \frac{1}{2}x - 3$?**

Perpendicular slope = $-2$. Answer: $y = -2x + 5$.

❌ **Trap:** $-\frac{1}{2}$  -  **Sign flip without reciprocal** (or reciprocal without flip).

---

**[Hard] Line through $(1,5)$ perpendicular to $y = -\frac{3}{4}x + 2$.**

Perpendicular slope: $\frac{4}{3}$. $y - 5 = \frac{4}{3}(x-1)$ → $y = \frac{4}{3}x + \frac{11}{3}$

❌ **Trap:** Using $-\frac{4}{3}$ (sign flip only) or $-\frac{3}{4}$ (parallel)  -  **Wrong slope relationship**.

---

**[Hard] For what $k$ is $kx + 2y = 8$ perpendicular to $y = \frac{1}{3}x + 4$?**

$m_1 = -\frac{k}{2}$, $m_2 = \frac{1}{3}$. Perpendicular: $(-\frac{k}{2})(\frac{1}{3}) = -1$ → $k = 6$

❌ **Trap:** Setting $-\frac{k}{2} = \frac{1}{3}$  -  **Parallel condition. Perpendicular requires product $= -1$**.

---

**[Very Hard] Line $l$ is perpendicular to $3x + 6y = 12$ and passes through $(2, 4)$. Write $l$'s equation.**

$3x + 6y = 12$ → $y = -\frac{1}{2}x + 2$, so $m = -\frac{1}{2}$. Perpendicular slope: $2$. Through $(2,4)$: $y - 4 = 2(x - 2)$ → $y = 2x$.

✅ **Check:** Slope of $y = 2x$ is 2; $2 \cdot (-\frac{1}{2}) = -1$. ✔ Passes through $(2,4)$: $2(2) = 4$. ✔

---

### B1.3.3 Standard Form $Ax + By = C$: What the Coefficients Mean in Context

**Definition in simplest terms:** In a context, $Ax + By = C$ usually models a **total or limit**: $x$ and $y$ are counts of two categories, $A$ and $B$ are the per-unit amounts each category contributes, and $C$ is the grand total. Example: $4x + 6y = 120$ could mean $x$ adult tickets at \$4 each plus $y$ child tickets at \$6 each, totaling \$120 in revenue.

- $A$ = contribution of **one** unit of $x$ (its per-unit rate)
- $B$ = contribution of **one** unit of $y$ (its per-unit rate)
- $C$ = the total, budget, or limit
- Slope $-\frac{A}{B}$ = the **trade-off rate**: how much $x$ must drop for each extra unit of $y$ (keeping the total fixed)

**Step-by-step method:**
1. Identify what $x$ and $y$ count (units, items, hours).
2. Match $A$ to the per-unit value of $x$, $B$ to the per-unit value of $y$, $C$ to the total.
3. To interpret the slope: for each additional unit of $y$, you can afford $\frac{A}{B}$ fewer units of $x$.
4. Intercepts: $x$-int $= \frac{C}{A}$ (all of the budget on $x$ alone); $y$-int $= \frac{C}{B}$.

**[Easy] The equation $4x + 6y = 120$ models revenue from $x$ adult tickets (\$4 each) and $y$ child tickets (\$6 each). Interpret 4, 6, and 120.**

- 4 = revenue, in dollars, from each adult ticket.
- 6 = revenue, in dollars, from each child ticket.
- 120 = total revenue, in dollars.

❌ **Trap:** Calling 120 "the price of a ticket"  -  $C$ is the **total**, not a per-unit amount.

---

**[Medium] A gardener spends a \$60 budget on $x$ rose bushes (\$2 each) and $y$ tulip bulbs (\$3 each): $2x + 3y = 60$. Interpret the coefficients, and find how many tulip bulbs can be bought if 21 roses are bought.**

- 2 = cost per rose, 3 = cost per tulip, 60 = total budget in dollars.
- $2(21) + 3y = 60$ → $42 + 3y = 60$ → $y = 6$ tulips.

❌ **Trap:** Writing $2x + 3y = 60$ but then plugging roses into $y$  -  match each variable to its own coefficient.

---

**[Hard] A concession stand sells $x$ hot dogs (\$3 each) and $y$ sodas (\$2 each), making \$180 total: $3x + 2y = 180$. If 40 sodas were sold, how many hot dogs?**

$3x + 2(40) = 180$ → $3x = 100$ → $x = 33\frac{1}{3}$. Since hot dogs come whole, the given numbers would be adjusted on a real test; the algebra gives $x = \frac{100}{3}$.

❌ **Trap:** Subtracting $2y$ but forgetting it is $2(40) = 80$, not 40  -  apply the coefficient to the given count.

---

**[Very Hard] The equation $3x + 2y = 24$ models a budget: $x$ = packs of pens (\$3), $y$ = notebooks (\$2). What does the slope $-\frac{3}{2}$ mean in context?**

For each additional notebook bought, $\frac{3}{2} = 1.5$ fewer packs of pens can be bought (to stay on budget). Equivalently, every 2 notebooks "cost" 3 packs of pens.

❌ **Trap:** Saying the slope is "the price of a notebook"  -  the slope is a **trade-off ratio between the two items**, not a single price. The prices are $A = 3$ and $B = 2$.

---

### B1.3.4 Intercepts from Standard Form

**Definition in simplest terms:** The $x$-intercept is where the line crosses the $x$-axis ($y = 0$); the $y$-intercept is where it crosses the $y$-axis ($x = 0$). From $Ax + By = C$: set the other variable to 0.

$x$-int $= \frac{C}{A}$ (set $y=0$), $y$-int $= \frac{C}{B}$ (set $x=0$).

**[Easy] $5x - 2y = 20$: find both intercepts.**

$x$-int: $5x = 20$ → $x = 4$. $y$-int: $-2y = 20$ → $y = -10$.

❌ **Trap:** $y = 10$  -  **Sign error from $-2y$**.

---

**[Medium] Line has $x$-int $-3$, $y$-int $6$. Write in standard form.**

$\frac{x}{-3} + \frac{y}{6} = 1$ → multiply by 6: $-2x + y = 6$ → $2x - y = -6$

✅ **Check:** $y=0$ → $2x = -6$ → $x=-3$. $x=0$ → $-y = -6$ → $y=6$. ✔

---

**[Hard] A line has $x$-intercept 5 and $y$-intercept $-4$. Write it in standard form.**

$\frac{x}{5} + \frac{y}{-4} = 1$ → multiply by 20: $4x - 5y = 20$.

✅ **Check:** $y=0$ → $x = 5$. $x=0$ → $-5y = 20$ → $y = -4$. ✔

❌ **Trap:** Writing $4x + 5y = 20$  -  the negative $y$-intercept forces the minus sign on the $y$ term.

---

**[Very Hard] The line $2x + 3y = k$ has $x$-intercept $-6$. Find $k$ and the $y$-intercept.**

$x$-int: $y = 0$ → $2(-6) = k$ → $k = -12$. Then $y$-int: $x = 0$ → $3y = -12$ → $y = -4$.

⚡ **Desmos tip:** Type `2x + 3y = k` with a slider for $k$; drag until the line crosses the $x$-axis at $-6$. Desmos shows the intercepts as clickable points.

---

### B1.3.5 Graphs and Solutions in Context

**Definition in simplest terms:** The graph of a two-variable equation shows **all** pairs $(x, y)$ that satisfy it. Intercepts are the "only one category" extremes; in context they answer "what if we bought none of the other item?"

**[Easy] $x + 2y = 10$ models $x$ apples and $y$ oranges in a bag of 10 fruits (weighted oddly). What does the $y$-intercept $(0, 5)$ mean?**

If no apples are in the bag, there are 5 oranges.

---

**[Medium] $4x + 6y = 120$: adult (\$4) and child (\$6) tickets for \$120 revenue. What does $x$-intercept mean?**

Set $y=0$: $4x = 120$ → $x = 30$. If no child tickets sold, 30 adult tickets generate \$120.

---

**[Hard] $800x + 1200y = 240000$: two programs. What does $y$-intercept mean?**

Set $x=0$: $1200y = 240000$ → $y = 200$. Program B students if no money goes to Program A.

❌ **Trap:** "The total budget"  -  **$C$ is the budget; $C/B$ is a variable value when $x=0$**.

---

**[Very Hard] 120m of fencing for a rectangular pen, one side is a river (no fencing). Model area $A$ as function of width $w$.**

$w$ = width (perpendicular to river), $l$ = length (parallel). $2w + l = 120$ → $l = 120 - 2w$. $A = w(120-2w) = 120w - 2w^2$ (quadratic from linear constraint).

❌ **Trap:** $l = 120 - w$  -  **Only three sides need fencing, not four**.

---

### B1.3.6 Writing Equations from Given Information

**What they test (official):** "write equation given two points, one point + slope, or one point + parallel/perpendicular line."

**Step-by-step method:**
1. **Two points:** slope $m = \frac{y_2 - y_1}{x_2 - x_1}$, then point-slope with either point.
2. **Point + slope:** straight to point-slope form.
3. **Point + parallel line:** slope = the given line's slope.
4. **Point + perpendicular line:** slope = negative reciprocal of the given line's slope.
5. Simplify to $y = mx + b$ if the answer choices are in that form.

**[Easy] Write the line with slope 2 through $(1, 5)$.**

$y - 5 = 2(x - 1)$ → $y = 2x + 3$.

✅ **Check:** $2(1) + 3 = 5$. ✔

---

**[Medium] Write the line through $(2, 1)$ and $(5, 7)$.**

$m = \frac{7 - 1}{5 - 2} = 2$. $y - 1 = 2(x - 2)$ → $y = 2x - 3$.

✅ **Check:** $2(5) - 3 = 7$. ✔

---

**[Hard] Write the line through $(-1, 4)$ parallel to $y = 3x - 2$.**

Parallel $\Rightarrow$ slope 3. $y - 4 = 3(x + 1)$ → $y = 3x + 7$.

❌ **Trap:** Using slope $-3$ (perpendicular by accident) or using the given line's intercept $-2$  -  the new line has its own intercept, found by plugging in the point.

---

**[Very Hard] Write the line through $(3, -2)$ perpendicular to $2x + y = 5$.**

$2x + y = 5$ → $y = -2x + 5$, slope $-2$. Perpendicular slope: $\frac{1}{2}$. $y + 2 = \frac{1}{2}(x - 3)$ → $y = \frac{1}{2}x - \frac{7}{2}$.

✅ **Check:** $(-2)(\frac{1}{2}) = -1$. ✔ And $\frac{1}{2}(3) - \frac{7}{2} = \frac{3 - 7}{2} = -2$. ✔

---

## B1.4 Systems of Two Linear Equations

> **Cross-domain:** Systems involving non-linear equations (quadratic-linear, exponential-linear) are covered in B2 (Advanced Math). See B2 §2.8–§2.9 for polynomial and exponential systems.

**What they test:** Substitution, elimination, Desmos intersection method, determining solution count via slopes, modeling real-world constraints, connecting algebraic and graph representations.

### B1.4.1 Solving Methods

| Method | When to Use | How |
|---|---|---|
| Substitution | One variable isolated or easy to isolate | Replace that variable in the other eq |
| Elimination | Same coefficient (or easy to match) on one variable | Add/subtract to cancel that variable |
| Desmos | Any system (especially messy numbers) | Graph both, click intersection |

**Step-by-step method (substitution):**
1. Solve one equation for one variable (e.g., $x = y + 3$).
2. Substitute that expression into the **other** equation.
3. Solve the resulting one-variable equation.
4. Plug back in to find the other variable.

**Step-by-step method (elimination):**
1. Arrange both equations as $Ax + By = C$.
2. Multiply one or both equations so a variable has **matching (or opposite) coefficients**.
3. Add (opposite signs) or subtract (same signs) to cancel that variable.
4. Solve, then back-substitute.

**Step-by-step method (graphing/Desmos):**
1. Graph both lines.
2. The intersection point $(x, y)$ is the solution.
3. Parallel lines → no solution; identical lines → infinite.

#### Substitution

**[Easy] $y = 3x - 4$ and $2x + y = 11$.**

$2x + (3x - 4) = 11$ → $5x = 15$ → $x = 3$, $y = 5$

❌ **Trap:** $2x + 3x - 4 = 11$ → $x - 4 = 11$  -  **Combining like terms incorrectly**.

---

**[Medium] $3x + 2y = 14$ and $x - y = 3$.**

$x = y+3$ → $3(y+3) + 2y = 14$ → $y = 1$, $x = 4$

---

#### Elimination

**[Easy] $x + y = 9$ and $x - y = 1$.**

Add: $2x = 10$ → $x = 5$, $y = 4$.

✅ **Check:** $5 + 4 = 9$; $5 - 4 = 1$. ✔

---

**[Medium] $2x + 3y = 7$ and $2x + 5y = 9$.**

$(2x+5y) - (2x+3y) = 9 - 7$ → $2y = 2$ → $y = 1$, $x = 2$

❌ **Trap:** Correct subtraction on left but $9 + 7 = 16$ on right  -  **Inconsistent operation**.

---

**[Hard] $3x - 4y = 10$ and $5x + 2y = 8$.**

Multiply second by 2: $10x + 4y = 16$. Add: $13x = 26$ → $x = 2$, $y = -1$.

❌ **Trap:** $10x + 2y = 8$  -  **Partial multiplication** (only multiplied $x$ term by 2).

---

**[Hard] $2x + 3y = 12$ and $5x - 2y = 11$.**

First ×2: $4x + 6y = 24$. Second ×3: $15x - 6y = 33$. Add: $19x = 57$ → $x = 3$, $y = 2$.

❌ **Trap:** $15x - 2y = 33$  -  **Partial scaling** (only multiplied $x$ term by 3).

---

**[Very Hard] $3x + 4y = 18$ and $2x - 3y = -5$.**

First ×3: $9x + 12y = 54$. Second ×4: $8x - 12y = -20$. Add: $17x = 34$ → $x = 2$. Then $3(2) + 4y = 18$ → $y = 3$.

✅ **Check:** $2(2) - 3(3) = 4 - 9 = -5$. ✔

❌ **Trap:** Choosing multipliers that create matching coefficients but then subtracting when you should add (or vice versa)  -  here $12y$ and $-12y$ **add** to cancel.

---

#### Desmos

For any system, type both equations into Desmos. The intersection point is the solution.

**[Hard] $4.7x + 2.3y = 15.1$ and $1.8x - 3.2y = 4.6$.**

Intersection $\approx$ $(3.07, 0.29)$. 15 seconds in Desmos vs. 2-3 minutes algebraically.

⚡ **Desmos tip:** Type both equations exactly as written (standard form is fine - Desmos handles it). Click the intersection point to read $(x, y)$.

---

**[Medium] $2x + 3y = 10$ and $x - y = 5$. Find $x + y$.**

$x = y+5$ → $2(y+5) + 3y = 10$ → $y = 0$, $x = 5$. $x+y = 5$.

⚡ The test often asks for $x+y$ or $x-y$, not individual values. Always re-read.

---

### B1.4.2 Number of Solutions

**Definition in simplest terms:** Two lines can relate three ways: cross at one point (1 solution), never meet (0 solutions - parallel), or be the same line (infinite solutions - coincident).

| Slopes | Intercepts | Solutions |
|---|---|---|
| $m_1 \neq m_2$ | Any | Exactly 1 |
| $m_1 = m_2$ | $b_1 \neq b_2$ | 0 (parallel) |
| $m_1 = m_2$ | $b_1 = b_2$ | Infinite (coincident) |

Standard form: $\frac{A_1}{A_2} = \frac{B_1}{B_2} \neq \frac{C_1}{C_2}$ → 0. All three equal → infinite.

**Step-by-step method:**
1. Put both equations in slope-intercept form (or compare standard-form ratios).
2. Slopes different → 1 solution. Stop.
3. Slopes equal: compare intercepts. Different → 0. Same → infinite.
4. Elimination shortcut: a false statement like $0 = 7$ means no solution; an identity like $0 = 0$ means infinite.

**[Easy] How many solutions does $\begin{cases} y = 2x + 1 \\ y = 2x - 3 \end{cases}$ have? And $\begin{cases} y = 2x + 1 \\ y = 2x + 1 \end{cases}$?**

First system: same slope (2), different intercepts (1 vs $-3$) → **no solution** (parallel lines). Second system: identical equations → **infinite solutions**.

❌ **Trap:** Answering "no solution" for both  -  identical lines share **every** point, which is infinite solutions, not zero.

---

**[Medium] $3x + 6y = 12$ and $x + 2y = 4$: how many solutions?**

First ÷3: $x + 2y = 4$. Identical to second → infinite.

❌ **Trap:** Saying "no solution" because right sides differ at a glance  -  **Must check proportionality**.

---

**[Hard] For what $k$ does $4x + ky = 8$ and $2x - 3y = 5$ have no solution?**

Eq1: $y = -\frac{4}{k}x + \frac{8}{k}$ ($k \neq 0$). Eq2: $y = \frac{2}{3}x - \frac{5}{3}$.

Slopes equal: $-\frac{4}{k} = \frac{2}{3}$ → $k = -6$. Intercepts: $\frac{8}{-6} = -\frac{4}{3} \neq -\frac{5}{3}$. Parallel → $k = -6$.

❌ **Trap:** $k = 6$  -  **Sign error** in $-\frac{4}{k} = \frac{2}{3}$.

---

**[Hard] For what $k$ does $2x + 3y = 6$ and $4x + 6y = k$ have infinite solutions?**

Proportional: $\frac{2}{4} = \frac{3}{6} = \frac{6}{k}$ → $\frac{1}{2} = \frac{6}{k}$ → $k = 12$

❌ **Trap:** $k = 6$  -  **Partial check. Must include constant ratio: $6/k = 1/2$**.

---

**[Very Hard] $ax + by = 4$ and $2x + 3y = 8$ have infinite solutions. Find $a + b$.**

$\frac{a}{2} = \frac{b}{3} = \frac{4}{8} = \frac{1}{2}$ → $a = 1$, $b = 1.5$ → $a + b = 2.5$

❌ **Trap:** Setting $a/2 = 4/8$ but forgetting $b/3$  -  **Partial proportionality check**. All three ratios must equal.

---

**[Very Hard] Which equation, paired with $y = 3x - 2$, gives a system with infinitely many solutions?**

A) $y = 3x + 2$  B) $2y = 6x - 4$  C) $y = -3x - 2$  D) $3y = 9x + 6$

**B** is correct: $2y = 6x - 4$ divides to $y = 3x - 2$, the same line. Check the others: A and C have different slopes (one solution); D gives $y = 3x + 2$ (parallel, no solution).

❌ **Trap:** Picking D because "it also has a 3x"  -  you must simplify each candidate fully before comparing. D is actually the **no-solution** trap.

---

### B1.4.3 Word Problems with Systems

**Definition in simplest terms:** Real-world constraints give two equations in two unknowns. The classic structure: one equation for **counts** (items, hours, people) and one for **totals** (cost, revenue, volume).

**Step-by-step method:**
1. Define two variables (one per unknown category).
2. Equation 1: the count/quantity relationship.
3. Equation 2: the value/amount relationship (costs, percentages, revenue).
4. Solve (substitution or elimination), then answer what was asked (often a combination like $x + y$ or a product).

**[Easy] Two numbers sum to 20 and differ by 4. Find them.**

$x + y = 20$, $x - y = 4$. Add: $2x = 24$ → $x = 12$, $y = 8$.

✅ **Check:** $12 + 8 = 20$; $12 - 8 = 4$. ✔

---

**[Medium] Sum of two numbers is 28. Twice the first minus the second is 17. Find them.**

$x + y = 28$, $2x - y = 17$. Add: $3x = 45$ → $x = 15$, $y = 13$.

❌ **Trap:** Writing $2x + y = 17$  -  **Misreading subtraction as addition**.

---

**[Hard] Baker sells loaves (\$4) and pastries (\$2). Sold 60 items, earned \$180. How many loaves?**

$L + P = 60$, $4L + 2P = 180$. First ×2: $2L + 2P = 120$. Subtract: $2L = 60$ → $L = 30$.

❌ **Trap:** $4L + 2P = 60$  -  **Confusing item count with revenue**.

---

**[Hard] Mix 12% acid with 20% acid to get 500 mL of 15%. How much of each?**

$x$ = mL of 12%, $y$ = mL of 20%. $x + y = 500$, $0.12x + 0.20y = 75$.

Multiply second by 100: $12x + 20y = 7500$. First ×12: $12x + 12y = 6000$. Subtract: $8y = 1500$ → $y = 187.5$, $x = 312.5$.

❌ **Trap:** $0.12x + 0.20y = 500$  -  **Right side = pure acid ($75$), not total volume ($500$)**.

---

**[Hard] A jar contains 30 coins, all nickels (\$0.05) and quarters (\$0.25), worth \$4.10 total. How many quarters?**

$n + q = 30$, $5n + 25q = 410$ (cents). $n = 30 - q$ → $5(30 - q) + 25q = 410$ → $150 + 20q = 410$ → $q = 13$.

❌ **Trap:** Mixing dollars and cents  -  pick one unit (cents) and stay consistent: \$4.10 = 410 cents.

---

**[Very Hard] Product A needs 2h machine + 3h labor. Product B needs 4h machine + 1h labor. Available: 80 machine hours, 60 labor hours.**

$a$ = units of A, $b$ = units of B.

Machine: $2a + 4b = 80$. Labor: $3a + b = 60$.

$b = 60 - 3a$ → $2a + 4(60-3a) = 80$ → $-10a = -160$ → $a = 16$, $b = 12$

✅ **Check:** Machine: $2(16) + 4(12) = 32 + 48 = 80$. Labor: $3(16) + 12 = 60$. ✔

---

### B1.4.4 Connecting Algebraic and Graph Representations

**Definition in simplest terms:** The solution of a system IS the intersection point of the two lines. You may be given the graph and asked to identify the system, or given the system and asked what the graph looks like, or asked to interpret the intersection in a context.

**Step-by-step method:**
1. **Graph → system:** read the intersection point; verify it satisfies candidate equations.
2. **System → graph:** convert to slope-intercept to picture the lines (crossing, parallel, coincident).
3. **Intersection in context:** the point where two models give the same output (break-even, catch-up, equal cost).

**[Easy] The lines $y = x + 1$ and $y = -x + 5$ intersect at $(2, 3)$. Verify.**

$y = 2 + 1 = 3$. ✔  $y = -2 + 5 = 3$. ✔  The point satisfies both equations.

---

**[Medium] A system's lines intersect at $(4, -1)$. Could the system be $\begin{cases} y = x - 5 \\ y = -2x + 7 \end{cases}$?**

Check $(4, -1)$: $4 - 5 = -1$. ✔  $-2(4) + 7 = -1$. ✔  Yes.

❌ **Trap:** Checking only one equation  -  a point is a solution only if it satisfies **both**.

---

**[Hard] Two lines intersect at $(3, 2)$. One line is $y = x - 1$. The other passes through $(0, 8)$. Find the second line.**

$m = \frac{8 - 2}{0 - 3} = \frac{6}{-3} = -2$. Through $(0, 8)$: $b = 8$. Second line: $y = -2x + 8$.

✅ **Check:** $-2(3) + 8 = 2$. ✔

---

**[Very Hard] Company A charges $y = 40x + 100$; Company B charges $y = 60x$ (x = hours, y = cost). Interpret the intersection and find it.**

$40x + 100 = 60x$ → $x = 5$, $y = 300$. At **5 hours** both cost **\$300** (the break-even point). For fewer than 5 hours, Company B is cheaper; for more than 5 hours, Company A is cheaper.

❌ **Trap:** Reporting only "$x = 5$" without the cost or the comparison meaning  -  the question usually wants the interpretation (which company is cheaper when), not just the number.

⚡ **Desmos tip:** Type both equations, click the intersection. Desmos shows $(5, 300)$ instantly - then interpret in context.

---

## B1.5 Linear Inequalities

**What they test:** Solving single inequalities (flip sign for negative multiplication/division), compound inequalities, graphing with solid/dashed lines and shading, systems of inequalities, and interpreting points relative to a solution region in context.

### B1.5.1 Solving Single Linear Inequalities

**Definition in simplest terms:** An inequality says one side is bigger/smaller than the other. Solving it works exactly like an equation, with **one critical extra rule: multiplying or dividing both sides by a NEGATIVE number flips the inequality sign** ($<$ becomes $>$, $\leq$ becomes $\geq$, and vice versa).

**Step-by-step method:**
1. Distribute and combine like terms (same as equations).
2. Move variable terms to one side, constants to the other.
3. Divide by the coefficient. **If that coefficient is negative, flip the sign.**
4. Graph the solution on a number line or express as an interval.

**[Easy] $2x + 5 > 13$** → $2x > 8$ → $x > 4$

❌ **Trap:** $x < 4$  -  **Flipping unnecessarily. Only flip for negative ×/÷**.

---

**[Medium] $-3x + 7 \leq 22$** → $-3x \leq 15$ → $x \geq -5$ (flip)

❌ **Trap:** $x \leq -5$  -  **Forgetting to flip when dividing by negative**.

---

**[Medium] $4 - 2x > 10$** → $-2x > 6$ → $x < -3$ (flip)

---

**[Hard] $\frac{2x - 5}{3} \leq \frac{x + 4}{2}$**

Multiply by 6: $2(2x-5) \leq 3(x+4)$ → $4x - 10 \leq 3x + 12$ → $x \leq 22$

❌ **Trap:** $2x-5 \leq x+4$ → $x \leq 9$  -  **Dropping denominators. Multiply by LCD**.

---

**[Very Hard] $-2(x - 3) + 5 \geq 3(x + 1) - 4$**

$-2x + 6 + 5 \geq 3x + 3 - 4$ → $-2x + 11 \geq 3x - 1$ → $12 \geq 5x$ → $x \leq \frac{12}{5}$ (divide by positive 5: no flip)

❌ **Trap:** Flipping at the last step because "we divided"  -  you only flip when dividing by a **negative** number. Dividing by $+5$ keeps the sign. Also check the distribution: $-2(x-3) = -2x + 6$, not $-2x - 6$.

⚡ **Desmos tip:** Type the inequality directly (`-2(x-3)+5 >= 3(x+1)-4`); Desmos shades the solution region on the number line and you can read the boundary.

---

### B1.5.2 Compound Inequalities

**Definition in simplest terms:** Two inequalities joined by **"and"** (both must hold - the solution is the **intersection**/overlap) or **"or"** (at least one holds - the solution is the **union** of both). A chained form like $-5 < 2x + 1 < 7$ is a hidden "and": $2x+1 > -5$ AND $2x+1 < 7$.

**Step-by-step method:**
1. **Chained "and" ($a < x < b$):** apply the same operation to ALL THREE parts (subtract, then divide - flip both signs if dividing by a negative).
2. **Separate "or":** solve each inequality independently, then combine with "or".
3. Graph: "and" = overlap of the two number-line regions; "or" = both regions together.

**[Easy] $-1 < x + 2 < 5$**

Subtract 2 from all parts: $-3 < x < 3$.

---

**[Medium] $-5 < 2x + 1 < 7$**

Subtract 1: $-6 < 2x < 6$. Divide: $-3 < x < 3$.

❌ **Trap:** Solving only one side ($2x+1 < 7 \to x < 3$)  -  **Both inequalities must be satisfied**.

---

**[Hard] $3x - 7 \leq 5$ or $2x + 1 > 11$**

First: $x \leq 4$. Second: $x > 5$. Solution: $x \leq 4$ or $x > 5$.

❌ **Trap:** Treating "or" as "and" → presenting $4 < x \leq 5$ (empty set).

---

**[Hard] $2 < 3x + 5 \leq 14$**

Subtract 5: $-3 < 3x \leq 9$. Divide: $-1 < x \leq 3$.

❌ **Trap:** Subtracting 5 from middle only  -  **Operation must apply to ALL three parts**.

---

**[Very Hard] Solve and graph: $4x - 3 \leq 9$ AND $2x + 1 > -5$; then solve $x - 2 > 3$ OR $2x \leq 8$.**

First ("and"): $4x \leq 12$ → $x \leq 3$; and $2x > -6$ → $x > -3$. Overlap: $-3 < x \leq 3$.

Second ("or"): $x > 5$; or $x \leq 4$. Union: $x \leq 4$ or $x > 5$ (everything except $4 < x \leq 5$).

❌ **Trap:** Writing the "or" answer as a single chained inequality like $4 < x \leq 5$  -  "or" solutions are usually **two separate rays**, not one interval.

---

### B1.5.3 Graphing Linear Inequalities

**Definition in simplest terms:** The graph of a two-variable inequality is a **half-plane**: a boundary line plus all points on one side of it. The boundary is **solid** when the inequality includes equality ($\leq$, $\geq$) and **dashed** when it does not ($<$, $>$). The shading shows the side where the inequality is true.

| Feature | Solid | Dashed |
|---|---|---|
| Used for | $\leq, \geq$ | $<, >$ |
| Boundary included | Yes | No |
| Shading | Above for $>/\geq$, below for $</\leq$ |

**Step-by-step method:**
1. Solve for $y$ (get $y > mx + b$ or similar).
2. Graph the boundary line $y = mx + b$: solid if $\leq$ or $\geq$; dashed if $<$ or $>$ (or if the boundary is vertical, shade right for $>$/$ \geq$, left for $<$/$\leq$).
3. Shade **above** for $>$ / $\geq$; **below** for $<$ / $\leq$.
4. **Test point:** pick $(0,0)$ (unless it is on the boundary). If it satisfies the inequality, shade the side containing it; otherwise shade the other side.

**Test point:** Pick $(0,0)$ unless it lies on the boundary. If it satisfies, shade that side.

**[Easy] Graph $y < x + 1$.**

Boundary $y = x + 1$ dashed (strict). Shade below. Test $(0,0)$: $0 < 1$ true → shade the side containing the origin.

---

**[Medium] Graph $y > 2x - 3$.** Dashed line, shade above. $(0,0)$: $0 > -3$ true → shade side containing origin.

---

**[Medium] Graph $3x + 2y \leq 6$.** $y \leq -\frac{3}{2}x + 3$. Solid line, shade below. $(0,0)$: $0 \leq 6$ true.

❌ **Trap:** Shading above when $y \leq$  -  **Reversing shading direction**.

---

**[Hard] Graph $x > 2$.**

Vertical dashed line at $x = 2$; shade to the right (all points with $x > 2$).

❌ **Trap:** Drawing a horizontal line  -  $x > 2$ constrains the $x$-coordinate, so the boundary is **vertical**. Test point $(3, 0)$: $3 > 2$ true, so the right side is correct.

---

**[Very Hard] Graph $y \geq -\frac{1}{2}x + 1$ and identify whether $(4, -1)$ is in the solution set.**

Solid line through $(0,1)$ with slope $-\frac{1}{2}$; shade above. Test $(4,-1)$: $-1 \geq -\frac{1}{2}(4) + 1 = -1$. True ($-1 = -1$), so $(4,-1)$ is ON the boundary and **included** (solid line).

⚡ **Desmos tip:** Type `y >= -x/2 + 1` directly. Desmos draws the solid boundary and shades above automatically; click any point to check inclusion.

---

### B1.5.4 Interpreting a Point Relative to the Solution Region

**What they test (official):** "interpret a point in the xy-plane in terms of the solution set" - given a point and an inequality (or system), decide whether the point is in the solution set, and interpret what that means in a real context (e.g., does a given order fit the budget?).

**Step-by-step method:**
1. Plug the point's coordinates into the inequality (each inequality, if there are several).
2. True → the point is **in the solution set** (in the shaded region, or on a solid boundary). False → **outside** (or on a dashed boundary = not included).
3. **Interpret in context:** "in the solution set" = the combination is **feasible** (fits the budget, meets the requirement). "Outside" = **infeasible** (exceeds the limit, falls short of the minimum).
4. Boundary check: on the line counts only for $\leq$ / $\geq$ (solid), never for $<$ / $>$ (dashed).

**[Easy] $y \geq 2x - 1$. Is $(3, 5)$ in the solution set?**

$5 \geq 2(3) - 1 = 5$. True ($5 = 5$) → yes, on the boundary, and the boundary is included because of $\geq$.

---

**[Medium] A bakery's labor constraint is $3c + b \leq 24$: $c$ cakes take 3 hours each, $b$ batches of cookies take 1 hour each, 24 hours available per day. Is making 5 cakes and 10 batches feasible? What about 4 cakes and 12 batches?**

- $(5, 10)$: $3(5) + 10 = 25 > 24$ → **No**. This order needs 25 hours, exceeding the limit - it falls outside the shaded region.
- $(4, 12)$: $3(4) + 12 = 24 \leq 24$ → **Yes**. Uses exactly the available hours - it lies on the (solid) boundary.

❌ **Trap:** Checking "24 $\leq$ 24" and calling it a failure  -  equality satisfies $\leq$, so boundary points are feasible.

---

**[Hard] A club has a \$100 budget: $x$ t-shirts at \$2 each and $y$ hoodies at \$5 each: $2x + 5y \leq 100$. Can they buy 15 t-shirts and 14 hoodies? 20 t-shirts and 13 hoodies?**

- $(15, 14)$: $2(15) + 5(14) = 30 + 70 = 100 \leq 100$ → **Yes**, exactly at budget.
- $(20, 13)$: $2(20) + 5(13) = 40 + 65 = 105 > 100$ → **No**, over budget by \$5.

❌ **Trap:** Reading the constraint backwards ($2x + 5y \geq 100$)  -  "at most \$100" means the cost must be **less than or equal to** 100.

---

**[Very Hard] A student needs to earn at least \$300/week across two jobs: Job A pays \$15/hr, Job B pays \$12/hr, and total hours are capped at 25: $15a + 12b \geq 300$ and $a + b \leq 25$. Is working 10 hours at A and 14 at B feasible? What about 8 hours at A and 14 at B?**

- $(10, 14)$: earnings $15(10) + 12(14) = 150 + 168 = 318 \geq 300$ ✓; hours $10 + 14 = 24 \leq 25$ ✓. **Feasible.**
- $(8, 14)$: earnings $120 + 168 = 288 < 300$ ✗. **Not feasible** - fails the earnings requirement even though the hours work.

❌ **Trap:** Checking only one constraint  -  a point must satisfy **every** inequality in the system. On the graph it must lie in the overlap of all shaded regions.

---

### B1.5.5 Systems of Inequalities

**Definition in simplest terms:** A system of inequalities has a solution region that is the **overlap** of each individual half-plane. Every point in the overlap satisfies all constraints at once.

**Step-by-step method:**
1. Graph each inequality (solid/dashed + shading as in B1.5.3).
2. The solution is the region where ALL shadings overlap.
3. To check a point: verify it against every inequality.
4. Real-world systems: always include $x \geq 0$, $y \geq 0$ (non-negativity) when quantities can't be negative.

**[Easy] Which region is the solution of $\begin{cases} y > 0 \\ y < 3 \end{cases}$?**

The horizontal strip strictly between $y = 0$ and $y = 3$ (both boundaries dashed - not included).

---

**[Medium] Which point satisfies both $y < 2x + 1$ and $y \geq -x + 3$?**

A) $(0,0)$: $0 < 1$ ✓, $0 \geq 3$ ✗. B) $(1,4)$: $4 < 3$ ✗. C) $(2,1)$: $1 < 5$ ✓, $1 \geq 1$ ✓. **Answer: C.**

❌ **Trap:** Checking only one inequality  -  **A point must satisfy ALL inequalities**.

---

**[Hard] Company makes two products. A needs 2h labor, B needs 3h. At most 60h/week. At least 10 total products/week.**

$a$ = units of A, $b$ = units of B.

$2a + 3b \leq 60$, $a + b \geq 10$, $a \geq 0$, $b \geq 0$

✅ **Always include non-negativity** for real-world quantities.

---

**[Hard] Scores 82 and 76 on two tests. What third score gives average $\geq 80$?**

$\frac{82 + 76 + x}{3} \geq 80$ → $158 + x \geq 240$ → $x \geq 82$

❌ **Trap:** Using $>$ instead of $\geq$  -  **"At least" means $\geq$, not $>$**.

---

**[Hard] Parking: \$5 first hour, \$3 each additional hour, max \$20/day. Inequality for hours $h$?**

Cost = $5 + 3(h-1)$ for $h \geq 1$. $5 + 3(h-1) \leq 20$ → $h \leq 6$. Solution: $1 \leq h \leq 6$.

❌ **Trap:** $3h + 5$  -  **First hour costs \$5, remaining $(h-1)$ hours cost \$3 each**.

---

**[Very Hard] Which region represents $y \leq 2x - 3$ and $y > -x + 4$?**

Graph both in Desmos:
- $y \leq 2x - 3$: solid line, shade below
- $y > -x + 4$: dashed line, shade above

Intersection: $2x - 3 = -x + 4$ → $x = \frac{7}{3}$, $y = \frac{5}{3}$. Solution is overlapping shaded region.

⚡ Type both inequalities directly with `<=` and `>`; Desmos shades automatically.

---

## B1.6 Linear Relationships in Context

**What they test:** The SAT puts ~30% of all math questions in real-world context. For Algebra this means: percent change word problems, distinguishing linear from exponential growth, interpreting constants in context ("what does the 500 represent?"), and full linear-model word problems. This section drills exactly those formats.

### B1.6.1 Percent Change Word Problems

**Definition in simplest terms:** Percent change measures how much a quantity grew or shrank relative to its original value:

$$\text{percent change} = \frac{\text{new} - \text{original}}{\text{original}} \times 100\%$$

To **apply** a $p\%$ change: new $= \text{original} \times \left(1 \pm \frac{p}{100}\right)$. To **undo** a $p\%$ change: original $= \frac{\text{new}}{1 \pm p/100}$.

**Step-by-step method:**
1. Identify the **original** amount (the base - usually the "before" amount).
2. Decide direction: increase ($+$) or decrease ($-$).
3. Apply the formula, or set up an equation and solve for the unknown (often the original).
4. Sanity check: a $20\%$ increase followed by a $20\%$ decrease does **not** return to the original (it lands at $96\%$ of it).

**[Easy] A jacket costs \$80 and is discounted 25%. What is the sale price?**

$\text{sale} = 80 \times (1 - 0.25) = 80 \times 0.75 = \$60$.

---

**[Medium] A town's population grows from 5000 to 5500. What is the percent increase?**

$\frac{5500 - 5000}{5000} \times 100\% = \frac{500}{5000} \times 100\% = 10\%$.

❌ **Trap:** Dividing by the new amount ($5500$)  -  percent change is always relative to the **original** ($5000$).

---

**[Hard] After a 20% increase, a salary is \$54,000. What was the salary before the increase?**

$1.20x = 54000$ → $x = 45000$.

❌ **Trap:** Computing $54000 \times 0.80 = 43200$  -  a 20% **decrease of the new amount** is not the same as undoing a 20% increase. Undo by **dividing** by $1.20$.

---

**[Very Hard] A store marks an item up 25%, then discounts the new price by 20% during a sale. The sale price is \$90. What was the original price?**

$x \times 1.25 \times 0.80 = 90$ → $x \times 1.00 = 90$ → $x = 90$.

⚡ **Insight:** A $25\%$ markup followed by a $20\%$ discount multiplies by $1.25 \times 0.8 = 1.00$ - the net change is **zero** (the original price returns). This is a classic "trap" answer design: many students compute a "net 5%" and get \$85.50. Watch for markup/discount pairs whose factors multiply to 1.

---

### B1.6.2 Linear Growth vs. Exponential Growth

**Definition in simplest terms:**
- **Linear growth:** the quantity changes by the **same amount** each step (add/subtract a constant). Model: $y = mx + b$.
- **Exponential growth:** the quantity changes by the **same factor** each step (multiply/divide by a constant). Model: $y = ab^x$.

| Feature | Linear | Exponential |
|---|---|---|
| Repeated change | Add the same difference | Multiply by the same factor |
| Common form | $y = mx + b$ | $y = ab^x$ |
| Table test | First differences constant | Ratios constant (nonzero outputs) |
| Wording | "Increases by 3 each year" | "Increases by 3% each year", "doubles", "triples" |

**Step-by-step method:**
1. Check the input spacing (equal steps of $x$).
2. Subtract consecutive outputs: constant → **linear**.
3. If differences vary, divide consecutive outputs: constant ratio → **exponential**.
4. Match the model: $b$ (or $a$) = starting value; slope $m$ = the difference; base $r$ = the factor.

**[Easy] A savings account earns \$50 every month. Linear or exponential? Write the model.**

Linear - same **amount** added each month. $A(t) = 50t + A_0$.

---

**[Medium] A population increases by 3% each year. Linear or exponential? Write the model.**

Exponential - each year multiplies by $1.03$. $P(t) = P_0 \cdot (1.03)^t$.

❌ **Trap:** Treating "3% per year" as linear ($P_0 + 0.03t$)  -  a percent change applies to the **current** amount each period, so it compounds. "Increases by 3" is linear; "increases by 3%" is exponential.

---

**[Hard] Classify each table (x = 0, 1, 2, 3): (a) y = 5, 8, 11, 14; (b) y = 5, 10, 20, 40.**

(a) Differences: 3, 3, 3 - constant → **linear**: $y = 3x + 5$.
(b) Ratios: $10/5 = 2$, $20/10 = 2$, $40/20 = 2$ - constant → **exponential**: $y = 5 \cdot 2^x$.

❌ **Trap:** Calling (b) linear because "it grows faster"  -  growing faster does not define exponential. Exponential requires a **constant multiplicative factor** across equal steps.

---

**[Very Hard] A car worth \$20,000 loses 15% of its value each year. Linear or exponential? Find its value after 3 years.**

Exponential (percent decrease): $V(t) = 20000(0.85)^t$. $V(3) = 20000(0.85)^3 = 20000 \times 0.614125 = \$12,282.50$.

❌ **Trap:** Computing $20000 - 3(0.15)(20000) = 11000$ (the linear version)  -  each year's loss is 15% of the **current** value, which shrinks, so the exponential answer ($12282.50$) is higher.

⚡ **Desmos tip:** Type `20000(0.85)^x` and read $y$ at $x = 3$ from the table or by evaluating.

---

### B1.6.3 Interpreting Constants in Context (Deep Dive)

**Definition in simplest terms:** Every number in a model plays a role: the **coefficient** of the variable = rate of change (per-unit amount); the **standalone constant** = starting value / fixed amount; in $y = ab^x$ the **base** $b$ = the multiplier per period (e.g., 0.9 = "retains 90% each period").

**Step-by-step method:**
1. Locate the number in the formula - is it multiplied by the variable, standing alone, or the base of a power?
2. Coefficient → "the change in (output), per (unit of input)."
3. Standalone constant → "the value of (output) when (input) is 0."
4. Base of a power → "the factor by which (output) is multiplied per (period)."
5. Always attach units.

**[Easy] $C = 0.5m + 12$: cost of a ride for $m$ miles. What does 12 represent?**

The flat fee, in dollars - the cost when 0 miles are driven.

---

**[Medium] $d(t) = 60t + 20$: distance, in miles, from home after driving $t$ hours. Interpret 60 and 20.**

- 60 = speed, in miles per hour (distance gained per hour).
- 20 = starting distance from home, in miles, at $t = 0$.

❌ **Trap:** Saying "60 is the total distance"  -  60 is the **rate**; total distance grows with $t$.

---

**[Hard] $N(t) = 3000(0.9)^t$: bacteria after $t$ hours. Interpret 3000 and 0.9.**

- 3000 = initial number of bacteria at $t = 0$.
- 0.9 = the population **retains 90% each hour** (a 10% hourly decrease).

❌ **Trap:** Calling 0.9 "the rate of decrease"  -  0.9 is the **remaining fraction**; the decrease rate is $1 - 0.9 = 0.1$, i.e., 10%.

---

**[Very Hard] A moving company charges $C(x) = 250 + 0.05x$ for a truck rented $x$ miles. (a) What does 250 mean? (b) What does 0.05 mean? (c) What is the cost for 0 miles, and what is a sensible domain for $x$?**

(a) 250 = base rental fee, in dollars (cost at 0 miles). (b) 0.05 = per-mile charge, dollars per mile. (c) $C(0) = 250$; sensible domain: $x \geq 0$ (miles driven can't be negative).

❌ **Trap:** Forgetting the domain question  -  the SAT sometimes asks for the set of reasonable input values. Money/miles/people all require non-negative inputs (and often integers).

---

### B1.6.4 Linear Model Word Problems

**Definition in simplest terms:** Build $f(x) = mx + b$ from a story, then evaluate or solve. The story usually hands you either (two data points) or (a rate + a starting value).

**Step-by-step method:**
1. Find the **rate** (slope): stated directly, or computed from two data points.
2. Find the **starting value** (intercept): stated, or solve $b = y - mx$ using one point.
3. Write $f(x) = mx + b$ with units.
4. Evaluate at the requested input, or solve $f(x) = $ target, or compare two models.

**[Easy] A candle is 30 cm tall and burns 2 cm per hour. How tall after 4 hours?**

$h(t) = 30 - 2t$. $h(4) = 30 - 8 = 22$ cm.

---

**[Medium] A tank holds 1200 L at noon and 900 L at 2 pm. Assuming linear draining, write $W(t)$ (hours after noon) and find when it empties.**

$m = \frac{900 - 1200}{2 - 0} = -150$ L/hr. $W(t) = 1200 - 150t$. Empty: $1200 - 150t = 0$ → $t = 8$ hours after noon (8 pm).

❌ **Trap:** Writing $W(t) = 1200 + 150t$  -  the water is leaving, so the slope is **negative**.

---

**[Hard] A tree was 4 ft tall when planted and 10 ft after 3 years. Assuming linear growth, how tall after 7 years?**

$m = \frac{10 - 4}{3 - 0} = 2$ ft/yr. $h(t) = 2t + 4$. $h(7) = 2(7) + 4 = 18$ ft.

❌ **Trap:** Using $h(7) = 10 + 2(4) = 18$ by accident is fine, but a common error is starting from the second point only and writing $h = 2t + 10$  -  the intercept must come from the point $(0, 4)$.

---

**[Very Hard] Plan A: \$30/month plus \$0.10 per minute. Plan B: \$10/month plus \$0.25 per minute. For what monthly usage is Plan A cheaper?**

$A(m) = 30 + 0.10m$, $B(m) = 10 + 0.25m$. Need $A < B$: $30 + 0.1m < 10 + 0.25m$ → $20 < 0.15m$ → $m > 133\frac{1}{3}$ minutes. So Plan A is cheaper for **more than** $133\frac{1}{3}$ minutes.

❌ **Trap:** Setting the plans equal and answering with that number as the "switch point" without stating the inequality direction  -  at exactly $133\frac{1}{3}$ min they tie; Plan A wins only **above** it.

⚡ **Desmos tip:** Graph $y_1 = 30 + 0.1x$ and $y_2 = 10 + 0.25x$; the intersection shows the break-even usage. Then reason about which side makes A cheaper.

---

## B1.7 Additional Algebra Topics

### B1.7.1 Absolute Value Equations

**Definition in simplest terms:** $|A|$ is the distance of $A$ from 0, so it is never negative. The equation $|A| = b$ (with $b \geq 0$) means $A$ is either $b$ or $-b$ - which is why absolute value equations usually have **two** solutions.

**Step-by-step method:**
1. Isolate the absolute value: get $|A|$ alone on one side.
2. Check the sign of the other side: negative → **no solution** immediately.
3. Split into two equations: $A = b$ and $A = -b$.
4. Solve both and check each solution in the original.

**[Easy] $|x - 5| = 3$** → $x - 5 = 3$ or $x - 5 = -3$ → $x = 8, 2$

**[Medium] $|2x + 1| = 7$** → $2x+1 = 7$ or $2x+1 = -7$ → $x = 3, -4$

❌ **Trap:** Only solving one case  -  **Absolute value equations almost always have two solutions**.

---

**[Medium] $3|x - 4| + 2 = 20$**

Isolate: $3|x-4| = 18$ → $|x-4| = 6$ → $x = 10, -2$

❌ **Trap:** $3x - 12 + 2 = 20$  -  **Distributing into the absolute value**. Isolate $|x-4|$ first.

---

**[Hard] $|x + 5| = -3$** → **No solution.** Absolute value cannot equal a negative.

❌ **Trap:** Writing $x+5 = -3$ or $x+5 = 3$  -  **Check sign before splitting**.

---

**[Hard] $|2x - 3| = |x + 4|$**

Case 1 (same signs): $2x - 3 = x+4$ → $x = 7$. Case 2 (opposite signs): $2x - 3 = -(x+4)$ → $x = -\frac{1}{3}$.

❌ **Trap:** Only solving Case 1  -  **Must also consider opposite signs**.

---

**Absolute Value Inequalities**

$|A| < b$ ($b>0$) → $-b < A < b$ (less th**and**)
$|A| > b$ ($b>0$) → $A < -b$ or $A > b$ (**great**or)

**[Medium] $|x - 3| < 5$** → $-5 < x-3 < 5$ → $-2 < x < 8$

**[Medium] $|2x + 1| \geq 9$** → $2x+1 \leq -9$ or $2x+1 \geq 9$ → $x \leq -5$ or $x \geq 4$

---

### B1.7.2 Literal Equations (Solving for a Variable)

**Definition in simplest terms:** A literal equation has several letters (like $A = lw$). Solving for one letter means isolating it using the same rules as a normal equation, treating the other letters as numbers.

**Step-by-step method:**
1. Identify the target variable.
2. Treat other variables as constants.
3. Clear denominators first (multiply through by the LCD).
4. Apply inverse operations to isolate the target.
5. If the target appears in several terms, collect them and factor it out.

**[Easy] $A = lw$ for $w$** → $w = A/l$

**[Medium] $P = 2l + 2w$ for $l$** → $l = \frac{P - 2w}{2}$ (or $\frac{P}{2} - w$)

❌ **Trap:** $l = P - 2w$  -  **Forgetting to divide by 2**.

---

**[Hard] $S = \frac{n}{2}(a + l)$ for $a$** → $2S = n(a+l)$ → $a = \frac{2S}{n} - l$

❌ **Trap:** Distributing before clearing fraction  -  adds steps and error risk. Clear denominators first.

---

**[Hard] $\frac{1}{R} = \frac{1}{r_1} + \frac{1}{r_2}$ for $r_1$**

Multiply by $R r_1 r_2$: $r_1 r_2 = R r_2 + R r_1$ → $r_1(r_2 - R) = R r_2$ → $r_1 = \frac{R r_2}{r_2 - R}$

❌ **Trap:** $r_1 = R - r_2$  -  **Treating reciprocals as simple addition**.

---

**[Very Hard] $y = \frac{2x + 3}{x - 1}$ for $x$**

$y(x-1) = 2x+3$ → $xy - y = 2x+3$ → $x(y-2) = y+3$ → $x = \frac{y+3}{y-2}$

❌ **Trap:** Forgetting to collect $x$ terms when $x$ appears on both sides  -  must factor.

---

### B1.7.3 Direct and Inverse Variation

**Definition in simplest terms:**
- **Direct variation:** $y = kx$ - doubling $x$ doubles $y$. The ratio $y/x = k$ is constant; the graph is a line through the origin.
- **Inverse variation:** $y = k/x$ (or $xy = k$) - doubling $x$ halves $y$. The product $xy = k$ is constant.

**Step-by-step method:**
1. Decide the type (direct: constant ratio; inverse: constant product; watch for powers like $d^2$).
2. Plug in the given pair to find $k$.
3. Use $k$ to answer the question.

**[Easy] $y$ varies directly with $x$. $y=12$ when $x=3$. Find $y$ when $x=7$.**

$12 = k(3)$ → $k = 4$. $y = 4(7) = 28$.

**[Medium] $y$ varies inversely with $x$. $y=6$ when $x=4$. Find $y$ when $x=8$.**

$6 \cdot 4 = k \to k = 24$. $y = \frac{24}{8} = 3$.

❌ **Trap:** $y = -kx$  -  **"Inverse" means multiplicative inverse ($1/x$), not negative**.

---

**[Medium] Spring stretch varies directly with weight. 5kg → 8cm. 12kg → ?**

$d = kw$: $8 = k(5)$ → $k = 1.6$. $d = 1.6(12) = 19.2$ cm.

---

**[Hard] Light intensity varies inversely with $d^2$. 20 units at 3m. Intensity at 6m?**

$I = \frac{k}{d^2}$: $20 = \frac{k}{9}$ → $k = 180$. $I = \frac{180}{36} = 5$ units.

❌ **Trap:** Using $I = k/d$ instead of $k/d^2$  -  **Ignoring the power**.

---

**[Hard] Does this table show direct or inverse variation?**

| $x$ | 2 | 4 | 6 | 8 |
|---|---|---|---|---|
| $y$ | 12 | 6 | 4 | 3 |

$xy = 24$ constant → inverse variation ($y = 24/x$).

❌ **Trap:** $y$ decreases as $x$ increases → assuming inverse without checking  -  **Must verify $xy$ is constant**.

---

### B1.7.4 Piecewise Linear Functions

**Definition in simplest terms:** A piecewise function uses different linear rules on different parts of the input. Evaluation means: check which condition the input satisfies, then use that piece only.

**Step-by-step method:**
1. Look at the input value.
2. Test it against each condition ($x < 3$, $x \geq 3$, ...).
3. Use the matching piece and evaluate.

**[Medium] $f(x) = \begin{cases} 2x+1, & x<3 \\ -x+10, & x \geq 3 \end{cases}$. Find $f(3)$.**

$3 \geq 3$, use second piece: $f(3) = -3 + 10 = 7$

❌ **Trap:** Using first piece because 3 is "close to 2"  -  **Check the condition, don't guess**.

---

**[Medium] $f(x) = \begin{cases} 3x-2, & x \leq 1 \\ x+4, & x > 1 \end{cases}$. Find $f(-2) + f(5)$.**

$f(-2) = 3(-2)-2 = -8$. $f(5) = 5+4 = 9$. Sum = 1.

---

**[Hard] Parking garage: \$10 first hour, \$5 each additional (or fraction), max \$30/day. Write $f(h)$.**

$f(h) = \begin{cases} 10, & 0 < h \leq 1 \\ 10 + 5(h-1), & 1 < h \leq 5 \\ 30, & h > 5 \end{cases}$

❌ **Trap:** $10 + 5h$ for second piece  -  **First hour costs \$10, not \$5**.

---

**[Hard] $f(x) = \begin{cases} 2x+3, & x \leq a \\ -x+9, & x > a \end{cases}$ continuous at $x=a$. Find $a$.**

$2a + 3 = -a + 9$ → $3a = 6$ → $a = 2$

✅ **Check:** $f(2) = 7$ from both pieces. ✔

---

## Common Mistake Catalog

### Category 1: Sign & Distribution Errors

| # | Mistake | Wrong | Correct |
|---|---|---|---|
| 1 | **Not distributing to all terms** | $3(x-4) = 3x-4$ | $3x-12$ |
| 2 | **Forgetting to flip inequality sign** | $-3x > 9 \to x > -3$ | $x < -3$ |
| 3 | **Losing negative in standard form slope** | $2x+3y=6 \to m = \frac{2}{3}$ | $m = -\frac{2}{3}$ |
| 4 | **Partial multiplication in elimination** | $3(2x+y=5) \to 6x+y=15$ | $6x+3y=15$ |
| 5 | **Distributing into absolute value** | $3|x-4| = 3x-12$ | Isolate $|x-4|$ first |

### Category 2: Conceptual Confusion

| # | Mistake | Why |
|---|---|---|
| 6 | **Identity vs. contradiction** | $0=0$ → infinite, not "no solution" |
| 7 | **Intercept vs. slope** | "$200$ in $C=5n+200$ is per-widget cost" → it's fixed cost |
| 8 | **$y$-intercept from table** | $b = \text{first } y$ in table → $b = f(0)$, compute it |
| 9 | **Direct vs. inverse variation** | "Inverse means negative" → inverse means $xy = k$ |
| 10 | **"Or" vs. "and" in compound** | $x<2$ or $x>5$ as $2<x<5$ → two separate ranges |
| 11 | **One-variable "no solution" trap** | $3(2x-5)=6x+k$ no solution → $k=-15$ (that's infinite!) → $k \neq -15$ |
| 12 | **Linear vs. exponential** | "Increases by 3% each year" written as $+0.03t$ → model is $P_0(1.03)^t$ |
| 13 | **Standard form $C$ meaning** | $C$ in $Ax+By=C$ = total/budget, not a per-unit price |
| 14 | **Percent change base** | Dividing by the new amount → always divide by the **original** |

### Category 3: Setup & Interpretation Errors

| # | Mistake | Why |
|---|---|---|
| 15 | **Wrong variable target** | Found $x$, question asks for $2x+1$ |
| 16 | **Confusing count with cost** | $4L+2P = 60$ (cost = item count) |
| 17 | **Swapping fixed and variable costs** | $C(d) = 3.50d + 2$ |
| 18 | **Forgetting non-negativity** | Real-world quantities can't be negative |
| 19 | **Misreading intercept meaning** | $y$-int = total budget (it's value at $x=0$) |
| 20 | **Point outside the region** | Checking only one inequality in a system → must satisfy ALL |

### Category 4: Calculation Errors

| # | Mistake | Wrong | Correct |
|---|---|---|---|
| 21 | **Inverted slope** | $\frac{x_2-x_1}{y_2-y_1}$ | $\frac{y_2-y_1}{x_2-x_1}$ |
| 22 | **Perpendicular: sign only** | $\frac{2}{3} \to -\frac{2}{3}$ | $\to -\frac{3}{2}$ |
| 23 | **Partial compound solving** | $-5<2x+1<7 \to x<3$ | $-3 < x < 3$ |
| 24 | **Sign error in elimination** | Add when should subtract | Subtract to cancel same-sign terms |
| 25 | **Dividing only one term** | $\frac{3x+6}{3} = x+6$ | $x+2$ |

### Category 5: Test-Day Strategy Errors

| # | Mistake | Fix |
|---|---|---|
| 26 | **Using Desmos for everything** | Decide in 10s: algebra, Desmos, or backsolving |
| 27 | **Not re-reading final quantity** | Find $x$ when question asks $x+y$ |
| 28 | **Not backsolving for multiple choice** | Plug answer choices instead of solving |
| 29 | **Forgetting Desmos for systems** | 15s in Desmos vs 2+ minutes algebra |
| 30 | **Not checking axis scaling** | Graph intercepts may be at unexpected positions |

---

## Difficulty-Progression Practice Sets

### Set 1: Linear Equations in One Variable

[Easy] $7x - 3 = 4x + 9$ → $x = 4$

[Medium] $\frac{5y}{3} - 2 = \frac{y}{2} + 3$ → Multiply by 6: $10y - 12 = 3y + 18$ → $y = \frac{30}{7}$

[Hard] For what $a$ does $2(x-3) + a = 2x + 5$ have no solution? → $2x - 6 + a = 2x + 5$ → any $a \neq 11$ gives no solution ($a = 11$ gives infinite).

[Very Hard] $3(kx+2) = 6x - 9$ has no solution. Find $k$. → $3kx + 6 = 6x - 9$ → $3k = 6$ → $k = 2$ (and $6 \neq -9$, confirmed).

---

### Set 2: Systems of Equations

[Easy] $x + y = 10$, $x - y = 2$ → $x = 6$, $y = 4$

[Medium] $3x + 2y = 16$, $2x - y = 6$ → $y = 2x - 6$ → $x = 4$, $y = 2$

[Hard] Sum of two numbers is 15, difference is 7. Find their product. → $x = 11$, $y = 4$ → product $= 44$.

[Very Hard] $kx + 3y = 6$ and $2x - y = 4$ have no solution. Find $k$. → $m_1 = -\frac{k}{3}$, $m_2 = 2$ → $-\frac{k}{3} = 2$ → $k = -6$

---

### Set 3: Linear Functions

[Easy] $f(x) = 4x - 7$, find $f(5)$. → $13$

[Medium] Line has slope $-\frac{2}{3}$ through $(9,1)$. Write equation. → $y = -\frac{2}{3}x + 7$

[Hard] Graph of $f$ passes through $(1,6)$ and $(4,15)$. Find $f(10)$. → $m = 3$, $f(x) = 3x+3$, $f(10) = 33$

[Very Hard] Car worth \$24,000 after 2 years, \$12,000 after 6. Initial value? → $m = -3000$, $V(t) = -3000t + 30000$, initial $= \$30,000$

---

### Set 4: Inequalities

[Easy] $4x - 7 > 9$ → $x > 4$

[Medium] $-2x + 5 \leq 13$ → $-2x \leq 8$ → $x \geq -4$

[Hard] $3 \leq 2x - 1 < 9$ → $4 \leq 2x < 10$ → $2 \leq x < 5$

[Very Hard] Sell widgets at \$12 each. Cost $C = 5w + 200$. Profit $\geq 400$? → $12w - (5w+200) \geq 400$ → $7w \geq 600$ → $w \geq 86$ (whole units)

---

### Set 5: Linear Relationships in Context

[Easy] A phone plan costs \$20/month plus \$0.10 per text. Cost for 150 texts? → $C = 0.10(150) + 20 = \$35$

[Medium] A town has 20,000 people and grows by 800 per year. When does it reach 26,400? → $20000 + 800t = 26400$ → $t = 8$ years

[Hard] A quantity triples every hour. Linear or exponential? If it starts at 4, find it after 3 hours. → Exponential, $4 \cdot 3^3 = 108$

[Very Hard] A \$60 shirt is discounted 30%, then the sale price is marked up 30%. Final price? → $60(0.70)(1.30) = \$54.60$ - not back to \$60 (the discount and markup are on different bases)

---

### Set 6: Two-Variable Equations & Standard Form

[Easy] Convert $2x + 5y = 10$ to slope-intercept. → $y = -\frac{2}{5}x + 2$

[Medium] Line through $(3, -1)$ and $(6, 5)$. Write equation. → $m = 2$, $y = 2x - 7$

[Hard] $4x + 3y = 24$: what does the $y$-intercept mean if $x$ = apples at \$4 and $y$ = oranges at \$3? → If no apples are bought, 8 oranges can be bought.

[Very Hard] A line is perpendicular to $2x - y = 3$ and passes through $(4, 1)$. Write it. → given line $y = 2x - 3$, perpendicular slope $-\frac{1}{2}$ → $y = -\frac{1}{2}x + 3$

---

**Before moving on:** ✅ Defined the variable? ✅ Re-read the question? ✅ Sign correct? ✅ Answer makes sense? ✅ Right units? ✅ Checked with Desmos where useful? ✅ Identified whether the equation is identity / conditional / contradiction (one variable) or 0 / 1 / infinite solutions (systems)?



