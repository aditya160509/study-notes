# 📘 Chapter 9: Vectors - 9709 Pure Mathematics 3 (CAIE A Level Maths)

## Cambridge International AS & A Level Mathematics (9709) - Paper 3

> **The complete walkthrough:** vector notation, magnitude and unit vectors, the scalar product, the vector equation of a line, deciding whether lines are parallel, intersecting or skew, angles between lines, areas of triangles, and the foot of the perpendicular from a point to a line. Every technique is built from fully solved examples, then tested with practice questions and full solutions.

---

# 📋 Table of Contents

1. [PART 1: Vector Notation, Magnitude and Unit Vectors](#part-1-vector-notation-magnitude-and-unit-vectors)
2. [PART 2: The Scalar Product](#part-2-the-scalar-product)
3. [PART 3: The Vector Equation of a Line](#part-3-the-vector-equation-of-a-line)
4. [PART 4: Parallel, Intersecting and Skew Lines](#part-4-parallel-intersecting-and-skew-lines)
5. [PART 5: Angles, Areas and the Foot of the Perpendicular](#part-5-angles-areas-and-the-foot-of-the-perpendicular)
6. [PART 6: Full Exam-Style Questions](#part-6-full-exam-style-questions)
7. [Formula Sheet](#formula-sheet)
8. [Quick Reference Card](#quick-reference-card)

---

# PART 1: Vector Notation, Magnitude and Unit Vectors

This part covers the language of vectors: how to write them, add them, subtract them, scale them, and measure them. Every later part depends on these operations being automatic.

## 1.1 Scalars and Vectors

A **scalar** has magnitude only: mass, speed, time, temperature.

A **vector** has both magnitude and direction: displacement, velocity, acceleration, force.

A vector is written in one of four equivalent ways:

$$\mathbf{a}, \qquad \underline{a}, \qquad \begin{pmatrix} x \\ y \\ z \end{pmatrix}, \qquad x\mathbf{i} + y\mathbf{j} + z\mathbf{k}$$

Here $\mathbf{i}$, $\mathbf{j}$, $\mathbf{k}$ are the unit vectors in the $x$-, $y$- and $z$-directions. The syllabus expects you to move freely between column form and $\mathbf{i}\mathbf{j}\mathbf{k}$ form; exam questions use both.

**Position vector.** If $O$ is the origin, the position vector of a point $A$ is written $\vec{OA}$ (or just $\mathbf{a}$). It tells you how to get from $O$ to $A$.

**Displacement vector.** The vector from $A$ to $B$ is

$$\vec{AB} = \vec{OB} - \vec{OA} = \mathbf{b} - \mathbf{a}$$

The order matters. $\vec{AB}$ is "head minus tail": final position minus starting position.

> ⭐ **Watch Out!** $\vec{AB} = \mathbf{b} - \mathbf{a}$, not $\mathbf{a} - \mathbf{b}$. Reversing the order gives $\vec{BA}$, which points the opposite way. This single sign error costs more marks in vector questions than anything else.

## 1.2 Magnitude and Unit Vectors

For $\mathbf{a} = x\mathbf{i} + y\mathbf{j} + z\mathbf{k}$,

$$|\mathbf{a}| = \sqrt{x^2 + y^2 + z^2}$$

The **unit vector** in the direction of $\mathbf{a}$ is

$$\hat{\mathbf{a}} = \frac{\mathbf{a}}{|\mathbf{a}|}$$

It has length $1$ and points the same way as $\mathbf{a}$. In 2D, replace the three components by two.

## 1.3 Addition, Subtraction and Scalar Multiplication

Vectors add and subtract component by component:

$$\mathbf{a} \pm \mathbf{b} = (a_1 \pm b_1)\mathbf{i} + (a_2 \pm b_2)\mathbf{j} + (a_3 \pm b_3)\mathbf{k}$$

Multiplying by a scalar $k$ scales every component:

$$k\mathbf{a} = ka_1\mathbf{i} + ka_2\mathbf{j} + ka_3\mathbf{k}$$

Geometrically:

- $\mathbf{a} + \mathbf{b}$ is the diagonal of the parallelogram with sides $\mathbf{a}$ and $\mathbf{b}$ (the **parallelogram law**), or the third side of the triangle formed by placing $\mathbf{b}$ at the end of $\mathbf{a}$ (the **triangle law**).
- $\mathbf{a} - \mathbf{b}$ is the vector from the end of $\mathbf{b}$ to the end of $\mathbf{a}$.
- $k\mathbf{a}$ is parallel to $\mathbf{a}$; it points the same way if $k > 0$ and the opposite way if $k < 0$.

**Midpoint.** The midpoint $M$ of $AB$ has position vector

$$\vec{OM} = \frac{\vec{OA} + \vec{OB}}{2} = \frac{\mathbf{a} + \mathbf{b}}{2}$$

This is a special case of the ratio theorem; the general ratio theorem is **not** required by 9709, but the midpoint formula is expected.

## 1.4 Parallel and Collinear Vectors

Two vectors are **parallel** if one is a scalar multiple of the other:

$$\mathbf{b} = k\mathbf{a} \quad \text{for some } k \neq 0$$

Three points $A$, $B$, $C$ are **collinear** if $\vec{AB}$ and $\vec{BC}$ are parallel **and** they share the point $B$. Checking parallel alone is not enough: two parallel vectors on different lines do not make the points collinear.

### Example 1 - Easy - Component arithmetic, magnitude and unit vector

> **Question:** The vectors $\mathbf{a} = 3\mathbf{i} - 2\mathbf{j} + \mathbf{k}$ and $\mathbf{b} = -\mathbf{i} + 4\mathbf{j} - 2\mathbf{k}$ are given. Find (a) $\mathbf{a} + \mathbf{b}$, (b) $2\mathbf{a} - 3\mathbf{b}$, (c) $|\mathbf{a}|$, (d) the unit vector in the direction of $\mathbf{a}$.

**Solution:**

Part (a):

$$\mathbf{a} + \mathbf{b} = (3 - 1)\mathbf{i} + (-2 + 4)\mathbf{j} + (1 - 2)\mathbf{k}$$

$$\mathbf{a} + \mathbf{b} = 2\mathbf{i} + 2\mathbf{j} - \mathbf{k} \quad\checkmark$$

Part (b):

$$2\mathbf{a} = 6\mathbf{i} - 4\mathbf{j} + 2\mathbf{k}, \qquad 3\mathbf{b} = -3\mathbf{i} + 12\mathbf{j} - 6\mathbf{k}$$

$$2\mathbf{a} - 3\mathbf{b} = (6 + 3)\mathbf{i} + (-4 - 12)\mathbf{j} + (2 + 6)\mathbf{k}$$

$$2\mathbf{a} - 3\mathbf{b} = 9\mathbf{i} - 16\mathbf{j} + 8\mathbf{k} \quad\checkmark$$

Part (c):

$$|\mathbf{a}| = \sqrt{3^2 + (-2)^2 + 1^2} = \sqrt{9 + 4 + 1} = \sqrt{14} \quad\checkmark$$

Part (d):

$$\hat{\mathbf{a}} = \frac{\mathbf{a}}{|\mathbf{a}|} = \frac{3\mathbf{i} - 2\mathbf{j} + \mathbf{k}}{\sqrt{14}} \quad\checkmark$$

**What the examiner wants:** each component handled separately, and the unit vector left in exact surd form. Do not replace $\sqrt{14}$ by a decimal unless the question asks for one.

### Example 2 - Easy - Displacement, length and midpoint

> **Question:** The points $A(1, 4, 2)$ and $B(2, 1, 3)$ are given. Find (a) $\vec{AB}$, (b) $|\vec{AB}|$, (c) the midpoint $M$ of $AB$, (d) the unit vector in the direction of $\vec{AB}$.

**Solution:**

Part (a) - head minus tail:

$$\vec{AB} = \vec{OB} - \vec{OA} = \begin{pmatrix} 2 \\ 1 \\ 3 \end{pmatrix} - \begin{pmatrix} 1 \\ 4 \\ 2 \end{pmatrix} = \begin{pmatrix} 1 \\ -3 \\ 1 \end{pmatrix} \quad\checkmark$$

Part (b):

$$|\vec{AB}| = \sqrt{1^2 + (-3)^2 + 1^2} = \sqrt{1 + 9 + 1} = \sqrt{11} \quad\checkmark$$

Part (c):

$$\vec{OM} = \frac{\vec{OA} + \vec{OB}}{2} = \frac{1}{2}\begin{pmatrix} 1 + 2 \\ 4 + 1 \\ 2 + 3 \end{pmatrix} = \begin{pmatrix} 3/2 \\ 5/2 \\ 5/2 \end{pmatrix} \quad\checkmark$$

Part (d):

$$\hat{\mathbf{u}} = \frac{1}{\sqrt{11}}\begin{pmatrix} 1 \\ -3 \\ 1 \end{pmatrix} \quad\checkmark$$

**What the examiner wants:** $\vec{AB} = \mathbf{b} - \mathbf{a}$ and the midpoint as the average of the two position vectors. Both are one-mark ideas, but they unlock the rest of the question.

### Example 3 - Medium - Proving three points are collinear

> **Question:** Show that the points $A(1, 2, 3)$, $B(3, 5, 9)$ and $C(5, 8, 15)$ are collinear.

**Solution:**

Find two consecutive displacement vectors:

$$\vec{AB} = \begin{pmatrix} 3 - 1 \\ 5 - 2 \\ 9 - 3 \end{pmatrix} = \begin{pmatrix} 2 \\ 3 \\ 6 \end{pmatrix}$$

$$\vec{BC} = \begin{pmatrix} 5 - 3 \\ 8 - 5 \\ 15 - 9 \end{pmatrix} = \begin{pmatrix} 2 \\ 3 \\ 6 \end{pmatrix}$$

Since $\vec{AB} = \vec{BC}$, the two vectors are parallel and they share the point $B$. Therefore $A$, $B$ and $C$ lie on the same straight line. $\checkmark$

As a check:

$$\vec{AC} = \begin{pmatrix} 4 \\ 6 \\ 12 \end{pmatrix} = 2\vec{AB}$$

so $AC = AB + BC$ in both length and direction.

**What the examiner wants:** the explicit statement that the vectors are parallel **and** share a point. "They are parallel" alone does not prove collinearity.

### Example 4 - Medium - A vector proof with midpoints

> **Question:** In triangle $OAB$, let $\vec{OA} = \mathbf{a}$ and $\vec{OB} = \mathbf{b}$. The point $M$ is the midpoint of $OA$ and $N$ is the midpoint of $OB$. Show that $MN$ is parallel to $AB$ and that $MN = \frac{1}{2}AB$.

**Solution:**

Midpoint position vectors:

$$\vec{OM} = \frac{1}{2}\mathbf{a}, \qquad \vec{ON} = \frac{1}{2}\mathbf{b}$$

Then

$$\vec{MN} = \vec{ON} - \vec{OM} = \frac{1}{2}\mathbf{b} - \frac{1}{2}\mathbf{a} = \frac{1}{2}(\mathbf{b} - \mathbf{a})$$

But

$$\vec{AB} = \mathbf{b} - \mathbf{a}$$

Therefore

$$\vec{MN} = \frac{1}{2}\vec{AB}$$

So $MN$ is parallel to $AB$ and its length is half of $AB$. $\checkmark$

**What the examiner wants:** the factor $\frac{1}{2}$ kept outside the bracket, then a clear comparison with $\vec{AB}$. This is the standard "midpoint theorem" proof and it reappears inside harder geometry questions.

### Practice Questions - Part 1

1. (Easy) For $\mathbf{a} = 2\mathbf{i} - \mathbf{j} + 3\mathbf{k}$ and $\mathbf{b} = 4\mathbf{i} + 2\mathbf{j} - \mathbf{k}$, find $\mathbf{a} + \mathbf{b}$, $\mathbf{a} - \mathbf{b}$, $3\mathbf{a} + 2\mathbf{b}$, $|\mathbf{a}|$ and the unit vector in the direction of $\mathbf{a}$.
2. (Easy) For $P(2, -1, 3)$ and $Q(5, 3, 1)$, find $\vec{PQ}$, $|\vec{PQ}|$ and the midpoint of $PQ$.
3. (Medium) Show that $A(0, 1, 2)$, $B(2, 5, 6)$ and $C(5, 11, 12)$ are collinear.
4. (Medium) For $\mathbf{a} = 3\mathbf{i} + 2\mathbf{j} - \mathbf{k}$ and $\mathbf{b} = \mathbf{i} - \mathbf{j} + 4\mathbf{k}$, find the unit vector in the direction of $2\mathbf{a} - \mathbf{b}$.
5. (Medium) $OABC$ is a parallelogram with $\vec{OA} = \mathbf{a}$ and $\vec{OC} = \mathbf{c}$. Find $\vec{OB}$ and $\vec{AC}$ in terms of $\mathbf{a}$ and $\mathbf{c}$.
6. (Medium) $M$ is the midpoint of $AB$, where $\vec{OA} = \mathbf{a}$ and $\vec{OB} = \mathbf{b}$. Show that $\vec{OM} = \frac{1}{2}(\mathbf{a} + \mathbf{b})$.

**Solutions:**

Question 1:

$$\mathbf{a} + \mathbf{b} = 6\mathbf{i} + \mathbf{j} + 2\mathbf{k}$$

$$\mathbf{a} - \mathbf{b} = -2\mathbf{i} - 3\mathbf{j} + 4\mathbf{k}$$

$$3\mathbf{a} + 2\mathbf{b} = (6\mathbf{i} - 3\mathbf{j} + 9\mathbf{k}) + (8\mathbf{i} + 4\mathbf{j} - 2\mathbf{k}) = 14\mathbf{i} + \mathbf{j} + 7\mathbf{k}$$

$$|\mathbf{a}| = \sqrt{4 + 1 + 9} = \sqrt{14}$$

$$\hat{\mathbf{a}} = \frac{2\mathbf{i} - \mathbf{j} + 3\mathbf{k}}{\sqrt{14}}$$

Question 2:

$$\vec{PQ} = \begin{pmatrix} 5 - 2 \\ 3 - (-1) \\ 1 - 3 \end{pmatrix} = \begin{pmatrix} 3 \\ 4 \\ -2 \end{pmatrix}$$

$$|\vec{PQ}| = \sqrt{9 + 16 + 4} = \sqrt{29}$$

$$\text{midpoint} = \left(\frac{2 + 5}{2}, \frac{-1 + 3}{2}, \frac{3 + 1}{2}\right) = \left(\frac{7}{2}, 1, 2\right)$$

Question 3:

$$\vec{AB} = \begin{pmatrix} 2 \\ 4 \\ 4 \end{pmatrix}, \qquad \vec{BC} = \begin{pmatrix} 3 \\ 6 \\ 6 \end{pmatrix} = \frac{3}{2}\vec{AB}$$

Since $\vec{BC}$ is a scalar multiple of $\vec{AB}$ and both pass through $B$, the points are collinear.

Question 4:

$$2\mathbf{a} - \mathbf{b} = (6\mathbf{i} + 4\mathbf{j} - 2\mathbf{k}) - (\mathbf{i} - \mathbf{j} + 4\mathbf{k}) = 5\mathbf{i} + 5\mathbf{j} - 6\mathbf{k}$$

$$|2\mathbf{a} - \mathbf{b}| = \sqrt{25 + 25 + 36} = \sqrt{86}$$

$$\text{unit vector} = \frac{5\mathbf{i} + 5\mathbf{j} - 6\mathbf{k}}{\sqrt{86}}$$

Question 5:

$$\vec{OB} = \vec{OA} + \vec{OC} = \mathbf{a} + \mathbf{c}$$

$$\vec{AC} = \vec{OC} - \vec{OA} = \mathbf{c} - \mathbf{a}$$

Question 6:

$$\vec{OM} = \vec{OA} + \vec{AM} = \mathbf{a} + \frac{1}{2}\vec{AB}$$

$$\vec{OM} = \mathbf{a} + \frac{1}{2}(\mathbf{b} - \mathbf{a}) = \frac{1}{2}\mathbf{a} + \frac{1}{2}\mathbf{b} = \frac{1}{2}(\mathbf{a} + \mathbf{b})$$

---

# PART 2: The Scalar Product

The scalar product (also called the **dot product**) turns two vectors into a single number. That number encodes the angle between them, which is why it is the main tool for proving perpendicularity and for finding angles in 3D.

## 2.1 Definition and Component Formula

For two non-zero vectors $\mathbf{a}$ and $\mathbf{b}$, with angle $\theta$ between them,

$$\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}|\,|\mathbf{b}|\cos\theta$$

In components,

$$\mathbf{a} \cdot \mathbf{b} = a_1b_1 + a_2b_2 + a_3b_3$$

The two formulas are equivalent. Use the component formula when you know the components; use the cosine formula when you know (or want) the angle.

**Sign of the dot product:**

| $\mathbf{a} \cdot \mathbf{b}$ | Angle $\theta$ | Geometry |
|---|---|---|
| Positive | $0 \le \theta < 90^\circ$ | acute |
| Zero | $\theta = 90^\circ$ | perpendicular |
| Negative | $90^\circ < \theta \le 180^\circ$ | obtuse |

**Key properties:**

$$\mathbf{a} \cdot \mathbf{b} = \mathbf{b} \cdot \mathbf{a} \qquad \text{(commutative)}$$

$$\mathbf{a} \cdot (\mathbf{b} + \mathbf{c}) = \mathbf{a} \cdot \mathbf{b} + \mathbf{a} \cdot \mathbf{c} \qquad \text{(distributive)}$$

$$\mathbf{a} \cdot \mathbf{a} = |\mathbf{a}|^2$$

$$(k\mathbf{a}) \cdot \mathbf{b} = k(\mathbf{a} \cdot \mathbf{b})$$

## 2.2 The Angle Between Two Vectors

Rearranging the definition:

$$\cos\theta = \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}|\,|\mathbf{b}|}$$

Then $\theta = \cos^{-1}\left(\dfrac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}|\,|\mathbf{b}|}\right)$.

> ⭐ **Watch Out!** The formula gives the angle between the two vectors when they are placed **tail to tail**. For the angle between two **lines**, the direction vectors can be reversed without changing the line, so take the absolute value of the dot product to get the acute angle:
> $$\cos\theta_{\text{acute}} = \frac{|\mathbf{a} \cdot \mathbf{b}|}{|\mathbf{a}|\,|\mathbf{b}|}$$
> For an angle such as $\angle BAC$, the vectors $\vec{AB}$ and $\vec{AC}$ both start at $A$, so do **not** take the absolute value: an obtuse angle is a legitimate answer.

## 2.3 Perpendicular Vectors

Two non-zero vectors are perpendicular exactly when

$$\mathbf{a} \cdot \mathbf{b} = 0$$

This is the fastest way to prove a right angle or to find an unknown component.

## 2.4 Projections and the Foot of the Perpendicular

The **scalar projection** of $\mathbf{a}$ onto the direction of $\mathbf{b}$ is

$$\mathbf{a} \cdot \hat{\mathbf{b}} = \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{b}|}$$

This is the signed length of the shadow of $\mathbf{a}$ along $\mathbf{b}$. It becomes the key idea in Part 5, where the foot of the perpendicular is found by forcing $\vec{PF} \cdot \mathbf{d} = 0$.

### Example 5 - Easy - Dot product and angle

> **Question:** For $\mathbf{a} = 2\mathbf{i} + 3\mathbf{j} - \mathbf{k}$ and $\mathbf{b} = \mathbf{i} - \mathbf{j} + 2\mathbf{k}$, find $\mathbf{a} \cdot \mathbf{b}$ and the angle between $\mathbf{a}$ and $\mathbf{b}$.

**Solution:**

Dot product:

$$\mathbf{a} \cdot \mathbf{b} = (2)(1) + (3)(-1) + (-1)(2) = 2 - 3 - 2 = -3$$

Magnitudes:

$$|\mathbf{a}| = \sqrt{4 + 9 + 1} = \sqrt{14}, \qquad |\mathbf{b}| = \sqrt{1 + 1 + 4} = \sqrt{6}$$

Cosine:

$$\cos\theta = \frac{-3}{\sqrt{14}\sqrt{6}} = \frac{-3}{\sqrt{84}} = -\frac{3}{2\sqrt{21}} = -\frac{\sqrt{21}}{14}$$

$$\theta = \cos^{-1}\left(-\frac{\sqrt{21}}{14}\right) \approx 109.1^\circ \quad\checkmark$$

The negative dot product tells you the angle is obtuse, which matches the diagram: the vectors point broadly away from each other.

**What the examiner wants:** the component calculation, both magnitudes, and an answer in degrees to one decimal place (or radians if specified). Keep the exact surd form until the final evaluation.

### Example 6 - Easy - Finding an unknown component

> **Question:** The vectors $\mathbf{a} = 2\mathbf{i} + p\mathbf{j} - \mathbf{k}$ and $\mathbf{b} = \mathbf{i} + 2\mathbf{j} + 3\mathbf{k}$ are perpendicular. Find $p$.

**Solution:**

Perpendicular means $\mathbf{a} \cdot \mathbf{b} = 0$:

$$(2)(1) + (p)(2) + (-1)(3) = 0$$

$$2 + 2p - 3 = 0$$

$$2p = 1$$

$$p = \frac{1}{2} \quad\checkmark$$

**What the examiner wants:** the equation set to zero immediately. Do not compute magnitudes; perpendicularity never needs them.

### Example 7 - Medium - Angle in a triangle

> **Question:** The points $A(1, 4, 2)$, $B(2, 1, 3)$ and $C(2, 3, 5)$ are given. Find the angle $\angle BAC$.

**Solution:**

Both vectors must start at $A$:

$$\vec{AB} = \begin{pmatrix} 2 - 1 \\ 1 - 4 \\ 3 - 2 \end{pmatrix} = \begin{pmatrix} 1 \\ -3 \\ 1 \end{pmatrix}$$

$$\vec{AC} = \begin{pmatrix} 2 - 1 \\ 3 - 4 \\ 5 - 2 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}$$

Dot product:

$$\vec{AB} \cdot \vec{AC} = (1)(1) + (-3)(-1) + (1)(3) = 1 + 3 + 3 = 7$$

Magnitudes:

$$|\vec{AB}| = \sqrt{1 + 9 + 1} = \sqrt{11}, \qquad |\vec{AC}| = \sqrt{1 + 1 + 9} = \sqrt{11}$$

Cosine:

$$\cos\angle BAC = \frac{7}{\sqrt{11}\sqrt{11}} = \frac{7}{11}$$

$$\angle BAC = \cos^{-1}\left(\frac{7}{11}\right) \approx 50.5^\circ \quad\checkmark$$

**What the examiner wants:** the vectors pointing **away from the vertex** $A$. A common error is to use $\vec{BA}$ or $\vec{CA}$, which gives the supplement of the correct angle.

### Example 8 - Medium - Adding a multiple to make a right angle

> **Question:** The vectors $\mathbf{a} = 2\mathbf{i} - \mathbf{j} + 3\mathbf{k}$ and $\mathbf{b} = \mathbf{i} + 4\mathbf{j} - \mathbf{k}$ are given. Find the value of $\lambda$ for which $\mathbf{a} + \lambda\mathbf{b}$ is perpendicular to $\mathbf{a}$.

**Solution:**

We need

$$(\mathbf{a} + \lambda\mathbf{b}) \cdot \mathbf{a} = 0$$

Expand:

$$\mathbf{a} \cdot \mathbf{a} + \lambda(\mathbf{b} \cdot \mathbf{a}) = 0$$

Compute:

$$\mathbf{a} \cdot \mathbf{a} = 2^2 + (-1)^2 + 3^2 = 14$$

$$\mathbf{b} \cdot \mathbf{a} = (1)(2) + (4)(-1) + (-1)(3) = 2 - 4 - 3 = -5$$

Substitute:

$$14 + \lambda(-5) = 0$$

$$\lambda = \frac{14}{5} \quad\checkmark$$

**What the examiner wants:** the distributive law used cleanly, then the two dot products evaluated separately. Resist the temptation to expand $\mathbf{a} + \lambda\mathbf{b}$ component by component; the dot-product algebra is faster and less error-prone.

### Example 9 - Medium - Proving a right angle and finding area

> **Question:** The points $A(1, 2, 3)$, $B(4, 2, 7)$ and $C(1, 6, 3)$ are given. Show that triangle $ABC$ is right-angled at $A$, and find its area.

**Solution:**

Vectors from $A$:

$$\vec{AB} = \begin{pmatrix} 3 \\ 0 \\ 4 \end{pmatrix}, \qquad \vec{AC} = \begin{pmatrix} 0 \\ 4 \\ 0 \end{pmatrix}$$

Dot product:

$$\vec{AB} \cdot \vec{AC} = (3)(0) + (0)(4) + (4)(0) = 0$$

Since the dot product is zero, $\angle BAC = 90^\circ$. $\checkmark$

Lengths:

$$|\vec{AB}| = \sqrt{9 + 0 + 16} = 5, \qquad |\vec{AC}| = \sqrt{0 + 16 + 0} = 4$$

Area of a right-angled triangle:

$$\text{Area} = \frac{1}{2} \times 5 \times 4 = 10 \quad\checkmark$$

**What the examiner wants:** the zero dot product explicitly interpreted as a right angle, then the two perpendicular sides used as base and height. Do not use the hypotenuse in the area formula.

### Example 10 - Hard - A dot-product proof

> **Question:** For any two vectors $\mathbf{a}$ and $\mathbf{b}$, prove that
> $$(\mathbf{a} - \mathbf{b}) \cdot (\mathbf{a} + \mathbf{b}) = |\mathbf{a}|^2 - |\mathbf{b}|^2$$
> Hence show that the diagonals of a parallelogram are perpendicular exactly when its sides are equal in length.

**Solution:**

Expand using distributivity:

$$(\mathbf{a} - \mathbf{b}) \cdot (\mathbf{a} + \mathbf{b}) = \mathbf{a} \cdot \mathbf{a} + \mathbf{a} \cdot \mathbf{b} - \mathbf{b} \cdot \mathbf{a} - \mathbf{b} \cdot \mathbf{b}$$

Since $\mathbf{a} \cdot \mathbf{b} = \mathbf{b} \cdot \mathbf{a}$ and $\mathbf{a} \cdot \mathbf{a} = |\mathbf{a}|^2$:

$$(\mathbf{a} - \mathbf{b}) \cdot (\mathbf{a} + \mathbf{b}) = |\mathbf{a}|^2 - |\mathbf{b}|^2 \quad\checkmark$$

Now let the parallelogram have adjacent sides $\mathbf{a}$ and $\mathbf{b}$. Its diagonals are $\mathbf{a} + \mathbf{b}$ and $\mathbf{a} - \mathbf{b}$. They are perpendicular exactly when

$$(\mathbf{a} + \mathbf{b}) \cdot (\mathbf{a} - \mathbf{b}) = 0$$

By the result just proved (the sign swap does not change the value):

$$|\mathbf{a}|^2 - |\mathbf{b}|^2 = 0$$

$$|\mathbf{a}| = |\mathbf{b}|$$

So the diagonals are perpendicular exactly when the adjacent sides are equal, i.e. when the parallelogram is a rhombus. $\checkmark$

**What the examiner wants:** the expansion with the cross terms cancelling, then a clear logical link between "diagonals perpendicular" and "sides equal". This is a standard proof; learn the pattern.

### Practice Questions - Part 2

1. (Easy) For $\mathbf{a} = \mathbf{i} + 2\mathbf{j} + 2\mathbf{k}$ and $\mathbf{b} = 3\mathbf{i} - \mathbf{j} + \mathbf{k}$, find $\mathbf{a} \cdot \mathbf{b}$ and the angle between them.
2. (Easy) Find $k$ such that $\mathbf{a} = 2\mathbf{i} + k\mathbf{j} - 3\mathbf{k}$ and $\mathbf{b} = k\mathbf{i} + \mathbf{j} + 4\mathbf{k}$ are perpendicular.
3. (Medium) For $A(1, 0, 2)$, $B(3, 2, 1)$ and $C(2, 4, 0)$, find the angle $\angle ABC$.
4. (Medium) Show that the vectors $\mathbf{a} = \mathbf{i} + \mathbf{j} + \mathbf{k}$, $\mathbf{b} = \mathbf{i} - \mathbf{j}$ and $\mathbf{c} = \mathbf{i} + \mathbf{j} - 2\mathbf{k}$ are mutually perpendicular.
5. (Medium) For $\mathbf{a} = \mathbf{i} + 2\mathbf{j} + 2\mathbf{k}$ and $\mathbf{b} = 2\mathbf{i} + \mathbf{j} - 2\mathbf{k}$, show that $\mathbf{a} \perp \mathbf{b}$ and find the area of the triangle with sides $\mathbf{a}$ and $\mathbf{b}$.
6. (Hard) Prove that for any two vectors $\mathbf{a}$ and $\mathbf{b}$,
> $$|\mathbf{a} + \mathbf{b}|^2 + |\mathbf{a} - \mathbf{b}|^2 = 2|\mathbf{a}|^2 + 2|\mathbf{b}|^2$$
> and interpret the result for a parallelogram.

**Solutions:**

Question 1:

$$\mathbf{a} \cdot \mathbf{b} = (1)(3) + (2)(-1) + (2)(1) = 3 - 2 + 2 = 3$$

$$|\mathbf{a}| = \sqrt{1 + 4 + 4} = 3, \qquad |\mathbf{b}| = \sqrt{9 + 1 + 1} = \sqrt{11}$$

$$\cos\theta = \frac{3}{3\sqrt{11}} = \frac{1}{\sqrt{11}}$$

$$\theta = \cos^{-1}\left(\frac{1}{\sqrt{11}}\right) \approx 72.5^\circ$$

Question 2:

$$(2)(k) + (k)(1) + (-3)(4) = 0$$

$$3k - 12 = 0$$

$$k = 4$$

Question 3:

$$\vec{BA} = \begin{pmatrix} 1 - 3 \\ 0 - 2 \\ 2 - 1 \end{pmatrix} = \begin{pmatrix} -2 \\ -2 \\ 1 \end{pmatrix}, \qquad \vec{BC} = \begin{pmatrix} 2 - 3 \\ 4 - 2 \\ 0 - 1 \end{pmatrix} = \begin{pmatrix} -1 \\ 2 \\ -1 \end{pmatrix}$$

$$\vec{BA} \cdot \vec{BC} = (-2)(-1) + (-2)(2) + (1)(-1) = 2 - 4 - 1 = -3$$

$$|\vec{BA}| = \sqrt{4 + 4 + 1} = 3, \qquad |\vec{BC}| = \sqrt{1 + 4 + 1} = \sqrt{6}$$

$$\cos\angle ABC = \frac{-3}{3\sqrt{6}} = -\frac{1}{\sqrt{6}}$$

$$\angle ABC = \cos^{-1}\left(-\frac{1}{\sqrt{6}}\right) \approx 114.1^\circ$$

Question 4:

$$\mathbf{a} \cdot \mathbf{b} = (1)(1) + (1)(-1) + (1)(0) = 0$$

$$\mathbf{a} \cdot \mathbf{c} = (1)(1) + (1)(1) + (1)(-2) = 1 + 1 - 2 = 0$$

$$\mathbf{b} \cdot \mathbf{c} = (1)(1) + (-1)(1) + (0)(-2) = 1 - 1 = 0$$

All three dot products are zero, so the three vectors are mutually perpendicular.

Question 5:

$$\mathbf{a} \cdot \mathbf{b} = (1)(2) + (2)(1) + (2)(-2) = 2 + 2 - 4 = 0$$

So $\mathbf{a} \perp \mathbf{b}$. The triangle has perpendicular sides of lengths

$$|\mathbf{a}| = \sqrt{1 + 4 + 4} = 3, \qquad |\mathbf{b}| = \sqrt{4 + 1 + 4} = 3$$

$$\text{Area} = \frac{1}{2} \times 3 \times 3 = \frac{9}{2}$$

Question 6:

$$|\mathbf{a} + \mathbf{b}|^2 = (\mathbf{a} + \mathbf{b}) \cdot (\mathbf{a} + \mathbf{b}) = |\mathbf{a}|^2 + 2\mathbf{a} \cdot \mathbf{b} + |\mathbf{b}|^2$$

$$|\mathbf{a} - \mathbf{b}|^2 = (\mathbf{a} - \mathbf{b}) \cdot (\mathbf{a} - \mathbf{b}) = |\mathbf{a}|^2 - 2\mathbf{a} \cdot \mathbf{b} + |\mathbf{b}|^2$$

Adding:

$$|\mathbf{a} + \mathbf{b}|^2 + |\mathbf{a} - \mathbf{b}|^2 = 2|\mathbf{a}|^2 + 2|\mathbf{b}|^2$$

This is the **parallelogram law**: the sum of the squares of the diagonals equals the sum of the squares of the four sides.

---

# PART 3: The Vector Equation of a Line

## 3.1 The Equation $\mathbf{r} = \mathbf{a} + \lambda\mathbf{b}$

A straight line is fixed by one point and one direction. In vector form,

$$\mathbf{r} = \mathbf{a} + \lambda\mathbf{b}$$

where:

- $\mathbf{r}$ is the **position vector of a general point** on the line (the variable);
- $\mathbf{a}$ is the position vector of a **known point** on the line;
- $\mathbf{b}$ is a **direction vector** parallel to the line;
- $\lambda$ is a scalar parameter.

In column form:

$$\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix} + \lambda\begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix}$$

