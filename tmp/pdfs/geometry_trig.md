This guide covers the four Geometry & Trigonometry skill areas: area and volume, lines and angles, triangles and trigonometry, and circles. The domain typically accounts for about 5–7 of the 44 SAT Math questions.

The sections organize key relationships, worked examples, and common traps into a practical problem-solving reference.

---

\newpage

# Part 0: THE MASTER GEOMETRY DECISION TREE

Before solving anything, classify the problem.

| You see | First thought |
|---|---|
| Rectangle/triangle/circle/shaded region | Area or perimeter |
| 3D solid | Volume or surface area |
| Similar figures | Find scale factor \(k\) |
| Intersecting lines | Vertical/supplementary angles |
| Parallel lines + transversal | Corresponding/alternate/same-side |
| Triangle | \(180^\circ\), similarity, Pythagoras, etc. |
| Right triangle | Pythagoras, special triangle, or trig |
| \(30^\circ,60^\circ,90^\circ\) | 30-60-90 |
| \(45^\circ,45^\circ,90^\circ\) | 45-45-90 |
| Height/distance + angle | SOHCAHTOA |
| Angle of elevation/depression | Draw right triangle |
| Point on circle + angle | Unit-circle trig |
| Circle equation | Center signs + square root of RHS |
| Tangent | Radius perpendicular to tangent |
| Inscribed angle | Half intercepted arc |
| Sector/arc | Fraction of whole circle |
| \(s=r\theta\) | \(\theta\) must be radians |

Use this trigger sheet to identify a likely solution path before starting calculations.

---

# Part I: AREA AND PERIMETER

## 1. The difference between area and perimeter

**Perimeter** is the distance around a 2D shape.

Units:

\[
\text{cm},\quad \text{ft},\quad \text{m}
\]

**Area** is the amount of 2D space inside.

Units:

\[
\text{cm}^2,\quad \text{ft}^2,\quad \text{m}^2.
\]

Never mix them.

A skinny long rectangle can have a large perimeter and relatively small area.

---

## 2. Rectangle

Area:

\[
\boxed{A=lw}
\]

Perimeter:

\[
\boxed{P=2l+2w}
\]

Example:

\[
l=12,\qquad w=5.
\]

Area:

\[
12(5)=\boxed{60}
\]

Perimeter:

\[
2(12)+2(5)=24+10=\boxed{34}.
\]

---

## 3. Square

Area:

\[
\boxed{A=s^2}
\]

Perimeter:

\[
\boxed{P=4s}.
\]

Example:

Square perimeter:

\[
28.
\]

Then:

\[
s=\frac{28}{4}=7.
\]

Area:

\[
7^2=\boxed{49}.
\]

---

## 4. Triangle area

\[
\boxed{A=\frac12 bh}
\]

The height must be **perpendicular** to the base.

That is crucial.

A slanted side is not automatically the height.

Example:

\[
b=12,\quad h=7.
\]

\[
A=\frac12(12)(7)=\boxed{42}.
\]

---

## 5. Parallelogram

\[
\boxed{A=bh}
\]

Again, \(h\) is perpendicular height.

If the base is \(10\), slanted side \(8\), perpendicular height \(6\):

\[
A=10(6)=60.
\]

Not:

\[
10(8).
\]

---

## 6. Trapezoid

\[
\boxed{
A=\frac12(b_1+b_2)h
}
\]

Think:

average of parallel bases × height.

Example:

\[
b_1=8,\quad b_2=12,\quad h=5.
\]

\[
A=
\frac12(8+12)(5)
=
\frac12(20)(5)
=
\boxed{50}.
\]

---

## 7. Circle

Area:

\[
\boxed{A=\pi r^2}
\]

Circumference:

\[
\boxed{C=2\pi r}
\]

or:

\[
\boxed{C=\pi d}.
\]

The first circle check should always be:

> Did they give me radius or diameter?

If diameter:

\[
d=14,
\]

then:

\[
r=7.
\]

Area:

\[
49\pi.
\]

Circumference:

\[
14\pi.
\]

Your manual explicitly flags confusing radius/diameter and circumference/area as major traps.

---

## 8. Composite figures

A composite figure is made from basic shapes.

Your strategy:

1. Identify pieces.
2. Calculate each piece separately.
3. Add if pieces are joined.
4. Subtract if something is removed.

Example:

Rectangle:

\[
10\times4.
\]

Semicircle removed from short side.

Short side = diameter \(4\), so:

\[
r=2.
\]

Rectangle:

\[
40.
\]

Full circle:

\[
\pi(2)^2=4\pi.
\]

Semicircle:

\[
2\pi.
\]

Remaining area:

\[
\boxed{40-2\pi}.
\]

### Trap

Do not forget:

\[
\boxed{\text{semicircle}=\frac12(\text{circle})}.
\]

---

## 9. Cutout example

Large rectangle:

\[
12\times8=96.
\]

Square corner removed:

\[
4\times4=16.
\]

Remaining:

\[
96-16=\boxed{80}.
\]

---

# Part II: VOLUME AND SURFACE AREA

## 10. Volume versus surface area

Volume = space **inside**.

Units:

\[
\text{cm}^3,\quad\text{m}^3.
\]

Surface area = total area of exposed surfaces.

Units:

\[
\text{cm}^2,\quad\text{m}^2.
\]

---

## 11. The one volume idea that simplifies everything

For a prism:

\[
\boxed{V=Bh}
\]

where \(B\) = area of base.

For pyramid/cone:

\[
\boxed{V=\frac13Bh}.
\]

That explains many formulas automatically.

Your manual explicitly uses this as the organizing principle.

---

## 12. Rectangular prism

\[
\boxed{V=lwh}.
\]

Example:

\[
l=4,\quad w=5,\quad h=7.
\]

\[
V=4(5)(7)=\boxed{140}.
\]

Surface area:

\[
\boxed{SA=2lw+2lh+2wh}.
\]

---

## 13. Cube

Volume:

\[
\boxed{V=s^3}.
\]

Surface area:

\[
\boxed{SA=6s^2}.
\]

---

## 14. Cylinder

\[
\boxed{V=\pi r^2h}.
\]

It is just:

circle base area × height.

Example:

\[
r=3,\quad h=8.
\]

\[
V=\pi(3)^2(8)
\]

\[
=\boxed{72\pi}.
\]

### Surface area

Two circular ends:

\[
2\pi r^2.
\]

Curved side:

\[
2\pi rh.
\]

Total:

\[
\boxed{SA=2\pi r^2+2\pi rh}.
\]

---

## 15. Cone

\[
\boxed{
V=\frac13\pi r^2h
}
\]

Example:

\[
r=5,\quad h=12.
\]

\[
V=
\frac13\pi(25)(12)
=
\boxed{100\pi}.
\]

Remember:

cone = one-third of cylinder with same base and height.

---

