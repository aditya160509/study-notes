# 📘 Chapter 1: Algebra - 9709 Pure Mathematics 2&3 (CAIE A Level Maths)

## Cambridge International AS & A Level Mathematics (9709) - Paper 3

> **Rule + fully solved examples.** Every technique shown step by step in proper LaTeX, every algebra step on its own line.

---

# PART 1: Algebra (Chapter 1)

**Covers:** the modulus function $|x|$, solving $|ax+b| = k$ and $|ax+b| = |cx+d|$, sketching $y = |f(x)|$, $y = f(|x|)$ and $y = \frac{1}{f(x)}$, polynomial long division, and the factor and remainder theorems with finding unknown coefficients.

## 1.1 The Modulus Function

The **modulus** (or absolute value) of a number is its magnitude without sign. Written $|x|$, defined as:

$$|x| = \begin{cases} x & \text{if } x \geq 0 \\ -x & \text{if } x < 0 \end{cases}$$

So $|3| = 3$ and $|-3| = 3$. The modulus is always non-negative.

Key property for solving equations:

$$|x| = k \quad (k \geq 0) \iff x = k \text{ or } x = -k$$

More generally, for equations of the form $|ax + b| = |cx + d|$, use:

$$|a| = |b| \iff a^2 = b^2 \iff a = b \text{ or } a = -b$$

> ⭐ **Watch Out!** When solving $|ax+b| = |cx+d|$ you get TWO linear equations to solve ($ax+b = cx+d$ and $ax+b = -(cx+d)$). You must **check** both solutions in the original equation — squaring can introduce extraneous roots, and with harder modulus equations some algebraic solutions fail the check.

### Example 1 - Easy - basic modulus evaluation and $|ax+b| = k$

> **Question:** (a) Evaluate $|{-7}|$ and $|5|$. (b) Solve $|2x - 1| = 3$.

**Solution:**

(a) By definition:

$$|{-7}| = -(-7) = 7$$

$$|5| = 5$$

(b) $|2x - 1| = 3$ means $2x - 1 = 3$ or $2x - 1 = -3$:

$$2x - 1 = 3$$

$$2x = 4$$

$$x = 2$$

or

$$2x - 1 = -3$$

$$2x = -2$$

$$x = -1$$

Check: $|2(2)-1| = |3| = 3 \checkmark$ and $|2(-1)-1| = |-3| = 3 \checkmark$.

$$x = -1 \text{ or } x = 2 \quad\checkmark$$

**What the examiner wants:** both branches written out, both solutions checked.

### Example 2 - Medium - solving $|ax+b| = |cx+d|$ (coursebook Worked example 1.1b / 1.2)

> **Question:** Solve $|x - 4| = |2x + 1|$.

**Solution:**

Use $|a| = |b| \iff a = b$ or $a = -b$:

Case 1: $x - 4 = 2x + 1$

$$x - 4 = 2x + 1$$

$$-4 - 1 = 2x - x$$

$$x = -5$$

Case 2: $x - 4 = -(2x + 1)$

$$x - 4 = -2x - 1$$

$$x + 2x = -1 + 4$$

$$3x = 3$$

$$x = 1$$

Check $x = -5$: $|{-5}-4| = |-9| = 9$ and $|2(-5)+1| = |-9| = 9 \checkmark$.

Check $x = 1$: $|1-4| = |-3| = 3$ and $|2(1)+1| = |3| = 3 \checkmark$.

$$x = -5 \text{ or } x = 1 \quad\checkmark$$

**What the examiner wants:** both linear equations solved cleanly, solutions verified in the original modulus equation.

### Example 3 - Medium - solving $|3x + 4| = |x - 2|$ with verification

> **Question:** Solve $|3x + 4| = |x - 2|$.

**Solution:**

Case 1: $3x + 4 = x - 2$

$$3x + 4 = x - 2$$

$$3x - x = -2 - 4$$

$$2x = -6$$

$$x = -3$$

Case 2: $3x + 4 = -(x - 2)$

$$3x + 4 = -x + 2$$

$$3x + x = 2 - 4$$

$$4x = -2$$

$$x = -\frac{1}{2}$$

