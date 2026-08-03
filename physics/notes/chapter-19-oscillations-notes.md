# Chapter 19: Oscillations - CAIE A Level Physics (9702) Study Notes

This chapter is A2 content. In the current syllabus it is topic **17 (Oscillations)** with three sub-topics: 17.1 Simple harmonic oscillations, 17.2 Energy in simple harmonic motion, 17.3 Damped and forced oscillations, resonance. It is examined on **Paper 1 (MCQ) and Paper 4 (structured questions, typically 8 - 10 marks)**. You get three SHM formulas in the exam data booklet, everything else you must recall or derive (see Section 3).

---

## 1. Theory

### 1.1 Oscillations, free and forced

An **oscillation** is a repeated back-and-forth motion about an **equilibrium position** (the position the object returns to when the oscillation stops; the resultant force there is zero).

- **Free oscillation:** the object oscillates on its own after an initial disturbance, at its **natural frequency** $f_0$ (e.g. a plucked guitar string, a pendulum after being released). No external periodic force acts once it is released.
- **Forced oscillation:** an external periodic force drives the object, so it oscillates at the **driving frequency** of the force, not its own natural frequency (e.g. your body vibrating on a bus, a loudspeaker cone driven by a signal generator, a building shaken by an earthquake).

Every oscillator has a natural frequency, the frequency with which it vibrates freely after a disturbance. Changing the oscillator (length of a string, mass on a spring) changes its natural frequency.

### 1.2 The vocabulary of oscillations

- **Displacement $x$** (m): the distance of the oscillator from its equilibrium position at an instant. It is a vector; one side is taken as positive, the other negative. It varies between $+x_0$ and $-x_0$.
- **Amplitude $x_0$** (m): the maximum displacement from the equilibrium position. It is always positive.
- **Period $T$** (s): the time for one complete oscillation (from one side to the other and back again, or any equivalent point in the cycle). One complete oscillation = one full cycle.
- **Frequency $f$** (Hz): the number of complete oscillations per unit time.
- **Angular frequency $\omega$** (rad s$^{-1}$): the rate of change of phase. One complete cycle corresponds to a phase change of $2\pi$ rad, so:

$$f = \frac{1}{T}, \qquad \omega = 2\pi f = \frac{2\pi}{T}, \qquad T = \frac{2\pi}{\omega}$$

- **Phase:** the point an oscillator has reached within its cycle, usually measured in radians from 0 to $2\pi$ (or degrees 0 to 360). During one complete cycle the phase changes by $2\pi$ rad.
- **Phase difference:** how far out of step two oscillations are, measured as a fraction of an oscillation, or in degrees, or in radians. One whole oscillation = 1 = $360^\circ$ = $2\pi$ rad. Two oscillations are **in phase** when they reach corresponding points at the same time (phase difference 0). They are **in antiphase** when the phase difference is half an oscillation ($180^\circ$, $\pi$ rad). To find the phase difference from two graphs: measure the time gap $t$ between corresponding points, then

$$\text{phase difference} = \frac{t}{T} \text{ of an oscillation} = \frac{t}{T} \times 360^\circ = \frac{t}{T} \times 2\pi \text{ rad}$$

### 1.3 SHM - the definition

**Definition (learn it word for word, it is a 2-mark question):**

> A body executes simple harmonic motion if its acceleration is directly proportional to its displacement from its equilibrium position, and is always directed towards that equilibrium position (i.e. in the opposite direction to the displacement).

In equation form:

$$a = -\omega^2 x$$

- The proportionality constant is $\omega^2$, the square of the angular frequency.
- The **minus sign** means acceleration and displacement are always in opposite directions; the acceleration is always directed back towards the equilibrium position. If there were no minus sign, the acceleration would push the object further away and it would never return.

The three requirements for a mechanical system to show SHM:

1. There is a **mass** that oscillates.
2. There is a position where the mass is in **equilibrium** (resultant force zero).
3. There is a **restoring force** that is directly proportional to the displacement from equilibrium and directed towards it. Since $F = ma$, $F \propto x$ gives $a \propto x$.

**Checking whether something is SHM (the standard 2-mark method):** write the acceleration in the form $a = -(\text{constant}) \times x$, then state: "the acceleration is proportional to the displacement, and the minus sign shows it is directed towards the equilibrium position / opposite to the displacement." This is exactly what the mark schemes want.

**Isochronous property:** for a simple harmonic oscillator, the period (and frequency) is **independent of the amplitude**. This is why a pendulum keeps steady time in a clock even as the swing gets smaller.

### 1.4 Equations of SHM

Displacement as a function of time (a solution of $a = -\omega^2 x$):

$$x = x_0 \sin \omega t \qquad \text{(motion starts at equilibrium, } x = 0 \text{ at } t = 0)$$

$$x = x_0 \cos \omega t \qquad \text{(motion starts at maximum displacement, } x = x_0 \text{ at } t = 0)$$

Both describe the same kind of motion; the difference is only where in the cycle $t = 0$ is taken. **Always use the sine form when the oscillator passes through equilibrium at $t = 0$, and the cosine form when it is released from rest at maximum displacement at $t = 0$.**

Velocity:

$$v = v_0 \cos \omega t, \qquad \text{where } v_0 = \omega x_0$$

$$v = \pm \omega \sqrt{x_0^2 - x^2}$$

- $v_0 = \omega x_0$ is the **maximum speed**, occurring at the equilibrium position ($x = 0$). The $\pm$ sign shows direction.
- $v_{\max} \propto x_0$ (bigger amplitude, faster at the centre) and $v_{\max} \propto \omega$ (higher frequency, faster at the centre).

Acceleration:

$$a = -\omega^2 x, \qquad a_{\max} = \omega^2 x_0$$

Maximum acceleration occurs at the extremes of the motion ($x = \pm x_0$); acceleration is zero at equilibrium.

**Critical calculator rule: in $\sin \omega t$ and $\cos \omega t$ the argument $\omega t$ is in RADIANS. Put your calculator in radian mode before any of these calculations.** (A classic trap, see Section 7.)

### 1.5 Graphs of SHM and phase

For motion $x = x_0 \sin \omega t$:

| Quantity | Graph shape | Value at $t = 0$ | Max value | Where the max occurs |
|---|---|---|---|---|
| Displacement $x$ | sine | 0 | $x_0$ | $t = T/4$, $3T/4$ |
| Velocity $v$ | cosine | $+v_0$ | $v_0 = \omega x_0$ | $t = 0$, $T/2$ (equilibrium) |
| Acceleration $a$ | negative sine | 0 | $\omega^2 x_0$ | $t = T/4$, $3T/4$ (extremes) |

Phase relationships you must know:

- **Velocity leads displacement by $90^\circ$ ($\pi/2$ rad).** Velocity is a maximum when displacement is zero, and zero when displacement is a maximum.
- **Acceleration is $180^\circ$ ($\pi$ rad) out of phase with displacement** (antiphase): the acceleration graph is the displacement graph turned upside down. Whenever $x$ is positive, $a$ is negative, and vice versa.
- **Acceleration leads velocity by $90^\circ$ ($\pi/2$ rad).**

