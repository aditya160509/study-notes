# 📘 Chapter 4: Differentiation - 9709 Pure Mathematics 2&3 (CAIE A Level Maths)

## Cambridge International AS & A Level Mathematics (9709) - Paper 2/3

> **Rule + fully solved examples.** Every technique shown step by step in proper LaTeX, every algebra step on its own line. 30+ solved examples, practice questions with full solutions, formula sheet and quick reference card at the end.

---

# 📋 Table of Contents

1. [4.1 The Product Rule](#41-the-product-rule)
2. [4.2 The Quotient Rule](#42-the-quotient-rule)
3. [4.3 Derivatives of Exponential Functions](#43-derivatives-of-exponential-functions)
4. [4.4 Derivatives of Natural Logarithmic Functions](#44-derivatives-of-natural-logarithmic-functions)
5. [4.5 Derivatives of Trigonometric Functions](#45-derivatives-of-trigonometric-functions)
6. [4.6 Implicit Differentiation](#46-implicit-differentiation)
7. [4.7 Parametric Differentiation](#47-parametric-differentiation)
8. [Practice Questions](#practice-questions)
9. [Solutions to Practice Questions](#solutions-to-practice-questions)
10. [Formula Sheet](#formula-sheet)
11. [Quick Reference Card](#quick-reference-card)

---

# Chapter 4: Differentiation (Pemberton Chapters 4 & 8 selected material)

**Covers:** the product rule, the quotient rule, differentiating $e^{f(x)}$ and $\ln f(x)$, differentiating $\sin$, $\cos$, $\tan$ (and $\sec$, $\operatorname{cosec}$, $\cot$ as extension), implicit differentiation, and parametric differentiation. All results assume radians for trig functions.

---

## 4.1 The Product Rule

If $y = u(x)\,v(x)$ where $u$ and $v$ are differentiable functions of $x$, then:

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(u\,v\big) = u\frac{\mathrm{d}v}{\mathrm{d}x} + v\frac{\mathrm{d}u}{\mathrm{d}x}$$

In words: **(first $\times$ derivative of second) + (second $\times$ derivative of first).**

Alternative Leibniz notation with $y = uv$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = u\frac{\mathrm{d}v}{\mathrm{d}x} + v\frac{\mathrm{d}u}{\mathrm{d}x}$$

**When to use it:** whenever the function is a product of two non-constant functions of $x$ that cannot be expanded into a simple polynomial first. If it expands easily (e.g. $(x+1)(x^2-3) = x^3+x^2-3x-3$), expanding and then differentiating is often faster — but the product rule always works.

> ⭐ **Watch Out!** (1) Do NOT forget the second term — the product rule has TWO terms added, not one. (2) When $u$ or $v$ itself needs the chain rule (e.g. $(x^2+1)^{1/2}$, $\sin 2x$, $e^{3x}$), remember to apply the chain rule inside the product rule. (3) Always simplify the final answer: factorise common factors, write as a single fraction if the question asks for it.

*Derivation sketch (first principles, coursebook p.82):* with $y = uv$, a small increment $\delta x$ gives $\delta y = u\,\delta v + v\,\delta u + \delta u\,\delta v$. Dividing by $\delta x$ and letting $\delta x \to 0$ (so $\delta u \to 0$) yields the rule.

### Example 1 - Easy - direct product rule (coursebook Worked example 4.1)

> **Question:** Find $\frac{\mathrm{d}y}{\mathrm{d}x}$ when $y = (2x - 1)\sqrt{4x+5}$, i.e. $y = (2x-1)(4x+5)^{1/2}$.

**Solution:**

Let $u = 2x - 1$ and $v = (4x+5)^{1/2}$.

$$u = 2x - 1$$

$$\frac{\mathrm{d}u}{\mathrm{d}x} = 2$$

$$v = (4x+5)^{1/2}$$

$$\frac{\mathrm{d}v}{\mathrm{d}x} = \frac{1}{2}(4x+5)^{-1/2} \cdot 4$$

$$= 2(4x+5)^{-1/2}$$

$$= \frac{2}{\sqrt{4x+5}}$$

Apply the product rule $\frac{\mathrm{d}y}{\mathrm{d}x} = u\frac{\mathrm{d}v}{\mathrm{d}x} + v\frac{\mathrm{d}u}{\mathrm{d}x}$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = (2x-1)\cdot \frac{2}{\sqrt{4x+5}} + (4x+5)^{1/2}\cdot 2$$

Write the second term with denominator $\sqrt{4x+5}$:

$$(4x+5)^{1/2}\cdot 2 = \frac{2(4x+5)}{\sqrt{4x+5}}$$

So:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{2(2x-1)}{\sqrt{4x+5}} + \frac{2(4x+5)}{\sqrt{4x+5}}$$

$$= \frac{2(2x-1) + 2(4x+5)}{\sqrt{4x+5}}$$

$$= \frac{4x - 2 + 8x + 10}{\sqrt{4x+5}}$$

$$= \frac{12x + 8}{\sqrt{4x+5}} \quad\checkmark$$

**What the examiner wants:** the chain rule applied correctly to $(4x+5)^{1/2}$, both terms of the product rule present, final answer as a single fraction.

### Example 2 - Medium - find where the gradient is zero (coursebook Worked example 4.2)

> **Question:** Find the $x$-coordinate of the points on the curve $y = (2x-3)^2(5x+1)$ where the gradient is $0$.

**Solution:**

Let $u = (2x-3)^2$ and $v = 5x+1$.

$$u = (2x-3)^2$$

$$\frac{\mathrm{d}u}{\mathrm{d}x} = 2(2x-3)\cdot 2$$

$$= 4(2x-3)$$

$$v = 5x + 1$$

$$\frac{\mathrm{d}v}{\mathrm{d}x} = 5$$

Apply the product rule:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = u\frac{\mathrm{d}v}{\mathrm{d}x} + v\frac{\mathrm{d}u}{\mathrm{d}x}$$

$$= (2x-3)^2\cdot 5 + (5x+1)\cdot 4(2x-3)$$

Factor out common factor $(2x-3)$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = (2x-3)\big[5(2x-3) + 4(5x+1)\big]$$

$$= (2x-3)\big[10x - 15 + 20x + 4\big]$$

$$= (2x-3)(30x - 11)$$

Wait — re-expand carefully from coursebook factorisation. The coursebook obtains:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = (2x-3)(5x+1)\text{ bracket form; setting } = 0$$

Actually with $y = (2x-3)^2(5x+1)$ the coursebook writes $y = (2x-3)^2(5x+1)$ and obtains $\frac{\mathrm{d}y}{\mathrm{d}x} = (2x-3)[4(5x+1)+5(2x-3)]$. Set $=0$:

$$(2x-3)\big[4(5x+1) + 5(2x-3)\big] = 0$$

$$4(5x+1) + 5(2x-3) = 20x + 4 + 10x - 15$$

$$= 30x - 11$$

So:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = (2x-3)(30x-11) = 0$$

$$2x - 3 = 0 \implies x = \frac{3}{2}$$

$$30x - 11 = 0 \implies x = \frac{11}{30}$$

$$x = \frac{3}{2} \text{ or } x = \frac{11}{30} \quad\checkmark$$

**What the examiner wants:** the product rule with the chain rule on $(2x-3)^2$, factorisation, then solving $\frac{\mathrm{d}y}{\mathrm{d}x}=0$. Note $x=\frac{3}{2}$ is a repeated-root stationary point.

### Example 3 - Medium - product with exponential

> **Question:** Differentiate $y = x^2 e^{3x}$ with respect to $x$.

**Solution:**

Let $u = x^2$ and $v = e^{3x}$.

$$u = x^2$$

$$\frac{\mathrm{d}u}{\mathrm{d}x} = 2x$$

$$v = e^{3x}$$

$$\frac{\mathrm{d}v}{\mathrm{d}x} = 3e^{3x}$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = u\frac{\mathrm{d}v}{\mathrm{d}x} + v\frac{\mathrm{d}u}{\mathrm{d}x}$$

$$= x^2\cdot 3e^{3x} + e^{3x}\cdot 2x$$

$$= 3x^2e^{3x} + 2xe^{3x}$$

Factorise $xe^{3x}$:

$$= xe^{3x}(3x + 2) \quad\checkmark$$

**What the examiner wants:** factorised final answer; the $e^{3x}$ chain rule ($3e^{3x}$, not $e^{3x}$).

### Example 4 - Hard - product with trig and simplification

> **Question:** Find $\frac{\mathrm{d}y}{\mathrm{d}x}$ when $y = x\sin 2x$.

**Solution:**

Let $u = x$ and $v = \sin 2x$.

$$u = x$$

$$\frac{\mathrm{d}u}{\mathrm{d}x} = 1$$

$$v = \sin 2x$$

$$\frac{\mathrm{d}v}{\mathrm{d}x} = 2\cos 2x$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = u\frac{\mathrm{d}v}{\mathrm{d}x} + v\frac{\mathrm{d}u}{\mathrm{d}x}$$

$$= x\cdot 2\cos 2x + \sin 2x \cdot 1$$

$$= 2x\cos 2x + \sin 2x \quad\checkmark$$

No further factorisation needed. The chain rule on $\sin 2x$ gives $2\cos 2x$, not $\cos 2x$.

**What the examiner wants:** full chain rule inside the product rule; answer left in exact trig form.

---

## 4.2 The Quotient Rule

If $y = \dfrac{u(x)}{v(x)}$ where $u$ and $v$ are differentiable and $v \neq 0$, then:

$$\frac{\mathrm{d}}{\mathrm{d}x}\!\left(\frac{u}{v}\right) = \frac{\,v\dfrac{\mathrm{d}u}{\mathrm{d}x} - u\dfrac{\mathrm{d}v}{\mathrm{d}x}\,}{v^{2}}$$

In words: **(bottom $\times$ derivative of top $-$ top $\times$ derivative of bottom) over (bottom squared).**

Order matters — it is $v\,u' - u\,v'$, not the reverse. The denominator is always $v^2$ (positive).

> ⭐ **Watch Out!** (1) The MINUS sign is the most common error — writing $+$ instead of $-$. (2) The denominator is $v^2$, not $v$. (3) When $u$ or $v$ needs the chain rule, apply it before substituting into the quotient formula. (4) An alternative is to write $\frac{u}{v} = u\,v^{-1}$ and use the product rule — both methods give the same answer (coursebook Explore 4.1). Choose whichever you find more reliable under exam pressure.

*Derivation sketch (coursebook p.84):* write $y = u/v$, so $y\,v = u$; differentiate both sides with product rule on the left and rearrange to obtain the formula.

### Example 5 - Easy - direct quotient rule (coursebook Worked example 4.3)

> **Question:** Find the derivative of $y = \dfrac{x^{2}-5}{2x+1}$.

**Solution:**

Let $u = x^2 - 5$ and $v = 2x + 1$.

$$u = x^{2} - 5$$

$$\frac{\mathrm{d}u}{\mathrm{d}x} = 2x$$

$$v = 2x + 1$$

$$\frac{\mathrm{d}v}{\mathrm{d}x} = 2$$

Apply the quotient rule $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{v\,u' - u\,v'}{v^{2}}$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{(2x+1)(2x) - (x^{2}-5)(2)}{(2x+1)^{2}}$$

Expand the numerator:

$$(2x+1)(2x) = 4x^{2} + 2x$$

$$(x^{2}-5)(2) = 2x^{2} - 10$$

So numerator:

$$4x^{2} + 2x - (2x^{2} - 10)$$

$$= 4x^{2} + 2x - 2x^{2} + 10$$

$$= 2x^{2} + 2x + 10$$

$$= 2(x^{2} + x + 5)$$

Therefore:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{2x^{2} + 2x + 10}{(2x+1)^{2}}$$

$$= \frac{2(x^{2}+x+5)}{(2x+1)^{2}} \quad\checkmark$$

**What the examiner wants:** the correct minus sign; numerator expanded and simplified; denominator left as $(2x+1)^2$.

### Example 6 - Medium - quotient with a fractional power (coursebook Worked example 4.4)

> **Question:** Find the derivative of $y = \dfrac{(x+2)^{3}}{\sqrt{x-1}} = \dfrac{(x+2)^{3}}{(x-1)^{1/2}}$.

**Solution:**

Let $u = (x+2)^{3}$ and $v = (x-1)^{1/2}$.

$$u = (x+2)^{3}$$

$$\frac{\mathrm{d}u}{\mathrm{d}x} = 3(x+2)^{2}$$

$$v = (x-1)^{1/2}$$

$$\frac{\mathrm{d}v}{\mathrm{d}x} = \frac{1}{2}(x-1)^{-1/2}$$

$$= \frac{1}{2\sqrt{x-1}}$$

Apply the quotient rule:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{v\,u' - u\,v'}{v^{2}}$$

$$= \frac{(x-1)^{1/2}\cdot 3(x+2)^{2} - (x+2)^{3}\cdot \frac{1}{2}(x-1)^{-1/2}}{(x-1)}$$

Multiply numerator and denominator by $(x-1)^{1/2}$ to clear the negative power (equivalently multiply top and bottom by $2(x-1)^{1/2}$):

Numerator $\times 2(x-1)^{1/2}$:

$$2(x-1)^{1/2}\cdot (x-1)^{1/2}\cdot 3(x+2)^{2} = 6(x-1)(x+2)^{2}$$

$$2(x-1)^{1/2}\cdot (x+2)^{3}\cdot \frac{1}{2}(x-1)^{-1/2} = (x+2)^{3}$$

So combined numerator over $2(x-1)^{1/2}$:

$$\text{numerator} = \frac{6(x-1)(x+2)^{2} - (x+2)^{3}}{2(x-1)^{1/2}}$$

Dividing by $v^{2} = (x-1)$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{6(x-1)(x+2)^{2} - (x+2)^{3}}{2(x-1)^{3/2}}$$

Factor out $(x+2)^{2}$:

$$= \frac{(x+2)^{2}\big[6(x-1) - (x+2)\big]}{2(x-1)^{3/2}}$$

$$= \frac{(x+2)^{2}\big[6x - 6 - x - 2\big]}{2(x-1)^{3/2}}$$

$$= \frac{(x+2)^{2}(5x - 8)}{2(x-1)^{3/2}} \quad\checkmark$$

**What the examiner wants:** handling the fractional power with the chain rule, clearing the compound fraction by multiplying through, factorised final form.

### Example 7 - Medium - quotient with trig

> **Question:** Differentiate $y = \dfrac{\sin x}{x}$ with respect to $x$ (for $x \neq 0$).

**Solution:**

Let $u = \sin x$ and $v = x$.

$$u = \sin x$$

$$\frac{\mathrm{d}u}{\mathrm{d}x} = \cos x$$

$$v = x$$

$$\frac{\mathrm{d}v}{\mathrm{d}x} = 1$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{v\,u' - u\,v'}{v^{2}}$$

$$= \frac{x\cos x - \sin x \cdot 1}{x^{2}}$$

$$= \frac{x\cos x - \sin x}{x^{2}} \quad\checkmark$$

**What the examiner wants:** recognising this is a standard quotient-rule shape; answer as a single fraction.

### Example 8 - Hard - product vs quotient equivalence

> **Question:** Show that differentiating $y = \dfrac{x^{2}-5}{2x+1}$ by writing it as $y = (x^{2}-5)(2x+1)^{-1}$ and using the product rule gives the same result as the quotient rule.

**Solution:**

Write $y = (x^{2}-5)(2x+1)^{-1}$. Let $u = x^{2}-5$, $w = (2x+1)^{-1}$.

$$u = x^{2} - 5$$

$$\frac{\mathrm{d}u}{\mathrm{d}x} = 2x$$

$$w = (2x+1)^{-1}$$

$$\frac{\mathrm{d}w}{\mathrm{d}x} = -1\cdot(2x+1)^{-2}\cdot 2$$

$$= -2(2x+1)^{-2}$$

Product rule: $\frac{\mathrm{d}y}{\mathrm{d}x} = u\,w' + w\,u'$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = (x^{2}-5)\cdot\big[-2(2x+1)^{-2}\big] + (2x+1)^{-1}\cdot 2x$$

$$= \frac{-2(x^{2}-5)}{(2x+1)^{2}} + \frac{2x}{2x+1}$$

Put over common denominator $(2x+1)^{2}$:

$$\frac{2x}{2x+1} = \frac{2x(2x+1)}{(2x+1)^{2}}$$

$$= \frac{4x^{2}+2x}{(2x+1)^{2}}$$

So:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{-2x^{2}+10 + 4x^{2}+2x}{(2x+1)^{2}}$$

$$= \frac{2x^{2}+2x+10}{(2x+1)^{2}}$$

This matches Example 5. $\checkmark$

**What the examiner wants:** confidence that either method is acceptable — but the quotient rule is usually faster for quotients.

---

## 4.3 Derivatives of Exponential Functions

### The basic result

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(e^{x}\big) = e^{x}$$

The function $e^{x}$ is its own derivative. This is the defining property of $e$.

### The chain-rule extension

If $y = e^{f(x)}$ where $f$ is differentiable, then by the chain rule:

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(e^{f(x)}\big) = f'(x)\,e^{f(x)}$$

In particular, for a linear exponent $ax+b$:

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(e^{ax+b}\big) = a\,e^{ax+b}$$

### Powers of $a$ (base-$a$ exponential)

For $y = a^{x}$ with $a > 0$, write $a^{x} = e^{x\ln a}$, so:

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(a^{x}\big) = a^{x}\ln a$$

And more generally:

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(a^{f(x)}\big) = f'(x)\,a^{f(x)}\ln a$$

> ⭐ **Watch Out!** (1) $\frac{\mathrm{d}}{\mathrm{d}x}(e^{ax+b}) = a\,e^{ax+b}$ — the $a$ multiplies in front, the exponent stays. Forgetting the $a$ is the most common error. (2) $e^{x}$ differentiates to $e^{x}$, but $(e^{x})^{2} = e^{2x}$ differentiates to $2e^{2x}$, not $2e^{x}$. (3) $a^{x}$ is NOT the same as $x^{a}$: $\frac{\mathrm{d}}{\mathrm{d}x}(x^{a}) = ax^{a-1}$ (power rule) vs $\frac{\mathrm{d}}{\mathrm{d}x}(a^{x}) = a^{x}\ln a$ (exponential rule). (4) When the exam writes $\exp(x)$ it means $e^{x}$.

### Example 9 - Easy - differentiating $e^{f(x)}$ (coursebook Worked example 4.5)

> **Question:** Differentiate with respect to $x$: **(a)** $e^{2x}$, **(b)** $e^{-5x}$, **(c)** $x\,e^{3x}$ (product rule needed), **(d)** $\dfrac{e^{2x}}{x}$ (quotient rule needed).

**Solution:**

**(a)** $y = e^{2x}$. Here $f(x) = 2x$, $f'(x) = 2$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = 2e^{2x} \quad\checkmark$$

**(b)** $y = e^{-5x}$. Here $f(x) = -5x$, $f'(x) = -5$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = -5e^{-5x} \quad\checkmark$$

**(c)** $y = x\,e^{3x} = x\cdot e^{3x}$. Use the product rule with $u = x$, $v = e^{3x}$:

$$u = x, \quad \frac{\mathrm{d}u}{\mathrm{d}x} = 1$$

$$v = e^{3x}, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = 3e^{3x}$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = u\frac{\mathrm{d}v}{\mathrm{d}x} + v\frac{\mathrm{d}u}{\mathrm{d}x}$$

$$= x\cdot 3e^{3x} + e^{3x}\cdot 1$$

$$= 3xe^{3x} + e^{3x}$$

$$= e^{3x}(3x+1) \quad\checkmark$$

**(d)** $y = \dfrac{e^{2x}}{x}$. Use the quotient rule with $u = e^{2x}$, $v = x$:

$$u = e^{2x}, \quad \frac{\mathrm{d}u}{\mathrm{d}x} = 2e^{2x}$$

$$v = x, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = 1$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{v\,u' - u\,v'}{v^{2}}$$

$$= \frac{x\cdot 2e^{2x} - e^{2x}\cdot 1}{x^{2}}$$

$$= \frac{2xe^{2x} - e^{2x}}{x^{2}}$$

$$= \frac{e^{2x}(2x-1)}{x^{2}} \quad\checkmark$$

**What the examiner wants:** the chain-rule factor ($2$, $-5$, $3$) present every time; combined rules (product/quotient + exponential) handled without dropping terms.

### Example 10 - Medium - stationary points of an exponential curve (coursebook Worked example 4.6)

> **Question:** The equation of a curve is $y = e^{2x} - 9e^{x} + 7$. Find the exact value of the $x$-coordinate at each stationary point and determine the nature of each stationary point.

**Solution:**

$$y = e^{2x} - 9e^{x} + 7$$

Differentiate term by term:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = 2e^{2x} - 9e^{x}$$

$$\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}} = 4e^{2x} - 9e^{x}$$

Stationary points occur when $\frac{\mathrm{d}y}{\mathrm{d}x} = 0$:

$$2e^{2x} - 9e^{x} = 0$$

Factor out $e^{x}$ (note $e^{x} > 0$ always, so $e^{x} \neq 0$):

$$e^{x}\big(2e^{x} - 9\big) = 0$$

$$2e^{x} - 9 = 0$$

$$2e^{x} = 9$$

$$e^{x} = \frac{9}{2}$$

$$x = \ln\!\left(\frac{9}{2}\right) \quad\checkmark$$

So there is one stationary point at $x = \ln\frac{9}{2}$.

Determine its nature using the second derivative at that point. When $e^{x} = \frac{9}{2}$:

$$\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}} = 4e^{2x} - 9e^{x}$$

$$= 4\left(\frac{9}{2}\right)^{2} - 9\left(\frac{9}{2}\right)$$

$$= 4\cdot\frac{81}{4} - \frac{81}{2}$$

$$= 81 - \frac{81}{2}$$

$$= \frac{81}{2} > 0$$

Since $\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}} > 0$, the stationary point is a **minimum**. $\checkmark$

The $y$-coordinate (if needed):

$$y = e^{2x} - 9e^{x} + 7 = \left(\frac{9}{2}\right)^{2} - 9\left(\frac{9}{2}\right) + 7$$

$$= \frac{81}{4} - \frac{81}{2} + 7$$

$$= -\frac{81}{4} + 7$$

$$= -\frac{81}{4} + \frac{28}{4}$$

$$= -\frac{53}{4}$$

So the minimum point is $\left(\ln\frac{9}{2},\, -\frac{53}{4}\right)$. $\checkmark$

**What the examiner wants:** factorising $e^{x}$ correctly (not dividing by zero); exact $\ln$ form for $x$; second derivative test with correct sign.

### Example 11 - Medium - differentiating $a^{x}$

> **Question:** Differentiate with respect to $x$: **(a)** $2^{x}$, **(b)** $5^{3x+1}$.

**Solution:**

**(a)** $y = 2^{x} = e^{x\ln 2}$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = 2^{x}\ln 2 \quad\checkmark$$

**(b)** $y = 5^{3x+1}$. Write $y = e^{(3x+1)\ln 5}$, so $f(x) = (3x+1)\ln 5$, $f'(x) = 3\ln 5$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = 3\ln 5 \cdot e^{(3x+1)\ln 5}$$

$$= 3\ln 5 \cdot 5^{3x+1} \quad\checkmark$$

Alternatively, directly: $\frac{\mathrm{d}}{\mathrm{d}x}(a^{f(x)}) = f'(x)\,a^{f(x)}\ln a$, so with $a=5$, $f(x)=3x+1$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = 3\cdot 5^{3x+1}\ln 5 \quad\checkmark$$

**What the examiner wants:** the $\ln a$ factor present; correct chain rule on the exponent.

---

## 4.4 Derivatives of Natural Logarithmic Functions

### The basic result

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(\ln x\big) = \frac{1}{x}, \qquad x > 0$$

### The chain-rule extensions

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(\ln(ax+b)\big) = \frac{a}{ax+b}, \qquad ax+b > 0$$

More generally, for any differentiable $f(x) > 0$:

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(\ln f(x)\big) = \frac{f'(x)}{f(x)}$$

This is one of the most used results in the chapter — it appears in almost every implicit/parametric question involving logs.

> ⭐ **Watch Out!** (1) $\ln x$ differentiates to $\frac{1}{x}$, not to $\ln x$ or $\frac{1}{x\ln x}$. (2) For $\ln(ax+b)$, the result is $\frac{a}{ax+b}$ — the $a$ goes on TOP. Forgetting it (writing $\frac{1}{ax+b}$) loses the mark. (3) Domain: $\ln x$ is only defined for $x > 0$; the derivative formula is valid only where the argument is positive. (4) Before differentiating logs with products/quotients/powers inside, consider using log laws to split them — e.g. $\ln(x^{2}e^{x}) = 2\ln x + x$ is much easier to differentiate.

*Derivation (coursebook p.91):* if $y = \ln x$ then $e^{y} = x$. Differentiate both sides with respect to $y$: $e^{y}\frac{\mathrm{d}y}{\mathrm{d}x}$... or more directly, $x = e^{y}$ gives $\frac{\mathrm{d}x}{\mathrm{d}y} = e^{y} = x$, so $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{1}{x}$.

### Example 12 - Easy - differentiating $\ln(ax+b)$ (coursebook Worked example 4.7)

> **Question:** Differentiate with respect to $x$: **(a)** $\ln 2x$, **(b)** $\ln(4x-3)$, **(c)** $\ln(5-x)$.

**Solution:**

Use $\frac{\mathrm{d}}{\mathrm{d}x}\ln(ax+b) = \frac{a}{ax+b}$.

**(a)** $y = \ln 2x = \ln(2x)$. Here $a = 2$, $b = 0$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{2}{2x}$$

$$= \frac{1}{x} \quad\checkmark$$

Note: $\ln 2x = \ln 2 + \ln x$, so $\frac{\mathrm{d}}{\mathrm{d}x}(\ln 2 + \ln x) = 0 + \frac{1}{x} = \frac{1}{x}$ — same result.

**(b)** $y = \ln(4x-3)$. Here $a = 4$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{4}{4x-3} \quad\checkmark$$

**(c)** $y = \ln(5-x)$. Here $a = -1$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{-1}{5-x}$$

$$= -\frac{1}{5-x}$$

$$= \frac{1}{x-5} \quad\checkmark$$

**What the examiner wants:** the $a$ in the numerator; correct sign when $a$ is negative.

### Example 13 - Medium - differentiating $\ln f(x)$ with product/chain (coursebook Worked example 4.8)

> **Question:** Differentiate with respect to $x$: **(a)** $\ln(x^{2}+1)$, **(b)** $x\ln x$, **(c)** $\dfrac{\ln x}{x}$.

**Solution:**

**(a)** $y = \ln(x^{2}+1)$. Here $f(x) = x^{2}+1$, $f'(x) = 2x$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{f'(x)}{f(x)}$$

$$= \frac{2x}{x^{2}+1} \quad\checkmark$$

**(b)** $y = x\ln x$. Use the product rule with $u = x$, $v = \ln x$:

$$u = x, \quad \frac{\mathrm{d}u}{\mathrm{d}x} = 1$$

$$v = \ln x, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = \frac{1}{x}$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = u\frac{\mathrm{d}v}{\mathrm{d}x} + v\frac{\mathrm{d}u}{\mathrm{d}x}$$

$$= x\cdot\frac{1}{x} + \ln x \cdot 1$$

$$= 1 + \ln x \quad\checkmark$$

**(c)** $y = \dfrac{\ln x}{x}$. Use the quotient rule with $u = \ln x$, $v = x$:

$$u = \ln x, \quad \frac{\mathrm{d}u}{\mathrm{d}x} = \frac{1}{x}$$

$$v = x, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = 1$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{v\,u' - u\,v'}{v^{2}}$$

$$= \frac{x\cdot \frac{1}{x} - \ln x \cdot 1}{x^{2}}$$

$$= \frac{1 - \ln x}{x^{2}} \quad\checkmark$$

**What the examiner wants:** correct identification of product vs quotient vs chain-rule-only; no missing terms.

### Example 14 - Hard - log laws before differentiating

> **Question:** Differentiate $y = \ln\!\left(\frac{(x+1)^{3}}{x^{2}}\right)$ with respect to $x$ (for $x > 0$).

**Solution:**

First simplify using log laws:

$$y = \ln\!\left(\frac{(x+1)^{3}}{x^{2}}\right)$$

$$= \ln(x+1)^{3} - \ln x^{2}$$

$$= 3\ln(x+1) - 2\ln x$$

Now differentiate term by term:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = 3\cdot\frac{1}{x+1} - 2\cdot\frac{1}{x}$$

$$= \frac{3}{x+1} - \frac{2}{x}$$

Put over a common denominator if required:

$$= \frac{3x - 2(x+1)}{x(x+1)}$$

$$= \frac{3x - 2x - 2}{x(x+1)}$$

$$= \frac{x - 2}{x(x+1)} \quad\checkmark$$

Direct chain-rule method (without splitting) gives the same answer:

$$y = \ln f(x), \quad f(x) = \frac{(x+1)^{3}}{x^{2}}, \quad \frac{\mathrm{d}y}{\mathrm{d}x} = \frac{f'(x)}{f(x)}$$

— but requires the quotient rule for $f'(x)$ and is far more error-prone. **Splitting first is strongly recommended.**

**What the examiner wants:** log laws used to simplify before differentiating; each $\ln$ term differentiated correctly with its chain-rule factor.

### Example 15 - Hard - stationary point of $\frac{\ln x}{x}$ (coursebook Exercise 4D Q8 style)

> **Question:** The equation of a curve is $y = \dfrac{\ln x}{x}$ for $x > 0$. Find the exact coordinates of the stationary point and determine its nature.

**Solution:**

From Example 13(c):

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{1 - \ln x}{x^{2}}$$

Stationary point when $\frac{\mathrm{d}y}{\mathrm{d}x} = 0$:

$$\frac{1 - \ln x}{x^{2}} = 0$$

$$1 - \ln x = 0$$

$$\ln x = 1$$

$$x = e$$

The $y$-coordinate:

$$y = \frac{\ln e}{e} = \frac{1}{e}$$

So the stationary point is $\left(e,\, \frac{1}{e}\right)$.

Nature: use the second derivative or test either side. Compute $\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}$ via quotient rule on $\frac{1-\ln x}{x^{2}}$:

Let $u = 1 - \ln x$, $v = x^{2}$:

$$u' = -\frac{1}{x}, \quad v' = 2x$$

$$\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}} = \frac{x^{2}\!\left(-\frac{1}{x}\right) - (1-\ln x)(2x)}{x^{4}}$$

$$= \frac{-x - 2x(1-\ln x)}{x^{4}}$$

$$= \frac{-x - 2x + 2x\ln x}{x^{4}}$$

$$= \frac{-3x + 2x\ln x}{x^{4}}$$

$$= \frac{-3 + 2\ln x}{x^{3}}$$

At $x = e$:

$$\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}\bigg|_{x=e} = \frac{-3 + 2(1)}{e^{3}}$$

$$= \frac{-1}{e^{3}} < 0$$

Since $\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}} < 0$, the stationary point is a **maximum**. $\checkmark$