## 16. Pyramid

\[
\boxed{V=\frac13Bh}.
\]

\(B\) is the area of the base.

---

## 17. Sphere

\[
\boxed{
V=\frac43\pi r^3
}
\]

Example:

\[
r=6.
\]

\[
V=
\frac43\pi(216)
=
\boxed{288\pi}.
\]

Sphere surface area:

\[
\boxed{SA=4\pi r^2}.
\]

---

## 18. Hemisphere

Half a sphere:

\[
\boxed{
V=\frac12\left(\frac43\pi r^3\right)
}
\]

Example \(r=3\):

\[
V=
\frac12(36\pi)
=
18\pi.
\]

---

# Part III: SCALE FACTORS

This is one of the most important concepts in B4.

## 19. The \(k,k^2,k^3\) rule

If all linear dimensions scale by \(k\):

\[
\boxed{\text{length/perimeter}\times k}
\]

\[
\boxed{\text{area}\times k^2}
\]

\[
\boxed{\text{volume}\times k^3}.
\]

Your source calls this the single most important rule in this part of the domain.

---

## 20. Example: similar squares

Original side:

\[
3.
\]

New side:

\[
9.
\]

Scale factor:

\[
k=\frac93=3.
\]

Area scale factor:

\[
3^2=9.
\]

So new area is 9 times old area.

---

## 21. Similar solids

Two similar cylinders:

\[
r_1=2,\quad r_2=6.
\]

So:

\[
k=3.
\]

Volume ratio:

\[
3^3=27.
\]

If smaller volume is:

\[
10\pi,
\]

larger:

\[
27(10\pi)=\boxed{270\pi}.
\]

---

## 22. Reverse scaling

Suppose volume increases by factor 8.

Find linear scale factor.

\[
k^3=8.
\]

\[
k=2.
\]

Therefore area increases by:

\[
k^2=4.
\]

---

## 23. Different dimensions scaling differently

Suppose a cone's radius triples and its height halves.

Original:

\[
V=\frac13\pi r^2h.
\]

Radius effect:

\[
3^2=9.
\]

Height effect:

\[
\frac12.
\]

Combined:

\[
9\cdot\frac12
=
\boxed{\frac92}.
\]

New volume:

\[
\boxed{\frac92V}.
\]

This is different from similar-figure scaling because not every dimension changed by same factor.

---

## 24. Conservation of volume

Cylinder 1:

\[
r=4,\quad h=10.
\]

Poured into cylinder 2:

\[
r=8,\quad h=x.
\]

Same water volume:

\[
\pi(4)^2(10)
=
\pi(8)^2x.
\]

\[
160\pi=64\pi x.
\]

\[
x=\boxed{2.5}.
\]

Doubling radius made base area 4 times larger, so water height becomes one-fourth.

---

# Part IV: ANGLES

## 25. Complementary angles

\[
\boxed{\text{sum}=90^\circ}
\]

Example:

one is \(32^\circ\).

Other:

\[
90-32=\boxed{58^\circ}.
\]

---

## 26. Supplementary angles

\[
\boxed{\text{sum}=180^\circ}
\]

---

## 27. Vertical angles

When two lines intersect:

opposite angles are equal.

\[
\boxed{\text{vertical angles are equal}}.
\]

If one is:

\[
47^\circ,
\]

opposite is:

\[
\boxed{47^\circ}.
\]

---

## 28. Linear pair

Adjacent angles forming a straight line:

\[
\boxed{\text{sum}=180^\circ}.
\]

Example:

\[
4x+10
\]

and:

\[
2x+20.
\]

\[
(4x+10)+(2x+20)=180.
\]

\[
6x+30=180.
\]

\[
x=25.
\]

Angles:

\[
110^\circ,\quad70^\circ.
\]

---

# Part V: PARALLEL LINES AND TRANSVERSALS

When parallel lines are cut by a transversal:

## 29. The three equal relationships

These are equal:

\[
\boxed{\text{corresponding angles}}
\]

\[
\boxed{\text{alternate interior angles}}
\]

\[
\boxed{\text{alternate exterior angles}}.
\]

---

## 30. Same-side interior

These are supplementary:

\[
\boxed{\text{sum}=180^\circ}.
\]

This is the relationship most students mix up.

Your manual gives exactly this split: corresponding/alternate angles equal, same-side interior supplementary.

---

## 31. Example: corresponding

\[
3x-20=x+40.
\]

\[
2x=60.
\]

\[
\boxed{x=30}.
\]

---

## 32. Example: same-side interior

\[
2x+30
\]

and:

\[
3x+10.
\]

Add:

\[
5x+40=180.
\]

\[
5x=140.
\]

\[
\boxed{x=28}.
\]

---

# Part VI: TRIANGLES

## 33. Triangle angle sum

\[
\boxed{A+B+C=180^\circ}.
\]

Example:

\[
50^\circ,\quad65^\circ.
\]

Third:

\[
180-50-65
=
\boxed{65^\circ}.
\]

---

## 34. Exterior angle theorem

An exterior angle equals the sum of the two **remote interior angles**.

Example:

exterior:

\[
120^\circ.
\]

Remote interior:

\[
45^\circ,\quad x.
\]

Then:

\[
45+x=120.
\]

\[
\boxed{x=75^\circ}.
\]

Do not use the adjacent interior angle as one of the remote angles.

---

## 35. Isosceles triangles

Two equal sides imply two equal base angles.

Suppose vertex angle:

\[
40^\circ.
\]

Remaining total:

\[
180-40=140.
\]

Divide equally:

\[
\boxed{70^\circ,70^\circ}.
\]

---

## 36. Equilateral triangle

All sides equal.

All angles:

\[
\boxed{60^\circ}.
\]

Height:

\[
\boxed{h=\frac{s\sqrt3}{2}}.
\]

Area:

\[
\boxed{A=\frac{s^2\sqrt3}{4}}.
\]

These come from splitting an equilateral triangle into two 30-60-90 triangles.

---

## 37. Triangle inequality

For side lengths:

\[
a,b,c,
\]

you need:

\[
a+b>c,
\]

\[
a+c>b,
\]

\[
b+c>a.
\]

Strictly greater than.

Not:

\[
\ge.
\]

Example:

\[
5,7,13.
\]

Check two smaller:

\[
5+7=12.
\]

But:

\[
12<13.
\]

So:

\[
\boxed{\text{not a triangle}}.
\]

Fast method: check whether the two smallest sides sum to more than the largest.

---

# Part VII: SIMILAR TRIANGLES

## 38. What similarity means

Same shape, potentially different size.

Corresponding angles equal.

Corresponding sides proportional.

\[
\boxed{
\frac{a_1}{a_2}
=
\frac{b_1}{b_2}
=
\frac{c_1}{c_2}
}
\]

---

## 39. AA similarity

If two angle pairs are equal:

\[
\boxed{\text{triangles are similar}}.
\]

A third angle automatically matches because triangle angles sum to 180.

---

## 40. Similar triangle scale factor

Suppose:

\[
AB=6,\quad DE=9.
\]

Then:

\[
k=\frac96=1.5.
\]

If corresponding side:

\[
BC=8,
\]

then:

\[
EF=8(1.5)=\boxed{12}.
\]

---

## 41. Area of similar triangles

If side scale factor:

\[
k,
\]

area ratio:

\[
\boxed{k^2}.
\]

Suppose small-to-big side ratio:

\[
\frac14.
\]

Then small-to-big area ratio:

\[
\frac1{16}.
\]

If small area:

\[
5,
\]

big area:

\[
5(16)=\boxed{80}.
\]

---

## 42. Parallel segment inside a triangle

If:

\[
DE\parallel BC,
\]

then:

\[
\triangle ADE\sim\triangle ABC.
\]

Suppose:

\[
AD=4,\quad DB=8.
\]

Then whole:

\[
AB=12.
\]

Small-to-big factor:

\[
\frac{AD}{AB}
=
\frac4{12}
=
\frac13.
\]

If:

\[
DE=6,
\]

then:

\[
BC=18.
\]

### Classic trap

Using \(AD/DB\) rather than \(AD/AB\).

---

## 43. Shadow problems

Same sun angle creates similar triangles.

Tree:

height \(10\),

shadow \(5\).

Building shadow:

\(40\).

\[
\frac{10}{5}
=
\frac{h}{40}.
\]

\[
2=\frac h{40}.
\]

\[
\boxed{h=80}.
\]

Your guide identifies shadow problems and parallel segments as standard SAT similarity setups.

---

# Part VIII: CONGRUENT TRIANGLES

Similar:

same shape.

Congruent:

same shape **and same size**.

## 44. Valid congruence information

You should recognize:

\[
\boxed{SSS}
\]

\[
\boxed{SAS}
\]

\[
\boxed{ASA}
\]

\[
\boxed{AAS}
\]

\[
\boxed{HL\text{ for right triangles}}.
\]

---

## 45. SSA is generally NOT sufficient

Two sides and a non-included angle can sometimes make two different triangles.

Therefore:

\[
\boxed{SSA\text{ generally does not prove congruence}}.
\]

Exception-type idea:

right triangle HL.

---

## 46. SAS example

Given:

\[
AB=DE,
\]

\[
BC=EF,
\]

and:

\[
\angle B=\angle E,
\]

where the angle lies between the given sides.

That is:

\[
\boxed{SAS}.
\]

---

## 47. HL

For right triangles:

same hypotenuse + same leg:

\[
\boxed{\text{congruent}}.
\]

Example:

hypotenuse \(13\),

leg \(5\).

Other leg is forced:

\[
\sqrt{13^2-5^2}
=
\sqrt{169-25}
=
12.
\]

Both triangles become 5-12-13.

---

# Part IX: PYTHAGOREAN THEOREM

## 48. Formula

For a right triangle:

\[
\boxed{a^2+b^2=c^2}.
\]

\(c\) must be the **hypotenuse**.

The hypotenuse:

- opposite the right angle
- longest side.

---

## 49. Missing hypotenuse

Legs:

\[
9,12.
\]

\[
c^2=9^2+12^2.
\]

\[
c^2=81+144=225.
\]

\[
\boxed{c=15}.
\]

---

## 50. Missing leg

Hypotenuse:

\[
13.
\]

One leg:

\[
5.
\]

\[
x^2+25=169.
\]

\[
x^2=144.
\]

\[
\boxed{x=12}.
\]

For a leg:

\[
\boxed{a=\sqrt{c^2-b^2}}
\]

not plus.

---

## 51. Pythagorean triples

Recognize these instantly:

\[
\boxed{3-4-5}
\]

\[
\boxed{5-12-13}
\]

\[
\boxed{8-15-17}
\]

\[
\boxed{7-24-25}.
\]

Multiples also work:

\[
6-8-10,
\]

\[
9-12-15,
\]

etc.

Your source explicitly recommends instant recognition of these triples.

---

## 52. Converse

If side lengths satisfy:

\[
a^2+b^2=c^2,
\]

the triangle is right.

Supplementary classification:

\[
a^2+b^2>c^2
\]

acute.

\[
a^2+b^2<c^2
\]

obtuse.

---

## 53. Space diagonal

For rectangular prism:

\[
\boxed{
d=\sqrt{l^2+w^2+h^2}
}
\]

Example:

\[
3,4,12.
\]

\[
d=
\sqrt{9+16+144}
=
\sqrt{169}
=
\boxed{13}.
\]

You can also do two Pythagorean steps:

3-4 gives 5.

Then 5-12 gives 13.

---

# Part X: SPECIAL RIGHT TRIANGLES

These must become automatic.

## 54. 45-45-90 triangle

Side ratio:

\[
\boxed{1:1:\sqrt2}.
\]

Or:

\[
\boxed{s:s:s\sqrt2}.
\]

The two legs are equal.

Hypotenuse:

\[
\boxed{s\sqrt2}.
\]

---

## 55. Example: given leg

Leg:

\[
7.
\]

Hypotenuse:

\[
\boxed{7\sqrt2}.
\]

---

## 56. Given hypotenuse

Hypotenuse:

\[
12.
\]

Then:

\[
s\sqrt2=12.
\]

\[
s=\frac{12}{\sqrt2}.
\]

Rationalize:

\[
s=\frac{12\sqrt2}{2}
=
\boxed{6\sqrt2}.
\]

### Important

Given hypotenuse, **divide** by \(\sqrt2\).

Do not multiply.

---

## 57. Square diagonal shortcut

Square side \(s\):

\[
d=s\sqrt2.
\]

So:

\[
s=\frac{d}{\sqrt2}.
\]

Area:

\[
s^2
=
\frac{d^2}{2}.
\]

Thus:

\[
\boxed{A_{\text{square}}=\frac{d^2}{2}}.
\]

If diagonal \(8\):

\[
A=\frac{64}{2}=\boxed{32}.
\]

---

## 58. 30-60-90 triangle

Ratio:

\[
\boxed{1:\sqrt3:2}.
\]

More precisely:

\[
\boxed{s:s\sqrt3:2s}.
\]

Where:

- \(s\) opposite \(30^\circ\)
- \(s\sqrt3\) opposite \(60^\circ\)
- \(2s\) is hypotenuse.

Memory:

**short, root-three, double.**

---

## 59. Given hypotenuse

Hypotenuse:

\[
18.
\]

Short leg:

\[
18/2=9.
\]

Long leg:

\[
\boxed{9\sqrt3}.
\]

---

## 60. Given short leg

Short leg:

\[
5.
\]

Long:

\[
5\sqrt3.
\]

