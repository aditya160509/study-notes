# 📘 Chapter 11: Complex Numbers - 9709 Pure Mathematics 3 (CAIE A Level Maths)

## Cambridge International AS & A Level Mathematics (9709) - Paper 3

> **The complete walkthrough:** the imaginary unit, arithmetic in Cartesian form, conjugates and division, the Argand diagram, modulus and argument, polar form, multiplication and division in polar form, powers and square roots, loci and regions, conjugate pairs, and polynomial equations. Every technique is built from fully solved examples, then tested with practice questions and full solutions.

---

# 📋 Table of Contents

1. [PART 1: The Complex Number System](#part-1-the-complex-number-system)
2. [PART 2: Argand Diagram, Modulus and Argument](#part-2-argand-diagram-modulus-and-argument)
3. [PART 3: Polar Form, Multiplication, Division and Roots](#part-3-polar-form-multiplication-division-and-roots)
4. [PART 4: Loci and Regions](#part-4-loci-and-regions)
5. [PART 5: Equations, Roots and Conjugate Pairs](#part-5-equations-roots-and-conjugate-pairs)
6. [PART 6: Full Exam-Style Questions](#part-6-full-exam-style-questions)
7. [Formula Sheet](#formula-sheet)
8. [Quick Reference Card](#quick-reference-card)

---

# PART 1: The Complex Number System

## 1.1 The Imaginary Unit

The equation $x^2 + 1 = 0$ has no real solution because the square of a real number is never negative. We introduce the imaginary unit $i$ with the defining property

$$i^2 = -1$$

A **complex number** is any number of the form

$$z = x + iy$$

where $x$ and $y$ are real. We call

$$\operatorname{Re}(z) = x, \qquad \operatorname{Im}(z) = y$$

The syllabus expects the notation $\operatorname{Re} z$, $\operatorname{Im} z$, $|z|$, $\arg z$ and $z^*$ to be known.

- If $y = 0$, then $z = x$ is **real**.
- If $x = 0$ and $y \neq 0$, then $z = iy$ is **purely imaginary**.
- The number $0 = 0 + 0i$ is real, and its argument is undefined.

**Equality.** Two complex numbers are equal exactly when their real parts and imaginary parts both match:

$$x_1 + iy_1 = x_2 + iy_2 \iff x_1 = x_2 \text{ and } y_1 = y_2$$

This is the single most useful fact for solving equations: one complex equation gives two real equations.

## 1.2 Addition, Subtraction and Multiplication

Addition and subtraction are component by component:

$$(x_1 + iy_1) \pm (x_2 + iy_2) = (x_1 \pm x_2) + i(y_1 \pm y_2)$$

Multiplication uses the ordinary distributive law, then replaces $i^2$ by $-1$:

$$(x_1 + iy_1)(x_2 + iy_2) = x_1x_2 + ix_1y_2 + iy_1x_2 + i^2y_1y_2$$

$$= (x_1x_2 - y_1y_2) + i(x_1y_2 + y_1x_2)$$

Do not memorise the final line; expand every time. It is faster and safer.

## 1.3 The Conjugate and Division

The **complex conjugate** of $z = x + iy$ is

$$z^* = x - iy \qquad \text{(also written } \overline{z}\text{)}$$

Geometrically, conjugation reflects the point in the real axis. Key properties:

$$z + z^* = 2x = 2\operatorname{Re}(z)$$

$$z - z^* = 2iy = 2i\operatorname{Im}(z)$$

$$zz^* = (x + iy)(x - iy) = x^2 + y^2 = |z|^2$$

$$(z^*)^* = z, \qquad (z_1 \pm z_2)^* = z_1^* \pm z_2^*, \qquad (z_1z_2)^* = z_1^*z_2^*$$

To **divide** by a complex number, multiply numerator and denominator by the conjugate of the denominator:

$$\frac{z_1}{z_2} = \frac{z_1 z_2^*}{z_2 z_2^*} = \frac{z_1 z_2^*}{|z_2|^2}$$

The denominator becomes the real number $|z_2|^2$, so the result is automatically in Cartesian form.

> ⭐ **Watch Out!** The conjugate of $z_2$ is $x_2 - iy_2$, not $x_2 + iy_2$. When the denominator is something like $3 + 2i$, multiply by $3 - 2i$; when it is $1 - i$, multiply by $1 + i$. The sign of the imaginary part flips.

## 1.4 Powers of $i$

The powers repeat in a cycle of four:

$$i^1 = i, \qquad i^2 = -1, \qquad i^3 = -i, \qquad i^4 = 1$$

For a large power, divide the exponent by $4$ and use the remainder:

$$i^n = i^{n \bmod 4}$$

For example, $2026 \div 4 = 506$ remainder $2$, so $i^{2026} = i^2 = -1$.

## 1.5 The Reciprocal

A useful special case of division is

$$\frac{1}{z} = \frac{z^*}{zz^*} = \frac{z^*}{|z|^2}$$

For example,

$$\frac{1}{3 + 4i} = \frac{3 - 4i}{25} = \frac{3}{25} - \frac{4}{25}i$$

### Example 1 - Easy - The four basic operations

> **Question:** For $z = 3 + 4i$ and $w = 1 - 2i$, find (a) $z + w$, (b) $z - w$, (c) $zw$, (d) $\dfrac{z}{w}$, (e) $z^*$, (f) $zz^*$.

**Solution:**

Part (a):

$$z + w = (3 + 1) + (4 - 2)i = 4 + 2i \quad\checkmark$$

Part (b):

$$z - w = (3 - 1) + (4 - (-2))i = 2 + 6i \quad\checkmark$$

Part (c):

$$zw = (3 + 4i)(1 - 2i) = 3 - 6i + 4i - 8i^2$$

$$zw = 3 - 2i + 8 = 11 - 2i \quad\checkmark$$

Part (d) - multiply by the conjugate of $1 - 2i$:

$$\frac{z}{w} = \frac{3 + 4i}{1 - 2i} \cdot \frac{1 + 2i}{1 + 2i} = \frac{(3 + 4i)(1 + 2i)}{1^2 + 2^2}$$

$$= \frac{3 + 6i + 4i + 8i^2}{5} = \frac{3 + 10i - 8}{5}$$

$$= \frac{-5 + 10i}{5} = -1 + 2i \quad\checkmark$$

Part (e):

$$z^* = 3 - 4i \quad\checkmark$$

Part (f):

$$zz^* = (3 + 4i)(3 - 4i) = 9 + 16 = 25 \quad\checkmark$$

Notice that $zz^* = |z|^2 = 5^2 = 25$, as expected.

**What the examiner wants:** full expansion in part (c), and the conjugate multiplication shown explicitly in part (d). The syllabus says "full details of the working should be shown" for multiplication and division.

### Example 2 - Easy - Powers of $i$

> **Question:** Evaluate (a) $i^{2026}$, (b) $i^{2027}$, (c) $(2i)^3$.

**Solution:**

Part (a) - divide the exponent by $4$:

$$2026 = 4(506) + 2 \implies i^{2026} = i^2 = -1 \quad\checkmark$$

Part (b):

$$i^{2027} = i^{2026} \cdot i = (-1)i = -i \quad\checkmark$$

Part (c):

$$(2i)^3 = 2^3 i^3 = 8(-i) = -8i \quad\checkmark$$

**What the examiner wants:** the remainder after division by $4$, not a long chain of multiplications.

### Example 3 - Medium - Solving a linear equation

> **Question:** Solve $(2 + 3i)z = 4 - i$, giving $z$ in the form $x + iy$.

**Solution:**

Divide by $2 + 3i$:

$$z = \frac{4 - i}{2 + 3i}$$

Multiply by the conjugate $2 - 3i$:

$$z = \frac{(4 - i)(2 - 3i)}{(2 + 3i)(2 - 3i)} = \frac{(4 - i)(2 - 3i)}{4 + 9}$$

Expand the numerator:

$$(4 - i)(2 - 3i) = 8 - 12i - 2i + 3i^2$$

$$= 8 - 14i - 3 = 5 - 14i$$

Therefore

$$z = \frac{5 - 14i}{13} = \frac{5}{13} - \frac{14}{13}i \quad\checkmark$$

**What the examiner wants:** the denominator rationalised to $13$, then the real and imaginary parts separated. Do not leave the answer as a fraction with $i$ in the denominator.

### Example 4 - Medium - Equating real and imaginary parts

> **Question:** Find real numbers $x$ and $y$ such that
> $$(x + iy)(2 - i) = 3 + 4i$$

**Solution:**

Expand the left side:

$$(x + iy)(2 - i) = 2x - xi + 2iy - i^2y$$

$$= 2x + y + i(2y - x)$$

Equate real and imaginary parts:

$$2x + y = 3 \quad \text{(1)}$$

$$-x + 2y = 4 \quad \text{(2)}$$

From (1), $y = 3 - 2x$. Substitute into (2):

$$-x + 2(3 - 2x) = 4$$

$$-x + 6 - 4x = 4$$

$$-5x = -2 \implies x = \frac{2}{5}$$

Then

$$y = 3 - 2\left(\frac{2}{5}\right) = 3 - \frac{4}{5} = \frac{11}{5}$$

Therefore

$$z = \frac{2}{5} + \frac{11}{5}i \quad\checkmark$$

**What the examiner wants:** one complex equation split into two real equations, then solved simultaneously. This is the standard method for every "find $x$ and $y$" question.

### Example 5 - Medium - A conjugate simplification

> **Question:** Simplify
> $$\frac{1 + i}{1 - i} + \frac{1 - i}{1 + i}$$

**Solution:**

First fraction:

$$\frac{1 + i}{1 - i} \cdot \frac{1 + i}{1 + i} = \frac{(1 + i)^2}{1^2 + 1^2} = \frac{1 + 2i + i^2}{2} = \frac{2i}{2} = i$$

Second fraction:

$$\frac{1 - i}{1 + i} \cdot \frac{1 - i}{1 - i} = \frac{(1 - i)^2}{2} = \frac{1 - 2i + i^2}{2} = \frac{-2i}{2} = -i$$

Therefore

$$\frac{1 + i}{1 - i} + \frac{1 - i}{1 + i} = i + (-i) = 0 \quad\checkmark$$

**What the examiner wants:** each fraction simplified separately, with the conjugate multiplication visible.

### Example 6 - Hard - A real-valued quotient

> **Question:** The complex number
> $$z = \frac{a + i}{1 - i}$$
> is real, where $a$ is real. Find $a$.

**Solution:**

Multiply by the conjugate $1 + i$:

$$z = \frac{(a + i)(1 + i)}{(1 - i)(1 + i)} = \frac{a + ai + i + i^2}{2}$$

$$= \frac{a - 1 + (a + 1)i}{2}$$

For $z$ to be real, the imaginary part must be zero:

$$a + 1 = 0 \implies a = -1 \quad\checkmark$$

Then

$$z = \frac{-1 - 1}{2} = -1$$

which is indeed real.

**What the examiner wants:** the condition "real" translated into "imaginary part $= 0$". If the question had said "purely imaginary", you would set the real part $= 0$ instead.

### Practice Questions - Part 1

1. (Easy) For $z = 2 - 3i$ and $w = -1 + 4i$, find $z + w$, $z - w$, $zw$, $z/w$ and $zz^*$.
2. (Easy) Evaluate $i^{100}$, $i^{101}$, $i^{102}$, $i^{103}$ and $i^{2024}$.
3. (Medium) Solve $(3 - 2i)z = 1 + 4i$, giving $z$ in the form $x + iy$.
4. (Medium) Find real $x$ and $y$ such that $(x + iy)(1 + 2i) = 3 + 4i$.
5. (Medium) Simplify $\dfrac{2 + i}{1 - i} + \dfrac{2 - i}{1 + i}$.
6. (Hard) Find the real value of $a$ for which $\dfrac{a + 2i}{1 + i}$ is purely imaginary.

**Solutions:**

Question 1:

$$z + w = (2 - 1) + (-3 + 4)i = 1 + i$$

$$z - w = (2 + 1) + (-3 - 4)i = 3 - 7i$$

$$zw = (2 - 3i)(-1 + 4i) = -2 + 8i + 3i - 12i^2 = 10 + 11i$$

$$\frac{z}{w} = \frac{(2 - 3i)(-1 - 4i)}{(-1)^2 + 4^2} = \frac{-2 - 8i + 3i + 12i^2}{17} = \frac{-14 - 5i}{17}$$

$$zz^* = 2^2 + (-3)^2 = 13$$

Question 2:

$$i^{100} = 1, \qquad i^{101} = i, \qquad i^{102} = -1, \qquad i^{103} = -i$$

$$2024 = 4(506) \implies i^{2024} = 1$$

Question 3:

$$z = \frac{1 + 4i}{3 - 2i} = \frac{(1 + 4i)(3 + 2i)}{3^2 + 2^2}$$

$$= \frac{3 + 2i + 12i + 8i^2}{13} = \frac{3 + 14i - 8}{13} = \frac{-5 + 14i}{13}$$

$$z = -\frac{5}{13} + \frac{14}{13}i$$

Question 4:

$$(x + iy)(1 + 2i) = x + 2xi + iy + 2i^2y = (x - 2y) + i(2x + y)$$

Equate:

$$x - 2y = 3, \qquad 2x + y = 4$$

From the first, $x = 3 + 2y$. Substitute:

$$2(3 + 2y) + y = 4 \implies 6 + 5y = 4 \implies y = -\frac{2}{5}$$

Then

$$x = 3 + 2\left(-\frac{2}{5}\right) = \frac{11}{5}$$

Question 5:

$$\frac{2 + i}{1 - i} = \frac{(2 + i)(1 + i)}{2} = \frac{2 + 2i + i + i^2}{2} = \frac{1 + 3i}{2}$$

$$\frac{2 - i}{1 + i} = \frac{(2 - i)(1 - i)}{2} = \frac{2 - 2i - i + i^2}{2} = \frac{1 - 3i}{2}$$

Adding:

$$\frac{1 + 3i}{2} + \frac{1 - 3i}{2} = \frac{2}{2} = 1$$

Question 6:

$$\frac{a + 2i}{1 + i} = \frac{(a + 2i)(1 - i)}{2} = \frac{a - ai + 2i - 2i^2}{2}$$

$$= \frac{a + 2 + (2 - a)i}{2}$$

Purely imaginary means the real part is zero:

$$a + 2 = 0 \implies a = -2$$

---

# PART 2: Argand Diagram, Modulus and Argument

## 2.1 The Argand Diagram

A complex number $z = x + iy$ is represented by the point $(x, y)$:

- the **real axis** is horizontal;
- the **imaginary axis** is vertical.

The point is the geometric image of $z$. The origin represents $0$. The diagram is called an **Argand diagram**.

Adding complex numbers is vector addition on the diagram. Multiplying is a rotation and a scaling, which is the subject of Part 3.

## 2.2 The Modulus

The **modulus** is the distance from the origin:

$$|z| = \sqrt{x^2 + y^2}$$

It is always non-negative, and $|z| = 0$ only for $z = 0$. For a difference,

$$|z_1 - z_2| = \text{distance between the points } z_1 \text{ and } z_2$$

This distance interpretation is the key to loci in Part 4.

## 2.3 The Argument

The **argument** is the angle the vector makes with the positive real axis, measured anticlockwise:

$$\arg z = \theta$$

The **principal argument** is usually taken in the interval

$$-\pi < \theta \le \pi$$

The syllabus allows either $-\pi < \theta \le \pi$ or $0 \le \theta < 2\pi$, unless the question specifies one. State which interval you are using in a "write down" question.

**Finding the argument.** Let $\alpha = \tan^{-1}\left|\dfrac{y}{x}\right|$ be the acute reference angle. Then:

| Quadrant | Signs of $x, y$ | Principal argument $\theta$ |
|---|---|---|
| 1st | $x > 0, y > 0$ | $\alpha$ |
| 2nd | $x < 0, y > 0$ | $\pi - \alpha$ |
| 3rd | $x < 0, y < 0$ | $-\pi + \alpha$ |
| 4th | $x > 0, y < 0$ | $-\alpha$ |

On the axes:

$$\arg(x) = 0 \text{ for } x > 0, \qquad \arg(-x) = \pi \text{ for } x > 0$$

$$\arg(iy) = \frac{\pi}{2} \text{ for } y > 0, \qquad \arg(-iy) = -\frac{\pi}{2} \text{ for } y > 0$$

The argument of $0$ is undefined.

> ⭐ **Watch Out!** $\tan^{-1}\left(\frac{y}{x}\right)$ alone only gives an angle between $-\frac{\pi}{2}$ and $\frac{\pi}{2}$. It cannot tell a second-quadrant point from a fourth-quadrant point. Always locate the quadrant first, then adjust the reference angle.

## 2.4 Modulus-Argument (Polar) Form

If $r = |z|$ and $\theta = \arg z$, then

$$x = r\cos\theta, \qquad y = r\sin\theta$$

so

$$z = r(\cos\theta + i\sin\theta) = r\operatorname{cis}\theta = re^{i\theta}$$

All three notations are used. The syllabus explicitly includes $r(\cos\theta + i\sin\theta)$ and $re^{i\theta}$.

The **conjugate** in polar form is

$$z^* = r(\cos\theta - i\sin\theta) = r\operatorname{cis}(-\theta) = re^{-i\theta}$$

So conjugation keeps the modulus and negates the argument.

## 2.5 Converting Between Forms

**Cartesian to polar:**

1. Compute $r = \sqrt{x^2 + y^2}$.
2. Locate the quadrant.
3. Compute the reference angle $\alpha = \tan^{-1}\left|\frac{y}{x}\right|$ and adjust.

**Polar to Cartesian:**

$$x = r\cos\theta, \qquad y = r\sin\theta$$

Use exact values for standard angles:

| $\theta$ | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ |
|---|---|---|---|---|---|
| $\cos\theta$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{\sqrt{2}}$ | $\frac{1}{2}$ | $0$ |
| $\sin\theta$ | $0$ | $\frac{1}{2}$ | $\frac{1}{\sqrt{2}}$ | $\frac{\sqrt{3}}{2}$ | $1$ |

### Example 7 - Easy - Polar form in the first quadrant

> **Question:** Write $z = 1 + i\sqrt{3}$ in modulus-argument form.

**Solution:**

Modulus:

$$r = \sqrt{1^2 + (\sqrt{3})^2} = \sqrt{1 + 3} = 2$$

The point $(1, \sqrt{3})$ is in the first quadrant. The reference angle is

$$\alpha = \tan^{-1}\left(\frac{\sqrt{3}}{1}\right) = \frac{\pi}{3}$$

Therefore

$$z = 2\left(\cos\frac{\pi}{3} + i\sin\frac{\pi}{3}\right) = 2\operatorname{cis}\frac{\pi}{3} \quad\checkmark$$

**What the examiner wants:** modulus first, then the quadrant, then the exact angle. Do not write $2\operatorname{cis} 60^\circ$ in a P3 answer unless the question uses degrees.

### Example 8 - Easy - Polar form in the second quadrant

> **Question:** Write $z = -2 + 2i$ in modulus-argument form.

**Solution:**

$$r = \sqrt{(-2)^2 + 2^2} = \sqrt{4 + 4} = 2\sqrt{2}$$

The point $(-2, 2)$ is in the second quadrant. The reference angle is

$$\alpha = \tan^{-1}\left(\frac{2}{2}\right) = \frac{\pi}{4}$$

In the second quadrant,

$$\theta = \pi - \frac{\pi}{4} = \frac{3\pi}{4}$$

Therefore

$$z = 2\sqrt{2}\left(\cos\frac{3\pi}{4} + i\sin\frac{3\pi}{4}\right) \quad\checkmark$$

**What the examiner wants:** the adjustment $\pi - \alpha$. Writing $\frac{\pi}{4}$ here would place the point in the first quadrant, which is wrong.

### Example 9 - Medium - Polar form in the fourth quadrant

> **Question:** Write $z = 3 - 4i$ in modulus-argument form, giving the argument to 3 significant figures.

**Solution:**

$$r = \sqrt{3^2 + (-4)^2} = 5$$

The point $(3, -4)$ is in the fourth quadrant. The reference angle is

$$\alpha = \tan^{-1}\left(\frac{4}{3}\right) \approx 0.9273 \text{ rad}$$

In the fourth quadrant,

$$\theta = -\alpha \approx -0.927 \text{ rad}$$

Therefore

$$z = 5\left(\cos(-0.927) + i\sin(-0.927)\right) \quad\checkmark$$

Equivalently, using $0 \le \theta < 2\pi$,

$$z = 5\left(\cos(5.36) + i\sin(5.36)\right)$$

**What the examiner wants:** the negative angle for the principal interval, or the equivalent angle in $[0, 2\pi)$. Both are acceptable unless the question specifies.

### Example 10 - Medium - Polar form in the third quadrant

> **Question:** Write $z = -1 - i$ in modulus-argument form, using the principal argument.

**Solution:**

$$r = \sqrt{1 + 1} = \sqrt{2}$$

The point $(-1, -1)$ is in the third quadrant. The reference angle is

$$\alpha = \tan^{-1}\left(\frac{1}{1}\right) = \frac{\pi}{4}$$

In the third quadrant, the principal argument is

$$\theta = -\pi + \frac{\pi}{4} = -\frac{3\pi}{4}$$

Therefore

$$z = \sqrt{2}\left(\cos\left(-\frac{3\pi}{4}\right) + i\sin\left(-\frac{3\pi}{4}\right)\right) \quad\checkmark$$

Note that $\frac{5\pi}{4}$ is the same direction but is **not** in the principal interval $-\pi < \theta \le \pi$.

**What the examiner wants:** $-\frac{3\pi}{4}$, not $\frac{5\pi}{4}$, when the principal argument is requested.

### Example 11 - Medium - Polar to Cartesian

> **Question:** Given $|z| = 4$ and $\arg z = \frac{\pi}{6}$, find $z$ in the form $x + iy$.

**Solution:**

$$z = 4\left(\cos\frac{\pi}{6} + i\sin\frac{\pi}{6}\right)$$

$$z = 4\left(\frac{\sqrt{3}}{2} + \frac{1}{2}i\right)$$

$$z = 2\sqrt{3} + 2i \quad\checkmark$$

**What the examiner wants:** exact trigonometric values, then multiplication through the modulus.

### Example 12 - Medium - Powers using polar form

> **Question:** Given $z = 2\left(\cos\frac{3\pi}{4} + i\sin\frac{3\pi}{4}\right)$, find $z^2$ and $z^3$ in Cartesian form.

**Solution:**

For a power, raise the modulus to the power and multiply the argument:

$$z^2 = 2^2\left(\cos\frac{6\pi}{4} + i\sin\frac{6\pi}{4}\right) = 4\left(\cos\frac{3\pi}{2} + i\sin\frac{3\pi}{2}\right)$$

$$z^2 = 4(0 - i) = -4i \quad\checkmark$$

For $z^3$:

$$z^3 = 2^3\left(\cos\frac{9\pi}{4} + i\sin\frac{9\pi}{4}\right)$$

Reduce the angle: $\frac{9\pi}{4} - 2\pi = \frac{\pi}{4}$.

$$z^3 = 8\left(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4}\right) = 8\left(\frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}}i\right)$$

$$z^3 = 4\sqrt{2} + 4\sqrt{2}i \quad\checkmark$$

**What the examiner wants:** the angle reduced back into the principal interval before reading off the exact values. The modulus is raised to the power, not multiplied by it.

### Example 13 - Hard - Quotient in polar and Cartesian form

> **Question:** Express $\dfrac{1 + i}{\sqrt{3} - i}$ in polar form, and hence in Cartesian form.

**Solution:**

For the numerator:

$$|1 + i| = \sqrt{2}, \qquad \arg(1 + i) = \frac{\pi}{4}$$

For the denominator:

$$|\sqrt{3} - i| = \sqrt{3 + 1} = 2, \qquad \arg(\sqrt{3} - i) = -\frac{\pi}{6}$$

Divide the moduli and subtract the arguments:

$$\left|\frac{1 + i}{\sqrt{3} - i}\right| = \frac{\sqrt{2}}{2} = \frac{1}{\sqrt{2}}$$

$$\arg\left(\frac{1 + i}{\sqrt{3} - i}\right) = \frac{\pi}{4} - \left(-\frac{\pi}{6}\right) = \frac{3\pi}{12} + \frac{2\pi}{12} = \frac{5\pi}{12}$$

So

$$\frac{1 + i}{\sqrt{3} - i} = \frac{1}{\sqrt{2}}\left(\cos\frac{5\pi}{12} + i\sin\frac{5\pi}{12}\right) \quad\checkmark$$

For the Cartesian form, multiply numerator and denominator by $\sqrt{3} + i$:

$$\frac{(1 + i)(\sqrt{3} + i)}{3 + 1} = \frac{\sqrt{3} + i + i\sqrt{3} + i^2}{4}$$

$$= \frac{(\sqrt{3} - 1) + (1 + \sqrt{3})i}{4}$$

Therefore

$$\frac{1 + i}{\sqrt{3} - i} = \frac{\sqrt{3} - 1}{4} + \frac{\sqrt{3} + 1}{4}i \quad\checkmark$$

As a check, $\cos\frac{5\pi}{12} = \frac{\sqrt{6} - \sqrt{2}}{4}$ and $\sin\frac{5\pi}{12} = \frac{\sqrt{6} + \sqrt{2}}{4}$; multiplying by $\frac{1}{\sqrt{2}}$ gives the same Cartesian result.

**What the examiner wants:** the polar form built from the moduli and arguments of numerator and denominator, then an independent Cartesian check. The angle $\frac{5\pi}{12}$ is outside the standard table, so the Cartesian route is the safer way to finish.

### Practice Questions - Part 2

1. (Easy) Write $z = -1 + i$ in modulus-argument form, using the principal argument.
2. (Easy) Write $z = 2 - 2i$ in modulus-argument form.
3. (Easy) Write $z = -3$ and $z = 4i$ in modulus-argument form.
4. (Easy) Given $|z| = 6$ and $\arg z = -\frac{\pi}{3}$, find $z$ in Cartesian form.
5. (Medium) For $z = \sqrt{3} + i$, find $z^2$ and $z^3$ in Cartesian form.
6. (Medium) For $z = 1 - i$, find $z^4$ using polar form.
7. (Medium) Write $-2 + 2\sqrt{3}i$ in modulus-argument form.
8. (Hard) Express $\dfrac{1 - i}{1 + i\sqrt{3}}$ in polar form and in Cartesian form.

**Solutions:**

Question 1:

$$r = \sqrt{1 + 1} = \sqrt{2}, \qquad \arg z = \pi - \frac{\pi}{4} = \frac{3\pi}{4}$$

$$z = \sqrt{2}\left(\cos\frac{3\pi}{4} + i\sin\frac{3\pi}{4}\right)$$

Question 2:

$$r = \sqrt{4 + 4} = 2\sqrt{2}, \qquad \arg z = -\frac{\pi}{4}$$

$$z = 2\sqrt{2}\left(\cos\left(-\frac{\pi}{4}\right) + i\sin\left(-\frac{\pi}{4}\right)\right)$$

Question 3:

$$-3 = 3(\cos\pi + i\sin\pi)$$

$$4i = 4\left(\cos\frac{\pi}{2} + i\sin\frac{\pi}{2}\right)$$

Question 4:

$$z = 6\left(\cos\left(-\frac{\pi}{3}\right) + i\sin\left(-\frac{\pi}{3}\right)\right) = 6\left(\frac{1}{2} - \frac{\sqrt{3}}{2}i\right)$$

$$z = 3 - 3\sqrt{3}i$$

Question 5:

$$z = \sqrt{3} + i \implies r = 2, \quad \arg z = \frac{\pi}{6}$$

$$z^2 = 4\left(\cos\frac{\pi}{3} + i\sin\frac{\pi}{3}\right) = 4\left(\frac{1}{2} + \frac{\sqrt{3}}{2}i\right) = 2 + 2\sqrt{3}i$$

$$z^3 = 8\left(\cos\frac{\pi}{2} + i\sin\frac{\pi}{2}\right) = 8i$$

Question 6:

$$z = 1 - i \implies r = \sqrt{2}, \quad \arg z = -\frac{\pi}{4}$$

$$z^4 = (\sqrt{2})^4\left(\cos(-\pi) + i\sin(-\pi)\right) = 4(-1 + 0i) = -4$$

Question 7:

$$r = \sqrt{4 + 12} = 4$$

The point $(-2, 2\sqrt{3})$ is in the second quadrant, with reference angle

$$\alpha = \tan^{-1}\left(\frac{2\sqrt{3}}{2}\right) = \frac{\pi}{3}$$

$$\arg z = \pi - \frac{\pi}{3} = \frac{2\pi}{3}$$

$$z = 4\left(\cos\frac{2\pi}{3} + i\sin\frac{2\pi}{3}\right)$$

Question 8:

Numerator:

$$|1 - i| = \sqrt{2}, \qquad \arg(1 - i) = -\frac{\pi}{4}$$

Denominator:

$$|1 + i\sqrt{3}| = 2, \qquad \arg(1 + i\sqrt{3}) = \frac{\pi}{3}$$

Quotient:

$$\left|\frac{1 - i}{1 + i\sqrt{3}}\right| = \frac{\sqrt{2}}{2} = \frac{1}{\sqrt{2}}$$

$$\arg\left(\frac{1 - i}{1 + i\sqrt{3}}\right) = -\frac{\pi}{4} - \frac{\pi}{3} = -\frac{7\pi}{12}$$

$$\frac{1 - i}{1 + i\sqrt{3}} = \frac{1}{\sqrt{2}}\left(\cos\left(-\frac{7\pi}{12}\right) + i\sin\left(-\frac{7\pi}{12}\right)\right)$$

For the Cartesian form, multiply by $1 - i\sqrt{3}$:

$$\frac{(1 - i)(1 - i\sqrt{3})}{1 + 3} = \frac{1 - i\sqrt{3} - i + i^2\sqrt{3}}{4}$$

$$= \frac{(1 - \sqrt{3}) - (1 + \sqrt{3})i}{4}$$

---

# PART 3: Polar Form, Multiplication, Division and Roots

## 3.1 Multiplication and Division in Polar Form

If

$$z_1 = r_1(\cos\theta_1 + i\sin\theta_1), \qquad z_2 = r_2(\cos\theta_2 + i\sin\theta_2)$$

then

$$z_1z_2 = r_1r_2\left(\cos(\theta_1 + \theta_2) + i\sin(\theta_1 + \theta_2)\right)$$

$$\frac{z_1}{z_2} = \frac{r_1}{r_2}\left(\cos(\theta_1 - \theta_2) + i\sin(\theta_1 - \theta_2)\right)$$

In words:

- **multiplying** multiplies the moduli and **adds** the arguments;
- **dividing** divides the moduli and **subtracts** the arguments.

These give the standard results

$$|z_1z_2| = |z_1||z_2|, \qquad \arg(z_1z_2) = \arg z_1 + \arg z_2$$

$$\left|\frac{z_1}{z_2}\right| = \frac{|z_1|}{|z_2|}, \qquad \arg\left(\frac{z_1}{z_2}\right) = \arg z_1 - \arg z_2$$

The arguments are understood **modulo $2\pi$**: after adding or subtracting, reduce the angle to your chosen interval.

> ⭐ **Watch Out!** The modulus rule is multiplicative for products and quotients, but **not** for sums: $|z_1 + z_2| \neq |z_1| + |z_2|$ in general. Only the product and quotient rules are safe.

## 3.2 Powers

Repeated multiplication gives, for a positive integer $n$,

$$z^n = r^n\left(\cos(n\theta) + i\sin(n\theta)\right)$$

This is **De Moivre's theorem**. It follows directly from the multiplication rule by induction, so you do not need to quote the name in an exam; just apply the formula.

For negative powers, use

$$z^{-n} = \frac{1}{z^n} = r^{-n}\left(\cos(-n\theta) + i\sin(-n\theta)\right)$$

## 3.3 Square Roots of a Complex Number

To find the two square roots of $a + bi$:

**Method 1 - Cartesian (recommended for exact answers).** Let

$$(x + iy)^2 = a + bi$$

Equate real and imaginary parts:

$$x^2 - y^2 = a, \qquad 2xy = b$$

Also use the modulus:

$$x^2 + y^2 = \sqrt{a^2 + b^2}$$

Solve the three equations for $x$ and $y$. The two roots are $\pm(x + iy)$.

**Method 2 - Polar.** Write $a + bi = r(\cos\theta + i\sin\theta)$. Then

$$\sqrt{a + bi} = \pm\sqrt{r}\left(\cos\frac{\theta}{2} + i\sin\frac{\theta}{2}\right)$$

The $\pm$ gives the two roots. This method is quick when $\theta$ is a standard angle, but the Cartesian method is usually better for exact surd answers.

> ⭐ **Watch Out!** A non-zero complex number always has **two** square roots, and they are negatives of each other. Do not stop after finding one.

## 3.4 Geometric Effects

On the Argand diagram:

| Operation | Geometric effect |
|---|---|
| $z \mapsto z + w$ | translation by the vector $w$ |
| $z \mapsto kz$ ($k > 0$ real) | scaling by factor $k$ about the origin |
| $z \mapsto iz$ | rotation by $\frac{\pi}{2}$ anticlockwise |
| $z \mapsto -iz$ | rotation by $\frac{\pi}{2}$ clockwise |
| $z \mapsto z^*$ | reflection in the real axis |
| $z \mapsto wz$ | scaling by $\lvert w\rvert$, rotation by $\arg w$ |
| $z \mapsto \dfrac{z}{w}$ | scaling by $\dfrac{1}{\lvert w\rvert}$, rotation by $-\arg w$ |

In particular, multiplying by $i$ four times returns the original number:

$$z \mapsto iz \mapsto -z \mapsto -iz \mapsto z$$

which matches $i^4 = 1$.

### Example 14 - Medium - Multiplication and division in polar form

> **Question:** Given
> $$z_1 = 2\left(\cos\frac{\pi}{3} + i\sin\frac{\pi}{3}\right), \qquad z_2 = 3\left(\cos\frac{\pi}{6} + i\sin\frac{\pi}{6}\right)$$
> find $z_1z_2$ and $\dfrac{z_1}{z_2}$ in polar form, and then in Cartesian form.

**Solution:**

Product:

$$z_1z_2 = (2)(3)\left(\cos\left(\frac{\pi}{3} + \frac{\pi}{6}\right) + i\sin\left(\frac{\pi}{3} + \frac{\pi}{6}\right)\right)$$

$$z_1z_2 = 6\left(\cos\frac{\pi}{2} + i\sin\frac{\pi}{2}\right) \quad\checkmark$$

In Cartesian form:

$$z_1z_2 = 6(0 + i) = 6i \quad\checkmark$$

Quotient:

$$\frac{z_1}{z_2} = \frac{2}{3}\left(\cos\left(\frac{\pi}{3} - \frac{\pi}{6}\right) + i\sin\left(\frac{\pi}{3} - \frac{\pi}{6}\right)\right)$$

$$= \frac{2}{3}\left(\cos\frac{\pi}{6} + i\sin\frac{\pi}{6}\right) \quad\checkmark$$

In Cartesian form:

$$\frac{z_1}{z_2} = \frac{2}{3}\left(\frac{\sqrt{3}}{2} + \frac{1}{2}i\right) = \frac{\sqrt{3}}{3} + \frac{1}{3}i \quad\checkmark$$

**What the examiner wants:** add/subtract the arguments and multiply/divide the moduli, then substitute exact trigonometric values.

### Example 15 - Medium - A fourth power

> **Question:** Find $(1 + i)^4$ using polar form.

**Solution:**

$$|1 + i| = \sqrt{2}, \qquad \arg(1 + i) = \frac{\pi}{4}$$

$$(1 + i)^4 = (\sqrt{2})^4\left(\cos\left(4 \cdot \frac{\pi}{4}\right) + i\sin\left(4 \cdot \frac{\pi}{4}\right)\right)$$

$$= 4(\cos\pi + i\sin\pi)$$

$$= 4(-1 + 0i) = -4 \quad\checkmark$$

**What the examiner wants:** the modulus raised to the fourth power, and the argument multiplied by $4$. Reducing $4\theta$ modulo $2\pi$ before evaluating is essential.

### Example 16 - Medium - Square roots by Cartesian equations

> **Question:** Find the two square roots of $5 + 12i$ in exact Cartesian form.

**Solution:**

Let

$$(x + iy)^2 = 5 + 12i$$

Expand:

$$x^2 - y^2 + 2xyi = 5 + 12i$$

Equate real and imaginary parts:

$$x^2 - y^2 = 5 \quad \text{(1)}$$

$$2xy = 12 \implies xy = 6 \quad \text{(2)}$$

Use the modulus:

$$x^2 + y^2 = \sqrt{5^2 + 12^2} = 13 \quad \text{(3)}$$

Add (1) and (3):

$$2x^2 = 18 \implies x^2 = 9 \implies x = \pm 3$$

Subtract (1) from (3):

$$2y^2 = 8 \implies y^2 = 4 \implies y = \pm 2$$

From (2), $xy = 6 > 0$, so $x$ and $y$ have the **same sign**:

$$(x, y) = (3, 2) \text{ or } (-3, -2)$$

Therefore

$$\sqrt{5 + 12i} = \pm(3 + 2i) \quad\checkmark$$

Check: $(3 + 2i)^2 = 9 + 12i + 4i^2 = 9 + 12i - 4 = 5 + 12i$.

**What the examiner wants:** all three equations, the same-sign condition from $2xy = b$, and both roots. The check is quick and catches sign errors.

### Example 17 - Medium - Square roots with a negative real part

> **Question:** Find the two square roots of $-3 + 4i$.

**Solution:**

Let $(x + iy)^2 = -3 + 4i$. Then

$$x^2 - y^2 = -3 \quad \text{(1)}$$

$$2xy = 4 \implies xy = 2 \quad \text{(2)}$$

$$x^2 + y^2 = \sqrt{9 + 16} = 5 \quad \text{(3)}$$

Add (1) and (3):

$$2x^2 = 2 \implies x^2 = 1 \implies x = \pm 1$$

Subtract (1) from (3):

$$2y^2 = 8 \implies y^2 = 4 \implies y = \pm 2$$

Since $xy = 2 > 0$, $x$ and $y$ have the same sign:

$$(x, y) = (1, 2) \text{ or } (-1, -2)$$

Therefore

$$\sqrt{-3 + 4i} = \pm(1 + 2i) \quad\checkmark$$

Check: $(1 + 2i)^2 = 1 + 4i + 4i^2 = 1 + 4i - 4 = -3 + 4i$.

**What the examiner wants:** the same method as Example 16, with the sign of $xy$ deciding the pairing. The negative real part does not change the procedure.

### Example 18 - Medium - Powers and reciprocals with $re^{i\theta}$

> **Question:** Given $z = 2e^{i\pi/3}$, find $z^3$ and $\dfrac{1}{z}$ in Cartesian form.

**Solution:**

For $z^3$:

$$z^3 = 2^3 e^{i(3\pi/3)} = 8e^{i\pi} = 8(\cos\pi + i\sin\pi) = -8 \quad\checkmark$$

For $1/z$:

$$\frac{1}{z} = \frac{1}{2}e^{-i\pi/3} = \frac{1}{2}\left(\cos\frac{\pi}{3} - i\sin\frac{\pi}{3}\right)$$

$$= \frac{1}{2}\left(\frac{1}{2} - \frac{\sqrt{3}}{2}i\right) = \frac{1}{4} - \frac{\sqrt{3}}{4}i \quad\checkmark$$

**What the examiner wants:** negative exponent for the reciprocal, then Euler's formula read off with exact values.

### Example 19 - Medium - Describing a geometric transformation

> **Question:** Describe the transformation of the Argand diagram given by $z \mapsto (1 + i)z$. Find the image of $3$ and the image of $1 + i$.

**Solution:**

For $w = 1 + i$:

$$|w| = \sqrt{2}, \qquad \arg w = \frac{\pi}{4}$$

Multiplication by $w$ therefore:

- scales distances from the origin by $\sqrt{2}$;
- rotates every point by $\frac{\pi}{4}$ anticlockwise about the origin.

Image of $3$:

$$(1 + i)(3) = 3 + 3i$$

Image of $1 + i$:

$$(1 + i)(1 + i) = 1 + 2i + i^2 = 2i$$

**What the examiner wants:** both the scale factor and the rotation angle, then the two specific images. "Rotation by $45^\circ$" is acceptable if the question uses degrees, but radians are safer in P3.

### Practice Questions - Part 3

1. (Easy) For $z_1 = \sqrt{2}\left(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4}\right)$ and $z_2 = 2\left(\cos\left(-\frac{\pi}{6}\right) + i\sin\left(-\frac{\pi}{6}\right)\right)$, find $z_1z_2$ and $z_1/z_2$ in polar form.
2. (Medium) For $z = \sqrt{3} - i$, find $z^6$ using polar form.
3. (Medium) Find the two square roots of $3 + 4i$.
4. (Medium) Find the two square roots of $-5 - 12i$.
5. (Medium) Find $(1 + i)^8$.
6. (Medium) For $z = 1 + i\sqrt{3}$, find $z^3$.
7. (Medium) Describe the transformation $z \mapsto iz$ and find the image of $2 + 3i$.
8. (Hard) Express $\dfrac{(1 + i)^4}{(1 - i\sqrt{3})^3}$ in polar form.

**Solutions:**

Question 1:

$$z_1z_2 = 2\sqrt{2}\left(\cos\left(\frac{\pi}{4} - \frac{\pi}{6}\right) + i\sin\left(\frac{\pi}{4} - \frac{\pi}{6}\right)\right)$$

$$= 2\sqrt{2}\left(\cos\frac{\pi}{12} + i\sin\frac{\pi}{12}\right)$$

$$\frac{z_1}{z_2} = \frac{\sqrt{2}}{2}\left(\cos\left(\frac{\pi}{4} + \frac{\pi}{6}\right) + i\sin\left(\frac{\pi}{4} + \frac{\pi}{6}\right)\right)$$

$$= \frac{1}{\sqrt{2}}\left(\cos\frac{5\pi}{12} + i\sin\frac{5\pi}{12}\right)$$

Question 2:

$$z = \sqrt{3} - i \implies r = 2, \quad \arg z = -\frac{\pi}{6}$$

$$z^6 = 2^6\left(\cos(-\pi) + i\sin(-\pi)\right) = 64(-1) = -64$$

Question 3:

$$x^2 - y^2 = 3, \qquad 2xy = 4 \implies xy = 2, \qquad x^2 + y^2 = 5$$

$$x^2 = 4 \implies x = \pm 2, \qquad y^2 = 1 \implies y = \pm 1$$

Since $xy > 0$, the signs match:

$$\sqrt{3 + 4i} = \pm(2 + i)$$

Question 4:

$$x^2 - y^2 = -5, \qquad 2xy = -12 \implies xy = -6, \qquad x^2 + y^2 = 13$$

$$x^2 = 4 \implies x = \pm 2, \qquad y^2 = 9 \implies y = \pm 3$$

Since $xy < 0$, the signs are opposite:

$$\sqrt{-5 - 12i} = \pm(2 - 3i)$$

Question 5:

$$1 + i = \sqrt{2}\operatorname{cis}\frac{\pi}{4}$$

$$(1 + i)^8 = (\sqrt{2})^8\operatorname{cis}(2\pi) = 16(1) = 16$$

Question 6:

$$1 + i\sqrt{3} = 2\operatorname{cis}\frac{\pi}{3}$$

$$z^3 = 8\operatorname{cis}(\pi) = -8$$

Question 7:

Multiplication by $i$ rotates every point by $\frac{\pi}{2}$ anticlockwise about the origin. The image of $2 + 3i$ is

$$i(2 + 3i) = 2i + 3i^2 = -3 + 2i$$

Question 8:

Numerator:

$$(1 + i)^4 = -4 \quad \text{(from Example 15)}$$

In polar form, $-4 = 4\operatorname{cis}\pi$.

Denominator:

$$1 - i\sqrt{3} = 2\operatorname{cis}\left(-\frac{\pi}{3}\right)$$

$$(1 - i\sqrt{3})^3 = 8\operatorname{cis}(-\pi) = -8$$

Therefore

$$\frac{(1 + i)^4}{(1 - i\sqrt{3})^3} = \frac{-4}{-8} = \frac{1}{2}$$

In polar form, $\frac{1}{2} = \frac{1}{2}\operatorname{cis}(0)$ (or $\frac{1}{2}e^{0i}$).

---

# PART 4: Loci and Regions

## 4.1 Circles from Modulus Equations

The equation

$$|z - z_0| = r \qquad (r > 0)$$

describes the **circle** with centre $z_0$ and radius $r$. The reason is that $|z - z_0|$ is the distance from $z$ to $z_0$.

The inequality

$$|z - z_0| < r$$

describes the **inside** of the circle (the open disc), and $|z - z_0| \le r$ includes the boundary. Similarly, $|z - z_0| > r$ is the outside.

## 4.2 Perpendicular Bisectors

The equation

$$|z - z_1| = |z - z_2|$$

describes the set of points equidistant from $z_1$ and $z_2$: the **perpendicular bisector** of the segment joining them. To find its Cartesian equation, let $z = x + iy$ and square both sides:

$$(x - x_1)^2 + (y - y_1)^2 = (x - x_2)^2 + (y - y_2)^2$$

The $x^2$ and $y^2$ terms cancel, leaving a straight line.

The inequality $|z - z_1| < |z - z_2|$ is the **half-plane** on the side of the perpendicular bisector containing $z_1$.

## 4.3 Half-Lines and Sectors from Arguments

The equation

$$\arg(z - z_0) = \theta$$

describes the **half-line** starting at $z_0$ and making angle $\theta$ with the positive real direction. The point $z_0$ itself is not included because $\arg 0$ is undefined.

The inequality

$$\alpha < \arg(z - z_0) < \beta$$

describes the **sector** (wedge) between the half-lines at angles $\alpha$ and $\beta$, with vertex at $z_0$, again excluding $z_0$.

> ⭐ **Watch Out!** The locus is $\arg(z - z_0) = \theta$, not $\arg z = \theta$. Subtracting $z_0$ moves the vertex to $z_0$. For example, $\arg(z - 2 - i) = \frac{\pi}{4}$ is a half-line from $(2, 1)$, not from the origin.

## 4.4 Regions and Shading

To describe or shade a region:

1. Identify each boundary (circle, line, half-line).
2. Decide whether the boundary is included ($\le$, $\ge$, $=$) or excluded ($<$, $>$, strict).
3. Test a convenient point to decide which side of each boundary to shade.
4. The required region is the **intersection** of the individual regions.

## 4.5 Maximum and Minimum Modulus

For points on the circle $|z - z_0| = r$, the distance from the origin varies between

$$|z|_{\min} = \bigl|\,|z_0| - r\,\bigr|, \qquad |z|_{\max} = |z_0| + r$$

Geometrically, draw the line from the origin through the centre $z_0$; it meets the circle at the nearest and farthest points.

### Example 20 - Easy - A circle

> **Question:** Describe the locus of $z$ satisfying $|z - (3 + 2i)| = 4$.

**Solution:**

Rewrite as

$$|z - (3 + 2i)| = 4$$

This is the set of points at distance $4$ from $3 + 2i$. Therefore the locus is a circle with centre $(3, 2)$ and radius $4$. $\checkmark$

**What the examiner wants:** "centre" and "radius" stated explicitly. A sketch with the centre marked earns the diagram mark.

### Example 21 - Easy - A circle after rewriting the centre

> **Question:** Describe the locus of $z$ satisfying $|z + 1 - 2i| = 3$.

**Solution:**

Rewrite the expression inside the modulus as a subtraction:

$$|z + 1 - 2i| = |z - (-1 + 2i)| = 3$$

Therefore the locus is a circle with centre $(-1, 2)$ and radius $3$. $\checkmark$

**What the examiner wants:** the centre read as $-1 + 2i$, not $1 - 2i$. The sign flip is the most common error in this topic.

### Example 22 - Medium - A perpendicular bisector

> **Question:** Find the Cartesian equation of the locus
> $$|z - (1 + 2i)| = |z - (3 - 4i)|$$

**Solution:**

Let $z = x + iy$. Then

$$|(x - 1) + i(y - 2)| = |(x - 3) + i(y + 4)|$$

Square both sides:

$$(x - 1)^2 + (y - 2)^2 = (x - 3)^2 + (y + 4)^2$$

Expand:

$$x^2 - 2x + 1 + y^2 - 4y + 4 = x^2 - 6x + 9 + y^2 + 8y + 16$$

Cancel $x^2$ and $y^2$:

$$-2x - 4y + 5 = -6x + 8y + 25$$

Rearrange:

$$4x - 12y - 20 = 0$$

Divide by $4$:

$$x - 3y - 5 = 0 \quad\checkmark$$

This is the perpendicular bisector of the segment joining $(1, 2)$ and $(3, -4)$.

**What the examiner wants:** the squared-distance equation, the cancellation, and a simplified linear equation. Do not try to complete the square; the quadratic terms are meant to cancel.

### Example 23 - Medium - A half-line

> **Question:** Describe the locus of $z$ satisfying
> $$\arg(z - 2 - i) = \frac{\pi}{4}$$

**Solution:**

Rewrite:

$$\arg\left(z - (2 + i)\right) = \frac{\pi}{4}$$

This is the half-line starting at $(2, 1)$ and making angle $\frac{\pi}{4}$ with the positive real direction. The direction vector is $(1, 1)$, so the Cartesian equation is

$$y - 1 = x - 2 \implies y = x - 1$$

with the restriction $x > 2$ (the half-line, not the whole line). $\checkmark$

**What the examiner wants:** the vertex, the angle, and the half-line restriction. Writing the full line $y = x - 1$ loses the "half" in half-line.

### Example 24 - Medium - A sector region

> **Question:** Describe the region satisfying both
> $$|z - 2| \le 2 \qquad \text{and} \qquad 0 \le \arg(z - 2) \le \frac{\pi}{4}$$

**Solution:**

The first inequality is the disc with centre $(2, 0)$ and radius $2$, including the boundary.

The second is the sector with vertex $(2, 0)$ between the positive real direction ($\theta = 0$) and the line at $\theta = \frac{\pi}{4}$.

The required region is the part of the disc lying between those two rays: a sector of the disc, bounded by the circular arc and the two straight edges, with vertex $(2, 0)$. $\checkmark$

**What the examiner wants:** a description of the intersection, not two separate regions. Mention the vertex and which boundaries are included.

### Example 25 - Medium - Maximum and minimum modulus

> **Question:** The point $z$ lies on the circle $|z - 3 - 4i| = 2$. Find the minimum and maximum possible values of $|z|$.

**Solution:**

The centre is $3 + 4i$, whose distance from the origin is

$$|3 + 4i| = 5$$

The radius is $2$. The nearest point of the circle to the origin is on the line from the origin through the centre:

$$|z|_{\min} = 5 - 2 = 3$$

The farthest point is on the opposite side:

$$|z|_{\max} = 5 + 2 = 7 \quad\checkmark$$

**What the examiner wants:** the centre distance first, then $\text{centre distance} \pm \text{radius}$. Drawing the line through the centre makes the result immediate.

### Example 26 - Medium - Another perpendicular bisector

> **Question:** Find the Cartesian equation of the locus $|z - 1| = |z - i|$.

**Solution:**

Let $z = x + iy$:

$$|(x - 1) + iy| = |x + i(y - 1)|$$

Square:

$$(x - 1)^2 + y^2 = x^2 + (y - 1)^2$$

Expand:

$$x^2 - 2x + 1 + y^2 = x^2 + y^2 - 2y + 1$$

Cancel:

$$-2x = -2y \implies y = x \quad\checkmark$$

This is the perpendicular bisector of the segment joining $(1, 0)$ and $(0, 1)$.

**What the examiner wants:** the correct difference $z - i = x + i(y - 1)$. A sign slip here changes the line completely.

### Example 27 - Hard - Intersection of a circle and a half-line

> **Question:** Find the point(s) of intersection of the circle $|z - 2| = 2$ and the half-line $\arg z = \frac{\pi}{4}$.

**Solution:**

The half-line $\arg z = \frac{\pi}{4}$ has Cartesian equation

$$y = x, \qquad x > 0$$

The circle $|z - 2| = 2$ has equation

$$(x - 2)^2 + y^2 = 4$$

Substitute $y = x$:

$$(x - 2)^2 + x^2 = 4$$

$$x^2 - 4x + 4 + x^2 = 4$$

$$2x^2 - 4x = 0$$

$$2x(x - 2) = 0$$

So $x = 0$ or $x = 2$. The half-line requires $x > 0$, so $x = 0$ is excluded. Therefore $x = 2$ and $y = 2$:

$$z = 2 + 2i \quad\checkmark$$

**What the examiner wants:** the algebraic substitution and the rejection of the extraneous root $x = 0$. The origin lies on the full line $y = x$ and on the circle, but not on the half-line because $\arg 0$ is undefined.

### Practice Questions - Part 4

1. (Easy) Describe the locus $|z + 2 - 3i| = 5$.
2. (Medium) Find the Cartesian equation of the locus $|z - 1| = |z + 2i|$.
3. (Medium) Describe the locus $\arg(z - 3) = \frac{\pi}{3}$.
4. (Medium) Describe and sketch the region $|z - 1| \le 2$ with $\operatorname{Im} z \ge 0$.
5. (Medium) The point $z$ lies on $|z - 1 - 2i| = 3$. Find the minimum and maximum values of $|z|$.
6. (Medium) Find the points of intersection of $|z| = 2$ and $|z - 2| = 2$.
7. (Medium) Describe the region $|z - 1| < |z + 1|$.
8. (Hard) Find the points of intersection of $|z - 1| = |z - i|$ and $|z| = 2$.

**Solutions:**

Question 1:

$$|z + 2 - 3i| = |z - (-2 + 3i)| = 5$$

The locus is a circle with centre $(-2, 3)$ and radius $5$.

Question 2:

$$|(x - 1) + iy| = |x + i(y + 2)|$$

$$(x - 1)^2 + y^2 = x^2 + (y + 2)^2$$

$$x^2 - 2x + 1 + y^2 = x^2 + y^2 + 4y + 4$$

$$-2x + 1 = 4y + 4$$

$$2x + 4y + 3 = 0$$

Question 3:

The locus is the half-line starting at $(3, 0)$ at angle $\frac{\pi}{3}$ to the positive real axis. Its Cartesian equation is

$$y = \sqrt{3}(x - 3), \qquad x > 3$$

Question 4:

The disc with centre $(1, 0)$ and radius $2$, restricted to the upper half-plane $y \ge 0$. The region is the upper half of the disc, including the diameter on the real axis.

Question 5:

The centre is $1 + 2i$, with

$$|1 + 2i| = \sqrt{5}$$

The radius is $3$, so

$$|z|_{\min} = 3 - \sqrt{5}, \qquad |z|_{\max} = 3 + \sqrt{5}$$

Since $\sqrt{5} \approx 2.236 < 3$, the minimum is positive.

Question 6:

The first circle is $x^2 + y^2 = 4$. The second is

$$(x - 2)^2 + y^2 = 4 \implies x^2 - 4x + 4 + y^2 = 4$$

Using $x^2 + y^2 = 4$:

$$4 - 4x + 4 = 4 \implies x = 1$$

Then

$$1 + y^2 = 4 \implies y^2 = 3 \implies y = \pm\sqrt{3}$$

The points are

$$z = 1 + i\sqrt{3} \quad \text{and} \quad z = 1 - i\sqrt{3}$$

Question 7:

$$|z - 1| < |z + 1| \iff (x - 1)^2 + y^2 < (x + 1)^2 + y^2$$

$$x^2 - 2x + 1 < x^2 + 2x + 1$$

$$-2x < 2x \implies x > 0$$

The region is the open right half-plane $x > 0$.

Question 8:

From $|z - 1| = |z - i|$ (Example 26), the locus is $y = x$.

With $|z| = 2$:

$$x^2 + y^2 = 4 \implies x^2 + x^2 = 4 \implies 2x^2 = 4 \implies x^2 = 2$$

$$x = \pm\sqrt{2}, \qquad y = \pm\sqrt{2}$$

The points are

$$z = \sqrt{2} + \sqrt{2}i \quad \text{and} \quad z = -\sqrt{2} - \sqrt{2}i$$

---

# PART 5: Equations, Roots and Conjugate Pairs

## 5.1 Quadratic Equations with Real Coefficients

For

$$az^2 + bz + c = 0 \qquad (a, b, c \in \mathbb{R}, \; a \neq 0)$$

the discriminant is

$$\Delta = b^2 - 4ac$$

- If $\Delta > 0$, there are two distinct real roots.
- If $\Delta = 0$, there is one repeated real root.
- If $\Delta < 0$, there are two complex conjugate roots.

In the complex case, the quadratic formula still works:

$$z = \frac{-b \pm i\sqrt{4ac - b^2}}{2a}$$

## 5.2 The Conjugate Pair Theorem

If a polynomial equation has **real coefficients** and $a + bi$ is a root, then its conjugate $a - bi$ is also a root.

This is why non-real roots of real polynomials come in pairs. It applies to quadratics, cubics, quartics and beyond. The theorem does **not** apply when the coefficients are complex.

**Consequences:**

- A cubic with real coefficients has either three real roots or one real root and one conjugate pair.
- A quartic with real coefficients has either four real roots, two real roots and one conjugate pair, or two conjugate pairs.
- Once you know one non-real root, you immediately know a second, and you can form the real quadratic factor
  $$(z - (a + bi))(z - (a - bi)) = (z - a)^2 + b^2 = z^2 - 2az + (a^2 + b^2)$$

## 5.3 Forming an Equation from Its Roots

If the roots are $\alpha$ and $\beta$, then

$$z^2 - (\alpha + \beta)z + \alpha\beta = 0$$

For a conjugate pair $a \pm bi$:

$$\text{sum} = 2a, \qquad \text{product} = a^2 + b^2$$

so the quadratic factor is

$$z^2 - 2az + (a^2 + b^2)$$

## 5.4 Cubic and Quartic Equations

For a cubic with a known non-real root:

1. Write down the conjugate root.
2. Form the real quadratic factor from the pair.
3. Divide the cubic by that quadratic (long division or inspection).
4. Solve the remaining linear factor for the third root.

For a quartic, divide by the quadratic factor and solve the remaining quadratic.

## 5.5 Equations Involving $z$ and $z^*$

When an equation mixes $z$ and $z^*$, substitute

$$z = x + iy, \qquad z^* = x - iy$$

expand, and equate real and imaginary parts. Useful shortcuts:

$$z + z^* = 2x, \qquad z - z^* = 2iy$$

## 5.6 Equations of the Form $z^2 = a + bi$

These are solved by the square-root method from Part 3. The two roots are negatives of each other. Always give both.

### Example 28 - Easy - Recovering the quadratic from one complex root

> **Question:** The equation $z^2 + pz + q = 0$ has real coefficients and $2 + 3i$ is a root. Find $p$ and $q$.

**Solution:**

Since the coefficients are real, the conjugate $2 - 3i$ is also a root.

Sum of roots:

$$(2 + 3i) + (2 - 3i) = 4$$

Product of roots:

$$(2 + 3i)(2 - 3i) = 4 + 9 = 13$$

For $z^2 + pz + q = 0$:

$$\text{sum} = -p = 4 \implies p = -4$$

$$\text{product} = q = 13$$

Therefore

$$p = -4, \qquad q = 13 \quad\checkmark$$

The equation is $z^2 - 4z + 13 = 0$.

**What the examiner wants:** the conjugate root stated, then sum and product compared with the coefficients. Do not substitute $2 + 3i$ into the equation and solve simultaneous equations; the sum/product route is faster.

### Example 29 - Easy - Solving a quadratic with complex roots

> **Question:** Solve $z^2 - 6z + 25 = 0$.

**Solution:**

Discriminant:

$$\Delta = (-6)^2 - 4(1)(25) = 36 - 100 = -64$$

Since $\Delta < 0$, the roots are complex:

$$z = \frac{6 \pm \sqrt{-64}}{2} = \frac{6 \pm 8i}{2}$$

$$z = 3 \pm 4i \quad\checkmark$$

**What the examiner wants:** the negative discriminant handled with $i$, and both roots given.

### Example 30 - Medium - A cubic with one complex root

> **Question:** The equation $z^3 - 3z^2 + 4z - 2 = 0$ has real coefficients and $1 + i$ is a root. Find all the roots.

**Solution:**

The conjugate $1 - i$ is also a root. Form the quadratic factor:

$$(z - (1 + i))(z - (1 - i)) = (z - 1)^2 + 1 = z^2 - 2z + 2$$

Divide the cubic by this quadratic. By inspection,

$$z^3 - 3z^2 + 4z - 2 = (z^2 - 2z + 2)(z - 1)$$

Check by expansion:

$$(z^2 - 2z + 2)(z - 1) = z^3 - z^2 - 2z^2 + 2z + 2z - 2 = z^3 - 3z^2 + 4z - 2 \quad\checkmark$$

The remaining root is $z = 1$. Therefore the roots are

$$z = 1 + i, \qquad z = 1 - i, \qquad z = 1 \quad\checkmark$$

**What the examiner wants:** the conjugate pair, the real quadratic factor, and the division. State all three roots clearly.

### Example 31 - Medium - A cubic with a non-monic leading coefficient

> **Question:** The equation $2z^3 - 9z^2 + 14z - 5 = 0$ has real coefficients and $2 - i$ is a root. Find all the roots.

**Solution:**

The conjugate $2 + i$ is also a root. The quadratic factor is

$$(z - (2 - i))(z - (2 + i)) = (z - 2)^2 + 1 = z^2 - 4z + 5$$

Divide:

$$2z^3 - 9z^2 + 14z - 5 = (z^2 - 4z + 5)(2z - 1)$$

Check:

$$(z^2 - 4z + 5)(2z - 1) = 2z^3 - z^2 - 8z^2 + 4z + 10z - 5 = 2z^3 - 9z^2 + 14z - 5 \quad\checkmark$$

The remaining root is

$$2z - 1 = 0 \implies z = \frac{1}{2}$$

Therefore the roots are

$$z = 2 - i, \qquad z = 2 + i, \qquad z = \frac{1}{2} \quad\checkmark$$

**What the examiner wants:** the factor $2z - 1$ (not $z - 1/2$ with a missing factor of $2$), and all three roots.

### Example 32 - Medium - An equation with $z$ and $z^*$

> **Question:** Solve
> $$z + 2z^* = 6 + 3i$$

**Solution:**

Let $z = x + iy$. Then $z^* = x - iy$, so

$$z + 2z^* = (x + iy) + 2(x - iy) = 3x - iy$$

Equate to $6 + 3i$:

$$3x = 6 \implies x = 2$$

$$-y = 3 \implies y = -3$$

Therefore

$$z = 2 - 3i \quad\checkmark$$

**What the examiner wants:** the substitution $z = x + iy$ and the equating of real and imaginary parts. Do not treat $z^*$ as an independent variable.

### Example 33 - Medium - Solving $z^2 = a + bi$

> **Question:** Solve $z^2 = 3 - 4i$.

**Solution:**

Let $z = x + iy$. Then

$$x^2 - y^2 = 3 \quad \text{(1)}$$

$$2xy = -4 \implies xy = -2 \quad \text{(2)}$$

$$x^2 + y^2 = \sqrt{3^2 + (-4)^2} = 5 \quad \text{(3)}$$

Add (1) and (3):

$$2x^2 = 8 \implies x^2 = 4 \implies x = \pm 2$$

Subtract (1) from (3):

$$2y^2 = 2 \implies y^2 = 1 \implies y = \pm 1$$

Since $xy = -2 < 0$, $x$ and $y$ have opposite signs:

$$(x, y) = (2, -1) \text{ or } (-2, 1)$$

Therefore

$$z = \pm(2 - i) \quad\checkmark$$

Check: $(2 - i)^2 = 4 - 4i + i^2 = 3 - 4i$.

**What the examiner wants:** both roots, with the opposite-sign condition from $xy < 0$.

### Example 34 - Hard - A real quotient condition plus a modulus condition

> **Question:** The complex number $z$ satisfies
> $$\frac{z - 1}{z + i} \text{ is real} \qquad \text{and} \qquad |z| = 5$$
> Find the possible values of $z$ in the form $x + iy$.

**Solution:**

Let $z = x + iy$. Then

$$\frac{z - 1}{z + i} = \frac{(x - 1) + iy}{x + i(y + 1)}$$

The quotient is real exactly when its imaginary part is zero. Multiplying numerator and denominator by the conjugate of the denominator, the imaginary part of the numerator is

$$y(x) - (x - 1)(y + 1) = xy - (xy + x - y - 1) = -x + y + 1$$

Set this equal to zero:

$$-x + y + 1 = 0 \implies y = x - 1 \quad \text{(1)}$$

Now impose $|z| = 5$:

$$x^2 + y^2 = 25$$

Substitute (1):

$$x^2 + (x - 1)^2 = 25$$

$$2x^2 - 2x + 1 = 25$$

$$2x^2 - 2x - 24 = 0$$

$$x^2 - x - 12 = 0$$

$$(x - 4)(x + 3) = 0$$

So $x = 4$ or $x = -3$. From (1):

- If $x = 4$, $y = 3$, so $z = 4 + 3i$.
- If $x = -3$, $y = -4$, so $z = -3 - 4i$.

Therefore

$$z = 4 + 3i \quad \text{or} \quad z = -3 - 4i \quad\checkmark$$

Check: for $z = 4 + 3i$,

$$\frac{3 + 3i}{4 + 4i} = \frac{3(1 + i)}{4(1 + i)} = \frac{3}{4}$$

which is real. For $z = -3 - 4i$,

$$\frac{-4 - 4i}{-3 - 3i} = \frac{4(1 + i)}{3(1 + i)} = \frac{4}{3}$$

which is also real.

**What the examiner wants:** the imaginary-part condition simplified to a line, then intersected with the circle. This is a loci problem in disguise.

### Example 35 - Hard - A cubic with a given complex root

> **Question:** The equation $z^3 - 9z^2 + 31z - 39 = 0$ has real coefficients and $3 + 2i$ is a root. Find all the roots.

**Solution:**

The conjugate $3 - 2i$ is also a root. Form the quadratic factor:

$$(z - (3 + 2i))(z - (3 - 2i)) = (z - 3)^2 + 4 = z^2 - 6z + 13$$

Divide the cubic:

$$z^3 - 9z^2 + 31z - 39 = (z^2 - 6z + 13)(z - 3)$$

Check:

$$(z^2 - 6z + 13)(z - 3) = z^3 - 3z^2 - 6z^2 + 18z + 13z - 39 = z^3 - 9z^2 + 31z - 39 \quad\checkmark$$

The remaining root is $z = 3$. Therefore the roots are

$$z = 3 + 2i, \qquad z = 3 - 2i, \qquad z = 3 \quad\checkmark$$

**What the examiner wants:** the real quadratic factor, the division, and the third root. Notice that the real root equals the real part of the complex pair here, but that is a coincidence of the numbers, not a general rule.

### Example 36 - Hard - A purely imaginary quotient as a locus

> **Question:** The complex number $z$ satisfies
> $$\frac{z + 1}{z - 1} \text{ is purely imaginary}$$
> Find the locus of $z$.

**Solution:**

Let $z = x + iy$. Then

$$\frac{z + 1}{z - 1} = \frac{(x + 1) + iy}{(x - 1) + iy}$$

Multiply numerator and denominator by $(x - 1) - iy$. The real part of the numerator is

$$(x + 1)(x - 1) + y^2 = x^2 - 1 + y^2$$

The denominator is $(x - 1)^2 + y^2 > 0$ for $z \neq 1$.

For the quotient to be purely imaginary, the real part must be zero:

$$x^2 + y^2 - 1 = 0 \implies x^2 + y^2 = 1$$

Therefore the locus is the unit circle $|z| = 1$, with the point $z = 1$ excluded because the denominator would be zero. $\checkmark$

**What the examiner wants:** the real part isolated, the condition "purely imaginary" translated to "real part $= 0$", and the excluded point stated.

### Practice Questions - Part 5

1. (Easy) The equation $z^2 + pz + q = 0$ has real coefficients and $1 - 2i$ is a root. Find $p$ and $q$.
2. (Easy) Solve $z^2 + 4z + 13 = 0$.
3. (Medium) The equation $z^3 - 5z^2 + 9z - 5 = 0$ has real coefficients and $2 + i$ is a root. Find all the roots.
4. (Medium) Solve $z - 2z^* = 3 + 4i$.
5. (Medium) Solve $z^2 = -8 + 6i$.
6. (Medium) The equation $z^3 - 3z^2 + 5z - 3 = 0$ has real coefficients and $1 + \sqrt{2}i$ is a root. Find all the roots.
7. (Easy) Solve $z^2 - 2z + 2 = 0$.
8. (Hard) The equation $z^3 - 4z^2 + 6z - 4 = 0$ has real coefficients and $1 + i$ is a root. Find all the roots.

**Solutions:**

Question 1:

The conjugate $1 + 2i$ is also a root.

$$\text{sum} = 2 = -p \implies p = -2$$

$$\text{product} = (1 - 2i)(1 + 2i) = 1 + 4 = 5 = q$$

Question 2:

$$\Delta = 16 - 52 = -36$$

$$z = \frac{-4 \pm 6i}{2} = -2 \pm 3i$$

Question 3:

The conjugate $2 - i$ is also a root. Quadratic factor:

$$(z - (2 + i))(z - (2 - i)) = (z - 2)^2 + 1 = z^2 - 4z + 5$$

Divide:

$$z^3 - 5z^2 + 9z - 5 = (z^2 - 4z + 5)(z - 1)$$

Roots:

$$z = 2 + i, \qquad z = 2 - i, \qquad z = 1$$

Question 4:

$$z - 2z^* = (x + iy) - 2(x - iy) = -x + 3iy$$

Equate to $3 + 4i$:

$$-x = 3 \implies x = -3$$

$$3y = 4 \implies y = \frac{4}{3}$$

$$z = -3 + \frac{4}{3}i$$

Question 5:

$$x^2 - y^2 = -8, \qquad 2xy = 6 \implies xy = 3, \qquad x^2 + y^2 = 10$$

$$x^2 = 1 \implies x = \pm 1, \qquad y^2 = 9 \implies y = \pm 3$$

Since $xy > 0$, the signs match:

$$z = \pm(1 + 3i)$$

Question 6:

The conjugate $1 - \sqrt{2}i$ is also a root. Quadratic factor:

$$(z - (1 + \sqrt{2}i))(z - (1 - \sqrt{2}i)) = (z - 1)^2 + 2 = z^2 - 2z + 3$$

Divide:

$$z^3 - 3z^2 + 5z - 3 = (z^2 - 2z + 3)(z - 1)$$

Roots:

$$z = 1 + \sqrt{2}i, \qquad z = 1 - \sqrt{2}i, \qquad z = 1$$

Question 7:

$$\Delta = 4 - 8 = -4$$

$$z = \frac{2 \pm 2i}{2} = 1 \pm i$$

Question 8:

The conjugate $1 - i$ is also a root. Quadratic factor:

$$(z - (1 + i))(z - (1 - i)) = (z - 1)^2 + 1 = z^2 - 2z + 2$$

Divide:

$$z^3 - 4z^2 + 6z - 4 = (z^2 - 2z + 2)(z - 2)$$

Roots:

$$z = 1 + i, \qquad z = 1 - i, \qquad z = 2$$

---

# PART 6: Full Exam-Style Questions

These questions combine several skills, just like a Paper 3 complex-number question. Attempt them with the solutions covered, then check your working line by line.

## Exam-Style Question 1 - Arithmetic, polar form and powers

> **Question:** The complex numbers are $z = 2 + 2i$ and $w = 1 - i\sqrt{3}$.
> (a) Find $\dfrac{z}{w}$ in the form $x + iy$. [3]
> (b) Write $z$, $w$ and $\dfrac{z}{w}$ in modulus-argument form. [5]
> (c) Hence find $z^4$. [2]

**Solution:**

Part (a) - multiply by the conjugate of $1 - i\sqrt{3}$:

$$\frac{z}{w} = \frac{2 + 2i}{1 - i\sqrt{3}} \cdot \frac{1 + i\sqrt{3}}{1 + i\sqrt{3}}$$

$$= \frac{(2 + 2i)(1 + i\sqrt{3})}{1 + 3}$$

$$= \frac{2 + 2i\sqrt{3} + 2i + 2i^2\sqrt{3}}{4}$$

$$= \frac{2 - 2\sqrt{3} + i(2\sqrt{3} + 2)}{4}$$

$$= \frac{1 - \sqrt{3}}{2} + \frac{1 + \sqrt{3}}{2}i \quad\checkmark$$

Part (b):

For $z = 2 + 2i$:

$$|z| = \sqrt{4 + 4} = 2\sqrt{2}, \qquad \arg z = \frac{\pi}{4}$$

$$z = 2\sqrt{2}\left(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4}\right) \quad\checkmark$$

For $w = 1 - i\sqrt{3}$:

$$|w| = \sqrt{1 + 3} = 2, \qquad \arg w = -\frac{\pi}{3}$$

$$w = 2\left(\cos\left(-\frac{\pi}{3}\right) + i\sin\left(-\frac{\pi}{3}\right)\right) \quad\checkmark$$

For the quotient:

$$\left|\frac{z}{w}\right| = \frac{2\sqrt{2}}{2} = \sqrt{2}$$

$$\arg\left(\frac{z}{w}\right) = \frac{\pi}{4} - \left(-\frac{\pi}{3}\right) = \frac{7\pi}{12}$$

$$\frac{z}{w} = \sqrt{2}\left(\cos\frac{7\pi}{12} + i\sin\frac{7\pi}{12}\right) \quad\checkmark$$

Part (c):

$$z^4 = (2\sqrt{2})^4\left(\cos\left(4 \cdot \frac{\pi}{4}\right) + i\sin\left(4 \cdot \frac{\pi}{4}\right)\right)$$

$$= 64(\cos\pi + i\sin\pi)$$

$$= -64 \quad\checkmark$$

**Examiner notes:** in part (a), the denominator becomes $1 + 3 = 4$, not $1 - 3$. In part (b), the argument of $w$ is negative because $w$ is in the fourth quadrant. In part (c), the modulus is raised to the fourth power: $(2\sqrt{2})^4 = 64$.

## Exam-Style Question 2 - A circle, maximum and minimum modulus

> **Question:** The point $z$ lies on the circle
> $$|z - 3 - 4i| = 2$$
> (a) State the centre and radius of the circle. [2]
> (b) Find the minimum and maximum possible values of $|z|$, and the points at which they occur. [4]
> (c) Describe the region $|z - 3 - 4i| \le 2$ with $\operatorname{Re} z \le 3$. [2]

**Solution:**

Part (a):

$$|z - (3 + 4i)| = 2$$

The centre is $3 + 4i$, i.e. $(3, 4)$, and the radius is $2$. $\checkmark$

Part (b):

The distance from the origin to the centre is

$$|3 + 4i| = 5$$

The nearest and farthest points lie on the line through the origin and the centre. Therefore

$$|z|_{\min} = 5 - 2 = 3, \qquad |z|_{\max} = 5 + 2 = 7 \quad\checkmark$$

The direction from the origin to the centre is the unit vector

$$\frac{1}{5}(3 + 4i) = \frac{3}{5} + \frac{4}{5}i$$

The farthest point is

$$z_{\max} = (3 + 4i) + 2\left(\frac{3}{5} + \frac{4}{5}i\right)$$

$$= 3 + \frac{6}{5} + i\left(4 + \frac{8}{5}\right) = \frac{21}{5} + \frac{28}{5}i$$

The nearest point is

$$z_{\min} = (3 + 4i) - 2\left(\frac{3}{5} + \frac{4}{5}i\right)$$

$$= 3 - \frac{6}{5} + i\left(4 - \frac{8}{5}\right) = \frac{9}{5} + \frac{12}{5}i \quad\checkmark$$

Part (c) - the inequality $|z - 3 - 4i| \le 2$ is the closed disc with centre $(3, 4)$ and radius $2$. The condition $\operatorname{Re} z \le 3$ is the left half-plane bounded by the vertical line $x = 3$. The required region is the left half of the disc, including the diameter on $x = 3$ and the circular boundary. $\checkmark$

**Examiner notes:** the nearest and farthest points are not vertically above or below the centre; they lie on the line through the origin and the centre. Part (c) needs the intersection of the two regions, not either one alone.

## Exam-Style Question 3 - A cubic with a complex root

> **Question:** The equation
> $$z^3 - 5z^2 + 11z - 15 = 0$$
> has real coefficients and $1 + 2i$ is a root.
> (a) Write down the conjugate root. [1]
> (b) Form the real quadratic factor corresponding to the conjugate pair. [2]
> (c) Find all the roots of the cubic. [4]

**Solution:**

Part (a): the conjugate is

$$1 - 2i \quad\checkmark$$

Part (b):

$$(z - (1 + 2i))(z - (1 - 2i)) = (z - 1)^2 + 4$$

$$= z^2 - 2z + 1 + 4 = z^2 - 2z + 5 \quad\checkmark$$

Part (c) - divide the cubic by $z^2 - 2z + 5$. By inspection,

$$z^3 - 5z^2 + 11z - 15 = (z^2 - 2z + 5)(z - 3)$$

Check:

$$(z^2 - 2z + 5)(z - 3) = z^3 - 3z^2 - 2z^2 + 6z + 5z - 15 = z^3 - 5z^2 + 11z - 15 \quad\checkmark$$

The remaining root is $z = 3$. Therefore the roots are

$$z = 1 + 2i, \qquad z = 1 - 2i, \qquad z = 3 \quad\checkmark$$

**Examiner notes:** the quadratic factor must have real coefficients. Expand $(z - 1)^2 + 4$, not $(z - 1)^2 - 4$. State all three roots.

## Exam-Style Question 4 - Locus and minimum distance

> **Question:** The complex number $z$ satisfies
> $$|z - 2| = |z - 4i|$$
> (a) Find the Cartesian equation of the locus. [3]
> (b) Find the exact minimum value of $|z|$. [3]

**Solution:**

Part (a) - let $z = x + iy$:

$$|(x - 2) + iy| = |x + i(y - 4)|$$

Square:

$$(x - 2)^2 + y^2 = x^2 + (y - 4)^2$$

Expand:

$$x^2 - 4x + 4 + y^2 = x^2 + y^2 - 8y + 16$$

Cancel:

$$-4x + 4 = -8y + 16$$

$$4x - 8y + 12 = 0$$

Divide by $4$:

$$x - 2y + 3 = 0 \quad\checkmark$$

This is the perpendicular bisector of the segment joining $(2, 0)$ and $(0, 4)$.

Part (b) - the minimum $|z|$ is the perpendicular distance from the origin to the line

$$x - 2y + 3 = 0$$

Using the distance formula:

$$|z|_{\min} = \frac{|0 - 0 + 3|}{\sqrt{1^2 + (-2)^2}} = \frac{3}{\sqrt{5}} = \frac{3\sqrt{5}}{5} \quad\checkmark$$

**Examiner notes:** part (a) is the standard perpendicular-bisector derivation. Part (b) uses the distance from a point to a line; the foot of the perpendicular is $\left(-\frac{3}{5}, \frac{6}{5}\right)$, but the question only asks for the distance.

---

# Formula Sheet

**Cartesian form:**

$$z = x + iy, \qquad \operatorname{Re} z = x, \qquad \operatorname{Im} z = y$$

$$i^2 = -1, \qquad z^* = x - iy$$

$$zz^* = x^2 + y^2 = |z|^2$$

$$\frac{z_1}{z_2} = \frac{z_1 z_2^*}{|z_2|^2}$$

**Modulus and argument:**

$$|z| = \sqrt{x^2 + y^2}$$

$$\arg z = \theta, \qquad -\pi < \theta \le \pi \text{ (principal)}$$

$$\tan\alpha = \left|\frac{y}{x}\right|, \qquad \theta \text{ adjusted by quadrant}$$

**Polar form:**

$$z = r(\cos\theta + i\sin\theta) = r\operatorname{cis}\theta = re^{i\theta}$$

$$z^* = r(\cos\theta - i\sin\theta) = re^{-i\theta}$$

**Multiplication and division:**

$$z_1z_2 = r_1r_2\left(\cos(\theta_1 + \theta_2) + i\sin(\theta_1 + \theta_2)\right)$$

$$\frac{z_1}{z_2} = \frac{r_1}{r_2}\left(\cos(\theta_1 - \theta_2) + i\sin(\theta_1 - \theta_2)\right)$$

$$|z_1z_2| = |z_1||z_2|, \qquad \left|\frac{z_1}{z_2}\right| = \frac{|z_1|}{|z_2|}$$

$$\arg(z_1z_2) = \arg z_1 + \arg z_2, \qquad \arg\left(\frac{z_1}{z_2}\right) = \arg z_1 - \arg z_2$$

**Powers and roots:**

$$z^n = r^n\left(\cos(n\theta) + i\sin(n\theta)\right)$$

$$\sqrt{a + bi}: \quad x^2 - y^2 = a, \quad 2xy = b, \quad x^2 + y^2 = \sqrt{a^2 + b^2}$$

**Loci:**

| Equation | Locus |
|---|---|
| $\lvert z - z_0\rvert = r$ | circle, centre $z_0$, radius $r$ |
| $\lvert z - z_0\rvert < r$ | inside the circle |
| $\lvert z - z_1\rvert = \lvert z - z_2\rvert$ | perpendicular bisector of $z_1z_2$ |
| $\arg(z - z_0) = \theta$ | half-line from $z_0$ at angle $\theta$ |
| $\alpha < \arg(z - z_0) < \beta$ | sector between two half-lines |

**Maximum and minimum modulus on a circle:**

$$|z|_{\min} = \bigl|\,|z_0| - r\,\bigr|, \qquad |z|_{\max} = |z_0| + r$$

**Conjugate pairs:**

If $a + bi$ is a root of a polynomial with real coefficients, then $a - bi$ is also a root. The real quadratic factor is

$$z^2 - 2az + (a^2 + b^2)$$

**Geometric effects:**

| Transformation | Effect |
|---|---|
| $z \mapsto z + w$ | translation by $w$ |
| $z \mapsto z^*$ | reflection in the real axis |
| $z \mapsto iz$ | rotation by $\frac{\pi}{2}$ anticlockwise |
| $z \mapsto wz$ | scale by $\lvert w\rvert$, rotate by $\arg w$ |
| $z \mapsto z/w$ | scale by $1/\lvert w\rvert$, rotate by $-\arg w$ |

---

# Quick Reference Card

- **Basics:** $i^2=-1$; $z=x+iy$; $\operatorname{Re}z=x$, $\operatorname{Im}z=y$; equality means both parts match.
- **Conjugate:** $z^*=x-iy$. It reflects in the real axis. $zz^*=|z|^2$, $z+z^*=2x$, $z-z^*=2iy$.
- **Division:** multiply numerator and denominator by the conjugate of the denominator. The denominator becomes $|z_2|^2$.
- **Powers of $i$:** cycle $i,-1,-i,1$. Reduce the exponent modulo $4$.
- **Modulus:** $|z|=\sqrt{x^2+y^2}$; $|z_1-z_2|$ is the distance between the points.
- **Argument:** angle from the positive real axis. Locate the quadrant first; $\tan^{-1}(y/x)$ alone is not enough. Principal interval $-\pi<\theta\le\pi$.
- **Polar form:** $z=r(\cos\theta+i\sin\theta)=r\operatorname{cis}\theta=re^{i\theta}$; $r=|z|$, $\theta=\arg z$.
- **Multiplication:** multiply moduli, add arguments. **Division:** divide moduli, subtract arguments.
- **Powers:** $z^n=r^n\operatorname{cis}(n\theta)$; reduce the angle modulo $2\pi$ before evaluating.
- **Square roots:** solve $x^2-y^2=a$, $2xy=b$, $x^2+y^2=\sqrt{a^2+b^2}$; use the sign of $b$ to pair $x$ and $y$; give both $\pm$ roots.
- **Circle:** $|z-z_0|=r$ has centre $z_0$, radius $r$; $<$ is the inside, $>$ is the outside.
- **Perpendicular bisector:** $|z-z_1|=|z-z_2|$; square both sides and cancel the quadratics.
- **Half-line:** $\arg(z-z_0)=\theta$ starts at $z_0$; the vertex is excluded.
- **Sector:** $\alpha<\arg(z-z_0)<\beta$ is the wedge between the two half-lines.
- **Max/min modulus:** for $|z-z_0|=r$, the values are $|z_0|\pm r$ (taking the absolute value of the difference if necessary). The points lie on the line through the origin and $z_0$.
- **Conjugate pairs:** real coefficients mean non-real roots occur in pairs $a\pm bi$; the quadratic factor is $z^2-2az+(a^2+b^2)$.
- **Cubic with one complex root:** write the conjugate, form the real quadratic, divide, solve the remaining linear factor.
- **Equations with $z$ and $z^*$:** substitute $z=x+iy$, $z^*=x-iy$, expand, equate real and imaginary parts.
- **Geometric effects:** conjugation reflects in the real axis; multiplication by $i$ rotates $90^\circ$ anticlockwise; multiplication by $w$ scales by $|w|$ and rotates by $\arg w$.
- **Exam habits:** exact values (no decimals unless asked); radians in P3; state both roots; state the excluded point for half-lines; draw the Argand diagram before describing a region.

---

*Sources: Cambridge International AS & A Level Mathematics 9709 syllabus (2026-2027), topic 3.9 Complex numbers; Cambridge 9709 Paper 3 past papers, including 9709/31/M/J/25 Q3, 9709/32/M/J/25 Q3 and 9709/33/O/N/25 Q4. All numerical answers were checked by direct computation.*
