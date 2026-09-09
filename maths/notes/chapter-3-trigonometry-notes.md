# 📘 Chapter 3: Trigonometry - 9709 Pure Mathematics 2&3 (CAIE A Level Maths)

## Cambridge International AS & A Level Mathematics (9709) - Paper 3

> **Rule + fully solved examples.** Every technique shown step by step in proper LaTeX, every algebra step on its own line.

---

# PART 3: Trigonometry (Chapter 3)

**Covers:** the reciprocal ratios $\cosec$, $\sec$, $\cot$ (definitions, graphs, identities), compound angle formulae $\sin(A \pm B)$ etc., double angle formulae, further identities derived from double angle, and the $R$-form $a\cos\theta + b\sin\theta = R\cos(\theta - \alpha)$.

## 3.1 The Cosecant, Secant and Cotangent Ratios

These three are the **reciprocal** trigonometric functions:

$$\cosec\theta = \frac{1}{\sin\theta}, \qquad \sec\theta = \frac{1}{\cos\theta}, \qquad \cot\theta = \frac{1}{\tan\theta} = \frac{\cos\theta}{\sin\theta}$$

Defined wherever the denominator is non-zero. From a right-angled triangle with hypotenuse $r$, opposite $y$, adjacent $x$:

$$\sin\theta = \frac{y}{r}, \quad \cos\theta = \frac{x}{r}, \quad \tan\theta = \frac{y}{x}$$

$$\cosec\theta = \frac{r}{y}, \quad \sec\theta = \frac{r}{x}, \quad \cot\theta = \frac{x}{y}$$

**Pythagorean identities** (divide $x^2 + y^2 = r^2$ by $x^2$ or $y^2$):

$$1 + \tan^2\theta \equiv \sec^2\theta$$

$$1 + \cot^2\theta \equiv \cosec^2\theta$$

> ⭐ **Watch Out!** (1) $\cosec\theta$ is undefined where $\sin\theta = 0$ (i.e. $\theta = 0°, 180°, 360°, \ldots$); $\sec\theta$ is undefined where $\cos\theta = 0$ (i.e. $\theta = 90°, 270°, \ldots$); $\cot\theta$ is undefined where $\sin\theta = 0$. These give **vertical asymptotes** on the graphs. (2) The identities $1 + \tan^2\theta \equiv \sec^2\theta$ and $1 + \cot^2\theta \equiv \cosec^2\theta$ are used to solve equations — substitute to get a quadratic in $\tan\theta$ or $\cot\theta$. (3) Exact values: combine the known $\sin$/$\cos$/$\tan$ values with the reciprocal — e.g. $\cosec 30° = \frac{1}{\sin 30°} = 2$.

### Example 30 - Easy - exact values of cosec, sec, cot (coursebook Exercise 3A)

> **Question:** Find the exact values of (a) $\sec 60°$, (b) $\cosec 45°$, (c) $\cot 120°$.

**Solution:**

(a) $\sec 60° = \frac{1}{\cos 60°}$ and $\cos 60° = \frac{1}{2}$:

$$\sec 60° = \frac{1}{1/2} = 2 \quad\checkmark$$

(b) $\cosec 45° = \frac{1}{\sin 45°}$ and $\sin 45° = \frac{\sqrt{2}}{2}$:

$$\cosec 45° = \frac{1}{\sqrt{2}/2} = \frac{2}{\sqrt{2}} = \sqrt{2} \quad\checkmark$$

(c) $\cot 120° = \frac{\cos 120°}{\sin 120°}$ and $\cos 120° = -\frac{1}{2}$, $\sin 120° = \frac{\sqrt{3}}{2}$:

$$\cot 120° = \frac{-1/2}{\sqrt{3}/2} = -\frac{1}{\sqrt{3}} = -\frac{\sqrt{3}}{3} \quad\checkmark$$

Alternatively, $\cot 120° = \frac{1}{\tan 120°} = \frac{1}{-\sqrt{3}} = -\frac{1}{\sqrt{3}}$.

**What the examiner wants:** the reciprocal applied to a known exact value; rationalised denominator.

### Example 31 - Medium - graphs of cosec, sec, cot

> **Question:** Describe the key features of $y = \cosec\theta$ for $0° \leq \theta \leq 360°$.

**Solution:**

$y = \cosec\theta = \frac{1}{\sin\theta}$ is the reciprocal of $y = \sin\theta$.

$$y = \sin\theta = 0 \text{ at } \theta = 0°, 180°, 360° \implies y = \cosec\theta \text{ has vertical asymptotes there}$$

$$y = \sin\theta = \pm 1 \text{ at } \theta = 90°, 270° \implies y = \cosec\theta = \pm 1 \text{ there}$$

Where $|\sin\theta| < 1$, $|\cosec\theta| > 1$ (the cosec curve is outside the sine curve).

$$|\cosec\theta| \geq 1 \text{ for all defined } \theta$$

The graph has U-shaped branches between asymptotes: minimum $y = 1$ at $\theta = 90°$, maximum $y = -1$ at $\theta = 270°$ (for the negative branch), repeating every $360°$. $\checkmark$

Similarly:

$$y = \sec\theta: \text{ asymptotes where } \cos\theta = 0 \text{ (at } 90°, 270°\text{)}, \quad |\sec\theta| \geq 1$$

