# Physics — All Methods & Questions (Master File)

> **Copied verbatim** from each chapter's **Methods (§4)** and **Solved Examples (§5)**.
> Originals in `physics/notes/` (and Ch26 at root) are **unchanged** — this file is a compiled reference in chapter order.
> Source files:
> - `physics/notes/chapter-17-circular-motion-notes.md` — Chapter 17: Circular Motion
> - `physics/notes/chapter-18-gravitational-fields-notes.md` — Chapter 18: Gravitational Fields
> - `physics/notes/chapter-19-oscillations-notes.md` — Chapter 19: Oscillations
> - `physics/notes/chapter-21-thermal-physics-notes.md` — Chapter 21: Thermal Physics
> - `physics/notes/chapter-22-ideal-gases-notes.md` — Chapter 22: Ideal Gases
> - `physics/notes/chapter-23-coulombs-law-notes.md` — Chapter 23: Coulomb's Law
> - `physics/notes/chapter-24-capacitance-notes.md` — Chapter 24: Capacitance
> - `physics/notes/chapter-25-electronics-notes.md` — Chapter 25: Electronics
> - `chapter-26-magnetic-fields-and-electromagnetism-notes.md` — Chapter 26: Magnetic Fields and Electromagnetism
> - `physics/notes/chapter-27-charged-particles-notes.md` — Chapter 27: Charged Particles
> - `physics/notes/chapter-29-alternating-currents-notes.md` — Chapter 29: Alternating Currents

---

## Contents
- **Chapter 17: Circular Motion**
- **Chapter 18: Gravitational Fields**
- **Chapter 19: Oscillations**
- **Chapter 21: Thermal Physics**
- **Chapter 22: Ideal Gases**
- **Chapter 23: Coulomb's Law**
- **Chapter 24: Capacitance**
- **Chapter 25: Electronics**
- **Chapter 26: Magnetic Fields and Electromagnetism**
- **Chapter 27: Charged Particles**
- **Chapter 28: Electromagnetic Induction**
- **Chapter 29: Alternating Currents**

---

# Chapter 17: Circular Motion
> Source: `physics/notes/chapter-17-circular-motion-notes.md`

## 4. Methods (Question Types & Methods)

### Type 1: Define the radian, angular velocity, centripetal force or centripetal acceleration (1-2 marks)

These are recall questions and the mark scheme is strict.

- **Radian**: "the angle subtended at the centre of a circle by an arc equal in length to the radius".
- **Angular velocity**: "rate of change of angular displacement" (mention $\text{rad s}^{-1}$ if asked for units). Do not answer with an equation alone.
- **Centripetal force**: "the resultant force acting on an object moving in a circle, directed towards the centre (perpendicular to the velocity)". Two key ideas: resultant force, towards the centre. You can mention it is supplied by a real force such as tension or friction.
- **Centripetal acceleration**: the 1-mark definition accepted in the November 2021 mark scheme is "acceleration perpendicular to velocity". For full marks add "towards the centre" and, if useful, that it arises because the direction of the velocity changes.

Method: write the definition from memory, in proper technical language. Never define a term using the term itself (writing "centripetal acceleration is the acceleration due to the centripetal force" earns nothing), and never answer with an equation instead of a definition.

### Type 2: Convert between degrees and radians

Multiply degrees by $\pi/180$ to get radians, or radians by $180/\pi$ to get degrees. Express answers as multiples of $\pi$ where possible (for example $60^{\circ} = \pi/3$ rad). Show the conversion factor, because "show that" questions need the working.

### Type 3: Find angular velocity from period, frequency or rpm

Steps:

1. If given rpm, divide by 60 to get revolutions per second (frequency $f$).
2. Use $\omega = 2\pi f$ or $\omega = 2\pi/T$.
3. Give the answer in $\text{rad s}^{-1}$.

Example check: the second hand of a clock has $T = 60$ s, so $\omega = 2\pi/60 = 0.105 \ \text{rad s}^{-1}$.

### Type 4: Find the linear speed of a point on a rotating body

Use $v = r\omega$. First get $\omega$ (Type 3), then multiply by the radius. Watch the radius: use the distance of the point from the axis, and convert cm to m. Remember every point on a rigid rotating body shares the same $\omega$ but $v$ grows with $r$.

### Type 5: Find centripetal acceleration

Pick the form that matches your data: $a = v^{2}/r$ if you know speed, $a = r\omega^{2}$ if you know angular velocity. Both are accepted; using the wrong one after computing the wrong intermediate is a common way to lose marks. State the direction (towards the centre) when the question asks.

### Type 6: Find centripetal force given mass, speed, radius

Substitute straight into $F = mv^{2}/r$ (or $F = mr\omega^{2}$). Convert mass to kg and radius to m first. The answer is the resultant force towards the centre; if the question asks "what provides it", name the real force (friction, tension, gravity, normal contact force).

### Type 7: Maximum speed before skidding (car on a flat road)

Steps:

1. Friction provides the centripetal force, and its maximum value is $F_{\text{max}} = \mu N = \mu mg$ (normal force equals weight on a flat road).
2. Set the required centripetal force equal to the maximum friction: $\dfrac{mv^{2}}{r} = \mu mg$.
3. The mass cancels: $v_{\text{max}} = \sqrt{\mu r g}$.
4. Above this speed the required force exceeds the available friction and the car skids outward (away from the centre, along the tangent).

The same pattern appears with a string that breaks (tension limit) and a coin on a turntable (friction limit, so there is a maximum radius at fixed $\omega$ because $F = mr\omega^{2}$ grows with $r$).

### Type 8: Vertical circle at the top and bottom (bucket of water, roller coaster, ball on a string)

Steps:

1. State the forces at the position in question: at the top, weight and tension both act towards the centre; at the bottom, tension acts towards the centre and weight acts away from it.
2. Write the resultant-force equation: top $T + mg = mv^{2}/r$, bottom $T - mg = mv^{2}/r$.
3. For minimum speed at the top (string taut / contact maintained), set $T = 0$, giving $mg = mv^{2}/r$ and $v_{\text{min}} = \sqrt{gr}$.
4. If the speed is not constant, link the top and bottom speeds with energy: $\dfrac{1}{2}mv_{\text{bottom}}^{2} = \dfrac{1}{2}mv_{\text{top}}^{2} + mg(2r)$.
5. Answer "is it in contact?" questions by comparing the computed acceleration (or speed) with the critical value $g$ (or $\sqrt{gr}$).

### Type 9: Conical pendulum (tension components, angle, period)

Steps:

1. Resolve the tension: vertically $T\cos\theta = mg$, horizontally $T\sin\theta = mv^{2}/r$.
2. Divide to get $\tan\theta = v^{2}/(rg)$ (the standard "show that" result).
3. Radius from geometry: $r = L\sin\theta$.
4. Find $T$ from the vertical equation, $v$ from $\tan\theta = v^{2}/(rg)$, and the period from $T_{\text{period}} = 2\pi r/v$.
5. For "what happens if it moves faster": $\theta$ increases, because a larger centripetal force needs a larger horizontal component $T\sin\theta$.

### Type 10: Banked track or banking aircraft

Steps:

1. Resolve the normal force (or lift): horizontally $N\sin\theta = mv^{2}/r$, vertically $N\cos\theta = mg$.
2. Divide: $\tan\theta = v^{2}/(rg)$; the design speed is $v = \sqrt{rg\tan\theta}$.
3. Below design speed the vehicle slides down the slope; above it, up the slope.
4. Explain why banking helps: the horizontal component of the normal force can supply centripetal force, so the car does not depend on friction alone.

### Type 11: Fairground rotor / wall of death

The wall pushes on the rider (normal contact force $N$) providing the centripetal force $N = mr\omega^{2}$; friction between rider and wall balances the weight. For the rider not to slip: $\mu N \geq mg$, so $\mu mr\omega^{2} \geq mg$ and $\omega_{\text{min}} = \sqrt{g/(\mu r)}$. Note the mass cancels.

### Type 12: Satellite or orbit speed and period

Steps:

1. Set gravity equal to the centripetal force: $mg = mv^{2}/r$ (or the full gravitational form $GMm/r^{2} = mv^{2}/r$ if $G$ and $M$ are given).
2. $v = \sqrt{gr}$ (or $\sqrt{GM/r}$). Use $r$ measured from the centre of the planet.
3. Period: $T = 2\pi r/v$.
4. Watch the units: km to m, days to seconds (687 days $\times 24 \times 3600$ for Mars).

### Type 13: Conceptual "what happens to X" / comparison questions

Past papers ask you to compare quantities between two paths or two positions (for example a larger-radius path vs a smaller-radius path with the same friction limit). Method: write the relevant equation, note which quantities are fixed, and reason about what changes. Examples: same friction force $F$ and same mass on a larger radius means the same centripetal acceleration ($a = F/m$), a larger maximum speed ($v = \sqrt{Fr/m}$), and a longer lap time ($t = 2\pi r/v = 2\pi\sqrt{mr/F}$). In a loop, the car is slower and the centripetal acceleration smaller at the top than at the bottom.

### Type 14: MCQ style (Paper 1)

Paper 1 multiple-choice questions test the same ideas at one step: which definition is correct, the direction of the centripetal force/acceleration, what provides the centripetal force in a given situation, converting rpm to $\text{rad s}^{-1}$, and simple $v = r\omega$ or $F = mv^{2}/r$ substitutions. The same traps apply, so the methods above work: convert units first, remember the direction is always towards the centre, and eliminate options that mention an outward "centrifugal" force (the syllabus does not use it).

## 5. Solved Examples

All solutions are written in mark-scheme style: equation, substitution, answer with units. Take $g = 9.81 \ \text{m s}^{-2}$ unless stated. Examples 1-8 are coursebook-style problems; Examples 9-11 are real CAIE questions with their published mark schemes, verified directly against the question papers and mark schemes. They cover every skill this chapter is examined on.

### Example 1: Radian conversion and the clock hands (Coursebook Chapter 17)

**Question:** (a) Convert $60^{\circ}$ to radians. (b) The second hand of a clock has length 1.8 cm. Calculate its angular velocity and the speed of its tip.

**Method:**
- (a) Multiply the angle in degrees by $\pi/180$.
- (b) One revolution is $2\pi$ rad and takes 60 s, so $\omega = 2\pi/T$. Convert the length to metres ($r = 0.018$ m), then use $v = r\omega$.

**Answer:**
- (a) $60^{\circ} = 60 \times \dfrac{\pi}{180} = \dfrac{\pi}{3} = 1.05 \ \text{rad}$.
- (b) $\omega = \dfrac{2\pi}{60} = 0.105 \ \text{rad s}^{-1}$; $v = r\omega = 0.018 \times 0.105 = 1.9 \times 10^{-3} \ \text{m s}^{-1}$.

**What the examiner wants:** the angular velocity part is the classic 2-mark question "show that the angular velocity of the second hand of a clock is about 0.105 rad s$^{-1}$" - write $\omega = 2\pi/60 = 0.105$ with the substitution shown, and convert cm to m before using $v = r\omega$.

### Example 2: Washing machine drum - rpm to angular velocity to speed (Coursebook Chapter 17)

**Question:** The drum of a washing machine spins at 1200 revolutions per minute. The clothes are at a radius of 0.32 m from the axis. Calculate (a) the angular velocity of the drum, (b) the speed of the clothes.

**Method:**
- (a) Convert rpm to revolutions per second (divide by 60), then to radians per second with $\omega = 2\pi f$.
- (b) Multiply by the radius: $v = r\omega$.

**Answer:**
- (a) $f = \dfrac{1200}{60} = 20 \ \text{Hz}$, so $\omega = 2\pi f = 2\pi \times 20 = 126 \ \text{rad s}^{-1}$.
- (b) $v = r\omega = 0.32 \times 125.7 = 40 \ \text{m s}^{-1}$.

**What the examiner wants:** the rpm conversion done as two clear steps (divide by 60, then multiply by $2\pi$), and a full substitution into $v = r\omega$ with units on the answer.

### Example 3: Maximum speed before a string breaks (Coursebook Chapter 17)

**Question:** A stone of mass 0.20 kg is whirled round on the end of a string of length 30 cm. The string breaks when the tension exceeds 8.0 N. Calculate the maximum speed at which the stone can be whirled without the string breaking.

**Method:**
1. The tension provides the centripetal force.
2. At the limit, $T = mv^{2}/r$.
3. Convert 30 cm to 0.30 m, then rearrange for $v$: $v = \sqrt{Tr/m}$.

**Answer:** $v = \sqrt{\dfrac{Tr}{m}} = \sqrt{\dfrac{8.0 \times 0.30}{0.20}} = \sqrt{12} = 3.5 \ \text{m s}^{-1}$.

**What the examiner wants:** equating the tension to $mv^{2}/r$ (not to the weight), converting cm to m, and giving the answer to two significant figures to match the data.

### Example 4: Vertical circle - bucket of water (Coursebook Chapter 17)

**Question:** A teacher swings a bucket of water of total mass 5.4 kg round in a vertical circle of diameter 1.8 m. (a) Calculate the minimum speed at the top so the water stays in the bucket. (b) Assuming the speed stays constant, find the force on the teacher's hand at the bottom.

**Method:**
- (a) At the minimum speed the tension is zero and the weight alone provides the centripetal force: $mg = mv^{2}/r$. The radius is half the diameter, $r = 0.9$ m.
- (b) At the bottom the tension acts towards the centre and the weight acts away from it: $T - mg = mv^{2}/r$, so $T = m(v^{2}/r + g)$.

**Answer:**
- (a) $v = \sqrt{gr} = \sqrt{9.81 \times 0.9} = 3.0 \ \text{m s}^{-1}$.
- (b) $T = 5.4\left(\dfrac{8.83}{0.9} + 9.81\right) = 5.4 \times 19.6 = 106 \ \text{N}$.

**What the examiner wants:** using the diameter to get the radius ($r = 1.8/2 = 0.9$ m, not 1.8 m). Note: at exactly $v = \sqrt{gr}$, $v^{2}/r = g$, so the bottom tension is $2mg = 2 \times 5.4 \times 9.81 = 106$ N.

### Example 5: Conical pendulum - rubber bung (Coursebook Chapter 17)

**Question:** A rubber bung of mass 0.20 kg is swung in a horizontal circle of radius 0.40 m so that the string makes an angle of $56^{\circ}$ with the vertical. Calculate (a) the tension in the string, (b) the angular velocity of the bung, (c) the time for one complete revolution.

**Method:**
- (a) Vertically, the tension's upward component balances the weight: $T\cos\theta = mg$.
- (b) Horizontally, the inward component provides the centripetal force: $T\sin\theta = mr\omega^{2}$, so $\omega = \sqrt{T\sin\theta/(mr)}$.
- (c) The period is $T_{\text{period}} = 2\pi/\omega$.

**Answer:**
- (a) $T = \dfrac{0.20 \times 9.81}{\cos 56^{\circ}} = \dfrac{1.96}{0.559} = 3.5 \ \text{N}$.
- (b) $\omega = \sqrt{\dfrac{3.51 \times 0.829}{0.20 \times 0.40}} = \sqrt{36.4} = 6.0 \ \text{rad s}^{-1}$.
- (c) $T_{\text{period}} = \dfrac{2\pi}{6.03} = 1.0 \ \text{s}$.

**What the examiner wants:** resolving the tension into components - the vertical component balances the weight, the horizontal component provides the centripetal force. Refer to components of the tension, never components of the weight.

### Example 6: Maximum cornering speed on a flat road (Coursebook Chapter 17)

**Question:** A car of mass 1200 kg rounds a flat bend of radius 50 m. The maximum frictional force is 0.60 of the car's weight. Calculate the maximum speed at which the car can take the bend.

**Method:**
1. Friction provides the centripetal force.
2. At the limit, $mv^{2}/r = 0.60mg$.
3. The mass cancels; solve for $v$.

**Answer:** $v = \sqrt{0.60 \, r g} = \sqrt{0.60 \times 50 \times 9.81} = 17 \ \text{m s}^{-1}$.

**What the examiner wants:** noticing that the mass cancels, so the answer does not depend on the mass of the car. Above this speed the car skids outward because the required centripetal force exceeds the maximum friction.

### Example 7: Banked track (Coursebook Chapter 17)

**Question:** A bend of radius 80 m is to be taken at a speed of 25 m s$^{-1}$. Calculate the banking angle for a frictionless track.

**Method:**
1. Resolve the normal force: horizontally $N\sin\theta = mv^{2}/r$, vertically $N\cos\theta = mg$.
2. Divide the two equations to eliminate $N$: $\tan\theta = v^{2}/(rg)$.
3. Substitute and take the inverse tangent.

**Answer:** $\tan\theta = \dfrac{v^{2}}{rg} = \dfrac{25^{2}}{80 \times 9.81} = \dfrac{625}{784.8} = 0.796$, so $\theta = 38.5^{\circ} \approx 39^{\circ}$.

**What the examiner wants:** showing the division of the two resolved equations, then a full substitution with all numbers before the final angle.

### Example 8: The International Space Station (Coursebook Chapter 17)

**Question:** The ISS has mass 350 tonnes and orbits at an average height of 340 km, where the gravitational field strength is $8.8 \ \text{m s}^{-2}$. The radius of the Earth is 6400 km. Calculate (a) the centripetal force on the ISS, (b) its orbital speed, (c) the time for each orbit.

**Method:**
1. Orbital radius from the centre of the Earth: $r = 6400 + 340 = 6740$ km $= 6.74 \times 10^{6}$ m. Mass: $m = 3.5 \times 10^{5}$ kg.
- (a) Gravity provides the centripetal force: $F = mg$.
- (b) $mg = mv^{2}/r$, so $v = \sqrt{gr}$ using $g$ at the orbital radius.
- (c) $T = 2\pi r/v$.

**Answer:**
- (a) $F = mg = 3.5 \times 10^{5} \times 8.8 = 3.1 \times 10^{6} \ \text{N}$.
- (b) $v = \sqrt{gr} = \sqrt{8.8 \times 6.74 \times 10^{6}} = 7.7 \times 10^{3} \ \text{m s}^{-1}$.
- (c) $T = \dfrac{2\pi r}{v} = \dfrac{2\pi \times 6.74 \times 10^{6}}{7.70 \times 10^{3}} = 5.5 \times 10^{3} \ \text{s} \approx 92 \ \text{minutes}$.

