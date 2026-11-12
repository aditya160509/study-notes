# Chapter 31: Nuclear Physics - CAIE A Level Physics (9702) Study Notes

Exam-focused revision notes for Cambridge International A Level Physics 9702, covering balanced nuclear equations, mass defect and Einstein's mass–energy equation, atomic mass units, binding energy and the binding-energy-per-nucleon curve, fission and fusion, the spontaneous and random nature of decay, activity and the decay constant, exponential decay and half-life. Definitions follow mark-scheme wording, and every formula is supported by worked calculations. Basic alpha, beta and gamma properties are in Chapter 16; this chapter focuses on the **energy** and **mathematics** of nuclear physics.

## 1. Theory

### 1.1 Balanced nuclear equations

In every nuclear reaction, two quantities are always conserved:

- **Nucleon number $A$** (total number of protons + neutrons).
- **Proton number $Z$** (total charge, in units of $e$).

**Mass–energy** is also conserved, but mass itself is **not** conserved: a small mass change appears as energy.

| Process | Change in $A$ | Change in $Z$ | Equation |
|---|---|---|---|
| Alpha decay | $-4$ | $-2$ | ${}^{A}_{Z}\text{X} \rightarrow {}^{A-4}_{Z-2}\text{Y} + {}^{4}_{2}\text{He}$ |
| Beta-minus decay | $0$ | $+1$ | ${}^{A}_{Z}\text{X} \rightarrow {}^{A}_{Z+1}\text{Y} + {}^{0}_{-1}\text{e} + \bar{\nu}_e$ |
| Beta-plus decay | $0$ | $-1$ | ${}^{A}_{Z}\text{X} \rightarrow {}^{A}_{Z-1}\text{Y} + {}^{0}_{+1}\text{e} + \nu_e$ |
| Gamma emission | $0$ | $0$ | ${}^{A}_{Z}\text{X}^{*} \rightarrow {}^{A}_{Z}\text{X} + \gamma$ |

**Parent nucleus:** the nucleus before decay. **Daughter nucleus:** the nucleus after decay.

**Worked example:** ${}^{238}_{92}\text{U}$ decays by alpha emission. Write the equation.

1. $A: 238 - 4 = 234$.
2. $Z: 92 - 2 = 90$.
3. $Z = 90$ is thorium (Th).

**Answer:** ${}^{238}_{92}\text{U} \rightarrow {}^{234}_{90}\text{Th} + {}^{4}_{2}\text{He}$.

**Worked example:** ${}^{14}_{6}\text{C}$ decays by beta-minus emission. Write the equation.

1. $A$ stays 14.
2. $Z: 6 + 1 = 7$ (nitrogen).
3. Emit an electron and an antineutrino.

**Answer:** ${}^{14}_{6}\text{C} \rightarrow {}^{14}_{7}\text{N} + {}^{0}_{-1}\text{e} + \bar{\nu}_e$.

### 1.2 Mass defect

The mass of a nucleus is **less** than the total mass of its separate protons and neutrons.

**Mass defect $\Delta m$:** the difference between the total mass of the separate nucleons and the mass of the nucleus.

$$\Delta m = \left(Zm_p + Nm_n\right) - m_{\text{nucleus}}$$

where $N = A - Z$.

**Why there is a mass defect:** work must be done against the strong nuclear force to pull a nucleus apart. The separated nucleons have more potential energy, and hence more mass, than the bound nucleus. Conversely, when nucleons bind together, energy is released and the mass decreases.

**Worked example:** A carbon-12 nucleus contains 6 protons and 6 neutrons. Given $m_p = 1.672\,623 \times 10^{-27}~\text{kg}$, $m_n = 1.674\,929 \times 10^{-27}~\text{kg}$ and $m_{\text{C-12}} = 19.926\,483 \times 10^{-27}~\text{kg}$, calculate the mass defect.

1. Mass of separate nucleons $= 6(1.672\,623) + 6(1.674\,929) = 20.085\,312 \times 10^{-27}~\text{kg}$.
2. $\Delta m = (20.085\,312 - 19.926\,483) \times 10^{-27}$.
3. $\Delta m = 0.158\,829 \times 10^{-27}~\text{kg} = 1.588 \times 10^{-28}~\text{kg}$.

**Answer:** $1.59 \times 10^{-28}~\text{kg}$.

### 1.3 Einstein's mass–energy equation

$$E = mc^2 \qquad \text{and} \qquad \Delta E = \Delta m\,c^2$$

where $c = 3.00 \times 10^8~\text{m s}^{-1}$.

**Interpretation:**

- When energy is supplied to a system, its mass **increases**.
- When energy is released, the mass of the system **decreases**.
- The mass change is extremely small in everyday processes, but significant in nuclear reactions.

**Worked example:** Calculate the energy released when the carbon-12 nucleus in the previous example is formed from separate nucleons.

1. $\Delta m = 1.588 \times 10^{-28}~\text{kg}$.
2. $\Delta E = \Delta m c^2 = 1.588 \times 10^{-28} \times (3.00 \times 10^8)^2$.
3. $\Delta E = 1.43 \times 10^{-11}~\text{J}$.

**Answer:** $1.43 \times 10^{-11}~\text{J}$ per nucleus (about $89~\text{MeV}$).

### 1.4 Atomic mass unit and mass excess

The **unified atomic mass unit (u)** is defined as $\frac{1}{12}$ of the mass of a neutral carbon-12 atom.

$$1~\text{u} = 1.6605 \times 10^{-27}~\text{kg}$$

Useful energy conversion:

$$1~\text{u} \times c^2 = 931.5~\text{MeV}$$

