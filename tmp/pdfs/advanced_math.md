Yes. I read the full B2 Advanced Math material. I’m going to teach this as a **complete Digital SAT Advanced Math lesson**, not as notes to memorize. The domain is built around four official skills: equivalent expressions, nonlinear equations in one variable, nonlinear systems, and nonlinear functions.

The six question families your file identifies as especially common are equivalent-expression problems, quadratic vertex/min-max problems, exponential growth/decay, extraneous-solution questions, nonlinear systems, and rearranging nonlinear formulas.

---

# The mental model for the whole SAT Advanced Math domain

Almost every problem in this domain is asking you to do one of these:

| SAT task | What you are actually doing |
|---|---|
| “Which expression is equivalent?” | Rewrite without changing value |
| “Solve for $x$” | Find inputs that make an equation true |
| “How many solutions?” | Count intersections/roots without necessarily solving everything |
| “What is the minimum/maximum?” | Find a vertex |
| “What does this constant represent?” | Interpret parameters in a model |
| “Which graph could represent…?” | Connect algebraic form to graph features |
| “For what value of $k$…?” | Use discriminants, tangency, or other constraints |
| “Solve for $r$, $t$, etc.” | Rearrange a formula |
| “Which function models…?” | Translate words into quadratic/exponential/etc. form |

Before doing algebra, **name the type of problem**.

That alone prevents a lot of wasted work.

---

# Part I. FOUNDATIONAL FORMULAS YOU MUST KNOW

# Exponent rules

These need to become automatic.

| Situation | Rule | Example |
|---|---|---|
| Same base, multiply | $a^m a^n=a^{m+n}$ | $x^3x^5=x^8$ |
| Same base, divide | $\frac{a^m}{a^n}=a^{m-n}$ | $\frac{x^7}{x^2}=x^5$ |
| Power of power | $(a^m)^n=a^{mn}$ | $(x^3)^4=x^{12}$ |
| Power of product | $(ab)^n=a^nb^n$ | $(2x)^3=8x^3$ |
| Zero exponent | $a^0=1$ | $7^0=1$ |
| Negative exponent | $a^{-n}=\frac1{a^n}$ | $x^{-3}=\frac1{x^3}$ |
| Fraction exponent | $a^{m/n}=\sqrt[n]{a^m}$ | $x^{2/3}=\sqrt[3]{x^2}$ |

## Important distinction

Multiplication lets you **add exponents** only when the bases match:

\[
x^{1/2}x^{1/3}
=
x^{1/2+1/3}
=
x^{5/6}.
\]

Not $x^{1/6}$.

For a power raised to another power, multiply:

\[
(x^{2/3})^6=x^4.
\]

## SAT example

Simplify

\[
\frac{x^{7/3}}{x^{1/2}}.
\]

Subtract:

\[
x^{7/3-1/2}
=
x^{14/6-3/6}
=
x^{11/6}.
\]

---

# Radical rules

A radical and a fractional exponent are two ways of writing the same thing:

\[
\sqrt{x}=x^{1/2}
\]

\[
\sqrt[3]{x}=x^{1/3}
\]

\[
\sqrt[4]{x^3}=x^{3/4}.
\]

This is extremely useful because complicated radical expressions become ordinary exponent problems.

## Critical exception

\[
\boxed{\sqrt{x^2}=|x|}
\]

not automatically $x$.

Why?

If $x=-5$,

\[
\sqrt{x^2}=\sqrt{25}=5,
\]

not $-5$.

---

# Rationalizing denominators

For something simple:

\[
\frac1{\sqrt 5}
\]

multiply numerator and denominator by $\sqrt5$:

\[
\frac{\sqrt5}{5}.
\]

For a binomial denominator:

\[
\frac1{3+\sqrt2},
\]

use the **conjugate**:

\[
3-\sqrt2.
\]

Then

\[
\frac{1}{3+\sqrt2}
\cdot
\frac{3-\sqrt2}{3-\sqrt2}
=
\frac{3-\sqrt2}{9-2}
=
\frac{3-\sqrt2}{7}.
\]

This works because

\[
(a+b)(a-b)=a^2-b^2.
\]

---

# Part II. EQUIVALENT EXPRESSIONS

Your file makes this the first major Advanced Math section. Two expressions are equivalent when they produce the same value for every allowable input.

The core operations are:

expanding, factoring, simplifying rational expressions, manipulating exponents/radicals, completing the square, and switching quadratic forms.

---

# Polynomial addition and subtraction

You may combine only **like terms**.

\[
3x^2+5x^2=8x^2
\]

but

\[
3x^2+5x
\]

cannot combine.

## Subtraction trap

Suppose:

\[
(4x^2+3x-2)-(x^2-5x+7).
\]

Distribute the negative to **every term**:

\[
4x^2+3x-2-x^2+5x-7.
\]

Then:

\[
3x^2+8x-9.
\]

The SAT loves the sign error

\[
-(x^2-5x+7)
\]

being incorrectly written as

\[
-x^2-5x-7.
\]

Correct:

\[
-x^2+5x-7.
\]

---

# Multiplying polynomials

Every term must multiply every relevant term.

Example:

\[
(2x-3)(x^2+4x-5).
\]

Multiply $2x$:

\[
2x^3+8x^2-10x.
\]

Multiply $-3$:

\[
-3x^2-12x+15.
\]

Combine:

\[
\boxed{2x^3+5x^2-22x+15}.
\]

---

# Three identities you should recognize instantly

## Square of a sum

\[
\boxed{(a+b)^2=a^2+2ab+b^2}
\]

Example:

\[
(x+7)^2=x^2+14x+49.
\]

## Square of a difference

\[
\boxed{(a-b)^2=a^2-2ab+b^2}
\]

Example:

\[
(3x-2)^2
=
9x^2-12x+4.
\]

## Difference of squares

\[
\boxed{a^2-b^2=(a-b)(a+b)}
\]

Example:

\[
x^2-81=(x-9)(x+9).
\]

### Huge trap

\[
(a+b)^2 \neq a^2+b^2.
\]

The middle term $2ab$ must exist.

