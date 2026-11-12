# Chapter 30: Quantum Physics - CAIE A Level Physics (9702) Study Notes

Exam-focused revision notes for Cambridge International A Level Physics 9702, covering the photon model of electromagnetic radiation, the photoelectric effect, Einstein's photoelectric equation, line spectra and discrete electron energy levels, the de Broglie wavelength and electron diffraction, wave–particle duality, and band theory for metals, insulators and semiconductors. Definitions follow mark-scheme wording, and all calculations use $h = 6.63 \times 10^{-34}~\text{J s}$, $c = 3.00 \times 10^8~\text{m s}^{-1}$ and $e = 1.60 \times 10^{-19}~\text{C}$.

## 1. Theory

### 1.1 The photon model

Electromagnetic radiation can be modelled as a stream of **photons**. A photon is a **quantum (packet) of electromagnetic energy**.

The energy of a photon is proportional to its frequency:

$$E = hf$$

where $h$ is the **Planck constant**, $h = 6.63 \times 10^{-34}~\text{J s}$.

Using $c = f\lambda$:

$$E = \frac{hc}{\lambda}$$

**Key points:**

- High-frequency radiation (gamma, X-ray, UV) has high-energy photons.
- Low-frequency radiation (radio, microwave, infrared) has low-energy photons.
- The energy of a photon is **inversely proportional** to wavelength.
- The photon model is needed to explain **absorption and emission** of light by individual atoms and electrons.

**Worked example:** Calculate the energy of a photon of wavelength $500~\text{nm}$.

1. $\lambda = 500 \times 10^{-9}~\text{m}$.
2. $E = \frac{hc}{\lambda} = \frac{6.63 \times 10^{-34} \times 3.00 \times 10^8}{500 \times 10^{-9}}$.
3. $E = 3.98 \times 10^{-19}~\text{J}$.

**Answer:** $3.98 \times 10^{-19}~\text{J}$ (about $2.49~\text{eV}$).

### 1.2 The electronvolt

The **electronvolt (eV)** is the energy transferred when an electron moves through a potential difference of $1~\text{V}$.

$$1~\text{eV} = 1.60 \times 10^{-19}~\text{J}$$

Conversions:

- eV to J: multiply by $1.60 \times 10^{-19}$.
- J to eV: divide by $1.60 \times 10^{-19}$.
- $1~\text{keV} = 1.60 \times 10^{-16}~\text{J}$; $1~\text{MeV} = 1.60 \times 10^{-13}~\text{J}$.

For a particle of charge $q$ accelerated through a potential difference $V$, the kinetic energy gained is:

$$E_k = qV$$

For an electron, $E_k = eV$; if $V = 1000~\text{V}$, the electron gains $1000~\text{eV} = 1~\text{keV}$.

**Worked example:** Express a photon energy of $2.5~\text{eV}$ in joules.

1. $E = 2.5 \times 1.60 \times 10^{-19}$.
2. $E = 4.0 \times 10^{-19}~\text{J}$.

**Answer:** $4.0 \times 10^{-19}~\text{J}$.

### 1.3 The photoelectric effect

The **photoelectric effect** is the emission of electrons from a metal surface when electromagnetic radiation of sufficiently high frequency is incident on it.

**Observations that the wave model cannot explain:**

1. **Threshold frequency:** below a certain frequency $f_0$, no electrons are emitted, no matter how intense the radiation.
2. **Instantaneous emission:** electrons are emitted immediately (within about $10^{-9}~\text{s}$), even for very low intensity.
3. **Maximum kinetic energy depends on frequency, not intensity:** increasing intensity increases the **number** of electrons emitted per second, but not their maximum kinetic energy.
4. **No emission below threshold even for very bright light.**
5. **Different metals have different threshold frequencies.**

**The photon explanation:**

- Light arrives as photons, each of energy $hf$.
- **One photon is absorbed by one electron** (one-to-one interaction).
- The electron needs a minimum energy, the **work function** $\Phi$, to escape from the metal surface.
- If $hf < \Phi$, the electron cannot escape, however many photons arrive.
- If $hf \ge \Phi$, the electron escapes instantaneously with kinetic energy up to $hf - \Phi$.
- Increasing intensity means more photons per second, so more electrons are released per second.

**Work function $\Phi$:** the minimum energy required to remove an electron from the surface of a metal.

**Threshold frequency $f_0$:** the minimum frequency of electromagnetic radiation that can release electrons from a metal surface. At threshold, $hf_0 = \Phi$.

**Threshold wavelength $\lambda_0 = \frac{hc}{\Phi}$.**

**Worked example:** The work function of zinc is $4.3~\text{eV}$. Calculate the threshold frequency.

1. $\Phi = 4.3 \times 1.60 \times 10^{-19} = 6.88 \times 10^{-19}~\text{J}$.
2. $f_0 = \frac{\Phi}{h} = \frac{6.88 \times 10^{-19}}{6.63 \times 10^{-34}}$.
3. $f_0 = 1.04 \times 10^{15}~\text{Hz}$.

**Answer:** $1.04 \times 10^{15}~\text{Hz}$ (ultraviolet).

### 1.4 Einstein's photoelectric equation

Energy conservation for a single photon–electron interaction:

$$\text{photon energy} = \text{work function} + \text{maximum kinetic energy}$$

$$hf = \Phi + \frac{1}{2}mv_{\max}^2$$

or

$$E_{k,\max} = hf - \Phi$$

**Interpretation:**

- $\Phi$ is the minimum escape energy.
- The **fastest** electrons are those that were least tightly bound and lost no energy in escaping.
- Electrons deeper in the metal lose more energy in collisions, so they emerge with less kinetic energy; hence there is a **range** of kinetic energies up to $E_{k,\max}$.
- If $hf = \Phi$, $E_{k,\max} = 0$: the electron just escapes.
- If $hf < \Phi$, no emission.

