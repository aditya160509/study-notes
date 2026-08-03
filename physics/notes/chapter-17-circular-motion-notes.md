# Chapter 17: Circular Motion - CAIE A Level Physics (9702) Study Notes

This chapter is A2 content in the CAIE 9702 syllabus, where it appears as Topic 12 "Motion in a circle". It is examined mainly in Paper 4 (structured questions, 2 hours) and Paper 1 (multiple choice). The physics is short on content but long on traps, so this guide is built around what Cambridge actually asks: definitions, conversions, the four equations, and force-resolution situations (vertical circles, conical pendulums, banked tracks, fairground rides, orbits).

## 1. Theory

### 1.1 Angular displacement and the radian

For an object moving in a straight line, position is described by displacement $s$. For an object moving round a circle, the corresponding quantity is **angular displacement** $\theta$: the angle (measured from a reference direction) through which the object has moved. Its SI unit is the **radian** (symbol rad), not degrees.

**Definition of the radian (learn this word for word, it is asked directly):**

> One radian is the angle subtended at the centre of a circle by an arc of length equal to the radius of the circle.

This definition is equivalent to the working definition: if an object moves a distance $s$ along an arc of a circle of radius $r$, its angular displacement is

$$\theta = \frac{s}{r}$$

Because $s$ and $r$ are both lengths in metres, $\theta$ is a ratio: it is dimensionless, but it is given the unit radian. One complete circuit has arc length $2\pi r$, so

$$360^{\circ} = 2\pi \ \text{rad}$$

which gives the conversion factors:

$$\text{radians} = \text{degrees} \times \frac{\pi}{180^{\circ}}, \qquad \text{degrees} = \text{radians} \times \frac{180^{\circ}}{\pi}$$

Standard values worth knowing instantly: $180^{\circ} = \pi$ rad, $90^{\circ} = \pi/2$ rad, $45^{\circ} = \pi/4$ rad, and $1$ radian $\approx 57.3^{\circ}$.

### 1.2 Angular velocity

The **angular velocity** $\omega$ (Greek omega) is the rate of change of angular displacement:

$$\omega = \frac{\Delta \theta}{\Delta t}$$

Its SI unit is radians per second, $\text{rad s}^{-1}$. The exam definition mark goes to "rate of change of angular displacement" (or "angle turned through per unit time"). Do not write "speed of rotation" or "revolutions per second" - that is not the definition, and it is not in $\text{rad s}^{-1}$.

For uniform circular motion (steady speed, constant $\omega$), one revolution is $2\pi$ radians, so if the period is $T$ (time for one revolution, in seconds) and the frequency is $f$ (revolutions per second, in Hz):

$$\omega = \frac{2\pi}{T} = 2\pi f$$

Remember $T = 1/f$. To convert revolutions per minute (rpm) to $\text{rad s}^{-1}$: divide by 60 to get revolutions per second, then multiply by $2\pi$.

### 1.3 Relating linear speed and angular velocity: $v = r\omega$

Every point on a rotating rigid body has the same angular velocity, but points further from the axis move faster. The linear speed is

$$v = r\omega$$

where $r$ is the distance from the axis. Derivation: one revolution takes time $T$, during which a point travels the circumference $2\pi r$, so

$$v = \frac{2\pi r}{T} = r\left(\frac{2\pi}{T}\right) = r\omega$$

Two consequences the exam likes: (1) the rim of a spinning disc moves faster than a point near the centre, even though both have the same $\omega$; (2) if a question gives you a period or frequency, get $\omega$ first, then use $v = r\omega$.

### 1.4 Why circular motion needs a force

An object moving round a circle at steady speed has constant **speed** but changing **velocity**, because velocity is a vector and its direction is constantly changing (the velocity is always tangent to the circle). A change in velocity is an acceleration, so an object in uniform circular motion is accelerating even though its speed never changes.

