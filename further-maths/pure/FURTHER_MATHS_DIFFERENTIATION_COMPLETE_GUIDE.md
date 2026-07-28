# 📐 FURTHER MATHS DIFFERENTIATION — ULTIMATE STUDY GUIDE

## Cambridge International AS & A Level Further Mathematics (9231) — Paper 2

> **The complete walkthrough:** Every technique explained step-by-step, with dozens of worked examples in proper LaTeX.

---

# 📋 Table of Contents

1. [PART 1: Implicit Differentiation](#part-1-implicit-differentiation)
2. [PART 2: Parametric Differentiation](#part-2-parametric-differentiation)
3. [PART 3: Hyperbolic Functions](#part-3-hyperbolic-functions)
4. [PART 4: Inverse Trigonometric Functions](#part-4-inverse-trigonometric-functions)
5. [PART 5: Inverse Hyperbolic Functions](#part-5-inverse-hyperbolic-functions)
6. [PART 6: Maclaurin Series](#part-6-maclaurin-series)
7. [PART 7: Successive Implicit Differentiation](#part-7-successive-implicit-differentiation)
8. [Formula Sheet](#formula-sheet)
9. [Cambridge Exam Analysis](#cambridge-exam-analysis)
10. [Common Mistakes](#common-mistakes)
11. [Practice Questions & Solutions](#practice-questions--solutions)
12. [Exam Strategy](#exam-strategy)
13. [Quick Reference Card](#quick-reference-card)

---

# How To Use This Guide

Each section follows this structure:

1. **The Rule** — the formula you must know (in LaTeX)
2. **Step-by-Step Method** — a numbered algorithm you can follow
3. **Easy Example** — labelled **Example 1**
4. **Medium Example** — labelled **Example 2**
5. **Hard Example** — labelled **Example 3**
6. **Watch Out!** — common pitfalls

---

# PART 1: Implicit Differentiation

## 1.1 What Is Implicit Differentiation?

An **explicit** function has $y$ written directly in terms of $x$:

$$y = x^2 + 3x$$

An **implicit** function has $x$ and $y$ mixed together:

$$x^2 + y^2 = 2y \quad\text{or}\quad e^x + e^{2y} = \ln y$$

When a function is implicit, you cannot (or should not) rearrange to $y = f(x)$.  
So you differentiate **both sides** with respect to $x$, treating $y$ as $y(x)$.

## 1.2 The Core Rule — Differentiating $y$ Terms

When you differentiate any term involving $y$, multiply by $\frac{dy}{dx}$ (chain rule):

| Term | Differentiates to | Reason |
|---|---|---|
| $y$ | $\displaystyle \frac{dy}{dx}$ | $\frac{d}{dx}(y) = \frac{dy}{dx}$ |
| $y^2$ | $\displaystyle 2y\frac{dy}{dx}$ | $\frac{d}{dx}(y^2) = 2y \cdot \frac{dy}{dx}$ |
| $y^3$ | $\displaystyle 3y^2\frac{dy}{dx}$ | $\frac{d}{dx}(y^3) = 3y^2 \cdot \frac{dy}{dx}$ |
| $y^n$ | $\displaystyle n y^{n-1}\frac{dy}{dx}$ | Power rule + chain rule |
| $\sin y$ | $\displaystyle \cos y \cdot \frac{dy}{dx}$ | Chain rule |
| $e^y$ | $\displaystyle e^y \cdot \frac{dy}{dx}$ | Chain rule |
| $\ln y$ | $\displaystyle \frac{1}{y} \cdot \frac{dy}{dx}$ | Chain rule |

### Quick Check

$$\frac{d}{dx}(y) = 1 \cdot \frac{dy}{dx}\qquad
\frac{d}{dx}(y^5) = 5y^4 \cdot \frac{dy}{dx}$$

$$\frac{d}{dx}(\sqrt{y}) = \frac{1}{2\sqrt{y}} \cdot \frac{dy}{dx}\qquad
\frac{d}{dx}(e^y) = e^y \cdot \frac{dy}{dx}$$

## 1.3 How To Find $\frac{dy}{dx}$ — Step by Step

### The Method

| Step | What To Do |
|---|---|
| **Step 1** | Differentiate **every term** on both sides with respect to $x$ |
| **Step 2** | For $y$-terms: differentiate as normal, then multiply by $\frac{dy}{dx}$ |
| **Step 3** | For products like $x^2 y$: use the **product rule** |
| **Step 4** | Collect all terms with $\frac{dy}{dx}$ on one side |
| **Step 5** | Factor out $\frac{dy}{dx}$ |
| **Step 6** | Divide by the bracket to get $\frac{dy}{dx} = \dots$ |

---

### Example 1 — Easy (just powers)

> **Question:** Find $\frac{dy}{dx}$ for $x^2 + y^2 = 25$

**Solution:**

$$\frac{d}{dx}(x^2) + \frac{d}{dx}(y^2) = \frac{d}{dx}(25)$$

$$2x + 2y\frac{dy}{dx} = 0$$

$$2y\frac{dy}{dx} = -2x$$

$$\frac{dy}{dx} = -\frac{2x}{2y} = -\frac{x}{y} \quad\checkmark$$

---

### Example 2 — Medium (with product)

> **Question:** Find $\frac{dy}{dx}$ for $x^2 y + y^3 = e^x$

**Solution:**

$$\frac{d}{dx}(x^2 y) + \frac{d}{dx}(y^3) = \frac{d}{dx}(e^x)$$

For $x^2 y$, use product rule with $u = x^2$, $v = y$:

$$\frac{d}{dx}(x^2 y) = 2x \cdot y + x^2 \cdot \frac{dy}{dx}$$

Also:

$$\frac{d}{dx}(y^3) = 3y^2 \frac{dy}{dx},\quad \frac{d}{dx}(e^x) = e^x$$

So:

$$2xy + x^2\frac{dy}{dx} + 3y^2\frac{dy}{dx} = e^x$$

$$x^2\frac{dy}{dx} + 3y^2\frac{dy}{dx} = e^x - 2xy$$

$$\frac{dy}{dx}(x^2 + 3y^2) = e^x - 2xy$$

$$\frac{dy}{dx} = \frac{e^x - 2xy}{x^2 + 3y^2} \quad\checkmark$$

---

### Example 3 — Medium with Trig

> **Question:** Find $\frac{dy}{dx}$ for $\sin(x + y) = xy$

**Solution:**

For $\sin(x + y)$, chain rule with inner $u = x + y$:

$$\cos(x + y) \cdot \left(1 + \frac{dy}{dx}\right) = y + x\frac{dy}{dx}$$

Expand:

$$\cos(x+y) + \cos(x+y)\frac{dy}{dx} = y + x\frac{dy}{dx}$$

Collect $\frac{dy}{dx}$ terms:

$$\cos(x+y)\frac{dy}{dx} - x\frac{dy}{dx} = y - \cos(x+y)$$

$$\frac{dy}{dx}(\cos(x+y) - x) = y - \cos(x+y)$$

$$\frac{dy}{dx} = \frac{y - \cos(x+y)}{\cos(x+y) - x} \quad\checkmark$$

---

### Example 4 — Hard (exponential + ln)

> **Question:** Find $\frac{dy}{dx}$ for $e^x + e^{2y} = \ln y$

**Solution:**

$$e^x + 2e^{2y}\frac{dy}{dx} = \frac{1}{y}\frac{dy}{dx}$$

$$2e^{2y}\frac{dy}{dx} - \frac{1}{y}\frac{dy}{dx} = -e^x$$

$$\frac{dy}{dx}\left(2e^{2y} - \frac{1}{y}\right) = -e^x$$

$$\frac{dy}{dx} = \frac{-e^x}{2e^{2y} - \frac{1}{y}}$$

Multiply numerator and denominator by $y$:

$$\frac{dy}{dx} = \frac{-ye^x}{2ye^{2y} - 1} \quad\checkmark$$

---

## 1.4 How To Find $\frac{d^2y}{dx^2}$ — The RIGHT Way ⭐

**This is THE most tested skill. Cambridge asks this in nearly every exam.**

### ❌ The Wrong Approach (what most students do)

Differentiate the **final simplified** $\frac{dy}{dx}$ expression.  
Problem: It's a fraction with $x$ and $y$. You need the quotient rule AND implicit differentiation at the same time. Massive mess.

### ✅ The RIGHT Approach — "Differentiate the First Form"

| Step | What To Do |
|---|---|
| **Step 1** | Find $\frac{dy}{dx}$ and stop at the **first form** (before you moved terms to isolate $\frac{dy}{dx}$) |
| **Step 2** | Differentiate **every term** of this first form with respect to $x$ |
| **Step 3** | When you see $\frac{dy}{dx}$, treat it as a function — its derivative is $\frac{d^2y}{dx^2}$ |
| **Step 4** | Products like $2y \cdot \frac{dy}{dx}$ need the product rule: $\frac{d}{dx}(2y) \cdot \frac{dy}{dx} + 2y \cdot \frac{d}{dx}\left(\frac{dy}{dx}\right)$ |
| **Step 5** | Substitute the expression for $\frac{dy}{dx}$ you found in Step 1 |
| **Step 6** | Solve for $\frac{d^2y}{dx^2}$ and simplify |

---

### Example 1 — Full Walkthrough

> **Question:** Find $\frac{d^2y}{dx^2}$ for $x^2 + y^2 = 2y$

**Phase A — Find the first form of $\frac{dy}{dx}$:**

$$2x + 2y\frac{dy}{dx} = 2\frac{dy}{dx}\quad\text{...STOP! This is the "first form"}$$

We DO NOT rearrange this yet.

**Phase B — Differentiate EVERY term:**

$$\frac{d}{dx}(2x) + \frac{d}{dx}\left(2y\frac{dy}{dx}\right) = \frac{d}{dx}\left(2\frac{dy}{dx}\right)$$

$$2 + \frac{d}{dx}\left(2y\frac{dy}{dx}\right) = 2\frac{d^2y}{dx^2}$$

**Phase C — The product $2y \cdot \frac{dy}{dx}$:**

This is a PRODUCT of two functions of $x$: $u = 2y$ and $v = \frac{dy}{dx}$

$$\frac{d}{dx}\left(2y\frac{dy}{dx}\right) = \left(\frac{d}{dx}(2y)\right)\left(\frac{dy}{dx}\right) + (2y)\left(\frac{d}{dx}\left(\frac{dy}{dx}\right)\right)$$

$$= \left(2\frac{dy}{dx}\right)\left(\frac{dy}{dx}\right) + (2y)\left(\frac{d^2y}{dx^2}\right)$$

$$= 2\left(\frac{dy}{dx}\right)^2 + 2y\frac{d^2y}{dx^2}$$

**Phase D — Put it all together:**

$$2 + 2\left(\frac{dy}{dx}\right)^2 + 2y\frac{d^2y}{dx^2} = 2\frac{d^2y}{dx^2}$$

**Phase E — Rearrange to isolate $\frac{d^2y}{dx^2}$:**

$$2y\frac{d^2y}{dx^2} - 2\frac{d^2y}{dx^2} = -2 - 2\left(\frac{dy}{dx}\right)^2$$

$$\frac{d^2y}{dx^2}(2y - 2) = -2 - 2\left(\frac{dy}{dx}\right)^2$$

$$\frac{d^2y}{dx^2} = \frac{-2 - 2\left(\frac{dy}{dx}\right)^2}{2y - 2}$$

**Phase F — Substitute $\frac{dy}{dx}$:**

From Phase A: $2x + 2y\frac{dy}{dx} = 2\frac{dy}{dx} \;\Rightarrow\; \frac{dy}{dx} = \frac{x}{1-y}$

So:

$$\frac{d^2y}{dx^2} = \frac{-2 - 2\left(\frac{x}{1-y}\right)^2}{2y - 2}$$

$$= \frac{-2 - \frac{2x^2}{(1-y)^2}}{2(y-1)}$$

Multiply numerator and denominator by $(1-y)^2$:

$$\frac{d^2y}{dx^2} = \frac{-2(1-y)^2 - 2x^2}{2(y-1)(1-y)^2}$$

$$= \frac{-2[(1-y)^2 + x^2]}{-2(1-y)^3}$$

$$= \frac{(1-y)^2 + x^2}{(1-y)^3} \quad\checkmark$$

---

### 🎯 Why This Works

The "first form" is usually simpler than the final rearranged $\frac{dy}{dx}$.  
By differentiating it, you **avoid the quotient rule entirely**.

---

### Example 2 — With Exponentials

> **Question:** Find $\frac{d^2y}{dx^2}$ for $e^x + e^{2y} = \ln y$

**Phase A — First form:**

$$e^x + 2e^{2y}\frac{dy}{dx} = \frac{1}{y}\frac{dy}{dx}$$

**Phase B — Differentiate:**

$$\frac{d}{dx}(e^x) + \frac{d}{dx}\left(2e^{2y}\frac{dy}{dx}\right) = \frac{d}{dx}\left(\frac{1}{y}\frac{dy}{dx}\right)$$

**Left product:** $2e^{2y} \cdot \frac{dy}{dx}$

$$u = 2e^{2y} \;\Rightarrow\; \frac{du}{dx} = 4e^{2y}\frac{dy}{dx}$$
$$v = \frac{dy}{dx} \;\Rightarrow\; \frac{dv}{dx} = \frac{d^2y}{dx^2}$$

$$\frac{d}{dx}\left(2e^{2y}\frac{dy}{dx}\right) = \left(4e^{2y}\frac{dy}{dx}\right)\left(\frac{dy}{dx}\right) + \left(2e^{2y}\right)\left(\frac{d^2y}{dx^2}\right)$$

$$= 4e^{2y}\left(\frac{dy}{dx}\right)^2 + 2e^{2y}\frac{d^2y}{dx^2}$$

**Right product:** $\frac{1}{y} \cdot \frac{dy}{dx}$

$$u = \frac{1}{y} = y^{-1} \;\Rightarrow\; \frac{du}{dx} = -y^{-2}\frac{dy}{dx} = -\frac{1}{y^2}\frac{dy}{dx}$$
$$v = \frac{dy}{dx} \;\Rightarrow\; \frac{dv}{dx} = \frac{d^2y}{dx^2}$$

$$\frac{d}{dx}\left(\frac{1}{y}\frac{dy}{dx}\right) = \left(-\frac{1}{y^2}\frac{dy}{dx}\right)\left(\frac{dy}{dx}\right) + \left(\frac{1}{y}\right)\left(\frac{d^2y}{dx^2}\right)$$

$$= -\frac{1}{y^2}\left(\frac{dy}{dx}\right)^2 + \frac{1}{y}\frac{d^2y}{dx^2}$$

**Phase C — Full equation:**

$$e^x + 4e^{2y}\left(\frac{dy}{dx}\right)^2 + 2e^{2y}\frac{d^2y}{dx^2} = -\frac{1}{y^2}\left(\frac{dy}{dx}\right)^2 + \frac{1}{y}\frac{d^2y}{dx^2}$$

Then substitute $\frac{dy}{dx} = \frac{-ye^x}{2ye^{2y} - 1}$ and solve for $\frac{d^2y}{dx^2}$.

---

## 1.5 Finding Numerical Values at a Point

This is **much easier** than finding the general expression.

### The Method

| Step | What To Do |
|---|---|
| **Step 1** | Differentiate once. Write the first form |
| **Step 2** | Substitute the given $(x, y)$ coordinates |
| **Step 3** | Solve for the **number** $\frac{dy}{dx}$ |
| **Step 4** | Differentiate the first form again |
| **Step 5** | Substitute $x$, $y$, **AND** the number $\frac{dy}{dx}$ |
| **Step 6** | Solve for the **number** $\frac{d^2y}{dx^2}$ |

---

### Example 1 — Numerical Values

> **Question:** Given $y^3 + x^3 y = e^x$ passes through $A(0, 1)$, find $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$ at $A$.

**First derivative:**

$$3y^2\frac{dy}{dx} + x^3\frac{dy}{dx} + 3x^2 y = e^x$$

At $(0, 1)$:

$$3(1)^2\frac{dy}{dx} + 0 + 0 = e^0$$

$$3\frac{dy}{dx} = 1 \;\Rightarrow\; \frac{dy}{dx} = \frac{1}{3} \quad\checkmark$$

**Second derivative — differentiate the first form:**

$$\frac{d}{dx}\left(3y^2\frac{dy}{dx}\right) + \frac{d}{dx}\left(x^3\frac{dy}{dx}\right) + \frac{d}{dx}\left(3x^2 y\right) = \frac{d}{dx}(e^x)$$

Term 1: $3y^2\frac{dy}{dx}$ is a product:

$$= 6y\frac{dy}{dx}\cdot\frac{dy}{dx} + 3y^2\frac{d^2y}{dx^2} = 6y\left(\frac{dy}{dx}\right)^2 + 3y^2\frac{d^2y}{dx^2}$$

Term 2: $x^3\frac{dy}{dx}$ is a product:

$$= 3x^2\frac{dy}{dx} + x^3\frac{d^2y}{dx^2}$$

Term 3: $3x^2 y$ is a product:

$$= 6xy + 3x^2\frac{dy}{dx}$$

Term 4: $\frac{d}{dx}(e^x) = e^x$$

Full equation:

$$6y\left(\frac{dy}{dx}\right)^2 + 3y^2\frac{d^2y}{dx^2} + 3x^2\frac{dy}{dx} + x^3\frac{d^2y}{dx^2} + 6xy + 3x^2\frac{dy}{dx} = e^x$$

At $(0, 1)$ with $\frac{dy}{dx} = \frac{1}{3}$:

$$6(1)\left(\frac{1}{9}\right) + 3(1)\frac{d^2y}{dx^2} + 0 + 0 + 0 + 0 = 1$$

$$\frac{6}{9} + 3\frac{d^2y}{dx^2} = 1$$

$$\frac{2}{3} + 3\frac{d^2y}{dx^2} = 1$$

$$3\frac{d^2y}{dx^2} = \frac{1}{3}$$

$$\frac{d^2y}{dx^2} = \frac{1}{9} \quad\checkmark$$

---

### Example 2 — Harder Numerical

> **Question:** An implicit curve $C$ is $y^2 = \ln x + e^y - 1$. Given $C$ passes through $(1, 0)$, find $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$ at this point.

**First derivative:**

$$2y\frac{dy}{dx} = \frac{1}{x} + e^y\frac{dy}{dx}$$

At $(1, 0)$:

$$0 = 1 + 1\cdot\frac{dy}{dx}$$

$$\frac{dy}{dx} = -1 \quad\checkmark$$

**Second derivative — differentiate first form:**

$$\frac{d}{dx}\left(2y\frac{dy}{dx}\right) = \frac{d}{dx}\left(\frac{1}{x}\right) + \frac{d}{dx}\left(e^y\frac{dy}{dx}\right)$$

Left side:

$$2\frac{dy}{dx}\cdot\frac{dy}{dx} + 2y\frac{d^2y}{dx^2} = 2\left(\frac{dy}{dx}\right)^2 + 2y\frac{d^2y}{dx^2}$$

Right side: $\frac{d}{dx}\left(\frac{1}{x}\right) = -\frac{1}{x^2}$

Right side: $e^y\frac{dy}{dx}$ is a product:

$$e^y\frac{dy}{dx}\cdot\frac{dy}{dx} + e^y\frac{d^2y}{dx^2} = e^y\left(\frac{dy}{dx}\right)^2 + e^y\frac{d^2y}{dx^2}$$

Full:

$$2\left(\frac{dy}{dx}\right)^2 + 2y\frac{d^2y}{dx^2} = -\frac{1}{x^2} + e^y\left(\frac{dy}{dx}\right)^2 + e^y\frac{d^2y}{dx^2}$$

At $(1, 0)$ with $\frac{dy}{dx} = -1$:

$$2(1) + 0 = -1 + 1(1) + 1\cdot\frac{d^2y}{dx^2}$$

$$2 = 0 + \frac{d^2y}{dx^2}$$

$$\frac{d^2y}{dx^2} = 2 \quad\checkmark$$

---

## 1.6 The Triple Product Rule

When you differentiate a product of THREE functions of $x$:

$$\frac{d}{dx}(u v w) = vw\frac{du}{dx} + uw\frac{dv}{dx} + uv\frac{dw}{dx}$$

### Where It Appears in Implicit Differentiation

When finding second derivatives, you'll encounter terms like:

$$x^3 \cdot y \cdot \frac{dy}{dx}$$

This is THREE functions of $x$: $u = x^3$, $v = y$, $w = \frac{dy}{dx}$

So:

$$\frac{d}{dx}\left(x^3 y \frac{dy}{dx}\right) = \frac{d(x^3)}{dx} \cdot y \cdot \frac{dy}{dx} + x^3 \cdot \frac{dy}{dx} \cdot \frac{dy}{dx} + x^3 \cdot y \cdot \frac{d^2y}{dx^2}$$

$$= 3x^2 y \frac{dy}{dx} + x^3 \left(\frac{dy}{dx}\right)^2 + x^3 y \frac{d^2y}{dx^2}$$

### Full Example with Triple Product

> **Question:** Given $x^3 y^2 + y = \sin x$, find $\frac{d^2y}{dx^2}$

**First derivative:**

$$3x^2 y^2 + x^3 \cdot 2y \frac{dy}{dx} + \frac{dy}{dx} = \cos x$$

$$3x^2 y^2 + 2x^3 y \frac{dy}{dx} + \frac{dy}{dx} = \cos x \quad\text{...first form}$$

**Second derivative — differentiate:**

$$\frac{d}{dx}(3x^2 y^2) + \frac{d}{dx}\left(2x^3 y \frac{dy}{dx}\right) + \frac{d^2y}{dx^2} = -\sin x$$

Term 1: $3x^2 y^2$ (product of $3x^2$ and $y^2$):

$$= 6x \cdot y^2 + 3x^2 \cdot 2y\frac{dy}{dx} = 6xy^2 + 6x^2 y \frac{dy}{dx}$$

Term 2: $2x^3 y \frac{dy}{dx}$ is a **triple product** ($u = 2x^3$, $v = y$, $w = \frac{dy}{dx}$):

$$= (6x^2)(y)\left(\frac{dy}{dx}\right) + (2x^3)\left(\frac{dy}{dx}\right)\left(\frac{dy}{dx}\right) + (2x^3)(y)\left(\frac{d^2y}{dx^2}\right)$$

$$= 6x^2 y \frac{dy}{dx} + 2x^3 \left(\frac{dy}{dx}\right)^2 + 2x^3 y \frac{d^2y}{dx^2}$$

Full equation:

$$6xy^2 + 6x^2 y \frac{dy}{dx} + 6x^2 y \frac{dy}{dx} + 2x^3 \left(\frac{dy}{dx}\right)^2 + 2x^3 y \frac{d^2y}{dx^2} + \frac{d^2y}{dx^2} = -\sin x$$

Collect $\frac{d^2y}{dx^2}$:

$$\frac{d^2y}{dx^2}(2x^3 y + 1) = -\sin x - 6xy^2 - 12x^2 y \frac{dy}{dx} - 2x^3 \left(\frac{dy}{dx}\right)^2$$

Then substitute $\frac{dy}{dx} = \frac{\cos x - 3x^2 y^2}{2x^3 y + 1}$.

---

## 1.7 Practice Questions — Implicit

### Easy
1. Find $\frac{dy}{dx}$ for $x^3 + y^3 = 6xy$
2. Find $\frac{dy}{dx}$ for $x^2 y = y^2 + x$
3. Find $\frac{dy}{dx}$ for $e^{xy} = x + y$

### Medium
4. Find $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$ for $xy^2 = e^x$
5. Find $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$ for $x^2 + y^2 = \ln(xy)$
6. Find $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$ at $(0, 0)$ for $x^2 = ye^x + y^2$

### Hard
7. Given $x e^{x+y} = (x+1)^2$, find $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$
8. Find $\frac{d^2y}{dx^2}$ for $\sin(xy) = y^2 + x$

---

# PART 2: Parametric Differentiation

## 2.1 What Are Parametric Equations?

Instead of $y = f(x)$, both $x$ and $y$ are written in terms of a third variable $t$ (the **parameter**):

$$x = f(t)$$
$$y = g(t)$$

For example: $x = t^2$, $y = t + 1$

As $t$ varies, the point $(x, y)$ traces out a curve.

## 2.2 Finding $\frac{dy}{dx}$

### The Formula

$$\frac{dy}{dx} = \frac{dy}{dt} \div \frac{dx}{dt} = \frac{\; \displaystyle \frac{dy}{dt} \;}{\; \displaystyle \frac{dx}{dt} \;}$$

### Why?

By the chain rule:

$$\frac{dy}{dt} = \frac{dy}{dx} \times \frac{dx}{dt}$$

Rearranging:

$$\frac{dy}{dx} = \frac{dy}{dt} \Big/ \frac{dx}{dt}$$

### Step-by-Step Method

| Step | What To Do |
|---|---|
| **Step 1** | Find $\frac{dx}{dt}$ (differentiate $x$ with respect to $t$) |
| **Step 2** | Find $\frac{dy}{dt}$ (differentiate $y$ with respect to $t$) |
| **Step 3** | Write $\frac{dy}{dx} = \dfrac{dy/dt}{dx/dt}$ |
| **Step 4** | Simplify if possible |

---

### Example 1 — Easy

> **Question:** $x = t^2$, $y = 3t + 1$. Find $\frac{dy}{dx}$.

$$\frac{dx}{dt} = 2t,\quad \frac{dy}{dt} = 3$$

$$\frac{dy}{dx} = \frac{3}{2t} \quad\checkmark$$

---

### Example 2 — Medium

> **Question:** $x = e^t$, $y = t^2 + t$. Find $\frac{dy}{dx}$.

$$\frac{dx}{dt} = e^t,\quad \frac{dy}{dt} = 2t + 1$$

$$\frac{dy}{dx} = \frac{2t + 1}{e^t} \quad\checkmark$$

---

### Example 3 — With Trig

> **Question:** $x = \sin t$, $y = \cos 2t$. Find $\frac{dy}{dx}$.

$$\frac{dx}{dt} = \cos t,\quad \frac{dy}{dt} = -2\sin 2t$$

$$\frac{dy}{dx} = \frac{-2\sin 2t}{\cos t}$$

Use $\sin 2t = 2\sin t\cos t$:

$$\frac{dy}{dx} = \frac{-2 \cdot 2\sin t\cos t}{\cos t} = -4\sin t \quad\checkmark$$

---

## 2.3 Finding $\frac{d^2y}{dx^2}$ ⭐

### The Formula ⭐

$$\frac{d^2y}{dx^2} = \frac{d}{dt}\left(\frac{dy}{dx}\right) \times \frac{dt}{dx}$$

where $\displaystyle \frac{dt}{dx} = \frac{1}{\; \displaystyle \frac{dx}{dt} \;}$

### Why This Formula?

$\frac{dy}{dx}$ is a function of $t$ (not $x$). To differentiate it with respect to $x$, use the chain rule:

$$\frac{d}{dx}\left(\frac{dy}{dx}\right) = \frac{d}{dt}\left(\frac{dy}{dx}\right) \times \frac{dt}{dx}$$

### Step-by-Step Method

| Step | What To Do |
|---|---|
| **Step 1** | Find $\frac{dy}{dx}$ as a function of $t$ |
| **Step 2** | Differentiate $\frac{dy}{dx}$ with respect to $t$: $\frac{d}{dt}\left(\frac{dy}{dx}\right)$ |
| **Step 3** | Find $\frac{dt}{dx} = \frac{1}{dx/dt}$ |
| **Step 4** | Multiply: $\frac{d^2y}{dx^2} = \frac{d}{dt}\left(\frac{dy}{dx}\right) \times \frac{dt}{dx}$ |
| **Step 5** | Simplify |

---

### Example 1 — Full Walkthrough

> **Question:** $x = t^2$, $y = t + 1$. Find $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$.

$$\frac{dx}{dt} = 2t,\quad \frac{dy}{dt} = 1$$

$$\frac{dy}{dx} = \frac{1}{2t} = \frac{1}{2}t^{-1}$$

$$\frac{d}{dt}\left(\frac{dy}{dx}\right) = \frac{d}{dt}\left(\frac{1}{2}t^{-1}\right) = -\frac{1}{2}t^{-2} = -\frac{1}{2t^2}$$

$$\frac{dt}{dx} = \frac{1}{dx/dt} = \frac{1}{2t}$$

$$\frac{d^2y}{dx^2} = \left(-\frac{1}{2t^2}\right) \times \left(\frac{1}{2t}\right) = -\frac{1}{4t^3} \quad\checkmark$$

---

### Example 2 — With Exponentials

> **Question:** $x = e^t$, $y = t^2$. Find $\frac{d^2y}{dx^2}$.

$$\frac{dx}{dt} = e^t,\quad \frac{dy}{dt} = 2t$$

$$\frac{dy}{dx} = \frac{2t}{e^t} = 2t e^{-t}$$

$$\frac{d}{dt}\left(\frac{dy}{dx}\right) = \frac{d}{dt}\left(2t e^{-t}\right)$$

Product rule: $u = 2t$, $v = e^{-t}$:

$$= 2\cdot e^{-t} + 2t \cdot (-e^{-t}) = 2e^{-t} - 2te^{-t} = 2e^{-t}(1 - t)$$

$$\frac{dt}{dx} = \frac{1}{e^t} = e^{-t}$$

$$\frac{d^2y}{dx^2} = 2e^{-t}(1 - t) \times e^{-t} = 2e^{-2t}(1 - t) \quad\checkmark$$

---

### Example 3 — Rational Functions

> **Question:** $x = t^2 + 1$, $y = \frac{t}{t+1}$. Find $\frac{d^2y}{dx^2}$.

$$\frac{dx}{dt} = 2t$$

For $\frac{dy}{dt}$, use quotient rule on $y = \frac{t}{t+1}$:

$$\frac{dy}{dt} = \frac{(1)(t+1) - t(1)}{(t+1)^2} = \frac{1}{(t+1)^2}$$

$$\frac{dy}{dx} = \frac{1/(t+1)^2}{2t} = \frac{1}{2t(t+1)^2}$$

For $\frac{d}{dt}\left(\frac{dy}{dx}\right)$, rewrite as $\frac{1}{2} t^{-1} (t+1)^{-2}$:

$$= \frac{1}{2}\left[(-1)t^{-2}(t+1)^{-2} + t^{-1}\cdot(-2)(t+1)^{-3}\right]$$

$$= \frac{1}{2}\left[-\frac{1}{t^2(t+1)^2} - \frac{2}{t(t+1)^3}\right]$$

$$\frac{dt}{dx} = \frac{1}{2t}$$

$$\frac{d^2y}{dx^2} = \frac{1}{2}\left[-\frac{1}{t^2(t+1)^2} - \frac{2}{t(t+1)^3}\right] \times \frac{1}{2t}$$

$$= \frac{1}{4}\left[-\frac{1}{t^3(t+1)^2} - \frac{2}{t^2(t+1)^3}\right] \quad\checkmark$$

---

## 2.4 Stationary Points for Parametric Curves

### Rules

**Stationary points** occur when $\frac{dy}{dx} = 0$.  
For parametric equations, this is equivalent to $\frac{dy}{dt} = 0$ (provided $\frac{dx}{dt} \neq 0$).

### Nature of Stationary Points

| $\frac{d^2y}{dx^2}$ | Nature |
|---|---|
| $\frac{d^2y}{dx^2} < 0$ | **Maximum** |
| $\frac{d^2y}{dx^2} > 0$ | **Minimum** |
| $\frac{d^2y}{dx^2} = 0$ | **Point of inflection** (possibly) |

### Step-by-Step Method

| Step | What To Do |
|---|---|
| **Step 1** | Find $\frac{dx}{dt}$ and $\frac{dy}{dt}$ |
| **Step 2** | Set $\frac{dy}{dt} = 0$, solve for $t$ |
| **Step 3** | Check $\frac{dx}{dt} \neq 0$ at these $t$ values (otherwise it's a vertical tangent, not a stationary point) |
| **Step 4** | Find $(x, y)$ coordinates by plugging $t$ into original equations |
| **Step 5** | Find $\frac{d^2y}{dx^2}$ |
| **Step 6** | Evaluate $\frac{d^2y}{dx^2}$ at each $t$ to determine max or min |

---

### Example 1 — Full Walkthrough

> **Question:** A curve is defined by $x = t^2 + t$, $y = t^3 - 3t$. Find stationary points and determine their nature.

**Step 1 — Find $\frac{dx}{dt}$ and $\frac{dy}{dt}$:**

$$\frac{dx}{dt} = 2t + 1,\quad \frac{dy}{dt} = 3t^2 - 3$$

**Step 2 — Set $\frac{dy}{dt} = 0$:**

$$3t^2 - 3 = 0 \;\Rightarrow\; t^2 = 1 \;\Rightarrow\; t = \pm 1$$

**Step 3 — Check $\frac{dx}{dt} \neq 0$:**

At $t = 1$: $\frac{dx}{dt} = 2(1) + 1 = 3 \neq 0 \;\checkmark$  
At $t = -1$: $\frac{dx}{dt} = 2(-1) + 1 = -1 \neq 0 \;\checkmark$

**Step 4 — Find coordinates:**

At $t = 1$: $x = 1^2 + 1 = 2$, $y = 1^3 - 3(1) = -2 \;\Rightarrow\; (2, -2)$  
At $t = -1$: $x = (-1)^2 + (-1) = 0$, $y = (-1)^3 - 3(-1) = 2 \;\Rightarrow\; (0, 2)$

**Step 5 — Find $\frac{d^2y}{dx^2}$:**

$$\frac{dy}{dx} = \frac{3t^2 - 3}{2t + 1}$$

$$\frac{d}{dt}\left(\frac{dy}{dx}\right) = \frac{(6t)(2t+1) - (3t^2-3)(2)}{(2t+1)^2}$$

$$= \frac{12t^2 + 6t - 6t^2 + 6}{(2t+1)^2} = \frac{6t^2 + 6t + 6}{(2t+1)^2} = \frac{6(t^2 + t + 1)}{(2t+1)^2}$$

$$\frac{dt}{dx} = \frac{1}{2t+1}$$

$$\frac{d^2y}{dx^2} = \frac{6(t^2 + t + 1)}{(2t+1)^2} \times \frac{1}{2t+1} = \frac{6(t^2 + t + 1)}{(2t+1)^3}$$

**Step 6 — Determine nature:**

At $t = 1$: $\frac{d^2y}{dx^2} = \frac{6(1+1+1)}{3^3} = \frac{18}{27} = \frac{2}{3} > 0 \;\Rightarrow\; \textbf{MINIMUM at }(2, -2)$

At $t = -1$: $\frac{d^2y}{dx^2} = \frac{6(1-1+1)}{(-1)^3} = \frac{6}{-1} = -6 < 0 \;\Rightarrow\; \textbf{MAXIMUM at }(0, 2)$

---

### Example 2 — Trigonometric Parametric

> **Question:** $x = \cos t$, $y = \sin 2t$ for $0 < t < \pi$. Find stationary points and their nature.

$$\frac{dx}{dt} = -\sin t,\quad \frac{dy}{dt} = 2\cos 2t$$

Stationary: $2\cos 2t = 0 \;\Rightarrow\; \cos 2t = 0 \;\Rightarrow\; 2t = \frac{\pi}{2}, \frac{3\pi}{2}$

$$t = \frac{\pi}{4},\; \frac{3\pi}{4}$$

Check $\frac{dx}{dt} \neq 0$: $\sin t \neq 0$ for these values. $\checkmark$

Coordinates:

At $t = \frac{\pi}{4}$: $x = \frac{\sqrt{2}}{2}$, $y = 1$  
At $t = \frac{3\pi}{4}$: $x = -\frac{\sqrt{2}}{2}$, $y = -1$

$$\frac{dy}{dx} = \frac{2\cos 2t}{-\sin t} = -\frac{2\cos 2t}{\sin t}$$

$$\frac{d^2y}{dx^2} = \frac{d}{dt}\left(\frac{dy}{dx}\right) \times \frac{1}{dx/dt}$$

After calculation (using quotient rule):

At $t = \frac{\pi}{4}$: $\frac{d^2y}{dx^2} = -8 < 0 \;\Rightarrow\; \textbf{MAXIMUM at }\left(\frac{\sqrt{2}}{2}, 1\right)$

At $t = \frac{3\pi}{4}$: $\frac{d^2y}{dx^2} = 8 > 0 \;\Rightarrow\; \textbf{MINIMUM at }\left(-\frac{\sqrt{2}}{2}, -1\right)$

---

## 2.5 Practice Questions — Parametric

### Easy
1. $x = 2t$, $y = t^3$. Find $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$.
2. $x = t - 1$, $y = t^2 + t$. Find $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$.
3. $x = e^{2t}$, $y = e^t$. Find $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$.

### Medium
4. $x = t^2 + 1$, $y = \ln t$. Find $\frac{d^2y}{dx^2}$.
5. $x = 3\cos t$, $y = 3\sin t$. Find $\frac{d^2y}{dx^2}$.
6. $x = t^3$, $y = t^2 - 2t$. Find stationary points and their nature.

### Hard
7. $x = e^t + e^{-t}$, $y = e^t - e^{-t}$. Find $\frac{d^2y}{dx^2}$.
8. $x = \ln(t + 1)$, $y = e^t$. Show $\frac{d^2y}{dx^2}$ is always positive.
9. $x = t^2 + 2t$, $y = t^3 - 12t$. Find and classify all stationary points.

---

# PART 3: Hyperbolic Functions

## 3.1 Definitions

| Function | Definition |
|---|---|
| $\sinh x$ | $\displaystyle \frac{e^x - e^{-x}}{2}$ |
| $\cosh x$ | $\displaystyle \frac{e^x + e^{-x}}{2}$ |
| $\tanh x$ | $\displaystyle \frac{\sinh x}{\cosh x} = \frac{e^x - e^{-x}}{e^x + e^{-x}}$ |
| $\operatorname{sech} x$ | $\displaystyle \frac{1}{\cosh x}$ |
| $\operatorname{cosech} x$ | $\displaystyle \frac{1}{\sinh x}$ |
| $\coth x$ | $\displaystyle \frac{\cosh x}{\sinh x}$ |

## 3.2 Derivatives — Learn These Cold 🥶

| $y$ | $\dfrac{dy}{dx}$ |
|---|---|
| **$\sinh x$** | **$\cosh x$** |
| **$\cosh x$** | **$\sinh x$** |
| **$\tanh x$** | **$\operatorname{sech}^2 x$** |
| $\operatorname{sech} x$ | $-\operatorname{sech} x \tanh x$ |
| $\operatorname{cosech} x$ | $-\operatorname{cosech} x \coth x$ |
| $\coth x$ | $-\operatorname{cosech}^2 x$ |

### ⚠️ Key Difference from Trig

| Trig | Derivative | Hyperbolic | Derivative |
|---|---|---|---|
| $\sin x$ | $\cos x$ | $\sinh x$ | $\cosh x$ |
| $\cos x$ | $-\sin x$ | $\cosh x$ | $+\sinh x$ ← **NO negative!** |
| $\tan x$ | $\sec^2 x$ | $\tanh x$ | $\operatorname{sech}^2 x$ |
| $\sec x$ | $\sec x \tan x$ | $\operatorname{sech} x$ | $-\operatorname{sech} x \tanh x$ |

> **The "#1 trap:** $\frac{d}{dx}(\cosh x) = +\sinh x$ (not $-\sinh x$ like $\cos x$)"

---

## 3.3 Worked Examples

### Example 1 — Chain Rule (Easy)

> **Question:** $y = \sinh 3x$. Find $\frac{dy}{dx}$.

Let $u = 3x$, then $y = \sinh u$:

$$\frac{dy}{dx} = \frac{dy}{du} \times \frac{du}{dx} = \cosh u \times 3 = 3\cosh 3x \quad\checkmark$$

---

### Example 2 — Power of Hyperbolic (Medium)

> **Question:** $y = \sinh^2 x$. Find $\frac{dy}{dx}$.

Option 1: Chain rule

$$y = (\sinh x)^2$$

$$\frac{dy}{dx} = 2\sinh x \times \cosh x = 2\sinh x\cosh x$$

Simplify using $2\sinh A\cosh A = \sinh 2A$:

$$\frac{dy}{dx} = \sinh 2x \quad\checkmark$$

---

### Example 3 — Chain Rule (Medium)

> **Question:** $y = \cosh(x^2 + 1)$. Find $\frac{dy}{dx}$.

Inner: $u = x^2 + 1$

$$\frac{dy}{dx} = \sinh(x^2 + 1) \times 2x = 2x\sinh(x^2 + 1) \quad\checkmark$$

---

### Example 4 — Product Rule (Medium)

> **Question:** $y = x^2 \sinh x$. Find $\frac{dy}{dx}$.

Product rule: $u = x^2$, $v = \sinh x$

$$\frac{dy}{dx} = 2x \cdot \sinh x + x^2 \cdot \cosh x = 2x\sinh x + x^2\cosh x \quad\checkmark$$

---

### Example 5 — Product and Chain (Hard)

> **Question:** $y = \cosh 3x \cdot \sinh 4x$. Find $\frac{dy}{dx}$.

Product rule: $u = \cosh 3x$, $v = \sinh 4x$

$$u' = 3\sinh 3x,\quad v' = 4\cosh 4x$$

$$\frac{dy}{dx} = 3\sinh 3x \cdot \sinh 4x + \cosh 3x \cdot 4\cosh 4x$$

$$= 3\sinh 3x \sinh 4x + 4\cosh 3x \cosh 4x \quad\checkmark$$

---

### Example 6 — Logarithm + Hyperbolic (Hard)

> **Question:** $y = \ln(\cosh x)$. Find $\frac{dy}{dx}$.

$$\frac{dy}{dx} = \frac{1}{\cosh x} \times \sinh x = \frac{\sinh x}{\cosh x} = \tanh x \quad\checkmark$$

---

### Example 7 — Implicit with Hyperbolic (Exam Style)

> **Question:** $\sinh(x + y) = yx^3$. Find $\frac{dy}{dx}$.

$$\cosh(x + y) \cdot \left(1 + \frac{dy}{dx}\right) = y \cdot 3x^2 + x^3 \cdot \frac{dy}{dx}$$

$$\cosh(x+y) + \cosh(x+y)\frac{dy}{dx} = 3x^2 y + x^3\frac{dy}{dx}$$

$$\cosh(x+y)\frac{dy}{dx} - x^3\frac{dy}{dx} = 3x^2 y - \cosh(x+y)$$

$$\frac{dy}{dx}(\cosh(x+y) - x^3) = 3x^2 y - \cosh(x+y)$$

$$\frac{dy}{dx} = \frac{3x^2 y - \cosh(x+y)}{\cosh(x+y) - x^3} \quad\checkmark$$

---

## 3.4 Practice Questions — Hyperbolic

1. $y = \sinh(5x - 2)$. Find $\frac{dy}{dx}$.
2. $y = \tanh(x^2)$. Find $\frac{dy}{dx}$.
3. $y = x \cosh(3x)$. Find $\frac{dy}{dx}$.
4. $y = e^x \tanh x$. Find $\frac{dy}{dx}$.
5. $y = \operatorname{sech}(2x + 1)$. Find $\frac{dy}{dx}$.
6. $y = \ln(\sinh x)$. Find $\frac{dy}{dx}$.
7. $y = \operatorname{cosech}(1/x)$. Find $\frac{dy}{dx}$.
8. $\sinh y = x^2 y$. Find $\frac{dy}{dx}$.

---

# PART 4: Inverse Trigonometric Functions

## 4.1 What Are Inverse Trig Functions?

| Function | Meaning | Domain |
|---|---|---|
| $y = \sin^{-1} x$ | $y$ is the angle whose sine is $x$ | $-1 \leq x \leq 1$ |
| $y = \cos^{-1} x$ | $y$ is the angle whose cosine is $x$ | $-1 \leq x \leq 1$ |
| $y = \tan^{-1} x$ | $y$ is the angle whose tangent is $x$ | All $x$ |

Also written as: $\arcsin x$, $\arccos x$, $\arctan x$.

## 4.2 Derivatives — MUST MEMORISE

| $y$ | $\dfrac{dy}{dx}$ | Domain |
|---|---|---|
| **$\sin^{-1} x$** | **$\displaystyle \frac{1}{\sqrt{1 - x^2}}$** | $-1 < x < 1$ |
| **$\cos^{-1} x$** | **$\displaystyle -\frac{1}{\sqrt{1 - x^2}}$** | $-1 < x < 1$ |
| **$\tan^{-1} x$** | **$\displaystyle \frac{1}{1 + x^2}$** | All $x$ |

---

## 4.3 Worked Examples

### Example 1 — Direct (Easy)

> **Question:** $y = \sin^{-1} x$. Find $\frac{dy}{dx}$.

$$\frac{dy}{dx} = \frac{1}{\sqrt{1 - x^2}} \quad\checkmark$$

---

### Example 2 — Chain Rule (Easy)

> **Question:** $y = \tan^{-1} 3x$. Find $\frac{dy}{dx}$.

Inner: $u = 3x$

$$\frac{dy}{dx} = \frac{1}{1 + (3x)^2} \times 3 = \frac{3}{1 + 9x^2} \quad\checkmark$$

---

### Example 3 — Chain Rule with Quadratic (Medium)

> **Question:** $y = \cos^{-1}(x^2)$. Find $\frac{dy}{dx}$.

Inner: $u = x^2$

$$\frac{dy}{dx} = -\frac{1}{\sqrt{1 - (x^2)^2}} \times 2x = -\frac{2x}{\sqrt{1 - x^4}} \quad\checkmark$$

Domain: $-1 < x^2 < 1$, so $-1 < x < 1$.

---

### Example 4 — Product Rule (Medium)

> **Question:** $y = x \cdot \sin^{-1} x$. Find $\frac{dy}{dx}$.

Product rule: $u = x$, $v = \sin^{-1} x$

$$\frac{dy}{dx} = 1 \cdot \sin^{-1} x + x \cdot \frac{1}{\sqrt{1 - x^2}}$$

$$= \sin^{-1} x + \frac{x}{\sqrt{1 - x^2}} \quad\checkmark$$

---

### Example 5 — Product + Chain (Medium)

> **Question:** $y = x \cdot \cos^{-1} 2x$. Find $\frac{dy}{dx}$.

$u = x$, $v = \cos^{-1} 2x$

$$v' = -\frac{1}{\sqrt{1 - (2x)^2}} \times 2 = -\frac{2}{\sqrt{1 - 4x^2}}$$

$$\frac{dy}{dx} = 1 \cdot \cos^{-1} 2x + x \cdot \left(-\frac{2}{\sqrt{1 - 4x^2}}\right)$$

$$= \cos^{-1} 2x - \frac{2x}{\sqrt{1 - 4x^2}} \quad\checkmark$$

---

### Example 6 — Implicit with Inverse Trig (Hard)

> **Question:** $xy = \sin^{-1} 2x$. Find $\frac{dy}{dx}$.

$$x\frac{dy}{dx} + y = \frac{2}{\sqrt{1 - 4x^2}}$$

$$x\frac{dy}{dx} = \frac{2}{\sqrt{1 - 4x^2}} - y$$

$$\frac{dy}{dx} = \frac{ \displaystyle \frac{2}{\sqrt{1 - 4x^2}} - y}{x} \quad\checkmark$$

---

### Example 7 — Power of Inverse Trig (Hard)

> **Question:** $y = (\tan^{-1} x)^2$. Find $\frac{dy}{dx}$.

Chain rule: outer $u^2$, inner $u = \tan^{-1} x$

$$\frac{dy}{dx} = 2(\tan^{-1} x) \times \frac{1}{1 + x^2} = \frac{2\tan^{-1} x}{1 + x^2} \quad\checkmark$$

---

### Example 8 — Quotient Rule (Hard)

> **Question:** $y = \dfrac{\sin^{-1} x}{x}$. Find $\frac{dy}{dx}$.

Quotient rule: $u = \sin^{-1} x$, $v = x$

$$\frac{dy}{dx} = \frac{x \cdot \frac{1}{\sqrt{1 - x^2}} - \sin^{-1} x \cdot 1}{x^2}$$

$$= \frac{\displaystyle \frac{x}{\sqrt{1 - x^2}} - \sin^{-1} x}{x^2} \quad\checkmark$$

---

## 4.4 Practice Questions — Inverse Trig

1. $y = \sin^{-1}(5x)$. Find $\frac{dy}{dx}$.
2. $y = \tan^{-1}\left(\frac{x}{2}\right)$. Find $\frac{dy}{dx}$.
3. $y = x^2 \cos^{-1} x$. Find $\frac{dy}{dx}$.
4. $y = \tan^{-1}\left(\frac{1}{x}\right)$. Find $\frac{dy}{dx}$.
5. $y = \sqrt{1 - x^2} \cdot \sin^{-1} x$. Find $\frac{dy}{dx}$ and simplify.
6. $x^2 y = \tan^{-1} x$. Find $\frac{dy}{dx}$.
7. $y = \sin^{-1}(\cos x)$. Find $\frac{dy}{dx}$.
8. $y = (\sin^{-1} x)(\cos^{-1} x)$. Find $\frac{dy}{dx}$.

---

# PART 5: Inverse Hyperbolic Functions

## 5.1 Derivatives — MUST MEMORISE

| $y$ | $\dfrac{dy}{dx}$ | Domain |
|---|---|---|
| **$\sinh^{-1} x$** | **$\displaystyle \frac{1}{\sqrt{1 + x^2}}$** | All $x$ |
| **$\cosh^{-1} x$** | **$\displaystyle \frac{1}{\sqrt{x^2 - 1}}$** | $x > 1$ |
| **$\tanh^{-1} x$** | **$\displaystyle \frac{1}{1 - x^2}$** | $-1 < x < 1$ |

### ⚠️ Key Differences from Inverse Trig

| Inverse Trig | Derivative | Inverse Hyperbolic | Derivative |
|---|---|---|---|
| $\sin^{-1} x$ | $\displaystyle \frac{1}{\sqrt{1 - x^2}}$ | $\sinh^{-1} x$ | $\displaystyle \frac{1}{\sqrt{1 + x^2}}$ ← **PLUS** |
| $\cos^{-1} x$ | $\displaystyle -\frac{1}{\sqrt{1 - x^2}}$ | $\cosh^{-1} x$ | $\displaystyle \frac{1}{\sqrt{x^2 - 1}}$ |
| $\tan^{-1} x$ | $\displaystyle \frac{1}{1 + x^2}$ | $\tanh^{-1} x$ | $\displaystyle \frac{1}{1 - x^2}$ ← **MINUS** |

> **The $\sinh^{-1}$ and $\tanh^{-1}$ derivatives are SWAPPED compared to their trig counterparts!**

---

## 5.2 Worked Examples

### Example 1 — Direct (Easy)

> **Question:** $y = \sinh^{-1} x$. Find $\frac{dy}{dx}$.

$$\frac{dy}{dx} = \frac{1}{\sqrt{1 + x^2}} \quad\checkmark$$

---

### Example 2 — Chain Rule (Easy)

> **Question:** $y = \cosh^{-1}(2x)$. Find $\frac{dy}{dx}$.

Inner: $u = 2x$

$$\frac{dy}{dx} = \frac{1}{\sqrt{(2x)^2 - 1}} \times 2 = \frac{2}{\sqrt{4x^2 - 1}} \quad\checkmark$$

Domain: $2x > 1 \;\Rightarrow\; x > \frac{1}{2}$.

---

### Example 3 — Chain Rule with Quadratic (Medium)

> **Question:** $y = \tanh^{-1}(x^2)$. Find $\frac{dy}{dx}$.

Inner: $u = x^2$

$$\frac{dy}{dx} = \frac{1}{1 - (x^2)^2} \times 2x = \frac{2x}{1 - x^4} \quad\checkmark$$

Domain: $-1 < x^2 < 1 \;\Rightarrow\; -1 < x < 1$.

---

### Example 4 — Product Rule (Medium)

> **Question:** $y = x \cdot \sinh^{-1} 2x$. Find $\frac{dy}{dx}$.

$u = x$, $v = \sinh^{-1} 2x$

$$v' = \frac{1}{\sqrt{1 + (2x)^2}} \times 2 = \frac{2}{\sqrt{1 + 4x^2}}$$

$$\frac{dy}{dx} = 1 \cdot \sinh^{-1} 2x + x \cdot \frac{2}{\sqrt{1 + 4x^2}}$$

$$= \sinh^{-1} 2x + \frac{2x}{\sqrt{1 + 4x^2}} \quad\checkmark$$

---

### Example 5 — Implicit with Inverse Hyperbolic (Hard)

> **Question:** $\tanh^{-1}(x + y) = xy$. Find $\frac{dy}{dx}$.

$$\frac{1}{1 - (x+y)^2} \cdot \left(1 + \frac{dy}{dx}\right) = y + x\frac{dy}{dx}$$

$$\frac{1 + \frac{dy}{dx}}{1 - (x+y)^2} = y + x\frac{dy}{dx}$$

$$1 + \frac{dy}{dx} = [1 - (x+y)^2]\left(y + x\frac{dy}{dx}\right)$$

$$1 + \frac{dy}{dx} = y[1 - (x+y)^2] + x[1 - (x+y)^2]\frac{dy}{dx}$$

$$\frac{dy}{dx} - x[1 - (x+y)^2]\frac{dy}{dx} = y[1 - (x+y)^2] - 1$$

$$\frac{dy}{dx}\left(1 - x[1 - (x+y)^2]\right) = y[1 - (x+y)^2] - 1$$

$$\frac{dy}{dx} = \frac{y[1 - (x+y)^2] - 1}{1 - x[1 - (x+y)^2]} \quad\checkmark$$

---

## 5.3 Practice Questions — Inverse Hyperbolic

1. $y = \sinh^{-1}(4x)$. Find $\frac{dy}{dx}$.
2. $y = \tanh^{-1}(3x - 1)$. Find $\frac{dy}{dx}$.
3. $y = \cosh^{-1}\left(\frac{x}{2}\right)$. Find $\frac{dy}{dx}$.
4. $y = e^x \cdot \sinh^{-1} x$. Find $\frac{dy}{dx}$.
5. $y = x \cdot \tanh^{-1} x$. Find $\frac{dy}{dx}$ and simplify.
6. $y = (\sinh^{-1} x)^2$. Find $\frac{dy}{dx}$.
7. $y = \ln(\cosh^{-1} x)$. Find $\frac{dy}{dx}$.

---

# PART 6: Maclaurin Series

## 6.1 The Formula

$$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \frac{f^{(4)}(0)}{4!}x^4 + \cdots$$

In summation form:

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}x^n$$

---

## 6.2 Method 1: Direct Differentiation

### Step-by-Step

| Step | What To Do |
|---|---|
| **Step 1** | Find $f(0)$ — plug $x = 0$ into the function |
| **Step 2** | Find $f'(x)$, then $f'(0)$ |
| **Step 3** | Find $f''(x)$, then $f''(0)$ |
| **Step 4** | Continue until you have enough **non-zero** terms |
| **Step 5** | Plug into the formula: $f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \cdots$ |
| **Step 6** | Simplify coefficients |

---

### Example 1 — $f(x) = e^x$

| $n$ | $f^{(n)}(x)$ | $f^{(n)}(0)$ |
|---|---|---|
| 0 | $e^x$ | 1 |
| 1 | $e^x$ | 1 |
| 2 | $e^x$ | 1 |
| 3 | $e^x$ | 1 |
| 4 | $e^x$ | 1 |

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots \quad\checkmark$$

---

### Example 2 — $f(x) = \sin x$

| $n$ | $f^{(n)}(x)$ | $f^{(n)}(0)$ |
|---|---|---|
| 0 | $\sin x$ | $0$ |
| 1 | $\cos x$ | $1$ |
| 2 | $-\sin x$ | $0$ |
| 3 | $-\cos x$ | $-1$ |
| 4 | $\sin x$ | $0$ |
| 5 | $\cos x$ | $1$ |

Pattern: $0, 1, 0, -1, 0, 1, 0, -1, \dots$

$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots \quad\checkmark$$

---

### Example 3 — $f(x) = \cos x$ (by differentiating $\sin x$)

$$\cos x = \frac{d}{dx}(\sin x) = \frac{d}{dx}\left(x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots\right)$$

$$= 1 - \frac{3x^2}{3!} + \frac{5x^4}{5!} - \cdots$$

$$= 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots \quad\checkmark$$

---

### Example 4 — $f(x) = \sin^{-1} x$ (First Three Non-Zero Terms)

| $n$ | $f^{(n)}(x)$ | $f^{(n)}(0)$ |
|---|---|---|
| 0 | $\sin^{-1} x$ | $0$ |
| 1 | $(1 - x^2)^{-1/2}$ | $1$ |
| 2 | $x(1 - x^2)^{-3/2}$ | $0$ |
| 3 | $(1-x^2)^{-3/2} + 3x^2(1-x^2)^{-5/2}$ | $1$ |
| 4 | ... | $0$ |
| 5 | ... | $9$ |

$$\sin^{-1} x = x + \frac{x^3}{6} + \frac{9x^5}{120} + \cdots$$

$$= x + \frac{x^3}{6} + \frac{3x^5}{40} + \cdots \quad\checkmark$$

---

## 6.3 Method 2: Using Known Series (Substitution)

### Step-by-Step

| Step | What To Do |
|---|---|
| **Step 1** | Identify a standard series inside your function |
| **Step 2** | Substitute the argument into that series |
| **Step 3** | Simplify |

---

### Example 1 — $f(x) = e^{2x}$

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$$

Replace $x$ with $2x$:

$$e^{2x} = 1 + 2x + \frac{(2x)^2}{2!} + \frac{(2x)^3}{3!} + \cdots$$

$$= 1 + 2x + \frac{4x^2}{2} + \frac{8x^3}{6} + \cdots$$

$$= 1 + 2x + 2x^2 + \frac{4x^3}{3} + \cdots \quad\checkmark$$

---

### Example 2 — $f(x) = \sin 3x$

$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$$

Replace $x$ with $3x$:

$$\sin 3x = 3x - \frac{(3x)^3}{3!} + \frac{(3x)^5}{5!} - \cdots$$

$$= 3x - \frac{27x^3}{6} + \frac{243x^5}{120} - \cdots$$

$$= 3x - \frac{9x^3}{2} + \frac{81x^5}{40} - \cdots \quad\checkmark$$

---

### Example 3 — $f(x) = e^{x^2}$

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots$$

Replace $x$ with $x^2$:

$$e^{x^2} = 1 + x^2 + \frac{(x^2)^2}{2!} + \frac{(x^2)^3}{3!} + \cdots$$

$$= 1 + x^2 + \frac{x^4}{2!} + \frac{x^6}{6} + \cdots \quad\checkmark$$

---

### Example 4 — $f(x) = \ln(1+2x)$

$$\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots\quad(-1 < x \leq 1)$$

Replace $x$ with $2x$:

$$\ln(1+2x) = 2x - \frac{(2x)^2}{2} + \frac{(2x)^3}{3} - \frac{(2x)^4}{4} + \cdots$$

$$= 2x - \frac{4x^2}{2} + \frac{8x^3}{3} - \frac{16x^4}{4} + \cdots$$

$$= 2x - 2x^2 + \frac{8x^3}{3} - 4x^4 + \cdots \quad\checkmark$$

Valid for $-\frac{1}{2} < x \leq \frac{1}{2}$.

---

### Example 5 — Product of Series (Hard)

> **Question:** Find Maclaurin series for $f(x) = e^x \cos x$ up to $x^3$.

$$e^x = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \cdots$$

$$\cos x = 1 - \frac{x^2}{2} + \frac{x^4}{24} - \cdots$$

Multiply:

$$(1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \cdots)(1 - \frac{x^2}{2} + \cdots)$$

$$= 1\cdot1 + x\cdot1 + \left(\frac{x^2}{2}\cdot1 + 1\cdot\left(-\frac{x^2}{2}\right)\right) + \left(\frac{x^3}{6}\cdot1 + x\cdot\left(-\frac{x^2}{2}\right)\right) + \cdots$$

$$= 1 + x + \left(\frac{x^2}{2} - \frac{x^2}{2}\right) + \left(\frac{x^3}{6} - \frac{x^3}{2}\right) + \cdots$$

$$= 1 + x - \frac{x^3}{3} + \cdots \quad\checkmark$$

---

## 6.4 Method 3: Successive Implicit Differentiation ⭐

**This is the advanced technique the Cambridge syllabus explicitly mentions.**

### The Idea
1. Find a simple differential equation that the function satisfies
2. Differentiate THAT equation repeatedly
3. Evaluate at $x = 0$
4. Build the series

### When To Use This Method

| Function | Differential Equation | At $x = 0$ |
|---|---|---|
| $y = \tan x$ | $y' = 1 + y^2$ | $y = 0$, $y' = 1$ |
| $y = \tanh x$ | $y' = 1 - y^2$ | $y = 0$, $y' = 1$ |
| $y = \ln(1+x)$ | $y' = e^{-y}$ | $y = 0$, $y' = 1$ |

---

### Example 1 — $y = \tan x$ (Classic Cambridge Question)

**Step 1:** $y = \tan x$

**Step 2:** Find $y'$ in terms of $y$:

$$y' = \sec^2 x = 1 + \tan^2 x = 1 + y^2 \quad\text{← key equation}$$

**Step 3:** Differentiate repeatedly:

$$y'' = \frac{d}{dx}(1 + y^2) = 2y \cdot y'$$

$$y''' = \frac{d}{dx}(2y y') = 2y' \cdot y' + 2y \cdot y'' = 2(y')^2 + 2y y''$$

$$y^{(4)} = \frac{d}{dx}(2(y')^2 + 2y y'') = 4y' y'' + 2y' y'' + 2y y''' = 6y' y'' + 2y y'''$$

$$y^{(5)} = \frac{d}{dx}(6y' y'' + 2y y''') = 6(y'')^2 + 6y' y''' + 2y' y''' + 2y y^{(4)} = 6(y'')^2 + 8y' y''' + 2y y^{(4)}$$

**Step 4:** Evaluate at $x = 0$ (where $y = 0$ and $y' = 1$):

$$y(0) = 0,\quad y'(0) = 1$$

$$y''(0) = 2(0)(1) = 0$$

$$y'''(0) = 2(1)^2 + 2(0)(0) = 2$$

$$y^{(4)}(0) = 0$$

$$y^{(5)}(0) = 6(0)^2 + 8(1)(2) + 0 = 16$$

**Step 5:** Maclaurin series:

$$\tan x = 0 + 1\cdot x + 0\cdot\frac{x^2}{2!} + 2\cdot\frac{x^3}{3!} + 0\cdot\frac{x^4}{4!} + 16\cdot\frac{x^5}{5!} + \cdots$$

$$= x + \frac{2x^3}{6} + \frac{16x^5}{120} + \cdots$$

$$= x + \frac{x^3}{3} + \frac{2x^5}{15} + \cdots \quad\checkmark$$

---

### Example 2 — $y = \ln(1+x)$ Using the $e^{-y}$ Trick

**Step 1:** $y = \ln(1+x)$

**Step 2:** Note that $e^y = 1 + x$, so:

$$y' = \frac{1}{1+x} = e^{-y} \quad\text{← key equation}$$

**Step 3:** Differentiate:

$$y'' = -y' \cdot e^{-y} = -e^{-y} \cdot e^{-y} = -e^{-2y}$$

$$y''' = 2e^{-3y}$$

$$y^{(4)} = -6e^{-4y}$$

**Step 4:** At $x = 0$, $y = 0$:

$$y'(0) = e^0 = 1$$

$$y''(0) = -1$$

$$y'''(0) = 2$$

$$y^{(4)}(0) = -6$$

**Step 5:**

$$\ln(1+x) = 0 + 1\cdot x + (-1)\frac{x^2}{2!} + 2\cdot\frac{x^3}{3!} + (-6)\cdot\frac{x^4}{4!} + \cdots$$

$$= x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots \quad\checkmark$$

---

### Example 3 — $y = \tanh x$

**Step 1:** $y = \tanh x$

**Step 2:** $y' = \operatorname{sech}^2 x = 1 - \tanh^2 x = 1 - y^2$

**Step 3:** 

$$y'' = -2y y'$$

$$y''' = -2(y')^2 - 2y y''$$

$$y^{(4)} = -6y' y'' - 2y y'''$$

**Step 4:** At $x = 0$: $y = 0$, $y' = 1$

$$y''(0) = 0$$

$$y'''(0) = -2$$

$$y^{(4)}(0) = 0$$

**Step 5:**

$$\tanh x = x - \frac{x^3}{3} + \frac{2x^5}{15} - \frac{17x^7}{315} + \cdots \quad\checkmark$$

---

## 6.5 Using Maclaurin Series for Approximations

### Example 1 — Estimate $e^{0.1}$

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots$$

$$e^{0.1} = 1 + 0.1 + \frac{0.01}{2} + \frac{0.001}{6} + \frac{0.0001}{24} + \cdots$$

$$= 1 + 0.1 + 0.005 + 0.0001667 + 0.0000042 + \cdots$$

$$= 1.1051709\dots$$

Actual $e^{0.1} = 1.105170918\dots$ ✅ Very accurate with 5 terms.

---

### Example 2 — Estimate $\sin^{-1} 0.1$ to 9 decimal places

$$\sin^{-1} x = x + \frac{x^3}{6} + \frac{3x^5}{40} + \frac{15x^7}{336} + \cdots$$

$$\sin^{-1}0.1 = 0.1 + \frac{0.001}{6} + \frac{3(0.00001)}{40} + \frac{15(0.0000001)}{336} + \cdots$$

$$= 0.1 + 0.0001666667 + 0.00000075 + 0.0000000045 + \cdots$$

$$= 0.100167421\dots$$

Actual $\sin^{-1}0.1 \approx 0.100167421$ ✅

---

## 6.6 Standard Maclaurin Series — MUST MEMORISE ⭐

| Function | Series (first 4 non-zero terms) |
|---|---|
| $e^x$ | $\displaystyle 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots$ |
| $\sin x$ | $\displaystyle x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots$ |
| $\cos x$ | $\displaystyle 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots$ |
| $\ln(1+x)$ | $\displaystyle x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots$ |
| $\tan^{-1} x$ | $\displaystyle x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \cdots$ |
| $\sinh x$ | $\displaystyle x + \frac{x^3}{3!} + \frac{x^5}{5!} + \frac{x^7}{7!} + \cdots$ |
| $\cosh x$ | $\displaystyle 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \frac{x^6}{6!} + \cdots$ |
| $\tan x$ | $\displaystyle x + \frac{x^3}{3} + \frac{2x^5}{15} + \frac{17x^7}{315} + \cdots$ |
| $\tanh x$ | $\displaystyle x - \frac{x^3}{3} + \frac{2x^5}{15} - \frac{17x^7}{315} + \cdots$ |
| $\sin^{-1} x$ | $\displaystyle x + \frac{x^3}{6} + \frac{3x^5}{40} + \frac{15x^7}{336} + \cdots$ |
| $\sinh^{-1} x$ | $\displaystyle x - \frac{x^3}{6} + \frac{3x^5}{40} - \frac{5x^7}{112} + \cdots$ |

---

## 6.7 Practice Questions — Maclaurin

### Easy
1. Find Maclaurin series for $f(x) = e^{3x}$ up to $x^3$.
2. Find Maclaurin series for $f(x) = \cos 2x$ up to $x^4$.
3. Find Maclaurin series for $f(x) = \sinh x$ up to $x^5$.

### Medium
4. Find Maclaurin series for $f(x) = \ln(1 + 3x)$ up to $x^4$.
5. Find Maclaurin series for $f(x) = x e^x$ up to $x^4$.
6. Find Maclaurin series for $f(x) = \sin x \cos x$ up to $x^5$.
7. Use known series for $e^{-x^2}$ up to $x^6$.
8. Find Maclaurin series for $\tan^{-1} x$ up to $x^5$.

### Hard
9. Using successive implicit differentiation, find Maclaurin series for $y = \ln(1+x)$ up to $x^4$.
10. Given $y = \tan x$, show $y' = 1 + y^2$ and find Maclaurin up to $x^5$.
11. Using Maclaurin series for $\sin x$, estimate $\sin 0.2$ to 6 decimal places.
12. Find Maclaurin series for $f(x) = e^x \sin x$ up to $x^4$.

---

# PART 7: Successive Implicit Differentiation — Deep Dive

## 7.1 Why This Method Exists

When Cambridge asks you to **"use successive implicit differentiation"** to find a Maclaurin series, they want you to:

1. Find a **simple relationship** between $y$ and $y'$
2. Differentiate that **relationship** repeatedly (instead of the original function)
3. This is usually **much faster** and less error-prone

### The General Pattern

| Step | Action |
|---|---|
| **Step 1** | Write $y = f(x)$ |
| **Step 2** | Find a way to express $y'$ **in terms of $y$ only** (not $x$) |
| **Step 3** | Differentiate this to find $y''$ in terms of $y$ and $y'$ |
| **Step 4** | Differentiate again to find $y'''$ in terms of $y$, $y'$, $y''$ |
| **Step 5** | Continue until you have enough derivatives |
| **Step 6** | Evaluate at $x = 0$ |
| **Step 7** | Plug into Maclaurin formula |

---

## 7.2 Functions That Work With This Method

| Function | Key Trick | The Equation |
|---|---|---|
| $y = \tan x$ | $\sec^2 x = 1 + \tan^2 x$ | $y' = 1 + y^2$ |
| $y = \tanh x$ | $\operatorname{sech}^2 x = 1 - \tanh^2 x$ | $y' = 1 - y^2$ |
| $y = \ln(1+x)$ | $e^y = 1 + x \Rightarrow y' = e^{-y}$ | $y' = e^{-y}$ |
| $y = \sec x$ | $\sec x \tan x$ relationship | $y' = y\sqrt{y^2 - 1}$ |

---

## 7.3 Full Worked Example — $y = \tan x$ ⭐

**This is THE classic Cambridge question.**

**Step 1:** $y = \tan x$

**Step 2:** Express $y'$ in terms of $y$:

$$y' = \sec^2 x = 1 + \tan^2 x = 1 + y^2$$

**Step 3:** Differentiate successively:

$$y' = 1 + y^2$$

$$y'' = \frac{d}{dx}(1 + y^2) = 2y \cdot y'$$

$$y''' = \frac{d}{dx}(2y y') = 2(y')^2 + 2y y''$$

$$y^{(4)} = \frac{d}{dx}(2(y')^2 + 2y y'') = 4y' y'' + 2y' y'' + 2y y''' = 6y' y'' + 2y y'''$$

$$y^{(5)} = \frac{d}{dx}(6y' y'' + 2y y''') = 6(y'')^2 + 6y' y''' + 2y' y''' + 2y y^{(4)}$$

$$= 6(y'')^2 + 8y' y''' + 2y y^{(4)}$$

**Step 4:** Evaluate at $x = 0$ (where $\tan 0 = 0$):

$$y(0) = 0,\; y'(0) = 1 + 0 = 1$$

$$y''(0) = 2(0)(1) = 0$$

$$y'''(0) = 2(1)^2 + 2(0)(0) = 2$$

$$y^{(4)}(0) = 0$$

$$y^{(5)}(0) = 6(0)^2 + 8(1)(2) + 2(0)(0) = 16$$

**Step 5:** Build Maclaurin series:

$$\tan x = 0 + 1\cdot x + 0\cdot\frac{x^2}{2!} + 2\cdot\frac{x^3}{3!} + 0\cdot\frac{x^4}{4!} + 16\cdot\frac{x^5}{5!} + \cdots$$

$$\tan x = x + \frac{2x^3}{6} + \frac{16x^5}{120} + \cdots$$

$$\tan x = x + \frac{x^3}{3} + \frac{2x^5}{15} + \cdots \quad\checkmark$$

---

## 7.4 Full Worked Example — $y = \ln(1+x)$

**Step 1:** $y = \ln(1+x)$

**Step 2:** We know $e^y = 1 + x$, so:

$$y' = \frac{1}{1+x} = e^{-y}$$

**Step 3:** Differentiate:

$$y' = e^{-y}$$

$$y'' = -y' e^{-y} = -e^{-y} \cdot e^{-y} = -e^{-2y}$$

$$y''' = 2e^{-3y}$$

$$y^{(4)} = -6e^{-4y}$$

**Step 4:** At $x = 0$: $y = \ln(1) = 0$

$$y'(0) = e^0 = 1$$

$$y''(0) = -1$$

$$y'''(0) = 2$$

$$y^{(4)}(0) = -6$$

**Step 5:**

$$\ln(1+x) = 0 + 1\cdot x + (-1)\frac{x^2}{2!} + 2\cdot\frac{x^3}{3!} + (-6)\frac{x^4}{4!} + \cdots$$

$$= x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots \quad\checkmark$$

---

# 📝 COMPLETE FORMULA SHEET

## Implicit Differentiation

$$\frac{d}{dx}(y^n) = n y^{n-1}\frac{dy}{dx}$$

$$\frac{d}{dx}(\sin y) = \cos y \cdot \frac{dy}{dx}$$

$$\frac{d}{dx}(\cos y) = -\sin y \cdot \frac{dy}{dx}$$

$$\frac{d}{dx}(e^y) = e^y \cdot \frac{dy}{dx}$$

$$\frac{d}{dx}(\ln y) = \frac{1}{y} \cdot \frac{dy}{dx}$$

Triple product: $\displaystyle \frac{d}{dx}(uvw) = vw\frac{du}{dx} + uw\frac{dv}{dx} + uv\frac{dw}{dx}$

---

## Parametric Differentiation

$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$$

$$\frac{d^2y}{dx^2} = \frac{d}{dt}\left(\frac{dy}{dx}\right) \times \frac{dt}{dx} = \frac{d}{dt}\left(\frac{dy}{dx}\right) \Big/ \frac{dx}{dt}$$

---

## Hyperbolic Functions

$$\sinh x = \frac{e^x - e^{-x}}{2},\quad \cosh x = \frac{e^x + e^{-x}}{2},\quad \tanh x = \frac{\sinh x}{\cosh x}$$

$$\cosh^2 x - \sinh^2 x = 1$$

| $y$ | $\dfrac{dy}{dx}$ |
|---|---|
| $\sinh x$ | $\cosh x$ |
| $\cosh x$ | $\sinh x$ |
| $\tanh x$ | $\operatorname{sech}^2 x$ |
| $\operatorname{sech} x$ | $-\operatorname{sech} x \tanh x$ |
| $\operatorname{cosech} x$ | $-\operatorname{cosech} x \coth x$ |
| $\coth x$ | $-\operatorname{cosech}^2 x$ |

---

## Inverse Trigonometric Functions

| $y$ | $\dfrac{dy}{dx}$ | Domain |
|---|---|---|
| $\sin^{-1} x$ | $\displaystyle \frac{1}{\sqrt{1 - x^2}}$ | $-1 < x < 1$ |
| $\cos^{-1} x$ | $\displaystyle -\frac{1}{\sqrt{1 - x^2}}$ | $-1 < x < 1$ |
| $\tan^{-1} x$ | $\displaystyle \frac{1}{1 + x^2}$ | All $x$ |

---

## Inverse Hyperbolic Functions

| $y$ | $\dfrac{dy}{dx}$ | Domain |
|---|---|---|
| $\sinh^{-1} x$ | $\displaystyle \frac{1}{\sqrt{1 + x^2}}$ | All $x$ |
| $\cosh^{-1} x$ | $\displaystyle \frac{1}{\sqrt{x^2 - 1}}$ | $x > 1$ |
| $\tanh^{-1} x$ | $\displaystyle \frac{1}{1 - x^2}$ | $-1 < x < 1$ |

---

## Maclaurin Series

$$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \frac{f^{(4)}(0)}{4!}x^4 + \cdots$$

| Function | Series |
|---|---|
| $e^x$ | $\displaystyle 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots$ |
| $\sin x$ | $\displaystyle x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots$ |
| $\cos x$ | $\displaystyle 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots$ |
| $\ln(1+x)$ | $\displaystyle x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \frac{x^5}{5} - \cdots$ |
| $\tan^{-1} x$ | $\displaystyle x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \cdots$ |
| $\sinh x$ | $\displaystyle x + \frac{x^3}{3!} + \frac{x^5}{5!} + \frac{x^7}{7!} + \cdots$ |
| $\cosh x$ | $\displaystyle 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \frac{x^6}{6!} + \cdots$ |
| $\tan x$ | $\displaystyle x + \frac{x^3}{3} + \frac{2x^5}{15} + \frac{17x^7}{315} + \cdots$ |

---

# 🎯 CAMBRIDGE EXAM ANALYSIS

## Question Frequency (from past papers 2018–2025)

### 🔴 Every Single Paper (100%)

| Topic | Typical Marks |
|---|---|
| Implicit second derivative $\frac{d^2y}{dx^2}$ | 6–9 |
| Parametric second derivative $\frac{d^2y}{dx^2}$ | 6–8 |
| Maclaurin series (3–4 non-zero terms) | 7–9 |

### 🟡 Very Common (70%+)

| Topic |
|---|
| Hyperbolic function differentiation (with chain/product rule) |
| Inverse trig/hyperbolic differentiation |
| Numerical derivative values at a point |

### 🟢 Sometimes (30–50%)

| Topic |
|---|
| Using known series for new expansions |
| Maclaurin approximations of values |
| Stationary point nature (parametric) |

---

## Typical Mark Schemes

### Implicit $\frac{d^2y}{dx^2}$ (8 marks)

| Mark | What For |
|---|---|
| B1 | Differentiates first time correctly |
| M1 | Uses correct rules for $y$ terms |
| A1 | Correct $\frac{dy}{dx}$ expression |
| M1 | Differentiates "first form" again |
| M1A1 | Handles product/chain rules correctly |
| M1 | Substitutes $\frac{dy}{dx}$ |
| A1 | Simplified $\frac{d^2y}{dx^2}$ |

### Parametric $\frac{d^2y}{dx^2}$ (7 marks)

| Mark | What For |
|---|---|
| M1 | Finds $\frac{dx}{dt}$ and $\frac{dy}{dt}$ |
| A1 | Correct $\frac{dy}{dx}$ |
| M1A1 | Correct $\frac{d}{dt}(\frac{dy}{dx})$ |
| M1 | Multiplies by $\frac{dt}{dx}$ |
| A1 | Simplified $\frac{d^2y}{dx^2}$ |

### Maclaurin Series (8 marks)

| Mark | What For |
|---|---|
| B1 | $f(0)$ |
| M1A1 | $f'(0)$ |
| M1A1 | Further derivatives and values |
| M1 | Uses formula (divides by factorials) |
| A1 | Correct series (3–4 non-zero terms) |

---

# 🧠 COMMON MISTAKES

## 🔴 Critical Errors

| Mistake | Correction |
|---|---|
| $\frac{d^2y}{dx^2} = \frac{d^2y}{dt^2} \div \frac{d^2x}{dt^2}$ ❌ | $\frac{d^2y}{dx^2} = \frac{d}{dt}(\frac{dy}{dx}) \times \frac{dt}{dx}$ ✅ |
| $\frac{d}{dx}(y^2) = 2y$ ❌ | $\frac{d}{dx}(y^2) = 2y \cdot \frac{dy}{dx}$ ✅ |
| $\frac{d}{dx}(\cosh x) = -\sinh x$ ❌ | $\frac{d}{dx}(\cosh x) = +\sinh x$ ✅ |
| $\frac{d}{dx}(\sinh^{-1} x) = \frac{1}{\sqrt{1-x^2}}$ ❌ | $\frac{d}{dx}(\sinh^{-1} x) = \frac{1}{\sqrt{1+x^2}}$ ✅ |
| $\frac{d}{dx}(\tanh^{-1} x) = \frac{1}{1+x^2}$ ❌ | $\frac{d}{dx}(\tanh^{-1} x) = \frac{1}{1-x^2}$ ✅ |
| Maclaurin: forgetting $n!$ in denominator ❌ | $f(x) = \sum \frac{f^{(n)}(0)}{n!}x^n$ ✅ |

## 🟡 Common Errors

| Error | Fix |
|---|---|
| Not simplifying $\frac{d^2y}{dx^2}$ | Factor and cancel — final A1 requires it |
| Forgetting $\frac{dt}{dx}$ in parametric $\frac{d^2y}{dx^2}$ | Always: $\frac{dt}{dx} = 1 / \frac{dx}{dt}$ |
| Not using "first form" for implicit $\frac{d^2y}{dx^2}$ | Differentiate BEFORE rearranging |
| Confusing $y'$ notation in successive implicit | $y'$ is $\frac{dy}{dx}$, not something else |
| Counting wrong number of Maclaurin terms | "first 3 non-zero" means skip zeros |
| Not checking $\frac{dx}{dt} \neq 0$ for stationary points | Always verify! |

---

# 📚 PRACTICE QUESTIONS & SOLUTIONS

## Question 1 — Implicit

> Given that $x^3 + y^3 = 3xy$, find $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$ in terms of $x$ and $y$.

**Solution:**

$$3x^2 + 3y^2\frac{dy}{dx} = 3y + 3x\frac{dy}{dx}$$

$$3y^2\frac{dy}{dx} - 3x\frac{dy}{dx} = 3y - 3x^2$$

$$\frac{dy}{dx}(3y^2 - 3x) = 3y - 3x^2$$

$$\frac{dy}{dx} = \frac{y - x^2}{y^2 - x}$$

For $\frac{d^2y}{dx^2}$, differentiate $3x^2 + 3y^2\frac{dy}{dx} = 3y + 3x\frac{dy}{dx}$:

$$6x + 6y\frac{dy}{dx}\frac{dy}{dx} + 3y^2\frac{d^2y}{dx^2} = 3\frac{dy}{dx} + 3\frac{dy}{dx} + 3x\frac{d^2y}{dx^2}$$

$$6x + 6y\left(\frac{dy}{dx}\right)^2 + 3y^2\frac{d^2y}{dx^2} = 6\frac{dy}{dx} + 3x\frac{d^2y}{dx^2}$$

$$(3y^2 - 3x)\frac{d^2y}{dx^2} = 6\frac{dy}{dx} - 6x - 6y\left(\frac{dy}{dx}\right)^2$$

$$\frac{d^2y}{dx^2} = \frac{6\left(\frac{dy}{dx} - x - y\left(\frac{dy}{dx}\right)^2\right)}{3(y^2 - x)}$$

Substitute $\frac{dy}{dx} = \frac{y - x^2}{y^2 - x}$ to get the final expression.

---

## Question 2 — Parametric

> $x = t^2 + 2$, $y = t^3 - 3t^2 + 2$. Find stationary points and determine their nature.

$$\frac{dx}{dt} = 2t,\quad \frac{dy}{dt} = 3t^2 - 6t$$

Stationary: $3t^2 - 6t = 0 \;\Rightarrow\; 3t(t-2) = 0 \;\Rightarrow\; t = 0, 2$

At $t = 2$: $\frac{dx}{dt} = 4 \neq 0$. At $t = 0$: $\frac{dx}{dt} = 0$ (vertical tangent).

$t = 2$: $x = 6$, $y = -2$

$$\frac{dy}{dx} = \frac{3t^2 - 6t}{2t} = \frac{3t - 6}{2}$$

$$\frac{d}{dt}\left(\frac{dy}{dx}\right) = \frac{3}{2},\quad \frac{dt}{dx} = \frac{1}{2t}$$

$$\frac{d^2y}{dx^2} = \frac{3}{2} \times \frac{1}{2t} = \frac{3}{4t}$$

At $t = 2$: $\frac{d^2y}{dx^2} = \frac{3}{8} > 0 \;\Rightarrow\; \textbf{MINIMUM at }(6, -2)$

---

## Question 3 — Hyperbolic

> $y = x\sinh x - \cosh x$. Find $\frac{dy}{dx}$. Hence find $\int x\cosh x\;dx$.

$$\frac{dy}{dx} = 1\cdot\sinh x + x\cosh x - \sinh x = x\cosh x$$

Since $\frac{d}{dx}(x\sinh x - \cosh x) = x\cosh x$:

$$\int x\cosh x\;dx = x\sinh x - \cosh x + C$$

---

## Question 4 — Maclaurin (Successive Implicit)

> By first showing $y = \ln(1+x)$ satisfies $y' = e^{-y}$, find Maclaurin series up to $x^4$.

$y = \ln(1+x) \;\Rightarrow\; e^y = 1+x \;\Rightarrow\; y' = \frac{1}{1+x} = e^{-y}$ ✓

$$y' = e^{-y},\quad y'' = -e^{-2y},\quad y''' = 2e^{-3y},\quad y^{(4)} = -6e^{-4y}$$

At $x=0$: $y=0$, $y'=1$, $y''=-1$, $y'''=2$, $y^{(4)} = -6$

$$\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots$$

---

## Question 5 — Mixed Inverse

> $y = \tan^{-1}(\sqrt{x^2 - 1})$. Find $\frac{dy}{dx}$.

Chain rule: outer $\tan^{-1}(u)$, inner $u = \sqrt{x^2 - 1}$.

$$\frac{dy}{dx} = \frac{1}{1 + (x^2 - 1)} \times \frac{x}{\sqrt{x^2 - 1}} = \frac{1}{x^2} \times \frac{x}{\sqrt{x^2 - 1}} = \frac{1}{x\sqrt{x^2 - 1}}$$

---

# ⏱️ EXAM STRATEGY

## 48 Hours Before

### Memorisation Checklist
- [ ] All 6 hyperbolic derivatives
- [ ] All 3 inverse trig derivatives
- [ ] All 3 inverse hyperbolic derivatives
- [ ] Maclaurin series formula
- [ ] Standard series: $e^x$, $\sin x$, $\cos x$, $\ln(1+x)$
- [ ] Parametric $\frac{d^2y}{dx^2}$ formula

### Practice Checklist
- [ ] 2 implicit second derivative questions
- [ ] 2 parametric second derivative questions
- [ ] 2 Maclaurin series questions
- [ ] 2 hyperbolic differentiation questions
- [ ] 1 "successive implicit" Maclaurin question

---

## In The Exam

| When You See... | Do This |
|---|---|
| "Find $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$" (implicit) | Differentiate once, stop at **first form**, differentiate again |
| "Find $\frac{dy}{dx}$ and $\frac{d^2y}{dx^2}$" (parametric) | $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$; $\frac{d^2y}{dx^2} = \frac{d}{dt}(\frac{dy}{dx}) \times \frac{dt}{dx}$ |
| "Find Maclaurin series" | Decide: direct diff OR successive implicit? |
| "Differentiate" (hyperbolic) | Apply rule, chain rule if needed |
| "Hence estimate" | Substitute $x$ into series |
| "Show that" | Show ALL working — method marks are generous |

---

## Last-Resort Tips

1. **Can't remember a derivative?** Go back to definitions:
   - $\sinh x = \frac{e^x - e^{-x}}{2}$ → differentiate to get $\cosh x$
   - $\sin^{-1} x$ → let $y = \sin^{-1}x$, take $\sin$ both sides, differentiate implicitly

2. **Algebra too messy?** Factor common terms. Look for identities like $\cosh^2 x - \sinh^2 x = 1$.

3. **Running out of time?** Write $f(0), f'(0), f''(0)$ for Maclaurin — method marks.
   For implicit $\frac{d^2y}{dx^2}$, just showing the differentiated first form gets M marks.

---

# QUICK REFERENCE CARD

Cut this out for last-minute revision.

### Derivatives

$$\sinh x \rightarrow \cosh x$$
$$\cosh x \rightarrow \sinh x \quad(\text{NO negative!})$$
$$\tanh x \rightarrow \operatorname{sech}^2 x$$
$$\sin^{-1} x \rightarrow \frac{1}{\sqrt{1-x^2}}$$
$$\cos^{-1} x \rightarrow -\frac{1}{\sqrt{1-x^2}}$$
$$\tan^{-1} x \rightarrow \frac{1}{1+x^2}$$
$$\sinh^{-1} x \rightarrow \frac{1}{\sqrt{1+x^2}}$$
$$\cosh^{-1} x \rightarrow \frac{1}{\sqrt{x^2-1}}$$
$$\tanh^{-1} x \rightarrow \frac{1}{1-x^2}$$

### Key Formulas

$$\text{Implicit: } \frac{d^2y}{dx^2} \text{ — differentiate the FIRST form}$$

$$\text{Parametric: } \frac{dy}{dx} = \frac{dy/dt}{dx/dt}$$

$$\text{Parametric } \frac{d^2y}{dx^2}: \frac{d}{dt}\left(\frac{dy}{dx}\right) \times \frac{dt}{dx}$$

$$\text{Maclaurin: } f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \cdots$$

### Deadly Sins

1. $\frac{d}{dx}(\cosh x) \neq -\sinh x$ (it's $+\sinh x$)
2. Parametric $\frac{d^2y}{dx^2} \neq \frac{d^2y/dt^2}{d^2x/dt^2}$
3. $\frac{d}{dx}(y^2) = 2y \cdot \frac{dy}{dx}$ (not $2y$)
4. $\frac{d}{dx}(\sinh^{-1} x) = \frac{1}{\sqrt{1+x^2}}$ (not $\frac{1}{\sqrt{1-x^2}}$)

---

> **Good luck! You've got this.** Every Cambridge differentiation question follows one of the patterns in this guide. 🚀

---

📁 **File saved to:** `/Users/adityabalaji/Documents/Codex/FURTHER_MATHS_DIFFERENTIATION_COMPLETE_GUIDE.md`
