# B2 Optional Appendix (Algebra II enrichment - not core SAT)

# B2.1 Appendix Fragment (archived from front matter + B2.1)

Material moved out of the main B2.1 flow during revision - kept here for reference, not deleted. All math in LaTeX; no em dashes used.

## A1. Archived Formula Reference Entries

### Vieta's Formulas

For $ax^2 + bx + c = 0$ with roots $r_1, r_2$:
- $r_1 + r_2 = -\frac{b}{a}$
- $r_1 \cdot r_2 = \frac{c}{a}$

For $ax^3 + bx^2 + cx + d = 0$ with roots $r_1, r_2, r_3$:
- $r_1 + r_2 + r_3 = -\frac{b}{a}$
- $r_1 r_2 + r_1 r_3 + r_2 r_3 = \frac{c}{a}$
- $r_1 r_2 r_3 = -\frac{d}{a}$

### Polynomial Theorems

- **Factor Theorem:** $f(a) = 0 \iff (x-a)$ is a factor of $f(x)$
- **Remainder Theorem:** $f(a)$ = remainder when $f(x)$ is divided by $(x-a)$
- **Rational Root Theorem:** Rational roots of $a_n x^n + \cdots + a_0$ are of form $\frac{\text{factor of }a_0}{\text{factor of }a_n}$
- **Polynomial long division:** divide term-by-term like numeric long division - leading term of dividend $\div$ leading term of divisor, multiply back, subtract, bring down, repeat. If the remainder is $R$, then $f(x) = d(x)q(x) + R$.
- **Synthetic division:** shortcut for dividing by $(x - a)$: bring down the leading coefficient, multiply by $a$, add to the next coefficient, repeat. The last entry is the remainder; the other entries are the quotient's coefficients.

## A2. Cubic Expansions (moved from B2.1.3 special-products table)

| Identity | Expanded |
|---|---|
| $(a+b)^3$ | $a^3 + 3a^2b + 3ab^2 + b^3$ |
| $(a-b)^3$ | $a^3 - 3a^2b + 3ab^2 - b^3$ |

[Very Hard] $(x^2 + 2x - 3)(x^2 - 2x + 3) = [x^2 + (2x-3)][x^2 - (2x-3)] = (x^2)^2 - (2x-3)^2$ $= x^4 - (4x^2 - 12x + 9) = x^4 - 4x^2 + 12x - 9$

⚡ Recognize $(A+B)(A-B) = A^2 - B^2$ even when $A$ and $B$ are expressions.

## A3. B2.1.7 Polynomial Theorems (moved whole section)

**Definition:** the Factor and Remainder Theorems let you extract information about a polynomial WITHOUT doing division. They are the fastest tools on the SAT for "is $x-a$ a factor?" and "what is the remainder?" questions.

**Remainder Theorem:** $f(a)$ = remainder when $f(x)$ is divided by $(x-a)$.

[Medium] What is the remainder when $x^3 - 5x^2 + 7$ is divided by $x + 2$?
$f(-2) = -8 - 20 + 7 = -21$. Answer: $-21$.

❌ **Sign trap:** $x+2 = x - (-2)$, so $a = -2$, not $2$.

**Factor Theorem:** $f(a) = 0 \iff (x-a)$ is a factor.

[Hard] Which of the following is a factor of $x^3 - 7x + 6$?

A) $x - 1$
B) $x - 2$
C) $x + 3$
D) All of the above

Test $f(1) = 1 - 7 + 6 = 0$ ✓, so $x - 1$ is a factor. Test $f(2) = 8 - 14 + 6 = 0$ ✓, so $x - 2$ is a factor. Test $f(-3) = -27 + 21 + 6 = 0$ ✓, so $x + 3$ is a factor. Since $x^3 - 7x + 6$ is a cubic, three linear factors means it factors completely: $(x-1)(x-2)(x+3)$. Answer: **D**.

❌ **Intuition trap:** students assume only ONE of the given answers must be correct. Always verify each independently.
⚡ **Remainder Theorem shortcut:** only need remainder? Compute $f(a)$. No division needed.

