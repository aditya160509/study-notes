# Chapter 14: Superposition of Waves - CAIE A Level Physics (9702) Study Notes

Exam-focused revision notes for Cambridge International AS & A Level Physics 9702, covering Chapter 14: the principle of superposition, constructive and destructive interference, coherence, two-source interference, Young's double-slit experiment, diffraction gratings, white-light fringes and antiphase noise cancellation. This is heavily examined in Paper 2 and Paper 4, usually as a calculation on fringe spacing or grating angles plus a "state and explain" part on coherence or path difference. Definitions are worded for mark schemes, and every section ends with a worked example. Chapter 13 covers the basic wave quantities, polarisation and the electromagnetic spectrum; this chapter concentrates on what happens when waves **meet**.

## 1. Theory

### 1.1 The principle of superposition

**The principle of superposition:** when two or more waves meet at a point, the resultant displacement is the **algebraic sum** of the displacements of the individual waves.

"Algebraic" means signs matter: a positive displacement (above equilibrium) and a negative displacement (below equilibrium) partly or wholly cancel. The principle applies to all waves — sound, light, water, microwaves, seismic waves — and to any number of waves.

The waves do not bounce off each other or change their individual identities; after crossing, each continues as if the other were not there. This is why two torch beams cross without interacting, and why you can hear several conversations at once.

**Adding waves graphically:** at each point along the distance axis, add the heights of the two displacement–distance graphs. The result is the resultant waveform. Where both are positive, the result is a larger positive displacement; where one is positive and the other negative, the result is smaller (or negative).

**Worked example:** Two waves of the same frequency meet in phase. Their amplitudes are $3.0~\text{cm}$ and $2.0~\text{cm}$. Calculate the resultant amplitude. Repeat for a phase difference of $180^\circ$.

1. In phase: displacements add, so $A = 3.0 + 2.0 = 5.0~\text{cm}$.
2. In antiphase: displacements subtract, so $A = 3.0 - 2.0 = 1.0~\text{cm}$.

**Answer:** $5.0~\text{cm}$ in phase; $1.0~\text{cm}$ in antiphase.

### 1.2 Constructive and destructive interference

**Interference** is the superposition of waves from two or more sources, producing regions of reinforcement and cancellation.

| Condition | Path difference | Phase difference | Result |
|---|---|---|---|
| Constructive | $n\lambda$ ($0, \lambda, 2\lambda, \dots$) | $0, 360^\circ, 720^\circ, \dots$ | Displacements add; maximum amplitude |
| Destructive | $\left(n+\frac{1}{2}\right)\lambda$ ($\frac{\lambda}{2}, \frac{3\lambda}{2}, \dots$) | $180^\circ, 540^\circ, \dots$ | Displacements cancel; minimum (often zero) amplitude |

Here $n = 0, 1, 2, \dots$ is any non-negative integer.

**Important:** the path difference conditions apply when the two sources are **in phase** at emission. If the sources are themselves in antiphase, the conditions swap: constructive occurs at $\left(n+\frac{1}{2}\right)\lambda$ and destructive at $n\lambda$. Always check the source phase.

If the two waves have **unequal amplitudes**, destructive interference does not give complete cancellation: the minimum amplitude is $A_1 - A_2$, not zero. Complete cancellation requires equal amplitudes **and** a phase difference of $180^\circ$.

**Worked example:** Two coherent waves of wavelength $0.80~\text{cm}$ arrive at a point with path difference $1.2~\text{cm}$. State and explain the type of interference.

1. $\frac{\Delta x}{\lambda} = \frac{1.2}{0.80} = 1.5$.
2. $1.5\lambda = \left(1+\frac{1}{2}\right)\lambda$, an odd number of half-wavelengths.
3. The waves arrive in antiphase, so the interference is destructive.

**Answer:** destructive interference.

### 1.3 Coherence

**Coherent sources** emit waves with a **constant phase difference**. This requires the same frequency (and, in practice, a stable phase relationship).

Why coherence matters: if the phase difference between two sources changes randomly, the positions of constructive and destructive interference shift continuously. Over the observation time the bright and dark regions blur into a uniform average intensity, and no stable pattern is seen.

- Two separate lamps are **not coherent**: each atom emits independently, with random phase, so the pattern changes far too quickly to observe.
- A **laser** is highly coherent and monochromatic, so it produces a stable, high-contrast pattern.
- In the school experiment, a **single slit** is placed before the double slit. The same wavefront reaches both slits, so they act as coherent sources with zero (or constant) phase difference.
- Two loudspeakers driven by the **same signal generator** are coherent. Two separate generators at slightly different frequencies are not: the phase difference drifts, and the loudness rises and falls periodically (**beats**).

**Worked example:** Explain why two identical lamps placed side by side do not produce a stable interference pattern, even though they emit the same wavelength.

1. The light from each lamp comes from many independent atomic emissions.
2. The phase difference between the two beams changes randomly and rapidly.
3. The bright and dark fringes move continuously and average out, so no steady pattern is observed.

**Answer:** the lamps are not coherent, because their phase difference is not constant.

### 1.4 Two-source interference in sound, microwaves and water

The same physics applies to any wave. Three standard experiments:

