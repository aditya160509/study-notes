# Chapter 12: Practical Circuits - CAIE A Level Physics (9702) Study Notes

Exam-focused revision notes for Cambridge International AS & A Level Physics 9702, covering the practical-circuits content of Chapter 12: e.m.f. and internal resistance, terminal p.d., power transfer, potential dividers, the potentiometer, I–V characteristics and resistivity. This is core Paper 2 and Paper 4 material, and it also underpins the practical work examined in Paper 3 and Paper 5. Definitions are worded to match mark schemes, and every section ends with worked examples using the formula just introduced. Assume $g = 9.81~\text{m s}^{-2}$ where a weight is involved, and always convert mA → A and cm → m before substituting.

## 1. Theory

### 1.1 E.m.f. and potential difference — the distinction

**Electromotive force (e.m.f.)** is the energy transferred from chemical (or other) form to electrical form **per unit charge** driven around a complete circuit by a source. In symbols:

$$E = \frac{W}{Q}$$

- $E$ is the e.m.f., in volts (V).
- $W$ is the energy transferred to the charge, in joules (J).
- $Q$ is the charge passing, in coulombs (C).

**Potential difference (p.d.)** is the energy transferred **from** electrical form to other forms per unit charge between two points in a circuit. Both are measured in volts, so $1~\text{V} = 1~\text{J C}^{-1}$. The difference is one of direction of energy transfer: a source **gives** energy to the charge (e.m.f.); a component **removes** energy from the charge (p.d.).

The e.m.f. of a cell is a property of the cell itself (its chemistry). The p.d. between its terminals is a property of the circuit it is connected to. That is why the same cell can show $1.50~\text{V}$ on a high-resistance voltmeter and only $1.20~\text{V}$ when supplying a lamp.

> **Exam wording:** e.m.f. = "energy transferred from chemical to electrical per unit charge" (or "work done per unit charge in driving charge round the complete circuit"). P.d. = "energy transferred from electrical to other forms per unit charge between two points." Do not define e.m.f. as "the voltage across a battery" — that is the terminal p.d., which is smaller.

A **high-resistance voltmeter** draws negligible current, so there is negligible lost volts and its reading is a good approximation to the e.m.f. A real voltmeter always draws some current, so it always reads slightly less than the e.m.f.

**Worked example:** A battery transfers $36~\text{J}$ of chemical energy to $3.0~\text{C}$ of charge. Calculate its e.m.f.

1. Use $E = \frac{W}{Q}$: $E = \frac{36}{3.0} = 12~\text{V}$.

**Answer:** $E = 12~\text{V}$.

### 1.2 Internal resistance, lost volts and terminal p.d.

Every source has some **internal resistance** $r$, due to the chemicals inside a cell or the wires and components inside a power supply. The charges pass through this resistance as well as through the external circuit, so some energy is dissipated inside the source. We model the source as an ideal cell of e.m.f. $E$ in series with a resistor $r$.

The current in a simple circuit is therefore:

$$I = \frac{E}{R + r}$$

- $R$ is the external resistance, in ohms ($\Omega$).
- $r$ is the internal resistance, in ohms ($\Omega$).

The **terminal potential difference** $V$ is the p.d. across the external resistance:

$$V = IR = E - Ir$$

The quantity $Ir$ is called the **lost volts**:

$$\text{terminal p.d.} = \text{e.m.f.} - \text{lost volts}$$

Key consequences:

- $V < E$ whenever current flows.
- $V \to E$ when $I \to 0$ (open circuit, or a very high-resistance voltmeter).
- $V$ falls as the current rises, because more energy is dissipated in $r$.
- If the terminals are short-circuited ($R \approx 0$), the current is limited only by $r$: $I_{\max} = \frac{E}{r}$.

**Worked example:** A cell of e.m.f. $1.50~\text{V}$ and internal resistance $0.50~\Omega$ is connected to a $2.50~\Omega$ resistor. Calculate the current, the terminal p.d. and the lost volts.

1. Total resistance: $R + r = 2.50 + 0.50 = 3.00~\Omega$.
2. $I = \frac{E}{R+r} = \frac{1.50}{3.00} = 0.50~\text{A}$.
3. $V = IR = 0.50 \times 2.50 = 1.25~\text{V}$.
4. Lost volts $= Ir = 0.50 \times 0.50 = 0.25~\text{V}$; check $E - Ir = 1.50 - 0.25 = 1.25~\text{V}$.

**Answer:** $I = 0.50~\text{A}$; $V = 1.25~\text{V}$; lost volts $= 0.25~\text{V}$.

**Worked example:** A battery of e.m.f. $6.0~\text{V}$ drives a current of $0.40~\text{A}$ through a $13.5~\Omega$ resistor. Calculate its internal resistance.

1. $E = I(R+r)$: $6.0 = 0.40(13.5 + r)$.
2. $13.5 + r = 15.0$, so $r = 1.5~\Omega$.
3. Check lost volts: $Ir = 0.40 \times 1.5 = 0.60~\text{V}$; terminal p.d. $= 5.40~\text{V} = 0.40 \times 13.5$.

**Answer:** $r = 1.5~\Omega$.

### 1.3 Determining e.m.f. and internal resistance from a $V$–$I$ graph

Rearranging $V = E - Ir$ gives a straight line:

$$V = (-r)I + E$$

Comparing with $y = mx + c$:

- **$y$-intercept** $= E$ (the e.m.f.).
- **gradient** $= -r$ (so $r$ is the magnitude of the gradient).
- The intercept on the $I$-axis (where $V = 0$) is the short-circuit current $I_{\max} = \frac{E}{r}$.

Experimentally, connect the cell to a variable resistor, an ammeter and a voltmeter across the cell terminals. Vary $R$, record $I$ and $V$, and plot $V$ against $I$. The line should be straight with a negative gradient.

**Why the line has a negative gradient:** a larger current means a larger $Ir$ lost volts, so the terminal p.d. is smaller.

**Worked example:** The following results are obtained for a cell.

| $V/\text{V}$ | 1.43 | 1.33 | 1.18 | 1.10 | 0.98 |
|---|---|---|---|---|---|
| $I/\text{A}$ | 0.10 | 0.30 | 0.60 | 0.75 | 1.00 |

Calculate $E$ and $r$.

1. Gradient $= \frac{0.98 - 1.43}{1.00 - 0.10} = \frac{-0.45}{0.90} = -0.50~\Omega$, so $r = 0.50~\Omega$.
2. Use $E = V + Ir$ with any point: $E = 1.43 + 0.10 \times 0.50 = 1.48~\text{V}$.
3. Check with the last point: $0.98 + 1.00 \times 0.50 = 1.48~\text{V}$.