---

# Factoring: the master method

Factoring means reversing multiplication.

Your decision process should be:

**GCF first → count terms → identify pattern → factor again if possible.**

## 7.1 Greatest common factor

\[
12x^3-8x^2+4x.
\]

Everything contains $4x$:

\[
\boxed{4x(3x^2-2x+1)}.
\]

Always check GCF first.

---

## 7.2 Difference of squares

\[
x^2-25
\]

is

\[
x^2-5^2
\]

so

\[
\boxed{(x-5)(x+5)}.
\]

More difficult:

\[
x^4-16.
\]

First:

\[
(x^2-4)(x^2+4).
\]

But $x^2-4$ factors again:

\[
\boxed{(x-2)(x+2)(x^2+4)}.
\]

Do not stop too early.

---

## 7.3 Sum of squares does NOT factor over the reals

\[
x^2+25
\]

does not factor into real linear factors.

This distinction matters:

\[
x^2-25 \quad \checkmark
\]

\[
x^2+25 \quad \text{no real factorization}.
\]

---

## 7.4 Perfect-square trinomials

Recognize:

\[
a^2+2ab+b^2=(a+b)^2
\]

and

\[
a^2-2ab+b^2=(a-b)^2.
\]

Example:

\[
x^2+10x+25.
\]

First and last:

\[
x^2,\quad 25=5^2.
\]

Middle:

\[
2(x)(5)=10x.
\]

Therefore:

\[
\boxed{(x+5)^2}.
\]

Example:

\[
4x^2-12x+9.
\]

\[
(2x)^2,\quad 3^2,
\]

middle:

\[
-2(2x)(3)=-12x.
\]

So

\[
\boxed{(2x-3)^2}.
\]

---

## 7.5 Simple trinomials

For

\[
x^2+bx+c,
\]

find two numbers $p,q$ such that

\[
p+q=b
\]

and

\[
pq=c.
\]

Example:

\[
x^2-7x+12.
\]

Need:

\[
p+q=-7,\qquad pq=12.
\]

Numbers:

\[
-3,-4.
\]

Therefore:

\[
\boxed{(x-3)(x-4)}.
\]

---

## 7.6 Hard trinomials: $ax^2+bx+c$

Example:

\[
6x^2+13x-5.
\]

Multiply:

\[
ac=6(-5)=-30.
\]

Find two numbers multiplying to $-30$ and adding to $13$:

\[
15,-2.
\]

Split the middle:

\[
6x^2+15x-2x-5.
\]

Group:

\[
3x(2x+5)-1(2x+5).
\]

Factor common binomial:

\[
\boxed{(3x-1)(2x+5)}.
\]

This method is very reliable.

---

## 7.7 Grouping

Usually four terms.

Example:

\[
x^3+3x^2-4x-12.
\]

Group:

\[
(x^3+3x^2)+(-4x-12).
\]

Factor:

\[
x^2(x+3)-4(x+3).
\]

Common factor:

\[
(x+3)(x^2-4).
\]

Difference of squares:

\[
\boxed{(x+3)(x-2)(x+2)}.
\]

---

## 7.8 Cubes

Know:

\[
\boxed{a^3-b^3=(a-b)(a^2+ab+b^2)}
\]

\[
\boxed{a^3+b^3=(a+b)(a^2-ab+b^2)}.
\]

Mnemonic:

**same, opposite, always positive.**

For $a^3-b^3$:

first factor uses same sign:

\[
a-b.
\]

Middle quadratic uses opposite sign:

\[
+a b.
\]

Final term positive.

Example:

\[
27x^3-64
=
(3x)^3-4^3
\]

so

\[
\boxed{(3x-4)(9x^2+12x+16)}.
\]

---

# Rational expressions

Example:

\[
\frac{x^2-9}{x^2+5x+6}.
\]

Factor:

\[
x^2-9=(x-3)(x+3)
\]

\[
x^2+5x+6=(x+2)(x+3).
\]

Thus:

\[
\frac{(x-3)(x+3)}
{(x+2)(x+3)}
=
\boxed{\frac{x-3}{x+2}}.
\]

But the original denominator told us:

\[
x\neq -3,-2.
\]

Even though $x+3$ disappeared algebraically, $x=-3$ remains excluded.

---

# You cancel factors, not terms

Legal:

\[
\frac{(x+2)(x-5)}{(x+2)(x+3)}
\]

because $x+2$ is a complete factor.

Illegal:

\[
\frac{x+3}{x}
\]

and trying to cancel the $x$.

Why?

The numerator is a **sum**.

There is no common multiplicative factor of $x$.

---

# Adding rational expressions

You need a common denominator.

Example:

\[
\frac{2}{x}+\frac{3}{x+1}.
\]

LCD:

\[
x(x+1).
\]

Rewrite:

\[
\frac{2(x+1)}{x(x+1)}
+
\frac{3x}{x(x+1)}.
\]

Combine:

\[
\boxed{\frac{5x+2}{x(x+1)}}.
\]

Restrictions:

\[
x\neq0,-1.
\]

---

# Dividing rational expressions

Division means multiply by reciprocal.

\[
\frac{x^2-4}{x+1}
\div
\frac{x-2}{x+3}.
\]

Rewrite:

\[
\frac{(x-2)(x+2)}{x+1}
\cdot
\frac{x+3}{x-2}.
\]

Cancel:

\[
\boxed{\frac{(x+2)(x+3)}{x+1}}.
\]

---

# Radical and exponent rewriting

Example:

\[
\frac{\sqrt[3]{x^2}}{\sqrt{x}}.
\]

Convert:

\[
\frac{x^{2/3}}{x^{1/2}}
=
x^{2/3-1/2}.
\]

Common denominator $6$:

\[
\frac46-\frac36=\frac16.
\]

Therefore:

\[
\boxed{x^{1/6}}
=
\boxed{\sqrt[6]x}.
\]

This fractional-exponent strategy is usually the cleanest SAT method.

---

# Part III. COMPLETING THE SQUARE

# Why completing the square exists

You are converting

\[
ax^2+bx+c
\]

into

