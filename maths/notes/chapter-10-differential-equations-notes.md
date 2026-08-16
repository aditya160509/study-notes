# 📘 Chapter 10: Differential Equations - 9709 Pure Mathematics 3 (CAIE A Level Maths)

## Cambridge International AS & A Level Mathematics (9709) - Paper 3

> **The complete walkthrough:** syllabus topic 3.8 - first order differential equations with separable variables. Every technique explained rule-first, with fully solved examples in proper LaTeX. Almost always one multi-part question worth 6 to 11 marks on Paper 3.

---

# 📋 Table of Contents

1. [PART 1: Forming Differential Equations from Rate Statements](#part-1-forming-differential-equations-from-rate-statements)
2. [PART 2: Separation of Variables - All Integration Techniques](#part-2-separation-of-variables---all-integration-techniques)
3. [PART 3: Initial Conditions - General vs Particular Solutions](#part-3-initial-conditions---general-vs-particular-solutions)
4. [PART 4: Modelling Applications - Growth, Decay, Cooling, Tanks, Motion](#part-4-modelling-applications---growth-decay-cooling-tanks-motion)
5. [Formula Sheet](#formula-sheet)
6. [Quick Reference Card](#quick-reference-card)

---

# PART 1: Forming Differential Equations from Rate Statements

This part turns English sentences about rates into equations. The translation step is a language skill: "rate of change" means a derivative, "proportional to" means a constant times, "decrease" means a minus sign. Always state $k > 0$ and put the sign explicitly in the equation.

## 1.1 The Translation Table

| English | Mathematics |
|---|---|
| "rate of change of $x$" | $\displaystyle \frac{\mathrm{d}x}{\mathrm{d}t}$ (with respect to time $t$ unless another variable is named) |
| "rate of increase of $x$" | $\displaystyle \frac{\mathrm{d}x}{\mathrm{d}t}$ (taken positive) |
| "rate of decrease of $x$" | $\displaystyle -\frac{\mathrm{d}x}{\mathrm{d}t}$ (the equation carries the minus sign) |
| "directly proportional to $x$" | $= kx$, with $k > 0$ |
| "inversely proportional to $x^2$" | $\displaystyle = \frac{k}{x^2}$, with $k > 0$ |
| "proportional to the product of $x$ and $y$" | $= kxy$, with $k > 0$ |
| "proportional to $(M - x)$" | $= k(M - x)$, with $k > 0$ |

**Procedure:** (1) identify the dependent and independent variables, (2) fix the sign from "increase" (positive) or "decrease" (negative), (3) replace "proportional to $\dots$" by $k \times (\dots)$, (4) write $\frac{\mathrm{d}x}{\mathrm{d}t} = \pm k(\dots)$ and state $k > 0$.

> **Watch Out!** "Square of the height" means the power $h^2$, not $\frac{1}{2}$. A square-root proportionality is a completely different question.

### Example 1 - Six Translations, No Solving (source: coursebook Exercise 10B Q1)

> **Question:** Write each statement as a differential equation. Do not solve.
> (a) The rate of decrease of the height $h$ of water in a tank is proportional to the square of the height.
> (b) The rate of increase of the number $n$ of infected cells is proportional to $n$.
> (c) The rate of decrease of the velocity $v$ of a particle in a fluid is proportional to the product of $v$ and $v+1$.
> (d) The rate at which oil is leaking from an engine is proportional to the volume $V$ of oil in the engine.
> (e) The rate at which the cost $C$ of an item increases is proportional to the cube of the cost.
> (f) The rate of change of the speed $v$ of a skydiver is inversely proportional to $e^{t/2}$.

**Solution:**

$$(a) \quad \frac{\mathrm{d}h}{\mathrm{d}t} = -kh^2, \quad k > 0$$

$$(b) \quad \frac{\mathrm{d}n}{\mathrm{d}t} = kn, \quad k > 0$$

$$(c) \quad \frac{\mathrm{d}v}{\mathrm{d}t} = -kv(v+1), \quad k > 0$$

$$(d) \quad \frac{\mathrm{d}V}{\mathrm{d}t} = -kV, \quad k > 0$$

$$(e) \quad \frac{\mathrm{d}C}{\mathrm{d}t} = kC^3, \quad k > 0$$

$$(f) \quad \frac{\mathrm{d}v}{\mathrm{d}t} = \frac{k}{e^{t/2}} = ke^{-t/2}, \quad k > 0 \quad\checkmark$$

**What the examiner wants:** the minus sign carried by "decrease" or "leaking", and $k > 0$ stated on its own.

### Example 2 - Bacteria: Replacing Words with Symbols (source: coursebook 10.2)

> **Question:** The rate of increase of the number of bacteria in a dish is $k$ times the number of bacteria in the dish. Let $x$ be the number of bacteria at time $t$. Form a differential equation.

**Solution:**

Replace "the number of bacteria in the dish" by $x$:

$$\text{rate of increase of } x = k \times x$$

$$\frac{\mathrm{d}x}{\mathrm{d}t} = kx, \quad k > 0 \quad\checkmark$$

**What the examiner wants:** the substitution of the symbol $x$ into the sentence before translating - this is the step that makes the translation mechanical.

## 1.2 Proportionality Constants from Data

The constant $k$ is found from given data, in one of two ways:

- **Rate data:** you are told the value of the derivative at one instant. Substitute both the value and the rate into the DE and solve for $k$.
- **Two states of the system:** use the first condition to fix $C$, the second to fix $k$.

### Example 3 - Rate and Value at the Same Instant (source: coursebook Worked Example 10.5)

> **Question:** The population density $P$ of a town is modelled as a continuous variable. When records began, $P = 2$ people per hectare, increasing at 0.5 people per hectare per year. The rate of increase of $P$ is inversely proportional to $P^2$. Form a differential equation to model this.

**Solution:**

$$\frac{\mathrm{d}P}{\mathrm{d}t} = \frac{k}{P^2}, \quad k > 0$$

At $t = 0$: $\frac{\mathrm{d}P}{\mathrm{d}t} = 0.5$ and $P = 2$, so substitute both:

$$0.5 = \frac{k}{2^2} = \frac{k}{4}$$

$$k = 4 \times 0.5 = 2$$

$$\frac{\mathrm{d}P}{\mathrm{d}t} = \frac{2}{P^2} \quad\checkmark$$

**What the examiner wants:** using the derivative data (rate + value at the same instant) to find $k$ - not just forming the DE and stopping.

### Example 4 - Proportionality Constant from a Rate at $x = 1$ (source: CAIE MJ24 P31 Q11)

> **Question:** In a field there are 300 plants, all of which can be infected by a disease. At time $t$ there are $x$ infected plants. The rate of change of $x$ is proportional to the product of the number infected and the number not yet infected. Given $\frac{\mathrm{d}x}{\mathrm{d}t} = 0.2$ when $x = 1$, show that $x$ and $t$ satisfy $\frac{\mathrm{d}x}{\mathrm{d}t} = \frac{x(300-x)}{1495}$.

**Solution:**

$$\frac{\mathrm{d}x}{\mathrm{d}t} = kx(300-x), \quad k > 0$$

Substitute $\frac{\mathrm{d}x}{\mathrm{d}t} = 0.2$, $x = 1$:

$$0.2 = k(1)(300-1) = 299k$$

$$k = \frac{0.2}{299} = \frac{1}{5 \times 299} = \frac{1}{1495}$$

$$\frac{\mathrm{d}x}{\mathrm{d}t} = \frac{x(300-x)}{1495} \quad\checkmark$$

**What the examiner wants:** "product of the number infected and the number not yet infected" translates to $x(300 - x)$, and the rate at $x = 1$ fixes $k$.

### Example 5 - "Not Enough Information Yet" (source: coursebook Worked Example 10.4)

> **Question:** The velocity of a particle at time $t$ seconds is inversely proportional to its displacement, $s$ metres, from an origin $O$. Form a differential equation to represent this data.

**Solution:**

Velocity is the rate of change of displacement:

$$v = \frac{\mathrm{d}s}{\mathrm{d}t}$$

$$v \propto \frac{1}{s}$$

$$\frac{\mathrm{d}s}{\mathrm{d}t} = \frac{k}{s}, \quad k > 0 \quad\checkmark$$

**What the examiner wants:** at this stage you do not yet have enough information to find $k$ - leave it as a letter. Part (a) is worth its mark for the correct form alone.

## 1.3 Tanks: Rate In Minus Rate Out, Then the Chain Rule

For a container being filled and drained:

$$\frac{\mathrm{d}V}{\mathrm{d}t} = \text{rate in} - \text{rate out}$$

To convert to a DE in the depth $h$, use the chain rule:

$$\frac{\mathrm{d}h}{\mathrm{d}t} = \frac{\mathrm{d}V}{\mathrm{d}t} \times \frac{\mathrm{d}h}{\mathrm{d}V} = \frac{\frac{\mathrm{d}V}{\mathrm{d}t}}{\frac{\mathrm{d}V}{\mathrm{d}h}}$$

For a cylinder of base radius $r$: $V = \pi r^2 h$, so $\frac{\mathrm{d}V}{\mathrm{d}h} = \pi r^2$. For a cube of side 50 cm: $V = 2500h$, so $\frac{\mathrm{d}V}{\mathrm{d}h} = 2500$. For a cone, first express $r$ in terms of $h$ using similar triangles.

### Example 6 - Cylindrical Tank (source: CAIE ON24 P31 Q10)

> **Question:** A cylindrical tank has a base of radius 4 m. At time $t$ minutes the depth of water is $h$ m. With the tap open, water flows out at a rate proportional to the square root of the volume of water in the tank. Show that $\frac{\mathrm{d}h}{\mathrm{d}t} = -m\sqrt{h}$, where $m$ is a positive constant.

**Solution:**

$$V = \pi(4)^2 h = 16\pi h$$

$$\frac{\mathrm{d}V}{\mathrm{d}h} = 16\pi$$

$$\frac{\mathrm{d}V}{\mathrm{d}t} = -k\sqrt{V}, \quad k > 0$$

$$\frac{\mathrm{d}V}{\mathrm{d}t} = -k\sqrt{16\pi h} = -4k\sqrt{\pi h}$$

$$\frac{\mathrm{d}h}{\mathrm{d}t} = \frac{\mathrm{d}V}{\mathrm{d}t} \times \frac{\mathrm{d}h}{\mathrm{d}V} = \frac{-4k\sqrt{\pi h}}{16\pi}$$

$$\frac{\mathrm{d}h}{\mathrm{d}t} = -\frac{k}{4\sqrt{\pi}}\sqrt{h} = -m\sqrt{h}, \quad \text{where } m = \frac{k}{4\sqrt{\pi}} > 0 \quad\checkmark$$

**What the examiner wants:** the chain rule written explicitly, and the negative sign on the outflow term. Merging constants into one symbol $m$ is expected.

### Example 7 - Cube Tank with Inflow and Outflow (source: CAIE ON25 P32 Q10)

> **Question:** A tank is a cube of side 50 cm. At time $t$ seconds the depth of water is $h$ cm. Water pours in at $5000\ \text{cm}^3\,\text{s}^{-1}$ and pours out through a hole at a rate proportional to $h^2$. When $h = 20$, the depth is increasing at 0.4 cm s$^{-1}$. Show that $\frac{\mathrm{d}h}{\mathrm{d}t} = 2 - \frac{h^2}{250}$.

**Solution:**

$$V = 50 \times 50 \times h = 2500h$$

$$\frac{\mathrm{d}V}{\mathrm{d}h} = 2500$$

$$\frac{\mathrm{d}V}{\mathrm{d}t} = 5000 - kh^2$$

$$\frac{\mathrm{d}h}{\mathrm{d}t} = \frac{\mathrm{d}V}{\mathrm{d}t} \times \frac{\mathrm{d}h}{\mathrm{d}V} = \frac{5000 - kh^2}{2500}$$

$$\frac{\mathrm{d}h}{\mathrm{d}t} = 2 - \frac{kh^2}{2500}$$

Use the data: $h = 20$ and $\frac{\mathrm{d}h}{\mathrm{d}t} = 0.4$:

$$0.4 = 2 - \frac{k(20)^2}{2500} = 2 - \frac{400k}{2500}$$

$$\frac{400k}{2500} = 2 - 0.4 = 1.6$$

$$k = \frac{1.6 \times 2500}{400} = 10$$

$$\frac{\mathrm{d}h}{\mathrm{d}t} = 2 - \frac{10h^2}{2500} = 2 - \frac{h^2}{250} \quad\checkmark$$

**What the examiner wants:** "rate in minus rate out" first, then the chain rule. The sign of the outflow term is the most common error (see June 2023 examiner reports).

## 1.4 Defining Your Own Variables

Some questions do not define the variables for you. You must define them, for example "let $T$ °C be the temperature of the curry at time $t$ minutes", and state that $k$ is a positive constant. The syllabus note for topic 3.8 says the introduction and evaluation of a constant of proportionality is included - the constant $k$ is always yours to introduce and to find.

### Example 8 - Curry: Define Everything Yourself (source: coursebook Exercise 10B Q8)

> **Question:** Maria makes a large dish of curry. The temperature of the curry is 94 °C when it has finished cooking. At 6 pm she places the hot dish in a sink full of cold water kept at a constant 7 °C. The rate at which the curry cools down is proportional to the difference between the temperature of the curry and the temperature of the water in the sink. Form a differential equation relating the temperature of the curry to time.

**Solution:**

Define your own variables:

$$\text{let } T \text{ °C be the temperature of the curry at time } t \text{ minutes, with } k > 0$$

The sink water is at a constant $7$ °C, so the temperature difference is $T - 7$:

$$\text{rate of cooling} \propto (T - 7)$$

$$\frac{\mathrm{d}T}{\mathrm{d}t} = -k(T - 7), \quad k > 0 \quad\checkmark$$

**What the examiner wants:** a clear statement of what $T$ and $t$ mean and that $k > 0$ - the mark scheme credits defining variables that the question left undefined.

### Example 9 - Motorbike Value: Decrease Means Minus (source: coursebook Worked Example 10.6)

> **Question:** The value $V$ of a motorbike $t$ months old decreases at a rate proportional to $V$. Write down a differential equation satisfied by $V$.

**Solution:**

$$\frac{\mathrm{d}V}{\mathrm{d}t} \propto V, \quad \text{but the value is decreasing}$$

$$\frac{\mathrm{d}V}{\mathrm{d}t} = -kV, \quad k > 0 \quad\checkmark$$

**What the examiner wants:** the explicit minus sign with $k$ stated positive - "rate is decreasing, so the constant of proportionality is negative" is exactly the wording examiners want to see.

---

### Practice Questions - Part 1

1. **Q1 (Easy)** At a point with coordinates $(x, y)$ the gradient of a particular curve is directly proportional to $xy^2$. At the point $P(1, 3)$ the gradient is 6. Find and simplify an expression for $y$ in terms of $x$. (source: coursebook Exercise 10A Q13)

**Solution:**

$$\frac{\mathrm{d}y}{\mathrm{d}x} = kxy^2$$

At $(1, 3)$: $6 = k(1)(3)^2 = 9k$:

$$k = \frac{6}{9} = \frac{2}{3}$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{2}{3}xy^2$$

$$\int \frac{1}{y^2}\,\mathrm{d}y = \int \frac{2}{3}x\,\mathrm{d}x$$

$$-\frac{1}{y} = \frac{x^2}{3} + C$$

Use $(1, 3)$:

$$-\frac{1}{3} = \frac{1}{3} + C \;\Rightarrow\; C = -\frac{2}{3}$$

$$-\frac{1}{y} = \frac{x^2 - 2}{3}$$

$$y = \frac{3}{2 - x^2} \quad\checkmark$$

2. **Q2 (Medium)** The gradient of a curve at the point $(x, y)$ is proportional to $xy$. At the point $(3, 4)$ the gradient is $-5$. (a) Form and solve a differential equation to find the equation of the curve. (b) Find the gradient of the curve at the point $(-3, 4)$. (source: coursebook End-of-Chapter Review Exercise 10 Q4)

**Solution:**

$$\frac{\mathrm{d}y}{\mathrm{d}x} = kxy$$

At $(3, 4)$: $-5 = k(3)(4) = 12k$:

$$k = -\frac{5}{12}$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = -\frac{5}{12}xy$$

$$\int \frac{1}{y}\,\mathrm{d}y = \int -\frac{5}{12}x\,\mathrm{d}x$$

$$\ln y = -\frac{5}{24}x^2 + C$$

Use $(3, 4)$:

$$\ln 4 = -\frac{5}{24}(9) + C = -\frac{15}{8} + C$$

$$C = \ln 4 + \frac{15}{8}$$

$$\ln y = -\frac{5}{24}x^2 + \ln 4 + \frac{15}{8}$$

$$y = 4e^{15/8}e^{-5x^2/24} \quad\checkmark$$

(b) Substitute $x = -3$, $y = 4$ into the DE:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = -\frac{5}{12}(-3)(4) = \frac{60}{12} = 5 \quad\checkmark$$

3. **Q3 (Medium)** A chemical reaction takes place between substances $A$ and $B$, producing substance $C$. After $t$ hours there are $5 - x$ grams of $A$, $10 - x$ grams of $B$ and $x$ grams of $C$. The rate of increase of $x$ is proportional to the product of $5 - x$ and $10 - x$. Initially $x = 0$ and the rate of increase of $x$ is 1 gram per hour. Show that $x$ and $t$ satisfy $50\frac{\mathrm{d}x}{\mathrm{d}t} = (5 - x)(10 - x)$. (source: coursebook End-of-Chapter Review Exercise 10 Q5)

**Solution:**

$$\frac{\mathrm{d}x}{\mathrm{d}t} = k(5 - x)(10 - x), \quad k > 0$$

At $t = 0$: $x = 0$, $\frac{\mathrm{d}x}{\mathrm{d}t} = 1$:

$$1 = k(5)(10) = 50k$$

$$k = \frac{1}{50}$$

$$\frac{\mathrm{d}x}{\mathrm{d}t} = \frac{(5 - x)(10 - x)}{50}$$

$$50\frac{\mathrm{d}x}{\mathrm{d}t} = (5 - x)(10 - x) \quad\checkmark$$

4. **Q4 (Easy)** For speed $v$ and time $t$: the rate of change of the speed of a skydiver just after he jumps out of a plane is inversely proportional to $e^{t/2}$. Write this as a differential equation. (source: coursebook Exercise 10B Q1f)

**Solution:**

$$\frac{\mathrm{d}v}{\mathrm{d}t} = \frac{k}{e^{t/2}} = ke^{-t/2}, \quad k > 0 \quad\checkmark$$

---

# PART 2: Separation of Variables - All Integration Techniques

This part solves $\frac{\mathrm{d}y}{\mathrm{d}x} = f(x)g(y)$ by separating: everything in $y$ on the left, everything in $x$ on the right, then integrate both sides. The syllabus says any integration technique from topic 3.5 may be needed, so each subsection below is one technique, with fully solved examples.

## 2.1 The Separation Algorithm

**KEY POINT 10.1:** integrating $f(y)\frac{\mathrm{d}y}{\mathrm{d}x}$ with respect to $x$ is equivalent to integrating $f(y)$ with respect to $y$:

$$\int f(y)\,\frac{\mathrm{d}y}{\mathrm{d}x}\,\mathrm{d}x = \int f(y)\,\mathrm{d}y$$

**Method:** (1) rearrange to $f(y)\frac{\mathrm{d}y}{\mathrm{d}x} = g(x)$, (2) write $\int f(y)\,\mathrm{d}y = \int g(x)\,\mathrm{d}x$, (3) integrate, writing one $+C$ on one side only, (4) solve for the general solution, (5) substitute any given conditions, (6) check by differentiating. If you divided by an expression in $y$, check whether the excluded value is itself a solution.

### Example 1 - The Classic $xy$ Equation (Easy) (source: coursebook 10.1)

> **Question:** Find the general solution of $\frac{\mathrm{d}y}{\mathrm{d}x} = xy$ for $y \neq 0$.

**Solution:**

Separate the variables (divide by $y$):

$$\frac{1}{y}\,\frac{\mathrm{d}y}{\mathrm{d}x} = x$$

$$\int \frac{1}{y}\,\mathrm{d}y = \int x\,\mathrm{d}x$$

$$\ln|y| = \frac{x^2}{2} + C$$

Exponentiate both sides:

$$|y| = e^{x^2/2 + C} = e^C e^{x^2/2}$$

The $\pm$ merges into the constant:

$$y = Ae^{x^2/2}, \quad \text{where } A = \pm e^C \quad\checkmark$$

**What the examiner wants:** one constant only, on one side, and the modulus removed cleanly by absorbing the sign into $A$.

### Example 2 - The Excluded Value $y = 0$ (Medium) (source: coursebook Worked Example 10.2)

> **Question:** Find the general solution of $x^2\frac{\mathrm{d}y}{\mathrm{d}x} + (1 + x^2)y^3 = 0$.

**Solution:**

$$x^2\frac{\mathrm{d}y}{\mathrm{d}x} = -(1 + x^2)y^3$$

Divide by $y^3$ - this assumes $y \neq 0$:

$$\frac{1}{y^3}\,\frac{\mathrm{d}y}{\mathrm{d}x} = -\frac{1 + x^2}{x^2}$$

$$\int \frac{1}{y^3}\,\mathrm{d}y = -\int \left(1 + \frac{1}{x^2}\right)\mathrm{d}x$$

$$\int y^{-3}\,\mathrm{d}y = -\frac{y^{-2}}{-2} = \frac{1}{2y^2}\quad\text{... check: } \frac{\mathrm{d}}{\mathrm{d}y}\left(-\frac{1}{2y^2}\right) = y^{-3}$$

Actually, integrate carefully:

$$-\frac{1}{2y^2} = -\left(x - \frac{1}{x}\right) + C$$

Multiply through by $-1$:

$$\frac{1}{2y^2} = x - \frac{1}{x} + C$$

Now check the excluded value: when $y = 0$, the original equation reads $0 + 0 = 0$, true for every $x$, so $y = 0$ is also a solution:

$$\frac{1}{2y^2} = x - \frac{1}{x} + C \quad \text{or} \quad y = 0 \quad\checkmark$$

**What the examiner wants:** the check for the excluded value $y = 0$ - the one mark most candidates lose on this type. The coursebook makes it a numbered checklist step.

## 2.2 Standard Integrals and Chain-Rule Factors

| Integral | Result |
|---|---|
| $\displaystyle \int x^n\,\mathrm{d}x$ | $\displaystyle \frac{x^{n+1}}{n+1} + C$ |
| $\displaystyle \int \frac{1}{x}\,\mathrm{d}x$ | $\ln|x| + C$ |
| $\displaystyle \int e^{ax}\,\mathrm{d}x$ | $\displaystyle \frac{1}{a}e^{ax} + C$ |
| $\displaystyle \int \sin ax\,\mathrm{d}x$ | $\displaystyle -\frac{1}{a}\cos ax + C$ |
| $\displaystyle \int \cos ax\,\mathrm{d}x$ | $\displaystyle \frac{1}{a}\sin ax + C$ |
| $\displaystyle \int \sec^2 ax\,\mathrm{d}x$ | $\displaystyle \frac{1}{a}\tan ax + C$ |

Watch the chain-rule factors: $\int e^{-2y}\,\mathrm{d}y = -\frac{1}{2}e^{-2y}$ and $\int \cos 2\theta\,\mathrm{d}\theta = \frac{1}{2}\sin 2\theta$.

### Example 3 - Integrate Directly (Easy) (source: coursebook 10.1 opening)

> **Question:** Find the general solution of $\frac{\mathrm{d}y}{\mathrm{d}x} = 6(x+1)^2$.

**Solution:**

$$y = \int 6(x+1)^2\,\mathrm{d}x$$

$$\int 6(x+1)^2\,\mathrm{d}x = 6 \cdot \frac{(x+1)^3}{3} + C$$

$$y = 2(x+1)^3 + C \quad\checkmark$$

**What the examiner wants:** recognising this is $\frac{\mathrm{d}y}{\mathrm{d}x} = f(x)$ alone, so one direct integration, with the chain-rule factor $\frac{1}{3}$ from integrating $(x+1)^2$.

### Example 4 - Moving the Whole $2y$ (Medium) (source: coursebook Worked Example 10.1, general solution stage)

> **Question:** Find the general solution of $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{1 + x}{2y}$.

**Solution:**

Move the whole $2y$ across (moving just $y$ would be equally valid):

$$2y\,\frac{\mathrm{d}y}{\mathrm{d}x} = 1 + x$$

$$\int 2y\,\mathrm{d}y = \int (1 + x)\,\mathrm{d}x$$

$$\int 2y\,\mathrm{d}y = y^2$$

$$\int (1 + x)\,\mathrm{d}x = x + \frac{x^2}{2}$$

$$y^2 = x + \frac{x^2}{2} + C \quad\checkmark$$

**What the examiner wants:** the constant appears once, on one side, and it is fine to leave the answer as $y^2 = \dots$ for a general solution.

## 2.3 The Derivative-on-Top Pattern

$$\int \frac{f'(x)}{f(x)}\,\mathrm{d}x = \ln|f(x)| + C$$

For example $\int \frac{x}{x^2 - 3}\,\mathrm{d}x = \frac{1}{2}\ln|x^2 - 3|$ and $\int \frac{kx}{x^2 + 1}\,\mathrm{d}x = \frac{k}{2}\ln(x^2 + 1)$.

### Example 5 - Trig Separation with $\sin 2\theta$ (Medium) (source: CAIE MJ25 P32 Q8)

> **Question:** The variables $x$ and $\theta$ satisfy $\sin 2\theta\,\frac{\mathrm{d}x}{\mathrm{d}\theta} = (4x + 3)\cos 2\theta$, and $x = 0$ when $\theta = \frac{\pi}{12}$. Solve the DE and obtain an expression for $x$ in terms of $\theta$.

**Solution:**

Separate the variables:

$$\frac{1}{4x + 3}\,\frac{\mathrm{d}x}{\mathrm{d}\theta} = \frac{\cos 2\theta}{\sin 2\theta}$$

$$\int \frac{1}{4x + 3}\,\mathrm{d}x = \int \frac{\cos 2\theta}{\sin 2\theta}\,\mathrm{d}\theta$$

Left side - derivative on top with a factor 4:

$$\int \frac{1}{4x + 3}\,\mathrm{d}x = \frac{1}{4}\ln|4x + 3|$$

Right side - derivative of $\sin 2\theta$ is $2\cos 2\theta$, so:

$$\int \frac{\cos 2\theta}{\sin 2\theta}\,\mathrm{d}\theta = \frac{1}{2}\ln|\sin 2\theta|$$

$$\frac{1}{4}\ln|4x + 3| = \frac{1}{2}\ln|\sin 2\theta| + C$$

Use $x = 0$, $\theta = \frac{\pi}{12}$:

$$\frac{1}{4}\ln 3 = \frac{1}{2}\ln\left(\sin\frac{\pi}{6}\right) + C = \frac{1}{2}\ln\frac{1}{2} + C$$

$$C = \frac{1}{4}\ln 3 + \frac{1}{2}\ln 2$$

$$\frac{1}{4}\ln|4x + 3| = \frac{1}{2}\ln|\sin 2\theta| + \frac{1}{4}\ln 3 + \frac{1}{2}\ln 2$$

Multiply by 4:

$$\ln|4x + 3| = 2\ln|\sin 2\theta| + \ln 3 + 2\ln 2$$

$$\ln|4x + 3| = \ln(3 \cdot 4 \cdot \sin^2 2\theta) = \ln(12\sin^2 2\theta)$$

Since $4x + 3 = 3 > 0$ at $\theta = \frac{\pi}{12}$ and stays positive, drop the modulus:

$$4x + 3 = 12\sin^2 2\theta$$

$$x = 3\sin^2 2\theta - \frac{3}{4} \quad\checkmark$$

Check: at $\theta = \frac{\pi}{12}$, $\sin\frac{\pi}{6} = \frac{1}{2}$, so $x = 3 \cdot \frac{1}{4} - \frac{3}{4} = 0$ - matches the initial condition.

**What the examiner wants:** the correct $\frac{1}{4}$ and $\frac{1}{2}$ chain-rule factors, log laws to combine into one logarithm, and justification before dropping the modulus. The November 2023 report (Paper 33 Q7) flagged "slips in removing logarithms" as the top error on this type.

### Example 6 - Polynomial Division Feeding the Integral (Hard) (source: CAIE MJ25 P31 Q10)

> **Question:** (a) Find the quotient and remainder when $x^3 + 5x^2 - 2x - 15$ is divided by $x^2 - 3$.
> (b) The variables $x$ and $y$ satisfy $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{x^3 + 5x^2 - 2x - 15}{6y(x^2 - 3)}$, with $y = 2$ when $x = 2$. Solve the DE to obtain an expression for $y^2$ in terms of $x$.

**Solution:**

(a) Divide:

$$(x^2 - 3)(x + 5) = x^3 + 5x^2 - 3x - 15$$

$$x^3 + 5x^2 - 2x - 15 - (x^3 + 5x^2 - 3x - 15) = x$$

$$\text{quotient} = x + 5, \quad \text{remainder} = x$$

(b) Separate the variables:

$$6y\,\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{x^3 + 5x^2 - 2x - 15}{x^2 - 3}$$

$$\int 6y\,\mathrm{d}y = \int \frac{x^3 + 5x^2 - 2x - 15}{x^2 - 3}\,\mathrm{d}x$$

Use part (a):

$$\frac{x^3 + 5x^2 - 2x - 15}{x^2 - 3} = x + 5 + \frac{x}{x^2 - 3}$$

$$3y^2 = \int \left(x + 5 + \frac{x}{x^2 - 3}\right)\mathrm{d}x$$

$$\int x\,\mathrm{d}x = \frac{x^2}{2}, \quad \int 5\,\mathrm{d}x = 5x$$

$$\int \frac{x}{x^2 - 3}\,\mathrm{d}x = \frac{1}{2}\ln|x^2 - 3|$$

$$3y^2 = \frac{x^2}{2} + 5x + \frac{1}{2}\ln|x^2 - 3| + C$$

Use $y = 2$, $x = 2$:

$$3(4) = 12 = \frac{4}{2} + 10 + \frac{1}{2}\ln|4 - 3| + C = 2 + 10 + 0 + C$$

$$C = 0$$

$$3y^2 = \frac{x^2}{2} + 5x + \frac{1}{2}\ln|x^2 - 3|$$

$$y^2 = \frac{x^2}{6} + \frac{5x}{3} + \frac{1}{6}\ln|x^2 - 3| \quad\checkmark$$

**What the examiner wants:** spotting that part (a) exists to make the integral direct, and keeping the modulus inside the log.

## 2.4 The Arctan Form

$$\int \frac{1}{a^2 + x^2}\,\mathrm{d}x = \frac{1}{a}\arctan\frac{x}{a} + C$$

> **Watch Out!** The June 2023 report (Paper 32 Q8) flagged the coefficient error: $\int \frac{1}{4 + 9y^2}\,\mathrm{d}y = \frac{1}{6}\arctan\frac{3y}{2} + C$, with candidates very often writing $\frac{1}{2}$ in place of $\frac{1}{6}$. Check: $\frac{\mathrm{d}}{\mathrm{d}y}\left[\frac{1}{6}\arctan\frac{3y}{2}\right] = \frac{1}{6} \cdot \frac{3/2}{1 + 9y^2/4} = \frac{1}{4} \cdot \frac{4}{4 + 9y^2} = \frac{1}{4 + 9y^2}$. Some candidates also wrote $\ln(4 + 9y^2)$ where no logarithm belongs - logarithms only come from $\int \frac{1}{u}\,\mathrm{d}u$ patterns.

### Example 7 - The Curve Through $(0, 1)$ (Medium) (source: coursebook Exercise 10A Q9)

> **Question:** Find the equation of the curve that satisfies $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{1 + y^2}{4 + x^2}$ and passes through the point $(0, 1)$. Give your answer in the form $y = f(x)$.

**Solution:**

Separate:

$$\frac{1}{1 + y^2}\,\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{1}{4 + x^2}$$

$$\int \frac{1}{1 + y^2}\,\mathrm{d}y = \int \frac{1}{4 + x^2}\,\mathrm{d}x$$

$$\arctan y = \frac{1}{2}\arctan\frac{x}{2} + C$$

Use $(0, 1)$:

$$\arctan 1 = \frac{\pi}{4} = \frac{1}{2}\arctan 0 + C = C$$

$$C = \frac{\pi}{4}$$

$$\arctan y = \frac{1}{2}\arctan\frac{x}{2} + \frac{\pi}{4}$$

$$y = \tan\left(\frac{\pi}{4} + \frac{1}{2}\arctan\frac{x}{2}\right) \quad\checkmark$$

**What the examiner wants:** both sides in arctan form with the correct $\frac{1}{2}$ factor on the $x$-side, and $\arctan 1 = \frac{\pi}{4}$ used to fix $C$.

## 2.5 Partial Fractions on Either Side

For fractions like $\frac{600}{x(300 - x)}$ and $\frac{1495}{x(300 - x)}$, decompose first:

$$\frac{1}{x(300 - x)} = \frac{1}{300}\left(\frac{1}{x} + \frac{1}{300 - x}\right), \qquad \frac{1}{y^2 + y} = \frac{1}{y} - \frac{1}{y + 1}$$

> **Watch Out!** Two examiner-report traps. June 2023 (Paper 34 Q11): many candidates claimed $\int \frac{1}{5x + x^3}\,\mathrm{d}x = \int\left(\frac{1}{5x} + \frac{1}{x^3}\right)\mathrm{d}x$ - a fraction only splits into partial fractions of the correct form. November 2023 (Paper 32 Q11): the same mistake as $\frac{1}{y^2 + y} = \frac{1}{y^2} + \frac{1}{y}$ instead of $\frac{1}{y} - \frac{1}{y + 1}$. Also remember $\int \frac{A}{b - x}\,\mathrm{d}x = -A\ln|b - x| + C$ - the chain-rule minus sign is easy to lose.

### Example 8 - Logistic-Type with Partial Fractions (Medium-Hard) (source: coursebook Worked Example 10.3)

> **Question:** It is given that, for $0 < x < 300$, $\frac{\mathrm{d}x}{\mathrm{d}t} = \frac{x(300 - x)}{600}$, and $x = 50$ when $t = 0$. Find the particular solution, giving your answer as an expression for $x$ in terms of $t$.

**Solution:**

Separate (leave the 600 on the right - simpler):

$$\frac{600}{x(300 - x)}\,\frac{\mathrm{d}x}{\mathrm{d}t} = 1$$

$$\int \frac{600}{x(300 - x)}\,\mathrm{d}x = \int \mathrm{d}t$$

Partial fractions: $\frac{600}{x(300 - x)} = \frac{A}{x} + \frac{B}{300 - x}$:

$$600 = A(300 - x) + Bx$$

$x = 0$: $600 = 300A \;\Rightarrow\; A = 2$

$x = 300$: $600 = 300B \;\Rightarrow\; B = 2$

$$\int \left(\frac{2}{x} + \frac{2}{300 - x}\right)\mathrm{d}x = \int \mathrm{d}t$$

$$2\ln x - 2\ln(300 - x) = t + C$$

No moduli, since $0 < x < 300$ makes both arguments positive:

$$2\ln\left(\frac{x}{300 - x}\right) = t + C$$

Use $x = 50$, $t = 0$:

$$2\ln\left(\frac{50}{250}\right) = C$$

$$C = 2\ln 0.2$$

$$2\ln\left(\frac{x}{300 - x}\right) = t + 2\ln 0.2$$

$$\ln\left(\frac{x}{300 - x}\right) = \frac{t}{2} + \ln 0.2$$

$$\frac{x}{300 - x} = e^{t/2} \cdot e^{\ln 0.2} = 0.2e^{t/2}$$

$$x = 0.2e^{t/2}(300 - x)$$

$$x + 0.2xe^{t/2} = 60e^{t/2}$$

$$x(1 + 0.2e^{t/2}) = 60e^{t/2}$$

$$x = \frac{60e^{t/2}}{1 + 0.2e^{t/2}} \quad\checkmark$$

Check: at $t = 0$, $x = \frac{60}{1.2} = 50$ - matches.

**What the examiner wants:** clean partial fractions, log laws to combine the two logs, the algebra that isolates $x$, and the modulus reasoning (dropped because $0 < x < 300$).

## 2.6 Integration by Parts and Trig Identities

Integration by parts:

$$\int u\,\frac{\mathrm{d}v}{\mathrm{d}x}\,\mathrm{d}x = uv - \int v\,\frac{\mathrm{d}u}{\mathrm{d}x}\,\mathrm{d}x$$

Useful identity:

$$\sin 4y = 2\sin 2y\cos 2y \quad\Rightarrow\quad \frac{\sin 4y}{\sin 2y} = 2\cos 2y$$

> **Watch Out!** June 2023 (Paper 31 Q7): candidates who recognised $\int \sec 2x\tan 2x\,\mathrm{d}x = \frac{1}{2}\sec 2x$ did best; the integration-by-parts route rarely completed. After applying a double-angle identity, "errors in the coefficients" were the most common fault - write the identity out first, then re-check every factor.

### Example 9 - Identity Plus Parts (Hard) (source: CAIE MJ25 P33 Q10)

> **Question:** The variables $x$ and $y$ satisfy $\sin 4y\,\frac{\mathrm{d}y}{\mathrm{d}x} = x\sin 2y\,\sin 3x$, with $y = \frac{\pi}{12}$ when $x = \frac{\pi}{2}$.
> (a) Solve the DE, obtaining a relation between $x$ and $y$.
> (b) Given $0 < y < \frac{\pi}{2}$, find the values of $y$ when $x = 0$.

**Solution:**

(a) Separate:

$$\int \frac{\sin 4y}{\sin 2y}\,\mathrm{d}y = \int x\sin 3x\,\mathrm{d}x$$

Simplify the left integrand with $\sin 4y = 2\sin 2y\cos 2y$:

$$\frac{\sin 4y}{\sin 2y} = 2\cos 2y$$

$$\int 2\cos 2y\,\mathrm{d}y = \sin 2y$$

Right side by parts: $u = x$, $\frac{\mathrm{d}v}{\mathrm{d}x} = \sin 3x$, so $\frac{\mathrm{d}u}{\mathrm{d}x} = 1$, $v = -\frac{1}{3}\cos 3x$:

$$\int x\sin 3x\,\mathrm{d}x = x\left(-\frac{1}{3}\cos 3x\right) - \int \left(-\frac{1}{3}\cos 3x\right)\mathrm{d}x$$

$$= -\frac{x\cos 3x}{3} + \frac{1}{3}\int \cos 3x\,\mathrm{d}x$$

$$= -\frac{x\cos 3x}{3} + \frac{1}{3}\cdot\frac{\sin 3x}{3}$$

$$= -\frac{x\cos 3x}{3} + \frac{\sin 3x}{9}$$

$$\sin 2y = -\frac{x\cos 3x}{3} + \frac{\sin 3x}{9} + C$$

Use $y = \frac{\pi}{12}$, $x = \frac{\pi}{2}$:

$$\sin\frac{\pi}{6} = \frac{1}{2} = -\frac{\pi/2}{3}\cos\frac{3\pi}{2} + \frac{1}{9}\sin\frac{3\pi}{2} + C$$

$$\frac{1}{2} = 0 - \frac{1}{9} + C$$

$$C = \frac{1}{2} + \frac{1}{9} = \frac{11}{18}$$

$$\sin 2y = \frac{\sin 3x}{9} - \frac{x\cos 3x}{3} + \frac{11}{18} \quad\checkmark$$

(b) At $x = 0$:

$$\sin 2y = 0 - 0 + \frac{11}{18} = \frac{11}{18}$$

With $0 < y < \frac{\pi}{2}$ we have $0 < 2y < \pi$, which gives two angles:

$$2y = \arcsin\frac{11}{18} \quad \text{or} \quad 2y = \pi - \arcsin\frac{11}{18}$$

$$\arcsin\frac{11}{18} = 0.6607$$

$$y = 0.330 \quad \text{or} \quad y = \frac{\pi - 0.6607}{2} = 1.240$$

$$y = 0.330 \text{ or } 1.24 \quad (3\text{ s.f.}) \quad\checkmark$$

**What the examiner wants:** the identity to reduce $\frac{\sin 4y}{\sin 2y}$, correct integration by parts with the $-\frac{1}{3}$ coefficient, and the second solution branch in (b) - the range $0 < 2y < \pi$ gives two angles.

---

### Practice Questions - Part 2

1. **Q1 (Medium)** (a) Using partial fractions, find $\int \frac{1}{P(P+5)}\,\mathrm{d}P$. (b) Given that $P = 3$ when $t = 0$, solve $\frac{\mathrm{d}P}{\mathrm{d}t} = -P(P+5)$, obtaining an expression for $P$ in terms of $t$. (c) Describe what happens to $P$ when $t \to \infty$. (source: coursebook End-of-Chapter Review Exercise 10 Q11; answer computed estimate)

**Solution:**

(a) Partial fractions: $\frac{1}{P(P+5)} = \frac{A}{P} + \frac{B}{P+5}$:

$$1 = A(P + 5) + BP$$

$P = 0$: $1 = 5A \;\Rightarrow\; A = \frac{1}{5}$

$P = -5$: $1 = -5B \;\Rightarrow\; B = -\frac{1}{5}$

$$\int \frac{1}{P(P+5)}\,\mathrm{d}P = \frac{1}{5}\int\left(\frac{1}{P} - \frac{1}{P+5}\right)\mathrm{d}P = \frac{1}{5}\ln\left|\frac{P}{P+5}\right| + C$$

(b) Separate:

$$\int \frac{1}{P(P+5)}\,\mathrm{d}P = \int -\,\mathrm{d}t$$

$$\frac{1}{5}\left(\ln P - \ln(P + 5)\right) = -t + C$$

Use $P = 3$, $t = 0$:

$$\frac{1}{5}\ln\frac{3}{8} = C$$

$$\ln\left(\frac{P}{P+5}\right) = -5t + \ln\frac{3}{8}$$

$$\frac{P}{P+5} = \frac{3}{8}e^{-5t}$$

$$8P = 3e^{-5t}(P + 5)$$

$$P(8 - 3e^{-5t}) = 15e^{-5t}$$

$$P = \frac{15e^{-5t}}{8 - 3e^{-5t}} \quad\checkmark$$

(c) As $t \to \infty$, $e^{-5t} \to 0$, so:

$$P \to \frac{0}{8} = 0 \quad\checkmark$$

2. **Q2 (Medium)** Solve the differential equation $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\tan x}{3y^2}$, given that $x = 0$ when $y = 0$. Give your answer in the form $y = f(x)$. (source: coursebook End-of-Chapter Review Exercise 10 Q14; answer computed estimate)

**Solution:**

$$\int 3y^2\,\mathrm{d}y = \int \tan x\,\mathrm{d}x$$

$$y^3 = -\ln|\cos x| + C$$

Use $y = 0$, $x = 0$:

$$0 = -\ln 1 + C = C$$

$$y^3 = -\ln(\cos x)$$

$$y = \left(-\ln(\cos x)\right)^{1/3} \quad\checkmark$$

3. **Q3 (Easy-Medium)** Given that $x, y > 0$, find the general solution of the differential equation $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{y}{x\ln x}$. (source: coursebook Exercise 10A Q15; answer computed estimate)

**Solution:**

$$\int \frac{1}{y}\,\mathrm{d}y = \int \frac{1}{x\ln x}\,\mathrm{d}x$$

Right side with substitution $u = \ln x$, $\frac{\mathrm{d}u}{\mathrm{d}x} = \frac{1}{x}$:

$$\int \frac{1}{x\ln x}\,\mathrm{d}x = \int \frac{1}{u}\,\mathrm{d}u = \ln|u| = \ln|\ln x|$$

$$\ln y = \ln(\ln x) + C$$

$$y = A\ln x, \quad A = e^C \quad\checkmark$$

4. **Q4 (Hard)** The variables $x$ and $\theta$ satisfy the differential equation $\frac{\mathrm{d}x}{\mathrm{d}\theta} = (x^2 + 2)\sin 2\theta$, and it is given that $x = 0$ when $\theta = 0$. Solve the differential equation and calculate the value of $x$ when $\theta = \frac{\pi}{4}$, giving your answer correct to 3 significant figures. (source: CAIE Nov 2015 P31 Q8, via coursebook End-of-Chapter Review Exercise 10 Q17; answer computed estimate)

**Solution:**

$$\int \frac{1}{x^2 + 2}\,\mathrm{d}x = \int \sin 2\theta\,\mathrm{d}\theta$$

$$\frac{1}{\sqrt{2}}\arctan\frac{x}{\sqrt{2}} = -\frac{1}{2}\cos 2\theta + C$$

Use $x = 0$, $\theta = 0$:

$$0 = -\frac{1}{2}\cos 0 + C = -\frac{1}{2} + C$$

$$C = \frac{1}{2}$$

$$\frac{1}{\sqrt{2}}\arctan\frac{x}{\sqrt{2}} = \frac{1}{2}(1 - \cos 2\theta)$$

At $\theta = \frac{\pi}{4}$: $\cos\frac{\pi}{2} = 0$:

$$\frac{1}{\sqrt{2}}\arctan\frac{x}{\sqrt{2}} = \frac{1}{2}$$

$$\arctan\frac{x}{\sqrt{2}} = \frac{\sqrt{2}}{2} = 0.7071$$

$$\frac{x}{\sqrt{2}} = \tan(0.7071) = 0.8541$$

$$x = \sqrt{2} \times 0.8541 = 1.2079$$

$$x = 1.21 \quad (3\text{ s.f.}) \quad\checkmark$$

---

# PART 3: Initial Conditions - General vs Particular Solutions

Solving a first order DE introduces exactly one arbitrary constant $C$. The result is the general solution - a whole family of curves. An initial condition ("$y = 2$ when $x = 0$", "passes through $(3, 4)$", "initially the particle is 2 m from $O$") fixes $C$ and gives the particular solution.

## 3.1 General vs Particular

| | General solution | Particular solution |
|---|---|---|
| Contains | one arbitrary constant $C$ | no arbitrary constant |
| Represents | a family of curves | one specific curve |
| Obtained by | integrating the DE | substituting an initial condition to find $C$ |

### Example 1 - Fixing $C$ (Easy)

> **Question:** Solve $\frac{\mathrm{d}y}{\mathrm{d}x} = 2x + 1$, given that $y = 3$ when $x = 1$.

**Solution:**

$$y = \int (2x + 1)\,\mathrm{d}x$$

$$y = x^2 + x + C$$

This is the general solution - one curve for each value of $C$. Now use $y = 3$ when $x = 1$:

$$3 = 1^2 + 1 + C$$

$$3 = 2 + C$$

$$C = 1$$

$$y = x^2 + x + 1 \quad\checkmark$$

**What the examiner wants:** the constant substituted into the integrated form only, and the particular solution stated in full.

### Example 2 - The Full Flow with Log Cleanup (Medium) (source: coursebook 10.1)

> **Question:** Solve $\frac{\mathrm{d}y}{\mathrm{d}x} = xy$ given that $y = 2$ when $x = 0$.

**Solution:**

$$\frac{1}{y}\,\frac{\mathrm{d}y}{\mathrm{d}x} = x$$

$$\int \frac{1}{y}\,\mathrm{d}y = \int x\,\mathrm{d}x$$

$$\ln y = \frac{x^2}{2} + C$$

Use $y = 2$, $x = 0$:

$$\ln 2 = 0 + C$$

$$C = \ln 2$$

$$\ln y = \frac{x^2}{2} + \ln 2$$

$$y = e^{x^2/2 + \ln 2}$$

$$y = e^{x^2/2} \cdot e^{\ln 2}$$

$$y = 2e^{x^2/2} \quad\checkmark$$

Check: $\frac{\mathrm{d}y}{\mathrm{d}x} = 2e^{x^2/2} \cdot x = xy$ - matches the original equation, and $x = 0$ gives $y = 2$.

**What the examiner wants:** the index-law cleanup $e^{a + b} = e^a e^b$ and $e^{\ln 2} = 2$ to write the answer as $y = f(x)$ - the June 2023 report (Paper 33 Q8) says the final mark requires this simplification, and a solution left as $e^{\ln(\dots)}$ is not simplified enough.

## 3.2 The Initial Condition Belongs in the Integrated Form Only

> **Watch Out!** A common error, seen regularly in examiner reports, is substituting the initial condition into the differential equation itself, or into the working before integrating. The condition's job is to pin down the constant of integration, which only exists after you integrate.

### Example 3 - Use the Condition Even When Not Asked (Medium) (source: coursebook Worked Example 10.1)

> **Question:** The variables $x$ and $y$ satisfy $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{1 + x}{2y}$. It is given that $y = 3$ when $x = 0$. Solve the differential equation and obtain an expression for $y$ in terms of $x$.

**Solution:**

$$2y\,\frac{\mathrm{d}y}{\mathrm{d}x} = 1 + x$$

$$\int 2y\,\mathrm{d}y = \int (1 + x)\,\mathrm{d}x$$

$$y^2 = x + \frac{x^2}{2} + C$$

Use $y = 3$, $x = 0$:

$$9 = 0 + 0 + C$$

$$C = 9$$

$$y^2 = x + \frac{x^2}{2} + 9$$

Take the positive square root (since $y = 3 > 0$ initially and the right-hand side stays positive):

$$y = \sqrt{\frac{x^2}{2} + x + 9} \quad\checkmark$$

**What the examiner wants:** even though the question does not say "use the initial condition", you must use it; the final answer must be $y$ in terms of $x$. Leaving $C$ as a letter loses the final marks.

## 3.3 Finding $k$ (Not Just $C$) from Two Conditions

When the DE contains an unknown constant $k$, you need two pieces of information: the first fixes $C$, the second fixes $k$. Read the question carefully to see which pair goes where - a classic error is using the second condition to find $C$ again.

### Example 4 - Particle Motion, Two Pairs of Values (Medium) (source: coursebook Worked Example 10.4)

> **Question:** The velocity of a particle at time $t$ seconds is inversely proportional to its displacement, $s$ metres, from an origin $O$.
> (a) Form a differential equation to represent this data.
> (b) Initially the particle is 2 m from $O$; after 1 second it is 5 m from $O$. Solve the differential equation, giving your answer in the form $t = f(s)$.
> (c) Find $t$ when the displacement is 10 m.

**Solution:**

(a) Already found in Example 5 of Part 1:

$$\frac{\mathrm{d}s}{\mathrm{d}t} = \frac{k}{s}, \quad k > 0$$

(b) Separate:

$$\int s\,\mathrm{d}s = \int k\,\mathrm{d}t$$

$$\frac{s^2}{2} = kt + C$$

Use $s = 2$, $t = 0$:

$$\frac{2^2}{2} = 2 = C$$

$$\frac{s^2}{2} = kt + 2$$

Use $s = 5$, $t = 1$ - this finds $k$, not $C$ again:

$$\frac{25}{2} = k + 2$$

$$k = \frac{25}{2} - 2 = \frac{21}{2}$$

$$\frac{s^2}{2} = \frac{21}{2}t + 2$$

$$s^2 = 21t + 4$$

$$t = \frac{s^2 - 4}{21} \quad\checkmark$$

(c) $s = 10$:

$$t = \frac{100 - 4}{21} = \frac{96}{21} = 4.5714\ldots$$

$$t = 4.57 \text{ seconds} \quad (3\text{ s.f.}) \quad\checkmark$$

**What the examiner wants:** the second pair of values used to find $k$; the answer rearranged to $t = f(s)$ as requested.

### Example 5 - Exact Value of $k$ and of $y$ (Hard) (source: CAIE ON25 P31 Q8)

> **Question:** The variables $x$ and $y$ satisfy $(x^2 + 1)\frac{\mathrm{d}y}{\mathrm{d}x} = kxe^{2y}$, where $k$ is a constant. It is given that $y = 0$ when $x = 0$ and $y = -\frac{1}{2}$ when $x = 1$. Solve the DE and find the exact value of $y$ when $x = 3$.

**Solution:**

Separate:

$$\int e^{-2y}\,\mathrm{d}y = \int \frac{kx}{x^2 + 1}\,\mathrm{d}x$$

$$-\frac{1}{2}e^{-2y} = \frac{k}{2}\ln(x^2 + 1) + C$$

Use $y = 0$, $x = 0$:

$$-\frac{1}{2} = \frac{k}{2}\ln 1 + C = C$$

$$C = -\frac{1}{2}$$

Use $y = -\frac{1}{2}$, $x = 1$:

$$-\frac{1}{2}e^{-2(-1/2)} = \frac{k}{2}\ln 2 - \frac{1}{2}$$

$$-\frac{1}{2}e = \frac{k}{2}\ln 2 - \frac{1}{2}$$

$$\frac{k\ln 2}{2} = \frac{1 - e}{2}$$

$$k = \frac{1 - e}{\ln 2}$$

At $x = 3$:

$$-\frac{1}{2}e^{-2y} = \frac{1 - e}{2\ln 2}\ln 10 - \frac{1}{2}$$

Multiply by $-2$:

$$e^{-2y} = \frac{(e - 1)\ln 10}{\ln 2} + 1$$

$$-2y = \ln\left(1 + \frac{(e - 1)\ln 10}{\ln 2}\right)$$

$$y = -\frac{1}{2}\ln\left(1 + \frac{(e - 1)\ln 10}{\ln 2}\right) \quad\checkmark$$

Evaluate (computed estimate):

$$\frac{(e - 1)\ln 10}{\ln 2} = \frac{1.7183 \times 2.3026}{0.6931} = 5.708$$

$$y = -\frac{1}{2}\ln(6.708) = -0.9515$$

$$y = -0.952 \quad (3\text{ s.f.}) \quad\checkmark$$

**What the examiner wants:** integrating $e^{-2y}$ (factor $-\frac{1}{2}$) and $\frac{kx}{x^2 + 1}$ (factor $\frac{k}{2}$) correctly; the first condition for $C$, the second for $k$; the final value left exact as requested - decimal approximations were not accepted in the June 2023 and November 2023 exact-answer questions.

## 3.4 Modulus Signs and Log/Index Cleanup

- The integral of $\frac{1}{x}$ is $\ln|x| + C$. Drop the modulus only when the argument is known positive (e.g. $0 < x < 300$, $V > 0$, $T - s > 0$).
- Keeping the modulus never hurts: $|y| = e^{\dots}$ means $y = \pm e^{\dots}$, and the $\pm$ merges into the constant: $y = Ae^{\dots}$.
- Index/log laws: $e^{\ln a} = a$, $e^{a + b} = e^a e^b$, $e^{a\ln b} = b^a$, $e^{-\ln a} = \frac{1}{a}$.

> **Watch Out!** November 2023 (Paper 33 Q7): "several slips in removing logarithms to obtain an expression for $x^2$ in terms of $\theta$". November 2023 (Paper 32 Q11): many candidates stopped at an expression for $\frac{y}{y+1}$ instead of going on to solve for $y$ itself - always finish the job by making the requested variable the subject.

### Example 6 - $\frac{\mathrm{d}y}{\mathrm{d}x} = e^{x - y}$ (Medium) (source: coursebook Exercise 10A Q3)

> **Question:** Given that $\frac{\mathrm{d}y}{\mathrm{d}x} = e^{x - y}$ and $y = \ln 2$ when $x = 0$, obtain an expression for $y$ in terms of $x$.

**Solution:**

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{e^x}{e^y}$$

$$e^y\,\frac{\mathrm{d}y}{\mathrm{d}x} = e^x$$

$$\int e^y\,\mathrm{d}y = \int e^x\,\mathrm{d}x$$

$$e^y = e^x + C$$

Use $y = \ln 2$, $x = 0$:

$$e^{\ln 2} = 2 = e^0 + C = 1 + C$$

$$C = 1$$

$$e^y = e^x + 1$$

$$y = \ln(e^x + 1) \quad\checkmark$$

**What the examiner wants:** splitting $e^{x - y}$ into $\frac{e^x}{e^y}$ (the exponent is a single quantity - never split $e^{2x + 1}$ into $e^{2x} + 1$, a June 2023 Paper 32 Q8 error), then $e^{\ln 2} = 2$ to fix $C$.

### Example 7 - Modulus and the $\pm$ Resolved by the Condition (Hard) (source: CAIE Nov 2012 P31 Q6, via coursebook End-of-Chapter Review Exercise 10 Q16)

> **Question:** The variables $x$ and $y$ are related by the differential equation $x^2\frac{\mathrm{d}y}{\mathrm{d}x} = y^2 - 1$. When $x = 2$, $y = 0$. Solve the differential equation, obtaining an expression for $y$ in terms of $x$.

**Solution:**

$$\int \frac{1}{y^2 - 1}\,\mathrm{d}y = \int \frac{1}{x^2}\,\mathrm{d}x$$

Partial fractions: $\frac{1}{y^2 - 1} = \frac{A}{y - 1} + \frac{B}{y + 1}$:

$$1 = A(y + 1) + B(y - 1)$$

$y = 1$: $1 = 2A \;\Rightarrow\; A = \frac{1}{2}$

$y = -1$: $1 = -2B \;\Rightarrow\; B = -\frac{1}{2}$

$$\frac{1}{2}\int\left(\frac{1}{y - 1} - \frac{1}{y + 1}\right)\mathrm{d}y = -\frac{1}{x} + C$$

$$\frac{1}{2}\ln\left|\frac{y - 1}{y + 1}\right| = -\frac{1}{x} + C$$

Use $y = 0$, $x = 2$:

$$\frac{1}{2}\ln\left|\frac{-1}{1}\right| = 0 = -\frac{1}{2} + C$$

$$C = \frac{1}{2}$$

$$\frac{1}{2}\ln\left|\frac{y - 1}{y + 1}\right| = \frac{1}{2} - \frac{1}{x}$$

$$\ln\left|\frac{y - 1}{y + 1}\right| = 1 - \frac{2}{x}$$

$$\left|\frac{y - 1}{y + 1}\right| = e^{1 - 2/x}$$

At $x = 2$: $e^{1 - 2/x} = e^0 = 1$, but $\frac{y - 1}{y + 1} = \frac{-1}{1} = -1$ at $y = 0$, so the negative branch is the one that matches the condition:

$$\frac{y - 1}{y + 1} = -e^{1 - 2/x}$$

$$y - 1 = -e^{1 - 2/x}(y + 1)$$

$$y - 1 = -ye^{1 - 2/x} - e^{1 - 2/x}$$

$$y\left(1 + e^{1 - 2/x}\right) = 1 - e^{1 - 2/x}$$

$$y = \frac{1 - e^{1 - 2/x}}{1 + e^{1 - 2/x}} \quad\checkmark$$

Check: at $x = 2$, $y = \frac{1 - 1}{1 + 1} = 0$ - matches the initial condition.

**What the examiner wants:** partial fractions on the $y$-side, the modulus kept until the initial condition resolves the sign, and the final rearrangement making $y$ the subject.

---

### Practice Questions - Part 3

1. **Q1 (Hard)** The variables $x$ and $y$ satisfy the differential equation $\frac{\mathrm{d}y}{\mathrm{d}x} = e^{x + 3y}$ and $y = 0$ when $x = 0$. Solve the differential equation and obtain an expression for $y$ in terms of $x$. (source: coursebook End-of-Chapter Review Exercise 10 Q9; answer computed estimate)

**Solution:**

$$\int e^{-3y}\,\mathrm{d}y = \int e^x\,\mathrm{d}x$$

$$-\frac{1}{3}e^{-3y} = e^x + C$$

Use $y = 0$, $x = 0$:

$$-\frac{1}{3} = 1 + C$$

$$C = -\frac{4}{3}$$

$$-\frac{1}{3}e^{-3y} = e^x - \frac{4}{3}$$

$$e^{-3y} = 4 - 3e^x$$

$$-3y = \ln(4 - 3e^x)$$

$$y = -\frac{1}{3}\ln(4 - 3e^x) \quad\checkmark$$

2. **Q2 (Medium)** The gradient of a curve at the point $(x, y)$ is $5x^3y^3$. (a) Write down the differential equation satisfied by $y$. (b) Given that the curve passes through the point $(1, 1)$, find $y^2$ as a function of $x$. (source: coursebook Exercise 10A Q4; answer computed estimate)

**Solution:**

(a)

$$\frac{\mathrm{d}y}{\mathrm{d}x} = 5x^3y^3$$

(b)

$$\int \frac{1}{y^3}\,\mathrm{d}y = \int 5x^3\,\mathrm{d}x$$

$$-\frac{1}{2y^2} = \frac{5x^4}{4} + C$$

Use $(1, 1)$:

$$-\frac{1}{2} = \frac{5}{4} + C$$

$$C = -\frac{7}{4}$$

$$-\frac{1}{2y^2} = \frac{5x^4 - 7}{4}$$

$$\frac{1}{2y^2} = \frac{7 - 5x^4}{4}$$

$$y^2 = \frac{2}{7 - 5x^4} \quad\checkmark$$

3. **Q3 (Medium-Hard)** At the start of a reaction there are $x$ grams of chemical $X$ present. At time $t$ seconds after the start, the rate of decrease of $x$ is proportional to $xt$. (a) Using $k$ as the constant of proportionality, where $k > 0$, form a differential equation. (b) Solve it, obtaining a relation between $x$, $t$ and $k$. (c) Initially there are 150 grams of $X$ and after 10 seconds this has decreased to 120 grams. Find the time after the start when the amount of $X$ has decreased to 1 gram. (source: coursebook End-of-Chapter Review Exercise 10 Q10; answers computed estimate)

**Solution:**

(a)

$$\frac{\mathrm{d}x}{\mathrm{d}t} = -kxt, \quad k > 0$$

(b)

$$\int \frac{1}{x}\,\mathrm{d}x = \int -kt\,\mathrm{d}t$$

$$\ln x = -\frac{kt^2}{2} + C$$

$$x = Ae^{-kt^2/2}$$

(c) Use $x = 150$, $t = 0$:

$$150 = A$$

$$x = 150e^{-kt^2/2}$$

Use $x = 120$, $t = 10$:

$$120 = 150e^{-50k}$$

$$e^{-50k} = 0.8$$

$$50k = \ln\frac{1}{0.8} = \ln 1.25$$

$$k = \frac{\ln 1.25}{50}$$

Set $x = 1$:

$$1 = 150e^{-kt^2/2}$$

$$e^{-kt^2/2} = \frac{1}{150}$$

$$\frac{kt^2}{2} = \ln 150$$

$$t^2 = \frac{2\ln 150}{k} = \frac{2\ln 150 \times 50}{\ln 1.25} = \frac{100\ln 150}{\ln 1.25}$$

$$t^2 = \frac{100 \times 5.0106}{0.22314} = 2245.5$$

$$t = 47.4 \text{ seconds} \quad (3\text{ s.f.}) \quad\checkmark$$

---

# PART 4: Modelling Applications - Growth, Decay, Cooling, Tanks, Motion

Every model below is the same separation-of-variables procedure applied to a recognisable DE. Learn the families so you recognise them on sight; each example below re-derives the solution in full.

## 4.1 Proportional Growth and Decay

"The rate of change of $x$ is proportional to $x$":

$$\frac{\mathrm{d}x}{\mathrm{d}t} = kx \quad \text{(growth)} \qquad \frac{\mathrm{d}x}{\mathrm{d}t} = -kx \quad \text{(decay)}, \quad k > 0$$

$$\int \frac{1}{x}\,\mathrm{d}x = \int \pm k\,\mathrm{d}t \;\Rightarrow\; \ln x = \pm kt + C$$

With $x = x_0$ at $t = 0$:

$$x = x_0e^{kt} \quad \text{(growth)} \qquad x = x_0e^{-kt} \quad \text{(decay)}$$

Half-life $=$ doubling time $= \frac{\ln 2}{k}$ for $x = x_0e^{\pm kt}$. Fraction remaining after time $t$: $e^{-kt} = 2^{-t/T}$, where $T$ is the half-life.

### Example 1 - Carbon-14 Fraction (Easy) (source: coursebook Exercise 10B Q9)

> **Question:** The half-life of carbon-14 is 5700 years. The rate of decrease of its mass $m$ is proportional to $m$. A sample has initial mass $m_0$. What fraction of the original amount remains after 2500 years?

**Solution:**

$$\frac{\mathrm{d}m}{\mathrm{d}t} = -km \;\Rightarrow\; m = m_0e^{-kt}$$

Half-life 5700 means $m = \frac{1}{2}m_0$ when $t = 5700$:

$$\frac{1}{2}m_0 = m_0e^{-5700k}$$

$$e^{-5700k} = \frac{1}{2}$$

$$k = \frac{\ln 2}{5700}$$

At $t = 2500$:

$$\frac{m}{m_0} = e^{-2500k} = e^{-\frac{2500\ln 2}{5700}} = 2^{-2500/5700}$$

$$\frac{m}{m_0} = 2^{-0.4386} = e^{-0.3040} = 0.7377$$

$$\frac{m}{m_0} = 0.738 \quad \text{(about } 74\%\text{)} \quad\checkmark$$

**What the examiner wants:** using the half-life to get $k$, or the index-law shortcut $e^{-kt} = 2^{-t/T}$ straight from the half-life without finding $k$ separately.

### Example 2 - Motorbike Value (Medium) (source: coursebook Worked Example 10.6)

> **Question:** The value $V$ of a motorbike $t$ months old decreases at a rate proportional to $V$.
> (a) Write down a differential equation satisfied by $V$.
> (b) The motorbike was worth \$10\,000 when new. Solve the DE, showing $V = 10\,000e^{-kt}$ with $k$ positive.
> (c) After 3 years the motorbike has lost half its value. Find its value when it was 2 years old.

**Solution:**

(a)

$$\frac{\mathrm{d}V}{\mathrm{d}t} = -kV, \quad k > 0$$

(b)

$$\int \frac{1}{V}\,\mathrm{d}V = \int -k\,\mathrm{d}t$$

$$\ln V = -kt + C \quad \text{(no modulus: } V > 0\text{)}$$

Use $V = 10\,000$, $t = 0$:

$$\ln 10\,000 = C$$

$$\ln V = -kt + \ln 10\,000$$

$$V = e^{-kt + \ln 10\,000} = e^{-kt} \cdot e^{\ln 10\,000}$$

$$V = 10\,000e^{-kt} \quad\checkmark$$

(c) After 3 years the value is half: $V = 5000$ at $t = 3$:

$$5000 = 10\,000e^{-3k}$$

$$e^{-3k} = \frac{1}{2}$$

$$k = \frac{\ln 2}{3}$$

At $t = 2$:

$$V = 10\,000e^{-\frac{2\ln 2}{3}} = 10\,000 \times 2^{-2/3}$$

$$2^{-2/3} = e^{-0.4621} = 0.62996$$

$$V = 6299.6$$

$$V = \$6300 \quad (3\text{ s.f.}) \quad\checkmark$$

**What the examiner wants:** the explicit minus sign with $k > 0$; using $e^{\ln 10\,000} = 10\,000$ when exponentiating; consistent units - here $t$ is in years, matching $k = \frac{\ln 2}{3}$ (3 years $= 36$ months if $t$ were in months).

### Example 3 - Medicine: Time to Reach a Safe Level (Medium) (source: coursebook Exercise 10A Q16)

> **Question:** After treatment, 65 mg of a light-sensitive medicine remains in Jonty's skin. The rate at which it disappears is modelled by $\frac{\mathrm{d}m}{\mathrm{d}t} = -0.05m$, where $m$ mg is the amount $t$ hours after treatment. He is safe in bright light once at most 6 mg remains. How long must he wait?

**Solution:**

Proportional decay with $m_0 = 65$:

$$m = 65e^{-0.05t}$$

Set $m = 6$:

$$6 = 65e^{-0.05t}$$

$$e^{-0.05t} = \frac{6}{65}$$

$$-0.05t = \ln\frac{6}{65}$$

$$t = -20\ln\frac{6}{65} = 20\ln\frac{65}{6}$$

$$t = 20\ln(10.8333) = 20 \times 2.3821$$

$$t = 47.64 \text{ hours}$$

$$t = 48 \text{ hours to the nearest hour} \quad\checkmark$$

**What the examiner wants:** recognising the decay solution instantly, the tidy log manipulation $-\ln\frac{6}{65} = \ln\frac{65}{6}$, and rounding sensibly to a whole number of hours.

### Example 4 - Bacteria Doubling Time (Medium) (source: coursebook Exercise 10B Q13)

> **Question:** Bacteria grow at a rate proportional to the number present. Initially there are 5000; after 3.5 hours there are a million. (a) Find the doubling time. (b) What assumption does the model make, and how realistic is it?

**Solution:**

$$N = 5000e^{kt}$$

Use $N = 10^6$ at $t = 3.5$:

$$10^6 = 5000e^{3.5k}$$

$$200 = e^{3.5k}$$

$$k = \frac{\ln 200}{3.5}$$

Doubling: $2 = e^{kT}$, so:

$$T = \frac{\ln 2}{k} = \frac{3.5\ln 2}{\ln 200}$$

$$T = \frac{3.5 \times 0.6931}{5.2983} = 0.4579$$

$$T = 0.458 \text{ hours} \quad\checkmark$$

(b) The model assumes unlimited exponential growth with no resource limits - unrealistic in the long term, as resources run out (see coursebook Explore 10.2: exponential growth is unlimited, logistic growth builds in a ceiling).

**What the examiner wants:** the doubling-time rearrangement, and a sensible comment on the assumption of unlimited growth.

## 4.2 Newton's Law of Cooling/Heating and Approach to a Ceiling

"The rate of change of temperature $T$ is proportional to the difference between $T$ and the constant surrounding temperature $s$":

$$\frac{\mathrm{d}T}{\mathrm{d}t} = -k(T - s), \quad k > 0$$

$$\int \frac{1}{T - s}\,\mathrm{d}T = \int -k\,\mathrm{d}t \;\Rightarrow\; \ln|T - s| = -kt + C$$

With $T = T_0$ at $t = 0$:

$$T = s + (T_0 - s)e^{-kt}$$

The object approaches $s$ asymptotically - it cools towards the room, or warms towards the air temperature, but never quite arrives. The same family with a different name: "rate of increase of $x$ is proportional to $(M - x)$" gives $x = M - (M - x_0)e^{-kt}$, approaching the ceiling $M$.

### Example 5 - Liquid Heating to a Ceiling (Medium) (source: coursebook Exercise 10B Q4)

> **Question:** A liquid is heated so that its temperature is $x$ °C after $t$ seconds. The rate of increase of $x$ is proportional to $(100 - x)$. The initial temperature is 25 °C.
> (a) Form a DE relating $x$, $t$ and a constant $k$.
> (b) Solve it, obtaining $x$ in terms of $t$ and $k$.
> (c) After 180 seconds the temperature is 85 °C. Find the temperature after 195 seconds.
> (d) Write down the maximum temperature the model predicts.

**Solution:**

(a)

$$\frac{\mathrm{d}x}{\mathrm{d}t} = k(100 - x), \quad k > 0$$

(b)

$$\int \frac{1}{100 - x}\,\mathrm{d}x = \int k\,\mathrm{d}t$$

$$-\ln(100 - x) = kt + C$$

Use $x = 25$, $t = 0$:

$$-\ln 75 = C$$

$$-\ln(100 - x) = kt - \ln 75$$

$$\ln(100 - x) = -kt + \ln 75$$

$$100 - x = 75e^{-kt}$$

$$x = 100 - 75e^{-kt} \quad\checkmark$$

(c) Use $x = 85$, $t = 180$:

$$15 = 75e^{-180k}$$

$$e^{-180k} = \frac{1}{5} = 0.2$$

$$k = \frac{\ln 5}{180}$$

At $t = 195$:

$$x = 100 - 75e^{-\frac{195\ln 5}{180}} = 100 - 75(0.2)^{195/180}$$

$$(0.2)^{1.0833} = e^{-1.7436} = 0.1749$$

$$x = 100 - 75(0.1749) = 100 - 13.12$$

$$x = 86.9 \text{ °C} \quad\checkmark$$

(d) As $t \to \infty$, $e^{-kt} \to 0$:

$$x \to 100$$

$$x_{\text{max}} = 100 \text{ °C} \quad\checkmark$$

**What the examiner wants:** the minus sign when integrating $\frac{1}{100 - x}$, reading the ceiling off the solution, and recognising the ceiling is approached but never exceeded at finite time.

### Example 6 - Cherry Tree Growing to 8 m (Medium) (source: coursebook End-of-Chapter Review Exercise 10 Q8)

> **Question:** The height $h$ metres of a cherry tree is recorded every year for $t$ years after it is planted. It is thought that the height is increasing at a rate proportional to $8 - h$. When planted it is 0.5 m tall and after 5 years it is 2 m tall. (a) Form and solve a differential equation, giving $h$ in terms of $t$. (b) According to the model, what will the height be when it is fully grown?

**Solution:**

(a)

$$\frac{\mathrm{d}h}{\mathrm{d}t} = k(8 - h), \quad k > 0$$

$$\int \frac{1}{8 - h}\,\mathrm{d}h = \int k\,\mathrm{d}t$$

$$-\ln(8 - h) = kt + C$$

Use $h = 0.5$, $t = 0$:

$$-\ln 7.5 = C$$

$$\ln(8 - h) = -kt + \ln 7.5$$

$$8 - h = 7.5e^{-kt}$$

$$h = 8 - 7.5e^{-kt}$$

Use $h = 2$, $t = 5$:

$$6 = 7.5e^{-5k}$$

$$e^{-5k} = 0.8$$

$$k = \frac{1}{5}\ln\frac{1}{0.8} = \frac{\ln 1.25}{5} = 0.04463$$

$$h = 8 - 7.5e^{-0.04463t} \quad\checkmark$$

(b) As $t \to \infty$, $e^{-0.04463t} \to 0$:

$$h \to 8$$

$$h = 8 \text{ m when fully grown} \quad\checkmark$$

**What the examiner wants:** the ceiling 8 m read directly from the solution; the second data point used to find $k$, not $C$.

### Example 7 - Curry: When Can Maria Refrigerate? (Hard) (source: coursebook Exercise 10B Q8)

> **Question:** The temperature of the curry is 94 °C when it has finished cooking. At 6 pm Maria places the dish in a sink full of cold water kept at a constant 7 °C. After 10 minutes the temperature of the curry is 54 °C. The rate at which the curry cools down is proportional to the difference between the temperature of the curry and the temperature of the water in the sink. She can refrigerate once the curry is at room temperature, 18 °C. At what time can she put the dish in the refrigerator?

**Solution:**

Define your own variables - let $T$ °C be the temperature of the curry at time $t$ minutes after 6 pm:

$$\frac{\mathrm{d}T}{\mathrm{d}t} = -k(T - 7), \quad k > 0$$

$$\int \frac{1}{T - 7}\,\mathrm{d}T = \int -k\,\mathrm{d}t$$

$$\ln(T - 7) = -kt + C$$

Use $T = 94$, $t = 0$:

$$\ln 87 = C$$

$$\ln(T - 7) = -kt + \ln 87$$

$$T - 7 = 87e^{-kt}$$

$$T = 7 + 87e^{-kt}$$

Use $T = 54$, $t = 10$:

$$47 = 87e^{-10k}$$

$$e^{-10k} = \frac{47}{87}$$

$$k = \frac{1}{10}\ln\frac{87}{47}$$

Set $T = 18$:

$$11 = 87e^{-kt}$$

$$e^{-kt} = \frac{11}{87}$$

$$kt = \ln\frac{87}{11}$$

$$t = \frac{\ln\frac{87}{11}}{k} = \frac{10\ln\frac{87}{11}}{\ln\frac{87}{47}}$$

$$\ln\frac{87}{11} = \ln 7.9091 = 2.0682, \qquad \ln\frac{87}{47} = \ln 1.8511 = 0.6156$$

$$t = \frac{10 \times 2.0682}{0.6156} = 33.6 \text{ minutes}$$

$$t = 33.6 \text{ min after } 6\text{ pm}$$

$$6{:}34 \text{ pm} \quad\checkmark \quad \text{(computed estimate)}$$

**What the examiner wants:** defining the variables yourself, the surrounding temperature is the sink water (7 °C), not the room, and the final time rounded sensibly.

## 4.3 Logistic (Restricted) Growth

"The rate of increase of $x$ is proportional to the product of the amount present and the amount remaining":

$$\frac{\mathrm{d}x}{\mathrm{d}t} = kx(M - x), \quad k > 0$$

Separating with partial fractions $\frac{1}{x(M - x)} = \frac{1}{M}\left(\frac{1}{x} + \frac{1}{M - x}\right)$ gives:

$$x = \frac{M}{1 + Ae^{-kMt}}$$

and $x \to M$ as $t \to \infty$. The population approaches its carrying capacity asymptotically.

### Example 8 - Birds (Medium) (source: coursebook End-of-Chapter Review Exercise 10 Q2)

> **Question:** The number of birds $x$ in a particular area of land is recorded every year for $t$ years, with $x$ modelled as a continuous variable. The rate of change of the number of birds over time is modelled by $\frac{\mathrm{d}x}{\mathrm{d}t} = \frac{x(2500 - x)}{5000}$. It is given that $x = 500$ when $t = 0$. (a) Find an expression for $x$ in terms of $t$. (b) How many birds does the model suggest there will be in the long term?

**Solution:**

(a) Separate:

$$\int \frac{5000}{x(2500 - x)}\,\mathrm{d}x = \int \mathrm{d}t$$

Partial fractions: $\frac{5000}{x(2500 - x)} = \frac{A}{x} + \frac{B}{2500 - x}$:

$$5000 = A(2500 - x) + Bx$$

$x = 0$: $5000 = 2500A \;\Rightarrow\; A = 2$

$x = 2500$: $5000 = 2500B \;\Rightarrow\; B = 2$

$$\int \left(\frac{2}{x} + \frac{2}{2500 - x}\right)\mathrm{d}x = \int \mathrm{d}t$$

$$2\ln x - 2\ln(2500 - x) = t + C$$

Use $x = 500$, $t = 0$:

$$2\ln\frac{500}{2000} = 2\ln\frac{1}{4} = C$$

$$2\ln\left(\frac{x}{2500 - x}\right) = t + 2\ln\frac{1}{4}$$

$$\ln\left(\frac{x}{2500 - x}\right) = \frac{t}{2} + \ln\frac{1}{4}$$

$$\frac{x}{2500 - x} = \frac{1}{4}e^{t/2}$$

$$x = \frac{1}{4}e^{t/2}(2500 - x)$$

$$x\left(1 + \frac{e^{t/2}}{4}\right) = 625e^{t/2}$$

$$x = \frac{625e^{t/2}}{1 + \frac{e^{t/2}}{4}} = \frac{2500e^{t/2}}{4 + e^{t/2}} \quad\checkmark$$

(b) Divide top and bottom by $e^{t/2}$ and let $t \to \infty$:

$$x = \frac{2500}{4e^{-t/2} + 1} \to \frac{2500}{1} = 2500$$

$$2500 \text{ birds in the long term} \quad\checkmark$$

**What the examiner wants:** clean partial fractions, log laws, and a justified limiting value - the June 2023 report (Paper 32 Q8) says a bare guess like "tends to 2500" is not enough; show the exponential term vanishing.

### Example 9 - Plants and Disease (Hard) (source: CAIE MJ24 P31 Q11)

> **Question:** In a field there are 300 plants, all of which can be infected by a disease. At time $t$ there are $x$ infected plants. The rate of change of $x$ is proportional to the product of the number infected and the number not yet infected. Given $\frac{\mathrm{d}x}{\mathrm{d}t} = 0.2$ when $x = 1$:
> (a) Show that $x$ and $t$ satisfy $\frac{\mathrm{d}x}{\mathrm{d}t} = \frac{x(300 - x)}{1495}$.
> (b) Using partial fractions, solve the DE and obtain an expression for $t$ in terms of a single logarithm involving $x$.

**Solution:**

(a) Done in Part 1, Example 4:

$$\frac{\mathrm{d}x}{\mathrm{d}t} = \frac{x(300 - x)}{1495}$$

(b) Separate:

$$\int \frac{1495}{x(300 - x)}\,\mathrm{d}x = \int \mathrm{d}t$$

Partial fractions: $\frac{1495}{x(300 - x)} = \frac{A}{x} + \frac{B}{300 - x}$:

$$1495 = A(300 - x) + Bx$$

$x = 0$: $1495 = 300A \;\Rightarrow\; A = \frac{1495}{300} = \frac{299}{60}$

$x = 300$: $1495 = 300B \;\Rightarrow\; B = \frac{299}{60}$

$$\frac{299}{60}\int\left(\frac{1}{x} + \frac{1}{300 - x}\right)\mathrm{d}x = \int \mathrm{d}t$$

$$\frac{299}{60}\left(\ln x - \ln(300 - x)\right) = t + C$$

$$\frac{299}{60}\ln\left(\frac{x}{300 - x}\right) = t + C$$

Use $x = 1$, $t = 0$:

$$C = \frac{299}{60}\ln\frac{1}{299}$$

$$t = \frac{299}{60}\left[\ln\left(\frac{x}{300 - x}\right) - \ln\frac{1}{299}\right]$$

$$t = \frac{299}{60}\ln\left(\frac{299x}{300 - x}\right) \quad\checkmark \quad \text{(computed estimate)}$$

**What the examiner wants:** the proportionality constant found from the rate at $x = 1$, partial fractions, and log laws to compress into a single logarithm exactly as requested.

## 4.4 Tanks and Containers

$$\frac{\mathrm{d}V}{\mathrm{d}t} = \text{rate in} - \text{rate out}, \qquad \frac{\mathrm{d}h}{\mathrm{d}t} = \frac{\mathrm{d}V}{\mathrm{d}t} \times \frac{\mathrm{d}h}{\mathrm{d}V}$$

For a cone, express $r$ in terms of $h$ using similar triangles before differentiating.

### Example 10 - Inverted Cone of Paint (Medium) (source: coursebook Exercise 10B Q5)

> **Question:** An inverted cone (radius 10 cm, height 15 cm at the rim) is full of paint. Paint drips out of a hole at the bottom at $16\ \text{cm}^3$ per second. At time $t$ the paint is a cone of depth $h$ cm.
> (a) Show that $\frac{\mathrm{d}V}{\mathrm{d}h} = \frac{4}{9}\pi h^2$.
> (b) Hence find an expression for $\frac{\mathrm{d}h}{\mathrm{d}t}$.
> (c) Solve the DE, giving $t$ in terms of $h$.
> (d) Find the time for the depth to fall to 7.5 cm.

**Solution:**

(a) By similar triangles:

$$\frac{r}{h} = \frac{10}{15} = \frac{2}{3} \;\Rightarrow\; r = \frac{2h}{3}$$

$$V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi\left(\frac{2h}{3}\right)^2 h = \frac{1}{3}\pi \cdot \frac{4h^2}{9} \cdot h$$

$$V = \frac{4\pi h^3}{27}$$

$$\frac{\mathrm{d}V}{\mathrm{d}h} = \frac{4\pi \cdot 3h^2}{27} = \frac{4\pi h^2}{9} \quad\checkmark$$

(b)

$$\frac{\mathrm{d}h}{\mathrm{d}t} = \frac{\mathrm{d}V}{\mathrm{d}t} \times \frac{\mathrm{d}h}{\mathrm{d}V} = -16 \times \frac{9}{4\pi h^2}$$

$$\frac{\mathrm{d}h}{\mathrm{d}t} = -\frac{36}{\pi h^2} \quad\checkmark$$

(c)

$$\int \pi h^2\,\mathrm{d}h = \int -36\,\mathrm{d}t$$

$$\frac{\pi h^3}{3} = -36t + C$$

Use $h = 15$, $t = 0$:

$$C = \frac{\pi(15)^3}{3} = 1125\pi$$

$$\frac{\pi h^3}{3} = -36t + 1125\pi$$

$$36t = \pi\left(1125 - \frac{h^3}{3}\right) = \frac{\pi(3375 - h^3)}{3}$$

$$t = \frac{\pi(3375 - h^3)}{108} \quad\checkmark$$

(d) $h = 7.5$:

$$t = \frac{\pi(3375 - 421.875)}{108} = \frac{2953.125\pi}{108}$$

$$t = 85.9 \text{ seconds} \quad (3\text{ s.f.}) \quad\checkmark$$

**What the examiner wants:** similar triangles first (you cannot start without $r$ in terms of $h$), the chain rule written explicitly, and the negative sign on the outflow.

### Example 11 - Cylindrical Tank Draining (Hard) (source: CAIE ON24 P31 Q10)

> **Question:** A cylindrical tank has a base of radius 4 m. At time $t$ minutes the depth of water is $h$ m. With the tap open, water flows out at a rate proportional to the square root of the volume of water in the tank.
> (a) Show that $\frac{\mathrm{d}h}{\mathrm{d}t} = -m\sqrt{h}$, where $m$ is a positive constant.
> (b) Given $h = 4$ when $t = 0$ and $h = 2.25$ when $t = 20$, solve the DE to obtain $t$ in terms of $h$, and find the time taken to empty the tank.

**Solution:**

(a) Done in Part 1, Example 6:

$$\frac{\mathrm{d}h}{\mathrm{d}t} = -m\sqrt{h}, \quad m = \frac{k}{4\sqrt{\pi}} > 0$$

(b) Separate:

$$\int \frac{1}{\sqrt{h}}\,\mathrm{d}h = \int -m\,\mathrm{d}t$$

$$2\sqrt{h} = -mt + C$$

Use $h = 4$, $t = 0$:

$$2(2) = 4 = C$$

Use $h = 2.25$, $t = 20$:

$$2(1.5) = 3 = -20m + 4$$

$$m = \frac{1}{20}$$

$$2\sqrt{h} = 4 - \frac{t}{20}$$

$$t = 80 - 40\sqrt{h} \quad\checkmark$$

Empty means $h = 0$:

$$t = 80 - 0 = 80$$

$$t = 80 \text{ minutes} \quad\checkmark \quad \text{(computed estimate)}$$

**What the examiner wants:** both pairs of values used correctly (first for $C$, second for $m$), and interpreting "empty" as $h = 0$.

### Example 12 - Cube Tank with Inflow and Outflow (Hard) (source: CAIE ON25 P32 Q10)

> **Question:** A tank is a cube of side 50 cm. At time $t$ seconds the depth of water is $h$ cm. Water pours in at $5000\ \text{cm}^3\,\text{s}^{-1}$ and pours out through a hole at a rate proportional to $h^2$. When $h = 20$, the depth is increasing at 0.4 cm s$^{-1}$.
> (a) Show that $\frac{\mathrm{d}h}{\mathrm{d}t} = 2 - \frac{h^2}{250}$.
> (b) Given $h = 0$ when $t = 0$, find the time taken for the depth to reach 20 cm.

**Solution:**

(a) Done in Part 1, Example 7:

$$\frac{\mathrm{d}h}{\mathrm{d}t} = 2 - \frac{h^2}{250} = \frac{500 - h^2}{250}$$

(b) Separate:

$$\int \frac{250}{500 - h^2}\,\mathrm{d}h = \int \mathrm{d}t$$

Partial fractions with $500 - h^2 = (\sqrt{500} - h)(\sqrt{500} + h)$:

$$\frac{250}{500 - h^2} = \frac{125}{\sqrt{500}}\left(\frac{1}{\sqrt{500} - h} + \frac{1}{\sqrt{500} + h}\right)$$

$$\int \frac{250}{500 - h^2}\,\mathrm{d}h = \frac{125}{\sqrt{500}}\left(-\ln(\sqrt{500} - h) + \ln(\sqrt{500} + h)\right)$$

$$= \frac{125}{\sqrt{500}}\ln\left(\frac{\sqrt{500} + h}{\sqrt{500} - h}\right)$$

$$t = \frac{125}{\sqrt{500}}\ln\left(\frac{\sqrt{500} + h}{\sqrt{500} - h}\right) + C$$

Use $h = 0$, $t = 0$:

$$0 = \frac{125}{\sqrt{500}}\ln\left(\frac{\sqrt{500}}{\sqrt{500}}\right) + C = C$$

$$C = 0$$

$$\frac{125}{\sqrt{500}} = \frac{125}{10\sqrt{5}} = \frac{5\sqrt{5}}{2}$$

$$t = \frac{5\sqrt{5}}{2}\ln\left(\frac{10\sqrt{5} + h}{10\sqrt{5} - h}\right)$$

At $h = 20$:

$$t = \frac{5\sqrt{5}}{2}\ln\left(\frac{10\sqrt{5} + 20}{10\sqrt{5} - 20}\right)$$

$$\frac{10\sqrt{5} + 20}{10\sqrt{5} - 20} = \frac{42.3607}{2.3607} = 17.944$$

$$t = \frac{5\sqrt{5}}{2}\ln(17.944) = 5.5902 \times 2.8874$$

$$t = 16.14 \text{ seconds}$$

$$t = 16.1 \text{ seconds} \quad (3\text{ s.f.}) \quad\checkmark \quad \text{(computed estimate)}$$

**What the examiner wants:** the rate-in-minus-rate-out setup, the derivative data at $h = 20$ to fix $k$, and the partial-fraction integral of $\frac{250}{500 - h^2}$. The June 2023 report noted sign errors in the course of integration were the most common fault after partial fractions.

## 4.5 Other Rates: Chemical Reactions

Same toolkit, different contexts. The syllabus guarantees no specialised knowledge of the context is required - everything you need is in the question.

### Example 13 - Chemical Reaction Producing $C$ (Medium) (source: coursebook End-of-Chapter Review Exercise 10 Q5)

> **Question:** A chemical reaction takes place between substances $A$ and $B$, producing substance $C$. After $t$ hours there are $5 - x$ grams of $A$, $10 - x$ grams of $B$ and $x$ grams of $C$ present. The rate of increase of $x$ is proportional to the product of $5 - x$ and $10 - x$. Initially $x = 0$ and the rate of increase of $x$ is 1 gram per hour.
> (i) Show that $x$ and $t$ satisfy $50\frac{\mathrm{d}x}{\mathrm{d}t} = (5 - x)(10 - x)$.
> (ii) Solve this equation, giving $x$ in terms of $t$.
> (iii) According to the model, approximately how many grams of chemical $C$ are produced by the reaction?

**Solution:**

(i) Done in Part 1, Practice Q3:

$$\frac{\mathrm{d}x}{\mathrm{d}t} = \frac{(5 - x)(10 - x)}{50}$$

(ii) Separate:

$$\int \frac{50}{(5 - x)(10 - x)}\,\mathrm{d}x = \int \mathrm{d}t$$

Partial fractions: $\frac{50}{(5 - x)(10 - x)} = \frac{A}{5 - x} + \frac{B}{10 - x}$:

$$50 = A(10 - x) + B(5 - x)$$

$x = 5$: $50 = 5A \;\Rightarrow\; A = 10$

$x = 10$: $50 = -5B \;\Rightarrow\; B = -10$

$$\int\left(\frac{10}{5 - x} - \frac{10}{10 - x}\right)\mathrm{d}x = \int \mathrm{d}t$$

$$-10\ln(5 - x) + 10\ln(10 - x) = t + C$$

$$10\ln\left(\frac{10 - x}{5 - x}\right) = t + C$$

Use $x = 0$, $t = 0$:

$$10\ln\frac{10}{5} = 10\ln 2 = C$$

$$10\ln\left(\frac{10 - x}{5 - x}\right) = t + 10\ln 2$$

$$\frac{10 - x}{5 - x} = 2e^{t/10}$$

$$10 - x = 2e^{t/10}(5 - x) = 10e^{t/10} - 2xe^{t/10}$$

$$x(2e^{t/10} - 1) = 10e^{t/10} - 10$$

$$x = \frac{10(e^{t/10} - 1)}{2e^{t/10} - 1} \quad\checkmark$$

(iii) As $t \to \infty$, divide top and bottom by $e^{t/10}$:

$$x = \frac{10(1 - e^{-t/10})}{2 - e^{-t/10}} \to \frac{10}{2} = 5$$

$$x \to 5 \text{ grams} \quad\checkmark$$

**What the examiner wants:** the sign of each partial fraction term, and reading the long-term production off the solution.

### Example 14 - Chemical $X$ Decreasing (Medium) (source: coursebook End-of-Chapter Review Exercise 10 Q10; solved in Part 3, Practice Q3)

> **Question:** At the start of a reaction there are $x$ grams of chemical $X$ present. At time $t$ seconds after the start, the rate of decrease of $x$ is proportional to $xt$. Initially there are 150 grams of $X$ and after 10 seconds this has decreased to 120 grams. Find the time after the start when the amount of $X$ has decreased to 1 gram.

**Solution:**

$$\frac{\mathrm{d}x}{\mathrm{d}t} = -kxt, \quad k > 0$$

$$\int \frac{1}{x}\,\mathrm{d}x = \int -kt\,\mathrm{d}t$$

$$\ln x = -\frac{kt^2}{2} + C$$

$$x = 150e^{-kt^2/2}$$

Use $x = 120$, $t = 10$:

$$120 = 150e^{-50k}$$

$$k = \frac{\ln 1.25}{50}$$

Set $x = 1$:

$$t^2 = \frac{100\ln 150}{\ln 1.25} = \frac{100 \times 5.0106}{0.22314} = 2245.5$$

$$t = 47.4 \text{ seconds} \quad\checkmark \quad \text{(computed estimate)}$$

**What the examiner wants:** the DE is separable despite the $xt$ product, because $t$ is the independent variable - everything in $x$ on the left, everything in $t$ on the right.

---

### Practice Questions - Part 4

1. **Q1 (Easy)** The size of a population $P$ at time $t$ minutes is modelled as a continuous variable such that the rate of increase of $P$ is directly proportional to $P$. (a) Write down a differential equation satisfied by $P$. (b) The initial size is $P_0$; show that $P = P_0e^{kt}$, $k > 0$. (c) The population is $1.5P_0$ after 2 minutes. Find when the population will be $3P_0$. (source: coursebook Exercise 10B Q6; answer computed estimate)

**Solution:**

(a)

$$\frac{\mathrm{d}P}{\mathrm{d}t} = kP, \quad k > 0$$

(b)

$$\int \frac{1}{P}\,\mathrm{d}P = \int k\,\mathrm{d}t$$

$$\ln P = kt + C$$

$P = P_0$ at $t = 0$ gives $C = \ln P_0$:

$$P = P_0e^{kt} \quad\checkmark$$

(c) Use $P = 1.5P_0$ at $t = 2$:

$$1.5 = e^{2k} \;\Rightarrow\; k = \frac{1}{2}\ln 1.5$$

Set $P = 3P_0$:

$$3 = e^{kt}$$

$$t = \frac{\ln 3}{k} = \frac{2\ln 3}{\ln 1.5}$$

$$t = \frac{2 \times 1.0986}{0.4055} = 5.42 \text{ minutes} \quad\checkmark$$

2. **Q2 (Medium)** The cost of designing an aircraft, \$A per kilogram, at time $t$ years after 1950 can be modelled as a continuous variable. The rate of increase of $A$ is directly proportional to $A$. (a) Write down a differential equation satisfied by $A$. (b) In 1950 the cost was \$12 per kilogram; show that $A = 12e^{kt}$. (c) After 25 years the cost was \$48 per kilogram. Find the cost after 60 years. (source: coursebook Exercise 10B Q3; answer computed estimate)

**Solution:**

(a)

$$\frac{\mathrm{d}A}{\mathrm{d}t} = kA, \quad k > 0$$

(b) $A = 12$ at $t = 0$, so:

$$A = 12e^{kt} \quad\checkmark$$

(c) Use $A = 48$, $t = 25$:

$$48 = 12e^{25k}$$

$$e^{25k} = 4$$

$$k = \frac{\ln 4}{25}$$

At $t = 60$:

$$A = 12e^{60k} = 12e^{\frac{60\ln 4}{25}} = 12 \times 4^{12/5}$$

$$4^{2.4} = e^{2.4 \times 1.3863} = e^{3.3271} = 27.858$$

$$A = 12 \times 27.858 = 334.3$$

$$A = \$334 \quad (3\text{ s.f.}) \quad\checkmark$$

3. **Q3 (Medium)** A bottle of water is taken out of a refrigerator at 4 °C and placed outside where the air temperature is a constant 24 °C. The rate at which the water warms up is proportional to the difference between the air temperature and the water temperature. After 2 minutes the water is 11 °C. (a) How long does it take for the water to warm 20 °C? (b) According to the model, what temperature will the water eventually reach? (source: coursebook Exercise 10B Q11; answer computed estimate)

**Solution:**

Newton's law of heating with surroundings $s = 24$:

$$T = 24 + (4 - 24)e^{-kt} = 24 - 20e^{-kt}$$

Use $T = 11$, $t = 2$:

$$11 = 24 - 20e^{-2k}$$

$$20e^{-2k} = 13$$

$$e^{-2k} = \frac{13}{20}$$

$$k = \frac{1}{2}\ln\frac{20}{13} = 0.2154$$

(a) Warming 20 °C means reaching $T = 24$ °C:

$$24 = 24 - 20e^{-kt}$$

$$e^{-kt} = 0$$

$$t \to \infty$$

The model says the water never quite reaches 24 °C - it approaches the air temperature asymptotically, so there is no finite time at which it has warmed the full 20 °C.

(b)

$$T \to 24 \text{ °C eventually} \quad\checkmark$$

4. **Q4 (Hard)** The population of a country was 50 million in 2000 and 60 million in 2010. The rate of increase of the population is modelled by $\frac{\mathrm{d}P}{\mathrm{d}t} = \frac{kP(100 - P)}{100}$. Use the model to predict the population in 2025. (source: coursebook End-of-Chapter Review Exercise 10 Q12; answer computed estimate)

**Solution:**

$$\int \frac{100}{P(100 - P)}\,\mathrm{d}P = \int k\,\mathrm{d}t$$

Partial fractions: $\frac{100}{P(100 - P)} = \frac{1}{P} + \frac{1}{100 - P}$:

$$\ln P - \ln(100 - P) = kt + C$$

Use $P = 50$, $t = 0$ (year 2000):

$$\ln\frac{50}{50} = 0 = C$$

$$\ln\left(\frac{P}{100 - P}\right) = kt$$

Use $P = 60$, $t = 10$ (year 2010):

$$\ln\frac{60}{40} = \ln 1.5 = 10k$$

$$k = \frac{\ln 1.5}{10} = 0.04055$$

At $t = 25$ (year 2025):

$$\ln\left(\frac{P}{100 - P}\right) = 25k = 25 \times 0.04055 = 1.0137$$

$$\frac{P}{100 - P} = e^{1.0137} = 2.7557$$

$$P = 2.7557(100 - P)$$

$$P(1 + 2.7557) = 275.57$$

$$P = \frac{275.57}{3.7557} = 73.37$$

$$P = 73.4 \text{ million} \quad\checkmark$$

5. **Q5 (Hard)** There are 2000 mice in a field. At time $t$ hours, $x$ mice are infected with a disease. The rate of increase of the number of mice infected is proportional to the product of the number infected and the number not infected. Initially 500 mice are infected and the disease is spreading at a rate of 50 mice per hour. (a) Form and solve a differential equation, giving $t$ in terms of $x$. (b) Find how long it takes for 1900 mice to be infected. (source: coursebook End-of-Chapter Review Exercise 10 Q15; answers computed estimate)

**Solution:**

(a)

$$\frac{\mathrm{d}x}{\mathrm{d}t} = kx(2000 - x)$$

At $x = 500$, $\frac{\mathrm{d}x}{\mathrm{d}t} = 50$:

$$50 = k(500)(1500) = 750\,000k$$

$$k = \frac{50}{750\,000} = \frac{1}{15\,000}$$

$$\frac{\mathrm{d}x}{\mathrm{d}t} = \frac{x(2000 - x)}{15\,000}$$

$$\int \frac{15\,000}{x(2000 - x)}\,\mathrm{d}x = \int \mathrm{d}t$$

Partial fractions: $\frac{15\,000}{x(2000 - x)} = \frac{7.5}{x} + \frac{7.5}{2000 - x}$:

$$7.5\left(\ln x - \ln(2000 - x)\right) = t + C$$

$$7.5\ln\left(\frac{x}{2000 - x}\right) = t + C$$

Use $x = 500$, $t = 0$:

$$C = 7.5\ln\frac{500}{1500} = 7.5\ln\frac{1}{3}$$

$$t = 7.5\left[\ln\left(\frac{x}{2000 - x}\right) - \ln\frac{1}{3}\right]$$

$$t = 7.5\ln\left(\frac{3x}{2000 - x}\right) \quad\checkmark$$

(b) $x = 1900$:

$$t = 7.5\ln\left(\frac{5700}{100}\right) = 7.5\ln 57$$

$$t = 7.5 \times 4.0431 = 30.32$$

$$t = 30.3 \text{ hours} \quad\checkmark$$

---

# Formula Sheet

### Forming Differential Equations

$$\frac{\mathrm{d}x}{\mathrm{d}t} = \pm k(\dots), \quad k > 0 \qquad \text{("increase" } + \text{, "decrease" } -\text{)}$$

$$\text{Newton's law of cooling/heating: } \frac{\mathrm{d}T}{\mathrm{d}t} = -k(T - s), \quad k > 0$$

$$\text{Tanks: } \frac{\mathrm{d}V}{\mathrm{d}t} = \text{rate in} - \text{rate out}, \qquad \frac{\mathrm{d}h}{\mathrm{d}t} = \frac{\mathrm{d}V}{\mathrm{d}t} \times \frac{\mathrm{d}h}{\mathrm{d}V}$$

$$\text{Kinematics: } v = \frac{\mathrm{d}s}{\mathrm{d}t}$$

### Separation of Variables

$$\frac{\mathrm{d}y}{\mathrm{d}x} = f(x)g(y) \;\Rightarrow\; \int \frac{1}{g(y)}\,\mathrm{d}y = \int f(x)\,\mathrm{d}x$$

$$\int \frac{1}{x}\,\mathrm{d}x = \ln|x| + C, \qquad \int \frac{f'(x)}{f(x)}\,\mathrm{d}x = \ln|f(x)| + C$$

$$\int e^{ax}\,\mathrm{d}x = \frac{1}{a}e^{ax}, \qquad \int \sin ax\,\mathrm{d}x = -\frac{1}{a}\cos ax, \qquad \int \cos ax\,\mathrm{d}x = \frac{1}{a}\sin ax$$

$$\int \sec^2 ax\,\mathrm{d}x = \frac{1}{a}\tan ax, \qquad \int \sec ax\tan ax\,\mathrm{d}x = \frac{1}{a}\sec ax$$

$$\int \frac{1}{a^2 + x^2}\,\mathrm{d}x = \frac{1}{a}\arctan\frac{x}{a} + C, \qquad \int \frac{1}{4 + 9y^2}\,\mathrm{d}y = \frac{1}{6}\arctan\frac{3y}{2} + C$$

$$\frac{1}{x(300 - x)} = \frac{1}{300}\left(\frac{1}{x} + \frac{1}{300 - x}\right), \qquad \frac{1}{y^2 + y} = \frac{1}{y} - \frac{1}{y + 1}, \qquad \int \frac{A}{b - x}\,\mathrm{d}x = -A\ln|b - x|$$

$$\int u\,\frac{\mathrm{d}v}{\mathrm{d}x}\,\mathrm{d}x = uv - \int v\,\frac{\mathrm{d}u}{\mathrm{d}x}\,\mathrm{d}x$$

$$\sin 4y = 2\sin 2y\cos 2y \;\Rightarrow\; \frac{\sin 4y}{\sin 2y} = 2\cos 2y$$

### General and Particular Solutions

$$\text{General solution: one arbitrary constant } C \text{ (family of curves)}$$

$$\text{Particular solution: substitute the initial condition into the integrated form only, solve for } C$$

$$e^{\ln a} = a, \qquad e^{a + b} = e^a e^b, \qquad e^{a\ln b} = b^a, \qquad e^{-\ln a} = \frac{1}{a}$$

$$\ln|x| \text{ by default; drop the modulus only when the argument is known positive}$$

### Standard Models

$$\frac{\mathrm{d}x}{\mathrm{d}t} = kx \;\Rightarrow\; x = x_0e^{kt} \qquad \frac{\mathrm{d}x}{\mathrm{d}t} = -kx \;\Rightarrow\; x = x_0e^{-kt}$$

$$\frac{\mathrm{d}x}{\mathrm{d}t} = k(M - x) \;\Rightarrow\; x = M - (M - x_0)e^{-kt}$$

$$\frac{\mathrm{d}T}{\mathrm{d}t} = -k(T - s) \;\Rightarrow\; T = s + (T_0 - s)e^{-kt}$$

$$\frac{\mathrm{d}x}{\mathrm{d}t} = kx(M - x) \;\Rightarrow\; x = \frac{M}{1 + Ae^{-kMt}} \quad (x \to M \text{ as } t \to \infty)$$

$$\text{Half-life} = \text{doubling time} = \frac{\ln 2}{k}, \qquad e^{-kt} = 2^{-t/T}$$

---

# Quick Reference Card

1. **Translate the rate statement:** $\frac{\mathrm{d}x}{\mathrm{d}t} = \pm k(\dots)$, state $k > 0$; "decrease" or "leaking" gives the minus sign.
2. **Separate:** move everything in the dependent variable to the left, everything else to the right, then $\int$ both sides with one $+C$.
3. **Integrate:** pick the technique from topic 3.5 - standard integrals, derivative-on-top $\ln|f|$, partial fractions, arctan, parts, identities.
4. **Fix constants:** first condition gives $C$, second condition gives $k$; substitute into the integrated form, never into the DE.
5. **Clean up:** remove logs with $e^{\ln a} = a$; keep moduli unless the argument is known positive; make the requested variable the subject.
6. **Interpret:** $t \to \infty$ kills $e^{-kt}$ terms (limiting value); justify every long-term statement from the solution; comment on model fit and assumptions.
7. **Check:** differentiate your final answer - it must reproduce the original DE - and verify the initial condition. If you divided by a function of $y$, check whether the excluded value (e.g. $y = 0$) is itself a solution.

> **Good luck!** Every 9709 differential equation question is one of the patterns in this guide: form the DE, separate, integrate, fix the constant, interpret. 🚀
