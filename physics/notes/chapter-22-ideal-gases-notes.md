# Chapter 22: Ideal Gases - CAIE A Level Physics (9702) Study Notes

This is the complete A2 chapter on ideal gases, written to the Cambridge International AS & A Level Physics 9702 syllabus (Topic 15: Ideal Gases). Everything here is exam-relevant: definitions Cambridge mark schemes actually credit, the exact equations on your data sheet, the derivation you must be able to reproduce, and the question types that keep appearing in Paper 4.

The data sheet values you get in the exam (and can quote without remembering):

- molar gas constant: $R = 8.31\ \text{J K}^{-1}\ \text{mol}^{-1}$
- Avogadro constant: $N_A = 6.02 \times 10^{23}\ \text{mol}^{-1}$
- Boltzmann constant: $k = 1.38 \times 10^{-23}\ \text{J K}^{-1}$

---

## 1. Theory

### 1.1 The ideal gas

A **gas** is a substance with no fixed shape or volume: its particles are far apart and in constant, random, fast motion. The four measurable properties of a gas are pressure $p$, volume $V$, temperature $T$ and the amount of substance (mass or number of moles).

An **ideal gas** is a theoretical gas that obeys the equation of state

$$pV = nRT$$

at all pressures and temperatures. Equivalently, for a fixed amount of gas it obeys

$$\frac{pV}{T} = \text{constant}$$

The examiner-friendly definition you should write (this is the one mark schemes credit):

> An ideal gas obeys $pV = nRT$ (or $pV \propto T$) for all pressures and temperatures, where $n$ and $R$ are constant.

Two details examiners complain about (June 2022 examiner report, Paper 41):
- Saying "it follows $pV = nRT$" is only equivalent to "it obeys $pV \propto T$" when you make clear that $n$ and $R$ are constants.
- Define all symbols you use in definition-type questions.

From the kinetic model, an ideal gas is also described as one whose molecules have **negligible volume** and exert **no forces on each other** (except during collisions).

### 1.2 Brownian motion

If you look at smoke particles or pollen grains in a liquid through a microscope, they jiggle about in a jerky, erratic, random path. This is **Brownian motion**: the visible particles are constantly being bombarded from all sides by the much smaller, faster molecules of the surrounding fluid. Because the hits are unequal in number and direction at any instant, the particle is knocked around randomly.

Brownian motion is evidence that:
- molecules exist and are in **constant random motion**,
- molecules are far smaller than the particles they buffet,
- molecules move **faster** than the visible particles (a small particle of mass $M$ and speed $V$ has comparable kinetic energy to one molecule of mass $m$ and speed $v$, so since $M \gg m$, it follows that $v \gg V$).

Exam answer (2 - 3 marks): "Visible particles are continuously and unevenly bombarded by molecules of the surrounding fluid. The bombardment is unequal, so the particle moves randomly. This shows molecules are in constant random motion."

### 1.3 Temperature scales

Thermodynamic (kelvin) temperature is the scale used in every gas equation:

$$T\ (\text{K}) = \theta\ (^\circ\text{C}) + 273.15$$

- Absolute zero is $0\ \text{K} = -273.15\ ^\circ\text{C}$: the lowest possible temperature.
- A temperature difference is the same number in K and °C: $\Delta T = \Delta \theta$.
- In gas calculations, use $T$ in kelvin, always. Never substitute Celsius into $pV = nRT$.

### 1.4 The mole and Avogadro constant

The **mole** is the SI base unit of amount of substance. One mole of any substance contains the same number of particles (atoms, molecules or ions) as there are atoms in 0.012 kg of carbon-12. That number is the **Avogadro constant**:

$$N_A = 6.02 \times 10^{23}\ \text{mol}^{-1}$$

Number of particles and number of moles:

$$N = nN_A$$

Mass and moles:

$$n = \frac{m}{M_r}$$

where $m$ is the mass in grams and $M_r$ is the molar mass in $\text{g mol}^{-1}$ (numerically equal to the relative atomic/molecular mass). In SI you may see $n = \frac{m}{M}$ with $m$ in kg and $M$ in $\text{kg mol}^{-1}$.

Trap: a mole of oxygen molecules, $\text{O}_2$, has molar mass about $32\ \text{g mol}^{-1}$. 1.6 kg of oxygen is 50 mol of $\text{O}_2$ molecules but 100 mol of oxygen **atoms**, because each molecule contains two atoms. Questions deliberately probe whether you count molecules or atoms.

### 1.5 Boyle's and Charles's laws

**Boyle's law.** For a **fixed mass of gas at constant temperature**, pressure and volume are inversely proportional:

$$p \propto \frac{1}{V} \quad \Rightarrow \quad pV = \text{constant}$$

For a change between two states:

$$p_1V_1 = p_2V_2$$

Graphs: $p$ against $V$ is a smooth curve (hyperbola); $p$ against $\frac{1}{V}$ is a straight line through the origin.

**Charles's law.** For a **fixed mass of gas at constant pressure**, volume is proportional to thermodynamic temperature:

$$V \propto T \quad \Rightarrow \quad \frac{V}{T} = \text{constant}$$

Extrapolating a volume-temperature graph to zero volume gives $T = 0\ \text{K}$: this is how absolute zero was first discovered.

### 1.6 The ideal gas equation $pV = nRT$

Combining Boyle's law and Charles's law for a fixed mass gives $\frac{pV}{T} = \text{constant}$. Including the amount of gas gives the equation of state:

$$pV = nRT$$

- $p$ = pressure of the gas (Pa)
- $V$ = volume of the gas ($\text{m}^3$)
- $n$ = number of moles (mol)
- $R$ = molar gas constant, $8.31\ \text{J K}^{-1}\ \text{mol}^{-1}$
- $T$ = thermodynamic temperature (K)

In molecular form, with $N$ = number of molecules:

$$pV = NkT$$

- $N$ = number of molecules
- $k$ = Boltzmann constant, $k = \dfrac{R}{N_A} = 1.38 \times 10^{-23}\ \text{J K}^{-1}$

$k$ is "the gas constant per molecule": it connects a microscopic quantity (energy of one molecule) to a macroscopic one (temperature). Both forms are on your allowed data; the exam expects you to pick whichever matches what you know ($n$ or $N$).

Combined gas law for a fixed mass changing between two states (all three quantities change):

$$\frac{p_1V_1}{T_1} = \frac{p_2V_2}{T_2}$$

Useful remembered value: one mole of ideal gas at room temperature and pressure (20 °C, $1.01 \times 10^5$ Pa) occupies about $0.0240\ \text{m}^3 = 24.0\ \text{dm}^3$.

### 1.7 Assumptions of the kinetic theory of gases

The kinetic theory explains the macroscopic properties of a gas (pressure, volume, temperature) in terms of the motion of its molecules. The assumptions (learn all of them - mark schemes take "any two" to "any five" of these):

1. A gas contains a **very large number** of particles (atoms or molecules) in **continuous random motion**.
2. The **volume of the particles is negligible** compared with the volume of the container.
3. **Forces between particles are negligible** except during collisions (so between collisions they travel in straight lines at constant velocity).
4. **Collisions are perfectly elastic**: no kinetic energy is lost in collisions between molecules or with the walls.
5. The **time of a collision is negligible** compared with the time between collisions.
6. The molecules obey Newton's laws of motion (and the gas is a large enough sample that statistical averages are meaningful).

Examiner note (Nov 2021, Paper 42): a common error is not recognising that the kinetic theory deals with the **particles that make up the gas**, not with the gas as a whole. Write "molecules", not "gas".

### 1.8 Explaining pressure in terms of molecules

