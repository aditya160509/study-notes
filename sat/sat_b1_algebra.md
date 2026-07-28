# Digital SAT Algebra (Domain B1)

~35% of Math section — 13-15 of 44 questions. Five official testing points covering linear equations, functions, systems, and inequalities. Desmos built-in on every question.

**Domain cross-references:** B2 (Advanced Math) for quadratic/exponential systems, piecewise functions | B3 (Data Analysis) for linear models in context | B4 (Geometry & Trig) for coordinate geometry applications

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

### Systems: Number of Solutions
| Condition | Solutions |
|---|---|
| $m_1 \neq m_2$ | 1 (intersecting) |
| $m_1 = m_2$, $b_1 \neq b_2$ | 0 (parallel) |
| $m_1 = m_2$, $b_1 = b_2$ | Infinite (coincident) |

Standard form: $\frac{A_1}{A_2} = \frac{B_1}{B_2} \neq \frac{C_1}{C_2} \to 0$; all three equal $\to \infty$.

### One-Variable Equation Types
| Simplifies to | Solutions | Type |
|---|---|---|
| $x = c$ | 1 | Conditional |
| $0 = 0$ | Infinite | Identity |
| $0 = c$ ($c \neq 0$) | 0 | Contradiction |

### Inequality Rules
- ×/÷ by **negative** → **flip** the sign
- Solid boundary: $\leq, \geq$ | Dashed: $<, >$
- Shade **above** for $>/\geq$, **below** for $</\leq$
- Compound "and" = intersection; "or" = union

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

---

## B1.1 Linear Equations in One Variable

**What they test:** Solving $ax + b = c$ (and variants), determining solution type (unique/none/infinite), creating equations from word problems, interpreting constants in context.

### 1.1.1 Solving Standard Linear Equations

**Method:** Distribute → combine like terms → isolate variable.

**[Easy] Solve $3(x - 4) = 2x + 5$ for $x$.**

$3x - 12 = 2x + 5$ → $x = 17$

✅ **Check:** $3(17-4) = 39$, $2(17)+5 = 39$.

❌ **Trap:** $3x - 4 = 2x + 5 \to x = 9$ — **Distribution error** (forgot to multiply $-4$ by 3).

---

**[Medium] Solve $4(y + 1) - 3y = 2(y - 3) + 5$ for $y$.**

$4y + 4 - 3y = 2y - 6 + 5$ → $y = 5$

⚡ **Desmos check:** Graph $y_1 = 4(x+1)-3x$, $y_2 = 2(x-3)+5$. Intersection at $x = 5$.

---

**[Medium] Solve $\frac{3}{4}x - \frac{1}{2} = \frac{5}{8}$.**

Multiply by 8 (LCD): $6x - 4 = 5$ → $x = \frac{3}{2}$

❌ **Trap:** $6x - \frac{1}{2} = 5 \to x = \frac{11}{12}$ — **Partial multiplication** (only multiplied $x$ term by 8).

---

**[Medium] If $3(x - 2) + a = 5x - 6$ and $x = 4$, what is $a$?**

$3(4-2) + a = 5(4)-6$ → $6 + a = 14$ → $a = 8$

❌ **Trap:** Solving for $x$ instead of $a$ — **Wrong variable target**.

---

### 1.1.2 Identity, Conditional, and Contradiction

Every linear equation falls into one of three types:

| Type | Simplifies to | Solutions |
|---|---|---|
| **Conditional** | $x = c$ | Exactly 1 |
| **Identity** | $0 = 0$ or $5 = 5$ | All real numbers |
| **Contradiction** | $0 = 5$ or $3 = 7$ | None |

**Quick test:** Same $x$-coefficient + same constant → identity. Same coefficient + different constant → contradiction. Different coefficients → conditional.

**[Medium] How many solutions does $4(x - 3) + 8 = 4x - 4$ have?**

$4x - 12 + 8 = 4x - 4$ → $4x - 4 = 4x - 4$ → $0 = 0$. **Identity** — infinite solutions.

❌ **Trap:** "They cancel, no solution" — **Confusing identity with contradiction**. $x$ cancels AND constants match → infinite.

---

**[Hard] If $3(2x - 5) + k = 6x - 15$ has infinitely many solutions, what is $k$?**

$6x - 15 + k = 6x - 15$. For identity: $-15 + k = -15$ → $k = 0$.

---

**[Hard] $2(px + 3) = 4x + 6$. For what $p$ does the equation have (a) one solution? (b) no solution? (c) infinite solutions?**

$2px + 6 = 4x + 6$

(a) One solution when $2p \neq 4$, i.e., $p \neq 2$.
(b) No solution requires $2p = 4$ AND $6 \neq 6$ — impossible. **No such $p$.**
(c) Infinite when $2p = 4$ AND $6 = 6$, i.e., $p = 2$.

❌ **Trap:** Assuming every parameter can produce all three types — **The constant equality condition may already be decided**.

---

**[Very Hard] For what $c$ does $2(x - 3) + 5 = 2x + c$ have no solution?**

$2x - 6 + 5 = 2x + c$ → $2x - 1 = 2x + c$. $x$ coefficients match ($2 = 2$), so no solution when constants differ: any $c \neq -1$. If $c = -1$, infinite solutions.

