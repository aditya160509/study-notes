# 📘 Chapter 2: Logarithmic and Exponential Functions - 9709 Pure Mathematics 2&3 (CAIE A Level Maths)

## Cambridge International AS & A Level Mathematics (9709) - Paper 3

> **Rule + fully solved examples.** Every technique shown step by step in proper LaTeX, every algebra step on its own line.

---

# PART 2: Logarithmic and Exponential Functions (Chapter 2)

**Covers:** logarithms to base $10$ and base $a$, the three laws of logarithms, solving logarithmic and exponential equations and inequalities, natural logarithms, and transforming $y = k\,a^x$ and $y = k\,x^n$ to linear form.

## 2.1 Logarithms to Base 10 and Base a

If $a^x = y$ then $x = \log_a y$. The logarithm is the **power** that the base must be raised to in order to obtain the number.

$$\log_a y = x \iff a^x = y \qquad (a > 0,\; a \neq 1,\; y > 0)$$

Special cases that follow directly from the definition:

$$\log_a a = 1 \qquad \log_a 1 = 0 \qquad a^{\log_a x} = x \qquad \log_a(a^x) = x$$

For base $10$: $\log_{10} y$ is often written $\log y$ or $\lg y$. On a calculator use the $\log$ key.

For a general base $a$: $\log_a y$ is the inverse function of $a^x$.

> ⭐ **Watch Out!** (1) $\log_a y$ only exists for $y > 0$ and $a > 0$, $a \neq 1$. Never write $\log(-3)$ or $\log_a(-5)$. (2) In log form the **index is always on its own** — $\log_a y = x$ means $a^x = y$, so $x$ is alone on one side. (3) $\log_a y$ and $a^{\log_a y}$ are inverse operations: $a^{\log_a y} = y$ cancels directly.

### Example 17 - Easy - converting between exponential and logarithmic form (coursebook Worked examples 2.1-2.6)

> **Question:** (a) Convert $10^x = 58$ to logarithmic form and solve for $x$ to 3 s.f. (b) Convert $\log_3 x = 2.5$ to exponential form and find $x$.

**Solution:**

(a) $10^x = 58 \iff x = \log_{10} 58$:

$$x = \log_{10} 58$$

$$x \approx 1.76 \quad \text{(3 s.f.)}$$

Alternatively, take logs of both sides:

$$10^x = 58$$

$$\log_{10}(10^x) = \log_{10} 58$$

$$x = \log_{10} 58 \approx 1.76 \quad\checkmark$$

(b) $\log_3 x = 2.5 \iff 3^{2.5} = x$:

$$x = 3^{2.5}$$

$$x = 3^{5/2} = \sqrt{3^5} = \sqrt{243}$$

$$x = 9\sqrt{3} \approx 15.6 \quad\checkmark$$

**What the examiner wants:** the base and index identified correctly; the index alone on one side in log form.

### Example 18 - Easy - evaluating logarithms without a calculator

> **Question:** Find (a) $\log_2 16$, (b) $\log_3\!\left(\frac{1}{9}\right)$, (c) $\log_x\!\left(\frac{x^3}{x}\right)$ where $x > 0$.

**Solution:**

(a) Write $16$ as a power of $2$: $16 = 2^4$:

$$\log_2 16 = \log_2(2^4) = 4 \quad\checkmark$$

(b) Write $\frac{1}{9}$ as a power of $3$: $\frac{1}{9} = 3^{-2}$:

$$\log_3\!\left(\frac{1}{9}\right) = \log_3(3^{-2}) = -2 \quad\checkmark$$

(c) Simplify inside the log first:

$$\frac{x^3}{x} = x^2$$

$$\log_x\!\left(\frac{x^3}{x}\right) = \log_x(x^2) = 2 \quad\checkmark$$

**What the examiner wants:** writing the argument as a power of the base, then reading off the exponent.

## 2.2 The Laws of Logarithms

For $x > 0$, $y > 0$, $a > 0$, $a \neq 1$:

$$\log_a(xy) = \log_a x + \log_a y \qquad \text{(multiplication law)}$$

$$\log_a\!\left(\frac{x}{y}\right) = \log_a x - \log_a y \qquad \text{(division law)}$$

$$\log_a(x^m) = m\log_a x \qquad \text{(power law)}$$

Useful consequences:

$$\log_a\!\left(\frac{1}{x}\right) = -\log_a x \qquad \log_a a = 1 \qquad \log_a 1 = 0$$

**Change of base:**

$$\log_a x = \frac{\log_b x}{\log_b a} \qquad \text{for any valid base } b$$

