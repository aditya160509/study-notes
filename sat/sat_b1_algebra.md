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

6. **Inequalities in context** - budget or capacity constraints. You may need to check whether a given point (order, plan, combination) satisfies the inequality - the point is "feasible" or not.

7. **Linear function from two points or a table** - find slope, then intercept, then evaluate or interpret.

8. **Standard form $Ax + By = C$ in context** - what each coefficient means (per-unit rates) and what $C$ is (the total), plus finding intercepts from it.

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

---

### Standard Form $Ax + By = C$ in Context

| Part | Meaning in context |
|---|---|
| $A$ | Units of $C$ contributed per 1 unit of $x$ (a per-unit rate) |
| $B$ | Units of $C$ contributed per 1 unit of $y$ (a per-unit rate) |
| $C$ | The total, budget, or limit |
| Slope $-\frac{A}{B}$ | Trade-off rate: $x$ must decrease $\frac{A}{B}$ units per extra unit of $y$ |

---

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

---

### Systems: Number of Solutions

| Condition | Solutions |
|---|---|
| $m_1 \neq m_2$ | 1 (intersecting) |
| $m_1 = m_2$, $b_1 \neq b_2$ | 0 (parallel) |
| $m_1 = m_2$, $b_1 = b_2$ | Infinite (coincident) |

Standard form: $\frac{A_1}{A_2} = \frac{B_1}{B_2} \neq \frac{C_1}{C_2} \Rightarrow 0$; all three equal $\Rightarrow \infty$.

---

### Inequality Rules

- ×/÷ by **negative** → **flip** the sign

- Solid boundary: $\leq, \geq$ | Dashed: $<, >$

- Shade **above** for $>/\geq$, **below** for $</\leq$

- Compound "and" = intersection; "or" = union

- **Point-in-region test:** plug the point into the inequality. True $\Rightarrow$ in the solution set; false $\Rightarrow$ outside. On the boundary line $\Rightarrow$ included only if $\leq$ or $\geq$.

---

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

---

### Desmos Tips for Algebra

- **One-variable equation:** Graph LHS as $y_1$, RHS as $y_2$; intersection $x$ = solution

- **System:** Graph both equations, click intersection point

- **Inequality:** Type directly (`y < 2x+1`); Desmos shades automatically


- **Parameter slider:** Use `k` in equations; drag to test values

- **Function eval:** Define `f(x) = ...` then type `f(3)`

- **Table → equation:** Enter table, type `y1 ~ mx1 + b` for regression

- **Fractions:** Parentheses: `(2x+1)/(x-3)` not `2x+1/x-3`

- **Point-in-region check:** Type the inequality, then plot the point; if it lands in the shaded region, it satisfies the inequality

---

## B1.1 Linear Equations in One Variable

**What they test:** Solving $ax + b = c$ (and variants), determining solution type (unique/none/infinite), creating equations from word problems, interpreting constants in context. On the real test, expect roughly **3-5 questions** from this testing point alone.

---

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

**Solution:**

1. $3x - 12 = 2x + 5$
2. $x = 17$

✅ **Check:** $3(17-4) = 39$, $2(17)+5 = 39$.

❌ **Trap:** $3x - 4 = 2x + 5 \to x = 9$ - **Distribution error** (forgot to multiply $-4$ by 3).

---

**[Medium] Solve $\frac{3}{4}x - \frac{1}{2} = \frac{5}{8}$.**

**Solution:**

1. Multiply by 8 (LCD): $6x - 4 = 5$
2. $x = \frac{3}{2}$

❌ **Trap:** $6x - \frac{1}{2} = 5 \to x = \frac{11}{12}$ - **Partial multiplication** (only multiplied $x$ term by 8).

---

**[Medium] If $3(x - 2) + a = 5x - 6$ and $x = 4$, what is $a$?**

**Solution:**

1. $3(4-2) + a = 5(4)-6$
2. $6 + a = 14$
3. $a = 8$

❌ **Trap:** Solving for $x$ instead of $a$ - **Wrong variable target**.

---

**[Hard] Solve $\frac{2x - 1}{5} - \frac{x - 2}{3} = \frac{1}{15}$ for $x$.**

**Solution:**

1. Multiply by 15 (LCD): $3(2x - 1) - 5(x - 2) = 1$
2. $6x - 3 - 5x + 10 = 1$
3. $x + 7 = 1$
4. $x = -6$

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

**Solution:**

1. $2x + 6 = 2x + 6$
2. $0 = 0$. **Identity** - true for all $x$. Plug in $x = 1$: $8 = 8$. Plug in $x = 100$: $206 = 206$. Always true.

---

**[Easy] Classify $2(x + 3) = 2x + 7$: conditional, identity, or contradiction?**

**Solution:**

1. $2x + 6 = 2x + 7$
2. $6 = 7$. **Contradiction** - false for every $x$, no solution.

❌ **Trap:** "The $x$'s cancel, so there's no solution" is only half right - you must check the constants. If the constants also match, it is an identity with infinite solutions, not a contradiction.

---

**[Hard] If $3(2x - 5) + k = 6x - 15$ has infinitely many solutions, what is $k$?**

**Solution:**

1. $6x - 15 + k = 6x - 15$. For identity: $-15 + k = -15$
2. $k = 0$.

---

**[Very Hard] For what $c$ does $2(x - 3) + 5 = 2x + c$ have no solution?**

**Solution:**

1. $2x - 6 + 5 = 2x + c$
2. $2x - 1 = 2x + c$. $x$ coefficients match ($2 = 2$), so no solution when constants differ: any $c \neq -1$. If $c = -1$, infinite solutions.

❌ **Trap:** Writing "$c = -1$" - that is the identity value. The question asks for no solution, so the answer is **every value except** $-1$.

---

**[Hard] The equation $ax + b = 2x + 7$ has infinitely many solutions. What are $a$ and $b$?**

**Solution:**

For infinite solutions the two sides must be identical: $a = 2$ and $b = 7$.

---

**[Very Hard variant] The equation $ax + 4 = 3x + b$ has no solution. What must be true of $a$ and $b$?**

**Solution:**

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

**Solution:**

1. Let $x$ = the number. $x + 12 = 31$
2. $x = 19$.

✅ **Check:** $19 + 12 = 31$. ✔

---