**Stopping potential:** the reverse potential difference $V_s$ needed to stop the fastest photoelectrons. Then:

$$eV_s = E_{k,\max}$$

so

$$eV_s = hf - \Phi$$

**Worked example:** Ultraviolet light of photon energy $2.5 \times 10^{-18}~\text{J}$ is incident on zinc ($\Phi = 4.3~\text{eV}$). Calculate the maximum kinetic energy of the emitted electrons in eV and in J.

1. Convert photon energy: $\frac{2.5 \times 10^{-18}}{1.60 \times 10^{-19}} = 15.6~\text{eV}$.
2. $E_{k,\max} = 15.6 - 4.3 = 11.3~\text{eV}$.
3. In joules: $11.3 \times 1.60 \times 10^{-19} = 1.81 \times 10^{-18}~\text{J}$.

**Answer:** $11.3~\text{eV} = 1.8 \times 10^{-18}~\text{J}$.

**Worked example:** Radiation of wavelength $2.4 \times 10^{-7}~\text{m}$ strikes a metal of work function $2.8 \times 10^{-19}~\text{J}$. Calculate the maximum speed of the photoelectrons.

1. $E = \frac{hc}{\lambda} = \frac{6.63 \times 10^{-34} \times 3.00 \times 10^8}{2.4 \times 10^{-7}} = 8.29 \times 10^{-19}~\text{J}$.
2. $E_{k,\max} = 8.29 \times 10^{-19} - 2.8 \times 10^{-19} = 5.49 \times 10^{-19}~\text{J}$.
3. $\frac{1}{2}mv^2 = 5.49 \times 10^{-19}$.
4. $v = \sqrt{\frac{2 \times 5.49 \times 10^{-19}}{9.11 \times 10^{-31}}} = 1.10 \times 10^6~\text{m s}^{-1}$.

**Answer:** $1.1 \times 10^6~\text{m s}^{-1}$.

### 1.5 Graphs for the photoelectric effect

**$E_{k,\max}$ against $f$:**

- Straight line.
- Gradient $= h$.
- $y$-intercept $= -\Phi$.
- $x$-intercept $= f_0 = \Phi/h$.

The equation is $E_{k,\max} = hf - \Phi$, which is of the form $y = mx + c$.

**Stopping potential $V_s$ against $f$:**

- Straight line with gradient $h/e$.
- $y$-intercept $= -\Phi/e$.
- $x$-intercept $= f_0$.

**Photocurrent against intensity (fixed frequency above threshold):**

- Proportional: doubling intensity doubles the number of photons per second, so doubles the number of photoelectrons per second.

**$E_{k,\max}$ against intensity:**

- Horizontal line: intensity does not change the energy of each photon, only the number of photons.

**Worked example:** A graph of $E_{k,\max}$ against $f$ has a gradient of $6.6 \times 10^{-34}~\text{J s}$ and an $x$-intercept of $5.6 \times 10^{14}~\text{Hz}$. Determine the work function.

1. $f_0 = 5.6 \times 10^{14}~\text{Hz}$.
2. $\Phi = hf_0 = 6.63 \times 10^{-34} \times 5.6 \times 10^{14}$.
3. $\Phi = 3.7 \times 10^{-19}~\text{J} \approx 2.3~\text{eV}$.

**Answer:** about $2.3~\text{eV}$.

### 1.6 Wave–particle duality of light

Light exhibits both wave-like and particle-like behaviour:

| Behaviour | Evidence |
|---|---|
| **Wave-like** | Diffraction, interference, polarisation |
| **Particle-like** | Photoelectric effect, line spectra, Compton scattering, individual clicks in a Geiger counter |

**Wave–particle duality:** electromagnetic radiation propagates as a wave but interacts with matter as discrete photons.

- **Travel:** wave behaviour (diffraction/interference).
- **Interaction/absorption/emission:** particle behaviour (photons).

Neither model alone explains all observations. The model used depends on the experiment.

**Worked example:** Explain how the photoelectric effect provides evidence for the particle nature of light.

1. There is a threshold frequency below which no electrons are emitted, regardless of intensity.
2. A wave model would predict that any frequency could eventually supply enough energy if the intensity were high enough.
3. The existence of a threshold and instantaneous emission are explained if light arrives as photons of energy $hf$, with one photon interacting with one electron.
4. Increasing intensity increases the number of photons, not the energy per photon, so $E_{k,\max}$ does not increase.

**Answer:** threshold frequency, instantaneous emission and intensity-independent $E_{k,\max}$ all require photons.

### 1.7 Line spectra and energy levels

**Emission spectrum:** a bright-line spectrum produced by a hot gas. Each line corresponds to a specific wavelength emitted by excited atoms.

**Absorption spectrum:** a continuous spectrum crossed by dark lines, produced when white light passes through a cooler gas. The gas absorbs photons of specific energies, so those wavelengths are missing.

**Energy levels:** electrons in an isolated atom can occupy only certain discrete energy values. These are **quantised**. An electron cannot have an energy between two levels.

**Ground state:** the lowest allowed energy level.

**Excitation:** an electron absorbs a photon of energy exactly equal to the gap between two levels and moves to a higher level.

**De-excitation:** an electron falls to a lower level and emits a photon with energy equal to the energy difference:

$$\Delta E = hf = \frac{hc}{\lambda}$$

**Why line spectra are unique:** each element has a different set of energy levels, so the energy differences (and hence wavelengths) are unique. Line spectra can be used to identify elements.

**Why absorption lines are dark:** the cooler gas absorbs photons of exactly the right energies from the continuous white-light spectrum. The re-emitted photons go in all directions, so less light of those wavelengths reaches the observer along the original line of sight. The absorbed wavelengths appear as dark lines.