**What the examiner wants:** the orbital radius measured from the centre of the planet (height added to the Earth's radius), and the value of $g$ at the orbital height used, not surface gravity.

### Example 9: Two cars on a circular track (9702/41/O/N/21 Q1, 7 marks)

**Question:** Two cars move around a horizontal circular track. Path X has radius 318 m; path Y is parallel to and 27 m outside path X (radius 345 m). Both cars have mass 790 kg, and the maximum lateral friction force $F$ is the same for both cars.

(a) With reference to velocity and acceleration, describe uniform circular motion. [2]

(b)(i) The maximum speed of the car on path X without sliding is 94 m s$^{-1}$. Calculate $F$. [2]

(b)(ii) Tick a table to compare, for the car on path Y, the centripetal acceleration, the maximum speed, and the time taken for one lap, against the car on path X. [3]

**Method:**
- (a) State two ideas: constant speed (constant magnitude of velocity), and acceleration always perpendicular to the velocity.
- (b)(i) Friction provides the centripetal force: $F = mv^{2}/r$. Substitute $m = 790$ kg, $v = 94$ m s$^{-1}$, $r = 318$ m.
- (b)(ii) With the same $F$ and the same $m$: $a = F/m$ is identical; $v_{\text{max}} = \sqrt{Fr/m}$ grows with $r$; the lap time $t = 2\pi r/v = 2\pi\sqrt{mr/F}$ grows with $r$.

**Answer:**
- (a) Constant speed (or constant magnitude of velocity); acceleration (always) perpendicular to the velocity.
- (b)(i) $F = \dfrac{mv^{2}}{r} = \dfrac{790 \times 94^{2}}{318} = 22\,000$ N.
- (b)(ii) Centripetal acceleration: same. Maximum speed: greater. Time taken for one lap: greater.

**What the examiner wants:** (a) B1 + B1 - both ideas are needed and an equation alone is not accepted. (b)(i) C1 for the substituted equation, A1 for the answer. (b)(ii) three B1s for the three correct table entries - this is Type 13 reasoning, tracking what is fixed ($F$, $m$) and what changes with $r$.

### Example 10: Toy car on a vertical loop (9702/42/O/N/21 Q1, 8 marks)

**Question:** An unpowered toy car of mass 230 g moves on a smooth track containing a vertical circular loop of diameter 62 cm. Resistive forces are negligible. X is at the bottom of the loop and Y at the top.

(a) State what is meant by centripetal acceleration. [1]

(b)(i) State what happens to the magnitude of the centripetal acceleration of the car as it moves around the loop from X to Y. [1]

(b)(ii) Explain, if the car remains in contact with the track, why the centripetal acceleration of the car at point Y must be greater than $9.8 \ \text{m s}^{-2}$. [2]

(c) The initial speed along the track is 3.8 m s$^{-1}$. Determine whether the car is in contact with the track at point Y. Show your working. [3]

(d) Suggest, with a reason but without calculation, whether your conclusion in (c) would be different for a car of mass 460 g moving with the same initial speed. [1]

**Method:**
- (a) Write the definition: acceleration perpendicular to velocity.
- (b)(i) The car is slower at Y than at X because it has gained gravitational potential energy, so its centripetal acceleration is smaller at Y.
- (b)(ii) The $9.8 \ \text{m s}^{-2}$ is caused by the weight alone; an acceleration greater than this needs an additional contact force from the track, which only exists while the car is in contact.
- (c) Use conservation of energy to find the speed at the top (the car rises by the diameter $h = 0.62$ m), then $a = v^{2}/r$ with $r = 0.31$ m, and compare $a$ with $g$. Alternative accepted method: the required speed for contact at the top is $v_{Y} = \sqrt{gr}$, then find the initial speed that would produce it.
- (d) Mass cancels in all the equations, so the conclusion is unchanged.

**Answer:**
- (a) Acceleration perpendicular to velocity. (Adding "towards the centre" is also fine; quoting an equation is not enough.)
- (b)(i) It decreases.
- (b)(ii) The acceleration of $9.8 \ \text{m s}^{-2}$ is caused by the weight of the car (or: the centripetal force must be greater than the weight of the car); an acceleration greater than $9.8 \ \text{m s}^{-2}$ requires a contact force from the track.
- (c) Energy: $\dfrac{1}{2}mv_{Y}^{2} = \dfrac{1}{2}mv_{X}^{2} - mgh$, so $v_{Y}^{2} = 3.8^{2} - 2 \times 9.81 \times 0.62 = 2.28$ and $v_{Y} = 1.5 \ \text{m s}^{-1}$. Then $a = \dfrac{v^{2}}{r} = \dfrac{1.5^{2}}{0.31} = 7.3 \ \text{m s}^{-2}$, which is less than $9.8 \ \text{m s}^{-2}$, so the car is **not** in contact with the track. (Alternative: contact at the top needs $v_{Y} = \sqrt{9.81 \times 0.31} = 1.74$ m s$^{-1}$, which requires $v_{X} = 3.9$ m s$^{-1}$, greater than the actual 3.8 m s$^{-1}$, so no contact.)
- (d) No - the acceleration and the conclusion are independent of mass because mass cancels in the equations.

**What the examiner wants:** (a) the exact 1-mark definition "acceleration perpendicular to velocity" (B1). (b)(i) B1. (b)(ii) B1 + B1 - both the weight idea and the contact-force idea. (c) C1 for the energy equation, A1 for $v_{Y} = 1.5$ m s$^{-1}$, C1 for $a = v^{2}/r$, then the comparison with $9.8$ decides the conclusion; the alternative $\sqrt{gr}$ method is also accepted. (d) B1 for mass cancels.

### Example 11: Steel sphere on a spring in a horizontal circle (9702/41/M/J/23 Q2, 12 marks)

**Question:** A steel sphere of mass 0.29 kg hangs in equilibrium from a vertical spring, its centre 8.5 cm from the top of the spring. The sphere is then set moving in a horizontal circle at constant speed; the distance from the centre of the sphere to the top of the spring is now 10.8 cm, and the spring's axis makes an angle of $27^{\circ}$ with the vertical.

(a) Explain, with reference to the forces acting on the sphere, why the length of the spring is now greater. [3]

(b)(i) Show that the radius of the circle is 4.9 cm. [1]

(b)(ii) Show that the tension in the spring is 3.2 N. [2]

(b)(iii) The spring obeys Hooke's law. Calculate the spring constant in $\text{N cm}^{-1}$. [2]

(c)(i) Determine the centripetal acceleration of the sphere. [2]

(c)(ii) Calculate the period of the circular motion. [2]

**Method:**
- (a) The horizontal component of the tension provides the centripetal force; the vertical component of the tension balances the weight; the combined (greater) tension means a greater extension of the spring.
- (b)(i) Radius from geometry: $r = 10.8 \sin 27^{\circ}$.
- (b)(ii) Vertically, $T\cos\theta = mg$.
- (b)(iii) Use the extra tension above equilibrium, $\Delta T = 3.2 - 0.29 \times 9.81$, and the extra extension, $\Delta x = 10.8 - 8.5$ cm; $k = \Delta T/\Delta x$.
- (c)(i) The horizontal component of the tension provides the centripetal force: $a = T\sin\theta/m$.
- (c)(ii) Use $a = r\omega^{2}$ with $\omega = 2\pi/T_{\text{period}}$, so $T_{\text{period}} = 2\pi\sqrt{r/a}$.

**Answer:**
- (a) The horizontal force on the sphere causes its centripetal acceleration; the weight of the sphere is now balanced by the vertical component of the tension (or: the horizontal and vertical components of the force combine to give a greater tension); a greater tension means a greater extension of the spring.
- (b)(i) $r = 10.8 \sin 27^{\circ} = 4.9$ cm.
- (b)(ii) $T = \dfrac{0.29 \times 9.81}{\cos 27^{\circ}} = 3.2 \ \text{N}$.
- (b)(iii) $k = \dfrac{\Delta T}{\Delta x} = \dfrac{0.36}{2.3} = 0.15 \ \text{N cm}^{-1}$.
- (c)(i) $a = \dfrac{T\sin\theta}{m} = \dfrac{3.2 \sin 27^{\circ}}{0.29} = 5.0 \ \text{m s}^{-2}$.
- (c)(ii) $T_{\text{period}} = 2\pi\sqrt{\dfrac{r}{a}} = 2\pi\sqrt{\dfrac{0.049}{5.0}} = 0.62 \ \text{s}$.

**What the examiner wants:** (a) three B1s for the three linked ideas. (b)(i) A1. (b)(ii) C1 for the vertical resolution, A1 for 3.2 N. (b)(iii) C1 for using the extra tension (3.2 - 0.29 $\times$ 9.81) and extra extension, A1 for the value - using the total tension or total length loses the method mark. (c)(i) C1 for using the horizontal component, A1. (c)(ii) C1 + A1. Note the mark scheme itself uses $T$ for the period here, which clashes with tension; in your answer, write "period $= 0.62$ s" to avoid confusion.

### Practice set from the coursebook (Cambridge International A Level Physics, Chapter 17 end-of-chapter questions)

These are the coursebook's own exam-style questions, with the mark allocations printed in the book. They are ideal practice because each one is a question type that has appeared on real papers:

1. (a) Explain what is meant by a radian. [1] (b) A body completes one revolution in 15 s. Calculate its angular velocity. [2]
2. A roller-coaster truck loops a loop of diameter 8.0 m; at the position shown there is no reaction force between the wheels and the track. (a) What provides the centripetal force? [1] (b) Calculate the speed of the truck, $g = 9.8 \ \text{m s}^{-2}$. [3]
3. A toy of mass 60 g sits on the edge of a turntable of diameter 15.0 cm making 20 revolutions per minute. (a) Describe what is meant by centripetal force. [1] (b)(i) Calculate the centripetal force on the toy. [4] (b)(ii) Explain why the toy falls off when the speed is increased. [2]
4. A metal ball of mass 50 g on a string of length 1.50 m is raised through 70 cm and released; it swings down in a circular arc. (a) Determine the speed at the bottom. [2] (b) Calculate the tension when the string is vertical. [4] (c) Explain why the tension is not equal to the weight of the ball. [2]
5. A car hits a patch of oil while going round a bend and slides off onto the grass. Explain, using circular motion, why the car came off the road. [2]
6. An aeroplane banks to make a horizontal turn at 75 m s$^{-1}$ with turning radius 80 m. (a) Draw and label the forces on the aeroplane. [2] (b) Calculate the angle the aeroplane makes with the horizontal. [4]
7. (a) Explain what is meant by angular velocity. [2] (b) A rubber bung of mass 200 g swings in a horizontal circle of radius 40 cm, the string at $56^{\circ}$ to the vertical. Calculate (i) the tension in the string, [3] (ii) the angular velocity of the bung, [2] (iii) the time for one complete revolution. [1]
8. (a) Explain what is meant by a centripetal force. [2] (b) A bucket of water of total mass 5.4 kg is swung in a vertical circle of diameter 1.8 m. (i) Calculate the minimum speed at the top so the water stays in. [3] (ii) Assuming constant speed, find the force on the hand at the bottom. [2]
9. A pilot sits in a seat on the end of a 5.0 m arm spun at high speed. (a) Describe what the pilot feels, relating it to the centripetal force. [3] (b)(i) At top speed the centripetal force equals six times the pilot's weight. Calculate the speed. [3] (b)(ii) Calculate the revolutions per minute. [2]
10. (a) Show that one revolution contains $2\pi$ radians. [2] (b) A centrifuge spins at 540 rpm with the test tube end 10 cm from the axis. (i) Calculate the angular velocity. [2] (ii) Calculate the centripetal force on a particle of mass 20 mg at the end of the tube. [2] (c) Explain, by comparing forces, why the centrifuge separates particles more effectively than letting them settle under gravity. [2]

Working through all ten, timed, is the best preparation for the Paper 4 questions this chapter produces.

---

# Chapter 18: Gravitational Fields
> Source: `physics/notes/chapter-18-gravitational-fields-notes.md`

## 4. Methods (Question Types & Methods)

Cambridge can ask about gravitational fields in the following ways. For each, here is the step-by-step method that gets full marks.

### Type 1: State Newton's law of gravitation (2 marks)

Write: "The force between two point masses is directly proportional to the product of their masses and inversely proportional to the square of their separation." The mark scheme (9702/41/O/N/19, 9702/41/M/J/18) awards one mark for the proportionality ideas and one mark for the idea that it applies to point masses. **Do not forget "point masses"** - the examiner report notes this was the most common omission.

### Type 2: Define gravitational field strength (1-2 marks)

"Force per unit mass" - and if there is room, "the gravitational force exerted per unit mass on a small object placed at that point." The mark scheme (9702/41/M/J/21) wants exactly "force per unit mass". Do not write a definition of gravitational potential instead - this was a common error in 9702/s21.

### Type 3: Define gravitational potential (2 marks)

Two B1 marks (9702/41/O/N/21, 9702/42/F/M/20):
1. "work done per unit mass"
2. "(work done in) moving a mass from infinity (to the point)"

The examiner specifically warns (9702/w21): saying "work done in moving a mass" without making clear it is *per unit mass* does not get the mark.

### Type 4: Calculate the gravitational force between two masses

Method:
1. Convert everything to SI (g to kg, mm/cm/km to m).
2. Substitute into $F = \frac{GMm}{r^2}$.
3. Quote the answer with units (N).

Example shape (coursebook Q1): two 100 g objects 1.0 cm apart: $F = \frac{6.67 \times 10^{-11} \times 0.1 \times 0.1}{(0.01)^2} = 6.7 \times 10^{-9}$ N.

### Type 5: Find $g$ at the surface or at a height above a planet

Method:
1. Identify the distance $r$ **from the centre**: at the surface $r = R$; at height $h$, $r = R + h$. This is where most marks are lost.
2. Substitute into $g = \frac{GM}{r^2}$.
3. Give units N kg$^{-1}$ (or m s$^{-2}$).

If the question gives density $\rho$ and diameter instead of mass, first find $M = \rho \times \frac{4}{3}\pi R^3$, then $g = \frac{GM}{R^2}$ (coursebook end-of-chapter Q4 does exactly this).

### Type 6: Find gravitational potential at a point

Method:
1. Use $r$ from the centre of the mass.
2. $\phi = -\frac{GM}{r}$. The minus sign is essential - potential is always negative.
3. Units: J kg$^{-1}$.
4. If there are **two or more masses**, add the potentials as scalars: $\phi = \phi_1 + \phi_2 = -\frac{GM_1}{r_1} - \frac{GM_2}{r_2}$. Both terms are negative, so the answer is more negative than either alone (9702/41/O/N/21 Q2(b)(iii) - many candidates subtracted instead of adding).

### Type 7: Work done / change in potential energy moving a mass

Method (matches the 9702/41/M/J/21 and 9702/42/F/M/20 mark schemes):
1. Write $\Delta E_P = GMm\left(\frac{1}{r_1} - \frac{1}{r_2}\right)$ where $r_1$ is the starting radius and $r_2$ the final radius.
2. Substitute $G$, $M$, $m$, $r_1$, $r_2$.
3. The sign tells you the direction: positive means energy was put in (moved further out), negative means energy was released (moved inward).
4. Never write $\frac{1}{r_2 - r_1}$ instead of $\frac{1}{r_1} - \frac{1}{r_2}$ - a flagged error in the 9702/s19 examiner report.
5. To go from potential to potential energy: multiply the potential by the mass: $E_P = m\phi$.

### Type 8: Escape velocity / energy to escape

Method:
1. Energy to escape per unit mass $= \frac{GM}{R}$ (the magnitude of the surface potential) - or $-\phi$ at the launch point.
2. Equate kinetic energy to potential energy: $\frac{1}{2}mv^2 = \frac{GMm}{R}$, cancel $m$, solve $v = \sqrt{\frac{2GM}{R}}$.
3. In a "show that" question, show the substitution for the potential energy first, then the energy equality (9702/41/O/N/13 Q1: show $\Delta E_P = 1.27 \times 10^7$ J for a 4.5 kg rock on the Moon, then $v = 2.4 \times 10^3$ m s$^{-1}$).

### Type 9: Orbital speed of a satellite or planet

Method (matches 9702/41/M/J/21 Q1(b) and coursebook Worked Example 3):
1. State the physics: gravitational force provides the centripetal force: $\frac{GMm}{r^2} = \frac{mv^2}{r}$.
2. Cancel $m$: $v^2 = \frac{GM}{r}$.
3. If you are given the period instead of the speed, use $v = \frac{2\pi r}{T}$.
4. Take the square root at the end - do not forget this (coursebook hint; also a source of slips).
5. Convert minutes to seconds if the period is given in minutes.

### Type 10: Orbital radius from period (including geostationary radius)

Method (matches 9702/42/F/M/20 Q1(b)(i) and 9702/41/O/N/19 Q1(b)(ii)):
1. State: gravitational force provides the centripetal force.
2. Use $\frac{GMm}{r^2} = mr\omega^2$ with $\omega = \frac{2\pi}{T}$, giving $r^3 = \frac{GMT^2}{4\pi^2}$.
3. Substitute $T$ in seconds ($24$ h $= 86400$ s; $94$ min $= 5640$ s).
4. Cube root at the end.
5. For a geostationary question, also convert the final radius to a height: height $= r - R$ where $R = 6.4 \times 10^6$ m.

### Type 11: Show $T^2 \propto r^3$ or find the constant $k$ in $r^3 = kT^2$

Method (matches 9702/41/M/J/18 Q1):
1. Equate $\frac{GMm}{r^2}$ to $\frac{mv^2}{r}$ (or $mr\omega^2$).
2. Substitute $v = \frac{2\pi r}{T}$ (or $\omega = \frac{2\pi}{T}$).
3. Rearrange to $r^3 = \frac{GM}{4\pi^2}T^2$, so $k = \frac{GM}{4\pi^2}$.
4. To find $M$: calculate $k$ from data ($k = \frac{R^3}{T^2}$ for one or more planets), then $M = \frac{4\pi^2 k}{G}$. Using several data points and showing they agree earns an extra mark (the 9702/41/M/J/18 mark scheme gives a B1 for using two or three values).

### Type 12: Ratio questions ($g$ at surface vs $g$ in orbit)

Method (matches 9702/42/F/M/20 Q1(b)(iii)):
1. Write $g = \frac{GM}{r^2}$ for both locations.
2. $G$ and $M$ cancel, so the ratio is $\left(\frac{r_{\text{orbit}}}{r_{\text{surface}}}\right)^2$ (note the inversion - the larger radius gives the smaller $g$).
3. Example: $\left(\frac{2.4 \times 10^8}{6.4 \times 10^6}\right)^2 = 1400$, so the surface field is 1400 times stronger.

### Type 13: Point of zero resultant field between two masses

Method (matches 9702/41/O/N/21 Q2(b)):
1. Explain (2 marks): the fields from the two masses act in **opposite directions** at points between them; the resultant is zero where the two field strengths are **equal in magnitude**. "The fields cancel out" alone is not enough - say equal magnitude, opposite direction.
2. Let $x$ = distance from one mass, so distance from the other is $(d - x)$ where $d$ = separation.
3. Set $\frac{GM_1}{x^2} = \frac{GM_2}{(d-x)^2}$.
4. Cancel $G$, take square roots of both sides (much easier than expanding into a quadratic): $\frac{\sqrt{M_1}}{x} = \frac{\sqrt{M_2}}{d-x}$, then solve for $x$.
5. The zero-field point is closer to the **smaller** mass (its weaker field needs less distance to fall to match).
6. Check: at that same point the potential is *not* zero - it is the most negative (maximum magnitude) point on the line.

### Type 14: Potential at a point due to two masses

Method (matches 9702/41/O/N/21 Q2(b)(iii)):
1. Find the distance of the point from each mass.
2. $\phi = -\frac{GM_1}{r_1} - \frac{GM_2}{r_2}$ - add the two (both negative) values.
3. Units J kg$^{-1}$. Do not subtract the magnitudes; potential is scalar.

### Type 15: $g = -d\phi/dr$ and $\phi$-$r$ graph questions

Method (matches 9702/42/O/N/21 Q2):
1. State: field strength equals the (negative of the) potential gradient: $g = -\frac{d\phi}{dr}$.
2. On a $\phi$-$r$ graph, $g$ is found from the gradient of the curve (steep curve = strong field, flat curve = weak field).
3. At a maximum of $\phi$, gradient is zero so $g = 0$: the zero-field point is at the maximum of the potential, not where $\phi = 0$.
4. When sketching $g$ vs $x$ between two masses: $g$ is negative near one mass and positive near the other, crossing zero at the point of maximum potential.
5. Comparing two planets: the more massive planet has a deeper potential well (more negative $\phi$ at the surface) and a steeper potential gradient (larger $g$) at its surface.

### Type 16: Sketching field lines / comparing fields

Method (coursebook end-of-chapter Q3, Q9):
1. Radial field: arrows point towards the centre; lines spread out with distance; more closely spaced lines = stronger field.
2. Uniform field (building scale): parallel, equally spaced, all pointing the same way.
3. Sketching $\phi$ vs $r$ for a planet of mass $2M$: same radius, curve twice as deep at the surface ($-\frac{2GM}{R}$ vs $-\frac{GM}{R}$).
4. For a planet of the same mass but radius $2R$: shallower well at the surface ($-\frac{GM}{2R}$), curve extends to larger $r$.
5. The least energy to escape comes from the shallowest well (smallest $\frac{GM}{R}$).

---

## 5. Solved Examples

All solutions are written the way the mark scheme wants: physics statement first, then equation, substitution, answer with units. The past paper questions are real, verified Paper 4 questions (question codes given so you can find the originals), with mark allocations from the published mark schemes.

### Example 1: Gravitational force between a satellite and the Earth (coursebook Q1(c))

**Question:** A satellite of mass $1.4 \times 10^4$ kg orbits the Earth at a distance of $6.8 \times 10^6$ m from the Earth's centre. The mass of the Earth is $6.0 \times 10^{24}$ kg. Calculate the gravitational force on the satellite.

**Method:**
1. State Newton's law of gravitation: $F = \frac{GMm}{r^2}$.
2. Substitute $G = 6.67 \times 10^{-11}$, $M = 6.0 \times 10^{24}$ kg, $m = 1.4 \times 10^4$ kg, $r = 6.8 \times 10^6$ m (from the centre).
3. Quote the answer with units (N).

**Answer:**

$$F = \frac{6.67 \times 10^{-11} \times 6.0 \times 10^{24} \times 1.4 \times 10^4}{(6.8 \times 10^6)^2} = \frac{5.60 \times 10^{18}}{4.62 \times 10^{13}} = 1.2 \times 10^5 \text{ N}$$

The satellite experiences a gravitational force of about $1.2 \times 10^5$ N towards the Earth's centre.

**What the examiner wants:** the correct substitution into $F = \frac{GMm}{r^2}$ with $r$ measured from the Earth's centre, and the answer quoted in N.

### Example 2: $g$ at the surface of the Moon and at a height above the Earth (coursebook Q4(a)(i))

**Question:** (a) The Moon has mass $7.4 \times 10^{22}$ kg and radius $1.74 \times 10^6$ m. Calculate the gravitational field strength at the Moon's surface. (b) Calculate the gravitational field strength at a height of 300 km above the Earth's surface. (Earth: $M = 6.0 \times 10^{24}$ kg, $R = 6.4 \times 10^6$ m.)

**Method:**
1. Use $g = \frac{GM}{r^2}$ with $r$ = distance from the centre.
2. For (a), $r = R$ = the Moon's radius.
3. For (b), convert 300 km to metres and add the Earth's radius: $r = R + h$. This is the step where marks are lost.

**Answer:**

$$g = \frac{GM}{r^2} = \frac{6.67 \times 10^{-11} \times 7.4 \times 10^{22}}{(1.74 \times 10^6)^2} = 1.63 \text{ N kg}^{-1}$$

$$r = R + h = 6.4 \times 10^6 + 3.0 \times 10^5 = 6.7 \times 10^6 \text{ m}$$

$$g = \frac{GM}{r^2} = \frac{6.67 \times 10^{-11} \times 6.0 \times 10^{24}}{(6.7 \times 10^6)^2} = 8.9 \text{ N kg}^{-1}$$

(Compare $9.81$ N kg$^{-1}$ at the surface - the field has dropped by about 9% at 300 km.)

**What the examiner wants:** $r = R + h$ for a height above the surface (never use the height alone), and units N kg$^{-1}$ (or m s$^{-2}$).

### Example 3: Mass and density of the Earth from surface $g$ (coursebook Worked Example 1)

**Question:** The Earth has radius $6.4 \times 10^6$ m and surface field strength $9.81$ N kg$^{-1}$. Determine the mass of the Earth and its mean density.

**Method:**
1. Rearrange $g = \frac{GM}{R^2}$ for $M = \frac{gR^2}{G}$.
2. Find the density from $\rho = \frac{M}{\frac{4}{3}\pi R^3}$.

**Answer:**

$$M = \frac{9.81 \times (6.4 \times 10^6)^2}{6.67 \times 10^{-11}} = 6.0 \times 10^{24} \text{ kg}$$

$$\rho = \frac{M}{\frac{4}{3}\pi R^3} = \frac{6.0 \times 10^{24}}{\frac{4}{3}\pi (6.4 \times 10^6)^3} = 5500 \text{ kg m}^{-3}$$

**What the examiner wants:** rearranging $g = \frac{GM}{R^2}$ correctly and using the full sphere volume $\frac{4}{3}\pi R^3$ - a common slip is using $R^3$ instead of the volume formula, or forgetting to cube the radius.

### Example 4: Gravitational potential and potential energy of a spacecraft (coursebook Worked Example 2)

**Question:** A planet has diameter $6.8 \times 10^6$ m and mass $4.9 \times 10^{23}$ kg. A rock of mass 200 kg, initially at rest and far from the planet, falls and hits the surface. Calculate the change in the rock's potential energy and its impact speed.

**Method:**
1. Radius $r = \frac{6.8 \times 10^6}{2} = 3.4 \times 10^6$ m (diameter, not radius - halve it).
2. Far away, $E_P = 0$, so the change in potential energy is $\Delta E_P = 0 - \left(-\frac{GMm}{r}\right) = \frac{GMm}{r}$.
3. All of this becomes kinetic energy (no atmosphere): $\frac{1}{2}mv^2 = \Delta E_P$.

**Answer:**

$$\Delta E_P = \frac{6.67 \times 10^{-11} \times 4.9 \times 10^{23} \times 200}{3.4 \times 10^6} = 1.9 \times 10^9 \text{ J}$$

$$\frac{1}{2}mv^2 = 1.9 \times 10^9$$

$$v = \sqrt{\frac{2 \times 1.9 \times 10^9}{200}} = 4.4 \times 10^3 \text{ m s}^{-1}$$

**What the examiner wants:** the impact speed does not depend on the rock's mass - $m$ cancels from $\frac{1}{2}mv^2 = \frac{GMm}{r}$. Also, halve the diameter to get the radius before substituting.

### Example 5: Satellite moved to a higher orbit (9702/41/M/J/21 Q1, 10 marks)

**Question:** The Earth is an isolated uniform sphere of mass $6.0 \times 10^{24}$ kg. A satellite of mass 1200 kg is in a circular orbit with period 94 minutes. (a) Define gravitational field strength. (b) Calculate the radius of the orbit. (c)(i) Show that in a new orbit of period 150 minutes the radius is $9.4 \times 10^6$ m. (c)(ii) State, with a reason, whether the gravitational potential energy increases or decreases. (c)(iii) Determine the magnitude of the change in potential energy.

**Method:**
- (a) Write "force per unit mass" and nothing else.
- (b) State the physics: gravitational force provides the centripetal force, $\frac{GMm}{r^2} = mr\omega^2$ with $\omega = \frac{2\pi}{T}$, giving $r^3 = \frac{GMT^2}{4\pi^2}$. Convert 94 minutes to seconds ($94 \times 60 = 5640$ s) and substitute. Cube root at the end.
- (c)(i) Use $T^2 \propto r^3$: $\frac{r_2^3}{r_1^3} = \left(\frac{T_2}{T_1}\right)^2$, so $r_2 = r_1 \left(\frac{150}{94}\right)^{2/3}$. Show every step - "show that" questions need full working.
- (c)(ii) The satellite moves further from the Earth, so its potential energy increases (becomes less negative, since $E_P = -\frac{GMm}{r}$ and $r$ increases).
- (c)(iii) $\Delta E_P = GMm\left(\frac{1}{r_1} - \frac{1}{r_2}\right)$ with $r_1 = 6.9 \times 10^6$ m and $r_2 = 9.4 \times 10^6$ m.

**Answer:**
- (a) Gravitational field strength is the force per unit mass.
- (b) $r = 6.9 \times 10^6$ m.
- (c)(i) $r_2 = 9.4 \times 10^6$ m (shown).
- (c)(ii) It increases, because the separation from the Earth's centre increases.
- (c)(iii) $\Delta E_P = 1.9 \times 10^{10}$ J. Full-mark working:

$$\Delta E_P = GMm\left(\frac{1}{r_1} - \frac{1}{r_2}\right) = 6.67 \times 10^{-11} \times 6.0 \times 10^{24} \times 1200 \times \left(\frac{1}{6.9 \times 10^6} - \frac{1}{9.4 \times 10^6}\right) = 1.9 \times 10^{10} \text{ J}$$

**What the examiner wants:** (a) "force per unit mass" (B1). (b) $\frac{GMm}{r^2} = mr\omega^2$ with $\omega = \frac{2\pi}{T}$ (C1), substitution (C1), $r = 6.9 \times 10^6$ m (A1). (c)(i) ratio $r^3/T^2$ constant (C1) with clear working (A1) - unclear presentation caused confusion between $r^3$ and $r$ in 9702/s21. (c)(ii) increases because separation increases (B1). (c)(iii) formula (C1), substitution (C1), $1.9 \times 10^{10}$ J (A1).

### Example 6: Orbital speed and period of the Moon (coursebook Worked Example 3)

**Question:** The Moon orbits the Earth at an average distance of $3.84 \times 10^8$ m from the Earth's centre. The mass of the Earth is $6.0 \times 10^{24}$ kg. Calculate the Moon's orbital speed and its orbital period.

**Method:**
1. State: gravitational force provides the centripetal force, so $v^2 = \frac{GM}{r}$.
2. Take the square root to find $v$.
3. Use $T = \frac{2\pi r}{v}$ for the period, and convert seconds to days.

**Answer:**

$$v^2 = \frac{GM}{r} = \frac{6.67 \times 10^{-11} \times 6.0 \times 10^{24}}{3.84 \times 10^8} = 1.04 \times 10^6$$

$$v = 1.0 \times 10^3 \text{ m s}^{-1}$$

$$T = \frac{2\pi r}{v} = \frac{2\pi \times 3.84 \times 10^8}{1.0 \times 10^3} = 2.4 \times 10^6 \text{ s} \approx 27.8 \text{ days}$$

**What the examiner wants:** the orbital speed is independent of the satellite's mass (it cancels), and the square root must actually be taken.

### Example 7: Geostationary orbit radius (coursebook worked calculation)

**Question:** Calculate the radius and the height above the Earth's surface of a geostationary orbit. ($T = 24$ h $= 86400$ s, Earth $M = 6.0 \times 10^{24}$ kg, $R = 6.4 \times 10^6$ m.)

**Method:**
1. Use $r^3 = \frac{GMT^2}{4\pi^2}$ with $T$ in seconds.
2. Cube root to find $r$.
3. Subtract the Earth's radius to get the height above the surface: height $= r - R$.

**Answer:**

$$r^3 = \frac{6.67 \times 10^{-11} \times 6.0 \times 10^{24} \times (86400)^2}{4\pi^2} = 7.66 \times 10^{22} \text{ m}^3$$

$$r = 4.23 \times 10^7 \text{ m} = 42\,300 \text{ km from the Earth's centre}$$

$$\text{height above surface} = r - R = 4.23 \times 10^7 - 6.4 \times 10^6 = 3.6 \times 10^7 \text{ m} \approx 36\,000 \text{ km}$$

**What the examiner wants:** $T$ in seconds (86400 s, not 24), the cube root taken, and the final height found by subtracting the Earth's radius from the orbital radius.

### Example 8: Escape speed from the Moon (9702/41/O/N/13 Q1, 7 marks)

**Question:** The Moon may be considered as an isolated sphere of radius $1.74 \times 10^6$ m with mass $7.35 \times 10^{22}$ kg. A rock of mass 4.50 kg sits on the Moon's surface. (a) Define gravitational potential at a point. (b)(i) Show that the change in gravitational potential energy of the rock in moving it from the surface to infinity is $1.27 \times 10^7$ J. (b)(ii) Determine the escape speed, explaining your working. (c) State and explain whether the minimum speed for the rock to reach the Earth differs from the escape speed.

**Method:**
- (a) Write: "the work done per unit mass in bringing a mass from infinity to the point" (two B1 ideas: work done per unit mass; from infinity).
- (b)(i) Moving to infinity means $r_2 \to \infty$, so $\frac{1}{r_2} \to 0$ and $\Delta E_P = \frac{GMm}{R}$. Show the substitution.
- (b)(ii) Equate kinetic energy to the potential energy change: $\frac{1}{2}mv^2 = \Delta E_P$, and solve for $v$. State that the change in gravitational potential energy equals the change in kinetic energy.
- (c) The Earth attracts the rock, so the potential at the Earth's position is not zero - the rock does not need enough energy to reach infinity.

**Answer:**
- (b)(i) $\Delta E_P = \frac{6.67 \times 10^{-11} \times 7.35 \times 10^{22} \times 4.5}{1.74 \times 10^6} = 1.27 \times 10^7$ J.
- (b)(ii) $v = \sqrt{\frac{2 \times 1.27 \times 10^7}{4.5}} = 2.4 \times 10^3$ m s$^{-1}$ (equivalently $v = \sqrt{\frac{2GM}{R}} = 2.4 \times 10^3$ m s$^{-1}$).
- (c) The minimum speed to reach the Earth is **less** than the escape speed, because the Earth's gravitational field attracts the rock.

**What the examiner wants:** (a) "work done per unit mass" + "from infinity" (2 B1s). (b)(i) $\Delta E_P = GMm/R$ with the substitution shown (1 mark - a "show that" question, so write every step). (b)(ii) change in g.p.e. equals change in kinetic energy (B1), $\frac{1}{2}mv^2 = 1.27 \times 10^7$ giving $v = 2.4 \times 10^3$ m s$^{-1}$ (A1). (c) lower, because the Earth attracts the rock / the potential at the Earth is not zero (M1 + A1).

### Example 9: Zero field point between the Earth and the Moon, and the potential there (9702/41/O/N/21 Q2, 9 marks)

**Question:** The Earth (mass $5.98 \times 10^{24}$ kg) and the Moon (mass $7.35 \times 10^{22}$ kg) are separated by $3.84 \times 10^8$ m. Point P is on the line joining their centres, at distance $x$ from the Earth's centre, where the resultant field is zero. (a) Define gravitational potential. (b)(i) Explain how the field strength can be zero despite two large masses nearby. (b)(ii) Show $x \approx 3.5 \times 10^8$ m. (b)(iii) Calculate the gravitational potential at P.

**Method:**
- (a) Write: "work done per unit mass" + "in moving a mass from infinity (to the point)".
- (b)(i) The fields from the two masses act in opposite directions; the resultant is zero where the two field strengths are equal in magnitude. Say both ideas - "the fields cancel" alone is not credited.
- (b)(ii) Set $\frac{GM_E}{x^2} = \frac{GM_M}{(3.84 \times 10^8 - x)^2}$. Cancel $G$ and take square roots of both sides (much easier than expanding the quadratic): $\frac{\sqrt{M_E}}{x} = \frac{\sqrt{M_M}}{3.84 \times 10^8 - x}$, then solve for $x$.
- (b)(iii) Potential is scalar - add the two (both negative) contributions: $\phi = -\frac{GM_E}{x} - \frac{GM_M}{3.84 \times 10^8 - x}$.

**Answer:**
- (b)(ii) $x = 3.5 \times 10^8$ m.
- (b)(iii) $\phi = -6.67 \times 10^{-11}\left(\frac{5.98 \times 10^{24}}{3.5 \times 10^8} + \frac{7.35 \times 10^{22}}{3.4 \times 10^7}\right) = -1.3 \times 10^6$ J kg$^{-1}$.

**What the examiner wants:** (a) "work done per unit mass" (B1) + "from infinity" (B1). (b)(i) opposite directions (B1) + equal magnitudes (B1) - the examiner report says saying the fields "cancel" without equal magnitude and opposite direction was not credited, and answers in terms of forces gained nothing (the question was about field strength). (b)(ii) equate the two field strengths (C1), solve to $x = 3.5 \times 10^8$ m (A1). (b)(iii) $\phi_E$ term (C1), $\phi_M$ term (C1), $\phi = -1.3 \times 10^6$ J kg$^{-1}$ (A1) - add the two negative contributions; potential is scalar. Note: the potential is *not* zero at P even though the field is zero - it is at its most negative value on the line.

### Example 10: TESS satellite - orbit radius, potential energy change, field ratio (9702/42/F/M/20 Q1, 10 marks)

**Question:** TESS is a satellite in a circular orbit about the Earth (mass $6.0 \times 10^{24}$ kg, radius $6.4 \times 10^6$ m). (a) Define gravitational potential at a point. (b)(i) TESS orbits in 13.7 days. Show that its orbital radius is $2.4 \times 10^8$ m. (b)(ii) Calculate the change in potential energy between TESS in orbit and TESS on the launch pad. (b)(iii) Calculate the ratio $\frac{\text{field strength at the Earth's surface}}{\text{field strength at TESS's orbit}}$.

**Method:**
- (a) Write: "work done per unit mass" + "from infinity".
- (b)(i) State gravitational force provides the centripetal force; use $r^3 = \frac{GMT^2}{4\pi^2}$ with $T$ in seconds. This is a "show that" question - write every step, including $T = 13.7 \times 24 \times 3600$ s.
- (b)(ii) $\Delta E_P = GMm\left(\frac{1}{r_1} - \frac{1}{r_2}\right)$ with $r_1 = 6.4 \times 10^6$ m (surface) and $r_2 = 2.4 \times 10^8$ m (orbit).
- (b)(iii) $G$ and $M$ cancel in the ratio: $\frac{g_{\text{surface}}}{g_{\text{orbit}}} = \left(\frac{r_{\text{orbit}}}{r_{\text{surface}}}\right)^2$ (note the inversion - larger radius, smaller $g$).

**Answer:**
- (b)(i) $r = 2.4 \times 10^8$ m (shown).
- (b)(ii) $\Delta E_P = 2.2 \times 10^{10}$ J.
- (b)(iii) $\frac{g_{\text{surface}}}{g_{\text{orbit}}} = \left(\frac{2.4 \times 10^8}{6.4 \times 10^6}\right)^2 = 1400$ - the surface field strength is 1400 times greater.

**What the examiner wants:** (a) as in Example 9(a). (b)(i) gravitational force provides centripetal force (C1), $r^3 = GMT^2/4\pi^2$ with $T$ in seconds (C1), substitution (A1). (b)(ii) $E_P = -GMm/r$ (C1), $\Delta E_P = GMm(1/r_1 - 1/r_2)$ (C1), $2.2 \times 10^{10}$ J (A1). (b)(iii) $g = GM/r^2$ (C1), ratio $= 1400$ (A1).

### Example 11: Geostationary satellite and the mass of the Earth (9702/41/O/N/19 Q1, 8 marks)

**Question:** (a) State Newton's law of gravitation. (b)(i) A geostationary satellite orbits the Earth with period 24 hours. State two features of its orbit (other than the period). (b)(ii) Given that the orbital radius is $4.23 \times 10^4$ km, determine the mass of the Earth, explaining your working.

**Method:**
- (a) Write: force directly proportional to the product of the masses and inversely proportional to the square of their separation + between point masses.
- (b)(i) State: directly above the Equator; from west to east. Do not just rephrase "geostationary".
- (b)(ii) Start from a principle: the gravitational force provides the centripetal force. Use $\frac{GM}{r^2} = r\left(\frac{2\pi}{T}\right)^2$ and solve for $M$. Convert km to m first, and square the period and cube the radius.

**Answer:**
- (b)(i) Directly above the Equator; from west to east.
- (b)(ii) $M = \frac{4\pi^2 r^3}{GT^2} = 6.0 \times 10^{24}$ kg.

**What the examiner wants:** (a) proportionality ideas (B1) + point masses (B1). (b)(i) above the Equator (B1) + west to east (B1) - the examiner report notes weak candidates repeated what "geostationary" means instead of giving these features. (b)(ii) gravitational force provides the centripetal force (B1), $\frac{GM}{r^2} = r(2\pi/T)^2$ (C1), substitution (C1), $M = 6.0 \times 10^{24}$ kg (A1). The examiner report flags: forgetting to square the period or cube the radius, power-of-ten errors from not converting km to m, and a significant number of candidates wrongly assumed $g = 9.81$ N kg$^{-1}$ at the satellite's height - never do that.

### Example 12: Planets orbiting a distant star - Kepler's third law (9702/41/M/J/18 Q1)

**Question:** (a) State Newton's law of gravitation. (b)(i) Explain whether planets in circular orbits at constant speed are in equilibrium. (b)(ii)1 Show that $R^3 = kT^2$ has $k = GM/4\pi^2$. (b)(ii)2 Use data for three planets to calculate the star's mass.

**Method:**
- (a) As in Example 11(a).
- (b)(i) They are not in equilibrium, because the direction of motion (velocity) is changing, so there is an acceleration and a resultant force.
- (b)(ii)1 Equate $\frac{GMm}{R^2} = \frac{mv^2}{R}$, substitute $v = \frac{2\pi R}{T}$, and rearrange to $R^3 = \frac{GM}{4\pi^2}T^2$ - convincing algebra earns the marks.
- (b)(ii)2 Calculate $k = \frac{R^3}{T^2}$ from the data for one planet (use several planets and show they agree for the extra mark), then $M = \frac{4\pi^2 k}{G}$.

**Answer:**
- (b)(i) Not in equilibrium - the velocity changes / the direction of motion changes / there is an acceleration / a resultant force.
- (b)(ii)1 $k = \frac{GM}{4\pi^2}$ (shown).
- (b)(ii)2 $k = 3.5(5) \times 10^{21}$, so $M = \frac{4\pi^2 k}{G} = 2.1 \times 10^{33}$ kg.

**What the examiner wants:** (b)(i) 1 mark for any one of: velocity changes, direction changes, acceleration, resultant force. (b)(ii)1 equate gravitational and centripetal force (C1), use $v = 2\pi R/T$ (M1), convincing algebra (A1). (b)(ii)2 calculate $R^3/T^2$ for one planet (C1), $3.5(5) \times 10^{21} = GM/4\pi^2$ (A1), $M = 2.1 \times 10^{33}$ kg; a further B1 for using two or three values in a valid way.

### Example 13: Measuring $G$ with a torsion balance (9702/42/M/J/19 Q1, 7 marks)

**Question:** Two point masses $M$ and $m$ are separated by distance $x$ in a vacuum. (a) State an expression for the force $F$ between them, and name any other symbol used. (b) A small sphere is deflected by a nearby large sphere; the deflection angle is $1.2 \times 10^{-3}$ rad per $8.0 \times 10^{-2}$ m of scale, and the torsion constant is $9.3 \times 10^{-10}$ N m rad$^{-1}$. Calculate the deflection angle and the torque. (c)(i) Use the torque to determine a value for $G$ (spheres: masses $1.3$ kg and $7.5 \times 10^{-3}$ kg, centre separation $6.0 \times 10^{-2}$ m, lever arm $8.0 \times 10^{-2}$ m). (c)(ii) Suggest one reason the result may differ from the accepted value.

**Method:**
- (a) $F = \frac{GMm}{x^2}$, where $G$ is the (universal) gravitational constant. Name $G$ - candidates who did not lost the mark.
- (b) angle $= \frac{\text{scale reading}}{\text{scale length}}$; torque $= \text{angle} \times \text{torsion constant}$.
- (c)(i) Set the torque due to the gravitational force equal to the restoring torque: $F \times \text{lever arm} = \text{torque}$, with $F = \frac{G \times 1.3 \times 7.5 \times 10^{-3}}{(6.0 \times 10^{-2})^2}$, and solve for $G$.
- (c)(ii) Quote one reason from the list: the law applies only to point masses / sphere radii not small compared with separation / spheres may not be uniform / masses not isolated / force between L and the rod / electrostatic forces between spheres.

**Answer:**
- (a) $F = \frac{GMm}{x^2}$, $G$ = gravitational constant.
- (b) angle $= \frac{1.2 \times 10^{-3}}{8.0 \times 10^{-2}} = 1.5 \times 10^{-2}$ rad; torque $= 1.5 \times 10^{-2} \times 9.3 \times 10^{-10} = 1.4 \times 10^{-11}$ N m.
- (c)(i) $G = 6.4 \times 10^{-11}$ N m$^2$ kg$^{-2}$.

**What the examiner wants:** (a) 1 mark - many candidates forgot to name $G$, or called $x$ the "radius" instead of the separation. (b) 2 marks for the two calculations. (c)(i) $F \times 8.0 \times 10^{-2} = 1.4 \times 10^{-11}$ (C1), full substitution (C1), $G = 6.4 \times 10^{-11}$ N m$^2$ kg$^{-2}$ (A1). (c)(ii) 1 mark for any one valid reason (e.g. spheres not point masses / not isolated / electrostatic forces).

### Example 14: Relationship between $\phi$ and $g$, potential graphs (9702/42/O/N/21 Q2)

**Question:** (a) State the relationship between gravitational potential and gravitational field strength. (b) A moon (mass $M$, radius $R$) orbits a planet (mass $3M$, radius $2R$). A graph of $\phi$ against $x$ between them is given. Explain why the potential is negative. Compare the potential at the surfaces of the planet and the moon. Sketch $g$ against $x$.

**Method:**
- (a) State: field strength equals the potential gradient, with a reference to the minus sign: $g = -\frac{d\phi}{dr}$.
- (b) Negative potential: potential is zero at infinity, the force is attractive, so a mass moving in from infinity loses potential energy (three separate ideas, three B1s).
- (b) Comparison: the potential at the planet's surface is more negative (deeper well); the potential gradient is steeper at the planet's surface; the maximum potential is nearer the moon (any two for B2).
- (b) Sketch of $g$ against $x$: starts with decreasing gradient magnitude at $2R$, finishes with increasing gradient at $D - R$; $g = 0$ at the point of maximum potential; negative near one sphere, positive near the other (three B1s).

**Answer:**
- (a) $g = -\frac{d\phi}{dr}$ - field strength equals (negative of) the potential gradient.
- (b) The potential is negative because it is zero at infinity and the force is attractive, so energy is lost moving in from infinity. The planet's well is deeper and steeper; $g$ crosses zero at the point of maximum potential.

**What the examiner wants:** (a) field strength equals potential gradient (M1) + reference to the minus sign (A1). (b) three separate B1s for why potential is negative; any two of the three comparison points for B2; three B1s for the sketch (zero at the maximum of $\phi$, not where $\phi = 0$).

**Pattern to notice**: definitions (1-2 marks) open the question; then one "show that" orbital calculation (2-3 marks); then a potential-energy change or potential calculation (3 marks); occasionally a graph sketch. Total 8-10 marks, always on Paper 4.

---

---

# Chapter 19: Oscillations
> Source: `physics/notes/chapter-19-oscillations-notes.md`

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

---

# Chapter 21: Thermal Physics
> Source: `physics/notes/chapter-21-thermal-physics-notes.md`

## 4. Methods (Question Types & Methods)

Cambridge asks the same few thermal questions year after year. Here is how to attack each one.

### Type 1: "Calculate the energy to heat something and change its state"

The question gives you a mass, a starting state, an ending state, and values of $c$ and $L$. You must add up the energy for each stage.

Method:

1. Write down the journey as a chain of stages, e.g. ice at $-18^\circ\text{C}$ to water at $20^\circ\text{C}$ = heat ice + melt ice + heat water.
2. Check the units of $c$ and $L$: if they are per gram ($\text{J g}^{-1}\text{K}^{-1}$ or $\text{J g}^{-1}$), keep the mass in grams; if per kg, convert the mass to kg. Mixing these up destroys the answer.
3. For each stage decide: temperature change (use $E = mc\Delta\theta$) or change of state (use $E = mL$).
4. Sum every stage. If the question mentions heat losses, add a loss term or state the assumption that the system is insulated.

### Type 2: "Use the first law with given $q$ and $w$"

Method:

1. Read the question for direction words. "Heated", "energy supplied to the gas", "heat transferred to the system" mean $q$ positive. "Loses heat", "cools by radiating" mean $q$ negative.
2. "Compressed", "work done **on** the gas" mean $W$ positive. "Expands", "does work on its surroundings" mean $W$ negative. If the gas expands at constant pressure with volume change $\Delta V$, the work done by the gas is $p\Delta V$, so $W = -p\Delta V$ in the first law.
3. Substitute into $\Delta U = q + W$ and state the answer with units and the correct sign (a negative $\Delta U$ means internal energy decreased).

### Type 3: "Find specific heat capacity from experiment data"

Method:

1. Find the power supplied: $P = VI$ (or it is given directly, or given via a wattmeter/joulemeter reading).
2. Energy supplied in time $t$: $E = Pt$.
3. If one temperature rise $\Delta\theta$ is measured: $c = Pt/(m\Delta\theta)$.
4. If a graph of $\theta$ against $t$ is given: take the gradient of the straight line, then $c = P/(m \times \text{gradient})$.
5. Comment on heat losses: energy escaping to the surroundings means the measured $c$ is too high (a systematic error). Starting below room temperature, insulating, and heating slowly reduce the problem.

### Type 4: "Find specific latent heat"

Method:

1. Measure (or read off a graph) the mass that changes state and the time interval, and find the heater power $P = VI$.
2. Energy supplied $= Pt$. If no heat loss is assumed: $L = Pt/m$.
3. With heat losses, correct for them:
   - **Heater-off measurement**: measure the mass that changes state due to the surroundings alone in the same time, and subtract it from the heater-on mass (this is the funnel experiment for ice, w08/04 Q2).
   - **Two-power method**: run at two different heater powers for equal times; the heat loss term is the same in both runs, so subtracting the two energy equations eliminates it (w19/41 Q3).
4. State whether the result is an over- or underestimate and why (see Section 7).

### Type 5: "Explain the regions of a heating/cooling curve"

Method:

1. Sloping sections: temperature changes, so the **kinetic energy** of the molecules changes (faster/slower motion); separation barely changes, so potential energy is roughly constant.
2. Flat sections: a change of state is happening, so bonds are being broken or formed and the **potential energy** changes; kinetic energy (and therefore temperature) is constant.
3. When asked why melting needs less energy than boiling: melting breaks one or two bonds per molecule, boiling breaks all of them (eight or nine per molecule).
4. For a cooling curve, remember the temperature can stay steady while energy is still being lost - the energy loss goes into forming bonds, not lowering KE.

### Type 6: "Mixture / temperature change (calorimetry) problems"

These give you a hot substance and a cold substance (often ice added to warm water, sometimes in a container that also changes temperature) and ask for a final temperature or a value of $c$ or $L$.

Method:

1. State the energy balance: energy lost by the hot bodies = energy gained by the cold bodies (assuming no exchange with the surroundings).
2. Write one term for every body that changes temperature: $mc\Delta\theta$ (use the actual temperature change of each, e.g. $38 - 23$ for the warm water, $0 - (-18)$ for the ice while warming).
3. Write an $mL$ term for every body that changes state (the melting ice).
4. Solve for the unknown. Remember the final equilibrium temperature applies to everything, and any melted ice is water that then warms up.

The classic example (s18/42 Q3): warm water + aluminium can + ice at $-18^\circ\text{C}$. Energy lost by can and water $= mc\Delta\theta$ for each; energy gained by the ice $=$ warming the ice $+$ melting it $+$ warming the melted water.

### Type 7: "Which energy goes to KE or PE on each graph section?"

Method: on a temperature-time graph, **sloping** sections are KE changes (molecules moving faster or slower) and **flat** sections are PE changes (bonds broken or formed at a change of state). On a potential energy against separation graph, remember that PE is negative for bonded molecules and rises towards zero as molecules separate - so separating molecules increases their potential energy.

### Type 8: Definitions and short explanations (worth easy marks, learn them word-perfect)

- Specific heat capacity: energy required per unit mass of a substance to raise its temperature by 1 K (or 1 $^\circ\text{C}$).
- Specific latent heat: energy required per kilogram of a substance to change its state without any change in temperature.
- Specific latent heat of fusion: as above for melting (solid to liquid).
- Specific latent heat of vaporisation: as above for boiling (liquid to gas).
- Internal energy: the sum of the random distribution of kinetic and potential energies of the atoms or molecules of a system.
- Absolute zero: the lowest possible temperature, $0\,\text{K}$ ($-273.15^\circ\text{C}$), at which no more energy can be removed from a substance.
- Thermal equilibrium: two objects in contact at the same temperature, with no net transfer of thermal energy between them.

### Type 9: Thermometer questions

- State which thermometric property the device uses (resistance of a metal, e.m.f. of a thermocouple, volume of a gas at constant pressure, density of a liquid, etc.).
- Explain why the thermodynamic scale is better: it does not depend on the property of any particular substance.
- Choose a thermometer for a job using the table in Section 1.3 (thermocouple for a point measurement or a wide range; resistance thermometer for accuracy over a wide range; thermistor for a sensitive, narrow-range measurement).

---

## 5. Solved Examples

Real coursebook and CAIE past-paper questions, worked fully. Each one shows the question, the method, the answer, and the mark-scheme point the examiner is looking for.

### Example 1: Finding specific heat capacity from $E = mc\Delta\theta$ (coursebook worked example)

**Question:** $26\,400\,\text{J}$ of energy is supplied to a well-insulated $2.0\,\text{kg}$ block of aluminium, and its temperature rises from $20^\circ\text{C}$ to $35^\circ\text{C}$. Determine the specific heat capacity of aluminium.

**Method:**
1. Write down the known quantities: $E = 26\,400\,\text{J}$, $m = 2.0\,\text{kg}$, $\Delta\theta = 35 - 20 = 15^\circ\text{C}$ ($= 15\,\text{K}$).
2. Rearrange $E = mc\Delta\theta$ to make $c$ the subject: $c = \frac{E}{m\Delta\theta}$.
3. Substitute and calculate.

**Answer:**

$$c = \frac{E}{m\Delta\theta} = \frac{26\,400}{2.0 \times 15} = 880\,\text{J kg}^{-1}\text{K}^{-1}$$

$c = 880\,\text{J kg}^{-1}\text{K}^{-1}$, which matches the accepted value for aluminium.

**What the examiner wants:** the correct rearrangement of $E = mc\Delta\theta$, the temperature change taken as $35 - 20 = 15\,\text{K}$ (not 35 K), and the answer quoted with units.

### Example 2: Multi-stage heating with a change of state (coursebook worked example)

**Question:** How much energy is needed to change $0.20\,\text{kg}$ of ice at $-18^\circ\text{C}$ into water at $20^\circ\text{C}$? Data: $c_{\text{ice}} = 2100\,\text{J kg}^{-1}\text{K}^{-1}$, $L_{\text{fusion}} = 3.30 \times 10^5\,\text{J kg}^{-1}$, $c_{\text{water}} = 4180\,\text{J kg}^{-1}\text{K}^{-1}$.

**Method:**
1. Break the journey into stages: warm the ice ($-18$ to $0$), melt the ice at $0^\circ\text{C}$, warm the water ($0$ to $20$).
2. Energy to warm the ice: $E_1 = mc_{\text{ice}}\Delta\theta = 0.20 \times 2100 \times 18 = 7560\,\text{J}$.
3. Energy to melt the ice: $E_2 = mL_{\text{fusion}} = 0.20 \times 3.30 \times 10^5 = 66\,000\,\text{J}$.
4. Energy to warm the melted water: $E_3 = mc_{\text{water}}\Delta\theta = 0.20 \times 4180 \times 20 = 16\,720\,\text{J}$.
5. Add every stage.

**Answer:**

$$E = E_1 + E_2 + E_3 = 7560 + 66\,000 + 16\,720 = 90\,280\,\text{J} \approx 9.0 \times 10^4\,\text{J}$$

About $9.0 \times 10^4\,\text{J}$. Note that melting alone (the $mL$ term) dominates.

**What the examiner wants:** all three energy terms written out separately (a mark each), consistent units, and the total quoted to 2 s.f. The same method is used in Example 7 (s18/42).

### Example 3: The first law of thermodynamics with given $q$ and $W$ (coursebook Question 3)

**Question:** (a) A gas is heated by supplying $250\,\text{kJ}$ of energy; at the same time it is compressed so that $500\,\text{kJ}$ of work is done on the gas. Calculate the change in internal energy. (b) The same gas is heated as before with $250\,\text{kJ}$, but this time it is allowed to expand so that it does $200\,\text{kJ}$ of work on its surroundings. Calculate the change in internal energy.

**Method:**
1. Decide the signs from the direction words. Heating the gas means $q = +250\,\text{kJ}$ in both parts.
2. (a) Compression means work done **on** the gas: $W = +500\,\text{kJ}$.
3. (b) The gas does work **on its surroundings**: $W = -200\,\text{kJ}$.
4. Substitute into $\Delta U = q + W$.

**Answer:**

(a) $$\Delta U = q + W = 250 + 500 = 750\,\text{kJ}$$ - the internal energy increases by $750\,\text{kJ}$.

(b) $$\Delta U = q + W = 250 + (-200) = +50\,\text{kJ}$$ - the internal energy increases by $50\,\text{kJ}$.

**What the examiner wants:** the sign of $W$ is the whole question. "Compressed" = work on the gas = positive; "expands, does work on surroundings" = negative. State the answer with units and the direction of the change.

### Example 4: Kettle question - estimating $c$ and $L$ from a rated power (w02/04 Q1)

**Question:** A kettle is rated at $2.3\,\text{kW}$. A mass of $750\,\text{g}$ of water at $20^\circ\text{C}$ is poured in. When switched on, it takes $2.0$ minutes for the water to start boiling. In a further $7.0$ minutes, one half of the mass of water is boiled away. Estimate the specific heat capacity of water and the specific latent heat of vaporisation.

**Method:**
1. Convert: $m = 0.75\,\text{kg}$, $P = 2300\,\text{W}$, $t_1 = 120\,\text{s}$, $t_2 = 420\,\text{s}$.
2. Specific heat capacity: energy supplied to reach boiling is $E = Pt_1 = 2300 \times 120 = 276\,000\,\text{J}$, with $\Delta\theta = 100 - 20 = 80\,\text{K}$. Then $c = \frac{Pt_1}{m\Delta\theta}$.
3. Specific latent heat: energy supplied while boiling is $E = Pt_2 = 2300 \times 420 = 966\,000\,\text{J}$, and the mass boiled away is $m = 0.75/2 = 0.375\,\text{kg}$. Then $L = \frac{Pt_2}{m}$.
4. State the assumption (all the kettle's energy goes into the water) and its effect on the estimates.

**Answer:**

$$c = \frac{276\,000}{0.75 \times 80} = 4600\,\text{J kg}^{-1}\text{K}^{-1}$$

$$L = \frac{966\,000}{0.375} = 2.6 \times 10^6\,\text{J kg}^{-1}$$

$c \approx 4600\,\text{J kg}^{-1}\text{K}^{-1}$ (higher than the true $4180$ because of the losses), $L \approx 2.6 \times 10^6\,\text{J kg}^{-1}$.

**What the examiner wants:** the two energy balances ($Pt = mc\Delta\theta$ and $Pt = mL$), the unit conversions (grams to kg, minutes to seconds), and the assumption about no heat loss. Because some energy is in fact lost to the kettle and the surroundings, the energy actually absorbed by the water is less than $Pt$, so the calculated values are **overestimates**. (This is a genuine 2002 Paper 4 question; the mark scheme was not in the research pack, so treat the numbers as a worked estimate.)

### Example 5: Latent heat of fusion with a heater-off correction (w08/04 Q2, 7 marks)

**Question:** (a) Define specific latent heat of fusion. (b) Crushed ice at $0^\circ\text{C}$ is placed in a funnel with an electric heater, and the melted water is collected in a beaker. With the heater off, $16.6\,\text{g}$ of water is collected in $10.0$ minutes. With the heater on, $64.7\,\text{g}$ is collected in $5.0$ minutes, and the energy supplied to the heater is $18\,000\,\text{J}$. (i) State why the mass of water is determined with the heater switched off. (ii) Suggest how it can be determined that the ice is melting at a constant rate. (iii) Calculate a value for the specific latent heat of fusion of ice.

**Method:**
1. Definition: the (thermal) energy required to convert unit mass of solid to liquid at its normal melting point / without any change in temperature.
2. (i) The heater-off run makes allowance for heat gains from the atmosphere (ice melting due to the surroundings).
3. (ii) Constant rate of production of droplets from the funnel, or a constant mass of water collected per minute in the beaker.
4. (iii) Find the mass melted by the heater alone: with the heater off, ambient heat melts $16.6\,\text{g}$ in $10$ minutes, so in $5$ minutes it melts $16.6/2 = 8.3\,\text{g}$. Mass melted by the heater: $m = 64.7 - 8.3 = 56.4\,\text{g} = 56.4 \times 10^{-3}\,\text{kg}$.
5. Use $mL = 18\,000$.

**Answer:**

$$L = \frac{18\,000}{56.4 \times 10^{-3}} = 3.2 \times 10^5\,\text{J kg}^{-1} = 320\,\text{kJ kg}^{-1}$$

$L = 320\,\text{kJ kg}^{-1}$ (close to the accepted $330\,\text{kJ kg}^{-1}$).

**What the examiner wants:** in the definition, "unit mass" **and** the constant-temperature condition - merely saying "per 1 kg of ice to water" scores at most 1 mark. The heater-off correction is the point of the calculation: using the raw $64.7\,\text{g}$ (forgetting the correction) gives $278\,\text{kJ kg}^{-1}$ and loses most of the marks (using $m = 48.1\,\text{g}$ scores at most 2).

### Example 6: Latent heat of vaporisation by the two-power method (w19/41 Q3, 10 marks)

**Question:** (a) State what is meant by specific latent heat. (b) A student finds the specific latent heat of vaporisation of a liquid by boiling it with an electric heater on a balance. From $0$ to $10$ minutes the heater runs at $I = 1.2\,\text{A}$, $V = 230\,\text{V}$ and $56\,\text{g}$ of liquid evaporates. From $12$ to $22$ minutes the heater runs at $I = 1.0\,\text{A}$, $V = 190\,\text{V}$ and $32\,\text{g}$ evaporates. The rate of loss of thermal energy to the surroundings is the same in both runs. (i) Determine the mass evaporated from $12.0$ to $22.0$ minutes. (ii) Explain why, although the power of the heater is changed, the rate of loss of thermal energy to the surroundings may be assumed to be constant. (iii) Determine a value for the specific latent heat of vaporisation $L$. (iv) Calculate the rate at which thermal energy is transferred to the surroundings.

**Method:**
1. Definition: (thermal) energy per (unit) mass (to change state); heat transfer during a change of state at constant temperature.
2. (i) Read the mass off the balance-time graph: $32\,\text{g}$.
3. (ii) The temperature difference between the liquid and the surroundings does not change, because the liquid stays at its boiling point throughout.
4. (iii) Write the energy balance for each run. In $10$ minutes ($600\,\text{s}$), energy supplied = energy to vaporise the liquid + heat lost to surroundings ($H$): $230 \times 1.2 \times 600 = 56L + H$ and $190 \times 1.0 \times 600 = 32L + H$. Subtract the equations to eliminate $H$: $(276 - 190) \times 600 = (56 - 32)L$.
5. (iv) Substitute the unrounded value of $L$ back into the first equation to find $H$, then divide by $600\,\text{s}$.

**Answer:**

$$86 \times 600 = 24L \qquad \Rightarrow \qquad L = \frac{51\,600}{24} = 2150\,\text{J g}^{-1} \approx 2.2 \times 10^3\,\text{J g}^{-1}$$

$$H = 165\,600 - (56 \times 2150) = 45\,200\,\text{J} \qquad \Rightarrow \qquad \text{rate} = \frac{45\,200}{600} = 75\,\text{W}$$

$L = 2.2 \times 10^3\,\text{J g}^{-1}$ (mark scheme value $2200\,\text{J g}^{-1}$) and the rate of loss of thermal energy to the surroundings is $75\,\text{W}$. Both match the official mark scheme.

**What the examiner wants:** the definition with both points (per unit mass + constant temperature); the explanation that the temperature difference to the surroundings is unchanged because the liquid stays at its boiling point; the two energy equations written with the heat loss term $H$ included; and the subtraction that eliminates $H$.

### Example 7: Calorimetry - ice in warm water (s18/42 Q3, 7 marks)

**Question:** An aluminium can of mass $160\,\text{g}$ contains $330\,\text{g}$ of warm water at $38^\circ\text{C}$. A mass of $48\,\text{g}$ of ice at $-18^\circ\text{C}$ from a freezer is added. The ice melts and the final temperature of the can and its contents is $23^\circ\text{C}$. Data: $c_{\text{aluminium}} = 0.910\,\text{J g}^{-1}\text{K}^{-1}$, $c_{\text{ice}} = 2.10\,\text{J g}^{-1}\text{K}^{-1}$, $c_{\text{water}} = 4.18\,\text{J g}^{-1}\text{K}^{-1}$. (i) Show that the loss in thermal energy of the can and the warm water is $2.3 \times 10^4\,\text{J}$. (ii) Calculate a value $L$ for the specific latent heat of fusion of ice.

**Method:**
1. (i) Both the can and the warm water cool from $38^\circ\text{C}$ to $23^\circ\text{C}$, a fall of $15\,\text{K}$. Energy lost $= mc\Delta\theta$ for each, and add.
2. (ii) Energy balance: energy lost by can and water = energy gained by the ice. The ice gains energy in three parts: warming from $-18^\circ\text{C}$ to $0^\circ\text{C}$, melting at $0^\circ\text{C}$, and warming the melted water from $0^\circ\text{C}$ to $23^\circ\text{C}$.
3. Write the full equation and solve for $L$.

**Answer:**

(i) $$\text{loss} = (160 \times 0.910 \times 15) + (330 \times 4.18 \times 15) = 2184 + 20\,691 = 22\,875\,\text{J} \approx 2.3 \times 10^4\,\text{J}$$

(ii) $$2.3 \times 10^4 = (48 \times 2.10 \times 18) + 48L + (48 \times 4.18 \times 23)$$

$$2.3 \times 10^4 = 1814 + 48L + 4615$$

$$48L = 1.66 \times 10^4$$

$$L = \frac{1.66 \times 10^4}{48} = 350\,\text{J g}^{-1}$$

$L = 350\,\text{J g}^{-1}$ (i.e. $350\,\text{kJ kg}^{-1}$), consistent with the accepted value of $330\,\text{kJ kg}^{-1}$.

**What the examiner wants:** for the "show that" part, full working of both $mc\Delta\theta$ terms (you cannot just write the final number - the answer is given); for $L$, all three energy terms for the ice written separately: warming the ice, melting it, and warming the melted water.

### Example 8: Melting explained by kinetic theory (s18/42 Q3(a), 3 marks)

**Question:** During melting, a solid becomes liquid with little or no change in volume. Use kinetic theory to explain why, during the melting process, thermal energy is required although there is no change in temperature.

**Method:** state the three mark-scheme points in order: what happens to the bonds, what happens to the energy, and why the energy must be thermal.

**Answer:**
- (during melting,) bonds between atoms/molecules are broken
- potential energy of atoms/molecules is increased
- no/little work done so the required input of energy is thermal

**What the examiner wants:** exactly those three ideas. The temperature does not change because the energy goes into potential energy (breaking bonds), not into kinetic energy - the kinetic energy (and so the temperature) of the molecules stays constant.

### Example 9: First law and internal energy of an ideal gas (w08/04 Q4, 4 marks)

**Question:** (a) State the first law of thermodynamics. (b) A fixed mass of an ideal gas is kept at a constant temperature. Explain why its internal energy does not change.

**Method:**
1. (a) Quote the equation or a correct word version: the increase in internal energy of a system equals the energy transferred to the system by heating plus the work done on the system.
2. (b) Split internal energy into its kinetic and potential parts and deal with each: kinetic energy depends on temperature; potential energy depends on intermolecular forces.

**Answer:**
(a) $\Delta U = q + w$ (a correct word equation also accepted).

(b) Kinetic energy is constant because the temperature is constant; potential energy is constant because there are no intermolecular forces (in an ideal gas); so there is no change in internal energy.

**What the examiner wants:** in the definition, the words "on", "to" and "increase" carry the marks (the 2009 examiner report: incomplete answers like "$+w$ is the work done", "$+q$ is the heat supplied" and "$+\Delta U$ is the change in internal energy" were common and lost marks). For part (b), both reasons are required - constant temperature (KE) and no intermolecular forces (PE).

### Other recurring question types (mark schemes not in the pack)

Two more recurring types, described generically because the mark schemes were not in the research pack:

- **Kettle/heater questions** (e.g. November 2002 Paper 4 Q1): use the rated power and times to estimate $c$ and $L$, then state an assumption (no heat loss) and whether the estimate is an over- or underestimation. Fully worked in Example 4.
- **First-law narrative questions** (e.g. the coursebook end-of-chapter question on carbon dioxide): explain cooling using $\Delta U = q + W$ - when a gas expands rapidly, it does work on its surroundings ($W < 0$), little heat is supplied ($q \approx 0$), so its internal energy (and hence temperature) falls enough for the solid to form.

---

---

# Chapter 22: Ideal Gases
> Source: `physics/notes/chapter-22-ideal-gases-notes.md`

## 4. Methods (Question Types & Methods)

These are the ways Cambridge actually asks about ideal gases in Paper 4 (verified against real papers and examiner reports). Each method below is the mark-scheme-shaped route to full marks.

### 4.1 Define an ideal gas (2 marks)

Method: write "$pV \propto T$ (at all temperatures and pressures) for a fixed amount of gas" and name the symbols ($V$ = volume, $T$ = thermodynamic temperature). Alternative acceptable versions: "obeys $pV = nRT$ at all pressures and temperatures (with $n$ and $R$ constant)" or, from the kinetic model, "no intermolecular forces; negligible volume of molecules". Examiner report (June 2022): if you say "follows $pV = nRT$", you must state $n$ and $R$ are constant, and define the symbols.

### 4.2 State the assumptions of the kinetic theory (2 - 5 marks)

Method: write down as many of the five assumptions in Section 1.7 as requested, phrased about **molecules**, e.g. "molecules are in constant random motion", "volume of molecules negligible compared with volume of container", "no forces between molecules except during collisions", "collisions are perfectly elastic", "collision time negligible". Never write "the gas is elastic" - the theory is about the particles of the gas.

### 4.3 Explain how molecular motion produces pressure (2 - 3 marks)

Method: molecules collide with (container) walls; collisions are elastic so a molecule's momentum changes (reverses) at the wall; force = rate of change of momentum (Newton's laws); the wall experiences many collisions per second; pressure = force per unit area. For a change question ("what happens when temperature rises / more gas is pumped in"): faster molecules hit harder and more often (temperature), or more molecules hit per second (amount), so pressure increases.

### 4.4 Derive $pV = \frac{1}{3}Nm\langle c^2 \rangle$ (4 - 6 marks)

Method: follow the numbered steps in Section 1.9. When the question gives a molecule of mass $m$ and speed $u$ in a cube of side $L$ and asks for expressions in terms of $m$, $u$ and $L$ only:
- change in momentum $= 2mu$
- time between collisions with the same face $= \dfrac{2L}{u}$
- force $= \dfrac{2mu}{2L/u} = \dfrac{mu^2}{L}$
- pressure on one face $= \dfrac{mu^2/L}{L^2} = \dfrac{mu^2}{L^3}$

Then extend: average over $N$ molecules (replace $u^2$ with $\langle c^2 \rangle$), and divide by 3 for three dimensions ($\langle c_x^2 \rangle = \frac{1}{3}\langle c^2 \rangle$), giving $pV = \frac{1}{3}Nm\langle c^2 \rangle$. Examiner report (Nov 2021): the two most common errors are omitting the factor of 2 (in $2mu$ and $2L/u$) and inventing letters that were not defined in the question.

### 4.5 Show that the mean kinetic energy is $\frac{3}{2}kT$ (2 marks)

Method: start from $pV = NkT$ (easier, says the examiner report) and $pV = \frac{1}{3}Nm\langle c^2 \rangle$. Equate: $\frac{1}{3}Nm\langle c^2 \rangle = NkT$, cancel $N$, rearrange to $\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}kT$, and state that $\frac{1}{2}m\langle c^2 \rangle = E_K$ is the mean translational kinetic energy. If you start from $pV = nRT$ instead, you must state $N = nN_A$ and $R = kN_A$ at some point.

### 4.6 Use $pV = nRT$ to find one variable (2 - 3 marks)

Method (e.g. find $n$): convert $T$ to kelvin; convert $V$ to $\text{m}^3$ (1 $\text{dm}^3 = 10^{-3}\ \text{m}^3$, 1 litre $= 10^{-3}\ \text{m}^3$, $1\ \text{cm}^3 = 10^{-6}\ \text{m}^3$); rearrange $n = \frac{pV}{RT}$; substitute with $R = 8.31$; answer with units. Then convert moles to mass or molecules if asked: $m = nM_r$ (g) or $N = nN_A$. Show the rearranged equation - you get method marks even if the arithmetic slips.

### 4.7 Find the number of molecules using $pV = NkT$ (2 - 3 marks, often "show that")

Method: rearrange $N = \frac{pV}{kT}$ with $k = 1.38 \times 10^{-23}$, or do $n = \frac{pV}{RT}$ then $N = nN_A$ (both routes are credited). For a "show that $N = 6.6 \times 10^{23}$" style question, write the substitution line in full with all numbers - the final line alone is rarely enough for all three marks. Examiner report (May/June 2021): candidates who quoted the formula with $T$ as the subject scored more readily.

### 4.8 Calculate the r.m.s. speed (2 - 4 marks)

Three routes, pick the one the question feeds you:
- From temperature and molecular mass: $c_{\text{r.m.s.}} = \sqrt{\frac{3kT}{m}}$ where $m$ is the mass of one molecule (find it from $m = \frac{M}{N_A}$ if you are given molar mass). Remember: convert molar mass from $\text{g mol}^{-1}$ to $\text{kg mol}^{-1}$.
- From temperature and molar mass: $c_{\text{r.m.s.}} = \sqrt{\frac{3RT}{M}}$ with $M$ in $\text{kg mol}^{-1}$.
- From pressure and density: $\langle c^2 \rangle = \frac{3p}{\rho}$, then square root.

Method marks: convert $T$ to kelvin (this is the single most common mark-loser), calculate $\langle c^2 \rangle$ first, then take the square root. Finishing with $\langle c^2 \rangle$ and never square-rooting loses the final mark (examiner report, Nov 2021).

### 4.9 Calculate the mean kinetic energy of a molecule (2 - 3 marks)

Method: $\langle E_K \rangle = \frac{3}{2}kT$ with $T$ in kelvin. Answer is a tiny number, typically $10^{-21}$ J at room temperature ($6.21 \times 10^{-21}$ J at 300 K). Comparisons: at the same temperature all molecules have the same mean translational KE; a heavier molecule has a smaller r.m.s. speed.

### 4.10 Internal energy change of an ideal gas (2 - 3 marks)

Method: an ideal gas has no intermolecular forces, so all internal energy is kinetic: $U = \frac{3}{2}NkT$. A temperature change $\Delta T$ (in kelvin, and a Celsius change is numerically the same) gives $\Delta U = \frac{3}{2}Nk\Delta T = \frac{3}{2}nR\Delta T$. At constant temperature, $\Delta U = 0$ regardless of what happens to pressure or volume (examiner report, June 2022: many candidates wrongly gave $\Delta U \neq 0$ for a constant-temperature expansion).

### 4.11 Two-state problems: $\frac{p_1V_1}{T_1} = \frac{p_2V_2}{T_2}$ (2 - 3 marks)

Method: identify which quantities stay constant. Constant temperature: $p_1V_1 = p_2V_2$ (Boyle). Constant pressure: $\frac{V_1}{T_1} = \frac{V_2}{T_2}$ (Charles). Everything changing (fixed mass): $\frac{p_1V_1}{T_1} = \frac{p_2V_2}{T_2}$. Units of $p$ and $V$ only need to match on both sides, but $T$ must be in kelvin. This is how bubbles rising, tyres heating up, and balloons expanding are examined.

### 4.12 Explain why a real gas deviates from ideal behaviour (2 - 3 marks)

Method: name the condition (high pressure and/or low temperature) and the two failed assumptions. At high pressure: molecules occupy a significant fraction of the volume (their own volume is no longer negligible) and intermolecular forces become significant. At low temperature: molecules move slowly, forces pull them together, and the gas may condense - the gas laws break down. The ideal gas model is best at low pressure, high temperature.

### 4.13 Explain Brownian motion (2 - 3 marks)

Method: visible particles are bombarded unevenly by invisible molecules of the fluid; the unequal bombardment from all sides makes the particle move randomly (jerky, erratic path); this provides evidence that molecules exist, are in constant random motion, and are much smaller and faster than the visible particle. On heating: molecules move faster, bombardment more vigorous, so the motion of the visible particle becomes more agitated.

### 4.14 Estimate the volume occupied by molecules (2 marks)

Method: volume of one (spherical) molecule $= \frac{4}{3}\pi r^3$; multiply by the number of molecules $N$. Then compare with the container volume to test the "negligible volume" assumption (FM19 Q2: $4 \times 10^{-8}\ \text{m}^3 \ll 6.8 \times 10^{-3}\ \text{m}^3$, so the assumption holds).

---

## 5. Solved Examples

Mark-scheme-style solutions: equation, substitution, answer with units. Examples 1 - 7 are practice questions; Examples 8 - 13 are real Paper 4 questions in chronological order, with mark allocations and answers from the published mark schemes.

### Example 1: Mass of gas in a tyre - pV = nRT then n to mass (practice question, 4 marks)

**Question:** A car tyre contains $0.020\ \text{m}^3$ of air at $3.0 \times 10^5$ Pa and 27 °C. The molar mass of air is $28.8\ \text{g mol}^{-1}$. Calculate the mass of air in the tyre.

**Method:**
1. Convert temperature to kelvin: $T = 27 + 273 = 300\ \text{K}$.
2. Find the number of moles from $pV = nRT$: $n = \frac{pV}{RT}$.
3. Convert moles to mass: $\text{mass} = n \times M_r$.

**Answer:**

$$n = \frac{pV}{RT} = \frac{3.0 \times 10^5 \times 0.020}{8.31 \times 300} = 2.41\ \text{mol}$$

$$\text{mass} = n \times M_r = 2.41 \times 28.8 = 69.4 \approx 69\ \text{g}$$

**What the examiner wants:** $T$ in kelvin (not °C), the rearranged equation $n = \frac{pV}{RT}$ written out (method marks even if the arithmetic slips), and the final answer with units (g).

### Example 2: Boyle's law compression (practice question, 3 marks)

**Question:** A cylinder contains $0.80\ \text{dm}^3$ of nitrogen at 1.2 atm. It is compressed slowly (constant temperature) to 6.0 atm. Calculate the final volume.

**Method:** $T$ constant and fixed mass, so use Boyle's law $p_1V_1 = p_2V_2$. Units of $p$ and $V$ only need to match on each side, so keep atm and $\text{dm}^3$. Rearrange for $V_2$.

**Answer:**

$$V_2 = \frac{p_1V_1}{p_2} = \frac{1.2 \times 0.80}{6.0} = 0.16\ \text{dm}^3$$

The pressure rose by a factor of 5, so the volume fell by a factor of 5.

**What the examiner wants:** recognising that constant temperature means $pV = \text{constant}$ (Boyle's law), and that $p$ and $V$ units only need to be consistent on each side - no conversion to Pa or $\text{m}^3$ needed.

### Example 3: Number of molecules - "show that" style (practice question, 3 marks)

**Question:** A gas occupies $3.1 \times 10^{-3}\ \text{m}^3$ at $8.5 \times 10^5$ Pa and 290 K. Show that the number of molecules is $6.6 \times 10^{23}$.

**Method:** Use $pV = NkT$ rearranged to $N = \frac{pV}{kT}$, and write the substitution line in full with every number. Alternative route: $n = \frac{pV}{RT}$ then $N = nN_A$.

**Answer:**

$$N = \frac{pV}{kT} = \frac{8.5 \times 10^5 \times 3.1 \times 10^{-3}}{1.38 \times 10^{-23} \times 290} = 6.6 \times 10^{23}$$

(Alternative: $n = \frac{pV}{RT} = 1.10$ mol, then $N = nN_A = 1.10 \times 6.02 \times 10^{23} = 6.6 \times 10^{23}$.)

**What the examiner wants:** the full substitution line - writing only the final answer loses marks. Both the $pV = NkT$ route and the $n$ then $N = nN_A$ route are credited.

### Example 4: Mean kinetic energy of a molecule (practice question, 2 - 3 marks)

**Question:** Calculate the mean translational kinetic energy of a molecule of an ideal gas at 27 °C.

**Method:** Convert to kelvin, then apply $\langle E_K \rangle = \frac{3}{2}kT$.

**Answer:**

$$T = 27 + 273 = 300\ \text{K}$$

$$\langle E_K \rangle = \frac{3}{2}kT = \frac{3}{2} \times 1.38 \times 10^{-23} \times 300 = 6.21 \times 10^{-21}\ \text{J}$$

Note the answer is per molecule: a gas with $N$ molecules has total energy $\frac{3}{2}NkT$.

**What the examiner wants:** the kelvin conversion (leaving 27 in the formula scores nothing) and an answer of the right magnitude (about $10^{-21}$ J at room temperature).

### Example 5: r.m.s. speed from temperature - nitrogen (practice question, 3 marks)

**Question:** Nitrogen molecules have mass $4.65 \times 10^{-26}$ kg. Calculate the r.m.s. speed of nitrogen molecules at 300 K.

**Method:** Use $\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}kT$ to get $\langle c^2 \rangle = \frac{3kT}{m}$, then take the square root: $c_{\text{r.m.s.}} = \sqrt{\langle c^2 \rangle}$.

**Answer:**

$$\langle c^2 \rangle = \frac{3kT}{m} = \frac{3 \times 1.38 \times 10^{-23} \times 300}{4.65 \times 10^{-26}} = 2.67 \times 10^5\ \text{m}^2\text{s}^{-2}$$

$$c_{\text{r.m.s.}} = \sqrt{2.67 \times 10^5} = 517\ \text{m s}^{-1}$$

(Shortcut with molar mass: $M = 0.028\ \text{kg mol}^{-1}$, $c_{\text{r.m.s.}} = \sqrt{\frac{3RT}{M}} = \sqrt{\frac{3 \times 8.31 \times 300}{0.028}} = 517\ \text{m s}^{-1}$. Both routes are credited.)

**What the examiner wants:** calculate $\langle c^2 \rangle$ first and then finish with the square root - stopping at $\langle c^2 \rangle$ loses the final mark (Nov 2021 examiner report).

### Example 6: r.m.s. speed from pressure and density (practice question, 3 marks)

**Question:** The density of air at room temperature is $1.29\ \text{kg m}^{-3}$ at a pressure of $1.0 \times 10^5$ Pa. Calculate the r.m.s. speed of air molecules.

**Method:** Use the density form $p = \frac{1}{3}\rho\langle c^2 \rangle$, rearrange to $\langle c^2 \rangle = \frac{3p}{\rho}$, then square root.

**Answer:**

$$\langle c^2 \rangle = \frac{3p}{\rho} = \frac{3 \times 1.0 \times 10^5}{1.29} = 2.33 \times 10^5\ \text{m}^2\text{s}^{-2}$$

$$c_{\text{r.m.s.}} = \sqrt{2.33 \times 10^5} = 4.8 \times 10^2\ \text{m s}^{-1}$$

This is a little above the speed of sound in air (about $330\ \text{m s}^{-1}$), which makes sense.

**What the examiner wants:** picking the density form of the kinetic theory equation and remembering to take the square root at the end.

### Example 7: Internal energy change of a gas (practice question, 3 marks)

**Question:** An ideal gas containing $6.6 \times 10^{23}$ molecules cools from 290 K to 190 K at constant volume. Calculate the change in its internal energy.

**Method:** Use $\Delta U = \frac{3}{2}Nk\Delta T$ with $\Delta T = 190 - 290 = -100\ \text{K}$.

**Answer:**

$$\Delta U = \frac{3}{2} \times 6.6 \times 10^{23} \times 1.38 \times 10^{-23} \times (190 - 290) = -1.4 \times 10^3\ \text{J} = -1400\ \text{J}$$

Negative because the gas lost internal energy (it cooled).

**What the examiner wants:** the negative sign (the gas cooled, so internal energy fell), and recognising that the temperature difference is the same number in kelvin and °C.

### Example 8: Estimating the mean distance between molecules (9702/42/O/N/16 Q2, 8 marks)

**Question:** A gas at 100 °C occupies $2.4 \times 10^3\ \text{cm}^3$ at a pressure of $4.9 \times 10^5$ Pa. (a) Show that the number of molecules of gas is $2.3 \times 10^{23}$. (b) Estimate the mean distance between the molecules.

**Method:**
1. Convert: $T = 100 + 273 = 373\ \text{K}$; $V = 2.4 \times 10^3\ \text{cm}^3 = 2.4 \times 10^3 \times 10^{-6} = 2.4 \times 10^{-3}\ \text{m}^3$.
2. (a) $N = \frac{pV}{kT}$ with the full substitution line.
3. (b) Volume per molecule $= \frac{V}{N}$. Assume each molecule sits at the centre of its own little cube; the mean distance between molecules is the side of that cube, i.e. the cube root of the volume per molecule.

**Answer:**

$$N = \frac{pV}{kT} = \frac{4.9 \times 10^5 \times 2.4 \times 10^{-3}}{1.38 \times 10^{-23} \times 373} = 2.3 \times 10^{23}$$

$$\text{volume per molecule} = \frac{V}{N} = \frac{2.4 \times 10^{-3}}{2.3 \times 10^{23}} = 1.04 \times 10^{-26}\ \text{m}^3$$

$$\text{mean distance} = (1.04 \times 10^{-26})^{1/3} = 2.2 \times 10^{-9}\ \text{m} = 2.2 \times 10^{-7}\ \text{cm}$$

**What the examiner wants:** the mean distance is estimated as the cube root of the volume per molecule (volume per molecule $= \frac{V}{N}$); convert $\text{cm}^3$ to $\text{m}^3$ before substituting; give the answer in the unit requested (cm).

### Example 9: Density form and molecule volume (9702/42/F/M/19 Q2, 10 marks)

**Question:** The pressure $p$ of an ideal gas having density $\rho$ is given by the expression $p = \frac{1}{3}\rho\langle c^2 \rangle$.

(a) State what is meant by:
(i) an ideal gas **[2]**
(ii) the term $\langle c^2 \rangle$. **[1]**

(b) A cylinder contains a fixed mass of a gas at a temperature of 120 °C. The gas has a volume of $6.8 \times 10^{-3}\ \text{m}^3$ at a pressure of $2.4 \times 10^5$ Pa.
(i) Assuming the gas acts as an ideal gas, show that the number of atoms of gas in the cylinder is $3.0 \times 10^{23}$. **[3]**
(ii) Each atom of the gas, assumed to be a sphere, has a radius of $3.2 \times 10^{-11}$ m. Use the answer in (i) to estimate the actual volume occupied by the gas atoms. **[2]**
(iii) One of the assumptions of the kinetic theory of gases is related to the volume of the atoms. State this assumption. Explain whether your answer in (ii) is consistent with this assumption. **[2]**

**Method:**
1. (a)(i) Write "the gas obeys $pV/T = \text{constant}$ (or $pV = nRT$)" and define the symbols $V$ and $T$.
2. (a)(ii) $\langle c^2 \rangle$ is the mean-square speed of the atoms/molecules.
3. (b)(i) $T = 120 + 273 = 393\ \text{K}$; use $pV = nRT$ then $N = nN_A$ (or directly $pV = NkT$), showing the substitution in full.
4. (b)(ii) Volume of one atom $= \frac{4}{3}\pi r^3$; multiply by the number of atoms $N$.
5. (b)(iii) State the assumption, then compare the occupied volume with the container volume.

**Answer:**

$$N = \frac{pV}{kT} = \frac{2.4 \times 10^5 \times 6.8 \times 10^{-3}}{1.38 \times 10^{-23} \times 393} = 3.0 \times 10^{23}$$

$$\text{volume of one atom} = \frac{4}{3}\pi r^3 = \frac{4}{3}\pi(3.2 \times 10^{-11})^3 = 1.37 \times 10^{-31}\ \text{m}^3$$

$$\text{total occupied volume} = 3.0 \times 10^{23} \times \frac{4}{3}\pi(3.2 \times 10^{-11})^3 = 4 \times 10^{-8}\ \text{m}^3$$

Assumption: the volume of the atoms is negligible compared with the volume of the container. $4 \times 10^{-8}\ \text{m}^3 \ll 6.8 \times 10^{-3}\ \text{m}^3$, so yes, the result is consistent with the assumption.

**What the examiner wants:** two separate marks for the ideal gas definition - the law ($pV/T = \text{constant}$ or $pV = nRT$) plus the symbols defined; the full substitution line for the "show that"; for the volume, $\frac{4}{3}\pi r^3$ per atom times $N$; and a comparison of magnitudes for the assumption check.

### Example 10: Explaining $p = \frac{1}{3}\rho\langle c^2 \rangle$ and the mass of one molecule (9702/42/M/J/20 Q2, 8 marks)

**Question:** (a) The pressure of an ideal gas is given by $pV = \frac{1}{3}Nm\langle c^2 \rangle$. Explain how each of the terms $\rho$, $\frac{1}{3}$ and $\langle c^2 \rangle$ arises in the equivalent expression $p = \frac{1}{3}\rho\langle c^2 \rangle$. (b) A sample of gas has mass 20.7 g. The number of molecules in the sample, found using $pV = NkT$, is $4.5 \times 10^{23}$. Calculate the mass of one molecule.

**Method:**
1. (a) $\rho = \frac{Nm}{V}$: the density of the gas, i.e. the total mass of all the molecules divided by the volume they occupy.
2. $\frac{1}{3}$: the molecules move randomly in three dimensions, so on average only one third of the molecular motion is along any one axis - only the component of velocity perpendicular to a wall contributes to the pressure on that wall.
3. $\langle c^2 \rangle$: the molecules have different speeds, so we use the mean of the squares of all their speeds (the mean-square speed).
4. (b) Mass of one molecule $= \frac{\text{total mass}}{N}$.

**Answer:**

$$\text{mass of one molecule} = \frac{20.7\ \text{g}}{4.5 \times 10^{23}} = 4.6 \times 10^{-23}\ \text{g}$$

**What the examiner wants:** each term explained separately - $\rho$ is the density ($Nm/V$); $\frac{1}{3}$ comes from random motion in three dimensions (only one third of the motion in any one direction); $\langle c^2 \rangle$ is the average of the squares of the speeds because the speeds differ. The molecule mass is simply the sample mass divided by $N$.

### Example 11: The full kinetic theory package (9702/42/O/N/21 Q3, 11 marks)

**Question (numbers and wording as printed):**

(a)(i) One assumption of the kinetic theory is that all collisions involving molecules of the gas are elastic. State what is meant by an elastic collision. **[1]**

(a)(ii) State two other assumptions of the kinetic theory of gases. **[2]**

(b) A molecule of mass $m$ is in a cubic box of side $L$, moving with velocity $u$ towards one face, colliding elastically with that face and the opposite face alternately. Deduce expressions, in terms of $m$, $u$ and $L$, for:
(i) the magnitude of the change in momentum of the molecule on colliding with a face **[1]**
(ii) the time between consecutive collisions of the molecule with the same face **[1]**
(iii) the average force exerted by the molecule on that face **[1]**
(iv) the pressure on the face if that force acts over the whole area of the face. **[1]**

(c) When the model is extended to three dimensions and $N$ molecules with mean-square speed $\langle c^2 \rangle$, it can be shown that $pV = \frac{1}{3}Nm\langle c^2 \rangle$. Use this expression with the equation of state to show that the average translational kinetic energy of a molecule is $E_K = \frac{3}{2}kT$. **[2]**

(d) The mass of a hydrogen molecule is $3.34 \times 10^{-27}$ kg. Use the expression for $E_K$ to determine the r.m.s. speed of a hydrogen molecule at 25 °C. **[2]**

**Method:**
1. (a)(i) An elastic collision is one with no loss of kinetic energy.
2. (a)(ii) Any two of: molecules have negligible volume (compared with the gas/container); no forces between molecules (except during collisions); molecules are in random motion; collisions are instantaneous.
3. (b)(i) Velocity reverses from $+u$ to $-u$: change in momentum $= 2mu$.
4. (b)(ii) Distance travelled between hits on the same face is $2L$ at speed $u$: time $= \frac{2L}{u}$.
5. (b)(iii) Force = rate of change of momentum: $F = \frac{2mu}{2L/u} = \frac{mu^2}{L}$.
6. (b)(iv) Pressure = force/area: $p = \frac{mu^2/L}{L^2} = \frac{mu^2}{L^3}$.
7. (c) Start from $pV = NkT$; equate with $pV = \frac{1}{3}Nm\langle c^2 \rangle$; cancel $N$; rearrange to $\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}kT$ and identify $\frac{1}{2}m\langle c^2 \rangle$ as $E_K$.
8. (d) Substitute with $T = 25 + 273 = 298\ \text{K}$; find $\langle c^2 \rangle$; take the square root for the r.m.s. speed.

