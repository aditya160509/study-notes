# Digital SAT Advanced Math | Domain B2

**Weight:** ~35% (13-15 of 44 questions) | **Prerequisite:** Algebra I + II | **Key Skill:** Nonlinear relationships — quadratics, exponentials, polynomials, radicals, rationals, and systems

**Domain cross-references:** B1 (Algebra) for linear prerequisite skills | B3 (Data Analysis) for exponential models in context | B4 (Geometry & Trig) for circle equations, triangle problems using quadratics

### Official Blueprint Mapping

| Skill Domain | Blueprint Code | B2 Section(s) |
|---|---|---|
| Equivalent expressions | 2.2.A | B2.1 |
| Nonlinear equations in one variable | 2.2.B | B2.2.1–B2.2.6 |
| Systems of equations (nonlinear) | 2.2.C | B2.2.7 |
| Nonlinear functions | 2.2.D | B2.3 |

**Question distribution:** ~7-9 on expressions/equations, ~5-7 on functions/graphs, ~1-2 on systems.

---

## Complete Formula Reference

### Exponent Rules

| Rule | Formula |
|---|---|
| Product | $a^m \cdot a^n = a^{m+n}$ |
| Quotient | $\frac{a^m}{a^n} = a^{m-n}$ |
| Power of a power | $(a^m)^n = a^{mn}$ |
| Power of a product | $(ab)^n = a^n b^n$ |
| Power of a quotient | $\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}$ |
| Zero exponent | $a^0 = 1$ (provided $a \neq 0$) |
| Negative exponent | $a^{-n} = \frac{1}{a^n}$ |
| Rational exponent | $a^{m/n} = \sqrt[n]{a^m} = (\sqrt[n]{a})^m$ |

### Radical Rules

| Rule | Formula |
|---|---|
| Product | $\sqrt[n]{ab} = \sqrt[n]{a} \cdot \sqrt[n]{b}$ |
| Quotient | $\sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}}$ |
| Power | $(\sqrt[n]{a})^m = \sqrt[n]{a^m}$ |
| Rationalize | $\frac{1}{\sqrt{a}} = \frac{\sqrt{a}}{a}$ |
| Conjugate | $(a+b)(a-b) = a^2 - b^2$; rationalize $\frac{1}{\sqrt{a}+\sqrt{b}}$ via conjugate |

### Factoring Identities

| Name | Formula |
|---|---|
| GCF | Factor out shared factor from all terms |
| Difference of squares | $a^2 - b^2 = (a-b)(a+b)$ |
| Perfect square (sum) | $a^2 + 2ab + b^2 = (a+b)^2$ |
| Perfect square (diff) | $a^2 - 2ab + b^2 = (a-b)^2$ |
| Sum of cubes | $a^3 + b^3 = (a+b)(a^2 - ab + b^2)$ |
| Diff of cubes | $a^3 - b^3 = (a-b)(a^2 + ab + b^2)$ |
| General trinomial | $x^2 + bx + c = (x+p)(x+q)$ where $p+q=b,\; pq=c$ |
| Grouping (4 terms) | Group pairs, factor each, extract common binomial |

### Quadratic Formula and Discriminant

$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ where $ax^2 + bx + c = 0$

$D = b^2 - 4ac$:
- $D > 0$: 2 distinct real solutions
- $D = 0$: 1 real solution (double root)
- $D < 0$: 0 real solutions (complex)

### Vertex Forms

**Standard to vertex:** $f(x) = ax^2 + bx + c \to f(x) = a(x-h)^2 + k$

$h = -\frac{b}{2a},\quad k = f(h)$

**Completing the square:** $x^2 + bx = \left(x + \frac{b}{2}\right)^2 - \left(\frac{b}{2}\right)^2$

### Quadratic Forms

| Form | Expression | Reveals |
|---|---|---|
| Standard | $ax^2 + bx + c$ | $y$-intercept $(0,c)$, end behavior from $a$ |
| Vertex | $a(x-h)^2 + k$ | Vertex $(h,k)$, axis $x=h$, min/max $k$ |
| Factored | $a(x-r_1)(x-r_2)$ | Roots $r_1, r_2$, axis of symmetry $x = \frac{r_1+r_2}{2}$ |

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

### End Behavior (Polynomials)

Leading term $ax^n$ determines both ends:
- $n$ even, $a > 0$: both $\to +\infty$
- $n$ even, $a < 0$: both $\to -\infty$
- $n$ odd, $a > 0$: left $-\infty$, right $+\infty$
- $n$ odd, $a < 0$: left $+\infty$, right $-\infty$

### Asymptotes (Rational Functions)

- **Vertical:** denominator $= 0$, numerator $\neq 0$ at that $x$
- **Horizontal:**
  - deg num $<$ deg den: $y = 0$
  - deg num $=$ deg den: $y = \frac{\text{leading coefficient}_n}{\text{leading coefficient}_d}$
  - deg num $>$ deg den: no horizontal asymptote (oblique possible)

### Exponential Functions

- **General:** $f(x) = a \cdot b^x$ where $a = f(0)$
- **Growth:** $b > 1$, $b = 1 + r$ where $r$ is growth rate
- **Decay:** $0 < b < 1$, $b = 1 - r$ where $r$ is decay rate
- **Doubling:** $f(x) = a \cdot 2^{x/d}$ (doubles every $d$ units)
- **Half-life:** $f(x) = a \cdot \left(\frac{1}{2}\right)^{x/h}$ (halves every $h$ units)

### Transformations

| Operation | Effect | Notation |
|---|---|---|
| Shift up $k$ | Moves up | $f(x) + k,\; k > 0$ |
| Shift down $k$ | Moves down | $f(x) - k,\; k > 0$ |
| Shift left $h$ | Moves left | $f(x + h),\; h > 0$ |
| Shift right $h$ | Moves right | $f(x - h),\; h > 0$ |
| Reflect $x$-axis | Flips vertical | $-f(x)$ |
| Reflect $y$-axis | Flips horizontal | $f(-x)$ |
| Vertical stretch | Steeper | $a \cdot f(x),\; a > 1$ |
| Vertical compress | Flatter | $a \cdot f(x),\; 0 < a < 1$ |

### Multiplicity at Roots

- **Odd** (1, 3, 5, ...): crosses the $x$-axis
- **Even** (2, 4, 6, ...): touches and turns (bounces)

---

## B2.1 — Equivalent Expressions

### B2.1.1 Operations with Polynomials

**Addition/Subtraction:** Combine like terms (same variable, same exponent).

[Easy] $(3x^2 - 5x + 2) + (x^2 + 7x - 4) = 4x^2 + 2x - 2$

[Medium] $(4x^3 - 2x^2 + 3) - (x^3 + 5x^2 - 7) = 4x^3 - 2x^2 + 3 - x^3 - 5x^2 + 7 = 3x^3 - 7x^2 + 10$

❌ **Sign error trap:** $-(x^3 + 5x^2 - 7) = -x^3 - 5x^2 + 7$, not $-x^3 + 5x^2 - 7$.

**Multiplication:** Distribute each term of the first to every term of the second.

[Medium] $(x+3)(x^2 - 2x + 5) = x(x^2 - 2x + 5) + 3(x^2 - 2x + 5) = x^3 - 2x^2 + 5x + 3x^2 - 6x + 15 = x^3 + x^2 - x + 15$

---

### B2.1.2 Factoring

#### Pattern Cheat Table

| Pattern | Form | Example |
|---|---|---|
| GCF | $ab + ac = a(b+c)$ | $12x^3 - 8x^2 + 4x = 4x(3x^2 - 2x + 1)$ |
| Diff of squares | $a^2 - b^2 = (a-b)(a+b)$ | $x^2 - 49 = (x-7)(x+7)$ |
| Perfect square | $a^2 \pm 2ab + b^2 = (a \pm b)^2$ | $x^2 + 10x + 25 = (x+5)^2$ |
| Sum of cubes | $a^3 + b^3 = (a+b)(a^2 - ab + b^2)$ | $x^3 + 8 = (x+2)(x^2 - 2x + 4)$ |
| Diff of cubes | $a^3 - b^3 = (a-b)(a^2 + ab + b^2)$ | $x^3 - 27 = (x-3)(x^2 + 3x + 9)$ |
| Simple trinomial | $x^2 + bx + c = (x+p)(x+q)$, $p+q=b$, $pq=c$ | $x^2 - 7x + 12 = (x-3)(x-4)$ |
| Hard trinomial | $ax^2 + bx + c$, $a\neq1$, via grouping | $6x^2 + 13x - 5 = (3x-1)(2x+5)$ |
| Grouping | 4 terms, group in pairs | $x^3 + 3x^2 - 4x - 12 = (x+3)(x-2)(x+2)$ |

**Order of operations:** GCF first → count terms → apply pattern → check if any factor factors further.

#### Difference of Squares

[Easy] $x^2 - 49 = (x - 7)(x + 7)$

[Hard] $x^4 - 16 = (x^2 - 4)(x^2 + 4) = (x - 2)(x + 2)(x^2 + 4)$

❌ **Sum-of-squares trap:** $x^2 + 49$ is NOT factorable over reals. $a^2 + b^2$ does not factor.
❌ **Partial factoring trap:** Stopping at $(x^2 - 4)(x^2 + 4)$ when $x^2 - 4$ factors further.

#### Perfect Square Trinomials

[Medium] $4x^2 - 12x + 9 = (2x - 3)^2$

⚡ Quick test: first and last terms must be perfect squares. Middle term must equal $\pm 2\sqrt{\text{first}}\sqrt{\text{last}}$.

#### General Trinomials

**When $a = 1$:** Find $p+q=b$, $pq=c$.

[Medium] $x^2 - 7x + 12 = (x-3)(x-4)$

**When $a \neq 1$:** Factor by grouping (split the middle term).

[Hard] $6x^2 + 13x - 5$
1. $a \cdot c = 6(-5) = -30$.
2. Factors of $-30$ that sum to $13$: $15$ and $-2$.
3. Rewrite: $6x^2 + 15x - 2x - 5$
4. Group: $3x(2x+5) - 1(2x+5) = (3x-1)(2x+5)$

