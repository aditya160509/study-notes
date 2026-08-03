# SAT B4: GEOMETRY & TRIGONOMETRY - MASTER MANUAL

**Weight:** ~15% of Math section (5-7 of 44 questions)

**Domain cross-references:** B1 (Algebra) for coordinate geometry, systems with geometric constraints | B2 (Advanced Math) for circle equations, quadratic geometry problems | B3 (Data Analysis) for geometric probability, unit conversions

## FRAMEWORK MAP

| Official Testing Point | Manual Section |
|---|---|
| Area and volume | B4.1-B4.2 |
| Lines, angles and triangles | B4.3 |
| Right triangles and trigonometry | B4.4-B4.4.9 |
| Circles | B4.5 |

The College Board Assessment Framework defines this domain with one claim: students "solve problems that focus on perimeter, area, and volume; angles, triangles, and trigonometry; and circles." The framework explicitly lists four skill/knowledge testing points: (1) Area and volume, (2) Lines, angles, and triangles, (3) Right triangles and trigonometry, and (4) Circles. Trigonometry (sine, cosine, tangent, radian measure, unit circle ratios) and circle theorems are tested on the SAT only, not the PSAT. The framework also stresses "scale factors," "congruence, similarity, and sufficiency," "vertical angles, triangles, and parallel lines cut by a transversal," "right triangle and unit circle trigonometry," and "properties of special right triangles." Every one of those phrases maps to a section below.

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
| $s = r\theta$ | Radians only |
| Rotation about origin | Apply the rule table in B4.3.9 |
| Not drawn to scale | Trust only stated measurements |

---

## How to Use This Guide

Every concept below has four parts: (1) a plain-English **definition**, (2) a numbered **step-by-step method**, (3) **worked examples** labeled [Easy], [Medium], [Hard], and [Very Hard] with full LaTeX solutions, and (4) **common traps** (❌) plus **Desmos tips** (⚡) where the built-in calculator saves time.

Formulas tagged `[REFERENCE SHEET]` appear in Bluebook - you are not required to memorize these, but knowing the commonly used formulas saves time. `[MEMORIZE]` formulas must be automatic. `[SUPPLEMENTARY]` is useful but lower priority. Every example has a difficulty label. Wrong-answer traps are in **bold**.

The geometry domain rewards three habits more than anything else:

1. **Label the figure first.** Write down every given length and angle on a sketch before you touch a formula. Most wrong-answer traps in this domain come from mislabeled sides (see the SOHCAHTOA trap in B4.4.3).
2. **Identify the "shape family" before computing.** Is the triangle a 3-4-5 triple? A 30-60-90? Is the figure similar to another one (so $k^2$ applies)? Is the circle equation hiding behind an expanded form (so completing the square applies)? Naming the pattern first tells you which formula to reach for.
3. **Use Desmos as a second set of eyes.** The digital SAT gives you Desmos on every question. Graph the circle, type the trig expression with the degree symbol, verify the distance. But always be able to do the algebra by hand - the fastest students read the answer off the structure before the calculator finishes drawing.

---

## Most Common Question Types on the Actual Exam

These seven archetypes recur on the digital SAT. Master them and you cover most of the domain's 5-7 questions.

| # | Archetype | Where in this guide | Frequency |
|---|-----------|--------------------|-----------|
| 1 | **Circle equation from a graph** - read the center $(h,k)$ and radius $r$ off the graph, write $(x-h)^2+(y-k)^2=r^2$, or complete the square from expanded form | B4.5.8, B4.5.9 | Very high |
| 2 | **Special right triangles** - 30-60-90 and 45-45-90 with exact radicals, no calculator needed | B4.4.2 | Very high |
| 3 | **Angle of elevation / depression word problems** - draw the right triangle, apply $\tan$ (or $\sin$ / $\cos$), finish with inverse trig | B4.4.4, B4.4.8 | High |
| 4 | **Similar triangles** - shadow problems, a segment parallel to a side, side ratios and $k^2$ area scaling | B4.3.5 | High |
| 5 | **Volume with scale factor** - change one or more dimensions, track $k$, $k^2$, $k^3$ | B4.2.3 | Medium-high |
| 6 | **Trig in the coordinate plane** - unit circle signs, quadrant-based $\sin$ and $\cos$, points on the circle | B4.4.9 | Medium |
| 7 | **Transformation coordinate rules** - apply a rotation, reflection, translation, or dilation rule to a point or shape; often combined with area or distance | B4.3.9 | Medium |

**Strategy notes per type:**

- **Type 1 (circle equation):** the instant you see a circle on a graph, read the center coordinates and count grid units to the edge for the radius. The radius is NOT squared on the graph - square it when you write the equation. If you see $x^2 + y^2 + Dx + Ey + F = 0$, you must complete the square (B4.5.9). Remember: center signs flip, right side is $r^2$.
- **Type 2 (special right triangles):** memorize the two ratio families cold: $s : s : s\sqrt{2}$ and $s : s\sqrt{3} : 2s$. The entire question is usually one division or one multiplication away. If the hypotenuse is given in a 45-45-90, divide by $\sqrt{2}$; never multiply.
- **Type 3 (elevation/depression):** draw the horizontal through the observer's eye, then the line of sight. The height difference is the opposite side, the horizontal distance is the adjacent side. That makes $\tan$ your default weapon; use $\sin$ or $\cos$ when the hypotenuse is involved. Finish with $\tan^{-1}$ if the question asks for the angle.
- **Type 4 (similar triangles):** find the scale factor $k$ from one pair of corresponding sides, then apply it to the unknown side. If the question involves area, square the factor. Label corresponding vertices before you write any proportion.
- **Type 5 (volume scale factor):** separate the two things being changed. A radius change hits the squared term, a height change hits the linear term. Multiply the individual factors at the end: $\left(\frac{r_2}{r_1}\right)^2 \times \frac{h_2}{h_1}$.
- **Type 6 (unit circle trig):** recall that $\cos\theta$ is the $x$-coordinate and $\sin\theta$ is the $y$-coordinate of the point on the unit circle. Use the quadrant to fix signs, and use the special-triangle table for exact values.
- **Type 7 (transformations):** have the rule table from B4.3.9 memorized. For a sequence, apply the rules left to right, one at a time. Rigid motions (translation, reflection, rotation) preserve lengths and areas; only a dilation changes size (by $k^2$ for area).

**Exam facts:** Geometry and Trigonometry is about 15% of the digital SAT Math section (5-7 of 44 questions). Every question is calculator-allowed (Desmos). Circle questions appear only on the SAT, not the PSAT. Expect 1-2 of the B4 questions to be grid-ins (student-produced responses) - often an exact radical or a simple integer. Trigonometry is tested on the SAT but not on the PSAT 8/9.

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
| Arc length (degrees) | $s = \frac{\theta}{360^\circ} \cdot 2\pi r$ |
| Sector area (degrees) | $A = \frac{\theta}{360^\circ} \cdot \pi r^2$ |
| Arc length (radians) | $s = r\theta$ (radians only) |
| Sector area (radians) | $A = \frac{1}{2}r^2\theta$ (radians only) |
| Circle equation | $(x - h)^2 + (y - k)^2 = r^2$ |
| Cylinder surface area | $SA = 2\pi r^2 + 2\pi rh$ |
| Sphere surface area | $SA = 4\pi r^2$ |
| Rectangular prism SA | $SA = 2lw + 2wh + 2lh$ |
| Cube surface area | $SA = 6s^2$ |
| Triangle inequality | $a + b > c$ |
| Inscribed angle | $\text{angle} = \frac{1}{2} \times \text{intercepted arc}$ |
| Polygon interior sum | $(n - 2) \times 180^\circ$ |
| Radian conversion | $\text{radians} = \frac{\pi}{180} \times \text{degrees}$ |
| Slope | $m = \frac{y_2 - y_1}{x_2 - x_1}$ |
| Scale factor rules | length $\times k$, area $\times k^2$, volume $\times k^3$ |
| Sector perimeter | $P = 2r + \text{arc length}$ |
| Transformations | rule table in B4.3.9 |
| Trig exact values | table in B4.4.9 (sin 30 = 1/2, cos 60 = 1/2, tan 45 = 1, etc.) |
| Density (cross-domain B3) | $\text{density} = \frac{\text{mass}}{\text{volume}}$ |

---

## B4.1 Area & Perimeter

**Definition:** Area is the number of unit squares that fit inside a two-dimensional figure; perimeter is the total length of its boundary. Area is measured in square units, perimeter in linear units. The two are never interchangeable - a figure can have a large perimeter and a tiny area (a long thin rectangle), or a huge area and a small perimeter (a circle).

**General method for any area question:**
1. Identify the shape (or shapes) in the figure.
2. Write down the given dimensions and the dimension you need.
3. Pick the formula and substitute.
4. Check units: if the problem mixes feet and inches, or gives diameter where you need radius, convert first.

### B4.1.1 Basic Shapes (all basic shapes)

| Shape | Area | Perimeter | Notes |
|-------|------|-----------|-------|
| Rectangle | $A = lw$ `[REFERENCE SHEET]` | $P = 2l + 2w$ `[MEMORIZE]` | |
| Square | $A = s^2$ | $P = 4s$ | Rectangle special case |
| Triangle | $A = \frac{1}{2}bh$ `[REFERENCE SHEET]` | sum of sides | $b \perp h$; altitude may fall outside obtuse triangle |
| Circle | $A = \pi r^2$ `[REFERENCE SHEET]` | $C = 2\pi r$ `[REFERENCE SHEET]` | |
| Parallelogram | $A = bh$ | $P = 2(a + b)$ | $h$ $\perp$ height |
| Trapezoid | $A = \frac{1}{2}(b_1 + b_2)h$ | sum of 4 sides | $h \perp$ bases |
| Regular polygon | $A = \frac{1}{2}Pa$ `[SUPPLEMENTARY]` | $n \times \text{side}$ | $a$ = apothem |

❌ **Diameter in $A = \pi r^2$** - always halve diameter first.
❌ **Circumference ($2\pi r$) vs area ($\pi r^2$)** - one is linear, one is squared.
❌ **Parallelogram side vs height** - the height is the perpendicular distance between bases, never a slanted side. A parallelogram with slanted side 10 and perpendicular height 6 has area $6b$, not $10b$.

[Easy] A rectangle has length 12 and width 5. Find its perimeter and area.

$P = 2(12) + 2(5) = 34$
$A = 12 \cdot 5 = 60$

[Easy] A square has perimeter 28. Find its area.

Side $s = 28/4 = 7$, so $A = 7^2 = 49$.

❌ **Trap:** Perimeter is a length (units); area is a count of squares (units$^2$). Never mix the two.

[Easy] A parallelogram has base 9 and height 4. Find its area.

$A = bh = 9 \cdot 4 = 36$

[Medium] A parallelogram has area 72 and base 12. Its slanted side is 8. Find the perpendicular height.

$72 = 12h \implies h = 6$. The slanted side (8) is a distractor - it never enters the area calculation.

❌ **Trap:** Using the slanted side as the height. Height must be perpendicular to the base.

[Medium] A trapezoid has bases 8 and 12 with height 5. Find its area.

$A = \frac{1}{2}(8 + 12)(5) = 50$

[Hard] A regular hexagon has side 6. Find its area.

A regular hexagon splits into 6 equilateral triangles of side 6. Each equilateral triangle has area $\frac{s^2\sqrt{3}}{4} = \frac{36\sqrt{3}}{4} = 9\sqrt{3}$.
Total: $6 \cdot 9\sqrt{3} = 54\sqrt{3}$.

⚡ The regular-hexagon trick: it is always 6 equilateral triangles, so $A = 6 \cdot \frac{s^2\sqrt{3}}{4} = \frac{3\sqrt{3}}{2}s^2$. This saves real time when a hexagon shows up.

### B4.1.2 Composite Figures

**Definition:** A composite figure is a shape made by joining or cutting out simpler shapes. The SAT loves these because they force you to decompose (split up) or subtract.

**Method:**
1. Identify constituent shapes (rectangle, semicircle, triangle, etc.)
2. Compute each area separately
3. Add or subtract as indicated by the figure. "Shaded region" usually means subtract; "total area" usually means add.
4. Watch for shared dimensions: a semicircle's diameter often equals a rectangle's side.

❌ **Trap:** Forgetting the $\frac{1}{2}$ factor for a semicircle, or treating "remove a circle" as "remove a semicircle." Read the figure.

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

[Hard] An L-shaped room is formed by a 12 by 8 rectangle with a 4 by 4 square cut out of one corner. Find the floor area.

Decompose into two rectangles: $12 \times 8 = 96$ minus $4 \times 4 = 16$, or split as $8 \times 8 + 4 \times 4 = 64 + 16 = 80$.
Either way: $A = 80$.

⚡ Desmos tip: type the full expression in one line, e.g. `12*8 - 4^2`, to avoid arithmetic slips.

[Very Hard] A 120 ft by 80 ft rectangular field has a circular fountain of diameter 20 ft at its center. Find the area of the grass, in square feet.

Field: $120 \cdot 80 = 9600$
Fountain radius: $10$, area: $100\pi$
Grass: $9600 - 100\pi$

✅ Desmos tip: Type `120*80 - pi*10^2` directly - Desmos keeps the answer exact in terms of $\pi$.

[Very Hard] A running track is a 100 m by 60 m rectangle with a semicircle attached to each short side. Find the total area enclosed.

Two semicircles = one full circle of radius 30: $\pi(30)^2 = 900\pi$
Rectangle: $100 \cdot 60 = 6000$
Total: $6000 + 900\pi$

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

### B4.1.3 Distance Formula (coordinate geometry)

**Definition:** The distance between two points $(x_1, y_1)$ and $(x_2, y_2)$ in the plane is the length of the straight segment joining them.

$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ `(MUST MEMORIZE)`

✅ The distance formula IS the Pythagorean theorem on the coordinate plane. The horizontal difference $(x_2 - x_1)$ is one leg, the vertical difference $(y_2 - y_1)$ is the other, and the distance is the hypotenuse.

