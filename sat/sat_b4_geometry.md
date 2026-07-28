# SAT B4: GEOMETRY & TRIGONOMETRY — MASTER MANUAL

**Weight:** ~15% of Math section (5–7 of 44 questions)

**Domain cross-references:** B1 (Algebra) for coordinate geometry, systems with geometric constraints | B2 (Advanced Math) for circle equations, quadratic geometry problems | B3 (Data Analysis) for geometric probability, unit conversions

## FRAMEWORK MAP

| Official Testing Point | Manual Section |
|---|---|
| Area and volume | B4.1–B4.2 |
| Lines, angles and triangles | B4.3 |
| Right triangles and trigonometry | B4.4–B4.4a |
| Circles | B4.5 |

## Master Decision Sheet

| See | Do |
|---|---|
| Diameter given | Divide by 2 |
| Similar figures | Find $k$; perimeter $k$, area $k^2$, volume $k^3$ |
| Right triangle | Pythagoras, special triangle, or SOHCAHTOA? |
| Circle equation | Flip center signs, sqrt RHS for radius |
| Tangent line | Radius $\perp$ tangent at point of contact |
| Inscribed angle | Half the intercepted arc |
| Arc / sector | Fraction of circumference / area via $\frac{\theta}{360^\circ}$ |

---

## How to Use This Guide

Formulas tagged `[REFERENCE SHEET]` appear in Bluebook — you are not required to memorize these, but knowing the commonly used formulas saves time. `[MEMORIZE]` formulas must be automatic. `[SUPPLEMENTARY]` is useful but lower priority. Every example has a difficulty label. Wrong-answer traps are in **bold**.

---

## Quick-Reference Formula Sheet

### Provided on Reference Sheet

| Concept | Formula |
|---------|---------|
| Rectangle area | $A = lw$ |
| Triangle area | $A = \frac{1}{2}bh$ |
| Circle area | $A = \pi r^2$ |
| Circle circumference | $C = 2\pi r$ |
| Pythagorean theorem | $a^2 + b^2 = c^2$ |
| 45-45-90 ratios | $s : s : s\sqrt{2}$ |
| 30-60-90 ratios | $s : s\sqrt{3} : 2s$ |
| Rectangular prism volume | $V = lwh$ |
| Cylinder volume | $V = \pi r^2 h$ |
| Sphere volume | $V = \frac{4}{3}\pi r^3$ |
| Cone volume | $V = \frac{1}{3}\pi r^2 h$ |
| Pyramid volume | $V = \frac{1}{3}Bh$ |
| Degrees/radians in a circle | $360^\circ = 2\pi$ |
| Triangle angle sum | $180^\circ$ |

### Must Memorize

| Topic | Formula / Rule |
|-------|---------------|
| Rectangle perimeter | $P = 2l + 2w$ |
| Parallelogram area | $A = bh$ |
| Trapezoid area | $A = \frac{1}{2}(b_1 + b_2)h$ |
| Distance formula | $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ |
| Midpoint formula | $M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$ |
| SOHCAHTOA | $\sin\theta = \frac{O}{H},\; \cos\theta = \frac{A}{H},\; \tan\theta = \frac{O}{A}$ |
| Cofunction identity | $\sin\theta = \cos(90^\circ - \theta)$ |
| Pythagorean identity | $\sin^2\theta + \cos^2\theta = 1$ |
| Tangent identity | $\tan\theta = \frac{\sin\theta}{\cos\theta}$ |
| Arc length | $s = \frac{\theta}{360^\circ} \cdot 2\pi r$ |
| Sector area | $A = \frac{\theta}{360^\circ} \cdot \pi r^2$ |
| Circle equation | $(x - h)^2 + (y - k)^2 = r^2$ |
| Cylinder surface area | $SA = 2\pi r^2 + 2\pi rh$ |
| Sphere surface area | $SA = 4\pi r^2$ |
| Rectangular prism SA | $SA = 2lw + 2wh + 2lh$ |
| Cube surface area | $SA = 6s^2$ |
| Triangle inequality | $a + b > c$ |
| Inscribed angle | $\text{angle} = \frac{1}{2} \times \text{intercepted arc}$ |
| Polygon interior sum | $(n - 2) \times 180^\circ$ |
| Radian conversion | $\text{radians} = \frac{\pi}{180} \times \text{degrees}$ |
| Density (cross-domain B3) | $\text{density} = \frac{\text{mass}}{\text{volume}}$ |

---

## B4.1 Area & Perimeter

### Basic Shapes