In particular, $\log_a x = \frac{\ln x}{\ln a} = \frac{\log_{10} x}{\log_{10} a}$.

> ⭐ **Watch Out!** (1) $\log_a(x + y) \neq \log_a x + \log_a y$ — the addition law is for a **product** inside the log, not a sum. (2) $\log_a x - \log_a y = \log_a\!\left(\frac{x}{y}\right)$, not $\log_a(x - y)$. (3) When using change of base, keep the same base top and bottom: $\frac{\log_{10} x}{\log_{10} a}$, not mixed bases.

### Example 19 - Medium - combining and splitting logarithms (coursebook Worked example 2.8)

> **Question:** (a) Write $\log_7 2 + \log_7 11$ as a single logarithm. (b) Write $\log_6 60 - \log_6 4$ as a single logarithm. (c) Simplify $\log_a\!\left(\frac{1}{x}\right)$.

**Solution:**

(a) Multiplication law: $\log_a x + \log_a y = \log_a(xy)$:

$$\log_7 2 + \log_7 11 = \log_7(2 \times 11)$$

$$= \log_7 22 \quad\checkmark$$

(b) Division law: $\log_a x - \log_a y = \log_a\!\left(\frac{x}{y}\right)$:

$$\log_6 60 - \log_6 4 = \log_6\!\left(\frac{60}{4}\right)$$

$$= \log_6 15 \quad\checkmark$$

(c) Power law with $m = -1$: $\log_a(x^{-1}) = -\log_a x$:

$$\log_a\!\left(\frac{1}{x}\right) = \log_a(x^{-1}) = -\log_a x \quad\checkmark$$

**What the examiner wants:** the correct law chosen for each combination; the argument written as a single number or expression.

### Example 20 - Medium - power law and simplifying $\log_a(x^m)$

> **Question:** Simplify (a) $\log_2(x^5)$, (b) $\log_5\!\left(\frac{x^3}{x^2}\right)$, (c) $3\log_a x - 2\log_a(x+1)$ as a single logarithm.

**Solution:**

(a) Power law:

$$\log_2(x^5) = 5\log_2 x \quad\checkmark$$

(b) Division law then power law, or simplify inside first:

$$\frac{x^3}{x^2} = x$$

$$\log_5\!\left(\frac{x^3}{x^2}\right) = \log_5 x \quad\checkmark$$

Alternatively:

$$\log_5(x^3) - \log_5(x^2) = 3\log_5 x - 2\log_5 x = \log_5 x$$

(c) Apply power law to each term, then division law:

$$3\log_a x = \log_a(x^3)$$

$$2\log_a(x+1) = \log_a\!\left((x+1)^2\right)$$

$$3\log_a x - 2\log_a(x+1) = \log_a(x^3) - \log_a\!\left((x+1)^2\right)$$

$$= \log_a\!\left(\frac{x^3}{(x+1)^2}\right) \quad\checkmark$$

**What the examiner wants:** the power law used to move coefficients inside as exponents before combining.

### Example 21 - Hard - change of base and arranging in order

> **Question:** Without a calculator, arrange $\log_9 3$, $\log_8 2$, $\log_{32} 2$ in ascending order.

**Solution:**

Write each as a power of its base. Use $\log_a(a^k) = k$:

$$\log_9 3: \quad 9 = 3^2, \text{ so } 3 = 9^{1/2}$$

$$\log_9 3 = \frac{1}{2}$$

$$\log_8 2: \quad 8 = 2^3, \text{ so } 2 = 8^{1/3}$$

$$\log_8 2 = \frac{1}{3}$$

$$\log_{32} 2: \quad 32 = 2^5, \text{ so } 2 = 32^{1/5}$$

$$\log_{32} 2 = \frac{1}{5}$$

Compare: $\frac{1}{5} < \frac{1}{3} < \frac{1}{2}$:

$$\log_{32} 2 < \log_8 2 < \log_9 3 \quad\checkmark$$

**What the examiner wants:** each logarithm evaluated exactly (often as a fraction) before comparing.

## 2.3 Solving Logarithmic and Exponential Equations

**Logarithmic equations:** use the laws to combine into a single log, then convert to exponential form. Or use $\log_a x = \log_a y \implies x = y$ (when both sides are single logs with the same base).

**Exponential equations:** take logs of both sides (any base, but $\ln$ or $\log_{10}$ on a calculator), then use the power law to bring the exponent down.

Key steps:

$$\log_a f(x) = k \implies f(x) = a^k$$

$$a^{f(x)} = b \implies f(x) \cdot \ln a = \ln b \implies f(x) = \frac{\ln b}{\ln a}$$