Equating components gives the **parametric equations**:

$$x = a_1 + \lambda b_1, \qquad y = a_2 + \lambda b_2, \qquad z = a_3 + \lambda b_3$$

Different values of $\lambda$ give different points on the line. Every point on the line corresponds to exactly one value of $\lambda$.

## 3.2 Finding the Equation from Two Points

If the line passes through $A$ and $B$, use

$$\mathbf{a} = \vec{OA}, \qquad \mathbf{b} = \vec{AB} = \vec{OB} - \vec{OA}$$

Then

$$\mathbf{r} = \vec{OA} + \lambda(\vec{OB} - \vec{OA})$$

Equivalently, you may start from $B$:

$$\mathbf{r} = \vec{OB} + \mu(\vec{OA} - \vec{OB})$$

Both describe the same line. The direction vector may be multiplied by any non-zero scalar; keep it as simple as possible.

## 3.3 Testing Whether a Point Lies on a Line

Given a point $P$ with position vector $\mathbf{p}$, solve

$$\mathbf{p} = \mathbf{a} + \lambda\mathbf{b}$$

for $\lambda$ using one component, then check that the same $\lambda$ works in the other two components. If it does, $P$ lies on the line; if not, it does not.

> ⭐ **Watch Out!** A point can satisfy two of the three component equations and fail the third. You must check **all three**. This is exactly the same consistency test used for intersecting lines in Part 4.

