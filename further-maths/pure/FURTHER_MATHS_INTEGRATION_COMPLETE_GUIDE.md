# 📐 FURTHER MATHS INTEGRATION - ULTIMATE STUDY GUIDE

## Cambridge International AS & A Level Further Mathematics (9231) - Paper 2 (Further Pure 2)

> **The complete walkthrough:** Every integration technique from Chapter 22 explained step-by-step, with dozens of fully solved examples in proper LaTeX - substitutions (including $t=\tan\frac{x}{2}$), hyperbolic integrals, reduction formulae, arc lengths, surface areas of revolution, Riemann sums with $\Delta x\to 0$ and the integral test.

---

# 📋 Table of Contents

1. [PART 1: Standard Integrals & Choosing the Right Substitution](#part-1-standard-integrals--choosing-the-right-substitution)
2. [PART 2: Hyperbolic Functions in Integration](#part-2-hyperbolic-functions-in-integration)
3. [PART 3: Reduction Formulae](#part-3-reduction-formulae)
4. [PART 4: Arc Lengths (Cartesian, Parametric, Polar)](#part-4-arc-lengths-cartesian-parametric-polar)
5. [PART 5: Surface Areas of Revolution](#part-5-surface-areas-of-revolution)
6. [PART 6A: Rectangle Sums and Limits of Areas (width $\to 0$)](#part-6a-rectangle-sums-and-limits-of-areas-width--0)
7. [PART 6B: Limits of Areas - The Integral Test (unit-width rectangles)](#part-6b-limits-of-areas---the-integral-test-unit-width-rectangles)
8. [Formula Sheet](#formula-sheet)
9. [Cambridge Exam Analysis](#cambridge-exam-analysis)
10. [Common Mistakes](#common-mistakes)
11. [Practice Questions & Solutions](#practice-questions--solutions)
12. [Exam Strategy](#exam-strategy)
13. [Quick Reference Card](#quick-reference-card)

---

# How To Use This Guide

Each section follows this structure:

1. **The Rule** - the formula you must know (in LaTeX)
2. **Step-by-Step Method** - a numbered algorithm you can follow
3. **Easy Example** - labelled **Example 1**
4. **Medium Example** - labelled **Example 2**
5. **Hard Example** - labelled **Example 3**
6. **Watch Out!** - common pitfalls

---

# PART 1: Standard Integrals & Choosing the Right Substitution

## 1.1 The Five Standard Results You Must Know

These come straight from the FP2 formula list. They are the building blocks of every substitution question in this chapter:

| Integral | Result |
|---|---|
| $\displaystyle \int \frac{1}{a^2 + x^2}\;\mathrm{d}x$ | $\displaystyle \frac{1}{a}\tan^{-1}\!\left(\frac{x}{a}\right) + c$ |
| $\displaystyle \int \frac{1}{\sqrt{a^2 - x^2}}\;\mathrm{d}x$ | $\displaystyle \sin^{-1}\!\left(\frac{x}{a}\right) + c$ |
| $\displaystyle \int \frac{1}{a^2 - x^2}\;\mathrm{d}x$ | $\displaystyle \frac{1}{a}\tanh^{-1}\!\left(\frac{x}{a}\right) + c$ |
| $\displaystyle \int \frac{1}{\sqrt{x^2 + a^2}}\;\mathrm{d}x$ | $\displaystyle \sinh^{-1}\!\left(\frac{x}{a}\right) + c$ |
| $\displaystyle \int \frac{1}{\sqrt{x^2 - a^2}}\;\mathrm{d}x$ | $\displaystyle \cosh^{-1}\!\left(\frac{x}{a}\right) + c$ |

**Why they work:** each one comes from differentiating an inverse function. For example:

$$\frac{\mathrm{d}}{\mathrm{d}x}\left[\sin^{-1}\!\left(\frac{x}{a}\right)\right] = \frac{\frac{1}{a}}{\sqrt{1 - \frac{x^2}{a^2}}} = \frac{1}{\sqrt{a^2 - x^2}}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\left[\sinh^{-1}\!\left(\frac{x}{a}\right)\right] = \frac{1}{\sqrt{x^2 + a^2}}$$

### Quick Check

$$\int \frac{1}{9 + x^2}\;\mathrm{d}x = \frac{1}{3}\tan^{-1}\!\left(\frac{x}{3}\right) + c$$

$$\int \frac{1}{\sqrt{25 - x^2}}\;\mathrm{d}x = \sin^{-1}\!\left(\frac{x}{5}\right) + c$$

$$\int \frac{1}{\sqrt{x^2 + 16}}\;\mathrm{d}x = \sinh^{-1}\!\left(\frac{x}{4}\right) + c$$

---

## 1.2 The Substitution Decision Table

When the integrand has a square root (or denominator) of two terms, a substitution replaces those two terms with ONE term using a Pythagorean-style identity:

| Form you see | Identity to use | Substitution | What the square root becomes |
|---|---|---|---|
| $a^2 - x^2$ | $1 - \sin^2 u = \cos^2 u$ | $x = a\sin u$ | $a\cos u$ |
| $a^2 - x^2$ | $1 - \tanh^2 u = \operatorname{sech}^2 u$ | $x = a\tanh u$ | $a\operatorname{sech} u$ |
| $a^2 + x^2$ | $1 + \tan^2 u = \sec^2 u$ | $x = a\tan u$ | $a\sec u$ |
| $a^2 + x^2$ | $1 + \sinh^2 u = \cosh^2 u$ | $x = a\sinh u$ | $a\cosh u$ |
| $x^2 - a^2$ | $\sec^2 u - 1 = \tan^2 u$ | $x = a\sec u$ | $a\tan u$ |
| $x^2 - a^2$ | $\cosh^2 u - 1 = \sinh^2 u$ | $x = a\cosh u$ | $a\sinh u$ |

### The Method

| Step | What To Do |
|---|---|
| **Step 1** | Match the form ($a^2 - x^2$, $a^2 + x^2$ or $x^2 - a^2$) to the substitution in the table |
| **Step 2** | Differentiate the substitution to find $\mathrm{d}x$ in terms of $u$ |
| **Step 3** | Replace $x$ and $\mathrm{d}x$ in the integral; simplify using the identity |
| **Step 4** | Integrate (now it is a simple standard integral) |
| **Step 5** | Convert back to $x$ using the inverse of your substitution |
| **Step 6** | For definite integrals: convert the LIMITS too (or convert back before applying them) |

> ⭐ **Watch Out!** For definite integrals, the cleanest method is to convert the limits to $u$ BEFORE integrating - you never need to convert back. Example 2 shows this.

---

### Example 1 - Easy (trig substitution $x = a\tan u$)

> **Question:** Determine the indefinite integral $\displaystyle I = \int \frac{1}{4 + x^2}\;\mathrm{d}x$.

**Solution:**

We have $a^2 + x^2$ with $a = 2$, so use $x = 2\tan u$:

$$\frac{\mathrm{d}x}{\mathrm{d}u} = 2\sec^2 u \quad\Rightarrow\quad \mathrm{d}x = 2\sec^2 u\;\mathrm{d}u$$

Substitute into the integral:

$$I = \int \frac{2\sec^2 u}{4 + 4\tan^2 u}\;\mathrm{d}u$$

Use $1 + \tan^2 u = \sec^2 u$:

$$I = \int \frac{2\sec^2 u}{4\sec^2 u}\;\mathrm{d}u = \int \frac{1}{2}\;\mathrm{d}u$$

$$I = \frac{1}{2}u + c$$

Convert back, using $u = \tan^{-1}\!\left(\frac{x}{2}\right)$:

$$I = \frac{1}{2}\tan^{-1}\!\left(\frac{x}{2}\right) + c \quad\checkmark$$

---

### Example 2 - Medium (trig substitution with definite limits)

> **Question:** Find the exact value of $\displaystyle \int_0^{1.5} \sqrt{9 - x^2}\;\mathrm{d}x$.

**Solution:**

We have $a^2 - x^2$ with $a = 3$, so use $x = 3\sin u$:

$$\frac{\mathrm{d}x}{\mathrm{d}u} = 3\cos u \quad\Rightarrow\quad \mathrm{d}x = 3\cos u\;\mathrm{d}u$$

Convert the limits:

$$x = 0 \Rightarrow 3\sin u = 0 \Rightarrow u = 0$$

$$x = 1.5 \Rightarrow 3\sin u = 1.5 \Rightarrow \sin u = \frac{1}{2} \Rightarrow u = \frac{\pi}{6}$$

Substitute everything:

$$I = \int_0^{\pi/6} \sqrt{9 - 9\sin^2 u} \cdot 3\cos u\;\mathrm{d}u$$

$$I = \int_0^{\pi/6} 3\cos u \cdot 3\cos u\;\mathrm{d}u = 9\int_0^{\pi/6} \cos^2 u\;\mathrm{d}u$$

Use $\cos^2 u = \frac{1}{2}(1 + \cos 2u)$:

$$I = \frac{9}{2}\int_0^{\pi/6} (1 + \cos 2u)\;\mathrm{d}u$$

$$I = \frac{9}{2}\left[u + \frac{1}{2}\sin 2u\right]_0^{\pi/6}$$

$$I = \frac{9}{2}\left(\frac{\pi}{6} + \frac{1}{2}\sin\frac{\pi}{3} - 0 - 0\right)$$

$$I = \frac{9}{2}\left(\frac{\pi}{6} + \frac{1}{2}\cdot\frac{\sqrt{3}}{2}\right) = \frac{9}{2}\left(\frac{\pi}{6} + \frac{\sqrt{3}}{4}\right)$$

$$I = \frac{3\pi}{4} + \frac{9\sqrt{3}}{8} \approx 4.30 \quad\checkmark$$

---

### Example 3 - Medium (hyperbolic substitution $x = a\sinh u$)

> **Question:** Using an appropriate substitution, determine the result of $\displaystyle \int \frac{3}{\sqrt{x^2 + 4}}\;\mathrm{d}x$.

**Solution:**

We have $x^2 + a^2$ with $a = 2$. Either $x = 2\tan u$ or $x = 2\sinh u$ works; the hyperbolic substitution is faster:

$$\frac{\mathrm{d}x}{\mathrm{d}u} = 2\cosh u \quad\Rightarrow\quad \mathrm{d}x = 2\cosh u\;\mathrm{d}u$$

$$I = \int \frac{3 \cdot 2\cosh u}{\sqrt{4\sinh^2 u + 4}}\;\mathrm{d}u$$

Use $1 + \sinh^2 u = \cosh^2 u$:

$$I = \int \frac{6\cosh u}{2\cosh u}\;\mathrm{d}u = \int 3\;\mathrm{d}u$$

$$I = 3u + c$$

Convert back, using $u = \sinh^{-1}\!\left(\frac{x}{2}\right)$:

$$I = 3\sinh^{-1}\!\left(\frac{x}{2}\right) + c \quad\checkmark$$

---

### Example 4 - Hard (choosing the WRONG substitution wastes time)

> **Question:** Using an appropriate substitution, determine the result of $\displaystyle \int \frac{1}{\sqrt{9 - 4x^2}}\;\mathrm{d}x$. Discuss your findings.

**Solution - the slow way ($x = \frac{3}{2}\tanh u$):**

Let $2x = 3\tanh u$, so $2\,\frac{\mathrm{d}x}{\mathrm{d}u} = 3\operatorname{sech}^2 u$, giving $\mathrm{d}x = \frac{3}{2}\operatorname{sech}^2 u\;\mathrm{d}u$:

$$I = \int \frac{\frac{3}{2}\operatorname{sech}^2 u}{\sqrt{9 - 9\tanh^2 u}}\;\mathrm{d}u = \int \frac{\frac{3}{2}\operatorname{sech}^2 u}{3\operatorname{sech} u}\;\mathrm{d}u = \int \frac{1}{2}\operatorname{sech} u\;\mathrm{d}u$$

Integrating $\operatorname{sech} u$ is not simple - it needs a further substitution ($t = e^u$). The result comes out as:

$$I = \frac{1}{2}\tan^{-1}\!\left(e^u\right) + c = \frac{1}{2}\tan^{-1}\!\left(e^{\tanh^{-1}(2x/3)}\right) + c$$

This is correct but ugly. **The trig substitution is far better.**

**Solution - the fast way ($x = \frac{3}{2}\sin u$):**

Let $2x = 3\sin u$, so $2\,\frac{\mathrm{d}x}{\mathrm{d}u} = 3\cos u$, giving $\mathrm{d}x = \frac{3}{2}\cos u\;\mathrm{d}u$:

$$I = \int \frac{\frac{3}{2}\cos u}{\sqrt{9 - 9\sin^2 u}}\;\mathrm{d}u = \int \frac{\frac{3}{2}\cos u}{3\cos u}\;\mathrm{d}u = \int \frac{1}{2}\;\mathrm{d}u$$

$$I = \frac{1}{2}u + c$$

Convert back, using $\sin u = \frac{2x}{3}$, so $u = \sin^{-1}\!\left(\frac{2x}{3}\right)$:

$$I = \frac{1}{2}\sin^{-1}\!\left(\frac{2x}{3}\right) + c \quad\checkmark$$

> ⭐ **Watch Out!** For $a^2 - x^2$ forms, prefer $x = a\sin u$ over $x = a\tanh u$ - the trig route lands on a standard integral immediately, while the hyperbolic route leads to $\int \operatorname{sech} u\;\mathrm{d}u$ which needs a second substitution. The coursebook makes exactly this point in Worked Example 22.4.

---

## 1.3 Completing the Square First

When the denominator is a quadratic that does not factor nicely (like $x^2 + 2x + 2$), complete the square first to turn it into one of the standard forms:

$$x^2 + 2x + 2 = (x + 1)^2 + 1$$

$$x^2 - 4x + 7 = (x - 2)^2 + 3$$

$$x^2 + 4x = (x + 2)^2 - 4$$

### The Method

| Step | What To Do |
|---|---|
| **Step 1** | Complete the square on the quadratic |
| **Step 2** | Substitute $u = $ (the bracket), so $\mathrm{d}u = \mathrm{d}x$ |
| **Step 3** | Match the result to a standard form and integrate |
| **Step 4** | Convert back to $x$ |

---

### Example 5 - Medium (completing the square, then $x = a\tan u$)

> **Question:** Using an appropriate substitution, determine the result of $\displaystyle \int \frac{1}{x^2 - 4x + 7}\;\mathrm{d}x$.

**Solution:**

Complete the square:

$$x^2 - 4x + 7 = (x - 2)^2 + 3$$

So the integral is:

$$I = \int \frac{1}{(x - 2)^2 + 3}\;\mathrm{d}x$$

Let $x - 2 = \sqrt{3}\tan u$, so $\mathrm{d}x = \sqrt{3}\sec^2 u\;\mathrm{d}u$:

$$I = \int \frac{\sqrt{3}\sec^2 u}{3 + 3\tan^2 u}\;\mathrm{d}u = \int \frac{\sqrt{3}\sec^2 u}{3\sec^2 u}\;\mathrm{d}u$$

$$I = \int \frac{1}{\sqrt{3}}\;\mathrm{d}u = \frac{1}{\sqrt{3}}u + c$$

Convert back, using $u = \tan^{-1}\!\left(\frac{x - 2}{\sqrt{3}}\right)$:

$$I = \frac{1}{\sqrt{3}}\tan^{-1}\!\left(\frac{x - 2}{\sqrt{3}}\right) + c \quad\checkmark$$

---

### Example 6 - Medium (completing the square, then hyperbolic)

> **Question:** Using a hyperbolic substitution, determine the result of $\displaystyle \int \frac{1}{x^2 + 4x}\;\mathrm{d}x$.

**Solution:**

Complete the square:

$$x^2 + 4x = (x + 2)^2 - 4$$

Let $x + 2 = 2\cosh u$, so $\mathrm{d}x = 2\sinh u\;\mathrm{d}u$:

$$I = \int \frac{2\sinh u}{4\cosh^2 u - 4}\;\mathrm{d}u = \int \frac{2\sinh u}{4\sinh^2 u}\;\mathrm{d}u = \int \frac{1}{2}\operatorname{cosech} u\;\mathrm{d}u$$

This is doable but messy. **Better: recognise the result directly as a standard form:**

$$\int \frac{1}{u^2 - a^2}\;\mathrm{d}u = \frac{1}{2a}\ln\left\lvert \frac{u - a}{u + a} \right\rvert + c$$

So with $u = x + 2$ and $a = 2$:

$$I = \frac{1}{4}\ln\left\lvert \frac{x + 2 - 2}{x + 2 + 2} \right\rvert + c$$

$$I = \frac{1}{4}\ln\left\lvert \frac{x}{x + 4} \right\rvert + c \quad\checkmark$$

> ⭐ **Watch Out!** $\displaystyle \int \frac{1}{x^2 - a^2}\;\mathrm{d}x$ is a standard partial-fractions result: $\displaystyle \frac{1}{2a}\ln\left\lvert \frac{x-a}{x+a} \right\rvert$. Do not reinvent it every time with hyperbolic substitutions - it appears in the formula list and saves you two lines of work.

---

### Example 7 - Easy (complete the square, spot the standard form)

> **Question:** Determine $\displaystyle \int \frac{1}{x^2 + 2x + 2}\;\mathrm{d}x$.

**Solution:**

$$x^2 + 2x + 2 = (x + 1)^2 + 1$$

$$I = \int \frac{1}{(x + 1)^2 + 1}\;\mathrm{d}x$$

This is $\displaystyle \int \frac{1}{u^2 + 1}\;\mathrm{d}u$ with $u = x + 1$, so:

$$I = \tan^{-1}(x + 1) + c \quad\checkmark$$

---

## 1.4 Harder 9709 Techniques Still Examinable in 9231

Cambridge warns: *any 9709 integration technique may appear in a harder form* - specifically **integration by parts on $e^{x}\sin x$/$e^{x}\cos x$ cycles** and the **$t=\tan\frac{x}{2}$ (Weierstrass) substitution**. You already know these from 9709 PM3; here they are in the 9231 context with full LaTeX working.

### The $t=\tan\frac{x}{2}$ Substitution

$$\boxed{t = \tan\frac{x}{2}} \qquad\Longrightarrow\qquad \boxed{\sin x = \frac{2t}{1+t^{2}}},\quad \boxed{\cos x = \frac{1-t^{2}}{1+t^{2}}},\quad \boxed{\mathrm{d}x = \frac{2\,\mathrm{d}t}{1+t^{2}}}$$

Use it when the integrand is rational in $\sin x$ and $\cos x$, especially $\displaystyle \int \frac{1}{a+b\cos x}\,\mathrm{d}x$ or $\displaystyle \int \frac{1}{a+b\sin x}\,\mathrm{d}x$.

| Step | What To Do |
|---|---|
| **Step 1** | Set $t=\tan\frac{x}{2}$, replace $\sin x$, $\cos x$, $\mathrm{d}x$ using the boxes above |
| **Step 2** | Simplify to a rational function in $t$ (often $\int\frac{1}{\text{quadratic in }t}\,\mathrm{d}t$) |
| **Step 3** | Integrate via partial fractions or completing the square + standard form |
| **Step 4** | Convert back: $t=\tan\frac{x}{2}$ (or convert limits if definite) |

### Example 7B - Medium ($t=\tan\frac{x}{2}$)

> **Question:** Find $\displaystyle \int \frac{1}{1+\sin x}\,\mathrm{d}x$.

**Solution:**

Let $t=\tan\frac{x}{2}$, so $\sin x = \frac{2t}{1+t^{2}}$ and $\mathrm{d}x = \frac{2\,\mathrm{d}t}{1+t^{2}}$:

$$I = \int \frac{1}{1+\frac{2t}{1+t^{2}}}\cdot\frac{2\,\mathrm{d}t}{1+t^{2}}$$

$$I = \int \frac{2}{1+t^{2}+2t}\,\mathrm{d}t = \int \frac{2}{(t+1)^{2}}\,\mathrm{d}t$$

$$I = -\frac{2}{t+1}+c$$

Convert back:

$$I = -\frac{2}{\tan\frac{x}{2}+1}+c \quad\checkmark$$

### Example 7C - Medium (harder denominator)

> **Question:** Evaluate $\displaystyle \int \frac{1}{3+2\cos x}\,\mathrm{d}x$.

**Solution:**

Let $t=\tan\frac{x}{2}$, so $\cos x = \frac{1-t^{2}}{1+t^{2}}$:

$$I = \int \frac{1}{3+2\frac{1-t^{2}}{1+t^{2}}}\cdot\frac{2\,\mathrm{d}t}{1+t^{2}}$$

$$I = \int \frac{2}{3(1+t^{2})+2(1-t^{2})}\,\mathrm{d}t = \int \frac{2}{t^{2}+5}\,\mathrm{d}t$$

$$I = \frac{2}{\sqrt{5}}\tan^{-1}\!\left(\frac{t}{\sqrt{5}}\right)+c$$

$$I = \frac{2}{\sqrt{5}}\tan^{-1}\!\left(\frac{\tan\frac{x}{2}}{\sqrt{5}}\right)+c \quad\checkmark$$

### The $e^{x}\sin x$ / $e^{x}\cos x$ Cycle (integration by parts twice)

> **Question:** Find $\displaystyle \int e^{x}\sin x\,\mathrm{d}x$.

Let $I=\int e^{x}\sin x\,\mathrm{d}x$. Integrate by parts ($u=\sin x$, $\mathrm{d}v=e^{x}\mathrm{d}x$):

$$I = e^{x}\sin x - \int e^{x}\cos x\,\mathrm{d}x$$

Again ($u=\cos x$, $\mathrm{d}v=e^{x}\mathrm{d}x$):

$$\int e^{x}\cos x\,\mathrm{d}x = e^{x}\cos x + \int e^{x}\sin x\,\mathrm{d}x = e^{x}\cos x + I$$

So:

$$I = e^{x}\sin x - e^{x}\cos x - I$$

$$2I = e^{x}(\sin x - \cos x)$$

$$I = \frac{e^{x}}{2}(\sin x - \cos x)+c \quad\checkmark$$

> ⭐ **Watch Out!** For $t=\tan\frac{x}{2}$, the $\mathrm{d}x = \frac{2\,\mathrm{d}t}{1+t^{2}}$ factor is the most dropped term. For $e^{x}\sin x$, the second by-parts returns to $I$ with the *opposite* sign - do not lose the minus.

---

### Practice Questions - Part 1

#### Question P1

> Determine $\displaystyle \int \frac{1}{\sqrt{25 - 9x^2}}\;\mathrm{d}x$.

<details>
<summary><strong>Click for Solution</strong></summary>

**Solution:**

This is $\sqrt{a^2 - x^2}$ form with $2x$ style scaling. Let $3x = 5\sin u$, so $3\,\frac{\mathrm{d}x}{\mathrm{d}u} = 5\cos u$, giving $\mathrm{d}x = \frac{5}{3}\cos u\;\mathrm{d}u$:

$$I = \int \frac{\frac{5}{3}\cos u}{\sqrt{25 - 25\sin^2 u}}\;\mathrm{d}u = \int \frac{\frac{5}{3}\cos u}{5\cos u}\;\mathrm{d}u = \int \frac{1}{3}\;\mathrm{d}u$$

$$I = \frac{1}{3}u + c = \frac{1}{3}\sin^{-1}\!\left(\frac{3x}{5}\right) + c \quad\checkmark$$

</details>

#### Question P2

> Evaluate $\displaystyle \int_0^1 \tan^{-1} x\;\mathrm{d}x$, giving your answer in exact form.

<details>
<summary><strong>Click for Solution</strong></summary>

**Solution:**

Integrate by parts with $u = \tan^{-1} x$, $\frac{\mathrm{d}v}{\mathrm{d}x} = 1$, so $\frac{\mathrm{d}u}{\mathrm{d}x} = \frac{1}{1 + x^2}$ and $v = x$:

$$I = \left[x\tan^{-1} x\right]_0^1 - \int_0^1 \frac{x}{1 + x^2}\;\mathrm{d}x$$

$$I = \left[x\tan^{-1} x\right]_0^1 - \frac{1}{2}\left[\ln(1 + x^2)\right]_0^1$$

$$I = \left(\frac{\pi}{4} - 0\right) - \frac{1}{2}\left(\ln 2 - \ln 1\right)$$

$$I = \frac{\pi}{4} - \frac{1}{2}\ln 2 \quad\checkmark$$

</details>

#### Question P3

> Find the area under the curve $y = \sinh 2x$ from $x = \ln 3$ to $x = \ln 5$.

<details>
<summary><strong>Click for Solution</strong></summary>

**Solution:**

$$\text{Area} = \int_{\ln 3}^{\ln 5} \sinh 2x\;\mathrm{d}x = \left[\frac{1}{2}\cosh 2x\right]_{\ln 3}^{\ln 5}$$

$$\text{Area} = \frac{1}{2}\left(\cosh(2\ln 5) - \cosh(2\ln 3)\right)$$

Use $\cosh(2\ln k) = \frac{k^2 + k^{-2}}{2}$:

$$\text{Area} = \frac{1}{2}\left(\frac{25 + \frac{1}{25}}{2} - \frac{9 + \frac{1}{9}}{2}\right) = \frac{1}{4}\left(\frac{626}{25} - \frac{82}{9}\right)$$

$$\text{Area} = \frac{1}{4}\left(\frac{5634 - 2050}{225}\right) = \frac{1}{4}\left(\frac{3584}{225}\right)$$

$$\text{Area} = \frac{896}{225} \approx 3.982 \quad\checkmark$$

</details>

---

# PART 2: Hyperbolic Functions in Integration

## 2.1 The Standard Hyperbolic Integrals

Every hyperbolic derivative from Chapter 21 reverses into an integral. Note the signs carefully - especially that $\cosh$ differentiates to $+\sinh$ (NO minus sign):

| Integral | Result |
|---|---|
| $\displaystyle \int \sinh x\;\mathrm{d}x$ | $\cosh x + c$ |
| $\displaystyle \int \cosh x\;\mathrm{d}x$ | $\sinh x + c$ |
| $\displaystyle \int \tanh x\;\mathrm{d}x$ | $\ln(\cosh x) + c$ |
| $\displaystyle \int \coth x\;\mathrm{d}x$ | $\ln\lvert \sinh x \rvert + c$ |
| $\displaystyle \int \operatorname{sech}^2 x\;\mathrm{d}x$ | $\tanh x + c$ |
| $\displaystyle \int \operatorname{cosech}^2 x\;\mathrm{d}x$ | $-\coth x + c$ |
| $\displaystyle \int \operatorname{sech} x \tanh x\;\mathrm{d}x$ | $-\operatorname{sech} x + c$ |
| $\displaystyle \int \operatorname{cosech} x \coth x\;\mathrm{d}x$ | $-\operatorname{cosech} x + c$ |

**Where $\tanh x$ and $\coth x$ come from:** they are $\frac{f'(x)}{f(x)}$ forms:

$$\int \tanh x\;\mathrm{d}x = \int \frac{\sinh x}{\cosh x}\;\mathrm{d}x = \ln(\cosh x) + c$$

$$\int \coth x\;\mathrm{d}x = \int \frac{\cosh x}{\sinh x}\;\mathrm{d}x = \ln\lvert \sinh x \rvert + c$$

---

### Example 8 - Easy (reverse chain rule)

> **Question:** Find a solution for the following integrals:
> a) $\displaystyle \int \sinh 3x\;\mathrm{d}x$  b) $\displaystyle \int 3\cosh 4x\;\mathrm{d}x$

**Solution (a):**

The derivative of $\cosh 3x$ is $3\sinh 3x$, so divide by 3:

$$\int \sinh 3x\;\mathrm{d}x = \frac{1}{3}\cosh 3x + c \quad\checkmark$$

**Solution (b):**

The derivative of $\sinh 4x$ is $4\cosh 4x$, so:

$$\int 3\cosh 4x\;\mathrm{d}x = \frac{3}{4}\sinh 4x + c \quad\checkmark$$

---

### Example 9 - Medium (definite integral with hyperbolic limits)

> **Question:** Evaluate $\displaystyle \int_{\ln 2}^{\ln 3} 3\cosh 4x\;\mathrm{d}x$.

**Solution:**

$$I = \frac{3}{4}\left[\sinh 4x\right]_{\ln 2}^{\ln 3}$$

$$I = \frac{3}{4}\left(\sinh(4\ln 3) - \sinh(4\ln 2)\right)$$

Use $\sinh(k\ln a) = \frac{a^k - a^{-k}}{2}$:

$$I = \frac{3}{4}\left(\frac{3^4 - 3^{-4}}{2} - \frac{2^4 - 2^{-4}}{2}\right)$$

$$I = \frac{3}{8}\left(81 - \frac{1}{81} - 16 + \frac{1}{16}\right)$$

$$I = \frac{3}{8}\left(65 - \frac{1}{81} + \frac{1}{16}\right)$$

$$I = \frac{3}{8}\left(65 - 0.0123 + 0.0625\right) = \frac{3}{8}(65.0502) = 24.394 \approx 24.4 \quad\checkmark$$

---

### Example 10 - Medium (exponential substitution, then partial fractions)

> **Question:** Evaluate $\displaystyle \int_{\ln 2}^{\ln 3} \frac{1}{\sinh x}\;\mathrm{d}x$.

**Solution:**

Rewrite $\sinh x$ in exponential form:

$$I = \int_{\ln 2}^{\ln 3} \frac{2}{e^x - e^{-x}}\;\mathrm{d}x$$

Let $u = e^x$, so $\frac{\mathrm{d}u}{\mathrm{d}x} = e^x = u$, giving $\mathrm{d}x = \frac{\mathrm{d}u}{u}$:

$$I = \int \frac{2}{u - \frac{1}{u}} \cdot \frac{\mathrm{d}u}{u}$$

Simplify the denominator and cancel the $u$:

$$\frac{2}{u - \frac{1}{u}} \cdot \frac{1}{u} = \frac{2}{u^2 - 1}$$

$$I = \int \frac{2}{u^2 - 1}\;\mathrm{d}u = \int \left(\frac{1}{u - 1} - \frac{1}{u + 1}\right)\mathrm{d}u$$

$$I = \ln\lvert u - 1 \rvert - \ln\lvert u + 1 \rvert + c = \ln\left\lvert \frac{u - 1}{u + 1} \right\rvert + c$$

Convert back: $u = e^x$:

$$I = \left[\ln\left\lvert \frac{e^x - 1}{e^x + 1} \right\rvert\right]_{\ln 2}^{\ln 3}$$

$$I = \ln\left(\frac{3 - 1}{3 + 1}\right) - \ln\left(\frac{2 - 1}{2 + 1}\right) = \ln\left(\frac{1}{2}\right) - \ln\left(\frac{1}{3}\right)$$

$$I = \ln\left(\frac{\frac{1}{2}}{\frac{1}{3}}\right) = \ln\left(\frac{3}{2}\right) \approx 0.405 \quad\checkmark$$

> 💡 **Note:** the antiderivative $\ln\left\lvert \frac{e^x - 1}{e^x + 1} \right\rvert$ is exactly $\ln\lvert \tanh(\frac{x}{2}) \rvert$, since $\tanh(\frac{x}{2}) = \frac{e^x - 1}{e^x + 1}$. The coursebook reaches the same answer via a second substitution ($w = \coth t$), giving $-2\coth^{-1}(e^x) + c$ - both forms are equivalent.

---

## 2.2 Integrating Inverse Hyperbolic Functions - The "1 Times" Trick

To integrate an inverse function like $\cosh^{-1} x$ or $\tan^{-1} x$, there is no direct standard integral. Instead, **multiply by 1** and use integration by parts with $\frac{\mathrm{d}v}{\mathrm{d}x} = 1$:

### The Method

| Step | What To Do |
|---|---|
| **Step 1** | Write the inverse function as $\text{(inverse function)} \times 1$ |
| **Step 2** | Let $u = \text{inverse function}$, $\frac{\mathrm{d}v}{\mathrm{d}x} = 1$, so $v = x$ |
| **Step 3** | Differentiate $u$ (you know these derivatives from Chapter 21) |
| **Step 4** | Apply integration by parts - the leftover integral is a standard form |
| **Step 5** | Integrate the leftover and simplify |

### The Three Results You Will Get

$$\int \cosh^{-1} x\;\mathrm{d}x = x\cosh^{-1} x - \sqrt{x^2 - 1} + c$$

$$\int \tanh^{-1} x\;\mathrm{d}x = x\tanh^{-1} x + \frac{1}{2}\ln\lvert 1 - x^2 \rvert + c$$

$$\int \tan^{-1} x\;\mathrm{d}x = x\tan^{-1} x - \frac{1}{2}\ln(1 + x^2) + c$$

---

### Example 11 - Medium (integrating $\cosh^{-1} x$)

> **Question:** Determine the result of $\displaystyle \int \cosh^{-1} x\;\mathrm{d}x$.

**Solution:**

Re-write as $\cosh^{-1} x \times 1$ and let $u = \cosh^{-1} x$, $\frac{\mathrm{d}v}{\mathrm{d}x} = 1$:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = \frac{1}{\sqrt{x^2 - 1}}, \qquad v = x$$

Apply integration by parts:

$$I = x\cosh^{-1} x - \int \frac{x}{\sqrt{x^2 - 1}}\;\mathrm{d}x$$

The leftover is a reverse chain rule - the derivative of $\sqrt{x^2 - 1}$ is $\frac{x}{\sqrt{x^2 - 1}}$:

$$\int \frac{x}{\sqrt{x^2 - 1}}\;\mathrm{d}x = \sqrt{x^2 - 1} + c$$

$$I = x\cosh^{-1} x - \sqrt{x^2 - 1} + c \quad\checkmark$$

---

### Example 12 - Medium (integrating $\tanh^{-1} x$)

> **Question:** Determine the result of $\displaystyle \int \tanh^{-1} x\;\mathrm{d}x$.

**Solution:**

Let $u = \tanh^{-1} x$, $\frac{\mathrm{d}v}{\mathrm{d}x} = 1$:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = \frac{1}{1 - x^2}, \qquad v = x$$

$$I = x\tanh^{-1} x - \int \frac{x}{1 - x^2}\;\mathrm{d}x$$

The leftover is of the form $\frac{f'(x)}{f(x)}$ (up to a constant factor): the derivative of $1 - x^2$ is $-2x$:

$$\int \frac{x}{1 - x^2}\;\mathrm{d}x = -\frac{1}{2}\ln\lvert 1 - x^2 \rvert + c$$

$$I = x\tanh^{-1} x + \frac{1}{2}\ln\lvert 1 - x^2 \rvert + c \quad\checkmark$$

---

### Example 13 - Easy (integrating $\tan^{-1} x$ - same trick, trig version)

> **Question:** Determine the result of $\displaystyle \int \tan^{-1} x\;\mathrm{d}x$.

**Solution:**

Let $u = \tan^{-1} x$, $\frac{\mathrm{d}v}{\mathrm{d}x} = 1$:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = \frac{1}{1 + x^2}, \qquad v = x$$

$$I = x\tan^{-1} x - \int \frac{x}{1 + x^2}\;\mathrm{d}x$$

$$I = x\tan^{-1} x - \frac{1}{2}\ln(1 + x^2) + c \quad\checkmark$$

---

### Practice Questions - Part 2

#### Question P4

> Evaluate $\displaystyle \int_{0.75}^1 \coth 2x\;\mathrm{d}x$, giving your answer correct to 3 significant figures.

<details>
<summary><strong>Click for Solution</strong></summary>

**Solution:**

$\coth 2x$ is $\frac{f'(x)}{f(x)}$ form: the derivative of $\sinh 2x$ is $2\cosh 2x$, so:

$$\int \coth 2x\;\mathrm{d}x = \frac{1}{2}\ln\lvert \sinh 2x \rvert + c$$

$$I = \frac{1}{2}\left[\ln(\sinh 2x)\right]_{0.75}^1$$

$$I = \frac{1}{2}\left(\ln(\sinh 2) - \ln(\sinh 1.5)\right) = \frac{1}{2}\ln\left(\frac{\sinh 2}{\sinh 1.5}\right)$$

$$I = \frac{1}{2}\ln\left(\frac{3.6269}{2.1293}\right) = \frac{1}{2}\ln(1.7033) = 0.2663 \approx 0.266 \quad\checkmark$$

</details>

#### Question P5

> Integrate $x\cosh x$.

<details>
<summary><strong>Click for Solution</strong></summary>

**Solution:**

Integration by parts with $u = x$, $\frac{\mathrm{d}v}{\mathrm{d}x} = \cosh x$, so $\frac{\mathrm{d}u}{\mathrm{d}x} = 1$ and $v = \sinh x$:

$$\int x\cosh x\;\mathrm{d}x = x\sinh x - \int 1 \cdot \sinh x\;\mathrm{d}x$$

$$\int x\cosh x\;\mathrm{d}x = x\sinh x - \cosh x + c \quad\checkmark$$

</details>

#### Question P6

> Determine the integral $\displaystyle \int \frac{1}{\sqrt{2 + x^2}}\;\mathrm{d}x$.

<details>
<summary><strong>Click for Solution</strong></summary>

**Solution:**

This is $\sqrt{x^2 + a^2}$ form with $a = \sqrt{2}$:

$$\int \frac{1}{\sqrt{x^2 + a^2}}\;\mathrm{d}x = \sinh^{-1}\!\left(\frac{x}{a}\right) + c$$

$$I = \sinh^{-1}\!\left(\frac{x}{\sqrt{2}}\right) + c \quad\checkmark$$

</details>

---
# PART 3: Reduction Formulae

## 3.1 What Is a Reduction Formula?

A **reduction formula** expresses an integral $I_n$ (which contains a power $n$) in terms of $I_{n-2}$ (or $I_{n-1}$) - an integral of the SAME form but with a lower power. Each application drops the power, so after enough steps you reach a base case you can do directly ($I_0$ or $I_1$).

**Why they exist:** powers like $\cos^7 x$ or $x^{10}e^x$ are brutal to integrate directly. A reduction formula turns "integrate the 7th power" into "apply the formula three times, then integrate $\cos x$".

### The General Method

| Step | What To Do |
|---|---|
| **Step 1** | Split the power: $\cos^n x = \cos^{n-1} x \cdot \cos x$ (single power integrated, high power differentiated) |
| **Step 2** | Integration by parts with $u = $ high power, $\frac{\mathrm{d}v}{\mathrm{d}x} = $ single power |
| **Step 3** | Use a Pythagorean identity ($\sin^2 x = 1 - \cos^2 x$, $\cosh^2 x = 1 + \sinh^2 x$, etc.) to eliminate the NEW power |
| **Step 4** | Rearrange so only $I_n$ and $I_{n-2}$ (or $I_{n-1}$) appear - collect like terms |
| **Step 5** | State the formula AND its validity range (usually $n \geq 2$) |

---

## 3.2 The Trig Power Formula: $I_n = \int \cos^n x\;\mathrm{d}x$

### The Result

$$I_n = \frac{1}{n}\cos^{n-1} x \sin x + \frac{n - 1}{n} I_{n-2}, \qquad n \geq 2$$

---

### Example 14 - Medium (deriving the reduction formula for $\cos^n x$)

> **Question:** Given that $I_n = \int \cos^n x\;\mathrm{d}x$, use integration by parts to find a reduction formula for $I_n$.

**Solution:**

Split the power:

$$I_n = \int \cos^{n-1} x \cdot \cos x\;\mathrm{d}x$$

Let $u = \cos^{n-1} x$, $\frac{\mathrm{d}v}{\mathrm{d}x} = \cos x$, so:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = -(n-1)\cos^{n-2} x \sin x, \qquad v = \sin x$$

Apply integration by parts:

$$I_n = \cos^{n-1} x \sin x + (n-1)\int \cos^{n-2} x \sin^2 x\;\mathrm{d}x$$

Use $\sin^2 x = 1 - \cos^2 x$:

$$I_n = \cos^{n-1} x \sin x + (n-1)\int \cos^{n-2} x\;\mathrm{d}x - (n-1)\int \cos^n x\;\mathrm{d}x$$

$$I_n = \cos^{n-1} x \sin x + (n-1)I_{n-2} - (n-1)I_n$$

Collect $I_n$ terms:

$$I_n + (n-1)I_n = \cos^{n-1} x \sin x + (n-1)I_{n-2}$$

$$nI_n = \cos^{n-1} x \sin x + (n-1)I_{n-2}$$

$$I_n = \frac{1}{n}\cos^{n-1} x \sin x + \frac{n - 1}{n} I_{n-2}, \qquad n \geq 2 \quad\checkmark$$

---

### Example 15 - Medium (using the formula: $I_3$ and $I_4$)

> **Question:** Using the reduction formula, find $\displaystyle \int \cos^3 x\;\mathrm{d}x$ and $\displaystyle \int \cos^4 x\;\mathrm{d}x$.

**Solution - $\cos^3 x$ (n = 3):**

$$I_3 = \frac{1}{3}\cos^2 x \sin x + \frac{2}{3}I_1$$

$$I_1 = \int \cos x\;\mathrm{d}x = \sin x$$

$$I_3 = \frac{1}{3}\cos^2 x \sin x + \frac{2}{3}\sin x + c$$

$$I_3 = \frac{1}{3}\left(\cos^2 x \sin x + 2\sin x\right) + c \quad\checkmark$$

**Solution - $\cos^4 x$ (n = 4):**

$$I_4 = \frac{1}{4}\cos^3 x \sin x + \frac{3}{4}I_2$$

$$I_2 = \frac{1}{2}\cos x \sin x + \frac{1}{2}I_0$$

$$I_0 = \int 1\;\mathrm{d}x = x$$

$$I_2 = \frac{1}{2}\cos x \sin x + \frac{1}{2}x$$

$$I_4 = \frac{1}{4}\cos^3 x \sin x + \frac{3}{4}\left(\frac{1}{2}\cos x \sin x + \frac{1}{2}x\right) + c$$

$$I_4 = \frac{1}{4}\cos^3 x \sin x + \frac{3}{8}\cos x \sin x + \frac{3}{8}x + c \quad\checkmark$$

> ⭐ **Watch Out!** Check the base cases: for even powers you walk down to $I_0 = x$; for odd powers down to $I_1 = \sin x$. NEVER mix them up - if $n$ is even, $I_{n-2}$ is even all the way to $I_0$; if odd, down to $I_1$.

---

## 3.3 The Sine Version: $I_n = \int \sin^n x\;\mathrm{d}x$

### The Result

$$I_n = -\frac{1}{n}\cos x \sin^{n-1} x + \frac{n - 1}{n} I_{n-2}, \qquad n \geq 2$$

The working mirrors the cosine version, using $\cos^2 x = 1 - \sin^2 x$.

---

### Example 16 - Medium (deriving the $\sin^n x$ formula)

> **Question:** If $I_n = \int \sin^n x\;\mathrm{d}x$, show, using integration by parts, that $\displaystyle I_n = \frac{1}{n}\left(-\cos x \sin^{n-1} x\right) + \frac{n-1}{n}I_{n-2}$ for $n \geq 2$.

**Solution:**

$$I_n = \int \sin^{n-1} x \cdot \sin x\;\mathrm{d}x$$

Let $u = \sin^{n-1} x$, $\frac{\mathrm{d}v}{\mathrm{d}x} = \sin x$, so:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = (n-1)\sin^{n-2} x \cos x, \qquad v = -\cos x$$

$$I_n = \left[-\cos x \sin^{n-1} x\right] + (n-1)\int \sin^{n-2} x \cos^2 x\;\mathrm{d}x$$

Use $\cos^2 x = 1 - \sin^2 x$:

$$I_n = -\cos x \sin^{n-1} x + (n-1)\int \sin^{n-2} x\;\mathrm{d}x - (n-1)\int \sin^n x\;\mathrm{d}x$$

$$I_n = -\cos x \sin^{n-1} x + (n-1)I_{n-2} - (n-1)I_n$$

$$nI_n = -\cos x \sin^{n-1} x + (n-1)I_{n-2}$$

$$I_n = -\frac{1}{n}\cos x \sin^{n-1} x + \frac{n - 1}{n} I_{n-2}, \qquad n \geq 2 \quad\checkmark$$

---

### Example 17 - Hard (applying to a definite integral)

> **Question:** Using the reduction formula, evaluate $\displaystyle \int_0^{\pi/2} \sin^5 x\;\mathrm{d}x$.

**Solution:**

$$I_5 = -\frac{1}{5}\left[\cos x \sin^4 x\right]_0^{\pi/2} + \frac{4}{5}I_3$$

At $x = \frac{\pi}{2}$: $\cos x = 0$, so the bracket term vanishes:

$$I_5 = \frac{4}{5}I_3$$

$$I_3 = -\frac{1}{3}\left[\cos x \sin^2 x\right]_0^{\pi/2} + \frac{2}{3}I_1 = \frac{2}{3}I_1$$

$$I_1 = \int_0^{\pi/2} \sin x\;\mathrm{d}x = \left[-\cos x\right]_0^{\pi/2} = 1$$

$$I_5 = \frac{4}{5} \cdot \frac{2}{3} \cdot 1 = \frac{8}{15} \approx 0.5333 \quad\checkmark$$

> 💡 **Handy shortcut:** for $0$ to $\frac{\pi}{2}$, the bracket terms ALWAYS vanish, so $I_n = \frac{n-1}{n}I_{n-2}$ and $\displaystyle \int_0^{\pi/2}\sin^n x\;\mathrm{d}x = \frac{(n-1)(n-3)\cdots}{n(n-2)\cdots} \times (\text{base case})$. This is the Wallis-type shortcut.

---

## 3.4 Hyperbolic Powers: $\cosh^n 2x$ and $\coth^n x$

The same splitting idea works on hyperbolic functions. Two classic results:

$$I_n = \int \cosh^n 2x\;\mathrm{d}x: \qquad I_n = \frac{1}{2n}\sinh 2x \cosh^{n-1} 2x + \frac{n-1}{n}I_{n-2}, \quad n \geq 2$$

$$I_n = \int \coth^n x\;\mathrm{d}x: \qquad I_n = -\frac{1}{n-1}\coth^{n-1} x + I_{n-2}, \quad n \geq 2$$

---

### Example 18 - Hard (deriving the $\coth^n x$ formula)

> **Question:** If $I_n = \int \coth^n x\;\mathrm{d}x$, show that $\displaystyle I_n = -\frac{1}{n-1}\coth^{n-1} x + I_{n-2}$ for $n \geq 2$.

**Solution:**

Split the power and use $\coth^2 x = 1 + \operatorname{cosech}^2 x$:

$$I_n = \int \coth^{n-2} x \cdot \coth^2 x\;\mathrm{d}x = \int \coth^{n-2} x\;\mathrm{d}x + \int \coth^{n-2} x \operatorname{cosech}^2 x\;\mathrm{d}x$$

The first integral is just $I_{n-2}$:

$$I_n = I_{n-2} + \int \coth^{n-2} x \operatorname{cosech}^2 x\;\mathrm{d}x$$

For the second, use the reverse chain rule: the derivative of $\coth x$ is $-\operatorname{cosech}^2 x$, so:

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(\coth^{n-1} x\right) = -(n-1)\coth^{n-2} x \operatorname{cosech}^2 x$$

$$I_n = I_{n-2} - \frac{1}{n-1}\coth^{n-1} x$$

$$I_n = -\frac{1}{n-1}\coth^{n-1} x + I_{n-2}, \qquad n \geq 2 \quad\checkmark$$

---

## 3.5 Algebraic Powers: $I_n = \int x^n e^x\;\mathrm{d}x$ and $I_n = \int x^n \sqrt{x^2 - 1}\;\mathrm{d}x$

For powers of $x$ times a simple function, differentiate the $x^n$ and integrate the rest - the power of $x$ drops by 1 each time.

$$I_n = \int x^n e^x\;\mathrm{d}x: \qquad I_n = x^n e^x - nI_{n-1}, \quad n \geq 1$$

---

### Example 19 - Medium (the $x^n e^x$ chain)

> **Question:** Given $I_n = \int x^n e^x\;\mathrm{d}x$, derive the reduction formula and hence find $I_4$.

**Solution:**

Let $u = x^n$, $\frac{\mathrm{d}v}{\mathrm{d}x} = e^x$, so $\frac{\mathrm{d}u}{\mathrm{d}x} = nx^{n-1}$ and $v = e^x$:

$$I_n = x^n e^x - n\int x^{n-1} e^x\;\mathrm{d}x$$

The leftover integral is $I_{n-1}$:

$$I_n = x^n e^x - nI_{n-1}, \qquad n \geq 1 \quad\checkmark$$

Now cascade down:

$$I_4 = x^4 e^x - 4I_3$$

$$I_3 = x^3 e^x - 3I_2$$

$$I_2 = x^2 e^x - 2I_1$$

$$I_1 = x e^x - I_0$$

$$I_0 = \int e^x\;\mathrm{d}x = e^x$$

Substitute back up:

$$I_4 = x^4 e^x - 4x^3 e^x + 12x^2 e^x - 24x e^x + 24e^x + c$$

$$I_4 = \left(x^4 - 4x^3 + 12x^2 - 24x + 24\right)e^x + c \quad\checkmark$$

---

### Example 20 - Hard (the $x^n\sqrt{x^2 - 1}$ formula)

> **Question:** If $I_n = \int x^n \sqrt{x^2 - 1}\;\mathrm{d}x$, show, using integration by parts, that $\displaystyle I_n = \frac{x^{n-1}(x^2 - 1)^{3/2}}{n + 2} + \frac{n - 1}{n + 2}I_{n-2}$ for $n \geq 2$.

**Solution:**

Let $u = x^{n-1}$, $\frac{\mathrm{d}v}{\mathrm{d}x} = x\sqrt{x^2 - 1}$, so $\frac{\mathrm{d}u}{\mathrm{d}x} = (n-1)x^{n-2}$ and (reverse chain rule) $v = \frac{1}{3}(x^2 - 1)^{3/2}$:

$$I_n = \frac{x^{n-1}}{3}(x^2 - 1)^{3/2} - \frac{n-1}{3}\int x^{n-2}(x^2 - 1)^{3/2}\;\mathrm{d}x$$

Write $(x^2 - 1)^{3/2} = (x^2 - 1)\sqrt{x^2 - 1}$ to bring back $I_n$ and $I_{n-2}$:

$$I_n = \frac{x^{n-1}}{3}(x^2 - 1)^{3/2} - \frac{n-1}{3}\int x^{n-2}(x^2 - 1)\sqrt{x^2 - 1}\;\mathrm{d}x$$

$$I_n = \frac{x^{n-1}}{3}(x^2 - 1)^{3/2} - \frac{n-1}{3}\int x^n\sqrt{x^2 - 1}\;\mathrm{d}x + \frac{n-1}{3}\int x^{n-2}\sqrt{x^2 - 1}\;\mathrm{d}x$$

$$I_n = \frac{x^{n-1}}{3}(x^2 - 1)^{3/2} - \frac{n-1}{3}I_n + \frac{n-1}{3}I_{n-2}$$

Collect $I_n$ terms:

$$\frac{n+2}{3}I_n = \frac{x^{n-1}}{3}(x^2 - 1)^{3/2} + \frac{n-1}{3}I_{n-2}$$

$$I_n = \frac{x^{n-1}(x^2 - 1)^{3/2}}{n + 2} + \frac{n - 1}{n + 2}I_{n-2}, \qquad n \geq 2 \quad\checkmark$$

---

## 3.6 Definite Reduction Formulae: $\tan^n x$ and $x^n \cos x$

For definite integrals, apply the reduction FIRST, then substitute limits - the bracket terms often simplify or vanish.

$$I_n = \int_0^{\pi/4} \tan^n x\;\mathrm{d}x: \qquad I_n = \frac{1}{n-1} - I_{n-2}, \quad n \geq 2$$

$$I_n = \int_0^{\pi/2} x^n \cos x\;\mathrm{d}x: \qquad I_n = \left(\frac{\pi}{2}\right)^n - n(n-1)I_{n-2}, \quad n \geq 2$$

---

### Example 21 - Hard (definite $\tan^n x$)

> **Question:** Find a reduction formula for $I_n = \int_0^{\pi/4} \tan^n x\;\mathrm{d}x$ and hence evaluate $I_4$.

**Solution:**

Split the power using $\tan^2 x = \sec^2 x - 1$:

$$I_n = \int_0^{\pi/4} \tan^{n-2} x \cdot \tan^2 x\;\mathrm{d}x = \int_0^{\pi/4} \tan^{n-2} x\sec^2 x\;\mathrm{d}x - \int_0^{\pi/4} \tan^{n-2} x\;\mathrm{d}x$$

The first integral is a reverse chain rule (derivative of $\tan x$ is $\sec^2 x$):

$$\int \tan^{n-2} x \sec^2 x\;\mathrm{d}x = \frac{\tan^{n-1} x}{n-1}$$

$$I_n = \left[\frac{\tan^{n-1} x}{n-1}\right]_0^{\pi/4} - I_{n-2}$$

$$\tan\frac{\pi}{4} = 1, \qquad \tan 0 = 0$$

$$I_n = \frac{1}{n-1} - I_{n-2}, \qquad n \geq 2 \quad\checkmark$$

Now evaluate $I_4$:

$$I_4 = \frac{1}{3} - I_2$$

$$I_2 = \frac{1}{1} - I_0 = 1 - \frac{\pi}{4}$$

$$I_4 = \frac{1}{3} - \left(1 - \frac{\pi}{4}\right) = \frac{1}{3} - 1 + \frac{\pi}{4}$$

$$I_4 = \frac{\pi}{4} - \frac{2}{3} \approx 0.1187 \quad\checkmark$$

---

### Example 22 - Hard (definite $x^n \cos x$ - the double by-parts)

> **Question:** Show that $I_n = \int_0^{\pi/2} x^n \cos x\;\mathrm{d}x$ satisfies $\displaystyle I_n = \left(\frac{\pi}{2}\right)^n - n(n-1)I_{n-2}$ for $n \geq 2$. Hence find the exact value of $\int_0^{\pi/2} x^3 \cos x\;\mathrm{d}x$.

**Solution:**

Let $u = x^n$, $\frac{\mathrm{d}v}{\mathrm{d}x} = \cos x$, so $\frac{\mathrm{d}u}{\mathrm{d}x} = nx^{n-1}$ and $v = \sin x$:

$$I_n = \left[x^n \sin x\right]_0^{\pi/2} - n\int_0^{\pi/2} x^{n-1}\sin x\;\mathrm{d}x$$

$$I_n = \left(\frac{\pi}{2}\right)^n - n\int_0^{\pi/2} x^{n-1}\sin x\;\mathrm{d}x$$

Integrate by parts again: $u = x^{n-1}$, $\frac{\mathrm{d}v}{\mathrm{d}x} = \sin x$, so $\frac{\mathrm{d}u}{\mathrm{d}x} = (n-1)x^{n-2}$ and $v = -\cos x$:

$$\int_0^{\pi/2} x^{n-1}\sin x\;\mathrm{d}x = \left[-x^{n-1}\cos x\right]_0^{\pi/2} + (n-1)\int_0^{\pi/2} x^{n-2}\cos x\;\mathrm{d}x$$

The bracket vanishes at both ends, and the leftover is $I_{n-2}$:

$$I_n = \left(\frac{\pi}{2}\right)^n - n(n-1)I_{n-2}, \qquad n \geq 2 \quad\checkmark$$

Now for $I_3$:

$$I_3 = \left(\frac{\pi}{2}\right)^3 - 3 \cdot 2 \cdot I_1$$

$$I_1 = \int_0^{\pi/2} x\cos x\;\mathrm{d}x = \left[x\sin x + \cos x\right]_0^{\pi/2} = \frac{\pi}{2} - 1$$

$$I_3 = \frac{\pi^3}{8} - 6\left(\frac{\pi}{2} - 1\right) = \frac{\pi^3}{8} - 3\pi + 6 \approx 0.451 \quad\checkmark$$

---

### Practice Questions - Part 3

#### Question P7

> Given that $I_n = \int \sin^n 2x\;\mathrm{d}x$, find a reduction formula for $I_n$, stating the values of $n$ for which it is valid.

<details>
<summary><strong>Click for Solution</strong></summary>

**Solution:**

$$I_n = \int \sin^{n-1} 2x \cdot \sin 2x\;\mathrm{d}x$$

Let $u = \sin^{n-1} 2x$, $\frac{\mathrm{d}v}{\mathrm{d}x} = \sin 2x$, so:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = 2(n-1)\sin^{n-2} 2x \cos 2x, \qquad v = -\frac{1}{2}\cos 2x$$

$$I_n = -\frac{1}{2}\cos 2x \sin^{n-1} 2x + (n-1)\int \sin^{n-2} 2x \cos^2 2x\;\mathrm{d}x$$

Use $\cos^2 2x = 1 - \sin^2 2x$:

$$I_n = -\frac{1}{2}\cos 2x \sin^{n-1} 2x + (n-1)I_{n-2} - (n-1)I_n$$

$$I_n = -\frac{1}{2n}\cos 2x \sin^{n-1} 2x + \frac{n-1}{n}I_{n-2}, \qquad n \geq 2 \quad\checkmark$$

</details>

#### Question P8

> Given that $I_n = \int x^5 e^x\;\mathrm{d}x$, find a relationship between $I_8$ and $I_7$ (write down the general formula and apply it once).

<details>
<summary><strong>Click for Solution</strong></summary>

**Solution:**

The general formula is $I_n = x^n e^x - nI_{n-1}$, so:

$$I_8 = x^8 e^x - 8I_7 \quad\checkmark$$

</details>

#### Question P9

> You are given that $I_n = \int_0^1 x(1 - 2x^4)^n\;\mathrm{d}x$.
> a) Show that $\displaystyle I_n = \frac{(-1)^n}{4n + 2} + \frac{2n}{2n + 1}I_{n-1}$ for $n \geq 1$.
> b) Find the exact value of $I_3$.

<details>
<summary><strong>Click for Solution</strong></summary>

**Solution (a):**

Integration by parts with $u = (1 - 2x^4)^n$, $\frac{\mathrm{d}v}{\mathrm{d}x} = x$:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = -8nx^3(1 - 2x^4)^{n-1}, \qquad v = \frac{x^2}{2}$$

$$I_n = \left[\frac{x^2}{2}(1 - 2x^4)^n\right]_0^1 + 4n\int_0^1 x^5(1 - 2x^4)^{n-1}\;\mathrm{d}x$$

At $x = 1$: $\frac{1}{2}(1 - 2)^n = \frac{(-1)^n}{2}$, and the $x = 0$ term is 0:

$$I_n = \frac{(-1)^n}{2} + 4n\int_0^1 x^5(1 - 2x^4)^{n-1}\;\mathrm{d}x$$

Write $x^5 = x \cdot x^4 = x \cdot \frac{1 - (1 - 2x^4)}{2}$:

$$\int_0^1 x^5(1 - 2x^4)^{n-1}\;\mathrm{d}x = \frac{1}{2}\int_0^1 x(1 - 2x^4)^{n-1}\;\mathrm{d}x - \frac{1}{2}\int_0^1 x(1 - 2x^4)^n\;\mathrm{d}x$$

$$= \frac{1}{2}I_{n-1} - \frac{1}{2}I_n$$

Substitute back:

$$I_n = \frac{(-1)^n}{2} + 4n\left(\frac{1}{2}I_{n-1} - \frac{1}{2}I_n\right)$$

$$I_n = \frac{(-1)^n}{2} + 2nI_{n-1} - 2nI_n$$

Collect $I_n$ terms:

$$(2n + 1)I_n = \frac{(-1)^n}{2} + 2nI_{n-1}$$

$$I_n = \frac{(-1)^n}{2(2n + 1)} + \frac{2n}{2n + 1}I_{n-1} = \frac{(-1)^n}{4n + 2} + \frac{2n}{2n + 1}I_{n-1}, \qquad n \geq 1 \quad\checkmark$$

**Solution (b):**

Walk down the formula:

$$I_0 = \int_0^1 x\;\mathrm{d}x = \frac{1}{2}$$

$$I_1 = \frac{(-1)^1}{4 + 2} + \frac{2}{3}I_0 = -\frac{1}{6} + \frac{2}{3}\cdot\frac{1}{2} = -\frac{1}{6} + \frac{1}{3} = \frac{1}{6}$$

$$I_2 = \frac{(-1)^2}{8 + 2} + \frac{4}{5}I_1 = \frac{1}{10} + \frac{4}{5}\cdot\frac{1}{6} = \frac{1}{10} + \frac{2}{15} = \frac{3}{30} + \frac{4}{30} = \frac{7}{30}$$

$$I_3 = \frac{(-1)^3}{12 + 2} + \frac{6}{7}I_2 = -\frac{1}{14} + \frac{6}{7}\cdot\frac{7}{30} = -\frac{1}{14} + \frac{1}{5} = \frac{-5 + 14}{70} = \frac{9}{70}$$

$$I_3 = \frac{9}{70} \approx 0.1286 \quad\checkmark$$

</details>

---

# PART 4: Arc Lengths (Cartesian, Parametric, Polar)

## 4.1 The Three Arc Length Formulas

**Cartesian form** (curve $y = f(x)$, from $x = a$ to $x = b$):

$$s = \int_a^b \sqrt{1 + \left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2}\;\mathrm{d}x$$

**Parametric form** (curve $x = x(t)$, $y = y(t)$, from $t = t_1$ to $t = t_2$):

$$s = \int_{t_1}^{t_2} \sqrt{\left(\frac{\mathrm{d}x}{\mathrm{d}t}\right)^2 + \left(\frac{\mathrm{d}y}{\mathrm{d}t}\right)^2}\;\mathrm{d}t$$

**Polar form** (curve $r = f(\theta)$, from $\theta = \alpha$ to $\theta = \beta$):

$$s = \int_{\alpha}^{\beta} \sqrt{r^2 + \left(\frac{\mathrm{d}r}{\mathrm{d}\theta}\right)^2}\;\mathrm{d}\theta$$

### Where They Come From

All three come from the same idea: a tiny arc of length $\delta s$ is (approximately) a straight line, so by Pythagoras:

$$(\delta s)^2 = (\delta x)^2 + (\delta y)^2$$

**Cartesian:** divide by $(\delta x)^2$, then $\delta x \to 0$:

$$\left(\frac{\mathrm{d}s}{\mathrm{d}x}\right)^2 = 1 + \left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2$$

**Parametric:** divide by $(\delta t)^2$, then $\delta t \to 0$:

$$\left(\frac{\mathrm{d}s}{\mathrm{d}t}\right)^2 = \left(\frac{\mathrm{d}x}{\mathrm{d}t}\right)^2 + \left(\frac{\mathrm{d}y}{\mathrm{d}t}\right)^2$$

**Polar:** for a small angle $\delta\theta$, the arc is approximately a sector: $(\delta s)^2 = (\delta r)^2 + (r\,\delta\theta)^2$, so:

$$\left(\frac{\mathrm{d}s}{\mathrm{d}\theta}\right)^2 = \left(\frac{\mathrm{d}r}{\mathrm{d}\theta}\right)^2 + r^2$$

### The Method

| Step | What To Do |
|---|---|
| **Step 1** | Identify the form of the curve (Cartesian / parametric / polar) |
| **Step 2** | Differentiate with respect to the correct variable |
| **Step 3** | Substitute into the right formula and simplify the square root (identities often collapse it to a standard integral) |
| **Step 4** | Integrate between the given limits |

---

### Example 23 - Easy (Cartesian arc length)

> **Question:** Find the length of the curve $y = \cosh x$ from $x = 0$ to $x = \ln 2$.

**Solution:**

Differentiate:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \sinh x$$

$$s = \int_0^{\ln 2} \sqrt{1 + \sinh^2 x}\;\mathrm{d}x$$

Use $\cosh^2 x - \sinh^2 x = 1$, so $1 + \sinh^2 x = \cosh^2 x$:

$$s = \int_0^{\ln 2} \cosh x\;\mathrm{d}x$$

$$s = \left[\sinh x\right]_0^{\ln 2} = \sinh(\ln 2) - 0$$

Use $\sinh(\ln 2) = \frac{2 - \frac{1}{2}}{2} = \frac{3}{4}$:

$$s = \frac{3}{4} \quad\checkmark$$

> 💡 **The EXPLORE 22.1 answer:** the function with arc length equal to area under the curve over any finite interval is $y = \cosh x$ - the arc length $\int\sqrt{1 + \sinh^2 x}\,\mathrm{d}x = \int\cosh x\,\mathrm{d}x$ equals the area $\int\cosh x\,\mathrm{d}x$.

---

### Example 24 - Medium (parametric arc length)

> **Question:** If $x = \cos^2 t$ and $y = \sin^2 t$, determine the length of the parametric curve from $t = 0$ to $t = \frac{\pi}{4}$.

**Solution:**

Differentiate both:

$$\frac{\mathrm{d}x}{\mathrm{d}t} = -2\sin t\cos t, \qquad \frac{\mathrm{d}y}{\mathrm{d}t} = 2\sin t\cos t$$

$$s = \int_0^{\pi/4} \sqrt{(-2\sin t\cos t)^2 + (2\sin t\cos t)^2}\;\mathrm{d}t$$

$$s = \int_0^{\pi/4} \sqrt{8\sin^2 t\cos^2 t}\;\mathrm{d}t$$

$$s = \int_0^{\pi/4} 2\sqrt{2}\sin t\cos t\;\mathrm{d}t$$

Use $2\sin t\cos t = \sin 2t$:

$$s = \int_0^{\pi/4} \sqrt{2}\sin 2t\;\mathrm{d}t$$

$$s = \sqrt{2}\left[-\frac{1}{2}\cos 2t\right]_0^{\pi/4}$$

$$s = -\frac{\sqrt{2}}{2}\left(\cos\frac{\pi}{2} - \cos 0\right) = -\frac{\sqrt{2}}{2}(0 - 1)$$

$$s = \frac{\sqrt{2}}{2} \approx 0.7071 \quad\checkmark$$

---

### Example 25 - Medium (polar arc length)

> **Question:** If $r = \sin\theta$, determine the length of the polar curve over the interval $\theta \in \left[0, \frac{\pi}{4}\right]$.

**Solution:**

Differentiate:

$$\frac{\mathrm{d}r}{\mathrm{d}\theta} = \cos\theta$$

$$s = \int_0^{\pi/4} \sqrt{\sin^2\theta + \cos^2\theta}\;\mathrm{d}\theta$$

$$s = \int_0^{\pi/4} 1\;\mathrm{d}\theta = \frac{\pi}{4} \approx 0.7854 \quad\checkmark$$

---

### Example 26 - Hard (polar arc length with exponential)

> **Question:** If $r = e^\theta$, determine the length of the polar curve over the interval $\theta \in \left[0, \frac{\pi}{2}\right]$.

**Solution:**

Differentiate:

$$\frac{\mathrm{d}r}{\mathrm{d}\theta} = e^\theta$$

$$s = \int_0^{\pi/2} \sqrt{e^{2\theta} + e^{2\theta}}\;\mathrm{d}\theta = \int_0^{\pi/2} \sqrt{2}e^{\theta}\;\mathrm{d}\theta$$

$$s = \sqrt{2}\left[e^{\theta}\right]_0^{\pi/2} = \sqrt{2}\left(e^{\pi/2} - 1\right) \approx 5.389 \quad\checkmark$$

---

### Example 27 - Hard (the classic past paper arc length)

> **Question:** The curve with equation $y = -\ln(\cos x)$ is defined for $0 \leq x < \frac{\pi}{2}$. Find the length of the arc of this curve from $x = 0$ to $x = \frac{\pi}{3}$. Give your answer in the form $\ln(a + b\sqrt{3})$ where $a$ and $b$ are integers to be determined.
> *(Cambridge International AS & A Level Further Mathematics 9231 Paper 1 Q8 November 2009)*

**Solution:**

Differentiate $y = -\ln(\cos x)$ using the chain rule (derivative of $\ln(\cos x)$ is $-\tan x$):

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \tan x$$

$$s = \int_0^{\pi/3} \sqrt{1 + \tan^2 x}\;\mathrm{d}x$$

Use $1 + \tan^2 x = \sec^2 x$:

$$s = \int_0^{\pi/3} \sec x\;\mathrm{d}x$$

$$\int \sec x\;\mathrm{d}x = \ln\lvert \sec x + \tan x \rvert + c$$

$$s = \left[\ln(\sec x + \tan x)\right]_0^{\pi/3}$$

At $x = \frac{\pi}{3}$: $\sec\frac{\pi}{3} = 2$, $\tan\frac{\pi}{3} = \sqrt{3}$. At $x = 0$: $\sec 0 = 1$, $\tan 0 = 0$:

$$s = \ln(2 + \sqrt{3}) - \ln(1 + 0) = \ln(2 + \sqrt{3})$$

$$s = \ln(2 + \sqrt{3}) \approx 1.317 \quad\checkmark$$

---

### Practice Questions - Part 4

#### Question P10

> The curve $y = x^{3/2}$ is defined for $0 \leq x \leq 1$. Find the arc length.

<details>
<summary><strong>Click for Solution</strong></summary>

**Solution:**

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{3}{2}x^{1/2}$$

$$s = \int_0^1 \sqrt{1 + \frac{9}{4}x}\;\mathrm{d}x$$

Let $u = 1 + \frac{9}{4}x$, so $\mathrm{d}u = \frac{9}{4}\mathrm{d}x$:

$$s = \frac{4}{9}\int_1^{13/4} \sqrt{u}\;\mathrm{d}u = \frac{4}{9}\left[\frac{2}{3}u^{3/2}\right]_1^{13/4}$$

$$s = \frac{8}{27}\left[\left(\frac{13}{4}\right)^{3/2} - 1\right] = \frac{8}{27}\left(\frac{13\sqrt{13}}{8} - 1\right)$$

$$s = \frac{13\sqrt{13} - 8}{27} \approx 1.4397 \quad\checkmark$$

</details>

#### Question P11

> A curve has parametric equations $x = t^2$, $y = t^3$. Find the arc length from $t = 1$ to $t = 2$.

<details>
<summary><strong>Click for Solution</strong></summary>

**Solution:**

$$\frac{\mathrm{d}x}{\mathrm{d}t} = 2t, \qquad \frac{\mathrm{d}y}{\mathrm{d}t} = 3t^2$$

$$s = \int_1^2 \sqrt{4t^2 + 9t^4}\;\mathrm{d}t = \int_1^2 t\sqrt{4 + 9t^2}\;\mathrm{d}t$$

Let $u = 4 + 9t^2$, so $\mathrm{d}u = 18t\,\mathrm{d}t$:

$$s = \frac{1}{18}\int_{13}^{40} \sqrt{u}\;\mathrm{d}u = \frac{1}{18}\left[\frac{2}{3}u^{3/2}\right]_{13}^{40}$$

$$s = \frac{1}{27}\left(40^{3/2} - 13^{3/2}\right) = \frac{1}{27}\left(80\sqrt{10} - 13\sqrt{13}\right) \approx 7.633 \quad\checkmark$$

</details>

---


# PART 5: Surface Areas of Revolution

## 5.1 The Surface Area Formulas

When an arc of a curve is rotated through a full revolution about an axis, it sweeps out a surface. The surface area is found by adding up tiny frustum strips: each strip has area $2\pi \times (\text{radius}) \times \delta s$.

**About the x-axis** (radius = $|y|$):

$$S = \int_a^b 2\pi y\;\mathrm{d}s$$

**About the y-axis** (radius = $|x|$):

$$S = \int_a^b 2\pi x\;\mathrm{d}s$$

Where $\mathrm{d}s$ is the arc-length element for the curve's form:

| Curve form | $\mathrm{d}s$ |
|---|---|
| Cartesian $y = f(x)$ | $\sqrt{1 + \left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2}\;\mathrm{d}x$ |
| Parametric $x(t), y(t)$ | $\sqrt{\left(\frac{\mathrm{d}x}{\mathrm{d}t}\right)^2 + \left(\frac{\mathrm{d}y}{\mathrm{d}t}\right)^2}\;\mathrm{d}t$ |

### The Method

| Step | What To Do |
|---|---|
| **Step 1** | Decide the axis: x-axis uses $2\pi y$, y-axis uses $2\pi x$ |
| **Step 2** | Write down $\mathrm{d}s$ for the curve's form |
| **Step 3** | Substitute into $S = \int 2\pi(\text{radius})\,\mathrm{d}s$ and simplify |
| **Step 4** | Integrate between the limits (convert limits too for parametric forms) |

> \u2b50 **Watch Out!** The most common error is using the wrong radius. Rotating about the **x-axis** means every strip's radius is the curve's **height above the x-axis**, which is $y$ (or the parametric $y(t)$). Rotating about the **y-axis** uses $x$. Also, do NOT confuse surface area ($2\pi y\,\mathrm{d}s$) with volume ($\pi y^2\,\mathrm{d}x$) - the surface area uses $\mathrm{d}s$, not $\mathrm{d}x$.

---

### Example 28 - Medium (Cartesian, about the x-axis)

> **Question:** The curve $y = \sqrt{x}$ from $x = 2$ to $x = 12$ is rotated completely about the x-axis. Find the surface area generated.

**Solution:**

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{1}{2\sqrt{x}}$$

$$\mathrm{d}s = \sqrt{1 + \frac{1}{4x}}\;\mathrm{d}x$$

$$S = \int_2^{12} 2\pi \sqrt{x}\sqrt{1 + \frac{1}{4x}}\;\mathrm{d}x$$

Simplify the product of square roots:

$$S = 2\pi\int_2^{12} \sqrt{x + \frac{1}{4}}\;\mathrm{d}x$$

Let $u = x + \frac{1}{4}$, so $\mathrm{d}u = \mathrm{d}x$:

$$S = 2\pi\int_{9/4}^{49/4} \sqrt{u}\;\mathrm{d}u = 2\pi\left[\frac{2}{3}u^{3/2}\right]_{9/4}^{49/4}$$

$$S = \frac{4\pi}{3}\left[\left(\frac{49}{4}\right)^{3/2} - \left(\frac{9}{4}\right)^{3/2}\right] = \frac{4\pi}{3}\left[\frac{343}{8} - \frac{27}{8}\right]$$

$$S = \frac{4\pi}{3}\left(\frac{316}{8}\right) = \frac{4\pi}{3} \times \frac{79}{2} = \frac{158\pi}{3} \approx 165.5 \quad\checkmark$$

---

### Example 29 - Hard (parametric, about the x-axis - the astroid)

> **Question:** The astroid has parametric equations $x = a\cos^3 t$, $y = a\sin^3 t$ (for $a > 0$). The arc from $t = 0$ to $t = \frac{\pi}{2}$ is rotated about the x-axis. Show that the surface area is $\frac{6\pi a^2}{5}$.

**Solution:**

Differentiate both:

$$\frac{\mathrm{d}x}{\mathrm{d}t} = -3a\cos^2 t\sin t, \qquad \frac{\mathrm{d}y}{\mathrm{d}t} = 3a\sin^2 t\cos t$$

$$\mathrm{d}s = \sqrt{9a^2\cos^4 t\sin^2 t + 9a^2\sin^4 t\cos^2 t}\;\mathrm{d}t$$

Factor out $9a^2\sin^2 t\cos^2 t$:

$$\mathrm{d}s = 3a\sin t\cos t\sqrt{\cos^2 t + \sin^2 t}\;\mathrm{d}t = 3a\sin t\cos t\;\mathrm{d}t$$

Rotating about the x-axis, the radius is $y = a\sin^3 t$:

$$S = \int_0^{\pi/2} 2\pi(a\sin^3 t)(3a\sin t\cos t)\;\mathrm{d}t$$

$$S = 6\pi a^2\int_0^{\pi/2} \sin^4 t\cos t\;\mathrm{d}t$$

This is a reverse chain rule (derivative of $\sin t$ is $\cos t$):

$$S = 6\pi a^2\left[\frac{\sin^5 t}{5}\right]_0^{\pi/2} = 6\pi a^2\left(\frac{1}{5} - 0\right)$$

$$S = \frac{6\pi a^2}{5} \quad\checkmark$$

---

### Example 30 - Hard (parametric, about the y-axis)

> **Question:** The curve with parametric equations $x = \cos^2 2t$, $y = \sin^2 2t$ from $t = 0$ to $t = \frac{\pi}{4}$ is rotated about the y-axis. Find the surface area generated.

**Solution:**

Differentiate both:

$$\frac{\mathrm{d}x}{\mathrm{d}t} = -4\cos 2t\sin 2t, \qquad \frac{\mathrm{d}y}{\mathrm{d}t} = 4\sin 2t\cos 2t$$

$$\mathrm{d}s = \sqrt{16\cos^2 2t\sin^2 2t + 16\sin^2 2t\cos^2 2t}\;\mathrm{d}t = 4\sqrt{2}\sin 2t\cos 2t\;\mathrm{d}t$$

Rotating about the y-axis, the radius is $x = \cos^2 2t$:

$$S = \int_0^{\pi/4} 2\pi(\cos^2 2t)(4\sqrt{2}\sin 2t\cos 2t)\;\mathrm{d}t$$

$$S = 8\sqrt{2}\pi\int_0^{\pi/4} \cos^3 2t\sin 2t\;\mathrm{d}t$$

Reverse chain rule: derivative of $\cos 2t$ is $-2\sin 2t$:

$$\int \cos^3 2t\sin 2t\;\mathrm{d}t = -\frac{1}{8}\cos^4 2t$$

$$S = 8\sqrt{2}\pi\left[-\frac{1}{8}\cos^4 2t\right]_0^{\pi/4}$$

$$S = -\sqrt{2}\pi\left[\cos^4\frac{\pi}{2} - \cos^4 0\right] = -\sqrt{2}\pi(0 - 1)$$

$$S = \pi\sqrt{2} \approx 4.443 \quad\checkmark$$

---

### Example 31 - Hard (the classic past paper surface area)

> **Question:** The curve with equation $y = 2\sqrt{x + 3}$ is rotated through one complete revolution about the x-axis. Find the surface area generated from $x = 0$ to $x = 1$, giving your answer in the form $\frac{\pi}{3}(a\sqrt{5} - b)$ where $a$ and $b$ are integers.
> *(Cambridge International AS & A Level Further Mathematics 9231 Paper 1 Q8 November 2009)*

**Solution:**

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{1}{\sqrt{x + 3}}$$

$$\mathrm{d}s = \sqrt{1 + \frac{1}{x + 3}}\;\mathrm{d}x = \sqrt{\frac{x + 4}{x + 3}}\;\mathrm{d}x$$

Rotating about the x-axis, the radius is $y = 2\sqrt{x + 3}$:

$$S = \int_0^1 2\pi(2\sqrt{x + 3})\sqrt{\frac{x + 4}{x + 3}}\;\mathrm{d}x$$

$$S = 4\pi\int_0^1 \sqrt{x + 3} \cdot \frac{\sqrt{x + 4}}{\sqrt{x + 3}}\;\mathrm{d}x = 4\pi\int_0^1 \sqrt{x + 4}\;\mathrm{d}x$$

$$S = 4\pi\left[\frac{2}{3}(x + 4)^{3/2}\right]_0^1 = \frac{8\pi}{3}\left(5^{3/2} - 4^{3/2}\right)$$

$$S = \frac{8\pi}{3}(5\sqrt{5} - 8) \approx 26.64 \quad\checkmark$$

---

### Practice Questions - Part 5

#### Question P12

> The curve $y = \sinh x$ from $x = 0$ to $x = 1$ is rotated about the x-axis. Find the volume of revolution. (Note: this is a volume question - use $V = \pi\int y^2\,\mathrm{d}x$, not the surface area formula!)

<details>
<summary><strong>Click for Solution</strong></summary>

**Solution:**

This is a volume, so use $V = \pi\int_0^1 y^2\;\mathrm{d}x$:

$$V = \pi\int_0^1 \sinh^2 x\;\mathrm{d}x$$

Use $\cosh 2x = 1 + 2\sinh^2 x$, so $\sinh^2 x = \frac{1}{2}(\cosh 2x - 1)$:

$$V = \frac{\pi}{2}\int_0^1 (\cosh 2x - 1)\;\mathrm{d}x = \frac{\pi}{2}\left[\frac{1}{2}\sinh 2x - x\right]_0^1$$

$$V = \frac{\pi}{2}\left(\frac{1}{2}\sinh 2 - 1\right) = \frac{\pi}{4}(\sinh 2 - 2) \approx 4.126 \quad\checkmark$$

</details>

#### Question P13

> The curve $y = \frac{1}{3}x^3 + 1$ from $x = 0$ to $x = 1$ has arc length $s = \int_0^1 \sqrt{1 + x^4}\;\mathrm{d}x$. When this arc is rotated about the x-axis, the surface area generated is denoted by $S$. Show that $\displaystyle S = 2\pi s + \frac{\pi}{9}\left(2\sqrt{2} - 1\right)$.
> *(Cambridge International AS & A Level Further Mathematics 9231 Paper 1 Q4 June 2009)*

<details>
<summary><strong>Click for Solution</strong></summary>

**Solution:**

Differentiate:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = x^2$$

$$\mathrm{d}s = \sqrt{1 + x^4}\;\mathrm{d}x$$

About the x-axis, radius is $y = \frac{1}{3}x^3 + 1$:

$$S = \int_0^1 2\pi\left(\frac{1}{3}x^3 + 1\right)\sqrt{1 + x^4}\;\mathrm{d}x$$

$$S = 2\pi\int_0^1 \sqrt{1 + x^4}\;\mathrm{d}x + \frac{2\pi}{3}\int_0^1 x^3\sqrt{1 + x^4}\;\mathrm{d}x$$

The first integral is exactly $s$:

$$S = 2\pi s + \frac{2\pi}{3}\int_0^1 x^3\sqrt{1 + x^4}\;\mathrm{d}x$$

For the second, use the reverse chain rule: the derivative of $1 + x^4$ is $4x^3$:

$$\int_0^1 x^3\sqrt{1 + x^4}\;\mathrm{d}x = \left[\frac{1}{4} \cdot \frac{2}{3}(1 + x^4)^{3/2}\right]_0^1 = \frac{1}{6}\left(2^{3/2} - 1\right) = \frac{1}{6}\left(2\sqrt{2} - 1\right)$$

$$S = 2\pi s + \frac{2\pi}{3} \cdot \frac{1}{6}\left(2\sqrt{2} - 1\right)$$

$$S = 2\pi s + \frac{\pi}{9}\left(2\sqrt{2} - 1\right) \quad\checkmark$$

</details>

---


# PART 6A: Rectangle Sums and Limits of Areas (width $\to 0$)

## 6A.1 The Big Idea: Rectangles Whose Width Tends to Zero

Cambridge explicitly says *questions may involve rectangles whose width can tend to zero* - e.g.

$$\frac{1}{n}\sum_{r=1}^{n} f\!\left(\frac{r}{n}\right) \to \int_{0}^{1} f(x)\,\mathrm{d}x$$

This is the **Riemann sum** construction. On $[a,b]$ cut it into $n$ strips of equal width:

$$\boxed{\Delta x = \frac{b-a}{n}}$$

$$\boxed{x_{r} = a + r\,\Delta x \qquad (r = 1, 2, \ldots, n)}$$

$$\boxed{\text{height of $r$-th rectangle} = f(x_{r})}$$

$$\boxed{\text{area of $r$-th rectangle} = \Delta x \cdot f(x_{r})}$$

$$\boxed{U_{n} = \sum_{r=1}^{n} \Delta x\,f(x_{r}) = \sum_{r=1}^{n} f\!\left(a + \frac{r(b-a)}{n}\right)\frac{b-a}{n}}$$

Then as $n \to \infty$ the rectangles fill the exact area:

$$\boxed{\int_{a}^{b} f(x)\,\mathrm{d}x = \lim_{n\to\infty} \sum_{r=1}^{n} f\!\left(a + \frac{r(b-a)}{n}\right)\frac{b-a}{n}}$$

**Special case $a = 0$, $b = 1$** (the form Cambridge quotes most often):

$$\boxed{\int_{0}^{1} f(x)\,\mathrm{d}x = \lim_{n\to\infty} \frac{1}{n}\sum_{r=1}^{n} f\!\left(\frac{r}{n}\right)}$$

> 💡 **When is it upper vs lower?** For a finite $n$ the sum is an over- or under-estimate depending on monotonicity and which endpoint you sample.

|  | Left endpoint $x_{r-1}=a+(r-1)\Delta x$ | Right endpoint $x_{r}=a+r\Delta x$ |
|---|---|---|
| **$f$ increasing** | **Lower** sum (rectangles lie below curve) | **Upper** sum (rectangles lie above curve) |
| **$f$ decreasing** | **Upper** sum | **Lower** sum |

For a **decreasing** positive function on $[0,1]$ with right endpoints $r/n$: the sum $\frac{1}{n}\sum_{r=1}^{n} f(r/n)$ is a **lower sum** and lies BELOW the integral. With left endpoints $(r-1)/n$ it would be an upper sum.

> ⭐ **Watch Out!** The $r$-index tells you the endpoint: $r = 1,\ldots,n$ means **right** endpoints; $r = 0,\ldots,n-1$ means **left** endpoints. Shifting the index by 1 flips upper/lower for monotone functions - the most common source of inequality-direction errors.

### The Method (for width $\to 0$ questions)

| Step | What To Do |
|---|---|
| **Step 1** | Identify $a$, $b$, $\Delta x = (b-a)/n$ and the sample points $x_{r} = a + r\Delta x$ |
| **Step 2** | Write the rectangle area: $\Delta x\, f(x_{r})$ and the sum $U_{n} = \sum \Delta x\, f(x_{r})$ |
| **Step 3** | Decide upper vs lower: increasing + right = upper; decreasing + right = lower (and vice versa for left) |
| **Step 4** | Evaluate $\lim_{n\to\infty} U_{n}$ by recognising it as $\int_{a}^{b} f(x)\,\mathrm{d}x$ |

---

### Example 32 - Easy (the definition: $[0,1]$ with $f(x)=x^{2}$)

> **Question:** For $f(x)=x^{2}$ on $[0,1]$, write down the right Riemann sum $U_{n}=\frac{1}{n}\sum_{r=1}^{n}\left(\frac{r}{n}\right)^{2}$. Is $U_{n}$ an upper or lower sum? Find $\lim_{n\to\infty}U_{n}$.

**Solution:**

$$\Delta x = \frac{1-0}{n} = \frac{1}{n}, \qquad x_{r} = \frac{r}{n}$$

$$U_{n} = \sum_{r=1}^{n} \frac{1}{n}\left(\frac{r}{n}\right)^{2} = \frac{1}{n^{3}}\sum_{r=1}^{n} r^{2}$$

$f(x)=x^{2}$ is **increasing** on $[0,1]$ and we use **right** endpoints, so $U_{n}$ is an **upper sum** - it lies above the integral for every finite $n$.

Use $\sum_{r=1}^{n} r^{2}=\frac{n(n+1)(2n+1)}{6}$:

$$U_{n} = \frac{1}{n^{3}}\cdot\frac{n(n+1)(2n+1)}{6} = \frac{(n+1)(2n+1)}{6n^{2}}$$

Take the limit:

$$\lim_{n\to\infty} U_{n} = \lim_{n\to\infty}\frac{2n^{2}+3n+1}{6n^{2}} = \frac{2}{6} = \frac{1}{3}$$

Check against the integral:

$$\int_{0}^{1} x^{2}\,\mathrm{d}x = \left[\frac{x^{3}}{3}\right]_{0}^{1} = \frac{1}{3} \quad\checkmark$$

So $\displaystyle \frac{1}{n}\sum_{r=1}^{n} \left(\frac{r}{n}\right)^{2} \to \frac{1}{3}$ and each $U_{n} > \frac{1}{3}$ (upper sum falling down to the limit).

---

### Example 33 - Medium (the rectangle question from your 2024 paper: exponential)

> **Question:** Let $f(x)=e^{x}$ on $[0,1]$. The interval is divided into $n$ equal subintervals of width $\Delta x = 1/n$ with right endpoints $x_{r}=r/n$.
> a) Show that $U_{n}=\frac{e^{1/n}\left(e-1\right)}{n\left(e^{1/n}-1\right)}$.
> b) Hence find $\lim_{n\to\infty} U_{n}$ and state whether $U_{n}$ is an upper or lower sum.

**Solution (a):**

$$U_{n} = \sum_{r=1}^{n} \frac{1}{n} e^{r/n} = \frac{1}{n}\sum_{r=1}^{n} \left(e^{1/n}\right)^{r}$$

This is a geometric progression with first term $e^{1/n}$ and ratio $e^{1/n}$:

$$\sum_{r=1}^{n} \left(e^{1/n}\right)^{r} = e^{1/n}\cdot\frac{\left(e^{1/n}\right)^{n}-1}{e^{1/n}-1} = \frac{e^{1/n}(e-1)}{e^{1/n}-1}$$

$$U_{n} = \frac{e^{1/n}(e-1)}{n\left(e^{1/n}-1\right)} \quad\checkmark$$

**Solution (b):**

$e^{x}$ is **increasing** on $[0,1]$ and we use **right** endpoints, so $U_{n}$ is an **upper sum**:

$$U_{n} > \int_{0}^{1} e^{x}\,\mathrm{d}x = e-1 \approx 1.718$$

for every finite $n$, and it decreases to the integral.

To find the limit, use $e^{1/n}-1 \sim \frac{1}{n}$ as $n\to\infty$ (or L'Hôpital with $h=1/n$):

Let $h = 1/n$, so $h\to 0$:

$$\lim_{n\to\infty} U_{n} = \lim_{h\to 0}\frac{e^{h}(e-1)}{(e^{h}-1)/h} = (e-1)\lim_{h\to 0}\frac{h\,e^{h}}{e^{h}-1}$$

Use $e^{h}-1 = h + \frac{h^{2}}{2}+\cdots$, so $\frac{h\,e^{h}}{e^{h}-1}\to 1$:

$$\lim_{n\to\infty} U_{n} = e-1 = \int_{0}^{1} e^{x}\,\mathrm{d}x \quad\checkmark$$

> 💡 **Exam shortcut:** you do NOT need the geometric sum in the exam - you can just state $\lim_{n\to\infty} U_{n}=\int_{0}^{1} e^{x}\,\mathrm{d}x = e-1$ by recognising the Riemann sum. The GP working is only needed if the question says "show that $U_{n}=\ldots$".

---

### Example 34 - Medium (general $[a,b]$ and decreasing function: lower sum)

> **Question:** Let $f(x)=\frac{1}{1+x}$ on $[0,1]$ with right endpoints $x_{r}=r/n$.
> a) Write down $U_{n}$ and decide if it is an upper or lower sum.
> b) Hence write down $\lim_{n\to\infty} U_{n}$ as an integral and evaluate it.

**Solution (a):**

$$\Delta x = \frac{1}{n}, \qquad x_{r} = \frac{r}{n}$$

$$U_{n} = \sum_{r=1}^{n} \frac{1}{n}\cdot\frac{1}{1+r/n} = \frac{1}{n}\sum_{r=1}^{n}\frac{n}{n+r} = \sum_{r=1}^{n}\frac{1}{n+r}$$

$f(x)=\frac{1}{1+x}$ is **decreasing** on $[0,1]$ and we use **right** endpoints, so this is a **lower sum**:

$$U_{n} < \int_{0}^{1}\frac{1}{1+x}\,\mathrm{d}x$$

and it **increases** to the integral as $n\to\infty$.

**Solution (b):**

$$\lim_{n\to\infty} U_{n} = \int_{0}^{1}\frac{1}{1+x}\,\mathrm{d}x$$

$$= \left[\ln(1+x)\right]_{0}^{1} = \ln 2 \approx 0.6931 \quad\checkmark$$

So $\displaystyle \sum_{r=1}^{n}\frac{1}{n+r} \to \ln 2$ from **below**.

---

### Example 35 - Hard (Cambridge-style inequality + limit)

> **Question:** Let $f(x)=\ln(1+x)$ on $[0,1]$, divided into $n$ equal strips of width $1/n$ with right endpoints.
> a) Show that $L_{n} < \int_{0}^{1}\ln(1+x)\,\mathrm{d}x < U_{n}$ where $L_{n}$ and $U_{n}$ are the lower and upper sums. Identify $L_{n}$ and $U_{n}$.
> b) Use $L_{n}=\frac{1}{n}\sum_{r=0}^{n-1}\ln\!\left(1+\frac{r}{n}\right)$ to prove $\displaystyle \ln\!\left(\frac{n!}{n^{n}}\right)+1 < \int_{0}^{1}\ln(1+x)\,\mathrm{d}x \cdot n$ -type bounds.

**Solution (a):**

$f(x)=\ln(1+x)$ is **increasing** on $[0,1]$ (derivative $1/(1+x)>0$).

- **Lower sum** uses **left** endpoints: $x_{r}=r/n$, $r=0,\ldots,n-1$:

$$L_{n} = \frac{1}{n}\sum_{r=0}^{n-1}\ln\!\left(1+\frac{r}{n}\right)$$

- **Upper sum** uses **right** endpoints: $x_{r}=r/n$, $r=1,\ldots,n$:

$$U_{n} = \frac{1}{n}\sum_{r=1}^{n}\ln\!\left(1+\frac{r}{n}\right)$$

Since left rectangles lie below and right rectangles above an increasing curve:

$$L_{n} < \int_{0}^{1}\ln(1+x)\,\mathrm{d}x < U_{n} \quad\checkmark$$

**Solution (b):**

$$U_{n} - L_{n} = \frac{1}{n}\left[\ln\!\left(1+\frac{n}{n}\right)-\ln\!\left(1+\frac{0}{n}\right)\right] = \frac{\ln 2}{n} \to 0$$

So both squeeze to the integral. Evaluating the integral:

$$\int_{0}^{1}\ln(1+x)\,\mathrm{d}x = \left[(1+x)\ln(1+x)-x\right]_{0}^{1} = 2\ln 2 - 1 \approx 0.3863 \quad\checkmark$$

Hence for large $n$: $\displaystyle \frac{1}{n}\sum_{r=1}^{n}\ln\!\left(1+\frac{r}{n}\right)\to 2\ln 2-1$.

> ⭐ **Key exam move:** if the question asks you to *derive an inequality*, draw the rectangles and argue upper vs lower. If it asks for the *limit*, just write $\lim = \int_{a}^{b} f(x)\,\mathrm{d}x$ and integrate - do not evaluate the sum first.

---

### Practice Questions - Part 6A

#### Question P14a

> The interval $[0,2]$ is divided into $n$ equal subintervals of width $2/n$ with right endpoints $x_{r}=2r/n$.
> a) Write down the Riemann sum for $f(x)=x^{3}$ on $[0,2]$.
> b) Is it an upper or lower sum? Why?
> c) Hence evaluate $\displaystyle \lim_{n\to\infty}\frac{2}{n}\sum_{r=1}^{n}\left(\frac{2r}{n}\right)^{3}$.

<details>
<summary><strong>Click for Solution</strong></summary>

**Solution (a):**

$$\Delta x = \frac{2}{n}, \qquad x_{r} = \frac{2r}{n}$$

$$U_{n} = \sum_{r=1}^{n} \frac{2}{n}\left(\frac{2r}{n}\right)^{3} = \frac{16}{n^{4}}\sum_{r=1}^{n} r^{3} \quad\checkmark$$

**Solution (b):**

$f(x)=x^{3}$ is **increasing** on $[0,2]$ and we use **right** endpoints, so $U_{n}$ is an **upper sum** - every rectangle lies above the curve. $U_{n} > \int_{0}^{2} x^{3}\,\mathrm{d}x$ for finite $n$. $\quad\checkmark$

**Solution (c):**

$$\lim_{n\to\infty} U_{n} = \int_{0}^{2} x^{3}\,\mathrm{d}x = \left[\frac{x^{4}}{4}\right]_{0}^{2} = 4 \quad\checkmark$$

</details>

#### Question P14b

> Let $f(x)=\frac{1}{x}$ on $[1,2]$ with $n$ strips of width $1/n$ and right endpoints $x_{r}=1+r/n$.
> a) Write the sum $\frac{1}{n}\sum_{r=1}^{n}\frac{1}{1+r/n}$ as a Riemann sum.
> b) State whether it is an upper or lower sum and give the inequality it satisfies.
> c) Find its limit as $n\to\infty$.

<details>
<summary><strong>Click for Solution</strong></summary>

**Solution (a):**

$$U_{n} = \sum_{r=1}^{n} \frac{1}{n}\cdot\frac{1}{1+r/n} = \frac{1}{n}\sum_{r=1}^{n}\frac{n}{n+r} = \sum_{r=1}^{n}\frac{1}{n+r} \quad\checkmark$$

**Solution (b):**

$f(x)=1/x$ is **decreasing** on $[1,2]$ and we use **right** endpoints, so $U_{n}$ is a **lower sum**:

$$U_{n} < \int_{1}^{2}\frac{1}{x}\,\mathrm{d}x = \ln 2 \quad\checkmark$$

It increases to $\ln 2$ as $n\to\infty$.

**Solution (c):**

$$\lim_{n\to\infty} U_{n} = \int_{1}^{2}\frac{1}{x}\,\mathrm{d}x = \ln 2 \approx 0.6931 \quad\checkmark$$

</details>

---

# PART 6B: Limits of Areas - The Integral Test (unit-width rectangles)

## 6B.1 The Big Idea: Sums vs Integrals

An infinite sum $\sum_{n=1}^{\infty} f(n)$ can be pictured as a staircase of unit-width rectangles of height $f(n)$. The curve $y = f(x)$ either runs above or below that staircase, so **the sum converges exactly when the improper integral $\int f(x)\,\mathrm{d}x$ converges** - as long as $f$ is positive and decreasing.

**The four rules (R = area under the curve, S = area of the rectangles):**

| Situation | Conclusion |
|---|---|
| $R > S$ and $R$ converges | $S$ **converges** |
| $R < S$ and $R$ diverges | $S$ **diverges** |
| $R > S$ and $R$ diverges | NO conclusion about $S$ |
| $R < S$ and $R$ converges | NO conclusion about $S$ |

> ⭐ **Watch Out!** The last two rows are the classic trap. A bigger curve diverging tells you nothing about the smaller sum, and a smaller curve converging tells you nothing about the bigger sum. You must compare the RIGHT way round.

### The Famous Harmonic Series

$$\sum_{n=1}^{\infty} \frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \cdots$$

Each term shrinks to 0, yet the sum still diverges - the classic counterexample to "if terms go to zero it must converge". The integral test shows why:

$$\sum_{n=1}^{\infty} \frac{1}{n} \geq \int_1^{\infty} \frac{1}{x}\,\mathrm{d}x = \left[\ln x\right]_1^{\infty} \to \infty$$

The integral diverges, and since $R < S$, so does the sum.

---

## 6B.2 Finding Upper and Lower Bounds for a Sum (Unit-Width Rectangles)

**Upper bound:** shift the rectangles LEFT so the curve sits above them. Then:

$$\sum_{r=2}^{n} f(r) < \int_1^n f(x)\,\mathrm{d}x$$

**Lower bound:** shift the rectangles RIGHT so the curve sits below them. Then:

$$\sum_{r=1}^{n} f(r) > \int_1^{n+1} f(x)\,\mathrm{d}x$$

> 💡 **How to remember:** for an UPPER bound, the integral must cover ALL the rectangles, so start the integral one step EARLIER ($\int_1^n$ covers $r = 2, \ldots, n$). For a LOWER bound, the integral must fit INSIDE the rectangles, so end it one step LATER ($\int_1^{n+1}$ fits inside $r = 1, \ldots, n$).

---

### Example 36 - Medium (bounds for $\sum \frac{1}{r\sqrt{r}}$)

> **Question:**
> a) Find the upper and lower bounds for $\displaystyle \sum_{r=1}^{n} \frac{1}{r\sqrt{r}}$.
> b) Hence show that $\displaystyle \sum_{n=1}^{\infty} \frac{1}{n\sqrt{n}}$ converges, and give an estimate for its upper bound.
> *(Cambridge International AS & A Level Further Mathematics 9231, Worked Example 22.20)*