**Method:**
1. Subtract the $x$-coordinates; square the result.
2. Subtract the $y$-coordinates; square the result.
3. Add the two squares.
4. Take the square root. (Recognize Pythagorean triples to skip the arithmetic.)

❌ **Trap:** Squaring a negative difference is fine - $(x_2 - x_1)^2 = (x_1 - x_2)^2$. Order does not matter.

[Medium] Find the distance between $(1, 2)$ and $(4, 6)$.

$d = \sqrt{(4-1)^2 + (6-2)^2} = \sqrt{9 + 16} = 5$

[Medium] Find the distance between $(-2, 3)$ and $(4, -5)$.

$d = \sqrt{(4 - (-2))^2 + (-5 - 3)^2} = \sqrt{6^2 + (-8)^2} = \sqrt{36 + 64} = 10$

❌ **Trap:** Sign errors when coordinates are negative. Write the subtraction with parentheses: $(4 - (-2))$, not $(4 - 2)$.

[Hard] A triangle has vertices $(0, 0)$, $(6, 0)$, and $(0, 8)$. Find its perimeter.

$AB = 6$, $AC = 8$, $BC = \sqrt{6^2 + 8^2} = 10$
Perimeter: $6 + 8 + 10 = 24$

⚡ This is a 6-8-10 Pythagorean triple on the coordinate plane - the distance formula is just the Pythagorean theorem in disguise.

[Hard] Show that the points $(1, 1)$, $(4, 5)$, and $(9, 1)$ form an isosceles triangle.

Distances from $(4,5)$:
$d_1 = \sqrt{(4-1)^2 + (5-1)^2} = \sqrt{9 + 16} = 5$
$d_2 = \sqrt{(9-4)^2 + (1-5)^2} = \sqrt{25 + 16} = \sqrt{41}$
Base: $\sqrt{(9-1)^2 + 0} = 8$
Two sides are 5 and $\sqrt{41}$; the base is 8, so this is NOT isosceles. (To be isosceles we would need two equal sides.)

❌ **Trap:** Proving isosceles requires computing all three distances - guessing from the picture is how the "not drawn to scale" note punishes you.

✅ Desmos tip: Type `sqrt((x2-x1)^2+(y2-y1)^2)` with the actual coordinates to check any distance in seconds.

### B4.1.4 Coordinate Area: Area of a Polygon Given Vertices

**Definition:** The area of a polygon whose vertices are given as coordinates can be found two ways: (1) decompose into triangles/rectangles, or (2) use the shoelace formula, which sums products of coordinates around the polygon.

**Shoelace formula** `[SUPPLEMENTARY]`:

$$A = \frac{1}{2}\left|\sum_{i} x_i y_{i+1} - \sum_{i} y_i x_{i+1}\right|$$

**Method (shoelace):**
1. List the vertices in order around the polygon (clockwise or counterclockwise).
2. Repeat the first vertex at the end.
3. For each consecutive pair, compute $x_i y_{i+1}$ (down-diagonal products) and $y_i x_{i+1}$ (up-diagonal products).
4. Sum each column; take half the absolute difference.

**Method (decomposition):** Draw the smallest bounding rectangle around the polygon, then subtract the right triangles that lie outside the polygon. No formula to memorize.

❌ **Trap:** For shoelace, the vertices must be listed in order around the polygon (clockwise or counterclockwise). A crossed ordering gives the area of a self-intersecting shape.

[Hard] Polygon with vertices $(1, 1)$, $(5, 1)$, $(6, 4)$, $(2, 5)$. Find its area by decomposition.

Bounding rectangle: $x$ from 1 to 6, $y$ from 1 to 5, area $5 \cdot 4 = 20$.
Outside pieces: bottom-right right triangle (base 1, height 3): $\frac{3}{2}$; top right triangle (base 4, height 1): $2$; left right triangle (base 1, height 4): $2$.
Polygon area: $20 - \frac{3}{2} - 2 - 2 = 14.5$

[Medium] Find the area of the triangle with vertices $(0,0)$, $(5,0)$, $(2,4)$.

Method 1 (decomposition): base $= 5$ on the $x$-axis, height $= 4$ (the $y$-coordinate of the top vertex). $A = \frac{1}{2}(5)(4) = 10$.
Method 2 (shoelace): $x_i y_{i+1}$: $0 + 20 + 0 = 20$; $y_i x_{i+1}$: $0 + 0 + 0 = 0$. $A = \frac{1}{2}|20 - 0| = 10$.

⚡ For a triangle with one side on an axis, the base and height are visible: base is the axis segment, height is the third vertex's other coordinate. No formula needed.

[Hard] Find the area of the quadrilateral with vertices $(-2, 1)$, $(2, 3)$, $(3, -1)$, $(-1, -2)$ by shoelace.

List in order and repeat the first vertex:

| $x$ | $y$ | $x_i y_{i+1}$ | $y_i x_{i+1}$ |
| --- | --- | --- | --- |
| -2 | 1 | (-2)(3) = -6 | (1)(2) = 2 |
| 2 | 3 | (2)(-1) = -2 | (3)(3) = 9 |
| 3 | -1 | (3)(-2) = -6 | (-1)(-1) = 1 |
| -1 | -2 | (-1)(1) = -1 | (-2)(-2) = 4 |
| -2 | 1 | - | - |

Sum down: $-6 + (-2) + (-6) + (-1) = -15$
Sum up: $2 + 9 + 1 + 4 = 16$
$A = \frac{1}{2}|-15 - 16| = \frac{31}{2} = 15.5$

❌ **Trap:** Negative products are fine; the absolute value at the end fixes the sign. Do not drop negatives mid-sum.

[Very Hard] The points $(0,0)$, $(8,0)$, $(10,4)$, and $(2,4)$ form a parallelogram. Verify with shoelace that its area equals the base-times-height result.

Base: 8 (bottom edge), height: 4 (vertical separation between the two horizontal edges). $A = bh = 32$.
Shoelace: down: $0 + 32 + 40 + 0 = 72$; up: $0 + 0 + 8 + 0 = 8$. $A = \frac{1}{2}|72 - 8| = 32$. They match.

⚡ Desmos tip: plot the points as a table, then use the polygon tool (or the `polygon` function) - Desmos can display the area. Use it to check shoelace arithmetic.

---

## B4.2 Volume & Surface Area

**Definition:** Volume is the amount of three-dimensional space inside a solid (cubic units). Surface area is the total area of all its faces (square units). The SAT primarily tests volume; surface area shows up less often, so prioritize the volume formulas and the scale-factor rules below.

### B4.2.1 Volume Formulas

The standard solid-volume formulas listed below appear on the reference sheet `[REFERENCE SHEET]`. Surface area formulas `[MEMORIZE]`.

| Shape | Volume | Surface Area |
|-------|--------|-------------|
| Rectangular prism | $V = lwh$ | $SA = 2lw + 2wh + 2lh$ `[MEMORIZE]` |
| Cube | $V = s^3$ | $SA = 6s^2$ `[MEMORIZE]` |
| Right circular cylinder | $V = \pi r^2 h$ | $SA = 2\pi r^2 + 2\pi rh$ `[MEMORIZE]` |
| Sphere | $V = \frac{4}{3}\pi r^3$ | $SA = 4\pi r^2$ `[SUPPLEMENTARY]` |
| Right circular cone | $V = \frac{1}{3}\pi r^2 h$ | rarely tested |
| Rectangular pyramid | $V = \frac{1}{3}Bh$ | rarely tested |

**The one organizing idea:** any prism has $V = B \cdot h$ (base area times height), and any pyramid or cone has $V = \frac{1}{3}B \cdot h$. The cylinder formula is just $B = \pi r^2$ plugged into the prism idea; the cone is the same base plugged into the pyramid idea. If you remember this, you never need to memorize a prism formula again.

❌ **Radius vs diameter** - cylinder with diameter 10 → $r = 5$.
❌ **Confusing $\frac{1}{3}$ (cone/pyramid) with $\frac{4}{3}$ (sphere).**
❌ **Forgetting the $2$ in $SA = 2\pi r^2 + 2\pi rh$** (top and bottom).

[Easy] A cylinder has radius 3 and height 8. Find its volume.

$V = \pi r^2 h = \pi(9)(8) = 72\pi$

[Easy] A sphere has radius 6. Find its volume.

$V = \frac{4}{3}\pi (6)^3 = \frac{4}{3}\pi (216) = 288\pi$

[Medium] A cylinder has volume $72\pi$ and radius 3. Find its height.

$72\pi = \pi(3)^2 h = 9\pi h \implies h = 8$

⚡ The official "work backwards" pattern: given a volume, solve for an unknown dimension. Don't stop at $r^2 = 9$ if the question asks for the diameter or height.

[Medium] A cone has radius 5 and height 12. Find its volume.

$V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi(25)(12) = 100\pi$

[Hard] A sphere has volume $288\pi$. Find its radius.

$\frac{4}{3}\pi r^3 = 288\pi \implies r^3 = 288 \cdot \frac{3}{4} = 216 \implies r = 6$

⚡ Cube-root recognition: $216 = 6^3$, $125 = 5^3$, $64 = 4^3$, $27 = 3^3$, $8 = 2^3$. Sphere-volume questions almost always use a perfect cube.

[Very Hard] A triangular prism has a right-triangle base with legs 6 and 8, and length 10. Find its volume.

Base area: $\frac{1}{2}(6)(8) = 24$; $V = 24 \cdot 10 = 240$

✅ Any prism (not just rectangular): $V = B \cdot h$, where $B$ is the area of the base face and $h$ is the distance between bases.

[Very Hard] A hemisphere (half a sphere) has radius 3 and sits on a cylinder of radius 3 and height 5. Find the total volume of the solid.

Hemisphere: $\frac{1}{2} \cdot \frac{4}{3}\pi(3)^3 = \frac{1}{2} \cdot 36\pi = 18\pi$
Cylinder: $\pi(3)^2(5) = 45\pi$
Total: $18\pi + 45\pi = 63\pi$

❌ **Trap:** The hemisphere is half a sphere, not a cone. Write the sphere volume, then multiply by $\frac{1}{2}$.

### B4.2.2 Surface Area

**Definition:** Surface area is the total area of every face of a solid. Surface area is tested less often than volume on the digital SAT. Memorize the rectangular prism, cube, and cylinder formulas; for any other solid, build the surface from its faces (the net). If you need a formula that is not on the reference sheet and not one of these three, the problem usually provides it.

**Method (net approach for unfamiliar solids):**
1. Unfold the solid mentally into flat faces.
2. Compute the area of each face.
3. Add them all. Watch for faces that are identical (top/bottom, front/back).

[Easy] A cube has edge 5. Find its surface area.

$SA = 6s^2 = 6(25) = 150$

[Medium] A cylinder has radius 3 and height 10. Find its surface area.

$SA = 2\pi r^2 + 2\pi rh = 2\pi(9) + 2\pi(3)(10) = 18\pi + 60\pi = 78\pi$

❌ **Trap:** Forgetting the $2\pi r^2$ term (the two circular ends). The curved part alone is $60\pi$, the total is $78\pi$.

[Hard] An open-top box has length 10, width 6, and height 4. Find the surface area (no lid).

Bottom: $10 \cdot 6 = 60$; two long sides: $2(10 \cdot 4) = 80$; two short sides: $2(6 \cdot 4) = 48$.
Total: $60 + 80 + 48 = 188$.

❌ **Trap:** "Open-top" means subtract one $lw$ face, not one of each. If you used the full formula you would get $2(60) + 2(40) + 2(24) = 248$; the correct answer is $188$.

[Hard] A rectangular prism has volume 120 and a square base of side 4. Find its surface area.

Height: $h = \frac{120}{16} = 7.5$.
$SA = 2(16) + 4(4 \cdot 7.5) = 32 + 120 = 152$.

⚡ The four side faces of a square-based prism are identical, so one side area times 4 works.

### B4.2.3 Scale Factors: Length, Area, and Volume

**Definition:** Two figures are similar when one is a scaled copy of the other. The scale factor $k$ is the ratio of any two corresponding lengths. The single most important rule in this domain:

- Linear scale factor $k$ → **perimeter** and **circumference** scale by $k$
- **Area** scales by $k^2$
- **Volume** scales by $k^3$

**Why it works:** area is a product of two lengths ($l \times w$, $\pi r^2$, $\frac{1}{2}bh$), so scaling both lengths by $k$ multiplies the product by $k \cdot k = k^2$. Volume is a product of three lengths, so it scales by $k^3$.

**Method:**
1. Find $k$ from any pair of corresponding linear dimensions (sides, radii, heights, perimeters).
2. Decide what the question wants: length ($k$), area ($k^2$), or volume ($k^3$).
3. Apply the correct power. Never apply $k^2$ to volume or $k^3$ to area.
4. If two different dimensions change by different factors, apply each factor to the right part of the formula, then multiply.

❌ **Trap:** Applying $k^2$ for volume or $k^3$ for area.
❌ **Trap:** Forgetting that perimeter/circumference scale by $k$, not $k^2$.

[Easy] A square has side 3. A similar square has side 9. What is the ratio of their areas?

$k = \frac{9}{3} = 3$; area ratio $= k^2 = 9$.

[Medium] Two similar cylinders have radii 2 and 6. The smaller has volume $10\pi$. Find the larger's volume.

$k = 3$, so volume scales by $k^3 = 27$. Larger: $270\pi$.

❌ **Trap:** Using $k^2 = 9$ for a volume question. Same shape, same $k$, but volume needs the cube.

[Hard] A sphere's radius is doubled. By what factor does its surface area increase?

$SA = 4\pi r^2$; new: $4\pi(2r)^2 = 16\pi r^2 = 4 \cdot 4\pi r^2$. Factor of 4 ($k^2$).

[Hard] A circle's circumference is tripled. By what factor does its area increase?

Circumference scales by $k$, so $k = 3$. Area scales by $k^2 = 9$.

⚡ The circumference-to-area chain is a favorite: they give you the linear change and ask for the squared effect (or vice versa). Find $k$ first, then power it.

[Very Hard] A cone has volume $V$. Its radius is tripled and its height is halved. Find the new volume in terms of $V$.