So a mass defect of $1~\text{u}$ corresponds to about $931.5~\text{MeV}$ of energy.

**Mass excess:** the difference between the mass of a nuclide in u and its nucleon number:

$$\text{mass excess} = \text{mass (in u)} - A$$

Mass excess can be positive or negative. It is **not** the same as mass defect: mass excess compares the nuclide mass with $A$ u, while mass defect compares the nucleus with its separate nucleons.

**Worked example:** The mass of ${}^{235}_{92}\text{U}$ is $235.043\,930~\text{u}$. Calculate its mass excess.

1. Mass excess $= 235.043\,930 - 235$.
2. Mass excess $= 0.043\,930~\text{u}$.

**Answer:** $+0.043\,930~\text{u}$.

### 1.5 Binding energy

**Binding energy (BE):** the minimum energy required to pull a nucleus apart into its separate nucleons.

$$\text{BE} = \Delta m\,c^2$$

**Binding energy per nucleon:**

$$\text{BE per nucleon} = \frac{\text{BE}}{A}$$

This is the standard measure of nuclear stability: the greater the binding energy per nucleon, the more stable the nucleus.

**Typical values:**

- Helium-4: about $7.1~\text{MeV}$ per nucleon.
- Carbon-12: about $7.7~\text{MeV}$ per nucleon.
- Iron-56: about $8.8~\text{MeV}$ per nucleon (maximum).
- Uranium-238: about $7.6~\text{MeV}$ per nucleon.

**Worked example:** Calculate the binding energy per nucleon of carbon-12 using the mass defect from Section 1.2.

1. $\text{BE} = 1.43 \times 10^{-11}~\text{J}$.
2. Per nucleon $= \frac{1.43 \times 10^{-11}}{12} = 1.19 \times 10^{-12}~\text{J}$.
3. In MeV: $\frac{1.19 \times 10^{-12}}{1.60 \times 10^{-13}} = 7.44~\text{MeV}$.

**Answer:** $1.19 \times 10^{-12}~\text{J}$ per nucleon $= 7.4~\text{MeV}$ per nucleon.

**Worked example:** The mass defect of an oxygen-16 nucleus is $2.20 \times 10^{-28}~\text{kg}$. Calculate its binding energy per nucleon.

1. $\text{BE} = 2.20 \times 10^{-28} \times (3.00 \times 10^8)^2 = 1.98 \times 10^{-11}~\text{J}$.
2. Per nucleon $= \frac{1.98 \times 10^{-11}}{16} = 1.24 \times 10^{-12}~\text{J}$.
3. In MeV: $7.74~\text{MeV}$.

**Answer:** $1.24 \times 10^{-12}~\text{J}$ per nucleon ($7.7~\text{MeV}$).

### 1.6 The binding-energy-per-nucleon curve

A graph of binding energy per nucleon against nucleon number $A$ has a characteristic shape:

- **Light nuclei ($A < 20$):** low and variable binding energy per nucleon, with sharp peaks for helium-4, carbon-12 and oxygen-16.
- **Intermediate nuclei ($A \approx 56$):** maximum binding energy per nucleon at **iron-56** (about $8.8~\text{MeV}$ per nucleon). Iron-56 is the most stable nuclide.
- **Heavy nuclei ($A > 56$):** binding energy per nucleon decreases slowly as $A$ increases, so heavy nuclei are less stable.

**Consequences:**

- **Fusion of light nuclei** increases binding energy per nucleon and releases energy.
- **Fission of heavy nuclei** increases binding energy per nucleon and releases energy.
- Energy is released in any process that moves nucleons toward the peak of the curve.

**Why iron is the end point:** fusion of nuclei lighter than iron releases energy; fusion beyond iron would **absorb** energy. Similarly, fission of nuclei lighter than iron would absorb energy. Iron-56 is therefore the most stable end point of nuclear energy release.

**Worked example:** Explain why energy is released when uranium-235 undergoes fission into two smaller fragments.

1. The uranium nucleus has a lower binding energy per nucleon than the fragments.
2. The fragments are closer to the iron-56 peak, so they are more tightly bound.
3. The increase in binding energy per nucleon corresponds to a decrease in total mass.
4. The mass difference appears as kinetic energy of the fragments (and neutrons).

**Answer:** the fragments have higher binding energy per nucleon, so mass is converted to energy.

### 1.7 Fission and fusion

**Nuclear fission:** a heavy nucleus splits into two (or more) smaller nuclei, with the release of energy and usually neutrons.

Example:

$${}^{235}_{92}\text{U} + {}^{1}_{0}\text{n} \rightarrow {}^{141}_{56}\text{Ba} + {}^{92}_{36}\text{Kr} + 3{}^{1}_{0}\text{n} + \text{energy}$$

**Nuclear fusion:** two light nuclei join to form a heavier nucleus, with the release of energy.

Example (in the Sun):

$${}^{2}_{1}\text{H} + {}^{3}_{1}\text{H} \rightarrow {}^{4}_{2}\text{He} + {}^{1}_{0}\text{n} + \text{energy}$$

**Why fusion needs high temperature:** the nuclei are positively charged and repel each other. High temperature gives them enough kinetic energy to overcome the electrostatic barrier and come close enough for the short-range strong force to act.

**Why fission releases energy:** the fragments have higher binding energy per nucleon than the original heavy nucleus.

**Why fusion releases energy:** the product has higher binding energy per nucleon than the light reactants.

**Worked example:** Explain why fusion of hydrogen nuclei occurs in the Sun but not in a laboratory at room temperature.