**Sound (two loudspeakers):** two loudspeakers connected to one signal generator emit coherent sound. Walking across the region in front, you hear alternating **loud** (constructive) and **quiet** (destructive) regions. The path difference from the two speakers changes as you move, passing through $n\lambda$ and $(n+\frac{1}{2})\lambda$ in turn.

**Microwaves:** a transmitter sends $2.8~\text{cm}$ (or $3~\text{cm}$) waves at a metal barrier with two gaps. The gaps diffract the waves, which then interfere. A probe connected to a meter detects maxima and minima as it moves along a line beyond the barrier. This is the microwave analogue of the double-slit experiment, and $w = \frac{\lambda D}{a}$ applies.

**Ripple tank:** two dippers (or two gaps in a barrier) produce overlapping circular ripples. The pattern of nodal lines (calm water) and antinodal lines (large ripples) is visible directly. The nodal lines are the curves where the path difference is $(n+\frac{1}{2})\lambda$.

**Why a single source is split:** using one source and two slits (or two gaps) guarantees coherence, because the two sets of waves come from the same wavefront.

**Worked example:** Two loudspeakers $1.5~\text{m}$ apart are driven in phase at the same frequency. A student $8.0~\text{m}$ away walks along a line parallel to the speakers and finds quiet spots $1.2~\text{m}$ apart. Estimate the wavelength.

1. Treat the arrangement like a double slit: fringe spacing $w = 1.2~\text{m}$, $D = 8.0~\text{m}$, $a = 1.5~\text{m}$.
2. $\lambda = \frac{wa}{D} = \frac{1.2 \times 1.5}{8.0} = 0.225~\text{m}$.

**Answer:** $\lambda \approx 0.23~\text{m}$ (about $23~\text{cm}$, a low-frequency sound).

### 1.5 Path difference and phase difference

The **path difference** $\Delta x$ is the extra distance travelled by one wave compared with the other from the sources to the point of interest. It determines the phase difference at that point:

$$\frac{\Delta\phi}{360^\circ} = \frac{\Delta x}{\lambda} \qquad \text{or} \qquad \Delta\phi = \frac{2\pi\Delta x}{\lambda}~\text{rad}$$

Equivalently, one wavelength corresponds to $2\pi$ radians or $360^\circ$.

**Worked example:** Two coherent waves of wavelength $0.60~\text{m}$ arrive at a point with path difference $0.15~\text{m}$. Calculate the phase difference.

1. $\frac{\Delta x}{\lambda} = \frac{0.15}{0.60} = 0.25$.
2. $\Delta\phi = 0.25 \times 360^\circ = 90^\circ$ ($\frac{\pi}{2}$ rad).

**Answer:** $90^\circ$.

### 1.6 Young's double-slit experiment

**The experiment (1801):** monochromatic light passes through a single narrow slit (to ensure coherence), then through two parallel slits a fraction of a millimetre apart. The light diffracts from each slit and the two diffracted beams overlap on a screen about a metre away, producing a pattern of equally spaced bright and dark **fringes**.

**What is observed:**

- A **bright central fringe** directly opposite the midpoint of the slits, because the path difference there is zero.
- Equally spaced bright and dark fringes on either side.
- The fringe spacing increases if $\lambda$ increases, $D$ increases, or $a$ decreases.
- With white light, the central fringe is white and the side fringes are coloured.

**Derivation of the fringe spacing.** Let the slit separation be $a$, the slit-to-screen distance $D$, and the position of a point on the screen be $x$ measured from the centre. The path difference between rays from the two slits is

$$\Delta x \approx a\sin\theta$$

where $\theta$ is the angle to the point. For small angles (which is the case when $D \gg x$),

$$\sin\theta \approx \tan\theta = \frac{x}{D}$$

so

$$\Delta x \approx \frac{ax}{D}$$

For the $n$th bright fringe, $\Delta x = n\lambda$:

$$\frac{ax_n}{D} = n\lambda \qquad \Rightarrow \qquad x_n = \frac{n\lambda D}{a}$$

The spacing between adjacent bright fringes (or adjacent dark fringes) is therefore

$$w = x_{n+1} - x_n = \frac{\lambda D}{a}$$

- $w$ is the fringe spacing (fringe width), in m.
- $\lambda$ is the wavelength, in m.
- $D$ is the slit-to-screen distance, in m.
- $a$ is the slit separation (centre to centre), in m.

The same formula gives the spacing of the dark fringes.

**Worked example:** In a double-slit experiment, ten fringes occupy a width of $1.5~\text{cm}$. The slit separation is $1.0~\text{mm}$ and the screen is $2.40~\text{m}$ from the slits. Calculate the wavelength.

1. Ten fringes span nine spaces: $w = \frac{1.5~\text{cm}}{9} = 0.167~\text{cm} = 1.67 \times 10^{-3}~\text{m}$.
2. Using the book's convention (width of 10 fringes divided by 10): $w = 1.5 \times 10^{-3}~\text{m}$.
3. $\lambda = \frac{wa}{D} = \frac{1.5 \times 10^{-3} \times 1.0 \times 10^{-3}}{2.40} = 6.25 \times 10^{-7}~\text{m}$.