| Shape | Area | Perimeter | Notes |
|-------|------|-----------|-------|
| Rectangle | $A = lw$ `[REFERENCE SHEET]` | $P = 2l + 2w$ `[MEMORIZE]` | |
| Square | $A = s^2$ | $P = 4s$ | Rectangle special case |
| Triangle | $A = \frac{1}{2}bh$ `[REFERENCE SHEET]` | sum of sides | $b \perp h$; altitude may fall outside obtuse triangle |
| Circle | $A = \pi r^2$ `[REFERENCE SHEET]` | $C = 2\pi r$ `[REFERENCE SHEET]` | |
| Parallelogram | $A = bh$ | $P = 2(a + b)$ | $h$ $\perp$ height |
| Trapezoid | $A = \frac{1}{2}(b_1 + b_2)h$ | sum of 4 sides | $h \perp$ bases |
| Regular polygon | $A = \frac{1}{2}Pa$ `[SUPPLEMENTARY]` | $n \times \text{side}$ | $a$ = apothem |

❌ **Diameter in $A = \pi r^2$** — always halve diameter first.
❌ **Circumference ($2\pi r$) vs area ($\pi r^2$)** — one is linear, one is squared.

### Composite Figures

1. Identify constituent shapes (rectangle, semicircle, triangle, etc.)
2. Compute each area separately
3. Add or subtract as indicated by the figure

[Medium] A trapezoid has bases 8 and 12 with height 5. Find its area.

$A = \frac{1}{2}(8 + 12)(5) = 50$

[Medium] A rectangle 10 by 4 has a semicircle removed from one short side (diameter = short side). Find remaining area.

Rectangle: $10 \cdot 4 = 40$
Semicircle $(r = 2)$: $\frac{1}{2}\pi(2)^2 = 2\pi$
Remaining: $40 - 2\pi$

❌ **Trap:** Forgetting the $\frac{1}{2}$ factor for the semicircle.

[Hard] A square of side 8 has a circle inscribed. Find the area outside the circle but inside the square.

$A_{\text{square}} = 64$, $r = 4$, $A_{\text{circle}} = 16\pi$
Shaded: $64 - 16\pi$

[Hard] Polygon vertices $(0,0)$, $(4,0)$, $(6,3)$, $(2,5)$. Find area via shoelace.

| $x$ | $y$ | $x_i y_{i+1}$ | $y_i x_{i+1}$ |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 4 | 0 | 20 | 0 |
| 6 | 3 | 18 | 12 |
| 2 | 5 | 0 | 10 |
| 0 | 0 | 0 | 0 |

Sum down: $0 + 20 + 18 + 0 = 38$
Sum up: $0 + 0 + 12 + 10 = 22$
$A = \frac{1}{2}|38 - 22| = 8$

❌ **Trap:** Forgetting to repeat the first vertex at the end.

### Distance Formula

$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ `(MUST MEMORIZE)`

✅ The distance formula IS the Pythagorean theorem on the coordinate plane.

### Coordinate Area

For polygons with vertices given as coordinates, decompose into triangles or rectangles first. 

The shoelace formula `[SUPPLEMENTARY]` can also work: $A = \frac{1}{2}\left|\sum x_i y_{i+1} - \sum y_i x_{i+1}\right|$ with vertices ordered and first vertex repeated at end. Decomposition is more intuitive.

---

## B4.2 Volume & Surface Area

The standard solid-volume formulas listed below appear on the reference sheet `[REFERENCE SHEET]`. Surface area formulas `[MEMORIZE]`.

| Shape | Volume | Surface Area |
|-------|--------|-------------|
| Rectangular prism | $V = lwh$ | $SA = 2lw + 2wh + 2lh$ `[MEMORIZE]` |
| Cube | $V = s^3$ | $SA = 6s^2$ `[MEMORIZE]` |
| Right circular cylinder | $V = \pi r^2 h$ | $SA = 2\pi r^2 + 2\pi rh$ `[MEMORIZE]` |
| Sphere | $V = \frac{4}{3}\pi r^3$ | $SA = 4\pi r^2$ `[SUPPLEMENTARY]` |
| Right circular cone | $V = \frac{1}{3}\pi r^2 h$ | rarely tested |
| Rectangular pyramid | $V = \frac{1}{3}Bh$ | rarely tested |

❌ **Radius vs diameter** — cylinder with diameter 10 → $r = 5$.
❌ **Confusing $\frac{1}{3}$ (cone/pyramid) with $\frac{4}{3}$ (sphere).**
❌ **Forgetting the $2$ in $SA = 2\pi r^2 + 2\pi rh$** (top and bottom).

### B4.2a Scale Factors: Length, Area, and Volume

- Linear scale factor $k$ → **perimeter** and **circumference** scale by $k$
- Area scales by $k^2$, volume scales by $k^3$
- Double a radius → circumference $\times 2$, area $\times 4$, volume $\times 8$
- Halve a radius → volume $\times \frac{1}{8}$

❌ **Trap:** Applying $k^2$ for volume or $k^3$ for area.
❌ **Trap:** Forgetting that perimeter/circumference scale by $k$, not $k^2$.

[Medium] A sphere has volume $36\pi$. Find its surface area.

$V = \frac{4}{3}\pi r^3 = 36\pi \implies r^3 = 27 \implies r = 3$
$SA = 4\pi(9) = 36\pi$