**Answer:** $E = 1.48~\text{V}$, $r = 0.50~\Omega$.

### 1.4 Power output and maximum power transfer

The power delivered to the external resistor is

$$P = I^2R = \left(\frac{E}{R+r}\right)^2 R$$

For a fixed $E$ and $r$, this has a maximum when the external resistance equals the internal resistance:

$$R = r \qquad \Rightarrow \qquad P_{\max} = \frac{E^2}{4r}$$

**Derivation (calculus):** write $P = \frac{E^2R}{(R+r)^2}$ and differentiate with respect to $R$:

$$\frac{dP}{dR} = E^2\frac{(R+r)^2 - 2R(R+r)}{(R+r)^4} = E^2\frac{r-R}{(R+r)^3}$$

This is zero when $R = r$. Substituting back gives $P_{\max} = \frac{E^2}{(2r)^2}r = \frac{E^2}{4r}$.

At maximum power transfer, exactly **half** the total power is dissipated in the source ($I^2r = I^2R$), so the **efficiency is 50%**. Power supplies are not usually designed to run at maximum power transfer for this reason — a car battery has very low internal resistance so that most power reaches the starter motor.

**Worked example:** A supply of e.m.f. $12~\text{V}$ and internal resistance $0.50~\Omega$ is connected to a variable resistor $R$. Calculate the power in $R$ when (a) $R = 0.50~\Omega$, (b) $R = 0.25~\Omega$, (c) $R = 1.0~\Omega$.

1. (a) $I = \frac{12}{0.50+0.50} = 12~\text{A}$; $P = I^2R = 144 \times 0.50 = 72~\text{W}$.
2. (b) $I = \frac{12}{0.75} = 16~\text{A}$; $P = 256 \times 0.25 = 64~\text{W}$.
3. (c) $I = \frac{12}{1.5} = 8.0~\text{A}$; $P = 64 \times 1.0 = 64~\text{W}$.
4. Check with $P_{\max} = \frac{E^2}{4r} = \frac{144}{2.0} = 72~\text{W}$.

**Answer:** (a) $72~\text{W}$ (maximum); (b) $64~\text{W}$; (c) $64~\text{W}$ — both off-maximum values are lower, confirming the $R = r$ condition.

### 1.5 Cells in series and in opposition (superposition of e.m.f.s)

**Cells in series, same direction:** the e.m.f.s add and the internal resistances add, because the same current passes through each cell:

$$E_{\text{total}} = E_1 + E_2 + \dots, \qquad r_{\text{total}} = r_1 + r_2 + \dots$$

**Cells in opposition:** the net e.m.f. is the difference, and the larger e.m.f. drives current in its own direction:

$$E_{\text{total}} = E_1 - E_2 \quad (\text{if } E_1 > E_2)$$

The cell with the smaller e.m.f. is being **charged**: current is forced into its positive terminal, so its terminal p.d. is $V = E_2 + Ir_2$ (larger than its e.m.f.). The cell driving the current has $V = E_1 - Ir_1$.

**Superposition of e.m.f.s** simply means that in a series loop the algebraic sum of the e.m.f.s drives the current. Assign one direction as positive; e.m.f.s in that direction are $+$, those opposing are $-$.

**Worked example:** Four identical cells, each of e.m.f. $1.5~\text{V}$ and internal resistance $0.10~\Omega$, are connected in series to a $2.0~\Omega$ lamp. Calculate the current.

1. $E_{\text{total}} = 4 \times 1.5 = 6.0~\text{V}$.
2. $r_{\text{total}} = 4 \times 0.10 = 0.40~\Omega$.
3. $I = \frac{6.0}{2.0 + 0.40} = 2.5~\text{A}$.

**Answer:** $I = 2.5~\text{A}$.

**Worked example:** A $6.0~\text{V}$ cell of internal resistance $1.0~\Omega$ is connected in series opposition with a $4.5~\text{V}$ cell of internal resistance $0.50~\Omega$, and a $1.5~\Omega$ resistor completes the circuit. Calculate the current and the terminal p.d. of each cell.

1. Net e.m.f. $= 6.0 - 4.5 = 1.5~\text{V}$.
2. Total resistance $= 1.0 + 0.50 + 1.5 = 3.0~\Omega$.
3. $I = \frac{1.5}{3.0} = 0.50~\text{A}$.
4. Driving cell: $V = 6.0 - 0.50 \times 1.0 = 5.5~\text{V}$.
5. Charged cell: $V = 4.5 + 0.50 \times 0.50 = 4.75~\text{V}$ (current forced into its positive terminal).

**Answer:** $I = 0.50~\text{A}$; terminal p.d.s are $5.5~\text{V}$ and $4.75~\text{V}$.

### 1.6 Potential dividers

A **potential divider** is two or more resistors in series across a supply. The supply p.d. is shared between them in direct proportion to their resistances, because the current through each is the same:

$$V_{\text{out}} = \frac{R_2}{R_1 + R_2}V_{\text{in}}$$

- $V_{\text{in}}$ is the p.d. across the whole divider, in volts.
- $V_{\text{out}}$ is the p.d. across $R_2$, in volts.
- $R_1$ and $R_2$ are the resistances, in ohms.

The ratio $\frac{R_2}{R_1+R_2}$ is the **fraction of the supply** taken by $R_2$. A variable resistor used this way is a simple **dimmer**: with the slider at one end, $V_{\text{out}} = 0$; at the other end, $V_{\text{out}} = V_{\text{in}}$.

**Loading effect:** if a load of resistance $R_L$ is connected across $R_2$, it is in parallel with $R_2$, so the effective resistance of that section falls. $V_{\text{out}}$ therefore falls below the unloaded value. The divider is only accurate when $R_L \gg R_2$.

**Worked example:** A $12~\text{V}$ supply is connected across a $6.0~\text{k}\Omega$ resistor in series with a $3.0~\text{k}\Omega$ resistor. Calculate the p.d. across the $3.0~\text{k}\Omega$ resistor.

1. $V_{\text{out}} = \frac{3.0}{6.0+3.0} \times 12 = \frac{1}{3} \times 12$.
2. $V_{\text{out}} = 4.0~\text{V}$.

**Answer:** $V_{\text{out}} = 4.0~\text{V}$.

### 1.7 Potential dividers with a thermistor and an LDR

A **thermistor** (NTC type) has a resistance that **falls as temperature rises**. An **LDR** has a resistance that **falls as light intensity rises**. Either can replace one resistor in a divider to make a sensing circuit.