\[
a(x-h)^2+k.
\]

The second form exposes the **vertex** immediately.

For

\[
x^2+bx,
\]

the magic number is

\[
\left(\frac b2\right)^2.
\]

---

# Example with $a=1$

Rewrite:

\[
x^2+8x+3.
\]

Half of $8$:

\[
4.
\]

Square it:

\[
16.
\]

Add and subtract:

\[
x^2+8x+16-16+3.
\]

Perfect square:

\[
(x+4)^2-13.
\]

So:

\[
\boxed{x^2+8x+3=(x+4)^2-13}.
\]

Vertex:

\[
\boxed{(-4,-13)}.
\]

---

# Example where $a\neq1$

Rewrite:

\[
2x^2-12x+5.
\]

Factor $2$ from only the $x$-terms:

\[
2(x^2-6x)+5.
\]

Half of $-6$:

\[
-3.
\]

Square:

\[
9.
\]

\[
2(x^2-6x+9-9)+5.
\]

\[
2[(x-3)^2-9]+5.
\]

Distribute the $2$:

\[
2(x-3)^2-18+5.
\]

\[
\boxed{2(x-3)^2-13}.
\]

Vertex:

\[
(3,-13).
\]

### Main trap

You cannot forget that the $-9$ inside gets multiplied by $2$.

---

# Part IV. THE THREE FORMS OF A QUADRATIC

This is one of the highest-yield SAT concepts.

# Standard form

\[
\boxed{f(x)=ax^2+bx+c}
\]

Immediately gives:

\[
y\text{-intercept}=c.
\]

Because:

\[
f(0)=c.
\]

Example:

\[
f(x)=3x^2-7x+12.
\]

$y$-intercept:

\[
\boxed{12}.
\]

---

# Factored form

\[
\boxed{f(x)=a(x-r_1)(x-r_2)}
\]

Immediately gives roots:

\[
x=r_1,\qquad x=r_2.
\]

Example:

\[
f(x)=2(x-3)(x+5).
\]

Roots:

\[
\boxed{3,-5}.
\]

Axis of symmetry:

\[
x=\frac{r_1+r_2}{2}
\]

so:

\[
x=\frac{3+(-5)}2=-1.
\]

---

# Vertex form

\[
\boxed{f(x)=a(x-h)^2+k}
\]

Immediately gives:

vertex:

\[
\boxed{(h,k)}
\]

axis:

\[
\boxed{x=h}
\]

and min/max value:

\[
\boxed{k}.
\]

If $a>0$, opens up to minimum.

If $a<0$, opens down to maximum.

Example:

\[
f(x)=-4(x-2)^2+9.
\]

Vertex:

\[
(2,9).
\]

Since $a=-4<0$:

\[
\boxed{\text{maximum}=9}.
\]

---

# Know which form to use

| Question asks for | Best form |
|---|---|
| $y$-intercept | Standard |
| roots/zeros/$x$-intercepts | Factored |
| vertex | Vertex |
| maximum/minimum | Vertex |
| axis of symmetry | Vertex or factored |
| equivalent expression | Usually expand/factor |
| graph behavior | Depends on feature |

A major SAT skill is not doing unnecessary algebra.

If you see:

\[
g(x)=3(x+7)^2-11
\]

and the question asks for the minimum, you should immediately answer:

\[
\boxed{-11}.
\]

---

# Part V. SOLVING QUADRATIC EQUATIONS

# First rule: put it equal to zero

Quadratic equation:

\[
ax^2+bx+c=0.
\]

Then choose a method.

---

# Quadratic method decision tree

| Situation | Best method |
|---|---|
| $x^2=k$ or $(x-h)^2=k$ | Square root |
| Factors obvious | Factoring |
| Need vertex | Complete square |
| Messy / uncertain | Quadratic formula |
| Need only number of solutions | Discriminant |
| Need decimal/intersection | Desmos can help |

---

# Factoring to solve

\[
x^2-5x+6=0.
\]

Factor:

\[
(x-2)(x-3)=0.
\]

Zero-product property:

\[
x-2=0
\]

or

\[
x-3=0.
\]

Therefore:

\[
\boxed{x=2,3}.
\]

---

# Square-root method

\[
3(x-4)^2=27.
\]

Divide by $3$:

\[
(x-4)^2=9.
\]

Take square root:

\[
x-4=\pm3.
\]

So:

\[
\boxed{x=7,1}.
\]

### Essential trap

\[
x^2=25
\]

means

\[
\boxed{x=\pm5},
\]

not just $5$.

---

# Quadratic formula

Memorize:

\[
\boxed{x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}}.
\]

Example:

\[
2x^2-7x=3.
\]

Move everything:

\[
2x^2-7x-3=0.
\]

So:

\[
a=2,\quad b=-7,\quad c=-3.
\]

Substitute:

\[
x=
\frac{-(-7)\pm\sqrt{(-7)^2-4(2)(-3)}}{4}.
\]

\[
=
\frac{7\pm\sqrt{49+24}}4.
\]

\[
\boxed{x=\frac{7\pm\sqrt{73}}4}.
\]

Write down $a,b,c$ first. It dramatically reduces sign errors.

---

# The discriminant

Inside the radical:

\[
\boxed{D=b^2-4ac}.
\]

It tells you the number of **real** roots.

| Discriminant | Real roots |
|---|---:|
| $D>0$ | 2 |
| $D=0$ | 1 |
| $D<0$ | 0 |

Geometrically:

| $D$ | Parabola |
|---|---|
| $>0$ | crosses $x$-axis twice |
| $=0$ | touches $x$-axis |
| $<0$ | never reaches $x$-axis |

---

# Parameter questions using discriminant

Example:

For what $k$ does

\[
x^2+kx+9=0
\]

have exactly one real solution?

Exactly one means:

\[
D=0.
\]

\[
k^2-4(1)(9)=0.
\]

\[
k^2-36=0.
\]

\[
k^2=36.
\]

\[
\boxed{k=\pm6}.
\]

Do not forget both signs.

---

# Two distinct solutions

Suppose:

\[
2x^2-4x+k=0
\]

