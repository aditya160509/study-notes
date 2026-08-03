# Chapter 18: Gravitational Fields - CAIE A Level Physics (9702) Study Notes

> **Exam reality check**: Gravitational fields is a Paper 4 (A2 structured questions) topic. In the 2016-2021 sessions it was Question 1 on almost every Paper 4 paper, worth 8-10 marks. You will be asked to do a definition (1-2 marks), a calculation or two (3-4 marks each), and an explanation (1-3 marks). The most common data: Earth mass $M = 6.0 \times 10^{24}$ kg, Earth radius $R = 6.4 \times 10^6$ m, $G = 6.67 \times 10^{-11}$ N m$^2$ kg$^{-2}$.

---

## 1. Theory

### 1.1 What a gravitational field is

Every mass creates a gravitational field in the space around it. Any other mass placed in that field experiences a force. The Moon orbits the Earth because the Earth's gravitational field pulls on it; the Earth orbits the Sun because of the gravitational field of the Sun. A gravitational field is a **field of force**: it exists in the space around a mass, whether or not anything is there to feel it.

- The gravitational force is always **attractive** (unlike electric forces, which can attract or repel).
- Gravitational fields act on anything with mass, so there is no way to "shield" against gravity.

### 1.2 Field lines

Field lines (lines of force) show two things:

- **Direction**: the arrows on the field lines show the direction of the gravitational force on a mass placed in the field. For the Earth, all arrows point towards the centre.
- **Strength**: the spacing of the field lines indicates the strength of the field. Closer lines = stronger field; more spread out lines = weaker field.

Two important field shapes:

- **Radial field**: the field of the Earth (or any sphere, point mass, star, planet) is radial - the field lines diverge outwards from the centre. The field strength obeys an inverse square law with distance: double the distance from the centre and $g$ drops to a quarter, because the same number of field lines is spread over four times the surface area.
- **Uniform field**: on the scale of a building (or any small region near the surface), the field lines are parallel and equally spaced, so the field strength is the same at every point. That is why your weight is (very nearly) the same on the ground floor and the top floor: $g$ is constant in a uniform field.

**Key fact**: for any point *outside* a uniform sphere, the sphere behaves as if its entire mass were concentrated at its centre (a point mass). So the Earth's field at any point above its surface is the same as the field of a point mass $M$ at the Earth's centre. This is syllabus point 13.2.1 and it is the justification for every equation in this chapter.

### 1.3 Newton's law of gravitation

**Statement (learn this exactly, it is a 2-mark definition question):**

> Any two point masses attract each other with a force that is directly proportional to the product of their masses and inversely proportional to the square of their separation.

As an equation:

$$F = \frac{GMm}{r^2}$$

where:

- $F$ = gravitational force of attraction between the two masses (N)
- $G$ = the gravitational constant (also called the universal gravitational constant) $= 6.67 \times 10^{-11}$ N m$^2$ kg$^{-2}$
- $M$, $m$ = the two masses (kg)
- $r$ = the distance between the centres of the two masses (m)

Things to know:

- The force is attractive, so it points along the line joining the two masses, towards the other mass.
- By Newton's third law, the two masses experience equal and opposite forces.
- The law applies to **point masses**, or to uniform spheres provided you measure $r$ between their centres. You will often see it as $F = \frac{Gm_1 m_2}{r^2}$.
- $G$ is a universal constant - believed to be the same value throughout the Universe.
- If you double $r$, the force drops to $\frac{1}{4}$. If you double one mass, the force doubles.

### 1.4 Gravitational field strength $g$

**Definition (1-mark question - learn it exactly):**

> The gravitational field strength at a point is the gravitational force exerted per unit mass on a small object placed at that point.

$$g = \frac{F}{m}$$

- $g$ = gravitational field strength (N kg$^{-1}$, which is the same unit as m s$^{-2}$)
- $F$ = gravitational force on the object (N)
- $m$ = mass of the object (kg)

$g$ is a **vector**: it points towards the centre of the mass creating the field. The value $g = 9.81$ N kg$^{-1}$ near the Earth's surface is the familiar acceleration of free fall - every freely falling object accelerates at $9.81$ m s$^{-2}$ regardless of its mass.