**Answer:**

- (a)(i) no loss of kinetic energy
- (a)(ii) any two of: negligible molecular volume; no forces except during collisions; random motion; instantaneous collisions
- (b)(i) $2mu$
- (b)(ii) $\frac{2L}{u}$
- (b)(iii) $F = \frac{2mu}{2L/u} = \frac{mu^2}{L}$
- (b)(iv) $p = \frac{mu^2/L}{L^2} = \frac{mu^2}{L^3}$
- (c) $NkT = \frac{1}{3}Nm\langle c^2 \rangle$ leading to $\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}kT$ and $\frac{1}{2}m\langle c^2 \rangle = E_K$
- (d) $\frac{1}{2} \times 3.34 \times 10^{-27} \times \langle c^2 \rangle = \frac{3}{2} \times 1.38 \times 10^{-23} \times 298$; r.m.s. speed $= 1.9 \times 10^3\ \text{m s}^{-1}$

**What the examiner wants (Nov 2021, Paper 42 report):** (a)(i) "kinetic energy is conserved" - momentum conservation or "energy is conserved" in general did not score. (a)(ii) the theory deals with the particles that make up the gas, not the gas itself. (b) the factors of 2 in (i) and (ii), and only the letters the question defines ($m$, $u$, $L$) - inventing symbols loses credit. (c) starting from $pV = NkT$ is easier; if you start from $pV = nRT$ you must state $N = nN_A$ and $R = kN_A$. (d) many calculated $\langle c^2 \rangle$ but did not square-root it; some left $T$ in °C and got no credit.