**Energy levels are negative:** the zero of energy is taken when the electron is completely free from the atom (at rest at infinity). A bound electron has less energy than a free electron, so its energy is negative. The **ionisation energy** is the energy needed to raise the electron from its current level to zero.

**Worked example:** An electron in a hydrogen atom falls from $-5.4 \times 10^{-19}~\text{J}$ to $-21.8 \times 10^{-19}~\text{J}$. Calculate the wavelength of the emitted photon.

1. $\Delta E = (-5.4) - (-21.8) = 16.4 \times 10^{-19}~\text{J}$.
2. $\lambda = \frac{hc}{\Delta E} = \frac{6.63 \times 10^{-34} \times 3.00 \times 10^8}{16.4 \times 10^{-19}}$.
3. $\lambda = 1.21 \times 10^{-7}~\text{m} = 121~\text{nm}$.

**Answer:** $121~\text{nm}$ (ultraviolet).

**Worked example:** Explain why a gas at low pressure produces a line spectrum rather than a continuous spectrum.

1. Atoms in a low-pressure gas are widely separated and do not interact significantly.
2. Electrons can occupy only discrete energy levels.
3. Transitions between levels emit photons of specific energies, so only specific wavelengths are present.

**Answer:** quantised energy levels produce discrete photon energies.

### 1.8 The de Broglie wavelength

Louis de Broglie proposed that **all moving particles have an associated wavelength**:

$$\lambda = \frac{h}{p} = \frac{h}{mv}$$

where $p = mv$ is the momentum.

**Key points:**

- The heavier or faster the particle, the shorter its de Broglie wavelength.
- Everyday objects have wavelengths far too small to show observable diffraction.
- Electrons accelerated to typical laboratory energies have wavelengths of order $10^{-11}$ to $10^{-10}~\text{m}$, similar to atomic spacing, so they can be diffracted by crystals.
- The de Broglie relation applies to all matter, not just electrons.

**Electron accelerated from rest through $V$:**

$$eV = \frac{1}{2}mv^2 \qquad \Rightarrow \qquad p = \sqrt{2meV}$$

$$\lambda = \frac{h}{\sqrt{2meV}}$$

This shows that increasing the accelerating voltage **decreases** the wavelength.

**Worked example:** Calculate the de Broglie wavelength of an electron travelling at $1.0 \times 10^7~\text{m s}^{-1}$.

1. $p = mv = 9.11 \times 10^{-31} \times 1.0 \times 10^7 = 9.11 \times 10^{-24}~\text{kg m s}^{-1}$.
2. $\lambda = \frac{6.63 \times 10^{-34}}{9.11 \times 10^{-24}}$.
3. $\lambda = 7.3 \times 10^{-11}~\text{m}$.

**Answer:** $7.3 \times 10^{-11}~\text{m}$, comparable to atomic spacing, so diffraction is possible.

**Worked example:** An electron is accelerated through $1000~\text{V}$. Calculate its speed and de Broglie wavelength.

1. $E_k = eV = 1.60 \times 10^{-19} \times 1000 = 1.60 \times 10^{-16}~\text{J}$.
2. $v = \sqrt{\frac{2E_k}{m}} = \sqrt{\frac{3.20 \times 10^{-16}}{9.11 \times 10^{-31}}} = 1.87 \times 10^7~\text{m s}^{-1}$.
3. $p = mv = 1.71 \times 10^{-23}~\text{kg m s}^{-1}$.
4. $\lambda = \frac{6.63 \times 10^{-34}}{1.71 \times 10^{-23}} = 3.88 \times 10^{-11}~\text{m}$.

**Answer:** $1.9 \times 10^7~\text{m s}^{-1}$; $\lambda \approx 3.9 \times 10^{-11}~\text{m}$.

### 1.9 Electron diffraction

**Apparatus:** an electron diffraction tube contains a heated cathode, an anode, a graphite film and a phosphor screen. Electrons are accelerated by a high voltage (typically a few kV) and pass through a thin graphite film.

**Observation:** concentric diffraction rings appear on the screen. Each ring is produced by electrons diffracted by a set of atomic layers in the graphite crystals.

**Conclusion:** electrons behave as waves when travelling through the graphite. The atomic layers act like a diffraction grating, with spacing comparable to the electron de Broglie wavelength.

**Effect of accelerating voltage:**

- Higher voltage → greater electron speed → greater momentum → **shorter** de Broglie wavelength.
- Shorter wavelength → smaller diffraction angle → the rings **shrink** toward the centre.

**Diffraction condition:** for atomic plane spacing $d$ and diffraction angle $\theta$:

$$\lambda = 2d\sin\theta$$

**Evidence for particle nature:** the screen shows individual flashes (dots), each caused by a single electron arriving. Over time, many individual arrivals build up the diffraction pattern. So the electron **travels as a wave** but **arrives as a particle**.

**Uses of electron diffraction:**

- Determining atomic spacing in crystals.
- Studying the structure of alloys and thin films.
- Investigating large molecules such as DNA.
- High-energy electron diffraction can probe nuclear size (wavelengths $\sim 10^{-15}~\text{m}$).

**Worked example:** Explain why the diffraction rings shrink when the accelerating voltage is increased.

1. Higher voltage gives the electrons more kinetic energy and speed.
2. Momentum increases, so the de Broglie wavelength decreases.
3. A shorter wavelength gives a smaller diffraction angle for the same atomic spacing.
4. Therefore the rings move closer to the centre.

**Answer:** $\lambda$ decreases, so $\theta$ decreases.

### 1.10 Wave–particle duality of matter

The electron (and all matter) shows **wave–particle duality**:

- **Particle behaviour:** localised arrival, momentum, collisions, deflection in fields.
- **Wave behaviour:** diffraction and interference.

**Which model to use:**

- Use the particle model when considering interactions (collisions, absorption, individual arrivals).
- Use the wave model when considering propagation and diffraction/interference.