**Degree bound:** A polynomial of degree $n$ has at most $n$ real roots and at most $n-1$ turning points.

---

## A4. B2.1.11 Polynomial Long Division and Synthetic Division (moved whole section)

**What it is:** the polynomial version of numeric long division. Dividing $f(x)$ by $d(x)$ produces a quotient $q(x)$ and a remainder $r(x)$:

$$f(x) = d(x) \cdot q(x) + r(x), \quad \deg(r) < \deg(d)$$

**Long division method (step by step):**
1. Write the dividend with ALL powers present (fill missing terms with $0x^k$).
2. Divide the leading term of the dividend by the leading term of the divisor - that is the next quotient term.
3. Multiply the whole divisor by that quotient term and subtract from the dividend.
4. Bring down the next term and repeat until the remaining degree is below the divisor's degree.
5. The leftover is the remainder.

[Medium] Divide $x^2 + 5x + 6$ by $x + 2$.
- $x^2 \div x = x$. Multiply: $x(x+2) = x^2 + 2x$. Subtract: $(x^2+5x+6) - (x^2+2x) = 3x + 6$.
- $3x \div x = 3$. Multiply: $3(x+2) = 3x + 6$. Subtract: $0$.
- Quotient $x + 3$, remainder $0$. Check: $(x+2)(x+3) = x^2 + 5x + 6$ ✓.

[Hard] Divide $x^3 - 2x + 1$ by $x - 1$. Note the missing $x^2$ term - write $x^3 + 0x^2 - 2x + 1$.
- $x^3 \div x = x^2$. Multiply: $x^2(x-1) = x^3 - x^2$. Subtract: $(x^3 + 0x^2) - (x^3 - x^2) = x^2$, bring down $-2x$: $x^2 - 2x$.
- $x^2 \div x = x$. Multiply: $x(x-1) = x^2 - x$. Subtract: $(x^2-2x) - (x^2-x) = -x$, bring down $1$: $-x + 1$.
- $-x \div x = -1$. Multiply: $-1(x-1) = -x + 1$. Subtract: $0$.
- Quotient $x^2 + x - 1$, remainder $0$. Check: $(x-1)(x^2+x-1) = x^3 - 2x + 1$ ✓.

❌ **Missing-term trap:** if the dividend skips a power ($x^3 - 2x + 1$ has no $x^2$), you MUST insert $0x^2$ or the subtraction columns misalign.

[Hard] Divide $2x^3 - 7x^2 + 5x - 4$ by $x - 2$.
- $2x^3 \div x = 2x^2$. Multiply: $2x^2(x-2) = 2x^3 - 4x^2$. Subtract: $-3x^2$, bring down $5x$: $-3x^2 + 5x$.
- $-3x^2 \div x = -3x$. Multiply: $-3x(x-2) = -3x^2 + 6x$. Subtract: $-x$, bring down $-4$: $-x - 4$.
- $-x \div x = -1$. Multiply: $-1(x-2) = -x + 2$. Subtract: $-6$.
- Quotient $2x^2 - 3x - 1$, remainder $-6$.
- Remainder Theorem check: $f(2) = 16 - 28 + 10 - 4 = -6$ ✓ - the two theorems agree.

**Synthetic division shortcut** (only when dividing by $x - a$):

[Hard] Divide $x^3 - 6x^2 + 11x - 6$ by $x - 2$:
```
2 | 1  -6   11  -6
  |      2   -8   6
  -----------------
    1  -4    3   0
```
Quotient $x^2 - 4x + 3$, remainder $0$. And $x^2 - 4x + 3 = (x-1)(x-3)$, so $f(x) = (x-2)(x-1)(x-3)$.

**Rational Root Theorem in action** (pairs with division):

[Very Hard] Find all rational roots of $x^3 - 7x + 6 = 0$.
- Possible rational roots: $\frac{\text{factors of } 6}{\text{factors of } 1} = \pm 1, \pm 2, \pm 3, \pm 6$.
- Test $f(1) = 1 - 7 + 6 = 0$ → $x = 1$ is a root.
- Synthetic division by $x - 1$: quotient $x^2 + x - 6 = (x+3)(x-2)$.
- Roots: $1, 2, -3$ ✓.