1. Hydrogen nuclei (protons) repel each other electrostatically.
2. They must be brought within about $10^{-15}~\text{m}$ for the strong force to bind them.
3. This requires very high kinetic energy, corresponding to temperatures of millions of kelvin.
4. The Sun's core is hot enough; room temperature is not.

**Answer:** high temperature is needed to overcome electrostatic repulsion.

### 1.8 Random and spontaneous decay

**Radioactive decay** is the spontaneous emission of particles or electromagnetic radiation from an unstable nucleus, which changes into a different nuclide.

**Random:** it is impossible to predict when a particular nucleus will decay. Each nucleus has the same probability of decaying per unit time, independently of the others.

**Spontaneous:** decay is not caused by external factors such as temperature, pressure, chemical state or the presence of other nuclei. It happens on its own.

**Evidence for randomness:** a Geiger counter near a weak source gives irregular clicks; the count rate fluctuates about an average value. The fluctuations become relatively smaller when averaged over a long time or over a large number of nuclei.

**Why decay is random:** the nucleus is isolated from neighbouring nuclei (nuclear forces are short-range), and the exact moment of decay depends on quantum-mechanical probability. A nucleus does not "age"; its chance of decaying in the next second is the same regardless of how long it has existed.

**Worked example:** Explain what is meant by saying radioactive decay is spontaneous.

1. The decay is not triggered by external conditions such as temperature, pressure or chemical reactions.
2. It occurs naturally because the nucleus is unstable.
3. The rate is unaffected by the environment.

**Answer:** decay occurs without external trigger and is unaffected by temperature, pressure or chemical state.

### 1.9 Activity and the decay constant

**Activity $A$:** the rate at which nuclei in a sample decay, measured in **becquerels (Bq)**.

$$1~\text{Bq} = 1~\text{decay per second}$$

**Decay constant $\lambda$:** the probability that an individual nucleus will decay per unit time.

Units: $\text{s}^{-1}$, $\text{min}^{-1}$, $\text{year}^{-1}$, etc.

For $N$ undecayed nuclei:

$$A = \lambda N$$

(The minus sign in $A = -\lambda N$ in some books indicates that $N$ is decreasing; activity itself is positive.)

**Worked example:** A sample contains $2.0 \times 10^{10}$ undecayed nuclei and has decay constant $5.0 \times 10^{-5}~\text{s}^{-1}$. Calculate its activity.

1. $A = \lambda N = 5.0 \times 10^{-5} \times 2.0 \times 10^{10}$.
2. $A = 1.0 \times 10^6~\text{Bq}$.

**Answer:** $1.0 \times 10^6~\text{Bq}$ ($1.0~\text{MBq}$).

**Worked example:** A source has activity $2.8 \times 10^7~\text{Bq}$. Estimate the number of beta-particles emitted in $2.0~\text{min}$.

1. $\Delta t = 120~\text{s}$.
2. $\Delta N = A\Delta t = 2.8 \times 10^7 \times 120$.
3. $\Delta N = 3.36 \times 10^9$.

**Answer:** about $3.4 \times 10^9$ particles (assuming the activity is constant over 2 minutes, which is a good approximation for a long half-life).

### 1.10 Exponential decay

The number of undecayed nuclei decreases exponentially:

$$N = N_0 e^{-\lambda t}$$

where $N_0$ is the initial number and $t$ is the elapsed time.

Since activity is proportional to $N$:

$$A = A_0 e^{-\lambda t}$$

The **corrected count rate** $R$ (background subtracted) also decays exponentially:

$$R = R_0 e^{-\lambda t}$$

**Graphs:** $N$ against $t$, $A$ against $t$ and $R$ against $t$ all have the same exponential shape. A graph of $\ln N$ against $t$ is a straight line with gradient $-\lambda$.

**Worked example:** A sample starts with $1.0 \times 10^{15}$ nuclei and has $\lambda = 0.02~\text{s}^{-1}$. Calculate the number remaining after $20~\text{s}$.

1. $N = 1.0 \times 10^{15} e^{-0.02 \times 20}$.
2. $N = 1.0 \times 10^{15} e^{-0.40}$.
3. $N = 6.7 \times 10^{14}$.

**Answer:** $6.7 \times 10^{14}$ nuclei.

**Worked example:** A sample has $\lambda = 0.10~\text{s}^{-1}$ and initially $5.0 \times 10^9$ nuclei. Calculate the number remaining and the activity after $50~\text{s}$.

1. $N = 5.0 \times 10^9 e^{-0.10 \times 50} = 5.0 \times 10^9 e^{-5.0}$.
2. $N = 3.37 \times 10^7$.
3. $A = \lambda N = 0.10 \times 3.37 \times 10^7 = 3.37 \times 10^6~\text{Bq}$.

**Answer:** $3.4 \times 10^7$ nuclei; $3.4 \times 10^6~\text{Bq}$.

### 1.11 Half-life

**Half-life $t_{1/2}$:** the mean time taken for half of the active nuclei in a sample to decay.

After one half-life, $N$ and $A$ are halved. After $n$ half-lives:

$$N = N_0\left(\frac{1}{2}\right)^n, \qquad n = \frac{t}{t_{1/2}}$$

**Relation to the decay constant:** setting $N/N_0 = \frac{1}{2}$ at $t = t_{1/2}$:

$$\frac{1}{2} = e^{-\lambda t_{1/2}} \qquad \Rightarrow \qquad \lambda t_{1/2} = \ln 2$$

$$\lambda = \frac{\ln 2}{t_{1/2}} \approx \frac{0.693}{t_{1/2}}$$

**Key point:** half-life and decay constant are **inversely proportional**. A short half-life means a large decay constant and a rapid decay.

