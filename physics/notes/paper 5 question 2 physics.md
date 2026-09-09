# CAIE Physics 9702 -- Paper 5 Question 2 Complete Guide

> **What is Question 2?** You get a table of data, a graph grid, and you must:
> 1. Process the data table (calculate values + uncertainties)
> 2. Plot the graph with error bars
> 3. Draw best-fit + worst acceptable lines
> 4. Find gradient + intercept (with uncertainties)
> 5. Use them to find physical constants
> 6. Do one final calculation
>
> **Always 15 marks. Always follows the same steps.**

---

## Before You Start: The 18+ Types of Questions You Will See

From past papers + WS, every Question 2 is one of these 19. The method is always the same -- only the equation changes. Rows 13-19 are the 6 WS relationships (pages 9-25) added for completeness.

| # | Type | Equation | Graph | Gradient | Intercept |
|---|------|----------|-------|----------|-----------|
| 1 | **Exponential decay** | $R = R_0 e^{-\mu t}$ | $\ln R$ vs $t$ | $-\mu$ | $\ln R_0$ |
| 2 | **Cooling** | $\theta = \theta_R + (\theta_0 - \theta_R)e^{-t/K}$ | $\ln(\theta-\theta_R)$ vs $t$ | $-1/K$ | $\ln(\theta_0-\theta_R)$ |
| 3 | **Viscosity** | $\eta = H e^{E/kT}$ | $\ln \eta$ vs $1/T$ | $E/k$ | $\ln H$ |
| 4 | **Power law** | $L = kM^n$ | $\lg L$ vs $\lg M$ | $n$ | $\lg k$ |
| 5 | **Capacitor discharge** | $V = I_0 R e^{-t/CR}$ | $\ln V$ vs $1/C$ | $-t/R$ | $\ln(I_0 R)$ |
| 6 | **Circular motion** | $Pg = mv^2/r$ | $v^2$ vs $r$ | $Pg/m$ | $0$ |
| 7 | **Pendulum** | $T^2 = \frac{4\pi^2}{g}(k-d)$ | $T^2$ vs $d$ | $-4\pi^2/g$ | $4\pi^2 k/g$ |
| 8 | **Doppler effect** | $f = \frac{f_s k}{k-v}$ | $1/f$ vs $v$ | $-1/(f_s k)$ | $1/f_s$ |
| 9 | **Lens** | $\frac{h_i}{h_o} = \frac{2f + t - d}{f}$ | $h_i/h_o$ vs $d$ | $-1/f$ | $(2f+t)/f$ |
| 10 | **Hubble / Redshift** | $\lambda = \lambda_0\left(1 + \frac{Hd}{c}\right)$ | $\lambda$ vs $d/c$ | $\lambda_0 H$ | $\lambda_0$ |
| 11 | **Phase difference** | $\tan\theta = \frac{1}{2\pi f C R}$ | $\tan\theta$ vs $1/R$ | $1/(2\pi f C)$ | $0$ |
| 12 | **Springs** | $T = 2\pi\sqrt{M/k}$ | $T^2$ vs $1/k$ | $4\pi^2 M$ | $0$ |
| 13 | **Foam attenuation** *(WS)* | $I = I_0 e^{-\alpha \rho t}$ | $\ln I$ vs $t$ | $-\alpha \rho$ | $\ln I_0$ |
| 14 | **Resonance tube** *(WS)* | $v = 2Lf + k d f$ | $1/f$ vs $d$ | $k/v$ | $2L/v$ |
| 15 | **Inclined plane** *(WS)* | $\frac{2d}{t^2} = \frac{A H}{A+B}\sin\theta + \frac{K A}{A+B}$ | $1/t^2$ vs $\sin\theta$ |$AH/(A+B)$ | $KA/(A+B)$ |
| 16 | **Heating blocks** *(WS)* | $E = a m + b$ | $E$ vs $m$ | $a$ | $b$ |
| 17 | **Turntable** *(WS)* | $\frac{K f_0^2}{f} = \beta K + m r$ | $1/f$ vs $m$ | $r/(K f_0^2)$ | $\beta/f_0^2$ |
| 18 | **Charged spheres** *(WS)* | $F = \frac{\alpha V^2}{r^2}$ | $F$ vs $V^2$ | $\alpha/r^2$ | $0$ |
| 19 | **Parallel plates** *(WS)* | $\frac{W}{C d} = \frac{1}{K A} + \frac{V}{K A}$ | $1/d$ vs $V$ | $C/(K A)$ | $C/(W K A)$ |

---

## Section 0: The Mark Breakdown (Exactly What You Get Marks For)

| Part | What You Do | Marks |
|------|------------|-------|
| **(a)** | Rearrange equation into $y=mx+c$, write gradient + intercept expressions | **1** |
| **(b)** | Fill table with processed values + uncertainties | **2-4** |
| **(c)(i)** | Plot graph with error bars | **2** |
| **(c)(ii)** | Draw best-fit + worst acceptable line (WAL) | **2** |
| **(c)(iii)** | Find gradient + its uncertainty | **2** |
| **(c)(iv)** | Find y-intercept + its uncertainty | **2** |
| **(d)** | Use gradient/intercept to find physical constants | **2-3** |
| **(e)** | Do one final calculation using your constants | **1** |
| **Total** | | **15** |

---

## Section 1: Part (a) -- Find Gradient & Intercept Expressions (1 mark)

### What You Do

You're given the equation and told what to plot. Just rearrange into $y = mx + c$ form and read off $m$ and $c$.

### The Method (Always 3 Steps)

1. Write the **given equation**
2. **Rearrange** so the y-axis quantity is alone on the left
3. **Read off:** gradient = coefficient of x, intercept = everything else

### Example 1: Exponential Decay (Geiger-Müller)

> Given: $R = R_0 e^{-\mu t}$. Graph: $\ln R$ on y-axis, $t$ on x-axis.

Take $\ln$ of both sides:

$$\ln R = \ln(R_0 e^{-\mu t}) = \ln R_0 + \ln(e^{-\mu t}) = \ln R_0 - \mu t$$

So:

$$\ln R = (-\mu)t + \ln R_0$$

Answer:
- **Gradient** = $-\mu$
- **y-intercept** = $\ln R_0$

### Example 2: Power Law (Star Luminosity)

> Given: $\lambda = k \mu^n$. Graph: $\lg \lambda$ on y-axis, $\lg \mu$ on x-axis.

Take $\lg$ of both sides:

$$\lg \lambda = \lg(k \mu^n) = \lg k + \lg(\mu^n) = \lg k + n \lg \mu$$

So:

$$\lg \lambda = (n)\lg \mu + \lg k$$

Answer:
- **Gradient** = $n$
- **y-intercept** = $\lg k$

### Example 3: Cooling

> Given: $\theta = \theta_R + (\theta_0 - \theta_R)e^{-t/K}$. Graph: $\ln(\theta - \theta_R)$ on y-axis, $t$ on x-axis.

Step 1: Isolate the exponential:

$$\theta - \theta_R = (\theta_0 - \theta_R)e^{-t/K}$$

Step 2: Take $\ln$:

$$\ln(\theta - \theta_R) = \ln(\theta_0 - \theta_R) + \ln(e^{-t/K}) = \ln(\theta_0 - \theta_R) - \frac{t}{K}$$

So:

$$\ln(\theta - \theta_R) = \left(-\frac{1}{K}\right)t + \ln(\theta_0 - \theta_R)$$

Answer:
- **Gradient** = $-\frac{1}{K}$
- **y-intercept** = $\ln(\theta_0 - \theta_R)$

### Example 4: Circular Motion

> Given: $Pg = \frac{mv^2}{r}$. Graph: $v^2$ on y-axis, $r$ on x-axis.

Rearrange:

$$v^2 = \left(\frac{Pg}{m}\right) r$$

Answer:
- **Gradient** = $\frac{Pg}{m}$
- **y-intercept** = $0$

### More Part (a) Examples

**Example 5: Springs (9702/52/M/J/19)**

> Given: $T = 2\pi\sqrt{M/k}$. Graph: $T^2$ on y-axis, $1/k$ on x-axis.

Square both sides:

$$T^2 = 4\pi^2 \frac{M}{k} = (4\pi^2 M)\frac{1}{k}$$

Answer:
- **Gradient** = $4\pi^2 M$
- **y-intercept** = $0$

**Example 6: Capacitor Discharge (9702/52/O/N/23)**

> Given: $V = I_0 R e^{-t/CR}$. Graph: $\ln V$ on y-axis, $1/C$ on x-axis.

Take $\ln$:

$$\ln V = \ln(I_0 R) + \ln(e^{-t/CR}) = \ln(I_0 R) - \frac{t}{C R}$$