## 3.4 Parallel and Perpendicular Lines

Two lines with direction vectors $\mathbf{b}_1$ and $\mathbf{b}_2$ are:

- **parallel** if $\mathbf{b}_1 = k\mathbf{b}_2$ for some non-zero $k$;
- **perpendicular** if $\mathbf{b}_1 \cdot \mathbf{b}_2 = 0$.

Parallel lines may be the same line or distinct lines. To decide, check whether a point on one line lies on the other.

### Example 11 - Easy - Writing and using a line equation

> **Question:** A line passes through $A(1, 4, 2)$ and has direction vector $\mathbf{d} = 2\mathbf{i} - \mathbf{j} + 3\mathbf{k}$. (a) Write down a vector equation for the line. (b) Find the point on the line with $\lambda = 2$. (c) Find where the line meets the plane $z = 0$.

**Solution:**

Part (a):

$$\mathbf{r} = \begin{pmatrix} 1 \\ 4 \\ 2 \end{pmatrix} + \lambda\begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} \quad\checkmark$$

Part (b) - substitute $\lambda = 2$:

$$\mathbf{r} = \begin{pmatrix} 1 + 4 \\ 4 - 2 \\ 2 + 6 \end{pmatrix} = \begin{pmatrix} 5 \\ 2 \\ 8 \end{pmatrix}$$