---

### 1.1.3 Word Problems: Creating One-Variable Equations

Define the variable first, then translate the relationship.

**[Medium] A 200-liter mixture is $15\%$ salt. How many liters of pure water must be added to make it $10\%$ salt?**

Let $x$ = liters of water added. Salt before: $0.15(200) = 30$ L. Total after: $200 + x$ L.

$0.10(200 + x) = 30$ → $20 + 0.1x = 30$ → $x = 100$

❌ **Trap:** $0.15(200) + x = 0.10(200 + x)$ — **Treating water as if it contains salt**. Water adds volume but zero salt.

---

**[Medium] A train travels 300 miles at constant speed. If the speed were 10 mph faster, the trip would take 1 hour less. Find the original speed.**

Let $r$ = original speed. Time: $\frac{300}{r}$; time at $r+10$: $\frac{300}{r+10}$.

$\frac{300}{r} - \frac{300}{r+10} = 1$ → $300(r+10) - 300r = r(r+10)$ → $r^2 + 10r - 3000 = 0$ → $(r+60)(r-50) = 0$ → $r = 50$ mph

❌ **Trap:** $\frac{240}{r} = \frac{240}{r+10} + 1$ — **Inverse subtraction**. Faster trip takes less time → shorter time + 1 = longer time.

---

**[Hard] Jack is twice as old as Jill. In 12 years, the sum of their ages will be 75. How old is Jill now?**

Let $x$ = Jill's age. Jack = $2x$. In 12 years: Jill = $x+12$, Jack = $2x+12$.

$(x+12) + (2x+12) = 75$ → $3x = 51$ → $x = 17$

❌ **Trap:** Adding 12 to Jack but forgetting to add 12 to Jill — **Asymmetric future ages**.

---

**[Hard] A chemist has 40 mL of $25\%$ acid solution. How many mL of pure acid must be added to create $40\%$ acid?**

Let $x$ = mL pure acid. Acid before: $0.25(40) = 10$ mL. Total after: $40+x$ mL. Acid after: $10+x$ mL.

$0.40(40+x) = 10+x$ → $16 + 0.4x = 10 + x$ → $x = 10$

❌ **Trap:** $0.40(40+x) = 10$ — **Forgetting added acid increases the acid amount, not just volume**. Right side must be $10+x$.

---

### 1.1.4 Parameter and Constant Interpretation

The constant term = value of the dependent variable when the independent variable = 0.

**[Medium] $C = 5n + 200$ models production cost for $n$ widgets. What does 200 represent?**

Cost when $n = 0$: fixed costs (equipment, rent).

❌ **Trap:** "Cost per widget" — **Confusing intercept with slope**. The 5 is per-unit; 200 is fixed.

---

**[Hard] $p = 50 - 0.2q$ models price $p$ at which $q$ units sell. Interpret 50.**

When $q = 0$, $p = 50$: the price when no units are sold (maximum price).

❌ **Trap:** "Maximum number of units" — **Reading a zero-output as an input constraint**. The $q$-intercept (where $p = 0$) gives max quantity.

---

## B1.2 Linear Functions

**What they test:** $f(x) = mx + b$, point-slope form, interpreting slope and intercept in context, writing equations from two points or point + rate, connecting tables/graphs/algebra.

### 1.2.1 Function Notation and Evaluation

$f(x)$ is output at input $x$. For $f(x) = mx + b$, $m$ = slope, $b$ = $y$-intercept.

**[Easy] If $f(x) = 3x - 5$, find $f(4)$.** → $f(4) = 3(4) - 5 = 7$

**[Medium] If $f(x) = 2x + 1$ and $f(a) = 17$, find $a$.** → $2a + 1 = 17$ → $a = 8$

**[Medium] If $f(2) = 5$ and $f(6) = 13$, find $f(x)$.**

$m = \frac{13-5}{6-2} = 2$. $f(x) = 2x + b$; $5 = 2(2) + b$ → $b = 1$. $f(x) = 2x + 1$.

❌ **Trap:** $f(2) = 5$ means $b = 5$ — **Intercept = $f(0)$, not $f(2)$**.

---

### 1.2.2 Slope and Rate of Change

$m = \frac{y_2 - y_1}{x_2 - x_1}$. Units of $m$ = (units of $y$) per (unit of $x$).

**[Medium] The table shows a linear relationship:**

| $x$ | 1 | 3 | 5 |
|---|---|---|---|
| $y$ | 7 | 15 | 23 |

$m = \frac{15-7}{3-1} = 4$. $7 = 4(1) + b$ → $b = 3$. $f(x) = 4x + 3$.

✅ **Check:** $f(5) = 4(5) + 3 = 23$. Matches table.

❌ **Trap:** Reading $b = 7$ from the first row — **$b$ is $f(0)$, not the first $y$ in the table**. Compute it.

---

**[Hard] The average rate of change of a linear function $f$ between $x=2$ and $x=5$ is 3. If $f(2) = 8$, find $f(7)$.**

