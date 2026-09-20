# Digital SAT Advanced Math | Domain B2

**Prerequisite:** Algebra I + II | **Key Skill:** Nonlinear relationships - quadratics, exponentials, polynomials, radicals, rationals, and systems

**Domain cross-references:** B1 (Algebra) for linear prerequisite skills | B3 (Data Analysis) for exponential models in context | B4 (Geometry and Trig) for circle equations, triangle problems using quadratics

### Official Blueprint Mapping

| Skill Domain | Blueprint Code | B2 Section(s) |
|---|---|---|
| Equivalent expressions | 2.2.A | B2.1 |
| Nonlinear equations in one variable | 2.2.B | B2.2.1-B2.2.6 |
| Systems of equations (nonlinear) | 2.2.C | B2.2.7 |
| Nonlinear functions | 2.2.D | B2.3 |

---

**Most Common Question Types on the Actual Exam - study these first:**

| # | Question Type | Covered In |
|---|---|---|
| 1 | **Equivalent expressions** - "Which of the following is equivalent to ...?" (expand, factor, rational simplify, exponent chains, radical rationalization) | B2.1 |
| 2 | **Quadratic vertex / min-max from context or graph** - "What is the minimum value of the given function?" | B2.1.8, B2.3.2 |
| 3 | **Exponential growth/decay word problems** - bacteria, investments, depreciation, half-life, doubling time; interpret the multiplier | B2.3.8 |
| 4 | **Extraneous solutions** - radical and rational equations; "how many solutions does the equation have?" | B2.2.3, B2.2.4 |
| 5 | **Nonlinear systems** - linear + quadratic, linear + circle (see B4.5), linear + absolute value; "how many solutions?" | B2.2.7, B4.5 |
| 6 | **Solving for a variable buried in a formula** - rearrange a nonlinear formula for one letter | B2.2.9 |

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
| Even root of a power | $\sqrt{x^2} = |x|$ (the SAT usually assumes $x \geq 0$ when simplifying) |

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

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \quad \text{where } ax^2 + bx + c = 0$$

$D = b^2 - 4ac$:
- $D > 0$: 2 distinct real solutions
- $D = 0$: 1 real solution (double root)
- $D < 0$: 0 real solutions (complex)

### Vertex Forms

**Standard to vertex:** $f(x) = ax^2 + bx + c \to f(x) = a(x-h)^2 + k$

$$h = -\frac{b}{2a}, \quad k = f(h)$$

**Completing the square:** $x^2 + bx = \left(x + \frac{b}{2}\right)^2 - \left(\frac{b}{2}\right)^2$

### Quadratic Forms

| Form | Expression | Reveals |
|---|---|---|
| Standard | $ax^2 + bx + c$ | $y$-intercept $(0,c)$, end behavior from $a$ |
| Vertex | $a(x-h)^2 + k$ | Vertex $(h,k)$, axis $x=h$, min/max $k$ |
| Factored | $a(x-r_1)(x-r_2)$ | Roots $r_1, r_2$, axis of symmetry $x = \frac{r_1+r_2}{2}$ |

### End Behavior (Polynomials)

Leading term $ax^n$ determines both ends:
- $n$ even, $a > 0$: both $\to +\infty$
- $n$ even, $a < 0$: both $\to -\infty$
- $n$ odd, $a > 0$: left $-\infty$, right $+\infty$
- $n$ odd, $a < 0$: left $+\infty$, right $-\infty$

### End Behavior (Exponentials)

For $f(x) = a \cdot b^x$ with $a > 0$:
- $b > 1$: as $x \to \infty$, $f \to \infty$; as $x \to -\infty$, $f \to 0$ (approaches the horizontal asymptote $y = 0$ from above)
- $0 < b < 1$: as $x \to \infty$, $f \to 0$; as $x \to -\infty$, $f \to \infty$
- For $f(x) = a \cdot b^x + k$: the horizontal asymptote is $y = k$

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
- **Compound interest:** $A = P\left(1 + \frac{r}{n}\right)^{nt}$ - $P$ = principal, $r$ = annual rate as a decimal, $n$ = compounding periods per year, $t$ = years
- **Exponential through two points:** plug both points into $f(x) = a \cdot b^x$, then divide one equation by the other to eliminate $a$ and solve for $b$
- **Scaled-time interpretation:** $f(t) = a(1.08)^{t/2}$ means 8% growth every 2 units of time, NOT per unit. The per-unit factor is $(1.08)^{1/2} \approx 1.0392$ (about 3.92% per unit). If asked "what percent increase over $n$ units," compute $(b)^{n/\text{period}} - 1$.
- **Horizontal asymptote:** $f(x) = a \cdot b^x + k$ has HA $y = k$
- **Range:** for $a > 0$, range of $f(x) = a \cdot b^x + k$ is $(k, \infty)$; for $a < 0$, it is $(-\infty, k)$

### Absolute Value

- **Piecewise definition:** $|x| = \begin{cases} x, & x \geq 0 \\ -x, & x < 0 \end{cases}$
- **Equation:** $|A| = B$ (with $B \geq 0$) $\iff A = B$ or $A = -B$
- **Graph:** $f(x) = a|x - h| + k$ is a V-shape with vertex $(h,k)$, opening up if $a > 0$, down if $a < 0$
- **Solution count:** $|x - h| = k$ has 2 solutions if $k > 0$, 1 solution if $k = 0$, 0 solutions if $k < 0$

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

### Interval Notation (quick review)

| Notation | Means | Includes endpoints? |
|---|---|---|
| $(a, b)$ | $a < x < b$ | No |
| $[a, b]$ | $a \leq x \leq b$ | Yes |
| $[a, b)$ | $a \leq x < b$ | Only $a$ |
| $(a, \infty)$ | $x > a$ | No |
| $(-\infty, b]$ | $x \leq b$ | Only $b$ |

---

## B2.1 - Equivalent Expressions

**What this whole section is about:** two expressions are *equivalent* when they give the SAME value for every allowable input. The SAT writes "Which of the following is equivalent to ...?" and the answer choices are different-looking but mathematically identical versions. Your job: transform one into another using factoring, expanding, combining fractions, rewriting radicals as exponents, completing the square, or polynomial division - and recognize the same expression in a new disguise.

**Golden rules:**
1. Whatever you do, do it to the WHOLE expression legally (factor, distribute, combine) - never "cancel" terms that are not factors.
2. Track restrictions: if you cancel $(x+3)$, the original expression still requires $x \neq -3$.
3. When stuck on a multiple-choice equivalent-expression question, plug in one number and eliminate.

### B2.1.1 Operations with Polynomials

**Definition:** a polynomial is a sum of terms like $ax^n$ where $n$ is a whole number ($0, 1, 2, \dots$). Adding, subtracting, and multiplying polynomials produces another polynomial.

**Step-by-step method (add/subtract):**
1. Remove parentheses. For subtraction, distribute the minus sign to EVERY term inside.
2. Identify like terms (same variable, same exponent).
3. Combine the coefficients of like terms.

**Step-by-step method (multiply):**
1. Distribute each term of the first polynomial to every term of the second.
2. Combine like terms.

[Easy] $(3x^2 - 5x + 2) + (x^2 + 7x - 4) = 4x^2 + 2x - 2$

[Medium] $(4x^3 - 2x^2 + 3) - (x^3 + 5x^2 - 7) = 4x^3 - 2x^2 + 3 - x^3 - 5x^2 + 7 = 3x^3 - 7x^2 + 10$

❌ **Sign error trap:** $-(x^3 + 5x^2 - 7) = -x^3 - 5x^2 + 7$, not $-x^3 + 5x^2 - 7$.