**[Medium] A 200-liter mixture is $15\%$ salt. How many liters of pure water must be added to make it $10\%$ salt?**

**Solution:**

Let $x$ = liters of water added. Salt before: $0.15(200) = 30$ L. Total after: $200 + x$ L.

1. $0.10(200 + x) = 30$
2. $20 + 0.1x = 30$
3. $x = 100$

❌ **Trap:** $0.15(200) + x = 0.10(200 + x)$ - **Treating water as if it contains salt**. Water adds volume but zero salt.

---

**[Hard] Jack i s twice as old as Jill. In 12 years, the sum of their ages will be 75. How old is Jill now?**

**Solution:**

Let $x$ = Jill's age. Jack = $2x$. In 12 years: Jill = $x+12$, Jack = $2x+12$.

1. $(x+12) + (2x+12) = 75$
2. $3x = 51$
3. $x = 17$

❌ **Trap:** Adding 12 to Jack but forgetting to add 12 to Jill - **Asymmetric future ages**.

---

**[Very Hard] The sum of three consecutive integers is 72. What is the largest of the three?**

**Solution:**

1. Let the integers be $n, n+1, n+2$: $3n + 3 = 72$
2. $n = 23$.
3. Largest: $n + 2 = 25$.

❌ **Trap:** Answering 23 (the smallest) or 24 (the middle). "Consecutive" questions often ask for a specific one - underline which.

---

**[Very Hard] The tens digit of a two-digit number is 3 more than the units digit. The number is 7 times the sum of its digits. What is the number?**

**Solution:**

1. Let $t$ = tens digit, $u$ = units digit. $t = u + 3$.
2. Value of the number: $10t + u$. Given: $10t + u = 7(t + u)$.
3. $10(u+3) + u = 7(u + 3 + u)$
4. $11u + 30 = 14u + 21$
5. $3u = 9$
6. $u = 3$.
7. $t = 6$. The number is 63. Check: $6 = 3 + 3$ ✓; $63 = 7(6+3) = 63$ ✓.

❌ **Trap:** Writing $tu$ or $t + u$ for the number's value - a two-digit number is $10t + u$, not a product. Also forgetting the "7 times the sum" applies to the whole number.

---

## B1.2 Linear Functions

**What they test:** $f(x) = mx + b$, point-slope form, interpreting slope and intercept in context, writing equations from two points or point + rate, connecting tables/graphs/algebra. The official testing point also requires: evaluate a function for an input or find the input from an output, and write a rule given two input-output pairs or one pair + a rate of change.

---

### B1.2.1 Function Notation and Evaluation

**Definition in simplest terms:** $f(x)$ means "the output of function $f$ when the input is $x$." For a linear function $f(x) = mx + b$, $m$ is the slope (rate) and $b$ is the $y$-intercept (output when input is 0).

**Step-by-step method:**

- **Evaluate (input → output):** substitute the number for $x$ and compute.

- **Find input (output → input):** set $f(x)$ equal to the given output and solve for $x$.

**[Easy] If $f(x) = 3x - 5$, find $f(4)$.** → $f(4) = 3(4) - 5 = 7$

---

**[Medium] If $f(x) = 2x + 1$ and $f(a) = 17$, find $a$.** → $2a + 1 = 17$ → $a = 8$

---

**[Medium] If $f(2) = 5$ and $f(6) = 13$, find $f(x)$.**

**Solution:**

1. $m = \frac{13-5}{6-2} = 2$. $f(x) = 2x + b$; $5 = 2(2) + b$
2. $b = 1$. $f(x) = 2x + 1$.

❌ **Trap:** $f(2) = 5$ means $b = 5$ - **Intercept = $f(0)$, not $f(2)$**.

---

**[Easy] If $f(x) = 3x - 1$, what is $f(x + 2) - f(x)$?**

**Solution:**

$f(x+2) = 3(x+2) - 1 = 3x + 6 - 1 = 3x + 5$. So $f(x+2) - f(x) = (3x + 5) - (3x - 1) = 6$.

⚡ **Insight:** The answer is always $m \times 2 = 6$: adding 2 to the input adds $2m$ to the output. This is a fast SAT pattern - no algebra needed.

**General shortcut:** for a linear function with slope $m$, $f(a) - f(b) = m(a - b)$ - no algebra needed.

---

**[Very Hard] If $f(x) = \frac{x}{2} + 3$, what is $f(2x + 1)$ in terms of $x$?**

**Solution:**

1. $f(2x + 1) = \frac{2x + 1}{2} + 3 = x + \frac{1}{2} + 3 = x + \frac{7}{2}$.

❌ **Trap:** Computing $2f(x) + 1$ instead of $f(2x + 1)$ - order matters. Also, not simplifying $\frac{2x+1}{2}$ to $x + \frac{1}{2}$.

---

### B1.2.2 Slope and Rate of Change

**Definition in simplest terms:** Slope measures how fast $y$ changes per 1 unit of $x$: $m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\Delta y}{\Delta x}$. The units of $m$ are (units of $y$) per (unit of $x$).

**Step-by-step method:**

1. Pick two points (or two rows of a table).

2. Subtract the $y$-values (rise), subtract the $x$-values (run), in the **same order**.

3. Divide: $m = \frac{\text{rise}}{\text{run}}$.

4. For a linear function, the rate of change is the same between **any** two points.

**[Easy] Find the slope of the line through $(1, 2)$ and $(4, 11)$.**

**Solution:**

$m = \frac{11 - 2}{4 - 1} = \frac{9}{3} = 3$

❌ **Trap:** Computing $\frac{x_2 - x_1}{y_2 - y_1}$ (inverted) - slope is **rise over run**, always $\frac{\Delta y}{\Delta x}$.

---

**[Medium] The table shows a linear relationship:**

**Solution:**

| $x$ | 1 | 3 | 5 |
|---|---|---|---|
| $y$ | 7 | 15 | 23 |

1. $m = \frac{15-7}{3-1} = 4$. $7 = 4(1) + b$
2. $b = 3$. $f(x) = 4x + 3$.

✅ **Check:** $f(5) = 4(5) + 3 = 23$. Matches table.

❌ **Trap:** Reading $b = 7$ from the first row - **$b$ is $f(0)$, not the first $y$ in the table**. Compute it.

---