For linear functions, rate of change = slope everywhere. $m = 3$. $f(x) = 3x + b$; $8 = 3(2) + b$ → $b = 2$. $f(7) = 3(7) + 2 = 23$.

❌ **Trap:** Thinking rate of change depends on interval — **Linear functions have constant rate**.

---

### 1.2.3 Point-Slope and Writing Equations

| Given | Use |
|---|---|
| Slope $m$, $y$-int $b$ | $y = mx + b$ |
| Slope $m$, point $(x_1,y_1)$ | $y - y_1 = m(x - x_1)$ |
| Two points | Find $m$, then point-slope |

**[Medium] Line with slope $-2$ through $(3, 8)$.**

$y - 8 = -2(x - 3)$ → $y = -2x + 14$

❌ **Trap:** $y = -2x + 8$ — **Plugging $b$ as the $y$-value of any point**. $y$-intercept is at $x = 0$.

---

**[Hard] Line through $(2, -3)$ and $(-4, 9)$.**

$m = \frac{9-(-3)}{-4-2} = \frac{12}{-6} = -2$. Using $(2,-3)$: $y+3 = -2(x-2)$ → $y = -2x + 1$.

✅ **Check:** $(-4,9)$: $-2(-4) + 1 = 9$. ✔

---

**[Medium] Equation of line with $x$-int 4 and $y$-int $-2$?**

Points: $(4,0)$ and $(0,-2)$. $m = \frac{-2-0}{0-4} = \frac{1}{2}$, $b = -2$. $y = \frac{1}{2}x - 2$.

❌ **Trap:** $y = \frac{1}{2}x + 2$ — **Sign error on $y$-intercept**.

---

### 1.2.4 Interpreting Slope and Intercept in Context

**[Medium] $C = 0.35m + 45$ models car rental cost for $m$ miles. Interpret.**

$0.35$: cost per mile. $45$: flat fee (cost at 0 miles).

❌ **Trap:** Swapping them — **Slope is a rate; intercept is a fixed amount**.

---

**[Medium] $V = 25000 - 3000t$ models machine value after $t$ years. Interpret.**

$-3000$: annual depreciation. $25000$: initial value.

❌ **Trap:** "The machine loses $3000$ total" — **Annual vs. total depreciation confusion**.

---

**[Hard] Balloon height $h(t) = 300 - 4.9t^2$. Is this linear?**

No — quadratic. The SAT may embed a non-linear equation in a "linear" context to test recognition.

---

### 1.2.5 Connected Representations (Table, Equation, Graph)

**[Medium] Which function matches the table?**

| $x$ | 0 | 2 | 4 |
|---|---|---|---|
| $f(x)$ | -3 | 5 | 13 |

$m = \frac{5-(-3)}{2-0} = 4$. $f(0) = -3$ → $b = -3$. $f(x) = 4x - 3$.

❌ **Trap:** $m = 2$ by counting $x\to y$ as 1-step ratio — **$x$ changed by 2, $y$ by 8, so $m = 8/2 = 4$**.

---

**[Hard] Graph passes through $(0,4)$ and $(3,10)$. Define $f$.**

$m = \frac{10-4}{3-0} = 2$, $b = 4$. $f(x) = 2x + 4$.

❌ **Trap:** $m = 6$ — **Using run (3) as slope instead of rise/run**.

---

**[Hard] Which graph represents $f(-2) = -1$ and $f(4) = 5$?**

$m = \frac{5-(-1)}{4-(-2)} = 1$; $f(x) = x + b$; $5 = 4 + b$ → $b = 1$. Line through $(0,1)$ with slope 1.

❌ **Trap:** Picking a graph with correct points but wrong $y$-intercept — **$y$-intercept must be 1**.

---

### 1.2.6 Linear Models in Context

**[Medium] Bacteria: 500 cells, grows 120/hr. Population after $t$ hours?**

$P(t) = 120t + 500$. $P(8) = 120(8) + 500 = 1460$.

---

**[Hard] Temperature $T = 85 - 4m$ (degrees Celsius after $m$ minutes). When does $T = 25$?**

$25 = 85 - 4m$ → $m = 15$ minutes

❌ **Trap:** Solving $85 - 4m = 0$ — **Wrong target. Question asks $T=25$, not $T=0$**.

---

**[Very Hard] Population $P(t) = 2000 + 150t$, $t$ = years since 2020. When does it reach 5000?**

$5000 = 2000 + 150t$ → $t = 20$ → Year: $2020 + 20 = 2040$

❌ **Trap:** Answering $t = 20$ when question asks for the year — **Always re-read what's being asked**.

---

## B1.3 Linear Equations in Two Variables

**What they test:** $Ax + By = C$, converting between forms, parallel/perpendicular lines, interpreting intercepts in context.

### 1.3.1 Forms of Linear Equations

| Form | Equation | Key Use |
|---|---|---|
| Slope-intercept | $y = mx + b$ | Read slope and $y$-int directly |
| Point-slope | $y - y_1 = m(x - x_1)$ | From a point and slope |
| Standard | $Ax + By = C$ | Intercepts, solving systems |
| Intercept | $\frac{x}{a} + \frac{y}{b} = 1$ | Read $x$- and $y$-intercepts directly |