$$y = \cot\theta: \text{ asymptotes where } \sin\theta = 0 \text{ (at } 0°, 180°, 360°\text{)}, \quad \text{period } 180°, \text{ decreasing from } +\infty \text{ to } -\infty$$

**What the examiner wants:** asymptotes at zeros of the original function; the inequality $|\cosec\theta| \geq 1$ / $|\sec\theta| \geq 1$ stated.

### Example 32 - Medium - solving $\sec^2 x - \tan x - 3 = 0$ (coursebook Worked example 3.2)

> **Question:** Solve $\sec^2 x - \tan x - 3 = 0$ for $0° \leq x \leq 360°$.

**Solution:**

Use $1 + \tan^2 x \equiv \sec^2 x$:

$$\sec^2 x = 1 + \tan^2 x$$

$$(1 + \tan^2 x) - \tan x - 3 = 0$$

$$\tan^2 x - \tan x - 2 = 0$$

Factorise:

$$(\tan x - 2)(\tan x + 1) = 0$$

$$\tan x = 2 \text{ or } \tan x = -1$$

Case 1: $\tan x = 2$:

$$x = \tan^{-1}(2) \approx 63.4°$$

$$x \approx 63.4° \text{ or } 63.4° + 180° = 243.4°$$

Case 2: $\tan x = -1$:

$$x = \tan^{-1}(-1) = -45°$$

$$x = -45° + 180° = 135° \text{ or } 135° + 180° = 315°$$

$$x = 63.4°, \; 135°, \; 243.4°, \; 315° \quad\checkmark$$

**What the examiner wants:** the identity substitution to get a quadratic in $\tan x$; all four solutions in range found (two per $\tan$ value because period is $180°$).

## 3.2 Compound Angle Formulae

For any angles $A$ and $B$:

$$\sin(A + B) \equiv \sin A\cos B + \cos A\sin B$$

$$\sin(A - B) \equiv \sin A\cos B - \cos A\sin B$$

$$\cos(A + B) \equiv \cos A\cos B - \sin A\sin B$$

$$\cos(A - B) \equiv \cos A\cos B + \sin A\sin B$$

$$\tan(A + B) \equiv \frac{\tan A + \tan B}{1 - \tan A\tan B}$$

$$\tan(A - B) \equiv \frac{\tan A - \tan B}{1 + \tan A\tan B}$$

Mnemonic: **sine** keeps the sign ($\sin(A+B)$ has $+$), **cosine** flips it ($\cos(A+B)$ has $-$), **tangent** has the fraction with flipped denominator sign.

> ⭐ **Watch Out!** (1) The sign in $\cos(A+B)$ is MINUS: $\cos(A+B) = \cos A\cos B - \sin A\sin B$ (not plus). (2) For $\tan(A+B)$ the denominator is $1 - \tan A\tan B$ (minus), and for $\tan(A-B)$ it is $1 + \tan A\tan B$ (plus) — the opposite of what you might expect. (3) These formulae let you find exact values for non-standard angles by splitting them: e.g. $75° = 45° + 30°$.

### Example 33 - Medium - exact value using compound angles

> **Question:** Find the exact value of $\sin 75°$.

**Solution:**

Write $75° = 45° + 30°$ and use $\sin(A+B)$:

$$\sin 75° = \sin(45° + 30°)$$

$$= \sin 45°\cos 30° + \cos 45°\sin 30°$$

Substitute exact values $\sin 45° = \cos 45° = \frac{\sqrt{2}}{2}$, $\cos 30° = \frac{\sqrt{3}}{2}$, $\sin 30° = \frac{1}{2}$:

$$= \frac{\sqrt{2}}{2}\cdot\frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2}\cdot\frac{1}{2}$$

$$= \frac{\sqrt{6}}{4} + \frac{\sqrt{2}}{4}$$

$$= \frac{\sqrt{6} + \sqrt{2}}{4} \quad\checkmark$$

**What the examiner wants:** the angle split into two standard angles; the correct compound formula with exact values substituted.

### Example 34 - Medium - proving an identity with compound angles

> **Question:** Prove that $\sin(60° - x) + \sin(60° + x) = \sqrt{3}\cos x$.

**Solution:**

Expand each term using $\sin(A \pm B)$:

$$\sin(60° - x) = \sin 60°\cos x - \cos 60°\sin x$$

$$= \frac{\sqrt{3}}{2}\cos x - \frac{1}{2}\sin x$$

$$\sin(60° + x) = \sin 60°\cos x + \cos 60°\sin x$$

$$= \frac{\sqrt{3}}{2}\cos x + \frac{1}{2}\sin x$$

Add:

$$\sin(60° - x) + \sin(60° + x) = \left(\frac{\sqrt{3}}{2}\cos x - \frac{1}{2}\sin x\right) + \left(\frac{\sqrt{3}}{2}\cos x + \frac{1}{2}\sin x\right)$$

$$= \frac{\sqrt{3}}{2}\cos x + \frac{\sqrt{3}}{2}\cos x - \frac{1}{2}\sin x + \frac{1}{2}\sin x$$

$$= \sqrt{3}\cos x \quad\checkmark$$

**What the examiner wants:** both expansions shown; the $\sin x$ terms cancelling to leave the result.

### Example 35 - Hard - using $\tan(A + B)$ to find an angle

> **Question:** Given that $\tan A = \frac{1}{2}$ and $\tan B = \frac{1}{3}$ where $A$ and $B$ are acute, find the exact value of $\tan(A + B)$ and hence find $A + B$.