Pressure arises from collisions of molecules with the container walls:

1. Molecules collide elastically with the walls; on a head-on collision with speed $c$ the molecule's velocity reverses, so its momentum changes by $2mc$ (perpendicular to the wall).
2. By Newton's laws, the wall exerts a force on the molecule, so the molecule exerts an equal force on the wall.
3. Force = rate of change of momentum, so each collision contributes a small force; the huge number of collisions per second averages to a steady force.
4. Pressure = force per unit area.

So pressure increases if: more molecules hit the walls per second (more molecules, or smaller volume), or each collision is harder (faster molecules, i.e. higher temperature).

### 1.9 Derivation of $pV = \frac{1}{3}Nm\langle c^2 \rangle$ (you must be able to reproduce this)

**Step 1 - momentum change of one molecule (1-D model).** A molecule of mass $m$ in a cube of side $L$ moves with speed $c$ perpendicular to a face. It hits the face elastically and rebounds with speed $-c$: its momentum changes from $+mc$ to $-mc$, so

$$\text{change in momentum} = 2mc$$

**Step 2 - time between collisions with the same face.** Between successive hits on the same face the molecule travels to the opposite face and back, a distance $2L$ at speed $c$:

$$\text{time} = \frac{2L}{c}$$

**Step 3 - force from one molecule.** Force = rate of change of momentum:

$$F = \frac{2mc}{2L/c} = \frac{mc^2}{L}$$

**Step 4 - pressure from one molecule.** Pressure = force / area of face ($L^2$):

$$p_{\text{one}} = \frac{mc^2/L}{L^2} = \frac{mc^2}{L^3} = \frac{mc^2}{V}$$

**Step 5 - extend to $N$ molecules.** Each molecule has a different speed; replace $c^2$ by the mean-square speed $\langle c^2 \rangle$ and multiply by $N$:

$$p = \frac{Nm\langle c^2 \rangle}{V} \quad \Rightarrow \quad pV = Nm\langle c^2 \rangle$$

**Step 6 - extend to three dimensions.** Molecules move randomly in all directions. The speed squared splits into components: $c^2 = c_x^2 + c_y^2 + c_z^2$. On average no direction is preferred, so

$$\langle c_x^2 \rangle = \langle c_y^2 \rangle = \langle c_z^2 \rangle = \frac{1}{3}\langle c^2 \rangle$$

Only the $x$-component contributes to pressure on the $x$-faces, so the pressure is one third of the value found in 1-D:

$$\boxed{pV = \frac{1}{3}Nm\langle c^2 \rangle}$$

Since $Nm$ is the total mass of the gas and $Nm/V$ is its density $\rho$, an equivalent form is

$$p = \frac{1}{3}\rho\langle c^2 \rangle$$

This equation is on the formula sheet, but the derivation is examined (e.g. 9702/42/O/N/21 Q3, 11 marks - solved in Example 11). The exam will give you $m$, $u$ and $L$ and ask you to deduce the change in momentum, the time between collisions, the force, and the pressure one step at a time.

### 1.10 Mean-square speed and r.m.s. speed

The **mean-square speed** $\langle c^2 \rangle$ is the average of the squares of the speeds of all the molecules:

$$\langle c^2 \rangle = \frac{c_1^2 + c_2^2 + \cdots + c_N^2}{N}$$

The **root-mean-square (r.m.s.) speed** is the square root of that average:

$$c_{\text{r.m.s.}} = \sqrt{\langle c^2 \rangle}$$

$c_{\text{r.m.s.}}$ is slightly larger than the plain mean speed (squaring gives more weight to fast molecules). It is the speed that appears in the kinetic theory equations. Common values: air molecules at room temperature have $c_{\text{r.m.s.}} \approx 500\ \text{m s}^{-1}$, comparable to the speed of sound.

### 1.11 Temperature and molecular kinetic energy

Equate the two expressions for $pV$:

$$\frac{1}{3}Nm\langle c^2 \rangle = NkT$$

Divide by $N$ and rearrange:

$$\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}kT$$

The left-hand side is the **mean translational kinetic energy** $\langle E_K \rangle$ of one molecule:

$$\langle E_K \rangle = \frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}kT$$

Key conclusions:

- The **mean translational kinetic energy of a molecule is proportional to the thermodynamic temperature**. Temperature is a measure of the average random kinetic energy of the molecules. At $T = 0\ \text{K}$ the translational kinetic energy would be zero.
- $\langle E_K \rangle$ depends **only on $T$**, not on the mass or type of molecule. At the same temperature, heavy molecules (e.g. $\text{CO}_2$) and light molecules (e.g. $\text{H}_2$) have the same mean kinetic energy - but the lighter ones move faster.
- Doubling $T$ (in kelvin) doubles the mean kinetic energy, but since $\text{KE} \propto c^2$, the r.m.s. speed increases by only $\sqrt{2}$.
- "Translational" matters: a molecule can also spin (rotational kinetic energy). The statement applies to translational kinetic energy.

Useful rearrangements:

$$c_{\text{r.m.s.}} = \sqrt{\frac{3kT}{m}}$$

and, using $m = M/N_A$ and $k = R/N_A$:

$$c_{\text{r.m.s.}} = \sqrt{\frac{3RT}{M}}$$

where $M$ is the **molar mass in $\text{kg mol}^{-1}$** (convert from $\text{g mol}^{-1}$ by dividing by 1000). Also from the density form:

$$c_{\text{r.m.s.}} = \sqrt{\frac{3p}{\rho}}$$

For $n$ moles of a monatomic ideal gas, the total internal energy (all kinetic, no potential energy because there are no intermolecular forces) is

$$U = \frac{3}{2}nRT = \frac{3}{2}NkT$$

so a temperature change $\Delta T$ at constant volume changes the internal energy by

$$\Delta U = \frac{3}{2}Nk\Delta T = \frac{3}{2}nR\Delta T$$

### 1.12 Real gases deviate from ideal behaviour

A real gas obeys the ideal gas equation only when its molecules behave like the ideal model. Deviations show up at:

- **High pressure**: the gas is squeezed so the molecules' own volume is no longer negligible compared with the container volume, and molecules are close enough for intermolecular forces to matter. The gas is harder to compress than ideal, and attractive forces pull molecules together, reducing the pressure on the walls.
- **Low temperature**: molecules slow down, intermolecular forces become significant, and the gas may condense to a liquid (e.g. nitrogen condenses at 77 K). Near condensation the volume-temperature graph curves away from the straight line predicted by Charles's law.

So the ideal gas equation works best for gases at low pressure and high temperature (far from condensation). In explanations, name the two failing assumptions: **negligible molecular volume** and **negligible intermolecular forces**.

### 1.13 Isotherms

An **isotherm** is a line on a $p$-$V$ graph showing states of a fixed mass of gas at one constant temperature. From $pV = nRT$ with $T$ constant, $pV = \text{constant}$: the isotherm is a hyperbola ($p \propto 1/V$). A family of isotherms for increasing temperature sit further from the origin, since $pV = nRT$ is larger at higher $T$. A straight-line version plots $p$ against $1/V$: gradient $= nRT$, so higher temperature gives a steeper line through the origin.

---

## 2. Definition Sheet

These are the definitions Cambridge mark schemes actually credit. Learn them word-perfect - definition questions are the cheapest marks in the paper.

> **Ideal gas** - a gas that obeys the equation of state $pV = nRT$ (or $\frac{pV}{T} = \text{constant}$, or $pV \propto T$) at all pressures and temperatures, for a fixed amount of gas with $n$ and $R$ constant.
> Mark-scheme wording (F/M/19): "gas obeys the formula $\frac{pV}{T} = \text{constant}$ (or $pV = nRT$); symbols $V$ and $T$ explained". If you write "follows $pV = nRT$", you must add "at all pressures and temperatures, with $n$ and $R$ constant" and define every symbol (June 2022 examiner report).