**Standard → slope-intercept:** $y = -\frac{A}{B}x + \frac{C}{B}$

**[Easy] Convert $3x + 4y = 12$ to $y = mx + b$.**

$4y = -3x + 12$ → $y = -\frac{3}{4}x + 3$

❌ **Trap:** $y = 3x + 12$ — **Dividing only the $x$ term by 4**. Every term must be divided.

---

**[Medium] Line $2x + 3y = 6$. Find slope and both intercepts.**

$m = -\frac{A}{B} = -\frac{2}{3}$. $y$-int ($x=0$): $3y=6$ → $y=2$. $x$-int ($y=0$): $2x=6$ → $x=3$.

✅ **Check:** Intercept form $\frac{x}{3} + \frac{y}{2} = 1$ confirms $(3,0)$ and $(0,2)$.

---

### 1.3.2 Parallel and Perpendicular Lines

**Parallel:** $m_1 = m_2$. **Perpendicular:** $m_1 \cdot m_2 = -1$ (flip fraction, change sign).

| Slope | Perpendicular |
|---|---|
| $\frac{2}{3}$ | $-\frac{3}{2}$ |
| $-4 = -\frac{4}{1}$ | $\frac{1}{4}$ |
| $0$ (horizontal) | undefined (vertical) |

**[Medium] Line $l$: $2x - 3y = 6$. Slope of parallel? Perpendicular?**

$y = \frac{2}{3}x - 2$. Parallel: $\frac{2}{3}$. Perpendicular: $-\frac{3}{2}$.

❌ **Trap:** $-\frac{2}{3}$ for perpendicular — **Flipping sign without reciprocating**.

---

**[Medium] Perpendicular to $y = \frac{1}{2}x - 3$?**

Perpendicular slope = $-2$. Answer: $y = -2x + 5$.

❌ **Trap:** $-\frac{1}{2}$ — **Sign flip without reciprocal** (or reciprocal without flip).

---

**[Hard] Line through $(1,5)$ perpendicular to $y = -\frac{3}{4}x + 2$.**

Perpendicular slope: $\frac{4}{3}$. $y - 5 = \frac{4}{3}(x-1)$ → $y = \frac{4}{3}x + \frac{11}{3}$

❌ **Trap:** Using $-\frac{4}{3}$ (sign flip only) or $-\frac{3}{4}$ (parallel) — **Wrong slope relationship**.

---

**[Hard] For what $k$ is $kx + 2y = 8$ perpendicular to $y = \frac{1}{3}x + 4$?**

$m_1 = -\frac{k}{2}$, $m_2 = \frac{1}{3}$. Perpendicular: $(-\frac{k}{2})(\frac{1}{3}) = -1$ → $k = 6$

❌ **Trap:** Setting $-\frac{k}{2} = \frac{1}{3}$ — **Parallel condition. Perpendicular requires product $= -1$**.

---

### 1.3.3 Intercepts from Standard Form

Given $Ax + By = C$: $x$-int = $\frac{C}{A}$ (set $y=0$), $y$-int = $\frac{C}{B}$ (set $x=0$).

**[Easy] $5x - 2y = 20$: find both intercepts.**

$x$-int: $5x = 20$ → $x = 4$. $y$-int: $-2y = 20$ → $y = -10$.

❌ **Trap:** $y = 10$ — **Sign error from $-2y$**.

---

**[Medium] Line has $x$-int $-3$, $y$-int $6$. Write in standard form.**

$\frac{x}{-3} + \frac{y}{6} = 1$ → multiply by 6: $-2x + y = 6$ → $2x - y = -6$

✅ **Check:** $y=0$ → $2x = -6$ → $x=-3$. $x=0$ → $-y = -6$ → $y=6$. ✔

---

### 1.3.4 Graphs and Solutions in Context

**[Medium] $4x + 6y = 120$: adult ($4) and child ($6) tickets for $120 revenue. What does $x$-intercept mean?**

Set $y=0$: $4x = 120$ → $x = 30$. If no child tickets sold, 30 adult tickets generate $120.

---

**[Hard] $800x + 1200y = 240000$: two programs. What does $y$-intercept mean?**

Set $x=0$: $1200y = 240000$ → $y = 200$. Program B students if no money goes to Program A.

❌ **Trap:** "The total budget" — **$C$ is the budget; $C/B$ is a variable value when $x=0$**.

---

**[Very Hard] 120m of fencing for a rectangular pen, one side is a river (no fencing). Model area $A$ as function of width $w$.**

$w$ = width (perpendicular to river), $l$ = length (parallel). $2w + l = 120$ → $l = 120 - 2w$. $A = w(120-2w) = 120w - 2w^2$ (quadratic from linear constraint).

❌ **Trap:** $l = 120 - w$ — **Only three sides need fencing, not four**.

---

## B1.4 Systems of Two Linear Equations

> **Cross-domain:** Systems involving non-linear equations (quadratic-linear, exponential-linear) are covered in B2 (Advanced Math). See B2 §2.8–§2.9 for polynomial and exponential systems.

**What they test:** Substitution, elimination, Desmos intersection method, determining solution count via slopes, modeling real-world constraints.