### Example 12: Equation of state plus internal energy (9702/42/M/J/21 Q2, 9 marks)

**Question (numbers as printed):**

An ideal gas has volume $3.1 \times 10^{-3}\ \text{m}^3$ at pressure $8.5 \times 10^5$ Pa and temperature 290 K. It suddenly expands to $6.3 \times 10^{-3}\ \text{m}^3$; no thermal energy is transferred; final pressure $2.7 \times 10^5$ Pa at temperature $T_F$.

(a) Show that the number of gas molecules is $6.6 \times 10^{23}$. **[3]**

(b)(i) Show that the final temperature $T_F$ of the gas is 190 K. **[1]**

(b)(ii) The average translational kinetic energy of a molecule is $E_K = \frac{3}{2}kT$. Calculate the increase in internal energy $\Delta U$ of the gas. **[3]**

(c) Use the first law of thermodynamics to explain why the external work done on the gas during the expansion equals the increase in internal energy in (b)(ii). **[2]**

**Method:**
1. (a) $N = \frac{pV}{kT}$ (or $n = \frac{pV}{RT}$ then $N = nN_A$), substitution line in full.
2. (b)(i) Fixed mass, all three quantities change: $\frac{p_1V_1}{T_1} = \frac{p_2V_2}{T_2}$, rearrange for $T_2$.
3. (b)(ii) $\Delta U = \frac{3}{2}Nk\Delta T$ with $\Delta T = T_F - 290$.
4. (c) First law $\Delta U = q + W$; no thermal energy transferred means $q = 0$, so $\Delta U = W$.

**Answer:**

- (a) $N = \frac{3.1 \times 10^{-3} \times 8.5 \times 10^5}{1.38 \times 10^{-23} \times 290} = 6.6 \times 10^{23}$
- (b)(i) $\frac{3.1 \times 10^{-3} \times 8.5 \times 10^5}{290} = \frac{6.3 \times 10^{-3} \times 2.7 \times 10^5}{T}$; so $T = 190\ \text{K}$
- (b)(ii) $\Delta U = \frac{3}{2} \times 1.38 \times 10^{-23} \times (190 - 290) \times 6.6 \times 10^{23} = -1400\ \text{J}$ (a decrease, since the gas cooled)
- (c) $\Delta U = q + W$; $q = 0$ (no thermal energy transferred) so $\Delta U = W$

**What the examiner wants (May/June 2021 report):** the "show that" parts require the substitution line written out; candidates who quoted the formula with $T$ (or $N$) as the subject scored the method marks more readily.

### Example 13: Potential energy zero and the internal energy-volume graph (9702/41/M/J/24 Q3, 12 marks)

**Question (verified points):** This 12-mark question on an ideal gas asked candidates to explain why the potential energy of the molecules of an ideal gas is zero, to show that the internal energy $U$ of a fixed mass of ideal gas at constant pressure is related to its volume by $U = \frac{3}{2}pV$, and to sketch a graph of internal energy $U$ against volume $V$ at constant pressure.

**Method:**
1. Potential energy: an ideal gas has no intermolecular forces. With no forces between molecules, no work is done in changing their separation, so the molecules have zero potential energy - all the internal energy is kinetic.
2. $U = \frac{3}{2}NkT$ (all kinetic, since the potential energy is zero). From the equation of state $pV = NkT$, substitute: $U = \frac{3}{2}NkT = \frac{3}{2}pV$.
3. Graph: at constant pressure, $U = \frac{3}{2}pV$ means $U \propto V$ - a straight line through the origin with positive gradient $\frac{3}{2}p$.

**Answer:** (a) the potential energy of the molecules is zero because there are no intermolecular forces; (b) $U = \frac{3}{2}NkT = \frac{3}{2}pV$; (c) the $U$ against $V$ graph is a straight line through the origin with positive gradient.

**What the examiner wants:** the key statement "no intermolecular forces, so potential energy is zero" - this is what makes all the internal energy kinetic; for the graph, a straight line through the origin with positive gradient, because at constant pressure $U = \frac{3}{2}pV$ means $U$ is proportional to $V$.

### Question patterns to expect (from examiner reports and exam-practice sources)

- **June 2022, Paper 41, Q3** (verified via the examiner report): an ideal gas question asked candidates to state what is meant by an ideal gas, calculate the amount of gas from $pV = nRT$, and complete a first-law energy table including a constant-temperature change. The report notes: stating "obeys $pV = nRT$" is only equivalent to "$pV \propto T$" when $n$ and $R$ are stated to be constant; candidates must define all symbols; all steps must be clear in "show that" questions; and for a change at constant temperature the increase in internal energy is zero.
- **May/June 2024, Paper 41** (verified Question 3 solved in Example 13): the 12-mark ideal gas question tested the zero potential energy of ideal gas molecules and the $U$ against $V$ graph at constant pressure. Related exam-practice styles from this session include the mean translational kinetic energy per molecule at a given temperature (5-mark style question) and the r.m.s. speed of $\text{N}_2$ molecules given the molar mass (6-mark style question).
- **Generic recurring types** (safe to expect): "state what is meant by an ideal gas" [2]; "state two assumptions" [2]; "explain, in terms of molecules, why the pressure increases when (i) temperature rises, (ii) more gas is added" [2-3]; "calculate the number of molecules in a container" [2-3]; "calculate the r.m.s. speed" [2-4]; "compare the mean kinetic energies / speeds of two different gases at the same temperature" [2]; "explain why a real gas deviates from ideal behaviour at high pressure / low temperature" [2-3].

---

---

# Chapter 23: Coulomb's Law
> Source: `physics/notes/chapter-23-coulombs-law-notes.md`

## 4. Methods (Question Types & Methods)

These are the ways Cambridge has actually asked about electric fields. Each method below is what a full-mark answer looks like.

### 1. Find the force between two charges (Coulomb's law)

**Method:**
1. Identify $Q_1$, $Q_2$ and the centre-to-centre distance $r$ in metres. Convert all units first (cm to m, $\mu\text{C}$ to C: $1 \mu\text{C} = 10^{-6} \text{ C}$, nC: $1 \text{ nC} = 10^{-9} \text{ C}$).
2. Substitute into $F = \frac{Q_1 Q_2}{4\pi\epsilon_0 r^2}$, using $\frac{1}{4\pi\epsilon_0} = 8.99 \times 10^9$.
3. Give the magnitude with units, then state the direction: like charges repel, unlike charges attract.

**Traps:** forgetting to square $r$; using surface-to-surface distance instead of centre-to-centre for spheres; mixing up $10^{-6}$ and $10^{-9}$.

### 2. Find the force on a charge in a field ($F = qE$)

**Method:**
1. Find $E$ (either given, from $E = \frac{V}{d}$ for plates, or from $E = \frac{Q}{4\pi\epsilon_0 r^2}$ for a point charge).
2. Multiply by the charge: $F = qE$.
3. Direction: positive charges are pushed along the field (towards negative plates/charges), negative charges opposite to the field.

### 3. Find the electric field strength at a point due to a point charge or sphere

**Method:**
1. Use $E = \frac{Q}{4\pi\epsilon_0 r^2}$ with $r$ measured from the centre of the charge/sphere.
2. Watch the units: field strengths are often quoted in $\text{V cm}^{-1}$ or $\text{kV m}^{-1}$; convert to $\text{V m}^{-1}$.
3. State the direction (radially away from a positive charge, towards a negative charge).

### 4. Resultant field of two or more charges (vector addition)

**Method:**
1. Work out the field each charge produces at the point (magnitude and direction) separately.
2. Add them as vectors along the line joining the charges: same direction adds, opposite direction subtracts.
3. The point where the resultant field is zero lies between two like charges, closer to the smaller charge: at that point $E_1 = E_2$, so $\frac{Q_1}{r_1^2} = \frac{Q_2}{r_2^2}$. Use this to find a charge ratio or an unknown charge.
4. Never use $Q = 4\pi\epsilon_0 r^2 E$ with the resultant field near one charge: the resultant field is not produced by a single charge.

### 5. Uniform field between parallel plates

**Method:**
1. $E = \frac{V}{d}$ (V in volts, d in metres).
2. Force on a charge: $F = qE = \frac{qV}{d}$.
3. Acceleration: $a = \frac{F}{m} = \frac{qE}{m}$.
4. Work/energy to move a charge between the plates: $W = qV$.
5. Projectile-style motion: constant speed parallel to the plates, constant acceleration towards the opposite plate; the path is a parabola. Use $s = ut + \frac{1}{2}at^2$ in the field direction.

### 6. Find the electric potential at a point

**Method:**
1. For each charge, compute $V = \frac{Q}{4\pi\epsilon_0 r}$ using the distance from that charge to the point.
2. Add the potentials as scalars, keeping the signs (positive for positive charges, negative for negative charges).
3. Give the answer in volts.

### 7. Potential energy of charge pairs / work done moving charges

**Method:**
1. For two charges: $E_P = \frac{Qq}{4\pi\epsilon_0 r}$ (sign follows the charges).
2. Work done moving a charge between two points: $W = q(V_B - V_A)$.
3. In a uniform field: $W = qV$ or $W = qEd$ (moving distance $d$ along the field direction). Moving perpendicular to the field does no work (potential does not change).

### 8. Field strength from a potential gradient (graph question)

**Method:**
1. If the graph is a straight line (uniform field): $E = \frac{\Delta V}{\Delta d}$, the constant gradient.
2. If the graph is curved (radial field): draw the tangent at the point of interest, find its gradient $\frac{\Delta V}{\Delta r}$, then $E = -\text{gradient}$.
3. Convert units carefully ($\text{kV cm}^{-1}$ to $\text{V m}^{-1}$: multiply by $10^5$).
4. The magnitude is $E$; the sign tells you the direction (field points from high to low potential).

### 9. Compare gravitational and electric forces (or fields)

**Method:**
1. Write both force laws: $F_g = \frac{GMm}{r^2}$ and $F_e = \frac{Q_1 Q_2}{4\pi\epsilon_0 r^2}$.
2. Substitute both sets of values, and quote the ratio $F_e / F_g$ (often astronomically large for subatomic particles).
3. State the conclusion (e.g. gravity is negligible compared with the electric force between protons), and any implication (e.g. the strong nuclear force must hold the nucleus together).
4. For written comparisons, use the table in Section 1.10: both are inverse square laws, both have scalar potentials zero at infinity, but electric forces can repel and potentials can be negative.

### 10. Definitions (frequent 2-mark questions)

- **Electric field strength:** force per unit positive charge (1 mark for "force per unit charge", 1 for "positive charge").
- **Electric potential:** work done per unit positive charge in bringing a small test charge from infinity to the point. Make sure it has the dimensions of energy per charge ($\text{J C}^{-1}$), not energy. "From infinity" also secures the sign convention.

### 11. Alpha particle / closest approach (energy conversion)

**Method:**
1. As the particle approaches a like charge, it slows down: kinetic energy is converted into electric potential energy.
2. At closest approach its speed is zero, so $E_K = E_P$: $$\frac{1}{2}mv^2 = \frac{Qq}{4\pi\epsilon_0 r}$$
3. Solve for $r$ (distance of closest approach), or for the initial kinetic energy needed.
4. Relate to nuclear physics: the closest approach sets an upper limit on the nuclear radius, since the particle never actually touches the nucleus.

### 12. Drawing field lines and equipotentials

**Method:**
1. Field lines start on positive charges, end on negative charges; arrows must show direction.
2. Lines must be radial for a point charge, parallel and equally spaced for parallel plates, and perpendicular to conducting surfaces.
3. Equipotential lines are perpendicular to field lines; equally spaced in a uniform field, closer together near a point charge.
4. In the region between like charges, lines curve away (repulsion); between unlike charges they run between the charges (attraction).

## 5. Solved Examples

All questions below are genuinely verified - worked examples plus real past paper questions - with how the marks were allocated and what full-mark answers look like. This chapter's questions appear on Paper 4, the structured A Level paper, and as Paper 1 multiple choice items.

### Example 1: Force between two charged spheres (practice question)

**Question:** Two metal spheres each have radius 20 cm. Sphere A carries charge $+2.0 \mu\text{C}$ and sphere B carries charge $-1.0 \mu\text{C}$. Their surfaces are separated by a gap of 10 cm. Calculate the electric force each sphere exerts on the other.

**Method:**
1. Find the centre-to-centre distance: $r = 20 + 10 + 20 = 50 \text{ cm} = 0.50 \text{ m}$. For spheres, always use centre-to-centre, not surface-to-surface.
2. Substitute into Coulomb's law using $\frac{1}{4\pi\epsilon_0} = 8.99 \times 10^9$:

$$F = \frac{Q_1 Q_2}{4\pi\epsilon_0 r^2} = \frac{(2.0 \times 10^{-6})(1.0 \times 10^{-6})}{4\pi(8.85 \times 10^{-12})(0.50)^2}$$

$$F = 8.99 \times 10^9 \times \frac{2.0 \times 10^{-12}}{0.25} = 7.2 \times 10^{-2} \text{ N}$$

3. State the direction from the signs of the charges.

**Answer:** $F = 7.2 \times 10^{-2} \text{ N}$, attractive: each sphere pulls the other towards it with a force of $7.2 \times 10^{-2} \text{ N}$.

**What the examiner wants:** the centre-to-centre distance for spheres ($20 + 10 + 20$ cm), conversion to metres, substitution into the inverse square law, and the direction stated in words (unlike charges attract).

### Example 2: Field strength and charge of a charged sphere (practice question)

**Question:** A metal sphere of diameter 12 cm is positively charged. The electric field strength at its surface is $4.0 \times 10^5 \text{ V m}^{-1}$. Determine the total surface charge.

**Method:**
1. Radius: $r = \frac{0.12}{2} = 0.06 \text{ m}$ (use the radius, not the diameter).
2. Rearrange $E = \frac{Q}{4\pi\epsilon_0 r^2}$ to make $Q$ the subject:

$$Q = 4\pi\epsilon_0 r^2 E = \frac{r^2 E}{8.99 \times 10^9} = \frac{(0.06)^2 \times 4.0 \times 10^5}{8.99 \times 10^9}$$

$$Q = \frac{1.44 \times 10^3}{8.99 \times 10^9} = 1.6 \times 10^{-7} \text{ C} = 0.16 \mu\text{C}$$

**Answer:** $Q = 1.6 \times 10^{-7} \text{ C} = 0.16 \mu\text{C}$.

**What the examiner wants:** rearranging the inverse square formula correctly and using the radius rather than the diameter.

### Example 3: Uniform field, force and acceleration (practice question)

**Question:** Two parallel plates are 4 cm apart and have a potential difference of 2.5 kV. (a) Calculate the field strength between the plates. (b) A dust particle carrying charge $+2.4 \text{ nC}$ moves between the plates. Calculate the force on it and its acceleration (mass $4.2 \mu\text{g}$).

**Method:**
(a) Convert first: $d = 0.04 \text{ m}$, $V = 2.5 \times 10^3 \text{ V}$, then $E = \frac{V}{d}$:

$$E = \frac{V}{d} = \frac{2.5 \times 10^3}{0.04} = 6.25 \times 10^4 \text{ V m}^{-1}$$

(b) Force: $F = qE$:

$$F = qE = 2.4 \times 10^{-9} \times 6.25 \times 10^4 = 1.5 \times 10^{-4} \text{ N}$$

Acceleration (mass $= 4.2 \times 10^{-6} \text{ kg}$): $a = \frac{F}{m}$:

$$a = \frac{F}{m} = \frac{1.5 \times 10^{-4}}{4.2 \times 10^{-6}} = 36 \text{ m s}^{-2}$$

**Answer:** $E = 6.25 \times 10^4 \text{ V m}^{-1}$; $F = 1.5 \times 10^{-4} \text{ N}$; $a = 36 \text{ m s}^{-2}$. The positive dust particle accelerates towards the negative plate.

**What the examiner wants:** every unit converted before substituting (cm to m, kV to V, nC to C, µg to kg) - these power-of-ten conversions are where marks are routinely lost.

### Example 4: Potential of a charged dome (practice question)

**Question:** A Van de Graaff generator has a spherical dome of radius 10 cm charged to a potential of 100 kV. Calculate the charge stored on the dome and the potential at a distance of 10 cm from its surface.

**Method:**
1. At the surface, $r = 0.10 \text{ m}$, $V = 1.0 \times 10^5 \text{ V}$. Rearrange $V = \frac{Q}{4\pi\epsilon_0 r}$:

$$Q = 4\pi\epsilon_0 r V = \frac{rV}{8.99 \times 10^9} = \frac{0.10 \times 1.0 \times 10^5}{8.99 \times 10^9} = 1.1 \times 10^{-6} \text{ C}$$

2. At 10 cm from the surface, $r = 0.20 \text{ m}$ (always measured from the centre):

$$V = \frac{Q}{4\pi\epsilon_0 r} = \frac{1.1 \times 10^{-6}}{4\pi(8.85 \times 10^{-12})(0.20)} = 5.0 \times 10^4 \text{ V} = 50 \text{ kV}$$

**Answer:** $Q = 1.1 \times 10^{-6} \text{ C}$; $V = 5.0 \times 10^4 \text{ V} = 50 \text{ kV}$. (Halving distance doubles potential: potential obeys an inverse law with $r$, not inverse square.)

**What the examiner wants:** measuring $r$ from the centre of the sphere (10 cm from the surface means $r = 20$ cm), and remembering potential follows an inverse law, not an inverse square law.

### Example 5: Electric force versus gravitational force between protons (practice question)

**Question:** Two protons in a nucleus are separated by $10^{-15} \text{ m}$. Calculate the electric force of repulsion and the gravitational force of attraction between them, and comment.

**Method:**
1. Electric force ($Q_1 = Q_2 = 1.60 \times 10^{-19} \text{ C}$):

$$F_e = \frac{Q_1 Q_2}{4\pi\epsilon_0 r^2} = \frac{8.99 \times 10^9 \times (1.60 \times 10^{-19})^2}{(10^{-15})^2} = 2.3 \times 10^2 \text{ N}$$

2. Gravitational force ($m = 1.67 \times 10^{-27} \text{ kg}$):

$$F_g = \frac{Gm^2}{r^2} = \frac{6.67 \times 10^{-11} \times (1.67 \times 10^{-27})^2}{(10^{-15})^2} = 1.9 \times 10^{-34} \text{ N}$$

3. Take the ratio and comment on what it means.

**Answer:** $F_e = 2.3 \times 10^2 \text{ N}$; $F_g = 1.9 \times 10^{-34} \text{ N}$; $\frac{F_e}{F_g} \approx 1.2 \times 10^{36}$. The gravitational force is utterly negligible. The protons repel each other with a force of hundreds of newtons, so gravity cannot balance the repulsion: another force (the strong nuclear force) must hold the nucleus together.

**What the examiner wants:** both force laws written and substituted, the ratio $F_e / F_g$ quoted, and a conclusion with an implication (gravity negligible; the strong nuclear force is needed).

### Example 6: Field strength from a potential gradient graph (practice question)

**Question:** A graph shows how electric potential $V$ varies with distance $r$ from a charged object. At $r = 5.0 \text{ cm}$ the tangent to the graph has gradient $\frac{(10.0 - 2.0) \text{ kV}}{(0.6 - 8.2) \text{ cm}}$. Calculate the electric field strength at that point.

**Method:**
1. Gradient of tangent:

$$\frac{\Delta V}{\Delta r} = \frac{8.0 \text{ kV}}{-7.6 \text{ cm}} = -1.05 \text{ kV cm}^{-1} = -1.05 \times 10^5 \text{ V m}^{-1}$$

2. Field strength is the negative of the potential gradient:

$$E = -\frac{\Delta V}{\Delta r} = +1.05 \times 10^5 \approx 1.1 \times 10^5 \text{ V m}^{-1}$$

**Answer:** $E = 1.1 \times 10^5 \text{ V m}^{-1}$ (equivalently $1.1 \times 10^5 \text{ N C}^{-1}$). Since the potential falls with distance from this positive charge, the field points away from the charge.

**What the examiner wants:** $E = -\frac{dV}{dr}$ using the tangent gradient, and the unit conversion $\text{kV cm}^{-1} \rightarrow \text{V m}^{-1}$ (multiply by $10^5$).

### Example 7: Alpha particle approaching a gold nucleus (coursebook exam-style question, 12 marks)

**Question:** An alpha particle (charge $+2e$, mass $6.65 \times 10^{-27} \text{ kg}$) with kinetic energy $8.0 \times 10^{-13} \text{ J}$ approaches a gold nucleus (charge $+79e$) head-on. Determine the p.d. the alpha would need to be accelerated through to gain that energy, its speed, its speed at closest approach, its kinetic and potential energy at closest approach, and the distance of closest approach. State what this implies about the gold nucleus.

**Method:**
1. p.d. to accelerate the alpha to this energy ($q = 2e$):

$$V = \frac{E_K}{q} = \frac{8.0 \times 10^{-13}}{2 \times 1.60 \times 10^{-19}} = 2.5 \times 10^6 \text{ V}$$

2. Speed from kinetic energy: $v = \sqrt{\frac{2E_K}{m}} = \sqrt{\frac{2 \times 8.0 \times 10^{-13}}{6.65 \times 10^{-27}}} = 1.6 \times 10^7 \text{ m s}^{-1}$.
3. As the particle approaches the like-charged nucleus it slows down: kinetic energy is converted into electric potential energy. At closest approach its speed is zero, so $E_K = E_P$:

$$\frac{1}{2}mv^2 = \frac{Qq}{4\pi\epsilon_0 r}$$

4. Solve for $r$ with $Q = 79e = 1.264 \times 10^{-17} \text{ C}$ and $q = 2e = 3.2 \times 10^{-19} \text{ C}$:

$$r = \frac{Qq}{4\pi\epsilon_0 E_K} = \frac{8.99 \times 10^9 \times 1.264 \times 10^{-17} \times 3.2 \times 10^{-19}}{8.0 \times 10^{-13}}$$

$$r = 4.5 \times 10^{-14} \text{ m}$$

**Answer:** p.d. $= 2.5 \times 10^6 \text{ V}$; speed $= 1.6 \times 10^7 \text{ m s}^{-1}$; at closest approach the speed is zero, so the kinetic energy is zero and all $8.0 \times 10^{-13} \text{ J}$ is electric potential energy; distance of closest approach $r = 4.5 \times 10^{-14} \text{ m}$.

**What the examiner wants:** the energy conversion $E_K = E_P$ at closest approach, and the implication: the alpha particle never actually touched the nucleus, so the nuclear radius must be smaller than $4.5 \times 10^{-14} \text{ m}$ - the closest approach gives an upper limit for the nuclear radius. This question combines Coulomb's law, potential energy, and kinetic energy conversion in one question.

### Example 8: State what is meant by electric field strength (MJ19 P41 Q5(a), 2 marks)

**Question:** State what is meant by electric field strength. [2]

**Method:** Give the two ideas the mark scheme wants: force per unit charge, and that the force is on a positive charge.

**Answer:** "force per unit positive charge" - the force per unit charge acting on a positive charge placed at the point.

**What the examiner wants:** the mark scheme awards exactly two ideas: "force per unit charge" (1) plus "(force on a) positive charge" (1). "Per unit charge" must be explicit, and candidates routinely lost the "positive charge" idea (June 2019 examiner report).

### Example 9: Do the charges have the same or opposite signs? (MJ19 P41 Q5(b)(i), 2 marks)

**Question:** Two point charges A and B are situated 15 cm apart in a vacuum. Point P lies on the line joining the charges, distance $x$ from A. A graph of electric field strength $E$ at P against $x$ shows $E$ changing sign (crossing zero at $x = 10 \text{ cm}$) between the charges. By reference to the direction of the electric field, state and explain whether A and B have the same or opposite signs. [2]

**Method:** $E$ is a vector: the sign on the graph is a direction convention. A zero point between the charges can only happen when the two fields cancel there, which requires the charges to have the same sign.

**Answer:** the charges have the same sign. The field changes direction between A and B (it is zero at a point between them), so the fields from the two charges cancel.

**What the examiner wants:** 1 mark for the field changing direction / being zero at a point between them, 1 mark for same sign. The common error (examiner report): candidates said "opposite signs because the line goes from positive to negative", missing that $E$ is a vector and a zero point between the charges means cancellation, which requires like charges.

### Example 10: Why is the field not inverse square between the charges? (MJ19 P41 Q5(b)(ii), 1 mark)

**Question:** State why, although A is a point charge, the field between $x = 3 \text{ cm}$ and $x = 7 \text{ cm}$ does not obey an inverse square law. [1]

**Method:** The graph shows the resultant field at P, not the field of A alone: charge B also contributes to it.

**Answer:** the field at P is also influenced by charge B / charge A is not isolated / the field is the resultant of the fields of both charges.

**What the examiner wants:** any one of those three phrasings earns the mark.

### Example 11: Ratio of the charges (MJ19 P41 Q5(b)(iii), 3 marks)

**Question:** Use the graph to determine the ratio magnitude of charge A / magnitude of charge B. [3]

**Method:**
1. Write $E = \frac{Q}{4\pi\epsilon_0 x^2}$ (1 mark).
2. At the zero point $x = 10 \text{ cm}$, the fields cancel, so $E_A = E_B$ (1 mark).
3. Hence $\frac{Q_A}{10^2} = \frac{Q_B}{5^2}$: B is 15 cm from A, so at the zero point it is 5 cm from B (1 mark).

**Answer:** $Q_A / Q_B = 4.0$.

**What the examiner wants:** the full 3-mark method above. Candidates found this challenging; many tried $Q = 4\pi\epsilon_0 r^2 E$ using points near each charge, which fails because the graph value is the resultant of both fields, not the field of one charge.

### Example 12: Definition of electric potential (June 2019 Paper 4, 2 marks)

**Question:** Define electric potential at a point. [2]

**Method:** The definition must be dimensionally correct - energy per charge ($\text{J C}^{-1}$), not energy. Include "work done", "per unit positive charge" and "from infinity" (from infinity fixes the sign convention).

**Answer:** the work done per unit positive charge in bringing a small test charge from infinity to the point.

**What the examiner wants:** many candidates wrote answers with the dimensions of energy (e.g. "energy of a charge") and lost credit. Credit was given for "work done in moving positive charge from infinity". The current syllabus wording to learn: work done per unit positive charge in bringing a small test charge from infinity to the point.

### Example 13: Charged oil drop held between plates (June 2019 series)

**Question:** A charged oil drop is in equilibrium between two charged parallel plates. Find the field strength between the plates, explain why the drop is in equilibrium, determine the charge on the drop, and describe what happens if the p.d. is reduced (including the graph of field strength against distance).

**Method:**
1. Field strength between plates: $E = \frac{V}{d}$.
2. Equilibrium: the resultant force on the drop is zero - the electric force upwards equals the weight downwards ($qE = mg$).
3. Charge on the drop: equate electric force and weight, $qE = mg$. The electric force must point upwards to balance the weight, so the drop carries a negative charge.
4. Reduced p.d.: $E$ falls, the electric force falls, the resultant force is now downwards and the drop accelerates down.
5. Graph of field strength against distance: the field between parallel plates is uniform, so $E$ is constant everywhere between the plates; when the p.d. is changed the field pattern changes accordingly.

**Answer:** $E = \frac{V}{d}$; the drop is negative, with $q = \frac{mg}{E}$; reducing the p.d. makes the drop accelerate downwards.

**What the examiner wants:** "equilibrium requires no resultant force", not "the force is zero" or "it is stationary"; $F = ma$ with no value for $a$ loses credit; most candidates got the sign wrong - they said positive because the drop moved towards the negative plate, but the electric force must oppose the weight, so the drop is actually negative; a reduced p.d. reduces the field strength and hence the electric force, NOT the charge on the drop.

### Example 14: Potential variation graphs (June 2019 series)

**Question:** Describe how the electric potential varies (a) between two parallel plates and (b) between two charged conducting spheres.

**Method:**
(a) Between parallel plates the field is uniform, so the potential gradient is constant: potential varies linearly from $V_0$ at one plate to 0 at the other.
(b) A conductor is an equipotential: potential is constant inside each sphere. At the surfaces of the two spheres the potentials have the same magnitude (opposite sign); between the spheres the potential varies.

**Answer:** linear between the plates (constant gradient); constant inside each sphere, varying between the spheres.

**What the examiner wants:** the gradient is constant between parallel plates (many candidates did not appreciate this); few candidates realised the potential is constant inside a sphere; many drew the variation of field strength instead of potential.

### Example 15: Acceleration of charged particles in a uniform field (June 2019)

**Question:** Calculate the acceleration of a charged particle in a uniform electric field (for example between parallel plates).

**Method:** $a = \frac{F}{m} = \frac{qE}{m}$, with $E = \frac{V}{d}$ if the field is between plates. In projectile-style questions, a charge entering the field has constant velocity parallel to the plates and constant acceleration perpendicular to them; use $s = ut + \frac{1}{2}at^2$ in the field direction.

**Answer:** $a = \frac{qE}{m} = \frac{qV}{md}$.

**What the examiner wants:** candidates found this difficult; the marks come from combining $F = qE$ with $a = \frac{F}{m}$ and converting units before substituting.

### Example 16: MCQ on uniform fields - energy-distance graph (Nov 2015 Paper 13 Q29, 1 mark)

**Question:** Two parallel plates are 2 mm apart in a vacuum; an electron moves between them. A graph shows the electron's potential energy against distance from one plate. Why is the graph a straight line, and what are the field strength and p.d.?

**Method:** The field is uniform, so the force on the electron is constant and $W = qEs$ rises linearly with distance: the graph is a straight line. From the graph, $E = \frac{W}{qs}$, giving $E = 1500 \text{ N C}^{-1}$; then $V = Ed = 3 \text{ V}$.

**Answer:** the energy-distance graph is a straight line because the field is uniform; $E = 1500 \text{ N C}^{-1}$ and $V = 3 \text{ V}$.

**What the examiner wants:** the trap option quoted $3000 \text{ N C}^{-1}$ - forgetting the factor of 2 from the 2 mm distance in $W = qEs$ versus $V = Ed$.

---

# Chapter 24: Capacitance
> Source: `physics/notes/chapter-24-capacitance-notes.md`

## 4. Methods (Question Types & Methods)

These are the ways Cambridge has actually asked about capacitance. Each method below is what a full-mark answer looks like.

### 1. Find the charge on a capacitor ($Q = VC$)

**Method:**
1. Convert the capacitance to farads ($\mu\text{F} \rightarrow \text{F}$: $\times 10^{-6}$; $\text{nF}$: $\times 10^{-9}$; $\text{pF}$: $\times 10^{-12}$).
2. Convert the p.d. to volts (kV to V: $\times 10^3$).
3. Substitute into $Q = VC$ and give the answer with units (C, or convert to mC/$\mu$C if asked).

**Traps:** forgetting to convert $\mu\text{F}$ to F is the single most common error in this chapter; answering in C when the question asks for $\mu\text{C}$ (or vice versa); forgetting that $Q$ means the charge on each plate, not the net charge (which is zero).

### 2. Find the energy stored (choose the right formula)

**Method:**
1. Identify which two quantities you are given.
2. Given $C$ and $V$: use $W = \frac{1}{2}CV^2$. Given $Q$ and $V$: use $W = \frac{1}{2}QV$. Given $Q$ and $C$: use $W = \frac{Q^2}{2C}$.
3. Convert all units to SI, substitute, and quote $W$ in joules.

**Traps:** forgetting the factor of $\frac{1}{2}$ (using $W = QV$ or $W = CV^2$, which are wrong for stored energy); mixing up $Q$ and $V$ in the formula; unit errors ($\mu\text{F}$ vs F, mC vs C). The $\frac{1}{2}$ appears because the p.d. builds up from zero while charging, so the average p.d. is $\frac{V}{2}$.

### 3. Capacitors in parallel

**Method:**
1. Add the capacitances: $C_{\text{total}} = C_1 + C_2 + \dots$.
2. Each capacitor has the full supply p.d. across it, so $Q_1 = C_1V$, $Q_2 = C_2V$, ...
3. Total charge: $Q = C_{\text{total}}V$ (or add the individual charges).

**Traps:** using the reciprocal formula by mistake (that is series); forgetting that every parallel capacitor sees the full p.d., not a share of it; the total capacitance in parallel is always LARGER than the largest individual one.

### 4. Capacitors in series (the reciprocal trap)

**Method:**
1. Write the reciprocal formula: $\frac{1}{C_{\text{total}}} = \frac{1}{C_1} + \frac{1}{C_2} + \dots$.
2. Combine the fractions on the right.
3. Take the reciprocal at the end to get $C_{\text{total}}$.
4. Check your answer is smaller than the smallest individual capacitance.

**Traps:** forgetting to take the reciprocal at the end (leaving the answer as $\frac{1}{C}$); adding the capacitances directly; using the formula for resistors in series; not checking that the answer is less than every individual capacitance. Work in the same prefix throughout (e.g. keep everything in $\mu\text{F}$ - the units cancel in the reciprocal sum).

### 5. Capacitor networks (mixed series/parallel)

**Method:**
1. Redraw the circuit and look for the simplest group: a parallel pair (same p.d. across both) or a series pair (one current path through both).
2. Combine that pair first and replace it with its single equivalent capacitor.
3. Repeat until one equivalent capacitor remains.
4. Check: parallel combinations increase the capacitance, series combinations decrease it.

**Traps:** combining the wrong pair first; not recognising which capacitors share the same p.d.; arithmetic slips with reciprocals. Solve in stages and never try to do the whole network in one line.

### 6. Sharing charge between capacitors (charge conserved, energy NOT)

**Method:**
1. Initial charge on the charged capacitor: $Q = C_1V_0$.
2. Combined capacitance once connected (they are in parallel): $C_{\text{total}} = C_1 + C_2$.
3. Final common p.d.: $V = \frac{Q}{C_{\text{total}}}$.
4. Initial energy $W_1 = \frac{1}{2}C_1V_0^2$; final energy $W_2 = \frac{1}{2}C_{\text{total}}V^2$.
5. Energy dissipated = $W_1 - W_2$ (lost as heat in the connecting wires).

**Traps:** saying energy is conserved (it is not: for two equal capacitors half the energy is lost); using the original p.d. after sharing; forgetting that charge IS conserved; computing the final energy of only one capacitor instead of the total.

### 7. Charge from a current-time graph (area under the graph)

**Method:**
1. The charge that flows equals the area under the $I$-$t$ graph.
2. Count squares (multiplying by the value of one square), or split the area into triangles/trapezia and add them.
3. Convert the current axis to amperes before multiplying by time in seconds.

**Traps:** counting squares with the wrong scale; reading the current axis in mA and forgetting to convert; treating a curved (exponential) discharge graph as a triangle when the question wants a careful area estimate (state "estimate" and give a range).

### 8. Energy from a $V$-$Q$ graph (area of a triangle)

**Method:**
1. The graph of $V$ against $Q$ is a straight line through the origin ($V = \frac{Q}{C}$).
2. Energy stored = area under the graph = $\frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2}QV$.
3. The gradient of the line is $\frac{1}{C}$, so the capacitance is $C = \frac{Q}{V}$ at any point on the line.

**Traps:** forgetting the $\frac{1}{2}$; confusing this graph with the $I$-$t$ graph (whose area is charge, not energy); reading $V$ and $Q$ in non-SI units (mC, mV) without converting.

### 9. Capacitance of an isolated sphere

**Method:**
1. Find the radius in metres: the radius is HALF the diameter (40 cm diameter means $r = 0.20~\text{m}$).
2. Capacitance: $C = 4\pi\epsilon_0 r$, or $C = \frac{r}{8.99 \times 10^9}$ for a quick estimate.
3. Charge from surface potential: $Q = CV$, using $V = \frac{Q}{4\pi\epsilon_0 r}$ if needed.

**Traps:** using the diameter instead of the radius; measuring distances from the surface instead of the centre in potential questions; confusing $C = 4\pi\epsilon_0 r$ with the field formula $E = \frac{Q}{4\pi\epsilon_0 r^2}$.

### 10. Discharge circuit ($R = V/I$, why the current decays, $Q$ from the graph, $C = Q/V$)

**Method:**
1. Initial resistance from the initial current: at the moment the switch closes, the p.d. across the capacitor is the full supply p.d. $V_0$ and the current is $I_0$, so $R = \frac{V_0}{I_0}$.
2. The current decreases because charge leaves the plates, so the p.d. across the capacitor falls, and since $I = \frac{V}{R}$ the current falls too (exponentially).
3. Charge: $Q$ = area under the $I$-$t$ graph (counting squares or estimating).
4. Capacitance: $C = \frac{Q}{V_0}$.

**Traps:** saying the current decreases "because the capacitor is running out of energy" without linking it to the falling p.d. and $I = \frac{V}{R}$ (the examiner wants that link); not converting mA to A; using a later current instead of the initial current for $R$; giving exact values where the question asks for estimates.

### 11. Definitions (frequent 2-mark questions)

**Method:**
1. **Capacitance:** "the charge stored on one plate per unit potential difference between the plates" - include both ideas: charge stored (1 mark) and per unit p.d. (1 mark).