**Solution (a) - upper bound:**

Note $\frac{1}{r\sqrt{r}} = r^{-3/2}$. For the upper bound, start the integral one step earlier:

$$\sum_{r=2}^{n} \frac{1}{r\sqrt{r}} < \int_1^{n} x^{-3/2}\,\mathrm{d}x$$

Add the $r = 1$ term ($= 1$) to both sides:

$$\sum_{r=1}^{n} \frac{1}{r\sqrt{r}} < 1 + \int_1^{n} x^{-3/2}\,\mathrm{d}x$$

$$= 1 + \left[-2x^{-1/2}\right]_1^{n} = 1 + \left(-\frac{2}{\sqrt{n}} + 2\right)$$

$$\text{Upper bound} = 3 - \frac{2}{\sqrt{n}} \quad\checkmark$$

**Solution (a) - lower bound:**

For the lower bound, end the integral one step later:

$$\sum_{r=1}^{n} \frac{1}{r\sqrt{r}} > \int_1^{n+1} x^{-3/2}\,\mathrm{d}x$$

$$= \left[-2x^{-1/2}\right]_1^{n+1} = 2 - \frac{2}{\sqrt{n+1}}$$

$$\text{Lower bound} = 2 - \frac{2}{\sqrt{n+1}} \quad\checkmark$$