❌ **Sign-error trap:** List ALL factor pairs before deciding. $10$ and $-3$ sum to $7$ (wrong).
⚡ Desmos: Graph $y = 6x^2 + 13x - 5$. $x$-intercepts at $\frac{1}{3}$ and $-\frac{5}{2}$ confirm $(3x-1)(2x+5)$.

#### Sum and Difference of Cubes

[Medium] $x^3 + 8 = (x + 2)(x^2 - 2x + 4)$

❌ **Sign trap:** Quadratic factor always has the OPPOSITE middle sign. $a^3 + b^3 \to a^2 - ab + b^2$ (minus).

#### Factoring by Grouping

[Medium] $x^3 + 3x^2 - 4x - 12 = x^2(x+3) - 4(x+3) = (x+3)(x^2 - 4) = (x+3)(x-2)(x+2)$

❌ **GCF trap:** If the leading coefficient of a pair is negative, factor out the negative.

#### Factoring Decision Quick Reference

| Terms | First Check | Then Try |
|---|---|---|
| 2 | GCF | Diff of squares, sum/diff of cubes |
| 3 | GCF | Perfect square? If not, trinomial method |
| 4 | GCF | Grouping |
| After | — | Can any factor be factored further? |

---

### B2.1.3 Expanding Products

**FOIL (Binomial $\times$ Binomial):**
[Easy] $(2x-3)(x+5) = 2x^2 + 10x - 3x - 15 = 2x^2 + 7x - 15$

**Special Products to Recognize Instantly:**

| Identity | Expanded |
|---|---|
| $(a+b)^2$ | $a^2 + 2ab + b^2$ |
| $(a-b)^2$ | $a^2 - 2ab + b^2$ |
| $(a+b)(a-b)$ | $a^2 - b^2$ |
| $(a+b)^3$ | $a^3 + 3a^2b + 3ab^2 + b^3$ |
| $(a-b)^3$ | $a^3 - 3a^2b + 3ab^2 - b^3$ |

[Medium] $(2x - 5y)^2 = 4x^2 - 20xy + 25y^2$
❌ **Middle-term trap:** $(2x-5y)^2 \neq 4x^2 + 25y^2$. The $-20xy$ is essential.

[Hard] $(x-2)(x+2)(x^2+4) = (x^2-4)(x^2+4) = x^4 - 16$

[Very Hard] $(x^2 + 2x - 3)(x^2 - 2x + 3) = [x^2 + (2x-3)][x^2 - (2x-3)] = (x^2)^2 - (2x-3)^2$ $= x^4 - (4x^2 - 12x + 9) = x^4 - 4x^2 + 12x - 9$

⚡ Recognize $(A+B)(A-B) = A^2 - B^2$ even when $A$ and $B$ are expressions.

---

### B2.1.4 Rational Expressions and Complex Fractions

**Simplifying:** Factor numerator and denominator, then cancel common factors. Restrictions from cancelled factors remain.

[Medium] $\frac{x^2 - 9}{x^2 + 5x + 6} = \frac{(x-3)(x+3)}{(x+3)(x+2)} = \frac{x-3}{x+2}$, $x \neq -3, -2$

❌ **Cancellation trap:** Cancel FACTORS, not terms. $\frac{x+3}{x}$ cannot simplify.
❌ **Sign flip trap:** $\frac{x-3}{3-x} = -1$, not $1$. Factor $-1$: $\frac{x-3}{-(x-3)} = -1$.

**Addition/Subtraction:** Use common denominator.

[Medium] $\frac{3}{x+2} + \frac{5}{x-2} = \frac{3(x-2) + 5(x+2)}{(x+2)(x-2)} = \frac{8x+4}{(x+2)(x-2)} = \frac{4(2x+1)}{x^2-4}$

[Hard] $\frac{2x}{x^2-1} - \frac{1}{x+1} = \frac{2x}{(x-1)(x+1)} - \frac{x-1}{(x-1)(x+1)} = \frac{2x - (x-1)}{(x-1)(x+1)} = \frac{x+1}{(x-1)(x+1)} = \frac{1}{x-1}$

❌ **Critical subtraction trap:** $-(x-1) = -x + 1$, NOT $-x - 1$. Distribute the minus to ALL terms.

**Multiplication:** Factor everything, cancel common factors, then multiply remaining.

[Medium] $\frac{x^2 - 9}{x+2} \cdot \frac{x^2 - 4}{x-3} = \frac{(x-3)(x+3)}{x+2} \cdot \frac{(x-2)(x+2)}{x-3} = (x+3)(x-2)$

**Division:** Multiply by the reciprocal.

[Medium] $\frac{x^2 - 4}{x+1} \div \frac{x-2}{x+3} = \frac{(x-2)(x+2)}{x+1} \cdot \frac{x+3}{x-2} = \frac{(x+2)(x+3)}{x+1}$

**Complex Fractions (nested fractions):** Multiply numerator and denominator by the LCD of all internal fractions.

[Hard] Simplify $\frac{1 + \frac{1}{x}}{1 - \frac{1}{x}}$
- LCD of internal fractions is $x$. Multiply: $\frac{x(1 + \frac{1}{x})}{x(1 - \frac{1}{x})} = \frac{x + 1}{x - 1}$

[Hard] $\frac{\frac{1}{x} + \frac{2}{x+1}}{\frac{3}{x}}$
- Multiply num/den by LCD $x(x+1)$: $\frac{(x+1) + 2x}{3(x+1)} = \frac{3x+1}{3x+3}$

---

### B2.1.5 Rewriting Radicals and Exponents

**Core conversion:** $\sqrt[n]{x^m} = x^{m/n}$

[Easy] $\sqrt[3]{x^2} = x^{2/3}$
[Medium] $(\sqrt[4]{x})^3 = x^{3/4}$
[Hard] $\sqrt[3]{x^4 y^2} \cdot \sqrt{xy^3} = x^{4/3}y^{2/3} \cdot x^{1/2}y^{3/2} = x^{4/3 + 1/2} y^{2/3 + 3/2} = x^{11/6} y^{13/6}$

❌ **Exponent addition trap:** $x^{1/2} \cdot x^{1/3} = x^{5/6}$, not $x^{1/6}$.
❌ **Radical-of-square trap:** $\sqrt{x^2} = |x|$, not $x$. SAT rarely tests the absolute value nuance, but know it.

⚡ Convert radicals to fractional exponents first — faster and less error-prone.

**Rationalizing Denominators:**

[Medium] $\frac{3}{\sqrt{2}} = \frac{3\sqrt{2}}{2}$
[Hard] $\frac{5}{2 - \sqrt{3}} = \frac{5(2 + \sqrt{3})}{(2 - \sqrt{3})(2 + \sqrt{3})} = \frac{5(2 + \sqrt{3})}{4 - 3} = 5(2 + \sqrt{3})$

❌ **Conjugate trap:** Must use the conjugate (change the middle sign). Using $(2-\sqrt{3})$ again does NOT eliminate the radical.

---

### B2.1.6 Completing the Square

$x^2 + bx \to \left(x + \frac{b}{2}\right)^2 - \left(\frac{b}{2}\right)^2$

[Medium] $x^2 + 8x + 3 = (x^2 + 8x + 16) - 16 + 3 = (x+4)^2 - 13$

[Hard] $2x^2 - 12x + 5 = 2(x^2 - 6x) + 5 = 2(x^2 - 6x + 9 - 9) + 5 = 2[(x-3)^2 - 9] + 5 = 2(x-3)^2 - 13$

❌ **Leading coefficient trap:** $2(-9) = -18$, not $-9$. The subtracted term must be multiplied by $a$.
⚡ Desmos: Graph the quadratic, click the vertex — read $h$ and $k$ directly.

---

### B2.1.7 Polynomial Theorems

**Remainder Theorem:** $f(a)$ = remainder when $f(x)$ is divided by $(x-a)$.

[Medium] What is the remainder when $x^3 - 5x^2 + 7$ is divided by $x + 2$?
$f(-2) = -8 - 20 + 7 = -21$. Answer: $-21$.

❌ **Sign trap:** $x+2 = x - (-2)$, so $a = -2$, not $2$.

**Factor Theorem:** $f(a) = 0 \iff (x-a)$ is a factor.

[Hard] Which of the following is a factor of $x^3 - 7x + 6$?

A) $x - 3$  
B) $x + 2$  
C) $x + 1$  
D) All of the above  

Test $f(3) = 27 - 21 + 6 = 12 \neq 0$ ❌. Test $f(-2) = -8 + 14 + 6 = 12 \neq 0$ ❌. Test $f(-1) = -1 + 7 + 6 = 12 \neq 0$ ❌. None are factors. Wait — test $f(1) = 1 - 7 + 6 = 0$, so $x-1$ is a factor. Since it's not listed, check: $f(2) = 8 - 14 + 6 = 0$, so $x-2$ is a factor. The question asks for a factor — none of A-C work. This is trick: actually $f(1)=0$, $f(2)=0$, $f(-3)=0$, so $x-1$, $x-2$, $x+3$ are all factors. Since none listed, the answer requires testing all. But note: $(x+2)$ gives $f(-2) = 12$, not $0$.

⏹ Wait — correct check: $x^3 - 7x + 6$: $f(1) = 0$, $f(2) = 0$, $f(-3) = 0$. So $x-1$, $x-2$, $x+3$ are factors. None match A-C, so none is a factor.

❌ **Intuition trap:** Students assume one of the given answers must be correct. Always verify each independently.

⚡ **Remainder Theorem shortcut:** Only need remainder? Compute $f(a)$. No division needed.

**Degree bound:** A polynomial of degree $n$ has at most $n$ real roots and at most $n-1$ turning points.

---

### B2.1.8 Equivalent Forms of Quadratics

[Medium] $f(x) = 2(x-3)^2 + 5$: vertex $(3,5)$, min $= 5$, axis $x = 3$, opens up, $y$-intercept at $23$.