**Solution:**

Use $\tan(A+B) = \frac{\tan A + \tan B}{1 - \tan A\tan B}$:

$$\tan(A+B) = \frac{\frac{1}{2} + \frac{1}{3}}{1 - \frac{1}{2}\cdot\frac{1}{3}}$$

Numerator:

$$\frac{1}{2} + \frac{1}{3} = \frac{3+2}{6} = \frac{5}{6}$$

Denominator:

$$1 - \frac{1}{6} = \frac{5}{6}$$

So:

$$\tan(A+B) = \frac{5/6}{5/6} = 1$$

Since $A$ and $B$ are acute, $0° < A+B < 180°$ and $\tan(A+B) = 1 \implies A+B = 45°$. $\checkmark$

$$A + B = 45° \quad\checkmark$$

**What the examiner wants:** the compound tan formula applied with fractions combined carefully; the angle deduced from the exact tan value.

## 3.3 Double Angle Formulae

Setting $B = A$ in the compound angle formulae gives the **double angle** identities:

$$\sin 2A \equiv 2\sin A\cos A$$

$$\cos 2A \equiv \cos^2 A - \sin^2 A \equiv 2\cos^2 A - 1 \equiv 1 - 2\sin^2 A$$

$$\tan 2A \equiv \frac{2\tan A}{1 - \tan^2 A}$$

The three forms of $\cos 2A$ are interchangeable — choose the one that eliminates the unwanted function:

- To get everything in $\cos$: use $\cos 2A = 2\cos^2 A - 1$.
- To get everything in $\sin$: use $\cos 2A = 1 - 2\sin^2 A$.
- Keep both: $\cos 2A = \cos^2 A - \sin^2 A$.

> ⭐ **Watch Out!** (1) $\sin 2A \neq 2\sin A$ — the $2$ does not factor out. $\sin 2A = 2\sin A\cos A$ always has the $\cos A$ factor. (2) When solving equations like $\cos 2x = \sin x$, convert $\cos 2x$ to $1 - 2\sin^2 x$ so everything is in $\sin x$, giving a quadratic. (3) $\cos 2A$ has THREE equivalent forms — picking the right one is the key step in most exam questions.

### Example 36 - Medium - using double angle to find exact values

> **Question:** Given that $\sin A = \frac{3}{5}$ and $A$ is acute, find the exact values of (a) $\sin 2A$, (b) $\cos 2A$.

**Solution:**

First find $\cos A$ using $\sin^2 A + \cos^2 A = 1$:

$$\cos^2 A = 1 - \sin^2 A = 1 - \frac{9}{25} = \frac{16}{25}$$

$$A \text{ acute} \implies \cos A > 0 \implies \cos A = \frac{4}{5}$$

(a) $\sin 2A = 2\sin A\cos A$:

$$\sin 2A = 2\cdot\frac{3}{5}\cdot\frac{4}{5}$$

$$= \frac{24}{25} \quad\checkmark$$

(b) $\cos 2A = \cos^2 A - \sin^2 A$:

$$\cos 2A = \frac{16}{25} - \frac{9}{25}$$

$$= \frac{7}{25} \quad\checkmark$$

Check with other forms: $1 - 2\sin^2 A = 1 - \frac{18}{25} = \frac{7}{25} \checkmark$; $2\cos^2 A - 1 = \frac{32}{25} - 1 = \frac{7}{25} \checkmark$.

**What the examiner wants:** the correct $\cos A$ sign chosen for the given quadrant; the double angle formula applied exactly.

### Example 37 - Hard - solving $\cos 2x = \sin x$ for $0° \leq x \leq 360°$

> **Question:** Solve $\cos 2x = \sin x$ for $0° \leq x \leq 360°$.

**Solution:**

Convert $\cos 2x$ to sines: $\cos 2x = 1 - 2\sin^2 x$:

$$1 - 2\sin^2 x = \sin x$$

Rearrange to a quadratic in $\sin x$:

$$2\sin^2 x + \sin x - 1 = 0$$

Factorise:

$$(2\sin x - 1)(\sin x + 1) = 0$$

$$\sin x = \frac{1}{2} \text{ or } \sin x = -1$$

Case 1: $\sin x = \frac{1}{2}$:

$$x = 30° \text{ or } x = 180° - 30° = 150°$$

Case 2: $\sin x = -1$:

$$x = 270°$$

$$x = 30°, \; 150°, \; 270° \quad\checkmark$$

**What the examiner wants:** the correct form of $\cos 2x$ chosen (the one in $\sin x$); the quadratic factorised; all solutions in range — including the single solution from $\sin x = -1$ (only one value of $x$ in $[0°, 360°]$ gives $\sin x = -1$).

### Example 38 - Hard - solving $\sin 2x = \cos x$ for $0 \leq x \leq 2\pi$

> **Question:** Solve $\sin 2x = \cos x$ for $0 \leq x \leq 2\pi$.

**Solution:**

Use $\sin 2x = 2\sin x\cos x$:

$$2\sin x\cos x = \cos x$$

$$2\sin x\cos x - \cos x = 0$$

Factorise:

$$\cos x(2\sin x - 1) = 0$$

$$\cos x = 0 \text{ or } \sin x = \frac{1}{2}$$

Case 1: $\cos x = 0$:

$$x = \frac{\pi}{2} \text{ or } x = \frac{3\pi}{2}$$

Case 2: $\sin x = \frac{1}{2}$:

$$x = \frac{\pi}{6} \text{ or } x = \pi - \frac{\pi}{6} = \frac{5\pi}{6}$$

$$x = \frac{\pi}{6}, \; \frac{\pi}{2}, \; \frac{5\pi}{6}, \; \frac{3\pi}{2} \quad\checkmark$$

**What the examiner wants:** factoring (not dividing by $\cos x$, which loses solutions); all four solutions found. Never divide by a trig function that could be zero.

## 3.4 Further Trigonometric Identities

These are derived from the double angle formulae and $\sin^2\theta + \cos^2\theta \equiv 1$:

$$\sin^2\theta \equiv \frac{1 - \cos 2\theta}{2}, \qquad \cos^2\theta \equiv \frac{1 + \cos 2\theta}{2}$$

$$\tan^2\theta \equiv \sec^2\theta - 1$$

Other useful identities obtained by combining compound and double angle results:

$$\sin 3\theta \equiv 3\sin\theta - 4\sin^3\theta$$

$$\cos 3\theta \equiv 4\cos^3\theta - 3\cos\theta$$

And factor formulae (product-to-sum), useful in integration (Chapter 5):

$$2\sin A\cos B \equiv \sin(A+B) + \sin(A-B)$$

$$2\cos A\cos B \equiv \cos(A+B) + \cos(A-B)$$

$$2\sin A\sin B \equiv \cos(A-B) - \cos(A+B)$$

> ⭐ **Watch Out!** $\sin^2\theta = \frac{1 - \cos 2\theta}{2}$ has a MINUS sign; $\cos^2\theta = \frac{1 + \cos 2\theta}{2}$ has a PLUS sign. These half-angle rearrangements are the reverse of the double-angle forms.

### Example 39 - Medium - expressing $\cos^2 x$ in terms of $\cos 2x$

> **Question:** Express $\cos^2 x$ in terms of $\cos 2x$ and hence find $\int \cos^2 x\,dx$ (preview of Chapter 5 technique).

**Solution:**

From $\cos 2x = 2\cos^2 x - 1$:

$$2\cos^2 x = 1 + \cos 2x$$

$$\cos^2 x = \frac{1 + \cos 2x}{2} \quad\checkmark$$

Hence:

$$\int \cos^2 x\,dx = \int \frac{1 + \cos 2x}{2}\,dx$$

$$= \frac{1}{2}\int (1 + \cos 2x)\,dx$$

$$= \frac{1}{2}\left(x + \frac{1}{2}\sin 2x\right) + c$$

$$= \frac{x}{2} + \frac{\sin 2x}{4} + c \quad\checkmark$$

**What the examiner wants:** the identity rearranged correctly (plus sign for $\cos^2$); the integration done term by term afterwards.

### Example 40 - Hard - proving $\cos 3\theta = 4\cos^3\theta - 3\cos\theta$

> **Question:** Prove that $\cos 3\theta \equiv 4\cos^3\theta - 3\cos\theta$.

**Solution:**

Write $3\theta = 2\theta + \theta$ and use $\cos(A+B)$:

$$\cos 3\theta = \cos(2\theta + \theta)$$

$$= \cos 2\theta\cos\theta - \sin 2\theta\sin\theta$$

Substitute double angle forms $\cos 2\theta = 2\cos^2\theta - 1$ and $\sin 2\theta = 2\sin\theta\cos\theta$:

$$= (2\cos^2\theta - 1)\cos\theta - (2\sin\theta\cos\theta)\sin\theta$$

$$= 2\cos^3\theta - \cos\theta - 2\sin^2\theta\cos\theta$$

Replace $\sin^2\theta = 1 - \cos^2\theta$:

$$= 2\cos^3\theta - \cos\theta - 2(1-\cos^2\theta)\cos\theta$$

$$= 2\cos^3\theta - \cos\theta - 2\cos\theta + 2\cos^3\theta$$

$$= 4\cos^3\theta - 3\cos\theta \quad\checkmark$$

**What the examiner wants:** the split $3\theta = 2\theta + \theta$; the double angle substitutions; the $\sin^2 \to \cos^2$ conversion to get everything in $\cos\theta$.

## 3.5 Expressing a cos θ + b sin θ in the Form R sin(θ ± α) or R cos(θ ± α)

Any expression $a\cos\theta + b\sin\theta$ can be written as a single trig function:

$$a\cos\theta + b\sin\theta \equiv R\cos(\theta - \alpha) \equiv R\sin(\theta + \alpha') \quad\text{etc.}$$

where:

$$R = \sqrt{a^2 + b^2} > 0$$

$$\alpha = \tan^{-1}\!\left(\frac{b}{a}\right) \quad\text{(with quadrant determined by signs of } a, b\text{)}$$

The four variants (choose the one matching the question):

$$R\cos(\theta - \alpha) = R\cos\theta\cos\alpha + R\sin\theta\sin\alpha \implies a = R\cos\alpha,\; b = R\sin\alpha$$

$$R\cos(\theta + \alpha) = R\cos\theta\cos\alpha - R\sin\theta\sin\alpha \implies a = R\cos\alpha,\; b = -R\sin\alpha$$

$$R\sin(\theta + \alpha) = R\sin\theta\cos\alpha + R\cos\theta\sin\alpha \implies a = R\sin\alpha,\; b = R\cos\alpha$$

$$R\sin(\theta - \alpha) = R\sin\theta\cos\alpha - R\cos\theta\sin\alpha \implies a = -R\sin\alpha,\; b = R\cos\alpha$$

**Method:** (1) Find $R = \sqrt{a^2+b^2}$. (2) Expand $R\cos(\theta - \alpha)$ (or whichever form) and compare coefficients to find $\cos\alpha$ and $\sin\alpha$. (3) Find $\alpha$ (usually acute; check quadrant). (4) To solve equations or find max/min, work with the $R$-form.

Maximum and minimum:

$$-R \leq a\cos\theta + b\sin\theta \leq R$$

The maximum $R$ occurs when $\cos(\theta - \alpha) = 1$, i.e. $\theta = \alpha$; the minimum $-R$ when $\cos(\theta - \alpha) = -1$, i.e. $\theta = \alpha + 180°$.

> ⭐ **Watch Out!** (1) $R$ is always positive: $R = \sqrt{a^2+b^2}$. (2) $\alpha$ is found from $\tan\alpha = \frac{b}{a}$ (for the $R\cos(\theta-\alpha)$ form) — but check which quadrant $\alpha$ is in from the individual signs of $\cos\alpha = \frac{a}{R}$ and $\sin\alpha = \frac{b}{R}$. (3) When solving $a\cos\theta + b\sin\theta = c$, rewrite as $R\cos(\theta-\alpha) = c$ and solve $\cos(\theta-\alpha) = \frac{c}{R}$ — this gives at most two solutions per $360°$ period. If $|c| > R$ there is no solution. (4) The form $R\sin(\theta + \alpha)$ has $a = R\sin\alpha$ and $b = R\cos\alpha$ — the roles of $a$ and $b$ are swapped compared to $R\cos(\theta-\alpha)$.

### Example 41 - Medium - expressing $3\cos\theta + 4\sin\theta$ in R-form (coursebook Section 3.5)

> **Question:** Express $3\cos\theta + 4\sin\theta$ in the form $R\cos(\theta - \alpha)$ where $R > 0$ and $0° < \alpha < 90°$.

**Solution:**

Find $R$:

$$R = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$

Expand $R\cos(\theta - \alpha)$ and compare:

$$R\cos(\theta - \alpha) = R\cos\theta\cos\alpha + R\sin\theta\sin\alpha$$

So:

$$R\cos\alpha = 3, \qquad R\sin\alpha = 4$$

$$\cos\alpha = \frac{3}{5}, \qquad \sin\alpha = \frac{4}{5}$$

Both positive $\implies \alpha$ in first quadrant:

$$\tan\alpha = \frac{4}{3}$$

$$\alpha = \tan^{-1}\!\left(\frac{4}{3}\right) \approx 53.1°$$

$$3\cos\theta + 4\sin\theta \equiv 5\cos(\theta - 53.1°) \quad\checkmark$$

Exact form: $\cos\alpha = \frac{3}{5}$, $\sin\alpha = \frac{4}{5}$, $\alpha = \tan^{-1}\!\frac{4}{3}$.

**What the examiner wants:** $R = 5$ found via $\sqrt{a^2+b^2}$; $\alpha$ from $\tan\alpha = \frac{b}{a}$ with the correct form chosen; $\alpha$ given to the required accuracy and in the correct quadrant.

### Example 42 - Medium - finding maximum and minimum values

> **Question:** Find the maximum and minimum values of $5\cos\theta + 12\sin\theta$ and the values of $\theta$ in $[0°, 360°)$ where they occur.

**Solution:**

Find $R$:

$$R = \sqrt{5^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13$$

Write in $R$-form:

$$5\cos\theta + 12\sin\theta = R\cos(\theta - \alpha)$$

$$R\cos\alpha = 5, \quad R\sin\alpha = 12$$

$$\cos\alpha = \frac{5}{13}, \quad \sin\alpha = \frac{12}{13}$$

$$\tan\alpha = \frac{12}{5}$$

$$\alpha = \tan^{-1}\!\left(\frac{12}{5}\right) \approx 67.4°$$

So:

$$5\cos\theta + 12\sin\theta \equiv 13\cos(\theta - 67.4°)$$

Maximum: $\cos(\theta - \alpha) = 1$:

$$13 \times 1 = 13 \quad\text{at } \theta - 67.4° = 0° \implies \theta = 67.4°$$

Minimum: $\cos(\theta - \alpha) = -1$:

$$13 \times (-1) = -13 \quad\text{at } \theta - 67.4° = 180° \implies \theta = 247.4°$$

$$\text{Maximum } 13 \text{ at } \theta = 67.4°, \quad \text{Minimum } -13 \text{ at } \theta = 247.4° \quad\checkmark$$

**What the examiner wants:** $R$ as the maximum/minimum magnitude; the $\theta$ values found by solving $\theta - \alpha = 0°$ and $180°$ respectively.

### Example 43 - Hard - solving $a\cos\theta + b\sin\theta = c$ using R-form

> **Question:** Solve $3\cos\theta + 4\sin\theta = 2$ for $0° \leq \theta < 360°$.

**Solution:**

From Example 41: $3\cos\theta + 4\sin\theta \equiv 5\cos(\theta - 53.1°)$ where $\alpha = \tan^{-1}\!\frac{4}{3} \approx 53.13°$.

$$5\cos(\theta - 53.13°) = 2$$

$$\cos(\theta - 53.13°) = \frac{2}{5} = 0.4$$

$$\theta - 53.13° = \pm\cos^{-1}(0.4) + 360°k$$

$$\cos^{-1}(0.4) \approx 66.42°$$

So:

$$\theta - 53.13° = 66.42° \implies \theta = 119.55°$$

$$\theta - 53.13° = -66.42° \implies \theta = -13.29° \implies \theta = 346.71° \quad (+360°)$$

$$ \theta \approx 119.6° \text{ or } 346.7° \quad\checkmark$$

Check: $3\cos 119.55° + 4\sin 119.55° \approx 3(-0.493) + 4(0.870) \approx -1.48 + 3.48 = 2.00 \checkmark$.

**What the examiner wants:** the $R$-form used to reduce to a single cosine equation; both solutions in $[0°, 360°)$ found — including the one that wraps around past $360°$.

### Example 44 - Hard - R-form with $R\sin(\theta + \alpha)$ (coursebook Section 3.5 variant)

> **Question:** Express $4\cos\theta - 3\sin\theta$ in the form $R\sin(\theta + \alpha)$ where $R > 0$ and $0° < \alpha < 90°$.

**Solution:**

Find $R$:

$$R = \sqrt{4^2 + (-3)^2} = \sqrt{16 + 9} = 5$$

Expand $R\sin(\theta + \alpha)$ (note: we want $R\sin(\theta + \alpha)$ but our expression is in $\cos$ and $\sin$ — alternatively use $R\cos(\theta + \alpha)$ and convert, or work with $R\sin$ directly).

Try $R\sin(\theta + \alpha) = R\sin\theta\cos\alpha + R\cos\theta\sin\alpha$:

$$R\sin\alpha = 4, \qquad R\cos\alpha = -3$$

This gives $\cos\alpha = -\frac{3}{5}$ (negative) — so $\alpha$ would not be in $(0°, 90°)$ for this form. Try instead $R\cos(\theta + \alpha)$:

$$R\cos(\theta + \alpha) = R\cos\theta\cos\alpha - R\sin\theta\sin\alpha$$

$$R\cos\alpha = 4, \qquad R\sin\alpha = 3$$

$$\cos\alpha = \frac{4}{5}, \quad \sin\alpha = \frac{3}{5}, \quad \tan\alpha = \frac{3}{4}$$

$$\alpha = \tan^{-1}\!\left(\frac{3}{4}\right) \approx 36.87°$$

$$4\cos\theta - 3\sin\theta \equiv 5\cos(\theta + 36.87°) \quad\checkmark$$

To write as $R\sin(\theta + \alpha')$: use $\cos(\theta + 36.87°) = \sin(90° - (\theta + 36.87°))$... or solve directly for $R\sin(\theta + \alpha')$:

$$R\sin(\theta + \alpha') = R\sin\theta\cos\alpha' + R\cos\theta\sin\alpha'$$

$$R\sin\alpha' = 4, \quad R\cos\alpha' = -3$$

With $R = 5$: $\sin\alpha' = \frac{4}{5}$, $\cos\alpha' = -\frac{3}{5}$ — so $\alpha'$ is in the second quadrant: $\alpha' = 180° - 36.87° = 126.87°$.

$$4\cos\theta - 3\sin\theta \equiv 5\sin(\theta + 126.87°) \quad\checkmark$$

If restricted to $0° < \alpha < 90°$, the $R\cos$ form $5\cos(\theta + 36.87°)$ is the appropriate answer.

**What the examiner wants:** awareness that the choice of $R$-form determines whether $\alpha$ is acute — if the question specifies $0° < \alpha < 90°$, choose the form that makes $\alpha$ acute.

### Practice Questions - Part 3

**Q10.** Find the exact value of $\cot 150°$.

**Q11.** Solve $\cosec^2 x - 2\cot x = 4$ for $0° \leq x \leq 360°$.

**Q12.** Given $\cos A = \frac{1}{3}$ with $A$ acute, find the exact value of $\cos 2A$.

**Q13.** Prove that $\sin(A+B) + \sin(A-B) \equiv 2\sin A\cos B$.

**Q14.** Express $12\cos\theta + 5\sin\theta$ in the form $R\cos(\theta - \alpha)$ with $R > 0$ and $0° < \alpha < 90°$. Hence find the maximum value of $12\cos\theta + 5\sin\theta$.

**Q15.** Solve $12\cos\theta + 5\sin\theta = 10$ for $0° \leq \theta < 360°$.

### Practice Questions - Part 3 - Full Solutions

**Solution Q10:**

$$\cot 150° = \frac{1}{\tan 150°} = \frac{1}{\tan(180°-30°)} = \frac{1}{-\tan 30°}$$

$$= \frac{1}{-1/\sqrt{3}} = -\sqrt{3} \quad\checkmark$$

Alternatively $\cot 150° = \frac{\cos 150°}{\sin 150°} = \frac{-\sqrt{3}/2}{1/2} = -\sqrt{3}$.

**Solution Q11:**

Use $1 + \cot^2 x \equiv \cosec^2 x$:

$$(1 + \cot^2 x) - 2\cot x = 4$$

$$\cot^2 x - 2\cot x - 3 = 0$$

$$(\cot x - 3)(\cot x + 1) = 0$$

$$\cot x = 3 \text{ or } \cot x = -1$$

$\cot x = 3 \implies \tan x = \frac{1}{3} \implies x = \tan^{-1}\!\frac{1}{3} \approx 18.4°$ or $198.4°$.

$\cot x = -1 \implies \tan x = -1 \implies x = 135°$ or $315°$.

$$x = 18.4°, \; 135°, \; 198.4°, \; 315° \quad\checkmark$$

**Solution Q12:**

$$\cos 2A = 2\cos^2 A - 1 = 2\left(\frac{1}{9}\right) - 1 = \frac{2}{9} - 1 = -\frac{7}{9} \quad\checkmark$$

**Solution Q13:**

$$\sin(A+B) = \sin A\cos B + \cos A\sin B$$

$$\sin(A-B) = \sin A\cos B - \cos A\sin B$$

Add:

$$\sin(A+B) + \sin(A-B) = 2\sin A\cos B \quad\checkmark$$

**Solution Q14:**

$$R = \sqrt{12^2 + 5^2} = \sqrt{144 + 25} = \sqrt{169} = 13$$

$$R\cos\alpha = 12, \quad R\sin\alpha = 5$$

$$\tan\alpha = \frac{5}{12}, \quad \alpha = \tan^{-1}\!\left(\frac{5}{12}\right) \approx 22.62°$$

$$12\cos\theta + 5\sin\theta \equiv 13\cos(\theta - 22.62°) \quad\checkmark$$

Maximum $= R = 13$ (when $\cos(\theta - \alpha) = 1$, i.e. $\theta = 22.62°$). $\checkmark$

**Solution Q15:**

$$13\cos(\theta - 22.62°) = 10$$

$$\cos(\theta - 22.62°) = \frac{10}{13}$$

$$\cos^{-1}\!\left(\frac{10}{13}\right) \approx 39.72°$$

$$\theta - 22.62° = \pm 39.72°$$

$$\theta = 22.62° + 39.72° = 62.34°$$

$$\theta = 22.62° - 39.72° = -17.10° \implies 342.90°$$

$$\theta \approx 62.3° \text{ or } 342.9° \quad\checkmark$$

---

# Practice Questions

Comprehensive cross-topic practice covering all three chapters. Full solutions follow immediately after.

**PQ1.** Solve $|5x - 3| = 12$.

**PQ2.** Solve $|x + 2| = |3x - 1|$.

**PQ3.** The polynomial $P(x) = x^3 - 2x^2 + ax + b$ satisfies $P(1) = 0$ and $P(-1) = 10$. Find $a$ and $b$. Is $(x-2)$ a factor of $P(x)$?

**PQ4.** Divide $3x^3 - 5x^2 + 2x - 8$ by $x - 2$ and state the quotient and remainder.

**PQ5.** Solve $\log_5(x + 3) + \log_5(x - 1) = 2$.

**PQ6.** Solve $4^x - 5\cdot 2^x + 4 = 0$.

**PQ7.** Variables $x$ and $y$ satisfy $y = k\,x^n$. When $\log_{10} y$ is plotted against $\log_{10} x$, the straight line has gradient $2.5$ and passes through $(\log_{10} x, \log_{10} y) = (1, 4)$. Find $k$ and $n$.

**PQ8.** Find the exact value of $\sec 135°$.

**PQ9.** Prove that $\cos(A - B) - \cos(A + B) \equiv 2\sin A\sin B$.

**PQ10.** Given $\sin x = \frac{5}{13}$ with $x$ acute, find the exact value of $\sin 2x$.

**PQ11.** Solve $\cos 2\theta + 3\sin\theta = 2$ for $0° \leq \theta \leq 360°$.

**PQ12.** Express $7\cos\theta + 24\sin\theta$ in the form $R\cos(\theta - \alpha)$ where $R > 0$ and $0° < \alpha < 90°$. State $R$ and $\alpha$ to 1 d.p.

---

# Practice Questions - Full Solutions

**Solution PQ1:**

$$|5x - 3| = 12 \implies 5x - 3 = 12 \text{ or } 5x - 3 = -12$$

$$5x = 15 \implies x = 3$$

$$5x = -9 \implies x = -\frac{9}{5}$$

$$x = -\frac{9}{5} \text{ or } x = 3 \quad\checkmark$$

**Solution PQ2:**

$$|x+2| = |3x-1| \implies x+2 = 3x-1 \text{ or } x+2 = -(3x-1)$$

$$x + 2 = 3x - 1$$

$$3 = 2x \implies x = \frac{3}{2}$$

$$x + 2 = -3x + 1$$

$$4x = -1 \implies x = -\frac{1}{4}$$

$$x = -\frac{1}{4} \text{ or } x = \frac{3}{2} \quad\checkmark$$

**Solution PQ3:**

$P(1) = 0$: $1 - 2 + a + b = 0 \implies a + b = 1$.

$P(-1) = 10$: $-1 - 2 - a + b = 10 \implies -a + b = 13$.

Add: $2b = 14 \implies b = 7$, then $a = -6$.

So $P(x) = x^3 - 2x^2 - 6x + 7$.

Check $(x-2)$: $P(2) = 8 - 8 - 12 + 7 = -5 \neq 0$, so $(x-2)$ is **not** a factor. $\checkmark$

$$a = -6, \quad b = 7, \quad (x-2) \text{ not a factor} \quad\checkmark$$

**Solution PQ4:**

Long division of $3x^3 - 5x^2 + 2x - 8$ by $x - 2$:

$$3x^3 \div x = 3x^2, \quad 3x^2(x-2) = 3x^3 - 6x^2$$

$$(3x^3 - 5x^2) - (3x^3 - 6x^2) = x^2$$

Bring down $2x$: $x^2 + 2x$, then $x^2 \div x = x$, $x(x-2) = x^2 - 2x$:

$$(x^2 + 2x) - (x^2 - 2x) = 4x$$

Bring down $-8$: $4x - 8$, then $4x \div x = 4$, $4(x-2) = 4x - 8$:

$$(4x - 8) - (4x - 8) = 0$$

$$\text{Quotient} = 3x^2 + x + 4, \quad \text{Remainder} = 0 \quad\checkmark$$

So $x - 2$ is a factor.

**Solution PQ5:**

Need $x + 3 > 0$ and $x - 1 > 0$, so $x > 1$.

$$\log_5\!\left((x+3)(x-1)\right) = 2$$

$$(x+3)(x-1) = 5^2 = 25$$

$$x^2 + 2x - 3 = 25$$

$$x^2 + 2x - 28 = 0$$

$$x = \frac{-2 \pm \sqrt{4 + 112}}{2} = \frac{-2 \pm \sqrt{116}}{2} = \frac{-2 \pm 2\sqrt{29}}{2} = -1 \pm \sqrt{29}$$

Reject $x = -1 - \sqrt{29} < 0$ (fails $x > 1$):

$$x = -1 + \sqrt{29} \approx 4.39 \quad\checkmark$$

**Solution PQ6:**

Let $y = 2^x$ (so $4^x = (2^2)^x = (2^x)^2 = y^2$):

$$y^2 - 5y + 4 = 0$$

$$(y-1)(y-4) = 0$$

$$y = 1 \text{ or } y = 4$$

$$2^x = 1 \implies x = 0$$

$$2^x = 4 \implies x = 2$$

$$x = 0 \text{ or } x = 2 \quad\checkmark$$

**Solution PQ7:**

$$\log_{10} y = \log_{10} k + n\log_{10} x$$

Gradient $= n = 2.5$.

The line passes through $(\log_{10} x, \log_{10} y) = (1, 4)$:

$$4 = \log_{10} k + 2.5(1)$$

$$\log_{10} k = 1.5$$

$$k = 10^{1.5} = 10\sqrt{10} \approx 31.6$$

$$k = 10^{1.5} \approx 31.6, \quad n = 2.5 \quad\checkmark$$

**Solution PQ8:**

$$\sec 135° = \frac{1}{\cos 135°} = \frac{1}{\cos(180°-45°)} = \frac{1}{-\cos 45°}$$

$$= \frac{1}{-\sqrt{2}/2} = -\frac{2}{\sqrt{2}} = -\sqrt{2} \quad\checkmark$$

**Solution PQ9:**

$$\cos(A-B) = \cos A\cos B + \sin A\sin B$$

$$\cos(A+B) = \cos A\cos B - \sin A\sin B$$

Subtract:

$$\cos(A-B) - \cos(A+B) = (\cos A\cos B + \sin A\sin B) - (\cos A\cos B - \sin A\sin B)$$

$$= 2\sin A\sin B \quad\checkmark$$

**Solution PQ10:**

$$\sin x = \frac{5}{13}, \quad \cos^2 x = 1 - \frac{25}{169} = \frac{144}{169}, \quad \cos x = \frac{12}{13} \text{ (acute)}$$

$$\sin 2x = 2\sin x\cos x = 2\cdot\frac{5}{13}\cdot\frac{12}{13} = \frac{120}{169} \quad\checkmark$$

**Solution PQ11:**

Use $\cos 2\theta = 1 - 2\sin^2\theta$:

$$1 - 2\sin^2\theta + 3\sin\theta = 2$$

$$-2\sin^2\theta + 3\sin\theta - 1 = 0$$

$$2\sin^2\theta - 3\sin\theta + 1 = 0$$

$$(2\sin\theta - 1)(\sin\theta - 1) = 0$$

$$\sin\theta = \frac{1}{2} \text{ or } \sin\theta = 1$$

$\sin\theta = \frac{1}{2} \implies \theta = 30°, 150°$.

$\sin\theta = 1 \implies \theta = 90°$.

$$\theta = 30°, \; 90°, \; 150° \quad\checkmark$$

**Solution PQ12:**

$$R = \sqrt{7^2 + 24^2} = \sqrt{49 + 576} = \sqrt{625} = 25$$

$$25\cos\alpha = 7, \quad 25\sin\alpha = 24$$

$$\tan\alpha = \frac{24}{7}, \quad \alpha = \tan^{-1}\!\left(\frac{24}{7}\right) \approx 73.74°$$

$$7\cos\theta + 24\sin\theta \equiv 25\cos(\theta - 73.7°) \quad\checkmark$$

$$R = 25, \quad \alpha \approx 73.7° \quad\checkmark$$

---


---

# Formula Sheet (Chapter 3)

*Extracted from the chapter — see full sheet in the combined file for cross-topic formulas. This sheet covers only Chapter 3: Trigonometry.*

# Quick Reference Card (Chapter 3)

*See combined file for the full quick reference. Key results for Chapter 3: Trigonometry are boxed throughout the chapter above.*