**Solution (b):**

As $n \to \infty$, the upper bound tends to:

$$\lim_{n \to \infty}\left(3 - \frac{2}{\sqrt{n}}\right) = 3$$

So the infinite sum satisfies $\sum_{n=1}^{\infty} \frac{1}{n\sqrt{n}} < 3$ - it converges, with upper bound 3. (Its actual value is about 2.612.) $\quad\checkmark$

---

## 6B.3 The Comparison Test

When the integral test is awkward, compare your sum against a KNOWN sum:

| Known fact | Compare against |
|---|---|
| $\sum \frac{1}{n}$ diverges (harmonic) | smaller-than-harmonic behaviour |
| $\sum \frac{1}{n^2}$ converges (p-series, $p > 1$) | larger-than-p-series behaviour |
| $\sum \frac{1}{\sqrt{n}} = \sum n^{-1/2}$ diverges (p-series, $p \leq 1$) | $\frac{1}{\sqrt{n+1}}$, $\frac{1}{\sqrt{n^2 - 3}}$ |

**Rules:**
- If your terms are BIGGER than a divergent series, yours diverges.
- If your terms are SMALLER than a convergent series, yours converges.

---

### Example 37 - Medium (comparison with the harmonic series)

> **Question:** Show that $\displaystyle \sum_{n=2}^{\infty} \frac{1}{\sqrt{n^2 - 3}}$ diverges.

