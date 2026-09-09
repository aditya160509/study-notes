# Physics — All Formulas & Definitions (Master Sheet)

> **Copied verbatim** from each chapter's **Definition Sheet (§2)** and **Formula Sheet (§3)** in the physics notes.
> Originals in `physics/notes/` are **unchanged** — this file is a compiled reference in chapter order.
> Source files: chapter-17-circular-motion-notes.md, chapter-18-gravitational-fields-notes.md, chapter-19-oscillations-notes.md, chapter-21-thermal-physics-notes.md, chapter-22-ideal-gases-notes.md, chapter-23-coulombs-law-notes.md, chapter-24-capacitance-notes.md, chapter-25-electronics-notes.md, chapter-26-magnetic-fields-and-electromagnetism-notes.md, chapter-27-charged-particles-notes.md, chapter-28-electromagnetic-induction-notes.md, chapter-29-alternating-currents-notes.md

---

## Contents
- **Chapter 17: Circular Motion** — `chapter-17-circular-motion-notes.md`
- **Chapter 18: Gravitational Fields** — `chapter-18-gravitational-fields-notes.md`
- **Chapter 19: Oscillations** — `chapter-19-oscillations-notes.md`
- **Chapter 21: Thermal Physics** — `chapter-21-thermal-physics-notes.md`
- **Chapter 22: Ideal Gases** — `chapter-22-ideal-gases-notes.md`
- **Chapter 23: Coulomb's Law and Electric Fields** — `chapter-23-coulombs-law-notes.md`
- **Chapter 24: Capacitance** — `chapter-24-capacitance-notes.md`
- **Chapter 25: Electronics** — `chapter-25-electronics-notes.md`
- **Chapter 26: Magnetic Fields and Electromagnetism** — `chapter-26-magnetic-fields-and-electromagnetism-notes.md`
- **Chapter 27: Charged Particles** — `chapter-27-charged-particles-notes.md`
- **Chapter 28: Electromagnetic Induction** — `chapter-28-electromagnetic-induction-notes.md`
- **Chapter 29: Alternating Currents** — `chapter-29-alternating-currents-notes.md`

---

# Chapter 17: Circular Motion
> Source: `physics/notes/chapter-17-circular-motion-notes.md`

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

---

# Chapter 18: Gravitational Fields
> Source: `physics/notes/chapter-18-gravitational-fields-notes.md`

## 2. Definition Sheet

Learn these word-for-word. Definitions open almost every Paper 4 question on this topic (1-2 marks each), and the mark schemes credit exact phrases: "force per unit mass", "work done per unit mass", "from infinity". A missing phrase such as "per unit mass" or "point masses" costs the mark.

### 2.1 Gravitational field

> A gravitational field is a region of space around a mass in which any other mass experiences a force of attraction. It is an example of a field of force.

- It exists in the space around a mass whether or not anything is there to feel it.
- The force is always attractive, and there is no way to shield against it.

### 2.2 Gravitational field strength

> The gravitational field strength at a point is the force per unit mass on a small object (test mass) placed at that point.

- Mark-scheme wording: **"force per unit mass"** is the exact phrase the examiner wants (9702/41/M/J/21 Q1(a)).
- Units: N kg$^{-1}$ (the same as m s$^{-2}$).
- It is a vector: it points towards the mass creating the field.
- Do not confuse it with gravitational potential - in 9702/s21 many candidates answered "define gravitational field strength" with the definition of gravitational potential. Field strength = **force** per unit mass; potential = **work done** per unit mass.

### 2.3 Gravitational potential

> The gravitational potential at a point is the work done per unit mass in bringing a mass from infinity to the point.

- Two B1 marks (9702/41/O/N/21 Q2(a), 9702/42/F/M/20 Q1(a)):
  1. **"work done per unit mass"**
  2. **"in moving a mass from infinity (to the point)"**
- $\phi = 0$ at infinity, and everywhere else $\phi < 0$ (always negative).
- It is a scalar - potentials from several masses simply add.
- Units: J kg$^{-1}$.
- Warning (9702/w21): "work done in moving a mass" without making clear it is *per unit mass* does not get the mark.

### 2.4 Gravitational potential energy

> The gravitational potential energy of a mass at a point is the work done in bringing the mass from infinity to that point.

- Equivalently, $E_P = m\phi$, where $\phi$ is the gravitational potential at the point.
- Zero at infinity, always negative everywhere else ($E_P = -\frac{GMm}{r}$); the more negative, the more tightly bound the mass.
- Units: J.
- Do not confuse potential energy with potential: potential energy = potential $\times$ mass, and they have different units (J vs J kg$^{-1}$).

### 2.5 Equipotential surface

> An equipotential surface is a surface on which the gravitational potential is the same (constant) at every point.

- No work is done moving a mass along an equipotential surface, because the potential energy does not change.
- Equipotential surfaces are perpendicular to the field lines at every point.
- Around a point mass they are concentric spheres; near the Earth's surface they are horizontal planes.

### 2.6 Escape velocity (escape speed)

> The escape velocity is the minimum speed a body needs, at a given point, to escape the gravitational field completely - to reach infinity with zero kinetic energy left over.

- $v = \sqrt{\frac{2GM}{R}}$ - it does not depend on the mass of the escaping body.
- It is not a separate syllabus line, but it is examined (e.g. 9702/41/O/N/13 Q1).

### 2.7 Geostationary orbit

> A geostationary orbit is an orbit in which the satellite remains above a fixed point on the Earth's surface: the orbital period is 24 hours, the orbit is directly above the Equator, and the satellite orbits from west to east.

The four features (2 marks, 9702/41/O/N/19 Q1(b)(i)):