Hypotenuse:

\[
10.
\]

---

## 61. Given long leg

Long leg:

\[
12.
\]

\[
s\sqrt3=12.
\]

\[
s=\frac{12}{\sqrt3}
=
4\sqrt3.
\]

Hypotenuse:

\[
2s
=
\boxed{8\sqrt3}.
\]

Your manual presents both special-triangle ratios as high-frequency SAT material.

---

# Part XI: SOHCAHTOA

This is the core trig skill.

## 62. Memorize

\[
\boxed{
\sin\theta=\frac{\text{opposite}}{\text{hypotenuse}}
}
\]

\[
\boxed{
\cos\theta=\frac{\text{adjacent}}{\text{hypotenuse}}
}
\]

\[
\boxed{
\tan\theta=\frac{\text{opposite}}{\text{adjacent}}
}
\]

Mnemonic:

\[
\boxed{\text{SOH CAH TOA}}
\]

Your manual notes these must be memorized.

---

## 63. Label sides relative to the angle

The hypotenuse never changes.

Opposite and adjacent **do** change depending on which acute angle you choose.

Before trig:

mark:

\[
O,\quad A,\quad H.
\]

This prevents most mistakes.

---

## 64. Example with 6-8-10

Hypotenuse:

\[
10.
\]

Angle \(\theta\) opposite side \(6\).

Then:

\[
O=6,\quad A=8,\quad H=10.
\]

So:

\[
\sin\theta=\frac6{10}=\boxed{\frac35}
\]

\[
\cos\theta=\frac8{10}=\boxed{\frac45}
\]

\[
\tan\theta=\frac68=\boxed{\frac34}.
\]

---

## 65. Finding a side

Right triangle:

\[
\theta=35^\circ,
\]

hypotenuse \(20\),

opposite side \(x\).

Use sine because O/H:

\[
\sin35^\circ=\frac{x}{20}.
\]

Therefore:

\[
x=20\sin35^\circ.
\]

Approximately:

\[
\boxed{11.47}.
\]

---

# Part XII: INVERSE TRIG

Regular trig:

angle then ratio.

Inverse trig:

ratio then angle.

## 66. Inverse sine

If:

\[
\sin\theta=\frac5{13},
\]

then:

\[
\boxed{
\theta=\sin^{-1}\left(\frac5{13}\right)
}
\]

---

## 67. Inverse tangent example

Right triangle legs:

opposite \(6\),

adjacent \(8\).

\[
\tan\theta=\frac68=.75.
\]

\[
\theta=\tan^{-1}(.75).
\]

\[
\boxed{\theta\approx36.9^\circ}.
\]

---

## 68. Major notation trap

\[
\sin^{-1}(x)
\]

means inverse sine.

It does **not** mean:

\[
\frac1{\sin x}.
\]

Reciprocal of sine is called cosecant, not inverse sine.

---

# Part XIII: COFUNCTIONS

In a right triangle, acute angles add to:

\[
90^\circ.
\]

Therefore:

\[
\boxed{
\sin\theta=\cos(90^\circ-\theta)
}
\]

and:

\[
\boxed{
\cos\theta=\sin(90^\circ-\theta)
}.
\]

Example:

If:

\[
\sin A=\frac35,
\]

and \(A+B=90^\circ\),

then:

\[
\boxed{\cos B=\frac35}.
\]

---

## 69. Algebraic cofunction problem

\[
\sin x=\cos2x
\]

for acute angles.

Since:

\[
\sin x=\cos(90^\circ-x),
\]

we have:

\[
90-x=2x.
\]

\[
90=3x.
\]

\[
\boxed{x=30^\circ}.
\]

---

# Part XIV: ANGLE OF ELEVATION AND DEPRESSION

## 70. Elevation

Angle measured **upward from horizontal**.

## 71. Depression

Angle measured **downward from horizontal**.

Not from vertical.

Your manual specifically warns about this.

---

## 72. Building example

You stand:

\[
60\text{ m}
\]

from building.

Angle elevation:

\[
40^\circ.
\]

Height \(h\).

Horizontal distance = adjacent.

Height = opposite.

Therefore:

\[
\tan40^\circ=\frac h{60}.
\]

\[
h=60\tan40^\circ.
\]

\[
\boxed{h\approx50.3\text{ m}}.
\]

---

## 73. Lighthouse depression

Lighthouse height:

\[
100.
\]

Angle of depression:

\[
30^\circ.
\]

The boat's angle of elevation is also:

\[
30^\circ
\]

because the horizontals are parallel.

Let horizontal distance be \(d\).

\[
\tan30^\circ=\frac{100}{d}.
\]

So:

\[
d=\frac{100}{\tan30^\circ}.
\]

Since:

\[
\tan30^\circ=\frac1{\sqrt3},
\]

\[
d=100\sqrt3.
\]

---

## 74. Line-of-sight/hypotenuse problems

Kite height:

\[
40.
\]

Angle:

\[
30^\circ.
\]

String length \(L\).

Height is opposite, string is hypotenuse.

Use sine:

\[
\sin30^\circ=\frac{40}{L}.
\]

\[
\frac12=\frac{40}{L}.
\]

\[
\boxed{L=80}.
\]

---

## 75. Two-observer problem

This is a hard SAT type.

At point A:

angle \(30^\circ\).

Walk 100 m closer to B:

angle \(60^\circ\).

Let distance from B to cliff = \(x\).

Height = \(h\).

From B:

\[
\tan60^\circ=\frac hx
\]

\[
h=x\sqrt3.
\]

From A:

distance = \(x+100\).

\[
\tan30^\circ=\frac h{x+100}.
\]

\[
h=\frac{x+100}{\sqrt3}.
\]

Set equal:

\[
x\sqrt3=\frac{x+100}{\sqrt3}.
\]

Multiply by \(\sqrt3\):

\[
3x=x+100.
\]

\[
2x=100.
\]

\[
x=50.
\]

Then:

\[
h=50\sqrt3.
\]

---

# Part XV: UNIT CIRCLE

## 76. The single most important unit-circle fact

For a point on the unit circle:

\[
\boxed{(x,y)=(\cos\theta,\sin\theta)}.
\]

So:

\[
\boxed{x=\cos\theta}
\]

\[
\boxed{y=\sin\theta}.
\]

And:

\[
\boxed{\tan\theta=\frac yx}.
\]

Your source states this directly.

---

## 77. Exact values to memorize

| \(\theta\) | \(\sin\theta\) | \(\cos\theta\) | \(\tan\theta\) |
|---:|---:|---:|---:|
| \(0^\circ\) | \(0\) | \(1\) | \(0\) |
| \(30^\circ\) | \(\frac12\) | \(\frac{\sqrt3}{2}\) | \(\frac{\sqrt3}{3}\) |
| \(45^\circ\) | \(\frac{\sqrt2}{2}\) | \(\frac{\sqrt2}{2}\) | \(1\) |
| \(60^\circ\) | \(\frac{\sqrt3}{2}\) | \(\frac12\) | \(\sqrt3\) |
| \(90^\circ\) | \(1\) | \(0\) | undefined |