**Field strength due to a point (or spherical) mass** - combine $F = \frac{GMm}{r^2}$ with $g = \frac{F}{m}$:

$$g = \frac{GM}{r^2}$$

- $M$ = mass of the body creating the field (kg)
- $r$ = distance from the centre of that body to the point (m)

Notes:

- $g$ does not depend on the mass of the object placed in the field.
- $g$ obeys an inverse square law with distance from the centre of the mass.
- The field of a more massive planet (Jupiter) is represented by more closely spaced field lines.

**Why $g$ is roughly constant near the surface (syllabus 13.3.3):** on or near the Earth's surface, $r$ changes by only a tiny fraction of the Earth's radius when you change height. The fractional change in $g$ is $\frac{\Delta g}{g} = -\frac{2\Delta h}{r}$. For Mount Everest (about 9 km high), $\frac{2 \times 9000}{6.4 \times 10^6} \approx 0.3\%$ - so a 100 kg mountaineer loses only about 0.3 kg of "weight" (about 3 N) at the summit, which bathroom scales would not reliably show.

### 1.5 Gravitational potential

The problem with $mg\Delta h$ is that it assumes $g$ is constant and picks the Earth's surface as the zero of energy. For objects moving through space this is useless: $g$ changes with height, and there is nothing special about the Earth's surface. So we define a zero of gravitational potential energy at **infinity** (an infinite distance from all masses).

**Definition (2-mark question - learn it exactly):**

> The gravitational potential at a point is the work done per unit mass in bringing a mass from infinity to the point.

$$\phi = -\frac{GM}{r}$$

- $\phi$ = gravitational potential (J kg$^{-1}$)
- $M$ = mass creating the field (kg)
- $r$ = distance from the centre of $M$ to the point (m)

Key points:

- **$\phi$ is always negative.** Work is *done by* the field (or equivalently, energy is *released*) as a mass is pulled in from infinity, so the potential decreases below zero. Since $\phi = 0$ at infinity, everywhere else $\phi < 0$.
- $\phi$ is a **scalar** (it has no direction), so potentials from several masses simply add as numbers - this is a favourite trap, see Section 7.
- The potential at the Earth's surface is about $-6.3 \times 10^7$ J kg$^{-1}$; at the Moon's surface about $-2.8 \times 10^6$ J kg$^{-1}$. The Earth's "potential well" is much deeper, which is why launching from the Moon needs a much smaller rocket.
- A useful way to picture it: the field creates a giant "potential well" in space; we live at the bottom of the Earth's well, and the Sun's well is much deeper.

### 1.6 Gravitational potential energy

The gravitational potential energy of a mass $m$ at a point where the potential is $\phi$ is:

$$E_P = m\phi$$

For the field of a point mass $M$:

$$E_P = -\frac{GMm}{r}$$

- $E_P$ = gravitational potential energy (J)
- $M$, $m$ = the two masses (kg)
- $r$ = separation of their centres (m)

**Why it is negative:** we chose zero potential energy at infinity. As a mass moves closer to another mass, it loses potential energy (the field does work on it), so its potential energy goes below zero. Anywhere other than infinity, $E_P < 0$. The more negative the value, the more tightly bound the mass is.

**Change in potential energy between two radii** (this is what examiners actually ask for):

$$\Delta E_P = E_{P2} - E_{P1} = -\frac{GMm}{r_2} - \left(-\frac{GMm}{r_1}\right) = GMm\left(\frac{1}{r_1} - \frac{1}{r_2}\right)$$

- If $r_2 > r_1$ (mass moves further out), $\Delta E_P > 0$: potential energy **increases** (becomes less negative). This is exactly what you expect - you do work lifting a satellite into a higher orbit.
- If $r_2 < r_1$ (mass falls inwards), $\Delta E_P < 0$: potential energy decreases.

**Warning:** a common exam error is to write $\Delta E_P = GMm \left(\frac{1}{r_2 - r_1}\right)$. This is wrong - the bracketed term is $\frac{1}{r_1} - \frac{1}{r_2}$, not $\frac{1}{r_2 - r_1}$ (see 9702/s19 examiner report).