**Worked example:** A person of mass $65~\text{kg}$ runs at $3.0~\text{m s}^{-1}$. Calculate their de Broglie wavelength and explain why diffraction is not observed.

1. $\lambda = \frac{h}{mv} = \frac{6.63 \times 10^{-34}}{65 \times 3.0}$.
2. $\lambda = 3.4 \times 10^{-36}~\text{m}$.
3. This is vastly smaller than any everyday gap, so the diffraction angle is unobservably small.

**Answer:** $3.4 \times 10^{-36}~\text{m}$; far too small to diffract through everyday openings.

### 1.11 Band theory in solids

In a solid, atoms are close together, so their electron energy levels interact and broaden into **energy bands**. Each band contains many closely spaced allowed levels. Between bands are **forbidden gaps** where no electron energy level exists.

- **Valence band:** the highest normally occupied band; electrons here are bound to atoms.
- **Conduction band:** a band above the valence band in which electrons are free to move through the material and carry current.
- **Forbidden gap (band gap):** the energy range between the valence and conduction bands in which no electron states exist.

**Metals:**

- The conduction band is **partially filled**, or the valence and conduction bands **overlap**.
- There are empty energy levels immediately above the occupied levels.
- A small applied p.d. can give electrons extra energy, so they move freely and carry a current.
- Good conductor.

**Insulators:**

- The valence band is **full** and the conduction band is **empty**.
- The forbidden gap is **wide** (typically greater than about $3~\text{eV}$).
- At room temperature, almost no electrons have enough thermal energy to cross the gap.
- No free electrons, so no current (except a negligible leakage current).

**Semiconductors:**

- The valence band is full and the conduction band is empty at $0~\text{K}$.
- The forbidden gap is **narrow** (typically about $1~\text{eV}$).
- At room temperature, a small fraction of electrons have enough thermal energy to jump the gap, creating a few conduction electrons (and holes).
- Conductivity is much lower than a metal but increases with temperature.

**Effect of temperature:**

- **Semiconductor:** heating gives more electrons enough energy to cross the gap; the number density of charge carriers increases, so resistance **decreases** (negative temperature coefficient).
- **Metal:** the number of conduction electrons is essentially fixed; heating increases lattice vibrations, so electrons collide more often and resistance **increases** (positive temperature coefficient).

**Worked example:** Use band theory to explain why the resistance of an intrinsic semiconductor decreases as its temperature increases.

1. The valence band is full and the conduction band is empty, separated by a narrow gap.
2. Heating gives electrons thermal energy.
3. More electrons can cross the gap into the conduction band.
4. The number density of charge carriers increases, so the material conducts better and its resistance falls.

**Answer:** more electrons in the conduction band; carrier density increases.

### 1.12 Light-dependent resistors (LDRs)

An LDR is made from a semiconductor. When light (photons) of sufficient energy strikes the material:

- A photon is absorbed by an electron in the valence band.
- If the photon energy is at least the band gap, the electron is excited into the conduction band, creating an electron–hole pair.
- The number of charge carriers increases, so the resistance **decreases**.

**Maximum detectable wavelength:** the photon energy must be at least the band gap:

$$\frac{hc}{\lambda_{\max}} = E_{\text{gap}} \qquad \Rightarrow \qquad \lambda_{\max} = \frac{hc}{E_{\text{gap}}}$$

**Worked example:** An LDR material has a band gap of $2.4~\text{eV}$. Calculate the maximum wavelength of radiation it can detect.

1. $E_{\text{gap}} = 2.4 \times 1.60 \times 10^{-19} = 3.84 \times 10^{-19}~\text{J}$.
2. $\lambda_{\max} = \frac{6.63 \times 10^{-34} \times 3.00 \times 10^8}{3.84 \times 10^{-19}}$.
3. $\lambda_{\max} = 5.18 \times 10^{-7}~\text{m} \approx 518~\text{nm}$.

**Answer:** about $518~\text{nm}$ (green light); longer wavelengths have insufficient photon energy.

### 1.13 LEDs and estimating the Planck constant

In a light-emitting diode, electrons and holes recombine across the band gap, releasing energy as a photon. The photon energy is approximately the band gap energy:

$$eV \approx \frac{hc}{\lambda}$$

where $V$ is the threshold voltage at which the LED begins to conduct.

Rearranging:

$$V = \frac{hc}{e}\cdot\frac{1}{\lambda}$$

A graph of threshold voltage $V$ against $1/\lambda$ is a straight line through the origin with gradient:

$$\text{gradient} = \frac{hc}{e} \qquad \Rightarrow \qquad h = \frac{e \times \text{gradient}}{c}$$

**Worked example:** A red LED with $\lambda = 670~\text{nm}$ has a threshold voltage of $1.70~\text{V}$. Estimate $h$.

1. $h = \frac{eV\lambda}{c}$.
2. $h = \frac{1.60 \times 10^{-19} \times 1.70 \times 670 \times 10^{-9}}{3.00 \times 10^8}$.
3. $h = 6.07 \times 10^{-34}~\text{J s}$.

**Answer:** $6.1 \times 10^{-34}~\text{J s}$, close to the accepted value.

## 2. Definition Sheet

> **Photon:** a quantum (packet) of electromagnetic energy, of energy $E = hf$.

> **Planck constant ($h$):** the constant relating photon energy to frequency, $E = hf$; $h = 6.63 \times 10^{-34}~\text{J s}$.

> **Electronvolt (eV):** the energy transferred when an electron moves through a potential difference of $1~\text{V}$; $1~\text{eV} = 1.60 \times 10^{-19}~\text{J}$.

> **Photoelectric effect:** the emission of electrons from a metal surface when electromagnetic radiation of frequency above the threshold frequency is incident on it.

> **Work function ($\Phi$):** the minimum energy required to remove an electron from the surface of a metal.