**What the examiner wants:** exact $x = e$ (not a decimal); second derivative test or gradient-sign test to classify.

---

## 4.5 Derivatives of Trigonometric Functions

### The three basic results (radians only!)

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(\sin x\big) = \cos x$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(\cos x\big) = -\sin x$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(\tan x\big) = \sec^{2}x = 1 + \tan^{2}x$$

### Chain-rule extensions for $ax+b$

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(\sin(ax+b)\big) = a\cos(ax+b)$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(\cos(ax+b)\big) = -a\sin(ax+b)$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(\tan(ax+b)\big) = a\sec^{2}(ax+b)$$

### Extension: $\sec$, $\operatorname{cosec}$, $\cot$ (used in Chapter 3 context)

These follow from the quotient rule:

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(\sec x\big) = \sec x\tan x$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(\operatorname{cosec} x\big) = -\operatorname{cosec} x\cot x$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(\cot x\big) = -\operatorname{cosec}^{2}x$$

> ⭐ **Watch Out!** (1) ALL trig differentiation requires **radians** — if your calculator is in degree mode, every derivative is wrong by a factor of $\frac{\pi}{180}$. (2) The minus sign on $\frac{\mathrm{d}}{\mathrm{d}x}(\cos x) = -\sin x$ is essential — it is the single most dropped sign in the paper. (3) For $\tan x$, remember $\sec^{2}x$, not $\sec x\tan x$ (that is the derivative of $\sec x$). (4) Chain-rule factor $a$: $\frac{\mathrm{d}}{\mathrm{d}x}\sin(3x) = 3\cos(3x)$, not $\cos(3x)$.