- Output taken **across the sensor**: as the sensed quantity rises, the sensor resistance falls, so it takes a smaller share of the supply — $V_{\text{out}}$ **falls**.
- Output taken **across the fixed resistor**: as the sensor resistance falls, the fixed resistor takes a larger share — $V_{\text{out}}$ **rises**.

This choice of where to take the output is the single most examined point in sensing circuits.

**Worked example:** An NTC thermistor is in series with a $5.0~\text{k}\Omega$ fixed resistor across a $10~\text{V}$ supply. The output is taken across the thermistor. At $20~^\circ\text{C}$ the thermistor resistance is $20~\text{k}\Omega$; at $60~^\circ\text{C}$ it is $1.0~\text{k}\Omega$. Calculate $V_{\text{out}}$ at each temperature.

1. At $20~^\circ\text{C}$: $V_{\text{out}} = \frac{20}{20+5.0} \times 10 = 8.0~\text{V}$.
2. At $60~^\circ\text{C}$: $V_{\text{out}} = \frac{1.0}{1.0+5.0} \times 10 = 1.67~\text{V}$.

**Answer:** $V_{\text{out}}$ falls from $8.0~\text{V}$ to $1.7~\text{V}$ as the temperature rises.

**Worked example:** An LDR ($1.0~\text{k}\Omega$ in bright light, $1.0~\text{M}\Omega$ in darkness) is in series with a $10~\text{k}\Omega$ resistor across a $9.0~\text{V}$ supply, with the output across the fixed resistor. Calculate $V_{\text{out}}$ in bright light and in darkness.

1. Bright: $V_{\text{out}} = \frac{10}{1.0+10} \times 9.0 = 8.18~\text{V}$.
2. Dark: $V_{\text{out}} = \frac{10}{1000+10} \times 9.0 = 0.089~\text{V}$.

**Answer:** $V_{\text{out}} \approx 8.2~\text{V}$ in bright light, falling to $0.089~\text{V}$ in darkness.

### 1.8 The potentiometer

A **potentiometer** compares potential differences without drawing current from the cell being tested. A uniform resistance wire $AB$ is connected across a **driver cell** of e.m.f. $E_0$. If the wire has length $L$, the p.d. per unit length is $\frac{V_{AB}}{L}$, and along a balance length $l$ the p.d. is proportional to $l$.

The unknown cell $E_X$ is connected with its positive terminal to $A$, through a sensitive galvanometer to a **jockey** on the wire. At the balance point $Y$ the galvanometer reads **zero**: no current flows through the unknown cell, so its terminal p.d. equals its e.m.f. (no lost volts). Then:

$$E_X = \frac{l_X}{L}V_{AB}$$

For two cells compared in turn on the same potentiometer:

$$\frac{E_X}{E_Y} = \frac{l_X}{l_Y}$$

Because the driver cell's terminal p.d. is less than $E_0$ when it supplies current, comparing against a **standard cell** of accurately known e.m.f. is more accurate than using $E_0$ directly:

$$E_X = E_{\text{standard}}\frac{l_X}{l_{\text{standard}}}$$

**Practical points:** tap the jockey briefly; never slide it, because scraping makes the wire non-uniform. The unknown e.m.f. must be less than the driver p.d. If the balance point is not found, the unknown e.m.f. is too large (or the connections are reversed).

**Worked example:** A driver cell of e.m.f. $2.0~\text{V}$ is connected across a uniform $100~\text{cm}$ wire of negligible resistance. An unknown cell balances at $63.0~\text{cm}$. Calculate its e.m.f.

1. p.d. per cm $= \frac{2.0}{100} = 0.020~\text{V cm}^{-1}$.
2. $E_X = 0.020 \times 63.0 = 1.26~\text{V}$.

**Answer:** $E_X = 1.26~\text{V}$.

**Worked example:** A standard cell of e.m.f. $1.018~\text{V}$ balances at $50.9~\text{cm}$ on a potentiometer wire. Under identical conditions an unknown cell balances at $63.0~\text{cm}$. Calculate the unknown e.m.f.

1. $\frac{E_X}{1.018} = \frac{63.0}{50.9}$.
2. $E_X = 1.018 \times 1.238 = 1.26~\text{V}$.

**Answer:** $E_X = 1.26~\text{V}$.

### 1.9 I–V characteristics

An **I–V characteristic** is a graph of current against potential difference for a component. The resistance at any point is $R = \frac{V}{I}$; on the graph this is the reciprocal of the gradient of the line from the origin to the point.

| Component | I–V characteristic | Resistance behaviour |
|---|---|---|
| Ohmic resistor (constant temperature) | Straight line through origin | Constant: $R = \frac{V}{I}$ is the same at every point |
| Filament lamp | Curve through origin, gradient decreasing at high $V$ | Increases as current (and temperature) rises |
| Semiconductor diode | Almost zero current in reverse; sharp rise above ~0.6 V forward | Very high in reverse; falls sharply above the threshold |
| Thermistor (NTC) | Curve; current rises faster than $V$ at high $V$ | Falls as temperature rises |

**Filament lamp:** as the current increases, the filament temperature rises, the metal ions vibrate more and scatter conduction electrons more strongly, so resistance increases. The characteristic therefore curves towards the voltage axis. The lamp is **non-ohmic**.

**Diode:** conducts only when the p.d. is in the forward direction and above about $0.6~\text{V}$ (silicon). In reverse it has a very high resistance; exceeding the reverse breakdown voltage destroys it (unless it is a Zener diode, Chapter 25).

**Worked example:** A filament lamp carries $0.20~\text{A}$ at $12~\text{V}$ and $0.50~\text{A}$ at $60~\text{V}$. Calculate its resistance at each point and comment.

1. At $12~\text{V}$: $R = \frac{12}{0.20} = 60~\Omega$.
2. At $60~\text{V}$: $R = \frac{60}{0.50} = 120~\Omega$.
3. The resistance has doubled because the filament is much hotter at the higher current.

**Answer:** $60~\Omega$ and $120~\Omega$; the lamp is non-ohmic because its resistance rises with temperature.

### 1.10 Resistivity and the temperature coefficient of resistance

The resistance of a uniform conductor is

$$R = \frac{\rho L}{A}$$

- $\rho$ is the resistivity, in ohm metres ($\Omega\,\text{m}$).
- $L$ is the length, in metres.
- $A$ is the cross-sectional area, in square metres.

For a circular wire of diameter $d$, $A = \pi\left(\frac{d}{2}\right)^2 = \frac{\pi d^2}{4}$. A common error is to use the diameter as the radius.