New radius $3r$: base area scales by $3^2 = 9$. New height: $\frac{h}{2}$.
New volume: $9 \cdot \frac{1}{2} \cdot V = \frac{9}{2}V$

❌ **Trap:** Apply each dimension's scale factor to the right part of the formula: a radius change affects the $r^2$ (area) term, a height change affects the linear term. Then multiply the factors.

[Very Hard] A rectangular prism is enlarged so that every edge is multiplied by $k$. Its volume becomes 8 times larger. What happens to its surface area?

$k^3 = 8 \implies k = 2$. Surface area scales by $k^2 = 4$.

[Medium] A sphere has volume $36\pi$. Find its surface area.

$V = \frac{4}{3}\pi r^3 = 36\pi \implies r^3 = 27 \implies r = 3$
$SA = 4\pi(9) = 36\pi$

[Hard] A cone and a cylinder share radius $r$ and height $h$. Cone volume is $12\pi$. Find cylinder volume.

$V_{\text{cone}} = \frac{1}{3}\pi r^2 h = 12\pi \implies \pi r^2 h = 36\pi$
$V_{\text{cylinder}} = \pi r^2 h = 36\pi$

⚡ Same radius and height, the cylinder is always exactly 3 times the cone. Remember the "3 times" shortcut.

[Hard] A cube of side 6 has a cylinder of radius 3, height 6 drilled through its center. Find remaining volume.

$V_{\text{cube}} = 216$, $V_{\text{cylinder}} = 54\pi$, $V_{\text{remaining}} = 216 - 54\pi$

[Hard] A prism has volume $V$. Length doubled, width tripled, height halved. New volume?

$(2l)(3w)(\frac{1}{2}h) = 3lwh = 3V$

[Hard] A sphere of radius 6 has density 2.5 g/cm$^3$. Find mass.

$V = \frac{4}{3}\pi(6)^3 = 288\pi$ cm$^3$
$m = 2.5 \cdot 288\pi = 720\pi$ grams

[Hard] Water fills a cylinder of radius 4 to a height of 10. All the water is poured into a second cylinder of radius 8. What is the new water height?

Volume is conserved: $\pi(4)^2(10) = \pi(8)^2 h \implies 160\pi = 64\pi h \implies h = 2.5$.

❌ **Trap:** Doubling the radius quarters the height (since $r^2$ appears). The answer is not 5; it is $10/4 = 2.5$.

---

## B4.3 Lines, Angles & Triangles

### B4.3.1 Angle Basics

**Definitions:**
- **Complementary angles:** two angles whose measures sum to $90^\circ$.
- **Supplementary angles:** two angles whose measures sum to $180^\circ$.
- **Vertical angles:** the opposite angles formed by two intersecting lines; they are **equal**.
- **Linear pair:** two adjacent angles whose non-shared sides form a straight line; they are **supplementary**.

| Relationship | Rule |
|-------------|------|
| Complementary | Sum = $90^\circ$ |
| Supplementary | Sum = $180^\circ$ |
| Vertical angles | **Equal** |
| Linear pair | Supplementary |

**Method:** write the relationship as an equation in the unknown, then solve. For vertical angles, set them equal. For linear pairs or supplementary angles, set the sum to 180.

[Easy] Two angles are complementary. One measures $32^\circ$. Find the other.

$90^\circ - 32^\circ = 58^\circ$

[Easy] Two lines intersect, forming a $47^\circ$ angle. Find the measure of its vertical angle.

Vertical angles are equal: $47^\circ$.

[Medium] Two angles form a linear pair. One measures $4x + 10$, the other $2x + 20$. Find the smaller angle.

$(4x + 10) + (2x + 20) = 180 \implies 6x = 150 \implies x = 25$
Angles: $110^\circ$ and $70^\circ$. Smaller: $70^\circ$.

❌ **Trap:** Linear pair sums to $180^\circ$ (straight line); complementary sums to $90^\circ$ (right angle). Read the wording carefully.

[Hard] Two intersecting lines create angles $3x + 15$ and $5x - 45$ that are vertical. Find the measure of each angle.

Vertical angles are equal: $3x + 15 = 5x - 45 \implies 2x = 60 \implies x = 30$.
Each angle: $3(30) + 15 = 105^\circ$.

❌ **Trap:** If the two expressions were a linear pair instead, you would add to 180. Check whether the problem says "vertical" or "adjacent."

### B4.3.2 Parallel Lines Cut by a Transversal

**Definition:** When a line (the transversal) crosses two parallel lines, it creates 8 angles with two special families of relationships.

- Corresponding, alternate interior, alternate exterior: **equal**
- Same-side interior (consecutive interior): **supplementary** (sum to $180^\circ$)

**Method:**
1. Identify the transversal (the line crossing both parallels).
2. Classify the pair of angles the problem names (corresponding? alternate interior? same-side interior?).
3. Apply equal or supplementary accordingly.

❌ **Trap:** Same-side interior are supplementary, not equal.
❌ **Trap:** Assuming parallel lines - the problem must state it or mark arrowheads.

[Easy] Two parallel lines are cut by a transversal. A pair of corresponding angles measures $(3x - 20)^\circ$ and $(x + 40)^\circ$. Find $x$.

Corresponding angles are equal: $3x - 20 = x + 40 \implies 2x = 60 \implies x = 30$

⚡ Fast check: if the diagram marks angle relationships (arcs or boxes), trust the marks; otherwise only trust stated parallel/right information.

[Medium] Two parallel lines cut by a transversal. Same-side interior angles are $2x + 30$ and $3x + 10$. Find $x$.

$(2x + 30) + (3x + 10) = 180$
$5x = 140 \implies x = 28$

❌ **Trap:** Setting them equal instead of supplementary.

[Hard] Two parallel lines are cut by a transversal. Alternate interior angles measure $4x - 25$ and $2x + 15$. Find the measure of each angle.

Equal: $4x - 25 = 2x + 15 \implies 2x = 40 \implies x = 20$.
Each angle: $4(20) - 25 = 55^\circ$.

[Hard] Three parallel lines are cut by two transversals. A $65^\circ$ angle appears between the first transversal and the middle line. What is the corresponding angle between the second transversal and the bottom line?

Every pair of parallel lines shares the same angle pattern, so corresponding angles are still $65^\circ$ regardless of which transversal is involved. Answer: $65^\circ$.

⚡ The "three parallel lines" setup is just two copies of the same rule. Do not overthink it - the angle relationships do not change.

### B4.3.3 Triangles: Angle Sum, Inequality, Special Families

**Angle sum:** $A + B + C = 180^\circ$ `(* ON REFERENCE SHEET)`

**Exterior angle theorem:** Exterior angle = sum of the two remote interior angles.

**Triangle inequality:** $a + b > c$, $a + c > b$, $b + c > a$ - strict inequality.

❌ **Trap:** $a + b \geq c$ is wrong. A degenerate triangle (3, 4, 7) is **not** valid.

**Isosceles:** Two equal sides, two equal base angles.
**Equilateral:** All sides equal, all angles $60^\circ$. Height = $\frac{s\sqrt{3}}{2}$, area = $\frac{s^2\sqrt{3}}{4}$ `[MEMORIZE for speed; otherwise derivable via 30-60-90]`.

**Method for angle questions:** two of the three angles determine the third via the angle sum. For exterior angles, add the two remote interiors. For side-existence questions, test all three triangle-inequality pairs.

[Easy] A triangle has angles $50^\circ$ and $65^\circ$. Find the third angle.

$180 - 50 - 65 = 65^\circ$

[Easy] An equilateral triangle has perimeter 36. Find its area.

Side $s = 12$. Area $= \frac{s^2\sqrt{3}}{4} = \frac{144\sqrt{3}}{4} = 36\sqrt{3}$.

[Medium] An exterior angle of a triangle is $120^\circ$. One remote interior angle is $45^\circ$. Find the other remote interior angle.

Exterior angle = sum of the two remote interior angles:
$120 = 45 + x \implies x = 75^\circ$

❌ **Trap:** The exterior angle theorem uses the remote interior angles, not the adjacent one.

[Medium] Isosceles triangle with vertex angle $40^\circ$. Find each base angle.

$2\theta + 40 = 180 \implies \theta = 70^\circ$

[Hard] Triangle sides $x$, $x+3$, $2x-1$. Find all possible integer values of $x$.

- $x + (x+3) > 2x-1 \implies 3 > -1$ (always true)
- $x + (2x-1) > x+3 \implies 2x > 4 \implies x > 2$
- $(x+3)+(2x-1) > x \implies 3x+2 > x \implies x > -1$ (true for positive $x$)

So $x > 2$. Integer values: $3, 4, 5, \ldots$

[Hard] Can a triangle have sides 5, 7, and 13?

$5 + 7 = 12 < 13$, so no. The two shorter sides must sum to more than the longest.

❌ **Trap:** Check the sum of the two SMALLEST sides against the largest. That single check decides the whole question.

### B4.3.4 Polygons

**Definition:** A polygon is a closed figure made of straight segments. A regular polygon has all sides equal and all angles equal.

Interior angle sum: $S = (n - 2) \times 180^\circ$ `(MUST MEMORIZE)`

Each interior angle (regular $n$-gon): $\frac{(n-2) \times 180^\circ}{n}$
Each exterior angle (regular $n$-gon): $\frac{360^\circ}{n}$

**Method:** the exterior-angle route is almost always faster for regular polygons because exterior angles of any polygon sum to $360^\circ$, so each exterior angle of a regular $n$-gon is $\frac{360}{n}$.

[Easy] A regular pentagon has 5 sides. Find each interior angle.

$\frac{(5-2) \times 180}{5} = \frac{540}{5} = 108^\circ$

[Medium] A regular polygon has 12 sides. Find each exterior angle.

$\frac{360}{12} = 30^\circ$

⚡ Exterior angles of any polygon sum to $360^\circ$, so each exterior angle of a regular $n$-gon is $\frac{360}{n}$ - often faster than the interior-angle formula.

[Hard] A regular polygon has interior angle $156^\circ$. How many sides?

$\frac{(n-2) \times 180}{n} = 156 \implies 180n - 360 = 156n \implies 24n = 360 \implies n = 15$

⚡ Alternative via exterior angles: interior $156^\circ$ means exterior $24^\circ$, and $\frac{360}{24} = 15$. Two lines instead of four.

[Hard] The sum of the interior angles of a polygon is $2160^\circ$. How many sides does it have?

$(n-2) \times 180 = 2160 \implies n - 2 = 12 \implies n = 14$

### B4.3.5 Similar Triangles

**Definition:** Two triangles are similar when they have the same shape: corresponding angles equal, corresponding sides proportional. The scale factor $k$ is the ratio of any pair of corresponding sides.

- **AA similarity:** Two equal angle pairs → triangles are similar. One equal angle alone does **not** establish similarity.
- Corresponding angles are equal. Corresponding sides are proportional.
- Side ratio = $k$, perimeter ratio = $k$, area ratio = $k^2$.
- $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2} = k$