1. Period **24 hours** (equal to the Earth's rotational period).
2. **Directly above the Equator**.
3. **From west to east** (same direction as the Earth's rotation).
4. Stays above the same point on the Earth's surface.

The examiner complains when candidates just rephrase feature 4 ("above the same point") instead of giving features 1-3.

### 2.8 Line of gravitational force (field line)

> A line of gravitational force is a line whose direction at every point gives the direction of the gravitational force on a mass placed at that point.

- The arrows point towards the mass creating the field.
- The spacing of the lines shows the field strength: closer lines = stronger field, more spread out lines = weaker field.
- Radial fields (around a point mass or sphere) have lines diverging from the centre; uniform fields (small region near the surface) have parallel, equally spaced lines.

### 2.9 Newton's law of gravitation (2-mark statement - learn it exactly)

> Any two point masses attract each other with a force that is directly proportional to the product of their masses and inversely proportional to the square of their separation.

- Mark scheme (9702/41/O/N/19 Q1(a), 9702/41/M/J/18 Q1(a)): one mark for the proportionality ideas, one mark for **"point masses"**.
- Omitting "point masses" was the most common omission in otherwise well-answered questions (9702/w19) - do not forget it.

---

## 3. Formula Sheet

| Formula | Meaning of symbols | SI units | When to use it |
|---|---|---|---|
| $$F = \frac{GMm}{r^2}$$ | $F$ = gravitational force, $G = 6.67 \times 10^{-11}$ N m$^2$ kg$^{-2}$, $M$, $m$ = masses, $r$ = centre-to-centre separation | N, kg, m | Force of attraction between two point masses / uniform spheres |
| $$g = \frac{F}{m}$$ | $g$ = field strength, $F$ = force on mass $m$ | N kg$^{-1}$ (= m s$^{-2}$) | Definition of gravitational field strength |
| $$g = \frac{GM}{r^2}$$ | $M$ = mass creating the field, $r$ = distance from its centre | N kg$^{-1}$ | Field strength due to a point/spherical mass, at or above the surface |
| $$\phi = -\frac{GM}{r}$$ | $\phi$ = gravitational potential, $M$ = mass, $r$ = distance from centre | J kg$^{-1}$ | Potential at a point in the field of one mass |
| $$E_P = m\phi = -\frac{GMm}{r}$$ | $E_P$ = gravitational potential energy of mass $m$ | J | Potential energy of a mass in a field; always negative |
| $$\Delta E_P = GMm\left(\frac{1}{r_1} - \frac{1}{r_2}\right)$$ | $r_1$, $r_2$ = initial and final distances from centre | J | Work done moving a mass between two radii (use $r_1 < r_2$ for lifting) |
| $$v = \sqrt{\frac{GM}{r}}$$ | $v$ = orbital speed, $M$ = central mass, $r$ = orbital radius | m s$^{-1}$ | Speed of a satellite/planet in a circular orbit |
| $$v = \frac{2\pi r}{T}$$ | $T$ = orbital period | m s$^{-1}$ | Speed from period and radius (circumference / time) |
| $$T^2 = \frac{4\pi^2 r^3}{GM}$$ | $T$ = orbital period | s | Kepler's third law; period from orbital radius |
| $$r^3 = \frac{GMT^2}{4\pi^2}$$ | $r$ = orbital radius | m | Orbital radius from period (geostationary orbit problems) |
| $$v_{\text{esc}} = \sqrt{\frac{2GM}{R}}$$ | $v_{\text{esc}}$ = escape speed, $R$ = radius at launch point | m s$^{-1}$ | Minimum speed to escape a gravitational field |
| $$g = -\frac{d\phi}{dr}$$ | potential gradient | N kg$^{-1}$ | Field strength from a $\phi$-$r$ graph; relationship between $g$ and $\phi$ |
| $$\frac{g_h}{g_0} = \left(\frac{R}{R+h}\right)^2$$ | $g_0$ = surface value, $g_h$ = value at height $h$ | dimensionless | Ratio questions: field strength at height vs surface |
| $$\rho = \frac{M}{\frac{4}{3}\pi R^3}$$ | $\rho$ = mean density, $M$ = mass, $R$ = radius | kg m$^{-3}$ | Finding planet density from $g$ and $R$ |
| $$\Delta E_P = mg\Delta h$$ | near-surface approximation, $\Delta h$ = height change | J | Only when $g$ is essentially constant (small heights) |

Supporting equations from Chapter 17 (circular motion) that you must be ready to combine:

- Centripetal force: $F = \frac{mv^2}{r} = mr\omega^2$
- Angular speed: $\omega = \frac{2\pi}{T}$

Constants and data you should recognise (given in questions):

- $G = 6.67 \times 10^{-11}$ N m$^2$ kg$^{-2}$
- Earth: mass $M = 6.0 \times 10^{24}$ kg, radius $R = 6.4 \times 10^6$ m, surface $g = 9.81$ N kg$^{-1}$
- Moon: mass $7.35 \times 10^{22}$ kg, radius $1.74 \times 10^6$ m
- Geostationary orbit: $T = 86400$ s, $r = 4.23 \times 10^7$ m from Earth's centre

---

---

# Chapter 19: Oscillations
> Source: `physics/notes/chapter-19-oscillations-notes.md`

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

---

# Chapter 21: Thermal Physics
> Source: `physics/notes/chapter-21-thermal-physics-notes.md`

## 2. Definition Sheet

Learn these word-perfect - the examiner's mark schemes quote them almost exactly, and the words that carry the marks are in bold. The mark-scheme wording is given where it is known from past papers.

> **Thermal equilibrium** - no net transfer of thermal energy between two objects in contact at the same temperature.

The syllabus puts it as "regions of equal temperature are in thermal equilibrium". The examiner wants the idea that at the same temperature there is no net transfer of energy. Related idea worth knowing: the zeroth law of thermodynamics - if A is in thermal equilibrium with B, and B with C, then A is in thermal equilibrium with C.

> **Thermodynamic temperature** - temperature measured on a scale that does not depend on the property of any particular substance; it is proportional to the average kinetic energy of the molecules of the substance.

This is why all thermometers agree on the thermodynamic scale: it is not defined by the expansion of any one liquid or the resistance of any one metal.

> **Kelvin** - the unit of thermodynamic temperature; $1\,\text{K}$ is $\frac{1}{273.16}$ of the thermodynamic temperature of the triple point of water.

A change of $1\,\text{K}$ equals a change of $1^\circ\text{C}$, but absolute temperatures are not interchangeable: $T/\text{K} = \theta/^\circ\text{C} + 273.15$.

> **Absolute zero** - the lowest possible temperature, $0\,\text{K} = -273.15^\circ\text{C}$, at which no more energy can be removed from a substance.

At absolute zero the molecules have minimum kinetic energy (and minimum electrical potential energy). It is not strictly true that matter has "no energy left" - the correct statement is that no more energy can be removed.

> **Specific heat capacity** - the energy required per unit mass of a substance to raise its temperature by $1\,\text{K}$ (or $1^\circ\text{C}$).

Mark-scheme wording: "(thermal) energy per unit mass (to raise temperature by) 1 K". Units: $\text{J kg}^{-1}\text{K}^{-1}$. The three elements that carry marks: energy, unit mass, and temperature rise of 1 K.

> **Specific latent heat** - the energy required per kilogram of a substance to change its state without any change in temperature.

Mark-scheme wording (w19/41 Q3(a), full marks): "(thermal) energy per (unit) mass (to change state); heat transfer during a change of state at constant temperature." You must include both the per-unit-mass idea and the constant-temperature condition.

> **Specific latent heat of fusion** - the (thermal) energy required to convert unit mass of solid to liquid at its normal melting point / without any change in temperature.

Mark-scheme note (w08/04 Q2(a)): merely saying "per 1 kg of ice to water" scores at most 1 mark - "unit mass" **and** the constant-temperature condition are both required.

> **Specific latent heat of vaporisation** - the (thermal) energy required to convert unit mass of liquid to gas at its normal boiling point / without any change in temperature.

The only difference from fusion is the change of state: liquid to gas (boiling) instead of solid to liquid (melting).

> **Internal energy** - the sum of the random distribution of kinetic and potential energies of the atoms or molecules of the system.

Mark-scheme note (November 2009 examiner report): almost everyone says "the sum of the kinetic and potential energies associated with the molecules", but very few say the **random distribution** - that phrase is in the syllabus definition, so use it. The kinetic part comes from molecular motion; the potential part is the electrical potential energy due to the positions of, and bonds between, the molecules.

> **First law of thermodynamics** - the increase in internal energy of a system equals the energy transferred to the system by heating plus the work done on the system: $\Delta U = q + W$.

Mark-scheme wording (w08/04 Q4(a)): "$\Delta U = q + w$" (a correct word equation is also accepted). Cambridge sign convention: $q$ is positive when energy is transferred **to** the system by heating; $W$ is positive when work is done **on** the system; $\Delta U$ is the **increase** in internal energy. The words "to", "on" and "increase" carry the marks.

> **Evaporation** - the change of state from liquid to gas that takes place at any temperature at the surface of the liquid; the most energetic molecules escape, so the average kinetic energy (and hence the temperature) of the liquid falls.

The key contrast with boiling: evaporation occurs at any temperature and only at the surface; boiling occurs throughout the liquid at a fixed temperature for a given pressure. Evaporation cools the liquid because the fastest molecules leave - this is why you feel cold when wet in a breeze.

---

## 3. Formula Sheet

| Formula | Meaning of symbols | SI units | When to use |
|---|---|---|---|
| $T = \theta + 273.15$ | $T$ = thermodynamic temperature (K), $\theta$ = Celsius temperature ($^\circ\text{C}$) | K, $^\circ\text{C}$ | Converting Celsius to kelvin (round the factor to 273 in calculations) |
| $\theta = T - 273.15$ | same symbols | K, $^\circ\text{C}$ | Converting kelvin to Celsius |
| $\Delta T = \Delta\theta$ | a change of 1 K equals a change of 1 $^\circ\text{C}$ | K or $^\circ\text{C}$ | Inside $E = mc\Delta\theta$ either scale works |
| $\Delta U = q + W$ | $\Delta U$ = increase in internal energy (J); $q$ = energy transferred **to** the system by heating (J); $W$ = work done **on** the system (J) | J | The first law: tracking energy for any system (heating, compression, expansion) |
| $W = p\Delta V$ | $p$ = pressure (Pa), $\Delta V$ = change in volume ($\text{m}^3$) | J | Work done by/on a gas changing volume at constant pressure; sign depends on whether the gas expands (work done by gas, negative $W$ in the first law) or is compressed (work done on gas, positive $W$) |
| $E = mc\Delta\theta$ | $E$ = energy (J), $m$ = mass (kg), $c$ = specific heat capacity ($\text{J kg}^{-1}\text{K}^{-1}$), $\Delta\theta$ = temperature change (K or $^\circ\text{C}$) | J | Heating or cooling with no change of state |
| $c = \frac{E}{m\Delta\theta}$ | as above | $\text{J kg}^{-1}\text{K}^{-1}$ | Finding $c$ from experiment data |
| $E = mL$ | $E$ = energy (J), $m$ = mass (kg), $L$ = specific latent heat of fusion or vaporisation ($\text{J kg}^{-1}$) | J | Melting, boiling or any change of state at constant temperature |
| $L = \frac{E}{m}$ | as above | $\text{J kg}^{-1}$ | Finding $L$ from experiment data |
| $E = Pt$ | $E$ = energy supplied by a heater (J), $P$ = heater power (W), $t$ = time (s) | J | Electrical heating experiments: energy supplied by a heater at power $P$ for time $t$ |
| $P = VI$ | $P$ = heater power (W), $V$ = p.d. (V), $I$ = current (A) | W | Electrical heating experiments (energy supplied $= Pt$) |
| $P = mc \times \text{gradient}$ | gradient $= \Delta\theta/\Delta t$ of the temperature-time graph ($\text{K s}^{-1}$) | W | Finding $c$ from a $\theta$-$t$ graph |
| $L = \frac{P}{\Delta m/\Delta t}$ | $\Delta m/\Delta t$ = rate of mass loss ($\text{kg s}^{-1}$) | $\text{J kg}^{-1}$ | Finding $L$ from a boiling/boil-off experiment |
| $P_1t_1 - P_2t_2 = (m_1 - m_2)L$ | two runs at different heater powers over equal times | J | Eliminating the heat loss to surroundings when finding $L$ |

---

---

# Chapter 22: Ideal Gases
> Source: `physics/notes/chapter-22-ideal-gases-notes.md`

## 2. Definition Sheet

These are the definitions Cambridge mark schemes actually credit. Learn them word-perfect - definition questions are the cheapest marks in the paper.

> **Ideal gas** - a gas that obeys the equation of state $pV = nRT$ (or $\frac{pV}{T} = \text{constant}$, or $pV \propto T$) at all pressures and temperatures, for a fixed amount of gas with $n$ and $R$ constant.
> Mark-scheme wording (F/M/19): "gas obeys the formula $\frac{pV}{T} = \text{constant}$ (or $pV = nRT$); symbols $V$ and $T$ explained". If you write "follows $pV = nRT$", you must add "at all pressures and temperatures, with $n$ and $R$ constant" and define every symbol (June 2022 examiner report).

> **Mole** - the SI base unit of amount of substance: the amount of any substance that contains the same number of particles (atoms, molecules or ions) as there are atoms in 0.012 kg of carbon-12. In one word: the amount of substance containing $N_A$ particles.

> **Avogadro constant** - the number of particles (atoms, molecules or ions) in one mole of a substance: $N_A = 6.02 \times 10^{23}\ \text{mol}^{-1}$.

> **Boltzmann constant** - the gas constant per molecule: $k = \frac{R}{N_A} = 1.38 \times 10^{-23}\ \text{J K}^{-1}$. It connects the microscopic energy of a single molecule to the macroscopic temperature.

> **Mean-square speed** - the average (mean) of the squares of the speeds of all the molecules: $\langle c^2 \rangle = \frac{c_1^2 + c_2^2 + \cdots + c_N^2}{N}$. (Mark scheme answer for "what is meant by $\langle c^2 \rangle$": "mean-square speed (of atoms/molecules)".)

> **r.m.s. speed** - the square root of the mean-square speed: $c_{\text{r.m.s.}} = \sqrt{\langle c^2 \rangle}$. It is slightly larger than the plain average speed.

> **Mean translational kinetic energy of a molecule** - $\langle E_K \rangle = \frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}kT$: the average kinetic energy of a molecule due to its random translational motion. It is proportional to the thermodynamic temperature and independent of the mass or type of molecule.

> **Elastic collision** - a collision in which kinetic energy is conserved (no kinetic energy is lost). Nov 2021 mark scheme: "no loss of kinetic energy". Momentum conservation, or "energy is conserved" in general, does not score.

> **Brownian motion** - the erratic, jerky, random motion of a visible particle caused by continuous, uneven bombardment by the much smaller, faster molecules of the surrounding fluid. It is evidence that molecules exist and are in constant random motion.

> **Thermodynamic temperature** - temperature measured on the kelvin scale, $T\ (\text{K}) = \theta\ (^\circ\text{C}) + 273.15$. Absolute zero is $0\ \text{K} = -273.15\ ^\circ\text{C}$, the lowest possible temperature.

**The kinetic theory assumptions** (state any of these, phrased about molecules):

1. A gas contains a very large number of particles in continuous random motion.
2. The volume of the particles is negligible compared with the volume of the container.
3. Forces between particles are negligible except during collisions.
4. Collisions are perfectly elastic (no kinetic energy is lost).
5. The time of a collision is negligible compared with the time between collisions.
6. Molecules obey Newton's laws of motion.

Mark-scheme phrasing for "state two assumptions" [2]: "molecules have negligible volume (compared with the container)"; "no forces between molecules except during collisions"; "molecules are in random motion"; "collisions are instantaneous". Never write "the gas has negligible volume" - the theory is about the particles that make up the gas.

**Internal energy of an ideal gas** - all kinetic, no potential energy: the potential energy of the molecules is zero because there are no intermolecular forces (M/J/24 mark-scheme point). So $U = \frac{3}{2}NkT$.

---

## 3. Formula Sheet

| Formula (LaTeX) | Meaning of symbols | SI units | When to use |
|---|---|---|---|
| $$pV = nRT$$ | $p$ pressure, $V$ volume, $n$ number of moles, $R = 8.31\ \text{J K}^{-1}\ \text{mol}^{-1}$, $T$ thermodynamic temperature | Pa, $\text{m}^3$, mol, K | Equation of state, molar form. Find $p$, $V$, $n$ or $T$. |
| $$pV = NkT$$ | $N$ number of molecules, $k = 1.38 \times 10^{-23}\ \text{J K}^{-1}$ | Pa, $\text{m}^3$, -, K | Equation of state, molecular form. Find $N$ or $T$. |
| $$k = \frac{R}{N_A}$$ | $k$ Boltzmann constant, $R$ gas constant, $N_A = 6.02 \times 10^{23}\ \text{mol}^{-1}$ | $\text{J K}^{-1}$ | Converting between molar and molecular quantities. |
| $$N = nN_A$$ | $N$ number of particles, $n$ moles | -, mol | Mole to molecule count (mind atoms vs molecules). |
| $$n = \frac{m}{M_r}$$ | $m$ mass in g, $M_r$ molar mass in $\text{g mol}^{-1}$ | g, $\text{g mol}^{-1}$ | Mass to moles before using $pV = nRT$. |
| $$p_1V_1 = p_2V_2$$ | subscripts 1, 2 = before, after | any consistent units | Fixed mass, constant temperature (Boyle's law). |
| $$\frac{V_1}{T_1} = \frac{V_2}{T_2}$$ | | any consistent units | Fixed mass, constant pressure (Charles's law). |
| $$\frac{p_1V_1}{T_1} = \frac{p_2V_2}{T_2}$$ | | any consistent units | Fixed mass, all three change. |
| $$pV = \frac{1}{3}Nm\langle c^2 \rangle$$ | $\langle c^2 \rangle$ mean-square speed | Pa, $\text{m}^3$, kg | Links macroscopic $p$, $V$ to molecular $m$, $N$, speeds. |
| $$p = \frac{1}{3}\rho\langle c^2 \rangle$$ | $\rho$ density of gas | Pa, $\text{kg m}^{-3}$, $\text{m}^2\text{s}^{-2}$ | Find $\langle c^2 \rangle$ or $c_{\text{r.m.s.}}$ from density and pressure. |
| $$c_{\text{r.m.s.}} = \sqrt{\langle c^2 \rangle}$$ | r.m.s. speed | $\text{m s}^{-1}$ | Square-root the mean-square speed. |
| $$\langle E_K \rangle = \frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}kT$$ | mean translational KE per molecule | J | Mean KE of one molecule; find $T$ or $c_{\text{r.m.s.}}$. |
| $$c_{\text{r.m.s.}} = \sqrt{\frac{3kT}{m}} = \sqrt{\frac{3RT}{M}}$$ | $M$ molar mass in $\text{kg mol}^{-1}$ | $\text{m s}^{-1}$ | r.m.s. speed from temperature. |
| $$c_{\text{r.m.s.}} = \sqrt{\frac{3p}{\rho}}$$ | $p$ pressure, $\rho$ density | $\text{m s}^{-1}$ | r.m.s. speed from pressure and density. |
| $$U = \frac{3}{2}NkT = \frac{3}{2}nRT$$ | $U$ internal energy of ideal gas | J | Total kinetic energy of all molecules. |
| $$\Delta U = \frac{3}{2}Nk\Delta T$$ | $\Delta U$ internal energy change | J | Internal energy change for a temperature change. |
| $$T/\text{K} = \theta/^\circ\text{C} + 273.15$$ | | K, °C | Convert temperature before any substitution. |
| $$V_{\text{sphere}} = \frac{4}{3}\pi r^3$$ | $r$ radius of molecule | $\text{m}^3$ | Estimate volume occupied by molecules (FM19 Q2 style: radius $3.2 \times 10^{-11}$ m gives total occupied volume $4 \times 10^{-8}\ \text{m}^3$). |

---

---

# Chapter 23: Coulomb's Law and Electric Fields
> Source: `physics/notes/chapter-23-coulombs-law-notes.md`

## 2. Definition Sheet

Every definition you must know word-perfect for the exam. Learn these exactly - the wording is what the mark schemes award.

> **Electric field:** a field of force - a region of space in which a charge experiences an electric force. It is produced by electric charges.

> **Electric field strength:** the force per unit positive charge acting on a charge placed at that point.
>
> Mark scheme: "force per unit charge" (1 mark) plus "(force on a) positive charge" (1 mark). "Per unit charge" must be explicit.

> **Coulomb's law:** any two point charges exert an electrical force on each other that is proportional to the product of their charges and inversely proportional to the square of the distance between them.

> **Electric potential:** the work done per unit positive charge in bringing a small test charge from infinity to the point.
>
> Mark scheme: the definition must be dimensionally correct, i.e. work done per unit charge (energy per coulomb, $\text{J C}^{-1}$), not energy. "Work done in moving positive charge from infinity" also gains credit, and "from infinity" fixes the sign convention.

> **Electric potential energy:** the work done in bringing two point charges from infinity to their separation. For charges $Q$ and $q$ separated by $r$: $E_P = \frac{Qq}{4\pi\epsilon_0 r}$.

> **Equipotential (line or surface):** a line (or surface) on which the electric potential is constant. Field lines are always perpendicular to equipotentials, and no work is done moving a charge along one.

> **Uniform field:** a field in which the field strength is the same at every point; the field lines are parallel and equally spaced (for example between two charged parallel plates).

> **Line of force (field line):** a line drawn so that its direction at any point gives the direction of the force on a positive test charge. The spacing of the lines shows the field strength: closer lines mean a stronger field. Lines never cross and they meet conductors at right angles.

**Comparing electric and gravitational fields - the essay points (learn all of these):**

- Both are fields of force.
- Both obey inverse square laws for point sources: $F = \frac{GMm}{r^2}$ and $F = \frac{Q_1 Q_2}{4\pi\epsilon_0 r^2}$.
- Both have scalar potentials that are zero at infinity.
- Both have the same relationship between field strength and potential gradient: $g = -\frac{d\phi}{dr}$, $E = -\frac{dV}{dr}$.
- The crucial difference: gravity only attracts because mass is always positive, while electric charges come in two signs, so electric forces can attract or repel and electric potentials can be positive or negative.

## 3. Formula Sheet

**Quick reference (using the Coulomb constant $k = \frac{1}{4\pi\epsilon_0} = 8.99 \times 10^9 \text{ N m}^2 \text{ C}^{-2} \approx 9.0 \times 10^9$):**

$$F = \frac{kQ_1 Q_2}{r^2}, \qquad E = \frac{F}{Q}, \qquad F = qE, \qquad E = \frac{kQ}{r^2}, \qquad E = \frac{V}{d}, \qquad V = \frac{kQ}{r}, \qquad E_P = \frac{kQq}{r}, \qquad W = qV, \qquad W = qEd, \qquad E = -\frac{\Delta V}{\Delta r}$$

| Formula | Meaning of symbols | Units | When to use it |
| --- | --- | --- | --- |
| $$F = \frac{Q_1 Q_2}{4\pi\epsilon_0 r^2}$$ | $F$ force between charges, $Q_1$, $Q_2$ charges, $r$ separation (centre-to-centre), $\epsilon_0$ permittivity of free space | $F$ in N, $Q$ in C, $r$ in m, $\epsilon_0$ in $\text{F m}^{-1}$ | Force between two point charges or charged spheres (recall from memory; not on formula sheet) |
| $$E = \frac{F}{Q}$$ | $E$ field strength, $F$ force on charge $Q$ at that point | $\text{N C}^{-1}$ or $\text{V m}^{-1}$ | Definition of field strength; finding $E$ from a measured force |
| $$F = qE$$ | $F$ force on charge $q$ in field $E$ | N | Force on any charge placed in an electric field |
| $$E = \frac{Q}{4\pi\epsilon_0 r^2}$$ | $E$ field strength due to charge $Q$ at distance $r$ | $\text{V m}^{-1}$ | Field near a point charge or outside a charged sphere (recall from memory) |
| $$E = \frac{V}{d}$$ | $E$ field strength, $V$ p.d. between plates, $d$ plate separation | $\text{V m}^{-1}$ | Uniform field between parallel plates ONLY |
| $$V = \frac{Q}{4\pi\epsilon_0 r}$$ | $V$ potential due to charge $Q$ at distance $r$ | V | Potential near a point charge or charged sphere (given on formula sheet) |
| $$E_P = \frac{Qq}{4\pi\epsilon_0 r}$$ | $E_P$ potential energy of two charges $Q$, $q$ separated by $r$ | J | Energy of a system of two charges; work to bring charges together from infinity |
| $$W = qV$$ | $W$ work done moving charge $q$ through potential difference $V$ | J | Work/energy change when a charge moves between two potentials |
| $$W = qEd$$ | $W$ work done moving charge $q$ a distance $d$ along a uniform field $E$ | J | Moving a charge along the field direction in a uniform field (moving perpendicular to the field does no work) |
| $$E = -\frac{\Delta V}{\Delta r}$$ | $E$ field strength, $\Delta V$ change in potential over distance $\Delta r$ | $\text{V m}^{-1}$ | Field strength from a potential gradient (graph tangent or uniform field) |
| $$\frac{1}{4\pi\epsilon_0} \approx 9.0 \times 10^9 \text{ N m}^2 \text{ C}^{-2}$$ | Coulomb constant $k$ | $\text{N m}^2 \text{ C}^{-2}$ | Quick estimates; data sheet value $8.99 \times 10^9 \text{ m F}^{-1}$ |

Constants you will need (from the data sheet): $\epsilon_0 = 8.85 \times 10^{-12} \text{ F m}^{-1}$, $\frac{1}{4\pi\epsilon_0} = 8.99 \times 10^9 \text{ m F}^{-1}$, $e = 1.60 \times 10^{-19} \text{ C}$, $m_p = 1.67 \times 10^{-27} \text{ kg}$, $G = 6.67 \times 10^{-11} \text{ N m}^2 \text{ kg}^{-2}$.

**Exam fact:** the data sheet gives $\epsilon_0 = 8.85 \times 10^{-12} \text{ F m}^{-1}$ and $\frac{1}{4\pi\epsilon_0} = 8.99 \times 10^9 \text{ m F}^{-1}$, plus $e = 1.60 \times 10^{-19} \text{ C}$. The formula sheet provides $V = \frac{Q}{4\pi\epsilon_0 r}$, but NOT Coulomb's law or $E = \frac{Q}{4\pi\epsilon_0 r^2}$: you must recall those two from memory.

---

# Chapter 24: Capacitance
> Source: `physics/notes/chapter-24-capacitance-notes.md`

## 2. Definition Sheet

Every definition you must know word-perfect for the exam. Learn these exactly - the wording is what the mark schemes award.

> **Capacitance:** the charge stored on one plate per unit potential difference between the plates.
>
> Mark scheme: "charge stored" (1 mark) plus "per unit potential difference" (1 mark). Say "on one plate" to show you know the two plates carry equal and opposite charges; "charge on the capacitor" alone can lose the mark. The defining equation is $C = \frac{Q}{V}$, where $Q$ is the magnitude of the charge on each plate and $V$ is the p.d. between the plates.

> **Farad:** the capacitance of a capacitor that stores a charge of 1 coulomb on each plate when the potential difference between the plates is 1 volt. $1~\text{F} = 1~\text{C V}^{-1}$.

> **Dielectric:** the insulating material between the plates of a capacitor. Its job is to keep the plates insulated from each other so that charge cannot leak across.

> **Charging a capacitor:** connecting it to a supply makes electrons flow onto one plate and away from the other until the p.d. across the capacitor equals the e.m.f. of the supply. The capacitor is then fully charged and the charging current stops. The conventional current (flow of positive charge) is in the opposite direction to the electron flow.

> **Discharging a capacitor:** connecting the plates through a conductor allows the stored charge to flow back round the circuit. The current falls as the p.d. across the capacitor falls.

> **Charge stored on a capacitor:** the magnitude $Q$ of the charge on each plate. The two plates carry equal and opposite charges $+Q$ and $-Q$, so the net charge on the capacitor is zero.

> **Capacitors in parallel:** the p.d. is the same across each capacitor; the total charge is the sum of the charges on the individual capacitors; the total capacitance is the sum of the individual capacitances.

> **Capacitors in series:** each capacitor stores the same charge (charge is conserved and the isolated section between the capacitors stays uncharged); the p.d.s across the capacitors add to the supply p.d.; the reciprocal of the total capacitance is the sum of the reciprocals of the individual capacitances.

> **Energy stored in a capacitor:** $W = \frac{1}{2}QV = \frac{1}{2}CV^2 = \frac{Q^2}{2C}$. The energy is proportional to the square of the p.d.: doubling $V$ quadruples $W$.

## 3. Formula Sheet

**Quick reference:**

$$Q = VC, \qquad C = \frac{Q}{V}, \qquad W = \frac{1}{2}QV, \qquad W = \frac{1}{2}CV^2, \qquad W = \frac{Q^2}{2C}, \qquad C_{\text{total}} = C_1 + C_2 + \dots, \qquad \frac{1}{C_{\text{total}}} = \frac{1}{C_1} + \frac{1}{C_2} + \dots, \qquad C = 4\pi\epsilon_0 r, \qquad Q = It$$

| Formula | Meaning of symbols | Units | When to use it |
| --- | --- | --- | --- |
| $$Q = VC$$ | $Q$ charge on each plate, $V$ p.d. between plates, $C$ capacitance | $Q$ in C, $V$ in V, $C$ in F | Charge stored for a given p.d.; the fundamental relation |
| $$C = \frac{Q}{V}$$ | $C$ capacitance, $Q$ charge on one plate, $V$ p.d. | $C$ in F ($\text{F} = \text{C V}^{-1}$) | Definition of capacitance; finding $C$ from measured $Q$ and $V$ |
| $$W = \frac{1}{2}QV$$ | $W$ energy stored, $Q$ charge, $V$ p.d. | J | Energy when you know charge and p.d. (area under $V$-$Q$ graph) |
| $$W = \frac{1}{2}CV^2$$ | $W$ energy stored, $C$ capacitance, $V$ p.d. | J | Energy when you know capacitance and p.d. (the most common case) |
| $$W = \frac{Q^2}{2C}$$ | $W$ energy stored, $Q$ charge, $C$ capacitance | J | Energy when you know charge and capacitance |
| $$C_{\text{total}} = C_1 + C_2 + C_3 + \dots$$ | $C_{\text{total}}$ combined capacitance, $C_1$, $C_2$, ... individual capacitances | F | Capacitors in parallel (same p.d. across each) |
| $$\frac{1}{C_{\text{total}}} = \frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3} + \dots$$ | $C_{\text{total}}$ combined capacitance, $C_1$, $C_2$, ... individual capacitances | F | Capacitors in series (same charge on each); take the reciprocal at the end |
| $$C = 4\pi\epsilon_0 r$$ | $C$ capacitance of an isolated conducting sphere, $r$ its radius, $\epsilon_0$ permittivity of free space | $C$ in F, $r$ in m, $\epsilon_0$ in $\text{F m}^{-1}$ | Capacitance of an isolated sphere (Earth, Van de Graaff dome) |
| $$V = \frac{Q}{4\pi\epsilon_0 r}$$ | $V$ potential at the surface of an isolated sphere, $Q$ its charge, $r$ its radius | V | Potential at the surface of a charged sphere |
| $$Q = It$$ | $Q$ charge flowing, $I$ current, $t$ time | $Q$ in C, $I$ in A, $t$ in s | Charge as the area under a current-time graph |

Constants you will need: $\epsilon_0 = 8.85 \times 10^{-12}~\text{F m}^{-1}$; $\frac{1}{4\pi\epsilon_0} = 8.99 \times 10^9~\text{m F}^{-1}$ (use $9.0 \times 10^9$ for quick estimates).

Prefix conversions: $1~\text{F} = 10^3~\text{mF} = 10^6~\mu\text{F} = 10^9~\text{nF} = 10^{12}~\text{pF}$; so $\mu\text{F} \rightarrow \text{F}$ is $\times 10^{-6}$, $\text{nF} \rightarrow \text{F}$ is $\times 10^{-9}$, $\text{pF} \rightarrow \text{F}$ is $\times 10^{-12}$.

**Exam fact:** $Q = VC$ and the energy equations are given on the formula sheet (and can be derived from $Q = VC$ anyway), but $C = 4\pi\epsilon_0 r$ for a sphere is NOT: recall it from memory. $V = \frac{Q}{4\pi\epsilon_0 r}$ IS on the data sheet.

---

# Chapter 25: Electronics
> Source: `physics/notes/chapter-25-electronics-notes.md`

## 2. Definition Sheet

Every definition you must know word-perfect for the exam. Learn these exactly - the wording is what the mark schemes award.

> **Transducer:** a device that changes energy from one form into another.

> **Sensing device:** an electronic component with a property (usually resistance) that changes when a physical quantity such as temperature, light intensity or pressure changes. A sensing device is also called a transducer.

> Mark scheme: "a property that changes with a physical quantity" (1 mark); naming the property (resistance) can earn a second.

> **Light-dependent resistor (LDR):** a semiconductor component whose resistance decreases as the intensity of the light falling on it increases. Light photons of high enough frequency release electrons in the semiconductor, which conduct electricity.

> Mark scheme: "resistance decreases as light intensity increases" is the core phrase - many candidates reverse it.

> **Negative temperature coefficient (NTC) thermistor:** a semiconductor component whose resistance decreases as its temperature increases. The rise in temperature increases the number of free electrons, so the resistance falls.

> Mark scheme: "resistance decreases as temperature increases" earns the mark. The resistance-temperature graph is not linear (roughly exponential), so a measuring circuit must be calibrated.

> **Piezo-electric effect:** the production of a potential difference (electric field) between the faces of a crystal when the crystal is stressed and changes shape. Some crystals (e.g. quartz) show this effect because they contain positive and negative ions in a regular arrangement.

> Mark scheme: "stress/force applied to the crystal produces a voltage" - both ideas (stress and voltage) are needed.

> **Strain gauge:** a device for measuring strain, made from a thin metal wire zigzagging between thin sheets of plastic, whose resistance changes when it is stretched or compressed. For small changes the change in resistance is directly proportional to the change in length: $\delta R \propto \delta L$.

> Mark scheme: "longer and narrower" so $R = \frac{\rho L}{A}$ rises (1); the proportionality $\delta R \propto \delta L$ is the examinable result (1).

> **Strain:** the fractional change in length of a wire or surface, $\text{strain} = \frac{\delta L}{L}$. It is a ratio, so it has no units.

> **Operational amplifier (op-amp):** a high-gain voltage amplifier with two inputs - the inverting input $(-)$ and the non-inverting input $(+)$ - and one output. It amplifies the potential difference between its two inputs: $V_{\text{out}} = G_0 (V_+ - V_-)$, where $G_0$ is the open-loop voltage gain.

> **Open-loop voltage gain:** the voltage gain of the op-amp with no feedback loop connecting the output to the input: $G_0 = \frac{V_{\text{out}}}{V_+ - V_-}$. For an ideal op-amp it is infinite; real op-amps have gains around $10^5$.

> **Saturation:** the state of an op-amp when the required output voltage exceeds the supply voltage, so the output is fixed at (close to) the positive or negative supply voltage $+V_s$ or $-V_s$.

> Mark scheme: "output cannot exceed the supply voltage" is the essential idea.

> **Virtual earth:** the point at the inverting input of an inverting amplifier, which is at (almost) zero potential even though it is not physically connected to earth. Because the open-loop gain is very high and the non-inverting input is at $0~\text{V}$, the potential difference between the inputs is almost zero, so the inverting input is at almost $0~\text{V}$.

> Mark scheme: two marks usually: "the inverting input is at (almost) zero volts" (1) and "because the open-loop gain is very high / the input difference is driven to zero" (1). Saying the input is "connected to earth" loses the mark - it is not connected; no current flows into it.

> **Negative feedback:** the process of returning part (or all) of the output of a system (or amplifier) to its input, so that the output affects the input. In an op-amp, feeding the output back to the inverting input reduces the gain but increases stability, increases the bandwidth and reduces distortion.

> Mark scheme: "part of the output is connected back to the input" is the core idea (1 mark).

> **Inverting amplifier:** an amplifier in which the input signal is applied to the inverting input through a resistor $R_{\text{in}}$, with a feedback resistor $R_f$ from the output to the inverting input. The gain is $G = -\frac{R_f}{R_{\text{in}}}$; the output is inverted (out of phase by $180^\circ$) with respect to the input.

> **Non-inverting amplifier:** an amplifier in which the input signal is applied to the non-inverting input and part of the output is fed back to the inverting input through a potential divider ($R_1$ from output to inverting input, $R_2$ from inverting input to $0~\text{V}$). The gain is $G = 1 + \frac{R_1}{R_2}$; the output is in phase with the input.

> **Bandwidth:** the range of frequencies for which an amplifier's gain is constant (amplified by the same amount). An ideal op-amp has infinite bandwidth; negative feedback increases the bandwidth.

> **Slew rate:** the rate at which an op-amp's output can change. An ideal op-amp has an infinite slew rate (the output changes instantaneously, with no time delay).

> **Relay:** an electromagnetic switch in which a small current in a coil magnetises an iron core and closes contacts, completing a separate circuit that can carry large currents or voltages.

> **Calibration:** the process of relating the readings of a measuring instrument to known values of the quantity being measured (e.g. using a thermometer in a water bath to produce a calibration graph of voltmeter reading against temperature).

## 3. Formula Sheet

**Quick reference:**

$$ V_{\text{out}} = \frac{R_2}{R_1 + R_2} V_s, \qquad V_{\text{out}} = G_0 (V_+ - V_-), \qquad G = -\frac{R_f}{R_{\text{in}}}, \qquad G = 1 + \frac{R_1}{R_2}, \qquad \frac{\delta R}{R} = \frac{\delta L}{L} \text{ (area constant)}, \qquad \frac{\delta R}{R} = \frac{2\,\delta L}{L} \text{ (volume constant)}, \qquad \text{strain} = \frac{\delta L}{L}, \qquad R = \frac{\rho L}{A}, \qquad I = \frac{V}{R}, \qquad R = \frac{V_s - V_{\text{LED}}}{I} $$

| Formula | Meaning of symbols | Units | When to use it |
| --- | --- | --- | --- |
| $$V_{\text{out}} = \frac{R_2}{R_1 + R_2} V_s$$ | $V_{\text{out}}$ output p.d. across $R_2$, $R_1$ other resistor, $V_s$ supply p.d. | $V$, $\Omega$, $V$ | Sensor potential-divider circuits (LDR, thermistor, strain gauge in series with a fixed resistor) |
| $$V_{\text{out}} = G_0 (V_+ - V_-)$$ | $G_0$ open-loop voltage gain, $V_+$ potential at non-inverting input, $V_-$ potential at inverting input | V (gain dimensionless) | Op-amp with no feedback (comparator); deciding the output state |
| $$G = -\frac{R_f}{R_{\text{in}}}$$ | $G$ voltage gain, $R_f$ feedback resistor, $R_{\text{in}}$ input resistor | dimensionless | Inverting amplifier (output inverted, $180^\circ$ out of phase) |
| $$G = 1 + \frac{R_1}{R_2}$$ | $G$ voltage gain, $R_1$ feedback resistor, $R_2$ resistor from inverting input to $0~\text{V}$ | dimensionless | Non-inverting amplifier (output in phase); gain can never be less than 1 |
| $$\frac{\delta R}{R} = \frac{\delta L}{L}$$ | $\delta R$ change in resistance, $R$ original resistance, $\delta L$ change in length, $L$ original length | dimensionless | Strain gauge when the cross-sectional area is assumed constant |
| $$\frac{\delta R}{R} = \frac{2\,\delta L}{L}$$ | as above | dimensionless | Strain gauge in practice (volume stays constant, so the wire narrows as well) |
| $$\text{strain} = \frac{\delta L}{L}$$ | $\delta L$ extension, $L$ original length | dimensionless | Strain of a wire or bar; strain gauges glued to a surface measure the surface's strain |
| $$R = \frac{\rho L}{A}$$ | $R$ resistance, $\rho$ resistivity, $L$ length, $A$ cross-sectional area | $\Omega$, $\Omega~\text{m}$, m, $\text{m}^2$ | Explaining why stretching a wire changes its resistance |
| $$I = \frac{V}{R}$$ | $I$ current, $V$ p.d., $R$ resistance | A, V, $\Omega$ | Current through LDR, thermistor, relay coil, LED series resistor |
| $$R = \frac{V_s - V_{\text{LED}}}{I}$$ | $V_s$ op-amp output (or supply) voltage, $V_{\text{LED}}$ LED conducting voltage (about 2 V), $I$ required LED current | $\Omega$, V, V, A | Series resistor for an LED (subtract the LED's $2~\text{V}$!) |

Constants you may need: none specific to this chapter, but note the typical values: LED conducting voltage about $2~\text{V}$; LED current about $20~\text{mA}$; op-amp maximum output current about $25~\text{mA}$; real op-amp open-loop gain about $10^5$; input resistance up to $10^{12}~\Omega$ (typically $10^6~\Omega$); output resistance about $75~\Omega$.

**Exam fact:** the op-amp gain equations ($G = -R_f/R_{\text{in}}$ and $G = 1 + R_1/R_2$) and the strain-gauge proportionalities are NOT on the data sheet - recall them from memory. $I = V/R$ and $R = \rho L/A$ are standard material from earlier chapters (both effectively given). The potential divider formula is used so often that you should be able to write it without thinking.

---

# Chapter 26: Magnetic Fields and Electromagnetism
> Source: `chapter-26-magnetic-fields-and-electromagnetism-notes.md` (root `chapter-26-magnetic-fields-and-electromagnetism-notes.md` — copied here; originals unchanged)

## 2. Definition Sheet

Definitions worded to match 9702 mark schemes. The exact phrasing matters: examiners award marks for the key phrases in bold.

1. **Magnetic field** - a region of space in which a magnetic pole (or a moving charge or current-carrying conductor) experiences a force. All magnetic fields are produced by **moving charges**.
2. **Magnetic field lines** - lines used to represent a magnetic field; the direction of a line at a point shows the direction of the force on a free north pole placed there, and the closeness of the lines shows the field's strength. Lines come out of north poles and go into south poles.
3. **Magnetic flux density, $B$** - the magnetic flux density at a point in space is **the force experienced per unit length by a long straight conductor carrying unit current placed at right angles to the field** at that point. Unit: tesla (T).
4. **Tesla (definition)** - the magnetic flux density is **1 T when a wire carrying a current of 1 A placed at right angles to the magnetic field experiences a force of 1 N per metre** of its length. $1~\text{T} = 1~\text{N A}^{-1}\text{m}^{-1} = 1~\text{kg A}^{-1}\text{s}^{-2}$.
5. **Motor effect** - the force experienced by a current-carrying conductor placed in a magnetic field (because the field of the current interacts with the external field).
6. **Fleming's left-hand rule (motor rule)** - if the thumb and first two fingers of the **left** hand are held mutually at right angles, with the **First** finger pointing in the direction of the magnetic **Field** and the se**C**ond finger in the direction of the **Current**, then the thu**M**b points in the direction of the **Motion** (force).
7. **Right-hand grip rule** - grip a coil with the right hand, fingers curling in the direction of the current; the thumb points in the direction of the magnetic field lines inside the coil (towards the north pole).
8. **Right-hand rule (straight wire)** - grip a wire with the right hand, thumb pointing in the direction of the conventional current; the fingers curl around in the direction of the circular magnetic field lines.
9. **Uniform magnetic field** - a field in which the flux density is the same (in magnitude and direction) at every point; represented by parallel, equally spaced field lines (e.g. between two flat opposite poles).
10. **Electromagnet** - a solenoid (often with a soft-iron core) whose magnetic field is produced by an electric current and can be switched on and off.
11. **Current balance** - an apparatus that measures magnetic flux density by weighing (balancing) the magnetic force $F = BIL$ on a current-carrying conductor, using $B = \frac{F}{IL}$.
12. **Hall probe** - a device containing a thin strip of semiconductor that gives a voltage proportional to the magnetic flux density passing at right angles through its face; used to measure $B$.
13. **Parallel currents rule** - two parallel conductors carrying currents in the **same direction attract**; carrying currents in **opposite directions repel**.

## 3. Formula Sheet

| Quantity | Formula | Notes |
|---|---|---|
| Force on a conductor in a field | $F = BIL$ | Only when the field is at right angles to the current |
| Force at an angle | $F = BIL\sin\theta$ | $\theta$ is the angle between the field and the current |
| Magnetic flux density | $B = \frac{F}{IL}$ | Force per unit length per unit current, at right angles |
| Weight from a current balance | $F = mg$ | $\Delta m \times g$; the magnetic force equals the change in balance reading |
| Torque on a motor coil | $\text{torque} = Fd$ | Couple: force on one side $\times$ separation of the sides |
| Tesla in base units | $1~\text{T} = 1~\text{N A}^{-1}\text{m}^{-1} = 1~\text{kg A}^{-1}\text{s}^{-2}$ | From $B = \frac{F}{IL}$ |
| Current from charge flow | $I = \frac{Ne}{t}$ | $N$ electrons of charge $e$ passing per second |
| Force per metre between two long parallel wires | $\frac{F}{L} = BI$ | Wire 1's field at wire 2: $B = 2.0 \times 10^{-7}\frac{I}{x}$ |

**Constants you need:** electron charge $e = 1.60 \times 10^{-19}~\text{C}$, $g = 9.81~\text{m s}^{-2}$, and the field a distance $x$ (m) from a long straight wire carrying current $I$ (A) is $B = 2.0 \times 10^{-7}\frac{I}{x}$.

**Exam fact:** on the 9702 data sheet, the force equations are given as $F = BIL$ and $F = BQv$ (the latter is the force on a moving charge, Chapter 27). The $F = BIL\sin\theta$ form and the wire field $B = 2.0 \times 10^{-7}\frac{I}{x}$ are not listed - derive them from $F = BIL$ and the definitions when you need them.

---

# Chapter 27: Charged Particles
> Source: `physics/notes/chapter-27-charged-particles-notes.md`

## 2. Definition Sheet

Every definition you must know word-perfect for the exam. Learn these exactly - the wording is what the mark schemes award.

> **Magnetic force on a moving charge:** the force experienced by a charge moving through a magnetic field. Its magnitude is $F = BQv\sin\theta$, where $\theta$ is the angle between the velocity and the field; the force acts at right angles to both the velocity and the field.
>
> Mark scheme: "force is proportional to $B$, $Q$ and $v$" plus "at right angles to the velocity" for the direction. For an electron, $F = Bev$.

> **Fleming's left-hand rule:** with the thumb, first finger and second finger of the left hand at right angles, the first finger points in the direction of the magnetic field, the second finger in the direction of the conventional current (flow of positive charge), and the thumb in the direction of the force on the charge.
>
> Mark scheme: the trap is using the *conventional* current direction - for electrons the second finger points opposite to the motion. State all three assignments.

> **Right-hand palm rule:** with the right hand flat, fingers pointing along the velocity of a positive charge and the palm facing the field, the thumb points in the direction of the force. For negative charges, use the left hand or reverse the direction.

> **Specific charge (charge-to-mass ratio):** the charge of a particle divided by its mass, $\frac{Q}{m}$, in C kg$^{-1}$. For the electron, $\frac{e}{m_e} = 1.76 \times 10^{11}~\text{C kg}^{-1}$.
>
> Mark scheme: "charge per unit mass" - the word "specific" means "per unit mass".

> **Centripetal force:** the resultant force on a body moving in a circle, directed towards the centre of the circle, of magnitude $\frac{mv^2}{r}$. In a uniform magnetic field the magnetic force $BQv$ provides the centripetal force, so $r = \frac{mv}{BQ}$.

> **Velocity selector:** a device using crossed electric and magnetic fields at right angles to each other, through which only particles of speed $v = \frac{E}{B}$ pass undeflected, because for that speed the electric and magnetic forces balance.
>
> Mark scheme: both forces balance ($Eq = Bqv$); faster particles are beaten by the stronger magnetic force, slower ones by the electric force.

> **Hall effect:** the sideways deflection of charge carriers in a current-carrying conductor placed in a magnetic field at right angles to the current, causing charge to separate and a p.d. (the Hall voltage) to appear across the conductor.
>
> Mark scheme: "charge carriers pushed to one side by the magnetic force" plus "a p.d. appears across the conductor". The sign of $V_H$ identifies the sign of the carriers.

> **Hall voltage:** the p.d. that appears between the two opposite sides of a current-carrying strip in a magnetic field, $V_H = \frac{BI}{ntq}$.
>
> Mark scheme: $V_H \propto B$ for fixed current is the phrase that earns the mark in probe questions; "depends on thickness $t$, not width $d$" is the common follow-up.

> **Number density of charge carriers ($n$):** the number of free charge carriers per unit volume of a material, in m$^{-3}$. It links current to drift velocity via $I = nAqv$, and it is far smaller in semiconductors than in metals.

> **Drift velocity ($v$):** the average velocity of the charge carriers along a conductor when a current flows, $v = \frac{I}{nAq}$. For the same current, carriers in a semiconductor drift much faster than in a metal because $n$ is much smaller.

> **Crossed fields:** electric and magnetic fields applied in the same region at right angles to each other. Used in velocity selectors and in Thomson's method, where the two forces on a particle can be balanced so that it travels undeflected.

> **Thomson's method:** measuring $\frac{e}{m_e}$ by accelerating electrons through a known p.d. $V_{ca}$ (so $eV_{ca} = \frac{1}{2}m_ev^2$) and measuring the radius $r$ of their circular path in a known field $B$, giving $\frac{e}{m_e} = \frac{2V_{ca}}{B^2r^2}$.

> **Millikan's oil-drop experiment:** measured the elementary charge $e$ by balancing electric and gravitational forces on charged oil droplets; every droplet's charge was an integer multiple of $e = 1.60 \times 10^{-19}~\text{C}$.

## 3. Formula Sheet

**Quick reference:**

$$F = BQv\sin\theta, \qquad r = \frac{mv}{BQ}, \qquad p = BQr, \qquad eV = \frac{1}{2}mv^2, \qquad \frac{e}{m_e} = \frac{v}{Br} = \frac{2V}{B^2r^2}, \qquad v = \frac{E}{B}, \qquad E = \frac{V}{d}, \qquad V_H = \frac{BI}{ntq} = Bvd, \qquad I = nAqv$$

| Formula | Meaning of symbols | Units | When to use it |
| --- | --- | --- | --- |
| $$F = BQv\sin\theta$$ | $F$ magnetic force, $B$ flux density, $Q$ charge, $v$ speed, $\theta$ angle between velocity and field | $F$ in N, $B$ in T, $Q$ in C, $v$ in m s$^{-1}$ | Force on a charge moving in a magnetic field; at right angles $\theta = 90^{\circ}$ so $F = BQv$ |
| $$F = Bev$$ | $B$ flux density, $e$ elementary charge, $v$ speed | N | Force on an electron; also the "Bev force" behind the motor effect |
| $$r = \frac{mv}{BQ}$$ | $r$ orbit radius, $m$ mass, $v$ speed, $B$ flux density, $Q$ charge | $r$ in m, $m$ in kg, $v$ in m s$^{-1}$, $B$ in T, $Q$ in C | Radius of circular path of a charge in a uniform field (centripetal force $= BQv$) |
| $$p = BQr$$ | $p$ momentum, $B$ flux density, $Q$ charge, $r$ radius | kg m s$^{-1}$ | Momentum form of the orbit equation; the form on the data sheet |
| $$eV = \frac{1}{2}mv^2$$ | $e$ elementary charge, $V$ accelerating p.d., $m$ mass, $v$ speed | $V$ in V, $v$ in m s$^{-1}$ | Speed gained by an electron accelerated through a p.d. (work done $eV$ becomes kinetic energy) |
| $$\frac{e}{m_e} = \frac{2V}{B^2r^2}$$ | $e/m_e$ specific charge, $V$ accelerating p.d., $B$ flux density, $r$ radius | C kg$^{-1}$ | Charge-to-mass ratio of the electron from accelerating p.d. and orbit radius |
| $$v = \frac{E}{B}$$ | $v$ speed, $E$ electric field strength, $B$ flux density | $v$ in m s$^{-1}$, $E$ in V m$^{-1}$, $B$ in T | Speed of a particle passing undeflected through crossed fields (velocity selector) |
| $$E = \frac{V}{d}$$ | $E$ field strength between plates, $V$ p.d. between plates, $d$ plate separation | V m$^{-1}$ | Field between parallel plates; combine with $v = E/B$ to get $v = \frac{V}{Bd}$ |
| $$V_H = \frac{BI}{ntq}$$ | $V_H$ Hall voltage, $B$ flux density, $I$ current, $n$ number density of carriers, $t$ thickness, $q$ charge per carrier | $V_H$ in V, $B$ in T, $I$ in A, $n$ in m$^{-3}$, $t$ in m, $q$ in C | Hall voltage across a strip; for electrons use $q = e$. Thickness $t$, never the width |
| $$V_H = Bvd$$ | $V_H$ Hall voltage, $B$ flux density, $v$ drift velocity, $d$ width of strip | V | Hall voltage from drift velocity and width (equilibrium form, $qE = Bqv$) |
| $$I = nAqv$$ | $I$ current, $n$ number density, $A$ cross-sectional area, $q$ charge per carrier, $v$ drift velocity | $I$ in A, $A$ in m$^2$, $v$ in m s$^{-1}$ | Relating current to drift velocity; combine with the Hall derivation ($A = dt$) |

Constants you will need: $e = 1.60 \times 10^{-19}~\text{C}$; $m_e = 9.11 \times 10^{-31}~\text{kg}$; $\frac{e}{m_e} = 1.76 \times 10^{11}~\text{C kg}^{-1}$. Particle data from the chapter's questions: proton mass $= 1.67 \times 10^{-27}~\text{kg}$, charge $+e$; helium nucleus ($\alpha$-particle) mass $= 6.8 \times 10^{-27}~\text{kg}$, charge $+2e$; electron mass $\approx \frac{1}{1836}$ of the proton mass.

**Exam fact:** $F = BQv$ (including the $\sin\theta$ version) is given on the data sheet, and the orbit radius appears on the data sheet in the momentum form $p = BQr$. The rest of the chapter's key results - $v = \frac{E}{B}$ for the velocity selector, $V_H = \frac{BI}{ntq}$ for the Hall voltage, and $\frac{e}{m_e} = \frac{2V}{B^2r^2}$ - are built from $F = BQv$ plus formulas you already know ($E = \frac{V}{d}$, $eV = \frac{1}{2}mv^2$, $I = nAqv$). Learn to derive them quickly: the derivations are routinely asked as questions in their own right.

---

# Chapter 28: Electromagnetic Induction
> Source: `physics/notes/chapter-28-electromagnetic-induction-notes.md`

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

---

# Chapter 29: Alternating Currents
> Source: `physics/notes/chapter-29-alternating-currents-notes.md`

## 2. Definition Sheet

Every definition you must know word-perfect for the exam. Learn these exactly — the wording is what the mark schemes award.

> **Alternating current (a.c.):** a current whose direction reverses periodically. For the 9702 syllabus the variation is sinusoidal: $I = I_0 \sin \omega t$, where $I_0$ is the peak value and $\omega = 2\pi f$.
>
> Mark scheme: must convey periodic reversal of direction; for sinusoidal a.c. the sine-wave statement earns credit.

> **Peak value ($I_0$ or $V_0$):** the maximum instantaneous value of the alternating current or voltage in either direction (the amplitude of the sine wave). Read from the highest point on the $I$–$t$ or $V$–$t$ graph.
>
> Mark scheme: "maximum value" or "amplitude" (1 mark); must distinguish from r.m.s. or mean.

> **Period ($T$):** the time for one complete cycle of the alternating current or voltage, in seconds. $T = \frac{1}{f}$.

> **Frequency ($f$):** the number of complete cycles per unit time, in hertz (Hz). $f = \frac{1}{T}$ and $\omega = 2\pi f$.

> **Root-mean-square (r.m.s.) value:** the value of the **steady direct current (or voltage)** that would dissipate the **same mean power** in the same resistor as the alternating current (or voltage).
>
> Mark scheme: "steady d.c." / "direct current or voltage" (1 mark) + "same mean/average power (or heating effect) in the same resistor / resistive load" (1 mark). Saying "average current/voltage" without "steady d.c." loses the first mark. For sinusoidal a.c., $I_{\text{rms}} = \frac{I_0}{\sqrt{2}}$, $V_{\text{rms}} = \frac{V_0}{\sqrt{2}}$ — but the definition must be the heating equivalence, not just the formula.

> **Mean value of a.c.:** the average of the instantaneous current or voltage over one complete cycle. For a sinusoidal a.c. the mean over a full cycle is **zero** (positive half-cycle cancels the negative half-cycle).

> **Mean power:** the average rate at which energy is dissipated in a resistive load, $P = I_{\text{rms}}^2 R = \frac{V_{\text{rms}}^2}{R} = I_{\text{rms}} V_{\text{rms}}$. For a sine wave, peak power $= 2 \times$ mean power.

> **Transformer:** two coils (primary with $N_{\text{p}}$ turns, secondary with $N_{\text{s}}$ turns) wound on a soft iron core (laminated). There is no electrical connection between the coils; energy is transferred by the changing magnetic flux in the core via electromagnetic induction.
>
> **Turns-ratio equation:** $\frac{V_{\text{s}}}{V_{\text{p}}} = \frac{N_{\text{s}}}{N_{\text{p}}}$. For an ideal (100% efficient) transformer, $I_{\text{p}} V_{\text{p}} = I_{\text{s}} V_{\text{s}}$, so $\frac{I_{\text{s}}}{I_{\text{p}}} = \frac{N_{\text{p}}}{N_{\text{s}}}$.

> **Step-up transformer:** $N_{\text{s}} > N_{\text{p}}$, so $V_{\text{s}} > V_{\text{p}}$ and $I_{\text{s}} < I_{\text{p}}$ (for an ideal transformer).

> **Step-down transformer:** $N_{\text{s}} < N_{\text{p}}$, so $V_{\text{s}} < V_{\text{p}}$ and $I_{\text{s}} > I_{\text{p}}$.

> **Rectification:** the conversion of alternating current to direct current (current in one direction only).
>
> Mark scheme: "a.c. to d.c." / "current flows in one direction only" (1 mark).

> **Half-wave rectification:** rectification using a single diode: current flows for one half-cycle and is blocked for the other, so the output is zero for half the time.

> **Full-wave rectification:** rectification using a bridge of four diodes: both half-cycles are made to drive current the same way through the load, so the output is always $\ge 0$ and its frequency is twice the supply frequency.

> **Smoothing:** the reduction of the variation (ripple) in the rectified output by means of a capacitor connected **in parallel (across) the load**. The capacitor charges when the rectified voltage rises and discharges through the load when the rectified voltage falls, maintaining a steadier voltage.

> **Ripple:** the small residual variation in the smoothed output. Ripple decreases when $C$ or $R$ (hence $RC$) increases.

> **Cathode-ray oscilloscope (CRO):** displays voltage ($y$-axis) against time ($x$-axis). Y-gain / Y-sensitivity (in $\text{V cm}^{-1}$ or $\text{V div}^{-1}$) converts vertical deflection to voltage; time-base (in $\text{s cm}^{-1}$ or $\text{s div}^{-1}$) converts horizontal distance to time. The signal to the Y-input deflects the electron beam vertically; the time-base sweeps it horizontally.

> **Faraday's law of electromagnetic induction:** the induced e.m.f. is proportional to the rate of change of magnetic flux linkage: $E = N\frac{\Delta \Phi}{\Delta t}$ (magnitudes) or $E = -\frac{d(N\Phi)}{dt}$ with Lenz's sign.

## 3. Formula Sheet

**Quick reference:**

$$I = I_0 \sin \omega t, \qquad V = V_0 \sin \omega t, \qquad \omega = 2\pi f, \qquad f = \frac{1}{T}, \qquad I_{\text{rms}} = \frac{I_0}{\sqrt{2}}, \qquad V_{\text{rms}} = \frac{V_0}{\sqrt{2}}$$

$$P = I_{\text{rms}}^2 R = \frac{V_{\text{rms}}^2}{R} = I_{\text{rms}} V_{\text{rms}}, \qquad \frac{V_{\text{s}}}{V_{\text{p}}} = \frac{N_{\text{s}}}{N_{\text{p}}}, \qquad I_{\text{p}} V_{\text{p}} = I_{\text{s}} V_{\text{s}}\; (\text{ideal}), \qquad P_{\text{loss}} = I_{\text{rms}}^2 R_{\text{cable}}, \qquad \text{efficiency} = \frac{P_{\text{out}}}{P_{\text{in}}} \times 100\%$$

| Formula | Meaning of symbols | Units | When to use it |
|---|---|---|---|
| $$I = I_0 \sin \omega t$$ | $I$ instantaneous current, $I_0$ peak, $\omega$ angular frequency, $t$ time | $I$ in A, $\omega$ in $\text{rad s}^{-1}$, $t$ in s, $\omega t$ in rad | Instantaneous value; finding $I$ at a given $t$ or writing the equation from $I_0$ and $f$ |
| $$V = V_0 \sin \omega t$$ | $V$ instantaneous p.d., $V_0$ peak | $V$ in V | Instantaneous voltage; same use as above |
| $$\omega = 2\pi f = \frac{2\pi}{T}$$ | $\omega$ angular frequency, $f$ frequency, $T$ period | $\omega$ in $\text{rad s}^{-1}$, $f$ in Hz, $T$ in s | Converting between $\omega$, $f$ and $T$; argument of the sine is always $\omega t$ in radians |
| $$I_{\text{rms}} = \frac{I_0}{\sqrt{2}}$$ | $I_{\text{rms}}$ r.m.s. current, $I_0$ peak | A | Sinusoidal a.c. only; heating-equivalence value |
| $$V_{\text{rms}} = \frac{V_0}{\sqrt{2}}$$ | $V_{\text{rms}}$ r.m.s. voltage, $V_0$ peak | V | Sinusoidal a.c. only; mains $230~\text{V}$ is this value |
| $$P = I_{\text{rms}}^2 R = \frac{V_{\text{rms}}^2}{R} = I_{\text{rms}} V_{\text{rms}}$$ | $P$ mean power, $R$ resistance | W | Mean power in a resistive load — always use r.m.s. values |
| $$\frac{V_{\text{s}}}{V_{\text{p}}} = \frac{N_{\text{s}}}{N_{\text{p}}}$$ | $V_{\text{s}}, V_{\text{p}}$ secondary/primary voltages, $N_{\text{s}}, N_{\text{p}}$ turns | V, dimensionless | Any transformer; same ratio for r.m.s. or peak |
| $$I_{\text{p}} V_{\text{p}} = I_{\text{s}} V_{\text{s}}$$ | $I_{\text{p}}, I_{\text{s}}$ primary/secondary currents | A·V = W | Ideal (100% efficient) transformer only; power in = power out |
| $$P_{\text{loss}} = I_{\text{rms}}^2 R_{\text{cable}}$$ | $P_{\text{loss}}$ power lost as heat in cables, $R_{\text{cable}}$ cable resistance | W | Transmission losses; explains why high $V$ / low $I$ is used |
| $$\text{efficiency} = \frac{I_{\text{s}} V_{\text{s}}}{I_{\text{p}} V_{\text{p}}} \times 100\%$$ | Output power / input power | % | Real transformers; $P_{\text{out}} < P_{\text{in}}$ |
| $$V_0 = (\text{vertical amplitude}) \times (\text{Y-gain})$$ | From CRO trace | V | Reading peak voltage from the screen |
| $$T = (\text{horizontal length of one cycle}) \times (\text{time-base})$$ | From CRO trace | s | Reading period from the screen |
| $$E = N\frac{\Delta \Phi}{\Delta t}$$ | Faraday's law: $E$ induced e.m.f., $N\Phi$ flux linkage | V, Wb | Explaining the transformer; phase of flux vs e.m.f. |

Constants you will need: $\sqrt{2} = 1.414$; $\frac{1}{\sqrt{2}} = 0.707$; $2\pi = 6.28$.

**Exam fact:** $I_{\text{rms}} = I_0/\sqrt{2}$ and $V_{\text{rms}} = V_0/\sqrt{2}$ are the only r.m.s. formulas in the syllabus — they apply only to **sinusoidal** waveforms. For any other waveform you must use the definition: find the steady d.c. that gives the same mean power.

---