**Solution:**

Compare with the harmonic series. Since $n^2 - 3 < n^2$:

$$\sqrt{n^2 - 3} < \sqrt{n^2} = n$$

So each term is BIGGER than the harmonic term:

$$\frac{1}{\sqrt{n^2 - 3}} > \frac{1}{n}$$

The harmonic series $\sum \frac{1}{n}$ diverges, so anything bigger also diverges:

$$\sum_{n=2}^{\infty} \frac{1}{\sqrt{n^2 - 3}} \text{ diverges} \quad\checkmark$$

---

### Example 38 - Medium (comparison using a shifted integral)

> **Question:** Show that $\displaystyle \sum_{n=1}^{\infty} \frac{1}{\sqrt{n}}$ diverges.

**Solution:**

Since $\sqrt{n} < \sqrt{n+1}$, we have $\frac{1}{\sqrt{n}} > \frac{1}{\sqrt{n+1}}$. If the SMALLER sum diverges, the bigger one does too:

$$\sum_{n=1}^{\infty} \frac{1}{\sqrt{n+1}} = \sum_{m=2}^{\infty} \frac{1}{\sqrt{m}}$$

Compare $\frac{1}{\sqrt{n+1}}$ against the integral:

$$\int_1^{\infty} \frac{1}{\sqrt{x+1}}\,\mathrm{d}x = \left[2\sqrt{x+1}\right]_1^{\infty} \to \infty$$