**Temperature dependence of a metal:** resistance increases approximately linearly with temperature:

$$R = R_0(1 + \alpha \Delta\theta)$$

- $R_0$ is the resistance at the reference temperature (usually $0~^\circ\text{C}$).
- $\alpha$ is the temperature coefficient of resistance, in $\text{K}^{-1}$.
- $\Delta\theta$ is the temperature change, in K (numerically the same as $^\circ\text{C}$).

For a **thermistor** the resistance **falls** with temperature, so $\alpha$ is negative (NTC).

**Worked example:** A wire of length $2.00~\text{m}$ and diameter $0.50~\text{mm}$ has resistance $4.5~\Omega$. Calculate its resistivity.

1. Radius $r = 0.25~\text{mm} = 2.5 \times 10^{-4}~\text{m}$.
2. $A = \pi r^2 = \pi(2.5 \times 10^{-4})^2 = 1.96 \times 10^{-7}~\text{m}^2$.
3. $\rho = \frac{RA}{L} = \frac{4.5 \times 1.96 \times 10^{-7}}{2.00} = 4.4 \times 10^{-7}~\Omega\,\text{m}$.

**Answer:** $\rho = 4.4 \times 10^{-7}~\Omega\,\text{m}$.

**Worked example:** A metal wire has resistance $50.0~\Omega$ at $0~^\circ\text{C}$ and $\alpha = 4.0 \times 10^{-3}~\text{K}^{-1}$. Calculate its resistance at $120~^\circ\text{C}$.

1. $\Delta\theta = 120~\text{K}$.
2. $R = 50.0(1 + 4.0 \times 10^{-3} \times 120) = 50.0(1 + 0.48)$.
3. $R = 74~\Omega$.

**Answer:** $R = 74~\Omega$.

## 2. Definition Sheet

> **Electromotive force (e.m.f.):** the energy transferred from chemical (or other) form to electrical form per unit charge driven around a complete circuit by a source. $E = \frac{W}{Q}$; unit V = J C$^{-1}$.
>
> Mark scheme: "energy transferred (from chemical to electrical) per unit charge" — both "energy" and "per unit charge" are needed. "Voltage across the battery" is not a definition.

> **Potential difference (p.d.):** the energy transferred from electrical form to other forms per unit charge between two points in a circuit. Unit V = J C$^{-1}$.

> **Internal resistance:** the resistance of the materials inside a source of e.m.f., which causes energy to be dissipated within the source when current flows. It is modelled as a resistor $r$ in series with an ideal cell of e.m.f. $E$.

> **Terminal potential difference:** the p.d. across the terminals of a source when it is supplying current; equal to the p.d. across the external circuit. $V = E - Ir$.

> **Lost volts:** the p.d. across the internal resistance of a source, $Ir$; the difference between the e.m.f. and the terminal p.d.

> **Potential divider:** a circuit of two or more resistors in series across a supply, used to obtain a fraction of the supply p.d.; $V_{\text{out}} = \frac{R_2}{R_1+R_2}V_{\text{in}}$.

> **Potentiometer:** a device used to compare potential differences by finding a balance point on a uniform resistance wire at which no current flows through the cell under test; at balance the p.d. across the balance length equals the e.m.f. of the cell.

> **Balanced (null) condition:** the jockey position at which the galvanometer reads zero, so no current flows through the unknown cell and its terminal p.d. equals its e.m.f.

> **Resistivity:** the resistance of a conductor of unit length and unit cross-sectional area, $R = \frac{\rho L}{A}$; unit $\Omega\,\text{m}$.

> **Temperature coefficient of resistance:** the fractional change in resistance per unit change in temperature, $\alpha = \frac{1}{R_0}\frac{\Delta R}{\Delta\theta}$; unit K$^{-1}$.

> **Ohmic conductor:** a conductor whose resistance remains constant when its temperature is constant, so its I–V graph is a straight line through the origin.

## 3. Formula Sheet

**Quick reference:**

$$E = \frac{W}{Q}, \quad I = \frac{E}{R+r}, \quad V = E - Ir, \quad P = I^2R, \quad P_{\max} = \frac{E^2}{4r}, \quad V_{\text{out}} = \frac{R_2}{R_1+R_2}V_{\text{in}}, \quad \frac{E_X}{E_Y} = \frac{l_X}{l_Y}, \quad R = \frac{\rho L}{A}, \quad R = R_0(1+\alpha\Delta\theta)$$

| Formula | Meaning of symbols | Units | When to use it |
|---|---|---|---|
| $$E = \frac{W}{Q}$$ | $E$ e.m.f., $W$ energy transferred, $Q$ charge | V, J, C | Definition of e.m.f.; energy per unit charge |
| $$I = \frac{E}{R+r}$$ | $I$ current, $E$ e.m.f., $R$ external resistance, $r$ internal resistance | A, V, $\Omega$ | Current in a single-loop circuit with a real source |
| $$V = E - Ir$$ | $V$ terminal p.d., $I$ current, $r$ internal resistance | V, A, $\Omega$ | Terminal p.d. when current flows; "lost volts" = $Ir$ |
| $$V = -rI + E$$ | Graph form: $V$ against $I$ | V, A | Intercept $=E$, gradient $=-r$ |
| $$P = I^2R = \frac{E^2R}{(R+r)^2}$$ | $P$ power in external resistor | W | Power delivered to the load |
| $$P_{\max} = \frac{E^2}{4r}$$ | Maximum power transfer, when $R=r$ | W | Maximum-power questions; efficiency then 50% |
| $$V_{\text{out}} = \frac{R_2}{R_1+R_2}V_{\text{in}}$$ | $V_{\text{out}}$ p.d. across $R_2$, $V_{\text{in}}$ supply p.d. | V, $\Omega$ | Unloaded potential divider |
| $$\frac{E_X}{E_Y} = \frac{l_X}{l_Y}$$ | Balance lengths on the same potentiometer wire | m (ratio) | Comparing two e.m.f.s or p.d.s |
| $$E_X = \frac{l_X}{L}V_{AB}$$ | $E_X$ unknown e.m.f., $L$ total wire length, $V_{AB}$ p.d. across wire | V, m | Potentiometer using a driver cell |
| $$R = \frac{\rho L}{A}$$ | $\rho$ resistivity, $L$ length, $A$ cross-sectional area | $\Omega$, $\Omega\,\text{m}$, m, m$^2$ | Resistivity calculations; $A=\pi d^2/4$ for a wire |
| $$R = R_0(1+\alpha\Delta\theta)$$ | $R_0$ resistance at reference temperature, $\alpha$ temperature coefficient | $\Omega$, K$^{-1}$, K | Metal resistance change with temperature |
| $$P = VI = I^2R = \frac{V^2}{R}$$ | Power in a component | W | Power in any resistor or lamp |