[Hard] A cone and a cylinder share radius $r$ and height $h$. Cone volume is $12\pi$. Find cylinder volume.

$V_{\text{cone}} = \frac{1}{3}\pi r^2 h = 12\pi \implies \pi r^2 h = 36\pi$
$V_{\text{cylinder}} = \pi r^2 h = 36\pi$

[Hard] A cube of side 6 has a cylinder of radius 3, height 6 drilled through its center. Find remaining volume.

$V_{\text{cube}} = 216$, $V_{\text{cylinder}} = 54\pi$, $V_{\text{remaining}} = 216 - 54\pi$

[Hard] A prism has volume $V$. Length doubled, width tripled, height halved. New volume?

$(2l)(3w)(\frac{1}{2}h) = 3lwh = 3V$

[Hard] A sphere of radius 6 has density 2.5 g/cm$^3$. Find mass.

$V = \frac{4}{3}\pi(6)^3 = 288\pi$ cm$^3$
$m = 2.5 \cdot 288\pi = 720\pi$ grams

---

## B4.3 Lines, Angles & Triangles

### Angle Basics

| Relationship | Rule |
|-------------|------|
| Complementary | Sum = $90^\circ$ |
| Supplementary | Sum = $180^\circ$ |
| Vertical angles | **Equal** |
| Linear pair | Supplementary |

### Parallel Lines Cut by a Transversal

- Corresponding, alternate interior, alternate exterior: **equal**
- Same-side interior (consecutive interior): **supplementary** (sum to $180^\circ$)

❌ **Trap:** Same-side interior are supplementary, not equal.
❌ **Trap:** Assuming parallel lines — the problem must state it or mark arrowheads.

### Triangles

**Angle sum:** $A + B + C = 180^\circ$ `(* ON REFERENCE SHEET)`

**Exterior angle theorem:** Exterior angle = sum of the two remote interior angles.

**Triangle inequality:** $a + b > c$, $a + c > b$, $b + c > a$ — strict inequality.

❌ **Trap:** $a + b \geq c$ is wrong. A degenerate triangle (3, 4, 7) is **not** valid.

**Isosceles:** Two equal sides, two equal base angles.
**Equilateral:** All sides equal, all angles $60^\circ$. Height = $\frac{s\sqrt{3}}{2}$, area = $\frac{s^2\sqrt{3}}{4}$ `[MEMORIZE for speed; otherwise derivable via 30-60-90]`.

### Polygons

Interior angle sum: $S = (n - 2) \times 180^\circ$ `(MUST MEMORIZE)`

Each interior angle (regular $n$-gon): $\frac{(n-2) \times 180^\circ}{n}$
Each exterior angle (regular $n$-gon): $\frac{360^\circ}{n}$

[Medium] Two parallel lines cut by a transversal. Same-side interior angles are $2x + 30$ and $3x + 10$. Find $x$.

$(2x + 30) + (3x + 10) = 180$
$5x = 140 \implies x = 28$

❌ **Trap:** Setting them equal instead of supplementary.

[Medium] Isosceles triangle with vertex angle $40^\circ$. Find each base angle.

$2\theta + 40 = 180 \implies \theta = 70^\circ$

[Hard] A regular polygon has interior angle $156^\circ$. How many sides?

$\frac{(n-2) \times 180}{n} = 156 \implies 180n - 360 = 156n \implies 24n = 360 \implies n = 15$

[Hard] Triangle sides $x$, $x+3$, $2x-1$. Find all possible integer values of $x$.

- $x + (x+3) > 2x-1 \implies 3 > -1$ (always true)
- $x + (2x-1) > x+3 \implies 2x > 4 \implies x > 2$
- $(x+3)+(2x-1) > x \implies 3x+2 > x \implies x > -1$ (true for positive $x$)

So $x > 2$. Integer values: $3, 4, 5, \ldots$

### Similar Triangles

- **AA similarity:** Two equal angle pairs → triangles are similar. One equal angle alone does **not** establish similarity.
- Corresponding angles are equal. Corresponding sides are proportional.
- Side ratio = $k$, perimeter ratio = $k$, area ratio = $k^2$.
- $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2} = k$

❌ **Trap:** Wrong corresponding sides. Label matching vertices first.
⚡ A line parallel to one side of a triangle creates a smaller similar triangle.

**Diagram sufficiency:** Equal side lengths must be stated or marked, not visually assumed. Two pairs of equal angles establish AA similarity; a single pair does not.

[Medium] Triangles $\triangle ABC$ and $\triangle DEF$ are similar. $AB = 6$, $DE = 9$, $BC = 8$. Find $EF$.

$k = \frac{9}{6} = 1.5$, $EF = 8 \times 1.5 = 12$

### Congruent Triangles

Triangles are congruent when all three corresponding sides and angles match. The SAT tests **recognizing whether given information is sufficient** to prove congruence, not theorem names.

