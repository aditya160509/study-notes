## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

**243**

# Chapter 10

## Review Copy-Cambridge University Press-Review Copy

# Diff erential equations

##### P3 This chapter is for Pure Mathematics 3 students only.

##### In this chapter you will learn how to:

formulate a simple statement involving a rate of change as a differential equation ■ fi nd, by integration, a general form of solution for a fi rst order differential equation in which the ■ variables are separable use an initial condition to fi nd a particular solution ■ interpret the solution of a differential equation in the context of a problem being modelled by the ■ equation.

Copyright Material - Review Only - Not for Redistribution

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

##### Cambridge International AS & A Level Mathematics: Pure Mathematics 2 & 3

##### PREREQUISITE KNOWLEDGE

##### Where it comes from What you should be able to do Check your skills

IGCSE / O Level Express direct and inverse variation **1** The weight, *w* newtons, of a sphere is Mathematics in algebraic terms and use this directly proportional to the cube of its form of expression to fi nd unknown radius, *r*cm. When the radius of the sphere quantities. is 60 cm, its weight is 4320 newtons. Find an equation connecting *w* and *r*.

IGCSE / O Level Understand and apply <u>x</u> **2** ln *yy yy yy yy yy yy yy yy yy yy yy yy yy yy yy yy* ln(20) =+ =+ ln 3 Mathematics ● laws of indices 4 Find and simplify an expression for *y* in

- laws of logarithms
terms of *x*.

Chapter 5 Integrate **3** Find :

|∫|1|d|
|---|---|---|
||31 31 31 −||
|∫|sin x|d x|

- standard functions **a** *x*
- using substitution
- using parts **b**
cos*x*

**c** *xx* ed ed ed ed ed ed −. ∫

