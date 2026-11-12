# Chapter 13: Waves - CAIE A Level Physics (9702) Study Notes

Exam-focused revision notes for Cambridge International AS & A Level Physics 9702, covering the wave content of Chapter 13: progressive waves, transverse and longitudinal motion, the wave equation, intensity, polarisation, diffraction, interference, the double slit and diffraction grating, the electromagnetic spectrum and the Doppler effect. This material appears in Paper 1 multiple choice, Paper 2 structured questions and Paper 4; the calculations are also examined through practical work in Paper 3. Definitions are worded for mark schemes, and every theory section ends with a worked example. Use $c = 3.0 \times 10^8~\text{m s}^{-1}$ and the speed of sound in air as $330~\text{m s}^{-1}$ unless told otherwise.

## 1. Theory

### 1.1 Progressive waves and the basic quantities

A **progressive wave** is a disturbance that transfers **energy** (not matter) from one place to another without the medium itself travelling. The particles of the medium oscillate about fixed equilibrium positions; each particle passes energy to its neighbour.

| Quantity | Symbol | Meaning | Unit |
|---|---|---|---|
| Displacement | $x$ | distance of a point from its undisturbed position | m |
| Amplitude | $A$ | maximum displacement from equilibrium | m |
| Wavelength | $\lambda$ | distance between two consecutive points with the same displacement and phase | m |
| Period | $T$ | time for one complete oscillation | s |
| Frequency | $f$ | number of oscillations per unit time | Hz |
| Wave speed | $v$ | distance travelled by the wave per unit time | $\text{m s}^{-1}$ |

$$f = \frac{1}{T} \qquad \text{and} \qquad v = f\lambda$$

**Wave speed** is the speed at which the **wave profile** (and energy) travels, not the speed of the particles. For a water wave the water particles move up and down (and slightly forwards and backwards); the wave crest moves horizontally.

**Worked example:** A sound wave has frequency $440~\text{Hz}$ and wavelength $0.75~\text{m}$. Calculate its speed.

1. $v = f\lambda = 440 \times 0.75 = 330~\text{m s}^{-1}$.

**Answer:** $v = 330~\text{m s}^{-1}$.

### 1.2 Transverse and longitudinal waves

**Transverse wave:** the particles of the medium oscillate **perpendicular** to the direction of energy transfer. Examples: all electromagnetic waves, waves on a string, seismic S-waves, water surface waves (approximately).

**Longitudinal wave:** the particles oscillate **parallel** to the direction of energy transfer, producing regions of **compression** (high pressure/density) and **rarefaction** (low pressure/density). Examples: sound waves, seismic P-waves, waves on a slinky pushed back and forth.

**Key consequences:**

- Only **transverse** waves can be polarised. Longitudinal waves cannot, because their oscillations are already along one line.
- Sound waves cannot be polarised, so polaroid sunglasses do not reduce sound.
- Both types obey $v = f\lambda$ and both transfer energy without transferring matter.

A longitudinal wave is often drawn as a sine curve: the displacement axis represents the displacement of particles from equilibrium, not a transverse physical displacement.

**Worked example:** A sound wave travels through steel at $5060~\text{m s}^{-1}$ with wavelength $0.25~\text{m}$. Calculate its frequency.

1. $f = \frac{v}{\lambda} = \frac{5060}{0.25} = 2.024 \times 10^4~\text{Hz}$.

**Answer:** $f \approx 2.0 \times 10^4~\text{Hz} = 20~\text{kHz}$ (just above the upper limit of human hearing).

### 1.3 Displacement–distance and displacement–time graphs

- A **displacement–distance** graph is a "snapshot" of the whole wave at one instant. The horizontal separation between two adjacent crests is $\lambda$.
- A **displacement–time** graph shows the motion of **one point** as time passes. The horizontal separation between two adjacent crests is $T$.

Do not read a wavelength from a displacement–time graph unless you convert time to distance using $v$.

**Phase and phase difference:** two points are **in phase** if they oscillate in step (same displacement and same direction of motion). Points separated by $n\lambda$ are in phase. The **phase difference** $\Delta\phi$ between two points separated by a distance $\Delta x$ is

$$\Delta\phi = \frac{\Delta x}{\lambda} \times 360^\circ = \frac{2\pi\,\Delta x}{\lambda}~\text{rad}$$

So a separation of $\frac{\lambda}{4}$ corresponds to $90^\circ$ ($\frac{\pi}{2}$ rad); $\frac{\lambda}{2}$ corresponds to $180^\circ$ ($\pi$ rad) — the points are **in antiphase**.

**Worked example:** Two points on a wave are separated by $0.15~\text{m}$. The wavelength is $0.60~\text{m}$. Calculate the phase difference.

1. $\frac{\Delta x}{\lambda} = \frac{0.15}{0.60} = 0.25$.
2. $\Delta\phi = 0.25 \times 360^\circ = 90^\circ$ (or $\pi/2$ rad).

**Answer:** $90^\circ$.

### 1.4 Measuring frequency with a cathode-ray oscilloscope

A microphone converts the sound into a varying voltage, which the c.r.o. displays. The **time-base** sets the time represented by one horizontal division. The period is the number of divisions for one complete wave multiplied by the time-base setting:

$$T = (\text{divisions per cycle}) \times (\text{time per division})$$

Then $f = \frac{1}{T}$.

**Worked example:** A c.r.o. trace shows one complete wave occupying $4.0$ divisions. The time-base is $2.5~\text{ms div}^{-1}$. Calculate the frequency.

1. $T = 4.0 \times 2.5~\text{ms} = 10~\text{ms} = 1.0 \times 10^{-2}~\text{s}$.
2. $f = \frac{1}{1.0 \times 10^{-2}} = 100~\text{Hz}$.

**Answer:** $f = 100~\text{Hz}$.

### 1.5 Intensity

**Intensity** is the rate of energy transfer (power) per unit area **at right angles to the direction of wave travel**:

$$I = \frac{P}{A}$$

- $I$ is intensity, in $\text{W m}^{-2}$.
- $P$ is power, in W.
- $A$ is the area perpendicular to the wave direction, in $\text{m}^2$.