- Three sides (SSS), two sides + included angle (SAS), two angles + included side (ASA) are sufficient
- **HL** (hypotenuse-leg): sufficient only for right triangles
- Vertical angles alone do not establish congruence
- Equal sides must be stated or marked, not visually assumed

### Midpoint Formula

$M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$ `(MUST MEMORIZE)`

### Slope & Lines

$m = \frac{y_2 - y_1}{x_2 - x_1}$ `(MUST MEMORIZE)`

- Parallel: $m_1 = m_2$
- Perpendicular: $m_1 \cdot m_2 = -1$ (negative reciprocals)
- Horizontal: $m = 0$; Vertical: $m$ undefined

[Medium] Line $l$ has slope $\frac{2}{3}$. Perpendicular slope?

$m_{\perp} = -\frac{3}{2}$

[Hard] Line $l$ through $(1, 4)$ and $(3, 10)$. Line $m$ through $(0, 5)$ $\perp$ $l$. Equation of $m$?

$m_l = 3$, $m_m = -\frac{1}{3}$
$y - 5 = -\frac{1}{3}(x - 0) \implies y = -\frac{1}{3}x + 5$

### Transformations `[SUPPLEMENTARY — coordinate-geometry reference]`

| Transformation | Rule | Notes |
|---------------|------|-------|
| Translation by $(a,b)$ | $(x, y) \to (x + a, y + b)$ | Congruent |
| Reflection over $x$-axis | $(x, y) \to (x, -y)$ | |
| Reflection over $y$-axis | $(x, y) \to (-x, y)$ | |
| Reflection over $y = x$ | $(x, y) \to (y, x)$ | Swap coordinates |
| Rotation $90^\circ$ CW | $(x, y) \to (y, -x)$ | |
| Rotation $90^\circ$ CCW | $(x, y) \to (-y, x)$ | |
| Rotation $180^\circ$ | $(x, y) \to (-x, -y)$ | |
| Dilation by $k$ about origin | $(x, y) \to (kx, ky)$ | Area scales by $k^2$ |

❌ **Trap:** Mixing $90^\circ$ CW and CCW.
❌ **Trap:** Dilation area scales by $k^2$, not $k$. Shape is similar, not congruent (unless $k=1$).

[Medium] Point $(3, -2)$ reflected over $y$-axis, then rotated $90^\circ$ CCW.

Reflect: $(-3, -2)$
Rotate CCW: $(-(-2), -3) = (2, -3)$

[Hard] Triangle $(1,2), (3,4), (5,1)$ dilated by $k=3$ about origin. Area of image?

Original area (shoelace): $\frac{1}{2}|17 - 27| = 5$
After $k=3$, area $\times 9$: $45$

---

## B4.4 Right Triangles & Trigonometry

### Pythagorean Theorem

$a^2 + b^2 = c^2$ `[REFERENCE SHEET]`

$c$ is the hypotenuse (opposite the right angle).

**Converse:** $a^2 + b^2 = c^2 \implies$ right triangle.
- $a^2 + b^2 > c^2$ → acute triangle `[SUPPLEMENTARY]`
- $a^2 + b^2 < c^2$ → obtuse triangle `[SUPPLEMENTARY]`

❌ **Trap:** Solving for a leg: $a = \sqrt{c^2 - b^2}$, **not** $\sqrt{c^2 + b^2}$.

**Common triples (recognize instantly):**

| Triple | Multiples |
|--------|-----------|
| 3-4-5 | 6-8-10, 9-12-15, 12-16-20 |
| 5-12-13 | 10-24-26 |
| 8-15-17 | 16-30-34 |
| 7-24-25 | 14-48-50 |

⚡ Legs 5 and 12 → hypotenuse 13 instantly, no calculation.

### Special Right Triangles

**45-45-90** `(* ON REFERENCE SHEET)`: $s : s : s\sqrt{2}$ — "same-leg-root-two"

**30-60-90** `(* ON REFERENCE SHEET)`: $s : s\sqrt{3} : 2s$ where $s$ is opposite $30^\circ$ — "short-$\sqrt{3}$-double"

❌ **Trap:** Confusing which side gets $\sqrt{3}$ — longer leg (opp $60^\circ$), not hypotenuse.
❌ **Trap:** Given hypotenuse of 45-45-90, students multiply by $\sqrt{2}$ — must **divide** by $\sqrt{2}$.
❌ **Trap:** Forgetting to rationalize: $\frac{12}{\sqrt{2}} = 6\sqrt{2}$.

[Medium] A 30-60-90 triangle has hypotenuse 18. Find the longer leg.

Short leg: $18/2 = 9$
Longer leg: $9\sqrt{3}$

[Medium] A 45-45-90 triangle has hypotenuse $10\sqrt{2}$. Find each leg.

$s\sqrt{2} = 10\sqrt{2} \implies s = 10$

[Hard] An equilateral triangle of side 12 is cut by an altitude. Find area.

Height = $6\sqrt{3}$, Area = $\frac{1}{2} \cdot 12 \cdot 6\sqrt{3} = 36\sqrt{3}$