**Exam facts:** $V = E - Ir$ and $P = VI$ are on the data sheet. $P_{\max} = \frac{E^2}{4r}$ is **not** — derive it from $P = I^2R$ and $R=r$. The potentiometer relation $\frac{E_X}{E_Y} = \frac{l_X}{l_Y}$ is not printed either. For a circular wire use $A = \frac{\pi d^2}{4}$, not $\pi d^2$.

## 4. Methods (Question Types & Methods)

### 1. Find current, terminal p.d. and lost volts

**Method:**
1. Draw the source as $E$ and $r$ in series with the external resistance.
2. Add $r$ to the external resistance and use $I = \frac{E}{R+r}$.
3. Terminal p.d. $V = IR = E - Ir$; lost volts $= Ir$.
4. Check $V + Ir = E$.

**Traps:** using $E$ as the p.d. across the external resistor; forgetting to add $r$ to $R$; treating $r$ as parallel with $R$ (it is in series).

### 2. Find $E$ and $r$ from a $V$–$I$ graph or table

**Method:**
1. Plot $V$ (y-axis) against $I$ (x-axis).
2. Read the intercept at $I=0$: that is $E$.
3. Gradient $= -r$; quote $r$ as a positive resistance.
4. Alternatively use two simultaneous equations $V_1 = E - I_1r$ and $V_2 = E - I_2r$.

**Traps:** reading the gradient as $+r$; using the $I$-intercept as $r$; failing to convert mA to A (a factor of 1000 error in $r$).

### 3. Maximum power transfer

**Method:**
1. State the condition $R = r$.
2. Current at this condition: $I = \frac{E}{2r}$.
3. $P_{\max} = I^2R = \frac{E^2}{4r}$.
4. Efficiency $= \frac{P_{\text{load}}}{P_{\text{total}}} = 50\%$.

**Traps:** thinking maximum power means maximum efficiency (it is 50%); using $P = \frac{E^2}{R}$ with the wrong $R$; forgetting that at $R=r$ the terminal p.d. is $E/2$.

### 4. Cells in series and opposition

**Method:**
1. Choose a positive current direction.
2. Add e.m.f.s in that direction, subtract those opposing: $E_{\text{net}} = \sum E$.
3. Add all internal resistances (they are in series).
4. $I = \frac{E_{\text{net}}}{R + \sum r}$.
5. For a cell being charged, use $V = E + Ir$.

**Traps:** adding e.m.f.s that oppose; subtracting internal resistances; giving a charged cell $V = E - Ir$ (it is $E + Ir$).

### 5. Potential divider (unloaded)

**Method:**
1. Confirm the resistors are in series across the supply.
2. Identify which resistor the output is across — that resistance goes on top.
3. $V_{\text{out}} = \frac{R_{\text{out}}}{R_{\text{total}}}V_{\text{in}}$.
4. Check: the larger resistance takes the larger share.

**Traps:** inverting the ratio; using the wrong total resistance; forgetting the output may be across the other resistor.

### 6. Potential divider with a thermistor or LDR

**Method:**
1. Decide how the sensor resistance changes with the physical quantity (temperature up → thermistor $R$ down; light up → LDR $R$ down).
2. Work out whether the sensor's share of the supply rises or falls.
3. If the output is across the sensor, $V_{\text{out}}$ follows the sensor's share; if across the fixed resistor, it follows the fixed resistor's share.
4. Substitute at the two conditions and compare.

**Traps:** saying "resistance rises so voltage rises" without stating which component the output is across; forgetting that the sensor and fixed resistor share the **same current**.

### 7. Potentiometer balance

**Method:**
1. Find the p.d. per unit length: $\frac{V_{AB}}{L}$ (or use the standard-cell ratio).
2. Multiply by the balance length: $E_X = \frac{l_X}{L}V_{AB}$.
3. For comparison: $\frac{E_X}{E_Y} = \frac{l_X}{l_Y}$.
4. State the balance condition: galvanometer reads zero, so no current is drawn from the unknown cell and its terminal p.d. equals its e.m.f.

**Traps:** using the driver cell's e.m.f. as $V_{AB}$ when its internal resistance matters; measuring the balance length from the wrong end; forgetting that the unknown e.m.f. must be smaller than the driver's.

### 8. I–V characteristic and resistance at a point

**Method:**
1. Read $V$ and $I$ at the required point.
2. $R = \frac{V}{I}$ (not the gradient of the curve, unless the line is straight through the origin).
3. For a straight line through the origin, the gradient is $\frac{I}{V} = \frac{1}{R}$.

**Traps:** using the gradient of a curved characteristic as the resistance; reading the axes the wrong way round; forgetting that a lamp's resistance changes with temperature.

### 9. Resistivity

**Method:**
1. Convert length to m and diameter to m; radius $= \frac{d}{2}$.
2. $A = \pi r^2 = \frac{\pi d^2}{4}$.
3. $\rho = \frac{RA}{L}$.
4. Check units: $\Omega \times \text{m}^2 / \text{m} = \Omega\,\text{m}$.

**Traps:** using diameter as radius (factor of 4 in area); cm$^2$ → m$^2$ is $\times 10^{-4}$; mm → m is $\times 10^{-3}$.

## 5. Solved Examples

### Example 1: Terminal p.d. and lost volts

**Question:** A cell of e.m.f. $1.50~\text{V}$ and internal resistance $0.80~\Omega$ is connected to a $3.0~\Omega$ resistor. Calculate (a) the current, (b) the terminal p.d., (c) the power dissipated in the internal resistance.

**Method:**
1. (a) $I = \frac{1.50}{3.0+0.80} = \frac{1.50}{3.80} = 0.395~\text{A}$.
2. (b) $V = E - Ir = 1.50 - 0.395 \times 0.80 = 1.18~\text{V}$.
3. (c) $P_r = I^2r = 0.395^2 \times 0.80 = 0.125~\text{W}$.

**Answer:** (a) $0.39~\text{A}$; (b) $1.2~\text{V}$; (c) $0.13~\text{W}$.

**What the examiner wants:** the total resistance must include $r$; the terminal p.d. is across the external resistor only; power in $r$ uses $I^2r$, not $V^2/r$ with the terminal p.d.

### Example 2: Internal resistance from two current readings