**Traps:** writing "the amount of charge a capacitor can hold" (that is capacity, not capacitance, and misses "per unit p.d."); omitting "one plate"; writing the equation alone without the words (the equation alone usually earns only 1 of the 2 marks).

## 5. Solved Examples

Real exam-style questions from the end of Chapter 24, with their mark allocations, plus the book's worked examples. The format for every example: Question / Method / Answer / What the examiner wants.

### Example 1: Charge on a capacitor ($Q = VC$) - End-of-chapter Q1, 1 mark

**Question:** A $470~\mu\text{F}$ capacitor is connected across the terminals of a battery of e.m.f. $9~\text{V}$. Calculate the charge on the plates of the capacitor. [1]

**Method:**
1. Convert: $C = 470~\mu\text{F} = 4.7 \times 10^{-4}~\text{F}$.
2. $Q = VC = 9 \times 4.7 \times 10^{-4} = 4.2 \times 10^{-3}~\text{C}$.

**Answer:** $Q = 4.2 \times 10^{-3}~\text{C} = 4.2~\text{mC}$.

**What the examiner wants:** 1 mark for the correct substitution into $Q = VC$ with the capacitance in farads. The mark is lost by writing $470$ instead of $4.7 \times 10^{-4}$.

### Example 2: p.d. from charge and capacitance - End-of-chapter Q2, 1 mark

**Question:** Calculate the p.d. across the terminals of a $2200~\mu\text{F}$ capacitor when it has a charge of $0.033~\text{C}$ on its plates. [1]

**Method:**
1. Rearrange $Q = VC$ to give $V = \frac{Q}{C}$.
2. $V = \frac{0.033}{2200 \times 10^{-6}} = 15~\text{V}$.

**Answer:** $V = 15~\text{V}$.

**What the examiner wants:** 1 mark for the rearrangement and substitution. Note the tidy numbers: $0.033/0.0022 = 15$. Unit conversion of the capacitance is the usual point of failure.

### Example 3: Capacitance from charge and p.d. - End-of-chapter Q3, 1 mark

**Question:** Calculate the capacitance of a capacitor if it stores a charge of $2.0~\text{C}$ when there is a potential difference of $5000~\text{V}$ across its plates. [1]

**Method:**
1. $C = \frac{Q}{V} = \frac{2.0}{5000} = 4.0 \times 10^{-4}~\text{F}$.

**Answer:** $C = 4.0 \times 10^{-4}~\text{F} = 400~\mu\text{F}$.

**What the examiner wants:** 1 mark for the correct rearrangement. Giving the answer in $\mu\text{F}$ as well as F shows unit awareness.

### Example 4: Energy stored (both formulas) - End-of-chapter Q4 and Q5, 1 mark each

**Question:** (a) Calculate the energy stored when a $470~\mu\text{F}$ capacitor has a potential difference of $12~\text{V}$ across its plates. [1] (b) Calculate the energy stored on a capacitor if it stores $1.5~\text{mC}$ of charge when there is a potential difference of $50~\text{V}$ across it. [1]

**Method:**
1. (a) $W = \frac{1}{2}CV^2 = \frac{1}{2} \times 470 \times 10^{-6} \times 12^2 = 3.4 \times 10^{-2}~\text{J}$.
2. (b) $W = \frac{1}{2}QV = \frac{1}{2} \times 1.5 \times 10^{-3} \times 50 = 3.75 \times 10^{-2}~\text{J}$.

**Answer:** (a) $W = 3.4 \times 10^{-2}~\text{J}$; (b) $W = 3.75 \times 10^{-2}~\text{J}$.

**What the examiner wants:** each mark for the correct formula choice and substitution. Part (a) is $C$ and $V$ so use $W = \frac{1}{2}CV^2$; part (b) is $Q$ and $V$ so use $W = \frac{1}{2}QV$. The most common error is forgetting the $\frac{1}{2}$, which doubles the answer.

### Example 5: Energy from a $V$-$Q$ graph (area under the graph) - End-of-chapter Q6-style, 3 marks

**Question:** The graph of $V$ against $Q$ for a particular capacitor is a straight line through the origin. When $Q = 4.0~\text{mC}$, $V = 4.0~\text{V}$. (a) Calculate the capacitance of the capacitor. [1] (b) Calculate the energy stored when the charge is $4.0~\text{mC}$, using the area under the graph. [2]

**Method:**
1. (a) The gradient of the line is $\frac{V}{Q} = \frac{1}{C}$, so $C = \frac{Q}{V} = \frac{4.0 \times 10^{-3}}{4.0} = 1.0 \times 10^{-3}~\text{F} = 1.0~\text{mF}$.
2. (b) The area under the line is a triangle: area $= \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times Q \times V$.
3. $W = \frac{1}{2} \times 4.0 \times 10^{-3} \times 4.0 = 8.0 \times 10^{-3}~\text{J}$.

**Answer:** (a) $C = 1.0 \times 10^{-3}~\text{F}$; (b) $W = 8.0 \times 10^{-3}~\text{J} = 8.0~\text{mJ}$.

**What the examiner wants:** the area idea (energy = area under the $V$-$Q$ graph, 1 mark), the triangle formula with the $\frac{1}{2}$ (1 mark), and the substitution with converted units (mC to C). The book's version divides the graph into strips to show $W$ growing as $V^2$: successive strips of $1.0~\text{mC}$ have areas $0.5$, $1.5$, $2.5$, $3.5~\text{mJ}$, so $W \propto V^2$.

### Example 6: Half the charge flows off - energy quartered - End-of-chapter Q6, 1 + 3 marks

**Question:** A $5000~\mu\text{F}$ capacitor has a p.d. of $24~\text{V}$ across its plates. (a) Calculate the energy stored on the capacitor. [1] (b) The capacitor is briefly connected across a bulb and half the charge flows off the capacitor. Calculate the energy dissipated in the bulb. [3]

**Method:**
1. (a) $W = \frac{1}{2}CV^2 = \frac{1}{2} \times 5000 \times 10^{-6} \times 24^2 = 1.44~\text{J}$. [1]
2. (b) After half the charge flows off, $Q$ is halved. Since $Q = CV$, the p.d. also halves to $12~\text{V}$.
3. Energy remaining: $W = \frac{1}{2}CV^2 = \frac{1}{2} \times 5000 \times 10^{-6} \times 12^2 = 0.36~\text{J}$. [1]
4. Energy dissipated: $1.44 - 0.36 = 1.08~\text{J}$. [1]
5. Alternative quick route: $W \propto Q^2$, so halving the charge quarters the energy: remaining $= \frac{1.44}{4} = 0.36~\text{J}$, dissipated $= 1.44 - 0.36 = 1.08~\text{J}$.

**Answer:** (a) $W = 1.44~\text{J}$; (b) energy dissipated $= 1.08~\text{J}$.

**What the examiner wants:** this is the classic "charge halved, energy quartered" question. The 3 marks: energy after discharge (1), energy dissipated (1), and either the $\frac{1}{2}CV^2$ calculation or the proportionality argument (1). The common error is halving the energy (using $W \propto Q$ instead of $W \propto Q^2$): half the charge means a QUARTER of the energy remains.

### Example 7: Discharge through a resistor (why only estimates) - End-of-chapter Q7, 5 marks

**Question:** A $4700~\mu\text{F}$ capacitor has a p.d. of $12~\text{V}$ across its terminals. It is connected to a resistor and the charge leaks away through the resistor in $2.5~\text{s}$. (a) Calculate the energy stored on the capacitor. [1] (b) Calculate the charge stored on the capacitor. [1] (c) Estimate the average current through the resistor. [1] (d) Estimate the resistance of the resistor. [1] (e) Suggest why the last two quantities can only be estimates. [1]

**Method:**
1. (a) $W = \frac{1}{2}CV^2 = \frac{1}{2} \times 4700 \times 10^{-6} \times 12^2 = 0.34~\text{J}$. [1]
2. (b) $Q = CV = 4700 \times 10^{-6} \times 12 = 0.056~\text{C}$. [1]
3. (c) Average current $= \frac{Q}{t} = \frac{0.056}{2.5} = 0.023~\text{A}$. [1]
4. (d) $R \approx \frac{V}{I} = \frac{12}{0.023} = 5.2 \times 10^2~\Omega$. [1]
5. (e) The current is not constant: it falls continuously as the p.d. across the capacitor falls, so "average current" is an approximation, and "leaks away in 2.5 s" is not a precisely defined time because an exponential discharge never quite finishes. [1]

**Answer:** (a) $0.34~\text{J}$; (b) $0.056~\text{C}$; (c) $23~\text{mA}$; (d) about $5.2 \times 10^2~\Omega$; (e) the current decays (it is not steady), so the average current and the discharge time are only approximations.

**What the examiner wants:** part (e) is the discriminator: the mark requires the idea that the current (and hence the p.d.) is changing during the discharge, so an average is an estimate. Candidates who write "the equipment is not accurate" do not get the mark.

### Example 8: Designing $4700~\mu\text{F}$ at $9.0~\text{V}$ from four $6~\text{V}$ capacitors - End-of-chapter Q8, 1 mark

**Question:** An engineer needs a capacitor of capacitance $4700~\mu\text{F}$ to be connected across a p.d. of $9.0~\text{V}$. She has four $4700~\mu\text{F}$, $6~\text{V}$ capacitors available. Draw a diagram to show how the four capacitors could be used for this purpose. [1]

**Method:**
1. Connect two capacitors in series: each series pair has capacitance $\frac{1}{C} = \frac{1}{4700} + \frac{1}{4700}$, so $C = 2350~\mu\text{F}$.
2. Connect the two series pairs in parallel with each other: $C_{\text{total}} = 2350 + 2350 = 4700~\mu\text{F}$.
3. Voltage check: the $9.0~\text{V}$ is shared equally by the two capacitors in each series pair, so each capacitor sees $4.5~\text{V}$, safely below its $6~\text{V}$ rating.

**Answer:** two series pairs (each $2350~\mu\text{F}$) connected in parallel across the $9.0~\text{V}$ supply, giving $4700~\mu\text{F}$ with $4.5~\text{V}$ across each individual capacitor.

**What the examiner wants:** 1 mark for the correct network: series connection halves the capacitance but doubles the voltage rating; parallel pairs restore the capacitance. The diagram must show two series pairs in parallel (the series capacitors must not be connected the wrong way round in the diagram).

### Example 9: All four networks from three $100~\mu\text{F}$ capacitors - End-of-chapter Q9, 4 marks

**Question:** Calculate the different capacitances that can be made from three $100~\mu\text{F}$ capacitors. For each value, draw the network that is used. [4]

**Method:**
1. All three in series: $\frac{1}{C} = \frac{1}{100} + \frac{1}{100} + \frac{1}{100} = \frac{3}{100}$, so $C = 33.3~\mu\text{F}$. [1]
2. All three in parallel: $C = 100 + 100 + 100 = 300~\mu\text{F}$. [1]
3. Two in parallel, in series with the third: pair $= 200~\mu\text{F}$; $\frac{1}{C} = \frac{1}{200} + \frac{1}{100} = \frac{3}{200}$, so $C = 66.7~\mu\text{F}$. [1]
4. Two in series, in parallel with the third: pair $= 50~\mu\text{F}$; $C = 50 + 100 = 150~\mu\text{F}$. [1]

**Answer:** $33.3~\mu\text{F}$ (all series), $300~\mu\text{F}$ (all parallel), $66.7~\mu\text{F}$ (pair parallel, then series), $150~\mu\text{F}$ (pair series, then parallel).

**What the examiner wants:** 1 mark per correct network, including the diagram. This is a pure test of the series and parallel formulas and the "solve in stages" skill: pair first, then combine with the third.

### Example 10: Three capacitors in series with a cell - charges on every plate - End-of-chapter Q10, 5 + 3 marks

**Question:** Three capacitors of capacitance $100~\text{mF}$, $200~\text{mF}$ and $600~\text{mF}$ are connected in series with a cell of e.m.f. $1.5~\text{V}$ (Figure 24.18). (a) Calculate the charges $Q_1$ to $Q_6$ on each of the six plates. [5] (b) Calculate the p.d. across each capacitor. [3]

**Method:**
1. Total capacitance: $\frac{1}{C} = \frac{1}{100} + \frac{1}{200} + \frac{1}{600} = \frac{6 + 3 + 1}{600} = \frac{10}{600}$, so $C = 60~\text{mF} = 0.060~\text{F}$. [1]
2. Charge stored: $Q = CV = 0.060 \times 1.5 = 0.090~\text{C}$. Capacitors in series all store this same charge. [1]
3. Plates carry equal and opposite charges: $Q_1 = -0.090~\text{C}$, $Q_2 = +0.090~\text{C}$, $Q_3 = -0.090~\text{C}$, $Q_4 = +0.090~\text{C}$, $Q_5 = -0.090~\text{C}$, $Q_6 = +0.090~\text{C}$. [3]
4. (b) $V_1 = \frac{Q}{C_1} = \frac{0.090}{0.100} = 0.90~\text{V}$; $V_2 = \frac{0.090}{0.200} = 0.45~\text{V}$; $V_3 = \frac{0.090}{0.600} = 0.15~\text{V}$. [3]
5. Check: $0.90 + 0.45 + 0.15 = 1.50~\text{V}$, the cell e.m.f.

**Answer:** (a) each plate carries $\pm 0.090~\text{C}$, alternating in sign along the chain; (b) p.d.s are $0.90~\text{V}$, $0.45~\text{V}$ and $0.15~\text{V}$ across the $100$, $200$ and $600~\text{mF}$ capacitors respectively.

**What the examiner wants:** the sign pattern is the point of part (a): adjacent plates carry equal and opposite charges, and the central isolated sections stay uncharged overall. The p.d.s divide in inverse proportion to the capacitances (the smallest capacitor takes the largest share of the voltage) and must add to the supply e.m.f.

### Example 11: Discharge circuit with an $I$-$t$ graph - End-of-chapter Q11, 8 marks

**Question:** A $9.0~\text{V}$ supply charges a capacitor, which then discharges through a resistor $R$. The current-time graph during discharge starts at $I = 15~\text{mA}$ at $t = 0$ and falls towards zero by about $t = 12~\text{s}$. (a)(i) Deduce the resistance $R$ of the resistor. [2] (a)(ii) Explain why the current decreases as the capacitor discharges. [2] (b)(i) The charge on the capacitor is equal to the area under the graph. Estimate the charge on the capacitor when the p.d. across it is $9.0~\text{V}$. [2] (b)(ii) Calculate the capacitance of the capacitor. [2]

**Method:**
1. (a)(i) At $t = 0$ the p.d. across the capacitor is the full $9.0~\text{V}$, so $R = \frac{V}{I_0} = \frac{9.0}{15 \times 10^{-3}} = 600~\Omega$. [2]
2. (a)(ii) As charge leaves the plates, the p.d. across the capacitor falls; since $I = \frac{V}{R}$ and $R$ is constant, the current falls too. [2]
3. (b)(i) Area under the graph (counting squares or trapezium rule): each small square is worth $1~\text{mA} \times 1~\text{s} = 1~\text{mC}$, and the total area is about $70$ squares, so $Q \approx 0.07~\text{C}$ (accept $0.06$ to $0.08~\text{C}$). [2]
4. (b)(ii) $C = \frac{Q}{V} = \frac{0.07}{9.0} = 7.8 \times 10^{-3}~\text{F} \approx 8~\text{mF}$ (accept $6$ to $9~\text{mF}$). [2]

**Answer:** (a)(i) $R = 600~\Omega$; (a)(ii) the p.d. across the capacitor falls as it discharges, so $I = \frac{V}{R}$ falls; (b)(i) $Q \approx 0.07~\text{C}$; (b)(ii) $C \approx 8 \times 10^{-3}~\text{F}$.

**What the examiner wants:** for (a)(ii) the mark scheme wants the link "p.d. falls, so $I = \frac{V}{R}$ falls" - not just "the capacitor runs out of charge". For the area estimate, working (square counting with the scale stated) earns the marks; a bare number with no scale or method does not. The final capacitance follows from $C = \frac{Q}{V}$ with the full initial p.d.

### Example 12: Van de Graaff dome - End-of-chapter Q12, 4 marks

**Question:** The spherical dome of a Van de Graaff generator has a diameter of $40~\text{cm}$ and the potential at its surface is $54~\text{kV}$. (a) Calculate the charge on the dome. [2] (b) Calculate the capacitance of the dome. [2]

**Method:**
1. Radius: $r = \frac{0.40}{2} = 0.20~\text{m}$ (use the radius, not the diameter). [1]
2. (a) $V = \frac{Q}{4\pi\epsilon_0 r}$, so $Q = 4\pi\epsilon_0 rV = \frac{rV}{8.99 \times 10^9} = \frac{0.20 \times 54 \times 10^3}{8.99 \times 10^9} = 1.2 \times 10^{-6}~\text{C}$. [2]
3. (b) $C = 4\pi\epsilon_0 r = \frac{0.20}{8.99 \times 10^9} = 2.2 \times 10^{-11}~\text{F} = 22~\text{pF}$. [2]

**Answer:** (a) $Q = 1.2 \times 10^{-6}~\text{C} = 1.2~\mu\text{C}$; (b) $C = 2.2 \times 10^{-11}~\text{F} = 22~\text{pF}$.

**What the examiner wants:** the radius is half the diameter (a common slip loses a factor of 2), and the marks require the sphere formulas $V = \frac{Q}{4\pi\epsilon_0 r}$ and $C = 4\pi\epsilon_0 r$ written or used. Note the dome's tiny capacitance: $22~\text{pF}$ at $54~\text{kV}$ still stores $1.2~\mu\text{C}$ because the voltage is huge.

### Example 13: Two brass spheres sharing charge - energy dissipated - End-of-chapter Q13, 12 marks

**Question:** Two identical conducting brass spheres of radius $10~\text{cm}$ sit on insulating stands. Sphere A has charge $+5.0 \times 10^{-8}~\text{C}$ and sphere B is uncharged. (a) Show that the capacitance of an isolated conducting sphere of radius $r$ is $C = 4\pi\epsilon_0 r$, and calculate the potential at the surface of sphere A. [4] (b) Calculate the energy stored on sphere A. [2] (c) Sphere B is brought up to sphere A and touched to it so the charge is shared, then separated. (i) Calculate the energy stored on each sphere. [3] (ii) Calculate the energy dissipated during the discharge. [1] (d) Suggest why there is a change in the total energy of the system. [1]

**Method:**
1. (a) Show: the potential at the surface of a charged sphere is $V = \frac{Q}{4\pi\epsilon_0 r}$, and since $C = \frac{Q}{V}$, $C = \frac{Q}{Q/(4\pi\epsilon_0 r)} = 4\pi\epsilon_0 r$. [2]
2. Potential: $V = \frac{Q}{4\pi\epsilon_0 r} = \frac{8.99 \times 10^9 \times 5.0 \times 10^{-8}}{0.10} = 4.5 \times 10^3~\text{V} = 4.5~\text{kV}$. [2]
3. (b) $W = \frac{1}{2}QV = \frac{1}{2} \times 5.0 \times 10^{-8} \times 4.5 \times 10^3 = 1.1 \times 10^{-4}~\text{J}$. [2]
4. (c)(i) Identical spheres share the charge equally: $Q = 2.5 \times 10^{-8}~\text{C}$ on each. [1]
5. Potential of each after sharing: $V = \frac{8.99 \times 10^9 \times 2.5 \times 10^{-8}}{0.10} = 2.25 \times 10^3~\text{V}$. [1]
6. Energy on each: $W = \frac{1}{2}QV = \frac{1}{2} \times 2.5 \times 10^{-8} \times 2.25 \times 10^3 = 2.8 \times 10^{-5}~\text{J}$; total $= 5.6 \times 10^{-5}~\text{J}$. [1]
7. (c)(ii) Energy dissipated $= 1.1 \times 10^{-4} - 5.6 \times 10^{-5} = 5.6 \times 10^{-5}~\text{J}$. [1]
8. (d) The missing energy is dissipated as heat and light (a spark) while the charge moves between the spheres; energy is conserved overall, but stored electrical energy is lost. [1]

**Answer:** (a) $V = 4.5 \times 10^3~\text{V}$; (b) $W = 1.1 \times 10^{-4}~\text{J}$; (c)(i) $2.8 \times 10^{-5}~\text{J}$ on each sphere (total $5.6 \times 10^{-5}~\text{J}$); (c)(ii) $5.6 \times 10^{-5}~\text{J}$ dissipated; (d) energy is lost as heat/light in the spark during the transfer.

**What the examiner wants:** the "show that" earns credit for both the surface potential formula and the substitution into $C = \frac{Q}{V}$. Charge sharing between IDENTICAL spheres means equal division. The energy comparison before and after is the same physics as Section 1.8: charge conserved, energy not.

### Example 14: Reed switch circuit - End-of-chapter Q14, 11 marks

**Question:** A reed switch vibrates back and forth at a frequency of $50~\text{Hz}$. Each time it contacts A, a $67~\text{mF}$ capacitor is charged by a $12~\text{V}$ battery; each time it contacts B, the capacitor is fully discharged through a resistor. (a)(i) Calculate the charge stored on the capacitor when there is a p.d. of $12~\text{V}$ across it. [2] (a)(ii) Calculate the average current in the resistor. [2] (a)(iii) Calculate the average power dissipated in the resistor. [3] (b) A second capacitor of the same value is connected in series with the first. Discuss the effect on both the current recorded and the power dissipated in the resistor. [4]

**Method:**
1. (a)(i) $Q = CV = 0.067 \times 12 = 0.80~\text{C}$. [2]
2. (a)(ii) The charge $0.80~\text{C}$ is dumped through the resistor $50$ times per second, so average current $= Qf = 0.80 \times 50 = 40~\text{A}$. [2]
3. (a)(iii) Energy per cycle: $W = \frac{1}{2}CV^2 = \frac{1}{2} \times 0.067 \times 12^2 = 4.8~\text{J}$. [2]
4. Average power $= Wf = 4.8 \times 50 = 240~\text{W}$. [1]
5. (b) Two equal capacitors in series: total capacitance halves to $33.5~\text{mF}$. [1]
6. At the same $12~\text{V}$, the charge stored per cycle halves: $Q = 0.40~\text{C}$, so the average current halves to about $20~\text{A}$. [1]
7. The energy stored per cycle halves ($W = \frac{1}{2}CV^2$ with $C$ halved), so the average power halves to about $120~\text{W}$. [1]
8. The readings are halved because each cycle moves only half the charge, and that charge is delivered at the same p.d. [1]

**Answer:** (a)(i) $Q = 0.80~\text{C}$; (a)(ii) $I = 40~\text{A}$; (a)(iii) $P = 240~\text{W}$; (b) the series capacitor halves the total capacitance, so the charge per cycle, the average current and the average power all halve (about $20~\text{A}$ and $120~\text{W}$).

**What the examiner wants:** the average current is "charge per unit time", i.e. the charge transferred each cycle times the frequency. The average power is "energy per unit time", i.e. $\frac{1}{2}CV^2$ per cycle times the frequency. For part (b) the 4 marks are: capacitance halves, charge halves, current halves, energy/power halves - each idea earns a mark, and the effect on power must be justified via the energy per cycle.

---

# Chapter 25: Electronics
> Source: `physics/notes/chapter-25-electronics-notes.md`

## 4. Methods (Question Types & Methods)

These are the ways Cambridge has actually asked about electronics. Each method below is what a full-mark answer looks like.

### 1. Read a sensor's resistance from a graph

**Method:**
1. Identify the curve for the right component (LDR against light intensity in lux; thermistor against temperature in °C).
2. Read the resistance at the stated value of the quantity, converting the axis units (kΩ to Ω if needed).
3. Use that resistance in the potential divider formula (Method 2).