[Very Hard] Right triangle with legs $x$ and $x+7$, hypotenuse $x+8$. Find $x$.

$x^2 + (x+7)^2 = (x+8)^2$
$x^2 + x^2 + 14x + 49 = x^2 + 16x + 64$
$x^2 - 2x - 15 = 0$
$(x - 5)(x + 3) = 0 \implies x = 5$

Sides: 5, 12, 13.

### SOHCAHTOA

$$\sin\theta = \frac{\text{opp}}{\text{hyp}} \qquad \cos\theta = \frac{\text{adj}}{\text{hyp}} \qquad \tan\theta = \frac{\text{opp}}{\text{adj}}$$

`[MEMORIZE]` — These ratios are not provided on the reference sheet, so they should be memorized until recall is automatic.

✅ **Inverse trig:** $\sin^{-1}, \cos^{-1}, \tan^{-1}$ find angles from ratios. Available in Desmos — confirm degree mode.

### Cofunction Identity

$$\sin\theta = \cos(90^\circ - \theta) \qquad \cos\theta = \sin(90^\circ - \theta)$$ `[MEMORIZE]`

❌ **Trap:** In a right triangle the acute angles are complementary, so $\sin A = \cos B$ automatically.

### Pythagorean Identity `[SUPPLEMENTARY]`

$$\sin^2\theta + \cos^2\theta = 1$$

### Tangent Identity `[SUPPLEMENTARY]`

$$\tan\theta = \frac{\sin\theta}{\cos\theta}$$

[Medium] In right $\triangle ABC$ ($\angle C = 90^\circ$), $\sin A = \frac{3}{5}$. Find $\cos B$.

$A + B = 90^\circ \implies \cos B = \sin A = \frac{3}{5}$

[Medium] Right triangle sides 5, 12, 13. Find $\tan\theta$ where $\theta$ is opposite side 5.

$\tan\theta = \frac{5}{12}$

[Medium] If $\sin\theta = \frac{3}{5}$ ($\theta$ acute), find $\cos\theta$.

$\frac{9}{25} + \cos^2\theta = 1 \implies \cos^2\theta = \frac{16}{25} \implies \cos\theta = \frac{4}{5}$ (acute → positive)

> Without an acute restriction, $\cos\theta$ could be $\pm\frac{4}{5}$ depending on the quadrant.

[Hard] A ramp rises 4 ft over 9 ft horizontal. Find angle of elevation.

$\tan\theta = \frac{4}{9} \implies \theta = \tan^{-1}\left(\frac{4}{9}\right) \approx 24^\circ$

[Hard] In $\triangle ABC$, $\angle C = 90^\circ$, $\angle A = 35^\circ$, $AB = 20$ (hypotenuse). Find $BC$ (opp $A$).

$\sin 35^\circ = \frac{BC}{20} \implies BC = 20\sin 35^\circ \approx 11.47$

❌ **Trap:** Using $\cos$ when $\sin$ is correct — label the triangle first.

[Hard] If $\sin(x^\circ) = \cos(2x^\circ)$ for acute $x$, find $x$.

$\sin(x^\circ) = \cos(90 - x)^\circ$
$\cos(90 - x)^\circ = \cos(2x)^\circ$
$90 - x = 2x \implies x = 30$

> The acute-angle condition prevents other periodic solutions. Without it, $x = 30 + 120n$ would need evaluation.

[Medium] If $\tan\theta = \frac{3}{4}$ ($\theta$ acute), find $\sin\theta + \cos\theta$.

Opp = 3, adj = 4, hyp = 5
$\sin\theta = \frac{3}{5}$, $\cos\theta = \frac{4}{5}$
Sum = $\frac{7}{5}$

### Angle of Elevation / Depression

- Elevation: horizontal **up** to line of sight
- Depression: horizontal **down** to line of sight
- They are **alternate interior angles** (horizontal ∥ horizontal), so they are equal.

✅ Draw a right triangle: horizontal = adjacent, vertical = opposite, angle at observer.

---

## B4.4a Unit Circle Trigonometry

The SAT includes unit-circle concepts alongside right-triangle trig.

### Core Facts

The unit circle: $x^2 + y^2 = 1$. For any angle $\theta$ in standard position:
- $x$-coordinate of the intersection point = $\cos\theta$
- $y$-coordinate = $\sin\theta$

### Exact Values to Memorize

| Degrees | Radians | $\cos\theta$ | $\sin\theta$ |
|--------:|--------:|-------------:|-------------:|
| $0^\circ$ | $0$ | $1$ | $0$ |
| $30^\circ$ | $\pi/6$ | $\sqrt{3}/2$ | $1/2$ |
| $45^\circ$ | $\pi/4$ | $\sqrt{2}/2$ | $\sqrt{2}/2$ |
| $60^\circ$ | $\pi/3$ | $1/2$ | $\sqrt{3}/2$ |
| $90^\circ$ | $\pi/2$ | $0$ | $1$ |