For a point source radiating equally in all directions, the power spreads over a sphere of area $4\pi r^2$, so

$$I = \frac{P}{4\pi r^2} \qquad \Rightarrow \qquad I \propto \frac{1}{r^2}$$

This is the **inverse-square law**: doubling the distance quarters the intensity.

**Intensity and amplitude:** for a wave, intensity is proportional to the square of the amplitude:

$$I \propto A^2$$

So doubling the amplitude quadruples the intensity; reducing the amplitude to one third reduces the intensity to one ninth.

**Worked example:** A $100~\text{W}$ lamp radiates equally in all directions. Calculate the intensity at $2.0~\text{m}$.

1. Area of sphere: $A = 4\pi(2.0)^2 = 50.3~\text{m}^2$.
2. $I = \frac{100}{50.3} = 1.99~\text{W m}^{-2}$.

**Answer:** $I = 2.0~\text{W m}^{-2}$.

**Worked example:** A wave has amplitude $5.0~\text{cm}$ and intensity $400~\text{W m}^{-2}$. Its amplitude is increased to $10.0~\text{cm}$. Calculate the new intensity.

1. Amplitude doubles, so $I$ increases by $2^2 = 4$.
2. $I = 4 \times 400 = 1600~\text{W m}^{-2}$.

**Answer:** $1600~\text{W m}^{-2}$.

### 1.6 Polarisation and Malus's law

**Polarisation** is the restriction of the oscillations of a transverse wave to **one plane**. Natural light from a lamp is **unpolarised**: its electric field oscillates in all planes perpendicular to the direction of travel. A **polaroid** filter transmits only the component oscillating along its transmission axis, so the emerging light is **plane-polarised**.

- Rotating a second polaroid (**analyser**) changes the transmitted intensity.
- When the analyser is parallel to the polariser, transmission is maximum; when crossed ($90^\circ$), transmission is (ideally) zero.
- **Longitudinal waves cannot be polarised** — this is direct evidence that sound is longitudinal and light is transverse.

For **polarised** light of intensity $I_0$ incident on an analyser whose axis is at angle $\theta$ to the plane of polarisation:

$$I = I_0\cos^2\theta \qquad \text{(Malus's law)}$$

For **unpolarised** light incident on the first polariser, the transmitted intensity is $\frac{I_0}{2}$ (half the light is absorbed, on average), and the emergent light is polarised.

**Worked example:** Plane-polarised light of intensity $80~\text{W m}^{-2}$ falls on an analyser whose axis is at $30^\circ$ to the plane of polarisation. Calculate the transmitted intensity.

1. $I = I_0\cos^2\theta = 80 \times \cos^2 30^\circ$.
2. $\cos 30^\circ = 0.866$, so $\cos^2 30^\circ = 0.75$.
3. $I = 80 \times 0.75 = 60~\text{W m}^{-2}$.

**Answer:** $60~\text{W m}^{-2}$.

**Worked example:** Unpolarised light of intensity $80~\text{W m}^{-2}$ passes through a polariser and then an analyser at $60^\circ$ to the polariser. Calculate the final intensity.

1. After the polariser: $I_1 = \frac{80}{2} = 40~\text{W m}^{-2}$.
2. After the analyser: $I_2 = 40\cos^2 60^\circ = 40 \times 0.25 = 10~\text{W m}^{-2}$.

**Answer:** $10~\text{W m}^{-2}$.

**Applications:** polaroid sunglasses reduce glare because light reflected from water or roads is partially polarised; liquid-crystal displays use polarising filters; stress analysis of transparent plastics uses polarised light.

### 1.7 Diffraction

**Diffraction** is the **spreading of waves** as they pass through a gap or around an obstacle. The amount of spreading depends on the ratio of wavelength to gap width:

- Gap much larger than $\lambda$: little spreading; the wave travels almost straight through.
- Gap comparable to $\lambda$: pronounced spreading; the wave emerges as a broad circular (or semicircular) pattern.
- Gap smaller than $\lambda$: the wave spreads out almost uniformly.

**Diffraction is not the same as refraction.** Refraction is a change of speed and direction at a boundary between media; diffraction is spreading without a change of medium.

**Diffraction grating:** many narrow, equally spaced slits. Each slit diffracts light, and the diffracted waves superpose. Because there are many slits, the maxima are very **sharp** and **bright**, and the positions are predictable. The condition for a maximum is

$$d\sin\theta = n\lambda$$

- $d$ is the slit spacing (grating constant), in m. If a grating has $N$ lines per metre, $d = \frac{1}{N}$; for $N$ lines per mm, $d = \frac{1}{N}~\text{mm}$.
- $\theta$ is the angle between the straight-through direction and the $n$th-order maximum.
- $n$ is the order ($0, 1, 2, \dots$); $n=0$ is the central maximum.
- $\lambda$ is the wavelength, in m.

**Maximum order:** since $\sin\theta \le 1$, $n \le \frac{d}{\lambda}$. The highest observable order is the largest integer satisfying this.

**Worked example:** A grating has $500$ lines per mm. Light of wavelength $600~\text{nm}$ is incident normally. Calculate the angles of the first three orders and the maximum order.

1. $d = \frac{1}{500}~\text{mm} = 2.0 \times 10^{-6}~\text{m}$.
2. $n=1$: $\sin\theta = \frac{600 \times 10^{-9}}{2.0 \times 10^{-6}} = 0.30$, so $\theta = 17.5^\circ$.
3. $n=2$: $\sin\theta = 0.60$, so $\theta = 36.9^\circ$.
4. $n=3$: $\sin\theta = 0.90$, so $\theta = 64.2^\circ$.
5. $n=4$ would need $\sin\theta = 1.20 > 1$, which is impossible, so the maximum order is $3$.

**Answer:** $17.5^\circ$, $36.9^\circ$, $64.2^\circ$; maximum order $3$.

### 1.8 Interference, coherence and path difference

**Superposition:** when two waves meet at a point, the resultant displacement is the **vector sum** of the individual displacements.

**Interference** is the superposition of waves from two or more sources, producing regions of **constructive** and **destructive** interference.

- **Constructive interference:** waves arrive **in phase**; displacements add; path difference $= n\lambda$; phase difference $= 0, 360^\circ, \dots$
- **Destructive interference:** waves arrive **in antiphase**; displacements cancel; path difference $= \left(n + \frac{1}{2}\right)\lambda$; phase difference $= 180^\circ, 540^\circ, \dots$

**Coherence:** two waves are coherent if they have a **constant phase difference**. This requires the same frequency (and, in practice, a stable source). Two separate lamps are not coherent because their emissions are random and the phase difference changes rapidly; the interference pattern averages out.

**Path difference** $\Delta x$ is the difference in distance travelled by the two waves from their sources to the point. It is related to phase difference by

$$\frac{\Delta\phi}{360^\circ} = \frac{\Delta x}{\lambda}$$

**Worked example:** Two coherent waves of wavelength $0.40~\text{m}$ arrive at a point with path difference $0.60~\text{m}$. State whether the interference is constructive or destructive.

1. $\frac{\Delta x}{\lambda} = \frac{0.60}{0.40} = 1.5$.
2. A path difference of $1.5\lambda = \left(1+\frac{1}{2}\right)\lambda$, so the waves are in antiphase.

**Answer:** destructive interference.

### 1.9 Young's double-slit experiment

Light from a single source passes through two narrow, closely spaced slits $S_1$ and $S_2$. The slits act as **coherent** sources (the same wavefront reaches both). The light from the two slits overlaps on a screen and produces a pattern of equally spaced bright and dark **fringes**.

**Derivation of the fringe spacing.** Let the slit separation be $a$, the distance from the slits to the screen be $D$, and the position of the $n$th bright fringe be $x_n$ measured from the centre. For small angles, the path difference from the two slits to the point on the screen is approximately

$$\Delta x \approx \frac{a x_n}{D}$$

For a bright fringe, $\Delta x = n\lambda$, so

$$x_n = \frac{n\lambda D}{a}$$

The spacing between adjacent bright (or dark) fringes is therefore

$$w = \frac{\lambda D}{a}$$

- $w$ is the fringe spacing, in m.
- $\lambda$ is the wavelength, in m.
- $D$ is the slit-to-screen distance, in m.
- $a$ is the slit separation, in m.

**Conditions for a visible pattern:** the slits must be coherent, close together (small $a$), and the screen far away (large $D$); the light must be monochromatic (single wavelength).

**Worked example:** In a double-slit experiment, $\lambda = 590~\text{nm}$, $a = 0.50~\text{mm}$ and $D = 1.5~\text{m}$. Calculate the fringe spacing.

1. Convert: $\lambda = 5.90 \times 10^{-7}~\text{m}$, $a = 5.0 \times 10^{-4}~\text{m}$.
2. $w = \frac{\lambda D}{a} = \frac{5.90 \times 10^{-7} \times 1.5}{5.0 \times 10^{-4}}$.
3. $w = 1.77 \times 10^{-3}~\text{m} = 1.8~\text{mm}$.

**Answer:** $w = 1.8~\text{mm}$.

**Worked example:** In a double-slit experiment, the distance between the centres of the first and fifth bright fringes is $4.8~\text{mm}$. The slit separation is $0.30~\text{mm}$ and the screen is $0.80~\text{m}$ away. Calculate the wavelength.

1. Four fringe spacings span the first to fifth fringe: $w = \frac{4.8}{4} = 1.2~\text{mm} = 1.2 \times 10^{-3}~\text{m}$.
2. $\lambda = \frac{wa}{D} = \frac{1.2 \times 10^{-3} \times 0.30 \times 10^{-3}}{0.80}$.
3. $\lambda = 4.5 \times 10^{-7}~\text{m} = 450~\text{nm}$.

**Answer:** $\lambda = 4.5 \times 10^{-7}~\text{m}$ (blue light).

**White-light fringes:** with white light, each wavelength produces its own fringe pattern. The central fringe is **white** (all wavelengths have zero path difference there), and the other fringes are coloured, with red furthest from the centre (since $w \propto \lambda$). The patterns overlap after a few fringes and appear white again.

### 1.10 The electromagnetic spectrum

All electromagnetic waves are **transverse** oscillations of electric and magnetic fields, at right angles to each other and to the direction of travel. In a vacuum they all travel at

$$c = 3.00 \times 10^8~\text{m s}^{-1}$$

and obey $c = f\lambda$. The bands, in order of **increasing wavelength** (decreasing frequency), are: gamma rays, X-rays, ultraviolet, visible, infrared, microwaves, radio waves.

| Band | Typical wavelength range / m | Typical frequency range / Hz |
|---|---|---|
| Gamma rays | $10^{-16}$ to $10^{-10}$ | $10^{18}$ to $10^{24}$ |
| X-rays | $10^{-13}$ to $10^{-8}$ | $10^{16}$ to $10^{21}$ |
| Ultraviolet | $10^{-8}$ to $4 \times 10^{-7}$ | $7.5 \times 10^{14}$ to $3 \times 10^{16}$ |
| Visible | $4 \times 10^{-7}$ (violet) to $7 \times 10^{-7}$ (red) | $4.3 \times 10^{14}$ to $7.5 \times 10^{14}$ |
| Infrared | $7 \times 10^{-7}$ to $10^{-3}$ | $3 \times 10^{11}$ to $4.3 \times 10^{14}$ |
| Microwaves | $10^{-3}$ to $10^{-1}$ | $3 \times 10^{9}$ to $3 \times 10^{11}$ |
| Radio waves | $10^{-1}$ to $>10^{6}$ | $<3 \times 10^{9}$ |

**Notes:**

- The boundaries are **arbitrary and overlap** (X-rays and gamma rays overlap around $10^{-10}$ to $10^{-13}~\text{m}$). The distinction is their **origin**: X-rays come from decelerating electrons; gamma rays come from nuclear transitions.
- Wavelength depends on the medium; **frequency is fixed** by the source. When light enters glass, $v$ and $\lambda$ decrease but $f$ is unchanged.
- Visible light is roughly $400$–$700~\text{nm}$, i.e. $4$–$7 \times 10^{-7}~\text{m}$.

**Worked example:** Calculate the frequency of light of wavelength $500~\text{nm}$ in a vacuum and state the band.

1. $\lambda = 500 \times 10^{-9} = 5.0 \times 10^{-7}~\text{m}$.
2. $f = \frac{c}{\lambda} = \frac{3.0 \times 10^8}{5.0 \times 10^{-7}} = 6.0 \times 10^{14}~\text{Hz}$.
3. This lies in the visible range (green light).

**Answer:** $f = 6.0 \times 10^{14}~\text{Hz}$; visible.

**Worked example:** A microwave has wavelength $3.0~\text{cm}$. Calculate its frequency.

1. $\lambda = 3.0 \times 10^{-2}~\text{m}$.
2. $f = \frac{3.0 \times 10^8}{3.0 \times 10^{-2}} = 1.0 \times 10^{10}~\text{Hz} = 10~\text{GHz}$.

**Answer:** $f = 1.0 \times 10^{10}~\text{Hz}$.

### 1.11 The Doppler effect

The **Doppler effect** is the change in observed frequency (and wavelength) when there is relative motion between a source and an observer.

For a source moving with speed $v_s$ through a medium in which the wave speed is $v$:

$$f_o = f_s\frac{v}{v \pm v_s}$$

- Use the **minus** sign when the source is **approaching**: the waves are compressed, $\lambda$ is shorter, $f_o > f_s$.
- Use the **plus** sign when the source is **receding**: the waves are stretched, $\lambda$ is longer, $f_o < f_s$.

The source frequency $f_s$ and the wave speed $v$ are **unchanged**; only the observed wavelength and frequency change. The formula assumes the observer is stationary and $v_s \ll v$.

**Worked example:** A train whistle emits $800~\text{Hz}$ and the train approaches at $60~\text{m s}^{-1}$. The speed of sound is $330~\text{m s}^{-1}$. Calculate the observed frequency.

1. Approaching, so use the minus sign: $f_o = 800 \times \frac{330}{330-60}$.
2. $f_o = 800 \times \frac{330}{270} = 978~\text{Hz}$.

**Answer:** $f_o \approx 9.8 \times 10^2~\text{Hz}$.

**Red shift:** for light from a receding source, the observed wavelength increases ($\Delta\lambda > 0$). For speeds much less than $c$:

$$\frac{\Delta\lambda}{\lambda} \approx \frac{v_s}{c}$$

Longer wavelengths are towards the red end of the spectrum, so a receding star's light is **red-shifted**. The greater the red shift, the faster the star is receding.

**Worked example:** A spectral line of laboratory wavelength $535~\text{nm}$ is observed at $550~\text{nm}$ from a distant star. Calculate the star's speed and direction.

1. $\Delta\lambda = 550 - 535 = 15~\text{nm}$.
2. $\frac{\Delta\lambda}{\lambda} = \frac{15}{535} = 0.0280$.
3. $v_s = c\frac{\Delta\lambda}{\lambda} = 3.0 \times 10^8 \times 0.0280 = 8.4 \times 10^6~\text{m s}^{-1}$.
4. The wavelength has **increased**, so the star is **receding**.

**Answer:** $v_s \approx 8.4 \times 10^6~\text{m s}^{-1}$ away from the observer.

### 1.12 Stationary and progressive waves compared

A **stationary (standing) wave** is formed when two progressive waves of the same frequency and amplitude travel in opposite directions and superpose (for example, an incident wave and its reflection). It has fixed **nodes** (zero amplitude) and **antinodes** (maximum amplitude). Chapter 15 treats stationary waves in detail; the comparison is examinable here.

| Feature | Progressive wave | Stationary wave |
|---|---|---|
| Energy transfer | Transfers energy along the wave | No net energy transfer |
| Amplitude | Same for all particles (ideal) | Varies from zero at nodes to maximum at antinodes |
| Wavelength | Distance between adjacent crests | Twice the distance between adjacent nodes |
| Phase | Varies continuously along the wave | All points between adjacent nodes are in phase; points either side of a node are in antiphase |
| Frequency | All particles oscillate at $f$ | All particles oscillate at $f$ |
| Waveform | Travels | Does not move; fixed envelope |

## 2. Definition Sheet

> **Progressive wave:** a wave that transfers energy from one place to another without transferring matter, by the oscillation of particles about fixed equilibrium positions.

> **Transverse wave:** a wave in which the particles of the medium oscillate perpendicular to the direction of energy transfer.

> **Longitudinal wave:** a wave in which the particles of the medium oscillate parallel to the direction of energy transfer, producing compressions and rarefactions.

> **Wavelength:** the distance between two consecutive points on a wave that are in phase (e.g. crest to crest).

> **Amplitude:** the maximum displacement of a point on the wave from its equilibrium position.

> **Frequency:** the number of complete oscillations of a point per unit time; $f = 1/T$; unit Hz.

> **Intensity:** the rate of energy transfer per unit area perpendicular to the direction of wave travel; $I = P/A$; unit $\text{W m}^{-2}$.

> **Polarisation:** the restriction of the oscillations of a transverse wave to one plane.

> **Diffraction:** the spreading of waves as they pass through a gap or around an obstacle.

> **Interference:** the superposition of two or more waves at a point, producing a resultant displacement equal to the vector sum of the individual displacements.

> **Coherence:** two waves have a constant phase difference (and therefore the same frequency).

> **Path difference:** the difference in the distances travelled by two waves from their sources to a given point.

> **Phase difference:** the fraction of a cycle by which one oscillation leads or lags another, measured in degrees or radians; $\Delta\phi = 360^\circ \Delta x/\lambda$.

> **Doppler effect:** the change in observed frequency of a wave when there is relative motion between the source and the observer.

> **Red shift:** the increase in wavelength (decrease in frequency) of light from a source receding from the observer.

## 3. Formula Sheet

**Quick reference:**

$$f = \frac{1}{T}, \quad v = f\lambda, \quad I = \frac{P}{A}, \quad I = \frac{P}{4\pi r^2}, \quad I \propto A^2, \quad I = I_0\cos^2\theta, \quad \Delta\phi = \frac{\Delta x}{\lambda}360^\circ, \quad w = \frac{\lambda D}{a}, \quad d\sin\theta = n\lambda, \quad f_o = f_s\frac{v}{v \pm v_s}, \quad \frac{\Delta\lambda}{\lambda} = \frac{v_s}{c}$$

| Formula | Meaning of symbols | Units | When to use it |
|---|---|---|---|
| $$f = \frac{1}{T}$$ | $f$ frequency, $T$ period | Hz, s | Convert period to frequency |
| $$v = f\lambda$$ | $v$ wave speed, $f$ frequency, $\lambda$ wavelength | $\text{m s}^{-1}$, Hz, m | Any progressive wave |
| $$I = \frac{P}{A}$$ | $I$ intensity, $P$ power, $A$ area perpendicular to travel | $\text{W m}^{-2}$ | Definition of intensity |
| $$I = \frac{P}{4\pi r^2}$$ | $P$ source power, $r$ distance from point source | $\text{W m}^{-2}$ | Isotropic point source; inverse-square law |
| $$I \propto A^2$$ | $A$ amplitude | — | Comparing intensities when amplitude changes |
| $$I = I_0\cos^2\theta$$ | $I_0$ incident polarised intensity, $\theta$ angle between polarisation planes | $\text{W m}^{-2}$ | Malus's law; polarised light through an analyser |
| $$I_1 = \frac{I_0}{2}$$ | $I_0$ unpolarised incident intensity | $\text{W m}^{-2}$ | First polariser only |
| $$\Delta\phi = \frac{\Delta x}{\lambda}360^\circ$$ | $\Delta\phi$ phase difference, $\Delta x$ path difference | degrees, m | Convert path difference to phase difference |
| $$w = \frac{\lambda D}{a}$$ | $w$ fringe spacing, $D$ slit–screen distance, $a$ slit separation | m | Young's double slit, small angles |
| $$d\sin\theta = n\lambda$$ | $d$ slit spacing, $\theta$ diffraction angle, $n$ order | m, degrees | Diffraction grating maxima |
| $$f_o = f_s\frac{v}{v \pm v_s}$$ | $f_o$ observed frequency, $f_s$ source frequency, $v$ wave speed, $v_s$ source speed | Hz, $\text{m s}^{-1}$ | Doppler effect, source moving; minus = approaching, plus = receding |
| $$\frac{\Delta\lambda}{\lambda} = \frac{v_s}{c}$$ | $\Delta\lambda$ wavelength shift, $v_s$ recession speed, $c$ speed of light | m, $\text{m s}^{-1}$ | Red shift for $v_s \ll c$ |
| $$c = f\lambda$$ | $c$ speed of light in vacuum | $\text{m s}^{-1}$ | All EM waves in a vacuum |

**Exam facts:** $v = f\lambda$, $I = P/A$, $d\sin\theta = n\lambda$ and the Doppler formula are on the data sheet. The double-slit result $w = \frac{\lambda D}{a}$ is **not** printed — derive it from path difference $\frac{ax}{D} = n\lambda$. Malus's law $I = I_0\cos^2\theta$ is not printed either. Remember that $d = \frac{1}{N}$ where $N$ is lines per metre; if $N$ is lines per mm, $d = \frac{1}{N}~\text{mm} = \frac{10^{-3}}{N}~\text{m}$.

## 4. Methods (Question Types & Methods)

### 1. Use the wave equation

**Method:**
1. Convert $\lambda$ to m (nm $\times 10^{-9}$, cm $\times 10^{-2}$) and $f$ to Hz (kHz $\times 10^3$, MHz $\times 10^6$).
2. Use $v = f\lambda$; rearrange as needed.
3. For a wave entering a new medium, $f$ stays the same; $v$ and $\lambda$ change together.

**Traps:** using $f = \frac{1}{T}$ with $T$ in ms without converting; mixing nm and m; assuming the frequency changes when light enters glass.

### 2. Read a c.r.o. trace

**Method:**
1. Count the horizontal divisions for **one complete wave** (crest to crest).
2. Multiply by the time-base setting to get $T$ in seconds.
3. $f = \frac{1}{T}$.
4. If asked for amplitude, count vertical divisions and multiply by the volts-per-division setting.

**Traps:** counting half a wave; using the whole screen width instead of one cycle; reading the time-base as the period.

### 3. Intensity and amplitude

**Method:**
1. For a point source: $I = \frac{P}{4\pi r^2}$; for a general beam: $I = \frac{P}{A}$.
2. For amplitude changes: $\frac{I_2}{I_1} = \left(\frac{A_2}{A_1}\right)^2$.
3. For distance changes: $\frac{I_2}{I_1} = \left(\frac{r_1}{r_2}\right)^2$.

**Traps:** using $I \propto A$ instead of $A^2$; forgetting the $4\pi$ for a sphere; using diameter instead of distance from the source.

### 4. Polarisation and Malus's law

**Method:**
1. If the incident light is unpolarised, first halve the intensity at the polariser.
2. If the light is already polarised, use $I = I_0\cos^2\theta$ directly.
3. Square the cosine before multiplying.
4. For crossed polarisers, $\theta = 90^\circ$ gives zero.

**Traps:** applying Malus's law to unpolarised light without halving first; using $\cos\theta$ instead of $\cos^2\theta$; measuring $\theta$ from the wrong axis (it is the angle between the polarisation planes).

### 5. Interference: path difference and phase difference

**Method:**
1. Find the path difference $\Delta x$ (or express it in terms of $\lambda$).
2. Constructive: $\Delta x = n\lambda$; destructive: $\Delta x = \left(n+\frac{1}{2}\right)\lambda$.
3. Phase difference: $\Delta\phi = 360^\circ\frac{\Delta x}{\lambda}$.
4. State coherence: constant phase difference, same frequency.

**Traps:** using $\Delta x = n\lambda$ for destructive; forgetting that a phase difference of $180^\circ$ corresponds to $\frac{\lambda}{2}$; claiming two lamps are coherent.

### 6. Young's double slit

**Method:**
1. Convert $a$ (mm → m) and $\lambda$ (nm → m).
2. Use $w = \frac{\lambda D}{a}$.
3. If the distance across several fringes is given, divide by the **number of spaces** (not the number of fringes) to get $w$.
4. To find $\lambda$: $\lambda = \frac{wa}{D}$.

**Traps:** counting fringes instead of spaces (5 fringes = 4 spaces); using cm for $D$; using the slit width instead of slit separation.

### 7. Diffraction grating

**Method:**
1. Find $d$: for $N$ lines per mm, $d = \frac{1}{N}~\text{mm} = \frac{10^{-3}}{N}~\text{m}$.
2. For the required order $n$, $\sin\theta = \frac{n\lambda}{d}$.
3. Maximum order: largest integer $n$ with $n\lambda \le d$.
4. The total number of maxima includes the central maximum and both sides: $2n_{\max}+1$.

**Traps:** inverting $N$ incorrectly; using degrees in the calculator set to radians; forgetting the central ($n=0$) maximum; taking $n_{\max}$ as the number of maxima on one side only.

### 8. Doppler effect

**Method:**
1. Decide whether the source is approaching (observed frequency higher) or receding (lower).
2. Use $f_o = f_s\frac{v}{v \mp v_s}$: minus for approaching, plus for receding.
3. For light, use $\frac{\Delta\lambda}{\lambda} = \frac{v_s}{c}$ and state the direction from the sign of $\Delta\lambda$.
4. Check that $v_s < v$; if not, the formula does not apply.

**Traps:** using the plus sign for approaching; using $c$ instead of the speed of sound; forgetting to convert km/s to m/s.

## 5. Solved Examples

### Example 1: Wave equation

**Question:** A wave on a string has frequency $64~\text{Hz}$ and wavelength $1.40~\text{m}$. Calculate its speed.

**Method:**
1. $v = f\lambda = 64 \times 1.40$.
2. $v = 89.6~\text{m s}^{-1}$.

**Answer:** $v \approx 90~\text{m s}^{-1}$.

### Example 2: c.r.o. trace

**Question:** A c.r.o. displays two complete waves in $5.0$ divisions. The time-base is $0.005~\text{s div}^{-1}$. Calculate the frequency.

**Method:**
1. One wave occupies $2.5$ divisions.
2. $T = 2.5 \times 0.005 = 0.0125~\text{s}$.
3. $f = \frac{1}{0.0125} = 80~\text{Hz}$.

**Answer:** $f = 80~\text{Hz}$.

### Example 3: Inverse-square law

**Question:** A point source radiates $P = 50~\text{W}$ equally in all directions. Calculate the intensity at $5.0~\text{m}$.

**Method:**
1. $A = 4\pi(5.0)^2 = 314~\text{m}^2$.
2. $I = \frac{50}{314} = 0.159~\text{W m}^{-2}$.

**Answer:** $I = 0.16~\text{W m}^{-2}$.

### Example 4: Amplitude and intensity

**Question:** A wave of intensity $200~\text{W m}^{-2}$ has its amplitude reduced to one quarter of its original value. Calculate the new intensity.

**Method:**
1. $I \propto A^2$, so the factor is $\left(\frac{1}{4}\right)^2 = \frac{1}{16}$.
2. $I = \frac{200}{16} = 12.5~\text{W m}^{-2}$.

**Answer:** $12.5~\text{W m}^{-2}$.

### Example 5: Malus's law

**Question:** Polarised light of intensity $120~\text{W m}^{-2}$ passes through an analyser at $45^\circ$ to its plane of polarisation. Calculate the transmitted intensity.

**Method:**
1. $\cos 45^\circ = \frac{1}{\sqrt{2}}$, so $\cos^2 45^\circ = \frac{1}{2}$.
2. $I = 120 \times \frac{1}{2} = 60~\text{W m}^{-2}$.

**Answer:** $60~\text{W m}^{-2}$.

### Example 6: Phase difference

**Question:** Two points on a wave are separated by $0.20~\text{m}$. The wavelength is $0.80~\text{m}$. Calculate the phase difference in degrees and radians.

**Method:**
1. $\frac{\Delta x}{\lambda} = 0.25$.
2. $\Delta\phi = 0.25 \times 360^\circ = 90^\circ$.
3. In radians: $90^\circ \times \frac{\pi}{180} = \frac{\pi}{2}~\text{rad}$.

**Answer:** $90^\circ = \frac{\pi}{2}~\text{rad}$.

### Example 7: Path difference condition

**Question:** Two coherent sources emit waves of wavelength $12~\text{cm}$. At a point, the path difference is $30~\text{cm}$. State and explain the type of interference.

**Method:**
1. $\frac{30}{12} = 2.5$.
2. $2.5\lambda = \left(2+\frac{1}{2}\right)\lambda$, an odd number of half-wavelengths.
3. The waves arrive in antiphase.

**Answer:** destructive interference.

### Example 8: Double-slit fringe spacing

**Question:** Light of wavelength $630~\text{nm}$ passes through slits $0.40~\text{mm}$ apart. The screen is $2.0~\text{m}$ away. Calculate the fringe spacing.

**Method:**
1. $w = \frac{\lambda D}{a} = \frac{630 \times 10^{-9} \times 2.0}{0.40 \times 10^{-3}}$.
2. $w = 3.15 \times 10^{-3}~\text{m}$.

**Answer:** $w = 3.2~\text{mm}$.

### Example 9: Wavelength from double-slit data

**Question:** In a double-slit experiment, eight bright fringes occupy a total distance of $8.4~\text{mm}$ on the screen. The slit separation is $0.25~\text{mm}$ and $D = 1.2~\text{m}$. Calculate $\lambda$.

**Method:**
1. Eight fringes span seven spaces: $w = \frac{8.4}{7} = 1.2~\text{mm}$.
2. $\lambda = \frac{wa}{D} = \frac{1.2 \times 10^{-3} \times 0.25 \times 10^{-3}}{1.2}$.
3. $\lambda = 2.5 \times 10^{-7}~\text{m}$.

**Answer:** $\lambda = 2.5 \times 10^{-7}~\text{m} = 250~\text{nm}$ (ultraviolet).

### Example 10: Grating angle

**Question:** A grating has $600$ lines per mm. Calculate the angle of the second-order maximum for light of wavelength $570~\text{nm}$.

**Method:**
1. $d = \frac{1}{600}~\text{mm} = 1.667 \times 10^{-6}~\text{m}$.
2. $\sin\theta = \frac{2 \times 570 \times 10^{-9}}{1.667 \times 10^{-6}} = 0.684$.
3. $\theta = \sin^{-1}(0.684) = 43.1^\circ$.

**Answer:** $\theta = 43^\circ$.

### Example 11: Maximum order

**Question:** A grating with $500$ lines per mm is used with light of wavelength $650~\text{nm}$. Determine the maximum order observed.

**Method:**
1. $d = \frac{1}{500}~\text{mm} = 2.0 \times 10^{-6}~\text{m}$.
2. $n_{\max} \le \frac{d}{\lambda} = \frac{2.0 \times 10^{-6}}{650 \times 10^{-9}} = 3.08$.
3. The largest integer is $3$.

**Answer:** maximum order $n = 3$; there are $2(3)+1 = 7$ maxima in total (including the central maximum).

### Example 12: Doppler effect and red shift

**Question (a):** A source emits $500~\text{Hz}$ and recedes at $34~\text{m s}^{-1}$. The speed of sound is $340~\text{m s}^{-1}$. Calculate the observed frequency.

**Question (b):** A galaxy recedes at $1.5 \times 10^7~\text{m s}^{-1}$. A spectral line has laboratory wavelength $486~\text{nm}$. Calculate the observed wavelength.

**Method (a):**
1. Receding, so use the plus sign: $f_o = 500 \times \frac{340}{340+34}$.
2. $f_o = 500 \times \frac{340}{374} = 455~\text{Hz}$.

**Method (b):**
1. $\frac{\Delta\lambda}{\lambda} = \frac{v}{c} = \frac{1.5 \times 10^7}{3.0 \times 10^8} = 0.050$.
2. $\Delta\lambda = 0.050 \times 486 = 24.3~\text{nm}$.
3. $\lambda_{\text{observed}} = 486 + 24.3 = 510~\text{nm}$.

**Answer:** (a) $f_o \approx 455~\text{Hz}$; (b) $\lambda_{\text{obs}} \approx 510~\text{nm}$, shifted towards the red.

## 6. Exam-Style Questions (Full Solutions)

### Question 1

A loudspeaker emits a note of frequency $256~\text{Hz}$. A microphone connected to a c.r.o. shows a trace in which one complete wave occupies $3.9$ divisions; the time-base is $1.0~\text{ms div}^{-1}$. The wavelength of the sound is measured separately as $1.29~\text{m}$. (a) Calculate the period and frequency displayed. (b) Calculate the speed of sound.

**Solution:**
1. (a) $T = 3.9 \times 1.0~\text{ms} = 3.9 \times 10^{-3}~\text{s}$.
2. $f = \frac{1}{3.9 \times 10^{-3}} = 256~\text{Hz}$, consistent with the source.
3. (b) $v = f\lambda = 256 \times 1.29 = 330~\text{m s}^{-1}$.

**Answer:** (a) $T = 3.9~\text{ms}$, $f = 256~\text{Hz}$; (b) $v = 330~\text{m s}^{-1}$.

### Question 2

Two identical lamps each emit $40~\text{W}$ equally in all directions. Lamp A is $2.0~\text{m}$ from a detector and lamp B is $4.0~\text{m}$ away. (a) Calculate the intensity at the detector from each lamp. (b) Calculate the ratio of the amplitudes received. (c) State one assumption.

**Solution:**
1. (a) $I_A = \frac{40}{4\pi(2.0)^2} = 0.796~\text{W m}^{-2}$.
2. $I_B = \frac{40}{4\pi(4.0)^2} = 0.199~\text{W m}^{-2}$.
3. (b) $I \propto A^2$, so $\frac{A_A}{A_B} = \sqrt{\frac{I_A}{I_B}} = \sqrt{4} = 2.0$.
4. (c) The lamps are point sources radiating isotropically, and there is no absorption.

**Answer:** (a) $0.80$ and $0.20~\text{W m}^{-2}$; (b) $2.0$; (c) isotropic point sources, no absorption.

### Question 3

Unpolarised light of intensity $200~\text{W m}^{-2}$ passes through a polariser. A second polariser (analyser) is placed after it, with its axis at $30^\circ$ to the first. (a) Calculate the intensity after the first polariser. (b) Calculate the intensity after the analyser. (c) At what angle would the transmitted intensity be zero?

**Solution:**
1. (a) $I_1 = \frac{200}{2} = 100~\text{W m}^{-2}$.
2. (b) $I_2 = 100\cos^2 30^\circ = 100 \times 0.75 = 75~\text{W m}^{-2}$.
3. (c) Zero when $\cos^2\theta = 0$, i.e. $\theta = 90^\circ$ (crossed polarisers).

**Answer:** (a) $100~\text{W m}^{-2}$; (b) $75~\text{W m}^{-2}$; (c) $90^\circ$.

### Question 4

In a Young's double-slit experiment, the slits are $0.50~\text{mm}$ apart and the screen is $1.8~\text{m}$ away. The distance between the first and sixth bright fringes is $10.6~\text{mm}$. (a) Calculate the fringe spacing. (b) Calculate the wavelength of the light. (c) State what happens to the fringe spacing if the slit separation is increased.

**Solution:**
1. (a) Five spaces between the first and sixth fringe: $w = \frac{10.6}{5} = 2.12~\text{mm}$.
2. (b) $\lambda = \frac{wa}{D} = \frac{2.12 \times 10^{-3} \times 0.50 \times 10^{-3}}{1.8} = 5.9 \times 10^{-7}~\text{m}$.
3. (c) $w \propto \frac{1}{a}$, so increasing $a$ decreases the fringe spacing.

**Answer:** (a) $2.1~\text{mm}$; (b) $5.9 \times 10^{-7}~\text{m}$ ($590~\text{nm}$); (c) fringes get closer together.

### Question 5

A diffraction grating has $300$ lines per mm and is illuminated normally with light of wavelength $600~\text{nm}$. (a) Calculate the slit spacing. (b) Calculate the angle of the first-order maximum. (c) Determine the maximum order and the total number of maxima.

**Solution:**
1. (a) $d = \frac{1}{300}~\text{mm} = 3.33 \times 10^{-6}~\text{m}$.
2. (b) $\sin\theta = \frac{600 \times 10^{-9}}{3.33 \times 10^{-6}} = 0.180$, so $\theta = 10.4^\circ$.
3. (c) $\frac{d}{\lambda} = \frac{3.33 \times 10^{-6}}{600 \times 10^{-9}} = 5.55$, so $n_{\max} = 5$.
4. Total maxima $= 2(5)+1 = 11$.

**Answer:** (a) $3.3 \times 10^{-6}~\text{m}$; (b) $10.4^\circ$; (c) $n_{\max} = 5$, 11 maxima.

### Question 6

A police car siren emits $700~\text{Hz}$. The car approaches a stationary observer at $25~\text{m s}^{-1}$ and then recedes at the same speed. The speed of sound is $340~\text{m s}^{-1}$. (a) Calculate the frequency heard while approaching. (b) Calculate the frequency heard while receding. (c) Explain why the pitch changes.

**Solution:**
1. (a) $f_o = 700 \times \frac{340}{340-25} = 700 \times \frac{340}{315} = 756~\text{Hz}$.
2. (b) $f_o = 700 \times \frac{340}{340+25} = 700 \times \frac{340}{365} = 652~\text{Hz}$.
3. (c) The source moves relative to the wavefronts: approaching, successive wavefronts are compressed into a shorter distance, so $\lambda$ is smaller and the observed frequency is higher; receding, the wavefronts are stretched, so $\lambda$ is larger and the frequency is lower.

**Answer:** (a) $756~\text{Hz}$; (b) $652~\text{Hz}$; (c) wavefront compression/stretching changes $\lambda$ and hence $f_o$.

## 7. Cheat Sheet

**Definitions in one line each:**
- Progressive wave: transfers energy without transferring matter.
- Transverse: oscillation perpendicular to travel. Longitudinal: parallel, with compressions/rarefactions.
- Intensity: power per unit area perpendicular to travel; $I = P/A$; unit $\text{W m}^{-2}$.
- Polarisation: restriction of transverse oscillations to one plane.
- Diffraction: spreading at a gap or obstacle.
- Coherence: constant phase difference.
- Phase difference: fraction of a cycle, $360^\circ \Delta x/\lambda$.
- Doppler: observed frequency changes due to relative motion.

**Formulas:**
- $f = 1/T$; $v = f\lambda$.
- $I = P/(4\pi r^2)$ for a point source; $I \propto A^2$.
- Malus: $I = I_0\cos^2\theta$ (polarised light); first polariser halves unpolarised light.
- Young: $w = \lambda D/a$.
- Grating: $d\sin\theta = n\lambda$; $d = 1/N$.
- Doppler: $f_o = f_s\frac{v}{v \mp v_s}$ (minus = approaching); red shift $\Delta\lambda/\lambda = v/c$.

**Numbers to know:**
- $c = 3.0 \times 10^8~\text{m s}^{-1}$; sound in air $\approx 330~\text{m s}^{-1}$.
- Visible: $400$–$700~\text{nm}$.
- Audible sound: $20~\text{Hz}$–$20~\text{kHz}$.

**Rules that win marks:**
- Only transverse waves polarise; sound cannot be polarised.
- Constructive: $\Delta x = n\lambda$. Destructive: $\Delta x = (n+\frac{1}{2})\lambda$.
- Two separate lamps are not coherent.
- In a double slit, count **spaces**, not fringes.
- White light gives a white central fringe with coloured fringes either side.
- For a grating, $n_{\max}$ is the largest integer with $n\lambda \le d$.

## 8. Common Exam Mistakes

1. **Using $v = f\lambda$ with $\lambda$ in nm and $f$ in Hz without converting.** Convert nm to m ($\times 10^{-9}$) first; otherwise the speed is wrong by $10^9$.
2. **Mixing up period and frequency in c.r.o. questions.** The time-base gives time per division; one cycle's divisions × time-base = period, then $f = 1/T$.
3. **Using $I \propto A$ instead of $I \propto A^2$.** Doubling the amplitude quadruples the intensity.
4. **Applying Malus's law to unpolarised light.** Halve the intensity at the first polariser, then use $\cos^2\theta$ at the analyser.
5. **Using $\cos\theta$ rather than $\cos^2\theta$.** Malus's law is $I = I_0\cos^2\theta$.
6. **Counting fringes instead of spaces.** The distance across $n$ fringes contains $n-1$ spaces.
7. **Using slit width instead of slit separation in $w = \lambda D/a$.** $a$ is the centre-to-centre distance between the slits.
8. **Forgetting to invert lines per mm for the grating.** $d = 1/N$; with $N$ in lines per mm, $d = (1/N)~\text{mm} = 10^{-3}/N~\text{m}$.
9. **Using the wrong sign in the Doppler formula.** Minus for approaching (higher frequency), plus for receding (lower frequency).
10. **Saying the frequency changes when light enters glass.** Frequency is fixed by the source; speed and wavelength change.
11. **Claiming sound can be polarised.** Sound is longitudinal, so it cannot; this is a standard "explain why not" question.
12. **Confusing diffraction and refraction.** Diffraction is spreading at a gap/obstacle in the same medium; refraction is a change of speed and direction at a boundary.