> **Mole** - the SI base unit of amount of substance: the amount of any substance that contains the same number of particles (atoms, molecules or ions) as there are atoms in 0.012 kg of carbon-12. In one word: the amount of substance containing $N_A$ particles.

> **Avogadro constant** - the number of particles (atoms, molecules or ions) in one mole of a substance: $N_A = 6.02 \times 10^{23}\ \text{mol}^{-1}$.

> **Boltzmann constant** - the gas constant per molecule: $k = \frac{R}{N_A} = 1.38 \times 10^{-23}\ \text{J K}^{-1}$. It connects the microscopic energy of a single molecule to the macroscopic temperature.

> **Mean-square speed** - the average (mean) of the squares of the speeds of all the molecules: $\langle c^2 \rangle = \frac{c_1^2 + c_2^2 + \cdots + c_N^2}{N}$. (Mark scheme answer for "what is meant by $\langle c^2 \rangle$": "mean-square speed (of atoms/molecules)".)

> **r.m.s. speed** - the square root of the mean-square speed: $c_{\text{r.m.s.}} = \sqrt{\langle c^2 \rangle}$. It is slightly larger than the plain average speed.

> **Mean translational kinetic energy of a molecule** - $\langle E_K \rangle = \frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}kT$: the average kinetic energy of a molecule due to its random translational motion. It is proportional to the thermodynamic temperature and independent of the mass or type of molecule.

> **Elastic collision** - a collision in which kinetic energy is conserved (no kinetic energy is lost). Nov 2021 mark scheme: "no loss of kinetic energy". Momentum conservation, or "energy is conserved" in general, does not score.

> **Brownian motion** - the erratic, jerky, random motion of a visible particle caused by continuous, uneven bombardment by the much smaller, faster molecules of the surrounding fluid. It is evidence that molecules exist and are in constant random motion.

> **Thermodynamic temperature** - temperature measured on the kelvin scale, $T\ (\text{K}) = \theta\ (^\circ\text{C}) + 273.15$. Absolute zero is $0\ \text{K} = -273.15\ ^\circ\text{C}$, the lowest possible temperature.

**The kinetic theory assumptions** (state any of these, phrased about molecules):

1. A gas contains a very large number of particles in continuous random motion.
2. The volume of the particles is negligible compared with the volume of the container.
3. Forces between particles are negligible except during collisions.
4. Collisions are perfectly elastic (no kinetic energy is lost).
5. The time of a collision is negligible compared with the time between collisions.
6. Molecules obey Newton's laws of motion.

Mark-scheme phrasing for "state two assumptions" [2]: "molecules have negligible volume (compared with the container)"; "no forces between molecules except during collisions"; "molecules are in random motion"; "collisions are instantaneous". Never write "the gas has negligible volume" - the theory is about the particles that make up the gas.

**Internal energy of an ideal gas** - all kinetic, no potential energy: the potential energy of the molecules is zero because there are no intermolecular forces (M/J/24 mark-scheme point). So $U = \frac{3}{2}NkT$.

---

## 3. Formula Sheet

| Formula (LaTeX) | Meaning of symbols | SI units | When to use |
|---|---|---|---|
| $$pV = nRT$$ | $p$ pressure, $V$ volume, $n$ number of moles, $R = 8.31\ \text{J K}^{-1}\ \text{mol}^{-1}$, $T$ thermodynamic temperature | Pa, $\text{m}^3$, mol, K | Equation of state, molar form. Find $p$, $V$, $n$ or $T$. |
| $$pV = NkT$$ | $N$ number of molecules, $k = 1.38 \times 10^{-23}\ \text{J K}^{-1}$ | Pa, $\text{m}^3$, -, K | Equation of state, molecular form. Find $N$ or $T$. |
| $$k = \frac{R}{N_A}$$ | $k$ Boltzmann constant, $R$ gas constant, $N_A = 6.02 \times 10^{23}\ \text{mol}^{-1}$ | $\text{J K}^{-1}$ | Converting between molar and molecular quantities. |
| $$N = nN_A$$ | $N$ number of particles, $n$ moles | -, mol | Mole to molecule count (mind atoms vs molecules). |
| $$n = \frac{m}{M_r}$$ | $m$ mass in g, $M_r$ molar mass in $\text{g mol}^{-1}$ | g, $\text{g mol}^{-1}$ | Mass to moles before using $pV = nRT$. |
| $$p_1V_1 = p_2V_2$$ | subscripts 1, 2 = before, after | any consistent units | Fixed mass, constant temperature (Boyle's law). |
| $$\frac{V_1}{T_1} = \frac{V_2}{T_2}$$ | | any consistent units | Fixed mass, constant pressure (Charles's law). |
| $$\frac{p_1V_1}{T_1} = \frac{p_2V_2}{T_2}$$ | | any consistent units | Fixed mass, all three change. |
| $$pV = \frac{1}{3}Nm\langle c^2 \rangle$$ | $\langle c^2 \rangle$ mean-square speed | Pa, $\text{m}^3$, kg | Links macroscopic $p$, $V$ to molecular $m$, $N$, speeds. |
| $$p = \frac{1}{3}\rho\langle c^2 \rangle$$ | $\rho$ density of gas | Pa, $\text{kg m}^{-3}$, $\text{m}^2\text{s}^{-2}$ | Find $\langle c^2 \rangle$ or $c_{\text{r.m.s.}}$ from density and pressure. |
| $$c_{\text{r.m.s.}} = \sqrt{\langle c^2 \rangle}$$ | r.m.s. speed | $\text{m s}^{-1}$ | Square-root the mean-square speed. |
| $$\langle E_K \rangle = \frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}kT$$ | mean translational KE per molecule | J | Mean KE of one molecule; find $T$ or $c_{\text{r.m.s.}}$. |
| $$c_{\text{r.m.s.}} = \sqrt{\frac{3kT}{m}} = \sqrt{\frac{3RT}{M}}$$ | $M$ molar mass in $\text{kg mol}^{-1}$ | $\text{m s}^{-1}$ | r.m.s. speed from temperature. |
| $$c_{\text{r.m.s.}} = \sqrt{\frac{3p}{\rho}}$$ | $p$ pressure, $\rho$ density | $\text{m s}^{-1}$ | r.m.s. speed from pressure and density. |
| $$U = \frac{3}{2}NkT = \frac{3}{2}nRT$$ | $U$ internal energy of ideal gas | J | Total kinetic energy of all molecules. |
| $$\Delta U = \frac{3}{2}Nk\Delta T$$ | $\Delta U$ internal energy change | J | Internal energy change for a temperature change. |
| $$T/\text{K} = \theta/^\circ\text{C} + 273.15$$ | | K, °C | Convert temperature before any substitution. |
| $$V_{\text{sphere}} = \frac{4}{3}\pi r^3$$ | $r$ radius of molecule | $\text{m}^3$ | Estimate volume occupied by molecules (FM19 Q2 style: radius $3.2 \times 10^{-11}$ m gives total occupied volume $4 \times 10^{-8}\ \text{m}^3$). |

---

## 4. Methods (Question Types & Methods)

These are the ways Cambridge actually asks about ideal gases in Paper 4 (verified against real papers and examiner reports). Each method below is the mark-scheme-shaped route to full marks.

### 4.1 Define an ideal gas (2 marks)

Method: write "$pV \propto T$ (at all temperatures and pressures) for a fixed amount of gas" and name the symbols ($V$ = volume, $T$ = thermodynamic temperature). Alternative acceptable versions: "obeys $pV = nRT$ at all pressures and temperatures (with $n$ and $R$ constant)" or, from the kinetic model, "no intermolecular forces; negligible volume of molecules". Examiner report (June 2022): if you say "follows $pV = nRT$", you must state $n$ and $R$ are constant, and define the symbols.

### 4.2 State the assumptions of the kinetic theory (2 - 5 marks)

Method: write down as many of the five assumptions in Section 1.7 as requested, phrased about **molecules**, e.g. "molecules are in constant random motion", "volume of molecules negligible compared with volume of container", "no forces between molecules except during collisions", "collisions are perfectly elastic", "collision time negligible". Never write "the gas is elastic" - the theory is about the particles of the gas.

### 4.3 Explain how molecular motion produces pressure (2 - 3 marks)

Method: molecules collide with (container) walls; collisions are elastic so a molecule's momentum changes (reverses) at the wall; force = rate of change of momentum (Newton's laws); the wall experiences many collisions per second; pressure = force per unit area. For a change question ("what happens when temperature rises / more gas is pumped in"): faster molecules hit harder and more often (temperature), or more molecules hit per second (amount), so pressure increases.