### Example 16 - Easy - basic trig derivatives (coursebook Worked example 4.9 style)

> **Question:** Differentiate with respect to $x$: **(a)** $2\sin x$, **(b)** $x\cos x$, **(c)** $\tan^{2}x$.

**Solution:**

**(a)** $y = 2\sin x$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = 2\cos x \quad\checkmark$$

**(b)** $y = x\cos x$. Product rule with $u = x$, $v = \cos x$:

$$u = x, \quad \frac{\mathrm{d}u}{\mathrm{d}x} = 1$$

$$v = \cos x, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = -\sin x$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = u\frac{\mathrm{d}v}{\mathrm{d}x} + v\frac{\mathrm{d}u}{\mathrm{d}x}$$

$$= x(-\sin x) + \cos x \cdot 1$$

$$= \cos x - x\sin x \quad\checkmark$$

**(c)** $y = \tan^{2}x = (\tan x)^{2}$. Chain rule with outer $w^{2}$ and inner $\tan x$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = 2\tan x \cdot \sec^{2}x$$

$$= 2\tan x\,\sec^{2}x \quad\checkmark$$

**What the examiner wants:** the minus sign on $\cos \to -\sin$; product/chain rules combined correctly.

### Example 17 - Medium - trig with linear argument (coursebook Worked example 4.10 style)