**[Medium] A plant is 12 cm tall at day 3 and 27 cm tall at day 8. Assuming constant (linear) growth, how tall was it at day 0?**

**Solution:**

1. $m = \frac{27 - 12}{8 - 3} = \frac{15}{5} = 3$ cm per day. $h(3) = 12$
2. $12 = 3(3) + b$
3. $b = 3$. So $h(0) = 3$ cm.

❌ **Trap:** Using day 3's height (12 cm) as the starting height - the intercept is the height at day 0, which must be computed by going back 3 days at 3 cm/day: $12 - 9 = 3$.

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

**Solution:**

1. $y - 3 = 5(x - 2)$
2. $y = 5x - 10 + 3$
3. $y = 5x - 7$

✅ **Check:** $5(2) - 7 = 3$. ✔

---

**[Medium] Line through $(2, -3)$ and $(-4, 9)$.**

**Solution:**

1. $m = \frac{9-(-3)}{-4-2} = \frac{12}{-6} = -2$. Using $(2,-3)$: $y+3 = -2(x-2)$
2. $y = -2x + 1$.

✅ **Check:** $(-4,9)$: $-2(-4) + 1 = 9$. ✔

---

**[Medium] Equation of line with $x$-int 4 and $y$-int $-2$?**

**Solution:**

Points: $(4,0)$ and $(0,-2)$. $m = \frac{-2-0}{0-4} = \frac{1}{2}$, $b = -2$. $y = \frac{1}{2}x - 2$.

❌ **Trap:** $y = \frac{1}{2}x + 2$ - **Sign error on $y$-intercept**.

---

**[Easy] A line passes through $(3, 7)$ and $(3, -2)$. What kind of line is it, and what is its equation?**

**Solution:**

The $x$-values are equal, so it is a **vertical line**: $x = 3$. Slope is undefined (division by zero).

❌ **Trap:** Trying to compute $m = \frac{-2 - 7}{3 - 3} = \frac{-9}{0}$ and calling it 0 - vertical lines have **undefined** slope, not zero slope. Zero slope is horizontal ($y = k$).

---

**[Very Hard] A line with slope $m$ passes through the points $(a, 5)$ and $(a + 4, 13)$. What is $m$?**

**Solution:**

1. $m = \frac{13 - 5}{(a+4) - a} = \frac{8}{4} = 2$.

❌ **Trap:** Panicking at the unknown $a$. The $a$'s cancel in the denominator difference - the slope is pure $\frac{\Delta y}{\Delta x}$.

---

### B1.2.4 Interpreting Slope and Intercept in Context

**Definition in simplest terms:** In a context, the **slope** is the rate - how much the output changes per 1 unit of input. The **intercept** is the starting value - the output when the input is 0. A **negative slope** means the quantity is decreasing.

**[Easy] A taxi charges $C = 3h + 10$, where $h$ is miles driven. What does the 3 represent? What does the 10 represent?**

**Solution:**

- 3 = the charge, in dollars, **per mile**.
- 10 = the base fare, in dollars, charged for 0 miles (the flag drop).

❌ **Trap:** Saying "3 is the total cost" - the coefficient is a per-unit rate, not a total.

---

**[Medium] $C = 5n + 200$ models production cost for $n$ widgets. What does 200 represent?**

**Solution:**

Cost when $n = 0$: fixed costs (equipment, rent).

❌ **Trap:** "Cost per widget" - **Confusing intercept with slope**. The 5 is per-unit; 200 is fixed.

---

**[Hard] $p = 50 - 0.2q$ models price $p$ at which $q$ units sell. Interpret 50.**

**Solution:**

When $q = 0$, $p = 50$: the price when no units are sold (maximum price).

❌ **Trap:** "Maximum number of units" - **Reading a zero-output as an input constraint**. The $q$-intercept (where $p = 0$) gives max quantity.

---

**[Medium] A drone's altitude is modeled by $h(t) = 1200 - 25t$, where $t$ is minutes after launch. Interpret the 1200, the $-25$, and find when the drone lands.**

**Solution:**

- 1200 = starting altitude, in meters, at $t = 0$ (launch).
- $-25$ = the altitude **decreases by 25 meters per minute** (rate of descent).

1. - Landing: $h(t) = 0$
2. $1200 - 25t = 0$
3. $t = 48$ minutes.

❌ **Trap:** Saying "the drone loses 25 meters total" - $-25$ is the rate **per minute**. Total loss is 1200 m. The negative sign tells you the direction (decreasing).

---

**[Medium] $V = 25000 - 3000t$ models machine value after $t$ years. Interpret.**

**Solution:**

$-3000$: annual depreciation. $25000$: initial value.

❌ **Trap:** "The machine loses $3000$ total" - **Annual vs. total depreciation confusion**.

---

**[Medium] Balloon height $h(t) = 300 - 4.9t^2$. Is this linear?**

**Solution:**

No - quadratic. The SAT may embed a non-linear equation in a "linear" context to test recognition.

❌ **Trap:** Calling it linear because it "goes down" - linear requires the input to appear to the **first power only**. The $t^2$ term makes it quadratic.

---

### B1.2.5-2.6 Connected Representations and Writing Rules

**Definition in simplest terms:** The same linear function can be shown as a table of $(x, f(x))$ pairs, an equation $f(x) = mx + b$, or a graph (a straight line). The SAT asks you to move between these: table → equation, graph → equation, equation → graph, and given conditions → equation.

**Step-by-step method:**

1. Find two points (from the table, the graph, or given conditions).

2. Compute slope $m = \frac{\Delta y}{\Delta x}$.

3. Find $b$ by plugging one point into $y = mx + b$.

4. Check against a third point / the graph's intercepts.

**What they test (official):** "write rule given two input-output pairs or one pair + rate of change." This is a frequent SAT format.

**Step-by-step method:**

1. **Two pairs:** slope $m = \frac{y_2 - y_1}{x_2 - x_1}$, then plug one pair into $y = mx + b$ to find $b$.

2. **One pair + rate:** the rate IS the slope. Plug the pair into $y = mx + b$ to find $b$.

3. Write $f(x) = mx + b$ and answer what was asked (often evaluate at a new input).

**[Medium] Which function matches the table?**

**Solution:**

| $x$ | 0 | 2 | 4 |
|---|---|---|---|
| $f(x)$ | -3 | 5 | 13 |