### 4.4 Derive $pV = \frac{1}{3}Nm\langle c^2 \rangle$ (4 - 6 marks)

Method: follow the numbered steps in Section 1.9. When the question gives a molecule of mass $m$ and speed $u$ in a cube of side $L$ and asks for expressions in terms of $m$, $u$ and $L$ only:
- change in momentum $= 2mu$
- time between collisions with the same face $= \dfrac{2L}{u}$
- force $= \dfrac{2mu}{2L/u} = \dfrac{mu^2}{L}$
- pressure on one face $= \dfrac{mu^2/L}{L^2} = \dfrac{mu^2}{L^3}$

Then extend: average over $N$ molecules (replace $u^2$ with $\langle c^2 \rangle$), and divide by 3 for three dimensions ($\langle c_x^2 \rangle = \frac{1}{3}\langle c^2 \rangle$), giving $pV = \frac{1}{3}Nm\langle c^2 \rangle$. Examiner report (Nov 2021): the two most common errors are omitting the factor of 2 (in $2mu$ and $2L/u$) and inventing letters that were not defined in the question.

### 4.5 Show that the mean kinetic energy is $\frac{3}{2}kT$ (2 marks)

Method: start from $pV = NkT$ (easier, says the examiner report) and $pV = \frac{1}{3}Nm\langle c^2 \rangle$. Equate: $\frac{1}{3}Nm\langle c^2 \rangle = NkT$, cancel $N$, rearrange to $\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}kT$, and state that $\frac{1}{2}m\langle c^2 \rangle = E_K$ is the mean translational kinetic energy. If you start from $pV = nRT$ instead, you must state $N = nN_A$ and $R = kN_A$ at some point.

### 4.6 Use $pV = nRT$ to find one variable (2 - 3 marks)

Method (e.g. find $n$): convert $T$ to kelvin; convert $V$ to $\text{m}^3$ (1 $\text{dm}^3 = 10^{-3}\ \text{m}^3$, 1 litre $= 10^{-3}\ \text{m}^3$, $1\ \text{cm}^3 = 10^{-6}\ \text{m}^3$); rearrange $n = \frac{pV}{RT}$; substitute with $R = 8.31$; answer with units. Then convert moles to mass or molecules if asked: $m = nM_r$ (g) or $N = nN_A$. Show the rearranged equation - you get method marks even if the arithmetic slips.

### 4.7 Find the number of molecules using $pV = NkT$ (2 - 3 marks, often "show that")

Method: rearrange $N = \frac{pV}{kT}$ with $k = 1.38 \times 10^{-23}$, or do $n = \frac{pV}{RT}$ then $N = nN_A$ (both routes are credited). For a "show that $N = 6.6 \times 10^{23}$" style question, write the substitution line in full with all numbers - the final line alone is rarely enough for all three marks. Examiner report (May/June 2021): candidates who quoted the formula with $T$ as the subject scored more readily.

### 4.8 Calculate the r.m.s. speed (2 - 4 marks)

Three routes, pick the one the question feeds you:
- From temperature and molecular mass: $c_{\text{r.m.s.}} = \sqrt{\frac{3kT}{m}}$ where $m$ is the mass of one molecule (find it from $m = \frac{M}{N_A}$ if you are given molar mass). Remember: convert molar mass from $\text{g mol}^{-1}$ to $\text{kg mol}^{-1}$.
- From temperature and molar mass: $c_{\text{r.m.s.}} = \sqrt{\frac{3RT}{M}}$ with $M$ in $\text{kg mol}^{-1}$.
- From pressure and density: $\langle c^2 \rangle = \frac{3p}{\rho}$, then square root.

Method marks: convert $T$ to kelvin (this is the single most common mark-loser), calculate $\langle c^2 \rangle$ first, then take the square root. Finishing with $\langle c^2 \rangle$ and never square-rooting loses the final mark (examiner report, Nov 2021).

### 4.9 Calculate the mean kinetic energy of a molecule (2 - 3 marks)

Method: $\langle E_K \rangle = \frac{3}{2}kT$ with $T$ in kelvin. Answer is a tiny number, typically $10^{-21}$ J at room temperature ($6.21 \times 10^{-21}$ J at 300 K). Comparisons: at the same temperature all molecules have the same mean translational KE; a heavier molecule has a smaller r.m.s. speed.

### 4.10 Internal energy change of an ideal gas (2 - 3 marks)

Method: an ideal gas has no intermolecular forces, so all internal energy is kinetic: $U = \frac{3}{2}NkT$. A temperature change $\Delta T$ (in kelvin, and a Celsius change is numerically the same) gives $\Delta U = \frac{3}{2}Nk\Delta T = \frac{3}{2}nR\Delta T$. At constant temperature, $\Delta U = 0$ regardless of what happens to pressure or volume (examiner report, June 2022: many candidates wrongly gave $\Delta U \neq 0$ for a constant-temperature expansion).

### 4.11 Two-state problems: $\frac{p_1V_1}{T_1} = \frac{p_2V_2}{T_2}$ (2 - 3 marks)

Method: identify which quantities stay constant. Constant temperature: $p_1V_1 = p_2V_2$ (Boyle). Constant pressure: $\frac{V_1}{T_1} = \frac{V_2}{T_2}$ (Charles). Everything changing (fixed mass): $\frac{p_1V_1}{T_1} = \frac{p_2V_2}{T_2}$. Units of $p$ and $V$ only need to match on both sides, but $T$ must be in kelvin. This is how bubbles rising, tyres heating up, and balloons expanding are examined.

### 4.12 Explain why a real gas deviates from ideal behaviour (2 - 3 marks)

Method: name the condition (high pressure and/or low temperature) and the two failed assumptions. At high pressure: molecules occupy a significant fraction of the volume (their own volume is no longer negligible) and intermolecular forces become significant. At low temperature: molecules move slowly, forces pull them together, and the gas may condense - the gas laws break down. The ideal gas model is best at low pressure, high temperature.

### 4.13 Explain Brownian motion (2 - 3 marks)

Method: visible particles are bombarded unevenly by invisible molecules of the fluid; the unequal bombardment from all sides makes the particle move randomly (jerky, erratic path); this provides evidence that molecules exist, are in constant random motion, and are much smaller and faster than the visible particle. On heating: molecules move faster, bombardment more vigorous, so the motion of the visible particle becomes more agitated.

### 4.14 Estimate the volume occupied by molecules (2 marks)