**Traps:** reading the wrong curve (thermistor vs metal wire - the metal wire's resistance rises with temperature); mixing up kΩ and Ω; misreading the lux or °C axis.

### 2. Output voltage of a sensor potential divider

**Method:**
1. Decide which component the output is across - that component is $R_2$ in $V_{\text{out}} = \frac{R_2}{R_1 + R_2} V_s$.
2. Write the sensor resistance at the stated condition (from the question or the graph).
3. Substitute both resistances (same units - keep both in kΩ or both in Ω) and the supply p.d.
4. Quote $V_{\text{out}}$ to 3 significant figures with the unit V.

**Traps:** putting the output across the wrong resistor in the formula; mixing units (20 kΩ + 300 Ω must become 20 300 Ω or 20 + 0.3 kΩ); giving $8.69$ instead of rounding $8.69565$ to $8.70$ (3 s.f.).

### 3. Design a sensing circuit (which component does the output go across)

**Method:**
1. Note the required behaviour: does $V_{\text{out}}$ need to rise or fall as the sensed quantity rises?
2. For an LDR or NTC thermistor, resistance falls as the sensed quantity rises. If the output is across the sensor, $V_{\text{out}}$ falls; if across the fixed resistor, $V_{\text{out}}$ rises.
3. Choose the arrangement that matches: output across the fixed resistor for "increases with quantity", across the sensor for "decreases with quantity".
4. To set a threshold, use a variable resistor and adjust it.

**Traps:** forgetting which way the sensor's resistance moves; drawing the output across both resistors (there is no output point); forgetting to show the supply and the $0~\text{V}$ line.

### 4. Comparator: find both input potentials, then decide the output

**Method:**
1. Treat each input separately: each is fed by its own potential divider, so compute $V_+$ and $V_-$ with the divider formula.
2. Compare them: $V_+ > V_-$ gives output $\approx +V_s$; $V_+ < V_-$ gives output $\approx -V_s$.
3. If the op-amp is not saturated and $G_0$ is given, use $V_{\text{out}} = G_0 (V_+ - V_-)$ and check against the supply.
4. State the switching condition in words (e.g. "the output switches when the temperature falls below the value at which $V_+ = V_-$").

**Traps:** computing only one input potential; mixing up the inputs; writing an absurd unsaturated output (e.g. 5000 V) instead of the supply rail.

### 5. Modify a comparator to reverse the switching behaviour

**Method:**
1. Work out which divider output rises and which falls as the sensed quantity changes.
2. To reverse the switching, swap the sensor and the fixed resistor in the sensor divider (or swap which input the sensor divider feeds).
3. Check with one hot and one cold example that the output states have swapped.

**Traps:** swapping the reference divider instead of the sensor divider; forgetting the switching temperature can also be adjusted by changing the series resistor value.

### 6. Inverting amplifier: gain, output, saturation limit

**Method:**
1. Gain: $G = -\frac{R_f}{R_{\text{in}}}$ (keep both resistances in the same unit).
2. Output: $V_{\text{out}} = G \times V_{\text{in}}$, keeping the minus sign.
3. Check against the rails: if $|V_{\text{out}}| > V_s$, the output is saturated at $\pm V_s$.
4. Maximum input before saturation: $V_{\text{in(max)}} = \frac{V_s}{|G|}$.
5. Input resistance of the amplifier $= R_{\text{in}}$ (virtual earth).

**Traps:** dropping the minus sign; forgetting the saturation clamp; dividing by the gain instead of multiplying; unit slips (mV vs V).

### 7. Non-inverting amplifier: gain and output

**Method:**
1. Gain: $G = 1 + \frac{R_1}{R_2}$.
2. Output: $V_{\text{out}} = G \times V_{\text{in}}$ (no sign change - the output is in phase).
3. Check saturation against the rails, especially when the input is large.

**Traps:** forgetting the $+1$; using the inverting formula by mistake; forgetting the output saturates when $G \times V_{\text{in}}$ exceeds the supply.

### 8. The virtual earth current method (find a current or resistance)

**Method:**
1. State that the inverting input is a virtual earth: at (almost) $0~\text{V}$.
2. Current through the input resistor: $I_{\text{in}} = \frac{V_{\text{in}}}{R_{\text{in}}}$ (the far end of $R_{\text{in}}$ is at $0~\text{V}$).
3. No current enters the op-amp input, so the same current flows through the feedback resistor: $I_f = I_{\text{in}}$.
4. $V_{\text{out}} = -I_f R_f$ (negative because the current leaves the virtual earth for the output).

**Traps:** thinking current flows into the op-amp; forgetting the virtual earth is at $0~\text{V}$ so $I_{\text{in}} = V_{\text{in}}/R_{\text{in}}$ directly; sign errors on $V_{\text{out}}$.

### 9. Strain gauge: resistance change to length change to output

**Method:**
1. From the divider output voltage, find the gauge resistance (Method 2, rearranged).
2. Change in resistance: $\delta R = R_{\text{new}} - R_0$.
3. Length change: use $\frac{\delta R}{R} = \frac{2\,\delta L}{L}$ (or $\frac{\delta R}{R} = \frac{\delta L}{L}$ if the question states the area is constant).
4. Strain: $\frac{\delta L}{L}$, dimensionless; the strain of the gauge equals the strain of the surface it is glued to.

**Traps:** using the wrong proportionality factor (2 vs 1) without reading the question; leaving lengths in cm and mixing with m; quoting strain with units.

### 10. Output devices: LED resistor and relay protection

**Method:**
1. LED: $R = \frac{V_{\text{out}} - 2~\text{V}}{I}$, with $I \approx 20~\text{mA}$ converted to amperes.
2. Relay: coil in series with the op-amp output; reverse-biased diode $D_1$ across the coil (protects against the induced e.m.f. when the coil is switched off); series diode $D_2$ if the relay must operate only for a positive output.
3. State why each diode is there - the marks are for the reasons.

**Traps:** forgetting to subtract the $2~\text{V}$ across the LED; mA not converted to A; drawing $D_1$ forward-biased; saying the relay "amplifies" the current (it switches a separate circuit, it does not amplify).

### 11. Sketch graphs: amplifier input/output and calibration curves

**Method:**
1. Amplifier: draw the input sine wave, then the output with the correct amplitude (gain $\times$ input) and the correct phase (inverting: $180^\circ$ out; non-inverting: in phase); clip the output at the supply rails if it would exceed them.
2. Calibration: plot voltmeter reading against the physical quantity from the calibration experiment; the curve is usually not a straight line (the sensor is non-linear); use it to convert readings.

**Traps:** wrong phase relationship; output amplitude not scaled by the gain; forgetting saturation clipping; drawing a linear calibration curve for a thermistor (it is curved).

### 12. Definitions and explanation questions (feedback, virtual earth, gains)

**Method:**
1. Feedback: "part of the output is returned/connected back to the input" - then give the effect (gain reduced, stability increased, bandwidth increased, distortion reduced).
2. Virtual earth: "the inverting input is at almost zero volts, although not connected to earth, because the high open-loop gain keeps the input difference almost zero" - never "it is connected to earth".
3. Why inverting gain can be below 1: the magnitude is just the resistor ratio $R_f/R_{\text{in}}$, which can be any positive value.
4. Why non-inverting gain cannot be below 1: $G = 1 + \frac{R_1}{R_2}$ and $R_1/R_2 \geq 0$.

**Traps:** giving the equation without the explanation (equation alone earns only part of the marks); "virtual earth = connected to earth" (a definite zero); "feedback makes the amplifier stronger" (feedback reduces gain).

## 5. Solved Examples

Real exam-style questions from the end of Chapter 25, with their mark allocations, plus the book's worked examples. The format for every example: Question / Method / Answer / What the examiner wants. Marks are summed from the printed allocations; where the printed layout was garbled, the split is noted as reconstructed.

### Example 1: Reversing a temperature comparator - End-of-chapter Q1, 1 mark

**Question:** How can the circuit of Figure 25.17 be altered so that the op-amp switches from $+9~\text{V}$ to $-9~\text{V}$ when the temperature rises, instead of when it falls? Draw the circuit diagram. [1]

**Method:**
1. In the original circuit the thermistor is between $+9~\text{V}$ and point A, and the $10~\text{k}\Omega$ resistor is between A and the $0~\text{V}$ line. As temperature falls, $R_T$ rises, $V_A = 9 \times \frac{10}{R_T + 10}$ falls below $4.5~\text{V}$, and the output switches from $+9~\text{V}$ to $-9~\text{V}$.
2. To make the output switch when the temperature RISES, swap the two components: put the $10~\text{k}\Omega$ resistor between $+9~\text{V}$ and A, and the thermistor between A and $0~\text{V}$.
3. Check: now $V_A = 9 \times \frac{R_T}{R_T + 10}$. When the temperature rises, $R_T$ falls, $V_A$ falls below $4.5~\text{V}$, and the output switches from $+9~\text{V}$ to $-9~\text{V}$.

**Answer:** swap the thermistor and the $10~\text{k}\Omega$ resistor in the sensor potential divider (thermistor connected to the $0~\text{V}$ line, $10~\text{k}\Omega$ to $+9~\text{V}$).

**What the examiner wants:** 1 mark for the swap. The switching temperature is still where $R_T = 10~\text{k}\Omega$ (the divider ratio is unchanged, just mirrored).

### Example 2: Comparator with an LDR - End-of-chapter Q2, 3 marks

**Question:** Draw the circuit diagram of a comparator that switches the output voltage from positive to negative when the light intensity falling on an LDR decreases. [3]

**Method:**
1. Sensor divider: LDR in series with a fixed resistor $R$ across the $+9~\text{V}$ supply and $0~\text{V}$ line, with the LDR connected to $+9~\text{V}$. The junction voltage is $V_A = 9 \times \frac{R}{R_{\text{LDR}} + R}$: bright light (small $R_{\text{LDR}}$) gives a high $V_A$; dim light (large $R_{\text{LDR}}$) gives a low $V_A$.
2. Reference divider: two equal resistors (or a variable resistor) across the supply, giving a fixed reference $V_{\text{ref}}$ between the two extremes, e.g. $4.5~\text{V}$.
3. Connect $V_A$ to the non-inverting input $(+)$ and $V_{\text{ref}}$ to the inverting input $(-)$, with the op-amp supplied at $\pm 9~\text{V}$.
4. Check: bright light gives $V_+ > V_-$, output $+9~\text{V}$; when the light falls, $V_A$ drops below $V_{\text{ref}}$, and the output switches to $-9~\text{V}$.

**Answer:** LDR plus fixed resistor as the sensor potential divider feeding $(+)$; fixed reference voltage (from a second potential divider) feeding $(-)$; op-amp with $\pm 9~\text{V}$ supplies.

**What the examiner wants:** 1 mark for the sensor potential divider with the LDR, 1 for a reference voltage, 1 for the correct connections (sensor divider to $(+)$, reference to $(-)$) so the output goes negative as the light falls.

### Example 3: Feedback and virtual earth definitions - End-of-chapter Q3, 1 + 2 marks

**Question:** Explain what is meant by (a) feedback [1] (b) the virtual earth approximation. [2]

**Method:**
1. (a) Feedback: part (or all) of the output of a system is returned (fed back) to its input, so the output affects the input. In an op-amp circuit, the output is connected back to the inverting input.
2. (b) Virtual earth: the potential at the inverting input of an inverting amplifier is (almost) zero, even though that input is not connected to earth. This happens because the open-loop gain is very high, so the potential difference between the two inputs is driven to almost zero; since the non-inverting input is at $0~\text{V}$, the inverting input is at almost $0~\text{V}$ too.

**Answer:** (a) returning part of the output to the input; (b) the inverting input sits at almost $0~\text{V}$ (not connected to earth) because the very high open-loop gain keeps the two inputs at almost the same potential.

**What the examiner wants:** feedback earns 1 mark for "part of the output is returned to the input". Virtual earth earns 2: "inverting input at (almost) zero volts" (1) and "because the input difference is almost zero / gain is very high" (1). "Connected to earth" scores zero - it is NOT connected.

### Example 4: Inverting amplifier calculations - End-of-chapter Q4, 2 + 2 + 1 marks

**Question:** In the inverting amplifier of Figure 25.20, $R_{\text{in}} = 10~\text{k}\Omega$, $R_f = 200~\text{k}\Omega$ and $V_s = 12~\text{V}$. Calculate: (a) the gain of the amplifier [2] (b) the input voltage when the output voltage is $8.0~\text{V}$ [2] (c) the maximum input voltage. [1]

**Method:**
1. (a) $G = -\frac{R_f}{R_{\text{in}}} = -\frac{200}{10} = -20$. [2]
2. (b) $V_{\text{out}} = G V_{\text{in}}$, so $V_{\text{in}} = \frac{V_{\text{out}}}{G} = \frac{8.0}{-20} = -0.40~\text{V}$. [2]
3. (c) Saturation at $V_{\text{out}} = \pm 12~\text{V}$: $V_{\text{in(max)}} = \frac{V_s}{|G|} = \frac{12}{20} = 0.60~\text{V}$. [1]

**Answer:** (a) $G = -20$; (b) $V_{\text{in}} = -0.40~\text{V}$; (c) maximum input $V_{\text{in}} = 0.60~\text{V}$ (so the output just reaches the rail).

**What the examiner wants:** part (a) 2 marks: formula plus substitution. Part (b) 2 marks: rearrangement and substitution with the sign correct (a positive output needs a negative input). Part (c) 1 mark: $12/20$, with the concept that the output cannot exceed the supply.

### Example 5: Gains below 1 - End-of-chapter Q5, 2 + 2 marks

**Question:** (a) Explain how an inverting amplifier can have a gain of $-0.5$. [2] (b) Explain why the gain of a non-inverting amplifier cannot be less than 1. [2]

**Method:**
1. (a) The gain is $G = -\frac{R_f}{R_{\text{in}}}$, and its magnitude is set by the resistor ratio. Choose $R_f$ smaller than $R_{\text{in}}$, e.g. $R_f = 5~\text{k}\Omega$ and $R_{\text{in}} = 10~\text{k}\Omega$: then $G = -\frac{5}{10} = -0.5$. The magnitude can be any positive value - even below 1. [2]
2. (b) $G = 1 + \frac{R_1}{R_2}$. Since $R_1$ and $R_2$ are positive resistances, $\frac{R_1}{R_2} \geq 0$, so $G \geq 1$. The smallest possible gain is 1 (when $R_1 = 0$). [2]

**Answer:** (a) choose the resistor ratio $R_f/R_{\text{in}} = 0.5$ (e.g. $5~\text{k}\Omega$ and $10~\text{k}\Omega$); (b) because $G = 1 + R_1/R_2$ with $R_1/R_2 \geq 0$.

**What the examiner wants:** the marks are for the reasoning, not the numbers: an inverting amplifier's gain magnitude is any ratio of two resistances; the non-inverting formula has the $+1$ built in. Candidates who write only "the resistor values are chosen" without the formula lose the second mark.

### Example 6: Sketching amplifier input and output - End-of-chapter Q6, 3 marks

**Question:** The non-inverting amplifier in Figure 25.21 has $R_1 = 15~\text{k}\Omega$, $R_2 = 5~\text{k}\Omega$ and $V_s = 10~\text{V}$. An a.c. signal of amplitude $0.20~\text{V}$ is applied to the input. Draw a single sketch graph which shows both the input and the output voltage over the same axes. [3]

**Method:**
1. Gain: $G = 1 + \frac{R_1}{R_2} = 1 + \frac{15}{5} = 4$.
2. Output amplitude: $V_{\text{out}} = 4 \times 0.20 = 0.80~\text{V}$ (well below the $10~\text{V}$ rails, so no clipping).
3. Graph: two sine waves on the same time axis, in phase (non-inverting), input amplitude $0.20~\text{V}$, output amplitude $0.80~\text{V}$, both centred on $0~\text{V}$, axes labelled.

**Answer:** two in-phase sine waves; input peaks at $\pm 0.20~\text{V}$, output peaks at $\pm 0.80~\text{V}$.

**What the examiner wants:** 1 mark for the correct amplitude ratio (4:1), 1 for the in-phase relationship, 1 for labelled axes and correct relative sizes. Drawing the output inverted (as for an inverting amplifier) loses the phase mark.

### Example 7: Identify the amplifier type and gain - End-of-chapter Q7, 3 marks

**Question:** Is the circuit shown in Figure 25.27 an inverting or non-inverting amplifier? Calculate its gain. ($R_{\text{in}} = 9~\text{k}\Omega$, $R_f = 1~\text{k}\Omega$, input to the inverting input through $R_{\text{in}}$, $+$ input at $0~\text{V}$.) [3]

**Method:**
1. The input is applied to the inverting input $(-)$ through $R_{\text{in}}$, the non-inverting input is at $0~\text{V}$, and $R_f$ connects the output back to the inverting input: this is the inverting amplifier configuration.
2. $G = -\frac{R_f}{R_{\text{in}}} = -\frac{1}{9} = -0.11$ (3 s.f.).

**Answer:** inverting amplifier; $G = -0.11$ (that is, $-1/9$).

**What the examiner wants:** the identification (input at $(-)$ through a resistor is the giveaway) and the ratio. Note the magnitude is below 1 - perfectly normal for an inverting amplifier, since the gain is just the resistor ratio.

### Example 8: LDR sensor circuit design - End-of-chapter Q8, 2 + 2 + 2 marks

**Question:** A light-dependent resistor is used with additional components to make a sensor. The voltage output increases as light intensity increases. (a) Sketch the diagram of a suitable circuit. [2] (b) Explain how your circuit works. [2] (c) State which parts of your circuit are the sensor, the processor and the output device. [2]

**Method:**
1. (a) LDR in series with a fixed resistor across a cell; output taken across the FIXED resistor (LDR connected to the positive terminal of the cell, fixed resistor to the $0~\text{V}$ line, output at their junction). [2]
2. (b) The two resistors form a potential divider. When the light intensity increases, the LDR resistance falls, so the LDR takes a smaller share of the supply voltage and the fixed resistor takes a larger share: the output voltage across the fixed resistor rises. [2]
3. (c) Sensor: the LDR (its resistance changes with light). Processor: the potential divider circuit (turns the resistance change into an output voltage). Output device: the voltmeter (or the device the voltage drives). [2]

**Answer:** (a) LDR and fixed resistor in series across the cell, output across the fixed resistor; (b) brighter light lowers $R_{\text{LDR}}$, so the fixed resistor takes a bigger share of the supply p.d. and $V_{\text{out}}$ rises; (c) sensor = LDR, processor = potential divider, output device = voltmeter.

**What the examiner wants:** part (a) needs the series pair, the supply, and the output across the FIXED resistor - taking it across the LDR gives a falling output. Part (b) needs the potential-divider argument (share of voltage proportional to resistance). Part (c) rewards the three-part vocabulary: sensing device, processor, output device.

### Example 9: Strain gauge on a metal bar - End-of-chapter Q9, 2 + 2 + 2 marks

**Question:** A strain gauge is used to measure the extension of a metal bar. The gauge is stuck to the bar and the change in resistance of the wire in the gauge enables the extension to be determined. The strain gauge is connected in the circuit shown in Figure 25.28: a $5.0~\text{V}$ d.c. supply, the strain gauge and a $300~\Omega$ resistor in series, voltmeter across the strain gauge. (a) Explain why the resistance of the wire increases when it is stretched and show that the change in resistance is proportional to the extension, provided that the cross-sectional area is constant. [2] (b) The resistance of the strain gauge when unstretched is $150~\Omega$. Calculate the reading on the voltmeter. [2] (c) State and explain the effect on the voltmeter reading when the strain gauge is stretched. [2]

**Method:**
1. (a) Stretching makes the wire longer and narrower. With $R = \frac{\rho L}{A}$, an increase in $L$ (with $A$ constant) increases $R$: $R + \delta R = \frac{\rho (L + \delta L)}{A}$, so $\delta R = \frac{\rho\,\delta L}{A}$ and $\frac{\delta R}{R} = \frac{\delta L}{L}$. Hence $\delta R \propto \delta L$ for constant $A$. [2]
2. (b) Potential divider across the strain gauge: $V = 5.0 \times \frac{150}{150 + 300} = 1.67~\text{V}$. [2]
3. (c) When stretched, $R$ increases, so the strain gauge takes a larger share of the supply p.d.: the voltmeter reading rises. [2]

**Answer:** (a) longer wire (and narrower, but the question fixes $A$) means larger $R$; $\frac{\delta R}{R} = \frac{\delta L}{L}$, so $\delta R \propto \delta L$; (b) $V = 1.67~\text{V}$; (c) the reading increases because the gauge's share of the $5.0~\text{V}$ grows with its resistance.

**What the examiner wants:** part (a) 2 marks: the "longer and narrower" idea (1) and the proportionality from $R = \rho L/A$ (1). Part (b): divider substitution with units. Part (c): the potential-divider reasoning - resistance up means p.d. across it up. (Assumption: the voltmeter is across the strain gauge, as the printed figure layout indicates; if your copy shows it across the $300~\Omega$ resistor, the reading is $3.33~\text{V}$ and falls when stretched.)

### Example 10: Fibre optic microphone amplifier - End-of-chapter Q10, 2 + 2 + 2 + 2 + 2 marks

**Question:** In a fibre optic system, sound into a microphone is used to produce different intensities of light passed along a glass fibre. The microphone is connected to a non-inverting amplifier (dual $15~\text{V}$ supplies), the output of which is connected to an LED. The microphone produces a maximum output of $+20~\text{mV}$. (a)(i) State two advantages of using negative feedback in the amplifier circuit. [2] (a)(ii) Calculate the maximum possible gain for the amplifier. [2] (b) Copy and complete the circuit to show the resistors necessary for a non-inverting amplifier, the connection of the microphone, and the output components needed. [2] (c)(i) With the maximum possible gain, suggest suitable values for all the resistors drawn. [2] (c)(ii) Explain what happens in the system when the voltage output from the microphone rises. [2]

**Method:**
1. (a)(i) Any two: less distortion; increased bandwidth; more stable gain (unaffected by temperature); low output resistance; high input resistance. [2]
2. (a)(ii) The output cannot exceed the supply: maximum gain $= \frac{V_s}{V_{\text{in(max)}}} = \frac{15}{20 \times 10^{-3}} = 750$. [2]
3. (b) $R_2$ from the inverting input to the $0~\text{V}$ line; $R_1$ from the output to the inverting input; microphone connected between the $0~\text{V}$ line and the non-inverting input; LED with a series resistor from the output to the $0~\text{V}$ line. [2]
4. (c)(i) Gain $= 1 + \frac{R_1}{R_2} = 750$, so $\frac{R_1}{R_2} = 749$. Choose $R_2 = 1~\text{k}\Omega$ and $R_1 = 749~\text{k}\Omega$ (or any pair with the same ratio, e.g. $10~\text{k}\Omega$ and $7.49~\text{M}\Omega$). LED series resistor: $R = \frac{V_{\text{out}} - 2}{I} = \frac{15 - 2}{0.020} = 650~\Omega$. [2]
5. (c)(ii) As the microphone output rises, the amplifier output rises (in phase), the p.d. across the LED and its series resistor rises, the LED current increases, the LED emits more light, and the light intensity passed along the fibre increases. [2]

**Answer:** (a)(i) e.g. less distortion and increased bandwidth; (a)(ii) $G = 750$; (b) standard non-inverting resistor pair, microphone to $(+)$, LED plus $650~\Omega$ series resistor from output to $0~\text{V}$; (c)(i) $R_1 = 749~\text{k}\Omega$, $R_2 = 1~\text{k}\Omega$, LED resistor $650~\Omega$; (c)(ii) the LED shines more brightly, so more light travels down the fibre.

**What the examiner wants:** the gain limit comes from saturation at $15~\text{V}$ - candidates who use $750$ without the $20~\text{mV}$ conversion lose the method mark. The resistor values must give a gain of (about) $750$; the LED resistor calculation must subtract the $2~\text{V}$ LED drop and convert $20~\text{mA}$ to amperes.

### Example 11: Two-LDR motor controller - End-of-chapter Q11, 1 + 1 + 2 + 5 marks

**Question:** A student builds a circuit to control a motor using two identical LDRs, P and Q (Figure 25.30). In room light the resistance of each LDR is $500~\Omega$; when a torch shines on an LDR its resistance becomes $200~\Omega$. Each LDR is in series with a $300~\Omega$ resistor across the $+9~\text{V}$ supply, with junctions A (P side) and B (Q side). A connects to the inverting input $(-)$ and B to the non-inverting input $(+)$ of an op-amp with $\pm 9~\text{V}$ supplies; the motor is between the output and $0~\text{V}$. (a) State the value of the output voltage when: (i) the potential at A is greater than the potential at B [1] (ii) the potential at B is greater than the potential at A. [1] (b) Calculate the potential at point A when a torch shines on P. [2] (c) Explain what happens when (i) a torch shines on P but not on Q [2] (ii) a torch shines on Q but not on P [2] (d) Explain why it is difficult to know what will happen if no torch shines on P or Q. [1]

**Method:**
1. (a)(i) A is the inverting input, so $V_A > V_B$ means $V_- > V_+$: the output saturates at the negative rail, $V_{\text{out}} = -9~\text{V}$. [1]
2. (a)(ii) $V_B > V_A$ means $V_+ > V_-$: $V_{\text{out}} = +9~\text{V}$. [1]
3. (b) Torch on P: $R_P = 200~\Omega$, fixed resistor $300~\Omega$, supply $9~\text{V}$: $V_A = 9 \times \frac{300}{200 + 300} = 5.4~\text{V}$. [2]
4. (c)(i) Torch on P only: $V_A = 5.4~\text{V}$; Q is in room light, so $V_B = 9 \times \frac{300}{500 + 300} = 3.4~\text{V}$. $V_A > V_B$, so the output is $-9~\text{V}$ and the motor turns (in the reverse direction). [2]
5. (c)(ii) Torch on Q only: $V_B = 5.4~\text{V}$, $V_A = 3.4~\text{V}$. $V_B > V_A$, so the output is $+9~\text{V}$ and the motor turns the other way. [2]
6. (d) With no torch, both LDRs are at $500~\Omega$ and the two divider outputs are exactly equal ($3.4~\text{V}$); the op-amp input difference is effectively zero, and any tiny imbalance (component tolerance, noise, input offset) decides the output, so it cannot be predicted. [1]

**Answer:** (a)(i) $-9~\text{V}$; (a)(ii) $+9~\text{V}$; (b) $V_A = 5.4~\text{V}$; (c)(i) output $-9~\text{V}$, motor turns one way; (c)(ii) output $+9~\text{V}$, motor turns the other way; (d) the inputs are (almost) equal, so the output is unpredictable.

**What the examiner wants:** the sign answers depend on which input each junction feeds - A to $(-)$, B to $(+)$ as stated. The divider calculation in (b) is the standard $V = V_s \times R_{\text{fixed}}/(R_{\text{LDR}} + R_{\text{fixed}})$. Part (d) earns the mark for the "equal inputs, so the output is not defined" idea - not for saying the motor "stops" (it does not; it is driven to one rail or the other). (Mark split reconstructed from the printed layout; the three explanation parts total 5 marks.)

### Example 12: Virtual earth and inverting gain - End-of-chapter Q12, 2 + 2 + 1 marks

**Question:** (a) Explain what is meant by a virtual earth, and use your explanation to show that the gain of the inverting amplifier in Figure 25.31 is $-\frac{R_2}{R_1}$. [2] (b) In that amplifier $R_1 = 20~\text{k}\Omega$, $R_2 = 4~\text{k}\Omega$ and $V_{\text{in}} = 0.50~\text{V}$. Calculate the value of $V_{\text{out}}$. [2] (c) A resistor of $4~\text{k}\Omega$ is placed in parallel with $R_2$. Calculate the new value of $V_{\text{out}}$. [1]

**Method:**
1. (a) The inverting input is a virtual earth: at almost $0~\text{V}$ (high open-loop gain, $+$ input at $0~\text{V}$). No current enters the input, so the current in $R_1$ equals the current in $R_2$: $\frac{V_{\text{in}}}{R_1} = -\frac{V_{\text{out}}}{R_2}$, giving $V_{\text{out}} = -\frac{R_2}{R_1} V_{\text{in}}$ and gain $= -\frac{R_2}{R_1}$. [2]
2. (b) $G = -\frac{R_2}{R_1} = -\frac{4}{20} = -0.20$; $V_{\text{out}} = -0.20 \times 0.50 = -0.10~\text{V}$. [2]
3. (c) Parallel combination: $R_2' = \frac{4 \times 4}{4 + 4} = 2~\text{k}\Omega$. New gain $= -\frac{2}{20} = -0.10$; $V_{\text{out}} = -0.10 \times 0.50 = -0.050~\text{V}$. [1]

**Answer:** (a) derivation via equal currents through $R_1$ and $R_2$ at the virtual earth; (b) $V_{\text{out}} = -0.10~\text{V}$; (c) $V_{\text{out}} = -0.050~\text{V}$ (gain halved because $R_2$ halved).

**What the examiner wants:** part (a) 2 marks: the virtual earth idea (1) and the equal-currents derivation giving the ratio (1). Part (c): the parallel resistance halves $R_2$, halving the magnitude of the gain.

### Example 13: Heater switching circuit - End-of-chapter Q13, 2 + 1 marks

**Question:** In order to switch on a heater when the temperature falls below a set value, a potential divider is connected to a switching circuit. When the input voltage to the switching circuit falls below $0.5~\text{V}$, it switches the heater on. (a) Copy Figure 25.32 and add a suitable potential divider circuit to trigger the switching circuit. [2] (b) Explain how the operator could lower the temperature at which the heater is switched on. [1]

**Method:**
1. (a) NTC thermistor in series with a fixed resistor across the supply. Put the THERMISTOR between the positive supply and the output point, and the fixed resistor between the output point and $0~\text{V}$, with the output taken across the fixed resistor and fed to the switching circuit. Then $V_{\text{out}} = V_s \times \frac{R_{\text{fixed}}}{R_T + R_{\text{fixed}}}$: when the temperature falls, $R_T$ rises and $V_{\text{out}}$ falls. Choose the resistor so $V_{\text{out}} = 0.5~\text{V}$ at the set temperature. [2]
2. (b) Increase the resistance of the fixed resistor (use a variable resistor and increase its setting). For any given temperature $V_{\text{out}}$ rises, so the temperature must fall further (to a larger $R_T$) before $V_{\text{out}}$ reaches $0.5~\text{V}$: the heater switches on at a lower temperature. [1]

**Answer:** (a) thermistor to $+V_s$, fixed (or variable) resistor to $0~\text{V}$, output across the fixed resistor to the switching circuit; (b) increase the fixed resistance.

**What the examiner wants:** part (a) 2 marks: the divider with the thermistor (1) and the output position across the fixed resistor so the voltage falls when cold (1). Part (b): increasing $R_{\text{fixed}}$ raises the output for a given temperature, so the switch-on temperature drops.

### Example 14: Room light monitor - End-of-chapter Q14, 3 + 1 marks

**Question:** Figure 25.33 shows a circuit used to monitor the variation of light intensity in a room: component X and a variable resistor form a potential divider across a supply, and the potential at their junction feeds one input of an op-amp comparator whose other input is a reference voltage; the op-amp output drives an output device. (a) Identify the component X and describe how the circuit works. [3] (b) Suggest the reason for including the variable resistor in the circuit. [1]

**Method:**
1. (a) X is a light-dependent resistor (LDR). The LDR and the variable resistor form a potential divider, so the p.d. across the LDR (or across the variable resistor) changes as the room light intensity changes: brighter light lowers $R_{\text{LDR}}$ and changes the junction potential. The op-amp compares this potential with the reference at its other input; when the light intensity crosses the threshold, the huge open-loop gain drives the output from one supply rail to the other. The output voltage therefore switches sharply when the light intensity passes the set level, which can be used to operate an indicator. [3]
2. (b) The variable resistor sets the light intensity at which the output switches (the threshold level) - it can be adjusted to the required "trigger" brightness. [1]

**Answer:** (a) X is an LDR; the divider output changes with light intensity and the comparator switches its output between the supply rails when the intensity crosses the reference level; (b) the variable resistor sets the threshold light intensity at which the output switches.

**What the examiner wants:** part (a) 3 marks: identifying X as the LDR (1), the potential-divider action producing a voltage that changes with light (1), and the comparison/switching action of the op-amp (1). Part (b): "sets the level at which the circuit switches" (1).

---

# Chapter 26: Magnetic Fields and Electromagnetism
> Source: `chapter-26-magnetic-fields-and-electromagnetism-notes.md`

## 4. Methods (Question Types)

**Method 1: Sketching or describing magnetic field patterns**

- For a straight wire: concentric circles centred on the wire; spacing increases with distance (weaker field). Use the right-hand rule for direction - thumb = current, fingers = field.
- For a solenoid or flat coil: pattern like a bar magnet - lines leave one end (N), curve round outside, enter the other end (S); inside the coil the lines are parallel and close together (strong uniform field).
- Reversing the current reverses every arrow. Doubling the current doesn't change the shape, only the strength (lines drawn closer together).

**Traps:** forgetting that the field inside a solenoid runs from S to N (the same direction as the thumb); drawing the field of a wire as a dipole (it has no poles); reversing only some of the arrows when the current reverses.

**Method 2: Finding the force on a straight conductor ($F = BIL$)**

1. Check the angle: if the wire is at right angles to the field, use $F = BIL$; if at angle $\theta$, use $F = BIL\sin\theta$; if parallel, the force is zero.
2. Convert everything to SI: cm to m, mA to A, mT to T.
3. Substitute and give the unit (N). State the direction using Fleming's left-hand rule (or say 'at right angles to both field and current').

**Traps:** using the full wire length instead of the length inside the field; using $\sin\theta$ when the angle given is between the field and the wire but measured the wrong way (the angle must be between the field direction and the current direction); forgetting that a wire parallel to the field feels no force at all.

**Method 3: Measuring $B$ with a current balance**

1. Find the magnetic force from the balance: $F = mg$, where $m$ is the change in reading (or the balancing mass) and $g = 9.81~\text{m s}^{-2}$.
2. Measure the length $L$ of wire actually inside the field.
3. Use $B = \frac{F}{IL}$.

**Traps:** using the whole mass on the balance instead of the change; forgetting that the magnets experience the reaction force (Newton's third law), not the wire's own weight; giving the answer in mT when the working used T.

**Method 4: Direction questions (which way does the wire move / which way does the force act)**

1. Identify the direction of the external magnetic field (N to S).
2. Identify the direction of the conventional current.
3. Apply Fleming's left-hand rule: First finger = Field, seCond finger = Current, thuMb = Motion.
4. For a force ON a wire crossing a field: check whether the current is into or out of the page (the $\times$/$\bullet$ convention).

**Traps:** using the right hand (Fleming's rule is left-hand for motors); using electron flow instead of conventional current; confusing the force direction with the field direction (they are always perpendicular).

**Method 5: Torque on a motor coil**

1. Force on one side: $F = BIL$ for each side at right angles to the field.
2. The two opposite sides feel equal and opposite forces - a couple. Torque = force $\times$ perpendicular separation of the two forces.
3. Maximum torque when the plane of the coil is parallel to the field (sides at right angles to the field); zero torque when the coil face is perpendicular to the field.

**Traps:** using the coil area instead of the side length in $F = BIL$; halving the separation instead of using the full distance between the two forces; saying 'more turns makes the motor faster' without noting that torque increases with each extra turn ($N$ times the single-coil torque).

**Method 6: Forces between parallel wires**

1. Parallel currents (same direction) attract; anti-parallel currents (opposite directions) repel.
2. To find the size of the force, treat one wire's field as the external field acting on the other wire: $F = BIL$ where $B = 2.0 \times 10^{-7}\frac{I}{x}$ at distance $x$.
3. By Newton's third law the forces on the two wires are equal and opposite.

**Traps:** saying opposite currents attract (they repel - the opposite of electric charges); forgetting the factor of 2.0 in the wire field formula; using the wire separation as the length $L$.

**Method 7: SI base-unit questions (show that $1~\text{T} = 1~\text{kg A}^{-1}\text{s}^{-2}$)**

1. Start from a formula you know, e.g. $B = \frac{F}{IL}$.
2. Replace every quantity by its base unit: N, A, m.
3. Replace the newton: $1~\text{N} = 1~\text{kg m s}^{-2}$, and simplify.

**Traps:** writing T = N m A (missing the inverse); forgetting that the ampere is a base unit; mixing up $\text{kg m s}^{-2}$ (N) with $\text{kg m}^2\text{s}^{-2}$ (J).

**Method 8: Top-pan balance / lifting-wire problems**

1. For the wire to just lift off: the magnetic force equals the wire's weight, $BIL = mg$.
2. For a balance reading change: the magnetic force on the wire is $F = \Delta m \cdot g$ (the balance measures the reaction force, which changes by the magnetic force).
3. Work out the direction from the left-hand rule, then decide whether the reading increases or decreases.

**Traps:** ignoring the direction of the force when deciding if the balance reading goes up or down; using the wire's total length when only part of it is in the field; forgetting $g$ when converting mass to force.

## 5. Solved Examples

Real exam-style questions from the end of Chapter 26, with their mark allocations, plus the book's worked examples. The format for every example: Question / Method / Answer / What the examiner wants.

### Example 1: When is there a force? - End-of-chapter Q1, [1] + [1] marks

**Question:** A current-carrying wire is placed in a uniform magnetic field. **a** When does the wire experience no force due to the magnetic field? **b** When does the wire experience the maximum force?

**Method:** The force depends on the angle between the current and the field. There is no force when the conductor is parallel to the field lines; the force is maximum when the conductor cuts the field at right angles.

**Answer:** **a** when the wire (current) is parallel to the magnetic field lines. **b** when the wire is at right angles (90°) to the magnetic field.

**What the examiner wants:** the phrase 'parallel to the field' for zero force and 'at right angles' / 'perpendicular' for maximum force. Saying 'when the current is at 90°' without mentioning the field loses the point - the angle is between the current direction and the field direction.

### Example 2: Scaling the force - End-of-chapter Q2, [2] + [2] + [2] marks

**Question:** A current-carrying conductor placed at right angles to a uniform magnetic field experiences a force of $4.70 \times 10^{-3}~\text{N}$. Determine the force on the wire when, separately: **a** the current is increased by a factor of 3.0; **b** the magnetic flux density is halved; **c** the length of the wire in the field is reduced to 40% of its original length.

**Method:** With the wire at right angles to the field, $F = BIL$, so $F$ is proportional to $I$, to $B$ and to $L$. Scale the original force by the appropriate factor in each part.

**Answer:**
- **a** $F = 3.0 \times 4.70 \times 10^{-3} = 1.41 \times 10^{-2}~\text{N}$.
- **b** $F = \frac{1}{2} \times 4.70 \times 10^{-3} = 2.35 \times 10^{-3}~\text{N}$.
- **c** $F = 0.40 \times 4.70 \times 10^{-3} = 1.88 \times 10^{-3}~\text{N}$.

**What the examiner wants:** proportional reasoning marks. Each part is a direct scaling of $F = BIL$ - no need to invent values of $B$, $I$ or $L$. The final force is still at right angles to the field, so $F = BIL$ (not $BIL\sin\theta$) applies throughout.

### Example 3: Force at an angle - End-of-chapter Q3, [3] + [1] marks

**Question:** A copper wire carrying a current of 1.2 A has 3.0 cm of its length placed in a uniform magnetic field, as shown in Figure 26.26. The force experienced by the wire is $3.8 \times 10^{-3}~\text{N}$ when the angle between the wire and the magnetic field is 50°. The current is downwards into the paper. **a** Calculate the magnetic field strength. **b** What is the direction of the force experienced by the wire?

**Method:**
1. The wire is at 50° to the field, so use $F = BIL\sin\theta$ rearranged: $B = \frac{F}{IL\sin\theta}$.
2. Convert: $L = 3.0~\text{cm} = 0.030~\text{m}$.
3. Substitute: $B = \frac{3.8 \times 10^{-3}}{1.2 \times 0.030 \times \sin 50°} = \frac{3.8 \times 10^{-3}}{1.2 \times 0.030 \times 0.766} = 0.138~\text{T}$.
4. Direction: Fleming's left-hand rule, with the field direction as drawn and current into the paper; the force is at right angles to both the current and the field.

**Answer:** **a** $B = 0.14~\text{T}$ (2 s.f.). **b** the force acts at right angles to the wire and to the field, in the direction given by the left-hand rule (perpendicular to the plane containing the wire and the field).

**What the examiner wants:** the $\sin\theta$ must be included (the most common error is using $F = BIL$ here); the angle used must be the angle between the wire and the field. Direction marks come from naming the left-hand rule and quoting the mutual-perpendicular property, not from guessing a compass point off the diagram.

### Example 4: Fields and forces between two strips - End-of-chapter Q4, [2] + [4] marks

**Question:** Figure 26.27 shows a view from above of two long, parallel strips of aluminium foil A and B, carrying a current. **a** On a copy of the diagram, draw the magnetic field around and between the two strips. **b** State and explain the direction of the forces caused by the current in the strips.

**Method:**
1. Each strip has concentric circular field lines around it; use the right-hand rule for the arrow direction (thumb = current, fingers = field).
2. The current is in the same direction in both strips (as in Figure 26.27), so the fields between the strips oppose and cancel; the lines outside are stronger.
3. Parallel currents attract: the force on A is towards B, and the force on B is towards A (action-reaction pair).

**Answer:** **a** concentric circles around each strip, arrows following the right-hand rule; between the strips the arrows oppose (fields cancel), outside they add. **b** the strips attract - the forces point towards each other, because parallel currents attract (or: each strip is in the other's field, and $F = BIL$ with the left-hand rule pulls them together).

**What the examiner wants:** both explanation styles are acceptable - field-line argument (fields cancel between, strengthen outside, 'elastic band' picture pushes them together) or the $BIL$ force on one wire in the other's field. The examiner specifically rewards 'parallel currents attract' stated with the direction of the force on each strip.

### Example 5: Compasses around a wire - End-of-chapter Q5, [2] + [2] + [2] marks

**Question:** Figure 26.28 shows a wire XY which carries a constant direct current. Plotting compass R, placed alongside the wire, points due north. Compass P is placed below the wire and compass Q is placed above the wire. **a** State the direction of the current in the wire. **b** State in which direction compass P points. **c** State in which direction compass Q points if the current in the wire is reversed.

**Method:**
1. Compass R points north, so the field at R (to the side of the wire) points north. Use the right-hand rule for a straight wire: thumb in the current direction, fingers curl in the field direction.
2. If the current flows upwards (from Y to X), the field circles anticlockwise viewed from above: at the east side of the wire the field points north - matching R. So the current flows from Y to X.
3. With the current up, the field at a point below the wire (P) points west; with the current reversed (now downwards), the field at a point above the wire (Q) circles clockwise viewed from above, so it points east.

**Answer:** **a** the current flows upwards, from Y to X. **b** P points west. **c** Q points east.

**What the examiner wants:** the current direction must be justified (via the right-hand rule matching compass R's north-pointing field). The compass needle always aligns with the local field direction - it points in the direction of the field at that point, which for P and Q is found by curling the fingers around the wire in the correct sense.

### Example 6: Rectangular frame in a uniform field - End-of-chapter Q6, [3] + [1] + [2] + [2] marks

**Question:** Figure 26.29 shows a rectangular metal frame PQRS (sides 4.0 cm and 7.0 cm) placed in a uniform magnetic field of flux density $4.5 \times 10^{-3}~\text{T}$. The current in the frame is 2.5 A. **a** Calculate the force experienced by side PQ of the frame. **b** Suggest why side QR does not experience a force. **c** Describe the motion of the frame immediately after the current is switched on. **d** Calculate the maximum torque (moment) exerted about an axis parallel to side PQ.

**Method:**
1. Side PQ is 4.0 cm long, at right angles to the field, so $F = BIL$: $F = 4.5 \times 10^{-3} \times 2.5 \times 0.040 = 4.5 \times 10^{-4}~\text{N}$.
2. Side QR carries its current parallel to the magnetic field lines, so $\sin\theta = 0$ and there is no force.
3. The force on PQ is opposite to the force on RS (equal and opposite, forming a couple), so the frame rotates about an axis through the other two sides.
4. Maximum torque about an axis parallel to PQ: only the force on RS acts about this axis (PQ lies on the axis). $F = BIL = 4.5 \times 10^{-4}~\text{N}$, separation = 7.0 cm, so torque $= F \times d = 4.5 \times 10^{-4} \times 0.070 = 3.2 \times 10^{-5}~\text{N m}$.

**Answer:** **a** $F = 4.5 \times 10^{-4}~\text{N}$. **b** because side QR is parallel to the magnetic field (the current in it is parallel to the field lines), so there is no force on it. **c** the frame rotates (about an axis parallel to QR / through the centres of PQ and RS) because the forces on PQ and RS form a couple. **d** maximum torque $= 3.2 \times 10^{-5}~\text{N m}$.

**What the examiner wants:** the length used in part (a) is the side in the field at right angles to it (4.0 cm, not 7.0 cm). Part (b) rewards the word 'parallel' - 'no force because the current is parallel to the field'. Part (d) wants torque = force on the far side $\times$ perpendicular distance between the sides; the force on PQ itself contributes nothing about an axis through PQ.

### Example 7: Current balance with a paper tape - End-of-chapter Q7, [1] + [2] + [3] + [1] marks

**Question:** Figure 26.30 shows a current-carrying wire frame placed between a pair of Magnadur magnets on a yoke; a pointer is attached to the wire. A current of 8.5 A in the wire causes the pointer to move vertically upwards. A small paper tape attached to the pointer brings it back to its initial position; the paper's mass is 60 mg. The section of the wire between the poles has a length of 5.2 cm. **a** State the direction of the magnetic field. **b** Calculate the force on the wire due to the magnetic field when it carries a current of 8.5 A. **c** Calculate the magnetic flux density between the poles. **d** Describe what happens to the frame if low-frequency alternating current passes through the wire.

**Method:**
1. The field is between the N and S poles of the magnets, so it is horizontal, at right angles to the wire, running from the north pole to the south pole.
2. The magnetic force on the wire equals the weight of the paper tape: $F = mg = 60 \times 10^{-6} \times 9.81 = 5.9 \times 10^{-4}~\text{N}$.
3. $B = \frac{F}{IL} = \frac{5.9 \times 10^{-4}}{8.5 \times 0.052} = 1.33 \times 10^{-3}~\text{T}$.
4. With alternating current, the direction of the force reverses every half-cycle, so the pointer vibrates up and down at the supply frequency (twice per cycle the force changes direction - net effect: oscillation about the initial position).

**Answer:** **a** horizontal, from the north pole to the south pole (at right angles to the wire). **b** $F = 5.9 \times 10^{-4}~\text{N}$. **c** $B = 1.3 \times 10^{-3}~\text{T}$ (2 s.f.). **d** the pointer oscillates up and down (vibrates) as the force on the wire alternates in direction.

**What the examiner wants:** part (b) is a Newton's-third-law balance: the tape's weight exactly balances the magnetic force, so $F = mg$. Part (c) needs the length in the field (5.2 cm, not the whole frame). Part (d): the force alternates direction with the current, so the wire vibrates at the a.c. frequency - a steady deflection is not possible with a.c.

### Example 8: Demonstrating $F \propto I$, and a lifting wire - End-of-chapter Q8, [5] + [1] + [3] marks

**Question:** **a** The size of the force acting on a wire carrying a current in a magnetic field is proportional to the size of the current. With the aid of a diagram, describe how this can be demonstrated in a school laboratory. **b** At a certain point on the Earth's surface the horizontal component of the Earth's magnetic field is $1.6 \times 10^{-5}~\text{T}$. A piece of wire 3.0 m long and of weight 0.020 N lies in an east-west direction on a laboratory bench. When a large current flows in the wire, the wire just lifts off the surface of the bench. **i** State the direction of the current in the wire. **ii** Calculate the minimum current needed to lift the wire from the bench.

**Method:**
1. **a** Set up a wire (or a section of it) at right angles to the field between the poles of a strong magnet, with the magnet on a top-pan balance. Connect the wire, an ammeter and a variable resistor in series with a power supply. Vary the current, and for each value record the current and the change in the balance reading (which gives the force via $F = mg$). Plot force against current: a straight line through the origin shows $F \propto I$.
2. **b i** For the wire to lift, the magnetic force must act upwards, against the weight. With the field pointing north (horizontal component) and the force upwards, the left-hand rule gives: First finger = Field (north), thuMb = Motion (up), so the seCond finger points east - the current flows from west to east (towards the east). (Cross-product check: $F = IL \times B$, with east $\times$ north $=$ up, confirms it.)

3. **b ii** Just lifting off means the magnetic force equals the weight: $BIL = mg$, so $I = \frac{mg}{BL} = \frac{0.020}{1.6 \times 10^{-5} \times 3.0} = \frac{0.020}{4.8 \times 10^{-5}} = 4.2 \times 10^{2}~\text{A}$.

**Answer:** **a** (description as Method 1; diagram showing magnet on top-pan balance, wire through the field, ammeter and variable resistor in series; straight-line graph of $F$ against $I$ through the origin). **b i** the current flows from west to east (eastwards). **b ii** $I = 4.2 \times 10^{2}~\text{A}$ (420 A).

**What the examiner wants:** part (a) is a 5-mark practical: named apparatus (top-pan balance or current balance, ammeter, rheostat/variable resistor), the wire at right angles to the field, force found from the balance reading, repeated readings, and the straight-line-through-origin conclusion. Part (b) needs the cross-product/left-hand logic spelled out (field north + force up $\Rightarrow$ current east), and the calculation uses the FULL 3.0 m of wire in the field.

### Example 9: Top-pan balance and the magnets - End-of-chapter Q9, [2] + [2] + [2] + [2] marks

**Question:** Figure 26.31 shows a fixed horizontal wire passing centrally between the poles of a permanent magnet placed on a top-pan balance. With no current, the balance records 102.45 g. When a current of 4.0 A flows in the wire, the balance records 101.06 g. **a** Explain why the reading decreases when the current is switched on. **b** State and explain the direction of the current flow in the wire. **c** The length of the wire in the magnetic field is 5.0 cm. Calculate the average magnetic flux density between the poles. **d** Sketch a graph, with balance reading on the vertical axis and current on the horizontal axis, to show how the balance reading changes when the current is altered.

**Method:**
1. The wire is fixed. The magnetic force on the wire is downwards; by Newton's third law the magnets experience an equal force upwards, so the force on the balance decreases - the reading falls by the magnetic force.
2. Field direction: from the N pole to the S pole (horizontal, left to right in the figure). Force on the wire: downwards. Left-hand rule (First finger = field, thuMb = motion of the wire = down): the seCond finger points into the paper, so the current flows downwards into the paper.
3. The decrease in balance reading corresponds to the magnetic force: $\Delta m = 102.45 - 101.06 = 1.39~\text{g} = 1.39 \times 10^{-3}~\text{kg}$. $F = \Delta m \cdot g = 1.39 \times 10^{-3} \times 9.81 = 1.36 \times 10^{-2}~\text{N}$. Then $B = \frac{F}{IL} = \frac{1.36 \times 10^{-2}}{4.0 \times 0.050} = 0.068~\text{T}$.
4. Graph: a straight line starting at 102.45 g at $I = 0$ and falling linearly as $I$ increases (force $\propto$ current). (For reversed current the line rises instead.)

**Answer:** **a** the wire experiences a downward magnetic force, so (Newton's third law) the magnets are pushed upwards, reducing the force on the balance. **b** current flows downwards into the paper (left-hand rule: field left-to-right, force on wire downwards). **c** $B = 0.068~\text{T}$. **d** straight line of negative slope through (0, 102.45 g) - the reading decreases linearly with current.

**What the examiner wants:** part (a) must mention Newton's third law (action-reaction between wire and magnets) - 'the wire pushes the magnet up' alone loses the mark. Part (b) wants the left-hand rule applied with both field and force directions stated. Part (c) is the standard $\Delta m g / IL$ route; part (d) wants a straight line (linear proportionality), not a curve.

### Example 10: Definition, stacked wires, force per unit length - End-of-chapter Q10, [3] + [4] + [3] marks

**Question:** **a** Define magnetic flux density and explain the similarity with the definition of electric field strength. **b** Two thin horizontal wires are placed in a north-south direction, one on a bench, the other held 3.0 cm directly above the first. **i** When equal currents flow in the two wires, the force exerted on the bench by the lower wire decreases. Explain why, and say what you can about the directions of the currents. **ii** The magnetic flux density $B$ at a distance $x$ from a long straight wire carrying current $I$ is $B = 2.0 \times 10^{-7}\frac{I}{x}$. When the current in each wire is 4.0 A, calculate the force per unit length on one wire due to the current in the other.

**Method:**
1. **a** Magnetic flux density at a point: the force per unit length on a long straight conductor carrying unit current placed at right angles to the field at that point. Electric field strength is force per unit positive charge - both are defined as force per unit 'test' quantity, measured by a test object at the point.
2. **b i** The lower wire presses on the bench less hard, so it feels a net upward magnetic force; the force between the wires is therefore attractive, which happens when the currents are in the same direction (parallel currents attract).
3. **b ii** Field of one wire at the other: $B = 2.0 \times 10^{-7} \times \frac{4.0}{0.030} = 2.67 \times 10^{-5}~\text{T}$. Force per unit length on the other wire: $\frac{F}{L} = BI = 2.67 \times 10^{-5} \times 4.0 = 1.07 \times 10^{-4}~\text{N m}^{-1}$.

**Answer:** **a** definition as in the Definition Sheet; similarity - both fields are defined as force per unit quantity (per unit charge for $E$, per unit current per unit length for $B$) on a test object placed at the point. **b i** the magnetic force between the wires is upward on the lower wire (attractive), so the currents flow in the same direction. **b ii** $\frac{F}{L} = 1.1 \times 10^{-4}~\text{N m}^{-1}$ (2 s.f.).

**What the examiner wants:** the definition must say 'force per unit length' and 'unit current' and 'at right angles' - missing any of the three costs a mark. The similarity mark is for 'force per unit (test) quantity' phrasing. Part (b i) links the reduced bench force to an upward magnetic force on the lower wire, hence attraction, hence same-direction currents. Part (b ii) uses $x = 3.0~\text{cm} = 0.030~\text{m}$ and the force-per-unit-length form - a common slip is using $x$ in cm.

---

# Chapter 27: Charged Particles
> Source: `physics/notes/chapter-27-charged-particles-notes.md`

## 4. Methods (Question Types & Methods)

These are the ways Cambridge has actually asked about charged particles. Each method below is what a full-mark answer looks like.

### 1. Force on a moving charge ($F = BQv\sin\theta$)

**Method:**
1. Check the angle between the velocity and the field. At right angles, $\sin\theta = 1$ and $F = BQv$.
2. Convert $B$ to tesla (mT to T: $\times 10^{-3}$) and $v$ to m s$^{-1}$.
3. For an electron use $Q = e = 1.60 \times 10^{-19}~\text{C}$; for a helium nucleus $Q = 2e = 3.2 \times 10^{-19}~\text{C}$.
4. Substitute and quote $F$ in newtons.

**Traps:** forgetting the $\sin\theta$ when the motion is not perpendicular; leaving $B$ in mT; using the electron mass instead of the proton mass in $F = BQv$ (mass is not needed at all for the force); confusing $Q$ with the number of charges.

### 2. Direction of the force (Fleming's left-hand rule / right-hand palm rule)

**Method:**
1. Identify the charge sign. Positive charge: conventional current is in the direction of motion. Negative charge (electron): conventional current is opposite to the motion.
2. Left hand: first finger along $B$, second finger along the conventional current, thumb gives the force.
3. Alternative for a positive charge: right-hand palm rule (fingers along $v$, field into palm, thumb gives $F$). For an electron, use the left hand or flip the answer.
4. Check the force is perpendicular to both $B$ and $v$ - if your answer is not, you have misapplied the rule.

**Traps:** using the electron motion as the current direction (the #1 direction error); using the right hand for electrons; forgetting that reversing $B$ or reversing the charge sign reverses the force.

### 3. Circular orbit radius ($r = \frac{mv}{BQ}$, $p = BQr$)

**Method:**
1. State that the magnetic force provides the centripetal force: $\frac{mv^2}{r} = BQv$.
2. Rearrange to $r = \frac{mv}{BQ}$.
3. Convert everything to SI ($B$ in T, $r$ in m, masses as given).
4. Use $r \propto v$, $r \propto m$, $r \propto \frac{1}{B}$ for the qualitative "what happens if..." parts.
5. Sanity-check the magnitude: electron orbits are centimetres to millimetres; proton orbits in Earth-scale fields can be hundreds of metres.

**Traps:** cancelling $v$ wrongly (leaving $r = \frac{m}{BQ}$ without the $v$); using diameter where radius is needed; mixing up which particle's mass to use; not realising the field changes only direction, so $v$ stays constant.

### 4. Speed of electrons from an accelerating p.d. ($eV = \frac{1}{2}mv^2$)

**Method:**
1. Write the energy equation: work done $eV$ becomes kinetic energy $\frac{1}{2}mv^2$.
2. Convert the p.d. to volts (kV to V: $\times 10^3$).
3. Solve: $v = \sqrt{\frac{2eV}{m}}$, or use the given $\frac{e}{m}$ directly: $v = \sqrt{2\left(\frac{e}{m}\right)V}$.
4. Quote $v$ in m s$^{-1}$; electron speeds from kilovolt tubes are of order $10^7~\text{m s}^{-1}$.

**Traps:** leaving the p.d. in kV; using $eV$ but forgetting the $\frac{1}{2}$; using the wrong mass (the electron mass is $9.11 \times 10^{-31}~\text{kg}$, about 1836 times lighter than a proton); not linking this equation to the orbit equation when finding $\frac{e}{m}$.

### 5. Charge-to-mass ratio ($\frac{e}{m_e}$) from deflection

**Method:**
1. Measure the accelerating p.d. $V_{ca}$ (gives the speed via $eV_{ca} = \frac{1}{2}m_ev^2$).
2. Measure the orbit radius $r$ in a known field $B$.
3. Eliminate $v$: $\frac{e}{m_e} = \frac{v}{Br} = \frac{2V_{ca}}{B^2r^2}$.
4. Alternatively, in a velocity-selector arrangement, measure $E$ and $B$ that balance (beam straight), giving $v = \frac{E}{B}$, then use $r = \frac{mv}{Be}$.
5. Combine with Millikan's $e$ to get $m_e = \frac{e}{e/m_e}$.

**Traps:** substituting the plate p.d. instead of the accelerating p.d.; forgetting to square both $B$ and $r$; unit errors with kV and mT; saying Thomson measured $e$ or $m_e$ directly (he measured only the ratio).

### 6. Velocity selector ($v = \frac{E}{B}$)

**Method:**
1. Balance the forces: $Eq = Bqv$, cancel $q$.
2. $v = \frac{E}{B}$. If given plate p.d. and separation, use $E = \frac{V}{d}$ so $v = \frac{V}{Bd}$.
3. Faster particles: magnetic force wins (it grows with $v$), deflected one way. Slower: electric force wins, deflected the other way.
4. State that gravity is negligible.

**Traps:** forgetting $q$ cancels (selected speed independent of charge and mass); swapping $E$ and $B$; not converting $d$ to metres; saying "all particles pass" instead of "only particles at $v = \frac{E}{B}$".

### 7. Electric vs magnetic deflection (path shapes)

**Method:**
1. Electric field: constant force $EQ$; constant acceleration; parabolic path between the plates; straight line outside. Faster electrons are deflected less (less time in the field).
2. Magnetic field: force $BQv$ perpendicular to velocity; circular arc inside the field; straight line outside. Force does no work; speed unchanged.
3. When drawing paths, start the curve where the field region begins and draw a straight line after the particle leaves the region.
4. For a charged particle deflected by an electric field, remember its charge-to-mass ratio determines the acceleration: $a = \frac{EQ}{m}$.

**Traps:** drawing the curve starting before the field region or continuing to curve outside it (a very common examiner-report criticism); forgetting the helium nucleus is charged (it is $+2e$); mixing up "deflected less" for fast particles between the two fields; saying a magnetic field speeds a particle up or slows it down.

### 8. Hall voltage calculation ($V_H = \frac{BI}{ntq}$)

**Method:**
1. Convert $t$ (the thickness) to metres: mm to m is $\times 10^{-3}$; $\mu$m to m is $\times 10^{-6}$.
2. Convert $I$ to amperes and $B$ to tesla.
3. Substitute into $V_H = \frac{BI}{ntq}$, with $q = e = 1.60 \times 10^{-19}~\text{C}$ for electrons.
4. Check the magnitude: semiconductor probes in tesla-strength fields give millivolt-level Hall voltages.
5. Cross-check with the equilibrium form $V_H = Bvd$.

**Traps:** using the width $d$ instead of the thickness $t$ (the width cancels in the derivation - the single most common Hall-effect error); leaving $t$ in mm; using $I$ in mA; dividing by $n$ instead of multiplying by it in the rearrangement for $B$.

### 9. Hall probe: measuring $B$ and identifying charge carriers

**Method:**
1. Fixed current, fixed slice: $V_H \propto B$, so calibrate the meter in known fields and read $B$ directly.
2. Orient the slice perpendicular to the field (the probe measures the component of $B$ perpendicular to the slice: $V_H = V_{\text{max}}\cos\theta$). Rotate the probe to find the maximum reading for an unknown field direction.
3. Sign of carriers: note which face goes negative and apply the left-hand rule to the carrier motion; electrons and positive holes give opposite signs of $V_H$.
4. Explain the design: semiconductor because $n$ is small (and drift velocity large for the same current); thin slice because $V_H \propto \frac{1}{t}$; steady current because the calibration assumes $I$ fixed.

**Traps:** forgetting the probe must be perpendicular to the field; saying "metal" when the probe uses semiconductor (and why); saying $V_H$ depends on the width; missing the constant-current reason in "why must the current be maintained constant?".

### 10. Explanations: why the speed stays constant / why the beam stays tight

**Method:**
1. Speed constant in a magnetic field: the force is always perpendicular to the velocity, so work done $= Fs\cos 90^{\circ} = 0$, kinetic energy unchanged, only the direction changes. Give the whole chain: force perpendicular, no work, no change in KE, speed constant.
2. Tight beam in Thomson's tube: all the particles must have the same mass, charge and speed, because the deflection depends on all three ($a = \frac{EQ}{m}$ for electric, $r = \frac{mv}{BQ}$ for magnetic) - a spread in any of them would smear the beam.
3. Radius decreasing (spiral): the particle loses speed (collisions, ionisation of the gas), and $r = \frac{mv}{BQ} \propto v$, so the orbit tightens.

**Traps:** saying "the magnetic field does work" or "the force slows the electron" (wrong - the force is perpendicular, it does no work); explaining the tight beam with only one of mass/charge/speed; missing the link $r \propto v$ in spiral questions.

### 11. Drift velocity and current ($I = nAqv$)

**Method:**
1. Rearrange $I = nAqv$ for the drift velocity: $v = \frac{I}{nAq}$.
2. Cross-sectional area for a strip: $A = d \times t$ (width times thickness) - use the face perpendicular to the current.
3. Convert the strip dimensions to metres.
4. Use this $v$ in $V_H = Bvd$ as a cross-check on a Hall calculation.

**Traps:** using the wrong face for $A$; mixing up $d$ and $t$; forgetting that in a metal the carriers are electrons ($q = e$); not converting mm to m.

### 12. Definitions (frequent 2-mark questions)

**Method:**
1. **Specific charge:** "charge per unit mass", $\frac{Q}{m}$ in C kg$^{-1}$.
2. **Hall effect:** charge carriers pushed sideways by the magnetic force, producing a p.d. across the conductor.
3. **Velocity selector:** crossed fields where $Eq = Bqv$, so only speed $v = \frac{E}{B}$ passes undeflected.
4. **Why the magnetic force does not change speed:** force at right angles to velocity, so no work is done.

**Traps:** writing formulas without the words (the equation alone usually earns only 1 of the 2 marks); omitting "per unit mass" from specific charge; omitting "perpendicular" from the no-work explanation.

## 5. Solved Examples

Real exam-style questions from the end of Chapter 27, with their mark allocations. The format for every example: Question / Method / Answer / What the examiner wants. Total: 76 marks across the ten questions.

### Example 1: Why the magnetic force does not change the electron's speed - End-of-chapter Q1, 3 marks

**Question:** The magnetic force $BQv$ causes an electron to travel in a circle in a uniform magnetic field. Explain why this force does not cause an increase in the speed of the electron. [3]

**Method:**
1. The magnetic force is always at right angles (perpendicular) to the velocity of the electron.
2. Work done is $W = Fs\cos\theta$ with $\theta = 90^{\circ}$, so the force does no work on the electron.
3. No work means no change in kinetic energy, so the speed stays constant - only the direction of motion changes.

**Answer:** The force is perpendicular to the velocity, does no work, so kinetic energy and speed are unchanged.

**What the examiner wants:** 1 mark for "force perpendicular to velocity", 1 for "no work done", 1 for "kinetic energy/speed unchanged". The phrase "at right angles to the motion" plus "so it does no work" is the full answer; "it is a centripetal force" alone earns only the first mark.

### Example 2: Specific charge of the electron from deflection - End-of-chapter Q2, 4 marks

**Question:** An electron beam is produced from an electron gun in which each electron is accelerated through a p.d. of $1.6~\text{kV}$. When these electrons pass at right angles through a magnetic field of flux density $8.0~\text{mT}$, the radius of curvature of the electron beam is $0.017~\text{m}$. Determine the specific charge of the electron, $\frac{e}{m_e}$. [4]

**Method:**
1. Convert: $V_{ca} = 1.6~\text{kV} = 1600~\text{V}$; $B = 8.0~\text{mT} = 8.0 \times 10^{-3}~\text{T}$.
2. Energy gained: $eV_{ca} = \frac{1}{2}m_ev^2$.
3. Orbit in the magnetic field: $r = \frac{mv}{Be}$.
4. Eliminate $v$: $\frac{e}{m_e} = \frac{2V_{ca}}{B^2r^2}$.
5. $\frac{e}{m_e} = \frac{2 \times 1600}{(8.0 \times 10^{-3})^2 \times (0.017)^2} = \frac{3200}{6.4 \times 10^{-5} \times 2.89 \times 10^{-4}} = \frac{3200}{1.85 \times 10^{-8}}$.

**Answer:** $\frac{e}{m_e} = 1.73 \times 10^{11}~\text{C kg}^{-1}$ (consistent with the accepted value $1.76 \times 10^{11}~\text{C kg}^{-1}$).

**What the examiner wants:** 4 marks: the energy equation (1), the orbit equation (1), eliminating $v$ correctly (1), substitution with converted units and answer with units (1). The classic slips: leaving $V$ in kV and $B$ in mT, or forgetting to square $B$ and $r$.

### Example 3: Alpha and beta particles compared - End-of-chapter Q3, 8 marks

**Question:** An $\alpha$-particle (helium nucleus, mass $4$ times the proton mass, charge $+2e$) and a $\beta$-particle (electron, mass about $\frac{1}{1836}$ of the proton mass, charge $-e$) travel through a uniform magnetic field with the same velocity, at right angles to the field. Determine the ratio of (a) the masses, (b) the charges, (c) the magnetic forces, (d) the radii of the circular orbits of the two particles. [2 each]

**Method:**
1. (a) $m_\alpha = 4 \times m_p$ and $m_\beta = \frac{m_p}{1836}$, so $\frac{m_\alpha}{m_\beta} = 4 \times 1836 = 7344 \approx 7.3 \times 10^3$.
2. (b) $\frac{Q_\alpha}{Q_\beta} = \frac{2e}{e} = 2$ (magnitudes of charge).
3. (c) $F = BQv$ with the same $B$ and $v$: $\frac{F_\alpha}{F_\beta} = \frac{Q_\alpha}{Q_\beta} = 2$.
4. (d) $r = \frac{mv}{BQ}$: $\frac{r_\alpha}{r_\beta} = \frac{m_\alpha}{m_\beta} \times \frac{Q_\beta}{Q_\alpha} = \frac{7344}{2} = 3672 \approx 3.7 \times 10^3$.

**Answer:** (a) $m_\alpha : m_\beta = 7.3 \times 10^3 : 1$; (b) $2 : 1$; (c) $2 : 1$; (d) $r_\alpha : r_\beta = 3.7 \times 10^3 : 1$ (the $\alpha$-particle curves far less tightly).

**What the examiner wants:** each part: 1 mark for the ratio setup and 1 for the arithmetic. Part (c) needs the insight that $F \propto Q$ (the velocity cancels); part (d) combines both ratios. The $\alpha$-particle's radius is about 3700 times the electron's because it is far more massive but only twice as charged.

### Example 4: Two differences between electric and magnetic forces - End-of-chapter Q4, 2 marks

**Question:** A moving charged particle experiences a force in an electric field and also in a magnetic field. State **two** differences between the forces experienced in the two types of field. [2]

**Method:**
1. The electric force acts on a charge whether it is moving or stationary; the magnetic force acts only on a **moving** charge.
2. The electric force can do work and change the speed (kinetic energy) of the particle; the magnetic force is always perpendicular to the velocity, does no work, and never changes the speed.
3. (Alternative third difference, pick any two) The electric force acts along the direction of the field; the magnetic force is perpendicular to both the field and the velocity. The electric force on a given charge is independent of its speed; the magnetic force is proportional to its speed.

**Answer:** Any two of: (1) magnetic force acts only on moving charges, electric force on stationary ones too; (2) magnetic force does no work and cannot change speed, electric force can; (3) electric force along the field, magnetic force perpendicular to field and velocity.

**What the examiner wants:** 1 mark per valid difference, clearly contrasted. "Magnetic is weaker" or "electric is stronger" earns nothing - the differences must be physical properties, not magnitudes.

### Example 5: The spiralling electron in air - End-of-chapter Q5, 8 marks

**Question:** An electron travels in air, rotating clockwise around a uniform magnetic field directed into the plane of the paper; the radius of the orbit gradually decreases. (a)(i) Explain the origin of the force that causes the electron to spiral. [2] (a)(ii) Explain why the radius gradually decreases. [2] (b) At one point the electron's speed is $1.0 \times 10^7~\text{m s}^{-1}$ and the flux density is $0.25~\text{T}$. Calculate (i) the magnetic force on the electron [2] and (ii) the radius of the path. [2]

**Method:**
1. (a)(i) The electron is moving in a magnetic field, so it experiences a force $F = Bev$ perpendicular to its velocity (direction from Fleming's left-hand rule, remembering the conventional current is opposite to the electron's motion); this force acts as the centripetal force towards the centre of the circle.
2. (a)(ii) The electron ionises air molecules and loses kinetic energy, so its speed falls; since $r = \frac{mv}{Be} \propto v$, a smaller speed means a smaller radius and the orbit tightens into a spiral.
3. (b)(i) $F = Bev = 1.60 \times 10^{-19} \times 1.0 \times 10^7 \times 0.25 = 4.0 \times 10^{-13}~\text{N}$.
4. (b)(ii) $r = \frac{mv}{Be} = \frac{9.11 \times 10^{-31} \times 1.0 \times 10^7}{1.60 \times 10^{-19} \times 0.25} = \frac{9.11 \times 10^{-24}}{4.0 \times 10^{-20}} = 2.28 \times 10^{-4}~\text{m}$.

**Answer:** (a)(i) magnetic force $Bev$ perpendicular to the velocity, acting as centripetal force; (a)(ii) speed falls as the electron ionises air molecules, and $r \propto v$; (b)(i) $F = 4.0 \times 10^{-13}~\text{N}$; (b)(ii) $r = 2.3 \times 10^{-4}~\text{m}$.

**What the examiner wants:** (a)(i) 2 marks for the force idea plus perpendicular/centripetal; (a)(ii) 2 marks for the energy loss (collisions with air/gas) AND the link $r \propto v$ - losing the link loses a mark. (b) 2 marks each for correct substitution with units; the magnetic force must NOT be said to do the slowing (it does no work - the gas collisions do).

### Example 6: Deflecting a proton beam to a detector - End-of-chapter Q6, 9 marks

**Question:** Protons travel from a source to a detector through a region of uniform magnetic field (Figure 27.16). (a)(i) Copy the diagram, sketch the proton's path, and draw arrows at two points on the path showing the direction of the magnetic force. [3] (a)(ii) State the direction of the magnetic field within the area shown. [1] (b) The proton's speed is $4.0 \times 10^6~\text{m s}^{-1}$ and the flux density is $0.25~\text{T}$. Calculate (i) the magnitude of the magnetic force [1] and (ii) the radius of curvature of the path. [2] (c) State two changes to the magnetic field that would allow an electron with the same speed to be deflected along the same path. [2]

**Method:**
1. (a)(i) The path is an arc of a circle inside the field region (the force is perpendicular to the velocity), with straight lines before entering and after leaving the region; at every point the force arrow points towards the centre of the arc.
2. (a)(ii) Use Fleming's left-hand rule with the proton's motion as the conventional current direction: for the geometry in the coursebook figure (protons deflected downwards towards the detector), the field must be directed out of the plane of the paper. If your diagram has the detector above the beam line, the field is into the page - the method is what earns the mark, and the rule must be applied to your own sketch.
3. (b)(i) $F = BQv = 0.25 \times 1.60 \times 10^{-19} \times 4.0 \times 10^6 = 1.6 \times 10^{-13}~\text{N}$.
4. (b)(ii) $r = \frac{mv}{BQ} = \frac{1.67 \times 10^{-27} \times 4.0 \times 10^6}{0.25 \times 1.60 \times 10^{-19}} = \frac{6.68 \times 10^{-21}}{4.0 \times 10^{-20}} = 0.167~\text{m}$.
5. (c) The electron has the same charge magnitude but a mass about 1836 times smaller, so at the same speed $r = \frac{mv}{BQ}$ would be 1836 times smaller. To make the electron follow the proton's path: reverse the direction of the magnetic field (the electron is negative, so the force direction flips), and reduce the flux density by the factor $1836$: $B = \frac{0.25}{1836} = 1.4 \times 10^{-4}~\text{T}$.

**Answer:** (a)(ii) out of the plane of the paper for the coursebook geometry (into the page if the detector lies above the beam line - apply the rule to your diagram); (b)(i) $F = 1.6 \times 10^{-13}~\text{N}$; (b)(ii) $r = 0.17~\text{m}$; (c) reverse the field direction and reduce $B$ by a factor of about 1836 (to $\approx 1.4 \times 10^{-4}~\text{T}$).

**What the examiner wants:** (a)(i) 3 marks for the arc inside the region only (1), straight lines outside (1), force arrows (1). (b)(i) 1 mark substitution; (b)(ii) 2 marks for $r = \frac{mv}{BQ}$ with the proton mass. (c) 2 marks: reverse the field for the negative charge AND scale $B$ down by $m_e/m_p$ - both changes needed.

### Example 7: Charge separation in a semiconductor strip - End-of-chapter Q7, 11 marks

**Question:** A thin strip of semiconductor carries a current in a magnetic field at right angles to the current (Figure 27.17). (a) Explain why the charges separate. [3] (b)(i) Add $+$ and $-$ signs to the diagram to show the charge separation. [1] (b)(ii) Explain how an electron is able to move in a straight line along the strip. [1] (c) The Hall voltage is measured with the same slice, current and field at two temperatures, one significantly higher. Describe and explain the changes in the number density, the drift velocity of the carriers, and the Hall voltage. [6]

**Method:**
1. (a) The electrons (charge carriers) drift along the strip with velocity $v$, so each experiences a magnetic force $Bev$ sideways (perpendicular to both the current and the field, from Fleming's left-hand rule). They are pushed towards one side of the strip and accumulate there, leaving the opposite side short of electrons (positive). This separation is the Hall effect.
2. (b)(i) For the standard figure layout (current to the right, field into the page): electrons are pushed to the top face, so mark the top face $-$ and the bottom face $+$. Apply the left-hand rule to your own diagram: conventional current opposite to the electron flow.
3. (b)(ii) The separated charges set up an electric field across the strip; when equilibrium is reached, the electric force $eE$ on each electron is equal and opposite to the magnetic force $Bev$, so the resultant sideways force is zero and the electron continues straight along the strip.
4. (c) Higher temperature: more electrons are promoted into the conduction band, so the number density $n$ increases. With the current fixed, $I = nAqv$ means the drift velocity $v$ decreases (larger $n$ at the same $I$ and $A$). Since $V_H = \frac{BI}{ntq}$, the larger $n$ makes the Hall voltage decrease.

**Answer:** (a) magnetic force $Bev$ pushes drifting electrons sideways, so charge accumulates on the sides; (b)(i) top $-$ and bottom $+$ for the standard layout (use the left-hand rule for your diagram); (b)(ii) electric force balances magnetic force at equilibrium, so the electron travels straight; (c) $n$ increases, $v$ decreases, $V_H$ decreases.

**What the examiner wants:** (a) 3 marks for the magnetic force idea (1), sideways direction (1), accumulation/separation (1). (b)(ii) 1 mark for the balanced forces idea. (c) 6 marks: 2 each for $n$, $v$, $V_H$ with the reasoning linking each change (temperature raises $n$; $I = nAqv$ then lowers $v$; $V_H = \frac{BI}{ntq}$ then falls). Saying only "it gets hotter" without the chain earns nothing.

### Example 8: The electron tube with crossed fields - End-of-chapter Q8, 10 marks

**Question:** Electrons emitted from a cathode accelerate towards an anode at $+1.0~\text{kV}$ and pass into a uniform electric field between parallel plates at $+500~\text{V}$ and $0~\text{V}$, $5.0~\text{cm}$ apart (Figure 27.18). The beam curves upwards. (a)(i) Explain why. [2] (a)(ii) Explain how the pattern on the fluorescent screen shows that all the electrons have the same speed as they leave the anode. [2] (b) Write an equation relating the electron speed $v$ to the anode-cathode p.d. $V_{ac}$. [1] (c)(i) State the direction of the magnetic field that cancels the upward deflection. [1] (c)(ii) Write an equation relating $v$, the electric field $E$ and the flux density $B$ for undeflected passage. [2] (c)(iii) Calculate $B$, given $\frac{e}{m_e} = 1.76 \times 10^{11}~\text{C kg}^{-1}$. [2]

**Method:**
1. (a)(i) The electric field between the plates points from the $+500~\text{V}$ plate to the $0~\text{V}$ plate, i.e. downwards. The electron is negative, so it feels a force opposite to the field direction, i.e. upwards; this constant force deflects the beam upwards in a curve.
2. (a)(ii) The upward deflection depends on how long each electron spends between the plates, which depends on its speed: faster electrons are deflected less. A single sharp spot (rather than a smeared or elongated one) means all the electrons are deflected by the same amount, so they all have the same speed.
3. (b) $eV_{ac} = \frac{1}{2}m_ev^2$, so $v = \sqrt{\frac{2eV_{ac}}{m_e}}$.
4. (c)(i) The magnetic force must act downwards to cancel the upward electric force. Electrons move rightwards (conventional current leftwards), so for the force to be downwards the field must be directed **into the plane of the paper** (left-hand rule).
5. (c)(ii) Balance the forces: $eE = Bev$, so $v = \frac{E}{B}$, with $E = \frac{V}{d}$ between the plates.
6. (c)(iii) $v = \sqrt{2\left(\frac{e}{m_e}\right)V_{ac}} = \sqrt{2 \times 1.76 \times 10^{11} \times 1000} = \sqrt{3.52 \times 10^{14}} = 1.876 \times 10^7~\text{m s}^{-1}$.
7. $E = \frac{V}{d} = \frac{500}{0.05} = 1.0 \times 10^4~\text{V m}^{-1}$.
8. $B = \frac{E}{v} = \frac{1.0 \times 10^4}{1.876 \times 10^7} = 5.33 \times 10^{-4}~\text{T}$.

**Answer:** (a)(i) negative electron pushed opposite to the downward field; (a)(ii) single sharp spot = same deflection = same speed; (b) $eV_{ac} = \frac{1}{2}m_ev^2$; (c)(i) into the plane of the paper; (c)(ii) $v = \frac{E}{B}$; (c)(iii) $B = 5.3 \times 10^{-4}~\text{T}$.

**What the examiner wants:** (a)(i) 2 marks: field direction between the plates (1) and force on a negative charge opposite to the field (1). (a)(ii) 2 marks: deflection depends on speed (1) and the sharp spot proves a single speed (1). (b) 1 mark for the energy equation. (c)(i) 1 mark for into the page. (c)(ii) 2 marks for equating $eE$ and $Bev$. (c)(iii) 2 marks for the two substitutions: $v$ from the accelerating p.d. (1) and $B = E/v$ with converted units (1).

### Example 9: Protons and helium nuclei at the Earth's poles - End-of-chapter Q9, 5 marks

**Question:** Protons and helium nuclei from the Sun enter the Earth's atmosphere above the poles, where the flux density is $6.0 \times 10^{-5}~\text{T}$. They move at $1.0 \times 10^6~\text{m s}^{-1}$ at right angles to the field. (a) Calculate the radius of the path of a proton. [3] (b) Draw a diagram showing the deflection of a proton and of a helium nucleus with the same initial velocity, stating each radius on the diagram. [2] (Mass of helium nucleus $= 6.8 \times 10^{-27}~\text{kg}$; charge on helium nucleus $= 3.2 \times 10^{-19}~\text{C}$; proton mass $= 1.67 \times 10^{-27}~\text{kg}$.)

**Method:**
1. (a) $r = \frac{mv}{BQ} = \frac{1.67 \times 10^{-27} \times 1.0 \times 10^6}{6.0 \times 10^{-5} \times 1.60 \times 10^{-19}} = \frac{1.67 \times 10^{-21}}{9.6 \times 10^{-24}} = 1.74 \times 10^2~\text{m}$.
2. (b) Helium nucleus: $r = \frac{6.8 \times 10^{-27} \times 1.0 \times 10^6}{6.0 \times 10^{-5} \times 3.2 \times 10^{-19}} = \frac{6.8 \times 10^{-21}}{1.92 \times 10^{-23}} = 3.54 \times 10^2~\text{m}$.
3. Both are positive, so both bend the same way (towards the same side); the helium nucleus has the larger radius (about twice the proton's), so it bends less.

**Answer:** (a) $r = 1.7 \times 10^2~\text{m}$; (b) proton radius $1.7 \times 10^2~\text{m}$, helium nucleus radius $3.5 \times 10^2~\text{m}$, both curving the same way with the helium bending less.

**What the examiner wants:** (a) 3 marks: formula (1), correct charge for the proton (1), arithmetic with units (1). (b) 2 marks: correct relative curvature of the two paths (1) and radii stated on the diagram (1). The comparison ratio $\frac{r_{He}}{r_p} = \frac{6.8}{1.67} \times \frac{1.6}{3.2} \approx 2$ is the quickest route to a correct sketch.

### Example 10: The metal strip and the Hall voltage - End-of-chapter Q10, 16 marks

**Question:** Figure 27.19 shows a thin metal strip of thickness $t = 0.030~\text{mm}$ and width $d = 9.0~\text{mm}$ carrying a current $I = 40~\text{mA}$, in a magnetic field $B = 0.60~\text{T}$ at right angles to the current. (a)(i) Mark the side of the strip that becomes negative because of the Hall effect. [1] (a)(ii) State where a voltmeter must be placed to measure the Hall voltage. [1] (b) Derive an expression for the Hall voltage in terms of $I$, $B$, $t$, the number density $n$ of free electrons and the charge $e$ on an electron. [3] (c)(i) Calculate the mean drift velocity of the free electrons, given $n = 8.5 \times 10^{28}~\text{m}^{-3}$. [3] (c)(ii) Calculate the Hall voltage across the strip. [2] (d)(i) Explain, in terms of the movement of electrons, why the Hall voltage increases when $I$ increases. [2] (d)(ii) Explain why a semiconductor is used for a Hall probe rather than metal. [2] (e) Explain why, when the strip is rotated about the horizontal axis XY, the Hall voltage varies between a maximum positive value and a maximum negative value. [2]

**Method:**
1. (a)(i) For the standard figure layout (current to the right, field into the page): the electrons move to the left (opposite the conventional current) and are pushed by the magnetic force towards the top face, so the top face (X) becomes negative. Apply the left-hand rule to your own diagram.
2. (a)(ii) Connect the voltmeter between the two opposite faces of the strip (across X and Y), so it measures the p.d. between the faces that have separated charge.
3. (b) Equilibrium: electric force $=$ magnetic force, $eE = Bev$ with $E = \frac{V_H}{d}$, giving $V_H = Bvd$. Substitute $v = \frac{I}{nAe}$ with cross-sectional area $A = dt$: $V_H = \frac{BId}{nAe} = \frac{BI}{nte}$.
4. (c)(i) $v = \frac{I}{nAe}$ with $A = dt = 9.0 \times 10^{-3} \times 0.030 \times 10^{-3} = 2.7 \times 10^{-7}~\text{m}^2$.
5. $v = \frac{0.040}{8.5 \times 10^{28} \times 2.7 \times 10^{-7} \times 1.60 \times 10^{-19}} = \frac{0.040}{3.67 \times 10^3} = 1.09 \times 10^{-5}~\text{m s}^{-1}$.
6. (c)(ii) $V_H = \frac{BI}{nte} = \frac{0.60 \times 0.040}{8.5 \times 10^{28} \times 0.030 \times 10^{-3} \times 1.60 \times 10^{-19}} = \frac{0.024}{4.08 \times 10^5} = 5.9 \times 10^{-8}~\text{V}$.
7. Cross-check with the equilibrium form: $V_H = Bvd = 0.60 \times 1.09 \times 10^{-5} \times 9.0 \times 10^{-3} = 5.9 \times 10^{-8}~\text{V}$. Consistent.
8. (d)(i) A larger current means a larger drift velocity $v$ (at fixed $n$ and $A$), so the sideways magnetic force $Bev$ on each electron is larger, more charge separates, and the Hall voltage (proportional to the separated charge) increases.
9. (d)(ii) A semiconductor has a much smaller number density of free electrons $n$ than a metal, and $V_H = \frac{BI}{nte}$ is inversely proportional to $n$, so the Hall voltage is much larger for the same current, field and thickness (the electrons also drift faster for the same current).
10. (e) The Hall voltage depends on the component of $B$ perpendicular to the plane of the strip: rotating the strip changes the angle $\theta$ between the field and the normal to the strip, and $V_H = V_{\text{max}}\cos\theta$. As the strip rotates through $180^{\circ}$, this component sweeps from maximum positive through zero to maximum negative, so the measured voltage varies between a maximum positive and a maximum negative value.

**Answer:** (a)(i) top face X negative for the standard layout; (a)(ii) across the two faces X and Y; (b) $V_H = \frac{BI}{nte}$; (c)(i) $v = 1.1 \times 10^{-5}~\text{m s}^{-1}$; (c)(ii) $V_H = 5.9 \times 10^{-8}~\text{V}$; (d)(i) bigger $I$ means bigger $v$, hence bigger sideways force and more separation; (d)(ii) $n$ is far smaller in a semiconductor, so $V_H$ is far larger; (e) $V_H \propto$ component of $B$ perpendicular to the strip, which varies as $\cos\theta$ through a full rotation.

**What the examiner wants:** (a) 1 mark each for the correct face and the voltmeter position. (b) 3 marks for the full derivation: balance $eE = Bev$ (1), substitute $E = \frac{V_H}{d}$ and $v = \frac{I}{nAe}$ (1), substitute $A = dt$ and cancel (1). (c)(i) 3 marks for $I = nAve$ with $A = dt$ and converted units; (c)(ii) 2 marks for $V_H = \frac{BI}{nte}$ (or $V_H = Bvd$ as a check). (d)(i) 2 marks for linking $I$ to $v$ and $v$ to the sideways force. (d)(ii) 2 marks for small $n$ and the inverse proportionality. (e) 2 marks for the perpendicular component idea plus the sign reversal over half a turn.

---

# Chapter 28: Electromagnetic Induction
> Source: `physics/notes/chapter-28-electromagnetic-induction-notes.md`

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

---

# Chapter 29: Alternating Currents
> Source: `physics/notes/chapter-29-alternating-currents-notes.md`

## 4. Methods (Question Types & Methods)

These are the ways Cambridge has actually asked about alternating currents. Each method below is what a full-mark answer looks like.

### 1. Write the equation of a sinusoidal a.c. or voltage from a graph or from $f$/$T$

**Method:**
1. Read $I_0$ or $V_0$ (peak) from the highest point on the graph (units A or V).
2. Find the period $T$ (time for one complete cycle) and $f = 1/T$.
3. Calculate $\omega = 2\pi f$.
4. Write $I = I_0 \sin \omega t$ or $V = V_0 \sin \omega t$ with $t$ in seconds and the argument in radians.

**Traps:** confusing peak-to-peak with peak (peak is half the peak-to-peak height); leaving the answer as $I = I_0 \sin(2\pi f t)$ instead of substituting the numerical $\omega$; using degrees instead of radians.

### 2. Find $f$, $T$ or $\omega$ from the equation $I = I_0 \sin \omega t$

**Method:**
1. Compare the given equation with $I = I_0 \sin \omega t$ to read off $I_0$ and $\omega$.
2. $f = \frac{\omega}{2\pi}$ and $T = \frac{1}{f} = \frac{2\pi}{\omega}$.

**Traps:** writing $f = \omega$ (forgetting $2\pi$); reading $120\pi t$ as $\omega = 120$ instead of $120\pi$.

### 3. Convert between peak and r.m.s. values

**Method:**
1. For a **sinusoidal** waveform: $I_{\text{rms}} = \frac{I_0}{\sqrt{2}}$ and $V_{\text{rms}} = \frac{V_0}{\sqrt{2}}$.
2. Invert: $I_0 = \sqrt{2}\,I_{\text{rms}}$ and $V_0 = \sqrt{2}\,V_{\text{rms}}$.
3. The mains $230~\text{V}$ (or $240~\text{V}$) quoted in questions is always $V_{\text{rms}}$ unless the question says "peak".

**Traps:** using $1/\sqrt{2}$ for a non-sinusoidal waveform (e.g. half-wave rectified — the mean power and hence the r.m.s. are different); multiplying by $\sqrt{2}$ when you should divide, and vice versa. Remember: **r.m.s. < peak**, so $I_{\text{rms}} = 0.707\,I_0$.

### 4. Calculate mean power in a resistive load

**Method:**
1. Identify $I_{\text{rms}}$ or $V_{\text{rms}}$ (convert from peak first if necessary).
2. Choose: $P = I_{\text{rms}}^2 R$ if you know current and $R$; $P = \frac{V_{\text{rms}}^2}{R}$ if you know voltage and $R$; $P = I_{\text{rms}} V_{\text{rms}}$ if you know both.
3. Quote $P$ in watts — this is the **mean** power.

**Traps:** using peak values in the power formula (gives double the correct mean power); using $P = I_0^2 R$ or $P = \frac{V_0^2}{R}$ without the $\frac{1}{2}$ — the factor-of-2 error is the single most common loss in this chapter.

### 5. Compare d.c. and a.c. heating (ratio questions)

**Method:**
1. D.C. power: $P_{\text{dc}} = I_{\text{dc}}^2 R$ (or $V_{\text{dc}}^2/R$).
2. A.C. mean power: $P_{\text{ac}} = I_{\text{rms}}^2 R = \frac{I_0^2}{2}R$.
3. Ratio: $\frac{P_{\text{dc}}}{P_{\text{ac}}} = \frac{I_{\text{dc}}^2}{I_{\text{rms}}^2}$ or $\frac{P_{\text{ac}}}{P_{\text{dc}}}$ as asked.

**Traps:** saying the heating effects are the same when $I_0 = I_{\text{dc}}$ (they are not — a.c. mean power is half); forgetting to square the currents in the ratio.

### 6. Read a CRO trace to find $V_0$, $V_{\text{rms}}$, $T$ and $f$

**Method:**
1. Vertical amplitude (cm or div) $\times$ Y-gain ($\text{V cm}^{-1}$ or $\text{V div}^{-1}$) $= V_0$ (peak). Then $V_{\text{rms}} = V_0/\sqrt{2}$.
2. Horizontal length of one complete cycle (cm or div) $\times$ time-base ($\text{s cm}^{-1}$ or $\text{s div}^{-1}$) $= T$. Then $f = 1/T$.
3. For current: $I_{\text{rms}} = V_{\text{rms}}/R$ if the trace is the voltage across a known resistor $R$.
4. Mean power: $P = V_{\text{rms}}^2/R$.

**Traps:** mixing up axes (time is $x$, voltage is $y$); reading peak-to-peak as peak; forgetting to convert ms to s ($1~\text{ms} = 10^{-3}~\text{s}$); using the wrong gain or time-base value after the question changes it.

### 7. Use the transformer turns-ratio equation

**Method:**
1. Write $\frac{V_{\text{s}}}{V_{\text{p}}} = \frac{N_{\text{s}}}{N_{\text{p}}}$ — keep secondary on top on both sides.
2. Substitute the two known values and solve for the third.
3. If power is asked and the transformer is ideal/100% efficient: $I_{\text{p}} V_{\text{p}} = I_{\text{s}} V_{\text{s}}$, so $I_{\text{s}} = I_{\text{p}}\frac{V_{\text{p}}}{V_{\text{s}}} = I_{\text{p}}\frac{N_{\text{p}}}{N_{\text{s}}}$.

**Traps:** swapping $N_{\text{p}}$ and $N_{\text{s}}$ (check: step-up means $N_{\text{s}} > N_{\text{p}}$); using peak for one side and r.m.s. for the other (use the same type on both sides — the ratio cancels the $\sqrt{2}$); assuming $I_{\text{p}} V_{\text{p}} = I_{\text{s}} V_{\text{s}}$ when the transformer is not ideal or losses are mentioned.

### 8. Solve power-transmission questions (high voltage, low loss)

**Method:**
1. Current in the cable: $I_{\text{rms}} = \frac{P}{V_{\text{rms}}}$ where $P$ is the **transmitted power** (not the loss).
2. Power lost as heat: $P_{\text{loss}} = I_{\text{rms}}^2 R_{\text{cable}}$.
3. Efficiency of transmission: $\frac{P - P_{\text{loss}}}{P} \times 100\%$.
4. To show the advantage: repeat for a higher $V$ and compare — $P_{\text{loss}} \propto 1/V^2$.

**Traps:** using $P_{\text{loss}} = \frac{V^2}{R}$ with the transmission voltage (that formula would give the power if the full transmission voltage were across the cable resistance — it is not; the cable voltage drop is $IR$, not $V_{\text{transmission}}$); confusing transmitted power with lost power (the question uses the same letter $P$ for both — label them); saying "high voltage reduces resistance" (resistance is unchanged; only current changes).

### 9. Identify transformer type and explain the design (flux, core, laminations)

**Method:**
1. State whether it is step-up ($N_{\text{s}} > N_{\text{p}}$) or step-down ($N_{\text{s}} < N_{\text{p}}$).
2. For "explain" questions: refer to Faraday's law — alternating current in primary $\rightarrow$ alternating magnetic flux in soft iron core $\rightarrow$ changing flux linkage in secondary $\rightarrow$ induced alternating e.m.f. in secondary.
3. Laminated / soft iron core: reduces eddy currents / hysteresis.

**Traps:** saying energy is transferred "through the wires" (it is via the magnetic field in the core); omitting "alternating/changing" flux (a steady flux induces no e.m.f.); saying laminations "reduce resistance" (they break up eddy-current paths in the core).

### 10. Draw and interpret rectification waveforms

**Method:**
1. Half-wave (1 diode): positive half-cycle passes unchanged, negative half-cycle is zero. Output frequency = supply frequency.
2. Full-wave bridge (4 diodes): both half-cycles are flipped positive; output is always $\ge 0$ with twice the supply frequency and no gaps.
3. Label axes: $V$ or $I$ on $y$, $t$ on $x$, with peak $V_0$ or $I_0$ marked.
4. For diode failure questions: one dead diode breaks the bridge — one half-cycle is lost and the output reverts to half-wave.

**Traps:** drawing full-wave as half-wave (leaving gaps); drawing the rectified frequency as the same as the supply for full-wave (it doubles); not labelling which terminal is positive on the load.

### 11. Smoothing — capacitor across the load: sketch, explain, and calculate

**Method:**
1. **Circuit:** capacitor $C$ is connected **in parallel (across) $R$**, after the rectifier.
2. **Sketch:** charging = steep rise following the rectified sine to $V_0$; discharging = gentle exponential decay between peaks; ripple amplitude = $V_0 - V_{\min}$.
3. **Effect of $R$ and $C$:** larger $C$ or larger $R$ $\rightarrow$ larger $RC$ $\rightarrow$ slower discharge $\rightarrow$ **less ripple**, higher mean voltage, higher mean power in $R$. Two equal capacitors in parallel $\rightarrow$ $C$ doubles $\rightarrow$ ripple halves.
4. **Calculations from the smoothed graph:** ripple $\Delta V \rightarrow \Delta Q = C\,\Delta V \rightarrow I_{\text{mean}} = \frac{\Delta Q}{\Delta t}$ (discharge time $\approx$ period minus brief charging time) $\rightarrow R \approx \frac{\langle V \rangle}{I_{\text{mean}}}$.

**Traps:** connecting the smoothing capacitor in series (it must be in parallel); saying "capacitor blocks a.c." (it charges and discharges — it does not block in this circuit); drawing the smoothed output as a flat line at $V_0$ (there is always some ripple; the voltage dips between peaks).

### 12. Flux and induced e.m.f. graphs for a transformer (Faraday phase question)

**Method:**
1. Primary current $I_{\text{p}} = I_0 \sin \omega t$.
2. Flux $\Phi$ in the core is **in phase** with $I_{\text{p}}$: $\Phi = \Phi_0 \sin \omega t$ — same sine shape, zero at the same times as the current.
3. Induced e.m.f. $E \propto -\frac{d\Phi}{dt}$: $E = -N\frac{d\Phi}{dt} = -N\omega\Phi_0 \cos \omega t$ — a **cosine** wave, $90°$ out of phase with the flux (zero when flux is at its peak, maximum when flux passes through zero). On the graph it is shifted by a quarter cycle.

**Traps:** drawing flux and e.m.f. in phase (they are not — e.m.f. is the derivative of flux); forgetting the minus sign / Lenz idea that the e.m.f. opposes the change (the phase shift is the way the mark scheme checks this).

### 13. Definitions and "explain" questions (frequent 2-mark questions)

**Method:**
1. **r.m.s.:** "the steady d.c. that dissipates the same mean power in the same resistor" — must say "steady d.c." and "same mean power / heating effect in the same (resistive) load".
2. **Why a.c. for power transmission:** "transformers can step voltage up, reducing current, so $I^2R$ losses in cables are reduced ($P_{\text{loss}} \propto 1/V^2$)".
3. **Rectification / smoothing:** "a.c. to d.c. (one direction only); diode conducts one way; capacitor in parallel charges and discharges to reduce ripple".
4. **Faraday's law:** "$E$ proportional to rate of change of (magnetic) flux linkage" — include "rate of change" and "flux linkage" ($N\Phi$), not just "flux".

**Traps:** defining r.m.s. as "$I_0/\sqrt{2}$" alone (1 mark at most — the words "same mean power" are required for full marks); saying "high voltage means low resistance" (wrong — low current); omitting "rate of change" in Faraday's law.

## 5. Solved Examples

Real exam-style questions from the end of Chapter 29 and from past 9702 papers, with their mark allocations. The format for every example: Question / Method / Answer / What the examiner wants.

### Example 1: Writing the equation of a sinusoidal current — End-of-chapter Q2, 6 marks

**Question:** The instantaneous value of an alternating current (in A) is $I = 2 \sin(50\pi t)$, where $t$ is in s. (a) What is the peak value of the current? [1] (b) What is the frequency? [2] (c) Sketch two cycles of $I$ against $t$, marking axes with suitable values. [2] (d) Calculate $I_{\text{rms}}$ and mark it on your graph. [1] (e) Find two values of $t$ at which $I = I_{\text{rms}}$. [3]

**Method:**
1. (a) Compare with $I = I_0 \sin \omega t$: $I_0 = 2.0~\text{A}$. [1]
2. (b) $\omega = 50\pi = 157~\text{rad s}^{-1}$; $f = \frac{\omega}{2\pi} = \frac{50\pi}{2\pi} = 25~\text{Hz}$; $T = \frac{1}{25} = 0.040~\text{s} = 40~\text{ms}$. [2]
3. (c) Sine wave from $0$ to $2.0~\text{A}$ peak, period $40~\text{ms}$, two cycles $0$–$80~\text{ms}$, crossing zero at $0$, $20$, $40$, $60$, $80~\text{ms}$. [2]
4. (d) $I_{\text{rms}} = \frac{2.0}{\sqrt{2}} = 1.41~\text{A}$ — horizontal dashed line at $1.41~\text{A}$ on the graph. [1]
5. (e) $I_{\text{rms}} = I_0 \sin \omega t \Rightarrow \sin(50\pi t) = \frac{1}{\sqrt{2}}$. So $50\pi t = \frac{\pi}{4}$ or $\frac{3\pi}{4}$ (first cycle). Hence $t = \frac{1}{200} = 5.0~\text{ms}$ or $t = \frac{3}{200} = 15~\text{ms}$ (and repeats every $40~\text{ms}$). [3]

**Answer:** (a) $2.0~\text{A}$; (b) $25~\text{Hz}$; (d) $1.41~\text{A}$; (e) $5.0~\text{ms}$ and $15~\text{ms}$ (then $45~\text{ms}$, $55~\text{ms}$, ...).

**What the examiner wants:** $\omega$ must be read as $50\pi$, not $50$; frequency needs the $2\pi$ step; the sketch must show two full cycles with correct $T$ and $I_0$ labelled; $I_{\text{rms}}$ marked as a horizontal line below the peak.

### Example 2: CRO measurement and power — End-of-chapter Q5, 7 marks

**Question:** An oscilloscope displays the voltage across a $200~\Omega$ resistor. Time-base $= 5.0~\text{ms div}^{-1}$, Y-gain $= 0.50~\text{V div}^{-1}$. The trace has peak height $3.0~\text{div}$ and one complete cycle occupies $4.0~\text{div}$. Determine (a) the period and frequency [2], (b) the peak and r.m.s. voltage [2], (c) the r.m.s. current [1], (d) the mean power [2].

**Method:**
1. (a) $T = 4.0 \times 5.0 = 20~\text{ms} = 0.020~\text{s}$; $f = \frac{1}{0.020} = 50~\text{Hz}$. [2]
2. (b) $V_0 = 3.0 \times 0.50 = 1.5~\text{V}$; $V_{\text{rms}} = \frac{1.5}{\sqrt{2}} = 1.06~\text{V}$. [2]
3. (c) $I_{\text{rms}} = \frac{V_{\text{rms}}}{R} = \frac{1.06}{200} = 5.3 \times 10^{-3}~\text{A}$. [1]
4. (d) $P = \frac{V_{\text{rms}}^2}{R} = \frac{1.06^2}{200} = 5.6 \times 10^{-3}~\text{W}$ (or $I_{\text{rms}}^2 R$ or $I_{\text{rms}} V_{\text{rms}}$). [2]

**Answer:** (a) $20~\text{ms}$, $50~\text{Hz}$; (b) $1.5~\text{V}$, $1.06~\text{V}$; (c) $5.3~\text{mA}$; (d) $5.6~\text{mW}$.

**What the examiner wants:** the CRO reading method (amplitude $\times$ Y-gain, length $\times$ time-base) with units; r.m.s. conversion; power must use r.m.s. values — using $V_0$ gives $11.3~\text{mW}$, which is double and earns at most 1 mark.

### Example 3: Transformer with a load — End-of-chapter Q3, 5 marks

**Question:** The $240~\text{V}$ r.m.s. mains is connected to the primary ($1200$ turns) of a transformer. The secondary r.m.s. output is $6.0~\text{V}$. (a) Calculate the number of secondary turns. [1] (b) A $6.0~\Omega$ resistor is connected across the secondary. Calculate (i) the mean power in the resistor [1], (ii) the peak current in the primary (assume ideal transformer). [3]

**Method:**
1. (a) $\frac{N_{\text{s}}}{N_{\text{p}}} = \frac{V_{\text{s}}}{V_{\text{p}}} = \frac{6.0}{240} = 0.025$; $N_{\text{s}} = 0.025 \times 1200 = 30$. [1]
2. (b)(i) $P = \frac{V_{\text{s,rms}}^2}{R} = \frac{6.0^2}{6.0} = 6.0~\text{W}$. [1]
3. (b)(ii) Secondary r.m.s. current: $I_{\text{s,rms}} = \frac{V_{\text{s,rms}}}{R} = \frac{6.0}{6.0} = 1.0~\text{A}$; so $I_{\text{s,peak}} = \sqrt{2} \times 1.0 = 1.41~\text{A}$. Ideal: $I_{\text{p}} V_{\text{p}} = I_{\text{s}} V_{\text{s}}$, so $I_{\text{p,peak}} = I_{\text{s,peak}} \times \frac{V_{\text{s,peak}}}{V_{\text{p,peak}}} = I_{\text{s,peak}} \times \frac{N_{\text{s}}}{N_{\text{p}}} = 1.41 \times 0.025 = 0.035~\text{A}$ (equivalently $I_{\text{p,rms}} = 0.025~\text{A}$, peak $= 0.035~\text{A}$). [3]

**Answer:** (a) $30$ turns; (b)(i) $6.0~\text{W}$; (b)(ii) $35~\text{mA}$ peak in the primary.

**What the examiner wants:** the turns ratio in the correct orientation; for (b)(ii) the chain r.m.s. $\rightarrow$ peak must be explicit — candidates who give $I_{\text{p,rms}} = 25~\text{mA}$ without converting to peak lose the last mark.

### Example 4: Flux and induced e.m.f. graphs — End-of-chapter Q4, 3 marks

**Question:** The graph shows the sinusoidal current in the primary of a transformer (secondary open-circuit). On the same axes sketch (i) the magnetic flux in the core (label A) [1], (ii) the induced e.m.f. in the primary (label B) [1]. (b) How are the two graphs related? [1]

**Method:**
1. (i) Flux $\Phi \propto I_{\text{p}}$: same sine wave as the current, in phase — zero at the same times, peak at the same times. Label A. [1]
2. (ii) Induced e.m.f. $E \propto -\frac{d\Phi}{dt}$: cosine wave, $90°$ shifted — zero when flux is at its maximum, maximum when flux passes through zero. Label B. [1]
3. (b) The e.m.f. is proportional to the rate of change of flux linkage (Faraday's law) and opposes the change (Lenz's law); it is $90°$ / a quarter cycle out of phase with the flux. [1]

**Answer:** A = sine (in phase with current); B = cosine (quarter-cycle shift, zero at flux peaks).

**What the examiner wants:** the phase relationship — flux follows current, e.m.f. is the derivative (cosine). A sketch with both curves in phase earns zero for (ii).

### Example 5: r.m.s. ratio and advantage of a.c. — End-of-chapter Q6, 6 marks

**Question:** (a) State $I_{\text{rms}}$ in terms of $I_0$ for a sine wave. [1] (b) A resistor carries $2.0~\text{A}$ d.c. and, separately, a sinusoidal a.c. with peak $2.0~\text{A}$. (i) Explain why the heating effects differ and which is greater. [2] (ii) Calculate $\frac{P_{\text{dc}}}{P_{\text{ac}}}$. [2] (c) State one advantage of a.c. in the home. [1]

**Method:**
1. (a) $I_{\text{rms}} = \frac{I_0}{\sqrt{2}}$. [1]
2. (b)(i) Heating $\propto I^2$, but a.c. spends part of the cycle below its peak and reverses direction; its mean squared value is half the peak squared, so mean power $\propto I_{\text{rms}}^2 = I_0^2/2$ is less than d.c. power $\propto I_{\text{dc}}^2$ when $I_0 = I_{\text{dc}}$. D.C. heating is greater. [2]
3. (b)(ii) $P_{\text{dc}} = I_{\text{dc}}^2 R = 4.0\,R$; $P_{\text{ac}} = I_{\text{rms}}^2 R = \frac{I_0^2}{2}R = 2.0\,R$; ratio $\frac{P_{\text{dc}}}{P_{\text{ac}}} = 2$. [2]
4. (c) A.c. voltage can be transformed to high voltage for efficient transmission (low $I^2R$ loss), or a.c. easily produces rotating magnetic fields for motors — any one valid advantage. [1]

**Answer:** (a) $I_0/\sqrt{2}$; (b)(ii) ratio $= 2$ (d.c. twice the mean a.c. power); (c) can be transformed / lower transmission losses.

**What the examiner wants:** the $\sqrt{2}$ statement alone for (a); for (b)(i) the link "power $\propto I^2$" and "mean power uses $I_{\text{rms}}$" — saying "a.c. averages to zero so no heating" is a zero-mark error.

### Example 6: Half-wave rectification with a diode — End-of-chapter Q7, 13 marks

**Question:** A $6.0~\text{V}$ r.m.s., $50~\text{Hz}$ sinusoidal supply is connected via a diode to a $400~\Omega$ resistor. (a) Sketch the supply voltage (dotted) and the voltage across $R$ (solid) on the same axes with scales. [4] (b) An uncharged capacitor $C$ is connected across $R$. It charges fully in the first quarter-cycle (diode drop $= 0$). For the next three-quarters of the first cycle, the diode stops conducting and the voltage across $R$ falls to half the peak value; the mean voltage during this discharge is $5.7~\text{V}$. For these three-quarters, calculate (i) the time taken [1], (ii) the mean current in $R$ [2], (iii) the charge through $R$ [2], (iv) the capacitance of $C$ [2]. (c) Explain why the diode stops conducting. [2]

**Method:**
1. (a) Peak: $V_0 = \sqrt{2} \times 6.0 = 8.5~\text{V}$; period $T = \frac{1}{50} = 20~\text{ms}$. Dotted: full sine $\pm 8.5~\text{V}$ at $50~\text{Hz}$. Solid: half-wave — the positive half-sine ($0$ to $8.5~\text{V}$) is present, the negative half-cycle is $0$ (diode blocks). [4]
2. (b)(i) Three-quarters of a cycle: $\Delta t = \frac{3}{4}T = \frac{3}{4} \times 20 = 15~\text{ms} = 0.015~\text{s}$. [1]
3. (b)(ii) Mean current during discharge: $I = \frac{\langle V \rangle}{R} = \frac{5.7}{400} = 1.425 \times 10^{-2}~\text{A} = 14.3~\text{mA}$. [2]
4. (b)(iii) Charge: $Q = I\,\Delta t = 1.425 \times 10^{-2} \times 0.015 = 2.14 \times 10^{-4}~\text{C}$. [2]
5. (b)(iv) $C$ charged to $V_0 = 8.5~\text{V}$ and fell to $V = 4.25~\text{V}$ ($\frac{1}{2}V_0$), so $\Delta V = 4.25~\text{V}$. $C = \frac{\Delta Q}{\Delta V} = \frac{2.14 \times 10^{-4}}{4.25} = 5.0 \times 10^{-5}~\text{F} = 50~\mu\text{F}$. [2]
6. (c) While the capacitor discharges through $R$, its voltage exceeds the supply voltage for most of the cycle. The diode is then reverse-biased (cathode more positive than anode), so it blocks. [2]

**Answer:** (b)(i) $15~\text{ms}$; (b)(ii) $14~\text{mA}$; (b)(iii) $2.1 \times 10^{-4}~\text{C}$; (b)(iv) $50~\mu\text{F}$; (c) capacitor voltage $>$ supply voltage $\rightarrow$ diode reverse-biased.

**What the examiner wants:** the half-wave sketch with correct $V_0$ and $T$ and the zero half-cycles; the chain $\langle V \rangle \rightarrow I \rightarrow Q \rightarrow C$ with the correct $\Delta V$ (peak to half-peak, not peak to zero).

### Example 7: Smoothing and ripple — End-of-chapter Q8, 12 marks

**Question:** The rectified output from a transformer is across a $1000~\Omega$ resistor. Graph A shows the unsmoothed p.d. across $R$ (full-wave rectified); Graph B shows the smoothed p.d. when a capacitor is placed across $R$. (a) How is rectification achieved? Draw the circuit. [6] (b) Explain the action of the capacitor. [3] (c) Using Graph B between $t = 0.005$ and $0.015~\text{s}$, determine (i) the charging time [1], (ii) the mean p.d. across $R$ [1], (iii) the mean power in $R$ [2].

**Method:**
1. (a) Four diodes in a bridge: supply across one diagonal, $R$ across the other. When $X$ is positive, diodes B and C conduct; when $Y$ is positive, diodes A and D conduct — current through $R$ always flows the same way. Full-wave: both half-cycles contribute. [6]
2. (b) $C$ in parallel with $R$. When rectified $V$ rises, $C$ charges to near $V_0$ through the low-resistance diode path. When rectified $V$ falls, the diode blocks and $C$ discharges through $R$, holding the voltage up — ripple is the small drop between peaks. [3]
3. (c)(i) Charging time = brief steep rise near each peak ($\approx 1$–$2~\text{ms}$ on the graph). Discharge dominates the cycle. [1]
4. (c)(ii) Mean $V$ $\approx$ midline of the ripple (e.g. $0.8$–$0.9~\text{V}$ if $V_0 = 1.0~\text{V}$ — read from the graph's mid-ripple level). [1]
5. (c)(iii) $P = \frac{\langle V \rangle^2}{R}$ (or $\langle V \rangle^2/R$ with the mean $V$ from (ii); using the graph's mean $\approx 0.85~\text{V}$, $P \approx \frac{0.85^2}{1000} = 0.72~\text{mW}$). [2]

**Answer:** (a) Bridge of four diodes; (b) charges on peaks, discharges through $R$ between peaks — reduces ripple; (c)(i) $\approx 1$–$2~\text{ms}$; (c)(ii) $\approx 0.85~\text{V}$ (read from mid-ripple); (c)(iii) $\approx 0.7~\text{mW}$.

**What the examiner wants:** the bridge diagram with correct diode directions and load connections; the two-phase "charge on rise, discharge on fall" explanation with "diode blocks"; power must use the **mean** (smoothed) voltage, not the peak.

### Example 8: Transformer, rectification and smoothing combined — End-of-chapter Q9, 9 marks

**Question:** A transformer produces $12~\text{V}$ peak output from the $230~\text{V}$ r.m.s. mains. (a) Its primary has $2000$ turns — find $N_{\text{s}}$. [3] (b) The secondary output is half-wave rectified and connected to $R$ and $C$ in parallel. Sketch on the same axes (i) the secondary p.d. and (ii) the p.d. across $R$. [3] (c) A second equal capacitor is placed in parallel with $C$. What happens to the p.d. across $R$? Explain. [3]

**Method:**
1. (a) Mains r.m.s. $= 230~\text{V}$, so primary peak $= \sqrt{2} \times 230 = 325~\text{V}$. Secondary peak $= 12~\text{V}$. $\frac{N_{\text{s}}}{N_{\text{p}}} = \frac{V_{\text{s,peak}}}{V_{\text{p,peak}}} = \frac{12}{325} = 0.0369$. $N_{\text{s}} = 2000 \times 0.0369 = 74$ turns. (If using r.m.s. throughout: $V_{\text{s,rms}} = 12/\sqrt{2} = 8.49~\text{V}$, ratio $= 8.49/230 = 0.0369$, same result. Mixing peak with r.m.s. without converting is the trap — here we converted consistently.) [3]
2. (b)(i) Secondary: sine wave $\pm 12~\text{V}$ peak. (ii) Across $R$: half-wave rectified — positive half-sine $0$ to $12~\text{V}$, negative half-cycle $0$; if $C$ is present the gaps are partially filled with a decaying exponential between peaks (smoothed half-wave). [3]
3. (c) $C_{\text{total}} = 2C$, so $RC$ doubles. The capacitor discharges more slowly between peaks, so **ripple decreases**, **mean voltage increases**, and mean power in $R$ increases. [3]

**Answer:** (a) $\approx 74$ turns; (b) see sketches: secondary = full sine $\pm 12~\text{V}$, $V_R$ = half-wave / smoothed half-wave; (c) ripple decreases, mean $V$ rises.

**What the examiner wants:** consistent peak/r.m.s. handling — r.m.s. on one side and peak on the other must be converted first; the two sketches on the same time axis with the same $T$; the $C \rightarrow 2C$ $\rightarrow$ larger $RC$ $\rightarrow$ less ripple chain.

### Example 9: High-voltage transmission — End-of-chapter Q10, 12 marks

**Question:** A $400~\text{kV}$ r.m.s. line of resistance $4.0~\Omega$ carries $500~\text{MW}$. (a)(i) What is meant by r.m.s. voltage? [2] (a)(ii) What peak voltage must the insulators withstand? [2] (b)(i) Find the r.m.s. current in the line. [2] (b)(ii) Find the power loss. [2] (b)(iii) Why is high voltage an advantage? [2] (c) Describe the principle of a step-down transformer. [2]

**Method:**
1. (a)(i) The steady d.c. voltage that would dissipate the same mean power in the same resistor as the a.c. voltage. [2]
2. (a)(ii) $V_0 = \sqrt{2} \times 400 = 566~\text{kV}$. Insulators must withstand at least this (practically higher, with a safety margin). [2]
3. (b)(i) $I_{\text{rms}} = \frac{P}{V_{\text{rms}}} = \frac{500 \times 10^6}{400 \times 10^3} = 1250~\text{A}$. [2]
4. (b)(ii) $P_{\text{loss}} = I_{\text{rms}}^2 R = 1250^2 \times 4.0 = 6.25 \times 10^6~\text{W} = 6.3~\text{MW}$. [2]
5. (b)(iii) For the same transmitted power, higher $V$ means lower $I$ ($I = P/V$), so $P_{\text{loss}} = I^2 R \propto 1/V^2$ is smaller — less fuel, fewer power stations. [2]
6. (c) Primary current produces alternating magnetic flux in a soft iron (laminated) core; the changing flux linkage induces an alternating e.m.f. in the secondary; step-down has $N_{\text{s}} < N_{\text{p}}$, so $V_{\text{s}} < V_{\text{p}}$ and (ideally) $I_{\text{s}} > I_{\text{p}}$. [2]

**Answer:** (a)(ii) $566~\text{kV}$; (b)(i) $1.25 \times 10^3~\text{A}$; (b)(ii) $6.3~\text{MW}$; (b)(iii) lower $I$ $\rightarrow$ lower $I^2R$ loss.

**What the examiner wants:** the r.m.s. definition with "same mean power in the same resistor"; peak $= \sqrt{2} \times$ r.m.s.; $P_{\text{loss}} = I^2R$ with $I = P/V$ — not $V^2/R$ with the transmission voltage.

### Example 10: a.c. basics — mean, r.m.s. and power — Past-paper style, 7 marks

**Question:** (a) Explain why a sinusoidal alternating current gives a heating effect even though its mean value is zero. [2] (b) Define the r.m.s. value. [2] (c) An a.c. of peak $3.0~\text{A}$ flows through a $100~\Omega$ resistor. Calculate the mean power. [3]

**Method:**
1. (a) Power $\propto I^2$; $I^2$ is always positive (negative current still gives positive $I^2$), so energy is dissipated in both half-cycles even though the signed mean of $I$ is zero (positive half cancels negative half). [2]
2. (b) The steady d.c. that dissipates the same mean power in the same resistor. [2]
3. (c) $I_{\text{rms}} = \frac{3.0}{\sqrt{2}} = 2.12~\text{A}$; $P = I_{\text{rms}}^2 R = 2.12^2 \times 100 = 450~\text{W}$. (Equivalently $P = \frac{I_0^2}{2}R$.) [3]

**Answer:** (c) $450~\text{W}$; peak power $= 900~\text{W}$.

**What the examiner wants:** "power depends on $I^2$, which is always positive" — the key idea; r.m.s. definition with "same mean power"; power must be halved from the peak-power value.

### Example 11: Transformer ratios and efficiency — Past-paper style, 6 marks

**Question:** A step-up transformer has $N_{\text{p}} = 100$, $N_{\text{s}} = 500$, $V_{\text{p}} = 230~\text{V}$ r.m.s., primary current $1.0~\text{A}$ r.m.s. (a) Find $V_{\text{s}}$ (ideal). [2] (b) Find $I_{\text{s}}$ (ideal). [2] (c) In practice $V_{\text{s}} = 1100~\text{V}$ and $I_{\text{s}} = 0.19~\text{A}$. Find the efficiency. [2]

**Method:**
1. (a) $V_{\text{s}} = V_{\text{p}} \times \frac{N_{\text{s}}}{N_{\text{p}}} = 230 \times 5 = 1150~\text{V}$. [2]
2. (b) $I_{\text{s}} = I_{\text{p}} \times \frac{N_{\text{p}}}{N_{\text{s}}} = 1.0 \times \frac{1}{5} = 0.20~\text{A}$. [2]
3. (c) $P_{\text{in}} = 230 \times 1.0 = 230~\text{W}$; $P_{\text{out}} = 1100 \times 0.19 = 209~\text{W}$; efficiency $= \frac{209}{230} \times 100\% = 91\%$. [2]

**Answer:** (a) $1150~\text{V}$; (b) $0.20~\text{A}$; (c) $91\%$.

**What the examiner wants:** the two ratios used in the correct sense (voltage $\propto N$, current $\propto 1/N$); efficiency as $P_{\text{out}}/P_{\text{in}}$ with the actual measured values.

### Example 12: Bridge rectifier and smoothing graph — Past-paper style, 8 marks

**Question:** A bridge rectifier delivers full-wave rectified output to a $2700~\Omega$ resistor. The p.d. across $R$ is shown (unsmoothed): a series of positive half-sines with peak $8.0~\text{V}$ at $100~\text{Hz}$ (supply $50~\text{Hz}$). (a) Use the graph to find the mean power in $R$ without smoothing. [3] (b) A capacitor is connected across $R$ to increase the mean power. Show where it is connected. [1] (c) One diode fails open-circuit. Sketch the new p.d. across $R$. [2]

**Method:**
1. (a) For full-wave rectified, both half-cycles contribute. Approximate mean $V^2$ over a cycle: for a sine, mean $V^2 = \frac{V_0^2}{2}$ even after rectification (rectification only flips the sign, $V^2$ is unchanged). So $P = \frac{V_{\text{rms}}^2}{R} = \frac{(V_0/\sqrt{2})^2}{R} = \frac{V_0^2}{2R} = \frac{64}{5400} = 1.19 \times 10^{-2}~\text{W} = 11.9~\text{mW}$. (Graph-reading alternative: estimate area/mean $V^2$ — same result to within reading tolerance.) [3]
2. (b) $C$ is connected **in parallel (across) $R$**, directly across the load terminals after the bridge. [1]
3. (c) Bridge broken $\rightarrow$ full-wave lost $\rightarrow$ half-wave: alternate half-cycles become zero, frequency halves to $50~\text{Hz}$, peak still $8.0~\text{V}$. [2]

**Answer:** (a) $\approx 12~\text{mW}$; (b) $C$ across $R$; (c) half-wave — every other half-sine missing.

**What the examiner wants:** $P$ unchanged by rectification (because $V^2$ is even); capacitor position is across the load, not in series; diode failure reverts full-wave to half-wave.

### Example 13: Calculating $C$ from a smoothed ripple — Past-paper style, 6 marks

**Question:** A bridge rectifier with smoothing capacitor $C = 5.0~\mu\text{F}$ across $R$ gives the smoothed waveform of Fig. 6.2 (Question 3 in the rectification topical). Between two peaks the voltage drops by $\Delta V = 0.60~\text{V}$ in $\Delta t = 9.0~\text{ms}$ and the mean voltage is $5.7~\text{V}$. (a) Find the charge lost by the capacitor during one discharge. [2] (b) Find the mean current in $R$ during discharge. [2] (c) Estimate $R$. [2]

**Method:**
1. (a) $\Delta Q = C\,\Delta V = 5.0 \times 10^{-6} \times 0.60 = 3.0 \times 10^{-6}~\text{C}$. [2]
2. (b) $I = \frac{\Delta Q}{\Delta t} = \frac{3.0 \times 10^{-6}}{9.0 \times 10^{-3}} = 3.3 \times 10^{-4}~\text{A} = 0.33~\text{mA}$. [2]
3. (c) $R = \frac{\langle V \rangle}{I} = \frac{5.7}{3.3 \times 10^{-4}} = 1.7 \times 10^4~\Omega = 17~\text{k}\Omega$. [2]

**Answer:** (a) $3.0~\mu\text{C}$; (b) $0.33~\text{mA}$; (c) $17~\text{k}\Omega$.

**What the examiner wants:** $\Delta Q = C\Delta V$ with the ripple $\Delta V$, not the peak voltage; $I = \Delta Q/\Delta t$ with the discharge time (not the full period); $R = V/I$ with the mean voltage during discharge.

### Example 14: Ideal transformer for a low-voltage device — Past-paper style, 6 marks

**Question:** An ideal transformer with $5000$ primary turns converts $230~\text{V}$ r.m.s. mains to $9.0~\text{V}$ peak output. (a) Find $N_{\text{s}}$. [3] (b) The output is full-wave rectified and smoothed by $C$ across $R$. State the charging interval on the smoothed $V$–$t$ graph and sketch the effect of doubling $R$. [3]

**Method:**
1. (a) Convert consistently: either both to peak or both to r.m.s. Primary peak $= \sqrt{2} \times 230 = 325~\text{V}$; secondary peak $= 9.0~\text{V}$. $\frac{N_{\text{s}}}{N_{\text{p}}} = \frac{9.0}{325} = 0.0277$; $N_{\text{s}} = 139$ turns. (Equivalently secondary r.m.s. $= 9.0/\sqrt{2} = 6.36~\text{V}$; ratio $= 6.36/230 = 0.0277$ — same result.) [3]
2. (b) $C$ charges during the brief steep rise to each peak (when the rectified supply exceeds the capacitor voltage and the diodes conduct); it discharges during the long gentle decay between peaks. Doubling $R$ $\rightarrow$ $RC$ doubles $\rightarrow$ slower discharge $\rightarrow$ less ripple, higher mean voltage — sketch a flatter decay with a higher trough. [3]

**Answer:** (a) $\approx 140$ turns; (b) charging = narrow peak region; doubling $R$ $\rightarrow$ less ripple, higher mean $V$.

**What the examiner wants:** consistent peak/r.m.s. handling — mixing them without $\sqrt{2}$ is the main error; charging = short peak interval, not the whole cycle; larger $R$ $\rightarrow$ larger $RC$ $\rightarrow$ less ripple.