Check $x = -3$: $|3(-3)+4| = |-5| = 5$ and $|-3-2| = |-5| = 5 \checkmark$.

Check $x = -\frac{1}{2}$: $|3(-\frac{1}{2})+4| = |\frac{5}{2}| = \frac{5}{2}$ and $|-\frac{1}{2}-2| = |-\frac{5}{2}| = \frac{5}{2} \checkmark$.

$$x = -3 \text{ or } x = -\frac{1}{2} \quad\checkmark$$

**What the examiner wants:** the squaring method or the $\pm$ split both accepted — but the $\pm$ split is faster and less error-prone. Always check.

## 1.2 Graphs: y = |f(x)|, y = f(|x|) and Related Transformations

Given the graph of $y = f(x)$:

| Transformation | What to do |
|---|---|
| $y = |f(x)|$ | Reflect the part **below** the $x$-axis in the $x$-axis; the rest stays. |
| $y = f(|x|)$ | Keep the part for $x \geq 0$; reflect it in the $y$-axis to fill $x < 0$ (the graph is symmetric in the $y$-axis). |
| $y = \frac{1}{f(x)}$ | Vertical asymptotes where $f(x) = 0$; $y \to 0$ where $|f(x)| \to \infty$. |

For $y = |f(x)|$: every $x$-intercept stays an intercept, every negative $y$-value becomes positive.

For $y = f(|x|)$: the graph for $x < 0$ is the mirror image of the graph for $x > 0$. If already given for $x \geq 0$, reflect that portion.

> ⭐ **Watch Out!** (1) $y = |f(x)|$ keeps the same $x$-intercepts but the negative lobes flip up. (2) $y = f(|x|)$ is an **even function** — it is symmetric about the $y$-axis. (3) When sketching $\frac{1}{f(x)}$, mark asymptotes at every zero of $f(x)$ before plotting anything.

### Example 4 - Easy - sketching $y = |2x - 5|$ from $y = 2x - 5$

> **Question:** Sketch the graph of $y = |2x - 5|$.

**Solution:**

Start with $y = 2x - 5$: a straight line, gradient $2$, intercepts at $\left(\frac{5}{2}, 0\right)$ and $(0, -5)$.

$$y = 2x - 5 \text{ crosses the } x\text{-axis at } x = \frac{5}{2}$$

$$y = |2x - 5| = \begin{cases} 2x - 5 & \text{if } x \geq \frac{5}{2} \\ -(2x - 5) = -2x + 5 & \text{if } x < \frac{5}{2} \end{cases}$$

So: for $x \geq \frac{5}{2}$ keep the line $y = 2x - 5$; for $x < \frac{5}{2}$ reflect the below-axis portion up:

$$y = |2x - 5| \text{ is V-shaped with vertex at } \left(\frac{5}{2}, 0\right)$$

$$y\text{-intercept: } |2(0) - 5| = 5, \text{ so } (0, 5)$$

The graph is a V with vertex $\left(\frac{5}{2}, 0\right)$, $y$-intercept $5$, arms of gradient $+2$ (right) and $-2$ (left). $\checkmark$

**What the examiner wants:** the vertex labelled, the $y$-intercept correct ($5$, not $-5$), and the V-shape clearly drawn.

### Example 5 - Medium - sketching $y = f(|x|)$ (coursebook Section 1.2)

> **Question:** The graph of $y = f(x)$ is a quadratic $y = x^2 - 4x + 3$ for $x \geq 0$. Sketch $y = f(|x|)$.

**Solution:**

For $y = f(|x|)$, use $|x|$: the graph is even.

$$f(|x|) = |x|^2 - 4|x| + 3 = x^2 - 4|x| + 3$$

For $x \geq 0$: $y = x^2 - 4x + 3$ (given).

For $x < 0$: $y = x^2 + 4x + 3$ (since $|x| = -x$).

$$x \geq 0: \quad y = x^2 - 4x + 3 = (x-1)(x-3), \quad \text{vertex at } x = 2, \, y = -1$$

$$x < 0: \quad y = x^2 + 4x + 3 = (x+1)(x+3), \quad \text{vertex at } x = -2, \, y = -1$$