1. $m = \frac{5-(-3)}{2-0} = 4$. $f(0) = -3$
2. $b = -3$. $f(x) = 4x - 3$.

❌ **Trap:** $m = 2$ by counting $x\to y$ as 1-step ratio - **$x$ changed by 2, $y$ by 8, so $m = 8/2 = 4$**.

---

**[Medium] A taxi charges a flat fee plus \$3.50 per mile. A 10-mile trip costs \$42.50. Write the cost function $f(m)$ and find the flat fee.**

**Solution:**

1. $f(m) = 3.5m + b$; $42.5 = 3.5(10) + b$
2. $b = 7.5$. So $f(m) = 3.5m + 7.5$; the flat fee is \$7.50.

❌ **Trap:** Using the flat fee as the slope or treating \$42.50 as the fee - the per-mile rate is given; the 10-mile cost lets you solve for the **intercept**.

---

**[Very Hard] A book club charges a one-time membership fee plus a per-book price. Five books cost $\$41$; eight books cost $\$59$. What would 12 books cost?**

**Solution:**

1. Slope: $m = \frac{59 - 41}{8 - 5} = \frac{18}{3} = 6$ per book.
2. $41 = 6(5) + b$
3. $b = 11$ membership fee.
4. $C(12) = 6(12) + 11 = \$83$.

❌ **Trap:** Assuming the one-time fee is $41$ (the 5-book cost). The intercept is $11$, the per-book rate is $6$.

⚡ **Desmos:** Enter $(5, 41)$ and $(8, 59)$, fit `y1 ~ mx1 + b`, then read `y1(12)`.

---

### B1.2.7 Linear Models in Context

**Definition in simplest terms:** A linear model uses $f(x) = mx + b$ to describe a real situation: $b$ = starting amount, $m$ = change per unit of $x$.

**Step-by-step method:** Identify the starting value ($b$) and the rate ($m$) from the story, build $f(x)$, then evaluate or solve.

**[Easy] A pool starts with 1000 gallons and fills at 25 gallons per minute. Write $P(t)$ and find the amount after 10 minutes.**

**Solution:**

$P(t) = 25t + 1000$. $P(10) = 25(10) + 1000 = 1250$ gallons.

---

**[Easy] Temperature $T = 85 - 4m$ (degrees Celsius after $m$ minutes). When does $T = 25$?**

**Solution:**

1. $25 = 85 - 4m$
2. $m = 15$ minutes

❌ **Trap:** Solving $85 - 4m = 0$ - **Wrong target. Question asks $T=25$, not $T=0$**.

---

**[Medium] Population $P(t) = 2000 + 150t$, $t$ = years since 2020. When does it reach 5000?**

**Solution:**

1. $5000 = 2000 + 150t$
2. $t = 20$
3. Year: $2020 + 20 = 2040$

❌ **Trap:** Answering $t = 20$ when question asks for the year - **Always re-read what's being asked**.

---

## B1.3 Linear Equations in Two Variables

**What they test:** $Ax + By = C$, converting between forms, parallel/perpendicular lines, interpreting intercepts and coefficients in context, writing equations from given information (two points, point + slope, point + parallel/perpendicular line).

---

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

**Solution:**

1. $4y = -3x + 12$
2. $y = -\frac{3}{4}x + 3$

❌ **Trap:** $y = 3x + 12$ - **Dividing only the $x$ term by 4**. Every term must be divided.

---

**[Medium] Line $2x + 3y = 6$. Find slope and both intercepts.**

**Solution:**

1. $m = -\frac{A}{B} = -\frac{2}{3}$. $y$-int ($x=0$): $3y=6$
2. $y=2$. $x$-int ($y=0$): $2x=6$
3. $x=3$.

✅ **Check:** Intercept form $\frac{x}{3} + \frac{y}{2} = 1$ confirms $(3,0)$ and $(0,2)$.

---

**[Medium] Convert $y = \frac{2}{3}x - 4$ to standard form with integer coefficients.**

**Solution:**

1. Multiply by 3: $3y = 2x - 12$
2. rearrange: $2x - 3y = 12$ (equivalently $-2x + 3y = -12$).

❌ **Trap:** Writing $2x - 3y = -12$ with the wrong sign - bring terms across correctly: $2x - 12 = 3y$ → $2x - 3y = 12$.

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

**Solution:**

Parallel: $4$. Perpendicular: $-\frac{1}{4}$.

❌ **Trap:** Perpendicular slope $-4$ - must flip **and** change sign: $4 \to -\frac{1}{4}$.

---

**[Medium] Line through $(1,5)$ perpendicular to $y = -\frac{3}{4}x + 2$.**

**Solution:**

1. Perpendicular slope: $\frac{4}{3}$. $y - 5 = \frac{4}{3}(x-1)$
2. $y = \frac{4}{3}x + \frac{11}{3}$

❌ **Trap:** Using $-\frac{4}{3}$ (sign flip only) or $-\frac{3}{4}$ (parallel) - **Wrong slope relationship**.

---

**[Medium] For what $k$ is $kx + 2y = 8$ perpendicular to $y = \frac{1}{3}x + 4$?**

**Solution:**

1. $m_1 = -\frac{k}{2}$, $m_2 = \frac{1}{3}$. Perpendicular: $(-\frac{k}{2})(\frac{1}{3}) = -1$
2. $k = 6$

❌ **Trap:** Setting $-\frac{k}{2} = \frac{1}{3}$ - **Parallel condition. Perpendicular requires product $= -1$**.

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

---

### B1.3.4 Intercepts from Standard Form

**Definition in simplest terms:** The $x$-intercept is where the line crosses the $x$-axis ($y = 0$); the $y$-intercept is where it crosses the $y$-axis ($x = 0$). From $Ax + By = C$: set the other variable to 0.

$x$-int $= \frac{C}{A}$ (set $y=0$), $y$-int $= \frac{C}{B}$ (set $x=0$).

**[Easy] $5x - 2y = 20$: find both intercepts.**

**Solution:**

1. $x$-int: $5x = 20$
2. $x = 4$. $y$-int: $-2y = 20$
3. $y = -10$.

❌ **Trap:** $y = 10$ - **Sign error from $-2y$**.

---

**[Medium] Line has $x$-int $-3$, $y$-int $6$. Write in standard form.**