[Hard] A quadratic has $x$-intercepts $x = -2$ and $x = 5$, passes through $(1, 6)$. Find standard form.
- $f(x) = a(x+2)(x-5)$. Plug $(1,6)$: $6 = a(3)(-4) = -12a \to a = -\frac{1}{2}$
- $f(x) = -\frac{1}{2}(x+2)(x-5) = -\frac{1}{2}(x^2 - 3x - 10) = -\frac{1}{2}x^2 + \frac{3}{2}x + 5$

[Very Hard] Quadratic has vertex $(4, -2)$ and passes through $(2, 10)$. Find $f(x)$.

**Graph-first (reverse direction):** SAT often gives the graph/description and asks for the equation.

[Hard] The graph of a quadratic function has $x$-intercepts at $x = -3$ and $x = 1$, and opens downward. Which of the following could represent the function?

A) $f(x) = -(x+3)(x-1)$  
B) $f(x) = (x+3)(x-1)$  
C) $f(x) = -(x-3)(x+1)$  
D) $f(x) = (x-3)(x+1)$  

$x$-intercepts at $-3$ and $1$ means factors $(x+3)(x-1)$. Opens down means negative leading coefficient. Answer: **A**.

❌ **Choice C trap:** Signs reversed — $(x-3)(x+1)$ gives intercepts $3$ and $-1$.

[Hard] The graph of $y = f(x)$ is shown. The vertex is at $(2, -3)$ and the parabola passes through $(0, 1)$. Which equation represents $f(x)$?

A) $f(x) = (x-2)^2 - 3$  
B) $f(x) = (x-2)^2 + 3$  
C) $f(x) = (x+2)^2 - 3$  
D) $f(x) = (x-2)^2 - 1$  

Vertex form: $f(x) = a(x-2)^2 - 3$. Plug $(0,1)$: $1 = a(4) - 3 \to a = 1$. So $f(x) = (x-2)^2 - 3$. Answer: **A**.

❌ **Choice C trap:** $(x+2)^2$ shifts LEFT, not right.

**Function notation traps — distinguishing $f(x+2)$ from $f(x)+2$:**

[Medium] For $f(x) = x^2$, evaluate $f(x+2)$ vs $f(x)+2$.

$f(x+2) = (x+2)^2 = x^2 + 4x + 4$ (shift left 2, entire parabola moves)  
$f(x)+2 = x^2 + 2$ (shift up 2, parabola stays in place vertically)

❌ **Notation trap:** Students write $f(x+2) = x^2 + 2$, confusing the two.

[Hard] If $f(x) = 3x - 1$, which is greater: $f(x+3)$ or $f(x)+3$?

$f(x+3) = 3(x+3) - 1 = 3x + 8$  
$f(x)+3 = 3x - 1 + 3 = 3x + 2$  
$f(x+3)$ is always greater by $6$.

---
- $f(x) = a(x-4)^2 - 2$. Plug $(2,10)$: $10 = a(4) - 2 \to a = 3$
- $f(x) = 3(x-4)^2 - 2 = 3x^2 - 24x + 46$

⚡ Desmos: Enter points as a table, fit $y_1 \sim ax_1^2 + bx_1 + c$ for instant quadratic regression.

---

### B2.1.9 "Which Expression Is Equivalent?" (SAT Style)

SAT rarely says "Simplify" — it says "Which of the following is equivalent to ...?" or "Which expression is equivalent to ...?"

**Strategy:** Eliminate wrong forms by testing a single numeric value (pick $x = 2$ or $x = 1$). If the original and a choice differ at that value, that choice is wrong.

**Radicals:**

[Medium] Which expression is equivalent to $\frac{\sqrt{18x^3}}{\sqrt{2x}}$ for $x > 0$?

A) $3x$  
B) $3\sqrt{x}$  
C) $9x$  
D) $3x\sqrt{2}$  

Simplify: $\sqrt{\frac{18x^3}{2x}} = \sqrt{9x^2} = 3x$. Answer: **A**.

❌ **Choice C trap:** $9x$ — student simplifies $\frac{18}{2} = 9$ but forgets square root.

[Hard] Which expression is equivalent to $\frac{x^2 - 16}{x^2 - 8x + 16}$ for $x \neq 4$?

A) $\frac{x-4}{x+4}$  
B) $\frac{x+4}{x-4}$  
C) $\frac{x+4}{x+4}$  
D) $1$  

Factor: $\frac{(x-4)(x+4)}{(x-4)^2} = \frac{x+4}{x-4}$. Answer: **B**.

❌ **Choice A trap:** Reversed numerator and denominator.  
❌ **Choice D trap:** Cancel $(x-4)$ from top and bottom without checking — leaves wrong factor.

**Exponent Rules:**

[Hard] Which expression is equivalent to $\frac{8x^6 y^{-3}}{2x^{-2} y^5}$ for $x, y \neq 0$?

A) $4x^4 y^{-8}$  
B) $4x^8 y^{-8}$  
C) $6x^4 y^2$  
D) $4x^8 y^2$  

$\frac{8}{2} = 4$, $x^{6 - (-2)} = x^8$, $y^{-3 - 5} = y^{-8}$. Answer: **B**.

❌ **Choice A trap:** $6 - (-2) = 8$, not $4$. Students subtract incorrectly.  
❌ **Choice D trap:** $y^{-3} - 5 = -8$, not $2$. Sign error.

**Completing the Square Form:**

[Hard] Which expression is equivalent to $2x^2 - 12x + 5$?

A) $2(x-3)^2 - 13$  
B) $2(x-3)^2 - 4$  
C) $(x-3)^2 - 13$  
D) $2(x-6)^2 - 31$  

Complete square: $2(x^2 - 6x) + 5 = 2(x-3)^2 - 18 + 5 = 2(x-3)^2 - 13$. Answer: **A**.

❌ **Choice C trap:** Forgets to multiply the $(-9)$ by the leading coefficient $2$.

---

### B2.1.10 Equivalent Forms of Quadratics (Convert Between Forms)

[Medium] Which expression is equivalent to $x^2 + 10x + 24$?

A) $(x+4)(x+6)$  
B) $(x+5)^2 - 1$  
C) $(x+12)(x-2)$  
D) Both A and B  

Check A: $(x+4)(x+6) = x^2 + 10x + 24$ ✅. Check B: $(x+5)^2 - 1 = x^2 + 10x + 25 - 1$ ✅. Answer: **D**.

❌ **Choice C trap:** $(x+12)(x-2) = x^2 + 10x - 24$ — sign error on constant term.

[Hard] The expression $3x^2 - 12x + 7$ can be written in vertex form $a(x-h)^2 + k$. What is $h + k$?

A) $-5$  
B) $1$  
C) $5$  
D) $7$  

Vertex: $h = -\frac{-12}{6} = 2$, $k = 3(2)^2 - 12(2) + 7 = 12 - 24 + 7 = -5$. $h + k = 2 + (-5) = -3$. Answer: None of above — answer is $-3$.

❌ **Choice A trap:** $k = -5$, student answers $k$ instead of $h+k$.

---

### B2.1 Summary

| Operation | Key Move | Common Error |
|---|---|---|
| Adding rational expressions | Find LCD first | Adding numerators without common denom |
| Simplifying radicals | Convert to fractional exponents | $x^{1/2} \cdot x^{1/3} = x^{1/6}$ |
| "Which expression is equivalent?" | Test a numeric value | Picking the first that looks plausible |
| Completing the square | Factor $a$ first, multiply subtraction by $a$ | Forgetting to multiply $a$ through |
| Equivalent quadratic forms | Match: standard → vertex → factored | Confusing $h$ sign in vertex form |

---

## B2.2 — Nonlinear Equations in One Variable and Systems

### B2.2.1 Quadratic Equations — Best Method Decision Flow

**Decision tree:**
1. Is it $ax^2 + c = 0$ (no $x$ term)? → **Square root method**
2. Are $a$, $b$, $c$ integers and $a=1$? → Try **factoring** (find $p+q=b$, $pq=c$)
3. Do you need vertex form anyway? → **Complete the square**
4. Messy coefficients or unsure? → **Quadratic formula** (always works)
5. Need exact radical form? → Quadratic formula. Need decimal? → Desmos.

| Method | When to Use | Speed |
|---|---|---|
| Factoring | Integer coefficients, factorable quickly | Fastest |
| Square root | No $x$ term ($ax^2 + c = 0$) | Fast |
| Quadratic formula | Any quadratic, messy coefficients | Always works |
| Completing the square | Need vertex form anyway | Medium |

**Factoring:** [Medium] $x^2 - 5x + 6 = 0 \to (x-2)(x-3) = 0 \to x = 2, 3$

**Square Root:** [Medium] $3(x-4)^2 = 27 \to (x-4)^2 = 9 \to x-4 = \pm 3 \to x = 7, 1$

❌ **Missing negative root trap:** $x^2 = 25$ gives $x = \pm 5$, not $x = 5$ only.

**Quadratic Formula:** $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$

[Hard] $2x^2 - 7x = 3 \to 2x^2 - 7x - 3 = 0$
$x = \frac{7 \pm \sqrt{49 - 4(2)(-3)}}{4} = \frac{7 \pm \sqrt{49 + 24}}{4} = \frac{7 \pm \sqrt{73}}{4}$

❌ **Sign-error trap:** $b = -7$, so $-b = +7$. Write $-(-7)$ explicitly.
❌ **c sign trap:** $c = -3$, so $-4ac = -4(2)(-3) = +24$, not $-24$.

**Completing the Square to Solve:**

[Medium] $x^2 + 6x + 5 = 0$
- $x^2 + 6x = -5 \to x^2 + 6x + 9 = 4 \to (x+3)^2 = 4 \to x + 3 = \pm 2 \to x = -1, -5$

**Best method practice:**

[Medium] Which method is fastest for $3x^2 - 27 = 0$?
Square root: $x^2 = 9 \to x = \pm 3$.

[Medium] Which method for $x^2 + 5x + 6 = 0$?
Factoring: $(x+2)(x+3) = 0 \to x = -2, -3$.

[Hard] Which method for $3x^2 - 5x + 1 = 0$?
Quadratic formula: $x = \frac{5 \pm \sqrt{25 - 12}}{6} = \frac{5 \pm \sqrt{13}}{6}$ (does not factor cleanly).