The point is $(5, 2, 8)$. $\checkmark$

Part (c) - set the $z$-component equal to $0$:

$$2 + 3\lambda = 0 \implies \lambda = -\frac{2}{3}$$

Then

$$x = 1 + 2\left(-\frac{2}{3}\right) = -\frac{1}{3}, \qquad y = 4 - \left(-\frac{2}{3}\right) = \frac{14}{3}$$

The line meets $z = 0$ at $\left(-\frac{1}{3}, \frac{14}{3}, 0\right)$. $\checkmark$

**What the examiner wants:** the structure $\mathbf{r} = \mathbf{a} + \lambda\mathbf{b}$ written explicitly, then component-by-component substitution.

### Example 12 - Easy - Line through two points

> **Question:** Find a vector equation for the line through $A(1, 4, 2)$ and $B(2, 1, 3)$.

**Solution:**

A point on the line is $\vec{OA} = \begin{pmatrix} 1 \\ 4 \\ 2 \end{pmatrix}$.

A direction vector is

$$\vec{AB} = \begin{pmatrix} 2 - 1 \\ 1 - 4 \\ 3 - 2 \end{pmatrix} = \begin{pmatrix} 1 \\ -3 \\ 1 \end{pmatrix}$$

Therefore

$$\mathbf{r} = \begin{pmatrix} 1 \\ 4 \\ 2 \end{pmatrix} + \lambda\begin{pmatrix} 1 \\ -3 \\ 1 \end{pmatrix} \quad\checkmark$$

Any non-zero multiple of the direction vector is equally valid, for example

$$\mathbf{r} = \begin{pmatrix} 2 \\ 1 \\ 3 \end{pmatrix} + \mu\begin{pmatrix} -1 \\ 3 \\ -1 \end{pmatrix}$$

**What the examiner wants:** a correct point and a correct direction. Do not use $\vec{OA} + \lambda\vec{OA}$ or $\vec{OA} + \lambda\vec{OB}$: the direction must be the displacement between the two points.

### Example 13 - Medium - Does the point lie on the line?

> **Question:** Determine whether $P(5, 0, 11)$ lies on the line
> $$\mathbf{r} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + \lambda\begin{pmatrix} 2 \\ -1 \\ 4 \end{pmatrix}$$

**Solution:**

Equate components:

$$1 + 2\lambda = 5 \implies \lambda = 2$$

$$2 - \lambda = 0 \implies \lambda = 2$$

$$3 + 4\lambda = 11 \implies \lambda = 2$$

The same value $\lambda = 2$ satisfies all three equations, so $P$ lies on the line. $\checkmark$

**What the examiner wants:** the same $\lambda$ from every component. If one component gives a different value, stop and write "not on the line".

### Example 14 - Medium - A parallel line through a given point

> **Question:** A line passes through $A(2, -1, 3)$ and is parallel to the line
> $$\mathbf{r} = \begin{pmatrix} 1 \\ 0 \\ 4 \end{pmatrix} + \mu\begin{pmatrix} 3 \\ 2 \\ -1 \end{pmatrix}$$
> (a) Find a vector equation for the new line. (b) Determine whether $B(8, 3, 1)$ lies on it.

**Solution:**

Part (a) - parallel lines have the same direction vector:

$$\mathbf{r} = \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} + \lambda\begin{pmatrix} 3 \\ 2 \\ -1 \end{pmatrix} \quad\checkmark$$

Part (b) - equate components:

$$2 + 3\lambda = 8 \implies \lambda = 2$$

$$-1 + 2\lambda = 3 \implies \lambda = 2$$

$$3 - \lambda = 1 \implies \lambda = 2$$

All three give $\lambda = 2$, so $B$ lies on the new line. $\checkmark$

**What the examiner wants:** reuse the direction vector unchanged (or as a multiple), then run the three-component check.

### Example 15 - Medium - Finding an unknown from a parallel condition

> **Question:** The line through $A(1, 2, 3)$ and $B(4, 5, k)$ is parallel to the line
> $$\mathbf{r} = \begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix} + \lambda\begin{pmatrix} 1 \\ 1 \\ 2 \end{pmatrix}$$
> Find $k$.

**Solution:**

Direction of $AB$:

$$\vec{AB} = \begin{pmatrix} 3 \\ 3 \\ k - 3 \end{pmatrix}$$

For the lines to be parallel, $\vec{AB}$ must be a scalar multiple of $\begin{pmatrix} 1 \\ 1 \\ 2 \end{pmatrix}$:

$$\begin{pmatrix} 3 \\ 3 \\ k - 3 \end{pmatrix} = t\begin{pmatrix} 1 \\ 1 \\ 2 \end{pmatrix}$$

From the first two components, $t = 3$. Then

$$k - 3 = 2t = 6$$

$$k = 9 \quad\checkmark$$

**What the examiner wants:** the scalar multiplier identified from a component where both entries are known, then applied to the unknown component.

### Example 16 - Medium - Line parallel to a line through two points

> **Question:** A line passes through $P(2, -1, 4)$ and is parallel to the line through $Q(1, 3, 0)$ and $R(4, 5, 6)$. Find a vector equation for the line through $P$.

**Solution:**

Direction of $QR$:

$$\vec{QR} = \begin{pmatrix} 4 - 1 \\ 5 - 3 \\ 6 - 0 \end{pmatrix} = \begin{pmatrix} 3 \\ 2 \\ 6 \end{pmatrix}$$

Therefore the line through $P$ is

$$\mathbf{r} = \begin{pmatrix} 2 \\ -1 \\ 4 \end{pmatrix} + \lambda\begin{pmatrix} 3 \\ 2 \\ 6 \end{pmatrix} \quad\checkmark$$

You may simplify the direction to $\begin{pmatrix} 1 \\ 2/3 \\ 2 \end{pmatrix}$ or any other non-zero multiple; the unsimplified integer version is usually safest.

**What the examiner wants:** the direction taken from the *other* line, and the given point used as $\mathbf{a}$.

### Practice Questions - Part 3

1. (Easy) A line passes through $(1, -2, 3)$ with direction vector $\begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}$. Find the point with $\lambda = 3$, and find where the line meets the plane $x = 0$.
2. (Easy) Find a vector equation for the line through $A(2, 3, -1)$ and $B(4, -1, 5)$.
3. (Medium) Determine whether $(7, 4, -3)$ lies on the line $\mathbf{r} = \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} + \lambda\begin{pmatrix} 3 \\ 1 \\ -2 \end{pmatrix}$.
4. (Medium) The line through $(1, 2, 3)$ and $(4, k, 9)$ is parallel to the vector $\begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}$. Find $k$.
5. (Medium) Find a vector equation for the line through $(3, -1, 2)$ parallel to the line $\mathbf{r} = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} + \mu\begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}$.
6. (Medium) Show that the line through $A(1, 1, 1)$ and $B(3, 5, 9)$ is parallel to the line through $C(0, 0, 0)$ and $D(1, 2, 4)$.

**Solutions:**

Question 1 - at $\lambda = 3$:

$$\mathbf{r} = \begin{pmatrix} 1 + 6 \\ -2 + 3 \\ 3 - 3 \end{pmatrix} = \begin{pmatrix} 7 \\ 1 \\ 0 \end{pmatrix}$$

The point is $(7, 1, 0)$.

For $x = 0$:

$$1 + 2\lambda = 0 \implies \lambda = -\frac{1}{2}$$

$$y = -2 - \frac{1}{2} = -\frac{5}{2}, \qquad z = 3 + \frac{1}{2} = \frac{7}{2}$$

The line meets $x = 0$ at $\left(0, -\frac{5}{2}, \frac{7}{2}\right)$.

Question 2:

$$\vec{AB} = \begin{pmatrix} 2 \\ -4 \\ 6 \end{pmatrix} = 2\begin{pmatrix} 1 \\ -2 \\ 3 \end{pmatrix}$$

$$\mathbf{r} = \begin{pmatrix} 2 \\ 3 \\ -1 \end{pmatrix} + \lambda\begin{pmatrix} 1 \\ -2 \\ 3 \end{pmatrix}$$

Question 3:

$$1 + 3\lambda = 7 \implies \lambda = 2$$

$$2 + \lambda = 4 \implies \lambda = 2$$

$$1 - 2\lambda = -3 \implies \lambda = 2$$

All three agree, so the point lies on the line.

Question 4:

$$\vec{AB} = \begin{pmatrix} 3 \\ k - 2 \\ 6 \end{pmatrix}$$

For this to be parallel to $\begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}$, the first component gives a multiplier of $3$:

$$\begin{pmatrix} 3 \\ k - 2 \\ 6 \end{pmatrix} = 3\begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}$$

$$k - 2 = 6 \implies k = 8$$

Question 5:

$$\mathbf{r} = \begin{pmatrix} 3 \\ -1 \\ 2 \end{pmatrix} + \lambda\begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}$$

Question 6:

$$\vec{AB} = \begin{pmatrix} 2 \\ 4 \\ 8 \end{pmatrix} = 2\begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}, \qquad \vec{CD} = \begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}$$

Since $\vec{AB} = 2\vec{CD}$, the direction vectors are parallel, so the two lines are parallel.

---

# PART 4: Parallel, Intersecting and Skew Lines

Two lines in 3D have exactly three possible relationships:

1. **Parallel** - the direction vectors are scalar multiples.
2. **Intersecting** - they meet at exactly one point.
3. **Skew** - they are not parallel and they never meet. They lie in different planes and pass each other at different heights.

The syllabus explicitly requires you to determine which case applies and to find the intersection when it exists.

## 4.1 The Intersection Algorithm

Write the two lines with **different** parameters:

$$\ell_1: \mathbf{r} = \mathbf{a}_1 + \lambda\mathbf{b}_1$$

$$\ell_2: \mathbf{r} = \mathbf{a}_2 + \mu\mathbf{b}_2$$

At a point of intersection, the position vectors are equal:

$$\mathbf{a}_1 + \lambda\mathbf{b}_1 = \mathbf{a}_2 + \mu\mathbf{b}_2$$

Equating components gives **three equations in the two unknowns** $\lambda$ and $\mu$:

$$a_{1x} + \lambda b_{1x} = a_{2x} + \mu b_{2x}$$

$$a_{1y} + \lambda b_{1y} = a_{2y} + \mu b_{2y}$$

$$a_{1z} + \lambda b_{1z} = a_{2z} + \mu b_{2z}$$

**Method:**

1. Check the direction vectors first. If $\mathbf{b}_1 = k\mathbf{b}_2$, the lines are parallel; stop (unless you also need to decide whether they are the same line).
2. Solve any two of the three equations simultaneously for $\lambda$ and $\mu$.
3. Substitute into the **third** equation.
4. If the third equation is satisfied, the lines intersect; substitute $\lambda$ (or $\mu$) into either line to get the point.
5. If the third equation is not satisfied, the lines are skew.

> ⭐ **Watch Out!** Never solve all three equations as if they were independent. There are only two unknowns, so a solution of two equations is only a *candidate*; the third equation is the consistency check that separates "intersect" from "skew".

## 4.2 Parallel Versus the Same Line

If the direction vectors are parallel, the lines are either distinct parallel lines or the same line. Pick a point on the first line and test whether it lies on the second (using the three-component check from Part 3). If it does, the lines coincide; if not, they are distinct parallel lines.

## 4.3 The Angle Between Two Lines

The angle between two lines is the angle between their direction vectors. Because a direction vector can be reversed without changing the line, take the **acute** angle:

$$\cos\theta = \frac{|\mathbf{b}_1 \cdot \mathbf{b}_2|}{|\mathbf{b}_1|\,|\mathbf{b}_2|}, \qquad 0 \le \theta \le 90^\circ$$

If the question asks for the angle between two specific vectors (rather than lines), do not take the absolute value; the angle can be obtuse.

### Example 17 - Medium - Finding an intersection

> **Question:** The lines
> $$\ell_1: \mathbf{r} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + \lambda\begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix}, \qquad \ell_2: \mathbf{r} = \begin{pmatrix} 3 \\ 1 \\ 4 \end{pmatrix} + \mu\begin{pmatrix} 1 \\ 1 \\ 2 \end{pmatrix}$$
> intersect. Find the point of intersection.

**Solution:**

Equate components:

$$1 + 2\lambda = 3 + \mu \quad \text{(1)}$$

$$2 - \lambda = 1 + \mu \quad \text{(2)}$$

$$3 + \lambda = 4 + 2\mu \quad \text{(3)}$$

From (1):

$$2\lambda - \mu = 2 \quad \text{(4)}$$

From (2):

$$\lambda + \mu = 1 \quad \text{(5)}$$

Add (4) and (5):

$$3\lambda = 3 \implies \lambda = 1$$

Then from (5):

$$\mu = 0$$

Check in (3):

$$\text{LHS} = 3 + 1 = 4, \qquad \text{RHS} = 4 + 2(0) = 4 \quad\checkmark$$

Substitute $\lambda = 1$ into $\ell_1$:

$$\mathbf{r} = \begin{pmatrix} 1 + 2 \\ 2 - 1 \\ 3 + 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \\ 4 \end{pmatrix}$$

The point of intersection is $(3, 1, 4)$. $\checkmark$

**What the examiner wants:** two equations solved, then an explicit check in the third. The check is worth a mark and catches sign errors.

### Example 18 - Medium - Proving two lines are skew

> **Question:** Show that the lines
> $$\ell_1: \mathbf{r} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + \lambda\begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix}, \qquad \ell_2: \mathbf{r} = \begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix} + \mu\begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}$$
> are skew.

**Solution:**

First check the directions:

$$\begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix} \neq k\begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}$$

for any $k$ (the ratios $1/2$, $-1/1$, $2/(-1)$ are not equal), so the lines are not parallel.

Now test for intersection:

$$1 + \lambda = 2 + 2\mu \quad \text{(1)}$$

$$2 - \lambda = 3 + \mu \quad \text{(2)}$$

$$3 + 2\lambda = 1 - \mu \quad \text{(3)}$$

From (1):

$$\lambda - 2\mu = 1 \quad \text{(4)}$$

From (2):

$$\lambda + \mu = -1 \quad \text{(5)}$$

Subtract (5) from (4):

$$-3\mu = 2 \implies \mu = -\frac{2}{3}$$

Then from (5):

$$\lambda = -1 - \left(-\frac{2}{3}\right) = -\frac{1}{3}$$

Check in (3):

$$\text{LHS} = 3 + 2\left(-\frac{1}{3}\right) = \frac{7}{3}$$

$$\text{RHS} = 1 - \left(-\frac{2}{3}\right) = \frac{5}{3}$$

Since $\frac{7}{3} \neq \frac{5}{3}$, the third equation fails. The lines are not parallel and do not intersect, so they are skew. $\checkmark$

**What the examiner wants:** the two-stage argument: not parallel, then a failed consistency check. Writing "they are skew" without showing both is worth fewer marks.

### Example 19 - Medium - Parallel but distinct

> **Question:** Show that the lines
> $$\ell_1: \mathbf{r} = \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} + \lambda\begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}, \qquad \ell_2: \mathbf{r} = \begin{pmatrix} 0 \\ 1 \\ 5 \end{pmatrix} + \mu\begin{pmatrix} -4 \\ 2 \\ -6 \end{pmatrix}$$
> are parallel and distinct.

**Solution:**

Compare directions:

$$\begin{pmatrix} -4 \\ 2 \\ -6 \end{pmatrix} = -2\begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}$$

so the lines are parallel (or identical).

Test whether the point $(0, 1, 5)$ on $\ell_2$ lies on $\ell_1$:

$$1 + 2\lambda = 0 \implies \lambda = -\frac{1}{2}$$

$$0 - \lambda = 1 \implies \lambda = -1$$

These values disagree, so $(0, 1, 5)$ is not on $\ell_1$. The lines are parallel and distinct. $\checkmark$

**What the examiner wants:** the direction comparison first, then a single point test. You do not need to run the full three-equation intersection algorithm when the directions are already parallel.

### Example 20 - Medium - Angle between two lines

> **Question:** Find the acute angle between the lines with direction vectors
> $$\mathbf{b}_1 = \mathbf{i} + 2\mathbf{j} - 2\mathbf{k}, \qquad \mathbf{b}_2 = 3\mathbf{i} + 4\mathbf{k}$$

**Solution:**

Dot product:

$$\mathbf{b}_1 \cdot \mathbf{b}_2 = (1)(3) + (2)(0) + (-2)(4) = 3 + 0 - 8 = -5$$

Magnitudes:

$$|\mathbf{b}_1| = \sqrt{1 + 4 + 4} = 3, \qquad |\mathbf{b}_2| = \sqrt{9 + 0 + 16} = 5$$

Acute-angle cosine:

$$\cos\theta = \frac{|-5|}{(3)(5)} = \frac{5}{15} = \frac{1}{3}$$

$$\theta = \cos^{-1}\left(\frac{1}{3}\right) \approx 70.5^\circ \quad\checkmark$$

Without the absolute value, $\cos^{-1}(-1/3) \approx 109.5^\circ$, which is the obtuse angle between the chosen direction vectors. The angle between the lines is the acute one.

**What the examiner wants:** the absolute value and the phrase "acute angle". State the angle, not just the cosine.

### Example 21 - Medium - Intersection with a clean parameter

> **Question:** Find the point of intersection of
> $$\ell_1: \mathbf{r} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + \lambda\begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix}, \qquad \ell_2: \mathbf{r} = \begin{pmatrix} 2 \\ 1 \\ 5 \end{pmatrix} + \mu\begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}$$

**Solution:**

Equate components:

$$1 + \lambda = 2 + 2\mu \quad \text{(1)}$$

$$2 - \lambda = 1 + \mu \quad \text{(2)}$$

$$3 + 2\lambda = 5 - \mu \quad \text{(3)}$$

From (1):

$$\lambda - 2\mu = 1 \quad \text{(4)}$$

From (2):

$$\lambda + \mu = 1 \quad \text{(5)}$$

Subtract (5) from (4):

$$-3\mu = 0 \implies \mu = 0$$

Then from (5):

$$\lambda = 1$$

Check in (3):

$$\text{LHS} = 3 + 2 = 5, \qquad \text{RHS} = 5 - 0 = 5 \quad\checkmark$$

Substitute $\lambda = 1$ into $\ell_1$:

$$\mathbf{r} = \begin{pmatrix} 1 + 1 \\ 2 - 1 \\ 3 + 2 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ 5 \end{pmatrix}$$

The point of intersection is $(2, 1, 5)$. $\checkmark$

### Example 22 - Hard - Relationship and angle in one question

> **Question:** The lines
> $$\ell_1: \mathbf{r} = \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} + \lambda\begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}, \qquad \ell_2: \mathbf{r} = \begin{pmatrix} 3 \\ 1 \\ 1 \end{pmatrix} + \mu\begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix}$$
> (a) Determine whether the lines are parallel, intersecting or skew. (b) If they intersect, find the point of intersection and the acute angle between the lines.

**Solution:**

Part (a) - directions:

$$\begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix} \neq k\begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix}$$

so the lines are not parallel. Equate components:

$$1 + 2\lambda = 3 + \mu \quad \text{(1)}$$

$$\lambda = 1 - \mu \quad \text{(2)}$$

$$2 - \lambda = 1 + 2\mu \quad \text{(3)}$$

From (1):

$$2\lambda - \mu = 2 \quad \text{(4)}$$

From (2):

$$\lambda + \mu = 1 \quad \text{(5)}$$

Add (4) and (5):

$$3\lambda = 3 \implies \lambda = 1$$

Then from (5):

$$\mu = 0$$

Check in (3):

$$\text{LHS} = 2 - 1 = 1, \qquad \text{RHS} = 1 + 0 = 1 \quad\checkmark$$

The lines intersect at

$$\mathbf{r} = \begin{pmatrix} 1 + 2 \\ 0 + 1 \\ 2 - 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \\ 1 \end{pmatrix}$$

Part (b) - angle between the direction vectors:

$$\mathbf{b}_1 \cdot \mathbf{b}_2 = (2)(1) + (1)(-1) + (-1)(2) = 2 - 1 - 2 = -1$$

$$|\mathbf{b}_1| = \sqrt{4 + 1 + 1} = \sqrt{6}, \qquad |\mathbf{b}_2| = \sqrt{1 + 1 + 4} = \sqrt{6}$$

$$\cos\theta = \frac{|-1|}{6} = \frac{1}{6}$$

$$\theta = \cos^{-1}\left(\frac{1}{6}\right) \approx 80.4^\circ \quad\checkmark$$

**What the examiner wants:** the full three-stage argument in part (a), then the acute-angle formula with the absolute value in part (b).

### Practice Questions - Part 4

1. (Medium) Determine whether the lines $\ell_1: \mathbf{r} = \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} + \lambda\begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}$ and $\ell_2: \mathbf{r} = \begin{pmatrix} 1 \\ 3 \\ 2 \end{pmatrix} + \mu\begin{pmatrix} 2 \\ 1 \\ 1 \end{pmatrix}$ intersect, are parallel, or are skew.
2. (Medium) Determine whether the lines $\ell_1: \mathbf{r} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} + \lambda\begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}$ and $\ell_2: \mathbf{r} = \begin{pmatrix} 4 \\ 0 \\ 7 \end{pmatrix} + \mu\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$ intersect, are parallel, or are skew.
3. (Medium) Find the point of intersection of $\ell_1: \mathbf{r} = \begin{pmatrix} 0 \\ 1 \\ 2 \end{pmatrix} + \lambda\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$ and $\ell_2: \mathbf{r} = \begin{pmatrix} 2 \\ 3 \\ 4 \end{pmatrix} + \mu\begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix}$.
4. (Medium) Show that $\ell_1: \mathbf{r} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + \lambda\begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix}$ and $\ell_2: \mathbf{r} = \begin{pmatrix} 2 \\ 1 \\ 5 \end{pmatrix} + \mu\begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}$ intersect, and find the acute angle between them.
5. (Medium) Show that $\ell_1: \mathbf{r} = \lambda\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$ and $\ell_2: \mathbf{r} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} + \mu\begin{pmatrix} 2 \\ 4 \\ 6 \end{pmatrix}$ are parallel and distinct.
6. (Hard) Determine whether $\ell_1: \mathbf{r} = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} + \lambda\begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix}$ and $\ell_2: \mathbf{r} = \begin{pmatrix} 0 \\ 2 \\ 3 \end{pmatrix} + \mu\begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix}$ intersect. If they do, find the point; if not, state whether they are parallel or skew.

**Solutions:**

Question 1 - equate components:

$$2 + \lambda = 1 + 2\mu \quad \text{(1)}$$

$$1 + 2\lambda = 3 + \mu \quad \text{(2)}$$

$$-\lambda = 2 + \mu \quad \text{(3)}$$

From (1):

$$\lambda - 2\mu = -1 \quad \text{(4)}$$

From (2):

$$2\lambda - \mu = 2 \quad \text{(5)}$$

From (4), $\lambda = 2\mu - 1$. Substitute into (5):

$$2(2\mu - 1) - \mu = 2 \implies 4\mu - 2 - \mu = 2 \implies 3\mu = 4 \implies \mu = \frac{4}{3}$$