**Answer:** $\lambda \approx 6.3 \times 10^{-7}~\text{m} = 630~\text{nm}$ (red light). The book divides the total width by 10; the difference from 9 is negligible at this precision, but in an exam count **spaces** if the wording says "between the first and tenth fringe".

**Measuring the quantities:**

- $a$: travelling microscope; measure between corresponding edges of the slits if the slits are equal in width (edge separation equals centre separation).
- $w$: measure across several fringes and divide by the number of spaces, to reduce percentage error.
- $D$: metre rule or tape.

**Improving accuracy:** use a laser (bright, monochromatic, coherent), increase $D$ so the fringes are further apart, measure many fringes, and darken the room. A laser also removes the need for the single slit.

### 1.7 White-light fringes

With white light, each wavelength forms its own fringe pattern. Because $w \propto \lambda$, red fringes are further from the centre than violet fringes.

- The **central fringe is white**, because at $x = 0$ the path difference is zero for every wavelength — all wavelengths interfere constructively there.
- The first few side fringes are **coloured**, with violet nearest the centre and red furthest out.
- Further from the centre the patterns from different wavelengths overlap and the fringes become blurred and eventually white again.

This is why white-light double-slit fringes are only visible for a few orders, and why a monochromatic filter (or laser) is used for measurements.

**Worked example:** In a double-slit experiment with red light ($\lambda = 600~\text{nm}$), the fringe spacing is $2.40~\text{mm}$. The red filter is replaced by a blue filter ($\lambda = 450~\text{nm}$). Calculate the new fringe spacing.

1. $w \propto \lambda$, so $\frac{w_{\text{blue}}}{w_{\text{red}}} = \frac{450}{600} = 0.75$.
2. $w_{\text{blue}} = 0.75 \times 2.40 = 1.80~\text{mm}$.

**Answer:** $1.80~\text{mm}$.

### 1.8 The diffraction grating

A **transmission diffraction grating** has many thousands of equally spaced parallel slits (or lines) per centimetre. Each slit diffracts the light, and the many diffracted beams interfere. The result is a series of very **sharp**, very **bright** maxima at predictable angles.

**The grating equation:**

$$d\sin\theta = n\lambda$$

- $d$ is the slit spacing (grating spacing), in m.
- $\theta$ is the angle between the straight-through direction and the $n$th-order maximum.
- $n$ is the order: $0, 1, 2, \dots$ ($n=0$ is the central maximum).
- $\lambda$ is the wavelength, in m.

If a grating has $N$ lines per metre, $d = \frac{1}{N}$. If it has $N$ lines per millimetre, $d = \frac{1}{N}~\text{mm} = \frac{10^{-3}}{N}~\text{m}$.

**Why the maxima are sharp:** for constructive interference, rays from **all** the slits must be in phase. This happens only at precise angles. Slightly away from the maximum, the contributions from the many slits progressively cancel, so the intensity falls to zero very quickly. With only two slits, the intensity varies slowly, giving broad fringes.

**Why the maxima are bright:** there are thousands of slits contributing in phase, so the resultant amplitude is thousands of times that from one slit.

**Maximum order:** since $\sin\theta \le 1$,

$$n_{\max} \le \frac{d}{\lambda}$$

The largest integer satisfying this is the highest order observed. The total number of maxima (including the central one and both sides) is $2n_{\max} + 1$.

**Worked example:** Monochromatic light is incident normally on a grating with $3000$ lines per cm. The first-order maximum is at $10.0^\circ$. Calculate the wavelength.

1. $d = \frac{1}{3000}~\text{cm} = 3.33 \times 10^{-4}~\text{cm} = 3.33 \times 10^{-6}~\text{m}$.
2. $\lambda = \frac{d\sin\theta}{n} = \frac{3.33 \times 10^{-6} \times \sin 10.0^\circ}{1}$.
3. $\lambda = 5.79 \times 10^{-7}~\text{m}$.

**Answer:** $\lambda \approx 5.8 \times 10^{-7}~\text{m} = 580~\text{nm}$ (yellow light).

**Worked example:** For the grating above, calculate the angle of the second-order maximum and determine the maximum order.

1. $\sin\theta_2 = \frac{2\lambda}{d} = \frac{2 \times 5.79 \times 10^{-7}}{3.33 \times 10^{-6}} = 0.348$.
2. $\theta_2 = 20.4^\circ$.
3. $\frac{d}{\lambda} = \frac{3.33 \times 10^{-6}}{5.79 \times 10^{-7}} = 5.75$, so $n_{\max} = 5$.
4. Total maxima $= 2(5)+1 = 11$.

**Answer:** $\theta_2 = 20.4^\circ$; maximum order $5$; 11 maxima.

### 1.9 White light and overlapping orders

With white light, the grating produces a **white central maximum** at $\theta = 0$ (all wavelengths in phase), and a spectrum on each side. Since $\sin\theta = \frac{n\lambda}{d}$, the angle increases with $\lambda$: **violet is closest to the centre and red furthest away**.

Higher-order spectra **overlap**: the red end of the second-order spectrum can occur at a larger angle than the violet end of the third-order spectrum. This is why only the first-order spectrum is usually clean and isolated.

**Worked example:** White light ($400$–$700~\text{nm}$) is incident on a grating with $d = 2.00 \times 10^{-6}~\text{m}$. Calculate the angular width of the first-order spectrum.