$$a^{f(x)} = a^{g(x)} \implies f(x) = g(x)$$

> ⭐ **Watch Out!** (1) After solving a log equation, check that every log argument is positive for your solutions — reject any that give $\log(0)$ or $\log(\text{negative})$. (2) When taking logs of an exponential equation, apply the log to the **entire** side, not term by term. (3) If an equation has the form $a^{2x} + b\cdot a^x + c = 0$, substitute $y = a^x$ to get a quadratic.

### Example 22 - Medium - solving a logarithmic equation (coursebook Section 2.4)

> **Question:** Solve $\log_2(x + 1) + \log_2(x - 1) = 3$.

**Solution:**

Combine using the multiplication law:

$$\log_2\!\left((x+1)(x-1)\right) = 3$$

$$\log_2(x^2 - 1) = 3$$

Convert to exponential form:

$$x^2 - 1 = 2^3$$

$$x^2 - 1 = 8$$

$$x^2 = 9$$

$$x = 3 \text{ or } x = -3$$

Check validity: need $x+1 > 0$ and $x-1 > 0$, so $x > 1$.

$$x = -3 \text{ gives } \log_2(-2) \text{ — invalid, reject}$$

$$x = 3: \quad \log_2 4 + \log_2 2 = 2 + 1 = 3 \checkmark$$

$$x = 3 \quad\checkmark$$

**What the examiner wants:** the validity check — the extraneous root $x = -3$ must be rejected with a reason.

### Example 23 - Medium - solving an exponential equation (coursebook Section 2.5)

> **Question:** Solve $3^x = 20$, giving your answer correct to 3 significant figures.

**Solution:**

Take logs of both sides (base $10$ or natural logs — either works):

$$\log_{10}(3^x) = \log_{10} 20$$

$$x\log_{10} 3 = \log_{10} 20$$

$$x = \frac{\log_{10} 20}{\log_{10} 3}$$

$$x = \frac{1.3010\ldots}{0.4771\ldots}$$

$$x \approx 2.73 \quad\text{(3 s.f.)} \quad\checkmark$$

Check with natural logs (same answer):

$$x = \frac{\ln 20}{\ln 3} \approx \frac{2.9957}{1.0986} \approx 2.73 \quad\checkmark$$

**What the examiner wants:** the power law used to bring $x$ down; the answer to the required accuracy.

### Example 24 - Hard - exponential equation requiring substitution

> **Question:** Solve $3^{2x} - 4 \cdot 3^x + 3 = 0$.

**Solution:**

Note that $3^{2x} = (3^x)^2$. Substitute $y = 3^x$ (where $y > 0$):

$$y^2 - 4y + 3 = 0$$

Factorise:

$$(y-1)(y-3) = 0$$

$$y = 1 \text{ or } y = 3$$

So:

$$3^x = 1 \implies x = 0 \quad (\text{since } 3^0 = 1)$$

$$3^x = 3 \implies x = 1$$

$$x = 0 \text{ or } x = 1 \quad\checkmark$$

Check: $3^0 - 4\cdot 3^0 + 3 = 1 - 4 + 3 = 0$... wait, $3^{2(0)} - 4\cdot 3^0 + 3 = 1 - 4 + 3 = 0 \checkmark$; $3^2 - 4\cdot 3 + 3 = 9 - 12 + 3 = 0 \checkmark$.

**What the examiner wants:** the substitution $y = 3^x$ recognised; both solutions found; the condition $y > 0$ noted (here both solutions satisfy it).

## 2.4 Natural Logarithms and Exponential Inequalities

The **natural logarithm** $\ln x$ is $\log_e x$, where $e \approx 2.71828\ldots$:

$$\ln x = \log_e x, \qquad e^{\ln x} = x \quad (x > 0), \qquad \ln(e^x) = x$$

All log laws apply with base $e$:

$$\ln(xy) = \ln x + \ln y, \quad \ln\!\left(\frac{x}{y}\right) = \ln x - \ln y, \quad \ln(x^m) = m\ln x$$

**Exponential inequalities:** if $a > 1$, then $a^x$ is increasing, so $a^x < a^y \iff x < y$. If $0 < a < 1$, the inequality reverses. Taking logs preserves the inequality direction when the log base $> 1$ (which $\ln$ and $\log_{10}$ both satisfy).

> ⭐ **Watch Out!** (1) $\ln x$ only exists for $x > 0$ — same domain restriction as any log. (2) $e^{\ln x} = x$ and $\ln(e^x) = x$ are inverse operations — use them to solve equations like $e^{2x} = 5$ or $\ln(x+1) = 3$. (3) When solving exponential inequalities by taking logs, the inequality direction stays the same if you take $\ln$ or $\log_{10}$ (both have base $> 1$).

