# Chapter 21: Thermal Physics - CAIE A Level Physics (9702) Study Notes

This chapter covers the CAIE A-Level Physics 9702 syllabus topics 14 (Temperature) and 16.1-16.2 (Internal energy and the first law of thermodynamics). It is examined on Paper 4 (structured questions) and Paper 1 (multiple choice). The big ideas: what temperature really measures, why energy can go in without the temperature rising (changes of state), and how to track energy with the first law of thermodynamics. Most of the calculation marks come from just three equations: $E = mc\Delta\theta$, $E = mL$ and $\Delta U = q + W$ - so the skill is knowing which one applies at each stage of a problem.

---

## 1. Theory

### 1.1 Temperature and thermal equilibrium

Temperature tells you the direction in which thermal energy flows. If two objects are placed in contact, energy flows from the hotter one to the cooler one. Energy flowing from a region of higher temperature to a region of lower temperature is called **thermal energy** (the mechanism - conduction, convection or radiation - does not matter here).

When two objects in contact are at the **same** temperature, there is no net transfer of thermal energy between them. They are said to be in **thermal equilibrium**. This is how a thermometer works: you put it in thermal contact with a substance, wait until its reading stops changing, and then the thermometer is in thermal equilibrium with the substance, so its reading tells you the temperature of the substance. Strictly, a thermometer always shows its own temperature - it only shows the substance's temperature once equilibrium is reached. This idea leads to the zeroth law of thermodynamics: if A is in thermal equilibrium with B, and B with C, then A is in thermal equilibrium with C.

### 1.2 Temperature scales and the thermodynamic scale

**Celsius scale.** The everyday scale, defined using two fixed points of water: the melting point of pure ice ($0^\circ\text{C}$) and the boiling point of pure water ($100^\circ\text{C}$), with the range divided into 100 equal divisions. There is nothing special about these fixed points: both change if the pressure changes or the water is impure. Also, a liquid-in-glass thermometer relies on the expansion of a particular liquid, which can be non-linear, so a mercury thermometer and an alcohol thermometer can be guaranteed to agree only at the fixed points, not in between.

**Thermodynamic (Kelvin) scale.** A better scale because it does not depend on the property of any particular substance. It is based on the idea that the average kinetic energy of the particles of a substance increases with temperature, and the average kinetic energy is the same for all substances at a given thermodynamic temperature. It has two fixed points:

- **absolute zero**, defined as $0\,\text{K}$ - the lowest possible temperature, at which it is impossible to remove any more energy from a substance (all substances have minimum internal energy; the kinetic energy of the molecules is zero and their electrical potential energy is minimum). It is not strictly true that matter has "no energy left" at absolute zero - the correct statement is that no more energy can be removed.
- the **triple point of water**, the temperature at which ice, water and water vapour can coexist, defined as $273.16\,\text{K}$ (equal to $0.01^\circ\text{C}$).

The gap between absolute zero and the triple point is divided into $273.16$ equal divisions, each of $1\,\text{K}$. This odd choice makes the size of a kelvin equal to the size of a degree Celsius, so conversions are easy.

Conversion between the two scales:

$$\theta\,(^\circ\text{C}) = T\,(\text{K}) - 273.15$$

$$T\,(\text{K}) = \theta\,(^\circ\text{C}) + 273.15$$

For most calculations the conversion factor is rounded to $273$. A **change** of $1\,\text{K}$ equals a **change** of $1^\circ\text{C}$, so $\Delta T = \Delta\theta$ - this is why it does not matter whether you use kelvin or degrees Celsius inside $E = mc\Delta\theta$.

**Advantage of the thermodynamic scale** (a classic 1-2 mark question): it is an absolute scale, not defined in terms of the property of any particular substance, so all thermometers agree on it; it has a true zero (absolute zero), the lowest possible temperature.

### 1.3 Thermometers and thermometric properties

Any device that measures temperature uses some physical property of a material that changes with temperature (a **thermometric property**). Examples from the syllabus:

- the density of a liquid
- the volume of a fixed mass of gas at constant pressure (constant-pressure gas thermometer)
- the resistance of a metal (resistance thermometer)
- the e.m.f. of a thermocouple (two junctions of different metals at different temperatures produce an e.m.f.)
- the length of a liquid column in a tube (liquid-in-glass thermometer)
- the colour of an electrically heated wire

A thermometer must be calibrated at two or more known temperatures, and the scale between them divided into equal divisions. Two different thermometers are only guaranteed to agree at the calibration points.

**Resistance thermometer vs thermocouple** - the coursebook's comparison table is worth learning:

| Feature | Resistance thermometer | Thermocouple thermometer |
|---|---|---|
| Robustness | very robust | robust |
| Range | thermistor: narrow range; resistance wire: wide range | can be very wide |
| Size | larger than a thermocouple, greater thermal capacity, slower acting | smaller, smaller thermal capacity, quicker acting, can measure temperature at a point |
| Sensitivity | thermistor: high sensitivity over a narrow range; resistance wire: less sensitive | can be sensitive if appropriate metals are chosen |
| Linearity | thermistor: fairly linear over a narrow range; resistance wire: good linearity | non-linear, so requires calibration |
| Remote operation | long conducting wires allow the operator to be at a distance | long conducting wires allow the operator to be at a distance |

Typical application questions: a thermocouple for measuring temperature at many different points on a car engine cylinder head (small and quick, measures at a point); a resistance thermometer or thermocouple for a nuclear reactor core (remote operation, wide range); a liquid-in-glass thermometer for a greenhouse.

### 1.4 Kinetic model of matter

The kinetic model describes matter in terms of moving particles (atoms or molecules):

- **Solid**: particles are close together, tightly bonded to their neighbours, and vibrate about fixed positions.
- **Liquid**: particles are close together but free to move around each other; bonds are weaker than in a solid.
- **Gas**: particles have broken free from their neighbours; they are widely separated and move freely within their container.

### 1.5 Changes of state and heating/cooling curves

Consider heating ice at a steady rate in a well-insulated container, from well below $0^\circ\text{C}$ until it becomes steam above $100^\circ\text{C}$. The graph of temperature against time has five sections:

| Section | What happens | Where the energy goes |
|---|---|---|
| AB | ice warms from below $0^\circ\text{C}$ to $0^\circ\text{C}$ | molecules vibrate more: **kinetic energy increases**; separation barely changes so potential energy is roughly constant |
| BC | ice melts at $0^\circ\text{C}$ (temperature constant) | molecules become more disordered, bonds break: **potential energy increases**; kinetic energy (temperature) unchanged |
| CD | water warms from $0^\circ\text{C}$ to $100^\circ\text{C}$ | molecules move faster: **kinetic energy increases**; potential energy roughly constant |
| DE | water boils at $100^\circ\text{C}$ (temperature constant) | molecules become completely separated from one another: **potential energy increases greatly**; kinetic energy unchanged |
| EF | steam warms above $100^\circ\text{C}$ | molecules move faster: **kinetic energy increases**; potential energy already at its maximum (zero, when molecules are fully separated) |

