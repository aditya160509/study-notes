## B2 Practice Set (moved Mixed Reasoning banks from B2.3 end matter)

### Must-Be-True / Could-Be-True

[Hard] The quadratic $f(x) = x^2 + kx + 9$ has exactly one real solution. Which statement must be true?

A) $k = 6$
B) $k = -6$
C) $k = \pm 6$
D) $k > 6$ or $k < -6$

$D = k^2 - 36 = 0 \to k = \pm 6$. Answer: **C**.

❌ **Choice A trap:** solving $k^2 = 36 \to k = 6$ forgets $k = -6$.

[Hard] The function $f(x) = ax^2 + bx + c$ opens upward and has $x$-intercepts at $-2$ and $5$. Which statement must be true?

A) $a > 0$ and $c < 0$
B) $a < 0$ and $c > 0$
C) $a > 0$ and $c > 0$
D) $a < 0$ and $c < 0$

Opens up $\to a > 0$. $c = f(0)$; with intercepts at $-2$ and $5$, the $y$-intercept is negative. Answer: **A**.

[Hard] The system $y = x^2 - 6x + 10$ and $y = 2x + k$ has NO real solutions. Which could be a value of $k$?

A) $-7$
B) $-6$
C) $-5$
D) $5$

$x^2 - 6x + 10 = 2x + k \to x^2 - 8x + (10 - k) = 0$. $D = 64 - 4(10 - k) = 24 + 4k < 0 \to k < -6$. Only $-7$ works. Answer: **A**.

[Very Hard] The polynomial $p(x) = ax^3 + bx^2 + cx + d$ has $x$-intercepts at $x = -2, 1, 4$ and passes through $(0, -8)$. Which statement must be true?

A) $a > 0$
B) $a < 0$
C) $a = 2$
D) $a = -2$

Factored: $p(x) = a(x+2)(x-1)(x-4)$. Plug $(0,-8)$: $-8 = a(2)(-1)(-4) = a(8) \to a = -1$. So $a < 0$. Answer: **B**.

---

### Which Function Could Satisfy These Conditions?

[Hard] A quadratic function $f$ has $f(0) = 3$ and $f(2) = 7$. Which of the following could be $f(x)$?

A) $f(x) = x^2 + 3$
B) $f(x) = (x-1)^2 + 3$
C) $f(x) = -(x-1)^2 + 4$
D) All of the above

Check A: $f(0) = 3$ ✓, $f(2) = 7$ ✓. Check B: $f(0) = 4$ ❌. Check C: $f(0) = 3$ ✓, $f(2) = 3$ ❌. Only A works. Answer: **A**.

[Hard] Which graph could represent $f(x) = -(x-2)^2 + 4$?
- Opens down, vertex at $(2,4)$. $x$-intercepts: $-(x-2)^2 + 4 = 0 \to (x-2)^2 = 4 \to x = 0, 4$. Look for: parabola opening down, peak at $(2,4)$, crossing at $0$ and $4$.

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

First differences: $2, 4, 8$ (not constant). Pattern: $3 = 2^1 + 1$, $5 = 2^2 + 1$, $9 = 2^3 + 1$, $17 = 2^4 + 1$ - exponential ($2^{x+1} + 1$). Answer: **C**.

❌ **Linear trap:** first differences look "almost linear" at a glance but double each time.

⚡ Desmos: enter the table, fit $y_1 \sim a \cdot b^{x_1}$; a good fit with clean $b$ says exponential.

---

### Interpret Coefficient Meaning

[Hard] The function $h(t) = -16t^2 + 64t + 10$ models the height (feet) of a projectile $t$ seconds after launch. What does the $10$ represent?

A) The maximum height
B) The initial height
C) The time to reach max height
D) The height after $1$ second

$h(0) = 10$, so it is the initial height. Answer: **B**.

[Hard] In the quadratic $y = 2(x-3)^2 + 5$, what does the $3$ represent?

A) The $y$-coordinate of the vertex
B) The $x$-coordinate of the vertex
C) The $y$-intercept
D) The axis is $x = -3$

Vertex form $a(x-h)^2 + k$: $h = 3$, so $x$-coordinate of vertex. Answer: **B**.

### Find Missing Parameter

[Hard] The function $f(x) = a(2)^x + 3$ passes through $(2, 19)$. Find $a$.
- $19 = a(2)^2 + 3 \to 19 = 4a + 3 \to a = 4$.

[Hard] The quadratic $f(x) = x^2 + bx + c$ has $x$-intercepts at $2$ and $5$. Find $b + c$.
- Factored: $f(x) = (x-2)(x-5) = x^2 - 7x + 10$. So $b = -7$, $c = 10$, $b + c = 3$.

❌ **Sign trap:** $b = -(p+q) = -(2+5) = -7$, not $7$.