**Close to the surface**, the general formula reduces to the familiar one: for a small height change $\Delta h$ near the surface, $\Delta E_P \approx mg\Delta h$, because $g$ is nearly constant there.

### 1.7 Equipotential surfaces

An equipotential surface is a surface on which the gravitational potential is constant everywhere.

- Equipotential surfaces are **perpendicular to the field lines** at every point.
- **No work is done** moving a mass along an equipotential surface, because the potential (and hence potential energy) does not change.
- Around a point mass they are concentric spheres centred on the mass; near the Earth's surface they are horizontal planes.
- The field strength is related to how closely packed the equipotential surfaces are: where they are close together, the potential changes rapidly with distance and the field is strong.

### 1.8 g and potential gradient

The gravitational field strength is the **negative of the potential gradient**:

$$g = -\frac{d\phi}{dr}$$

(Examined directly in 9702/42/O/N/21 Q2: "State the relationship between gravitational potential and gravitational field strength" - the mark scheme wants "field strength equals potential gradient" plus "reference to the minus sign".)

What this means in practice:

- On a graph of $\phi$ against $r$, the gradient of the curve at any point gives $-g$ at that point.
- Where the $\phi$-$r$ curve is steepest, the field is strongest.
- At a **maximum** of $\phi$ (between two masses, where the two potential wells meet), the gradient is zero, so $g = 0$ - this is the point of zero resultant field. A sketch of $g$ against $r$ crosses zero at this point.
- Since $\phi$ is negative and becomes less negative as $r$ increases, $d\phi/dr$ is positive, so $g = -d\phi/dr$ correctly points back towards the mass (in the direction of decreasing $r$).

### 1.9 Orbits

For a satellite (mass $m$) orbiting a planet (mass $M$) in a circular orbit of radius $r$ at constant speed $v$, the only force acting is the gravitational attraction, and it provides the **centripetal force**:

$$\frac{GMm}{r^2} = \frac{mv^2}{r}$$

The satellite's mass $m$ cancels:

$$v^2 = \frac{GM}{r}$$

$$v = \sqrt{\frac{GM}{r}}$$

Key consequences:

- The orbital speed depends **only on the mass of the central body $M$ and the orbital radius $r$** - not on the mass of the satellite. All satellites (and astronauts on a space walk!) travel at the same speed in the same orbit.
- The closer the orbit, the **faster** the satellite must travel. Too slow and it falls towards the planet; too fast and it moves out to a higher orbit.
- The gravitational force is at right angles to the velocity, so the speed is constant but the direction keeps changing - the satellite is accelerating (centripetally) even though its speed never changes.

**Orbital period.** Since one orbit covers a circumference $2\pi r$:

$$v = \frac{2\pi r}{T}$$

Substituting into $v^2 = \frac{GM}{r}$:

$$\frac{4\pi^2 r^2}{T^2} = \frac{GM}{r}$$

$$T^2 = \frac{4\pi^2 r^3}{GM}$$

This is Kepler's third law: the square of the orbital period is directly proportional to the cube of the orbital radius ($T^2 \propto r^3$). Kepler found this empirically from planetary data; Newton's law of gravitation explains it. The constant $k$ in $r^3 = kT^2$ is $k = \frac{GM}{4\pi^2}$ (examined in 9702/41/M/J/18 Q1).

Often you will rearrange it to find the orbital radius from the period:

$$r^3 = \frac{GMT^2}{4\pi^2}$$

### 1.10 Geostationary orbits

A geostationary satellite orbits so that it **remains above a fixed point on the Earth's equator**. The Earth rotates below it at the same rate.

**The four features you must be able to state (this is a 2-mark question - see 9702/41/O/N/19 Q1):**