### Example 25 - Medium - solving with natural logs (coursebook Section 2.7)

> **Question:** Solve (a) $e^{2x} = 5$, (b) $\ln(x + 1) = 3$, giving answers in exact form.

**Solution:**

(a) Take natural logs:

$$e^{2x} = 5$$

$$\ln(e^{2x}) = \ln 5$$

$$2x = \ln 5$$

$$x = \frac{1}{2}\ln 5 \quad\checkmark$$

Alternatively, $x = \frac{\ln 5}{2} = \ln\!\left(5^{1/2}\right) = \ln\!\sqrt{5}$.

(b) Convert from log to exponential form:

$$\ln(x+1) = 3 \iff x + 1 = e^3$$

$$x = e^3 - 1 \quad\checkmark$$

Check: $\ln((e^3-1)+1) = \ln(e^3) = 3 \checkmark$.

**What the examiner wants:** the inverse relationship $e^{\ln x} = x$ / $\ln(e^x) = x$ used fluently; exact form (not decimal) when asked.

### Example 26 - Medium - solving an exponential inequality

> **Question:** Solve $2^x > 10$.

**Solution:**

Take logs (base $10$ or $\ln$, base $> 1$ so inequality direction preserved):

$$2^x > 10$$

$$\ln(2^x) > \ln 10$$

$$x\ln 2 > \ln 10$$

$$x > \frac{\ln 10}{\ln 2}$$

$$x > \frac{\log_{10} 10}{\log_{10} 2} = \frac{1}{\log_{10} 2}$$

$$x > 3.32 \quad\text{(3 s.f.)} \quad\checkmark$$

Since $\frac{\ln 10}{\ln 2} = \log_2 10 \approx 3.32$.

**What the examiner wants:** the log taken on both sides correctly; the inequality direction kept (since $\ln 2 > 0$, dividing preserves direction).

## 2.5 Transforming a Relationship to Linear Form

Many non-linear relationships can be linearised by taking logs. Two standard forms in the syllabus:

**Form 1: $y = k\,a^x$** — take logs (any base):

$$\log y = \log k + x\log a$$

So plotting $\log y$ against $x$ gives a straight line with gradient $\log a$ and intercept $\log k$.

With natural logs:

$$\ln y = \ln k + x\ln a$$

Gradient $= \ln a$, intercept $= \ln k$.

**Form 2: $y = k\,x^n$** — take logs:

$$\log y = \log k + n\log x$$

So plotting $\log y$ against $\log x$ gives a straight line with gradient $n$ and intercept $\log k$.

> ⭐ **Watch Out!** (1) Identify which form you have: $y = k\,a^x$ has $x$ in the exponent (linearise with $\log y$ vs $x$); $y = k\,x^n$ has $x$ as a base (linearise with $\log y$ vs $\log x$). (2) The gradient and intercept are in terms of $\log a$ / $\log k$ — you need to exponentiate to find $a$ and $k$ themselves. (3) Read the graph carefully: the axes may be $\ln y$ vs $x$, $\log_{10} y$ vs $x$, etc. — match the base used.

### Example 27 - Medium - linearising $y = k\,a^x$ (coursebook Section 2.8)

> **Question:** The variables $x$ and $y$ satisfy $y = k\cdot a^x$ where $k$ and $a$ are constants. When $\log_{10} y$ is plotted against $x$, the graph is a straight line with gradient $0.301$ and vertical intercept $0.477$. Find $k$ and $a$.

**Solution:**

Take $\log_{10}$ of both sides:

$$\log_{10} y = \log_{10} k + x\log_{10} a$$

This is linear in $x$: $Y = mX + c$ with $Y = \log_{10} y$, $X = x$, $m = \log_{10} a$, $c = \log_{10} k$.

Given gradient $= 0.301$:

$$\log_{10} a = 0.301$$

$$a = 10^{0.301}$$

$$a \approx 2$$

Given intercept $= 0.477$:

$$\log_{10} k = 0.477$$

$$k = 10^{0.477}$$

$$k \approx 3$$

$$k \approx 3, \quad a \approx 2 \quad\checkmark$$

Check: $y = 3 \cdot 2^x$; $\log_{10} y = \log_{10} 3 + x\log_{10} 2 \approx 0.477 + 0.301x \checkmark$.

**What the examiner wants:** the linear form derived by taking logs; gradient identified as $\log_{10} a$ and intercept as $\log_{10} k$; exponentiated to find $a$ and $k$.