So $y = f(|x|)$ is symmetric about the $y$-axis: two parabola halves meeting at $(0, 3)$, with $x$-intercepts at $x = \pm 1$ and $x = \pm 3$, vertices at $(\pm 2, -1)$. $\checkmark$

**What the examiner wants:** the $y$-axis symmetry explicitly shown; the $x \geq 0$ portion kept and mirrored.

### Example 6 - Hard - solving $|2x - 3| = x + 1$ with graphical check

> **Question:** (a) Solve $|2x - 3| = x + 1$. (b) Verify graphically.

**Solution:**

(a) $|2x - 3| = x + 1$ requires $x + 1 \geq 0$ (since a modulus is non-negative), so $x \geq -1$ is needed. Now split:

Case 1: $2x - 3 = x + 1$

$$2x - 3 = x + 1$$

$$x = 4$$

Case 2: $2x - 3 = -(x + 1)$

$$2x - 3 = -x - 1$$

$$2x + x = -1 + 3$$

$$3x = 2$$

$$x = \frac{2}{3}$$

Check $x = 4$: $|2(4)-3| = |5| = 5$ and $4 + 1 = 5 \checkmark$.

Check $x = \frac{2}{3}$: $|2(\frac{2}{3})-3| = |{-}\frac{5}{3}| = \frac{5}{3}$ and $\frac{2}{3}+1 = \frac{5}{3} \checkmark$.

$$x = \frac{2}{3} \text{ or } x = 4 \quad\checkmark$$

(b) $y = |2x-3|$ is V-shaped with vertex $(\frac{3}{2}, 0)$; $y = x+1$ is a line of gradient $1$ through $(0,1)$. They intersect at exactly the two $x$-values found above. $\checkmark$

**What the examiner wants:** the domain restriction $x \geq -1$ noted (or both solutions checked); the extraneous-root trap avoided.

## 1.3 Solving Modulus Equations and Inequalities

**Equations:** use $|a| = |b| \iff a^2 = b^2$ or $a = \pm b$.

**Inequalities** — two standard methods:

**Algebraic:** $|x| < k \iff -k < x < k$ and $|x| > k \iff x < -k$ or $x > k$ (for $k > 0$).

For $|ax+b| < |cx+d|$: square both sides (both sides non-negative):

$$|ax+b| < |cx+d| \iff (ax+b)^2 < (cx+d)^2$$

**Graphical:** sketch $y = |ax+b|$ and $y = |cx+d|$ (or $y = k$), find intersection points, read off where one graph is above/below the other.

> ⭐ **Watch Out!** For inequalities of the form $|ax+b| > k$: the solution is TWO separate intervals ($x < \dots$ or $x > \dots$), never a single combined interval. For $|ax+b| < |cx+d|$: squaring gives a quadratic inequality — factor it and use a sign diagram or critical values.

### Example 7 - Medium - modulus inequality $|x - 2| < 3$ and $|2x - 5| > 3$ (coursebook Section 1.3)

> **Question:** Solve (a) $|x - 2| < 3$, (b) $|2x - 5| > 3$.

**Solution:**

(a) $|x - 2| < 3 \iff -3 < x - 2 < 3$:

$$-3 < x - 2 < 3$$

Add $2$ throughout:

$$-1 < x < 5 \quad\checkmark$$

(b) $|2x - 5| > 3 \iff 2x - 5 < -3$ or $2x - 5 > 3$:

$$2x - 5 < -3$$

$$2x < 2$$

$$x < 1$$

or

$$2x - 5 > 3$$

$$2x > 8$$

$$x > 4$$

$$x < 1 \text{ or } x > 4 \quad\checkmark$$

**What the examiner wants:** the two-interval answer for $>$ written with "or" (not "and"); the $-k < x < k$ rule applied correctly.

### Example 8 - Hard - inequality with two moduli $|3x + 4| > |x - 2|$ (coursebook Section 1.3)

> **Question:** Solve $|3x + 4| > |x - 2|$.

**Solution:**

Both sides non-negative, so square:

$$|3x + 4|^2 > |x - 2|^2$$

$$(3x + 4)^2 > (x - 2)^2$$

Expand:

$$9x^2 + 24x + 16 > x^2 - 4x + 4$$

Bring all to one side:

$$9x^2 + 24x + 16 - x^2 + 4x - 4 > 0$$

$$8x^2 + 28x + 12 > 0$$

Divide by $4$:

$$2x^2 + 7x + 3 > 0$$

Factorise:

$$2x^2 + 7x + 3 = (2x + 1)(x + 3)$$

Critical values $x = -\frac{1}{2}$ and $x = -3$. Since the quadratic opens upward ($a = 2 > 0$), it is positive outside the roots:

$$x < -3 \text{ or } x > -\frac{1}{2} \quad\checkmark$$

Equivalently, from Example 3 the graphs $y = |3x+4|$ and $y = |x-2|$ intersect at $x = -3$ and $x = -\frac{1}{2}$; $|3x+4|$ is above $|x-2|$ outside those $x$-values. $\checkmark$

**What the examiner wants:** squaring done correctly, quadratic factorised, sign diagram or parabola reasoning to get the two outer intervals.

### Example 9 - Hard - graphical method for $|2x - 5| < 3$ (coursebook Worked example 1.5)

> **Question:** Solve $|2x - 5| < 3$ using a graphical method.

**Solution:**

Sketch $y = |2x - 5|$ (V-shape, vertex $(\frac{5}{2}, 0)$, $y$-intercept $5$) and $y = 3$ (horizontal line).

Find intersections: $|2x - 5| = 3$:

$$2x - 5 = 3 \implies 2x = 8 \implies x = 4$$

$$2x - 5 = -3 \implies 2x = 2 \implies x = 1$$

$$y = |2x-5| \text{ meets } y = 3 \text{ at } x = 1 \text{ and } x = 4$$

The V-shape is **below** the horizontal line between the two intersection points:

$$1 < x < 4 \quad\checkmark$$

**What the examiner wants:** the two intersection $x$-values found algebraically, then the inequality read off from the graph positions.

## 1.4 Division of Polynomials

Dividing a polynomial $P(x)$ (degree $\leq 4$) by a linear or quadratic divisor gives a **quotient** $Q(x)$ and a **remainder** $R(x)$:

$$P(x) = Q(x) \cdot D(x) + R(x), \qquad \deg R < \deg D$$

For a linear divisor $ax + b$: use long division or equating coefficients. The remainder is a constant.

For a quadratic divisor: the remainder is at most linear ($cx + d$).

Long division steps: (1) divide leading terms, (2) multiply back, (3) subtract, (4) bring down, (5) repeat until degree of remainder $<$ degree of divisor.

> ⭐ **Watch Out!** Include a zero coefficient for any missing power of $x$ (e.g. write $x^3 + 2x - 5$ as $x^3 + 0x^2 + 2x - 5$). Sign errors in the subtraction step are the most common mistake — change every sign in the row being subtracted.

### Example 10 - Medium - dividing by a linear divisor $x - 2$ (coursebook Section 1.4)

> **Question:** Divide $2x^3 + 3x^2 - 5x - 6$ by $x - 2$. Give the quotient and remainder.

**Solution:**

Set up long division of $2x^3 + 3x^2 - 5x - 6$ by $x - 2$:

Divide $2x^3$ by $x$:

$$2x^3 \div x = 2x^2$$

Multiply back:

$$2x^2(x - 2) = 2x^3 - 4x^2$$

Subtract:

$$(2x^3 + 3x^2) - (2x^3 - 4x^2) = 7x^2$$

Bring down $-5x$:

$$7x^2 - 5x$$

Next term:

$$7x^2 \div x = 7x$$

$$7x(x - 2) = 7x^2 - 14x$$

Subtract:

$$(7x^2 - 5x) - (7x^2 - 14x) = 9x$$

Bring down $-6$:

$$9x - 6$$

Final term:

$$9x \div x = 9$$

$$9(x - 2) = 9x - 18$$

Subtract:

$$(9x - 6) - (9x - 18) = 12$$

$$2x^3 + 3x^2 - 5x - 6 = (x - 2)(2x^2 + 7x + 9) + 12$$