[Hard] Which expression is equivalent to $(2x - 1)(x^2 + 3x - 4)$?
$$(2x - 1)(x^2 + 3x - 4) = 2x^3 + 6x^2 - 8x - x^2 - 3x + 4 = 2x^3 + 5x^2 - 11x + 4$$

❌ **Distribution trap:** forgetting to distribute the $-1$ to ALL THREE terms of the second polynomial. The $-3x$ term is the one students drop most.

⚡ Desmos: graph the original product and your answer; identical curves = equivalent expressions.

**Special products to recognize instantly (expanding direction - the reverse of factoring in B2.1.2):**

| Identity | Expanded |
|---|---|
| $(a+b)^2$ | $a^2 + 2ab + b^2$ |
| $(a-b)^2$ | $a^2 - 2ab + b^2$ |
| $(a+b)(a-b)$ | $a^2 - b^2$ |

[Medium] $(2x - 5y)^2 = 4x^2 - 20xy + 25y^2$
❌ **Middle-term trap:** $(2x-5y)^2 \neq 4x^2 + 25y^2$. The $-20xy$ is essential.

---

### B2.1.2 Factoring

**Definition:** factoring is the reverse of expanding - writing an expression as a PRODUCT of simpler expressions. It is the single most-used skill in Advanced Math because it appears in equivalent expressions, solving equations, simplifying rationals, and finding roots.

**Step-by-step method (general factoring strategy):**
1. **GCF first:** factor out the greatest common factor of all terms (including the sign if the leading term is negative).
2. **Count the terms:**
   - 2 terms: try difference of squares $a^2 - b^2$, then sum/difference of cubes.
   - 3 terms: check perfect-square pattern; if not, use the trinomial method.
   - 4 terms: try grouping in pairs.
3. **Check each factor** - can it be factored further? (e.g. $x^4 - 16$ factors twice.)
4. **Verify:** expand your answer - you must get the original back.

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

[Medium] Difference of squares, factored twice: $x^4 - 16 = (x^2 - 4)(x^2 + 4) = (x - 2)(x + 2)(x^2 + 4)$

❌ **Partial factoring trap:** stopping at $(x^2 - 4)(x^2 + 4)$ when $x^2 - 4$ factors further. ❌ **Sum-of-squares trap:** $x^2 + 49$ is NOT factorable over reals.

[Medium] Perfect square: $4x^2 - 12x + 9 = (2x - 3)^2$
⚡ Quick test: first and last terms must be perfect squares; middle term must equal $\pm 2\sqrt{\text{first}}\sqrt{\text{last}}$.

[Medium] Simple trinomial: $x^2 - 7x + 12 = (x-3)(x-4)$ - find $p+q=-7$, $pq=12$.

[Hard] Hard trinomial ($a \neq 1$): $6x^2 + 13x - 5$
1. $a \cdot c = 6(-5) = -30$.
2. Factors of $-30$ that sum to $13$: $15$ and $-2$.
3. Rewrite: $6x^2 + 15x - 2x - 5$
4. Group: $3x(2x+5) - 1(2x+5) = (3x-1)(2x+5)$
⚡ Desmos: graph $y = 6x^2 + 13x - 5$; $x$-intercepts at $\frac{1}{3}$ and $-\frac{5}{2}$ confirm the factors.

[Medium] Grouping: $x^3 + 3x^2 - 4x - 12 = x^2(x+3) - 4(x+3) = (x+3)(x^2 - 4) = (x+3)(x-2)(x+2)$

[Hard] Difference of cubes: $27x^3 - 64 = (3x - 4)(9x^2 + 12x + 16)$
❌ **Sign trap:** the quadratic factor always has the OPPOSITE middle sign ($a^3 + b^3 \to a^2 - ab + b^2$), and it NEVER factors further over the reals.

#### Factoring Decision Quick Reference

| Terms | First Check | Then Try |
|---|---|---|
| 2 | GCF | Diff of squares, sum/diff of cubes |
| 3 | GCF | Perfect square? If not, trinomial method |
| 4 | GCF | Grouping |
| After | - | Can any factor be factored further? |

---

### B2.1.4 Rational Expressions and Complex Fractions

**Definition:** a rational expression is a fraction whose numerator and denominator are polynomials, like $\frac{x^2 - 9}{x^2 + 5x + 6}$. A complex fraction is a fraction that contains fractions inside it. SAT equivalent-expression questions with rationals almost always hinge on factoring + canceling.

**Step-by-step method (simplify):**
1. Factor the numerator completely.
2. Factor the denominator completely.
3. Cancel common FACTORS (not terms).
4. Write the restrictions: any value that zeroed a cancelled factor is still excluded from the domain.

[Medium] $\frac{x^2 - 9}{x^2 + 5x + 6} = \frac{(x-3)(x+3)}{(x+3)(x+2)} = \frac{x-3}{x+2}$, $x \neq -3, -2$

❌ **Cancellation trap:** cancel FACTORS, not terms. $\frac{x+3}{x}$ cannot simplify.
❌ **Sign flip trap:** $\frac{x-3}{3-x} = -1$, not $1$. Factor $-1$: $\frac{x-3}{-(x-3)} = -1$.

[Hard] Which expression is equivalent to $\frac{x^2 - 5x + 6}{x^2 - 9}$ for $x \neq \pm 3$?
$$\frac{x^2 - 5x + 6}{x^2 - 9} = \frac{(x-2)(x-3)}{(x-3)(x+3)} = \frac{x-2}{x+3}, \quad x \neq \pm 3$$
❌ **Over-cancellation trap:** the original expression is undefined at $x = 3$ and $x = -3$ even though the simplified form is not.

**Addition/Subtraction:** use a common denominator.

[Hard] $\frac{2x}{x^2-1} - \frac{1}{x+1} = \frac{2x}{(x-1)(x+1)} - \frac{x-1}{(x-1)(x+1)} = \frac{2x - (x-1)}{(x-1)(x+1)} = \frac{x+1}{(x-1)(x+1)} = \frac{1}{x-1}$

❌ **Critical subtraction trap:** $-(x-1) = -x + 1$, NOT $-x - 1$. Distribute the minus to ALL terms.

**Multiplication/Division:** factor everything, cancel common factors, then multiply (for division, multiply by the reciprocal).

[Medium] $\frac{x^2 - 9}{x+2} \cdot \frac{x^2 - 4}{x-3} = \frac{(x-3)(x+3)}{x+2} \cdot \frac{(x-2)(x+2)}{x-3} = (x+3)(x-2)$

[Medium] $\frac{x^2 - 4}{x+1} \div \frac{x-2}{x+3} = \frac{(x-2)(x+2)}{x+1} \cdot \frac{x+3}{x-2} = \frac{(x+2)(x+3)}{x+1}$

**Complex fractions (optional - rare on the SAT):** multiply numerator and denominator by the LCD of all internal fractions.

[Hard] (Optional) Simplify $\frac{1 + \frac{1}{x}}{1 - \frac{1}{x}}$
- LCD of internal fractions is $x$. Multiply: $\frac{x(1 + \frac{1}{x})}{x(1 - \frac{1}{x})} = \frac{x + 1}{x - 1}$

---

### B2.1.5 Rewriting Radicals and Exponents

**Definition:** a radical $\sqrt[n]{x^m}$ and a rational exponent $x^{m/n}$ are two notations for the SAME number. Converting between them (almost always to exponent form) is the fastest way to simplify chains of radicals and powers.

**Step-by-step method:**
1. Rewrite every radical as a rational exponent: $\sqrt[n]{x^m} = x^{m/n}$.
2. Apply exponent rules (product = add, quotient = subtract, power = multiply).
3. Convert the final answer back to the form the question wants (radical or exponent).