### 1.4.1 Solving Methods

| Method | When to Use | How |
|---|---|---|
| Substitution | One variable isolated or easy to isolate | Replace that variable in the other eq |
| Elimination | Same coefficient (or easy to match) on one variable | Add/subtract to cancel that variable |
| Desmos | Any system (especially messy numbers) | Graph both, click intersection |

#### Substitution

**[Easy] $y = 3x - 4$ and $2x + y = 11$.**

$2x + (3x - 4) = 11$ → $5x = 15$ → $x = 3$, $y = 5$

❌ **Trap:** $2x + 3x - 4 = 11$ → $x - 4 = 11$ — **Combining like terms incorrectly**.

---

**[Medium] $3x + 2y = 14$ and $x - y = 3$.**

$x = y+3$ → $3(y+3) + 2y = 14$ → $y = 1$, $x = 4$

---

#### Elimination

**[Medium] $2x + 3y = 7$ and $2x + 5y = 9$.**

$(2x+5y) - (2x+3y) = 9 - 7$ → $2y = 2$ → $y = 1$, $x = 2$

❌ **Trap:** Correct subtraction on left but $9 + 7 = 16$ on right — **Inconsistent operation**.

---

**[Hard] $3x - 4y = 10$ and $5x + 2y = 8$.**

Multiply second by 2: $10x + 4y = 16$. Add: $13x = 26$ → $x = 2$, $y = -1$.

❌ **Trap:** $10x + 2y = 8$ — **Partial multiplication** (only multiplied $x$ term by 2).

---

**[Hard] $2x + 3y = 12$ and $5x - 2y = 11$.**

First ×2: $4x + 6y = 24$. Second ×3: $15x - 6y = 33$. Add: $19x = 57$ → $x = 3$, $y = 2$.

❌ **Trap:** $15x - 2y = 33$ — **Partial scaling** (only multiplied $x$ term by 3).

---

#### Desmos

For any system, type both equations into Desmos. The intersection point is the solution.

**[Hard] $4.7x + 2.3y = 15.1$ and $1.8x - 3.2y = 4.6$.**

Intersection ≈ $(3.07, 0.29)$. 15 seconds in Desmos vs. 2-3 minutes algebraically.

---

**[Medium] $2x + 3y = 10$ and $x - y = 5$. Find $x + y$.**

$x = y+5$ → $2(y+5) + 3y = 10$ → $y = 0$, $x = 5$. $x+y = 5$.

⚡ The test often asks for $x+y$ or $x-y$, not individual values. Always re-read.

---

### 1.4.2 Number of Solutions

| Slopes | Intercepts | Solutions |
|---|---|---|
| $m_1 \neq m_2$ | Any | Exactly 1 |
| $m_1 = m_2$ | $b_1 \neq b_2$ | 0 (parallel) |
| $m_1 = m_2$ | $b_1 = b_2$ | Infinite (coincident) |

Standard form: $\frac{A_1}{A_2} = \frac{B_1}{B_2} \neq \frac{C_1}{C_2}$ → 0. All three equal → infinite.

**[Medium] $3x + 6y = 12$ and $x + 2y = 4$: how many solutions?**

First ÷3: $x + 2y = 4$. Identical to second → infinite.

❌ **Trap:** Saying "no solution" because right sides differ at a glance — **Must check proportionality**.

---

**[Hard] For what $k$ does $4x + ky = 8$ and $2x - 3y = 5$ have no solution?**

Eq1: $y = -\frac{4}{k}x + \frac{8}{k}$ ($k \neq 0$). Eq2: $y = \frac{2}{3}x - \frac{5}{3}$.

Slopes equal: $-\frac{4}{k} = \frac{2}{3}$ → $k = -6$. Intercepts: $\frac{8}{-6} = -\frac{4}{3} \neq -\frac{5}{3}$. Parallel → $k = -6$.

❌ **Trap:** $k = 6$ — **Sign error** in $-\frac{4}{k} = \frac{2}{3}$.

---

**[Hard] For what $k$ does $2x + 3y = 6$ and $4x + 6y = k$ have infinite solutions?**

Proportional: $\frac{2}{4} = \frac{3}{6} = \frac{6}{k}$ → $\frac{1}{2} = \frac{6}{k}$ → $k = 12$

❌ **Trap:** $k = 6$ — **Partial check. Must include constant ratio: $6/k = 1/2$**.

---

**[Very Hard] $ax + by = 4$ and $2x + 3y = 8$ have infinite solutions. Find $a + b$.**

$\frac{a}{2} = \frac{b}{3} = \frac{4}{8} = \frac{1}{2}$ → $a = 1$, $b = 1.5$ → $a + b = 2.5$

❌ **Trap:** Setting $a/2 = 4/8$ but forgetting $b/3$ — **Partial proportionality check**. All three ratios must equal.

---

### 1.4.3 Word Problems with Systems

**[Medium] Sum of two numbers is 28. Twice the first minus the second is 17. Find them.**

$x + y = 28$, $2x - y = 17$. Add: $3x = 45$ → $x = 15$, $y = 13$.