The key insight is that you can put energy into a substance **without its temperature rising**. During a change of state the energy goes into breaking the bonds between neighbouring molecules, i.e. into potential energy, not kinetic energy. Temperature is a measure of the average kinetic energy of the molecules, so while KE stays constant the temperature stays constant.

Melting takes much less energy than boiling the same mass. When a solid melts, each molecule breaks only one or two bonds with its immediate neighbours; when a liquid boils, each molecule breaks free of all of its neighbours (eight or nine bonds per molecule). This is why the specific latent heat of vaporisation of water ($2.26\,\text{MJ kg}^{-1}$) is roughly seven times its specific latent heat of fusion ($330\,\text{kJ kg}^{-1}$).

The same analysis applies to cooling curves: a flat region on a cooling curve (temperature steady while the substance is solidifying) happens because energy is still being lost to the surroundings, but it goes into forming bonds (potential energy decreases) rather than reducing kinetic energy. Cooling curves are used to find melting points: the flat region BC in the coursebook's octadecanoic acid experiment gives the melting point.

A caution from the coursebook: the "steam" you see above a kettle is not a gas - it is a cloud of tiny droplets of liquid water. Water vapour is an invisible gas.

### 1.6 Evaporation

A liquid can change to a gas without boiling - this is **evaporation**. It happens at any temperature (unlike boiling, which occurs throughout the liquid at a fixed temperature for a given pressure). In the liquid, molecules move with a range of speeds. The most energetic molecules near the surface can break free of the bulk of the liquid and escape into the vapour above it. Because the fastest molecules leave, the average kinetic energy of the molecules left behind falls - so the temperature of the evaporating liquid falls. This is why you feel cold when alcohol evaporates off your skin, or when you stand around wet in a breeze. The escaping molecules carry away energy even though no heat is supplied.

### 1.7 Internal energy

The **internal energy** of a system is defined as:

> the sum of the random distribution of kinetic and potential energies of the atoms or molecules of the system.

The kinetic part comes from the motion of the molecules (vibrating, moving around); the potential part is the electrical potential energy of the molecules due to their positions and the bonds between them. Raising the temperature of an object increases its internal energy (molecules move faster), and a change of state also increases internal energy (potential energy rises) even though the temperature does not change.

There are two ways to increase the internal energy of a system:

- **heating it** - energy transferred by heating, symbol $q$
- **doing work on it** - e.g. compressing a gas, or passing an electric current through it, symbol $W$

And two ways to decrease it: losing heat to the surroundings, or expanding so that it does work on its surroundings.

### 1.8 First law of thermodynamics

The first law is a formal statement of the conservation of energy:

$$\Delta U = q + W$$

where:

- $\Delta U$ is the **increase** in internal energy of the system (J)
- $q$ is the energy transferred **to the system** by heating (J)
- $W$ is the work done **on the system** (J)

Sign conventions (the most common place to lose marks - see Section 7):

- $q$ is positive when energy is transferred **to** the system by heating; negative when the system loses heat to its surroundings.
- $W$ is positive when work is done **on** the system (e.g. compressing a gas); negative when the system does work **on its surroundings** (e.g. the gas expands).
- $\Delta U$ is positive for an increase in internal energy.

**Work done by a gas changing volume.** When a gas changes volume at constant pressure $p$, the magnitude of the work done is

$$W = p\Delta V$$

where $\Delta V$ is the change in volume. If the gas **expands** ($\Delta V > 0$), it does work on its surroundings, so in the first law $W = -p\Delta V$ (work done on the gas is negative). If the gas is **compressed** ($\Delta V < 0$), work is done on the gas, and $W = +p\Delta V$. Note that $W = p\Delta V$ requires the pressure to be constant; if the pressure changes, you would need the area under a pressure-volume graph.

**Useful special cases:**

- Constant volume (no expansion or compression): $W = 0$, so $\Delta U = q$. All the heat supplied goes into internal energy.
- No heating (insulated, or a fast process): $q = 0$, so $\Delta U = W$. The change in internal energy equals the work done on the gas - this is how a bicycle pump barrel gets hot when you pump quickly, and why compressed gas gets hot while expanding gas cools (e.g. solid carbon dioxide forming when CO$_2$ escapes from a cylinder).
- An ideal gas at constant temperature has constant kinetic energy and (because there are no intermolecular forces) zero potential energy, so its internal energy is unchanged: $\Delta U = 0$, meaning $q = -W$.

### 1.9 Specific heat capacity

If you heat a material so its temperature rises, the energy required depends on three things: the mass $m$, the temperature change $\Delta\theta$, and the material itself.

The **specific heat capacity** $c$ of a substance is:

> the energy required per unit mass of the substance to raise its temperature by $1\,\text{K}$ (or $1^\circ\text{C}$).

"Specific" means per unit mass (per kg). The energy required to produce a temperature change is

$$E = mc\Delta\theta$$

Rearranged:

$$c = \frac{E}{m\Delta\theta}$$

Units: $\text{J kg}^{-1}\text{K}^{-1}$ (or $\text{J kg}^{-1}\ \ ^{\circ}\text{C}^{-1}$). Since a change of $1\,\text{K}$ equals a change of $1^{\circ}\text{C}$, the numerical value is the same either way.

Typical values of specific heat capacity (from the coursebook, in $\text{J kg}^{-1}\text{K}^{-1}$):

| Substance | $c$ / $\text{J kg}^{-1}\text{K}^{-1}$ |
|---|---|
| aluminium | 880 |
| copper | 380 |
| lead | 126 |
| glass | 500-680 |
| ice | 2100 |
| water | 4180 |
| seawater | 3950 |
| ethanol | 2500 |
| mercury | 140 |

Water has a very high specific heat capacity - that is why it is a good coolant and why coastal climates are mild. On a heating curve, the specific heat capacity is related to the gradient of the sloping sections: a steeper gradient means the substance heats up faster, so it has a lower specific heat capacity.

**Experiment: determining specific heat capacity (coursebook Box 21.1).**

A metal block of known mass $m$ (e.g. a 1.00 kg aluminium cylinder) is heated with an **electrical heater**, because the energy supplied is easy to determine. An ammeter and voltmeter measure the current and p.d., giving $P = VI$. A thermometer or temperature probe (with datalogger) monitors the temperature. The block must be insulated (lagged) and heated slowly so the energy has time to spread through the metal.

Method A (single measurement): $E = Pt = mc\Delta\theta$, so

$$c = \frac{Pt}{m\Delta\theta}$$