Then

$$\lambda = 2\left(\frac{4}{3}\right) - 1 = \frac{5}{3}$$

Check in (3):

$$\text{LHS} = -\frac{5}{3}, \qquad \text{RHS} = 2 + \frac{4}{3} = \frac{10}{3}$$

Not equal, so the lines are skew.

Question 2 - directions are not parallel. Equate:

$$1 + 2\lambda = 4 + \mu \quad \text{(1)}$$

$$1 - \lambda = \mu \quad \text{(2)}$$

$$1 + 3\lambda = 7 + \mu \quad \text{(3)}$$

From (1):

$$2\lambda - \mu = 3 \quad \text{(4)}$$

From (2):

$$\lambda + \mu = 1 \quad \text{(5)}$$

Adding:

$$3\lambda = 4 \implies \lambda = \frac{4}{3}, \qquad \mu = -\frac{1}{3}$$

Check in (3):

$$\text{LHS} = 1 + 4 = 5, \qquad \text{RHS} = 7 - \frac{1}{3} = \frac{20}{3}$$

Not equal, so the lines are skew.

Question 3 - equate:

$$\lambda = 2 + 2\mu \quad \text{(1)}$$

$$1 + \lambda = 3 + \mu \quad \text{(2)}$$

$$2 + \lambda = 4 \quad \text{(3)}$$

From (3):

$$\lambda = 2$$

Then from (1):

$$2 = 2 + 2\mu \implies \mu = 0$$

Check in (2):

$$\text{LHS} = 1 + 2 = 3, \qquad \text{RHS} = 3 + 0 = 3 \quad\checkmark$$

The point of intersection is

$$\mathbf{r} = \begin{pmatrix} 0 + 2 \\ 1 + 2 \\ 2 + 2 \end{pmatrix} = \begin{pmatrix} 2 \\ 3 \\ 4 \end{pmatrix}$$

Question 4 - this is Example 21; the point is $(2, 1, 5)$ and the angle is

$$\cos\theta = \frac{|(1)(2) + (-1)(1) + (2)(-1)|}{\sqrt{6}\sqrt{6}} = \frac{|2 - 1 - 2|}{6} = \frac{1}{6}$$

$$\theta \approx 80.4^\circ$$

Question 5 - direction of $\ell_2$ is $\begin{pmatrix} 2 \\ 4 \\ 6 \end{pmatrix} = 2\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$, so the lines are parallel. Test the point $(1, 1, 1)$ on $\ell_1$:

$$\lambda = 1, \quad 2\lambda = 1 \implies \lambda = \frac{1}{2}$$

These disagree, so the point is not on $\ell_1$. The lines are distinct.

Question 6 - directions are not parallel. Equate:

$$1 + 2\lambda = \mu \quad \text{(1)}$$

$$-\lambda = 2 + \mu \quad \text{(2)}$$

$$1 + \lambda = 3 - \mu \quad \text{(3)}$$

From (1), $\mu = 1 + 2\lambda$. Substitute into (2):

$$-\lambda = 2 + 1 + 2\lambda \implies -3\lambda = 3 \implies \lambda = -1$$

Then

$$\mu = 1 - 2 = -1$$

Check in (3):

$$\text{LHS} = 1 - 1 = 0, \qquad \text{RHS} = 3 - (-1) = 4$$

Not equal, so the lines are skew.

---

# PART 5: Angles, Areas and the Foot of the Perpendicular

## 5.1 The Area of a Triangle from Two Vectors

If a triangle has two sides represented by vectors $\mathbf{a}$ and $\mathbf{b}$ meeting at a vertex, then

$$\text{Area} = \frac{1}{2}|\mathbf{a}|\,|\mathbf{b}|\sin\theta$$

where $\theta$ is the angle between $\mathbf{a}$ and $\mathbf{b}$. Since $\cos\theta$ comes from the dot product,

$$\sin\theta = \sqrt{1 - \cos^2\theta}$$

This is the standard 9709 route: find $\cos\theta$ with the scalar product, convert to $\sin\theta$, then use $\frac{1}{2}ab\sin C$. The vector product is **not** required.

If the triangle is right-angled, skip the trigonometry and use $\frac{1}{2}\times\text{base}\times\text{height}$ directly.

## 5.2 The Foot of the Perpendicular from a Point to a Line

Given a point $P$ and a line $\ell: \mathbf{r} = \mathbf{a} + \lambda\mathbf{d}$, the foot $F$ is the point on $\ell$ such that $PF$ is perpendicular to the line.

**Method:**

1. Write $F$ as a general point on the line:
   $$\vec{OF} = \mathbf{a} + \lambda\mathbf{d}$$
2. Form the vector $\vec{PF} = \vec{OF} - \vec{OP}$ (or $\vec{FP} = \vec{OP} - \vec{OF}$; either sign works).
3. Impose perpendicularity:
   $$\vec{PF} \cdot \mathbf{d} = 0$$
4. Solve for $\lambda$, then find $F$.
5. The perpendicular distance is $|\vec{PF}|$.

> ⭐ **Watch Out!** The condition is $(\vec{OF} - \vec{OP}) \cdot \mathbf{d} = 0$, **not** $\vec{OF} \cdot \mathbf{d} = 0$. The second condition would put $F$ at the point where $OF$ is perpendicular to the line, which is not generally the foot from $P$.

## 5.3 Angles in 3D Objects

The same tools handle cuboids, tetrahedra and other solids:

- Write down the coordinates of the relevant vertices.
- Form the two vectors that meet at the angle you need.
- Use the scalar product.
- For an area, use $\frac{1}{2}ab\sin\theta$ or split the shape into right-angled triangles.

### Example 23 - Medium - Area of a triangle using the scalar product

> **Question:** The points $A(1, 4, 2)$, $B(2, 1, 3)$ and $C(2, 3, 5)$ are given. Find the exact area of triangle $ABC$.

**Solution:**

From Example 7:

$$\vec{AB} = \begin{pmatrix} 1 \\ -3 \\ 1 \end{pmatrix}, \qquad \vec{AC} = \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}$$

$$|\vec{AB}| = |\vec{AC}| = \sqrt{11}, \qquad \cos\angle BAC = \frac{7}{11}$$

Find $\sin\angle BAC$:

$$\sin^2\angle BAC = 1 - \left(\frac{7}{11}\right)^2 = 1 - \frac{49}{121} = \frac{72}{121}$$

$$\sin\angle BAC = \frac{\sqrt{72}}{11} = \frac{6\sqrt{2}}{11}$$

Area:

$$\text{Area} = \frac{1}{2}|\vec{AB}|\,|\vec{AC}|\sin\angle BAC$$

$$\text{Area} = \frac{1}{2}(\sqrt{11})(\sqrt{11})\left(\frac{6\sqrt{2}}{11}\right)$$

$$\text{Area} = \frac{1}{2}(11)\left(\frac{6\sqrt{2}}{11}\right) = 3\sqrt{2} \quad\checkmark$$

**What the examiner wants:** the exact value, not a decimal. Keep the surds until the final cancellation.

### Example 24 - Medium - Foot of the perpendicular

> **Question:** Find the foot of the perpendicular from $P(1, 1, 1)$ to the line
> $$\ell: \mathbf{r} = \begin{pmatrix} 2 \\ 0 \\ 3 \end{pmatrix} + \lambda\begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}$$
> and hence find the perpendicular distance from $P$ to $\ell$.

**Solution:**

A general point on the line is

$$F(2 + \lambda, \; 2\lambda, \; 3 - \lambda)$$

Then

$$\vec{PF} = \vec{OF} - \vec{OP} = \begin{pmatrix} 2 + \lambda - 1 \\ 2\lambda - 1 \\ 3 - \lambda - 1 \end{pmatrix} = \begin{pmatrix} 1 + \lambda \\ 2\lambda - 1 \\ 2 - \lambda \end{pmatrix}$$

The direction vector is $\mathbf{d} = \begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}$. Perpendicularity:

$$\vec{PF} \cdot \mathbf{d} = 0$$

$$(1 + \lambda)(1) + (2\lambda - 1)(2) + (2 - \lambda)(-1) = 0$$

$$1 + \lambda + 4\lambda - 2 - 2 + \lambda = 0$$

$$6\lambda - 3 = 0$$

$$\lambda = \frac{1}{2}$$

So

$$F = \left(2 + \frac{1}{2}, \; 1, \; 3 - \frac{1}{2}\right) = \left(\frac{5}{2}, 1, \frac{5}{2}\right) \quad\checkmark$$

Distance:

$$\vec{PF} = \begin{pmatrix} 3/2 \\ 0 \\ 3/2 \end{pmatrix}$$

$$|\vec{PF}| = \sqrt{\left(\frac{3}{2}\right)^2 + 0^2 + \left(\frac{3}{2}\right)^2} = \sqrt{\frac{9}{4} + \frac{9}{4}} = \sqrt{\frac{18}{4}} = \frac{3\sqrt{2}}{2} \quad\checkmark$$

**What the examiner wants:** the general point, the vector $\vec{PF}$, the zero dot product, and then the distance. The foot and the distance are two separate answers; make sure both are stated.

### Example 25 - Medium - Distance from a point to a line

> **Question:** Find the perpendicular distance from $P(1, 2, 3)$ to the line
> $$\ell: \mathbf{r} = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} + \lambda\begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix}$$

**Solution:**

A general point on the line is

$$F(\lambda, \; 1 - \lambda, \; 1 + 2\lambda)$$

Then

$$\vec{PF} = \begin{pmatrix} \lambda - 1 \\ -1 - \lambda \\ -2 + 2\lambda \end{pmatrix}$$

Direction vector:

$$\mathbf{d} = \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix}$$

Perpendicularity:

$$(\lambda - 1)(1) + (-1 - \lambda)(-1) + (-2 + 2\lambda)(2) = 0$$

$$\lambda - 1 + 1 + \lambda - 4 + 4\lambda = 0$$

$$6\lambda - 4 = 0$$

$$\lambda = \frac{2}{3}$$

So

$$F = \left(\frac{2}{3}, \; 1 - \frac{2}{3}, \; 1 + \frac{4}{3}\right) = \left(\frac{2}{3}, \frac{1}{3}, \frac{7}{3}\right)$$

Then

$$\vec{PF} = \begin{pmatrix} -1/3 \\ -5/3 \\ -2/3 \end{pmatrix}$$

$$|\vec{PF}| = \frac{1}{3}\sqrt{(-1)^2 + (-5)^2 + (-2)^2} = \frac{\sqrt{30}}{3} \quad\checkmark$$

**What the examiner wants:** clean fraction arithmetic. Multiplying through by $3$ at the end is safer than squaring the fractions immediately.

### Example 26 - Hard - Angle between the diagonals of a cuboid

> **Question:** A cuboid has $O$ at the origin, $OA = 3\mathbf{i}$, $OC = 4\mathbf{j}$ and $OD = 2\mathbf{k}$. The vertices are
> $$O(0,0,0), \; A(3,0,0), \; B(3,4,0), \; C(0,4,0), \; D(0,0,2), \; E(3,0,2), \; F(3,4,2), \; G(0,4,2)$$
> Find the angle between the space diagonals $OF$ and $AG$.

**Solution:**

The diagonal vectors are

$$\vec{OF} = \begin{pmatrix} 3 \\ 4 \\ 2 \end{pmatrix}, \qquad \vec{AG} = \vec{OG} - \vec{OA} = \begin{pmatrix} 0 - 3 \\ 4 - 0 \\ 2 - 0 \end{pmatrix} = \begin{pmatrix} -3 \\ 4 \\ 2 \end{pmatrix}$$

Dot product:

$$\vec{OF} \cdot \vec{AG} = (3)(-3) + (4)(4) + (2)(2) = -9 + 16 + 4 = 11$$

Magnitudes:

$$|\vec{OF}| = \sqrt{9 + 16 + 4} = \sqrt{29}, \qquad |\vec{AG}| = \sqrt{9 + 16 + 4} = \sqrt{29}$$