Method: volume of one (spherical) molecule $= \frac{4}{3}\pi r^3$; multiply by the number of molecules $N$. Then compare with the container volume to test the "negligible volume" assumption (FM19 Q2: $4 \times 10^{-8}\ \text{m}^3 \ll 6.8 \times 10^{-3}\ \text{m}^3$, so the assumption holds).

---

## 5. Solved Examples

Mark-scheme-style solutions: equation, substitution, answer with units. Examples 1 - 7 are practice questions; Examples 8 - 13 are real Paper 4 questions in chronological order, with mark allocations and answers from the published mark schemes.

### Example 1: Mass of gas in a tyre - pV = nRT then n to mass (practice question, 4 marks)

**Question:** A car tyre contains $0.020\ \text{m}^3$ of air at $3.0 \times 10^5$ Pa and 27 °C. The molar mass of air is $28.8\ \text{g mol}^{-1}$. Calculate the mass of air in the tyre.

**Method:**
1. Convert temperature to kelvin: $T = 27 + 273 = 300\ \text{K}$.
2. Find the number of moles from $pV = nRT$: $n = \frac{pV}{RT}$.
3. Convert moles to mass: $\text{mass} = n \times M_r$.

**Answer:**

$$n = \frac{pV}{RT} = \frac{3.0 \times 10^5 \times 0.020}{8.31 \times 300} = 2.41\ \text{mol}$$

$$\text{mass} = n \times M_r = 2.41 \times 28.8 = 69.4 \approx 69\ \text{g}$$

**What the examiner wants:** $T$ in kelvin (not °C), the rearranged equation $n = \frac{pV}{RT}$ written out (method marks even if the arithmetic slips), and the final answer with units (g).

### Example 2: Boyle's law compression (practice question, 3 marks)

**Question:** A cylinder contains $0.80\ \text{dm}^3$ of nitrogen at 1.2 atm. It is compressed slowly (constant temperature) to 6.0 atm. Calculate the final volume.

**Method:** $T$ constant and fixed mass, so use Boyle's law $p_1V_1 = p_2V_2$. Units of $p$ and $V$ only need to match on each side, so keep atm and $\text{dm}^3$. Rearrange for $V_2$.

**Answer:**

$$V_2 = \frac{p_1V_1}{p_2} = \frac{1.2 \times 0.80}{6.0} = 0.16\ \text{dm}^3$$

The pressure rose by a factor of 5, so the volume fell by a factor of 5.

**What the examiner wants:** recognising that constant temperature means $pV = \text{constant}$ (Boyle's law), and that $p$ and $V$ units only need to be consistent on each side - no conversion to Pa or $\text{m}^3$ needed.

### Example 3: Number of molecules - "show that" style (practice question, 3 marks)

**Question:** A gas occupies $3.1 \times 10^{-3}\ \text{m}^3$ at $8.5 \times 10^5$ Pa and 290 K. Show that the number of molecules is $6.6 \times 10^{23}$.

**Method:** Use $pV = NkT$ rearranged to $N = \frac{pV}{kT}$, and write the substitution line in full with every number. Alternative route: $n = \frac{pV}{RT}$ then $N = nN_A$.

**Answer:**

$$N = \frac{pV}{kT} = \frac{8.5 \times 10^5 \times 3.1 \times 10^{-3}}{1.38 \times 10^{-23} \times 290} = 6.6 \times 10^{23}$$

(Alternative: $n = \frac{pV}{RT} = 1.10$ mol, then $N = nN_A = 1.10 \times 6.02 \times 10^{23} = 6.6 \times 10^{23}$.)

**What the examiner wants:** the full substitution line - writing only the final answer loses marks. Both the $pV = NkT$ route and the $n$ then $N = nN_A$ route are credited.

### Example 4: Mean kinetic energy of a molecule (practice question, 2 - 3 marks)

**Question:** Calculate the mean translational kinetic energy of a molecule of an ideal gas at 27 °C.

**Method:** Convert to kelvin, then apply $\langle E_K \rangle = \frac{3}{2}kT$.

**Answer:**

$$T = 27 + 273 = 300\ \text{K}$$

$$\langle E_K \rangle = \frac{3}{2}kT = \frac{3}{2} \times 1.38 \times 10^{-23} \times 300 = 6.21 \times 10^{-21}\ \text{J}$$

Note the answer is per molecule: a gas with $N$ molecules has total energy $\frac{3}{2}NkT$.

**What the examiner wants:** the kelvin conversion (leaving 27 in the formula scores nothing) and an answer of the right magnitude (about $10^{-21}$ J at room temperature).

### Example 5: r.m.s. speed from temperature - nitrogen (practice question, 3 marks)

**Question:** Nitrogen molecules have mass $4.65 \times 10^{-26}$ kg. Calculate the r.m.s. speed of nitrogen molecules at 300 K.

**Method:** Use $\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}kT$ to get $\langle c^2 \rangle = \frac{3kT}{m}$, then take the square root: $c_{\text{r.m.s.}} = \sqrt{\langle c^2 \rangle}$.

**Answer:**

$$\langle c^2 \rangle = \frac{3kT}{m} = \frac{3 \times 1.38 \times 10^{-23} \times 300}{4.65 \times 10^{-26}} = 2.67 \times 10^5\ \text{m}^2\text{s}^{-2}$$

$$c_{\text{r.m.s.}} = \sqrt{2.67 \times 10^5} = 517\ \text{m s}^{-1}$$

(Shortcut with molar mass: $M = 0.028\ \text{kg mol}^{-1}$, $c_{\text{r.m.s.}} = \sqrt{\frac{3RT}{M}} = \sqrt{\frac{3 \times 8.31 \times 300}{0.028}} = 517\ \text{m s}^{-1}$. Both routes are credited.)

**What the examiner wants:** calculate $\langle c^2 \rangle$ first and then finish with the square root - stopping at $\langle c^2 \rangle$ loses the final mark (Nov 2021 examiner report).

### Example 6: r.m.s. speed from pressure and density (practice question, 3 marks)

**Question:** The density of air at room temperature is $1.29\ \text{kg m}^{-3}$ at a pressure of $1.0 \times 10^5$ Pa. Calculate the r.m.s. speed of air molecules.

**Method:** Use the density form $p = \frac{1}{3}\rho\langle c^2 \rangle$, rearrange to $\langle c^2 \rangle = \frac{3p}{\rho}$, then square root.

**Answer:**

$$\langle c^2 \rangle = \frac{3p}{\rho} = \frac{3 \times 1.0 \times 10^5}{1.29} = 2.33 \times 10^5\ \text{m}^2\text{s}^{-2}$$

$$c_{\text{r.m.s.}} = \sqrt{2.33 \times 10^5} = 4.8 \times 10^2\ \text{m s}^{-1}$$

This is a little above the speed of sound in air (about $330\ \text{m s}^{-1}$), which makes sense.

**What the examiner wants:** picking the density form of the kinetic theory equation and remembering to take the square root at the end.

### Example 7: Internal energy change of a gas (practice question, 3 marks)

**Question:** An ideal gas containing $6.6 \times 10^{23}$ molecules cools from 290 K to 190 K at constant volume. Calculate the change in its internal energy.

**Method:** Use $\Delta U = \frac{3}{2}Nk\Delta T$ with $\Delta T = 190 - 290 = -100\ \text{K}$.

**Answer:**

$$\Delta U = \frac{3}{2} \times 6.6 \times 10^{23} \times 1.38 \times 10^{-23} \times (190 - 290) = -1.4 \times 10^3\ \text{J} = -1400\ \text{J}$$

Negative because the gas lost internal energy (it cooled).