has two distinct real roots.

Need:

\[
D>0.
\]

\[
(-4)^2-4(2)(k)>0.
\]

\[
16-8k>0.
\]

\[
16>8k.
\]

\[
\boxed{k<2}.
\]

---

# Part VI. QUADRATIC-IN-FORM PROBLEMS

# $u$-substitution

Sometimes an equation is not technically quadratic in $x$, but contains a repeated expression.

Example:

\[
x^4-5x^2+6=0.
\]

Notice:

\[
x^4=(x^2)^2.
\]

Let:

\[
u=x^2.
\]

Then:

\[
u^2-5u+6=0.
\]

Factor:

\[
(u-2)(u-3)=0.
\]

So:

\[
u=2,3.
\]

Back-substitute:

\[
x^2=2
\]

or

\[
x^2=3.
\]

Thus:

\[
\boxed{x=\pm\sqrt2,\pm\sqrt3}.
\]

Four real solutions.

---

# Negative substituted values

Example:

\[
x^4-2x^2-3=0.
\]

Set $u=x^2$:

\[
u^2-2u-3=0.
\]

Factor:

\[
(u-3)(u+1)=0.
\]

So:

\[
u=3,-1.
\]

Back-substitute:

\[
x^2=3 \Rightarrow x=\pm\sqrt3.
\]

But:

\[
x^2=-1
\]

has no real solution.

Therefore:

\[
\boxed{2\text{ real solutions}}.
\]

---

# Part VII. RADICAL EQUATIONS

# Why extraneous solutions appear

Squaring is not a one-to-one operation.

For example:

\[
3^2=(-3)^2.
\]

Therefore when you square both sides of an equation, information about sign can disappear.

So you must check answers in the **original equation**.

---

# Radical equation method

Suppose:

\[
\sqrt{2x+3}+5=x.
\]

Isolate the radical:

\[
\sqrt{2x+3}=x-5.
\]

Square:

\[
2x+3=(x-5)^2.
\]

\[
2x+3=x^2-10x+25.
\]

Move everything:

\[
x^2-12x+22=0.
\]

Quadratic formula gives:

\[
x=6\pm\sqrt{14}.
\]

Now check.

Since the original isolated form was

\[
\sqrt{2x+3}=x-5,
\]

the right side must be nonnegative.

For

\[
x=6-\sqrt{14}\approx2.26,
\]

\[
x-5<0.
\]

Impossible because a square root is nonnegative.

Reject it.

Therefore:

\[
\boxed{x=6+\sqrt{14}}.
\]

---

# Radical SAT checklist

For any square-root equation:

\[
\boxed{\text{isolate to square to solve to check original}}
\]

Never skip the final step.

---

# Part VIII. RATIONAL EQUATIONS

# Start with restrictions

Example:

\[
\frac{x^2}{x-1}=\frac1{x-1}.
\]

Original denominator means:

\[
\boxed{x\neq1}.
\]

Now multiply by $x-1$:

\[
x^2=1.
\]

So:

\[
x=\pm1.
\]

But $x=1$ is illegal.

Thus:

\[
\boxed{x=-1}.
\]

---

# Full rational-equation process

For:

\[
\frac{x}{x-3}
+
\frac2{x+1}
=
\frac5{x^2-2x-3},
\]

factor:

\[
x^2-2x-3=(x-3)(x+1).
\]

Restrictions:

\[
x\neq3,-1.
\]

LCD:

\[
(x-3)(x+1).
\]

Multiply everything:

\[
x(x+1)+2(x-3)=5.
\]

Expand:

\[
x^2+x+2x-6=5.
\]

\[
x^2+3x-11=0.
\]

Then solve the quadratic.

Final candidates must still respect:

\[
x\neq3,-1.
\]

---

# Part IX. ABSOLUTE VALUE EQUATIONS

# Meaning of absolute value

\[
|x|
\]

is the distance between $x$ and $0$.

Distances cannot be negative.

Therefore:

\[
|x|=-5
\]

has

\[
\boxed{\text{no solution}}.
\]

---

# Standard absolute-value equation

If:

\[
|A|=B
\]

and $B>0$, then:

\[
A=B
\]

or

\[
A=-B.
\]

Example:

\[
|2x+5|-3=10.
\]

Isolate:

\[
|2x+5|=13.
\]

Case 1:

\[
2x+5=13
\]

\[
2x=8
\]

\[
x=4.
\]

Case 2:

\[
2x+5=-13
\]

\[
2x=-18
\]

\[
x=-9.
\]

Answer:

\[
\boxed{4,-9}.
\]

---

# Number of absolute-value solutions

For:

\[
|x-h|=k,
\]

| $k$ | Number of solutions |
|---|---:|
| $k>0$ | 2 |
| $k=0$ | 1 |
| $k<0$ | 0 |

Visualize a horizontal line intersecting a V.

---

# Part X. EXPONENTIAL EQUATIONS

# Same-base method

If:

\[
a^{f(x)}=a^{g(x)}
\]

with a valid positive base $a\neq1$, then:

\[
f(x)=g(x).
\]

Example:

\[
3^{x^2-4}=27^{x+2}.
\]

Rewrite:

\[
27=3^3.
\]

Thus:

\[
3^{x^2-4}
=
3^{3(x+2)}.
\]

Equate exponents:

\[
x^2-4=3x+6.
\]

\[
x^2-3x-10=0.
\]

Factor:

\[
(x-5)(x+2)=0.
\]

\[
\boxed{x=5,-2}.
\]

---

# Exponential $u$-substitution

Example:

\[
4^x-2^{x+1}=8.
\]

Rewrite:

\[
4^x=(2^x)^2.
\]

and:

\[
2^{x+1}=2(2^x).
\]

Let:

\[
u=2^x.
\]

Then:

\[
u^2-2u=8.
\]

\[
u^2-2u-8=0.
\]

\[
(u-4)(u+2)=0.
\]

So:

\[
u=4
\]

or

\[
u=-2.
\]

But:

\[
2^x>0
\]

for every real $x$.

Reject $-2$.

\[
2^x=4=2^2
\]

so:

\[
\boxed{x=2}.
\]

---

# Part XI. NONLINEAR SYSTEMS

The standard strategy in your material is to substitute the linear equation into the nonlinear equation, then solve and back-substitute.

# Line + parabola

Example:

\[
y=2x+1
\]

and

\[
y=x^2-2x+3.
\]

Since both equal $y$:

\[
2x+1=x^2-2x+3.
\]

Move everything:

\[
x^2-4x+2=0.
\]

Solve:

\[
x=2\pm\sqrt2.
\]

Then plug each $x$ into

\[
y=2x+1.
\]

That gives the two intersection points.

---

# Counting intersections using discriminant

Suppose:

\[
y=mx+d
\]

and:

\[
y=ax^2+bx+c.
\]

Set equal:

\[
mx+d=ax^2+bx+c.
\]

Rearrange:

\[
ax^2+(b-m)x+(c-d)=0.
\]

Then use the discriminant.

\[
D>0\Rightarrow2\text{ intersections}
\]

\[
D=0\Rightarrow1\text{ intersection, tangent}
\]

\[
D<0\Rightarrow0\text{ intersections}.
\]

This is extremely SAT-friendly.

---

# Tangency parameter problem

Find $k$ so that:

\[
y=2x+k
\]

and

\[
y=x^2-3x+1
\]

intersect exactly once.

Set equal:

\[
2x+k=x^2-3x+1.
\]

\[
x^2-5x+(1-k)=0.
\]

Exactly once means:

\[
D=0.
\]

\[
(-5)^2-4(1)(1-k)=0.
\]

\[
25-4+4k=0.
\]

\[
21+4k=0.
\]

\[
\boxed{k=-\frac{21}{4}}.
\]

---

# Quadratic + quadratic

Example:

\[
y=x^2-4
\]

\[
y=-x^2+4.
\]

Set equal:

\[
x^2-4=-x^2+4.
\]

\[
2x^2=8.
\]

\[
x^2=4.
\]

\[
x=\pm2.
\]

For either value:

\[
y=0.
\]

Solutions:

\[
\boxed{(2,0),(-2,0)}.
\]

---

# Absolute-value systems

Example:

\[
y=2x-1
\]

\[
y=|x+2|.
\]

You can graph this instantly on Desmos.

Algebraically, split based on:

\[
x+2\ge0
\]

or

\[
x+2<0.
\]

The key is that after solving a branch, the answer must satisfy that branch's condition.

---

# Part XII. REARRANGING NONLINEAR FORMULAS

Your document treats this as another tested skill: identify the target variable and undo operations in reverse order.

# Simple square formula

\[
A=\pi r^2.
\]

Solve for $r$:

\[
r^2=\frac A\pi.
\]

\[
r=\pm\sqrt{\frac A\pi}.
\]

But if $r$ is a geometric radius:

\[
\boxed{r=\sqrt{\frac A\pi}}.
\]

Context removes the negative answer.

---

# Radical formula

\[
T=2\pi\sqrt{\frac Lg}.
\]

Divide:

\[
\frac{T}{2\pi}
=
\sqrt{\frac Lg}.
\]

Square:

\[
\frac{T^2}{4\pi^2}
=
\frac Lg.
\]

Multiply by $g$:

\[
\boxed{L=\frac{gT^2}{4\pi^2}}.
\]

---

# Formula with fractions

\[
\frac1R=\frac1{R_1}+\frac1{R_2}.
\]

Solve for $R_1$.

Multiply everything by:

\[
RR_1R_2.
\]

Then:

\[
R_1R_2=RR_2+RR_1.
\]

Collect $R_1$:

\[
R_1R_2-RR_1=RR_2.
\]

Factor:

\[
R_1(R_2-R)=RR_2.
\]

Thus:

\[
\boxed{R_1=\frac{RR_2}{R_2-R}}.
\]

---

# Part XIII. FUNCTIONS: DOMAIN AND RANGE

# Domain

Domain means:

\[
\boxed{\text{allowed }x\text{-values}}.
\]

The SAT restrictions you care about most are:

| Expression | Restriction |
|---|---|
| $\sqrt{A}$ | $A\ge0$ |
| $\frac1B$ | $B\neq0$ |
| real-life time/count/etc. | obey context |

Example:

\[
f(x)=\frac{\sqrt{x-5}}{x-8}.
\]

Square root requires:

\[
x-5\ge0
\]

\[
x\ge5.
\]

Denominator requires:

\[
x\neq8.
\]

Domain:

\[
\boxed{[5,8)\cup(8,\infty)}.
\]

---

# Range

Range means:

\[
\boxed{\text{possible }y\text{-values}}.
\]

Example:

\[
f(x)=3+\sqrt{2x-4}.
\]

A square root is always nonnegative:

\[
\sqrt{2x-4}\ge0.
\]

Therefore:

\[
f(x)\ge3.
\]

Range:

\[
\boxed{[3,\infty)}.
\]

---

# Part XIV. MAXIMUM AND MINIMUM

# Vertex formula

For:

\[
f(x)=ax^2+bx+c,
\]

the vertex $x$-coordinate is:

\[
\boxed{x_v=-\frac{b}{2a}}.
\]

Then:

\[
\boxed{y_v=f(x_v)}.
\]

If $a>0$:

minimum.

If $a<0$:

maximum.

---

# Example

\[
f(x)=-2x^2+12x-7.
\]

\[
a=-2,\quad b=12.
\]

\[
x_v=-\frac{12}{2(-2)}
=
3.
\]

Now:

\[
f(3)
=
-2(9)+36-7
=
11.
\]

Because the parabola opens downward:

\[
\boxed{\text{maximum}=11}
\]

at:

\[
\boxed{x=3}.
\]

Be careful about the wording.

“What is the maximum value?” to $11$

“At what value of $x$ does the maximum occur?” to $3$

---

# Part XV. INCREASING AND DECREASING

For an upward parabola with vertex $x=h$:

\[
\boxed{\text{decreasing on }(-\infty,h)}
\]

\[
\boxed{\text{increasing on }(h,\infty)}.
\]