$$\ln V = \left(-\frac{t}{R}\right)\frac{1}{C} + \ln(I_0 R)$$

Answer:
- **Gradient** = $-\frac{t}{R}$
- **y-intercept** = $\ln(I_0 R)$

**Example 7: Phase Difference (9702/52/F/M/22)**

> Given: $\tan\theta = \frac{1}{2\pi f C R}$. Graph: $\tan\theta$ on y-axis, $1/R$ on x-axis.

$$\tan\theta = \left(\frac{1}{2\pi f C}\right)\frac{1}{R}$$

Answer:
- **Gradient** = $\frac{1}{2\pi f C}$
- **y-intercept** = $0$

**Example 8: Doppler Effect (9702/51/M/J/24)**

> Given: $f = \frac{f_s k}{k - v}$. Graph: $1/f$ on y-axis, $v$ on x-axis.

Invert:

$$\frac{1}{f} = \frac{k - v}{f_s k} = \frac{1}{f_s} - \frac{1}{f_s k} v$$

$$\frac{1}{f} = \left(-\frac{1}{f_s k}\right)v + \frac{1}{f_s}$$

Answer:
- **Gradient** = $-\frac{1}{f_s k}$
- **y-intercept** = $\frac{1}{f_s}$

**Example 9: Lens (9702/51/O/N/20)**

> Given: $\frac{h_i}{h_o} = \frac{2f + t - d}{f}$. Graph: $\frac{h_i}{h_o}$ on y-axis, $d$ on x-axis.

$$\frac{h_i}{h_o} = \frac{2f + t}{f} - \frac{d}{f} = \left(-\frac{1}{f}\right)d + \frac{2f + t}{f}$$

Answer:
- **Gradient** = $-\frac{1}{f}$
- **y-intercept** = $\frac{2f + t}{f}$

**Example 10: Pendulum (9702/52/M/J/14)**

> Given: $T^2 = \frac{4\pi^2}{g}(k - d)$. Graph: $T^2$ on y-axis, $d$ on x-axis.

$$T^2 = -\frac{4\pi^2}{g}d + \frac{4\pi^2 k}{g}$$

Answer:
- **Gradient** = $-\frac{4\pi^2}{g}$
- **y-intercept** = $\frac{4\pi^2 k}{g}$

### Template for Part (a) Answer

Write exactly this format:

```
y = [y-axis quantity]
x = [x-axis quantity]

Rearranged equation:
[y] = ([gradient expr])[x] + ([intercept expr])

gradient = [full expression]
y-intercept = [full expression]
```

### Traps to Avoid

1. **Don't write just the constant name!** The gradient expression is $\frac{Pg}{m}$, not just $P$. If you write just $P$, you lose the mark. Always write the **full expression**.
2. **Don't forget the sign!** If gradient is $-\mu$, don't write $\mu$. That negative sign is part of the answer.
3. **Don't confuse $\ln$ and $\lg$.** $\ln$ = natural log (base $e$). $\lg$ = log base 10.

---

## Section 2: Part (b) -- Process the Data Table (2-4 marks)

### 2.1 Calculating Processed Quantities

You'll be asked to calculate things like $\ln R$, $1/f$, $T^2$, $\frac{1}{C}$, etc. Just do the math for each row.

**Example (Circular Motion, 9702/53/O/N/15):**

Given $r$ and $t$, find $T$, $v$, and $v^2$.

| $r$/m | $t$/s | $T$/s | $v$ / $\text{m s}^{-1}$ | $v^2$ / $\text{m}^2\text{s}^{-2}$ |
|-------|-------|-------|-----------|-------------|
| 0.160 | 3.4±0.2 | | | |
| 0.280 | 4.0±0.2 | | | |

$T = t / 10$ (10 revolutions), $v = 2\pi r / T$, $v^2 = (2\pi r / T)^2$

Row 1: $T = 3.4/10 = 0.34$ s, $v = 2\pi(0.160)/0.34 = 2.96$\text{m s}^{-1}$, $v^2 = 8.74$\text{m}^2\text{s}^{-2}$

### 2.2 Significant Figures Rule

This is where marks are lost. The rule depends on what you're calculating.

| If you're calculating... | Rule |
|--------------------------|------|
| **$\ln$ or $\lg$ of something** | **Decimal places** in answer = **significant figures** in raw data |
| **Any other processed quantity** ($T^2$, $1/k$, $v^2$) | Same **s.f.** as raw data (or 1 more max) |

**Why?** The integer part of a log tells you the order of magnitude (not meaningful). Only the decimal part carries precision. So if $R = 47.7$ (3 s.f.), then $\ln(47.7) = 3.865$ (3 decimal places).

**Examples from past papers:**

| Raw data | s.f. | $\ln$ value | d.p. needed | $\lg$ value | d.p. needed |
|----------|------|-------------|-------------|-------------|-------------|
| 47.7 | 3 | 3.865 | **3** | 1.679 | **3** |
| 44.0 | 3 | 3.784 | **3** | 1.643 | **3** |
| 12.3 | 3 | 2.510 | **3** | 1.090 | **3** |
| 4.6 | 2 | 1.526 | **2** | 0.663 | **2** |

### 2.3 Repeated Readings (Finding Average + Uncertainty)

When two readings $t_1$ and $t_2$ are given:

$$\text{Average} = \frac{t_1 + t_2}{2}$$

$$\text{Uncertainty} = \frac{|t_1 - t_2|}{2}$$

**Example (Geiger-Müller, 9702/52/O/N/21):**

$t_1 = 0.19$ mm, $t_2 = 0.13$ mm

Average $t = \frac{0.19 + 0.13}{2} = 0.16$ mm

$\Delta t = \frac{|0.19 - 0.13|}{2} = \frac{0.06}{2} = 0.03$ mm

So $t = 0.16 \pm 0.03$ mm

### 2.4 Uncertainty Rules (KNOW THESE COLD)

There are only 4 rules. Memorize them.

#### Rule 1: Sum or Difference -- ADD ABSOLUTE UNCERTAINTIES

$$\Delta(A + B) = \Delta A + \Delta B$$
$$\Delta(A - B) = \Delta A + \Delta B$$

**Always add.** Doesn't matter if you're adding or subtracting.

**Example (Cooling, 9702/52/F/M/25):**

$\theta = 75.0 \pm 0.5$ $^{\circ}\text{C}$, $\theta_R = 18.5 \pm 0.5$ $^{\circ}\text{C}$

Find $\theta - \theta_R$: $75.0 - 18.5 = 56.5$ $^{\circ}\text{C}$

$\Delta(\theta - \theta_R) = 0.5 + 0.5 = 1.0$ $^{\circ}\text{C}$

Answer: $56.5 \pm 1.0$ $^{\circ}\text{C}$

#### Rule 2: Product or Quotient -- ADD PERCENTAGE UNCERTAINTIES

$$\frac{\Delta(A \times B)}{A \times B} = \frac{\Delta A}{A} + \frac{\Delta B}{B}$$

$$\frac{\Delta(A / B)}{A / B} = \frac{\Delta A}{A} + \frac{\Delta B}{B}$$

**Method:** Convert to %, add, convert back.

**Example (Circular Motion, 9702/53/O/N/15):**

$v = 2\pi r / T$, $r = 0.160$ m (exact), $T = 0.34 \pm 0.02$ s

% uncertainty in $T = \frac{0.02}{0.34} \times 100\% = 5.9\%$

% uncertainty in $v = 5.9\%$ (only $T$ has uncertainty since $r$ is exact)

$v = 2\pi(0.160)/0.34 = 2.96$\text{m s}^{-1}$

$\Delta v = 2.96 \times \frac{5.9}{100} = 0.17$\text{m s}^{-1}$

#### Rule 3: Power ($A^n$) -- MULTIPLY % UNCERTAINTY BY $n$

$$\frac{\Delta(A^n)}{A^n} = n \times \frac{\Delta A}{A}$$

**Example (Circular Motion):**

$v = 2.96 \pm 0.17$\text{m s}^{-1}$. Find $\Delta(v^2)$.

% uncertainty in $v = \frac{0.17}{2.96} \times 100\% = 5.7\%$

% uncertainty in $v^2 = 2 \times 5.7\% = 11.4\%$

$v^2 = (2.96)^2 = 8.74$\text{m}^2\text{s}^{-2}$

$\Delta(v^2) = 8.74 \times \frac{11.4}{100} = 1.0$\text{m}^2\text{s}^{-2}$

So $v^2 = 8.7 \pm 1.0$\text{m}^2\text{s}^{-2}$