❌ **Candidate-list trap:** the Rational Root Theorem only LISTS candidates - every candidate must be tested, and roots can still be irrational ($x^2 - 2 = 0$ has no rational roots).
❌ **Division sign trap:** dividing by $x - 2$ uses synthetic value $2$; dividing by $x + 2$ uses $-2$.

⚡ Desmos: graph the dividend and the quotient times the divisor; the curves should overlap wherever the divisor is nonzero.

---

## A5. Excess Drill Bank (cut from B2.1.1, B2.1.2, B2.1.4, B2.1.5, B2.1.9, B2.1.10)

### From B2.1.1 (extra polynomial-operation drills)

[Medium] $(x+3)(x^2 - 2x + 5) = x(x^2 - 2x + 5) + 3(x^2 - 2x + 5) = x^3 - 2x^2 + 5x + 3x^2 - 6x + 15 = x^3 + x^2 - x + 15$

[Hard] $(x-2)(x+2)(x^2+4) = (x^2-4)(x^2+4) = x^4 - 16$

### From B2.1.2 (extra factoring drills)

[Very Hard] Factor $x^4 - 13x^2 + 36$ completely.
$$x^4 - 13x^2 + 36 = (x^2 - 4)(x^2 - 9) = (x-2)(x+2)(x-3)(x+3)$$
Quadratic in disguise: let $u = x^2$, then $u^2 - 13u + 36 = (u-4)(u-9)$.
⚡ Desmos: graph $y = x^4 - 13x^2 + 36$; the four $x$-intercepts ($\pm 2, \pm 3$) confirm the four factors.

[Hard] Which expression is equivalent to $9x^2 + 30x + 25$?
$$9x^2 + 30x + 25 = (3x + 5)^2$$
Check: $(3x)^2 = 9x^2$ ✓, $5^2 = 25$ ✓, $2(3x)(5) = 30x$ ✓.
❌ **"Almost perfect" trap:** $x^2 + 8x + 15$ looks like a perfect square but $15 \neq 16$; it factors as $(x+3)(x+5)$, not $(x+4)^2$.

[Very Hard] Factor $12x^2 - 7x - 10$ completely.
1. $a \cdot c = 12(-10) = -120$.
2. Factor pairs of $-120$ that sum to $-7$: $8$ and $-15$.
3. Rewrite: $12x^2 + 8x - 15x - 10$
4. Group: $4x(3x + 2) - 5(3x + 2) = (3x + 2)(4x - 5)$
❌ **Sign-error trap:** list ALL factor pairs before deciding.

[Medium] $x^3 + 8 = (x + 2)(x^2 - 2x + 4)$

[Hard] Factor $2x^3 - 3x^2 - 8x + 12$.
$$2x^3 - 3x^2 - 8x + 12 = x^2(2x - 3) - 4(2x - 3) = (2x - 3)(x^2 - 4) = (2x-3)(x-2)(x+2)$$
❌ **GCF trap:** if the leading coefficient of a pair is negative, factor out the negative.

### From B2.1.4 (extra rational drills)

[Medium] $\frac{3}{x+2} + \frac{5}{x-2} = \frac{3(x-2) + 5(x+2)}{(x+2)(x-2)} = \frac{8x+4}{(x+2)(x-2)} = \frac{4(2x+1)}{x^2-4}$

[Hard] $\frac{\frac{1}{x} + \frac{2}{x+1}}{\frac{3}{x}}$ - multiply num/den by LCD $x(x+1)$: $\frac{(x+1) + 2x}{3(x+1)} = \frac{3x+1}{3x+3}$