Chapter 8 Decompose a compound fraction <u>2</u> with denominator **4** Find ∫(2 (2 (2 *xx* −+ −+ −+ −+ −+ −+ −+ −+ −+ −+ −+ −+ −+ −+ −+<u>)()(</u>31 31 31) d

*x*.

● **244** ●

- () () () () () ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ *bc* () () () () () () ()
<u>2</u>

into its partial fractions and integrate the result. Review Copy-Cambridge University Press-Review Copy

*x²* Chapter 1 Sketch graphs of standard functions **5 a** Sketch the graph of *y* = e.

e.g. involving ln f(*x*) and e
f(*x*) <u>12e</u> *x* (including understanding end **b** 3e + *x* → *k* as *x* →∞.

behaviour as *x* →±∞). Find the value of the constant *k*.

##### What is a diff erential equation?

<u>ddy d²y</u> An equation that has a derivative such as or 2 as one of its terms is called a d*x* d*x* <u>ddy</u> **differential equation**. When the equation has the fi rst derivative as one of its terms, d*x* <u>ddy</u>2 it is called a **fi rst order** differential equation. For example, the equation = 3*x* is an d*x* alternative way of representing the relationship *yx* =+ =+ =+ =+ =+ <u>3</u> *C*, where *C* is a constant.

To solve a differential equation, we integrate to fi nd the direct relationship between *x* and *y*, such as *yx* =+ =+ =+ =+ =+ <u>3</u>

*C*. The direct equation *yx* =+ =+ =+ =+ =+
<u>3</u> *C* is called the **general solution** <u>ddy</u>2 of the differential equation = 3*x*. To fi nd a **particular solution**, we must have further d*x* information that will enable us to fi nd the value of *C*.

The solution of an algebraic equation is a number or set of numbers. The solution of a differential equation is a function.

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

##### Chapter 10: Diff erential equations

In this chapter, we will learn the initial skills needed to master the solution of one type of fi rst order differential equations. These simple skills will be the foundation for further study of this subject.

You might wonder about the usefulness of such seemingly abstract equations in the real world. In fact, differential equations are excellent mathematical models for many real-life situations and are essential to solve many problems. First order differential equations can model rates of change, in other words, the rate at which one quantity is increasing or decreasing with respect to another quantity. There are many examples in the physical world that can be modelled using such relationships. A few examples are the rate of increase of the number of bacteria in a culture, simple kinematics problems, the rate of decrease of the value of a car and the rate at which a hot liquid cools.

##### 10.1 The technique of separating the variables

<u>ddy</u>2 Solving a differential equation such as =+ =+ =+ =+ =+ 6(*x* 1) can be done using an d*x* anti-differentiation approach.

We know, from the Pure Mathematics 1 Coursebook, Chapter 9, that if we integrate both sides with respect to *x*, we have:

|d||
|---|---|
||∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫|

2 d6 d6 *xx* =+ =+ =+ =+ =+ =+ =+ =+ =+ =+ =+ (1 (1 (1)d)d)d*x*

<u>6(x + 1)</u> 3 *y* = + *C* 3 *yx* =+ =+ =+ =+ =+ =+ =+ 2(2( 1) 3 + *C* **245** <u>d</u>2 Notice that the fi rst line on the left-hand side is d6 d6 *xx* =+ =+ =+ =+ =+ =+ =+ =+ =+ =+ =+ (1 (1 (1)d)d)d*x* and from ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ <u>ddy</u> anti-differentiation we can see that, if we integrate with respect to *x* we obtain an Review Copy-Cambridge University Press-Review Copy d*x* expression for *y*.

<u>ddy</u> This means that d. d. d. =.. is equivalent to d*y* = ..., which is *y* =… ∫d*x*∫

##### This result is generally true.

##### KEY POINT 10.1

|Integrating an expression of the form f( y)||d dy with respect to x is equivalent to integrating f( y)|
|---|---|---|
|with respect to y.||dx|
|Therefore|f( y) d dy dx is equivalent to|f( yy)d)d.|
||dx||

#### ∫ ∫

<u>dy</u>2<u>ddy</u> The differential equation =+ 6(*x* 1) is easy to solve because is equal to a d*x* d*x* function that we know how to integrate. This is not always the case.

<u>ddy</u> How do we solve the differential equation = *xy* when *y*.0? d*x* As it is written, we cannot integrate both sides with respect to *x* and fi nd a solution.

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

Separating the variables in the expression *xy* means that we are then able to integrate.

<u>ddy</u> = *xy* Separate the variables *x* and *y*. d*x* 1d 1d<u>y</u> = *x* Form integrals of both sides with respect to *x*. *y* d*x* <u>yyy</u>

### ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫

dd *xx xx xx xx xx x* *yy* d*xx*

### ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫

dd *yx yx yx yx yx yx yx yx yx x* Integrate each side. *yy*

*x²*

||y|
|---|---|
|y|. 0.|

ln *yA* += += += + *B* The modulus of is not required as 2 we know that

<u>x²</u> ln *y* =+ =+ *C* The constants of integration can be combined 2 as one term and we only need to write a constant on one side.

<u>x²</u> 2 + *C* *y* = e This is the general solution of the differential <u>x</u> 2 equation as we do not know the value of the *yD* = e2 where *D* = e *C* **arbitrary constant** *C*.

**246** When we have further information, we can fi nd the particular solution of the differential solution given by that information. <u>ddy</u> For example, solve = *xy* given that *y* = 2 when *x* = 0. d*x*

## Review Copy-Cambridge University Press-Review Copy

Using this information:

<u>x² 0</u> 2 ln *y* =+ =+ *C* and so ln 2 =+ =+ *C*, *C* = ln 2 2 2 <u>x²</u> 2 + ln 2 *y* = e This is the **particular** solution of the differential equation. <u>x²</u> *y* =× =× =× =× =× =× =× ee2 ln 2 Note that you often need to write your answer as

<u>x</u> 2an expression for *y* in terms of *x*. This commonly *y* = 2e2 means using laws of indices or logarithms.

By separating the variables we are rearranging the differential equation to the form <u>dyyy</u> f(*y*) = g(*x*). d*x*

<u>ddy</u> f(*y*) = g(*x*) (Note: Other variables may be used such as *v* d*x* and *t*.)

|d||dg dg|xx () () ()d||
|---|---|---|---|---|
||∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫|g(||xx)d)d|

*x*

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

<u>ddy</u> So, in the case where the derivative is : d*x*

- form *an expression in x only* on one side of the equation
<u>dyyy</u>

- form *an expression in y* × on the other side of the equation.
d*x* This gives us a form of the equation that can be integrated on both sides, one side with respect to *x* and the other side with respect to *y*.

##### WORKED EXAMPLE 10.1

<u>ddy 1 + x</u> The variables *x* and *y* satisfy the differential equation =. d*x* 2*y* It is given that *y* = 3 when *x* = 0.

Solve the differential equation and obtain an expression for *y* in terms of *x*.

##### Answer

Even though the question does not ask for it directly, you are expected to use the initial condition that you have been given to fi nd a particular solution.

<u>ddy 1 + x</u> Separate the variables *x* and*y*. = d*x* 2*y* Here we have moved the 22*y*. It was not essential to move the 2, we could have moved the *y* only. This would be just as valid as **247**

it would also give expressions that can be integrated.

<u>ddy</u>

## Review Copy-Cambridge University Press-Review Copy

2*y* =+ =+ =+ 1 *x* Form integrals of both sides with respect to *x*. d*x*

<u>d</u> d1 d1 =+ =+ () () () () () () () () () () () () () () d*x* ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫

=+ () () () () () () () () () 1d 1d *xx* Integrate each side.

### ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫

<u>2</u>*x²* *yx yx yx yx yx* =+ + *C* 2 *y* = 3 when *x* = 0. 0 2 90 =+ =+ =+ += += *CC CC CC CC CC CC*,9 2 <u>2</u>*x²* *yx yx yx yx yx* =+ + 9 2 <u>1</u>  <u>x² </u>2 *yx yx yx yx yx yx yx yx yx yx yx yx yx yx yx yx yx yx yx yx yx yx yx yx yx yx yx yx* =+ =+ =+ =+ =+ =+ =++ 9 You can check this by differentiating.  2 

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

##### WORKED EXAMPLE 10.2

23 2<u>ddy</u> Find the general solution of the differential equation (1 (1 (1 (1 (1 (1 (1 *xy* ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++)) *x* = 0. d*x*

##### Answer

<u>ddy</u>

|23 23 23 23|2|
|---|---|
|22 22 22 22|3|
||2|
|3 −− −− −− 32 32 32 −− −− −− 32 32 32|2|

(1 (1 (1 (1 (1 (1 (1 (1 (1 (1 (1 (1 (1 *xy* ++ ++ ++))))) *x* = 0 Separate the variables *x* and *y*. d*x*

*x²²* <u>ddddy</u> =−(1 (1 (1 (1 (1 (1 (1 (1 (1 (1 (1 (1 *xy*)) d*x* 1d 1d*y* <u>(1 (1 (1 (1 (1 (1 (1)</u> Form integrals of both sides with respect to *x*. =− ** *y* d*x x* Here we are assuming that *y* ≠ 0. <u>d</u> d( d( d( d( d( *xx* =− =− =− =− =− =− − 1) d*x* ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫

d( d( d( =− =− =− =− =− =− *xx* − 1)1) dd Integrate each side. ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫

1 <u>1</u> −= −= −= −= 22 −+ −+ −+ *xC* 2*yx*

##### Is this the complete solution?

Earlier in the solution (at line **) we assumed that *y* ≠ 0. However, when *y* = 0, the original differential equation <u>dyyy</u> 0 becomes == == == == 2

0. Since *y* = 0 is the *x*-axis, it is true that its gradient is 0 at all points and so *y* = 0 is also
d*x x* **248** a solution of the differential equation and must be included for the general solution to be complete. <u>1 1</u> The complete general solution is, therefore, −= −= −= 2 −+ *xC xC xC* or *y* = 0. 2*y x*

## Review Copy-Cambridge University Press-Review Copy

<u>ddy</u> In Worked example 10.2, we saw that, when rearranging to the form f(*y*) = g(*x*), there d*x* <u>1</u> are cases where f(*y*) is a function such as, for example, 3. In these cases, a value (or *y* values) of *y* must be excluded for the separation of the variables to take place.

As a fi nal step, when fi nding the general solution in these cases, we must check if the value (or values) we have excluded when separating the variables gives (or give) a valid solution of the original differential equation. When they do, we should include them.

##### WORKED EXAMPLE 10.3

<u>dx xx xx ((300 300 −)</u> It is given that, for 0,, *xx* 300, = and *x* = 50 when *t* = 0. Find the particular solution of the d*t* 600 differential equation, giving your answer as an expression for *x* in terms of *t*.

##### Answer

<u>dx xx xx ((300 300 −)</u> Separate the variables. The derivative is with = d*t* 600 respect to *t* and so the expression in *x* needs to be moved to the left-hand side.

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

1 <u>dx</u> 1 = Form integrals of both sides with respect to *t*. *xx* ((300 300 −) d*t* 600 <u>1</u> d 1 Note that it is simpler to leave the 600 on the *tt* dd right-hand side here. ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫() 1 1 Write the expression on the left in terms of its *xt* dd ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫() partial fractions. 1  11  1 *xt* dd Integrate each side. 300∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫   1 1 The modulus signs are not required as we () () () () () () () () () () () () () () () () () () () () () =+ =+ =+ =+ *tC* 300 600 know that 0,, <u>xx</u> 300. <u>1</u> ln *xx* −− −− −− −− −− ln( ln(300 300) =+ =+ =+ =+ *tC* 2 *x* <u>1</u> ln =+ =+ =+ =+ *tC x* = 50 when *t* = 0. 300 − *x* 2 <u>50 50</u> *CC CC* = lnln,l,l,l = n0.2 300 300 − 50 50 *x* <u>1</u> ln =+ =+ =+ =+ *t* ln 0.2 300 − *x* 2 *x* 2 *t*+ ln 0.2 <u>1</u> = e 300 − *x* <u>1</u> *t* *x* 2 ln 0.2 =× =× =× =× =× =× =× ee 300 − *x* <u>1</u> *t* *xx xx xx xx xx* =− =− =− =− =− =− =− =− =− =− =− =− =− =− =− 0.0.2e 2e<u>22</u>((300 300) **249** <u>1</u> *tt tt* <u>1</u> *xx xx xx* += += += += += += += += += += += += += += += += += 0.0.0.2e 2e 2e260 60e²² <u>1</u> *tt tt* <u>1</u> *x*(1 += += += += += += += += += 0.2e2)6)6 0e 0e22

## Review Copy-Cambridge University Press-Review Copy

<u>1</u> *t* <u>60e²</u> *x* = <u>1</u> 2 *t* 10 +.2e

##### <u>EXERCISE 10A</u>

**1** Find the general solution of each of the following differential equations. dy3d*A*2d*s* **a** =− =− =− =− =− *x* 6 **b** =π 22 *r* **c** *s* =+ =+ =+ =+ =+ cos(*t* 5) d*x* d*r* d*t*

−1d*V* dd*y y* + 1 *xx xx xx xx xx xx xx xx xx xx xx* += += += += += += += += secs in *yy* d*yyyy* 1 **d** *V* = 2 **e** = **f** d*t* d*x x* d*x*

**2** Find the particular solution for each of the following differential equations, using the values given.

2<u>ddy</u> **a** cos *x* = *y* given *y* = 5 when *x* = 0 d*x* <u>ddy xx −</u> **b** *xy* = given *y* = 4 when *x* = 3 d1 d1 d1 − *y*

<u>ddy</u>*xy* − Given that = e and *y* = ln 2 when *x* = 0, obtain an expression for *y* in d*x* terms of *x*.

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

**4** The gradient of a curve at the point (, (, (, *xy*) is 5*yx* 33.

**a** Write down the differential equation satisfi ed by *y*.

**b** Given that the curve passes through the point (1,1), fi nd *y²* as a function of *x*.

<u>1 A B</u> **5 a** Express in the form +. **TIP** (2 −+ −+ −+ −+ −+ −+ −+ −+ −+ *xx xx*)()()( 1) 21 21 21 21 21 − *x x* +

**b** The va riables *x* and *t* satisfy the differential equation *x*ɺ is an alternative <u>dx</u> <u>dx</u> notation for d *t*. =− (( (( (( (( (( (( (( (( *xx xx xx xx xx xx xx xx xx xx*)))))))))))))))))))))). d*t* It is given that *t* = 0 when *x* = 0.

**i** Solve this differential equation and obtain an expression for *x* in terms of *t*.

**ii** State what happens to the value of *x* when *t* becomes large.

**PS 6** The varia bles *w* and *t* satisfy the differential equation <u>dw</u>2 =− =− =− =− =− =− =− 0.001(100 *w*). d*t*

Given that when *t* = 0 *w* = 0, show that the solution to the differential equation <u>1000</u> can be written in the form *w* =− =− =− 100. *t* + 10 <u>dx2</u> **7** Solve the differential equation 4 =− =− =− (3*xx xx xx xx xx xx xx*)cos*t* given that *x* = 0.4 when d*t* *t* = 0. Give your answer as an expression for *x* in terms of *t*. **250** 2 <u>ddy x − 1</u> **8** Find the general solution of the differential equation *xy* = *y*+1. d*x* e <u>ddy 1 + y²</u> **9** Find the equation of the curve that satisfi es the equation = 2 Review Copy-Cambridge University Press-Review Copy d*x* 4 + *x* and passes through the point (0,1). Give your answer in the form *yx* = f(f().

3<u>ddy</u> **10** Find the general solution of the equation *x* += += += += += 21 *y*. d*x* <u>dx2</u> **11** Solve the differential equation = 4c *xt xt xt xt xt xt xt* os given that *x* = 1 when *t* = 0. d*t* Give your answer as an expression for *x* in terms of *t*.

2 *t²* **12 a** Use the substitution *ut* = to fi nd *te* d*t*. ∫ *t* <u>2</u> <u>dx te (5 (5 (5 (5 (5 (5 (5 +)</u> **b** Solve the differential equation = 2 given that *x* = 1 when *t* = 0. d*t x*

**PS 13** At a point with coordinates (, (, (, *xy*) the gradient of a particular curve is directly proportional to *xy²*. At a particular point *P* with coordinates (1,3) it is known that the gradient of this curve is 6.

Find and simplify an expression for *y* in terms of *x*.

**14** The variables *x* and *t* satisfy the differential equation 32 32 32 32 32<u>ddx</u>4 (3*xx* += += += += += += += += += += += += += += 2) 2) 2) 2) 2) *kx* (3(3(3 + *x*) d*t* for *x*. 0 where *k* is a constant. When *t* = 0, *x* = 1 and when *t* = 0.5, *x* = 2.

Solve the differential equation, fi nding the exact value of *k*, and show

*t*<u>xx +++</u> that 7 =.

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

<u>1</u> **15 a** Use the substitution *ux ux ux ux ux* ln to fi nd d*x*.

### ∫xx xx xx ln

**b** Given that *xy xy xy*.. 0,0,0,0, 0, fi nd the general solution of the differential equation <u>ddy y</u> ln*x* =. d*x x*

**M 16** A type of medicine that reacts to strong light can be used to treat some skin problems.

It is important that, after treatment with this type of medicine, the person stays out of bright light until the amount of medicine remaining in the skin is at a safe level.

Jonty is treated with a medicine of this type.

|After the treatment, 65 mg remains in the treated area of skin.||TIP|
|---|---|---|
|The rate at which the medicine disappears from the treated area of Jonty’s skin||Notice that the rate|
|is modelled by the differential equation|dm =−0.05 m, where m is the amount of dt|at which the medicine disappears is with|
|medicine, in milligrams, in the skin t hours after the treatment.||respect to time but the|
|Jonty is safe to go out in bright light when no more than 6mg of the medicine||words ‘with respect to time’ are usually not|

remains in his skin. included. How long must Jonty wait before he goes out in bright light?

##### EXPLORE 10.1

**251**

##### Newton’s law of cooling or heating

Many differential equations arise from modelling natural laws and relationships. One

## Review Copy-Cambridge University Press-Review Copy

example is Newton’s law of cooling or heating:

The rate of change of temperature of an object is proportional to the difference in temperature of the object and its surroundings.

We defi ne *T* as the temperature of the object

##### t as time

*T₀₀* as the temperature of the object when *t* = 0

*s* as the constant temperature of the surroundings

##### k as the constant of proportionality.

##### Discuss the following.

- Why it is necessary to defi ne the variables and constants.
<u>dT</u>

- Why the differential equation =− =− =− =− =− =− =− *kT* () () () () (), *k*. 0 is satisfi ed by *T*.
d*t*

- Other possible correct ways to represent Newton’s law of cooling or heating as a differential equation with this set of defi ned variables and constants.
- Why the general solution of the given form of the differential equation may be written as: *Ts* −=*A*e
*kt* where *A* e. e. e. <u>C</u>

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

- How many arbitrary constants there are in the general solution of **any** fi rst order differential equation.
- Why the modulus in the general solution is required.
- How the general solution can be used to represent the temperature of an object cooling down or warming up.
##### 10.2 Forming a diff erential equation from a problem

The key to forming a differential equation from a problem is the successful interpretation of the language used in the question.

For example, when you are given a problem such as:

The rate of increase of **the number of bacteria in a dish** is *k* times **the number of** **bacteria in the dish**. The number of bacteria present in the dish at time *t* is *x*…

Replacing the words **the number of bacteria in a dish** by *x* the problem becomes:

The rate of increase of *x* is *k* times *x*.

This rate of increase of *x* is with respect to time, *t*, and is much easier to translate into a <u>dx</u> differential equation: = *kx*. **252** d*t*

##### WORKED EXAMPLE 10.4

## Review Copy-Cambridge University Press-Review Copy

Velocity is defi ned to be the rate of change of displacement with respect to time.

The velocity of a particle at time *t* seconds is inversely proportional to its displacement, *s* metres, from an origin, *O*.

**a** Form a differential equation to represent this data.

**b** Initially, the particle has a displacement of 2 metres from *O*. After 1 second, the particle has a displacement of 5 metres from *O*. Solve the differential equation giving your answer in the form *ts* = f(f().

**c** Find *t* when the displacement of the particle from *O* is 10 metres.

##### Answer

**a** The **velocity** of a particle at time *t* seconds **is inversely proportional to** its **displacement**, *s* metres, from the origin, *O*.

d*s* d*s* 1 d*s k* *v* = and so ∝, which means that = At the moment, you do not have enough d*t* d*ts* d*t s* information to fi nd the constant of proportionality, *k*

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

<u>ds k</u> **b** = Separate the variables *s* and *t*. d*t s* <u>ds</u> *s* = *k* Form integrals of both sides with respect to *t*. d*t*

<u>ds</u> *s* dd *tk tk tk tk tk t*

### ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫t

*ss ss ss* dd *kt kt kt* Integrate each side.

### ∫∫ ∫∫ ∫∫ ∫∫ ∫∫

*s²* =+ =+ =+ *kt C s* = 2 when *t* = 0. 2 <u>s²</u> *C* == == == == 2, *kt* + 2 *s* = 5 when *t* = 1. 2 5 2 =+ =+ =+ *kk* 2,2, = 10.5 2 *s²* <u>21</u> =+ =+ =+ =+ *t* 2 Write in the form *ts* = f(f( ). 2 2 <u>s² − 4</u> *t* = 21

**c** Find *t* when *s* = 10

<u>100 − 4</u> *t* = == == == 4.5714... 4.57 seconds correct to 3significant figures. 21 **253**

##### WORKED EXAMPLE 10.5

## Review Copy-Cambridge University Press-Review Copy

The population density, *P*, of a town can be modelled as a continuous variable.

##### In the year when records began:

- the population density, *P*, of the town was increasing at the rate of 0.5 people per hectare per year
- the population density of the town was 2 people per hectare.
It is suggested that, *t* years after records began, the rate of increase of the population density is inversely proportional to the square of the population density.

**a** Form a differential equation to model this information.

**b** Solve the differential equation, giving your answer in the form *Pt* = f(f( ).

**c** The table shows the actual population density of the town, every 5 years for the fi rst 20 years after records began.

**t** 5 10 15 20

**P** 3.5 4 5.5 7

Comment on how good a fi t the model is to the actual data in the longer term.

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

##### Answer

**a** The rate of increase of *P* is inversely proportional to *P²*:

d*P* 1d *P k* ∝= ∝= ∝= ∝= ∝= 22 d*t P* dd*tt PP* <u>dP</u> When *t* = 0, = 0.5 and *P* = 2, therefore: d*t*

|d P|k =|
|---|---|
|d t|P|
|d P|2|
||=|
|d|tP|

*k*

20.5 == == == == ==,2,2,2 *k*
4

<u>dP</u> 2 Separate the variables *P* and *t*. **b** = 2 d*tP*

2<u>dP</u> *P* = 2 Form integrals of both sides with respect to *t*. d*t*

<u>dP</u> *P* d2 *tt tt tt tt tt tt tt tt tt* d

### ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫t

*PP PP PP PP PP* d*t* Integrate each side.*tP tP tP tP* == == == == == == 0, 2

### ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫

*P³* =+ =+ =+ =+ =+ 2*tC* 3 **254** <u>8</u> = *C* 3 *P³* <u>8</u> Write in the form *Pt* = f(f( ). =+ =+ =+ =+ =+ 2*t* 3 3

## Review Copy-Cambridge University Press-Review Copy

*Pt* 33 =+ =+ =+ =+ =+ 68 68 68 *Pt Pt* =+ =+ =+ =+ =+ =+ =+ =+ 33 68 68 68

##### c c ..................................................

|t|5|10|15|20|
|---|---|---|---|---|
|P|3.5|4|5.5|7|
|Model prediction (to 2 signifi cant fi gures)|3.4|4.1|4.6|5.0|

In the longer term, the model is not a particularly good fi t as the values it generates when time increases are under-estimates of the known data.

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

##### WORKED EXAMPLE 10.6

The value, $*V*, of a motorbike as it gets older can be modelled as a continuous variable.

A model is suggested to estimate the rate of decrease of the value of the motorbike. This model is that the value *V* when the motorbike is *t* months old decreases at a rate proportional to *V*.

**a** Write down a differential equation that is satisfi ed by *V*.

**b** The motorbike had a value of $10 000 when it was new.

Solve the differential equation, showing that *V* = 10 000e −*kt*, where *k* is a positive constant.

**c** After 3 years the motorbike has lost half of its value when new.

Find the value of the motorbike when it was 2 years old.

##### Answer

**a** The rate of decrease of *V* is proportional to *V*. This describes exponential decay. The rate is decreasing and so the constant of <u>dV dV</u> proportionality is negative. ∝ *V* and so =−*kV*, where *k* is a positive constant. d*t* d*t*

||d V|=− kV|
|---|---|---|
||d t 1d V|=− k|
|V 1d|d t|dd dd dd =− ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫|

**b** Separate the variables *V* and *t*.

Form integrals of both sides with respect to *t*. **255**

*t*

<u>1</u> Review Copy-Cambridge University Press-Review Copy dd dd dd *Vk* =−*t* Integrate each side.

### ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫

ln *Vk Vk* =− *tC* + *t* = 0, *V* = 10 000

ln 10 000 = *C* For this particular solution, *V* is positive and so the modulus is not required.

ln*Vk Vk Vk t* + ln 10 000 Write in the form *Vt* = f(f( ).

*V* = e −+ −+ −+ *kt* ln 10 000

*V* =× =× =× =× =× =× =× ee −<u>kt</u> ln 10 000

*V* = 10 000e −*kt*

**c** *V* = 10 000e −*kt* *t* = 3, *V* = 5000 5000 = 10 000e −3*k*

<u>5000</u>−3*k* = e 10 000 ln 0.53 =−*k* <u>− ln 0.5</u> *k* =

−2 <u> − ln 0.5 </u>   *V* = 10 000e *V* == == == $6299.605 …. $6300

correct to 3 signifi cant fi gures

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

##### <u>EXERCISE 10B</u>

**M 1** Write the following as differential equations. Do **not** solve the equations.

**a** For height *h* and time *t*:

The rate of decrease of the height of water in a tank is proportional to the square of the height.

**b** For number of infected cells *n* and time *t*:

The rate of increase of the number of infected cells in a body is proportional to the number of infected cells in the body at that time.

**c** For velocity *v* and time *t*:

The rate of decrease of the velocity of a particle moving in a fl uid is proportional to the product of *v* and *v* + 1.

**d** For volume *V* and time *t*:

The rate at which oil is leaking from an engine is proportional to the volume of oil in the engine at that time.

**e** For cost *C* and time *t*:

The rate at which the cost of an item increases is proportional to the cube of the cost at that time.

**f** For speed *v* and time *t*: **256** The rate of change of the speed of a skydiver just after he jumps out of a <u>t</u> plane is inversely proportional to e².

**M 2** A large tank is full of water. The tank starts to leak. Review Copy-Cambridge University Press-Review Copy

*t* seconds after the tank starts to leak the depth of water in the tank is *x* metres.

The rate of decrease of the depth of water is proportional to the square root of the depth of water.

**a** Write down a differential equation relating *xt*,, and a constant of proportionality.

**b** At the instant when water starts to leak from the tank, the depth of water is

6.25 metres. Given that 120 seconds after the tank starts to leak, the depth of water is 4 metres, solve the differential equation, expressing *t* in terms of *x*.
**c** Find the time it takes for the depth of the water to halve.

**M 3** The cost of designing an aircraft, $*A* per kilogram, at time *t* years after 1950 can be modelled as a continuous variable. The rate of increase of *A* is directly proportional to *A*.

**a** Write down a differential equation that is satisfi ed by *A*.

**b** In 1950, the cost of designing an aircraft was $12 per kilogram. Show that *A* = 12e *kt*, where *k* is a positive constant.

**c** After 25 years, the cost of designing an aircraft was $48 per kilogram. Find the cost of designing an aircraft after 60 years.

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

**M 4** A liquid is heated so that its temperature is *x*°C after *t* seconds. It is given that the rate of increase of *x* is proportional to (100 − *x*). The initial temperature of the liquid is 25 °C.

**a** Form a differential equation relating *xt*,, and a constant of proportionality, *k*, to model this information.

**b** Solve the differential equation and obtain an expression for *x* in terms of *t* and *k*.

**c** After 180 seconds the temperature of the liquid is 85 °C. Find the temperature of the liquid after 195 seconds.

**d** The model predicts that *x* cannot exceed a certain temperature. Write down this maximum temperature.

**M 5** The diagram shows an inverted cone fi lled with liquid paint. <u>10 cm</u>

An artist cuts a small hole in the bottom of the cone and the liquid paint drips out at a rate of 16 cm³ per second. At time *t* seconds after 15 cm the hole is cut, the paint in the cone is an inverted cone of depth *h*cm. <u>dV 4</u>2 **a** Show that =π =π =π =π *h*. d*h* 9 <u>dh</u> **b** Hence fi nd an expression for. d*t* **c** Solve the differential equation in **part b**, giving *t* in terms of *h*.

**d** Find the length of time it takes for the depth of the paint to fall to 7.5cm.

**M 6** The size of a population, *P*, at time *t* minutes is to be modelled as a continuous **257** variable such that the rate of increase of *P* is directly proportional to *P*.

**a** Write down a differential equation that is satisfi ed by *P*.

**b** The initial size of the population is *P*00.

## Review Copy-Cambridge University Press-Review Copy

Show that *PP* =00e *kt*, where *k* is a positive constant.

**c** The size of the population is 1. 5*P₀₀* after 2 minutes. Find when the population will be 3*P₀₀*.

**M 7** A ball in the shape of a sphere is being fi lled with air. After *t* seconds, the radius of the ball is *r*cm. The rate of increase of the radius is inversely proportional to the square root of its radius. It is known that when *t* = 4 the radius is increasing at the rate of 1. 4cms −1 and *r* = 7.84.

**a** Form a differential equation relating *r* and *t* to model this information.

**b** Solve the differential equation and obtain an expression for *r* in terms of *t*.

**c** How much air was in the ball at the start?

**M 8** Maria makes a large dish of curry on Monday, ready for her family to eat on **TIP** Tuesday. She needs to put the dish of curry in the refrigerator but must let it cool to room temperature, 18 °C, fi rst. The temperature of the curry is 94 °C when it You must defi ne your has fi nished cooking. own variables in this question as they have At 6pm, Maria places the hot dish in a sink full of cold water and keeps the not been defi ned for water at a constant temperature of 7C ° by running the cold tap and stirring the you. dish from time to time. After 10 minutes, the temperature of the curry is 54 °C.

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

It is given that the rate at which the curry cools down is proportional to the difference between the temperature of the curry and the temperature of the water in the sink.

At what time can Maria put her dish of curry in the refrigerator?

**M 9** The half-life of a radioactive isotope is the amount of time it takes for half of the isotope in a sample to decay to its stable form.

Carbon-14 is a radioactive isotope that has a half-life of 5700 years.

It is given that the rate of decrease of the mass, *m*, of the carbon-14 in a sample is proportional to its mass.

A sample of carbon-14 has initial mass *m₀*. What fraction of the original amount of carbon-14 would be present in this sample after 2500 years?

**M 10** Anya carried out an experiment and discovered that the rate of growth of her hair was constant. At the start of her experiment, her hair was 20 cm long. After 20 weeks, her hair was 26 cm long. Form and solve a differential equation to fi nd a direct relationship between time, *t*, and the length of Anya’s hair, *L*.

**M 11** A bottle of water is taken out of a refrigerator. The temperature of the water in the bottle is 4C °. The bottle of water is taken outside to drink. The air temperature outside is constant at 24 °C.

It is given that the rate at which the water in the bottle warms up is proportional to the difference in the air temperature outside and the temperature of the water **258** in the bottle.

After 2 minutes the temperature of the water in the bottle is 11°C.

**a** How long does it take for the water to warm 20 °C?

## Review Copy-Cambridge University Press-Review Copy

**b** According to the model, what temperature will the water in the bottle eventually reach if the air temperature remains constant and the water is not drunk?

**M 12** The number of customers, *n*, of a food shop *t* months after it opens for the fi rst time can be modelled as a continuous variable. It is suggested that the number of customers is increasing at a rate that is proportional to the square root of *n*.

**a** Form and solve a differential equation relating *n* and *t* to model this information.

**b** Initially, *n* = 0, and after 6 months the food shop has 3600 customers. Find how many complete months it takes for the number of customers to reach 6800.

**c** The food shop has a capacity of serving 14 000 customers per month. Show that the model predicts the shop will have reached its capacity sometime in the 12th month.

**M 13** Doubling time is the length of time it takes for a quantity to double in size or value.

The number of bacteria in a liquid culture can be modelled as a continuous variable and grows at a rate proportional to the number of bacteria present. Initially, there are 5000 bacteria in the culture. After 3.5 hours there are a million bacteria.

**a** What is the doubling time of the bacteria in the culture?

**b** What assumption does the model make about the growth of the bacteria and how realistic is this assumption?

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

##### EXPLORE 10.2

##### Modelling growth

Many of the models we have been using have assumed exponential growth. This type of growth is unlimited as the rate of growth of a population is proportional to the size of the population at that time.

<u>dP</u> This means that = *kP*. d*t*

Is an exponential growth model appropriate for modelling the population of the planet Earth in the long term?

It is thought that the maximum capacity of the Earth is about 10 billion people.

In 1987, the population of the Earth was about 5 billion people and the growth rate of the population was about 1. 84%.

Some people think that the problem of the Earth’s increasing population can be solved by sending some people to live on other planets, such as Mars. In 2031, the fi rst people to live on Mars will launch into space. The environment on Mars is different to Earth and many challenges must be overcome. This will all take time.

When a population is modelled as growing **exponentially** at a **constant** rate of *r* % per <u>70</u> year, it takes about years for the population to double. *r*

- Use the data given so far to investigate whether going to live on Mars is a good **259** solution to the population problem.
- Comment on any assumptions you have made in your investigation.
There is statistical evidence that the population of the Earth is not growing at a Review Copy-Cambridge University Press-Review Copy constant rate each year. In 2017, the growth rate had decreased to 1. 11% per year. The population needs resources to survive and so the growth rate has decreased as resources have decreased.

A different model, logistic growth, can be used when resources are limited. This model takes into account the changing growth rates of the population.

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

Here are sketch graphs of exponential and logistic growth models:

||Exponential growth|
|---|---|
||Maximum possible population|
|Population size||
|O|Time|

Logistic growth

Maximum possible population **260**

## Review Copy-Cambridge University Press-Review Copy

Population size

*O* Time

For example, for a population of size *P*,

<u>dP rP</u>() () () <u>−</u> = d*t k* where the constant *r* is the maximum natural growth rate (birth rate – death rate) and the constant *k* is the maximum capacity of the limited environment.

- Show that as time increases this model suggests that *P* tends to *k*.
- Comment on the limitations of this model.
## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

#### Checklist of learning and understanding

##### General procedure to solve a differential equation using the technique of separating the variables

<u>dyyy</u>

- Separate the variables f(*y*) = g(*x*).
d*x* <u>dyyy</u>

- Integrate both sides
#### ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫

*y* dg *xx xx xx xx xx xx xx xx xx* ()d*x* *x*

#### ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫ ∫∫

*yy yy yy* g(*xx xx xx*<u>)d</u>.

- Solve to fi nd a general solution.
- Substitute any given conditions to fi nd a particular solution.
- Check your answer by differentiating.
##### Other points to remember

- Take care with modulus signs in expressions such as ln f(*x*).
- When fi nding a general solution, check to see if any values excluded when the variables are separated are possible solutions.
**261**

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

##### <u>END-OF-CHAPTER REVIEW EXERCISE 10</u>

**1** The variables *x* and *y* satisfy the differential equation <u>dyyy</u>22 *yx yx yx* ++ = *x* ee d*x* and it is given that *y* = 0 when *x* = 0.

Solve the differential equation and obtain an expression for *y* in terms of *x*. **[9]**

**2** The number of birds, *x*, in a particular area of land is recorded every year for *t* years. *x* is to be modelled as a continuous variable. The rate of change of the number of birds over time is modelled by <u>dx xx xx xx xx xx xx xx (2500)</u> =. d*t* 5000 It is given that *x* = 500 when *t* = 0.

**a** Find an expression for *x* in terms of *t*. **[9]**

**b** How many birds does the model suggest there will be in the long term? **[1]**

**3** Given that *y* = 2 when *x* = 0, solve the differential equation

34 34 34<u>dy dy</u> *y* =+ =+ =+ =+ =+ =+ 1 *y* d*x* obtaining an expression for*y⁴* in terms of *x*. **[6]**

**4** The gradient of a curve is such that, at the point (, (, (, *xy*), the gradient of the curve is proportional to *xy xy*. At the point (3,4) the gradient of this curve is −5. **262** **a** Form and solve a differential equation to fi nd the equation of this curve. **[7]**

**b** Find the gradient of the curve at the point (3 − ,4). **[1]**

<u>50</u> Review Copy-Cambridge University Press-Review Copy **5 a** Given that *x*, 5, fi nd d*x*. **[3]**

### ∫(5 −− −− −− −− −− −− −− xx)()(10 10)

**b** A chemical reaction takes place between two substances *A* and *B*. When this happens, a third substance, *C*, is produced. After *t* hours there are 5 − *x* grams of *A*, there are 10 − *x* grams of *B* and there are *x* grams of *C* present. The rate of increase of *x* is proportional to the product of 5 − *x* and 10 − *x*. Initially, *x* = 0 and the rate of increase of *x* is 1 gram per hour. <u>dx</u> **i** Show that *x* and *t* satisfy the differential equation 50 =− =− =− (5 *xx xx*)()(10 10 −). **[1]** d*t* **ii** Solve this equation, giving *x* in terms of *t*. **[6]**

**iii** According to the model, approximately how many grams of chemical *C* are produced by the reaction? **[1]**

**6** The variables *x* and *y* are related by the differential equation <u>dyyy xe</u> *x* = 4. d5 *x y* It is given that *y* = 4 when *x* = 0. Find a particular solution of the differential equation and hence fi nd the value of *y* when *x* = 3.5. **[8]**

<u>4y³</u> **7 a** Use the substitution *uy uy* =− =− =− =− =− =− 1 to fi nd ∫

d. *yyy* **[1]**
*y⁴* − 1 <u>dyyy (2xy xy xy xy xy xy xy xy xy xy +− +− +− +− +− +− +− 1)</u> **b** Given that =, *y* = 3 when *x* = 1, fi nd a relationship between *x* and *y*. **[6]** d*x xy*

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

**8** The height, *h* metres, of a cherry tree is recorded every year for *t* years after it is planted. It is thought that the height of the tree is increasing at a rate proportional to 8 − *h*. When the tree is planted it is 0.5 metres tall and after 5 years it is 2 metres tall.

**a** Form and solve a differential equation to model this information. Give your answer in the form *ht* = f(f( ). **[6]**

**b** According to the model, what will the height of the cherry tree be when it is fully grown? **[1]**

**9** The variables *x* and *y* satisfy the differential equation <u>dyyy</u>3(*xy* ++) = e and *y* = 0 when *x* = 0. d*x*

Solve the differential equation and obtain an expression for *y* in terms of *x*. **[6]**

**10** At the start of a reaction, there are *x* grams of chemical *X* present. At time *t* seconds after the start, the rate of decrease of *x* is proportional to *xt*.

**a** Using *k* as constant of proportionality, where *k*. 0, form a differential equation to model this reaction rate. **[1]**

**b** Solve the differential equation obtaining a relation between *xt*,, and *k*. **[5]**

**c** Initially, there are 150 grams of chemical *X* present and after 10 seconds this has decreased to 120 grams. Find the time after the start of the reaction when the amount of chemical *X* has decreased to 1 gram. **[3]** **263** <u>1</u> **11 a** Using partial fractions fi nd ∫ d*P*. **[4]** *PP PP PP PP PP* (5) <u>dP</u> **b** Given that *P* = 3 when *t* = 0, solve the differential equation =− *PP PP PP PP PP PP PP* (5), obtaining an expression d*t*

## Review Copy-Cambridge University Press-Review Copy

for *P* in terms of *t*. **[4]**

**c** Describe what happens to *P* when *t* →∞. **[1]**

**12** The population of a country was 50 million in 2000 and 60 million in 2010. The rate of increase of the population is modelled by <u>dP kP(100 − P)</u> = d*t* 100 Use the model to predict the population of the country in 2025. **[7]**

**13 a** Use the substitution *ux* = 2 to fi nd *xx* sisind nd nd nd nd 2

*x*. **[3]**
∫ <u>dyyy xx xx xx xx xx sin</u> 2 **b** Given that =, *y* =−1 when *x* = 0, fi nd a relationship between *x* and *y*. **[5]** d*x y*

##### 14 Solve the differential equation

<u>dyyy tanx</u> = 3*y* d*x* e

given that *x* = 0 when *y* = 0. Give your answer in the form *yx yx yx yx yx* f(). **[6]**

**15** There are 2000 mice in a fi eld. At time *t* hours, *x* mice are infected with a disease. The rate of increase of the number of mice infected is proportional to the product of the number of mice infected and the number of mice not infected. Initially 500 mice are infected and the disease is spreading at a rate of 50 mice per hour.

**a** Form and solve a differential equation to model this data. Give your answer in the form *tx* = f(f(). **[7]**

**b** Find how long it takes for 1900 mice to be infected. **[1]**

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy

**16** The variables *x* and *y* are related by the differential equation <u>dyyy</u>2 *x* =− =− =− 1. 1. 1. *yy* d*x* When *x* = 2, *y* = 0. Solve the differential equation, obtaining an expression for *y* in terms of *x*. **[8]**

*Cambridge International A Level Mathematics 9709 Paper 31 Q6 November 2012*

**17** The variables *x* and θ satisfy the differential equation

<u>dx</u>2 =+ =+ =+ =+ =+ (2 (2 (2)sin 2, θ dθ

and it is given that *x* = 0 when θ = 0. Solve the differential equation and calculate the value of <u>1</u> *x* when θ =π =π =π, giving your answer correct to 3 signifi cant fi gures. **[9]** 4 *Cambridge International A Level Mathematics 9709 Paper 31 Q8 November 2015*

**264**

## Review Copy-Cambridge University Press-Review Copy

## Review Copy-Cambridge University Press-Review Copy