**Method:**
1. Label the corresponding vertices (same position in each triangle's name).
2. Find $k$ from one known pair of corresponding sides.
3. Apply $k$ to the unknown side (multiply the small side by $k$, or divide the large side by $k$).
4. For area questions, square $k$.

❌ **Trap:** Wrong corresponding sides. Label matching vertices first.
⚡ A line parallel to one side of a triangle creates a smaller similar triangle.

**Diagram sufficiency:** Equal side lengths must be stated or marked, not visually assumed. Two pairs of equal angles establish AA similarity; a single pair does not.

[Medium] Triangles $\triangle ABC$ and $\triangle DEF$ are similar. $AB = 6$, $DE = 9$, $BC = 8$. Find $EF$.

$k = \frac{9}{6} = 1.5$, $EF = 8 \times 1.5 = 12$

[Hard] At the same time of day, a 10-foot tree casts a 5-foot shadow and a nearby building casts a 40-foot shadow. How tall is the building?

Similar right triangles: $\frac{10}{5} = \frac{h}{40} \implies h = 80$ feet

⚡ This is the official framework's model question: shadow problems are the most common similarity setup on the SAT.

[Hard] In $\triangle ABC$, segment $DE \parallel BC$ with $D$ on $AB$ and $E$ on $AC$. $AD = 4$, $DB = 8$, $DE = 6$. Find $BC$.

$\triangle ADE \sim \triangle ABC$ with $k = \frac{AD}{AB} = \frac{4}{12} = \frac{1}{3}$.
$BC = DE \cdot 3 = 18$

❌ **Trap:** The scale factor uses the WHOLE side $AB = AD + DB = 12$, not just $AD = 4$. Forgetting to add $AD + DB$ is the classic error.

[Hard] Two similar triangles have perimeters 30 and 45. The area of the smaller is 20. Find the area of the larger.

$k = \frac{45}{30} = 1.5$; area scales by $k^2 = 2.25$: $20 \cdot 2.25 = 45$

[Very Hard] A flagpole casts a shadow of 24 m. A 1.6 m person standing next to it casts a shadow of 2 m. Find the height of the flagpole.

$\frac{h}{24} = \frac{1.6}{2} \implies h = 24 \cdot 0.8 = 19.2$ m

⚡ Set up the proportion as $\frac{\text{height}}{\text{shadow}}$ on both sides; mixing up which quantity goes on top is the most common error.

[Very Hard] In $\triangle ABC$, point $D$ is on $AB$ and $E$ is on $AC$ with $DE \parallel BC$. $AD = 3$, $DB = 9$, and the area of $\triangle ADE$ is 5. Find the area of $\triangle ABC$.

$k = \frac{AD}{AB} = \frac{3}{12} = \frac{1}{4}$. Area of $\triangle ADE$ is $k^2 = \frac{1}{16}$ of the area of $\triangle ABC$.
$\triangle ABC$ area $= 5 \cdot 16 = 80$.

❌ **Trap:** $k = \frac{1}{4}$ means the small triangle is $\frac{1}{16}$ of the big one - students often square the wrong direction and get $5 \cdot 4 = 20$. The areas differ by $k^2$, not $k$.

### B4.3.6 Congruent Triangles

**Definition:** Triangles are congruent when all three corresponding sides and angles match - same size AND same shape. The SAT tests **recognizing whether given information is sufficient** to prove congruence, not theorem names.

- Three sides (SSS), two sides + included angle (SAS), two angles + included side (ASA) are sufficient
- **HL** (hypotenuse-leg): sufficient only for right triangles
- **AAS** (two angles + a non-included side): also sufficient
- Vertical angles alone do not establish congruence

[Medium] In $\triangle ABC$ and $\triangle DEF$: $AB = DE$, $BC = EF$, and $\angle B = \angle E$. Is this sufficient to prove congruence?

Yes - two sides and the included angle (SAS). $\angle B$ lies between $AB$ and $BC$.

❌ **Trap:** SAS requires the angle between the two sides. Two sides plus a non-included angle (SSA) is not sufficient - it can describe two different triangles.

[Hard] In $\triangle PQR$ and $\triangle STU$: $\angle P = \angle S$, $\angle Q = \angle T$, and $PQ = ST$. Is this sufficient to prove congruence?

Yes - two angles and the included side (ASA). The side $PQ$ lies between $\angle P$ and $\angle Q$.

[Hard] Two right triangles each have hypotenuse 13 and one leg 5. Must they be congruent?

Yes - HL (hypotenuse-leg) applies to right triangles, and by Pythagoras the third side is forced to be 12 in both.

❌ **Trap:** For non-right triangles, "two sides and a non-included angle" (SSA) does NOT guarantee congruence. It does for right triangles via HL.
- Equal sides must be stated or marked, not visually assumed

### B4.3.7 Midpoint Formula

**Definition:** The midpoint of a segment is the point exactly halfway between its endpoints.

$M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$ `(MUST MEMORIZE)`

**Method:** average the $x$-coordinates and average the $y$-coordinates. To find a missing endpoint, work backwards: an endpoint equals $2 \times$ midpoint minus the other endpoint.

[Easy] Find the midpoint of the segment from $(2, 3)$ to $(6, 9)$.

$M = \left(\frac{2+6}{2}, \frac{3+9}{2}\right) = (4, 6)$

[Medium] The midpoint of segment $AB$ is $(3, -1)$ and $A = (1, 5)$. Find $B$.

$\frac{1 + x_B}{2} = 3 \implies x_B = 5$; $\frac{5 + y_B}{2} = -1 \implies y_B = -7$. So $B = (5, -7)$.

❌ **Trap:** Work backwards carefully: an endpoint equals $2 \times$ midpoint minus the other endpoint.

[Hard] A circle has a diameter with endpoints $(-4, 2)$ and $(8, 6)$. Find the center.

The center of a circle is the midpoint of any diameter:
$M = \left(\frac{-4 + 8}{2}, \frac{2 + 6}{2}\right) = (2, 4)$

⚡ Circle center from endpoints is a midpoint question in disguise - see B4.5.7 for the full pipeline.

### B4.3.8 Slope & Lines (Coordinate Geometry)

**Definition:** Slope measures how steep a line is: the vertical change per unit of horizontal change.

$m = \frac{y_2 - y_1}{x_2 - x_1}$ `(MUST MEMORIZE)`

- Parallel: $m_1 = m_2$
- Perpendicular: $m_1 \cdot m_2 = -1$ (negative reciprocals)
- Horizontal: $m = 0$; Vertical: $m$ undefined

**Method:** plug two points into the slope formula. For perpendicular slopes, flip the fraction and change the sign. On the digital SAT, slope is often presented as a rate of change in a word problem: "the height increases by 3 feet per second" means slope 3.

[Medium] Line $l$ has slope $\frac{2}{3}$. Perpendicular slope?

$m_{\perp} = -\frac{3}{2}$

[Hard] Line $l$ through $(1, 4)$ and $(3, 10)$. Line $m$ through $(0, 5)$ $\perp$ $l$. Equation of $m$?

$m_l = 3$, $m_m = -\frac{1}{3}$
$y - 5 = -\frac{1}{3}(x - 0) \implies y = -\frac{1}{3}x + 5$

[Easy] Lines $y = 3x + 2$ and $y = 3x - 7$: parallel or perpendicular?

Same slope (3) -> parallel.

[Medium] A line passes through $(2, 5)$ and $(6, 11)$. Find its slope and interpret it as a rate of change.

$m = \frac{11 - 5}{6 - 2} = \frac{6}{4} = 1.5$

In context, $y$ increases by 1.5 for every 1-unit increase in $x$ (e.g., $\$1.50$ per item).

[Hard] Line $l$: $2x + 3y = 12$. Find the slope of a line perpendicular to $l$.

$y = -\frac{2}{3}x + 4$, so $m_l = -\frac{2}{3}$ and $m_\perp = \frac{3}{2}$

❌ **Trap:** Horizontal lines have slope 0; vertical lines have undefined slope. The line perpendicular to a horizontal line is vertical - "negative reciprocal of 0" is undefined, not 0.

### B4.3.9 Transformations (Coordinate Geometry)

**Definition:** A transformation moves or changes a figure on the coordinate plane. Three types are **rigid motions** (they preserve size and shape): translation (slide), reflection (flip), and rotation (turn). A **dilation** (stretch or shrink) changes size unless $k = 1$.

| Transformation | Rule | Notes |
|---------------|------|-------|
| Translation by $(a,b)$ | $(x, y) \to (x + a, y + b)$ | Rigid: congruent |
| Reflection over $x$-axis | $(x, y) \to (x, -y)$ | Rigid |
| Reflection over $y$-axis | $(x, y) \to (-x, y)$ | Rigid |
| Reflection over $y = x$ | $(x, y) \to (y, x)$ | Swap coordinates; rigid |
| Reflection over $y = -x$ | $(x, y) \to (-y, -x)$ | `[SUPPLEMENTARY]` |
| Rotation $90^\circ$ CCW about origin | $(x, y) \to (-y, x)$ | Rigid |
| Rotation $90^\circ$ CW about origin | $(x, y) \to (y, -x)$ | Rigid |
| Rotation $180^\circ$ about origin | $(x, y) \to (-x, -y)$ | Rigid |
| Rotation $270^\circ$ CCW about origin | $(x, y) \to (y, -x)$ | Same as $90^\circ$ CW; rigid |
| Rotation $270^\circ$ CW about origin | $(x, y) \to (-y, x)$ | Same as $90^\circ$ CCW; rigid |
| Dilation by $k$ about origin | $(x, y) \to (kx, ky)$ | Area scales by $k^2$; similar, not congruent (unless $k = 1$) |

**Method (any single transformation):** identify the transformation from the wording, look up its rule, apply the rule to every vertex (for a shape) or to the single point (for a point question).

**Method (sequence of transformations):** apply the rules left to right, one at a time. The output of the first step is the input of the second. Order matters - reflect-then-translate is generally NOT the same as translate-then-reflect.

**Memory aids:**
- Rotations about the origin: $90^\circ$ CCW is "swap, then negate the new first coordinate": $(x,y) \to (-y, x)$. $180^\circ$ just negates both. Everything else is a combination of these two.
- Reflections over the axes just flip one sign. Reflection over $y = x$ swaps coordinates.
- Dilation about the origin multiplies both coordinates by $k$.

❌ **Trap:** Mixing $90^\circ$ CW and CCW.
❌ **Trap:** Dilation area scales by $k^2$, not $k$. Shape is similar, not congruent (unless $k=1$).
❌ **Trap:** Order matters when combining transformations. Reflect-then-translate is not the same as translate-then-reflect.

[Easy] Translate point $(4, -3)$ by the vector $(-2, 5)$.

$(4 - 2, -3 + 5) = (2, 2)$

[Easy] Reflect point $(3, 5)$ over the $x$-axis.

$(x, y) \to (x, -y)$: $(3, 5) \to (3, -5)$

[Easy] Reflect point $(-2, 4)$ over the $y$-axis.

$(x, y) \to (-x, y)$: $(-2, 4) \to (2, 4)$

[Easy] Rotate point $(2, 3)$ by $180^\circ$ about the origin.

$(x, y) \to (-x, -y)$: $(2, 3) \to (-2, -3)$

[Medium] Reflect point $(5, 2)$ over the line $y = x$.

$(5, 2) \to (2, 5)$ - swap coordinates.

[Medium] Rotate point $(2, 3)$ by $90^\circ$ counterclockwise about the origin.

$(x, y) \to (-y, x)$: $(2, 3) \to (-3, 2)$

[Medium] Rotate point $(2, 3)$ by $90^\circ$ clockwise about the origin.

$(x, y) \to (y, -x)$: $(2, 3) \to (3, -2)$

❌ **Trap:** CCW and CW are mirror rules. Check with a mental picture: the point $(2,3)$ is in Quadrant I, slightly above the $45^\circ$ line. Rotating CCW (counterclockwise) should push it toward the negative $x$-axis: $(-3, 2)$ is in Quadrant II. Rotating CW pushes it toward the positive $y$-axis: $(3, -2)$ is in Quadrant IV.

[Medium] Point $(3, -2)$ reflected over $y$-axis, then rotated $90^\circ$ CCW.

Reflect: $(-3, -2)$
Rotate CCW: $(-(-2), -3) = (2, -3)$

[Hard] Rotate point $(-3, 4)$ by $270^\circ$ counterclockwise about the origin.

$270^\circ$ CCW equals $90^\circ$ CW: $(x, y) \to (y, -x)$. So $(-3, 4) \to (4, 3)$.

[Hard] Reflect point $(2, 3)$ over the $y$-axis, then translate by $(5, -1)$.

Reflect: $(-2, 3)$; translate: $(-2 + 5, 3 - 1) = (3, 2)$

[Hard] Translate point $(2, 3)$ by $(5, -1)$, then reflect over the $y$-axis. Compare with the previous example.

Translate: $(7, 2)$; reflect: $(-7, 2)$. The previous example gave $(3, 2)$. Different - order matters.

❌ **Trap:** The order of operations in a sequence is fixed. Read "then" literally.

[Hard] A triangle with vertices $(0,0)$, $(4,0)$, $(0,3)$ is rotated $90^\circ$ clockwise about the origin. Find the area of the image.

Rotations are rigid motions (congruence): area is unchanged.
Original area: $\frac{1}{2}(4)(3) = 6$. Image area: 6.

❌ **Trap:** Rotations, reflections, and translations preserve length and area. Only dilations change size.

[Hard] Triangle $(1,2), (3,4), (5,1)$ dilated by $k=3$ about origin. Area of image?

Original area (shoelace): $\frac{1}{2}|17 - 27| = 5$
After $k=3$, area $\times 9$: $45$

[Hard] Rotate the point $(5, 1)$ by $270^\circ$ clockwise about the origin.

$270^\circ$ CW equals $90^\circ$ CCW: $(x, y) \to (-y, x)$. So $(5, 1) \to (-1, 5)$.

[Very Hard] Triangle $A(1, 1)$, $B(3, 1)$, $C(2, 4)$ is dilated by factor 2 about the point $(1, 1)$ (not the origin). Find the new vertices.

For each point: subtract the center, scale, add the center back.
$A$: $(0,0) \to (0,0) \to A'(1,1)$
$B$: $(2,0) \to (4,0) \to B'(5,1)$
$C$: $(1,3) \to (2,6) \to C'(3,7)$

✅ Desmos tip: Define the rule $(x,y) \to (h + k(x-h), j + k(y-j))$ as a function and apply it to each vertex to verify.

[Very Hard] A square with vertices $(1,1)$, $(3,1)$, $(3,3)$, $(1,3)$ is dilated by $k = 0.5$ about the origin, then rotated $90^\circ$ CCW. Find the coordinates of the image of $(3,3)$.

Dilate: $(3,3) \to (1.5, 1.5)$. Rotate $90^\circ$ CCW: $(1.5, 1.5) \to (-1.5, 1.5)$.

❌ **Trap:** A dilation with $k < 1$ shrinks the figure but the rules still apply exactly as written. Do not skip the dilation step.

⚡ Desmos tip: plot the original point and the transformed point; if your rules are right, the transformed point lands where the mental picture says it should.

---

## B4.4 Right Triangles & Trigonometry

### B4.4.1 Pythagorean Theorem

**Definition:** In a right triangle, the square of the hypotenuse (the longest side, opposite the right angle) equals the sum of the squares of the legs.

$a^2 + b^2 = c^2$ `[REFERENCE SHEET]`

$c$ is the hypotenuse (opposite the right angle).

**Converse:** $a^2 + b^2 = c^2 \implies$ right triangle.
- $a^2 + b^2 > c^2$ → acute triangle `[SUPPLEMENTARY]`
- $a^2 + b^2 < c^2$ → obtuse triangle `[SUPPLEMENTARY]`

**Method:**
1. Identify the hypotenuse (opposite the right angle; the longest side).
2. If the hypotenuse is unknown: $c = \sqrt{a^2 + b^2}$.
3. If a leg is unknown: $a = \sqrt{c^2 - b^2}$, **not** $\sqrt{c^2 + b^2}$.
4. Recognize triples to skip arithmetic (see table).

❌ **Trap:** Solving for a leg: $a = \sqrt{c^2 - b^2}$, **not** $\sqrt{c^2 + b^2}$.

**Common triples (recognize instantly):**

| Triple | Multiples |
|--------|-----------|
| 3-4-5 | 6-8-10, 9-12-15, 12-16-20 |
| 5-12-13 | 10-24-26 |
| 8-15-17 | 16-30-34 |
| 7-24-25 | 14-48-50 |

⚡ Legs 5 and 12 → hypotenuse 13 instantly, no calculation.

[Easy] A right triangle has legs 9 and 12. Find the hypotenuse.

$c = \sqrt{81 + 144} = 15$ (a 9-12-15 triple, which is 3 times 3-4-5)

[Easy] A right triangle has hypotenuse 13 and one leg 5. Find the other leg.

$b = \sqrt{13^2 - 5^2} = \sqrt{169 - 25} = \sqrt{144} = 12$ (the 5-12-13 triple)

[Hard] A rectangle has diagonal $5\sqrt{17}$ and shorter side 5. Find the longer side.

$5^2 + b^2 = (5\sqrt{17})^2 = 25 \cdot 17 = 425 \implies b^2 = 400 \implies b = 20$

⚡ Official framework model question: a rectangle's diagonal splits it into two right triangles.

[Hard] A right triangle has legs $2x$ and $3x$, hypotenuse $4\sqrt{13}$. Find $x$.

$(2x)^2 + (3x)^2 = (4\sqrt{13})^2 \implies 4x^2 + 9x^2 = 208 \implies 13x^2 = 208 \implies x^2 = 16 \implies x = 4$.
Legs: 8 and 12; hypotenuse $4\sqrt{13} \approx 14.4$. Check: $8^2 + 12^2 = 64 + 144 = 208 = (4\sqrt{13})^2$. ✓

[Very Hard] A box has dimensions 3, 4, and 12. Find the length of the space diagonal (corner to opposite corner).

Face diagonal of the 3-by-4 face: $\sqrt{3^2 + 4^2} = 5$
Space diagonal: $\sqrt{5^2 + 12^2} = 13$

✅ Formula: space diagonal of a box $= \sqrt{l^2 + w^2 + h^2}$. Two Pythagorean steps are safer than one big square root.

### B4.4.2 Special Right Triangles

**Definition:** Two right triangles have side ratios so important they are printed on the reference sheet, because they appear constantly on the SAT - often in questions that are meant to be solved WITHOUT a calculator.

**45-45-90** `(* ON REFERENCE SHEET)`: $s : s : s\sqrt{2}$ - "same-leg-root-two"

The 45-45-90 triangle is half of a square (cut along a diagonal). The legs are equal; the hypotenuse is a leg times $\sqrt{2}$.

**30-60-90** `(* ON REFERENCE SHEET)`: $s : s\sqrt{3} : 2s$ where $s$ is opposite $30^\circ$ - "short-$\sqrt{3}$-double"

The 30-60-90 triangle is half of an equilateral triangle (cut along an altitude). The short leg (opposite $30^\circ$) is half the hypotenuse; the long leg (opposite $60^\circ$) is the short leg times $\sqrt{3}$.

**Method:**
1. Identify which special triangle you have (45-45-90, or 30-60-90) from the angles.
2. Find the "seed" length: in 45-45-90 the leg $s$; in 30-60-90 the short leg $s$ (opposite $30^\circ$).
3. Multiply or divide to reach the requested side.
   - Hypotenuse given in 45-45-90: **divide** by $\sqrt{2}$ (then rationalize).
   - Hypotenuse given in 30-60-90: divide by 2 to get the short leg.
   - Long leg given in 30-60-90: divide by $\sqrt{3}$ to get the short leg.

❌ **Trap:** Confusing which side gets $\sqrt{3}$ - longer leg (opp $60^\circ$), not hypotenuse.
❌ **Trap:** Given hypotenuse of 45-45-90, students multiply by $\sqrt{2}$ - must **divide** by $\sqrt{2}$.
❌ **Trap:** Forgetting to rationalize: $\frac{12}{\sqrt{2}} = 6\sqrt{2}$.

[Easy] A 45-45-90 triangle has a leg of 7. Find the hypotenuse.

$7\sqrt{2}$

[Medium] A 45-45-90 triangle has hypotenuse $10\sqrt{2}$. Find each leg.

$s\sqrt{2} = 10\sqrt{2} \implies s = 10$

[Medium] A 30-60-90 triangle has hypotenuse 18. Find the longer leg.

Short leg: $18/2 = 9$
Longer leg: $9\sqrt{3}$

[Medium] A 30-60-90 triangle has short leg 5. Find the hypotenuse and long leg.

Hypotenuse: $10$; long leg: $5\sqrt{3}$.

[Hard] A 30-60-90 triangle has long leg $12$. Find the short leg and the hypotenuse.

Short leg: $\frac{12}{\sqrt{3}} = 4\sqrt{3}$ (rationalized). Hypotenuse: $2 \cdot 4\sqrt{3} = 8\sqrt{3}$.

❌ **Trap:** Dividing by $\sqrt{3}$ and leaving $\frac{12}{\sqrt{3}}$ unrationalized. The SAT's grid-in accepts $4\sqrt{3} \approx 6.928$; graders want the clean form.

[Hard] An equilateral triangle of side 12 is cut by an altitude. Find area.

Height = $6\sqrt{3}$, Area = $\frac{1}{2} \cdot 12 \cdot 6\sqrt{3} = 36\sqrt{3}$

⚡ Altitude of an equilateral triangle splits it into two 30-60-90 triangles: height $= \frac{s\sqrt{3}}{2}$, area $= \frac{s^2\sqrt{3}}{4}$.

[Hard] A square has diagonal 8. Find its area.

The diagonal splits the square into two 45-45-90 triangles: $s\sqrt{2} = 8 \implies s = \frac{8}{\sqrt{2}} = 4\sqrt{2}$.
Area $= s^2 = 32$.

⚡ Shortcut: square area from diagonal $d$ is $\frac{d^2}{2}$. Here $\frac{64}{2} = 32$. Same answer, one line.

[Very Hard] Right triangle with legs $x$ and $x+7$, hypotenuse $x+8$. Find $x$.

$x^2 + (x+7)^2 = (x+8)^2$
$x^2 + x^2 + 14x + 49 = x^2 + 16x + 64$
$x^2 - 2x - 15 = 0$
$(x - 5)(x + 3) = 0 \implies x = 5$

Sides: 5, 12, 13.

[Very Hard] An isosceles right triangle has area 18. Find its hypotenuse.

Let legs be $s$. $\frac{1}{2}s^2 = 18 \implies s^2 = 36 \implies s = 6$.
Hypotenuse $= 6\sqrt{2}$.

### B4.4.3 SOHCAHTOA

**Definition:** For an acute angle $\theta$ in a right triangle, the three basic trig ratios compare pairs of sides. "Opposite" and "adjacent" are always relative to the angle you are working with.

$$\sin\theta = \frac{\text{opp}}{\text{hyp}} \qquad \cos\theta = \frac{\text{adj}}{\text{hyp}} \qquad \tan\theta = \frac{\text{opp}}{\text{adj}}$$

`[MEMORIZE]` - These ratios are not provided on the reference sheet, so they should be memorized until recall is automatic.

**Method:**
1. Label the triangle: mark the angle you are using; write O (opposite), A (adjacent, the non-hypotenuse side touching the angle), H (hypotenuse) on the sides.
2. Identify which two sides you know or need.
3. Pick the ratio containing both: $\sin$ (O/H), $\cos$ (A/H), $\tan$ (O/A).
4. Write the equation and solve for the unknown.

❌ **Trap:** Using the wrong sides - "opposite" and "adjacent" swap when you switch angles. Labeling first prevents this.
❌ **Trap:** SOHCAHTOA applies only to right triangles.

[Easy] In a right triangle with hypotenuse 10 and one leg 6, find $\sin\theta$ and $\cos\theta$ where $\theta$ is opposite the leg of length 6.

The other leg is $\sqrt{100 - 36} = 8$.
$\sin\theta = \frac{6}{10} = \frac{3}{5}$, $\cos\theta = \frac{8}{10} = \frac{4}{5}$, $\tan\theta = \frac{6}{8} = \frac{3}{4}$.

⚡ This is the 3-4-5 triple scaled by 2: recognize it and write the three ratios in seconds.

[Medium] A right triangle has hypotenuse 13 and one leg 5. Find $\cos\theta$ where $\theta$ is adjacent to the leg of length 5.

$\cos\theta = \frac{5}{13}$ (no need for Pythagoras - the 5-12-13 triple gives the other leg, but $\cos$ only needs adjacent and hypotenuse).

[Hard] In $\triangle ABC$, $\angle C = 90^\circ$, $\angle A = 35^\circ$, $AB = 20$ (hypotenuse). Find $BC$ (opp $A$).

$\sin 35^\circ = \frac{BC}{20} \implies BC = 20\sin 35^\circ \approx 11.47$

❌ **Trap:** Using $\cos$ when $\sin$ is correct - label the triangle first.

[Hard] In a right triangle, $\tan\theta = \frac{3}{4}$. Find $\sin\theta$ and $\cos\theta$.

Opp = 3, adj = 4, hyp = 5 (3-4-5 triple).
$\sin\theta = \frac{3}{5}$, $\cos\theta = \frac{4}{5}$.

⚡ Given any trig ratio, draw the triangle with those two sides, find the third by Pythagoras, then read off the other ratios. No formulas beyond the triple needed.

### B4.4.4 Inverse Trigonometry

**Definition:** The inverse functions $\sin^{-1}$, $\cos^{-1}$, $\tan^{-1}$ answer the question "which angle has this ratio?" They find an angle when two sides of a right triangle are known.

**Method:**
1. Identify which ratio you know: opp/hyp, adj/hyp, or opp/adj
2. Set up the equation, e.g. $\sin\theta = \frac{5}{13}$
3. Apply the inverse: $\theta = \sin^{-1}\left(\frac{5}{13}\right)$
4. In Desmos, type the inverse directly and confirm degree mode

**Exact-value check:** if the ratio matches a special triangle (e.g. $\sin\theta = \frac{1}{2}$), the angle is an exact special value ($30^\circ$), and no calculator is needed.

[Easy] If $\sin\theta = \frac{1}{2}$ and $\theta$ is acute, find $\theta$.

$\theta = \sin^{-1}\left(\frac{1}{2}\right) = 30^\circ$ (special value).

[Medium] A right triangle has legs 6 and 8. Find the angle opposite the leg of length 6.

$\tan\theta = \frac{6}{8} = 0.75 \implies \theta = \tan^{-1}(0.75) \approx 36.9^\circ$

[Hard] A 25 ft ladder leans against a wall, reaching 7 ft up the wall. Find the angle between the ladder and the ground.

$\sin\theta = \frac{7}{25} \implies \theta = \sin^{-1}\left(\frac{7}{25}\right) \approx 16.3^\circ$

✅ Desmos tip: Type `sin^{-1}(7/25)`; Desmos returns degrees when the degree symbol context is used - otherwise check your settings.

❌ **Trap:** $\sin^{-1}$ means inverse sine (an angle), NOT $\frac{1}{\sin}$. They are completely different.

[Hard] If $\cos\theta = \frac{5}{13}$ and $\theta$ is acute, find $\sin\theta$ (not the angle).

Draw the triangle: adj = 5, hyp = 13, so opp = 12 (5-12-13). $\sin\theta = \frac{12}{13}$.

⚡ Often the question wants another ratio, not the angle. The triangle-drawing method in B4.4.3 handles both.

### B4.4.5 Cofunction Identity

**Definition:** Sine and cosine are "cofunctions": the sine of an angle equals the cosine of its complement.

$$\sin\theta = \cos(90^\circ - \theta) \qquad \cos\theta = \sin(90^\circ - \theta)$$ `[MEMORIZE]`

**Why it works:** in a right triangle the two acute angles are complementary ($A + B = 90^\circ$), and the side that is opposite $A$ is adjacent to $B$. So $\sin A = \cos B$ automatically.

**Method:** if you see $\sin$ of one acute angle and $\cos$ of the other acute angle in the same right triangle, they are equal. If you see $\sin(x^\circ) = \cos(y^\circ)$ with both acute, set $x + y = 90$.

❌ **Trap:** In a right triangle the acute angles are complementary, so $\sin A = \cos B$ automatically.

[Easy] In a right triangle, $\angle A = 25^\circ$. Find $\cos(\angle B)$ where $B$ is the other acute angle.

$B = 90 - 25 = 65^\circ$, so $\cos B = \sin 25^\circ$. If the question gives $\sin 25^\circ \approx 0.42$, then $\cos B \approx 0.42$.

[Medium] In right $\triangle ABC$ ($\angle C = 90^\circ$), $\sin A = \frac{3}{5}$. Find $\cos B$.

$A + B = 90^\circ \implies \cos B = \sin A = \frac{3}{5}$

[Hard] If $\sin(x^\circ) = \cos(2x^\circ)$ for acute $x$, find $x$.

$\sin(x^\circ) = \cos(90 - x)^\circ$
$\cos(90 - x)^\circ = \cos(2x)^\circ$
$90 - x = 2x \implies x = 30$

> The acute-angle condition prevents other periodic solutions. Without it, $x = 30 + 120n$ would need evaluation.

### B4.4.6 Pythagorean Identity `[SUPPLEMENTARY]`

$$\sin^2\theta + \cos^2\theta = 1$$

**Definition:** the fundamental identity connecting sine and cosine for ANY angle - it is the unit circle equation $x^2 + y^2 = 1$ written in trig form ($x = \cos\theta$, $y = \sin\theta$).

**Method:** given one of $\sin\theta$ or $\cos\theta$, solve for the other: $\sin^2\theta = 1 - \cos^2\theta$. Use the quadrant (or "acute") condition to decide the sign.

[Medium] If $\sin\theta = \frac{3}{5}$ ($\theta$ acute), find $\cos\theta$.

$\frac{9}{25} + \cos^2\theta = 1 \implies \cos^2\theta = \frac{16}{25} \implies \cos\theta = \frac{4}{5}$ (acute → positive)

> Without an acute restriction, $\cos\theta$ could be $\pm\frac{4}{5}$ depending on the quadrant.

[Hard] If $\sin\theta = \frac{3}{5}$ and $\theta$ is in Quadrant II, find $\tan\theta$.

$\cos\theta = -\frac{4}{5}$ (negative in QII), so $\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{3/5}{-4/5} = -\frac{3}{4}$

❌ **Trap:** In Quadrant II, sine is positive but cosine is negative, so tangent is negative.

[Hard] If $\cos\theta = \frac{12}{13}$ and $\theta$ is acute, find $\sin\theta$.

$\sin\theta = \sqrt{1 - \frac{144}{169}} = \sqrt{\frac{25}{169}} = \frac{5}{13}$. (Or just recognize the 5-12-13 triangle.)

### B4.4.7 Tangent Identity `[SUPPLEMENTARY]`

$$\tan\theta = \frac{\sin\theta}{\cos\theta}$$

**Definition:** tangent is the ratio of sine to cosine. This matches the unit circle slope interpretation: $\tan\theta$ is the slope of the radius at angle $\theta$, since slope $= \frac{y}{x} = \frac{\sin\theta}{\cos\theta}$.

[Medium] Right triangle sides 5, 12, 13. Find $\tan\theta$ where $\theta$ is opposite side 5.

$\tan\theta = \frac{5}{12}$

[Medium] If $\tan\theta = \frac{3}{4}$ ($\theta$ acute), find $\sin\theta + \cos\theta$.

Opp = 3, adj = 4, hyp = 5
$\sin\theta = \frac{3}{5}$, $\cos\theta = \frac{4}{5}$
Sum = $\frac{7}{5}$

[Hard] If $\sin\theta = \frac{3}{5}$ and $\theta$ is acute, use the tangent identity to find $\tan\theta$.

First $\cos\theta = \frac{4}{5}$ (B4.4.6 method), then $\tan\theta = \frac{3/5}{4/5} = \frac{3}{4}$.

### B4.4.8 Angle of Elevation / Depression

**Definitions:**
- **Angle of elevation:** the angle between the horizontal and the line of sight, measured UP from the horizontal to the object above.
- **Angle of depression:** the angle between the horizontal and the line of sight, measured DOWN from the horizontal to the object below.

**Key facts:**
- Elevation: horizontal **up** to line of sight
- Depression: horizontal **down** to line of sight
- They are **alternate interior angles** (horizontal $\parallel$ horizontal), so the angle of depression from the top equals the angle of elevation from the bottom.

**Method:**
1. Draw the right triangle: horizontal = adjacent, vertical = opposite, the line of sight = hypotenuse. The angle sits at the observer.
2. Identify which sides are known/needed.
3. Pick the ratio: $\tan$ when you have (or need) the two legs; $\sin$ or $\cos$ when the hypotenuse is involved.
4. Solve; use inverse trig if the question asks for the angle.

❌ **Trap:** The angle of depression is measured from the horizontal down to the line of sight, not from the vertical. Draw the horizontal through the observer's eye first.

[Easy] From a point 50 m from the base of a building, the angle of elevation to the top is $45^\circ$. Find the height of the building.

$\tan 45^\circ = \frac{h}{50} \implies h = 50 \cdot 1 = 50$ m. (The 45-45-90 pattern: horizontal and vertical are equal.)

[Medium] From a point 60 m from the base of a building, the angle of elevation to the top is $40^\circ$. Find the height of the building.

$\tan 40^\circ = \frac{h}{60} \implies h = 60\tan 40^\circ \approx 50.3$ m

[Hard] From the top of a 100 ft lighthouse, the angle of depression to a boat is $30^\circ$. How far is the boat from the base of the lighthouse?

Angle of depression = angle of elevation from the boat ($30^\circ$) by alternate interior angles.
$\tan 30^\circ = \frac{100}{d} \implies d = \frac{100}{\tan 30^\circ} = 100\sqrt{3} \approx 173.2$ ft

✅ Desmos tip: Type `tan(30 deg)` or `tan(30°)` with the degree symbol - Desmos defaults to radians.

[Hard] A kite is flying at a height of 40 m. The angle of elevation from the observer is $30^\circ$. Find the length of the string (the hypotenuse).

$\sin 30^\circ = \frac{40}{L} \implies L = \frac{40}{\sin 30^\circ} = \frac{40}{1/2} = 80$ m

⚡ The kite/string problem is the hypotenuse version: when the question asks for the length of the line of sight, use $\sin$ (opposite is the height, hypotenuse is the string).

[Very Hard] From point A on the ground, the angle of elevation to the top of a cliff is $30^\circ$. Walking 100 m closer to point B, the angle of elevation is $60^\circ$. Find the height of the cliff.

Let height $= h$, distance from B to the base $= x$.
From B: $\tan 60^\circ = \frac{h}{x} \implies h = x\sqrt{3}$.
From A: $\tan 30^\circ = \frac{h}{x + 100} \implies h = \frac{x + 100}{\sqrt{3}}$.
Set equal: $x\sqrt{3} = \frac{x + 100}{\sqrt{3}} \implies 3x = x + 100 \implies x = 50$.
$h = 50\sqrt{3} \approx 86.6$ m.

❌ **Trap:** The two observers see the SAME height $h$ but DIFFERENT horizontal distances. Write two equations in $h$ and the unknown distance, then eliminate. This two-observer setup is a frequent hard question.

### B4.4.9 Unit Circle Trigonometry

**Definition:** The unit circle is the circle $x^2 + y^2 = 1$ centered at the origin. For any angle $\theta$ in standard position (vertex at the origin, initial side on the positive $x$-axis):

- $x$-coordinate of the intersection point = $\cos\theta$
- $y$-coordinate = $\sin\theta$
- $\tan\theta = \frac{y}{x} = \frac{\sin\theta}{\cos\theta}$ (the slope of the radius)

**Why the SAT tests it:** the framework explicitly lists "right triangle and unit circle trigonometry" and "radian measure." A point on the unit circle gives $\sin$ and $\cos$ directly, and the special-triangle ratios (B4.4.2) provide the exact values.

**Method (find trig values from an angle):**
1. Locate the angle's quadrant; this fixes the signs.
2. Find the reference angle (the acute angle the terminal side makes with the $x$-axis).
3. Read the exact value from the table below.
4. Attach the sign from the quadrant.

**Method (find an angle from a trig value):**
1. Identify the special value in the table (e.g. $\sin = \frac{\sqrt{3}}{2}$ → reference angle $60^\circ$).
2. Use the quadrant condition to pick the correct angle.

### Exact Values to Memorize

| Degrees | Radians | $\cos\theta$ | $\sin\theta$ | $\tan\theta$ |
|--------:|--------:|-------------:|-------------:|-------------:|
| $0^\circ$ | $0$ | $1$ | $0$ | $0$ |
| $30^\circ$ | $\pi/6$ | $\sqrt{3}/2$ | $1/2$ | $\frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}$ |
| $45^\circ$ | $\pi/4$ | $\sqrt{2}/2$ | $\sqrt{2}/2$ | $1$ |
| $60^\circ$ | $\pi/3$ | $1/2$ | $\sqrt{3}/2$ | $\sqrt{3}$ |
| $90^\circ$ | $\pi/2$ | $0$ | $1$ | undefined |