> **Question:** Differentiate with respect to $x$: **(a)** $\sin 3x$, **(b)** $4\tan 2x$, **(c)** $\dfrac{\cos\!\left(2x - \frac{\pi}{4}\right)}{x}$, **(d)** $(3-2\cos 5x)^{4}$.

**Solution:**

**(a)** $y = \sin 3x$. Here $f(x) = 3x$, $f' = 3$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = 3\cos 3x \quad\checkmark$$

**(b)** $y = 4\tan 2x$. Here the argument is $2x$, factor $2$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = 4\cdot 2\sec^{2}2x$$

$$= 8\sec^{2}2x \quad\checkmark$$

**(c)** $y = \dfrac{\cos\!\left(2x - \frac{\pi}{4}\right)}{x}$. Quotient rule with $u = \cos\!\left(2x-\frac{\pi}{4}\right)$, $v = x$:

$$u = \cos\!\left(2x-\frac{\pi}{4}\right), \quad \frac{\mathrm{d}u}{\mathrm{d}x} = -2\sin\!\left(2x-\frac{\pi}{4}\right)$$

$$v = x, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = 1$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{v\,u' - u\,v'}{v^{2}}$$

$$= \frac{x\cdot\left[-2\sin\!\left(2x-\frac{\pi}{4}\right)\right] - \cos\!\left(2x-\frac{\pi}{4}\right)\cdot 1}{x^{2}}$$

$$= \frac{-2x\sin\!\left(2x-\frac{\pi}{4}\right) - \cos\!\left(2x-\frac{\pi}{4}\right)}{x^{2}} \quad\checkmark$$

**(d)** $y = (3-2\cos 5x)^{4}$. Chain rule: outer $w^{4}$, inner $3-2\cos 5x$:

Inner derivative:

$$\frac{\mathrm{d}}{\mathrm{d}x}(3-2\cos 5x) = -2\cdot 5\sin 5x\text{ with sign? }$$

Actually $\frac{\mathrm{d}}{\mathrm{d}x}(\cos 5x) = -5\sin 5x$, so:

$$\frac{\mathrm{d}}{\mathrm{d}x}(-2\cos 5x) = -2(-5\sin 5x) = 10\sin 5x$$

Therefore:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = 4(3-2\cos 5x)^{3}\cdot 10\sin 5x$$

$$= 40\sin 5x\,(3-2\cos 5x)^{3} \quad\checkmark$$

**What the examiner wants:** chain-rule factor $a$ every time; quotient rule minus sign; careful sign handling with $\cos \to -\sin$.

### Example 18 - Medium - proving $\frac{\mathrm{d}}{\mathrm{d}x}(\tan x) = \sec^{2}x$ and extensions

> **Question:** **(a)** Prove that $\frac{\mathrm{d}}{\mathrm{d}x}(\tan x) = \sec^{2}x$. **(b)** Hence find $\frac{\mathrm{d}}{\mathrm{d}x}(\sec x)$.

**Solution:**

**(a)** Write $\tan x = \dfrac{\sin x}{\cos x}$. Use the quotient rule with $u = \sin x$, $v = \cos x$:

$$u = \sin x, \quad \frac{\mathrm{d}u}{\mathrm{d}x} = \cos x$$

$$v = \cos x, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = -\sin x$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(\tan x) = \frac{v\,u' - u\,v'}{v^{2}}$$

$$= \frac{\cos x\cdot\cos x - \sin x\cdot(-\sin x)}{\cos^{2}x}$$

$$= \frac{\cos^{2}x + \sin^{2}x}{\cos^{2}x}$$

$$= \frac{1}{\cos^{2}x}$$

$$= \sec^{2}x \quad\checkmark$$

Since $\sec^{2}x = 1 + \tan^{2}x$, this can also be written as $1+\tan^{2}x$.

**(b)** Write $\sec x = \dfrac{1}{\cos x} = (\cos x)^{-1}$. Use the chain rule or quotient rule. Using the chain rule:

$$y = (\cos x)^{-1}$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = -1\cdot(\cos x)^{-2}\cdot(-\sin x)$$

$$= \frac{\sin x}{\cos^{2}x}$$

$$= \frac{1}{\cos x}\cdot\frac{\sin x}{\cos x}$$

$$= \sec x\tan x \quad\checkmark$$

**What the examiner wants:** quotient rule applied to $\frac{\sin x}{\cos x}$; identity $\sin^{2}+\cos^{2}=1$ used; final answer in $\sec$ form.

### Example 19 - Hard - products and quotients of mixed trig/exp

> **Question:** Differentiate with respect to $x$: **(a)** $e^{x}\sin x$, **(b)** $\dfrac{\sin x}{\cos x + \sin x}$.

**Solution:**

**(a)** $y = e^{x}\sin x$. Product rule with $u = e^{x}$, $v = \sin x$:

$$u = e^{x}, \quad \frac{\mathrm{d}u}{\mathrm{d}x} = e^{x}$$

$$v = \sin x, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = \cos x$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = u\frac{\mathrm{d}v}{\mathrm{d}x} + v\frac{\mathrm{d}u}{\mathrm{d}x}$$

$$= e^{x}\cos x + \sin x\cdot e^{x}$$

$$= e^{x}(\cos x + \sin x) \quad\checkmark$$

**(b)** $y = \dfrac{\sin x}{\cos x + \sin x}$. Quotient rule with $u = \sin x$, $v = \cos x + \sin x$:

$$u = \sin x, \quad \frac{\mathrm{d}u}{\mathrm{d}x} = \cos x$$

$$v = \cos x + \sin x, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = -\sin x + \cos x$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{v\,u' - u\,v'}{v^{2}}$$

$$= \frac{(\cos x + \sin x)\cos x - \sin x(-\sin x + \cos x)}{(\cos x + \sin x)^{2}}$$

Expand numerator:

$$(\cos x + \sin x)\cos x = \cos^{2}x + \sin x\cos x$$

$$\sin x(-\sin x + \cos x) = -\sin^{2}x + \sin x\cos x$$

So:

$$v\,u' - u\,v' = \cos^{2}x + \sin x\cos x - \big(-\sin^{2}x + \sin x\cos x\big)$$

$$= \cos^{2}x + \sin x\cos x + \sin^{2}x - \sin x\cos x$$

$$= \cos^{2}x + \sin^{2}x$$

$$= 1$$

Therefore:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{1}{(\cos x + \sin x)^{2}} \quad\checkmark$$

**What the examiner wants:** product and quotient rules with trig derivatives correct; numerator simplification using $\cos^{2}+\sin^{2}=1$.

---

## 4.6 Implicit Differentiation

When $y$ is not given explicitly as $y = f(x)$ but instead by an equation like $x^{2}+y^{2}=25$ or $xy + y^{2}=4$, we differentiate **every term** with respect to $x$, treating $y$ as a function of $x$.

**Key rules for implicit differentiation:**

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(y^{n}\big) = n\,y^{\,n-1}\frac{\mathrm{d}y}{\mathrm{d}x}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(x\,y\big) = x\frac{\mathrm{d}y}{\mathrm{d}x} + y \quad\text{(product rule)}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(f(y)\big) = f'(y)\,\frac{\mathrm{d}y}{\mathrm{d}x} \quad\text{(chain rule)}$$

After differentiating, collect all $\frac{\mathrm{d}y}{\mathrm{d}x}$ terms on one side and factorise to solve for $\frac{\mathrm{d}y}{\mathrm{d}x}$.