**What the examiner wants:** the negative sign (the gas cooled, so internal energy fell), and recognising that the temperature difference is the same number in kelvin and °C.

### Example 8: Estimating the mean distance between molecules (9702/42/O/N/16 Q2, 8 marks)

**Question:** A gas at 100 °C occupies $2.4 \times 10^3\ \text{cm}^3$ at a pressure of $4.9 \times 10^5$ Pa. (a) Show that the number of molecules of gas is $2.3 \times 10^{23}$. (b) Estimate the mean distance between the molecules.

**Method:**
1. Convert: $T = 100 + 273 = 373\ \text{K}$; $V = 2.4 \times 10^3\ \text{cm}^3 = 2.4 \times 10^3 \times 10^{-6} = 2.4 \times 10^{-3}\ \text{m}^3$.
2. (a) $N = \frac{pV}{kT}$ with the full substitution line.
3. (b) Volume per molecule $= \frac{V}{N}$. Assume each molecule sits at the centre of its own little cube; the mean distance between molecules is the side of that cube, i.e. the cube root of the volume per molecule.

**Answer:**

$$N = \frac{pV}{kT} = \frac{4.9 \times 10^5 \times 2.4 \times 10^{-3}}{1.38 \times 10^{-23} \times 373} = 2.3 \times 10^{23}$$

$$\text{volume per molecule} = \frac{V}{N} = \frac{2.4 \times 10^{-3}}{2.3 \times 10^{23}} = 1.04 \times 10^{-26}\ \text{m}^3$$

$$\text{mean distance} = (1.04 \times 10^{-26})^{1/3} = 2.2 \times 10^{-9}\ \text{m} = 2.2 \times 10^{-7}\ \text{cm}$$

**What the examiner wants:** the mean distance is estimated as the cube root of the volume per molecule (volume per molecule $= \frac{V}{N}$); convert $\text{cm}^3$ to $\text{m}^3$ before substituting; give the answer in the unit requested (cm).

### Example 9: Density form and molecule volume (9702/42/F/M/19 Q2, 10 marks)

**Question:** The pressure $p$ of an ideal gas having density $\rho$ is given by the expression $p = \frac{1}{3}\rho\langle c^2 \rangle$.

(a) State what is meant by:
(i) an ideal gas **[2]**
(ii) the term $\langle c^2 \rangle$. **[1]**

(b) A cylinder contains a fixed mass of a gas at a temperature of 120 °C. The gas has a volume of $6.8 \times 10^{-3}\ \text{m}^3$ at a pressure of $2.4 \times 10^5$ Pa.
(i) Assuming the gas acts as an ideal gas, show that the number of atoms of gas in the cylinder is $3.0 \times 10^{23}$. **[3]**
(ii) Each atom of the gas, assumed to be a sphere, has a radius of $3.2 \times 10^{-11}$ m. Use the answer in (i) to estimate the actual volume occupied by the gas atoms. **[2]**
(iii) One of the assumptions of the kinetic theory of gases is related to the volume of the atoms. State this assumption. Explain whether your answer in (ii) is consistent with this assumption. **[2]**

**Method:**
1. (a)(i) Write "the gas obeys $pV/T = \text{constant}$ (or $pV = nRT$)" and define the symbols $V$ and $T$.
2. (a)(ii) $\langle c^2 \rangle$ is the mean-square speed of the atoms/molecules.
3. (b)(i) $T = 120 + 273 = 393\ \text{K}$; use $pV = nRT$ then $N = nN_A$ (or directly $pV = NkT$), showing the substitution in full.
4. (b)(ii) Volume of one atom $= \frac{4}{3}\pi r^3$; multiply by the number of atoms $N$.
5. (b)(iii) State the assumption, then compare the occupied volume with the container volume.

**Answer:**

$$N = \frac{pV}{kT} = \frac{2.4 \times 10^5 \times 6.8 \times 10^{-3}}{1.38 \times 10^{-23} \times 393} = 3.0 \times 10^{23}$$

$$\text{volume of one atom} = \frac{4}{3}\pi r^3 = \frac{4}{3}\pi(3.2 \times 10^{-11})^3 = 1.37 \times 10^{-31}\ \text{m}^3$$

$$\text{total occupied volume} = 3.0 \times 10^{23} \times \frac{4}{3}\pi(3.2 \times 10^{-11})^3 = 4 \times 10^{-8}\ \text{m}^3$$

Assumption: the volume of the atoms is negligible compared with the volume of the container. $4 \times 10^{-8}\ \text{m}^3 \ll 6.8 \times 10^{-3}\ \text{m}^3$, so yes, the result is consistent with the assumption.

**What the examiner wants:** two separate marks for the ideal gas definition - the law ($pV/T = \text{constant}$ or $pV = nRT$) plus the symbols defined; the full substitution line for the "show that"; for the volume, $\frac{4}{3}\pi r^3$ per atom times $N$; and a comparison of magnitudes for the assumption check.

### Example 10: Explaining $p = \frac{1}{3}\rho\langle c^2 \rangle$ and the mass of one molecule (9702/42/M/J/20 Q2, 8 marks)

**Question:** (a) The pressure of an ideal gas is given by $pV = \frac{1}{3}Nm\langle c^2 \rangle$. Explain how each of the terms $\rho$, $\frac{1}{3}$ and $\langle c^2 \rangle$ arises in the equivalent expression $p = \frac{1}{3}\rho\langle c^2 \rangle$. (b) A sample of gas has mass 20.7 g. The number of molecules in the sample, found using $pV = NkT$, is $4.5 \times 10^{23}$. Calculate the mass of one molecule.

**Method:**
1. (a) $\rho = \frac{Nm}{V}$: the density of the gas, i.e. the total mass of all the molecules divided by the volume they occupy.
2. $\frac{1}{3}$: the molecules move randomly in three dimensions, so on average only one third of the molecular motion is along any one axis - only the component of velocity perpendicular to a wall contributes to the pressure on that wall.
3. $\langle c^2 \rangle$: the molecules have different speeds, so we use the mean of the squares of all their speeds (the mean-square speed).
4. (b) Mass of one molecule $= \frac{\text{total mass}}{N}$.

**Answer:**

$$\text{mass of one molecule} = \frac{20.7\ \text{g}}{4.5 \times 10^{23}} = 4.6 \times 10^{-23}\ \text{g}$$

**What the examiner wants:** each term explained separately - $\rho$ is the density ($Nm/V$); $\frac{1}{3}$ comes from random motion in three dimensions (only one third of the motion in any one direction); $\langle c^2 \rangle$ is the average of the squares of the speeds because the speeds differ. The molecule mass is simply the sample mass divided by $N$.

### Example 11: The full kinetic theory package (9702/42/O/N/21 Q3, 11 marks)

**Question (numbers and wording as printed):**

(a)(i) One assumption of the kinetic theory is that all collisions involving molecules of the gas are elastic. State what is meant by an elastic collision. **[1]**

(a)(ii) State two other assumptions of the kinetic theory of gases. **[2]**

(b) A molecule of mass $m$ is in a cubic box of side $L$, moving with velocity $u$ towards one face, colliding elastically with that face and the opposite face alternately. Deduce expressions, in terms of $m$, $u$ and $L$, for:
(i) the magnitude of the change in momentum of the molecule on colliding with a face **[1]**
(ii) the time between consecutive collisions of the molecule with the same face **[1]**
(iii) the average force exerted by the molecule on that face **[1]**
(iv) the pressure on the face if that force acts over the whole area of the face. **[1]**

(c) When the model is extended to three dimensions and $N$ molecules with mean-square speed $\langle c^2 \rangle$, it can be shown that $pV = \frac{1}{3}Nm\langle c^2 \rangle$. Use this expression with the equation of state to show that the average translational kinetic energy of a molecule is $E_K = \frac{3}{2}kT$. **[2]**

