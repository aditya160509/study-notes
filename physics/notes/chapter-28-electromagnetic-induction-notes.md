# Chapter 28: Electromagnetic Induction - CAIE A Level Physics (9702) Study Notes

Exam-focused revision notes for Cambridge International AS & A Level Physics 9702, covering Topic 18 (Electromagnetic Induction) as taught in Chapter 28 of the coursebook. Everything here is what the exam can actually ask, nothing more. All definitions are worded to match mark schemes, and every question type below has appeared in real 9702 papers (mainly Paper 4 structured questions). Every theory section ends with worked examples, so you can see the formula being used the moment it is introduced.

## 1. Theory

### 1.1 Observing electromagnetic induction

Electromagnetic induction is the process whereby a **current or e.m.f. is induced** when a conductor and a magnetic field move relative to each other. Most of the electricity we use is generated this way — power-station generators, wind turbines and bicycle dynamos all work by induction.

Three school experiments illustrate every feature Cambridge can ask:

1. **Motor as generator:** spin the shaft of a small motor connected to a voltmeter — the meter deflects; faster spin gives larger deflection; stopping gives zero. A generator is a motor in reverse.
2. **Magnet and coil:** move a bar magnet into a coil connected to a microammeter — the meter deflects while the magnet moves; holding it still gives zero; removing it deflects the other way; faster movement and stronger magnets give larger deflection; more turns gives larger deflection.
3. **Wire in a field:** move a straight wire through the field between two magnets — the meter deflects; twice the length in the field gives twice the deflection; forming the wire into a loop doubles the flux linkage.

**Factors that affect the induced current or e.m.f.:**

- For a straight wire: magnitude of $B$, length $L$ of wire in the field, speed $v$ of movement.
- For a coil: magnitude of $B$, cross-sectional area $A$, number of turns $N$, rate at which the coil turns or moves.

All of these are contained in the two laws of induction (Faraday and Lenz) below.

> Exam relevance: the 9702 specification lists "describe experiments which illustrate aspects of electromagnetic induction" — the three experiments above are what the mark scheme expects. You must state that an e.m.f. is induced only **while** there is relative movement / change of flux, and that the size depends on rate of change, not on the flux itself.

### 1.2 Cutting magnetic field lines

We represent a magnetic field by field lines. When a wire moves so that it **cuts across** the lines, an induced current appears; when the wire is parallel to the lines it cuts none and no current appears. Moving the magnet past a stationary conductor has the same effect — it is the **relative** cutting that matters.

A coil links a number of field lines. When the coil is outside the field, no lines link it; when it is inside, lines link it. Moving the coil into or out of the field **changes the linkage**, and this induces an e.m.f. across the ends of the coil (or a current if the coil is part of a complete circuit).

**Induced e.m.f. vs induced current:** if the conductor is not part of a complete circuit, charges separate to the ends and an **e.m.f.** appears (work is done pushing the wire, becoming electrical energy). If the ends are connected, that e.m.f. drives a current through the circuit. So we always talk about an induced **e.m.f.** — the current is secondary.

> Exam relevance: questions often start "explain why an e.m.f. is induced" — answer with "conductor cuts field lines / flux linkage changes due to relative movement between conductor and field."

### 1.3 Magnetic flux $\Phi$ and flux linkage $N\Phi$

**Magnetic flux**, $\Phi$, is the product of the magnetic flux density and the area it threads, taking account of angle:

$$\Phi = BA\cos\theta$$

- $B$ is the magnetic flux density (T), $A$ is the area (m$^2$), $\theta$ is the angle between the field direction and the **normal** to the area. When the field is perpendicular to the plane of the area ($B$ parallel to the normal), $\cos\theta = 1$ and $\Phi = BA$.
- SI unit: **weber** (Wb), where $1~\text{Wb} = 1~\text{T m}^2$.

For a coil of $N$ turns, the total linkage is the **magnetic flux linkage**:

$$\text{flux linkage} = N\Phi = BAN\cos\theta$$

When $\theta$ is not mentioned and the field is perpendicular to the coil face, $\text{flux linkage} = BAN$.

**Flux vs flux linkage — the distinction Cambridge enforces:** flux is for one loop ($\Phi$); flux linkage is for $N$ loops ($N\Phi$). Using one when you mean the other loses the mark. The weber is the unit of flux; flux linkage has units **Wb turns** (often just Wb, but the "$N$" must appear in the formula).

> Exam relevance: every Faraday's-law calculation starts with $\Phi = BA$ or $N\Phi = BAN$. Angle questions use $\Phi = BA\cos\theta$ with $\theta$ measured from the **normal** (a common trap: the angle given may be to the **plane** — you then need $\sin$ or $90° - \theta$).

### 1.4 Faraday's law of electromagnetic induction

**Faraday's law:** the magnitude of the induced e.m.f. is **proportional to the rate of change of magnetic flux linkage**:

$$E \propto \frac{\Delta(N\Phi)}{\Delta t} \qquad \text{and with SI units} \qquad E = \frac{\Delta(N\Phi)}{\Delta t}$$

In differential form (what the mark scheme recognizes for the $e = -k\frac{d\Phi}{dt}$ discussion):

$$E = -\frac{d(N\Phi)}{dt}$$

The minus sign is Lenz's law (next section). For **magnitude** questions the minus can be dropped:

$$|E| = N\frac{\Delta\Phi}{\Delta t} = N\frac{\Delta(BA\cos\theta)}{\Delta t}$$