❌ **Trap:** Writing $2x + y = 17$ — **Misreading subtraction as addition**.

---

**[Hard] Baker sells loaves ($4) and pastries ($2). Sold 60 items, earned $180. How many loaves?**

$L + P = 60$, $4L + 2P = 180$. First ×2: $2L + 2P = 120$. Subtract: $2L = 60$ → $L = 30$.

❌ **Trap:** $4L + 2P = 60$ — **Confusing item count with revenue**.

---

**[Hard] Mix 12% acid with 20% acid to get 500 mL of 15%. How much of each?**

$x$ = mL of 12%, $y$ = mL of 20%. $x + y = 500$, $0.12x + 0.20y = 75$.

Multiply second by 100: $12x + 20y = 7500$. First ×12: $12x + 12y = 6000$. Subtract: $8y = 1500$ → $y = 187.5$, $x = 312.5$.

❌ **Trap:** $0.12x + 0.20y = 500$ — **Right side = pure acid ($75$), not total volume ($500$)**.

---

**[Very Hard] Product A needs 2h machine + 3h labor. Product B needs 4h machine + 1h labor. Available: 80 machine hours, 60 labor hours.**

$a$ = units of A, $b$ = units of B.

Machine: $2a + 4b = 80$. Labor: $3a + b = 60$.

$b = 60 - 3a$ → $2a + 4(60-3a) = 80$ → $-10a = -160$ → $a = 16$, $b = 12$

---

## B1.5 Linear Inequalities

**What they test:** Solving single inequalities (flip sign for negative multiplication/division), compound inequalities, graphing with solid/dashed lines and shading, systems of inequalities.

### 1.5.1 Solving Single Linear Inequalities

Solve like equations, but **×/÷ by a negative flips the inequality sign**.

**[Easy] $2x + 5 > 13$** → $2x > 8$ → $x > 4$

❌ **Trap:** $x < 4$ — **Flipping unnecessarily. Only flip for negative ×/÷**.

---

**[Medium] $-3x + 7 \leq 22$** → $-3x \leq 15$ → $x \geq -5$ (flip)

❌ **Trap:** $x \leq -5$ — **Forgetting to flip when dividing by negative**.

---

**[Medium] $4 - 2x > 10$** → $-2x > 6$ → $x < -3$ (flip)

---

**[Hard] $\frac{2x - 5}{3} \leq \frac{x + 4}{2}$**

Multiply by 6: $2(2x-5) \leq 3(x+4)$ → $4x - 10 \leq 3x + 12$ → $x \leq 22$

❌ **Trap:** $2x-5 \leq x+4$ → $x \leq 9$ — **Dropping denominators. Multiply by LCD**.

---

### 1.5.2 Compound Inequalities

**[Medium] $-5 < 2x + 1 < 7$**

Subtract 1: $-6 < 2x < 6$. Divide: $-3 < x < 3$.

❌ **Trap:** Solving only one side ($2x+1 < 7 \to x < 3$) — **Both inequalities must be satisfied**.

---

**[Hard] $3x - 7 \leq 5$ or $2x + 1 > 11$**

First: $x \leq 4$. Second: $x > 5$. Solution: $x \leq 4$ or $x > 5$.

❌ **Trap:** Treating "or" as "and" → presenting $4 < x \leq 5$ (empty set).

---

**[Hard] $2 < 3x + 5 \leq 14$**

Subtract 5: $-3 < 3x \leq 9$. Divide: $-1 < x \leq 3$.

❌ **Trap:** Subtracting 5 from middle only — **Operation must apply to ALL three parts**.

---

### 1.5.3 Graphing Linear Inequalities

| Feature | Solid | Dashed |
|---|---|---|
| Used for | $\leq, \geq$ | $<, >$ |
| Boundary included | Yes | No |
| Shading | Above for $>/\geq$, below for $</\leq$ |

**Test point:** Pick $(0,0)$ unless it lies on the boundary. If it satisfies, shade that side.

**[Medium] Graph $y > 2x - 3$.** Dashed line, shade above. $(0,0)$: $0 > -3$ true → shade side containing origin.

**[Medium] Graph $3x + 2y \leq 6$.** $y \leq -\frac{3}{2}x + 3$. Solid line, shade below. $(0,0)$: $0 \leq 6$ true.

❌ **Trap:** Shading above when $y \leq$ — **Reversing shading direction**.

---

### 1.5.4 Systems of Inequalities

**[Medium] Which point satisfies both $y < 2x + 1$ and $y \geq -x + 3$?**

A) $(0,0)$: $0 < 1$ ✓, $0 \geq 3$ ✗. B) $(1,4)$: $4 < 3$ ✗. C) $(2,1)$: $1 < 5$ ✓, $1 \geq 1$ ✓. **Answer: C.**

❌ **Trap:** Checking only one inequality — **A point must satisfy ALL inequalities**.

---

**[Hard] Company makes two products. A needs 2h labor, B needs 3h. At most 60h/week. At least 10 total products/week.**

$a$ = units of A, $b$ = units of B.

$2a + 3b \leq 60$, $a + b \geq 10$, $a \geq 0$, $b \geq 0$

✅ **Always include non-negativity** for real-world quantities.