1. Violet: $\sin\theta = \frac{400 \times 10^{-9}}{2.00 \times 10^{-6}} = 0.200$, so $\theta = 11.5^\circ$.
2. Red: $\sin\theta = \frac{700 \times 10^{-9}}{2.00 \times 10^{-6}} = 0.350$, so $\theta = 20.5^\circ$.
3. Angular width $= 20.5 - 11.5 = 9.0^\circ$.

**Answer:** $9.0^\circ$.

### 1.10 Double slit versus diffraction grating

| Feature | Double slit | Diffraction grating |
|---|---|---|
| Number of slits | 2 | Thousands per cm |
| Fringe pattern | Equally spaced, broad | Sharp, bright maxima at angles |
| Measurement | Fringe spacing $w$ | Angle $\theta$ |
| Equation | $w = \frac{\lambda D}{a}$ | $d\sin\theta = n\lambda$ |
| Precision of $\lambda$ | Lower (small $a$, small $w$) | Higher ($d$ known precisely, $\theta$ large) |
| White light | Central white, a few coloured fringes | Central white, clear spectra; orders overlap at high $n$ |

### 1.11 Antiphase and noise cancellation

**Active noise cancellation** uses superposition deliberately. A microphone detects the incoming noise, an electronic circuit generates a signal of the **same frequency and amplitude** but **in antiphase** ($180^\circ$ phase difference), and a loudspeaker emits it. The two waves superpose destructively and the noise is reduced.

Conditions for good cancellation:

- Equal amplitudes (otherwise the minimum is $A_1 - A_2$, not zero).
- A constant $180^\circ$ phase difference at the listener's ear.
- The electronics must respond fast enough; this is easier at low frequencies, where the wavelength is long and a small timing error is a small fraction of a cycle.

**Worked example:** A noise wave of frequency $200~\text{Hz}$ travels at $340~\text{m s}^{-1}$. Calculate the shortest extra path length that would put a cancelling wave in antiphase.

1. $\lambda = \frac{v}{f} = \frac{340}{200} = 1.70~\text{m}$.
2. Antiphase requires a path difference of $\frac{\lambda}{2}$.
3. $\Delta x = \frac{1.70}{2} = 0.85~\text{m}$.

**Answer:** $0.85~\text{m}$ (or an odd multiple of $0.85~\text{m}$).

Other applications of antiphase superposition: **anti-reflection coatings** (reflected waves from the top and bottom surfaces of a thin film cancel when the film thickness is about $\frac{\lambda}{4}$ in the film), and **noise-cancelling headphones**.

## 2. Definition Sheet

> **Principle of superposition:** when two or more waves meet at a point, the resultant displacement is the algebraic sum of the displacements of the individual waves.

> **Interference:** the superposition of waves from two or more coherent sources, producing regions of constructive and destructive interference.

> **Constructive interference:** superposition of waves that arrive in phase, giving a resultant amplitude equal to the sum of the individual amplitudes; path difference $= n\lambda$.

> **Destructive interference:** superposition of waves that arrive in antiphase, giving a resultant amplitude equal to the difference of the individual amplitudes (zero if equal); path difference $= \left(n+\frac{1}{2}\right)\lambda$.

> **Coherence:** two sources are coherent when they emit waves with a constant phase difference; this requires the same frequency.

> **Path difference:** the difference in the distances travelled by two waves from their sources to a given point.

> **Phase difference:** the fraction of a cycle by which one oscillation leads or lags another; $\Delta\phi = 360^\circ \Delta x/\lambda$.

> **Fringe spacing (fringe width):** the distance between the centres of adjacent bright (or adjacent dark) fringes in an interference pattern; $w = \frac{\lambda D}{a}$.

> **Diffraction grating:** a device with many equally spaced parallel slits or lines, which diffracts light and produces sharp interference maxima according to $d\sin\theta = n\lambda$.

> **Order (of a maximum):** the integer $n$ in $d\sin\theta = n\lambda$, counting the number of wavelengths of path difference between adjacent slits; $n=0$ is the central maximum.

> **Dispersion (by a grating):** the separation of white light into its component wavelengths because the diffraction angle depends on $\lambda$.

## 3. Formula Sheet

**Quick reference:**

$$\Delta x = n\lambda \quad \text{(constructive)}, \qquad \Delta x = \left(n+\tfrac{1}{2}\right)\lambda \quad \text{(destructive)}, \qquad \Delta\phi = \frac{\Delta x}{\lambda}360^\circ, \qquad w = \frac{\lambda D}{a}, \qquad d\sin\theta = n\lambda, \qquad d = \frac{1}{N}$$

