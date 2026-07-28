# 📐 FURTHER MATHS HYPERBOLIC FUNCTIONS — COMPLETE STUDY GUIDE

## Cambridge International AS & A Level Further Mathematics (9231) — Paper 2

> **Chapter 19 Deep Dive:** Definitions, graphs, identities, derivatives, inverse functions, solving equations, integration, and exam strategy — every technique explained step-by-step with proper LaTeX.

---

# 📋 Table of Contents

1. [Syllabus Requirements](#1-syllabus-requirements)
2. [What Are Hyperbolic Functions?](#2-what-are-hyperbolic-functions)
3. [Definitions — Exponential Forms](#3-definitions--exponential-forms)
4. [Graphs of Hyperbolic Functions](#4-graphs-of-hyperbolic-functions)
5. [Hyperbolic Identities](#5-hyperbolic-identities)
6. [Derivatives of Hyperbolic Functions](#6-derivatives-of-hyperbolic-functions)
7. [Inverse Hyperbolic Functions](#7-inverse-hyperbolic-functions)
8. [Logarithmic Forms of Inverses](#8-logarithmic-forms-of-inverse-hyperbolic-functions)
9. [Derivatives of Inverse Hyperbolic Functions](#9-derivatives-of-inverse-hyperbolic-functions)
10. [Solving Hyperbolic Equations](#10-solving-hyperbolic-equations)
11. [Integration of Hyperbolic Functions](#11-integration-of-hyperbolic-functions)
12. [Complete Formula Sheet](#12-complete-formula-sheet)
13. [Cambridge Exam Analysis](#13-cambridge-exam-analysis)
14. [Common Mistakes](#14-common-mistakes)
15. [Practice Questions & Full Solutions](#15-practice-questions--full-solutions)
16. [Quick Reference Card](#16-quick-reference-card)

---

# 1. Syllabus Requirements

## What Cambridge Expects (9231 Further Pure Mathematics 2)

| Topic | Cambridge Learning Outcome | Exam Weight |
|---|---|---|
| **Exponential forms** | Relate $\sinh x$, $\cosh x$, $\tanh x$, $\operatorname{sech} x$, $\operatorname{cosech} x$, $\coth x$ to exponentials | ⭐⭐ |
| **Graphs** | Sketch graphs of all 6 hyperbolic functions, including transformations | ⭐⭐ |
| **Identities** | Prove and use hyperbolic identities including $\cosh^2 x - \sinh^2 x = 1$ | ⭐⭐⭐ |
| **Osborne's Rule** | Convert trigonometric identities to hyperbolic identities (with sign changes) | ⭐⭐ |
| **Inverse functions** | Find inverse hyperbolic functions and express in logarithmic form | ⭐⭐⭐ |
| **Derivatives** | Differentiate $\sinh$, $\cosh$, $\tanh$, $\operatorname{sech}$, $\operatorname{cosech}$, $\coth$ and their inverses | ⭐⭐⭐ |
| **Integration** | Integrate functions that lead to hyperbolic or inverse hyperbolic forms | ⭐⭐⭐ |
| **Solving equations** | Solve hyperbolic equations using exponential definitions and identities | ⭐⭐⭐ |

> **📌 Cambridge Pattern:** Hyperbolic functions appear on **Paper 2** (Further Pure Mathematics 2). Expect at least one 8–12 mark question. Identities and solving equations are the most frequently tested skills.

---

# 2. What Are Hyperbolic Functions?

Hyperbolic functions are **analogues of trigonometric functions** but defined using the **unit hyperbola** $x^2 - y^2 = 1$ rather than the unit circle $x^2 + y^2 = 1$.

| Shape | Equation | Functions Derived |
|---|---|---|
| Unit circle | $x^2 + y^2 = 1$ | $\sin x$, $\cos x$, $\tan x$ — **circular functions** |
| Unit hyperbola | $x^2 - y^2 = 1$ | $\sinh x$, $\cosh x$, $\tanh x$ — **hyperbolic functions** |

The hyperbolic functions arise naturally in **engineering, differential equations, and the shape of hanging cables (catenaries)**. The curve $y = \cosh x$ is called a **catenary** — the shape of a hanging chain supported at both ends.

---

# 3. Definitions — Exponential Forms

## 3.1 Primary Hyperbolic Functions

| Function | Pronunciation | Exponential Definition | Domain | Range |
|---|---|---|---|---|
| $\sinh x$ | **shine** | $\displaystyle \frac{e^x - e^{-x}}{2}$ | $\mathbb{R}$ | $\mathbb{R}$ |
| $\cosh x$ | **cosh** | $\displaystyle \frac{e^x + e^{-x}}{2}$ | $\mathbb{R}$ | $f(x) \ge 1$ |

## 3.2 Derived Hyperbolic Functions

| Function | Pronunciation | Exponential Definition | Domain | Range |
|---|---|---|---|---|
| $\tanh x$ | **tanch / than** | $\displaystyle \frac{e^x - e^{-x}}{e^x + e^{-x}} = \frac{e^{2x} - 1}{e^{2x} + 1}$ | $\mathbb{R}$ | $-1 < f(x) < 1$ |
| $\operatorname{sech} x$ | **setch** | $\displaystyle \frac{2}{e^x + e^{-x}}$ | $\mathbb{R}$ | $0 < f(x) \le 1$ |
| $\operatorname{cosech} x$ | **cosetch** | $\displaystyle \frac{2}{e^x - e^{-x}}$ | $x \neq 0$ | $f(x) \neq 0$ |
| $\coth x$ | **coth** | $\displaystyle \frac{e^x + e^{-x}}{e^x - e^{-x}}$ | $x \neq 0$ | $f(x) > 1,\; f(x) < -1$ |

### Key Relationship

$$\boxed{e^x = \cosh x + \sinh x}$$
$$\boxed{e^{-x} = \cosh x - \sinh x}$$

### Reciprocal Relationships (Third Letter Rule)

$$\operatorname{sech} x = \frac{1}{\cosh x}, \qquad \operatorname{cosech} x = \frac{1}{\sinh x}, \qquad \coth x = \frac{1}{\tanh x}$$

---

### Worked Example 1 — Converting to Exponential (Easy)

> **Question:** Express $4\cosh x - 3\sinh x$ in terms of $e^x$ and $e^{-x}$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Write definitions: $\displaystyle \cosh x = \frac{e^x + e^{-x}}{2},\; \sinh x = \frac{e^x - e^{-x}}{2}$ |
| **Step 2** | Substitute: $\displaystyle 4\left(\frac{e^x + e^{-x}}{2}\right) - 3\left(\frac{e^x - e^{-x}}{2}\right)$ |
| **Step 3** | Simplify: $\displaystyle 2(e^x + e^{-x}) - \frac{3}{2}(e^x - e^{-x})$ |
| **Step 4** | Combine: $\displaystyle 2e^x + 2e^{-x} - \frac{3}{2}e^x + \frac{3}{2}e^{-x}$ |
| **Step 5** | Result: $\displaystyle \frac{1}{2}e^x + \frac{7}{2}e^{-x}$ |

$$\boxed{\frac{e^x + 7e^{-x}}{2}} \quad\checkmark$$

---

### Worked Example 2 — Proving Relationships (Easy)

> **Question:** Prove that $\cosh^2 x - \sinh^2 x = 1$ using exponential definitions.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | $\displaystyle \cosh^2 x = \left(\frac{e^x + e^{-x}}{2}\right)^2 = \frac{e^{2x} + 2 + e^{-2x}}{4}$ |
| **Step 2** | $\displaystyle \sinh^2 x = \left(\frac{e^x - e^{-x}}{2}\right)^2 = \frac{e^{2x} - 2 + e^{-2x}}{4}$ |
| **Step 3** | Subtract: $\displaystyle \cosh^2 x - \sinh^2 x = \frac{(e^{2x} + 2 + e^{-2x}) - (e^{2x} - 2 + e^{-2x})}{4}$ |
| **Step 4** | Simplify: $\displaystyle = \frac{4}{4} = 1$ |

$$\boxed{\cosh^2 x - \sinh^2 x = 1} \quad\checkmark$$

---

### Worked Example 3 — Evaluating Exact Values (Easy)

> **Question:** Find the exact value of $\sinh(\ln 3)$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | $\displaystyle \sinh(\ln 3) = \frac{e^{\ln 3} - e^{-\ln 3}}{2}$ |
| **Step 2** | $e^{\ln 3} = 3$, and $e^{-\ln 3} = e^{\ln(1/3)} = \frac{1}{3}$ |
| **Step 3** | $\displaystyle \sinh(\ln 3) = \frac{3 - \frac{1}{3}}{2} = \frac{\frac{8}{3}}{2} = \frac{4}{3}$ |

$$\boxed{\sinh(\ln 3) = \frac{4}{3}} \quad\checkmark$$

---

### Worked Example 4 — Evaluating cosh (Easy)

> **Question:** Find the exact value of $\cosh\left(\ln\frac{5}{2}\right)$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | $\displaystyle \cosh\left(\ln\frac{5}{2}\right) = \frac{e^{\ln(5/2)} + e^{-\ln(5/2)}}{2}$ |
| **Step 2** | $\displaystyle e^{\ln(5/2)} = \frac{5}{2}$, and $\displaystyle e^{-\ln(5/2)} = e^{\ln(2/5)} = \frac{2}{5}$ |
| **Step 3** | $\displaystyle \cosh\left(\ln\frac{5}{2}\right) = \frac{\frac{5}{2} + \frac{2}{5}}{2} = \frac{\frac{25+4}{10}}{2} = \frac{29}{20}$ |

$$\boxed{\cosh\left(\ln\frac{5}{2}\right) = \frac{29}{20}} \quad\checkmark$$

---

# 4. Graphs of Hyperbolic Functions

## 4.1 Shape, Symmetry, and Asymptotes

### $y = \sinh x$
- **Odd function** (symmetric about origin)
- One-to-one mapping
- Domain: $\mathbb{R}$, Range: $\mathbb{R}$
- No asymptotes
- Shape: like a smooth "S" curve through origin

### $y = \cosh x$
- **Even function** (symmetric about $y$-axis)
- NOT one-to-one (need to restrict $x \ge 0$ for inverse)
- Domain: $\mathbb{R}$, Range: $y \ge 1$
- Minimum at $(0, 1)$
- Shape: "U" shape — the catenary

### $y = \tanh x$
- **Odd function**
- Domain: $\mathbb{R}$, Range: $-1 < y < 1$
- Horizontal asymptotes: $y = 1$ and $y = -1$
- Passes through $(0, 0)$
- Shape: flattened S-curve approaching asymptotes

### $y = \operatorname{sech} x$
- **Even function**
- Domain: $\mathbb{R}$, Range: $0 < y \le 1$
- Maximum at $(0, 1)$
- Horizontal asymptote: $y = 0$
- Shape: bell-shaped curve (models **soliton** waves)

### $y = \operatorname{cosech} x$
- **Odd function**
- Domain: $x \neq 0$, Range: $y \neq 0$
- Vertical asymptote: $x = 0$
- Horizontal asymptote: $y = 0$
- Shape: two branches in Q1 and Q3, like $y = 1/x$

### $y = \coth x$
- **Odd function**
- Domain: $x \neq 0$, Range: $y < -1$ or $y > 1$
- Vertical asymptote: $x = 0$
- Horizontal asymptotes: $y = 1$ and $y = -1$
- Shape: two branches approaching asymptotes

## 4.2 Summary Table

| Function | Symmetry | Domain | Range | Asymptotes |
|---|---|---|---|---|
| $\sinh x$ | Odd | $\mathbb{R}$ | $\mathbb{R}$ | None |
| $\cosh x$ | Even | $\mathbb{R}$ | $[1, \infty)$ | None |
| $\tanh x$ | Odd | $\mathbb{R}$ | $(-1, 1)$ | $y = \pm 1$ |
| $\operatorname{sech} x$ | Even | $\mathbb{R}$ | $(0, 1]$ | $y = 0$ |
| $\operatorname{cosech} x$ | Odd | $\mathbb{R}\setminus\{0\}$ | $\mathbb{R}\setminus\{0\}$ | $x = 0,\; y = 0$ |
| $\coth x$ | Odd | $\mathbb{R}\setminus\{0\}$ | $(-\infty, -1) \cup (1, \infty)$ | $x = 0,\; y = \pm 1$ |

---

### Worked Example 5 — Graph Transformation (Medium)

> **Question:** Sketch the graph of $y = |3\cosh(x + 1) - 4|$.

**Solution:**

| Step | Transformation | Effect on Graph |
|---|---|---|
| **Step 1** | Start with $f(x) = \cosh x$ | Minimum at $(0, 1)$ |
| **Step 2** | $y = f(x + 1)$ | Shift **left** by 1. Min moves to $(-1, 1)$ |
| **Step 3** | $y = 3f(x + 1)$ | Vertical stretch ×3. Min at $(-1, 3)$ |
| **Step 4** | $y = 3f(x + 1) - 4$ | Shift **down** by 4. Min at $(-1, -1)$ |
| **Step 5** | $y = |3f(x + 1) - 4|$ | Reflect negative part above $x$-axis. "W" shape with local max at $(-1, 1)$ |

**Final shape:** A "W"-shaped curve symmetric about $x = -1$, touching the $x$-axis at two points with a local maximum at $(-1, 1)$. $\checkmark$

---

### Worked Example 6 — Graph with Cosech (Medium)

> **Question:** Sketch the graph of $y = 4 - \operatorname{cosech}(x - 2)$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Start with $g(x) = \operatorname{cosech} x$ (odd, two branches, asymptotes at $x=0$, $y=0$) |
| **Step 2** | $y = \operatorname{cosech}(x - 2)$: shift **right** by 2. Vertical asymptote at $x = 2$ |
| **Step 3** | $y = 4 - \operatorname{cosech}(x - 2)$: reflect in $x$-axis and shift up by 4 |

**Final:** Two branches either side of $x = 2$, approaching $y = 4$ from below on the right and from above on the left. $\checkmark$

---

# 5. Hyperbolic Identities

## 5.1 The Fundamental Identity

$$\boxed{\cosh^2 x - \sinh^2 x \equiv 1}$$

This is the **most important** hyperbolic identity — the analogue of $\cos^2 x + \sin^2 x = 1$.

### Derived Identities

Dividing the fundamental identity:

| Operation | Result |
|---|---|
| Divide by $\cosh^2 x$ | $\boxed{1 - \tanh^2 x \equiv \operatorname{sech}^2 x}$ |
| Divide by $\sinh^2 x$ | $\boxed{\coth^2 x - 1 \equiv \operatorname{cosech}^2 x}$ |

## 5.2 Double Angle Formulas

$$\boxed{\sinh 2x \equiv 2\sinh x \cosh x}$$
$$\boxed{\cosh 2x \equiv \cosh^2 x + \sinh^2 x \equiv 2\cosh^2 x - 1 \equiv 1 + 2\sinh^2 x}$$

## 5.3 Addition Formulas

$$\boxed{\sinh(A + B) \equiv \sinh A \cosh B + \cosh A \sinh B}$$
$$\boxed{\sinh(A - B) \equiv \sinh A \cosh B - \cosh A \sinh B}$$
$$\boxed{\cosh(A + B) \equiv \cosh A \cosh B + \sinh A \sinh B}$$
$$\boxed{\cosh(A - B) \equiv \cosh A \cosh B - \sinh A \sinh B}$$

$$\boxed{\tanh(A + B) \equiv \frac{\tanh A + \tanh B}{1 + \tanh A \tanh B}}$$

## 5.4 Osborne's Rule

> **📌 Key Point:** To convert a trigonometric identity to a hyperbolic identity:
> 1. Replace $\cos$ with $\cosh$
> 2. Replace $\sin$ with $\sinh$
> 3. **Change the sign** wherever there is a **product of two $\sinh$ terms**

### Examples of Osborne's Rule

| Trig Identity | → Hyperbolic Identity | Sign Change? |
|---|---|---|
| $\cos^2 x + \sin^2 x = 1$ | $\cosh^2 x - \sinh^2 x = 1$ | Yes (product of 2 sinhs) |
| $\sin(A + B) = \sin A \cos B + \cos A \sin B$ | $\sinh(A + B) = \sinh A \cosh B + \cosh A \sinh B$ | No ($\sinh A \cosh B$ has only one sinh) |
| $\cos(A + B) = \cos A \cos B - \sin A \sin B$ | $\cosh(A + B) = \cosh A \cosh B + \sinh A \sinh B$ | Yes ($-\sin A \sin B \to +\sinh A \sinh B$) |
| $\tan(A + B) = \frac{\tan A + \tan B}{1 - \tan A \tan B}$ | $\tanh(A + B) = \frac{\tanh A + \tanh B}{1 + \tanh A \tanh B}$ | Yes ($1 - \tan A \tan B \to 1 + \tanh A \tanh B$) |

> **⚠️ Osborne's Rule is a memory aid, NOT a proof!** You still need to prove identities using exponential definitions.

---

### Worked Example 7 — Proving sinh(A + B) (Medium)

> **Question:** Prove that $\sinh(A + B) \equiv \sinh A \cosh B + \cosh A \sinh B$.

**Solution (using exponential forms):**

| Step | Operation |
|---|---|
| **Step 1** | Start with RHS: $\sinh A \cosh B + \cosh A \sinh B$ |
| **Step 2** | $\displaystyle = \left(\frac{e^A - e^{-A}}{2}\right)\left(\frac{e^B + e^{-B}}{2}\right) + \left(\frac{e^A + e^{-A}}{2}\right)\left(\frac{e^B - e^{-B}}{2}\right)$ |
| **Step 3** | $\displaystyle = \frac{1}{4}\left[(e^A - e^{-A})(e^B + e^{-B}) + (e^A + e^{-A})(e^B - e^{-B})\right]$ |
| **Step 4** | Expand: $\displaystyle = \frac{1}{4}\left[e^{A+B} + e^{A-B} - e^{-A+B} - e^{-A-B} + e^{A+B} - e^{A-B} + e^{-A+B} - e^{-A-B}\right]$ |
| **Step 5** | Cancel: $\displaystyle = \frac{1}{4}\left[2e^{A+B} - 2e^{-(A+B)}\right] = \frac{e^{A+B} - e^{-(A+B)}}{2}$ |
| **Step 6** | $\displaystyle = \sinh(A + B)$ LHS ✓ |

$$\boxed{\sinh(A + B) \equiv \sinh A \cosh B + \cosh A \sinh B} \quad\checkmark$$

---

### Worked Example 8 — Proving cosh(A - B) (Medium)

> **Question:** Prove that $\cosh(A - B) \equiv \cosh A \cosh B - \sinh A \sinh B$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | RHS $\displaystyle = \left(\frac{e^A + e^{-A}}{2}\right)\left(\frac{e^B + e^{-B}}{2}\right) - \left(\frac{e^A - e^{-A}}{2}\right)\left(\frac{e^B - e^{-B}}{2}\right)$ |
| **Step 2** | $\displaystyle = \frac{1}{4}\left[(e^A + e^{-A})(e^B + e^{-B}) - (e^A - e^{-A})(e^B - e^{-B})\right]$ |
| **Step 3** | Expand: $\displaystyle = \frac{1}{4}\left[e^{A+B} + e^{A-B} + e^{-A+B} + e^{-A-B} - (e^{A+B} - e^{A-B} - e^{-A+B} + e^{-A-B})\right]$ |
| **Step 4** | $\displaystyle = \frac{1}{4}\left[e^{A+B} + e^{A-B} + e^{-A+B} + e^{-A-B} - e^{A+B} + e^{A-B} + e^{-A+B} - e^{-A-B}\right]$ |
| **Step 5** | $\displaystyle = \frac{1}{4}\left[2e^{A-B} + 2e^{-(A-B)}\right] = \frac{e^{A-B} + e^{-(A-B)}}{2} = \cosh(A - B)$ |

$$\boxed{\cosh(A - B) \equiv \cosh A \cosh B - \sinh A \sinh B} \quad\checkmark$$

---

### Worked Example 9 — Using Osborne's Rule (Easy)

> **Question:** Using Osborne's rule, state the identity for $\tanh(A + B)$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Start with trig identity: $\displaystyle \tan(A + B) = \frac{\tan A + \tan B}{1 - \tan A \tan B}$ |
| **Step 2** | Replace $\tan$ with $\tanh$ everywhere |
| **Step 3** | Check for product of $\sinh$ terms: $\tanh A \tanh B = \frac{\sinh A}{\cosh A} \cdot \frac{\sinh B}{\cosh B}$ contains a product of $\sinh A \sinh B$ → sign changes |
| **Step 4** | The minus becomes plus: $\displaystyle \tanh(A + B) = \frac{\tanh A + \tanh B}{1 + \tanh A \tanh B}$ |

$$\boxed{\tanh(A + B) = \frac{\tanh A + \tanh B}{1 + \tanh A \tanh B}} \quad\checkmark$$

---

### Worked Example 10 — Triple Angle (Medium)

> **Question:** Prove that $\cosh 3x \equiv 4\cosh^3 x - 3\cosh x$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | $\cosh 3x = \cosh(2x + x) = \cosh 2x \cosh x + \sinh 2x \sinh x$ |
| **Step 2** | Use $\cosh 2x = 2\cosh^2 x - 1$ and $\sinh 2x = 2\sinh x \cosh x$ |
| **Step 3** | $\cosh 3x = (2\cosh^2 x - 1)\cosh x + (2\sinh x \cosh x)\sinh x$ |
| **Step 4** | $= 2\cosh^3 x - \cosh x + 2\sinh^2 x \cosh x$ |
| **Step 5** | Use $\sinh^2 x = \cosh^2 x - 1$: $= 2\cosh^3 x - \cosh x + 2(\cosh^2 x - 1)\cosh x$ |
| **Step 6** | $= 2\cosh^3 x - \cosh x + 2\cosh^3 x - 2\cosh x$ |
| **Step 7** | $= 4\cosh^3 x - 3\cosh x$ |

$$\boxed{\cosh 3x \equiv 4\cosh^3 x - 3\cosh x} \quad\checkmark$$

---

### Worked Example 11 — Proving with coth (Medium)

> **Question:** Prove that $\coth 2x - \coth x \equiv \frac{1}{2}(\tanh x - \coth x)$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Express $\coth 2x = \frac{1}{\tanh 2x} = \frac{1 + \tanh^2 x}{2\tanh x}$ (using $\tanh 2x = \frac{2\tanh x}{1 + \tanh^2 x}$) |
| **Step 2** | LHS $\displaystyle = \frac{1 + \tanh^2 x}{2\tanh x} - \frac{1}{\tanh x} = \frac{1 + \tanh^2 x - 2}{2\tanh x}$ |
| **Step 3** | $\displaystyle = \frac{\tanh^2 x - 1}{2\tanh x} = -\frac{1 - \tanh^2 x}{2\tanh x}$ |
| **Step 4** | Use $\operatorname{sech}^2 x = 1 - \tanh^2 x$: $\displaystyle = -\frac{\operatorname{sech}^2 x}{2\tanh x}$ |
| **Step 5** | $\displaystyle = -\frac{1}{2\tanh x \cosh^2 x} = -\frac{1}{2\sinh x \cosh x}$ |
| **Step 6** | $\displaystyle = -\frac{1}{\sinh 2x}$ |
| **Step 7** | Meanwhile RHS $\displaystyle = \frac{1}{2}\left(\frac{\sinh x}{\cosh x} - \frac{\cosh x}{\sinh x}\right) = \frac{1}{2}\left(\frac{\sinh^2 x - \cosh^2 x}{\sinh x \cosh x}\right) = -\frac{1}{2\sinh x \cosh x} = -\frac{1}{\sinh 2x}$ |

Both sides equal $-\frac{1}{\sinh 2x}$. Identity proved. $\checkmark$

---

### Worked Example 12 — Identity with sinh difference (Medium)

> **Question:** Prove that $\sinh A - \sinh B \equiv 2\cosh\left(\frac{A + B}{2}\right) \sinh\left(\frac{A - B}{2}\right)$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | RHS $\displaystyle = 2\left(\frac{e^{(A+B)/2} + e^{-(A+B)/2}}{2}\right)\left(\frac{e^{(A-B)/2} - e^{-(A-B)/2}}{2}\right)$ |
| **Step 2** | $\displaystyle = \frac{1}{2}\left(e^{(A+B)/2} + e^{-(A+B)/2}\right)\left(e^{(A-B)/2} - e^{-(A-B)/2}\right)$ |
| **Step 3** | Expand: $\displaystyle = \frac{1}{2}\left[e^{A} - e^{B} + e^{-B} - e^{-A}\right]$ |
| **Step 4** | $\displaystyle = \frac{e^{A} - e^{-A}}{2} - \frac{e^{B} - e^{-B}}{2} = \sinh A - \sinh B$ LHS ✓ |

$$\boxed{\sinh A - \sinh B \equiv 2\cosh\left(\frac{A + B}{2}\right) \sinh\left(\frac{A - B}{2}\right)} \quad\checkmark$$

---

# 6. Derivatives of Hyperbolic Functions

## 6.1 Derivative Table

| $y$ | $\displaystyle \frac{dy}{dx}$ |
|---|---|
| $\sinh x$ | $\cosh x$ |
| $\cosh x$ | $\sinh x$ ← **NO negative!** |
| $\tanh x$ | $\operatorname{sech}^2 x$ |
| $\operatorname{sech} x$ | $-\operatorname{sech} x \tanh x$ |
| $\operatorname{cosech} x$ | $-\operatorname{cosech} x \coth x$ |
| $\coth x$ | $-\operatorname{cosech}^2 x$ |

## 6.2 ⚠️ Critical Differences from Trigonometric Derivatives

| Trig $y$ | $\frac{dy}{dx}$ | Hyperbolic $y$ | $\frac{dy}{dx}$ | What Changed |
|---|---|---|---|---|
| $\sin x$ | $\cos x$ | $\sinh x$ | $\cosh x$ | Same (no change) |
| $\cos x$ | $-\sin x$ | $\cosh x$ | $+\sinh x$ | **No negative sign!** |
| $\tan x$ | $\sec^2 x$ | $\tanh x$ | $\operatorname{sech}^2 x$ | Same pattern |
| $\sec x$ | $\sec x \tan x$ | $\operatorname{sech} x$ | $-\operatorname{sech} x \tanh x$ | **Extra negative!** |

> **🎯 #1 Trap:** $\displaystyle \frac{d}{dx}(\cosh x) = +\sinh x$ (NOT $-\sinh x$ like $\cos x$)

## 6.3 Derivations from Exponential Definitions

### Derivation of $\frac{d}{dx}(\sinh x)$

$$\frac{d}{dx}(\sinh x) = \frac{d}{dx}\left(\frac{e^x - e^{-x}}{2}\right) = \frac{e^x - (-e^{-x})}{2} = \frac{e^x + e^{-x}}{2} = \cosh x \quad\checkmark$$

### Derivation of $\frac{d}{dx}(\cosh x)$

$$\frac{d}{dx}(\cosh x) = \frac{d}{dx}\left(\frac{e^x + e^{-x}}{2}\right) = \frac{e^x + (-e^{-x})}{2} = \frac{e^x - e^{-x}}{2} = \sinh x \quad\checkmark$$

### Derivation of $\frac{d}{dx}(\tanh x)$

$$\frac{d}{dx}(\tanh x) = \frac{d}{dx}\left(\frac{\sinh x}{\cosh x}\right)$$

Using quotient rule:

$$\frac{d}{dx}(\tanh x) = \frac{\cosh x \cdot \cosh x - \sinh x \cdot \sinh x}{\cosh^2 x} = \frac{\cosh^2 x - \sinh^2 x}{\cosh^2 x} = \frac{1}{\cosh^2 x} = \operatorname{sech}^2 x \quad\checkmark$$

---

### Worked Example 13 — Chain Rule (Easy)

> **Question:** $y = \sinh(3x + 2)$. Find $\frac{dy}{dx}$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Inner function: $u = 3x + 2$, outer: $y = \sinh u$ |
| **Step 2** | $\displaystyle \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = \cosh u \cdot 3$ |
| **Step 3** | Substitute back: $\displaystyle \frac{dy}{dx} = 3\cosh(3x + 2)$ |

$$\boxed{\frac{dy}{dx} = 3\cosh(3x + 2)} \quad\checkmark$$

---

### Worked Example 14 — Power of Hyperbolic (Easy)

> **Question:** $y = \sinh^2 x$. Find $\frac{dy}{dx}$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Write $y = (\sinh x)^2$ |
| **Step 2** | Chain rule: $\displaystyle \frac{dy}{dx} = 2\sinh x \cdot \cosh x$ |
| **Step 3** | Simplify: $\displaystyle \frac{dy}{dx} = 2\sinh x \cosh x = \sinh 2x$ |

$$\boxed{\frac{dy}{dx} = \sinh 2x} \quad\checkmark$$

---

### Worked Example 15 — Product Rule (Medium)

> **Question:** $y = x^2 \cosh x$. Find $\frac{dy}{dx}$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Product rule: $u = x^2$, $v = \cosh x$ |
| **Step 2** | $u' = 2x$, $v' = \sinh x$ |
| **Step 3** | $\displaystyle \frac{dy}{dx} = 2x \cdot \cosh x + x^2 \cdot \sinh x$ |

$$\boxed{\frac{dy}{dx} = 2x\cosh x + x^2\sinh x} \quad\checkmark$$

---

### Worked Example 16 — Sech Differentiation (Medium)

> **Question:** $y = \operatorname{sech}(2x)$. Find $\frac{dy}{dx}$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | $\displaystyle y = \operatorname{sech}(2x) = \frac{1}{\cosh(2x)}$ |
| **Step 2** | Chain rule: $\displaystyle \frac{dy}{dx} = -\operatorname{sech}(2x)\tanh(2x) \cdot 2$ (using formula $\frac{d}{dx}\operatorname{sech} x = -\operatorname{sech} x \tanh x$) |
| **Step 3** | $\displaystyle \frac{dy}{dx} = -2\operatorname{sech}(2x)\tanh(2x)$ |

$$\boxed{\frac{dy}{dx} = -2\operatorname{sech}(2x)\tanh(2x)} \quad\checkmark$$

---

### Worked Example 17 — Logarithm + Hyperbolic (Medium)

> **Question:** $y = \ln(\cosh x)$. Find $\frac{dy}{dx}$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | $\displaystyle \frac{dy}{dx} = \frac{1}{\cosh x} \cdot \sinh x$ |
| **Step 2** | $\displaystyle \frac{dy}{dx} = \frac{\sinh x}{\cosh x} = \tanh x$ |

$$\boxed{\frac{dy}{dx} = \tanh x} \quad\checkmark$$

---

### Worked Example 18 — Coth Differentiation (Medium)

> **Question:** $y = \coth(1 - 3x)$. Find $\frac{dy}{dx}$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Using $\frac{d}{dx}(\coth x) = -\operatorname{cosech}^2 x$ |
| **Step 2** | Chain rule: $\displaystyle \frac{dy}{dx} = -\operatorname{cosech}^2(1 - 3x) \cdot (-3)$ |
| **Step 3** | $\displaystyle \frac{dy}{dx} = 3\operatorname{cosech}^2(1 - 3x)$ |

$$\boxed{\frac{dy}{dx} = 3\operatorname{cosech}^2(1 - 3x)} \quad\checkmark$$

---

### Worked Example 19 — Product and Chain (Hard)

> **Question:** $y = \cosh 3x \cdot \sinh 4x$. Find $\frac{dy}{dx}$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Product rule: $u = \cosh 3x$, $v = \sinh 4x$ |
| **Step 2** | $u' = 3\sinh 3x$, $v' = 4\cosh 4x$ |
| **Step 3** | $\displaystyle \frac{dy}{dx} = 3\sinh 3x \cdot \sinh 4x + \cosh 3x \cdot 4\cosh 4x$ |

$$\boxed{\frac{dy}{dx} = 3\sinh 3x \sinh 4x + 4\cosh 3x \cosh 4x} \quad\checkmark$$

---

### Worked Example 20 — Implicit with Hyperbolic (Hard)

> **Question:** $\sinh(x + y) = yx^3$. Find $\frac{dy}{dx}$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Differentiate implicitly: $\displaystyle \cosh(x + y) \cdot \left(1 + \frac{dy}{dx}\right) = y \cdot 3x^2 + x^3 \cdot \frac{dy}{dx}$ |
| **Step 2** | Expand: $\displaystyle \cosh(x+y) + \cosh(x+y)\frac{dy}{dx} = 3x^2 y + x^3\frac{dy}{dx}$ |
| **Step 3** | Collect $\frac{dy}{dx}$ terms: $\displaystyle \cosh(x+y)\frac{dy}{dx} - x^3\frac{dy}{dx} = 3x^2 y - \cosh(x+y)$ |
| **Step 4** | Factor: $\displaystyle \frac{dy}{dx}(\cosh(x+y) - x^3) = 3x^2 y - \cosh(x+y)$ |
| **Step 5** | Divide: $\displaystyle \frac{dy}{dx} = \frac{3x^2 y - \cosh(x+y)}{\cosh(x+y) - x^3}$ |

$$\boxed{\frac{dy}{dx} = \frac{3x^2 y - \cosh(x+y)}{\cosh(x+y) - x^3}} \quad\checkmark$$

---

# 7. Inverse Hyperbolic Functions

## 7.1 Why Inverses Exist

- $\sinh x$ is **one-to-one** over $\mathbb{R}$ → $\sinh^{-1} x$ exists with domain $\mathbb{R}$
- $\cosh x$ is **not one-to-one** → we restrict to $x \ge 0$ → $\cosh^{-1} x$ valid for $x \ge 1$
- $\tanh x$ is **one-to-one** over $\mathbb{R}$ → $\tanh^{-1} x$ valid for $-1 < x < 1$

## 7.2 Domain and Range

| Inverse Function | Domain | Range |
|---|---|---|
| $\sinh^{-1} x$ | $\mathbb{R}$ | $\mathbb{R}$ |
| $\cosh^{-1} x$ | $x \ge 1$ | $y \ge 0$ |
| $\tanh^{-1} x$ | $-1 < x < 1$ | $\mathbb{R}$ |

> **📌 Notation:** $\sinh^{-1} x$ is also written as $\operatorname{arsinh} x$ (area hyperbolic sine). The "arc" prefix from trig becomes "ar" (area) for hyperbolics.

---

# 8. Logarithmic Forms of Inverse Hyperbolic Functions

## 8.1 Key Point 19.4 — Complete Table

| Inverse Function | Logarithmic Form |
|---|---|
| $\sinh^{-1} x$ | $\displaystyle \ln(x + \sqrt{x^2 + 1})$ |
| $\cosh^{-1} x$ | $\displaystyle \ln(x + \sqrt{x^2 - 1})$ |
| $\tanh^{-1} x$ | $\displaystyle \frac{1}{2}\ln\left(\frac{1 + x}{1 - x}\right)$ |
| $\coth^{-1} x$ | $\displaystyle \frac{1}{2}\ln\left(\frac{x + 1}{x - 1}\right)$ |
| $\operatorname{sech}^{-1} x$ | $\displaystyle \ln\left(\frac{1 + \sqrt{1 - x^2}}{x}\right)$ |
| $\operatorname{cosech}^{-1} x$ | $\displaystyle \ln\left(\frac{1 + \sqrt{1 + x^2}}{x}\right)$ |

> **📌 You must be able to DERIVE the logarithmic form for $\sinh^{-1} x$, $\cosh^{-1} x$, and $\tanh^{-1} x$.**

---

### Worked Example 21 — Deriving Logarithmic Form of sinh⁻¹ (Medium)

> **Question:** Derive the logarithmic form of $\sinh^{-1} x$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Let $y = \sinh^{-1} x$, so $\sinh y = x$ |
| **Step 2** | $\displaystyle \frac{e^y - e^{-y}}{2} = x$ |
| **Step 3** | Multiply by $2e^y$: $e^{2y} - 1 = 2xe^y$ |
| **Step 4** | Rearrange: $e^{2y} - 2xe^y - 1 = 0$ |
| **Step 5** | Complete the square: $(e^y - x)^2 = x^2 + 1$ |
| **Step 6** | Take positive root (since $e^y > 0$): $e^y = x + \sqrt{x^2 + 1}$ |
| **Step 7** | Take logs: $y = \ln(x + \sqrt{x^2 + 1})$ |

$$\boxed{\sinh^{-1} x = \ln(x + \sqrt{x^2 + 1})} \quad\checkmark$$

---

### Worked Example 22 — Deriving Logarithmic Form of tanh⁻¹ (Medium)

> **Question:** Derive the logarithmic form of $\tanh^{-1} x$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Let $y = \tanh^{-1} x$, so $\tanh y = x$ |
| **Step 2** | $\displaystyle \frac{e^y - e^{-y}}{e^y + e^{-y}} = x$ |
| **Step 3** | Cross-multiply: $e^y - e^{-y} = x(e^y + e^{-y})$ |
| **Step 4** | Multiply by $e^y$: $e^{2y} - 1 = x(e^{2y} + 1)$ |
| **Step 5** | Expand: $e^{2y} - 1 = xe^{2y} + x$ |
| **Step 6** | Collect $e^{2y}$ terms: $e^{2y} - xe^{2y} = 1 + x$ |
| **Step 7** | Factor: $e^{2y}(1 - x) = 1 + x$ |
| **Step 8** | Solve: $e^{2y} = \frac{1 + x}{1 - x}$ |
| **Step 9** | Take logs: $\displaystyle 2y = \ln\left(\frac{1 + x}{1 - x}\right)$, so $\displaystyle y = \frac{1}{2}\ln\left(\frac{1 + x}{1 - x}\right)$ |

$$\boxed{\tanh^{-1} x = \frac{1}{2}\ln\left(\frac{1 + x}{1 - x}\right)} \quad\checkmark$$

---

# 9. Derivatives of Inverse Hyperbolic Functions

## 9.1 Derivative Table

| $y$ | $\displaystyle \frac{dy}{dx}$ | Domain |
|---|---|---|
| $\sinh^{-1} x$ | $\displaystyle \frac{1}{\sqrt{1 + x^2}}$ | All $x$ |
| $\cosh^{-1} x$ | $\displaystyle \frac{1}{\sqrt{x^2 - 1}}$ | $x > 1$ |
| $\tanh^{-1} x$ | $\displaystyle \frac{1}{1 - x^2}$ | $-1 < x < 1$ |

## 9.2 ⚠️ Key Differences from Inverse Trig Derivatives

| Inverse Trig | Derivative | Inverse Hyperbolic | Derivative |
|---|---|---|---|
| $\sin^{-1} x$ | $\displaystyle \frac{1}{\sqrt{1 - x^2}}$ | $\sinh^{-1} x$ | $\displaystyle \frac{1}{\sqrt{1 + x^2}}$ ← **PLUS** |
| $\cos^{-1} x$ | $\displaystyle -\frac{1}{\sqrt{1 - x^2}}$ | $\cosh^{-1} x$ | $\displaystyle \frac{1}{\sqrt{x^2 - 1}}$ |
| $\tan^{-1} x$ | $\displaystyle \frac{1}{1 + x^2}$ | $\tanh^{-1} x$ | $\displaystyle \frac{1}{1 - x^2}$ ← **MINUS** |

> **🎯 The $\sinh^{-1}$ and $\tanh^{-1}$ derivatives are SWAPPED compared to their trig counterparts!**

---

### Worked Example 23 — Derivative of sinh⁻¹ from First Principles (Hard)

> **Question:** Given that $y = \sinh^{-1} x$, show that $\frac{dy}{dx} = \frac{1}{\sqrt{1 + x^2}}$.

**Solution (Method 1 — from logarithmic form):**

| Step | Operation |
|---|---|
| **Step 1** | $y = \ln(x + \sqrt{1 + x^2})$ |
| **Step 2** | $\displaystyle \frac{dy}{dx} = \frac{1}{x + \sqrt{1 + x^2}} \cdot \frac{d}{dx}\left(x + \sqrt{1 + x^2}\right)$ |
| **Step 3** | $\displaystyle \frac{dy}{dx} = \frac{1}{x + \sqrt{1 + x^2}} \cdot \left(1 + \frac{2x}{2\sqrt{1 + x^2}}\right)$ |
| **Step 4** | $\displaystyle \frac{dy}{dx} = \frac{1}{x + \sqrt{1 + x^2}} \cdot \left(\frac{\sqrt{1 + x^2} + x}{\sqrt{1 + x^2}}\right)$ |
| **Step 5** | Cancel: $\displaystyle \frac{dy}{dx} = \frac{1}{\sqrt{1 + x^2}}$ |

$$\boxed{\frac{dy}{dx} = \frac{1}{\sqrt{1 + x^2}}} \quad\checkmark$$

---

### Worked Example 24 — Chain Rule with cosh⁻¹ (Medium)

> **Question:** $y = \cosh^{-1}(2x)$. Find $\frac{dy}{dx}$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Inner: $u = 2x$, using $\frac{d}{dx}\cosh^{-1} x = \frac{1}{\sqrt{x^2 - 1}}$ |
| **Step 2** | $\displaystyle \frac{dy}{dx} = \frac{1}{\sqrt{(2x)^2 - 1}} \cdot 2$ |
| **Step 3** | $\displaystyle \frac{dy}{dx} = \frac{2}{\sqrt{4x^2 - 1}}$ |

Domain: $2x > 1 \Rightarrow x > \frac{1}{2}$.

$$\boxed{\frac{dy}{dx} = \frac{2}{\sqrt{4x^2 - 1}}} \quad\checkmark$$

---

### Worked Example 25 — Chain Rule with tanh⁻¹ (Medium)

> **Question:** $y = \tanh^{-1}(x^2)$. Find $\frac{dy}{dx}$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Inner: $u = x^2$, using $\frac{d}{dx}\tanh^{-1} x = \frac{1}{1 - x^2}$ |
| **Step 2** | $\displaystyle \frac{dy}{dx} = \frac{1}{1 - (x^2)^2} \cdot 2x$ |
| **Step 3** | $\displaystyle \frac{dy}{dx} = \frac{2x}{1 - x^4}$ |

Domain: $-1 < x^2 < 1 \Rightarrow -1 < x < 1$.

$$\boxed{\frac{dy}{dx} = \frac{2x}{1 - x^4}} \quad\checkmark$$

---

### Worked Example 26 — Implicit Differentiation with sinh⁻¹ (Hard)

> **Question:** $y = x \cdot \sinh^{-1} x$. Find $\frac{dy}{dx}$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Product rule: $u = x$, $v = \sinh^{-1} x$ |
| **Step 2** | $u' = 1$, $\displaystyle v' = \frac{1}{\sqrt{1 + x^2}}$ |
| **Step 3** | $\displaystyle \frac{dy}{dx} = 1 \cdot \sinh^{-1} x + x \cdot \frac{1}{\sqrt{1 + x^2}}$ |

$$\boxed{\frac{dy}{dx} = \sinh^{-1} x + \frac{x}{\sqrt{1 + x^2}}} \quad\checkmark$$

---

# 10. Solving Hyperbolic Equations

## 10.1 Methods Summary

| Equation Type | Method | Example |
|---|---|---|
| Linear combination $a\cosh x + b\sinh x = c$ | Convert to exponentials, then solve quadratic in $e^x$ | $4\cosh x - 3\sinh x = 4$ |
| Quadratic in $\tanh x$ | Substitute $T = \tanh x$, solve, check range | $3\tanh^2 x - 4\tanh x = 4$ |
| Quadratic in $\sinh x$ or $\cosh x$ | Factor or use identity to rewrite in one function | $\sinh^2 x - 5\sinh x + 4 = 0$ |
| Using inverse functions | Identify the hyperbolic value, apply inverse with logarithmic form | $\sinh x = 4 \Rightarrow x = \sinh^{-1} 4$ |
| Using identities | Rewrite using $\cosh^2 x - \sinh^2 x = 1$ or double-angle formulas | $\cosh 2x + \sinh x = 5$ |

### Step-by-Step: Solving $a\cosh x + b\sinh x = c$

| Step | What To Do |
|---|---|
| **Step 1** | Replace $\cosh x = \frac{e^x + e^{-x}}{2}$, $\sinh x = \frac{e^x - e^{-x}}{2}$ |
| **Step 2** | Multiply both sides by 2 |
| **Step 3** | Collect $e^x$ and $e^{-x}$ terms |
| **Step 4** | Multiply through by $e^x$ to form a quadratic in $e^x$ |
| **Step 5** | Solve the quadratic (factor or formula) |
| **Step 6** | Take natural logs: $x = \ln(\text{positive root})$ |

> **⚠️ Check your solutions!** $e^x$ must be positive. Discard any negative roots.

---

### Worked Example 27 — Solving Linear Combination (Medium)

> **Question:** Solve $4\cosh x - 3\sinh x = 4$, leaving answer in exact form.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | $\displaystyle 4\left(\frac{e^x + e^{-x}}{2}\right) - 3\left(\frac{e^x - e^{-x}}{2}\right) = 4$ |
| **Step 2** | Multiply by 2: $4(e^x + e^{-x}) - 3(e^x - e^{-x}) = 8$ |
| **Step 3** | Expand: $4e^x + 4e^{-x} - 3e^x + 3e^{-x} = 8$ |
| **Step 4** | Simplify: $e^x + 7e^{-x} = 8$ |
| **Step 5** | Multiply by $e^x$: $e^{2x} + 7 = 8e^x$ |
| **Step 6** | Rearrange: $e^{2x} - 8e^x + 7 = 0$ |
| **Step 7** | Factor: $(e^x - 7)(e^x - 1) = 0$ |
| **Step 8** | Solve: $e^x = 7$ or $e^x = 1$ |
| **Step 9** | Take logs: $x = \ln 7$ or $x = \ln 1 = 0$ |

Both are valid (positive). 

$$\boxed{x = 0,\; x = \ln 7} \quad\checkmark$$

---

### Worked Example 28 — Solving Quadratic in tanh (Medium)

> **Question:** Solve $3\tanh^2 x - 4\tanh x = 4$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Rearrange: $3\tanh^2 x - 4\tanh x - 4 = 0$ |
| **Step 2** | Let $T = \tanh x$: $3T^2 - 4T - 4 = 0$ |
| **Step 3** | Factor: $(3T + 2)(T - 2) = 0$ |
| **Step 4** | $T = -\frac{2}{3}$ or $T = 2$ |
| **Step 5** | Check range: $-1 < \tanh x < 1$, so $T = 2$ is **invalid** |
| **Step 6** | $\tanh x = -\frac{2}{3}$ |
| **Step 7** | $\displaystyle x = \tanh^{-1}\left(-\frac{2}{3}\right)$ |

$$\boxed{x = \tanh^{-1}\left(-\frac{2}{3}\right)} \quad\checkmark$$

(Can also be expressed as $\displaystyle x = \frac{1}{2}\ln\left(\frac{1 - 2/3}{1 + 2/3}\right) = \frac{1}{2}\ln\left(\frac{1/3}{5/3}\right) = \frac{1}{2}\ln\left(\frac{1}{5}\right)$)

---

### Worked Example 29 — Solving Quadratic in sinh (Medium)

> **Question:** Solve $\sinh^2 x - 5\sinh x + 4 = 0$. Give answers in exact logarithmic form.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Factor: $(\sinh x - 4)(\sinh x - 1) = 0$ |
| **Step 2** | $\sinh x = 4$ or $\sinh x = 1$ |
| **Step 3** | $\sinh^{-1} 4 = \ln(4 + \sqrt{4^2 + 1}) = \ln(4 + \sqrt{17})$ |
| **Step 4** | $\sinh^{-1} 1 = \ln(1 + \sqrt{1^2 + 1}) = \ln(1 + \sqrt{2})$ |

$$\boxed{x = \ln(4 + \sqrt{17}),\; x = \ln(1 + \sqrt{2})} \quad\checkmark$$

---

### Worked Example 30 — Using Identities to Solve (Hard)

> **Question:** Solve $4\cosh^2 x = 10\sinh x + 3$, giving answers in exact logarithmic form.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Use $\cosh^2 x = 1 + \sinh^2 x$: $4(1 + \sinh^2 x) = 10\sinh x + 3$ |
| **Step 2** | Expand: $4 + 4\sinh^2 x = 10\sinh x + 3$ |
| **Step 3** | Rearrange: $4\sinh^2 x - 10\sinh x + 1 = 0$ |
| **Step 4** | Let $S = \sinh x$: $4S^2 - 10S + 1 = 0$ |
| **Step 5** | Quadratic formula: $\displaystyle S = \frac{10 \pm \sqrt{100 - 16}}{8} = \frac{10 \pm \sqrt{84}}{8} = \frac{10 \pm 2\sqrt{21}}{8} = \frac{5 \pm \sqrt{21}}{4}$ |
| **Step 6** | Both positive — valid. $x = \sinh^{-1}\left(\frac{5 + \sqrt{21}}{4}\right)$ or $x = \sinh^{-1}\left(\frac{5 - \sqrt{21}}{4}\right)$ |
| **Step 7** | $\displaystyle x = \ln\left(\frac{5 + \sqrt{21}}{4} + \sqrt{\left(\frac{5 + \sqrt{21}}{4}\right)^2 + 1}\right)$ and similar for the second root |

$$\boxed{x = \sinh^{-1}\left(\frac{5 \pm \sqrt{21}}{4}\right)} \quad\checkmark$$

---

### Worked Example 31 — Solving with cosech and coth (Hard)

> **Question:** Solve $\operatorname{cosech} x - 2\coth x = 2$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Write in exponentials: $\displaystyle \frac{2}{e^x - e^{-x}} - 2\left(\frac{e^x + e^{-x}}{e^x - e^{-x}}\right) = 2$ |
| **Step 2** | Combine: $\displaystyle \frac{2 - 2(e^x + e^{-x})}{e^x - e^{-x}} = 2$ |
| **Step 3** | Cross-multiply: $2 - 2(e^x + e^{-x}) = 2(e^x - e^{-x})$ |
| **Step 4** | Divide by 2: $1 - (e^x + e^{-x}) = e^x - e^{-x}$ |
| **Step 5** | Simplify: $1 - e^x - e^{-x} = e^x - e^{-x}$ |
| **Step 6** | $1 - e^x = e^x$ |
| **Step 7** | $1 = 2e^x \Rightarrow e^x = \frac{1}{2}$ |
| **Step 8** | $x = \ln\frac{1}{2} = -\ln 2$ |

Check: $x = -\ln 2$ is valid (not zero).

$$\boxed{x = -\ln 2} \quad\checkmark$$

---

### Worked Example 32 — Solving with sech (Hard)

> **Question:** Given that $\operatorname{sech}^{-1} x = \ln\left(\frac{1 + \sqrt{1 - x^2}}{x}\right)$, solve $4\operatorname{sech} x - 3\tanh^2 x = 1$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Use $\tanh^2 x = 1 - \operatorname{sech}^2 x$: $4\operatorname{sech} x - 3(1 - \operatorname{sech}^2 x) = 1$ |
| **Step 2** | $4\operatorname{sech} x - 3 + 3\operatorname{sech}^2 x = 1$ |
| **Step 3** | $3\operatorname{sech}^2 x + 4\operatorname{sech} x - 4 = 0$ |
| **Step 4** | Let $S = \operatorname{sech} x$: $3S^2 + 4S - 4 = 0$ |
| **Step 5** | $(3S - 2)(S + 2) = 0$ |
| **Step 6** | $S = \frac{2}{3}$ or $S = -2$ |
| **Step 7** | Range of $\operatorname{sech} x$ is $0 < \operatorname{sech} x \le 1$, so $S = -2$ is **invalid** |
| **Step 8** | $\operatorname{sech} x = \frac{2}{3}$ |
| **Step 9** | $\displaystyle x = \operatorname{sech}^{-1}\left(\frac{2}{3}\right) = \ln\left(\frac{1 + \sqrt{1 - (2/3)^2}}{2/3}\right) = \ln\left(\frac{1 + \sqrt{5/9}}{2/3}\right) = \ln\left(\frac{1 + \frac{\sqrt{5}}{3}}{2/3}\right)$ |
| **Step 10** | $\displaystyle x = \ln\left(\frac{(3 + \sqrt{5})/3}{2/3}\right) = \ln\left(\frac{3 + \sqrt{5}}{2}\right)$ |

$$\boxed{x = \ln\left(\frac{3 + \sqrt{5}}{2}\right)} \quad\checkmark$$

---

# 11. Integration of Hyperbolic Functions

## 11.1 Standard Integrals

| Integrand | Integral |
|---|---|
| $\sinh x$ | $\cosh x + C$ |
| $\cosh x$ | $\sinh x + C$ |
| $\tanh x$ | $\ln(\cosh x) + C$ |
| $\coth x$ | $\ln(\sinh x) + C$ |
| $\operatorname{sech} x$ | $\tan^{-1}(\sinh x) + C$ or $2\tan^{-1}(e^x) + C$ |
| $\operatorname{cosech} x$ | $\ln\left|\tanh\frac{x}{2}\right| + C$ or $-\operatorname{coth}^{-1}(\cosh x) + C$ |
| $\operatorname{sech}^2 x$ | $\tanh x + C$ |
| $\operatorname{cosech}^2 x$ | $-\coth x + C$ |
| $\operatorname{sech} x \tanh x$ | $-\operatorname{sech} x + C$ |
| $\operatorname{cosech} x \coth x$ | $-\operatorname{cosech} x + C$ |

## 11.2 Integrals Leading to Inverse Hyperbolic Functions

| Integrand | Integral | Condition |
|---|---|---|
| $\displaystyle \frac{1}{\sqrt{a^2 + x^2}}$ | $\displaystyle \sinh^{-1}\left(\frac{x}{a}\right) + C$ | $a > 0$ |
| $\displaystyle \frac{1}{\sqrt{x^2 - a^2}}$ | $\displaystyle \cosh^{-1}\left(\frac{x}{a}\right) + C$ | $x > a > 0$ |
| $\displaystyle \frac{1}{a^2 - x^2}$ | $\displaystyle \frac{1}{a}\tanh^{-1}\left(\frac{x}{a}\right) + C$ | $|x| < a$ |

> **📌 Cambridge often tests these as recognition integrals — you must spot the form quickly.**

---

### Worked Example 33 — Basic Integration (Easy)

> **Question:** Find $\displaystyle \int \sinh 3x \, dx$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Standard: $\int \sinh(kx)\,dx = \frac{1}{k}\cosh(kx) + C$ |
| **Step 2** | $\displaystyle \int \sinh 3x \, dx = \frac{1}{3}\cosh 3x + C$ |

$$\boxed{\int \sinh 3x \, dx = \frac{1}{3}\cosh 3x + C} \quad\checkmark$$

---

### Worked Example 34 — Integrating tanh (Medium)

> **Question:** Find $\displaystyle \int \tanh x \, dx$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | $\displaystyle \int \tanh x \, dx = \int \frac{\sinh x}{\cosh x} \, dx$ |
| **Step 2** | Let $u = \cosh x$, $du = \sinh x \, dx$ |
| **Step 3** | $\displaystyle \int \frac{1}{u} \, du = \ln|u| + C$ |
| **Step 4** | Back-substitute: $\ln(\cosh x) + C$ (since $\cosh x > 0$, no absolute needed) |

$$\boxed{\int \tanh x \, dx = \ln(\cosh x) + C} \quad\checkmark$$

---

### Worked Example 35 — Inverse Hyperbolic Integration (Medium)

> **Question:** Find $\displaystyle \int \frac{1}{\sqrt{9 + x^2}} \, dx$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Write in form $\displaystyle \frac{1}{\sqrt{a^2 + x^2}}$ with $a = 3$ |
| **Step 2** | $\displaystyle \int \frac{1}{\sqrt{9 + x^2}} \, dx = \sinh^{-1}\left(\frac{x}{3}\right) + C$ |

$$\boxed{\int \frac{1}{\sqrt{9 + x^2}} \, dx = \sinh^{-1}\left(\frac{x}{3}\right) + C} \quad\checkmark$$

---

### Worked Example 36 — Completing the Square (Hard)

> **Question:** Find $\displaystyle \int \frac{1}{\sqrt{x^2 + 4x + 13}} \, dx$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Complete the square: $x^2 + 4x + 13 = (x+2)^2 + 9$ |
| **Step 2** | $\displaystyle \int \frac{1}{\sqrt{(x+2)^2 + 9}} \, dx$ |
| **Step 3** | Let $u = x+2$, $du = dx$ |
| **Step 4** | $\displaystyle \int \frac{1}{\sqrt{u^2 + 9}} \, du = \sinh^{-1}\left(\frac{u}{3}\right) + C$ |
| **Step 5** | Back-substitute: $\displaystyle \sinh^{-1}\left(\frac{x+2}{3}\right) + C$ |

$$\boxed{\int \frac{1}{\sqrt{x^2 + 4x + 13}} \, dx = \sinh^{-1}\left(\frac{x+2}{3}\right) + C} \quad\checkmark$$

---

### Worked Example 37 — Using tanh⁻¹ Integration (Medium)

> **Question:** Find $\displaystyle \int_{0}^{1/2} \frac{1}{1 - x^2} \, dx$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | $\displaystyle \int \frac{1}{1 - x^2} \, dx = \tanh^{-1} x + C$ for $|x| < 1$ |
| **Step 2** | $\displaystyle \int_{0}^{1/2} \frac{1}{1 - x^2} \, dx = \left[\tanh^{-1} x\right]_{0}^{1/2}$ |
| **Step 3** | $\displaystyle = \tanh^{-1}\left(\frac{1}{2}\right) - \tanh^{-1}(0) = \frac{1}{2}\ln\left(\frac{1 + 1/2}{1 - 1/2}\right) - 0$ |
| **Step 4** | $\displaystyle = \frac{1}{2}\ln\left(\frac{3/2}{1/2}\right) = \frac{1}{2}\ln 3$ |

$$\boxed{\int_{0}^{1/2} \frac{1}{1 - x^2} \, dx = \frac{1}{2}\ln 3} \quad\checkmark$$

---

### Worked Example 38 — cosh² Integration (Medium)

> **Question:** Find $\displaystyle \int \cosh^2 x \, dx$.

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Use identity: $\cosh 2x = 2\cosh^2 x - 1 \;\Rightarrow\; \cosh^2 x = \frac{1}{2}(\cosh 2x + 1)$ |
| **Step 2** | $\displaystyle \int \cosh^2 x \, dx = \frac{1}{2}\int (\cosh 2x + 1) \, dx$ |
| **Step 3** | $\displaystyle = \frac{1}{2}\left(\frac{1}{2}\sinh 2x + x\right) + C$ |
| **Step 4** | $\displaystyle = \frac{1}{4}\sinh 2x + \frac{x}{2} + C$ |

$$\boxed{\int \cosh^2 x \, dx = \frac{1}{4}\sinh 2x + \frac{x}{2} + C} \quad\checkmark$$

---

# 12. Complete Formula Sheet

## Definitions

$$\sinh x = \frac{e^x - e^{-x}}{2} \qquad \cosh x = \frac{e^x + e^{-x}}{2}$$
$$\tanh x = \frac{e^x - e^{-x}}{e^x + e^{-x}} \qquad \operatorname{sech} x = \frac{2}{e^x + e^{-x}}$$
$$\operatorname{cosech} x = \frac{2}{e^x - e^{-x}} \qquad \coth x = \frac{e^x + e^{-x}}{e^x - e^{-x}}$$

## Key Relationship

$$e^x = \cosh x + \sinh x \qquad e^{-x} = \cosh x - \sinh x$$

## Fundamental Identity

$$\cosh^2 x - \sinh^2 x = 1$$
$$1 - \tanh^2 x = \operatorname{sech}^2 x$$
$$\coth^2 x - 1 = \operatorname{cosech}^2 x$$

## Double Angle

$$\sinh 2x = 2\sinh x \cosh x$$
$$\cosh 2x = \cosh^2 x + \sinh^2 x = 2\cosh^2 x - 1 = 1 + 2\sinh^2 x$$

## Addition Formulas

| Formula | |
|---|---|
| $\sinh(A \pm B) = \sinh A \cosh B \pm \cosh A \sinh B$ | |
| $\cosh(A \pm B) = \cosh A \cosh B \pm \sinh A \sinh B$ | (note: $\pm$ on RHS is $+$ for $+$, $-$ for $-$) |
| $\displaystyle \tanh(A \pm B) = \frac{\tanh A \pm \tanh B}{1 \pm \tanh A \tanh B}$ | |

## Derivatives

$$\frac{d}{dx}(\sinh x) = \cosh x \quad \frac{d}{dx}(\cosh x) = \sinh x$$
$$\frac{d}{dx}(\tanh x) = \operatorname{sech}^2 x \quad \frac{d}{dx}(\coth x) = -\operatorname{cosech}^2 x$$
$$\frac{d}{dx}(\operatorname{sech} x) = -\operatorname{sech} x \tanh x \quad \frac{d}{dx}(\operatorname{cosech} x) = -\operatorname{cosech} x \coth x$$

## Inverse Hyperbolic Derivatives

$$\frac{d}{dx}(\sinh^{-1} x) = \frac{1}{\sqrt{1 + x^2}} \quad \frac{d}{dx}(\cosh^{-1} x) = \frac{1}{\sqrt{x^2 - 1}} \quad \frac{d}{dx}(\tanh^{-1} x) = \frac{1}{1 - x^2}$$

## Logarithmic Forms

$$\sinh^{-1} x = \ln(x + \sqrt{x^2 + 1})$$
$$\cosh^{-1} x = \ln(x + \sqrt{x^2 - 1})$$
$$\tanh^{-1} x = \frac{1}{2}\ln\left(\frac{1 + x}{1 - x}\right)$$

## Standard Integrals

$$\int \sinh x \, dx = \cosh x + C \qquad \int \cosh x \, dx = \sinh x + C$$
$$\int \tanh x \, dx = \ln(\cosh x) + C \qquad \int \coth x \, dx = \ln|\sinh x| + C$$
$$\int \operatorname{sech}^2 x \, dx = \tanh x + C \qquad \int \operatorname{cosech}^2 x \, dx = -\coth x + C$$

## Integrals Leading to Inverse Hyperbolic

$$\int \frac{1}{\sqrt{a^2 + x^2}} \, dx = \sinh^{-1}\left(\frac{x}{a}\right) + C$$
$$\int \frac{1}{\sqrt{x^2 - a^2}} \, dx = \cosh^{-1}\left(\frac{x}{a}\right) + C$$
$$\int \frac{1}{a^2 - x^2} \, dx = \frac{1}{a}\tanh^{-1}\left(\frac{x}{a}\right) + C \quad (|x| < a)$$

---

# 13. Cambridge Exam Analysis

## What Gets Tested

Based on Cambridge 9231 Paper 2 past papers, Chapter 19 Hyperbolic Functions typically appears as:

| Question Type | Frequency | Marks | Difficulty |
|---|---|---|---|
| Solving equations ($a\cosh x + b\sinh x = c$) | Very High | 5–7 | Medium |
| Proving identities from exponential definitions | High | 5–8 | Medium |
| Logarithmic form of inverse functions | High | 4–6 | Medium |
| Derivatives of hyperbolic/inverse hyperbolic | High | 4–6 | Easy–Med |
| Integration leading to inverse hyperbolic | Medium | 5–7 | Medium–Hard |
| Sketching transformed graphs | Medium | 4–5 | Medium |
| Stationary points with hyperbolic functions | Low–Med | 6–8 | Hard |

## Cambridge Exam Patterns

1. **Part (a) — Derive, Part (b) — Use**: Cambridge loves two-part questions where (a) asks you to prove a logarithmic form or identity, and (b) asks you to apply it to solve an equation.

2. **The $\sinh^{-1} x$ derivation**: Frequently tested. Know how to go from $y = \sinh^{-1} x$ to $y = \ln(x + \sqrt{x^2 + 1})$.

3. **Exponential substitution method**: The standard technique for solving $a\cosh x + b\sinh x = c$ appears in almost every exam sitting.

4. **Mixed with differentiation**: Expect hyperbolic functions in implicit differentiation questions and chain rule applications.

5. **Integration by recognition**: Cambridge asks you to recognise $\frac{1}{\sqrt{a^2 + x^2}}$ etc. and integrate directly to inverse hyperbolic form.

## Typical Question Structure

```
9 (a) Express sinh x and cosh x in exponential form. [2]
   (b) Hence solve 5 cosh x - 3 sinh x = 7, giving your answer in exact form. [5]
   (c) Find ∫ 1/√(x² + 4) dx. [2]
```

Total: 9 marks from one question cluster.

---

# 14. Common Mistakes

## ⚠️ Mistake 1: $\frac{d}{dx}(\cosh x) = -\sinh x$

**WRONG:** This is the derivative of $\cos x$, not $\cosh x$.

**RIGHT:** $\displaystyle \frac{d}{dx}(\cosh x) = +\sinh x$

Remember: Hyperbolic cosh derivative has **NO negative sign**.

## ⚠️ Mistake 2: $\cosh^2 x + \sinh^2 x = 1$

**WRONG:** This is the trig identity. Hyperbolic identity uses **minus**.

**RIGHT:** $\cosh^2 x - \sinh^2 x = 1$

## ⚠️ Mistake 3: Forgetting Osborne's Rule sign change

When converting $\cos 2x = 1 - 2\sin^2 x$ to hyperbolic:
- $\cos 2x \to \cosh 2x$
- $\sin^2 x \to \sinh^2 x$ — but this is a **product of two $\sinh$ terms**, so sign changes
- $\cosh 2x = 1 + 2\sinh^2 x$ ✓

## ⚠️ Mistake 4: Discarding valid negative $e^x$ in equations

When solving $e^x = k$, if $k < 0$, there is **no solution** (since $e^x > 0$ for all real $x$). But don't forget to check — sometimes students keep a negative solution.

## ⚠️ Mistake 5: Forgetting to restrict domain for $\cosh^{-1}$

$\cosh^{-1} x$ is only defined for $x \ge 1$.
$\tanh^{-1} x$ is only defined for $-1 < x < 1$.

## ⚠️ Mistake 6: Confusing $\frac{1}{\sqrt{1 + x^2}}$ with $\frac{1}{\sqrt{1 - x^2}}$

| Function | Derivative |
|---|---|
| $\sinh^{-1} x$ | $\displaystyle \frac{1}{\sqrt{1 + x^2}}$ |
| $\sin^{-1} x$ | $\displaystyle \frac{1}{\sqrt{1 - x^2}}$ |

The **plus/minus sign** inside the square root is the only difference — and it matters enormously.

## ⚠️ Mistake 7: Confusing $\tanh^{-1}$ derivative with $\tan^{-1}$

| Function | Derivative |
|---|---|
| $\tanh^{-1} x$ | $\displaystyle \frac{1}{1 - x^2}$ |
| $\tan^{-1} x$ | $\displaystyle \frac{1}{1 + x^2}$ |

The **minus/plus** sign is swapped.

## ⚠️ Mistake 8: Forgetting $e^x = \cosh x + \sinh x$

This identity is extremely useful for simplifying expressions and proving relationships. Memorise it.

## ⚠️ Mistake 9: Not checking $\tanh$ solution range

When solving quadratic equations in $\tanh x$, always check that your solution lies within $-1 < \tanh x < 1$. Values outside this range must be discarded.

## ⚠️ Mistake 10: Using $\sinh(A+B)$ identity with wrong signs

$$\sinh(A+B) = \sinh A \cosh B + \cosh A \sinh B$$
$$\sinh(A-B) = \sinh A \cosh B - \cosh A \sinh B$$

Both signs are **same as trig** (unlike $\cosh$ where signs differ from $\cos$).

---

# 15. Practice Questions & Full Solutions

## Exercise 19A (from textbook)

### Q1 — Solve $19\sinh x + 16\cosh x = 8$

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | $\displaystyle 19\left(\frac{e^x - e^{-x}}{2}\right) + 16\left(\frac{e^x + e^{-x}}{2}\right) = 8$ |
| **Step 2** | Multiply by 2: $19(e^x - e^{-x}) + 16(e^x + e^{-x}) = 16$ |
| **Step 3** | Expand: $19e^x - 19e^{-x} + 16e^x + 16e^{-x} = 16$ |
| **Step 4** | Simplify: $35e^x - 3e^{-x} = 16$ |
| **Step 5** | Multiply by $e^x$: $35e^{2x} - 3 = 16e^x$ |
| **Step 6** | $35e^{2x} - 16e^x - 3 = 0$ |
| **Step 7** | $(5e^x - 3)(7e^x + 1) = 0$ |
| **Step 8** | $e^x = \frac{3}{5}$ or $e^x = -\frac{1}{7}$ (invalid, must be positive) |
| **Step 9** | $x = \ln\frac{3}{5}$ |

$$\boxed{x = \ln\frac{3}{5}} \quad\checkmark$$

---

### Q2 — Solve $29\cosh x = 11\sinh x + 27$

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | $\displaystyle 29\left(\frac{e^x + e^{-x}}{2}\right) = 11\left(\frac{e^x - e^{-x}}{2}\right) + 27$ |
| **Step 2** | Multiply by 2: $29(e^x + e^{-x}) = 11(e^x - e^{-x}) + 54$ |
| **Step 3** | $29e^x + 29e^{-x} = 11e^x - 11e^{-x} + 54$ |
| **Step 4** | Collect: $18e^x + 40e^{-x} = 54$ |
| **Step 5** | Multiply by $e^x$: $18e^{2x} + 40 = 54e^x$ |
| **Step 6** | $18e^{2x} - 54e^x + 40 = 0$ |
| **Step 7** | Divide by 2: $9e^{2x} - 27e^x + 20 = 0$ |
| **Step 8** | $(3e^x - 4)(3e^x - 5) = 0$ |
| **Step 9** | $e^x = \frac{4}{3}$ or $e^x = \frac{5}{3}$ |
| **Step 10** | $x = \ln\frac{4}{3}$ or $x = \ln\frac{5}{3}$ |

$$\boxed{x = \ln\frac{4}{3},\; x = \ln\frac{5}{3}} \quad\checkmark$$

---

### Q9 — Solve $4\cosh x + \sinh x = 8$ in form $b\ln a$

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | $\displaystyle 4\left(\frac{e^x + e^{-x}}{2}\right) + \left(\frac{e^x - e^{-x}}{2}\right) = 8$ |
| **Step 2** | Multiply by 2: $4(e^x + e^{-x}) + (e^x - e^{-x}) = 16$ |
| **Step 3** | $4e^x + 4e^{-x} + e^x - e^{-x} = 16$ |
| **Step 4** | $5e^x + 3e^{-x} = 16$ |
| **Step 5** | Multiply by $e^x$: $5e^{2x} + 3 = 16e^x$ |
| **Step 6** | $5e^{2x} - 16e^x + 3 = 0$ |
| **Step 7** | $(5e^x - 1)(e^x - 3) = 0$ |
| **Step 8** | $e^x = \frac{1}{5}$ or $e^x = 3$ |
| **Step 9** | $x = \ln\frac{1}{5} = -\ln 5$ or $x = \ln 3$ |

$$\boxed{x = -\ln 5,\; x = \ln 3} \quad\checkmark$$

---

## Exercise 19B — Identities

### Q2 — Prove $\cosh 3x = 4\cosh^3 x - 3\cosh x$

**Solution:** (See Worked Example 10 — already proved above) $\checkmark$

### Q4a — Prove $\cosh(A - B) = \cosh A \cosh B - \sinh A \sinh B$

**Solution:** (See Worked Example 8 — already proved above) $\checkmark$

### Q4b — Prove $\sinh 3x = 3\sinh x + 4\sinh^3 x$

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | $\sinh 3x = \sinh(2x + x) = \sinh 2x \cosh x + \cosh 2x \sinh x$ |
| **Step 2** | $= (2\sinh x \cosh x)\cosh x + (1 + 2\sinh^2 x)\sinh x$ |
| **Step 3** | $= 2\sinh x \cosh^2 x + \sinh x + 2\sinh^3 x$ |
| **Step 4** | Use $\cosh^2 x = 1 + \sinh^2 x$: $= 2\sinh x(1 + \sinh^2 x) + \sinh x + 2\sinh^3 x$ |
| **Step 5** | $= 2\sinh x + 2\sinh^3 x + \sinh x + 2\sinh^3 x$ |
| **Step 6** | $= 3\sinh x + 4\sinh^3 x$ |

$$\boxed{\sinh 3x = 3\sinh x + 4\sinh^3 x} \quad\checkmark$$

---

## Exercise 19C — Inverse Functions

### Q3 — Prove $\cosh^{-1} x = \ln(x + \sqrt{x^2 - 1})$

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Let $y = \cosh^{-1} x$, so $\cosh y = x$, $y \ge 0$ |
| **Step 2** | $\displaystyle \frac{e^y + e^{-y}}{2} = x$ |
| **Step 3** | Multiply by $2e^y$: $e^{2y} + 1 = 2xe^y$ |
| **Step 4** | $e^{2y} - 2xe^y + 1 = 0$ |
| **Step 5** | Complete square: $(e^y - x)^2 = x^2 - 1$ |
| **Step 6** | $e^y = x \pm \sqrt{x^2 - 1}$ |
| **Step 7** | Since $y \ge 0$, $e^y \ge 1$, and $x \ge 1$, take $+$: $e^y = x + \sqrt{x^2 - 1}$ |
| **Step 8** | $y = \ln(x + \sqrt{x^2 - 1})$ |

$$\boxed{\cosh^{-1} x = \ln(x + \sqrt{x^2 - 1})} \quad\checkmark$$

---

### Q6 — Prove $\tanh^{-1} A + \tanh^{-1} B = \tanh^{-1}\left(\frac{A + B}{1 + AB}\right)$

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Let $X = \tanh^{-1} A$, $Y = \tanh^{-1} B$, so $\tanh X = A$, $\tanh Y = B$ |
| **Step 2** | $\displaystyle \tanh(X + Y) = \frac{\tanh X + \tanh Y}{1 + \tanh X \tanh Y} = \frac{A + B}{1 + AB}$ |
| **Step 3** | Therefore $X + Y = \tanh^{-1}\left(\frac{A + B}{1 + AB}\right)$ |
| **Step 4** | So $\tanh^{-1} A + \tanh^{-1} B = \tanh^{-1}\left(\frac{A + B}{1 + AB}\right)$ |

$$\boxed{\text{Identity proved}} \quad\checkmark$$

---

## End-of-Chapter Review Exercise 19

### Q1 — Solve $5\cosh x - \cosh 2x = 3$

**Solution:**

| Step | Operation |
|---|---|
| **Step 1** | Use $\cosh 2x = 2\cosh^2 x - 1$: $5\cosh x - (2\cosh^2 x - 1) = 3$ |
| **Step 2** | $5\cosh x - 2\cosh^2 x + 1 = 3$ |
| **Step 3** | $-2\cosh^2 x + 5\cosh x - 2 = 0$ |
| **Step 4** | $2\cosh^2 x - 5\cosh x + 2 = 0$ |
| **Step 5** | $(2\cosh x - 1)(\cosh x - 2) = 0$ |
| **Step 6** | $\cosh x = \frac{1}{2}$ or $\cosh x = 2$ |
| **Step 7** | $\cosh x \ge 1$, so $\cosh x = \frac{1}{2}$ is **invalid** |
| **Step 8** | $\cosh x = 2$ |
| **Step 9** | $x = \cosh^{-1} 2 = \ln(2 + \sqrt{4 - 1}) = \ln(2 + \sqrt{3})$ |

$$\boxed{x = \ln(2 + \sqrt{3})} \quad\checkmark$$

---

### Q3 — Stationary point of $y = \cosh 2x + \sinh x$

**Solution (Part a — Show exactly one stationary point):**

| Step | Operation |
|---|---|
| **Step 1** | $\displaystyle \frac{dy}{dx} = 2\sinh 2x + \cosh x$ |
| **Step 2** | Use $\sinh 2x = 2\sinh x \cosh x$: $\displaystyle \frac{dy}{dx} = 4\sinh x \cosh x + \cosh x$ |
| **Step 3** | Factor: $\displaystyle \frac{dy}{dx} = \cosh x(4\sinh x + 1)$ |
| **Step 4** | Set $= 0$: since $\cosh x \ge 1 > 0$ for all $x$, we need $4\sinh x + 1 = 0$ |
| **Step 5** | $\sinh x = -\frac{1}{4}$ — this gives **exactly one** solution |

$$\boxed{\text{Exactly one stationary point exists}} \quad\checkmark$$

**Solution (Part b — Find $x$-coordinate in exact logarithmic form):**

| Step | Operation |
|---|---|
| **Step 1** | $x = \sinh^{-1}\left(-\frac{1}{4}\right)$ |
| **Step 2** | $x = \ln\left(-\frac{1}{4} + \sqrt{\frac{1}{16} + 1}\right)$ |
| **Step 3** | $x = \ln\left(-\frac{1}{4} + \sqrt{\frac{17}{16}}\right) = \ln\left(-\frac{1}{4} + \frac{\sqrt{17}}{4}\right)$ |
| **Step 4** | $\displaystyle x = \ln\left(\frac{\sqrt{17} - 1}{4}\right)$ |

$$\boxed{x = \ln\left(\frac{\sqrt{17} - 1}{4}\right)} \quad\checkmark$$

---

### Extra Practice — Exam-Style Question

> **Question:** Given that $\sinh y = x$:
> (a) Show that $y = \ln(x + \sqrt{1 + x^2})$
> (b) By differentiating this result, show that $\displaystyle \frac{dy}{dx} = \frac{1}{\sqrt{1 + x^2}}$

**Solution (a):**

| Step | Operation |
|---|---|
| **Step 1** | $\displaystyle \frac{e^y - e^{-y}}{2} = x$ |
| **Step 2** | Multiply by $2e^y$: $e^{2y} - 1 = 2xe^y$ |
| **Step 3** | $e^{2y} - 2xe^y - 1 = 0$ |
| **Step 4** | Complete square: $(e^y - x)^2 = x^2 + 1$ |
| **Step 5** | Take positive root: $e^y = x + \sqrt{x^2 + 1}$ |
| **Step 6** | $y = \ln(x + \sqrt{x^2 + 1})$ |

$$\boxed{y = \ln(x + \sqrt{1 + x^2})} \quad\checkmark$$

**Solution (b):**

| Step | Operation |
|---|---|
| **Step 1** | $\displaystyle \frac{dy}{dx} = \frac{1}{x + \sqrt{1 + x^2}} \cdot \frac{d}{dx}(x + \sqrt{1 + x^2})$ |
| **Step 2** | $\displaystyle \frac{dy}{dx} = \frac{1}{x + \sqrt{1 + x^2}} \cdot \left(1 + \frac{2x}{2\sqrt{1 + x^2}}\right)$ |
| **Step 3** | $\displaystyle \frac{dy}{dx} = \frac{1}{x + \sqrt{1 + x^2}} \cdot \left(\frac{\sqrt{1 + x^2} + x}{\sqrt{1 + x^2}}\right)$ |
| **Step 4** | Cancel $x + \sqrt{1 + x^2}$: $\displaystyle \frac{dy}{dx} = \frac{1}{\sqrt{1 + x^2}}$ |

$$\boxed{\frac{dy}{dx} = \frac{1}{\sqrt{1 + x^2}}} \quad\checkmark$$

---

# 16. Quick Reference Card

## 🔥 MUST MEMORISE — The 6 Definitions

| Function | $e^x$ Form | $\frac{d}{dx}$ | $\int$ |
|---|---|---|---|
| $\sinh x$ | $\frac{e^x - e^{-x}}{2}$ | $\cosh x$ | $\cosh x + C$ |
| $\cosh x$ | $\frac{e^x + e^{-x}}{2}$ | $\sinh x$ | $\sinh x + C$ |
| $\tanh x$ | $\frac{e^x - e^{-x}}{e^x + e^{-x}}$ | $\operatorname{sech}^2 x$ | $\ln(\cosh x) + C$ |
| $\operatorname{sech} x$ | $\frac{2}{e^x + e^{-x}}$ | $-\operatorname{sech} x \tanh x$ | $\tan^{-1}(\sinh x) + C$ |
| $\operatorname{cosech} x$ | $\frac{2}{e^x - e^{-x}}$ | $-\operatorname{cosech} x \coth x$ | $\ln|\tanh\frac{x}{2}| + C$ |
| $\coth x$ | $\frac{e^x + e^{-x}}{e^x - e^{-x}}$ | $-\operatorname{cosech}^2 x$ | $\ln|\sinh x| + C$ |

## 🔥 MUST MEMORISE — Inverse Hyperbolic

| Function | Domain | Derivative | Log Form |
|---|---|---|---|
| $\sinh^{-1} x$ | $\mathbb{R}$ | $\frac{1}{\sqrt{1+x^2}}$ | $\ln(x+\sqrt{x^2+1})$ |
| $\cosh^{-1} x$ | $x\ge 1$ | $\frac{1}{\sqrt{x^2-1}}$ | $\ln(x+\sqrt{x^2-1})$ |
| $\tanh^{-1} x$ | $|x|<1$ | $\frac{1}{1-x^2}$ | $\frac{1}{2}\ln\frac{1+x}{1-x}$ |

## 🔥 MUST MEMORISE — Top Identities

$$\cosh^2 x - \sinh^2 x = 1$$
$$1 - \tanh^2 x = \operatorname{sech}^2 x$$
$$\sinh 2x = 2\sinh x \cosh x$$
$$\cosh 2x = \cosh^2 x + \sinh^2 x = 2\cosh^2 x - 1 = 1 + 2\sinh^2 x$$
$$e^x = \cosh x + \sinh x$$

## 🔥 Osborne's Rule

> Change the sign of any product of **two $\sinh$ terms** when converting a trig identity.

## 🔥 Solving $a\cosh x + b\sinh x = c$

1. Replace with exponentials
2. Multiply by $2e^x$
3. Solve quadratic in $e^x$
4. Take logs (discard negative $e^x$)

## 🔥 Top 3 Exam Traps

| Trap | Truth |
|---|---|
| $\frac{d}{dx}\cosh x = -\sinh x$ | ❌ $\to$ **$+\sinh x$** ✅ |
| $\cosh^2 x + \sinh^2 x = 1$ | ❌ $\to$ **$\cosh^2 x - \sinh^2 x = 1$** ✅ |
| $\frac{d}{dx}\tanh^{-1} x = \frac{1}{1+x^2}$ | ❌ $\to$ **$\frac{1}{1-x^2}$** ✅ |

---

> **End of Chapter 19 Study Guide.** Created from Cambridge International AS & A Level Further Mathematics (9231) textbook, pages 431–446.
>
> *"Hyperbolic functions are not just mathematical curiosities — they model real physical phenomena from hanging chains to tsunami waves."*