### Choose Correct Model

[Hard] A balloon rises at $3$ feet per second from an initial height of $10$ feet. Which model best represents its height after $t$ seconds?

A) $h(t) = 3t + 10$
B) $h(t) = 10(3)^t$
C) $h(t) = 3^t + 10$
D) $h(t) = 3t^2 + 10$

Constant rate ($3$ ft/s) + initial ($10$ ft) gives linear. Answer: **A**.

### Estimate from Graph

[Hard] The graph of $y = f(x)$ is a parabola opening up with vertex $(-1, -4)$ and passing through $(0, -3)$. Estimate $f(2)$.
- Vertex form: $f(x) = a(x+1)^2 - 4$. Plug $(0,-3)$: $-3 = a(1) - 4 \to a = 1$. $f(x) = (x+1)^2 - 4$. $f(2) = 9 - 4 = 5$.

[Hard] From the graph of $y = -x^2 + 4x$, estimate the $x$-intercepts.
- $0 = -x(x - 4) \to x = 0, 4$.

### Choose Best Method

[Medium] What is the best first step to solve $3(x-2)^2 = 27$?

A) Expand $(x-2)^2$
B) Multiply both sides by $3$
C) Divide both sides by $3$, then square root
D) Use quadratic formula

Divide by $3$: $(x-2)^2 = 9$, then $x-2 = \pm 3 \to x = 5, -1$. Answer: **C**.

[Hard] What is the best first step to solve $\sqrt{2x+3} = x - 5$?

A) Square both sides
B) Isolate the radical - already done
C) Move all terms to one side
D) Check for extraneous solutions

The radical is already isolated. Next: square both sides. Answer: **B** (first step already done). If asked for the "next step," it is **A**.

### Mixed Nonlinear Review - Final Set

[Easy] Solve: $x^2 - 7x + 12 = 0$.
- $(x-3)(x-4) = 0 \to x = 3, 4$.

[Easy] Simplify: $\frac{x^2 - 4}{x-2}$.
- $\frac{(x-2)(x+2)}{x-2} = x+2$, $x \neq 2$.

[Medium] Solve: $2^{x+1} = 16$.
- $2^{x+1} = 2^4 \to x + 1 = 4 \to x = 3$.

[Medium] Which expression is equivalent to $\sqrt{50x^5}$ for $x > 0$?
- $\sqrt{25 \cdot 2 \cdot x^4 \cdot x} = 5x^2\sqrt{2x}$.

[Medium] Solve: $|2x - 3| = 7$.
- $2x - 3 = 7 \to x = 5$, or $2x - 3 = -7 \to x = -2$.

[Medium] If $f(x) = 3x - 2$, find $f^{-1}(7)$.
- $3x - 2 = 7 \to x = 3$.

[Hard] The system $y = x^2 - 4x$ and $y = 2x - 5$ has how many solutions?
- $x^2 - 4x = 2x - 5 \to x^2 - 6x + 5 = 0$. $D = 36 - 20 = 16 > 0$ so $2$ solutions.

[Hard] The function $f(x) = 3(x+1)^2 - 8$ has a minimum at what point?
- Vertex form $a(x-h)^2 + k$: $h = -1$, $k = -8$. Minimum at $(-1, -8)$.

[Hard] Which expression is equivalent to $\frac{3}{x-1} + \frac{2}{x+1}$?
- $\frac{3(x+1) + 2(x-1)}{(x-1)(x+1)} = \frac{5x+1}{x^2-1}$.

[Hard] A population of $200$ grows at $5\%$ per year. Which function models the population after $t$ years?
- $P(t) = 200(1.05)^t$.

[Hard] The graph of a polynomial touches at $x = -2$ and crosses at $x = 4$. Minimum degree?
- Touch gives even mult (at least $2$). Cross gives odd mult (at least $1$). Minimum degree: $2 + 1 = 3$.

[Very Hard] Solve: $x^4 - 10x^2 + 9 = 0$.
- Let $u = x^2$: $u^2 - 10u + 9 = 0 \to u = 1, 9$. $x = \pm 1, \pm 3$.

[Very Hard] The function $f(x) = a(b)^x$ passes through $(0, 5)$ and $(2, 45)$. Find $a$ and $b$.
- $f(0) = a = 5$. $f(2) = 5b^2 = 45 \to b^2 = 9 \to b = 3$ ($b > 0$ for exponential).

[Very Hard] $f(x) = \sqrt{x+5} - 3$. Find $f^{-1}(x)$.
- Swap: $x = \sqrt{y+5} - 3 \to \sqrt{y+5} = x + 3 \to y + 5 = (x+3)^2 \to f^{-1}(x) = (x+3)^2 - 5$, domain $x \geq -3$.