| Formula | Meaning of symbols | Units | When to use it |
|---|---|---|---|
| $$\Delta x = n\lambda$$ | $\Delta x$ path difference, $n$ integer, $\lambda$ wavelength | m | Constructive interference (sources in phase) |
| $$\Delta x = \left(n+\tfrac{1}{2}\right)\lambda$$ | as above | m | Destructive interference (sources in phase) |
| $$\Delta\phi = \frac{\Delta x}{\lambda}360^\circ$$ | $\Delta\phi$ phase difference, $\Delta x$ path difference | degrees | Convert path difference to phase difference |
| $$A_{\text{resultant}} = A_1 + A_2$$ | amplitudes of in-phase waves | m | Constructive interference |
| $$A_{\text{resultant}} = \lvert A_1 - A_2\rvert$$ | amplitudes of antiphase waves | m | Destructive interference (zero if $A_1 = A_2$) |
| $$w = \frac{\lambda D}{a}$$ | $w$ fringe spacing, $D$ slit–screen distance, $a$ slit separation | m | Young's double slit, small angles |
| $$\lambda = \frac{wa}{D}$$ | rearranged for wavelength | m | Calculating $\lambda$ from measured $w$, $a$, $D$ |
| $$d\sin\theta = n\lambda$$ | $d$ grating spacing, $\theta$ diffraction angle, $n$ order | m, degrees | Diffraction grating maxima |
| $$d = \frac{1}{N}$$ | $N$ lines per unit length | m | Grating spacing; convert $N$ to lines per metre first |
| $$n_{\max} \le \frac{d}{\lambda}$$ | highest observable order | — | Maximum order and total number of maxima |

**Exam facts:** $d\sin\theta = n\lambda$ is on the data sheet. $w = \frac{\lambda D}{a}$ is **not** — derive it from $\frac{ax}{D} = n\lambda$. The path-difference conditions are not printed; learn them with the words "whole number of wavelengths" and "odd number of half-wavelengths". $N$ lines per mm means $d = \frac{1}{N}~\text{mm} = \frac{10^{-3}}{N}~\text{m}$; a factor-of-1000 error here is the most common grating mistake.

## 4. Methods (Question Types & Methods)

### 1. Superposition at a point (amplitudes)

**Method:**
1. Find the phase difference (or path difference) at the point.
2. In phase: add amplitudes. In antiphase: subtract. Otherwise use a phasor/vector sum.
3. If the waves have equal amplitudes and are in antiphase, the resultant is zero.

**Traps:** adding intensities instead of amplitudes; assuming unequal amplitudes can cancel completely; forgetting that phase difference must be converted from path difference.

### 2. Decide constructive or destructive

**Method:**
1. Calculate $\frac{\Delta x}{\lambda}$.
2. If it is an integer, constructive. If it is a half-integer, destructive.
3. If the sources are in antiphase at emission, reverse the conclusion.
4. State the phase difference: $0^\circ$ (or $360^\circ$) for constructive, $180^\circ$ for destructive.

**Traps:** using the path difference in cm with $\lambda$ in m; forgetting the source-phase condition; saying "destructive" when the path difference is $2\lambda$ (that is constructive).

### 3. Two-source interference (sound/microwave)

**Method:**
1. Identify $a$ (source separation), $D$ (distance to the line of observation) and the spacing $w$ of adjacent maxima or minima.
2. Use $w = \frac{\lambda D}{a}$ and rearrange.
3. For a count of maxima, divide the total distance by $w$ and add 1 for the central maximum.

**Traps:** using the distance from one source instead of the perpendicular distance $D$; forgetting that the formula assumes $D \gg a$; counting minima as maxima.

### 4. Young's double slit — find $w$, $\lambda$, $a$ or $D$

**Method:**
1. Convert all lengths to metres (mm $\times 10^{-3}$, nm $\times 10^{-9}$).
2. If a total width across several fringes is given, divide by the number of **spaces**.
3. Use $w = \frac{\lambda D}{a}$ and rearrange.
4. Check the order of magnitude: visible wavelengths are $10^{-7}~\text{m}$, so $w$ is typically a few mm.

**Traps:** dividing by the number of fringes instead of spaces; using the slit width instead of the separation; mixing mm and m.

### 5. Diffraction grating — angle of a maximum

**Method:**
1. Calculate $d$ from $N$: $d = \frac{1}{N}$; convert to metres.
2. Use $\sin\theta = \frac{n\lambda}{d}$.
3. Take the inverse sine; quote the angle to a sensible number of significant figures.
4. Check $\sin\theta \le 1$; if not, that order does not exist.

**Traps:** using $N$ in lines per cm without converting; forgetting to take $\sin^{-1}$; using radians mode on the calculator; quoting the angle between the two first-order maxima as $\theta$ instead of $2\theta$.

### 6. Maximum order and number of maxima

**Method:**
1. Calculate $\frac{d}{\lambda}$.
2. $n_{\max}$ is the largest integer less than or equal to this value.
3. Total maxima $= 2n_{\max} + 1$ (central plus both sides).
4. If asked for the number on one side only, it is $n_{\max}$.

**Traps:** rounding $\frac{d}{\lambda}$ up; forgetting the central maximum; counting only one side.

### 7. White-light fringes and spectra

**Method:**
1. Central maximum is white (zero path difference for all $\lambda$).
2. For side fringes/spectra, use $w \propto \lambda$ or $\sin\theta \propto \lambda$.
3. Red is deviated most; violet least.
4. For overlapping orders, compare $n\lambda_{\text{red}}$ with $(n+1)\lambda_{\text{violet}}$.

**Traps:** saying red is closest to the centre (it is furthest); forgetting that the central fringe is white, not coloured; assuming orders never overlap.

### 8. Coherence and "explain why no pattern" questions