> **Threshold frequency ($f_0$):** the minimum frequency of incident radiation that can cause photoelectric emission from a metal.

> **Threshold wavelength ($\lambda_0$):** the maximum wavelength of radiation that can cause photoelectric emission.

> **Stopping potential ($V_s$):** the minimum reverse potential difference that stops the fastest photoelectrons, so $eV_s = E_{k,\max}$.

> **Energy level:** a discrete allowed energy value that an electron can have in an isolated atom.

> **Ground state:** the lowest energy level of an atom.

> **Excitation:** the promotion of an electron to a higher energy level by absorbing energy.

> **Ionisation:** the removal of an electron from an atom completely.

> **Emission line spectrum:** a spectrum consisting of bright lines at specific wavelengths, emitted by excited atoms in a hot gas.

> **Absorption line spectrum:** a continuous spectrum with dark lines at wavelengths absorbed by a cooler gas.

> **de Broglie wavelength ($\lambda$):** the wavelength associated with a moving particle, $\lambda = h/p = h/mv$.

> **Wave–particle duality:** the property that electromagnetic radiation and matter exhibit both wave-like and particle-like behaviour depending on the experiment.

> **Valence band:** the highest occupied energy band in a solid at absolute zero.

> **Conduction band:** an energy band in which electrons are free to move and carry current.

> **Forbidden gap (band gap):** the range of energies between the valence and conduction bands in which no electron states exist.

> **Intrinsic semiconductor:** a pure semiconductor whose conductivity arises from thermally excited electrons crossing the band gap.

> **LDR:** a light-dependent resistor; a semiconductor whose resistance decreases when light of sufficient photon energy creates additional charge carriers.

## 3. Formula Sheet

| Formula | Meaning of symbols | Units | When to use it |
|---|---|---|---|
| $E = hf$ | $E$ photon energy, $f$ frequency | J, Hz | Photon energy from frequency |
| $E = \frac{hc}{\lambda}$ | $\lambda$ wavelength | J, m | Photon energy from wavelength |
| $1~\text{eV} = 1.60 \times 10^{-19}~\text{J}$ | conversion | J | Converting photon/particle energies |
| $hf = \Phi + \frac{1}{2}mv_{\max}^2$ | $\Phi$ work function | J | Einstein photoelectric equation |
| $E_{k,\max} = hf - \Phi$ | maximum kinetic energy | J | Photoelectric calculations |
| $f_0 = \frac{\Phi}{h}$ | threshold frequency | Hz | Minimum frequency for emission |
| $\lambda_0 = \frac{hc}{\Phi}$ | threshold wavelength | m | Maximum wavelength for emission |
| $eV_s = E_{k,\max}$ | $V_s$ stopping potential | V | Stopping-potential experiments |
| $\Delta E = hf = \frac{hc}{\lambda}$ | $\Delta E$ energy level difference | J | Line spectra |
| $\lambda = \frac{h}{mv}$ | $m$ mass, $v$ speed | m | de Broglie wavelength |
| $eV = \frac{1}{2}mv^2$ | accelerating voltage | J | Electron gun |
| $\lambda = \frac{h}{\sqrt{2meV}}$ | $V$ accelerating voltage | m | Electron wavelength from voltage |
| $\lambda = 2d\sin\theta$ | $d$ atomic plane spacing | m | Electron diffraction |
| $\frac{hc}{\lambda_{\max}} = E_{\text{gap}}$ | band gap energy | J | Maximum LDR wavelength |
| $eV \approx \frac{hc}{\lambda}$ | LED threshold voltage | V | Estimating $h$ with LEDs |

**Exam facts:** $h$, $c$ and $e$ are on the data sheet. The photoelectric equation and de Broglie equation are **not** printed and must be recalled. When using $E = hf$, frequencies must be in Hz; when using $E = hc/\lambda$, wavelengths must be in metres.

## 4. Methods (Question Types & Methods)

### 1. Photon energy

**Method:**
1. Convert wavelength to metres or frequency to Hz.
2. Use $E = hf$ or $E = hc/\lambda$.
3. If needed, convert to eV by dividing by $1.60 \times 10^{-19}$.

**Traps:** using nm directly in $hc/\lambda$; mixing eV and J in the same equation; forgetting that $E \propto 1/\lambda$.

### 2. Photoelectric equation

**Method:**
1. Calculate photon energy in joules (or convert $\Phi$ to joules).
2. Subtract the work function: $E_{k,\max} = hf - \Phi$.
3. If the result is negative, no emission occurs.
4. For speed, use $\frac{1}{2}mv^2 = E_{k,\max}$.

**Traps:** using frequency below threshold and still giving a negative kinetic energy as physical; forgetting to convert $\Phi$ from eV to J; using the photon energy as kinetic energy.

### 3. Threshold frequency/wavelength

**Method:**
1. $\Phi$ must be in joules.
2. $f_0 = \Phi/h$; $\lambda_0 = hc/\Phi$.
3. Check the region of the EM spectrum.

**Traps:** using $\Phi$ in eV in $f_0 = \Phi/h$; mixing threshold wavelength with the wavelength of the incident light.

### 4. Stopping potential

**Method:**
1. $E_{k,\max} = eV_s$.
2. If $V_s$ is given, $E_{k,\max} = 1.60 \times 10^{-19} \times V_s$.
3. Then use $hf = \Phi + eV_s$.

**Traps:** using $V_s$ as the photon energy; forgetting that $V_s$ is a reverse p.d.; mixing sign conventions.

### 5. Graph analysis

**Method:**
1. Identify the axes.
2. For $E_{k,\max}$ vs $f$: gradient $= h$, intercept $= -\Phi$, $x$-intercept $= f_0$.
3. For $V_s$ vs $f$: gradient $= h/e$, intercept $= -\Phi/e$.
4. Use the gradient to find $h$; use the intercept to find $\Phi$.