[Very Hard] Simplify $\frac{\frac{1}{x} - \frac{1}{y}}{\frac{1}{x^2} - \frac{1}{y^2}}$ for $x \neq y$, $x \neq -y$, $x, y \neq 0$.
- Multiply numerator and denominator by the LCD $x^2 y^2$:
$$\frac{y^2 x - x^2 y}{y^2 - x^2} = \frac{xy(y - x)}{(y-x)(y+x)} = \frac{xy}{x + y}$$
❌ **Pattern trap:** the denominator is a difference of squares AFTER multiplying by the LCD - $\frac{1}{x^2} - \frac{1}{y^2}$ cannot "simplify" into $\frac{1}{x} - \frac{1}{y}$.

### From B2.1.5 (extra radical drills)

[Medium] $(\sqrt[4]{x})^3 = x^{3/4}$

[Medium] $\frac{3}{\sqrt{2}} = \frac{3\sqrt{2}}{2}$

### From dissolved B2.1.9 (redundant "which is equivalent" drills - skills taught in B2.1.4/B2.1.5/B2.1.6)

[Medium] Which expression is equivalent to $\frac{\sqrt{18x^3}}{\sqrt{2x}}$ for $x > 0$?

A) $3x$
B) $3\sqrt{x}$
C) $9x$
D) $3x\sqrt{2}$

Simplify: $\sqrt{\frac{18x^3}{2x}} = \sqrt{9x^2} = 3x$. Answer: **A**.
❌ **Choice C trap:** $9x$ - simplifies $\frac{18}{2} = 9$ but forgets the square root.

[Hard] Which expression is equivalent to $\frac{x^2 - 16}{x^2 - 8x + 16}$ for $x \neq 4$?

A) $\frac{x-4}{x+4}$
B) $\frac{x+4}{x-4}$
C) $\frac{x+4}{x+4}$
D) $1$

Factor: $\frac{(x-4)(x+4)}{(x-4)^2} = \frac{x+4}{x-4}$. Answer: **B**.

[Hard] Which expression is equivalent to $\frac{8x^6 y^{-3}}{2x^{-2} y^5}$ for $x, y \neq 0$?

A) $4x^4 y^{-8}$
B) $4x^8 y^{-8}$
C) $6x^4 y^2$
D) $4x^8 y^2$

$\frac{8}{2} = 4$, $x^{6 - (-2)} = x^8$, $y^{-3 - 5} = y^{-8}$. Answer: **B**.

[Hard] Which expression is equivalent to $2x^2 - 12x + 5$?

A) $2(x-3)^2 - 13$
B) $2(x-3)^2 - 4$
C) $(x-3)^2 - 13$
D) $2(x-6)^2 - 31$

Complete square: $2(x^2 - 6x) + 5 = 2(x-3)^2 - 18 + 5 = 2(x-3)^2 - 13$. Answer: **A**.

### From deleted B2.1.10 (duplicate-of-B2.1.8 drill)

[Hard] The expression $3x^2 - 12x + 7$ can be written in vertex form $a(x-h)^2 + k$. What is $h + k$?

A) $-5$
B) $-3$
C) $5$
D) $7$

Vertex: $h = -\frac{-12}{6} = 2$, $k = 3(2)^2 - 12(2) + 7 = 12 - 24 + 7 = -5$. $h + k = 2 + (-5) = -3$. Answer: **B**.
❌ **Choice A trap:** $k = -5$; student answers $k$ instead of $h+k$.

---

---

# B2 Appendix 2 - Enrichment and Moved Topics (from B2.2)

## Vieta's Formulas (Enrichment, moved from B2.2.1)

For $ax^2 + bx + c = 0$ with roots $r_1, r_2$:
- $r_1 + r_2 = -\frac{b}{a}$
- $r_1 r_2 = \frac{c}{a}$

[Medium] If $3x^2 - 12x + 7 = 0$ has roots $r_1, r_2$: sum $= 4$, product $= \frac{7}{3}$.

[Hard] $2x^2 + kx - 6 = 0$ has roots $3$ and $m$. Find $k$ and $m$.
- Product: $3m = \frac{-6}{2} = -3 \to m = -1$
- Sum: $3 + (-1) = 2 = -\frac{k}{2} \to k = -4$

