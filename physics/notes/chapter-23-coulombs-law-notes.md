# Chapter 23: Coulomb's Law and Electric Fields - CAIE A Level Physics (9702) Study Notes

Exam-focused revision notes for Cambridge International AS & A Level Physics 9702, covering the whole of Topic 18 (Electric fields) as taught in Chapter 23 of the coursebook. Everything here is what the exam can actually ask, nothing more. All definitions are worded to match mark schemes, and all question types below have appeared in real 9702 papers.

## 1. Theory

### 1.1 The electric field

An electric field is a field of force: a region of space in which a charge experiences an electric force. It is produced by electric charges. You represent it with field lines:

- Field lines show the direction of the force on a **positive** test charge. They point away from positive charges and towards negative charges.
- The spacing of the lines shows the strength: closer lines mean a stronger field.
- Lines never cross, and they meet conductors at right angles (the surface of a conductor is an equipotential).
- Two like charges repel, so their lines curve away; two unlike charges attract, and lines run from the positive to the negative charge.

### 1.2 Electric field strength

**Definition (2-mark version used in mark schemes):** the electric field strength at a point is the **force per unit positive charge** acting on a charge placed at that point.

$$E = \frac{F}{Q}$$

- $E$ is electric field strength, unit $\text{N C}^{-1}$ (equivalent to $\text{V m}^{-1}$; examiners accept either).
- $F$ is the force on a charge $Q$ placed at the point.
- Electric field strength is a **vector**: you must give its direction (the direction of the force on a positive charge).

Rearranged, the force on a charge $q$ in a field of strength $E$ is:

$$F = qE$$

### 1.3 Coulomb's law

**Statement:** any two point charges exert an electrical force on each other that is proportional to the product of their charges and inversely proportional to the square of the distance between them.

$$F = \frac{Q_1 Q_2}{4\pi\epsilon_0 r^2}$$

- $Q_1$, $Q_2$ are the two point charges in coulombs.
- $r$ is the distance between their centres, in metres.
- $\epsilon_0$ is the permittivity of free space, $8.85 \times 10^{-12} \text{ F m}^{-1}$.
- $\frac{1}{4\pi\epsilon_0} = 8.99 \times 10^9 \approx 9.0 \times 10^9 \text{ N m}^2 \text{ C}^{-2}$, so a quick estimate is $F \approx \frac{9.0 \times 10^9 Q_1 Q_2}{r^2}$.

Key points:

- It is an inverse square law: double $r$ and the force drops to a quarter.
- The force is a vector and acts along the line joining the charges. The two charges exert equal and opposite forces on each other (Newton's third law).
- Sign convention: the product $Q_1 Q_2$ carries the sign. Like charges give a positive force (repulsion); unlike charges give a negative force (attraction). In calculations you usually just state the direction in words.
- Coulomb's law applies to point charges and to uniformly charged spheres, as long as you use the **centre-to-centre** distance (see below).

### 1.4 Charged spheres act like point charges

For a point outside a spherical conductor, the charge on the sphere behaves as if it were all concentrated at the centre. So for two charged spheres you use the centre-to-centre separation in Coulomb's law, and for a point outside a sphere the field is the same as that of a point charge $Q$ at the centre:

$$E = \frac{Q}{4\pi\epsilon_0 r^2}$$

where $r$ is the distance from the centre of the sphere.

### 1.5 Uniform electric fields (parallel plates)

Two charged parallel plates produce a uniform field between them: the field lines are parallel, equally spaced, and run from the positive plate to the negative plate.

$$E = \frac{V}{d}$$

- $V$ is the potential difference between the plates in volts.
- $d$ is the plate separation in metres.
- This formula is ONLY valid for a uniform field. Do not use it for the radial field of a point charge.

The force on a charge $q$ between the plates is constant everywhere:

$$F = qE = \frac{qV}{d}$$

A charged particle entering the space between the plates accelerates at:

$$a = \frac{F}{m} = \frac{qE}{m}$$

Motion of charged particles in a uniform field:

- A charge released from rest moves in a straight line along the field lines (positive charges towards the negative plate, negative charges towards the positive plate).
- A charge entering perpendicular to the field has constant velocity parallel to the plates and constant acceleration perpendicular to them, so it follows a **parabolic** path (exactly like projectile motion under gravity).
- The work done moving a charge $q$ through a potential difference $V$ is $W = qV$. The change in potential energy of a charge moved between the plates is therefore $\Delta E_P = qV$.

### 1.6 Field strength of a point charge (radial field)

A point charge produces a radial field. Dividing the Coulomb force on a test charge $Q_2$ by $Q_2$ gives the field strength due to charge $Q$ at distance $r$:

$$E = \frac{F}{Q_2} = \frac{Q}{4\pi\epsilon_0 r^2}$$

- The field obeys an inverse square law: double $r$ and $E$ falls to a quarter.
- $E$ is a vector, directed radially away from a positive charge and radially towards a negative charge.
- This formula is used for point charges and for points outside charged spheres (using the distance from the centre).

### 1.7 Electric potential energy

Moving a charge in an electric field changes its potential energy, exactly like lifting a mass in a gravitational field:

- Pushing a positive charge towards another positive charge requires work, so its potential energy increases (repulsion; like lifting a mass).
- Letting it go, it accelerates away, converting potential energy into kinetic energy.

In a uniform field, moving a charge $q$ through a potential difference $V$ changes its potential energy by:

$$\Delta E_P = qV$$

The electric potential energy of a system of two point charges $Q$ and $q$ separated by $r$ is the work done in bringing them from infinity to that separation:

$$E_P = \frac{Qq}{4\pi\epsilon_0 r}$$

- It is a scalar. The sign follows the charges: for two like charges it is positive (energy is stored; they repel), for unlike charges it is negative (energy is released as they attract).
- It equals the kinetic energy gained if the charges are released and allowed to separate or come together.

### 1.8 Electric potential

**Definition (full marks):** the electric potential at a point is the **work done per unit positive charge** in bringing a small test charge from infinity to that point.

- Symbol $V$ (or $\phi$ in some books), unit volt, $1 \text{ V} = 1 \text{ J C}^{-1}$.
- It is a **scalar** quantity.
- The zero of potential is at infinity.
- Potential is the electrical analogue of voltage: the potential difference between two points is the difference in their electric potentials.

For a point charge $Q$ at distance $r$:

$$V = \frac{Q}{4\pi\epsilon_0 r}$$

- Potential is positive near a positive charge and negative near a negative charge.
- It obeys an inverse (not inverse square) relationship with $r$: double $r$ and $V$ halves.
- Because potential is a scalar, the potential at a point due to several charges is found by adding the individual potentials (with their signs). Positive charges give positive contributions, negative charges give negative contributions.

A positive charge sits on a potential "hill", a negative charge creates a potential "well".

### 1.9 Field strength and potential gradient

The electric field strength is the **negative of the potential gradient**:

$$E = -\frac{\Delta V}{\Delta r}$$

- In a uniform field the potential gradient is constant, so $E = \frac{V}{d}$ (same formula as above).
- In a radial field the gradient changes with position. To find $E$ at a point from a $V$ against $r$ graph: draw the tangent at that point, find its gradient, and take the negative.
- Equipotential lines (lines of constant potential) are always perpendicular to field lines. They are equally spaced in a uniform field, and get closer together nearer a point charge (where the gradient is steeper).

### 1.10 Comparing gravitational and electric fields

This is a favourite exam question. Learn the table.

| Property | Gravitational field | Electric field |
| --- | --- | --- |
| Origin | Masses | Electric charges |
| Force | Always attractive | Attractive or repulsive (positive and negative charges) |
| Field strength | $g = \frac{F}{m}$, unit $\text{N kg}^{-1}$ or $\text{m s}^{-2}$ | $E = \frac{F}{Q}$, unit $\text{N C}^{-1}$ or $\text{V m}^{-1}$ |
| Point mass / point charge | $g = \frac{GM}{r^2}$ (radial, always towards the mass) | $E = \frac{Q}{4\pi\epsilon_0 r^2}$ (radial, away from positive, towards negative) |
| Force law | $F = \frac{GMm}{r^2}$ (Newton's law) | $F = \frac{Q_1 Q_2}{4\pi\epsilon_0 r^2}$ (Coulomb's law) |
| Potential | $\phi = -\frac{GM}{r}$ (always negative, zero at infinity) | $V = \frac{Q}{4\pi\epsilon_0 r}$ (sign follows the charge, zero at infinity) |
| Field lines | Radial, pointing towards the mass | Radial, pointing away from positive, towards negative |
| Uniform field | $g$ constant near the Earth's surface | $E = \frac{V}{d}$ between parallel plates |
| Scalar or vector | Field strength vector, potential scalar | Field strength vector, potential scalar |
| Inverse square law | Yes: $g \propto \frac{1}{r^2}$ | Yes: $E \propto \frac{1}{r^2}$ |

Both fields are fields of force, both obey inverse square laws for point sources, both have scalar potentials that are zero at infinity, and both have the same relationship between field strength and potential gradient ($g = -\frac{d\phi}{dr}$, $E = -\frac{dV}{dr}$). The crucial difference: gravity only attracts because mass is always positive, while electric charges come in two signs, so electric forces can attract or repel and electric potentials can be positive or negative.

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

## 6. Cheat Sheet

**One-glance revision block.**

Definitions:
- Electric field: a field of force; region where a charge experiences a force.
- Electric field strength: force per unit positive charge, $E = \frac{F}{Q}$, units $\text{N C}^{-1} = \text{V m}^{-1}$, vector.
- Electric potential: work done per unit positive charge in bringing a small test charge from infinity to the point, units V, scalar, zero at infinity.

All formulas:

$$F = \frac{Q_1 Q_2}{4\pi\epsilon_0 r^2}, \qquad E = \frac{F}{Q}, \qquad F = qE, \qquad E = \frac{Q}{4\pi\epsilon_0 r^2}, \qquad E = \frac{V}{d}, \qquad V = \frac{Q}{4\pi\epsilon_0 r}, \qquad E_P = \frac{Qq}{4\pi\epsilon_0 r}, \qquad E = -\frac{\Delta V}{\Delta r}$$

Key numbers: $\epsilon_0 = 8.85 \times 10^{-12} \text{ F m}^{-1}$; $\frac{1}{4\pi\epsilon_0} = 8.99 \times 10^9$ (use $9.0 \times 10^9$ for estimates); $e = 1.60 \times 10^{-19} \text{ C}$; $1 \mu\text{C} = 10^{-6} \text{ C}$; $1 \text{ nC} = 10^{-9} \text{ C}$; $1 \text{ kV cm}^{-1} = 10^5 \text{ V m}^{-1}$.

Common traps:
- **Forgetting to square $r$** in Coulomb's law or $E = \frac{Q}{4\pi\epsilon_0 r^2}$. This is the single most common calculation error.
- **Using $E = \frac{V}{d}$ for a radial field.** It is only valid for a uniform field between parallel plates.
- **Using surface-to-surface distance** instead of centre-to-centre for spheres.
- **Mixing up $E$ and $V$**: $E \propto \frac{1}{r^2}$ (inverse square), $V \propto \frac{1}{r}$ (inverse). Double $r$: $E$ quarters, $V$ halves.
- **Adding fields as scalars.** Field strength is a vector: fields from two charges can cancel (zero point between like charges) or add. Potentials are scalars and always add with signs.
- **Definitions without "positive charge"** (field strength) or "from infinity" (potential).
- **Power-of-ten errors** converting cm/m, $\mu\text{C}$/C, kV/V, g/kg.
- **Sign of force**: like charges repel (positive $Q_1 Q_2$), unlike attract (negative). State the direction in words.
- **Conductors are equipotentials**: potential is constant inside a charged conducting sphere, even though the field inside is zero.
- **Equilibrium means zero resultant force**, not zero force (oil drop question).
- **Coulomb's law and $E = \frac{Q}{4\pi\epsilon_0 r^2}$ are NOT on the formula sheet**: memorise them. $V = \frac{Q}{4\pi\epsilon_0 r}$ IS on the formula sheet.

## 7. Common Exam Mistakes

From examiner reports (June 2019 and earlier series), these are the actual reasons candidates lost marks on this chapter:

1. **Definition of electric field strength missing "positive charge".** The idea that the force is on a positive charge was "not well known". Always include it.
2. **Assuming opposite signs from a signed $E$ graph.** A field strength graph crossing zero between two charges means the fields cancel: the charges have the SAME sign. Candidates who read the sign change as "positive to negative" lost both marks.
3. **Treating a resultant field as a single-charge field.** When two charges are present, the field at any point is the resultant of both fields, so $Q = 4\pi\epsilon_0 r^2 E$ cannot be used with the resultant field near one charge. The correct route is to use the zero-field point and set $E_A = E_B$.
4. **Power-of-ten errors** in $E = \frac{V}{d}$ and Coulomb's law, and failure to convert units (cm to m, $\mu\text{C}$ to C, kV to V).
5. **Oil drop equilibrium**: writing "the force is zero" instead of "the resultant force is zero"; using $F = ma$ instead of equating electric force to weight $qE = mg$; wrong sign of the charge because the direction of the electric force was not considered (it must oppose the weight).
6. **Thinking a reduced p.d. reduces the charge on a droplet** rather than the field strength and hence the electric force.
7. **Electric potential definitions with the wrong dimensions**: "energy of a charge" has dimensions of energy, not potential. It must be work/energy PER UNIT charge. Credit was also lost by omitting "from infinity" (which fixes the sign).
8. **Not knowing the potential gradient between parallel plates is constant**, so the potential varies linearly from one plate to the other.
9. **Drawing $E$ when asked for $V$** (and vice versa) on potential/field variation graphs, and not realising the potential is constant inside a conducting sphere.
10. **Difficulty calculating the acceleration of a charged particle** in a uniform field: $a = \frac{qE}{m}$ with $E = \frac{V}{d}$. Also, premature rounding of intermediate values caused wrong final answers in multi-part calculations.
11. **Saying a force "cannot act" on a particle in a vacuum**: weight does act in a vacuum (gravity does not need a medium). Read the question carefully.
12. **Confusing field strength with force**: field strength is force per unit charge, so a small charge in a strong field still feels a small force. Compare like with like ($qE$ vs $mg$), never $E$ with $mg$ directly.