**Solution:**

1. $\frac{x}{-3} + \frac{y}{6} = 1$
2. multiply by 6: $-2x + y = 6$
3. $2x - y = -6$

✅ **Check:** $y=0$ → $2x = -6$ → $x=-3$. $x=0$ → $-y = -6$ → $y=6$. ✔

---

**[Medium] The line $2x + 3y = k$ has $x$-intercept $-6$. Find $k$ and the $y$-intercept.**

**Solution:**

1. $x$-int: $y = 0$
2. $2(-6) = k$
3. $k = -12$. Then $y$-int: $x = 0$
4. $3y = -12$
5. $y = -4$.

⚡ **Desmos tip:** Type `2x + 3y = k` with a slider for $k$; drag until the line crosses the $x$-axis at $-6$. Desmos shows the intercepts as clickable points.

---

**[Very Hard] Line $l$ passes through $(4, 9)$ and has slope $-\frac{3}{2}$. What is the $x$-intercept of $l$?**

**Solution:**

1. $y - 9 = -\frac{3}{2}(x - 4)$
2. $y = -\frac{3}{2}x + 6 + 9 = -\frac{3}{2}x + 15$.
3. $x$-intercept: $0 = -\frac{3}{2}x + 15$
4. $\frac{3}{2}x = 15$
5. $x = 10$.

❌ **Trap:** Sign error on the slope when distributing: $-\frac{3}{2}(x-4) = -\frac{3}{2}x + 6$. Getting $y = -\frac{3}{2}x - 6 + 9$ gives intercept 2 instead of 10.

---

### B1.3.5 Graphs and Solutions in Context

**Definition in simplest terms:** The graph of a two-variable equation shows **all** pairs $(x, y)$ that satisfy it. Intercepts are the "only one category" extremes; in context they answer "what if we bought none of the other item?"

**[Easy] $x + 2y = 10$ models $x$ apples and $y$ oranges in a bag of 10 fruits (weighted oddly). What does the $y$-intercept $(0, 5)$ mean?**

**Solution:**

If no apples are in the bag, there are 5 oranges.

---

**[Medium] $4x + 6y = 120$: adult (\$4) and child (\$6) tickets for \$120 revenue. What does $x$-intercept mean?**

**Solution:**

1. Set $y=0$: $4x = 120$
2. $x = 30$. If no child tickets sold, 30 adult tickets generate \$120.

---

**[Very Hard] For what value of $k$ is the point $(k, 2k)$ on the line $3x - 4y = 10$?**

**Solution:**

1. Substitute: $3k - 4(2k) = 10$
2. $3k - 8k = 10$
3. $-5k = 10$
4. $k = -2$.

❌ **Trap:** Substituting $x = k$ and $y = k$ (treating them as equal) instead of $y = 2k$. Read the point's coordinates as ordered pairs.

---

### B1.3.6 Writing Equations from Given Information

**What they test (official):** "write equation given two points, one point + slope, or one point + parallel/perpendicular line."

**[Medium] Write the line through $(-1, 4)$ parallel to $y = 3x - 2$.**

**Solution:**

1. Parallel $\Rightarrow$ slope 3. $y - 4 = 3(x + 1)$
2. $y = 3x + 7$.

❌ **Trap:** Using slope $-3$ (perpendicular by accident) or using the given line's intercept $-2$ - the new line has its own intercept, found by plugging in the point.

---

**[Medium] Write the line through $(3, -2)$ perpendicular to $2x + y = 5$.**

**Solution:**

1. $2x + y = 5$
2. $y = -2x + 5$, slope $-2$. Perpendicular slope: $\frac{1}{2}$. $y + 2 = \frac{1}{2}(x - 3)$
3. $y = \frac{1}{2}x - \frac{7}{2}$.

✅ **Check:** $(-2)(\frac{1}{2}) = -1$. ✔ And $\frac{1}{2}(3) - \frac{7}{2} = \frac{3 - 7}{2} = -2$. ✔

---

## B1.4 Systems of Two Linear Equations

> **Cross-domain:** Systems involving non-linear equations (quadratic-linear, exponential-linear) are covered in B2 (Advanced Math). See B2 §2.8-§2.9 for polynomial and exponential systems.

**What they test:** Substitution, elimination, Desmos intersection method, determining solution count via slopes, modeling real-world constraints, connecting algebraic and graph representations.

---

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

**Solution:**

1. $2x + (3x - 4) = 11$
2. $5x = 15$
3. $x = 3$, $y = 5$

❌ **Trap:** $2x + 3x - 4 = 11$ → $x - 4 = 11$ - **Combining like terms incorrectly**.

---

#### Elimination

**[Hard] $3x - 4y = 10$ and $5x + 2y = 8$.**

**Solution:**

1. Multiply second by 2: $10x + 4y = 16$. Add: $13x = 26$
2. $x = 2$, $y = -1$.

❌ **Trap:** $10x + 2y = 8$ - **Partial multiplication** (only multiplied $x$ term by 2).

---

#### Desmos

**[Hard] $4.7x + 2.3y = 15.1$ and $1.8x - 3.2y = 4.6$.**

**Solution:**

Intersection $\approx$ $(3.07, 0.29)$. 15 seconds in Desmos vs. 2-3 minutes algebraically.

⚡ **Desmos tip:** Type both equations exactly as written (standard form is fine - Desmos handles it). Click the intersection point to read $(x, y)$.

---

**[Very Hard] If $2x + 5y = 19$ and $5x + 2y = 13$, what is the value of $x + y$?**

**Solution:**

1. Add the two equations: $7x + 7y = 32$
2. Divide by 7: $x + y = \frac{32}{7}$

❌ **Trap:** Solving the system fully and wasting 60 seconds. The SAT asks for $x + y$ on purpose - adding the equations gives it directly in one line.

⚡ **Desmos insight:** Graph both lines and read the intersection, then compute $x + y$ from the point.

---

**[Very Hard] The system $ax + by = 6$ and $cx + dy = 10$ has exactly one solution at $(2, -1)$. What is the value of $2a - b$?**

**Solution:**

1. Substitute the point into the first equation: $a(2) + b(-1) = 6$
2. $2a - b = 6$. Done - the second equation is a distractor.

❌ **Trap:** Trying to use both equations. The point satisfies BOTH, so either one alone pins down the requested combination when the combination matches the structure of the equation.

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