[Very Hard] $x^2 - 5x + 3 = 0$ has roots $p$ and $q$. Find $\frac{1}{p} + \frac{1}{q}$.
- $p + q = 5$, $pq = 3$. $\frac{1}{p} + \frac{1}{q} = \frac{p+q}{pq} = \frac{5}{3}$

❌ **Vieta sign trap:** $r_1 + r_2 = -\frac{b}{a}$, NOT $\frac{b}{a}$.

---

## Nested u-Substitution (moved from B2.2.2)

[Very Hard] $(x^2 - 3x)^2 - 2(x^2 - 3x) - 8 = 0$: let $u = x^2 - 3x$.
- $u^2 - 2u - 8 = 0 \to u = 4, -2$
- $x^2 - 3x = 4 \to x = 4, -1$
- $x^2 - 3x = -2 \to x = 1, 2$
- Solutions: $4, -1, 1, 2$

❌ **Back-substitution trap:** Each $u$ may produce 0, 1, or 2 $x$ values. Solve for original variable.

---

## Two-Radical Equation (moved from B2.2.3)

[Hard] $\sqrt{x+7} - \sqrt{x-1} = 2$
1. $\sqrt{x+7} = \sqrt{x-1} + 2$
2. Square: $x+7 = (x-1) + 4\sqrt{x-1} + 4 \to 4 = 4\sqrt{x-1} \to 1 = \sqrt{x-1} \to x = 2$
3. Check: $\sqrt{9} - \sqrt{1} = 3 - 1 = 2$ ✓

---

## Absolute Value Graphs (moved from B2.2.5 - see also B2.3 transformations)

The graph of $f(x) = a|x - h| + k$ is a V-shape with vertex $(h,k)$, opening up if $a > 0$, down if $a < 0$.

[Medium] Which graph represents $f(x) = -2|x - 3| + 4$?

Vertex at $(3,4)$, opens down, steepness $2$. The $x$-intercepts: $0 = -2|x-3| + 4 \to |x-3| = 2 \to x = 1, 5$.

❌ **Vertex sign trap:** $|x-3|$ has vertex at $x = 3$, not $x = -3$.

[Hard] The graph of $y = |x + 1| + 2$ is shifted right 3 and down 4. What is the new vertex?

Original vertex: $(-1, 2)$. Shift right 3: $(2, 2)$. Down 4: $(2, -2)$.

[Hard] The equation $|2x - 4| + k = 6$ has no solution. Which could be $k$?
- $|2x - 4| = 6 - k$. No solution iff the right side is negative: $6 - k < 0 \to k > 6$.

**Graph → equation matching:**

[Hard] Which function has a V-shaped graph with vertex $(-2, 3)$ and $x$-intercepts at $x = -5$ and $x = 1$?
- Vertex form: $f(x) = a|x + 2| + 3$. Plug an intercept, say $x = 1$: $0 = a|1 + 2| + 3 = 3a + 3 \to a = -1$.
- $f(x) = -|x + 2| + 3$. Check: $f(-5) = -3 + 3 = 0$ ✓, $f(1) = -3 + 3 = 0$ ✓. Opens down (peak at the vertex) ✓.

❌ **Vertex sign trap:** $|x + 2|$ means the vertex's $x$-coordinate is $-2$, not $+2$.

---

## Extra Systems Examples (moved from B2.2.7)

[Hard] $y = 2x + 1$, $y = 3^x$. How many solutions?
- Set $3^x = 2x + 1$. Test integer values: $x = 0$: $3^0 = 1 = 2(0)+1$ ✓; $x = 1$: $3^1 = 3 = 2(1)+1$ ✓.
- For $x > 1$ the exponential outruns the line ($3^2 = 9 > 5$), and for $x < 0$ we have $3^x > 0 > 2x + 1$, so there are no other crossings.
- Exactly 2 solutions: $(0, 1)$ and $(1, 3)$. Graph both in Desmos to confirm.