Method B (graph, better): record temperature $\theta$ as it rises and plot $\theta$ against $t$. Dividing $E = mc\Delta\theta$ by $\Delta t$:

$$\frac{E}{\Delta t} = mc\frac{\Delta\theta}{\Delta t}$$

so $P = mc \times \text{gradient}$, where the gradient of the graph is $\Delta\theta/\Delta t$. Hence

$$c = \frac{P}{m \times \text{gradient}}$$

Sources of error: some energy escapes to the surroundings, so more energy must be supplied per degree of temperature rise and the experimental value of $c$ comes out **too high**. This is a systematic error. One way to reduce it is to cool the block below room temperature before heating starts; then as the temperature passes room temperature the heat losses are (in principle) zero because there is no temperature difference with the surroundings.

### 1.10 Specific latent heat

Energy must be supplied to melt or boil a substance, and during this change of state the temperature stays constant. This energy is called **latent heat** ("latent" means hidden - the energy seems to disappear because the temperature does not rise).

The **specific latent heat** $L$ of a substance is:

> the energy required per kilogram of the substance to change its state without any change in temperature.

- **Specific latent heat of fusion**: melting (solid to liquid).
- **Specific latent heat of vaporisation**: boiling (liquid to gas).

The energy required to change the state of a mass $m$ is

$$E = mL$$

Units: $\text{J kg}^{-1}$. Note there is no "per degree" in the unit, because there is no temperature change.

For water:

- specific latent heat of fusion $= 330\,\text{kJ kg}^{-1} = 3.30 \times 10^5\,\text{J kg}^{-1}$
- specific latent heat of vaporisation $= 2.26\,\text{MJ kg}^{-1} = 2.26 \times 10^6\,\text{J kg}^{-1}$

The value of $L$ for boiling is roughly seven times the value for melting because boiling breaks several bonds per molecule while melting breaks only one or two (Section 1.5).

**Experiment: determining specific latent heat (coursebook Box 21.2).**

For vaporisation: a beaker of water is heated electrically and stands on a balance. A wattmeter (or ammeter + voltmeter) gives the rate of energy supply, and a thermometer confirms the water stays at $100^\circ\text{C}$. The mass is recorded at equal time intervals as the water boils; the graph of mass against time is a straight line whose gradient is the rate of mass loss $\Delta m/\Delta t$. Then

$$L = \frac{\text{rate of supply of energy}}{\text{rate of loss of mass}} = \frac{P}{\Delta m/\Delta t}$$

For fusion: ice is heated electrically in a funnel and the melted water is collected in a beaker on a balance. To correct for ice that melts due to the warmth of the surroundings, the mass of water collected is first measured with the heater switched off, and this "background" melting is subtracted.

Sources of error: when heating water to produce steam, some energy escapes to the surroundings, so the measured energy is greater than that supplied to the water - this systematic error makes the measured $L$ **too high**. When ice is melted, energy from the surroundings conducts into the ice, so the measured value of $L$ is an **underestimate**.

A related quantity: the specific latent heat of **sublimation** (solid to gas directly, e.g. solid carbon dioxide) is greater than both fusion and vaporisation because all the bonds are broken in a single step.

---

## 2. Definition Sheet

Learn these word-perfect - the examiner's mark schemes quote them almost exactly, and the words that carry the marks are in bold. The mark-scheme wording is given where it is known from past papers.

> **Thermal equilibrium** - no net transfer of thermal energy between two objects in contact at the same temperature.

The syllabus puts it as "regions of equal temperature are in thermal equilibrium". The examiner wants the idea that at the same temperature there is no net transfer of energy. Related idea worth knowing: the zeroth law of thermodynamics - if A is in thermal equilibrium with B, and B with C, then A is in thermal equilibrium with C.

> **Thermodynamic temperature** - temperature measured on a scale that does not depend on the property of any particular substance; it is proportional to the average kinetic energy of the molecules of the substance.

This is why all thermometers agree on the thermodynamic scale: it is not defined by the expansion of any one liquid or the resistance of any one metal.

> **Kelvin** - the unit of thermodynamic temperature; $1\,\text{K}$ is $\frac{1}{273.16}$ of the thermodynamic temperature of the triple point of water.

A change of $1\,\text{K}$ equals a change of $1^\circ\text{C}$, but absolute temperatures are not interchangeable: $T/\text{K} = \theta/^\circ\text{C} + 273.15$.

> **Absolute zero** - the lowest possible temperature, $0\,\text{K} = -273.15^\circ\text{C}$, at which no more energy can be removed from a substance.

At absolute zero the molecules have minimum kinetic energy (and minimum electrical potential energy). It is not strictly true that matter has "no energy left" - the correct statement is that no more energy can be removed.

> **Specific heat capacity** - the energy required per unit mass of a substance to raise its temperature by $1\,\text{K}$ (or $1^\circ\text{C}$).

Mark-scheme wording: "(thermal) energy per unit mass (to raise temperature by) 1 K". Units: $\text{J kg}^{-1}\text{K}^{-1}$. The three elements that carry marks: energy, unit mass, and temperature rise of 1 K.

> **Specific latent heat** - the energy required per kilogram of a substance to change its state without any change in temperature.

Mark-scheme wording (w19/41 Q3(a), full marks): "(thermal) energy per (unit) mass (to change state); heat transfer during a change of state at constant temperature." You must include both the per-unit-mass idea and the constant-temperature condition.

> **Specific latent heat of fusion** - the (thermal) energy required to convert unit mass of solid to liquid at its normal melting point / without any change in temperature.

Mark-scheme note (w08/04 Q2(a)): merely saying "per 1 kg of ice to water" scores at most 1 mark - "unit mass" **and** the constant-temperature condition are both required.

> **Specific latent heat of vaporisation** - the (thermal) energy required to convert unit mass of liquid to gas at its normal boiling point / without any change in temperature.

The only difference from fusion is the change of state: liquid to gas (boiling) instead of solid to liquid (melting).

> **Internal energy** - the sum of the random distribution of kinetic and potential energies of the atoms or molecules of the system.

Mark-scheme note (November 2009 examiner report): almost everyone says "the sum of the kinetic and potential energies associated with the molecules", but very few say the **random distribution** - that phrase is in the syllabus definition, so use it. The kinetic part comes from molecular motion; the potential part is the electrical potential energy due to the positions of, and bonds between, the molecules.

> **First law of thermodynamics** - the increase in internal energy of a system equals the energy transferred to the system by heating plus the work done on the system: $\Delta U = q + W$.

Mark-scheme wording (w08/04 Q4(a)): "$\Delta U = q + w$" (a correct word equation is also accepted). Cambridge sign convention: $q$ is positive when energy is transferred **to** the system by heating; $W$ is positive when work is done **on** the system; $\Delta U$ is the **increase** in internal energy. The words "to", "on" and "increase" carry the marks.

