# 📘 Chapter 5: Integration - 9709 Pure Mathematics 3 (CAIE A Level Maths)

## Cambridge International AS & A Level Mathematics (9709) - Paper 3

> **Rule + fully solved examples.** Every technique shown step by step in proper LaTeX, every algebra step on its own line. 39 solved examples, 17 practice questions with full solutions, formula sheet and quick reference card at the end.

---

# 📋 Table of Contents

1. [PART 1: Standard Integrals and Reverse Differentiation](#part-1-standard-integrals-and-reverse-differentiation)
2. [PART 2: Definite Integrals and Area](#part-2-definite-integrals-and-area)
3. [PART 3: Trig Identities in Integration](#part-3-trig-identities-in-integration)
4. [PART 4: P3 Extras - Arctan, k f'(x)/f(x) and Algebraic Preparation](#part-4-p3-extras---arctan-k-fx-fx-and-algebraic-preparation)
5. [Formula Sheet](#formula-sheet)
6. [Quick Reference Card](#quick-reference-card)

---

# PART 1: Standard Integrals and Reverse Differentiation

**Covers:** what integration is, the five non-negotiable standard results, the reverse results to spot (sec, cosec, cot), and reconstructing a curve from its gradient.

## 1.1 Integration Is Reverse Differentiation

If $\frac{\mathrm{d}}{\mathrm{d}x}\big(F(x)\big) = f(x)$ then $\displaystyle \int f(x)\,\mathrm{d}x = F(x) + c$. The $+c$ is compulsory for indefinite integrals, because a constant differentiates to zero. Every formula in this chapter comes from reading the derivative table backwards.

Integration is linear:

$$ \int \big(f(x) \pm g(x)\big)\,\mathrm{d}x = \int f(x)\,\mathrm{d}x \pm \int g(x)\,\mathrm{d}x $$

$$ \int k\,f(x)\,\mathrm{d}x = k\int f(x)\,\mathrm{d}x \qquad \text{($k$ constant)} $$

> ⭐ **Watch Out!** The integral of a product is NOT the product of the integrals. Nov 2023 examiner report: assuming $\int fg = \left(\int f\right)\left(\int g\right)$ was a common wrong method. Products need identities, substitution or by parts.

### Example 1 - Easy - checking an integral by differentiating

> **Question:** Verify each of these by differentiating the right-hand side: $\int 2x\,\mathrm{d}x = x^2 + c$, $\int 3e^{3x}\,\mathrm{d}x = e^{3x} + c$, $\int 2\cos 2x\,\mathrm{d}x = \sin 2x + c$, $\int \frac{1}{x}\,\mathrm{d}x = \ln|x| + c$.

**Solution:**

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(x^2\right) = 2x \quad\Rightarrow\quad \int 2x\,\mathrm{d}x = x^2 + c$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(e^{3x}\right) = 3e^{3x} \quad\Rightarrow\quad \int 3e^{3x}\,\mathrm{d}x = e^{3x} + c$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(\sin 2x\right) = 2\cos 2x \quad\Rightarrow\quad \int 2\cos 2x\,\mathrm{d}x = \sin 2x + c$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(\ln x\right) = \frac{1}{x} \quad\Rightarrow\quad \int \frac{1}{x}\,\mathrm{d}x = \ln|x| + c \quad\checkmark$$

**What the examiner wants:** this check catches most lost marks - if differentiating your answer does not give the integrand, the integration is wrong.

### Example 2 - Easy - linearity: split, then integrate

> **Question:** Find $\int \left(3x^2 + 5e^{-2x} + 4\cos 3x\right)\mathrm{d}x$.

**Solution:**

Split into three standard pieces:

$$\int 3x^2\,\mathrm{d}x = x^3 + c$$

$$\int 5e^{-2x}\,\mathrm{d}x = 5 \cdot \left(-\frac{1}{2}\right)e^{-2x} = -\frac{5}{2}e^{-2x} + c$$

$$\int 4\cos 3x\,\mathrm{d}x = 4 \cdot \frac{1}{3}\sin 3x = \frac{4}{3}\sin 3x + c$$

$$\int \left(3x^2 + 5e^{-2x} + 4\cos 3x\right)\mathrm{d}x = x^3 - \frac{5}{2}e^{-2x} + \frac{4}{3}\sin 3x + c \quad\checkmark$$

**What the examiner wants:** splitting the integrand before integrating; one $+c$ for the whole line.

## 1.2 The Five Standard Results

The syllabus requires exactly these five families, all of the form $f(ax+b)$, with $a \neq 0$:

$$\int e^{ax+b}\,\mathrm{d}x = \frac{1}{a}e^{ax+b} + c$$

$$\int \frac{1}{ax+b}\,\mathrm{d}x = \frac{1}{a}\ln|ax+b| + c$$

$$\int \sin(ax+b)\,\mathrm{d}x = -\frac{1}{a}\cos(ax+b) + c$$

$$\int \cos(ax+b)\,\mathrm{d}x = \frac{1}{a}\sin(ax+b) + c$$

$$\int \sec^2(ax+b)\,\mathrm{d}x = \frac{1}{a}\tan(ax+b) + c$$

Why the $\frac{1}{a}$: by the chain rule $\frac{\mathrm{d}}{\mathrm{d}x}\big(f(ax+b)\big) = a\,f'(ax+b)$, so integration must divide by $a$ to cancel it. This is the **reverse chain rule**, and forgetting the $\frac{1}{a}$ is the most common error in the chapter (Nov 2023 report: candidates used the incorrect result $\int \cos(kx)\,\mathrm{d}x = \cos(kx)$ - no $\frac{1}{k}$, no sine switch).

> ⭐ **Watch Out!** (1) Sine integrates to NEGATIVE cosine. (2) The $\ln$ result needs the modulus: $\int \frac{1}{ax+b}\,\mathrm{d}x = \frac{1}{a}\ln|ax+b| + c$. (3) The constant $b$ inside the argument does nothing; only $a$ matters. (4) Radians only - degrees invalidate every trig integration.

### Example 3 - Easy - basic exponential integrals (coursebook Worked example 5.1)

> **Question:** Find (a) $\int 3e^x\,\mathrm{d}x$, (b) $\int e^{-2x}\,\mathrm{d}x$, (c) $\int e^{5x-4}\,\mathrm{d}x$.

**Solution:**

(a) The constant 3 multiplies the standard result:

$$\int 3e^x\,\mathrm{d}x = 3e^x + c$$

(b) Here $a = -2$, so divide by $-2$:

$$\int e^{-2x}\,\mathrm{d}x = \frac{1}{-2}e^{-2x} + c = -\frac{1}{2}e^{-2x} + c$$

(c) Here $a = 5$, $b = -4$; the $-4$ is irrelevant:

$$\int e^{5x-4}\,\mathrm{d}x = \frac{1}{5}e^{5x-4} + c \quad\checkmark$$

**What the examiner wants:** the $\frac{1}{a}$ on every term and a $+c$ on each answer.

> ⭐ **Watch Out!** Exponent algebra traps (June 2023 report): $e^{2x+1} \neq e^{2x} + 1$ (correct: $e^{2x+1} = e^{2x}\cdot e$), and $e^{-2x-1}$ was often misread as $e^{-2x+1}$. For $\int e^{-2x-1}\,\mathrm{d}x$ the answer is $-\frac{1}{2}e^{-2x-1} + c$.

### Example 4 - Medium - integrating $\frac{1}{ax+b}$ and stating validity (coursebook Worked example 5.4)

> **Question:** Find (a) $\int \frac{2}{x}\,\mathrm{d}x$, (b) $\int \frac{4}{2x+1}\,\mathrm{d}x$, (c) $\int \frac{6}{2-3x}\,\mathrm{d}x$, stating the values of $x$ for which each result is valid.

**Solution:**

Use $\int \frac{k}{ax+b}\,\mathrm{d}x = \frac{k}{a}\ln|ax+b| + c$.

(a) $k = 2$, $a = 1$:

$$\int \frac{2}{x}\,\mathrm{d}x = 2\ln|x| + c, \qquad \text{valid for } x \neq 0$$

(b) $k = 4$, $a = 2$:

$$\int \frac{4}{2x+1}\,\mathrm{d}x = \frac{4}{2}\ln|2x+1| + c = 2\ln|2x+1| + c, \qquad \text{valid for } 2x+1 > 0 \text{, i.e. } x > -\frac{1}{2}$$

(c) $k = 6$, $a = -3$, so $\frac{k}{a} = -2$:

$$\int \frac{6}{2-3x}\,\mathrm{d}x = \frac{6}{-3}\ln|2-3x| + c = -2\ln|2-3x| + c, \qquad \text{valid for } 2-3x > 0 \text{, i.e. } x < \frac{2}{3} \quad\checkmark$$

**What the examiner wants:** the $\frac{k}{a}$ factor (including a negative $a$), the modulus, and the validity statement - the validity carries its own mark.

### Example 5 - Medium - basic trig integrals (coursebook Worked example 5.6)

> **Question:** Find (a) $\int \sin 2x\,\mathrm{d}x$, (b) $\int \cos 3x\,\mathrm{d}x$, (c) $\int 4\sec^2\left(\frac{x}{2}\right)\mathrm{d}x$.

**Solution:**

(a) $\sin$ integrates to $-\cos$, divide by $a = 2$:

$$\int \sin 2x\,\mathrm{d}x = -\frac{1}{2}\cos 2x + c$$

(b) $\cos$ integrates to $\sin$, divide by $a = 3$:

$$\int \cos 3x\,\mathrm{d}x = \frac{1}{3}\sin 3x + c$$

(c) $\sec^2$ integrates to $\tan$, divide by $a = \frac{1}{2}$, then multiply by 4:

$$\int 4\sec^2\left(\frac{x}{2}\right)\mathrm{d}x = 4 \cdot \frac{1}{1/2}\tan\left(\frac{x}{2}\right) + c = 8\tan\left(\frac{x}{2}\right) + c \quad\checkmark$$

**What the examiner wants:** the minus sign on sine, the $\frac{1}{a}$ on every term, and correct handling of the fractional $a = \frac{1}{2}$ (dividing by $\frac{1}{2}$ multiplies by 2).

## 1.3 Reverse Results to Spot: sec, cosec, cot

These four come straight from derivatives you already know, and P3 reaches them through "show that ... hence find" chains:

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(\sec x\right) = \sec x\tan x \quad\Rightarrow\quad \int \sec x\tan x\,\mathrm{d}x = \sec x + c$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(\cot x\right) = -\cosec^2 x \quad\Rightarrow\quad \int \cosec^2 x\,\mathrm{d}x = -\cot x + c$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(\cosec x\right) = -\cosec x\cot x \quad\Rightarrow\quad \int \cosec x\cot x\,\mathrm{d}x = -\cosec x + c$$

With an $ax+b$ argument, divide by $a$ as usual: $\int \sec 2x\tan 2x\,\mathrm{d}x = \frac{1}{2}\sec 2x + c$. The June 2023 report: in a differential equation question the most straightforward route for the $x$ integral was recognising $\sec 2x\tan 2x$ as a constant multiple of the derivative of $\sec 2x$.

> ⭐ **Watch Out!** In a "show that ... hence find" question, part (b) is unmarked unless the derivative from part (a) is used to spot the integral. June 2023 report: "a 'show that' question requires full and thorough steps of working to secure full marks".

### Example 6 - Medium - "show that ... hence find" with sec x (coursebook Worked example 5.11)

> **Question:** (a) Show that if $y = \sec x$ then $\frac{\mathrm{d}y}{\mathrm{d}x} = \sec x\tan x$. (b) Hence find the exact value of $\int_0^{\frac{\pi}{4}}\left(\cos 2x + 5\sec x\tan x\right)\mathrm{d}x$.

**Solution:**

Part (a) - write $y$ as a power of $\cos x$ and use the chain rule:

$$y = \sec x = (\cos x)^{-1}$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = -(\cos x)^{-2} \cdot (-\sin x) = \frac{\sin x}{\cos^2 x}$$

$$\frac{\sin x}{\cos^2 x} = \frac{1}{\cos x} \cdot \frac{\sin x}{\cos x} = \sec x\tan x \quad\checkmark$$

Part (b) - from part (a), $\int \sec x\tan x\,\mathrm{d}x = \sec x + c$, so:

$$\int \left(\cos 2x + 5\sec x\tan x\right)\mathrm{d}x = \frac{1}{2}\sin 2x + 5\sec x$$

$$\int_0^{\frac{\pi}{4}}\left(\cos 2x + 5\sec x\tan x\right)\mathrm{d}x = \left[\frac{1}{2}\sin 2x + 5\sec x\right]_0^{\frac{\pi}{4}}$$

Substitute the upper limit $\frac{\pi}{4}$:

$$\frac{1}{2}\sin\left(\frac{\pi}{2}\right) + 5\sec\left(\frac{\pi}{4}\right) = \frac{1}{2} + 5\sqrt{2}$$

Substitute the lower limit 0:

$$\frac{1}{2}\sin 0 + 5\sec 0 = 0 + 5 = 5$$

Subtract, upper minus lower:

$$\frac{1}{2} + 5\sqrt{2} - 5 = 5\sqrt{2} - \frac{9}{2} \quad\checkmark$$

**What the examiner wants:** the "hence" link used explicitly - spotting $\sec x\tan x$ as the derivative found in (a).

## 1.4 Reconstructing a Curve from Its Gradient

Given $\frac{\mathrm{d}y}{\mathrm{d}x} = f(x)$ and a point on the curve: integrate, then use the point to pin down $c$. Given $\frac{\mathrm{d}^2y}{\mathrm{d}x^2}$: integrate twice, finding one constant per integration.

### Example 7 - Easy - curve from a first derivative

> **Question:** The gradient of a curve is given by $\frac{\mathrm{d}y}{\mathrm{d}x} = 3x^2 + 4e^{2x}$ and the curve passes through $(0, 3)$. Find the equation of the curve.

**Solution:**

Integrate:

$$y = \int \left(3x^2 + 4e^{2x}\right)\mathrm{d}x = x^3 + 2e^{2x} + c$$

Substitute $(0, 3)$, so $x = 0$, $y = 3$:

$$3 = 0 + 2e^{0} + c = 2 + c$$

$$c = 1$$

$$y = x^3 + 2e^{2x} + 1 \quad\checkmark$$

**What the examiner wants:** the integration done with $\frac{1}{a}$ on the exponential, then the point used to find $c$ exactly.

### Example 8 - Hard - curve from a second derivative

> **Question:** Given $\frac{\mathrm{d}^2y}{\mathrm{d}x^2} = 12x - 8\sin 2x$, and that at $x = 0$: $y = 3$ and $\frac{\mathrm{d}y}{\mathrm{d}x} = 5$, find $y$ in terms of $x$.

**Solution:**

Integrate once - sine integrates to negative cosine:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \int \left(12x - 8\sin 2x\right)\mathrm{d}x = 6x^2 + 4\cos 2x + c_1$$

Use $\frac{\mathrm{d}y}{\mathrm{d}x} = 5$ at $x = 0$:

$$5 = 0 + 4\cos 0 + c_1 = 4 + c_1$$

$$c_1 = 1$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = 6x^2 + 4\cos 2x + 1$$

Integrate again:

$$y = \int \left(6x^2 + 4\cos 2x + 1\right)\mathrm{d}x = 2x^3 + 2\sin 2x + x + c_2$$

Use $y = 3$ at $x = 0$:

$$3 = 0 + 0 + 0 + c_2$$

$$c_2 = 3$$

$$y = 2x^3 + 2\sin 2x + x + 3 \quad\checkmark$$

**What the examiner wants:** one constant per integration, each found from its own condition, and the sign discipline of $\int \sin 2x\,\mathrm{d}x = -\frac{1}{2}\cos 2x$ (so $\int -8\sin 2x\,\mathrm{d}x = 4\cos 2x$).

### Practice Questions - Part 1

**Q1.** Find $\int \left(3e^{2x} + 5\cos 4x - 2\sin x\right)\mathrm{d}x$.

**Q2.** Find $\int \frac{6}{3x-1}\,\mathrm{d}x$ and state the values of $x$ for which the result is valid.

**Q3.** A curve has $\frac{\mathrm{d}y}{\mathrm{d}x} = 3x^2 + 4e^{2x}$ and passes through $(0, 3)$. Find the equation of the curve. (Same structure as Example 7 - redo it from memory first.)

**Q4.** (a) Show that if $y = \cosec x$ then $\frac{\mathrm{d}y}{\mathrm{d}x} = -\cosec x\cot x$. (b) Hence find $\int 5\cosec x\cot x\,\mathrm{d}x$.

### Practice Questions - Part 1 - Full Solutions

**Solution Q1:**

Split the integrand:

$$\int 3e^{2x}\,\mathrm{d}x = \frac{3}{2}e^{2x} + c$$

$$\int 5\cos 4x\,\mathrm{d}x = \frac{5}{4}\sin 4x + c$$

$$\int -2\sin x\,\mathrm{d}x = -2(-\cos x) + c = 2\cos x + c$$

$$\int \left(3e^{2x} + 5\cos 4x - 2\sin x\right)\mathrm{d}x = \frac{3}{2}e^{2x} + \frac{5}{4}\sin 4x + 2\cos x + c \quad\checkmark$$

**Solution Q2:**

$k = 6$, $a = 3$, so $\frac{k}{a} = 2$:

$$\int \frac{6}{3x-1}\,\mathrm{d}x = 2\ln|3x-1| + c$$

Valid for $3x - 1 > 0$, i.e. $x > \frac{1}{3}$ (equivalently $x \neq \frac{1}{3}$ with the modulus). $\checkmark$

**Solution Q3:**

$$y = \int \left(3x^2 + 4e^{2x}\right)\mathrm{d}x = x^3 + 2e^{2x} + c$$

At $(0, 3)$:

$$3 = 0 + 2 + c$$

$$c = 1$$

$$y = x^3 + 2e^{2x} + 1 \quad\checkmark$$

**Solution Q4:**

Part (a) - write $y = \cosec x = (\sin x)^{-1}$ and use the chain rule:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = -(\sin x)^{-2}\cos x = -\frac{\cos x}{\sin^2 x} = -\frac{1}{\sin x}\cdot\frac{\cos x}{\sin x} = -\cosec x\cot x \quad\checkmark$$

Part (b) - from (a), $\int \cosec x\cot x\,\mathrm{d}x = -\cosec x + c$, so:

$$\int 5\cosec x\cot x\,\mathrm{d}x = -5\cosec x + c \quad\checkmark$$

---

# PART 2: Definite Integrals and Area

**Covers:** evaluating definite integrals exactly, area under curves (above, below and crossing the axis), and the trapezium rule.

## 2.1 Definite Integrals: The Rules

$$\int_a^b f(x)\,\mathrm{d}x = \left[F(x)\right]_a^b = F(b) - F(a)$$

The answer is a number; no $+c$ appears (the constants would cancel anyway). Rules:

$$\int_a^b f(x)\,\mathrm{d}x = -\int_b^a f(x)\,\mathrm{d}x$$

$$\int_a^b f(x)\,\mathrm{d}x = \int_a^c f(x)\,\mathrm{d}x + \int_c^b f(x)\,\mathrm{d}x$$

> ⭐ **Watch Out!** Always substitute the UPPER limit first, then subtract the LOWER limit (June 2023 report: candidates "using the limits for $u$ in the wrong order"). P3 nearly always demands EXACT values - a decimal loses the final accuracy mark (June 2023 report: "a decimal approximation is not an acceptable substitute").

### Example 9 - Medium - definite integral of an exponential (coursebook Worked example 5.2)

> **Question:** Evaluate $\int_1^2 9e^{3x-1}\,\mathrm{d}x$.

**Solution:**

Integrate first - the 9 divides by $a = 3$:

$$\int 9e^{3x-1}\,\mathrm{d}x = 9 \cdot \frac{1}{3}e^{3x-1} = 3e^{3x-1}$$

$$\int_1^2 9e^{3x-1}\,\mathrm{d}x = \left[3e^{3x-1}\right]_1^2$$

Upper limit $x = 2$:

$$3e^{6-1} = 3e^5$$

Lower limit $x = 1$:

$$3e^{3-1} = 3e^2$$

Subtract, upper minus lower:

$$3e^5 - 3e^2 = 3\left(e^5 - e^2\right) \quad\checkmark$$

**What the examiner wants:** the exact form with $e$; the 9 correctly divided by $a = 3$; limits in the right order.

### Example 10 - Hard - definite integral with the modulus (coursebook Worked example 5.5)

> **Question:** Find the value of $\int_2^3 \frac{6}{2-3x}\,\mathrm{d}x$.

**Solution:**

From Example 4(c):

$$\int \frac{6}{2-3x}\,\mathrm{d}x = -2\ln|2-3x|$$

$$\int_2^3 \frac{6}{2-3x}\,\mathrm{d}x = \left[-2\ln|2-3x|\right]_2^3$$

Keep the modulus through the substitution - both $2 - 3x$ values are negative:

Upper limit $x = 3$:

$$-2\ln|-7| = -2\ln 7$$

Lower limit $x = 2$:

$$-2\ln|-4| = -2\ln 4$$

Subtract, upper minus lower:

$$-2\ln 7 - \left(-2\ln 4\right) = -2\ln 7 + 2\ln 4$$

Combine the logarithms:

$$2\left(\ln 4 - \ln 7\right) = 2\ln\left(\frac{4}{7}\right) \quad\checkmark$$

**What the examiner wants:** the modulus kept until after substitution (never write $\ln(-7)$), then the logs combined into one.

### Example 11 - Medium - exact value with trig (coursebook Worked example 5.7)

> **Question:** Find the exact value of $\int_0^{\frac{\pi}{4}}\left(3 - 2\sin 2x\right)\mathrm{d}x$.

**Solution:**

Integrate term by term - $-2\sin 2x$ gives $+\cos 2x$:

$$\int \left(3 - 2\sin 2x\right)\mathrm{d}x = 3x + \cos 2x$$

$$\int_0^{\frac{\pi}{4}}\left(3 - 2\sin 2x\right)\mathrm{d}x = \left[3x + \cos 2x\right]_0^{\frac{\pi}{4}}$$

Upper limit $x = \frac{\pi}{4}$:

$$\frac{3\pi}{4} + \cos\left(\frac{\pi}{2}\right) = \frac{3\pi}{4} + 0 = \frac{3\pi}{4}$$

Lower limit $x = 0$:

$$0 + \cos 0 = 1$$

Subtract:

$$\frac{3\pi}{4} - 1 \quad\checkmark$$

**What the examiner wants:** the exact form in $\pi$; correct sign when integrating $-2\sin 2x$.

## 2.2 Area Under a Curve

$$\text{Area} = \int_a^b y\,\mathrm{d}x = \int_a^b f(x)\,\mathrm{d}x \qquad \text{(curve above the axis on } [a,b])$$

Three situations:

1. Curve entirely above the axis: the integral is the area.
2. Curve entirely below the axis: the integral is negative; area $= -\int_a^b f(x)\,\mathrm{d}x$ (take the modulus).
3. Curve crosses the axis inside $[a,b]$: split at every crossing (solve $y = 0$), take the modulus of each piece, add.

> ⭐ **Watch Out!** Integrating across an axis crossing without splitting cancels the positive and negative parts - that is not the area. Nov 2023 report: the limits $\frac{\pi}{4}$ and $\frac{3\pi}{4}$ in the $\sin x\cos 2x$ question were "a simple deduction from consideration of $\cos 2x = 0$".

### Example 12 - Medium - area above the axis (coursebook Worked example 5.3)

> **Question:** The diagram shows the curve $y = x^2 + e^{-2x}$. Find the area of the region bounded by the curve, the $x$-axis and the lines $x = 1$ and $x = 2$.

**Solution:**

Both $x^2 > 0$ and $e^{-2x} > 0$, so the curve lies above the axis on $[1, 2]$ and the area is the definite integral:

$$\text{Area} = \int_1^2 \left(x^2 + e^{-2x}\right)\mathrm{d}x$$

Integrate:

$$\int \left(x^2 + e^{-2x}\right)\mathrm{d}x = \frac{x^3}{3} - \frac{1}{2}e^{-2x}$$

Upper limit $x = 2$:

$$\frac{8}{3} - \frac{1}{2}e^{-4}$$

Lower limit $x = 1$:

$$\frac{1}{3} - \frac{1}{2}e^{-2}$$

Subtract:

$$\frac{8}{3} - \frac{1}{2}e^{-4} - \frac{1}{3} + \frac{1}{2}e^{-2}$$

Simplify:

$$\frac{7}{3} + \frac{1}{2}e^{-2} - \frac{1}{2}e^{-4} \approx 2.39 \ \text{units}^2 \quad\checkmark$$

**What the examiner wants:** recognising area as a definite integral, correct $\frac{1}{a}$ on the exponential (including the minus sign for $e^{-2x}$), exact or appropriately rounded area.

### Example 13 - Hard - area with axis crossings (ON23 P32 Q9, 5 + 4 marks)

> **Question:** The diagram shows the curve $y = \sin x\cos 2x$, for $0 \le x \le \pi$, and a maximum point $M$, where $x = a$. The shaded region between the curve and the $x$-axis is denoted by $R$. (a) Find the value of $a$ correct to 2 decimal places. (b) Find the exact area of the region $R$, giving your answer in simplified form.

**Solution:**

Part (a) - differentiate with the product rule:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \cos x\cos 2x - 2\sin x\sin 2x$$

Set $\frac{\mathrm{d}y}{\mathrm{d}x} = 0$:

$$\cos x\cos 2x - 2\sin x\sin 2x = 0$$

Use $\sin 2x = 2\sin x\cos x$:

$$\cos x\cos 2x - 2\sin x\left(2\sin x\cos x\right) = 0$$

$$\cos x\cos 2x - 4\sin^2 x\cos x = 0$$

$$\cos x\left(\cos 2x - 4\sin^2 x\right) = 0$$

The maximum is not at $\cos x = 0$ (that gives the minimum $y = -1$ at $x = \frac{\pi}{2}$), so solve the bracket:

$$\cos 2x - 4\sin^2 x = 0$$

Use $\cos 2x = 1 - 2\sin^2 x$:

$$1 - 2\sin^2 x - 4\sin^2 x = 0$$

$$1 - 6\sin^2 x = 0$$

$$\sin^2 x = \frac{1}{6}$$

$$\sin x = \frac{1}{\sqrt{6}}$$

$$x = \sin^{-1}\left(\frac{1}{\sqrt{6}}\right) \approx 0.4205$$

$$a = 0.42 \ \text{(2 dp)} \quad\checkmark$$

*(computed estimate - question text and mark allocations confirmed from the paper; the Nov 2023 examiner report discusses both parts)*

Part (b) - find the axis crossings by solving $y = 0$:

$$\sin x\cos 2x = 0$$

$$\sin x = 0 \Rightarrow x = 0, \ \pi$$

$$\cos 2x = 0 \Rightarrow 2x = \frac{\pi}{2}, \ \frac{3\pi}{2} \Rightarrow x = \frac{\pi}{4}, \ \frac{3\pi}{4}$$

The curve is above the axis on $\left[0, \frac{\pi}{4}\right]$ and $\left[\frac{3\pi}{4}, \pi\right]$, and below on $\left[\frac{\pi}{4}, \frac{3\pi}{4}\right]$. Split the integral at the crossings. First rewrite the product with the factor formula ($2\sin A\cos B = \sin(A+B) + \sin(A-B)$ with $A = 3x$, $B = x$):

$$\sin x\cos 2x = \frac{1}{2}\left(\sin 3x + \sin(-x)\right) = \frac{1}{2}\left(\sin 3x - \sin x\right)$$

Integrate:

$$\int \sin x\cos 2x\,\mathrm{d}x = \frac{1}{2}\left(-\frac{1}{3}\cos 3x + \cos x\right) = -\frac{1}{6}\cos 3x + \frac{1}{2}\cos x$$

Piece 1 - $\left[0, \frac{\pi}{4}\right]$:

$$\left[-\frac{1}{6}\cos 3x + \frac{1}{2}\cos x\right]_0^{\frac{\pi}{4}} = \left(\frac{\sqrt{2}}{12} + \frac{\sqrt{2}}{4}\right) - \left(-\frac{1}{6} + \frac{1}{2}\right)$$

$$= \frac{\sqrt{2}}{12} + \frac{3\sqrt{2}}{12} - \frac{1}{3} = \frac{4\sqrt{2}}{12} - \frac{1}{3} = \frac{\sqrt{2}}{3} - \frac{1}{3}$$

Piece 2 - $\left[\frac{\pi}{4}, \frac{3\pi}{4}\right]$ (this piece is below the axis, so its integral is negative):

$$F\left(\frac{3\pi}{4}\right) = -\frac{1}{6}\cos\left(\frac{9\pi}{4}\right) + \frac{1}{2}\cos\left(\frac{3\pi}{4}\right) = -\frac{1}{6}\left(\frac{\sqrt{2}}{2}\right) + \frac{1}{2}\left(-\frac{\sqrt{2}}{2}\right) = -\frac{\sqrt{2}}{12} - \frac{\sqrt{2}}{4} = -\frac{\sqrt{2}}{3}$$

$$F\left(\frac{\pi}{4}\right) = -\frac{1}{6}\cos\left(\frac{3\pi}{4}\right) + \frac{1}{2}\cos\left(\frac{\pi}{4}\right) = \frac{\sqrt{2}}{12} + \frac{\sqrt{2}}{4} = \frac{\sqrt{2}}{3}$$

$$\int_{\frac{\pi}{4}}^{\frac{3\pi}{4}} \sin x\cos 2x\,\mathrm{d}x = F\left(\frac{3\pi}{4}\right) - F\left(\frac{\pi}{4}\right) = -\frac{\sqrt{2}}{3} - \frac{\sqrt{2}}{3} = -\frac{2\sqrt{2}}{3}$$

Piece 3 - $\left[\frac{3\pi}{4}, \pi\right]$:

$$\left[-\frac{1}{6}\cos 3x + \frac{1}{2}\cos x\right]_{\frac{3\pi}{4}}^{\pi} = \left(\frac{1}{6} - \frac{1}{2}\right) - \left(-\frac{\sqrt{2}}{3}\right) = -\frac{1}{3} + \frac{\sqrt{2}}{3} = \frac{\sqrt{2}}{3} - \frac{1}{3}$$

Add the moduli of the three pieces:

$$\text{Area} = \left(\frac{\sqrt{2}}{3} - \frac{1}{3}\right) + \frac{2\sqrt{2}}{3} + \left(\frac{\sqrt{2}}{3} - \frac{1}{3}\right)$$

$$\text{Area} = \frac{4\sqrt{2}}{3} - \frac{2}{3} = \frac{4\sqrt{2} - 2}{3} \quad\checkmark$$

*(computed estimate - question text and mark allocations confirmed from the paper; the Nov 2023 examiner report discusses both parts)*

**What the examiner wants:** for (a) the product rule with the $-2\sin x\sin 2x$ term handled correctly (the Nov 2023 report noted the factor 2 was often lost, turning $2\sin x\sin 2x$ into $2\sin^2 x\cos x$); for (b) the split at $\cos 2x = 0$ and moduli added.

## 2.3 The Trapezium Rule

When you cannot integrate a function, estimate the definite integral with chords:

$$\int_a^b f(x)\,\mathrm{d}x \approx \frac{h}{2}\left(y_0 + y_n + 2\left(y_1 + y_2 + \cdots + y_{n-1}\right)\right), \qquad h = \frac{b-a}{n}$$

$n$ strips give $n+1$ ordinates $y_0, y_1, \ldots, y_n$ at $x = a, a+h, a+2h, \ldots, b$. Memory aid: half the strip width times (first + last + twice the sum of all the others).

Over-estimate or under-estimate (decide from a sketch - the syllabus requires this):

- Top edges of the strips ABOVE the curve (curve dips below its chords, convex like $y = x^2$): **over-estimate**.
- Top edges of the strips BELOW the curve (curve arches above its chords, concave like $y = \ln x$): **under-estimate**.

The full reason sentence earns the mark, not just the word: "over-estimate since the top edges of the strips all lie above the curve".

> ⭐ **Watch Out!** Common slips (all examiner-reported): using $n$ values instead of $n+1$; forgetting to double the middle values; using $h$ instead of $\frac{h}{2}$; rounding each $y$ to 2 dp before the final answer; unequal strips. Never use the trapezium rule when an algebraic method works, unless asked.

### Example 14 - Medium - two strips, with over/under reason (coursebook Worked example 5.14)

> **Question:** The diagram shows the curve $y = x - 2\ln x$. Use the trapezium rule with 2 intervals to estimate the value of $\int_{0.5}^{3.5}\left(x - 2\ln x\right)\mathrm{d}x$, giving your answer correct to 2 decimal places. State, with a reason, whether the trapezium rule gives an under-estimate or an over-estimate of the true value of the integral.

**Solution:**

Compute $h$:

$$h = \frac{3.5 - 0.5}{2} = \frac{3}{2} = 1.5$$

List the $x$-values and compute $y = x - 2\ln x$ at each:

$$y_0 = 0.5 - 2\ln 0.5 = 0.5 + 1.3863 = 1.8863$$

$$y_1 = 2 - 2\ln 2 = 2 - 1.3863 = 0.6137$$

$$y_2 = 3.5 - 2\ln 3.5 = 3.5 - 2.5055 = 0.9945$$

Apply the formula - first and last once, middle doubled:

$$\int_{0.5}^{3.5}\left(x - 2\ln x\right)\mathrm{d}x \approx \frac{1.5}{2}\left(1.8863 + 0.9945 + 2(0.6137)\right)$$

$$= 0.75\left(1.8863 + 0.9945 + 1.2274\right)$$

$$= 0.75 \times 4.1082 = 3.08115$$

$$3.08 \ \text{(2 dp)}$$

The curve $y = x - 2\ln x$ is convex on this interval, so the top edges of the strips lie above the curve:

$$\int_{0.5}^{3.5}\left(x - 2\ln x\right)\mathrm{d}x \approx 3.08, \qquad \text{over-estimate, since the top edges of the strips all lie above the curve} \quad\checkmark$$

**What the examiner wants:** the $\frac{h}{2}$ factor, middles doubled, 2 dp accuracy, and the full reason sentence.

### Example 15 - Medium - four strips with surd values (coursebook Worked example 5.15)

> **Question:** Use the trapezium rule with 4 intervals to estimate the value of $\int_0^4 2\sqrt{4x - x^2}\,\mathrm{d}x$, giving your answer correct to 2 decimal places. State, with a reason, whether the trapezium rule gives an under-estimate or an over-estimate of the true value of the integral.

**Solution:**

Compute $h$:

$$h = \frac{4 - 0}{4} = 1$$

List the $x$-values: $0, 1, 2, 3, 4$ and compute $y = 2\sqrt{4x - x^2}$:

$$y_0 = 2\sqrt{0} = 0$$

$$y_1 = 2\sqrt{3}$$

$$y_2 = 2\sqrt{4} = 4$$

$$y_3 = 2\sqrt{3}$$

$$y_4 = 2\sqrt{0} = 0$$

Apply the formula:

$$\int_0^4 2\sqrt{4x - x^2}\,\mathrm{d}x \approx \frac{1}{2}\left(0 + 0 + 2\left(2\sqrt{3} + 4 + 2\sqrt{3}\right)\right)$$

$$= \frac{1}{2}\left(8\sqrt{3} + 8\right) = 4 + 4\sqrt{3}$$

Convert:

$$4 + 4\sqrt{3} \approx 4 + 6.9282 = 10.9282$$

$$10.93 \ \text{(2 dp)}$$

The curve is the upper half of an ellipse-type (concave, arch) shape, so the top edges of the strips lie below the curve:

$$\int_0^4 2\sqrt{4x - x^2}\,\mathrm{d}x \approx 10.93, \qquad \text{under-estimate, since the top edges of the strips all lie below the curve} \quad\checkmark$$

**What the examiner wants:** exact surd working ($4 + 4\sqrt{3}$ seen before the decimal earns full marks), and the under-estimate reason.

### Example 16 - Hard - six strips with a trig function (coursebook Exercise 5E Q3)

> **Question:** (a) Use the trapezium rule with 6 intervals to estimate the value of $\int_{\frac{\pi}{4}}^{\frac{7\pi}{4}}\cosec\left(\frac{x}{2}\right)\mathrm{d}x$, giving your answer correct to 2 decimal places. (b) Use a sketch of the graph of $y = \cosec\left(\frac{x}{2}\right)$ for $0 \le x \le 2\pi$ to explain whether the trapezium rule gives an under-estimate or an over-estimate of the true value of the integral.

**Solution:**

Compute $h$:

$$h = \frac{\frac{7\pi}{4} - \frac{\pi}{4}}{6} = \frac{\frac{6\pi}{4}}{6} = \frac{\pi}{4}$$

List the $x$-values: $\frac{\pi}{4}, \frac{\pi}{2}, \frac{3\pi}{4}, \pi, \frac{5\pi}{4}, \frac{3\pi}{2}, \frac{7\pi}{4}$, and compute $y = \cosec\left(\frac{x}{2}\right)$ at each (work in $x/2$):

$$y_0 = \cosec\left(\frac{\pi}{8}\right) = \frac{1}{\sin\left(\frac{\pi}{8}\right)} = \frac{1}{0.3827} = 2.6131$$

$$y_1 = \cosec\left(\frac{\pi}{4}\right) = \sqrt{2} = 1.4142$$

$$y_2 = \cosec\left(\frac{3\pi}{8}\right) = \frac{1}{0.9239} = 1.0824$$

$$y_3 = \cosec\left(\frac{\pi}{2}\right) = 1$$

$$y_4 = 1.0824, \qquad y_5 = 1.4142, \qquad y_6 = 2.6131$$

Apply the formula:

$$\int_{\frac{\pi}{4}}^{\frac{7\pi}{4}}\cosec\left(\frac{x}{2}\right)\mathrm{d}x \approx \frac{\pi}{8}\left(2.6131 + 2.6131 + 2\left(1.4142 + 1.0824 + 1 + 1.0824 + 1.4142\right)\right)$$

$$= \frac{\pi}{8}\left(5.2262 + 2(5.9932)\right)$$

$$= \frac{\pi}{8}\left(5.2262 + 11.9864\right) = \frac{\pi}{8} \times 17.2126$$

$$= 6.7593 \approx 6.76 \ \text{(2 dp)}$$

From the sketch, the curve is convex on each side of its minimum at $x = \pi$, so the top edges of the strips lie above the curve:

$$\int_{\frac{\pi}{4}}^{\frac{7\pi}{4}}\cosec\left(\frac{x}{2}\right)\mathrm{d}x \approx 6.76, \qquad \text{over-estimate, since the top edges of the strips all lie above the curve} \quad\checkmark$$

**What the examiner wants:** care with the $\frac{x}{2}$ arguments (a common source of slips - remember $\cosec$ is $1/\sin$, so the values are all greater than or equal to 1), and the sketch used to justify the over-estimate. (Answer 6.76 verified from the coursebook answer key.)

### Example 17 - Hard - three strips with an exponential-times-cosine curve (coursebook Exercise 5E Q4)

> **Question:** The diagram shows the curve $y = e^x\cos x$ for $0 \le x \le \frac{\pi}{2}$. Use the trapezium rule with 3 intervals to estimate the value of $\int_0^{\frac{\pi}{2}} e^x\cos x\,\mathrm{d}x$, giving your answer correct to 2 decimal places. State, with a reason, whether the trapezium rule gives an under-estimate or an over-estimate of the true value of the integral.

**Solution:**

Compute $h$:

$$h = \frac{\frac{\pi}{2} - 0}{3} = \frac{\pi}{6}$$

List the $x$-values: $0, \frac{\pi}{6}, \frac{\pi}{3}, \frac{\pi}{2}$ and compute $y = e^x\cos x$ at each:

$$y_0 = e^0\cos 0 = 1$$

$$y_1 = e^{\frac{\pi}{6}}\cos\left(\frac{\pi}{6}\right) = 1.6881 \times 0.8660 = 1.4619$$

$$y_2 = e^{\frac{\pi}{3}}\cos\left(\frac{\pi}{3}\right) = 2.8497 \times 0.5 = 1.4248$$

$$y_3 = e^{\frac{\pi}{2}}\cos\left(\frac{\pi}{2}\right) = 4.8105 \times 0 = 0$$

Apply the formula:

$$\int_0^{\frac{\pi}{2}} e^x\cos x\,\mathrm{d}x \approx \frac{\pi}{12}\left(1 + 0 + 2\left(1.4619 + 1.4248\right)\right)$$

$$= \frac{\pi}{12}\left(1 + 2(2.8867)\right) = \frac{\pi}{12}\left(1 + 5.7734\right) = \frac{\pi}{12} \times 6.7734$$

$$= 1.7733 \approx 1.77 \ \text{(2 dp)}$$

The curve is concave on this interval (its second derivative is $-2e^x\sin x < 0$ for $0 < x < \frac{\pi}{2}$), so the top edges of the strips lie below the curve:

$$\int_0^{\frac{\pi}{2}} e^x\cos x\,\mathrm{d}x \approx 1.77, \qquad \text{under-estimate, since the top edges of the strips all lie below the curve} \quad\checkmark$$

**What the examiner wants:** a tidy table of $y$-values kept to enough decimal places for the 2 dp answer to be safe, and the reason stated in full. (Answer verified from the coursebook answer key.)

### Practice Questions - Part 2

**Q1.** Find the exact value of $\int_1^3 \left(2x + e^{2x-1}\right)\mathrm{d}x$.

**Q2.** Find the exact value of $\int_0^{\frac{\pi}{3}}\left(3\cos 2x - \sin x\right)\mathrm{d}x$.

**Q3.** Find the exact area of the region bounded by the curve $y = \sin 2x$ and the $x$-axis between $x = 0$ and $x = \pi$. (The curve crosses the axis inside the interval.)

**Q4.** Use the trapezium rule with 4 intervals to estimate $\int_0^2 e^{x^2}\,\mathrm{d}x$ correct to 2 decimal places, and state, with a reason, whether it is an over-estimate or an under-estimate.

### Practice Questions - Part 2 - Full Solutions

**Solution Q1:**

$$\int \left(2x + e^{2x-1}\right)\mathrm{d}x = x^2 + \frac{1}{2}e^{2x-1}$$

$$\int_1^3 \left(2x + e^{2x-1}\right)\mathrm{d}x = \left[x^2 + \frac{1}{2}e^{2x-1}\right]_1^3$$

Upper limit $x = 3$:

$$9 + \frac{1}{2}e^5$$

Lower limit $x = 1$:

$$1 + \frac{1}{2}e^{1}$$

Subtract:

$$9 + \frac{1}{2}e^5 - 1 - \frac{1}{2}e = 8 + \frac{1}{2}\left(e^5 - e\right) \quad\checkmark$$

**Solution Q2:**

$$\int \left(3\cos 2x - \sin x\right)\mathrm{d}x = \frac{3}{2}\sin 2x + \cos x$$

$$\int_0^{\frac{\pi}{3}}\left(3\cos 2x - \sin x\right)\mathrm{d}x = \left[\frac{3}{2}\sin 2x + \cos x\right]_0^{\frac{\pi}{3}}$$

Upper limit $x = \frac{\pi}{3}$:

$$\frac{3}{2}\sin\left(\frac{2\pi}{3}\right) + \cos\left(\frac{\pi}{3}\right) = \frac{3}{2}\left(\frac{\sqrt{3}}{2}\right) + \frac{1}{2} = \frac{3\sqrt{3}}{4} + \frac{1}{2}$$

Lower limit $x = 0$:

$$\frac{3}{2}\sin 0 + \cos 0 = 1$$

Subtract:

$$\frac{3\sqrt{3}}{4} + \frac{1}{2} - 1 = \frac{3\sqrt{3}}{4} - \frac{1}{2} \quad\checkmark$$

**Solution Q3:**

Find the crossings:

$$\sin 2x = 0 \Rightarrow 2x = 0, \pi, 2\pi \Rightarrow x = 0, \frac{\pi}{2}, \pi$$

The curve is above the axis on $\left[0, \frac{\pi}{2}\right]$ and below on $\left[\frac{\pi}{2}, \pi\right]$. Split and take moduli:

$$\text{Area} = \int_0^{\frac{\pi}{2}} \sin 2x\,\mathrm{d}x - \int_{\frac{\pi}{2}}^{\pi} \sin 2x\,\mathrm{d}x$$

First piece:

$$\int_0^{\frac{\pi}{2}} \sin 2x\,\mathrm{d}x = \left[-\frac{1}{2}\cos 2x\right]_0^{\frac{\pi}{2}} = -\frac{1}{2}\cos\pi + \frac{1}{2}\cos 0 = -\frac{1}{2}(-1) + \frac{1}{2} = 1$$

Second piece:

$$\int_{\frac{\pi}{2}}^{\pi} \sin 2x\,\mathrm{d}x = \left[-\frac{1}{2}\cos 2x\right]_{\frac{\pi}{2}}^{\pi} = -\frac{1}{2}\cos 2\pi + \frac{1}{2}\cos\pi = -\frac{1}{2}(1) + \frac{1}{2}(-1) = -1$$

$$\text{Area} = 1 - (-1) = 2 \ \text{units}^2 \quad\checkmark$$

**Solution Q4:**

$$h = \frac{2 - 0}{4} = 0.5$$

$x$-values: $0, 0.5, 1, 1.5, 2$, and $y = e^{x^2}$:

$$y_0 = e^0 = 1$$

$$y_1 = e^{0.25} = 1.2840$$

$$y_2 = e^1 = 2.7183$$

$$y_3 = e^{2.25} = 9.4877$$

$$y_4 = e^4 = 54.5982$$

Apply the formula:

$$\int_0^2 e^{x^2}\,\mathrm{d}x \approx \frac{0.5}{2}\left(1 + 54.5982 + 2\left(1.2840 + 2.7183 + 9.4877\right)\right)$$

$$= 0.25\left(55.5982 + 2(13.4900)\right)$$

$$= 0.25\left(55.5982 + 26.9800\right) = 0.25 \times 82.5782 = 20.6446$$

$$20.64 \ \text{(2 dp)}$$

The curve $y = e^{x^2}$ is convex on $[0, 2]$ (its second derivative $e^{x^2}(2 + 4x^2) > 0$), so the top edges of the strips lie above the curve:

$$\int_0^2 e^{x^2}\,\mathrm{d}x \approx 20.64, \qquad \text{over-estimate, since the top edges of the strips all lie above the curve} \quad\checkmark$$

---

# PART 3: Trig Identities in Integration

**Covers:** double angle identities for $\sin^2$, $\cos^2$, $\tan^2$; higher powers; the factor formulae; expanding squares; and "show that ... hence" identity chains.

## 3.1 Squares of Trig Functions: Double Angle First

There is no standard integral for $\sin^2 x$ or $\cos^2 x$ as they stand - rewrite first:

$$\sin^2(ax) = \frac{1}{2}\left(1 - \cos(2ax)\right)$$

$$\cos^2(ax) = \frac{1}{2}\left(1 + \cos(2ax)\right)$$

$$\tan^2 x = \sec^2 x - 1$$

Two coefficients come from different places: the $\frac{1}{2}$ from the identity, then the $\frac{1}{2a}$ from integrating the $\cos(2ax)$ term. The June 2023 report noted candidates "often obtained an integral of the correct form, albeit with some errors in the coefficients" - the coefficients are the trap.

> ⭐ **Watch Out!** Never treat $\int \tan^2 x\,\mathrm{d}x$ as a standard result. It is $\int (\sec^2 x - 1)\,\mathrm{d}x = \tan x - x + c$.

### Example 18 - Easy - squares with the double angle formula (coursebook Worked example 5.8)

> **Question:** Find (a) $\int \sin^2 x\,\mathrm{d}x$, (b) $\int 3\cos^2 2x\,\mathrm{d}x$.

**Solution:**

(a) Replace $\sin^2 x = \frac{1}{2}(1 - \cos 2x)$:

$$\int \sin^2 x\,\mathrm{d}x = \int \frac{1}{2}\left(1 - \cos 2x\right)\mathrm{d}x$$

$$= \frac{1}{2}\int 1\,\mathrm{d}x - \frac{1}{2}\int \cos 2x\,\mathrm{d}x$$

$$= \frac{x}{2} - \frac{1}{2}\left(\frac{1}{2}\sin 2x\right) + c = \frac{x}{2} - \frac{\sin 2x}{4} + c$$

(b) Replace $\cos^2 2x = \frac{1}{2}(1 + \cos 4x)$, then multiply by 3:

$$\int 3\cos^2 2x\,\mathrm{d}x = \frac{3}{2}\int \left(1 + \cos 4x\right)\mathrm{d}x$$

$$= \frac{3}{2}\left(x + \frac{1}{4}\sin 4x\right) + c = \frac{3x}{2} + \frac{3\sin 4x}{8} + c \quad\checkmark$$

**What the examiner wants:** the identity actually written down (method marks), and the $\frac{1}{4}$ when integrating $\cos 4x$.

### Example 19 - Medium - definite integral of $\tan^2 x$ (coursebook Worked example 5.10)

> **Question:** Find the exact value of $\int_0^{\frac{\pi}{4}} 5\tan^2 x\,\mathrm{d}x$.

**Solution:**

Replace $\tan^2 x = \sec^2 x - 1$:

$$\int 5\tan^2 x\,\mathrm{d}x = 5\int \left(\sec^2 x - 1\right)\mathrm{d}x = 5\left(\tan x - x\right)$$

$$\int_0^{\frac{\pi}{4}} 5\tan^2 x\,\mathrm{d}x = \left[5\tan x - 5x\right]_0^{\frac{\pi}{4}}$$

Upper limit $x = \frac{\pi}{4}$:

$$5\tan\left(\frac{\pi}{4}\right) - 5\left(\frac{\pi}{4}\right) = 5(1) - \frac{5\pi}{4} = 5 - \frac{5\pi}{4}$$

Lower limit $x = 0$:

$$5\tan 0 - 0 = 0$$

Subtract:

$$5 - \frac{5\pi}{4} \quad\checkmark$$

**What the examiner wants:** converting $\tan^2 x$ to $\sec^2 x - 1$ and leaving the answer exact.

### Example 20 - Medium - real paper: $\cos^2 5x$ (MJ25 P33 Q3, 4 marks)

> **Question:** Find the exact value of $\int_{\frac{\pi}{5}}^{\frac{\pi}{4}} 3\cos^2 5x\,\mathrm{d}x$.

**Solution:**

Replace $\cos^2 5x = \frac{1}{2}(1 + \cos 10x)$:

$$\int 3\cos^2 5x\,\mathrm{d}x = \frac{3}{2}\int \left(1 + \cos 10x\right)\mathrm{d}x$$

$$= \frac{3}{2}\left(x + \frac{1}{10}\sin 10x\right)$$

$$\int_{\frac{\pi}{5}}^{\frac{\pi}{4}} 3\cos^2 5x\,\mathrm{d}x = \left[\frac{3x}{2} + \frac{3}{20}\sin 10x\right]_{\frac{\pi}{5}}^{\frac{\pi}{4}}$$

Upper limit $x = \frac{\pi}{4}$:

$$\frac{3}{2}\left(\frac{\pi}{4}\right) + \frac{3}{20}\sin\left(\frac{10\pi}{4}\right) = \frac{3\pi}{8} + \frac{3}{20}\sin\left(\frac{5\pi}{2}\right) = \frac{3\pi}{8} + \frac{3}{20}(1) = \frac{3\pi}{8} + \frac{3}{20}$$

Lower limit $x = \frac{\pi}{5}$:

$$\frac{3}{2}\left(\frac{\pi}{5}\right) + \frac{3}{20}\sin(2\pi) = \frac{3\pi}{10} + 0 = \frac{3\pi}{10}$$

Subtract:

$$\frac{3\pi}{8} - \frac{3\pi}{10} + \frac{3}{20} = \frac{15\pi - 12\pi}{40} + \frac{3}{20} = \frac{3\pi}{40} + \frac{3}{20} \quad\checkmark$$

*(computed estimate - question text confirmed from the paper; no local mark scheme)*

**What the examiner wants:** the double angle identity used to reach $\frac{1}{10}\sin 10x$ (a classic $\frac{1}{2a}$ trap), then exact evaluation with the limits in the correct order.

## 3.2 Higher Powers: Apply the Identity Twice

$$\sin^4 x = \left(\sin^2 x\right)^2 = \left(\frac{1}{2}\left(1 - \cos 2x\right)\right)^2 = \frac{1}{4}\left(1 - 2\cos 2x + \cos^2 2x\right)$$

Then apply the identity again to $\cos^2 2x$.

### Example 21 - Hard - $\sin^4 x$ (coursebook Worked example 5.9)

> **Question:** Find $\int \sin^4 x\,\mathrm{d}x$.

**Solution:**

Write $\sin^4 x$ as a square of $\sin^2 x$:

$$\sin^4 x = \left(\sin^2 x\right)^2 = \left(\frac{1}{2}\left(1 - \cos 2x\right)\right)^2$$

$$= \frac{1}{4}\left(1 - 2\cos 2x + \cos^2 2x\right)$$

Apply the identity to $\cos^2 2x$:

$$\cos^2 2x = \frac{1}{2}\left(1 + \cos 4x\right)$$

$$\sin^4 x = \frac{1}{4}\left(1 - 2\cos 2x + \frac{1}{2}\left(1 + \cos 4x\right)\right)$$

$$= \frac{1}{4} - \frac{1}{2}\cos 2x + \frac{1}{8} + \frac{1}{8}\cos 4x$$

Collect the constants:

$$\sin^4 x = \frac{3}{8} - \frac{1}{2}\cos 2x + \frac{1}{8}\cos 4x$$

Integrate term by term:

$$\int \sin^4 x\,\mathrm{d}x = \frac{3x}{8} - \frac{1}{2}\left(\frac{1}{2}\sin 2x\right) + \frac{1}{8}\left(\frac{1}{4}\sin 4x\right) + c$$

$$= \frac{3x}{8} - \frac{\sin 2x}{4} + \frac{\sin 4x}{32} + c \quad\checkmark$$

**What the examiner wants:** the double angle formula applied twice, then each term integrated with the correct $\frac{1}{a}$ (the $\frac{1}{2}$ and $\frac{1}{8}$ coefficients become $\frac{1}{4}$ and $\frac{1}{32}$ after dividing by the arguments 2 and 4).

## 3.3 Products of Trig Functions: The Factor Formulae

A product integrates directly only after conversion to a sum:

$$2\sin A\sin B = \cos(A-B) - \cos(A+B)$$

$$2\cos A\cos B = \cos(A-B) + \cos(A+B)$$

$$2\sin A\cos B = \sin(A+B) + \sin(A-B)$$

Take $A$ as the larger argument. Watch negative angles: $\cos(-x) = \cos x$, $\sin(-x) = -\sin x$, so $\sin x\cos 2x = \frac{1}{2}(\sin 3x - \sin x)$.

### Example 22 - Medium - product of sines (coursebook Worked example 5.13)

> **Question:** (a) Show that $\cos 2x - \cos 4x \equiv 2\sin 3x\sin x$. (b) Hence show that $\int_0^{\frac{\pi}{4}}\sin 3x\sin x\,\mathrm{d}x = \frac{1}{4}$.

**Solution:**

Part (a) - use $2\sin A\sin B = \cos(A-B) - \cos(A+B)$ with $A = 3x$, $B = x$:

$$2\sin 3x\sin x = \cos(3x - x) - \cos(3x + x)$$

$$= \cos 2x - \cos 4x \quad\checkmark$$

Part (b) - from (a):

$$\sin 3x\sin x = \frac{1}{2}\left(\cos 2x - \cos 4x\right)$$

$$\int_0^{\frac{\pi}{4}}\sin 3x\sin x\,\mathrm{d}x = \frac{1}{2}\int_0^{\frac{\pi}{4}}\left(\cos 2x - \cos 4x\right)\mathrm{d}x$$

$$= \frac{1}{2}\left[\frac{1}{2}\sin 2x - \frac{1}{4}\sin 4x\right]_0^{\frac{\pi}{4}}$$

Upper limit $x = \frac{\pi}{4}$:

$$\frac{1}{2}\left(\frac{1}{2}\sin\left(\frac{\pi}{2}\right) - \frac{1}{4}\sin\pi\right) = \frac{1}{2}\left(\frac{1}{2}(1) - \frac{1}{4}(0)\right) = \frac{1}{4}$$

Lower limit $x = 0$:

$$\frac{1}{2}\left(0 - 0\right) = 0$$

Subtract:

$$\frac{1}{4} - 0 = \frac{1}{4} \quad\checkmark$$

**What the examiner wants:** the factor formula applied the right way round, and careful coefficient work ($\frac{1}{2}$ outside, $\frac{1}{2}$ and $\frac{1}{4}$ inside).

## 3.4 Expand a Square, Then Integrate

Squares of sums like $(a\sin x + b\cos x)^2$ expand into $\sin^2$, $\cos^2$ and $2\sin x\cos x$ terms, each handled by the identities above (and $2\sin x\cos x = \sin 2x$).

### Example 23 - Hard - expand, then integrate (coursebook Review exercise 5 Q11, from Cambridge P21 Q7 June 2012, 5 + 4 marks)

> **Question:** (i) Show that $(2\sin x + \cos x)^2$ can be written in the form $\frac{5}{2} + 2\sin 2x - \frac{3}{2}\cos 2x$. (ii) Hence find the exact value of $\int_0^{\frac{\pi}{4}}\left(2\sin x + \cos x\right)^2\mathrm{d}x$.

**Solution:**

Part (i) - expand the square:

$$(2\sin x + \cos x)^2 = 4\sin^2 x + 4\sin x\cos x + \cos^2 x$$

Replace $\sin^2 x = \frac{1}{2}(1 - \cos 2x)$, $\cos^2 x = \frac{1}{2}(1 + \cos 2x)$ and $4\sin x\cos x = 2\sin 2x$:

$$= 4\left(\frac{1}{2}\left(1 - \cos 2x\right)\right) + 2\sin 2x + \frac{1}{2}\left(1 + \cos 2x\right)$$

$$= 2 - 2\cos 2x + 2\sin 2x + \frac{1}{2} + \frac{1}{2}\cos 2x$$

Collect like terms:

$$= \frac{5}{2} + 2\sin 2x - \frac{3}{2}\cos 2x \quad\checkmark$$

Part (ii) - integrate:

$$\int_0^{\frac{\pi}{4}}\left(2\sin x + \cos x\right)^2\mathrm{d}x = \int_0^{\frac{\pi}{4}}\left(\frac{5}{2} + 2\sin 2x - \frac{3}{2}\cos 2x\right)\mathrm{d}x$$

$$= \left[\frac{5x}{2} - \cos 2x - \frac{3}{4}\sin 2x\right]_0^{\frac{\pi}{4}}$$

Upper limit $x = \frac{\pi}{4}$:

$$\frac{5}{2}\left(\frac{\pi}{4}\right) - \cos\left(\frac{\pi}{2}\right) - \frac{3}{4}\sin\left(\frac{\pi}{2}\right) = \frac{5\pi}{8} - 0 - \frac{3}{4} = \frac{5\pi}{8} - \frac{3}{4}$$

Lower limit $x = 0$:

$$0 - \cos 0 - 0 = -1$$

Subtract:

$$\frac{5\pi}{8} - \frac{3}{4} + 1 = \frac{5\pi}{8} + \frac{1}{4} \quad\checkmark$$

**What the examiner wants:** both double angle identities and the sine double angle used in one expansion, then exact evaluation. (Answer verified from the coursebook answer key.)

## 3.5 Identity Chains: "Show That ... Hence"

These questions build an identity step by step, and each step feeds the next. Part (i) of the chain is usually a reverse differentiation, part (ii) a definite integral, part (iii) another identity.

### Example 24 - Hard - $\cosec 2x\tan x$ identity chain (coursebook Worked example 5.12)

> **Question:** (a) Prove that $2\cosec 2x\tan x \equiv \sec^2 x$. (b) Hence find the exact value of $\int_{-\frac{\pi}{3}}^{\frac{\pi}{3}}\left(5 + \cosec 2x\tan x\right)\mathrm{d}x$.

**Solution:**

Part (a) - write everything in terms of sine and cosine:

$$2\cosec 2x\tan x = 2 \cdot \frac{1}{\sin 2x} \cdot \frac{\sin x}{\cos x}$$

Use $\sin 2x = 2\sin x\cos x$:

$$= \frac{2\sin x}{2\sin x\cos x \cdot \cos x} = \frac{1}{\cos^2 x} = \sec^2 x \quad\checkmark$$

Part (b) - from (a):

$$\cosec 2x\tan x = \frac{1}{2}\sec^2 x$$

$$\int_{-\frac{\pi}{3}}^{\frac{\pi}{3}}\left(5 + \cosec 2x\tan x\right)\mathrm{d}x = \int_{-\frac{\pi}{3}}^{\frac{\pi}{3}}\left(5 + \frac{1}{2}\sec^2 x\right)\mathrm{d}x$$

$$= \left[5x + \frac{1}{2}\tan x\right]_{-\frac{\pi}{3}}^{\frac{\pi}{3}}$$

Upper limit $x = \frac{\pi}{3}$:

$$5\left(\frac{\pi}{3}\right) + \frac{1}{2}\tan\left(\frac{\pi}{3}\right) = \frac{5\pi}{3} + \frac{1}{2}\sqrt{3} = \frac{5\pi}{3} + \frac{\sqrt{3}}{2}$$

Lower limit $x = -\frac{\pi}{3}$:

$$5\left(-\frac{\pi}{3}\right) + \frac{1}{2}\tan\left(-\frac{\pi}{3}\right) = -\frac{5\pi}{3} - \frac{\sqrt{3}}{2}$$

Subtract:

$$\frac{5\pi}{3} + \frac{\sqrt{3}}{2} + \frac{5\pi}{3} + \frac{\sqrt{3}}{2} = \frac{10\pi}{3} + \sqrt{3} \quad\checkmark$$

**What the examiner wants:** the trig proof done cleanly, the $\frac{1}{2}$ factor from (a) not lost, and exact evaluation using $\tan\left(\frac{\pi}{3}\right) = \sqrt{3}$.

### Example 25 - Hard - the full cot chain (coursebook Review exercise 5 Q12, from Cambridge P21 Q8 June 2010, 3 + 4 + 3 marks)

> **Question:** (i) By differentiating, show that if $y = \cot x$ then $\frac{\mathrm{d}y}{\mathrm{d}x} = -\cosec^2 x$. (ii) By expressing $\cot^2 x$ in terms of $\cosec^2 x$ and using the result of part (i), show that $\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\cot^2 x\,\mathrm{d}x = 1 - \frac{\pi}{4}$. (iii) Express $\cos 2x$ in terms of $\sin^2 x$ and hence show that $\frac{1}{1 - \cos 2x}$ can be expressed as $\frac{1}{2}\cosec^2 x$. Hence find $\int \frac{1}{1 - \cos 2x}\,\mathrm{d}x$.

**Solution:**

Part (i) - write $y = \frac{\cos x}{\sin x}$ and use the quotient rule:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{(-\sin x)(\sin x) - (\cos x)(\cos x)}{\sin^2 x}$$

$$= \frac{-\sin^2 x - \cos^2 x}{\sin^2 x} = -\frac{1}{\sin^2 x} = -\cosec^2 x \quad\checkmark$$

Part (ii) - use $\cot^2 x = \cosec^2 x - 1$:

$$\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\cot^2 x\,\mathrm{d}x = \int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\left(\cosec^2 x - 1\right)\mathrm{d}x$$

From (i), $\int \cosec^2 x\,\mathrm{d}x = -\cot x + c$:

$$= \left[-\cot x - x\right]_{\frac{\pi}{4}}^{\frac{\pi}{2}}$$

Upper limit $x = \frac{\pi}{2}$:

$$-\cot\left(\frac{\pi}{2}\right) - \frac{\pi}{2} = 0 - \frac{\pi}{2} = -\frac{\pi}{2}$$

Lower limit $x = \frac{\pi}{4}$:

$$-\cot\left(\frac{\pi}{4}\right) - \frac{\pi}{4} = -1 - \frac{\pi}{4}$$

Subtract:

$$-\frac{\pi}{2} + 1 + \frac{\pi}{4} = 1 - \frac{\pi}{4} \quad\checkmark$$

Part (iii) - express $\cos 2x$ in terms of $\sin^2 x$:

$$\cos 2x = 1 - 2\sin^2 x$$

$$1 - \cos 2x = 2\sin^2 x$$

$$\frac{1}{1 - \cos 2x} = \frac{1}{2\sin^2 x} = \frac{1}{2}\cosec^2 x \quad\checkmark$$

Integrate:

$$\int \frac{1}{1 - \cos 2x}\,\mathrm{d}x = \frac{1}{2}\int \cosec^2 x\,\mathrm{d}x = -\frac{1}{2}\cot x + c \quad\checkmark$$

**What the examiner wants:** every part linked through part (i) (a pure reverse-differentiation chain) and the sign discipline of $\int \cosec^2 x\,\mathrm{d}x = -\cot x + c$. (Answers verified from the coursebook answer key.)

### Practice Questions - Part 3

**Q1.** Find the exact value of $\int_0^{\frac{\pi}{6}}\cos^2 3x\,\mathrm{d}x$.

**Q2.** Find $\int \sin 3x\cos x\,\mathrm{d}x$.

**Q3.** Find the exact value of $\int_0^{\frac{\pi}{4}}\tan^2 x\,\mathrm{d}x$.

**Q4.** (i) Show that $(\sin x - \cos x)^2 \equiv 1 - \sin 2x$. (ii) Hence find the exact value of $\int_0^{\frac{\pi}{4}}(\sin x - \cos x)^2\mathrm{d}x$.

### Practice Questions - Part 3 - Full Solutions

**Solution Q1:**

Replace $\cos^2 3x = \frac{1}{2}(1 + \cos 6x)$:

$$\int \cos^2 3x\,\mathrm{d}x = \frac{1}{2}\int \left(1 + \cos 6x\right)\mathrm{d}x = \frac{x}{2} + \frac{1}{12}\sin 6x$$

$$\int_0^{\frac{\pi}{6}}\cos^2 3x\,\mathrm{d}x = \left[\frac{x}{2} + \frac{1}{12}\sin 6x\right]_0^{\frac{\pi}{6}}$$

Upper limit $x = \frac{\pi}{6}$:

$$\frac{1}{2}\left(\frac{\pi}{6}\right) + \frac{1}{12}\sin\pi = \frac{\pi}{12} + 0 = \frac{\pi}{12}$$

Lower limit $x = 0$:

$$0 + 0 = 0$$

$$\int_0^{\frac{\pi}{6}}\cos^2 3x\,\mathrm{d}x = \frac{\pi}{12} \quad\checkmark$$

**Solution Q2:**

Use $2\sin A\cos B = \sin(A+B) + \sin(A-B)$ with $A = 3x$, $B = x$:

$$\sin 3x\cos x = \frac{1}{2}\left(\sin 4x + \sin 2x\right)$$

$$\int \sin 3x\cos x\,\mathrm{d}x = \frac{1}{2}\left(-\frac{1}{4}\cos 4x - \frac{1}{2}\cos 2x\right) + c$$

$$= -\frac{1}{8}\cos 4x - \frac{1}{4}\cos 2x + c \quad\checkmark$$

**Solution Q3:**

$$\tan^2 x = \sec^2 x - 1$$

$$\int_0^{\frac{\pi}{4}}\tan^2 x\,\mathrm{d}x = \left[\tan x - x\right]_0^{\frac{\pi}{4}}$$

$$= \tan\left(\frac{\pi}{4}\right) - \frac{\pi}{4} - (0 - 0) = 1 - \frac{\pi}{4} \quad\checkmark$$

**Solution Q4:**

Part (i) - expand:

$$(\sin x - \cos x)^2 = \sin^2 x - 2\sin x\cos x + \cos^2 x$$

$$= \left(\sin^2 x + \cos^2 x\right) - \sin 2x = 1 - \sin 2x \quad\checkmark$$

Part (ii) - integrate:

$$\int_0^{\frac{\pi}{4}}(\sin x - \cos x)^2\mathrm{d}x = \int_0^{\frac{\pi}{4}}\left(1 - \sin 2x\right)\mathrm{d}x$$

$$= \left[x + \frac{1}{2}\cos 2x\right]_0^{\frac{\pi}{4}}$$

Upper limit $x = \frac{\pi}{4}$:

$$\frac{\pi}{4} + \frac{1}{2}\cos\left(\frac{\pi}{2}\right) = \frac{\pi}{4} + 0 = \frac{\pi}{4}$$

Lower limit $x = 0$:

$$0 + \frac{1}{2}\cos 0 = \frac{1}{2}$$

Subtract:

$$\frac{\pi}{4} - \frac{1}{2} \quad\checkmark$$

---

# PART 4: P3 Extras - Arctan, k f'(x)/f(x) and Algebraic Preparation

**Covers:** the genuinely new P3 integral $\frac{1}{x^2+a^2}$, the log rule $\frac{k f'(x)}{f(x)}$, preparing ugly integrands (divide, split, decompose), the repeated-factor trap, Chapter 8 closers, and given substitutions.

## 4.1 The Arctan Integral: $\frac{1}{x^2 + a^2}$

Differentiating $\tan^{-1}\left(\frac{x}{a}\right)$ gives:

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(\tan^{-1}\left(\frac{x}{a}\right)\right) = \frac{1/a}{1 + \frac{x^2}{a^2}} = \frac{a}{x^2 + a^2}$$

Dividing both sides by $a$ gives the standard result (syllabus 3.5, "including examples such as $\frac{1}{2+3x^2}$"):

$$\int \frac{1}{x^2 + a^2}\,\mathrm{d}x = \frac{1}{a}\tan^{-1}\left(\frac{x}{a}\right) + c$$

The number $a$ is the positive square root of the constant in the denominator: in $\frac{1}{4+x^2}$, $a = 2$; in $\frac{1}{9+y^2}$, $a = 3$. A constant multiplier pulls out in front:

$$\int \frac{4}{y^2 + 4}\,\mathrm{d}y = 4 \cdot \frac{1}{2}\tan^{-1}\left(\frac{y}{2}\right) + c = 2\tan^{-1}\left(\frac{y}{2}\right) + c$$

> ⭐ **Watch Out!** The classic coefficient trap (June 2023 report): for $\int \frac{1}{4 + 9y^2}\,\mathrm{d}y$ the correct answer is $\frac{1}{6}\tan^{-1}\left(\frac{3y}{2}\right) + c$ because $a = 2$ and the extra $9$ in front of $y^2$ contributes a further $\frac{1}{3}$. Writing $\frac{1}{2}\tan^{-1}\left(\frac{3y}{2}\right)$ was "very common" and wrong. The arctan result NEVER becomes a logarithm - the denominator is a sum, not a product.

### Example 26 - Easy - basic arctan integrals (June 2023 report examples)

> **Question:** Find (a) $\int \frac{1}{4 + x^2}\,\mathrm{d}x$, (b) $\int \frac{4}{y^2 + 4}\,\mathrm{d}y$.

**Solution:**

(a) Here $a = 2$:

$$\int \frac{1}{4 + x^2}\,\mathrm{d}x = \frac{1}{2}\tan^{-1}\left(\frac{x}{2}\right) + c$$

(b) Here $a = 2$ again, and the 4 multiplies the result:

$$\int \frac{4}{y^2 + 4}\,\mathrm{d}y = 4\int \frac{1}{y^2 + 4}\,\mathrm{d}y = 4 \cdot \frac{1}{2}\tan^{-1}\left(\frac{y}{2}\right) + c$$

$$= 2\tan^{-1}\left(\frac{y}{2}\right) + c \quad\checkmark$$

**What the examiner wants:** the $\frac{1}{a}$ factor, and recognising the arctan result at all - the June 2023 report noted some candidates wrote $\tan^{-1}\left(\frac{y}{2}\right)$ for part (b), missing the factor 2 in front, and others introduced logarithms to obtain $\ln(4+9y^2)$.

### Example 27 - Medium - the coefficient trap (June 2023 examiner report)

> **Question:** Find $\int \frac{1}{4 + 9y^2}\,\mathrm{d}y$.

**Solution:**

Substitute $u = 3y$, so $\mathrm{d}u = 3\,\mathrm{d}y$ and $\mathrm{d}y = \frac{1}{3}\mathrm{d}u$:

$$\int \frac{1}{4 + 9y^2}\,\mathrm{d}y = \int \frac{1}{4 + u^2} \cdot \frac{1}{3}\,\mathrm{d}u$$

$$= \frac{1}{3}\int \frac{1}{4 + u^2}\,\mathrm{d}u$$

The denominator is now $u^2 + a^2$ with $a = 2$:

$$= \frac{1}{3} \cdot \frac{1}{2}\tan^{-1}\left(\frac{u}{2}\right) + c$$

$$= \frac{1}{6}\tan^{-1}\left(\frac{u}{2}\right) + c$$

Substitute back $u = 3y$:

$$\int \frac{1}{4 + 9y^2}\,\mathrm{d}y = \frac{1}{6}\tan^{-1}\left(\frac{3y}{2}\right) + c \quad\checkmark$$

**What the examiner wants:** the full coefficient - $\frac{1}{a}$ from the arctan rule times $\frac{1}{3}$ from the substitution, giving $\frac{1}{6}$, not $\frac{1}{2}$. This exact integral appears in a June 2023 differential equation question.

### Example 28 - Hard - the syllabus's own example: $\frac{1}{2 + 3x^2}$ (syllabus 3.5)

> **Question:** Find $\int \frac{1}{2 + 3x^2}\,\mathrm{d}x$.

**Solution:**

Factor the constant out of the denominator to reach $1 + (\text{something})^2$:

$$2 + 3x^2 = 2\left(1 + \frac{3}{2}x^2\right)$$

$$\int \frac{1}{2 + 3x^2}\,\mathrm{d}x = \frac{1}{2}\int \frac{1}{1 + \frac{3}{2}x^2}\,\mathrm{d}x$$

Now $\frac{3}{2}x^2 = \left(\sqrt{\frac{3}{2}}\,x\right)^2$, so use the substitution $u = \sqrt{\frac{3}{2}}\,x$, $\mathrm{d}u = \sqrt{\frac{3}{2}}\,\mathrm{d}x$:

$$= \frac{1}{2} \cdot \frac{1}{\sqrt{3/2}}\int \frac{1}{1 + u^2}\,\mathrm{d}u$$

$$= \frac{1}{2}\sqrt{\frac{2}{3}}\tan^{-1}(u) + c$$

Simplify the constant:

$$\frac{1}{2}\sqrt{\frac{2}{3}} = \frac{\sqrt{2}}{2\sqrt{3}} = \frac{\sqrt{6}}{6} = \frac{1}{\sqrt{6}}$$

Substitute back:

$$\int \frac{1}{2 + 3x^2}\,\mathrm{d}x = \frac{1}{\sqrt{6}}\tan^{-1}\left(\sqrt{\frac{3}{2}}\,x\right) + c \quad\checkmark$$

**What the examiner wants:** factoring the coefficient of $x^2$ out FIRST, then applying the arctan rule with $a = \sqrt{\frac{2}{3}}$. This is the syllabus's own example.

## 4.2 The Log Rule: $\int \frac{k\,f'(x)}{f(x)}\,\mathrm{d}x$

By the chain rule, $\frac{\mathrm{d}}{\mathrm{d}x}\left(\ln|f(x)|\right) = \frac{f'(x)}{f(x)}$, so:

$$\int \frac{k\,f'(x)}{f(x)}\,\mathrm{d}x = k\ln|f(x)| + c$$

The rule fires exactly when the numerator is a constant multiple of the derivative of the denominator. Three recognisable shapes:

$$\int \frac{x}{x^2 + 4}\,\mathrm{d}x = \frac{1}{2}\ln\left(x^2 + 4\right) + c \qquad \left(f(x) = x^2+4, \ f'(x) = 2x\right)$$

$$\int \frac{3}{1+5x}\,\mathrm{d}x = \frac{3}{5}\ln|1+5x| + c \qquad \left(f(x) = 1+5x, \ f'(x) = 5\right)$$

$$\int \frac{\sec^2 x}{\tan x}\,\mathrm{d}x = \ln|\tan x| + c \qquad \left(f(x) = \tan x, \ f'(x) = \sec^2 x\right)$$

> ⭐ **Watch Out!** (Nov 2023 report) Candidates claimed $\int \frac{x-4}{x^2+4}\,\mathrm{d}x = \frac{1}{2}\ln(x^2+4)$ - WRONG. The $-4$ is not part of the derivative of $x^2+4$, so the integrand must be split first (the second piece is an arctan integral). The rule only fires when the numerator is EXACTLY a constant multiple of $f'(x)$, and never forget the modulus.

### Example 29 - Easy - recognising the log rule

> **Question:** Find (a) $\int \frac{x}{x^2 + 4}\,\mathrm{d}x$, (b) $\int \frac{3}{1 + 5x}\,\mathrm{d}x$.

**Solution:**

(a) Differentiate the denominator: $f(x) = x^2 + 4$, $f'(x) = 2x$. The numerator $x$ is $\frac{1}{2}f'(x)$, so $k = \frac{1}{2}$:

$$\int \frac{x}{x^2 + 4}\,\mathrm{d}x = \frac{1}{2}\ln\left(x^2 + 4\right) + c$$

(No modulus needed - $x^2 + 4 > 0$ always.)

(b) $f(x) = 1 + 5x$, $f'(x) = 5$. The numerator 3 is $\frac{3}{5}f'(x)$, so $k = \frac{3}{5}$:

$$\int \frac{3}{1 + 5x}\,\mathrm{d}x = \frac{3}{5}\ln|1 + 5x| + c \quad\checkmark$$

**What the examiner wants:** the quick mental check - differentiate the denominator, compare with the numerator, and read off $k$.

### Example 30 - Medium - trig numerator over trig denominator

> **Question:** Find $\int \frac{\sec^2 x}{\tan x}\,\mathrm{d}x$.

**Solution:**

$f(x) = \tan x$, $f'(x) = \sec^2 x$. The numerator is exactly $1 \times f'(x)$:

$$\int \frac{\sec^2 x}{\tan x}\,\mathrm{d}x = \ln|\tan x| + c \quad\checkmark$$

**What the examiner wants:** spotting the derivative hiding inside the fraction (the June 2023 report praised candidates who recognised $\sec 2x\tan 2x$ as a constant multiple of the derivative of $\sec 2x$ in a differential equation question).

### Example 31 - Hard - the split trap (Nov 2023 examiner report)

> **Question:** Find $\int \frac{x - 4}{x^2 + 4}\,\mathrm{d}x$.

**Solution:**

The numerator $x - 4$ is NOT a constant multiple of $2x$, so split the fraction:

$$\frac{x - 4}{x^2 + 4} = \frac{x}{x^2 + 4} - \frac{4}{x^2 + 4}$$

First piece - log rule with $k = \frac{1}{2}$:

$$\int \frac{x}{x^2 + 4}\,\mathrm{d}x = \frac{1}{2}\ln\left(x^2 + 4\right) + c$$

Second piece - arctan rule with $a = 2$:

$$\int \frac{4}{x^2 + 4}\,\mathrm{d}x = 4 \cdot \frac{1}{2}\tan^{-1}\left(\frac{x}{2}\right) + c = 2\tan^{-1}\left(\frac{x}{2}\right) + c$$

Combine:

$$\int \frac{x - 4}{x^2 + 4}\,\mathrm{d}x = \frac{1}{2}\ln\left(x^2 + 4\right) - 2\tan^{-1}\left(\frac{x}{2}\right) + c \quad\checkmark$$

**What the examiner wants:** refusing the tempting (wrong) single-log answer; one log piece plus one arctan piece.

## 4.3 Algebraic Preparation: Divide Before Integrating

If the degree of the numerator is at least the degree of the denominator, the fraction is improper - divide first. The Nov 2023 report: "many did not realise that the improper algebraic fraction needed to be dealt with before integration", and "several candidates spent a long time on attempts at integration by parts" instead of dividing.

> ⭐ **Watch Out!** (Nov 2023 report) Candidates "realised that they needed to split the fraction but then assumed that $x^2+4 = (x-2)(x+2)$". A sum of squares NEVER factors over the reals - which is exactly why it produces arctan, not log.

### Example 32 - Hard - divide, split, integrate (ON23 P32 Q5, 6 marks)

> **Question:** Find the exact value of $\int_0^6 \frac{x(x+1)}{x^2+4}\,\mathrm{d}x$.

**Solution:**

Expand the numerator:

$$\frac{x(x+1)}{x^2+4} = \frac{x^2 + x}{x^2 + 4}$$

The numerator degree equals the denominator degree, so divide first:

$$\frac{x^2 + x}{x^2 + 4} = 1 + \frac{x - 4}{x^2 + 4}$$

Check: $1 \cdot (x^2+4) + (x-4) = x^2 + 4 + x - 4 = x^2 + x$. Split the remainder:

$$\frac{x - 4}{x^2 + 4} = \frac{x}{x^2 + 4} - \frac{4}{x^2 + 4}$$

Now integrate the three terms - the 1 gives $x$, the middle is a log integral, the last is an arctan integral:

$$\int \left(1 + \frac{x}{x^2+4} - \frac{4}{x^2+4}\right)\mathrm{d}x = x + \frac{1}{2}\ln\left(x^2+4\right) - 2\tan^{-1}\left(\frac{x}{2}\right)$$

$$\int_0^6 \frac{x(x+1)}{x^2+4}\,\mathrm{d}x = \left[x + \frac{1}{2}\ln\left(x^2+4\right) - 2\tan^{-1}\left(\frac{x}{2}\right)\right]_0^6$$

Upper limit $x = 6$:

$$6 + \frac{1}{2}\ln 40 - 2\tan^{-1}(3)$$

Lower limit $x = 0$:

$$0 + \frac{1}{2}\ln 4 - 2\tan^{-1}(0) = \frac{1}{2}\ln 4$$

Subtract and combine the logs:

$$6 + \frac{1}{2}\ln 40 - 2\tan^{-1}(3) - \frac{1}{2}\ln 4 = 6 + \frac{1}{2}\ln 10 - 2\tan^{-1}(3) \quad\checkmark$$

*(computed estimate - question text confirmed; the Nov 2023 examiner report describes this exact question)*

**What the examiner wants:** the improper fraction dealt with BEFORE integration, then one log integral via $\frac{k f'(x)}{f(x)}$ and one arctan integral via $\frac{1}{x^2+a^2}$.

## 4.4 Repeated Linear Factors: Power, Not Log

$$\int \frac{k}{(ax+b)^2}\,\mathrm{d}x = -\frac{k}{a(ax+b)} + c$$

This is a negative power, never a logarithm. June 2023 report: "the correct answer for $\int \frac{k}{(x+2)^2}\,\mathrm{d}x$ was less common, with many candidates giving a third log term".

### Example 33 - Medium - the repeated factor trap (June 2023 examiner report)

> **Question:** Find $\int \frac{4}{(x+2)^2}\,\mathrm{d}x$.

**Solution:**

Write as a negative power:

$$\frac{4}{(x+2)^2} = 4(x+2)^{-2}$$

Integrate using the power rule in reverse:

$$\int 4(x+2)^{-2}\,\mathrm{d}x = 4 \cdot \frac{(x+2)^{-1}}{-1} + c$$

$$= -\frac{4}{x+2} + c \quad\checkmark$$

**What the examiner wants:** recognising $(x+2)^{-2}$ as a power of a linear factor - the answer is a rational function, NOT a logarithm.

## 4.5 Chapter 8 Closers: By Parts Questions That End With This Chapter's Integrals

Every integration-by-parts question on Paper 3 finishes with a Chapter 5 standard integral. The by-parts does the front work; the arctan, $\ln$ and trig results close the question.

### Example 34 - Hard - $\int \ln(3x)$ (ON25 P31 Q1, 4 marks)

> **Question:** Find the exact value of $\int_1^2 \ln(3x)\,\mathrm{d}x$. Give your answer in the form $a + \ln b$, where $a$ and $b$ are integers.

**Solution:**

By parts (Chapter 8) gives the antiderivative:

$$\int \ln(3x)\,\mathrm{d}x = x\ln(3x) - x + c$$

Check by differentiating: $x\ln(3x) - x$ differentiates to $\ln(3x) + x \cdot \frac{3}{3x} - 1 = \ln(3x)$. So:

$$\int_1^2 \ln(3x)\,\mathrm{d}x = \left[x\ln(3x) - x\right]_1^2$$

Upper limit $x = 2$:

$$2\ln 6 - 2$$

Lower limit $x = 1$:

$$\ln 3 - 1$$

Subtract:

$$2\ln 6 - 2 - \ln 3 + 1 = 2\ln 6 - \ln 3 - 1$$

Use $2\ln 6 = \ln 36$:

$$\ln 36 - \ln 3 - 1 = \ln\left(\frac{36}{3}\right) - 1 = \ln 12 - 1$$

$$= -1 + \ln 12 \quad\checkmark$$

*(computed estimate - question text confirmed from the paper; the "form $a + \ln b$" instruction pins the required shape, so $a = -1$, $b = 12$)*

**What the examiner wants:** the exact form $-1 + \ln 12$ matching "$a + \ln b$", with the log combination done correctly ($2\ln 6 - \ln 3 = \ln 12$).

### Example 35 - Hard - $\int x\tan^{-1}(2x)$ (MJ25 P32 Q10(b), 6 marks)

> **Question:** Find the exact value of $\int_0^{0.5} x\tan^{-1}(2x)\,\mathrm{d}x$.

**Solution:**

By parts with $u = \tan^{-1}(2x)$, $\frac{\mathrm{d}v}{\mathrm{d}x} = x$:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = \frac{2}{1 + 4x^2}, \qquad v = \frac{x^2}{2}$$

$$\int_0^{0.5} x\tan^{-1}(2x)\,\mathrm{d}x = \left[\frac{x^2}{2}\tan^{-1}(2x)\right]_0^{0.5} - \int_0^{0.5} \frac{x^2}{2} \cdot \frac{2}{1 + 4x^2}\,\mathrm{d}x$$

$$= \left[\frac{x^2}{2}\tan^{-1}(2x)\right]_0^{0.5} - \int_0^{0.5} \frac{x^2}{1 + 4x^2}\,\mathrm{d}x$$

Boundary term:

$$\frac{(0.5)^2}{2}\tan^{-1}(1) - 0 = \frac{0.25}{2} \cdot \frac{\pi}{4} = \frac{1}{8} \cdot \frac{\pi}{4} = \frac{\pi}{32}$$

Prepare the second integrand - algebraic division of $\frac{x^2}{1+4x^2}$:

$$\frac{x^2}{1 + 4x^2} = \frac{1}{4} - \frac{1}{4(1 + 4x^2)}$$

Check by combining over the common denominator:

$$\frac{1}{4} - \frac{1}{4(1+4x^2)} = \frac{1 + 4x^2 - 1}{4(1+4x^2)} = \frac{4x^2}{4(1+4x^2)} = \frac{x^2}{1+4x^2} \quad\checkmark$$

Integrate - for the second term, write $1 + 4x^2 = 1 + (2x)^2$ so $\int \frac{1}{1+4x^2}\,\mathrm{d}x = \frac{1}{2}\tan^{-1}(2x)$:

$$\int \left(\frac{1}{4} - \frac{1}{4(1 + 4x^2)}\right)\mathrm{d}x = \frac{x}{4} - \frac{1}{4} \cdot \frac{1}{2}\tan^{-1}(2x) = \frac{x}{4} - \frac{1}{8}\tan^{-1}(2x)$$

Evaluate from 0 to 0.5:

$$\left[\frac{x}{4} - \frac{1}{8}\tan^{-1}(2x)\right]_0^{0.5} = \left(\frac{0.5}{4} - \frac{1}{8}\tan^{-1}(1)\right) - (0 - 0) = \frac{1}{8} - \frac{\pi}{32}$$

Subtract from the boundary term:

$$\frac{\pi}{32} - \left(\frac{1}{8} - \frac{\pi}{32}\right) = \frac{\pi}{32} - \frac{1}{8} + \frac{\pi}{32} = \frac{\pi}{16} - \frac{1}{8} \quad\checkmark$$

*(computed estimate - question text confirmed from the paper; no local mark scheme)*

**What the examiner wants:** the algebraic preparation step (splitting $\frac{x^2}{1+4x^2}$ into a constant plus an arctan integrand) is the make-or-break step - candidates who skipped it could not finish. The chapter's $\frac{1}{x^2+a^2}$ result does the heavy lifting at the end.

### Example 36 - Hard - $\int x^2\sin 2x$ (ON25 P33 Q6, 6 marks)

> **Question:** Find the exact value of $\int_0^{\frac{\pi}{6}} x^2\sin 2x\,\mathrm{d}x$.

**Solution:**

By parts applied twice. First application - $u = x^2$, $\frac{\mathrm{d}v}{\mathrm{d}x} = \sin 2x$:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = 2x, \qquad v = -\frac{1}{2}\cos 2x$$

$$\int x^2\sin 2x\,\mathrm{d}x = -\frac{x^2}{2}\cos 2x + \int x\cos 2x\,\mathrm{d}x$$

Second application - $u = x$, $\frac{\mathrm{d}v}{\mathrm{d}x} = \cos 2x$:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = 1, \qquad v = \frac{1}{2}\sin 2x$$

$$\int x\cos 2x\,\mathrm{d}x = \frac{x}{2}\sin 2x - \int \frac{1}{2}\sin 2x\,\mathrm{d}x$$

$$= \frac{x}{2}\sin 2x + \frac{1}{4}\cos 2x$$

Combine:

$$F(x) = -\frac{x^2}{2}\cos 2x + \frac{x}{2}\sin 2x + \frac{1}{4}\cos 2x$$

$$\int_0^{\frac{\pi}{6}} x^2\sin 2x\,\mathrm{d}x = \left[F(x)\right]_0^{\frac{\pi}{6}}$$

Upper limit $x = \frac{\pi}{6}$:

$$-\frac{1}{2}\left(\frac{\pi}{6}\right)^2\cos\left(\frac{\pi}{3}\right) + \frac{1}{2}\left(\frac{\pi}{6}\right)\sin\left(\frac{\pi}{3}\right) + \frac{1}{4}\cos\left(\frac{\pi}{3}\right)$$

$$= -\frac{\pi^2}{72} \cdot \frac{1}{2} + \frac{\pi}{12} \cdot \frac{\sqrt{3}}{2} + \frac{1}{4} \cdot \frac{1}{2} = -\frac{\pi^2}{144} + \frac{\sqrt{3}\pi}{24} + \frac{1}{8}$$

Lower limit $x = 0$:

$$0 + 0 + \frac{1}{4}\cos 0 = \frac{1}{4}$$

Subtract:

$$-\frac{\pi^2}{144} + \frac{\sqrt{3}\pi}{24} + \frac{1}{8} - \frac{1}{4} = \frac{\sqrt{3}\pi}{24} - \frac{\pi^2}{144} - \frac{1}{8} \quad\checkmark$$

*(computed estimate - question text confirmed from the paper; no local mark scheme)*

**What the examiner wants:** sign discipline through two rounds of by parts ($\sin 2x$ integrates to $-\frac{1}{2}\cos 2x$), exact values at $\frac{\pi}{6}$, and keeping the $\pi$ and $\pi^2$ terms separate.

### Example 37 - Hard - $\int x^2\cos\left(\frac{x}{3}\right)$ (FM25 P32 Q11, 6 marks)

> **Question:** Find the exact value of $\int_0^{\pi} x^2\cos\left(\frac{x}{3}\right)\mathrm{d}x$.

**Solution:**

By parts applied twice. First application - $u = x^2$, $\frac{\mathrm{d}v}{\mathrm{d}x} = \cos\left(\frac{x}{3}\right)$:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = 2x, \qquad v = 3\sin\left(\frac{x}{3}\right)$$

$$\int x^2\cos\left(\frac{x}{3}\right)\mathrm{d}x = 3x^2\sin\left(\frac{x}{3}\right) - \int 3\sin\left(\frac{x}{3}\right) \cdot 2x\,\mathrm{d}x$$

$$= 3x^2\sin\left(\frac{x}{3}\right) - 6\int x\sin\left(\frac{x}{3}\right)\mathrm{d}x$$

Second application - $u = x$, $\frac{\mathrm{d}v}{\mathrm{d}x} = \sin\left(\frac{x}{3}\right)$:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = 1, \qquad v = -3\cos\left(\frac{x}{3}\right)$$

$$\int x\sin\left(\frac{x}{3}\right)\mathrm{d}x = -3x\cos\left(\frac{x}{3}\right) + \int 3\cos\left(\frac{x}{3}\right)\mathrm{d}x$$

$$= -3x\cos\left(\frac{x}{3}\right) + 9\sin\left(\frac{x}{3}\right)$$

Combine:

$$F(x) = 3x^2\sin\left(\frac{x}{3}\right) - 6\left(-3x\cos\left(\frac{x}{3}\right) + 9\sin\left(\frac{x}{3}\right)\right)$$

$$= 3x^2\sin\left(\frac{x}{3}\right) + 18x\cos\left(\frac{x}{3}\right) - 54\sin\left(\frac{x}{3}\right)$$

Upper limit $x = \pi$:

$$3\pi^2\sin\left(\frac{\pi}{3}\right) + 18\pi\cos\left(\frac{\pi}{3}\right) - 54\sin\left(\frac{\pi}{3}\right) = 3\pi^2\left(\frac{\sqrt{3}}{2}\right) + 18\pi\left(\frac{1}{2}\right) - 54\left(\frac{\sqrt{3}}{2}\right)$$

$$= \frac{3\sqrt{3}}{2}\pi^2 + 9\pi - 27\sqrt{3}$$

Lower limit $x = 0$:

$$0 + 0 - 0 = 0$$

$$\int_0^{\pi} x^2\cos\left(\frac{x}{3}\right)\mathrm{d}x = \frac{3\sqrt{3}}{2}\pi^2 + 9\pi - 27\sqrt{3} \quad\checkmark$$

*(computed estimate - question text confirmed from the paper; no local mark scheme)*

**What the examiner wants:** the repeated by-parts pattern done methodically (Nov 2023 report: "very few applied the method twice to obtain a correct expression"), and exact values of sine and cosine at $\pi$-family angles. Everything after the by-parts is Chapter 5 standard integrals.

## 4.6 Using a Given Substitution (syllabus 3.5)

The substitution is always GIVEN in P3, so the skill is mechanical:

1. Differentiate the substitution to get $\frac{\mathrm{d}u}{\mathrm{d}x}$, hence $\mathrm{d}x$.
2. Replace every $x$ (or trig function of $x$) in the integrand with $u$.
3. For definite integrals, change the limits BEFORE integrating: $x = a \Rightarrow u = u(a)$.
4. Integrate in $u$.
5. For indefinite integrals, substitute back to $x$ at the end.

June 2023 report advice: change the limits and find $\frac{\mathrm{d}u}{\mathrm{d}x}$ and hence $\frac{\mathrm{d}x}{\mathrm{d}u}$ SEPARATELY from the integrand work - candidates who combined everything in one line "did not show clearly that they were carrying out all of the operations correctly".

### Example 38 - Medium - the syllabus's own example: $u = \sin x$ (syllabus 3.5)

> **Question:** Use the substitution $u = \sin x$ to find $\int \sin^2 2x\cos x\,\mathrm{d}x$.

**Solution:**

Differentiate the substitution:

$$u = \sin x \quad\Rightarrow\quad \frac{\mathrm{d}u}{\mathrm{d}x} = \cos x \quad\Rightarrow\quad \mathrm{d}u = \cos x\,\mathrm{d}x$$

Rewrite $\sin 2x$ in terms of $u$:

$$\sin 2x = 2\sin x\cos x = 2u\cos x$$

So:

$$\sin^2 2x\cos x\,\mathrm{d}x = (2u\cos x)^2 \cdot \cos x\,\mathrm{d}x = 4u^2\cos^2 x \cdot \cos x\,\mathrm{d}x = 4u^2\cos^3 x\,\mathrm{d}x$$

Use $\mathrm{d}u = \cos x\,\mathrm{d}x$, leaving $\cos^2 x$ to convert:

$$4u^2\cos^3 x\,\mathrm{d}x = 4u^2\cos^2 x \cdot \cos x\,\mathrm{d}x = 4u^2\cos^2 x\,\mathrm{d}u$$

And $\cos^2 x = 1 - \sin^2 x = 1 - u^2$:

$$\int \sin^2 2x\cos x\,\mathrm{d}x = 4\int u^2\left(1 - u^2\right)\mathrm{d}u$$

$$= 4\int \left(u^2 - u^4\right)\mathrm{d}u$$

$$= 4\left(\frac{u^3}{3} - \frac{u^5}{5}\right) + c$$

Substitute back $u = \sin x$:

$$\int \sin^2 2x\cos x\,\mathrm{d}x = \frac{4}{3}\sin^3 x - \frac{4}{5}\sin^5 x + c \quad\checkmark$$

**What the examiner wants:** the substitution written out cleanly (June 2023 report: separate lines for $\frac{\mathrm{d}u}{\mathrm{d}x}$, the integrand swap, and the limits), and the trig swap $\cos^2 x = 1 - u^2$ handled before integrating.

### Example 39 - Medium - definite integral with changed limits

> **Question:** Use the substitution $u = \sin x$ to evaluate $\int_0^{\frac{\pi}{2}} \sin^2 x\cos x\,\mathrm{d}x$.

**Solution:**

Differentiate the substitution and change the limits:

$$u = \sin x, \qquad \frac{\mathrm{d}u}{\mathrm{d}x} = \cos x, \qquad \mathrm{d}u = \cos x\,\mathrm{d}x$$

$$x = 0 \Rightarrow u = \sin 0 = 0, \qquad x = \frac{\pi}{2} \Rightarrow u = \sin\left(\frac{\pi}{2}\right) = 1$$

Replace the integrand:

$$\sin^2 x\cos x\,\mathrm{d}x = u^2\,\mathrm{d}u$$

$$\int_0^{\frac{\pi}{2}} \sin^2 x\cos x\,\mathrm{d}x = \int_0^1 u^2\,\mathrm{d}u$$

$$= \left[\frac{u^3}{3}\right]_0^1 = \frac{1}{3} - 0 = \frac{1}{3} \quad\checkmark$$

**What the examiner wants:** the limits converted to $u$ BEFORE integrating (never substitute back into a definite integral), and the answer left as a number.

### Practice Questions - Part 4

**Q1.** Find $\int \frac{3}{9 + x^2}\,\mathrm{d}x$.

**Q2.** Find $\int \frac{2x}{x^2 + 5}\,\mathrm{d}x$.

**Q3.** Find the exact value of $\int_0^2 \frac{2x + 1}{x^2 + x + 4}\,\mathrm{d}x$. (Spot the derivative of the denominator in the numerator.)

**Q4.** Find $\int \frac{x^2}{x^2 + 9}\,\mathrm{d}x$. (Improper fraction - divide first.)

**Q5.** Use the substitution $u = \sin x$ to find $\int_0^{\frac{\pi}{2}} \sin^2 x\cos x\,\mathrm{d}x$, then verify the answer by direct integration of the antiderivative.

### Practice Questions - Part 4 - Full Solutions

**Solution Q1:**

Here $a = 3$:

$$\int \frac{3}{9 + x^2}\,\mathrm{d}x = 3\int \frac{1}{9 + x^2}\,\mathrm{d}x = 3 \cdot \frac{1}{3}\tan^{-1}\left(\frac{x}{3}\right) + c$$

$$= \tan^{-1}\left(\frac{x}{3}\right) + c \quad\checkmark$$

**Solution Q2:**

$f(x) = x^2 + 5$, $f'(x) = 2x$. The numerator is exactly $f'(x)$, so $k = 1$:

$$\int \frac{2x}{x^2 + 5}\,\mathrm{d}x = \ln\left(x^2 + 5\right) + c \quad\checkmark$$

**Solution Q3:**

$f(x) = x^2 + x + 4$, $f'(x) = 2x + 1$. The numerator is exactly $f'(x)$:

$$\int_0^2 \frac{2x + 1}{x^2 + x + 4}\,\mathrm{d}x = \left[\ln\left(x^2 + x + 4\right)\right]_0^2$$

Upper limit $x = 2$:

$$\ln(4 + 2 + 4) = \ln 10$$

Lower limit $x = 0$:

$$\ln 4$$

Subtract:

$$\ln 10 - \ln 4 = \ln\left(\frac{10}{4}\right) = \ln\left(\frac{5}{2}\right) \quad\checkmark$$

**Solution Q4:**

Divide first - the numerator degree equals the denominator degree:

$$\frac{x^2}{x^2 + 9} = 1 - \frac{9}{x^2 + 9}$$

Check: $1 \cdot (x^2+9) - 9 = x^2$. Integrate:

$$\int \frac{x^2}{x^2 + 9}\,\mathrm{d}x = \int \left(1 - \frac{9}{x^2 + 9}\right)\mathrm{d}x$$

$$= x - 9 \cdot \frac{1}{3}\tan^{-1}\left(\frac{x}{3}\right) + c = x - 3\tan^{-1}\left(\frac{x}{3}\right) + c \quad\checkmark$$

**Solution Q5:**

Limits change: $x = 0 \Rightarrow u = 0$, $x = \frac{\pi}{2} \Rightarrow u = 1$:

$$\int_0^{\frac{\pi}{2}} \sin^2 x\cos x\,\mathrm{d}x = \int_0^1 u^2\,\mathrm{d}u = \left[\frac{u^3}{3}\right]_0^1 = \frac{1}{3}$$

Verification - the antiderivative of $\sin^2 x\cos x$ is $\frac{\sin^3 x}{3}$ (since $\frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{\sin^3 x}{3}\right) = \sin^2 x\cos x$):

$$\left[\frac{\sin^3 x}{3}\right]_0^{\frac{\pi}{2}} = \frac{1}{3}(1)^3 - \frac{1}{3}(0)^3 = \frac{1}{3} \quad\checkmark$$

---

# Formula Sheet

**The five non-negotiable standard integrals** (all divided by $a$, sine with a minus):

$$\int e^{ax+b}\,\mathrm{d}x = \frac{1}{a}e^{ax+b} + c \qquad \int \frac{1}{ax+b}\,\mathrm{d}x = \frac{1}{a}\ln|ax+b| + c$$

$$\int \sin(ax+b)\,\mathrm{d}x = -\frac{1}{a}\cos(ax+b) + c \qquad \int \cos(ax+b)\,\mathrm{d}x = \frac{1}{a}\sin(ax+b) + c$$

$$\int \sec^2(ax+b)\,\mathrm{d}x = \frac{1}{a}\tan(ax+b) + c$$

**P3 additions:**

$$\int \frac{1}{x^2+a^2}\,\mathrm{d}x = \frac{1}{a}\tan^{-1}\left(\frac{x}{a}\right) + c \qquad \int \frac{k\,f'(x)}{f(x)}\,\mathrm{d}x = k\ln|f(x)| + c$$

**Reverse differentiation results to spot:**

$$\int \sec x\tan x\,\mathrm{d}x = \sec x + c \qquad \int \cosec^2 x\,\mathrm{d}x = -\cot x + c \qquad \int \cosec x\cot x\,\mathrm{d}x = -\cosec x + c$$

**Squares (double angle identities applied first):**

$$\int \sin^2(ax)\,\mathrm{d}x = \frac{x}{2} - \frac{\sin(2ax)}{4a} + c \qquad \int \cos^2(ax)\,\mathrm{d}x = \frac{x}{2} + \frac{\sin(2ax)}{4a} + c$$

$$\int \tan^2 x\,\mathrm{d}x = \tan x - x + c \qquad \int \sin^4 x\,\mathrm{d}x = \frac{3x}{8} - \frac{\sin 2x}{4} + \frac{\sin 4x}{32} + c$$

**Factor formulae (product-to-sum):**

$$2\sin A\sin B = \cos(A-B) - \cos(A+B) \qquad 2\cos A\cos B = \cos(A-B) + \cos(A+B)$$

$$2\sin A\cos B = \sin(A+B) + \sin(A-B)$$

**Definite integrals:**

$$\int_a^b f(x)\,\mathrm{d}x = \left[F(x)\right]_a^b = F(b) - F(a) \qquad \int_a^b f(x)\,\mathrm{d}x = -\int_b^a f(x)\,\mathrm{d}x$$

$$\int_a^b f(x)\,\mathrm{d}x = \int_a^c f(x)\,\mathrm{d}x + \int_c^b f(x)\,\mathrm{d}x \qquad \int_a^b \big(f(x) \pm g(x)\big)\mathrm{d}x = \int_a^b f(x)\,\mathrm{d}x \pm \int_a^b g(x)\,\mathrm{d}x$$

**Area under a curve:**

$$\text{Area} = \int_a^b y\,\mathrm{d}x \qquad \text{(split at axis crossings and add moduli otherwise)}$$

**Trapezium rule:**

$$\int_a^b f(x)\,\mathrm{d}x \approx \frac{h}{2}\left(y_0 + y_n + 2\left(y_1 + y_2 + \cdots + y_{n-1}\right)\right), \qquad h = \frac{b-a}{n}$$

over-estimate when the top edges of the strips lie above the curve, under-estimate when they lie below.

**Curve from its gradient:**

$$\frac{\mathrm{d}y}{\mathrm{d}x} = f(x) \Rightarrow y = \int f(x)\,\mathrm{d}x + c, \qquad \text{with } c \text{ found from a given point}$$

**Given substitution:**

$$u = g(x), \quad \mathrm{d}u = g'(x)\,\mathrm{d}x, \qquad x = a \Rightarrow u = g(a) \text{ (change limits before integrating)}$$

---

# Quick Reference Card

1. **Standard form?** Write the answer: divide by $a$, sine goes to negative cosine, $\ln$ gets a modulus, add $+c$.
2. **Square of a trig function?** Identity swap: $\sin^2 \to \frac{1}{2}(1-\cos 2x)$, $\cos^2 \to \frac{1}{2}(1+\cos 2x)$, $\tan^2 \to \sec^2 x - 1$. Higher powers: apply twice.
3. **Product of trig functions?** Factor formula to a sum, then integrate term by term.
4. **Improper fraction (numerator degree $\ge$ denominator degree)?** Divide first, then split.
5. **Numerator a constant multiple of the denominator's derivative?** $\ln$: $\int \frac{k f'(x)}{f(x)}\,\mathrm{d}x = k\ln|f(x)| + c$.
6. **$\frac{k}{x^2+a^2}$ shape?** $\tan^{-1}$: $\frac{k}{a}\tan^{-1}\left(\frac{x}{a}\right) + c$. Factor out any $x^2$ coefficient first.
7. **$(ax+b)^{-n}$ with $n \ge 2$?** Power rule, never a log.
8. **Definite integral?** Square brackets, upper limit first, exact form ($\pi$, $e$, $\ln$, surds) unless told to round.
9. **Area?** Split at axis crossings, add moduli; trapezium rule only when integration is impossible and asked.
10. **Still stuck?** Given substitution, or by parts (Chapter 8) - which always ends with one of the integrals above.