For a downward parabola, reverse them.

Example:

\[
f(x)=x^2-4x+1.
\]

Vertex:

\[
x=-\frac{-4}{2}=2.
\]

Opens upward.

So:

\[
\boxed{\text{decreasing on }(-\infty,2)}
\]

and

\[
\boxed{\text{increasing on }(2,\infty)}.
\]

---

# Part XVI. POLYNOMIAL END BEHAVIOR

Only the **leading term** matters.

Suppose:

\[
f(x)=ax^n+\cdots
\]

There are four possibilities.

| Degree | Leading coefficient | Left end | Right end |
|---|---|---|---|
| Even | positive | up | up |
| Even | negative | down | down |
| Odd | positive | down | up |
| Odd | negative | up | down |

Think:

### Even degree
ends go the **same direction**.

### Odd degree
ends go **opposite directions**.

Then the sign of $a$ tells you the right-hand end.

Example:

\[
f(x)=-3x^4+100x^3-5.
\]

Highest degree:

\[
-3x^4.
\]

Even + negative:

\[
\boxed{\text{both ends down}}.
\]

The $100x^3$ does not control long-run behavior.

---

# Part XVII. GRAPH FEATURES OF RATIONAL FUNCTIONS

# Intercepts

$x$-intercept:

\[
f(x)=0.
\]

For a rational function, this usually means numerator $=0$, provided denominator $\neq0$.

$y$-intercept:

\[
f(0).
\]

---

# Vertical asymptotes

For:

\[
f(x)=\frac{N(x)}{D(x)},
\]

a vertical asymptote occurs when:

\[
D(x)=0
\]

after simplification, provided the corresponding factor did not cancel.

Example:

\[
\frac{2x+1}{(x-3)(x+2)}.
\]

VA:

\[
\boxed{x=3,\;x=-2}.
\]

---

# Holes vs vertical asymptotes

Example:

\[
f(x)=
\frac{(x-2)(x+3)}
{(x-2)(x+5)}.
\]

Cancel:

\[
f(x)=\frac{x+3}{x+5},
\]

but original restrictions are still:

\[
x\neq2,-5.
\]

At $x=2$, the factor canceled.

So:

\[
\boxed{x=2\text{ is a hole}}.
\]

At $x=-5$, denominator remains zero.

So:

\[
\boxed{x=-5\text{ is a vertical asymptote}}.
\]

Memorize:

\[
\boxed{\text{cancelled denominator factor} \rightarrow \text{hole}}
\]

\[
\boxed{\text{uncancelled denominator zero} \rightarrow \text{VA}}
\]

---

# Horizontal asymptotes

For:

\[
\frac{\text{polynomial}}{\text{polynomial}},
\]

compare degrees.

### Numerator degree < denominator degree

\[
\boxed{y=0}.
\]

Example:

\[
\frac{x}{x^2+1}.
\]

### Degrees equal

Ratio of leading coefficients.

\[
\boxed{
y=
\frac{\text{leading numerator coefficient}}
{\text{leading denominator coefficient}}
}
\]

Example:

\[
\frac{5x^3-2x}{2x^3+7}.
\]

\[
\boxed{y=\frac52}.
\]

### Numerator degree > denominator degree

No ordinary horizontal asymptote.

---

# Part XVIII. FUNCTION TRANSFORMATIONS

You need these cold.

| Expression | Transformation |
|---|---|
| $f(x)+k$ | up $k$ |
| $f(x)-k$ | down $k$ |
| $f(x-h)$ | right $h$ |
| $f(x+h)$ | left $h$ |
| $-f(x)$ | reflect over $x$-axis |
| $f(-x)$ | reflect over $y$-axis |
| $af(x), a>1$ | vertical stretch |
| $af(x),0<a<1$ | vertical compression |

The horizontal shift is the famous trap.

\[
f(x-5)
\]

moves **right 5**.

\[
f(x+5)
\]

moves **left 5**.

Inside is opposite.

Outside is intuitive.

---

# Transformation example

Parent:

\[
f(x)=\sqrt x.
\]

Shift right $2$:

\[
\sqrt{x-2}.
\]

Reflect over $x$-axis:

\[
-\sqrt{x-2}.
\]

Shift down $5$:

\[
\boxed{-\sqrt{x-2}-5}.
\]

---

# Part XIX. POLYNOMIAL ROOT MULTIPLICITY

# Multiplicity tells you graph behavior

Suppose a polynomial contains:

\[
(x-r)^m.
\]

Then $r$ is a root with multiplicity $m$.

If multiplicity is odd:

\[
\boxed{\text{graph crosses}}
\]

If multiplicity is even:

\[
\boxed{\text{graph touches/bounces}}.
\]

Examples:

\[
(x-2)
\]

multiplicity $1$: crosses.

\[
(x-2)^2
\]

multiplicity $2$: touches.

\[
(x-2)^3
\]

multiplicity $3$: crosses, usually flatter/S-shaped.

---

# Full polynomial graph example

\[
f(x)=-(x+1)^2(x-3)(x-5)^3.
\]

Roots:

\[
x=-1,3,5.
\]

At $-1$:

multiplicity $2$ to bounce.

At $3$:

multiplicity $1$ to cross.

At $5$:

multiplicity $3$ to cross.

Degree:

\[
2+1+3=6.
\]

Notice here the leading sign is negative, so even degree + negative coefficient means both ends down.

When doing these questions, calculate degree from **multiplicity**, not just number of distinct roots.

---

# Least possible degree

Graph:

cross at $x=-1$

touch at $x=2$

cross at $x=5$.

Minimum multiplicities:

\[
1+2+1=4.
\]

So minimum degree:

\[
\boxed4.
\]

A touch cannot come from multiplicity $1$.

---

# Part XX. EXPONENTIAL FUNCTIONS

This is extremely important on the Digital SAT.

# General form

\[
\boxed{f(t)=a(b)^t}.
\]

$a$:

\[
\boxed{\text{initial value}}
\]

because:

\[
f(0)=ab^0=a.
\]

$b$:

\[
\boxed{\text{multiplicative factor per time period}}.
\]