#### Rule 4: Natural Log ($\ln x$) -- FRACTIONAL UNCERTAINTY

$$\Delta(\ln x) = \frac{\Delta x}{x}$$

**This is THE most important rule for Paper 5 Q2.** Almost every question uses it.

For $\lg x$ (log base 10):

$$\Delta(\lg x) = \frac{\Delta x}{x} \times \frac{1}{\ln 10} = \frac{\Delta x}{x \times 2.303}$$

> **Memorize this:** $\Delta(\ln x) = \Delta x / x$

**Example (Viscosity, 9702/52/M/J/20):**

$\eta = 12.3 \pm 0.2$ ($\times 10^{-4}$ Pa s)

$\ln(12.3) = 2.510$ (3 d.p. since 12.3 is 3 s.f.)

$\Delta(\ln \eta) = \frac{0.2}{12.3} = 0.016$

So $\ln \eta = 2.510 \pm 0.016$

**Example (Star Luminosity -- $\lg$, 9702/54/M/J/25):**

$\mu = 4.6 \pm 0.4$

$\lg(4.6) = 0.663$ (2 d.p. since 4.6 is 2 s.f.)

$\Delta(\lg \mu) = \frac{0.4}{4.6 \times 2.303} = \frac{0.4}{10.59} = 0.038$

So $\lg \mu = 0.66 \pm 0.04$

### 2.5 More Table Processing Examples

**Example: Pendulum (9702/52/M/J/14) -- Finding mean, T, T2**

Given $d$ and two $t$ readings (time for 10 oscillations).

| $d$/m | $t_1$/s | $t_2$/s | mean $t$/s | $T$/s | $T^2$/s2 |
|-------|---------|---------|------------|-------|----------|
| 0.45 ± 0.05 | 56.4 | 56.4 | | | |
| 0.70 ± 0.05 | 55.4 | 55.6 | | | |

**Row 1:**
- mean $t = (56.4 + 56.4)/2 = 56.4$ s
- $\Delta t = |56.4 - 56.4|/2 = 0.0$ s → but use instrument precision, say ±0.1
- $T = 56.4/10 = 5.64$ s
- $T^2 = (5.64)^2 = 31.8$ s2 (3 s.f. to match $d$)
- % unc. in $t = (0.1/56.4) \times 100\% = 0.18\%$
- % unc. in $T = 0.18\%$ (same, dividing by constant)
- % unc. in $T^2 = 2 \times 0.18\% = 0.36\%$
- $\Delta(T^2) = 31.8 \times 0.0036 = 0.11$ s2

**Example: Capacitor (9702/52/O/N/23) -- Finding $1/C$ from $C_A$ and $C_B$**

Given $C_A$, $C_B$, find $1/C$ where $\frac{1}{C} = \frac{C_A + C_B}{C_A C_B}$.

| $C_A/10^{-4}$F | $C_B/10^{-4}$F | $1/C / 10^{4}$F-1 | $V$/V | $\ln(V$/V) |
|----------------|----------------|-------------------|-------|------------|
| 2.2 | 2.2 | | 2.45 ± 0.05 | |
| 2.2 | 3.3 | | 2.75 ± 0.05 | |

**Row 1:**
- $\frac{1}{C} = \frac{2.2 + 2.2}{2.2 \times 2.2} = \frac{4.4}{4.84} = 0.909 \times 10^4$ F-1
- $\ln(2.45) = 0.896$ (3 d.p. -- 2.45 has 3 s.f.)
- $\Delta(\ln V) = 0.05/2.45 = 0.020$

**Row 2:**
- $\frac{1}{C} = \frac{2.2 + 3.3}{2.2 \times 3.3} = \frac{5.5}{7.26} = 0.758 \times 10^4$ F-1
- $\ln(2.75) = 1.012$ (3 d.p.)
- $\Delta(\ln V) = 0.05/2.75 = 0.018$

**Example: Hubble (9702/51/O/N/25) -- Finding $d/c$ with uncertainty propagation**

Given $d$ and its uncertainty, $c = 3.00 \times 10^5$ km s-1. Find $d/c$.

| $d / 10^{21}$ km | $d/c / 10^{15}$ s | $\lambda$/nm |
|------------------|-------------------|-------------|
| 0.48 ± 0.12 | | 658.4 |
| 1.04 ± 0.12 | | 661.2 |

**Row 1:**
- $d/c = 0.48 \times 10^{21} / 3.00 \times 10^5 = 0.48 \times 10^{21-5} / 3.00 = 0.48 \times 10^{16} / 3.00$
- Wait, careful with units: $d$ is in $10^{21}$ km, $c$ is in km s-1
- So $d/c = (0.48 \times 10^{21}) / (3.00 \times 10^5) = 0.16 \times 10^{16} = 1.6 \times 10^{15}$ s
- But table wants answer in $10^{15}$ s, so write: $1.6$
- $\Delta(d/c)$: % unc in $d = (0.12/0.48) \times 100\% = 25\%$
- % unc in $c = 0\%$ (given constant, exact)
- % unc in $d/c = 25\%$
- $\Delta(d/c) = 1.6 \times 0.25 = 0.4$ (in units of $10^{15}$ s)
- So $d/c = 1.6 \pm 0.4$ (in $10^{15}$ s)

### 2.6 Putting It All Together -- Full Table Example

**Geiger-Müller question (9702/52/O/N/21):**

| $t_1$/mm | $t_2$/mm | avg $t$/mm | $R$/s-1 | $\ln(R$/s-1) |
|----------|----------|------------|---------|---------------|
| 0.19 | 0.13 | | 47.7 | |
| 0.22 | 0.28 | | 44.0 | |

**Row 1:**
- avg $t = (0.19+0.13)/2 = 0.16$ mm
- $\Delta t = |0.19-0.13|/2 = 0.03$ mm → $0.16 \pm 0.03$
- $\ln(47.7) = 3.865$ (3 d.p. -- 47.7 has 3 s.f.)
- $\Delta(\ln R) = \frac{\Delta R}{R}$ -- but we don't have $\Delta R$ from the table. If given or assumed as 0.5: $\Delta(\ln R) = 0.5/47.7 = 0.010$

**Row 2:**
- avg $t = (0.22+0.28)/2 = 0.25$ mm
- $\Delta t = |0.22-0.28|/2 = 0.03$ mm → $0.25 \pm 0.03$
- $\ln(44.0) = 3.784$ (3 d.p.)
- $\Delta(\ln R) = 0.5/44.0 = 0.011$

Notice: $\Delta(\ln R)$ is **different** for each row (decreases as $R$ increases). So error bars will be different sizes!

### Template for Part (b) Table

Write answers in the table like this:

```
| raw1 | raw2 | processed ± uncertainty | ln(processed) ± Delta(ln) |
|------|------|------------------------|-----------------------|
| 0.19 | 0.13 | 0.16 ± 0.03            | 3.865 ± 0.010         |
```

Show one sample calculation below the table. The examiner needs to see your method for at least one row.

---

## Section 3: Part (c)(i) -- Plot the Graph (2 marks)

### Mark 1: Choosing the Scale

**Rules:**
- Your plotted points should fill **at least half** the graph grid in both directions
- Scales must be **easy to read** (1 small square = 1, 2, 5, or 0.1, 0.2, 0.5 -- NOT 3, 7, 9)
- Label each axis with the **quantity AND unit**

**Examples of good scales:**
- 1 small square = 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50
- 1 small square = 0.001, 0.002, 0.005, 0.01...

**Examples of BAD scales (DO NOT use):**
- 1 small square = 3, 6, 7, 9, 0.03, 0.07
- Reason: you can't read fractions of these easily

### Mark 2: The False Origin Trap

**The graph almost NEVER starts at (0,0).** Always check the axis labels before plotting.

**How to check the scale:**
1. Read the numbers at both ends of each axis
2. Count how many small squares between them
3. Calculate: value per small square = range ÷ number of squares
4. Write this down before plotting

**Example (Viscosity graph, 9702/52/M/J/20):**

x-axis: $1/T$ from 2.8 to 3.5 ($\times 10^{-3}$ $\text{K}^{-1}$)
y-axis: $\ln(\eta/10^{-4})$ from 2.8 to something

If there are 14 small squares between 2.8 and 3.5:
Each small square = $(3.5 - 2.8) / 14 = 0.05$

**Example (Pendulum, 9702/52/M/J/14):**

x-axis: $d$ from 0.4 to 1.8 m

If there are 14 large squares (each with 10 small squares):
Each large square = $(1.8 - 0.4) / 14 = 0.1$ m
Each small square = $0.1 / 10 = 0.01$ m (= 1 cm)

### Mark 3: Plotting Points