How the graphs link:

- Velocity at any time = gradient of the $x$-$t$ graph: $v = \frac{\Delta x}{\Delta t}$.
- Acceleration at any time = gradient of the $v$-$t$ graph: $a = \frac{\Delta v}{\Delta t}$.
- Reading these gradients is a standard exam skill, both numerically (tangent method) and by shape (a sine graph differentiates to a cosine graph, etc.).

Key graph-reading facts:

- Amplitude $x_0$ = peak value of the $x$-$t$ graph.
- Period $T$ = time between two successive identical points (e.g. peak to peak) on any of the three graphs.
- Maximum velocity = peak of the $v$-$t$ graph = $\omega x_0$.
- Maximum acceleration = peak of the $a$-$t$ graph = $\omega^2 x_0$.
- The $a$-$x$ graph for SHM is a **straight line through the origin with negative gradient $-\omega^2$**. Its gradient is independent of amplitude. If the exam shows you an $a$-$x$ graph, the gradient gives you $\omega^2$ directly, and $\omega^2$ gives you $f$ and $T$.

### 1.6 Energy in SHM

During SHM there is a continuous interchange between **kinetic energy** (of the moving mass) and **potential energy** (stored in the system: elastic potential energy for a spring, gravitational potential energy for a pendulum).

- At equilibrium ($x = 0$): KE is maximum, PE is zero, speed is $v_0 = \omega x_0$.
- At the extremes ($x = \pm x_0$): KE is zero, PE is maximum, speed is zero.
- For an **undamped** oscillator the total energy stays constant; all loss is ignored.

Total energy (syllabus formula):

$$E = \frac{1}{2} m \omega^2 x_0^2$$

Useful derived forms (build them from $v^2 = \omega^2 (x_0^2 - x^2)$):

$$E_K = \frac{1}{2} m v^2 = \frac{1}{2} m \omega^2 (x_0^2 - x^2), \qquad E_P = E - E_K = \frac{1}{2} m \omega^2 x^2$$

So the total energy can also be written as the maximum KE or the maximum PE:

$$E = \frac{1}{2} m v_0^2 = \frac{1}{2} m \omega^2 x_0^2$$

Key facts about energy graphs:

- **Total energy is proportional to amplitude squared: $E \propto x_0^2$.** Doubling the amplitude quadruples the total energy. Halving the input energy reduces the amplitude by a factor of $1/\sqrt{2}$.
- On an energy-time graph: KE and PE each complete **two cycles during one period** of the oscillation (KE peaks twice per cycle: once moving left through the centre, once moving right). Their sum (the total) is a horizontal line.
- On an energy-displacement graph: PE is a parabola with its maximum at $x = \pm x_0$ and minimum at $x = 0$; KE is the inverted parabola (maximum at $x = 0$). At any $x$ the two add to the same constant.

### 1.7 Period of a mass-spring system and a pendulum

**Mass on a spring (or tethered trolley).** For a single spring obeying $F = -kx$:

$$F = ma = -kx \Rightarrow a = -\frac{k}{m} x$$

Comparing with $a = -\omega^2 x$ gives $\omega^2 = \frac{k}{m}$, so

$$T = 2\pi \sqrt{\frac{m}{k}}$$

- $m$ is the oscillating mass (kg), $k$ is the spring constant (N m$^{-1}$).
- For two identical springs in parallel (e.g. a trolley tethered between two springs, both always extended) the effective constant is $2k$, so $a = -\frac{2k}{m} x$ and $\omega = \sqrt{\frac{2k}{m}}$. Watch for this in exams.
- $T$ is independent of the amplitude and independent of $g$.

**Simple pendulum (small angles only).** For small oscillations the restoring force is proportional to displacement, giving

$$T = 2\pi \sqrt{\frac{l}{g}}$$

- $l$ is the length from the point of suspension to the centre of mass of the bob (m), $g = 9.81$ m s$^{-2}$.
- Valid only for small amplitudes (typically less than about $10^\circ$), where $\sin \theta \approx \theta$.
- $T$ is independent of the mass of the bob and independent of the amplitude (for small angles).

**Neither period formula is in the exam data booklet.** You must be able to recall them or derive them quickly by writing $a = -\omega^2 x$ with the correct expression for the acceleration.

### 1.8 Damping

**Damping** is the removal of energy from an oscillating system by resistive forces (friction, air resistance, eddy currents). As energy is lost, the **amplitude and the maximum speed decrease** with time. For light damping the amplitude decays exponentially, so the graph of displacement against time shows a sine curve inside a decaying exponential envelope. The **period/frequency is essentially unchanged** by light damping.

Three types (syllabus terms: light, critical, heavy):

| Type | What happens | Displacement-time graph |
|---|---|---|
| **Light (under-) damping** | Oscillator makes many oscillations; amplitude decays gradually (exponentially); period roughly unchanged | Oscillating curve with slowly shrinking envelope; it keeps crossing zero many times |
| **Critical damping** | The minimum damping needed to return to equilibrium **without oscillating**, in the shortest possible time | Curve falls smoothly to zero, touches it, does not cross; no overshoot |
| **Heavy (over-) damping** | Oscillator returns to equilibrium slowly, without oscillating, taking longer than critical | Curve falls smoothly to zero but very slowly, no overshoot |

Uses: car suspension systems are (close to) **critically damped** so the car returns smoothly to its ride height after a bump without bouncing; door closers are critically damped; instruments with moving needles are critically damped so the needle settles quickly without oscillating.

Causes of damping that appear in mark schemes: air resistance, friction between moving parts (e.g. wheels on a surface), and (for a metal sheet oscillating in a magnetic field) **induced eddy currents** which dissipate energy. A complete answer is two ideas: the oscillator **loses energy** and the energy loss is **due to resistive forces**. (See the real question in Example 10 of Section 5.)

### 1.9 Forced oscillations and resonance

- **Natural frequency $f_0$:** the frequency at which a system oscillates when it is free (after a disturbance, with no driving force).
- **Forced oscillation:** a periodic driving force makes the system oscillate at the **driving frequency** $f$, whatever that is.
- **Resonance:** the amplitude of the forced oscillation is **maximum** when the driving frequency equals the natural frequency of the system ($f = f_0$). At resonance the system absorbs the greatest possible energy from the driver.

$$f = f_0 \Rightarrow \text{amplitude maximum} \Rightarrow \text{maximum energy transfer}$$

**Definition of resonance (2-mark phrasing used by Cambridge):** "oscillation of the system at maximum amplitude when the driving frequency is equal to the natural frequency of the system."

**The resonance curve** (amplitude against driving frequency): a curve that rises to a sharp peak at $f = f_0$ and falls away on both sides. As the amplitude of the driving force increases, the whole curve scales up.

**Effect of damping on the resonance curve:** as damping increases, the maximum (resonant) amplitude decreases, the peak becomes broader, and the resonant frequency becomes slightly lower (the peak shifts to a slightly lower frequency).