If $B$ or $A$ or $\theta$ changes, the corresponding $\Delta$ appears. If only $B$ changes and $A$, $N$ are constant, $|E| = NA\frac{\Delta B}{\Delta t}$. If a coil rotates, $\Phi = BA\cos\omega t$ and $E = BAN\omega\sin\omega t$.

**Units check:** $E$ in volts (V), $N\Phi$ in Wb turns, $t$ in s, so $\frac{\text{Wb}}{\text{s}} = \text{V}$.

> Exam relevance: the statement "proportional to the rate of change of flux linkage" earns 1 mark; the formula $E = N\frac{\Delta\Phi}{\Delta t}$ earns the second mark. You must say **flux linkage** (not just flux) when a coil is involved.

### 1.5 Lenz's law — direction of the induced e.m.f.

**Lenz's law:** the direction of the induced e.m.f. (and hence of any induced current) is such that it **opposes the change that produces it**.

- If flux linkage through a coil **increases**, the induced current creates a field that tries to **reduce** the linkage.
- If flux linkage **decreases**, the induced current tries to **increase** it.

Lenz's law is conservation of energy: if the induced current aided the change, the change would grow without limit, giving free energy. Opposing the change means work must be done to move the magnet or wire — that work becomes the electrical energy.

**Fleming's right-hand rule (generator rule)** gives the direction for a straight wire: thumb = **M**otion of the conductor, **F**irst finger = **F**ield (N to S), se**C**ond finger = induced **C**urrent (conventional). It is the mirror image of the motor (left-hand) rule — for a motor you **supply** a current and get a force; for a generator you **provide** a motion and get a current.

**Full Faraday–Lenz law combining both:**

$$E = -\frac{d(N\Phi)}{dt}$$

The negative sign carries the Lenz direction. For magnitude questions Cambridge usually asks for $|E|$ and a separate direction deduction via Lenz or the right-hand rule.

> Exam relevance: every direction question is a Lenz question. The mark scheme expects "opposes the change in flux / flux linkage" plus either the field direction of the induced current or the right-hand rule with all three fingers correctly assigned. Saying "opposes the motion" alone is insufficient — the opposed thing is the **change in flux linkage**.

### 1.6 Induced e.m.f. in a straight wire: $E = Blv$

When a straight conductor of length $L$ moves at speed $v$ perpendicular to a uniform field $B$ (and perpendicular to its own length), the induced e.m.f. between its ends is:

$$E = Blv$$

If the velocity makes an angle $\theta$ to the field (still perpendicular to the wire length), $E = Blv\sin\theta$. If the wire moves parallel to the field, $E = 0$.

This is a special case of Faraday's law: in time $\Delta t$ the wire sweeps area $A = Lv\Delta t$, so $\Delta\Phi = B\Delta A = BLv\Delta t$ and $E = \frac{\Delta\Phi}{\Delta t} = Blv$.

> Exam relevance: $E = Blv$ is NOT on the 9702 data sheet — but it follows in one line from Faraday's law ($E = \frac{\Delta\Phi}{\Delta t}$, $\Phi = BA$, $A = Lx$). Cambridge expects you to derive it. It appears when a wire slides on rails, a rod falls through a field, or a search coil is mentioned.

### 1.7 Factors affecting the size of the induced e.m.f. — summary

From Faraday's law, every factor that makes $N\frac{\Delta\Phi}{\Delta t}$ larger makes $E$ larger:

- Stronger field $B$ (larger $\Phi$ for the same area).
- Larger area $A$ or more turns $N$.
- Faster movement / faster rate of change of $B$ or of angle $\theta$.
- An iron core that increases the flux through the coil.

For a rotating coil in a uniform field, the flux linkage varies as $N\Phi = BAN\cos\omega t$, so $E = BAN\omega\sin\omega t$. The **peak** e.m.f. is $E_0 = BAN\omega$, and the e.m.f. is maximum when the **rate of change** of flux is maximum (coil plane parallel to the field, flux zero), not when the flux is maximum.

> Exam relevance: the mark scheme for "what affects the induced e.m.f.?" rewards any two of: $B$, $A$, $N$, speed/rate, angle. For a rotating coil, the distinction between "flux is maximum" and "rate of change of flux is maximum" separates A from B grades.

### 1.8 Applications of electromagnetic induction

**Eddy currents:** when a solid metal plate moves through a non-uniform field, or a changing field threads a solid conductor, circulating currents (eddy currents) are induced in the metal. By Lenz's law they oppose the motion, producing a **braking force**. Applications: electromagnetic braking (trains, drop-tower rides), damping in moving-coil meters. Laminating the core (thin sheets insulated from each other) breaks up the eddy-current paths and reduces energy loss — why transformer cores are laminated.

**Generators (alternators):** a coil rotated in a magnetic field — the changing flux linkage induces an alternating e.m.f. $E = BAN\omega\sin\omega t$, which is sinusoidal. A bicycle dynamo and power-station generators are the coursebook examples. The generated e.m.f. is maximum when the coil cuts the field fastest, not when it is face-on to the field.

> Exam relevance: Chapter 28 teaches the **principles** (flux, Faraday, Lenz, $E = Blv$, eddy currents, generators); the **quantitative** alternating-current and transformer material is Chapter 29. A question that asks for an e.m.f. value uses Chapter 28; a question that asks for r.m.s. or power transmission uses Chapter 29. Cambridge often combines them: Faraday gives the peak $E_0 = BAN\omega$, then Chapter 29 converts to $E_{\text{rms}} = E_0/\sqrt{2}$.