> **Evaporation** - the change of state from liquid to gas that takes place at any temperature at the surface of the liquid; the most energetic molecules escape, so the average kinetic energy (and hence the temperature) of the liquid falls.

The key contrast with boiling: evaporation occurs at any temperature and only at the surface; boiling occurs throughout the liquid at a fixed temperature for a given pressure. Evaporation cools the liquid because the fastest molecules leave - this is why you feel cold when wet in a breeze.

---

## 3. Formula Sheet

| Formula | Meaning of symbols | SI units | When to use |
|---|---|---|---|
| $T = \theta + 273.15$ | $T$ = thermodynamic temperature (K), $\theta$ = Celsius temperature ($^\circ\text{C}$) | K, $^\circ\text{C}$ | Converting Celsius to kelvin (round the factor to 273 in calculations) |
| $\theta = T - 273.15$ | same symbols | K, $^\circ\text{C}$ | Converting kelvin to Celsius |
| $\Delta T = \Delta\theta$ | a change of 1 K equals a change of 1 $^\circ\text{C}$ | K or $^\circ\text{C}$ | Inside $E = mc\Delta\theta$ either scale works |
| $\Delta U = q + W$ | $\Delta U$ = increase in internal energy (J); $q$ = energy transferred **to** the system by heating (J); $W$ = work done **on** the system (J) | J | The first law: tracking energy for any system (heating, compression, expansion) |
| $W = p\Delta V$ | $p$ = pressure (Pa), $\Delta V$ = change in volume ($\text{m}^3$) | J | Work done by/on a gas changing volume at constant pressure; sign depends on whether the gas expands (work done by gas, negative $W$ in the first law) or is compressed (work done on gas, positive $W$) |
| $E = mc\Delta\theta$ | $E$ = energy (J), $m$ = mass (kg), $c$ = specific heat capacity ($\text{J kg}^{-1}\text{K}^{-1}$), $\Delta\theta$ = temperature change (K or $^\circ\text{C}$) | J | Heating or cooling with no change of state |
| $c = \frac{E}{m\Delta\theta}$ | as above | $\text{J kg}^{-1}\text{K}^{-1}$ | Finding $c$ from experiment data |
| $E = mL$ | $E$ = energy (J), $m$ = mass (kg), $L$ = specific latent heat of fusion or vaporisation ($\text{J kg}^{-1}$) | J | Melting, boiling or any change of state at constant temperature |
| $L = \frac{E}{m}$ | as above | $\text{J kg}^{-1}$ | Finding $L$ from experiment data |
| $E = Pt$ | $E$ = energy supplied by a heater (J), $P$ = heater power (W), $t$ = time (s) | J | Electrical heating experiments: energy supplied by a heater at power $P$ for time $t$ |
| $P = VI$ | $P$ = heater power (W), $V$ = p.d. (V), $I$ = current (A) | W | Electrical heating experiments (energy supplied $= Pt$) |
| $P = mc \times \text{gradient}$ | gradient $= \Delta\theta/\Delta t$ of the temperature-time graph ($\text{K s}^{-1}$) | W | Finding $c$ from a $\theta$-$t$ graph |
| $L = \frac{P}{\Delta m/\Delta t}$ | $\Delta m/\Delta t$ = rate of mass loss ($\text{kg s}^{-1}$) | $\text{J kg}^{-1}$ | Finding $L$ from a boiling/boil-off experiment |
| $P_1t_1 - P_2t_2 = (m_1 - m_2)L$ | two runs at different heater powers over equal times | J | Eliminating the heat loss to surroundings when finding $L$ |

---

## 4. Methods (Question Types & Methods)

Cambridge asks the same few thermal questions year after year. Here is how to attack each one.

### Type 1: "Calculate the energy to heat something and change its state"

The question gives you a mass, a starting state, an ending state, and values of $c$ and $L$. You must add up the energy for each stage.

Method:

1. Write down the journey as a chain of stages, e.g. ice at $-18^\circ\text{C}$ to water at $20^\circ\text{C}$ = heat ice + melt ice + heat water.
2. Check the units of $c$ and $L$: if they are per gram ($\text{J g}^{-1}\text{K}^{-1}$ or $\text{J g}^{-1}$), keep the mass in grams; if per kg, convert the mass to kg. Mixing these up destroys the answer.
3. For each stage decide: temperature change (use $E = mc\Delta\theta$) or change of state (use $E = mL$).
4. Sum every stage. If the question mentions heat losses, add a loss term or state the assumption that the system is insulated.

### Type 2: "Use the first law with given $q$ and $w$"

Method:

1. Read the question for direction words. "Heated", "energy supplied to the gas", "heat transferred to the system" mean $q$ positive. "Loses heat", "cools by radiating" mean $q$ negative.
2. "Compressed", "work done **on** the gas" mean $W$ positive. "Expands", "does work on its surroundings" mean $W$ negative. If the gas expands at constant pressure with volume change $\Delta V$, the work done by the gas is $p\Delta V$, so $W = -p\Delta V$ in the first law.
3. Substitute into $\Delta U = q + W$ and state the answer with units and the correct sign (a negative $\Delta U$ means internal energy decreased).

### Type 3: "Find specific heat capacity from experiment data"

Method:

1. Find the power supplied: $P = VI$ (or it is given directly, or given via a wattmeter/joulemeter reading).
2. Energy supplied in time $t$: $E = Pt$.
3. If one temperature rise $\Delta\theta$ is measured: $c = Pt/(m\Delta\theta)$.
4. If a graph of $\theta$ against $t$ is given: take the gradient of the straight line, then $c = P/(m \times \text{gradient})$.
5. Comment on heat losses: energy escaping to the surroundings means the measured $c$ is too high (a systematic error). Starting below room temperature, insulating, and heating slowly reduce the problem.

### Type 4: "Find specific latent heat"

Method:

1. Measure (or read off a graph) the mass that changes state and the time interval, and find the heater power $P = VI$.
2. Energy supplied $= Pt$. If no heat loss is assumed: $L = Pt/m$.
3. With heat losses, correct for them:
   - **Heater-off measurement**: measure the mass that changes state due to the surroundings alone in the same time, and subtract it from the heater-on mass (this is the funnel experiment for ice, w08/04 Q2).
   - **Two-power method**: run at two different heater powers for equal times; the heat loss term is the same in both runs, so subtracting the two energy equations eliminates it (w19/41 Q3).
4. State whether the result is an over- or underestimate and why (see Section 7).

### Type 5: "Explain the regions of a heating/cooling curve"

Method:

1. Sloping sections: temperature changes, so the **kinetic energy** of the molecules changes (faster/slower motion); separation barely changes, so potential energy is roughly constant.
2. Flat sections: a change of state is happening, so bonds are being broken or formed and the **potential energy** changes; kinetic energy (and therefore temperature) is constant.
3. When asked why melting needs less energy than boiling: melting breaks one or two bonds per molecule, boiling breaks all of them (eight or nine per molecule).
4. For a cooling curve, remember the temperature can stay steady while energy is still being lost - the energy loss goes into forming bonds, not lowering KE.