By Newton's first law, a body whose velocity is changing must have a resultant (unbalanced) force acting on it. A vector diagram of the velocities at two nearby points shows the change in velocity $\Delta v$ points towards the centre of the circle. Since acceleration is in the same direction as $\Delta v$, and force is in the same direction as acceleration, both the **centripetal acceleration** and the **centripetal force** point towards the centre, at right angles to the velocity.

Key points to state in answers:

- The centripetal force is the **resultant** force acting on the object. It is not an extra force that appears out of nowhere; it is supplied by a real force (tension, friction, gravity, a normal contact force, or a component of one).
- The word "centripetal" means "towards the centre". It describes the direction of the force, not what causes it.
- An object moving in a circle is **not in equilibrium**: it has a resultant force acting on it.
- Because the centripetal force is perpendicular to the velocity, it does **no work** on the object. So the kinetic energy and speed stay constant. (Its component along the velocity is $F\cos 90^{\circ} = 0$.)
- If the centripetal force suddenly disappears (string breaks, road gets icy), the object moves off in a straight line **tangent** to the circle at constant velocity (Newton's first law). The coursebook's example: release a whirling bung and it flies off at a tangent.

### 1.5 Centripetal acceleration and centripetal force

For an object moving at speed $v$ in a circle of radius $r$ with angular velocity $\omega$, the magnitude of the centripetal acceleration is

$$a = \frac{v^{2}}{r} = r\omega^{2} = v\omega$$

(The coursebook derives $a = v\omega$ from a vector triangle, then substitutes $v = r\omega$ to get $a = v^{2}/r$; question 13 in the chapter asks you to show $a = \omega^{2}r$ from $a = v\omega$ and $v = r\omega$.)

Using Newton's second law $F = ma$, the magnitude of the centripetal force on an object of mass $m$ is

$$F = \frac{mv^{2}}{r} = mr\omega^{2}$$

Choose the version that matches the data you are given: if you know speed, use $v^{2}/r$; if you know angular velocity, use $r\omega^{2}$. Both are equally correct and the mark schemes accept either.

### 1.6 Where the centripetal force comes from (memorise these)

The exam frequently asks "state what provides the centripetal force" in a given situation, worth 1 to 2 marks. The answer is always a real force, never "centripetal force" itself:

| Situation | What provides the centripetal force |
|---|---|
| Moon orbiting the Earth | gravitational pull of the Earth |
| Earth orbiting the Sun | gravitational pull of the Sun |
| Car going round a flat, rough bend | friction between tyres and road |
| Rubber bung whirled on a string | tension in the string |
| Ball on the end of a pendulum | horizontal component of the tension |
| Aircraft banking to turn | horizontal component of the lift force |
| Fairground "rotor" (wall of death) | normal contact force from the spinning wall (friction balances the weight) |
| Satellite / spacecraft in orbit | gravitational pull of the planet |
| Particle in a centrifuge tube | (in the rotating frame, the wall/container pushes it round; in the exam, the force towards the centre is provided by the container) |
| Toy on a rotating turntable | friction between the toy and the turntable surface |

### 1.7 Vertical circles (mass on a string, roller coaster, bucket of water)

In a vertical circle the weight always acts vertically downwards, so the resultant force towards the centre changes around the loop. Analyse the top and bottom positions.

**At the bottom** of the circle, the tension (or normal contact force) $T$ acts upwards towards the centre and the weight $mg$ acts downwards, so

$$T - mg = \frac{mv^{2}}{r}$$

**At the top** of the circle, both the tension and the weight act downwards towards the centre, so

$$T + mg = \frac{mv^{2}}{r}$$

**Minimum speed at the top for a string (or for a track the car must stay in contact with):** the string goes slack (or the car loses contact) when $T = 0$. Then the weight alone provides the centripetal force:

$$mg = \frac{mv^{2}}{r} \qquad \Rightarrow \qquad v_{\text{min}} = \sqrt{gr}$$

Below this speed the string goes slack / the truck leaves the track. This is why a bucket of water can be swung over your head without spilling: at the top the water needs $mg = mv^{2}/r$, and if the bucket is fast enough the water is pressed into the bucket.

If you know the speed at one point and want it at another, combine with conservation of energy: between the bottom and the top the height change is the diameter $2r$, so

$$\frac{1}{2}mv_{\text{bottom}}^{2} = \frac{1}{2}mv_{\text{top}}^{2} + mg(2r) \qquad \Rightarrow \qquad v_{\text{bottom}}^{2} = v_{\text{top}}^{2} + 4gr$$

### 1.8 Horizontal circles: the conical pendulum

A mass on a string moving in a horizontal circle, with the string making an angle $\theta$ with the vertical, is a **conical pendulum**. The string sweeps out a cone. Resolve the tension $T$:

- vertically, the upward component balances the weight: $T\cos\theta = mg$
- horizontally, the inward component provides the centripetal force: $T\sin\theta = \dfrac{mv^{2}}{r}$

Dividing the second by the first:

$$\tan\theta = \frac{v^{2}}{rg}$$

The radius of the circle is related to the string length $L$ by $r = L\sin\theta$. The exam frequently asks you to show one of these relationships, or to find $T$, $\omega$, $v$ or the period from a diagram. If the mass moves faster, the angle $\theta$ increases (the string rises towards the horizontal) because a larger centripetal force is needed.

### 1.9 Banked tracks and banking aircraft

On a **banked** track (angled so the outside edge is higher), the normal contact force $N$ is not vertical. For a frictionless banked track at angle $\theta$:

- horizontally: $N\sin\theta = \dfrac{mv^{2}}{r}$
- vertically: $N\cos\theta = mg$

Dividing gives the design condition

$$\tan\theta = \frac{v^{2}}{rg}$$

A car travelling at this "design speed" needs no friction at all. The horizontal component of the normal force provides the centripetal force, which is why a banked track allows a higher cornering speed than a flat road. Going slower than the design speed, the car tends to slide **down** the slope (friction acts up the slope to hold it); going faster, it tends to slide **up** the slope. An aircraft banking works the same way with the lift force replacing the normal force.

### 1.10 Satellites and orbits

For a satellite (or the Moon, or the ISS) in a circular orbit of radius $r$ (measured from the centre of the planet), gravity provides the centripetal force:

$$\frac{mv^{2}}{r} = mg \qquad \Rightarrow \qquad v = \sqrt{gr}$$

where $g$ is the gravitational field strength at the orbital radius (not at the surface). Near the Earth's surface, with $g = 9.81 \ \text{m s}^{-2}$ and $R \approx 6.4 \times 10^{6}$ m, the orbital speed is

$$v = \sqrt{9.81 \times 6.4 \times 10^{6}} \approx 7.9 \times 10^{3} \ \text{m s}^{-1}$$

about 8 km per second. The period of one orbit is

$$T = \frac{2\pi r}{v}$$

Two exam habits for orbits: always use the distance from the **centre** of the planet (add the height above the surface to the planet's radius), and always use the value of $g$ at the orbit height, not at the surface, unless the question tells you otherwise.

## 2. Definition Sheet

These are the definitions you must be able to write word-perfect. The mark schemes are strict: they want the exact phrases, not an equation and not a circular definition (never define a term using the term itself).

### Radian

> One radian is the angle subtended at the centre of a circle by an arc of length equal to the radius of the circle.

(Mark scheme wording: "the angle subtended at the centre of a circle by an arc equal in length to the radius".) Equivalent working form: $\theta = s/r$, so $360^{\circ} = 2\pi$ rad.

### Angular displacement

> The angle, measured in radians from a reference direction, through which an object has moved.

The exam rarely asks for this definition directly, but it appears inside the angular velocity definition and in "show that" work, so write it with "radians" and "reference direction" included.

### Angular velocity

> The rate of change of angular displacement.

(Mark scheme wording: "rate of change of angular displacement", or "angle turned through per unit time".) SI unit: $\text{rad s}^{-1}$. Do not answer with an equation alone, and do not write "speed of rotation" or "revolutions per second".

### Centripetal acceleration

> The acceleration of an object moving in a circle, directed towards the centre and perpendicular to the velocity.

(The 1-mark definition accepted in the November 2021 mark scheme is exactly "acceleration perpendicular to velocity". For full marks add "towards the centre", and if useful, that it arises because the direction of the velocity changes. Quoting an equation is not enough.)

### Centripetal force

> The resultant force acting on an object moving in a circle, directed towards the centre and perpendicular to the velocity.

(Two key ideas the mark scheme wants: it is a **resultant** force, and it points **towards the centre**. You can add that it is supplied by a real force such as tension, friction, gravity or a normal contact force. It is not a third force that "balances" the others, and there is no "centrifugal force" in the 9702 syllabus.)

### Period

> The time taken for one complete revolution (one complete cycle).

Symbol $T$, SI unit second (s). Related to frequency by $T = 1/f$, and to angular velocity by $\omega = 2\pi/T$. Watch out: the mark scheme sometimes uses $T$ for the period in the same question where $T$ is also the tension - label yours clearly.

### Frequency

> The number of complete revolutions (or cycles) per unit time.

Symbol $f$, SI unit hertz (Hz) or $\text{s}^{-1}$. Related to period by $f = 1/T$, and to angular velocity by $\omega = 2\pi f$. To convert rpm to Hz, divide by 60.

## 3. Formula Sheet

| Formula | Meaning of symbols | SI units | When to use it |
|---|---|---|---|
| $\theta = \dfrac{s}{r}$ | $\theta$ = angular displacement, $s$ = arc length, $r$ = radius | $\theta$ in rad, $s$, $r$ in m | Converting arc length to angle, or defining the radian |
| $\omega = \dfrac{\Delta\theta}{\Delta t}$ | $\omega$ = angular velocity, $\Delta\theta$ = angular displacement in time $\Delta t$ | $\text{rad s}^{-1}$ | Finding angular velocity from angle and time; definition of angular velocity |
| $\omega = \dfrac{2\pi}{T} = 2\pi f$ | $T$ = period (time for one revolution), $f$ = frequency | $T$ in s, $f$ in Hz | Converting period or frequency (or rpm) into angular velocity |
| $v = r\omega$ | $v$ = linear speed, $r$ = radius, $\omega$ = angular velocity | $v$ in $\text{m s}^{-1}$ | Finding speed of a point on a rotating body, or speed from angular velocity |
| $a = \dfrac{v^{2}}{r} = r\omega^{2} = v\omega$ | $a$ = centripetal acceleration | $\text{m s}^{-2}$ | Finding centripetal acceleration from speed, angular velocity, or both |
| $F = \dfrac{mv^{2}}{r} = mr\omega^{2}$ | $F$ = centripetal force (resultant force towards centre), $m$ = mass | N | Finding the centripetal force, or the real force supplying it (tension, friction, gravity) |
| $v_{\text{min}} = \sqrt{gr}$ (top of vertical circle) | $v_{\text{min}}$ = minimum speed at the top, $g$ = 9.81 $\text{m s}^{-2}$, $r$ = radius | $\text{m s}^{-1}$ | Minimum speed so a string stays taut, water stays in a bucket, or a truck keeps contact at the top of a loop |
| $T - mg = \dfrac{mv^{2}}{r}$ (bottom of vertical circle) | $T$ = tension or contact force, $mg$ = weight | N | Tension/contact force at the bottom of a vertical circle |
| $T + mg = \dfrac{mv^{2}}{r}$ (top of vertical circle) | as above | N | Tension/contact force at the top of a vertical circle |
| $v_{\text{bottom}}^{2} = v_{\text{top}}^{2} + 4gr$ | speeds at bottom and top, radius $r$ | $\text{m}^{2}\text{s}^{-2}$ | Linking speeds at top and bottom via conservation of energy |
| $\tan\theta = \dfrac{v^{2}}{rg}$ (conical pendulum or banked track) | $\theta$ = angle with vertical (pendulum) or banking angle, $v$ = speed, $r$ = radius | dimensionless | Finding the angle, or showing the bank/pendulum condition |
| $v_{\text{max}} = \sqrt{\mu r g}$ (flat road) | $\mu$ = coefficient of friction, $r$ = radius of bend | $\text{m s}^{-1}$ | Maximum cornering speed before a car skids on a flat road |
| $v = \sqrt{gr}$ (orbit) | $g$ = gravitational field strength at orbital radius $r$ | $\text{m s}^{-1}$ | Orbital speed of a satellite; $r$ measured from the centre of the planet |
| $T = \dfrac{2\pi r}{v}$ (orbit) | $T$ = orbital period | s | Time for one orbit once speed and radius are known |

Degrees-radians conversion: $\text{radians} = \text{degrees} \times \dfrac{\pi}{180^{\circ}}$ and $\text{degrees} = \text{radians} \times \dfrac{180^{\circ}}{\pi}$. Standard values: $180^{\circ} = \pi$ rad, $90^{\circ} = \pi/2$ rad, $45^{\circ} = \pi/4$ rad, $1$ rad $\approx 57.3^{\circ}$.

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

## 6. Cheat Sheet

### All formulas in one block

$$\theta = \frac{s}{r}, \qquad \omega = \frac{\Delta\theta}{\Delta t}, \qquad \omega = \frac{2\pi}{T} = 2\pi f, \qquad v = r\omega$$

$$a = \frac{v^{2}}{r} = r\omega^{2} = v\omega, \qquad F = \frac{mv^{2}}{r} = mr\omega^{2}$$

Vertical circle: top $T + mg = \dfrac{mv^{2}}{r}$, bottom $T - mg = \dfrac{mv^{2}}{r}$, minimum speed at top $v_{\text{min}} = \sqrt{gr}$, energy link $v_{\text{bottom}}^{2} = v_{\text{top}}^{2} + 4gr$.

Conical pendulum / banked track: $T\cos\theta = mg$, $T\sin\theta = \dfrac{mv^{2}}{r}$, $\tan\theta = \dfrac{v^{2}}{rg}$, $r = L\sin\theta$.

Flat-road skid limit: $v_{\text{max}} = \sqrt{\mu r g}$. Orbit: $v = \sqrt{gr}$, $T = \dfrac{2\pi r}{v}$.

### Key definitions (word for word)

- **Radian**: the angle subtended at the centre of a circle by an arc equal in length to the radius.
- **Angular velocity**: rate of change of angular displacement, in $\text{rad s}^{-1}$.
- **Centripetal acceleration**: acceleration of an object moving in a circle, directed towards the centre, perpendicular to the velocity.
- **Centripetal force**: the resultant force on an object moving in a circle, directed towards the centre (perpendicular to the velocity). It is supplied by a real force: tension, friction, gravity, or a normal contact force.

### Conversions to do instantly

- degrees to radians: $\times \pi/180$
- rpm to $\text{rad s}^{-1}$: divide by 60, then $\times 2\pi$
- cm to m, g to kg: always
- orbital radius: height above surface + planet radius

### Common traps

- Forgetting to convert degrees to radians before using $\theta = \omega t$ or any angular formula.
- Mixing up $\omega$ and $f$: they differ by a factor of $2\pi$. $\omega = 2\pi f$, never $\omega = f$.
- Writing the centripetal force pointing outwards. It always points towards the centre. There is no "centrifugal force" in the 9702 syllabus.
- Answering a definition question with an equation. "Rate of change of angular displacement" earns the mark; "$\omega = \Delta\theta/\Delta t$" alone often does not.
- Saying the centripetal force "balances" the weight or is a third force. It is the resultant of the real forces.
- Using the diameter where the radius is needed (loop of diameter 62 cm has $r = 0.31$ m).
- Using surface gravity for an orbit at height; use $g$ at the orbital radius.
- Not showing the substitution in "show that" questions. Full substitution is required, including all constants.
- Premature rounding of intermediate values; carry at least one extra significant figure through your working.
- Using $T$ for both tension and period in the same solution; label one clearly (for example "period $= 0.62$ s").
- Forgetting that in uniform circular motion the speed is constant but the velocity is not: the object is accelerating and not in equilibrium.
- Saying "the centripetal force does work". It does no work because it is perpendicular to the displacement.

## 7. Common Exam Mistakes

These come from the actual CAIE Principal Examiner Reports for Teachers for the sessions where circular motion was examined.

### From the November 2021 Paper 42 report (toy car on a vertical loop)

- Definitions were too vague. Candidates defined centripetal acceleration by quoting an equation, or by using the word "centripetal" inside the definition ("the acceleration caused by the centripetal force"). The mark scheme wanted "acceleration perpendicular to velocity".
- Candidates treated the centripetal force as an extra force that has to "balance" the weight. Very few understood that the centripetal force is the **resultant of the weight and the normal contact force** from the track. This was the single most damaging misunderstanding on the paper.
- Many candidates did not appreciate that the car moves more slowly at the top of the loop (Y) than at the bottom (X), so its centripetal acceleration is smaller at Y than at X.
- Many candidates thought a greater mass means a greater centripetal acceleration. Mass cancels in $mg = mv^{2}/r$, so the acceleration and the conclusion are independent of mass.
- In the "is the car in contact" calculation, candidates knew $a = v^{2}/r$ but did not apply conservation of energy to find the speed at the top of the loop first.

### On the Paper 41-style track comparison (same friction limit, different radius)

No examiner report exists for the November 2021 Paper 41 session (too few candidates), so treat this as a weak spot to train, not a quoted examiner complaint. The comparison table in the two-cars question requires three careful steps: with the same maximum friction force $F$ and the same mass, the centripetal acceleration is the same ($a = F/m$); the maximum speed is greater on the larger radius ($v_{\text{max}} = \sqrt{Fr/m}$); and the lap time is also greater ($t = 2\pi r/v = 2\pi\sqrt{mr/F}$). Getting "same / greater / greater" right requires tracking what is fixed and what changes, which is exactly the reasoning candidates found hard.

### From the May/June 2023 Paper 41 report (steel sphere on a spring, horizontal circle)

- Candidates did not refer to the components of the tension. Many referred to components of the weight, or treated the centripetal force as a third force acting on the sphere rather than the resultant of the tension and the weight.
- Some candidates thought the sphere was oscillating from side to side like a pendulum instead of moving in horizontal circles. Failing to see the tension components at the start led to wrong numerical methods later.
- In the "show that" question, candidates did not show their working clearly enough: a numerical value for the weight appeared without the evidence that it came from mass times gravitational field strength.
- In the spring-constant part, candidates used the total tension (3.2 N) instead of the extra tension above equilibrium ($3.2 - 0.29 \times 9.81$), and the total length instead of the extra extension.
- In the period calculation, candidates tried circular-motion equations where $F = ma$ with the horizontal component of the tension was the required first step, then found the equations worked once the acceleration was known.

### General warnings that apply to this chapter (from the same reports)

- Use technical language accurately; "centripetal" is an adjective describing a direction, not the name of a force.
- Show your reasoning line by line. Correct working with a wrong final answer can earn method marks; an unsupported number cannot.
- Match the significant figures of the data, and do not round intermediate values prematurely.
- Read the question: answers to a question that was not asked (often recycled from memorised mark schemes) get no credit.
- Definitions need to be dimensionally and conceptually complete; "per unit time", "towards the centre" and "resultant force" are the phrases the mark schemes look for.

---

Sources used: CAIE 9702 syllabus for 2022-2024 (official syllabus document), the Cambridge International A Level Physics coursebook Chapter 17 (the source chapter), CAIE question papers and published mark schemes for 9702/41/O/N/21, 9702/42/O/N/21 and 9702/41/M/J/23, the Principal Examiner Reports for November 2021 and June 2023, and TheLucidSTEM Paper 4 practice set for Topic 12.
