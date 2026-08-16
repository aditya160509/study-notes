# 📘 Chapter 6: Numerical Solutions of Equations - 9709 Pure Mathematics 3 (CAIE A Level Maths)

## Cambridge International AS & A Level Mathematics (9709) - Paper 3

> **Rule + fully solved examples.** Locating roots by change of sign and sketching, then improving them with iterative formulas $x_{n+1} = F(x_n)$. 15 solved examples, 9 practice questions with full solutions, formula sheet and quick reference card at the end.

---

# 📋 Table of Contents

1. [PART 1: Finding a Starting Point - Change of Sign and Sketching](#part-1-finding-a-starting-point---change-of-sign-and-sketching)
2. [PART 2: Improving the Solution - Iterative Formulas](#part-2-improving-the-solution---iterative-formulas)
3. [PART 3: Using Iteration in Applications](#part-3-using-iteration-in-applications)
4. [Formula Sheet](#formula-sheet)
5. [Quick Reference Card](#quick-reference-card)

---

# PART 1: Finding a Starting Point - Change of Sign and Sketching

**Covers:** locating a root before any iteration begins - graphically by sketching a suitable pair of curves, and by calculation using the change of sign test.

## 1.1 The Change of Sign Test

If $f(x)$ is continuous and $f(a)$ and $f(b)$ have opposite signs, then the equation $f(x) = 0$ has at least one root between $a$ and $b$:

$$f(a) < 0 \text{ and } f(b) > 0 \quad\Rightarrow\quad \text{root } \alpha \in (a, b)$$

> ⭐ **Watch Out!** A change of sign guarantees a root for continuous functions, but the converse is FALSE: a repeated root (e.g. $(x-2)^2 = 0$) has NO sign change. Also, a discontinuity (like $\tan x$) can flip the sign without a root in between.

### Example 1 - Easy - change of sign by calculation (coursebook WE 6.2)

> **Question:** Show, by calculation, that $f(x) = x^5 + x - 1 = 0$ has a root $\alpha$ between 0 and 1.

**Solution:**

$$f(0) = 0^5 + 0 - 1 = -1$$

$$f(1) = 1^5 + 1 - 1 = 1$$

$$f(0) < 0 \text{ and } f(1) > 0 \Rightarrow \text{change of sign}$$

$$f \text{ is continuous (a polynomial), so } 0 < \alpha < 1 \quad\checkmark$$

### Example 2 - Medium - sketch, then verify by calculation (coursebook WE 6.3)

> **Question:** (a) By sketching suitable graphs, show that $\cos x = 2x - 1$ (radians) has only one root for $0 \le x \le \frac{\pi}{2}$. (b) Verify by calculation that this root lies between $x = 0.8$ and $x = 0.9$.

**Solution (a):**

Draw $y = \cos x$ and $y = 2x - 1$ on the same axes.

$$y = \cos x \text{ starts at } (0, 1) \text{ and falls to } \left(\frac{\pi}{2}, 0\right)$$

$$y = 2x - 1 \text{ is a straight line through } (0, -1) \text{ and } (0.5, 0)$$

The two graphs cross exactly once on this interval, so the equation has exactly one root.

**Solution (b):**

Let $f(x) = \cos x - 2x + 1$:

$$f(0.8) = \cos 0.8 - 2(0.8) + 1 = 0.6967 - 1.6 + 1 = 0.0967\ldots$$

$$f(0.9) = \cos 0.9 - 2(0.9) + 1 = 0.6216 - 1.8 + 1 = -0.1784\ldots$$

$$f(0.8) > 0 \text{ and } f(0.9) < 0 \Rightarrow \text{change of sign}$$

$$\text{Root lies between } 0.8 \text{ and } 0.9 \quad\checkmark$$

### Example 3 - Easy - sketching a pair of graphs (coursebook WE 6.1)

> **Question:** By sketching graphs of $y = x^3$ and $y = 4 - x$, show that $x^3 + x - 4 = 0$ has a root $\alpha$ between 1 and 2.

**Solution:**

$$y = x^3 \text{ passes through } (0,0), (1,1), (2,8)$$

$$y = 4 - x \text{ is a straight line through } (0,4) \text{ and } (4,0)$$

$$x^3 = 4 - x \text{ has one intersection point, with } 1 < x < 2$$

$$\text{At the intersection, } x^3 + x - 4 = 0, \text{ so } 1 < \alpha < 2 \quad\checkmark$$

> **What the examiner wants:** pick the two graphs so that one is a standard curve ($x^3$, $e^x$, $\cos x$, $\ln x$) and the other is a straight line. Count the intersections, then name the root.

### Practice Questions - PART 1

**Q1.** Show by calculation that $e^x - x - 6 = 0$ has a root between $x = 2.0$ and $x = 2.1$.

**Q2.** The curve $y = x^3 + 5x - 1$ cuts the $x$-axis at $(\alpha, 0)$. Show that $0.1 < \alpha < 0.5$.

**Q3.** By sketching suitable graphs, show that $x^3 + 5x^2 + 2x - 5 = 0$ has three real roots, and verify by calculation that the largest root lies between 0 and 2.

<details>
<summary><b>Full solutions</b></summary>

**Q1 Solution:**

Let $f(x) = e^x - x - 6$:

$$f(2.0) = e^2 - 2.0 - 6 = 7.389 - 8 = -0.611$$

$$f(2.1) = e^{2.1} - 2.1 - 6 = 8.166 - 8.1 = 0.0662$$

$$f(2.0) < 0 \text{ and } f(2.1) > 0 \Rightarrow \text{root between } 2.0 \text{ and } 2.1 \quad\checkmark$$

**Q2 Solution:**

Let $f(x) = x^3 + 5x - 1$:

$$f(0.1) = 0.001 + 0.5 - 1 = -0.499$$

$$f(0.5) = 0.125 + 2.5 - 1 = 1.625$$

$$f(0.1) < 0 \text{ and } f(0.5) > 0 \Rightarrow 0.1 < \alpha < 0.5 \quad\checkmark$$

**Q3 Solution:**

$$y = x^3 + 5x^2 \text{ and } y = 5 - 2x \text{ intersect three times}$$

(The cubic $y = x^3 + 5x^2 = x^2(x+5)$ crosses the $x$-axis at $x = -5$ and $x = 0$ with a turning point between, and the falling line $y = 5 - 2x$ cuts it three times.)

$$\text{So } x^3 + 5x^2 + 2x - 5 = 0 \text{ has three real roots}$$

Let $f(x) = x^3 + 5x^2 + 2x - 5$:

$$f(0) = -5 \quad\text{and}\quad f(2) = 8 + 20 + 4 - 5 = 27$$

$$f(0) < 0 \text{ and } f(2) > 0 \Rightarrow \text{largest root between } 0 \text{ and } 2 \quad\checkmark$$

</details>

---

# PART 2: Improving the Solution - Iterative Formulas

**Covers:** rearranging $f(x) = 0$ into $x = F(x)$, generating the sequence $x_{n+1} = F(x_n)$, and proving the final answer with a change of sign test.

## 2.1 The Iterative Formula $x_{n+1} = F(x_n)$

Rearranged form and iteration:

$$f(x) = 0 \;\Rightarrow\; x = F(x) \qquad x_{n+1} = F(x_n)$$

Each application of the formula is one iteration. If the sequence converges, it converges to a value $\alpha$ satisfying $\alpha = F(\alpha)$, which is a root of $f(x) = 0$.

> ⭐ **Watch Out!** The rearrangement you choose matters. Different rearrangements of the SAME equation can converge, converge slowly, or diverge. The success depends on both $F$ and the starting value $x_1$.

### Example 4 - Easy - iteration from a rearrangement (coursebook section 6.2)

> **Question:** $x^5 + x - 1 = 0$ has a root $\alpha$ between 0 and 1. Rearrange as $x = \sqrt[5]{1-x}$ and iterate from $x_1 = 0.5$ until $x_n$ and $F(x_n)$ agree to 1 significant figure.

**Solution:**

$$x^5 + x - 1 = 0 \Rightarrow x^5 = 1 - x \Rightarrow x = \sqrt[5]{1-x}$$

$$x_1 = 0.5$$

$$x_2 = \sqrt[5]{1 - 0.5} = \sqrt[5]{0.5} = 0.8706$$

$$x_3 = \sqrt[5]{1 - 0.8706} = \sqrt[5]{0.1294} = 0.6644$$

$$x_4 = \sqrt[5]{1 - 0.6644} = \sqrt[5]{0.3356} = 0.8038$$

$$x_5 = \sqrt[5]{1 - 0.8038} = \sqrt[5]{0.1962} = 0.7220$$

$$x_6 = \sqrt[5]{1 - 0.7220} = \sqrt[5]{0.2780} = 0.7741$$

$$x_7 = \sqrt[5]{1 - 0.7741} = \sqrt[5]{0.2259} = 0.7426$$

$$x_8 = \sqrt[5]{1 - 0.7426} = \sqrt[5]{0.2574} = 0.7623$$

$$x_9 = \sqrt[5]{1 - 0.7623} = \sqrt[5]{0.2377} = 0.7503$$

$$x_{10} = \sqrt[5]{1 - 0.7503} = \sqrt[5]{0.2497} = 0.7577$$

$$x_9 = 0.7503 \text{ and } x_{10} = 0.7577 \text{ both round to } 0.8 \text{ (1 s.f.)} \Rightarrow \alpha \approx 0.8 \quad\checkmark$$

> **What the examiner wants:** write each iteration on its own line, compare successive values, and state the accuracy you have reached. A calculator with an Ans key makes this fast.

### Example 5 - Medium - negative root to 2 d.p. with proof (coursebook WE 6.4)

> **Question:** $x^2 + x - 3 = 0$ has a negative root $\alpha$. (a) Show it can be rearranged as $x = \frac{3}{x} - 1$. (b) Use $x_{n+1} = \frac{3}{x_n} - 1$ with $x_1 = -2.5$ to find $\alpha$ correct to 2 decimal places, then prove it.

**Solution (a):**

$$x^2 + x - 3 = 0$$

Divide through by $x$ (valid since $x \ne 0$ for this root):

$$\frac{x^2}{x} + \frac{x}{x} - \frac{3}{x} = 0$$

$$x + 1 - \frac{3}{x} = 0$$

Isolate $x$:

$$x = \frac{3}{x} - 1 \quad\checkmark$$

**Solution (b):**

$$x_1 = -2.5$$

$$x_2 = \frac{3}{-2.5} - 1 = -2.2$$

$$x_3 = \frac{3}{-2.2} - 1 = -2.3636$$

$$x_4 = \frac{3}{-2.3636} - 1 = -2.2692$$

$$x_5 = \frac{3}{-2.2692} - 1 = -2.3220$$

$$x_6 = \frac{3}{-2.3220} - 1 = -2.2920$$

$$x_7 = \frac{3}{-2.2920} - 1 = -2.3089$$

$$x_8 = \frac{3}{-2.3089} - 1 = -2.2993$$

$$x_9 = \frac{3}{-2.2993} - 1 = -2.3047$$

$$x_8 \text{ and } x_9 \text{ both round to } -2.30 \text{ (2 d.p.)}$$

Proof with change of sign. If $\alpha = -2.30$ to 2 d.p., then $-2.305 < \alpha < -2.295$:

$$f(-2.305) = (-2.305)^2 + (-2.305) - 3 = 5.3130 - 5.305 = 0.00802\ldots$$

$$f(-2.295) = (-2.295)^2 + (-2.295) - 3 = 5.2670 - 5.295 = -0.0279\ldots$$

$$f(-2.305) > 0 \text{ and } f(-2.295) < 0 \Rightarrow \text{change of sign}$$

$$\alpha = -2.30 \text{ correct to 2 decimal places} \quad\checkmark$$

### Example 6 - Medium - root to 3 s.f. with proof (coursebook WE 6.5)

> **Question:** $e^x - 1 = 2x$ has a root $\alpha = 0$ and another root $\beta$. (a) Show $1 < \beta < 2$. (b) Show the equation rearranges to $x = \ln(2x + 1)$. (c) Iterate from $x_1 = 1.5$ to find $\beta$ correct to 3 significant figures.

**Solution (a):**

$$f(x) = e^x - 1 - 2x$$

$$f(1) = e^1 - 1 - 2 = 2.7183 - 3 = -0.2817\ldots$$

$$f(2) = e^2 - 1 - 4 = 7.3891 - 5 = 2.3891\ldots$$

$$f(1) < 0 \text{ and } f(2) > 0 \Rightarrow 1 < \beta < 2 \quad\checkmark$$

**Solution (b):**

$$e^x - 1 = 2x$$

Isolate $e^x$:

$$e^x = 2x + 1$$

Take natural logs:

$$x = \ln(2x + 1) \quad\checkmark$$

**Solution (c):**

$$x_1 = 1.5$$

$$x_2 = \ln(2 \times 1.5 + 1) = \ln 4 = 1.3863$$

$$x_3 = \ln(2 \times 1.3863 + 1) = \ln 3.7726 = 1.3278$$

$$x_4 = \ln(2 \times 1.3278 + 1) = \ln 3.6556 = 1.2962$$

$$x_5 = \ln(2 \times 1.2962 + 1) = \ln 3.5924 = 1.2788$$

$$x_6 = \ln(2 \times 1.2788 + 1) = \ln 3.5576 = 1.2691$$

$$x_7 = \ln(2 \times 1.2691 + 1) = \ln 3.5382 = 1.2636$$

$$x_8 = \ln(2 \times 1.2636 + 1) = \ln 3.5272 = 1.2605$$

$$x_7 \text{ and } x_8 \text{ both round to } 1.26 \text{ (3 s.f.)}$$

Proof. If $\beta = 1.26$ to 3 s.f., then $1.255 < \beta < 1.265$:

$$f(1.255) = e^{1.255} - 1 - 2(1.255) = 3.5079 - 3.51 = -0.00216\ldots$$

$$f(1.265) = e^{1.265} - 1 - 2(1.265) = 3.5431 - 3.53 = 0.01309\ldots$$

$$f(1.255) < 0 \text{ and } f(1.265) > 0 \Rightarrow \text{change of sign}$$

$$\beta = 1.26 \text{ correct to 3 significant figures} \quad\checkmark$$

> **What the examiner wants:** the change of sign test on the ORIGINAL $f(x)$, using the exact rounding boundaries (e.g. $\pm 0.005$ for 2 d.p., $\pm 0.005$ around the 3 s.f. truncation). This converts a "seems to be" into a proof.

## 2.2 Convergence, Cobwebs and Choosing the Right Rearrangement

- **Cobweb pattern:** $x_{n+1}$ alternates around $\alpha$, the values spiral in towards the intersection of $y = x$ and $y = F(x)$ (Example 4 above).
- **Staircase pattern:** the values approach $\alpha$ monotonically from one side (Example 6 above).
- A rearrangement fails when $|F'(x)| > 1$ near the root, or when $x_1$ is outside the basin of convergence.

### Example 7 - Hard - one rearrangement fails, another converges (coursebook Ex 6B Q8)

> **Question:** $\cosec x = x^2$ has a root $\alpha$ between 1 and 2. (a) Write down iterative formulas from $x = \sin^{-1}\!\left(\frac{1}{x^2}\right)$ and $x = \frac{1}{\sqrt{\sin x}}$. (b) Show the first fails to converge from $x_1 = 1.5$. (c) Use the second to find $\alpha$ correct to 3 decimal places.

**Solution (a):**

$$\text{Formula A: } x_{n+1} = \sin^{-1}\!\left(\frac{1}{x_n^2}\right)$$

$$\text{Formula B: } x_{n+1} = \frac{1}{\sqrt{\sin x_n}}$$

**Solution (b) - formula A fails:**

$$x_1 = 1.5$$

$$x_2 = \sin^{-1}\!\left(\frac{1}{1.5^2}\right) = \sin^{-1}(0.4444) = 0.4606$$

$$x_3 = \sin^{-1}\!\left(\frac{1}{0.4606^2}\right) = \sin^{-1}(4.713) \text{ is undefined}$$

$\sin^{-1}$ only accepts inputs in $[-1, 1]$, so the iteration breaks down. Formula A fails.

**Solution (c) - formula B converges:**

$$x_1 = 1.5$$

$$x_2 = \frac{1}{\sqrt{\sin 1.5}} = \frac{1}{\sqrt{0.9975}} = 1.0013$$

$$x_3 = \frac{1}{\sqrt{\sin 1.0013}} = \frac{1}{\sqrt{0.8415}} = 1.0897$$

$$x_4 = \frac{1}{\sqrt{\sin 1.0897}} = \frac{1}{\sqrt{0.8863}} = 1.0621$$

$$x_5 = \frac{1}{\sqrt{\sin 1.0621}} = \frac{1}{\sqrt{0.8753}} = 1.0700$$

$$x_6 = \frac{1}{\sqrt{\sin 1.0700}} = \frac{1}{\sqrt{0.8770}} = 1.0677$$

$$x_7 = \frac{1}{\sqrt{\sin 1.0677}} = \frac{1}{\sqrt{0.8764}} = 1.0684$$

$$x_8 = \frac{1}{\sqrt{\sin 1.0684}} = \frac{1}{\sqrt{0.8766}} = 1.0682$$

$$x_7 \text{ and } x_8 \text{ both round to } 1.068 \text{ (3 d.p.)}$$

$$\alpha = 1.068 \text{ correct to 3 decimal places} \quad\checkmark$$

> **What the examiner wants:** if the question says "one formula fails", run it and show exactly where it breaks (undefined value, oscillation, or divergence). Then switch to the convergent rearrangement.

### Practice Questions - PART 2

**Q1.** The equation $\ln(x+1) + 2x - 4 = 0$ has a root $\alpha$ between $x = 1$ and $x = 2$. Use $x_{n+1} = \frac{4 - \ln(x_n + 1)}{2}$ with $x_1 = 1.5$ to find $\alpha$ correct to 3 decimal places.

**Q2.** The sequence defined by $x_{n+1} = \frac{1}{7}\left(6x_n + \frac{3}{x_n^3}\right)$ with $x_1 = 1.5$ converges to $\alpha$. (a) Find $\alpha$ correct to 2 decimal places. (b) State an equation satisfied by $\alpha$ and hence find its exact value. (Coursebook review exercise Q1)

**Q3.** The equation $x = \cos x + \sin x$ has a root $\alpha$ between 1 and 1.4. (a) Show $\alpha$ is also a root of $x = \sqrt{2}\cos\!\left(x - \frac{\pi}{4}\right)$. (b) Iterate from $x_1 = 1.2$ to find $\alpha$ correct to 2 decimal places.

<details>
<summary><b>Full solutions</b></summary>

**Q1 Solution:**

$$x_1 = 1.5$$

$$x_2 = \frac{4 - \ln(1.5 + 1)}{2} = \frac{4 - 0.9163}{2} = 1.5419$$

$$x_3 = \frac{4 - \ln(1.5419 + 1)}{2} = \frac{4 - 0.9329}{2} = 1.5336$$

$$x_4 = \frac{4 - \ln(1.5336 + 1)}{2} = \frac{4 - 0.9298}{2} = 1.5351$$

$$x_5 = \frac{4 - \ln(1.5351 + 1)}{2} = \frac{4 - 0.9302}{2} = 1.5349$$

$$x_6 = \frac{4 - \ln(1.5349 + 1)}{2} = \frac{4 - 0.9301}{2} = 1.5349$$

$$x_5 \text{ and } x_6 \text{ both round to } 1.535 \text{ (3 d.p.)}$$

$$\alpha = 1.535 \text{ correct to 3 decimal places} \quad\checkmark$$

**Q2 Solution (a):**

The formula rearranges $7x = 6x + \frac{3}{x^3}$, i.e. $x^4 = 3$, so the iteration converges to $\sqrt[4]{3} \approx 1.3161$:

$$x_1 = 1.5$$

$$x_2 = \frac{6(1.5) + \frac{3}{1.5^3}}{7} = \frac{9 + 0.8889}{7} = 1.4127$$

$$x_3 = \frac{6(1.4127) + \frac{3}{1.4127^3}}{7} = \frac{8.4762 + 1.0643}{7} = 1.3629$$

$$x_4 = \frac{6(1.3629) + \frac{3}{1.3629^3}}{7} = \frac{8.1774 + 1.1848}{7} = 1.3375$$

$$x_5 = \frac{6(1.3375) + \frac{3}{1.3375^3}}{7} = \frac{8.0250 + 1.2540}{7} = 1.3256$$

$$x_6 = \frac{6(1.3256) + \frac{3}{1.3256^3}}{7} = \frac{7.9536 + 1.2871}{7} = 1.3201$$

$$x_7 = \frac{6(1.3201) + \frac{3}{1.3201^3}}{7} = \frac{7.9206 + 1.3044}{7} = 1.3179$$

$$x_8 = \frac{6(1.3179) + \frac{3}{1.3179^3}}{7} = \frac{7.9074 + 1.3101}{7} = 1.3168$$

$$x_9 = \frac{6(1.3168) + \frac{3}{1.3168^3}}{7} = \frac{7.9008 + 1.3136}{7} = 1.3163$$

$$x_8 \text{ and } x_9 \text{ both round to } 1.32 \text{ (2 d.p.)}$$

$$\alpha = 1.32 \text{ correct to 2 decimal places}$$

(b) At the limit $x_{n+1} = x_n = \alpha$:

$$\alpha = \frac{6\alpha + \frac{3}{\alpha^3}}{7}$$

$$7\alpha = 6\alpha + \frac{3}{\alpha^3}$$

$$\alpha = \frac{3}{\alpha^3}$$

$$\alpha^4 = 3$$

$$\alpha = \sqrt[4]{3} \quad\checkmark$$

**Q3 Solution (a):**

$$\cos x + \sin x = \sqrt{2}\left(\frac{1}{\sqrt{2}}\cos x + \frac{1}{\sqrt{2}}\sin x\right)$$

$$\cos x + \sin x = \sqrt{2}\left(\cos x \cos\frac{\pi}{4} + \sin x \sin\frac{\pi}{4}\right)$$

$$\cos x + \sin x = \sqrt{2}\cos\left(x - \frac{\pi}{4}\right) \quad\checkmark$$

So $x = \cos x + \sin x$ becomes $x = \sqrt{2}\cos\left(x - \frac{\pi}{4}\right)$.

**Q3 Solution (b):**

$$x_1 = 1.2$$

$$x_2 = \sqrt{2}\cos\left(1.2 - \frac{\pi}{4}\right) = \sqrt{2}\cos(0.4146) = 1.2946$$

$$x_3 = \sqrt{2}\cos(1.2946 - 0.7854) = \sqrt{2}\cos(0.5092) = 1.2355$$

$$x_4 = \sqrt{2}\cos(1.2355 - 0.7854) = \sqrt{2}\cos(0.4501) = 1.2737$$

$$x_5 = \sqrt{2}\cos(1.2737 - 0.7854) = \sqrt{2}\cos(0.4883) = 1.2491$$

$$x_6 = \sqrt{2}\cos(1.2491 - 0.7854) = \sqrt{2}\cos(0.4637) = 1.2652$$

$$x_7 = \sqrt{2}\cos(1.2652 - 0.7854) = \sqrt{2}\cos(0.4798) = 1.2548$$

$$x_8 = \sqrt{2}\cos(1.2548 - 0.7854) = \sqrt{2}\cos(0.4694) = 1.2613$$

$$x_9 = \sqrt{2}\cos(1.2613 - 0.7854) = \sqrt{2}\cos(0.4759) = 1.2577$$

$$x_8 \text{ and } x_9 \text{ both round to } 1.26 \text{ (2 d.p.)}$$

$$\alpha = 1.26 \text{ correct to 2 decimal places} \quad\checkmark$$

</details>

---

# PART 3: Using Iteration in Applications

**Covers:** feeding iteration into stationary points, geometry problems and other areas of mathematics - the setup is usually the hard part, the iteration is mechanical.

## 3.1 Stationary Points from Iteration

For a curve given by $y = f(x)$, a stationary point satisfies $\frac{\mathrm{d}y}{\mathrm{d}x} = 0$. Rearranged into $x = F(x)$, this becomes an iteration problem.

### Example 8 - Medium - stationary point of a parametric curve (coursebook Ex 6C Q2)

> **Question:** The curve $x = t^2 + 6$, $y = t^4 - t^3 - 5t$ has a stationary point for $1 < t < 2$. (a) Show $t$ satisfies $t = \sqrt[3]{\frac{3t^2 + 5}{4}}$. (b) Iterate from $t_1 = 1.5$ to find $t$ correct to 3 decimal places. (c) Find the coordinates of the stationary point to 1 significant figure.

**Solution (a):**

$$\frac{\mathrm{d}x}{\mathrm{d}t} = 2t$$

$$\frac{\mathrm{d}y}{\mathrm{d}t} = 4t^3 - 3t^2 - 5$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{4t^3 - 3t^2 - 5}{2t}$$

Stationary point $\Rightarrow \frac{\mathrm{d}y}{\mathrm{d}x} = 0$:

$$4t^3 - 3t^2 - 5 = 0$$

$$4t^3 = 3t^2 + 5$$

$$t^3 = \frac{3t^2 + 5}{4}$$

$$t = \sqrt[3]{\frac{3t^2 + 5}{4}} \quad\checkmark$$

**Solution (b):**

$$t_1 = 1.5$$

$$t_2 = \sqrt[3]{\frac{3(1.5)^2 + 5}{4}} = \sqrt[3]{\frac{11.75}{4}} = \sqrt[3]{2.9375} = 1.4322$$

$$t_3 = \sqrt[3]{\frac{3(1.4322)^2 + 5}{4}} = \sqrt[3]{\frac{11.1537}{4}} = \sqrt[3]{2.7884} = 1.4075$$

$$t_4 = \sqrt[3]{\frac{3(1.4075)^2 + 5}{4}} = \sqrt[3]{\frac{10.9432}{4}} = \sqrt[3]{2.7358} = 1.3986$$

$$t_5 = \sqrt[3]{\frac{3(1.3986)^2 + 5}{4}} = \sqrt[3]{\frac{10.8683}{4}} = \sqrt[3]{2.7171} = 1.3954$$

$$t_6 = \sqrt[3]{\frac{3(1.3954)^2 + 5}{4}} = \sqrt[3]{\frac{10.8454}{4}} = \sqrt[3]{2.7114} = 1.3943$$

$$t_7 = \sqrt[3]{\frac{3(1.3943)^2 + 5}{4}} = \sqrt[3]{\frac{10.8362}{4}} = \sqrt[3]{2.7091} = 1.3938$$

$$t_8 = \sqrt[3]{\frac{3(1.3938)^2 + 5}{4}} = \sqrt[3]{\frac{10.8320}{4}} = \sqrt[3]{2.7080} = 1.3936$$

$$t = 1.394 \text{ correct to 3 decimal places}$$

**Solution (c):**

$$x = t^2 + 6 = 1.3936^2 + 6 = 1.9422 + 6 = 7.94$$

$$y = t^4 - t^3 - 5t = 3.7723 - 2.7069 - 6.968 = -5.90$$

$$\text{Stationary point } (8, -6) \text{ to 1 significant figure} \quad\checkmark$$

## 3.2 Geometry Problems

### Example 9 - Medium - circle geometry to 3 s.f. (coursebook WE 6.7)

> **Question:** In a company logo, $AB$ is an arc of a circle with centre $C$. The area of the unshaded segment equals the area of the shaded triangle. Angle $ACB = \theta$ radians. (a) Show $\theta = 2\sin\theta$. (b) Iterate $\theta_{n+1} = 2\sin\theta_n$ from $\theta_1 = 1.85$ to find $\theta$ correct to 3 significant figures. (c) Find the length of $AB$ given $AC = 8$ cm.

**Solution (a):**

$$\text{Area of triangle } = \frac{1}{2}r^2\sin\theta$$

$$\text{Area of segment } = \frac{1}{2}r^2\theta - \frac{1}{2}r^2\sin\theta$$

Areas are equal:

$$\frac{1}{2}r^2\sin\theta = \frac{1}{2}r^2(\theta - \sin\theta)$$

Divide through by $\frac{1}{2}r^2$:

$$\sin\theta = \theta - \sin\theta$$

$$\theta = 2\sin\theta \quad\checkmark$$

**Solution (b):**

$$\theta_1 = 1.85$$

$$\theta_2 = 2\sin 1.85 = 2(0.96128) = 1.9226$$

$$\theta_3 = 2\sin 1.9226 = 2(0.93877) = 1.8775$$

$$\theta_4 = 2\sin 1.8775 = 2(0.95332) = 1.9066$$

$$\theta_5 = 2\sin 1.9066 = 2(0.94413) = 1.8883$$

$$\theta_6 = 2\sin 1.8883 = 2(0.95003) = 1.9001$$

$$\theta_7 = 2\sin 1.9001 = 2(0.94628) = 1.8926$$

$$\theta_8 = 2\sin 1.8926 = 2(0.94868) = 1.8974$$

$$\theta_9 = 2\sin 1.8974 = 2(0.94715) = 1.8943$$

$$\theta_{10} = 2\sin 1.8943 = 2(0.94812) = 1.8963$$

$$\theta_{11} = 2\sin 1.8963 = 2(0.94750) = 1.8950$$

$$\theta_{10} \text{ and } \theta_{11} \text{ both round to } 1.90 \text{ (3 s.f.)}$$

Proof with $f(\theta) = \theta - 2\sin\theta$:

$$f(1.895) = 1.895 - 2\sin 1.895 = 1.895 - 1.8958 = -0.000809\ldots$$

$$f(1.905) = 1.905 - 2\sin 1.905 = 1.905 - 1.8893 = 0.01566\ldots$$

$$f(1.895) < 0 \text{ and } f(1.905) > 0 \Rightarrow \text{change of sign}$$

$$\theta = 1.90 \text{ correct to 3 significant figures}$$

**Solution (c):**

$AC = 8$ cm and $\angle ACB = \theta$. The triangle $ACB$ is isosceles, so half of $AB$ sits opposite half the angle:

$$\sin\frac{\theta}{2} = \frac{\frac{1}{2}AB}{8}$$

$$\sin(0.95) = \frac{AB}{16}$$

$$AB = 16\sin(0.95) = 16(0.81342) = 13.01$$

$$AB = 13 \text{ cm (correct to 2 significant figures)} \quad\checkmark$$

## 3.3 Other Areas of Mathematics

### Example 10 - Easy - the golden ratio (coursebook Explore 6.3)

> **Question:** The golden ratio $\varphi$ satisfies $\frac{\varphi - 1}{1} = \frac{1}{\varphi}$. Use an iterative formula with starting value 1 to find $\varphi$ correct to 5 significant figures.

**Solution:**

$$\frac{\varphi - 1}{1} = \frac{1}{\varphi}$$

$$\varphi^2 - \varphi = 1$$

$$\varphi^2 = \varphi + 1$$

$$\varphi = 1 + \frac{1}{\varphi} \quad (\text{dividing by } \varphi)$$

Iterate $\varphi_{n+1} = 1 + \frac{1}{\varphi_n}$ from $\varphi_1 = 1$:

$$\varphi_2 = 1 + \frac{1}{1} = 2$$

$$\varphi_3 = 1 + \frac{1}{2} = 1.5$$

$$\varphi_4 = 1 + \frac{1}{1.5} = 1.6667$$

$$\varphi_5 = 1 + \frac{1}{1.6667} = 1.6$$

$$\varphi_6 = 1 + \frac{1}{1.6} = 1.625$$

$$\varphi_7 = 1 + \frac{1}{1.625} = 1.6154$$

$$\varphi_8 = 1 + \frac{1}{1.6154} = 1.6190$$

$$\varphi_9 = 1 + \frac{1}{1.6190} = 1.6176$$

$$\varphi_{10} = 1 + \frac{1}{1.6176} = 1.6182$$

$$\varphi_{11} = 1 + \frac{1}{1.6182} = 1.6180$$

$$\varphi_{12} = 1 + \frac{1}{1.6180} = 1.6180$$

$$\varphi = 1.6180 \text{ correct to 5 significant figures} \quad\checkmark$$

> **What the examiner wants:** in application questions, most marks come from deriving the equation. Do the geometry/calculus set-up carefully, then show the iteration table clearly and finish with the change of sign proof.

### Practice Questions - PART 3

**Q1.** A curve has equation $y = \frac{e^{2x} + x}{x^3}$ and a stationary point with $x$-coordinate between 1 and 2. (a) Show that the $x$-coordinate satisfies $2xe^{2x} - 3e^{2x} - 2x = 0$. (b) Rearrange to $x = \frac{3}{2} + xe^{-2x}$ and iterate from $x_1 = 1.5$ to find the $x$-coordinate correct to 2 decimal places.

**Q2.** In the diagram, triangle $ABC$ is right-angled with angle $BAC = \theta$ radians. Point $O$ is the midpoint of $AC$, $OC = r$, angle $BOC = 2\theta$, and $BOC$ is a sector of the circle centred at $O$. The area of triangle $ABC$ is twice the area of the shaded segment. (a) Show that $\theta$ satisfies $\sin 2\theta = \theta$. (b) Use $\theta_{n+1} = \sin 2\theta_n$ to find the root correct to 2 decimal places, giving iterations to 4 decimal places.

**Q3.** The functions $f(x) = e^{x-2}$ and $g(x) = 5 - \cos x$ have equal gradients when $x = p$ and when $x = q$, with $p < q$. Show that $q$ satisfies $q = 2 + \ln(\sin q)$, and use $q_{n+1} = 2 + \ln(\sin q_n)$ with $q_1 = 2$ to find $q$ correct to 2 decimal places.

<details>
<summary><b>Full solutions</b></summary>

**Q1 Solution (a):**

$$y = \frac{e^{2x} + x}{x^3} = e^{2x}x^{-3} + x^{-2}$$

$$\frac{\mathrm{d}y}{\mathrm{d}x} = 2e^{2x}x^{-3} - 3e^{2x}x^{-4} - 2x^{-3}$$

Multiply by $x^4$:

$$\frac{\mathrm{d}y}{\mathrm{d}x} = 0 \Rightarrow 2xe^{2x} - 3e^{2x} - 2x = 0$$

**Q1 Solution (b):**

From $2xe^{2x} - 3e^{2x} = 2x$:

$$e^{2x}(2x - 3) = 2x$$

$$2x - 3 = 2xe^{-2x}$$

$$2x = 3 + 2xe^{-2x}$$

$$x = \frac{3}{2} + xe^{-2x}$$

Iterate $x_{n+1} = \frac{3}{2} + x_ne^{-2x_n}$ from $x_1 = 1.5$:

$$x_2 = 1.5 + 1.5e^{-3} = 1.5 + 0.0747 = 1.5747$$

$$x_3 = 1.5 + 1.5747e^{-3.1494} = 1.5 + 1.5747(0.0429) = 1.5676$$

$$x_4 = 1.5 + 1.5676e^{-3.1352} = 1.5 + 1.5676(0.0434) = 1.5680$$

$$x_5 = 1.5 + 1.5680e^{-3.1360} = 1.5 + 1.5680(0.0434) = 1.5680$$

$$x_4 \text{ and } x_5 \text{ both round to } 1.57 \text{ (2 d.p.)}$$

$$x\text{-coordinate } = 1.57 \text{ correct to 2 decimal places} \quad\checkmark$$

**Q2 Solution (a):**

Since $O$ is the midpoint of the hypotenuse $AC$ of the right-angled triangle $ABC$, $O$ is the circumcentre: $OA = OB = OC = r$.

$$\text{Area of } \triangle ABC = \frac{1}{2} \cdot AB \cdot BC$$

$$AB = AC\cos\theta = 2r\cos\theta$$

$$\text{Area of } \triangle ABC = \frac{1}{2}(2r\cos\theta)(2r\sin\theta) = 2r^2\sin\theta\cos\theta = r^2\sin 2\theta$$

$$\text{Area of segment } = \frac{1}{2}r^2(2\theta) - \frac{1}{2}r^2\sin 2\theta$$

Given: triangle area $= 2 \times$ segment area:

$$r^2\sin 2\theta = 2\left(r^2\theta - \frac{1}{2}r^2\sin 2\theta\right)$$

$$\sin 2\theta = 2\theta - \sin 2\theta$$

$$2\sin 2\theta = 2\theta$$

$$\sin 2\theta = \theta \quad\checkmark$$

**Q2 Solution (b):**

$$\theta_1 = 0.9$$

$$\theta_2 = \sin(1.8) = 0.9738$$

$$\theta_3 = \sin(1.9476) = 0.9298$$

$$\theta_4 = \sin(1.8596) = 0.9586$$

$$\theta_5 = \sin(1.9172) = 0.9406$$

$$\theta_6 = \sin(1.8812) = 0.9522$$

$$\theta_7 = \sin(1.9044) = 0.9449$$

$$\theta_8 = \sin(1.8898) = 0.9495$$

$$\theta_9 = \sin(1.8990) = 0.9466$$

$$\theta_{10} = \sin(1.8932) = 0.9485$$

$$\theta_{11} = \sin(1.8970) = 0.9473$$

$$\theta_{12} = \sin(1.8946) = 0.9480$$

$$\theta_{13} = \sin(1.8960) = 0.9476$$

$$\theta_{14} = \sin(1.8952) = 0.9478$$

$$\theta_{15} = \sin(1.8956) = 0.9477$$

$$\theta_{16} = \sin(1.8954) = 0.9478$$

$$\theta_{14} \text{ and } \theta_{15} \text{ both round to } 0.95 \text{ (2 d.p.)}$$

$$\theta = 0.95 \text{ correct to 2 decimal places} \quad\checkmark$$

**Q3 Solution:**

$$f'(x) = e^{x-2}, \quad g'(x) = \sin x$$

Equal gradients:

$$e^{x-2} = \sin x$$

Take logs (valid where $\sin x > 0$, which includes the root at $x = q$):

$$x - 2 = \ln(\sin x)$$

$$x = 2 + \ln(\sin x) \quad\checkmark$$

So $q$ satisfies $q = 2 + \ln(\sin q)$.

Iterate $q_{n+1} = 2 + \ln(\sin q_n)$ from $q_1 = 2$:

$$q_2 = 2 + \ln(\sin 2) = 2 + \ln(0.9093) = 1.9049$$

$$q_3 = 2 + \ln(\sin 1.9049) = 2 + \ln(0.9447) = 1.9431$$

$$q_4 = 2 + \ln(\sin 1.9431) = 2 + \ln(0.9315) = 1.9290$$

$$q_5 = 2 + \ln(\sin 1.9290) = 2 + \ln(0.9365) = 1.9344$$

$$q_6 = 2 + \ln(\sin 1.9344) = 2 + \ln(0.9346) = 1.9324$$

$$q_7 = 2 + \ln(\sin 1.9324) = 2 + \ln(0.9353) = 1.9332$$

$$q_8 = 2 + \ln(\sin 1.9332) = 2 + \ln(0.9351) = 1.9329$$

$$q_9 = 2 + \ln(\sin 1.9329) = 2 + \ln(0.9352) = 1.9330$$

$$q_8 \text{ and } q_9 \text{ both round to } 1.93 \text{ (2 d.p.)}$$

$$q = 1.93 \text{ correct to 2 decimal places} \quad\checkmark$$

</details>

---

# Formula Sheet

**Change of sign (root location):**

$$f(a) \text{ and } f(b) \text{ of opposite signs} \;\Rightarrow\; \text{root } \alpha \in (a, b)$$

**Iterative formula (root improvement):**

$$f(x) = 0 \;\Rightarrow\; x = F(x) \qquad x_{n+1} = F(x_n)$$

**Convergence to the root:**

$$x_n \to \alpha \text{ as } n \to \infty, \text{ where } \alpha = F(\alpha) \text{ and } f(\alpha) = 0$$

**Proving the answer (change of sign test on original $f$):**

$$x = a.bc \text{ to 2 d.p. } \Rightarrow \text{ check } f(a.bc \pm 0.005)$$

**Common standard identities used in rearrangements:**

$$\cos x + \sin x = \sqrt{2}\cos\left(x - \frac{\pi}{4}\right)$$

$$\sin 2\theta = 2\sin\theta\cos\theta \qquad \tan\theta = \frac{\sin\theta}{\cos\theta}$$

# Quick Reference Card

1. **Locate:** sketch $y = $ LHS and $y = $ RHS, or evaluate $f(x)$ at two points until the sign changes.
2. **Rearrange:** make $x$ the subject of $f(x) = 0$ to get $x = F(x)$. Choose a rearrangement with a small multiplier on $x$ - test another if the values explode or oscillate wildly.
3. **Iterate:** $x_{n+1} = F(x_n)$ from a sensible $x_1$ (inside the located interval). Record every value; stop when two consecutive values agree to the required accuracy.
4. **Prove:** apply the change of sign test to the ORIGINAL $f(x)$ using the rounding boundaries ($\pm 0.005$ for 2 d.p., or the 3 s.f. bracket), and state the root with its accuracy.
5. **Calculator trick:** type $x_1$ =, then enter the formula with Ans in place of $x_n$; each press of = gives the next iteration.