**Worked example:** Nitrogen-13 has a half-life of $10~\text{min}$ and a sample initially contains $8.0 \times 10^{10}$ nuclei. Calculate the number remaining after (a) $10~\text{min}$, (b) $20~\text{min}$, (c) $30~\text{min}$.

1. (a) 1 half-life: $4.0 \times 10^{10}$.
2. (b) 2 half-lives: $2.0 \times 10^{10}$.
3. (c) 3 half-lives: $1.0 \times 10^{10}$.

**Answer:** $4.0 \times 10^{10}$, $2.0 \times 10^{10}$, $1.0 \times 10^{10}$.

**Worked example:** The half-life of carbon-14 is $5730~\text{years}$. Calculate its decay constant in $\text{s}^{-1}$.

1. $t_{1/2} = 5730 \times 3.15 \times 10^7~\text{s} = 1.805 \times 10^{11}~\text{s}$.
2. $\lambda = \frac{\ln 2}{t_{1/2}} = \frac{0.693}{1.805 \times 10^{11}}$.
3. $\lambda = 3.84 \times 10^{-12}~\text{s}^{-1}$.

**Answer:** $3.84 \times 10^{-12}~\text{s}^{-1}$.

### 1.12 Count rate and background radiation

A detector does not detect every decay:

- Some radiation is absorbed in the sample or its container.
- Some is emitted in directions away from the detector.
- The detector has finite efficiency and solid angle.

The measured **count rate** is therefore lower than the activity. The **corrected count rate** is:

$$R_{\text{corrected}} = R_{\text{measured}} - R_{\text{background}}$$

Background radiation comes from cosmic rays, rocks, radon gas and artificial sources; it must be measured separately (with the source removed) and subtracted.

**Worked example:** A detector records $85$ counts per minute with a source present and $15$ counts per minute with the source removed. Calculate the corrected count rate.

1. $R_{\text{corrected}} = 85 - 15$.
2. $R_{\text{corrected}} = 70~\text{counts min}^{-1}$.

**Answer:** $70~\text{counts min}^{-1}$.

### 1.13 Determining half-life from a graph

**Method 1 (graph):**
1. Read the initial value.
2. Halve it and find the corresponding time on the curve.
3. Alternatively, choose any value, halve it, and find the time interval.
4. Repeat for several pairs and average.

**Method 2 (calculation):**
1. Find $\lambda$ from $A = \lambda N$ or from the exponential equation.
2. Use $t_{1/2} = \ln 2/\lambda$.

**Worked example:** A sample's activity falls from $8.0 \times 10^5~\text{Bq}$ to $1.0 \times 10^5~\text{Bq}$ in $45~\text{min}$. Calculate the half-life.

1. The activity has fallen by a factor of 8, so $n = 3$ half-lives.
2. $3t_{1/2} = 45~\text{min}$.
3. $t_{1/2} = 15~\text{min}$.

**Answer:** $15~\text{min}$.

### 1.14 Energy released in decay and reactions

For any nuclear reaction:

$$\Delta E = \left(m_{\text{reactants}} - m_{\text{products}}\right)c^2$$

If the product mass is smaller, $\Delta E$ is positive (energy released).

**Worked example:** In the alpha decay of uranium-238, the mass of the parent is $3.952\,83 \times 10^{-25}~\text{kg}$ and the total mass of the products is $3.952\,76 \times 10^{-25}~\text{kg}$. Calculate the energy released.

1. $\Delta m = 3.952\,83 - 3.952\,76 = 0.000\,07 \times 10^{-25} = 7.0 \times 10^{-30}~\text{kg}$.
2. $\Delta E = 7.0 \times 10^{-30} \times (3.00 \times 10^8)^2$.
3. $\Delta E = 6.3 \times 10^{-13}~\text{J}$.

**Answer:** $6.3 \times 10^{-13}~\text{J}$ per decay.

**Worked example:** Calculate the energy equivalent of a mass of $1.0~\text{g}$.

1. $m = 1.0 \times 10^{-3}~\text{kg}$.
2. $E = mc^2 = 1.0 \times 10^{-3} \times (3.00 \times 10^8)^2$.
3. $E = 9.0 \times 10^{13}~\text{J}$.

**Answer:** $9.0 \times 10^{13}~\text{J}$.

### 1.15 Nuclear reactors and energy release (qualitative)

A nuclear reactor uses controlled fission of uranium-235. A slow neutron is absorbed by a U-235 nucleus, forming excited U-236, which splits into two fragments and several neutrons, releasing energy. The extra neutrons can cause further fissions (a chain reaction); control rods absorb neutrons to keep the rate steady, and a moderator slows neutrons because slow neutrons are more likely to be captured by U-235.

Most of the energy released appears as **kinetic energy of the fission fragments**, which is transferred to the surrounding material as thermal energy, driving a steam turbine.

**Worked example:** Explain why a moderator is needed in a thermal reactor.

1. Fission neutrons are fast and are less likely to be captured by U-235.
2. A moderator (e.g. graphite or water) slows them through collisions.
3. Slow (thermal) neutrons have a higher probability of inducing fission in U-235.

**Answer:** to slow neutrons and increase the fission probability.

## 2. Definition Sheet

> **Mass defect ($\Delta m$):** the difference between the total mass of the separate nucleons and the mass of the nucleus.

> **Binding energy:** the minimum energy required to split a nucleus into its separate nucleons.

> **Binding energy per nucleon:** the binding energy divided by the nucleon number; a measure of nuclear stability.

> **Atomic mass unit (u):** one-twelfth of the mass of a neutral carbon-12 atom; $1~\text{u} = 1.6605 \times 10^{-27}~\text{kg}$.