$$\text{Quotient } = 2x^2 + 7x + 9, \quad \text{Remainder } = 12 \quad\checkmark$$

**What the examiner wants:** every subtraction done correctly; the answer stated as quotient plus remainder, or equivalently $P(x) = D(x)Q(x) + R$.

### Example 11 - Medium - dividing by a quadratic divisor $x^2 + x + 1$

> **Question:** Divide $x^4 + 2x^3 + 3x^2 + 2x + 1$ by $x^2 + x + 1$. Give the quotient and remainder.

**Solution:**

Long division:

Leading term $x^4 \div x^2 = x^2$:

$$x^2(x^2 + x + 1) = x^4 + x^3 + x^2$$

Subtract from dividend:

$$(x^4 + 2x^3 + 3x^2) - (x^4 + x^3 + x^2) = x^3 + 2x^2$$

Bring down $+2x$:

$$x^3 + 2x^2 + 2x$$

Next: $x^3 \div x^2 = x$:

$$x(x^2 + x + 1) = x^3 + x^2 + x$$

Subtract:

$$(x^3 + 2x^2 + 2x) - (x^3 + x^2 + x) = x^2 + x$$

Bring down $+1$:

$$x^2 + x + 1$$

Next: $x^2 \div x^2 = 1$:

$$1(x^2 + x + 1) = x^2 + x + 1$$

Subtract:

$$(x^2 + x + 1) - (x^2 + x + 1) = 0$$

$$x^4 + 2x^3 + 3x^2 + 2x + 1 = (x^2 + x + 1)(x^2 + x + 1) + 0$$

$$\text{Quotient } = x^2 + x + 1, \quad \text{Remainder } = 0 \quad\checkmark$$

So $x^2 + x + 1$ is a factor (the polynomial is $(x^2+x+1)^2$). $\checkmark$

**What the examiner wants:** the quadratic divisor handled term by term; the remainder degree checked ($< 2$).

### Example 12 - Medium - equating coefficients as an alternative

> **Question:** When $x^3 + ax^2 + bx - 6$ is divided by $x - 1$, the quotient is $x^2 + 2x + c$ and the remainder is $d$. Use equating coefficients to set up the identity.

**Solution:**

Write the division identity:

$$x^3 + ax^2 + bx - 6 = (x - 1)(x^2 + 2x + c) + d$$

Expand the right-hand side:

$$(x - 1)(x^2 + 2x + c) = x^3 + 2x^2 + cx - x^2 - 2x - c$$

$$= x^3 + x^2 + (c - 2)x - c$$

So:

$$x^3 + ax^2 + bx - 6 = x^3 + x^2 + (c-2)x - c + d$$

Equate coefficients of $x^2$:

$$a = 1$$

Equate coefficients of $x$:

$$b = c - 2$$

Equate constants:

$$-6 = -c + d$$

These equations can then be solved once further information is given. $\checkmark$

**What the examiner wants:** the identity $P(x) = D(x)Q(x) + R$ written first, then coefficients compared systematically.

## 1.5 The Factor Theorem and the Remainder Theorem

**Remainder theorem:** When $P(x)$ is divided by $(x - a)$, the remainder is $P(a)$. When divided by $(ax - b)$, the remainder is $P\!\left(\frac{b}{a}\right)$.

**Factor theorem:** $(x - a)$ is a factor of $P(x) \iff P(a) = 0$. More generally, $(ax - b)$ is a factor $\iff P\!\left(\frac{b}{a}\right) = 0$.

To find unknown coefficients: substitute the known root or remainder value, equate, and solve the resulting linear equations. For two unknowns, you need two conditions (e.g. two factor conditions, or one factor + one remainder).

> ⭐ **Watch Out!** (1) For divisor $(2x - 1)$, substitute $x = \frac{1}{2}$ (not $x = 1$). For $(x + a)$, substitute $x = -a$. (2) "Remainder is 5 when divided by $(x-2)$" means $P(2) = 5$, not $P(2) = 0$. (3) After finding one factor, you may need to factorise the quotient further to solve $P(x) = 0$ completely.

### Example 13 - Easy - using the factor theorem to check a factor