**Discriminant Analysis:** $D = b^2 - 4ac$

| $D$ | Real Solutions | Graph |
|---|---|---|
| $> 0$ | 2 distinct | Two $x$-intercepts |
| $= 0$ | 1 (double root) | Vertex on $x$-axis |
| $< 0$ | 0 | No $x$-intercepts |

[Medium] $3x^2 - 2x + 5 = 0$: $D = 4 - 60 = -56$ — no real solutions.

[Hard] For what $k$ does $x^2 + kx + 9 = 0$ have exactly one solution?
$D = k^2 - 36 = 0 \to k = \pm 6$

❌ **Double-root trap:** Both $k = 6$ AND $k = -6$ give one solution. Students commonly forget $k = -6$.

[Very Hard] For what $k$ does $2x^2 - 4x + k = 0$ have two distinct solutions?
$D = 16 - 8k > 0 \to k < 2$

**Vieta's Formulas:**

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

### B2.2.2 Quadratic in Form (u-Substitution)

[Hard] $x^4 - 5x^2 + 6 = 0$: let $u = x^2$. $u^2 - 5u + 6 = 0 \to u = 2, 3$. Then $x = \pm\sqrt{2}, \pm\sqrt{3}$.

[Very Hard] $(x^2 - 3x)^2 - 2(x^2 - 3x) - 8 = 0$: let $u = x^2 - 3x$.
- $u^2 - 2u - 8 = 0 \to u = 4, -2$
- $x^2 - 3x = 4 \to x = 4, -1$
- $x^2 - 3x = -2 \to x = 1, 2$
- Solutions: $4, -1, 1, 2$

❌ **Back-substitution trap:** Each $u$ may produce 0, 1, or 2 $x$ values. Solve for original variable.

---

### B2.2.3 Radical Equations

**Method:** Isolate the radical, raise to the power, ALWAYS check for extraneous roots.

[Hard] $\sqrt{2x + 3} + 5 = x$
1. $\sqrt{2x + 3} = x - 5$
2. $2x + 3 = x^2 - 10x + 25 \to 0 = x^2 - 12x + 22$
3. $x = \frac{12 \pm \sqrt{144 - 88}}{2} = 6 \pm \sqrt{14}$
4. Check $6 + \sqrt{14} \approx 9.74$: $\sqrt{22.48} + 5 \approx 9.74$ ✅
5. Check $6 - \sqrt{14} \approx 2.26$: $\sqrt{7.52} + 5 \approx 7.74 \neq 2.26$ ❌ **Extraneous**
6. Answer: $x = 6 + \sqrt{14}$ only

[Hard] $\sqrt{x+7} - \sqrt{x-1} = 2$
1. $\sqrt{x+7} = \sqrt{x-1} + 2$
2. Square: $x+7 = (x-1) + 4\sqrt{x-1} + 4 \to 4 = 4\sqrt{x-1} \to 1 = \sqrt{x-1} \to x = 2$
3. Check: $\sqrt{9} - \sqrt{1} = 3 - 1 = 2$ ✅

❌ **No-check trap:** Both answers may seem algebraically valid, but only one may satisfy the original.
❌ **Pre-squaring trap:** Squaring without isolating the radical first creates cross-term mayhem.

---

### B2.2.4 Rational Equations

**Method:** Multiply by LCD, solve resulting polynomial, exclude restricted values.

[Medium] $\frac{5}{x} + \frac{3}{2} = \frac{7}{4}$: multiply by $4x \to 20 + 6x = 7x \to x = 20$. Restriction $x \neq 0$ ✅.

[Hard] $\frac{x}{x-3} + \frac{2}{x+1} = \frac{5}{x^2 - 2x - 3}$
- Factor: $x^2 - 2x - 3 = (x-3)(x+1)$
- Multiply by $(x-3)(x+1)$: $x(x+1) + 2(x-3) = 5 \to x^2 + 3x - 11 = 0$
- $x = \frac{-3 \pm \sqrt{53}}{2}$. Restrictions $x \neq 3, -1$, neither violated ✅.

❌ **Restrictions trap:** Forgetting to exclude values that zero any denominator.

[Very Hard] $\frac{2x}{x-4} = 3 + \frac{16}{x-4}$: multiply by $(x-4) \to 2x = 3(x-4) + 16 \to x = -4$. $x \neq 4$ ✅.

⚡ If the equation is $\frac{A}{B} = \frac{C}{D}$ (proportion form), cross-multiply directly: $AD = BC$.

---

### B2.2.5 Absolute Value Equations and Graphs

**Method:** $|A| = B$ (with $B \geq 0$) $\to A = B$ or $A = -B$

[Easy] $|x - 3| = 7 \to x = 10$ or $x = -4$

[Medium] $|2x + 5| - 3 = 10 \to |2x + 5| = 13 \to x = 4$ or $x = -9$

❌ **No-solution trap:** $|x| = -5$ has no solution. Absolute value cannot be negative.

[Hard] $|x - 2| = |3x + 1| \to x - 2 = 3x + 1$ or $x - 2 = -(3x+1) \to x = -\frac{3}{2}, \frac{1}{4}$

⚡ Desmos: Graph $y = |x-2|$ and $y = |3x+1|$; intersections give solutions.

**Absolute value graph interpretation:**

The graph of $f(x) = a|x - h| + k$ is a V-shape with vertex $(h,k)$, opening up if $a>0$, down if $a<0$.

[Medium] Which graph represents $f(x) = -2|x - 3| + 4$?

Vertex at $(3,4)$, opens down, steepness $2$. The $x$-intercepts: $0 = -2|x-3| + 4 \to |x-3| = 2 \to x = 1, 5$.

❌ **Vertex sign trap:** $|x-3|$ has vertex at $x = 3$, not $x = -3$.

[Hard] The graph of $y = |x + 1| + 2$ is shifted right 3 and down 4. What is the new vertex?

Original vertex: $(-1, 2)$. Shift right 3: $(2, 2)$. Down 4: $(2, -2)$.

---

### B2.2.6 Exponential Equations

**Same-base method:** If $a^{f(x)} = a^{g(x)}$, then $f(x) = g(x)$.

**Key base conversions to memorize:** $4=2^2$, $8=2^3$, $9=3^2$, $16=2^4$, $25=5^2$, $27=3^3$, $32=2^5$, $64=2^6=4^3=8^2$, $81=3^4$, $125=5^3$.

[Medium] $2^{3x-1} = 2^{x+7} \to 3x - 1 = x + 7 \to x = 4$

[Hard] $3^{x^2 - 4} = 27^{x+2} \to 3^{x^2-4} = 3^{3x+6} \to x^2 - 3x - 10 = 0 \to x = 5, -2$

❌ **Different-base trap:** MUST rewrite to the same base before equating exponents.

[Very Hard] $4^x - 2^{x+1} = 8$
- Rewrite $4^x = 2^{2x}$, $2^{x+1} = 2 \cdot 2^x$. Let $u = 2^x$: $u^2 - 2u - 8 = 0 \to u = 4, -2$.
- $u = 4 \to 2^x = 4 \to x = 2$. $u = -2$: reject ($2^x > 0$ for all real $x$).

❌ **Exponential positivity trap:** $b^x$ is ALWAYS positive. Reject any $u$-solution $\leq 0$.

⚡ If bases cannot be matched cleanly, graph both sides in Desmos and find the intersection.

---

### B2.2.7 Systems of Equations (Linear + Nonlinear)

**General Strategy:** Substitute the linear equation into the nonlinear one, solve, back-substitute.

**Linear + Quadratic:**

[Medium] $y = 2x + 1$, $y = x^2 - 2x + 3 \to 2x + 1 = x^2 - 2x + 3 \to x^2 - 4x + 2 = 0$
$x = 2 \pm \sqrt{2}$, $y = 5 \pm 2\sqrt{2}$

⚡ Desmos: Graph both — intersection points are solutions.

**Linear + Circle:**

[Hard] $x + y = 5$, $x^2 + y^2 = 13 \to y = 5 - x \to x^2 + (5-x)^2 = 13 \to x = 2, 3$. Solutions: $(2,3)$, $(3,2)$

**Linear + Absolute Value:**

[Medium] $y = 2x - 1$, $y = |x + 2|$
- Case 1 ($x+2 \geq 0$): $2x-1 = x+2 \to x = 3$ ✅
- Case 2 ($x+2 < 0$): $2x-1 = -(x+2) \to x = -\frac{1}{3}$ — violates condition ❌ **Domain trap**
- Solution: $(3,5)$ only

**Quadratic + Quadratic:**

[Hard] $y = x^2 - 4$, $y = -x^2 + 4 \to 2x^2 = 8 \to x = \pm 2$. Solutions: $(2,0)$, $(-2,0)$

[Very Hard] $y = x^2 - 2x$, $y = -x^2 + 6x - 8 \to 2x^2 - 8x + 8 = 0 \to (x-2)^2 = 0 \to x = 2$ (tangent). Solution: $(2,0)$

**System Solutions by Discriminant:**

When $y = mx + d$ is substituted into $y = ax^2 + bx + c$, the resulting $ax^2 + (b-m)x + (c-d) = 0$ has discriminant $D$:
- $D > 0$: 2 intersections
- $D = 0$: 1 (tangent)
- $D < 0$: 0

[Hard] For what $k$ does $y = 2x + k$ intersect $y = x^2 - 3x + 1$ exactly once?
$2x + k = x^2 - 3x + 1 \to x^2 - 5x + (1-k) = 0$. $D = 25 - 4(1-k) = 21 + 4k = 0 \to k = -\frac{21}{4}$

---

### B2.2.8 Piecewise Functions

$f(x) = \begin{cases} x^2, & x < 0 \\ 2x + 1, & x \geq 0 \end{cases}$

**Evaluation:** Determine which branch applies, then substitute.

[Medium] Find $f(-3) + f(2)$.
- $f(-3) = (-3)^2 = 9$ ($x < 0$ branch)
- $f(2) = 2(2) + 1 = 5$ ($x \geq 0$ branch)
- $9 + 5 = 14$