> **Mass excess:** the difference between the mass of a nuclide in u and its nucleon number.

> **Nuclear fission:** the splitting of a heavy nucleus into two smaller nuclei, with release of energy.

> **Nuclear fusion:** the joining of two light nuclei to form a heavier nucleus, with release of energy.

> **Radioactive decay:** the spontaneous emission of particles or electromagnetic radiation from an unstable nucleus.

> **Random decay:** decay in which it is impossible to predict when a particular nucleus will decay; each nucleus has a fixed probability of decay per unit time.

> **Spontaneous decay:** decay that is not triggered or affected by external conditions such as temperature, pressure or chemical state.

> **Activity ($A$):** the rate at which nuclei in a sample decay; measured in becquerels (Bq).

> **Becquerel (Bq):** the activity of a source that decays at a rate of one nucleus per second.

> **Decay constant ($\lambda$):** the probability that an individual nucleus will decay per unit time.

> **Half-life ($t_{1/2}$):** the mean time taken for half of the active nuclei in a sample to decay.

> **Corrected count rate:** the measured count rate minus the background count rate.

> **Chain reaction:** a reaction in which the neutrons produced by fission cause further fissions.

> **Moderator:** a material that slows neutrons so they are more likely to cause fission.

## 3. Formula Sheet

| Formula | Meaning of symbols | Units | When to use it |
|---|---|---|---|
| $A = Z + N$ | $A$ nucleon number, $Z$ proton number, $N$ neutron number | — | Nuclide composition |
| $\Delta m = (Zm_p + Nm_n) - m_{\text{nucleus}}$ | mass defect | kg | Binding energy calculations |
| $\Delta E = \Delta m c^2$ | energy equivalent of mass change | J | Mass–energy calculations |
| $1~\text{u} = 1.6605 \times 10^{-27}~\text{kg}$ | atomic mass unit | kg | Converting u to kg |
| $1~\text{u}\,c^2 = 931.5~\text{MeV}$ | energy equivalent | MeV | Quick u-to-energy conversion |
| $\text{mass excess} = m(\text{u}) - A$ | mass excess | u | Nuclide data |
| $\text{BE} = \Delta m c^2$ | binding energy | J | Nuclear stability |
| $\text{BE per nucleon} = \frac{\text{BE}}{A}$ | binding energy per nucleon | J | Comparing stability |
| $A = \lambda N$ | activity, decay constant, number of nuclei | Bq | Activity calculations |
| $N = N_0 e^{-\lambda t}$ | exponential decay | — | Number remaining after time $t$ |
| $A = A_0 e^{-\lambda t}$ | activity decay | Bq | Activity after time $t$ |
| $R = R_0 e^{-\lambda t}$ | count-rate decay | counts $\text{s}^{-1}$ | Corrected count rate |
| $t_{1/2} = \frac{\ln 2}{\lambda} \approx \frac{0.693}{\lambda}$ | half-life | s | Half-life/decay constant |
| $N = N_0\left(\frac{1}{2}\right)^{t/t_{1/2}}$ | decay by half-lives | — | Quick half-life estimates |
| $\ln N = \ln N_0 - \lambda t$ | logarithmic form | — | Straight-line graph of $\ln N$ vs $t$ |
| $\Delta E = (m_{\text{reactants}} - m_{\text{products}})c^2$ | energy released in a reaction | J | Fission/fusion/decay energy |

**Exam facts:** $\ln 2 \approx 0.693$. The decay constant and half-life must use the **same time unit**. Activity is always positive; the negative sign in $A = -\lambda N$ only indicates that $N$ decreases. The binding-energy curve peaks at iron-56, not at uranium.

## 4. Methods (Question Types & Methods)

### 1. Balance a nuclear equation

**Method:**
1. Write the equation with the unknown.
2. Balance $A$ first.
3. Balance $Z$ second.
4. Identify the element from $Z$.
5. For beta decay, include the neutrino/antineutrino.

**Traps:** changing $A$ in beta decay; forgetting the electron's $Z = -1$; using the wrong element for $Z$.

### 2. Mass defect and binding energy

**Method:**
1. Count protons $Z$ and neutrons $N = A - Z$.
2. Calculate the mass of the separate nucleons.
3. Subtract the nuclear mass.
4. Convert to energy with $\Delta E = \Delta m c^2$.
5. Divide by $A$ for binding energy per nucleon.

**Traps:** using the atomic mass instead of the nuclear mass (electron masses matter in precise data); forgetting to multiply by the number of nucleons; mixing u and kg.

### 3. Convert u to energy

**Method:**
1. Find the mass defect in u.
2. Multiply by $931.5~\text{MeV u}^{-1}$.
3. Or convert u to kg and use $E = mc^2$.

**Traps:** using $1~\text{u} = 1.66 \times 10^{-27}~\text{J}$ (wrong units); forgetting to convert MeV to J when needed.

### 4. Activity

**Method:**
1. Identify $\lambda$ and $N$ in consistent units.
2. $A = \lambda N$.
3. If given activity and $\lambda$, find $N = A/\lambda$.
4. For a time interval, $\Delta N = A\Delta t$ if $A$ is approximately constant.

**Traps:** using the count rate as the activity without correcting for efficiency; mixing $\text{s}^{-1}$ and $\text{min}^{-1}$; forgetting that $A$ decreases with time.

### 5. Exponential decay

**Method:**
1. Write $N = N_0 e^{-\lambda t}$ or $A = A_0 e^{-\lambda t}$.
2. Convert $t$ to match the units of $\lambda$.
3. Calculate the exponent, then use the $e^x$ key.
4. To find time, rearrange: $t = -\frac{\ln(N/N_0)}{\lambda}$.