(d) The mass of a hydrogen molecule is $3.34 \times 10^{-27}$ kg. Use the expression for $E_K$ to determine the r.m.s. speed of a hydrogen molecule at 25 °C. **[2]**

**Method:**
1. (a)(i) An elastic collision is one with no loss of kinetic energy.
2. (a)(ii) Any two of: molecules have negligible volume (compared with the gas/container); no forces between molecules (except during collisions); molecules are in random motion; collisions are instantaneous.
3. (b)(i) Velocity reverses from $+u$ to $-u$: change in momentum $= 2mu$.
4. (b)(ii) Distance travelled between hits on the same face is $2L$ at speed $u$: time $= \frac{2L}{u}$.
5. (b)(iii) Force = rate of change of momentum: $F = \frac{2mu}{2L/u} = \frac{mu^2}{L}$.
6. (b)(iv) Pressure = force/area: $p = \frac{mu^2/L}{L^2} = \frac{mu^2}{L^3}$.
7. (c) Start from $pV = NkT$; equate with $pV = \frac{1}{3}Nm\langle c^2 \rangle$; cancel $N$; rearrange to $\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}kT$ and identify $\frac{1}{2}m\langle c^2 \rangle$ as $E_K$.
8. (d) Substitute with $T = 25 + 273 = 298\ \text{K}$; find $\langle c^2 \rangle$; take the square root for the r.m.s. speed.

**Answer:**

- (a)(i) no loss of kinetic energy
- (a)(ii) any two of: negligible molecular volume; no forces except during collisions; random motion; instantaneous collisions
- (b)(i) $2mu$
- (b)(ii) $\frac{2L}{u}$
- (b)(iii) $F = \frac{2mu}{2L/u} = \frac{mu^2}{L}$
- (b)(iv) $p = \frac{mu^2/L}{L^2} = \frac{mu^2}{L^3}$
- (c) $NkT = \frac{1}{3}Nm\langle c^2 \rangle$ leading to $\frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}kT$ and $\frac{1}{2}m\langle c^2 \rangle = E_K$
- (d) $\frac{1}{2} \times 3.34 \times 10^{-27} \times \langle c^2 \rangle = \frac{3}{2} \times 1.38 \times 10^{-23} \times 298$; r.m.s. speed $= 1.9 \times 10^3\ \text{m s}^{-1}$

**What the examiner wants (Nov 2021, Paper 42 report):** (a)(i) "kinetic energy is conserved" - momentum conservation or "energy is conserved" in general did not score. (a)(ii) the theory deals with the particles that make up the gas, not the gas itself. (b) the factors of 2 in (i) and (ii), and only the letters the question defines ($m$, $u$, $L$) - inventing symbols loses credit. (c) starting from $pV = NkT$ is easier; if you start from $pV = nRT$ you must state $N = nN_A$ and $R = kN_A$. (d) many calculated $\langle c^2 \rangle$ but did not square-root it; some left $T$ in °C and got no credit.

### Example 12: Equation of state plus internal energy (9702/42/M/J/21 Q2, 9 marks)

**Question (numbers as printed):**

An ideal gas has volume $3.1 \times 10^{-3}\ \text{m}^3$ at pressure $8.5 \times 10^5$ Pa and temperature 290 K. It suddenly expands to $6.3 \times 10^{-3}\ \text{m}^3$; no thermal energy is transferred; final pressure $2.7 \times 10^5$ Pa at temperature $T_F$.

(a) Show that the number of gas molecules is $6.6 \times 10^{23}$. **[3]**

(b)(i) Show that the final temperature $T_F$ of the gas is 190 K. **[1]**

(b)(ii) The average translational kinetic energy of a molecule is $E_K = \frac{3}{2}kT$. Calculate the increase in internal energy $\Delta U$ of the gas. **[3]**

(c) Use the first law of thermodynamics to explain why the external work done on the gas during the expansion equals the increase in internal energy in (b)(ii). **[2]**

**Method:**
1. (a) $N = \frac{pV}{kT}$ (or $n = \frac{pV}{RT}$ then $N = nN_A$), substitution line in full.
2. (b)(i) Fixed mass, all three quantities change: $\frac{p_1V_1}{T_1} = \frac{p_2V_2}{T_2}$, rearrange for $T_2$.
3. (b)(ii) $\Delta U = \frac{3}{2}Nk\Delta T$ with $\Delta T = T_F - 290$.
4. (c) First law $\Delta U = q + W$; no thermal energy transferred means $q = 0$, so $\Delta U = W$.

**Answer:**

- (a) $N = \frac{3.1 \times 10^{-3} \times 8.5 \times 10^5}{1.38 \times 10^{-23} \times 290} = 6.6 \times 10^{23}$
- (b)(i) $\frac{3.1 \times 10^{-3} \times 8.5 \times 10^5}{290} = \frac{6.3 \times 10^{-3} \times 2.7 \times 10^5}{T}$; so $T = 190\ \text{K}$
- (b)(ii) $\Delta U = \frac{3}{2} \times 1.38 \times 10^{-23} \times (190 - 290) \times 6.6 \times 10^{23} = -1400\ \text{J}$ (a decrease, since the gas cooled)
- (c) $\Delta U = q + W$; $q = 0$ (no thermal energy transferred) so $\Delta U = W$

**What the examiner wants (May/June 2021 report):** the "show that" parts require the substitution line written out; candidates who quoted the formula with $T$ (or $N$) as the subject scored the method marks more readily.

### Example 13: Potential energy zero and the internal energy-volume graph (9702/41/M/J/24 Q3, 12 marks)

**Question (verified points):** This 12-mark question on an ideal gas asked candidates to explain why the potential energy of the molecules of an ideal gas is zero, to show that the internal energy $U$ of a fixed mass of ideal gas at constant pressure is related to its volume by $U = \frac{3}{2}pV$, and to sketch a graph of internal energy $U$ against volume $V$ at constant pressure.

**Method:**
1. Potential energy: an ideal gas has no intermolecular forces. With no forces between molecules, no work is done in changing their separation, so the molecules have zero potential energy - all the internal energy is kinetic.
2. $U = \frac{3}{2}NkT$ (all kinetic, since the potential energy is zero). From the equation of state $pV = NkT$, substitute: $U = \frac{3}{2}NkT = \frac{3}{2}pV$.
3. Graph: at constant pressure, $U = \frac{3}{2}pV$ means $U \propto V$ - a straight line through the origin with positive gradient $\frac{3}{2}p$.

**Answer:** (a) the potential energy of the molecules is zero because there are no intermolecular forces; (b) $U = \frac{3}{2}NkT = \frac{3}{2}pV$; (c) the $U$ against $V$ graph is a straight line through the origin with positive gradient.

**What the examiner wants:** the key statement "no intermolecular forces, so potential energy is zero" - this is what makes all the internal energy kinetic; for the graph, a straight line through the origin with positive gradient, because at constant pressure $U = \frac{3}{2}pV$ means $U$ is proportional to $V$.

### Question patterns to expect (from examiner reports and exam-practice sources)