### Signs by Quadrant

| Quadrant | $\cos$ | $\sin$ |
|----------|-------|-------|
| I | $+$ | $+$ |
| II | $-$ | $+$ |
| III | $-$ | $-$ |
| IV | $+$ | $-$ |

[Medium] If $\sin\theta = \frac{1}{2}$ and $\theta$ is in Quadrant II, find $\cos\theta$.

$\sin\theta = \frac{1}{2}$ → reference angle $30^\circ$. In QII, $\cos$ is negative → $\cos\theta = -\frac{\sqrt{3}}{2}$.

[Hard] If $\cos\theta = -\frac{\sqrt{2}}{2}$ and $\theta$ is in Quadrant III, find $\theta$ in degrees.

$\cos\theta = \frac{\sqrt{2}}{2}$ at $45^\circ$ reference angle. QIII $\theta = 180^\circ + 45^\circ = 225^\circ$.

---

## B4.5 Circles

### Basic Properties

$C = 2\pi r$, $A = \pi r^2$ `(* ON REFERENCE SHEET)`

### Arcs and Sectors

Arc length: $s = \frac{\theta}{360^\circ} \cdot 2\pi r$
Sector area: $A_{\text{sector}} = \frac{\theta}{360^\circ} \cdot \pi r^2$
`(Both MUST MEMORIZE)`

**Arc length** (linear distance) ≠ **arc measure** (angle in degrees).

The proportion is the same for both:
$$\frac{\text{arc length}}{\text{circumference}} = \frac{\text{sector area}}{\text{circle area}} = \frac{\text{central angle}}{360^\circ}$$

❌ **Trap:** Arc length formula uses degrees. If using $s = r\theta$, $\theta$ **must** be in radians — never substitute a degree value directly. Wrong: $s = r \cdot 60^\circ$. Correct: $s = r \cdot \frac{\pi}{3}$.
❌ **Trap:** Confusing arc length (fraction of circumference) with sector area (fraction of area).

### Radians

$2\pi$ rad = $360^\circ$ `(* ON REFERENCE SHEET)`

$$\text{radians} = \frac{\pi}{180} \times \text{degrees}$$

Arc length in radians: $s = r\theta$

[Easy] Circle radius 10, sector angle $72^\circ$. Find sector area.

$A = \frac{72}{360} \cdot \pi(10)^2 = \frac{1}{5} \cdot 100\pi = 20\pi$

[Medium] Circle radius 6, arc length $4\pi$. Find central angle in degrees.

$4\pi = \frac{\theta}{360} \cdot 12\pi \implies \frac{\theta}{360} = \frac{1}{3} \implies \theta = 120^\circ$

[Medium] Convert $150^\circ$ to radians.

$150 \times \frac{\pi}{180} = \frac{5\pi}{6}$

[Hard] Circle radius 8, sector area $32\pi$. Find arc length.

$32\pi = \frac{\theta}{360} \cdot 64\pi \implies \theta = 180^\circ$
$s = \frac{180}{360} \cdot 16\pi = 8\pi$

### Central vs. Inscribed Angles

- **Central angle:** vertex at center. Measure = intercepted arc.
- **Inscribed angle:** vertex on circle. Measure = **half** the intercepted arc.
- **Thales' theorem:** An inscribed angle subtending a diameter is $90^\circ$.

❌ **Trap:** Forgetting the $\frac{1}{2}$ factor for inscribed angles.

[Medium] Central angle $80^\circ$. Measure of inscribed angle subtending same arc?

$80/2 = 40^\circ$

[Hard] Inscribed angle $35^\circ$. Measure of intercepted arc?

$2 \times 35 = 70^\circ$

### Tangent Lines

A tangent is **perpendicular** to the radius drawn to the point of tangency.

✅ Draw the radius to the tangency point and mark the right angle immediately.

**Tangent-length property** `[SUPPLEMENTARY]`: From the same external point, tangent segments to a circle are equal in length ($PA = PB$).

### Chords

- A perpendicular from center to chord **bisects** the chord. `[OFFICIAL CORE]`
- Two chords equidistant from center are equal in length. `[SUPPLEMENTARY]`

### Circle from Diameter Endpoints

Given endpoints of a diameter:
1. Center = midpoint of endpoints (midpoint formula)
2. Diameter = distance between endpoints (distance formula)
3. Radius = half the diameter
4. Write circle equation $(x - h)^2 + (y - k)^2 = r^2$

[Medium] The endpoints of a diameter are $(2, 3)$ and $(8, -5)$. Find the circle equation.

Center: $\left(\frac{2+8}{2}, \frac{3+(-5)}{2}\right) = (5, -1)$
Diameter: $\sqrt{(8-2)^2 + (-5-3)^2} = \sqrt{36 + 64} = 10$
Radius: $5$
Equation: $(x - 5)^2 + (y + 1)^2 = 25$

### Equation of a Circle