**Traps:** taking the gradient as $\Phi$; forgetting the negative intercept; reading the $x$-axis in units of $10^{14}~\text{Hz}$.

### 6. Line spectra/energy levels

**Method:**
1. Identify the initial and final levels.
2. $\Delta E = E_{\text{initial}} - E_{\text{final}}$ (higher minus lower).
3. For emission, $\Delta E$ is positive and the photon energy equals it.
4. $f = \Delta E/h$; $\lambda = hc/\Delta E$.
5. For absorption, the photon energy must equal the gap exactly.

**Traps:** subtracting the wrong way and getting a negative energy; using the energy of a level instead of the difference; forgetting to convert eV to J.

### 7. de Broglie wavelength

**Method:**
1. Find momentum $p = mv$.
2. $\lambda = h/p$.
3. For an accelerated electron, use $eV = \frac{1}{2}mv^2$ to find $v$ or use $\lambda = h/\sqrt{2meV}$.
4. Compare $\lambda$ with atomic spacing ($\sim 10^{-10}~\text{m}$) to decide whether diffraction is significant.

**Traps:** using $E = hf$ for a matter wave; forgetting to convert keV to eV; using the speed of light for an electron.

### 8. Band theory explanations

**Method:**
1. Identify the material: metal, insulator or semiconductor.
2. Describe the occupancy of the valence and conduction bands.
3. Describe the size of the forbidden gap.
4. Link to the number of free electrons and hence conductivity/resistance.
5. For temperature effects, state how the number of charge carriers or the lattice vibrations change.

**Traps:** saying a semiconductor has no free electrons (it has a few); saying heating a metal increases free-electron number (it does not); confusing band gap with work function (both are energies but different contexts).

## 5. Solved Examples

### Example 1: Photon energy from frequency

**Question:** Calculate the energy of a photon of frequency $6.0 \times 10^{14}~\text{Hz}$.

**Method:**
1. $E = hf = 6.63 \times 10^{-34} \times 6.0 \times 10^{14}$.
2. $E = 3.98 \times 10^{-19}~\text{J}$.

**Answer:** $4.0 \times 10^{-19}~\text{J}$ (about $2.5~\text{eV}$).

### Example 2: Photon energy from wavelength

**Question:** Calculate the energy of a photon of wavelength $450~\text{nm}$ in eV.

**Method:**
1. $E = \frac{6.63 \times 10^{-34} \times 3.00 \times 10^8}{450 \times 10^{-9}} = 4.42 \times 10^{-19}~\text{J}$.
2. $E = \frac{4.42 \times 10^{-19}}{1.60 \times 10^{-19}} = 2.76~\text{eV}$.

**Answer:** $2.8~\text{eV}$.

### Example 3: Threshold wavelength

**Question:** The work function of gold is $4.9~\text{eV}$. Calculate the threshold wavelength.

**Method:**
1. $\Phi = 4.9 \times 1.60 \times 10^{-19} = 7.84 \times 10^{-19}~\text{J}$.
2. $\lambda_0 = \frac{hc}{\Phi} = \frac{1.989 \times 10^{-25}}{7.84 \times 10^{-19}}$.
3. $\lambda_0 = 2.54 \times 10^{-7}~\text{m}$.

**Answer:** $254~\text{nm}$ (ultraviolet).

### Example 4: Maximum kinetic energy

**Question:** Light of wavelength $300~\text{nm}$ is incident on a metal with work function $2.0~\text{eV}$. Calculate $E_{k,\max}$ in eV.

**Method:**
1. $E = \frac{6.63 \times 10^{-34} \times 3.00 \times 10^8}{300 \times 10^{-9}} = 6.63 \times 10^{-19}~\text{J}$.
2. $E = 4.14~\text{eV}$.
3. $E_{k,\max} = 4.14 - 2.0 = 2.14~\text{eV}$.

**Answer:** $2.1~\text{eV}$.

### Example 5: Photoelectron speed

**Question:** In Example 4, calculate the maximum speed of the photoelectrons.

**Method:**
1. $E_{k,\max} = 2.14 \times 1.60 \times 10^{-19} = 3.42 \times 10^{-19}~\text{J}$.
2. $\frac{1}{2}mv^2 = 3.42 \times 10^{-19}$.
3. $v = \sqrt{\frac{2 \times 3.42 \times 10^{-19}}{9.11 \times 10^{-31}}} = 8.67 \times 10^5~\text{m s}^{-1}$.

**Answer:** $8.7 \times 10^5~\text{m s}^{-1}$.

### Example 6: Stopping potential

**Question:** The maximum kinetic energy of photoelectrons is $1.8~\text{eV}$. Calculate the stopping potential.

**Method:**
1. $eV_s = 1.8~\text{eV}$.
2. $V_s = 1.8~\text{V}$.

**Answer:** $1.8~\text{V}$.

### Example 7: Work function from a graph

**Question:** A graph of $E_{k,\max}$ against $f$ has a gradient of $6.6 \times 10^{-34}~\text{J s}$ and a $y$-intercept of $-3.2 \times 10^{-19}~\text{J}$. Determine $\Phi$ and $f_0$.

**Method:**
1. $y$-intercept $= -\Phi$, so $\Phi = 3.2 \times 10^{-19}~\text{J}$.
2. $f_0 = \Phi/h = \frac{3.2 \times 10^{-19}}{6.63 \times 10^{-34}} = 4.8 \times 10^{14}~\text{Hz}$.

**Answer:** $\Phi = 3.2 \times 10^{-19}~\text{J}$ ($2.0~\text{eV}$); $f_0 = 4.8 \times 10^{14}~\text{Hz}$.

### Example 8: Energy level transition

**Question:** An electron falls from $-3.4~\text{eV}$ to $-13.6~\text{eV}$. Calculate the photon wavelength.