- **June 2022, Paper 41, Q3** (verified via the examiner report): an ideal gas question asked candidates to state what is meant by an ideal gas, calculate the amount of gas from $pV = nRT$, and complete a first-law energy table including a constant-temperature change. The report notes: stating "obeys $pV = nRT$" is only equivalent to "$pV \propto T$" when $n$ and $R$ are stated to be constant; candidates must define all symbols; all steps must be clear in "show that" questions; and for a change at constant temperature the increase in internal energy is zero.
- **May/June 2024, Paper 41** (verified Question 3 solved in Example 13): the 12-mark ideal gas question tested the zero potential energy of ideal gas molecules and the $U$ against $V$ graph at constant pressure. Related exam-practice styles from this session include the mean translational kinetic energy per molecule at a given temperature (5-mark style question) and the r.m.s. speed of $\text{N}_2$ molecules given the molar mass (6-mark style question).
- **Generic recurring types** (safe to expect): "state what is meant by an ideal gas" [2]; "state two assumptions" [2]; "explain, in terms of molecules, why the pressure increases when (i) temperature rises, (ii) more gas is added" [2-3]; "calculate the number of molecules in a container" [2-3]; "calculate the r.m.s. speed" [2-4]; "compare the mean kinetic energies / speeds of two different gases at the same temperature" [2]; "explain why a real gas deviates from ideal behaviour at high pressure / low temperature" [2-3].

---

## 6. Cheat Sheet (quick revision block)

**All formulas in one place:**

$$pV = nRT \qquad pV = NkT \qquad k = \frac{R}{N_A} \qquad N = nN_A \qquad n = \frac{m}{M_r}$$

$$p_1V_1 = p_2V_2 \quad (\text{const } T) \qquad \frac{V_1}{T_1} = \frac{V_2}{T_2} \quad (\text{const } p) \qquad \frac{p_1V_1}{T_1} = \frac{p_2V_2}{T_2} \quad (\text{fixed mass})$$

$$pV = \frac{1}{3}Nm\langle c^2 \rangle = \frac{1}{3}M_{\text{gas}}\langle c^2 \rangle \qquad p = \frac{1}{3}\rho\langle c^2 \rangle \qquad c_{\text{r.m.s.}} = \sqrt{\langle c^2 \rangle}$$

$$\langle E_K \rangle = \frac{1}{2}m\langle c^2 \rangle = \frac{3}{2}kT \qquad c_{\text{r.m.s.}} = \sqrt{\frac{3kT}{m}} = \sqrt{\frac{3RT}{M}} = \sqrt{\frac{3p}{\rho}}$$

$$U = \frac{3}{2}NkT = \frac{3}{2}nRT \qquad \Delta U = \frac{3}{2}Nk\Delta T \qquad T/\text{K} = \theta/^\circ\text{C} + 273.15$$

**Key definitions:**

- Ideal gas: obeys $pV = nRT$ (or $pV \propto T$) at all pressures and temperatures; kinetic model: no intermolecular forces, negligible molecular volume.
- Mole: amount of substance containing Avogadro's number of particles.
- Mean-square speed: average of the squares of molecular speeds.
- r.m.s. speed: square root of the mean-square speed.
- Mean translational kinetic energy of a molecule: $\frac{3}{2}kT$; proportional to $T$, independent of gas type.
- Brownian motion: erratic motion of visible particles caused by uneven molecular bombardment; evidence for random molecular motion.
- Boltzmann constant: gas constant per molecule, $k = R/N_A$.

**The five kinetic theory assumptions (short form):** many molecules in random motion; negligible molecular volume; no forces except during collisions; perfectly elastic collisions; negligible collision time.

**Common traps (check these before you submit):**

- Temperature: always kelvin. $25\ ^\circ\text{C} = 298\ \text{K}$, not 25.
- Volume: must be $\text{m}^3$. $1\ \text{dm}^3 = 10^{-3}\ \text{m}^3$; $1\ \text{cm}^3 = 10^{-6}\ \text{m}^3$; 1 litre $= 10^{-3}\ \text{m}^3$.
- Molar mass: divide by 1000 to get $\text{kg mol}^{-1}$ before using $c_{\text{r.m.s.}} = \sqrt{3RT/M}$.
- $n$ (moles) vs $N$ (number of molecules): they differ by a factor of $N_A$ ($6 \times 10^{23}$). Use $pV = nRT$ with $R$; use $pV = NkT$ with $k$.
- Molecules vs atoms: $\text{O}_2$ gas, 1 mol of molecules = 2 mol of atoms.
- r.m.s. speed: square first, average, then square root. Do not just average the speeds.
- Finish the job: if you calculated $\langle c^2 \rangle$, take the square root for $c_{\text{r.m.s.}}$.
- $\Delta T$ is the same number in K and °C, but the absolute temperature $T$ is not.
- A constant-temperature change of an ideal gas means $\Delta U = 0$.

---

## 7. Common Exam Mistakes (from examiner reports)

These are documented, repeated mistakes from the 9702 examiner reports. Fixing them is worth several marks.

1. **Celsius instead of kelvin** (Nov 2021, Paper 42, Q3(d); June 2022, Paper 41, Q3(a)(ii)): leaving the temperature in °C in any $pV = nRT$ or $\frac{3}{2}kT$ calculation scored nothing. Convert first: $T = \theta + 273.15$.

2. **Elastic collision defined wrongly** (Nov 2021, Paper 42): "an elastic collision is one in which kinetic energy is conserved" is the answer. Momentum conservation, "energy is conserved" in general, or elastic deformation of particles did not score.

3. **Kinetic theory assumptions written about the gas, not its molecules** (Nov 2021, Paper 42): the theory deals with the particles that make up the gas. Write "molecules have negligible volume", not "the gas has negligible volume".

4. **Omitting factors of 2 in the derivation** (Nov 2021, Paper 42): the momentum change is $2mu$ (not $mu$) and the time between collisions with the same face is $\frac{2L}{u}$ (not $\frac{L}{u}$). Both are 1-mark answers, so this is expensive.

5. **Inventing symbols** (Nov 2021, Paper 42): in derivation questions, use only the letters the question defines ($m$, $u$, $L$). Making up new symbols loses credit.

6. **Forgetting the final square root** (Nov 2021, Paper 42): candidates calculated $\langle c^2 \rangle$ and stopped. The r.m.s. speed is $\sqrt{\langle c^2 \rangle}$.

7. **Confusing $n$ and $N$** (Nov 2021, Paper 42): treated the number of moles and the number of molecules as the same quantity. They differ by $N_A$. Similarly, "atom" and "molecule" are confused in written answers (Paper 42 key message).

8. **Ideal gas definition without constants** (June 2022, Paper 41): "it obeys $pV = nRT$" is only acceptable if you add "at all pressures and temperatures, with $n$ and $R$ constant", and define the symbols.

9. **Not showing "show that" working** (June 2022, Paper 41; May/June 2021, Paper 42): in "show that $N = 6.6 \times 10^{23}$" type questions, the full substitution line is required for the marks. Write the equation, substitute every value, then state the result.

10. **$\Delta U = 0$ at constant temperature** (June 2022, Paper 41): many candidates thought an ideal gas expanding at constant temperature still gained internal energy. No temperature change means no internal energy change.

11. **Writing more points than asked** (Nov 2021, Paper 42 key message): if a question asks for "two assumptions", examiners assess only up to the required number of points. Incorrect extra points written first can bury your correct answers. Give exactly what is asked.

12. **Significant figures and premature rounding** (Nov 2021, Paper 42 key message): match the precision of the data, carry at least one extra significant figure in intermediate steps, and show working so partial credit can be awarded.

---

*Sources: CAIE 9702 syllabus (Topic 15); Cambridge International AS & A Level Physics coursebook, Chapter 22; CAIE 9702 examiner reports (Nov 2021, June 2022); CAIE 9702 question papers and mark schemes (O/N 2016 Q2, F/M 2019 Q2, M/J 2020 Q2, O/N 2021 Q3, M/J 2021 Q2, M/J 2024 Q3); data and formulae sheet 9702/42/O/N/21.*