[Easy] $\sqrt[3]{x^2} = x^{2/3}$

[Hard] $\sqrt[3]{x^4 y^2} \cdot \sqrt{xy^3} = x^{4/3}y^{2/3} \cdot x^{1/2}y^{3/2} = x^{4/3 + 1/2} y^{2/3 + 3/2} = x^{11/6} y^{13/6}$

[Hard] Which expression is equivalent to $\frac{\sqrt[3]{x^2}}{\sqrt{x}}$ for $x > 0$?
$$\frac{x^{2/3}}{x^{1/2}} = x^{2/3 - 1/2} = x^{4/6 - 3/6} = x^{1/6} = \sqrt[6]{x}$$

❌ **Exponent addition trap:** $x^{1/2} \cdot x^{1/3} = x^{5/6}$, not $x^{1/6}$.
❌ **Radical-of-square trap:** $\sqrt{x^2} = |x|$, not $x$.

[Hard] Rationalize via conjugate: $\frac{5}{2 - \sqrt{3}} = \frac{5(2 + \sqrt{3})}{(2 - \sqrt{3})(2 + \sqrt{3})} = \frac{5(2 + \sqrt{3})}{4 - 3} = 5(2 + \sqrt{3})$
❌ **Conjugate trap:** must change the middle sign; using $(2-\sqrt{3})$ again does NOT eliminate the radical.

⚡ Convert radicals to fractional exponents first - faster and less error-prone.

---

### B2.1.6 Completing the Square

**Definition:** completing the square rewrites a quadratic $ax^2 + bx + c$ into vertex form $a(x-h)^2 + k$. The name comes from the method: you add and subtract exactly the constant that makes a perfect-square trinomial. SAT uses it to reveal the vertex (min/max) and in "which is equivalent" questions.

**Step-by-step method:**
1. If $a \neq 1$, factor $a$ out of the $x^2$ and $x$ terms only.
2. Take half of the $x$-coefficient: $\frac{b}{2}$ (after factoring).
3. Square it: $\left(\frac{b}{2}\right)^2$.
4. Add and subtract it inside the parentheses.
5. Factor the perfect square, then simplify the constants - remembering to multiply any subtracted term by the factored-out $a$.

$x^2 + bx \to \left(x + \frac{b}{2}\right)^2 - \left(\frac{b}{2}\right)^2$

[Medium] $x^2 + 8x + 3 = (x^2 + 8x + 16) - 16 + 3 = (x+4)^2 - 13$

[Hard] $2x^2 - 12x + 5 = 2(x^2 - 6x) + 5 = 2(x^2 - 6x + 9 - 9) + 5 = 2[(x-3)^2 - 9] + 5 = 2(x-3)^2 - 13$

[Very Hard] Write $3x^2 + 5x - 2$ in vertex form.
$$3x^2 + 5x - 2 = 3\left(x^2 + \frac{5}{3}x\right) - 2 = 3\left[\left(x + \frac{5}{6}\right)^2 - \frac{25}{36}\right] - 2$$
$$= 3\left(x + \frac{5}{6}\right)^2 - \frac{25}{12} - 2 = 3\left(x + \frac{5}{6}\right)^2 - \frac{49}{12}$$
So the vertex is $\left(-\frac{5}{6}, -\frac{49}{12}\right)$ and the minimum value is $-\frac{49}{12}$.

❌ **Leading coefficient trap:** $2(-9) = -18$, not $-9$. The subtracted term must be multiplied by $a$.
❌ **Fraction trap:** half of $\frac{5}{3}$ is $\frac{5}{6}$, not $\frac{5}{3}$; and $\left(\frac{5}{6}\right)^2 = \frac{25}{36}$.
⚡ Desmos: graph the quadratic, click the vertex - read $h$ and $k$ directly.

---

### B2.1.8 Equivalent Forms of Quadratics

**Definition:** every quadratic can be written three ways - standard, vertex, factored - and each form instantly reveals different information. The SAT's favorite trick is giving you one form and asking a question whose answer is "written on the face" of a different form.

| Form | Look | Instantly Reveals | Use When Asked For |
|---|---|---|---|
| Standard | $ax^2 + bx + c$ | $y$-intercept $(0, c)$, end behavior from $a$ | $y$-intercept |
| Vertex | $a(x-h)^2 + k$ | vertex $(h,k)$, min/max $= k$, axis $x = h$ | min/max value, vertex, axis of symmetry |
| Factored | $a(x-r_1)(x-r_2)$ | roots $r_1, r_2$, axis $x = \frac{r_1+r_2}{2}$ | $x$-intercepts, "passes through $(p,0)$" |

**When to convert (decision guide):**
- Asked for **min/max or vertex** → convert to vertex form (or use $x_v = -\frac{b}{2a}$).
- Asked for **$x$-intercepts / roots / zeros** → convert to factored form (or set to 0 and solve).
- Asked for **$y$-intercept** → keep standard form.
- Asked for **"which of these is equivalent"** → expand everything to standard form and compare, or test a point.

The sample question type: $g(x) = x^2 + 55$ "What is the minimum value?" It is already vertex form $1(x-0)^2 + 55$, so the minimum is $55$ - no computation needed once you NAME the form.

[Medium] Which expression is equivalent to $x^2 + 10x + 24$? Both $(x+4)(x+6)$ (factored) and $(x+5)^2 - 1$ (vertex) expand to $x^2 + 10x + 24$ - one quadratic, two revealing forms.
❌ **Sign trap:** $(x+12)(x-2) = x^2 + 10x - 24$ - wrong constant sign.

[Hard] A quadratic has $x$-intercepts $x = -2$ and $x = 5$, passes through $(1, 6)$. Find standard form.
- $f(x) = a(x+2)(x-5)$. Plug $(1,6)$: $6 = a(3)(-4) = -12a \to a = -\frac{1}{2}$
- $f(x) = -\frac{1}{2}(x+2)(x-5) = -\frac{1}{2}(x^2 - 3x - 10) = -\frac{1}{2}x^2 + \frac{3}{2}x + 5$

[Very Hard] Quadratic has vertex $(4, -2)$ and passes through $(2, 10)$. Find $f(x)$.
- $f(x) = a(x-4)^2 - 2$. Plug $(2,10)$: $10 = a(4) - 2 \to a = 3$
- $f(x) = 3(x-4)^2 - 2 = 3x^2 - 24x + 46$

[Hard] The graph of a quadratic function has $x$-intercepts at $x = -3$ and $x = 1$, and opens downward. Which of the following could represent the function?

A) $f(x) = -(x+3)(x-1)$
B) $f(x) = (x+3)(x-1)$
C) $f(x) = -(x-3)(x+1)$
D) $f(x) = (x-3)(x+1)$

$x$-intercepts at $-3$ and $1$ means factors $(x+3)(x-1)$. Opens down means negative leading coefficient. Answer: **A**.
❌ **Choice C trap:** signs reversed - $(x-3)(x+1)$ gives intercepts $3$ and $-1$.

[Medium] Function notation check: for $f(x) = x^2$, $f(x+2) = (x+2)^2 = x^2 + 4x + 4$ (shift left 2), while $f(x)+2 = x^2 + 2$ (shift up 2).
❌ **Notation trap:** students write $f(x+2) = x^2 + 2$, confusing the two.

⚡ Desmos: enter points as a table, fit $y_1 \sim ax_1^2 + bx_1 + c$ for instant quadratic regression.

---

### B2.1 Final Check (mixed "which is equivalent" question)

**Strategy:** eliminate wrong forms by testing a single numeric value (pick $x = 2$ or $x = 1$). If the original and a choice differ at that value, that choice is wrong.