**Traps:** using $\log_{10}$ instead of $\ln$; forgetting the minus sign; mixing years and seconds.

### 6. Half-life

**Method:**
1. If the number of half-lives is an integer, halve repeatedly.
2. Otherwise use $N = N_0(1/2)^{t/t_{1/2}}$.
3. Use $\lambda = \ln 2/t_{1/2}$ for calculations.
4. From a graph, find the time for the value to halve.

**Traps:** halving the time instead of the quantity; using $t_{1/2} = 0.693/\lambda$ with inconsistent units; assuming the sample ever reaches exactly zero.

### 7. Energy released in a reaction

**Method:**
1. Find total mass before and after.
2. $\Delta m = m_{\text{before}} - m_{\text{after}}$.
3. $\Delta E = \Delta m c^2$.
4. If $\Delta m$ is negative, energy is absorbed; if positive, energy is released.
5. For per-mole or per-kilogram energy, multiply by the number of reactions.

**Traps:** subtracting the wrong way; forgetting to include all product particles (e.g. neutrons); using atomic masses without accounting for electrons in beta decay.

### 8. Fission/fusion explanation

**Method:**
1. Refer to the binding-energy-per-nucleon curve.
2. State that the products have higher binding energy per nucleon.
3. Therefore the total mass decreases.
4. The mass difference appears as kinetic energy (and gamma radiation).

**Traps:** saying fission releases energy because the nucleus is "unstable" without mentioning binding energy; saying fusion only happens in the Sun; forgetting that fusion requires high temperature to overcome repulsion.

## 5. Solved Examples

### Example 1: Alpha decay equation

**Question:** ${}^{226}_{88}\text{Ra}$ emits an alpha-particle. Write the equation.

**Method:**
1. $A: 226 - 4 = 222$.
2. $Z: 88 - 2 = 86$ (radon).

**Answer:** ${}^{226}_{88}\text{Ra} \rightarrow {}^{222}_{86}\text{Rn} + {}^{4}_{2}\text{He}$.

### Example 2: Beta-minus equation

**Question:** ${}^{90}_{38}\text{Sr}$ emits a beta-minus particle. Write the equation.

**Method:**
1. $A$ stays 90.
2. $Z: 38 + 1 = 39$ (yttrium).
3. Include electron and antineutrino.

**Answer:** ${}^{90}_{38}\text{Sr} \rightarrow {}^{90}_{39}\text{Y} + {}^{0}_{-1}\text{e} + \bar{\nu}_e$.

### Example 3: Mass defect of helium-4

**Question:** A helium-4 nucleus has mass $6.644\,661 \times 10^{-27}~\text{kg}$. Calculate its mass defect and binding energy.

**Method:**
1. 2 protons + 2 neutrons: $2(1.672\,623) + 2(1.674\,929) = 6.695\,104 \times 10^{-27}~\text{kg}$.
2. $\Delta m = (6.695\,104 - 6.644\,661) \times 10^{-27} = 0.050\,443 \times 10^{-27}~\text{kg}$.
3. $\Delta E = 5.0443 \times 10^{-29} \times 9.0 \times 10^{16} = 4.54 \times 10^{-12}~\text{J}$.

**Answer:** $\Delta m = 5.04 \times 10^{-29}~\text{kg}$; $\text{BE} = 4.54 \times 10^{-12}~\text{J}$ ($28.4~\text{MeV}$).

### Example 4: Binding energy per nucleon

**Question:** For the helium-4 nucleus above, calculate the binding energy per nucleon in MeV.

**Method:**
1. $\text{BE} = 4.54 \times 10^{-12}~\text{J}$.
2. Per nucleon $= 1.135 \times 10^{-12}~\text{J}$.
3. In MeV: $\frac{1.135 \times 10^{-12}}{1.60 \times 10^{-13}} = 7.09~\text{MeV}$.

**Answer:** $7.1~\text{MeV}$ per nucleon.

### Example 5: Activity from number of nuclei

**Question:** A sample contains $4.0 \times 10^{12}$ nuclei and $\lambda = 2.5 \times 10^{-6}~\text{s}^{-1}$. Calculate the activity.

**Method:**
1. $A = \lambda N = 2.5 \times 10^{-6} \times 4.0 \times 10^{12}$.
2. $A = 1.0 \times 10^7~\text{Bq}$.

**Answer:** $1.0 \times 10^7~\text{Bq}$.

### Example 6: Number of decays in a time interval

**Question:** A source of activity $5.0 \times 10^5~\text{Bq}$ is observed for $10~\text{min}$. Estimate the number of decays.

**Method:**
1. $t = 600~\text{s}$.
2. $\Delta N = A t = 5.0 \times 10^5 \times 600 = 3.0 \times 10^8$.

**Answer:** $3.0 \times 10^8$ decays (assuming constant activity).

### Example 7: Exponential decay

**Question:** A sample has $N_0 = 6.0 \times 10^{10}$ and $\lambda = 0.05~\text{min}^{-1}$. Calculate $N$ after $40~\text{min}$.

**Method:**
1. $N = 6.0 \times 10^{10} e^{-0.05 \times 40}$.
2. $N = 6.0 \times 10^{10} e^{-2.0}$.
3. $N = 8.12 \times 10^9$.

**Answer:** $8.1 \times 10^9$ nuclei.

### Example 8: Half-life from decay constant

**Question:** $\lambda = 3.0 \times 10^{-4}~\text{s}^{-1}$. Calculate the half-life.