These are explicitly listed in your guide.

---

## 78. Easy memory trick

Sine values for:

\[
0,30,45,60,90
\]

are:

\[
\frac{\sqrt0}{2},
\frac{\sqrt1}{2},
\frac{\sqrt2}{2},
\frac{\sqrt3}{2},
\frac{\sqrt4}{2}.
\]

Cosine is the same list backward.

That means you do not need to memorize ten unrelated values.

---

## 79. Quadrant signs

| Quadrant | \(x=\cos\) | \(y=\sin\) | \(\tan\) |
|---|---:|---:|---:|
| I | + | + | + |
| II | - | + | - |
| III | - | - | + |
| IV | + | - | - |

Mnemonic from your guide:

**All Students Take Calculus**

I: All positive

II: Sine positive

III: Tangent positive

IV: Cosine positive

---

## 80. Reference angle

Suppose:

\[
\cos\theta=-\frac{\sqrt2}{2}
\]

and \(\theta\) lies in QIII.

Magnitude:

\[
\frac{\sqrt2}{2}
\]

corresponds to reference angle:

\[
45^\circ.
\]

QIII angle:

\[
180+45
=
\boxed{225^\circ}.
\]

---

## 81. Radian quadrant example

\[
\cos\theta=\frac12
\]

in QIV.

Reference angle:

\[
60^\circ=\frac\pi3.
\]

QIV:

\[
2\pi-\frac\pi3
=
\boxed{\frac{5\pi}{3}}.
\]

---

## 82. Point given on unit circle

Point:

\[
\left(-\frac{12}{13},\frac5{13}\right).
\]

Then directly:

\[
\boxed{\cos\theta=-\frac{12}{13}}
\]

\[
\boxed{\sin\theta=\frac5{13}}
\]

and:

\[
\tan\theta
=
\frac{5/13}{-12/13}
=
\boxed{-\frac5{12}}.
\]

---

## 83. Point not on unit circle

Suppose terminal side passes through:

\[
(-3,4).
\]

Radius from origin:

\[
r=\sqrt{(-3)^2+4^2}=5.
\]

For a general circle:

\[
\boxed{\cos\theta=\frac xr}
\]

\[
\boxed{\sin\theta=\frac yr}.
\]

Thus:

\[
\cos\theta=-\frac35,
\]

\[
\sin\theta=\frac45.
\]

---

## 84. Coordinates from radius and angle

General circle radius \(r\):

\[
\boxed{
(x,y)=(r\cos\theta,r\sin\theta)
}
\]

Example:

\[
r=2,\quad\theta=30^\circ.
\]

\[
x=2\frac{\sqrt3}{2}=\sqrt3
\]

\[
y=2\frac12=1.
\]

Point:

\[
\boxed{(\sqrt3,1)}.
\]

---

# Part XVI: PYTHAGOREAN TRIG IDENTITY

## 85. Formula

\[
\boxed{\sin^2\theta+\cos^2\theta=1}.
\]

Suppose:

\[
\sin\theta=\frac35
\]

and angle is acute.

Then:

\[
\frac9{25}+\cos^2\theta=1.
\]

\[
\cos^2\theta=\frac{16}{25}.
\]

\[
\cos\theta=\frac45.
\]

Because acute then cosine positive.

Without quadrant/acute information:

\[
\cos\theta=\pm\frac45.
\]

---

## 86. Tangent identity

\[
\boxed{
\tan\theta=\frac{\sin\theta}{\cos\theta}
}
\]

If:

\[
\sin\theta=\frac35,
\qquad
\cos\theta=\frac45,
\]

then:

\[
\tan\theta
=
\frac{3/5}{4/5}
=
\boxed{\frac34}.
\]

---

# Part XVII: DISTANCE AND MIDPOINT

## 87. Distance formula

\[
\boxed{
d=
\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
}
\]

This is just Pythagoras in coordinates.

Example:

\[
(1,2),(4,6).
\]

Horizontal:

\[
4-1=3.
\]

Vertical:

\[
6-2=4.
\]

Distance:

\[
\sqrt{3^2+4^2}=5.
\]

---

## 88. Negative coordinates

Points:

\[
(-2,3),(4,-5).
\]

\[
d=
\sqrt{(4-(-2))^2+(-5-3)^2}.
\]

\[
=
\sqrt{6^2+(-8)^2}
\]

\[
=
\sqrt{36+64}
\]

\[
=\boxed{10}.
\]

Put negatives in parentheses.

---

## 89. Midpoint

\[
\boxed{
M=
\left(
\frac{x_1+x_2}{2},
\frac{y_1+y_2}{2}
\right)
}
\]

Example:

\[
(1,1),(7,9).
\]

\[
M=
\left(
\frac8{2},
\frac{10}{2}
\right)
=
\boxed{(4,5)}.
\]

---

# Part XVIII: CIRCLES

This is one of the highest-yield portions of B4.

## 90. Circle basics

\[
\boxed{d=2r}
\]

\[
\boxed{C=2\pi r}
\]

\[
\boxed{A=\pi r^2}.
\]

If circumference:

\[
30\pi,
\]

then:

\[
2\pi r=30\pi.
\]

\[
r=15.
\]

Area:

\[
\boxed{225\pi}.
\]

---

# Part XIX: ARC LENGTH AND SECTOR AREA

## 91. The single idea

A central angle represents a fraction of a full circle:

\[
\boxed{\frac{\theta}{360^\circ}}.
\]

Therefore:

arc length = that fraction of circumference.

sector area = that fraction of circle area.

---

## 92. Arc length in degrees

\[
\boxed{
s=
\frac{\theta}{360^\circ}(2\pi r)
}
\]

Example:

\[
r=6,\quad\theta=60^\circ.
\]

\[
s=
\frac{60}{360}(12\pi)
\]

\[
=\frac16(12\pi)
\]

\[
=\boxed{2\pi}.
\]

---

## 93. Sector area in degrees

\[
\boxed{
A_{\text{sector}}
=
\frac{\theta}{360^\circ}\pi r^2
}
\]

Example:

\[
r=10,\quad\theta=72^\circ.
\]

\[
A=
\frac{72}{360}(100\pi).
\]

\[
=\frac15(100\pi)
\]

\[
=\boxed{20\pi}.
\]

---

## 94. Unified circle proportion

Memorize conceptually:

\[
\boxed{
\frac{\text{arc length}}{\text{circumference}}
=
\frac{\text{sector area}}{\text{circle area}}
=
\frac{\theta}{360^\circ}
}
\]

This can solve almost every degree-based arc/sector problem.

---

## 95. Sector perimeter