- Use a sharp pencil
- Small, clear crosses (not dots)
- Centre of cross must be within **half a small square** of true position
- Plot ALL points before drawing any lines

### Mark 4: Error Bars

- Draw a vertical (or horizontal) line centered on the point
- Extend **exactly** the absolute uncertainty above AND below
- Total bar length = $2 \times$ uncertainty

> **Trap:** If $\Delta y = 0.03$, the bar goes from $y-0.03$ to $y+0.03$. Total length = 0.06. The uncertainty is the **HALF-length**, not the full length.

- If all uncertainties are the same → all error bars same size
- If they vary (e.g. $\ln$ uncertainties) → each bar must be sized individually
- Draw the crossbar at the top and bottom of each error bar (small horizontal lines)

### Template for Graph

```
1. Check scale -- write value per small square on the margin
2. Label axes -- [quantity] / [unit]
3. Plot points -- sharp pencil, small crosses
4. Draw error bars -- centred on point, length = 2 x uncertainty
5. Add crossbars at top and bottom of each error bar
```

---

---

## Section 4: Part (c)(ii) -- Draw the Lines (2 marks)

### Line of Best Fit

- One single straight line (not a curve, not dot-to-dot)
- Use a transparent 30cm ruler + sharp pencil
- Extend across the **full range** of data (don't stop in the middle)
- Roughly equal number of points above and below along the length

> **Don't force through origin** unless the equation says intercept = 0.

### Worst Acceptable Line (WAL)

The WAL is the **most extreme** straight line that still passes through **all** error bars.

- Either steepest possible or shallowest possible
- Must touch every error bar (any part of it, not just the centre)
- Must be **visibly different** from the best-fit line
- **LABEL IT "WAL"** -- otherwise you lose the mark!

**How to draw it:** Place your ruler at the steepest angle where it still passes through every error bar. If the points have a positive correlation, the WAL is usually steeper. If negative, shallower.

---

## Section 5: Part (c)(iii) -- Find the Gradient (2 marks)

### The Triangle Method (Must Show)

1. Draw a **large** triangle on your best-fit line (hypotenuse >= half the line length)
2. Mark the two points you read **from the line** (circle them or write coordinates)
3. Write: $m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\Delta y}{\Delta x}$
4. State the gradient **with units**

### Getting the Uncertainty

$$\Delta m = |m_{\text{best}} - m_{\text{WAL}}|$$

- Calculate gradient of WAL using the same method
- Absolute difference is your uncertainty
- Final answer: $m = (\text{value} \pm \text{uncertainty})$ unit

### The Power-of-10 Trap (BIGGEST MARK LOSS)

**If axis labels have multipliers (like $/10^{-3}$ or $\times 10^4$), the gradient you read from the graph is NOT the physical gradient.**

**Example (Viscosity, 9702/52/M/J/20):**

x-axis: $1/T$ **/ $10^{-3}$** $\text{K}^{-1}$, y-axis: $\ln(\eta$ **/ $10^{-4}$** Pa s)

Suppose you read from graph: $\Delta y = 0.80$, $\Delta x = 0.50$ (graph units).

The x-axis is labelled $1/T$ / $10^{-3}$ $\text{K}^{-1}$, so a graph reading of $0.50$ means $0.50 \times 10^{-3}$ $\text{K}^{-1}$.

$$\Delta x_{\text{physical}} = 0.50 \times 10^{-3}\ \text{K}^{-1}$$

$$m_{\text{true}} = \frac{\Delta y}{\Delta x_{\text{physical}}} = \frac{0.80}{0.50 \times 10^{-3}} = 1.6 \times 10^{3}\ \text{K}$$

> **Rule:** $m_{\text{true}} = m_{\text{graph}} \times 10^{\text{power}}$. Always multiply by the axis power-of-ten.

---

## Section 6: Part (c)(iv) -- Find the y-intercept (2 marks)

### If y-axis starts at 0

Just read where the line crosses the y-axis. Read to the nearest small square.

### If y-axis has a false origin (ALMOST ALWAYS)

**You CANNOT read the intercept from where the line hits the edge of the graph.** You must CALCULATE it.

$$c = y_1 - m x_1$$

Pick any point $(x_1, y_1)$ on your best-fit line (not a data point), use your gradient $m$, and solve.

### Uncertainty in y-intercept

$$\Delta c = |c_{\text{best}} - c_{\text{WAL}}|$$

Use the same formula with a point on the WAL.

---

## Section 7: Part (d) -- Find Physical Constants (2-3 marks)

### The Method (Always the Same)

From part (a): Gradient = [expression], Intercept = [expression]
From parts (c)(iii) and (c)(iv): Numerical values

Set them equal and solve.

**Example (Geiger-Müller):**

From (a): gradient $= -\mu$, intercept $= \ln R_0$
From graph: $m = -0.520 \pm 0.015$, $c = 3.92 \pm 0.02$

$\mu = -m = -(-0.520) = 0.520$ mm-1
$R_0 = e^{c} = e^{3.92} = 50.4$ s-1

### If intercept involves $\ln$ or $\lg$

| If intercept = $\ln X$ | Then $X = e^{\text{intercept}}$ |
|------------------------|--------------------------------|
| If intercept = $\lg X$ | Then $X = 10^{\text{intercept}}$ |
| If intercept = $\ln k$ | Then $k = e^{\text{intercept}}$ |

**Most common mistake:** Using $10$ when it should be $e$, or vice versa. $\ln$ = natural log = $e$. $\lg$ = log base 10 = $10$.

### Uncertainty in the Constant

**If constant = gradient directly (e.g., $n = m$):**

$$\Delta n = \Delta m$$

% uncertainty in $n = \frac{\Delta m}{m} \times 100\%$

**If constant = $e^{\text{intercept}}$ (e.g., $R_0 = e^c$):**

$$\Delta R_0 = R_0 \times \Delta c$$

(This is the reverse of Rule 4: if $\Delta(\ln x) = \frac{\Delta x}{x}$, then $\Delta x = x \times \Delta(\ln x)$)

**If constant = gradient × given constant (e.g., $E = m \times k$):**

$$\frac{\Delta E}{E} = \frac{\Delta m}{m} + \frac{\Delta k}{k}$$

Add percentage uncertainties.

---

## Section 8: Part (e) -- Final Calculation (1 mark)

Use the original equation with your found constants to find one unknown value.

**Example (Geiger-Müller):** Find $t$ when $R = 20.0$ s-1.

$$R = R_0 e^{-\mu t}$$

$$t = \frac{\ln(R_0 / R)}{\mu} = \frac{\ln(50.4 / 20.0)}{0.520} = \frac{\ln(2.52)}{0.520} = \frac{0.924}{0.520} = 1.78 \text{ mm}$$

### More Part (e) Examples

**Example 2 (Circular Motion):** Find $v$ when $r = 0.500 \pm 0.005$ m.

From $Pg = mv^2/r$, with $P$ and $m$ from earlier:

$v = \sqrt{P g r / m}$

Plug in values. Show every step.

**Example 3 (Capacitor):** Find $C$ when $V = 1.20$ V.

From $V = I_0 R e^{-t/CR}$, take $\ln$:

$\ln V = \ln(I_0 R) - \frac{t}{CR}$

$C = \frac{-t}{R(\ln V - \ln(I_0 R))}$

Plug in your found $R$, $I_0$, and the given $t$, $V$.

### Template for Part (e) Answer

```
Given equation:
[original equation]

Rearrange to find [unknown]:
[algebra steps]

Substitute values:
[equation with numbers] = [answer]

Answer: [value] [unit]
```

---

## Section 9: FULL Worked Example -- Viscosity (9702/52/M/J/20)

Let's walk through the **entire** question from start to finish.

**Equation:** $\eta = He^{E/kT}$ where $k = 1.38 \times 10^{-23}$ J$\text{K}^{-1}$

**Graph:** $\ln \eta$ vs $1/T$

### Step (a): Gradient and Intercept Expressions

$$\ln \eta = \ln H + \frac{E}{k} \cdot \frac{1}{T}$$

$$\ln \eta = \left(\frac{E}{k}\right)\frac{1}{T} + \ln H$$

- **Gradient** $= E/k$
- **y-intercept** $= \ln H$

### Step (b): Data Table