**Method:**
1. State that coherent sources have a constant phase difference (same frequency).
2. Explain that independent sources have randomly changing phase.
3. Conclude that the maxima and minima move rapidly and average out, so no steady pattern is seen.
4. For the school experiment, state that the single slit ensures the same wavefront reaches both slits.

**Traps:** saying "they have different wavelengths" when the frequencies are the same; omitting the averaging-out argument; forgetting the role of the single slit.

## 5. Solved Examples

### Example 1: Superposition of two waves

**Question:** Two waves of amplitude $4.0~\text{cm}$ and $1.0~\text{cm}$ meet (a) in phase, (b) in antiphase. Calculate the resultant amplitude in each case.

**Method:**
1. (a) $A = 4.0 + 1.0 = 5.0~\text{cm}$.
2. (b) $A = 4.0 - 1.0 = 3.0~\text{cm}$.

**Answer:** (a) $5.0~\text{cm}$; (b) $3.0~\text{cm}$.

### Example 2: Path difference condition

**Question:** Two coherent sources emit waves of wavelength $0.50~\text{m}$. At a point, the path difference is $3.0~\text{m}$. State the type of interference.

**Method:**
1. $\frac{3.0}{0.50} = 6.0$.
2. An integer number of wavelengths means the waves arrive in phase.

**Answer:** constructive interference.

### Example 3: Phase difference from path difference

**Question:** Two waves of wavelength $0.80~\text{m}$ have a path difference of $0.20~\text{m}$. Calculate the phase difference.

**Method:**
1. $\frac{\Delta x}{\lambda} = \frac{0.20}{0.80} = 0.25$.
2. $\Delta\phi = 0.25 \times 360^\circ = 90^\circ$.

**Answer:** $90^\circ$.

### Example 4: Two loudspeakers

**Question:** Two loudspeakers $2.0~\text{m}$ apart emit coherent sound of wavelength $0.40~\text{m}$. A listener walks along a line $10~\text{m}$ away. Calculate the spacing between adjacent quiet points.

**Method:**
1. $w = \frac{\lambda D}{a} = \frac{0.40 \times 10}{2.0}$.
2. $w = 2.0~\text{m}$.

**Answer:** $2.0~\text{m}$.

### Example 5: Young's double slit — fringe spacing

**Question:** Light of wavelength $589~\text{nm}$ passes through slits $0.20~\text{mm}$ apart. The screen is $1.20~\text{m}$ away. Calculate the fringe separation.

**Method:**
1. $w = \frac{\lambda D}{a} = \frac{589 \times 10^{-9} \times 1.20}{0.20 \times 10^{-3}}$.
2. $w = 3.53 \times 10^{-3}~\text{m}$.

**Answer:** $w = 3.5~\text{mm}$.

### Example 6: Young's double slit — wavelength

**Question:** In a double-slit experiment, the distance between the first and eleventh bright fringes is $15.0~\text{mm}$. The slit separation is $0.50~\text{mm}$ and $D = 1.50~\text{m}$. Calculate $\lambda$.

**Method:**
1. Ten spaces: $w = \frac{15.0}{10} = 1.50~\text{mm} = 1.50 \times 10^{-3}~\text{m}$.
2. $\lambda = \frac{wa}{D} = \frac{1.50 \times 10^{-3} \times 0.50 \times 10^{-3}}{1.50}$.
3. $\lambda = 5.0 \times 10^{-7}~\text{m}$.

**Answer:** $\lambda = 5.0 \times 10^{-7}~\text{m} = 500~\text{nm}$.

### Example 7: Effect of changing $D$

**Question:** In Example 5, the screen is moved to $2.40~\text{m}$ from the slits. Calculate the new fringe spacing.

**Method:**
1. $w \propto D$, so $w$ doubles.
2. $w = 2 \times 3.53 = 7.06~\text{mm}$.

**Answer:** $w \approx 7.1~\text{mm}$.

### Example 8: Grating wavelength

**Question:** A grating has $5000$ lines per cm. The first-order maximum is at $17.0^\circ$. Calculate the wavelength.

**Method:**
1. $d = \frac{1}{5000}~\text{cm} = 2.0 \times 10^{-4}~\text{cm} = 2.0 \times 10^{-6}~\text{m}$.
2. $\lambda = d\sin\theta = 2.0 \times 10^{-6} \times \sin 17.0^\circ$.
3. $\lambda = 5.85 \times 10^{-7}~\text{m}$.

**Answer:** $\lambda \approx 585~\text{nm}$.

### Example 9: Grating angle and maximum order

**Question:** A grating has $400$ lines per mm. Light of wavelength $600~\text{nm}$ is used. Calculate (a) the first-order angle, (b) the maximum order.

**Method:**
1. $d = \frac{1}{400}~\text{mm} = 2.5 \times 10^{-6}~\text{m}$.
2. (a) $\sin\theta = \frac{600 \times 10^{-9}}{2.5 \times 10^{-6}} = 0.240$, so $\theta = 13.9^\circ$.
3. (b) $\frac{d}{\lambda} = \frac{2.5 \times 10^{-6}}{600 \times 10^{-9}} = 4.17$, so $n_{\max} = 4$.
4. Total maxima $= 2(4)+1 = 9$.

**Answer:** (a) $13.9^\circ$; (b) $n_{\max} = 4$, 9 maxima.