## 2. Definition Sheet

Every definition you must know word-perfect for the exam. Learn these exactly — the wording is what the mark schemes award.

> **Magnetic flux ($\Phi$):** the product of the magnetic flux density and the area perpendicular to the field: $\Phi = BA\cos\theta$, where $\theta$ is the angle between the field and the normal to the area. Unit: weber (Wb), where $1~\text{Wb} = 1~\text{T m}^2$. Flux is a scalar.
>
> Mark scheme: must include "$BA$" and "perpendicular" or "$\cos\theta$" and the unit Wb. Saying "number of field lines" alone earns at most 1 mark.

> **Magnetic flux linkage ($N\Phi$):** the product of the number of turns $N$ of a coil and the magnetic flux $\Phi$ through each turn: $\text{flux linkage} = N\Phi = BAN\cos\theta$. Unit: weber-turns (Wb turns). For $N = 1$, flux linkage equals flux.
>
> Mark scheme: the "$N$" is compulsory when a coil is involved; "flux linkage" is not the same as "flux" — using one for the other loses the mark.

> **Weber (definition):** one weber is the magnetic flux through an area of $1~\text{m}^2$ perpendicular to a uniform magnetic flux density of $1~\text{T}$: $1~\text{Wb} = 1~\text{T m}^2$.
>
> Mark scheme: "$\text{T m}^2$" or "field of $1~\text{T}$ through $1~\text{m}^2$ perpendicular" earns the mark.

> **Faraday's law of electromagnetic induction:** the magnitude of the induced e.m.f. is proportional to the rate of change of magnetic flux linkage: $E \propto \frac{\Delta(N\Phi)}{\Delta t}$, or with coherent SI units $E = \frac{\Delta(N\Phi)}{\Delta t}$.
>
> Mark scheme: "proportional to the rate of change of (magnetic) flux linkage" — must say "rate of change" and "flux linkage" (not just "flux" when a coil is involved, not just "flux linkage changes").

> **Lenz's law:** the direction of the induced e.m.f. (and hence of any induced current) is such that it opposes the change that produces it (the change in magnetic flux linkage).
>
> Mark scheme: "opposes the change in flux / flux linkage" — must include "change" and the thing opposed is the flux, not the motion or the field. This is conservation of energy.

> **Fleming's right-hand rule (generator rule):** with the thumb, first finger and second finger of the right hand held mutually at right angles, the thu**M**b points in the direction of **M**otion of the conductor, the **F**irst finger points in the direction of the magnetic **F**ield (N to S), and the se**C**ond finger points in the direction of the (conventional) induced **C**urrent.
>
> Mark scheme: all three assignments must be correct; using the left hand is a motor-rule answer and earns zero.

> **Eddy currents:** circulating electric currents induced in a solid conductor by a changing magnetic flux through the conductor. By Lenz's law their magnetic field opposes the change in flux, producing a braking or damping force and dissipating energy as heat ($I^2R$).
>
> Mark scheme: "currents induced in the conductor / metal" + "oppose the change / motion" (Lenz) + "cause heating / energy loss" earns full marks.

> **Generator (alternator principle):** a device that converts mechanical energy into electrical energy by rotating a coil in a magnetic field so that the magnetic flux linkage through the coil changes continuously, inducing an alternating e.m.f. by Faraday's law: $E = BAN\omega\sin\omega t$.
>
> Mark scheme: "coil rotates in a magnetic field" + "changing flux linkage" + "induces an e.m.f. (by Faraday's law)" earns the marks.

> **Rate of change of flux linkage:** the change in $N\Phi$ per unit time, $\frac{\Delta(N\Phi)}{\Delta t}$, in Wb s$^{-1}$ (= V). Its magnitude equals the induced e.m.f.; its sign (via Lenz, $E = -d(N\Phi)/dt$) gives the direction. The induced e.m.f. is **maximum when the rate of change is maximum**, not when the flux itself is maximum.

## 3. Formula Sheet

**Quick reference:**

$$\Phi = BA\cos\theta, \qquad N\Phi = BAN\cos\theta, \qquad E = \frac{\Delta(N\Phi)}{\Delta t}, \qquad E = -\frac{d(N\Phi)}{dt}, \qquad E = Blv, \qquad E_0 = BAN\omega, \quad [1~\text{Wb} = 1~\text{T m}^2]$$

| Formula | Meaning of symbols | Units | When to use it |
|---|---|---|---|
| $$\Phi = BA\cos\theta$$ | $\Phi$ magnetic flux, $B$ flux density, $A$ area, $\theta$ angle between field and normal to area | $\Phi$ in Wb, $B$ in T, $A$ in m$^2$, $\theta$ in rad/° | Flux through a loop or area; if $B$ is perpendicular to the plane, $\Phi = BA$ |
| $$N\Phi = BAN\cos\theta$$ | $N\Phi$ flux linkage, $N$ turns, $B$ flux density, $A$ area | Wb turns | Flux linkage for a coil; the form Faraday's law uses |
| $$E = \frac{\Delta(N\Phi)}{\Delta t}$$ | $E$ induced e.m.f. magnitude, $N\Phi$ flux linkage, $t$ time | $E$ in V, $N\Phi$ in Wb, $t$ in s, $\frac{\text{Wb}}{\text{s}} = \text{V}$ | Faraday's law magnitude; work out $\Delta(N\Phi)$ first, then divide by $\Delta t$ |
| $$E = -\frac{d(N\Phi)}{dt}$$ | $E$ induced e.m.f. with Lenz sign, $N\Phi$ flux linkage | V | Direction (Lenz): the minus sign means the induced field opposes the change in $N\Phi$ |
| $$E = Blv$$ | $E$ induced e.m.f. across a straight wire, $B$ flux density, $l$ length in field, $v$ speed perpendicular to field and wire | $E$ in V, $l$ in m, $v$ in m s$^{-1}$ | Straight wire cutting a field; if $v$ is at angle $\theta$ to $B$, $E = Blv\sin\theta$; parallel to field gives $E = 0$ |
| $$E = Blv\sin\theta$$ | $\theta$ angle between wire velocity and field | V | General $Blv$ at an angle ($v$ perpendicular to wire length) |
| $$E_0 = BAN\omega$$ | Peak e.m.f. of a coil rotating at angular speed $\omega$ in a uniform field | V | Generator / rotating coil: $E = E_0\sin\omega t = BAN\omega\sin\omega t$ |
| $$1~\text{Wb} = 1~\text{T m}^2$$ | Weber in terms of tesla and area | Wb = T m$^2$ | Unit conversions and base-unit checks |