| $T$/K | $\eta/10^{-4}$Pa s | $1/T / 10^{-3}$$\text{K}^{-1}$ | $\ln(\eta/10^{-4})$ |
|-------|-------------------|-------------------|---------------------|
| 292 | 12.3 ± 0.2 | 3.42 | 2.510 ± 0.016 |
| 303 | 9.8 ± 0.2 | 3.30 | 2.282 ± 0.020 |
| 311 | 8.4 ± 0.2 | 3.22 | 2.128 ± 0.024 |
| 323 | 6.8 ± 0.2 | 3.10 | 1.917 ± 0.029 |
| 335 | 5.6 ± 0.2 | 2.99 | 1.723 ± 0.036 |
| 346 | 4.8 ± 0.2 | 2.89 | 1.569 ± 0.042 |

**Calculations for Row 1:**
- $\ln(12.3) = 2.510$ (3 d.p. -- 12.3 is 3 s.f.)
- $\Delta(\ln \eta) = 0.2 / 12.3 = 0.016$

**Notice:** $\Delta(\ln \eta)$ grows as $\eta$ gets smaller (the fraction $0.2/\eta$ gets bigger). Error bars will be different sizes.

### Step (c)(i): Plot

Use the provided grid. x from 2.8 to 3.5, y from 1.5 to 2.6.
Error bars for $\ln \eta$ -- each is a different length!

### Step (c)(ii): Lines

Draw best-fit line through all error bars. Draw WAL steepest/shallowest still through all bars. **Label WAL.**

### Step (c)(iii): Gradient

**Best-fit line:** Pick two points ON the line.

Say: $(x_1, y_1) = (2.90, 1.60)$, $(x_2, y_2) = (3.40, 2.50)$

$m_{\text{best}} = \frac{2.50 - 1.60}{3.40 - 2.90} = \frac{0.90}{0.50} = 1.80$

**But wait!** x-axis has multiplier $/10^{-3}$ $\text{K}^{-1}$. So $\Delta x = 0.50 \times 10^{-3}$ $\text{K}^{-1}$.

$m_{\text{true}} = \frac{0.90}{0.50 \times 10^{-3}} = 1.80 \times 10^{3}$ K

**WAL:** Say $m_{\text{WAL}} = \frac{2.48 - 1.62}{3.38 - 2.92} = \frac{0.86}{0.46} = 1.87$ (raw)

$m_{\text{WAL, true}} = 1.87 \times 10^{3}$ K

$\Delta m = |1.80 - 1.87| \times 10^3 = 0.07 \times 10^{3}$ K

$m = (1.80 \pm 0.07) \times 10^{3}$ K

### Step (c)(iv): y-intercept

**Can't read from graph edge** (false origin). Calculate:

Pick point on best-fit line: $(2.90, 1.60)$

$c = y - mx = 1.60 - 1.80(2.90) = 1.60 - 5.22 = -3.62$

**WAL:** Pick point on WAL: $(2.92, 1.62)$

$c_{\text{WAL}} = 1.62 - 1.87(2.92) = 1.62 - 5.46 = -3.84$

$\Delta c = | -3.62 - (-3.84) | = 0.22$

$c = -3.62 \pm 0.22$

But since this is $\ln(\eta/10^{-4})$, the actual intercept value is dimensionless.

### Step (d): Find Constants

Gradient $= E/k$:

$E = m \times k = 1.80 \times 10^3 \times 1.38 \times 10^{-23} = 2.48 \times 10^{-20}$ J

Intercept $= \ln H$:

$H = e^{c} = e^{-3.62} = 0.027$ (in whatever units match the axis scaling)

**Uncertainty in $E$:**

% uncertainty in $m = \frac{0.07}{1.80} \times 100\% = 3.9\%$

If $k$ has no given uncertainty, % unc. in $E$ = 3.9%

$\Delta E = 2.48 \times 10^{-20} \times 0.039 = 0.097 \times 10^{-20}$ J

$E = (2.48 \pm 0.10) \times 10^{-20}$ J

### Step (e): Final Calculation

Find $\eta$ at $T = 273$ K.

$1/T = 1/273 = 3.663 \times 10^{-3}$ $\text{K}^{-1}$

$\ln \eta = E/k \cdot 1/T + \ln H = 1.80 \times 10^3 \times 3.663 \times 10^{-3} + (-3.62)$

$\ln \eta = 6.59 - 3.62 = 2.97$

$\eta = e^{2.97} \times 10^{-4} = 19.5 \times 10^{-4}$ Pa s

(Remember: the y-axis was $\ln(\eta/10^{-4})$, so the actual $\eta = e^{\ln\eta} \times 10^{-4}$)

---

## Section 10: All Mistakes Table -- Every Trap & How to Avoid It

| # | Mistake | Where It Happens | Why It Loses Marks | How to Avoid It |
|---|---------|-----------------|-------------------|-----------------|
| 1 | **Writing just constant name instead of full expression** | Part (a) | You write "gradient = $P$" but it's $\frac{Pg}{m}$ | Always write the full algebraic expression with all constants |
| 2 | **Wrong sign on gradient** | Part (a) | Sign is negative but you wrote positive | Check: if $y = -mx + c$, gradient = $-m$, not $m$ |
| 3 | **Confusing $\ln$ and $\lg$** | Part (d) | You use $10^c$ when it should be $e^c$ | $\ln$ → $e$, $\lg$ → $10$. Memorize: "ln = natural = e, lg = log base 10" |
| 4 | **Wrong s.f./d.p. in table** | Part (b) | $\ln(47.7)$ written as 3.9 instead of 3.865 | $\ln$ or $\lg$: **d.p.** in answer = **s.f.** in raw data |
| 5 | **Adding absolute uncertainties instead of % for products** | Part (b) | For $A \times B$: $\Delta(AB) = \Delta A + \Delta B$ (WRONG!) | Product/quotient → convert to **%**, add %, convert back |
| 6 | **Forgetting $\Delta(\ln x) = \Delta x / x$** | Part (b) | Not calculating $\ln$ uncertainty at all | $\Delta(\ln x) = \frac{\Delta x}{x}$. Write it at the top of the page! |
| 7 | **Wrong error bar length** | Part (c)(i) | Drawing total bar = $\Delta y$ instead of $2\Delta y$ | Bar goes from $y - \Delta y$ to $y + \Delta y$. Total = $2 \times \Delta y$ |
| 8 | **All error bars same size when $\ln$ uncertainties differ** | Part (c)(i) | Every $\ln$ bar is identical | Each $\Delta(\ln x) = \Delta x / x$ is different. Calculate each row! |
| 9 | **Not checking false origin** | Part (c)(i) | Plotting points at wrong position on grid | Read axis labels FIRST. Count squares. Calculate value per square |
| 10 | **Forcing line through origin** | Part (c)(ii) | Drawing best-fit line through (0,0) when data doesn't support it | Only force through origin if the equation says intercept = 0 |
| 11 | **Not labeling WAL** | Part (c)(ii) | WAL drawn but examiner can't tell which is which | Write "WAL" clearly next to the line. Use a dashed line or different colour |
| 12 | **WAL not extreme enough** | Part (c)(ii) | WAL looks almost identical to best-fit | WAL should be the **steepest/shallowest** line still through ALL error bars |
| 13 | **Small triangle for gradient** | Part (c)(iii) | Triangle uses less than half the line length | Hypotenuse must be **at least half** the drawn line's length |
| 14 | **Reading points from DATA instead of LINE** | Part (c)(iii) | Using original data points for gradient triangle | Read coordinates from the **line itself**, not from data points |
| 15 | **Power-of-10 error in gradient** | Part (c)(iii) | Axis says $/10^{-3}$ but you use raw numbers | Include axis multipliers: $m_{\text{true}} = m_{\text{graph}} \times 10^{\text{(power)}}$ |
| 16 | **No units on gradient** | Part (c)(iii) | Just writing a number without unit | Gradient always has units. Write: $m = (1.80 \pm 0.07) \times 10^3$ K |
| 17 | **Reading intercept from graph edge** | Part (c)(iv) | y-axis doesn't start at 0, you read where line hits left edge | Use $c = y_1 - m x_1$ with a point ON the line |
| 18 | **Wrong uncertainty formula for $e^c$** | Part (d) | Using $\Delta R_0 = \Delta c$ instead of $\Delta R_0 = R_0 \times \Delta c$ | $\Delta(\text{constant}) = \text{constant} \times \Delta(\ln(\text{constant}))$ |
| 19 | **Not showing working** | Any part | Just writing final answer without method | Show every algebraic step. Examiner needs to see your method |
| 20 | **Skipping part (e) -- free mark!** | Part (e) | Running out of time and not attempting it | Part (e) is **1 free mark** -- just plug numbers into the original equation |

---

## Section 11: Templates to Guarantee Marks

### Template for Part (a) -- "The Answer Format"

```
Rearranged equation:
[ln R] = ([-mu])[t] + [ln R0]
         ^gradient     ^intercept

gradient = -mu
y-intercept = ln R0
```