**Question:** With a $2.00~\Omega$ resistor connected to a cell, the current is $0.625~\text{A}$. With a second identical resistor in series, the current falls to $0.341~\text{A}$. Calculate $r$ and $E$.

**Method:**
1. First: $E = 0.625(2.00 + r)$.
2. Second: $E = 0.341(4.00 + r)$.
3. Equate: $1.25 + 0.625r = 1.364 + 0.341r$.
4. $0.284r = 0.114$, so $r = 0.401~\Omega$.
5. $E = 0.625(2.401) = 1.50~\text{V}$.

**Answer:** $r = 0.40~\Omega$, $E = 1.50~\text{V}$.

**What the examiner wants:** two equations with the same $E$; correct expansion; an answer to 2–3 s.f. (the data justify 2 s.f.).

### Example 3: $V$–$I$ graph

**Question:** A cell gives terminal p.d. $1.40~\text{V}$ at $0.20~\text{A}$ and $1.10~\text{V}$ at $0.80~\text{A}$. Find $E$, $r$ and the short-circuit current.

**Method:**
1. $r = \frac{1.40-1.10}{0.80-0.20} = \frac{0.30}{0.60} = 0.50~\Omega$.
2. $E = V + Ir = 1.40 + 0.20 \times 0.50 = 1.50~\text{V}$.
3. Short circuit: $I_{\max} = \frac{E}{r} = \frac{1.50}{0.50} = 3.0~\text{A}$.

**Answer:** $E = 1.50~\text{V}$, $r = 0.50~\Omega$, $I_{\max} = 3.0~\text{A}$.

**What the examiner wants:** gradient magnitude for $r$; intercept for $E$; $I_{\max}$ from $V=0$.

### Example 4: Maximum power

**Question:** A battery of e.m.f. $9.0~\text{V}$ and internal resistance $1.5~\Omega$ is connected to a variable resistor. Calculate the maximum power that can be delivered to the resistor and the efficiency at this point.

**Method:**
1. Condition: $R = r = 1.5~\Omega$.
2. $I = \frac{9.0}{1.5+1.5} = 3.0~\text{A}$.
3. $P = I^2R = 9.0 \times 1.5 = 13.5~\text{W}$.
4. $P_{\text{total}} = EI = 27~\text{W}$, so efficiency $= \frac{13.5}{27} = 50\%$.

**Answer:** $P_{\max} = 13.5~\text{W}$; efficiency $50\%$.

**What the examiner wants:** the condition $R=r$ stated; power in the external resistor; the 50% result explained as equal dissipation in $r$ and $R$.

### Example 5: Cells in series

**Question:** Three cells, each e.m.f. $2.0~\text{V}$ and internal resistance $0.20~\Omega$, are connected in series with a $5.4~\Omega$ resistor. Calculate the current and the terminal p.d. of the combination.

**Method:**
1. $E_{\text{total}} = 3 \times 2.0 = 6.0~\text{V}$.
2. $r_{\text{total}} = 3 \times 0.20 = 0.60~\Omega$.
3. $I = \frac{6.0}{5.4+0.60} = 1.0~\text{A}$.
4. $V = E - Ir = 6.0 - 1.0 \times 0.60 = 5.4~\text{V}$ (equals $IR$).

**Answer:** $I = 1.0~\text{A}$; $V = 5.4~\text{V}$.

### Example 6: Cells in opposition

**Question:** A $12~\text{V}$ battery of internal resistance $0.50~\Omega$ is connected in opposition to a $9.0~\text{V}$ battery of internal resistance $0.30~\Omega$, with a $1.2~\Omega$ resistor in the loop. Calculate the current and the terminal p.d. of each battery.

**Method:**
1. $E_{\text{net}} = 12 - 9.0 = 3.0~\text{V}$.
2. $R_{\text{total}} = 1.2 + 0.50 + 0.30 = 2.0~\Omega$.
3. $I = 1.5~\text{A}$.
4. $12~\text{V}$ battery (driving): $V = 12 - 1.5 \times 0.50 = 11.25~\text{V}$.
5. $9.0~\text{V}$ battery (charged): $V = 9.0 + 1.5 \times 0.30 = 9.45~\text{V}$.

**Answer:** $I = 1.5~\text{A}$; $V_{12} = 11.25~\text{V}$, $V_{9} = 9.45~\text{V}$.

### Example 7: Potential divider

**Question:** A $24~\text{V}$ supply is connected across a $8.0~\text{k}\Omega$ and a $4.0~\text{k}\Omega$ resistor in series. Calculate the p.d. across each.

**Method:**
1. $R_{\text{total}} = 12~\text{k}\Omega$.
2. Across $8.0~\text{k}\Omega$: $V = \frac{8.0}{12} \times 24 = 16~\text{V}$.
3. Across $4.0~\text{k}\Omega$: $V = \frac{4.0}{12} \times 24 = 8.0~\text{V}$.

**Answer:** $16~\text{V}$ and $8.0~\text{V}$; they add to $24~\text{V}$.

### Example 8: Thermistor divider

**Question:** A thermistor is in series with a $2.0~\text{k}\Omega$ resistor across a $6.0~\text{V}$ supply, output across the fixed resistor. At $25~^\circ\text{C}$ the thermistor is $4.0~\text{k}\Omega$; at $55~^\circ\text{C}$ it is $1.0~\text{k}\Omega$. Calculate $V_{\text{out}}$ at each temperature and state the effect of warming.

**Method:**
1. At $25~^\circ\text{C}$: $V_{\text{out}} = \frac{2.0}{4.0+2.0} \times 6.0 = 2.0~\text{V}$.
2. At $55~^\circ\text{C}$: $V_{\text{out}} = \frac{2.0}{1.0+2.0} \times 6.0 = 4.0~\text{V}$.
3. Warming lowers the thermistor resistance, so the fixed resistor takes a larger share.

**Answer:** $2.0~\text{V}$ at $25~^\circ\text{C}$, rising to $4.0~\text{V}$ at $55~^\circ\text{C}$.

### Example 9: LDR divider

**Question:** An LDR is in series with a $4.7~\text{k}\Omega$ resistor across a $5.0~\text{V}$ supply, output across the LDR. The LDR is $1.0~\text{k}\Omega$ in bright light and $500~\text{k}\Omega$ in darkness. Calculate $V_{\text{out}}$ in each case.

**Method:**
1. Bright: $V_{\text{out}} = \frac{1.0}{1.0+4.7} \times 5.0 = 0.877~\text{V}$.
2. Dark: $V_{\text{out}} = \frac{500}{500+4.7} \times 5.0 = 4.95~\text{V}$.
3. The output rises in darkness because the LDR takes a larger share.