> **Question:** Show that $x - 2$ is a factor of $P(x) = x^3 - 3x^2 - 4x + 12$.

**Solution:**

By the factor theorem, $x - 2$ is a factor $\iff P(2) = 0$:

$$P(2) = (2)^3 - 3(2)^2 - 4(2) + 12$$

$$= 8 - 12 - 8 + 12$$

$$= 0$$

$$P(2) = 0 \implies (x-2) \text{ is a factor } \quad\checkmark$$

**What the examiner wants:** the substitution $x = 2$ shown explicitly and the conclusion stated.

### Example 14 - Medium - finding an unknown coefficient using the factor theorem

> **Question:** Given that $x + 1$ is a factor of $P(x) = x^3 + ax^2 + 5x + 2$, find the value of $a$.

**Solution:**

$x + 1$ is a factor $\iff P(-1) = 0$:

$$P(-1) = (-1)^3 + a(-1)^2 + 5(-1) + 2$$

$$= -1 + a - 5 + 2$$

$$= a - 4$$

Set equal to zero:

$$a - 4 = 0$$

$$a = 4 \quad\checkmark$$

Check: $P(x) = x^3 + 4x^2 + 5x + 2$, $P(-1) = -1 + 4 - 5 + 2 = 0 \checkmark$.

**What the examiner wants:** the correct substitution $x = -1$ (not $x = 1$); the linear equation in $a$ solved.

### Example 15 - Hard - two unknowns from factor + remainder conditions

> **Question:** The polynomial $P(x) = 2x^3 + ax^2 + bx - 6$ has $(x-2)$ as a factor and leaves remainder $12$ when divided by $(x+1)$. Find $a$ and $b$.

**Solution:**

Condition 1: $(x-2)$ is a factor, so $P(2) = 0$:

$$P(2) = 2(2)^3 + a(2)^2 + b(2) - 6$$

$$= 16 + 4a + 2b - 6$$

$$= 4a + 2b + 10$$

$$4a + 2b + 10 = 0$$

$$4a + 2b = -10$$

$$2a + b = -5 \tag{1}$$

Condition 2: remainder when divided by $(x+1)$ is $12$, so $P(-1) = 12$:

$$P(-1) = 2(-1)^3 + a(-1)^2 + b(-1) - 6$$

$$= -2 + a - b - 6$$

$$= a - b - 8$$

$$a - b - 8 = 12$$

$$a - b = 20 \tag{2}$$

Solve simultaneously. From (2): $a = 20 + b$. Substitute into (1):

$$2(20 + b) + b = -5$$

$$40 + 2b + b = -5$$

$$3b = -45$$

$$b = -15$$

Then:

$$a = 20 + (-15) = 5$$

$$a = 5, \quad b = -15 \quad\checkmark$$

Check: $P(2) = 16 + 20 - 30 - 6 = 0 \checkmark$; $P(-1) = -2 + 5 + 15 - 6 = 12 \checkmark$.

**What the examiner wants:** two linear equations from the two conditions, solved simultaneously, with the sign of the substitution ($x = -1$ for divisor $x+1$) correct throughout.

### Example 16 - Hard - factor theorem with $(2x - 1)$ and complete factorisation

> **Question:** The polynomial $P(x) = 2x^3 + x^2 - 5x + 2$ has $(2x - 1)$ as a factor. (a) Verify this. (b) Hence solve $P(x) = 0$.

**Solution:**

(a) $(2x - 1)$ is a factor $\iff P\!\left(\frac{1}{2}\right) = 0$:

$$P\!\left(\frac{1}{2}\right) = 2\left(\frac{1}{2}\right)^3 + \left(\frac{1}{2}\right)^2 - 5\left(\frac{1}{2}\right) + 2$$

$$= 2 \cdot \frac{1}{8} + \frac{1}{4} - \frac{5}{2} + 2$$

$$= \frac{1}{4} + \frac{1}{4} - \frac{5}{2} + 2$$

$$= \frac{1}{2} - \frac{5}{2} + 2$$

$$= -2 + 2 = 0 \quad\checkmark$$

(b) Divide $P(x)$ by $(2x - 1)$ or equivalently note that $x = \frac{1}{2}$ is a root. Use polynomial division or equate coefficients. Write:

$$P(x) = (2x-1)(Ax^2 + Bx + C)$$

Expand:

$$(2x-1)(Ax^2 + Bx + C) = 2Ax^3 + 2Bx^2 + 2Cx - Ax^2 - Bx - C$$

$$= 2Ax^3 + (2B-A)x^2 + (2C-B)x - C$$

Compare with $2x^3 + x^2 - 5x + 2$:

$$2A = 2 \implies A = 1$$

$$2B - A = 1 \implies 2B - 1 = 1 \implies B = 1$$

$$-C = 2 \implies C = -2$$

Check: $2C - B = -4 - 1 = -5 \checkmark$.

So:

$$P(x) = (2x-1)(x^2 + x - 2)$$

Factorise the quadratic:

$$x^2 + x - 2 = (x+2)(x-1)$$

$$P(x) = (2x-1)(x+2)(x-1)$$

$$P(x) = 0 \implies x = \frac{1}{2}, \quad x = -2, \quad x = 1 \quad\checkmark$$

**What the examiner wants:** the substitution $x = \frac{1}{2}$ (not $x = 1$ or $x = 2$); the quotient found and factorised fully to give all three roots.

### Practice Questions - Part 1

**Q1.** Solve $|3x - 2| = 7$.

**Q2.** Solve $|2x + 1| = |x - 5|$.

**Q3.** Sketch the graph of $y = |x^2 - 4|$.

**Q4.** Solve the inequality $|x + 3| > 5$.

**Q5.** The polynomial $P(x) = x^3 + ax^2 - 7x + b$ has $(x-1)$ as a factor and leaves remainder $6$ when divided by $(x+2)$. Find $a$ and $b$.

### Practice Questions - Part 1 - Full Solutions

**Solution Q1:**

$$|3x - 2| = 7 \implies 3x - 2 = 7 \text{ or } 3x - 2 = -7$$

$$3x = 9 \implies x = 3$$

$$3x = -5 \implies x = -\frac{5}{3}$$

$$x = -\frac{5}{3} \text{ or } x = 3 \quad\checkmark$$

**Solution Q2:**

$$|2x+1| = |x-5| \implies 2x+1 = x-5 \text{ or } 2x+1 = -(x-5)$$

$$2x + 1 = x - 5$$

$$x = -6$$

$$2x + 1 = -x + 5$$

$$3x = 4$$

$$x = \frac{4}{3}$$

Check both satisfy the original. $\checkmark$

$$x = -6 \text{ or } x = \frac{4}{3} \quad\checkmark$$

**Solution Q3:**

$$y = x^2 - 4 = (x-2)(x+2), \quad \text{parabola with } x\text{-intercepts } \pm 2, \text{ vertex } (0,-4)$$

$$y = |x^2 - 4|: \text{ reflect the below-axis portion (between } x=-2 \text{ and } x=2\text{) in the } x\text{-axis}$$

Result: W-shaped graph touching $x$-axis at $x = \pm 2$, vertex at $(0, 4)$ for the middle hump, same outer arms as $x^2 - 4$ for $|x| > 2$. $\checkmark$

**Solution Q4:**

$$|x+3| > 5 \iff x+3 < -5 \text{ or } x+3 > 5$$

$$x < -8 \text{ or } x > 2 \quad\checkmark$$

**Solution Q5:**

$P(1) = 0$: $1 + a - 7 + b = 0 \implies a + b = 6$.

$P(-2) = 6$: $-8 + 4a + 14 + b = 6 \implies 4a + b = 0$.

Subtract: $3a = -6 \implies a = -2$, then $b = 8$. $\checkmark$

Check: $P(1) = 1 - 2 - 7 + 8 = 0 \checkmark$; $P(-2) = -8 - 8 + 14 + 8 = 6 \checkmark$.

---


---

# Formula Sheet (Chapter 1)

*Extracted from the chapter — see full sheet in the combined file for cross-topic formulas. This sheet covers only Chapter 1: Algebra.*

# Quick Reference Card (Chapter 1)

*See combined file for the full quick reference. Key results for Chapter 1: Algebra are boxed throughout the chapter above.*