---

**[Hard] Scores 82 and 76 on two tests. What third score gives average $\geq 80$?**

$\frac{82 + 76 + x}{3} \geq 80$ → $158 + x \geq 240$ → $x \geq 82$

❌ **Trap:** Using $>$ instead of $\geq$ — **"At least" means $\geq$, not $>$**.

---

**[Hard] Parking: $5 first hour, $3 each additional hour, max $20/day. Inequality for hours $h$?**

Cost = $5 + 3(h-1)$ for $h \geq 1$. $5 + 3(h-1) \leq 20$ → $h \leq 6$. Solution: $1 \leq h \leq 6$.

❌ **Trap:** $3h + 5$ — **First hour costs $5$, remaining $(h-1)$ hours cost $3$ each**.

---

**[Very Hard] Which region represents $y \leq 2x - 3$ and $y > -x + 4$?**

Graph both in Desmos:
- $y \leq 2x - 3$: solid line, shade below
- $y > -x + 4$: dashed line, shade above

Intersection: $2x - 3 = -x + 4$ → $x = \frac{7}{3}$, $y = \frac{5}{3}$. Solution is overlapping shaded region.

⚡ Type both inequalities directly with `<=` and `>`; Desmos shades automatically.

---

## B1.6 Additional Algebra Topics

### 1.6.1 Absolute Value Equations

**Method:** Isolate $|A|$, split into $A = b$ and $A = -b$, solve both, check.

**[Easy] $|x - 5| = 3$** → $x - 5 = 3$ or $x - 5 = -3$ → $x = 8, 2$

**[Medium] $|2x + 1| = 7$** → $2x+1 = 7$ or $2x+1 = -7$ → $x = 3, -4$

❌ **Trap:** Only solving one case — **Absolute value equations almost always have two solutions**.

---

**[Medium] $3|x - 4| + 2 = 20$**

Isolate: $3|x-4| = 18$ → $|x-4| = 6$ → $x = 10, -2$

❌ **Trap:** $3x - 12 + 2 = 20$ — **Distributing into the absolute value**. Isolate $|x-4|$ first.

---

**[Hard] $|x + 5| = -3$** → **No solution.** Absolute value cannot equal a negative.

❌ **Trap:** Writing $x+5 = -3$ or $x+5 = 3$ — **Check sign before splitting**.

---

**[Hard] $|2x - 3| = |x + 4|$**

Case 1 (same signs): $2x - 3 = x+4$ → $x = 7$. Case 2 (opposite signs): $2x - 3 = -(x+4)$ → $x = -\frac{1}{3}$.

❌ **Trap:** Only solving Case 1 — **Must also consider opposite signs**.

---

**Absolute Value Inequalities**

$|A| < b$ ($b>0$) → $-b < A < b$ (less th**and**)
$|A| > b$ ($b>0$) → $A < -b$ or $A > b$ (**great**or)

**[Medium] $|x - 3| < 5$** → $-5 < x-3 < 5$ → $-2 < x < 8$

**[Medium] $|2x + 1| \geq 9$** → $2x+1 \leq -9$ or $2x+1 \geq 9$ → $x \leq -5$ or $x \geq 4$

---

### 1.6.2 Literal Equations (Solving for a Variable)

**Method:** Identify target, treat other variables as constants, apply inverse operations (clear denominators first).

**[Easy] $A = lw$ for $w$** → $w = A/l$

**[Medium] $P = 2l + 2w$ for $l$** → $l = \frac{P - 2w}{2}$ (or $\frac{P}{2} - w$)

❌ **Trap:** $l = P - 2w$ — **Forgetting to divide by 2**.

---

**[Hard] $S = \frac{n}{2}(a + l)$ for $a$** → $2S = n(a+l)$ → $a = \frac{2S}{n} - l$

❌ **Trap:** Distributing before clearing fraction — adds steps and error risk. Clear denominators first.

---

**[Hard] $\frac{1}{R} = \frac{1}{r_1} + \frac{1}{r_2}$ for $r_1$**

Multiply by $R r_1 r_2$: $r_1 r_2 = R r_2 + R r_1$ → $r_1(r_2 - R) = R r_2$ → $r_1 = \frac{R r_2}{r_2 - R}$

❌ **Trap:** $r_1 = R - r_2$ — **Treating reciprocals as simple addition**.

---

**[Very Hard] $y = \frac{2x + 3}{x - 1}$ for $x$**

$y(x-1) = 2x+3$ → $xy - y = 2x+3$ → $x(y-2) = y+3$ → $x = \frac{y+3}{y-2}$

❌ **Trap:** Forgetting to collect $x$ terms when $x$ appears on both sides — must factor.

---

### 1.6.3 Direct and Inverse Variation

**Direct:** $y = kx$ (constant ratio $y/x = k$, line through origin)
**Inverse:** $y = k/x$ or $xy = k$ (constant product)

**[Easy] $y$ varies directly with $x$. $y=12$ when $x=3$. Find $y$ when $x=7$.**

$12 = k(3)$ → $k = 4$. $y = 4(7) = 28$.

**[Medium] $y$ varies inversely with $x$. $y=6$ when $x=4$. Find $y$ when $x=8$.**

