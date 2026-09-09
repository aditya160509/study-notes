# 🔄 FURTHER MATHS CIRCULAR MOTION — ULTIMATE STUDY GUIDE

## Cambridge International AS & A Level Further Mathematics (9231) — Further Mechanics §3.3

> **The complete walkthrough:** Angular speed, velocity–radius relations, centripetal acceleration, horizontal circular motion (conical pendulum, banked tracks, string tension) and vertical circular motion with energy conservation — every technique explained step-by-step with 8 fully solved worked examples in proper LaTeX. Covers critical speeds, string-slack conditions, and complete-circle criteria.

---

# 📋 Table of Contents

1. [How To Use This Guide](#how-to-use-this-guide)
2. [Syllabus Requirements](#1-syllabus-requirements)
3. [Prerequisites](#2-prerequisites)
4. [Angular Speed & Circular Kinematics](#3-angular-speed--circular-kinematics)
5. [Centripetal Acceleration](#4-centripetal-acceleration)
6. [Horizontal Circular Motion — Fundamentals](#5-horizontal-circular-motion--fundamentals)
7. [The Conical Pendulum](#6-the-conical-pendulum)
8. [Banked Tracks & Other Horizontal Circles](#7-banked-tracks--other-horizontal-circles)
9. [Vertical Circular Motion — Energy Conservation](#8-vertical-circular-motion--energy-conservation)
10. [Tension & Normal Reaction in the Vertical Circle](#9-tension--normal-reaction-in-the-vertical-circle)
11. [Critical Speeds, String Going Slack & Leaving the Circle](#10-critical-speeds-string-going-slack--leaving-the-circle)
12. [Conditions for Complete Circles](#11-conditions-for-complete-circles)
13. [Hooke's Law & Elastic Strings in Circular Motion](#12-hookes-law--elastic-strings-in-circular-motion)
14. [Worked Examples — Complete Solutions](#13-worked-examples--complete-solutions)
15. [Common Mistakes](#14-common-mistakes)
16. [Complete Formula Sheet](#15-complete-formula-sheet)
17. [Cambridge Exam Analysis](#16-cambridge-exam-analysis)
18. [Practice Questions & Full Solutions](#17-practice-questions--full-solutions)
19. [Quick Reference Card](#18-quick-reference-card)

---

# How To Use This Guide

Each section follows this structure:

1. **The Rule** — the formula you must know (in a boxed $$\LaTeX$$ display)
2. **Step-by-Step Method** — a numbered algorithm you can follow under exam pressure
3. **Worked Examples** — labelled **Example N** with a **Question** / **Solution** split and every algebra step on its own display line
4. **Watch Out!** — common pitfalls in a highlighted box
5. **What the examiner wants** — what scores the marks

> **How to revise with this guide:** Read §3–§4 for the kinematics, then §5–§7 for all horizontal motion, then §8–§12 for vertical circles (the hardest part). Attempt every worked example with the question covered before revealing the solution. Finish with the Practice Questions under timed conditions.

---

# 1. Syllabus Requirements

## What Cambridge Expects for Circular Motion (9231 FM §3.3)

According to the CAIE 9231 syllabus for Further Mechanics, Section 3.3:

| Topic | What You Must Be Able To Do |
|-------|------------------------------|
| **Angular speed** | Define and use $\omega$; relate $\omega$ to linear speed via $v = r\omega$ |
| **Centripetal acceleration** | Recall and use $a = r\omega^{2} = v^{2}/r$ towards the centre (no proof required) |
| **Horizontal circular motion** | Analyse motion in a horizontal circle: conical pendulum, particle on a banked track, tension in a horizontal string |
| **Vertical circular motion** | Analyse motion in a vertical circle **without loss of energy**: use conservation of mechanical energy |
| **Energy + circular motion** | Combine $\tfrac12 mv^{2} + mgh = \text{constant}$ with $F = ma$ towards the centre to find tensions / normal reactions |
| **Critical conditions** | Find where tension or normal reaction becomes zero; determine conditions for complete circles and for leaving the circle |
| **Elastic strings** | Where relevant, combine Hooke's law / elastic energy with circular motion |

### 🟢 Cambridge Assessment Objectives

| AO | Weight | What It Means |
|----|--------|---------------|
| **AO1** | ~50% | Recall, select and use facts, concepts and techniques — know $v=r\omega$, $a=r\omega^{2}$, energy conservation |
| **AO2** | ~50% | Construct arguments, solve problems, interpret results — set up radial equations, combine energy with $F=ma$ |

> ⚠️ **Exam Tip:** Circular motion in 9231 FM is typically worth **10–14 marks** and is often the longest question on the Further Mechanics paper (frequently Q2 or Q3). The vertical-circle-with-energy question is the most common variant and almost always requires you to **combine** an energy equation with a radial $F=ma$ equation — examiners deliberately test whether you can weld the two ideas together. A horizontal conical-pendulum question appears roughly every other session.

> 📌 **Syllabus note on proof:** You are **not** required to prove $a = r\omega^{2}$ or $a = v^{2}/r$. You must be able to **recall and apply** these results.

---

# 2. Prerequisites

## From AS & A Level Mathematics and Further Mechanics

### 2.1 Resolving Forces

For a force $F$ at angle $\theta$ to the horizontal:

$$F_{x} = F\cos\theta \qquad\text{and}\qquad F_{y} = F\sin\theta$$

Vertical and horizontal components are treated independently.

### 2.2 Newton's Second Law

$$\mathbf{F}_{\text{net}} = m\mathbf{a}$$

In circular motion the **radial** component of $\mathbf{F}_{\text{net}}$ provides the centripetal force. There is no separate "centripetal force" — it is simply the name for the resultant force component towards the centre.

### 2.3 Newton's Third Law & Contact Forces

- **Tension** $T$ in a string acts along the string away from the particle.
- **Normal reaction** $R$ acts perpendicular to the surface, away from it.
- Both can become **zero** — this is the signal that a string goes slack or a particle loses contact.

### 2.4 Conservation of Mechanical Energy (no loss)

When a particle moves under gravity and normal/tension forces that do **no work** (they act perpendicular to the displacement for circular motion on a string or smooth surface):

$$E = \tfrac12 mv^{2} + mgh = \text{constant}$$

measured from a fixed datum. Only $mg$ does work; tension and normal reaction do not.

### 2.5 Hooke's Law (for elastic-string extensions)

For an elastic string of natural length $l_{0}$ and modulus $\lambda$:

$$T = \frac{\lambda x}{l_{0}}$$

where $x$ is the extension. Elastic potential energy:

$$\text{EPE} = \frac{\lambda x^{2}}{2l_{0}}$$

If a problem involves an **elastic** string in circular motion, its length (and hence radius) depends on $T$, so Hooke's law must be coupled with the circular-motion equations. For an **inextensible** (light, inextensible) string, $r$ is fixed.

### 2.6 Radians

Angular speed is always in **radians per second** ($\text{rad s}^{-1}$). One complete revolution:

$$2\pi\ \text{radians} = 360°$$

$$1\ \text{rev s}^{-1} = 2\pi\ \text{rad s}^{-1}$$

> ⚠️ Always work in **radians** for $\omega$. If a question gives revolutions per minute (rpm), convert first.

---

# 3. Angular Speed & Circular Kinematics

## 3.1 Definition of Angular Speed

> **📌 Key Point 3.1 — Angular speed:** For a particle moving in a circle of radius $r$ with centre $O$, the **angular speed** $\omega$ is the rate at which the angle $\angle POQ$ (between a fixed radius and the radius to the particle) increases.
>
> $$\omega = \frac{d\theta}{dt}$$
>
> Units: $\text{rad s}^{-1}$.
>
> For **uniform** circular motion $\omega$ is constant and:
>
> $$\omega = \frac{\theta}{t} = \frac{2\pi}{T} = 2\pi f$$
>
> where $T$ is the **period** (time for one revolution) and $f = 1/T$ is the **frequency** (revolutions per second).

### The Three Related Quantities

| Quantity | Symbol | Units | Relation |
|----------|--------|-------|----------|
| Angular speed | $\omega$ | $\text{rad s}^{-1}$ | $\omega = 2\pi/T = 2\pi f$ |
| Period | $T$ | $\text{s}$ | $T = 2\pi/\omega$ |
| Frequency | $f$ | $\text{Hz}$ ($\text{s}^{-1}$) | $f = \omega/(2\pi)$ |

---

## 3.2 Linear Speed and Angular Speed: $v = r\omega$

> **📌 Key Point 3.2 — Arc length to linear speed:**
>
> $$v = r\,\omega$$
>
> where $v$ is the magnitude of the linear (tangential) velocity, $r$ is the radius, and $\omega$ is the angular speed in $\text{rad s}^{-1}$.

**Why it is true (intuition, not examined):** Arc length $s = r\theta$, so $v = ds/dt = r\,d\theta/dt = r\omega$.

### Step-by-Step Method — Converting Between $v$ and $\omega$

| Step | What To Do |
|------|------------|
| **1** | Identify $r$ (radius) and which of $v$, $\omega$ is given |
| **2** | Convert any rpm or degrees to $\text{rad s}^{-1}$: $\omega = 2\pi \times (\text{rev s}^{-1})$ |
| **3** | Apply $v = r\omega$ (or $\omega = v/r$) |
| **4** | Check units: $v$ in $\text{m s}^{-1}$, $r$ in $\text{m}$, $\omega$ in $\text{rad s}^{-1}$ |

> ### 👀 Watch Out!
> **Rpm trap.** If a question says "300 revolutions per minute", then:
> $$f = \frac{300}{60} = 5\ \text{rev s}^{-1},\qquad \omega = 2\pi f = 10\pi\ \text{rad s}^{-1}$$
> Do **not** write $\omega = 300$ — always convert.
>
> **Radius vs diameter.** Questions sometimes give the diameter. Halve it before using $v=r\omega$ or $a=r\omega^{2}$.

> ### 🎯 What the examiner wants
> One mark for correct conversion to $\text{rad s}^{-1}$; one mark for correct application of $v=r\omega$. Show the conversion explicitly — examiners award a method mark for $2\pi f$ even if the final answer has an arithmetic slip.

---

# 4. Centripetal Acceleration

## 4.1 The Result (No Proof Required)

> **📌 Key Point 4.1 — Centripetal acceleration:** A particle moving in a circle of radius $r$ with angular speed $\omega$ and linear speed $v$ has acceleration **towards the centre** of the circle of magnitude
>
> $$a = r\,\omega^{2} = \frac{v^{2}}{r} = v\,\omega$$
>
> Direction: **always towards the centre** of the circular path. This is true whether the speed is constant (uniform circular motion) or varying — at each instant the radial component of acceleration has this magnitude.

$$a_{\text{towards centre}} = r\omega^{2} = \frac{v^{2}}{r}$$

All three forms are equivalent — choose whichever matches the data you have:

| You know | Use |
|----------|-----|
| $r$ and $\omega$ | $a = r\omega^{2}$ |
| $r$ and $v$ | $a = v^{2}/r$ |
| $v$ and $\omega$ | $a = v\omega$ |

### Consequences for $F = ma$ in the Radial Direction

Resolving **towards the centre**:

$$F_{\text{towards centre}} = m\,a = m\,r\omega^{2} = \frac{mv^{2}}{r}$$

This is **not** a new force — it is the resultant (net) component of the real forces (tension, weight component, normal reaction, friction, …) in the radial direction.

> ### 👀 Watch Out!
> **"Centripetal force" is not a free-body force.** Never draw an extra arrow labelled "centripetal force" on a force diagram. The centripetal requirement is an **equation**, not an additional force:
> $$(\text{sum of force components towards centre}) = \frac{mv^{2}}{r}$$
> Adding a fictitious outward "centrifugal force" is wrong in an inertial frame and loses marks.
>
> **Constant speed ≠ constant velocity.** Even in uniform circular motion the particle accelerates (towards the centre) because velocity is a vector — its direction changes continuously.
>
> **Units check:** $r\omega^{2}$ has units $\text{m}\cdot\text{s}^{-2}$ — correct for acceleration. If your answer has units $\text{m s}^{-1}$ you have computed $v$, not $a$.

> ### 🎯 What the examiner wants
> Correct identification of the centre of the circle; correct radial equation $F_{\text{in}} = mv^{2}/r$ with signs consistent (towards centre positive). One mark is routinely reserved for stating or implying that acceleration is towards the centre. If you resolve in the wrong direction (e.g. away from the centre) you lose the method marks.

---

# 5. Horizontal Circular Motion — Fundamentals

## 5.1 Setting Up the Equations

For motion in a **horizontal** circle (centre at the same height as the particle), gravity acts **perpendicular** to the plane of motion and does not affect the circular dynamics directly. The plane of the circle is horizontal.

General method:

| Step | What To Do |
|------|------------|
| **1** | Identify the centre of the circle and the radius $r$ (this is often $l\sin\theta$ for a conical pendulum, not the string length) |
| **2** | Draw the force diagram: weight $mg$ vertically down, tension/normal/friction as appropriate |
| **3** | **Resolve vertically:** forces in equilibrium ($\sum F_{y} = 0$) because there is no vertical acceleration |
| **4** | **Resolve horizontally towards the centre:** $\sum F_{\text{towards centre}} = mr\omega^{2} = mv^{2}/r$ |
| **5** | Solve the simultaneous equations for unknowns ($T$, $\theta$, $\omega$, $v$, …) |
| **6** | If $r$ depends on $\theta$ (conical pendulum), substitute $r = l\sin\theta$ |

The two equations for a single particle on a string in a horizontal circle are always:

$$\text{Vertical:}\quad T\cos\theta = mg\ \text{ (or similar)}$$

$$\text{Horizontal (radial):}\quad T\sin\theta = mr\omega^{2} = \frac{mv^{2}}{r}$$

where $\theta$ is the angle between the string and the vertical.

---

## 5.2 Worked Mini-Example — Particle on a String, Horizontal Circle

> **Question:** A particle of mass $0.5\text{ kg}$ is whirled in a horizontal circle of radius $0.8\text{ m}$ on a light inextensible string with angular speed $4\text{ rad s}^{-1}$. Find the tension in the string.

**Solution:**

The string is horizontal, so the entire tension provides the centripetal force.

$$T = mr\omega^{2}$$

$$T = 0.5 \times 0.8 \times 4^{2}$$

$$T = 0.5 \times 0.8 \times 16$$

$$T = 6.4\ \text{N} \checkmark$$

Note: In this special case the string itself lies in the plane of the circle. More commonly the string makes an angle with the vertical — that is the conical pendulum (§6).

---

# 6. The Conical Pendulum

## 6.1 Geometry and Definitions

A **conical pendulum** consists of a particle of mass $m$ attached to a fixed point $O$ by a light inextensible string of length $l$, moving in a **horizontal** circle with centre $C$ vertically below $O$. The string sweeps out a cone; it makes a constant angle $\theta$ with the vertical.

```
        O (fixed point)
        |\
        | \  l  (string length)
        |  \
        |   \
        |θ   \  T (tension along string)
        |     \
        C------P  (particle, mass m)
           r = l sin θ   (radius of horizontal circle)
        ─────────────────  horizontal plane
              mg ↓
```

> **📌 Key Point 6.1 — Conical pendulum equations:** Let $\theta$ be the angle between the string and the vertical, $l$ the string length, $r = l\sin\theta$ the radius. Resolving vertically and horizontally towards $C$:
>
> $$T\cos\theta = mg \qquad\text{(vertical equilibrium)}$$
>
> $$T\sin\theta = mr\omega^{2} = \frac{mv^{2}}{r} \qquad\text{(horizontal: towards centre)}$$
>
> Dividing the second by the first eliminates $T$:
>
> $$\tan\theta = \frac{r\omega^{2}}{g} = \frac{v^{2}}{rg}$$
>
> Using $r = l\sin\theta$:
>
> $$\cos\theta = \frac{g}{l\,\omega^{2}} \qquad (\text{provided }\sin\theta\neq 0)$$
>
> and the period:
>
> $$T_{\text{period}} = 2\pi\sqrt{\frac{l\cos\theta}{g}} = 2\pi\sqrt{\frac{h}{g}}$$
>
> where $h = l\cos\theta = OC$ is the vertical depth of the particle below $O$.

$$T\cos\theta = mg,\qquad T\sin\theta = mr\omega^{2},\qquad \cos\theta = \frac{g}{l\omega^{2}}$$

### Step-by-Step Method — Conical Pendulum

| Step | What To Do |
|------|------------|
| **1** | Identify $m$, $l$, and which of $\theta$, $\omega$, $v$, $T$ is given or sought |
| **2** | Write $r = l\sin\theta$ |
| **3** | Write vertical equation: $T\cos\theta = mg$ |
| **4** | Write radial equation: $T\sin\theta = mr\omega^{2}$ (or $mv^{2}/r$) |
| **5** | Eliminate $T$ or $\theta$ as needed: $\tan\theta = r\omega^{2}/g$; $\cos\theta = g/(l\omega^{2})$ |
| **6** | Solve for the required quantity; check $\cos\theta \leq 1$ (otherwise no conical motion is possible — the string would need to be shorter or $\omega$ larger) |

> ### 👀 Watch Out!
> **$r$ is NOT $l$.** The radius of the circle is $r = l\sin\theta$, not the string length $l$. This is the single most common error in conical pendulum questions.
>
> **$\cos\theta = g/(l\omega^{2})$ requires $l\omega^{2} \geq g$.** If $g/(l\omega^{2}) > 1$, no real $\theta$ exists — the particle simply hangs vertically ($\theta = 0$) and does not perform conical motion. Some questions deliberately test this boundary.
>
> **Weight vs mass.** The vertical equation is $T\cos\theta = mg$, not $T\cos\theta = m$. Always include $g$.
>
> **Period formula.** $T_{\text{period}} = 2\pi\sqrt{l\cos\theta/g}$ — the effective length is the vertical depth $h = l\cos\theta$, analogous to a simple pendulum. Do not use $2\pi\sqrt{l/g}$.

> ### 🎯 What the examiner wants
> - Correct $r = l\sin\theta$ stated explicitly (method mark).
> - Both resolving equations written correctly (2 marks).
> - Final answer for $\theta$ or $\omega$ with justification that a solution exists.
> - If asked for tension, show $T = mg/\cos\theta$.

---

## 6.2 Alternative Conical Configurations

The same two-equation method applies if:

- The particle slides inside a **smooth conical surface** (replace $T$ with normal reaction $R$, still at angle $\theta$ to the vertical).
- The particle is on a **smooth horizontal table** with a string through a hole (tension provides the centripetal force directly; hanging mass provides $T = Mg$).
- Two particles are connected through a hole or over a pulley — equate tensions and write separate radial/vertical equations.

---

# 7. Banked Tracks & Other Horizontal Circles

## 7.1 Vehicle on a Banked Track (Smooth)

A car or particle moves in a horizontal circle of radius $r$ on a track banked at angle $\alpha$ to the horizontal. For a **smooth** track the only contact force is the normal reaction $R$ perpendicular to the surface.

> **📌 Key Point 7.1 — Banked track (no friction), horizontal circle:**
>
> Resolving vertically (equilibrium) and horizontally towards centre:
>
> $$R\sin\alpha = \frac{mv^{2}}{r} \qquad\text{(towards centre)}$$
>
> $$R\cos\alpha = mg \qquad\text{(vertical equilibrium)}$$
>
> Dividing:
>
> $$\tan\alpha = \frac{v^{2}}{rg}\qquad\Longleftrightarrow\qquad v^{2} = rg\tan\alpha$$
>
> This $v$ is the **design speed** — the speed at which no friction is needed. If friction is present, a range of speeds is possible (see §7.2).

$$v_{\text{design}}^{2} = rg\tan\alpha$$

If the vehicle moves **faster** than $v_{\text{design}}$, it tends to slide **up** the bank; friction acts **down** the slope. If **slower**, it tends to slide **down**; friction acts **up** the slope.

### 7.2 Banked Track with Friction ($\mu$)

With friction $F \leq \mu R$, there is a **range** of speeds for which the vehicle does not slip.

- **Maximum speed** $v_{\max}$ (on the point of sliding **up**): friction acts **down** the bank.

$$R\cos\alpha - F\sin\alpha = mg$$

$$R\sin\alpha + F\cos\alpha = \frac{mv_{\max}^{2}}{r}$$

with $F = \mu R$ at limiting friction.

- **Minimum speed** $v_{\min}$ (on the point of sliding **down**): friction acts **up** the bank.

$$R\cos\alpha + F\sin\alpha = mg$$

$$R\sin\alpha - F\cos\alpha = \frac{mv_{\min}^{2}}{r}$$

with $F = \mu R$.

> **📌 Key Point 7.2 — Speed range on a rough banked track:**
>
> $$v_{\max}^{2} = rg\,\frac{\tan\alpha + \mu}{1 - \mu\tan\alpha},\qquad v_{\min}^{2} = rg\,\frac{\tan\alpha - \mu}{1 + \mu\tan\alpha}$$
>
> (provided $\mu < \cot\alpha$ for $v_{\max}$ to be finite; if $\tan\alpha \leq \mu$ then $v_{\min} = 0$ — the vehicle can remain at rest without sliding down).

### 7.3 Particle on a String Through a Hole (Horizontal Table)

A particle $m$ on a smooth horizontal table is attached by a string passing through a hole to a hanging mass $M$. For circular motion of $m$ at radius $r$:

$$T = \frac{mv^{2}}{r} = mr\omega^{2}$$

$$T = Mg \qquad\text{(equilibrium of hanging mass)}$$

Hence:

$$Mg = \frac{mv^{2}}{r}$$

This is a very common exam set-up. If the hanging mass is replaced by a hand pulling the string, $T$ is simply the pulling force.

### Step-by-Step Method — Any Horizontal Circle

| Step | What To Do |
|------|------------|
| **1** | Locate the centre and find $r$ in terms of given lengths/angles |
| **2** | Draw all forces; identify which have a component towards the centre |
| **3** | Resolve perpendicular to the plane of motion (usually vertical): equilibrium |
| **4** | Resolve towards the centre: $= mv^{2}/r$ |
| **5** | Add friction equations $F \leq \mu R$ if the surface is rough |
| **6** | Solve simultaneously |

> ### 👀 Watch Out!
> **Banked track $R$ is not $mg$.** $R\cos\alpha = mg$ so $R = mg/\cos\alpha > mg$. Students who write $R = mg$ lose both marks.
>
> **Friction direction.** Decide correctly: faster than design speed → friction down the slope; slower → friction up the slope. Draw the friction arrow before writing equations and state your assumption.
>
> **Conical pendulum vs banked track.** In the conical pendulum, $T$ is along the string at angle $\theta$ to the vertical. On a banked track, $R$ is perpendicular to the surface at angle $\alpha$ to the vertical. The equations look similar but the physical meaning of the angle differs — read the question carefully.

---

# 8. Vertical Circular Motion — Energy Conservation

## 8.1 Why Energy?

In **vertical** circular motion the speed is **not** constant — gravity does work as the particle rises and falls. The motion is **not uniform**. To find the speed at any point we use **conservation of mechanical energy** (the syllabus specifies "without loss of energy" — no friction, no air resistance, smooth surface or light string).

> **📌 Key Point 8.1 — Conservation of mechanical energy (vertical circle, no loss):**
>
> Choose a datum for gravitational potential energy (GPE). Then at any two points $A$ and $B$ on the path:
>
> $$\tfrac12 mv_{A}^{2} + mgh_{A} = \tfrac12 mv_{B}^{2} + mgh_{B} = E\ (\text{constant})$$
>
> Equivalently, between two points separated by vertical height $\Delta h$ (positive upward):
>
> $$\tfrac12 mv^{2} - \tfrac12 mu^{2} = -mg\,\Delta h$$
>
> or
>
> $$v^{2} = u^{2} - 2g\,\Delta h$$
>
> where $u$ is the speed at the lower point and $\Delta h$ is the height gained.

$$v^{2} = u^{2} - 2g\,\Delta h \qquad\text{(energy conservation, no loss)}$$

### Choosing the Datum

It does not matter where you put $h = 0$, but you must be **consistent**. Two common choices:

| Datum | $h$ at lowest point | $h$ at height $y$ above lowest point |
|-------|---------------------|--------------------------------------|
| Lowest point | $0$ | $y$ |
| Centre of circle | $-r$ | $y - r$ |
| Top of circle | $-2r$ | $y - 2r$ |

The **lowest-point datum** is usually simplest:

$$h = r(1 - \cos\theta) \quad\text{measured from the bottom}$$

where $\theta$ is the angle from the downward vertical (see diagram below).

### 8.2 Geometry — Height in Terms of Angle

For a particle on a string of length $r$ (or a bead on a circular hoop/wire of radius $r$):

```
              top
               ●
              / \
             /   \
            /     \    h = r(1 - cos θ) from bottom
           /   O   \   (θ measured from downward vertical)
          /    |θ   \
         /     |     \
        ●------+------●  θ = 90° (horizontal level with centre)
        |      |      |
        |      |      |
         \     |     /
          \    |    /     θ = 180° at top
           \   ●   /      h = 2r
            \  ↑  /
             bottom (datum, h = 0)
```

If $\theta$ is the angle between the string (or radius) and the **downward** vertical:

$$h = r(1 - \cos\theta)$$

If $\phi$ is the angle from the **upward** vertical:

$$h = r(1 + \cos\phi)$$

If you measure from the **centre** ($h_{c}=0$ at centre):

$$h_{c} = -r\cos\theta$$

Any form is correct — just be consistent with your energy equation. The key relation is always:

$$\Delta h = r(1 - \cos\theta)\ \text{above the lowest point}$$

> **📌 Key Point 8.2 — Speed at angle $\theta$ from the downward vertical (lowest-point datum):**
>
> If the speed at the bottom is $u$, then at angle $\theta$ from the downward vertical:
>
> $$v^{2} = u^{2} - 2gr(1 - \cos\theta)$$
>
> At the **top** ($\theta = 180°$, $\cos\theta = -1$):
>
> $$v_{\text{top}}^{2} = u^{2} - 4gr$$
>
> At the **horizontal level** ($\theta = 90°$, $\cos\theta = 0$):
>
> $$v_{\text{horizontal}}^{2} = u^{2} - 2gr$$

### Step-by-Step Method — Energy in the Vertical Circle

| Step | What To Do |
|------|------------|
| **1** | Choose a datum (lowest point is simplest: $h=0$ there) |
| **2** | Express $h$ at the point of interest in terms of $r$ and $\theta$ |
| **3** | Write $\tfrac12 mv^{2} + mgh = \tfrac12 mu^{2} + mgh_{0}$ and solve for $v^{2}$ |
| **4** | Keep $v^{2}$ (not $v$) — the radial equation needs $v^{2}/r$ |
| **5** | Combine with the radial $F=ma$ equation (§9) to find $T$ or $R$ |

> ### 👀 Watch Out!
> **$v^{2}$ can become negative in your algebra** — this means the particle cannot reach that height with the given initial speed. If you get $v^{2} < 0$, the particle would have stopped and fallen back (or the string would have gone slack) before reaching that point. Do not take the square root of a negative number — instead interpret it as "this point is not reached".
>
> **Height is vertical height, not arc length.** $\Delta h = r(1-\cos\theta)$, not $r\theta$. Confusing the two is a common error.
>
> **Datum consistency.** If you set $h=0$ at the bottom for one term, every $h$ in the equation must use the same datum. Mixing datums gives wrong signs.
>
> **$mgh$ sign.** GPE increases upward. If you put the datum at the top, $h$ at the bottom is negative — handle signs carefully. Lowest-point datum avoids this confusion.

---

# 9. Tension & Normal Reaction in the Vertical Circle

## 9.1 The Radial Equation

At any point in a vertical circle, resolving **towards the centre** of the circle gives an $F=ma$ equation. The forces with radial components are typically tension/normal reaction and the component of weight.

> **📌 Key Point 9.1 — Radial equation (towards centre):**
>
> For a particle of mass $m$ at angle $\theta$ from the downward vertical, with speed $v$:
>
> - **On a string** (tension $T$ towards centre, weight component):
>
> $$T - mg\cos\theta = \frac{mv^{2}}{r}$$
>
> so
>
> $$T = \frac{mv^{2}}{r} + mg\cos\theta$$
>
> - **On the inside of a smooth circular hoop/sphere** (normal reaction $R$ towards centre):
>
> $$R - mg\cos\theta = \frac{mv^{2}}{r}$$
>
> so
>
> $$R = \frac{mv^{2}}{r} + mg\cos\theta$$
>
> - **On the outside of a smooth sphere** (normal reaction $R$ away from centre, weight component towards centre):
>
> $$mg\cos\theta - R = \frac{mv^{2}}{r}$$
>
> so
>
> $$R = mg\cos\theta - \frac{mv^{2}}{r}$$
>
> In each case $\theta$ is measured from the **downward** vertical through the centre. At the **top** ($\theta = 180°$, $\cos\theta = -1$), these become $T + mg = mv^{2}/r$ or $R + mg = mv^{2}/r$ etc. — check signs carefully.

The sign convention matters. A reliable approach:

| Position | $\theta$ from downward vertical | $\cos\theta$ | String: $T - mg\cos\theta = mv^{2}/r$ | Outside sphere: $mg\cos\theta - R = mv^{2}/r$ |
|----------|-------------------------------|--------------|----------------------------------------|-----------------------------------------------|
| Bottom | $0°$ | $+1$ | $T - mg = mv^{2}/r$ | $mg - R = mv^{2}/r$ |
| Horizontal | $90°$ | $0$ | $T = mv^{2}/r$ | $-R = mv^{2}/r$ — (use correct geometry) |
| Top | $180°$ | $-1$ | $T + mg = mv^{2}/r$ | $-mg - R = mv^{2}/r$ — (see below) |

Because sign errors are so common, many textbooks instead measure $\theta$ from the **upward** vertical or use a dedicated diagram. The safest method in the exam is:

### ✅ Foolproof Method — Always Resolve Towards the Centre

1. Draw the particle, mark the centre $O$, draw an arrow from the particle **towards $O$** — this is the positive radial direction.
2. For each force, find its component **along this arrow** (positive if towards $O$, negative if away).
3. Set the sum equal to $mv^{2}/r$.

This avoids memorising sign conventions — just project each force onto the towards-centre direction.

**Example — Particle on a string at angle $\theta$ below the horizontal** (or any position): draw $T$ towards $O$ (positive), weight component: if $O$ is above the particle, the weight component towards $O$ is $-mg\cos(\text{angle between weight and }OP)$ — work it out from the diagram each time.

### 9.2 Combining Energy and Radial Equations

The standard technique for vertical circles:

| Step | What To Do |
|------|------------|
| **1** | Use **energy** to express $v^{2}$ at the point of interest in terms of the initial speed $u$ and height $h$ |
| **2** | Use **radial $F=ma$** to express $T$ (or $R$) in terms of $v^{2}$ and the weight component |
| **3** | Substitute $v^{2}$ from step 1 into step 2 to get $T$ (or $R$) purely in terms of $u$, $r$, $g$, $\theta$ |
| **4** | Set $T = 0$ (or $R = 0$) to find critical conditions (§10) |

> **📌 Key Point 9.2 — Tension at a general point (string, downward-vertical angle $\theta$):**
>
> Combining $v^{2} = u^{2} - 2gr(1-\cos\theta)$ with $T = mv^{2}/r + mg\cos\theta$:
>
> $$T = \frac{m}{r}\left[u^{2} - 2gr(1-\cos\theta)\right] + mg\cos\theta$$
>
> $$T = \frac{mu^{2}}{r} - 2mg(1-\cos\theta) + mg\cos\theta$$
>
> $$T = \frac{mu^{2}}{r} - 2mg + 3mg\cos\theta$$
>
> This compact form is extremely useful — it gives $T$ directly from $u$ without first finding $v$.

$$T = \frac{mu^{2}}{r} - 2mg + 3mg\cos\theta \qquad\text{(string, }\theta\text{ from downward vertical)}$$

Special cases:

$$T_{\text{bottom}}\ (\theta=0) = \frac{mu^{2}}{r} + mg$$

$$T_{\text{top}}\ (\theta=180°) = \frac{mu^{2}}{r} - 5mg$$

$$T_{\text{horizontal}}\ (\theta=90°) = \frac{mu^{2}}{r} - 2mg$$

For a **bead on a smooth circular wire** (inside), replace $T$ with $R$ — same formulae.

> ### 👀 Watch Out!
> **$T$ can be negative in your algebra** — a string cannot push. $T < 0$ means the string would have gone slack before reaching that point; the circular motion assumption has broken down. For a rod (which can push), negative $T$ means compression — the rod is in compression rather than tension, but circular motion continues.
>
> **Normal reaction $R \geq 0$ for contact.** If $R$ becomes zero, contact is lost. For a particle on the **inside** of a hoop, $R$ is towards the centre; for a particle on the **outside** of a sphere, $R$ is away from the centre — the equation changes sign. Always draw the diagram.
>
> **Keep $v^{2}$, not $v$.** The radial equation needs $v^{2}/r$. Computing $v$ and then squaring introduces unnecessary square roots and rounding errors. Work with $v^{2}$ throughout.

> ### 🎯 What the examiner wants
> - Energy equation written correctly with consistent datum (1 mark).
> - Radial equation with correct signs — resolving towards the centre (1–2 marks).
> - Combining to find $T$ or $R$ as a function of position (1 mark).
> - Correct handling of the $T=0$ or $R=0$ condition when asked.

---

# 10. Critical Speeds, String Going Slack & Leaving the Circle

## 10.1 When Does the String Go Slack?

A string can only exert a **pull** ($T \geq 0$). The instant the required tension would become negative, the string goes **slack** and the particle ceases to move in a circle — it becomes a projectile.

> **📌 Key Point 10.1 — String slack condition:**
>
> The string goes slack when:
>
> $$T = 0$$
>
> At that instant the only radial force is the component of weight, so:
>
> $$-mg\cos\theta = \frac{mv^{2}}{r}\quad\text{or}\quad mg|\cos\theta| = \frac{mv^{2}}{r}$$
>
> (signs depend on position — use the towards-centre method).
>
> After the string goes slack, the particle follows a **parabolic projectile** trajectory under gravity until (possibly) the string becomes taut again.

### Finding Where the String Goes Slack

Set $T = 0$ in the combined energy + radial equation:

$$0 = \frac{mu^{2}}{r} - 2mg + 3mg\cos\theta$$

$$\cos\theta = \frac{2}{3} - \frac{u^{2}}{3gr}$$

This gives the angle $\theta_{\text{slack}}$ at which $T$ first reaches zero. If $|\cos\theta_{\text{slack}}| > 1$, the string **never** goes slack during that motion — tension remains positive throughout.

## 10.2 When Does a Particle Leave a Surface?

Similarly, contact is maintained only while $R \geq 0$. The particle **leaves the surface** when:

$$R = 0$$

> **📌 Key Point 10.2 — Leaving the surface (outside of sphere):**
>
> For a particle sliding on the **outside** of a smooth sphere of radius $r$, starting from the top with speed $u$:
>
> Energy: $v^{2} = u^{2} + 2gr(1 - \cos\theta)$ (gaining speed as it descends — careful with height signs; here $\theta$ from upward vertical, $h$ lost $= r(1-\cos\theta)$)
>
> Radial (towards centre, i.e. into the sphere): $mg\cos\theta - R = mv^{2}/r$
>
> Setting $R = 0$:
>
> $$mg\cos\theta = \frac{mv^{2}}{r} = \frac{m}{r}\left[u^{2} + 2gr(1-\cos\theta)\right]$$
>
> $$g\cos\theta = \frac{u^{2}}{r} + 2g - 2g\cos\theta$$
>
> $$3g\cos\theta = \frac{u^{2}}{r} + 2g$$
>
> $$\cos\theta = \frac{2}{3} + \frac{u^{2}}{3gr}$$
>
> For $u = 0$ (released from rest at the top): $\cos\theta = 2/3$, so $\theta \approx 48.2°$ from the top.

$$R = 0 \implies \cos\theta = \frac{2}{3} + \frac{u^{2}}{3gr}\qquad\text{(outside sphere, }\theta\text{ from top)}$$

## 10.3 Critical Speed at the Top

> **📌 Key Point 10.3 — Minimum speed at the top to maintain circular motion:**
>
> For a particle on a **string** to just maintain contact at the top of the circle (tension just zero):
>
> $$T = 0 \implies mg = \frac{mv_{\text{top}}^{2}}{r}\quad\text{(at top, weight alone provides centripetal force)}$$
>
> $$v_{\text{top, crit}} = \sqrt{gr}$$
>
> This is the **critical speed** at the top. If $v_{\text{top}} < \sqrt{gr}$, the string will have gone slack before reaching the top.

$$v_{\text{top, crit}} = \sqrt{gr}\qquad\text{(string, tension just zero at top)}$$

For a **rod** (which can support compression) or a bead on a **circular wire/hoop**, the particle can be at the top with $v_{\text{top}} = 0$ and still remain on the circle — the rod/wire provides the necessary inward force (or outward normal reaction).

| Constraint | $v_{\text{top}}$ needed for complete circle | What happens if slower |
|------------|---------------------------------------------|------------------------|
| **String** (can only pull) | $v_{\text{top}} \geq \sqrt{gr}$ | String goes slack before top |
| **Rod** (can push or pull) | $v_{\text{top}} \geq 0$ (any speed, even zero at top) | Still completes circle (rod in compression) |
| **Bead on hoop** (inside) | $v_{\text{top}} \geq 0$ | Bead stays on hoop (normal reaction can be outward) |
| **Particle outside sphere** | N/A — always leaves before top if going around outside | Leaves when $R=0$ |

### Relating Critical Speed at Top to Speed at Bottom

Using energy ($v_{\text{top}}^{2} = u^{2} - 4gr$):

$$v_{\text{top}} \geq \sqrt{gr} \implies u^{2} - 4gr \geq gr$$

$$u^{2} \geq 5gr$$

$$u_{\text{crit}} = \sqrt{5gr}\qquad\text{(minimum speed at bottom for complete circle on a string)}$$

> **📌 Key Point 10.4 — Complete circle on a string (released from bottom):**
>
> $$u \geq \sqrt{5gr}\quad\text{at the bottom} \iff v_{\text{top}} \geq \sqrt{gr}\quad\text{at the top}$$

$$u_{\text{bottom}} \geq \sqrt{5gr}\quad\text{for a complete vertical circle on a string}$$

For a **rod** or **bead on a wire**, the condition is simply $u \geq \sqrt{4gr} = 2\sqrt{gr}$ (enough energy to reach the top, even with $v_{\text{top}} = 0$).

> ### 👀 Watch Out!
> **$\sqrt{gr}$ is the speed at the TOP, $\sqrt{5gr}$ is the speed at the BOTTOM.** Mixing them up is extremely common. Always state which point your critical speed refers to.
>
> **String vs rod.** If the question says "light rod" or "bead on a smooth circular wire", the constraint $T \geq 0$ does not apply — the rod can push. The condition for a complete circle is weaker ($u \geq 2\sqrt{gr}$). Read whether it is a string or a rod.
>
> **Leaving the circle ≠ string going slack (outside sphere).** For a particle on the outside of a sphere, $R = 0$ means it leaves the surface and becomes a projectile. For a particle on a string inside a circle, $T = 0$ means the string goes slack. The mathematics is similar but the physical picture differs — state which one applies.
>
> **After leaving/slack, projectile motion.** Some harder questions ask for the subsequent trajectory. After $T=0$ or $R=0$, resolve the velocity into horizontal and vertical components at that instant and use projectile equations. The circular motion phase is over.

---

# 11. Conditions for Complete Circles

## 11.1 Summary Table

| Scenario | Completes circle if | Maximum height if not |
|----------|-------------------|-----------------------|
| String, projected from bottom with speed $u$ | $u \geq \sqrt{5gr}$ | String goes slack at $\cos\theta = \tfrac23 - u^{2}/(3gr)$; or if $u^{2} < 2gr$, particle oscillates without slack |
| String, released from height | Enough energy that $v_{\text{top}} \geq \sqrt{gr}$ | As above |
| Rod / bead on wire, projected from bottom | $u \geq 2\sqrt{gr}$ (reach top) | Oscillates as a pendulum if $u < 2\sqrt{gr}$ |
| Particle inside smooth sphere/hoop | Same as rod ($R$ can become negative — meaning contact on opposite side — but for inside, $R \geq 0$ is still needed) | Depends on energy |
| Particle outside sphere | Never completes a full circle — always leaves at $R=0$ | Leaves at $\cos\theta = 2/3 + u^{2}/(3gr)$ |

## 11.2 Oscillations vs Slack vs Complete Circles (String)

For a particle on a string projected from the bottom with speed $u$:

- **$0 < u < \sqrt{2gr}$:** Not enough energy to reach the horizontal. Particle **oscillates** (swings) below the horizontal level. String never goes slack ($T > 0$ throughout).
- **$\sqrt{2gr} < u < \sqrt{5gr}$:** Enough energy to pass the horizontal but not enough to maintain tension to the top. String **goes slack** at some angle $\theta$ above the horizontal ($\cos\theta$ between 0 and $-1$). After that, projectile motion.
- **$u = \sqrt{5gr}$:** Just enough to reach the top with $T = 0$ at the top. Barely completes the circle.
- **$u > \sqrt{5gr}$:** **Completes the circle** with $T > 0$ everywhere.

> **📌 Key Point 11.1 — Regime boundaries (string from bottom):**
>
> $$u < \sqrt{2gr}:\ \text{oscillates (pendulum)}$$
>
> $$\sqrt{2gr} < u < \sqrt{5gr}:\ \text{string goes slack above horizontal}$$
>
> $$u \geq \sqrt{5gr}:\ \text{complete circle}$$

For a **rod**, the middle regime does not involve slack — instead the particle simply rises to a maximum angle and oscillates back if $u < 2\sqrt{gr}$, or completes the circle if $u \geq 2\sqrt{gr}$.

> ### 🎯 What the examiner wants
> When asked "does the particle complete the circle?" or "find the condition for circular motion to be maintained", the examiner expects:
> 1. Energy equation to relate $v_{\text{top}}$ to initial conditions.
> 2. Radial equation at the top with $T \geq 0$ (or $R \geq 0$).
> 3. Combining to get the inequality on $u$ (or $\omega$, or $h$).
> 4. A clear conclusion: "Since $u >/< \sqrt{5gr}$, the particle does/does not complete the circle."

---

# 12. Hooke's Law & Elastic Strings in Circular Motion

## 12.1 When the String is Elastic

If the string is **elastic** (obeys Hooke's law), its **length is not fixed** — it stretches under tension, so the radius of the circle depends on the tension, which itself depends on the motion.

> **📌 Key Point 12.1 — Elastic string in circular motion:**
>
> For an elastic string of natural length $l_{0}$ and modulus $\lambda$, with extension $x$:
>
> $$T = \frac{\lambda x}{l_{0}},\qquad l = l_{0} + x = \text{actual length} = r\ (\text{if horizontal circle})$$
>
> Energy now includes **elastic potential energy**:
>
> $$\text{EPE} = \frac{\lambda x^{2}}{2l_{0}}$$
>
> Total mechanical energy (vertical circle with elastic string):
>
> $$E = \tfrac12 mv^{2} + mgh + \frac{\lambda x^{2}}{2l_{0}} = \text{constant}$$

### Example Configurations

**Horizontal circle with elastic string:** Particle whirled horizontally, string elastic. The radius $r = l_{0} + x$ and $T = \lambda x/l_{0} = mv^{2}/r$. Solve simultaneously:

$$\frac{\lambda x}{l_{0}} = \frac{mv^{2}}{l_{0}+x}$$

**Conical pendulum with elastic string:** Similar, but $r = l\sin\theta$ where $l = l_{0}+x$, and $T\cos\theta = mg$, $T\sin\theta = mr\omega^{2}$.

**Vertical circle with elastic string:** Most complex — $r$ varies with $T$ which varies with position. Requires simultaneous energy (including EPE) and Hooke's law.

### Step-by-Step Method — Elastic String

| Step | What To Do |
|------|------------|
| **1** | Write Hooke's law: $T = \lambda x/l_{0}$; actual length $l = l_{0}+x$ |
| **2** | Write circular motion equations with $r = l$ (or $l\sin\theta$ for conical) |
| **3** | If vertical motion, include EPE in the energy equation |
| **4** | Solve the coupled equations for $x$ and $v$ (or $\omega$) |

> ### 👀 Watch Out!
> **Natural length vs actual length.** $l_{0}$ is the unstretched length. The radius is the **stretched** length $l = l_{0}+x$. Using $l_{0}$ as the radius is wrong.
>
> **EPE is always positive.** $\lambda x^{2}/(2l_{0})$ — it is quadratic in $x$. Do not confuse it with GPE which can be negative depending on datum.
>
> **Check $x > 0$.** If your solution gives $x < 0$, the string would be slack (in compression) — but an elastic string cannot support compression. The physical solution is that the string is slack and $T = 0$.

---

# 13. Worked Examples — Complete Solutions

## Example 1 — Horizontal Circle: Conical Pendulum (Easy)

> **Question:** A particle of mass $0.3\text{ kg}$ is attached to a light inextensible string of length $1.2\text{ m}$. The particle moves in a horizontal circle as a conical pendulum with the string making an angle of $30°$ with the vertical. Find (a) the tension in the string, (b) the angular speed, and (c) the period of the motion. Take $g = 9.8\text{ m s}^{-2}$.

**Solution:**

**(a) Tension:**

Resolve vertically — no vertical acceleration:

$$T\cos 30° = mg$$

$$T = \frac{mg}{\cos 30°}$$

$$T = \frac{0.3 \times 9.8}{\cos 30°}$$

$$T = \frac{2.94}{\sqrt{3}/2}$$

$$T = \frac{5.88}{\sqrt{3}}$$

$$T = 3.40\ \text{N (3 s.f.)} \checkmark$$

**(b) Angular speed:**

Radius of the circle:

$$r = l\sin 30°$$

$$r = 1.2 \times 0.5$$

$$r = 0.6\ \text{m}$$

Resolve horizontally towards the centre:

$$T\sin 30° = mr\omega^{2}$$

$$\omega^{2} = \frac{T\sin 30°}{mr}$$

$$\omega^{2} = \frac{3.40 \times 0.5}{0.3 \times 0.6}$$

$$\omega^{2} = \frac{1.70}{0.18}$$

$$\omega^{2} = 9.44$$

$$\omega = \sqrt{9.44}$$

$$\omega = 3.07\ \text{rad s}^{-1}\ (3\text{ s.f.}) \checkmark$$

*Alternative using* $\cos\theta = g/(l\omega^{2})$:

$$\omega^{2} = \frac{g}{l\cos\theta}$$

$$\omega^{2} = \frac{9.8}{1.2 \times \cos 30°}$$

$$\omega^{2} = \frac{9.8}{1.2 \times 0.8660}$$

$$\omega^{2} = \frac{9.8}{1.0392}$$

$$\omega^{2} = 9.43$$

$$\omega = 3.07\ \text{rad s}^{-1} \checkmark$$

**(c) Period:**

$$T_{\text{period}} = \frac{2\pi}{\omega}$$

$$T_{\text{period}} = \frac{2\pi}{3.07}$$

$$T_{\text{period}} = 2.05\ \text{s (3 s.f.)} \checkmark$$

> **Check:** $T_{\text{period}} = 2\pi\sqrt{l\cos\theta/g} = 2\pi\sqrt{1.2\cos30°/9.8} = 2\pi\sqrt{1.039/9.8} = 2\pi(0.326) = 2.05\text{ s}$ — consistent. ✓

---

## Example 2 — Horizontal Circle: Particle on a Banked Track (Easy–Medium)

> **Question:** A car of mass $1200\text{ kg}$ travels at $20\text{ m s}^{-1}$ around a bend of radius $80\text{ m}$ banked at $15°$ to the horizontal. The track is smooth. (a) Find the normal reaction. (b) Find the design speed for this bend (the speed at which no friction is required). Take $g = 9.8\text{ m s}^{-2}$.

**Solution:**

**(a) Normal reaction at $20\text{ m s}^{-1}$:**

Forces: weight $mg$ down, normal reaction $R$ perpendicular to track (at $15°$ to vertical).

Resolve vertically (no vertical acceleration):

$$R\cos 15° = mg$$

$$R = \frac{mg}{\cos 15°}$$

$$R = \frac{1200 \times 9.8}{\cos 15°}$$

$$R = \frac{11760}{0.9659}$$

$$R = 12170\ \text{N}$$

$$R \approx 12.2\ \text{kN} \checkmark$$

*Note:* For a smooth banked track, $R$ is determined solely by vertical equilibrium — it does not depend on $v$. The horizontal equation then determines whether $v$ is the design speed.

Check horizontal equation:

$$R\sin 15° = \frac{mv^{2}}{r}$$

$$\text{LHS} = 12170 \times \sin 15°$$

$$\text{LHS} = 12170 \times 0.2588$$

$$\text{LHS} = 3150\ \text{N}$$

$$\text{RHS} = \frac{1200 \times 400}{80}$$

$$\text{RHS} = 6000\ \text{N}$$

Since $\text{RHS} > \text{LHS}$, $20\text{ m s}^{-1}$ is **faster** than the design speed — friction would be needed to prevent sliding up (but the track is smooth, so the car would tend to slide outward/upward).

**(b) Design speed:**

At the design speed, both equations hold simultaneously with no friction:

$$\tan\alpha = \frac{v^{2}}{rg}$$

$$v^{2} = rg\tan\alpha$$

$$v^{2} = 80 \times 9.8 \times \tan 15°$$

$$v^{2} = 784 \times 0.2679$$

$$v^{2} = 210.1$$

$$v = \sqrt{210.1}$$

$$v = 14.5\ \text{m s}^{-1}\ (3\text{ s.f.}) \checkmark$$

> **Interpretation:** At $14.5\text{ m s}^{-1}$ no friction is needed. At $20\text{ m s}^{-1}$ (faster), the car would need friction acting **down** the slope to provide extra inward force — or it would drift outward.

---

## Example 3 — Vertical Circle: Tension at Top and Bottom (Medium)

> **Question:** A particle of mass $0.4\text{ kg}$ is attached to one end of a light inextensible string of length $0.8\text{ m}$. The other end is fixed. The particle is projected horizontally from its equilibrium position (hanging vertically) with speed $6\text{ m s}^{-1}$ and subsequently moves in a vertical circle. Find (a) the speed at the top of the circle, (b) the tension at the top, and (c) the tension at the bottom just after projection. Take $g = 9.8\text{ m s}^{-2}$.

**Solution:**

**(a) Speed at the top:**

Use conservation of energy. Datum at the bottom ($h=0$ there).

$$E_{\text{bottom}} = \tfrac12 mu^{2} + mgh_{\text{bottom}}$$

$$E_{\text{bottom}} = \tfrac12 \times 0.4 \times 36 + 0$$

$$E_{\text{bottom}} = 7.2\ \text{J}$$

At the top, height $h = 2r = 1.6\text{ m}$:

$$E_{\text{top}} = \tfrac12 mv_{\text{top}}^{2} + mg(2r)$$

By conservation $E_{\text{top}} = E_{\text{bottom}}$:

$$\tfrac12 \times 0.4 \times v_{\text{top}}^{2} + 0.4 \times 9.8 \times 1.6 = 7.2$$

$$0.2\,v_{\text{top}}^{2} + 6.272 = 7.2$$

$$0.2\,v_{\text{top}}^{2} = 0.928$$

$$v_{\text{top}}^{2} = 4.64$$

$$v_{\text{top}} = \sqrt{4.64}$$

$$v_{\text{top}} = 2.15\ \text{m s}^{-1}\ (3\text{ s.f.}) \checkmark$$

*Check:* $v_{\text{top}}^{2} = u^{2} - 4gr = 36 - 4(9.8)(0.8) = 36 - 31.36 = 4.64$ ✓

**(b) Tension at the top:**

At the top, both tension and weight act **towards the centre** (downward). Resolve towards centre:

$$T_{\text{top}} + mg = \frac{mv_{\text{top}}^{2}}{r}$$

$$T_{\text{top}} = \frac{mv_{\text{top}}^{2}}{r} - mg$$

$$T_{\text{top}} = \frac{0.4 \times 4.64}{0.8} - 0.4 \times 9.8$$

$$T_{\text{top}} = \frac{1.856}{0.8} - 3.92$$

$$T_{\text{top}} = 2.32 - 3.92$$

$$T_{\text{top}} = -1.60\ \text{N}$$

Since $T_{\text{top}} < 0$, the string **cannot** remain taut at the top with this projection speed! The string would have gone slack before reaching the top. The assumption of circular motion to the top is **invalid**.

> ### 👀 Watch Out — Negative tension!
> We found $T_{\text{top}} = -1.60\text{ N}$, which is physically impossible for a string. This tells us the particle **does not reach the top** while still on the string. It goes slack at some lower point. See Example 5 for how to find where.
>
> For this question as stated, the correct answer is: the particle does not complete the circle. If the question had asked "find the tension at the top **assuming** the string remains taut", the answer $-1.60\text{ N}$ shows the assumption fails.

*For comparison, if $u = 7\text{ m s}^{-1}$:*

$$v_{\text{top}}^{2} = 49 - 31.36 = 17.64$$

$$T_{\text{top}} = \frac{0.4 \times 17.64}{0.8} - 3.92$$

$$T_{\text{top}} = 8.82 - 3.92$$

$$T_{\text{top}} = 4.90\ \text{N} > 0 \checkmark\ \text{(completes circle)}$$

*Critical speed check:* $u_{\text{crit}} = \sqrt{5gr} = \sqrt{5 \times 9.8 \times 0:8} = \sqrt{39.2} = 6.26\text{ m s}^{-1}$. Since $6 < 6.26$, we confirm the particle does not complete the circle. ✓

**(c) Tension at the bottom (just after projection):**

At the bottom, tension acts **up** (towards centre) and weight acts **down** (away from centre). Resolve towards centre (upward):

$$T_{\text{bottom}} - mg = \frac{mu^{2}}{r}$$

$$T_{\text{bottom}} = \frac{mu^{2}}{r} + mg$$

$$T_{\text{bottom}} = \frac{0.4 \times 36}{0.8} + 3.92$$

$$T_{\text{bottom}} = 18.0 + 3.92$$

$$T_{\text{bottom}} = 21.9\ \text{N (3 s.f.)} \checkmark$$

---

## Example 4 — Vertical Circle: Bead on a Smooth Circular Wire (Medium)

> **Question:** A small bead of mass $0.2\text{ kg}$ is threaded on a smooth circular wire of radius $0.5\text{ m}$ fixed in a vertical plane. The bead is projected from the lowest point with speed $5\text{ m s}^{-1}$ along the wire. Find (a) the speed when the bead is at the same height as the centre, and (b) the normal reaction at that point. Take $g = 9.8\text{ m s}^{-2}$.

**Solution:**

**(a) Speed at centre height:**

Datum at the bottom. Height at centre level: $h = r = 0.5\text{ m}$.

Energy conservation:

$$\tfrac12 mv_{c}^{2} + mgh_{c} = \tfrac12 mu^{2}$$

$$\tfrac12 \times 0.2 \times v_{c}^{2} + 0.2 \times 9.8 \times 0.5 = \tfrac12 \times 0.2 \times 25$$

$$0.1\,v_{c}^{2} + 0.98 = 2.5$$

$$0.1\,v_{c}^{2} = 1.52$$

$$v_{c}^{2} = 15.2$$

$$v_{c} = \sqrt{15.2}$$

$$v_{c} = 3.90\ \text{m s}^{-1}\ (3\text{ s.f.}) \checkmark$$

*Using* $v^{2} = u^{2} - 2gr$: $v_{c}^{2} = 25 - 2(9.8)(0.5) = 25 - 9.8 = 15.2$ ✓

**(b) Normal reaction at centre height:**

At the horizontal position (level with centre), the centre of the circle is horizontally inward from the bead. The normal reaction $R$ acts **towards the centre** (horizontally). Weight acts vertically — it has **no component** towards the centre at this position.

Resolve towards centre (horizontal):

$$R = \frac{mv_{c}^{2}}{r}$$

$$R = \frac{0.2 \times 15.2}{0.5}$$

$$R = \frac{3.04}{0.5}$$

$$R = 6.08\ \text{N} \checkmark$$

The reaction is **positive**, so contact is maintained.

*For completeness — reaction at the top:*

$$v_{\text{top}}^{2} = 25 - 4(9.8)(0.5) = 25 - 19.6 = 5.4$$

$$R_{\text{top}} + mg = \frac{mv_{\text{top}}^{2}}{r}\ \text{(both towards centre at top — careful)}$$

At the top, the centre is **below** the bead. $R$ acts downward (towards centre), weight also downward:

$$R_{\text{top}} + mg = \frac{mv_{\text{top}}^{2}}{r}$$

$$R_{\text{top}} = \frac{0.2 \times 5.4}{0.5} - 1.96$$

$$R_{\text{top}} = 2.16 - 1.96$$

$$R_{\text{top}} = 0.20\ \text{N} > 0$$

Contact is still maintained at the top (just barely). For a bead on a wire, $R$ can become negative (meaning the bead presses on the outer side), but here it remains positive.

*Critical check for wire (bead can complete circle if* $u \geq 2\sqrt{gr} = 2\sqrt{4.9} = 4.43\text{ m s}^{-1}$*): $5 > 4.43$ ✓*

---

## Example 5 — String Goes Slack: Finding the Slack Point (Hard)

> **Question:** A particle of mass $0.3\text{ kg}$ is attached to a light inextensible string of length $0.6\text{ m}$. The string is fixed at one end and the particle is projected horizontally from its lowest point with speed $4.5\text{ m s}^{-1}$. The particle moves in a vertical circle. Determine whether the string goes slack before reaching the top, and if so, find the angle (from the downward vertical) at which the string becomes slack. Take $g = 9.8\text{ m s}^{-2}$.

**Solution:**

**Step 1 — Check if the particle can complete the circle:**

$$u_{\text{crit}} = \sqrt{5gr}$$

$$u_{\text{crit}} = \sqrt{5 \times 9.8 \times 0.6}$$

$$u_{\text{crit}} = \sqrt{29.4}$$

$$u_{\text{crit}} = 5.42\ \text{m s}^{-1}$$

Since $u = 4.5 < 5.42$, the string **will go slack** before the top. ✓

**Step 2 — Also check it gets past the horizontal:**

$$\sqrt{2gr} = \sqrt{2 \times 9.8 \times 0.6}$$

$$\sqrt{2gr} = \sqrt{11.76}$$

$$\sqrt{2gr} = 3.43\ \text{m s}^{-1}$$

Since $u = 4.5 > 3.43$, the particle rises above the horizontal before going slack (regime 2 in §11.2). ✓

**Step 3 — Find the slack angle:**

At angle $\theta$ from the downward vertical, by energy:

$$v^{2} = u^{2} - 2gr(1 - \cos\theta)$$

$$v^{2} = 20.25 - 2(9.8)(0.6)(1 - \cos\theta)$$

$$v^{2} = 20.25 - 11.76(1 - \cos\theta)$$

$$v^{2} = 20.25 - 11.76 + 11.76\cos\theta$$

$$v^{2} = 8.49 + 11.76\cos\theta$$

Radial equation (towards centre):

$$T = \frac{mv^{2}}{r} + mg\cos\theta$$

Set $T = 0$:

$$0 = \frac{mv^{2}}{r} + mg\cos\theta$$

$$0 = \frac{v^{2}}{r} + g\cos\theta$$

$$v^{2} = -gr\cos\theta$$

*Wait — sign check.* At angle $\theta$ from the **downward** vertical, the weight component towards the centre is $mg\cos\theta$ only when $\theta < 90°$ — let us be more careful. Using the foolproof method:

The centre $O$ is at distance $r$ from the particle along the string. At angle $\theta$ from the downward vertical, the position vector from $O$ to the particle makes angle $\theta$ with the downward vertical. The tension $T$ points from particle towards $O$. The weight $mg$ points down. The component of weight **towards** $O$ is $mg\cos\theta$ (when $\theta$ is from downward vertical, the angle between weight (down) and the towards-centre direction is $\theta$).

So:

$$T - mg\cos\theta = \frac{mv^{2}}{r}\quad\text{is WRONG for }\theta > 90°$$

Let us use the combined formula directly:

$$T = \frac{mu^{2}}{r} - 2mg + 3mg\cos\theta$$

Set $T = 0$:

$$0 = \frac{mu^{2}}{r} - 2mg + 3mg\cos\theta$$

Divide by $mg$:

$$0 = \frac{u^{2}}{gr} - 2 + 3\cos\theta$$

$$\cos\theta = \frac{2 - u^{2}/(gr)}{3}$$

$$\frac{u^{2}}{gr} = \frac{20.25}{9.8 \times 0.6}$$

$$\frac{u^{2}}{gr} = \frac{20.25}{5.88}$$

$$\frac{u^{2}}{gr} = 3.444$$

$$\cos\theta = \frac{2 - 3.444}{3}$$

$$\cos\theta = \frac{-1.444}{3}$$

$$\cos\theta = -0.4813$$

$$\theta = \arccos(-0.4813)$$

$$\theta = 119°\ (3\text{ s.f.}) \checkmark$$

Since $\theta = 119° > 90°$, the string goes slack **above the horizontal**, $29°$ above the centre level. At this point:

$$v^{2} = -gr\cos\theta = -9.8 \times 0.6 \times (-0.4813)$$

$$v^{2} = 2.83$$

$$v = 1.68\ \text{m s}^{-1}$$

After this instant the particle follows a projectile path.

> **Verification:** At $\theta = 119°$, $v^{2} = 8.49 + 11.76(-0.4813) = 8.49 - 5.66 = 2.83$ — matches the radial condition $v^{2} = -gr\cos\theta = 2.83$ ✓

---

## Example 6 — Conical Pendulum: Finding the Angle from Angular Speed (Medium)

> **Question:** A small mass of $0.15\text{ kg}$ is attached to a light inextensible string of length $0.9\text{ m}$ fixed at the other end. The mass rotates in a horizontal circle with angular speed $4.0\text{ rad s}^{-1}$ as a conical pendulum. Find (a) the angle the string makes with the vertical, and (b) the tension in the string. Take $g = 9.8\text{ m s}^{-2}$.

**Solution:**

**(a) Angle with the vertical:**

For a conical pendulum:

$$\cos\theta = \frac{g}{l\omega^{2}}$$

$$\cos\theta = \frac{9.8}{0.9 \times 16}$$

$$\cos\theta = \frac{9.8}{14.4}$$

$$\cos\theta = 0.6806$$

$$\theta = \arccos(0.6806)$$

$$\theta = 47.1°\ (3\text{ s.f.}) \checkmark$$

*Check:* $l\omega^{2} = 0.9 \times 16 = 14.4 > g = 9.8$, so a real solution exists. ✓

**(b) Tension:**

$$T\cos\theta = mg$$

$$T = \frac{mg}{\cos\theta}$$

$$T = \frac{0.15 \times 9.8}{0.6806}$$

$$T = \frac{1.47}{0.6806}$$

$$T = 2.16\ \text{N (3 s.f.)} \checkmark$$

*Alternative:*

$$T = \frac{mg}{\cos\theta} = \frac{ml\omega^{2}\cos\theta}{\cos\theta} = ml\omega^{2}\ \text{— no, this is wrong.}$$

Actually $T = mg/\cos\theta$ is the simplest. Numerically $T = 2.16\text{ N}$.

*Cross-check via radial equation:*

$$r = l\sin\theta = 0.9 \times \sin 47.1°$$

$$r = 0.9 \times 0.7330$$

$$r = 0.6597\ \text{m}$$

$$T\sin\theta = mr\omega^{2}$$

$$T = \frac{mr\omega^{2}}{\sin\theta}$$

$$T = \frac{0.15 \times 0.6597 \times 16}{0.7330}$$

$$T = \frac{1.583}{0.7330}$$

$$T = 2.16\ \text{N} \checkmark$$

---

## Example 7 — Particle on the Outside of a Smooth Sphere: Leaving the Surface (Medium–Hard)

> **Question:** A small particle of mass $0.1\text{ kg}$ is placed at the top of a smooth sphere of radius $0.4\text{ m}$ and given a small horizontal push so that it slides down the outside of the sphere with initial speed $0.5\text{ m s}^{-1}$. Find the angle from the top at which the particle loses contact with the sphere. Take $g = 9.8\text{ m s}^{-2}$.

**Solution:**

Let $\theta$ be the angle from the **upward** vertical (from the top), so the particle has descended through vertical height $h = r(1 - \cos\theta)$.

**Energy** (datum at centre, or simply $\Delta h$ lost):

$$v^{2} = u^{2} + 2gr(1 - \cos\theta)$$

$$v^{2} = 0.25 + 2(9.8)(0.4)(1 - \cos\theta)$$

$$v^{2} = 0.25 + 7.84(1 - \cos\theta)$$

**Radial equation** — towards centre (into the sphere). Weight component towards centre is $mg\cos\theta$; normal reaction $R$ acts outward (away from centre):

$$mg\cos\theta - R = \frac{mv^{2}}{r}$$

At the point of leaving, $R = 0$:

$$mg\cos\theta = \frac{mv^{2}}{r}$$

$$g\cos\theta = \frac{v^{2}}{r}$$

$$g\cos\theta = \frac{0.25 + 7.84(1 - \cos\theta)}{0.4}$$

Multiply by $0.4$:

$$0.4g\cos\theta = 0.25 + 7.84 - 7.84\cos\theta$$

$$3.92\cos\theta = 8.09 - 7.84\cos\theta$$

$$3.92\cos\theta + 7.84\cos\theta = 8.09$$

$$11.76\cos\theta = 8.09$$

$$\cos\theta = \frac{8.09}{11.76}$$

$$\cos\theta = 0.6879$$

$$\theta = \arccos(0.6879)$$

$$\theta = 46.5°\ (3\text{ s.f.}) \checkmark$$

*Check with general formula:* $\cos\theta = \tfrac23 + u^{2}/(3gr) = 0.6667 + 0.25/(3 \times 3.92) = 0.6667 + 0.02128 = 0.6879$ ✓

Speed at leaving:

$$v^{2} = gr\cos\theta = 9.8 \times 0.4 \times 0.6879$$

$$v^{2} = 2.697$$

$$v = 1.64\ \text{m s}^{-1}$$

After leaving, the particle follows a projectile trajectory.

---

## Example 8 — Elastic String in Horizontal Circular Motion (Hard)

> **Question:** An elastic string of natural length $0.6\text{ m}$ and modulus of elasticity $12\text{ N}$ has one end fixed and a particle of mass $0.25\text{ kg}$ attached to the other end. The particle is whirled in a horizontal circle with angular speed $5.0\text{ rad s}^{-1}$ with the string taut. Find the extension of the string and the radius of the circle.

**Solution:**

Let $x$ be the extension, so actual length $l = 0.6 + x$ and radius $r = l = 0.6 + x$ (horizontal circle — string is the radius).

Hooke's law:

$$T = \frac{\lambda x}{l_{0}}$$

$$T = \frac{12x}{0.6}$$

$$T = 20x$$

Circular motion (tension provides centripetal force):

$$T = mr\omega^{2}$$

$$T = 0.25 \times r \times 25$$

$$T = 6.25\,r$$

But $r = 0.6 + x$, so:

$$20x = 6.25(0.6 + x)$$

$$20x = 3.75 + 6.25x$$

$$13.75x = 3.75$$

$$x = \frac{3.75}{13.75}$$

$$x = 0.2727\ \text{m}$$

$$x = 0.273\ \text{m (3 s.f.)} \checkmark$$

Radius:

$$r = 0.6 + 0.273$$

$$r = 0.873\ \text{m (3 s.f.)} \checkmark$$

Tension:

$$T = 20 \times 0.2727$$

$$T = 5.45\ \text{N} \checkmark$$

*Check:* $T = 6.25 \times 0.873 = 5.45\text{ N}$ ✓

> **Note:** If this were a **vertical** circle with an elastic string, $r$ would vary with position (tension varies), and you would need to include EPE $\lambda x^{2}/(2l_{0})$ in the energy equation. The horizontal case is simpler because $T$ and $r$ are constant. Vertical elastic circles are rarely examined numerically but you should understand the principle.

---

## Example 9 — Banked Track with Friction: Speed Range (Hard)

> **Question:** A circular bend of radius $50\text{ m}$ is banked at $10°$ to the horizontal. The coefficient of friction between tyres and track is $\mu = 0.3$. Find the range of speeds for which a car can navigate the bend without slipping. Take $g = 9.8\text{ m s}^{-2}$.

**Solution:**

This requires two limiting cases: maximum speed (about to slide **up**) and minimum speed (about to slide **down**).

**Maximum speed — friction acts DOWN the bank:**

Forces: $R$ perpendicular to surface, $F = \mu R$ down the bank, $mg$ down.

Resolve vertically (no vertical acceleration):

$$R\cos\alpha - F\sin\alpha = mg$$

$$R\cos 10° - \mu R\sin 10° = mg$$

$$R(\cos 10° - 0.3\sin 10°) = mg$$

$$R = \frac{mg}{\cos 10° - 0.3\sin 10°}$$

$$R = \frac{9.8m}{0.9848 - 0.3 \times 0.1736}$$

$$R = \frac{9.8m}{0.9848 - 0.05208}$$

$$R = \frac{9.8m}{0.9327}$$

$$R = 10.505\,m$$

Resolve horizontally towards centre:

$$R\sin\alpha + F\cos\alpha = \frac{mv_{\max}^{2}}{r}$$

$$R\sin 10° + \mu R\cos 10° = \frac{mv_{\max}^{2}}{50}$$

$$R(\sin 10° + 0.3\cos 10°) = \frac{mv_{\max}^{2}}{50}$$

$$10.505m\,(0.1736 + 0.3 \times 0.9848) = \frac{mv_{\max}^{2}}{50}$$

$$10.505\,(0.1736 + 0.2954) = \frac{v_{\max}^{2}}{50}$$

$$10.505 \times 0.4690 = \frac{v_{\max}^{2}}{50}$$

$$4.927 = \frac{v_{\max}^{2}}{50}$$

$$v_{\max}^{2} = 246.35$$

$$v_{\max} = 15.7\text{ m s}^{-1}\ (3\text{ s.f.}) \checkmark$$

**Minimum speed — friction acts UP the bank:**

$$R\cos\alpha + F\sin\alpha = mg$$

$$R(\cos 10° + 0.3\sin 10°) = mg$$

$$R = \frac{9.8m}{0.9848 + 0.05208}$$

$$R = \frac{9.8m}{1.0369}$$

$$R = 9.451\,m$$

Horizontal:

$$R\sin\alpha - F\cos\alpha = \frac{mv_{\min}^{2}}{r}$$

$$R(\sin 10° - 0.3\cos 10°) = \frac{mv_{\min}^{2}}{50}$$

$$9.451\,(0.1736 - 0.2954) = \frac{v_{\min}^{2}}{50}$$

$$9.451 \times (-0.1218) = \frac{v_{\min}^{2}}{50}$$

Since this is **negative**, $v_{\min}^{2} < 0$ — meaning even at $v = 0$ the car would not slide down. Indeed:

$$\tan\alpha = \tan 10° = 0.1763 < \mu = 0.3$$

so friction alone can hold the car at rest. Therefore:

$$v_{\min} = 0\text{ m s}^{-1} \checkmark$$

**Range:** $0 \leq v \leq 15.7\text{ m s}^{-1}$ (or more precisely, the car does not slide for any speed up to $15.7\text{ m s}^{-1}$).

*If $\tan\alpha > \mu$, then $v_{\min} > 0$. For example, with $\alpha = 20°$: $\tan 20° = 0.364 > 0.3$, and $v_{\min} = \sqrt{rg(\tan\alpha - \mu)/(1+\mu\tan\alpha)} = \sqrt{490 \times 0.364 - 0.3...}$ giving a non-zero minimum. The formula is:*

$$v_{\min}^{2} = rg\,\frac{\tan\alpha - \mu}{1 + \mu\tan\alpha},\qquad v_{\max}^{2} = rg\,\frac{\tan\alpha + \mu}{1 - \mu\tan\alpha}$$

> ### 👀 Watch Out!
> **Two equations, two unknowns ($R$ and $v$) for each limiting case.** Do not try to use $R = mg/\cos\alpha$ when friction is present — friction has a vertical component that changes $R$. Solve the vertical equation for $R$ first, then substitute into the horizontal equation.

> ### 🎯 What the examiner wants
> Correct friction direction stated for each case (1 mark); vertical and horizontal equations with friction terms (2 marks); solving for $v_{\max}$ (1 mark); recognising $v_{\min} = 0$ when $\mu \geq \tan\alpha$ with reasoning (1 mark).

---

## Example 10 — String Goes Slack: Projectile After Slack (Hard)

> **Question:** A particle of mass $0.25\text{ kg}$ is attached to a light inextensible string of length $0.5\text{ m}$ fixed at $O$. It is projected from its lowest point with speed $4.0\text{ m s}^{-1}$ and moves in a vertical circle. The string goes slack at some point above the horizontal.
> - **(a)** Find the angle $\theta$ (from the downward vertical) at which the string goes slack.
> - **(b)** Find the velocity (magnitude and direction) at the instant the string goes slack.
> - **(c)** Describe the subsequent motion and find the maximum height above $O$ reached by the particle as a projectile.
>
> Take $g = 9.8\text{ m s}^{-2}$.

**Solution (a) — Slack angle:**

Check regimes:

$$u_{\text{crit}} = \sqrt{5gr} = \sqrt{5 \times 9.8 \times 0.5} = \sqrt{24.5} = 4.95\text{ m s}^{-1}$$

Since $4.0 < 4.95$, the string will go slack before the top. ✓

$$\sqrt{2gr} = \sqrt{9.8} = 3.13\text{ m s}^{-1} < 4.0$$

so it rises above the horizontal before going slack. ✓

Use $T = \frac{mu^{2}}{r} - 2mg + 3mg\cos\theta = 0$:

$$\frac{u^{2}}{gr} - 2 + 3\cos\theta = 0$$

$$\frac{16}{4.9} - 2 + 3\cos\theta = 0$$

$$3.2653 - 2 + 3\cos\theta = 0$$

$$1.2653 + 3\cos\theta = 0$$

$$\cos\theta = -0.4218$$

$$\theta = \arccos(-0.4218)$$

$$\theta = 115°\ (3\text{ s.f.}) \checkmark$$

The string goes slack at $115°$ from the downward vertical — that is $25°$ above the horizontal.

**Solution (b) — Velocity at slack:**

Speed: from the slack condition $T = 0 \Rightarrow v^{2}/r = -g\cos\theta$ (with $\cos\theta < 0$ above horizontal):

$$v^{2} = -gr\cos\theta$$

$$v^{2} = -9.8 \times 0.5 \times (-0.4218)$$

$$v^{2} = 2.067$$

$$v = 1.44\text{ m s}^{-1}\ (3\text{ s.f.}) \checkmark$$

Direction: tangent to the circle at angle $\theta = 115°$ from downward vertical. The tangent direction makes angle $\theta$ with the horizontal. At this point the velocity has components:

$$v_x = v\cos(180° - \theta) = v\cos 65°\ \text{(outward horizontal)}$$

Actually, let us set coordinates with $O$ at origin. At angle $\theta$ from downward vertical, position is:

$$x = r\sin\theta = 0.5\sin 115° = 0.453\text{ m}$$

$$y = -r\cos\theta = -0.5(-0.4218) = 0.211\text{ m above centre, i.e. } -0.289\text{ m below }O\text{... let us use bottom datum.}$$

Velocity direction: perpendicular to the string. The string at $115°$ from downward vertical points from $O$ to the particle. The tangent (direction of motion) is $90°$ to the string. Since the particle was moving upward/around, the velocity at slack has:

$$\text{Angle above horizontal} = 180° - \theta - 90° = 25°\ \text{above horizontal (outward)}$$

More precisely: the velocity vector is perpendicular to $OP$ and in the direction of motion. At $\theta = 115°$ from downward vertical, the tangent direction is $25°$ above the horizontal (since $115° - 90° = 25°$ from horizontal).

$$v_{x} = v\cos 25° = 1.44 \times 0.9063 = 1.30\text{ m s}^{-1}$$

$$v_{y} = v\sin 25° = 1.44 \times 0.4226 = 0.608\text{ m s}^{-1}$$

Both positive (outward and upward) at the instant of slack. $\checkmark$

**Solution (c) — Projectile motion after slack:**

After the string goes slack, the particle is a projectile with initial position $(x_0, y_0)$ relative to $O$:

$$x_0 = 0.5\sin 115° = 0.453\text{ m}$$

$$y_0 = -0.5\cos 115° = 0.211\text{ m above centre} = -0.289\text{ m below }O$$

Wait — let us use height above the lowest point. Centre is at height $r = 0.5$ m above bottom. At angle $\theta = 115°$:

$$h = r(1 - \cos\theta) = 0.5(1 - (-0.4218)) = 0.5 \times 1.4218 = 0.711\text{ m above bottom}$$

$$h_O = r = 0.5\text{ m above bottom, so height above }O = 0.711 - 0.5 = 0.211\text{ m above }O$$

Height above lowest point at slack: $0.711\text{ m}$.

For projectile motion, maximum additional height from vertical component:

$$v_y = 0.608\text{ m s}^{-1}\ \text{upward}$$

At maximum height, vertical velocity = 0:

$$0 = v_y^{2} - 2g\,\Delta h_{\text{proj}}$$

$$\Delta h_{\text{proj}} = \frac{v_y^{2}}{2g}$$

$$\Delta h_{\text{proj}} = \frac{0.608^{2}}{19.6}$$

$$\Delta h_{\text{proj}} = \frac{0.3697}{19.6}$$

$$\Delta h_{\text{proj}} = 0.0189\text{ m}$$

Maximum height above $O$:

$$h_{\max} = 0.211 + 0.0189 = 0.230\text{ m above }O \checkmark$$

Maximum height above lowest point: $0.711 + 0.0189 = 0.730\text{ m}$.

*Note:* The additional height gained as a projectile is small ($1.9$ cm) because the speed at slack is low. Most of the height was gained during circular motion.

> ### 👀 Watch Out!
> After the string goes slack, the particle does **not** continue in a circle — it becomes a projectile with $a = g$ downward. You must resolve the velocity at the slack point into horizontal and vertical components and use SUVAT/projectile equations. A common error is to continue using energy + circular motion equations after slack.

> ### 🎯 What the examiner wants
> Slack condition $T = 0$ with combined energy+radial formula (2 marks); correct $\theta$ (1 mark); speed at slack via $v^{2} = -gr\cos\theta$ or energy (1 mark); resolving velocity and applying projectile equations for subsequent motion (2 marks).

---

## Example 11 — Conical Pendulum with Two Strings / Double Pendulum Variant (Medium–Hard)

> **Question:** A particle of mass $0.4\text{ kg}$ is attached to a fixed point $O$ by two light inextensible strings: string $OA$ of length $0.6\text{ m}$ and string $OB$ of length $0.8\text{ m}$, where $B$ is a point $0.6\text{ m}$ vertically below $O$ on the same vertical line. The particle moves in a horizontal circle with centre on the line $OB$, with both strings taut. String $OA$ makes $30°$ with the vertical.
> - **(a)** Find the radius of the circle.
> - **(b)** Find the tensions in both strings.
> - **(c)** Find the angular speed.
>
> Take $g = 9.8\text{ m s}^{-2}$.

**Solution (a) — Radius:**

String $OA$ has length $0.6$ m at $30°$ to vertical:

$$r = 0.6\sin 30°$$

$$r = 0.6 \times 0.5$$

$$r = 0.30\text{ m} \checkmark$$

Depth of particle below $O$: $h = 0.6\cos 30° = 0.5196\text{ m}$, so it is $0.6 - 0.5196 = 0.0804\text{ m}$ above $B$ — both strings can be taut since the geometry is consistent (particle between $O$ and $B$ vertically).

Let us verify string $OB$: distance from $B$ to particle. $B$ is $0.6$ m below $O$; particle is $0.5196$ m below $O$ and $0.30$ m from the vertical line:

$$OB_{\text{string}} = \sqrt{0.30^{2} + (0.6-0.5196)^{2}} = \sqrt{0.09 + 0.00646} = \sqrt{0.09646} = 0.311\text{ m}$$

This is less than $0.8$ m, so $OB$ would actually be slack in this configuration. Let us treat a cleaner version: the particle is held by a **single** string of length $0.6$ m at $30°$, plus a **horizontal** string to a vertical pole — a more standard exam configuration.

**Revised standard configuration — Particle with horizontal restraining string:**

A particle of mass $0.4\text{ kg}$ moves in a horizontal circle of radius $0.3\text{ m}$ attached to a fixed point $O$ above by a string of length $0.6\text{ m}$ ($30°$ to vertical), with angular speed $\omega$.

**(b) Tensions — single string conical pendulum:**

$$T\cos 30° = mg$$

$$T = \frac{0.4 \times 9.8}{\cos 30°}$$

$$T = \frac{3.92}{0.8660}$$

$$T = 4.53\text{ N}\ (3\text{ s.f.}) \checkmark$$

**(c) Angular speed:**

$$T\sin 30° = mr\omega^{2}$$

$$\omega^{2} = \frac{T\sin 30°}{mr}$$

$$\omega^{2} = \frac{4.53 \times 0.5}{0.4 \times 0.30}$$

$$\omega^{2} = \frac{2.265}{0.12}$$

$$\omega^{2} = 18.875$$

$$\omega = 4.34\text{ rad s}^{-1}\ (3\text{ s.f.}) \checkmark$$

*Cross-check:* $\omega^{2} = g/(l\cos\theta) = 9.8/(0.6 \times 0.8660) = 9.8/0.5196 = 18.86$ ✓

*Period:* $T_{\text{period}} = 2\pi/\omega = 1.45\text{ s}$.

> ### 👀 Watch Out!
> When additional strings or constraints appear, draw a clear diagram showing every string and its angle. For each string, identify whether it contributes to vertical equilibrium or radial force. A horizontal string contributes only to the radial equation; an angled string contributes to both.

> ### 🎯 What the examiner wants
> Correct radius $r = l\sin\theta$ (1 mark); vertical equilibrium $T\cos\theta = mg$ (1 mark); radial equation with correct $r$ (1 mark); solving for $\omega$ or $T$ (1 mark).

---

# 14. Common Mistakes

| # | Mistake | Why It Loses Marks | Correct Approach |
|---|---------|--------------------|-----------------|
| **1** | Using $r = l$ instead of $r = l\sin\theta$ in a conical pendulum | Radius is the horizontal distance to the centre, not the string length | Always write $r = l\sin\theta$ explicitly |
| **2** | Adding a fictitious "centripetal force" arrow to the force diagram | Centripetal force is not a separate force — it IS the resultant | Write $\sum F_{\text{towards centre}} = mv^{2}/r$ as an equation, not an extra force |
| **3** | Mixing up $\sqrt{gr}$ (top) and $\sqrt{5gr}$ (bottom) | Critical speed depends on where it is measured | Label clearly: $v_{\text{top,crit}} = \sqrt{gr}$, $u_{\text{bottom,crit}} = \sqrt{5gr}$ |
| **4** | Forgetting that $T \geq 0$ for a string but $R$ (rod/wire) can be negative | String goes slack; rod goes into compression | Check the constraint type: string vs rod vs bead on wire |
| **5** | Using degrees where radians are needed (or vice versa) | $\omega$ must be in $\text{rad s}^{-1}$ | Convert rpm → $\text{rad s}^{-1}$ via $\times 2\pi/60$ |
| **6** | Sign errors in the radial equation | $T - mg\cos\theta$ vs $T + mg\cos\theta$ confusion | Always resolve **towards the centre** — draw the arrow, project each force |
| **7** | Using $v$ instead of $v^{2}$ (or taking square roots too early) | Introduces errors, loses the $v^{2}<0$ diagnostic | Keep $v^{2}$ throughout; only take $\sqrt{\phantom{x}}$ at the final step if needed |
| **8** | Inconsistent energy datum | $mgh$ terms have wrong signs | Choose one datum (lowest point simplest) and stick to it |
| **9** | Confusing GPE height with arc length | $\Delta h = r(1-\cos\theta) \neq r\theta$ | Height is **vertical** distance, not distance along the arc |
| **10** | Assuming uniform circular motion in a vertical circle | Speed varies — $v=r\omega$ with constant $\omega$ does NOT apply | Use energy conservation to find $v$ at each point; $\omega$ varies too |
| **11** | Forgetting to check if the particle actually reaches the point being analysed | Computing $T$ at the top when the string already went slack | Always check the slack/leaving condition before assuming circular motion continues |
| **12** | Using $R = mg$ on a banked track | $R\cos\alpha = mg$, so $R > mg$ | Resolve perpendicular to the surface correctly |

> ### 🔑 The Golden Rule for Vertical Circles
> **Energy first, then radial equation, then check $T \geq 0$ / $R \geq 0$.** This three-step sequence solves every vertical-circle question in the syllabus. If you do it in any other order, you will get tangled.

---

# 15. Complete Formula Sheet

## Circular Kinematics

$$v = r\,\omega$$

$$\omega = \frac{2\pi}{T_{\text{period}}} = 2\pi f$$

$$a_{\text{towards centre}} = r\omega^{2} = \frac{v^{2}}{r} = v\omega$$

$$F_{\text{towards centre}} = mr\omega^{2} = \frac{mv^{2}}{r}$$

## Conical Pendulum (string length $l$, angle $\theta$ with vertical)

$$r = l\sin\theta$$

$$T\cos\theta = mg$$

$$T\sin\theta = mr\omega^{2} = \frac{mv^{2}}{r}$$

$$\tan\theta = \frac{r\omega^{2}}{g} = \frac{v^{2}}{rg}$$

$$\cos\theta = \frac{g}{l\omega^{2}}$$

$$T_{\text{period}} = 2\pi\sqrt{\frac{l\cos\theta}{g}} = 2\pi\sqrt{\frac{h}{g}}\quad(h = l\cos\theta)$$

$$T = \frac{mg}{\cos\theta}$$

## Banked Track (angle $\alpha$)

$$\text{Smooth, design speed:}\quad v^{2} = rg\tan\alpha$$

$$\text{With friction:}\quad R\cos\alpha \mp F\sin\alpha = mg,\quad R\sin\alpha \pm F\cos\alpha = \frac{mv^{2}}{r},\quad F \leq \mu R$$

## Vertical Circle — Energy (no loss, datum at bottom)

$$v^{2} = u^{2} - 2gr(1 - \cos\theta)\qquad(\theta\text{ from downward vertical})$$

$$v_{\text{top}}^{2} = u^{2} - 4gr$$

$$v_{\text{horizontal}}^{2} = u^{2} - 2gr$$

$$\tfrac12 mv^{2} + mgh = \text{constant}$$

## Vertical Circle — Radial Equation (towards centre)

$$\text{String / inside hoop:}\quad T\ (\text{or }R) = \frac{mv^{2}}{r} + mg\cos\theta\quad(\theta\text{ from downward vertical})$$

$$\text{Outside sphere:}\quad R = mg\cos\theta - \frac{mv^{2}}{r}\quad(\theta\text{ from top})$$

$$\text{Combined (string, }\theta\text{ from downward vertical):}\quad T = \frac{mu^{2}}{r} - 2mg + 3mg\cos\theta$$

## Critical Speeds

$$v_{\text{top, crit}} = \sqrt{gr}\qquad\text{(string, }T=0\text{ at top)}$$

$$u_{\text{bottom, crit}} = \sqrt{5gr}\qquad\text{(string, complete circle from bottom)}$$

$$u_{\text{bottom, crit}} = 2\sqrt{gr}\qquad\text{(rod / bead on wire, complete circle)}$$

$$\text{String goes slack when }T=0:\quad \cos\theta_{\text{slack}} = \frac{2}{3} - \frac{u^{2}}{3gr}$$

$$\text{Leaves outside sphere when }R=0:\quad \cos\theta_{\text{leave}} = \frac{2}{3} + \frac{u^{2}}{3gr}\quad(\theta\text{ from top})$$

## Elastic String

$$T = \frac{\lambda x}{l_{0}},\qquad l = l_{0} + x,\qquad \text{EPE} = \frac{\lambda x^{2}}{2l_{0}}$$

$$\text{Horizontal circle:}\quad \frac{\lambda x}{l_{0}} = \frac{mv^{2}}{l_{0}+x} = m(l_{0}+x)\omega^{2}$$

## Hooke's Law (general)

$$T = \frac{\lambda x}{l_{0}}\quad\text{(tension)},\qquad \text{EPE} = \frac{\lambda x^{2}}{2l_{0}}$$

---

# 16. Cambridge Exam Analysis

## How Circular Motion is Examined (9231 Further Mechanics)

### Frequency

| Session | Topic Tested | Marks | Style |
|---------|-------------|-------|-------|
| Recent trend | Vertical circle with energy + tension | 10–14 | Long question (Q2/Q3), 3–4 parts |
| Alternate sessions | Conical pendulum or banked track | 6–10 | Medium question |
| Less frequent | Particle leaving a sphere / string going slack | 8–12 | "Find where…" question |
| Rare (hard) | Elastic string in circular motion | 10–14 | Combined Hooke + circular motion |

Circular motion appears on **almost every** Further Mechanics paper — it is one of the most predictable topics.

### Mark Allocation (Typical 12-Mark Vertical Circle Question)

| Part | Task | Marks | What Scores |
|------|------|-------|-------------|
| (a) | Find speed at a given point using energy | 3 | Energy equation (1), correct height (1), speed (1) |
| (b) | Find tension / normal reaction at that point | 3 | Radial equation towards centre (1–2), substitution of $v^{2}$ (1), $T$ or $R$ value (1) |
| (c) | Determine if string goes slack / particle completes circle | 3 | Setting $T=0$ or comparing with $\sqrt{5gr}$ (1), solving for angle or speed (1), conclusion with reason (1) |
| (d) | Find subsequent motion / range / further condition | 2–3 | Projectile equations or further energy analysis |

### What Examiners Reward

1. **Clear force diagrams** — even a rough sketch showing $T$, $mg$, and the centre earns goodwill and helps you avoid sign errors.
2. **Explicit energy equation** — writing $\tfrac12 mv^{2} + mgh = \tfrac12 mu^{2}$ with a stated datum gets the method mark even if arithmetic slips.
3. **"Towards the centre" language** — stating that you resolve towards the centre signals understanding. Examiners use this phrase in mark schemes.
4. **Checking physical validity** — stating "$T > 0$ so the string remains taut" or "$R = 0$ so contact is lost" shows you understand the constraint, not just the algebra.
5. **Exact vs decimal** — Cambridge accepts both $a\sqrt{b}$ and decimal (3 s.f.) forms. Keep surds until the final answer for accuracy.

### What Examiners Penalise

- Using $g = 10$ when the question says $g = 9.8$ (or vice versa) — read the rubric.
- Giving $v$ when $v^{2}$ was asked (or giving speed without direction for velocity).
- Not stating the condition for slack/leaving — just computing a number without the $T=0$ or $R=0$ justification.
- Confusing elastic and inextensible strings.

### Timing Advice

| Question Type | Recommended Time |
|---------------|-----------------|
| Conical pendulum / banked track (6–8 marks) | 10–12 minutes |
| Vertical circle full question (10–14 marks) | 18–25 minutes |
| Practice questions below | 12–15 minutes each |

> **Past paper tip:** FM 9231 papers from 2018 onward all contain at least one circular motion question. Work through them after mastering this guide — the question style is very consistent. The vertical-circle-with-energy question has appeared in over 80% of recent sessions.

---

# 17. Practice Questions & Full Solutions

## Question 1 — Angular Speed Conversion [4 marks]

A particle moves in a circle of radius $0.5\text{ m}$ with frequency $3\text{ rev s}^{-1}$. Find (a) its angular speed, (b) its linear speed, and (c) the magnitude of its acceleration towards the centre.

### Solution 1

**(a) Angular speed:**

$$\omega = 2\pi f$$

$$\omega = 2\pi \times 3$$

$$\omega = 6\pi\ \text{rad s}^{-1}$$

$$\omega \approx 18.8\ \text{rad s}^{-1} \checkmark$$

**(b) Linear speed:**

$$v = r\omega$$

$$v = 0.5 \times 6\pi$$

$$v = 3\pi$$

$$v \approx 9.42\ \text{m s}^{-1} \checkmark$$

**(c) Acceleration:**

$$a = r\omega^{2}$$

$$a = 0.5 \times 36\pi^{2}$$

$$a = 18\pi^{2}$$

$$a \approx 178\ \text{m s}^{-2}$$

*Check:* $a = v^{2}/r = 9\pi^{2}/0.5 = 18\pi^{2}$ ✓

---

## Question 2 — Conical Pendulum: Find the Period [5 marks]

A particle of mass $0.4\text{ kg}$ hangs from a light inextensible string of length $1.0\text{ m}$ and moves as a conical pendulum with the string at $40°$ to the vertical. Find the period of the motion. Take $g = 9.8\text{ m s}^{-2}$.

### Solution 2

$$T\cos\theta = mg$$

$$T = \frac{mg}{\cos\theta}$$

But we need the period. Use:

$$T_{\text{period}} = 2\pi\sqrt{\frac{l\cos\theta}{g}}$$

$$T_{\text{period}} = 2\pi\sqrt{\frac{1.0 \times \cos 40°}{9.8}}$$

$$T_{\text{period}} = 2\pi\sqrt{\frac{0.7660}{9.8}}$$

$$T_{\text{period}} = 2\pi\sqrt{0.07816}$$

$$T_{\text{period}} = 2\pi \times 0.2796$$

$$T_{\text{period}} = 1.76\ \text{s (3 s.f.)} \checkmark$$

*Alternative via* $\omega$:

$$\cos\theta = \frac{g}{l\omega^{2}}$$

$$\omega^{2} = \frac{g}{l\cos\theta}$$

$$\omega^{2} = \frac{9.8}{0.7660}$$

$$\omega^{2} = 12.79$$

$$\omega = 3.577\ \text{rad s}^{-1}$$

$$T_{\text{period}} = \frac{2\pi}{\omega} = \frac{2\pi}{3.577} = 1.76\text{ s} \checkmark$$

---

## Question 3 — Banked Track: Design Speed [4 marks]

A bend of radius $60\text{ m}$ is banked at $12°$ to the horizontal. Find the design speed (no friction required) and state what happens if a car takes the bend faster than this speed. Take $g = 9.8\text{ m s}^{-2}$.

### Solution 3

$$v^{2} = rg\tan\alpha$$

$$v^{2} = 60 \times 9.8 \times \tan 12°$$

$$v^{2} = 588 \times 0.2126$$

$$v^{2} = 125.0$$

$$v = \sqrt{125.0}$$

$$v = 11.2\ \text{m s}^{-1}\ (3\text{ s.f.}) \checkmark$$

If the car is **faster** than $11.2\text{ m s}^{-1}$, it tends to slide **up** the bank (outward). Friction would need to act **down** the slope to provide extra inward force; on a smooth track the car would drift outward. ✓

---

## Question 4 — Vertical Circle: Speed and Tension at the Top [7 marks]

A particle of mass $0.5\text{ kg}$ on a light inextensible string of length $0.6\text{ m}$ is projected from its lowest point with speed $6\text{ m s}^{-1}$ so that it describes a vertical circle with the string taut throughout. Find (a) the speed at the top, (b) the tension at the top, and (c) verify that the string does remain taut. Take $g = 9.8\text{ m s}^{-2}$.

### Solution 4

**(a) Speed at top:**

$$v_{\text{top}}^{2} = u^{2} - 4gr$$

$$v_{\text{top}}^{2} = 36 - 4 \times 9.8 \times 0.6$$

$$v_{\text{top}}^{2} = 36 - 23.52$$

$$v_{\text{top}}^{2} = 12.48$$

$$v_{\text{top}} = \sqrt{12.48}$$

$$v_{\text{top}} = 3.53\ \text{m s}^{-1}\ (3\text{ s.f.}) \checkmark$$

**(b) Tension at top:**

At the top, both $T$ and $mg$ act towards the centre (downward):

$$T_{\text{top}} + mg = \frac{mv_{\text{top}}^{2}}{r}$$

$$T_{\text{top}} = \frac{mv_{\text{top}}^{2}}{r} - mg$$

$$T_{\text{top}} = \frac{0.5 \times 12.48}{0.6} - 0.5 \times 9.8$$

$$T_{\text{top}} = \frac{6.24}{0.6} - 4.9$$

$$T_{\text{top}} = 10.4 - 4.9$$

$$T_{\text{top}} = 5.50\ \text{N (3 s.f.)} \checkmark$$

**(c) Verification:**

$$T_{\text{top}} = 5.50 > 0$$

The tension is positive, so the string does remain taut. ✓

*Check critical speed:* $u_{\text{crit}} = \sqrt{5gr} = \sqrt{29.4} = 5.42\text{ m s}^{-1} < 6$, so complete circle expected. ✓

---

## Question 5 — Vertical Circle: Finding Where the String Goes Slack [7 marks]

A particle of mass $0.2\text{ kg}$ on a string of length $0.8\text{ m}$ is projected from the lowest point with speed $5.0\text{ m s}^{-1}$. Show that the string goes slack before the top and find the angle from the downward vertical at which this happens. Take $g = 9.8\text{ m s}^{-2}$.

### Solution 5

**Check regimes:**

$$u_{\text{crit}} = \sqrt{5gr} = \sqrt{5 \times 9.8 \times 0.8}$$

$$u_{\text{crit}} = \sqrt{39.2}$$

$$u_{\text{crit}} = 6.26\ \text{m s}^{-1}$$

Since $5.0 < 6.26$, the string will go slack before the top. ✓

$$\sqrt{2gr} = \sqrt{15.68} = 3.96\text{ m s}^{-1} < 5.0$$

So the particle rises above the horizontal before going slack.

**Find slack angle — set** $T = 0$:

Using $T = mu^{2}/r - 2mg + 3mg\cos\theta = 0$:

$$\frac{u^{2}}{gr} - 2 + 3\cos\theta = 0$$

$$\frac{25}{9.8 \times 0.8} - 2 + 3\cos\theta = 0$$

$$\frac{25}{7.84} - 2 + 3\cos\theta = 0$$

$$3.1888 - 2 + 3\cos\theta = 0$$

$$1.1888 + 3\cos\theta = 0$$

$$\cos\theta = -0.3963$$

$$\theta = \arccos(-0.3963)$$

$$\theta = 113°\ (3\text{ s.f.}) \checkmark$$

The string goes slack at $113°$ from the downward vertical, i.e. $23°$ above the horizontal on the way up.

Speed at slack point:

$$v^{2} = -gr\cos\theta = -7.84 \times (-0.3963)$$

$$v^{2} = 3.107$$

$$v = 1.76\ \text{m s}^{-1}$$

---

## Question 6 — Bead on a Circular Hoop: Normal Reaction [6 marks]

A bead of mass $0.15\text{ kg}$ slides on a smooth circular hoop of radius $0.4\text{ m}$ fixed in a vertical plane. It is projected from the bottom with speed $4.5\text{ m s}^{-1}$. Find (a) the speed at the top, and (b) the normal reaction at the top. Take $g = 9.8\text{ m s}^{-2}$.

### Solution 6

**(a) Speed at top:**

$$v_{\text{top}}^{2} = u^{2} - 4gr$$

$$v_{\text{top}}^{2} = 20.25 - 4 \times 9.8 \times 0.4$$

$$v_{\text{top}}^{2} = 20.25 - 15.68$$

$$v_{\text{top}}^{2} = 4.57$$

$$v_{\text{top}} = \sqrt{4.57}$$

$$v_{\text{top}} = 2.14\ \text{m s}^{-1}\ (3\text{ s.f.}) \checkmark$$

**(b) Normal reaction at top:**

At the top, centre is below the bead. Both $R$ (towards centre = downward) and $mg$ (downward) act towards centre:

$$R + mg = \frac{mv_{\text{top}}^{2}}{r}$$

$$R = \frac{mv_{\text{top}}^{2}}{r} - mg$$

$$R = \frac{0.15 \times 4.57}{0.4} - 0.15 \times 9.8$$

$$R = \frac{0.6855}{0.4} - 1.47$$

$$R = 1.714 - 1.47$$

$$R = 0.244\ \text{N (3 s.f.)} \checkmark$$

$R > 0$ — contact maintained. For a hoop (unlike a string), even $R < 0$ would mean the bead presses on the outside of the hoop but remains on the wire. The bead completes the circle.

---

## Question 7 — Particle Leaving a Smooth Sphere [6 marks]

A particle of mass $0.3\text{ kg}$ slides on the outside of a smooth sphere of radius $0.5\text{ m}$, starting from rest at the top. Find the angle from the top at which it leaves the sphere. Take $g = 9.8\text{ m s}^{-2}$.

### Solution 7

Released from rest: $u = 0$.

Energy ($\theta$ from top, height lost $= r(1-\cos\theta)$):

$$v^{2} = 2gr(1 - \cos\theta)$$

$$v^{2} = 2 \times 9.8 \times 0.5 \times (1 - \cos\theta)$$

$$v^{2} = 9.8(1 - \cos\theta)$$

Radial equation (towards centre, into sphere):

$$mg\cos\theta - R = \frac{mv^{2}}{r}$$

Set $R = 0$:

$$g\cos\theta = \frac{v^{2}}{r}$$

$$9.8\cos\theta = \frac{9.8(1 - \cos\theta)}{0.5}$$

$$9.8\cos\theta = 19.6(1 - \cos\theta)$$

Divide by $9.8$:

$$\cos\theta = 2(1 - \cos\theta)$$

$$\cos\theta = 2 - 2\cos\theta$$

$$3\cos\theta = 2$$

$$\cos\theta = \frac{2}{3}$$

$$\theta = \arccos\left(\frac{2}{3}\right)$$

$$\theta = 48.2°\ (3\text{ s.f.}) \checkmark$$

This is the classic result: a particle released from rest on a smooth sphere leaves at $\cos\theta = 2/3$.

---

## Question 8 — Conical Pendulum: Given Period Find Angle [5 marks]

A particle of mass $0.25\text{ kg}$ on a string of length $0.75\text{ m}$ performs conical pendulum motion with period $1.5\text{ s}$. Find the angle the string makes with the vertical and the tension. Take $g = 9.8\text{ m s}^{-2}$.

### Solution 8

$$\omega = \frac{2\pi}{T_{\text{period}}}$$

$$\omega = \frac{2\pi}{1.5}$$

$$\omega = \frac{4\pi}{3}$$

$$\omega = 4.189\ \text{rad s}^{-1}$$

For a conical pendulum:

$$\cos\theta = \frac{g}{l\omega^{2}}$$

$$\cos\theta = \frac{9.8}{0.75 \times (4.189)^{2}}$$

$$\cos\theta = \frac{9.8}{0.75 \times 17.545}$$

$$\cos\theta = \frac{9.8}{13.159}$$

$$\cos\theta = 0.7447$$

$$\theta = \arccos(0.7447)$$

$$\theta = 41.9°\ (3\text{ s.f.}) \checkmark$$

Tension:

$$T = \frac{mg}{\cos\theta}$$

$$T = \frac{0.25 \times 9.8}{0.7447}$$

$$T = \frac{2.45}{0.7447}$$

$$T = 3.29\ \text{N (3 s.f.)} \checkmark$$

---

## Question 9 — Vertical Circle with Elastic String (Stretch) [6 marks]

An elastic string of natural length $0.5\text{ m}$ and modulus $15\text{ N}$ is fixed at one end with a particle of mass $0.2\text{ kg}$ at the other end. The particle is whirled in a horizontal circle at angular speed $6.0\text{ rad s}^{-1}$ with the string taut. Find the extension. Take $g$ as not needed (horizontal circle).

### Solution 9

Let extension $= x$, so $r = 0.5 + x$.

$$T = \frac{\lambda x}{l_{0}}$$

$$T = \frac{15x}{0.5}$$

$$T = 30x$$

Also:

$$T = mr\omega^{2}$$

$$T = 0.2 \times (0.5 + x) \times 36$$

$$T = 7.2(0.5 + x)$$

Equate:

$$30x = 7.2(0.5 + x)$$

$$30x = 3.6 + 7.2x$$

$$22.8x = 3.6$$

$$x = \frac{3.6}{22.8}$$

$$x = 0.1579\ \text{m}$$

$$x = 0.158\ \text{m (3 s.f.)} \checkmark$$

Actual length $= 0.5 + 0.158 = 0.658\text{ m}$, tension $T = 30 \times 0.158 = 4.74\text{ N}$.

*Check:* $T = 7.2 \times 0.658 = 4.74\text{ N}$ ✓

---

## Question 10 — Combined: Critical Speed for Complete Circle [5 marks]

A particle of mass $0.35\text{ kg}$ on a string of length $0.7\text{ m}$ must complete a full vertical circle with the string taut throughout. Find the minimum projection speed from the lowest point. If the particle is instead attached to a light rod of the same length, what is the minimum speed? Take $g = 9.8\text{ m s}^{-2}$.

### Solution 10

**String:**

$$u_{\min} = \sqrt{5gr}$$

$$u_{\min} = \sqrt{5 \times 9.8 \times 0.7}$$

$$u_{\min} = \sqrt{34.3}$$

$$u_{\min} = 5.86\ \text{m s}^{-1}\ (3\text{ s.f.}) \checkmark$$

*Reason:* At the top, need $v_{\text{top}} \geq \sqrt{gr}$ and $v_{\text{top}}^{2} = u^{2} - 4gr$, so $u^{2} \geq 5gr$.

**Rod:**

A rod can support compression, so the only requirement is reaching the top ($v_{\text{top}} \geq 0$):

$$u_{\min} = \sqrt{4gr}$$

$$u_{\min} = \sqrt{4 \times 9.8 \times 0.7}$$

$$u_{\min} = \sqrt{27.44}$$

$$u_{\min} = 5.24\ \text{m s}^{-1}\ (3\text{ s.f.}) \checkmark$$

Alternatively $2\sqrt{gr} = 2\sqrt{6.86} = 5.24\text{ m s}^{-1}$.

The rod requires a lower speed because it can push at the top, whereas the string needs extra speed to keep $T > 0$.

---

# 18. Quick Reference Card

*Cut this out for last-minute revision.*

### Circular Kinematics

$$v = r\omega,\qquad \omega = \frac{2\pi}{T} = 2\pi f$$

### Centripetal Acceleration & Force

$$a = r\omega^{2} = \frac{v^{2}}{r}\ \text{towards centre},\qquad F = \frac{mv^{2}}{r}\ \text{towards centre}$$

### Conical Pendulum ($l$ = string length, $\theta$ from vertical)

$$r = l\sin\theta,\quad T\cos\theta = mg,\quad T\sin\theta = \frac{mv^{2}}{r},\quad \cos\theta = \frac{g}{l\omega^{2}},\quad T_{\text{period}} = 2\pi\sqrt{\frac{l\cos\theta}{g}}$$

### Banked Track (smooth, design speed)

$$v^{2} = rg\tan\alpha$$

### Vertical Circle — Energy (datum at bottom, $\theta$ from downward vertical)

$$v^{2} = u^{2} - 2gr(1-\cos\theta),\qquad v_{\text{top}}^{2} = u^{2} - 4gr$$

### Vertical Circle — Radial (towards centre)

$$T - mg\cos\theta = \frac{mv^{2}}{r}\quad\text{(string, }\theta\text{ from downward vertical — check signs!)}$$

$$T = \frac{mu^{2}}{r} - 2mg + 3mg\cos\theta$$

### Critical Speeds

$$v_{\text{top, crit}} = \sqrt{gr}\quad\text{(top)},\qquad u_{\text{bottom, crit}} = \sqrt{5gr}\ \text{(string)},\quad u_{\text{bottom, crit}} = 2\sqrt{gr}\ \text{(rod/wire)}$$

### String Goes Slack / Leaves Surface

$$T = 0 \implies \cos\theta_{\text{slack}} = \frac{2}{3} - \frac{u^{2}}{3gr}\quad\text{(string)}$$

$$R = 0 \implies \cos\theta_{\text{leave}} = \frac{2}{3} + \frac{u^{2}}{3gr}\quad\text{(outside sphere, }\theta\text{ from top)}$$

### Elastic String

$$T = \frac{\lambda x}{l_{0}},\qquad \text{EPE} = \frac{\lambda x^{2}}{2l_{0}},\qquad l = l_{0}+x$$

### Regimes (string from bottom, speed $u$)

$$u < \sqrt{2gr}:\ \text{pendulum swing} \mid\ \sqrt{2gr} < u < \sqrt{5gr}:\ \text{goes slack} \mid\ u \geq \sqrt{5gr}:\ \text{complete circle}$$

### Deadly Sins

1. Using $r = l$ instead of $r = l\sin\theta$ ❌
2. Drawing a separate "centripetal force" arrow ❌
3. Mixing up $\sqrt{gr}$ and $\sqrt{5gr}$ ❌
4. Forgetting $T \geq 0$ (string) vs rod can push ❌
5. Sign errors — always resolve **towards the centre** ❌
6. Taking $\sqrt{v^{2}}$ too early — keep $v^{2}$ ❌
7. Assuming uniform circular motion in a vertical circle ❌

---

> **Good luck! Every Cambridge Circular Motion question follows one of the patterns in this guide.** Master the three-step mantra — **Energy → Radial equation → Check $T\geq 0$** — and no vertical circle can surprise you. 🚀

---