**Memory trick:** the sine column reads $\frac{\sqrt{0}}{2}, \frac{\sqrt{1}}{2}, \frac{\sqrt{2}}{2}, \frac{\sqrt{3}}{2}, \frac{\sqrt{4}}{2}$; cosine runs the same list backward.

### Signs by Quadrant

| Quadrant | $\cos$ | $\sin$ |
|----------|-------|-------|
| I | $+$ | $+$ |
| II | $-$ | $+$ |
| III | $-$ | $-$ |
| IV | $+$ | $-$ |

(All Students Take Calculus: in QI all positive, QII sine only, QIII tangent only, QIV cosine only.)

[Medium] If $\sin\theta = \frac{1}{2}$ and $\theta$ is in Quadrant II, find $\cos\theta$.

$\sin\theta = \frac{1}{2}$ → reference angle $30^\circ$. In QII, $\cos$ is negative → $\cos\theta = -\frac{\sqrt{3}}{2}$.

[Hard] If $\cos\theta = -\frac{\sqrt{2}}{2}$ and $\theta$ is in Quadrant III, find $\theta$ in degrees.

$\cos\theta = \frac{\sqrt{2}}{2}$ at $45^\circ$ reference angle. QIII $\theta = 180^\circ + 45^\circ = 225^\circ$.