### Example 28 - Hard - linearising $y = k\,x^n$ (coursebook Section 2.8)

> **Question:** Experimental data for $x$ and $y$ satisfy $y = kx^n$. A plot of $\ln y$ against $\ln x$ is a straight line passing through $(0, 1.10)$ and $(2, 4.30)$. Find $k$ and $n$.

**Solution:**

Take natural logs:

$$\ln y = \ln k + n\ln x$$

So $\ln y$ vs $\ln x$ is linear with gradient $n$ and intercept $\ln k$.

Find gradient from the two points on the line:

$$n = \frac{4.30 - 1.10}{2 - 0}$$

$$n = \frac{3.20}{2}$$

$$n = 1.6$$

Find intercept — the line passes through $(\ln x, \ln y) = (0, 1.10)$, so when $\ln x = 0$:

$$\ln k = 1.10$$

$$k = e^{1.10}$$

$$k \approx 3.00$$

$$k \approx 3.00, \quad n = 1.6 \quad\checkmark$$

Check: at $\ln x = 2$: $\ln y = 1.10 + 1.6(2) = 4.30 \checkmark$.

**What the examiner wants:** the correct linear form $\ln y = \ln k + n\ln x$; gradient $= n$ read from two points on the graph; intercept exponentiated to find $k$.

### Example 29 - Hard - distinguishing the two forms

> **Question:** For each relationship, state what to plot to get a straight line and what the gradient and intercept represent: (a) $y = 5 \cdot 3^x$, (b) $y = 5x^3$.

**Solution:**

(a) $y = 5 \cdot 3^x$: $x$ is in the exponent $\implies$ take logs, plot $\log y$ vs $x$:

$$\log y = \log 5 + x\log 3$$

Plot $\log y$ (vertical) against $x$ (horizontal):

$$\text{Gradient} = \log 3, \qquad \text{Intercept} = \log 5 \quad\checkmark$$

(b) $y = 5x^3$: $x$ is a base $\implies$ take logs, plot $\log y$ vs $\log x$:

$$\log y = \log 5 + 3\log x$$

Plot $\log y$ (vertical) against $\log x$ (horizontal):

$$\text{Gradient} = 3, \qquad \text{Intercept} = \log 5 \quad\checkmark$$

**What the examiner wants:** the correct choice of axes for each form; gradient and intercept identified without expanding numerically.

### Practice Questions - Part 2

**Q6.** Write $\log_a x + 2\log_a y - \log_a z$ as a single logarithm.

**Q7.** Solve $\log_3(x - 2) = 4$.

**Q8.** Solve $5^{2x} - 6\cdot 5^x + 5 = 0$.

**Q9.** The relationship $y = k\cdot a^x$ gives a straight line when $\ln y$ is plotted against $x$, with gradient $0.693$ and intercept $1.386$. Find $k$ and $a$.

### Practice Questions - Part 2 - Full Solutions

**Solution Q6:**

$$2\log_a y = \log_a(y^2)$$

$$\log_a x + \log_a(y^2) - \log_a z = \log_a\!\left(\frac{xy^2}{z}\right) \quad\checkmark$$

**Solution Q7:**

$$\log_3(x-2) = 4 \implies x - 2 = 3^4$$

$$x - 2 = 81$$

$$x = 83 \quad\checkmark$$

Check: $\log_3(81) = \log_3(3^4) = 4 \checkmark$.

**Solution Q8:**

Let $u = 5^x$, so $5^{2x} = u^2$:

$$u^2 - 6u + 5 = 0$$

$$(u-1)(u-5) = 0$$

$$u = 1 \text{ or } u = 5$$

$$5^x = 1 \implies x = 0$$

$$5^x = 5 \implies x = 1$$

$$x = 0 \text{ or } x = 1 \quad\checkmark$$

**Solution Q9:**

$$\ln y = \ln k + x\ln a, \quad \text{gradient} = \ln a = 0.693, \quad \text{intercept} = \ln k = 1.386$$

$$\ln a = 0.693 \implies a = e^{0.693} \approx 2$$

$$\ln k = 1.386 \implies k = e^{1.386} \approx 4$$

$$k \approx 4, \quad a \approx 2 \quad\checkmark$$

---


---

# Formula Sheet (Chapter 2)

*Extracted from the chapter — see full sheet in the combined file for cross-topic formulas. This sheet covers only Chapter 2: Logs & Exponentials.*

# Quick Reference Card (Chapter 2)

*See combined file for the full quick reference. Key results for Chapter 2: Logs & Exponentials are boxed throughout the chapter above.*