> ⭐ **Watch Out!** (1) Every $y$-term produces a $\frac{\mathrm{d}y}{\mathrm{d}x}$ factor — forgetting it is the most common error. (2) Terms involving BOTH $x$ and $y$ (like $xy$, $x^{2}y$, $e^{xy}$) need the product rule (and sometimes chain rule) with the $\frac{\mathrm{d}y}{\mathrm{d}x}$ included. (3) After finding $\frac{\mathrm{d}y}{\mathrm{d}x}$, substitute the point coordinates carefully — $x$ and $y$ values both matter. (4) For tangents/normals: gradient of tangent $= \frac{\mathrm{d}y}{\mathrm{d}x}$ at the point; gradient of normal $= -\frac{1}{\mathrm{d}y/\mathrm{d}x}$.

### Example 20 - Easy - basic implicit differentiation

> **Question:** Find $\frac{\mathrm{d}y}{\mathrm{d}x}$ if $x^{2} + y^{2} = 25$.

**Solution:**

Differentiate every term with respect to $x$:

$$\frac{\mathrm{d}}{\mathrm{d}x}(x^{2}) = 2x$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(y^{2}) = 2y\frac{\mathrm{d}y}{\mathrm{d}x}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(25) = 0$$

So:

$$2x + 2y\frac{\mathrm{d}y}{\mathrm{d}x} = 0$$

Solve for $\frac{\mathrm{d}y}{\mathrm{d}x}$:

$$2y\frac{\mathrm{d}y}{\mathrm{d}x} = -2x$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = -\frac{2x}{2y}$$

$$= -\frac{x}{y} \quad\checkmark$$

At the point $(3,4)$: $\frac{\mathrm{d}y}{\mathrm{d}x} = -\frac{3}{4}$; at $(3,-4)$: $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{3}{4}$.

**What the examiner wants:** the $2y\frac{\mathrm{d}y}{\mathrm{d}x}$ term (chain rule on $y^{2}$); final answer with $\frac{\mathrm{d}y}{\mathrm{d}x}$ isolated.

### Example 21 - Medium - implicit differentiation with $xy$ term (coursebook Worked example 4.12)

> **Question:** Find $\frac{\mathrm{d}y}{\mathrm{d}x}$ for the curve $xy + y^{2} = 4x$. Hence find the gradient at the point $(1, -4)$ — wait, check: if $x=1$, then $y + y^{2} = 4$, so $y^{2}+y-4=0$. Use instead the coursebook example: $x^{2} + 3xy + y^{2} = 4$.

**Solution (coursebook curve $x^{2}+3xy+y^{2}=4$, with a check at a point):**

Differentiate term by term:

$$\frac{\mathrm{d}}{\mathrm{d}x}(x^{2}) = 2x$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(3xy) = 3\left(x\frac{\mathrm{d}y}{\mathrm{d}x} + y\cdot 1\right)$$

$$= 3x\frac{\mathrm{d}y}{\mathrm{d}x} + 3y$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(y^{2}) = 2y\frac{\mathrm{d}y}{\mathrm{d}x}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(4) = 0$$

So:

$$2x + 3x\frac{\mathrm{d}y}{\mathrm{d}x} + 3y + 2y\frac{\mathrm{d}y}{\mathrm{d}x} = 0$$

Collect $\frac{\mathrm{d}y}{\mathrm{d}x}$ terms:

$$\left(3x + 2y\right)\frac{\mathrm{d}y}{\mathrm{d}x} = -2x - 3y$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = -\frac{2x+3y}{3x+2y} \quad\checkmark$$

**Finding the gradient at a specific point:** if the curve passes through $(2,0)$:

$$2x+3y = 4+0 = 4, \quad 3x+2y = 6+0 = 6$$

$$\frac{\mathrm{d}y}{\mathrm{d}x}\bigg|_{(2,0)} = -\frac{4}{6} = -\frac{2}{3} \quad\checkmark$$

**What the examiner wants:** product rule on $xy$ giving TWO terms ($x\frac{\mathrm{d}y}{\mathrm{d}x}+y$); all $\frac{\mathrm{d}y}{\mathrm{d}x}$ collected and factorised.

### Example 22 - Medium - implicit with exponential and log

> **Question:** Find $\frac{\mathrm{d}y}{\mathrm{d}x}$ if $e^{y} + xy = 5$.

**Solution:**

Differentiate with respect to $x$:

$$\frac{\mathrm{d}}{\mathrm{d}x}(e^{y}) = e^{y}\frac{\mathrm{d}y}{\mathrm{d}x}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(xy) = x\frac{\mathrm{d}y}{\mathrm{d}x} + y$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(5) = 0$$

So:

$$e^{y}\frac{\mathrm{d}y}{\mathrm{d}x} + x\frac{\mathrm{d}y}{\mathrm{d}x} + y = 0$$

Factor out $\frac{\mathrm{d}y}{\mathrm{d}x}$:

$$\left(e^{y} + x\right)\frac{\mathrm{d}y}{\mathrm{d}x} = -y$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = -\frac{y}{e^{y}+x} \quad\checkmark$$

**What the examiner wants:** chain rule on $e^{y}$ giving $e^{y}\frac{\mathrm{d}y}{\mathrm{d}x}$; product rule on $xy$; clean isolation of $\frac{\mathrm{d}y}{\mathrm{d}x}$.

### Example 23 - Hard - stationary points of an implicit curve (coursebook Worked example 4.13)

> **Question:** The equation of a curve is $x^{2} + 2y^{2} + 2xy = 6$. Find the coordinates of the two stationary points on the curve (where the tangent is parallel to the $x$-axis).

**Solution:**

**Step 1:** Differentiate implicitly to find $\frac{\mathrm{d}y}{\mathrm{d}x}$.

$$\frac{\mathrm{d}}{\mathrm{d}x}(x^{2}) = 2x$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(2y^{2}) = 4y\frac{\mathrm{d}y}{\mathrm{d}x}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(2xy) = 2\left(x\frac{\mathrm{d}y}{\mathrm{d}x} + y\right) = 2x\frac{\mathrm{d}y}{\mathrm{d}x} + 2y$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(6) = 0$$

So:

$$2x + 4y\frac{\mathrm{d}y}{\mathrm{d}x} + 2x\frac{\mathrm{d}y}{\mathrm{d}x} + 2y = 0$$

Group:

$$\left(4y + 2x\right)\frac{\mathrm{d}y}{\mathrm{d}x} = -2x - 2y$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{-2x-2y}{4y+2x}$$

$$= -\frac{x+y}{2y+x} \quad\checkmark$$

**Step 2:** Stationary points occur when $\frac{\mathrm{d}y}{\mathrm{d}x} = 0$, i.e. the numerator is zero (and denominator non-zero):

$$-(x+y) = 0$$

$$x + y = 0$$

$$y = -x$$

**Step 3:** Substitute $y = -x$ into the original curve equation:

$$x^{2} + 2(-x)^{2} + 2x(-x) = 6$$

$$x^{2} + 2x^{2} - 2x^{2} = 6$$

$$x^{2} = 6$$

$$x = \pm\sqrt{6}$$

So with $y = -x$:

$$x = \sqrt{6} \implies y = -\sqrt{6}$$

$$x = -\sqrt{6} \implies y = \sqrt{6}$$

The two stationary points are:

$$\left(\sqrt{6},\, -\sqrt{6}\right) \text{ and } \left(-\sqrt{6},\, \sqrt{6}\right) \quad\checkmark$$

Check denominator non-zero: at $(\sqrt{6},-\sqrt{6})$, $2y+x = -2\sqrt{6}+\sqrt{6} = -\sqrt{6} \neq 0$ ✓; similarly for the other point.

**What the examiner wants:** setting the numerator of $\frac{\mathrm{d}y}{\mathrm{d}x}$ to zero (not the denominator); substituting back into the ORIGINAL equation to find coordinates; both points found.

### Example 24 - Hard - tangent parallel to $y$-axis (vertical tangent)

> **Question:** The equation of a curve is $x^{2} + 3xy + y^{2} = 4$. Find the points where the tangent is parallel to the $y$-axis (i.e. where $\frac{\mathrm{d}y}{\mathrm{d}x}$ is undefined / infinite).

**Solution:**

From Example 21:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = -\frac{2x+3y}{3x+2y}$$

A vertical tangent occurs when the denominator is zero (and numerator non-zero), i.e.:

$$3x + 2y = 0$$

$$y = -\frac{3x}{2}$$

Substitute into the curve equation:

$$x^{2} + 3x\left(-\frac{3x}{2}\right) + \left(-\frac{3x}{2}\right)^{2} = 4$$

$$x^{2} - \frac{9x^{2}}{2} + \frac{9x^{2}}{4} = 4$$

Put over denominator $4$:

$$\frac{4x^{2} - 18x^{2} + 9x^{2}}{4} = 4$$

$$\frac{-5x^{2}}{4} = 4$$

$$-5x^{2} = 16$$

This has no real solution for this particular curve — meaning this curve has no vertical tangents. For a curve where it does exist, you would solve and obtain real $x$, then find $y = -\frac{3x}{2}$.

*For a curve that does have vertical tangents, e.g. $x^{2}+2y^{2}+2xy=6$ from Example 23:*

$$2y + x = 0 \implies x = -2y$$

$$(-2y)^{2} + 2y^{2} + 2(-2y)y = 6$$

$$4y^{2} + 2y^{2} - 4y^{2} = 6$$

$$2y^{2} = 6$$

$$y^{2} = 3$$

$$y = \pm\sqrt{3}, \quad x = \mp 2\sqrt{3}$$

So the vertical-tangent points would be $\left(-2\sqrt{3},\sqrt{3}\right)$ and $\left(2\sqrt{3},-\sqrt{3}\right)$. $\checkmark$

**What the examiner wants:** understanding that horizontal tangent $\iff$ numerator $=0$, vertical tangent $\iff$ denominator $=0$; substitution back into curve equation; awareness that some curves have no such points.

---

## 4.7 Parametric Differentiation

When $x$ and $y$ are both given as functions of a parameter $t$ (or $\theta$):

$$x = f(t), \qquad y = g(t)$$

then by the chain rule:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\displaystyle\frac{\mathrm{d}y}{\mathrm{d}t}}{\displaystyle\frac{\mathrm{d}x}{\mathrm{d}t}} = \frac{\dot{y}}{\dot{x}} \qquad\text{(provided }\frac{\mathrm{d}x}{\mathrm{d}t}\neq 0\text{)}$$

For a parameter $\theta$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\mathrm{d}y/\mathrm{d}\theta}{\mathrm{d}x/\mathrm{d}\theta}$$

The second derivative (if needed) is:

$$\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}} = \frac{\mathrm{d}}{\mathrm{d}x}\!\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right) = \frac{\dfrac{\mathrm{d}}{\mathrm{d}t}\!\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)}{\dfrac{\mathrm{d}x}{\mathrm{d}t}}$$