[Hard] The system $y = x + 1$ and $y = |2x - 4|$ has how many solutions?
- Case 1 ($x \geq 2$): $x + 1 = 2x - 4 \to x = 5$, valid since $5 \geq 2$. ✓
- Case 2 ($x < 2$): $x + 1 = -2x + 4 \to 3x = 3 \to x = 1$, valid since $1 < 2$. ✓
- Both candidates survive the domain check → 2 solutions: $(5, 6)$ and $(1, 2)$.
- Graph check: the V-shape crosses the rising line twice. If one candidate had failed its case condition, the answer would have been 1.

---

## Extra Exponential Example (moved from B2.2.6)

[Very Hard] How many real solutions does $2^{2x} - 3 \cdot 2^x + 2 = 0$ have?
- Let $u = 2^x$: $u^2 - 3u + 2 = 0 \to (u-1)(u-2) = 0 \to u = 1, 2$.
- $u = 1 \to 2^x = 1 \to x = 0$. $u = 2 \to 2^x = 2 \to x = 1$.
- Both valid (both $u > 0$). Answer: 2 real solutions.

---

## Doubling-Time Rearrangement (moved from B2.2.9)

[Very Hard] Solve for $t$: $P = P_0 \cdot 2^{t/d}$ (doubling-time formula).
- $\frac{P}{P_0} = 2^{t/d}$. If $\frac{P}{P_0}$ is a power of 2, equate exponents directly; otherwise graph both sides in Desmos (no logarithms on the DSAT).
- Example: $P_0 = 100$, $d = 3$, $P = 800$: $\frac{800}{100} = 8 = 2^3 \to \frac{t}{3} = 3 \to t = 9$.

⚡ Desmos: to solve $f(t) = c$, graph $y = f(t)$ and $y = c$; the intersection's $t$-coordinate is the answer.

---

## Optional Algebra II Appendix: Piecewise Functions

**Definition:** a piecewise function is ONE function defined by different rules on different intervals of its domain - like a phone plan that charges a flat fee up to some minutes, then a per-minute rate beyond. The SAT tests (a) evaluation at a given input, (b) graph interpretation (open vs closed circles), and (c) writing the function from a context.

**Step-by-step method (evaluate):**
1. Look at the input value $x$.
2. Find which branch's condition contains $x$ (check $\leq$, $<$, $\geq$, $>$ carefully).
3. Substitute into THAT branch only.

$f(x) = \begin{cases} x^2, & x < 0 \\ 2x + 1, & x \geq 0 \end{cases}$

**Evaluation:** Determine which branch applies, then substitute.

[Medium] Find $f(-3) + f(2)$.
- $f(-3) = (-3)^2 = 9$ ($x < 0$ branch)
- $f(2) = 2(2) + 1 = 5$ ($x \geq 0$ branch)
- $9 + 5 = 14$

❌ **Branch trap:** Always check the domain condition. Using the wrong branch is the #1 piecewise error.

**Real-World Application:**

[Hard] A parking garage charges \$5 for the first hour and \$3 per additional hour.
$C(t) = \begin{cases} 5, & 0 < t \leq 1 \\ 5 + 3(t-1), & t > 1 \end{cases}$
Cost for 4 hours: $C(4) = 5 + 3(3) = \$14$.

**Piecewise graph reading - evaluate from graph:**

[Medium] A piecewise function is defined as:
$f(x) = \begin{cases} 2x + 1, & x \leq 0 \\ x^2, & 0 < x < 3 \\ 9, & x \geq 3 \end{cases}$
Find $f(-2) + f(2) + f(4)$.

$f(-2) = 2(-2) + 1 = -3$ (first branch)
$f(2) = 2^2 = 4$ (second branch)
$f(4) = 9$ (third branch)
Sum: $-3 + 4 + 9 = 10$

❌ **Boundary trap:** At $x = 0$, only the first branch ($\leq$) applies. At $x = 3$, only the third branch ($\geq$) applies.

**Graph interpretation - open vs. closed circles:**

[Hard] A piecewise function is shown on a graph: a line segment $y = -x + 3$ for $x < 2$ with an open circle at $(2, 1)$, and a horizontal ray $y = 2$ starting at a closed circle at $(2, 2)$ for $x \geq 2$. Which definition matches?