### Template for Part (b) -- "Table Calculation"

```
For Row 1:
  average = (t1 + t2) / 2 = (0.19 + 0.13) / 2 = 0.16
  Deltat = |t1 - t2| / 2 = |0.19 - 0.13| / 2 = 0.03
  ln(R) = ln(47.7) = 3.865    (3 d.p. because 47.7 has 3 s.f.)
  Delta(ln R) = DeltaR / R = 0.5 / 47.7 = 0.010
```

### Template for Part (c)(iii) -- "Gradient Write-up"

```
Points on line of best fit:
  (x1, y1) = (2.90, 1.60)
  (x2, y2) = (3.40, 2.50)

m(best) = (y2 - y1) / (x2 - x1)
        = (2.50 - 1.60) / (3.40 - 2.90)
        = 0.90 / 0.50
        = 1.80

With axis multiplier (/10-3):
  m(true) = 1.80 / 10-3 = 1.80 x 103 K

Points on WAL:
  (x1, y1) = (2.92, 1.62)
  (x2, y2) = (3.38, 2.48)

m(WAL) = (2.48 - 1.62) / (3.38 - 2.92) = 0.86 / 0.46 = 1.87
m(WAL, true) = 1.87 x 103 K

Deltam = |m(best) - m(WAL)| = |1.80 - 1.87| x 103 = 0.07 x 103 K

gradient = (1.80 ± 0.07) x 103 K
```

### Template for Part (c)(iv) -- "Intercept Write-up"

```
Point on best-fit line: (2.90, 1.60)
c(best) = y1 - m(best) x x1
        = 1.60 - (1.80 x 2.90)
        = 1.60 - 5.22
        = -3.62

Point on WAL: (2.92, 1.62)
c(WAL) = 1.62 - (1.87 x 2.92) = 1.62 - 5.46 = -3.84

Deltac = |c(best) - c(WAL)| = |-3.62 - (-3.84)| = 0.22

y-intercept = -3.62 ± 0.22
```

### Template for Part (d) -- "Finding Constants Write-up"

```
From (a):  gradient = E/k
From (c)(iii): gradient = 1.80 x 103 K

Therefore:  E/k = 1.80 x 103 K
            E = 1.80 x 103 x k
              = 1.80 x 103 x 1.38 x 10-23
              = 2.48 x 10-20 J

From (a):  y-intercept = ln H
From (c)(iv): y-intercept = -3.62

Therefore:  ln H = -3.62
            H = e-3.62
              = 0.027
```

---

## Section 12: Complete Answer Checklist (15/15 Guaranteed)

Go through this after you finish. Tick each box.

### Part (a) -- [ ] 
- [ ] Equation rearranged correctly into $y = mx + c$
- [ ] Gradient written as **full expression** (not just the constant)
- [ ] Intercept written as **full expression**

### Part (b) -- [ ]
- [ ] All processed values calculated for every row
- [ ] $\ln$ values have correct **d.p.** (equal to raw data **s.f.**)
- [ ] Non-log values have correct **s.f.**
- [ ] Repeated readings: average AND uncertainty both calculated
- [ ] Uncertainties calculated using the correct rule for each column
- [ ] $\Delta(\ln x) = \Delta x / x$ applied (if applicable)
- [ ] At least ONE sample calculation shown below the table

### Part (c)(i) -- [ ]
- [ ] Scale checked for **false origin**
- [ ] Value per small square calculated and noted
- [ ] All points plotted with sharp pencil, small crosses
- [ ] Error bars drawn: half-length = uncertainty (total = $2\times$ uncertainty)
- [ ] Crossbars at top and bottom of each error bar
- [ ] Different-sized error bars if $\ln$ uncertainties vary

### Part (c)(ii) -- [ ]
- [ ] Best-fit line: straight, through all points, equal above/below
- [ ] WAL drawn: steepest/shallowest through all error bars
- [ ] WAL **labelled** clearly ("WAL" written next to it)
- [ ] WAL visibly different from best-fit

### Part (c)(iii) -- [ ]
- [ ] Large triangle drawn (>= half the line length)
- [ ] Coordinates read **from the line**, not from data points
- [ ] Calculation shown: $m = \Delta y / \Delta x$
- [ ] Axis **multipliers** included in final gradient value
- [ ] **Units** stated with gradient
- [ ] WAL gradient calculated using same method
- [ ] $\Delta m = |m_{\text{best}} - m_{\text{WAL}}|$ shown
- [ ] Final answer: $m = (\text{value} \pm \text{uncertainty})$ unit

### Part (c)(iv) -- [ ]
- [ ] Intercept calculated (not read from graph edge)
- [ ] Formula shown: $c = y_1 - m x_1$
- [ ] Point used is ON the line, not a data point
- [ ] WAL intercept calculated
- [ ] $\Delta c = |c_{\text{best}} - c_{\text{WAL}}|$ shown

### Part (d) -- [ ]
- [ ] Gradient expression equated to numerical gradient
- [ ] Intercept expression equated to numerical intercept
- [ ] $\ln X$ → $X = e^{\text{value}}$ (or $\lg$ → $10^{\text{value}}$)
- [ ] **Sign handled correctly** (if $-\mu = m$, then $\mu = -m$)
- [ ] Units stated for each constant
- [ ] Uncertainty in constant calculated (if asked)

### Part (e) -- [ ]
- [ ] Original equation written
- [ ] Algebraic rearrangement shown (if needed)
- [ ] Values substituted
- [ ] Final answer given with unit

---

## Section 13: The Cheat Sheet (Everything in One Page)

### Part (a) -- 1 mark
Rearrange given equation into $y = mx + c$. Gradient = coefficient of $x$ (full expression). Intercept = rest.

### Part (b) -- 2-4 marks
- $\ln$ or $\lg$: **d.p.** in answer = **s.f.** in raw data
- Other: same **s.f.** as raw data
- Repeated readings: avg = $(t_1+t_2)/2$, $\Delta t = |t_1 - t_2|/2$
- **Uncertainty rules:**
  - Sum/difference: **add absolute** uncertainties
  - Product/quotient: **add %** uncertainties
  - Power $n$: **multiply %** uncertainty by $n$
  - $\ln x$: $\Delta(\ln x) = \Delta x / x$
  - $\lg x$: $\Delta(\lg x) = \Delta x / (x \times 2.303)$

### Part (c)(i) -- 2 marks
Check for **false origin** first. Plot with small crosses. Error bars: half-length = uncertainty.

### Part (c)(ii) -- 2 marks
Best-fit: straight line through all points. **WAL:** steepest/shallowest through all error bars. **LABEL WAL.**

### Part (c)(iii) -- 2 marks
**Large triangle** (>= half line length). Read points **from the line**. Include axis multipliers. $\Delta m = |m_{\text{best}} - m_{\text{WAL}}|$.

### Part (c)(iv) -- 2 marks
If false origin: $c = y_1 - mx_1$ (point on line, not data point). $\Delta c = |c_{\text{best}} - c_{\text{WAL}}|$.

### Part (d) -- 2-3 marks
Gradient expression = gradient value. Intercept expression = intercept value. Solve.
- $\ln X$ → $X = e^{\text{intercept}}$
- $\lg X$ → $X = 10^{\text{intercept}}$
- $-\mu = m$ → $\mu = -m$

### Part (e) -- 1 mark
Plug constants + given value into original equation. Show all steps.

---

## Section 14: Three Additional Full Worked Q2 Examples (15 marks each)

> These three complete walkthroughs cover the WS-adjacent relationships examiners love to recycle. Each follows (a)-(e) with numbers, WAL, and examiner tips.

### Example A -- Circular Motion: $Pg = mv^{2}/r$ (9702/53/O/N/15 style)

**Given:** $Pg = \frac{mv^{2}}{r}$ where $P$ is the power factor, $g = 9.81\ \text{m s}^{-2}$, $m$ is the effective mass. Graph: $v^{2}$ on y-axis, $r$ on x-axis. Data: $r$ in $\text{m}$, $t$ is time for 10 revolutions.

#### (a) Gradient & intercept

$$v^{2} = \left(\frac{Pg}{m}\right) r$$

- **Gradient** $= Pg/m$
- **y-intercept** $= 0$

> Examiner tip: Write the **full** expression $Pg/m$, not just $P$.

#### (b) Table -- process $T$, $v$, $v^{2}$ with uncertainties

$r$ known to $\pm 0.005\ \text{m}$ (steel rule), $t$ measured twice for 10 revs.