**Answer:** $0.88~\text{V}$ bright, $4.95~\text{V}$ dark.

### Example 10: Potentiometer with a driver cell

**Question:** A driver cell of e.m.f. $3.0~\text{V}$ is connected across a uniform $1.00~\text{m}$ potentiometer wire of negligible resistance. An unknown cell balances at $42.0~\text{cm}$. Calculate the unknown e.m.f. and explain why the value is only an estimate.

**Method:**
1. p.d. per metre $= 3.0~\text{V m}^{-1}$.
2. $E_X = 3.0 \times 0.420 = 1.26~\text{V}$.
3. The driver cell has internal resistance, so the p.d. across the wire is slightly less than $3.0~\text{V}$; also the wire may not be perfectly uniform.

**Answer:** $E_X \approx 1.26~\text{V}$; it is an estimate because the driver's terminal p.d. is less than its e.m.f. (and the wire may not be uniform).

### Example 11: Potentiometer with a standard cell

**Question:** A standard cell of e.m.f. $1.500~\text{V}$ balances at $50.0~\text{cm}$. An unknown cell balances at $42.0~\text{cm}$ under the same conditions. Calculate $E_X$.

**Method:**
1. $\frac{E_X}{1.500} = \frac{42.0}{50.0}$.
2. $E_X = 1.500 \times 0.840 = 1.26~\text{V}$.

**Answer:** $E_X = 1.26~\text{V}$; using a standard cell removes the driver's internal-resistance error.

### Example 12: Resistivity and temperature coefficient

**Question:** A metal wire of length $1.50~\text{m}$ and diameter $0.40~\text{mm}$ has resistance $5.2~\Omega$ at $20~^\circ\text{C}$. (a) Calculate its resistivity. (b) The temperature coefficient is $4.0 \times 10^{-3}~\text{K}^{-1}$ referred to $0~^\circ\text{C}$; estimate the resistance at $100~^\circ\text{C}$.

**Method:**
1. (a) $r = 0.20~\text{mm} = 2.0 \times 10^{-4}~\text{m}$; $A = \pi(2.0 \times 10^{-4})^2 = 1.257 \times 10^{-7}~\text{m}^2$.
2. $\rho = \frac{RA}{L} = \frac{5.2 \times 1.257 \times 10^{-7}}{1.50} = 4.36 \times 10^{-7}~\Omega\,\text{m}$.
3. (b) Using $R_0 \approx \frac{5.2}{1+4.0\times10^{-3}\times20} = \frac{5.2}{1.08} = 4.81~\Omega$.
4. $R_{100} = 4.81(1 + 4.0 \times 10^{-3} \times 100) = 4.81 \times 1.40 = 6.7~\Omega$.

**Answer:** (a) $\rho = 4.4 \times 10^{-7}~\Omega\,\text{m}$; (b) $R \approx 6.7~\Omega$.

## 6. Exam-Style Questions (Full Solutions)

### Question 1

A battery of e.m.f. $9.0~\text{V}$ and internal resistance $1.2~\Omega$ is connected to a $3.6~\Omega$ resistor. Calculate (a) the current, (b) the terminal p.d., (c) the power dissipated in the external resistor and in the battery, (d) the efficiency.

**Solution:**
1. (a) $I = \frac{9.0}{3.6+1.2} = \frac{9.0}{4.8} = 1.875~\text{A}$.
2. (b) $V = IR = 1.875 \times 3.6 = 6.75~\text{V}$.
3. (c) $P_R = I^2R = 1.875^2 \times 3.6 = 12.7~\text{W}$; $P_r = I^2r = 1.875^2 \times 1.2 = 4.22~\text{W}$.
4. (d) $P_{\text{total}} = EI = 9.0 \times 1.875 = 16.9~\text{W}$; efficiency $= \frac{12.7}{16.9} = 75\%$.

**Answer:** $1.9~\text{A}$; $6.8~\text{V}$; $13~\text{W}$ and $4.2~\text{W}$; $75\%$.

### Question 2

A cell is connected to a variable resistor. The graph of terminal p.d. $V$ against current $I$ is a straight line with intercept $1.50~\text{V}$ on the $V$-axis and gradient $-0.80~\text{V A}^{-1}$. (a) State the e.m.f. and internal resistance. (b) Calculate the short-circuit current. (c) Calculate the terminal p.d. when the current is $0.50~\text{A}$.

**Solution:**
1. (a) Intercept gives $E = 1.50~\text{V}$; gradient magnitude gives $r = 0.80~\Omega$.
2. (b) $I_{\max} = \frac{E}{r} = \frac{1.50}{0.80} = 1.875~\text{A}$.
3. (c) $V = E - Ir = 1.50 - 0.50 \times 0.80 = 1.10~\text{V}$.

**Answer:** (a) $1.50~\text{V}$, $0.80~\Omega$; (b) $1.9~\text{A}$; (c) $1.10~\text{V}$.

### Question 3

A supply of e.m.f. $6.0~\text{V}$ and internal resistance $1.5~\Omega$ feeds a variable resistor $R$. (a) State the value of $R$ for maximum power transfer. (b) Calculate the maximum power. (c) Explain why operating at this point is inefficient.

**Solution:**
1. (a) $R = r = 1.5~\Omega$.
2. (b) $I = \frac{6.0}{1.5+1.5} = 2.0~\text{A}$; $P = I^2R = 4.0 \times 1.5 = 6.0~\text{W}$.
3. (c) At this point $I^2r = I^2R$, so half the total power is dissipated inside the supply; efficiency is only 50%.

**Answer:** (a) $1.5~\Omega$; (b) $6.0~\text{W}$; (c) half the power is wasted in $r$.

### Question 4

An NTC thermistor is in series with a $3.0~\text{k}\Omega$ resistor across a $9.0~\text{V}$ supply, with the output across the fixed resistor. The thermistor resistance is $6.0~\text{k}\Omega$ at $20~^\circ\text{C}$ and $1.0~\text{k}\Omega$ at $50~^\circ\text{C}$. (a) Calculate $V_{\text{out}}$ at each temperature. (b) State and explain how $V_{\text{out}}$ changes as the temperature rises. (c) Calculate the thermistor resistance at which $V_{\text{out}} = 4.5~\text{V}$.