$$(x - h)^2 + (y - k)^2 = r^2$$ `(MUST MEMORIZE)`

Center $(h, k)$, radius $r$.

❌ **Trap:** Center sign. $(x - 3)^2 + (y + 2)^2 = 25$ → center $(3, -2)$, not $(-3, 2)$.
✅ **Best method:** Ask what value of $x$ makes $(x - h) = 0$, and what value of $y$ makes $(y - k) = 0$.
❌ **Trap:** RHS = $r^2$. If RHS = 25, $r = 5$, not 25.

### Completing the Square

Given $x^2 + y^2 + Dx + Ey + F = 0$:

1. Group $x$ and $y$ terms, move constant to RHS
2. Add $(D/2)^2$ for $x$, $(E/2)^2$ for $y$ to **both** sides
3. Factor into $(x - h)^2$ and $(y - k)^2$
4. Center $(h, k)$, radius $r = \sqrt{\text{RHS}}$

❌ **Trap:** Adding $(b/2)^2$ to LHS only — must add to both sides.
❌ **Trap:** $(x + 3)^2$ means $h = -3$.

[Hard] Find center and radius of $x^2 + y^2 + 6x - 8y - 11 = 0$.

$(x^2 + 6x + 9) + (y^2 - 8y + 16) = 11 + 9 + 16$
$(x + 3)^2 + (y - 4)^2 = 36$
Center $(-3, 4)$, radius $6$

[Hard] Circle center $(2, -1)$, radius 5. Point $(2, 4)$ lies on a tangent line. Find line equation.

Center to $(2, 4)$ is vertical. Tangent $\perp$ radius → tangent is horizontal.
$y = 4$

[Medium] Circle centered at $(3, 2)$ passes through $(7, 5)$. Write equation.

$r = \sqrt{(7-3)^2 + (5-2)^2} = 5$
$(x - 3)^2 + (y - 2)^2 = 25$

[Hard] $x^2 + y^2 - 10x + 4y + 20 = 0$ represents a circle. Find area.

$(x^2 - 10x + 25) + (y^2 + 4y + 4) = -20 + 25 + 4$
$(x - 5)^2 + (y + 2)^2 = 9$
$r = 3$, $A = 9\pi$

---

---

## Mixed Practice — B4

**1 [Medium]** A rectangular prism has length 8, width 6, height 4. Find the volume.
- (A) 18 (B) 48 (C) 192 (D) 288
- $V = 8 \cdot 6 \cdot 4 = 192$ → **(C)**.
- (A) 18 = **sum of dimensions, not product**. (B) 48 = **length × width only** (2D). (D) 288 = **volume × 1.5, no basis**.

**2 [Hard]** A right triangle has legs $x$ and $x+1$, hypotenuse $x+2$. Find $x$.
- (A) 1 (B) 3 (C) 5 (D) 7
- $x^2 + (x+1)^2 = (x+2)^2 \implies x^2 + x^2+2x+1 = x^2+4x+4 \implies x^2-2x-3=0 \implies (x-3)(x+1)=0 \implies x=3$ → **(B)**.
- (A) 1 = **extraneous root of the quadratic** ($x+1$ would be 2, $x+2$ would be 3, $1^2+2^2 \neq 3^2$). (C) 5 = **guess from 3-4-5 triple similarity**. (D) 7 = **using $x+(x+1)=x+2$ instead of squares**.

**3 [Medium]** Circle center $(-2, 5)$, radius 4. Which is the equation?
- (A) $(x-2)^2+(y+5)^2=4$ (B) $(x+2)^2+(y-5)^2=4$ (C) $(x+2)^2+(y-5)^2=16$ (D) $(x-2)^2+(y+5)^2=16$
- Center $(-2,5)$ → $(x+2)+(y-5)$, radius 4 → RHS = 16 → **(C)**.
- (A) **center signs flipped and RHS not squared**: $r=2$. (B) **RHS not squared**: $r=2$. (D) **center signs flipped**.

**4 [Hard]** A 30-60-90 triangle has hypotenuse 20. Find its area.
- (A) $50\sqrt{3}$ (B) $100$ (C) $100\sqrt{3}$ (D) $200$
- Short leg = $10$, longer leg = $10\sqrt{3}$, area = $\frac{1}{2} \cdot 10 \cdot 10\sqrt{3} = 50\sqrt{3}$ → **(A)**.
- (B) 100 = **product of legs without $\frac{1}{2}$**. (C) $100\sqrt{3}$ = **missing $\frac{1}{2}$ in area**. (D) 200 = **hypotenuse $\times$ 10**.

**5 [Medium]** **(Not drawn to scale)** Triangle ABC has $AB = AC = 10$ and $BC = 12$. The diagram shows $BC$ as the base and $A$ above it, but $BC$ looks shorter than the equal sides. Find the height from $A$ to $BC$.
- The altitude splits the isosceles triangle into two right triangles with hypotenuse 10 and base 6.
- $h = \sqrt{10^2 - 6^2} = 8$.
- ❌ **Trap:** Visually estimating instead of calculating. The diagram is intentionally misleading.