[Very Hard] Which of the following is equivalent to $\frac{2x^2 + 7x - 4}{2x^2 + 9x + 4}$ for $x \neq -4, -\frac{1}{2}$?

A) $\frac{2x - 1}{2x + 1}$
B) $\frac{x + 4}{x + 4}$
C) $\frac{x - 4}{x + 4}$
D) $\frac{2x - 1}{x + 4}$

Factor numerator: $2x^2 + 7x - 4$: need factors of $2 \cdot (-4) = -8$ summing to $7$: $8$ and $-1$. So $2x^2 + 8x - x - 4 = 2x(x+4) - 1(x+4) = (2x - 1)(x + 4)$.
Factor denominator: $2x^2 + 9x + 4$: factors of $8$ summing to $9$: $8$ and $1$. So $2x^2 + 8x + x + 4 = 2x(x+4) + 1(x+4) = (2x + 1)(x + 4)$.
$$\frac{(2x-1)(x+4)}{(2x+1)(x+4)} = \frac{2x-1}{2x+1}$$
Answer: **A**.
❌ **Both-sides trap:** you must factor BOTH numerator and denominator; students factor only the numerator and then guess.
⚡ Desmos: graph the original fraction and choice A - identical curves (except the hole at $x = -4$) confirm equivalence.

---

### B2.1 Summary

- Polynomial add/subtract/multiply: see B2.1.1 (sign errors and full distribution are the traps).
- Expanding special products $(a \pm b)^2$, $(a+b)(a-b)$: see B2.1.1 table (reverse of factoring).
- Factoring patterns and cheat table: see B2.1.2 (GCF first, then count terms).
- Rational simplify, domain restrictions, LCD add/subtract, multiply/divide: see B2.1.4.
- Radical-to-exponent conversion, $\sqrt{x^2} = |x|$, conjugates: see B2.1.5.
- Completing the square to vertex form: see B2.1.6 (factor out $a$ first).
- Naming and converting quadratic forms: see B2.1.8 (vertex for min/max, factored for roots).
- Archived extensions (polynomial theorems, division, extra drills): see Appendix A1-A4.

---

---

## B2.2 - Nonlinear Equations in One Variable and Systems

**What this whole section is about:** equations that are NOT linear - quadratics, radicals, rationals, absolute values, exponentials - plus systems where at least one equation is nonlinear. The official testing point has three moves: SOLVE (find all solutions), COUNT (how many solutions), and CREATE (build the equation from a context). Every equation type below has the same overall workflow: identify the type → apply its signature method → check your answers against the domain (extraneous solutions and excluded values).

**Solution-counting vocabulary the SAT uses:** "how many real solutions," "no real solutions," "exactly one solution," "extraneous solution." Real solutions = $x$-intercepts of the graph. Extraneous = algebraically valid but fails the original equation.

### B2.2.1 Quadratic Equations - Best Method Decision Flow

**Definition:** a quadratic equation has the form $ax^2 + bx + c = 0$ with $a \neq 0$. Its graph is a parabola, and its solutions are the parabola's $x$-intercepts. A quadratic can have 2, 1, or 0 real solutions.

**Step-by-step method:**
1. Get everything on one side: $ax^2 + bx + c = 0$.
2. Choose a method (decision tree below).
3. Solve.
4. For word problems: check the answer makes sense in context (e.g. time cannot be negative).

**Decision tree:**
1. Is it $ax^2 + c = 0$ (no $x$ term)? → **Square root method**
2. Are $a$, $b$, $c$ integers and $a = 1$? → Try **factoring** (find $p + q = b$, $pq = c$)
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

**Square Root:** [Medium] $3(x-4)^2 = 27 \to (x-4)^2 = 9 \to x - 4 = \pm 3 \to x = 7, 1$

❌ **Missing negative root trap:** $x^2 = 25$ gives $x = \pm 5$, not $x = 5$ only.

**Quadratic Formula:** $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$

[Hard] $2x^2 - 7x = 3 \to 2x^2 - 7x - 3 = 0$
$$x = \frac{7 \pm \sqrt{49 - 4(2)(-3)}}{4} = \frac{7 \pm \sqrt{49 + 24}}{4} = \frac{7 \pm \sqrt{73}}{4}$$

❌ **Sign-error trap:** $b = -7$, so $-b = +7$. Write $-(-7)$ explicitly.
❌ **c sign trap:** $c = -3$, so $-4ac = -4(2)(-3) = +24$, not $-24$.

**Completing the Square to Solve:**

[Medium] $x^2 + 6x + 5 = 0$
- $x^2 + 6x = -5 \to x^2 + 6x + 9 = 4 \to (x+3)^2 = 4 \to x + 3 = \pm 2 \to x = -1, -5$

**Discriminant Analysis:** $D = b^2 - 4ac$

| $D$ | Real Solutions | Graph |
|---|---|---|
| $> 0$ | 2 distinct | Two $x$-intercepts |
| $= 0$ | 1 (double root) | Vertex on $x$-axis |
| $< 0$ | 0 | No $x$-intercepts |

[Medium] $3x^2 - 2x + 5 = 0$: $D = 4 - 60 = -56$ - no real solutions.

[Hard] For what $k$ does $x^2 + kx + 9 = 0$ have exactly one solution?
$D = k^2 - 36 = 0 \to k = \pm 6$

❌ **Double-root trap:** Both $k = 6$ AND $k = -6$ give one solution. Students commonly forget $k = -6$.

[Very Hard] For what $k$ does $2x^2 - 4x + k = 0$ have two distinct solutions?
$D = 16 - 8k > 0 \to k < 2$

---

### B2.2.2 Quadratic in Form (u-Substitution)

**Definition:** some equations are not quadratics in $x$ but BECOME quadratics in a substitution $u$. The classic cases: $x^4 - 5x^2 + 6 = 0$ (quadratic in $x^2$) and $4^x - 2^{x+1} = 8$ (quadratic in $2^x$ - see B2.2.6).

**Step-by-step method:**
1. Identify the repeated "inner" expression - call it $u$.
2. Solve the resulting quadratic in $u$.
3. Back-substitute: for each $u$, solve for $x$.
4. Each $u$ can yield 0, 1, or 2 real $x$-values. Count carefully.

[Hard] $x^4 - 5x^2 + 6 = 0$: let $u = x^2$. $u^2 - 5u + 6 = 0 \to u = 2, 3$. Then $x = \pm\sqrt{2}, \pm\sqrt{3}$.

[Very Hard] How many real solutions does $x^4 - 2x^2 - 3 = 0$ have?
- Let $u = x^2$: $u^2 - 2u - 3 = 0 \to (u-3)(u+1) = 0 \to u = 3, -1$.
- $u = 3 \to x = \pm\sqrt{3}$ (2 real solutions). $u = -1 \to x^2 = -1$ (0 real solutions).
- Answer: 2 real solutions.

❌ **Negative-u trap:** $u = -1$ gives NO real $x$-values because $x^2 \geq 0$ always. Do not report imaginary solutions.

---

### B2.2.3 Radical Equations

**Definition:** an equation where the variable sits inside a radical, like $\sqrt{2x + 3} + 5 = x$. The danger: squaring both sides can create EXTRANEOUS solutions - numbers that satisfy the squared equation but not the original. The SAT specifically tests whether you check.

**Step-by-step method:**
1. Isolate the radical on one side (if there are two radicals, isolate one at a time).
2. Raise both sides to the power that removes the radical (square for $\sqrt{}$).
3. Solve the resulting equation.
4. **ALWAYS check every candidate in the ORIGINAL equation.** Reject any that fail. For even-index radicals, an instant red flag is a candidate that makes a radicand negative or fails the sign of the isolated side.