**Solution:**

1. First system: same slope (2), different intercepts (1 vs $-3$)
2. **no solution** (parallel lines). Second system: identical equations
3. **infinite solutions**.

❌ **Trap:** Answering "no solution" for both - identical lines share **every** point, which is infinite solutions, not zero.

---

**[Medium] $3x + 6y = 12$ and $x + 2y = 4$: how many solutions?**

**Solution:**

1. First ÷3: $x + 2y = 4$. Identical to second
2. infinite.

❌ **Trap:** Saying "no solution" because right sides differ at a glance - **Must check proportionality**.

---

**[Hard] For what $k$ does $4x + ky = 8$ and $2x - 3y = 5$ have no solution?**

**Solution:**

Eq1: $y = -\frac{4}{k}x + \frac{8}{k}$ ($k \neq 0$). Eq2: $y = \frac{2}{3}x - \frac{5}{3}$.

1. Slopes equal: $-\frac{4}{k} = \frac{2}{3}$
2. $k = -6$. Intercepts: $\frac{8}{-6} = -\frac{4}{3} \neq -\frac{5}{3}$. Parallel
3. $k = -6$.

❌ **Trap:** $k = 6$ - **Sign error** in $-\frac{4}{k} = \frac{2}{3}$.

---

**[Medium] For what $k$ does $2x + 3y = 6$ and $4x + 6y = k$ have infinite solutions?**

**Solution:**

1. Proportional: $\frac{2}{4} = \frac{3}{6} = \frac{6}{k}$
2. $\frac{1}{2} = \frac{6}{k}$
3. $k = 12$

❌ **Trap:** $k = 6$ - **Partial check. Must include constant ratio: $6/k = 1/2$**.

---

### B1.4.3 Word Problems with Systems

**Definition in simplest terms:** Real-world constraints give two equations in two unknowns. The classic structure: one equation for **counts** (items, hours, people) and one for **totals** (cost, revenue, volume).

**Step-by-step method:**

1. Define two variables (one per unknown category).

2. Equation 1: the count/quantity relationship.

3. Equation 2: the value/amount relationship (costs, percentages, revenue).

4. Solve (substitution or elimination), then answer what was asked (often a combination like $x + y$ or a product).

**[Easy] Two numbers sum to 20 and differ by 4. Find them.**

**Solution:**

1. $x + y = 20$, $x - y = 4$. Add: $2x = 24$
2. $x = 12$, $y = 8$.

✅ **Check:** $12 + 8 = 20$; $12 - 8 = 4$. ✔

---

**[Hard] Baker sells loaves (\$4) and pastries (\$2). Sold 60 items, earned \$180. How many loaves?**

**Solution:**

1. $L + P = 60$, $4L + 2P = 180$. First ×2: $2L + 2P = 120$. Subtract: $2L = 60$
2. $L = 30$.

❌ **Trap:** $4L + 2P = 60$ - **Confusing item count with revenue**.

---

**[Hard] Mix 12% acid with 20% acid to get 500 mL of 15%. How much of each?**

**Solution:**

$x$ = mL of 12%, $y$ = mL of 20%. $x + y = 500$, $0.12x + 0.20y = 75$.

1. Multiply second by 100: $12x + 20y = 7500$. First ×12: $12x + 12y = 6000$. Subtract: $8y = 1500$
2. $y = 187.5$, $x = 312.5$.

❌ **Trap:** $0.12x + 0.20y = 500$ - **Right side = pure acid ($75$), not total volume ($500$)**.

---

**[Very Hard] Product A needs 2h machine + 3h labor. Product B needs 4h machine + 1h labor. Available: 80 machine hours, 60 labor hours.**

**Solution:**

$a$ = units of A, $b$ = units of B.
Machine: $2a + 4b = 80$. Labor: $3a + b = 60$.

1. $b = 60 - 3a$
2. $2a + 4(60-3a) = 80$
3. $-10a = -160$
4. $a = 16$, $b = 12$

✅ **Check:** Machine: $2(16) + 4(12) = 32 + 48 = 80$. Labor: $3(16) + 12 = 60$. ✔

---

### B1.4.4 Connecting Algebraic and Graph Representations

**Definition in simplest terms:** The solution of a system IS the intersection point of the two lines. You may be given the graph and asked to identify the system, or given the system and asked what the graph looks like, or asked to interpret the intersection in a context.

**Step-by-step method:**

1. **Graph → system:** read the intersection point; verify it satisfies candidate equations.

2. **System → graph:** convert to slope-intercept to picture the lines (crossing, parallel, coincident).

3. **Intersection in context:** the point where two models give the same output (break-even, catch-up, equal cost).

**[Easy] The lines $y = x + 1$ and $y = -x + 5$ intersect at $(2, 3)$. Verify.**

**Solution:**

$y = 2 + 1 = 3$. ✔  $y = -2 + 5 = 3$. ✔  The point satisfies both equations.

---

**[Very Hard] If $f(x) = 2x + 5$ and $g(x) = 3x - 1$, for what value of $x$ is $f(x) = g(x)$? What does this value represent on the graphs?**

**Solution:**

1. $2x + 5 = 3x - 1$
2. $x = 6$.
3. $f(6) = 17$, $g(6) = 17$. The point $(6, 17)$ is where the two lines INTERSECT.

❌ **Trap:** Giving only $x = 6$ without the $y$-value when asked "what does it represent" - the full answer is the intersection point $(6, 17)$.

---

**[Hard] Company A charges $y = 40x + 100$; Company B charges $y = 60x$ (x = hours, y = cost). Interpret the intersection and find it.**

**Solution:**

1. $40x + 100 = 60x$
2. $x = 5$, $y = 300$. At **5 hours** both cost **\$300** (the break-even point). For fewer than 5 hours, Company B is cheaper; for more than 5 hours, Company A is cheaper.

❌ **Trap:** Reporting only "$x = 5$" without the cost or the comparison meaning - the question usually wants the interpretation (which company is cheaper when), not just the number.

⚡ **Desmos tip:** Type both equations, click the intersection. Desmos shows $(5, 300)$ instantly - then interpret in context.

---

## B1.5 Linear Inequalities