A sector is like a pizza slice.

Its boundary contains:

- one arc
- two radii.

Therefore:

\[
\boxed{
P_{\text{sector}}=s+2r
}
\]

Example:

\[
r=6,\quad s=2\pi.
\]

\[
P=
12+2\pi.
\]

Do not give only \(2\pi\).

---

# Part XX: RADIANS

## 96. Full-circle equivalence

\[
\boxed{360^\circ=2\pi}
\]

Therefore:

\[
\boxed{180^\circ=\pi}.
\]

---

## 97. Degrees to radians

\[
\boxed{
\text{radians}
=
\text{degrees}\cdot\frac{\pi}{180}
}
\]

Example:

\[
150^\circ.
\]

\[
150\frac{\pi}{180}
=
\boxed{\frac{5\pi}{6}}.
\]

---

## 98. Radians to degrees

\[
\boxed{
\text{degrees}
=
\text{radians}\cdot\frac{180}{\pi}
}
\]

Example:

\[
\frac{5\pi}{6}.
\]

\[
\frac{5\pi}{6}\frac{180}{\pi}
=
\boxed{150^\circ}.
\]

---

## 99. Standard radian values

Memorize:

\[
\boxed{30^\circ=\frac\pi6}
\]

\[
\boxed{45^\circ=\frac\pi4}
\]

\[
\boxed{60^\circ=\frac\pi3}
\]

\[
\boxed{90^\circ=\frac\pi2}
\]

\[
\boxed{180^\circ=\pi}
\]

\[
\boxed{270^\circ=\frac{3\pi}{2}}
\]

\[
\boxed{360^\circ=2\pi}.
\]

---

## 100. Arc length in radians

This is beautifully simple:

\[
\boxed{s=r\theta}.
\]

BUT:

\[
\boxed{\theta\text{ MUST be in radians}}.
\]

Example:

\[
r=5,\quad
\theta=\frac{2\pi}{3}.
\]

\[
s=
5\frac{2\pi}{3}
=
\boxed{\frac{10\pi}{3}}.
\]

Never put \(60^\circ\) directly into \(s=r\theta\).

---

## 101. Sector area in radians

\[
\boxed{
A=\frac12r^2\theta
}
\]

again only when:

\[
\boxed{\theta\text{ is radians}}.
\]

Example:

\[
r=4,\quad
\theta=\frac\pi6.
\]

\[
A=
\frac12(16)\frac\pi6.
\]

\[
=\frac{8\pi}{6}
=
\boxed{\frac{4\pi}{3}}.
\]

---

# Part XXI: CENTRAL AND INSCRIBED ANGLES

## 102. Central angle

Vertex at center.

Its degree measure equals intercepted arc measure.

\[
\boxed{
m\angle_{\text{central}}
=
m\text{arc}
}
\]

---

## 103. Inscribed angle

Vertex lies on circle.

\[
\boxed{
m\angle_{\text{inscribed}}
=
\frac12(m\text{ intercepted arc})
}
\]

This is a must-know rule.

---

## 104. Example

Central/intercepted arc:

\[
80^\circ.
\]

Inscribed angle:

\[
\frac{80}{2}
=
\boxed{40^\circ}.
\]

---

## 105. Reverse direction

Inscribed:

\[
35^\circ.
\]

Arc:

\[
2(35)=\boxed{70^\circ}.
\]

---

## 106. Thales' theorem

If an inscribed angle intercepts a **diameter**, then intercepted arc is a semicircle:

\[
180^\circ.
\]

So inscribed angle:

\[
\frac12(180)
=
\boxed{90^\circ}.
\]

Thus:

> An angle subtending a diameter is a right angle.

This connects circles to Pythagoras.

---

# Part XXII: TANGENT LINES

## 107. Main tangent theorem

A tangent touches the circle at exactly one point.

The radius to that point is perpendicular to tangent.

\[
\boxed{\text{radius}\perp\text{tangent}}.
\]

That means tangent problems often hide a right triangle.

---

## 108. Example

External point to center:

\[
25.
\]

Tangent segment:

\[
7.
\]

Radius \(r\).

Because radius and tangent form \(90^\circ\):

\[
r^2+7^2=25^2.
\]

\[
r^2+49=625.
\]

\[
r^2=576.
\]

\[
\boxed{r=24}.
\]

Hidden 7-24-25 triple.

---

## 109. Two tangents from same external point

If tangents from \(P\) touch circle at A and B:

\[
\boxed{PA=PB}.
\]

Example:

\[
PA=4x-3
\]

\[
PB=x+9.
\]

Set equal:

\[
4x-3=x+9.
\]

\[
3x=12.
\]

\[
\boxed{x=4}.
\]

---

# Part XXIII: CHORDS

## 110. Core chord theorem

A perpendicular from the circle's center to a chord **bisects the chord**.

If chord length:

\[
24,
\]

each half:

\[
12.
\]

---

## 111. Chord example

Radius:

\[
13.
\]

Chord:

\[
24.
\]

Perpendicular from center creates right triangle:

hypotenuse \(13\),

one leg \(12\),

other leg \(d\).

\[
d^2+12^2=13^2.
\]

\[
d^2=169-144=25.
\]

\[
\boxed{d=5}.
\]

Hidden 5-12-13.

---

# Part XXIV: CIRCLE FROM DIAMETER ENDPOINTS

Suppose diameter endpoints are given.

Your method:

1. midpoint then center
2. distance then diameter
3. divide by 2 then radius
4. write equation

---

## 112. Example

Endpoints:

\[
(2,3),(8,-5).
\]

Center:

\[
\left(
\frac{2+8}{2},
\frac{3-5}{2}
\right)
\]

\[
=
\boxed{(5,-1)}.
\]

Diameter:

\[
\sqrt{(8-2)^2+(-5-3)^2}
\]

\[
=
\sqrt{36+64}=10.
\]

Radius:

\[
5.
\]

Equation:

\[
\boxed{
(x-5)^2+(y+1)^2=25
}
\]

---

# Part XXV: EQUATION OF A CIRCLE

This is one of the most important formulas in the entire domain.

## 113. Standard form

\[
\boxed{
(x-h)^2+(y-k)^2=r^2
}
\]

Center:

\[
\boxed{(h,k)}
\]

Radius:

\[
\boxed r.
\]

---

## 114. THE SIGN TRAP

Suppose:

\[
(x-3)^2+(y+2)^2=25.
\]

Center is:

\[
\boxed{(3,-2)}
\]

because:

\[
y+2=y-(-2).
\]

Radius:

\[
\boxed5.
\]

### Best way to avoid the sign trap

Ask:

> What \(x\) value makes this parenthesis zero?

\[
x-3=0\Rightarrow x=3.
\]

What \(y\) value?

\[
y+2=0\Rightarrow y=-2.
\]

---

## 115. Radius trap