### Example 10: White-light grating

**Question:** White light ($400$–$700~\text{nm}$) is incident on a grating with $d = 1.50 \times 10^{-6}~\text{m}$. Calculate the angular width of the first-order spectrum.

**Method:**
1. Violet: $\sin\theta = \frac{400 \times 10^{-9}}{1.50 \times 10^{-6}} = 0.267$, so $\theta = 15.5^\circ$.
2. Red: $\sin\theta = \frac{700 \times 10^{-9}}{1.50 \times 10^{-6}} = 0.467$, so $\theta = 27.8^\circ$.
3. Width $= 27.8 - 15.5 = 12.3^\circ$.

**Answer:** $12^\circ$.

### Example 11: Noise cancellation path difference

**Question:** A cancelling signal must be $180^\circ$ out of phase with a $500~\text{Hz}$ noise. The speed of sound is $340~\text{m s}^{-1}$. Calculate the shortest extra path length required.

**Method:**
1. $\lambda = \frac{340}{500} = 0.680~\text{m}$.
2. $\Delta x = \frac{\lambda}{2} = 0.340~\text{m}$.

**Answer:** $0.34~\text{m}$ (or $0.34 + n\lambda$).

### Example 12: Counting maxima

**Question:** Microwaves of wavelength $3.0~\text{cm}$ pass through two gaps $12.0~\text{cm}$ apart. A detector moves along a line $1.20~\text{m}$ away from the midpoint, from the central maximum to $2.16~\text{m}$ to one side. Calculate the number of maxima crossed.

**Method:**
1. $w = \frac{\lambda D}{a} = \frac{0.030 \times 1.20}{0.120} = 0.30~\text{m}$.
2. Number of spaces $= \frac{2.16}{0.30} = 7.2$.
3. Maxima crossed $= 7$ (the eighth would be at $2.40~\text{m}$).

**Answer:** 7 maxima.

## 6. Exam-Style Questions (Full Solutions)

### Question 1

Two coherent waves of equal amplitude meet at a point. Explain what is meant by coherent, and state the conditions for (a) constructive and (b) destructive interference in terms of path difference.

**Solution:**
1. Coherent: the waves have a constant phase difference (same frequency).
2. (a) Constructive: path difference $= n\lambda$; waves arrive in phase and displacements add.
3. (b) Destructive: path difference $= \left(n+\frac{1}{2}\right)\lambda$; waves arrive in antiphase and displacements cancel.

**Answer:** as above; the phase conditions are $0^\circ$ and $180^\circ$ respectively.

### Question 2

A student sets up a double-slit experiment with a laser of wavelength $632.8~\text{nm}$. The slits are $0.25~\text{mm}$ apart and the screen is $2.00~\text{m}$ away. (a) Calculate the fringe spacing. (b) The student measures the distance across 20 fringes as $98~\text{mm}$. Calculate the experimental value of $\lambda$. (c) Suggest one reason for the difference.

**Solution:**
1. (a) $w = \frac{632.8 \times 10^{-9} \times 2.00}{0.25 \times 10^{-3}} = 5.06 \times 10^{-3}~\text{m}$.
2. (b) 20 fringes span 19 spaces: $w = \frac{98}{19} = 5.16~\text{mm}$.
3. $\lambda = \frac{wa}{D} = \frac{5.16 \times 10^{-3} \times 0.25 \times 10^{-3}}{2.00} = 6.45 \times 10^{-7}~\text{m}$.
4. (c) The measured width includes the finite width of the fringes, and the slit separation may differ slightly from its nominal value; also the screen distance is measured to the screen surface, not the fringe plane.

**Answer:** (a) $5.06~\text{mm}$; (b) $6.45 \times 10^{-7}~\text{m}$; (c) measurement uncertainty in $a$, $D$ or the fringe positions.

### Question 3

A diffraction grating has $600$ lines per mm. Light of wavelength $550~\text{nm}$ is incident normally. (a) Calculate the angle of the second-order maximum. (b) Determine the highest order visible. (c) State two advantages of a grating over a double slit for measuring wavelength.

**Solution:**
1. (a) $d = \frac{1}{600}~\text{mm} = 1.667 \times 10^{-6}~\text{m}$.
2. $\sin\theta_2 = \frac{2 \times 550 \times 10^{-9}}{1.667 \times 10^{-6}} = 0.660$, so $\theta_2 = 41.3^\circ$.
3. (b) $\frac{d}{\lambda} = \frac{1.667 \times 10^{-6}}{550 \times 10^{-9}} = 3.03$, so $n_{\max} = 3$.
4. (c) The maxima are sharper and brighter, and the angles are larger, so $\theta$ and $d$ can be measured more precisely; this gives a more accurate $\lambda$.

**Answer:** (a) $41.3^\circ$; (b) $n_{\max} = 3$; (c) sharper/bright maxima and more precise angle measurement.

### Question 4

White light passes through a double slit. Describe the appearance of the fringe pattern and explain why the central fringe is white.

**Solution:**
1. The central fringe is white and bright.
2. On either side there are coloured fringes, with violet nearest the centre and red furthest away.
3. The coloured fringes overlap and blur after a few orders.
4. Explanation: at the centre the path difference is zero for every wavelength, so all wavelengths interfere constructively. Away from the centre, $w = \frac{\lambda D}{a}$ is larger for longer wavelengths, so red is displaced further than violet.