**What they test:** Solving single inequalities (flip sign for negative multiplication/division), compound inequalities, graphing with solid/dashed lines and shading, systems of inequalities, and interpreting points relative to a solution region in context.

---

### B1.5.1 Solving Single Linear Inequalities

**Definition in simplest terms:** An inequality says one side is bigger/smaller than the other. Solving it works exactly like an equation, with **one critical extra rule: multiplying or dividing both sides by a NEGATIVE number flips the inequality sign** ($<$ becomes $>$, $\leq$ becomes $\geq$, and vice versa).

**Step-by-step method:**

1. Distribute and combine like terms (same as equations).

2. Move variable terms to one side, constants to the other.

3. Divide by the coefficient. **If that coefficient is negative, flip the sign.**

4. Graph the solution on a number line or express as an interval.

**[Easy] Solve $2x + 5 > 13$ for $x$.**

**Solution:**

1. Subtract 5: $2x > 8$
2. Divide by 2: $x > 4$

❌ **Trap:** $x < 4$ - **Flipping unnecessarily. Only flip for negative ×/÷**.

---

**[Medium] $-3x + 7 \leq 22$** → $-3x \leq 15$ → $x \geq -5$ (flip)

❌ **Trap:** $x \leq -5$ - **Forgetting to flip when dividing by negative**.

---

**[Medium] $\frac{2x - 5}{3} \leq \frac{x + 4}{2}$**

**Solution:**

1. Multiply by 6: $2(2x-5) \leq 3(x+4)$
2. $4x - 10 \leq 3x + 12$
3. $x \leq 22$

❌ **Trap:** $2x-5 \leq x+4$ → $x \leq 9$ - **Dropping denominators. Multiply by LCD**.

---

**[Hard] $-2(x - 3) + 5 \geq 3(x + 1) - 4$**

**Solution:**

1. $-2x + 6 + 5 \geq 3x + 3 - 4$
2. $-2x + 11 \geq 3x - 1$
3. $12 \geq 5x$
4. $x \leq \frac{12}{5}$ (divide by positive 5: no flip)

❌ **Trap:** Flipping at the last step because "we divided" - you only flip when dividing by a **negative** number. Dividing by $+5$ keeps the sign. Also check the distribution: $-2(x-3) = -2x + 6$, not $-2x - 6$.

⚡ **Desmos tip:** Type the inequality directly (`-2(x-3)+5 >= 3(x+1)-4`); Desmos shades the solution region on the number line and you can read the boundary.

---

**[Medium] Scores 82 and 76 on two tests. What third score gives average $\geq 80$?**

**Solution:**

1. $\frac{82 + 76 + x}{3} \geq 80$
2. $158 + x \geq 240$
3. $x \geq 82$

❌ **Trap:** Using $>$ instead of $\geq$ - **"At least" means $\geq$, not $>$**.

---

### B1.5.2 Compound Inequalities

**Definition in simplest terms:** Two inequalities joined by **"and"** (both must hold - the solution is the **intersection**/overlap) or **"or"** (at least one holds - the solution is the **union** of both). A chained form like $-5 < 2x + 1 < 7$ is a hidden "and": $2x+1 > -5$ AND $2x+1 < 7$.

**Step-by-step method:**

1. **Chained "and" ($a < x < b$):** apply the same operation to ALL THREE parts (subtract, then divide - flip both signs if dividing by a negative).

2. **Separate "or":** solve each inequality independently, then combine with "or".

3. Graph: "and" = overlap of the two number-line regions; "or" = both regions together.

**[Medium] $-5 < 2x + 1 < 7$**

**Solution:**

Subtract 1: $-6 < 2x < 6$. Divide: $-3 < x < 3$.

❌ **Trap:** Solving only one side ($2x+1 < 7 \to x < 3$) - **Both inequalities must be satisfied**.

---

**[Medium] $3x - 7 \leq 5$ or $2x + 1 > 11$**

**Solution:**

First: $x \leq 4$. Second: $x > 5$. Solution: $x \leq 4$ or $x > 5$.

❌ **Trap:** Treating "or" as "and" → presenting $4 < x \leq 5$ (empty set).

---

**[Hard] Solve and graph: $4x - 3 \leq 9$ AND $2x + 1 > -5$; then solve $x - 2 > 3$ OR $2x \leq 8$.**

**Solution:**

1. First ("and"): $4x \leq 12$
2. $x \leq 3$; and $2x > -6$
3. $x > -3$. Overlap: $-3 < x \leq 3$.

Second ("or"): $x > 5$; or $x \leq 4$. Union: $x \leq 4$ or $x > 5$ (everything except $4 < x \leq 5$).

❌ **Trap:** Writing the "or" answer as a single chained inequality like $4 < x \leq 5$ - "or" solutions are usually **two separate rays**, not one interval.

---

**[Very Hard] For how many integer values of $x$ is $-3 < \frac{2x - 1}{3} \leq 5$?**

**Solution:**

1. Multiply all parts by 3: $-9 < 2x - 1 \leq 15$.
2. Add 1: $-8 < 2x \leq 16$
3. $-4 < x \leq 8$.
4. Integers: $-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8$
5. 12 integers.

❌ **Trap:** Counting $-4$ (the strict $<$ excludes it) or forgetting that $x$ must be an integer when the solution is a range. Also, multiplying each part by 3 must happen to ALL THREE parts.

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

**[Easy] Graph $y < x + 1$.**

**Solution:**

1. Boundary $y = x + 1$ dashed (strict). Shade below. Test $(0,0)$: $0 < 1$ true
2. shade the side containing the origin.

---

**[Medium] Graph $3x + 2y \leq 6$.** $y \leq -\frac{3}{2}x + 3$. Solid line, shade below. $(0,0)$: $0 \leq 6$ true.

❌ **Trap:** Shading above when $y \leq$ - **Reversing shading direction**.

---

**[Easy] Graph $x > 2$.**

**Solution:**

Vertical dashed line at $x = 2$; shade to the right (all points with $x > 2$).

❌ **Trap:** Drawing a horizontal line - $x > 2$ constrains the $x$-coordinate, so the boundary is **vertical**. Test point $(3, 0)$: $3 > 2$ true, so the right side is correct.

---

**[Medium] Graph $y \geq -\frac{1}{2}x + 1$ and identify whether $(4, -1)$ is in the solution set.**

**Solution:**

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

**Solution:**