**Method:**
1. $\Delta E = (-3.4) - (-13.6) = 10.2~\text{eV}$.
2. $\Delta E = 10.2 \times 1.60 \times 10^{-19} = 1.63 \times 10^{-18}~\text{J}$.
3. $\lambda = \frac{hc}{\Delta E} = \frac{1.989 \times 10^{-25}}{1.63 \times 10^{-18}}$.
4. $\lambda = 1.22 \times 10^{-7}~\text{m}$.

**Answer:** $122~\text{nm}$ (ultraviolet).

### Example 9: de Broglie wavelength

**Question:** Calculate the de Broglie wavelength of an electron moving at $2.0 \times 10^6~\text{m s}^{-1}$.

**Method:**
1. $p = 9.11 \times 10^{-31} \times 2.0 \times 10^6 = 1.82 \times 10^{-24}~\text{kg m s}^{-1}$.
2. $\lambda = \frac{6.63 \times 10^{-34}}{1.82 \times 10^{-24}}$.
3. $\lambda = 3.64 \times 10^{-10}~\text{m}$.

**Answer:** $3.6 \times 10^{-10}~\text{m}$, comparable to atomic spacing.

### Example 10: Electron accelerated through a p.d.

**Question:** An electron is accelerated through $500~\text{V}$. Calculate its de Broglie wavelength.

**Method:**
1. $E_k = 500~\text{eV} = 8.0 \times 10^{-17}~\text{J}$.
2. $v = \sqrt{\frac{2 \times 8.0 \times 10^{-17}}{9.11 \times 10^{-31}}} = 1.33 \times 10^7~\text{m s}^{-1}$.
3. $p = 1.21 \times 10^{-23}~\text{kg m s}^{-1}$.
4. $\lambda = \frac{6.63 \times 10^{-34}}{1.21 \times 10^{-23}} = 5.48 \times 10^{-11}~\text{m}$.

**Answer:** $5.5 \times 10^{-11}~\text{m}$.

### Example 11: LDR band gap

**Question:** An LDR has a band gap of $1.9~\text{eV}$. Calculate the maximum wavelength it can detect.

**Method:**
1. $E_{\text{gap}} = 1.9 \times 1.60 \times 10^{-19} = 3.04 \times 10^{-19}~\text{J}$.
2. $\lambda_{\max} = \frac{1.989 \times 10^{-25}}{3.04 \times 10^{-19}}$.
3. $\lambda_{\max} = 6.54 \times 10^{-7}~\text{m}$.

**Answer:** $654~\text{nm}$ (red light).

### Example 12: Number of photons per second

**Question:** A $1.0~\text{mW}$ laser emits light of wavelength $648~\text{nm}$. Calculate the number of photons emitted per second.

**Method:**
1. $E_{\text{photon}} = \frac{6.63 \times 10^{-34} \times 3.00 \times 10^8}{648 \times 10^{-9}} = 3.07 \times 10^{-19}~\text{J}$.
2. Power $= 1.0 \times 10^{-3}~\text{J s}^{-1}$.
3. Number per second $= \frac{1.0 \times 10^{-3}}{3.07 \times 10^{-19}} = 3.26 \times 10^{15}$.

**Answer:** $3.3 \times 10^{15}~\text{photons s}^{-1}$.

## 6. Exam-Style Questions (Full Solutions)

### Question 1

Light of wavelength $250~\text{nm}$ is incident on a metal surface of work function $3.5~\text{eV}$. (a) Calculate the photon energy in eV. (b) Calculate the maximum kinetic energy of the emitted electrons. (c) State and explain what happens if the intensity is doubled at the same wavelength.

**Solution:**
1. (a) $E = \frac{hc}{\lambda} = \frac{6.63 \times 10^{-34} \times 3.00 \times 10^8}{250 \times 10^{-9}} = 7.96 \times 10^{-19}~\text{J}$.
2. $E = \frac{7.96 \times 10^{-19}}{1.60 \times 10^{-19}} = 4.98~\text{eV}$.
3. (b) $E_{k,\max} = 4.98 - 3.5 = 1.48~\text{eV}$.
4. (c) Doubling the intensity doubles the number of photons per second, so the number of photoelectrons per second doubles. The maximum kinetic energy is unchanged because each photon still has the same energy.

**Answer:** (a) $5.0~\text{eV}$; (b) $1.5~\text{eV}$; (c) rate doubles, $E_{k,\max}$ unchanged.

### Question 2

Explain the photoelectric effect in terms of photons, and explain why the wave model fails to account for (a) the threshold frequency and (b) the instantaneous emission of electrons.

**Solution:**
1. Light arrives as photons of energy $hf$; one photon is absorbed by one electron.
2. The electron needs at least the work function $\Phi$ to escape. If $hf \ge \Phi$, it escapes with kinetic energy up to $hf - \Phi$.
3. (a) A wave model predicts that any frequency could supply enough energy if the intensity is high enough or the exposure long enough. In reality, below $f_0$ no electrons are emitted even for very intense light, because each photon has insufficient energy.
4. (b) A wave model predicts a delay while energy builds up over the surface. The photon model predicts immediate emission because a single photon can transfer all its energy to a single electron at once.

**Answer:** as above.

### Question 3

An electron in a hydrogen atom falls from the $n=3$ level at $-1.51~\text{eV}$ to the $n=2$ level at $-3.40~\text{eV}$. (a) Calculate the energy of the emitted photon in joules. (b) Calculate its wavelength. (c) State the region of the electromagnetic spectrum.

**Solution:**
1. (a) $\Delta E = (-1.51) - (-3.40) = 1.89~\text{eV}$.
2. $\Delta E = 1.89 \times 1.60 \times 10^{-19} = 3.02 \times 10^{-19}~\text{J}$.
3. (b) $\lambda = \frac{hc}{\Delta E} = \frac{1.989 \times 10^{-25}}{3.02 \times 10^{-19}} = 6.58 \times 10^{-7}~\text{m}$.
4. (c) $658~\text{nm}$ is visible red light.