### Type 6: "Mixture / temperature change (calorimetry) problems"

These give you a hot substance and a cold substance (often ice added to warm water, sometimes in a container that also changes temperature) and ask for a final temperature or a value of $c$ or $L$.

Method:

1. State the energy balance: energy lost by the hot bodies = energy gained by the cold bodies (assuming no exchange with the surroundings).
2. Write one term for every body that changes temperature: $mc\Delta\theta$ (use the actual temperature change of each, e.g. $38 - 23$ for the warm water, $0 - (-18)$ for the ice while warming).
3. Write an $mL$ term for every body that changes state (the melting ice).
4. Solve for the unknown. Remember the final equilibrium temperature applies to everything, and any melted ice is water that then warms up.

The classic example (s18/42 Q3): warm water + aluminium can + ice at $-18^\circ\text{C}$. Energy lost by can and water $= mc\Delta\theta$ for each; energy gained by the ice $=$ warming the ice $+$ melting it $+$ warming the melted water.

### Type 7: "Which energy goes to KE or PE on each graph section?"

Method: on a temperature-time graph, **sloping** sections are KE changes (molecules moving faster or slower) and **flat** sections are PE changes (bonds broken or formed at a change of state). On a potential energy against separation graph, remember that PE is negative for bonded molecules and rises towards zero as molecules separate - so separating molecules increases their potential energy.

### Type 8: Definitions and short explanations (worth easy marks, learn them word-perfect)

- Specific heat capacity: energy required per unit mass of a substance to raise its temperature by 1 K (or 1 $^\circ\text{C}$).
- Specific latent heat: energy required per kilogram of a substance to change its state without any change in temperature.
- Specific latent heat of fusion: as above for melting (solid to liquid).
- Specific latent heat of vaporisation: as above for boiling (liquid to gas).
- Internal energy: the sum of the random distribution of kinetic and potential energies of the atoms or molecules of a system.
- Absolute zero: the lowest possible temperature, $0\,\text{K}$ ($-273.15^\circ\text{C}$), at which no more energy can be removed from a substance.
- Thermal equilibrium: two objects in contact at the same temperature, with no net transfer of thermal energy between them.

### Type 9: Thermometer questions

- State which thermometric property the device uses (resistance of a metal, e.m.f. of a thermocouple, volume of a gas at constant pressure, density of a liquid, etc.).
- Explain why the thermodynamic scale is better: it does not depend on the property of any particular substance.
- Choose a thermometer for a job using the table in Section 1.3 (thermocouple for a point measurement or a wide range; resistance thermometer for accuracy over a wide range; thermistor for a sensitive, narrow-range measurement).

---

## 5. Solved Examples

Real coursebook and CAIE past-paper questions, worked fully. Each one shows the question, the method, the answer, and the mark-scheme point the examiner is looking for.

### Example 1: Finding specific heat capacity from $E = mc\Delta\theta$ (coursebook worked example)

**Question:** $26\,400\,\text{J}$ of energy is supplied to a well-insulated $2.0\,\text{kg}$ block of aluminium, and its temperature rises from $20^\circ\text{C}$ to $35^\circ\text{C}$. Determine the specific heat capacity of aluminium.

**Method:**
1. Write down the known quantities: $E = 26\,400\,\text{J}$, $m = 2.0\,\text{kg}$, $\Delta\theta = 35 - 20 = 15^\circ\text{C}$ ($= 15\,\text{K}$).
2. Rearrange $E = mc\Delta\theta$ to make $c$ the subject: $c = \frac{E}{m\Delta\theta}$.
3. Substitute and calculate.

**Answer:**

$$c = \frac{E}{m\Delta\theta} = \frac{26\,400}{2.0 \times 15} = 880\,\text{J kg}^{-1}\text{K}^{-1}$$

$c = 880\,\text{J kg}^{-1}\text{K}^{-1}$, which matches the accepted value for aluminium.

**What the examiner wants:** the correct rearrangement of $E = mc\Delta\theta$, the temperature change taken as $35 - 20 = 15\,\text{K}$ (not 35 K), and the answer quoted with units.

### Example 2: Multi-stage heating with a change of state (coursebook worked example)

**Question:** How much energy is needed to change $0.20\,\text{kg}$ of ice at $-18^\circ\text{C}$ into water at $20^\circ\text{C}$? Data: $c_{\text{ice}} = 2100\,\text{J kg}^{-1}\text{K}^{-1}$, $L_{\text{fusion}} = 3.30 \times 10^5\,\text{J kg}^{-1}$, $c_{\text{water}} = 4180\,\text{J kg}^{-1}\text{K}^{-1}$.

**Method:**
1. Break the journey into stages: warm the ice ($-18$ to $0$), melt the ice at $0^\circ\text{C}$, warm the water ($0$ to $20$).
2. Energy to warm the ice: $E_1 = mc_{\text{ice}}\Delta\theta = 0.20 \times 2100 \times 18 = 7560\,\text{J}$.
3. Energy to melt the ice: $E_2 = mL_{\text{fusion}} = 0.20 \times 3.30 \times 10^5 = 66\,000\,\text{J}$.
4. Energy to warm the melted water: $E_3 = mc_{\text{water}}\Delta\theta = 0.20 \times 4180 \times 20 = 16\,720\,\text{J}$.
5. Add every stage.

**Answer:**

$$E = E_1 + E_2 + E_3 = 7560 + 66\,000 + 16\,720 = 90\,280\,\text{J} \approx 9.0 \times 10^4\,\text{J}$$

About $9.0 \times 10^4\,\text{J}$. Note that melting alone (the $mL$ term) dominates.

**What the examiner wants:** all three energy terms written out separately (a mark each), consistent units, and the total quoted to 2 s.f. The same method is used in Example 7 (s18/42).

### Example 3: The first law of thermodynamics with given $q$ and $W$ (coursebook Question 3)

**Question:** (a) A gas is heated by supplying $250\,\text{kJ}$ of energy; at the same time it is compressed so that $500\,\text{kJ}$ of work is done on the gas. Calculate the change in internal energy. (b) The same gas is heated as before with $250\,\text{kJ}$, but this time it is allowed to expand so that it does $200\,\text{kJ}$ of work on its surroundings. Calculate the change in internal energy.

**Method:**
1. Decide the signs from the direction words. Heating the gas means $q = +250\,\text{kJ}$ in both parts.
2. (a) Compression means work done **on** the gas: $W = +500\,\text{kJ}$.
3. (b) The gas does work **on its surroundings**: $W = -200\,\text{kJ}$.
4. Substitute into $\Delta U = q + W$.