| $r$ / $\text{m}$ | $t_{1}$ / $\text{s}$ | $t_{2}$ / $\text{s}$ | $T = t/10$ / $\text{s}$ | $v = 2\pi r/T$ / $\text{m s}^{-1}$ | $v^{2}$ / $\text{m}^{2}\text{s}^{-2}$ |
|---|---|---|---|---|---|
| 0.160 | 3.4 | 3.5 | $0.345 \pm 0.005$ | $2.91 \pm 0.12$ | $8.47 \pm 0.70$ |
| 0.250 | 4.2 | 4.3 | $0.425 \pm 0.005$ | $3.70 \pm 0.10$ | $13.7 \pm 0.74$ |
| 0.340 | 4.8 | 4.9 | $0.485 \pm 0.005$ | $4.40 \pm 0.10$ | $19.4 \pm 0.88$ |
| 0.420 | 5.4 | 5.5 | $0.545 \pm 0.005$ | $4.84 \pm 0.10$ | $23.4 \pm 0.97$ |
| 0.500 | 5.9 | 6.0 | $0.595 \pm 0.005$ | $5.28 \pm 0.09$ | $27.9 \pm 0.95$ |

Sample row 1 stepped:

$$T = \frac{3.4+3.5}{2}\cdot\frac{1}{10} = 0.345\ \text{s},\quad \Delta T = \frac{|3.5-3.4|}{2}\cdot\frac{1}{10}=0.005\ \text{s}$$

$$v = \frac{2\pi(0.160)}{0.345}=2.91\ \text{m s}^{-1},\quad \frac{\Delta v}{v}= \frac{\Delta T}{T}= \frac{0.005}{0.345}=1.45\%\ \Rightarrow\ \Delta v =0.042\ \text{m s}^{-1}$$

$$v^{2}=8.47,\quad \frac{\Delta(v^{2})}{v^{2}} = 2\frac{\Delta v}{v}=2.9\%\ \Rightarrow\ \Delta(v^{2})=0.25$$

*Values above use combined $r$ + $T$ % for realism (exam: add %). Shown rounded for plotting; error bars on $v^{2}$ are **different per row** (power rule).*

#### (c)(i)-(ii) Plot

- y: $v^{2}$ $0$-$30\ \text{m}^{2}\text{s}^{-2}$, x: $r$ $0.10$-$0.55\ \text{m}$. False origin? No -- line through origin.
- Error bars: vertical only, half-length $=\Delta(v^{2})$, total $2\Delta$.
- Best-fit: straight line, equal points above/below. **WAL:** steepest line still through all bars, labelled.

#### (c)(iii) Gradient

Pick points **on the line**, large triangle $\ge \tfrac12$ line length:

Best-fit: $(r_{1},v^{2}_{1})=(0.15,7.8)$, $(r_{2},v^{2}_{2})=(0.50,27.5)$

$$m_{\text{best}} = \frac{27.5-7.8}{0.50-0.15}=\frac{19.7}{0.35}=56.3\ \text{m s}^{-2}$$

WAL: $(0.16,7.5)$, $(0.49,28.0)$

$$m_{\text{WAL}} = \frac{28.0-7.5}{0.49-0.16}=\frac{20.5}{0.33}=62.1\ \text{m s}^{-2}$$

$$\Delta m = |56.3-62.1| = 5.8\ \text{m s}^{-2}$$

$$m = (56.3 \pm 5.8)\ \text{m s}^{-2}\quad\text{(no power-of-ten trap here)}$$

> Examiner tip: Show triangle coordinates on the graph, write $\Delta y/\Delta x$ explicitly.

#### (c)(iv) Intercept

Equation predicts $c=0$. From graph:

$$c_{\text{best}} = v^{2}_{1} - m_{\text{best}} r_{1}=7.8-56.3(0.15)=-0.65$$

$$c_{\text{WAL}} =7.5-62.1(0.16)=-2.44$$

$$\Delta c = |-0.65-(-2.44)|=1.79$$

$$c = (-0.7 \pm 1.8)\ \text{m}^{2}\text{s}^{-2}\approx 0\ \text{(passes through origin within error)}$$

#### (d) Find $P$

$$m_{\text{best}} = \frac{Pg}{m}\ \Rightarrow\ P = \frac{m\,m_{\text{best}}}{g}$$

Take $m=0.120\ \text{kg}$ (given):

$$P = \frac{0.120\times 56.3}{9.81}=0.689$$

$$\frac{\Delta P}{P}=\frac{\Delta m_{\text{best}}}{m_{\text{best}}}= \frac{5.8}{56.3}=10.3\%\ \Rightarrow\ \Delta P =0.071$$

$$P = 0.69 \pm 0.07\ \text{(dimensionless power factor)}$$

#### (e) Final calculation -- $v$ at $r=0.60\ \text{m}$

$$v = \sqrt{\frac{P g r}{m}} = \sqrt{\frac{0.689\times9.81\times0.60}{0.120}} = \sqrt{33.8}=5.81\ \text{m s}^{-1}$$

> Tip: Part (e) is 1 free mark -- just substitute into the **original** equation.

---

### Example B -- Capacitor Discharge: $V = I_{0}R\,e^{-t/CR}$ (9702/52/O/N/23 style)

**Given:** $V = I_{0}R\,e^{-t/CR}$ where $t=2.0\ \text{s}$ fixed, $R$ is the resistor under test, $C$ varies via $C_{A},C_{B}$ in parallel. Graph: $\ln V$ vs $1/C$. $V$ measured $\pm0.05\ \text{V}$.

#### (a) Gradient & intercept

$$\ln V = \ln(I_{0}R) - \frac{t}{R}\cdot\frac{1}{C}$$

$$\ln V = \left(-\frac{t}{R}\right)\frac{1}{C}+ \ln(I_{0}R)$$

- **Gradient** $= -t/R$
- **y-intercept** $= \ln(I_{0}R)$

#### (b) Table

$1/C = 1/C_{A}+1/C_{B}$ (in $10^{4}\ \text{F}^{-1}$), $\ln V$ to 3 d.p. (raw $V$ 3 s.f.), $\Delta(\ln V)=\Delta V/V$.

| $C_{A}/10^{-4}\text{F}$ | $C_{B}/10^{-4}\text{F}$ | $1/C\ /10^{4}\text{F}^{-1}$ | $V$ / $\text{V}$ | $\ln(V/\text{V})$ |
|---|---|---|---|---|
| 2.2 | 2.2 | 0.909 | $2.45\pm0.05$ | $0.896\pm0.020$ |
| 2.2 | 3.3 | 0.758 | $2.75\pm0.05$ | $1.012\pm0.018$ |
| 3.3 | 3.3 | 0.606 | $3.15\pm0.05$ | $1.147\pm0.016$ |
| 2.2 | 4.7 | 0.668 | $2.95\pm0.05$ | $1.082\pm0.017$ |
| 3.3 | 4.7 | 0.516 | $3.40\pm0.05$ | $1.224\pm0.015$ |
| 4.7 | 4.7 | 0.426 | $3.75\pm0.05$ | $1.322\pm0.013$ |

Sample row 1:

$$\frac{1}{C}= \frac{1}{2.2}+\frac{1}{2.2}=0.909\times10^{4}\ \text{F}^{-1}$$

$$\ln(2.45)=0.896\ (3\text{ d.p.}),\quad \Delta(\ln V)=\frac{0.05}{2.45}=0.020$$

> Trap: If $C$ values had uncertainties, add % for $1/C$; here $C$ exact so only $V$ contributes.

#### (c)(i)-(ii) Plot

- x: $1/C$ $0.40$-$0.95\times10^{4}\ \text{F}^{-1}$ (false origin at $0.40$), y: $\ln V$ $0.85$-$1.35$.
- Error bars vertical, sizes as above (decrease as $V$ rises).
- Best-fit + WAL (steepest/shallowest through all bars).

#### (c)(iii) Gradient

Best-fit points: $(0.42,1.322)$, $(0.91,0.896)$

$$m_{\text{best}}=\frac{0.896-1.322}{0.909-0.426}\times10^{-4}=\frac{-0.426}{0.483}\times10^{-4}=-0.882\times10^{-4}\ \text{F}$$

But $1/C$ axis is in $10^{4}\ \text{F}^{-1}$, so include power:

$$\Delta x_{\text{phys}}=0.483\times10^{4}\ \text{F}^{-1},\quad m_{\text{true}}=\frac{-0.426}{0.483\times10^{4}}=-0.882\times10^{-4}\ \text{F}$$

In graph units: $m_{\text{graph}}=-0.882$, $m_{\text{true}}=-0.882\times10^{-4}\ \text{F}$.

WAL: $(0.43,1.335)$, $(0.90,0.876)$

$$m_{\text{WAL}}=\frac{0.876-1.335}{0.47\times10^{4}}=-0.977\times10^{-4}\ \text{F}$$