1. Its orbital period is **24 hours** (equal to the Earth's rotational period).
2. It orbits **directly above the Equator**.
3. It orbits **from west to east** (in the same direction as the Earth's rotation).
4. It stays above the same point on the Earth's surface (this is what "geostationary" means - note the examiner complains when candidates just rephrase this instead of giving features 1-3).

The orbital radius: using $r^3 = \frac{GMT^2}{4\pi^2}$ with $T = 24$ h $= 86400$ s and $M = 6.0 \times 10^{24}$ kg:

$$r^3 = \frac{6.67 \times 10^{-11} \times 6.0 \times 10^{24} \times (86400)^2}{4\pi^2} = 7.66 \times 10^{22} \text{ m}^3$$

$$r = 4.23 \times 10^7 \text{ m} \approx 42\,300 \text{ km from the Earth's centre}$$

Since the Earth's radius is 6400 km, the height above the surface is about $42\,300 - 6400 = 35\,900$ km (about 5.6 Earth radii above the surface, or 6.6 Earth radii from the centre).

**Uses**: telecommunications, satellite television, weather monitoring. Because the satellite never moves in the sky, receiver dishes can be fixed - no tracking system needed. Geostationary satellites drift out of position over ~10 years and need small rocket motors to return them to the correct position.

**Why 24 hours?** The satellite must complete one orbit in exactly the same time the Earth takes to rotate once, in the same sense, so the line from the Earth's centre to the satellite always points at the same ground location.

### 1.11 Escape velocity

The escape velocity (escape speed) is the **minimum speed** a body needs, at a given point, to escape the gravitational field completely - to reach infinity with zero kinetic energy left over.

At the surface of a planet (mass $M$, radius $R$), the potential energy is $-\frac{GMm}{R}$. For the body to just reach infinity with zero speed, its initial kinetic energy must exactly pay for the potential energy "debt":

$$\frac{1}{2}mv^2 = \frac{GMm}{R}$$

The mass $m$ cancels:

$$v = \sqrt{\frac{2GM}{R}}$$

- Escape velocity does **not** depend on the mass of the escaping object.
- For the Earth: $v = \sqrt{\frac{2 \times 6.67 \times 10^{-11} \times 6.0 \times 10^{24}}{6.4 \times 10^6}} \approx 1.1 \times 10^4$ m s$^{-1}$ (about 11 km s$^{-1}$).
- For the Moon (mass $7.35 \times 10^{22}$ kg, radius $1.74 \times 10^6$ m): $v \approx 2.4 \times 10^3$ m s$^{-1}$ (about 2.4 km s$^{-1}$) - the classic 9702/41/O/N/13 Q1 answer.
- The value $\frac{GM}{R}$ (the magnitude of the surface potential) is the **energy per unit mass** needed to escape: about $6.3 \times 10^7$ J kg$^{-1}$ from the Earth's surface, but only about $2.8 \times 10^6$ J kg$^{-1}$ from the Moon's surface. That is why a small rocket suffices to launch from the Moon but a huge one is needed from Earth, and why deep-space probes are assembled at space stations and launched from orbit rather than from the Earth's surface (less energy needed at the start, plus less atmospheric drag).

**Exam subtlety** (9702/41/O/N/13 Q1(c)): if the Moon is *not* assumed isolated (it orbits the Earth), the minimum speed for the rock to reach the Earth is **lower** than the escape speed, because the Earth's gravity attracts the rock - the Earth's potential well "catches" it, so it does not need enough energy to reach infinity.

### 1.12 g at surface vs height

Let $R$ be the planet's radius and $h$ the height above the surface. Then $r = R + h$ and:

$$g_{\text{surface}} = \frac{GM}{R^2}, \qquad g_{\text{at height } h} = \frac{GM}{(R+h)^2}$$

Ratio form (handy for ratio questions like 9702/42/F/M/20 Q1(b)(iii)):

$$\frac{g_{\text{at height } h}}{g_{\text{surface}}} = \left(\frac{R}{R+h}\right)^2$$

So at height $h = R$ (twice the radius from the centre), $g = \frac{g_{\text{surface}}}{4}$. At height $2R$ (three times the radius from the centre), $g = \frac{g_{\text{surface}}}{9}$.

**The single most common numerical error in this chapter** is using the height above the surface instead of the distance from the centre. Whenever you substitute into $\frac{GM}{r^2}$ or $-\frac{GM}{r}$, $r$ is always measured **from the centre of the planet**. Only the $mg\Delta h$ approximation uses height.

---

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

## 6. Cheat Sheet

### All formulas in one block

- Newton's law: $$F = \frac{GMm}{r^2}$$ (attractive, between point masses, $r$ = centre-to-centre)
- Field strength: $$g = \frac{F}{m} = \frac{GM}{r^2}$$ (vector, towards the mass, units N kg$^{-1}$ = m s$^{-2}$)
- Potential: $$\phi = -\frac{GM}{r}$$ (scalar, always negative, units J kg$^{-1}$)
- Potential energy: $$E_P = m\phi = -\frac{GMm}{r}$$ (always negative; zero at infinity)
- Change in PE between radii: $$\Delta E_P = GMm\left(\frac{1}{r_1} - \frac{1}{r_2}\right)$$
- Field from potential: $$g = -\frac{d\phi}{dr}$$
- Orbital speed: $$v = \sqrt{\frac{GM}{r}}$$ (independent of satellite mass)
- Speed from period: $$v = \frac{2\pi r}{T}$$
- Kepler III / period: $$T^2 = \frac{4\pi^2 r^3}{GM}, \qquad r^3 = \frac{GMT^2}{4\pi^2}$$
- Escape speed: $$v_{\text{esc}} = \sqrt{\frac{2GM}{R}}$$
- Ratio trick: $$\frac{g_h}{g_0} = \left(\frac{R}{R+h}\right)^2$$
- Near the surface only: $$\Delta E_P = mg\Delta h$$

### Key definitions (word-for-word)

- **Gravitational field strength**: the gravitational force exerted per unit mass on a small object placed at that point.
- **Gravitational potential**: the work done per unit mass in bringing a mass from infinity to the point.
- **Newton's law of gravitation**: any two point masses attract each other with a force directly proportional to the product of their masses and inversely proportional to the square of their separation.
- **Geostationary orbit**: period 24 h, directly above the Equator, west to east, stays above a fixed point.
- **Escape speed**: the minimum speed needed for a body to escape a gravitational field (reach infinity) with no kinetic energy left.

### Constants to recognise

- $G = 6.67 \times 10^{-11}$ N m$^2$ kg$^{-2}$
- Earth: $M = 6.0 \times 10^{24}$ kg, $R = 6.4 \times 10^6$ m, $g = 9.81$ N kg$^{-1}$
- Geostationary: $T = 86400$ s, $r = 4.23 \times 10^7$ m from centre ($\approx 36\,000$ km above surface)
- Moon: $M = 7.35 \times 10^{22}$ kg, $R = 1.74 \times 10^6$ m, surface $g \approx 1.6$ N kg$^{-1}$

### Common traps (see Section 7 for the full list)

1. Using height above the surface instead of distance from the centre in $GM/r^2$ and $-GM/r$.
2. Forgetting the minus sign in $\phi = -GM/r$ and $E_P = -GMm/r$.
3. Forgetting that negative potential energy *increases* when $r$ increases.
4. Writing $\frac{1}{r_2 - r_1}$ instead of $\frac{1}{r_1} - \frac{1}{r_2}$.
5. Treating potential as a vector (subtracting) instead of a scalar (adding).
6. Forgetting to convert minutes to seconds for $T$, or km to m for $r$.
7. Assuming $g = 9.81$ N kg$^{-1}$ at a satellite's height - use $GM/r^2$ with the orbital radius.
8. Not taking the square root when finding $v$ from $v^2$.
9. Saying fields "cancel" without "equal magnitude, opposite direction".
10. Confusing gravitational field strength (force per unit mass) with gravitational potential (energy per unit mass).

---

## 7. Common Exam Mistakes

Compiled from the CAIE 9702 Principal Examiner Reports for Teachers (June 2021, Nov 2021, Nov 2019, June 2019).

### Definitions

- **Giving the wrong definition entirely**: the most common incorrect answer to "define gravitational field strength" (9702/s21 Q1(a)) was the definition of gravitational potential. Learn the two side by side: field strength = *force per unit mass*; potential = *work done per unit mass*.
- **Omitting "per unit mass"**: in Nov 2021, saying "work done in moving a mass" did not get the mark because it does not convey the division by mass. The ratio must be explicit: work done divided by mass.
- **Omitting "point masses"** when stating Newton's law (9702/w19 Q1(a)) - the most common omission in an otherwise well-answered question.
- **Not naming symbols**: in 9702/s19 Q1(a), candidates who wrote $F = GMm/x^2$ often failed to state that $G$ is the gravitational constant. Also, $x$ is the *separation* of the masses, not a "radius".

### Calculations

- **Using the height instead of the radius**: in 9702/s19, "a small but significant number of candidates used the height above the surface of the planet and forgot to add the radius." Also in 9702/w19 Q1(b)(ii), a small but significant number assumed $g = 9.81$ N kg$^{-1}$ at the satellite - the field strength is not the surface value up there.
- **Unit conversions**: forgetting to convert minutes to seconds (9702/s21 Q1(b)), km to m (9702/w19 - "power-of-ten errors due to forgetting to convert the radius from km into m"), and cm to m (9702/s19).
- **Squaring/cubing errors**: forgetting to square the period or cube the radius in geostationary calculations (9702/w19). Confusing $r^3$ with $r$ in "show that" working (9702/s21).
- **The $\frac{1}{r_2 - r_1}$ error**: candidates treated $\frac{1}{r_2 - r_1}$ as the same as $\frac{1}{r_1} - \frac{1}{r_2}$ when finding changes in potential energy (9702/s19). They are not the same.
- **Change in potential vs change in potential energy**: in 9702/s21 Q1(c)(iii), the most common mistake was calculating the change in *potential* ($\Delta\phi$) rather than the change in *potential energy* ($\Delta E_P = m\Delta\phi$). Read which quantity the question asks for.
- **Sign of the change in potential energy**: many candidates in 9702/s21 knew $E_P = -GMm/r$ but did not realise that, because it is negative, the energy *increases* as $r$ increases. The answer "separation and energy are inversely proportional" ignores the minus sign.

### Explanations and concepts

- **"Cancelling fields" is not enough** (9702/w21 Q2(b)(i)): to explain a zero resultant field you must say the fields are equal in magnitude and opposite in direction. The word "cancelling" alone was not credited. Also, candidates who answered in terms of *forces* gained nothing - the question was about field strength.
- **Potential is scalar**: in 9702/w21 Q2(b)(iii), many candidates calculated the potential due to the Earth only; of those who used both, many subtracted the negative values instead of adding them. Potentials always add.
- **Taking square roots beats expanding quadratics**: for zero-field point problems, square-rooting both sides of $\frac{M_1}{x^2} = \frac{M_2}{(d-x)^2}$ is much cleaner than expanding; several candidates got lost in the quadratic (9702/w21).
- **Confusing potential with potential energy** (9702/s19): candidates wrote "gravitational potential" when the question was about the potential energy of a spacecraft. They are different quantities with different units.
- **Vague energy arguments**: in 9702/s19, candidates applied conservation of energy with one energy type increasing while the other decreased, without checking the context. Use the physics: potential energy decreases as a body approaches a planet (it becomes more negative).
- **Repeating the question**: in 9702/w19 Q1(b)(i), weak candidates just rephrased what "geostationary" means ("above the same point on the Earth") instead of stating the orbit features: above the Equator, west to east, period 24 hours.
- **Not explaining working in "determine" questions**: in 9702/w19 Q1(b)(ii) the question explicitly said "explain your working"; candidates who jumped straight to numbers lost the method mark. Start from a principle: "the gravitational force provides the centripetal force."
- **"Show that" presentation**: in 9702/s21 Q1(c)(i), unclear presentation caused confusion between $r^3$ and $r$. In "show that" questions you must show every step, including constants like $G$ and the full substitution.

### General advice from the examiners

- Convert to standard SI units *before* starting calculations.
- State the physical principle you are using before substituting numbers.
- In multi-part calculations, if you get a value in (i), use it in (ii) - error carried forward (ECF) marks are usually available, but only if your working is visible.
- Definitions must be ratios: "per unit mass" must be explicit, not implied.
- Descriptive questions are harder than calculations: use the correct technical terms and avoid ambiguity.

---

*Sources: CAIE 9702 syllabus (2022-2024); Cambridge International AS & A Level Physics coursebook (Chapter 18); CAIE published question papers, mark schemes and Principal Examiner Reports for Teachers for 9702/41 and 9702/42, May/June 2018, 2019, 2021; Oct/Nov 2013, 2019, 2021; Feb/March 2020.*
