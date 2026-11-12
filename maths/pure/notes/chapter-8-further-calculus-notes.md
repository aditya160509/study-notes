# 📘 Chapter 8: Further Calculus - 9709 Pure Mathematics 3 (CAIE A Level Maths)

## Cambridge International AS & A Level Mathematics (9709) - Paper 3

> **The complete walkthrough:** four new weapons added to your Chapter 5 toolkit - the derivative of $\tan^{-1}x$, the integral $\int \frac{1}{x^2+a^2}\,\mathrm{d}x$, integration by substitution, and integration by parts - plus feeding partial fractions into integrals. Every technique is built from fully solved examples.

---

# 📋 Table of Contents

1. [PART 1: The Derivative of $\tan^{-1}x$ and Integrating $\frac{1}{x^2+a^2}$](#part-1-the-derivative-of-tan-1x-and-integrating-1x2a2)
2. [PART 2: Integration of $\frac{k\,f'(x)}{f(x)}$](#part-2-integration-of-kfx-fx)
3. [PART 3: Integration by Substitution](#part-3-integration-by-substitution)
4. [PART 4: Partial Fractions in Integration](#part-4-partial-fractions-in-integration)
5. [PART 5: Integration by Parts](#part-5-integration-by-parts)
6. [Formula Sheet](#formula-sheet)
7. [Quick Reference Card](#quick-reference-card)

---

# PART 1: The Derivative of $\tan^{-1}x$ and Integrating $\frac{1}{x^2+a^2}$

This part adds one new derivative (which unlocks a whole family of integrals) and turns it into the standard integral $\int \frac{1}{x^2+a^2}\,\mathrm{d}x = \frac{1}{a}\tan^{-1}\left(\frac{x}{a}\right) + c$. Derivatives of $\sin^{-1}x$ and $\cos^{-1}x$ are NOT on the syllabus - do not waste time on them.

## 1.1 The Derivative of $\tan^{-1}x$

$y = \tan^{-1}x$ means $\tan y = x$ with $-\frac{\pi}{2} < y < \frac{\pi}{2}$. It is the inverse of the restricted tangent function, NOT $\frac{1}{\tan x}$. The derivative is proved by implicit differentiation:

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(\tan^{-1}x\right) = \frac{1}{1+x^2}$$

### Example 1 - Easy - Proving the derivative of $\tan^{-1}x$ (coursebook Section 8.1)

> **Question:** Show that $\frac{\mathrm{d}}{\mathrm{d}x}\left(\tan^{-1}x\right) = \frac{1}{1+x^2}$.

**Solution:**

Let $y = \tan^{-1}x$:

$$\tan y = x$$

Differentiate both sides with respect to $x$ (chain rule on $\tan y$):

$$\sec^2 y \cdot \frac{\mathrm{d}y}{\mathrm{d}x} = 1$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{1}{\sec^2 y}$$

Use the Pythagorean identity $\sec^2 y = 1 + \tan^2 y$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{1}{1 + \tan^2 y}$$

Since $\tan y = x$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{1}{1+x^2} \quad\checkmark$$

**What the examiner wants:** the implicit differentiation route with $\sec^2 y = 1 + \tan^2 y$ written out.

## 1.2 The Chain Rule for $\tan^{-1}\big(f(x)\big)$

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(\tan^{-1}\big(f(x)\big)\right) = \frac{f'(x)}{1 + \big(f(x)\big)^2}$$

For example $\frac{\mathrm{d}}{\mathrm{d}x}\left(\tan^{-1}(3x)\right) = \frac{3}{1+9x^2}$ and $\frac{\mathrm{d}}{\mathrm{d}x}\left(\tan^{-1}(x^2)\right) = \frac{2x}{1+x^4}$.

> ⭐ **Watch Out!** $\tan^{-1}x$ is NOT $\frac{1}{\tan x}$. The June 2023 examiner report flags candidates who "suggested that $\tan^{-1}3a$ was the reciprocal of $\tan 3a$". Also: never forget the chain-rule factor $f'(x)$ on top.

### Example 2 - Medium - Differentiating $\tan^{-1}$ composites (coursebook Worked Example 8.1)

> **Question:** Differentiate with respect to $x$: (a) $\tan^{-1}(3x)$; (b) $\tan^{-1}\sqrt{x}$; (c) $\tan^{-1}\left(\frac{x}{x-2}\right)$.

**Solution:**

Part (a) - $f(x) = 3x$, so $f'(x) = 3$:

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(\tan^{-1}(3x)\right) = \frac{3}{1 + (3x)^2}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(\tan^{-1}(3x)\right) = \frac{3}{1 + 9x^2} \quad\checkmark$$

Part (b) - $f(x) = \sqrt{x}$, so $f'(x) = \frac{1}{2\sqrt{x}}$:

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(\tan^{-1}\sqrt{x}\right) = \frac{\frac{1}{2\sqrt{x}}}{1 + \left(\sqrt{x}\right)^2}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(\tan^{-1}\sqrt{x}\right) = \frac{\frac{1}{2\sqrt{x}}}{1 + x}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(\tan^{-1}\sqrt{x}\right) = \frac{1}{2\sqrt{x}(1+x)} \quad\checkmark$$

Part (c) - $f(x) = \frac{x}{x-2}$, quotient rule for $f'(x)$:

$$f'(x) = \frac{(x-2)(1) - x(1)}{(x-2)^2} = \frac{x - 2 - x}{(x-2)^2}$$

$$f'(x) = \frac{-2}{(x-2)^2}$$

Substitute into the chain-rule form:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\frac{-2}{(x-2)^2}}{1 + \left(\frac{x}{x-2}\right)^2}$$

Multiply numerator and denominator by $(x-2)^2$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{-2}{(x-2)^2 + x^2}$$

Expand the denominator:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{-2}{x^2 - 4x + 4 + x^2} = \frac{-2}{2x^2 - 4x + 4}$$

Divide top and bottom by 2:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{-1}{x^2 - 2x + 2} \quad\checkmark$$

**What the examiner wants:** chain rule applied to $\tan^{-1}$ with clean algebra at the end; the final simplification to a single fraction is where most marks are lost.

### Example 3 - Medium - Tangent to a $\tan^{-1}$ curve (coursebook Exercise 8A Q3, computed estimate)

> **Question:** Find the equation of the tangent to the curve $y = \tan^{-1}\left(\frac{x}{2}\right)$ at the point where $x = 2$.

**Solution:**

Differentiate with the chain rule:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\frac{1}{2}}{1 + \left(\frac{x}{2}\right)^2}$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\frac{1}{2}}{\frac{4 + x^2}{4}} = \frac{2}{4 + x^2}$$

Gradient at $x = 2$:

$$m = \frac{2}{4 + 4} = \frac{2}{8} = \frac{1}{4}$$

The point of contact:

$$y(2) = \tan^{-1}\left(\frac{2}{2}\right) = \tan^{-1}(1) = \frac{\pi}{4}$$

Tangent through $\left(2, \frac{\pi}{4}\right)$ with gradient $\frac{1}{4}$:

$$y - \frac{\pi}{4} = \frac{1}{4}(x - 2)$$

$$y = \frac{x}{4} - \frac{1}{2} + \frac{\pi}{4} \quad\checkmark$$

**What the examiner wants:** exact evaluation $\tan^{-1}1 = \frac{\pi}{4}$ in RADIANS (degrees are a mark-killer in P3), and a tidy final line.

## 1.3 Integrating $\frac{1}{x^2 + a^2}$

$$\int \frac{1}{x^2 + a^2}\,\mathrm{d}x = \frac{1}{a}\tan^{-1}\left(\frac{x}{a}\right) + c$$

The $\frac{1}{a}$ comes from the chain rule: differentiating $\frac{1}{a}\tan^{-1}\left(\frac{x}{a}\right)$ gives $\frac{1}{a} \cdot \frac{1/a}{1 + x^2/a^2} = \frac{1}{x^2 + a^2}$.

> ⭐ **Watch Out!** Forgetting the $\frac{1}{a}$ factor is the single most common error in this chapter. If the denominator has a coefficient, e.g. $\frac{1}{kx^2 + a^2}$, factor out $k$ FIRST to reach the form $x^2 + a^2$.

### Example 4 - Easy - The basic arctan integrals (coursebook Worked Examples 8.2 - 8.4)

> **Question:** Find (a) $\int \frac{1}{x^2+25}\,\mathrm{d}x$; (b) $\int \frac{1}{2x^2+3}\,\mathrm{d}x$; (c) the exact value of $\int_0^2 \frac{1}{x^2+4}\,\mathrm{d}x$.

**Solution:**

Part (a) - $a^2 = 25$, so $a = 5$:

$$\int \frac{1}{x^2 + 25}\,\mathrm{d}x = \frac{1}{5}\tan^{-1}\left(\frac{x}{5}\right) + c \quad\checkmark$$

Part (b) - factor out the 2 to create $x^2 + a^2$:

$$\int \frac{1}{2x^2 + 3}\,\mathrm{d}x = \frac{1}{2}\int \frac{1}{x^2 + \frac{3}{2}}\,\mathrm{d}x$$

Here $a^2 = \frac{3}{2}$, so $a = \sqrt{\frac{3}{2}}$:

$$\int \frac{1}{2x^2 + 3}\,\mathrm{d}x = \frac{1}{2} \cdot \frac{1}{\sqrt{\frac{3}{2}}} \tan^{-1}\left(\frac{x}{\sqrt{\frac{3}{2}}}\right) + c$$

$$\int \frac{1}{2x^2 + 3}\,\mathrm{d}x = \frac{1}{2}\sqrt{\frac{2}{3}}\,\tan^{-1}\left(\sqrt{\frac{2}{3}}\,x\right) + c \quad\checkmark$$

Part (c) - $a^2 = 4$, so $a = 2$:

$$\int_0^2 \frac{1}{x^2 + 4}\,\mathrm{d}x = \left[\frac{1}{2}\tan^{-1}\left(\frac{x}{2}\right)\right]_0^2$$

$$\int_0^2 \frac{1}{x^2 + 4}\,\mathrm{d}x = \frac{1}{2}\tan^{-1}(1) - \frac{1}{2}\tan^{-1}(0)$$

$$\int_0^2 \frac{1}{x^2 + 4}\,\mathrm{d}x = \frac{1}{2} \cdot \frac{\pi}{4} - \frac{1}{2} \cdot 0 = \frac{\pi}{8} \quad\checkmark$$

**What the examiner wants:** the $\frac{1}{a}$ coefficient every time, exact $\tan^{-1}$ values at the limits, and no decimals for "exact value".

## 1.4 Arctan Integrals Inside Differential Equations and with Coefficients

This integral appears constantly in Chapter 10 (differential equations), usually written $\int \frac{\mathrm{d}y}{a^2 + y^2}$. The key is to rewrite the denominator as $a^2\left(1 + \left(\frac{y}{a}\right)^2\right)$ first.

### Example 5 - Medium - Arctan inside a differential equation (June 2023 Paper 32 Q8, computed estimate)

> **Question:** From the June 2023 Paper 32 differential equation question, the integral $\int \frac{\mathrm{d}y}{4 + 9y^2}$ was required. Evaluate it.

**Solution:**

Factor the 4 out of the denominator:

$$4 + 9y^2 = 4\left(1 + \frac{9y^2}{4}\right) = 4\left(1 + \left(\frac{3y}{2}\right)^2\right)$$

$$\int \frac{\mathrm{d}y}{4 + 9y^2} = \frac{1}{4}\int \frac{\mathrm{d}y}{1 + \left(\frac{3y}{2}\right)^2}$$

Let $u = \frac{3y}{2}$, so $\frac{\mathrm{d}u}{\mathrm{d}y} = \frac{3}{2}$ and $\mathrm{d}y = \frac{2}{3}\,\mathrm{d}u$:

$$\int \frac{\mathrm{d}y}{4 + 9y^2} = \frac{1}{4} \cdot \frac{2}{3} \int \frac{\mathrm{d}u}{1 + u^2}$$

$$\int \frac{\mathrm{d}y}{4 + 9y^2} = \frac{1}{6}\tan^{-1}\left(\frac{3y}{2}\right) + c \quad\checkmark$$

**What the examiner wants:** the coefficient $\frac{1}{6}$ (common wrong answers: $\frac{1}{2}$), and $\frac{3y}{2}$ inside the arctan with the CORRECT variable. The June 2023 Paper 32 report: candidates got $\frac{1}{2}$ instead of $\frac{1}{6}$, or wrote $\tan^{-1}\left(\frac{x}{2}\right)$ with the wrong variable.

### Example 6 - Medium - Exact values of definite arctan integrals (coursebook Exercise 8B style, computed estimate)

> **Question:** Find the exact value of (a) $\int_0^3 \frac{1}{x^2+9}\,\mathrm{d}x$; (b) $\int_1^{\sqrt{3}} \frac{1}{x^2+1}\,\mathrm{d}x$.

**Solution:**

Part (a) - $a^2 = 9$, so $a = 3$:

$$\int_0^3 \frac{1}{x^2 + 9}\,\mathrm{d}x = \left[\frac{1}{3}\tan^{-1}\left(\frac{x}{3}\right)\right]_0^3$$

$$\int_0^3 \frac{1}{x^2 + 9}\,\mathrm{d}x = \frac{1}{3}\tan^{-1}(1) - \frac{1}{3}\tan^{-1}(0)$$

$$\int_0^3 \frac{1}{x^2 + 9}\,\mathrm{d}x = \frac{1}{3} \cdot \frac{\pi}{4} - 0 = \frac{\pi}{12} \quad\checkmark$$

Part (b) - $a^2 = 1$, so $a = 1$:

$$\int_1^{\sqrt{3}} \frac{1}{x^2 + 1}\,\mathrm{d}x = \left[\tan^{-1}x\right]_1^{\sqrt{3}}$$

$$\int_1^{\sqrt{3}} \frac{1}{x^2 + 1}\,\mathrm{d}x = \tan^{-1}\left(\sqrt{3}\right) - \tan^{-1}(1)$$

$$\int_1^{\sqrt{3}} \frac{1}{x^2 + 1}\,\mathrm{d}x = \frac{\pi}{3} - \frac{\pi}{4} = \frac{\pi}{12} \quad\checkmark$$

**What the examiner wants:** the standard exact values $\tan^{-1}0 = 0$, $\tan^{-1}1 = \frac{\pi}{4}$, $\tan^{-1}\sqrt{3} = \frac{\pi}{3}$, all in radians.

### Practice Questions - Part 1

1. (Easy) Differentiate with respect to $x$: (a) $\tan^{-1}(2x)$; (b) $\tan^{-1}(x^2)$.
2. (Medium) Find the equation of the normal to the curve $y = \tan^{-1}x$ at the point where $x = 1$.
3. (Easy) Find the exact value of $\int_0^4 \frac{1}{x^2+16}\,\mathrm{d}x$.
4. (Medium) Find $\int \frac{1}{9x^2+1}\,\mathrm{d}x$, and hence the exact value of $\int_0^{1/\sqrt{3}} \frac{1}{9x^2+1}\,\mathrm{d}x$.

**Solutions:**

Question 1(a):

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(\tan^{-1}(2x)\right) = \frac{2}{1 + (2x)^2} = \frac{2}{1 + 4x^2} \quad\checkmark$$

Question 1(b):

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(\tan^{-1}(x^2)\right) = \frac{2x}{1 + (x^2)^2} = \frac{2x}{1 + x^4} \quad\checkmark$$

Question 2 - gradient of the tangent at $x = 1$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{1}{1+x^2}$$

$$m_{\text{tangent}} = \frac{1}{1+1} = \frac{1}{2}$$

$$m_{\text{normal}} = -\frac{1}{m_{\text{tangent}}} = -2$$

Point of contact:

$$y(1) = \tan^{-1}(1) = \frac{\pi}{4}$$

Normal through $\left(1, \frac{\pi}{4}\right)$:

$$y - \frac{\pi}{4} = -2(x - 1)$$

$$y = -2x + 2 + \frac{\pi}{4} \quad\checkmark$$

Question 3 - $a^2 = 16$, so $a = 4$:

$$\int_0^4 \frac{1}{x^2+16}\,\mathrm{d}x = \left[\frac{1}{4}\tan^{-1}\left(\frac{x}{4}\right)\right]_0^4$$

$$\int_0^4 \frac{1}{x^2+16}\,\mathrm{d}x = \frac{1}{4}\tan^{-1}(1) - \frac{1}{4}\tan^{-1}(0) = \frac{1}{4} \cdot \frac{\pi}{4} = \frac{\pi}{16} \quad\checkmark$$

Question 4 - rewrite the denominator as $(3x)^2 + 1$:

$$9x^2 + 1 = (3x)^2 + 1^2$$

$$\int \frac{1}{9x^2+1}\,\mathrm{d}x = \frac{1}{3}\tan^{-1}(3x) + c \quad\checkmark$$

Definite version:

$$\int_0^{1/\sqrt{3}} \frac{1}{9x^2+1}\,\mathrm{d}x = \left[\frac{1}{3}\tan^{-1}(3x)\right]_0^{1/\sqrt{3}}$$

$$\int_0^{1/\sqrt{3}} \frac{1}{9x^2+1}\,\mathrm{d}x = \frac{1}{3}\tan^{-1}\left(\sqrt{3}\right) - \frac{1}{3}\tan^{-1}(0) = \frac{1}{3} \cdot \frac{\pi}{3} = \frac{\pi}{9} \quad\checkmark$$

---

# PART 2: Integration of $\frac{k\,f'(x)}{f(x)}$

This part covers recognising when an integrand is a constant multiple of $\frac{f'(x)}{f(x)}$ and turning it into a logarithm. It is the single most frequently reused pattern in the whole of P3.

## 2.1 The Core Rule - Spotting $\frac{k\,f'(x)}{f(x)}$

$$\int \frac{k\,f'(x)}{f(x)}\,\mathrm{d}x = k\ln\big|f(x)\big| + c$$

**How to spot it:** differentiate the denominator in your head. If the numerator is a constant multiple of that derivative, the integral is a logarithm. The modulus bars matter: $\ln$ is only defined for positive inputs. When the domain guarantees $f(x) > 0$, Cambridge often drops the bars - but writing $|f(x)|$ is always safe.

> ⭐ **Watch Out!** Missing the constant $k$ is the classic error. If the numerator is $2f'(x)$, the answer is $2\ln|f(x)|$, not $\ln|f(x)|$. Also never split a sum in the denominator term-by-term: $\frac{1}{5x + \frac{x^2}{3}} \neq \frac{1}{5x} + \frac{1}{x^2/3}$ (June 2023 Paper 33 Q11 report).

### Example 7 - Easy - Numerator matches $f'(x)$ exactly (coursebook Worked Example 8.5)

> **Question:** Find $\int \frac{2x}{x^2+3}\,\mathrm{d}x$.

**Solution:**

Name the denominator and differentiate it:

$$f(x) = x^2 + 3 \quad\Rightarrow\quad f'(x) = 2x$$

The numerator is exactly $f'(x)$, so $k = 1$:

$$\int \frac{2x}{x^2+3}\,\mathrm{d}x = \int \frac{f'(x)}{f(x)}\,\mathrm{d}x$$

$$\int \frac{2x}{x^2+3}\,\mathrm{d}x = \ln\big|x^2+3\big| + c \quad\checkmark$$

**What the examiner wants:** the recognition step written down - naming $f(x)$ and $f'(x)$ earns the method marks even if the log is miswritten.

### Example 8 - Medium - Numerator is a multiple of $f'(x)$ (coursebook Worked Example 8.7)

> **Question:** Find $\int \frac{3x^2 + 5x}{2x^3 + 5x^2}\,\mathrm{d}x$.

**Solution:**

Name the denominator and differentiate:

$$f(x) = 2x^3 + 5x^2 \quad\Rightarrow\quad f'(x) = 6x^2 + 10x$$

Factor the derivative to compare with the numerator:

$$f'(x) = 2(3x^2 + 5x)$$

So the numerator is $\frac{1}{2}f'(x)$, giving $k = \frac{1}{2}$:

$$\int \frac{3x^2 + 5x}{2x^3 + 5x^2}\,\mathrm{d}x = \frac{1}{2}\int \frac{f'(x)}{f(x)}\,\mathrm{d}x$$

$$\int \frac{3x^2 + 5x}{2x^3 + 5x^2}\,\mathrm{d}x = \frac{1}{2}\ln\big|2x^3 + 5x^2\big| + c \quad\checkmark$$

**What the examiner wants:** writing $\frac{3x^2+5x}{2x^3+5x^2}$ as $\frac{1}{2}\cdot\frac{6x^2+10x}{2x^3+5x^2}$ explicitly. The common wrong answer is $\ln|2x^3+5x^2|$ with no $\frac{1}{2}$.

## 2.2 Trig Versions of $\frac{k\,f'(x)}{f(x)}$

The trig integrals $\tan$, $\cot$, $\sec\tan$, $\sec^2\tan$ are all $\frac{k f'}{f}$ in disguise:

| Integral | Rewrite | $f(x)$ | $k$ | Result |
|---|---|---|---|---|
| $\int \tan x\,\mathrm{d}x$ | $\frac{\sin x}{\cos x}$ | $\cos x$ | $-1$ | $-\ln|\cos x| + c = \ln|\sec x| + c$ |
| $\int \cot x\,\mathrm{d}x$ | $\frac{\cos x}{\sin x}$ | $\sin x$ | $1$ | $\ln|\sin x| + c$ |
| $\int \sec x \tan x\,\mathrm{d}x$ | itself | $\sec x$ | $1$ | $\ln|\sec x| + c$ |

### Example 9 - Medium - $\int \tan 3x\,\mathrm{d}x$ (coursebook Worked Example 8.6)

> **Question:** Find $\int \tan 3x\,\mathrm{d}x$.

**Solution:**

Rewrite $\tan 3x$ as a quotient:

$$\int \tan 3x\,\mathrm{d}x = \int \frac{\sin 3x}{\cos 3x}\,\mathrm{d}x$$

Name the denominator and differentiate:

$$f(x) = \cos 3x \quad\Rightarrow\quad f'(x) = -3\sin 3x$$

So $\sin 3x = -\frac{1}{3}f'(x)$, giving $k = -\frac{1}{3}$:

$$\int \tan 3x\,\mathrm{d}x = -\frac{1}{3}\int \frac{-3\sin 3x}{\cos 3x}\,\mathrm{d}x$$

$$\int \tan 3x\,\mathrm{d}x = -\frac{1}{3}\ln\big|\cos 3x\big| + c \quad\checkmark$$

**What the examiner wants:** the minus sign (from $f'(x) = -3\sin 3x$) and the $\frac{1}{3}$ both present. Getting $+\frac{1}{3}\ln|\cos 3x|$ is a classic sign slip.

### Example 10 - Medium - $\sec 2x \tan 2x$ as $\frac{k f'}{f}$ (June 2023 Paper 31 examiner report)

> **Question:** Find (a) $\int \cot x\,\mathrm{d}x$; (b) $\int \sec 2x \tan 2x\,\mathrm{d}x$.

**Solution:**

Part (a):

$$\int \cot x\,\mathrm{d}x = \int \frac{\cos x}{\sin x}\,\mathrm{d}x$$

$$f(x) = \sin x \quad\Rightarrow\quad f'(x) = \cos x$$

The numerator is exactly $f'(x)$, so $k = 1$:

$$\int \cot x\,\mathrm{d}x = \ln\big|\sin x\big| + c \quad\checkmark$$

Part (b) - differentiate $f(x) = \sec 2x$:

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(\sec 2x\right) = 2\sec 2x \tan 2x$$

So $\sec 2x \tan 2x = \frac{1}{2}f'(x)$, giving $k = \frac{1}{2}$:

$$\int \sec 2x \tan 2x\,\mathrm{d}x = \frac{1}{2}\int \frac{2\sec 2x \tan 2x}{\sec 2x}\,\mathrm{d}x$$

$$\int \sec 2x \tan 2x\,\mathrm{d}x = \frac{1}{2}\ln\big|\sec 2x\big| + c \quad\checkmark$$

**What the examiner wants:** the June 2023 Paper 31 examiner report praises candidates who recognised $\sec 2x \tan 2x$ as a $\frac{k f'}{f}$ form inside a differential equation; the $\frac{1}{2}$ is the mark.

## 2.3 Definite Integrals with Log Simplification

For definite integrals, substitute the limits and combine the logs with $\ln A - \ln B = \ln\frac{A}{B}$ so the "exact value" is one tidy logarithm.

### Example 11 - Medium - Definite $\frac{k f'}{f}$ (coursebook Worked Example 8.8)

> **Question:** Find the exact value of $\int_0^1 \frac{2e^x}{1+e^x}\,\mathrm{d}x$.

**Solution:**

Name the denominator and differentiate:

$$f(x) = 1 + e^x \quad\Rightarrow\quad f'(x) = e^x$$

The numerator is $2f'(x)$, so $k = 2$:

$$\int_0^1 \frac{2e^x}{1+e^x}\,\mathrm{d}x = \left[2\ln\left(1+e^x\right)\right]_0^1$$

Substitute the limits:

$$\int_0^1 \frac{2e^x}{1+e^x}\,\mathrm{d}x = 2\ln(1+e) - 2\ln(1+1)$$

$$\int_0^1 \frac{2e^x}{1+e^x}\,\mathrm{d}x = 2\ln(1+e) - 2\ln 2$$

Combine the logs:

$$\int_0^1 \frac{2e^x}{1+e^x}\,\mathrm{d}x = 2\ln\left(\frac{1+e}{2}\right) \quad\checkmark$$

**What the examiner wants:** the factor of 2 carried through, and the log laws used to reach a single tidy exact answer. Leaving $2\ln(1+e) - 2\ln 2$ uncombined often loses the final mark.

### Practice Questions - Part 2

1. (Easy) Find $\int \frac{6x}{x^2-1}\,\mathrm{d}x$.
2. (Medium) Find $\int \tan 2x\,\mathrm{d}x$.
3. (Medium) Find the exact value of $\int_0^{\ln 2} \frac{e^x}{1+e^x}\,\mathrm{d}x$.
4. (Medium) Find $\int \frac{e^x + 1}{e^x + x}\,\mathrm{d}x$.

**Solutions:**

Question 1:

$$f(x) = x^2 - 1 \quad\Rightarrow\quad f'(x) = 2x$$

The numerator is $3 \cdot 2x = 3f'(x)$, so $k = 3$:

$$\int \frac{6x}{x^2-1}\,\mathrm{d}x = 3\ln\big|x^2 - 1\big| + c \quad\checkmark$$

Question 2:

$$\int \tan 2x\,\mathrm{d}x = \int \frac{\sin 2x}{\cos 2x}\,\mathrm{d}x$$

$$f(x) = \cos 2x \quad\Rightarrow\quad f'(x) = -2\sin 2x$$

So $\sin 2x = -\frac{1}{2}f'(x)$, giving $k = -\frac{1}{2}$:

$$\int \tan 2x\,\mathrm{d}x = -\frac{1}{2}\ln\big|\cos 2x\big| + c \quad\checkmark$$

Question 3:

$$f(x) = 1 + e^x \quad\Rightarrow\quad f'(x) = e^x$$

The numerator is exactly $f'(x)$, so $k = 1$:

$$\int_0^{\ln 2} \frac{e^x}{1+e^x}\,\mathrm{d}x = \left[\ln\left(1+e^x\right)\right]_0^{\ln 2}$$

$$\int_0^{\ln 2} \frac{e^x}{1+e^x}\,\mathrm{d}x = \ln(1+2) - \ln(1+1)$$

$$\int_0^{\ln 2} \frac{e^x}{1+e^x}\,\mathrm{d}x = \ln 3 - \ln 2 = \ln\left(\frac{3}{2}\right) \quad\checkmark$$

Question 4:

$$f(x) = e^x + x \quad\Rightarrow\quad f'(x) = e^x + 1$$

The numerator is exactly $f'(x)$, so $k = 1$:

$$\int \frac{e^x + 1}{e^x + x}\,\mathrm{d}x = \ln\big|e^x + x\big| + c \quad\checkmark$$

---

# PART 3: Integration by Substitution

Integration by substitution is the reverse of the chain rule. If you set $u = g(x)$, then $\frac{\mathrm{d}u}{\mathrm{d}x} = g'(x)$, which you treat as $\mathrm{d}u = g'(x)\,\mathrm{d}x$. You must rewrite the ENTIRE integral in terms of $u$: the integrand, the $\mathrm{d}x$, and (for definite integrals) the limits.

> ⭐ **The golden rule:** after substituting, the original variable $x$ must not appear anywhere in the integral. If it does, you chose the substitution badly or forgot to replace something. The syllabus says "use a given substitution" - Cambridge always tells you which one; you must carry it through flawlessly.

## 3.1 Algebraic Substitutions - $u = ax + b$ or $u = f(x)$

When $u = 2x + 1$ and the integrand still contains $x$, you must solve for $x = \frac{u-1}{2}$ and replace it. Leaving $x$ in the $u$-integral is a guaranteed mark loss.

### Example 12 - Medium - Linear substitution with $x$ replaced (coursebook Worked Example 8.9)

> **Question:** Using the substitution $u = 2x + 1$, find $\int 4x\sqrt{2x+1}\,\mathrm{d}x$.

**Solution:**

Differentiate the substitution:

$$u = 2x + 1 \quad\Rightarrow\quad \frac{\mathrm{d}u}{\mathrm{d}x} = 2 \quad\Rightarrow\quad \mathrm{d}x = \frac{1}{2}\,\mathrm{d}u$$

Solve the substitution for $x$:

$$x = \frac{u-1}{2}$$

Rewrite the integral completely in $u$:

$$\int 4x\sqrt{2x+1}\,\mathrm{d}x = \int 4\left(\frac{u-1}{2}\right)u^{1/2}\left(\frac{1}{2}\right)\mathrm{d}u$$

Simplify the constant factors:

$$\int 4x\sqrt{2x+1}\,\mathrm{d}x = \int (u-1)u^{1/2}\,\mathrm{d}u$$

Expand:

$$\int 4x\sqrt{2x+1}\,\mathrm{d}x = \int \left(u^{3/2} - u^{1/2}\right)\mathrm{d}u$$

Integrate with respect to $u$:

$$\int 4x\sqrt{2x+1}\,\mathrm{d}x = \frac{2}{5}u^{5/2} - \frac{2}{3}u^{3/2} + c$$

Substitute back $u = 2x + 1$:

$$\int 4x\sqrt{2x+1}\,\mathrm{d}x = \frac{2}{5}(2x+1)^{5/2} - \frac{2}{3}(2x+1)^{3/2} + c \quad\checkmark$$

**What the examiner wants:** the complete rewrite (no $x$ left), correct fractional-power integration, and substitution back at the end.

## 3.2 Trigonometric Substitutions

Three families you will meet:

1. $x = a\sin\theta$ when the integrand contains $\sqrt{a^2 - x^2}$: since $\sqrt{a^2 - a^2\sin^2\theta} = a\cos\theta$, the square root disappears.
2. $x = a\tan\theta$ when the integrand contains $x^2 + a^2$ raised to a power: since $x^2 + a^2 = a^2\sec^2\theta$.
3. $u = \sin x$ (or similar) when $\cos x$ (or a trig derivative) sits outside.

> ⭐ **Watch Out!** The wrong simplification $\sqrt{1-\sin^2\theta} = 1 - \sin\theta$ is called out in the June 2023 Paper 33 report. It is $\sqrt{1-\sin^2\theta} = \cos\theta$, and $\cos\theta \geq 0$ on the relevant range.

### Example 13 - Medium - $x = a\tan u$ substitution (coursebook Worked Example 8.10)

> **Question:** Using the substitution $x = 2\tan u$, find $\int \frac{8}{x^2+4}\,\mathrm{d}x$.

**Solution:**

Differentiate the substitution:

$$x = 2\tan u \quad\Rightarrow\quad \frac{\mathrm{d}x}{\mathrm{d}u} = 2\sec^2 u \quad\Rightarrow\quad \mathrm{d}x = 2\sec^2 u\,\mathrm{d}u$$

Simplify $x^2 + 4$ using $\tan^2 u + 1 = \sec^2 u$:

$$x^2 + 4 = 4\tan^2 u + 4 = 4\left(\tan^2 u + 1\right) = 4\sec^2 u$$

Rewrite the integral completely in $u$:

$$\int \frac{8}{x^2+4}\,\mathrm{d}x = \int \frac{8}{4\sec^2 u} \cdot 2\sec^2 u\,\mathrm{d}u$$

Cancel the $\sec^2 u$ factors:

$$\int \frac{8}{x^2+4}\,\mathrm{d}x = \int 4\,\mathrm{d}u$$

Integrate with respect to $u$:

$$\int \frac{8}{x^2+4}\,\mathrm{d}x = 4u + c$$

Substitute back $u = \tan^{-1}\left(\frac{x}{2}\right)$:

$$\int \frac{8}{x^2+4}\,\mathrm{d}x = 4\tan^{-1}\left(\frac{x}{2}\right) + c \quad\checkmark$$

**What the examiner wants:** $\sec^2 = 1 + \tan^2$ used to kill the denominator, and the return to $x$ via $\tan^{-1}$ at the end.

### Example 14 - Medium - $u = \sin x$ substitution (coursebook Worked Example 8.11)

> **Question:** Using the substitution $u = \sin x$, find $\int 4\sin^2 x \cos^3 x\,\mathrm{d}x$.

**Solution:**

Differentiate the substitution:

$$u = \sin x \quad\Rightarrow\quad \frac{\mathrm{d}u}{\mathrm{d}x} = \cos x \quad\Rightarrow\quad \mathrm{d}u = \cos x\,\mathrm{d}x$$

Split $\cos^3 x$ into $\cos^2 x \cdot \cos x$ and use $\cos^2 x = 1 - \sin^2 x$:

$$\int 4\sin^2 x \cos^3 x\,\mathrm{d}x = \int 4\sin^2 x \cos^2 x \cdot \cos x\,\mathrm{d}x$$

$$\int 4\sin^2 x \cos^3 x\,\mathrm{d}x = \int 4u^2\left(1-u^2\right)\mathrm{d}u$$

Expand:

$$\int 4\sin^2 x \cos^3 x\,\mathrm{d}x = \int \left(4u^2 - 4u^4\right)\mathrm{d}u$$

Integrate with respect to $u$:

$$\int 4\sin^2 x \cos^3 x\,\mathrm{d}x = \frac{4}{3}u^3 - \frac{4}{5}u^5 + c$$

Substitute back $u = \sin x$:

$$\int 4\sin^2 x \cos^3 x\,\mathrm{d}x = \frac{4}{3}\sin^3 x - \frac{4}{5}\sin^5 x + c \quad\checkmark$$

**What the examiner wants:** the $\sin^2 x + \cos^2 x = 1$ rewrite before substituting, and clean fractional-power integration. (The syllabus lists $\int \sin^2 2x \cos x\,\mathrm{d}x$ with $u = \sin x$ as its example of this family.)

### Example 15 - Hard - $x = a\sin\theta$ substitution, show-then-evaluate (N10 P31 Q5, 3 + 4 marks)

> **Question:** Let $I = \int_0^1 \frac{x^2}{\sqrt{4-x^2}}\,\mathrm{d}x$. (i) Using the substitution $x = 2\sin\theta$, show that $I = \int_0^{\pi/6} 4\sin^2\theta\,\mathrm{d}\theta$. (ii) Hence find the exact value of $I$.

**Solution:**

Part (i) - differentiate the substitution:

$$x = 2\sin\theta \quad\Rightarrow\quad \frac{\mathrm{d}x}{\mathrm{d}\theta} = 2\cos\theta \quad\Rightarrow\quad \mathrm{d}x = 2\cos\theta\,\mathrm{d}\theta$$

Convert the limits:

$$x = 0 \quad\Rightarrow\quad 2\sin\theta = 0 \quad\Rightarrow\quad \theta = 0$$

$$x = 1 \quad\Rightarrow\quad 2\sin\theta = 1 \quad\Rightarrow\quad \sin\theta = \frac{1}{2} \quad\Rightarrow\quad \theta = \frac{\pi}{6}$$

Replace every piece:

$$x^2 = 4\sin^2\theta$$

$$\sqrt{4 - x^2} = \sqrt{4 - 4\sin^2\theta} = \sqrt{4\cos^2\theta} = 2\cos\theta$$

Rewrite the integral:

$$I = \int_0^{\pi/6} \frac{4\sin^2\theta}{2\cos\theta} \cdot 2\cos\theta\,\mathrm{d}\theta$$

Cancel the $\cos\theta$ factors:

$$I = \int_0^{\pi/6} 4\sin^2\theta\,\mathrm{d}\theta \quad\checkmark$$

Part (ii) - use $\sin^2\theta = \frac{1-\cos 2\theta}{2}$:

$$I = \int_0^{\pi/6} 4\sin^2\theta\,\mathrm{d}\theta = \int_0^{\pi/6} 2\left(1 - \cos 2\theta\right)\mathrm{d}\theta$$

$$I = \left[2\theta - \sin 2\theta\right]_0^{\pi/6}$$

$$I = 2\left(\frac{\pi}{6}\right) - \sin\left(\frac{\pi}{3}\right) - 0$$

$$I = \frac{\pi}{3} - \frac{\sqrt{3}}{2} \quad\checkmark$$

**What the examiner wants:** the three separate steps written out (limits conversion, $\mathrm{d}x$ replacement, integrand rewrite) - examiner reports say candidates must show them line by line - then the double-angle integration with an exact final answer.

## 3.3 Definite Integrals - Convert the Limits

When you substitute into $\int_a^b$, convert the limits: compute $u = g(a)$ and $u = g(b)$, rewrite the integral entirely in $u$, integrate, and substitute the $u$-limits. NEVER return to $x$. Cambridge expects this method.

> ⭐ **Watch Out!** The June 2023 examiner reports complain about candidates who did not convert limits at all, or converted them but used them in the wrong order.

### Example 16 - Medium - Definite substitution with converted limits (coursebook Worked Example 8.12)

> **Question:** Using the substitution $u = x + 1$, find the exact value of $\int_0^3 \frac{x}{\sqrt{x+1}}\,\mathrm{d}x$.

**Solution:**

Differentiate the substitution and solve for $x$:

$$u = x + 1 \quad\Rightarrow\quad \frac{\mathrm{d}u}{\mathrm{d}x} = 1 \quad\Rightarrow\quad \mathrm{d}x = \mathrm{d}u$$

$$x = u - 1$$

Convert the limits:

$$x = 0 \quad\Rightarrow\quad u = 1$$

$$x = 3 \quad\Rightarrow\quad u = 4$$

Rewrite the integral completely in $u$:

$$\int_0^3 \frac{x}{\sqrt{x+1}}\,\mathrm{d}x = \int_1^4 \frac{u-1}{u^{1/2}}\,\mathrm{d}u$$

Split the fraction:

$$\int_0^3 \frac{x}{\sqrt{x+1}}\,\mathrm{d}x = \int_1^4 \left(u^{1/2} - u^{-1/2}\right)\mathrm{d}u$$

Integrate with respect to $u$:

$$\int_0^3 \frac{x}{\sqrt{x+1}}\,\mathrm{d}x = \left[\frac{2}{3}u^{3/2} - 2u^{1/2}\right]_1^4$$

Substitute the $u$-limits:

$$\int_0^3 \frac{x}{\sqrt{x+1}}\,\mathrm{d}x = \left(\frac{2}{3} \cdot 8 - 4\right) - \left(\frac{2}{3} - 2\right)$$

$$\int_0^3 \frac{x}{\sqrt{x+1}}\,\mathrm{d}x = \frac{4}{3} - \left(-\frac{4}{3}\right) = \frac{8}{3} \quad\checkmark$$

**What the examiner wants:** limits converted to 1 and 4 and never returning to $x$; exact fraction at the end.

### Example 17 - Medium - Substitution with $\sec^2$ derivative (J14 P31 Q2, 5 marks, computed estimate)

> **Question:** Use the substitution $u = 1 + 3\tan x$ to find the exact value of $\int_0^{\pi/4} \frac{1+3\tan x}{\cos^2 x}\,\mathrm{d}x$.

**Solution:**

Differentiate the substitution:

$$u = 1 + 3\tan x \quad\Rightarrow\quad \frac{\mathrm{d}u}{\mathrm{d}x} = 3\sec^2 x \quad\Rightarrow\quad \sec^2 x\,\mathrm{d}x = \frac{1}{3}\,\mathrm{d}u$$

Convert the limits:

$$x = 0 \quad\Rightarrow\quad u = 1 + 0 = 1$$

$$x = \frac{\pi}{4} \quad\Rightarrow\quad u = 1 + 3\tan\left(\frac{\pi}{4}\right) = 1 + 3 = 4$$

Rewrite the integral, using $\frac{1}{\cos^2 x} = \sec^2 x$:

$$\int_0^{\pi/4} \frac{1+3\tan x}{\cos^2 x}\,\mathrm{d}x = \int_1^4 u \cdot \frac{1}{3}\,\mathrm{d}u$$

$$\int_0^{\pi/4} \frac{1+3\tan x}{\cos^2 x}\,\mathrm{d}x = \frac{1}{3}\int_1^4 u\,\mathrm{d}u$$

Integrate with respect to $u$:

$$\int_0^{\pi/4} \frac{1+3\tan x}{\cos^2 x}\,\mathrm{d}x = \frac{1}{3}\left[\frac{u^2}{2}\right]_1^4$$

$$\int_0^{\pi/4} \frac{1+3\tan x}{\cos^2 x}\,\mathrm{d}x = \frac{1}{3}\left(\frac{16}{2} - \frac{1}{2}\right) = \frac{1}{3} \cdot \frac{15}{2}$$

$$\int_0^{\pi/4} \frac{1+3\tan x}{\cos^2 x}\,\mathrm{d}x = \frac{5}{2} \quad\checkmark$$

**What the examiner wants:** noticing that $\sec^2 x$ is (a multiple of) $\frac{\mathrm{d}u}{\mathrm{d}x}$, converting limits to 1 and 4, and a clean exact fraction.

## 3.4 The Minus-Sign Trap - Substitutions with Negative Derivatives

If the substitution is $u = \cos x$ (so $\frac{\mathrm{d}u}{\mathrm{d}x} = -\sin x$), the $\mathrm{d}x$ replacement introduces a minus sign and the new limits come out in the "wrong" order. Either keep the minus sign with the limits as found, or swap the limits and drop the sign. Do one or the other - never both, never neither.

> ⭐ **Watch Out!** The June 2023 Paper 33 examiner report: "many [candidates] missing dx or du or a minus sign that disappeared without the order of the limits being changed." The June 2023 Paper 33 Q7 report also flags candidates integrating $e^{2u}$ to $2e^{2u}$ instead of $\frac{1}{2}e^{2u}$.

### Example 18 - Medium - $u = \cos x$ with the minus sign handled (June 2023 Paper 33 Q7 pattern, computed estimate)

> **Question:** Using the substitution $u = \cos x$, find the exact value of $\int_0^{\pi/3} \sin x \cos^2 x\,\mathrm{d}x$.

**Solution:**

Differentiate the substitution:

$$u = \cos x \quad\Rightarrow\quad \frac{\mathrm{d}u}{\mathrm{d}x} = -\sin x \quad\Rightarrow\quad \sin x\,\mathrm{d}x = -\mathrm{d}u$$

Convert the limits:

$$x = 0 \quad\Rightarrow\quad u = \cos 0 = 1$$

$$x = \frac{\pi}{3} \quad\Rightarrow\quad u = \cos\left(\frac{\pi}{3}\right) = \frac{1}{2}$$

Method A - keep the minus sign and the limits as found:

$$\int_0^{\pi/3} \sin x \cos^2 x\,\mathrm{d}x = \int_1^{1/2} u^2 (-\mathrm{d}u) = -\int_1^{1/2} u^2\,\mathrm{d}u$$

$$= -\left[\frac{u^3}{3}\right]_1^{1/2} = -\left(\frac{1}{24} - \frac{1}{3}\right) = -\left(\frac{1}{24} - \frac{8}{24}\right)$$

$$= -\left(-\frac{7}{24}\right) = \frac{7}{24} \quad\checkmark$$

Method B - swap the limits and drop the minus sign:

$$\int_0^{\pi/3} \sin x \cos^2 x\,\mathrm{d}x = \int_{1/2}^{1} u^2\,\mathrm{d}u = \left[\frac{u^3}{3}\right]_{1/2}^{1}$$

$$= \frac{1}{3} - \frac{1}{24} = \frac{7}{24} \quad\checkmark$$

Both methods give the same answer - pick one and stick to it.

**What the examiner wants:** the minus sign never silently vanishing. Doing both (keeping the sign AND swapping) gives $-\frac{7}{24}$ - wrong.

### Practice Questions - Part 3

1. (Easy) Using $u = x^2$, find the exact value of $\int_0^1 x\,e^{x^2}\,\mathrm{d}x$.
2. (Medium) Using $u = x + 2$, find the exact value of $\int_0^1 \frac{x}{(x+2)^2}\,\mathrm{d}x$.
3. (Medium) Using $u = x - 1$, find the exact value of $\int_1^4 x\sqrt{x-1}\,\mathrm{d}x$.
4. (Medium) Using $x = \sin\theta$, find the exact value of $\int_0^1 \frac{x}{\sqrt{1-x^2}}\,\mathrm{d}x$.
5. (Hard) Using $u = \cos x$, find the exact value of $\int_0^{\pi/2} \sin^3 x \cos^2 x\,\mathrm{d}x$.

**Solutions:**

Question 1:

$$u = x^2 \quad\Rightarrow\quad \frac{\mathrm{d}u}{\mathrm{d}x} = 2x \quad\Rightarrow\quad x\,\mathrm{d}x = \frac{1}{2}\,\mathrm{d}u$$

Convert the limits:

$$x = 0 \quad\Rightarrow\quad u = 0; \qquad x = 1 \quad\Rightarrow\quad u = 1$$

$$\int_0^1 x\,e^{x^2}\,\mathrm{d}x = \frac{1}{2}\int_0^1 e^u\,\mathrm{d}u = \frac{1}{2}\left[e^u\right]_0^1$$

$$\int_0^1 x\,e^{x^2}\,\mathrm{d}x = \frac{1}{2}(e - 1) \quad\checkmark$$

Question 2:

$$u = x + 2 \quad\Rightarrow\quad \mathrm{d}x = \mathrm{d}u, \qquad x = u - 2$$

Convert the limits:

$$x = 0 \quad\Rightarrow\quad u = 2; \qquad x = 1 \quad\Rightarrow\quad u = 3$$

$$\int_0^1 \frac{x}{(x+2)^2}\,\mathrm{d}x = \int_2^3 \frac{u-2}{u^2}\,\mathrm{d}u$$

Split the fraction:

$$\int_0^1 \frac{x}{(x+2)^2}\,\mathrm{d}x = \int_2^3 \left(\frac{1}{u} - \frac{2}{u^2}\right)\mathrm{d}u$$

Integrate with respect to $u$:

$$\int_0^1 \frac{x}{(x+2)^2}\,\mathrm{d}x = \left[\ln u + \frac{2}{u}\right]_2^3$$

$$\int_0^1 \frac{x}{(x+2)^2}\,\mathrm{d}x = \left(\ln 3 + \frac{2}{3}\right) - \left(\ln 2 + 1\right)$$

$$\int_0^1 \frac{x}{(x+2)^2}\,\mathrm{d}x = \ln\left(\frac{3}{2}\right) - \frac{1}{3} \quad\checkmark$$

Question 3:

$$u = x - 1 \quad\Rightarrow\quad \mathrm{d}x = \mathrm{d}u, \qquad x = u + 1$$

Convert the limits:

$$x = 1 \quad\Rightarrow\quad u = 0; \qquad x = 4 \quad\Rightarrow\quad u = 3$$

$$\int_1^4 x\sqrt{x-1}\,\mathrm{d}x = \int_0^3 (u+1)u^{1/2}\,\mathrm{d}u$$

Expand:

$$\int_1^4 x\sqrt{x-1}\,\mathrm{d}x = \int_0^3 \left(u^{3/2} + u^{1/2}\right)\mathrm{d}u$$

Integrate with respect to $u$:

$$\int_1^4 x\sqrt{x-1}\,\mathrm{d}x = \left[\frac{2}{5}u^{5/2} + \frac{2}{3}u^{3/2}\right]_0^3$$

$$\int_1^4 x\sqrt{x-1}\,\mathrm{d}x = \frac{2}{5}(3\sqrt{3})^2\sqrt{3} + \frac{2}{3}(3\sqrt{3})$$

$$\int_1^4 x\sqrt{x-1}\,\mathrm{d}x = \frac{2}{5} \cdot 9\sqrt{3} + \frac{2}{3} \cdot 3\sqrt{3}$$

$$\int_1^4 x\sqrt{x-1}\,\mathrm{d}x = \frac{18\sqrt{3}}{5} + 2\sqrt{3} = \frac{28\sqrt{3}}{5} \quad\checkmark$$

Question 4:

$$x = \sin\theta \quad\Rightarrow\quad \mathrm{d}x = \cos\theta\,\mathrm{d}\theta$$

Convert the limits:

$$x = 0 \quad\Rightarrow\quad \theta = 0; \qquad x = 1 \quad\Rightarrow\quad \theta = \frac{\pi}{2}$$

$$\sqrt{1 - x^2} = \sqrt{1 - \sin^2\theta} = \cos\theta$$

$$\int_0^1 \frac{x}{\sqrt{1-x^2}}\,\mathrm{d}x = \int_0^{\pi/2} \frac{\sin\theta}{\cos\theta} \cdot \cos\theta\,\mathrm{d}\theta$$

Cancel the $\cos\theta$ factors:

$$\int_0^1 \frac{x}{\sqrt{1-x^2}}\,\mathrm{d}x = \int_0^{\pi/2} \sin\theta\,\mathrm{d}\theta$$

$$\int_0^1 \frac{x}{\sqrt{1-x^2}}\,\mathrm{d}x = \left[-\cos\theta\right]_0^{\pi/2} = -\cos\left(\frac{\pi}{2}\right) + \cos 0 = 1 \quad\checkmark$$

Question 5:

$$u = \cos x \quad\Rightarrow\quad \frac{\mathrm{d}u}{\mathrm{d}x} = -\sin x \quad\Rightarrow\quad \sin x\,\mathrm{d}x = -\mathrm{d}u$$

Convert the limits:

$$x = 0 \quad\Rightarrow\quad u = 1; \qquad x = \frac{\pi}{2} \quad\Rightarrow\quad u = 0$$

Rewrite $\sin^3 x = \sin^2 x \cdot \sin x = (1 - \cos^2 x)\sin x$:

$$\int_0^{\pi/2} \sin^3 x \cos^2 x\,\mathrm{d}x = \int_1^0 (1-u^2)u^2(-\mathrm{d}u)$$

Swap the limits and drop the minus sign:

$$\int_0^{\pi/2} \sin^3 x \cos^2 x\,\mathrm{d}x = \int_0^1 (u^2 - u^4)\,\mathrm{d}u$$

$$\int_0^{\pi/2} \sin^3 x \cos^2 x\,\mathrm{d}x = \left[\frac{u^3}{3} - \frac{u^5}{5}\right]_0^1 = \frac{1}{3} - \frac{1}{5} = \frac{2}{15} \quad\checkmark$$

---

# PART 4: Partial Fractions in Integration

Some rational functions cannot be integrated directly, but split into simpler pieces whose integrals you know. This uses the partial fractions machinery from Chapter 7, then each piece is integrated with a Chapter 5 / this-chapter result.

## 4.1 The Decomposition Templates and How Each Piece Integrates

| Denominator contains | Decomposition form | Integral of each piece |
|---|---|---|
| Distinct linear factors $(ax+b)(cx+d)$ | $\frac{A}{ax+b} + \frac{B}{cx+d}$ | $\frac{A}{a}\ln|ax+b|$ |
| Repeated linear factor $(ax+b)^2$ | $\frac{A}{ax+b} + \frac{B}{(ax+b)^2}$ | $\frac{A}{a}\ln|ax+b| - \frac{B}{a(ax+b)}$ |
| Irreducible quadratic $ax^2+bx+c$ | $\frac{Ax+B}{ax^2+bx+c}$ | log part from $Ax$ term, arctan part from constant term |

> ⭐ **Watch Out!** $\int \frac{B}{(ax+b)^2}\,\mathrm{d}x = -\frac{B}{a(ax+b)} + c$ is a NEGATIVE POWER, not a third logarithm. The June 2023 Paper 31 report: "many candidates giving a third log term" where the correct answer was $-\frac{1}{x+2}$. Also: an improper fraction (numerator degree $\geq$ denominator degree) must be divided first (November 2023 Paper 32 Q5 report).

### Example 19 - Easy - Distinct linear factors (coursebook Explore 8.1)

> **Question:** Find $\int \frac{2}{x^2-1}\,\mathrm{d}x$.

**Solution:**

Factorise the denominator:

$$x^2 - 1 = (x-1)(x+1)$$

Set up the decomposition:

$$\frac{2}{x^2-1} = \frac{A}{x-1} + \frac{B}{x+1}$$

Multiply through by $(x-1)(x+1)$:

$$2 = A(x+1) + B(x-1)$$

Substitute $x = 1$:

$$2 = A(2) \quad\Rightarrow\quad A = 1$$

Substitute $x = -1$:

$$2 = B(-2) \quad\Rightarrow\quad B = -1$$

So:

$$\frac{2}{x^2-1} = \frac{1}{x-1} - \frac{1}{x+1}$$

Integrate each piece:

$$\int \frac{2}{x^2-1}\,\mathrm{d}x = \int \frac{1}{x-1}\,\mathrm{d}x - \int \frac{1}{x+1}\,\mathrm{d}x$$

$$\int \frac{2}{x^2-1}\,\mathrm{d}x = \ln|x-1| - \ln|x+1| + c$$

Combine the logs:

$$\int \frac{2}{x^2-1}\,\mathrm{d}x = \ln\left|\frac{x-1}{x+1}\right| + c \quad\checkmark$$

**What the examiner wants:** the decomposition done BEFORE integrating, then two clean log integrals combined with the quotient rule for logs.

### Example 20 - Easy - Partial fractions in a differential equation (Nov 2023 Paper 32 Q11 pattern, computed estimate)

> **Question:** Find $\int \frac{1}{y^2 + y}\,\mathrm{d}y$.

**Solution:**

Factorise the denominator:

$$y^2 + y = y(y+1)$$

Set up the decomposition:

$$\frac{1}{y(y+1)} = \frac{A}{y} + \frac{B}{y+1}$$

Multiply through by $y(y+1)$:

$$1 = A(y+1) + By$$

Substitute $y = 0$:

$$1 = A$$

Substitute $y = -1$:

$$1 = -B \quad\Rightarrow\quad B = -1$$

So:

$$\frac{1}{y(y+1)} = \frac{1}{y} - \frac{1}{y+1}$$

Integrate each piece:

$$\int \frac{1}{y^2 + y}\,\mathrm{d}y = \int \frac{1}{y}\,\mathrm{d}y - \int \frac{1}{y+1}\,\mathrm{d}y$$

$$\int \frac{1}{y^2 + y}\,\mathrm{d}y = \ln|y| - \ln|y+1| + c = \ln\left|\frac{y}{y+1}\right| + c \quad\checkmark$$

**What the examiner wants:** the correct split. The November 2023 Paper 32 Q11 report flags candidates writing $\frac{1}{y^2+y} = \frac{1}{y^2} + \frac{1}{y}$ - always partial fractions, never term-by-term splitting of a sum in the denominator.

## 4.2 Repeated Linear Factors

### Example 21 - Hard - Repeated factor decomposition (coursebook Worked Example 8.14, computed estimate)

> **Question:** Find $\int \frac{9}{(2x+1)(x-1)^2}\,\mathrm{d}x$.

**Solution:**

Set up the decomposition (one fraction for each power):

$$\frac{9}{(2x+1)(x-1)^2} = \frac{A}{2x+1} + \frac{B}{x-1} + \frac{C}{(x-1)^2}$$

Multiply through by $(2x+1)(x-1)^2$:

$$9 = A(x-1)^2 + B(2x+1)(x-1) + C(2x+1)$$

Substitute $x = 1$ (kills the $A$ and $B$ terms):

$$9 = C(3) \quad\Rightarrow\quad C = 3$$

Substitute $x = -\frac{1}{2}$ (kills the $B$ and $C$ terms):

$$9 = A\left(-\frac{3}{2}\right)^2 = \frac{9}{4}A \quad\Rightarrow\quad A = 4$$

Substitute $x = 0$:

$$9 = A(1) + B(1)(-1) + C(1) = 4 - B + 3$$

$$9 = 7 - B \quad\Rightarrow\quad B = -2$$

So:

$$\frac{9}{(2x+1)(x-1)^2} = \frac{4}{2x+1} - \frac{2}{x-1} + \frac{3}{(x-1)^2}$$

Integrate each piece:

$$\int \frac{9}{(2x+1)(x-1)^2}\,\mathrm{d}x = \int \frac{4}{2x+1}\,\mathrm{d}x - \int \frac{2}{x-1}\,\mathrm{d}x + \int \frac{3}{(x-1)^2}\,\mathrm{d}x$$

First piece - linear denominator:

$$\int \frac{4}{2x+1}\,\mathrm{d}x = 2\ln|2x+1|$$

Second piece:

$$\int \frac{2}{x-1}\,\mathrm{d}x = 2\ln|x-1|$$

Third piece - NEGATIVE POWER, not a log:

$$\int \frac{3}{(x-1)^2}\,\mathrm{d}x = \int 3(x-1)^{-2}\,\mathrm{d}x = -\frac{3}{x-1}$$

Assemble:

$$\int \frac{9}{(2x+1)(x-1)^2}\,\mathrm{d}x = 2\ln|2x+1| - 2\ln|x-1| - \frac{3}{x-1} + c \quad\checkmark$$

**What the examiner wants:** the full template including the repeated-factor term, and $\frac{3}{(x-1)^2}$ integrated as a negative power (see the June 2023 Paper 31 complaint about "a third log term").

## 4.3 Quadratic Factors - The $Bx + C$ Template

For an irreducible quadratic factor, use $\frac{Bx + C}{ax^2 + bx + c}$ on top. After decomposition, the quadratic piece usually splits into a $\frac{k f'}{f}$ log part plus an arctan part.

### Example 22 - Medium - Quadratic factor, log + arctan finish (coursebook Worked Example 8.13)

> **Question:** Find $\int \frac{3-x}{(x+1)(x^2+3)}\,\mathrm{d}x$.

**Solution:**

Set up the decomposition:

$$\frac{3-x}{(x+1)(x^2+3)} = \frac{A}{x+1} + \frac{Bx + C}{x^2 + 3}$$

Multiply through by $(x+1)(x^2+3)$:

$$3 - x = A(x^2+3) + (Bx + C)(x+1)$$

Substitute $x = -1$ (kills the $Bx + C$ term):

$$4 = A(4) \quad\Rightarrow\quad A = 1$$

Substitute $x = 0$:

$$3 = 3A + C = 3 + C \quad\Rightarrow\quad C = 0$$

Substitute $x = 1$:

$$2 = 4A + (B + C)(2) = 4 + 2B$$

$$2B = -2 \quad\Rightarrow\quad B = -1$$

So:

$$\frac{3-x}{(x+1)(x^2+3)} = \frac{1}{x+1} - \frac{x}{x^2+3}$$

Integrate piece by piece:

$$\int \frac{3-x}{(x+1)(x^2+3)}\,\mathrm{d}x = \int \frac{1}{x+1}\,\mathrm{d}x - \int \frac{x}{x^2+3}\,\mathrm{d}x$$

First piece - a log:

$$\int \frac{1}{x+1}\,\mathrm{d}x = \ln|x+1|$$

Second piece - $\frac{k f'}{f}$ with $f(x) = x^2+3$:

$$\int \frac{x}{x^2+3}\,\mathrm{d}x = \frac{1}{2}\int \frac{2x}{x^2+3}\,\mathrm{d}x = \frac{1}{2}\ln(x^2+3)$$

Assemble:

$$\int \frac{3-x}{(x+1)(x^2+3)}\,\mathrm{d}x = \ln|x+1| - \frac{1}{2}\ln(x^2+3) + c \quad\checkmark$$

**What the examiner wants:** the $Bx + C$ template over the quadratic factor, and recognising $\frac{x}{x^2+3}$ as a $\frac{k f'}{f}$ log.

### Example 23 - Hard - Partial fractions with a quadratic factor, show that (N11 P31 Q8, 4 + 5 marks)

> **Question:** Let $f(x) = \frac{12 + 8x - x^2}{(2-x)(4+x^2)}$. (i) Express $f(x)$ in the form $\frac{A}{2-x} + \frac{Bx+C}{4+x^2}$. (ii) Show that $\int_0^1 f(x)\,\mathrm{d}x = \ln\left(\frac{25}{2}\right)$.

**Solution:**

Part (i) - set up the decomposition:

$$\frac{12 + 8x - x^2}{(2-x)(4+x^2)} = \frac{A}{2-x} + \frac{Bx + C}{4+x^2}$$

Multiply through by $(2-x)(4+x^2)$:

$$12 + 8x - x^2 = A(4+x^2) + (Bx + C)(2-x)$$

Expand the right-hand side:

$$A(4+x^2) = 4A + Ax^2$$

$$(Bx + C)(2-x) = 2Bx - Bx^2 + 2C - Cx = -Bx^2 + (2B - C)x + 2C$$

Compare coefficients:

$$x^2: \quad A - B = -1$$

$$x: \quad 2B - C = 8$$

$$\text{constant:} \quad 4A + 2C = 12$$

From the first equation, $B = A + 1$. Substitute into the second:

$$2(A+1) - C = 8 \quad\Rightarrow\quad 2A - C = 6 \quad\Rightarrow\quad C = 2A - 6$$

Substitute into the constant equation:

$$4A + 2(2A - 6) = 12 \quad\Rightarrow\quad 8A - 12 = 12 \quad\Rightarrow\quad A = 3$$

Then:

$$B = A + 1 = 4, \qquad C = 2(3) - 6 = 0$$

So:

$$f(x) = \frac{3}{2-x} + \frac{4x}{4+x^2} \quad\checkmark$$

Part (ii) - integrate piece by piece:

$$\int_0^1 f(x)\,\mathrm{d}x = \int_0^1 \frac{3}{2-x}\,\mathrm{d}x + \int_0^1 \frac{4x}{4+x^2}\,\mathrm{d}x$$

First piece (the $-1$ from the chain rule on $2-x$):

$$\int \frac{3}{2-x}\,\mathrm{d}x = -3\ln|2-x|$$

Second piece - $\frac{k f'}{f}$ with $f(x) = 4+x^2$:

$$\int \frac{4x}{4+x^2}\,\mathrm{d}x = 2\ln(4+x^2)$$

So:

$$\int_0^1 f(x)\,\mathrm{d}x = \left[-3\ln(2-x) + 2\ln(4+x^2)\right]_0^1$$

Substitute the limits:

$$\int_0^1 f(x)\,\mathrm{d}x = \left(-3\ln 1 + 2\ln 5\right) - \left(-3\ln 2 + 2\ln 4\right)$$

Simplify, using $\ln 1 = 0$:

$$\int_0^1 f(x)\,\mathrm{d}x = 2\ln 5 + 3\ln 2 - 2\ln 4$$

Since $2\ln 4 = 4\ln 2$:

$$\int_0^1 f(x)\,\mathrm{d}x = 2\ln 5 + 3\ln 2 - 4\ln 2 = 2\ln 5 - \ln 2$$

$$\int_0^1 f(x)\,\mathrm{d}x = \ln 25 - \ln 2 = \ln\left(\frac{25}{2}\right) \quad\checkmark$$

**What the examiner wants:** constants found cleanly (substituting values or comparing coefficients both fine), then tidy log handling to hit the given answer exactly.

## 4.4 Improper Fractions - Divide First

If the degree of the numerator is greater than or equal to the degree of the denominator, divide first so you get a polynomial part plus a proper fraction. The November 2023 Paper 32 examiner report: many candidates "did not realise that the improper algebraic fraction needed to be dealt with before integration."

### Example 24 - Medium - Simplify before integrating (W23 P32 Q5, computed estimate)

> **Question:** Find $\int \frac{x^2 + 2x}{x^2 + 4}\,\mathrm{d}x$. (A question of this type appeared in November 2023 Paper 32; the examiner report describes candidates failing to deal with the improper fraction first.)

**Solution:**

The degrees are equal, so divide. Write $x^2 + 2x = (x^2 + 4) + (2x - 4)$:

$$\frac{x^2 + 2x}{x^2 + 4} = 1 + \frac{2x - 4}{x^2 + 4}$$

Split the remainder:

$$\frac{x^2 + 2x}{x^2 + 4} = 1 + \frac{2x}{x^2 + 4} - \frac{4}{x^2 + 4}$$

Integrate term by term:

$$\int \frac{x^2 + 2x}{x^2 + 4}\,\mathrm{d}x = \int 1\,\mathrm{d}x + \int \frac{2x}{x^2+4}\,\mathrm{d}x - \int \frac{4}{x^2+4}\,\mathrm{d}x$$

First term:

$$\int 1\,\mathrm{d}x = x$$

Second term - $\frac{k f'}{f}$ with $f(x) = x^2 + 4$:

$$\int \frac{2x}{x^2+4}\,\mathrm{d}x = \ln(x^2+4)$$

Third term - arctan form with $a = 2$:

$$\int \frac{4}{x^2+4}\,\mathrm{d}x = 4 \cdot \frac{1}{2}\tan^{-1}\left(\frac{x}{2}\right) = 2\tan^{-1}\left(\frac{x}{2}\right)$$

Assemble:

$$\int \frac{x^2 + 2x}{x^2 + 4}\,\mathrm{d}x = x + \ln(x^2+4) - 2\tan^{-1}\left(\frac{x}{2}\right) + c \quad\checkmark$$

**What the examiner wants:** seeing that the fraction must be split before integrating. The November 2023 report notes candidates wrongly claimed $\int \frac{x-4}{x^2+4}\,\mathrm{d}x = \frac{1}{2}\ln(x^2+4)$ and others assumed $x^2 + 4 = (x-2)(x+2)$ - both fatal.

### Practice Questions - Part 4

1. (Easy) Find the exact value of $\int_0^1 \frac{1}{(x+1)(x+2)}\,\mathrm{d}x$.
2. (Medium) Find the exact value of $\int_0^1 \frac{3x+1}{(x+1)(x+2)}\,\mathrm{d}x$.
3. (Hard) Find the exact value of $\int_2^3 \frac{1}{x(x-1)^2}\,\mathrm{d}x$.
4. (Medium) Find $\int \frac{2x+1}{x^2+1}\,\mathrm{d}x$.
5. (Medium) By first dividing, find $\int \frac{x^2 + x + 1}{x^2 + 1}\,\mathrm{d}x$.

**Solutions:**

Question 1:

$$\frac{1}{(x+1)(x+2)} = \frac{A}{x+1} + \frac{B}{x+2}$$

$$1 = A(x+2) + B(x+1)$$

Substitute $x = -1$:

$$1 = A \quad\Rightarrow\quad A = 1$$

Substitute $x = -2$:

$$1 = -B \quad\Rightarrow\quad B = -1$$

So:

$$\frac{1}{(x+1)(x+2)} = \frac{1}{x+1} - \frac{1}{x+2}$$

$$\int_0^1 \frac{1}{(x+1)(x+2)}\,\mathrm{d}x = \left[\ln(x+1) - \ln(x+2)\right]_0^1$$

$$\int_0^1 \frac{1}{(x+1)(x+2)}\,\mathrm{d}x = (\ln 2 - \ln 3) - (\ln 1 - \ln 2)$$

$$\int_0^1 \frac{1}{(x+1)(x+2)}\,\mathrm{d}x = 2\ln 2 - \ln 3 = \ln\left(\frac{4}{3}\right) \quad\checkmark$$

Question 2:

$$\frac{3x+1}{(x+1)(x+2)} = \frac{A}{x+1} + \frac{B}{x+2}$$

$$3x + 1 = A(x+2) + B(x+1)$$

Substitute $x = -1$:

$$-2 = A(1) \quad\Rightarrow\quad A = -2$$

Substitute $x = -2$:

$$-5 = B(-1) \quad\Rightarrow\quad B = 5$$

So:

$$\frac{3x+1}{(x+1)(x+2)} = -\frac{2}{x+1} + \frac{5}{x+2}$$

$$\int_0^1 \frac{3x+1}{(x+1)(x+2)}\,\mathrm{d}x = \left[-2\ln(x+1) + 5\ln(x+2)\right]_0^1$$

$$\int_0^1 \frac{3x+1}{(x+1)(x+2)}\,\mathrm{d}x = (-2\ln 2 + 5\ln 3) - (0 + 5\ln 2)$$

$$\int_0^1 \frac{3x+1}{(x+1)(x+2)}\,\mathrm{d}x = 5\ln 3 - 7\ln 2 = \ln\left(\frac{243}{128}\right) \quad\checkmark$$

Question 3:

$$\frac{1}{x(x-1)^2} = \frac{A}{x} + \frac{B}{x-1} + \frac{C}{(x-1)^2}$$

$$1 = A(x-1)^2 + Bx(x-1) + Cx$$

Substitute $x = 0$:

$$1 = A$$

Substitute $x = 1$:

$$1 = C$$

Substitute $x = 2$:

$$1 = A(1) + B(2)(1) + C(2) = 1 + 2B + 2$$

$$2B = -2 \quad\Rightarrow\quad B = -1$$

So:

$$\frac{1}{x(x-1)^2} = \frac{1}{x} - \frac{1}{x-1} + \frac{1}{(x-1)^2}$$

$$\int_2^3 \frac{1}{x(x-1)^2}\,\mathrm{d}x = \left[\ln x - \ln(x-1) - \frac{1}{x-1}\right]_2^3$$

$$\int_2^3 \frac{1}{x(x-1)^2}\,\mathrm{d}x = \left(\ln 3 - \ln 2 - \frac{1}{2}\right) - \left(\ln 2 - \ln 1 - 1\right)$$

$$\int_2^3 \frac{1}{x(x-1)^2}\,\mathrm{d}x = \ln 3 - 2\ln 2 + \frac{1}{2} = \ln\left(\frac{3}{4}\right) + \frac{1}{2} \quad\checkmark$$

Question 4 - split the numerator:

$$\frac{2x+1}{x^2+1} = \frac{2x}{x^2+1} + \frac{1}{x^2+1}$$

$$\int \frac{2x+1}{x^2+1}\,\mathrm{d}x = \int \frac{2x}{x^2+1}\,\mathrm{d}x + \int \frac{1}{x^2+1}\,\mathrm{d}x$$

$$\int \frac{2x+1}{x^2+1}\,\mathrm{d}x = \ln(x^2+1) + \tan^{-1}x + c \quad\checkmark$$

Question 5 - divide first:

$$x^2 + x + 1 = (x^2 + 1) + x$$

$$\frac{x^2 + x + 1}{x^2 + 1} = 1 + \frac{x}{x^2+1}$$

$$\int \frac{x^2 + x + 1}{x^2 + 1}\,\mathrm{d}x = \int 1\,\mathrm{d}x + \int \frac{x}{x^2+1}\,\mathrm{d}x$$

$$\int \frac{x^2 + x + 1}{x^2 + 1}\,\mathrm{d}x = x + \frac{1}{2}\ln(x^2+1) + c \quad\checkmark$$

---

# PART 5: Integration by Parts

Integration by parts is the reverse of the product rule. From the product rule, integrate both sides and rearrange:

$$\int u\,\frac{\mathrm{d}v}{\mathrm{d}x}\,\mathrm{d}x = uv - \int v\,\frac{\mathrm{d}u}{\mathrm{d}x}\,\mathrm{d}x$$

You choose which factor is $u$ (to be differentiated) and which is $\frac{\mathrm{d}v}{\mathrm{d}x}$ (to be integrated). The aim: $\int v\,\frac{\mathrm{d}u}{\mathrm{d}x}\,\mathrm{d}x$ must be easier than the original.

## 5.1 Choosing $u$ - LIATE

Pick $u$ from this list, earliest first: **L**ogarithms, **I**nverse trig, **A**lgebraic (polynomials), **T**rigonometric, **E**xponential.

| Integrand | Choose $u$ | Choose $\frac{\mathrm{d}v}{\mathrm{d}x}$ | Why |
|---|---|---|---|
| $x e^{2x}$ | $x$ | $e^{2x}$ | differentiating $x$ kills the polynomial |
| $x \ln x$ | $\ln x$ | $x$ | differentiating $\ln x$ gives $\frac{1}{x}$ |
| $\ln x$ (as $1 \cdot \ln x$) | $\ln x$ | $1$ | the only way to get started |
| $x^2 \sin x$ | $x^2$ | $\sin x$ | needs two rounds; power drops each time |
| $x \tan^{-1}x$ | $\tan^{-1}x$ | $x$ | derivative $\frac{1}{1+x^2}$ combines with $v$ |

> ⭐ **Watch Out!** The coursebook warning: for $\int x\ln x\,\mathrm{d}x$, choosing $u = x$ and $\frac{\mathrm{d}v}{\mathrm{d}x} = \ln x$ leaves you needing to integrate $\ln x$ - legal only if you know the trick below. Choose $u = \ln x$ first.

### Example 25 - Easy - Polynomial times exponential (coursebook Worked Example 8.15)

> **Question:** Find $\int x\,e^{2x}\,\mathrm{d}x$.

**Solution:**

Choose $u = x$ and $\frac{\mathrm{d}v}{\mathrm{d}x} = e^{2x}$:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = 1, \qquad v = \frac{1}{2}e^{2x}$$

Substitute into the formula:

$$\int x\,e^{2x}\,\mathrm{d}x = x \cdot \frac{1}{2}e^{2x} - \int \frac{1}{2}e^{2x} \cdot 1\,\mathrm{d}x$$

$$\int x\,e^{2x}\,\mathrm{d}x = \frac{x}{2}e^{2x} - \frac{1}{2}\int e^{2x}\,\mathrm{d}x$$

Integrate the leftover:

$$\int x\,e^{2x}\,\mathrm{d}x = \frac{x}{2}e^{2x} - \frac{1}{2} \cdot \frac{1}{2}e^{2x} + c$$

$$\int x\,e^{2x}\,\mathrm{d}x = \frac{x}{2}e^{2x} - \frac{1}{4}e^{2x} + c \quad\checkmark$$

**What the examiner wants:** correct $v = \frac{1}{2}e^{2x}$ (not $e^{2x}$), the minus sign in the formula, and $c$ at the end.

### Example 26 - Medium - $\ln x$ as $u$ (coursebook Worked Example 8.16)

> **Question:** Find $\int x\ln x\,\mathrm{d}x$.

**Solution:**

Choose $u = \ln x$ and $\frac{\mathrm{d}v}{\mathrm{d}x} = x$:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = \frac{1}{x}, \qquad v = \frac{x^2}{2}$$

Substitute into the formula:

$$\int x\ln x\,\mathrm{d}x = \ln x \cdot \frac{x^2}{2} - \int \frac{x^2}{2} \cdot \frac{1}{x}\,\mathrm{d}x$$

Simplify the leftover integral:

$$\int x\ln x\,\mathrm{d}x = \frac{x^2}{2}\ln x - \frac{1}{2}\int x\,\mathrm{d}x$$

$$\int x\ln x\,\mathrm{d}x = \frac{x^2}{2}\ln x - \frac{1}{2} \cdot \frac{x^2}{2} + c$$

$$\int x\ln x\,\mathrm{d}x = \frac{x^2}{2}\ln x - \frac{x^2}{4} + c \quad\checkmark$$

**What the examiner wants:** $\ln x$ as $u$ so its derivative $\frac{1}{x}$ cancels the polynomial.

### Example 27 - Medium - $\int \ln x\,\mathrm{d}x$ - the 1 trick (coursebook Worked Example 8.17)

> **Question:** Find $\int \ln x\,\mathrm{d}x$.

**Solution:**

Write the integrand as $1 \cdot \ln x$:

$$\int \ln x\,\mathrm{d}x = \int 1 \cdot \ln x\,\mathrm{d}x$$

Choose $u = \ln x$ and $\frac{\mathrm{d}v}{\mathrm{d}x} = 1$:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = \frac{1}{x}, \qquad v = x$$

Substitute into the formula:

$$\int \ln x\,\mathrm{d}x = \ln x \cdot x - \int x \cdot \frac{1}{x}\,\mathrm{d}x$$

Simplify:

$$\int \ln x\,\mathrm{d}x = x\ln x - \int 1\,\mathrm{d}x$$

$$\int \ln x\,\mathrm{d}x = x\ln x - x + c \quad\checkmark$$

**What the examiner wants:** the trick of multiplying by 1 so parts can start. This result is reused constantly, including inside repeated parts.

## 5.2 Repeated Integration by Parts

When $u$ is a polynomial of degree $n$, one application lowers its degree by 1, so you may need $n$ applications. After each application the new integral is the same type with a smaller power of $x$; keep going until the polynomial is gone.

### Example 28 - Hard - Two rounds of parts (coursebook Worked Example 8.18)

> **Question:** Find $\int x^2\sin x\,\mathrm{d}x$.

**Solution:**

First application - choose $u = x^2$ and $\frac{\mathrm{d}v}{\mathrm{d}x} = \sin x$:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = 2x, \qquad v = -\cos x$$

$$\int x^2\sin x\,\mathrm{d}x = -x^2\cos x - \int (-\cos x)(2x)\,\mathrm{d}x$$

$$\int x^2\sin x\,\mathrm{d}x = -x^2\cos x + 2\int x\cos x\,\mathrm{d}x$$

Second application on $\int x\cos x\,\mathrm{d}x$ - choose $u = x$ and $\frac{\mathrm{d}v}{\mathrm{d}x} = \cos x$:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = 1, \qquad v = \sin x$$

$$\int x\cos x\,\mathrm{d}x = x\sin x - \int \sin x\,\mathrm{d}x$$

$$\int x\cos x\,\mathrm{d}x = x\sin x + \cos x$$

Substitute back into the first result:

$$\int x^2\sin x\,\mathrm{d}x = -x^2\cos x + 2\left(x\sin x + \cos x\right) + c$$

$$\int x^2\sin x\,\mathrm{d}x = -x^2\cos x + 2x\sin x + 2\cos x + c \quad\checkmark$$

**What the examiner wants:** discipline across two by-parts rounds, each with the formula shown. The June 2023 Paper 31 report: candidates who show each application earn the process marks.

### Example 29 - Hard - Repeated parts with exponential, definite (J16 P31 Q2, 5 marks, computed estimate)

> **Question:** Find the exact value of $\int_0^2 x^2 e^{-2x}\,\mathrm{d}x$.

**Solution:**

First application - choose $u = x^2$ and $\frac{\mathrm{d}v}{\mathrm{d}x} = e^{-2x}$:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = 2x, \qquad v = -\frac{1}{2}e^{-2x}$$

$$\int x^2 e^{-2x}\,\mathrm{d}x = -\frac{x^2}{2}e^{-2x} - \int \left(-\frac{1}{2}e^{-2x}\right)(2x)\,\mathrm{d}x$$

$$\int x^2 e^{-2x}\,\mathrm{d}x = -\frac{x^2}{2}e^{-2x} + \int x\,e^{-2x}\,\mathrm{d}x$$

Second application on $\int x\,e^{-2x}\,\mathrm{d}x$ - choose $u = x$ and $\frac{\mathrm{d}v}{\mathrm{d}x} = e^{-2x}$:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = 1, \qquad v = -\frac{1}{2}e^{-2x}$$

$$\int x\,e^{-2x}\,\mathrm{d}x = -\frac{x}{2}e^{-2x} - \int \left(-\frac{1}{2}e^{-2x}\right)(1)\,\mathrm{d}x$$

$$\int x\,e^{-2x}\,\mathrm{d}x = -\frac{x}{2}e^{-2x} + \frac{1}{2}\int e^{-2x}\,\mathrm{d}x$$

$$\int x\,e^{-2x}\,\mathrm{d}x = -\frac{x}{2}e^{-2x} - \frac{1}{4}e^{-2x}$$

Assemble the antiderivative:

$$\int x^2 e^{-2x}\,\mathrm{d}x = -\frac{x^2}{2}e^{-2x} - \frac{x}{2}e^{-2x} - \frac{1}{4}e^{-2x}$$

Factor out $-\frac{1}{4}e^{-2x}$:

$$\int x^2 e^{-2x}\,\mathrm{d}x = -\frac{1}{4}e^{-2x}\left(2x^2 + 2x + 1\right)$$

Evaluate from 0 to 2:

$$\int_0^2 x^2 e^{-2x}\,\mathrm{d}x = \left[-\frac{1}{4}e^{-2x}\left(2x^2 + 2x + 1\right)\right]_0^2$$

$$\int_0^2 x^2 e^{-2x}\,\mathrm{d}x = -\frac{1}{4}e^{-4}(8 + 4 + 1) - \left(-\frac{1}{4}e^{0}(1)\right)$$

$$\int_0^2 x^2 e^{-2x}\,\mathrm{d}x = -\frac{13}{4e^4} + \frac{1}{4}$$

$$\int_0^2 x^2 e^{-2x}\,\mathrm{d}x = \frac{1}{4}\left(1 - 13e^{-4}\right) \quad\checkmark$$

**What the examiner wants:** two clean by-parts rounds with careful signs, then exact evaluation. (Answer computed from first principles; the coursebook marks this question 5 marks.)

## 5.3 Definite Integration by Parts

Apply the formula with limits on every term:

$$\int_a^b u\,\frac{\mathrm{d}v}{\mathrm{d}x}\,\mathrm{d}x = \Big[uv\Big]_a^b - \int_a^b v\,\frac{\mathrm{d}u}{\mathrm{d}x}\,\mathrm{d}x$$

### Example 30 - Medium - Definite by parts with trig (coursebook Worked Example 8.20)

> **Question:** Find the exact value of $\int_0^{\pi/2} 4x\sin 2x\,\mathrm{d}x$.

**Solution:**

Choose $u = 4x$ and $\frac{\mathrm{d}v}{\mathrm{d}x} = \sin 2x$:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = 4, \qquad v = -\frac{1}{2}\cos 2x$$

Substitute into the definite formula:

$$\int_0^{\pi/2} 4x\sin 2x\,\mathrm{d}x = \left[-2x\cos 2x\right]_0^{\pi/2} - \int_0^{\pi/2} \left(-\frac{1}{2}\cos 2x\right)(4)\,\mathrm{d}x$$

$$\int_0^{\pi/2} 4x\sin 2x\,\mathrm{d}x = \left[-2x\cos 2x\right]_0^{\pi/2} + \int_0^{\pi/2} 2\cos 2x\,\mathrm{d}x$$

Evaluate the boundary term:

$$\left[-2x\cos 2x\right]_0^{\pi/2} = -2\left(\frac{\pi}{2}\right)\cos\pi - 0 = -\pi(-1) = \pi$$

Integrate the leftover:

$$\int_0^{\pi/2} 2\cos 2x\,\mathrm{d}x = \left[\sin 2x\right]_0^{\pi/2} = \sin\pi - \sin 0 = 0$$

Assemble:

$$\int_0^{\pi/2} 4x\sin 2x\,\mathrm{d}x = \pi + 0 = \pi \quad\checkmark$$

**What the examiner wants:** correct $v = -\frac{1}{2}\cos 2x$, exact trig values ($\cos\pi = -1$, $\sin\pi = 0$) at the limits.

### Example 31 - Medium - By parts with a fractional power (N13 P31 Q3, 5 marks)

> **Question:** Find the exact value of $\int_1^4 \frac{\ln x}{\sqrt{x}}\,\mathrm{d}x$.

**Solution:**

Rewrite with a fractional power:

$$\int_1^4 \frac{\ln x}{\sqrt{x}}\,\mathrm{d}x = \int_1^4 x^{-1/2}\ln x\,\mathrm{d}x$$

Choose $u = \ln x$ and $\frac{\mathrm{d}v}{\mathrm{d}x} = x^{-1/2}$:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = \frac{1}{x}, \qquad v = 2x^{1/2} = 2\sqrt{x}$$

Substitute into the definite formula:

$$\int_1^4 x^{-1/2}\ln x\,\mathrm{d}x = \left[2\sqrt{x}\ln x\right]_1^4 - \int_1^4 2\sqrt{x} \cdot \frac{1}{x}\,\mathrm{d}x$$

Simplify the leftover integral:

$$\int_1^4 2\sqrt{x} \cdot \frac{1}{x}\,\mathrm{d}x = \int_1^4 2x^{-1/2}\,\mathrm{d}x = \left[4\sqrt{x}\right]_1^4$$

So:

$$\int_1^4 \frac{\ln x}{\sqrt{x}}\,\mathrm{d}x = \left[2\sqrt{x}\ln x - 4\sqrt{x}\right]_1^4$$

Substitute the limits:

$$\int_1^4 \frac{\ln x}{\sqrt{x}}\,\mathrm{d}x = \left(2(2)\ln 4 - 4(2)\right) - \left(2(1)\ln 1 - 4(1)\right)$$

$$\int_1^4 \frac{\ln x}{\sqrt{x}}\,\mathrm{d}x = (4\ln 4 - 8) - (0 - 4)$$

$$\int_1^4 \frac{\ln x}{\sqrt{x}}\,\mathrm{d}x = 4\ln 4 - 4 = 4(\ln 4 - 1) \quad\checkmark$$

**What the examiner wants:** $\ln x$ as $u$ (never as $\frac{\mathrm{d}v}{\mathrm{d}x}$), correct fractional-power integration, exact answer.

## 5.4 Self-Referencing Integration by Parts

Sometimes the new integral equals the ORIGINAL integral $I$. Then you get an equation $I = \dots - I$, which you solve for $I$. This trick also reappears in Chapter 10.

### Example 32 - Medium - Solving $I = (\ln x)^2 - I$ (coursebook Worked Example 8.19)

> **Question:** Given that $I = \int \frac{\ln x}{x}\,\mathrm{d}x$, use integration by parts to show that $I = \frac{1}{2}(\ln x)^2 + c$.

**Solution:**

Choose $u = \ln x$ and $\frac{\mathrm{d}v}{\mathrm{d}x} = \frac{1}{x}$:

$$\frac{\mathrm{d}u}{\mathrm{d}x} = \frac{1}{x}, \qquad v = \ln x$$

Substitute into the formula:

$$I = \ln x \cdot \ln x - \int \ln x \cdot \frac{1}{x}\,\mathrm{d}x$$

The new integral is exactly the original $I$:

$$I = (\ln x)^2 - I$$

Add $I$ to both sides:

$$2I = (\ln x)^2$$

Divide by 2:

$$I = \frac{1}{2}(\ln x)^2 + c \quad\checkmark$$

**What the examiner wants:** noticing the new integral equals the original, then solving the equation for $I$ rather than integrating again.

## 5.5 Combining Techniques

Real exam questions rarely test one technique in isolation. The common combinations: partial fractions then integrate each piece; algebraic simplification first; trig identities before integrating; substitution inside a by-parts problem; a by-parts result used to prove an equation.

**A decision flow for any new integral:**

1. Can I see it as a known standard integral (powers, $e$, trig, $\frac{1}{x^2+a^2}$)?
2. Is the numerator a multiple of the derivative of the denominator ($\frac{k f'}{f}$)?
3. Is it a product? Then integration by parts.
4. Is it a rational function? Then partial fractions (divide first if improper).
5. Would a given substitution make it simpler? Use it, and convert limits if definite.

### Example 33 - Hard - Substitution then by parts (J11 P31 Q7, 3 + 5 marks, computed estimate)

> **Question:** The integral $I$ is defined by $I = \int_1^2 (2x-2)\ln x\,\mathrm{d}x$. (i) Use the substitution $x = t^2 + 1$ to show that $I = \int_0^1 4t^3\ln(1+t^2)\,\mathrm{d}t$. (ii) Hence find the exact value of $I$.

**Solution:**

Part (i) - differentiate the substitution:

$$x = t^2 + 1 \quad\Rightarrow\quad \frac{\mathrm{d}x}{\mathrm{d}t} = 2t \quad\Rightarrow\quad \mathrm{d}x = 2t\,\mathrm{d}t$$

Convert the limits:

$$x = 1 \quad\Rightarrow\quad t^2 + 1 = 1 \quad\Rightarrow\quad t = 0$$

$$x = 2 \quad\Rightarrow\quad t^2 + 1 = 2 \quad\Rightarrow\quad t = 1$$

Rewrite every piece:

$$2x - 2 = 2(t^2 + 1) - 2 = 2t^2$$

$$\ln x = \ln(t^2 + 1)$$

Rewrite the integral:

$$I = \int_0^1 (2t^2)\ln(1+t^2) \cdot 2t\,\mathrm{d}t$$

$$I = \int_0^1 4t^3\ln(1+t^2)\,\mathrm{d}t \quad\checkmark$$

Part (ii) - integrate by parts: choose $u = \ln(1+t^2)$ and $\frac{\mathrm{d}v}{\mathrm{d}t} = 4t^3$:

$$\frac{\mathrm{d}u}{\mathrm{d}t} = \frac{2t}{1+t^2}, \qquad v = t^4$$

$$I = \left[t^4\ln(1+t^2)\right]_0^1 - \int_0^1 t^4 \cdot \frac{2t}{1+t^2}\,\mathrm{d}t$$

Evaluate the boundary term:

$$\left[t^4\ln(1+t^2)\right]_0^1 = 1 \cdot \ln 2 - 0 = \ln 2$$

Divide the algebraic fraction in the leftover integral:

$$\frac{2t^5}{1+t^2} = 2t^3 - 2t + \frac{2t}{1+t^2}$$

So:

$$I = \ln 2 - \int_0^1 \left(2t^3 - 2t + \frac{2t}{1+t^2}\right)\mathrm{d}t$$

Integrate each piece (the last one is $\frac{k f'}{f}$ with $f = 1+t^2$):

$$I = \ln 2 - \left[\frac{t^4}{2} - t^2 + \ln(1+t^2)\right]_0^1$$

Substitute the limits:

$$I = \ln 2 - \left(\frac{1}{2} - 1 + \ln 2 - 0\right)$$

$$I = \ln 2 - \ln 2 + \frac{1}{2} = \frac{1}{2} \quad\checkmark$$

**What the examiner wants:** clean substitution with limits, then a correct by-parts run with algebraic division of the remainder. Check: $\int_1^2 (2x-2)\ln x\,\mathrm{d}x = \frac{1}{2}$ directly also verifies this answer.

### Example 34 - Medium - Trig identity then integrate (J15 P31 Q5, 3 + 5 marks)

> **Question:** (a) Find $\int \left(4 + \tan^2 2x\right)\mathrm{d}x$. (b) Find the exact value of $\int_{\pi/4}^{\pi/2} \frac{\sin\left(x + \frac{\pi}{6}\right)}{\sin x}\,\mathrm{d}x$.

**Solution:**

Part (a) - use $\tan^2 2x = \sec^2 2x - 1$:

$$\int \left(4 + \tan^2 2x\right)\mathrm{d}x = \int \left(4 + \sec^2 2x - 1\right)\mathrm{d}x$$

$$\int \left(4 + \tan^2 2x\right)\mathrm{d}x = \int \left(3 + \sec^2 2x\right)\mathrm{d}x$$

$$\int \left(4 + \tan^2 2x\right)\mathrm{d}x = 3x + \frac{1}{2}\tan 2x + c \quad\checkmark$$

Part (b) - expand the numerator with the compound-angle formula:

$$\sin\left(x + \frac{\pi}{6}\right) = \sin x\cos\left(\frac{\pi}{6}\right) + \cos x\sin\left(\frac{\pi}{6}\right)$$

$$\sin\left(x + \frac{\pi}{6}\right) = \frac{\sqrt{3}}{2}\sin x + \frac{1}{2}\cos x$$

Divide by $\sin x$:

$$\frac{\sin\left(x + \frac{\pi}{6}\right)}{\sin x} = \frac{\sqrt{3}}{2} + \frac{1}{2}\cot x$$

Integrate:

$$\int_{\pi/4}^{\pi/2} \frac{\sin\left(x + \frac{\pi}{6}\right)}{\sin x}\,\mathrm{d}x = \left[\frac{\sqrt{3}}{2}x + \frac{1}{2}\ln|\sin x|\right]_{\pi/4}^{\pi/2}$$

Substitute the limits:

$$= \left(\frac{\sqrt{3}}{2} \cdot \frac{\pi}{2} + \frac{1}{2}\ln 1\right) - \left(\frac{\sqrt{3}}{2} \cdot \frac{\pi}{4} + \frac{1}{2}\ln\left(\frac{\sqrt{2}}{2}\right)\right)$$

$$= \frac{\sqrt{3}\pi}{4} - \frac{\sqrt{3}\pi}{8} - \frac{1}{2}\ln\left(\frac{\sqrt{2}}{2}\right)$$

Since $\ln\left(\frac{\sqrt{2}}{2}\right) = \frac{1}{2}\ln 2 - \ln 2 = -\frac{1}{2}\ln 2$:

$$= \frac{\sqrt{3}\pi}{8} + \frac{1}{4}\ln 2 \quad\checkmark$$

**What the examiner wants:** (a) the $\sec^2 - 1$ trick; (b) the compound-angle expansion used to split a quotient that otherwise looks unintegrable. (Answer to (b) verified against the coursebook answers file.)

### Example 35 - Hard - Identity, then $\frac{k f'}{f}$ integrals (N16 P31 Q5, 4 + 4 marks)

> **Question:** (i) Prove the identity $\tan 2\theta - \tan\theta \equiv \tan\theta\sec 2\theta$. (ii) Hence show that $\int_0^{\pi/6} \tan\theta\sec 2\theta\,\mathrm{d}\theta = \frac{1}{2}\ln\left(\frac{3}{2}\right)$.

**Solution:**

Part (i) - write $t = \tan\theta$ and use the double-angle formulas:

$$\tan 2\theta = \frac{2t}{1-t^2}, \qquad \sec 2\theta = \frac{1+t^2}{1-t^2}$$

Left-hand side:

$$\tan 2\theta - \tan\theta = \frac{2t}{1-t^2} - t$$

$$= \frac{2t - t(1-t^2)}{1-t^2} = \frac{2t - t + t^3}{1-t^2} = \frac{t + t^3}{1-t^2}$$

Factor:

$$= \frac{t(1+t^2)}{1-t^2}$$

Right-hand side:

$$\tan\theta\sec 2\theta = t \cdot \frac{1+t^2}{1-t^2} = \frac{t(1+t^2)}{1-t^2}$$

Both sides are equal, so:

$$\tan 2\theta - \tan\theta \equiv \tan\theta\sec 2\theta \quad\checkmark$$

Part (ii) - replace the integrand using the identity:

$$\int_0^{\pi/6} \tan\theta\sec 2\theta\,\mathrm{d}\theta = \int_0^{\pi/6} \left(\tan 2\theta - \tan\theta\right)\mathrm{d}\theta$$

Integrate each piece with the $\frac{k f'}{f}$ rule:

$$\int \tan 2\theta\,\mathrm{d}\theta = -\frac{1}{2}\ln|\cos 2\theta|, \qquad \int \tan\theta\,\mathrm{d}\theta = -\ln|\cos\theta|$$

So:

$$\int_0^{\pi/6} \tan\theta\sec 2\theta\,\mathrm{d}\theta = \left[-\frac{1}{2}\ln|\cos 2\theta| + \ln|\cos\theta|\right]_0^{\pi/6}$$

Substitute the upper limit:

$$-\frac{1}{2}\ln\left(\cos\frac{\pi}{3}\right) + \ln\left(\cos\frac{\pi}{6}\right) = -\frac{1}{2}\ln\left(\frac{1}{2}\right) + \ln\left(\frac{\sqrt{3}}{2}\right)$$

$$= \frac{1}{2}\ln 2 + \frac{1}{2}\ln 3 - \ln 2 = \frac{1}{2}\ln 3 - \frac{1}{2}\ln 2$$

Substitute the lower limit:

$$-\frac{1}{2}\ln(\cos 0) + \ln(\cos 0) = -\frac{1}{2}\ln 1 + \ln 1 = 0$$

Assemble:

$$\int_0^{\pi/6} \tan\theta\sec 2\theta\,\mathrm{d}\theta = \frac{1}{2}\ln 3 - \frac{1}{2}\ln 2 = \frac{1}{2}\ln\left(\frac{3}{2}\right) \quad\checkmark$$

**What the examiner wants:** the identity proved with full working (a "prove" question requires every step justified), then exact trig values and tidy log laws. The June 2023 Paper 33 report: crossing terms out to match a given answer earns nothing.

### Practice Questions - Part 5

1. (Easy) Find $\int x\cos x\,\mathrm{d}x$.
2. (Medium) Find the exact value of $\int_0^{\pi/2} x\cos x\,\mathrm{d}x$.
3. (Medium) Find $\int x^2 e^x\,\mathrm{d}x$.
4. (Hard) Given that $I = \int e^x\sin x\,\mathrm{d}x$, use integration by parts twice to find $I$.
5. (Hard) Find the exact value of $\int_1^e (\ln x)^2\,\mathrm{d}x$.

**Solutions:**

Question 1:

$$u = x, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = \cos x \quad\Rightarrow\quad \frac{\mathrm{d}u}{\mathrm{d}x} = 1, \quad v = \sin x$$

$$\int x\cos x\,\mathrm{d}x = x\sin x - \int \sin x\,\mathrm{d}x$$

$$\int x\cos x\,\mathrm{d}x = x\sin x + \cos x + c \quad\checkmark$$

Question 2:

$$\int_0^{\pi/2} x\cos x\,\mathrm{d}x = \left[x\sin x + \cos x\right]_0^{\pi/2}$$

$$\int_0^{\pi/2} x\cos x\,\mathrm{d}x = \left(\frac{\pi}{2}\sin\frac{\pi}{2} + \cos\frac{\pi}{2}\right) - (0 + \cos 0)$$

$$\int_0^{\pi/2} x\cos x\,\mathrm{d}x = \frac{\pi}{2} \cdot 1 + 0 - 1 = \frac{\pi}{2} - 1 \quad\checkmark$$

Question 3 - first application:

$$u = x^2, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = e^x \quad\Rightarrow\quad \frac{\mathrm{d}u}{\mathrm{d}x} = 2x, \quad v = e^x$$

$$\int x^2 e^x\,\mathrm{d}x = x^2 e^x - 2\int x\,e^x\,\mathrm{d}x$$

Second application on $\int x\,e^x\,\mathrm{d}x$:

$$u = x, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = e^x \quad\Rightarrow\quad \frac{\mathrm{d}u}{\mathrm{d}x} = 1, \quad v = e^x$$

$$\int x\,e^x\,\mathrm{d}x = xe^x - \int e^x\,\mathrm{d}x = xe^x - e^x$$

Assemble:

$$\int x^2 e^x\,\mathrm{d}x = x^2 e^x - 2xe^x + 2e^x + c = e^x\left(x^2 - 2x + 2\right) + c \quad\checkmark$$

Question 4 - first application:

$$u = e^x, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = \sin x \quad\Rightarrow\quad \frac{\mathrm{d}u}{\mathrm{d}x} = e^x, \quad v = -\cos x$$

$$I = -e^x\cos x + \int e^x\cos x\,\mathrm{d}x$$

Second application on $\int e^x\cos x\,\mathrm{d}x$:

$$u = e^x, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = \cos x \quad\Rightarrow\quad v = \sin x$$

$$\int e^x\cos x\,\mathrm{d}x = e^x\sin x - \int e^x\sin x\,\mathrm{d}x = e^x\sin x - I$$

Substitute back:

$$I = -e^x\cos x + e^x\sin x - I$$

$$2I = e^x(\sin x - \cos x)$$

$$I = \frac{1}{2}e^x(\sin x - \cos x) + c \quad\checkmark$$

Question 5 - first application:

$$u = (\ln x)^2, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = 1 \quad\Rightarrow\quad \frac{\mathrm{d}u}{\mathrm{d}x} = \frac{2\ln x}{x}, \quad v = x$$

$$\int_1^e (\ln x)^2\,\mathrm{d}x = \left[x(\ln x)^2\right]_1^e - 2\int_1^e \ln x\,\mathrm{d}x$$

Evaluate the boundary term:

$$\left[x(\ln x)^2\right]_1^e = e(1)^2 - 1(0)^2 = e$$

Use the standard result $\int \ln x\,\mathrm{d}x = x\ln x - x$:

$$2\int_1^e \ln x\,\mathrm{d}x = 2\left[x\ln x - x\right]_1^e$$

$$= 2\left[(e \cdot 1 - e) - (1 \cdot 0 - 1)\right] = 2(0 + 1) = 2$$

Assemble:

$$\int_1^e (\ln x)^2\,\mathrm{d}x = e - 2 \quad\checkmark$$

---

# Formula Sheet

Grouped by part - all the formulas you must know cold from this chapter.

**Part 1 - $\tan^{-1}$ and $\frac{1}{x^2+a^2}$:**

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(\tan^{-1}x\right) = \frac{1}{1+x^2}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(\tan^{-1}\big(f(x)\big)\right) = \frac{f'(x)}{1 + \big(f(x)\big)^2}$$

$$\int \frac{1}{x^2 + a^2}\,\mathrm{d}x = \frac{1}{a}\tan^{-1}\left(\frac{x}{a}\right) + c$$

$$\int \frac{k}{x^2 + a^2}\,\mathrm{d}x = \frac{k}{a}\tan^{-1}\left(\frac{x}{a}\right) + c$$

**Part 2 - $\frac{k f'(x)}{f(x)}$:**

$$\int \frac{k\,f'(x)}{f(x)}\,\mathrm{d}x = k\ln\big|f(x)\big| + c$$

$$\int \tan x\,\mathrm{d}x = -\ln|\cos x| + c = \ln|\sec x| + c, \qquad \int \cot x\,\mathrm{d}x = \ln|\sin x| + c$$

**Part 3 - Substitution:**

$$u = g(x) \quad\Rightarrow\quad \mathrm{d}u = g'(x)\,\mathrm{d}x, \qquad \int f(g(x))\,g'(x)\,\mathrm{d}x = \int f(u)\,\mathrm{d}u$$

$$x = a\sin\theta \quad\Rightarrow\quad \sqrt{a^2 - x^2} = a\cos\theta$$

$$x = a\tan\theta \quad\Rightarrow\quad x^2 + a^2 = a^2\sec^2\theta$$

$$\int_a^b f(x)\,\mathrm{d}x \text{ with } u = g(x) \text{ becomes } \int_{g(a)}^{g(b)} \dots \,\mathrm{d}u$$

**Part 4 - Partial fractions:**

| Denominator contains | Decomposition | Integral |
|---|---|---|
| $(ax+b)(cx+d)$ | $\frac{A}{ax+b} + \frac{B}{cx+d}$ | $\frac{A}{a}\ln|ax+b| + \frac{B}{c}\ln|cx+d|$ |
| $(ax+b)^2$ | $\frac{A}{ax+b} + \frac{B}{(ax+b)^2}$ | $\frac{A}{a}\ln|ax+b| - \frac{B}{a(ax+b)}$ |
| $ax^2+bx+c$ | $\frac{Ax+B}{ax^2+bx+c}$ | log part + arctan part |

Improper fraction (numerator degree $\geq$ denominator degree)? Divide first.

**Part 5 - Integration by parts:**

$$\int u\,\frac{\mathrm{d}v}{\mathrm{d}x}\,\mathrm{d}x = uv - \int v\,\frac{\mathrm{d}u}{\mathrm{d}x}\,\mathrm{d}x$$

$$\int_a^b u\,\frac{\mathrm{d}v}{\mathrm{d}x}\,\mathrm{d}x = \Big[uv\Big]_a^b - \int_a^b v\,\frac{\mathrm{d}u}{\mathrm{d}x}\,\mathrm{d}x$$

$$\int \ln x\,\mathrm{d}x = x\ln x - x + c$$

Choose $u$ by LIATE: Logarithms, Inverse trig, Algebraic, Trigonometric, Exponential.

**Classic exact values at limits:** $\tan^{-1}0 = 0$, $\tan^{-1}1 = \frac{\pi}{4}$, $\tan^{-1}\frac{1}{\sqrt{3}} = \frac{\pi}{6}$, $\tan^{-1}\sqrt{3} = \frac{\pi}{3}$; $\ln 1 = 0$; $\ln\frac{\sqrt{3}}{2} = \frac{1}{2}\ln 3 - \ln 2$.

---

# Quick Reference Card

- **Differentiate $\tan^{-1}$:** $\frac{f'(x)}{1+f(x)^2}$. Never $\frac{1}{\tan}$.
- **$\int \frac{1}{x^2+a^2}\,\mathrm{d}x$:** always the $\frac{1}{a}$ factor: $\frac{1}{a}\tan^{-1}\left(\frac{x}{a}\right) + c$. Factor out coefficients on $x^2$ first.
- **$\frac{k f'}{f}$:** differentiate the denominator in your head; if the numerator is a constant multiple, integrate to $k\ln|f(x)|$. Watch trig versions: $\tan$, $\cot$, $\sec\tan$.
- **Substitution:** write $u$ and $\frac{\mathrm{d}u}{\mathrm{d}x}$; convert $\mathrm{d}x$; convert limits (definite); NO $x$ may survive. $x = a\sin\theta$ kills $\sqrt{a^2-x^2}$; $x = a\tan\theta$ kills $x^2+a^2$.
- **Minus-sign trap ($u = \cos x$):** keep the minus with the limits as found, OR swap limits and drop the sign. Never both, never neither.
- **Partial fractions:** divide first if improper; repeated factors get one fraction per power; quadratic factors get $Bx + C$. $\int \frac{B}{(ax+b)^2}\,\mathrm{d}x = -\frac{B}{a(ax+b)}$ - a power, NOT a log.
- **By parts:** $uv - \int v\,\frac{\mathrm{d}u}{\mathrm{d}x}\,\mathrm{d}x$; choose $u$ by LIATE; polynomials need one round per degree; if the new integral equals $I$, solve $I = \dots - I$.
- **Decision flow:** standard form? $\to$ done. Numerator multiple of $f'$ of denominator? $\to$ log. Product of unlike functions? $\to$ parts. Rational? $\to$ partial fractions. Given substitution? $\to$ use it, convert limits.
- **Always:** radians in P3 calculus, exact values (no decimals for "exact value"), and $+c$ on every indefinite integral.

---

*Sources: Cambridge International AS & A Level Mathematics 9709 syllabus (2026-2027); Cambridge Pure Mathematics 2 & 3 coursebook Chapter 8 (Worked Examples 8.1 - 8.20, Explore 8.1, Exercises 8A - 8F) and answers; Cambridge 9709 examiner reports June 2023 (Papers 31/32/33) and November 2023 (Papers 31/32/33); past papers 9709/31 N10 Q5, J11 Q7, J14 Q2, J15 Q5, J16 Q2, N11 Q8, N13 Q3, N16 Q5 and 2025 series papers. Answers marked (computed estimate) were verified by direct computation rather than against a published mark scheme.*
