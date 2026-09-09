# 💥 FURTHER MATHS MOMENTUM — ULTIMATE STUDY GUIDE

## Cambridge International AS & A Level Further Mathematics (9231) — Further Mechanics

> **The complete walkthrough:** Every technique explained step-by-step, with 30+ worked derivations and 11 fully solved examples in proper LaTeX. Covers conservation of momentum, Newton's experimental law, coefficient of restitution, direct and oblique impact of smooth spheres, impact with fixed surfaces, and loss of kinetic energy.

---

# 📋 Table of Contents

1. [Syllabus Requirements](#1-syllabus-requirements)
2. [Prerequisite Knowledge](#2-prerequisite-knowledge)
3. [Conservation of Linear Momentum](#3-conservation-of-linear-momentum)
4. [Newton's Experimental Law & Coefficient of Restitution](#4-newtons-experimental-law--coefficient-of-restitution)
5. [Direct Impact of Two Smooth Spheres](#5-direct-impact-of-two-smooth-spheres)
6. [Oblique Impact of Two Smooth Spheres](#6-oblique-impact-of-two-smooth-spheres)
7. [Direct Impact with a Fixed Surface](#7-direct-impact-with-a-fixed-surface)
8. [Oblique Impact with a Fixed Plane](#8-oblique-impact-with-a-fixed-plane)
9. [Loss of Kinetic Energy](#9-loss-of-kinetic-energy)
10. [Worked Examples](#10-worked-examples)
11. [Common Mistakes](#11-common-mistakes)
12. [Complete Formula Sheet](#12-complete-formula-sheet)
13. [Cambridge Exam Analysis](#13-cambridge-exam-analysis)
14. [Practice Questions & Full Solutions](#14-practice-questions--full-solutions)
15. [Quick Reference Card](#15-quick-reference-card)

---

# How To Use This Guide

Each section follows this structure:

1. **The Rule** — the formula you must know (in LaTeX, boxed)
2. **Step-by-Step Method** — a numbered algorithm you can follow
3. **Derivation / Explanation** — why the formula works
4. **Illustrative Mini-Example** — short application
5. **Watch Out!** — common pitfalls

Full worked examples (11) with Question/Solution format appear in Section 10, each with every algebra step on its own `$$` line.

---

# 1. Syllabus Requirements

## What Cambridge Expects for Momentum (Further Mechanics §3.6)

According to the CAIE 9231 syllabus for Further Mechanics, Section 3.6:

| Topic | What You Must Be Able To Do |
|-------|------------------------------|
| **Conservation of linear momentum** | Apply momentum conservation to collisions between particles/spheres |
| **Newton's experimental law (NEL)** | State and use $e = \frac{\text{speed of separation}}{\text{speed of approach}}$ |
| **Coefficient of restitution $e$** | Understand $0 \leq e \leq 1$, with $e=1$ perfectly elastic, $e=0$ perfectly inelastic |
| **Direct impact of two smooth spheres** | Solve for post-impact velocities using momentum + NEL together |
| **Oblique impact of two smooth spheres** | Resolve parallel and perpendicular to the line of centres; momentum conserved only along line of centres |
| **Direct impact with fixed surface** | Apply NEL with one particle's velocity zero before/after (wall is immovable) |
| **Oblique impact with fixed plane/surface** | Resolve parallel/perpendicular to the plane; component parallel to plane unchanged, NEL perpendicular to plane |
| **Loss of kinetic energy** | Calculate KE lost in an impact and determine conditions for KE conservation |

### 🟢 Cambridge Assessment Objectives

| AO | Weight | What It Means |
|----|--------|---------------|
| **AO1** | ~50% | Recall, select, and use mathematical facts, concepts, and techniques |
| **AO2** | ~50% | Construct rigorous arguments, solve problems, and interpret results |

> ⚠️ **Exam Tip:** Momentum questions in Further Mechanics are typically worth **8–14 marks** and appear as one of the three questions on the paper (often Q2 or Q3). Expect to solve simultaneous equations from momentum + NEL, handle vector components in oblique impacts, and compute energy loss. Vectors and trigonometry are essential.

---

# 2. Prerequisite Knowledge

## From AS & A Level Mathematics (Mechanics) and Pure Mathematics

### 2.1 Momentum and Impulse (AS Mechanics)

Linear momentum of a particle:

$$p = mv$$

where $m$ is mass and $v$ is velocity (vector). Units: $\text{kg m s}^{-1}$ or $\text{N s}$.

Impulse:

$$J = F \cdot \Delta t = \Delta p = mv - mu$$

Impulse equals change in momentum.

### 2.2 Newton's Laws

- **First Law:** A body remains at rest or in uniform motion unless acted upon by a resultant external force.
- **Second Law:** $F = ma = \frac{dp}{dt}$ (rate of change of momentum).
- **Third Law:** Every action has an equal and opposite reaction — crucial for understanding why total momentum is conserved when only internal impulsive forces act.

### 2.3 Conservation of Mechanical Energy

Kinetic energy:

$$KE = \frac{1}{2}mv^2$$

For elastic collisions, KE is conserved. For inelastic collisions, KE is not conserved (some is lost to heat, sound, deformation).

### 2.4 Vectors and Components

For a velocity vector $\mathbf{v}$ making angle $\theta$ with a chosen axis:

$$v_{\parallel} = v\cos\theta, \quad v_{\perp} = v\sin\theta$$

You must be fluent in resolving velocities parallel and perpendicular to the **line of centres** or to a **fixed plane**.

### 2.5 Smooth vs Rough Surfaces

- **Smooth** spheres/planes: no frictional impulse; no force component perpendicular to the line of centres / parallel to a smooth plane. Momentum of each particle perpendicular to the line of centres (or parallel to a smooth plane) is individually conserved.
- All spheres in 9231 are **smooth** unless stated otherwise.

---

# 3. Conservation of Linear Momentum

## 3.1 The Principle

> **📌 Key Point 3.1 — Conservation of Linear Momentum:**
> When no external impulsive forces act on a system, the total linear momentum of the system is conserved (remains constant) in any direction.
>
> $$m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2$$
>
> where $u_1, u_2$ are velocities before impact and $v_1, v_2$ are velocities after impact, all measured in the same direction along the line of motion.

**What this means:** During the brief instant of collision, the only forces acting are the equal and opposite impulsive forces between the two bodies (Newton's Third Law). These internal impulses cancel, so total momentum cannot change.

### When Does It Apply?

| Situation | Momentum Conserved? |
|-----------|---------------------|
| Two spheres collide in free space | ✅ Yes — total momentum conserved |
| Two spheres collide on a smooth horizontal table | ✅ Yes — horizontal momentum conserved (vertical forces balance) |
| Sphere hits a fixed wall | ❌ No — external impulse from the wall changes total momentum |
| Oblique impact of two spheres — along line of centres | ✅ Yes — along line of centres |
| Oblique impact of two spheres — perpendicular to line of centres | ❌ Not as a combined system — but each sphere's component perpendicular to line of centres is individually unchanged (smooth = no impulse in that direction) |

### Step-by-Step Method — Applying Conservation of Momentum

| Step | What To Do |
|------|------------|
| **1** | Choose a positive direction (e.g. left-to-right is positive) |
| **2** | Write momentum before: $m_1 u_1 + m_2 u_2$ (respect signs — velocities in opposite directions have opposite signs) |
| **3** | Write momentum after: $m_1 v_1 + m_2 v_2$ |
| **4** | Equate: $m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2$ |
| **5** | This is one equation — you need NEL for the second equation |

> **⚠️ Watch Out!** Sign convention is the #1 source of errors. If sphere $A$ moves right at $5\text{ m s}^{-1}$ and sphere $B$ moves left at $3\text{ m s}^{-1}$, then $u_A = +5$, $u_B = -3$ (or vice versa — just be consistent throughout).

> **🎯 What the examiner wants:** You to write the momentum equation explicitly with correct signs before substituting numbers. Even if arithmetic slips, you earn M1 for a correct signed equation. Always state your positive direction ("Take right as positive") — examiners reward clarity.

---

## 3.2 Vector Form

For oblique impacts, momentum is a vector. Conservation along the line of centres ($x$-direction):

$$m_A u_{Ax} + m_B u_{Bx} = m_A v_{Ax} + m_B v_{Bx}$$

Perpendicular to the line of centres ($y$-direction), for smooth spheres the impulse is zero in this direction, so each particle's momentum in this direction is individually conserved:

$$v_{Ay} = u_{Ay}, \quad v_{By} = u_{By}$$

> **📌 Key Point 3.2 — Smooth Spheres Perpendicular to Line of Centres:**
> For smooth spheres, the velocity component of each sphere perpendicular to the line of centres is unchanged by the impact.
>
> $$v_{A\perp} = u_{A\perp}, \quad v_{B\perp} = u_{B\perp}$$

---

### Mini-Example — Momentum Before NEL

> **Question:** Two particles of mass $3\text{ kg}$ and $5\text{ kg}$ move towards each other with speeds $4\text{ m s}^{-1}$ and $2\text{ m s}^{-1}$ respectively. Write the conservation of momentum equation.

**Solution:**

Take right as positive. $u_1 = +4$, $u_2 = -2$:

$$3(4) + 5(-2) = 3v_1 + 5v_2$$

$$12 - 10 = 3v_1 + 5v_2$$

$$2 = 3v_1 + 5v_2 \quad \checkmark$$

---

# 4. Newton's Experimental Law & Coefficient of Restitution

## 4.1 Newton's Experimental Law (NEL)

When two bodies collide, the ratio of their relative speed after impact to their relative speed before impact (measured along the line of centres) is constant for a given pair of materials. This constant is the **coefficient of restitution** $e$.

> **📌 Key Point 4.1 — Newton's Experimental Law:**
>
> $$e = \frac{\text{speed of separation along line of centres}}{\text{speed of approach along line of centres}}$$
>
> Equivalently, for two particles $A$ and $B$ moving along the same line (with positive direction from $A$ towards $B$):
>
> $$v_B - v_A = e(u_A - u_B)$$
>
> where $u_A, u_B$ are velocities before impact and $v_A, v_B$ are velocities after, measured in the same consistent direction.

**Understanding the formula:** The speed of approach is how fast the gap between the particles is closing before impact. The speed of separation is how fast the gap opens after impact. Their ratio $e$ measures the "bounciness."

### Line-of-Centres Diagram

```
Before impact:          After impact:

   A ----→  uA              A  → vA  or  A ← vA
         ←----  uB                   B  → vB
    ──────────               ──────────
   Speed of approach         Speed of separation
   = uA - uB  (if uA > 0,  = vB - vA   (if vB > vA)
     uB may be negative)
```

> **⚠️ Watch Out!** The formula $v_B - v_A = e(u_A - u_B)$ assumes both velocities are measured in the **same positive direction**. If you chose right as positive, then $u_A$ and $u_B$ must both use that convention. A common mistake is to use speeds (magnitudes) instead of signed velocities.

---

## 4.2 The Coefficient of Restitution $e$

> **📌 Key Point 4.2 — Range of $e$:**
>
> $$0 \leq e \leq 1$$

| Value of $e$ | Name | Physical Meaning |
|---------------|------|-----------------|
| $e = 1$ | **Perfectly elastic** | No KE lost; speed of separation = speed of approach. Relative velocity simply reverses. |
| $0 < e < 1$ | **Inelastic** | Some KE lost; separation speed is a fraction of approach speed. Most real collisions. |
| $e = 0$ | **Perfectly inelastic** | Maximum KE lost (consistent with momentum); particles coalesce / move together after impact. $v_A = v_B$. |

> **📌 Key Point 4.3 — Perfectly Elastic vs Perfectly Inelastic:**
>
> $$e = 1: \quad v_B - v_A = u_A - u_B \quad \text{(relative velocity reverses)}$$
>
> $$e = 0: \quad v_B - v_A = 0 \implies v_A = v_B \quad \text{(common velocity)}$$

**Note:** $e$ is a property of the **pair of materials** (and their surfaces), not of a single body. Two steel spheres have a different $e$ than a steel sphere and a wooden wall.

### How $e$ Relates to Energy

- When $e = 1$, kinetic energy is **conserved** in a direct impact between two particles.
- When $e < 1$, kinetic energy is **lost** — converted to heat, sound, and deformation.
- Energy loss increases as $e$ decreases.

---

## 4.3 Impact with a Fixed Surface

When a particle strikes a **fixed** (immovable) surface, the surface does not move. If $u$ is the component of approach velocity perpendicular to the surface and $v$ is the component of rebound velocity perpendicular to the surface:

> **📌 Key Point 4.4 — NEL for Fixed Surface:**
>
> $$v = eu \quad \text{(rebound speed perpendicular to surface = $e \times$ approach speed)}$$
>
> More precisely, if the surface is at rest: speed of separation $= v$, speed of approach $= u$, so $e = v/u$.

The component **parallel** to a smooth fixed plane is unchanged (no impulse parallel to a smooth plane).

---

### Mini-Example — Using NEL Directly

> **Question:** Two spheres $A$ (mass $2\text{ kg}$) and $B$ (mass $3\text{ kg}$) collide directly. Before impact $u_A = 5\text{ m s}^{-1}$, $u_B = -1\text{ m s}^{-1}$. The coefficient of restitution is $e = 0.6$. Write the NEL equation.

**Solution:**

$$v_B - v_A = e(u_A - u_B)$$

$$v_B - v_A = 0.6(5 - (-1))$$

$$v_B - v_A = 0.6 \times 6 = 3.6 \quad \checkmark$$

Combined with momentum $2(5) + 3(-1) = 2v_A + 3v_B$, i.e. $7 = 2v_A + 3v_B$, you can solve for $v_A$ and $v_B$.

---

# 5. Direct Impact of Two Smooth Spheres

## 5.1 What Is Direct Impact?

**Direct impact** (also called **direct collision**) occurs when the centres of the two spheres and their velocities all lie on the same straight line — the **line of centres**. At the instant of impact, the spheres touch at a single point and the line joining their centres is the line along which the impulsive force acts.

```
         Line of centres
    ─────────●──────────●─────────
            A           B
           →uA    ←uB    (approaching)
           →vA    →vB    (after - various possibilities)
```

For smooth spheres, the impulsive force is entirely along this line. No transverse impulse exists.

## 5.2 The Two Governing Equations

For a direct impact between spheres of mass $m_1$ and $m_2$:

> **📌 Key Point 5.1 — Direct Impact: Two Equations, Two Unknowns:**
>
> $$\text{(1) Conservation of momentum: } \quad m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2$$
>
> $$\text{(2) Newton's experimental law: } \quad v_2 - v_1 = e(u_1 - u_2)$$

Two equations in two unknowns ($v_1, v_2$) — always solvable.

### Step-by-Step Method — Direct Impact of Two Spheres

| Step | What To Do |
|------|------------|
| **1** | Draw a diagram: mark $u_1, u_2, v_1, v_2$ with a consistent positive direction |
| **2** | Write conservation of momentum along the line of centres |
| **3** | Write NEL: $v_2 - v_1 = e(u_1 - u_2)$ (check sign convention!) |
| **4** | Solve the two simultaneous equations for $v_1$ and $v_2$ |
| **5** | Check: if $e=0$, verify $v_1 = v_2$; if $e=1$, verify KE is conserved |

### 5.3 General Solution

Solving the system gives the well-known closed forms. For masses $m_A, m_B$:

$$v_A = \frac{m_A u_A + m_B u_B - m_B e(u_A - u_B)}{m_A + m_B}$$

$$v_B = \frac{m_A u_A + m_B u_B + m_A e(u_A - u_B)}{m_A + m_B}$$

> You do **not** need to memorise these — derive them from the two equations each time. Examiners award method marks for writing both equations clearly.

---

### Mini-Example — Direct Impact Velocities

> **Question:** Spheres $A$ (4 kg) and $B$ (6 kg) collide directly. $u_A = 3$, $u_B = -2$ (m s$^{-1}$, right positive), $e = 0.5$. Find $v_A$ and $v_B$.

**Solution:**

Momentum:

$$4(3) + 6(-2) = 4v_A + 6v_B$$

$$12 - 12 = 4v_A + 6v_B$$

$$0 = 4v_A + 6v_B \quad \text{...(i)}$$

NEL:

$$v_B - v_A = 0.5(3 - (-2))$$

$$v_B - v_A = 0.5 \times 5 = 2.5 \quad \text{...(ii)}$$

From (ii): $v_B = v_A + 2.5$. Substitute into (i):

$$0 = 4v_A + 6(v_A + 2.5)$$

$$0 = 10v_A + 15$$

$$v_A = -1.5\text{ m s}^{-1}, \quad v_B = 1.0\text{ m s}^{-1} \quad \checkmark$$

Interpretation: $A$ rebounds to the left, $B$ moves right.

> **⚠️ Watch Out — Direction After Impact!** After solving, check whether your velocities make physical sense. If a sphere was moving right before impact and you get a large negative (leftward) velocity after, that may be correct (rebound) — but if the approaching sphere passes through the other one, something is wrong with signs.

---

## 5.4 Special Cases

### Equal Masses, Perfectly Elastic ($m_1 = m_2$, $e = 1$)

Spheres **exchange** velocities:

$$v_1 = u_2, \quad v_2 = u_1$$

### One Sphere Initially at Rest

If $u_2 = 0$, then:

$$m_1 u_1 = m_1 v_1 + m_2 v_2, \quad v_2 - v_1 = eu_1$$

This is the most common exam scenario.

> **🎯 What the examiner wants:** Both the momentum equation and the NEL equation written separately before solving. Don't jump to the closed-form $v_A$, $v_B$ formulae — show simultaneous equations for full method marks. If $e=1$ check that KE is conserved; if $e=0$ check $v_A = v_B$.

---

# 6. Oblique Impact of Two Smooth Spheres

## 6.1 What Is Oblique Impact?

**Oblique impact** occurs when the velocities of the spheres are **not** along the line of centres at the instant of impact. Each sphere's velocity makes some angle with the line of centres.

```
                    y (perp to line of centres)
                    ↑
                    │
        B           │    ╱ vB'
         ●          │   ╱  (after)
        ╱│╲         │  ╱
       ╱ │ ╲        │ ╱ θB'
      ╱  │  ╲_______│╱___________→ x (line of centres)
     ╱   │   ╲      │╲
    ╱  θB│    ╲     │ ╲  vA' (after)
   →uB  │     ●    │  ╲╱
        │     A    │   ● A
        │   →uA    │
```

The key principle: resolve every velocity into components **parallel** ($x$) and **perpendicular** ($y$) to the **line of centres**.

## 6.2 The Three Governing Principles

> **📌 Key Point 6.1 — Oblique Impact of Two Smooth Spheres:**
>
> $$\text{(1) Momentum conserved along line of centres: } \quad m_A u_{Ax} + m_B u_{Bx} = m_A v_{Ax} + m_B v_{Bx}$$
>
> $$\text{(2) NEL along line of centres: } \quad v_{Bx} - v_{Ax} = e(u_{Ax} - u_{Bx})$$
>
> $$\text{(3) No impulse perpendicular to line of centres (smooth): } \quad v_{Ay} = u_{Ay}, \quad v_{By} = u_{By}$$

**Summary:** Along the line of centres, the impact behaves exactly like a direct impact. Perpendicular to the line of centres, nothing happens — each sphere keeps its transverse velocity component.

### Why No Transverse Impulse?

For **smooth** spheres, the contact force is entirely **normal** to the surfaces at the point of contact, i.e. along the line of centres. By definition, a smooth surface cannot exert a tangential (frictional) force. Therefore there is no impulse — and no momentum change — perpendicular to the line of centres.

### Step-by-Step Method — Oblique Impact of Two Spheres

| Step | What To Do |
|------|------------|
| **1** | Identify the line of centres at the instant of impact — this is your $x$-axis |
| **2** | Define $y$-axis perpendicular to the line of centres |
| **3** | Resolve every initial velocity into $x$ and $y$ components: $u_{Ax} = u_A\cos\theta_A$ etc. |
| **4** | Apply momentum conservation along $x$: $m_A u_{Ax} + m_B u_{Bx} = m_A v_{Ax} + m_B v_{Bx}$ |
| **5** | Apply NEL along $x$: $v_{Bx} - v_{Ax} = e(u_{Ax} - u_{Bx})$ |
| **6** | Apply no-impulse condition: $v_{Ay} = u_{Ay}$ and $v_{By} = u_{By}$ |
| **7** | Solve for $v_{Ax}, v_{Bx}$; combine with unchanged $y$-components to get final velocity vectors |
| **8** | If asked for speed/direction after: $\lvert\mathbf{v}\rvert = \sqrt{v_x^2 + v_y^2}$, $\tan\phi = v_y/v_x$ |

> **⚠️ Watch Out!** The line of centres is NOT necessarily the direction of motion of either sphere. It is the line joining the centres at the instant of impact. You must resolve velocities relative to this line, not relative to the incoming velocity direction.

> **🎯 What the examiner wants:** Explicit resolution: show $u_{Ax} = u_A\cos\theta_A$, $u_{Ay} = u_A\sin\theta_A$ etc. on separate lines. State "$v_{Ay}=u_{Ay}$, $v_{By}=u_{By}$ (smooth — no transverse impulse)" — this statement alone earns A1. Then solve momentum + NEL along $x$ only.

---

### Mini-Example — Oblique Impact Setup

> **Question:** Sphere $A$ (mass 2 kg) moves at $5\text{ m s}^{-1}$ at $30°$ to the line of centres. Sphere $B$ (mass 3 kg) is at rest. The line of centres is the $x$-axis. Find the $x$ and $y$ components of $u_A$ and $u_B$.

**Solution:**

$$u_{Ax} = 5\cos 30° = \frac{5\sqrt{3}}{2} \approx 4.33\text{ m s}^{-1}$$

$$u_{Ay} = 5\sin 30° = 2.5\text{ m s}^{-1}$$

$$u_{Bx} = 0, \quad u_{By} = 0$$

After impact: $v_{Ay} = 2.5$, $v_{By} = 0$, and $v_{Ax}, v_{Bx}$ found from momentum + NEL along $x$.

---

## 6.3 Finding the Direction After Impact

After solving, each sphere's velocity vector has magnitude and direction:

$$|\mathbf{v}_A| = \sqrt{v_{Ax}^2 + v_{Ay}^2}$$

$$\tan\phi_A = \frac{v_{Ay}}{v_{Ax}} \quad \text{(angle with line of centres)}$$

If $v_{Ax}$ turns out negative, the sphere rebounds — its $x$-component reverses direction.

---

# 7. Direct Impact with a Fixed Surface

## 7.1 The Model

A small smooth sphere strikes a **fixed** (immovable) smooth surface — e.g. a wall or barrier — directly, meaning its velocity is perpendicular (normal) to the surface.

```
    Wall (fixed, immovable)
    ┃
    ┃  ● → u  (approaching, perpendicular to wall)
    ┃  ● ← v  (rebounding)
    ┃
```

The wall has effectively infinite mass and does not move. Total momentum of the sphere + wall system is not useful (the wall is attached to the Earth). Instead, we apply only NEL.

> **📌 Key Point 7.1 — Direct Impact with Fixed Surface:**
> If a sphere approaches a fixed surface with speed $u$ normal to the surface and rebounds with speed $v$:
>
> $$v = eu$$
>
> The direction reverses; the speed is reduced by factor $e$.

If the sphere is moving directly towards the wall ($u > 0$ towards wall), after impact it moves away with speed $eu$.

### What About Momentum?

Momentum of the sphere alone is **not** conserved — the wall exerts an external impulse on the sphere:

$$J = m(v - (-u)) = m(v + u) = m(eu + u) = mu(1+e)$$

(taking away from wall as positive after impact).

This impulse is absorbed by the wall/Earth and is not needed in calculations unless the question asks for it.

---

### Mini-Example — Direct Impact with Wall

> **Question:** A sphere of mass 0.5 kg strikes a fixed smooth wall directly with speed $8\text{ m s}^{-1}$. It rebounds with speed $5\text{ m s}^{-1}$. Find $e$ and the impulse exerted by the wall.

**Solution:**

$$e = \frac{v}{u} = \frac{5}{8} = 0.625$$

Impulse on sphere (taking rebound direction as positive):

$$J = m(v - (-u)) = 0.5(5 + 8) = 6.5\text{ N s}$$

By Newton's Third Law, impulse on wall is $6.5\text{ N s}$ in the opposite direction. $\checkmark$

> **⚠️ Watch Out!** Impulse is $m(v - u)$ with **signed** velocities. If $u = +8$ towards wall and $v = -5$ away (same axis), then $J = m(-5 - 8) = -6.5m$ — the magnitude is $6.5m$. Be consistent with your sign convention.

> **🎯 What the examiner wants:** For wall impacts, the statement "$v = eu$" (or "$v_{\perp}=eu_{\perp}$" for oblique) plus the impulse calculation $J = m(v+u)$ with sign explanation. If asked for impulse magnitude, give the magnitude and state the direction ("away from wall" / "normal to wall").

---

## 7.2 Successive Bounces

If a sphere is dropped from height $h_0$ onto a fixed horizontal surface, it bounces repeatedly with coefficient $e$:

- Speed just before first impact: $u_0 = \sqrt{2gh_0}$ (from $v^2 = u^2 + 2as$)
- Speed just after first impact: $v_0 = eu_0$
- Maximum height after first bounce: $h_1 = \frac{v_0^2}{2g} = e^2 h_0$
- After $n$ bounces: $h_n = e^{2n}h_0$

> **📌 Key Point 7.2 — Successive Bounces:**
>
> $$h_n = e^{2n} h_0, \quad v_n = e^n v_0$$

The total distance travelled and total time can be summed as geometric series — a common exam extension.

**Total distance travelled** (dropped from $h_0$, bouncing until rest):

$$D = h_0 + 2h_1 + 2h_2 + \cdots = h_0 + 2h_0(e^2 + e^4 + \cdots)$$

$$D = h_0 + 2h_0\cdot\frac{e^2}{1-e^2} = h_0\cdot\frac{1+e^2}{1-e^2}$$

**Total time** (with $t_0 = \sqrt{2h_0/g}$ time to first impact):

$$T = t_0 + 2t_1 + 2t_2 + \cdots = t_0\left(1 + 2e + 2e^2 + \cdots\right) = t_0\cdot\frac{1+e}{1-e}$$

Note: $t_n = e^n t_0$ because $v_n = e^n v_0$ and time to rise and fall $= 2v_n/g$.

> **⚠️ Watch Out!** The first drop $h_0$ is counted once, but each bounce height $h_n$ ($n\geq1$) is counted twice (up and down). Forgetting the factor of 2 is a classic error.

> **🎯 What the examiner wants:** Recognition that $h_n = e^{2n}h_0$ comes from $v_n^2 = 2gh_n$ and $v_n = e^n v_0$. Show the geometric series sum explicitly — don't just quote the $D$ formula.

---

# 8. Oblique Impact with a Fixed Plane

## 8.1 The Model

A smooth sphere strikes a **fixed smooth plane** (e.g. a wall, barrier, or horizontal surface) at an angle. The velocity has components both **perpendicular** (normal) and **parallel** to the plane.

```
         Fixed smooth plane (e.g. vertical wall)
         ┃  ╱ v' (after - angle β to plane)
         ┃ ╱
         ┃╱ β
         ┃●  ← sphere at impact
         ┃╲ α
         ┃ ╲
         ┃  ╲ u (before - angle α to plane)
         ┃
    ─────┨
    normal to plane →    parallel to plane ↑
```

**Key:** For a smooth plane, there is no frictional impulse parallel to the plane. The only impulse is **normal** (perpendicular) to the plane.

## 8.2 The Two Governing Principles

> **📌 Key Point 8.1 — Oblique Impact with Fixed Smooth Plane:**
>
> $$\text{(1) Component parallel to plane unchanged: } \quad v_{\parallel} = u_{\parallel}$$
>
> $$\text{(2) NEL perpendicular to plane: } \quad v_{\perp} = e \cdot u_{\perp}$$
>
> where $u_{\perp}, v_{\perp}$ are the speeds perpendicular to the plane (magnitudes, before and after), and $u_{\parallel}, v_{\parallel}$ are the components parallel to the plane.

**In vector terms** (with $x$ normal to plane, $y$ parallel to plane):

$$v_y = u_y, \quad v_x = e \cdot u_x \text{ (with direction reversed)}$$

### Angle Relationships

If the sphere approaches at angle $\alpha$ to the plane (or equivalently $90° - \alpha$ to the normal):

$$u_{\perp} = u\sin\alpha, \quad u_{\parallel} = u\cos\alpha$$

After impact:

$$v_{\perp} = e \cdot u\sin\alpha, \quad v_{\parallel} = u\cos\alpha$$

The rebound angle $\beta$ (with the plane) satisfies:

$$\tan\beta = \frac{v_{\perp}}{v_{\parallel}} = \frac{e \cdot u\sin\alpha}{u\cos\alpha} = e\tan\alpha$$

> **📌 Key Point 8.2 — Angle Change on Oblique Impact with Fixed Plane:**
>
> $$\tan\beta = e\tan\alpha$$
>
> where $\alpha$ is the angle between the incoming velocity and the plane, and $\beta$ is the angle between the outgoing velocity and the plane. (If angles are measured from the **normal**, then $\tan\beta = \frac{1}{e}\tan\alpha$ — always clarify which angle you mean!)

Similarly, if angles are measured from the **normal** ($\theta$ to normal before, $\phi$ to normal after):

$$\tan\phi = \frac{1}{e}\tan\theta$$

> **⚠️ Watch Out — Which Angle?** Cambridge may measure angles from the **plane** or from the **normal**. These give different formulae! Always draw a diagram and resolve explicitly rather than blindly applying $\tan\beta = e\tan\alpha$. The safest method is to resolve into normal/parallel components and apply the two principles separately.

> **🎯 What the examiner wants:** A resolved diagram with $u_{\perp}$ and $u_{\parallel}$ labelled, the two statements "$v_{\parallel}=u_{\parallel}$" and "$v_{\perp}=eu_{\perp}$" on separate lines, and the rebound angle specified as "to the wall/plane" or "to the normal". Never just quote $\tan\beta=e\tan\alpha$ without derivation.

### Step-by-Step Method — Oblique Impact with Fixed Plane

| Step | What To Do |
|------|------------|
| **1** | Draw the plane and mark the normal direction |
| **2** | Resolve the incoming velocity $\mathbf{u}$ into $u_{\perp}$ (normal) and $u_{\parallel}$ (parallel) |
| **3** | Apply: $v_{\parallel} = u_{\parallel}$ (parallel unchanged) |
| **4** | Apply: $v_{\perp} = e \cdot u_{\perp}$ (normal: NEL, direction reverses) |
| **5** | Recombine: $|\mathbf{v}| = \sqrt{v_{\perp}^2 + v_{\parallel}^2}$, $\tan(\text{angle}) = v_{\perp}/v_{\parallel}$ |
| **6** | If asked for direction, state angle clearly — specify "to the plane" or "to the normal" |

---

### Mini-Example — Oblique Impact with Wall

> **Question:** A sphere strikes a fixed smooth vertical wall with velocity $10\text{ m s}^{-1}$ at $60°$ to the wall. The coefficient of restitution is $e = 0.7$. Find the speed and direction after impact.

**Solution:**

$$u_{\parallel} = 10\cos 60° = 5\text{ m s}^{-1}$$

$$u_{\perp} = 10\sin 60° = 5\sqrt{3} \approx 8.66\text{ m s}^{-1}$$

After impact:

$$v_{\parallel} = u_{\parallel} = 5\text{ m s}^{-1}$$

$$v_{\perp} = e \cdot u_{\perp} = 0.7 \times 5\sqrt{3} = 3.5\sqrt{3} \approx 6.06\text{ m s}^{-1}$$

$$|\mathbf{v}| = \sqrt{5^2 + (3.5\sqrt{3})^2} = \sqrt{25 + 36.75} = \sqrt{61.75} \approx 7.86\text{ m s}^{-1}$$

$$\tan\beta = \frac{v_{\perp}}{v_{\parallel}} = \frac{3.5\sqrt{3}}{5} = 0.7\tan 60°$$

$$\beta = \tan^{-1}(1.212) \approx 50.5° \text{ to the wall} \quad \checkmark$$

---

# 9. Loss of Kinetic Energy

## 9.1 Calculating Energy Loss

Kinetic energy is **only** conserved when $e = 1$ (perfectly elastic direct impact). In all other cases, some KE is lost.

> **📌 Key Point 9.1 — Loss of Kinetic Energy:**
>
> $$\Delta KE = KE_{\text{before}} - KE_{\text{after}} = \frac{1}{2}m_1 u_1^2 + \frac{1}{2}m_2 u_2^2 - \frac{1}{2}m_1 v_1^2 - \frac{1}{2}m_2 v_2^2$$

For oblique impacts, use the **speeds** (magnitudes of velocity vectors):

$$KE = \frac{1}{2}m|\mathbf{v}|^2 = \frac{1}{2}m(v_x^2 + v_y^2)$$

## 9.2 General Formula for Direct Impact

For a direct impact between masses $m_1, m_2$ with coefficient $e$:

> **📌 Key Point 9.2 — KE Loss in Direct Impact:**
>
> $$\Delta KE = \frac{1}{2} \cdot \frac{m_1 m_2}{m_1 + m_2} \cdot (1 - e^2)(u_1 - u_2)^2$$

**Derivation sketch:** Substitute the general solutions for $v_1, v_2$ into the KE expression and simplify. The factor $(1-e^2)$ shows explicitly that no energy is lost when $e=1$, and maximum energy is lost when $e=0$.

This can also be written as:

$$\Delta KE = \frac{1}{2}(1 - e^2) \cdot \frac{m_1 m_2}{m_1 + m_2}(u_1 - u_2)^2$$

> You do **not** need to memorise this formula — compute $v_1, v_2$ first, then calculate KE before and after directly. But it is useful for quickly checking your answer and for understanding the dependence on $e$.

### When Is KE Conserved?

| Condition | KE Conserved? |
|-----------|---------------|
| $e = 1$ (direct impact, two particles) | ✅ Yes — perfectly elastic |
| $e < 1$ (any impact) | ❌ No — energy lost |
| Oblique impact, even with $e = 1$ | ❌ Not necessarily — KE along line of centres is conserved only if $e=1$, but total KE: if $e=1$ and both particles are involved, total KE is conserved. For impact with a fixed wall even with $e=1$, KE of the sphere alone is conserved only in the normal direction; parallel KE is always conserved (smooth). |
| Impact with fixed wall, $e = 1$ | ✅ KE of sphere conserved (speed unchanged, only normal component reverses) |

> **⚠️ Watch Out!** For oblique impacts with $e=1$, the **total** KE of the two-sphere system is conserved (because the $y$-components are unchanged and the $x$-components behave like a perfectly elastic direct impact). Don't confuse this with only the line-of-centres KE being conserved.

> **🎯 What the examiner wants:** KE calculated as $\frac12 m|\mathbf v|^2 = \frac12 m(v_x^2+v_y^2)$ — show the speed squared includes both components. Display $KE_{\text{before}}$ and $KE_{\text{after}}$ on separate lines before subtracting. Fractional loss $= \Delta KE / KE_{\text{before}}$ should be shown if asked for percentage.

---

### Mini-Example — Energy Loss

> **Question:** Two spheres of mass $2\text{ kg}$ and $4\text{ kg}$ collide directly. $u_1 = 6\text{ m s}^{-1}$, $u_2 = -2\text{ m s}^{-1}$, $e = 0.5$. Find the loss of KE.

**Solution:**

First find $v_1, v_2$:

$$2(6) + 4(-2) = 2v_1 + 4v_2 \implies 4 = 2v_1 + 4v_2 \quad \text{...(i)}$$

$$v_2 - v_1 = 0.5(6-(-2)) = 4 \quad \text{...(ii)}$$

From (ii): $v_2 = v_1 + 4$. Into (i):

$$4 = 2v_1 + 4(v_1+4) = 6v_1 + 16$$

$$v_1 = -2\text{ m s}^{-1}, \quad v_2 = 2\text{ m s}^{-1}$$

$$KE_{\text{before}} = \tfrac{1}{2}(2)(36) + \tfrac{1}{2}(4)(4) = 36 + 8 = 44\text{ J}$$

$$KE_{\text{after}} = \tfrac{1}{2}(2)(4) + \tfrac{1}{2}(4)(4) = 4 + 8 = 12\text{ J}$$

$$\Delta KE = 44 - 12 = 32\text{ J} \quad \checkmark$$

Check with formula: $\Delta KE = \frac{1}{2}\cdot\frac{8}{6}\cdot(1-0.25)\cdot 64 = \frac{4}{6}\cdot 0.75 \cdot 64 = 32\text{ J}$ ✅

---

# 10. Worked Examples

## Example 1 — Direct Impact: Finding $e$ and Velocities (Easy)

> **Question:** Two smooth spheres $A$ and $B$ of masses $3\text{ kg}$ and $5\text{ kg}$ respectively are moving directly towards each other on a smooth horizontal table. Sphere $A$ has speed $4\text{ m s}^{-1}$ and sphere $B$ has speed $2\text{ m s}^{-1}$. After the collision, sphere $A$ rebounds with speed $1\text{ m s}^{-1}$. Find (a) the speed of $B$ after the collision, (b) the coefficient of restitution $e$, and (c) the loss of kinetic energy.

**Solution:**

Take the initial direction of $A$ as positive. Then:

$$u_A = 4, \quad u_B = -2$$

After impact, $A$ rebounds so $v_A = -1$. Let $v_B$ be the velocity of $B$ after.

**(a) Speed of $B$ after:**

Conservation of momentum:

$$m_A u_A + m_B u_B = m_A v_A + m_B v_B$$

$$3(4) + 5(-2) = 3(-1) + 5v_B$$

$$12 - 10 = -3 + 5v_B$$

$$2 = -3 + 5v_B$$

$$5v_B = 5$$

$$v_B = 1\text{ m s}^{-1} \quad \checkmark$$

So $B$ moves in the original direction of $A$ with speed $1\text{ m s}^{-1}$.

**(b) Coefficient of restitution:**

$$e = \frac{v_B - v_A}{u_A - u_B}$$

$$e = \frac{1 - (-1)}{4 - (-2)}$$

$$e = \frac{2}{6}$$

$$e = \frac{1}{3} \quad \checkmark$$

**(c) Loss of kinetic energy:**

$$KE_{\text{before}} = \frac{1}{2}(3)(4^2) + \frac{1}{2}(5)(2^2)$$

$$KE_{\text{before}} = \frac{1}{2}(3)(16) + \frac{1}{2}(5)(4)$$

$$KE_{\text{before}} = 24 + 10 = 34\text{ J}$$

$$KE_{\text{after}} = \frac{1}{2}(3)(1^2) + \frac{1}{2}(5)(1^2)$$

$$KE_{\text{after}} = \frac{3}{2} + \frac{5}{2} = 4\text{ J}$$

$$\Delta KE = 34 - 4 = 30\text{ J} \quad \checkmark$$

---

## Example 2 — Direct Impact: Both Velocities Unknown (Medium)

> **Question:** Two smooth spheres $A$ and $B$ of masses $2\text{ kg}$ and $4\text{ kg}$ lie at rest on a smooth horizontal table with $A$ to the left of $B$. Sphere $A$ is projected towards $B$ with speed $9\text{ m s}^{-1}$. The coefficient of restitution between the spheres is $e = \frac{2}{3}$. Find (a) the velocities of $A$ and $B$ after the impact, (b) the magnitude of the impulse exerted by $A$ on $B$, and (c) the loss of KE.

**Solution:**

$$u_A = 9, \quad u_B = 0, \quad m_A = 2, \quad m_B = 4, \quad e = \frac{2}{3}$$

**(a) Velocities after:**

Momentum:

$$m_A u_A + m_B u_B = m_A v_A + m_B v_B$$

$$2(9) + 4(0) = 2v_A + 4v_B$$

$$18 = 2v_A + 4v_B$$

$$9 = v_A + 2v_B \quad \text{...(i)}$$

NEL:

$$v_B - v_A = e(u_A - u_B)$$

$$v_B - v_A = \frac{2}{3}(9 - 0)$$

$$v_B - v_A = 6 \quad \text{...(ii)}$$

From (ii):

$$v_B = v_A + 6$$

Substitute into (i):

$$9 = v_A + 2(v_A + 6)$$

$$9 = 3v_A + 12$$

$$3v_A = -3$$

$$v_A = -1\text{ m s}^{-1}$$

$$v_B = -1 + 6 = 5\text{ m s}^{-1} \quad \checkmark$$

So $A$ rebounds with $1\text{ m s}^{-1}$ and $B$ moves forward with $5\text{ m s}^{-1}$.

**(b) Impulse on $B$:**

$$J_B = m_B(v_B - u_B)$$

$$J_B = 4(5 - 0)$$

$$J_B = 20\text{ N s} \quad \checkmark$$

(Impulse on $A$: $J_A = 2(-1 - 9) = -20\text{ N s}$, equal and opposite — check ✅)

**(c) Loss of KE:**

$$KE_{\text{before}} = \frac{1}{2}(2)(81) + 0 = 81\text{ J}$$

$$KE_{\text{after}} = \frac{1}{2}(2)(1) + \frac{1}{2}(4)(25)$$

$$KE_{\text{after}} = 1 + 50 = 51\text{ J}$$

$$\Delta KE = 81 - 51 = 30\text{ J} \quad \checkmark$$

---

## Example 3 — Direct Impact: Finding $e$ from Given After-Velocities (Medium)

> **Question:** Two smooth spheres $A$ and $B$ of masses $5\text{ kg}$ and $3\text{ kg}$ are moving in the same direction on a smooth horizontal table. $A$ is behind $B$ with $u_A = 8\text{ m s}^{-1}$ and $u_B = 2\text{ m s}^{-1}$. After the direct impact, $A$ continues in the same direction with speed $3\text{ m s}^{-1}$. Find (a) the velocity of $B$ after impact, (b) $e$, and (c) determine whether $B$ will subsequently catch $A$ if both continue without further collisions.

**Solution:**

$$u_A = 8, \quad u_B = 2, \quad m_A = 5, \quad m_B = 3, \quad v_A = 3$$

**(a) Velocity of $B$ after:**

$$m_A u_A + m_B u_B = m_A v_A + m_B v_B$$

$$5(8) + 3(2) = 5(3) + 3v_B$$

$$40 + 6 = 15 + 3v_B$$

$$46 = 15 + 3v_B$$

$$3v_B = 31$$

$$v_B = \frac{31}{3} \approx 10.33\text{ m s}^{-1} \quad \checkmark$$

**(b) Coefficient of restitution:**

$$e = \frac{v_B - v_A}{u_A - u_B}$$

$$e = \frac{\frac{31}{3} - 3}{8 - 2}$$

$$e = \frac{\frac{31-9}{3}}{6}$$

$$e = \frac{\frac{22}{3}}{6}$$

$$e = \frac{22}{18} = \frac{11}{9}$$

But $e > 1$ is impossible!

Let us re-examine. Wait — we must check data consistency. If $v_A = 3$ and momentum gives $v_B = 31/3$, then $e = 11/9 > 1$ violates physics. This would mean the question has inconsistent data, OR $A$ must actually rebound.

> **⚠️ Watch Out!** If you calculate $e > 1$ or $e < 0$, the given data is physically impossible — or you have a sign error. In exams, this is sometimes used as a check: "Show that $e \leq 1$" or the data will always give $0 \leq e \leq 1$.

**Revised scenario (physically valid):** Suppose instead $v_A = 4\text{ m s}^{-1}$:

$$5(8) + 3(2) = 5(4) + 3v_B$$

$$46 = 20 + 3v_B$$

$$v_B = \frac{26}{3}\text{ m s}^{-1}$$

$$e = \frac{\frac{26}{3} - 4}{6} = \frac{\frac{14}{3}}{6} = \frac{7}{9} \quad \checkmark$$

**(c) Will $B$ catch $A$?** With $v_B > v_A$ ($26/3 > 4$), $B$ is ahead and moving faster, so $B$ pulls away — no further collision. If $v_A > v_B$, $A$ would catch $B$.

---

## Example 4 — Oblique Impact of Two Smooth Spheres (Hard)

> **Question:** Two smooth spheres $A$ and $B$ have masses $3\text{ kg}$ and $2\text{ kg}$ respectively. Sphere $A$ is moving with velocity $6\text{ m s}^{-1}$ at an angle of $30°$ to the line of centres at the instant of impact. Sphere $B$ is moving with velocity $4\text{ m s}^{-1}$ directly along the line of centres towards $A$. The coefficient of restitution between the spheres is $e = 0.6$. Find the velocity of each sphere after the impact (magnitude and direction).

**Solution:**

Set up coordinates: $x$ along line of centres (positive from $A$ towards $B$), $y$ perpendicular to line of centres.

**Resolve initial velocities:**

For $A$ ($6\text{ m s}^{-1}$ at $30°$ to line of centres):

$$u_{Ax} = 6\cos 30° = 6 \cdot \frac{\sqrt{3}}{2} = 3\sqrt{3}\text{ m s}^{-1}$$

$$u_{Ay} = 6\sin 30° = 3\text{ m s}^{-1}$$

For $B$ (directly along line of centres towards $A$, so negative $x$-direction):

$$u_{Bx} = -4\text{ m s}^{-1}$$

$$u_{By} = 0$$

**Perpendicular components (unchanged — smooth):**

$$v_{Ay} = u_{Ay} = 3\text{ m s}^{-1}$$

$$v_{By} = u_{By} = 0$$

**Along line of centres — momentum:**

$$m_A u_{Ax} + m_B u_{Bx} = m_A v_{Ax} + m_B v_{Bx}$$

$$3(3\sqrt{3}) + 2(-4) = 3v_{Ax} + 2v_{Bx}$$

$$9\sqrt{3} - 8 = 3v_{Ax} + 2v_{Bx} \quad \text{...(i)}$$

**Along line of centres — NEL:**

$$v_{Bx} - v_{Ax} = e(u_{Ax} - u_{Bx})$$

$$v_{Bx} - v_{Ax} = 0.6(3\sqrt{3} - (-4))$$

$$v_{Bx} - v_{Ax} = 0.6(3\sqrt{3} + 4) \quad \text{...(ii)}$$

Compute numerically: $3\sqrt{3} \approx 5.196$, so $3\sqrt{3} + 4 \approx 9.196$:

$$v_{Bx} - v_{Ax} = 0.6 \times 9.196 = 5.5176 \quad \text{...(ii)}$$

From (ii):

$$v_{Bx} = v_{Ax} + 5.5176$$

Substitute into (i):

$$9\sqrt{3} - 8 = 3v_{Ax} + 2(v_{Ax} + 5.5176)$$

$$9\sqrt{3} - 8 = 5v_{Ax} + 11.0352$$

$$5v_{Ax} = 9\sqrt{3} - 8 - 11.0352$$

$$5v_{Ax} = 15.588 - 19.0352 = -3.4472$$

$$v_{Ax} = -0.689\text{ m s}^{-1}$$

$$v_{Bx} = -0.689 + 5.5176 = 4.828\text{ m s}^{-1}$$

**Recombine for $A$:**

$$|\mathbf{v}_A| = \sqrt{v_{Ax}^2 + v_{Ay}^2} = \sqrt{(-0.689)^2 + 3^2}$$

$$|\mathbf{v}_A| = \sqrt{0.475 + 9} = \sqrt{9.475} \approx 3.08\text{ m s}^{-1}$$

$$\tan\phi_A = \frac{v_{Ay}}{|v_{Ax}|} = \frac{3}{0.689}$$

But since $v_{Ax}$ is negative, $A$ now moves at angle to the **opposite** side. More precisely:

$$\phi_A = \tan^{-1}\left(\frac{3}{-0.689}\right) \approx 102.9° \text{ from positive } x\text{-axis}$$

Or equivalently $77.1°$ to the (negative) line of centres, on the same side as before in $y$.

$$|\mathbf{v}_B| = |v_{Bx}| = 4.83\text{ m s}^{-1} \text{ along the line of centres (positive }x\text{)} \quad \checkmark$$

Sphere $B$ moves directly along the line of centres; sphere $A$ rebounds with a significant transverse component.

> **⚠️ Watch Out!** When $v_{Ax}$ comes out negative, it means sphere $A$'s $x$-component has reversed — it bounces back. Don't forget to account for this sign when computing the angle. The angle with the line of centres uses $|\tan\phi| = |v_y / v_x|$.

---

## Example 5 — Oblique Impact with Fixed Wall (Medium-Hard)

> **Question:** A smooth sphere of mass $0.4\text{ kg}$ strikes a fixed smooth vertical wall with velocity $12\text{ m s}^{-1}$ at an angle of $40°$ to the wall. The coefficient of restitution between the sphere and the wall is $e = 0.75$. Find (a) the velocity of the sphere after impact (magnitude and direction), (b) the impulse exerted by the wall on the sphere, and (c) the loss of kinetic energy.

**Solution:**

Resolve relative to the wall. Let $x$ be normal (perpendicular) to the wall, $y$ parallel to the wall.

$$u_{\perp} = 12\sin 40° \quad \text{(component towards wall, normal)}$$

$$u_{\parallel} = 12\cos 40° \quad \text{(component parallel to wall)}$$

Compute:

$$u_{\perp} = 12\sin 40° = 12 \times 0.6428 = 7.713\text{ m s}^{-1}$$

$$u_{\parallel} = 12\cos 40° = 12 \times 0.7660 = 9.193\text{ m s}^{-1}$$

**(a) Velocity after:**

Parallel unchanged:

$$v_{\parallel} = u_{\parallel} = 9.193\text{ m s}^{-1}$$

Perpendicular (NEL, direction reverses):

$$v_{\perp} = e \cdot u_{\perp} = 0.75 \times 7.713 = 5.785\text{ m s}^{-1} \quad \text{(away from wall)}$$

Magnitude:

$$|\mathbf{v}| = \sqrt{v_{\perp}^2 + v_{\parallel}^2} = \sqrt{(5.785)^2 + (9.193)^2}$$

$$|\mathbf{v}| = \sqrt{33.47 + 84.51} = \sqrt{117.98} \approx 10.86\text{ m s}^{-1}$$

Direction ($\beta$ = angle to wall after):

$$\tan\beta = \frac{v_{\perp}}{v_{\parallel}} = \frac{5.785}{9.193} = 0.6293$$

$$\beta = \tan^{-1}(0.6293) \approx 32.2° \text{ to the wall} \quad \checkmark$$

(Before: $40°$ to wall; after: $32.2°$ to wall — the angle decreases because the normal component is reduced.)

**(b) Impulse by wall on sphere:**

Only the normal component changes. Taking away from wall as positive for $v_{\perp}$:

$$J = m(v_{\perp} - (-u_{\perp})) = m(v_{\perp} + u_{\perp})$$

$$J = 0.4(5.785 + 7.713) = 0.4 \times 13.498 = 5.40\text{ N s}$$

$$J = 5.40\text{ N s normal to the wall} \quad \checkmark$$

(Equivalently: change in momentum in normal direction = $0.4(5.785 - (-7.713)) = 5.40\text{ N s}$.)

**(c) Loss of KE:**

$$KE_{\text{before}} = \frac{1}{2}(0.4)(12^2) = 0.2 \times 144 = 28.8\text{ J}$$

$$KE_{\text{after}} = \frac{1}{2}(0.4)(10.86^2) = 0.2 \times 117.98 = 23.60\text{ J}$$

$$\Delta KE = 28.8 - 23.60 = 5.20\text{ J} \quad \checkmark$$

Alternatively, only normal KE is affected:

$$\Delta KE = \tfrac{1}{2}m(u_{\perp}^2 - v_{\perp}^2) = \tfrac{1}{2}(0.4)(7.713^2 - 5.785^2) = 0.2(59.49 - 33.47) = 5.20\text{ J} \quad \checkmark$$

---

## Example 6 — Oblique Impact Between Two Spheres with General Directions (Hard)

> **Question:** Two identical smooth spheres $P$ and $Q$, each of mass $m$, are moving on a smooth horizontal table. At the instant of impact, the line of centres is along the $x$-axis. Before impact: $P$ has velocity $(4\mathbf{i} + 3\mathbf{j})\text{ m s}^{-1}$ and $Q$ has velocity $(-2\mathbf{i} + 1\mathbf{j})\text{ m s}^{-1}$. The coefficient of restitution is $e = 0.8$. Find the velocities of $P$ and $Q$ after the impact.

**Solution:**

$$m_P = m_Q = m, \quad \mathbf{u}_P = 4\mathbf{i} + 3\mathbf{j}, \quad \mathbf{u}_Q = -2\mathbf{i} + 1\mathbf{j}$$

Line of centres is along $\mathbf{i}$ ($x$-axis), so:

$$u_{Px} = 4, \quad u_{Py} = 3, \quad u_{Qx} = -2, \quad u_{Qy} = 1$$

**Transverse components unchanged:**

$$v_{Py} = u_{Py} = 3$$

$$v_{Qy} = u_{Qy} = 1$$

**Along line of centres ($x$):**

Momentum ($m_P = m_Q = m$, so $m$ cancels):

$$m(4) + m(-2) = mv_{Px} + mv_{Qx}$$

$$4 - 2 = v_{Px} + v_{Qx}$$

$$v_{Px} + v_{Qx} = 2 \quad \text{...(i)}$$

NEL:

$$v_{Qx} - v_{Px} = e(u_{Px} - u_{Qx})$$

$$v_{Qx} - v_{Px} = 0.8(4 - (-2))$$

$$v_{Qx} - v_{Px} = 0.8 \times 6 = 4.8 \quad \text{...(ii)}$$

Solve (i) and (ii):

Adding (i) and (ii):

$$2v_{Qx} = 6.8$$

$$v_{Qx} = 3.4\text{ m s}^{-1}$$

$$v_{Px} = 2 - 3.4 = -1.4\text{ m s}^{-1}$$

**Final velocities:**

$$\mathbf{v}_P = -1.4\mathbf{i} + 3\mathbf{j}\text{ m s}^{-1}$$

$$\mathbf{v}_Q = 3.4\mathbf{i} + 1\mathbf{j}\text{ m s}^{-1} \quad \checkmark$$

**Magnitudes and directions (if asked):**

$$|\mathbf{v}_P| = \sqrt{1.96 + 9} = \sqrt{10.96} \approx 3.31\text{ m s}^{-1}$$

$$\text{Direction of }P: \tan\phi_P = \frac{3}{1.4} \implies \phi_P \approx 65.0° \text{ above negative }x\text{-axis}$$

$$|\mathbf{v}_Q| = \sqrt{11.56 + 1} = \sqrt{12.56} \approx 3.54\text{ m s}^{-1}$$

$$\text{Direction of }Q: \tan\phi_Q = \frac{1}{3.4} \implies \phi_Q \approx 16.4° \text{ above }x\text{-axis} \quad \checkmark$$

> **⚠️ Watch Out!** For identical masses with $e=1$, the $x$-components would simply swap: $v_{Px} = u_{Qx} = -2$, $v_{Qx} = u_{Px} = 4$. With $e < 1$, the exchange is incomplete — $P$ still rebounds but less dramatically. This is a useful sanity check.

---

## Example 7 — Sphere Striking a Fixed Horizontal Plane at an Angle (Medium)

> **Question:** A small smooth sphere is projected with velocity $15\text{ m s}^{-1}$ at an angle of $50°$ above the horizontal towards a fixed smooth horizontal plane (the ground). The sphere strikes the plane and rebounds. The coefficient of restitution between the sphere and the plane is $e = 0.6$. Find (a) the speed and direction of the sphere immediately after impact, (b) the loss of kinetic energy due to the impact, and (c) the maximum height reached after the bounce (take $g = 10\text{ m s}^{-2}$).

**Solution:**

At impact, the velocity has horizontal and vertical components. For a horizontal plane:
- Normal = vertical, Parallel = horizontal.

$$u_{\text{horizontal}} = 15\cos 50° = 15 \times 0.6428 = 9.642\text{ m s}^{-1}$$

$$u_{\text{vertical}} = 15\sin 50° = 15 \times 0.7660 = 11.491\text{ m s}^{-1} \quad \text{(downwards towards plane)}$$

**(a) After impact:**

Horizontal unchanged:

$$v_{\text{horizontal}} = 9.642\text{ m s}^{-1}$$

Vertical (NEL, reverses direction — now upwards):

$$v_{\text{vertical}} = e \cdot u_{\text{vertical}} = 0.6 \times 11.491 = 6.894\text{ m s}^{-1} \text{ (upwards)}$$

Speed:

$$|\mathbf{v}| = \sqrt{9.642^2 + 6.894^2} = \sqrt{92.97 + 47.53} = \sqrt{140.50} \approx 11.85\text{ m s}^{-1}$$

Direction above horizontal:

$$\tan\beta = \frac{6.894}{9.642} = 0.7150$$

$$\beta = \tan^{-1}(0.7150) \approx 35.6° \text{ above the horizontal} \quad \checkmark$$

**(b) Loss of KE (mass $m$):**

$$KE_{\text{before}} = \frac{1}{2}m(15^2) = \frac{225m}{2}$$

$$KE_{\text{after}} = \frac{1}{2}m(11.85^2) = \frac{1}{2}m(140.50) = 70.25m$$

$$\Delta KE = \frac{1}{2}m(225 - 140.50) = 42.25m\text{ J}$$

As a fraction:

$$\frac{\Delta KE}{KE_{\text{before}}} = \frac{42.25}{112.5} = 0.376 = 37.6\% \quad \checkmark$$

Equivalently, only vertical KE is lost:

$$\Delta KE = \tfrac{1}{2}m(1-e^2)u_{\text{vertical}}^2 = \tfrac{1}{2}m(0.64)(11.491^2) = \tfrac{1}{2}m(84.51) = 42.25m\text{ J} \quad \checkmark$$

**(c) Maximum height after bounce:**

Vertical motion after: $v_y = 6.894$ upwards, $a = -g = -10$:

$$v^2 = u^2 - 2gh \implies 0 = 6.894^2 - 20h$$

$$h = \frac{6.894^2}{20} = \frac{47.53}{20} = 2.38\text{ m} \quad \checkmark$$

---

## Example 8 — Direct Impact Followed by Impact with Wall (Hard / Multi-Stage)

> **Question:** Three smooth spheres $A$, $B$, $C$ of masses $2\text{ kg}$, $3\text{ kg}$, $5\text{ kg}$ lie in a straight line on a smooth horizontal table, with $B$ between $A$ and $C$. Sphere $A$ is projected towards $B$ with speed $10\text{ m s}^{-1}$; $B$ and $C$ are initially at rest. The coefficient of restitution between $A$ and $B$ is $e_1 = 0.5$, and between $B$ and $C$ is $e_2 = 0.8$. After $A$ strikes $B$, $B$ goes on to strike $C$. Find (a) the velocities of $A$ and $B$ immediately after the first impact, (b) the velocities of $B$ and $C$ after the second impact, and (c) whether $A$ and $B$ will collide a second time.

**Solution:**

**(a) First impact: $A$ strikes $B$:**

$$u_A = 10, \quad u_B = 0, \quad m_A = 2, \quad m_B = 3, \quad e_1 = 0.5$$

Momentum:

$$2(10) + 3(0) = 2v_A + 3v_B$$

$$20 = 2v_A + 3v_B \quad \text{...(i)}$$

NEL:

$$v_B - v_A = 0.5(10 - 0) = 5 \quad \text{...(ii)}$$

From (ii): $v_B = v_A + 5$. Into (i):

$$20 = 2v_A + 3(v_A + 5) = 5v_A + 15$$

$$5v_A = 5$$

$$v_A = 1\text{ m s}^{-1}, \quad v_B = 6\text{ m s}^{-1} \quad \checkmark$$

**(b) Second impact: $B$ strikes $C$:**

Now $u_B = 6$, $u_C = 0$, $m_B = 3$, $m_C = 5$, $e_2 = 0.8$. Let $v_B'$ and $v_C'$ be velocities after second impact.

Momentum:

$$3(6) + 5(0) = 3v_B' + 5v_C'$$

$$18 = 3v_B' + 5v_C' \quad \text{...(iii)}$$

NEL:

$$v_C' - v_B' = 0.8(6 - 0) = 4.8 \quad \text{...(iv)}$$

From (iv): $v_C' = v_B' + 4.8$. Into (iii):

$$18 = 3v_B' + 5(v_B' + 4.8) = 8v_B' + 24$$

$$8v_B' = -6$$

$$v_B' = -0.75\text{ m s}^{-1}, \quad v_C' = 4.05\text{ m s}^{-1} \quad \checkmark$$

So $B$ rebounds backwards at $0.75\text{ m s}^{-1}$ after hitting $C$.

**(c) Will $A$ and $B$ collide again?**

After all impacts: $v_A = 1\text{ m s}^{-1}$ (still moving right), $v_B' = -0.75\text{ m s}^{-1}$ (moving left).

$A$ is to the left of $B$. $A$ moves right at $1\text{ m s}^{-1}$, $B$ moves left at $0.75\text{ m s}^{-1}$ — they approach each other!

Approach speed $= 1 + 0.75 = 1.75\text{ m s}^{-1} > 0$, so **yes**, $A$ and $B$ will collide a second time. $\checkmark$

> **⚠️ Watch Out!** Multi-stage problems require careful bookkeeping. After each impact, update the velocities before analysing the next. Always check whether subsequent collisions occur — if a trailing sphere is still faster than the one ahead, another impact is inevitable.

---


## Example 9 — Direct Impact: Finding $e$ from Impulse Data (Medium)

> **Question:** Two smooth spheres $A$ and $B$ of masses $1.5\text{ kg}$ and $2.5\text{ kg}$ respectively are moving on a smooth horizontal table directly towards each other. Before impact, $A$ has speed $5\text{ m s}^{-1}$ and $B$ has speed $3\text{ m s}^{-1}$. The impulse exerted by $B$ on $A$ during the collision is $9\text{ N s}$. Find (a) the velocities of $A$ and $B$ after the impact, (b) the coefficient of restitution $e$, and (c) the loss of kinetic energy.

**Solution:**

Take the initial direction of $A$ as positive. Then:

$$u_A = 5$$

$$u_B = -3$$

$$m_A = 1.5$$

$$m_B = 2.5$$

Let $v_A$ and $v_B$ be the signed velocities after impact (positive = original direction of $A$).

Impulse on $A$ is the change in momentum of $A$:

$$J_A = m_A(v_A - u_A)$$

$$9 = 1.5(v_A - 5) \quad \text{(but careful with sign: $A$ is slowed/reversed, so impulse is opposite to motion)}$$

Actually $B$ exerts an impulse on $A$ directed away from $B$, i.e. in the negative $x$-direction. Taking magnitudes: the impulse magnitude on $A$ is $9\text{ N s}$ opposing $A$'s motion. Using signed impulse $J_A = -9$ (negative because it opposes positive $A$ direction):

$$J_A = m_A(v_A - u_A) = -9$$

$$1.5(v_A - 5) = -9$$

$$v_A - 5 = -6$$

$$v_A = -1\text{ m s}^{-1} \quad \checkmark$$

So $A$ rebounds with speed $1\text{ m s}^{-1}$ in the opposite direction.

**(a) Velocity of $B$ after — use conservation of momentum:**

$$m_A u_A + m_B u_B = m_A v_A + m_B v_B$$

$$1.5(5) + 2.5(-3) = 1.5(-1) + 2.5v_B$$

$$7.5 - 7.5 = -1.5 + 2.5v_B$$

$$0 = -1.5 + 2.5v_B$$

$$2.5v_B = 1.5$$

$$v_B = 0.6\text{ m s}^{-1} \quad \checkmark$$

So $B$ moves in $A$'s original direction with speed $0.6\text{ m s}^{-1}$.

**(b) Coefficient of restitution:**

$$e = \frac{v_B - v_A}{u_A - u_B}$$

$$e = \frac{0.6 - (-1)}{5 - (-3)}$$

$$e = \frac{1.6}{8}$$

$$e = 0.2 \quad \checkmark$$

**(c) Loss of kinetic energy:**

$$KE_{\text{before}} = \frac{1}{2}m_A u_A^2 + \frac{1}{2}m_B u_B^2$$

$$KE_{\text{before}} = \frac{1}{2}(1.5)(25) + \frac{1}{2}(2.5)(9)$$

$$KE_{\text{before}} = 18.75 + 11.25$$

$$KE_{\text{before}} = 30\text{ J}$$

$$KE_{\text{after}} = \frac{1}{2}(1.5)(1) + \frac{1}{2}(2.5)(0.36)$$

$$KE_{\text{after}} = 0.75 + 0.45$$

$$KE_{\text{after}} = 1.2\text{ J}$$

$$\Delta KE = 30 - 1.2 = 28.8\text{ J} \quad \checkmark$$

Check with direct formula:

$$\Delta KE = \frac{1}{2}\cdot\frac{1.5 \times 2.5}{4.0}\cdot(1-0.04)\cdot 64$$

$$\Delta KE = \frac{1}{2}\cdot 0.9375 \cdot 0.96 \cdot 64$$

$$\Delta KE = 28.8\text{ J} \quad \checkmark$$

> **⚠️ Watch Out!** Impulse sign: $J = m(v-u)$ is signed. If $A$ moves right and the impulse from $B$ acts left, $J_A$ is negative in the $A$-positive coordinate. Getting the sign of $J$ wrong flips $v_A$ — always draw the impulse direction on your diagram.
---

## Example 10 — Complex Multi-Stage Oblique Impact: Two Spheres Then Wall Rebound (Hard)

> **Question:** Two smooth spheres $P$ and $Q$ of masses $2\text{ kg}$ and $3\text{ kg}$ lie on a smooth horizontal table. A fixed smooth vertical wall is parallel to the $y$-axis. At the instant of impact between $P$ and $Q$, the line of centres is along the $x$-axis (which is normal to the wall). Before the $P$–$Q$ impact:
> - $P$ has velocity $(6\mathbf{i} + 4\mathbf{j})\text{ m s}^{-1}$
> - $Q$ has velocity $(-2\mathbf{i} - \mathbf{j})\text{ m s}^{-1}$
> The coefficient of restitution between $P$ and $Q$ is $e_{PQ} = 0.6$. Immediately after this impact, sphere $Q$ moves towards the fixed wall and strikes it obliquely. The coefficient of restitution between $Q$ and the wall is $e_{W} = 0.7$. Find (a) the velocities of $P$ and $Q$ immediately after the $P$–$Q$ impact, (b) the velocity of $Q$ after it rebounds from the wall (magnitude and direction), and (c) the total loss of kinetic energy in both impacts combined.

**Solution:**

**(a) $P$–$Q$ oblique impact — line of centres along $x$:**

Resolve:

$$u_{Px} = 6$$

$$u_{Py} = 4$$

$$u_{Qx} = -2$$

$$u_{Qy} = -1$$

**Transverse components unchanged (smooth spheres):**

$$v_{Py} = u_{Py} = 4$$

$$v_{Qy} = u_{Qy} = -1$$

**Along line of centres ($x$) — momentum:**

$$m_P u_{Px} + m_Q u_{Qx} = m_P v_{Px} + m_Q v_{Qx}$$

$$2(6) + 3(-2) = 2v_{Px} + 3v_{Qx}$$

$$12 - 6 = 2v_{Px} + 3v_{Qx}$$

$$6 = 2v_{Px} + 3v_{Qx} \quad \text{...(i)}$$

**Along line of centres — NEL:**

$$v_{Qx} - v_{Px} = e_{PQ}(u_{Px} - u_{Qx})$$

$$v_{Qx} - v_{Px} = 0.6(6 - (-2))$$

$$v_{Qx} - v_{Px} = 0.6 \times 8$$

$$v_{Qx} - v_{Px} = 4.8 \quad \text{...(ii)}$$

From (ii):

$$v_{Qx} = v_{Px} + 4.8$$

Substitute into (i):

$$6 = 2v_{Px} + 3(v_{Px} + 4.8)$$

$$6 = 5v_{Px} + 14.4$$

$$5v_{Px} = -8.4$$

$$v_{Px} = -1.68\text{ m s}^{-1}$$

$$v_{Qx} = -1.68 + 4.8 = 3.12\text{ m s}^{-1}$$

Therefore:

$$\mathbf{v}_P = -1.68\mathbf{i} + 4\mathbf{j}\text{ m s}^{-1} \quad \checkmark$$

$$\mathbf{v}_Q = 3.12\mathbf{i} - 1\mathbf{j}\text{ m s}^{-1} \quad \checkmark$$

Check: $|\mathbf{v}_P| = \sqrt{1.68^2 + 16} = \sqrt{2.8224+16} = \sqrt{18.8224} \approx 4.34\text{ m s}^{-1}$.

Check: $|\mathbf{v}_Q| = \sqrt{9.7344+1} = \sqrt{10.7344} \approx 3.28\text{ m s}^{-1}$.

$Q$ now moves towards the wall (positive $x$ is towards the wall since wall normal is along $x$). $|\mathbf{v}_Q|$ before wall impact is $3.28\text{ m s}^{-1}$ at angle:

$$\tan\alpha_Q = \frac{|v_{Qy}|}{|v_{Qx}|} = \frac{1}{3.12} = 0.3205$$

$$\alpha_Q = \tan^{-1}(0.3205) \approx 17.8° \text{ to the normal (}x\text{-axis)} \quad \text{(or }72.2° \text{ to the wall)}$$

**(b) $Q$ strikes the wall — oblique impact with fixed smooth plane:**

Wall is parallel to $y$-axis. Normal = $x$-direction, parallel = $y$-direction.

Decompose $\mathbf{v}_Q$ relative to wall:

$$v_{Q\perp}^{\text{(before wall)}} = 3.12\text{ m s}^{-1} \quad \text{(normal, towards wall)}$$

$$v_{Q\parallel}^{\text{(before wall)}} = -1\text{ m s}^{-1} \quad \text{(parallel to wall)}$$

After wall impact — parallel unchanged (smooth wall):

$$v'_{Q\parallel} = -1\text{ m s}^{-1}$$

After wall impact — normal NEL (reverses direction):

$$v'_{Q\perp} = e_W \cdot v_{Q\perp}^{\text{(before wall)}}$$

$$v'_{Q\perp} = 0.7 \times 3.12$$

$$v'_{Q\perp} = 2.184\text{ m s}^{-1} \quad \text{(away from wall, so negative }x\text{ if towards was positive)}$$

Taking away from wall as the new positive for clarity, or keeping coordinates: if $\mathbf{i}$ points towards wall, then after rebound the $x$-component is negative:

$$\mathbf{v}'_Q = -2.184\mathbf{i} - 1\mathbf{j}\text{ m s}^{-1} \quad \checkmark$$

Magnitude:

$$|\mathbf{v}'_Q| = \sqrt{2.184^2 + (-1)^2}$$

$$|\mathbf{v}'_Q| = \sqrt{4.7699 + 1}$$

$$|\mathbf{v}'_Q| = \sqrt{5.7699} \approx 2.40\text{ m s}^{-1}$$

Direction after wall:

$$\tan\beta = \frac{|v'_{Q\parallel}|}{|v'_{Q\perp}|} = \frac{1}{2.184} = 0.4579 \text{ (to normal)}$$

$$\beta = \tan^{-1}(0.4579) \approx 24.6° \text{ to the normal}$$

$$\text{Equivalently } 65.4° \text{ to the wall} \quad \checkmark$$

Note: angle to normal increases (from $17.8°$ to $24.6°$) because $v_{\perp}$ shrinks while $v_{\parallel}$ is unchanged — the trajectory becomes more grazing.

**(c) Total loss of KE:**

Initial KE:

$$KE_{\text{initial}} = \frac{1}{2}(2)(36+16) + \frac{1}{2}(3)(4+1)$$

$$KE_{\text{initial}} = 1 \times 52 + 1.5 \times 5$$

$$KE_{\text{initial}} = 52 + 7.5 = 59.5\text{ J}$$

After $P$–$Q$ impact:

$$KE_{\text{after }PQ} = \frac{1}{2}(2)(1.68^2 + 16) + \frac{1}{2}(3)(3.12^2 + 1)$$

$$KE_{\text{after }PQ} = 1 \times (2.8224 + 16) + 1.5 \times (9.7344 + 1)$$

$$KE_{\text{after }PQ} = 18.8224 + 16.1016$$

$$KE_{\text{after }PQ} = 34.924\text{ J}$$

$$\Delta KE_{PQ} = 59.5 - 34.924 = 24.576\text{ J}$$

Check with oblique loss formula (only $x$-components contribute):

$$\Delta KE_{PQ} = \frac{1}{2}\cdot\frac{2\times3}{5}\cdot(1-0.36)\cdot(8)^2$$

$$\Delta KE_{PQ} = 0.6 \times 0.64 \times 64$$

$$\Delta KE_{PQ} = 24.576\text{ J} \quad \checkmark$$

After wall impact (only $Q$ affected, only its normal KE changes):

$$KE_{\text{final}} = \frac{1}{2}(2)|\mathbf{v}_P|^2 + \frac{1}{2}(3)|\mathbf{v}'_Q|^2$$

$$KE_{\text{final}} = 18.8224 + 1.5 \times 5.7699$$

$$KE_{\text{final}} = 18.8224 + 8.6549$$

$$KE_{\text{final}} = 27.477\text{ J}$$

$$\Delta KE_{\text{wall}} = 34.924 - 27.477 = 7.447\text{ J}$$

Also:

$$\Delta KE_{\text{wall}} = \frac{1}{2}(3)(1 - 0.49)(3.12^2)$$

$$\Delta KE_{\text{wall}} = 1.5 \times 0.51 \times 9.7344$$

$$\Delta KE_{\text{wall}} = 7.447\text{ J} \quad \checkmark$$

Total loss:

$$\Delta KE_{\text{total}} = 24.576 + 7.447 = 32.023\text{ J} \quad \checkmark$$

Fraction lost:

$$\frac{\Delta KE_{\text{total}}}{KE_{\text{initial}}} = \frac{32.023}{59.5} \approx 53.8\% \quad \checkmark$$

> **⚠️ Watch Out!** Multi-stage oblique problems chain $x$–$y$ bookkeeping across impacts. After the first impact, re-identify normal/parallel for the next surface — it may be a different axis. Also, KE loss in oblique impacts comes only from the normal/line-of-centres direction; transverse KE is untouched. Compute KE via $|\mathbf v|^2 = v_x^2 + v_y^2$ each time, never just $v_x^2$.

> **🎯 What the examiner wants:** For the 10–14 mark hard question, they expect a clear $x$/$y$ table before and after each impact, bothimpacts solved sequentially with updated velocities, and a final KE comparison. Show the check $\Delta KE_{PQ} = \frac12\frac{m_1m_2}{m_1+m_2}(1-e^2)(u_{1x}-u_{2x})^2$ as verification.
---

## Example 11 — Oblique Two-Sphere Impact: Finding $e$ and Deflection from Given After-Velocities (Hard)

> **Question:** Two smooth spheres $A$ and $B$ of masses $4\text{ kg}$ and $2\text{ kg}$ collide obliquely on a smooth horizontal table. The line of centres at impact is along the $x$-axis. Before impact:
> $$ \mathbf{u}_A = (5\mathbf{i} + 3\mathbf{j})\text{ m s}^{-1}, \quad \mathbf{u}_B = (-3\mathbf{i} + \mathbf{j})\text{ m s}^{-1} $$
> After impact, sphere $A$ has velocity $\mathbf{v}_A = (1.5\mathbf{i} + 3\mathbf{j})\text{ m s}^{-1}$. Find (a) the velocity of $B$ after the impact, (b) the coefficient of restitution $e$, (c) the magnitude and direction of $\mathbf{v}_B$, and (d) the loss of kinetic energy.

**Solution:**

$$u_{Ax} = 5, \quad u_{Ay} = 3$$

$$u_{Bx} = -3, \quad u_{By} = 1$$

$$v_{Ax} = 1.5, \quad v_{Ay} = 3$$

Check transverse — smooth, so $v_{Ay}$ should equal $u_{Ay}$:

$$v_{Ay} = 3 = u_{Ay} \quad \checkmark \text{ (consistent, smooth)}$$

So $v_{By} = u_{By} = 1$ for smooth — we will verify via momentum.

**(a) Velocity of $B$ — momentum along line of centres ($x$):**

$$m_A u_{Ax} + m_B u_{Bx} = m_A v_{Ax} + m_B v_{Bx}$$

$$4(5) + 2(-3) = 4(1.5) + 2v_{Bx}$$

$$20 - 6 = 6 + 2v_{Bx}$$

$$14 = 6 + 2v_{Bx}$$

$$2v_{Bx} = 8$$

$$v_{Bx} = 4\text{ m s}^{-1}$$

Transverse ($y$) — individually conserved (smooth):

$$v_{By} = u_{By} = 1\text{ m s}^{-1}$$

Therefore:

$$\mathbf{v}_B = 4\mathbf{i} + 1\mathbf{j}\text{ m s}^{-1} \quad \checkmark$$

**(b) Coefficient of restitution (along $x$):**

$$e = \frac{v_{Bx} - v_{Ax}}{u_{Ax} - u_{Bx}}$$

$$e = \frac{4 - 1.5}{5 - (-3)}$$

$$e = \frac{2.5}{8}$$

$$e = 0.3125 = \frac{5}{16} \quad \checkmark$$

**(c) Magnitude and direction of $\mathbf{v}_B$:**

$$|\mathbf{v}_B| = \sqrt{v_{Bx}^2 + v_{By}^2}$$

$$|\mathbf{v}_B| = \sqrt{16 + 1}$$

$$|\mathbf{v}_B| = \sqrt{17} \approx 4.12\text{ m s}^{-1}$$

$$\tan\phi_B = \frac{v_{By}}{v_{Bx}} = \frac{1}{4}$$

$$\phi_B = \tan^{-1}(0.25) \approx 14.0° \text{ above the line of centres (}x\text{-axis)} \quad \checkmark$$

For $A$:

$$|\mathbf{v}_A| = \sqrt{1.5^2 + 9} = \sqrt{2.25+9} = \sqrt{11.25} \approx 3.35\text{ m s}^{-1}$$

$$\tan\phi_A = \frac{3}{1.5} = 2$$

$$\phi_A = \tan^{-1}(2) \approx 63.4° \text{ above line of centres} \quad \checkmark$$

**(d) Loss of kinetic energy:**

$$KE_{\text{before}} = \frac{1}{2}(4)(25+9) + \frac{1}{2}(2)(9+1)$$

$$KE_{\text{before}} = 2 \times 34 + 1 \times 10$$

$$KE_{\text{before}} = 68 + 10 = 78\text{ J}$$

$$KE_{\text{after}} = \frac{1}{2}(4)(2.25+9) + \frac{1}{2}(2)(16+1)$$

$$KE_{\text{after}} = 2 \times 11.25 + 1 \times 17$$

$$KE_{\text{after}} = 22.5 + 17 = 39.5\text{ J}$$

$$\Delta KE = 78 - 39.5 = 38.5\text{ J} \quad \checkmark$$

Check with formula (only $x$-direction contributes to loss):

$$\Delta KE = \frac{1}{2}\cdot\frac{4\times2}{6}\cdot(1 - 0.09766)\cdot 64$$

$$\Delta KE = \frac{2}{3}\cdot 0.90234 \cdot 64$$

$$\Delta KE = 38.5\text{ J} \quad \checkmark$$

> **⚠️ Watch Out!** When given $\mathbf{v}_A$ after and asked to find $\mathbf{v}_B$, use momentum — not NEL — to find $v_{Bx}$. Then use the result to find $e$. Students often try to use NEL first, but $e$ is unknown, so momentum is the only equation that gives $v_{Bx}$ directly.

> **🎯 What the examiner wants:** Recognition that $v_{Ay}=u_{Ay}$ is a consistency check (if it fails, the data is non-smooth or erroneous). Then momentum along $x$ for $v_{Bx}$, NEL for $e$, and KE via $|\mathbf v|^2 = v_x^2+v_y^2$ — three distinct method marks in one question.
---

# 11. Common Mistakes

## ❌ Mistake 1 — Sign Errors in Momentum and NEL

**Wrong:** Using speeds (magnitudes) instead of signed velocities.

**Example error:** $m_1(4) + m_2(2) = m_1 v_1 + m_2 v_2$ when the spheres approach each other (one velocity should be negative).

**Correct:** Choose a positive direction and stick to it. If $A$ moves right ($u_A = +4$) and $B$ moves left ($u_B = -2$):

$$m_A(4) + m_B(-2) = m_A v_A + m_B v_B$$

Similarly for NEL: $v_B - v_A = e(u_A - u_B)$ uses **signed** velocities in a consistent direction.

---

## ❌ Mistake 2 — Applying NEL Perpendicular to Line of Centres

**Wrong:** Writing $v_{By} - v_{Ay} = e(u_{Ay} - u_{By})$ for the transverse direction.

**Correct:** NEL applies **only** along the line of centres (or normal to a fixed plane). Perpendicular to the line of centres:

$$v_{Ay} = u_{Ay}, \quad v_{By} = u_{By}$$

No $e$ appears in the transverse direction.

---

## ❌ Mistake 3 — Momentum "Conservation" Perpendicular to Line of Centres

**Wrong:** Writing $m_A u_{Ay} + m_B u_{By} = m_A v_{Ay} + m_B v_{By}$ and treating it as a useful equation.

**Correct:** Each component is individually conserved ($v_{Ay} = u_{Ay}$, $v_{By} = u_{By}$), so the combined equation is trivially satisfied but gives no new information. The useful momentum equation is only along the line of centres.

---

## ❌ Mistake 4 — Confusing Angle with Plane vs Angle with Normal

**Wrong:** Using $\tan\beta = e\tan\alpha$ when $\alpha$ was measured from the normal.

**Correct:** Be explicit:
- If $\alpha$ = angle to the **plane**: $\tan\beta = e\tan\alpha$ (angle decreases after bounce)
- If $\alpha$ = angle to the **normal**: $\tan\beta = \frac{1}{e}\tan\alpha$ (angle increases after bounce — measured from normal, the rebound is further from the normal)

**Safest approach:** Always resolve into normal and parallel components explicitly; never rely on memorised angle formulae alone.

---

## ❌ Mistake 5 — Forgetting That $0 \leq e \leq 1$

**Wrong:** Accepting $e = 1.3$ as a valid answer without comment.

**Correct:** If you calculate $e > 1$, either the data is inconsistent or you have a sign error. Energy cannot be created in a collision (for passive spheres). Always check that $0 \leq e \leq 1$ and flag impossible results.

---

## ❌ Mistake 6 — Using Conservation of Energy Instead of Momentum + NEL

**Wrong:** Writing $\frac{1}{2}m_1 u_1^2 + \frac{1}{2}m_2 u_2^2 = \frac{1}{2}m_1 v_1^2 + \frac{1}{2}m_2 v_2^2$ for a general collision.

**Correct:** Energy is **not** conserved unless $e = 1$. The two correct equations for direct impact are momentum conservation and NEL. Never assume KE conservation — calculate it and check.

---

## ❌ Mistake 7 — Impulse Sign and Direction

**Wrong:** $J = m(v + u)$ without considering which direction is positive.

**Correct:** Impulse on a particle is $J = m(v - u)$ with **signed** velocities. If $u = +5$ (towards wall) and $v = -3$ (away, same axis), then $J = m(-3 - 5) = -8m$. The magnitude is $8m$ and the direction is away from the wall. State direction explicitly.

---

## ❌ Mistake 8 — Not Recombining Components After Oblique Impact

**Wrong:** Giving only $v_x$ and $v_y$ without finding the resultant speed and direction when the question asks for "the velocity."

**Correct:** If asked for velocity (vector), give both magnitude and direction:

$$|\mathbf{v}| = \sqrt{v_x^2 + v_y^2}, \quad \tan\theta = \frac{v_y}{v_x}$$

Specify what the angle is measured from.

---

# 12. Complete Formula Sheet

## Conservation of Linear Momentum

$$m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2 \quad \text{(direct impact, same line)}$$

$$m_A u_{Ax} + m_B u_{Bx} = m_A v_{Ax} + m_B v_{Bx} \quad \text{(oblique: along line of centres)}$$

## Newton's Experimental Law (NEL)

$$e = \frac{\text{speed of separation}}{\text{speed of approach}} = \frac{v_B - v_A}{u_A - u_B} \quad \text{(signed, same positive direction)}$$

$$v_B - v_A = e(u_A - u_B)$$

## Coefficient of Restitution

$$0 \leq e \leq 1$$

$$e = 1: \text{ perfectly elastic}, \quad e = 0: \text{ perfectly inelastic } (v_A = v_B)$$

## Fixed Surface — Direct Impact

$$v = eu \quad \text{(rebound speed = $e \times$ approach speed, direction reverses)}$$

## Fixed Smooth Plane — Oblique Impact

$$v_{\parallel} = u_{\parallel} \quad \text{(parallel to plane unchanged)}$$

$$v_{\perp} = e \cdot u_{\perp} \quad \text{(perpendicular: NEL, direction reverses)}$$

$$\tan\beta = e\tan\alpha \quad \text{($\alpha$, $\beta$ = angles to plane, before and after)}$$

$$\tan\phi = \frac{1}{e}\tan\theta \quad \text{($\theta$, $\phi$ = angles to normal, before and after)}$$

## Oblique Impact — Two Smooth Spheres

$$v_{Ay} = u_{Ay}, \quad v_{By} = u_{By} \quad \text{(perpendicular to line of centres, each unchanged)}$$

## General Solution — Direct Impact

$$v_A = \frac{m_A u_A + m_B u_B - m_B e(u_A - u_B)}{m_A + m_B}$$

$$v_B = \frac{m_A u_A + m_B u_B + m_A e(u_A - u_B)}{m_A + m_B}$$

## Impulse

$$J = m(v - u) \quad \text{(signed velocities)}$$

$$|J| = m(1+e)|u_{\text{approach}}| \quad \text{(sphere striking fixed wall directly)}$$

For oblique wall impact (normal direction only):

$$J = m(v_{\perp} + u_{\perp}) = m(1+e)u_{\perp}$$

## Kinetic Energy and Loss

$$KE = \frac{1}{2}mv^2 = \frac{1}{2}m(v_x^2 + v_y^2) \quad \text{(oblique: use speed squared)}$$

$$\Delta KE = KE_{\text{before}} - KE_{\text{after}}$$

$$\Delta KE = \frac{1}{2}\cdot\frac{m_1 m_2}{m_1 + m_2}(1 - e^2)(u_1 - u_2)^2 \quad \text{(direct impact)}$$

$$\Delta KE = \frac{1}{2}m(1 - e^2)u_{\perp}^2 \quad \text{(oblique impact with fixed plane — only normal KE lost)}$$

## Successive Bounces (Dropped Sphere)

$$h_n = e^{2n}h_0, \quad v_n = e^n v_0, \quad t_n = e^n t_0$$

## Equal Masses, Perfectly Elastic

$$v_A = u_B, \quad v_B = u_A \quad \text{(velocities exchange)}$$

---

# 13. Cambridge Exam Analysis

## How Momentum Is Examined in 9231

### Paper Structure

- **Paper 4: Further Mechanics** — 3 questions, totalling ~50 marks, 1 hour 15 minutes.
- Momentum is **one full question** (typically Q1, Q2, or Q3), worth **10–14 marks**.
- The question often has 3–4 parts: (a) direct impact, (b) oblique impact, (c) energy loss or impulse.

### Topic Frequency (Based on Past Papers 2018–2024)

| Sub-topic | Frequency | Typical Marks |
|-----------|-----------|---------------|
| Direct impact of two spheres (find $e$ / velocities) | Very common — almost every paper | 4–6 |
| Oblique impact of two spheres | Common — every 2nd paper | 5–7 |
| Impact with fixed wall/plane (direct or oblique) | Common — every 2nd paper | 4–6 |
| Loss of kinetic energy / impulse calculation | Very common — tied to above | 2–4 |
| Successive bounces / multi-stage impacts | Occasional | 4–6 |
| Vector velocity after oblique impact (magnitude + direction) | Common | 3–4 |

### What Examiners Look For

| Assessment Point | How to Secure Marks |
|------------------|---------------------|
| **Momentum equation** | Write it explicitly with correct signs — M1 even if arithmetic is wrong |
| **NEL equation** | State $v_B - v_A = e(u_A - u_B)$ or $e = \frac{\text{sep}}{\text{app}}$ — M1 |
| **Resolving correctly** | Show $u\cos\theta$ and $u\sin\theta$ components — M1 |
| **Transverse components unchanged** | State $v_{Ay} = u_{Ay}$ explicitly — A1 |
| **Final answer with direction** | Give angle + what it is measured from (line of centres / wall / horizontal) |
| **Energy loss** | Show $KE = \frac{1}{2}mv^2$ for both before and after — M1 |

### Common Exam Question Structures

**Structure A — Direct Impact Chain (10 marks):**
> (a) Find $e$ given velocities before and after. [3]
> (b) Find the velocities after a subsequent impact. [5]
> (c) Find the loss of KE. [2]

**Structure B — Oblique Impact (12 marks):**
> (a) Resolve velocities, apply momentum + NEL along line of centres, find velocity of one sphere after. [6]
> (b) Find the speed and direction of the other sphere after. [3]
> (c) Find the impulse / energy loss. [3]

**Structure C — Wall Impact (10 marks):**
> A sphere strikes a smooth wall obliquely at angle $\alpha$ with speed $u$.
> (a) Find the speed and direction after impact in terms of $e$, $u$, $\alpha$. [4]
> (b) Given the rebound angle / speed, find $e$. [3]
> (c) Find the impulse exerted by the wall. [3]

### Time Allocation

- **10-mark question:** ~18 minutes (including checking signs)
- **14-mark question:** ~22 minutes
- Always spend the first 2 minutes drawing a clear diagram with labelled velocities and the line of centres / plane.

### Grade Boundaries Insight

- Momentum questions have a **high average score** (students who master the two-equation method score well).
- The differentiator is **oblique impacts** — students who confuse which direction has NEL vs which is unchanged lose 4–5 marks.
- Energy loss parts are often the easiest 2–3 marks — just compute $\frac{1}{2}mv^2$ before and after.

---

# 14. Practice Questions & Full Solutions

## Question 1 — Direct Impact: Find $e$ [Easy]

> **Question:** Two smooth spheres $A$ and $B$ of masses $4\text{ kg}$ and $6\text{ kg}$ are moving in the same direction on a smooth horizontal table. $A$ is behind $B$ with $u_A = 7\text{ m s}^{-1}$ and $u_B = 1\text{ m s}^{-1}$. After the direct impact, $A$ has velocity $2\text{ m s}^{-1}$ in the same direction. Find (a) the velocity of $B$ after impact, (b) the coefficient of restitution, and (c) the loss of kinetic energy.

<details>
<summary><strong>Solution</strong></summary>

**(a) Velocity of $B$:**

$$m_A u_A + m_B u_B = m_A v_A + m_B v_B$$

$$4(7) + 6(1) = 4(2) + 6v_B$$

$$28 + 6 = 8 + 6v_B$$

$$34 = 8 + 6v_B$$

$$6v_B = 26$$

$$v_B = \frac{13}{3} \approx 4.33\text{ m s}^{-1} \quad \checkmark$$

**(b) Coefficient of restitution:**

$$e = \frac{v_B - v_A}{u_A - u_B}$$

$$e = \frac{\frac{13}{3} - 2}{7 - 1}$$

$$e = \frac{\frac{7}{3}}{6}$$

$$e = \frac{7}{18} \approx 0.389 \quad \checkmark$$

**(c) Loss of KE:**

$$KE_{\text{before}} = \tfrac{1}{2}(4)(49) + \tfrac{1}{2}(6)(1) = 98 + 3 = 101\text{ J}$$

$$KE_{\text{after}} = \tfrac{1}{2}(4)(4) + \tfrac{1}{2}(6)\left(\tfrac{169}{9}\right) = 8 + \tfrac{169}{3} = 8 + 56.33 = 64.33\text{ J}$$

$$\Delta KE = 101 - 64.33 = 36.67\text{ J} = \tfrac{110}{3}\text{ J} \quad \checkmark$$

Exact: $KE_{\text{after}} = 8 + 507/9$ ... let's compute exactly:

$$KE_{\text{after}} = 8 + \frac{1}{2}(6)\cdot\frac{169}{9} = 8 + \frac{169}{3} = \frac{24+169}{3} = \frac{193}{3}$$

$$\Delta KE = 101 - \frac{193}{3} = \frac{303-193}{3} = \frac{110}{3} \approx 36.7\text{ J} \quad \checkmark$$

</details>

---

## Question 2 — Direct Impact: Approaching Spheres [Easy]

> **Question:** Two smooth spheres $P$ and $Q$ of masses $2\text{ kg}$ and $5\text{ kg}$ move directly towards each other with speeds $6\text{ m s}^{-1}$ and $3\text{ m s}^{-1}$ respectively. The coefficient of restitution is $e = 0.4$. Find the velocities of $P$ and $Q$ after the impact.

<details>
<summary><strong>Solution</strong></summary>

Take direction of $P$ as positive: $u_P = 6$, $u_Q = -3$.

Momentum:

$$2(6) + 5(-3) = 2v_P + 5v_Q$$

$$12 - 15 = 2v_P + 5v_Q$$

$$-3 = 2v_P + 5v_Q \quad \text{...(i)}$$

NEL:

$$v_Q - v_P = e(u_P - u_Q)$$

$$v_Q - v_P = 0.4(6 - (-3))$$

$$v_Q - v_P = 0.4 \times 9 = 3.6 \quad \text{...(ii)}$$

From (ii): $v_Q = v_P + 3.6$. Into (i):

$$-3 = 2v_P + 5(v_P + 3.6)$$

$$-3 = 7v_P + 18$$

$$7v_P = -21$$

$$v_P = -3\text{ m s}^{-1}$$

$$v_Q = 0.6\text{ m s}^{-1} \quad \checkmark$$

$P$ rebounds at $3\text{ m s}^{-1}$, $Q$ moves slowly in $P$'s original direction at $0.6\text{ m s}^{-1}$.

</details>

---

## Question 3 — Direct Impact with Fixed Wall [Easy]

> **Question:** A smooth sphere of mass $0.8\text{ kg}$ strikes a fixed smooth wall directly with speed $10\text{ m s}^{-1}$ and rebounds with speed $6\text{ m s}^{-1}$. Find (a) the coefficient of restitution, (b) the magnitude of the impulse exerted by the wall on the sphere, and (c) the loss of kinetic energy.

<details>
<summary><strong>Solution</strong></summary>

**(a)**

$$e = \frac{v}{u} = \frac{6}{10} = 0.6 \quad \checkmark$$

**(b)**

$$J = m(v + u) = 0.8(6 + 10) = 0.8 \times 16 = 12.8\text{ N s} \quad \checkmark$$

(More formally: $J = m(v - (-u)) = m(v+u)$ taking rebound as positive.)

**(c)**

$$KE_{\text{before}} = \tfrac{1}{2}(0.8)(100) = 40\text{ J}$$

$$KE_{\text{after}} = \tfrac{1}{2}(0.8)(36) = 14.4\text{ J}$$

$$\Delta KE = 40 - 14.4 = 25.6\text{ J} \quad \checkmark$$

</details>

---

## Question 4 — Oblique Impact with Fixed Wall [Medium]

> **Question:** A smooth sphere strikes a fixed smooth vertical wall with speed $8\text{ m s}^{-1}$ at an angle of $30°$ to the wall. After impact it rebounds with speed $6\text{ m s}^{-1}$. Find (a) the coefficient of restitution, (b) the direction of the rebound (angle to the wall), and (c) the impulse exerted by the wall.

<details>
<summary><strong>Solution</strong></summary>

Let $x$ = normal to wall, $y$ = parallel to wall. Mass = $m$ (cancels for (a) and (b); keep symbolic).

$$u_{\perp} = 8\sin 30° = 8 \times 0.5 = 4\text{ m s}^{-1}$$

$$u_{\parallel} = 8\cos 30° = 8 \times \tfrac{\sqrt{3}}{2} = 4\sqrt{3}\text{ m s}^{-1}$$

After impact:

$$v_{\parallel} = u_{\parallel} = 4\sqrt{3}\text{ m s}^{-1}$$

$$v_{\perp} = e \cdot u_{\perp} = 4e$$

Speed after:

$$|\mathbf{v}|^2 = v_{\perp}^2 + v_{\parallel}^2 = 16e^2 + 48 = 36 \quad (\text{given }|\mathbf{v}|=6)$$

$$16e^2 = 36 - 48 = -12$$

This gives $e^2 < 0$ — impossible! Let us re-read: speed after is $6$, but parallel component alone is $4\sqrt{3} \approx 6.93 > 6$. The parallel component cannot exceed the total speed. The question data as stated is inconsistent with a smooth wall (parallel component must be $\leq$ total speed).

**Revised (consistent) version:** Suppose the sphere strikes at $60°$ to the wall with speed $8$:

$$u_{\perp} = 8\sin 60° = 4\sqrt{3} \approx 6.93\text{ m s}^{-1}$$

$$u_{\parallel} = 8\cos 60° = 4\text{ m s}^{-1}$$

$$v_{\parallel} = 4, \quad v_{\perp} = e \cdot 4\sqrt{3}$$

$$|\mathbf{v}|^2 = 16 + 48e^2$$

If $|\mathbf{v}| = 7$ (for example):

$$49 = 16 + 48e^2$$

$$e^2 = \frac{33}{48} = \frac{11}{16}$$

$$e = \frac{\sqrt{11}}{4} \approx 0.829 \quad \checkmark$$

**For the original question with consistent data** (strikes at $30°$ to wall, speed $8$, rebounds at speed $7$):

$$49 = 48 + 16e^2 \implies e^2 = \tfrac{1}{16} \implies e = \tfrac{1}{4}$$

$$\tan\beta = \frac{v_{\perp}}{v_{\parallel}} = \frac{4(1/4)}{4\sqrt{3}} = \frac{1}{4\sqrt{3}}$$

$$\beta = \tan^{-1}\left(\tfrac{1}{4\sqrt{3}}\right) \approx 8.21° \text{ to wall} \quad \checkmark$$

$$J = m(v_{\perp} + u_{\perp}) = m\left(1 + \tfrac{1}{4}\right)(4) = 5m\text{ N s} \quad \checkmark$$

> The key lesson: always check that $v_{\parallel} \leq |\mathbf{v}|$ — the parallel component is part of the total speed!

</details>

---

## Question 5 — Oblique Impact of Two Spheres [Medium]

> **Question:** Two smooth spheres $A$ and $B$ of masses $4\text{ kg}$ and $2\text{ kg}$ are on a smooth horizontal table. The line of centres at impact is along the $x$-axis. Before impact: $\mathbf{u}_A = 5\mathbf{i} + 2\mathbf{j}$ and $\mathbf{u}_B = -\mathbf{i} + 2\mathbf{j}$ (in $\text{m s}^{-1}$). The coefficient of restitution is $e = 0.5$. Find the velocities after impact.

<details>
<summary><strong>Solution</strong></summary>

$$u_{Ax} = 5,\; u_{Ay} = 2, \quad u_{Bx} = -1,\; u_{By} = 2$$

Transverse unchanged:

$$v_{Ay} = 2, \quad v_{By} = 2$$

Along $x$ — momentum:

$$4(5) + 2(-1) = 4v_{Ax} + 2v_{Bx}$$

$$20 - 2 = 4v_{Ax} + 2v_{Bx}$$

$$18 = 4v_{Ax} + 2v_{Bx}$$

$$9 = 2v_{Ax} + v_{Bx} \quad \text{...(i)}$$

NEL along $x$:

$$v_{Bx} - v_{Ax} = 0.5(5 - (-1))$$

$$v_{Bx} - v_{Ax} = 0.5 \times 6 = 3 \quad \text{...(ii)}$$

From (ii): $v_{Bx} = v_{Ax} + 3$. Into (i):

$$9 = 2v_{Ax} + v_{Ax} + 3$$

$$3v_{Ax} = 6$$

$$v_{Ax} = 2\text{ m s}^{-1}$$

$$v_{Bx} = 5\text{ m s}^{-1}$$

$$\mathbf{v}_A = 2\mathbf{i} + 2\mathbf{j}\text{ m s}^{-1}, \quad \mathbf{v}_B = 5\mathbf{i} + 2\mathbf{j}\text{ m s}^{-1} \quad \checkmark$$

$$|\mathbf{v}_A| = \sqrt{8} = 2\sqrt{2}\text{ m s}^{-1}, \quad |\mathbf{v}_B| = \sqrt{29}\text{ m s}^{-1}$$

</details>

---

## Question 6 — Oblique Impact: Finding $e$ from Rebound Angle [Medium-Hard]

> **Question:** A smooth sphere of mass $m$ strikes a fixed smooth wall with speed $u$ at an angle $\alpha$ to the wall. It rebounds with speed $\frac{3u}{4}$ at an angle of $30°$ to the wall. Given that $\alpha = 60°$, find the coefficient of restitution $e$ and verify consistency.

<details>
<summary><strong>Solution</strong></summary>

$$u_{\perp} = u\sin 60° = \tfrac{\sqrt{3}}{2}u$$

$$u_{\parallel} = u\cos 60° = \tfrac{1}{2}u$$

After:

$$v_{\parallel} = u_{\parallel} = \tfrac{1}{2}u$$

$$v_{\perp} = e \cdot u_{\perp} = e\cdot\tfrac{\sqrt{3}}{2}u$$

Speed after:

$$|\mathbf{v}|^2 = v_{\perp}^2 + v_{\parallel}^2 = \frac{3e^2 u^2}{4} + \frac{u^2}{4} = \frac{u^2}{4}(3e^2 + 1)$$

Given $|\mathbf{v}| = \frac{3u}{4}$:

$$\frac{9u^2}{16} = \frac{u^2}{4}(3e^2 + 1)$$

$$\frac{9}{4} = 3e^2 + 1$$

$$3e^2 = \frac{5}{4}$$

$$e^2 = \frac{5}{12}$$

$$e = \sqrt{\tfrac{5}{12}} \approx 0.645 \quad \checkmark$$

Check angle: $\tan 30° = \frac{v_{\perp}}{v_{\parallel}} = \frac{e\sqrt{3}/2}{1/2} = e\sqrt{3}$

$$e\sqrt{3} = \sqrt{\tfrac{5}{12}}\cdot\sqrt{3} = \sqrt{\tfrac{5}{4}} = \tfrac{\sqrt{5}}{2} \approx 1.118$$

But $\tan 30° = 1/\sqrt{3} \approx 0.577 \neq 1.118$ — **inconsistent!**

If instead we use the angle condition directly: $\tan 30° = e\tan 60°$:

$$\tfrac{1}{\sqrt{3}} = e\sqrt{3}$$

$$e = \tfrac{1}{3} \quad \checkmark$$

Then $|\mathbf{v}| = \sqrt{(e\cdot\frac{\sqrt{3}}{2}u)^2 + (\frac{1}{2}u)^2} = \sqrt{\frac{u^2}{12}+\frac{u^2}{4}} = \sqrt{\frac{u^2}{3}} = \frac{u}{\sqrt{3}} \neq \frac{3u}{4}$.

**Conclusion:** The speed and angle conditions over-determine $e$ — only two of the three (angle before, angle after, speed after) can be independently specified. In an exam, you will be given consistent data and asked to find $e$ from one condition.

Using angle condition alone with $\alpha = 60°$, $\beta = 30°$:

$$e = \frac{\tan 30°}{\tan 60°} = \frac{1/\sqrt{3}}{\sqrt{3}} = \frac{1}{3} \quad \checkmark$$

</details>

---

## Question 7 — Loss of KE in Oblique Impact [Medium]

> **Question:** Two smooth spheres $A$ ($3\text{ kg}$) and $B$ ($1\text{ kg}$) collide obliquely. The line of centres is along the $x$-axis. Before impact: $A$ has velocity $4\mathbf{i} + 2\mathbf{j}$, $B$ has velocity $-2\mathbf{i} + 5\mathbf{j}$ (in $\text{m s}^{-1}$). After impact: $A$ has velocity $\mathbf{i} + 2\mathbf{j}$, $B$ has velocity $7\mathbf{i} + 5\mathbf{j}$. Find (a) $e$, (b) the loss of KE, and (c) the impulse exerted on $B$.

<details>
<summary><strong>Solution</strong></summary>

**(a) Coefficient of restitution (along $x$):**

$$u_{Ax} = 4,\; u_{Bx} = -2, \quad v_{Ax} = 1,\; v_{Bx} = 7$$

$$e = \frac{v_{Bx} - v_{Ax}}{u_{Ax} - u_{Bx}} = \frac{7-1}{4-(-2)} = \frac{6}{6} = 1 \quad \checkmark$$

Perfectly elastic along the line of centres!

Check $y$-components: $v_{Ay} = u_{Ay} = 2$, $v_{By} = u_{By} = 5$ — consistent with smooth (unchanged). ✅

**(b) Loss of KE:**

Since $e = 1$, we expect no loss. Verify:

$$KE_{\text{before}} = \tfrac{1}{2}(3)(16+4) + \tfrac{1}{2}(1)(4+25) = \tfrac{1}{2}(3)(20) + \tfrac{1}{2}(29) = 30 + 14.5 = 44.5\text{ J}$$

$$KE_{\text{after}} = \tfrac{1}{2}(3)(1+4) + \tfrac{1}{2}(1)(49+25) = \tfrac{1}{2}(3)(5) + \tfrac{1}{2}(74) = 7.5 + 37 = 44.5\text{ J}$$

$$\Delta KE = 0\text{ J} \quad \checkmark$$

**(c) Impulse on $B$ (along line of centres only — smooth):**

$$J_B = m_B(v_{Bx} - u_{Bx}) = 1(7-(-2)) = 9\text{ N s in positive }x\text{-direction}$$

$$\mathbf{J}_B = 9\mathbf{i}\text{ N s} \quad \checkmark$$

(Impulse on $A$: $3(1-4) = -9\mathbf{i}$ — equal and opposite ✅)

</details>

---

## Question 8 — Successive Impacts / Wall Bounce Chain [Hard]

> **Question:** A smooth sphere $A$ of mass $2\text{ kg}$ moves on a smooth horizontal table towards a fixed smooth vertical wall. The wall is $3\text{ m}$ from $A$'s starting position. $A$ is projected towards the wall with speed $6\text{ m s}^{-1}$ directly towards the wall. The coefficient of restitution between $A$ and the wall is $e = 0.5$. A second sphere $B$ of mass $3\text{ kg}$ is initially at rest $1\text{ m}$ from the wall, between $A$ and the wall. After $A$ rebounds from the wall, it collides directly with $B$. Find (a) the speed of $A$ after rebounding from the wall, (b) the velocities of $A$ and $B$ after they collide (given $e_{AB} = 0.6$), and (c) the total loss of KE in both impacts combined.

<details>
<summary><strong>Solution</strong></summary>

**(a) $A$ rebounds from wall:**

$$v_A^{\text{(after wall)}} = e \cdot u_A = 0.5 \times 6 = 3\text{ m s}^{-1} \text{ away from wall} \quad \checkmark$$

**(b) $A$ collides with $B$:**

Now $A$ moves away from wall (towards $B$) at $3\text{ m s}^{-1}$. $B$ is at rest. Take away from wall as positive? Let's take towards wall as positive initially, but after rebound $A$ moves negative. Easier: take the direction from wall outward as positive.

$$u_A = 3,\; u_B = 0,\; m_A = 2,\; m_B = 3,\; e_{AB} = 0.6$$

But careful: $A$ is between wall and $B$? Actually $B$ is between $A$ and wall. After $A$ rebounds, $A$ moves away from wall and will meet $B$ which is between $A$'s rebound path. Let's set positive = away from wall (direction $A$ rebounds).

$A$ approaches $B$ from the wall side. $B$ may be pushed further from wall.

Momentum:

$$2(3) + 3(0) = 2v_A + 3v_B$$

$$6 = 2v_A + 3v_B \quad \text{...(i)}$$

NEL:

$$v_B - v_A = 0.6(3 - 0) = 1.8 \quad \text{...(ii)}$$

From (ii): $v_B = v_A + 1.8$. Into (i):

$$6 = 2v_A + 3(v_A + 1.8) = 5v_A + 5.4$$

$$5v_A = 0.6$$

$$v_A = 0.12\text{ m s}^{-1}, \quad v_B = 1.92\text{ m s}^{-1} \quad \checkmark$$

Both move away from wall after.

**(c) Total KE loss:**

$$KE_{\text{initial}} = \tfrac{1}{2}(2)(36) = 36\text{ J}$$

After wall bounce:

$$KE_{\text{after wall}} = \tfrac{1}{2}(2)(9) = 9\text{ J}$$

$$\Delta KE_{\text{wall}} = 27\text{ J}$$

After $A$-$B$ collision:

$$KE_{\text{final}} = \tfrac{1}{2}(2)(0.0144) + \tfrac{1}{2}(3)(3.6864) = 0.0144 + 5.5296 = 5.544\text{ J}$$

$$\Delta KE_{AB} = 9 - 5.544 = 3.456\text{ J}$$

$$\Delta KE_{\text{total}} = 27 + 3.456 = 30.456\text{ J} \quad \checkmark$$

Total KE remaining: $5.544\text{ J}$.

</details>

---

## Question 9 — General Oblique Impact with Energy Check [Hard]

> **Question:** Two smooth spheres $A$ and $B$, each of mass $m$, collide obliquely. The line of centres at impact is along the $x$-axis. Before impact, $A$ has speed $10\text{ m s}^{-1}$ at $60°$ to the line of centres and $B$ has speed $5\text{ m s}^{-1}$ along the line of centres towards $A$. The coefficient of restitution is $e = 0.7$. Find (a) the velocities after impact (vector form), (b) the deflection angle of $A$ (angle between its velocity before and after), and (c) the fraction of KE lost.

<details>
<summary><strong>Solution</strong></summary>

$$u_{Ax} = 10\cos 60° = 5,\; u_{Ay} = 10\sin 60° = 5\sqrt{3}$$

$$u_{Bx} = -5,\; u_{By} = 0$$

Transverse:

$$v_{Ay} = 5\sqrt{3}, \quad v_{By} = 0$$

Along $x$ — momentum ($m$ cancels):

$$5 + (-5) = v_{Ax} + v_{Bx}$$

$$v_{Ax} + v_{Bx} = 0 \quad \text{...(i)}$$

NEL:

$$v_{Bx} - v_{Ax} = 0.7(5 - (-5))$$

$$v_{Bx} - v_{Ax} = 7 \quad \text{...(ii)}$$

From (i): $v_{Bx} = -v_{Ax}$. Into (ii):

$$-v_{Ax} - v_{Ax} = 7$$

$$v_{Ax} = -3.5,\quad v_{Bx} = 3.5 \quad \checkmark$$

**(a)**

$$\mathbf{v}_A = -3.5\mathbf{i} + 5\sqrt{3}\,\mathbf{j}\text{ m s}^{-1}$$

$$\mathbf{v}_B = 3.5\mathbf{i}\text{ m s}^{-1} \quad \checkmark$$

$$|\mathbf{v}_A| = \sqrt{12.25 + 75} = \sqrt{87.25} \approx 9.34\text{ m s}^{-1}$$

$$|\mathbf{v}_B| = 3.5\text{ m s}^{-1}$$

**(b) Deflection of $A$:**

$$\cos\theta = \frac{\mathbf{u}_A \cdot \mathbf{v}_A}{|\mathbf{u}_A||\mathbf{v}_A|} = \frac{(5)(-3.5) + (5\sqrt{3})(5\sqrt{3})}{10 \times 9.34}$$

$$\cos\theta = \frac{-17.5 + 75}{93.4} = \frac{57.5}{93.4} = 0.6156$$

$$\theta = \cos^{-1}(0.6156) \approx 52.0° \quad \checkmark$$

**(c) Fraction of KE lost:**

$$KE_{\text{before}} = \tfrac{1}{2}m(100) + \tfrac{1}{2}m(25) = 62.5m$$

$$KE_{\text{after}} = \tfrac{1}{2}m(87.25) + \tfrac{1}{2}m(12.25) = 49.75m$$

$$\Delta KE = 12.75m$$

$$\text{Fraction lost} = \frac{12.75}{62.5} = 0.204 = 20.4\% \quad \checkmark$$

Check: $\Delta KE$ should equal $\frac{1}{2}\frac{m^2}{2m}(1-e^2)(10)^2$ for the $x$-direction only? Actually for oblique: only $x$-components contribute to loss:

$$\Delta KE_x = \tfrac{1}{2}\tfrac{m}{2}(1-0.49)(10)^2 = \tfrac{m}{4}(0.51)(100) = 12.75m \quad \checkmark$$

</details>

---

## Question 10 — Impact at an Angle: Finding $e$ from Given Data [Medium]

> **Question:** A smooth sphere of mass $0.5\text{ kg}$ is moving with velocity $(6\mathbf{i} - 4\mathbf{j})\text{ m s}^{-1}$ towards a fixed smooth wall. The wall lies along the $y$-axis (so the normal is along $\mathbf{i}$). The sphere strikes the wall and rebounds with velocity $(-3\mathbf{i} - 4\mathbf{j})\text{ m s}^{-1}$ (note: this means the $\mathbf{i}$-component values given are before/after with signs). Actually the sphere approaches with $\mathbf{u} = -6\mathbf{i} - 4\mathbf{j}$ (towards wall at $x=0$) — reframe: the sphere has velocity $6\text{ m s}^{-1}$ towards the wall (normal) and $4\text{ m s}^{-1}$ parallel to the wall. After impact its normal component is $3\text{ m s}^{-1}$ away. Find $e$ and the impulse.

<details>
<summary><strong>Solution</strong></summary>

Normal direction: $\mathbf{i}$ (perpendicular to wall along $y$-axis). Parallel: $\mathbf{j}$.

$$u_{\perp} = 6\text{ m s}^{-1} \text{ (towards wall)}$$

$$u_{\parallel} = 4\text{ m s}^{-1}$$

$$v_{\perp} = 3\text{ m s}^{-1} \text{ (away from wall)}$$

$$v_{\parallel} = 4\text{ m s}^{-1} \text{ (unchanged — smooth, check: given as }4\text{, consistent ✅)}$$

$$e = \frac{v_{\perp}}{u_{\perp}} = \frac{3}{6} = 0.5 \quad \checkmark$$

Impulse (normal direction, on sphere):

$$J = m(v_{\perp} - (-u_{\perp})) = 0.5(3 + 6) = 4.5\text{ N s}$$

$$\mathbf{J} = 4.5\mathbf{i}\text{ N s (away from wall)} \quad \checkmark$$

If vector form with wall at $x=0$, $\mathbf{u} = -6\mathbf{i} + 4\mathbf{j}$, $\mathbf{v} = 3\mathbf{i} + 4\mathbf{j}$:

$$\mathbf{J} = m(\mathbf{v} - \mathbf{u})_{\perp} = 0.5((3-(-6))\mathbf{i}) = 4.5\mathbf{i}\text{ N s} \quad \checkmark$$

(The $\mathbf{j}$-component of impulse is zero — smooth wall.)

</details>

---

## Question 11 — Complex Oblique + Wall Chain (Hard) [Exam Style, 12 marks]

> **Question:** Two smooth spheres $A$ and $B$ of masses $3\text{ kg}$ and $1\text{ kg}$ collide obliquely on a smooth horizontal table. The line of centres at impact is along the $x$-axis. Before impact:
> $$\mathbf{u}_A = (4\mathbf{i} + 2\mathbf{j})\text{ m s}^{-1}, \quad \mathbf{u}_B = (-2\mathbf{i} + 5\mathbf{j})\text{ m s}^{-1}$$
> The coefficient of restitution between $A$ and $B$ is $e = 0.5$. After the impact, sphere $B$ strikes a fixed smooth vertical wall which is parallel to the $y$-axis (normal along $x$). The coefficient of restitution between $B$ and the wall is $e_W = 0.6$.
> Find (a) the velocities of $A$ and $B$ after the $A$–$B$ impact [5], (b) the velocity of $B$ after rebounding from the wall [3], and (c) the total loss of KE in both impacts [4].

<details>
<summary><strong>Solution</strong></summary>

**(a) $A$–$B$ impact — line of centres along $x$:**

$$u_{Ax} = 4, \quad u_{Ay} = 2$$

$$u_{Bx} = -2, \quad u_{By} = 5$$

Transverse unchanged:

$$v_{Ay} = 2, \quad v_{By} = 5$$

Momentum along $x$:

$$m_A u_{Ax} + m_B u_{Bx} = m_A v_{Ax} + m_B v_{Bx}$$

$$3(4) + 1(-2) = 3v_{Ax} + 1v_{Bx}$$

$$12 - 2 = 3v_{Ax} + v_{Bx}$$

$$10 = 3v_{Ax} + v_{Bx} \quad \text{...(i)}$$

NEL along $x$:

$$v_{Bx} - v_{Ax} = e(u_{Ax} - u_{Bx})$$

$$v_{Bx} - v_{Ax} = 0.5(4 - (-2))$$

$$v_{Bx} - v_{Ax} = 0.5 \times 6$$

$$v_{Bx} - v_{Ax} = 3 \quad \text{...(ii)}$$

From (ii):

$$v_{Bx} = v_{Ax} + 3$$

Into (i):

$$10 = 3v_{Ax} + v_{Ax} + 3$$

$$4v_{Ax} = 7$$

$$v_{Ax} = 1.75\text{ m s}^{-1}$$

$$v_{Bx} = 4.75\text{ m s}^{-1}$$

$$\mathbf{v}_A = 1.75\mathbf{i} + 2\mathbf{j}\text{ m s}^{-1} \quad \checkmark$$

$$\mathbf{v}_B = 4.75\mathbf{i} + 5\mathbf{j}\text{ m s}^{-1} \quad \checkmark$$

**(b) $B$ strikes wall — normal along $x$:**

$$v_{B\perp}^{\text{before}} = 4.75\text{ m s}^{-1} \quad \text{(towards wall)}$$

$$v_{B\parallel}^{\text{before}} = 5\text{ m s}^{-1}$$

After wall:

$$v'_{B\parallel} = 5\text{ m s}^{-1} \quad \text{(unchanged, smooth)}$$

$$v'_{B\perp} = e_W \cdot v_{B\perp}^{\text{before}}$$

$$v'_{B\perp} = 0.6 \times 4.75$$

$$v'_{B\perp} = 2.85\text{ m s}^{-1} \quad \text{(away from wall)}$$

$$\mathbf{v}'_B = -2.85\mathbf{i} + 5\mathbf{j}\text{ m s}^{-1} \quad \text{(if }\mathbf{i}\text{ was towards wall)} \quad \checkmark$$

Magnitude:

$$|\mathbf{v}'_B| = \sqrt{2.85^2 + 25}$$

$$|\mathbf{v}'_B| = \sqrt{8.1225 + 25}$$

$$|\mathbf{v}'_B| = \sqrt{33.1225} \approx 5.76\text{ m s}^{-1}$$

Direction:

$$\tan\beta = \frac{2.85}{5} = 0.57 \text{ (perp/parallel, angle to wall)}$$

$$\beta = \tan^{-1}(0.57) \approx 29.7° \text{ to the wall} \quad \checkmark$$

**(c) Total KE loss:**

$$KE_{\text{before}} = \frac{1}{2}(3)(16+4) + \frac{1}{2}(1)(4+25)$$

$$KE_{\text{before}} = 1.5 \times 20 + 0.5 \times 29$$

$$KE_{\text{before}} = 30 + 14.5 = 44.5\text{ J}$$

$$KE_{\text{after }AB} = \frac{1}{2}(3)(1.75^2+4) + \frac{1}{2}(1)(4.75^2+25)$$

$$KE_{\text{after }AB} = 1.5 \times 7.0625 + 0.5 \times 47.5625$$

$$KE_{\text{after }AB} = 10.5938 + 23.7813 = 34.375\text{ J}$$

$$\Delta KE_{AB} = 44.5 - 34.375 = 10.125\text{ J}$$

$$KE_{\text{final}} = \frac{1}{2}(3)|\mathbf{v}_A|^2 + \frac{1}{2}(1)|\mathbf{v}'_B|^2$$

$$KE_{\text{final}} = 10.5938 + 0.5 \times 33.1225$$

$$KE_{\text{final}} = 10.5938 + 16.5613 = 27.155\text{ J}$$

$$\Delta KE_{\text{wall}} = 34.375 - 27.155 = 7.22\text{ J}$$

$$\Delta KE_{\text{total}} = 10.125 + 7.22 = 17.345\text{ J} \quad \checkmark$$

$$\text{Fraction lost} = \frac{17.345}{44.5} \approx 39.0\% \quad \checkmark$$

</details>

---

## Question 12 — Direct Impact with Energy Condition (Medium-Hard)

> **Question:** Two smooth spheres $A$ and $B$ of masses $m$ and $3m$ respectively are moving directly towards each other on a smooth horizontal table with speeds $u$ and $2u$ respectively. The coefficient of restitution between them is $e$. Find the velocities after impact in terms of $u$ and $e$, and find the fraction of KE lost in terms of $e$. Evaluate for $e = 0.6$.

<details>
<summary><strong>Solution</strong></summary>

Take $A$'s initial direction as positive:

$$u_A = u, \quad u_B = -2u$$

Let $v_A$ and $v_B$ be velocities after.

Momentum:

$$m(u) + 3m(-2u) = m v_A + 3m v_B$$

$$mu - 6mu = mv_A + 3mv_B$$

$$-5mu = mv_A + 3mv_B$$

$$-5u = v_A + 3v_B \quad \text{...(i)}$$

NEL:

$$v_B - v_A = e(u_A - u_B)$$

$$v_B - v_A = e(u - (-2u))$$

$$v_B - v_A = 3eu \quad \text{...(ii)}$$

From (ii):

$$v_B = v_A + 3eu$$

Into (i):

$$-5u = v_A + 3(v_A + 3eu)$$

$$-5u = 4v_A + 9eu$$

$$4v_A = -5u - 9eu$$

$$v_A = -\frac{(5+9e)u}{4}$$

$$v_B = -\frac{(5+9e)u}{4} + 3eu$$

$$v_B = \frac{(-5-9e+12e)u}{4}$$

$$v_B = \frac{(-5+3e)u}{4} \quad \checkmark$$

For $0 \leq e \leq 1$, both $v_A < 0$ and $v_B < 0$ — both continue in $B$'s original direction, with $A$ rebounding and $B$ slowing.

KE loss in terms of $e$:

$$KE_{\text{before}} = \frac{1}{2}m u^2 + \frac{1}{2}(3m)(4u^2)$$

$$KE_{\text{before}} = 0.5mu^2 + 6mu^2$$

$$KE_{\text{before}} = 6.5mu^2$$

$$KE_{\text{after}} = \frac{1}{2}m v_A^2 + \frac{1}{2}(3m)v_B^2$$

$$KE_{\text{after}} = \frac{mu^2}{32}(5+9e)^2 + \frac{3mu^2}{32}(5-3e)^2$$

$$KE_{\text{after}} = \frac{mu^2}{32}\left[(25+90e+81e^2) + 3(25-30e+9e^2)\right]$$

$$KE_{\text{after}} = \frac{mu^2}{32}\left[25+90e+81e^2+75-90e+27e^2\right]$$

$$KE_{\text{after}} = \frac{mu^2}{32}\left[100+108e^2\right]$$

$$\Delta KE = 6.5mu^2 - \frac{mu^2}{32}(100+108e^2)$$

$$\Delta KE = mu^2\left(6.5 - 3.125 - 3.375e^2\right)$$

$$\Delta KE = mu^2(3.375 - 3.375e^2)$$

$$\Delta KE = 3.375mu^2(1-e^2) \quad \checkmark$$

Check with general formula:

$$\Delta KE = \frac{1}{2}\cdot\frac{3m^2}{4m}\cdot(1-e^2)(3u)^2$$

$$\Delta KE = \frac{3m}{8}\cdot(1-e^2)\cdot 9u^2$$

$$\Delta KE = \frac{27}{8}mu^2(1-e^2) = 3.375mu^2(1-e^2) \quad \checkmark$$

For $e = 0.6$:

$$\Delta KE = 3.375mu^2(1-0.36)$$

$$\Delta KE = 3.375 \times 0.64\, mu^2$$

$$\Delta KE = 2.16mu^2$$

$$\text{Fraction lost} = \frac{2.16}{6.5} \approx 33.2\% \quad \checkmark$$

> **⚠️ Watch Out!** When deriving $v_A$, $v_B$ in terms of $e$ and $u$, keep the algebra symbolic as long as possible — substituting $e=0.6$ too early hides the $(1-e^2)$ structure that examiners expect you to identify.

</details>

---

# 15. Quick Reference Card

Cut this out for last-minute revision.

### Conservation of Momentum (Direct)

$$m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2$$

### Newton's Experimental Law

$$e = \frac{v_B - v_A}{u_A - u_B} \quad (0 \leq e \leq 1)$$

$$e=1: \text{ elastic}, \quad e=0: \text{ inelastic } (v_A = v_B)$$

### Fixed Wall — Direct

$$v = eu, \quad J = m(1+e)u$$

### Fixed Plane — Oblique

$$v_{\parallel} = u_{\parallel}, \quad v_{\perp} = eu_{\perp}$$

$$\tan\beta = e\tan\alpha \quad (\alpha, \beta \text{ to plane})$$

### Two Spheres — Oblique (Line of Centres = $x$)

$$m_A u_{Ax} + m_B u_{Bx} = m_A v_{Ax} + m_B v_{Bx} \quad ✅$$

$$v_{Bx} - v_{Ax} = e(u_{Ax} - u_{Bx}) \quad ✅$$

$$v_{Ay} = u_{Ay}, \quad v_{By} = u_{By} \quad ✅$$

### After Oblique Impact

$$|\mathbf{v}| = \sqrt{v_x^2 + v_y^2}, \quad \tan\theta = \frac{v_y}{v_x}$$

### Loss of KE

$$\Delta KE = KE_{\text{before}} - KE_{\text{after}}$$

$$\Delta KE = \tfrac{1}{2}\tfrac{m_1 m_2}{m_1+m_2}(1-e^2)(u_1-u_2)^2 \quad \text{(direct)}$$

$$\Delta KE = \tfrac{1}{2}m(1-e^2)u_{\perp}^2 \quad \text{(fixed plane)}$$

### Successive Bounces

$$h_n = e^{2n}h_0$$

### Deadly Sins

1. Sign errors — use **signed** velocities consistently ❌
2. Applying NEL perpendicular to line of centres ❌
3. Forgetting $v_{\parallel}$ unchanged for smooth planes ❌
4. Confusing angle to plane vs angle to normal ❌
5. Assuming KE conserved (only when $e=1$) ❌
6. Not recombining $x$ and $y$ when asked for "velocity" ❌
7. Accepting $e > 1$ without flagging impossibility ❌

---

> **Good luck! Every Cambridge Momentum question is momentum + NEL (+ transverse unchanged for oblique). Master the two equations and the resolve step — that's 90% of the marks.** 🚀

---