**Method:**
1. $t_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.693}{3.0 \times 10^{-4}}$.
2. $t_{1/2} = 2.31 \times 10^3~\text{s}$.

**Answer:** $2.3 \times 10^3~\text{s}$ (about 38 min).

### Example 9: Time to decay to one-eighth

**Question:** How long does a sample with $\lambda = 3.0 \times 10^{-4}~\text{s}^{-1}$ take to fall to one-eighth of its activity?

**Method:**
1. One-eighth $= (1/2)^3$, so 3 half-lives.
2. $t = 3 \times 2.31 \times 10^3 = 6.93 \times 10^3~\text{s}$.

**Answer:** $6.9 \times 10^3~\text{s}$ (about 1.9 h).

### Example 10: Carbon dating

**Question:** A sample contains 99.2% of the carbon-14 expected in a new sample. The half-life is $5730~\text{years}$. Calculate the age.

**Method:**
1. $\lambda = \frac{0.693}{5730} = 1.210 \times 10^{-4}~\text{y}^{-1}$.
2. $N/N_0 = 0.992$.
3. $t = -\frac{\ln 0.992}{\lambda} = -\frac{-0.00803}{1.210 \times 10^{-4}}$.
4. $t = 66.4~\text{years}$.

**Answer:** about 66 years.

### Example 11: Mass–energy of 1 g

**Question:** Calculate the energy equivalent of $1.0~\text{g}$ of matter.

**Method:**
1. $E = mc^2 = 1.0 \times 10^{-3} \times 9.0 \times 10^{16}$.
2. $E = 9.0 \times 10^{13}~\text{J}$.

**Answer:** $9.0 \times 10^{13}~\text{J}$.

### Example 12: Sun's mass loss

**Question:** The Sun radiates $4.0 \times 10^{26}~\text{W}$. Estimate its mass loss per second.

**Method:**
1. $E = 4.0 \times 10^{26}~\text{J}$ each second.
2. $\Delta m = \frac{E}{c^2} = \frac{4.0 \times 10^{26}}{9.0 \times 10^{16}}$.
3. $\Delta m = 4.44 \times 10^9~\text{kg s}^{-1}$.

**Answer:** about $4.4 \times 10^9~\text{kg s}^{-1}$.

## 6. Exam-Style Questions (Full Solutions)

### Question 1

A nucleus of ${}^{235}_{92}\text{U}$ absorbs a neutron and undergoes fission into ${}^{141}_{56}\text{Ba}$ and ${}^{92}_{36}\text{Kr}$, emitting three neutrons. (a) Write the balanced equation. (b) Explain why energy is released. (c) State the form in which most of the energy appears.

**Solution:**
1. (a) ${}^{235}_{92}\text{U} + {}^{1}_{0}\text{n} \rightarrow {}^{141}_{56}\text{Ba} + {}^{92}_{36}\text{Kr} + 3{}^{1}_{0}\text{n}$.
2. Check: $A: 235 + 1 = 141 + 92 + 3 = 236$; $Z: 92 + 0 = 56 + 36 + 0 = 92$.
3. (b) The fission fragments have a higher binding energy per nucleon than uranium-235, so the total mass decreases; the mass difference is released as energy ($\Delta E = \Delta m c^2$).
4. (c) Most appears as kinetic energy of the fragments and neutrons, which becomes thermal energy in the reactor.

**Answer:** (a) as above; (b) higher binding energy per nucleon of fragments; (c) kinetic/thermal energy.

### Question 2

The mass of a ${}^{56}_{26}\text{Fe}$ nucleus is $9.288 \times 10^{-26}~\text{kg}$. Given $m_p = 1.673 \times 10^{-27}~\text{kg}$ and $m_n = 1.675 \times 10^{-27}~\text{kg}$, calculate (a) the mass defect, (b) the binding energy, and (c) the binding energy per nucleon.

**Solution:**
1. (a) 26 protons, 30 neutrons.
2. Mass of separate nucleons $= 26(1.673) + 30(1.675) = 43.498 + 50.250 = 93.748 \times 10^{-27}~\text{kg}$.
3. $\Delta m = (93.748 - 92.88) \times 10^{-27} = 0.868 \times 10^{-27}~\text{kg}$.
4. (b) $\text{BE} = 8.68 \times 10^{-28} \times 9.0 \times 10^{16} = 7.81 \times 10^{-11}~\text{J}$.
5. (c) Per nucleon $= \frac{7.81 \times 10^{-11}}{56} = 1.39 \times 10^{-12}~\text{J} \approx 8.7~\text{MeV}$.

**Answer:** (a) $8.68 \times 10^{-28}~\text{kg}$; (b) $7.8 \times 10^{-11}~\text{J}$; (c) $1.4 \times 10^{-12}~\text{J}$ per nucleon ($8.7~\text{MeV}$).

### Question 3

A radioactive isotope has a half-life of $6.0~\text{h}$. A sample initially contains $2.4 \times 10^{12}$ nuclei. (a) Calculate the decay constant in $\text{s}^{-1}$. (b) Calculate the number of nuclei remaining after $18~\text{h}$. (c) Calculate the initial activity.

**Solution:**
1. (a) $t_{1/2} = 6.0 \times 3600 = 2.16 \times 10^4~\text{s}$.
2. $\lambda = \frac{0.693}{2.16 \times 10^4} = 3.21 \times 10^{-5}~\text{s}^{-1}$.
3. (b) $18~\text{h} = 3$ half-lives, so $N = 2.4 \times 10^{12}/8 = 3.0 \times 10^{11}$.
4. (c) $A_0 = \lambda N_0 = 3.21 \times 10^{-5} \times 2.4 \times 10^{12} = 7.70 \times 10^7~\text{Bq}$.