The integral diverges, so $\sum \frac{1}{\sqrt{n+1}}$ diverges, hence $\sum \frac{1}{\sqrt{n}}$ diverges too. $\quad\checkmark$

---

### Example 39 - Hard (the $\sum \frac{1}{n\ln n}$ classic)

> **Question:** Find the upper bound for $\displaystyle \sum_{r=2}^{n} \frac{1}{r\ln r}$. Hence, show that $\displaystyle \sum_{n=2}^{\infty} \frac{1}{n\ln n}$ diverges.
> *(Cambridge International AS & A Level Further Mathematics 9231, Worked Example 22.21)*

**Solution:**

For the upper bound, start the integral one step earlier:

$$\sum_{r=3}^{n} \frac{1}{r\ln r} < \int_2^{n} \frac{1}{x\ln x}\,\mathrm{d}x$$

Add the $r = 2$ term ($= \frac{1}{2\ln 2}$):

$$\sum_{r=2}^{n} \frac{1}{r\ln r} < \frac{1}{2\ln 2} + \int_2^{n} \frac{1}{x\ln x}\,\mathrm{d}x$$

The integral is of the form $\int \frac{f'(x)}{f(x)}\,\mathrm{d}x$ with $f(x) = \ln x$:

$$\int_2^{n} \frac{1}{x\ln x}\,\mathrm{d}x = \left[\ln(\ln x)\right]_2^{n} = \ln(\ln n) - \ln(\ln 2)$$

$$\text{Upper bound} = \frac{1}{2\ln 2} + \ln(\ln n) - \ln(\ln 2)$$

As $n \to \infty$, $\ln(\ln n) \to \infty$, so the upper bound grows without limit - the sum diverges:

$$\sum_{n=2}^{\infty} \frac{1}{n\ln n} \text{ diverges} \quad\checkmark$$

---

### Example 40 - Medium (the p-series classification)

> **Question:** Determine for which values of $p$ the series $\displaystyle \sum_{n=1}^{\infty} \frac{1}{n^p}$ converges.

**Solution:**

Apply the integral test:

$$\int_1^{\infty} x^{-p}\,\mathrm{d}x = \begin{cases} \left[\frac{x^{1-p}}{1-p}\right]_1^{\infty} & p \neq 1 \\ \left[\ln x\right]_1^{\infty} & p = 1 \end{cases}$$

- $p > 1$: $x^{1-p} \to 0$ as $x \to \infty$, so the integral converges, hence the sum converges.
- $p \leq 1$: the integral diverges (for $p = 1$ it is the harmonic series), hence the sum diverges.

$$ \sum \frac{1}{n^p} \text{ converges} \iff p > 1 \quad\checkmark$$

---

### Practice Questions - Part 6B

#### Question P14

> By using the integral test, determine whether $\displaystyle \sum_{n=1}^{\infty} \frac{n}{n^2 + 1}$ converges or diverges.

<details>
<summary><strong>Click for Solution</strong></summary>

**Solution:**

$$\sum_{n=1}^{\infty} \frac{n}{n^2 + 1} \geq \int_1^{\infty} \frac{x}{x^2 + 1}\,\mathrm{d}x$$

The sum's rectangles sit above the curve, so $R < S$; if $R$ diverges, so does $S$:

$$\int_1^{\infty} \frac{x}{x^2 + 1}\,\mathrm{d}x = \left[\frac{1}{2}\ln(x^2 + 1)\right]_1^{\infty} \to \infty$$

The integral diverges, hence the sum diverges. $\quad\checkmark$

</details>

#### Question P15

> Show that $\displaystyle \sum_{n=2}^{\infty} \frac{1}{n^2 - 1}$ converges.

<details>
<summary><strong>Click for Solution</strong></summary>

**Solution:**

Compare with the integral $\int_2^{\infty} \frac{1}{x^2 - 1}\,\mathrm{d}x$, which is bigger than $\int_2^{\infty} \frac{1}{x^2}\,\mathrm{d}x$:

$$\int_2^{\infty} \frac{1}{x^2 - 1}\,\mathrm{d}x = \frac{1}{2}\int_2^{\infty}\left(\frac{1}{x-1} - \frac{1}{x+1}\right)\,\mathrm{d}x$$

$$= \frac{1}{2}\left[\ln\left(\frac{x-1}{x+1}\right)\right]_2^{\infty} = \frac{1}{2}\left(\ln 1 - \ln\frac{1}{3}\right) = \frac{1}{2}\ln 3$$

This is finite, and it is larger than $\int_2^{\infty} \frac{1}{x^2}\,\mathrm{d}x$ which must therefore also be finite. Hence $\sum \frac{1}{n^2}$ converges, so $\sum \frac{1}{n^2 - 1}$ converges. $\quad\checkmark$

</details>

#### Question P16

> Determine whether $\displaystyle \sum_{n=1}^{\infty} \frac{1}{\sqrt{n^2 + 3}}$ converges or diverges.

<details>
<summary><strong>Click for Solution</strong></summary>

**Solution:**

Since $n^2 + 3 > n^2$:

$$\sqrt{n^2 + 3} > n$$

$$\frac{1}{\sqrt{n^2 + 3}} < \frac{1}{n}$$

This shows the terms are SMALLER than the harmonic terms - but the harmonic series DIVERGES, so this comparison is inconclusive (a smaller series than a divergent one can go either way). Compare with $\frac{1}{2n}$ instead: since $n^2 + 3 \leq 4n^2$ for $n \geq 1$:

$$\sqrt{n^2 + 3} \leq 2n$$

$$\frac{1}{\sqrt{n^2 + 3}} \geq \frac{1}{2n}$$

Now $\sum_{n=1}^{\infty} \frac{1}{2n} = \frac{1}{2}\sum \frac{1}{n}$ diverges (it is half the harmonic series), and our terms are BIGGER than these diverging terms:

$$\sum_{n=1}^{\infty} \frac{1}{\sqrt{n^2 + 3}} \text{ diverges} \quad\checkmark$$

</details>

---


# 📝 COMPLETE FORMULA SHEET

## Standard Integrals (the Big Five)

$$\int \frac{1}{1 + x^2}\,\mathrm{d}x = \tan^{-1} x + c$$

$$\int \frac{1}{a^2 + x^2}\,\mathrm{d}x = \frac{1}{a}\tan^{-1}\left(\frac{x}{a}\right) + c$$

$$\int \frac{1}{\sqrt{a^2 - x^2}}\,\mathrm{d}x = \sin^{-1}\left(\frac{x}{a}\right) + c$$

$$\int \frac{1}{a^2 - x^2}\,\mathrm{d}x = \frac{1}{a}\tanh^{-1}\left(\frac{x}{a}\right) + c = \frac{1}{2a}\ln\left|\frac{a + x}{a - x}\right| + c$$

$$\int \frac{1}{\sqrt{x^2 + a^2}}\,\mathrm{d}x = \sinh^{-1}\left(\frac{x}{a}\right) + c = \ln\left(x + \sqrt{x^2 + a^2}\right) + c$$

$$\int \frac{1}{\sqrt{x^2 - a^2}}\,\mathrm{d}x = \cosh^{-1}\left(\frac{x}{a}\right) + c = \ln\left|x + \sqrt{x^2 - a^2}\right| + c$$

---

## Substitution Choices

| Integrand contains | Substitution | Resulting identity |
|---|---|---|
| $a^2 - x^2$ | $x = a\sin u$ | $\sqrt{a^2 - x^2} = a\cos u$ |
| $a^2 + x^2$ | $x = a\tan u$ | $a^2 + x^2 = a^2\sec^2 u$ |
| $a^2 + x^2$ | $x = a\sinh u$ | $\sqrt{a^2 + x^2} = a\cosh u$ |
| $x^2 - a^2$ | $x = a\cosh u$ | $\sqrt{x^2 - a^2} = a\sinh u$ |
| $a^2 - x^2$ | $x = a\tanh u$ | $a^2 - x^2 = a^2\operatorname{sech}^2 u$ |
| rational in $\sin x$, $\cos x$ | $t=\tan\frac{x}{2}$ | $\sin x=\frac{2t}{1+t^{2}}$, $\cos x=\frac{1-t^{2}}{1+t^{2}}$, $\mathrm{d}x=\frac{2\,\mathrm{d}t}{1+t^{2}}$ |

**Before substituting, complete the square:** $x^2 + bx + c = \left(x + \frac{b}{2}\right)^2 + \left(c - \frac{b^2}{4}\right)$

**Weierstrass tip:** after $t=\tan\frac{x}{2}$ you always get $\int \frac{2\,R(t)}{1+t^{2}}\,\mathrm{d}t$ where $R$ is rational - simplify before integrating.

---

## Hyperbolic Function Integrals

| $f(x)$ | $\int f(x)\,\mathrm{d}x$ |
|---|---|
| $\sinh x$ | $\cosh x + c$ |
| $\cosh x$ | $\sinh x + c$ |
| $\tanh x$ | $\ln(\cosh x) + c$ |
| $\coth x$ | $\ln\lvert \sinh x \rvert + c$ |
| $\operatorname{sech}^2 x$ | $\tanh x + c$ |
| $\operatorname{cosech}^2 x$ | $-\coth x + c$ |
| $\operatorname{sech} x\tanh x$ | $-\operatorname{sech} x + c$ |
| $\operatorname{cosech} x\coth x$ | $-\operatorname{cosech} x + c$ |
| $\frac{1}{\sinh x}$ | $\ln\left|\tanh\frac{x}{2}\right| + c$ |

---

## Inverse Functions - the "1 Times" Integration by Parts

$$\int \sin^{-1} x\,\mathrm{d}x = x\sin^{-1} x + \sqrt{1 - x^2} + c$$

$$\int \cos^{-1} x\,\mathrm{d}x = x\cos^{-1} x - \sqrt{1 - x^2} + c$$

$$\int \tan^{-1} x\,\mathrm{d}x = x\tan^{-1} x - \frac{1}{2}\ln(1 + x^2) + c$$

$$\int \sinh^{-1} x\,\mathrm{d}x = x\sinh^{-1} x - \sqrt{1 + x^2} + c$$

$$\int \cosh^{-1} x\,\mathrm{d}x = x\cosh^{-1} x - \sqrt{x^2 - 1} + c$$

$$\int \tanh^{-1} x\,\mathrm{d}x = x\tanh^{-1} x + \frac{1}{2}\ln\left(1 - x^2\right) + c$$

---

## Reduction Formulae

| Integral | Reduction formula | Valid |
|---|---|---|
| $I_n = \int \cos^n x\,\mathrm{d}x$ | $I_n = \dfrac{1}{n}\cos^{n-1} x\sin x + \dfrac{n-1}{n}I_{n-2}$ | $n \geq 2$ |
| $I_n = \int \sin^n x\,\mathrm{d}x$ | $I_n = -\dfrac{1}{n}\cos x\sin^{n-1} x + \dfrac{n-1}{n}I_{n-2}$ | $n \geq 2$ |
| $I_n = \int \cosh^n 2x\,\mathrm{d}x$ | $I_n = \dfrac{1}{2n}\sinh 2x\cosh^{n-1} 2x + \dfrac{n-1}{n}I_{n-2}$ | $n \geq 2$ |
| $I_n = \int \coth^n x\,\mathrm{d}x$ | $I_n = -\dfrac{1}{n-1}\coth^{n-1} x + I_{n-2}$ | $n \geq 2$ |
| $I_n = \int x^n e^x\,\mathrm{d}x$ | $I_n = x^n e^x - nI_{n-1}$ | $n \geq 1$ |
| $I_n = \int x^n\sqrt{x^2-1}\,\mathrm{d}x$ | $I_n = \dfrac{x^{n-1}(x^2-1)^{3/2}}{n+2} + \dfrac{n-1}{n+2}I_{n-2}$ | $n \geq 2$ |
| $I_n = \int_0^{\pi/4} \tan^n x\,\mathrm{d}x$ | $I_n = \dfrac{1}{n-1} - I_{n-2}$ | $n \geq 2$ |
| $I_n = \int_0^{\pi/2} x^n\cos x\,\mathrm{d}x$ | $I_n = \left(\dfrac{\pi}{2}\right)^n - n(n-1)I_{n-2}$ | $n \geq 2$ |

---

## Arc Lengths

**Cartesian:** $\displaystyle s = \int_a^b \sqrt{1 + \left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2}\,\mathrm{d}x$

**Parametric:** $\displaystyle s = \int_{t_1}^{t_2} \sqrt{\left(\frac{\mathrm{d}x}{\mathrm{d}t}\right)^2 + \left(\frac{\mathrm{d}y}{\mathrm{d}t}\right)^2}\,\mathrm{d}t$

**Polar:** $\displaystyle s = \int_{\alpha}^{\beta} \sqrt{r^2 + \left(\frac{\mathrm{d}r}{\mathrm{d}\theta}\right)^2}\,\mathrm{d}\theta$

---

## Surface Areas of Revolution

**About x-axis, Cartesian:** $\displaystyle S = \int_a^b 2\pi y\sqrt{1 + \left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2}\,\mathrm{d}x$

**About x-axis, parametric:** $\displaystyle S = \int_{t_1}^{t_2} 2\pi y\sqrt{\left(\frac{\mathrm{d}x}{\mathrm{d}t}\right)^2 + \left(\frac{\mathrm{d}y}{\mathrm{d}t}\right)^2}\,\mathrm{d}t$

**About y-axis, Cartesian:** $\displaystyle S = \int_a^b 2\pi x\sqrt{1 + \left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)^2}\,\mathrm{d}x$