**Answer:**

(a) $$\Delta U = q + W = 250 + 500 = 750\,\text{kJ}$$ - the internal energy increases by $750\,\text{kJ}$.

(b) $$\Delta U = q + W = 250 + (-200) = +50\,\text{kJ}$$ - the internal energy increases by $50\,\text{kJ}$.

**What the examiner wants:** the sign of $W$ is the whole question. "Compressed" = work on the gas = positive; "expands, does work on surroundings" = negative. State the answer with units and the direction of the change.

### Example 4: Kettle question - estimating $c$ and $L$ from a rated power (w02/04 Q1)

**Question:** A kettle is rated at $2.3\,\text{kW}$. A mass of $750\,\text{g}$ of water at $20^\circ\text{C}$ is poured in. When switched on, it takes $2.0$ minutes for the water to start boiling. In a further $7.0$ minutes, one half of the mass of water is boiled away. Estimate the specific heat capacity of water and the specific latent heat of vaporisation.

**Method:**
1. Convert: $m = 0.75\,\text{kg}$, $P = 2300\,\text{W}$, $t_1 = 120\,\text{s}$, $t_2 = 420\,\text{s}$.
2. Specific heat capacity: energy supplied to reach boiling is $E = Pt_1 = 2300 \times 120 = 276\,000\,\text{J}$, with $\Delta\theta = 100 - 20 = 80\,\text{K}$. Then $c = \frac{Pt_1}{m\Delta\theta}$.
3. Specific latent heat: energy supplied while boiling is $E = Pt_2 = 2300 \times 420 = 966\,000\,\text{J}$, and the mass boiled away is $m = 0.75/2 = 0.375\,\text{kg}$. Then $L = \frac{Pt_2}{m}$.
4. State the assumption (all the kettle's energy goes into the water) and its effect on the estimates.

**Answer:**

$$c = \frac{276\,000}{0.75 \times 80} = 4600\,\text{J kg}^{-1}\text{K}^{-1}$$

$$L = \frac{966\,000}{0.375} = 2.6 \times 10^6\,\text{J kg}^{-1}$$

$c \approx 4600\,\text{J kg}^{-1}\text{K}^{-1}$ (higher than the true $4180$ because of the losses), $L \approx 2.6 \times 10^6\,\text{J kg}^{-1}$.

**What the examiner wants:** the two energy balances ($Pt = mc\Delta\theta$ and $Pt = mL$), the unit conversions (grams to kg, minutes to seconds), and the assumption about no heat loss. Because some energy is in fact lost to the kettle and the surroundings, the energy actually absorbed by the water is less than $Pt$, so the calculated values are **overestimates**. (This is a genuine 2002 Paper 4 question; the mark scheme was not in the research pack, so treat the numbers as a worked estimate.)

### Example 5: Latent heat of fusion with a heater-off correction (w08/04 Q2, 7 marks)

**Question:** (a) Define specific latent heat of fusion. (b) Crushed ice at $0^\circ\text{C}$ is placed in a funnel with an electric heater, and the melted water is collected in a beaker. With the heater off, $16.6\,\text{g}$ of water is collected in $10.0$ minutes. With the heater on, $64.7\,\text{g}$ is collected in $5.0$ minutes, and the energy supplied to the heater is $18\,000\,\text{J}$. (i) State why the mass of water is determined with the heater switched off. (ii) Suggest how it can be determined that the ice is melting at a constant rate. (iii) Calculate a value for the specific latent heat of fusion of ice.

**Method:**
1. Definition: the (thermal) energy required to convert unit mass of solid to liquid at its normal melting point / without any change in temperature.
2. (i) The heater-off run makes allowance for heat gains from the atmosphere (ice melting due to the surroundings).
3. (ii) Constant rate of production of droplets from the funnel, or a constant mass of water collected per minute in the beaker.
4. (iii) Find the mass melted by the heater alone: with the heater off, ambient heat melts $16.6\,\text{g}$ in $10$ minutes, so in $5$ minutes it melts $16.6/2 = 8.3\,\text{g}$. Mass melted by the heater: $m = 64.7 - 8.3 = 56.4\,\text{g} = 56.4 \times 10^{-3}\,\text{kg}$.
5. Use $mL = 18\,000$.

**Answer:**

$$L = \frac{18\,000}{56.4 \times 10^{-3}} = 3.2 \times 10^5\,\text{J kg}^{-1} = 320\,\text{kJ kg}^{-1}$$

$L = 320\,\text{kJ kg}^{-1}$ (close to the accepted $330\,\text{kJ kg}^{-1}$).

**What the examiner wants:** in the definition, "unit mass" **and** the constant-temperature condition - merely saying "per 1 kg of ice to water" scores at most 1 mark. The heater-off correction is the point of the calculation: using the raw $64.7\,\text{g}$ (forgetting the correction) gives $278\,\text{kJ kg}^{-1}$ and loses most of the marks (using $m = 48.1\,\text{g}$ scores at most 2).

### Example 6: Latent heat of vaporisation by the two-power method (w19/41 Q3, 10 marks)

**Question:** (a) State what is meant by specific latent heat. (b) A student finds the specific latent heat of vaporisation of a liquid by boiling it with an electric heater on a balance. From $0$ to $10$ minutes the heater runs at $I = 1.2\,\text{A}$, $V = 230\,\text{V}$ and $56\,\text{g}$ of liquid evaporates. From $12$ to $22$ minutes the heater runs at $I = 1.0\,\text{A}$, $V = 190\,\text{V}$ and $32\,\text{g}$ evaporates. The rate of loss of thermal energy to the surroundings is the same in both runs. (i) Determine the mass evaporated from $12.0$ to $22.0$ minutes. (ii) Explain why, although the power of the heater is changed, the rate of loss of thermal energy to the surroundings may be assumed to be constant. (iii) Determine a value for the specific latent heat of vaporisation $L$. (iv) Calculate the rate at which thermal energy is transferred to the surroundings.

**Method:**
1. Definition: (thermal) energy per (unit) mass (to change state); heat transfer during a change of state at constant temperature.
2. (i) Read the mass off the balance-time graph: $32\,\text{g}$.
3. (ii) The temperature difference between the liquid and the surroundings does not change, because the liquid stays at its boiling point throughout.
4. (iii) Write the energy balance for each run. In $10$ minutes ($600\,\text{s}$), energy supplied = energy to vaporise the liquid + heat lost to surroundings ($H$): $230 \times 1.2 \times 600 = 56L + H$ and $190 \times 1.0 \times 600 = 32L + H$. Subtract the equations to eliminate $H$: $(276 - 190) \times 600 = (56 - 32)L$.
5. (iv) Substitute the unrounded value of $L$ back into the first equation to find $H$, then divide by $600\,\text{s}$.

**Answer:**

$$86 \times 600 = 24L \qquad \Rightarrow \qquad L = \frac{51\,600}{24} = 2150\,\text{J g}^{-1} \approx 2.2 \times 10^3\,\text{J g}^{-1}$$

$$H = 165\,600 - (56 \times 2150) = 45\,200\,\text{J} \qquad \Rightarrow \qquad \text{rate} = \frac{45\,200}{600} = 75\,\text{W}$$

$L = 2.2 \times 10^3\,\text{J g}^{-1}$ (mark scheme value $2200\,\text{J g}^{-1}$) and the rate of loss of thermal energy to the surroundings is $75\,\text{W}$. Both match the official mark scheme.

**What the examiner wants:** the definition with both points (per unit mass + constant temperature); the explanation that the temperature difference to the surroundings is unchanged because the liquid stays at its boiling point; the two energy equations written with the heat loss term $H$ included; and the subtraction that eliminates $H$.

### Example 7: Calorimetry - ice in warm water (s18/42 Q3, 7 marks)

**Question:** An aluminium can of mass $160\,\text{g}$ contains $330\,\text{g}$ of warm water at $38^\circ\text{C}$. A mass of $48\,\text{g}$ of ice at $-18^\circ\text{C}$ from a freezer is added. The ice melts and the final temperature of the can and its contents is $23^\circ\text{C}$. Data: $c_{\text{aluminium}} = 0.910\,\text{J g}^{-1}\text{K}^{-1}$, $c_{\text{ice}} = 2.10\,\text{J g}^{-1}\text{K}^{-1}$, $c_{\text{water}} = 4.18\,\text{J g}^{-1}\text{K}^{-1}$. (i) Show that the loss in thermal energy of the can and the warm water is $2.3 \times 10^4\,\text{J}$. (ii) Calculate a value $L$ for the specific latent heat of fusion of ice.

**Method:**
1. (i) Both the can and the warm water cool from $38^\circ\text{C}$ to $23^\circ\text{C}$, a fall of $15\,\text{K}$. Energy lost $= mc\Delta\theta$ for each, and add.
2. (ii) Energy balance: energy lost by can and water = energy gained by the ice. The ice gains energy in three parts: warming from $-18^\circ\text{C}$ to $0^\circ\text{C}$, melting at $0^\circ\text{C}$, and warming the melted water from $0^\circ\text{C}$ to $23^\circ\text{C}$.
3. Write the full equation and solve for $L$.

**Answer:**

(i) $$\text{loss} = (160 \times 0.910 \times 15) + (330 \times 4.18 \times 15) = 2184 + 20\,691 = 22\,875\,\text{J} \approx 2.3 \times 10^4\,\text{J}$$

(ii) $$2.3 \times 10^4 = (48 \times 2.10 \times 18) + 48L + (48 \times 4.18 \times 23)$$

$$2.3 \times 10^4 = 1814 + 48L + 4615$$

$$48L = 1.66 \times 10^4$$

$$L = \frac{1.66 \times 10^4}{48} = 350\,\text{J g}^{-1}$$

$L = 350\,\text{J g}^{-1}$ (i.e. $350\,\text{kJ kg}^{-1}$), consistent with the accepted value of $330\,\text{kJ kg}^{-1}$.

**What the examiner wants:** for the "show that" part, full working of both $mc\Delta\theta$ terms (you cannot just write the final number - the answer is given); for $L$, all three energy terms for the ice written separately: warming the ice, melting it, and warming the melted water.

### Example 8: Melting explained by kinetic theory (s18/42 Q3(a), 3 marks)

**Question:** During melting, a solid becomes liquid with little or no change in volume. Use kinetic theory to explain why, during the melting process, thermal energy is required although there is no change in temperature.

**Method:** state the three mark-scheme points in order: what happens to the bonds, what happens to the energy, and why the energy must be thermal.

**Answer:**
- (during melting,) bonds between atoms/molecules are broken
- potential energy of atoms/molecules is increased
- no/little work done so the required input of energy is thermal

**What the examiner wants:** exactly those three ideas. The temperature does not change because the energy goes into potential energy (breaking bonds), not into kinetic energy - the kinetic energy (and so the temperature) of the molecules stays constant.

### Example 9: First law and internal energy of an ideal gas (w08/04 Q4, 4 marks)

**Question:** (a) State the first law of thermodynamics. (b) A fixed mass of an ideal gas is kept at a constant temperature. Explain why its internal energy does not change.

**Method:**
1. (a) Quote the equation or a correct word version: the increase in internal energy of a system equals the energy transferred to the system by heating plus the work done on the system.
2. (b) Split internal energy into its kinetic and potential parts and deal with each: kinetic energy depends on temperature; potential energy depends on intermolecular forces.

**Answer:**
(a) $\Delta U = q + w$ (a correct word equation also accepted).

(b) Kinetic energy is constant because the temperature is constant; potential energy is constant because there are no intermolecular forces (in an ideal gas); so there is no change in internal energy.

**What the examiner wants:** in the definition, the words "on", "to" and "increase" carry the marks (the 2009 examiner report: incomplete answers like "$+w$ is the work done", "$+q$ is the heat supplied" and "$+\Delta U$ is the change in internal energy" were common and lost marks). For part (b), both reasons are required - constant temperature (KE) and no intermolecular forces (PE).

### Other recurring question types (mark schemes not in the pack)

Two more recurring types, described generically because the mark schemes were not in the research pack:

- **Kettle/heater questions** (e.g. November 2002 Paper 4 Q1): use the rated power and times to estimate $c$ and $L$, then state an assumption (no heat loss) and whether the estimate is an over- or underestimation. Fully worked in Example 4.
- **First-law narrative questions** (e.g. the coursebook end-of-chapter question on carbon dioxide): explain cooling using $\Delta U = q + W$ - when a gas expands rapidly, it does work on its surroundings ($W < 0$), little heat is supplied ($q \approx 0$), so its internal energy (and hence temperature) falls enough for the solid to form.

---

## 6. Cheat Sheet

**All the formulas**

$$T/\text{K} = \theta/^\circ\text{C} + 273.15, \qquad \Delta T = \Delta\theta$$

$$\Delta U = q + W \qquad (q = \text{heat to system}, W = \text{work on system})$$

$$W = p\Delta V \qquad (\text{magnitude; } W < 0 \text{ in the first law when the gas expands})$$

$$E = mc\Delta\theta, \qquad c = \frac{E}{m\Delta\theta} \qquad [\text{J kg}^{-1}\text{K}^{-1}]$$

$$E = mL, \qquad L = \frac{E}{m} \qquad [\text{J kg}^{-1}]$$

$$P = VI, \qquad P = mc \times \text{gradient}, \qquad L = \frac{P}{\Delta m/\Delta t}$$

**Key definitions (quote them exactly)**

- Thermal equilibrium: no net transfer of thermal energy between two objects in contact at the same temperature.
- Absolute zero: $0\,\text{K} = -273.15^\circ\text{C}$; the lowest possible temperature; no more energy can be removed from a substance.
- Thermodynamic scale: does not depend on the property of any particular substance; fixed points absolute zero and the triple point of water ($273.16\,\text{K}$).
- Internal energy: the sum of the random distribution of kinetic and potential energies of the atoms or molecules of a system.
- Specific heat capacity: energy required per unit mass to raise the temperature by 1 K.
- Specific latent heat: energy required per kilogram to change state without any change in temperature; fusion = melting, vaporisation = boiling.
- Evaporation: change from liquid to gas at any temperature; the fastest molecules escape, so the liquid cools.

**Key numbers**

- $c_{\text{water}} = 4180\,\text{J kg}^{-1}\text{K}^{-1}$, $c_{\text{aluminium}} = 880$, $c_{\text{ice}} = 2100$, $c_{\text{copper}} = 380$
- $L_{\text{fusion, water}} = 330\,\text{kJ kg}^{-1}$, $L_{\text{vaporisation, water}} = 2.26\,\text{MJ kg}^{-1}$ (about 7 times the fusion value)
- Triple point of water: $273.16\,\text{K} = 0.01^\circ\text{C}$

**Common traps (see Section 7 for the full list)**

- Forgetting $+273.15$ when converting to kelvin (a change of $1\,\text{K}$ equals a change of $1^\circ\text{C}$, but absolute temperatures are not interchangeable).
- Getting the sign of $W$ wrong in $\Delta U = q + W$: compression = work on the gas = positive; expansion = work by the gas = negative.
- Ignoring heat losses in experiments (measured $c$ and $L$ come out too high for a heater; $L$ for ice comes out too low because surroundings melt it).
- Mixing units of $c$ and $L$ (per gram vs per kg).
- Forgetting the "without any change in temperature" clause in the definition of specific latent heat.
- Saying temperature measures "degree of hotness" instead of the direction of energy flow / average kinetic energy of molecules.

---

## 7. Common Exam Mistakes

These come from the examiner reports and mark-scheme notes in the research pack (principally the November 2009 Principal Examiner Report, Paper 41).

**1. The first law sign conventions (the single biggest source of lost marks).** In the 2009 examiner report on the first-law question, the examiner noted that incomplete answers such as "$+w$ is the work done" (rather than the work done **on the system**), "$+q$ is the heat supplied" (rather than the heat supplied **to the system**), and "$+\Delta U$ is the change in internal energy" (rather than the **increase** in internal energy) were common. The word "on", "to" and "increase" carry the marks. Also: when a gas expands and does work on its surroundings, that work is negative in $\Delta U = q + W$; when the gas is compressed, work done on it is positive. Watch out for the alternative textbook convention $\Delta U = q - W$ (with $W$ = work done **by** the gas) - the CAIE formula sheet and syllabus use $\Delta U = q + W$, so follow the direction words in the question and substitute accordingly.

**2. Internal energy definition omits "random distribution".** The 2009 examiner report: most candidates said internal energy is "the sum of the kinetic and potential energies associated with the molecules of the gas", but very few mentioned that it is the **random distribution** of the kinetic and potential energies that is significant. That phrase is in the syllabus definition - use it.

**3. Substituting volume in cm$^3$ instead of m$^3$ in $W = p\Delta V$.** The 2009 report notes that candidates "had difficulty in substituting the volume in m$^3$ rather than cm$^3$". Convert $1\,\text{cm}^3 = 10^{-6}\,\text{m}^3$ before using $W = p\Delta V$.

**4. Not linking the first law to expansion cooling.** In the same question, very few candidates explained that when a gas does work on its surroundings with no heat supplied, the work done by the gas equals the decrease in its internal energy ($q = 0$, so $\Delta U = W = -p\Delta V$). This is the physics behind compressed gas cooling and the bicycle pump getting hot.

**5. Vague temperature answers.** On a question asking what observations show that temperature indicates the direction of thermal energy transfer, most candidates said temperature is the "degree of hotness" or mentioned only melting/boiling. The credit-worthy points: energy flows from higher to lower temperature, and the amount of energy transferred depends on mass and specific heat capacity as well as temperature difference.

**6. Steady temperature does not mean melting.** In a heating experiment where the temperature stopped rising, most candidates attributed the constant temperature to melting. The expected deduction: when the rate of rise is zero, the power input equals the rate of energy loss from the block. A steady temperature just means equilibrium between input and loss - only a flat section **at the melting/boiling point** means a change of state.

**7. Evaporation vs boiling.** Candidates struggled to state that evaporation occurs at any temperature of the liquid (it is a surface effect driven by the fastest molecules escaping), while boiling occurs throughout the liquid at a fixed temperature for a given pressure. Also note the distinction between boiling (energy goes into breaking bonds, PE increases) and evaporation (the liquid cools because the most energetic molecules leave).

**8. Definition traps in specific latent heat.** The 2008 mark scheme warns: "reference to 1 kg or to ice to water scores max 1 mark" for the definition of specific latent heat of fusion. You must say **per unit mass** (or per kg) **and** at the melting point / without any change in temperature.

**9. Forgetting the heater-off correction.** In the funnel experiment, using the raw heater-on mass of $64.7\,\text{g}$ (instead of $64.7 - 8.3 = 56.4\,\text{g}$ after subtracting what the surroundings melted) gives $L = 278\,\text{kJ kg}^{-1}$ and loses most of the marks. Any experiment with a change of state needs the "background" mass-loss measurement subtracted.

**10. Systematic vs random error for heat losses.** Heat losses from a heater experiment consistently make the measured $c$ (or $L$) too high - that is a systematic error, not a random one, because it always acts in the same direction. Remedies: insulate, heat slowly so energy spreads, or start below room temperature so losses balance out during the run.

**11. "Show that" questions need the full working.** The examiner reports stress that when the command word is "show" or "derive", the answer is given, so a full explanation of the method is required - you cannot just write the final number.

**12. Calculator and unit slips.** Common small errors that cost marks: forgetting that a change of $1\,\text{K} = 1^\circ\text{C}$ (so $\Delta\theta$ needs no conversion), keeping masses in grams when $c$ is in $\text{J kg}^{-1}\text{K}^{-1}$, and giving answers to the wrong number of significant figures. Quote final values to 2-3 s.f. with units.

---

*Sources: CAIE 9702 syllabus (2025-2027), Cambridge International AS & A Level Physics coursebook Chapter 21, June 2018 Paper 42 Q3, October/November 2019 Paper 41 Q3, November 2008 Paper 4 Q2 and Q4, November 2009 Principal Examiner Report (Paper 41 and Paper 22).*