$f(x) = \begin{cases} -x + 3, & x < 2 \\ 2, & x \geq 2 \end{cases}$

- Open circle at $(2,1)$ means the first branch does NOT include $x = 2$ (strict $<$).
- Closed circle at $(2,2)$ means the second branch DOES include $x = 2$ ($\geq$).
- So $f(2) = 2$ (second branch), $f(1.9) = 1.1$ (first branch), $f(2.1) = 2$ (second branch).

❌ **Open vs. closed trap:** an open circle at the boundary excludes that $x$ from that branch; a closed circle includes it. The value AT the boundary always comes from the branch with the closed circle.

**Writing a piecewise from a description (common SAT form):**

[Medium] A phone plan costs \$20 per month for the first 100 minutes, plus \$0.10 per minute beyond 100. Write $C(m)$ for $m$ minutes used.
$C(m) = \begin{cases} 20, & 0 \leq m \leq 100 \\ 20 + 0.10(m - 100), & m > 100 \end{cases}$
Cost for 250 minutes: $C(250) = 20 + 0.10(150) = \$35$.

**Absolute value as a piecewise function:**

[Medium] Write $f(x) = |x - 3|$ as a piecewise function and evaluate $f(0)$, $f(3)$, $f(5)$.
$|x - 3| = \begin{cases} x - 3, & x \geq 3 \\ -(x - 3), & x < 3 \end{cases}$
$f(0) = 3$, $f(3) = 0$, $f(5) = 2$. The V-shape graph is exactly the two piecewise branches joined at $x = 3$.

**Composed piecewise:**

[Very Hard] $f(x) = \begin{cases} x^2, & x < 0 \\ 2x + 1, & x \geq 0 \end{cases}$. Find $f(f(-1))$.
- Inner: $f(-1) = (-1)^2 = 1$ (first branch, since $-1 < 0$).
- Outer: $f(1) = 2(1) + 1 = 3$ (second branch, since $1 \geq 0$).
- Answer: 3.

❌ **Inner-first trap:** $f(f(-1))$ means apply $f$ to the OUTPUT $f(-1) = 1$ - the inner input $-1$ picks the first branch, but the outer input $1$ picks the second. Always evaluate inside-out.

---

## B2 Appendix 3: Inverse and Composition (moved from B2.3.10-11)

### B2.3.10 Inverse Functions

**Definition:** the inverse $f^{-1}$ undoes $f$: if $f$ sends $x$ to $y$, then $f^{-1}$ sends $y$ back to $x$. Graphically, the inverse is the reflection of the graph across the line $y = x$. Domain/range swap.

**Property:** $f^{-1}(f(x)) = x$, $f(f^{-1}(x)) = x$. Graph: reflection across $y = x$. Domain/range swap.

**Finding inverse:** replace $f(x)$ with $y$, swap $x$ and $y$, solve for $y$, replace $y$ with $f^{-1}(x)$.

[Medium] $f(x) = 2x + 5 \to y = 2x + 5 \to x = 2y + 5 \to f^{-1}(x) = \frac{x-5}{2}$

[Hard] $f(x) = \frac{3x-1}{x+2} \to x = \frac{3y-1}{y+2} \to x(y+2) = 3y - 1 \to xy + 2x = 3y - 1$ $\to xy - 3y = -2x - 1 \to y(x-3) = -(2x+1) \to f^{-1}(x) = -\frac{2x+1}{x-3}$

**SAT-style inverse evaluation:**

[Medium] If $f(x) = 2x - 7$, what is $f^{-1}(3)$?
- Find $x$ such that $f(x) = 3$: $2x - 7 = 3 \to x = 5$. So $f^{-1}(3) = 5$.

❌ **Swap-and-solve trap:** solving $f(x) = 3$ directly is faster than finding the full $f^{-1}(x)$ first.