---

# Growth

Increase by $r\%$:

\[
\boxed{b=1+\frac r{100}}.
\]

8% increase:

\[
b=1.08.
\]

15% increase:

\[
b=1.15.
\]

So:

\[
500(1.08)^t
\]

means initial value $500$, increasing $8\%$ each period.

---

# Decay

Decrease by $r\%$:

\[
\boxed{b=1-\frac r{100}}.
\]

12% depreciation:

\[
1-0.12=0.88.
\]

If a \$25,000 car loses 12% annually:

\[
\boxed{V(t)=25000(0.88)^t}.
\]

Do not use $0.12$.

The car retains $88\%$, not $12\%$.

---

# Multiplier <-> percentage conversion

If multiplier:

\[
1.27,
\]

percentage growth:

\[
(1.27-1)(100)=27\%.
\]

If multiplier:

\[
0.84,
\]

percentage decrease:

\[
(1-0.84)(100)=16\%.
\]

---

# Doubling time

If a quantity doubles every $d$ units:

\[
\boxed{f(t)=a2^{t/d}}.
\]

Example: initial population $300$, doubles every 5 hours:

\[
\boxed{P(t)=300(2)^{t/5}}.
\]

At $t=5$:

\[
300(2)^1=600.
\]

At $t=10$:

\[
300(2)^2=1200.
\]

---

# Half-life

If something halves every $h$ units:

\[
\boxed{f(t)=a\left(\frac12\right)^{t/h}}.
\]

50 grams, half-life 30 days:

\[
\boxed{M(t)=50\left(\frac12\right)^{t/30}}.
\]

At 30 days:

\[
25.
\]

At 60:

\[
12.5.
\]

---

# Scaled time, one of the nastiest SAT traps

Suppose:

\[
A(t)=18000(1.1025)^{t/2}.
\]

Do **not** say it grows 10.25% every year.

The exponent is:

\[
\frac t2.
\]

So one full multiplication by $1.1025$ occurs every **2 years**.

Thus:

\[
\boxed{10.25\%\text{ growth every 2 years}}.
\]

What is the per-year multiplier?

\[
(1.1025)^{1/2}.
\]

Since:

\[
1.05^2=1.1025,
\]

the annual factor is:

\[
1.05.
\]

So:

\[
\boxed{5\%\text{ growth per year}}.
\]

---

# Growth over several periods

Suppose something grows $8\%$ every 2 years.

What percent does it grow over 6 years?

Number of periods:

\[
\frac62=3.
\]

Overall multiplier:

\[
1.08^3.
\]

\[
1.08^3=1.259712.
\]

Growth percentage:

\[
(1.259712-1)(100)
=
25.9712\%.
\]

Approximately:

\[
\boxed{26.0\%}.
\]

You do not simply calculate:

\[
8\%\times3=24\%
\]

because exponential growth compounds.

---

# Exponential asymptotes

For:

\[
f(x)=ab^x+k,
\]

horizontal asymptote:

\[
\boxed{y=k}.
\]

Example:

\[
f(x)=5(2)^x-7.
\]

HA:

\[
\boxed{y=-7}.
\]

For $a>0$, range:

\[
\boxed{(-7,\infty)}.
\]

---

# Part XXI. RATIONAL FUNCTION TRANSFORMATIONS

# Parent function

\[
\boxed{f(x)=\frac1x}.
\]

Transformed form:

\[
\boxed{f(x)=\frac a{x-h}+k}.
\]

Immediately:

\[
\boxed{\text{VA}:x=h}
\]

\[
\boxed{\text{HA}:y=k}.
\]

Example:

\[
f(x)=\frac3{x-2}+1.
\]

VA:

\[
x=2.
\]

HA:

\[
y=1.
\]

Domain:

\[
x\neq2.
\]

Range:

\[
y\neq1.
\]

---

# Part XXII. DESMOS: WHAT YOU SHOULD ACTUALLY USE IT FOR

Because the Digital SAT includes Desmos, you should know when it saves time.

## Roots

Graph:

\[
y=f(x).
\]

The $x$-intercepts are the real roots.

## Systems

Graph both equations.

Each intersection is one solution.

This is particularly useful for “how many solutions?” questions.

## Vertex

Graph the quadratic and select the turning point.

Useful for min/max questions when exact symbolic manipulation is unnecessary.

## Equivalent expressions

Graph:

\[
y=\text{original}
\]

and:

\[
y=\text{answer choice}.
\]

If they overlap for the relevant domain, they are equivalent.

Be careful about **holes/domain restrictions**.

## Regression from a table

Quadratic:

\[
y_1\sim ax_1^2+bx_1+c.
\]

Exponential:

\[
y_1\sim ab^{x_1}.
\]

These can recover models rapidly.

## When you should NOT automatically use Desmos

Simple factoring such as:

\[
x^2-9.
\]

Simple coefficient interpretation such as:

\[
300(1.07)^t.
\]

Exact radical answers such as:

\[
\frac{7+\sqrt{73}}4.
\]

Basic exponent rules.

You need enough algebra fluency that opening Desmos does not make a 10-second question take a minute.

---

# Part XXIII. THE TRAPS YOU NEED TO BE PARANOID ABOUT

Your source explicitly emphasizes these traps.

| Trap | Correct idea |
|---|---|
| $(a+b)^2=a^2+b^2$ | Wrong. Include $2ab$ |
| $x^2+49$ factors like diff. squares | No real factorization |
| Radical equation candidates | Check original |
| Cancelled denominator | Original excluded value remains excluded |
| $|x|=-5$ | No solution |
| $f(x+3)$ | Shift left 3 |
| $D=0$, then $k^2=36$ | $k=\pm6$ |
| Even multiplicity | Bounce |
| Odd multiplicity | Cross |
| $1.08$ | 8% growth |
| $0.92$ | 8% decay |
| Completing square with $a\neq1$ | Factor $a$ first |
| Rational simplification | Cancel factors, not terms |
| $b^x$ for positive base | Always positive |
| $1.08^{t/2}$ | 8% every 2 units |

---

# Part XXIV. THE MASTER SAT METHOD CHECKLIST