[Hard] $\sqrt{2x + 3} + 5 = x$
1. $\sqrt{2x + 3} = x - 5$
2. $2x + 3 = x^2 - 10x + 25 \to 0 = x^2 - 12x + 22$
3. $x = \frac{12 \pm \sqrt{144 - 88}}{2} = 6 \pm \sqrt{14}$
4. Check $6 + \sqrt{14} \approx 9.74$: $\sqrt{22.48} + 5 \approx 9.74$ ✓
5. Check $6 - \sqrt{14} \approx 2.26$: $\sqrt{7.52} + 5 \approx 7.74 \neq 2.26$ ❌ **Extraneous**
6. Answer: $x = 6 + \sqrt{14}$ only

[Hard] How many real solutions does $\sqrt{x + 3} = x - 3$ have?
- Square: $x + 3 = x^2 - 6x + 9 \to x^2 - 7x + 6 = 0 \to (x-1)(x-6) = 0 \to x = 1, 6$.
- Check $x = 1$: $\sqrt{4} = 2$, but $x - 3 = -2$. $2 \neq -2$ ❌ Extraneous.
- Check $x = 6$: $\sqrt{9} = 3$, and $x - 3 = 3$. $3 = 3$ ✓.
- Answer: exactly 1 real solution ($x = 6$).

❌ **No-check trap:** Both answers may seem algebraically valid, but only one may satisfy the original.
❌ **Pre-squaring trap:** Squaring without isolating the radical first creates cross-term mayhem.

⚡ Desmos: graph $y = \sqrt{x+3}$ and $y = x - 3$; the single intersection at $x = 6$ confirms the extraneous root died.

Odd-root equations do not create extraneous roots because cubing is one-to-one.

---

### B2.2.4 Rational Equations

**Definition:** an equation with fractions whose denominators contain variables, like $\frac{x}{x-3} + \frac{2}{x+1} = \frac{5}{x^2 - 2x - 3}$. The plan: clear denominators with the LCD, solve, then EXCLUDE any value that zeroes a denominator (those values are not in the domain, so they can never be solutions - even if the cleared equation produces them).

**Step-by-step method:**
1. Factor every denominator.
2. Find the LCD (least common denominator).
3. Multiply BOTH sides by the LCD to clear all fractions.
4. Solve the resulting polynomial equation.
5. Check every candidate against the excluded values (denominator $= 0$). Reject excluded candidates.

[Medium] $\frac{5}{x} + \frac{3}{2} = \frac{7}{4}$: multiply by $4x \to 20 + 6x = 7x \to x = 20$. Restriction $x \neq 0$ ✓.

[Hard] $\frac{x}{x-3} + \frac{2}{x+1} = \frac{5}{x^2 - 2x - 3}$
- Factor: $x^2 - 2x - 3 = (x-3)(x+1)$
- Multiply by $(x-3)(x+1)$: $x(x+1) + 2(x-3) = 5 \to x^2 + 3x - 11 = 0$
- $x = \frac{-3 \pm \sqrt{53}}{2}$. Restrictions $x \neq 3, -1$, neither violated ✓.

❌ **Restrictions trap:** Forgetting to exclude values that zero any denominator.

[Hard] How many real solutions does $\frac{x^2}{x - 1} = \frac{1}{x - 1}$ have?
- Multiply by $x - 1$: $x^2 = 1 \to x = \pm 1$.
- Check the restriction: $x = 1$ makes the denominator $0$ ❌ - excluded, cannot be a solution.
- Check $x = -1$: $\frac{1}{-2} = \frac{1}{-2}$ ✓.
- Answer: exactly 1 real solution.

❌ **Zero-denominator trap:** $x = 1$ solves the cleared equation but is NOT a solution of the original - it is undefined there. The SAT loves this exact trap.

⚡ If the equation is $\frac{A}{B} = \frac{C}{D}$ (proportion form), cross-multiply directly: $AD = BC$.

---

### B2.2.5 Absolute Value Equations

**Definition:** absolute value $|x|$ measures distance from zero - it is never negative. The equation $|A| = B$ says "the distance of $A$ from 0 equals $B$," which splits into two cases. (For graphing and transforming absolute-value functions, see B2.3.)

**Step-by-step method (solve):**
1. Isolate the absolute value: get $|A| = B$ with everything else moved out.
2. If $B < 0$: no solution (absolute value cannot equal a negative).
3. If $B \geq 0$: solve $A = B$ and $A = -B$.
4. Check solutions in the original equation when variables appear inside the absolute value on both sides.

[Medium] $|2x + 5| - 3 = 10 \to |2x + 5| = 13 \to x = 4$ or $x = -9$

❌ **No-solution trap:** $|x| = -5$ has no solution. Absolute value cannot be negative.

[Hard] $|x - 2| = |3x + 1| \to x - 2 = 3x + 1$ or $x - 2 = -(3x+1) \to x = -\frac{3}{2}, \frac{1}{4}$

⚡ Desmos: Graph $y = |x-2|$ and $y = |3x+1|$; intersections give solutions.

**Parameter solution counts (SAT favorite):**

[Hard] For which values of $k$ does $|x - 3| = k$ have exactly two solutions?
- $|x-3| = k$ has 2 solutions iff $k > 0$, exactly 1 solution iff $k = 0$, and 0 solutions iff $k < 0$.
- Answer: $k > 0$. Think of the graph: the horizontal line $y = k$ cuts the V-shape twice only when it sits above the vertex.

---

### B2.2.6 Exponential Equations

**Definition:** an equation where the variable lives in an exponent, like $3^{x^2 - 4} = 27^{x+2}$. If you can rewrite both sides with the SAME base, the exponents must be equal. If not, substitute $u = b^x$ (making a quadratic) or graph both sides in Desmos.

**Step-by-step method:**
1. Try to rewrite both sides with the same base.
2. Equate the exponents: $a^{f(x)} = a^{g(x)} \Rightarrow f(x) = g(x)$.
3. Solve the resulting (often linear or quadratic) equation.
4. If bases cannot match: substitute $u = b^x$ and solve the quadratic in $u$; reject $u \leq 0$ because $b^x > 0$ always.

[Hard] $3^{x^2 - 4} = 27^{x+2} \to 3^{x^2-4} = 3^{3x+6} \to x^2 - 3x - 10 = 0 \to x = 5, -2$

❌ **Different-base trap:** MUST rewrite to the same base before equating exponents.

[Very Hard] $4^x - 2^{x+1} = 8$
- Rewrite $4^x = 2^{2x}$, $2^{x+1} = 2 \cdot 2^x$. Let $u = 2^x$: $u^2 - 2u - 8 = 0 \to u = 4, -2$.
- $u = 4 \to 2^x = 4 \to x = 2$. $u = -2$: reject ($2^x > 0$ for all real $x$).

❌ **Exponential positivity trap:** $b^x$ is ALWAYS positive. Reject any $u$-solution $\leq 0$.

⚡ If bases cannot be matched cleanly, graph both sides in Desmos and find the intersection.

---

### B2.2.7 Systems of Equations (Linear + Nonlinear)

**General Strategy:** Substitute the linear equation into the nonlinear one, solve, back-substitute. The AF names the system types explicitly - each has its own signature move, so **name the type before you start**:

| System Type | Signature Move | Max Solutions | How to Count |
|---|---|---|---|
| Linear + Linear | elimination or substitution | 1 | parallel lines → 0; identical → infinite |
| Linear + Quadratic (line + parabola) | substitute line into parabola | 2 | discriminant of resulting quadratic: $D > 0$ → 2, $D = 0$ → 1, $D < 0$ → 0 |
| Linear + Circle (line + circle) | substitute line into circle | 2 | same discriminant rule - see B4.5 |
| Linear + Absolute Value (line + V) | split into cases by sign of inside | 2 | solve each case, CHECK case condition |
| Quadratic + Quadratic (two parabolas) | subtract to eliminate $y$ | 2 | solve for $x$, then find $y$ |
| Linear + Exponential | substitute; can't match bases | usually 0-2 | graph or test values |

**TYPE 1: Linear + Quadratic** - substitute the line into the parabola, get a quadratic in $x$:

[Medium] $y = 2x + 1$, $y = x^2 - 2x + 3 \to 2x + 1 = x^2 - 2x + 3 \to x^2 - 4x + 2 = 0$
$x = 2 \pm \sqrt{2}$, $y = 5 \pm 2\sqrt{2}$

⚡ Desmos: Graph both - intersection points are solutions.

**Line + circle systems** live in B4.5 (substitute the line into the circle; the discriminant counts 2/1/0 intersections) - see the line + circle block at the end of B4.5.

**TYPE 2: Linear + Absolute Value** - split into cases by the sign of the inside of the absolute value, solve each case, and CHECK every candidate against its case condition:

[Medium] $y = 2x - 1$, $y = |x + 2|$
- Case 1 ($x+2 \geq 0$): $2x-1 = x+2 \to x = 3$ ✓
- Case 2 ($x+2 < 0$): $2x-1 = -(x+2) \to x = -\frac{1}{3}$ - violates condition ❌ **Domain trap**
- Solution: $(3,5)$ only

**TYPE 3: Quadratic + Quadratic** - subtract the equations to eliminate $y$, then solve for $x$:

[Hard] $y = x^2 - 4$, $y = -x^2 + 4 \to 2x^2 = 8 \to x = \pm 2$. Solutions: $(2,0)$, $(-2,0)$

[Very Hard] $y = x^2 - 2x$, $y = -x^2 + 6x - 8 \to 2x^2 - 8x + 8 = 0 \to (x-2)^2 = 0 \to x = 2$ (tangent). Solution: $(2,0)$

**System Solutions by Discriminant:**

When $y = mx + d$ is substituted into $y = ax^2 + bx + c$, the resulting $ax^2 + (b-m)x + (c-d) = 0$ has discriminant $D$:
- $D > 0$: 2 intersections
- $D = 0$: 1 (tangent)
- $D < 0$: 0

[Hard] For what $k$ does $y = 2x + k$ intersect $y = x^2 - 3x + 1$ exactly once?
$2x + k = x^2 - 3x + 1 \to x^2 - 5x + (1-k) = 0$. $D = 25 - 4(1-k) = 21 + 4k = 0 \to k = -\frac{21}{4}$

[Very Hard] The system $y = |x|$ and $y = x^2 - 2$ has how many solutions?
- Case 1 ($x \geq 0$): $x = x^2 - 2 \to x^2 - x - 2 = 0 \to (x-2)(x+1) = 0 \to x = 2$ (valid) or $x = -1$ (violates $x \geq 0$ ❌).
- Case 2 ($x < 0$): $-x = x^2 - 2 \to x^2 + x - 2 = 0 \to (x+2)(x-1) = 0 \to x = -2$ (valid) or $x = 1$ (violates $x < 0$ ❌).
- Answer: 2 solutions: $(2, 2)$ and $(-2, 2)$.

⚡ Desmos: graph both curves; each intersection is a solution. For "how many" questions, the graph is usually faster than casework.

---

### B2.2.9 Solving for a Variable of Interest (Rearranging Nonlinear Formulas)

**What it is:** the AF tests "interpreting and creating equations" - you get a formula that is NOT linear in the target variable and you must isolate it. Same reverse-operations drill as linear equations, but the operations are radicals, fractions, and exponents, so $\pm$ signs and restrictions appear.

**Method:**
1. Identify the target variable.
2. Undo operations in reverse order (the operation "closest" to the variable is undone last... no - the LAST operation applied to the variable is undone FIRST).
3. If the variable sits inside a square root → isolate the radical, then square.
4. If the variable is in a denominator → multiply through by the LCD (or cross-multiply if it is a proportion).
5. If the variable is inside a square or other even power → take the corresponding root and keep $\pm$.
6. Check the result against any restrictions from the original formula.

[Easy] Solve for $r$: $A = \pi r^2$.
$r^2 = \frac{A}{\pi} \to r = \pm\sqrt{\frac{A}{\pi}}$. In a geometry context $r > 0$, so $r = \sqrt{\frac{A}{\pi}}$.

[Medium] Solve for $L$: $T = 2\pi\sqrt{\frac{L}{g}}$.
- $\frac{T}{2\pi} = \sqrt{\frac{L}{g}} \to \frac{T^2}{4\pi^2} = \frac{L}{g} \to L = \frac{gT^2}{4\pi^2}$.
- No $\pm$ needed: $L$ is a length, and $\frac{L}{g} > 0$ in context.

[Hard] Solve for $R_1$: $\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2}$ (parallel resistors - a recurring SAT formula).
- Multiply by the LCD $R \cdot R_1 \cdot R_2$: $R_1 R_2 = R R_2 + R R_1$.
- Collect the $R_1$ terms: $R_1 R_2 - R R_1 = R R_2 \to R_1(R_2 - R) = R R_2$.
- $R_1 = \frac{R R_2}{R_2 - R}$.

❌ **LCD trap:** multiplying by the LCD clears ALL denominators at once - do not multiply term-by-term or fractions survive.

---

---

## B2.3 - Nonlinear Functions

**What this whole section is about:** applying ALL the function concepts from linear algebra (domain, range, min/max, increasing/decreasing, end behavior, graph features, transformations) to NONLINEAR functions - quadratics, absolute values, rationals, radicals, polynomials, and exponentials. The SAT asks you to interpret, not just compute: "what does the 10 represent?", "which statement must be true?", "which graph could represent f?"

### B2.3.1 Domain and Range

**Definition:** the domain is the set of ALLOWED inputs $x$; the range is the set of all possible outputs $y = f(x)$. Restrictions come from three sources: even-index radicals (radicand $\geq 0$), denominators (cannot be $0$), and real-world context (time, quantity $\geq 0$).

| Cause | Condition |
|---|---|
| Square root (even-index radical) | Radicand $\geq 0$ |
| Denominator | $\neq 0$ |
| Real-world context | Usually $x \geq 0$ or within bounds |

[Medium] Domain of $f(x) = \frac{\sqrt{x-5}}{x-8}$: $x \geq 5$ and $x \neq 8$, so $[5,8) \cup (8,\infty)$.

[Hard] Range of $f(x) = 3 + \sqrt{2x - 4}$: $\sqrt{2x-4} \geq 0$, so $f(x) \geq 3$, giving $[3,\infty)$.

[Hard] Range of $f(x) = -2|x-3| + 5$: $|x-3| \geq 0$ gives $-2|x-3| \leq 0$, so $f(x) \leq 5$, giving $(-\infty, 5]$.

❌ **Domain vs. range trap:** Domain = $x$-values, range = $y$-values.
❌ **Union trap:** when two restrictions both apply, use $\cup$ for the pieces - $[5,8) \cup (8,\infty)$, not $[5, \infty)$.

---

### B2.3.2 Maximum and Minimum

**Definition:** for a quadratic, the vertex is either the lowest point (minimum, when $a > 0$) or the highest point (maximum, when $a < 0$). The SAT asks "what is the minimum/maximum value" (the $y$-coordinate $k$) or "at what $x$" (the $h$).