$$\Delta m = |-0.882-(-0.977)|\times10^{-4}=0.095\times10^{-4}\ \text{F}$$

$$m = (-0.88 \pm 0.10)\times10^{-4}\ \text{F}$$

> Power-of-ten: axis label $/10^{4}\ \text{F}^{-1}$ means true gradient is graph value $\times10^{-4}$.

#### (c)(iv) Intercept

False origin -- calculate:

$$c_{\text{best}} = y_{1} - m x_{1}=1.322 - (-0.882\times10^{-4})(0.426\times10^{4})=1.322+0.376=1.698$$

$$c_{\text{WAL}}=1.335+0.977\times10^{-4}\times0.43\times10^{4}=1.335+0.420=1.755$$

$$\Delta c = |1.698-1.755|=0.057$$

$$c = 1.70 \pm 0.06$$

#### (d) Find $R$ and $I_{0}$

$$m = -\frac{t}{R}\ \Rightarrow\ R = -\frac{t}{m}= \frac{2.0}{0.882\times10^{-4}}=2.27\times10^{4}\ \Omega$$

$$\frac{\Delta R}{R}=\frac{\Delta m}{|m|}= \frac{0.10}{0.88}=11.4\%\ \Rightarrow\ \Delta R =0.26\times10^{4}\ \Omega$$

$$R = (2.27 \pm 0.26)\times10^{4}\ \Omega$$

$$c = \ln(I_{0}R)\ \Rightarrow\ I_{0}R = e^{c}=e^{1.698}=5.46\ \text{V}$$

$$I_{0}= \frac{5.46}{2.27\times10^{4}}=2.41\times10^{-4}\ \text{A}$$

$$\Delta(I_{0}R)=I_{0}R\cdot\Delta c =5.46\times0.06=0.33\ \text{V},\quad \frac{\Delta I_{0}}{I_{0}}=\frac{\Delta(I_{0}R)}{I_{0}R}+\frac{\Delta R}{R}=6\%+11\%=17\%$$

$$I_{0}=(2.4\pm0.4)\times10^{-4}\ \text{A}$$

#### (e) Final -- predict $V$ at $C=1.5\times10^{-4}\ \text{F}$

$$\frac{1}{C}=0.667\times10^{4}\ \text{F}^{-1},\quad \ln V = m\frac{1}{C}+c = -0.882\times10^{-4}\times0.667\times10^{4}+1.698= -0.588+1.698=1.110$$

$$V = e^{1.110}=3.03\ \text{V}$$

---

### Example C -- Hubble / Redshift: $\lambda = \lambda_{0} + \lambda_{0}H\,d/c$ (9702/51/O/N/25 style)

**Given:** $\frac{\lambda-\lambda_{0}}{\lambda_{0}} = \frac{H d}{c}\ \Rightarrow\ \lambda = \lambda_{0} + \lambda_{0}H\frac{d}{c}$, $c=3.00\times10^{5}\ \text{km s}^{-1}$ exact. Graph: $\lambda$ vs $d/c$. $d$ in $10^{21}\ \text{km}$, $\lambda$ in $\text{nm}$.

#### (a) Gradient & intercept

$$\lambda = (\lambda_{0}H)\frac{d}{c} + \lambda_{0}$$

- **Gradient** $= \lambda_{0}H$
- **y-intercept** $= \lambda_{0}$

#### (b) Table

$d/c = d/(3.00\times10^{5})$ converted to $10^{15}\ \text{s}$; $\Delta(d/c)/(d/c)=\Delta d/d$.

| $d/10^{21}\text{km}$ | $d/c\ /10^{15}\text{s}$ | $\lambda$ / $\text{nm}$ |
|---|---|---|
| $0.48\pm0.12$ | $1.60\pm0.40$ | $658.4$ |
| $1.04\pm0.12$ | $3.47\pm0.40$ | $661.2$ |
| $1.60\pm0.12$ | $5.33\pm0.40$ | $664.5$ |
| $2.16\pm0.12$ | $7.20\pm0.40$ | $667.1$ |
| $2.72\pm0.12$ | $9.07\pm0.40$ | $670.3$ |
| $3.28\pm0.12$ | $10.93\pm0.40$ | $673.0$ |

Sample row 1:

$$d/c = \frac{0.48\times10^{21}}{3.00\times10^{5}}=1.60\times10^{15}\ \text{s},\quad \frac{\Delta(d/c)}{d/c}= \frac{0.12}{0.48}=25\%\ \Rightarrow\ \Delta=0.40\times10^{15}\ \text{s}$$

> No $\ln$ here -- keep $\lambda$ s.f. as given (4 s.f.), $d/c$ to 2-3 s.f. matching $d$.

#### (c)(i)-(ii) Plot

- x: $d/c$ $1.0$-$11.0\times10^{15}\ \text{s}$ (false origin $1.0$), y: $\lambda$ $657$-$674\ \text{nm}$ (false origin $657$).
- Error bars **horizontal** (uncertainty in $x$), half-length $0.40\times10^{15}\ \text{s}$.
- Best-fit + WAL (most extreme still through horizontal bars).

#### (c)(iii) Gradient

Best-fit points on line: $(2.0\times10^{15}, 659.0)$, $(10.0\times10^{15}, 672.0)$

$$m_{\text{best}}=\frac{672.0-659.0}{(10.0-2.0)\times10^{15}}=\frac{13.0}{8.0\times10^{15}}=1.625\times10^{-15}\ \text{nm s}^{-1}$$

Convert to $\text{m s}^{-1}$ if needed: $1\ \text{nm}=10^{-9}\ \text{m}\Rightarrow 1.625\times10^{-24}\ \text{m s}^{-1}$ but keep $\text{nm}$ for ratio.

WAL (shallowest through bars): $(1.6,659.5)$, $(10.9,672.5)$

$$m_{\text{WAL}}=\frac{672.5-659.5}{(10.93-1.60)\times10^{15}} \text{ using extremes} =\frac{13.0}{9.33\times10^{15}}=1.393\times10^{-15}$$

Actually choose visibly shallowest: $(2.0,659.8)$, $(10.0,671.2)$

$$m_{\text{WAL}}=\frac{671.2-659.8}{8.0\times10^{15}}=1.425\times10^{-15}\ \text{nm s}^{-1}$$

$$\Delta m =|1.625-1.425|\times10^{-15}=0.20\times10^{-15}\ \text{nm s}^{-1}$$

$$m=(1.63\pm0.20)\times10^{-15}\ \text{nm s}^{-1}$$

> Show units: $m$ has units of $\lambda/(d/c)=\text{nm}/10^{15}\text{s}$.

#### (c)(iv) Intercept

False origin -- use point $(2.0\times10^{15},659.0)$:

$$c_{\text{best}}=659.0 -1.625\times10^{-15}\times2.0\times10^{15}=659.0-3.25=655.75\ \text{nm}$$

$$c_{\text{WAL}}=659.8-1.425\times10^{-15}\times2.0\times10^{15}=659.8-2.85=656.95\ \text{nm}$$

$$\Delta c =|655.75-656.95|=1.20\ \text{nm}$$

$$c = (655.8 \pm 1.2)\ \text{nm} = \lambda_{0}$$

#### (d) Find $H$ and check $\lambda_{0}$

$$\lambda_{0}=c =655.8\pm1.2\ \text{nm}$$

$$H = \frac{m}{\lambda_{0}} = \frac{1.625\times10^{-15}\ \text{nm s}^{-1}}{655.8\ \text{nm}}=2.48\times10^{-18}\ \text{s}^{-1}$$

$$\frac{\Delta H}{H}= \frac{\Delta m}{m}+\frac{\Delta\lambda_{0}}{\lambda_{0}}= \frac{0.20}{1.63}+ \frac{1.2}{655.8}=12.3\%+0.2\%=12.5\%$$

$$\Delta H =0.31\times10^{-18}\ \text{s}^{-1}$$

$$H=(2.48\pm0.31)\times10^{-18}\ \text{s}^{-1}$$

> $H$ is the Hubble constant -- matches order $10^{-18}\ \text{s}^{-1}$.

#### (e) Final -- predict $\lambda$ for $d=4.0\times10^{21}\ \text{km}$

$$d/c = \frac{4.0\times10^{21}}{3.00\times10^{5}}=13.33\times10^{15}\ \text{s}$$

$$\lambda = \lambda_{0}+ m\,d/c =655.8 +1.625\times10^{-15}\times13.33\times10^{15}=655.8+21.66=677.5\ \text{nm}$$

$$ \lambda \approx 678\ \text{nm}$$

---