❌ **Branch trap:** Always check the domain condition. Using the wrong branch is the #1 piecewise error.

**Continuity at Boundary:**

[Hard] $g(x) = \begin{cases} 3x - 2, & x \leq 1 \\ x^2 + a, & x > 1 \end{cases}$. If $g$ is continuous at $x = 1$, find $a$.
- Left: $g(1) = 3(1)-2 = 1$. Right: $\lim_{x\to 1^+} g(x) = 1 + a$
- $1 = 1 + a \to a = 0$

**Real-World Application:**

[Hard] A parking garage charges \$5 for the first hour and \$3 per additional hour.
$C(t) = \begin{cases} 5, & 0 < t \leq 1 \\ 5 + 3(t-1), & t > 1 \end{cases}$
Cost for 4 hours: $C(4) = 5 + 3(3) = \$14$.

**Piecewise graph reading — evaluate from graph:**

[Medium] A piecewise function is defined as:
$f(x) = \begin{cases} 2x + 1, & x \leq 0 \\ x^2, & 0 < x < 3 \\ 9, & x \geq 3 \end{cases}$
Find $f(-2) + f(2) + f(4)$.

$f(-2) = 2(-2) + 1 = -3$ (first branch)  
$f(2) = 2^2 = 4$ (second branch)  
$f(4) = 9$ (third branch)  
Sum: $-3 + 4 + 9 = 10$

❌ **Boundary trap:** At $x = 0$, only the first branch ($\leq$) applies. At $x = 3$, only the third branch ($\geq$) applies.

[Hard] For the piecewise function $f$, what is the domain? What values produce a jump discontinuity?

$f(x) = \begin{cases} x + 2, & x < 1 \\ 4, & x = 1 \\ 3x - 1, & x > 1 \end{cases}$

Left limit at $1$: $1 + 2 = 3$. Right limit: $3(1) - 1 = 2$. Value at $1$: $4$. Jump from $3$ to $4$ to $2$. Discontinuity at $x = 1$.

---

## B2.3 — Nonlinear Functions

### B2.3.1 Domain and Range

**Restriction sources:**

| Cause | Condition |
|---|---|
| Square root (even-index radical) | Radicand $\geq 0$ |
| Denominator | $\neq 0$ |
| Real-world context | Usually $x \geq 0$ or within bounds |

[Medium] Domain of $f(x) = \frac{\sqrt{x-5}}{x-8}$: $x \geq 5$ and $x \neq 8 \to [5,8) \cup (8,\infty)$

[Hard] Range of $f(x) = 3 + \sqrt{2x - 4}$: $\sqrt{2x-4} \geq 0 \to f(x) \geq 3 \to [3,\infty)$

[Hard] Range of $f(x) = -2|x-3| + 5$: $|x-3| \geq 0 \to -2|x-3| \leq 0 \to f(x) \leq 5 \to (-\infty, 5]$

❌ **Domain vs. range trap:** Domain = x-values, range = y-values.

---

### B2.3.2 Maximum and Minimum

$x_v = -\frac{b}{2a}$, $y_v = f(x_v)$. $a > 0$: minimum. $a < 0$: maximum.

[Medium] $f(x) = -2x^2 + 12x - 7$: $x_v = -\frac{12}{-4} = 3$, $y_v = -18 + 36 - 7 = 11$. Maximum of $11$ at $x = 3$.

⚡ Desmos: Graph, click the vertex for exact coordinates.

---

### B2.3.3 Increasing / Decreasing Intervals

For quadratics:
- $a > 0$: decreasing on $(-\infty, h)$, increasing on $(h, \infty)$
- $a < 0$: increasing on $(-\infty, h)$, decreasing on $(h, \infty)$

❌ **Interval notation trap:** Parentheses for non-inclusive, brackets for inclusive.

---

### B2.3.4 End Behavior

**Polynomials:** Leading term $ax^n$ determines both ends. $f(x) = -3x^4 + 2x^3 - 5$: both ends $\to -\infty$.

**Rational functions:** $f(x) = \frac{3x^2 - 5}{2x^2 + x - 1} \to$ HA: $y = \frac{3}{2}$ (equal degrees).

---

### B2.3.5 Graph Features

**Intercepts:** $x$-intercept: set $y = 0$. $y$-intercept: $f(0)$.

**Vertical Asymptotes:** Denominator $= 0$, numerator $\neq 0$ at that $x$.

[Medium] $f(x) = \frac{2x+1}{(x-3)(x+2)}$: VA at $x = 3$ and $x = -2$.

**Holes vs. Vertical Asymptotes — critical distinction:**

| Feature | Condition | Graph |
|---|---|---|
| Hole | Factor cancels entirely | Missing point (open circle) |
| VA | Denominator $= 0$, numerator $\neq 0$ at that $x$ | Vertical line, unbounded |

[Hard] $f(x) = \frac{(x-2)(x+3)}{(x-2)(x+5)}$: $x = 2$ is a hole (cancels), $x = -5$ is a VA (does not cancel).

❌ **Hole vs. VA trap:** If $(x-2)$ cancels, there is NO asymptote at $x=2$ — only a hole.

[Hard] A rational function has VA at $x = -1$ and a hole at $x = 2$. Which could be $f(x)$?

A) $f(x) = \frac{x-2}{(x+1)(x-2)}$  
B) $f(x) = \frac{x+1}{(x+1)(x-2)}$  
C) $f(x) = \frac{(x+1)(x-2)}{x-2}$  
D) $f(x) = \frac{(x+1)(x-2)}{x+1}$

Check each: A) numerator $x-2$, denom $(x+1)(x-2)$ → hole at 2, VA at -1 ✅. Answer: **A**.

❌ **Choice B trap:** Hole at $x=-1$, VA at $x=2$ — reversed.

**More graph questions — given graph, identify features:**

[Hard] The graph of a rational function $f$ has a hole at $x = -2$, VA at $x = 3$, and HA at $y = 0$. Which function could represent $f$?

A) $f(x) = \frac{x+2}{(x-3)(x+2)}$  
B) $f(x) = \frac{x-3}{(x+2)(x-3)}$  
C) $f(x) = \frac{x+2}{x-3}$  
D) $f(x) = \frac{x+2}{(x+2)^2(x-3)}$

A: hole at -2, VA at 3 ✅, deg num < deg den → HA: $y=0$ ✅. Answer: **A**.

❌ **Choice C trap:** No hole (factor doesn't cancel), just VA at 3.

**Symmetry:** Even $(f(-x) = f(x))$, odd $(f(-x) = -f(x))$.

---

### B2.3.6 Transformations

[Medium] $f(x) = x^2$, $g(x) = (x-4)^2 + 3$ is $f$ shifted right 4 and up 3.

[Hard] $f(x) = \sqrt{x}$ shifted right 2, down 5, reflected over $x$-axis: $g(x) = -\sqrt{x-2} - 5$

❌ **Horizontal shift trap:** $f(x+3)$ shifts LEFT (opposite of intuition).

[Very Hard] $f(x) = x^2 - 4x + 5$. Shift right 3, down 2: new vertex?
- Vertex of $f$: $(2,1)$. Shift right 3 $\to (5,1)$, down 2 $\to (5,-1)$.

⚡ Vertex/key points transform the same way as the function.

**Multiple transformations in sequence — order matters:**

[Hard] $f(x) = x^2$. Apply: reflect over $x$-axis, then shift right 2, then shift up 3. What is $g(x)$?

Reflect: $-x^2$. Shift right 2: $-(x-2)^2$. Shift up 3: $g(x) = -(x-2)^2 + 3$.

❌ **Order trap:** If you shift before reflecting, $g(x) = -(x-2)^2 + 3$ changes sign of the shift. With reflection first: $g(x) = -(x-2)^2 + 3$. With shift first then reflect: $g(x) = -(x^2 - 3)$ — different!

[Hard] $f(x) = \sqrt{x}$. Apply: stretch vertically by 2, reflect over $y$-axis, shift down 1.

Stretch: $2\sqrt{x}$. Reflect $y$: $2\sqrt{-x}$. Shift down: $g(x) = 2\sqrt{-x} - 1$.

**Reverse transformations — given $g(x)$, describe from $f(x)$:**

[Hard] $g(x) = -2(x+1)^3 + 5$ is a transformation of $f(x) = x^3$. Describe.

Factor: $g(x) = -2 \cdot f(x+1) + 5$. Steps: (1) Shift left 1, (2) vertical stretch by 2, (3) reflect over $x$-axis, (4) shift up 5.

❌ **Order ambiguity trap:** If the description says "shift left, stretch, reflect, shift up," that's one order. But $g(x) = -2(x+1)^3 + 5$ could be interpreted as shift left 1, then stretch 2, then reflect, then up 5. The order of stretch and reflect can commute since both are vertical.

[Very Hard] $g(x) = 3\left(\frac{x-4}{2}\right)^2 - 1$ is a transformation of $f(x) = x^2$. Describe.

$3\left(\frac{x-4}{2}\right)^2 - 1 = 3 \cdot f\left(\frac{x-4}{2}\right) - 1$. Steps: (1) Shift right 4, (2) horizontal stretch by 2 (divide $x$ by 2), (3) vertical stretch by 3, (4) shift down 1.

---

### B2.3.7 Polynomial Specifics

**Factor Theorem:** $f(a) = 0 \iff (x-a)$ is a factor.
**Remainder Theorem:** $f(a)$ = remainder of $f(x) \div (x-a)$.

[Medium] Remainder of $x^3 - 5x^2 + 7 \div (x+2)$: $f(-2) = -8 - 20 + 7 = -21$.

[Hard] $f(x) = 2x^3 + kx^2 - 3x + 4$. If $x-1$ is a factor, $f(1) = 2 + k - 3 + 4 = k + 3 = 0 \to k = -3$.

[Very Hard] $f(x) = x^3 - 6x^2 + 11x - 6$, given $x=1$ is a root. Factor completely.
Synthetic division:
```
1 | 1  -6   11  -6
  |      1   -5   6
  ----------------
    1  -5    6   0
```
$f(x) = (x-1)(x^2 - 5x + 6) = (x-1)(x-2)(x-3)$

**Zero Multiplicity:** Odd $\to$ cross, even $\to$ bounce.

[Hard] $f(x) = -(x+1)^2(x-3)(x-5)^3$
- $x = -1$: mult 2 (even) $\to$ bounce
- $x = 3$: mult 1 (odd) $\to$ cross
- $x = 5$: mult 3 (odd) $\to$ s-curve cross
- Leading term: $-x^5$ $\to$ up left, down right

**Graph interpretation — which polynomial could produce this graph?**

[Hard] A polynomial graph touches the $x$-axis at $x = -2$, crosses at $x = 1$, and has end behavior: up on left, down on right. Which could be $f(x)$?

A) $f(x) = -(x+2)^2(x-1)$  
B) $f(x) = (x+2)^2(x-1)$  
C) $f(x) = -(x+2)(x-1)^2$  
D) $f(x) = (x+2)(x-1)$  