Constants you will need: the elementary charge $e = 1.60 \times 10^{-19}~\text{C}$ appears when induced e.m.f. drives a current that does work $eE$; $\pi = 3.14$ for area $A = \pi r^2$ of a circular coil.

**Exam fact:** $E = \frac{\Delta(N\Phi)}{\Delta t}$ and $\Phi = BA$ (with $\cos\theta$) are the foundation; $E = Blv$ and $E_0 = BAN\omega$ are **derived** from them ($\Phi = BA$, $A = Lv\Delta t$ or $A\cos\omega t$) and are not printed separately on the 9702 data sheet. You must be able to derive $Blv$ in two lines when asked. The minus sign ($E = -d(N\Phi)/dt$) carries the Lenz direction — for a magnitude the sign can be dropped, but for a direction you must invoke Lenz ("opposes the change in flux linkage") or the right-hand rule.

## 4. Methods (Question Types & Methods)

These are the ways Cambridge has actually asked about electromagnetic induction. Each method below is what a full-mark answer looks like.

### 1. Calculate magnetic flux or flux linkage

**Method:**
1. Decide: one loop → $\Phi = BA\cos\theta$; $N$ turns → flux linkage $= N\Phi = BAN\cos\theta$.
2. Find $A$ (for a circle $A = \pi r^2$; be careful — the question may give **diameter**).
3. Decide the angle: $\theta$ is between the **field and the normal** to the plane. If the angle given is to the **plane**, use $90° - \theta$ (or $\sin$).
4. Substitute with units: $B$ in T, $A$ in m$^2$, angle in degrees but $\cos$ handles either.
5. Quote flux in Wb; flux linkage in Wb turns.

**Traps:** using diameter as radius; using the angle to the plane as $\theta$ in $\cos\theta$ (the most common error — field in the plane means $\theta = 90°$ so $\Phi = 0$); forgetting the $N$ for a coil; confusing flux with flux linkage.

### 2. Apply Faraday's law for magnitude of the induced e.m.f.

**Method:**
1. Work out the **change** in flux linkage: $\Delta(N\Phi) = N(\Phi_{\text{final}} - \Phi_{\text{initial}})$. If only $B$ changes, $\Delta(N\Phi) = NA\Delta B$; if only area or angle changes, vary that term.
2. Divide by the **time** over which the change happens: $E = \frac{\Delta(N\Phi)}{\Delta t}$. Use the **average** rate if the graph is curved — the tangent gives the instantaneous rate.
3. For a rotating coil: $\Phi = BA\cos\omega t$, so $E = BAN\omega\sin\omega t$; the e.m.f. is sinusoidal.

**Traps:** using the flux (or final flux linkage) instead of the **change** in flux linkage; using the time for one event as $\Delta t$ when the question gives a $\Phi$–$t$ graph (you need the gradient); forgetting $N$; mixing up Wb and Wb turns.

### 3. Deduce the direction of the induced e.m.f. or current (Lenz)

**Method:**
1. Identify whether the flux linkage **increases** or **decreases** (movement direction, field change).
2. Lenz: the induced current creates a field that **opposes the change** — so if $N\Phi$ increases, the induced field opposes $B$; if it decreases, the induced field aids $B$.
3. From the induced field direction, deduce the current direction (right-hand grip rule for a coil: fingers = current, thumb = field).
4. For a straight wire, use Fleming's **right-hand** rule: thu**M**b = **M**otion, **F**irst finger = **F**ield, se**C**ond finger = induced **C**urrent (conventional).

**Traps:** saying "opposes the motion" instead of "opposes the change in flux linkage" (one mark lost); using the left hand (motor rule) for a generator question; reversing Lenz (the induced field aids when the flux grows — backwards).

### 4. Use $E = Blv$ for a straight wire or rail

**Method:**
1. Check the wire moves **perpendicular** to both its own length and the field — then $E = Blv$; if the motion makes an angle $\theta$ to the field, $E = Blv\sin\theta$.
2. If the wire completes a circuit (e.g. slides on rails of resistance $R$), the induced current is $I = \frac{E}{R} = \frac{Blv}{R}$ and the mechanical force to oppose Lenz is $F = BIL = \frac{B^2l^2v}{R}$ (work per unit time equals electrical power).
3. For a wire at rest in a changing field, use Faraday's law directly — $Blv$ does not apply (there is no $v$).