Cosine:

$$\cos\theta = \frac{11}{\sqrt{29}\sqrt{29}} = \frac{11}{29}$$

$$\theta = \cos^{-1}\left(\frac{11}{29}\right) \approx 67.7^\circ \quad\checkmark$$

**What the examiner wants:** coordinates read correctly from the cuboid, then the two diagonal vectors formed by subtracting position vectors. Drawing a quick sketch prevents mixing up $F$ and $G$.

### Example 27 - Hard - Diagonals of a parallelogram bisect each other

> **Question:** $OABC$ is a parallelogram with $\vec{OA} = \mathbf{a}$ and $\vec{OC} = \mathbf{c}$. Prove that the diagonals $OB$ and $AC$ bisect each other.

**Solution:**

The diagonals are

$$\vec{OB} = \mathbf{a} + \mathbf{c}, \qquad \vec{AC} = \mathbf{c} - \mathbf{a}$$

The midpoint of $OB$ has position vector

$$\frac{\mathbf{a} + \mathbf{c}}{2}$$

The midpoint of $AC$ is the average of the position vectors of $A$ and $C$:

$$\frac{\mathbf{a} + \mathbf{c}}{2}$$

The two midpoints are the same point, so the diagonals bisect each other. $\checkmark$

**What the examiner wants:** the midpoint formula applied to both diagonals and the explicit observation that the results are identical.

### Example 28 - Hard - A regular tetrahedron

> **Question:** The vertices of a regular tetrahedron are
> $$A(1,1,1), \; B(1,-1,-1), \; C(-1,1,-1), \; D(-1,-1,1)$$
> (a) Show that the angle between $AB$ and $AC$ is $60^\circ$. (b) Show that the opposite edges $AB$ and $CD$ are perpendicular.

**Solution:**

Part (a):

$$\vec{AB} = \begin{pmatrix} 0 \\ -2 \\ -2 \end{pmatrix}, \qquad \vec{AC} = \begin{pmatrix} -2 \\ 0 \\ -2 \end{pmatrix}$$

Dot product:

$$\vec{AB} \cdot \vec{AC} = 0 + 0 + 4 = 4$$

Magnitudes:

$$|\vec{AB}| = \sqrt{0 + 4 + 4} = 2\sqrt{2}, \qquad |\vec{AC}| = \sqrt{4 + 0 + 4} = 2\sqrt{2}$$

Cosine:

$$\cos\angle BAC = \frac{4}{(2\sqrt{2})(2\sqrt{2})} = \frac{4}{8} = \frac{1}{2}$$

$$\angle BAC = 60^\circ \quad\checkmark$$

Part (b):

$$\vec{CD} = \vec{OD} - \vec{OC} = \begin{pmatrix} 0 \\ -2 \\ 2 \end{pmatrix}$$

Then

$$\vec{AB} \cdot \vec{CD} = (0)(0) + (-2)(-2) + (-2)(2) = 4 - 4 = 0$$

So $AB$ and $CD$ are perpendicular. $\checkmark$

**What the examiner wants:** the exact $60^\circ$ from $\cos^{-1}(1/2)$, and the zero dot product for the opposite edges. This is a classic "3D object" exam question.

### Practice Questions - Part 5

1. (Medium) Find the exact area of the triangle with vertices $P(2, 1, 0)$, $Q(3, 4, 2)$ and $R(1, 0, 3)$.
2. (Medium) Find the foot of the perpendicular from $P(1, 2, 3)$ to the line $\mathbf{r} = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} + \lambda\begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix}$, and hence the perpendicular distance.
3. (Medium) Find the perpendicular distance from the origin to the line $\mathbf{r} = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix} + \lambda\begin{pmatrix} 2 \\ -1 \\ 2 \end{pmatrix}$.
4. (Medium) A cuboid has sides $2$, $3$ and $6$. Find the length of its space diagonal and the angle it makes with the base.
5. (Medium) For $\mathbf{a} = \mathbf{i} + 2\mathbf{j} + 2\mathbf{k}$ and $\mathbf{b} = 3\mathbf{i} + 4\mathbf{k}$, find the area of the triangle with sides $\mathbf{a}$ and $\mathbf{b}$.
6. (Hard) Find the foot of the perpendicular from $P(3, 1, 2)$ to the line through $A(1, 0, 0)$ with direction $\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$, and hence the distance from $P$ to the line.

**Solutions:**

Question 1:

$$\vec{PQ} = \begin{pmatrix} 1 \\ 3 \\ 2 \end{pmatrix}, \qquad \vec{PR} = \begin{pmatrix} -1 \\ -1 \\ 3 \end{pmatrix}$$

$$\vec{PQ} \cdot \vec{PR} = (1)(-1) + (3)(-1) + (2)(3) = -1 - 3 + 6 = 2$$

$$|\vec{PQ}| = \sqrt{1 + 9 + 4} = \sqrt{14}, \qquad |\vec{PR}| = \sqrt{1 + 1 + 9} = \sqrt{11}$$

$$\cos\theta = \frac{2}{\sqrt{154}}$$

$$\sin\theta = \sqrt{1 - \frac{4}{154}} = \sqrt{\frac{150}{154}} = \sqrt{\frac{75}{77}}$$

$$\text{Area} = \frac{1}{2}\sqrt{154}\sqrt{\frac{75}{77}} = \frac{1}{2}\sqrt{150} = \frac{5\sqrt{6}}{2}$$

Question 2:

$$F(2\lambda, 1 - \lambda, \lambda)$$

$$\vec{PF} = \begin{pmatrix} 2\lambda - 1 \\ -1 - \lambda \\ \lambda - 3 \end{pmatrix}$$

$$\vec{PF} \cdot \begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix} = 0$$

$$2(2\lambda - 1) - (-1 - \lambda) + (\lambda - 3) = 0$$

$$4\lambda - 2 + 1 + \lambda + \lambda - 3 = 0$$

$$6\lambda - 4 = 0 \implies \lambda = \frac{2}{3}$$

$$F = \left(\frac{4}{3}, \frac{1}{3}, \frac{2}{3}\right)$$

$$\vec{PF} = \begin{pmatrix} 1/3 \\ -5/3 \\ -7/3 \end{pmatrix}$$

$$|\vec{PF}| = \frac{1}{3}\sqrt{1 + 25 + 49} = \frac{\sqrt{75}}{3} = \frac{5\sqrt{3}}{3}$$

Question 3:

$$F(1 + 2\lambda, 2 - \lambda, 2 + 2\lambda)$$

$$\vec{OF} \cdot \begin{pmatrix} 2 \\ -1 \\ 2 \end{pmatrix} = 0$$

$$2(1 + 2\lambda) - (2 - \lambda) + 2(2 + 2\lambda) = 0$$

$$2 + 4\lambda - 2 + \lambda + 4 + 4\lambda = 0$$

$$9\lambda + 4 = 0 \implies \lambda = -\frac{4}{9}$$

$$F = \left(\frac{1}{9}, \frac{22}{9}, \frac{10}{9}\right)$$

$$|\vec{OF}| = \frac{1}{9}\sqrt{1 + 484 + 100} = \frac{\sqrt{585}}{9} = \frac{3\sqrt{65}}{9} = \frac{\sqrt{65}}{3}$$

Question 4:

The space diagonal is

$$\sqrt{2^2 + 3^2 + 6^2} = \sqrt{4 + 9 + 36} = \sqrt{49} = 7$$

The base diagonal is

$$\sqrt{2^2 + 3^2} = \sqrt{13}$$

If $\phi$ is the angle between the space diagonal and the base, then

$$\cos\phi = \frac{\sqrt{13}}{7}$$

$$\phi = \cos^{-1}\left(\frac{\sqrt{13}}{7}\right) \approx 59.0^\circ$$

Question 5:

$$\mathbf{a} \cdot \mathbf{b} = (1)(3) + (2)(0) + (2)(4) = 3 + 0 + 8 = 11$$

$$|\mathbf{a}| = 3, \qquad |\mathbf{b}| = 5$$

$$\cos\theta = \frac{11}{15}, \qquad \sin\theta = \sqrt{1 - \frac{121}{225}} = \frac{\sqrt{104}}{15} = \frac{2\sqrt{26}}{15}$$

$$\text{Area} = \frac{1}{2}(3)(5)\left(\frac{2\sqrt{26}}{15}\right) = \sqrt{26}$$

Question 6:

$$F(1 + \lambda, \lambda, 0)$$

$$\vec{PF} = \begin{pmatrix} \lambda - 2 \\ \lambda - 1 \\ -2 \end{pmatrix}$$

$$\vec{PF} \cdot \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} = 0$$

$$(\lambda - 2) + (\lambda - 1) = 0 \implies 2\lambda - 3 = 0 \implies \lambda = \frac{3}{2}$$

$$F = \left(\frac{5}{2}, \frac{3}{2}, 0\right)$$

$$\vec{PF} = \begin{pmatrix} -1/2 \\ 1/2 \\ -2 \end{pmatrix}$$

$$|\vec{PF}| = \sqrt{\frac{1}{4} + \frac{1}{4} + 4} = \sqrt{\frac{18}{4}} = \frac{3\sqrt{2}}{2}$$

---

# PART 6: Full Exam-Style Questions

These questions combine several skills, just like a Paper 3 vector question. Attempt them with the solutions covered, then check your working line by line.

## Exam-Style Question 1 - Line, angle and area

> **Question:** With respect to the origin $O$, the points $A$, $B$ and $C$ have position vectors
> $$\vec{OA} = \begin{pmatrix} 1 \\ 4 \\ 2 \end{pmatrix}, \qquad \vec{OB} = \begin{pmatrix} 2 \\ 1 \\ 3 \end{pmatrix}, \qquad \vec{OC} = \begin{pmatrix} 2 \\ 3 \\ 5 \end{pmatrix}$$
> (a) Find a vector equation for the line through $A$ and $B$. [2]
> (b) Using a scalar product, find the exact value of $\cos\angle BAC$. [4]
> (c) Hence find the exact area of triangle $ABC$. [3]

**Solution:**

Part (a):

$$\vec{AB} = \vec{OB} - \vec{OA} = \begin{pmatrix} 1 \\ -3 \\ 1 \end{pmatrix}$$

$$\mathbf{r} = \begin{pmatrix} 1 \\ 4 \\ 2 \end{pmatrix} + \lambda\begin{pmatrix} 1 \\ -3 \\ 1 \end{pmatrix} \quad\checkmark$$

Part (b) - both vectors from $A$:

$$\vec{AB} = \begin{pmatrix} 1 \\ -3 \\ 1 \end{pmatrix}, \qquad \vec{AC} = \vec{OC} - \vec{OA} = \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}$$

$$\vec{AB} \cdot \vec{AC} = (1)(1) + (-3)(-1) + (1)(3) = 1 + 3 + 3 = 7$$

$$|\vec{AB}| = \sqrt{1 + 9 + 1} = \sqrt{11}, \qquad |\vec{AC}| = \sqrt{1 + 1 + 9} = \sqrt{11}$$

$$\cos\angle BAC = \frac{7}{\sqrt{11}\sqrt{11}} = \frac{7}{11} \quad\checkmark$$

Part (c):

$$\sin^2\angle BAC = 1 - \left(\frac{7}{11}\right)^2 = \frac{72}{121}$$

$$\sin\angle BAC = \frac{6\sqrt{2}}{11}$$

$$\text{Area} = \frac{1}{2}(\sqrt{11})(\sqrt{11})\left(\frac{6\sqrt{2}}{11}\right) = 3\sqrt{2} \quad\checkmark$$

**Examiner notes:** part (a) is two marks: one for a correct point, one for a correct direction. In part (b), use $\vec{AB}$ and $\vec{AC}$, not $\vec{BA}$ and $\vec{CA}$. In part (c), keep the exact surd throughout; a decimal loses the "exact" mark.

## Exam-Style Question 2 - Intersection and perpendicular distance