Touch at $-2$ → even multiplicity → $(x+2)^2$ ✅. Cross at $1$ → odd → $(x-1)$ ✅. Ends up left/down right → leading coefficient negative → $-(x)^3$ behavior. Answer: **A**.

❌ **Choice B trap:** Up on right (positive leading coefficient), not down.  
❌ **Choice C trap:** Cross at -2 (odd), touch at 1 (even) — reversed.

**Least possible degree from a graph:**

[Hard] A polynomial graph crosses at $x = -1$, touches at $x = 2$, and crosses at $x = 5$. Both ends go up. What is the minimum degree?

Cross at $-1$: at least degree 1. Touch at $2$: at least degree 2. Cross at $5$: at least degree 1. Total: $1 + 2 + 1 = 4$, and ends both up means degree even with positive leading coefficient. Minimum degree: 4.

❌ **Degree trap:** Students count roots instead of multiplicities. Three roots ≠ degree 3. Touch = even multiplicity ≥ 2.

[Hard] A polynomial graph crosses at $x = 0$, bounces at $x = 3$, and has one end up, one end down. Minimum degree?

Cross at 0: mult 1 (odd). Bounce at 3: mult 2 (even). Ends opposite → odd degree. Minimum: $1 + 2 = 3$ (degree 3, odd, works: up right, down left if $a>0$).

**Remainder / Factor theorem without full division:**

[Medium] If $f(x) = x^3 - 5x^2 + kx + 8$ has remainder 10 when divided by $x - 2$, find $k$.

$f(2) = 8 - 20 + 2k + 8 = 2k - 4 = 10 \to k = 7$.

[Hard] If $x + 3$ is a factor of $x^3 + kx^2 - 13x + 6$, find $k$.

$f(-3) = -27 + 9k + 39 + 6 = 9k + 18 = 0 \to k = -2$.

❌ **Factor sign trap:** $x + 3$ means $a = -3$, not $3$.

---

### B2.3.8 Exponential Interpretation

**General form:** $f(x) = a \cdot b^x$, $a = f(0)$.

| $b$ | Behavior | Meaning |
|---|---|---|
| $b > 1$ | Growth | $b = 1 + r$, $r$ = growth rate |
| $0 < b < 1$ | Decay | $b = 1 - r$, $r$ = decay rate |

[Easy] $f(t) = 500(1.08)^t$: initial $= 500$, growth rate $= 8\%$.
[Medium] $g(t) = 1200(0.93)^t$: initial $= 1200$, decay rate $= 7\%$.

❌ **Percent trap:** $1.08$ is an 8% increase (NOT 108%). $0.92$ is an 8% decrease (NOT 92%).

**Percent wording traps — SAT is precise about wording:**

| Phrase | Multiplier |
|---|---|
| "increases by 5%" | $1.05$ |
| "increases by 5 percentage points" | $+0.05$ (additive, not multiplicative) |
| "is 150% of" | $1.5$ |
| "becomes 150% of original" | $1.5$ |
| "decreases by 12%" | $0.88$ |
| "retains 88% of its value" | $0.88$ |
| "depreciates by 15% annually" | $0.85$ |
| "remaining" / "left after" | Usually $\times$ fraction |
| "of the original" | Direct proportion |

[Medium] A car worth \$25,000 depreciates by 12% each year. Which function models its value after $t$ years?

A) $V(t) = 25000(0.12)^t$  
B) $V(t) = 25000(0.88)^t$  
C) $V(t) = 25000(1.12)^t$  
D) $V(t) = 25000 - 3000t$

Depreciates 12% → retains 88% → multiplier $0.88$. Answer: **B**.

❌ **Choice A trap:** Uses 12% as the multiplier instead of the retention rate.  
❌ **Choice D trap:** Treats exponential depreciation as linear.

[Hard] An investment grows at 6% annual rate compounded annually. If \$2000 is invested, which function models the value after $t$ years?

A) $V(t) = 2000(1.06)^t$  
B) $V(t) = 2000(0.06)^t$  
C) $V(t) = 2000(6)^t$  
D) $V(t) = 2000 + 120t$

Growth: $1 + 0.06 = 1.06$, so $V(t) = 2000(1.06)^t$. Answer: **A**.

[Hard] A bacteria population triples every 4 hours. If the initial population is 100, which function models the population after $t$ hours?

A) $P(t) = 100(3)^{t}$  
B) $P(t) = 100(3)^{t/4}$  
C) $P(t) = 100(4)^{t/3}$  
D) $P(t) = 100(1.75)^{t}$

Triples every 4 hours: $P(t) = 100 \cdot 3^{t/4}$. Answer: **B**.

❌ **Choice A trap:** Ignores the time scaling — triples every 4 hours, not every hour.

[Hard] The half-life of a radioactive substance is 30 days. Which function models the mass $M(t)$ of a 50-gram sample after $t$ days?

A) $M(t) = 50(0.5)^{t/30}$  
B) $M(t) = 50(0.5)^{30t}$  
C) $M(t) = 50(2)^{t/30}$  
D) $M(t) = 50 - \frac{t}{30} \cdot 25$

Half-life formula: $M(t) = a(1/2)^{t/h} = 50(0.5)^{t/30}$. Answer: **A**.

[Very Hard] The value of a \$40,000 machine depreciates by 20% each year. After 3 years, management sells it for 60% of its then-current value. How much do they receive?

Year 1: $40000(0.8) = 32000$  
Year 2: $32000(0.8) = 25600$  
Year 3: $25600(0.8) = 20480$  
Sale: $20480(0.6) = 12288$  
Answer: \$12,288.

❌ **Linear depreciation trap:** Students subtract $0.2 \times 40000 = 8000$ per year, getting $40000 - 24000 = 16000$, then $16000 \times 0.6 = 9600$. Wrong.

**Doubling / Half-Life:**

| Type | Formula | Meaning |
|---|---|---|
| Doubling | $f(x) = a \cdot 2^{x/d}$ | Doubles every $d$ units |
| Half-life | $f(x) = a \cdot (1/2)^{x/h}$ | Halves every $h$ units |

[Medium] Bacteria doubles every 3 hours, initial $200$: $P(t) = 200 \cdot 2^{t/3}$.

[Hard] Half-life 50 years, initial $80$ g: $M(t) = 80 \cdot (1/2)^{t/50}$. After 200 years: $80 \cdot (1/2)^4 = 5$ g.

[Very Hard] After 10 years, population is 500. After 20 years, 2000. Find doubling time.
- Ratio $\frac{2000}{500} = 4 = 2^2$: two doublings in 10 years $\to d = 5$ years.
- Algebra: $500 = a \cdot 2^{10/d}$, $2000 = a \cdot 2^{20/d}$. Divide: $4 = 2^{10/d} \to d = 5$.

[Medium] A city population of 50,000 grows at 2% per year. Which function models the population after $t$ years?

A) $P(t) = 50000(1.02)^t$  
B) $P(t) = 50000(0.98)^t$  
C) $P(t) = 50000(2)^t$  
D) $P(t) = 50000 + 1000t$

Growth at 2% → $1.02$. Answer: **A**.

[Hard] A new social media site has 1000 users and grows by 40% each month. Which function models the number of users after $m$ months?

A) $U(m) = 1000(1.4)^m$  
B) $U(m) = 1000(0.4)^m$  
C) $U(m) = 1000(40)^m$  
D) $U(m) = 1000 + 400m$

40% growth → multiplier $1.4$. Answer: **A**.

**Exponential decision flow:**

Can you match bases? → Yes → Equate exponents directly  
Can you use $u$-substitution? → Yes → Quadratic in $b^x$  
Neither? → Graph both sides in Desmos, find intersection

---

### B2.3.9 Rational Function Transformations

$f(x) = \frac{a}{x-h} + k$: VA at $x = h$, HA at $y = k$.

[Medium] $f(x) = \frac{3}{x-2} + 1$: VA $x = 2$, HA $y = 1$. Domain: $x \neq 2$, Range: $y \neq 1$.

[Hard] $f(x) = \frac{2x+1}{x-3} = 2 + \frac{7}{x-3}$: VA $x = 3$, HA $y = 2$.

---

### B2.3.10 Inverse Functions

**Property:** $f^{-1}(f(x)) = x$, $f(f^{-1}(x)) = x$. Graph: reflection across $y = x$. Domain/range swap.

**Finding inverse:** Replace $f(x)$ with $y$, swap $x$ and $y$, solve for $y$, replace $y$ with $f^{-1}(x)$.

[Medium] $f(x) = 2x + 5 \to y = 2x + 5 \to x = 2y + 5 \to f^{-1}(x) = \frac{x-5}{2}$

[Hard] $f(x) = \frac{3x-1}{x+2} \to x = \frac{3y-1}{y+2} \to x(y+2) = 3y - 1 \to xy + 2x = 3y - 1$ $\to xy - 3y = -2x - 1 \to y(x-3) = -(2x+1) \to f^{-1}(x) = -\frac{2x+1}{x-3}$

**SAT-style inverse evaluation:**

[Medium] If $f(x) = 2x - 7$, what is $f^{-1}(3)$?

Find $x$ such that $f(x) = 3$: $2x - 7 = 3 \to x = 5$. So $f^{-1}(3) = 5$.