**Traps:** applying $Blv$ when the field is changing but the wire is stationary (use $E = N\Delta\Phi/\Delta t$ instead); using the wire's total length instead of the length **in the field**; forgetting $\sin\theta$ when the motion is not perpendicular to the field.

### 5. Work with $\Phi$–$t$ and $E$–$t$ graphs

**Method:**
1. On a flux-linkage vs time graph, the **gradient** is $\frac{d(N\Phi)}{dt}$ and the **negative** of the gradient is the e.m.f.: $E = -\frac{d(N\Phi)}{dt}$.
2. When $N\Phi$ is a straight line, the gradient is constant so $E$ is constant; when $N\Phi = BAN\cos\omega t$ (sinusoidal), the $\Phi$–$t$ graph is a cosine and the $E$–$t$ graph is a **sine** ($\pi/2$ out of phase, zero when $\Phi$ is maximal).
3. Area under an $E$–$t$ graph (or $I$–$t$ graph times $R$) equals the change in flux linkage.

**Traps:** drawing $E$–$t$ in phase with $\Phi$–$t$ (they are $90°$ out of phase — the derivative); saying the e.m.f. is zero when the flux is at its rate of change maximum (backwards — e.m.f. is maximum when $\left|\frac{d\Phi}{dt}\right|$ is maximum, which is when $\Phi = 0$ for a sinusoid).

### 6. Rotating coil / generator questions

**Method:**
1. Write flux linkage as $N\Phi = BAN\cos\omega t$ where $\omega = 2\pi f$.
2. Differentiate: $E = -\frac{d}{dt}(BAN\cos\omega t) = BAN\omega\sin\omega t$, so peak $E_0 = BAN\omega$ and $E_{\text{rms}} = \frac{E_0}{\sqrt{2}}$ (link to Chapter 29).
3. The coil is maximum flux when its plane is perpendicular to the field; maximum e.m.f. when its plane is **parallel** to the field (flux zero, rate of change maximum).

**Traps:** confusing flux and e.m.f. maxima (they are $90°$ apart); forgetting to convert $f$ to $\omega = 2\pi f$; using the r.m.s. formula $E_0/\sqrt{2}$ without noting it applies only to the sinusoidal generator output.

### 7. Eddy currents and electromagnetic damping (explain questions)

**Method:**
1. State that the changing flux through the metal induces circulating eddy currents in the metal itself (Faraday).
2. By Lenz, the eddy-current field **opposes the change / motion** that produces them, so they exert a braking/damping force or dissipate $I^2R$ heat.
3. Give the application: e.g. electromagnetic braking (train between magnets), damping in a pivoted coil, heating in an induction furnace — and the remedy: **laminating** the core (thin insulated sheets) breaks up the eddy-current loops and reduces loss.

**Traps:** describing eddy currents as "current in the wires of the coil" (they are in the **solid metal** itself); omitting Lenz's "opposes the change" — that is the physics mark; saying laminations "reduce resistance" (they break up the current paths, not the resistance of the core material).

### 8. Explain questions: complete Faraday–Lenz answer structure

**Method:**
1. State Faraday: "magnitude of induced e.m.f. is proportional to rate of change of magnetic flux linkage, $E = N\Delta\Phi/\Delta t$."
2. Apply to the situation: identify what changes ($B$, $A$, $\theta$, $N$) and why the change produces an e.m.f.
3. State Lenz for direction: "direction opposes the change in flux linkage" and deduce the current direction (right-hand rule or induced-field argument).
4. Close with energy: "work is done against the opposing force, becoming electrical energy" (the Lenz sign ensures conservation of energy).

**Traps:** defining Faraday without "rate of change" or without "flux linkage" (loses one mark per omission); defining Lenz without "opposes the **change**" (the word "change" is compulsory); omitting the minus sign or Lenz when asked to include it ($E = -d(N\Phi)/dt$ is the **Faraday–Lenz** law, not just Faraday).

## 5. Solved Examples

Real exam-style questions from the end of Chapter 28 and from past 9702 papers, with their mark allocations. The format for every example: Question / Method / Answer / What the examiner wants.

### Example 1: Magnetic flux through a loop — End-of-chapter Q1, [1] + [2] marks

**Question:** A circular loop of area $28~\text{cm}^2$ is placed in a uniform magnetic field of flux density $0.038~\text{T}$. (a) Calculate the magnetic flux through the loop when the field is perpendicular to the plane of the loop. [1] (b) The loop is rotated through $90°$ so that the field is now parallel to the plane. What is the change in magnetic flux? [2]

**Method:**
1. (a) Field perpendicular to the plane means $B$ is parallel to the normal, so $\theta = 0$, $\cos\theta = 1$: $\Phi = BA$.
2. Convert: $A = 28~\text{cm}^2 = 28 \times 10^{-4}~\text{m}^2 = 2.8 \times 10^{-3}~\text{m}^2$.
3. $\Phi = 0.038 \times 2.8 \times 10^{-3} = 1.064 \times 10^{-4}~\text{Wb}$.
4. (b) Field in the plane means $B$ is $90°$ to the normal, $\cos90° = 0$, so $\Phi = 0$. The change is $|\Delta\Phi| = 1.064 \times 10^{-4}~\text{Wb}$ (flux linkage goes from max to zero).

**Answer:** (a) $\Phi = 1.1 \times 10^{-4}~\text{Wb}$ (2 s.f.). (b) $\Phi = 0$ in the new position; $|\Delta\Phi| = 1.1 \times 10^{-4}~\text{Wb}$.