**Answer:** (a) $3.0 \times 10^{-19}~\text{J}$; (b) $658~\text{nm}$; (c) visible (red).

### Question 4

Describe the evidence for the wave nature of electrons and explain how the electron diffraction pattern changes when the accelerating voltage is increased.

**Solution:**
1. Electrons accelerated through a p.d. pass through a thin graphite film and produce concentric diffraction rings on a phosphor screen.
2. Diffraction is a wave property, so the electrons must have a wavelength comparable to the spacing of the atomic layers.
3. The de Broglie wavelength is $\lambda = h/mv$.
4. Increasing the voltage increases the electrons' speed and momentum, so $\lambda$ decreases.
5. A smaller wavelength gives a smaller diffraction angle, so the rings shrink toward the centre.

**Answer:** diffraction rings; higher voltage → shorter wavelength → smaller rings.

### Question 5

Use band theory to explain why (a) a metal conducts well, (b) an insulator does not conduct, and (c) the resistance of a semiconductor decreases when it is heated.

**Solution:**
1. (a) In a metal, the conduction band is partially filled (or overlaps the valence band), so electrons can move into empty levels just above them and carry current.
2. (b) In an insulator, the valence band is full and the conduction band is empty, with a wide forbidden gap. At room temperature, essentially no electrons can cross the gap, so there are no free charge carriers.
3. (c) In a semiconductor, the gap is narrow. Heating gives more electrons enough thermal energy to cross into the conduction band, increasing the number density of charge carriers. Resistance therefore decreases.

**Answer:** as above.

### Question 6

A particle of mass $m$ and charge $q$ is accelerated from rest through a potential difference $V$. Show that its de Broglie wavelength is $\lambda = \frac{h}{\sqrt{2mqV}}$. Hence compare the wavelengths of an electron and a proton accelerated through the same p.d.

**Solution:**
1. $qV = \frac{1}{2}mv^2$, so $v = \sqrt{\frac{2qV}{m}}$.
2. Momentum $p = mv = m\sqrt{\frac{2qV}{m}} = \sqrt{2mqV}$.
3. $\lambda = \frac{h}{p} = \frac{h}{\sqrt{2mqV}}$.
4. For the same $V$, $\lambda \propto 1/\sqrt{mq}$. The proton has a much larger mass, so its wavelength is much smaller (about $\sqrt{1836} \approx 43$ times smaller, since both have the same charge magnitude).

**Answer:** derivation as above; proton wavelength is about 43 times smaller.

## 7. Cheat Sheet

**Photon:**
- $E = hf = hc/\lambda$; $h = 6.63 \times 10^{-34}~\text{J s}$.
- $1~\text{eV} = 1.60 \times 10^{-19}~\text{J}$.

**Photoelectric:**
- $hf = \Phi + E_{k,\max}$.
- Threshold: $hf_0 = \Phi$; $\lambda_0 = hc/\Phi$.
- Stopping potential: $eV_s = E_{k,\max}$.
- Intensity → number of electrons; frequency → maximum kinetic energy.

**Spectra:**
- $\Delta E = hf = hc/\lambda$.
- Emission: bright lines; absorption: dark lines.
- Energy levels negative; ground state lowest.

**de Broglie:**
- $\lambda = h/mv$.
- Accelerated electron: $\lambda = h/\sqrt{2meV}$.
- Electron diffraction rings shrink as voltage increases.

**Band theory:**
- Metal: partially filled conduction band/overlap → conductor.
- Insulator: full valence, empty conduction, wide gap → no conduction.
- Semiconductor: narrow gap → few carriers; heating increases carriers → resistance falls.
- LDR: photons create electron–hole pairs → resistance falls.

**Duality:**
- Light: wave for propagation/diffraction; particle for absorption/emission.
- Electron: wave for diffraction; particle for collisions/arrival.

## 8. Common Exam Mistakes

1. **Using $E = hf$ with wavelength instead of frequency.** Convert with $f = c/\lambda$ first, or use $E = hc/\lambda$.
2. **Forgetting to convert nm to m.** A wavelength of $500~\text{nm}$ is $500 \times 10^{-9}~\text{m}$, not $500~\text{m}$.
3. **Mixing eV and J.** Convert the work function to joules before subtracting from a photon energy in joules, or convert everything to eV.
4. **Saying brighter light gives faster electrons.** Intensity increases the **number** of photons, not the energy per photon; $E_{k,\max}$ depends on frequency.
5. **Saying below-threshold light eventually works if dim enough/long enough.** Below $f_0$, no single photon has enough energy; no emission occurs at any intensity.
6. **Forgetting that one photon interacts with one electron.** This is the key to the threshold and instantaneous emission.
7. **Using the work function as the kinetic energy.** $\Phi$ is the escape energy; the kinetic energy is the leftover.
8. **Getting the sign of $\Delta E$ wrong.** Use higher level minus lower level for emission; the photon energy is positive.
9. **Using energy levels in eV with $h$ in J s.** Convert $\Delta E$ to joules first.
10. **Using $E = hf$ for an electron.** For matter use $\lambda = h/mv$; $E = hf$ is for photons.
11. **Forgetting that the electron's speed is non-relativistic at low voltages.** The $eV = \frac{1}{2}mv^2$ equation is fine for the usual kV range but not for speeds near $c$.
12. **Saying a semiconductor has no free electrons.** It has a few thermally excited electrons; that is why it conducts slightly.
13. **Saying heating a metal increases the number of free electrons.** It does not; it increases lattice vibrations and collisions, so resistance rises.
14. **Confusing the band gap with the work function.** The band gap is between bands in a solid; the work function is the escape energy from a metal surface.
