# 🔗 FURTHER MATHS HOOKE'S LAW — ULTIMATE STUDY GUIDE

## Cambridge International AS & A Level Further Mathematics (9231) — Further Mechanics §3.4

> **The complete walkthrough:** Every technique explained step-by-step, with 11 fully solved worked examples and 12 practice questions in proper LaTeX. Covers Hooke's law, modulus of elasticity, natural length, extension, elastic potential energy, and problems with elastic strings and springs — horizontal, vertical, inclined plane, conical pendulum, work-energy, and equilibrium with elasticity.

---

# 📋 Table of Contents

1. [Syllabus Requirements](#1-syllabus-requirements)
2. [Prerequisite Knowledge](#2-prerequisite-knowledge)
3. [Hooke's Law — The Fundamental Relation](#3-hookes-law--the-fundamental-relation)
4. [Modulus of Elasticity and Stiffness](#4-modulus-of-elasticity-and-stiffness)
5. [Natural Length, Extension and Strings vs Springs](#5-natural-length-extension-and-strings-vs-springs)
6. [Elastic Potential Energy](#6-elastic-potential-energy)
7. [Equilibrium with Elastic Strings and Springs](#7-equilibrium-with-elastic-strings-and-springs)
8. [Horizontal Motion with Elasticity](#8-horizontal-motion-with-elasticity)
9. [Vertical Motion with Elasticity](#9-vertical-motion-with-elasticity)
10. [Elastic Strings on an Inclined Plane](#10-elastic-strings-on-an-inclined-plane)
11. [Conical Pendulum with an Elastic String](#11-conical-pendulum-with-an-elastic-string)
12. [Work, Energy and Elastic Potential Energy](#12-work-energy-and-elastic-potential-energy)
13. [Worked Examples — Complete Solutions](#13-worked-examples--complete-solutions)
14. [Common Mistakes](#14-common-mistakes)
15. [Complete Formula Sheet](#15-complete-formula-sheet)
16. [Cambridge Exam Analysis](#16-cambridge-exam-analysis)
17. [Practice Questions & Full Solutions](#17-practice-questions--full-solutions)
18. [Quick Reference Card](#18-quick-reference-card)

---

# How To Use This Guide

Each section follows this structure:

1. **The Rule** — the formula you must know (in LaTeX, boxed)
2. **Step-by-Step Method** — a numbered algorithm you can follow
3. **Worked Examples** — labelled **Example 1, 2, ...** with Question/Solution headers
4. **Watch Out!** — common pitfalls for that topic

> 💡 **How to get the most from this guide:** Work through Sections 3–6 to master the fundamentals, then tackle the situation-specific Sections 7–12. Attempt each worked example yourself before reading the solution. Every algebra step is shown on its own display line so you can follow the logic line-by-line.

---

# 1. Syllabus Requirements

## What Cambridge Expects for Hooke's Law — Further Mechanics §3.4

According to the CAIE 9231 syllabus for Further Mechanics, Section 3.4:

| Topic | What You Must Be Able To Do |
|-------|------------------------------|
| **Hooke's law** | State and apply $T = \dfrac{\lambda x}{l}$ (or $F = kx$) for elastic strings and springs |
| **Modulus of elasticity** | Understand and use the modulus of elasticity $\lambda$ — a property of the string/spring |
| **Natural length** | Identify and use the natural (unstretched) length $l$ |
| **Extension** | Calculate the extension $x = \text{current length} - l$ |
| **Comprehension of strings vs springs** | Know that an elastic **string** can only support tension (goes slack when $x \leq 0$); an elastic **spring** can support both tension and thrust (compression) |
| **Elastic potential energy** | State and use $E = \dfrac{\lambda x^{2}}{2l}$ for the elastic potential energy stored in a stretched string or spring |
| **Equilibrium problems** | Solve equilibrium problems involving elastic strings/springs (including on inclined planes) |
| **Elastic string on horizontal plane** | Analyse horizontal motion with elastic strings |
| **Vertical motion** | Solve problems with particles suspended vertically or oscillating on elastic strings |
| **Conical pendulum** | Analyse a particle whirling as a conical pendulum on an elastic string |
| **Work-energy** | Use conservation of energy / work-energy principle including elastic potential energy |

### 🟢 Cambridge Assessment Objectives

| AO | Weight | What It Means |
|----|--------|---------------|
| **AO1** | ~50% | Recall, select, and use mathematical facts, concepts, and techniques |
| **AO2** | ~50% | Construct rigorous arguments, solve problems, and interpret results |

> ⚠️ **Exam Tip:** Hooke's law questions in Further Mechanics are typically worth **7–12 marks** and most commonly appear as Question 1 or 2 on the paper. They frequently combine **equilibrium + energy conservation** in a single question (e.g. find the extension at equilibrium, then use energy to find the speed at another position). The elastic potential energy formula is **given** in the formula booklet — but you must know when and how to apply it.

---

# 2. Prerequisite Knowledge

## From AS & A Level Mathematics (Mechanics) and Further Mechanics

### 2.1 Resolving Forces

For a force $F$ at an angle $\theta$ to the horizontal:

$$F_{x} = F\cos\theta \quad\text{and}\quad F_{y} = F\sin\theta$$

### 2.2 Newton's Laws

- **First Law:** A body remains at rest or in uniform motion unless acted on by a net external force.
- **Second Law:** $F = ma$ (resultant force = mass × acceleration).
- **Third Law:** Every action has an equal and opposite reaction.

### 2.3 Weight and Normal Reaction

$$W = mg$$

where $m$ is the mass and $g$ is the acceleration due to gravity (take $g = 9.8\text{ m s}^{-2}$ or $10\text{ m s}^{-2}$ as directed).

### 2.4 Friction

For a body on a rough surface:

$$F \leq \mu R$$

where $F$ is the frictional force, $R$ is the normal reaction, and $\mu$ is the coefficient of friction. At limiting friction, $F = \mu R$.

### 2.5 Conservation of Mechanical Energy

In the absence of non-conservative forces (friction, air resistance):

$$\text{KE}_{1} + \text{GPE}_{1} + \text{EPE}_{1} = \text{KE}_{2} + \text{GPE}_{2} + \text{EPE}_{2}$$

where $\text{KE} = \frac{1}{2}mv^{2}$, $\text{GPE} = mgh$, and $\text{EPE} = \frac{\lambda x^{2}}{2l}$.

### 2.6 Circular Motion (for Conical Pendulum)

For a particle moving in a horizontal circle of radius $r$ with angular speed $\omega$:

$$F_{\text{centripetal}} = \frac{mv^{2}}{r} = mr\omega^{2}$$

---

# 3. Hooke's Law — The Fundamental Relation

## 3.1 Statement of Hooke's Law

> **📌 Key Point 18.1 — Hooke's Law:** For an elastic string or spring obeying Hooke's law, the **tension** $T$ is **directly proportional** to the **extension** $x$.
>
> $$T = \frac{\lambda x}{l}$$
>
> where:
> - $T$ = tension in the string/spring (N)
> - $\lambda$ = modulus of elasticity (N) — a constant for the given string/spring
> - $l$ = natural (unstretched) length (m)
> - $x$ = extension $= \text{current length} - l$ (m)

An equivalent form uses the **stiffness** (or spring constant) $k$:

$$T = kx \quad\text{where}\quad k = \frac{\lambda}{l}$$

> **📌 Key Point 18.2 — Alternative Form:**
>
> $$T = kx$$
>
> where $k = \dfrac{\lambda}{l}$ is called the **stiffness** or **spring constant** (units: $\text{N m}^{-1}$), while $\lambda$ has units of **force** (N).

### What Each Symbol Means

| Symbol | Name | Units | Notes |
|--------|------|-------|-------|
| $T$ | Tension | N | Force in the string/spring when stretched |
| $\lambda$ | Modulus of elasticity | N | Property of the material + cross-section |
| $l$ | Natural length | m | Length when no forces act |
| $x$ | Extension | m | $x = L - l$ where $L$ is the stretched length |
| $k$ | Stiffness | $\text{N m}^{-1}$ | $k = \lambda/l$ |

### Step-by-Step Method — Applying Hooke's Law

| Step | What To Do |
|------|------------|
| **1** | Identify $l$ (natural length), $L$ (current/stretched length), and hence $x = L - l$ |
| **2** | Identify which of $T$, $\lambda$, $l$, $x$ is unknown |
| **3** | Substitute into $T = \dfrac{\lambda x}{l}$ (or $T = kx$) and solve |
| **4** | Check: if the question says the string is **slack**, then $T = 0$ and $x \leq 0$ |

> ⚠️ **Watch Out!** Hooke's law only applies when the string is **taut** ($L > l$, so $x > 0$). If $L \leq l$, the string is slack and $T = 0$. A **spring** can go into compression ($x < 0$ gives a thrust/compressive force), but a **string** cannot — it simply goes slack.

---

# 4. Modulus of Elasticity and Stiffness

## 4.1 Modulus of Elasticity $\lambda$

> **📌 Key Point 18.3 — Modulus of Elasticity:**
>
> The **modulus of elasticity** $\lambda$ is a constant for a given elastic string or spring. It represents the force that would be required to stretch the string to **twice** its natural length (i.e. to produce an extension equal to the natural length), **if** Hooke's law remained valid for such a large extension.
>
> $$T = \lambda \quad\text{when}\quad x = l$$

In practice Hooke's law breaks down long before $x = l$, but $\lambda$ is still a useful and well-defined constant. A larger $\lambda$ means a **stiffer** string — more force is needed per unit extension.

$$k = \frac{\lambda}{l}$$

So for two strings of the **same material and cross-section** (same $\lambda$), the shorter one is stiffer (larger $k$).

### 4.2 Finding $\lambda$ or $l$ from Data

Often you are given two pairs of $(L, T)$ or $(x, T)$ measurements and must find both $\lambda$ and $l$.

**Method — Two measurements:**

Given: at length $L_{1}$ tension is $T_{1}$; at length $L_{2}$ tension is $T_{2}$.

$$T_{1} = \frac{\lambda(L_{1} - l)}{l}$$

$$T_{2} = \frac{\lambda(L_{2} - l)}{l}$$

Divide or subtract to eliminate one unknown.

> **📌 Key Point 18.4 — Finding $\lambda$ and $l$ Simultaneously:**
>
> From two tension–extension pairs, use:
>
> $$\frac{T_{1}}{T_{2}} = \frac{L_{1} - l}{L_{2} - l} \quad \text{(eliminates $\lambda$)}$$
>
> Solve for $l$ first, then back-substitute to find $\lambda$.

---

# 5. Natural Length, Extension and Strings vs Springs

## 5.1 Natural Length and Extension

> **📌 Key Point 18.5 — Definitions:**
>
> - **Natural length** $l$: the length of the string/spring when it is **not stretched** and no tension acts.
> - **Extended length** $L$: the current length when under tension.
> - **Extension** $x$: the amount by which the string has been stretched beyond its natural length.
>
> $$x = L - l$$
>
> - **Compression** (springs only): when $L < l$, we have $x < 0$; the spring exerts a **thrust** (push) of magnitude $\dfrac{\lambda|x|}{l}$.

### 5.2 Elastic String vs Elastic Spring

| Feature | Elastic String | Elastic Spring |
|---------|---------------|----------------|
| Can support **tension** ($x > 0$) | ✅ Yes: $T = \dfrac{\lambda x}{l}$ | ✅ Yes: $T = \dfrac{\lambda x}{l}$ |
| Can support **compression/thrust** ($x < 0$) | ❌ No — goes **slack**, $T = 0$ | ✅ Yes — exerts a **thrust** |
| When $L \leq l$ | $T = 0$ (slack) | $T < 0$ (compressive force) |
| Typical Cambridge phrasing | "light elastic **string**" | "light elastic **spring**" |

> ⚠️ **Watch Out!** This is one of the most examined distinctions. If a question says **"string"** and you calculate a negative extension (or the length is less than $l$), the answer is $T = 0$ — not a negative tension. If it says **"spring"**, a negative $x$ gives a genuine compressive force.

### 5.3 Diagram Convention

```
Natural:    |---- l ----|
Stretched:  |---- l ----|-- x --|  = L = l + x,  T = λx/l  (tension)
Compressed: |-- x --|                (spring only, thrust)
Slack:      |---- L ----|  where L ≤ l  →  T = 0  (string only)
```

---

# 6. Elastic Potential Energy

## 6.1 The Energy Stored in a Stretched String or Spring

> **📌 Key Point 18.6 — Elastic Potential Energy (EPE):**
>
> The elastic potential energy stored in a stretched elastic string or spring with modulus $\lambda$, natural length $l$, and extension $x$ is:
>
> $$E = \frac{\lambda x^{2}}{2l}$$
>
> Equivalently, using stiffness $k = \dfrac{\lambda}{l}$:
>
> $$E = \frac{1}{2}kx^{2}$$
>
> And in terms of tension:
>
> $$E = \frac{T^{2}l}{2\lambda} = \frac{T^{2}}{2k}$$

**Proof sketch (not required for the exam, but illuminating):** The work done stretching the string from extension $0$ to $x$ is the area under the $T$–$x$ graph. Since $T = \frac{\lambda x}{l}$ is linear through the origin:

$$E = \int_{0}^{x} T\, dx' = \int_{0}^{x} \frac{\lambda x'}{l}\, dx' = \frac{\lambda}{l}\cdot\frac{x^{2}}{2} = \frac{\lambda x^{2}}{2l}$$

This is the area of a triangle with base $x$ and height $T = \frac{\lambda x}{l}$:

$$E = \frac{1}{2}\times x \times T = \frac{1}{2}xT = \frac{\lambda x^{2}}{2l}$$

### 6.2 Key Properties

| Property | Detail |
|----------|--------|
| Always **non-negative** | $E = \frac{\lambda x^{2}}{2l} \geq 0$ (energy is stored whether stretched or compressed — for a spring, $x^{2}$ is always positive) |
| Zero when unextended | $E = 0$ when $x = 0$ (natural length) |
| **Slack string**: $E = 0$ | If an elastic **string** is slack ($x \leq 0$), no energy is stored: $E = 0$ |
| Quadratic in $x$ | Doubling the extension **quadruples** the stored energy |

### 6.3 Work Done Against / By the Elastic Force

- **Stretching** the string from extension $x_{1}$ to $x_{2}$ ($x_{2} > x_{1}$): work done **against** the elastic force = $E_{2} - E_{1} = \frac{\lambda}{2l}(x_{2}^{2} - x_{1}^{2})$.
- **If the string contracts** from $x_{2}$ to $x_{1}$: energy **released** = $E_{2} - E_{1}$.

> ⚠️ **Watch Out!** The elastic potential energy is $\frac{\lambda x^{2}}{2l}$, **not** $\frac{\lambda x}{2l}$ and **not** $\frac{\lambda x^{2}}{l}$. The factor of $\frac{1}{2}$ is essential. Also, when using energy conservation, remember that a **slack** elastic string contributes **zero** EPE — do not plug in a negative $x$.

---

# 7. Equilibrium with Elastic Strings and Springs

## 7.1 General Principle

A particle or body attached to one or more elastic strings/springs is in equilibrium when the **vector sum of all forces** is zero. The elastic force(s) are found from Hooke's law.

> **📌 Key Point 18.7 — Equilibrium with Elasticity:**
>
> For a particle in equilibrium under elastic forces:
>
> $$\sum F = 0 \quad\text{with}\quad T = \frac{\lambda x}{l} \text{ for each taut string/spring}$$

### Step-by-Step Method — Equilibrium with Elastic Strings

| Step | What To Do |
|------|------------|
| **1** | Draw a diagram showing all forces: weight, normal reaction, friction (if rough), and tension(s) from Hooke's law |
| **2** | Write $x = L - l$ for each string (check: is it taut? If $L \leq l$ for a string, $T = 0$) |
| **3** | Express each tension as $T = \dfrac{\lambda x}{l}$ |
| **4** | Resolve forces ($\sum F_{x} = 0$, $\sum F_{y} = 0$) or take moments ($\sum M = 0$ for rigid bodies) |
| **5** | Solve for the unknown (extension, modulus, natural length, position of equilibrium, etc.) |

### 7.2 Particle Attached to Two Elastic Strings (Horizontal Line)

A common configuration: a particle of mass $m$ is attached to two elastic strings on a smooth horizontal surface (or suspended between two fixed points).

```
A ●--------● P --------● B
  |--- a ---|- x -|-- (b-x) --|
  Fixed    Particle   Fixed
```

If $A$ and $B$ are fixed points distance $d$ apart, with strings of natural lengths $l_{1}$, $l_{2}$ and moduli $\lambda_{1}$, $\lambda_{2}$, and the particle $P$ is distance $y$ from $A$:

$$T_{1} = \frac{\lambda_{1}(y - l_{1})}{l_{1}}, \qquad T_{2} = \frac{\lambda_{2}(d - y - l_{2})}{l_{2}}$$

At equilibrium (smooth horizontal, no other horizontal forces): $T_{1} = T_{2}$.

---

# 8. Horizontal Motion with Elasticity

## 8.1 Particle on a Smooth Horizontal Surface

> **📌 Key Point 18.8 — Horizontal Motion (Smooth):**
>
> A particle of mass $m$ attached to an elastic string on a smooth horizontal plane has no weight/friction component along the plane. The only horizontal force is the elastic tension.
>
> - If the string is **taut**: $T = \dfrac{\lambda x}{l}$ acts towards the fixed point.
> - If the string is **slack**: $T = 0$ and the particle moves freely (constant velocity) until the string becomes taut again.

### Step-by-Step Method — Horizontal Elastic Problems

| Step | What To Do |
|------|------------|
| **1** | Determine whether the string is taut or slack at each stage |
| **2** | If taut, write $T = \dfrac{\lambda x}{l}$ and apply $F = ma$ or energy conservation |
| **3** | If slack, $T = 0$ and $E = 0$ — particle moves with constant velocity (if smooth) |
| **4** | For energy methods: $\frac{1}{2}mv^{2} + \frac{\lambda x^{2}}{2l} = \text{constant}$ (if no friction and horizontal) |

---

# 9. Vertical Motion with Elasticity

## 9.1 Particle Suspended Vertically

> **📌 Key Point 18.9 — Vertical Equilibrium:**
>
> A particle of mass $m$ hanging in equilibrium from a fixed point by a light elastic string of natural length $l$ and modulus $\lambda$ satisfies:
>
> $$mg = \frac{\lambda x}{l} \quad\text{(weight = tension)}$$
>
> So the equilibrium extension is:
>
> $$x_{\text{eq}} = \frac{mgl}{\lambda}$$

The equilibrium length is therefore:

$$L_{\text{eq}} = l + x_{\text{eq}} = l + \frac{mgl}{\lambda} = l\left(1 + \frac{mg}{\lambda}\right)$$

### 9.2 Vertical Motion — Energy Approach

For a particle moving vertically on an elastic string, define the gravitational potential energy datum. Then:

$$\frac{1}{2}mv^{2} + mgh + \frac{\lambda x^{2}}{2l} = \text{constant}$$

(provided the string remains taut throughout the motion being considered; if it goes slack, set EPE $= 0$ for that phase).

> ⚠️ **Watch Out!** When a particle hangs vertically, students often forget that the **total distance fallen** includes both the free-fall (string slack, $T = 0$) phase and the stretching phase. If a particle is dropped from the point of suspension, it falls distance $l$ freely before the string even begins to stretch. Account for this correctly in energy equations.

---

# 10. Elastic Strings on an Inclined Plane

## 10.1 Particle on an Inclined Plane Attached to an Elastic String

> **📌 Key Point 18.10 — Inclined Plane with Elastic String:**
>
> A particle of mass $m$ on a plane inclined at angle $\alpha$ to the horizontal, attached to an elastic string (natural length $l$, modulus $\lambda$) with the string parallel to the line of greatest slope, has along-slope equilibrium:
>
> **Smooth plane:**
>
> $$mg\sin\alpha = \frac{\lambda x}{l} \quad\text{(component of weight down slope = tension up slope)}$$
>
> **Rough plane** (friction $F \leq \mu R$, $R = mg\cos\alpha$):
>
> $$\left|mg\sin\alpha - \frac{\lambda x}{l}\right| \leq \mu mg\cos\alpha$$

### Step-by-Step Method — Inclined Plane

| Step | What To Do |
|------|------------|
| **1** | Resolve weight: $mg\sin\alpha$ down the slope, $mg\cos\alpha$ perpendicular to slope |
| **2** | Normal reaction: $R = mg\cos\alpha$ |
| **3** | Tension: $T = \dfrac{\lambda x}{l}$ (up the slope, if taut; zero if slack) |
| **4** | Friction (if rough): $F \leq \mu R$, direction opposes tendency to slip |
| **5** | Apply equilibrium: $T + F = mg\sin\alpha$ (signs depend on direction of $F$) or energy methods |

### 10.2 Energy on an Inclined Plane

If the particle moves along the slope, the work-energy principle gives:

$$\frac{1}{2}mv^{2} + mgh + \frac{\lambda x^{2}}{2l} \pm F_{\text{friction}}\cdot d = \text{constant}$$

where $h$ is the vertical height and $d$ is the distance moved along the plane. The sign on the friction work depends on direction.

---

# 11. Conical Pendulum with an Elastic String

## 11.1 Setup

> **📌 Key Point 18.11 — Conical Pendulum with Elastic String:**
>
> A particle of mass $m$ whirls in a **horizontal circle** while attached to a fixed point $O$ by a light elastic string of natural length $l$ and modulus $\lambda$. The string makes an angle $\theta$ with the vertical and has extended length $L = l + x$ with tension $T = \dfrac{\lambda x}{l}$.
>
> Forces on the particle:
> - **Weight** $mg$ vertically downward
> - **Tension** $T$ along the string (towards $O$)
>
> Resolving:
>
> $$T\cos\theta = mg \quad\text{(vertical equilibrium)}$$
>
> $$T\sin\theta = \frac{mv^{2}}{r} = mr\omega^{2} \quad\text{(horizontal — provides centripetal force)}$$
>
> where $r = L\sin\theta$ is the radius of the circular path.

```
         O (fixed point)
         |
         |  L = l + x (stretched length)
         |  T = λx/l
         |  /
         | /  θ
         |/
         ●  particle, mass m
        / \
       /   \  r = L sin θ
      /  ○  \  horizontal circle
```

### Step-by-Step Method — Elastic Conical Pendulum

| Step | What To Do |
|------|------------|
| **1** | Let $x$ be the extension, so $L = l + x$ and $T = \dfrac{\lambda x}{l}$ |
| **2** | Radius of circle: $r = L\sin\theta = (l + x)\sin\theta$ |
| **3** | Resolve **vertically**: $T\cos\theta = mg$ |
| **4** | Resolve **horizontally**: $T\sin\theta = mr\omega^{2} = \dfrac{mv^{2}}{r}$ |
| **5** | Eliminate $T$ and/or $\theta$ as needed; often divide horizontal by vertical to get $\tan\theta = \dfrac{r\omega^{2}}{g}$ |
| **6** | Use $r = (l+x)\sin\theta$ to relate $x$, $\theta$, and $\omega$ |

### 11.2 Useful Derived Relations

Dividing the two force equations:

$$\tan\theta = \frac{r\omega^{2}}{g} = \frac{(l+x)\sin\theta\,\omega^{2}}{g}$$

For $\sin\theta \neq 0$:

$$\cos\theta = \frac{g}{(l+x)\,\omega^{2}} \quad\Longrightarrow\quad \omega^{2} = \frac{g}{(l+x)\cos\theta}$$

Combined with $T\cos\theta = mg$ and $T = \dfrac{\lambda x}{l}$:

$$\frac{\lambda x}{l}\cos\theta = mg$$

---

# 12. Work, Energy and Elastic Potential Energy

## 12.1 The Work-Energy Principle with Elasticity

> **📌 Key Point 18.12 — Conservation of Mechanical Energy (Including EPE):**
>
> For a system with gravitational and elastic potential energy, and no non-conservative work (no friction/air resistance):
>
> $$\frac{1}{2}mv_{1}^{2} + mgh_{1} + \frac{\lambda x_{1}^{2}}{2l} = \frac{1}{2}mv_{2}^{2} + mgh_{2} + \frac{\lambda x_{2}^{2}}{2l}$$
>
> If friction or other non-conservative forces do work $W_{\text{nc}}$:
>
> $$\Delta(\text{KE} + \text{GPE} + \text{EPE}) = W_{\text{nc}}$$

### When to Use Energy vs. Force Methods

| Situation | Best Method | Why |
|-----------|-------------|-----|
| Find **speed** at a given position | **Energy** conservation | Avoids solving differential equations |
| Find **extension** at equilibrium | **Force** balance ($\sum F = 0$) | Direct from Hooke's law |
| Find **maximum extension** when dropped | **Energy** (KE = 0 at max extension) | Clean — set final KE to zero |
| Find **time** or **acceleration** | **Force** ($F = ma$) | Energy doesn't give time info |
| Particle on **rough** surface | **Work-energy** with friction work | $W_{\text{friction}} = -\mu R \times d$ |

### 12.2 Work Done by the Elastic Force

The work done **by** the elastic force when the extension changes from $x_{1}$ to $x_{2}$ is:

$$W_{\text{elastic}} = \frac{\lambda x_{1}^{2}}{2l} - \frac{\lambda x_{2}^{2}}{2l} = E_{1} - E_{2}$$

If $x_{2} > x_{1}$ (string stretched further), the elastic force does **negative** work — energy is **stored**.

> ⚠️ **Watch Out!** When writing energy conservation equations, be meticulous about:
> 1. **Datum for GPE** — choose a consistent zero level (often the lowest point or the suspension point).
> 2. **Slack vs taut** — if the string goes slack between positions 1 and 2, then at the slack position $E = 0$ (not $\frac{\lambda x^{2}}{2l}$ with negative $x$!).
> 3. **Sign of $h$** — if the particle moves downward, GPE decreases. Make sure $mgh$ terms have the correct sign relative to your datum.

---

# 13. Worked Examples — Complete Solutions

---

### Example 1 — Easy: Finding the Modulus of Elasticity

> **Question:** A light elastic string has natural length $0.8\text{ m}$. When a particle of mass $3\text{ kg}$ hangs in equilibrium from the string, the length of the string is $1.1\text{ m}$. Find the modulus of elasticity $\lambda$ of the string. Take $g = 10\text{ m s}^{-2}$.

**Solution:**

| Step | Working |
|------|---------|
| **1** | Natural length $l = 0.8\text{ m}$, equilibrium length $L = 1.1\text{ m}$ |
| **2** | Extension $x = L - l = 1.1 - 0.8$ |
| **3** | At equilibrium, weight $=$ tension: $mg = \dfrac{\lambda x}{l}$ |

$$x = 1.1 - 0.8 = 0.3\text{ m}$$

At equilibrium:

$$mg = \frac{\lambda x}{l}$$

$$3 \times 10 = \frac{\lambda \times 0.3}{0.8}$$

$$30 = \frac{0.3\lambda}{0.8}$$

$$\lambda = \frac{30 \times 0.8}{0.3}$$

$$\lambda = \frac{24}{0.3} = 80\text{ N} \quad \checkmark$$

> 💡 **Check:** $\lambda = 80\text{ N}$ means that extending this string by its full natural length ($0.8\text{ m}$) would require $80\text{ N}$ (if Hooke's law held that far). Our $3\text{ kg}$ weight produces $30\text{ N}$, giving a modest $0.3\text{ m}$ extension — reasonable.

---

### Example 2 — Medium: Finding Both $\lambda$ and Natural Length from Two Measurements

> **Question:** A light elastic string obeys Hooke's law. When a mass of $2\text{ kg}$ hangs on the string, its length is $1.35\text{ m}$. When a mass of $5\text{ kg}$ hangs on the string, its length is $1.65\text{ m}$. Find (a) the natural length $l$ of the string, and (b) the modulus of elasticity $\lambda$. Take $g = 10\text{ m s}^{-2}$.

**Solution:**

| Step | Working |
|------|---------|
| **1** | Let $l$ = natural length, $\lambda$ = modulus. Two equilibrium states. |
| **2** | For $2\text{ kg}$: $T_{1} = 2g = 20\text{ N}$, $L_{1} = 1.35\text{ m}$ |
| **3** | For $5\text{ kg}$: $T_{2} = 5g = 50\text{ N}$, $L_{2} = 1.65\text{ m}$ |
| **4** | Write Hooke's law for each: $T = \dfrac{\lambda(L - l)}{l}$ |

For the $2\text{ kg}$ mass at equilibrium:

$$20 = \frac{\lambda(1.35 - l)}{l} \tag{1}$$

For the $5\text{ kg}$ mass at equilibrium:

$$50 = \frac{\lambda(1.65 - l)}{l} \tag{2}$$

Divide equation (2) by equation (1) to eliminate $\lambda$:

$$\frac{50}{20} = \frac{1.65 - l}{1.35 - l}$$

$$\frac{5}{2} = \frac{1.65 - l}{1.35 - l}$$

$$5(1.35 - l) = 2(1.65 - l)$$

$$6.75 - 5l = 3.30 - 2l$$

$$6.75 - 3.30 = 5l - 2l$$

$$3.45 = 3l$$

$$l = 1.15\text{ m} \quad \checkmark \text{ — Part (a)}$$

Now substitute $l = 1.15$ into equation (1):

$$20 = \frac{\lambda(1.35 - 1.15)}{1.15}$$

$$20 = \frac{\lambda \times 0.20}{1.15}$$

$$\lambda = \frac{20 \times 1.15}{0.20}$$

$$\lambda = \frac{23}{0.20} = 115\text{ N} \quad \checkmark \text{ — Part (b)}$$

**Verification** with equation (2):

$$\frac{115 \times (1.65 - 1.15)}{1.15} = \frac{115 \times 0.50}{1.15} = \frac{57.5}{1.15} = 50\text{ N} = 5g \quad \checkmark$$

> ⚠️ **Watch Out!** A common error is to write $x = L$ (forgetting to subtract $l$). Always compute extension as $x = L - l$. In this problem, $l$ was unknown, so we kept it symbolic until the division eliminated $\lambda$.

---

### Example 3 — Medium: Vertical Equilibrium and Elastic Potential Energy

> **Question:** A light elastic spring has natural length $0.6\text{ m}$ and modulus of elasticity $120\text{ N}$. A particle of mass $4\text{ kg}$ is attached to one end of the spring, the other end being fixed at a point $O$.
>
> (a) Find the extension of the spring when the particle hangs in equilibrium vertically below $O$.
>
> (b) Find the elastic potential energy stored in the spring in this equilibrium position.
>
> Take $g = 10\text{ m s}^{-2}$.

**Solution (a):**

| Step | Working |
|------|---------|
| **1** | $l = 0.6\text{ m}$, $\lambda = 120\text{ N}$, $m = 4\text{ kg}$ |
| **2** | At equilibrium: $mg = \dfrac{\lambda x}{l}$ |
| **3** | Solve for $x$ |

$$mg = \frac{\lambda x}{l}$$

$$4 \times 10 = \frac{120\, x}{0.6}$$

$$40 = \frac{120x}{0.6}$$

$$40 = 200x$$

$$x = \frac{40}{200} = 0.20\text{ m} \quad \checkmark$$

**Solution (b):**

Elastic potential energy:

$$E = \frac{\lambda x^{2}}{2l}$$

$$E = \frac{120 \times (0.20)^{2}}{2 \times 0.6}$$

$$E = \frac{120 \times 0.04}{1.2}$$

$$E = \frac{4.8}{1.2} = 4.0\text{ J} \quad \checkmark$$

> 💡 **Alternative check for (b):** Using $E = \frac{1}{2}Tx$ where $T = mg = 40\text{ N}$:
>
> $$E = \frac{1}{2} \times 40 \times 0.20 = 4.0\text{ J} \quad \checkmark$$

---

### Example 4 — Hard: Energy Conservation — Particle Dropped on an Elastic String

> **Question:** A light elastic string has natural length $1.2\text{ m}$ and modulus of elasticity $60\text{ N}$. One end is attached to a fixed point $O$. A particle of mass $2\text{ kg}$ is attached to the other end. The particle is held at $O$ and released from rest.
>
> (a) Find the distance the particle falls before it first comes to instantaneous rest.
>
> (b) Find the speed of the particle when it has fallen $2.0\text{ m}$ below $O$.
>
> Take $g = 10\text{ m s}^{-2}$.

**Solution (a):**

| Step | Working |
|------|---------|
| **1** | $l = 1.2\text{ m}$, $\lambda = 60\text{ N}$, $m = 2\text{ kg}$ |
| **2** | Particle falls freely for $1.2\text{ m}$ (string slack), then stretches the string |
| **3** | Let $d$ = total distance fallen when particle first comes to rest ($d > 1.2$) |
| **4** | Extension at lowest point: $x = d - l = d - 1.2$ |
| **5** | Use energy conservation: loss of GPE = gain in EPE (KE = 0 at both ends) |

The particle starts at rest at $O$ (GPE datum at $O$: initial GPE $= 0$) and comes to rest at distance $d$ below $O$.

Loss of gravitational potential energy:

$$\Delta\text{GPE} = mgd = 2 \times 10 \times d = 20d$$

Gain in elastic potential energy (only when $x > 0$, i.e. $d > 1.2$):

$$E = \frac{\lambda x^{2}}{2l} = \frac{60(d - 1.2)^{2}}{2 \times 1.2}$$

$$E = \frac{60(d - 1.2)^{2}}{2.4}$$

$$E = 25(d - 1.2)^{2}$$

Energy conservation ($\text{KE}_{\text{initial}} = \text{KE}_{\text{final}} = 0$):

$$mgd = \frac{\lambda(d - l)^{2}}{2l}$$

$$20d = 25(d - 1.2)^{2}$$

$$20d = 25(d^{2} - 2.4d + 1.44)$$

$$20d = 25d^{2} - 60d + 36$$

$$25d^{2} - 80d + 36 = 0$$

Using the quadratic formula:

$$d = \frac{80 \pm \sqrt{80^{2} - 4 \times 25 \times 36}}{2 \times 25}$$

$$d = \frac{80 \pm \sqrt{6400 - 3600}}{50}$$

$$d = \frac{80 \pm \sqrt{2800}}{50}$$

$$d = \frac{80 \pm 52.915}{50}$$

The two solutions are:

$$d = \frac{132.915}{50} = 2.658\text{ m} \quad\text{or}\quad d = \frac{27.085}{50} = 0.542\text{ m}$$

The second solution $d = 0.542\text{ m} < l = 1.2\text{ m}$ is invalid because the string is slack there (no EPE is stored, so the energy equation does not apply in that form). The physical solution is:

$$d = 2.66\text{ m (to 3 s.f.)} \quad \checkmark$$

The maximum extension is:

$$x_{\max} = 2.658 - 1.2 = 1.458\text{ m}$$

> ⚠️ **Watch Out!** You must **reject** the extraneous root where $d < l$. When $d < l$, the string is slack and $E = 0$, so $mgd = 0$ would imply $d = 0$ — the only valid slack solution is the starting point. The quadratic was derived assuming $d > l$ (string taut), so only roots with $d > l$ are physical.

**Solution (b):**

When the particle has fallen $2.0\text{ m}$ below $O$:

$$x = 2.0 - 1.2 = 0.8\text{ m}$$

$$E = \frac{60 \times 0.8^{2}}{2 \times 1.2} = \frac{60 \times 0.64}{2.4} = \frac{38.4}{2.4} = 16\text{ J}$$

Energy conservation (initial: at $O$, KE $= 0$, GPE $= 0$, EPE $= 0$; at $2.0\text{ m}$ below $O$):

$$0 = \frac{1}{2}mv^{2} - mgd + E$$

More carefully, with GPE measured downward from $O$:

$$\text{KE} + \text{EPE} - mgd = 0 \quad\text{(taking downward as loss of height)}$$

$$\frac{1}{2} \times 2 \times v^{2} + 16 - 2 \times 10 \times 2.0 = 0$$

$$v^{2} + 16 - 40 = 0$$

$$v^{2} = 24$$

$$v = \sqrt{24} = 2\sqrt{6} \approx 4.90\text{ m s}^{-1} \quad \checkmark$$

---

### Example 5 — Hard: Particle Attached to Two Elastic Strings on a Horizontal Line

> **Question:** Two fixed points $A$ and $B$ are $3\text{ m}$ apart on a smooth horizontal table. A particle $P$ of mass $0.5\text{ kg}$ is attached to $A$ by a light elastic string of natural length $1.0\text{ m}$ and modulus $20\text{ N}$, and to $B$ by a light elastic **spring** of natural length $0.8\text{ m}$ and modulus $16\text{ N}$.
>
> (a) Find the equilibrium position of $P$ (distance from $A$).
>
> (b) The particle is held at a point $1.5\text{ m}$ from $A$ and released from rest. Find its speed when it passes through the equilibrium position. (Assume both string and spring remain taut/acting throughout.)

**Solution (a):**

| Step | Working |
|------|---------|
| **1** | Let $y$ = distance of $P$ from $A$ at equilibrium |
| **2** | String $AP$: extension $x_{1} = y - 1.0$, tension $T_{1} = \dfrac{20(y-1.0)}{1.0}$ |
| **3** | Spring $BP$: the stretched length of $BP$ is $3 - y$; extension $x_{2} = (3-y) - 0.8 = 2.2 - y$, tension $T_{2} = \dfrac{16(2.2 - y)}{0.8}$ |
| **4** | At equilibrium (smooth, no other horizontal forces): $T_{1} = T_{2}$ |

$$T_{1} = \frac{20(y - 1.0)}{1.0} = 20(y - 1.0)$$

$$T_{2} = \frac{16(2.2 - y)}{0.8} = 20(2.2 - y)$$

At equilibrium:

$$20(y - 1.0) = 20(2.2 - y)$$

$$y - 1.0 = 2.2 - y$$

$$2y = 3.2$$

$$y = 1.6\text{ m from } A \quad \checkmark$$

**Check that both are taut:** $y = 1.6 > 1.0$ (string taut ✓), $3 - y = 1.4 > 0.8$ (spring stretched ✓).

**Solution (b):**

Use energy conservation. On a smooth horizontal table, GPE is irrelevant; only KE and EPE matter.

At the release point ($y = 1.5\text{ m}$):

$$x_{1} = 1.5 - 1.0 = 0.5\text{ m}, \quad E_{1} = \frac{20 \times 0.5^{2}}{2 \times 1.0} = \frac{20 \times 0.25}{2} = 2.5\text{ J}$$

$$x_{2} = 2.2 - 1.5 = 0.7\text{ m}, \quad E_{2} = \frac{16 \times 0.7^{2}}{2 \times 0.8} = \frac{16 \times 0.49}{1.6} = \frac{7.84}{1.6} = 4.9\text{ J}$$

$$\text{Total EPE at release} = 2.5 + 4.9 = 7.4\text{ J}$$

$$\text{KE at release} = 0$$

At equilibrium ($y = 1.6\text{ m}$):

$$x_{1} = 1.6 - 1.0 = 0.6\text{ m}, \quad E_{1}' = \frac{20 \times 0.6^{2}}{2 \times 1.0} = \frac{20 \times 0.36}{2} = 3.6\text{ J}$$

$$x_{2} = 2.2 - 1.6 = 0.6\text{ m}, \quad E_{2}' = \frac{16 \times 0.6^{2}}{2 \times 0.8} = \frac{16 \times 0.36}{1.6} = 3.6\text{ J}$$

$$\text{Total EPE at equilibrium} = 3.6 + 3.6 = 7.2\text{ J}$$

Energy conservation:

$$\text{KE}_{\text{release}} + \text{EPE}_{\text{release}} = \text{KE}_{\text{eq}} + \text{EPE}_{\text{eq}}$$

$$0 + 7.4 = \frac{1}{2} \times 0.5 \times v^{2} + 7.2$$

$$0.25v^{2} = 7.4 - 7.2 = 0.2$$

$$v^{2} = \frac{0.2}{0.25} = 0.8$$

$$v = \sqrt{0.8} = \frac{2}{\sqrt{5}} = \frac{2\sqrt{5}}{5} \approx 0.894\text{ m s}^{-1} \quad \checkmark$$

---

### Example 6 — Medium: Particle on a Rough Inclined Plane with an Elastic String

> **Question:** A particle of mass $2\text{ kg}$ is attached to a light elastic string of natural length $0.5\text{ m}$ and modulus $40\text{ N}$. The other end of the string is attached to a fixed point at the top of a smooth plane inclined at $30^{\circ}$ to the horizontal. The string lies along the line of greatest slope.
>
> (a) Find the extension of the string when the particle is in equilibrium on the plane.
>
> (b) If the plane is rough with coefficient of friction $\mu = 0.3$, find the range of possible extensions for which the particle can remain in equilibrium.
>
> Take $g = 10\text{ m s}^{-2}$.

**Solution (a): Smooth plane**

| Step | Working |
|------|---------|
| **1** | $l = 0.5\text{ m}$, $\lambda = 40\text{ N}$, $m = 2\text{ kg}$, $\alpha = 30^{\circ}$ |
| **2** | Component of weight down slope: $mg\sin30^{\circ}$ |
| **3** | Tension up slope: $T = \dfrac{\lambda x}{l}$ |
| **4** | Equilibrium: $T = mg\sin30^{\circ}$ |

$$mg\sin30^{\circ} = \frac{\lambda x}{l}$$

$$2 \times 10 \times \frac{1}{2} = \frac{40x}{0.5}$$

$$10 = 80x$$

$$x = \frac{10}{80} = 0.125\text{ m} \quad \checkmark$$

The equilibrium length is $L = 0.5 + 0.125 = 0.625\text{ m}$.

**Solution (b): Rough plane**

Normal reaction:

$$R = mg\cos30^{\circ} = 2 \times 10 \times \frac{\sqrt{3}}{2} = 10\sqrt{3}\text{ N}$$

Maximum friction:

$$F_{\max} = \mu R = 0.3 \times 10\sqrt{3} = 3\sqrt{3} \approx 5.196\text{ N}$$

**Case 1: Particle on the point of sliding DOWN** (friction acts UP the slope, i.e. in the same direction as tension):

$$mg\sin30^{\circ} = T + F_{\max}$$

$$10 = \frac{40x}{0.5} + 3\sqrt{3}$$

$$10 - 3\sqrt{3} = 80x$$

$$x = \frac{10 - 3\sqrt{3}}{80} = \frac{10 - 5.196}{80} = \frac{4.804}{80} \approx 0.0600\text{ m}$$

**Case 2: Particle on the point of sliding UP** (friction acts DOWN the slope, opposing the tension which would pull it up):

$$T = mg\sin30^{\circ} + F_{\max}$$

$$\frac{40x}{0.5} = 10 + 3\sqrt{3}$$

$$80x = 10 + 3\sqrt{3}$$

$$x = \frac{10 + 3\sqrt{3}}{80} = \frac{15.196}{80} \approx 0.190\text{ m}$$

Therefore the range of equilibrium extensions is:

$$0.060\text{ m} \leq x \leq 0.190\text{ m (to 3 s.f.)} \quad \checkmark$$

Equivalently:

$$\frac{10 - 3\sqrt{3}}{80} \leq x \leq \frac{10 + 3\sqrt{3}}{80}\text{ metres}$$

> ⚠️ **Watch Out!** For the rough inclined plane, there are **two** limiting positions — one where friction acts up the slope and one where it acts down. Don't just calculate one. The smooth equilibrium extension ($0.125\text{ m}$) lies between these two extremes, as it must.

---

### Example 7 — Hard: Conical Pendulum with an Elastic String

> **Question:** A particle of mass $0.4\text{ kg}$ is attached to one end of a light elastic string of natural length $0.6\text{ m}$ and modulus $24\text{ N}$. The other end is attached to a fixed point $O$. The particle whirls in a horizontal circle with the string making an angle of $60^{\circ}$ with the vertical.
>
> (a) Find the extension of the string.
>
> (b) Find the angular speed $\omega$ of the particle.
>
> Take $g = 10\text{ m s}^{-2}$.

**Solution (a):**

| Step | Working |
|------|---------|
| **1** | $l = 0.6\text{ m}$, $\lambda = 24\text{ N}$, $m = 0.4\text{ kg}$, $\theta = 60^{\circ}$ |
| **2** | Let $x$ = extension, $T = \dfrac{24x}{0.6} = 40x$ |
| **3** | Resolve vertically: $T\cos\theta = mg$ |

$$T\cos60^{\circ} = mg$$

$$T \times \frac{1}{2} = 0.4 \times 10$$

$$T \times \frac{1}{2} = 4$$

$$T = 8\text{ N}$$

Now find $x$ from Hooke's law:

$$T = \frac{\lambda x}{l}$$

$$8 = \frac{24x}{0.6}$$

$$8 = 40x$$

$$x = \frac{8}{40} = 0.20\text{ m} \quad \checkmark$$

The stretched length is $L = 0.6 + 0.20 = 0.80\text{ m}$.

**Solution (b):**

| Step | Working |
|------|---------|
| **1** | Radius of circle: $r = L\sin\theta = 0.80\sin60^{\circ}$ |
| **2** | Resolve horizontally: $T\sin\theta = mr\omega^{2}$ |

$$r = 0.80 \times \sin60^{\circ} = 0.80 \times \frac{\sqrt{3}}{2} = 0.40\sqrt{3}\text{ m}$$

$$T\sin60^{\circ} = mr\omega^{2}$$

$$8 \times \frac{\sqrt{3}}{2} = 0.4 \times 0.40\sqrt{3} \times \omega^{2}$$

$$4\sqrt{3} = 0.16\sqrt{3}\,\omega^{2}$$

$$\omega^{2} = \frac{4\sqrt{3}}{0.16\sqrt{3}} = \frac{4}{0.16} = 25$$

$$\omega = 5\text{ rad s}^{-1} \quad \checkmark$$

> 💡 **Alternative via $\tan\theta$:** Dividing horizontal by vertical gives $\tan\theta = \dfrac{r\omega^{2}}{g}$. So:
>
> $$\tan60^{\circ} = \frac{0.40\sqrt{3}\,\omega^{2}}{10}$$
>
> $$\sqrt{3} = \frac{0.40\sqrt{3}\,\omega^{2}}{10}$$
>
> $$\omega^{2} = \frac{10}{0.40} = 25 \implies \omega = 5\text{ rad s}^{-1} \quad \checkmark$$

---

### Example 8 — Hard: Work-Energy with an Elastic String on a Horizontal Surface

> **Question:** A particle of mass $0.6\text{ kg}$ is attached to a light elastic string of natural length $1.0\text{ m}$ and modulus $30\text{ N}$. The other end of the string is attached to a fixed point $A$ on a smooth horizontal table. The particle is pulled to a point $1.8\text{ m}$ from $A$ and released from rest.
>
> (a) Find the speed of the particle when the string first becomes slack.
>
> (b) Describe the subsequent motion of the particle after the string becomes slack.

**Solution (a):**

| Step | Working |
|------|---------|
| **1** | $l = 1.0\text{ m}$, $\lambda = 30\text{ N}$, $m = 0.6\text{ kg}$ |
| **2** | Initial position: $1.8\text{ m}$ from $A$, extension $x_{0} = 1.8 - 1.0 = 0.8\text{ m}$ |
| **3** | String becomes slack when $x = 0$ (i.e. at $1.0\text{ m}$ from $A$) |
| **4** | Use energy conservation on the smooth table (no GPE change, no friction) |

Initial EPE:

$$E_{0} = \frac{\lambda x_{0}^{2}}{2l} = \frac{30 \times 0.8^{2}}{2 \times 1.0}$$

$$E_{0} = \frac{30 \times 0.64}{2}$$

$$E_{0} = 15 \times 0.64 = 9.6\text{ J}$$

At the point where the string becomes slack ($x = 0$): $E = 0$, so all EPE has been converted to KE.

$$\frac{1}{2}mv^{2} = E_{0}$$

$$\frac{1}{2} \times 0.6 \times v^{2} = 9.6$$

$$0.3v^{2} = 9.6$$

$$v^{2} = \frac{9.6}{0.3} = 32$$

$$v = \sqrt{32} = 4\sqrt{2} \approx 5.66\text{ m s}^{-1} \quad \checkmark$$

**Solution (b):**

After the string becomes slack ($x \leq 0$), the tension is zero:

$$T = 0$$

There are no horizontal forces on the particle (smooth table, slack string), so by Newton's first law:

$$a = 0 \quad\Longrightarrow\quad \text{particle continues with constant velocity } v = 4\sqrt{2}\text{ m s}^{-1}$$

The particle moves in a **straight line** with **constant speed** $4\sqrt{2}\text{ m s}^{-1}$ away from $A$ (or more precisely, continues in whatever direction it was moving when the string went slack — radially outward from $A$).

If the particle were constrained to move along a line through $A$ (e.g. in a groove), it would continue outward indefinitely at constant speed. If it could move freely on the table, it would move in a straight line at constant velocity.

> ⚠️ **Watch Out!** After the string goes slack, students sometimes continue to use Hooke's law with a negative extension. For a **string**, once $L \leq l$, the tension is **zero** — not negative. The particle is then in free motion. Only a **spring** would exert a thrust/compressive force for $L < l$.

### Example 9 — Easy: Elastic Spring in Compression (String vs Spring)

> **Question:** A light elastic **spring** has natural length $0.40\text{ m}$ and modulus of elasticity $60\text{ N}$.
>
> (a) The spring is compressed to a length of $0.30\text{ m}$. Find the thrust (compressive force) exerted by the spring.
>
> (b) Calculate the elastic potential energy stored in the compressed spring.
>
> (c) Explain what would happen if the spring were replaced by a light elastic **string** of the same natural length and modulus, and an attempt were made to compress it to $0.30\text{ m}$.

**Solution (a): Finding the thrust**

| Step | Working |
|------|---------|
| **1** | $l = 0.40\text{ m}$, $\lambda = 60\text{ N}$, $L = 0.30\text{ m}$ |
| **2** | Extension $x = L - l = 0.30 - 0.40 = -0.10\text{ m}$ (negative — compression) |
| **3** | For a **spring**, Hooke's law still applies with $x < 0$: $T = \dfrac{\lambda x}{l}$ |

$$x = L - l$$

$$x = 0.30 - 0.40$$

$$x = -0.10\text{ m}$$

$$T = \frac{\lambda x}{l}$$

$$T = \frac{60 \times (-0.10)}{0.40}$$

$$T = \frac{-6.0}{0.40}$$

$$T = -15\text{ N}$$

The negative sign indicates **thrust** (the spring pushes outward at each end). The magnitude of the compressive force is:

$$|T| = 15\text{ N (thrust)} \quad \checkmark$$

**Solution (b): Elastic potential energy when compressed**

$$E = \frac{\lambda x^{2}}{2l}$$

$$E = \frac{60 \times (-0.10)^{2}}{2 \times 0.40}$$

$$E = \frac{60 \times 0.01}{0.80}$$

$$E = \frac{0.60}{0.80}$$

$$E = 0.75\text{ J} \quad \checkmark$$

> 💡 **Note:** $x^{2} = (-0.10)^{2} = 0.01$ — the energy is **positive** even though $x$ is negative. A compressed spring still stores energy.

**Solution (c): String vs spring**

If the spring were replaced by an elastic **string** and compressed to $L = 0.30\text{ m} < l$:

$$x = 0.30 - 0.40 = -0.10\text{ m} < 0$$

For a **string**, a negative extension means the string is **slack**:

$$T = 0\text{ (string goes slack — it cannot support compression)}$$

$$E = 0\text{ (no energy stored when slack)}$$

The string would simply buckle/go limp and exert **no force**. This is the crucial string-vs-spring distinction that Cambridge examines.

> ⚠️ **Watch Out!** Students often apply $T = \frac{\lambda x}{l}$ blindly for a string and report a "negative tension" of $-15\text{ N}$. For a **string**, negative $x$ always means $T = 0$ (slack). Only a **spring** can have $T < 0$ representing a genuine thrust. If the question says **"string"**, check the sign of $x$ before calculating $T$.

> 🎯 **What the examiner wants:** When you see the word **"spring"** and $L < l$, the examiner expects you to recognise compression/thrust and still use $E = \frac{\lambda x^{2}}{2l}$ (energy is still stored). When you see **"string"** and $L < l$, they expect "$T = 0$, $E = 0$, string is slack." Stating this distinction explicitly earns method marks.

---

### Example 10 — Medium: Work-Energy with Friction on a Horizontal Surface

> **Question:** A particle of mass $0.5\text{ kg}$ is attached to a light elastic string of natural length $1.0\text{ m}$ and modulus $24\text{ N}$. The other end of the string is fixed at point $A$ on a **rough** horizontal table with coefficient of friction $\mu = 0.2$. The particle is pulled to a point $1.6\text{ m}$ from $A$ and released from rest. The particle moves towards $A$ in a straight line.
>
> (a) Find the speed of the particle when it has moved $0.3\text{ m}$ towards $A$ (i.e. when it is $1.3\text{ m}$ from $A$).
>
> (b) Determine whether the string is still taut at that position.
>
> Take $g = 10\text{ m s}^{-2}$.

**Solution (a):**

| Step | Working |
|------|---------|
| **1** | $l = 1.0\text{ m}$, $\lambda = 24\text{ N}$, $m = 0.5\text{ kg}$, $\mu = 0.2$ |
| **2** | Initial position: $L_{0} = 1.6\text{ m}$, $x_{0} = 1.6 - 1.0 = 0.60\text{ m}$ |
| **3** | Final position: $L_{1} = 1.3\text{ m}$, $x_{1} = 1.3 - 1.0 = 0.30\text{ m}$ |
| **4** | Distance moved: $d = 0.3\text{ m}$; friction does work $W_{f} = -\mu mg\, d$ |
| **5** | Use work-energy: $\Delta\text{KE} + \Delta\text{EPE} = W_{\text{friction}}$ |

Initial elastic potential energy:

$$E_{0} = \frac{\lambda x_{0}^{2}}{2l}$$

$$E_{0} = \frac{24 \times 0.60^{2}}{2 \times 1.0}$$

$$E_{0} = \frac{24 \times 0.36}{2}$$

$$E_{0} = 12 \times 0.36$$

$$E_{0} = 4.32\text{ J}$$

Final elastic potential energy (at $1.3\text{ m}$ from $A$):

$$E_{1} = \frac{\lambda x_{1}^{2}}{2l}$$

$$E_{1} = \frac{24 \times 0.30^{2}}{2 \times 1.0}$$

$$E_{1} = \frac{24 \times 0.09}{2}$$

$$E_{1} = 12 \times 0.09$$

$$E_{1} = 1.08\text{ J}$$

Work done against friction (friction opposes motion, so negative work):

$$W_{f} = -\mu mg\, d$$

$$W_{f} = -0.2 \times 0.5 \times 10 \times 0.3$$

$$W_{f} = -0.2 \times 5 \times 0.3$$

$$W_{f} = -0.30\text{ J}$$

Normal reaction on horizontal table:

$$R = mg = 0.5 \times 10 = 5\text{ N}$$

Frictional force:

$$F = \mu R = 0.2 \times 5 = 1.0\text{ N}$$

Work-energy equation (initial KE $= 0$, released from rest):

$$\text{KE}_{1} - \text{KE}_{0} + (E_{1} - E_{0}) = W_{f}$$

$$\frac{1}{2}mv^{2} - 0 + (1.08 - 4.32) = -0.30$$

$$\frac{1}{2} \times 0.5 \times v^{2} - 3.24 = -0.30$$

$$0.25v^{2} = 3.24 - 0.30$$

$$0.25v^{2} = 2.94$$

$$v^{2} = \frac{2.94}{0.25}$$

$$v^{2} = 11.76$$

$$v = \sqrt{11.76} \approx 3.43\text{ m s}^{-1} \quad \checkmark$$

**Solution (b):**

$$x_{1} = 1.3 - 1.0 = 0.30\text{ m} > 0$$

Since $x_{1} > 0$, the string is still **taut**:

$$T_{1} = \frac{\lambda x_{1}}{l} = \frac{24 \times 0.30}{1.0} = 7.2\text{ N} > 0 \quad \checkmark$$

> ⚠️ **Watch Out!** On a rough surface, you **cannot** use simple conservation of mechanical energy ($\text{KE} + \text{EPE} = \text{constant}$). You must account for the work done against friction: $\Delta(\text{KE} + \text{EPE}) = W_{\text{friction}} = -\mu mg\, d$. Forgetting the friction work is the most common error. Also, always check that the string is still taut at the final position — if $x \leq 0$ for a string, set $E = 0$ and $T = 0$ from that point onward.

> 🎯 **What the examiner wants:** Write the work-energy equation with **all three terms** explicitly: "By the work-energy principle: $\text{KE}_{1} + \text{EPE}_{1} - (\text{KE}_{0} + \text{EPE}_{0}) = -\mu mgd$." Defining $R = mg$ and $F = \mu R$ separately earns method marks even if the final speed is wrong.

---

### Example 11 — Hard: Elastic String on an Inclined Plane with Energy (Projected Down the Slope)

> **Question:** A smooth plane is inclined at $30^{\circ}$ to the horizontal. A light elastic string of natural length $0.8\text{ m}$ and modulus $48\text{ N}$ has one end attached to a fixed point $A$ at the top of the slope and the other end attached to a particle $P$ of mass $1.2\text{ kg}$. The string lies along the line of greatest slope.
>
> (a) Find the extension of the string when $P$ is in equilibrium on the plane.
>
> (b) $P$ is held at a point where the string has length $1.5\text{ m}$ (further down the slope than the equilibrium position) and released from rest. Find the speed of $P$ when it first passes through the equilibrium position.
>
> (c) Find the distance from $A$ to $P$ when the string first becomes slack (if it does) during the subsequent motion up the slope.
>
> Take $g = 10\text{ m s}^{-2}$.

**Solution (a): Equilibrium position**

| Step | Working |
|------|---------|
| **1** | $l = 0.8\text{ m}$, $\lambda = 48\text{ N}$, $m = 1.2\text{ kg}$, $\alpha = 30^{\circ}$ |
| **2** | Component of weight down slope: $mg\sin\alpha$ |
| **3** | Tension up slope: $T = \dfrac{\lambda x}{l}$ |
| **4** | At equilibrium: $T = mg\sin\alpha$ |

$$mg\sin30^{\circ} = \frac{\lambda x_{\text{eq}}}{l}$$

$$1.2 \times 10 \times \frac{1}{2} = \frac{48\, x_{\text{eq}}}{0.8}$$

$$6.0 = \frac{48\, x_{\text{eq}}}{0.8}$$

$$6.0 = 60\, x_{\text{eq}}$$

$$x_{\text{eq}} = \frac{6.0}{60}$$

$$x_{\text{eq}} = 0.10\text{ m} \quad \checkmark$$

Equilibrium length:

$$L_{\text{eq}} = l + x_{\text{eq}} = 0.80 + 0.10 = 0.90\text{ m from } A \quad \checkmark$$

**Solution (b): Speed through equilibrium**

Starting position: $L_{0} = 1.5\text{ m}$

$$x_{0} = 1.5 - 0.8 = 0.70\text{ m}$$

$$E_{0} = \frac{\lambda x_{0}^{2}}{2l}$$

$$E_{0} = \frac{48 \times 0.70^{2}}{2 \times 0.8}$$

$$E_{0} = \frac{48 \times 0.49}{1.6}$$

$$E_{0} = 30 \times 0.49$$

$$E_{0} = 14.7\text{ J}$$

At equilibrium:

$$x_{\text{eq}} = 0.10\text{ m}$$

$$E_{\text{eq}} = \frac{48 \times 0.10^{2}}{2 \times 0.8}$$

$$E_{\text{eq}} = \frac{48 \times 0.01}{1.6}$$

$$E_{\text{eq}} = 30 \times 0.01$$

$$E_{\text{eq}} = 0.30\text{ J}$$

Distance moved up the slope (from $1.5\text{ m}$ to $0.90\text{ m}$ from $A$):

$$d = 1.50 - 0.90 = 0.60\text{ m up the slope}$$

Vertical height gained:

$$h = d\sin30^{\circ}$$

$$h = 0.60 \times 0.5$$

$$h = 0.30\text{ m}$$

Gain in gravitational potential energy:

$$\Delta\text{GPE} = mgh$$

$$\Delta\text{GPE} = 1.2 \times 10 \times 0.30$$

$$\Delta\text{GPE} = 3.6\text{ J}$$

Energy conservation (smooth plane — no friction; string taut throughout this phase):

$$E_{0} = \frac{1}{2}mv^{2} + E_{\text{eq}} + mgh$$

$$14.7 = \frac{1}{2} \times 1.2 \times v^{2} + 0.30 + 3.6$$

$$14.7 = 0.6v^{2} + 3.90$$

$$0.6v^{2} = 14.7 - 3.90$$

$$0.6v^{2} = 10.8$$

$$v^{2} = \frac{10.8}{0.6}$$

$$v^{2} = 18$$

$$v = \sqrt{18} = 3\sqrt{2} \approx 4.24\text{ m s}^{-1} \quad \checkmark$$

**Solution (c): Does the string go slack?**

After passing through equilibrium, the particle continues **up** the slope. The string extension decreases. It becomes slack when $L = l = 0.80\text{ m}$, i.e. when the particle is $0.80\text{ m}$ from $A$.

Check whether the particle has enough energy to reach that point. Distance from equilibrium to slack point:

$$d_{2} = 0.90 - 0.80 = 0.10\text{ m up the slope}$$

Height gained from equilibrium to slack point:

$$h_{2} = 0.10\sin30^{\circ}$$

$$h_{2} = 0.10 \times 0.5$$

$$h_{2} = 0.05\text{ m}$$

Energy at equilibrium: $\text{KE}_{\text{eq}} + E_{\text{eq}} + \text{GPE}_{\text{eq}}$

Take GPE datum at the equilibrium position ($\text{GPE}_{\text{eq}} = 0$):

$$\text{KE}_{\text{eq}} = \frac{1}{2} \times 1.2 \times 18$$

$$\text{KE}_{\text{eq}} = 0.6 \times 18$$

$$\text{KE}_{\text{eq}} = 10.8\text{ J}$$

At the slack point ($E = 0$), let speed be $v_{s}$:

$$\text{KE}_{\text{eq}} + E_{\text{eq}} = \frac{1}{2}mv_{s}^{2} + 0 + mgh_{2}$$

$$10.8 + 0.30 = \frac{1}{2} \times 1.2 \times v_{s}^{2} + 1.2 \times 10 \times 0.05$$

$$11.1 = 0.6v_{s}^{2} + 0.60$$

$$0.6v_{s}^{2} = 11.1 - 0.60$$

$$0.6v_{s}^{2} = 10.5$$

$$v_{s}^{2} = \frac{10.5}{0.6}$$

$$v_{s}^{2} = 17.5$$

$$v_{s} = \sqrt{17.5} \approx 4.18\text{ m s}^{-1} > 0$$

Since $v_{s} > 0$, the particle **does** reach the slack point with non-zero speed. The string first becomes slack when:

$$L = 0.80\text{ m from } A \quad \checkmark$$

Beyond this point the string is slack ($T = 0$, $E = 0$) and the particle continues up the slope as a projectile on the incline (decelerating under $mg\sin30^{\circ}$) until it momentarily comes to rest.

> ⚠️ **Watch Out!** In part (c), many students assume the string never goes slack because the particle "oscillates about equilibrium." But here the initial amplitude ($0.60\text{ m}$ beyond equilibrium) exceeds the equilibrium extension ($0.10\text{ m}$), so the particle easily passes the natural length. **Always check** whether the amplitude exceeds $x_{\text{eq}}$ — if it does, the string goes slack on the upswing.

> 🎯 **What the examiner wants:** For inclined-plane energy problems, explicitly state your GPE datum and show the vertical height as $h = d\sin\alpha$. Write every energy term (KE + GPE + EPE) at each position. In part (c), the examiner awards marks for (i) identifying the slack condition $L = l$, (ii) checking energy to confirm the particle reaches that point, and (iii) stating that beyond slack, $T = 0$.

---

---

# 14. Common Mistakes

### ❌ Mistake 1: Confusing natural length $l$ with extended length $L$ or extension $x$

> ✅ Always be crystal clear: $l$ = natural (unstretched) length, $L$ = current stretched length, $x = L - l$ = extension. When the question says "the string has length $1.5\text{ m}$", that is $L$, not $x$. You must subtract $l$ to get $x$ before applying Hooke's law.

### ❌ Mistake 2: Using a negative extension for an elastic string

> ✅ An elastic **string** cannot support compression. If $L \leq l$, the string is **slack** and $T = 0$, $E = 0$. Never plug a negative $x$ into $T = \frac{\lambda x}{l}$ for a string. (For a **spring**, negative $x$ gives a valid thrust.)

### ❌ Mistake 3: Forgetting the factor of $\frac{1}{2}$ in elastic potential energy

> ✅ The correct formula is $E = \dfrac{\lambda x^{2}}{2l}$, **not** $\dfrac{\lambda x^{2}}{l}$. Think of it as the area of a triangle: $E = \frac{1}{2}Tx = \frac{1}{2}\cdot\frac{\lambda x}{l}\cdot x$.

### ❌ Mistake 4: Writing $\lambda = kx$ or mixing up $\lambda$ and $k$

> ✅ $\lambda$ has units of **force** (N); $k$ has units of $\text{N m}^{-1}$. The relations are $T = \frac{\lambda x}{l}$ and $T = kx$ where $k = \frac{\lambda}{l}$. So $\lambda = kl$, not $\lambda = k$.

### ❌ Mistake 5: Forgetting the free-fall phase when a particle is dropped from the suspension point

> ✅ If a particle is released from the fixed point $O$ itself, it falls distance $l$ (the natural length) **freely** under gravity before the string becomes taut. The total energy equation must account for the full distance fallen $d$, while EPE only involves $x = d - l$. Don't write $mgx = \frac{\lambda x^{2}}{2l}$ — it should be $mgd = \frac{\lambda(d-l)^{2}}{2l}$.

### ❌ Mistake 6: Rejecting the wrong root (or not rejecting any root) in energy quadratics

> ✅ When energy conservation gives a quadratic for the distance fallen (as in Example 4), one root will have $d < l$ (string slack — invalid for the taut-string energy equation). Always check that $d > l$ and reject roots where the string would be slack.

### ❌ Mistake 7: Using weight $mg$ as mass $m$ in Hooke's law

> ✅ Hooke's law gives a **force** (tension). At equilibrium $T = mg$ (a force equals a force). Don't write $T = m$ or $x = \frac{ml}{\lambda}$ — it must be $x = \frac{mgl}{\lambda}$.

### ❌ Mistake 8: Incorrect radius in the conical pendulum

> ✅ The radius of the circular path is $r = L\sin\theta = (l + x)\sin\theta$ where $L$ is the **stretched** length, not the natural length. Students often use $r = l\sin\theta$ — this is wrong. You must use the extended length.

### ❌ Mistake 9: Sign errors in the work-energy equation with inclined planes

> ✅ When a particle moves **down** the slope, GPE **decreases** (energy released); when it moves **up**, GPE **increases**. Be consistent with your datum. If measuring $h$ upward from the lowest point, then moving down means $h$ decreases. Double-check every sign.

### ❌ Mistake 10: Applying elastic potential energy when the string is slack

> ✅ If a problem involves a phase where the elastic **string** is slack (e.g. a particle bouncing, or passing through the natural length), set $E = 0$ for that phase. Do not calculate $E = \frac{\lambda x^{2}}{2l}$ with a negative or zero $x$ and include it — while $0^{2} = 0$ happens to give $E = 0$, a negative $x$ for a string should not be squared blindly; conceptually $E = 0$ because the string stores no energy when slack.

### ❌ Mistake 11: Confusing modulus $\lambda$ with Young's modulus

> ✅ In 9231 Further Mechanics, $\lambda$ is the **modulus of elasticity of the string/spring** (units: N), defined by $T = \frac{\lambda x}{l}$. This is **not** Young's modulus $E$ from materials science (units: Pa = $\text{N m}^{-2}$). They are related by $\lambda = EA/l$ where $A$ is cross-sectional area, but Cambridge will always give or ask for $\lambda$ directly.

### ❌ Mistake 12: Not checking that both strings/springs are taut in two-string problems

> ✅ When a particle is between two fixed points with two elastic connections (Example 5), verify at the end that **both** are taut ($x_{1} > 0$ and $x_{2} > 0$). If one goes slack, the equilibrium condition changes — you no longer have $T_{1} = T_{2}$.

---

# 15. Complete Formula Sheet

## Hooke's Law

| Formula | Description |
|---------|-------------|
| $$T = \dfrac{\lambda x}{l}$$ | Hooke's law — tension in terms of modulus |
| $$T = kx$$ | Hooke's law — tension in terms of stiffness |
| $$k = \dfrac{\lambda}{l}$$ | Relation between stiffness and modulus |
| $$x = L - l$$ | Extension (stretched length minus natural length) |

## Elastic Potential Energy

| Formula | Description |
|---------|-------------|
| $$E = \dfrac{\lambda x^{2}}{2l}$$ | Elastic potential energy (modulus form) |
| $$E = \dfrac{1}{2}kx^{2}$$ | Elastic potential energy (stiffness form) |
| $$E = \dfrac{T^{2}l}{2\lambda}$$ | Elastic potential energy (tension form) |
| $$E = \dfrac{1}{2}Tx$$ | Elastic potential energy (tension × extension) |
| $$E = 0 \text{ if string is slack }(x \leq 0)$$ | No energy stored when string goes slack |

## Vertical Equilibrium

| Formula | Description |
|---------|-------------|
| $$mg = \dfrac{\lambda x}{l}$$ | Extension when hanging in vertical equilibrium |
| $$x_{\text{eq}} = \dfrac{mgl}{\lambda}$$ | Equilibrium extension (vertical) |
| $$L_{\text{eq}} = l\left(1 + \dfrac{mg}{\lambda}\right)$$ | Equilibrium length (vertical) |

## Inclined Plane

| Formula | Description |
|---------|-------------|
| $$mg\sin\alpha = \dfrac{\lambda x}{l}$$ | Equilibrium on smooth inclined plane (angle $\alpha$) |
| $$R = mg\cos\alpha$$ | Normal reaction on inclined plane |
| $$\left|mg\sin\alpha - \dfrac{\lambda x}{l}\right| \leq \mu R$$ | Equilibrium condition on rough inclined plane |

## Conical Pendulum (Elastic String)

| Formula | Description |
|---------|-------------|
| $$T\cos\theta = mg$$ | Vertical equilibrium |
| $$T\sin\theta = mr\omega^{2} = \dfrac{mv^{2}}{r}$$ | Horizontal (centripetal force) |
| $$r = (l + x)\sin\theta$$ | Radius of circular path (stretched length!) |
| $$T = \dfrac{\lambda x}{l}$$ | Tension from Hooke's law |
| $$\tan\theta = \dfrac{r\omega^{2}}{g}$$ | Angle–angular speed relation |
| $$\omega^{2} = \dfrac{g}{(l+x)\cos\theta}$$ | Angular speed formula |

## Two Elastic Strings (Particle Between Fixed Points $A$, $B$ Distance $d$ Apart)

| Formula | Description |
|---------|-------------|
| $$T_{1} = \dfrac{\lambda_{1}(y - l_{1})}{l_{1}}$$ | Tension in string from $A$ (particle at distance $y$ from $A$) |
| $$T_{2} = \dfrac{\lambda_{2}(d - y - l_{2})}{l_{2}}$$ | Tension in string/spring to $B$ |
| $$T_{1} = T_{2}$$ | Equilibrium on smooth horizontal line |

## Conservation of Energy (with Elasticity)

| Formula | Description |
|---------|-------------|
| $$\dfrac{1}{2}mv_{1}^{2} + mgh_{1} + \dfrac{\lambda x_{1}^{2}}{2l} = \dfrac{1}{2}mv_{2}^{2} + mgh_{2} + \dfrac{\lambda x_{2}^{2}}{2l}$$ | Conservation of mechanical energy (no friction) |
| $$\Delta(\text{KE} + \text{GPE} + \text{EPE}) = W_{\text{nc}}$$ | Work-energy with non-conservative work |
| $$W_{\text{elastic}} = \dfrac{\lambda x_{1}^{2}}{2l} - \dfrac{\lambda x_{2}^{2}}{2l}$$ | Work done by elastic force |

## Useful GPE + EPE Combinations

| Situation | Energy Equation |
|-----------|----------------|
| Particle dropped from $O$ (string natural length $l$), falls total distance $d > l$ | $$mgd = \dfrac{\lambda(d-l)^{2}}{2l} + \dfrac{1}{2}mv^{2}$$ (if not at rest at $d$) |
| Particle at max extension (instantaneously at rest) | $$mgd_{\max} = \dfrac{\lambda(d_{\max}-l)^{2}}{2l}$$ |

---

# 16. Cambridge Exam Analysis

## Topic Frequency

| Topic | Typical Marks | Frequency |
|-------|---------------|-----------|
| Finding $\lambda$ or $l$ from equilibrium data | 3–5 marks | Very common |
| Vertical equilibrium with elastic string | 3–5 marks | Very common |
| Elastic potential energy calculation | 2–4 marks | Common |
| Energy conservation with elastic string (particle dropped / projected) | 5–8 marks | Very common |
| Particle between two elastic strings (equilibrium + energy) | 6–10 marks | Common |
| Inclined plane with elastic string | 4–7 marks | Common |
| Conical pendulum with elastic string | 5–8 marks | Common |
| Work-energy with rough surface + elasticity | 6–9 marks | Occasional |
| Combined equilibrium + energy in one question | 8–12 marks | Very common |

## Past Paper Trends (9231 Further Mechanics)

- **Hooke's law questions appear on almost every 9231 Further Mechanics paper**, typically as Question 1 or 2 (the more accessible questions, worth 7–11 marks).
- The most common question structure is a **two-part question**: (a) find the extension/modulus/natural length from equilibrium (3–4 marks), then (b) use **energy conservation** to find a speed or maximum extension (5–7 marks).
- **Particle dropped from the suspension point** is the single most common energy scenario — examiners love the subtlety that the particle falls distance $l$ freely before the string goes taut.
- **Two-string problems** (particle between two fixed points) test both equilibrium ($T_{1} = T_{2}$) and energy, often requiring you to find the equilibrium position first and then calculate oscillations or speeds.
- **Conical pendulum** with an elastic string is a favourite "harder" question combining Hooke's law with circular motion. The key is remembering $r = (l+x)\sin\theta$ with the **stretched** length.
- **Inclined plane** variants usually involve a smooth plane (straightforward $mg\sin\alpha = T$) or ask for the **range** of equilibrium positions on a rough plane.
- The **EPE formula is given** in the formula booklet: $E = \frac{\lambda x^{2}}{2l}$. You won't need to derive it, but you must apply it correctly (especially knowing when $E = 0$ for a slack string).

## What to Expect

> ⚠️ **Exam Tips:**
> - **Always state Hooke's law** explicitly: write "$T = \frac{\lambda x}{l}$" so the examiner sees your method, even if the final answer is wrong.
> - **Show every step** when solving for $\lambda$ and $l$ simultaneously — the division method ($\frac{T_{1}}{T_{2}} = \frac{L_{1}-l}{L_{2}-l}$) earns method marks.
> - For **energy questions**, clearly state "By conservation of energy:" and list all terms (KE + GPE + EPE) at each position. Define your GPE datum.
> - When a particle is **dropped from $O$**, explicitly note "the particle falls $l$ freely before the string becomes taut" — this shows understanding and earns marks.
> - For the **conical pendulum**, always write both $T\cos\theta = mg$ and $T\sin\theta = mr\omega^{2}$ — these two equations are the foundation; marks are awarded for each.
> - **Check that strings are taut** at every stage. If your calculated extension is negative for a string, state "string is slack, so $T = 0$".
> - Use $g = 10\text{ m s}^{-2}$ unless the question says otherwise — many Cambridge questions use $g = 10$ for cleaner arithmetic.
> - Give answers to **3 significant figures** unless an exact form is requested.

> 🎯 **What the examiner wants — Hooke's Law (9231 §3.4):**
> 1. **State Hooke's law explicitly** — always write "$T = \frac{\lambda x}{l}$" or "$T = kx$" before substituting. This earns the M1 even if arithmetic slips.
> 2. **Distinguish string vs spring** — if $L \leq l$ for a **string**, write "string is slack so $T = 0$, $E = 0$." For a **spring**, allow $x < 0$ and compute the thrust. Examiners award a B1 for this distinction.
> 3. **Show the extension calculation** — write "$x = L - l = ...$" as a separate line. Never jump straight to $T$ without showing $x$.
> 4. **Energy: list every term** — write "By conservation of energy: $\text{KE}_{1} + \text{GPE}_{1} + \text{EPE}_{1} = \text{KE}_{2} + \text{GPE}_{2} + \text{EPE}_{2}$" with all six terms identified (use $E = \frac{\lambda x^{2}}{2l}$). Define your GPE datum. Missing terms cost marks.
> 5. **Check physical validity** — after solving, verify $x > 0$ (taut) or state "string goes slack." For conical pendulums, verify $r = (l+x)\sin\theta$ uses the **stretched** length. Examiners penalise $r = l\sin\theta$.
> 6. **Reject extraneous roots** — when a quadratic gives two values of $d$, explicitly reject the root with $d < l$ ("string would be slack, so discard"). Stating the reason earns the final A1.

---

## Mark Allocation Strategy

| Marks | What Earns Them |
|-------|----------------|
| M1 | Correct application of Hooke's law ($T = \frac{\lambda x}{l}$) |
| M1 | Correct equilibrium condition or energy equation |
| A1 | Correct algebraic manipulation |
| A1 | Correct final answer (with units where appropriate) |
| B1 | Correct statement of EPE formula or identification of slack/taut |

---

# 17. Practice Questions & Full Solutions

---

## Question 1 — Easy: Basic Hooke's Law

> A light elastic string has natural length $0.75\text{ m}$ and modulus of elasticity $60\text{ N}$. Find the tension in the string when its length is $1.05\text{ m}$.

**Solution:**

$$l = 0.75\text{ m}, \quad \lambda = 60\text{ N}, \quad L = 1.05\text{ m}$$

$$x = L - l = 1.05 - 0.75 = 0.30\text{ m}$$

$$T = \frac{\lambda x}{l} = \frac{60 \times 0.30}{0.75}$$

$$T = \frac{18}{0.75} = 24\text{ N} \quad \checkmark$$

---

## Question 2 — Easy: Finding Natural Length

> A light elastic spring has modulus $48\text{ N}$. When a force of $12\text{ N}$ is applied, the spring has length $0.9\text{ m}$. Find the natural length of the spring.

**Solution:**

$$T = 12\text{ N}, \quad \lambda = 48\text{ N}, \quad L = 0.9\text{ m}, \quad l = \,?$$

$$T = \frac{\lambda(L - l)}{l}$$

$$12 = \frac{48(0.9 - l)}{l}$$

$$12l = 48(0.9 - l)$$

$$12l = 43.2 - 48l$$

$$60l = 43.2$$

$$l = \frac{43.2}{60} = 0.72\text{ m} \quad \checkmark$$

---

## Question 3 — Easy: Elastic Potential Energy

> A light elastic string has natural length $1.0\text{ m}$ and modulus $80\text{ N}$. The string is stretched to a length of $1.4\text{ m}$. Calculate the elastic potential energy stored in the string.

**Solution:**

$$l = 1.0\text{ m}, \quad \lambda = 80\text{ N}, \quad L = 1.4\text{ m}$$

$$x = 1.4 - 1.0 = 0.4\text{ m}$$

$$E = \frac{\lambda x^{2}}{2l} = \frac{80 \times 0.4^{2}}{2 \times 1.0}$$

$$E = \frac{80 \times 0.16}{2}$$

$$E = \frac{12.8}{2} = 6.4\text{ J} \quad \checkmark$$

---

## Question 4 — Medium: Vertical Equilibrium — Two Different Masses

> A light elastic string has natural length $0.9\text{ m}$. When a particle of mass $1.5\text{ kg}$ hangs in equilibrium from the string, its length is $1.2\text{ m}$.
>
> (a) Find the modulus of elasticity of the string.
>
> (b) Find the length of the string when a particle of mass $2.5\text{ kg}$ hangs in equilibrium from it.
>
> Take $g = 10\text{ m s}^{-2}$.

**Solution (a):**

$$l = 0.9\text{ m}, \quad L_{1} = 1.2\text{ m}, \quad x_{1} = 0.3\text{ m}, \quad m_{1} = 1.5\text{ kg}$$

At equilibrium:

$$m_{1}g = \frac{\lambda x_{1}}{l}$$

$$1.5 \times 10 = \frac{\lambda \times 0.3}{0.9}$$

$$15 = \frac{0.3\lambda}{0.9}$$

$$\lambda = \frac{15 \times 0.9}{0.3} = \frac{13.5}{0.3} = 45\text{ N} \quad \checkmark$$

**Solution (b):**

For $m_{2} = 2.5\text{ kg}$:

$$m_{2}g = \frac{\lambda x_{2}}{l}$$

$$2.5 \times 10 = \frac{45x_{2}}{0.9}$$

$$25 = \frac{45x_{2}}{0.9}$$

$$x_{2} = \frac{25 \times 0.9}{45} = \frac{22.5}{45} = 0.5\text{ m}$$

$$L_{2} = l + x_{2} = 0.9 + 0.5 = 1.4\text{ m} \quad \checkmark$$

---

## Question 5 — Medium: Particle Between Two Strings — Finding Modulus

> Two fixed points $A$ and $B$ are $2.5\text{ m}$ apart on a smooth horizontal table. A particle of mass $0.8\text{ kg}$ is attached to $A$ by a light elastic string of natural length $0.6\text{ m}$ and to $B$ by a light elastic string of natural length $1.0\text{ m}$. Both strings have the same modulus of elasticity $\lambda$. The particle is in equilibrium $1.4\text{ m}$ from $A$. Find $\lambda$ given that a horizontal force of $12\text{ N}$ is applied to the particle towards $B$ to maintain this equilibrium position.
>
> *Note: In the absence of the applied force, the equilibrium would be at a different position. Here the $12\text{ N}$ force holds the particle at $1.4\text{ m}$ from $A$.*

**Solution:**

$$y = 1.4\text{ m from } A, \quad d = 2.5\text{ m}, \quad l_{1} = 0.6\text{ m}, \quad l_{2} = 1.0\text{ m}$$

String $AP$: length $= 1.4\text{ m}$, extension $x_{1} = 1.4 - 0.6 = 0.8\text{ m}$

$$T_{1} = \frac{\lambda \times 0.8}{0.6} = \frac{4\lambda}{3}$$

String $BP$: length $= 2.5 - 1.4 = 1.1\text{ m}$, extension $x_{2} = 1.1 - 1.0 = 0.1\text{ m}$

$$T_{2} = \frac{\lambda \times 0.1}{1.0} = 0.1\lambda$$

Forces on particle: $T_{1}$ towards $A$ (left), $T_{2}$ towards $B$ (right), applied force $12\text{ N}$ towards $B$ (right).

Equilibrium: forces to the right $=$ forces to the left:

$$T_{2} + 12 = T_{1}$$

$$0.1\lambda + 12 = \frac{4\lambda}{3}$$

$$12 = \frac{4\lambda}{3} - 0.1\lambda$$

$$12 = \frac{4\lambda}{3} - \frac{\lambda}{10}$$

$$12 = \frac{40\lambda - 3\lambda}{30}$$

$$12 = \frac{37\lambda}{30}$$

$$\lambda = \frac{12 \times 30}{37} = \frac{360}{37} \approx 9.73\text{ N} \quad \checkmark$$

---

## Question 6 — Medium: Energy — Particle Pulled and Released on Horizontal Table

> A light elastic string has natural length $0.8\text{ m}$ and modulus $36\text{ N}$. One end is fixed at point $A$ on a smooth horizontal table. A particle of mass $0.4\text{ kg}$ is attached to the other end. The particle is pulled to a point $1.3\text{ m}$ from $A$ and released from rest.
>
> (a) Find the speed of the particle when it is $1.0\text{ m}$ from $A$.
>
> (b) Find the speed when the string first becomes slack.

**Solution (a):**

Initial position: $L_{0} = 1.3\text{ m}$, $x_{0} = 1.3 - 0.8 = 0.5\text{ m}$

$$E_{0} = \frac{36 \times 0.5^{2}}{2 \times 0.8} = \frac{36 \times 0.25}{1.6} = \frac{9}{1.6} = 5.625\text{ J}$$

At $1.0\text{ m}$ from $A$: $x = 1.0 - 0.8 = 0.2\text{ m}$

$$E_{1} = \frac{36 \times 0.2^{2}}{2 \times 0.8} = \frac{36 \times 0.04}{1.6} = \frac{1.44}{1.6} = 0.9\text{ J}$$

Energy conservation (smooth table, no GPE change):

$$\frac{1}{2}mv^{2} + E_{1} = E_{0}$$

$$\frac{1}{2} \times 0.4 \times v^{2} + 0.9 = 5.625$$

$$0.2v^{2} = 5.625 - 0.9 = 4.725$$

$$v^{2} = \frac{4.725}{0.2} = 23.625$$

$$v = \sqrt{23.625} \approx 4.86\text{ m s}^{-1} \quad \checkmark$$

**Solution (b):**

String becomes slack at $x = 0$ (i.e. at $0.8\text{ m}$ from $A$): $E = 0$

$$\frac{1}{2} \times 0.4 \times v^{2} = 5.625$$

$$0.2v^{2} = 5.625$$

$$v^{2} = 28.125$$

$$v = \sqrt{28.125} \approx 5.30\text{ m s}^{-1} \quad \checkmark$$

---

## Question 7 — Hard: Vertical Drop — Maximum Extension

> A light elastic string has natural length $1.5\text{ m}$ and modulus $90\text{ N}$. One end is attached to a fixed point $O$. A particle of mass $3\text{ kg}$ is attached to the other end. The particle is held at the level of $O$ and released from rest. Find the maximum extension of the string.
>
> Take $g = 10\text{ m s}^{-2}$.

**Solution:**

$$l = 1.5\text{ m}, \quad \lambda = 90\text{ N}, \quad m = 3\text{ kg}$$

Let $d$ = total distance fallen when particle first comes to rest (maximum extension $x_{\max} = d - l$).

Energy conservation: loss of GPE = gain in EPE (KE $= 0$ at both ends).

$$mgd = \frac{\lambda(d - l)^{2}}{2l}$$

$$3 \times 10 \times d = \frac{90(d - 1.5)^{2}}{2 \times 1.5}$$

$$30d = \frac{90(d - 1.5)^{2}}{3}$$

$$30d = 30(d - 1.5)^{2}$$

$$d = (d - 1.5)^{2}$$

Let $x = d - 1.5$ (the maximum extension), so $d = x + 1.5$:

$$x + 1.5 = x^{2}$$

$$x^{2} - x - 1.5 = 0$$

$$x = \frac{1 \pm \sqrt{1 + 6}}{2} = \frac{1 \pm \sqrt{7}}{2}$$

$$x = \frac{1 + \sqrt{7}}{2} \approx \frac{1 + 2.6458}{2} \approx 1.823\text{ m}$$

(The negative root $x = \frac{1 - \sqrt{7}}{2} < 0$ is rejected — the string must be taut.)

$$x_{\max} = \frac{1 + \sqrt{7}}{2} \approx 1.82\text{ m} \quad \checkmark$$

Total distance fallen: $d = 1.5 + 1.823 = 3.323\text{ m}$.

> 💡 **Check via alternative method:** At maximum extension, we could also write the energy equation directly in terms of $x$:
>
> $$mg(l + x) = \frac{\lambda x^{2}}{2l}$$
>
> $$30(1.5 + x) = \frac{90x^{2}}{3} = 30x^{2}$$
>
> $$1.5 + x = x^{2} \implies x^{2} - x - 1.5 = 0$$
>
> Same quadratic. $\checkmark$

---

## Question 8 — Hard: Inclined Plane — Energy with Elastic String

> A particle of mass $1.5\text{ kg}$ is attached to a light elastic string of natural length $0.6\text{ m}$ and modulus $45\text{ N}$. The other end of the string is attached to a fixed point at the top of a smooth plane inclined at $30^{\circ}$ to the horizontal. The string lies along the line of greatest slope. The particle is held at a point where the string has length $1.2\text{ m}$ and released from rest. Find the speed of the particle when the string first becomes slack.
>
> Take $g = 10\text{ m s}^{-2}$.

**Solution:**

$$l = 0.6\text{ m}, \quad \lambda = 45\text{ N}, \quad m = 1.5\text{ kg}, \quad \alpha = 30^{\circ}$$

Initial position: $L_{0} = 1.2\text{ m}$, $x_{0} = 1.2 - 0.6 = 0.6\text{ m}$

$$E_{0} = \frac{45 \times 0.6^{2}}{2 \times 0.6} = \frac{45 \times 0.36}{1.2} = \frac{16.2}{1.2} = 13.5\text{ J}$$

String becomes slack when $L = l = 0.6\text{ m}$, i.e. after the particle has moved $1.2 - 0.6 = 0.6\text{ m}$ **up** the slope.

Vertical height gained:

$$h = 0.6\sin30^{\circ} = 0.6 \times 0.5 = 0.3\text{ m}$$

Gain in GPE:

$$\Delta\text{GPE} = mgh = 1.5 \times 10 \times 0.3 = 4.5\text{ J}$$

When string becomes slack: $E = 0$.

Energy conservation (initial EPE → KE + GPE):

$$E_{0} = \frac{1}{2}mv^{2} + mgh + 0$$

$$13.5 = \frac{1}{2} \times 1.5 \times v^{2} + 4.5$$

$$0.75v^{2} = 13.5 - 4.5 = 9.0$$

$$v^{2} = \frac{9.0}{0.75} = 12$$

$$v = \sqrt{12} = 2\sqrt{3} \approx 3.46\text{ m s}^{-1} \quad \checkmark$$

---

## Question 9 — Hard: Conical Pendulum — Finding the Angular Speed

> A particle of mass $0.6\text{ kg}$ is attached to a light elastic string of natural length $0.8\text{ m}$ and modulus $48\text{ N}$. The other end is attached to a fixed point $O$. The particle whirls in a horizontal circle with the string making an angle of $60^{\circ}$ with the vertical. Find:
>
> (a) the extension of the string,
>
> (b) the angular speed $\omega$ of the particle.
>
> Take $g = 10\text{ m s}^{-2}$.

**Solution (a): Extension**

$$m = 0.6\text{ kg}, \quad l = 0.80\text{ m}, \quad \lambda = 48\text{ N}, \quad \theta = 60^{\circ}$$

Let $x$ = extension, so $L = l + x$ and:

$$T = \frac{\lambda x}{l} = \frac{48x}{0.80} = 60x$$

**Vertical equilibrium:**

$$T\cos60^{\circ} = mg$$

$$T \times \frac{1}{2} = 0.6 \times 10$$

$$\frac{T}{2} = 6$$

$$T = 12\text{ N}$$

Now find $x$ from Hooke's law:

$$T = \frac{\lambda x}{l}$$

$$12 = \frac{48x}{0.80}$$

$$12 = 60x$$

$$x = \frac{12}{60}$$

$$x = 0.20\text{ m} \quad \checkmark$$

Stretched length:

$$L = 0.80 + 0.20 = 1.00\text{ m}$$

> ✅ **Check:** $x = 0.20 > 0$ — string is taut. $L = 1.00\text{ m} > l$ ✓.

**Solution (b): Angular speed**

Radius of the circular path:

$$r = L\sin\theta$$

$$r = 1.00 \times \sin60^{\circ}$$

$$r = 1.00 \times \frac{\sqrt{3}}{2}$$

$$r = \frac{\sqrt{3}}{2}\text{ m} \approx 0.866\text{ m}$$

**Horizontal (centripetal force):**

$$T\sin\theta = mr\omega^{2}$$

$$12 \times \sin60^{\circ} = 0.6 \times r \times \omega^{2}$$

$$12 \times \frac{\sqrt{3}}{2} = 0.6 \times \frac{\sqrt{3}}{2} \times \omega^{2}$$

$$6\sqrt{3} = 0.3\sqrt{3}\, \omega^{2}$$

$$\omega^{2} = \frac{6\sqrt{3}}{0.3\sqrt{3}}$$

$$\omega^{2} = \frac{6}{0.3}$$

$$\omega^{2} = 20$$

$$\omega = \sqrt{20} = 2\sqrt{5} \approx 4.47\text{ rad s}^{-1} \quad \checkmark$$

> 💡 **Alternative via $\tan\theta$:** Dividing horizontal by vertical: $\tan\theta = \dfrac{r\omega^{2}}{g}$.

$$\tan60^{\circ} = \frac{r\,\omega^{2}}{g}$$

$$\sqrt{3} = \frac{\frac{\sqrt{3}}{2}\,\omega^{2}}{10}$$

$$\sqrt{3} = \frac{\sqrt{3}\,\omega^{2}}{20}$$

$$\omega^{2} = 20$$

$$\omega = 2\sqrt{5}\text{ rad s}^{-1} \quad \checkmark$$

> ⚠️ **Watch Out!** The radius is $r = L\sin\theta = (l + x)\sin\theta$ using the **stretched** length $L$, not $r = l\sin\theta$. Using the natural length gives the wrong radius and a wrong $\omega$. Always compute $L = l + x$ first.


---

## Question 10 — Hard: Combined Equilibrium and Energy — Exam Style

> A light elastic string has natural length $0.5\text{ m}$ and modulus $20\text{ N}$. One end is attached to a fixed point $A$. A particle of mass $0.3\text{ kg}$ is attached to the other end.
>
> (a) Find the extension of the string when the particle hangs in equilibrium vertically below $A$.
>
> (b) The particle is now pulled down a further $0.2\text{ m}$ from its equilibrium position and released from rest. Find the speed of the particle when it first passes through the equilibrium position.
>
> Take $g = 10\text{ m s}^{-2}$.

**Solution (a):**

$$l = 0.5\text{ m}, \quad \lambda = 20\text{ N}, \quad m = 0.3\text{ kg}$$

At equilibrium:

$$mg = \frac{\lambda x_{\text{eq}}}{l}$$

$$0.3 \times 10 = \frac{20x_{\text{eq}}}{0.5}$$

$$3 = 40x_{\text{eq}}$$

$$x_{\text{eq}} = \frac{3}{40} = 0.075\text{ m} \quad \checkmark$$

Equilibrium length: $L_{\text{eq}} = 0.5 + 0.075 = 0.575\text{ m}$ below $A$.

**Solution (b):**

The particle is pulled $0.2\text{ m}$ further down, so its starting position is $0.075 + 0.2 = 0.275\text{ m}$ extension:

$$x_{0} = 0.275\text{ m}, \quad L_{0} = 0.775\text{ m below } A$$

At equilibrium position: $x_{\text{eq}} = 0.075\text{ m}$.

Use energy conservation. Take GPE datum at the equilibrium position (or at $A$ — either works, but datum at equilibrium is convenient).

**Method: GPE datum at equilibrium position** (so GPE $= 0$ at equilibrium, GPE $= -mg \times 0.2$ at the release point which is $0.2\text{ m}$ below equilibrium — wait, the release point is BELOW equilibrium, so relative to equilibrium datum, the release point is $0.2\text{ m}$ lower, meaning GPE there is $-0.2mg$ if we measure height upward).

Let me use datum at the **release point** or more clearly, track all energies.

**Clearest method: GPE measured upward from the release point.**

- Release point: $h = 0$, $x_{0} = 0.275\text{ m}$
- Equilibrium position: $h = 0.2\text{ m}$ above release point (particle moves UP to equilibrium)

$$E_{0} = \frac{20 \times 0.275^{2}}{2 \times 0.5} = \frac{20 \times 0.075625}{1.0} = 1.5125\text{ J}$$

Actually:

$$E_{0} = \frac{20 \times 0.275^{2}}{2 \times 0.5} = \frac{20 \times 0.075625}{1.0}$$

$$E_{0} = 20 \times 0.075625 = 1.5125\text{ J}$$

Wait, let me recalculate: $\frac{\lambda x^{2}}{2l} = \frac{20 \times 0.275^{2}}{2 \times 0.5} = \frac{20 \times 0.075625}{1} = 1.5125\text{ J}$.

$$E_{\text{eq}} = \frac{20 \times 0.075^{2}}{2 \times 0.5} = \frac{20 \times 0.005625}{1} = 0.1125\text{ J}$$

Energy at release (KE $= 0$):

$$\text{Total}_{0} = \text{KE}_{0} + \text{GPE}_{0} + \text{EPE}_{0} = 0 + 0 + 1.5125$$

Energy at equilibrium position ($0.2\text{ m}$ above release point):

$$\text{Total}_{\text{eq}} = \frac{1}{2}mv^{2} + mg(0.2) + 0.1125$$

Conservation:

$$1.5125 = \frac{1}{2} \times 0.3 \times v^{2} + 0.3 \times 10 \times 0.2 + 0.1125$$

$$1.5125 = 0.15v^{2} + 0.6 + 0.1125$$

$$1.5125 = 0.15v^{2} + 0.7125$$

$$0.15v^{2} = 1.5125 - 0.7125 = 0.8$$

$$v^{2} = \frac{0.8}{0.15} = \frac{80}{15} = \frac{16}{3}$$

$$v = \sqrt{\frac{16}{3}} = \frac{4}{\sqrt{3}} = \frac{4\sqrt{3}}{3} \approx 2.31\text{ m s}^{-1} \quad \checkmark$$

> 💡 **Alternative insight:** The particle oscillates about the equilibrium position (simple harmonic motion for small displacements about equilibrium, though the full motion with EPE is not exactly SHM due to gravity). The energy method elegantly avoids needing to solve the equation of motion.

## Question 11 — Medium: Elastic String — Finding Natural Length and Modulus (Exam Style)

> A light elastic string obeys Hooke's law. When a mass of $1.5\text{ kg}$ hangs in equilibrium from the string, its length is $1.20\text{ m}$. When a mass of $3.0\text{ kg}$ hangs in equilibrium from the same string, its length is $1.50\text{ m}$.
>
> (a) Find the natural length $l$ and modulus $\lambda$ of the string.
>
> (b) Find the elastic potential energy stored in the string when the $3.0\text{ kg}$ mass hangs in equilibrium.
>
> Take $g = 10\text{ m s}^{-2}$.

**Solution (a):**

Let $l$ = natural length, $\lambda$ = modulus.

For $m_{1} = 1.5\text{ kg}$: $T_{1} = 1.5g = 15\text{ N}$, $L_{1} = 1.20\text{ m}$

$$T_{1} = \\frac{\\lambda(L_{1} - l)}{l}$$

$$15 = \\frac{\\lambda(1.20 - l)}{l} \\tag{1}$$

For $m_{2} = 3.0\text{ kg}$: $T_{2} = 3.0g = 30\text{ N}$, $L_{2} = 1.50\text{ m}$

$$T_{2} = \\frac{\\lambda(L_{2} - l)}{l}$$

$$30 = \\frac{\\lambda(1.50 - l)}{l} \\tag{2}$$

Divide (2) by (1):

$$\\frac{30}{15} = \\frac{1.50 - l}{1.20 - l}$$

$$2 = \\frac{1.50 - l}{1.20 - l}$$

$$2(1.20 - l) = 1.50 - l$$

$$2.40 - 2l = 1.50 - l$$

$$2.40 - 1.50 = 2l - l$$

$$l = 0.90\\text{ m} \\quad \\checkmark$$

Substitute into (1):

$$15 = \\frac{\\lambda(1.20 - 0.90)}{0.90}$$

$$15 = \\frac{\\lambda \\times 0.30}{0.90}$$

$$15 = \\frac{\\lambda}{3}$$

$$\\lambda = 45\\text{ N} \\quad \\checkmark$$

**Verification** with (2):

$$\\frac{45 \\times (1.50 - 0.90)}{0.90} = \\frac{45 \\times 0.60}{0.90} = \\frac{27}{0.90} = 30\\text{ N} = 3.0g \\quad \\checkmark$$

**Solution (b):**

When $m_{2} = 3.0\text{ kg}$ hangs in equilibrium:

$$x_{2} = L_{2} - l = 1.50 - 0.90 = 0.60\\text{ m}$$

$$E = \\frac{\\lambda x_{2}^{2}}{2l}$$

$$E = \\frac{45 \\times 0.60^{2}}{2 \\times 0.90}$$

$$E = \\frac{45 \\times 0.36}{1.80}$$

$$E = \\frac{16.2}{1.80}$$

$$E = 9.0\\text{ J} \\quad \\checkmark$$

> 💡 **Check via $E = \\frac{1}{2}Tx$:** $E = \\frac{1}{2} \\times 30 \\times 0.60 = 9.0\\text{ J}$ ✓.

---

## Question 12 — Hard: Combined Energy — Particle Projected Towards an Elastic String

> A light elastic string has natural length $1.0\text{ m}$ and modulus $50\text{ N}$. One end is fixed at point $O$ on a smooth horizontal table. A particle $P$ of mass $0.4\text{ kg}$ is placed $2.0\text{ m}$ from $O$ (beyond the natural length) with the string taut. $P$ is projected directly towards $O$ with speed $6.0\text{ m s}^{-1}$.
>
> (a) Find the speed of $P$ when it first reaches the point where the string becomes slack ($1.0\text{ m}$ from $O$).
>
> (b) Describe the motion of $P$ after the string becomes slack. How close does $P$ get to $O$?

**Solution (a):**

$$l = 1.0\\text{ m}, \\quad \\lambda = 50\\text{ N}, \\quad m = 0.4\\text{ kg}$$

Initial position: $L_{0} = 2.0\\text{ m}$

$$x_{0} = 2.0 - 1.0 = 1.0\\text{ m}$$

$$E_{0} = \\frac{\\lambda x_{0}^{2}}{2l}$$

$$E_{0} = \\frac{50 \\times 1.0^{2}}{2 \\times 1.0}$$

$$E_{0} = \\frac{50}{2}$$

$$E_{0} = 25\\text{ J}$$

Initial kinetic energy (projected towards $O$):

$$\\text{KE}_{0} = \\frac{1}{2}mv_{0}^{2}$$

$$\\text{KE}_{0} = \\frac{1}{2} \\times 0.4 \\times 6.0^{2}$$

$$\\text{KE}_{0} = 0.2 \\times 36$$

$$\\text{KE}_{0} = 7.2\\text{ J}$$

At the slack point ($1.0\text{ m}$ from $O$): $x = 0$, $E = 0$.

On a smooth horizontal table, GPE is constant and there is no friction. However, the elastic string **opposes** the motion towards $O$ (tension pulls $P$ back towards $O$, but as $P$ moves towards $O$ the string does **negative** work — wait, tension acts towards $O$, and displacement is towards $O$, so tension does **positive** work? Let us be careful.)

Actually the string pulls $P$ **towards** $O$ (tension direction is towards $O$), and $P$ moves towards $O$, so the elastic force assists the motion. But EPE **decreases** as $x$ decreases. Energy: $\text{KE} + \text{EPE} = \\text{constant}$ on the smooth table.

$$\text{KE}_{0} + E_{0} = \\text{KE}_{1} + E_{1}$$

$$7.2 + 25 = \\frac{1}{2} \\times 0.4 \\times v_{1}^{2} + 0$$

$$32.2 = 0.2v_{1}^{2}$$

$$v_{1}^{2} = \\frac{32.2}{0.2}$$

$$v_{1}^{2} = 161$$

$$v_{1} = \\sqrt{161} \\approx 12.7\\text{ m s}^{-1} \\quad \\checkmark$$

> 💡 **Intuition:** The particle **accelerates** towards $O$ because the tension assists the motion (pulling it in). Its speed at the slack point is **greater** than its projection speed — elastic energy has been converted to kinetic energy.

**Solution (b):**

After the string becomes slack ($L \\leq 1.0\text{ m}$ from $O$):

$$T = 0, \\quad E = 0$$

There are no horizontal forces on $P$ (smooth table, slack string):

$$F = 0 \\implies a = 0$$

So $P$ continues with **constant velocity**:

$$v = \\sqrt{161} \\approx 12.7\\text{ m s}^{-1} \\text{ directly towards } O$$

On a smooth table with no other obstacles, $P$ would pass through $O$ and continue beyond it. In practice:

- $P$ moves in a **straight line** at constant speed $v_{1}$ towards $O$.
- It will **pass through** (or over) the fixed point $O$ — the string, being slack, offers no resistance.
- If the string were reattached or could go taut again on the far side, further analysis would be needed. But for a string that simply goes slack, the particle continues indefinitely at $v = \\sqrt{161}\\text{ m s}^{-1}$.

If instead the particle were constrained (e.g. by a wall at $O$), it would collide with the wall at that speed.

> ⚠️ **Watch Out!** Some students think the speed **decreases** as the particle approaches $O$ (because "the string is pulling it back"). In fact, when moving **towards** the anchor point, the elastic force acts **in the direction of motion** (tension pulls towards $O$), so the particle **speeds up**. The string only decelerates a particle moving **away** from $O$. Get the sign right by checking: does EPE increase or decrease? Here $x$ decreases so EPE decreases → KE must increase.

---

---

# 18. Quick Reference Card

*Cut this out for last-minute revision.*

### Hooke's Law

$$T = \frac{\lambda x}{l} = kx \quad\text{where}\quad k = \frac{\lambda}{l},\quad x = L - l$$

### Key Definitions

| Quantity | Symbol | Units | Definition |
|----------|--------|-------|------------|
| Modulus of elasticity | $\lambda$ | N | Force to double the length (if Hooke's law held) |
| Natural length | $l$ | m | Unstretched length |
| Extension | $x$ | m | $L - l$ |
| Stiffness | $k$ | $\text{N m}^{-1}$ | $\lambda/l$ |

### Elastic Potential Energy

$$E = \frac{\lambda x^{2}}{2l} = \frac{1}{2}kx^{2} = \frac{1}{2}Tx$$

$$E = 0 \text{ when string is slack }(x \leq 0)$$

### String vs Spring

- **String:** $T = 0$ when $L \leq l$ (slack — no compression)
- **Spring:** $T = \frac{\lambda x}{l}$ even when $x < 0$ (thrust/compression)

### Vertical Equilibrium

$$mg = \frac{\lambda x}{l} \implies x_{\text{eq}} = \frac{mgl}{\lambda}$$

### Inclined Plane (angle $\alpha$)

$$mg\sin\alpha = \frac{\lambda x}{l} \quad\text{(smooth)}$$

### Conical Pendulum

$$T\cos\theta = mg, \quad T\sin\theta = mr\omega^{2}, \quad r = (l+x)\sin\theta, \quad T = \frac{\lambda x}{l}$$

### Conservation of Energy

$$\frac{1}{2}mv_{1}^{2} + mgh_{1} + \frac{\lambda x_{1}^{2}}{2l} = \frac{1}{2}mv_{2}^{2} + mgh_{2} + \frac{\lambda x_{2}^{2}}{2l}$$

### Two Strings Between Fixed Points ($d$ apart, particle at $y$ from $A$)

$$T_{1} = \frac{\lambda_{1}(y-l_{1})}{l_{1}}, \quad T_{2} = \frac{\lambda_{2}(d-y-l_{2})}{l_{2}}, \quad T_{1} = T_{2} \text{ at equilibrium (smooth)}$$

### Work Done by Elastic Force

$$W = \frac{\lambda x_{1}^{2}}{2l} - \frac{\lambda x_{2}^{2}}{2l}$$

### Deadly Sins

1. Using $L$ instead of $x = L - l$ in Hooke's law ❌
2. Plugging negative $x$ into Hooke's law for a string ❌
3. Forgetting $\frac{1}{2}$ in $E = \frac{\lambda x^{2}}{2l}$ ❌
4. Forgetting the free-fall distance $l$ when particle is dropped from $O$ ❌
5. Using $r = l\sin\theta$ instead of $r = (l+x)\sin\theta$ in conical pendulum ❌
6. Not checking that strings are taut ($x > 0$) ❌
7. Sign errors in GPE when using energy conservation ❌
8. Confusing $\lambda$ (N) with $k$ ($\text{N m}^{-1}$) ❌

---

> **Good luck! You've got this.** Every Cambridge Hooke's Law question follows one of the patterns in this guide — identify the situation (vertical, horizontal, inclined, conical, energy), write down the correct equation, and solve step-by-step. 🔗🚀

---