> **Question:** The lines $\ell_1$ and $\ell_2$ are
> $$\ell_1: \mathbf{r} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + \lambda\begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix}, \qquad \ell_2: \mathbf{r} = \begin{pmatrix} 2 \\ 1 \\ 5 \end{pmatrix} + \mu\begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}$$
> (a) Show that $\ell_1$ and $\ell_2$ intersect, and find the point of intersection. [4]
> (b) Find the acute angle between $\ell_1$ and $\ell_2$. [3]
> (c) Find the foot of the perpendicular from $P(0, 0, 1)$ to $\ell_1$, and hence find the perpendicular distance from $P$ to $\ell_1$. [5]

**Solution:**

Part (a) - equate components:

$$1 + \lambda = 2 + 2\mu \quad \text{(1)}$$

$$2 - \lambda = 1 + \mu \quad \text{(2)}$$

$$3 + 2\lambda = 5 - \mu \quad \text{(3)}$$

From (1):

$$\lambda - 2\mu = 1 \quad \text{(4)}$$

From (2):

$$\lambda + \mu = 1 \quad \text{(5)}$$

Subtract (5) from (4):

$$-3\mu = 0 \implies \mu = 0$$

Then from (5), $\lambda = 1$. Check in (3):

$$\text{LHS} = 3 + 2 = 5, \qquad \text{RHS} = 5 - 0 = 5 \quad\checkmark$$

The point of intersection is

$$\mathbf{r} = \begin{pmatrix} 1 + 1 \\ 2 - 1 \\ 3 + 2 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ 5 \end{pmatrix} \quad\checkmark$$

Part (b):

$$\mathbf{d}_1 \cdot \mathbf{d}_2 = (1)(2) + (-1)(1) + (2)(-1) = 2 - 1 - 2 = -1$$

$$|\mathbf{d}_1| = \sqrt{1 + 1 + 4} = \sqrt{6}, \qquad |\mathbf{d}_2| = \sqrt{4 + 1 + 1} = \sqrt{6}$$

$$\cos\theta = \frac{|-1|}{6} = \frac{1}{6}$$

$$\theta = \cos^{-1}\left(\frac{1}{6}\right) \approx 80.4^\circ \quad\checkmark$$

Part (c) - a general point on $\ell_1$ is

$$F(1 + \lambda, \; 2 - \lambda, \; 3 + 2\lambda)$$

Then

$$\vec{PF} = \begin{pmatrix} 1 + \lambda \\ 2 - \lambda \\ 2 + 2\lambda \end{pmatrix}$$

Perpendicularity with $\mathbf{d}_1 = \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix}$:

$$(1 + \lambda)(1) + (2 - \lambda)(-1) + (2 + 2\lambda)(2) = 0$$

$$1 + \lambda - 2 + \lambda + 4 + 4\lambda = 0$$

$$6\lambda + 3 = 0 \implies \lambda = -\frac{1}{2}$$

So

$$F = \left(\frac{1}{2}, \frac{5}{2}, 2\right) \quad\checkmark$$

Distance:

$$\vec{PF} = \begin{pmatrix} 1/2 \\ 5/2 \\ 1 \end{pmatrix}$$

$$|\vec{PF}| = \sqrt{\frac{1}{4} + \frac{25}{4} + 1} = \sqrt{\frac{26}{4} + \frac{4}{4}} = \sqrt{\frac{30}{4}} = \frac{\sqrt{30}}{2} \quad\checkmark$$

**Examiner notes:** part (a) needs the third-equation check. Part (b) needs the absolute value. Part (c) needs the general point and the zero dot product; the distance is the length of $\vec{PF}$, not the parameter value.

## Exam-Style Question 3 - Skew lines and angle

> **Question:** The lines $\ell_1$ and $\ell_2$ are
> $$\ell_1: \mathbf{r} = \begin{pmatrix} 1 \\ 1 \\ 2 \end{pmatrix} + \lambda\begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix}, \qquad \ell_2: \mathbf{r} = \begin{pmatrix} 3 \\ 2 \\ 0 \end{pmatrix} + \mu\begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}$$
> (a) Show that $\ell_1$ and $\ell_2$ are skew. [5]
> (b) Find the acute angle between the directions of the two lines. [3]

**Solution:**

Part (a) - directions:

$$\begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix} \neq k\begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}$$

for any $k$ (the ratios $2/1$, $-1/2$, $1/2$ are not all equal), so the lines are not parallel.

Equate components:

$$1 + 2\lambda = 3 + \mu \quad \text{(1)}$$

$$1 - \lambda = 2 + 2\mu \quad \text{(2)}$$

$$2 + \lambda = 2\mu \quad \text{(3)}$$

From (1):

$$2\lambda - \mu = 2 \implies \mu = 2\lambda - 2$$

Substitute into (2):

$$1 - \lambda = 2 + 2(2\lambda - 2)$$

$$1 - \lambda = 4\lambda - 2$$

$$3 = 5\lambda \implies \lambda = \frac{3}{5}$$

Then

$$\mu = 2\left(\frac{3}{5}\right) - 2 = \frac{6}{5} - \frac{10}{5} = -\frac{4}{5}$$

Check in (3):

$$\text{LHS} = 2 + \frac{3}{5} = \frac{13}{5}$$

$$\text{RHS} = 2\left(-\frac{4}{5}\right) = -\frac{8}{5}$$

Since $\frac{13}{5} \neq -\frac{8}{5}$, the third equation fails. The lines are not parallel and do not intersect, so they are skew. $\checkmark$

Part (b):

$$\mathbf{d}_1 \cdot \mathbf{d}_2 = (2)(1) + (-1)(2) + (1)(2) = 2 - 2 + 2 = 2$$

$$|\mathbf{d}_1| = \sqrt{4 + 1 + 1} = \sqrt{6}, \qquad |\mathbf{d}_2| = \sqrt{1 + 4 + 4} = 3$$

$$\cos\theta = \frac{|2|}{\sqrt{6}\cdot 3} = \frac{2}{3\sqrt{6}} = \frac{\sqrt{6}}{9}$$

$$\theta = \cos^{-1}\left(\frac{\sqrt{6}}{9}\right) \approx 74.2^\circ \quad\checkmark$$

**Examiner notes:** always test the third component before declaring skew. The two-stage argument (not parallel, then inconsistent third component) is what earns full marks. For the angle, take the absolute value of the dot product because the direction vectors can be reversed without changing the lines.

---

# Formula Sheet

**Vector basics:**

$$|\mathbf{a}| = \sqrt{a_1^2 + a_2^2 + a_3^2}$$

$$\hat{\mathbf{a}} = \frac{\mathbf{a}}{|\mathbf{a}|}$$

$$\vec{AB} = \vec{OB} - \vec{OA} = \mathbf{b} - \mathbf{a}$$

$$\vec{OM}_{\text{midpoint of }AB} = \frac{\mathbf{a} + \mathbf{b}}{2}$$

$$\mathbf{b} \parallel \mathbf{a} \iff \mathbf{b} = k\mathbf{a} \quad (k \neq 0)$$

**Scalar product:**

$$\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}|\,|\mathbf{b}|\cos\theta = a_1b_1 + a_2b_2 + a_3b_3$$

$$\cos\theta = \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}|\,|\mathbf{b}|}$$

$$\mathbf{a} \perp \mathbf{b} \iff \mathbf{a} \cdot \mathbf{b} = 0$$

$$\mathbf{a} \cdot \mathbf{a} = |\mathbf{a}|^2$$

**Lines:**

$$\mathbf{r} = \mathbf{a} + \lambda\mathbf{b}$$

$$x = a_1 + \lambda b_1, \qquad y = a_2 + \lambda b_2, \qquad z = a_3 + \lambda b_3$$

Line through $A$ and $B$:

$$\mathbf{r} = \vec{OA} + \lambda(\vec{OB} - \vec{OA})$$

**Relationships between two lines:**

| Condition | Relationship |
|---|---|
| $\mathbf{b}_1 = k\mathbf{b}_2$ | parallel (or identical) |
| consistent $\lambda, \mu$ in all three components | intersecting |
| not parallel and one component inconsistent | skew |

**Angle between lines (acute):**

$$\cos\theta = \frac{|\mathbf{b}_1 \cdot \mathbf{b}_2|}{|\mathbf{b}_1|\,|\mathbf{b}_2|}$$

**Area of triangle:**

$$\text{Area} = \frac{1}{2}|\mathbf{a}|\,|\mathbf{b}|\sin\theta, \qquad \sin\theta = \sqrt{1 - \cos^2\theta}$$

**Foot of the perpendicular from $P$ to $\mathbf{r} = \mathbf{a} + \lambda\mathbf{d}$:**

$$F = \mathbf{a} + \lambda\mathbf{d}, \qquad (\vec{OF} - \vec{OP}) \cdot \mathbf{d} = 0$$

$$\text{distance} = |\vec{PF}|$$

**Useful exact values:** $\cos 30^\circ = \frac{\sqrt{3}}{2}$, $\cos 45^\circ = \frac{1}{\sqrt{2}}$, $\cos 60^\circ = \frac{1}{2}$.

---

# Quick Reference Card

- **Displacement:** $\vec{AB} = \mathbf{b} - \mathbf{a}$ (head minus tail). Reversing the order flips the sign.
- **Magnitude:** $|\mathbf{a}| = \sqrt{x^2+y^2+z^2}$. The unit vector is $\mathbf{a}/|\mathbf{a}|$.
- **Midpoint:** $\frac{1}{2}(\mathbf{a}+\mathbf{b})$. The general ratio theorem is not required, but this midpoint case is.
- **Parallel:** $\mathbf{b} = k\mathbf{a}$. For collinearity, parallel is not enough: the vectors must also share a point.
- **Dot product:** $\mathbf{a}\cdot\mathbf{b} = |\mathbf{a}||\mathbf{b}|\cos\theta = a_1b_1+a_2b_2+a_3b_3$.
- **Angle:** $\cos\theta = \frac{\mathbf{a}\cdot\mathbf{b}}{|\mathbf{a}||\mathbf{b}|}$. For the angle between **lines**, use $|\mathbf{a}\cdot\mathbf{b}|$ and give the acute angle.
- **Perpendicular:** $\mathbf{a}\cdot\mathbf{b}=0$. No magnitudes needed.
- **Line:** $\mathbf{r} = \mathbf{a} + \lambda\mathbf{b}$. $\mathbf{a}$ is a point, $\mathbf{b}$ is a direction, $\lambda$ is the parameter. A line through $A$ and $B$ uses $\mathbf{b} = \vec{AB}$.
- **Point on a line:** solve one component for $\lambda$, then check the other **two**. Same $\lambda$ in all three means the point is on the line.
- **Intersection of two lines:** different parameters $\lambda$ and $\mu$; solve two equations, then check the third. Consistent $\to$ intersect; inconsistent $\to$ skew (after ruling out parallel).
- **Parallel lines:** compare direction vectors first. Then test one point to decide same line vs distinct.
- **Skew:** not parallel and no intersection. Show both facts.
- **Angle between lines:** dot product of direction vectors, absolute value, acute angle.
- **Area of triangle:** $\frac{1}{2}ab\sin C$; get $\cos C$ from the dot product, then $\sin C = \sqrt{1-\cos^2 C}$. Right-angled triangles: $\frac{1}{2}\times$ base $\times$ height.
- **Foot of perpendicular:** write $F = \mathbf{a}+\lambda\mathbf{d}$, impose $(\vec{OF}-\vec{OP})\cdot\mathbf{d}=0$, solve for $\lambda$, then distance $=|\vec{PF}|$.
- **Exam habits:** 3D means three components every time; keep exact surds; draw a rough diagram; state the relationship (parallel/intersect/skew) explicitly.

---

*Sources: Cambridge International AS & A Level Mathematics 9709 syllabus (2026-2027), topic 3.7 Vectors; Cambridge Pure Mathematics 2 & 3 coursebook Chapter 9; Cambridge 9709 Paper 3 past papers, including 9709/32/M/J/25 Q9 and 9709/31/M/J/25 Q8. All numerical answers were checked by direct computation.*