This is the checklist I would actually memorize.

| If you see… | Do this |
|---|---|
| “Equivalent expression” | factor / expand / exponent rules / test values |
| Polynomial with 2 terms | GCF to diff squares to cubes |
| Polynomial with 3 terms | GCF to perfect square to trinomial |
| Polynomial with 4 terms | GCF to grouping |
| Rational expression | factor numerator + denominator first |
| Square root + exponents | convert to fractional exponents |
| Quadratic roots | factoring / square root / quadratic formula |
| “How many real solutions?” quadratic | discriminant |
| Radical equation | isolate to square to solve to check |
| Rational equation | restrictions to LCD to solve to reject forbidden values |
| Absolute-value equation | isolate to positive and negative cases |
| Exponential equation | same base or $u=b^x$ |
| Line + parabola system | substitute to quadratic |
| “Exactly one intersection” | discriminant $=0$ |
| Quadratic min/max | vertex |
| Quadratic roots | factored form |
| Quadratic $y$-intercept | standard form |
| Domain | square roots $\ge0$; denominators $\neq0$ |
| Range | reason from graph/output restrictions |
| Polynomial end behavior | leading term only |
| Rational VA | uncancelled denominator zero |
| Rational hole | cancelled denominator factor |
| Exponential model | initial × multiplier$^{\text{number of periods}}$ |
| Doubling | $a2^{t/d}$ |
| Half-life | $a(1/2)^{t/h}$ |
| $f(x-h)$ | right |
| $f(x+h)$ | left |
| even multiplicity | touch |
| odd multiplicity | cross |

---

# Part XXV. FORMULA SHEET TO MEMORIZE

## Factoring

\[
\boxed{a^2-b^2=(a-b)(a+b)}
\]

\[
\boxed{a^2+2ab+b^2=(a+b)^2}
\]

\[
\boxed{a^2-2ab+b^2=(a-b)^2}
\]

\[
\boxed{a^3+b^3=(a+b)(a^2-ab+b^2)}
\]

\[
\boxed{a^3-b^3=(a-b)(a^2+ab+b^2)}
\]

## Quadratics

\[
\boxed{x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}}
\]

\[
\boxed{D=b^2-4ac}
\]

\[
\boxed{x_v=-\frac b{2a}}
\]

\[
\boxed{y_v=f(x_v)}
\]

## Vertex form

\[
\boxed{f(x)=a(x-h)^2+k}
\]

vertex:

\[
\boxed{(h,k)}.
\]

## Factored form

\[
\boxed{f(x)=a(x-r_1)(x-r_2)}
\]

roots:

\[
\boxed{r_1,r_2}.
\]

axis:

\[
\boxed{x=\frac{r_1+r_2}{2}}.
\]

## Completing square

\[
\boxed{x^2+bx=
\left(x+\frac b2\right)^2-
\left(\frac b2\right)^2}
\]

## Fractional exponents

\[
\boxed{a^{m/n}=\sqrt[n]{a^m}}
\]

## Exponential growth

\[
\boxed{A=A_0(1+r)^t}
\]

## Exponential decay

\[
\boxed{A=A_0(1-r)^t}
\]

## Change every $d$ units

\[
\boxed{A=A_0b^{t/d}}
\]

## Doubling

\[
\boxed{A=A_0\,2^{t/d}}
\]

## Half-life

\[
\boxed{A=A_0\left(\frac12\right)^{t/h}}
\]

## Compound interest

\[
\boxed{
A=P\left(1+\frac rn\right)^{nt}
}
\]

## Rational horizontal asymptote

\[
\boxed{
\deg N<\deg D\Rightarrow y=0
}
\]

\[
\boxed{
\deg N=\deg D
\Rightarrow
y=\frac{\text{leading coeff. }N}
{\text{leading coeff. }D}
}
\]

## Rational transformation

\[
\boxed{f(x)=\frac a{x-h}+k}
\]

\[
\boxed{\text{VA }x=h,\quad\text{HA }y=k}
\]

## Absolute value

\[
\boxed{|A|=B\Rightarrow A=B\text{ or }A=-B}
\]

provided $B\ge0$.

---

# Final “am I SAT-ready?” checklist

You should be able to do every one of these without needing notes:

1. Expand $(3x-5)^2$ without forgetting the middle term.
2. Factor simple and hard trinomials.
3. Recognize difference of squares and perfect squares immediately.
4. Simplify rational expressions while preserving domain restrictions.
5. Convert radicals into rational exponents.
6. Complete the square, including when $a\neq1$.
7. Switch mentally among standard, factored, and vertex quadratic forms.
8. Choose the fastest quadratic-solving method.
9. Use $D=b^2-4ac$ for 0/1/2 real roots and tangency.
10. Recognize $x^4+bx^2+c$ as a quadratic in $x^2$.
11. Solve radical equations and check for extraneous roots.
12. Solve rational equations and reject denominator-zero candidates.
13. Split absolute-value equations correctly.
14. Rewrite exponential equations to a common base.
15. Use $u=b^x$ for quadratic-in-exponential equations.
16. Solve/count intersections in nonlinear systems.
17. Rearrange formulas containing squares, roots, and fractions.
18. Determine domain and range.
19. Find quadratic min/max and know whether the question wants $x$ or $y$.
20. Determine increasing/decreasing intervals from the vertex.
21. Determine polynomial end behavior from degree parity and leading sign.
22. Identify holes versus vertical asymptotes.
23. Identify horizontal asymptotes.
24. Interpret transformations, especially horizontal shifts.
25. Read root multiplicity from factors and graph behavior.
26. Translate percent growth/decay into multipliers.
27. Handle half-life and doubling-time models.
28. Interpret scaled exponents such as $t/3$.
29. Compute compound percentage change rather than adding percentages.
30. Know when Desmos is faster and when paper algebra is faster.

If you can do those 30 things confidently, you have covered the substantive material in the B2 Advanced Math document rather than merely memorizing its formulas. The file itself frames the same domain around nonlinear relationships involving quadratics, exponentials, polynomials, radicals, rationals, and systems.