**Step-by-step method:**
1. Find $x_v = -\frac{b}{2a}$ (or read $h$ from vertex form $f(x) = a(x-h)^2 + k$).
2. Find $y_v = f(x_v)$ (or read $k$).
3. State the value: minimum if $a > 0$, maximum if $a < 0$.

$x_v = -\frac{b}{2a}$, $y_v = f(x_v)$. $a > 0$: minimum. $a < 0$: maximum.

[Medium] $f(x) = -2x^2 + 12x - 7$: $x_v = -\frac{12}{-4} = 3$, $y_v = -18 + 36 - 7 = 11$. Maximum of $11$ at $x = 3$.

[Hard] What is the minimum value of $g(x) = 3(x+2)^2 - 7$?
- Already vertex form: $a = 3 > 0$, vertex $(-2, -7)$. Minimum value $= -7$ (at $x = -2$). No computation needed.

[Very Hard] A quadratic function has a maximum value of $8$ at $x = 2$ and passes through $(0, 4)$. Find $f(x)$.
- Vertex form: $f(x) = a(x-2)^2 + 8$. Plug $(0, 4)$: $4 = a(4) + 8$, so $a = -1$.
- $f(x) = -(x-2)^2 + 8 = -x^2 + 4x + 4$.

⚡ Desmos: graph, click the vertex for exact coordinates.

---

### B2.3.3 Increasing / Decreasing Intervals

**Definition:** a function is increasing where its graph rises as $x$ moves right, decreasing where it falls. For a parabola the vertex $x = h$ splits the domain: one side up, one side down.

- $a > 0$: decreasing on $(-\infty, h)$, increasing on $(h, \infty)$
- $a < 0$: increasing on $(-\infty, h)$, decreasing on $(h, \infty)$

[Medium] Over which interval is $f(x) = x^2 - 4x + 1$ decreasing?
- $h = -\frac{-4}{2} = 2$. Opens up. Decreasing on $(-\infty, 2)$.

---

### B2.3.4 End Behavior

**Definition:** end behavior describes what $f(x)$ does as $x \to \infty$ and $x \to -\infty$. For polynomials only the leading term $ax^n$ matters; for exponentials the base decides growth vs. flattening toward the asymptote.

**Polynomials:** the four even/odd $\times$ positive/negative cases live in the Formula Reference end-behavior tables - use those. Rule of thumb: $f(x) = -3x^4 + 2x^3 - 5$ has leading term $-3x^4$, so both ends go to $-\infty$.

**Exponentials:** for $f(x) = a \cdot b^x + k$, if $b > 1$ the right end shoots to $\infty$ and the left end flattens to $y = k$; if $0 < b < 1$ the reverse holds.

[Medium] As $x \to \infty$, $f(x) = 2^x \to \infty$; as $x \to -\infty$, $2^x \to 0$ (approaches HA $y = 0$ from above).

[Medium] As $x \to \infty$, $g(x) = 100(0.5)^x + 3 \to 3$ (the horizontal asymptote $y = 3$).

**Rational functions:** equal degrees give HA = ratio of leading coefficients. $f(x) = \frac{5x^3 - 2x}{x^3 + 1} \to y = \frac{5}{1} = 5$ as $x \to \infty$.

❌ **Degree trap:** use the HIGHEST-degree term in numerator and denominator, not the first term you see.

---

### B2.3.5 Graph Features

**Definition:** the features that define a graph: intercepts (where it crosses the axes), asymptotes (lines the graph approaches but never touches), and holes (missing points where a factor cancels). Even/odd symmetry: even means $f(-x) = f(x)$ ($y$-axis symmetry); odd means $f(-x) = -f(x)$ (origin symmetry).

**Intercepts:** $x$-intercept: set $y = 0$. $y$-intercept: compute $f(0)$.

**Vertical asymptotes:** denominator $= 0$ with numerator $\neq 0$ at that $x$.

[Medium] $f(x) = \frac{2x+1}{(x-3)(x+2)}$: VA at $x = 3$ and $x = -2$.

**Holes vs. vertical asymptotes:**

| Feature | Condition | Graph |
|---|---|---|
| Hole | Factor cancels entirely | Missing point (open circle) |
| VA | Denominator $= 0$, numerator $\neq 0$ at that $x$ | Vertical line, unbounded |

[Hard] $f(x) = \frac{(x-2)(x+3)}{(x-2)(x+5)}$: $x = 2$ is a hole (cancels), $x = -5$ is a VA (does not cancel).

❌ **Hole vs. VA trap:** if $(x-2)$ cancels, there is NO asymptote at $x = 2$ - only a hole.

[Hard] A rational function has VA at $x = -1$ and a hole at $x = 2$. Which could be $f(x)$?

A) $f(x) = \frac{x-2}{(x+1)(x-2)}$
B) $f(x) = \frac{x+1}{(x+1)(x-2)}$
C) $f(x) = \frac{(x+1)(x-2)}{x-2}$
D) $f(x) = \frac{(x+1)(x-2)}{x+1}$

Check each: A) hole at $2$, VA at $-1$ ✓. Answer: **A**.

❌ **Choice B trap:** hole at $x = -1$, VA at $x = 2$ - reversed.

---

### B2.3.6 Transformations

**Definition:** transformations move and reshape any graph - shifting, reflecting, stretching. Inside changes affect $x$ (and work "backwards"); outside changes affect $y$.

| Change | Effect |
|---|---|
| $f(x-h)$ | Shift right $h$ |
| $f(x+h)$ | Shift left $h$ |
| $f(x) + k$ | Shift up $k$ |
| $f(x) - k$ | Shift down $k$ |
| $-f(x)$ | Reflect over $x$-axis |
| $f(-x)$ | Reflect over $y$-axis |
| $a \cdot f(x)$, $a > 1$ | Vertical stretch |
| $a \cdot f(x)$, $0 < a < 1$ | Vertical compression |

[Medium] $f(x) = x^2$, $g(x) = (x-4)^2 + 3$ is $f$ shifted right $4$ and up $3$.

[Hard] $f(x) = \sqrt{x}$ shifted right $2$, down $5$, reflected over $x$-axis: $g(x) = -\sqrt{x-2} - 5$.

❌ **Horizontal shift trap:** $f(x+3)$ shifts LEFT (opposite of intuition).

[Hard] $f(x) = x^2$. Apply: reflect over $x$-axis, then shift right $2$, then shift up $3$. What is $g(x)$?
- Reflect: $-x^2$. Shift right $2$: $-(x-2)^2$. Shift up $3$: $g(x) = -(x-2)^2 + 3$.

❌ **Order trap (genuinely non-commuting pair):** vertical shift and $x$-axis reflection do NOT commute. Shift up $3$ then reflect: $-(x^2 + 3) = -x^2 - 3$. Reflect then shift up $3$: $-x^2 + 3$. Different signs on the constant - order matters here. (By contrast, shifting right then reflecting over the $x$-axis gives the same result as reflecting then shifting right: both give $-(x-2)^2$.)

---

### B2.3.7 Polynomial Specifics

**Definition:** the special facts about polynomial graphs: where they cross vs. touch the $x$-axis (multiplicity), and how the leading term controls end behavior. (Factor/Remainder Theorem and synthetic division live in the appendix - see B2.3.10/11 appendix note.)

**Zero multiplicity:** even multiplicity $\to$ touch/bounce; odd multiplicity $\to$ cross. Single root (mult 1) passes straight through; double root (mult 2) touches and bounces; triple root (mult 3) crosses with an S-curve flattening.

[Hard] $f(x) = -(x+1)^2(x-3)(x-5)^3$
- $x = -1$: mult $2$ (even) $\to$ bounce
- $x = 3$: mult $1$ (odd) $\to$ cross
- $x = 5$: mult $3$ (odd) $\to$ S-curve cross
- Leading term: $-x^5$ $\to$ up left, down right

