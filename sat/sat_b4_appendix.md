# B4 Optional Appendix (enrichment - not core SAT)

[Hard] Polygon vertices $(0,0)$, $(4,0)$, $(6,3)$, $(2,5)$. Find area via shoelace.

| $x$ | $y$ | $x_i y_{i+1}$ | $y_i x_{i+1}$ |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 4 | 0 | 12 | 0 |
| 6 | 3 | 30 | 6 |
| 2 | 5 | 0 | 0 |
| 0 | 0 | 0 | 0 |

Sum down: $0 + 12 + 30 + 0 = 42$
Sum up: $0 + 0 + 6 + 0 = 6$
$A = \frac{1}{2}|42 - 6| = 18$

❌ **Trap:** Forgetting to repeat the first vertex at the end.

---

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

---

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

---

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

---

[Hard] A circle has equation $(x - 1)^2 + (y + 3)^2 = 25$. It is translated 3 units right and 2 units down, and its radius is increased by 1. Write the new equation.

Original center $(1, -3)$, radius 5. New center: $(1 + 3, -3 - 2) = (4, -5)$. New radius: 6.
New equation: $(x - 4)^2 + (y + 5)^2 = 36$.

⚡ Translations move the center only; radius changes only when the problem says so. This "shift the circle" pattern is a real Bluebook-style medium question.