**Answer:** white centre, coloured fringes with red outermost; zero path difference at the centre for all $\lambda$.

### Question 5

Two microwave sources $12.5~\text{cm}$ apart emit coherent waves of wavelength $1.5~\text{cm}$. A detector is $1.2~\text{m}$ from the midpoint and is moved $4.50~\text{m}$ parallel to the sources. Calculate the number of maxima detected and the frequency of the microwaves.

**Solution:**
1. $w = \frac{\lambda D}{a} = \frac{0.015 \times 1.2}{0.125} = 0.144~\text{m}$.
2. Number of spaces across the full $4.50~\text{m}$: $\frac{4.50}{0.144} = 31.25$.
3. Maxima: the central maximum plus 15 each side gives about 31; the detector crosses 31 maxima.
4. $f = \frac{c}{\lambda} = \frac{3.0 \times 10^8}{0.015} = 2.0 \times 10^{10}~\text{Hz}$.

**Answer:** about 31 maxima; $f = 2.0 \times 10^{10}~\text{Hz}$ ($20~\text{GHz}$).

### Question 6

Explain how active noise cancellation uses superposition, and state two conditions necessary for it to work well.

**Solution:**
1. A microphone detects the noise and a circuit generates a wave of the same frequency and amplitude but in antiphase.
2. The two waves superpose; their displacements cancel (destructive interference), reducing the sound.
3. Conditions: equal amplitudes at the listener's ear, and a stable $180^\circ$ phase difference (the electronics must respond within a fraction of a period).
4. It works best for low-frequency, steady noise, where the wavelength is long and the required timing accuracy is less demanding.

**Answer:** generate an antiphase wave of equal amplitude; destructive superposition cancels the noise; needs equal amplitudes and stable $180^\circ$ phase.

## 7. Cheat Sheet

**Core ideas:**
- Superposition: displacements add algebraically.
- Constructive: path difference $= n\lambda$, phase $0^\circ$.
- Destructive: path difference $= (n+\frac{1}{2})\lambda$, phase $180^\circ$.
- Coherent: constant phase difference, same frequency.
- Two independent lamps are not coherent; a single slit before a double slit makes the two slits coherent.

**Formulas:**
- $\Delta\phi = 360^\circ \Delta x/\lambda$.
- Double slit: $w = \frac{\lambda D}{a}$ (derive from $\frac{ax}{D} = n\lambda$).
- Grating: $d\sin\theta = n\lambda$; $d = 1/N$; $n_{\max} \le d/\lambda$.
- Total grating maxima $= 2n_{\max} + 1$.

**White light:**
- Central fringe white (zero path difference for all $\lambda$).
- Red furthest from centre, violet nearest.
- Grating spectra: red at larger angle; higher orders overlap.

**Rules that win marks:**
- Destructive needs **odd** number of half-wavelengths.
- Unequal amplitudes cannot cancel completely.
- In fringe measurements, count **spaces**, not fringes.
- Grating $N$ lines per mm: $d = 10^{-3}/N$ m.
- Coherence explanation must mention **constant phase difference**, not just "same wavelength".

## 8. Common Exam Mistakes

1. **Using $n\lambda$ for destructive interference.** Constructive is $n\lambda$; destructive is $(n+\frac{1}{2})\lambda$. Mixing them reverses the whole answer.
2. **Forgetting the source phase.** If the sources are in antiphase at emission, the conditions swap. Read the question for "in phase" or "antiphase" at the sources.
3. **Adding intensities rather than amplitudes.** Superposition adds displacements/amplitudes; intensity is proportional to amplitude squared. Two equal coherent waves in phase give **four times** the intensity of one, not twice.
4. **Claiming complete cancellation with unequal amplitudes.** The minimum amplitude is $|A_1 - A_2|$, which is zero only if the amplitudes are equal.
5. **Counting fringes instead of spaces.** The distance from the first to the $n$th fringe contains $n-1$ spaces. This is the most common double-slit arithmetic error.
6. **Using slit width instead of slit separation.** $a$ is the centre-to-centre separation, not the width of either slit.
7. **Grating unit errors.** $N$ lines per mm gives $d = 10^{-3}/N$ m; $N$ lines per cm gives $d = 10^{-2}/N$ m. A factor of 10 or 1000 error follows if this is rushed.
8. **Forgetting $\sin\theta \le 1$.** If $\frac{n\lambda}{d} > 1$, that order does not exist; the maximum order is the largest integer below $d/\lambda$.
9. **Quoting the angle between two maxima as $\theta$.** The grating equation gives the angle from the central maximum; the angle between the $+n$ and $-n$ maxima is $2\theta$.
10. **Saying red is closest to the centre in a grating spectrum.** Since $\sin\theta \propto \lambda$, red is deviated most and is furthest from the centre; violet is closest.
11. **Saying two lamps are coherent because they have the same frequency.** Coherence requires a **constant phase difference**; independent lamps have random, rapidly changing phase.
12. **Forgetting the central white fringe.** In white-light interference the centre is white, not coloured, because the path difference is zero for all wavelengths there.