**Resonance as a problem:** the Millennium Footbridge, London (pedestrians walking in step drove the bridge at its natural frequency); buildings in earthquakes (ground vibrations match a building's natural frequency); soldiers breaking step when crossing a bridge; wind causing a bridge or mast to oscillate. Solutions: damping, changing the natural frequency, avoiding the driving frequency.

**Resonance as useful:** pushing a child on a swing (small pushes timed to the natural frequency build a large amplitude); tuning a radio or TV (the circuit resonates at the selected station's frequency); microwave ovens (microwaves match a natural vibration frequency of water molecules, which absorb the energy and heat the food); MRI/NMR (radio waves at the natural frequency of protons, which absorb energy); musical instruments (air column/body resonates at the played note).

**Exam reality check:** the definition of SHM ("acceleration proportional to displacement, in the opposite direction"), reading graphs, and the $\omega = 2\pi f$ relationships are the most frequently examined ideas. Damping and resonance appear as "state and explain" questions worth 2 - 4 marks almost every session.

---

## 2. Definition Sheet

Learn every definition below word-perfect. The ones with a mark-scheme quote attached are the exact phrasing Cambridge awards marks for - both halves are needed.

**Oscillation:** a repeated back-and-forth motion about an equilibrium position.

**Displacement $x$ (m):** the distance of the oscillator from its equilibrium position at an instant. It is a vector: one side is taken as positive, the other negative.

**Amplitude $x_0$ (m):** the maximum displacement from the equilibrium position. It is always positive.

**Period $T$ (s):** the time for one complete oscillation (one full cycle).

**Frequency $f$ (Hz):** the number of complete oscillations per unit time.

**Angular frequency $\omega$ (rad s$^{-1}$):** the rate of change of phase. One complete cycle corresponds to a phase change of $2\pi$ rad, so $\omega = 2\pi f = \frac{2\pi}{T}$.

**Simple harmonic motion (SHM):**

> A body executes simple harmonic motion if its acceleration is directly proportional to its displacement from its equilibrium position, and is always directed towards that equilibrium position (in the opposite direction to the displacement).

Mark-scheme split: (1) "acceleration proportional to displacement" and (2) "directed towards the fixed point" / "acceleration and displacement in opposite directions". **Both ideas are required for full marks** (9702/42/M/J/18 Q4(a)). Do not write "the force is proportional to displacement" - the definition is about acceleration.

**Phase difference:** how far out of step two oscillations are, measured as a fraction of an oscillation, or in degrees, or in radians. In phase = phase difference 0 (corresponding points at the same time); in antiphase = half an oscillation ($180^\circ$, $\pi$ rad).

**Damping:** the removal of energy from an oscillating system by resistive forces. Mark-scheme phrasing: the oscillator "loses energy" (1) "due to resistive forces" (1) (9702/42/F/M/21 Q9(c)).

- **Light damping:** many oscillations; amplitude decays gradually (exponentially); period essentially unchanged.
- **Critical damping:** the minimum damping needed to return to equilibrium **without oscillating**, in the shortest possible time.
- **Heavy damping:** a slow return to equilibrium without oscillating, taking longer than critical damping.

**Free oscillation:** oscillation of a system on its own after an initial disturbance, at its natural frequency, with no external periodic force acting once released.

**Forced oscillation:** oscillation driven by an external periodic force, so the system oscillates at the driving frequency of that force (not its natural frequency).

**Natural frequency:** the frequency at which a system oscillates when it is free (after a disturbance, with no driving force).

**Resonance:**

> Oscillation of a system at maximum amplitude when the driving frequency is equal to the natural frequency of the system.

Mark-scheme split: (1) "oscillation (of object) at maximum amplitude" and (2) "when driving frequency = natural frequency (of system)" (9702/43/M/J/24 Q4(a)). At resonance the system absorbs the greatest possible energy from the driver.

---

## 3. Formula Sheet

| Formula | Meaning of symbols | SI units | When to use |
|---|---|---|---|
| $f = \dfrac{1}{T}$ | $f$ frequency, $T$ period | Hz, s | Converting between frequency and period |
| $\omega = 2\pi f = \dfrac{2\pi}{T}$ | $\omega$ angular frequency | rad s$^{-1}$ | Getting $\omega$ from $f$ or $T$ (needed for all SHM equations) |
| $x = x_0 \sin \omega t$ | $x$ displacement at time $t$, $x_0$ amplitude | m, s, rad s$^{-1}$ | Displacement when motion starts at equilibrium ($x = 0$ at $t = 0$) |
| $x = x_0 \cos \omega t$ | as above | m, s, rad s$^{-1}$ | Displacement when motion starts at max displacement ($x = x_0$ at $t = 0$) |
| $x = x_0 \sin(\omega t + \phi)$ | $\phi$ phase constant (where in the cycle $t = 0$ is taken) | m, s, rad s$^{-1}$ | General form when the motion starts part-way through the cycle |
| $a = -\omega^2 x$ | $a$ acceleration, $x$ displacement | m s$^{-2}$, m | The defining equation of SHM; acceleration at any displacement |
| $v = v_0 \cos \omega t$ | $v$ velocity, $v_0$ max velocity | m s$^{-1}$ | Velocity as a function of time (starts at max velocity) |
| $v = \pm \omega \sqrt{x_0^2 - x^2}$ | as above | m s$^{-1}$ | Velocity at a given displacement $x$ (no time needed) |
| $v_0 = \omega x_0$ | $v_0$ max speed | m s$^{-1}$ | Maximum speed (at equilibrium) |
| $a_{\max} = \omega^2 x_0$ | $a_{\max}$ max acceleration | m s$^{-2}$ | Maximum acceleration (at extremes); then $F_{\max} = ma_{\max}$ |
| $E = \frac{1}{2} m \omega^2 x_0^2$ | $E$ total energy, $m$ mass | J, kg | Total energy of SHM (syllabus formula) |
| $E_K = \frac{1}{2} m \omega^2 (x_0^2 - x^2)$ | $E_K$ kinetic energy | J | KE at a given displacement |
| $E_P = \frac{1}{2} m \omega^2 x^2$ | $E_P$ potential energy | J | PE at a given displacement |
| $T = 2\pi \sqrt{\dfrac{m}{k}}$ | $m$ mass on spring, $k$ spring constant | s, kg, N m$^{-1}$ | Period of a mass-spring system (not in the data booklet) |
| $T = 2\pi \sqrt{\dfrac{l}{g}}$ | $l$ pendulum length, $g$ gravitational field strength | s, m, m s$^{-2}$ | Period of a simple pendulum, small angles (not in the data booklet) |
| phase diff $= \dfrac{t}{T} \times 360^\circ$ or $\times 2\pi$ | $t$ time gap between corresponding points, $T$ period | rad or degrees | Phase difference between two oscillations from graphs |
| $E \propto x_0^2$ | energy vs amplitude | - | Comparing energies when amplitude changes |

**Data booklet check:** the booklet gives you only $a = -\omega^2 x$, $v = v_0 \cos \omega t$ and $v = \pm \omega \sqrt{x_0^2 - x^2}$. Everything else in this table must be recalled or derived.

---

## 4. Methods (Question Types & Methods)

### Type 1: "State the conditions for / define simple harmonic motion" (2 marks)

Method:

1. Write: "the acceleration is directly proportional to the displacement from the equilibrium position".
2. Add the direction: "and is directed towards the equilibrium position" OR "acceleration and displacement are in opposite directions".

That is the whole mark scheme. If asked for "two conditions", one mark is the proportionality, the other is the direction. Do not write "the force is proportional to displacement" without mentioning acceleration, and do not write "the acceleration is constant" (it is not).

### Type 2: "State the significance of the minus sign in $a = -\omega^2 x$" (1 mark)

Answer: "acceleration and displacement are in opposite directions" (acceleration is always directed towards the equilibrium position).

### Type 3: "Use the expression $a = -(\text{constant})x$ to explain why the motion is SHM" (2 marks)

Method:

1. Point out that everything multiplying $x$ (e.g. $\frac{c}{ML^3}$ or $\frac{A\rho g}{M}$) is constant, so $a \propto x$ (acceleration is proportional to displacement).
2. Point out that the minus sign shows the acceleration is in the opposite direction to the displacement (directed towards the equilibrium position).

### Type 4: "State and justify whether X undergoes SHM" (1 - 2 marks each)

Method: test the three requirements. Is there a restoring force? Is it proportional to displacement and directed towards equilibrium? If any requirement fails, it is not SHM. Examples from the coursebook: a basketball being bounced (not SHM: between bounces it is in free fall with constant acceleration; during contact the forces are impulsive, not proportional to displacement); a guitar string (SHM for small vibrations: the restoring force is proportional to displacement); a pendulum (SHM for small angles only); a person on a trampoline (not SHM: their feet lose contact, so there is no restoring force proportional to displacement for part of the cycle).

### Type 5: "Calculate the displacement at a given time" (2 - 3 marks)

Method:

1. Choose sine or cosine from the starting condition (equilibrium at $t = 0$: sine; released from max displacement at $t = 0$: cosine).
2. Find $\omega$ from $f$ or $T$: $\omega = 2\pi f = \frac{2\pi}{T}$.
3. Substitute into $x = x_0 \sin \omega t$ with the calculator **in radian mode**. Check the sign of the answer: negative means the other side of equilibrium.

### Type 6: "Write down an equation for the displacement" (2 marks)

Method: give $x = x_0 \sin \omega t$ (or cosine) with the numbers inserted: $x_0$ in metres and $\omega$ in rad s$^{-1}$. E.g. for $x_0 = 4.0$ cm and $T = 1.0$ s: $x = 0.040 \sin(2\pi t)$. Keep $t$ as a symbol.

### Type 7: "Find the maximum velocity / maximum acceleration" (1 - 2 marks each)

Method:

1. Read $x_0$ (and $T$ or $f$) from the question or graph.
2. $\omega = 2\pi f = \frac{2\pi}{T}$.
3. $v_{\max} = \omega x_0$; $a_{\max} = \omega^2 x_0$. Give units (m s$^{-1}$, m s$^{-2}$).

Then the maximum force is $F_{\max} = m a_{\max}$ (used in piston questions: force on the piston to produce the max acceleration).

### Type 8: "Find the velocity at a given displacement" (1 - 2 marks)

Method: use $v = \pm \omega \sqrt{x_0^2 - x^2}$. Substitute $x_0$, $\omega$ and $x$ (all in metres). The speed is the magnitude; state direction only if asked. At $x = 0$ this reduces to $v = \omega x_0$.

### Type 9: "Determine period, frequency, angular frequency from a graph" (1 - 3 marks)

Method:

1. Period: time between two adjacent identical points (peak to peak, or crossing to crossing in the same direction).
2. Frequency: $f = 1/T$; angular frequency: $\omega = 2\pi f$.
3. If the graph shows acceleration against displacement, the gradient is $-\omega^2$, so $\omega = \sqrt{|\text{gradient}|}$.
4. If the graph shows several oscillations, count them: $T = \frac{\text{total time}}{\text{number of oscillations}}$.

### Type 10: "Phase difference between two oscillations" (2 - 3 marks)

Method:

1. Measure the time $t$ between two corresponding points (both peaks, or both zero crossings in the same direction).
2. $\text{phase difference} = \frac{t}{T}$ of an oscillation.
3. Convert: $\times 360^\circ$ for degrees, $\times 2\pi$ for radians. Give both if asked.

Also know these by heart: velocity leads displacement by $\frac{1}{4}$ cycle ($90^\circ$, $\frac{\pi}{2}$ rad); acceleration is $\frac{1}{2}$ cycle ($180^\circ$, $\pi$ rad) out of phase with displacement; graphs that are mirror images about the time axis (like $x$ and $a$) are $\pi$ rad apart.

### Type 11: "Sketch graphs" (1 - 2 marks each)

Method:

- $x$-$t$, $v$-$t$, $a$-$t$ for SHM: three sinusoids of the same period; $v$ is a cosine if $x$ is a sine, $a$ is an inverted sine. Label peaks with the correct values ($x_0$, $v_0 = \omega x_0$, $\omega^2 x_0$) and one period on the time axis.
- Energy-time: KE and PE sinusoids at twice the frequency of the displacement, total = horizontal line at $E$.
- Energy-displacement: parabolas, PE max at $\pm x_0$, KE max at 0.
- Damped oscillations: sine curve shrinking inside an exponential envelope; for critical/heavy damping, a smooth curve decaying to zero with no crossing.
- Resonance curve: amplitude vs driving frequency, peak at $f_0$; a second curve on the same axes showing heavier damping = lower, broader peak.

### Type 12: "Energy calculations" (2 - 3 marks)

Method:

1. Total energy: $E = \frac{1}{2} m \omega^2 x_0^2$ (need $m$, $\omega$, $x_0$).
2. KE at displacement $x$: $E_K = \frac{1}{2} m \omega^2 (x_0^2 - x^2)$, or $\frac{1}{2} m v^2$ with $v = \omega \sqrt{x_0^2 - x^2}$.
3. PE at displacement $x$: $E_P = E - E_K = \frac{1}{2} m \omega^2 x^2$.
4. From a $v$-$t$ graph: $v_{\max}$ is the peak; $E_{K,\max} = \frac{1}{2} m v_{\max}^2$; for an undamped oscillator max PE = max KE = total energy; $a_{\max}$ is the peak of the $a$-$t$ graph or $\omega v_{\max}$; $F_{\max} = m a_{\max}$.

Energy ratio shortcut: since $E \propto x_0^2$, halving the amplitude quarters the total energy. Since $E_K = E(1 - x^2/x_0^2)$, at $x = x_0/2$ the oscillator has $\frac{3}{4}$ of its energy as KE and $\frac{1}{4}$ as PE.

### Type 13: "Force, spring constant, period chains" (4 - 6 marks)

The real exam pattern (e.g. 9702/42/F/M/21 Q4):

1. Resultant force on a trolley between two springs at release: extension of each spring = (equilibrium length - natural length) $\pm$ displacement; $F = k \times$ extension for each; the resultant is the difference (or sum, depending on geometry). Show your substitution clearly.
2. Maximum acceleration: $a = F/m$.
3. Period: use $a = -\omega^2 x$ with the values just found: $\omega = \sqrt{a/x_0}$, then $T = 2\pi/\omega$. (Or use $T = 2\pi\sqrt{m/k_{\text{eff}}}$.)
4. Effect of changing amplitude: state that the force and the displacement are both halved, so $a/x$ is unchanged and **the period is unchanged** (period independent of amplitude).

### Type 14: "Damping questions" (2 - 4 marks)

Method:

- Identify the type from a graph: many oscillations with slowly decreasing amplitude = light damping; a single fast return to zero without overshoot = critical; a slow return without oscillation = heavy.
- Explain the amplitude decrease: the oscillator **loses energy** **due to resistive forces** (air resistance, friction, eddy currents).
- For a metal sheet in a magnetic field: the sheet cuts flux, an emf is induced, eddy currents flow, the currents cause a resistive force / dissipate energy (this is the 9702/42/F/M/21 Q9(c) answer).
- Sketch the damped $x$-$t$ graph (exponential envelope) or compare two damped curves (more damping = envelope shrinks faster).

### Type 15: "Resonance questions" (2 - 4 marks)

Method:

- Define resonance: oscillation at maximum amplitude when the driving frequency equals the natural frequency.
- Explain a resonance situation: identify the oscillator and the driver; state that energy is transferred from the driver to the system most efficiently when $f_{\text{driving}} = f_{\text{natural}}$; amplitude grows because energy is added each cycle.
- Sketch/compare resonance curves: damping lowers the peak, broadens it, and shifts it slightly to lower frequency.
- Examples: name the oscillating system AND what forces it (e.g. swing + child: driver is the person pushing; Millennium Bridge: driver is the pedestrians; microwave oven: driver is the microwaves, resonating system is water molecules; MRI: driver is the radio waves, resonating system is the protons).

### Type 16: "Experiment to determine $g$ using a pendulum" (method questions, Paper 3/4/5 style)

Method:

1. Measure the length $l$ from the point of suspension to the centre of the bob with a metre rule (to the nearest mm).
2. Displace the bob through a small angle (less than $10^\circ$) and release it so it swings in a single vertical plane.
3. Time 20 complete oscillations with a stopwatch; $T = \frac{\text{total time}}{20}$. Repeat and average for reliability.
4. Vary $l$ over a wide range, repeat the timing for each length.
5. Plot $T^2$ against $l$: gradient $= \frac{4\pi^2}{g}$, so $g = \frac{4\pi^2}{\text{gradient}}$.

Sources of error and improvements (from the June 2024 examiner report, which criticised exactly these):

- Parallax error judging the extremes of the swing: use a fiducial marker (e.g. a pointer) at the equilibrium position and time the passage through it.
- Difficult to judge the end of a complete oscillation: time many oscillations (20) and divide.
- Oscillation not in a single plane (swings in an ellipse): ensure a small initial displacement and release along a straight line.
- Not accounting for the mass of the bob / putty: include it in $m$ if the experiment involves mass.
- Two sets of data are not enough for a valid conclusion: take a range of lengths and plot a graph.
- Improvements: video camera with a timer in frame, view frame by frame; take more readings and plot a graph.

---

## 5. Solved Examples

All paper-code examples below are real CAIE questions whose wording and mark schemes were verified from the published papers. Mark allocations and full-mark answers are taken from the published mark schemes.

### Example 1: Phase difference from graphs (coursebook Worked example 1 pattern, 3 marks)

**Question:** Two identical oscillators have graphs that are out of step by $t = 17$ ms; the period of each is $T = 60$ ms. Find the phase difference as a fraction, in degrees and in radians.

**Method:**

1. Phase difference = time gap between corresponding points divided by the period: $\frac{t}{T}$.
2. Convert the fraction to degrees ($\times 360^\circ$) and to radians ($\times 2\pi$).

**Answer:**

$$\text{phase difference} = \frac{t}{T} = \frac{17}{60} = 0.283 \text{ of an oscillation}$$

$$\text{in degrees: } 0.283 \times 360^\circ = 102^\circ \approx 100^\circ$$

$$\text{in radians: } 0.283 \times 2\pi = 1.78 \text{ rad} \approx 1.8 \text{ rad}$$

**What the examiner wants:** the time gap measured between two corresponding points (both peaks, or both crossings in the same direction), and correct conversion of the fraction into both degrees and radians when asked.

### Example 2: Displacement equation and displacement at a time (coursebook Worked example 2 pattern)

**Question:** A pendulum oscillates with frequency 1.5 Hz and amplitude 0.10 m, passing through equilibrium at $t = 0$. (a) Write an equation for its displacement. (b) Find its displacement at $t = 0.50$ s.

**Method:**

1. It passes through equilibrium at $t = 0$, so use the sine form with $\omega = 2\pi f = 2\pi \times 1.5 = 3.0\pi$ rad s$^{-1}$.
2. Substitute $t = 0.50$ s into $x = x_0 \sin \omega t$ with the calculator **in radian mode**.

**Answer:**

(a) $$x = x_0 \sin \omega t = 0.10 \sin(3.0\pi t)$$

(b) $$x = 0.10 \sin(2\pi \times 1.5 \times 0.50) = 0.10 \sin(4.713) = -0.10 \text{ m}$$

The bob is at the extreme end of its swing; the minus sign means the negative (left-hand) side.

**What the examiner wants:** choosing sine or cosine from the starting condition (equilibrium at $t = 0$ means sine), and radian mode - with degrees this gives $-8.2 \times 10^{-3}$ m instead of $-0.10$ m, a classic error.

### Example 3: Two-spring trolley: force, acceleration, period (9702/42/F/M/21 Q4, 9 marks)

**Question:** A trolley rests on a bench, tethered between two identical stretched springs, each of spring constant $k = 8.0$ N m$^{-1}$ and unstretched length 12.0 cm. In equilibrium each spring is 18.0 cm long. The trolley of mass 250 g is displaced 4.8 cm to one side and released; resistive forces are negligible. (a) State the significance of the minus sign in $a = -\omega^2 x$ [1]. (b)(i) Show that the resultant force on the trolley at the moment of release is 0.77 N [2]. (ii) Find the maximum acceleration [1]. (iii) Use $a = -\omega^2 x$ to find the period [3]. (iv) The experiment is repeated with an initial displacement of 2.4 cm: state and explain the effect on the period [2].

**Method:**

1. Minus sign: acceleration and displacement are in opposite directions.
2. Force at release: the spring on one side is stretched to $18.0 + 4.8 = 22.8$ cm (extension $0.108$ m) and the other is compressed to $18.0 - 4.8 = 13.2$ cm (extension above its natural length $0.012$ m). Both forces oppose the displacement, so take the difference.
3. Maximum acceleration: $a = F/m$.
4. Period: at the maximum displacement $x_0 = 0.048$ m, $a_{\max} = 3.1$ m s$^{-2}$, so $\omega = \sqrt{a_{\max}/x_0}$ and $T = 2\pi/\omega$.
5. Amplitude change: both the resultant force and the displacement are halved, so $a/x$ (and hence $\omega$) is unchanged - the period is unchanged because the period of SHM is independent of the amplitude.

**Answer:**

$$F = k \times 0.108 - k \times 0.012 = 8.0 \times 0.108 - 8.0 \times 0.012 = 0.864 - 0.096 = 0.77 \text{ N}$$

$$a = \frac{F}{m} = \frac{0.77}{0.25} = 3.1 \text{ m s}^{-2}$$

$$\omega = \sqrt{\frac{3.1}{0.048}} = 8.04 \text{ rad s}^{-1}, \qquad T = \frac{2\pi}{8.04} = 0.78 \text{ s}$$

Period unchanged: "(resultant) force halved and distance halved" (1), "same T" (1).

**What the examiner wants:** M1 for $F = kx$ on each spring with the correct extensions ($0.108$ m and $0.012$ m), A1 for 0.77 N - show your substitution clearly; $a = F/m$ with $m$ in kg; $\omega = \sqrt{a/x_0}$ then $T = 2\pi/\omega$; and for the last part both ideas: force halved AND distance halved, so period unchanged.

### Example 4: Damped trolley: SHM conditions, angular frequency, time from a graph (9702/42/M/J/18 Q4, 10 marks)

**Question:** (a) State two conditions necessary for a mass to be undergoing SHM [2]. (b) A trolley of mass 950 g is held between two springs, each of constant 230 N m$^{-1}$, both always extended. It is displaced and released; its displacement-time graph shows oscillations whose amplitude decreases gradually. (i) 1. State and explain whether the oscillations are heavily damped, critically damped or lightly damped. 2. Suggest the cause of the damping [3]. (ii) 1. Given $a = -\frac{2k}{m} x$, calculate the angular frequency $\omega$. 2. Determine the time $t_1$ shown on the graph (the first minimum after release, 1.5 periods) [5].

**Method:**

1. Conditions for SHM: acceleration proportional to displacement; acceleration directed towards the fixed point (displacement and acceleration in opposite directions).
2. Damping: the amplitude decreases gradually and the oscillations continue for many cycles, so light damping; the energy loss is due to friction in the wheels / friction between wheels and surface / air resistance.
3. Two springs in parallel (both always extended) give effective constant $2k$, so $\omega^2 = \frac{2k}{m}$.
4. $T = 2\pi/\omega$, then $t_1 = 1.5T$.

**Answer:**

$$\omega^2 = \frac{2k}{m} = \frac{2 \times 230}{0.950} \Rightarrow \omega = 22 \text{ rad s}^{-1}$$

$$T = \frac{2\pi}{\omega} = \frac{2\pi}{22} = 0.286 \text{ s}, \qquad t_1 = 1.5T = 0.43 \text{ s}$$

**What the examiner wants:** both ideas in (a) - "acceleration proportional to displacement" (1) AND "acceleration directed towards the fixed point" or "displacement and acceleration in opposite directions" (1); "amplitude decreases gradually, so light damping" (1) + "loss of energy" (1) + "due to friction in wheels / friction between wheels and surface / air resistance" (1); $\omega^2 = 2k/m$ (C1, C1) with $\omega = 22$ rad s$^{-1}$ (A1); $T = 2\pi/\omega$ (C1) and $t_1 = 1.5T = 0.43$ s (A1). **Lesson: the "two conditions" question needs BOTH the proportionality and the direction, and with two springs you use $2k$, not $k$.**

### Example 5: Floating test tube (9702/42/F/M/19 Q3, 7 marks)

**Question:** A test tube floats vertically in a liquid. When pushed down and released it oscillates. The acceleration of the tube is given by $a = -\frac{A\rho g}{M} x$, where $A = 4.5 \times 10^{-4}$ m$^2$ is the cross-sectional area, $M = 0.17$ kg the total mass and $x$ the vertical displacement. The period of oscillation is 1.3 s. (a) State what is meant by SHM [2]. (b) Use the expression to explain why the tube undergoes SHM [2]. (c)(i) Determine the angular frequency [2]. (c)(ii) Determine the density $\rho$ of the liquid [3].

**Method:**

1. SHM definition: acceleration directly proportional to displacement, directed towards equilibrium (opposite direction to displacement).
2. $A$, $\rho$, $g$ and $M$ are all constant, so the acceleration is proportional to the displacement; the minus sign shows the acceleration is in the opposite direction to the displacement (directed towards the equilibrium position).
3. $\omega = 2\pi/T$.
4. Compare $a = -\frac{A\rho g}{M} x$ with $a = -\omega^2 x$: $\omega^2 = \frac{A\rho g}{M}$, rearrange for $\rho$.

**Answer:**

$$\omega = \frac{2\pi}{T} = \frac{2\pi}{1.3} = 4.8 \text{ rad s}^{-1}$$

$$\omega^2 = \frac{A\rho g}{M} \Rightarrow 4.8^2 = \frac{4.5 \times 10^{-4} \times \rho \times 9.81}{0.17}$$

$$\rho = \frac{4.8^2 \times 0.17}{4.5 \times 10^{-4} \times 9.81} = 900 \text{ kg m}^{-3}$$

**What the examiner wants:** "constants so $a \propto x$" (1) and "minus sign shows acceleration and displacement in opposite directions" (1); correct rearrangement and substitution into $\omega^2 = A\rho g/M$, with units kg m$^{-3}$.

### Example 6: Energy from a velocity-time graph (coursebook Question 22 pattern)

**Question:** A 2.0 kg mass oscillates with SHM. Its velocity-time graph is sinusoidal with peak $v_{\max} = 0.40$ m s$^{-1}$ and period $T = 0.80$ s. Find (a) the maximum kinetic energy, (b) the maximum potential energy, (c) the maximum acceleration, (d) the maximum restoring force.

**Method:**

1. $E_{K,\max} = \frac{1}{2} m v_{\max}^2$.
2. For undamped SHM the total energy is constant, so the maximum PE equals the maximum KE.
3. $\omega = 2\pi/T$, and $a_{\max} = \omega^2 x_0 = \omega v_{\max}$ (since $v_{\max} = \omega x_0$).
4. $F_{\max} = m a_{\max}$.

**Answer:**

(a) $$E_{K,\max} = \frac{1}{2} m v_{\max}^2 = \frac{1}{2} \times 2.0 \times 0.40^2 = 0.16 \text{ J}$$

(b) $$E_{P,\max} = 0.16 \text{ J}$$

(c) First get the amplitude: $\omega = \frac{2\pi}{T} = \frac{2\pi}{0.80} = 7.85$ rad s$^{-1}$ and $x_0 = \frac{v_{\max}}{\omega} = \frac{0.40}{7.85} = 0.051$ m. Then

$$a_{\max} = \omega^2 x_0 = \omega v_{\max} = 7.85 \times 0.40 = 3.1 \text{ m s}^{-2}$$

(d) $$F_{\max} = m a_{\max} = 2.0 \times 3.1 = 6.3 \text{ N}$$

**What the examiner wants:** recognising that max PE = max KE for an undamped oscillator, and using $a_{\max} = \omega v_{\max}$ to avoid an unnecessary amplitude step. Give units on every answer.

### Example 7: Metal strip with a load (9702/42/O/N/17 Q3(b), 5 marks)

**Question:** A thin metal strip clamped at one end carries a load of mass $M = 0.24$ kg at the free end. Theory predicts the acceleration of the load is $a = -\frac{c}{ML^3} x$, where $L$ is the effective length of the strip and $c$ a positive constant. (i) Explain how the expression shows the load is undergoing SHM [2]. (ii) For $L = 0.65$ m the frequency of oscillation is 3.2 Hz. Calculate $c$ [3].

**Method:**

1. $\frac{c}{ML^3}$ is a constant, so acceleration is proportional to displacement; the minus sign shows acceleration and displacement are in opposite directions.
2. Compare with $a = -\omega^2 x$: the constant $\frac{c}{ML^3}$ plays the role of $\omega^2$, and $\omega = 2\pi f$.
3. Rearrange: $c = 4\pi^2 f^2 M L^3$, substituting $M = 0.24$ kg, $L = 0.65$ m, $f = 3.2$ Hz.

**Answer:**

$$\frac{c}{ML^3} = (2\pi f)^2 \Rightarrow c = 4\pi^2 f^2 M L^3$$

$$c = 4\pi^2 \times 3.2^2 \times 0.24 \times 0.65^3 = 27 \text{ kg m}^3 \text{ s}^{-2}$$

**What the examiner wants:** "$\frac{c}{ML^3}$ is a constant so acceleration is proportional to displacement" (1); "minus sign shows that acceleration and displacement are in opposite directions" (1); $\frac{c}{ML^3} = (2\pi f)^2$ (C1), $c = 4\pi^2 \times 3.2^2 \times 0.24 \times 0.65^3$ (C1), $c = 27$ kg m$^3$ s$^{-2}$ (A1).

### Example 8: Resonance, damping and the resonance curve (9702/43/M/J/24 Q4, 8 marks)

**Question:** (a) State what is meant by resonance [2]. (b) A ball on a stretched string is displaced and released; its displacement-time graph shows the amplitude decreasing steadily with time. (i) Name the phenomenon [1]. (ii) Explain the decrease in amplitude with time [2]. (iii) The graph shows 2.0 complete cycles in 0.50 s. Determine the frequency [1]. (c) The string is now driven by a vibration generator whose frequency is increased from 0 to 10 Hz. Sketch the variation of amplitude with driving frequency on axes from 0 to 10 Hz [2].

**Method:**

1. Resonance: oscillation of the object at maximum amplitude when the driving frequency equals the natural frequency of the system.
2. Amplitude decrease: the oscillations of the ball lose energy due to resistive forces acting on it - this is light damping.
3. Frequency: 2.0 complete cycles in 0.50 s gives $T = 0.25$ s, so $f = 1/T = 4.0$ Hz.
4. Sketch: a curve with a single maximum at a non-zero frequency, with that maximum at 4.0 Hz.

**Answer:** light damping; "oscillations (of ball) lose energy" due to "resistive forces (acting on ball)"; $f = 1/0.25 = 4.0$ Hz; resonance curve peaking at 4.0 Hz.

**What the examiner wants:** "oscillation (of object) at maximum amplitude" (1) "when driving frequency = natural frequency (of system)" (1) - defining resonance as just "amplitude increases" loses the mark; for the damping explanation: "oscillations lose energy" (1) AND "due to resistive forces" (1); for the sketch: a single maximum at a non-zero frequency (1), located at 4.0 Hz (1).

### Example 9: Resonance in NMR imaging (9702/42/F/M/21 Q8(b), 4 marks)

**Question:** Nuclear magnetic resonance imaging uses radio waves directed at the body. (i) Explain why radio waves are used, i.e. why resonance occurs [2]. (ii) State when the protons emit their own radio-frequency signal [2].

**Method:**

1. Identify the oscillating system (protons) and the driver (radio waves).
2. Resonance occurs when the driving frequency equals the natural frequency - the radio wave frequency matches the protons' natural frequency, so the protons absorb energy.
3. When the radio-wave pulse stops, the excited protons de-excite and emit their own radio-frequency signal, which is detected.

**Answer:** "frequency of radio waves is equal to natural frequency of protons" (1); "resonance of protons occurs / protons absorb energy" (1); "in between pulses / when pulse stops" (1); "protons de-excite / emit r.f. pulses / emitted pulse detected" (1).

**What the examiner wants:** resonance explanations need the oscillator, the driver, and the frequency match. Energy absorption happens because the driving frequency equals the natural frequency.

### Example 10: Light damping via eddy currents (9702/42/F/M/21 Q9(c), 4 marks)

**Question:** A copper sheet oscillates between the poles of a magnet. (i) State the type of damping [1]. (ii) A second sheet (with a slit) oscillates and its amplitude decays more slowly. Explain the damping of the first sheet [3].

**Method:**

1. The amplitude decays gradually over many oscillations: light damping.
2. Mechanism: the sheet cuts (magnetic) flux, inducing an emf; the emf drives (eddy) currents in the sheet; the currents cause a resistive force / dissipate energy.
3. Comparison: the slitted sheet has smaller currents, so less energy is dissipated and its amplitude decays more slowly.

**Answer:** light damping; "sheet cuts (magnetic) flux and causes induced emf" (1); "(induced) emf causes (eddy) currents (in sheet)" (1); "currents (in sheet) cause resistive force" OR "currents (in sheet) dissipate energy" (1); smaller currents in the slitted sheet, so its decay is slower (1).

**What the examiner wants:** the full chain - flux cut, induced emf, eddy currents, resistive force/energy dissipation. **Lesson: full damping answers = energy loss + the mechanism of the resistive force.**

### Further practice: coursebook end-of-chapter questions worth doing (from the Cambridge coursebook, Chapter 19)

- Q2: pendulum, $x_0 = 4.0$ cm, $T = 1.0$ s: write the displacement equation [2], max velocity [2], velocity at $x = 2.0$ cm [1].
- Q3: 50 g mass on a spring, amplitude 16 mm, $T = 0.84$ s: frequency [1], max velocity [1], max KE [2], max PE [1].
- Q5: from a displacement-time graph, determine $f$ and $T$ [2], then sketch velocity and acceleration on the same axes [3].
- Q7: car engine piston at 4200 rev min$^{-1}$, amplitude 12.5 cm, mass 0.24 kg: explain SHM [2], frequency [1], max speed [2], max acceleration [2], force for max acceleration [1].
- Q10: seismometer: explain why the natural frequency of the spring-mass system should be much less than the 30 - 40 Hz shock wave range [3]; what evidence an $a$-$x$ graph gives that motion is SHM [2]; calculate frequency from the graph [4].

---

## 6. Cheat Sheet (quick revision block)

**Definitions to write blind:**

- **SHM:** acceleration directly proportional to displacement from equilibrium, and directed towards it (opposite direction to displacement).
- **Amplitude $x_0$:** maximum displacement from equilibrium.
- **Period $T$:** time for one complete oscillation. **Frequency $f$:** oscillations per second.
- **Angular frequency $\omega$:** rate of change of phase, $\omega = 2\pi f = 2\pi/T$.
- **Phase difference:** fraction of a cycle (or degrees/radians) by which two oscillations are out of step.
- **Damping:** loss of energy from an oscillator due to resistive forces; amplitude decays.
- **Light damping:** gradual exponential decay of amplitude, many oscillations, period roughly constant.
- **Critical damping:** minimum damping for return to equilibrium without oscillating (fastest non-oscillatory return).
- **Heavy damping:** slow return to equilibrium without oscillating.
- **Resonance:** maximum amplitude of forced oscillation when driving frequency = natural frequency.
- **Natural frequency:** frequency of free oscillation after a disturbance.

**All formulas:**

$$f = \frac{1}{T}, \qquad \omega = 2\pi f = \frac{2\pi}{T}$$

$$x = x_0 \sin \omega t \text{ (start at equilibrium)} \qquad x = x_0 \cos \omega t \text{ (start at max } x)$$

$$a = -\omega^2 x, \qquad v = v_0 \cos \omega t, \qquad v = \pm \omega \sqrt{x_0^2 - x^2}$$

$$v_{\max} = \omega x_0, \qquad a_{\max} = \omega^2 x_0, \qquad F_{\max} = m a_{\max}$$

$$E = \frac{1}{2} m \omega^2 x_0^2, \qquad E_K = \frac{1}{2} m \omega^2 (x_0^2 - x^2), \qquad E_P = \frac{1}{2} m \omega^2 x^2$$

$$T = 2\pi \sqrt{\frac{m}{k}} \text{ (mass-spring; use } 2k \text{ for two springs in parallel)}$$

$$T = 2\pi \sqrt{\frac{l}{g}} \text{ (pendulum, small angles)}$$

$$\text{phase difference} = \frac{t}{T} \times 360^\circ = \frac{t}{T} \times 2\pi \text{ rad}$$

**Key facts:**

- Acceleration is always opposite to displacement (that is the minus sign).
- $v$ leads $x$ by $90^\circ$; $a$ is $180^\circ$ out of phase with $x$.
- Velocity = gradient of $x$-$t$ graph; acceleration = gradient of $v$-$t$ graph; $a$-$x$ graph is a straight line of gradient $-\omega^2$.
- Period is independent of amplitude (and of $m$ for a pendulum; independent of $g$ for a mass-spring).
- KE max at centre, PE max at extremes, total energy constant if undamped; $E \propto x_0^2$.
- KE and PE each go through 2 cycles per period of the oscillation.
- Resonance: amplitude max when $f_{\text{driving}} = f_{\text{natural}}$; damping lowers and broadens the peak.
- Energy of a damped oscillator is lost to resistive forces; amplitude decays exponentially.

**Common traps (see Section 7):**

- Calculator in DEGREES for $\sin \omega t$ - always use radians.
- Forgetting the minus sign in $a = -\omega^2 x$.
- Amplitude vs displacement: amplitude is the maximum, always positive.
- cm vs m and ms vs s conversions (phase difference $\frac{17 \text{ ms}}{60 \text{ ms}}$ needs no conversion, but $x_0$ and $x$ must be in the same unit).
- Two springs: effective constant is $2k$.
- Giving only "acceleration proportional to displacement" without the direction - drops a mark.
- Saying resonance is "when amplitude increases" - it is maximum at $f_{\text{driving}} = f_{\text{natural}}$.

---

## 7. Common Exam Mistakes (from examiner reports and mark scheme patterns)

**On the definition of SHM (most common lost marks):**

- Giving only "acceleration is proportional to displacement". The mark scheme gives one mark for proportionality and a second for the direction ("directed towards the equilibrium position" / "acceleration and displacement in opposite directions"). Both ideas are required for full marks (9702/42/M/J/18 Q4(a)).
- Writing "the force is proportional to displacement" when the question asks about acceleration - the definition is about acceleration.
- Saying "the acceleration is constant" or "velocity is proportional to displacement" - both wrong.

**On calculations:**

- **Calculator in degrees instead of radians.** The coursebook's own worked example 2 demonstrates the classic error: with degrees, $x = 0.10 \sin(4.713)$ gives $-8.2 \times 10^{-3}$ m instead of $-0.10$ m. The presence of $\pi$ in $\omega t$ is the reminder: radian mode.
- Forgetting the minus sign when quoting $a = -\omega^2 x$ or when stating the direction of acceleration.
- Using the wrong spring constant: with two springs holding a trolley, the effective constant is $2k$ (9702/42/M/J/18 Q4(b)(ii): $\omega^2 = 2k/m$, not $k/m$).
- Premature rounding of intermediate values (a general examiner complaint across papers: rounding early gives wrong final answers to the required significant figures).
- Mixing units: amplitudes in cm with displacements in m; times in ms with periods in s.
- In the pendulum experiment: timing only half an oscillation, or not dividing the total time by the number of oscillations to get $T$; not showing repeated readings; missing units (June 2024 examiner report).
- In $T = 2\pi\sqrt{m/k}$ problems, forgetting that $m$ must be in kg (950 g, 250 g, 50 g appear in real questions).

**On graphs and energy:**

- Confusing the $v$-$t$ and $a$-$t$ graph shapes: $v$ is a cosine when $x$ is a sine; $a$ is an inverted sine (antiphase with $x$).
- Thinking KE and PE peak once per cycle - they each peak twice (KE at both passages through the centre, PE at both extremes).
- Writing that total energy depends on amplitude linearly - it depends on $x_0^2$.
- On energy-displacement sketches: drawing KE and PE as straight lines instead of parabolas.

**On damping and resonance (from mark scheme patterns):**

- Identifying damping type from a graph: "amplitude decreases gradually, so light damping" - a single smooth return to zero with no oscillation is critical OR heavy; distinguish them by time (heavy is slower). "Returns without oscillating" alone is not enough.
- Explaining damping without the mechanism: full marks need "loses energy" AND "due to resistive forces" (9702/42/F/M/21 Q9(c), 9702/43/M/J/24 Q4(b)(ii)).
- Defining resonance as just "amplitude increases" - the mark scheme wants "oscillation at maximum amplitude" AND "when driving frequency = natural frequency" (9702/43/M/J/24 Q4(a)).
- Confusing the effect of damping on the resonance curve: damping DECREASES the peak amplitude, BROADENS the peak, and shifts the resonant frequency slightly LOWER. "Damping increases the amplitude" is a common wrong answer.
- Confusing free and forced oscillations: a forced oscillator vibrates at the driving frequency, not its natural frequency.
- For resonance examples, forgetting to name both the oscillating system and the driver (coursebook Q24 asks for exactly this: three problems and three uses, with system + driver for each).

**On the practical (from the June 2024 examiner report on the oscillation experiment):**

- Judging the end of a complete oscillation is difficult - time 20 oscillations, not one.
- Parallax error when reading the amplitude or the position of the oscillating mass - use a fiducial marker.
- The oscillation swinging in more than one plane (elliptical motion) - release it carefully in a single vertical plane.
- Not accounting for the mass of the bob/putty.
- Two sets of data are not enough for a valid conclusion - take a range of values and plot a graph.
- Improvement answers need specifics: "video camera with a timer in the frame, viewed frame by frame", not just "use a video camera".