**Answer:** (a) $3.2 \times 10^{-5}~\text{s}^{-1}$; (b) $3.0 \times 10^{11}$; (c) $7.7 \times 10^7~\text{Bq}$.

### Question 4

Explain what is meant by (a) the random nature of radioactive decay and (b) the spontaneous nature of radioactive decay. (c) Explain why the count rate from a weak source fluctuates.

**Solution:**
1. (a) It is impossible to predict when a particular nucleus will decay; each nucleus has a fixed probability of decaying per unit time, independent of other nuclei.
2. (b) Decay is not triggered or affected by external conditions such as temperature, pressure or chemical state; it occurs naturally because the nucleus is unstable.
3. (c) Each decay is a random event, so the number detected in a fixed time interval varies about an average value. The fluctuations are relatively larger for a small number of counts.

**Answer:** as above.

### Question 5

A source has an activity of $8.0 \times 10^5~\text{Bq}$ at time $t=0$ and $1.0 \times 10^5~\text{Bq}$ after $36~\text{min}$. (a) Show that three half-lives have elapsed. (b) Calculate the half-life. (c) Calculate the decay constant in $\text{s}^{-1}$.

**Solution:**
1. (a) $\frac{8.0 \times 10^5}{1.0 \times 10^5} = 8 = 2^3$, so 3 half-lives.
2. (b) $t_{1/2} = \frac{36}{3} = 12~\text{min}$.
3. (c) $t_{1/2} = 720~\text{s}$; $\lambda = \frac{0.693}{720} = 9.63 \times 10^{-4}~\text{s}^{-1}$.

**Answer:** (a) factor 8 = $2^3$; (b) $12~\text{min}$; (c) $9.6 \times 10^{-4}~\text{s}^{-1}$.

### Question 6

Explain, using the binding-energy-per-nucleon curve, why (a) fusion of light nuclei releases energy and (b) fission of heavy nuclei releases energy. (c) Why is iron-56 particularly stable?

**Solution:**
1. (a) Light nuclei have low binding energy per nucleon. Fusion produces a heavier nucleus with higher binding energy per nucleon, so the total mass decreases and energy is released.
2. (b) Heavy nuclei have lower binding energy per nucleon than intermediate-mass fragments. Fission produces fragments closer to the peak, so binding energy per nucleon increases, mass decreases and energy is released.
3. (c) Iron-56 has the maximum binding energy per nucleon (about $8.8~\text{MeV}$), so the most energy is required to dismantle it; it is the most stable nuclide.

**Answer:** as above.

## 7. Cheat Sheet

**Mass–energy:**
- $\Delta E = \Delta m c^2$.
- $1~\text{u} = 1.6605 \times 10^{-27}~\text{kg}$; $1~\text{u}\,c^2 = 931.5~\text{MeV}$.
- Mass defect $= (Zm_p + Nm_n) - m_{\text{nucleus}}$.
- Binding energy per nucleon peaks at iron-56 ($\sim 8.8~\text{MeV}$).

**Decay:**
- $A = \lambda N$.
- $N = N_0 e^{-\lambda t}$; $A = A_0 e^{-\lambda t}$.
- $t_{1/2} = \ln 2/\lambda \approx 0.693/\lambda$.
- After $n$ half-lives, fraction remaining $= (1/2)^n$.
- Random: unpredictable individual decay. Spontaneous: unaffected by environment.

**Fission/fusion:**
- Both increase binding energy per nucleon.
- Fission: heavy nucleus splits.
- Fusion: light nuclei join; needs high temperature to overcome repulsion.

**Practical:**
- Corrected count rate $=$ measured $-$ background.
- $\ln N$ vs $t$ is a straight line with gradient $-\lambda$.

## 8. Common Exam Mistakes

1. **Confusing mass defect with mass excess.** Mass defect is nucleus vs separate nucleons; mass excess is nuclide mass in u minus $A$.
2. **Forgetting to multiply by $c^2$.** A mass difference in kg is not an energy until multiplied by $9.0 \times 10^{16}$.
3. **Using atomic masses without accounting for electrons.** In precise calculations, electron masses must be included or cancelled consistently.
4. **Mixing u and kg.** Convert all masses to the same unit before subtracting.
5. **Dividing by the wrong number of nucleons.** Binding energy per nucleon uses $A$, not $Z$ or $N$.
6. **Saying iron-56 has the highest binding energy.** It has the highest binding energy **per nucleon**; the total binding energy generally increases with $A$.
7. **Saying fission releases energy because uranium is unstable.** The key is the increase in binding energy per nucleon of the fragments.
8. **Saying fusion needs high pressure only.** High temperature gives the nuclei enough kinetic energy to overcome electrostatic repulsion.
9. **Using $A = \lambda N$ with inconsistent units.** If $\lambda$ is in $\text{s}^{-1}$, $N$ is fine but time calculations must use seconds.
10. **Using $\log_{10}$ instead of $\ln$.** Exponential decay uses natural logarithms; $\ln 2 = 0.693$.
11. **Forgetting the minus sign in $t = -\ln(N/N_0)/\lambda$.** Since $N < N_0$, $\ln(N/N_0)$ is negative, so the time is positive.
12. **Treating half-life as the time for all nuclei to decay.** The sample never reaches exactly zero in the model; it halves repeatedly.
13. **Using the measured count rate as the activity.** The detector only detects a fraction of decays; correct for efficiency and background.
14. **Saying decay can be sped up by heating.** Radioactive decay is spontaneous and unaffected by temperature or chemical state.