[Medium] Find $\sin\left(\frac{\pi}{3}\right)$.

$\frac{\pi}{3} = 60^\circ$, so $\sin\left(\frac{\pi}{3}\right) = \frac{\sqrt{3}}{2}$

[Medium] Find $\tan 45^\circ$.

$\tan 45^\circ = \frac{\sin 45^\circ}{\cos 45^\circ} = \frac{\sqrt{2}/2}{\sqrt{2}/2} = 1$

[Hard] If $\cos\theta = \frac{1}{2}$ and $\theta$ is in Quadrant IV, find $\theta$ in radians.

Reference angle $60^\circ = \frac{\pi}{3}$; QIV: $\theta = 2\pi - \frac{\pi}{3} = \frac{5\pi}{3}$

❌ **Trap:** In QIV, cosine is positive and sine is negative. The angle $\frac{5\pi}{3}$ has $\cos = \frac{1}{2}$; the QI angle $\frac{\pi}{3}$ has the same cosine but is not in QIV.

[Hard] In the $xy$-plane, the point $P$ on the unit circle has $y$-coordinate $\frac{12}{13}$ and lies in Quadrant II. Find $\cos\theta$ and $\tan\theta$.

$\sin\theta = \frac{12}{13}$. $\cos^2\theta = 1 - \frac{144}{169} = \frac{25}{169}$, so $\cos\theta = -\frac{5}{13}$ (negative in QII).
$\tan\theta = \frac{12/13}{-5/13} = -\frac{12}{5}$.

⚡ The 5-12-13 triple hides in the unit circle: a point with $\frac{12}{13}$ and $\frac{5}{13}$ is on the circle because $5^2 + 12^2 = 13^2$.

[Very Hard] Point $P$ on the unit circle has coordinates $\left(-\frac{12}{13}, \frac{5}{13}\right)$. Find $\sin\theta$, $\cos\theta$, and $\tan\theta$ for the angle $\theta$ in standard position.

$\cos\theta = -\frac{12}{13}$, $\sin\theta = \frac{5}{13}$, $\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{5/13}{-12/13} = -\frac{5}{12}$

⚡ Any point $(x, y)$ on the unit circle gives $(\cos\theta, \sin\theta)$ directly - no memorized table needed.

[Very Hard] In the $xy$-plane, the terminal side of an angle $\theta$ in standard position passes through the point $(-3, 4)$, which lies on a circle of radius 5 centered at the origin. Find $\sin\theta$ and $\cos\theta$.

For a circle of radius $r$ (not the unit circle): $\sin\theta = \frac{y}{r}$, $\cos\theta = \frac{x}{r}$.
$\sin\theta = \frac{4}{5}$, $\cos\theta = -\frac{3}{5}$, $\tan\theta = -\frac{4}{3}$.

❌ **Trap:** When the point is NOT on the unit circle, divide by the radius $r = \sqrt{x^2 + y^2}$, not by 1. Here $r = 5$.

[Very Hard] A circle is centered at the origin with radius 2. Point $Q$ on the circle makes a $30^\circ$ angle with the positive $x$-axis. Find the coordinates of $Q$.

$x = r\cos\theta = 2\cos 30^\circ = 2 \cdot \frac{\sqrt{3}}{2} = \sqrt{3}$
$y = r\sin\theta = 2\sin 30^\circ = 2 \cdot \frac{1}{2} = 1$
$Q = (\sqrt{3}, 1)$

⚡ This generalizes the unit circle: for radius $r$, the coordinates are $(r\cos\theta, r\sin\theta)$. The Khan Academy "central angle in radians" pattern uses exactly this with special triangles.

---

## B4.5 Circles

### B4.5.1 Basic Properties

**Definition:** A circle is the set of all points at distance $r$ (radius) from a center point. The diameter $d = 2r$ is the longest chord, through the center.

$C = 2\pi r$, $A = \pi r^2$ `(* ON REFERENCE SHEET)`

**Method:** always convert diameter to radius first, then substitute. If the answer choices contain $\pi$, keep $\pi$ symbolic; only compute a decimal if choices are decimals.

[Easy] A circle has diameter 14. Find its circumference and area.

$r = 7$; $C = 2\pi(7) = 14\pi$; $A = \pi(7)^2 = 49\pi$

❌ **Trap:** "Diameter 14" - halve it first.

[Medium] A circle has circumference $30\pi$. Find its area.

$2\pi r = 30\pi \implies r = 15$; $A = \pi(15)^2 = 225\pi$.

⚡ Working backwards from circumference to area: find $r$ first, then square it.

### B4.5.2 Arcs and Sectors

**Definitions:**
- **Arc:** a portion of the circumference. **Arc length** is a distance (linear units). **Arc measure** is the central angle in degrees (or radians). Do not confuse them.
- **Sector:** a "pizza slice" region bounded by two radii and an arc. Its area is a fraction of the circle's area.

Arc length: $s = \frac{\theta}{360^\circ} \cdot 2\pi r$
Sector area: $A_{\text{sector}} = \frac{\theta}{360^\circ} \cdot \pi r^2$
`(Both MUST MEMORIZE)`

**The one proportion that unifies everything:**

$$\frac{\text{arc length}}{\text{circumference}} = \frac{\text{sector area}}{\text{circle area}} = \frac{\text{central angle}}{360^\circ}$$

**Method:**
1. Find the fraction of the circle: $\frac{\theta}{360^\circ}$.
2. Multiply the full circumference (for arc length) or full area (for sector area) by that fraction.
3. If a problem gives arc length and asks for circumference (or vice versa), set up the proportion directly.

❌ **Trap:** Arc length formula uses degrees. If using $s = r\theta$, $\theta$ **must** be in radians - never substitute a degree value directly. Wrong: $s = r \cdot 60^\circ$. Correct: $s = r \cdot \frac{\pi}{3}$.
❌ **Trap:** Confusing arc length (fraction of circumference) with sector area (fraction of area).

[Easy] A circle has radius 6 and a central angle of $60^\circ$. Find the arc length.

$s = \frac{60}{360} \cdot 2\pi(6) = \frac{1}{6} \cdot 12\pi = 2\pi$

[Easy] A circle has radius 10 and a central angle of $72^\circ$. Find the sector area.

$A = \frac{72}{360} \cdot \pi(10)^2 = \frac{1}{5} \cdot 100\pi = 20\pi$

[Medium] A circle of radius 6 has a sector with central angle $60^\circ$. Find the sector's perimeter.

Perimeter = two radii + arc length: $2(6) + \frac{60}{360}(2\pi \cdot 6) = 12 + 2\pi$