[Hard] A polynomial graph touches the $x$-axis at $x = -2$, crosses at $x = 1$, with ends up left / down right. Which could be $f(x)$?

A) $f(x) = -(x+2)^2(x-1)$
B) $f(x) = (x+2)^2(x-1)$
C) $f(x) = -(x+2)(x-1)^2$
D) $f(x) = (x+2)(x-1)$

Touch at $-2$ gives even multiplicity $(x+2)^2$; cross at $1$ gives $(x-1)$; ends up-left/down-right give negative leading coefficient. Answer: **A**.

**Least possible degree from a graph:** sum the minimum multiplicities (cross $= 1$, touch $= 2$), then check parity against end behavior.

[Hard] A polynomial graph crosses at $x = -1$, touches at $x = 2$, and crosses at $x = 5$, with both ends up. Minimum degree?
- Cross at $-1$: $\geq 1$. Touch at $2$: $\geq 2$. Cross at $5$: $\geq 1$. Total $1 + 2 + 1 = 4$; both ends up means even degree. Minimum degree: $4$.

❌ **Degree trap:** count multiplicities, not roots. Three roots $\neq$ degree $3$ - a touch needs multiplicity $\geq 2$.

---

### B2.3.8 Exponential Interpretation

**Definition:** exponential functions model quantities that multiply by a fixed factor each unit of time: $f(x) = a \cdot b^x$ with $a = f(0)$ the initial amount and $b$ the growth factor ($b > 1$) or decay factor ($0 < b < 1$). Increase of $r\%$ gives $b = 1 + \frac{r}{100}$; decrease of $r\%$ gives $b = 1 - \frac{r}{100}$. If the change happens every $d$ units, use $f(x) = a \cdot b^{x/d}$.

| $b$ | Behavior | Meaning |
|---|---|---|
| $b > 1$ | Growth | $b = 1 + r$ |
| $0 < b < 1$ | Decay | $b = 1 - r$ |

[Easy] $f(t) = 500(1.08)^t$: initial $= 500$, growth rate $= 8\%$.

❌ **Percent trap:** $1.08$ is an $8\%$ increase (NOT $108\%$). $0.92$ is an $8\%$ decrease (NOT $92\%$).

[Medium] A car worth \$25,000 depreciates by $12\%$ each year. Which function models its value after $t$ years?

A) $V(t) = 25000(0.12)^t$
B) $V(t) = 25000(0.88)^t$
C) $V(t) = 25000(1.12)^t$
D) $V(t) = 25000 - 3000t$

Depreciates $12\%$ so retains $88\%$: multiplier $0.88$. Answer: **B**.

[Hard] The half-life of a radioactive substance is $30$ days. Which function models the mass $M(t)$ of a $50$-gram sample after $t$ days?

A) $M(t) = 50(0.5)^{t/30}$
B) $M(t) = 50(0.5)^{30t}$
C) $M(t) = 50(2)^{t/30}$
D) $M(t) = 50 - \frac{t}{30} \cdot 25$

Half-life formula: $M(t) = a(1/2)^{t/h} = 50(0.5)^{t/30}$. Answer: **A**.

[Hard] The function $A(t) = 18000(1.1025)^{t/2}$ models an investment $t$ years after opening. By what percent does the amount increase every $8$ years?
- Every $8$ years $=$ $4$ periods of $2$ years. Factor: $(1.1025)^{8/2} = (1.1025)^4 \approx 1.4775$.
- Percent increase: $(1.4775 - 1) \times 100 \approx 47.75\%$. Answer: about $47.75\%$.

❌ **Period trap:** $(1.1025)^{t/2}$ means $10.25\%$ growth every $2$ years, NOT every year (per-year factor is $\sqrt{1.1025} = 1.05$, i.e. $5\%$ per year).

[Hard] A population is modeled by $P(t) = 4000(0.8)^{t/3}$. What is the meaning of the $\frac{t}{3}$ in the exponent?
- The quantity decays by $20\%$ every $3$ units of time (each $3$-unit period multiplies by $0.8$).

---

### B2.3.9 Rational Function Transformations

**Definition:** the simplest rational functions are transformations of the parent $\frac{1}{x}$: $f(x) = \frac{a}{x-h} + k$. VA at $x = h$, HA at $y = k$. Domain: $x \neq h$. Range: $y \neq k$ (simple form).

[Medium] $f(x) = \frac{3}{x-2} + 1$: VA $x = 2$, HA $y = 1$. Domain: $x \neq 2$, Range: $y \neq 1$.

[Hard] $f(x) = \frac{2x+1}{x-3} = 2 + \frac{7}{x-3}$: VA $x = 3$, HA $y = 2$.

❌ **HA trap:** the HA of $\frac{2x+1}{x-3}$ is $y = 2$ (ratio of leading coefficients), NOT $y = \frac{1}{-3}$.

---

## The 12 Traps of Advanced Math

1. **Middle term in $(a+b)^2$:** $(x+3)^2 = x^2 + 6x + 9$, NOT $x^2 + 9$.
2. **Sum vs. diff of squares:** $x^2 - 49$ factors; $x^2 + 49$ does not over reals.
3. **Extraneous roots:** ALWAYS check radical equation solutions in the ORIGINAL equation.
4. **Denominator restrictions:** $x \neq$ values that zero any denominator - even after canceling.
5. **Absolute value $=$ negative:** $|x| = -5$ has no solution.
6. **$f(x+3)$ shifts LEFT:** intuition says right, math says left.
7. **Double root parameter:** $k = \pm 6$ when $D = 0$, not just $k = 6$.
8. **Bounce vs. cross:** even multiplicity $=$ bounce, odd $=$ cross.
9. **Percent vs. multiplier:** $1.08$ is $8\%$ increase (NOT $108\%$). $0.92$ is $8\%$ decrease.
10. **Completing square with $a \neq 1$:** factor $a$ first; multiply subtracted term by $a$.
11. **Cancel factors, not terms:** only cancel FACTORS. $\frac{x+3}{x}$ cannot simplify.
12. **Exponential positivity and scaled time:** $b^x > 0$ always (reject $u$-solutions $\leq 0$); $(1.08)^{t/2}$ is $8\%$ every $2$ units, not per unit.

Note: the piecewise-branch and Vieta-sign traps travel with their sections (archived by other agents), so they are dropped here.

---

## Desmos Strategy Quick Reference

- Roots: graph $y = f(x)$, click $x$-intercepts.
- Vertex/min/max: graph, click the turning point.
- System solutions: graph both curves, click intersections; the COUNT of intersections is the solution count.
- Equivalent expressions: graph the original plus each choice; the correct one overlaps perfectly.
- Exponential fit: enter the table, use $y_1 \sim a \cdot b^{x_1}$.
- Quadratic fit: enter the table, use $y_1 \sim ax_1^2 + bx_1 + c$.
- Parameter tangency: graph with a slider (e.g. $y = x^2 + kx + 9$), adjust until curves just touch (confirms $D = 0$).
- Extraneous-root check: graph the original equation; false algebraic roots visibly fail.
- Transformation check: graph $f$ and $g$ side by side to verify shifts/reflections.
- Graph-window warning: "no intersection" may be a zoom issue - zoom out; Desmos may draw a spurious vertical line at a VA.
- Domain/range check: the visible $x$-extent is the domain, the $y$-extent is the range.
- Factoring verification: the $x$-intercepts should match the claimed factors.
- When NOT to use Desmos: simple factoring, single-variable algebra under ~$15$ seconds, coefficient-meaning questions, anything needing exact radical form - solve on paper.