---

## Desmos Strategies for Geometry

- **Circle equations:** Type `(x-h)^2+(y-k)^2=r^2` — Desmos displays the circle for visual verification.
- **Distance:** Enter $\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$ directly for the exact distance.
- **Area/volume arithmetic:** Set up the full expression (e.g., `(1/3)*π*5^2*12`) to avoid errors.
- **Inverse trig:** `sin^{-1}(0.6)` works directly — confirm the result is in the expected unit (degrees vs radians).
- **Trig in degrees:** Use `sin(35°)` with the degree symbol — Desmos defaults to **radians**.
- **Completing the square:** Do algebra on paper, use Desmos to verify the final circle.
- **Midpoint:** Type `((x1+x2)/2, (y1+y2)/2)` to check.
- **Transformations:** Compute $(x,y) \to (-y,x)$ via function composition.
- **Scaling:** Multiply by $k^2$ or $k^3$ and verify.

⚠️ **Desmos defaults to radians.** For degree trig, always include the $^\circ$ symbol or convert manually: $\text{degrees} \times \frac{\pi}{180} = \text{radians}$.

---

## Common Mistake Catalog

| # | Mistake | Why | Fix |
|---|---------|-----|-----|
| 1 | Radius vs. diameter | Problem gives diameter, formula needs radius | Halve diameter immediately |
| 2 | Circumference vs. area | $2\pi r$ vs $\pi r^2$ | C = linear, A = squared |
| 3 | Same-side interior = equal | Forgetting the one exception | They're supplementary, not equal |
| 4 | Triangle inequality with $\geq$ | Thinking $a+b=c$ is valid | Strict: $a+b > c$ |
| 5 | Inscribed angle = central | Forgetting $\frac{1}{2}$ | Inscribed = $\frac{1}{2}$ central |
| 6 | Circle center sign | $(x + 3)$ read as $h = +3$ | Flip sign: $(x + 3) \to h = -3$ |
| 7 | Completing square: forget RHS | Adding $(b/2)^2$ to LHS only | Must add to **both** sides |
| 8 | SOHCAHTOA: wrong sides | Not labeling before solving | Write opp/adj/hyp first |
| 9 | Cofunction not applied | Not recognizing $A+B=90^\circ$ | $\sin A = \cos B$ always in right triangles |
| 10 | Arc length vs. arc measure | Treating interchangeably | Length = distance, measure = angle |
| 11 | Scale factor: $k$ vs $k^2$ vs $k^3$ | Applying area scaling to volume | Area $k^2$, volume $k^3$ |
| 12 | Assuming parallel/right from diagram | Visual guess | Must be stated or marked |
| 13 | SOHCAHTOA not on reference sheet | Assuming trig is provided | **Memorize it** |
| 14 | Perimeter/SA not on reference sheet | Assuming they're given | **Memorize them** |
| 15 | No $\frac{1}{2}$ for semicircle | Treating as full circle | Semicircle = $\frac{1}{2}\pi r^2$ |

---

## B4 at a Glance (Final Revision Reference)

### Formulas by Priority

| Priority | What |
|----------|------|
| `[REFERENCE SHEET]` | Rectangle/triangle/circle area, Pythagoras, special triangle ratios, prism/cylinder/sphere/cone/pyramid volume, triangle angle sum, degrees-radians |
| `[MEMORIZE]` | Perimeter ($P=2l+2w$), trapezoid/parallelogram area, distance/midpoint/slope, SOHCAHTOA, cofunction, arc length, sector area, circle equation, $\frac{\sqrt{3}}{4}s^2$, cylinder surface area, polygon interior sum, scale factor rules |
| `[SUPPLEMENTARY]` | Shoelace, Pythagorean identity, tangent identity, full transformation table, apothem, sphere SA, extended chord theorems, 8-15-17/7-24-25 triples |

### Key Triggers

| See | Do |
|---|---|
| Diameter given | Divide by 2 |
| Similar figures | Find $k$; perimeter $k$, area $k^2$, volume $k^3$ |
| Right triangle | Pythagoras, special triangle, or SOHCAHTOA? Label sides first |
| Circle equation | "What makes $(x-h)=0$?" for center; sqrt RHS for radius |
| Tangent line | Radius $\perp$ tangent |
| Inscribed angle | Half the intercepted arc |
| Arc / sector | $\frac{\theta}{360^\circ} \times$ circumference or area |
| $s = r\theta$ | **Radians only** |
| Composite figure | Identify add vs. subtract |
| Not drawn to scale | Trust only stated measurements |
| Unit conversion | Convert before computing area/volume |

### Traps Quick-Check
- ✅ Diameter halved? Scale factor $k$ not $k^2$? Circle signs flipped? RHS squared? $\frac{1}{2}$ for semicircle/inscribed? Same-side interior = supplementary? Desmos in degree mode?