**What the examiner wants:** the area in m$^2$ and the argument $\theta = 0$ vs $90°$ (or $\Phi = BA$ vs $\Phi = 0$) explicitly; the change is the difference, not the new flux alone.

### Example 2: Flux linkage of a coil — End-of-chapter Q2, [2] marks

**Question:** A coil of $120$ turns and area $15~\text{cm}^2$ is placed in a uniform magnetic field of flux density $0.025~\text{T}$ with the field perpendicular to the plane of the coil. Calculate the magnetic flux linkage through the coil.

**Method:**
1. Flux through one turn: $\Phi = BA = 0.025 \times (15 \times 10^{-4}) = 0.025 \times 1.5 \times 10^{-3} = 3.75 \times 10^{-5}~\text{Wb}$.
2. Flux linkage: $N\Phi = 120 \times 3.75 \times 10^{-5} = 4.5 \times 10^{-3}~\text{Wb turns}$.

**Answer:** $N\Phi = 4.5 \times 10^{-3}~\text{Wb turns}$.

**What the examiner wants:** the "$N$" in the answer and the unit "Wb turns" (or "Wb" credited but "Wb turns" preferred when $N$ is explicit). A flux-only answer loses the factor of $120$.

### Example 3: Induced e.m.f. when a magnet is moved — End-of-chapter Q3, [3] marks

**Question:** The flux linkage through a coil of $200$ turns changes from $1.2 \times 10^{-3}~\text{Wb}$ to $0.4 \times 10^{-3}~\text{Wb}$ in $0.050~\text{s}$ as a magnet is pulled away. Calculate the magnitude of the average induced e.m.f.

**Method:**
1. $\Delta(N\Phi) = (0.4 - 1.2) \times 10^{-3} = -0.80 \times 10^{-3}~\text{Wb}$; magnitude $0.80 \times 10^{-3}$ (the "$N$" is already in the given $N\Phi$, so do not multiply by $200$ again).
2. Alternatively from the $N\Phi$ change: if the given values were $N\Phi$, $E = \frac{|\Delta(N\Phi)|}{\Delta t}$; if they were $\Phi$, use $E = \frac{N\Delta\Phi}{\Delta t}$. The coursebook gives this as a flux-linkage change, so $E = \frac{0.80 \times 10^{-3}}{0.050}$.
3. $E = \frac{0.80 \times 10^{-3}}{0.050} = 1.6 \times 10^{-2}~\text{V}$.

**Answer:** $E = 1.6 \times 10^{-2}~\text{V}$ ($16~\text{mV}$).

**What the examiner wants:** recognising whether the numbers given are $\Phi$ or $N\Phi$ (if $\Phi$, multiply by $N$; if $N\Phi$, do not). The trap variant gives $\Phi$ and $N$ separately — then $E = N\Delta\Phi/\Delta t$.

### Example 4: Sliding wire on rails — $E = Blv$ — End-of-chapter Q4, [3] + [1] marks

**Question:** A metal rod of length $0.15~\text{m}$ slides at $2.0~\text{m s}^{-1}$ on conducting rails through a uniform field $B = 0.30~\text{T}$ directed perpendicular to the rod and to its motion. The circuit resistance is $4.0~\Omega$. (a) Calculate the induced e.m.f. between the ends of the rod. [2] (b) Calculate the induced current. [1] (c) What is the direction of the current (use the right-hand rule)? [1]

**Method:**
1. (a) $E = Blv = 0.30 \times 0.15 \times 2.0 = 0.090~\text{V}$.
2. (b) $I = \frac{E}{R} = \frac{0.090}{4.0} = 2.25 \times 10^{-2}~\text{A}$.
3. (c) Right-hand rule: motion × field gives current direction across the rod; the return path through the rails completes the loop, so the current circulates (clockwise or anticlockwise depending on the $B$ direction given in the diagram).

**Answer:** (a) $0.090~\text{V}$. (b) $23~\text{mA}$ (2 s.f.). (c) direction given by the right-hand rule — thumb = motion, first finger = field, second finger = induced current along the rod.

**What the examiner wants:** $E = Blv$ must be stated (derived from Faraday if the mark scheme is strict); the length is the length **in the field** ($0.15~\text{m}$, not the rail separation unless they coincide); direction via the right hand with all three assignments.

### Example 5: $\Phi$–$t$ graph to $E$–$t$ graph — End-of-chapter Q5, [4] marks

**Question:** The graph shows magnetic flux linkage $N\Phi$ (Wb turns) against time $t$ (s) for a coil. The curve is sinusoidal, $N\Phi = 3.0 \times 10^{-3}\cos(100\pi t)$. Sketch the induced e.m.f. $E$ (V) against $t$, marking the peak value and period.

**Method:**
1. $E = -\frac{d(N\Phi)}{dt} = -\frac{d}{dt}[3.0 \times 10^{-3}\cos(100\pi t)] = 3.0 \times 10^{-3} \times 100\pi\sin(100\pi t)$.
2. Peak: $E_0 = 3.0 \times 10^{-3} \times 100\pi = 0.30\pi \approx 0.94~\text{V}$.
3. Period: $\omega = 100\pi$, so $T = \frac{2\pi}{\omega} = \frac{2\pi}{100\pi} = 0.020~\text{s}$.
4. The $E$–$t$ graph is a **sine** (shifted $90°$ from the cosine $N\Phi$–$t$ graph), zero when $N\Phi$ is maximum, maximum when $N\Phi$ is zero (maximum rate of change).