**About y-axis, parametric:** $\displaystyle S = \int_{t_1}^{t_2} 2\pi x\sqrt{\left(\frac{\mathrm{d}x}{\mathrm{d}t}\right)^2 + \left(\frac{\mathrm{d}y}{\mathrm{d}t}\right)^2}\,\mathrm{d}t$

> **Not examinable:** surface area of revolution for **polar** curves ($r=f(\theta)$) - Cambridge explicitly excludes this (syllabus p.22). Only Cartesian and parametric surface areas are required.

---

## The Integral Test

If $f(x)$ is positive and decreasing, then $\sum_{n=a}^{\infty} f(n)$ converges $\iff$ $\int_a^{\infty} f(x)\,\mathrm{d}x$ converges.

**Unit-width bounds:** $\displaystyle \sum_{r=2}^{n} f(r) < \int_1^n f(x)\,\mathrm{d}x$

**Unit-width bounds:** $\displaystyle \sum_{r=1}^{n} f(r) > \int_1^{n+1} f(x)\,\mathrm{d}x$

**Riemann sum (width $\to 0$):** $\displaystyle \int_a^b f(x)\,\mathrm{d}x = \lim_{n\to\infty}\sum_{r=1}^{n} f\!\left(a+\frac{r(b-a)}{n}\right)\frac{b-a}{n}$