❌ **Swap-and-solve trap:** Students swap $x$ and $y$ then solve, getting $f^{-1}(x) = \frac{x+7}{2}$, then plug $3 \to 5$. But solving $f(x)=3$ is faster.

[Hard] For $f(x) = \sqrt{x - 2} + 3$, $x \geq 2$, find $f^{-1}(x)$ and its domain.

Swap: $x = \sqrt{y - 2} + 3 \to \sqrt{y-2} = x-3 \to y - 2 = (x-3)^2 \to f^{-1}(x) = (x-3)^2 + 2$.  
Domain of $f^{-1}$ = range of $f = [3, \infty)$ (since $\sqrt{x-2} \geq 0 \to f(x) \geq 3$).

❌ **Domain swap trap:** Students forget domain/range swap. $f^{-1}$ domain is $f$'s range.

**Interpreting inverse in context:**

[Hard] The function $C(t) = 500(1.04)^t$ models the value of an investment after $t$ years. What does $C^{-1}(800)$ represent?

A) The value after 800 years  
B) The time it takes for the investment to reach $800  
C) The initial investment  
D) The annual interest rate  

$C^{-1}(800)$ asks: "How many years until the investment is worth \$800?" Answer: **B**.

❌ **Choice A trap:** Students invert input/output, thinking $C^{-1}(800)$ means "value at $t=800$."

[Hard] If $f(x) = \frac{2x}{x-1}$ for $x \neq 1$, what is $f^{-1}(4)$?

$f^{-1}(4)$: find $x$ s.t. $f(x) = 4$. $\frac{2x}{x-1} = 4 \to 2x = 4x - 4 \to -2x = -4 \to x = 2$.

---

### B2.3.11 Composition of Functions

$(f \circ g)(x) = f(g(x))$.

**Numeric composition:**

[Medium] $f(x) = x^2 + 1$, $g(x) = 3x - 2$. $f(g(4)) = f(10) = 101$.

[Medium] $f(x) = \sqrt{x}$, $g(x) = x + 5$. Evaluate $f(g(11))$: $g(11) = 16$, $f(16) = 4$.

**Symbolic composition:**

[Hard] $f(x) = x^2 + 1$, $g(x) = \sqrt{x - 1}$. Find $f(g(x))$ and $g(f(x))$.

$f(g(x)) = (\sqrt{x-1})^2 + 1 = x - 1 + 1 = x$ (they are inverses!)  
$g(f(x)) = \sqrt{(x^2 + 1) - 1} = \sqrt{x^2} = |x|$

❌ **Absolute value trap:** $g(f(x)) = \sqrt{x^2} = |x|$, not $x$. Without domain restriction, the principal square root returns $|x|$.

**Domain of composition:**

[Hard] $f(x) = \sqrt{x+1}$, $g(x) = x^2 - 4$. Domain of $f(g(x)) = \sqrt{x^2 - 3}$: $x^2 - 3 \geq 0 \to |x| \geq \sqrt{3} \to (-\infty, -\sqrt{3}] \cup [\sqrt{3}, \infty)$.

[Very Hard] $f(x) = \frac{1}{x-2}$, $g(x) = \sqrt{x+1}$. Find domain of $f(g(x))$.

$f(g(x)) = \frac{1}{\sqrt{x+1} - 2}$. Restrictions: (1) $\sqrt{x+1}$ requires $x \geq -1$. (2) Denominator $\neq 0$: $\sqrt{x+1} \neq 2 \to x+1 \neq 4 \to x \neq 3$. Domain: $[-1, 3) \cup (3, \infty)$.

**Composition as "applying one after another":**

[Medium] $f(x) = 2x$, $g(x) = x + 1$. What does $g(f(x))$ represent vs $f(g(x))$?

$g(f(x))$: first double, then add 1 → $2x + 1$.  
$f(g(x))$: first add 1, then double → $2x + 2$. Order matters.

**Value from a table (SAT style):**

[Medium] Given $f(1)=3$, $f(3)=7$, $g(1)=5$, $g(3)=1$, find $f(g(3))$.

$g(3) = 1$, then $f(1) = 3$. Answer: $3$.

---

## Mixed Reasoning: "Which Statement Must Be True?" / "Which Could Be True?"

SAT asks about implications — not "solve" but "what must follow."

**Root/Graph reasoning:**

[Hard] The quadratic $f(x) = x^2 + kx + 9$ has exactly one real solution. Which statement must be true?

A) $k = 6$  
B) $k = -6$  
C) $k = \pm 6$  
D) $k > 6$ or $k < -6$

$D = k^2 - 36 = 0 \to k = \pm 6$. Answer: **C**.

❌ **Choice A trap:** Students solve $k^2 = 36 \to k = 6$, forgetting $k = -6$.

[Hard] The function $f(x) = ax^2 + bx + c$ opens upward and has $x$-intercepts at $-2$ and $5$. Which statement must be true?

A) $a > 0$ and $c < 0$  
B) $a < 0$ and $c > 0$  
C) $a > 0$ and $c > 0$  
D) $a < 0$ and $c < 0$  

Opens up $\to a > 0$. $c = f(0)$. Since intercepts are $-2$ and $5$, the $y$-intercept is negative (parabola crossing at negative $y$ between roots). $c < 0$. Answer: **A**.

❌ **Choice C trap:** Student knows $a > 0$ but guesses $c > 0$ without checking.

[Hard] The system $y = x^2 - 6x + 10$ and $y = 2x + k$ has two real solutions. Which could be a value of $k$?

A) $-7$  
B) $-6$  
C) $-5$  
D) $5$  

$x^2 - 6x + 10 = 2x + k \to x^2 - 8x + (10 - k) = 0$. $D = 64 - 4(10 - k) = 24 + 4k > 0 \to k > -6$. Among choices, $-5$ and $5$ satisfy. Answer: **C** or **D** — SAT with one answer would specify the range differently.

[Very Hard] The polynomial $p(x) = ax^3 + bx^2 + cx + d$ has $x$-intercepts at $x = -2, 1, 4$ and passes through $(0, -8)$. Which statement must be true?

A) $a > 0$  
B) $a < 0$  
C) $a = 2$  
D) $a = -2$  

Factored: $p(x) = a(x+2)(x-1)(x-4)$. Plug $(0,-8)$: $-8 = a(2)(-1)(-4) = a(8) \to a = -1$. So $a < 0$. Answer: **B**.

❌ **Choice D trap:** Student computes $a = -1$ and sees negative, picks D $-2$ without checking.

---

## The 25 Traps of Advanced Math

1. **Middle term in $(a+b)^2$:** $(x+3)^2 = x^2 + 6x + 9$, NOT $x^2 + 9$.
2. **Sum vs. diff of squares:** $x^2 - 49$ factors; $x^2 + 49$ does not over reals.
3. **Extraneous roots:** ALWAYS check radical equation solutions in the ORIGINAL equation.
4. **Denominator restrictions:** $x \neq$ values that zero any denominator — even after canceling.
5. **Absolute value $=$ negative:** $|x| = -5$ has no solution.
6. **$f(x+3)$ shifts LEFT:** Intuition says right, math says left.
7. **Double root parameter:** $k = \pm 6$ when $D = 0$, not just $k = 6$.
8. **Bounce vs. cross:** Even multiplicity = bounce, odd = cross.
9. **Percent vs. multiplier:** $1.08$ is 8% increase (NOT 108%). $0.92$ is 8% decrease.
10. **Squaring without isolating radical:** Creates cross-terms and false solutions.
11. **Piecewise branch selection:** Match input to the CORRECT domain condition.
12. **Completing square with $a \neq 1$:** Factor $a$ first; multiply subtracted term by $a$.
13. **Leading coefficient in end behavior:** $f(x) = -x^2$ goes down on both sides.
14. **Vieta's sign:** $r_1 + r_2 = -\frac{b}{a}$, not $\frac{b}{a}$.
15. **Canceling terms vs. factors:** Only cancel FACTORS. $\frac{x+3}{x}$ cannot simplify.
16. **Negative exponent confusion:** $x^{-n} = \frac{1}{x^n}$, not $-x^n$.
17. **Missing negative in subtraction:** $\frac{A}{B} - \frac{C}{D}$: distribute minus to ALL terms of $C$.
18. **Exponential always positive:** $2^x$ is NEVER negative. Reject $u$-solutions $\leq 0$.
19. **System branch conditions:** $|x+2|$ solutions must satisfy their case's domain condition.
20. **Back-substitution in $u$-substitution:** Each $u$ may yield 0, 1, or 2 $x$'s.
21. **Complex fraction panic:** Multiply numerator and denominator by the LCD of all internal fractions.
22. **Domain after canceling:** If $(x+3)$ cancels, $x \neq -3$ still applies in the original expression.
23. **Piecewise boundary:** At the boundary, only the $\leq$ or $\geq$ branch includes that $x$.
24. **Exponent base mismatch:** If you cannot rewrite to the same base, graph in Desmos.
25. **$(a-b) = -(b-a)$:** $\frac{x-3}{3-x} = -1$, not $1$.

---

## Mixed Reasoning: Function Selection, Models, and Estimation

### Which function could satisfy these conditions?

[Hard] A quadratic function $f$ has $f(0) = 3$ and $f(2) = 7$. Which of the following could be $f(x)$?

A) $f(x) = x^2 + 3$  
B) $f(x) = (x-1)^2 + 3$  
C) $f(x) = -(x-1)^2 + 4$  
D) All of the above  

Check A: $f(0) = 3$ ✅, $f(2) = 7$ ✅. Check B: $f(0) = 4$ ❌. Check C: $f(0)=3$ ✅, $f(2)=3$ ❌. Only A works. Answer: **A**.

[Hard] Which graph could represent $f(x) = -(x-2)^2 + 4$?

Opens down, vertex at $(2,4)$. $x$-intercepts: $-(x-2)^2 + 4 = 0 \to (x-2)^2 = 4 \to x = 0, 4$. Look for: parabola opening down, peak at $(2,4)$, crossing at $0$ and $4$.