1. $5 \geq 2(3) - 1 = 5$. True ($5 = 5$)
2. yes, on the boundary, and the boundary is included because of $\geq$.

---

**[Medium] A bakery's labor constraint is $3c + b \leq 24$: $c$ cakes take 3 hours each, $b$ batches of cookies take 1 hour each, 24 hours available per day. Is making 5 cakes and 10 batches feasible? What about 4 cakes and 12 batches?**

**Solution:**

1. - $(5, 10)$: $3(5) + 10 = 25 > 24$
2. **No**. This order needs 25 hours, exceeding the limit - it falls outside the shaded region.

1. - $(4, 12)$: $3(4) + 12 = 24 \leq 24$
2. **Yes**. Uses exactly the available hours - it lies on the (solid) boundary.

❌ **Trap:** Checking "24 $\leq$ 24" and calling it a failure - equality satisfies $\leq$, so boundary points are feasible.

---

**[Very Hard] A student needs to earn at least \$300/week across two jobs: Job A pays \$15/hr, Job B pays \$12/hr, and total hours are capped at 25: $15a + 12b \geq 300$ and $a + b \leq 25$. Is working 10 hours at A and 14 at B feasible? What about 8 hours at A and 14 at B?**

**Solution:**

- $(10, 14)$: earnings $15(10) + 12(14) = 150 + 168 = 318 \geq 300$ ✓; hours $10 + 14 = 24 \leq 25$ ✓. **Feasible.**
- $(8, 14)$: earnings $120 + 168 = 288 < 300$ ✗. **Not feasible** - fails the earnings requirement even though the hours work.

❌ **Trap:** Checking only one constraint - a point must satisfy **every** inequality in the system. On the graph it must lie in the overlap of all shaded regions.

---

### B1.5.5 Systems of Inequalities

**Definition in simplest terms:** A system of inequalities has a solution region that is the **overlap** of each individual half-plane. Every point in the overlap satisfies all constraints at once.

**Step-by-step method:**

1. Graph each inequality (solid/dashed + shading as in B1.5.3).

2. The solution is the region where ALL shadings overlap.

3. To check a point: verify it against every inequality.

4. Real-world systems: always include $x \geq 0$, $y \geq 0$ (non-negativity) when quantities can't be negative.

**[Easy] Which region is the solution of $\begin{cases} y > 0 \\ y < 3 \end{cases}$?**

**Solution:**

The horizontal strip strictly between $y = 0$ and $y = 3$ (both boundaries dashed - not included).

---

**[Medium] Which point satisfies both $y < 2x + 1$ and $y \geq -x + 3$?**

**Solution:**

A) $(0,0)$: $0 < 1$ ✓, $0 \geq 3$ ✗. B) $(1,4)$: $4 < 3$ ✗. C) $(2,1)$: $1 < 5$ ✓, $1 \geq 1$ ✓. **Answer: C.**

❌ **Trap:** Checking only one inequality - **A point must satisfy ALL inequalities**.

---

**[Hard] Company makes two products. A needs 2h labor, B needs 3h. At most 60h/week. At least 10 total products/week.**

**Solution:**

$a$ = units of A, $b$ = units of B.
$2a + 3b \leq 60$, $a + b \geq 10$, $a \geq 0$, $b \geq 0$

✅ **Always include non-negativity** for real-world quantities.

---

**[Very Hard] A bakery can make at most 60 cakes per day. Each cake needs 2 cups of flour and 3 eggs. The bakery has 150 cups of flour and 200 eggs. If $c$ = cakes, which inequality system is correct?**

**Solution:**

1. Capacity: $c \leq 60$.
2. Flour: $2c \leq 150$
3. $c \leq 75$.
4. Eggs: $3c \leq 200$
5. $c \leq 66\frac{2}{3}$.
6. Combined: $c \leq 60$ (the binding constraint). The answer is $c \leq 60$ alone - the flour and egg constraints never bind.

❌ **Trap:** Building a two-variable system when the problem is one-variable. Since every cake uses the same resources, each constraint is a single inequality on $c$ - and the limiting one is the smallest upper bound.

---

## Common Mistake Catalog

| 1 | **Not distributing to all terms** | $3(x-4) = 3x-4$ | $3x-12$ |
| 2 | **Forgetting to flip inequality sign** | $-3x > 9 \to x > -3$ | $x < -3$ |
| 3 | **Losing negative in standard form slope** | $2x+3y=6 \to m = \frac{2}{3}$ | $m = -\frac{2}{3}$ |
| 4 | **Partial multiplication in elimination** | $3(2x+y=5) \to 6x+y=15$ | $6x+3y=15$ |
| 5 | **Identity vs. contradiction** | $0=0$ → infinite, not "no solution" |
| 6 | **Slope/intercept mix-up** | "$200$ in $C=5n+200$ is per-widget cost" → it's the fixed cost ($n=0$ value); slope is the per-unit rate |
| 7 | **$y$-intercept from table** | $b = \text{first } y$ in table → $b = f(0)$, compute it |
| 8 | **"Or" vs. "and" in compound** | $x<2$ or $x>5$ as $2<x<5$ → two separate ranges |
| 9 | **One-variable "no solution" trap** | $3(2x-5)=6x+k$ no solution → $k=-15$ (that's infinite!) → $k \neq -15$ |
| 10 | **Standard form $C$ meaning** | $C$ in $Ax+By=C$ = total/budget, not a per-unit price |
| 11 | **Wrong variable target** | Found $x$, question asks for $2x+1$ |
| 12 | **Confusing count with cost** | $4L+2P = 60$ (cost = item count) |
| 13 | **Forgetting non-negativity** | Real-world quantities can't be negative |
| 14 | **Point outside the region** | Checking only one inequality in a system → must satisfy ALL |
| 15 | **Inverted slope** | $\frac{x_2-x_1}{y_2-y_1}$ | $\frac{y_2-y_1}{x_2-x_1}$ |
| 16 | **Perpendicular: sign only** | $\frac{2}{3} \to -\frac{2}{3}$ | $\to -\frac{3}{2}$ |
| 17 | **Partial compound solving** | $-5<2x+1<7 \to x<3$ | $-3 < x < 3$ |
| 18 | **Dividing only one term** | $\frac{3x+6}{3} = x+6$ | $x+2$ |