Right side is:

\[
r^2.
\]

If:

\[
r^2=36,
\]

then:

\[
\boxed{r=6}.
\]

Not 36.

---

## 116. Writing from center and radius

Center:

\[
(2,3)
\]

radius:

\[
4.
\]

Equation:

\[
\boxed{
(x-2)^2+(y-3)^2=16
}.
\]

---

## 117. Circle through a point

Center:

\[
(3,2).
\]

Passes through:

\[
(7,5).
\]

Radius is distance:

\[
r=
\sqrt{(7-3)^2+(5-2)^2}
\]

\[
=
\sqrt{16+9}
=
5.
\]

Equation:

\[
\boxed{
(x-3)^2+(y-2)^2=25
}.
\]

---

## 118. Point inside/on/outside circle

Circle:

\[
(x-h)^2+(y-k)^2=r^2.
\]

Plug point into left side.

If result:

\[
<r^2
\]

inside.

If:

\[
=r^2
\]

on.

If:

\[
>r^2
\]

outside.

You do not even need square roots.

---

# Part XXVI: COMPLETING THE SQUARE FOR CIRCLES

This is the hardest common circle algebra.

Suppose:

\[
x^2+y^2-6x+4y-12=0.
\]

Goal:

\[
(x-h)^2+(y-k)^2=r^2.
\]

---

## 119. Step 1: group

Move constant:

\[
(x^2-6x)+(y^2+4y)=12.
\]

---

## 120. Complete \(x\)-square

For:

\[
x^2-6x,
\]

half of \(-6\):

\[
-3.
\]

Square:

\[
9.
\]

Add 9 to both sides.

---

## 121. Complete \(y\)-square

For:

\[
y^2+4y,
\]

half of 4:

\[
2.
\]

Square:

\[
4.
\]

Add 4 to both sides.

Now:

\[
x^2-6x+9+y^2+4y+4
=
12+9+4.
\]

Factor:

\[
(x-3)^2+(y+2)^2=25.
\]

Therefore:

center:

\[
\boxed{(3,-2)}
\]

radius:

\[
\boxed5.
\]

---

## 122. Completing-square recipe

For:

\[
x^2+Dx,
\]

add:

\[
\boxed{\left(\frac D2\right)^2}.
\]

For:

\[
y^2+Ey,
\]

add:

\[
\boxed{\left(\frac E2\right)^2}.
\]

Whatever you add to left:

\[
\boxed{\text{also add to right}}.
\]

---

## 123. Another example

\[
x^2+y^2+6x-8y-11=0.
\]

Move constant:

\[
x^2+6x+y^2-8y=11.
\]

For \(x\):

half of 6 = 3,

square = 9.

For \(y\):

half of -8 = -4,

square = 16.

\[
x^2+6x+9+y^2-8y+16
=
11+9+16.
\]

\[
(x+3)^2+(y-4)^2=36.
\]

Center:

\[
\boxed{(-3,4)}
\]

radius:

\[
\boxed6.
\]

---

# Part XXVII: LINE-CIRCLE SYSTEMS

Suppose:

\[
x+y=5
\]

and:

\[
x^2+y^2=13.
\]

Solve first:

\[
y=5-x.
\]

Substitute:

\[
x^2+(5-x)^2=13.
\]

Expand:

\[
x^2+25-10x+x^2=13.
\]

\[
2x^2-10x+12=0.
\]

Divide 2:

\[
x^2-5x+6=0.
\]

Factor:

\[
(x-2)(x-3)=0.
\]

So:

\[
x=2,3.
\]

Then:

\[
y=3,2.
\]

Solutions:

\[
\boxed{(2,3),(3,2)}.
\]

---

## 124. Tangency through discriminant

A line intersects a circle exactly once when tangent.

After substitution, you get a quadratic.

Exactly one intersection means:

\[
\boxed{D=0}.
\]

Example:

\[
y=x+k
\]

with:

\[
x^2+y^2=8.
\]

Substitute:

\[
x^2+(x+k)^2=8.
\]

\[
2x^2+2kx+k^2-8=0.
\]

Exactly once:

\[
D=0.
\]

\[
(2k)^2-4(2)(k^2-8)=0.
\]

\[
4k^2-8k^2+64=0.
\]

\[
64-4k^2=0.
\]

\[
k^2=16.
\]

\[
\boxed{k=\pm4}.
\]

This links B4 circle geometry directly to B2 discriminants.

---

# Part XXVIII: DESMOS STRATEGY

Desmos helps, but it should not replace the geometry.

## Circle equations

Enter:

```text
(x-3)^2+(y+2)^2=25
```

You can visually check center and radius.

---

## Expanded circles

Enter:

```text
x^2+y^2-6x+4y-12=0
```

Desmos graphs the circle even before you complete the square.

Great for checking.

---

## Trig

Make sure you distinguish degrees and radians.

For 35 degrees:

```text
sin(35°)
```

not blindly:

```text
sin(35)
```

because trig software commonly interprets bare numerical angles according to its angle mode.

---

## Inverse trig

For:

\[
\sin\theta=.6
\]

use:

```text
sin^(-1)(.6)
```

and confirm you're interpreting the result in the requested angular unit.

---

## Arithmetic

Cone:

```text
(1/3)*pi*5^2*12
```

Great for preventing arithmetic errors.

---

# Part XXIX: THE MAJOR SAT TRAPS

Memorize these.

| Trap | Correct response |
|---|---|
| Diameter used as radius | Divide by 2 |
| \(2\pi r\) vs \(\pi r^2\) | Circumference vs area |
| Slanted parallelogram side used as height | Height must be perpendicular |
| Semicircle treated as full circle | Multiply by \(1/2\) |
| Volume scaling by \(k^2\) | Use \(k^3\) |
| Area scaling by \(k\) | Use \(k^2\) |
| Same-side interior set equal | They sum to \(180^\circ\) |
| Triangle inequality allows equality | Must be strict \(>\) |
| Wrong corresponding sides in similarity | Match vertices first |
| Side ratio used directly for area | Square it |
| SSA assumed congruent | Not generally sufficient |
| Wrong side treated as hypotenuse | Opposite \(90^\circ\) |
| 45-45-90 hypotenuse given then multiply | Divide by \(\sqrt2\) |
| 30-60-90 \(\sqrt3\) attached to hypotenuse | It belongs to long leg |
| SOHCAHTOA on non-right triangle | Only right triangles |
| Opposite/adjacent not labeled | Label relative to chosen angle |
| \(\sin^{-1}\) treated as reciprocal | It returns an angle |
| Angle of depression measured from vertical | Measure from horizontal |
| Unit-circle \(x=\sin\) | \(x=\cos,\ y=\sin\) |
| Wrong quadrant sign | Determine signs first |
| \(s=r\theta\) with degrees | Radians only |
| Sector perimeter = arc only | Add two radii |
| Inscribed angle equals arc | It is half the arc |
| Tangent/radius not marked perpendicular | They form \(90^\circ\) |
| Circle center signs copied directly | Flip signs |
| RHS of circle treated as radius | Radius = square root |
| Completing square added only one side | Add to both sides |
| Diagram looks equal so assume equality | Trust labels/statements only |