❌ **Trap:** A sector's perimeter includes the two straight radii - it is not just the arc.

[Medium] A circle has radius 6 and arc length $4\pi$. Find the central angle in degrees.

$4\pi = \frac{\theta}{360} \cdot 12\pi \implies \frac{\theta}{360} = \frac{1}{3} \implies \theta = 120^\circ$

[Hard] A circle of radius 8 has sector area $32\pi$. Find the arc length of that sector.

$32\pi = \frac{\theta}{360} \cdot 64\pi \implies \theta = 180^\circ$
$s = \frac{180}{360} \cdot 16\pi = 8\pi$

[Very Hard] The measure of arc $AB$ is $45^\circ$ and its length is 3 inches. Find the circumference of the circle.

$\frac{45}{360} = \frac{1}{8}$, so the arc is $\frac{1}{8}$ of the circumference: $C = 8 \cdot 3 = 24$ inches

⚡ Official framework model question: use the proportion $\frac{\text{arc length}}{\text{circumference}} = \frac{\text{arc measure}}{360^\circ}$.

[Very Hard] A sector has area $6\pi$ and central angle $60^\circ$. Find the radius.

$\frac{60}{360}\pi r^2 = 6\pi \implies \frac{1}{6}r^2 = 6 \implies r^2 = 36 \implies r = 6$

### B4.5.3 Radians

**Definition:** A radian is the angle that cuts off an arc equal to the radius. One full circle is $2\pi$ radians, so:

$2\pi$ rad = $360^\circ$ `(* ON REFERENCE SHEET)`

$$\text{radians} = \frac{\pi}{180} \times \text{degrees}$$

Arc length in radians: $s = r\theta$
Sector area in radians: $A = \frac{1}{2}r^2\theta$

**Method:**
1. Convert to radians (multiply degrees by $\frac{\pi}{180}$) or to degrees (multiply radians by $\frac{180}{\pi}$).
2. Use $s = r\theta$ or $A = \frac{1}{2}r^2\theta$ ONLY with radians.

**Radians to memorize:** $30^\circ = \frac{\pi}{6}$, $45^\circ = \frac{\pi}{4}$, $60^\circ = \frac{\pi}{3}$, $90^\circ = \frac{\pi}{2}$, $180^\circ = \pi$, $270^\circ = \frac{3\pi}{2}$.

[Easy] Convert $150^\circ$ to radians.

$150 \times \frac{\pi}{180} = \frac{5\pi}{6}$

[Easy] Convert $\frac{5\pi}{6}$ radians to degrees.

$\frac{5\pi}{6} \cdot \frac{180}{\pi} = 150^\circ$

[Medium] A circle of radius 5 has a central angle of $\frac{2\pi}{3}$ radians. Find the arc length.

$s = r\theta = 5 \cdot \frac{2\pi}{3} = \frac{10\pi}{3}$

❌ **Trap:** $s = r\theta$ requires radians. If the angle is given in degrees, convert first (or use the $\frac{\theta}{360} \cdot 2\pi r$ form).

[Medium] A circle of radius 4 has a sector with angle $\frac{\pi}{6}$ radians. Find the sector area.

$A = \frac{1}{2}r^2\theta = \frac{1}{2}(16)\left(\frac{\pi}{6}\right) = \frac{4\pi}{3}$

[Hard] A central angle of $\frac{3\pi}{4}$ radians subtends an arc of length $9\pi$. Find the radius.

$s = r\theta \implies 9\pi = r \cdot \frac{3\pi}{4} \implies r = 12$

[Hard] In the $xy$-plane, a circle centered at the origin has radius 6. Point $P$ on the circle lies at an angle of $30^\circ$ from the positive $x$-axis. What is the radian measure of the central angle $\angle POX$ (where $X$ is on the positive $x$-axis)?

$30^\circ \times \frac{\pi}{180} = \frac{\pi}{6}$ radians.

⚡ The framework's "central angle in radian measure" question: convert the special angle, or recognize $\frac{\pi}{6}$ directly from the special-triangle table.

### B4.5.4 Central vs. Inscribed Angles

**Definitions:**
- **Central angle:** vertex at the center of the circle. Its measure equals the intercepted arc.
- **Inscribed angle:** vertex on the circle, sides are chords. Its measure equals **half** the intercepted arc.
- **Thales' theorem:** an inscribed angle subtending a diameter is $90^\circ$.

**Method:** inscribed angle = $\frac{1}{2}$ × intercepted arc (or $\frac{1}{2}$ × central angle subtending the same arc). Work backwards (multiply by 2) when the arc is unknown.

❌ **Trap:** Forgetting the $\frac{1}{2}$ factor for inscribed angles.

[Medium] Central angle $80^\circ$. Measure of inscribed angle subtending same arc?

$80/2 = 40^\circ$

[Hard] Inscribed angle $35^\circ$. Measure of intercepted arc?

$2 \times 35 = 70^\circ$

[Medium] An inscribed angle intercepts an arc of $100^\circ$. Find the angle.

$\frac{1}{2} \cdot 100 = 50^\circ$

[Hard] Points $A$, $B$, $C$ lie on a circle with $AC$ a diameter. By Thales' theorem, $\angle ABC = 90^\circ$. If $AB = 6$ and $BC = 8$, find the radius.

$AC$ is the hypotenuse: $AC = \sqrt{36 + 64} = 10$, so radius $= 5$

✅ Thales' theorem: any inscribed angle that intercepts a diameter is a right angle - the bridge between circle theorems and right-triangle tools.

[Very Hard] In a circle, inscribed angle $\angle ABC$ measures $40^\circ$ and intercepts arc $AC$. The central angle subtending the same arc $AC$ measures $x^\circ$. Find $x$.

The central angle equals the arc: $x = 2 \times 40 = 80^\circ$.

❌ **Trap:** The central angle subtending the SAME arc as an inscribed angle is always twice the inscribed angle. Do not halve the central angle; it is the arc that is halved.

### B4.5.5 Tangent Lines

**Definition:** A tangent line touches the circle at exactly one point. The tangent is **perpendicular** to the radius drawn to the point of tangency.

**Method:** draw the radius to the tangency point, mark the right angle, then use Pythagoras or right-triangle trig on the triangle formed by the center, the tangency point, and the external point.

✅ Draw the radius to the tangency point and mark the right angle immediately.

**Tangent-length property** `[SUPPLEMENTARY]`: From the same external point, tangent segments to a circle are equal in length ($PA = PB$).

[Medium] From an external point $P$, a tangent segment to a circle measures 7 cm, and the distance from $P$ to the center is 25 cm. Find the radius.

Radius $\perp$ tangent: right triangle with legs $r$ and 7, hypotenuse 25.
$r^2 + 7^2 = 25^2 \implies r^2 = 576 \implies r = 24$

⚡ Hidden 7-24-25 triple.

❌ **Trap:** The radius must be drawn to the point of tangency to form the right angle.

[Hard] From point $P$ outside a circle, two tangent segments $PA$ and $PB$ are drawn. $PA = 4x - 3$ and $PB = x + 9$. Find $x$.

Tangent segments from the same external point are equal:
$4x - 3 = x + 9 \implies 3x = 12 \implies x = 4$

### B4.5.6 Chords

**Definitions:** A chord is a segment joining two points on the circle. A diameter is the longest chord.

- A perpendicular from center to chord **bisects** the chord. `[OFFICIAL CORE]`
- Two chords equidistant from center are equal in length. `[SUPPLEMENTARY]`

**Method:** draw the radius to one endpoint of the chord and the perpendicular from the center to the chord's midpoint. This creates a right triangle: hypotenuse = radius, one leg = half the chord, other leg = distance from center to chord.

[Hard] A circle of radius 13 has a chord 24 units long. Find the distance from the center to the chord.

The perpendicular from the center bisects the chord: half-chord $= 12$.
Right triangle: $5^2 + 12^2 = 13^2$, so distance $= 5$.

⚡ Hidden 5-12-13 triple. Draw the radius to the chord's endpoint and the perpendicular to the chord's midpoint.

[Hard] A chord is 16 units long and the distance from the center to the chord is 6. Find the radius.

Half-chord $= 8$; right triangle legs 8 and 6: $r = \sqrt{64 + 36} = 10$.

### B4.5.7 Circle from Diameter Endpoints

**Definition:** the diameter's endpoints are the two farthest-apart points on the circle. The center is their midpoint; the radius is half their distance.

Given endpoints of a diameter:
1. Center = midpoint of endpoints (midpoint formula)
2. Diameter = distance between endpoints (distance formula)
3. Radius = half the diameter
4. Write circle equation $(x - h)^2 + (y - k)^2 = r^2$

[Easy] The endpoints of a diameter are $(1, 1)$ and $(7, 9)$. Find the center.

Center = midpoint: $\left(\frac{1+7}{2}, \frac{1+9}{2}\right) = (4, 5)$

[Medium] The endpoints of a diameter are $(2, 3)$ and $(8, -5)$. Find the circle equation.

Center: $\left(\frac{2+8}{2}, \frac{3+(-5)}{2}\right) = (5, -1)$
Diameter: $\sqrt{(8-2)^2 + (-5-3)^2} = \sqrt{36 + 64} = 10$
Radius: $5$
Equation: $(x - 5)^2 + (y + 1)^2 = 25$

[Hard] The endpoints of a diameter are $(-2, 1)$ and $(6, 7)$. Find the area of the circle.

Center: $\left(\frac{-2+6}{2}, \frac{1+7}{2}\right) = (2, 4)$
Radius: half of $\sqrt{(6-(-2))^2 + (7-1)^2} = \frac{1}{2}\sqrt{64 + 36} = \frac{10}{2} = 5$
Area: $25\pi$.

### B4.5.8 Equation of a Circle

**Definition:** The equation $(x - h)^2 + (y - k)^2 = r^2$ describes every point exactly $r$ units from the center $(h, k)$. It is just the distance formula squared: the distance from $(x,y)$ to $(h,k)$ equals $r$.

$$(x - h)^2 + (y - k)^2 = r^2$$ `(MUST MEMORIZE)`

Center $(h, k)$, radius $r$.

**Method (read an equation):**
1. Rewrite each parenthesis as $x - h$ and $y - k$ mentally: $(x + 3)$ becomes $(x - (-3))$, so $h = -3$.
2. The center is $(h, k)$ - the signs are FLIPPED from what is written.
3. Take the square root of the right side for the radius: RHS = 25 → $r = 5$.

**Method (write an equation from a graph):**
1. Read the center $(h, k)$ off the graph.
2. Count grid units from the center to any point on the circle for the radius.
3. Square the radius into the RHS.

**Method (check whether a point is on/inside/outside):**
1. Substitute the point into the left side.
2. Compare to $r^2$: equal → on the circle; less → inside; greater → outside.

❌ **Trap:** Center sign. $(x - 3)^2 + (y + 2)^2 = 25$ → center $(3, -2)$, not $(-3, 2)$.
✅ **Best method:** Ask what value of $x$ makes $(x - h) = 0$, and what value of $y$ makes $(y - k) = 0$.
❌ **Trap:** RHS = $r^2$. If RHS = 25, $r = 5$, not 25.

[Easy] A circle is graphed with center $(2, 3)$ and radius 4. Write its equation.

$(x - 2)^2 + (y - 3)^2 = 16$

⚡ This is the most common circle question on the digital SAT: read the center and radius off the graph, then write the equation. The radius is NOT squared on the graph - square it when writing the equation.

[Easy] A circle has equation $(x + 2)^2 + (y - 5)^2 = 36$. Find its center and radius.

$(x + 2) = (x - (-2))$ → $h = -2$; $k = 5$. Radius $= \sqrt{36} = 6$.
Center $(-2, 5)$, radius 6.

❌ **Trap:** Reading the center as $(2, -5)$ by taking the signs literally. The signs flip.

[Medium] Does the point $(6, 3)$ lie on, inside, or outside the circle $(x - 3)^2 + (y + 1)^2 = 25$?

Distance from center $(3, -1)$: $\sqrt{(6-3)^2 + (3+1)^2} = \sqrt{9 + 16} = 5 = r$. On the circle.

❌ **Trap:** Compare distance to the radius (or distance$^2$ to $r^2$) - just be consistent. Distance $< r$ inside, $= r$ on, $> r$ outside.

✅ Desmos tip: Graph the circle equation; Desmos draws it, and you can click a point to check if it lies on the circle.

[Medium] A circle centered at $(3, 2)$ passes through $(7, 5)$. Write the equation.

$r = \sqrt{(7-3)^2 + (5-2)^2} = 5$
$(x - 3)^2 + (y - 2)^2 = 25$

[Hard] The point $(k, -2)$ lies on the circle $(x - 4)^2 + (y + 2)^2 = 49$. Find the possible values of $k$.

Substitute: $(k - 4)^2 + (-2 + 2)^2 = 49 \implies (k - 4)^2 = 49$.
$k - 4 = 7$ or $k - 4 = -7$, so $k = 11$ or $k = -3$.

❌ **Trap:** Forgetting the negative square root. The horizontal line $y = -2$ through the center meets the circle twice, so there are two answers. Grid-ins can only accept one - read whether the question asks for "the value" or "a possible value."

[Hard] A circle has equation $(x - 1)^2 + (y + 3)^2 = 25$. It is translated 3 units right and 2 units down, and its radius is increased by 1. Write the new equation.

Original center $(1, -3)$, radius 5. New center: $(1 + 3, -3 - 2) = (4, -5)$. New radius: 6.
New equation: $(x - 4)^2 + (y + 5)^2 = 36$.

⚡ Translations move the center only; radius changes only when the problem says so. This "shift the circle" pattern is a real Bluebook-style medium question.

[Very Hard] A circle has equation $x^2 + y^2 = 10$. Does the point $(3, 1)$ lie inside, on, or outside the circle?

Left side at $(3,1)$: $3^2 + 1^2 = 10 = r^2$. On the circle.

⚡ An equation with no linear terms is centered at the origin: $x^2 + y^2 = r^2$. Read $r^2$ straight off.

### B4.5.9 Completing the Square