**Answer:** sinusoidal $E$–$t$ with period $0.020~\text{s}$, peak $\approx 0.94~\text{V}$, $90°$ ($\pi/2$) out of phase with the $N\Phi$–$t$ graph (zero at the $N\Phi$ maxima).

**What the examiner wants:** the derivative relation ($E = -d(N\Phi)/dt$) stated; the peak value from $N\Phi\,\omega$; the correct period $T = 2\pi/\omega$; and the $90°$ phase shift (the most examined point in this graph pair — they are **not** in phase).

### Example 6: Lenz direction — magnet approaching a coil — End-of-chapter Q6, [3] marks

**Question:** A bar magnet's N pole is pushed towards one end of a coil. Explain the direction of the induced current in the coil.

**Method:**
1. As the N pole approaches, the flux linkage into the coil **increases** in the direction of the magnet's field.
2. Lenz: the induced current's field **opposes the increase**, so it creates a field running **away** from the incoming N pole — the near end of the coil becomes an N pole too.
3. Repulsion is felt on the magnet (energy is required to push it — that work becomes the electrical energy). For the opposite pole, or removal, the induced field aids the diminishing flux (the near end becomes S, attracting the receding N).

**Answer:** near end becomes N; induced current circulates to put its field opposite the approaching field (Lenz: opposes the increase in flux linkage). The force on the magnet is repulsive, so work is done.

**What the examiner wants:** "opposes the **change in / increase in** flux linkage" (not just "opposes the motion"); the induced field direction; and the consequence that the near end is the same polarity as the approaching pole (N–N repulsion). "Opposes the magnet" without flux earns at most 1 mark.

### Example 7: Rotating coil — peak e.m.f. — End-of-chapter Q7, [2] + [2] marks

**Question:** A rectangular coil of $N = 100$ turns, area $A = 0.020~\text{m}^2$, rotates at $f = 50~\text{Hz}$ in a uniform field $B = 0.10~\text{T}$. (a) State the expression for the flux linkage as a function of time. [1] (b) Calculate the peak induced e.m.f. [2]

**Method:**
1. (a) $N\Phi = BAN\cos\omega t$, where $\omega = 2\pi f = 100\pi~\text{rad s}^{-1}$.
2. (b) Peak when $\sin\omega t = 1$: $E_0 = BAN\omega = 100 \times 0.10 \times 0.020 \times 100\pi = 20\pi \approx 62.8~\text{V}$. Or via $E_0 = 2\pi f\,BAN$.

**Answer:** (a) $N\Phi = 100 \times 0.10 \times 0.020\cos(100\pi t) = 0.20\cos(100\pi t)~\text{Wb turns}$. (b) $E_0 \approx 63~\text{V}$.

**What the examiner wants:** the $N$ in the flux-linkage expression; $\omega = 2\pi f$, not $\omega = f$; the peak at $\sin$, not the flux at $\cos$.

### Example 8: Search coil in a changing field — End-of-chapter Q8, [4] marks

**Question:** A search coil of $N = 500$ turns, area $4.0 \times 10^{-4}~\text{m}^2$, is placed in a field $B = 0.060~\text{T}$ perpendicular to the coil face. The field is then reduced uniformly to zero in $0.12~\text{s}$. Calculate (a) the change in flux linkage [2] and (b) the average induced e.m.f. [2].

**Method:**
1. (a) $\Phi = BA = 0.060 \times 4.0 \times 10^{-4} = 2.4 \times 10^{-5}~\text{Wb}$ per turn. Flux linkage $N\Phi = 500 \times 2.4 \times 10^{-5} = 1.2 \times 10^{-2}~\text{Wb turns}$. Going to zero, $|\Delta(N\Phi)| = 1.2 \times 10^{-2}$.
2. (b) $E = \frac{\Delta(N\Phi)}{\Delta t} = \frac{1.2 \times 10^{-2}}{0.12} = 0.10~\text{V}$.

**Answer:** (a) $1.2 \times 10^{-2}~\text{Wb turns}$. (b) $0.10~\text{V}$.

**What the examiner wants:** $N\Phi$ not just $\Phi$; the change (final $-$ initial, or magnitude) divided by time. A flux-only answer is a factor-of-$N$ error.

### Example 9: Eddy-current braking (explain) — End-of-chapter Q9, [3] marks

**Question:** Explain why a copper plate moving between the poles of a strong magnet is rapidly brought to rest (electromagnetic braking).

**Method:**
1. As the leading edge enters the field, the flux through the plate increases; at the trailing edge it decreases — both changes induce **circulating eddy currents** in the plate (Faraday).
2. By Lenz, the eddy-current field **opposes the change**, so the currents at both edges produce a force that **opposes the motion** of the plate.
3. The eddy currents dissipate $I^2R$ heat in the plate, converting kinetic energy to thermal energy until the plate stops.

**Answer:** changing flux through the moving plate → induced eddy currents → by Lenz they oppose the motion → braking force → kinetic energy → heat.

**What the examiner wants:** "eddy currents induced in the plate" + "Lenz: oppose the change / motion" + "energy dissipated as heat / kinetic → thermal" for three marks. Omitting Lenz loses the middle mark.

### Example 10: Induced e.m.f. at an angle — End-of-chapter Q10, [3] marks

**Question:** A coil of area $6.0 \times 10^{-3}~\text{m}^2$ with $N = 250$ turns is rotated so that its plane makes an angle of $30°$ to the magnetic field $B = 0.040~\text{T}$. Calculate the flux linkage through the coil when the normal to the coil makes $60°$ to the field, and state what angle gives maximum flux linkage.