[Hard] For $f(x) = \sqrt{x - 2} + 3$, $x \geq 2$, find $f^{-1}(x)$ and its domain.
- Swap: $x = \sqrt{y - 2} + 3 \to \sqrt{y-2} = x-3 \to y - 2 = (x-3)^2 \to f^{-1}(x) = (x-3)^2 + 2$.
- Domain of $f^{-1}$ = range of $f = [3, \infty)$ (since $\sqrt{x-2} \geq 0 \to f(x) \geq 3$).

❌ **Domain swap trap:** $f^{-1}$ domain is $f$'s range.

**Interpreting inverse in context:**

[Hard] The function $C(t) = 500(1.04)^t$ models the value of an investment after $t$ years. What does $C^{-1}(800)$ represent?

A) The value after $800$ years
B) The time it takes for the investment to reach $\$800$
C) The initial investment
D) The annual interest rate

$C^{-1}(800)$ asks: "How many years until the investment is worth $\$800$?" Answer: **B**.

❌ **Choice A trap:** $C^{-1}(800)$ is not "value at $t = 800$."

[Hard] If $f(x) = \frac{2x}{x-1}$ for $x \neq 1$, what is $f^{-1}(4)$?
- $f^{-1}(4)$: find $x$ s.t. $f(x) = 4$. $\frac{2x}{x-1} = 4 \to 2x = 4x - 4 \to -2x = -4 \to x = 2$.

---

### B2.3.11 Composition of Functions

**Definition:** composition chains functions: $(f \circ g)(x) = f(g(x))$ means "apply $g$ first, then feed the result to $f$." Order matters.

**Step-by-step method:**
1. Start with the innermost function: evaluate $g(x)$ (or the inner input).
2. Feed that output into the outer function $f$.
3. For domains: the composed function inherits restrictions from BOTH - $g$'s domain AND $f$'s domain applied to $g(x)$'s outputs.

$(f \circ g)(x) = f(g(x))$.

**Numeric composition:**

[Medium] $f(x) = x^2 + 1$, $g(x) = 3x - 2$. $f(g(4)) = f(10) = 101$.

[Medium] $f(x) = \sqrt{x}$, $g(x) = x + 5$. Evaluate $f(g(11))$: $g(11) = 16$, $f(16) = 4$.

**Symbolic composition:**

[Hard] $f(x) = x^2 + 1$, $g(x) = \sqrt{x - 1}$. Find $f(g(x))$ and $g(f(x))$.
- $f(g(x)) = (\sqrt{x-1})^2 + 1 = x - 1 + 1 = x$
- $g(f(x)) = \sqrt{(x^2 + 1) - 1} = \sqrt{x^2} = |x|$

❌ **Absolute value trap:** $g(f(x)) = \sqrt{x^2} = |x|$, not $x$.

**Domain of composition:**

[Hard] $f(x) = \sqrt{x+1}$, $g(x) = x^2 - 4$. Domain of $f(g(x)) = \sqrt{x^2 - 3}$: $x^2 - 3 \geq 0 \to |x| \geq \sqrt{3} \to (-\infty, -\sqrt{3}] \cup [\sqrt{3}, \infty)$.

[Very Hard] $f(x) = \frac{1}{x-2}$, $g(x) = \sqrt{x+1}$. Find domain of $f(g(x))$.
- $f(g(x)) = \frac{1}{\sqrt{x+1} - 2}$. Restrictions: (1) $\sqrt{x+1}$ requires $x \geq -1$. (2) Denominator $\neq 0$: $\sqrt{x+1} \neq 2 \to x+1 \neq 4 \to x \neq 3$. Domain: $[-1, 3) \cup (3, \infty)$.

**Composition as "applying one after another":**

[Medium] $f(x) = 2x$, $g(x) = x + 1$. What does $g(f(x))$ represent vs $f(g(x))$?
- $g(f(x))$: first double, then add $1 \to 2x + 1$.
- $f(g(x))$: first add $1$, then double $\to 2x + 2$. Order matters.

**Value from a table (SAT style):**

[Medium] Given $f(1) = 3$, $f(3) = 7$, $g(1) = 5$, $g(3) = 1$, find $f(g(3))$.
- $g(3) = 1$, then $f(1) = 3$. Answer: $3$.