---

# Part XXX: FORMULAS TO KNOW

## 2D area/perimeter

\[
\boxed{A_{\text{rectangle}}=lw}
\]

\[
\boxed{P_{\text{rectangle}}=2l+2w}
\]

\[
\boxed{A_{\triangle}=\frac12bh}
\]

\[
\boxed{A_{\text{parallelogram}}=bh}
\]

\[
\boxed{
A_{\text{trapezoid}}
=
\frac12(b_1+b_2)h
}
\]

\[
\boxed{A_{\text{circle}}=\pi r^2}
\]

\[
\boxed{C=2\pi r}
\]

---

## Volume

\[
\boxed{V_{\text{prism}}=Bh}
\]

\[
\boxed{V_{\text{rect prism}}=lwh}
\]

\[
\boxed{V_{\text{cylinder}}=\pi r^2h}
\]

\[
\boxed{V_{\text{cone}}=\frac13\pi r^2h}
\]

\[
\boxed{V_{\text{pyramid}}=\frac13Bh}
\]

\[
\boxed{V_{\text{sphere}}=\frac43\pi r^3}
\]

---

## Surface area

\[
\boxed{SA_{\text{rect prism}}=2lw+2lh+2wh}
\]

\[
\boxed{SA_{\text{cube}}=6s^2}
\]

\[
\boxed{SA_{\text{cylinder}}=2\pi r^2+2\pi rh}
\]

\[
\boxed{SA_{\text{sphere}}=4\pi r^2}
\]

---

## Scale

\[
\boxed{\text{length}\sim k}
\]

\[
\boxed{\text{area}\sim k^2}
\]

\[
\boxed{\text{volume}\sim k^3}
\]

---

## Triangles

\[
\boxed{A+B+C=180^\circ}
\]

\[
\boxed{a+b>c}
\]

\[
\boxed{a^2+b^2=c^2}
\]

---

## Special triangles

\[
\boxed{45-45-90:\quad s:s:s\sqrt2}
\]

\[
\boxed{30-60-90:\quad s:s\sqrt3:2s}
\]

---

## Trig

\[
\boxed{\sin\theta=\frac OH}
\]

\[
\boxed{\cos\theta=\frac AH}
\]

\[
\boxed{\tan\theta=\frac OA}
\]

\[
\boxed{\sin^2\theta+\cos^2\theta=1}
\]

\[
\boxed{\tan\theta=\frac{\sin\theta}{\cos\theta}}
\]

\[
\boxed{\sin\theta=\cos(90^\circ-\theta)}
\]

---

## Coordinate geometry

\[
\boxed{
d=
\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
}
\]

\[
\boxed{
M=
\left(
\frac{x_1+x_2}{2},
\frac{y_1+y_2}{2}
\right)
}
\]

---

## Circles

\[
\boxed{
(x-h)^2+(y-k)^2=r^2
}
\]

\[
\boxed{
s=
\frac{\theta}{360^\circ}(2\pi r)
}
\]

\[
\boxed{
A_{\text{sector}}
=
\frac{\theta}{360^\circ}\pi r^2
}
\]

\[
\boxed{
m\angle_{\text{inscribed}}
=
\frac12(m\text{ arc})
}
\]

---

## Radians

\[
\boxed{180^\circ=\pi}
\]

\[
\boxed{
\text{rad}
=
\text{deg}\frac{\pi}{180}
}
\]

\[
\boxed{s=r\theta}
\]

\[
\boxed{
A_{\text{sector}}
=
\frac12r^2\theta
}
\]

with \(\theta\) in radians.

---

# Part XXXI: FINAL SAT B4 CHECKLIST

Before you consider Geometry/Trig learned, you should be able to do all of these without notes:

1. Distinguish perimeter from area.
2. Use rectangle, triangle, parallelogram, trapezoid, and circle formulas.
3. Decompose or subtract composite figures.
4. Convert diameter to radius automatically.
5. Calculate prism, cylinder, cone, pyramid, and sphere volumes.
6. Distinguish volume from surface area.
7. Use \(k,k^2,k^3\) scaling correctly.
8. Handle individual dimensions changing by different factors.
9. Recognize complementary, supplementary, vertical, and linear-pair angles.
10. Know corresponding and alternate angles are equal for parallel lines.
11. Know same-side interior angles are supplementary.
12. Use triangle angle sum.
13. Use exterior-angle theorem.
14. Apply triangle inequality.
15. Use isosceles/equilateral properties.
16. Recognize similar triangles from AA.
17. Match corresponding sides correctly.
18. Square the scale factor for similar-triangle areas.
19. Recognize SSS/SAS/ASA/AAS/HL sufficiency.
20. Know SSA is generally insufficient.
21. Identify the hypotenuse correctly.
22. Use Pythagorean theorem.
23. Recognize 3-4-5 and 5-12-13 immediately.
24. Know 45-45-90 ratios.
25. Know 30-60-90 ratios.
26. Use SOHCAHTOA.
27. Label O/A/H relative to the selected angle.
28. Use inverse trig to find an angle.
29. Know inverse sine is not reciprocal sine.
30. Use sine/cosine cofunction relationships.
31. Draw angle-of-elevation/depression diagrams correctly.
32. Know unit-circle \(x=\cos,\ y=\sin\).
33. Memorize exact trig values for \(0,30,45,60,90^\circ\).
34. Apply correct quadrant signs.
35. Find reference angles.
36. Use \(\sin^2+\cos^2=1\).
37. Use distance and midpoint.
38. Convert degrees to radians.
39. Use degree arc/sector formulas.
40. Use \(s=r\theta\) only with radians.
41. Include two radii in sector perimeter.
42. Know central angle equals arc measure.
43. Know inscribed angle is half its intercepted arc.
44. Recognize an inscribed angle over a diameter is \(90^\circ\).
45. Know radius is perpendicular to tangent.
46. Know tangents from same external point have equal length.
47. Know a perpendicular from center bisects a chord.
48. Build a circle from diameter endpoints.
49. Read center and radius from circle equation.
50. Flip the center signs correctly.
51. Square the radius when writing the circle equation.
52. Complete the square for expanded circle equations.
53. Determine whether a point is inside/on/outside a circle.
54. Solve line-circle systems by substitution.
55. Use discriminant \(=0\) for a tangent line.
56. Use Desmos to verify, not to replace understanding.

If those 56 items are automatic, you have the B4 material organized the right way: not hundreds of isolated geometry facts, but a small number of **recognition patterns and reusable methods**.