**Method:**
1. Normal at $60°$ to $B$: $N\Phi = BAN\cos 60° = 250 \times 0.040 \times 6.0 \times 10^{-3} \times 0.5$.
2. $BAN = 250 \times 0.040 \times 6.0 \times 10^{-3} = 0.060~\text{Wb turns}$; times $0.5$ gives $0.030~\text{Wb turns}$.
3. Maximum when the normal is **parallel** to the field ($\theta = 0$, coil plane perpendicular to $B$), where $\cos\theta = 1$ and $N\Phi = BAN = 0.060~\text{Wb turns}$. Minimum (zero) when the field is in the plane ($\theta = 90°$).

**Answer:** $N\Phi = 3.0 \times 10^{-2}~\text{Wb turns}$ at $60°$; maximum at $\theta = 0°$ (normal parallel to $B$).

**What the examiner wants:** the "$\cos\theta$" with $\theta$ to the **normal** (the most examined angle error) and maximum at $0°$, minimum at $90°$.

## 6. Cheat Sheet

**The one-page summary — everything you must have in your head before the exam.**

**Flux & flux linkage**
- $\Phi = BA\cos\theta$ — $B$ in T, $A$ in m$^2$, $\theta$ between field and **normal** to area; unit: Wb = T m$^2$.
- $N\Phi = BAN\cos\theta$ — $N$ turns; flux linkage = $N \times$ flux; unit: Wb turns.
- Max flux linkage when normal is parallel to $B$ ($0°$); zero when field is in the plane ($90°$).

**Faraday + Lenz**
- Faraday magnitude: $E = \frac{\Delta(N\Phi)}{\Delta t}$ — **rate of change** of flux linkage, not flux itself.
- Faraday–Lenz with sign: $E = -\frac{d(N\Phi)}{dt}$ — minus = Lenz (opposes the **change** in $N\Phi$).
- $E$ is maximum when $\left|\frac{d(N\Phi)}{dt}\right|$ is maximum (not when $N\Phi$ is maximum — $90°$ apart for a sinusoid).

**Straight wire**
- $E = Blv$ — $l$ in field, $v$ perpendicular to both field and wire; if $v$ at $\theta$ to field, $E = Blv\sin\theta$; parallel gives $0$.
- If the wire slides on rails of resistance $R$, $I = \frac{Blv}{R}$ and opposing force $F = BIL = \frac{B^2l^2v}{R}$.

**Rotating coil / generator**
- $N\Phi = BAN\cos\omega t$, $E = BAN\omega\sin\omega t$, peak $E_0 = BAN\omega$, $\omega = 2\pi f$.

**Direction**
- Straight wire: Fleming's **right-hand** rule — thu**M**b = **M**otion, **F**irst finger = **F**ield, se**C**ond finger = induced **C**urrent (conventional).
- Coil: Lenz → induced field **opposes the change** in $N\Phi$ (not just "opposes the motion"); induced pole is same polarity as approaching pole (repulsion = work input).

**Applications**
- **Eddy currents:** circulating currents in solid metal from changing flux → Lenz braking → $I^2R$ heat; laminating breaks them up.
- **Generator:** coil rotating in field → alternating $E$ as above; e.m.f. max when coil plane is parallel to field.

## 7. Common Exam Mistakes

**1. Using flux where you need flux linkage.** The exam gives $N$ and asks for an e.m.f. — forgetting the $N$ costs the mark. Always decide: one turn → $\Phi$; $N$ turns → $N\Phi = BAN\cos\theta$.

**2. Forgetting "rate of change."** Faraday's law is "$E$ proportional to the **rate of change** of flux linkage" — writing "$E$ proportional to flux linkage" alone earns zero. The word "rate of change" is compulsory.

**3. Angle to the wrong reference.** In $\Phi = BA\cos\theta$, $\theta$ is to the **normal**, not to the plane. If the question says "field makes $30°$ to the plane," $\theta = 60°$ in the formula. Field in the plane gives $\Phi = 0$, not $BA$.

**4. Applying $Blv$ when the wire is stationary.** $Blv$ is for a wire **moving** through a uniform field. If the field changes but the wire is fixed, use $E = N\Delta\Phi/\Delta t$ instead. Mixing the two is the most common method error in this chapter.

**5. Lenz without "change."** "The induced e.m.f. opposes the magnetic field" or "opposes the motion" alone loses the mark. The opposed thing is the **change in flux linkage** — that phrase must appear. Without it the answer reads as if the flux itself is opposed.

**6. Using the left hand for a generator.** Fleming's left-hand rule is the **motor** rule (current → force). For **generation** (motion → current) you must use the **right hand**. Using the wrong hand gives the current the opposite direction and earns zero on a direction question.

**7. Confusing flux and rate-of-change maxima.** For a rotating coil or a sinusoidal $\Phi$–$t$ graph, $N\Phi$ is maximum when its rate of change is zero, and vice versa. So the e.m.f. ($-\frac{d(N\Phi)}{dt}$) peaks when the flux is zero. Swapping them is a standard 2-mark loss on graph questions — the two curves are $90°$ ($π/2$) out of phase.

**8. Unit and conversion slips.** Area given in cm$^2$ → must be m$^2$ ($\times 10^{-4}$); turns used as an extra factor when the given value is already $N\Phi$ (double-counting $N$); Wb turns confused with Wb (unit mark lost); $B = 2.0 \times 10^{-7}\frac{I}{x}$ (from Chapter 26) mixed into Faraday questions — they are separate chapters.