$6 \cdot 4 = k \to k = 24$. $y = \frac{24}{8} = 3$.

❌ **Trap:** $y = -kx$ — **"Inverse" means multiplicative inverse ($1/x$), not negative**.

---

**[Medium] Spring stretch varies directly with weight. 5kg → 8cm. 12kg → ?**

$d = kw$: $8 = k(5)$ → $k = 1.6$. $d = 1.6(12) = 19.2$ cm.

---

**[Hard] Light intensity varies inversely with $d^2$. 20 units at 3m. Intensity at 6m?**

$I = \frac{k}{d^2}$: $20 = \frac{k}{9}$ → $k = 180$. $I = \frac{180}{36} = 5$ units.

❌ **Trap:** Using $I = k/d$ instead of $k/d^2$ — **Ignoring the power**.

---

**[Hard] Does this table show direct or inverse variation?**

| $x$ | 2 | 4 | 6 | 8 |
|---|---|---|---|---|
| $y$ | 12 | 6 | 4 | 3 |

$xy = 24$ constant → inverse variation ($y = 24/x$).

❌ **Trap:** $y$ decreases as $x$ increases → assuming inverse without checking — **Must verify $xy$ is constant**.

---

### 1.6.4 Piecewise Linear Functions

**[Medium] $f(x) = \begin{cases} 2x+1, & x<3 \\ -x+10, & x \geq 3 \end{cases}$. Find $f(3)$.**

$3 \geq 3$, use second piece: $f(3) = -3 + 10 = 7$

❌ **Trap:** Using first piece because 3 is "close to 2" — **Check the condition, don't guess**.

---

**[Medium] $f(x) = \begin{cases} 3x-2, & x \leq 1 \\ x+4, & x > 1 \end{cases}$. Find $f(-2) + f(5)$.**

$f(-2) = 3(-2)-2 = -8$. $f(5) = 5+4 = 9$. Sum = 1.

---

**[Hard] Parking garage: $10 first hour, $5 each additional (or fraction), max $30/day. Write $f(h)$.**

$f(h) = \begin{cases} 10, & 0 < h \leq 1 \\ 10 + 5(h-1), & 1 < h \leq 5 \\ 30, & h > 5 \end{cases}$

❌ **Trap:** $10 + 5h$ for second piece — **First hour costs $10$, not $5$**.

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

### Category 3: Setup & Interpretation Errors

| # | Mistake | Why |
|---|---|---|
| 11 | **Wrong variable target** | Found $x$, question asks for $2x+1$ |
| 12 | **Confusing count with cost** | $4L+2P = 60$ (cost = item count) |
| 13 | **Swapping fixed and variable costs** | $C(d) = 3.50d + 2$ |
| 14 | **Forgetting non-negativity** | Real-world quantities can't be negative |
| 15 | **Misreading intercept meaning** | $y$-int = total budget (it's value at $x=0$) |

### Category 4: Calculation Errors

| # | Mistake | Wrong | Correct |
|---|---|---|---|
| 16 | **Inverted slope** | $\frac{x_2-x_1}{y_2-y_1}$ | $\frac{y_2-y_1}{x_2-x_1}$ |
| 17 | **Perpendicular: sign only** | $\frac{2}{3} \to -\frac{2}{3}$ | $\to -\frac{3}{2}$ |
| 18 | **Partial compound solving** | $-5<2x+1<7 \to x<3$ | $-3 < x < 3$ |
| 19 | **Sign error in elimination** | Add when should subtract | Subtract to cancel same-sign terms |
| 20 | **Dividing only one term** | $\frac{3x+6}{3} = x+6$ | $x+2$ |

### Category 5: Test-Day Strategy Errors

| # | Mistake | Fix |
|---|---|---|
| 21 | **Using Desmos for everything** | Decide in 10s: algebra, Desmos, or backsolving |
| 22 | **Not re-reading final quantity** | Find $x$ when question asks $x+y$ |
| 23 | **Not backsolving for multiple choice** | Plug answer choices instead of solving |
| 24 | **Forgetting Desmos for systems** | 15s in Desmos vs 2+ minutes algebra |
| 25 | **Not checking axis scaling** | Graph intercepts may be at unexpected positions |

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

[Very Hard] Car worth $24,000$ after 2 years, $12,000$ after 6. Initial value? → $m = -3000$, $V(t) = -3000t + 30000$, initial $= \$30,000$

---

### Set 4: Inequalities

[Easy] $4x - 7 > 9$ → $x > 4$

[Medium] $-2x + 5 \leq 13$ → $-2x \leq 8$ → $x \geq -4$

[Hard] $3 \leq 2x - 1 < 9$ → $4 \leq 2x < 10$ → $2 \leq x < 5$

[Very Hard] Sell widgets at $12 each. Cost $C = 5w + 200$. Profit $\geq 400$? → $12w - (5w+200) \geq 400$ → $7w \geq 600$ → $w \geq 86$ (whole units)

---

**Before moving on:** ✅ Defined the variable? ✅ Re-read the question? ✅ Sign correct? ✅ Answer makes sense? ✅ Right units?