### Equivalent: Expressions, Functions, Graphs, Tables

[Hard] The table shows values of a function $f$.

| $x$ | $f(x)$ |
|---|---|
| 0 | 3 |
| 1 | 5 |
| 2 | 9 |
| 3 | 17 |

Which type of function best models the data?

A) Linear  
B) Quadratic  
C) Exponential  
D) Absolute value  

First differences: $2, 4, 8$ (not constant). Second differences: $2, 4$ (not constant). Ratios: $\frac{5}{3} \approx 1.67, \frac{9}{5} = 1.8, \frac{17}{9} \approx 1.89$ (not constant either). Pattern: $3 = 2^1 + 1$, $5 = 2^2 + 1$, $9 = 2^3 + 1$, $17 = 2^4 + 1$ — exponential ($2^{x+1} + 1$). Answer: **C**.

❌ **Linear trap:** First differences look "almost linear" at a glance but double each time.

### Interpret Coefficient Meaning

[Hard] The function $h(t) = -16t^2 + 64t + 10$ models the height (feet) of a projectile $t$ seconds after launch. What does the $10$ represent?

A) The maximum height  
B) The initial height  
C) The time to reach max height  
D) The height after 1 second  

$h(0) = 10$, so it's the initial height. Answer: **B**.

❌ **Choice A trap:** Students think the constant term is always the max.

[Hard] In the quadratic $y = 2(x-3)^2 + 5$, what does the $3$ represent?

A) The $y$-coordinate of the vertex  
B) The $x$-coordinate of the vertex  
C) The $y$-intercept  
D) The axis is $x = -3$

Vertex form $a(x-h)^2 + k$: $h = 3$, so $x$-coordinate of vertex. Answer: **B**.

### Find Missing Parameter

[Hard] The function $f(x) = a(2)^x + 3$ passes through $(2, 19)$. Find $a$.

$19 = a(2)^2 + 3 \to 19 = 4a + 3 \to a = 4$.

[Hard] The quadratic $f(x) = x^2 + bx + c$ has $x$-intercepts at $2$ and $5$. Find $b + c$.

Factored: $f(x) = (x-2)(x-5) = x^2 - 7x + 10$. So $b = -7$, $c = 10$, $b + c = 3$.

❌ **Sign trap:** $b = -(p+q) = -(2+5) = -7$, not $7$.

### Choose Correct Model

[Hard] A balloon rises at 3 feet per second from an initial height of 10 feet. Which model best represents its height after $t$ seconds?

A) $h(t) = 3t + 10$  
B) $h(t) = 10(3)^t$  
C) $h(t) = 3^t + 10$  
D) $h(t) = 3t^2 + 10$

Constant rate (3 ft/s) + initial (10 ft) → linear. Answer: **A**.

❌ **Choice B trap:** Exponential growth model for a constant-rate situation.

### Estimate from Graph

[Hard] The graph of $y = f(x)$ is a parabola opening up with vertex $(-1, -4)$ and passing through $(0, -3)$. Estimate $f(2)$.

Vertex form: $f(x) = a(x+1)^2 - 4$. Plug $(0,-3)$: $-3 = a(1) - 4 \to a = 1$. $f(x) = (x+1)^2 - 4$. $f(2) = 9 - 4 = 5$.

[Hard] From the graph of $y = -x^2 + 4x$, estimate the $x$-intercepts.

$0 = -x(x - 4) \to x = 0, 4$.

### Choose Best Method

[Medium] What is the best first step to solve $3(x-2)^2 = 27$?

A) Expand $(x-2)^2$  
B) Multiply both sides by 3  
C) Divide both sides by 3, then square root  
D) Use quadratic formula  

Divide by 3: $(x-2)^2 = 9$, then $x-2 = \pm 3 \to x = 5, -1$. Answer: **C**.

❌ **Choice A trap:** Expanding creates unnecessary work when square root method is simpler.

[Hard] What is the best first step to solve $\sqrt{2x+3} = x - 5$?

A) Square both sides  
B) Isolate the radical — already done  
C) Move all terms to one side  
D) Check for extraneous solutions  

The radical is already isolated. Next: square both sides. Answer: **B** (first step already done). If they ask "next step," it is **A**.

### Mixed Nonlinear Review — Final Set

[Easy] Solve: $x^2 - 7x + 12 = 0$.  
$(x-3)(x-4) = 0 \to x = 3, 4$.

[Easy] Simplify: $\frac{x^2 - 4}{x-2}$.  
$\frac{(x-2)(x+2)}{x-2} = x+2$, $x \neq 2$.

[Medium] Solve: $2^{x+1} = 16$.  
$2^{x+1} = 2^4 \to x + 1 = 4 \to x = 3$.

[Medium] Which expression is equivalent to $\sqrt{50x^5}$ for $x > 0$?  
$\sqrt{25 \cdot 2 \cdot x^4 \cdot x} = 5x^2\sqrt{2x}$.

[Medium] Solve: $|2x - 3| = 7$.  
$2x - 3 = 7 \to x = 5$, or $2x - 3 = -7 \to x = -2$.

[Medium] If $f(x) = 3x - 2$, find $f^{-1}(7)$.  
$3x - 2 = 7 \to x = 3$.

[Hard] The system $y = x^2 - 4x$ and $y = 2x - 5$ has how many solutions?  
$x^2 - 4x = 2x - 5 \to x^2 - 6x + 5 = 0$. $D = 36 - 20 = 16 > 0$ → 2 solutions.

[Hard] The function $f(x) = 3(x+1)^2 - 8$ has a minimum at what point?  
Vertex form $a(x-h)^2 + k$: $h = -1$, $k = -8$. Minimum at $(-1, -8)$.

[Hard] Which expression is equivalent to $\frac{3}{x-1} + \frac{2}{x+1}$?  
$\frac{3(x+1) + 2(x-1)}{(x-1)(x+1)} = \frac{5x+1}{x^2-1}$.

[Hard] A population of 200 grows at 5% per year. Which function models the population after $t$ years?  
$P(t) = 200(1.05)^t$.

[Hard] The graph of a polynomial touches at $x = -2$ and crosses at $x = 4$. Minimum degree?  
Touch → even mult (at least 2). Cross → odd mult (at least 1). Minimum degree: $2+1 = 3$.

[Very Hard] Solve: $x^4 - 10x^2 + 9 = 0$.  
Let $u = x^2$: $u^2 - 10u + 9 = 0 \to u = 1, 9$. $x = \pm 1, \pm 3$.

[Very Hard] The function $f(x) = a(b)^x$ passes through $(0, 5)$ and $(2, 45)$. Find $a$ and $b$.  
$f(0) = a = 5$. $f(2) = 5b^2 = 45 \to b^2 = 9 \to b = 3$ ($b > 0$ for exponential).

[Very Hard] $f(x) = \sqrt{x+5} - 3$. Find $f^{-1}(x)$.  
Swap: $x = \sqrt{y+5} - 3 \to \sqrt{y+5} = x + 3 \to y + 5 = (x+3)^2 \to f^{-1}(x) = (x+3)^2 - 5$, domain $x \geq -3$.

---

## Desmos Strategy Quick Reference

### Exact vs. Approximate — Know the Difference

| Need | Desmos Role | Backup |
|---|---|---|
| Exact answer (integer, simple fraction) | Confirm, but solve algebraically | Algebra first |
| Exact radical form ($\sqrt{73}$, $\frac{5\pm\sqrt{13}}{6}$) | **Cannot** give exact radicals — use quadratic formula | Solve on paper |
| Decimal answer (3.14, 0.0625) | Read directly from graph | Round as needed |
| "Which expression is equivalent?" | Graph all choices; correct one overlaps | Test numeric value |
| Parameter (find $k$ for tangency) | Use slider, adjust until tangent | Set $D = 0$ |

### Quick Reference Table

| Situation | Desmos Move |
|---|---|
| Find roots | Graph $y = f(x)$, click $x$-intercepts |
| Vertex / min / max | Graph, click turning point |
| Solve system (linear + nonlinear) | Graph both, click intersection(s) |
| Check equivalent expressions | Graph original + each choice; should overlap perfectly |
| Parameter for tangency | Graph with slider, adjust until curves just touch |
| Fit exponential | Table $\to y_1 \sim a \cdot b^{x_1}$ |
| Quadratic regression | Table $\to y_1 \sim ax_1^2 + bx_1 + c$ |
| Verify transformation | Graph $f$ and transformed $g$ side by side |
| Extraneous root check | Graph original equation, see which roots survive |
| Factoring verification | Graph, check $x$-intercepts match factors |
| Domain / range | Graph, observe $x$ and $y$ extents |

### Sliders for Parameter Exploration

Add `k` as a slider (e.g., $y = x^2 + kx + 9$), then drag to see:
- **Discriminant:** $k$ controls $D = k^2 - 36$. Watch when the parabola touches the $x$-axis.
- **Tangent conditions:** $y = kx + 2$ with $y = x^2 + x + 1$ — adjust $k$ until exactly one intersection.
- **Transformations:** $y = a(x-h)^2 + k$ — see how $a$, $h$, $k$ affect shape.

### Table Tools

Enter data as a table (type `(x1, y1)` into expression list):
- **Estimate growth factor:** For exponential data, fit $y_1 \sim a \cdot b^{x_1}$ — read $b$ directly.
- **Estimate quadratic:** Fit $y_1 \sim ax_1^2 + bx_1 + c$ — read $a$, $b$, $c$.

### Graph Window Warnings

- **"No intersection" may be a zoom issue:** If Desmos shows no intersection but algebra suggests there should be one, zoom out or adjust the window.
- **Oscillating/high-degree polynomials:** May hide features in default window. Try $x \in [-10, 10]$, then narrow.
- **Rational function with VA:** Desmos may draw a spurious vertical line at the VA — that's NOT part of the graph.
- **Check precision:** Desmos rounds to ~3 decimal places by default. For exact answers, zoom in or use algebra.

### When NOT to use Desmos

Simple factoring (difference of squares), Vieta's formulas, single-variable algebra taking <15 seconds, conceptual questions about coefficient meaning, problems needing exact radical form.