**Definition:** The expanded form $x^2 + y^2 + Dx + Ey + F = 0$ hides the center and radius. Completing the square converts it into $(x - h)^2 + (y - k)^2 = r^2$, which reveals them.

**Why it works:** $(x - h)^2 = x^2 - 2hx + h^2$: the linear coefficient $-2h$ encodes the center, and the constant $h^2$ is the "completion" that makes a perfect square. Adding $(\text{half the linear coefficient})^2$ to both sides rebuilds that perfect square.

Given $x^2 + y^2 + Dx + Ey + F = 0$:

**Method:**
1. Group $x$ and $y$ terms, move constant to RHS: $(x^2 + Dx) + (y^2 + Ey) = -F$
2. For the $x$-group, take half of $D$ and square it: $\left(\frac{D}{2}\right)^2$; add it to **both** sides.
3. For the $y$-group, take half of $E$ and square it: $\left(\frac{E}{2}\right)^2$; add it to **both** sides.
4. Factor each group: $(x^2 + Dx + (D/2)^2) = (x + D/2)^2$.
5. Read center $(h, k)$ (flip the signs) and radius $r = \sqrt{\text{RHS}}$.

❌ **Trap:** Adding $(b/2)^2$ to LHS only - must add to both sides.
❌ **Trap:** $(x + 3)^2$ means $h = -3$.
❌ **Trap:** If the RHS comes out negative or zero, the equation does not describe a circle. A valid circle needs RHS $> 0$.

[Medium] Find the center and radius of $x^2 + y^2 - 6x + 4y - 12 = 0$.

$(x^2 - 6x) + (y^2 + 4y) = 12$
Half of $-6$ is $-3$; square: $9$. Half of $4$ is $2$; square: $4$.
$(x^2 - 6x + 9) + (y^2 + 4y + 4) = 12 + 9 + 4$
$(x - 3)^2 + (y + 2)^2 = 25$
Center $(3, -2)$, radius $5$.

⚡ This exact equation style ($x^2 + y^2 - 6x + 4y - 12 = 0$) is a near-template for SAT circle questions. Practice until the four lines above are automatic.

[Hard] Find center and radius of $x^2 + y^2 + 6x - 8y - 11 = 0$.

$(x^2 + 6x + 9) + (y^2 - 8y + 16) = 11 + 9 + 16$
$(x + 3)^2 + (y - 4)^2 = 36$
Center $(-3, 4)$, radius $6$

[Hard] $x^2 + y^2 - 10x + 4y + 20 = 0$ represents a circle. Find area.

$(x^2 - 10x + 25) + (y^2 + 4y + 4) = -20 + 25 + 4$
$(x - 5)^2 + (y + 2)^2 = 9$
$r = 3$, $A = 9\pi$

[Hard] $x^2 + y^2 + 8x - 6y = 0$ represents a circle. Find its area.

$(x^2 + 8x + 16) + (y^2 - 6y + 9) = 0 + 16 + 9$
$(x + 4)^2 + (y - 3)^2 = 25$
$r^2 = 25$, so area $= \pi r^2 = 25\pi$ - you never need to compute $r$.

⚡ Efficiency trick: when the question asks for AREA (not radius), stop at $r^2$. The area formula uses $r^2$ directly. Same idea: circumference questions want $\sqrt{r^2}$.

[Very Hard] Find the center and radius of $x^2 + y^2 - 6x + 10y + 18 = 0$.

$(x^2 - 6x + 9) + (y^2 + 10y + 25) = -18 + 9 + 25$
$(x - 3)^2 + (y + 5)^2 = 16$
Center $(3, -5)$, radius 4

❌ **Trap:** Even middle coefficients give perfect squares like 9; odd coefficients give fractions or a radical radius. Check that the RHS is positive - if it is negative or zero, the equation does not describe a circle.

[Very Hard] The equation $x^2 + y^2 + 14x - 2y + c = 0$ represents a circle with radius 5. Find $c$.

$(x^2 + 14x + 49) + (y^2 - 2y + 1) = -c + 49 + 1$
$(x + 7)^2 + (y - 1)^2 = 50 - c$
Radius 5 means RHS $= 25$: $50 - c = 25 \implies c = 25$.

[Very Hard] The equation $4x^2 + 4y^2 - 8x + 16y - 44 = 0$ represents a circle. Find its radius.

First divide everything by 4 (the $x^2$ and $y^2$ coefficients must be 1):
$x^2 + y^2 - 2x + 4y - 11 = 0$
$(x^2 - 2x + 1) + (y^2 + 4y + 4) = 11 + 1 + 4$
$(x - 1)^2 + (y + 2)^2 = 16$
Radius 4.

❌ **Trap:** Completing the square only works when the $x^2$ and $y^2$ coefficients are 1. If they are 4 (or anything else), divide through first. This is a frequent "hard module" trap.

✅ Desmos tip: Type the expanded form $x^2 + y^2 - 6x + 10y + 18 = 0$ - Desmos graphs the circle, and you can read the center and radius off the graph to check your completing-the-square work.

---

## Mixed Practice - B4

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

**6 [Medium]** A circle in the $xy$-plane has center $(4, -2)$ and radius 3. Which of the following is the equation of the circle?
- (A) $(x-4)^2 + (y+2)^2 = 3$ (B) $(x-4)^2 + (y+2)^2 = 9$ (C) $(x+4)^2 + (y-2)^2 = 3$ (D) $(x+4)^2 + (y-2)^2 = 9$
- Center $(4, -2)$ -> $(x - 4)$, $(y + 2)$; radius 3 -> RHS $= 9$ -> **(B)**.
- (A) **RHS not squared**. (C)/(D) **center signs flipped**.

**7 [Hard]** The radius of a sphere is doubled and its new volume is $V$. What was the original volume?
- (A) $V/2$ (B) $V/4$ (C) $V/8$ (D) $V/16$
- Doubling the radius multiplies volume by $2^3 = 8$, so original $= V/8$ -> **(C)**.
- (A) **applying linear scaling to volume**. (B) **$k^2$ (area scaling) used for volume**. (D) **squaring the cube**.

**8 [Hard]** In the $xy$-plane, point $P\left(-\frac{3}{5}, \frac{4}{5}\right)$ lies on the unit circle. What is $\sin\theta + \cos\theta$, where $\theta$ is the angle in standard position for $P$?
- $\sin\theta = \frac{4}{5}$, $\cos\theta = -\frac{3}{5}$: sum $= \frac{1}{5}$.
- ❌ **Trap:** Reading the coordinates in the wrong order - $\sin$ is the $y$-coordinate.

**9 [Medium]** A circle has equation $(x + 1)^2 + (y - 4)^2 = 10$. Does the point $(2, 5)$ lie on the circle?
- Substitute: $(2 + 1)^2 + (5 - 4)^2 = 9 + 1 = 10 = r^2$ → **yes, on the circle**.
- ❌ **Trap:** Adding the coordinates instead of substituting into the squared terms.

**10 [Hard]** The point $(k, -2)$ lies on the circle $(x - 4)^2 + (y + 2)^2 = 49$. What are the possible values of $k$?
- $(k - 4)^2 = 49 \implies k - 4 = \pm 7 \implies k = 11$ or $k = -3$.
- ❌ **Trap:** Only taking the positive square root and answering 11.

**11 [Medium]** A point $(2, -3)$ is rotated $90^\circ$ counterclockwise about the origin. What are the coordinates of the image?
- Rule: $(x, y) \to (-y, x)$: $(2, -3) \to (3, 2)$.
- (A) $(-2, 3)$ = **$180^\circ$ rotation**. (B) $(3, 2)$ = **correct**. (C) $(-3, -2)$ = **$90^\circ$ CW**. (D) $(2, 3)$ = **reflection over x-axis**.

**12 [Hard]** A 30-60-90 triangle has a long leg of $6\sqrt{3}$. What is the perimeter?
- Short leg $= \frac{6\sqrt{3}}{\sqrt{3}} = 6$; hypotenuse $= 12$. Perimeter $= 6 + 6\sqrt{3} + 12 = 18 + 6\sqrt{3}$.
- ❌ **Trap:** Treating the long leg as the short leg and writing hypotenuse $= 12\sqrt{3}$.

**13 [Medium]** A circle of radius 6 has a sector with central angle $90^\circ$. Find the sector area.
- $A = \frac{90}{360} \cdot \pi(6)^2 = \frac{1}{4} \cdot 36\pi = 9\pi$.
- (A) $6\pi$ = **using circumference-style fraction incorrectly**. (B) $9\pi$ = **correct**. (C) $18\pi$ = **half the circle**. (D) $36\pi$ = **the full circle**.

**14 [Hard]** Triangle $ABC$ has $DE \parallel BC$ with $D$ on $AB$, $E$ on $AC$. $AD = 2$, $DB = 6$, $DE = 5$. Find $BC$.
- $k = \frac{AD}{AB} = \frac{2}{8} = \frac{1}{4}$; $BC = 5 \cdot 4 = 20$.
- ❌ **Trap:** Using $AD = 2$ against $DB = 6$ (ratio $\frac{1}{3}$) instead of the whole side $AB = 8$.

**15 [Hard]** A building casts a shadow of 30 m. A 1.5 m pole casts a 2 m shadow at the same time. Find the building's height.
- $\frac{h}{30} = \frac{1.5}{2} \implies h = 30 \cdot 0.75 = 22.5$ m.
- ❌ **Trap:** Setting up the proportion upside down ($\frac{h}{1.5} = \frac{30}{2}$ gives $h = 22.5$ only by luck of symmetry - keep height over shadow on both sides to be safe).

**16 [Very Hard]** The equation $x^2 + y^2 + 8x - 6y = 0$ represents a circle. What is its area?
- $(x + 4)^2 + (y - 3)^2 = 25$; $r^2 = 25$; area $= 25\pi$.
- (A) $5\pi$ = **using $r = 5$ then multiplying by $\pi$ but forgetting the square... actually $25\pi$**. (B) $10\pi$ = **treating $\sqrt{25}$ as diameter**. (C) $25\pi$ = **correct**. (D) $100\pi$ = **squaring the diameter**.

---

## Desmos Strategies for Geometry

- **Circle equations:** Type `(x-h)^2+(y-k)^2=r^2` - Desmos displays the circle for visual verification.
- **Expanded circle equations:** Type the expanded form (e.g. `x^2 + y^2 - 6x + 4y - 12 = 0`) - Desmos graphs it anyway, letting you read off the center and radius to check completing-the-square work.
- **Distance:** Enter $\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$ directly for the exact distance.
- **Area/volume arithmetic:** Set up the full expression (e.g., `(1/3)*pi*5^2*12`) to avoid errors.
- **Inverse trig:** `sin^{-1}(0.6)` works directly - confirm the result is in the expected unit (degrees vs radians).
- **Trig in degrees:** Use `sin(35°)` with the degree symbol - Desmos defaults to **radians**.
- **Completing the square:** Do algebra on paper, use Desmos to verify the final circle.
- **Midpoint:** Type `((x1+x2)/2, (y1+y2)/2)` to check.
- **Transformations:** Compute $(x,y) \to (-y,x)$ via function composition.
- **Scaling:** Multiply by $k^2$ or $k^3$ and verify.
- **Special values:** `sin(30°)`, `cos(60°)`, `tan(45°)` return the exact fractions $0.5$, $0.5$, $1$ - use them to confirm exact-value work.
- **Point-on-circle checks:** Graph the circle, then click any point to read whether it lies on it.

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
| 16 | 45-45-90: multiply hypotenuse by $\sqrt{2}$ | Confusing given side with given hypotenuse | Hypotenuse given: **divide** by $\sqrt{2}$ |
| 17 | $s = r\theta$ with a degree angle | Forgetting the radian requirement | Convert to radians first |
| 18 | Dilation area factor $k$ | Treating dilation as rigid motion | Area scales by $k^2$ |
| 19 | Desmos in radian mode for degree trig | Default setting | Use the $^\circ$ symbol or convert |
| 20 | Rotation $90^\circ$ CW vs CCW | Using the wrong rule | CW: $(y,-x)$; CCW: $(-y,x)$ |
| 21 | Circle point: missing negative root | Only taking the positive square root | $(k - 4)^2 = 49 \to k = 11$ or $-3$ |
| 22 | Dividing by $\sqrt{3}$ without rationalizing | Leaving $\frac{12}{\sqrt{3}}$ | Write $4\sqrt{3}$ |
| 23 | Elevation vs depression diagram | Measuring from the vertical | Draw the horizontal through the eye first |
| 24 | $\sin^{-1}$ read as reciprocal | $\frac{1}{\sin}$ vs inverse sine | Inverse sine returns an angle |
| 25 | $\sin$/$x$-coordinate swap on unit circle | Reading the point backwards | $\cos$ = $x$, $\sin$ = $y$ |

---

## B4 at a Glance (Final Revision Reference)

### Formulas by Priority

| Priority | What |
|----------|------|
| `[REFERENCE SHEET]` | Rectangle/triangle/circle area, Pythagoras, special triangle ratios, prism/cylinder/sphere/cone/pyramid volume, triangle angle sum, degrees-radians |
| `[MEMORIZE]` | Perimeter ($P=2l+2w$), trapezoid/parallelogram area, distance/midpoint/slope, SOHCAHTOA, cofunction, arc length, sector area, circle equation, $\frac{\sqrt{3}}{4}s^2$, cylinder surface area, polygon interior sum, scale factor rules, radian arc/sector ($s = r\theta$, $A = \frac{1}{2}r^2\theta$) |
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
| Rotation about origin | Rule table in B4.3.9 (90 CCW: $(-y,x)$; 180: $(-x,-y)$; 270 CCW: $(y,-x)$) |
| Expanded circle form | Complete the square; divide through if $x^2, y^2$ coefficients $\neq 1$ |

### Traps Quick-Check
- ✅ Diameter halved? Scale factor $k$ not $k^2$? Circle signs flipped? RHS squared? $\frac{1}{2}$ for semicircle/inscribed? Same-side interior = supplementary? Desmos in degree mode? Rotation CW vs CCW rule? Both square roots on circle-point questions?