**Tangents and normals:** evaluate $\frac{\mathrm{d}y}{\mathrm{d}x}$ at the given parameter value $t_{0}$, then use $y - y_{0} = m(x - x_{0})$ with $m = \frac{\mathrm{d}y}{\mathrm{d}x}$ (tangent) or $m = -\frac{1}{\mathrm{d}y/\mathrm{d}x}$ (normal).

> ⭐ **Watch Out!** (1) $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\mathrm{d}y/\mathrm{d}t}{\mathrm{d}x/\mathrm{d}t}$ — it is $y$-derivative over $x$-derivative, not the reverse. (2) Do NOT cancel $t$ — differentiate each of $x(t)$ and $y(t)$ separately with respect to $t$ first, then divide. (3) When finding the tangent/normal, substitute the parameter value into BOTH $x(t)$ and $y(t)$ to get the point $(x_{0},y_{0})$, and into $\frac{\mathrm{d}y}{\mathrm{d}x}$ to get $m$. (4) $\frac{\mathrm{d}x}{\mathrm{d}t}=0$ gives a vertical tangent (if $\frac{\mathrm{d}y}{\mathrm{d}t}\neq 0$); $\frac{\mathrm{d}y}{\mathrm{d}t}=0$ gives a horizontal tangent.

### Example 25 - Easy - basic parametric differentiation (coursebook Worked example 4.14 style)

> **Question:** The parametric equations of a curve are $x = 2t^{2} + 1$, $y = t^{3} - 3t$.
> **(a)** Find $\frac{\mathrm{d}y}{\mathrm{d}x}$ in terms of $t$.
> **(b)** Find the gradient of the curve at the point where $t = 2$.

**Solution:**

**(a)** Differentiate each with respect to $t$:

$$x = 2t^{2} + 1$$

$$\frac{\mathrm{d}x}{\mathrm{d}t} = 4t$$

$$y = t^{3} - 3t$$

$$\frac{\mathrm{d}y}{\mathrm{d}t} = 3t^{2} - 3$$

Now:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\mathrm{d}y/\mathrm{d}t}{\mathrm{d}x/\mathrm{d}t}$$

$$= \frac{3t^{2} - 3}{4t}$$

$$= \frac{3(t^{2}-1)}{4t} \quad\checkmark$$

**(b)** At $t = 2$:

$$\frac{\mathrm{d}y}{\mathrm{d}x}\bigg|_{t=2} = \frac{3(4-1)}{8}$$

$$= \frac{9}{8} \quad\checkmark$$

The point at $t=2$: $x = 2(4)+1 = 9$, $y = 8-6 = 2$, so the curve passes through $(9,2)$ with gradient $\frac{9}{8}$.

**What the examiner wants:** each of $\frac{\mathrm{d}x}{\mathrm{d}t}$ and $\frac{\mathrm{d}y}{\mathrm{d}t}$ found correctly; division in the right order; substitution of $t=2$ into the simplified $\frac{\mathrm{d}y}{\mathrm{d}x}$.

### Example 26 - Medium - tangent and normal to a parametric curve

> **Question:** The parametric equations of a curve are $x = e^{2t}$, $y = e^{t} + 2e^{-t}$. Find the equation of the normal to the curve at the point where $t = 0$.

**Solution:**

**Step 1:** Find $\frac{\mathrm{d}y}{\mathrm{d}x}$.

$$x = e^{2t}$$

$$\frac{\mathrm{d}x}{\mathrm{d}t} = 2e^{2t}$$

$$y = e^{t} + 2e^{-t}$$

$$\frac{\mathrm{d}y}{\mathrm{d}t} = e^{t} - 2e^{-t}$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{e^{t} - 2e^{-t}}{2e^{2t}}$$

**Step 2:** Evaluate at $t = 0$:

At $t = 0$: $e^{0} = 1$, $e^{-0} = 1$, $e^{2\cdot0} = 1$:

$$\frac{\mathrm{d}y}{\mathrm{d}x}\bigg|_{t=0} = \frac{1 - 2}{2\cdot 1}$$

$$= -\frac{1}{2}$$

So the tangent gradient is $-\frac{1}{2}$.

The normal gradient is:

$$m_{\text{normal}} = -\frac{1}{\mathrm{d}y/\mathrm{d}x} = -\frac{1}{-1/2} = 2$$

**Step 3:** Find the point at $t = 0$:

$$x_{0} = e^{0} = 1$$

$$y_{0} = e^{0} + 2e^{0} = 1 + 2 = 3$$

Point is $(1, 3)$.

**Step 4:** Equation of the normal:

$$y - y_{0} = m_{\text{normal}}(x - x_{0})$$

$$y - 3 = 2(x - 1)$$

$$y - 3 = 2x - 2$$

$$y = 2x + 1 \quad\checkmark$$

**What the examiner wants:** $\frac{\mathrm{d}x}{\mathrm{d}t}$ with the $2e^{2t}$ chain-rule factor; correct normal gradient as the negative reciprocal; point $(x_{0},y_{0})$ found from the parametric equations.

### Example 27 - Medium - parametric trig (coursebook Worked example 4.15 style)

> **Question:** The parametric equations of a curve are $x = 1 + 2\sin\theta$, $y = 4\tan\theta$ for $-\frac{\pi}{2} < \theta < \frac{\pi}{2}$.
> **(a)** Find $\frac{\mathrm{d}y}{\mathrm{d}x}$ in terms of $\theta$.
> **(b)** Find the gradient at $\theta = \frac{\pi}{3}$.

**Solution:**

**(a)** Differentiate with respect to $\theta$:

$$x = 1 + 2\sin\theta$$

$$\frac{\mathrm{d}x}{\mathrm{d}\theta} = 2\cos\theta$$

$$y = 4\tan\theta$$

$$\frac{\mathrm{d}y}{\mathrm{d}\theta} = 4\sec^{2}\theta$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\mathrm{d}y/\mathrm{d}\theta}{\mathrm{d}x/\mathrm{d}\theta}$$

$$= \frac{4\sec^{2}\theta}{2\cos\theta}$$

$$= \frac{2\sec^{2}\theta}{\cos\theta}$$

Since $\sec\theta = \frac{1}{\cos\theta}$:

$$= \frac{2}{\cos^{3}\theta}$$

$$= 2\sec^{3}\theta \quad\checkmark$$

**(b)** At $\theta = \frac{\pi}{3}$: $\cos\frac{\pi}{3} = \frac{1}{2}$:

$$\frac{\mathrm{d}y}{\mathrm{d}x}\bigg|_{\theta=\pi/3} = \frac{2}{(1/2)^{3}}$$

$$= \frac{2}{1/8}$$

$$= 16 \quad\checkmark$$

The point at $\theta = \frac{\pi}{3}$: $x = 1+2\cdot\frac{\sqrt{3}}{2} = 1+\sqrt{3}$, $y = 4\sqrt{3}$.

**What the examiner wants:** trig derivatives correct ($\sin\to\cos$, $\tan\to\sec^{2}$); simplification using $\sec = 1/\cos$; evaluation at the given angle in radians.

### Example 28 - Hard - stationary points of a parametric curve

> **Question:** A curve is defined by the parametric equations $x = t^{2}$, $y = t^{3} - 3t^{2}$ for $t \in \mathbb{R}$.
> **(a)** Find $\frac{\mathrm{d}y}{\mathrm{d}x}$ in terms of $t$.
> **(b)** Find the coordinates of the stationary points.

**Solution:**

**(a)**

$$x = t^{2}$$

$$\frac{\mathrm{d}x}{\mathrm{d}t} = 2t$$

$$y = t^{3} - 3t^{2}$$

$$\frac{\mathrm{d}y}{\mathrm{d}t} = 3t^{2} - 6t$$

$$= 3t(t-2)$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{3t^{2}-6t}{2t}$$

$$= \frac{3t(t-2)}{2t}$$

For $t \neq 0$:

$$= \frac{3(t-2)}{2}$$

$$= \frac{3t-6}{2} \quad\checkmark$$

At $t = 0$: $\frac{\mathrm{d}x}{\mathrm{d}t}=0$ and $\frac{\mathrm{d}y}{\mathrm{d}t}=0$, so $\frac{\mathrm{d}y}{\mathrm{d}x}$ is indeterminate — this is a cusp/singular point, not a standard stationary point.

**(b)** Stationary points occur when $\frac{\mathrm{d}y}{\mathrm{d}x} = 0$ (with $\frac{\mathrm{d}x}{\mathrm{d}t}\neq 0$):

$$\frac{3(t-2)}{2} = 0$$

$$t - 2 = 0$$

$$t = 2$$

At $t = 2$:

$$x = (2)^{2} = 4$$

$$y = 8 - 12 = -4$$

So the stationary point is $(4, -4)$. $\checkmark$

Check nature: for $t < 2$ (e.g. $t=1$): $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{-3}{2} < 0$; for $t > 2$ (e.g. $t=3$): $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{3}{2} > 0$. So the gradient goes from negative to positive — this is a **minimum** point.

Note at $t=0$: $(x,y)=(0,0)$ with both derivatives zero — this is a **cusp** (a sharp point where the curve reverses direction), not a stationary point in the usual sense.

**What the examiner wants:** division giving $\frac{3(t-2)}{2}$; identifying $t=2$ as the only stationary parameter; handling the $t=0$ cusp correctly (or noting it is not a standard stationary point).

---

## Practice Questions

Try these without looking at the solutions. They are graded by difficulty and cover every section.

### Q1 - Easy - product rule

Differentiate $y = (x+3)(x^{2}-5)$ with respect to $x$.

### Q2 - Easy - quotient rule

Differentiate $y = \dfrac{3x+1}{x-2}$ with respect to $x$.

### Q3 - Easy - exponential

Differentiate $y = 5e^{4x-1}$ with respect to $x$.

### Q4 - Easy - log

Differentiate $y = \ln(7x+2)$ with respect to $x$.

### Q5 - Easy - trig

Differentiate $y = 3\cos 2x$ with respect to $x$.

### Q6 - Medium - product with exponential and chain

Differentiate $y = (x^{2}+1)e^{2x}$ with respect to $x$. Give your answer in fully factorised form.

### Q7 - Medium - quotient with exponential

Find $\frac{\mathrm{d}y}{\mathrm{d}x}$ when $y = \dfrac{e^{x}}{1+e^{x}}$.

### Q8 - Medium - trig quotient

Differentiate $y = \dfrac{\sin x}{x^{2}}$ with respect to $x$.

### Q9 - Medium - implicit differentiation