**Special case $[0,1]$:** $\displaystyle \int_0^1 f(x)\,\mathrm{d}x = \lim_{n\to\infty}\frac{1}{n}\sum_{r=1}^{n} f\!\left(\frac{r}{n}\right)$

**Upper/lower rule:** increasing + right = upper; decreasing + right = lower (left endpoints reverse it)

**p-series:** $\sum \dfrac{1}{n^p}$ converges $\iff p > 1$ (so $\sum \frac{1}{n}$ diverges, $\sum \frac{1}{n^2}$ converges)

---

# 🎯 CAMBRIDGE EXAM ANALYSIS

## Question Frequency (from the coursebook chapter and 9231 Paper 1/Paper 2 past papers)

### 🔴 Every Single Paper (100%)

| Topic | Typical Marks |
|---|---|
| Standard integrals with substitutions ($\sin u$, $\tan u$, $\sinh u$ route) | 4-6 |
| Reduction formulae (derive + apply once or twice) | 6-8 |
| Arc length or surface area of revolution | 7-9 |

### 🟡 Very Common (70%+)

| Topic |
|---|
| Completing the square then a standard integral |
| Hyperbolic function integrals (reverse chain rule, $\frac{1}{\sinh x}$ type) |
| Inverse hyperbolic / inverse trig integration by parts (the "1 Times" trick) |
| Parametric arc length (astroid-style curves) |

### 🟢 Sometimes (30-50%)

| Topic |
|---|
| Polar arc length ($r = \sin\theta$, $r = e^\theta$ type) |
| Surface area about the y-axis |
| Integral test / comparison test with upper and lower bounds |
| **Riemann sums with $\Delta x=(b-a)/n\to 0$ (new: explicitly on syllabus)** |
| $t=\tan\frac{x}{2}$ substitution for $\int \frac{1}{a+b\cos x + c\sin x}\,\mathrm{d}x$ (9709 technique in harder 9231 integrals) |

---

## Typical Mark Schemes

### Arc Length (8 marks) - e.g. 9231 Paper 1 Q8 Nov 2009

| Mark | What For |
|---|---|
| M1 | Differentiates the curve correctly |
| A1 | Correct $\frac{\mathrm{d}y}{\mathrm{d}x}$ |
| M1 | Substitutes into $s = \int\sqrt{1 + (dy/dx)^2}\,\mathrm{d}x$ |
| M1 | Simplifies using a trigonometric identity ($1 + \tan^2 x = \sec^2 x$) |
| M1 | Integrates (e.g. $\int\sec x\,\mathrm{d}x$) |
| A1 | Correct indefinite integral |
| M1 | Substitutes both limits |
| A1 | Final exact answer (e.g. $\ln(2 + \sqrt{3})$) |

### Surface Area (8 marks) - e.g. 9231 Paper 1 Q8 Nov 2009

| Mark | What For |
|---|---|
| B1 | Correct $\frac{\mathrm{d}y}{\mathrm{d}x}$ |
| M1 | Forms $\mathrm{d}s = \sqrt{1 + (dy/dx)^2}\,\mathrm{d}x$ |
| M1 | Correct formula $S = \int 2\pi y\,\mathrm{d}s$ (radius matched to axis) |
| M1A1 | Simplifies the integrand (cancellation inside square root) |
| M1 | Integrates |
| A1 | Substitutes limits correctly |
| A1 | Final answer in required form |

### Reduction Formula (7 marks)

| Mark | What For |
|---|---|
| M1 | Splits the power ($\cos^{n-1} x \cdot \cos x$) |
| M1A1 | Correct by-parts application |
| M1 | Uses the Pythagorean identity to eliminate the new power |
| M1 | Collects $I_n$ terms |
| A1 | Correct reduction formula with validity range |
| M1 | Applies the formula (or evaluates base case) |
| A1 | Final exact value |