**Solution:**
1. (a) At $20~^\circ\text{C}$: $V_{\text{out}} = \frac{3.0}{6.0+3.0} \times 9.0 = 3.0~\text{V}$.
2. At $50~^\circ\text{C}$: $V_{\text{out}} = \frac{3.0}{1.0+3.0} \times 9.0 = 6.75~\text{V}$.
3. (b) $V_{\text{out}}$ rises because the thermistor resistance falls, so the fixed resistor takes a larger fraction of the supply p.d.
4. (c) $4.5 = \frac{3.0}{R_T+3.0} \times 9.0$, so $R_T + 3.0 = 6.0$ and $R_T = 3.0~\text{k}\Omega$.

**Answer:** (a) $3.0~\text{V}$ and $6.75~\text{V}$; (b) rises, because the thermistor's share falls; (c) $3.0~\text{k}\Omega$.

### Question 5

A potentiometer uses a driver cell of e.m.f. $4.0~\text{V}$ across a uniform $1.00~\text{m}$ wire of negligible resistance. (a) An unknown cell balances at $37.0~\text{cm}$; calculate its e.m.f. (b) A standard cell of e.m.f. $1.230~\text{V}$ balances at $31.2~\text{cm}$; use this to recalculate the unknown e.m.f. (c) Explain why the answer in (b) is more reliable.

**Solution:**
1. (a) $E_X = \frac{37.0}{100} \times 4.0 = 1.48~\text{V}$.
2. (b) $E_X = 1.230 \times \frac{37.0}{31.2} = 1.230 \times 1.186 = 1.46~\text{V}$.
3. (c) The standard-cell method cancels the driver's terminal p.d. and any non-uniformity of the wire, because both cells are compared under identical conditions; the driver's e.m.f. is not assumed to appear fully across the wire.

**Answer:** (a) $1.48~\text{V}$; (b) $1.46~\text{V}$; (c) ratio method removes driver and wire errors.

### Question 6

A $12~\text{V}$, $36~\text{W}$ car headlamp is connected to a battery of e.m.f. $12~\text{V}$ and internal resistance $0.040~\Omega$. (a) Calculate the normal resistance of the lamp. (b) Calculate the p.d. across the lamp when the starter motor draws $100~\text{A}$ from the same battery. (c) Explain why the lamps dim.

**Solution:**
1. (a) $P = \frac{V^2}{R}$, so $R = \frac{12^2}{36} = 4.0~\Omega$.
2. (b) Terminal p.d. $V = E - Ir = 12 - 100 \times 0.040 = 8.0~\text{V}$.
3. (c) The large starter current causes a large lost volts $Ir$ inside the battery, so the terminal p.d. falls and the lamps receive less power ($P = V^2/R$).

**Answer:** (a) $4.0~\Omega$; (b) $8.0~\text{V}$; (c) terminal p.d. falls because of the large $Ir$ drop.

## 7. Cheat Sheet

**Formulas:**
- $E = \frac{W}{Q}$; $I = \frac{E}{R+r}$; $V = E - Ir$; lost volts $= Ir$.
- $V$–$I$ graph: intercept $= E$, gradient $= -r$.
- $P = I^2R$; maximum power when $R = r$, $P_{\max} = \frac{E^2}{4r}$ (efficiency 50%).
- Series cells: e.m.f.s and internal resistances add. Opposition: subtract e.m.f.s, add resistances.
- Divider: $V_{\text{out}} = \frac{R_2}{R_1+R_2}V_{\text{in}}$.
- Potentiometer: $\frac{E_X}{E_Y} = \frac{l_X}{l_Y}$; at balance the galvanometer reads zero and no current is drawn from the unknown cell.
- $R = \frac{\rho L}{A}$; $A = \frac{\pi d^2}{4}$; $R = R_0(1+\alpha\Delta\theta)$.

**Rules that win marks:**
- The terminal p.d. is always **less** than the e.m.f. when current flows.
- A high-resistance voltmeter reads approximately $E$ because $I \approx 0$.
- Thermistor/LDR: resistance falls as temperature/light rises; the output change depends on **which resistor** the voltmeter is across.
- A potentiometer measures e.m.f. accurately because at balance **no current** flows through the cell, so there are no lost volts.
- Ohmic conductor: I–V straight line through origin at constant temperature. Filament lamp: resistance rises with temperature.

**Common traps:**
- Forgetting to add $r$ to $R$.
- Using $E$ instead of $V$ in $P = \frac{V^2}{R}$ for the external load.
- Saying maximum power means maximum efficiency.
- Adding opposing e.m.f.s.
- Inverting the potential-divider ratio.
- Using diameter as radius in $A = \pi r^2$.
- Forgetting that a charged cell has $V = E + Ir$.

## 8. Common Exam Mistakes

1. **Treating terminal p.d. as the e.m.f.** The e.m.f. is fixed by the source; the terminal p.d. depends on the current. Always write $V = E - Ir$ when current flows.
2. **Forgetting the internal resistance in the current calculation.** Use $I = \frac{E}{R+r}$, not $\frac{E}{R}$. If the question says "negligible internal resistance", then $r = 0$ and $V = E$.
3. **Reading the $V$–$I$ gradient as $+r$.** The line slopes downwards: gradient $= -r$, so quote the magnitude as the resistance.
4. **Confusing maximum power with maximum efficiency.** Maximum power transfer occurs at $R = r$ and is only 50% efficient. Maximum efficiency occurs when $R \gg r$, but the power delivered is then small.
5. **Adding e.m.f.s in opposition.** Choose a direction and subtract the opposing e.m.f.; do not add magnitudes blindly.
6. **Giving a charged cell $V = E - Ir$.** When current is forced into the positive terminal, the cell is being charged and $V = E + Ir$.
7. **Taking the output across the wrong component in a divider.** Decide explicitly whether $V_{\text{out}}$ is across the sensor or the fixed resistor; the two change in opposite directions.
8. **Using the driver cell's e.m.f. as the wire p.d.** The driver supplies current, so its terminal p.d. is less than $E_0$; the standard-cell comparison avoids this error.
9. **Sliding the jockey.** The wire becomes non-uniform, so p.d. is no longer proportional to length. Tap gently and briefly.
10. **Using diameter for radius.** $A = \pi r^2 = \frac{\pi d^2}{4}$. A diameter error changes the area by a factor of 4.
11. **Forgetting prefix conversions.** mA → A ($\times 10^{-3}$), k$\Omega$ → $\Omega$ ($\times 10^3$), cm → m ($\times 10^{-2}$), mm → m ($\times 10^{-3}$), cm$^2$ → m$^2$ ($\times 10^{-4}$).
12. **Using the gradient of a curved I–V characteristic as resistance.** Resistance at a point is $\frac{V}{I}$, the reciprocal of the gradient of the line from the origin to that point.