The equation of a curve is $x^{2} + y^{2} - 4xy = 12$. Find $\frac{\mathrm{d}y}{\mathrm{d}x}$ in terms of $x$ and $y$.

### Q10 - Medium - parametric: find gradient

The parametric equations of a curve are $x = 3t^{2}$, $y = 2t^{3}$.

**(a)** Find $\frac{\mathrm{d}y}{\mathrm{d}x}$ in terms of $t$.

**(b)** Find the gradient of the curve at the point where $t = 2$.

### Q11 - Medium - implicit: equation of tangent

The equation of a curve is $y^{2} + xy = 6$. The point $(2, 2)$ lies on the curve. Find the equation of the tangent to the curve at $(2, 2)$.

### Q12 - Hard - stationary point of $\frac{\ln x}{x^{2}}$

The equation of a curve is $y = \dfrac{\ln x}{x^{2}}$ for $x > 0$.

**(a)** Find $\frac{\mathrm{d}y}{\mathrm{d}x}$.

**(b)** Find the exact coordinates of the stationary point and determine its nature.

### Q13 - Hard - parametric stationary points

A curve is defined by the parametric equations $x = t^{3} - 3t$, $y = t^{2} + 1$.

Find the coordinates of the stationary points (where $\frac{\mathrm{d}y}{\mathrm{d}x}=0$).

### Q14 - Hard - implicit: tangents parallel to axes

The equation of a curve is $x^{2} + 4y^{2} + 4xy + 2x = 8$.

**(a)** Find $\frac{\mathrm{d}y}{\mathrm{d}x}$ in terms of $x$ and $y$.

**(b)** Find the points where the tangent is parallel to the $x$-axis.

**(c)** Find the points where the tangent is parallel to the $y$-axis.

### Q15 - Hard - mixed: product of trig and exponential

Differentiate $y = e^{-x}\cos 3x$ with respect to $x$. Simplify your answer.

### Q16 - Hard - parametric: equation of normal

The parametric equations of a curve are $x = \ln(t+1)$, $y = t^{2} + t$ for $t > -1$.

**(a)** Find $\frac{\mathrm{d}y}{\mathrm{d}x}$ in terms of $t$.

**(b)** Find the equation of the normal to the curve at the point where $t = 1$.

---

## Solutions to Practice Questions

### Q1

Let $u = x+3$, $v = x^{2}-5$:

$$u = x+3, \quad \frac{\mathrm{d}u}{\mathrm{d}x} = 1$$

$$v = x^{2}-5, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = 2x$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = u\frac{\mathrm{d}v}{\mathrm{d}x} + v\frac{\mathrm{d}u}{\mathrm{d}x}$$

$$= (x+3)(2x) + (x^{2}-5)(1)$$

$$= 2x^{2}+6x + x^{2}-5$$

$$= 3x^{2}+6x-5 \quad\checkmark$$

*Check by expanding first:* $y = x^{3}+3x^{2}-5x-15$, $\frac{\mathrm{d}y}{\mathrm{d}x}=3x^{2}+6x-5$ ✓.

---

### Q2

Let $u = 3x+1$, $v = x-2$:

$$u = 3x+1, \quad \frac{\mathrm{d}u}{\mathrm{d}x} = 3$$

$$v = x-2, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = 1$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{v\,u' - u\,v'}{v^{2}}$$

$$= \frac{(x-2)(3) - (3x+1)(1)}{(x-2)^{2}}$$

$$= \frac{3x-6-3x-1}{(x-2)^{2}}$$

$$= \frac{-7}{(x-2)^{2}} \quad\checkmark$$

---

### Q3

$$y = 5e^{4x-1}$$

$$f(x) = 4x-1, \quad f'(x) = 4$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = 5\cdot 4e^{4x-1}$$

$$= 20e^{4x-1} \quad\checkmark$$

---

### Q4

$$y = \ln(7x+2)$$

$$f(x) = 7x+2, \quad f'(x) = 7$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{7}{7x+2} \quad\checkmark$$

---

### Q5

$$y = 3\cos 2x$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = 3\cdot(-2\sin 2x)$$

$$= -6\sin 2x \quad\checkmark$$

---

### Q6

Let $u = x^{2}+1$, $v = e^{2x}$:

$$u = x^{2}+1, \quad \frac{\mathrm{d}u}{\mathrm{d}x} = 2x$$

$$v = e^{2x}, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = 2e^{2x}$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = u\frac{\mathrm{d}v}{\mathrm{d}x} + v\frac{\mathrm{d}u}{\mathrm{d}x}$$

$$= (x^{2}+1)(2e^{2x}) + e^{2x}(2x)$$

$$= 2e^{2x}(x^{2}+1) + 2xe^{2x}$$

$$= 2e^{2x}\big(x^{2}+1+x\big)$$

$$= 2e^{2x}(x^{2}+x+1) \quad\checkmark$$

---

### Q7

Let $u = e^{x}$, $v = 1+e^{x}$:

$$u = e^{x}, \quad \frac{\mathrm{d}u}{\mathrm{d}x} = e^{x}$$

$$v = 1+e^{x}, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = e^{x}$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{v\,u' - u\,v'}{v^{2}}$$

$$= \frac{(1+e^{x})e^{x} - e^{x}\cdot e^{x}}{(1+e^{x})^{2}}$$

$$= \frac{e^{x}+e^{2x}-e^{2x}}{(1+e^{x})^{2}}$$

$$= \frac{e^{x}}{(1+e^{x})^{2}} \quad\checkmark$$

---

### Q8

Let $u = \sin x$, $v = x^{2}$:

$$u = \sin x, \quad \frac{\mathrm{d}u}{\mathrm{d}x} = \cos x$$

$$v = x^{2}, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = 2x$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{v\,u' - u\,v'}{v^{2}}$$

$$= \frac{x^{2}\cos x - \sin x\cdot 2x}{x^{4}}$$

$$= \frac{x^{2}\cos x - 2x\sin x}{x^{4}}$$

$$= \frac{x\cos x - 2\sin x}{x^{3}} \quad\checkmark$$

---

### Q9

$$x^{2} + y^{2} - 4xy = 12$$

Differentiate with respect to $x$:

$$\frac{\mathrm{d}}{\mathrm{d}x}(x^{2}) = 2x$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(y^{2}) = 2y\frac{\mathrm{d}y}{\mathrm{d}x}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(4xy) = 4\left(x\frac{\mathrm{d}y}{\mathrm{d}x}+y\right) = 4x\frac{\mathrm{d}y}{\mathrm{d}x}+4y$$

So:

$$2x + 2y\frac{\mathrm{d}y}{\mathrm{d}x} - 4x\frac{\mathrm{d}y}{\mathrm{d}x} - 4y = 0$$

Collect $\frac{\mathrm{d}y}{\mathrm{d}x}$:

$$\left(2y - 4x\right)\frac{\mathrm{d}y}{\mathrm{d}x} = 4y - 2x$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{4y-2x}{2y-4x}$$

$$= \frac{2y-x}{y-2x} \quad\checkmark$$

---

### Q10

**(a)**

$$x = 3t^{2}, \quad \frac{\mathrm{d}x}{\mathrm{d}t} = 6t$$

$$y = 2t^{3}, \quad \frac{\mathrm{d}y}{\mathrm{d}t} = 6t^{2}$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{6t^{2}}{6t}$$

$$= t \quad (t\neq 0) \checkmark$$

**(b)** At $t=2$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = 2 \quad\checkmark$$

Point: $x=12$, $y=16$.

---

### Q11

$$y^{2} + xy = 6$$

Differentiate:

$$\frac{\mathrm{d}}{\mathrm{d}x}(y^{2}) = 2y\frac{\mathrm{d}y}{\mathrm{d}x}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(xy) = x\frac{\mathrm{d}y}{\mathrm{d}x}+y$$

So:

$$2y\frac{\mathrm{d}y}{\mathrm{d}x} + x\frac{\mathrm{d}y}{\mathrm{d}x} + y = 0$$

$$\left(2y+x\right)\frac{\mathrm{d}y}{\mathrm{d}x} = -y$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = -\frac{y}{2y+x}$$

At $(2,2)$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = -\frac{2}{4+2}$$

$$= -\frac{2}{6}$$

$$= -\frac{1}{3}$$

Equation of the tangent at $(2,2)$:

$$y - 2 = -\frac{1}{3}(x-2)$$

$$3(y-2) = -(x-2)$$

$$3y-6 = -x+2$$

$$x+3y-8 = 0$$

$$y = -\frac{1}{3}x + \frac{8}{3} \quad\checkmark$$

---

### Q12

**(a)**

$$y = \frac{\ln x}{x^{2}}$$

Let $u = \ln x$, $v = x^{2}$:

$$u' = \frac{1}{x}, \quad v' = 2x$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{v\,u' - u\,v'}{v^{2}}$$

$$= \frac{x^{2}\cdot\frac{1}{x} - \ln x\cdot 2x}{x^{4}}$$

$$= \frac{x - 2x\ln x}{x^{4}}$$

$$= \frac{1-2\ln x}{x^{3}} \quad\checkmark$$

**(b)** Stationary point when $\frac{\mathrm{d}y}{\mathrm{d}x}=0$:

$$1-2\ln x = 0$$

$$2\ln x = 1$$

$$\ln x = \frac{1}{2}$$

$$x = e^{1/2} = \sqrt{e}$$

The $y$-coordinate:

$$y = \frac{\ln(\sqrt{e})}{(\sqrt{e})^{2}}$$

$$= \frac{1/2}{e}$$

$$= \frac{1}{2e}$$

Stationary point: $\left(\sqrt{e},\,\frac{1}{2e}\right)$.

Nature: compute $\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}$ from $\frac{1-2\ln x}{x^{3}}$.

Let $p = 1-2\ln x$, $q = x^{3}$:

$$p' = -\frac{2}{x}, \quad q' = 3x^{2}$$

$$\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}} = \frac{q\,p' - p\,q'}{q^{2}}$$

$$= \frac{x^{3}\!\left(-\frac{2}{x}\right) - (1-2\ln x)(3x^{2})}{x^{6}}$$

$$= \frac{-2x^{2} - 3x^{2}(1-2\ln x)}{x^{6}}$$

$$= \frac{-2x^{2} - 3x^{2} + 6x^{2}\ln x}{x^{6}}$$

$$= \frac{-5x^{2}+6x^{2}\ln x}{x^{6}}$$

$$= \frac{-5+6\ln x}{x^{4}}$$

At $x = \sqrt{e}$: $\ln x = \frac{1}{2}$:

$$\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}} = \frac{-5+6(1/2)}{(\sqrt{e})^{4}}$$

$$= \frac{-5+3}{e^{2}}$$

$$= -\frac{2}{e^{2}} < 0$$

So the stationary point is a **maximum**. $\checkmark$

---

### Q13

$$x = t^{3}-3t, \quad \frac{\mathrm{d}x}{\mathrm{d}t} = 3t^{2}-3 = 3(t^{2}-1)$$

$$y = t^{2}+1, \quad \frac{\mathrm{d}y}{\mathrm{d}t} = 2t$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{2t}{3(t^{2}-1)}$$

Stationary points when $\frac{\mathrm{d}y}{\mathrm{d}x}=0$:

$$2t = 0$$

$$t = 0$$

At $t=0$: $x = 0-0 = 0$, $y = 0+1 = 1$.

Stationary point: $(0, 1)$. $\checkmark$

Note: $\frac{\mathrm{d}y}{\mathrm{d}x}$ is undefined when $3(t^{2}-1)=0$, i.e. $t=\pm1$ — these give vertical tangents, not stationary points.

---

### Q14

$$x^{2}+4y^{2}+4xy+2x = 8$$

**(a)** Differentiate:

$$\frac{\mathrm{d}}{\mathrm{d}x}(x^{2}) = 2x$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(4y^{2}) = 8y\frac{\mathrm{d}y}{\mathrm{d}x}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(4xy) = 4x\frac{\mathrm{d}y}{\mathrm{d}x}+4y$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(2x) = 2$$

So:

$$2x + 8y\frac{\mathrm{d}y}{\mathrm{d}x} + 4x\frac{\mathrm{d}y}{\mathrm{d}x} + 4y + 2 = 0$$

$$\left(8y+4x\right)\frac{\mathrm{d}y}{\mathrm{d}x} = -2x-4y-2$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{-2x-4y-2}{8y+4x}$$

$$= -\frac{x+2y+1}{4y+2x}$$

$$= -\frac{x+2y+1}{2(2y+x)} \quad\checkmark$$

**(b)** Tangent parallel to $x$-axis when $\frac{\mathrm{d}y}{\mathrm{d}x}=0$, i.e. numerator $=0$:

$$x+2y+1 = 0$$

$$x = -2y-1$$

Substitute into the curve:

$$(-2y-1)^{2} + 4y^{2} + 4(-2y-1)y + 2(-2y-1) = 8$$

$$(4y^{2}+4y+1) + 4y^{2} + (-8y^{2}-4y) + (-4y-2) = 8$$

$$4y^{2}+4y+1+4y^{2}-8y^{2}-4y-4y-2 = 8$$

$$-4y -1 = 8$$

$$-4y = 9$$

$$y = -\frac{9}{4}$$

$$x = -2\left(-\frac{9}{4}\right)-1 = \frac{9}{2}-1 = \frac{7}{2}$$

Horizontal-tangent point: $\left(\frac{7}{2},\, -\frac{9}{4}\right)$. $\checkmark$

**(c)** Tangent parallel to $y$-axis when denominator $=0$:

$$8y+4x = 0$$

$$4x = -8y$$

$$x = -2y$$

Substitute:

$$(-2y)^{2}+4y^{2}+4(-2y)y+2(-2y) = 8$$

$$4y^{2}+4y^{2}-8y^{2}-4y = 8$$

$$-4y = 8$$

$$y = -2$$

$$x = -2(-2) = 4$$

Vertical-tangent point: $(4, -2)$. $\checkmark$

---

### Q15

$$y = e^{-x}\cos 3x$$

Let $u = e^{-x}$, $v = \cos 3x$:

$$u = e^{-x}, \quad \frac{\mathrm{d}u}{\mathrm{d}x} = -e^{-x}$$

$$v = \cos 3x, \quad \frac{\mathrm{d}v}{\mathrm{d}x} = -3\sin 3x$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = u\frac{\mathrm{d}v}{\mathrm{d}x} + v\frac{\mathrm{d}u}{\mathrm{d}x}$$

$$= e^{-x}(-3\sin 3x) + \cos 3x(-e^{-x})$$

$$= -3e^{-x}\sin 3x - e^{-x}\cos 3x$$

$$= -e^{-x}(3\sin 3x + \cos 3x) \quad\checkmark$$

---

### Q16

**(a)**

$$x = \ln(t+1), \quad \frac{\mathrm{d}x}{\mathrm{d}t} = \frac{1}{t+1}$$

$$y = t^{2}+t, \quad \frac{\mathrm{d}y}{\mathrm{d}t} = 2t+1$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{2t+1}{\frac{1}{t+1}}$$

$$= (2t+1)(t+1) \quad\checkmark$$

**(b)** At $t=1$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = (3)(2) = 6$$

Normal gradient:

$$m_{\text{normal}} = -\frac{1}{6}$$

Point:

$$x_{0} = \ln 2$$

$$y_{0} = 1+1 = 2$$

Equation of the normal:

$$y - 2 = -\frac{1}{6}(x - \ln 2)$$

$$6(y-2) = -(x-\ln 2)$$

$$6y-12 = -x+\ln 2$$

$$x + 6y - 12 - \ln 2 = 0$$

Or equivalently:

$$y = -\frac{1}{6}x + 2 + \frac{\ln 2}{6} \quad\checkmark$$

---

## Formula Sheet

### Product and Quotient Rules

$$\frac{\mathrm{d}}{\mathrm{d}x}(uv) = u\frac{\mathrm{d}v}{\mathrm{d}x} + v\frac{\mathrm{d}u}{\mathrm{d}x}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\!\left(\frac{u}{v}\right) = \frac{v\,u' - u\,v'}{v^{2}}$$

### Exponential Functions

$$\frac{\mathrm{d}}{\mathrm{d}x}(e^{x}) = e^{x}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(e^{f(x)}\big) = f'(x)\,e^{f(x)}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(e^{ax+b}\big) = a\,e^{ax+b}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(a^{x}) = a^{x}\ln a$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(a^{f(x)}\big) = f'(x)\,a^{f(x)}\ln a$$

### Logarithmic Functions

$$\frac{\mathrm{d}}{\mathrm{d}x}(\ln x) = \frac{1}{x}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(\ln(ax+b)\big) = \frac{a}{ax+b}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(\ln f(x)\big) = \frac{f'(x)}{f(x)}$$

### Trigonometric Functions (radians)

$$\frac{\mathrm{d}}{\mathrm{d}x}(\sin x) = \cos x$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(\cos x) = -\sin x$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(\tan x) = \sec^{2}x$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(\sin(ax+b)\big) = a\cos(ax+b)$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(\cos(ax+b)\big) = -a\sin(ax+b)$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(\tan(ax+b)\big) = a\sec^{2}(ax+b)$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(\sec x) = \sec x\tan x$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(\operatorname{cosec} x) = -\operatorname{cosec} x\cot x$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(\cot x) = -\operatorname{cosec}^{2}x$$

### Implicit Differentiation

$$\frac{\mathrm{d}}{\mathrm{d}x}(y^{n}) = n\,y^{n-1}\frac{\mathrm{d}y}{\mathrm{d}x}$$

$$\frac{\mathrm{d}}{\mathrm{d}x}(xy) = x\frac{\mathrm{d}y}{\mathrm{d}x}+y$$

$$\frac{\mathrm{d}}{\mathrm{d}x}\big(f(y)\big) = f'(y)\frac{\mathrm{d}y}{\mathrm{d}x}$$

### Parametric Differentiation

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\mathrm{d}y/\mathrm{d}t}{\mathrm{d}x/\mathrm{d}t} \qquad \left(\frac{\mathrm{d}x}{\mathrm{d}t}\neq 0\right)$$

$$\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}} = \frac{\dfrac{\mathrm{d}}{\mathrm{d}t}\!\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)}{\dfrac{\mathrm{d}x}{\mathrm{d}t}}$$

---

## Quick Reference Card

| Situation | Rule | Key step |
|---|---|---|
| **Product** $y = uv$ | $y' = uv' + vu'$ | Two terms, chain rule inside each if needed. Factorise at the end. |
| **Quotient** $y = u/v$ | $y' = (vu'-uv')/v^{2}$ | Minus sign! Denominator is $v^{2}$. |
| **$e^{f(x)}$** | $f'(x)e^{f(x)}$ | Chain-rule factor $f'(x)$ in front. |
| **$a^{x}$** | $a^{x}\ln a$ | Extra $\ln a$ vs power rule $ax^{a-1}$. |
| **$\ln f(x)$** | $f'(x)/f(x)$ | Use log laws to split products/quotients first. |
| **$\sin(ax+b)$** | $a\cos(ax+b)$ | Factor $a$; sign flip only on $\cos\to -\sin$. |
| **$\tan x$** | $\sec^{2}x$ | Prove via $\sin/\cos$ quotient rule if asked. |
| **Implicit $F(x,y)=0$** | Differentiate every term; $y$-terms get $\times\frac{\mathrm{d}y}{\mathrm{d}x}$ | Product rule for $xy$ terms. Solve for $\frac{\mathrm{d}y}{\mathrm{d}x}$. |
| **Horizontal tangent** | Numerator of $\frac{\mathrm{d}y}{\mathrm{d}x}=0$ | Substitute $y$ in terms of $x$ back into curve. |
| **Vertical tangent** | Denominator of $\frac{\mathrm{d}y}{\mathrm{d}x}=0$ | Same substitution with denominator condition. |
| **Parametric $x(t),y(t)$** | $\frac{\mathrm{d}y}{\mathrm{d}x}=\frac{\dot y}{\dot x}$ | $\dot y$ over $\dot x$, not reverse. |
| **Parametric tangent/normal** | $m_{\tan}=\frac{\mathrm{d}y}{\mathrm{d}x}$, $m_{\text{norm}}=-\frac{1}{m_{\tan}}$ | Get $(x_{0},y_{0})$ from $t_{0}$; use $y-y_{0}=m(x-x_{0})$. |
| **Radians** | Always | Check calculator mode — degrees invalidates trig derivatives. |

> **Exam tip:** The most common lost marks in Chapter 4 are: (1) forgetting the chain-rule factor $a$ in $e^{ax+b}$, $\ln(ax+b)$, $\sin(ax+b)$; (2) wrong sign on $\cos\to -\sin$ and on the quotient-rule minus; (3) forgetting $\times\frac{\mathrm{d}y}{\mathrm{d}x}$ on every $y$-term in implicit differentiation. Write each derivative on its own line so the examiner can award method marks even if the final answer slips.