---

# 🧠 COMMON MISTAKES

## 🔴 Critical Errors

| Mistake | Correction |
|---|---|
| $\int \frac{1}{\sqrt{x^2 + a^2}}\,\mathrm{d}x = \sin^{-1}\left(\frac{x}{a}\right)$ ❌ | It is $\sinh^{-1}\left(\frac{x}{a}\right) = \ln(x + \sqrt{x^2 + a^2})$ ✅ - the PLUS sign inside means hyperbolic |
| $\int \cosh x\,\mathrm{d}x = -\sinh x$ ❌ | $\int \cosh x\,\mathrm{d}x = +\sinh x$ ✅ (no negative for cosh) |
| Forgetting the $\frac{1}{a}$ or $\frac{1}{2a}$ factor in standard integrals ❌ | $\int \frac{1}{a^2+x^2}\,\mathrm{d}x = \frac{1}{a}\tan^{-1}\frac{x}{a}$ ✅ |
| Using $2\pi x$ when rotating about the x-axis ❌ | x-axis uses radius $y$: $2\pi y$; y-axis uses $2\pi x$ ✅ |
| Confusing surface area $S = \int 2\pi y\,\mathrm{d}s$ with volume $V = \pi\int y^2\,\mathrm{d}x$ ❌ | Surface area uses the ARC element $\mathrm{d}s$; volume uses $\mathrm{d}x$ ✅ |
| Reduction formula index wrong: $I_n$ in terms of $I_{n-1}$ for $\cos^n x$ ❌ | $\cos^n x$ reduces to $I_{n-2}$ (power drops by 2) ✅ |
| Integral test conclusion backwards: "curve diverges so sum converges" ❌ | If the curve (R) is below the rectangles (S) and R diverges, S diverges; if R > S and R converges, S converges ✅ |
| Riemann sum width wrong: using $1$ instead of $(b-a)/n$ ❌ | On $[a,b]$: $\Delta x=(b-a)/n$; on $[0,1]$: $\Delta x=1/n$ ✅ |
| Riemann upper/lower flipped ❌ | Increasing + right = upper, decreasing + right = lower (left endpoints reverse) ✅ |
| Confusing unit-width rectangles with width$\to 0$ rectangles ❌ | Unit-width tests *convergence* of $\sum f(n)$; width$\to 0$ evaluates *limits* of $\sum f(r/n)/n$ as $\int f$ ✅ |

## 🟡 Common Errors

| Error | Fix |
|---|---|
| Completing the square but forgetting the constant | $x^2 - 4x + 7 = (x-2)^2 + 3$, NOT $(x-2)^2$ |
| Substituting $x = a\tan u$ but using wrong identity | $a^2 + x^2$ needs $\sec^2$; $a^2 - x^2$ needs $\cos^2$ |
| Not changing limits when substituting in definite integrals | Always convert limits: $x = a\sin u \Rightarrow u = \sin^{-1}(x/a)$ |
| Forgetting $+c$ on indefinite integrals | One mark per integral - cheap to lose |
| Not stating validity range on reduction formulae | "$n \geq 2$" or "$n \geq 1$" is usually a B mark |
| Forgetting the $2\pi$ in surface area | $S = \int 2\pi(\text{radius})\,\mathrm{d}s$ - the $2\pi$ is the circumference |
| Partial fractions before integrating rational functions | For $\frac{1}{x^2 + bx + c}$: complete the square; for factorable denominators: partial fractions first |
| Integral test: forgetting to shift the integral | Upper bound: $\int_1^n$; lower bound: $\int_1^{n+1}$ - the $+1$ matters |

---

# 📚 PRACTICE QUESTIONS & SOLUTIONS

## Question 1 - Standard Integral with Completing the Square

> Find $\displaystyle \int \frac{1}{x^2 - 4x + 13}\,\mathrm{d}x$.

**Solution:**

Complete the square:

$$x^2 - 4x + 13 = (x - 2)^2 + 9$$

Let $u = x - 2$, so $\mathrm{d}u = \mathrm{d}x$:

$$\int \frac{1}{(x - 2)^2 + 9}\,\mathrm{d}x = \int \frac{1}{u^2 + 9}\,\mathrm{d}u$$

This matches $\int \frac{1}{u^2 + a^2}\,\mathrm{d}u = \frac{1}{a}\tan^{-1}\left(\frac{u}{a}\right)$ with $a = 3$:

$$\int \frac{1}{x^2 - 4x + 13}\,\mathrm{d}x = \frac{1}{3}\tan^{-1}\left(\frac{x - 2}{3}\right) + c \quad\checkmark$$

---

## Question 2 - Hyperbolic Integral

> Evaluate $\displaystyle \int_{\ln 2}^{\ln 3} \coth x\,\mathrm{d}x$, giving your answer in the form $\ln\left(\frac{a}{b}\right)$.

**Solution:**

$$\int \coth x\,\mathrm{d}x = \ln\lvert\sinh x\rvert + c$$

$$\int_{\ln 2}^{\ln 3} \coth x\,\mathrm{d}x = \left[\ln(\sinh x)\right]_{\ln 2}^{\ln 3}$$

$$\sinh(\ln 3) = \frac{3 - \frac{1}{3}}{2} = \frac{4}{3}, \qquad \sinh(\ln 2) = \frac{2 - \frac{1}{2}}{2} = \frac{3}{4}$$

$$= \ln\left(\frac{4}{3}\right) - \ln\left(\frac{3}{4}\right) = \ln\left(\frac{4}{3} \times \frac{4}{3}\right) = \ln\left(\frac{16}{9}\right) \approx 0.5754 \quad\checkmark$$

---

## Question 3 - Integration by Parts with Inverse Hyperbolic

> Evaluate $\displaystyle \int_0^{1/2} \sinh^{-1} x\,\mathrm{d}x$.

**Solution:**

Use the "1 Times" trick ($u = \sinh^{-1} x$, $\frac{\mathrm{d}v}{\mathrm{d}x} = 1$):

$$\int \sinh^{-1} x\,\mathrm{d}x = x\sinh^{-1} x - \int x \cdot \frac{1}{\sqrt{1 + x^2}}\,\mathrm{d}x$$

The second integral is a reverse chain rule:

$$\int \frac{x}{\sqrt{1 + x^2}}\,\mathrm{d}x = \sqrt{1 + x^2}$$

$$\int_0^{1/2} \sinh^{-1} x\,\mathrm{d}x = \left[x\sinh^{-1} x - \sqrt{1 + x^2}\right]_0^{1/2}$$

At $x = \frac{1}{2}$: $\sinh^{-1}\left(\frac{1}{2}\right) = \ln\left(\frac{1}{2} + \frac{\sqrt{5}}{2}\right) = \ln\left(\frac{1 + \sqrt{5}}{2}\right)$, and $\sqrt{1 + \frac{1}{4}} = \frac{\sqrt{5}}{2}$.

At $x = 0$: both terms are 0 and $-1$:

$$= \frac{1}{2}\ln\left(\frac{1 + \sqrt{5}}{2}\right) - \frac{\sqrt{5}}{2} + 1 \approx 0.1226 \quad\checkmark$$

---

## Question 4 - Reduction Formula

> Given that $I_n = \int_0^{\pi/2} \cos^n x\,\mathrm{d}x$, show that $I_n = \frac{n-1}{n}I_{n-2}$ and hence find $I_6$.

**Solution:**

From the reduction formula, the bracket term vanishes at both limits (since $\sin 0 = 0$ and $\cos\frac{\pi}{2} = 0$):

$$I_n = \left[\frac{1}{n}\cos^{n-1} x\sin x\right]_0^{\pi/2} + \frac{n-1}{n}I_{n-2} = \frac{n-1}{n}I_{n-2} \quad\checkmark$$

Cascade down:

$$I_6 = \frac{5}{6}I_4, \qquad I_4 = \frac{3}{4}I_2, \qquad I_2 = \frac{1}{2}I_0$$

$$I_0 = \int_0^{\pi/2} 1\,\mathrm{d}x = \frac{\pi}{2}$$

$$I_6 = \frac{5}{6} \cdot \frac{3}{4} \cdot \frac{1}{2} \cdot \frac{\pi}{2} = \frac{5\pi}{32} \approx 0.4909 \quad\checkmark$$

---

## Question 5 - Polar Arc Length

> Find, to three decimal places, the length of the polar curve $r = \theta$ from $\theta = 0.1$ to $\theta = 0.3$.
> *(Cambridge International AS & A Level Further Mathematics 9231, Exercise 22C Q8)*

**Solution:**

$$\frac{\mathrm{d}r}{\mathrm{d}\theta} = 1$$

$$s = \int_{0.1}^{0.3} \sqrt{\theta^2 + 1}\,\mathrm{d}\theta$$

$$\int \sqrt{\theta^2 + 1}\,\mathrm{d}\theta = \frac{1}{2}\left(\theta\sqrt{\theta^2 + 1} + \sinh^{-1}\theta\right)$$

$$s = \frac{1}{2}\left[\theta\sqrt{\theta^2 + 1} + \sinh^{-1}\theta\right]_{0.1}^{0.3}$$

$$s \approx 0.2043 \quad\checkmark$$

---

## Question 6 - Surface Area

> The curve $y = x^2$ from $x = 1$ to $x = 2$ is rotated about the y-axis. Find the surface area generated.

**Solution:**

About the y-axis, the radius is $x$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = 2x$$

$$S = \int_1^2 2\pi x\sqrt{1 + (2x)^2}\,\mathrm{d}x = \int_1^2 2\pi x\sqrt{1 + 4x^2}\,\mathrm{d}x$$

Reverse chain rule (derivative of $1 + 4x^2$ is $8x$):

$$S = 2\pi \cdot \frac{1}{8} \cdot \frac{2}{3}\left[(1 + 4x^2)^{3/2}\right]_1^2 = \frac{\pi}{6}\left(17^{3/2} - 5^{3/2}\right)$$

$$S = \frac{\pi}{6}\left(17\sqrt{17} - 5\sqrt{5}\right) \approx 30.85 \quad\checkmark$$

---

## Question 7 - Integral Test

> By using the integral test, determine whether $\displaystyle \sum_{n=1}^{\infty} \frac{1}{n^2 + 1}$ converges or diverges.

**Solution:**

Since $n^2 + 1 > n^2$, each term satisfies $\frac{1}{n^2 + 1} < \frac{1}{n^2}$, and $\sum \frac{1}{n^2}$ converges (p-series with $p = 2 > 1$). By comparison, the sum converges.

Alternatively, using the integral test directly:

$$\int_1^{\infty} \frac{1}{x^2 + 1}\,\mathrm{d}x = \left[\tan^{-1} x\right]_1^{\infty} = \frac{\pi}{2} - \frac{\pi}{4} = \frac{\pi}{4}$$

The integral is finite, so the sum converges (to a value near 1.077). $\quad\checkmark$

---

# ⏱️ EXAM STRATEGY

## 48 Hours Before

### Memorisation Checklist
- [ ] The Big Five standard integrals (with the $\frac{1}{a}$ factors!)
- [ ] Substitution table: which of $\sin u$ / $\tan u$ / $\sinh u$ / $\cosh u$ / $\tanh u$ for which form
- [ ] All 9 hyperbolic function integrals
- [ ] The 6 inverse function integrals (the "1 Times" trick)
- [ ] All 8 reduction formulae (indefinite AND definite forms)
- [ ] Arc length: Cartesian / parametric / polar
- [ ] Surface area: x-axis vs y-axis, Cartesian vs parametric
- [ ] Integral test rules (which R/S comparisons give conclusions)

### Practice Checklist
- [ ] 2 standard integral questions (one with completing the square)
- [ ] 2 hyperbolic integral questions
- [ ] 2 reduction formula questions (one derive, one apply)
- [ ] 1 arc length question
- [ ] 1 surface area question
- [ ] 1 integral test question

---

## In The Exam

| When You See... | Do This |
|---|---|
| $\frac{1}{x^2 + a^2}$ or $\frac{1}{\sqrt{a^2 - x^2}}$ type | Match the form to the Big Five; watch the sign inside the root |
| Quadratic denominator | Complete the square FIRST |
| $\sqrt{a^2 - x^2}$ in a hard integral | $x = a\sin u$ (avoid the $\tanh$ route) |
| $\sqrt{x^2 + a^2}$ | $x = a\sinh u$ or $x = a\tan u$ |
| "Show that $I_n = \ldots$" | Split power, by parts, Pythagorean identity, collect $I_n$ terms, state validity |
| "Find the length of the arc" | Pick Cartesian / parametric / polar formula, substitute, simplify, integrate |
| "Rotated about the x-axis" | Surface area: radius $= y$, use $2\pi y\,\mathrm{d}s$ |
| "Rotated about the y-axis" | Surface area: radius $= x$, use $2\pi x\,\mathrm{d}s$ |
| "Converges or diverges" | Integral test or comparison test; check the direction of the R/S rules |
| "Find the exact value" | Keep $\pi$, $\ln$, $\sqrt{}$ in the answer - do not round |

---

## Last-Resort Tips

1. **Can't remember a standard integral?** Re-derive from derivatives:
   - $\frac{\mathrm{d}}{\mathrm{d}x}\left(\tan^{-1} x\right) = \frac{1}{1 + x^2}$ so $\int \frac{1}{1+x^2}\,\mathrm{d}x = \tan^{-1} x$
   - $\frac{\mathrm{d}}{\mathrm{d}x}\left(\ln(x + \sqrt{x^2 + 1})\right) = \frac{1}{\sqrt{x^2+1}}$

2. **Reduction formula too hard?** Write the integration by parts setup anyway - you get M marks for the split and the parts step.

3. **Arc length integral looks impossible?** Check for identities: $1 + \tan^2 x = \sec^2 x$, $1 + \sinh^2 x = \cosh^2 x$, $\sin^2 t + \cos^2 t = 1$. The simplification is almost always the point of the question.

4. **Running out of time?** Write down the correct formula and the correct derivative - those are B/M marks even if you do not finish the integration.

---

# QUICK REFERENCE CARD

Cut this out for last-minute revision.

### The Big Five

$$\int \frac{1}{a^2 + x^2}\,\mathrm{d}x = \frac{1}{a}\tan^{-1}\left(\frac{x}{a}\right)$$

$$\int \frac{1}{\sqrt{a^2 - x^2}}\,\mathrm{d}x = \sin^{-1}\left(\frac{x}{a}\right)$$

$$\int \frac{1}{a^2 - x^2}\,\mathrm{d}x = \frac{1}{a}\tanh^{-1}\left(\frac{x}{a}\right)$$

$$\int \frac{1}{\sqrt{x^2 + a^2}}\,\mathrm{d}x = \sinh^{-1}\left(\frac{x}{a}\right)$$

$$\int \frac{1}{\sqrt{x^2 - a^2}}\,\mathrm{d}x = \cosh^{-1}\left(\frac{x}{a}\right)$$

### Substitutions

$$a^2 - x^2 \to x = a\sin u, \qquad a^2 + x^2 \to x = a\tan u \text{ or } a\sinh u, \qquad x^2 - a^2 \to x = a\cosh u$$

### Reduction Formula Master List

$$\int \cos^n x = \frac{1}{n}\cos^{n-1} x\sin x + \frac{n-1}{n}I_{n-2}$$

$$\int \sin^n x = -\frac{1}{n}\cos x\sin^{n-1} x + \frac{n-1}{n}I_{n-2}$$

$$\int x^n e^x = x^n e^x - nI_{n-1}$$

$$\int \coth^n x = -\frac{1}{n-1}\coth^{n-1} x + I_{n-2}$$

### Arc Length & Surface Area

$$s = \int \sqrt{1 + (dy/dx)^2}\,\mathrm{d}x \quad \text{(Cartesian)}$$

$$s = \int \sqrt{(dx/dt)^2 + (dy/dt)^2}\,\mathrm{d}t \quad \text{(parametric)}$$

$$s = \int \sqrt{r^2 + (dr/d\theta)^2}\,\mathrm{d}\theta \quad \text{(polar)}$$

$$S_{\text{x-axis}} = \int 2\pi y\,\mathrm{d}s, \qquad S_{\text{y-axis}} = \int 2\pi x\,\mathrm{d}s$$

### Integral Test

$$\sum \frac{1}{n^p} \text{ converges } \iff p > 1$$

$$\text{Unit-width: } \sum_{r=2}^n f(r) < \int_1^n f, \qquad \text{Lower: } \sum_{r=1}^n f(r) > \int_1^{n+1} f$$

$$\text{Riemann (width $\to 0$): } \int_a^b f = \lim_{n\to\infty}\sum_{r=1}^{n} f\!\left(a+\tfrac{r(b-a)}{n}\right)\tfrac{b-a}{n}, \quad \int_0^1 f = \lim_{n\to\infty}\tfrac1n\sum f(r/n)$$

### Deadly Sins

1. $\int \frac{1}{\sqrt{x^2 + a^2}}\,\mathrm{d}x \neq \sin^{-1}$ (it is $\sinh^{-1}$; the PLUS sign means hyperbolic)
2. $\int \cosh x\,\mathrm{d}x \neq -\sinh x$ (it is $+\sinh x$)
3. Surface area $\neq \pi y^2$ (that is volume; surface area uses $2\pi y\,\mathrm{d}s$)
4. Rotating about x-axis $\neq 2\pi x$ (x-axis uses $y$ as radius, y-axis uses $x$)

---

> **Good luck! You've got this.** Every Cambridge integration question follows one of the patterns in this guide. 🚀

---

📁 **File saved to:** `/Users/adityabalaji/Documents/Codex/further-maths/pure/FURTHER_MATHS_INTEGRATION_COMPLETE_GUIDE.md`
