# A2 Physics: All Chapter Summaries (Definitions, Formulas, Methods, Solved Examples, Notes)


---

# Chapter 12: Practical Circuits - CAIE A Level Physics (9702) Study Notes

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

---

# Chapter 13: Waves - CAIE A Level Physics (9702) Study Notes

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

---

# Chapter 14: Superposition of Waves - CAIE A Level Physics (9702) Study Notes

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

---

# Chapter 15: Stationary Waves - CAIE A Level Physics (9702) Study Notes

## 2. Definition Sheet

> **Stationary (standing) wave:** a wave pattern formed when two progressive waves of the same frequency and amplitude travel in opposite directions and superpose; it has fixed nodes and antinodes and transfers no net energy along the wave.

> **Node:** a point on a stationary wave where the amplitude of vibration is always zero.

> **Antinode:** a point on a stationary wave where the amplitude of vibration is maximum.

> **Fundamental mode:** the lowest-frequency stationary-wave pattern possible for a given system; it has the longest wavelength.

> **Fundamental frequency:** the minimum frequency of a stationary wave for a given system or arrangement.

> **Harmonic:** a stationary-wave mode whose frequency is an integer multiple of the fundamental frequency; the $n$th harmonic has frequency $nf_0$.

> **Resonance:** the condition in which a system is driven at one of its natural frequencies, giving maximum amplitude because energy is transferred most efficiently.

> **End correction:** the small distance beyond the open end of a pipe at which the displacement antinode actually forms; it must be added to the measured length, $l + c$.

> **Closed pipe:** an air column closed at one end and open at the other; it has a node at the closed end and an antinode at the open end, and supports only odd harmonics.

> **Open pipe:** an air column open at both ends; it has an antinode at each end and supports all harmonics.

## 3. Formula Sheet

**Quick reference:**

$$\frac{\lambda}{2} = \text{node–node spacing}, \quad \frac{\lambda}{4} = \text{node–antinode spacing}, \quad v = f\lambda, \quad f_n = \frac{nv}{2l}~\text{(string/open pipe)}, \quad f_n = \frac{(2n-1)v}{4l}~\text{(closed pipe)}, \quad \lambda = 2(l_2-l_1), \quad c = \frac{\lambda}{4}-l_1$$

| Formula | Meaning of symbols | Units | When to use it |
|---|---|---|---|
| $$\lambda = 2 \times (\text{node–node distance})$$ | $\lambda$ wavelength | m | Any stationary-wave pattern |
| $$\lambda = 4 \times (\text{node–antinode distance})$$ | $\lambda$ wavelength | m | Checking a pattern or finding $\lambda$ |
| $$v = f\lambda$$ | $v$ wave speed, $f$ frequency | $\text{m s}^{-1}$, Hz | Link stationary pattern to the progressive wave |
| $$f_n = \frac{nv}{2l}$$ | $l$ string/pipe length, $n = 1,2,3,\dots$ | Hz | String fixed at both ends, or open pipe |
| $$\lambda_n = \frac{2l}{n}$$ | $n$th harmonic wavelength | m | String/open pipe mode shapes |
| $$f_n = \frac{(2n-1)v}{4l}$$ | $n = 1,2,3,\dots$ | Hz | Closed pipe (odd harmonics only) |
| $$\lambda_n = \frac{4l}{2n-1}$$ | $n$th resonance wavelength | m | Closed pipe mode shapes |
| $$l_1 + c = \frac{\lambda}{4}$$ | $l_1$ first resonance length, $c$ end correction | m | Resonance tube, first resonance |
| $$l_2 + c = \frac{3\lambda}{4}$$ | $l_2$ second resonance length | m | Resonance tube, second resonance |
| $$\lambda = 2(l_2-l_1)$$ | difference of resonance lengths | m | Eliminates the end correction |
| $$c = \frac{\lambda}{4}-l_1$$ | end correction | m | Finding $c$ after $\lambda$ is known |
| $$v = 2f(l_2-l_1)$$ | $f$ tuning-fork frequency | $\text{m s}^{-1}$ | Speed of sound from two resonances |

**Exam facts:** $v = f\lambda$ is on the data sheet. The harmonic formulas are **not** printed; derive them from the boundary conditions each time. Remember: string and open pipe have all harmonics; a closed pipe has only odd harmonics. The end-correction equations are not printed, but the subtraction $\lambda = 2(l_2-l_1)$ is easy to reproduce.

## 4. Methods (Question Types & Methods)

### 1. Find wavelength from a stationary-wave diagram

**Method:**
1. Identify the nodes (zero amplitude) and antinodes (maximum amplitude).
2. Count the number of half-wavelengths between the marked points.
3. $\lambda = 2 \times$ (adjacent node separation), or $\lambda = \frac{2l}{n}$ for $n$ loops.
4. Check with the node–antinode distance: it should be $\frac{\lambda}{4}$.

**Traps:** using the node–antinode distance as $\lambda$; counting loops as full wavelengths (each loop is $\frac{\lambda}{2}$); measuring from a node to the next node but calling it $\lambda$.

### 2. String fixed at both ends

**Method:**
1. Count the number of loops $n$.
2. $l = \frac{n\lambda}{2}$, so $\lambda = \frac{2l}{n}$.
3. $f = \frac{v}{\lambda} = \frac{nv}{2l}$.
4. The fundamental is $n=1$; the $n$th harmonic has frequency $nf_0$.

**Traps:** using $n$ as the number of nodes (it is the number of loops); forgetting that both ends are nodes; assuming the first drawn pattern is the fundamental (count the loops).

### 3. Open pipe

**Method:**
1. Antinodes at both ends; the simplest pattern has a node in the middle.
2. Fundamental: $l = \frac{\lambda}{2}$, $\lambda = 2l$, $f_0 = \frac{v}{2l}$.
3. Harmonics: $f_n = nf_0$ for all integers $n$.

**Traps:** putting a node at the open end; using $4l$ instead of $2l$; thinking only odd harmonics exist (that is the closed pipe).

### 4. Closed pipe

**Method:**
1. Node at the closed end, antinode at the open end.
2. Fundamental: $l = \frac{\lambda}{4}$, $\lambda = 4l$, $f_0 = \frac{v}{4l}$.
3. Resonances: $f = f_0, 3f_0, 5f_0, \dots$; in general $f_n = \frac{(2n-1)v}{4l}$.

**Traps:** using $2l$ instead of $4l$; including even harmonics; confusing displacement and pressure nodes.

### 5. Resonance tube with end correction

**Method:**
1. Write $l_1 + c = \frac{\lambda}{4}$ and $l_2 + c = \frac{3\lambda}{4}$.
2. Subtract: $\frac{\lambda}{2} = l_2 - l_1$, so $\lambda = 2(l_2-l_1)$.
3. $v = f\lambda$.
4. $c = \frac{\lambda}{4} - l_1$.

**Traps:** adding the lengths instead of subtracting; forgetting to convert cm to m; using the first and third resonance instead of the first and second (the factor changes).

### 6. Find the speed of sound from a stationary-wave experiment

**Method:**
1. Find $\lambda$ from the node spacing (or from two resonance lengths).
2. Use the known frequency $f$ of the source.
3. $v = f\lambda$.
4. If the experiment uses a microwave transmitter, use $c = f\lambda$ with $c = 3.0 \times 10^8~\text{m s}^{-1}$.

**Traps:** using the tuning-fork frequency in the wrong unit (kHz); using the separation of adjacent **antinodes** as $\lambda$ rather than $\frac{\lambda}{2}$.

### 7. Explain resonance

**Method:**
1. State that the driving frequency equals a natural frequency of the system.
2. Energy is transferred most efficiently, so the amplitude is maximum.
3. Give the practical example (air column, string, microwave cavity).
4. If asked why the pattern disappears when the frequency changes, say the new frequency no longer matches a natural frequency, so the reflected waves do not superpose in phase to build a large amplitude.

**Traps:** saying "the frequency increases so the amplitude increases" without the resonance condition; confusing resonance with forced vibration at any frequency.

### 8. Stationary vs progressive comparison

**Method:**
1. Energy: progressive transfers energy; stationary has no net transfer.
2. Amplitude: progressive constant (ideal); stationary varies from zero to maximum.
3. Phase: progressive varies continuously; stationary has points in phase within a loop and antiphase between loops.
4. Wavelength: progressive is crest-to-crest; stationary is twice the node spacing.

**Traps:** saying a stationary wave has "no energy" (it has energy, but no net transport); saying "the wave does not move so there is no frequency" (the particles still oscillate at $f$).

## 5. Solved Examples

### Example 1: Node spacing

**Question:** Adjacent nodes on a stationary wave are $0.15~\text{m}$ apart. Calculate the wavelength and the distance between adjacent antinodes.

**Method:**
1. $\frac{\lambda}{2} = 0.15~\text{m}$, so $\lambda = 0.30~\text{m}$.
2. Adjacent antinodes are also $\frac{\lambda}{2} = 0.15~\text{m}$ apart.

**Answer:** $\lambda = 0.30~\text{m}$; antinode spacing $= 0.15~\text{m}$.

### Example 2: String with two loops

**Question:** A string of length $60~\text{cm}$ vibrates with two loops. Calculate the wavelength and the separation of the two antinodes.

**Method:**
1. Two loops: $l = \lambda$, so $\lambda = 0.60~\text{m}$.
2. Adjacent antinodes are $\frac{\lambda}{2} = 0.30~\text{m}$ apart.

**Answer:** $\lambda = 0.60~\text{m}$; antinode separation $= 0.30~\text{m}$.

### Example 3: String with three loops

**Question:** The frequency of the vibrator in Example 2 is increased until three loops appear. Calculate the new wavelength.

**Method:**
1. Three loops: $l = \frac{3\lambda}{2}$.
2. $\lambda = \frac{2l}{3} = \frac{2 \times 0.60}{3} = 0.40~\text{m}$.

**Answer:** $\lambda = 0.40~\text{m}$.

### Example 4: String speed

**Question:** A $75~\text{cm}$ string vibrates in three loops at $120~\text{Hz}$. Calculate the speed of the progressive wave on the string.

**Method:**
1. $\lambda = \frac{2l}{n} = \frac{2 \times 0.75}{3} = 0.50~\text{m}$.
2. $v = f\lambda = 120 \times 0.50 = 60~\text{m s}^{-1}$.

**Answer:** $v = 60~\text{m s}^{-1}$.

### Example 5: Guitar fundamental

**Question:** A guitar string of length $0.64~\text{m}$ has a wave speed of $320~\text{m s}^{-1}$. Calculate its fundamental frequency.

**Method:**
1. $\lambda = 2l = 1.28~\text{m}$.
2. $f_0 = \frac{v}{\lambda} = \frac{320}{1.28} = 250~\text{Hz}$.

**Answer:** $f_0 = 250~\text{Hz}$.

### Example 6: Open pipe

**Question:** An open pipe is $0.40~\text{m}$ long. The speed of sound is $340~\text{m s}^{-1}$. Calculate the fundamental frequency and the frequency of the third harmonic.

**Method:**
1. $f_0 = \frac{v}{2l} = \frac{340}{0.80} = 425~\text{Hz}$.
2. Third harmonic: $3f_0 = 1275~\text{Hz}$.

**Answer:** $425~\text{Hz}$ and $1275~\text{Hz}$.

### Example 7: Closed pipe

**Question:** A closed pipe is $0.40~\text{m}$ long. The speed of sound is $340~\text{m s}^{-1}$. Calculate the fundamental frequency and the next two possible resonant frequencies.

**Method:**
1. $f_0 = \frac{v}{4l} = \frac{340}{1.60} = 212.5~\text{Hz}$.
2. Next: $3f_0 = 637.5~\text{Hz}$; then $5f_0 = 1062.5~\text{Hz}$.

**Answer:** $213~\text{Hz}$, $638~\text{Hz}$, $1063~\text{Hz}$ (odd harmonics).

### Example 8: Resonance tube

**Question:** A tuning fork of frequency $500~\text{Hz}$ gives resonances at $16.0~\text{cm}$ and $50.0~\text{cm}$. Calculate the wavelength, the speed of sound and the end correction.

**Method:**
1. $\lambda = 2(l_2-l_1) = 2(0.500-0.160) = 0.680~\text{m}$.
2. $v = f\lambda = 500 \times 0.680 = 340~\text{m s}^{-1}$.
3. $c = \frac{\lambda}{4} - l_1 = 0.170 - 0.160 = 0.010~\text{m}$.

**Answer:** $\lambda = 0.680~\text{m}$; $v = 340~\text{m s}^{-1}$; $c = 1.0~\text{cm}$.

### Example 9: Microwave stationary wave

**Question:** Adjacent maxima in a microwave stationary wave are $15~\text{mm}$ apart. Calculate the wavelength and frequency.

**Method:**
1. $\lambda = 2 \times 15 = 30~\text{mm} = 0.030~\text{m}$.
2. $f = \frac{c}{\lambda} = \frac{3.0 \times 10^8}{0.030} = 1.0 \times 10^{10}~\text{Hz}$.

**Answer:** $\lambda = 0.030~\text{m}$; $f = 1.0 \times 10^{10}~\text{Hz}$.

### Example 10: Phase difference

**Question:** Two points on a stationary wave are separated by $0.10~\text{m}$. The wavelength is $0.40~\text{m}$. State their phase difference if they lie in (a) the same loop, (b) adjacent loops.

**Method:**
1. The separation is $\frac{\lambda}{4}$.
2. (a) Points in the same loop oscillate in phase: $0^\circ$.
3. (b) Points in adjacent loops are separated by a node: $180^\circ$.

**Answer:** (a) $0^\circ$; (b) $180^\circ$.

### Example 11: Number of loops

**Question:** A string of length $1.50~\text{m}$ is driven at $300~\text{Hz}$ and the wave speed is $180~\text{m s}^{-1}$. Determine the number of loops in the stationary pattern.

**Method:**
1. $\lambda = \frac{v}{f} = \frac{180}{300} = 0.60~\text{m}$.
2. $n = \frac{2l}{\lambda} = \frac{3.00}{0.60} = 5$.

**Answer:** 5 loops.

### Example 12: Closed pipe resonance lengths

**Question:** A closed pipe resonates at lengths $0.25~\text{m}$ and $0.75~\text{m}$ with a $340~\text{Hz}$ source. Calculate $\lambda$, $v$ and $c$.

**Method:**
1. $\lambda = 2(0.75-0.25) = 1.00~\text{m}$.
2. $v = 340 \times 1.00 = 340~\text{m s}^{-1}$.
3. $c = \frac{1.00}{4} - 0.25 = 0$.

**Answer:** $\lambda = 1.00~\text{m}$; $v = 340~\text{m s}^{-1}$; $c = 0$ (idealised).

## 6. Exam-Style Questions (Full Solutions)

### Question 1

A stationary wave on a string has nodes $0.40~\text{m}$ apart. The frequency is $50~\text{Hz}$. (a) Calculate the wavelength. (b) Calculate the speed of the progressive waves on the string. (c) State the phase difference between two points $0.10~\text{m}$ apart in the same loop.

**Solution:**
1. (a) $\lambda = 2 \times 0.40 = 0.80~\text{m}$.
2. (b) $v = f\lambda = 50 \times 0.80 = 40~\text{m s}^{-1}$.
3. (c) They are in the same loop, so they oscillate in phase: $0^\circ$.

**Answer:** (a) $0.80~\text{m}$; (b) $40~\text{m s}^{-1}$; (c) $0^\circ$.

### Question 2

A string of length $1.20~\text{m}$ is fixed at both ends and vibrates at $240~\text{Hz}$ with four loops. (a) Calculate the wavelength. (b) Calculate the wave speed. (c) Calculate the fundamental frequency. (d) State the frequency of the third harmonic.

**Solution:**
1. (a) $\lambda = \frac{2l}{n} = \frac{2 \times 1.20}{4} = 0.60~\text{m}$.
2. (b) $v = f\lambda = 240 \times 0.60 = 144~\text{m s}^{-1}$.
3. (c) $f_0 = \frac{v}{2l} = \frac{144}{2.40} = 60~\text{Hz}$.
4. (d) Third harmonic $= 3f_0 = 180~\text{Hz}$.

**Answer:** (a) $0.60~\text{m}$; (b) $144~\text{m s}^{-1}$; (c) $60~\text{Hz}$; (d) $180~\text{Hz}$.

### Question 3

An air column closed at one end resonates at $256~\text{Hz}$ with a first resonance length of $31.2~\text{cm}$. The second resonance occurs at $97.8~\text{cm}$. (a) Calculate the wavelength. (b) Calculate the speed of sound. (c) Calculate the end correction.

**Solution:**
1. (a) $\lambda = 2(0.978-0.312) = 2(0.666) = 1.332~\text{m}$.
2. (b) $v = f\lambda = 256 \times 1.332 = 341~\text{m s}^{-1}$.
3. (c) $c = \frac{\lambda}{4} - l_1 = 0.333 - 0.312 = 0.021~\text{m}$.

**Answer:** (a) $1.33~\text{m}$; (b) $341~\text{m s}^{-1}$; (c) $2.1~\text{cm}$.

### Question 4

Explain why a closed pipe produces only odd harmonics, while an open pipe produces all harmonics.

**Solution:**
1. A closed pipe has a node at the closed end and an antinode at the open end. The shortest pattern is a quarter wavelength, $l = \frac{\lambda}{4}$. The next pattern that fits has three quarters, $l = \frac{3\lambda}{4}$, then five quarters, and so on. This gives $f = \frac{v}{4l}, \frac{3v}{4l}, \frac{5v}{4l}, \dots$ — odd multiples only.
2. An open pipe has antinodes at both ends and a node in the middle. The shortest pattern is a half wavelength, $l = \frac{\lambda}{2}$; the next is a full wavelength, $l = \lambda$; then $\frac{3\lambda}{2}$, and so on. This gives $f = \frac{v}{2l}, \frac{2v}{2l}, \frac{3v}{2l}, \dots$ — all integer multiples.

**Answer:** the boundary conditions allow only odd quarter-wavelength fits in a closed pipe, but any number of half-wavelength fits in an open pipe.

### Question 5

A microwave transmitter faces a metal plate. A probe moved along the line between them records maxima every $12.5~\text{mm}$. (a) Calculate the wavelength. (b) Calculate the frequency. (c) State whether the metal plate is a node or an antinode, and why.

**Solution:**
1. (a) $\lambda = 2 \times 12.5 = 25~\text{mm} = 0.025~\text{m}$.
2. (b) $f = \frac{c}{\lambda} = \frac{3.0 \times 10^8}{0.025} = 1.2 \times 10^{10}~\text{Hz}$.
3. (c) The metal plate is a **node**: the electric field cannot penetrate a conductor, so the reflected wave cancels the incident wave at the surface.

**Answer:** (a) $0.025~\text{m}$; (b) $1.2 \times 10^{10}~\text{Hz}$; (c) node, because the field is zero at the metal surface.

### Question 6

A stationary wave is formed on a string. State and explain three differences between this stationary wave and a progressive wave of the same frequency.

**Solution:**
1. Energy: the progressive wave transfers energy along its direction of travel; the stationary wave has no net energy transfer.
2. Amplitude: every point on an ideal progressive wave has the same amplitude; on a stationary wave the amplitude varies from zero at nodes to maximum at antinodes.
3. Phase: in a progressive wave the phase changes continuously with distance; in a stationary wave all points within a loop are in phase and adjacent loops are in antiphase.
4. (Optional) The stationary wave has fixed nodes and antinodes and no wave speed; the progressive wave profile travels at $v = f\lambda$.

**Answer:** energy transfer, amplitude variation and phase behaviour differ as above.

## 7. Cheat Sheet

**Geometry:**
- Node–node $= \frac{\lambda}{2}$; antinode–antinode $= \frac{\lambda}{2}$; node–antinode $= \frac{\lambda}{4}$.

**Strings and open pipes (all harmonics):**
- $f_n = \frac{nv}{2l}$, $n = 1, 2, 3, \dots$
- Fundamental: $\lambda = 2l$.

**Closed pipe (odd harmonics only):**
- $f_n = \frac{(2n-1)v}{4l}$, $n = 1, 2, 3, \dots$
- Fundamental: $\lambda = 4l$.

**Resonance tube:**
- $l_1 + c = \frac{\lambda}{4}$; $l_2 + c = \frac{3\lambda}{4}$.
- $\lambda = 2(l_2-l_1)$; $v = f\lambda$; $c = \frac{\lambda}{4}-l_1$.

**Rules that win marks:**
- A stationary wave is formed by two identical progressive waves travelling in **opposite** directions.
- Fixed end / closed end = **node**; open end = **antinode** (displacement).
- No net energy transfer in a stationary wave.
- Measure across several nodes to reduce percentage error.
- The end correction is a **systematic** error removed by subtracting two resonance lengths.

## 8. Common Exam Mistakes

1. **Saying adjacent nodes are one wavelength apart.** They are **half** a wavelength apart. This is the single most common error in the chapter.
2. **Counting loops as full wavelengths.** Each loop is $\frac{\lambda}{2}$; $n$ loops fit $l = \frac{n\lambda}{2}$.
3. **Using the open-pipe formula for a closed pipe.** A closed pipe has $\lambda = 4l$ for the fundamental, not $2l$.
4. **Including even harmonics for a closed pipe.** Only odd multiples of the fundamental are possible.
5. **Putting an antinode at a fixed end.** A fixed end cannot move, so it must be a node.
6. **Confusing displacement and pressure nodes.** At a closed end the displacement is zero (node) but the pressure variation is maximum (pressure antinode). Read the question carefully.
7. **Adding the resonance lengths instead of subtracting.** $\lambda = 2(l_2-l_1)$; adding them gives no useful result.
8. **Forgetting to convert cm to m.** A wavelength quoted in cm must be converted before using $v = f\lambda$; otherwise the speed is wrong by $10^2$.
9. **Saying a stationary wave has no energy.** It has oscillating energy stored in the system; what it lacks is **net energy transfer** along the wave.
10. **Saying the frequency is zero because the wave does not travel.** The pattern is stationary, but every particle still oscillates at $f$; the wave speed of the pattern is zero, not the frequency.
11. **Measuring only one node separation.** The node positions have uncertainty; measure across several nodes and divide to reduce the percentage error.
12. **Ignoring the end correction.** The antinode is slightly beyond the open end; using $l$ alone gives a small systematic error in $\lambda$ and $v$.

---

# Chapter 16: Radioactivity - CAIE A Level Physics (9702) Study Notes

## 2. Definition Sheet

> **Nucleon:** a proton or a neutron in a nucleus.

> **Nucleon number ($A$):** the total number of protons and neutrons in a nucleus.

> **Proton number ($Z$):** the number of protons in a nucleus; it determines the element.

> **Neutron number ($N$):** the number of neutrons in a nucleus, $N = A - Z$.

> **Nuclide:** a particular combination of protons and neutrons in a nucleus, specified by $A$ and $Z$.

> **Isotopes:** nuclei of the same element with the same number of protons but different numbers of neutrons.

> **Ion:** an atom or molecule that has gained or lost one or more electrons, so it has a net charge.

> **Alpha-particle:** a helium-4 nucleus, consisting of two protons and two neutrons.

> **Beta-minus particle:** an electron emitted from a nucleus when a neutron changes into a proton.

> **Beta-plus particle (positron):** the antiparticle of the electron, emitted when a proton changes into a neutron.

> **Gamma radiation:** high-energy electromagnetic radiation emitted by an excited nucleus as it loses energy.

> **Neutrino:** a nearly massless, uncharged lepton emitted in beta-plus decay (electron neutrino).

> **Antineutrino:** the antiparticle of the neutrino, emitted in beta-minus decay.

> **Hadron:** a particle that experiences the strong nuclear force; made of quarks.

> **Lepton:** a fundamental particle that does not experience the strong nuclear force (e.g. electron, neutrino).

> **Quark:** a fundamental particle that makes up hadrons; the up and down quarks make protons and neutrons.

> **Strong nuclear force:** the short-range attractive force between nucleons that holds the nucleus together.

> **Weak interaction:** the force responsible for beta decay, acting on quarks and leptons.

> **Ionisation:** the removal of electrons from atoms by radiation, producing ion pairs.

> **Electronvolt (eV):** the energy gained or lost by an electron when it moves through a potential difference of $1~\text{V}$; $1~\text{eV} = 1.60 \times 10^{-19}~\text{J}$.

## 3. Formula Sheet

| Formula | Meaning of symbols | Units | When to use it |
|---|---|---|---|
| $A = Z + N$ | $A$ nucleon number, $Z$ proton number, $N$ neutron number | — | Finding protons/neutrons in a nuclide |
| ${}^{A}_{Z}\text{X}$ | nuclide notation | — | Writing nuclei and decay equations |
| ${}^{A}_{Z}\text{X} \rightarrow {}^{A-4}_{Z-2}\text{Y} + {}^{4}_{2}\text{He}$ | alpha decay | — | Alpha decay equations |
| ${}^{A}_{Z}\text{X} \rightarrow {}^{A}_{Z+1}\text{Y} + {}^{0}_{-1}\text{e} + \bar{\nu}_e$ | beta-minus decay | — | Beta-minus equations |
| ${}^{A}_{Z}\text{X} \rightarrow {}^{A}_{Z-1}\text{Y} + {}^{0}_{+1}\text{e} + \nu_e$ | beta-plus decay | — | Beta-plus equations |
| ${}^{A}_{Z}\text{X}^{*} \rightarrow {}^{A}_{Z}\text{X} + \gamma$ | gamma emission | — | Excited nucleus losing energy |
| $1~\text{eV} = 1.60 \times 10^{-19}~\text{J}$ | conversion | J | Converting particle energies |
| $1~\text{MeV} = 1.60 \times 10^{-13}~\text{J}$ | conversion | J | Nuclear/gamma energies |
| $r = \frac{mv}{qB}$ | $r$ radius of path, $B$ flux density | m | Charged particle in a magnetic field |
| $E = mc^2$ | mass–energy equivalence | J | Mass defect (Chapter 31) |

**Exam facts:** the quark charges and decay equations are **not** on the data sheet and must be memorised. $1~\text{eV} = 1.60 \times 10^{-19}~\text{J}$ is on the data sheet. The specific charge of an alpha-particle is about $4.8 \times 10^7~\text{C kg}^{-1}$.

## 4. Methods (Question Types & Methods)

### 1. Count protons, neutrons and electrons

**Method:**
1. Protons $= Z$ (lower number).
2. Neutrons $= A - Z$.
3. Electrons $= Z$ for a neutral atom; adjust for the charge if it is an ion.
4. Check: $A = Z + N$.

**Traps:** reading $A$ and $Z$ the wrong way round; forgetting that an alpha-particle has no electrons; giving the electron number as $A$.

### 2. Identify isotopes

**Method:**
1. Compare $Z$: same $Z$ means the same element.
2. Compare $A$: different $A$ means different isotopes.
3. Check that $N = A - Z$ differs.

**Traps:** saying "same number of nucleons" (that would be the same nuclide, not isotopes); confusing isotopes with ions.

### 3. Complete a decay equation

**Method:**
1. Write the equation with the unknown nuclide/particle.
2. Balance $A$ on both sides.
3. Balance $Z$ on both sides.
4. Identify the element from $Z$ using the periodic table.
5. Add the neutrino/antineutrino for beta decay.

**Traps:** forgetting the antineutrino in $\beta^-$; using a proton instead of a neutron in $\beta^+$; changing $A$ in beta decay (it does not change); losing charge conservation.

### 4. Determine the type of decay from $A$ and $Z$ changes

**Method:**
1. $\Delta A = -4$, $\Delta Z = -2$: alpha.
2. $\Delta A = 0$, $\Delta Z = +1$: beta-minus.
3. $\Delta A = 0$, $\Delta Z = -1$: beta-plus.
4. $\Delta A = 0$, $\Delta Z = 0$: gamma.

**Traps:** beta-plus and electron capture both decrease $Z$; if a neutrino is shown, it is beta-plus.

### 5. Explain Rutherford scattering

**Method:**
1. Most pass straight through → mostly empty space.
2. Some deflected → positive charge concentrated somewhere.
3. Few back-scattered → tiny, massive, positive nucleus.
4. Use the words "repulsive electrostatic force" and "closer approach → greater force".

**Traps:** saying the nucleus attracts alpha-particles (it repels them); saying electrons cause the large deflections (they are too light).

### 6. Compare ionising radiations

**Method:**
1. State charge and mass.
2. Link charge/mass/speed to ionising power.
3. Link ionising power to range/penetration (inverse relationship).
4. State the absorber needed.

**Traps:** saying gamma is "not ionising" (it is, but weakly); saying alpha has the greatest range; confusing penetration with ionising power.

### 7. Quark calculations

**Method:**
1. Write the quark composition (proton uud, neutron udd).
2. Add the charges in units of $e$.
3. Check the total equals the known charge.
4. For beta decay, identify which quark changes: d → u ($\beta^-$) or u → d ($\beta^+$).

**Traps:** using $+1/3$ for down; forgetting that antiquarks have opposite charge; thinking a beta-particle is a quark (it is a lepton).

### 8. Convert eV and MeV to joules

**Method:**
1. Convert MeV to eV by multiplying by $10^6$.
2. Multiply by $1.60 \times 10^{-19}$.
3. Check the power of ten: nuclear energies are typically $10^{-13}$ to $10^{-12}~\text{J}$.

**Traps:** using $1.60 \times 10^{-19}$ as the MeV-to-J conversion directly; forgetting the $10^6$.

## 5. Solved Examples

### Example 1: Nuclide composition

**Question:** Determine the number of protons, neutrons and electrons in ${}^{56}_{26}\text{Fe}$.

**Method:**
1. Protons $= 26$.
2. Neutrons $= 56 - 26 = 30$.
3. Electrons $= 26$ (neutral atom).

**Answer:** 26 protons, 30 neutrons, 26 electrons.

### Example 2: Isotope identification

**Question:** Which of ${}^{12}_{6}\text{C}$, ${}^{14}_{6}\text{C}$ and ${}^{14}_{7}\text{N}$ are isotopes of each other?

**Method:**
1. Isotopes have the same $Z$.
2. ${}^{12}_{6}\text{C}$ and ${}^{14}_{6}\text{C}$ both have $Z = 6$.
3. ${}^{14}_{7}\text{N}$ has $Z = 7$, so it is a different element.

**Answer:** the two carbon nuclides are isotopes.

### Example 3: Alpha decay

**Question:** ${}^{226}_{88}\text{Ra}$ decays by alpha emission. Write the equation.

**Method:**
1. $A: 226 - 4 = 222$.
2. $Z: 88 - 2 = 86$.
3. $Z = 86$ is radon (Rn).

**Answer:** ${}^{226}_{88}\text{Ra} \rightarrow {}^{222}_{86}\text{Rn} + {}^{4}_{2}\text{He}$.

### Example 4: Beta-minus decay

**Question:** ${}^{90}_{38}\text{Sr}$ decays by beta-minus emission. Write the equation.

**Method:**
1. $A$ stays 90.
2. $Z: 38 + 1 = 39$.
3. $Z = 39$ is yttrium (Y).
4. Emit an electron and an antineutrino.

**Answer:** ${}^{90}_{38}\text{Sr} \rightarrow {}^{90}_{39}\text{Y} + {}^{0}_{-1}\text{e} + \bar{\nu}_e$.

### Example 5: Beta-plus decay

**Question:** ${}^{23}_{12}\text{Mg}$ decays by beta-plus emission. Write the equation.

**Method:**
1. $A$ stays 23.
2. $Z: 12 - 1 = 11$.
3. $Z = 11$ is sodium (Na).
4. Emit a positron and a neutrino.

**Answer:** ${}^{23}_{12}\text{Mg} \rightarrow {}^{23}_{11}\text{Na} + {}^{0}_{+1}\text{e} + \nu_e$.

### Example 6: Missing particle

**Question:** Complete ${}^{1}_{0}\text{n} \rightarrow {}^{1}_{1}\text{p} + \text{?} + \bar{\nu}_e$.

**Method:**
1. $A: 1 = 1 + A + 0$, so $A = 0$.
2. $Z: 0 = 1 + Z + 0$, so $Z = -1$.
3. The particle with $A = 0$, $Z = -1$ is an electron.

**Answer:** ${}^{0}_{-1}\text{e}$ (a beta-minus particle).

### Example 7: Quark charge

**Question:** Show that a proton has charge $+e$ using the quark model.

**Method:**
1. Proton = uud.
2. Charge $= +\frac{2}{3}e + \frac{2}{3}e - \frac{1}{3}e$.
3. Charge $= +1e$.

**Answer:** uud gives $+e$.

### Example 8: Quark change

**Question:** State the quark change in beta-plus decay.

**Method:**
1. Beta-plus: proton → neutron.
2. Proton is uud, neutron is udd.
3. One up quark becomes a down quark.

**Answer:** u → d, with emission of a positron and a neutrino.

### Example 9: Energy conversion

**Question:** A beta-particle has kinetic energy $1.2~\text{MeV}$. Calculate its energy in joules.

**Method:**
1. $1.2~\text{MeV} = 1.2 \times 10^6~\text{eV}$.
2. $E = 1.2 \times 10^6 \times 1.60 \times 10^{-19}$.
3. $E = 1.92 \times 10^{-13}~\text{J}$.

**Answer:** $1.9 \times 10^{-13}~\text{J}$.

### Example 10: Alpha then beta

**Question:** ${}^{238}_{92}\text{U}$ emits an alpha-particle, then a beta-minus particle. Determine the final $A$ and $Z$.

**Method:**
1. Alpha: $A = 238 - 4 = 234$; $Z = 92 - 2 = 90$.
2. Beta-minus: $A = 234$; $Z = 90 + 1 = 91$.

**Answer:** $A = 234$, $Z = 91$ (protactinium).

### Example 11: Number of decays

**Question:** ${}^{210}_{82}\text{Pb}$ decays to ${}^{206}_{82}\text{Pb}$. How many alpha and beta-minus particles are emitted?

**Method:**
1. $\Delta A = 210 - 206 = 4$, so one alpha-particle.
2. One alpha changes $Z$ by $-2$, but the final $Z$ is the same.
3. Two beta-minus decays each increase $Z$ by 1, restoring $Z$.

**Answer:** one alpha and two beta-minus particles.

### Example 12: Nuclear density ratio

**Question:** The radius of a nucleus is about $10^{-15}~\text{m}$ and the radius of an atom is about $10^{-10}~\text{m}$. Show that the density of nuclear matter is about $10^{15}$ times the density of the atom.

**Method:**
1. Volume ratio $= (10^{-10}/10^{-15})^3 = (10^5)^3 = 10^{15}$.
2. Density $= m/V$; almost all the mass is in the nucleus.
3. Nuclear density / atomic density $= (m/V_{\text{nucleus}})/(m/V_{\text{atom}}) = V_{\text{atom}}/V_{\text{nucleus}} = 10^{15}$.

**Answer:** the ratio is about $10^{15}$.

## 6. Exam-Style Questions (Full Solutions)

### Question 1

In Rutherford's alpha-particle scattering experiment, most alpha-particles passed straight through a thin gold foil, but a small fraction were deflected through angles greater than $90^\circ$. (a) State what this shows about the structure of the atom. (b) Explain why the alpha-particles are deflected. (c) Explain why the foil is made very thin.

**Solution:**
1. (a) The atom is mostly empty space, with a tiny, massive, positively charged nucleus at the centre containing most of the mass.
2. (b) The alpha-particle is positive and experiences a repulsive electrostatic force from the positive nucleus. The closer the approach, the stronger the force and the greater the deflection; a head-on collision gives back-scattering.
3. (c) A thin foil ensures that an alpha-particle is likely to pass through without being absorbed, and reduces the chance of multiple scattering, so the deflection is due to a single close encounter with a nucleus.

**Answer:** as above.

### Question 2

Complete the following equations and state the type of decay:
(a) ${}^{222}_{86}\text{Rn} \rightarrow \text{?} + {}^{4}_{2}\text{He}$
(b) ${}^{14}_{6}\text{C} \rightarrow {}^{14}_{7}\text{N} + \text{?}$
(c) ${}^{22}_{11}\text{Na} \rightarrow {}^{22}_{10}\text{Ne} + \text{?}$

**Solution:**
1. (a) $A = 218$, $Z = 84$: ${}^{218}_{84}\text{Po}$; alpha decay.
2. (b) $A = 0$, $Z = -1$: ${}^{0}_{-1}\text{e}$ (plus $\bar{\nu}_e$); beta-minus decay.
3. (c) $A = 0$, $Z = +1$: ${}^{0}_{+1}\text{e}$ (plus $\nu_e$); beta-plus decay.

**Answer:** (a) ${}^{218}_{84}\text{Po}$, alpha; (b) ${}^{0}_{-1}\text{e} + \bar{\nu}_e$, beta-minus; (c) ${}^{0}_{+1}\text{e} + \nu_e$, beta-plus.

### Question 3

Compare alpha, beta-minus and gamma radiation in terms of (a) charge, (b) ionising power, (c) penetrating power and (d) deflection in an electric field.

**Solution:**
1. (a) Alpha $+2e$; beta-minus $-e$; gamma 0.
2. (b) Alpha is most ionising (charged, massive, slow); beta is intermediate; gamma is least ionising.
3. (c) Alpha is least penetrating (paper/few cm air); beta is intermediate (few mm aluminium); gamma is most penetrating (cm of lead).
4. (d) Alpha deflects toward the negative plate; beta-minus toward the positive plate and much more strongly; gamma is undeflected.

**Answer:** as above.

### Question 4

A nucleus ${}^{A}_{Z}\text{X}$ decays by alpha emission followed by two beta-minus emissions. (a) Write the final nucleon and proton numbers. (b) State how the element changes. (c) Explain which conservation laws are obeyed.

**Solution:**
1. (a) Alpha: $A-4$, $Z-2$. Two beta-minus: $Z-2+2 = Z$; $A$ stays $A-4$.
2. (b) The final nucleus has the same $Z$ as the original but a different $A$, so it is a different isotope of the same element.
3. (c) Nucleon number is conserved ($A \rightarrow A-4+4$); proton number is conserved at each step when the emitted particles' charges are included; mass–energy is also conserved.

**Answer:** (a) $A-4$, $Z$; (b) same element, different isotope; (c) $A$, $Z$ and mass–energy.

### Question 5

Describe the quark model of the proton and neutron. Hence explain what happens in beta-minus decay.

**Solution:**
1. Proton = uud; charge $+\frac{2}{3}+\frac{2}{3}-\frac{1}{3} = +1$.
2. Neutron = udd; charge $+\frac{2}{3}-\frac{1}{3}-\frac{1}{3} = 0$.
3. In beta-minus decay, a neutron changes into a proton: one down quark changes into an up quark.
4. The nucleus emits an electron and an electron antineutrino: d → u + e$^-$ + $\bar{\nu}_e$.

**Answer:** proton uud, neutron udd; beta-minus is d → u with electron and antineutrino emission.

### Question 6

Explain why (a) alpha radiation is stopped by paper but gamma radiation is not, and (b) beta radiation is deflected more than alpha radiation in the same electric field.

**Solution:**
1. (a) Alpha particles are highly ionising because of their large charge and mass, so they lose energy rapidly in a short distance and are stopped by a few sheets of paper. Gamma photons are uncharged and interact weakly, so they can pass through paper and need dense, thick material such as lead to attenuate them.
2. (b) The electric force on a particle is $F = qE$. The beta-particle has a smaller charge magnitude than an alpha-particle, but its mass is about $1/7000$ as large. The acceleration $a = F/m$ is therefore much larger for the beta-particle, so it is deflected much more.

**Answer:** as above.

## 7. Cheat Sheet

**Nuclide notation:**
- ${}^{A}_{Z}\text{X}$: $A$ = protons + neutrons, $Z$ = protons, $N = A-Z$.
- Neutral atom: electrons $= Z$.

**Decay changes:**
- Alpha: $A-4$, $Z-2$.
- Beta-minus: $A$ unchanged, $Z+1$, emit e$^-$ + $\bar{\nu}_e$.
- Beta-plus: $A$ unchanged, $Z-1$, emit e$^+$ + $\nu_e$.
- Gamma: $A$, $Z$ unchanged.

**Quarks:**
- u = $+2/3$, d = $-1/3$, s = $-1/3$.
- Proton uud, neutron udd.
- Beta-minus: d → u; beta-plus: u → d.

**Radiation ranking:**
- Ionising: $\alpha > \beta > \gamma$.
- Penetrating: $\gamma > \beta > \alpha$.
- Alpha: paper; beta: few mm Al; gamma: cm Pb.

**Rutherford:**
- Most straight → empty space.
- Few large deflections → tiny, massive, positive nucleus.
- Repulsive electrostatic force.

**Energy:**
- $1~\text{eV} = 1.60 \times 10^{-19}~\text{J}$; $1~\text{MeV} = 1.60 \times 10^{-13}~\text{J}$.

## 8. Common Exam Mistakes

1. **Reading $A$ and $Z$ the wrong way round.** $A$ is the top (nucleon) number, $Z$ the bottom (proton) number.
2. **Saying isotopes have different proton numbers.** They have the **same** $Z$ and different $N$.
3. **Forgetting the antineutrino in beta-minus decay.** A beta-minus equation without $\bar{\nu}_e$ is incomplete in modern notation.
4. **Changing $A$ in beta decay.** Beta decay leaves the nucleon number unchanged; only $Z$ changes.
5. **Putting an electron in the nucleus.** Beta-particles are created at the moment of decay when a neutron changes into a proton; they were not orbiting inside the nucleus.
6. **Saying the nucleus attracts alpha-particles.** Both are positive, so the force is **repulsive**.
7. **Saying electrons cause the large deflections.** Electrons are far too light; the nucleus provides the concentrated positive charge and mass.
8. **Saying gamma is not ionising.** Gamma is weakly ionising; it is just far less ionising than alpha or beta.
9. **Confusing ionising power with penetrating power.** They are inversely related: the most ionising radiation is the least penetrating.
10. **Forgetting that alpha is dangerous inside the body.** Short range means concentrated energy deposition in tissue, even though it cannot penetrate skin.
11. **Using the wrong quark charge for down.** Down is $-1/3$, not $+1/3$.
12. **Treating a beta-particle as a hadron.** Beta-particles are leptons (electrons/positrons), not quarks.

---

# Chapter 17: Circular Motion - CAIE A Level Physics (9702) Study Notes

## 2. Definition Sheet

These are the definitions you must be able to write word-perfect. The mark schemes are strict: they want the exact phrases, not an equation and not a circular definition (never define a term using the term itself).

### Radian

> One radian is the angle subtended at the centre of a circle by an arc of length equal to the radius of the circle.

(Mark scheme wording: "the angle subtended at the centre of a circle by an arc equal in length to the radius".) Equivalent working form: $\theta = s/r$, so $360^{\circ} = 2\pi$ rad.

### Angular displacement

> The angle, measured in radians from a reference direction, through which an object has moved.

The exam rarely asks for this definition directly, but it appears inside the angular velocity definition and in "show that" work, so write it with "radians" and "reference direction" included.

### Angular velocity

> The rate of change of angular displacement.

(Mark scheme wording: "rate of change of angular displacement", or "angle turned through per unit time".) SI unit: $\text{rad s}^{-1}$. Do not answer with an equation alone, and do not write "speed of rotation" or "revolutions per second".

### Centripetal acceleration

> The acceleration of an object moving in a circle, directed towards the centre and perpendicular to the velocity.

(The 1-mark definition accepted in the November 2021 mark scheme is exactly "acceleration perpendicular to velocity". For full marks add "towards the centre", and if useful, that it arises because the direction of the velocity changes. Quoting an equation is not enough.)

### Centripetal force

> The resultant force acting on an object moving in a circle, directed towards the centre and perpendicular to the velocity.

(Two key ideas the mark scheme wants: it is a **resultant** force, and it points **towards the centre**. You can add that it is supplied by a real force such as tension, friction, gravity or a normal contact force. It is not a third force that "balances" the others, and there is no "centrifugal force" in the 9702 syllabus.)

### Period

> The time taken for one complete revolution (one complete cycle).

Symbol $T$, SI unit second (s). Related to frequency by $T = 1/f$, and to angular velocity by $\omega = 2\pi/T$. Watch out: the mark scheme sometimes uses $T$ for the period in the same question where $T$ is also the tension - label yours clearly.

### Frequency

> The number of complete revolutions (or cycles) per unit time.

Symbol $f$, SI unit hertz (Hz) or $\text{s}^{-1}$. Related to period by $f = 1/T$, and to angular velocity by $\omega = 2\pi f$. To convert rpm to Hz, divide by 60.

## 3. Formula Sheet

| Formula | Meaning of symbols | SI units | When to use it |
|---|---|---|---|
| $\theta = \dfrac{s}{r}$ | $\theta$ = angular displacement, $s$ = arc length, $r$ = radius | $\theta$ in rad, $s$, $r$ in m | Converting arc length to angle, or defining the radian |
| $\omega = \dfrac{\Delta\theta}{\Delta t}$ | $\omega$ = angular velocity, $\Delta\theta$ = angular displacement in time $\Delta t$ | $\text{rad s}^{-1}$ | Finding angular velocity from angle and time; definition of angular velocity |
| $\omega = \dfrac{2\pi}{T} = 2\pi f$ | $T$ = period (time for one revolution), $f$ = frequency | $T$ in s, $f$ in Hz | Converting period or frequency (or rpm) into angular velocity |
| $v = r\omega$ | $v$ = linear speed, $r$ = radius, $\omega$ = angular velocity | $v$ in $\text{m s}^{-1}$ | Finding speed of a point on a rotating body, or speed from angular velocity |
| $a = \dfrac{v^{2}}{r} = r\omega^{2} = v\omega$ | $a$ = centripetal acceleration | $\text{m s}^{-2}$ | Finding centripetal acceleration from speed, angular velocity, or both |
| $F = \dfrac{mv^{2}}{r} = mr\omega^{2}$ | $F$ = centripetal force (resultant force towards centre), $m$ = mass | N | Finding the centripetal force, or the real force supplying it (tension, friction, gravity) |
| $v_{\text{min}} = \sqrt{gr}$ (top of vertical circle) | $v_{\text{min}}$ = minimum speed at the top, $g$ = 9.81 $\text{m s}^{-2}$, $r$ = radius | $\text{m s}^{-1}$ | Minimum speed so a string stays taut, water stays in a bucket, or a truck keeps contact at the top of a loop |
| $T - mg = \dfrac{mv^{2}}{r}$ (bottom of vertical circle) | $T$ = tension or contact force, $mg$ = weight | N | Tension/contact force at the bottom of a vertical circle |
| $T + mg = \dfrac{mv^{2}}{r}$ (top of vertical circle) | as above | N | Tension/contact force at the top of a vertical circle |
| $v_{\text{bottom}}^{2} = v_{\text{top}}^{2} + 4gr$ | speeds at bottom and top, radius $r$ | $\text{m}^{2}\text{s}^{-2}$ | Linking speeds at top and bottom via conservation of energy |
| $\tan\theta = \dfrac{v^{2}}{rg}$ (conical pendulum or banked track) | $\theta$ = angle with vertical (pendulum) or banking angle, $v$ = speed, $r$ = radius | dimensionless | Finding the angle, or showing the bank/pendulum condition |
| $v_{\text{max}} = \sqrt{\mu r g}$ (flat road) | $\mu$ = coefficient of friction, $r$ = radius of bend | $\text{m s}^{-1}$ | Maximum cornering speed before a car skids on a flat road |
| $v = \sqrt{gr}$ (orbit) | $g$ = gravitational field strength at orbital radius $r$ | $\text{m s}^{-1}$ | Orbital speed of a satellite; $r$ measured from the centre of the planet |
| $T = \dfrac{2\pi r}{v}$ (orbit) | $T$ = orbital period | s | Time for one orbit once speed and radius are known |

Degrees-radians conversion: $\text{radians} = \text{degrees} \times \dfrac{\pi}{180^{\circ}}$ and $\text{degrees} = \text{radians} \times \dfrac{180^{\circ}}{\pi}$. Standard values: $180^{\circ} = \pi$ rad, $90^{\circ} = \pi/2$ rad, $45^{\circ} = \pi/4$ rad, $1$ rad $\approx 57.3^{\circ}$.

## 4. Methods (Question Types & Methods)

### Type 1: Define the radian, angular velocity, centripetal force or centripetal acceleration (1-2 marks)

These are recall questions and the mark scheme is strict.

- **Radian**: "the angle subtended at the centre of a circle by an arc equal in length to the radius".
- **Angular velocity**: "rate of change of angular displacement" (mention $\text{rad s}^{-1}$ if asked for units). Do not answer with an equation alone.
- **Centripetal force**: "the resultant force acting on an object moving in a circle, directed towards the centre (perpendicular to the velocity)". Two key ideas: resultant force, towards the centre. You can mention it is supplied by a real force such as tension or friction.
- **Centripetal acceleration**: the 1-mark definition accepted in the November 2021 mark scheme is "acceleration perpendicular to velocity". For full marks add "towards the centre" and, if useful, that it arises because the direction of the velocity changes.

Method: write the definition from memory, in proper technical language. Never define a term using the term itself (writing "centripetal acceleration is the acceleration due to the centripetal force" earns nothing), and never answer with an equation instead of a definition.

### Type 2: Convert between degrees and radians

Multiply degrees by $\pi/180$ to get radians, or radians by $180/\pi$ to get degrees. Express answers as multiples of $\pi$ where possible (for example $60^{\circ} = \pi/3$ rad). Show the conversion factor, because "show that" questions need the working.

### Type 3: Find angular velocity from period, frequency or rpm

Steps:

1. If given rpm, divide by 60 to get revolutions per second (frequency $f$).
2. Use $\omega = 2\pi f$ or $\omega = 2\pi/T$.
3. Give the answer in $\text{rad s}^{-1}$.

Example check: the second hand of a clock has $T = 60$ s, so $\omega = 2\pi/60 = 0.105 \ \text{rad s}^{-1}$.

### Type 4: Find the linear speed of a point on a rotating body

Use $v = r\omega$. First get $\omega$ (Type 3), then multiply by the radius. Watch the radius: use the distance of the point from the axis, and convert cm to m. Remember every point on a rigid rotating body shares the same $\omega$ but $v$ grows with $r$.

### Type 5: Find centripetal acceleration

Pick the form that matches your data: $a = v^{2}/r$ if you know speed, $a = r\omega^{2}$ if you know angular velocity. Both are accepted; using the wrong one after computing the wrong intermediate is a common way to lose marks. State the direction (towards the centre) when the question asks.

### Type 6: Find centripetal force given mass, speed, radius

Substitute straight into $F = mv^{2}/r$ (or $F = mr\omega^{2}$). Convert mass to kg and radius to m first. The answer is the resultant force towards the centre; if the question asks "what provides it", name the real force (friction, tension, gravity, normal contact force).

### Type 7: Maximum speed before skidding (car on a flat road)

Steps:

1. Friction provides the centripetal force, and its maximum value is $F_{\text{max}} = \mu N = \mu mg$ (normal force equals weight on a flat road).
2. Set the required centripetal force equal to the maximum friction: $\dfrac{mv^{2}}{r} = \mu mg$.
3. The mass cancels: $v_{\text{max}} = \sqrt{\mu r g}$.
4. Above this speed the required force exceeds the available friction and the car skids outward (away from the centre, along the tangent).

The same pattern appears with a string that breaks (tension limit) and a coin on a turntable (friction limit, so there is a maximum radius at fixed $\omega$ because $F = mr\omega^{2}$ grows with $r$).

### Type 8: Vertical circle at the top and bottom (bucket of water, roller coaster, ball on a string)

Steps:

1. State the forces at the position in question: at the top, weight and tension both act towards the centre; at the bottom, tension acts towards the centre and weight acts away from it.
2. Write the resultant-force equation: top $T + mg = mv^{2}/r$, bottom $T - mg = mv^{2}/r$.
3. For minimum speed at the top (string taut / contact maintained), set $T = 0$, giving $mg = mv^{2}/r$ and $v_{\text{min}} = \sqrt{gr}$.
4. If the speed is not constant, link the top and bottom speeds with energy: $\dfrac{1}{2}mv_{\text{bottom}}^{2} = \dfrac{1}{2}mv_{\text{top}}^{2} + mg(2r)$.
5. Answer "is it in contact?" questions by comparing the computed acceleration (or speed) with the critical value $g$ (or $\sqrt{gr}$).

### Type 9: Conical pendulum (tension components, angle, period)

Steps:

1. Resolve the tension: vertically $T\cos\theta = mg$, horizontally $T\sin\theta = mv^{2}/r$.
2. Divide to get $\tan\theta = v^{2}/(rg)$ (the standard "show that" result).
3. Radius from geometry: $r = L\sin\theta$.
4. Find $T$ from the vertical equation, $v$ from $\tan\theta = v^{2}/(rg)$, and the period from $T_{\text{period}} = 2\pi r/v$.
5. For "what happens if it moves faster": $\theta$ increases, because a larger centripetal force needs a larger horizontal component $T\sin\theta$.

### Type 10: Banked track or banking aircraft

Steps:

1. Resolve the normal force (or lift): horizontally $N\sin\theta = mv^{2}/r$, vertically $N\cos\theta = mg$.
2. Divide: $\tan\theta = v^{2}/(rg)$; the design speed is $v = \sqrt{rg\tan\theta}$.
3. Below design speed the vehicle slides down the slope; above it, up the slope.
4. Explain why banking helps: the horizontal component of the normal force can supply centripetal force, so the car does not depend on friction alone.

### Type 11: Fairground rotor / wall of death

The wall pushes on the rider (normal contact force $N$) providing the centripetal force $N = mr\omega^{2}$; friction between rider and wall balances the weight. For the rider not to slip: $\mu N \geq mg$, so $\mu mr\omega^{2} \geq mg$ and $\omega_{\text{min}} = \sqrt{g/(\mu r)}$. Note the mass cancels.

### Type 12: Satellite or orbit speed and period

Steps:

1. Set gravity equal to the centripetal force: $mg = mv^{2}/r$ (or the full gravitational form $GMm/r^{2} = mv^{2}/r$ if $G$ and $M$ are given).
2. $v = \sqrt{gr}$ (or $\sqrt{GM/r}$). Use $r$ measured from the centre of the planet.
3. Period: $T = 2\pi r/v$.
4. Watch the units: km to m, days to seconds (687 days $\times 24 \times 3600$ for Mars).

### Type 13: Conceptual "what happens to X" / comparison questions

Past papers ask you to compare quantities between two paths or two positions (for example a larger-radius path vs a smaller-radius path with the same friction limit). Method: write the relevant equation, note which quantities are fixed, and reason about what changes. Examples: same friction force $F$ and same mass on a larger radius means the same centripetal acceleration ($a = F/m$), a larger maximum speed ($v = \sqrt{Fr/m}$), and a longer lap time ($t = 2\pi r/v = 2\pi\sqrt{mr/F}$). In a loop, the car is slower and the centripetal acceleration smaller at the top than at the bottom.

### Type 14: MCQ style (Paper 1)

Paper 1 multiple-choice questions test the same ideas at one step: which definition is correct, the direction of the centripetal force/acceleration, what provides the centripetal force in a given situation, converting rpm to $\text{rad s}^{-1}$, and simple $v = r\omega$ or $F = mv^{2}/r$ substitutions. The same traps apply, so the methods above work: convert units first, remember the direction is always towards the centre, and eliminate options that mention an outward "centrifugal" force (the syllabus does not use it).

## 5. Solved Examples

All solutions are written in mark-scheme style: equation, substitution, answer with units. Take $g = 9.81 \ \text{m s}^{-2}$ unless stated. Examples 1-8 are coursebook-style problems; Examples 9-11 are real CAIE questions with their published mark schemes, verified directly against the question papers and mark schemes. They cover every skill this chapter is examined on.

### Example 1: Radian conversion and the clock hands (Coursebook Chapter 17)

**Question:** (a) Convert $60^{\circ}$ to radians. (b) The second hand of a clock has length 1.8 cm. Calculate its angular velocity and the speed of its tip.

**Method:**
- (a) Multiply the angle in degrees by $\pi/180$.
- (b) One revolution is $2\pi$ rad and takes 60 s, so $\omega = 2\pi/T$. Convert the length to metres ($r = 0.018$ m), then use $v = r\omega$.

**Answer:**
- (a) $60^{\circ} = 60 \times \dfrac{\pi}{180} = \dfrac{\pi}{3} = 1.05 \ \text{rad}$.
- (b) $\omega = \dfrac{2\pi}{60} = 0.105 \ \text{rad s}^{-1}$; $v = r\omega = 0.018 \times 0.105 = 1.9 \times 10^{-3} \ \text{m s}^{-1}$.

**What the examiner wants:** the angular velocity part is the classic 2-mark question "show that the angular velocity of the second hand of a clock is about 0.105 rad s$^{-1}$" - write $\omega = 2\pi/60 = 0.105$ with the substitution shown, and convert cm to m before using $v = r\omega$.

### Example 2: Washing machine drum - rpm to angular velocity to speed (Coursebook Chapter 17)

**Question:** The drum of a washing machine spins at 1200 revolutions per minute. The clothes are at a radius of 0.32 m from the axis. Calculate (a) the angular velocity of the drum, (b) the speed of the clothes.

**Method:**
- (a) Convert rpm to revolutions per second (divide by 60), then to radians per second with $\omega = 2\pi f$.
- (b) Multiply by the radius: $v = r\omega$.

**Answer:**
- (a) $f = \dfrac{1200}{60} = 20 \ \text{Hz}$, so $\omega = 2\pi f = 2\pi \times 20 = 126 \ \text{rad s}^{-1}$.
- (b) $v = r\omega = 0.32 \times 125.7 = 40 \ \text{m s}^{-1}$.

**What the examiner wants:** the rpm conversion done as two clear steps (divide by 60, then multiply by $2\pi$), and a full substitution into $v = r\omega$ with units on the answer.

### Example 3: Maximum speed before a string breaks (Coursebook Chapter 17)

**Question:** A stone of mass 0.20 kg is whirled round on the end of a string of length 30 cm. The string breaks when the tension exceeds 8.0 N. Calculate the maximum speed at which the stone can be whirled without the string breaking.

**Method:**
1. The tension provides the centripetal force.
2. At the limit, $T = mv^{2}/r$.
3. Convert 30 cm to 0.30 m, then rearrange for $v$: $v = \sqrt{Tr/m}$.

**Answer:** $v = \sqrt{\dfrac{Tr}{m}} = \sqrt{\dfrac{8.0 \times 0.30}{0.20}} = \sqrt{12} = 3.5 \ \text{m s}^{-1}$.

**What the examiner wants:** equating the tension to $mv^{2}/r$ (not to the weight), converting cm to m, and giving the answer to two significant figures to match the data.

### Example 4: Vertical circle - bucket of water (Coursebook Chapter 17)

**Question:** A teacher swings a bucket of water of total mass 5.4 kg round in a vertical circle of diameter 1.8 m. (a) Calculate the minimum speed at the top so the water stays in the bucket. (b) Assuming the speed stays constant, find the force on the teacher's hand at the bottom.

**Method:**
- (a) At the minimum speed the tension is zero and the weight alone provides the centripetal force: $mg = mv^{2}/r$. The radius is half the diameter, $r = 0.9$ m.
- (b) At the bottom the tension acts towards the centre and the weight acts away from it: $T - mg = mv^{2}/r$, so $T = m(v^{2}/r + g)$.

**Answer:**
- (a) $v = \sqrt{gr} = \sqrt{9.81 \times 0.9} = 3.0 \ \text{m s}^{-1}$.
- (b) $T = 5.4\left(\dfrac{8.83}{0.9} + 9.81\right) = 5.4 \times 19.6 = 106 \ \text{N}$.

**What the examiner wants:** using the diameter to get the radius ($r = 1.8/2 = 0.9$ m, not 1.8 m). Note: at exactly $v = \sqrt{gr}$, $v^{2}/r = g$, so the bottom tension is $2mg = 2 \times 5.4 \times 9.81 = 106$ N.

### Example 5: Conical pendulum - rubber bung (Coursebook Chapter 17)

**Question:** A rubber bung of mass 0.20 kg is swung in a horizontal circle of radius 0.40 m so that the string makes an angle of $56^{\circ}$ with the vertical. Calculate (a) the tension in the string, (b) the angular velocity of the bung, (c) the time for one complete revolution.

**Method:**
- (a) Vertically, the tension's upward component balances the weight: $T\cos\theta = mg$.
- (b) Horizontally, the inward component provides the centripetal force: $T\sin\theta = mr\omega^{2}$, so $\omega = \sqrt{T\sin\theta/(mr)}$.
- (c) The period is $T_{\text{period}} = 2\pi/\omega$.

**Answer:**
- (a) $T = \dfrac{0.20 \times 9.81}{\cos 56^{\circ}} = \dfrac{1.96}{0.559} = 3.5 \ \text{N}$.
- (b) $\omega = \sqrt{\dfrac{3.51 \times 0.829}{0.20 \times 0.40}} = \sqrt{36.4} = 6.0 \ \text{rad s}^{-1}$.
- (c) $T_{\text{period}} = \dfrac{2\pi}{6.03} = 1.0 \ \text{s}$.

**What the examiner wants:** resolving the tension into components - the vertical component balances the weight, the horizontal component provides the centripetal force. Refer to components of the tension, never components of the weight.

### Example 6: Maximum cornering speed on a flat road (Coursebook Chapter 17)

**Question:** A car of mass 1200 kg rounds a flat bend of radius 50 m. The maximum frictional force is 0.60 of the car's weight. Calculate the maximum speed at which the car can take the bend.

**Method:**
1. Friction provides the centripetal force.
2. At the limit, $mv^{2}/r = 0.60mg$.
3. The mass cancels; solve for $v$.

**Answer:** $v = \sqrt{0.60 \, r g} = \sqrt{0.60 \times 50 \times 9.81} = 17 \ \text{m s}^{-1}$.

**What the examiner wants:** noticing that the mass cancels, so the answer does not depend on the mass of the car. Above this speed the car skids outward because the required centripetal force exceeds the maximum friction.

### Example 7: Banked track (Coursebook Chapter 17)

**Question:** A bend of radius 80 m is to be taken at a speed of 25 m s$^{-1}$. Calculate the banking angle for a frictionless track.

**Method:**
1. Resolve the normal force: horizontally $N\sin\theta = mv^{2}/r$, vertically $N\cos\theta = mg$.
2. Divide the two equations to eliminate $N$: $\tan\theta = v^{2}/(rg)$.
3. Substitute and take the inverse tangent.

**Answer:** $\tan\theta = \dfrac{v^{2}}{rg} = \dfrac{25^{2}}{80 \times 9.81} = \dfrac{625}{784.8} = 0.796$, so $\theta = 38.5^{\circ} \approx 39^{\circ}$.

**What the examiner wants:** showing the division of the two resolved equations, then a full substitution with all numbers before the final angle.

### Example 8: The International Space Station (Coursebook Chapter 17)

**Question:** The ISS has mass 350 tonnes and orbits at an average height of 340 km, where the gravitational field strength is $8.8 \ \text{m s}^{-2}$. The radius of the Earth is 6400 km. Calculate (a) the centripetal force on the ISS, (b) its orbital speed, (c) the time for each orbit.

**Method:**
1. Orbital radius from the centre of the Earth: $r = 6400 + 340 = 6740$ km $= 6.74 \times 10^{6}$ m. Mass: $m = 3.5 \times 10^{5}$ kg.
- (a) Gravity provides the centripetal force: $F = mg$.
- (b) $mg = mv^{2}/r$, so $v = \sqrt{gr}$ using $g$ at the orbital radius.
- (c) $T = 2\pi r/v$.

**Answer:**
- (a) $F = mg = 3.5 \times 10^{5} \times 8.8 = 3.1 \times 10^{6} \ \text{N}$.
- (b) $v = \sqrt{gr} = \sqrt{8.8 \times 6.74 \times 10^{6}} = 7.7 \times 10^{3} \ \text{m s}^{-1}$.
- (c) $T = \dfrac{2\pi r}{v} = \dfrac{2\pi \times 6.74 \times 10^{6}}{7.70 \times 10^{3}} = 5.5 \times 10^{3} \ \text{s} \approx 92 \ \text{minutes}$.

**What the examiner wants:** the orbital radius measured from the centre of the planet (height added to the Earth's radius), and the value of $g$ at the orbital height used, not surface gravity.

### Example 9: Two cars on a circular track (9702/41/O/N/21 Q1, 7 marks)

**Question:** Two cars move around a horizontal circular track. Path X has radius 318 m; path Y is parallel to and 27 m outside path X (radius 345 m). Both cars have mass 790 kg, and the maximum lateral friction force $F$ is the same for both cars.

(a) With reference to velocity and acceleration, describe uniform circular motion. [2]

(b)(i) The maximum speed of the car on path X without sliding is 94 m s$^{-1}$. Calculate $F$. [2]

(b)(ii) Tick a table to compare, for the car on path Y, the centripetal acceleration, the maximum speed, and the time taken for one lap, against the car on path X. [3]

**Method:**
- (a) State two ideas: constant speed (constant magnitude of velocity), and acceleration always perpendicular to the velocity.
- (b)(i) Friction provides the centripetal force: $F = mv^{2}/r$. Substitute $m = 790$ kg, $v = 94$ m s$^{-1}$, $r = 318$ m.
- (b)(ii) With the same $F$ and the same $m$: $a = F/m$ is identical; $v_{\text{max}} = \sqrt{Fr/m}$ grows with $r$; the lap time $t = 2\pi r/v = 2\pi\sqrt{mr/F}$ grows with $r$.

**Answer:**
- (a) Constant speed (or constant magnitude of velocity); acceleration (always) perpendicular to the velocity.
- (b)(i) $F = \dfrac{mv^{2}}{r} = \dfrac{790 \times 94^{2}}{318} = 22\,000$ N.
- (b)(ii) Centripetal acceleration: same. Maximum speed: greater. Time taken for one lap: greater.

**What the examiner wants:** (a) B1 + B1 - both ideas are needed and an equation alone is not accepted. (b)(i) C1 for the substituted equation, A1 for the answer. (b)(ii) three B1s for the three correct table entries - this is Type 13 reasoning, tracking what is fixed ($F$, $m$) and what changes with $r$.

### Example 10: Toy car on a vertical loop (9702/42/O/N/21 Q1, 8 marks)

**Question:** An unpowered toy car of mass 230 g moves on a smooth track containing a vertical circular loop of diameter 62 cm. Resistive forces are negligible. X is at the bottom of the loop and Y at the top.

(a) State what is meant by centripetal acceleration. [1]

(b)(i) State what happens to the magnitude of the centripetal acceleration of the car as it moves around the loop from X to Y. [1]

(b)(ii) Explain, if the car remains in contact with the track, why the centripetal acceleration of the car at point Y must be greater than $9.8 \ \text{m s}^{-2}$. [2]

(c) The initial speed along the track is 3.8 m s$^{-1}$. Determine whether the car is in contact with the track at point Y. Show your working. [3]

(d) Suggest, with a reason but without calculation, whether your conclusion in (c) would be different for a car of mass 460 g moving with the same initial speed. [1]

**Method:**
- (a) Write the definition: acceleration perpendicular to velocity.
- (b)(i) The car is slower at Y than at X because it has gained gravitational potential energy, so its centripetal acceleration is smaller at Y.
- (b)(ii) The $9.8 \ \text{m s}^{-2}$ is caused by the weight alone; an acceleration greater than this needs an additional contact force from the track, which only exists while the car is in contact.
- (c) Use conservation of energy to find the speed at the top (the car rises by the diameter $h = 0.62$ m), then $a = v^{2}/r$ with $r = 0.31$ m, and compare $a$ with $g$. Alternative accepted method: the required speed for contact at the top is $v_{Y} = \sqrt{gr}$, then find the initial speed that would produce it.
- (d) Mass cancels in all the equations, so the conclusion is unchanged.

**Answer:**
- (a) Acceleration perpendicular to velocity. (Adding "towards the centre" is also fine; quoting an equation is not enough.)
- (b)(i) It decreases.
- (b)(ii) The acceleration of $9.8 \ \text{m s}^{-2}$ is caused by the weight of the car (or: the centripetal force must be greater than the weight of the car); an acceleration greater than $9.8 \ \text{m s}^{-2}$ requires a contact force from the track.
- (c) Energy: $\dfrac{1}{2}mv_{Y}^{2} = \dfrac{1}{2}mv_{X}^{2} - mgh$, so $v_{Y}^{2} = 3.8^{2} - 2 \times 9.81 \times 0.62 = 2.28$ and $v_{Y} = 1.5 \ \text{m s}^{-1}$. Then $a = \dfrac{v^{2}}{r} = \dfrac{1.5^{2}}{0.31} = 7.3 \ \text{m s}^{-2}$, which is less than $9.8 \ \text{m s}^{-2}$, so the car is **not** in contact with the track. (Alternative: contact at the top needs $v_{Y} = \sqrt{9.81 \times 0.31} = 1.74$ m s$^{-1}$, which requires $v_{X} = 3.9$ m s$^{-1}$, greater than the actual 3.8 m s$^{-1}$, so no contact.)
- (d) No - the acceleration and the conclusion are independent of mass because mass cancels in the equations.

**What the examiner wants:** (a) the exact 1-mark definition "acceleration perpendicular to velocity" (B1). (b)(i) B1. (b)(ii) B1 + B1 - both the weight idea and the contact-force idea. (c) C1 for the energy equation, A1 for $v_{Y} = 1.5$ m s$^{-1}$, C1 for $a = v^{2}/r$, then the comparison with $9.8$ decides the conclusion; the alternative $\sqrt{gr}$ method is also accepted. (d) B1 for mass cancels.

### Example 11: Steel sphere on a spring in a horizontal circle (9702/41/M/J/23 Q2, 12 marks)

**Question:** A steel sphere of mass 0.29 kg hangs in equilibrium from a vertical spring, its centre 8.5 cm from the top of the spring. The sphere is then set moving in a horizontal circle at constant speed; the distance from the centre of the sphere to the top of the spring is now 10.8 cm, and the spring's axis makes an angle of $27^{\circ}$ with the vertical.

(a) Explain, with reference to the forces acting on the sphere, why the length of the spring is now greater. [3]

(b)(i) Show that the radius of the circle is 4.9 cm. [1]

(b)(ii) Show that the tension in the spring is 3.2 N. [2]

(b)(iii) The spring obeys Hooke's law. Calculate the spring constant in $\text{N cm}^{-1}$. [2]

(c)(i) Determine the centripetal acceleration of the sphere. [2]

(c)(ii) Calculate the period of the circular motion. [2]

**Method:**
- (a) The horizontal component of the tension provides the centripetal force; the vertical component of the tension balances the weight; the combined (greater) tension means a greater extension of the spring.
- (b)(i) Radius from geometry: $r = 10.8 \sin 27^{\circ}$.
- (b)(ii) Vertically, $T\cos\theta = mg$.
- (b)(iii) Use the extra tension above equilibrium, $\Delta T = 3.2 - 0.29 \times 9.81$, and the extra extension, $\Delta x = 10.8 - 8.5$ cm; $k = \Delta T/\Delta x$.
- (c)(i) The horizontal component of the tension provides the centripetal force: $a = T\sin\theta/m$.
- (c)(ii) Use $a = r\omega^{2}$ with $\omega = 2\pi/T_{\text{period}}$, so $T_{\text{period}} = 2\pi\sqrt{r/a}$.

**Answer:**
- (a) The horizontal force on the sphere causes its centripetal acceleration; the weight of the sphere is now balanced by the vertical component of the tension (or: the horizontal and vertical components of the force combine to give a greater tension); a greater tension means a greater extension of the spring.
- (b)(i) $r = 10.8 \sin 27^{\circ} = 4.9$ cm.
- (b)(ii) $T = \dfrac{0.29 \times 9.81}{\cos 27^{\circ}} = 3.2 \ \text{N}$.
- (b)(iii) $k = \dfrac{\Delta T}{\Delta x} = \dfrac{0.36}{2.3} = 0.15 \ \text{N cm}^{-1}$.
- (c)(i) $a = \dfrac{T\sin\theta}{m} = \dfrac{3.2 \sin 27^{\circ}}{0.29} = 5.0 \ \text{m s}^{-2}$.
- (c)(ii) $T_{\text{period}} = 2\pi\sqrt{\dfrac{r}{a}} = 2\pi\sqrt{\dfrac{0.049}{5.0}} = 0.62 \ \text{s}$.

**What the examiner wants:** (a) three B1s for the three linked ideas. (b)(i) A1. (b)(ii) C1 for the vertical resolution, A1 for 3.2 N. (b)(iii) C1 for using the extra tension (3.2 - 0.29 $\times$ 9.81) and extra extension, A1 for the value - using the total tension or total length loses the method mark. (c)(i) C1 for using the horizontal component, A1. (c)(ii) C1 + A1. Note the mark scheme itself uses $T$ for the period here, which clashes with tension; in your answer, write "period $= 0.62$ s" to avoid confusion.

### Practice set from the coursebook (Cambridge International A Level Physics, Chapter 17 end-of-chapter questions)

These are the coursebook's own exam-style questions, with the mark allocations printed in the book. They are ideal practice because each one is a question type that has appeared on real papers:

1. (a) Explain what is meant by a radian. [1] (b) A body completes one revolution in 15 s. Calculate its angular velocity. [2]
2. A roller-coaster truck loops a loop of diameter 8.0 m; at the position shown there is no reaction force between the wheels and the track. (a) What provides the centripetal force? [1] (b) Calculate the speed of the truck, $g = 9.8 \ \text{m s}^{-2}$. [3]
3. A toy of mass 60 g sits on the edge of a turntable of diameter 15.0 cm making 20 revolutions per minute. (a) Describe what is meant by centripetal force. [1] (b)(i) Calculate the centripetal force on the toy. [4] (b)(ii) Explain why the toy falls off when the speed is increased. [2]
4. A metal ball of mass 50 g on a string of length 1.50 m is raised through 70 cm and released; it swings down in a circular arc. (a) Determine the speed at the bottom. [2] (b) Calculate the tension when the string is vertical. [4] (c) Explain why the tension is not equal to the weight of the ball. [2]
5. A car hits a patch of oil while going round a bend and slides off onto the grass. Explain, using circular motion, why the car came off the road. [2]
6. An aeroplane banks to make a horizontal turn at 75 m s$^{-1}$ with turning radius 80 m. (a) Draw and label the forces on the aeroplane. [2] (b) Calculate the angle the aeroplane makes with the horizontal. [4]
7. (a) Explain what is meant by angular velocity. [2] (b) A rubber bung of mass 200 g swings in a horizontal circle of radius 40 cm, the string at $56^{\circ}$ to the vertical. Calculate (i) the tension in the string, [3] (ii) the angular velocity of the bung, [2] (iii) the time for one complete revolution. [1]
8. (a) Explain what is meant by a centripetal force. [2] (b) A bucket of water of total mass 5.4 kg is swung in a vertical circle of diameter 1.8 m. (i) Calculate the minimum speed at the top so the water stays in. [3] (ii) Assuming constant speed, find the force on the hand at the bottom. [2]
9. A pilot sits in a seat on the end of a 5.0 m arm spun at high speed. (a) Describe what the pilot feels, relating it to the centripetal force. [3] (b)(i) At top speed the centripetal force equals six times the pilot's weight. Calculate the speed. [3] (b)(ii) Calculate the revolutions per minute. [2]
10. (a) Show that one revolution contains $2\pi$ radians. [2] (b) A centrifuge spins at 540 rpm with the test tube end 10 cm from the axis. (i) Calculate the angular velocity. [2] (ii) Calculate the centripetal force on a particle of mass 20 mg at the end of the tube. [2] (c) Explain, by comparing forces, why the centrifuge separates particles more effectively than letting them settle under gravity. [2]

Working through all ten, timed, is the best preparation for the Paper 4 questions this chapter produces.

## 6. Cheat Sheet

### All formulas in one block

$$\theta = \frac{s}{r}, \qquad \omega = \frac{\Delta\theta}{\Delta t}, \qquad \omega = \frac{2\pi}{T} = 2\pi f, \qquad v = r\omega$$

$$a = \frac{v^{2}}{r} = r\omega^{2} = v\omega, \qquad F = \frac{mv^{2}}{r} = mr\omega^{2}$$

Vertical circle: top $T + mg = \dfrac{mv^{2}}{r}$, bottom $T - mg = \dfrac{mv^{2}}{r}$, minimum speed at top $v_{\text{min}} = \sqrt{gr}$, energy link $v_{\text{bottom}}^{2} = v_{\text{top}}^{2} + 4gr$.

Conical pendulum / banked track: $T\cos\theta = mg$, $T\sin\theta = \dfrac{mv^{2}}{r}$, $\tan\theta = \dfrac{v^{2}}{rg}$, $r = L\sin\theta$.

Flat-road skid limit: $v_{\text{max}} = \sqrt{\mu r g}$. Orbit: $v = \sqrt{gr}$, $T = \dfrac{2\pi r}{v}$.

### Key definitions (word for word)

- **Radian**: the angle subtended at the centre of a circle by an arc equal in length to the radius.
- **Angular velocity**: rate of change of angular displacement, in $\text{rad s}^{-1}$.
- **Centripetal acceleration**: acceleration of an object moving in a circle, directed towards the centre, perpendicular to the velocity.
- **Centripetal force**: the resultant force on an object moving in a circle, directed towards the centre (perpendicular to the velocity). It is supplied by a real force: tension, friction, gravity, or a normal contact force.

### Conversions to do instantly

- degrees to radians: $\times \pi/180$
- rpm to $\text{rad s}^{-1}$: divide by 60, then $\times 2\pi$
- cm to m, g to kg: always
- orbital radius: height above surface + planet radius

### Common traps

- Forgetting to convert degrees to radians before using $\theta = \omega t$ or any angular formula.
- Mixing up $\omega$ and $f$: they differ by a factor of $2\pi$. $\omega = 2\pi f$, never $\omega = f$.
- Writing the centripetal force pointing outwards. It always points towards the centre. There is no "centrifugal force" in the 9702 syllabus.
- Answering a definition question with an equation. "Rate of change of angular displacement" earns the mark; "$\omega = \Delta\theta/\Delta t$" alone often does not.
- Saying the centripetal force "balances" the weight or is a third force. It is the resultant of the real forces.
- Using the diameter where the radius is needed (loop of diameter 62 cm has $r = 0.31$ m).
- Using surface gravity for an orbit at height; use $g$ at the orbital radius.
- Not showing the substitution in "show that" questions. Full substitution is required, including all constants.
- Premature rounding of intermediate values; carry at least one extra significant figure through your working.
- Using $T$ for both tension and period in the same solution; label one clearly (for example "period $= 0.62$ s").
- Forgetting that in uniform circular motion the speed is constant but the velocity is not: the object is accelerating and not in equilibrium.
- Saying "the centripetal force does work". It does no work because it is perpendicular to the displacement.

## 7. Common Exam Mistakes

These come from the actual CAIE Principal Examiner Reports for Teachers for the sessions where circular motion was examined.

### From the November 2021 Paper 42 report (toy car on a vertical loop)

- Definitions were too vague. Candidates defined centripetal acceleration by quoting an equation, or by using the word "centripetal" inside the definition ("the acceleration caused by the centripetal force"). The mark scheme wanted "acceleration perpendicular to velocity".
- Candidates treated the centripetal force as an extra force that has to "balance" the weight. Very few understood that the centripetal force is the **resultant of the weight and the normal contact force** from the track. This was the single most damaging misunderstanding on the paper.
- Many candidates did not appreciate that the car moves more slowly at the top of the loop (Y) than at the bottom (X), so its centripetal acceleration is smaller at Y than at X.
- Many candidates thought a greater mass means a greater centripetal acceleration. Mass cancels in $mg = mv^{2}/r$, so the acceleration and the conclusion are independent of mass.
- In the "is the car in contact" calculation, candidates knew $a = v^{2}/r$ but did not apply conservation of energy to find the speed at the top of the loop first.

### On the Paper 41-style track comparison (same friction limit, different radius)

No examiner report exists for the November 2021 Paper 41 session (too few candidates), so treat this as a weak spot to train, not a quoted examiner complaint. The comparison table in the two-cars question requires three careful steps: with the same maximum friction force $F$ and the same mass, the centripetal acceleration is the same ($a = F/m$); the maximum speed is greater on the larger radius ($v_{\text{max}} = \sqrt{Fr/m}$); and the lap time is also greater ($t = 2\pi r/v = 2\pi\sqrt{mr/F}$). Getting "same / greater / greater" right requires tracking what is fixed and what changes, which is exactly the reasoning candidates found hard.

### From the May/June 2023 Paper 41 report (steel sphere on a spring, horizontal circle)

- Candidates did not refer to the components of the tension. Many referred to components of the weight, or treated the centripetal force as a third force acting on the sphere rather than the resultant of the tension and the weight.
- Some candidates thought the sphere was oscillating from side to side like a pendulum instead of moving in horizontal circles. Failing to see the tension components at the start led to wrong numerical methods later.
- In the "show that" question, candidates did not show their working clearly enough: a numerical value for the weight appeared without the evidence that it came from mass times gravitational field strength.
- In the spring-constant part, candidates used the total tension (3.2 N) instead of the extra tension above equilibrium ($3.2 - 0.29 \times 9.81$), and the total length instead of the extra extension.
- In the period calculation, candidates tried circular-motion equations where $F = ma$ with the horizontal component of the tension was the required first step, then found the equations worked once the acceleration was known.

### General warnings that apply to this chapter (from the same reports)

- Use technical language accurately; "centripetal" is an adjective describing a direction, not the name of a force.
- Show your reasoning line by line. Correct working with a wrong final answer can earn method marks; an unsupported number cannot.
- Match the significant figures of the data, and do not round intermediate values prematurely.
- Read the question: answers to a question that was not asked (often recycled from memorised mark schemes) get no credit.
- Definitions need to be dimensionally and conceptually complete; "per unit time", "towards the centre" and "resultant force" are the phrases the mark schemes look for.

---

Sources used: CAIE 9702 syllabus for 2022-2024 (official syllabus document), the Cambridge International A Level Physics coursebook Chapter 17 (the source chapter), CAIE question papers and published mark schemes for 9702/41/O/N/21, 9702/42/O/N/21 and 9702/41/M/J/23, the Principal Examiner Reports for November 2021 and June 2023, and TheLucidSTEM Paper 4 practice set for Topic 12.

---

# Chapter 18: Gravitational Fields - CAIE A Level Physics (9702) Study Notes

## 2. Definition Sheet

Learn these word-for-word. Definitions open almost every Paper 4 question on this topic (1-2 marks each), and the mark schemes credit exact phrases: "force per unit mass", "work done per unit mass", "from infinity". A missing phrase such as "per unit mass" or "point masses" costs the mark.

### 2.1 Gravitational field

> A gravitational field is a region of space around a mass in which any other mass experiences a force of attraction. It is an example of a field of force.

- It exists in the space around a mass whether or not anything is there to feel it.
- The force is always attractive, and there is no way to shield against it.

### 2.2 Gravitational field strength

> The gravitational field strength at a point is the force per unit mass on a small object (test mass) placed at that point.

- Mark-scheme wording: **"force per unit mass"** is the exact phrase the examiner wants (9702/41/M/J/21 Q1(a)).
- Units: N kg$^{-1}$ (the same as m s$^{-2}$).
- It is a vector: it points towards the mass creating the field.
- Do not confuse it with gravitational potential - in 9702/s21 many candidates answered "define gravitational field strength" with the definition of gravitational potential. Field strength = **force** per unit mass; potential = **work done** per unit mass.

### 2.3 Gravitational potential

> The gravitational potential at a point is the work done per unit mass in bringing a mass from infinity to the point.

- Two B1 marks (9702/41/O/N/21 Q2(a), 9702/42/F/M/20 Q1(a)):
  1. **"work done per unit mass"**
  2. **"in moving a mass from infinity (to the point)"**
- $\phi = 0$ at infinity, and everywhere else $\phi < 0$ (always negative).
- It is a scalar - potentials from several masses simply add.
- Units: J kg$^{-1}$.
- Warning (9702/w21): "work done in moving a mass" without making clear it is *per unit mass* does not get the mark.

### 2.4 Gravitational potential energy

> The gravitational potential energy of a mass at a point is the work done in bringing the mass from infinity to that point.

- Equivalently, $E_P = m\phi$, where $\phi$ is the gravitational potential at the point.
- Zero at infinity, always negative everywhere else ($E_P = -\frac{GMm}{r}$); the more negative, the more tightly bound the mass.
- Units: J.
- Do not confuse potential energy with potential: potential energy = potential $\times$ mass, and they have different units (J vs J kg$^{-1}$).

### 2.5 Equipotential surface

> An equipotential surface is a surface on which the gravitational potential is the same (constant) at every point.

- No work is done moving a mass along an equipotential surface, because the potential energy does not change.
- Equipotential surfaces are perpendicular to the field lines at every point.
- Around a point mass they are concentric spheres; near the Earth's surface they are horizontal planes.

### 2.6 Escape velocity (escape speed)

> The escape velocity is the minimum speed a body needs, at a given point, to escape the gravitational field completely - to reach infinity with zero kinetic energy left over.

- $v = \sqrt{\frac{2GM}{R}}$ - it does not depend on the mass of the escaping body.
- It is not a separate syllabus line, but it is examined (e.g. 9702/41/O/N/13 Q1).

### 2.7 Geostationary orbit

> A geostationary orbit is an orbit in which the satellite remains above a fixed point on the Earth's surface: the orbital period is 24 hours, the orbit is directly above the Equator, and the satellite orbits from west to east.

The four features (2 marks, 9702/41/O/N/19 Q1(b)(i)):

1. Period **24 hours** (equal to the Earth's rotational period).
2. **Directly above the Equator**.
3. **From west to east** (same direction as the Earth's rotation).
4. Stays above the same point on the Earth's surface.

The examiner complains when candidates just rephrase feature 4 ("above the same point") instead of giving features 1-3.

### 2.8 Line of gravitational force (field line)

> A line of gravitational force is a line whose direction at every point gives the direction of the gravitational force on a mass placed at that point.

- The arrows point towards the mass creating the field.
- The spacing of the lines shows the field strength: closer lines = stronger field, more spread out lines = weaker field.
- Radial fields (around a point mass or sphere) have lines diverging from the centre; uniform fields (small region near the surface) have parallel, equally spaced lines.

### 2.9 Newton's law of gravitation (2-mark statement - learn it exactly)

> Any two point masses attract each other with a force that is directly proportional to the product of their masses and inversely proportional to the square of their separation.

- Mark scheme (9702/41/O/N/19 Q1(a), 9702/41/M/J/18 Q1(a)): one mark for the proportionality ideas, one mark for **"point masses"**.
- Omitting "point masses" was the most common omission in otherwise well-answered questions (9702/w19) - do not forget it.

---

## 3. Formula Sheet

| Formula | Meaning of symbols | SI units | When to use it |
|---|---|---|---|
| $$F = \frac{GMm}{r^2}$$ | $F$ = gravitational force, $G = 6.67 \times 10^{-11}$ N m$^2$ kg$^{-2}$, $M$, $m$ = masses, $r$ = centre-to-centre separation | N, kg, m | Force of attraction between two point masses / uniform spheres |
| $$g = \frac{F}{m}$$ | $g$ = field strength, $F$ = force on mass $m$ | N kg$^{-1}$ (= m s$^{-2}$) | Definition of gravitational field strength |
| $$g = \frac{GM}{r^2}$$ | $M$ = mass creating the field, $r$ = distance from its centre | N kg$^{-1}$ | Field strength due to a point/spherical mass, at or above the surface |
| $$\phi = -\frac{GM}{r}$$ | $\phi$ = gravitational potential, $M$ = mass, $r$ = distance from centre | J kg$^{-1}$ | Potential at a point in the field of one mass |
| $$E_P = m\phi = -\frac{GMm}{r}$$ | $E_P$ = gravitational potential energy of mass $m$ | J | Potential energy of a mass in a field; always negative |
| $$\Delta E_P = GMm\left(\frac{1}{r_1} - \frac{1}{r_2}\right)$$ | $r_1$, $r_2$ = initial and final distances from centre | J | Work done moving a mass between two radii (use $r_1 < r_2$ for lifting) |
| $$v = \sqrt{\frac{GM}{r}}$$ | $v$ = orbital speed, $M$ = central mass, $r$ = orbital radius | m s$^{-1}$ | Speed of a satellite/planet in a circular orbit |
| $$v = \frac{2\pi r}{T}$$ | $T$ = orbital period | m s$^{-1}$ | Speed from period and radius (circumference / time) |
| $$T^2 = \frac{4\pi^2 r^3}{GM}$$ | $T$ = orbital period | s | Kepler's third law; period from orbital radius |
| $$r^3 = \frac{GMT^2}{4\pi^2}$$ | $r$ = orbital radius | m | Orbital radius from period (geostationary orbit problems) |
| $$v_{\text{esc}} = \sqrt{\frac{2GM}{R}}$$ | $v_{\text{esc}}$ = escape speed, $R$ = radius at launch point | m s$^{-1}$ | Minimum speed to escape a gravitational field |
| $$g = -\frac{d\phi}{dr}$$ | potential gradient | N kg$^{-1}$ | Field strength from a $\phi$-$r$ graph; relationship between $g$ and $\phi$ |
| $$\frac{g_h}{g_0} = \left(\frac{R}{R+h}\right)^2$$ | $g_0$ = surface value, $g_h$ = value at height $h$ | dimensionless | Ratio questions: field strength at height vs surface |
| $$\rho = \frac{M}{\frac{4}{3}\pi R^3}$$ | $\rho$ = mean density, $M$ = mass, $R$ = radius | kg m$^{-3}$ | Finding planet density from $g$ and $R$ |
| $$\Delta E_P = mg\Delta h$$ | near-surface approximation, $\Delta h$ = height change | J | Only when $g$ is essentially constant (small heights) |

Supporting equations from Chapter 17 (circular motion) that you must be ready to combine:

- Centripetal force: $F = \frac{mv^2}{r} = mr\omega^2$
- Angular speed: $\omega = \frac{2\pi}{T}$

Constants and data you should recognise (given in questions):

- $G = 6.67 \times 10^{-11}$ N m$^2$ kg$^{-2}$
- Earth: mass $M = 6.0 \times 10^{24}$ kg, radius $R = 6.4 \times 10^6$ m, surface $g = 9.81$ N kg$^{-1}$
- Moon: mass $7.35 \times 10^{22}$ kg, radius $1.74 \times 10^6$ m
- Geostationary orbit: $T = 86400$ s, $r = 4.23 \times 10^7$ m from Earth's centre

---

## 4. Methods (Question Types & Methods)

Cambridge can ask about gravitational fields in the following ways. For each, here is the step-by-step method that gets full marks.

### Type 1: State Newton's law of gravitation (2 marks)

Write: "The force between two point masses is directly proportional to the product of their masses and inversely proportional to the square of their separation." The mark scheme (9702/41/O/N/19, 9702/41/M/J/18) awards one mark for the proportionality ideas and one mark for the idea that it applies to point masses. **Do not forget "point masses"** - the examiner report notes this was the most common omission.

### Type 2: Define gravitational field strength (1-2 marks)

"Force per unit mass" - and if there is room, "the gravitational force exerted per unit mass on a small object placed at that point." The mark scheme (9702/41/M/J/21) wants exactly "force per unit mass". Do not write a definition of gravitational potential instead - this was a common error in 9702/s21.

### Type 3: Define gravitational potential (2 marks)

Two B1 marks (9702/41/O/N/21, 9702/42/F/M/20):
1. "work done per unit mass"
2. "(work done in) moving a mass from infinity (to the point)"

The examiner specifically warns (9702/w21): saying "work done in moving a mass" without making clear it is *per unit mass* does not get the mark.

### Type 4: Calculate the gravitational force between two masses

Method:
1. Convert everything to SI (g to kg, mm/cm/km to m).
2. Substitute into $F = \frac{GMm}{r^2}$.
3. Quote the answer with units (N).

Example shape (coursebook Q1): two 100 g objects 1.0 cm apart: $F = \frac{6.67 \times 10^{-11} \times 0.1 \times 0.1}{(0.01)^2} = 6.7 \times 10^{-9}$ N.

### Type 5: Find $g$ at the surface or at a height above a planet

Method:
1. Identify the distance $r$ **from the centre**: at the surface $r = R$; at height $h$, $r = R + h$. This is where most marks are lost.
2. Substitute into $g = \frac{GM}{r^2}$.
3. Give units N kg$^{-1}$ (or m s$^{-2}$).

If the question gives density $\rho$ and diameter instead of mass, first find $M = \rho \times \frac{4}{3}\pi R^3$, then $g = \frac{GM}{R^2}$ (coursebook end-of-chapter Q4 does exactly this).

### Type 6: Find gravitational potential at a point

Method:
1. Use $r$ from the centre of the mass.
2. $\phi = -\frac{GM}{r}$. The minus sign is essential - potential is always negative.
3. Units: J kg$^{-1}$.
4. If there are **two or more masses**, add the potentials as scalars: $\phi = \phi_1 + \phi_2 = -\frac{GM_1}{r_1} - \frac{GM_2}{r_2}$. Both terms are negative, so the answer is more negative than either alone (9702/41/O/N/21 Q2(b)(iii) - many candidates subtracted instead of adding).

### Type 7: Work done / change in potential energy moving a mass

Method (matches the 9702/41/M/J/21 and 9702/42/F/M/20 mark schemes):
1. Write $\Delta E_P = GMm\left(\frac{1}{r_1} - \frac{1}{r_2}\right)$ where $r_1$ is the starting radius and $r_2$ the final radius.
2. Substitute $G$, $M$, $m$, $r_1$, $r_2$.
3. The sign tells you the direction: positive means energy was put in (moved further out), negative means energy was released (moved inward).
4. Never write $\frac{1}{r_2 - r_1}$ instead of $\frac{1}{r_1} - \frac{1}{r_2}$ - a flagged error in the 9702/s19 examiner report.
5. To go from potential to potential energy: multiply the potential by the mass: $E_P = m\phi$.

### Type 8: Escape velocity / energy to escape

Method:
1. Energy to escape per unit mass $= \frac{GM}{R}$ (the magnitude of the surface potential) - or $-\phi$ at the launch point.
2. Equate kinetic energy to potential energy: $\frac{1}{2}mv^2 = \frac{GMm}{R}$, cancel $m$, solve $v = \sqrt{\frac{2GM}{R}}$.
3. In a "show that" question, show the substitution for the potential energy first, then the energy equality (9702/41/O/N/13 Q1: show $\Delta E_P = 1.27 \times 10^7$ J for a 4.5 kg rock on the Moon, then $v = 2.4 \times 10^3$ m s$^{-1}$).

### Type 9: Orbital speed of a satellite or planet

Method (matches 9702/41/M/J/21 Q1(b) and coursebook Worked Example 3):
1. State the physics: gravitational force provides the centripetal force: $\frac{GMm}{r^2} = \frac{mv^2}{r}$.
2. Cancel $m$: $v^2 = \frac{GM}{r}$.
3. If you are given the period instead of the speed, use $v = \frac{2\pi r}{T}$.
4. Take the square root at the end - do not forget this (coursebook hint; also a source of slips).
5. Convert minutes to seconds if the period is given in minutes.

### Type 10: Orbital radius from period (including geostationary radius)

Method (matches 9702/42/F/M/20 Q1(b)(i) and 9702/41/O/N/19 Q1(b)(ii)):
1. State: gravitational force provides the centripetal force.
2. Use $\frac{GMm}{r^2} = mr\omega^2$ with $\omega = \frac{2\pi}{T}$, giving $r^3 = \frac{GMT^2}{4\pi^2}$.
3. Substitute $T$ in seconds ($24$ h $= 86400$ s; $94$ min $= 5640$ s).
4. Cube root at the end.
5. For a geostationary question, also convert the final radius to a height: height $= r - R$ where $R = 6.4 \times 10^6$ m.

### Type 11: Show $T^2 \propto r^3$ or find the constant $k$ in $r^3 = kT^2$

Method (matches 9702/41/M/J/18 Q1):
1. Equate $\frac{GMm}{r^2}$ to $\frac{mv^2}{r}$ (or $mr\omega^2$).
2. Substitute $v = \frac{2\pi r}{T}$ (or $\omega = \frac{2\pi}{T}$).
3. Rearrange to $r^3 = \frac{GM}{4\pi^2}T^2$, so $k = \frac{GM}{4\pi^2}$.
4. To find $M$: calculate $k$ from data ($k = \frac{R^3}{T^2}$ for one or more planets), then $M = \frac{4\pi^2 k}{G}$. Using several data points and showing they agree earns an extra mark (the 9702/41/M/J/18 mark scheme gives a B1 for using two or three values).

### Type 12: Ratio questions ($g$ at surface vs $g$ in orbit)

Method (matches 9702/42/F/M/20 Q1(b)(iii)):
1. Write $g = \frac{GM}{r^2}$ for both locations.
2. $G$ and $M$ cancel, so the ratio is $\left(\frac{r_{\text{orbit}}}{r_{\text{surface}}}\right)^2$ (note the inversion - the larger radius gives the smaller $g$).
3. Example: $\left(\frac{2.4 \times 10^8}{6.4 \times 10^6}\right)^2 = 1400$, so the surface field is 1400 times stronger.

### Type 13: Point of zero resultant field between two masses

Method (matches 9702/41/O/N/21 Q2(b)):
1. Explain (2 marks): the fields from the two masses act in **opposite directions** at points between them; the resultant is zero where the two field strengths are **equal in magnitude**. "The fields cancel out" alone is not enough - say equal magnitude, opposite direction.
2. Let $x$ = distance from one mass, so distance from the other is $(d - x)$ where $d$ = separation.
3. Set $\frac{GM_1}{x^2} = \frac{GM_2}{(d-x)^2}$.
4. Cancel $G$, take square roots of both sides (much easier than expanding into a quadratic): $\frac{\sqrt{M_1}}{x} = \frac{\sqrt{M_2}}{d-x}$, then solve for $x$.
5. The zero-field point is closer to the **smaller** mass (its weaker field needs less distance to fall to match).
6. Check: at that same point the potential is *not* zero - it is the most negative (maximum magnitude) point on the line.

### Type 14: Potential at a point due to two masses

Method (matches 9702/41/O/N/21 Q2(b)(iii)):
1. Find the distance of the point from each mass.
2. $\phi = -\frac{GM_1}{r_1} - \frac{GM_2}{r_2}$ - add the two (both negative) values.
3. Units J kg$^{-1}$. Do not subtract the magnitudes; potential is scalar.

### Type 15: $g = -d\phi/dr$ and $\phi$-$r$ graph questions

Method (matches 9702/42/O/N/21 Q2):
1. State: field strength equals the (negative of the) potential gradient: $g = -\frac{d\phi}{dr}$.
2. On a $\phi$-$r$ graph, $g$ is found from the gradient of the curve (steep curve = strong field, flat curve = weak field).
3. At a maximum of $\phi$, gradient is zero so $g = 0$: the zero-field point is at the maximum of the potential, not where $\phi = 0$.
4. When sketching $g$ vs $x$ between two masses: $g$ is negative near one mass and positive near the other, crossing zero at the point of maximum potential.
5. Comparing two planets: the more massive planet has a deeper potential well (more negative $\phi$ at the surface) and a steeper potential gradient (larger $g$) at its surface.

### Type 16: Sketching field lines / comparing fields

Method (coursebook end-of-chapter Q3, Q9):
1. Radial field: arrows point towards the centre; lines spread out with distance; more closely spaced lines = stronger field.
2. Uniform field (building scale): parallel, equally spaced, all pointing the same way.
3. Sketching $\phi$ vs $r$ for a planet of mass $2M$: same radius, curve twice as deep at the surface ($-\frac{2GM}{R}$ vs $-\frac{GM}{R}$).
4. For a planet of the same mass but radius $2R$: shallower well at the surface ($-\frac{GM}{2R}$), curve extends to larger $r$.
5. The least energy to escape comes from the shallowest well (smallest $\frac{GM}{R}$).

---

## 5. Solved Examples

All solutions are written the way the mark scheme wants: physics statement first, then equation, substitution, answer with units. The past paper questions are real, verified Paper 4 questions (question codes given so you can find the originals), with mark allocations from the published mark schemes.

### Example 1: Gravitational force between a satellite and the Earth (coursebook Q1(c))

**Question:** A satellite of mass $1.4 \times 10^4$ kg orbits the Earth at a distance of $6.8 \times 10^6$ m from the Earth's centre. The mass of the Earth is $6.0 \times 10^{24}$ kg. Calculate the gravitational force on the satellite.

**Method:**
1. State Newton's law of gravitation: $F = \frac{GMm}{r^2}$.
2. Substitute $G = 6.67 \times 10^{-11}$, $M = 6.0 \times 10^{24}$ kg, $m = 1.4 \times 10^4$ kg, $r = 6.8 \times 10^6$ m (from the centre).
3. Quote the answer with units (N).

**Answer:**

$$F = \frac{6.67 \times 10^{-11} \times 6.0 \times 10^{24} \times 1.4 \times 10^4}{(6.8 \times 10^6)^2} = \frac{5.60 \times 10^{18}}{4.62 \times 10^{13}} = 1.2 \times 10^5 \text{ N}$$

The satellite experiences a gravitational force of about $1.2 \times 10^5$ N towards the Earth's centre.

**What the examiner wants:** the correct substitution into $F = \frac{GMm}{r^2}$ with $r$ measured from the Earth's centre, and the answer quoted in N.

### Example 2: $g$ at the surface of the Moon and at a height above the Earth (coursebook Q4(a)(i))

**Question:** (a) The Moon has mass $7.4 \times 10^{22}$ kg and radius $1.74 \times 10^6$ m. Calculate the gravitational field strength at the Moon's surface. (b) Calculate the gravitational field strength at a height of 300 km above the Earth's surface. (Earth: $M = 6.0 \times 10^{24}$ kg, $R = 6.4 \times 10^6$ m.)

**Method:**
1. Use $g = \frac{GM}{r^2}$ with $r$ = distance from the centre.
2. For (a), $r = R$ = the Moon's radius.
3. For (b), convert 300 km to metres and add the Earth's radius: $r = R + h$. This is the step where marks are lost.

**Answer:**

$$g = \frac{GM}{r^2} = \frac{6.67 \times 10^{-11} \times 7.4 \times 10^{22}}{(1.74 \times 10^6)^2} = 1.63 \text{ N kg}^{-1}$$

$$r = R + h = 6.4 \times 10^6 + 3.0 \times 10^5 = 6.7 \times 10^6 \text{ m}$$

$$g = \frac{GM}{r^2} = \frac{6.67 \times 10^{-11} \times 6.0 \times 10^{24}}{(6.7 \times 10^6)^2} = 8.9 \text{ N kg}^{-1}$$

(Compare $9.81$ N kg$^{-1}$ at the surface - the field has dropped by about 9% at 300 km.)

**What the examiner wants:** $r = R + h$ for a height above the surface (never use the height alone), and units N kg$^{-1}$ (or m s$^{-2}$).

### Example 3: Mass and density of the Earth from surface $g$ (coursebook Worked Example 1)

**Question:** The Earth has radius $6.4 \times 10^6$ m and surface field strength $9.81$ N kg$^{-1}$. Determine the mass of the Earth and its mean density.

**Method:**
1. Rearrange $g = \frac{GM}{R^2}$ for $M = \frac{gR^2}{G}$.
2. Find the density from $\rho = \frac{M}{\frac{4}{3}\pi R^3}$.

**Answer:**

$$M = \frac{9.81 \times (6.4 \times 10^6)^2}{6.67 \times 10^{-11}} = 6.0 \times 10^{24} \text{ kg}$$

$$\rho = \frac{M}{\frac{4}{3}\pi R^3} = \frac{6.0 \times 10^{24}}{\frac{4}{3}\pi (6.4 \times 10^6)^3} = 5500 \text{ kg m}^{-3}$$

**What the examiner wants:** rearranging $g = \frac{GM}{R^2}$ correctly and using the full sphere volume $\frac{4}{3}\pi R^3$ - a common slip is using $R^3$ instead of the volume formula, or forgetting to cube the radius.

### Example 4: Gravitational potential and potential energy of a spacecraft (coursebook Worked Example 2)

**Question:** A planet has diameter $6.8 \times 10^6$ m and mass $4.9 \times 10^{23}$ kg. A rock of mass 200 kg, initially at rest and far from the planet, falls and hits the surface. Calculate the change in the rock's potential energy and its impact speed.

**Method:**
1. Radius $r = \frac{6.8 \times 10^6}{2} = 3.4 \times 10^6$ m (diameter, not radius - halve it).
2. Far away, $E_P = 0$, so the change in potential energy is $\Delta E_P = 0 - \left(-\frac{GMm}{r}\right) = \frac{GMm}{r}$.
3. All of this becomes kinetic energy (no atmosphere): $\frac{1}{2}mv^2 = \Delta E_P$.

**Answer:**

$$\Delta E_P = \frac{6.67 \times 10^{-11} \times 4.9 \times 10^{23} \times 200}{3.4 \times 10^6} = 1.9 \times 10^9 \text{ J}$$

$$\frac{1}{2}mv^2 = 1.9 \times 10^9$$

$$v = \sqrt{\frac{2 \times 1.9 \times 10^9}{200}} = 4.4 \times 10^3 \text{ m s}^{-1}$$

**What the examiner wants:** the impact speed does not depend on the rock's mass - $m$ cancels from $\frac{1}{2}mv^2 = \frac{GMm}{r}$. Also, halve the diameter to get the radius before substituting.

### Example 5: Satellite moved to a higher orbit (9702/41/M/J/21 Q1, 10 marks)

**Question:** The Earth is an isolated uniform sphere of mass $6.0 \times 10^{24}$ kg. A satellite of mass 1200 kg is in a circular orbit with period 94 minutes. (a) Define gravitational field strength. (b) Calculate the radius of the orbit. (c)(i) Show that in a new orbit of period 150 minutes the radius is $9.4 \times 10^6$ m. (c)(ii) State, with a reason, whether the gravitational potential energy increases or decreases. (c)(iii) Determine the magnitude of the change in potential energy.

**Method:**
- (a) Write "force per unit mass" and nothing else.
- (b) State the physics: gravitational force provides the centripetal force, $\frac{GMm}{r^2} = mr\omega^2$ with $\omega = \frac{2\pi}{T}$, giving $r^3 = \frac{GMT^2}{4\pi^2}$. Convert 94 minutes to seconds ($94 \times 60 = 5640$ s) and substitute. Cube root at the end.
- (c)(i) Use $T^2 \propto r^3$: $\frac{r_2^3}{r_1^3} = \left(\frac{T_2}{T_1}\right)^2$, so $r_2 = r_1 \left(\frac{150}{94}\right)^{2/3}$. Show every step - "show that" questions need full working.
- (c)(ii) The satellite moves further from the Earth, so its potential energy increases (becomes less negative, since $E_P = -\frac{GMm}{r}$ and $r$ increases).
- (c)(iii) $\Delta E_P = GMm\left(\frac{1}{r_1} - \frac{1}{r_2}\right)$ with $r_1 = 6.9 \times 10^6$ m and $r_2 = 9.4 \times 10^6$ m.

**Answer:**
- (a) Gravitational field strength is the force per unit mass.
- (b) $r = 6.9 \times 10^6$ m.
- (c)(i) $r_2 = 9.4 \times 10^6$ m (shown).
- (c)(ii) It increases, because the separation from the Earth's centre increases.
- (c)(iii) $\Delta E_P = 1.9 \times 10^{10}$ J. Full-mark working:

$$\Delta E_P = GMm\left(\frac{1}{r_1} - \frac{1}{r_2}\right) = 6.67 \times 10^{-11} \times 6.0 \times 10^{24} \times 1200 \times \left(\frac{1}{6.9 \times 10^6} - \frac{1}{9.4 \times 10^6}\right) = 1.9 \times 10^{10} \text{ J}$$

**What the examiner wants:** (a) "force per unit mass" (B1). (b) $\frac{GMm}{r^2} = mr\omega^2$ with $\omega = \frac{2\pi}{T}$ (C1), substitution (C1), $r = 6.9 \times 10^6$ m (A1). (c)(i) ratio $r^3/T^2$ constant (C1) with clear working (A1) - unclear presentation caused confusion between $r^3$ and $r$ in 9702/s21. (c)(ii) increases because separation increases (B1). (c)(iii) formula (C1), substitution (C1), $1.9 \times 10^{10}$ J (A1).

### Example 6: Orbital speed and period of the Moon (coursebook Worked Example 3)

**Question:** The Moon orbits the Earth at an average distance of $3.84 \times 10^8$ m from the Earth's centre. The mass of the Earth is $6.0 \times 10^{24}$ kg. Calculate the Moon's orbital speed and its orbital period.

**Method:**
1. State: gravitational force provides the centripetal force, so $v^2 = \frac{GM}{r}$.
2. Take the square root to find $v$.
3. Use $T = \frac{2\pi r}{v}$ for the period, and convert seconds to days.

**Answer:**

$$v^2 = \frac{GM}{r} = \frac{6.67 \times 10^{-11} \times 6.0 \times 10^{24}}{3.84 \times 10^8} = 1.04 \times 10^6$$

$$v = 1.0 \times 10^3 \text{ m s}^{-1}$$

$$T = \frac{2\pi r}{v} = \frac{2\pi \times 3.84 \times 10^8}{1.0 \times 10^3} = 2.4 \times 10^6 \text{ s} \approx 27.8 \text{ days}$$

**What the examiner wants:** the orbital speed is independent of the satellite's mass (it cancels), and the square root must actually be taken.

### Example 7: Geostationary orbit radius (coursebook worked calculation)

**Question:** Calculate the radius and the height above the Earth's surface of a geostationary orbit. ($T = 24$ h $= 86400$ s, Earth $M = 6.0 \times 10^{24}$ kg, $R = 6.4 \times 10^6$ m.)

**Method:**
1. Use $r^3 = \frac{GMT^2}{4\pi^2}$ with $T$ in seconds.
2. Cube root to find $r$.
3. Subtract the Earth's radius to get the height above the surface: height $= r - R$.

**Answer:**

$$r^3 = \frac{6.67 \times 10^{-11} \times 6.0 \times 10^{24} \times (86400)^2}{4\pi^2} = 7.66 \times 10^{22} \text{ m}^3$$

$$r = 4.23 \times 10^7 \text{ m} = 42\,300 \text{ km from the Earth's centre}$$

$$\text{height above surface} = r - R = 4.23 \times 10^7 - 6.4 \times 10^6 = 3.6 \times 10^7 \text{ m} \approx 36\,000 \text{ km}$$

**What the examiner wants:** $T$ in seconds (86400 s, not 24), the cube root taken, and the final height found by subtracting the Earth's radius from the orbital radius.

### Example 8: Escape speed from the Moon (9702/41/O/N/13 Q1, 7 marks)

**Question:** The Moon may be considered as an isolated sphere of radius $1.74 \times 10^6$ m with mass $7.35 \times 10^{22}$ kg. A rock of mass 4.50 kg sits on the Moon's surface. (a) Define gravitational potential at a point. (b)(i) Show that the change in gravitational potential energy of the rock in moving it from the surface to infinity is $1.27 \times 10^7$ J. (b)(ii) Determine the escape speed, explaining your working. (c) State and explain whether the minimum speed for the rock to reach the Earth differs from the escape speed.

**Method:**
- (a) Write: "the work done per unit mass in bringing a mass from infinity to the point" (two B1 ideas: work done per unit mass; from infinity).
- (b)(i) Moving to infinity means $r_2 \to \infty$, so $\frac{1}{r_2} \to 0$ and $\Delta E_P = \frac{GMm}{R}$. Show the substitution.
- (b)(ii) Equate kinetic energy to the potential energy change: $\frac{1}{2}mv^2 = \Delta E_P$, and solve for $v$. State that the change in gravitational potential energy equals the change in kinetic energy.
- (c) The Earth attracts the rock, so the potential at the Earth's position is not zero - the rock does not need enough energy to reach infinity.

**Answer:**
- (b)(i) $\Delta E_P = \frac{6.67 \times 10^{-11} \times 7.35 \times 10^{22} \times 4.5}{1.74 \times 10^6} = 1.27 \times 10^7$ J.
- (b)(ii) $v = \sqrt{\frac{2 \times 1.27 \times 10^7}{4.5}} = 2.4 \times 10^3$ m s$^{-1}$ (equivalently $v = \sqrt{\frac{2GM}{R}} = 2.4 \times 10^3$ m s$^{-1}$).
- (c) The minimum speed to reach the Earth is **less** than the escape speed, because the Earth's gravitational field attracts the rock.

**What the examiner wants:** (a) "work done per unit mass" + "from infinity" (2 B1s). (b)(i) $\Delta E_P = GMm/R$ with the substitution shown (1 mark - a "show that" question, so write every step). (b)(ii) change in g.p.e. equals change in kinetic energy (B1), $\frac{1}{2}mv^2 = 1.27 \times 10^7$ giving $v = 2.4 \times 10^3$ m s$^{-1}$ (A1). (c) lower, because the Earth attracts the rock / the potential at the Earth is not zero (M1 + A1).

### Example 9: Zero field point between the Earth and the Moon, and the potential there (9702/41/O/N/21 Q2, 9 marks)

**Question:** The Earth (mass $5.98 \times 10^{24}$ kg) and the Moon (mass $7.35 \times 10^{22}$ kg) are separated by $3.84 \times 10^8$ m. Point P is on the line joining their centres, at distance $x$ from the Earth's centre, where the resultant field is zero. (a) Define gravitational potential. (b)(i) Explain how the field strength can be zero despite two large masses nearby. (b)(ii) Show $x \approx 3.5 \times 10^8$ m. (b)(iii) Calculate the gravitational potential at P.

**Method:**
- (a) Write: "work done per unit mass" + "in moving a mass from infinity (to the point)".
- (b)(i) The fields from the two masses act in opposite directions; the resultant is zero where the two field strengths are equal in magnitude. Say both ideas - "the fields cancel" alone is not credited.
- (b)(ii) Set $\frac{GM_E}{x^2} = \frac{GM_M}{(3.84 \times 10^8 - x)^2}$. Cancel $G$ and take square roots of both sides (much easier than expanding the quadratic): $\frac{\sqrt{M_E}}{x} = \frac{\sqrt{M_M}}{3.84 \times 10^8 - x}$, then solve for $x$.
- (b)(iii) Potential is scalar - add the two (both negative) contributions: $\phi = -\frac{GM_E}{x} - \frac{GM_M}{3.84 \times 10^8 - x}$.

**Answer:**
- (b)(ii) $x = 3.5 \times 10^8$ m.
- (b)(iii) $\phi = -6.67 \times 10^{-11}\left(\frac{5.98 \times 10^{24}}{3.5 \times 10^8} + \frac{7.35 \times 10^{22}}{3.4 \times 10^7}\right) = -1.3 \times 10^6$ J kg$^{-1}$.

**What the examiner wants:** (a) "work done per unit mass" (B1) + "from infinity" (B1). (b)(i) opposite directions (B1) + equal magnitudes (B1) - the examiner report says saying the fields "cancel" without equal magnitude and opposite direction was not credited, and answers in terms of forces gained nothing (the question was about field strength). (b)(ii) equate the two field strengths (C1), solve to $x = 3.5 \times 10^8$ m (A1). (b)(iii) $\phi_E$ term (C1), $\phi_M$ term (C1), $\phi = -1.3 \times 10^6$ J kg$^{-1}$ (A1) - add the two negative contributions; potential is scalar. Note: the potential is *not* zero at P even though the field is zero - it is at its most negative value on the line.

### Example 10: TESS satellite - orbit radius, potential energy change, field ratio (9702/42/F/M/20 Q1, 10 marks)

**Question:** TESS is a satellite in a circular orbit about the Earth (mass $6.0 \times 10^{24}$ kg, radius $6.4 \times 10^6$ m). (a) Define gravitational potential at a point. (b)(i) TESS orbits in 13.7 days. Show that its orbital radius is $2.4 \times 10^8$ m. (b)(ii) Calculate the change in potential energy between TESS in orbit and TESS on the launch pad. (b)(iii) Calculate the ratio $\frac{\text{field strength at the Earth's surface}}{\text{field strength at TESS's orbit}}$.

**Method:**
- (a) Write: "work done per unit mass" + "from infinity".
- (b)(i) State gravitational force provides the centripetal force; use $r^3 = \frac{GMT^2}{4\pi^2}$ with $T$ in seconds. This is a "show that" question - write every step, including $T = 13.7 \times 24 \times 3600$ s.
- (b)(ii) $\Delta E_P = GMm\left(\frac{1}{r_1} - \frac{1}{r_2}\right)$ with $r_1 = 6.4 \times 10^6$ m (surface) and $r_2 = 2.4 \times 10^8$ m (orbit).
- (b)(iii) $G$ and $M$ cancel in the ratio: $\frac{g_{\text{surface}}}{g_{\text{orbit}}} = \left(\frac{r_{\text{orbit}}}{r_{\text{surface}}}\right)^2$ (note the inversion - larger radius, smaller $g$).

**Answer:**
- (b)(i) $r = 2.4 \times 10^8$ m (shown).
- (b)(ii) $\Delta E_P = 2.2 \times 10^{10}$ J.
- (b)(iii) $\frac{g_{\text{surface}}}{g_{\text{orbit}}} = \left(\frac{2.4 \times 10^8}{6.4 \times 10^6}\right)^2 = 1400$ - the surface field strength is 1400 times greater.

**What the examiner wants:** (a) as in Example 9(a). (b)(i) gravitational force provides centripetal force (C1), $r^3 = GMT^2/4\pi^2$ with $T$ in seconds (C1), substitution (A1). (b)(ii) $E_P = -GMm/r$ (C1), $\Delta E_P = GMm(1/r_1 - 1/r_2)$ (C1), $2.2 \times 10^{10}$ J (A1). (b)(iii) $g = GM/r^2$ (C1), ratio $= 1400$ (A1).

### Example 11: Geostationary satellite and the mass of the Earth (9702/41/O/N/19 Q1, 8 marks)

**Question:** (a) State Newton's law of gravitation. (b)(i) A geostationary satellite orbits the Earth with period 24 hours. State two features of its orbit (other than the period). (b)(ii) Given that the orbital radius is $4.23 \times 10^4$ km, determine the mass of the Earth, explaining your working.

**Method:**
- (a) Write: force directly proportional to the product of the masses and inversely proportional to the square of their separation + between point masses.
- (b)(i) State: directly above the Equator; from west to east. Do not just rephrase "geostationary".
- (b)(ii) Start from a principle: the gravitational force provides the centripetal force. Use $\frac{GM}{r^2} = r\left(\frac{2\pi}{T}\right)^2$ and solve for $M$. Convert km to m first, and square the period and cube the radius.

**Answer:**
- (b)(i) Directly above the Equator; from west to east.
- (b)(ii) $M = \frac{4\pi^2 r^3}{GT^2} = 6.0 \times 10^{24}$ kg.

**What the examiner wants:** (a) proportionality ideas (B1) + point masses (B1). (b)(i) above the Equator (B1) + west to east (B1) - the examiner report notes weak candidates repeated what "geostationary" means instead of giving these features. (b)(ii) gravitational force provides the centripetal force (B1), $\frac{GM}{r^2} = r(2\pi/T)^2$ (C1), substitution (C1), $M = 6.0 \times 10^{24}$ kg (A1). The examiner report flags: forgetting to square the period or cube the radius, power-of-ten errors from not converting km to m, and a significant number of candidates wrongly assumed $g = 9.81$ N kg$^{-1}$ at the satellite's height - never do that.

### Example 12: Planets orbiting a distant star - Kepler's third law (9702/41/M/J/18 Q1)

**Question:** (a) State Newton's law of gravitation. (b)(i) Explain whether planets in circular orbits at constant speed are in equilibrium. (b)(ii)1 Show that $R^3 = kT^2$ has $k = GM/4\pi^2$. (b)(ii)2 Use data for three planets to calculate the star's mass.

**Method:**
- (a) As in Example 11(a).
- (b)(i) They are not in equilibrium, because the direction of motion (velocity) is changing, so there is an acceleration and a resultant force.
- (b)(ii)1 Equate $\frac{GMm}{R^2} = \frac{mv^2}{R}$, substitute $v = \frac{2\pi R}{T}$, and rearrange to $R^3 = \frac{GM}{4\pi^2}T^2$ - convincing algebra earns the marks.
- (b)(ii)2 Calculate $k = \frac{R^3}{T^2}$ from the data for one planet (use several planets and show they agree for the extra mark), then $M = \frac{4\pi^2 k}{G}$.

**Answer:**
- (b)(i) Not in equilibrium - the velocity changes / the direction of motion changes / there is an acceleration / a resultant force.
- (b)(ii)1 $k = \frac{GM}{4\pi^2}$ (shown).
- (b)(ii)2 $k = 3.5(5) \times 10^{21}$, so $M = \frac{4\pi^2 k}{G} = 2.1 \times 10^{33}$ kg.

**What the examiner wants:** (b)(i) 1 mark for any one of: velocity changes, direction changes, acceleration, resultant force. (b)(ii)1 equate gravitational and centripetal force (C1), use $v = 2\pi R/T$ (M1), convincing algebra (A1). (b)(ii)2 calculate $R^3/T^2$ for one planet (C1), $3.5(5) \times 10^{21} = GM/4\pi^2$ (A1), $M = 2.1 \times 10^{33}$ kg; a further B1 for using two or three values in a valid way.

### Example 13: Measuring $G$ with a torsion balance (9702/42/M/J/19 Q1, 7 marks)

**Question:** Two point masses $M$ and $m$ are separated by distance $x$ in a vacuum. (a) State an expression for the force $F$ between them, and name any other symbol used. (b) A small sphere is deflected by a nearby large sphere; the deflection angle is $1.2 \times 10^{-3}$ rad per $8.0 \times 10^{-2}$ m of scale, and the torsion constant is $9.3 \times 10^{-10}$ N m rad$^{-1}$. Calculate the deflection angle and the torque. (c)(i) Use the torque to determine a value for $G$ (spheres: masses $1.3$ kg and $7.5 \times 10^{-3}$ kg, centre separation $6.0 \times 10^{-2}$ m, lever arm $8.0 \times 10^{-2}$ m). (c)(ii) Suggest one reason the result may differ from the accepted value.

**Method:**
- (a) $F = \frac{GMm}{x^2}$, where $G$ is the (universal) gravitational constant. Name $G$ - candidates who did not lost the mark.
- (b) angle $= \frac{\text{scale reading}}{\text{scale length}}$; torque $= \text{angle} \times \text{torsion constant}$.
- (c)(i) Set the torque due to the gravitational force equal to the restoring torque: $F \times \text{lever arm} = \text{torque}$, with $F = \frac{G \times 1.3 \times 7.5 \times 10^{-3}}{(6.0 \times 10^{-2})^2}$, and solve for $G$.
- (c)(ii) Quote one reason from the list: the law applies only to point masses / sphere radii not small compared with separation / spheres may not be uniform / masses not isolated / force between L and the rod / electrostatic forces between spheres.

**Answer:**
- (a) $F = \frac{GMm}{x^2}$, $G$ = gravitational constant.
- (b) angle $= \frac{1.2 \times 10^{-3}}{8.0 \times 10^{-2}} = 1.5 \times 10^{-2}$ rad; torque $= 1.5 \times 10^{-2} \times 9.3 \times 10^{-10} = 1.4 \times 10^{-11}$ N m.
- (c)(i) $G = 6.4 \times 10^{-11}$ N m$^2$ kg$^{-2}$.

**What the examiner wants:** (a) 1 mark - many candidates forgot to name $G$, or called $x$ the "radius" instead of the separation. (b) 2 marks for the two calculations. (c)(i) $F \times 8.0 \times 10^{-2} = 1.4 \times 10^{-11}$ (C1), full substitution (C1), $G = 6.4 \times 10^{-11}$ N m$^2$ kg$^{-2}$ (A1). (c)(ii) 1 mark for any one valid reason (e.g. spheres not point masses / not isolated / electrostatic forces).

### Example 14: Relationship between $\phi$ and $g$, potential graphs (9702/42/O/N/21 Q2)

**Question:** (a) State the relationship between gravitational potential and gravitational field strength. (b) A moon (mass $M$, radius $R$) orbits a planet (mass $3M$, radius $2R$). A graph of $\phi$ against $x$ between them is given. Explain why the potential is negative. Compare the potential at the surfaces of the planet and the moon. Sketch $g$ against $x$.

**Method:**
- (a) State: field strength equals the potential gradient, with a reference to the minus sign: $g = -\frac{d\phi}{dr}$.
- (b) Negative potential: potential is zero at infinity, the force is attractive, so a mass moving in from infinity loses potential energy (three separate ideas, three B1s).
- (b) Comparison: the potential at the planet's surface is more negative (deeper well); the potential gradient is steeper at the planet's surface; the maximum potential is nearer the moon (any two for B2).
- (b) Sketch of $g$ against $x$: starts with decreasing gradient magnitude at $2R$, finishes with increasing gradient at $D - R$; $g = 0$ at the point of maximum potential; negative near one sphere, positive near the other (three B1s).

**Answer:**
- (a) $g = -\frac{d\phi}{dr}$ - field strength equals (negative of) the potential gradient.
- (b) The potential is negative because it is zero at infinity and the force is attractive, so energy is lost moving in from infinity. The planet's well is deeper and steeper; $g$ crosses zero at the point of maximum potential.

**What the examiner wants:** (a) field strength equals potential gradient (M1) + reference to the minus sign (A1). (b) three separate B1s for why potential is negative; any two of the three comparison points for B2; three B1s for the sketch (zero at the maximum of $\phi$, not where $\phi = 0$).

**Pattern to notice**: definitions (1-2 marks) open the question; then one "show that" orbital calculation (2-3 marks); then a potential-energy change or potential calculation (3 marks); occasionally a graph sketch. Total 8-10 marks, always on Paper 4.

---

## 6. Cheat Sheet

### All formulas in one block

- Newton's law: $$F = \frac{GMm}{r^2}$$ (attractive, between point masses, $r$ = centre-to-centre)
- Field strength: $$g = \frac{F}{m} = \frac{GM}{r^2}$$ (vector, towards the mass, units N kg$^{-1}$ = m s$^{-2}$)
- Potential: $$\phi = -\frac{GM}{r}$$ (scalar, always negative, units J kg$^{-1}$)
- Potential energy: $$E_P = m\phi = -\frac{GMm}{r}$$ (always negative; zero at infinity)
- Change in PE between radii: $$\Delta E_P = GMm\left(\frac{1}{r_1} - \frac{1}{r_2}\right)$$
- Field from potential: $$g = -\frac{d\phi}{dr}$$
- Orbital speed: $$v = \sqrt{\frac{GM}{r}}$$ (independent of satellite mass)
- Speed from period: $$v = \frac{2\pi r}{T}$$
- Kepler III / period: $$T^2 = \frac{4\pi^2 r^3}{GM}, \qquad r^3 = \frac{GMT^2}{4\pi^2}$$
- Escape speed: $$v_{\text{esc}} = \sqrt{\frac{2GM}{R}}$$
- Ratio trick: $$\frac{g_h}{g_0} = \left(\frac{R}{R+h}\right)^2$$
- Near the surface only: $$\Delta E_P = mg\Delta h$$

### Key definitions (word-for-word)

- **Gravitational field strength**: the gravitational force exerted per unit mass on a small object placed at that point.
- **Gravitational potential**: the work done per unit mass in bringing a mass from infinity to the point.
- **Newton's law of gravitation**: any two point masses attract each other with a force directly proportional to the product of their masses and inversely proportional to the square of their separation.
- **Geostationary orbit**: period 24 h, directly above the Equator, west to east, stays above a fixed point.
- **Escape speed**: the minimum speed needed for a body to escape a gravitational field (reach infinity) with no kinetic energy left.

### Constants to recognise

- $G = 6.67 \times 10^{-11}$ N m$^2$ kg$^{-2}$
- Earth: $M = 6.0 \times 10^{24}$ kg, $R = 6.4 \times 10^6$ m, $g = 9.81$ N kg$^{-1}$
- Geostationary: $T = 86400$ s, $r = 4.23 \times 10^7$ m from centre ($\approx 36\,000$ km above surface)
- Moon: $M = 7.35 \times 10^{22}$ kg, $R = 1.74 \times 10^6$ m, surface $g \approx 1.6$ N kg$^{-1}$

### Common traps (see Section 7 for the full list)

1. Using height above the surface instead of distance from the centre in $GM/r^2$ and $-GM/r$.
2. Forgetting the minus sign in $\phi = -GM/r$ and $E_P = -GMm/r$.
3. Forgetting that negative potential energy *increases* when $r$ increases.
4. Writing $\frac{1}{r_2 - r_1}$ instead of $\frac{1}{r_1} - \frac{1}{r_2}$.
5. Treating potential as a vector (subtracting) instead of a scalar (adding).
6. Forgetting to convert minutes to seconds for $T$, or km to m for $r$.
7. Assuming $g = 9.81$ N kg$^{-1}$ at a satellite's height - use $GM/r^2$ with the orbital radius.
8. Not taking the square root when finding $v$ from $v^2$.
9. Saying fields "cancel" without "equal magnitude, opposite direction".
10. Confusing gravitational field strength (force per unit mass) with gravitational potential (energy per unit mass).

---

## 7. Common Exam Mistakes

Compiled from the CAIE 9702 Principal Examiner Reports for Teachers (June 2021, Nov 2021, Nov 2019, June 2019).

### Definitions

- **Giving the wrong definition entirely**: the most common incorrect answer to "define gravitational field strength" (9702/s21 Q1(a)) was the definition of gravitational potential. Learn the two side by side: field strength = *force per unit mass*; potential = *work done per unit mass*.
- **Omitting "per unit mass"**: in Nov 2021, saying "work done in moving a mass" did not get the mark because it does not convey the division by mass. The ratio must be explicit: work done divided by mass.
- **Omitting "point masses"** when stating Newton's law (9702/w19 Q1(a)) - the most common omission in an otherwise well-answered question.
- **Not naming symbols**: in 9702/s19 Q1(a), candidates who wrote $F = GMm/x^2$ often failed to state that $G$ is the gravitational constant. Also, $x$ is the *separation* of the masses, not a "radius".

### Calculations

- **Using the height instead of the radius**: in 9702/s19, "a small but significant number of candidates used the height above the surface of the planet and forgot to add the radius." Also in 9702/w19 Q1(b)(ii), a small but significant number assumed $g = 9.81$ N kg$^{-1}$ at the satellite - the field strength is not the surface value up there.
- **Unit conversions**: forgetting to convert minutes to seconds (9702/s21 Q1(b)), km to m (9702/w19 - "power-of-ten errors due to forgetting to convert the radius from km into m"), and cm to m (9702/s19).
- **Squaring/cubing errors**: forgetting to square the period or cube the radius in geostationary calculations (9702/w19). Confusing $r^3$ with $r$ in "show that" working (9702/s21).
- **The $\frac{1}{r_2 - r_1}$ error**: candidates treated $\frac{1}{r_2 - r_1}$ as the same as $\frac{1}{r_1} - \frac{1}{r_2}$ when finding changes in potential energy (9702/s19). They are not the same.
- **Change in potential vs change in potential energy**: in 9702/s21 Q1(c)(iii), the most common mistake was calculating the change in *potential* ($\Delta\phi$) rather than the change in *potential energy* ($\Delta E_P = m\Delta\phi$). Read which quantity the question asks for.
- **Sign of the change in potential energy**: many candidates in 9702/s21 knew $E_P = -GMm/r$ but did not realise that, because it is negative, the energy *increases* as $r$ increases. The answer "separation and energy are inversely proportional" ignores the minus sign.

### Explanations and concepts

- **"Cancelling fields" is not enough** (9702/w21 Q2(b)(i)): to explain a zero resultant field you must say the fields are equal in magnitude and opposite in direction. The word "cancelling" alone was not credited. Also, candidates who answered in terms of *forces* gained nothing - the question was about field strength.
- **Potential is scalar**: in 9702/w21 Q2(b)(iii), many candidates calculated the potential due to the Earth only; of those who used both, many subtracted the negative values instead of adding them. Potentials always add.
- **Taking square roots beats expanding quadratics**: for zero-field point problems, square-rooting both sides of $\frac{M_1}{x^2} = \frac{M_2}{(d-x)^2}$ is much cleaner than expanding; several candidates got lost in the quadratic (9702/w21).
- **Confusing potential with potential energy** (9702/s19): candidates wrote "gravitational potential" when the question was about the potential energy of a spacecraft. They are different quantities with different units.
- **Vague energy arguments**: in 9702/s19, candidates applied conservation of energy with one energy type increasing while the other decreased, without checking the context. Use the physics: potential energy decreases as a body approaches a planet (it becomes more negative).
- **Repeating the question**: in 9702/w19 Q1(b)(i), weak candidates just rephrased what "geostationary" means ("above the same point on the Earth") instead of stating the orbit features: above the Equator, west to east, period 24 hours.
- **Not explaining working in "determine" questions**: in 9702/w19 Q1(b)(ii) the question explicitly said "explain your working"; candidates who jumped straight to numbers lost the method mark. Start from a principle: "the gravitational force provides the centripetal force."
- **"Show that" presentation**: in 9702/s21 Q1(c)(i), unclear presentation caused confusion between $r^3$ and $r$. In "show that" questions you must show every step, including constants like $G$ and the full substitution.

### General advice from the examiners

- Convert to standard SI units *before* starting calculations.
- State the physical principle you are using before substituting numbers.
- In multi-part calculations, if you get a value in (i), use it in (ii) - error carried forward (ECF) marks are usually available, but only if your working is visible.
- Definitions must be ratios: "per unit mass" must be explicit, not implied.
- Descriptive questions are harder than calculations: use the correct technical terms and avoid ambiguity.

---

*Sources: CAIE 9702 syllabus (2022-2024); Cambridge International AS & A Level Physics coursebook (Chapter 18); CAIE published question papers, mark schemes and Principal Examiner Reports for Teachers for 9702/41 and 9702/42, May/June 2018, 2019, 2021; Oct/Nov 2013, 2019, 2021; Feb/March 2020.*

---

# Chapter 19: Oscillations - CAIE A Level Physics (9702) Study Notes

## 2. Definition Sheet

Learn every definition below word-perfect. The ones with a mark-scheme quote attached are the exact phrasing Cambridge awards marks for - both halves are needed.

**Oscillation:** a repeated back-and-forth motion about an equilibrium position.

**Displacement $x$ (m):** the distance of the oscillator from its equilibrium position at an instant. It is a vector: one side is taken as positive, the other negative.

**Amplitude $x_0$ (m):** the maximum displacement from the equilibrium position. It is always positive.

**Period $T$ (s):** the time for one complete oscillation (one full cycle).

**Frequency $f$ (Hz):** the number of complete oscillations per unit time.

**Angular frequency $\omega$ (rad s$^{-1}$):** the rate of change of phase. One complete cycle corresponds to a phase change of $2\pi$ rad, so $\omega = 2\pi f = \frac{2\pi}{T}$.

**Simple harmonic motion (SHM):**

> A body executes simple harmonic motion if its acceleration is directly proportional to its displacement from its equilibrium position, and is always directed towards that equilibrium position (in the opposite direction to the displacement).

Mark-scheme split: (1) "acceleration proportional to displacement" and (2) "directed towards the fixed point" / "acceleration and displacement in opposite directions". **Both ideas are required for full marks** (9702/42/M/J/18 Q4(a)). Do not write "the force is proportional to displacement" - the definition is about acceleration.

**Phase difference:** how far out of step two oscillations are, measured as a fraction of an oscillation, or in degrees, or in radians. In phase = phase difference 0 (corresponding points at the same time); in antiphase = half an oscillation ($180^\circ$, $\pi$ rad).

**Damping:** the removal of energy from an oscillating system by resistive forces. Mark-scheme phrasing: the oscillator "loses energy" (1) "due to resistive forces" (1) (9702/42/F/M/21 Q9(c)).

- **Light damping:** many oscillations; amplitude decays gradually (exponentially); period essentially unchanged.
- **Critical damping:** the minimum damping needed to return to equilibrium **without oscillating**, in the shortest possible time.
- **Heavy damping:** a slow return to equilibrium without oscillating, taking longer than critical damping.

**Free oscillation:** oscillation of a system on its own after an initial disturbance, at its natural frequency, with no external periodic force acting once released.

**Forced oscillation:** oscillation driven by an external periodic force, so the system oscillates at the driving frequency of that force (not its natural frequency).

**Natural frequency:** the frequency at which a system oscillates when it is free (after a disturbance, with no driving force).

**Resonance:**

> Oscillation of a system at maximum amplitude when the driving frequency is equal to the natural frequency of the system.

Mark-scheme split: (1) "oscillation (of object) at maximum amplitude" and (2) "when driving frequency = natural frequency (of system)" (9702/43/M/J/24 Q4(a)). At resonance the system absorbs the greatest possible energy from the driver.

---

## 3. Formula Sheet

| Formula | Meaning of symbols | SI units | When to use |
|---|---|---|---|
| $f = \dfrac{1}{T}$ | $f$ frequency, $T$ period | Hz, s | Converting between frequency and period |
| $\omega = 2\pi f = \dfrac{2\pi}{T}$ | $\omega$ angular frequency | rad s$^{-1}$ | Getting $\omega$ from $f$ or $T$ (needed for all SHM equations) |
| $x = x_0 \sin \omega t$ | $x$ displacement at time $t$, $x_0$ amplitude | m, s, rad s$^{-1}$ | Displacement when motion starts at equilibrium ($x = 0$ at $t = 0$) |
| $x = x_0 \cos \omega t$ | as above | m, s, rad s$^{-1}$ | Displacement when motion starts at max displacement ($x = x_0$ at $t = 0$) |
| $x = x_0 \sin(\omega t + \phi)$ | $\phi$ phase constant (where in the cycle $t = 0$ is taken) | m, s, rad s$^{-1}$ | General form when the motion starts part-way through the cycle |
| $a = -\omega^2 x$ | $a$ acceleration, $x$ displacement | m s$^{-2}$, m | The defining equation of SHM; acceleration at any displacement |
| $v = v_0 \cos \omega t$ | $v$ velocity, $v_0$ max velocity | m s$^{-1}$ | Velocity as a function of time (starts at max velocity) |
| $v = \pm \omega \sqrt{x_0^2 - x^2}$ | as above | m s$^{-1}$ | Velocity at a given displacement $x$ (no time needed) |
| $v_0 = \omega x_0$ | $v_0$ max speed | m s$^{-1}$ | Maximum speed (at equilibrium) |
| $a_{\max} = \omega^2 x_0$ | $a_{\max}$ max acceleration | m s$^{-2}$ | Maximum acceleration (at extremes); then $F_{\max} = ma_{\max}$ |
| $E = \frac{1}{2} m \omega^2 x_0^2$ | $E$ total energy, $m$ mass | J, kg | Total energy of SHM (syllabus formula) |
| $E_K = \frac{1}{2} m \omega^2 (x_0^2 - x^2)$ | $E_K$ kinetic energy | J | KE at a given displacement |
| $E_P = \frac{1}{2} m \omega^2 x^2$ | $E_P$ potential energy | J | PE at a given displacement |
| $T = 2\pi \sqrt{\dfrac{m}{k}}$ | $m$ mass on spring, $k$ spring constant | s, kg, N m$^{-1}$ | Period of a mass-spring system (not in the data booklet) |
| $T = 2\pi \sqrt{\dfrac{l}{g}}$ | $l$ pendulum length, $g$ gravitational field strength | s, m, m s$^{-2}$ | Period of a simple pendulum, small angles (not in the data booklet) |
| phase diff $= \dfrac{t}{T} \times 360^\circ$ or $\times 2\pi$ | $t$ time gap between corresponding points, $T$ period | rad or degrees | Phase difference between two oscillations from graphs |
| $E \propto x_0^2$ | energy vs amplitude | - | Comparing energies when amplitude changes |

**Data booklet check:** the booklet gives you only $a = -\omega^2 x$, $v = v_0 \cos \omega t$ and $v = \pm \omega \sqrt{x_0^2 - x^2}$. Everything else in this table must be recalled or derived.

---

## 4. Methods (Question Types & Methods)

### Type 1: "State the conditions for / define simple harmonic motion" (2 marks)

Method:

1. Write: "the acceleration is directly proportional to the displacement from the equilibrium position".
2. Add the direction: "and is directed towards the equilibrium position" OR "acceleration and displacement are in opposite directions".

That is the whole mark scheme. If asked for "two conditions", one mark is the proportionality, the other is the direction. Do not write "the force is proportional to displacement" without mentioning acceleration, and do not write "the acceleration is constant" (it is not).

### Type 2: "State the significance of the minus sign in $a = -\omega^2 x$" (1 mark)

Answer: "acceleration and displacement are in opposite directions" (acceleration is always directed towards the equilibrium position).

### Type 3: "Use the expression $a = -(\text{constant})x$ to explain why the motion is SHM" (2 marks)

Method:

1. Point out that everything multiplying $x$ (e.g. $\frac{c}{ML^3}$ or $\frac{A\rho g}{M}$) is constant, so $a \propto x$ (acceleration is proportional to displacement).
2. Point out that the minus sign shows the acceleration is in the opposite direction to the displacement (directed towards the equilibrium position).

### Type 4: "State and justify whether X undergoes SHM" (1 - 2 marks each)

Method: test the three requirements. Is there a restoring force? Is it proportional to displacement and directed towards equilibrium? If any requirement fails, it is not SHM. Examples from the coursebook: a basketball being bounced (not SHM: between bounces it is in free fall with constant acceleration; during contact the forces are impulsive, not proportional to displacement); a guitar string (SHM for small vibrations: the restoring force is proportional to displacement); a pendulum (SHM for small angles only); a person on a trampoline (not SHM: their feet lose contact, so there is no restoring force proportional to displacement for part of the cycle).

### Type 5: "Calculate the displacement at a given time" (2 - 3 marks)

Method:

1. Choose sine or cosine from the starting condition (equilibrium at $t = 0$: sine; released from max displacement at $t = 0$: cosine).
2. Find $\omega$ from $f$ or $T$: $\omega = 2\pi f = \frac{2\pi}{T}$.
3. Substitute into $x = x_0 \sin \omega t$ with the calculator **in radian mode**. Check the sign of the answer: negative means the other side of equilibrium.

### Type 6: "Write down an equation for the displacement" (2 marks)

Method: give $x = x_0 \sin \omega t$ (or cosine) with the numbers inserted: $x_0$ in metres and $\omega$ in rad s$^{-1}$. E.g. for $x_0 = 4.0$ cm and $T = 1.0$ s: $x = 0.040 \sin(2\pi t)$. Keep $t$ as a symbol.

### Type 7: "Find the maximum velocity / maximum acceleration" (1 - 2 marks each)

Method:

1. Read $x_0$ (and $T$ or $f$) from the question or graph.
2. $\omega = 2\pi f = \frac{2\pi}{T}$.
3. $v_{\max} = \omega x_0$; $a_{\max} = \omega^2 x_0$. Give units (m s$^{-1}$, m s$^{-2}$).

Then the maximum force is $F_{\max} = m a_{\max}$ (used in piston questions: force on the piston to produce the max acceleration).

### Type 8: "Find the velocity at a given displacement" (1 - 2 marks)

Method: use $v = \pm \omega \sqrt{x_0^2 - x^2}$. Substitute $x_0$, $\omega$ and $x$ (all in metres). The speed is the magnitude; state direction only if asked. At $x = 0$ this reduces to $v = \omega x_0$.

### Type 9: "Determine period, frequency, angular frequency from a graph" (1 - 3 marks)

Method:

1. Period: time between two adjacent identical points (peak to peak, or crossing to crossing in the same direction).
2. Frequency: $f = 1/T$; angular frequency: $\omega = 2\pi f$.
3. If the graph shows acceleration against displacement, the gradient is $-\omega^2$, so $\omega = \sqrt{|\text{gradient}|}$.
4. If the graph shows several oscillations, count them: $T = \frac{\text{total time}}{\text{number of oscillations}}$.

### Type 10: "Phase difference between two oscillations" (2 - 3 marks)

Method:

1. Measure the time $t$ between two corresponding points (both peaks, or both zero crossings in the same direction).
2. $\text{phase difference} = \frac{t}{T}$ of an oscillation.
3. Convert: $\times 360^\circ$ for degrees, $\times 2\pi$ for radians. Give both if asked.

Also know these by heart: velocity leads displacement by $\frac{1}{4}$ cycle ($90^\circ$, $\frac{\pi}{2}$ rad); acceleration is $\frac{1}{2}$ cycle ($180^\circ$, $\pi$ rad) out of phase with displacement; graphs that are mirror images about the time axis (like $x$ and $a$) are $\pi$ rad apart.

### Type 11: "Sketch graphs" (1 - 2 marks each)

Method:

- $x$-$t$, $v$-$t$, $a$-$t$ for SHM: three sinusoids of the same period; $v$ is a cosine if $x$ is a sine, $a$ is an inverted sine. Label peaks with the correct values ($x_0$, $v_0 = \omega x_0$, $\omega^2 x_0$) and one period on the time axis.
- Energy-time: KE and PE sinusoids at twice the frequency of the displacement, total = horizontal line at $E$.
- Energy-displacement: parabolas, PE max at $\pm x_0$, KE max at 0.
- Damped oscillations: sine curve shrinking inside an exponential envelope; for critical/heavy damping, a smooth curve decaying to zero with no crossing.
- Resonance curve: amplitude vs driving frequency, peak at $f_0$; a second curve on the same axes showing heavier damping = lower, broader peak.

### Type 12: "Energy calculations" (2 - 3 marks)

Method:

1. Total energy: $E = \frac{1}{2} m \omega^2 x_0^2$ (need $m$, $\omega$, $x_0$).
2. KE at displacement $x$: $E_K = \frac{1}{2} m \omega^2 (x_0^2 - x^2)$, or $\frac{1}{2} m v^2$ with $v = \omega \sqrt{x_0^2 - x^2}$.
3. PE at displacement $x$: $E_P = E - E_K = \frac{1}{2} m \omega^2 x^2$.
4. From a $v$-$t$ graph: $v_{\max}$ is the peak; $E_{K,\max} = \frac{1}{2} m v_{\max}^2$; for an undamped oscillator max PE = max KE = total energy; $a_{\max}$ is the peak of the $a$-$t$ graph or $\omega v_{\max}$; $F_{\max} = m a_{\max}$.

Energy ratio shortcut: since $E \propto x_0^2$, halving the amplitude quarters the total energy. Since $E_K = E(1 - x^2/x_0^2)$, at $x = x_0/2$ the oscillator has $\frac{3}{4}$ of its energy as KE and $\frac{1}{4}$ as PE.

### Type 13: "Force, spring constant, period chains" (4 - 6 marks)

The real exam pattern (e.g. 9702/42/F/M/21 Q4):

1. Resultant force on a trolley between two springs at release: extension of each spring = (equilibrium length - natural length) $\pm$ displacement; $F = k \times$ extension for each; the resultant is the difference (or sum, depending on geometry). Show your substitution clearly.
2. Maximum acceleration: $a = F/m$.
3. Period: use $a = -\omega^2 x$ with the values just found: $\omega = \sqrt{a/x_0}$, then $T = 2\pi/\omega$. (Or use $T = 2\pi\sqrt{m/k_{\text{eff}}}$.)
4. Effect of changing amplitude: state that the force and the displacement are both halved, so $a/x$ is unchanged and **the period is unchanged** (period independent of amplitude).

### Type 14: "Damping questions" (2 - 4 marks)

Method:

- Identify the type from a graph: many oscillations with slowly decreasing amplitude = light damping; a single fast return to zero without overshoot = critical; a slow return without oscillation = heavy.
- Explain the amplitude decrease: the oscillator **loses energy** **due to resistive forces** (air resistance, friction, eddy currents).
- For a metal sheet in a magnetic field: the sheet cuts flux, an emf is induced, eddy currents flow, the currents cause a resistive force / dissipate energy (this is the 9702/42/F/M/21 Q9(c) answer).
- Sketch the damped $x$-$t$ graph (exponential envelope) or compare two damped curves (more damping = envelope shrinks faster).

### Type 15: "Resonance questions" (2 - 4 marks)

Method:

- Define resonance: oscillation at maximum amplitude when the driving frequency equals the natural frequency.
- Explain a resonance situation: identify the oscillator and the driver; state that energy is transferred from the driver to the system most efficiently when $f_{\text{driving}} = f_{\text{natural}}$; amplitude grows because energy is added each cycle.
- Sketch/compare resonance curves: damping lowers the peak, broadens it, and shifts it slightly to lower frequency.
- Examples: name the oscillating system AND what forces it (e.g. swing + child: driver is the person pushing; Millennium Bridge: driver is the pedestrians; microwave oven: driver is the microwaves, resonating system is water molecules; MRI: driver is the radio waves, resonating system is the protons).

### Type 16: "Experiment to determine $g$ using a pendulum" (method questions, Paper 3/4/5 style)

Method:

1. Measure the length $l$ from the point of suspension to the centre of the bob with a metre rule (to the nearest mm).
2. Displace the bob through a small angle (less than $10^\circ$) and release it so it swings in a single vertical plane.
3. Time 20 complete oscillations with a stopwatch; $T = \frac{\text{total time}}{20}$. Repeat and average for reliability.
4. Vary $l$ over a wide range, repeat the timing for each length.
5. Plot $T^2$ against $l$: gradient $= \frac{4\pi^2}{g}$, so $g = \frac{4\pi^2}{\text{gradient}}$.

Sources of error and improvements (from the June 2024 examiner report, which criticised exactly these):

- Parallax error judging the extremes of the swing: use a fiducial marker (e.g. a pointer) at the equilibrium position and time the passage through it.
- Difficult to judge the end of a complete oscillation: time many oscillations (20) and divide.
- Oscillation not in a single plane (swings in an ellipse): ensure a small initial displacement and release along a straight line.
- Not accounting for the mass of the bob / putty: include it in $m$ if the experiment involves mass.
- Two sets of data are not enough for a valid conclusion: take a range of lengths and plot a graph.
- Improvements: video camera with a timer in frame, view frame by frame; take more readings and plot a graph.

---

## 5. Solved Examples

All paper-code examples below are real CAIE questions whose wording and mark schemes were verified from the published papers. Mark allocations and full-mark answers are taken from the published mark schemes.

### Example 1: Phase difference from graphs (coursebook Worked example 1 pattern, 3 marks)

**Question:** Two identical oscillators have graphs that are out of step by $t = 17$ ms; the period of each is $T = 60$ ms. Find the phase difference as a fraction, in degrees and in radians.

**Method:**

1. Phase difference = time gap between corresponding points divided by the period: $\frac{t}{T}$.
2. Convert the fraction to degrees ($\times 360^\circ$) and to radians ($\times 2\pi$).

**Answer:**

$$\text{phase difference} = \frac{t}{T} = \frac{17}{60} = 0.283 \text{ of an oscillation}$$

$$\text{in degrees: } 0.283 \times 360^\circ = 102^\circ \approx 100^\circ$$

$$\text{in radians: } 0.283 \times 2\pi = 1.78 \text{ rad} \approx 1.8 \text{ rad}$$

**What the examiner wants:** the time gap measured between two corresponding points (both peaks, or both crossings in the same direction), and correct conversion of the fraction into both degrees and radians when asked.

### Example 2: Displacement equation and displacement at a time (coursebook Worked example 2 pattern)

**Question:** A pendulum oscillates with frequency 1.5 Hz and amplitude 0.10 m, passing through equilibrium at $t = 0$. (a) Write an equation for its displacement. (b) Find its displacement at $t = 0.50$ s.

**Method:**

1. It passes through equilibrium at $t = 0$, so use the sine form with $\omega = 2\pi f = 2\pi \times 1.5 = 3.0\pi$ rad s$^{-1}$.
2. Substitute $t = 0.50$ s into $x = x_0 \sin \omega t$ with the calculator **in radian mode**.

**Answer:**

(a) $$x = x_0 \sin \omega t = 0.10 \sin(3.0\pi t)$$

(b) $$x = 0.10 \sin(2\pi \times 1.5 \times 0.50) = 0.10 \sin(4.713) = -0.10 \text{ m}$$

The bob is at the extreme end of its swing; the minus sign means the negative (left-hand) side.

**What the examiner wants:** choosing sine or cosine from the starting condition (equilibrium at $t = 0$ means sine), and radian mode - with degrees this gives $-8.2 \times 10^{-3}$ m instead of $-0.10$ m, a classic error.

### Example 3: Two-spring trolley: force, acceleration, period (9702/42/F/M/21 Q4, 9 marks)

**Question:** A trolley rests on a bench, tethered between two identical stretched springs, each of spring constant $k = 8.0$ N m$^{-1}$ and unstretched length 12.0 cm. In equilibrium each spring is 18.0 cm long. The trolley of mass 250 g is displaced 4.8 cm to one side and released; resistive forces are negligible. (a) State the significance of the minus sign in $a = -\omega^2 x$ [1]. (b)(i) Show that the resultant force on the trolley at the moment of release is 0.77 N [2]. (ii) Find the maximum acceleration [1]. (iii) Use $a = -\omega^2 x$ to find the period [3]. (iv) The experiment is repeated with an initial displacement of 2.4 cm: state and explain the effect on the period [2].

**Method:**

1. Minus sign: acceleration and displacement are in opposite directions.
2. Force at release: the spring on one side is stretched to $18.0 + 4.8 = 22.8$ cm (extension $0.108$ m) and the other is compressed to $18.0 - 4.8 = 13.2$ cm (extension above its natural length $0.012$ m). Both forces oppose the displacement, so take the difference.
3. Maximum acceleration: $a = F/m$.
4. Period: at the maximum displacement $x_0 = 0.048$ m, $a_{\max} = 3.1$ m s$^{-2}$, so $\omega = \sqrt{a_{\max}/x_0}$ and $T = 2\pi/\omega$.
5. Amplitude change: both the resultant force and the displacement are halved, so $a/x$ (and hence $\omega$) is unchanged - the period is unchanged because the period of SHM is independent of the amplitude.

**Answer:**

$$F = k \times 0.108 - k \times 0.012 = 8.0 \times 0.108 - 8.0 \times 0.012 = 0.864 - 0.096 = 0.77 \text{ N}$$

$$a = \frac{F}{m} = \frac{0.77}{0.25} = 3.1 \text{ m s}^{-2}$$

$$\omega = \sqrt{\frac{3.1}{0.048}} = 8.04 \text{ rad s}^{-1}, \qquad T = \frac{2\pi}{8.04} = 0.78 \text{ s}$$

Period unchanged: "(resultant) force halved and distance halved" (1), "same T" (1).

**What the examiner wants:** M1 for $F = kx$ on each spring with the correct extensions ($0.108$ m and $0.012$ m), A1 for 0.77 N - show your substitution clearly; $a = F/m$ with $m$ in kg; $\omega = \sqrt{a/x_0}$ then $T = 2\pi/\omega$; and for the last part both ideas: force halved AND distance halved, so period unchanged.

### Example 4: Damped trolley: SHM conditions, angular frequency, time from a graph (9702/42/M/J/18 Q4, 10 marks)

**Question:** (a) State two conditions necessary for a mass to be undergoing SHM [2]. (b) A trolley of mass 950 g is held between two springs, each of constant 230 N m$^{-1}$, both always extended. It is displaced and released; its displacement-time graph shows oscillations whose amplitude decreases gradually. (i) 1. State and explain whether the oscillations are heavily damped, critically damped or lightly damped. 2. Suggest the cause of the damping [3]. (ii) 1. Given $a = -\frac{2k}{m} x$, calculate the angular frequency $\omega$. 2. Determine the time $t_1$ shown on the graph (the first minimum after release, 1.5 periods) [5].

**Method:**

1. Conditions for SHM: acceleration proportional to displacement; acceleration directed towards the fixed point (displacement and acceleration in opposite directions).
2. Damping: the amplitude decreases gradually and the oscillations continue for many cycles, so light damping; the energy loss is due to friction in the wheels / friction between wheels and surface / air resistance.
3. Two springs in parallel (both always extended) give effective constant $2k$, so $\omega^2 = \frac{2k}{m}$.
4. $T = 2\pi/\omega$, then $t_1 = 1.5T$.

**Answer:**

$$\omega^2 = \frac{2k}{m} = \frac{2 \times 230}{0.950} \Rightarrow \omega = 22 \text{ rad s}^{-1}$$

$$T = \frac{2\pi}{\omega} = \frac{2\pi}{22} = 0.286 \text{ s}, \qquad t_1 = 1.5T = 0.43 \text{ s}$$

**What the examiner wants:** both ideas in (a) - "acceleration proportional to displacement" (1) AND "acceleration directed towards the fixed point" or "displacement and acceleration in opposite directions" (1); "amplitude decreases gradually, so light damping" (1) + "loss of energy" (1) + "due to friction in wheels / friction between wheels and surface / air resistance" (1); $\omega^2 = 2k/m$ (C1, C1) with $\omega = 22$ rad s$^{-1}$ (A1); $T = 2\pi/\omega$ (C1) and $t_1 = 1.5T = 0.43$ s (A1). **Lesson: the "two conditions" question needs BOTH the proportionality and the direction, and with two springs you use $2k$, not $k$.**

### Example 5: Floating test tube (9702/42/F/M/19 Q3, 7 marks)

**Question:** A test tube floats vertically in a liquid. When pushed down and released it oscillates. The acceleration of the tube is given by $a = -\frac{A\rho g}{M} x$, where $A = 4.5 \times 10^{-4}$ m$^2$ is the cross-sectional area, $M = 0.17$ kg the total mass and $x$ the vertical displacement. The period of oscillation is 1.3 s. (a) State what is meant by SHM [2]. (b) Use the expression to explain why the tube undergoes SHM [2]. (c)(i) Determine the angular frequency [2]. (c)(ii) Determine the density $\rho$ of the liquid [3].

**Method:**

1. SHM definition: acceleration directly proportional to displacement, directed towards equilibrium (opposite direction to displacement).
2. $A$, $\rho$, $g$ and $M$ are all constant, so the acceleration is proportional to the displacement; the minus sign shows the acceleration is in the opposite direction to the displacement (directed towards the equilibrium position).
3. $\omega = 2\pi/T$.
4. Compare $a = -\frac{A\rho g}{M} x$ with $a = -\omega^2 x$: $\omega^2 = \frac{A\rho g}{M}$, rearrange for $\rho$.

**Answer:**

$$\omega = \frac{2\pi}{T} = \frac{2\pi}{1.3} = 4.8 \text{ rad s}^{-1}$$

$$\omega^2 = \frac{A\rho g}{M} \Rightarrow 4.8^2 = \frac{4.5 \times 10^{-4} \times \rho \times 9.81}{0.17}$$

$$\rho = \frac{4.8^2 \times 0.17}{4.5 \times 10^{-4} \times 9.81} = 900 \text{ kg m}^{-3}$$

**What the examiner wants:** "constants so $a \propto x$" (1) and "minus sign shows acceleration and displacement in opposite directions" (1); correct rearrangement and substitution into $\omega^2 = A\rho g/M$, with units kg m$^{-3}$.

### Example 6: Energy from a velocity-time graph (coursebook Question 22 pattern)

**Question:** A 2.0 kg mass oscillates with SHM. Its velocity-time graph is sinusoidal with peak $v_{\max} = 0.40$ m s$^{-1}$ and period $T = 0.80$ s. Find (a) the maximum kinetic energy, (b) the maximum potential energy, (c) the maximum acceleration, (d) the maximum restoring force.

**Method:**

1. $E_{K,\max} = \frac{1}{2} m v_{\max}^2$.
2. For undamped SHM the total energy is constant, so the maximum PE equals the maximum KE.
3. $\omega = 2\pi/T$, and $a_{\max} = \omega^2 x_0 = \omega v_{\max}$ (since $v_{\max} = \omega x_0$).
4. $F_{\max} = m a_{\max}$.

**Answer:**

(a) $$E_{K,\max} = \frac{1}{2} m v_{\max}^2 = \frac{1}{2} \times 2.0 \times 0.40^2 = 0.16 \text{ J}$$

(b) $$E_{P,\max} = 0.16 \text{ J}$$

(c) First get the amplitude: $\omega = \frac{2\pi}{T} = \frac{2\pi}{0.80} = 7.85$ rad s$^{-1}$ and $x_0 = \frac{v_{\max}}{\omega} = \frac{0.40}{7.85} = 0.051$ m. Then

$$a_{\max} = \omega^2 x_0 = \omega v_{\max} = 7.85 \times 0.40 = 3.1 \text{ m s}^{-2}$$

(d) $$F_{\max} = m a_{\max} = 2.0 \times 3.1 = 6.3 \text{ N}$$

**What the examiner wants:** recognising that max PE = max KE for an undamped oscillator, and using $a_{\max} = \omega v_{\max}$ to avoid an unnecessary amplitude step. Give units on every answer.

### Example 7: Metal strip with a load (9702/42/O/N/17 Q3(b), 5 marks)

**Question:** A thin metal strip clamped at one end carries a load of mass $M = 0.24$ kg at the free end. Theory predicts the acceleration of the load is $a = -\frac{c}{ML^3} x$, where $L$ is the effective length of the strip and $c$ a positive constant. (i) Explain how the expression shows the load is undergoing SHM [2]. (ii) For $L = 0.65$ m the frequency of oscillation is 3.2 Hz. Calculate $c$ [3].

**Method:**

1. $\frac{c}{ML^3}$ is a constant, so acceleration is proportional to displacement; the minus sign shows acceleration and displacement are in opposite directions.
2. Compare with $a = -\omega^2 x$: the constant $\frac{c}{ML^3}$ plays the role of $\omega^2$, and $\omega = 2\pi f$.
3. Rearrange: $c = 4\pi^2 f^2 M L^3$, substituting $M = 0.24$ kg, $L = 0.65$ m, $f = 3.2$ Hz.

**Answer:**

$$\frac{c}{ML^3} = (2\pi f)^2 \Rightarrow c = 4\pi^2 f^2 M L^3$$

$$c = 4\pi^2 \times 3.2^2 \times 0.24 \times 0.65^3 = 27 \text{ kg m}^3 \text{ s}^{-2}$$

**What the examiner wants:** "$\frac{c}{ML^3}$ is a constant so acceleration is proportional to displacement" (1); "minus sign shows that acceleration and displacement are in opposite directions" (1); $\frac{c}{ML^3} = (2\pi f)^2$ (C1), $c = 4\pi^2 \times 3.2^2 \times 0.24 \times 0.65^3$ (C1), $c = 27$ kg m$^3$ s$^{-2}$ (A1).

### Example 8: Resonance, damping and the resonance curve (9702/43/M/J/24 Q4, 8 marks)

**Question:** (a) State what is meant by resonance [2]. (b) A ball on a stretched string is displaced and released; its displacement-time graph shows the amplitude decreasing steadily with time. (i) Name the phenomenon [1]. (ii) Explain the decrease in amplitude with time [2]. (iii) The graph shows 2.0 complete cycles in 0.50 s. Determine the frequency [1]. (c) The string is now driven by a vibration generator whose frequency is increased from 0 to 10 Hz. Sketch the variation of amplitude with driving frequency on axes from 0 to 10 Hz [2].

**Method:**

1. Resonance: oscillation of the object at maximum amplitude when the driving frequency equals the natural frequency of the system.
2. Amplitude decrease: the oscillations of the ball lose energy due to resistive forces acting on it - this is light damping.
3. Frequency: 2.0 complete cycles in 0.50 s gives $T = 0.25$ s, so $f = 1/T = 4.0$ Hz.
4. Sketch: a curve with a single maximum at a non-zero frequency, with that maximum at 4.0 Hz.

**Answer:** light damping; "oscillations (of ball) lose energy" due to "resistive forces (acting on ball)"; $f = 1/0.25 = 4.0$ Hz; resonance curve peaking at 4.0 Hz.

**What the examiner wants:** "oscillation (of object) at maximum amplitude" (1) "when driving frequency = natural frequency (of system)" (1) - defining resonance as just "amplitude increases" loses the mark; for the damping explanation: "oscillations lose energy" (1) AND "due to resistive forces" (1); for the sketch: a single maximum at a non-zero frequency (1), located at 4.0 Hz (1).

### Example 9: Resonance in NMR imaging (9702/42/F/M/21 Q8(b), 4 marks)

**Question:** Nuclear magnetic resonance imaging uses radio waves directed at the body. (i) Explain why radio waves are used, i.e. why resonance occurs [2]. (ii) State when the protons emit their own radio-frequency signal [2].

**Method:**

1. Identify the oscillating system (protons) and the driver (radio waves).
2. Resonance occurs when the driving frequency equals the natural frequency - the radio wave frequency matches the protons' natural frequency, so the protons absorb energy.
3. When the radio-wave pulse stops, the excited protons de-excite and emit their own radio-frequency signal, which is detected.

**Answer:** "frequency of radio waves is equal to natural frequency of protons" (1); "resonance of protons occurs / protons absorb energy" (1); "in between pulses / when pulse stops" (1); "protons de-excite / emit r.f. pulses / emitted pulse detected" (1).

**What the examiner wants:** resonance explanations need the oscillator, the driver, and the frequency match. Energy absorption happens because the driving frequency equals the natural frequency.

### Example 10: Light damping via eddy currents (9702/42/F/M/21 Q9(c), 4 marks)

**Question:** A copper sheet oscillates between the poles of a magnet. (i) State the type of damping [1]. (ii) A second sheet (with a slit) oscillates and its amplitude decays more slowly. Explain the damping of the first sheet [3].

**Method:**

1. The amplitude decays gradually over many oscillations: light damping.
2. Mechanism: the sheet cuts (magnetic) flux, inducing an emf; the emf drives (eddy) currents in the sheet; the currents cause a resistive force / dissipate energy.
3. Comparison: the slitted sheet has smaller currents, so less energy is dissipated and its amplitude decays more slowly.

**Answer:** light damping; "sheet cuts (magnetic) flux and causes induced emf" (1); "(induced) emf causes (eddy) currents (in sheet)" (1); "currents (in sheet) cause resistive force" OR "currents (in sheet) dissipate energy" (1); smaller currents in the slitted sheet, so its decay is slower (1).

**What the examiner wants:** the full chain - flux cut, induced emf, eddy currents, resistive force/energy dissipation. **Lesson: full damping answers = energy loss + the mechanism of the resistive force.**

### Further practice: coursebook end-of-chapter questions worth doing (from the Cambridge coursebook, Chapter 19)

- Q2: pendulum, $x_0 = 4.0$ cm, $T = 1.0$ s: write the displacement equation [2], max velocity [2], velocity at $x = 2.0$ cm [1].
- Q3: 50 g mass on a spring, amplitude 16 mm, $T = 0.84$ s: frequency [1], max velocity [1], max KE [2], max PE [1].
- Q5: from a displacement-time graph, determine $f$ and $T$ [2], then sketch velocity and acceleration on the same axes [3].
- Q7: car engine piston at 4200 rev min$^{-1}$, amplitude 12.5 cm, mass 0.24 kg: explain SHM [2], frequency [1], max speed [2], max acceleration [2], force for max acceleration [1].
- Q10: seismometer: explain why the natural frequency of the spring-mass system should be much less than the 30 - 40 Hz shock wave range [3]; what evidence an $a$-$x$ graph gives that motion is SHM [2]; calculate frequency from the graph [4].

---

## 6. Cheat Sheet (quick revision block)

**Definitions to write blind:**

- **SHM:** acceleration directly proportional to displacement from equilibrium, and directed towards it (opposite direction to displacement).
- **Amplitude $x_0$:** maximum displacement from equilibrium.
- **Period $T$:** time for one complete oscillation. **Frequency $f$:** oscillations per second.
- **Angular frequency $\omega$:** rate of change of phase, $\omega = 2\pi f = 2\pi/T$.
- **Phase difference:** fraction of a cycle (or degrees/radians) by which two oscillations are out of step.
- **Damping:** loss of energy from an oscillator due to resistive forces; amplitude decays.
- **Light damping:** gradual exponential decay of amplitude, many oscillations, period roughly constant.
- **Critical damping:** minimum damping for return to equilibrium without oscillating (fastest non-oscillatory return).
- **Heavy damping:** slow return to equilibrium without oscillating.
- **Resonance:** maximum amplitude of forced oscillation when driving frequency = natural frequency.
- **Natural frequency:** frequency of free oscillation after a disturbance.

**All formulas:**

$$f = \frac{1}{T}, \qquad \omega = 2\pi f = \frac{2\pi}{T}$$

$$x = x_0 \sin \omega t \text{ (start at equilibrium)} \qquad x = x_0 \cos \omega t \text{ (start at max } x)$$

$$a = -\omega^2 x, \qquad v = v_0 \cos \omega t, \qquad v = \pm \omega \sqrt{x_0^2 - x^2}$$

$$v_{\max} = \omega x_0, \qquad a_{\max} = \omega^2 x_0, \qquad F_{\max} = m a_{\max}$$

$$E = \frac{1}{2} m \omega^2 x_0^2, \qquad E_K = \frac{1}{2} m \omega^2 (x_0^2 - x^2), \qquad E_P = \frac{1}{2} m \omega^2 x^2$$

$$T = 2\pi \sqrt{\frac{m}{k}} \text{ (mass-spring; use } 2k \text{ for two springs in parallel)}$$

$$T = 2\pi \sqrt{\frac{l}{g}} \text{ (pendulum, small angles)}$$

$$\text{phase difference} = \frac{t}{T} \times 360^\circ = \frac{t}{T} \times 2\pi \text{ rad}$$

**Key facts:**

- Acceleration is always opposite to displacement (that is the minus sign).
- $v$ leads $x$ by $90^\circ$; $a$ is $180^\circ$ out of phase with $x$.
- Velocity = gradient of $x$-$t$ graph; acceleration = gradient of $v$-$t$ graph; $a$-$x$ graph is a straight line of gradient $-\omega^2$.
- Period is independent of amplitude (and of $m$ for a pendulum; independent of $g$ for a mass-spring).
- KE max at centre, PE max at extremes, total energy constant if undamped; $E \propto x_0^2$.
- KE and PE each go through 2 cycles per period of the oscillation.
- Resonance: amplitude max when $f_{\text{driving}} = f_{\text{natural}}$; damping lowers and broadens the peak.
- Energy of a damped oscillator is lost to resistive forces; amplitude decays exponentially.

**Common traps (see Section 7):**

- Calculator in DEGREES for $\sin \omega t$ - always use radians.
- Forgetting the minus sign in $a = -\omega^2 x$.
- Amplitude vs displacement: amplitude is the maximum, always positive.
- cm vs m and ms vs s conversions (phase difference $\frac{17 \text{ ms}}{60 \text{ ms}}$ needs no conversion, but $x_0$ and $x$ must be in the same unit).
- Two springs: effective constant is $2k$.
- Giving only "acceleration proportional to displacement" without the direction - drops a mark.
- Saying resonance is "when amplitude increases" - it is maximum at $f_{\text{driving}} = f_{\text{natural}}$.

---

## 7. Common Exam Mistakes (from examiner reports and mark scheme patterns)

**On the definition of SHM (most common lost marks):**

- Giving only "acceleration is proportional to displacement". The mark scheme gives one mark for proportionality and a second for the direction ("directed towards the equilibrium position" / "acceleration and displacement in opposite directions"). Both ideas are required for full marks (9702/42/M/J/18 Q4(a)).
- Writing "the force is proportional to displacement" when the question asks about acceleration - the definition is about acceleration.
- Saying "the acceleration is constant" or "velocity is proportional to displacement" - both wrong.

**On calculations:**

- **Calculator in degrees instead of radians.** The coursebook's own worked example 2 demonstrates the classic error: with degrees, $x = 0.10 \sin(4.713)$ gives $-8.2 \times 10^{-3}$ m instead of $-0.10$ m. The presence of $\pi$ in $\omega t$ is the reminder: radian mode.
- Forgetting the minus sign when quoting $a = -\omega^2 x$ or when stating the direction of acceleration.
- Using the wrong spring constant: with two springs holding a trolley, the effective constant is $2k$ (9702/42/M/J/18 Q4(b)(ii): $\omega^2 = 2k/m$, not $k/m$).
- Premature rounding of intermediate values (a general examiner complaint across papers: rounding early gives wrong final answers to the required significant figures).
- Mixing units: amplitudes in cm with displacements in m; times in ms with periods in s.
- In the pendulum experiment: timing only half an oscillation, or not dividing the total time by the number of oscillations to get $T$; not showing repeated readings; missing units (June 2024 examiner report).
- In $T = 2\pi\sqrt{m/k}$ problems, forgetting that $m$ must be in kg (950 g, 250 g, 50 g appear in real questions).

**On graphs and energy:**

- Confusing the $v$-$t$ and $a$-$t$ graph shapes: $v$ is a cosine when $x$ is a sine; $a$ is an inverted sine (antiphase with $x$).
- Thinking KE and PE peak once per cycle - they each peak twice (KE at both passages through the centre, PE at both extremes).
- Writing that total energy depends on amplitude linearly - it depends on $x_0^2$.
- On energy-displacement sketches: drawing KE and PE as straight lines instead of parabolas.

**On damping and resonance (from mark scheme patterns):**

- Identifying damping type from a graph: "amplitude decreases gradually, so light damping" - a single smooth return to zero with no oscillation is critical OR heavy; distinguish them by time (heavy is slower). "Returns without oscillating" alone is not enough.
- Explaining damping without the mechanism: full marks need "loses energy" AND "due to resistive forces" (9702/42/F/M/21 Q9(c), 9702/43/M/J/24 Q4(b)(ii)).
- Defining resonance as just "amplitude increases" - the mark scheme wants "oscillation at maximum amplitude" AND "when driving frequency = natural frequency" (9702/43/M/J/24 Q4(a)).
- Confusing the effect of damping on the resonance curve: damping DECREASES the peak amplitude, BROADENS the peak, and shifts the resonant frequency slightly LOWER. "Damping increases the amplitude" is a common wrong answer.
- Confusing free and forced oscillations: a forced oscillator vibrates at the driving frequency, not its natural frequency.
- For resonance examples, forgetting to name both the oscillating system and the driver (coursebook Q24 asks for exactly this: three problems and three uses, with system + driver for each).

**On the practical (from the June 2024 examiner report on the oscillation experiment):**

- Judging the end of a complete oscillation is difficult - time 20 oscillations, not one.
- Parallax error when reading the amplitude or the position of the oscillating mass - use a fiducial marker.
- The oscillation swinging in more than one plane (elliptical motion) - release it carefully in a single vertical plane.
- Not accounting for the mass of the bob/putty.
- Two sets of data are not enough for a valid conclusion - take a range of values and plot a graph.
- Improvement answers need specifics: "video camera with a timer in the frame, viewed frame by frame", not just "use a video camera".

---

# Chapter 20: Communications Systems - CAIE A Level Physics (9702) Study Notes

## 2. Definition Sheet

> **Communication system:** a system that transfers information from a source to a receiver via a channel.

> **Carrier wave:** a high-frequency wave whose amplitude or frequency is modulated to carry information.

> **Modulation:** the variation of the amplitude or frequency of a carrier wave in order to carry information.

> **Demodulation:** the recovery of the original information signal from a modulated carrier.

> **Amplitude modulation (AM):** modulation in which the amplitude of the carrier wave varies in proportion to the signal, while the frequency remains constant.

> **Frequency modulation (FM):** modulation in which the frequency of the carrier wave varies in proportion to the signal, while the amplitude remains constant.

> **Sideband:** a frequency produced by modulation, at $f_c - f_m$ (lower) or $f_c + f_m$ (upper).

> **Bandwidth:** the range of frequencies occupied by a signal; for AM with highest modulating frequency $f_m$, bandwidth $= 2f_m$.

> **Analogue signal:** a signal that varies continuously and can take any value within a range.

> **Digital signal:** a signal that takes only two discrete levels, represented by 0 and 1.

> **Bit:** a single binary digit (0 or 1).

> **Sampling:** measuring the analogue signal at regular time intervals.

> **Sampling rate:** the number of samples taken per second.

> **Quantisation:** rounding each sample to the nearest discrete voltage level before encoding it as a binary number.

> **Analogue-to-digital conversion (ADC):** the process of sampling and quantising an analogue signal to produce a digital signal.

> **Digital-to-analogue conversion (DAC):** the process of converting a digital signal back into an analogue voltage.

> **Regeneration:** the process of restoring a distorted digital pulse to a clean 0 or 1, removing noise.

> **Noise:** unwanted random electrical signal that adds to and distorts the transmitted signal.

> **Attenuation:** the reduction in signal power as it travels through a channel.

> **Decibel (dB):** a logarithmic unit for comparing two powers; $10\log_{10}(P_1/P_2)$.

> **Signal-to-noise ratio (SNR):** $10\log_{10}(P_{\text{signal}}/P_{\text{noise}})$.

> **Crosstalk:** unwanted transfer of a signal from one channel to another.

> **Geostationary satellite:** a satellite in an equatorial orbit with a period of 24 hours at a height of about $36\,000~\text{km}$, so it appears stationary from Earth.

> **Total internal reflection:** the complete reflection of light at a boundary when the angle of incidence exceeds the critical angle.

## 3. Formula Sheet

| Formula | Meaning of symbols | Units | When to use it |
|---|---|---|---|
| $c = f\lambda$ | $c$ speed of light, $f$ frequency, $\lambda$ wavelength | $\text{m s}^{-1}$, Hz, m | Carrier wavelength/frequency |
| $f_{\text{LSB}} = f_c - f_m$ | lower sideband | Hz | AM spectrum |
| $f_{\text{USB}} = f_c + f_m$ | upper sideband | Hz | AM spectrum |
| $B = 2f_m$ | $B$ bandwidth, $f_m$ highest modulating frequency | Hz | AM bandwidth |
| $\Delta f = k A_m$ | frequency deviation, $k$ deviation sensitivity, $A_m$ signal amplitude | Hz | FM frequency swing |
| $f_s \ge 2f_{\max}$ | $f_s$ sampling rate | Hz | Nyquist sampling condition |
| $N = 2^n$ | $N$ levels, $n$ bits | — | ADC resolution |
| $\text{bit rate} = n f_s$ | bits per second | $\text{bit s}^{-1}$ | Digital data rate |
| $\text{attenuation} = 10\log_{10}(P_{\text{in}}/P_{\text{out}})$ | powers | dB | Signal loss |
| $\text{gain} = 10\log_{10}(P_{\text{out}}/P_{\text{in}})$ | powers | dB | Amplification |
| $\text{attenuation per length} = \frac{\text{attenuation}}{\text{length}}$ | length in km | $\text{dB km}^{-1}$ | Cable/fibre loss |
| $\text{SNR} = 10\log_{10}(P_{\text{signal}}/P_{\text{noise}})$ | powers | dB | Signal quality |
| $P_{\text{out}} = P_{\text{in}} \times 10^{\text{dB}_{\text{total}}/10}$ | total dB (signed) | W | Combined stages |
| $t = \frac{d}{c}$ | $d$ path length, $c$ speed of light | s | Satellite delay |

**Exam facts:** decibels add for cascaded stages. A doubling of power is about $+3~\text{dB}$; a tenfold increase is $+10~\text{dB}$; a thousandfold increase is $+30~\text{dB}$. The Nyquist rate is **twice** the highest frequency, not the bandwidth.

## 4. Methods (Question Types & Methods)

### 1. Sketch and describe AM/FM waves

**Method:**
1. Draw the unmodulated carrier with constant amplitude and constant frequency.
2. Draw the signal (usually a lower-frequency sine wave).
3. For AM: draw a carrier whose envelope follows the signal; frequency stays the same.
4. For FM: draw a carrier of constant amplitude whose spacing between cycles decreases when the signal is positive and increases when negative.
5. Label one carrier period and one signal period.

**Traps:** changing the carrier frequency in AM; changing the amplitude in FM; drawing the envelope with a larger amplitude than the carrier.

### 2. Find carrier and signal frequencies from a graph

**Method:**
1. Count the number of complete carrier cycles in a known time interval; $f_c = N/t$.
2. Find the period of the envelope (one complete variation of amplitude or frequency) to get $f_m$.
3. Check: the carrier should have many cycles per signal cycle.

**Traps:** counting half-cycles; using the envelope period as the carrier period; mixing $\mu\text{s}$ and ms.

### 3. Find sidebands and bandwidth

**Method:**
1. Identify $f_c$ and the highest modulating frequency $f_m$.
2. Sidebands: $f_c - f_m$ and $f_c + f_m$.
3. Bandwidth $= 2f_m$.
4. For a range of signal frequencies, use the highest $f_m$.

**Traps:** using $f_m$ instead of $2f_m$; forgetting that the bandwidth is centred on the carrier; adding the carrier to the bandwidth.

### 4. FM deviation

**Method:**
1. Maximum frequency shift $= \text{deviation sensitivity} \times \text{signal amplitude}$.
2. Maximum frequency $= f_c + \Delta f$; minimum $= f_c - \Delta f$.
3. The frequency changes at the signal frequency (twice per cycle if counting both increase and decrease).

**Traps:** applying the deviation to the amplitude; forgetting to convert kHz/V and V consistently; using peak-to-peak signal amplitude instead of peak.

### 5. Binary conversion

**Method:**
1. Write the place values $1, 2, 4, 8, 16, \dots$
2. For decimal to binary, subtract the largest place value repeatedly.
3. For binary to decimal, multiply each bit by its place value and add.
4. Pad to the required number of bits with leading zeros.

**Traps:** reversing bit order; forgetting leading zeros; treating binary 10 as decimal ten.

### 6. Sampling and bit rate

**Method:**
1. Identify the highest signal frequency $f_{\max}$.
2. Minimum sampling rate $= 2f_{\max}$.
3. Number of levels $= 2^n$.
4. Bit rate $= n f_s$.
5. For storage, multiply bit rate by time.

**Traps:** using the bandwidth instead of $f_{\max}$; forgetting to convert kHz to Hz; using $2^n$ as the number of bits rather than levels.

### 7. Attenuation in dB

**Method:**
1. Identify input and output powers in the **same units**.
2. Attenuation $= 10\log(P_{\text{in}}/P_{\text{out}})$.
3. For cascaded stages, add dB values (attenuation positive, gain negative, or use signed dB throughout).
4. Convert back: $P_{\text{out}} = P_{\text{in}} \times 10^{-\text{attenuation}/10}$.

**Traps:** mixing mW and W; subtracting instead of adding dB; using natural logs; forgetting that a gain of $30~\text{dB}$ means a factor of $1000$, not 30.

### 8. Signal-to-noise ratio

**Method:**
1. Identify signal and noise powers in the same units.
2. $\text{SNR} = 10\log(P_s/P_n)$.
3. To find minimum signal power: $P_s = P_n \times 10^{\text{SNR}/10}$.
4. To find maximum cable length: attenuation available $= 10\log(P_{\text{in}}/P_{\min})$; length $=$ attenuation / attenuation per km.

**Traps:** using amplitudes instead of powers (would give $20\log$); forgetting the noise is constant; using the wrong power for the input.

### 9. Compare channels

**Method:**
1. State bandwidth, attenuation, noise/interference, security, cost and mobility.
2. Link each property to the physics (screening, TIR, line-of-sight, diffraction).
3. Give a clear advantage and disadvantage for each channel.

**Traps:** claiming optic fibre has no attenuation (it has low attenuation); claiming satellites have no delay; claiming radio is always secure.

## 5. Solved Examples

### Example 1: AM frequencies

**Question:** An AM carrier of $200~\text{kHz}$ is modulated by a $5~\text{kHz}$ signal. State the sideband frequencies and the bandwidth.

**Method:**
1. LSB $= 200 - 5 = 195~\text{kHz}$.
2. USB $= 200 + 5 = 205~\text{kHz}$.
3. Bandwidth $= 205 - 195 = 10~\text{kHz}$.

**Answer:** $195$ and $205~\text{kHz}$; $10~\text{kHz}$.

### Example 2: AM bandwidth and station count

**Question:** AM stations have a bandwidth of $9~\text{kHz}$. The available band is $530$–$1700~\text{kHz}$. Calculate the maximum number of stations.

**Method:**
1. Available range $= 1700 - 530 = 1170~\text{kHz}$.
2. Number $= \frac{1170}{9} = 130$.

**Answer:** 130 stations.

### Example 3: FM deviation

**Question:** A $500~\text{kHz}$ carrier is modulated by a $16~\text{kHz}$ signal of amplitude $3.0~\text{V}$. The deviation is $8.0~\text{kHz V}^{-1}$. Calculate the maximum and minimum frequencies and the number of frequency changes per second.

**Method:**
1. $\Delta f = 8.0 \times 3.0 = 24~\text{kHz}$.
2. Maximum $= 500 + 24 = 524~\text{kHz}$.
3. Minimum $= 500 - 24 = 476~\text{kHz}$.
4. The frequency increases and decreases once per signal cycle, so $16\,000$ increases and $16\,000$ decreases per second (or $32\,000$ changes in direction).

**Answer:** $524$ and $476~\text{kHz}$; $16\,000$ cycles per second.

### Example 4: FM bandwidth

**Question:** An FM signal has a carrier of $100~\text{MHz}$ and a maximum deviation of $75~\text{kHz}$. Estimate the frequency range occupied.

**Method:**
1. Upper frequency $= 100.000 + 0.075 = 100.075~\text{MHz}$.
2. Lower frequency $= 100.000 - 0.075 = 99.925~\text{MHz}$.
3. The actual FM spectrum extends further due to sidebands; this is the minimum range.

**Answer:** approximately $99.925$–$100.075~\text{MHz}$.

### Example 5: Binary conversion

**Question:** Convert $1011_2$ to decimal and $13$ to binary.

**Method:**
1. $1011_2 = 8 + 0 + 2 + 1 = 11$.
2. $13 = 8 + 4 + 1 = 1101_2$.

**Answer:** 11 and 1101.

### Example 6: Sampling rate

**Question:** A signal has a maximum frequency of $15~\text{kHz}$. State the minimum sampling rate and the bit rate for 16-bit samples.

**Method:**
1. $f_s \ge 30~\text{kHz}$.
2. Bit rate $= 16 \times 30\,000 = 480\,000~\text{bit s}^{-1}$.

**Answer:** $30~\text{kHz}$; $480~\text{kbit s}^{-1}$.

### Example 7: ADC resolution

**Question:** An 8-bit ADC has a range of $0$ to $5.0~\text{V}$. Calculate the number of levels and the voltage resolution.

**Method:**
1. Levels $= 2^8 = 256$.
2. Resolution $= \frac{5.0}{255} = 0.0196~\text{V}$.

**Answer:** 256 levels; about $20~\text{mV}$ per step.

### Example 8: Attenuation

**Question:** A signal of $10~\text{mW}$ is attenuated by $20~\text{dB}$. Calculate the output power.

**Method:**
1. $20 = 10\log(10/P_{\text{out}})$.
2. $\log(10/P_{\text{out}}) = 2$, so $10/P_{\text{out}} = 100$.
3. $P_{\text{out}} = 0.10~\text{mW}$.

**Answer:** $0.10~\text{mW}$.

### Example 9: Attenuation per km

**Question:** A $60~\text{m}$ fibre has input $1.26~\text{mW}$ and output $1.12~\text{mW}$. Calculate the attenuation per km.

**Method:**
1. Attenuation $= 10\log(1.26/1.12) = 0.512~\text{dB}$.
2. Length $= 0.060~\text{km}$.
3. Per km $= 0.512/0.060 = 8.5~\text{dB km}^{-1}$.

**Answer:** $8.5~\text{dB km}^{-1}$.

### Example 10: Gain and attenuation

**Question:** A $1.0~\text{mW}$ signal passes through a $30~\text{dB}$ amplifier and then a cable with $18~\text{dB}$ attenuation. Calculate the overall gain in dB and the output power.

**Method:**
1. Overall $= +30 - 18 = +12~\text{dB}$.
2. $P_{\text{out}} = 1.0 \times 10^{12/10} = 1.0 \times 10^{1.2}$.
3. $P_{\text{out}} = 15.8~\text{mW}$.

**Answer:** $+12~\text{dB}$; $16~\text{mW}$.

### Example 11: Repeater spacing

**Question:** A cable has attenuation $10~\text{dB km}^{-1}$. The input power is $200~\text{mW}$ and the minimum acceptable power is $2.0~\text{mW}$. Calculate the maximum length without a repeater.

**Method:**
1. Attenuation $= 10\log(200/2.0) = 10\log 100 = 20~\text{dB}$.
2. Length $= 20/10 = 2.0~\text{km}$.

**Answer:** $2.0~\text{km}$.

### Example 12: Satellite delay

**Question:** A geostationary satellite is $36\,000~\text{km}$ above the Earth's surface. Calculate the one-way delay and the minimum delay in a two-way conversation.

**Method:**
1. One-way distance $= 3.6 \times 10^7~\text{m}$.
2. $t = \frac{3.6 \times 10^7}{3.0 \times 10^8} = 0.12~\text{s}$.
3. Two-way (up and down) $= 0.24~\text{s}$ for one speaker; a reply adds another $0.24~\text{s}$, total $0.48~\text{s}$.

**Answer:** $0.12~\text{s}$ one way; at least $0.48~\text{s}$ for a two-way exchange (including the reply path).

## 6. Exam-Style Questions (Full Solutions)

### Question 1

An AM radio station broadcasts on a carrier of $198~\text{kHz}$ and is modulated by audio frequencies up to $4.5~\text{kHz}$. (a) State the frequency range transmitted. (b) Calculate the bandwidth. (c) Explain why the station's bandwidth must be limited.

**Solution:**
1. (a) Lower $= 198 - 4.5 = 193.5~\text{kHz}$; upper $= 198 + 4.5 = 202.5~\text{kHz}$.
2. (b) Bandwidth $= 2 \times 4.5 = 9.0~\text{kHz}$.
3. (c) Stations are spaced by at least the bandwidth; if the bandwidth were larger, adjacent stations would overlap and interfere. The total number of stations in the LW/MW band would also decrease.

**Answer:** (a) $193.5$–$202.5~\text{kHz}$; (b) $9.0~\text{kHz}$; (c) to avoid overlap/interference between stations.

### Question 2

A carrier wave of $2.0~\text{MHz}$ and amplitude $4.0~\text{V}$ is frequency-modulated by a signal of frequency $5.0~\text{kHz}$ and amplitude $1.5~\text{V}$. The frequency deviation is $20~\text{kHz V}^{-1}$. (a) Calculate the maximum frequency deviation. (b) State the maximum and minimum frequencies. (c) State the amplitude of the modulated wave. (d) Explain how the wave changes if the signal amplitude is doubled.

**Solution:**
1. (a) $\Delta f = 20 \times 1.5 = 30~\text{kHz}$.
2. (b) Maximum $= 2.000 + 0.030 = 2.030~\text{MHz}$; minimum $= 1.970~\text{MHz}$.
3. (c) $4.0~\text{V}$ (constant in FM).
4. (d) The deviation doubles to $60~\text{kHz}$, so the frequency range becomes $1.940$–$2.060~\text{MHz}$; the rate of change stays at $5.0~\text{kHz}$.

**Answer:** (a) $30~\text{kHz}$; (b) $2.030$ and $1.970~\text{MHz}$; (c) $4.0~\text{V}$; (d) double the deviation.

### Question 3

Explain the difference between analogue and digital signals, and state three advantages of digital transmission.

**Solution:**
1. An analogue signal varies continuously and can take any value in a range; a digital signal has only two levels (0 and 1).
2. Advantage 1: digital signals can be regenerated, removing accumulated noise.
3. Advantage 2: digital signals can be stored and processed by computers and can carry error-detection data.
4. Advantage 3: digital transmission is more reliable/secure and can be encrypted.

**Answer:** as above.

### Question 4

A signal has a bandwidth of $3.4~\text{kHz}$ and is sampled at $8.0~\text{kHz}$ with 8-bit resolution. (a) Show that the sampling rate is adequate. (b) Calculate the bit rate. (c) State one effect of reducing the number of bits to 4.

**Solution:**
1. (a) Nyquist requires $f_s \ge 2 \times 3.4 = 6.8~\text{kHz}$; $8.0~\text{kHz}$ is adequate.
2. (b) Bit rate $= 8 \times 8000 = 64\,000~\text{bit s}^{-1}$.
3. (c) Fewer levels (16 instead of 256), so the quantisation error increases and the reproduced signal is less accurate/noisier.

**Answer:** (a) $8.0 > 6.8~\text{kHz}$; (b) $64~\text{kbit s}^{-1}$; (c) greater quantisation error.

### Question 5

A $20~\text{km}$ cable has an attenuation of $10~\text{dB km}^{-1}$. Four repeater amplifiers, each with a gain of $40~\text{dB}$, are spaced along the cable. The input power is $200~\text{mW}$. (a) Calculate the total attenuation. (b) Calculate the total gain. (c) Calculate the output power.

**Solution:**
1. (a) Attenuation $= 10 \times 20 = 200~\text{dB}$.
2. (b) Gain $= 4 \times 40 = 160~\text{dB}$.
3. (c) Net $= -200 + 160 = -40~\text{dB}$.
4. $P_{\text{out}} = 200 \times 10^{-40/10} = 200 \times 10^{-4} = 0.020~\text{mW}$.

**Answer:** (a) $200~\text{dB}$; (b) $160~\text{dB}$; (c) $0.020~\text{mW}$ (or $2.0 \times 10^{-5}~\text{W}$).

### Question 6

Compare a geostationary satellite with a polar-orbit satellite for communications.

**Solution:**
1. Geostationary: equatorial orbit, period 24 hours, height about $36\,000~\text{km}$; appears stationary, so dishes are fixed; wide coverage except near the poles; long delay ($\sim 0.24~\text{s}$ each way).
2. Polar: passes over the poles, lower altitude (e.g. $1000~\text{km}$), shorter period (e.g. $100~\text{min}$); better resolution because closer; not always overhead, so tracking is needed; shorter delay.
3. Both use microwave uplink/downlink at different frequencies.

**Answer:** as above.

## 7. Cheat Sheet

**Modulation:**
- AM: amplitude varies, frequency constant; sidebands $f_c \pm f_m$; bandwidth $2f_m$.
- FM: frequency varies, amplitude constant; deviation $\Delta f = kA_m$; larger bandwidth, better quality, less noise.

**Digital:**
- Analogue = continuous; digital = 0/1.
- ADC: sample → quantise → encode; DAC: decode → staircase → smooth.
- Nyquist: $f_s \ge 2f_{\max}$.
- Levels $=2^n$; bit rate $= nf_s$.
- Regeneration removes noise; amplification does not.

**Decibels:**
- Attenuation $= 10\log(P_{\text{in}}/P_{\text{out}})$.
- Gain $= 10\log(P_{\text{out}}/P_{\text{in}})$.
- dB add for cascaded stages.
- $+3~\text{dB}$ = double; $+10~\text{dB}$ = ten times; $+30~\text{dB}$ = thousand times.
- SNR $= 10\log(P_s/P_n)$.

**Channels:**
- Wire-pair: cheap, lossy, noisy, low bandwidth.
- Coaxial: screened, higher bandwidth, less crosstalk.
- Radio: surface (<3 MHz, 1000 km), sky (3–30 MHz, worldwide), space (>30 MHz, line-of-sight).
- Microwave/satellite: high bandwidth, line-of-sight, geostationary 36,000 km/24 h, polar lower/faster.
- Optic fibre: TIR, infrared, huge bandwidth, low loss, secure, immune to EMI.

## 8. Common Exam Mistakes

1. **Saying the frequency changes in AM.** In AM the carrier frequency is constant; only the amplitude changes.
2. **Saying the amplitude changes in FM.** In FM the amplitude is constant; only the frequency changes.
3. **Using bandwidth $= f_m$ instead of $2f_m$.** An AM signal has two sidebands, one on each side of the carrier.
4. **Forgetting the carrier in the spectrum.** The modulated wave contains the carrier plus both sidebands.
5. **Mixing up deviation and signal frequency.** Deviation is the **frequency swing**; the signal frequency is the **rate** at which the swing occurs.
6. **Using Nyquist as $f_s = f_{\max}$.** It must be at least **twice** the highest frequency.
7. **Forgetting to convert kHz to Hz.** Decibel and bit-rate calculations require consistent units.
8. **Adding dB incorrectly.** Attenuation and gain have opposite signs; use signed dB and add.
9. **Using $10\log$ for amplitude ratios.** Power ratios use $10\log$; amplitude ratios would use $20\log$.
10. **Mixing mW and W in a ratio.** Convert both powers to the same unit before taking the logarithm.
11. **Claiming optic fibre has zero attenuation.** It has **low** attenuation, not zero; repeaters are still needed over long distances.
12. **Claiming satellites have no delay.** The long path to and from a geostationary satellite causes a noticeable delay (about $0.24~\text{s}$ each way).
13. **Saying digital signals cannot be corrupted.** Noise can still cause bit errors; regeneration only works if the pulse is recognisable.
14. **Confusing crosstalk with noise.** Crosstalk is interference from another signal channel; noise is random unwanted disturbance.

---

# Chapter 21: Thermal Physics - CAIE A Level Physics (9702) Study Notes

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

---

# Chapter 22: Ideal Gases - CAIE A Level Physics (9702) Study Notes

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

---

# Chapter 23: Coulomb's Law and Electric Fields - CAIE A Level Physics (9702) Study Notes

## 2. Definition Sheet

Every definition you must know word-perfect for the exam. Learn these exactly - the wording is what the mark schemes award.

> **Electric field:** a field of force - a region of space in which a charge experiences an electric force. It is produced by electric charges.

> **Electric field strength:** the force per unit positive charge acting on a charge placed at that point.
>
> Mark scheme: "force per unit charge" (1 mark) plus "(force on a) positive charge" (1 mark). "Per unit charge" must be explicit.

> **Coulomb's law:** any two point charges exert an electrical force on each other that is proportional to the product of their charges and inversely proportional to the square of the distance between them.

> **Electric potential:** the work done per unit positive charge in bringing a small test charge from infinity to the point.
>
> Mark scheme: the definition must be dimensionally correct, i.e. work done per unit charge (energy per coulomb, $\text{J C}^{-1}$), not energy. "Work done in moving positive charge from infinity" also gains credit, and "from infinity" fixes the sign convention.

> **Electric potential energy:** the work done in bringing two point charges from infinity to their separation. For charges $Q$ and $q$ separated by $r$: $E_P = \frac{Qq}{4\pi\epsilon_0 r}$.

> **Equipotential (line or surface):** a line (or surface) on which the electric potential is constant. Field lines are always perpendicular to equipotentials, and no work is done moving a charge along one.

> **Uniform field:** a field in which the field strength is the same at every point; the field lines are parallel and equally spaced (for example between two charged parallel plates).

> **Line of force (field line):** a line drawn so that its direction at any point gives the direction of the force on a positive test charge. The spacing of the lines shows the field strength: closer lines mean a stronger field. Lines never cross and they meet conductors at right angles.

**Comparing electric and gravitational fields - the essay points (learn all of these):**

- Both are fields of force.
- Both obey inverse square laws for point sources: $F = \frac{GMm}{r^2}$ and $F = \frac{Q_1 Q_2}{4\pi\epsilon_0 r^2}$.
- Both have scalar potentials that are zero at infinity.
- Both have the same relationship between field strength and potential gradient: $g = -\frac{d\phi}{dr}$, $E = -\frac{dV}{dr}$.
- The crucial difference: gravity only attracts because mass is always positive, while electric charges come in two signs, so electric forces can attract or repel and electric potentials can be positive or negative.

## 3. Formula Sheet

**Quick reference (using the Coulomb constant $k = \frac{1}{4\pi\epsilon_0} = 8.99 \times 10^9 \text{ N m}^2 \text{ C}^{-2} \approx 9.0 \times 10^9$):**

$$F = \frac{kQ_1 Q_2}{r^2}, \qquad E = \frac{F}{Q}, \qquad F = qE, \qquad E = \frac{kQ}{r^2}, \qquad E = \frac{V}{d}, \qquad V = \frac{kQ}{r}, \qquad E_P = \frac{kQq}{r}, \qquad W = qV, \qquad W = qEd, \qquad E = -\frac{\Delta V}{\Delta r}$$

| Formula | Meaning of symbols | Units | When to use it |
| --- | --- | --- | --- |
| $$F = \frac{Q_1 Q_2}{4\pi\epsilon_0 r^2}$$ | $F$ force between charges, $Q_1$, $Q_2$ charges, $r$ separation (centre-to-centre), $\epsilon_0$ permittivity of free space | $F$ in N, $Q$ in C, $r$ in m, $\epsilon_0$ in $\text{F m}^{-1}$ | Force between two point charges or charged spheres (recall from memory; not on formula sheet) |
| $$E = \frac{F}{Q}$$ | $E$ field strength, $F$ force on charge $Q$ at that point | $\text{N C}^{-1}$ or $\text{V m}^{-1}$ | Definition of field strength; finding $E$ from a measured force |
| $$F = qE$$ | $F$ force on charge $q$ in field $E$ | N | Force on any charge placed in an electric field |
| $$E = \frac{Q}{4\pi\epsilon_0 r^2}$$ | $E$ field strength due to charge $Q$ at distance $r$ | $\text{V m}^{-1}$ | Field near a point charge or outside a charged sphere (recall from memory) |
| $$E = \frac{V}{d}$$ | $E$ field strength, $V$ p.d. between plates, $d$ plate separation | $\text{V m}^{-1}$ | Uniform field between parallel plates ONLY |
| $$V = \frac{Q}{4\pi\epsilon_0 r}$$ | $V$ potential due to charge $Q$ at distance $r$ | V | Potential near a point charge or charged sphere (given on formula sheet) |
| $$E_P = \frac{Qq}{4\pi\epsilon_0 r}$$ | $E_P$ potential energy of two charges $Q$, $q$ separated by $r$ | J | Energy of a system of two charges; work to bring charges together from infinity |
| $$W = qV$$ | $W$ work done moving charge $q$ through potential difference $V$ | J | Work/energy change when a charge moves between two potentials |
| $$W = qEd$$ | $W$ work done moving charge $q$ a distance $d$ along a uniform field $E$ | J | Moving a charge along the field direction in a uniform field (moving perpendicular to the field does no work) |
| $$E = -\frac{\Delta V}{\Delta r}$$ | $E$ field strength, $\Delta V$ change in potential over distance $\Delta r$ | $\text{V m}^{-1}$ | Field strength from a potential gradient (graph tangent or uniform field) |
| $$\frac{1}{4\pi\epsilon_0} \approx 9.0 \times 10^9 \text{ N m}^2 \text{ C}^{-2}$$ | Coulomb constant $k$ | $\text{N m}^2 \text{ C}^{-2}$ | Quick estimates; data sheet value $8.99 \times 10^9 \text{ m F}^{-1}$ |

Constants you will need (from the data sheet): $\epsilon_0 = 8.85 \times 10^{-12} \text{ F m}^{-1}$, $\frac{1}{4\pi\epsilon_0} = 8.99 \times 10^9 \text{ m F}^{-1}$, $e = 1.60 \times 10^{-19} \text{ C}$, $m_p = 1.67 \times 10^{-27} \text{ kg}$, $G = 6.67 \times 10^{-11} \text{ N m}^2 \text{ kg}^{-2}$.

**Exam fact:** the data sheet gives $\epsilon_0 = 8.85 \times 10^{-12} \text{ F m}^{-1}$ and $\frac{1}{4\pi\epsilon_0} = 8.99 \times 10^9 \text{ m F}^{-1}$, plus $e = 1.60 \times 10^{-19} \text{ C}$. The formula sheet provides $V = \frac{Q}{4\pi\epsilon_0 r}$, but NOT Coulomb's law or $E = \frac{Q}{4\pi\epsilon_0 r^2}$: you must recall those two from memory.

## 4. Methods (Question Types & Methods)

These are the ways Cambridge has actually asked about electric fields. Each method below is what a full-mark answer looks like.

### 1. Find the force between two charges (Coulomb's law)

**Method:**
1. Identify $Q_1$, $Q_2$ and the centre-to-centre distance $r$ in metres. Convert all units first (cm to m, $\mu\text{C}$ to C: $1 \mu\text{C} = 10^{-6} \text{ C}$, nC: $1 \text{ nC} = 10^{-9} \text{ C}$).
2. Substitute into $F = \frac{Q_1 Q_2}{4\pi\epsilon_0 r^2}$, using $\frac{1}{4\pi\epsilon_0} = 8.99 \times 10^9$.
3. Give the magnitude with units, then state the direction: like charges repel, unlike charges attract.

**Traps:** forgetting to square $r$; using surface-to-surface distance instead of centre-to-centre for spheres; mixing up $10^{-6}$ and $10^{-9}$.

### 2. Find the force on a charge in a field ($F = qE$)

**Method:**
1. Find $E$ (either given, from $E = \frac{V}{d}$ for plates, or from $E = \frac{Q}{4\pi\epsilon_0 r^2}$ for a point charge).
2. Multiply by the charge: $F = qE$.
3. Direction: positive charges are pushed along the field (towards negative plates/charges), negative charges opposite to the field.

### 3. Find the electric field strength at a point due to a point charge or sphere

**Method:**
1. Use $E = \frac{Q}{4\pi\epsilon_0 r^2}$ with $r$ measured from the centre of the charge/sphere.
2. Watch the units: field strengths are often quoted in $\text{V cm}^{-1}$ or $\text{kV m}^{-1}$; convert to $\text{V m}^{-1}$.
3. State the direction (radially away from a positive charge, towards a negative charge).

### 4. Resultant field of two or more charges (vector addition)

**Method:**
1. Work out the field each charge produces at the point (magnitude and direction) separately.
2. Add them as vectors along the line joining the charges: same direction adds, opposite direction subtracts.
3. The point where the resultant field is zero lies between two like charges, closer to the smaller charge: at that point $E_1 = E_2$, so $\frac{Q_1}{r_1^2} = \frac{Q_2}{r_2^2}$. Use this to find a charge ratio or an unknown charge.
4. Never use $Q = 4\pi\epsilon_0 r^2 E$ with the resultant field near one charge: the resultant field is not produced by a single charge.

### 5. Uniform field between parallel plates

**Method:**
1. $E = \frac{V}{d}$ (V in volts, d in metres).
2. Force on a charge: $F = qE = \frac{qV}{d}$.
3. Acceleration: $a = \frac{F}{m} = \frac{qE}{m}$.
4. Work/energy to move a charge between the plates: $W = qV$.
5. Projectile-style motion: constant speed parallel to the plates, constant acceleration towards the opposite plate; the path is a parabola. Use $s = ut + \frac{1}{2}at^2$ in the field direction.

### 6. Find the electric potential at a point

**Method:**
1. For each charge, compute $V = \frac{Q}{4\pi\epsilon_0 r}$ using the distance from that charge to the point.
2. Add the potentials as scalars, keeping the signs (positive for positive charges, negative for negative charges).
3. Give the answer in volts.

### 7. Potential energy of charge pairs / work done moving charges

**Method:**
1. For two charges: $E_P = \frac{Qq}{4\pi\epsilon_0 r}$ (sign follows the charges).
2. Work done moving a charge between two points: $W = q(V_B - V_A)$.
3. In a uniform field: $W = qV$ or $W = qEd$ (moving distance $d$ along the field direction). Moving perpendicular to the field does no work (potential does not change).

### 8. Field strength from a potential gradient (graph question)

**Method:**
1. If the graph is a straight line (uniform field): $E = \frac{\Delta V}{\Delta d}$, the constant gradient.
2. If the graph is curved (radial field): draw the tangent at the point of interest, find its gradient $\frac{\Delta V}{\Delta r}$, then $E = -\text{gradient}$.
3. Convert units carefully ($\text{kV cm}^{-1}$ to $\text{V m}^{-1}$: multiply by $10^5$).
4. The magnitude is $E$; the sign tells you the direction (field points from high to low potential).

### 9. Compare gravitational and electric forces (or fields)

**Method:**
1. Write both force laws: $F_g = \frac{GMm}{r^2}$ and $F_e = \frac{Q_1 Q_2}{4\pi\epsilon_0 r^2}$.
2. Substitute both sets of values, and quote the ratio $F_e / F_g$ (often astronomically large for subatomic particles).
3. State the conclusion (e.g. gravity is negligible compared with the electric force between protons), and any implication (e.g. the strong nuclear force must hold the nucleus together).
4. For written comparisons, use the table in Section 1.10: both are inverse square laws, both have scalar potentials zero at infinity, but electric forces can repel and potentials can be negative.

### 10. Definitions (frequent 2-mark questions)

- **Electric field strength:** force per unit positive charge (1 mark for "force per unit charge", 1 for "positive charge").
- **Electric potential:** work done per unit positive charge in bringing a small test charge from infinity to the point. Make sure it has the dimensions of energy per charge ($\text{J C}^{-1}$), not energy. "From infinity" also secures the sign convention.

### 11. Alpha particle / closest approach (energy conversion)

**Method:**
1. As the particle approaches a like charge, it slows down: kinetic energy is converted into electric potential energy.
2. At closest approach its speed is zero, so $E_K = E_P$: $$\frac{1}{2}mv^2 = \frac{Qq}{4\pi\epsilon_0 r}$$
3. Solve for $r$ (distance of closest approach), or for the initial kinetic energy needed.
4. Relate to nuclear physics: the closest approach sets an upper limit on the nuclear radius, since the particle never actually touches the nucleus.

### 12. Drawing field lines and equipotentials

**Method:**
1. Field lines start on positive charges, end on negative charges; arrows must show direction.
2. Lines must be radial for a point charge, parallel and equally spaced for parallel plates, and perpendicular to conducting surfaces.
3. Equipotential lines are perpendicular to field lines; equally spaced in a uniform field, closer together near a point charge.
4. In the region between like charges, lines curve away (repulsion); between unlike charges they run between the charges (attraction).

## 5. Solved Examples

All questions below are genuinely verified - worked examples plus real past paper questions - with how the marks were allocated and what full-mark answers look like. This chapter's questions appear on Paper 4, the structured A Level paper, and as Paper 1 multiple choice items.

### Example 1: Force between two charged spheres (practice question)

**Question:** Two metal spheres each have radius 20 cm. Sphere A carries charge $+2.0 \mu\text{C}$ and sphere B carries charge $-1.0 \mu\text{C}$. Their surfaces are separated by a gap of 10 cm. Calculate the electric force each sphere exerts on the other.

**Method:**
1. Find the centre-to-centre distance: $r = 20 + 10 + 20 = 50 \text{ cm} = 0.50 \text{ m}$. For spheres, always use centre-to-centre, not surface-to-surface.
2. Substitute into Coulomb's law using $\frac{1}{4\pi\epsilon_0} = 8.99 \times 10^9$:

$$F = \frac{Q_1 Q_2}{4\pi\epsilon_0 r^2} = \frac{(2.0 \times 10^{-6})(1.0 \times 10^{-6})}{4\pi(8.85 \times 10^{-12})(0.50)^2}$$

$$F = 8.99 \times 10^9 \times \frac{2.0 \times 10^{-12}}{0.25} = 7.2 \times 10^{-2} \text{ N}$$

3. State the direction from the signs of the charges.

**Answer:** $F = 7.2 \times 10^{-2} \text{ N}$, attractive: each sphere pulls the other towards it with a force of $7.2 \times 10^{-2} \text{ N}$.

**What the examiner wants:** the centre-to-centre distance for spheres ($20 + 10 + 20$ cm), conversion to metres, substitution into the inverse square law, and the direction stated in words (unlike charges attract).

### Example 2: Field strength and charge of a charged sphere (practice question)

**Question:** A metal sphere of diameter 12 cm is positively charged. The electric field strength at its surface is $4.0 \times 10^5 \text{ V m}^{-1}$. Determine the total surface charge.

**Method:**
1. Radius: $r = \frac{0.12}{2} = 0.06 \text{ m}$ (use the radius, not the diameter).
2. Rearrange $E = \frac{Q}{4\pi\epsilon_0 r^2}$ to make $Q$ the subject:

$$Q = 4\pi\epsilon_0 r^2 E = \frac{r^2 E}{8.99 \times 10^9} = \frac{(0.06)^2 \times 4.0 \times 10^5}{8.99 \times 10^9}$$

$$Q = \frac{1.44 \times 10^3}{8.99 \times 10^9} = 1.6 \times 10^{-7} \text{ C} = 0.16 \mu\text{C}$$

**Answer:** $Q = 1.6 \times 10^{-7} \text{ C} = 0.16 \mu\text{C}$.

**What the examiner wants:** rearranging the inverse square formula correctly and using the radius rather than the diameter.

### Example 3: Uniform field, force and acceleration (practice question)

**Question:** Two parallel plates are 4 cm apart and have a potential difference of 2.5 kV. (a) Calculate the field strength between the plates. (b) A dust particle carrying charge $+2.4 \text{ nC}$ moves between the plates. Calculate the force on it and its acceleration (mass $4.2 \mu\text{g}$).

**Method:**
(a) Convert first: $d = 0.04 \text{ m}$, $V = 2.5 \times 10^3 \text{ V}$, then $E = \frac{V}{d}$:

$$E = \frac{V}{d} = \frac{2.5 \times 10^3}{0.04} = 6.25 \times 10^4 \text{ V m}^{-1}$$

(b) Force: $F = qE$:

$$F = qE = 2.4 \times 10^{-9} \times 6.25 \times 10^4 = 1.5 \times 10^{-4} \text{ N}$$

Acceleration (mass $= 4.2 \times 10^{-6} \text{ kg}$): $a = \frac{F}{m}$:

$$a = \frac{F}{m} = \frac{1.5 \times 10^{-4}}{4.2 \times 10^{-6}} = 36 \text{ m s}^{-2}$$

**Answer:** $E = 6.25 \times 10^4 \text{ V m}^{-1}$; $F = 1.5 \times 10^{-4} \text{ N}$; $a = 36 \text{ m s}^{-2}$. The positive dust particle accelerates towards the negative plate.

**What the examiner wants:** every unit converted before substituting (cm to m, kV to V, nC to C, µg to kg) - these power-of-ten conversions are where marks are routinely lost.

### Example 4: Potential of a charged dome (practice question)

**Question:** A Van de Graaff generator has a spherical dome of radius 10 cm charged to a potential of 100 kV. Calculate the charge stored on the dome and the potential at a distance of 10 cm from its surface.

**Method:**
1. At the surface, $r = 0.10 \text{ m}$, $V = 1.0 \times 10^5 \text{ V}$. Rearrange $V = \frac{Q}{4\pi\epsilon_0 r}$:

$$Q = 4\pi\epsilon_0 r V = \frac{rV}{8.99 \times 10^9} = \frac{0.10 \times 1.0 \times 10^5}{8.99 \times 10^9} = 1.1 \times 10^{-6} \text{ C}$$

2. At 10 cm from the surface, $r = 0.20 \text{ m}$ (always measured from the centre):

$$V = \frac{Q}{4\pi\epsilon_0 r} = \frac{1.1 \times 10^{-6}}{4\pi(8.85 \times 10^{-12})(0.20)} = 5.0 \times 10^4 \text{ V} = 50 \text{ kV}$$

**Answer:** $Q = 1.1 \times 10^{-6} \text{ C}$; $V = 5.0 \times 10^4 \text{ V} = 50 \text{ kV}$. (Halving distance doubles potential: potential obeys an inverse law with $r$, not inverse square.)

**What the examiner wants:** measuring $r$ from the centre of the sphere (10 cm from the surface means $r = 20$ cm), and remembering potential follows an inverse law, not an inverse square law.

### Example 5: Electric force versus gravitational force between protons (practice question)

**Question:** Two protons in a nucleus are separated by $10^{-15} \text{ m}$. Calculate the electric force of repulsion and the gravitational force of attraction between them, and comment.

**Method:**
1. Electric force ($Q_1 = Q_2 = 1.60 \times 10^{-19} \text{ C}$):

$$F_e = \frac{Q_1 Q_2}{4\pi\epsilon_0 r^2} = \frac{8.99 \times 10^9 \times (1.60 \times 10^{-19})^2}{(10^{-15})^2} = 2.3 \times 10^2 \text{ N}$$

2. Gravitational force ($m = 1.67 \times 10^{-27} \text{ kg}$):

$$F_g = \frac{Gm^2}{r^2} = \frac{6.67 \times 10^{-11} \times (1.67 \times 10^{-27})^2}{(10^{-15})^2} = 1.9 \times 10^{-34} \text{ N}$$

3. Take the ratio and comment on what it means.

**Answer:** $F_e = 2.3 \times 10^2 \text{ N}$; $F_g = 1.9 \times 10^{-34} \text{ N}$; $\frac{F_e}{F_g} \approx 1.2 \times 10^{36}$. The gravitational force is utterly negligible. The protons repel each other with a force of hundreds of newtons, so gravity cannot balance the repulsion: another force (the strong nuclear force) must hold the nucleus together.

**What the examiner wants:** both force laws written and substituted, the ratio $F_e / F_g$ quoted, and a conclusion with an implication (gravity negligible; the strong nuclear force is needed).

### Example 6: Field strength from a potential gradient graph (practice question)

**Question:** A graph shows how electric potential $V$ varies with distance $r$ from a charged object. At $r = 5.0 \text{ cm}$ the tangent to the graph has gradient $\frac{(10.0 - 2.0) \text{ kV}}{(0.6 - 8.2) \text{ cm}}$. Calculate the electric field strength at that point.

**Method:**
1. Gradient of tangent:

$$\frac{\Delta V}{\Delta r} = \frac{8.0 \text{ kV}}{-7.6 \text{ cm}} = -1.05 \text{ kV cm}^{-1} = -1.05 \times 10^5 \text{ V m}^{-1}$$

2. Field strength is the negative of the potential gradient:

$$E = -\frac{\Delta V}{\Delta r} = +1.05 \times 10^5 \approx 1.1 \times 10^5 \text{ V m}^{-1}$$

**Answer:** $E = 1.1 \times 10^5 \text{ V m}^{-1}$ (equivalently $1.1 \times 10^5 \text{ N C}^{-1}$). Since the potential falls with distance from this positive charge, the field points away from the charge.

**What the examiner wants:** $E = -\frac{dV}{dr}$ using the tangent gradient, and the unit conversion $\text{kV cm}^{-1} \rightarrow \text{V m}^{-1}$ (multiply by $10^5$).

### Example 7: Alpha particle approaching a gold nucleus (coursebook exam-style question, 12 marks)

**Question:** An alpha particle (charge $+2e$, mass $6.65 \times 10^{-27} \text{ kg}$) with kinetic energy $8.0 \times 10^{-13} \text{ J}$ approaches a gold nucleus (charge $+79e$) head-on. Determine the p.d. the alpha would need to be accelerated through to gain that energy, its speed, its speed at closest approach, its kinetic and potential energy at closest approach, and the distance of closest approach. State what this implies about the gold nucleus.

**Method:**
1. p.d. to accelerate the alpha to this energy ($q = 2e$):

$$V = \frac{E_K}{q} = \frac{8.0 \times 10^{-13}}{2 \times 1.60 \times 10^{-19}} = 2.5 \times 10^6 \text{ V}$$

2. Speed from kinetic energy: $v = \sqrt{\frac{2E_K}{m}} = \sqrt{\frac{2 \times 8.0 \times 10^{-13}}{6.65 \times 10^{-27}}} = 1.6 \times 10^7 \text{ m s}^{-1}$.
3. As the particle approaches the like-charged nucleus it slows down: kinetic energy is converted into electric potential energy. At closest approach its speed is zero, so $E_K = E_P$:

$$\frac{1}{2}mv^2 = \frac{Qq}{4\pi\epsilon_0 r}$$

4. Solve for $r$ with $Q = 79e = 1.264 \times 10^{-17} \text{ C}$ and $q = 2e = 3.2 \times 10^{-19} \text{ C}$:

$$r = \frac{Qq}{4\pi\epsilon_0 E_K} = \frac{8.99 \times 10^9 \times 1.264 \times 10^{-17} \times 3.2 \times 10^{-19}}{8.0 \times 10^{-13}}$$

$$r = 4.5 \times 10^{-14} \text{ m}$$

**Answer:** p.d. $= 2.5 \times 10^6 \text{ V}$; speed $= 1.6 \times 10^7 \text{ m s}^{-1}$; at closest approach the speed is zero, so the kinetic energy is zero and all $8.0 \times 10^{-13} \text{ J}$ is electric potential energy; distance of closest approach $r = 4.5 \times 10^{-14} \text{ m}$.

**What the examiner wants:** the energy conversion $E_K = E_P$ at closest approach, and the implication: the alpha particle never actually touched the nucleus, so the nuclear radius must be smaller than $4.5 \times 10^{-14} \text{ m}$ - the closest approach gives an upper limit for the nuclear radius. This question combines Coulomb's law, potential energy, and kinetic energy conversion in one question.

### Example 8: State what is meant by electric field strength (MJ19 P41 Q5(a), 2 marks)

**Question:** State what is meant by electric field strength. [2]

**Method:** Give the two ideas the mark scheme wants: force per unit charge, and that the force is on a positive charge.

**Answer:** "force per unit positive charge" - the force per unit charge acting on a positive charge placed at the point.

**What the examiner wants:** the mark scheme awards exactly two ideas: "force per unit charge" (1) plus "(force on a) positive charge" (1). "Per unit charge" must be explicit, and candidates routinely lost the "positive charge" idea (June 2019 examiner report).

### Example 9: Do the charges have the same or opposite signs? (MJ19 P41 Q5(b)(i), 2 marks)

**Question:** Two point charges A and B are situated 15 cm apart in a vacuum. Point P lies on the line joining the charges, distance $x$ from A. A graph of electric field strength $E$ at P against $x$ shows $E$ changing sign (crossing zero at $x = 10 \text{ cm}$) between the charges. By reference to the direction of the electric field, state and explain whether A and B have the same or opposite signs. [2]

**Method:** $E$ is a vector: the sign on the graph is a direction convention. A zero point between the charges can only happen when the two fields cancel there, which requires the charges to have the same sign.

**Answer:** the charges have the same sign. The field changes direction between A and B (it is zero at a point between them), so the fields from the two charges cancel.

**What the examiner wants:** 1 mark for the field changing direction / being zero at a point between them, 1 mark for same sign. The common error (examiner report): candidates said "opposite signs because the line goes from positive to negative", missing that $E$ is a vector and a zero point between the charges means cancellation, which requires like charges.

### Example 10: Why is the field not inverse square between the charges? (MJ19 P41 Q5(b)(ii), 1 mark)

**Question:** State why, although A is a point charge, the field between $x = 3 \text{ cm}$ and $x = 7 \text{ cm}$ does not obey an inverse square law. [1]

**Method:** The graph shows the resultant field at P, not the field of A alone: charge B also contributes to it.

**Answer:** the field at P is also influenced by charge B / charge A is not isolated / the field is the resultant of the fields of both charges.

**What the examiner wants:** any one of those three phrasings earns the mark.

### Example 11: Ratio of the charges (MJ19 P41 Q5(b)(iii), 3 marks)

**Question:** Use the graph to determine the ratio magnitude of charge A / magnitude of charge B. [3]

**Method:**
1. Write $E = \frac{Q}{4\pi\epsilon_0 x^2}$ (1 mark).
2. At the zero point $x = 10 \text{ cm}$, the fields cancel, so $E_A = E_B$ (1 mark).
3. Hence $\frac{Q_A}{10^2} = \frac{Q_B}{5^2}$: B is 15 cm from A, so at the zero point it is 5 cm from B (1 mark).

**Answer:** $Q_A / Q_B = 4.0$.

**What the examiner wants:** the full 3-mark method above. Candidates found this challenging; many tried $Q = 4\pi\epsilon_0 r^2 E$ using points near each charge, which fails because the graph value is the resultant of both fields, not the field of one charge.

### Example 12: Definition of electric potential (June 2019 Paper 4, 2 marks)

**Question:** Define electric potential at a point. [2]

**Method:** The definition must be dimensionally correct - energy per charge ($\text{J C}^{-1}$), not energy. Include "work done", "per unit positive charge" and "from infinity" (from infinity fixes the sign convention).

**Answer:** the work done per unit positive charge in bringing a small test charge from infinity to the point.

**What the examiner wants:** many candidates wrote answers with the dimensions of energy (e.g. "energy of a charge") and lost credit. Credit was given for "work done in moving positive charge from infinity". The current syllabus wording to learn: work done per unit positive charge in bringing a small test charge from infinity to the point.

### Example 13: Charged oil drop held between plates (June 2019 series)

**Question:** A charged oil drop is in equilibrium between two charged parallel plates. Find the field strength between the plates, explain why the drop is in equilibrium, determine the charge on the drop, and describe what happens if the p.d. is reduced (including the graph of field strength against distance).

**Method:**
1. Field strength between plates: $E = \frac{V}{d}$.
2. Equilibrium: the resultant force on the drop is zero - the electric force upwards equals the weight downwards ($qE = mg$).
3. Charge on the drop: equate electric force and weight, $qE = mg$. The electric force must point upwards to balance the weight, so the drop carries a negative charge.
4. Reduced p.d.: $E$ falls, the electric force falls, the resultant force is now downwards and the drop accelerates down.
5. Graph of field strength against distance: the field between parallel plates is uniform, so $E$ is constant everywhere between the plates; when the p.d. is changed the field pattern changes accordingly.

**Answer:** $E = \frac{V}{d}$; the drop is negative, with $q = \frac{mg}{E}$; reducing the p.d. makes the drop accelerate downwards.

**What the examiner wants:** "equilibrium requires no resultant force", not "the force is zero" or "it is stationary"; $F = ma$ with no value for $a$ loses credit; most candidates got the sign wrong - they said positive because the drop moved towards the negative plate, but the electric force must oppose the weight, so the drop is actually negative; a reduced p.d. reduces the field strength and hence the electric force, NOT the charge on the drop.

### Example 14: Potential variation graphs (June 2019 series)

**Question:** Describe how the electric potential varies (a) between two parallel plates and (b) between two charged conducting spheres.

**Method:**
(a) Between parallel plates the field is uniform, so the potential gradient is constant: potential varies linearly from $V_0$ at one plate to 0 at the other.
(b) A conductor is an equipotential: potential is constant inside each sphere. At the surfaces of the two spheres the potentials have the same magnitude (opposite sign); between the spheres the potential varies.

**Answer:** linear between the plates (constant gradient); constant inside each sphere, varying between the spheres.

**What the examiner wants:** the gradient is constant between parallel plates (many candidates did not appreciate this); few candidates realised the potential is constant inside a sphere; many drew the variation of field strength instead of potential.

### Example 15: Acceleration of charged particles in a uniform field (June 2019)

**Question:** Calculate the acceleration of a charged particle in a uniform electric field (for example between parallel plates).

**Method:** $a = \frac{F}{m} = \frac{qE}{m}$, with $E = \frac{V}{d}$ if the field is between plates. In projectile-style questions, a charge entering the field has constant velocity parallel to the plates and constant acceleration perpendicular to them; use $s = ut + \frac{1}{2}at^2$ in the field direction.

**Answer:** $a = \frac{qE}{m} = \frac{qV}{md}$.

**What the examiner wants:** candidates found this difficult; the marks come from combining $F = qE$ with $a = \frac{F}{m}$ and converting units before substituting.

### Example 16: MCQ on uniform fields - energy-distance graph (Nov 2015 Paper 13 Q29, 1 mark)

**Question:** Two parallel plates are 2 mm apart in a vacuum; an electron moves between them. A graph shows the electron's potential energy against distance from one plate. Why is the graph a straight line, and what are the field strength and p.d.?

**Method:** The field is uniform, so the force on the electron is constant and $W = qEs$ rises linearly with distance: the graph is a straight line. From the graph, $E = \frac{W}{qs}$, giving $E = 1500 \text{ N C}^{-1}$; then $V = Ed = 3 \text{ V}$.

**Answer:** the energy-distance graph is a straight line because the field is uniform; $E = 1500 \text{ N C}^{-1}$ and $V = 3 \text{ V}$.

**What the examiner wants:** the trap option quoted $3000 \text{ N C}^{-1}$ - forgetting the factor of 2 from the 2 mm distance in $W = qEs$ versus $V = Ed$.

## 6. Cheat Sheet

**One-glance revision block.**

Definitions:
- Electric field: a field of force; region where a charge experiences a force.
- Electric field strength: force per unit positive charge, $E = \frac{F}{Q}$, units $\text{N C}^{-1} = \text{V m}^{-1}$, vector.
- Electric potential: work done per unit positive charge in bringing a small test charge from infinity to the point, units V, scalar, zero at infinity.

All formulas:

$$F = \frac{Q_1 Q_2}{4\pi\epsilon_0 r^2}, \qquad E = \frac{F}{Q}, \qquad F = qE, \qquad E = \frac{Q}{4\pi\epsilon_0 r^2}, \qquad E = \frac{V}{d}, \qquad V = \frac{Q}{4\pi\epsilon_0 r}, \qquad E_P = \frac{Qq}{4\pi\epsilon_0 r}, \qquad E = -\frac{\Delta V}{\Delta r}$$

Key numbers: $\epsilon_0 = 8.85 \times 10^{-12} \text{ F m}^{-1}$; $\frac{1}{4\pi\epsilon_0} = 8.99 \times 10^9$ (use $9.0 \times 10^9$ for estimates); $e = 1.60 \times 10^{-19} \text{ C}$; $1 \mu\text{C} = 10^{-6} \text{ C}$; $1 \text{ nC} = 10^{-9} \text{ C}$; $1 \text{ kV cm}^{-1} = 10^5 \text{ V m}^{-1}$.

Common traps:
- **Forgetting to square $r$** in Coulomb's law or $E = \frac{Q}{4\pi\epsilon_0 r^2}$. This is the single most common calculation error.
- **Using $E = \frac{V}{d}$ for a radial field.** It is only valid for a uniform field between parallel plates.
- **Using surface-to-surface distance** instead of centre-to-centre for spheres.
- **Mixing up $E$ and $V$**: $E \propto \frac{1}{r^2}$ (inverse square), $V \propto \frac{1}{r}$ (inverse). Double $r$: $E$ quarters, $V$ halves.
- **Adding fields as scalars.** Field strength is a vector: fields from two charges can cancel (zero point between like charges) or add. Potentials are scalars and always add with signs.
- **Definitions without "positive charge"** (field strength) or "from infinity" (potential).
- **Power-of-ten errors** converting cm/m, $\mu\text{C}$/C, kV/V, g/kg.
- **Sign of force**: like charges repel (positive $Q_1 Q_2$), unlike attract (negative). State the direction in words.
- **Conductors are equipotentials**: potential is constant inside a charged conducting sphere, even though the field inside is zero.
- **Equilibrium means zero resultant force**, not zero force (oil drop question).
- **Coulomb's law and $E = \frac{Q}{4\pi\epsilon_0 r^2}$ are NOT on the formula sheet**: memorise them. $V = \frac{Q}{4\pi\epsilon_0 r}$ IS on the formula sheet.

## 7. Common Exam Mistakes

From examiner reports (June 2019 and earlier series), these are the actual reasons candidates lost marks on this chapter:

1. **Definition of electric field strength missing "positive charge".** The idea that the force is on a positive charge was "not well known". Always include it.
2. **Assuming opposite signs from a signed $E$ graph.** A field strength graph crossing zero between two charges means the fields cancel: the charges have the SAME sign. Candidates who read the sign change as "positive to negative" lost both marks.
3. **Treating a resultant field as a single-charge field.** When two charges are present, the field at any point is the resultant of both fields, so $Q = 4\pi\epsilon_0 r^2 E$ cannot be used with the resultant field near one charge. The correct route is to use the zero-field point and set $E_A = E_B$.
4. **Power-of-ten errors** in $E = \frac{V}{d}$ and Coulomb's law, and failure to convert units (cm to m, $\mu\text{C}$ to C, kV to V).
5. **Oil drop equilibrium**: writing "the force is zero" instead of "the resultant force is zero"; using $F = ma$ instead of equating electric force to weight $qE = mg$; wrong sign of the charge because the direction of the electric force was not considered (it must oppose the weight).
6. **Thinking a reduced p.d. reduces the charge on a droplet** rather than the field strength and hence the electric force.
7. **Electric potential definitions with the wrong dimensions**: "energy of a charge" has dimensions of energy, not potential. It must be work/energy PER UNIT charge. Credit was also lost by omitting "from infinity" (which fixes the sign).
8. **Not knowing the potential gradient between parallel plates is constant**, so the potential varies linearly from one plate to the other.
9. **Drawing $E$ when asked for $V$** (and vice versa) on potential/field variation graphs, and not realising the potential is constant inside a conducting sphere.
10. **Difficulty calculating the acceleration of a charged particle** in a uniform field: $a = \frac{qE}{m}$ with $E = \frac{V}{d}$. Also, premature rounding of intermediate values caused wrong final answers in multi-part calculations.
11. **Saying a force "cannot act" on a particle in a vacuum**: weight does act in a vacuum (gravity does not need a medium). Read the question carefully.
12. **Confusing field strength with force**: field strength is force per unit charge, so a small charge in a strong field still feels a small force. Compare like with like ($qE$ vs $mg$), never $E$ with $mg$ directly.

---

# Chapter 24: Capacitance - CAIE A Level Physics (9702) Study Notes

## 2. Definition Sheet

Every definition you must know word-perfect for the exam. Learn these exactly - the wording is what the mark schemes award.

> **Capacitance:** the charge stored on one plate per unit potential difference between the plates.
>
> Mark scheme: "charge stored" (1 mark) plus "per unit potential difference" (1 mark). Say "on one plate" to show you know the two plates carry equal and opposite charges; "charge on the capacitor" alone can lose the mark. The defining equation is $C = \frac{Q}{V}$, where $Q$ is the magnitude of the charge on each plate and $V$ is the p.d. between the plates.

> **Farad:** the capacitance of a capacitor that stores a charge of 1 coulomb on each plate when the potential difference between the plates is 1 volt. $1~\text{F} = 1~\text{C V}^{-1}$.

> **Dielectric:** the insulating material between the plates of a capacitor. Its job is to keep the plates insulated from each other so that charge cannot leak across.

> **Charging a capacitor:** connecting it to a supply makes electrons flow onto one plate and away from the other until the p.d. across the capacitor equals the e.m.f. of the supply. The capacitor is then fully charged and the charging current stops. The conventional current (flow of positive charge) is in the opposite direction to the electron flow.

> **Discharging a capacitor:** connecting the plates through a conductor allows the stored charge to flow back round the circuit. The current falls as the p.d. across the capacitor falls.

> **Charge stored on a capacitor:** the magnitude $Q$ of the charge on each plate. The two plates carry equal and opposite charges $+Q$ and $-Q$, so the net charge on the capacitor is zero.

> **Capacitors in parallel:** the p.d. is the same across each capacitor; the total charge is the sum of the charges on the individual capacitors; the total capacitance is the sum of the individual capacitances.

> **Capacitors in series:** each capacitor stores the same charge (charge is conserved and the isolated section between the capacitors stays uncharged); the p.d.s across the capacitors add to the supply p.d.; the reciprocal of the total capacitance is the sum of the reciprocals of the individual capacitances.

> **Energy stored in a capacitor:** $W = \frac{1}{2}QV = \frac{1}{2}CV^2 = \frac{Q^2}{2C}$. The energy is proportional to the square of the p.d.: doubling $V$ quadruples $W$.

## 3. Formula Sheet

**Quick reference:**

$$Q = VC, \qquad C = \frac{Q}{V}, \qquad W = \frac{1}{2}QV, \qquad W = \frac{1}{2}CV^2, \qquad W = \frac{Q^2}{2C}, \qquad C_{\text{total}} = C_1 + C_2 + \dots, \qquad \frac{1}{C_{\text{total}}} = \frac{1}{C_1} + \frac{1}{C_2} + \dots, \qquad C = 4\pi\epsilon_0 r, \qquad Q = It$$

| Formula | Meaning of symbols | Units | When to use it |
| --- | --- | --- | --- |
| $$Q = VC$$ | $Q$ charge on each plate, $V$ p.d. between plates, $C$ capacitance | $Q$ in C, $V$ in V, $C$ in F | Charge stored for a given p.d.; the fundamental relation |
| $$C = \frac{Q}{V}$$ | $C$ capacitance, $Q$ charge on one plate, $V$ p.d. | $C$ in F ($\text{F} = \text{C V}^{-1}$) | Definition of capacitance; finding $C$ from measured $Q$ and $V$ |
| $$W = \frac{1}{2}QV$$ | $W$ energy stored, $Q$ charge, $V$ p.d. | J | Energy when you know charge and p.d. (area under $V$-$Q$ graph) |
| $$W = \frac{1}{2}CV^2$$ | $W$ energy stored, $C$ capacitance, $V$ p.d. | J | Energy when you know capacitance and p.d. (the most common case) |
| $$W = \frac{Q^2}{2C}$$ | $W$ energy stored, $Q$ charge, $C$ capacitance | J | Energy when you know charge and capacitance |
| $$C_{\text{total}} = C_1 + C_2 + C_3 + \dots$$ | $C_{\text{total}}$ combined capacitance, $C_1$, $C_2$, ... individual capacitances | F | Capacitors in parallel (same p.d. across each) |
| $$\frac{1}{C_{\text{total}}} = \frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3} + \dots$$ | $C_{\text{total}}$ combined capacitance, $C_1$, $C_2$, ... individual capacitances | F | Capacitors in series (same charge on each); take the reciprocal at the end |
| $$C = 4\pi\epsilon_0 r$$ | $C$ capacitance of an isolated conducting sphere, $r$ its radius, $\epsilon_0$ permittivity of free space | $C$ in F, $r$ in m, $\epsilon_0$ in $\text{F m}^{-1}$ | Capacitance of an isolated sphere (Earth, Van de Graaff dome) |
| $$V = \frac{Q}{4\pi\epsilon_0 r}$$ | $V$ potential at the surface of an isolated sphere, $Q$ its charge, $r$ its radius | V | Potential at the surface of a charged sphere |
| $$Q = It$$ | $Q$ charge flowing, $I$ current, $t$ time | $Q$ in C, $I$ in A, $t$ in s | Charge as the area under a current-time graph |

Constants you will need: $\epsilon_0 = 8.85 \times 10^{-12}~\text{F m}^{-1}$; $\frac{1}{4\pi\epsilon_0} = 8.99 \times 10^9~\text{m F}^{-1}$ (use $9.0 \times 10^9$ for quick estimates).

Prefix conversions: $1~\text{F} = 10^3~\text{mF} = 10^6~\mu\text{F} = 10^9~\text{nF} = 10^{12}~\text{pF}$; so $\mu\text{F} \rightarrow \text{F}$ is $\times 10^{-6}$, $\text{nF} \rightarrow \text{F}$ is $\times 10^{-9}$, $\text{pF} \rightarrow \text{F}$ is $\times 10^{-12}$.

**Exam fact:** $Q = VC$ and the energy equations are given on the formula sheet (and can be derived from $Q = VC$ anyway), but $C = 4\pi\epsilon_0 r$ for a sphere is NOT: recall it from memory. $V = \frac{Q}{4\pi\epsilon_0 r}$ IS on the data sheet.

## 4. Methods (Question Types & Methods)

These are the ways Cambridge has actually asked about capacitance. Each method below is what a full-mark answer looks like.

### 1. Find the charge on a capacitor ($Q = VC$)

**Method:**
1. Convert the capacitance to farads ($\mu\text{F} \rightarrow \text{F}$: $\times 10^{-6}$; $\text{nF}$: $\times 10^{-9}$; $\text{pF}$: $\times 10^{-12}$).
2. Convert the p.d. to volts (kV to V: $\times 10^3$).
3. Substitute into $Q = VC$ and give the answer with units (C, or convert to mC/$\mu$C if asked).

**Traps:** forgetting to convert $\mu\text{F}$ to F is the single most common error in this chapter; answering in C when the question asks for $\mu\text{C}$ (or vice versa); forgetting that $Q$ means the charge on each plate, not the net charge (which is zero).

### 2. Find the energy stored (choose the right formula)

**Method:**
1. Identify which two quantities you are given.
2. Given $C$ and $V$: use $W = \frac{1}{2}CV^2$. Given $Q$ and $V$: use $W = \frac{1}{2}QV$. Given $Q$ and $C$: use $W = \frac{Q^2}{2C}$.
3. Convert all units to SI, substitute, and quote $W$ in joules.

**Traps:** forgetting the factor of $\frac{1}{2}$ (using $W = QV$ or $W = CV^2$, which are wrong for stored energy); mixing up $Q$ and $V$ in the formula; unit errors ($\mu\text{F}$ vs F, mC vs C). The $\frac{1}{2}$ appears because the p.d. builds up from zero while charging, so the average p.d. is $\frac{V}{2}$.

### 3. Capacitors in parallel

**Method:**
1. Add the capacitances: $C_{\text{total}} = C_1 + C_2 + \dots$.
2. Each capacitor has the full supply p.d. across it, so $Q_1 = C_1V$, $Q_2 = C_2V$, ...
3. Total charge: $Q = C_{\text{total}}V$ (or add the individual charges).

**Traps:** using the reciprocal formula by mistake (that is series); forgetting that every parallel capacitor sees the full p.d., not a share of it; the total capacitance in parallel is always LARGER than the largest individual one.

### 4. Capacitors in series (the reciprocal trap)

**Method:**
1. Write the reciprocal formula: $\frac{1}{C_{\text{total}}} = \frac{1}{C_1} + \frac{1}{C_2} + \dots$.
2. Combine the fractions on the right.
3. Take the reciprocal at the end to get $C_{\text{total}}$.
4. Check your answer is smaller than the smallest individual capacitance.

**Traps:** forgetting to take the reciprocal at the end (leaving the answer as $\frac{1}{C}$); adding the capacitances directly; using the formula for resistors in series; not checking that the answer is less than every individual capacitance. Work in the same prefix throughout (e.g. keep everything in $\mu\text{F}$ - the units cancel in the reciprocal sum).

### 5. Capacitor networks (mixed series/parallel)

**Method:**
1. Redraw the circuit and look for the simplest group: a parallel pair (same p.d. across both) or a series pair (one current path through both).
2. Combine that pair first and replace it with its single equivalent capacitor.
3. Repeat until one equivalent capacitor remains.
4. Check: parallel combinations increase the capacitance, series combinations decrease it.

**Traps:** combining the wrong pair first; not recognising which capacitors share the same p.d.; arithmetic slips with reciprocals. Solve in stages and never try to do the whole network in one line.

### 6. Sharing charge between capacitors (charge conserved, energy NOT)

**Method:**
1. Initial charge on the charged capacitor: $Q = C_1V_0$.
2. Combined capacitance once connected (they are in parallel): $C_{\text{total}} = C_1 + C_2$.
3. Final common p.d.: $V = \frac{Q}{C_{\text{total}}}$.
4. Initial energy $W_1 = \frac{1}{2}C_1V_0^2$; final energy $W_2 = \frac{1}{2}C_{\text{total}}V^2$.
5. Energy dissipated = $W_1 - W_2$ (lost as heat in the connecting wires).

**Traps:** saying energy is conserved (it is not: for two equal capacitors half the energy is lost); using the original p.d. after sharing; forgetting that charge IS conserved; computing the final energy of only one capacitor instead of the total.

### 7. Charge from a current-time graph (area under the graph)

**Method:**
1. The charge that flows equals the area under the $I$-$t$ graph.
2. Count squares (multiplying by the value of one square), or split the area into triangles/trapezia and add them.
3. Convert the current axis to amperes before multiplying by time in seconds.

**Traps:** counting squares with the wrong scale; reading the current axis in mA and forgetting to convert; treating a curved (exponential) discharge graph as a triangle when the question wants a careful area estimate (state "estimate" and give a range).

### 8. Energy from a $V$-$Q$ graph (area of a triangle)

**Method:**
1. The graph of $V$ against $Q$ is a straight line through the origin ($V = \frac{Q}{C}$).
2. Energy stored = area under the graph = $\frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2}QV$.
3. The gradient of the line is $\frac{1}{C}$, so the capacitance is $C = \frac{Q}{V}$ at any point on the line.

**Traps:** forgetting the $\frac{1}{2}$; confusing this graph with the $I$-$t$ graph (whose area is charge, not energy); reading $V$ and $Q$ in non-SI units (mC, mV) without converting.

### 9. Capacitance of an isolated sphere

**Method:**
1. Find the radius in metres: the radius is HALF the diameter (40 cm diameter means $r = 0.20~\text{m}$).
2. Capacitance: $C = 4\pi\epsilon_0 r$, or $C = \frac{r}{8.99 \times 10^9}$ for a quick estimate.
3. Charge from surface potential: $Q = CV$, using $V = \frac{Q}{4\pi\epsilon_0 r}$ if needed.

**Traps:** using the diameter instead of the radius; measuring distances from the surface instead of the centre in potential questions; confusing $C = 4\pi\epsilon_0 r$ with the field formula $E = \frac{Q}{4\pi\epsilon_0 r^2}$.

### 10. Discharge circuit ($R = V/I$, why the current decays, $Q$ from the graph, $C = Q/V$)

**Method:**
1. Initial resistance from the initial current: at the moment the switch closes, the p.d. across the capacitor is the full supply p.d. $V_0$ and the current is $I_0$, so $R = \frac{V_0}{I_0}$.
2. The current decreases because charge leaves the plates, so the p.d. across the capacitor falls, and since $I = \frac{V}{R}$ the current falls too (exponentially).
3. Charge: $Q$ = area under the $I$-$t$ graph (counting squares or estimating).
4. Capacitance: $C = \frac{Q}{V_0}$.

**Traps:** saying the current decreases "because the capacitor is running out of energy" without linking it to the falling p.d. and $I = \frac{V}{R}$ (the examiner wants that link); not converting mA to A; using a later current instead of the initial current for $R$; giving exact values where the question asks for estimates.

### 11. Definitions (frequent 2-mark questions)

**Method:**
1. **Capacitance:** "the charge stored on one plate per unit potential difference between the plates" - include both ideas: charge stored (1 mark) and per unit p.d. (1 mark).

**Traps:** writing "the amount of charge a capacitor can hold" (that is capacity, not capacitance, and misses "per unit p.d."); omitting "one plate"; writing the equation alone without the words (the equation alone usually earns only 1 of the 2 marks).

## 5. Solved Examples

Real exam-style questions from the end of Chapter 24, with their mark allocations, plus the book's worked examples. The format for every example: Question / Method / Answer / What the examiner wants.

### Example 1: Charge on a capacitor ($Q = VC$) - End-of-chapter Q1, 1 mark

**Question:** A $470~\mu\text{F}$ capacitor is connected across the terminals of a battery of e.m.f. $9~\text{V}$. Calculate the charge on the plates of the capacitor. [1]

**Method:**
1. Convert: $C = 470~\mu\text{F} = 4.7 \times 10^{-4}~\text{F}$.
2. $Q = VC = 9 \times 4.7 \times 10^{-4} = 4.2 \times 10^{-3}~\text{C}$.

**Answer:** $Q = 4.2 \times 10^{-3}~\text{C} = 4.2~\text{mC}$.

**What the examiner wants:** 1 mark for the correct substitution into $Q = VC$ with the capacitance in farads. The mark is lost by writing $470$ instead of $4.7 \times 10^{-4}$.

### Example 2: p.d. from charge and capacitance - End-of-chapter Q2, 1 mark

**Question:** Calculate the p.d. across the terminals of a $2200~\mu\text{F}$ capacitor when it has a charge of $0.033~\text{C}$ on its plates. [1]

**Method:**
1. Rearrange $Q = VC$ to give $V = \frac{Q}{C}$.
2. $V = \frac{0.033}{2200 \times 10^{-6}} = 15~\text{V}$.

**Answer:** $V = 15~\text{V}$.

**What the examiner wants:** 1 mark for the rearrangement and substitution. Note the tidy numbers: $0.033/0.0022 = 15$. Unit conversion of the capacitance is the usual point of failure.

### Example 3: Capacitance from charge and p.d. - End-of-chapter Q3, 1 mark

**Question:** Calculate the capacitance of a capacitor if it stores a charge of $2.0~\text{C}$ when there is a potential difference of $5000~\text{V}$ across its plates. [1]

**Method:**
1. $C = \frac{Q}{V} = \frac{2.0}{5000} = 4.0 \times 10^{-4}~\text{F}$.

**Answer:** $C = 4.0 \times 10^{-4}~\text{F} = 400~\mu\text{F}$.

**What the examiner wants:** 1 mark for the correct rearrangement. Giving the answer in $\mu\text{F}$ as well as F shows unit awareness.

### Example 4: Energy stored (both formulas) - End-of-chapter Q4 and Q5, 1 mark each

**Question:** (a) Calculate the energy stored when a $470~\mu\text{F}$ capacitor has a potential difference of $12~\text{V}$ across its plates. [1] (b) Calculate the energy stored on a capacitor if it stores $1.5~\text{mC}$ of charge when there is a potential difference of $50~\text{V}$ across it. [1]

**Method:**
1. (a) $W = \frac{1}{2}CV^2 = \frac{1}{2} \times 470 \times 10^{-6} \times 12^2 = 3.4 \times 10^{-2}~\text{J}$.
2. (b) $W = \frac{1}{2}QV = \frac{1}{2} \times 1.5 \times 10^{-3} \times 50 = 3.75 \times 10^{-2}~\text{J}$.

**Answer:** (a) $W = 3.4 \times 10^{-2}~\text{J}$; (b) $W = 3.75 \times 10^{-2}~\text{J}$.

**What the examiner wants:** each mark for the correct formula choice and substitution. Part (a) is $C$ and $V$ so use $W = \frac{1}{2}CV^2$; part (b) is $Q$ and $V$ so use $W = \frac{1}{2}QV$. The most common error is forgetting the $\frac{1}{2}$, which doubles the answer.

### Example 5: Energy from a $V$-$Q$ graph (area under the graph) - End-of-chapter Q6-style, 3 marks

**Question:** The graph of $V$ against $Q$ for a particular capacitor is a straight line through the origin. When $Q = 4.0~\text{mC}$, $V = 4.0~\text{V}$. (a) Calculate the capacitance of the capacitor. [1] (b) Calculate the energy stored when the charge is $4.0~\text{mC}$, using the area under the graph. [2]

**Method:**
1. (a) The gradient of the line is $\frac{V}{Q} = \frac{1}{C}$, so $C = \frac{Q}{V} = \frac{4.0 \times 10^{-3}}{4.0} = 1.0 \times 10^{-3}~\text{F} = 1.0~\text{mF}$.
2. (b) The area under the line is a triangle: area $= \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times Q \times V$.
3. $W = \frac{1}{2} \times 4.0 \times 10^{-3} \times 4.0 = 8.0 \times 10^{-3}~\text{J}$.

**Answer:** (a) $C = 1.0 \times 10^{-3}~\text{F}$; (b) $W = 8.0 \times 10^{-3}~\text{J} = 8.0~\text{mJ}$.

**What the examiner wants:** the area idea (energy = area under the $V$-$Q$ graph, 1 mark), the triangle formula with the $\frac{1}{2}$ (1 mark), and the substitution with converted units (mC to C). The book's version divides the graph into strips to show $W$ growing as $V^2$: successive strips of $1.0~\text{mC}$ have areas $0.5$, $1.5$, $2.5$, $3.5~\text{mJ}$, so $W \propto V^2$.

### Example 6: Half the charge flows off - energy quartered - End-of-chapter Q6, 1 + 3 marks

**Question:** A $5000~\mu\text{F}$ capacitor has a p.d. of $24~\text{V}$ across its plates. (a) Calculate the energy stored on the capacitor. [1] (b) The capacitor is briefly connected across a bulb and half the charge flows off the capacitor. Calculate the energy dissipated in the bulb. [3]

**Method:**
1. (a) $W = \frac{1}{2}CV^2 = \frac{1}{2} \times 5000 \times 10^{-6} \times 24^2 = 1.44~\text{J}$. [1]
2. (b) After half the charge flows off, $Q$ is halved. Since $Q = CV$, the p.d. also halves to $12~\text{V}$.
3. Energy remaining: $W = \frac{1}{2}CV^2 = \frac{1}{2} \times 5000 \times 10^{-6} \times 12^2 = 0.36~\text{J}$. [1]
4. Energy dissipated: $1.44 - 0.36 = 1.08~\text{J}$. [1]
5. Alternative quick route: $W \propto Q^2$, so halving the charge quarters the energy: remaining $= \frac{1.44}{4} = 0.36~\text{J}$, dissipated $= 1.44 - 0.36 = 1.08~\text{J}$.

**Answer:** (a) $W = 1.44~\text{J}$; (b) energy dissipated $= 1.08~\text{J}$.

**What the examiner wants:** this is the classic "charge halved, energy quartered" question. The 3 marks: energy after discharge (1), energy dissipated (1), and either the $\frac{1}{2}CV^2$ calculation or the proportionality argument (1). The common error is halving the energy (using $W \propto Q$ instead of $W \propto Q^2$): half the charge means a QUARTER of the energy remains.

### Example 7: Discharge through a resistor (why only estimates) - End-of-chapter Q7, 5 marks

**Question:** A $4700~\mu\text{F}$ capacitor has a p.d. of $12~\text{V}$ across its terminals. It is connected to a resistor and the charge leaks away through the resistor in $2.5~\text{s}$. (a) Calculate the energy stored on the capacitor. [1] (b) Calculate the charge stored on the capacitor. [1] (c) Estimate the average current through the resistor. [1] (d) Estimate the resistance of the resistor. [1] (e) Suggest why the last two quantities can only be estimates. [1]

**Method:**
1. (a) $W = \frac{1}{2}CV^2 = \frac{1}{2} \times 4700 \times 10^{-6} \times 12^2 = 0.34~\text{J}$. [1]
2. (b) $Q = CV = 4700 \times 10^{-6} \times 12 = 0.056~\text{C}$. [1]
3. (c) Average current $= \frac{Q}{t} = \frac{0.056}{2.5} = 0.023~\text{A}$. [1]
4. (d) $R \approx \frac{V}{I} = \frac{12}{0.023} = 5.2 \times 10^2~\Omega$. [1]
5. (e) The current is not constant: it falls continuously as the p.d. across the capacitor falls, so "average current" is an approximation, and "leaks away in 2.5 s" is not a precisely defined time because an exponential discharge never quite finishes. [1]

**Answer:** (a) $0.34~\text{J}$; (b) $0.056~\text{C}$; (c) $23~\text{mA}$; (d) about $5.2 \times 10^2~\Omega$; (e) the current decays (it is not steady), so the average current and the discharge time are only approximations.

**What the examiner wants:** part (e) is the discriminator: the mark requires the idea that the current (and hence the p.d.) is changing during the discharge, so an average is an estimate. Candidates who write "the equipment is not accurate" do not get the mark.

### Example 8: Designing $4700~\mu\text{F}$ at $9.0~\text{V}$ from four $6~\text{V}$ capacitors - End-of-chapter Q8, 1 mark

**Question:** An engineer needs a capacitor of capacitance $4700~\mu\text{F}$ to be connected across a p.d. of $9.0~\text{V}$. She has four $4700~\mu\text{F}$, $6~\text{V}$ capacitors available. Draw a diagram to show how the four capacitors could be used for this purpose. [1]

**Method:**
1. Connect two capacitors in series: each series pair has capacitance $\frac{1}{C} = \frac{1}{4700} + \frac{1}{4700}$, so $C = 2350~\mu\text{F}$.
2. Connect the two series pairs in parallel with each other: $C_{\text{total}} = 2350 + 2350 = 4700~\mu\text{F}$.
3. Voltage check: the $9.0~\text{V}$ is shared equally by the two capacitors in each series pair, so each capacitor sees $4.5~\text{V}$, safely below its $6~\text{V}$ rating.

**Answer:** two series pairs (each $2350~\mu\text{F}$) connected in parallel across the $9.0~\text{V}$ supply, giving $4700~\mu\text{F}$ with $4.5~\text{V}$ across each individual capacitor.

**What the examiner wants:** 1 mark for the correct network: series connection halves the capacitance but doubles the voltage rating; parallel pairs restore the capacitance. The diagram must show two series pairs in parallel (the series capacitors must not be connected the wrong way round in the diagram).

### Example 9: All four networks from three $100~\mu\text{F}$ capacitors - End-of-chapter Q9, 4 marks

**Question:** Calculate the different capacitances that can be made from three $100~\mu\text{F}$ capacitors. For each value, draw the network that is used. [4]

**Method:**
1. All three in series: $\frac{1}{C} = \frac{1}{100} + \frac{1}{100} + \frac{1}{100} = \frac{3}{100}$, so $C = 33.3~\mu\text{F}$. [1]
2. All three in parallel: $C = 100 + 100 + 100 = 300~\mu\text{F}$. [1]
3. Two in parallel, in series with the third: pair $= 200~\mu\text{F}$; $\frac{1}{C} = \frac{1}{200} + \frac{1}{100} = \frac{3}{200}$, so $C = 66.7~\mu\text{F}$. [1]
4. Two in series, in parallel with the third: pair $= 50~\mu\text{F}$; $C = 50 + 100 = 150~\mu\text{F}$. [1]

**Answer:** $33.3~\mu\text{F}$ (all series), $300~\mu\text{F}$ (all parallel), $66.7~\mu\text{F}$ (pair parallel, then series), $150~\mu\text{F}$ (pair series, then parallel).

**What the examiner wants:** 1 mark per correct network, including the diagram. This is a pure test of the series and parallel formulas and the "solve in stages" skill: pair first, then combine with the third.

### Example 10: Three capacitors in series with a cell - charges on every plate - End-of-chapter Q10, 5 + 3 marks

**Question:** Three capacitors of capacitance $100~\text{mF}$, $200~\text{mF}$ and $600~\text{mF}$ are connected in series with a cell of e.m.f. $1.5~\text{V}$ (Figure 24.18). (a) Calculate the charges $Q_1$ to $Q_6$ on each of the six plates. [5] (b) Calculate the p.d. across each capacitor. [3]

**Method:**
1. Total capacitance: $\frac{1}{C} = \frac{1}{100} + \frac{1}{200} + \frac{1}{600} = \frac{6 + 3 + 1}{600} = \frac{10}{600}$, so $C = 60~\text{mF} = 0.060~\text{F}$. [1]
2. Charge stored: $Q = CV = 0.060 \times 1.5 = 0.090~\text{C}$. Capacitors in series all store this same charge. [1]
3. Plates carry equal and opposite charges: $Q_1 = -0.090~\text{C}$, $Q_2 = +0.090~\text{C}$, $Q_3 = -0.090~\text{C}$, $Q_4 = +0.090~\text{C}$, $Q_5 = -0.090~\text{C}$, $Q_6 = +0.090~\text{C}$. [3]
4. (b) $V_1 = \frac{Q}{C_1} = \frac{0.090}{0.100} = 0.90~\text{V}$; $V_2 = \frac{0.090}{0.200} = 0.45~\text{V}$; $V_3 = \frac{0.090}{0.600} = 0.15~\text{V}$. [3]
5. Check: $0.90 + 0.45 + 0.15 = 1.50~\text{V}$, the cell e.m.f.

**Answer:** (a) each plate carries $\pm 0.090~\text{C}$, alternating in sign along the chain; (b) p.d.s are $0.90~\text{V}$, $0.45~\text{V}$ and $0.15~\text{V}$ across the $100$, $200$ and $600~\text{mF}$ capacitors respectively.

**What the examiner wants:** the sign pattern is the point of part (a): adjacent plates carry equal and opposite charges, and the central isolated sections stay uncharged overall. The p.d.s divide in inverse proportion to the capacitances (the smallest capacitor takes the largest share of the voltage) and must add to the supply e.m.f.

### Example 11: Discharge circuit with an $I$-$t$ graph - End-of-chapter Q11, 8 marks

**Question:** A $9.0~\text{V}$ supply charges a capacitor, which then discharges through a resistor $R$. The current-time graph during discharge starts at $I = 15~\text{mA}$ at $t = 0$ and falls towards zero by about $t = 12~\text{s}$. (a)(i) Deduce the resistance $R$ of the resistor. [2] (a)(ii) Explain why the current decreases as the capacitor discharges. [2] (b)(i) The charge on the capacitor is equal to the area under the graph. Estimate the charge on the capacitor when the p.d. across it is $9.0~\text{V}$. [2] (b)(ii) Calculate the capacitance of the capacitor. [2]

**Method:**
1. (a)(i) At $t = 0$ the p.d. across the capacitor is the full $9.0~\text{V}$, so $R = \frac{V}{I_0} = \frac{9.0}{15 \times 10^{-3}} = 600~\Omega$. [2]
2. (a)(ii) As charge leaves the plates, the p.d. across the capacitor falls; since $I = \frac{V}{R}$ and $R$ is constant, the current falls too. [2]
3. (b)(i) Area under the graph (counting squares or trapezium rule): each small square is worth $1~\text{mA} \times 1~\text{s} = 1~\text{mC}$, and the total area is about $70$ squares, so $Q \approx 0.07~\text{C}$ (accept $0.06$ to $0.08~\text{C}$). [2]
4. (b)(ii) $C = \frac{Q}{V} = \frac{0.07}{9.0} = 7.8 \times 10^{-3}~\text{F} \approx 8~\text{mF}$ (accept $6$ to $9~\text{mF}$). [2]

**Answer:** (a)(i) $R = 600~\Omega$; (a)(ii) the p.d. across the capacitor falls as it discharges, so $I = \frac{V}{R}$ falls; (b)(i) $Q \approx 0.07~\text{C}$; (b)(ii) $C \approx 8 \times 10^{-3}~\text{F}$.

**What the examiner wants:** for (a)(ii) the mark scheme wants the link "p.d. falls, so $I = \frac{V}{R}$ falls" - not just "the capacitor runs out of charge". For the area estimate, working (square counting with the scale stated) earns the marks; a bare number with no scale or method does not. The final capacitance follows from $C = \frac{Q}{V}$ with the full initial p.d.

### Example 12: Van de Graaff dome - End-of-chapter Q12, 4 marks

**Question:** The spherical dome of a Van de Graaff generator has a diameter of $40~\text{cm}$ and the potential at its surface is $54~\text{kV}$. (a) Calculate the charge on the dome. [2] (b) Calculate the capacitance of the dome. [2]

**Method:**
1. Radius: $r = \frac{0.40}{2} = 0.20~\text{m}$ (use the radius, not the diameter). [1]
2. (a) $V = \frac{Q}{4\pi\epsilon_0 r}$, so $Q = 4\pi\epsilon_0 rV = \frac{rV}{8.99 \times 10^9} = \frac{0.20 \times 54 \times 10^3}{8.99 \times 10^9} = 1.2 \times 10^{-6}~\text{C}$. [2]
3. (b) $C = 4\pi\epsilon_0 r = \frac{0.20}{8.99 \times 10^9} = 2.2 \times 10^{-11}~\text{F} = 22~\text{pF}$. [2]

**Answer:** (a) $Q = 1.2 \times 10^{-6}~\text{C} = 1.2~\mu\text{C}$; (b) $C = 2.2 \times 10^{-11}~\text{F} = 22~\text{pF}$.

**What the examiner wants:** the radius is half the diameter (a common slip loses a factor of 2), and the marks require the sphere formulas $V = \frac{Q}{4\pi\epsilon_0 r}$ and $C = 4\pi\epsilon_0 r$ written or used. Note the dome's tiny capacitance: $22~\text{pF}$ at $54~\text{kV}$ still stores $1.2~\mu\text{C}$ because the voltage is huge.

### Example 13: Two brass spheres sharing charge - energy dissipated - End-of-chapter Q13, 12 marks

**Question:** Two identical conducting brass spheres of radius $10~\text{cm}$ sit on insulating stands. Sphere A has charge $+5.0 \times 10^{-8}~\text{C}$ and sphere B is uncharged. (a) Show that the capacitance of an isolated conducting sphere of radius $r$ is $C = 4\pi\epsilon_0 r$, and calculate the potential at the surface of sphere A. [4] (b) Calculate the energy stored on sphere A. [2] (c) Sphere B is brought up to sphere A and touched to it so the charge is shared, then separated. (i) Calculate the energy stored on each sphere. [3] (ii) Calculate the energy dissipated during the discharge. [1] (d) Suggest why there is a change in the total energy of the system. [1]

**Method:**
1. (a) Show: the potential at the surface of a charged sphere is $V = \frac{Q}{4\pi\epsilon_0 r}$, and since $C = \frac{Q}{V}$, $C = \frac{Q}{Q/(4\pi\epsilon_0 r)} = 4\pi\epsilon_0 r$. [2]
2. Potential: $V = \frac{Q}{4\pi\epsilon_0 r} = \frac{8.99 \times 10^9 \times 5.0 \times 10^{-8}}{0.10} = 4.5 \times 10^3~\text{V} = 4.5~\text{kV}$. [2]
3. (b) $W = \frac{1}{2}QV = \frac{1}{2} \times 5.0 \times 10^{-8} \times 4.5 \times 10^3 = 1.1 \times 10^{-4}~\text{J}$. [2]
4. (c)(i) Identical spheres share the charge equally: $Q = 2.5 \times 10^{-8}~\text{C}$ on each. [1]
5. Potential of each after sharing: $V = \frac{8.99 \times 10^9 \times 2.5 \times 10^{-8}}{0.10} = 2.25 \times 10^3~\text{V}$. [1]
6. Energy on each: $W = \frac{1}{2}QV = \frac{1}{2} \times 2.5 \times 10^{-8} \times 2.25 \times 10^3 = 2.8 \times 10^{-5}~\text{J}$; total $= 5.6 \times 10^{-5}~\text{J}$. [1]
7. (c)(ii) Energy dissipated $= 1.1 \times 10^{-4} - 5.6 \times 10^{-5} = 5.6 \times 10^{-5}~\text{J}$. [1]
8. (d) The missing energy is dissipated as heat and light (a spark) while the charge moves between the spheres; energy is conserved overall, but stored electrical energy is lost. [1]

**Answer:** (a) $V = 4.5 \times 10^3~\text{V}$; (b) $W = 1.1 \times 10^{-4}~\text{J}$; (c)(i) $2.8 \times 10^{-5}~\text{J}$ on each sphere (total $5.6 \times 10^{-5}~\text{J}$); (c)(ii) $5.6 \times 10^{-5}~\text{J}$ dissipated; (d) energy is lost as heat/light in the spark during the transfer.

**What the examiner wants:** the "show that" earns credit for both the surface potential formula and the substitution into $C = \frac{Q}{V}$. Charge sharing between IDENTICAL spheres means equal division. The energy comparison before and after is the same physics as Section 1.8: charge conserved, energy not.

### Example 14: Reed switch circuit - End-of-chapter Q14, 11 marks

**Question:** A reed switch vibrates back and forth at a frequency of $50~\text{Hz}$. Each time it contacts A, a $67~\text{mF}$ capacitor is charged by a $12~\text{V}$ battery; each time it contacts B, the capacitor is fully discharged through a resistor. (a)(i) Calculate the charge stored on the capacitor when there is a p.d. of $12~\text{V}$ across it. [2] (a)(ii) Calculate the average current in the resistor. [2] (a)(iii) Calculate the average power dissipated in the resistor. [3] (b) A second capacitor of the same value is connected in series with the first. Discuss the effect on both the current recorded and the power dissipated in the resistor. [4]

**Method:**
1. (a)(i) $Q = CV = 0.067 \times 12 = 0.80~\text{C}$. [2]
2. (a)(ii) The charge $0.80~\text{C}$ is dumped through the resistor $50$ times per second, so average current $= Qf = 0.80 \times 50 = 40~\text{A}$. [2]
3. (a)(iii) Energy per cycle: $W = \frac{1}{2}CV^2 = \frac{1}{2} \times 0.067 \times 12^2 = 4.8~\text{J}$. [2]
4. Average power $= Wf = 4.8 \times 50 = 240~\text{W}$. [1]
5. (b) Two equal capacitors in series: total capacitance halves to $33.5~\text{mF}$. [1]
6. At the same $12~\text{V}$, the charge stored per cycle halves: $Q = 0.40~\text{C}$, so the average current halves to about $20~\text{A}$. [1]
7. The energy stored per cycle halves ($W = \frac{1}{2}CV^2$ with $C$ halved), so the average power halves to about $120~\text{W}$. [1]
8. The readings are halved because each cycle moves only half the charge, and that charge is delivered at the same p.d. [1]

**Answer:** (a)(i) $Q = 0.80~\text{C}$; (a)(ii) $I = 40~\text{A}$; (a)(iii) $P = 240~\text{W}$; (b) the series capacitor halves the total capacitance, so the charge per cycle, the average current and the average power all halve (about $20~\text{A}$ and $120~\text{W}$).

**What the examiner wants:** the average current is "charge per unit time", i.e. the charge transferred each cycle times the frequency. The average power is "energy per unit time", i.e. $\frac{1}{2}CV^2$ per cycle times the frequency. For part (b) the 4 marks are: capacitance halves, charge halves, current halves, energy/power halves - each idea earns a mark, and the effect on power must be justified via the energy per cycle.

## 6. Cheat Sheet

**One-glance revision block.**

Formulas (all of them):

$$Q = VC, \qquad C = \frac{Q}{V}, \qquad W = \frac{1}{2}QV = \frac{1}{2}CV^2 = \frac{Q^2}{2C}, \qquad Q = It$$

Parallel: $C_{\text{total}} = C_1 + C_2 + C_3 + \dots$ (add - like resistors in series).

Series: $\frac{1}{C_{\text{total}}} = \frac{1}{C_1} + \frac{1}{C_2} + \dots$ (reciprocals - like resistors in parallel), then take the reciprocal.

Sphere: $C = 4\pi\epsilon_0 r$; surface potential $V = \frac{Q}{4\pi\epsilon_0 r}$.

Key numbers: $\epsilon_0 = 8.85 \times 10^{-12}~\text{F m}^{-1}$; $\frac{1}{4\pi\epsilon_0} = 8.99 \times 10^9 \approx 9.0 \times 10^9~\text{m F}^{-1}$.

Unit conversions: $1~\text{F} = 10^6~\mu\text{F} = 10^9~\text{nF} = 10^{12}~\text{pF}$; so $\mu\text{F} \rightarrow \text{F}$ is $\times 10^{-6}$.

Rules that win marks:

- **Charge conserved, energy NOT, when capacitors share charge.** Connecting a charged capacitor across an uncharged one: $Q$ stays the same, $V$ falls to $\frac{Q}{C_1 + C_2}$, and the missing energy is lost as heat in the wires. Two equal capacitors: exactly half the energy is lost.
- **$W \propto V^2$ and $W \propto Q^2$:** double $V$ or $Q$ and the energy quadruples; halve $Q$ and the energy quarters.
- **Series total < smallest individual capacitance; parallel total > largest individual.** Use these to check every answer.
- **Charge stored means charge on ONE plate** (the plates carry $+Q$ and $-Q$, net zero).
- **Charge = area under $I$-$t$ graph; energy = area under $V$-$Q$ graph** (a triangle, so $\frac{1}{2}QV$).
- **Sphere questions: use the radius (half the diameter) and measure from the centre.**
- **Discharge:** current falls because the p.d. falls ($I = \frac{V}{R}$); initial $R = \frac{V_0}{I_0}$.

Common traps in one line each:

- Forgetting the final reciprocal in series combinations.
- Forgetting the $\frac{1}{2}$ in energy formulas.
- $\mu\text{F}$ not converted to F before using $Q = VC$.
- Assuming energy is conserved when capacitors share charge.
- Using the diameter instead of the radius for a sphere.
- Reading mA as A when computing $R = \frac{V}{I}$ or areas.
- Connecting electrolytic capacitors the wrong way round (polarity markings matter).
- Thinking doubling $V$ doubles the stored energy (it quadruples).

## 7. Common Exam Mistakes

From examiner reports and the coursebook's own questions, these are the actual reasons candidates lose marks on this chapter:

1. **Reciprocal formula errors in series.** Candidates add the capacitances directly, or forget to take the reciprocal at the end and quote $\frac{1}{C}$ as the answer. Always check: series total must be smaller than the smallest individual capacitance.
2. **Forgetting the $\frac{1}{2}$ in the energy formulas.** $W = QV$ and $W = CV^2$ are wrong for stored energy. The $\frac{1}{2}$ comes from the p.d. building up from zero while charging (average p.d. $= \frac{V}{2}$).
3. **Unit errors ($\mu\text{F}$ vs F).** Writing $C = 470$ instead of $C = 4.7 \times 10^{-4}~\text{F}$ changes the answer by six orders of magnitude. Convert every prefix before substituting, and quote the unit.
4. **Saying energy is conserved when capacitors share charge.** Charge is conserved; energy is not. For two equal capacitors half the stored energy is dissipated as heat in the connecting wires. This is the chapter's most famous trap.
5. **Using surface-to-centre distance wrongly.** For sphere potential questions the distance is always measured from the centre of the sphere, and the capacitance $C = 4\pi\epsilon_0 r$ uses the radius, which is half the diameter.
6. **Forgetting that the area under a graph is the answer.** The charge is the area under the current-time graph; the energy is the area under the p.d.-charge graph. Losing the $\frac{1}{2}$ on the triangular area, or counting squares with the wrong scale, loses both the method and the answer marks.
7. **Sign and polarity of electrolytic capacitors.** Electrolytic capacitors must be connected with the marked lead to the positive terminal; reversing the connection damages the capacitor and can be dangerous. Candidates should also remember that exceeding the working voltage makes the dielectric break down and charge leak across.
8. **The "doubling $V$ quadruples energy" trap.** Because $W \propto V^2$, doubling the charging voltage stores four times the energy, not twice. Similarly, when half the charge flows off a capacitor, the remaining energy is a quarter of the original, so three quarters is dissipated.
9. **Treating average current as constant current in discharge questions.** The discharge current decays because the p.d. falls, so $R = \frac{V}{I}$ can only give an estimate unless the initial current at full p.d. is used. "The current decreases because the p.d. across the capacitor falls, so $I = \frac{V}{R}$ falls" is the phrase the mark scheme wants.
10. **Confusing the letters.** $C$ means capacitance in farads but coulombs in $\text{C V}^{-1}$; $Q$ is charge and $V$ is p.d. Writing $W = \frac{1}{2}V^2C$ with $C$ in $\mu\text{F}$ and $V$ in mV, or swapping $Q$ and $V$ in formulas, produces answers that are wrong by large factors.
11. **Not stating "per unit p.d." in the definition of capacitance.** "The amount of charge a capacitor can hold" misses the ratio idea and does not earn both marks. The definition must be the charge stored on one plate per unit potential difference.
12. **Ignoring the conservation of charge argument in series circuits.** Each series capacitor stores the same charge because the central isolated section between the capacitors stays uncharged. Questions that ask you to find the charge on every plate (like Q10) reward this reasoning, not just the formula.

---

# Chapter 25: Electronics - CAIE A Level Physics (9702) Study Notes

## 2. Definition Sheet

Every definition you must know word-perfect for the exam. Learn these exactly - the wording is what the mark schemes award.

> **Transducer:** a device that changes energy from one form into another.

> **Sensing device:** an electronic component with a property (usually resistance) that changes when a physical quantity such as temperature, light intensity or pressure changes. A sensing device is also called a transducer.

> Mark scheme: "a property that changes with a physical quantity" (1 mark); naming the property (resistance) can earn a second.

> **Light-dependent resistor (LDR):** a semiconductor component whose resistance decreases as the intensity of the light falling on it increases. Light photons of high enough frequency release electrons in the semiconductor, which conduct electricity.

> Mark scheme: "resistance decreases as light intensity increases" is the core phrase - many candidates reverse it.

> **Negative temperature coefficient (NTC) thermistor:** a semiconductor component whose resistance decreases as its temperature increases. The rise in temperature increases the number of free electrons, so the resistance falls.

> Mark scheme: "resistance decreases as temperature increases" earns the mark. The resistance-temperature graph is not linear (roughly exponential), so a measuring circuit must be calibrated.

> **Piezo-electric effect:** the production of a potential difference (electric field) between the faces of a crystal when the crystal is stressed and changes shape. Some crystals (e.g. quartz) show this effect because they contain positive and negative ions in a regular arrangement.

> Mark scheme: "stress/force applied to the crystal produces a voltage" - both ideas (stress and voltage) are needed.

> **Strain gauge:** a device for measuring strain, made from a thin metal wire zigzagging between thin sheets of plastic, whose resistance changes when it is stretched or compressed. For small changes the change in resistance is directly proportional to the change in length: $\delta R \propto \delta L$.

> Mark scheme: "longer and narrower" so $R = \frac{\rho L}{A}$ rises (1); the proportionality $\delta R \propto \delta L$ is the examinable result (1).

> **Strain:** the fractional change in length of a wire or surface, $\text{strain} = \frac{\delta L}{L}$. It is a ratio, so it has no units.

> **Operational amplifier (op-amp):** a high-gain voltage amplifier with two inputs - the inverting input $(-)$ and the non-inverting input $(+)$ - and one output. It amplifies the potential difference between its two inputs: $V_{\text{out}} = G_0 (V_+ - V_-)$, where $G_0$ is the open-loop voltage gain.

> **Open-loop voltage gain:** the voltage gain of the op-amp with no feedback loop connecting the output to the input: $G_0 = \frac{V_{\text{out}}}{V_+ - V_-}$. For an ideal op-amp it is infinite; real op-amps have gains around $10^5$.

> **Saturation:** the state of an op-amp when the required output voltage exceeds the supply voltage, so the output is fixed at (close to) the positive or negative supply voltage $+V_s$ or $-V_s$.

> Mark scheme: "output cannot exceed the supply voltage" is the essential idea.

> **Virtual earth:** the point at the inverting input of an inverting amplifier, which is at (almost) zero potential even though it is not physically connected to earth. Because the open-loop gain is very high and the non-inverting input is at $0~\text{V}$, the potential difference between the inputs is almost zero, so the inverting input is at almost $0~\text{V}$.

> Mark scheme: two marks usually: "the inverting input is at (almost) zero volts" (1) and "because the open-loop gain is very high / the input difference is driven to zero" (1). Saying the input is "connected to earth" loses the mark - it is not connected; no current flows into it.

> **Negative feedback:** the process of returning part (or all) of the output of a system (or amplifier) to its input, so that the output affects the input. In an op-amp, feeding the output back to the inverting input reduces the gain but increases stability, increases the bandwidth and reduces distortion.

> Mark scheme: "part of the output is connected back to the input" is the core idea (1 mark).

> **Inverting amplifier:** an amplifier in which the input signal is applied to the inverting input through a resistor $R_{\text{in}}$, with a feedback resistor $R_f$ from the output to the inverting input. The gain is $G = -\frac{R_f}{R_{\text{in}}}$; the output is inverted (out of phase by $180^\circ$) with respect to the input.

> **Non-inverting amplifier:** an amplifier in which the input signal is applied to the non-inverting input and part of the output is fed back to the inverting input through a potential divider ($R_1$ from output to inverting input, $R_2$ from inverting input to $0~\text{V}$). The gain is $G = 1 + \frac{R_1}{R_2}$; the output is in phase with the input.

> **Bandwidth:** the range of frequencies for which an amplifier's gain is constant (amplified by the same amount). An ideal op-amp has infinite bandwidth; negative feedback increases the bandwidth.

> **Slew rate:** the rate at which an op-amp's output can change. An ideal op-amp has an infinite slew rate (the output changes instantaneously, with no time delay).

> **Relay:** an electromagnetic switch in which a small current in a coil magnetises an iron core and closes contacts, completing a separate circuit that can carry large currents or voltages.

> **Calibration:** the process of relating the readings of a measuring instrument to known values of the quantity being measured (e.g. using a thermometer in a water bath to produce a calibration graph of voltmeter reading against temperature).

## 3. Formula Sheet

**Quick reference:**

$$ V_{\text{out}} = \frac{R_2}{R_1 + R_2} V_s, \qquad V_{\text{out}} = G_0 (V_+ - V_-), \qquad G = -\frac{R_f}{R_{\text{in}}}, \qquad G = 1 + \frac{R_1}{R_2}, \qquad \frac{\delta R}{R} = \frac{\delta L}{L} \text{ (area constant)}, \qquad \frac{\delta R}{R} = \frac{2\,\delta L}{L} \text{ (volume constant)}, \qquad \text{strain} = \frac{\delta L}{L}, \qquad R = \frac{\rho L}{A}, \qquad I = \frac{V}{R}, \qquad R = \frac{V_s - V_{\text{LED}}}{I} $$

| Formula | Meaning of symbols | Units | When to use it |
| --- | --- | --- | --- |
| $$V_{\text{out}} = \frac{R_2}{R_1 + R_2} V_s$$ | $V_{\text{out}}$ output p.d. across $R_2$, $R_1$ other resistor, $V_s$ supply p.d. | $V$, $\Omega$, $V$ | Sensor potential-divider circuits (LDR, thermistor, strain gauge in series with a fixed resistor) |
| $$V_{\text{out}} = G_0 (V_+ - V_-)$$ | $G_0$ open-loop voltage gain, $V_+$ potential at non-inverting input, $V_-$ potential at inverting input | V (gain dimensionless) | Op-amp with no feedback (comparator); deciding the output state |
| $$G = -\frac{R_f}{R_{\text{in}}}$$ | $G$ voltage gain, $R_f$ feedback resistor, $R_{\text{in}}$ input resistor | dimensionless | Inverting amplifier (output inverted, $180^\circ$ out of phase) |
| $$G = 1 + \frac{R_1}{R_2}$$ | $G$ voltage gain, $R_1$ feedback resistor, $R_2$ resistor from inverting input to $0~\text{V}$ | dimensionless | Non-inverting amplifier (output in phase); gain can never be less than 1 |
| $$\frac{\delta R}{R} = \frac{\delta L}{L}$$ | $\delta R$ change in resistance, $R$ original resistance, $\delta L$ change in length, $L$ original length | dimensionless | Strain gauge when the cross-sectional area is assumed constant |
| $$\frac{\delta R}{R} = \frac{2\,\delta L}{L}$$ | as above | dimensionless | Strain gauge in practice (volume stays constant, so the wire narrows as well) |
| $$\text{strain} = \frac{\delta L}{L}$$ | $\delta L$ extension, $L$ original length | dimensionless | Strain of a wire or bar; strain gauges glued to a surface measure the surface's strain |
| $$R = \frac{\rho L}{A}$$ | $R$ resistance, $\rho$ resistivity, $L$ length, $A$ cross-sectional area | $\Omega$, $\Omega~\text{m}$, m, $\text{m}^2$ | Explaining why stretching a wire changes its resistance |
| $$I = \frac{V}{R}$$ | $I$ current, $V$ p.d., $R$ resistance | A, V, $\Omega$ | Current through LDR, thermistor, relay coil, LED series resistor |
| $$R = \frac{V_s - V_{\text{LED}}}{I}$$ | $V_s$ op-amp output (or supply) voltage, $V_{\text{LED}}$ LED conducting voltage (about 2 V), $I$ required LED current | $\Omega$, V, V, A | Series resistor for an LED (subtract the LED's $2~\text{V}$!) |

Constants you may need: none specific to this chapter, but note the typical values: LED conducting voltage about $2~\text{V}$; LED current about $20~\text{mA}$; op-amp maximum output current about $25~\text{mA}$; real op-amp open-loop gain about $10^5$; input resistance up to $10^{12}~\Omega$ (typically $10^6~\Omega$); output resistance about $75~\Omega$.

**Exam fact:** the op-amp gain equations ($G = -R_f/R_{\text{in}}$ and $G = 1 + R_1/R_2$) and the strain-gauge proportionalities are NOT on the data sheet - recall them from memory. $I = V/R$ and $R = \rho L/A$ are standard material from earlier chapters (both effectively given). The potential divider formula is used so often that you should be able to write it without thinking.

## 4. Methods (Question Types & Methods)

These are the ways Cambridge has actually asked about electronics. Each method below is what a full-mark answer looks like.

### 1. Read a sensor's resistance from a graph

**Method:**
1. Identify the curve for the right component (LDR against light intensity in lux; thermistor against temperature in °C).
2. Read the resistance at the stated value of the quantity, converting the axis units (kΩ to Ω if needed).
3. Use that resistance in the potential divider formula (Method 2).

**Traps:** reading the wrong curve (thermistor vs metal wire - the metal wire's resistance rises with temperature); mixing up kΩ and Ω; misreading the lux or °C axis.

### 2. Output voltage of a sensor potential divider

**Method:**
1. Decide which component the output is across - that component is $R_2$ in $V_{\text{out}} = \frac{R_2}{R_1 + R_2} V_s$.
2. Write the sensor resistance at the stated condition (from the question or the graph).
3. Substitute both resistances (same units - keep both in kΩ or both in Ω) and the supply p.d.
4. Quote $V_{\text{out}}$ to 3 significant figures with the unit V.

**Traps:** putting the output across the wrong resistor in the formula; mixing units (20 kΩ + 300 Ω must become 20 300 Ω or 20 + 0.3 kΩ); giving $8.69$ instead of rounding $8.69565$ to $8.70$ (3 s.f.).

### 3. Design a sensing circuit (which component does the output go across)

**Method:**
1. Note the required behaviour: does $V_{\text{out}}$ need to rise or fall as the sensed quantity rises?
2. For an LDR or NTC thermistor, resistance falls as the sensed quantity rises. If the output is across the sensor, $V_{\text{out}}$ falls; if across the fixed resistor, $V_{\text{out}}$ rises.
3. Choose the arrangement that matches: output across the fixed resistor for "increases with quantity", across the sensor for "decreases with quantity".
4. To set a threshold, use a variable resistor and adjust it.

**Traps:** forgetting which way the sensor's resistance moves; drawing the output across both resistors (there is no output point); forgetting to show the supply and the $0~\text{V}$ line.

### 4. Comparator: find both input potentials, then decide the output

**Method:**
1. Treat each input separately: each is fed by its own potential divider, so compute $V_+$ and $V_-$ with the divider formula.
2. Compare them: $V_+ > V_-$ gives output $\approx +V_s$; $V_+ < V_-$ gives output $\approx -V_s$.
3. If the op-amp is not saturated and $G_0$ is given, use $V_{\text{out}} = G_0 (V_+ - V_-)$ and check against the supply.
4. State the switching condition in words (e.g. "the output switches when the temperature falls below the value at which $V_+ = V_-$").

**Traps:** computing only one input potential; mixing up the inputs; writing an absurd unsaturated output (e.g. 5000 V) instead of the supply rail.

### 5. Modify a comparator to reverse the switching behaviour

**Method:**
1. Work out which divider output rises and which falls as the sensed quantity changes.
2. To reverse the switching, swap the sensor and the fixed resistor in the sensor divider (or swap which input the sensor divider feeds).
3. Check with one hot and one cold example that the output states have swapped.

**Traps:** swapping the reference divider instead of the sensor divider; forgetting the switching temperature can also be adjusted by changing the series resistor value.

### 6. Inverting amplifier: gain, output, saturation limit

**Method:**
1. Gain: $G = -\frac{R_f}{R_{\text{in}}}$ (keep both resistances in the same unit).
2. Output: $V_{\text{out}} = G \times V_{\text{in}}$, keeping the minus sign.
3. Check against the rails: if $|V_{\text{out}}| > V_s$, the output is saturated at $\pm V_s$.
4. Maximum input before saturation: $V_{\text{in(max)}} = \frac{V_s}{|G|}$.
5. Input resistance of the amplifier $= R_{\text{in}}$ (virtual earth).

**Traps:** dropping the minus sign; forgetting the saturation clamp; dividing by the gain instead of multiplying; unit slips (mV vs V).

### 7. Non-inverting amplifier: gain and output

**Method:**
1. Gain: $G = 1 + \frac{R_1}{R_2}$.
2. Output: $V_{\text{out}} = G \times V_{\text{in}}$ (no sign change - the output is in phase).
3. Check saturation against the rails, especially when the input is large.

**Traps:** forgetting the $+1$; using the inverting formula by mistake; forgetting the output saturates when $G \times V_{\text{in}}$ exceeds the supply.

### 8. The virtual earth current method (find a current or resistance)

**Method:**
1. State that the inverting input is a virtual earth: at (almost) $0~\text{V}$.
2. Current through the input resistor: $I_{\text{in}} = \frac{V_{\text{in}}}{R_{\text{in}}}$ (the far end of $R_{\text{in}}$ is at $0~\text{V}$).
3. No current enters the op-amp input, so the same current flows through the feedback resistor: $I_f = I_{\text{in}}$.
4. $V_{\text{out}} = -I_f R_f$ (negative because the current leaves the virtual earth for the output).

**Traps:** thinking current flows into the op-amp; forgetting the virtual earth is at $0~\text{V}$ so $I_{\text{in}} = V_{\text{in}}/R_{\text{in}}$ directly; sign errors on $V_{\text{out}}$.

### 9. Strain gauge: resistance change to length change to output

**Method:**
1. From the divider output voltage, find the gauge resistance (Method 2, rearranged).
2. Change in resistance: $\delta R = R_{\text{new}} - R_0$.
3. Length change: use $\frac{\delta R}{R} = \frac{2\,\delta L}{L}$ (or $\frac{\delta R}{R} = \frac{\delta L}{L}$ if the question states the area is constant).
4. Strain: $\frac{\delta L}{L}$, dimensionless; the strain of the gauge equals the strain of the surface it is glued to.

**Traps:** using the wrong proportionality factor (2 vs 1) without reading the question; leaving lengths in cm and mixing with m; quoting strain with units.

### 10. Output devices: LED resistor and relay protection

**Method:**
1. LED: $R = \frac{V_{\text{out}} - 2~\text{V}}{I}$, with $I \approx 20~\text{mA}$ converted to amperes.
2. Relay: coil in series with the op-amp output; reverse-biased diode $D_1$ across the coil (protects against the induced e.m.f. when the coil is switched off); series diode $D_2$ if the relay must operate only for a positive output.
3. State why each diode is there - the marks are for the reasons.

**Traps:** forgetting to subtract the $2~\text{V}$ across the LED; mA not converted to A; drawing $D_1$ forward-biased; saying the relay "amplifies" the current (it switches a separate circuit, it does not amplify).

### 11. Sketch graphs: amplifier input/output and calibration curves

**Method:**
1. Amplifier: draw the input sine wave, then the output with the correct amplitude (gain $\times$ input) and the correct phase (inverting: $180^\circ$ out; non-inverting: in phase); clip the output at the supply rails if it would exceed them.
2. Calibration: plot voltmeter reading against the physical quantity from the calibration experiment; the curve is usually not a straight line (the sensor is non-linear); use it to convert readings.

**Traps:** wrong phase relationship; output amplitude not scaled by the gain; forgetting saturation clipping; drawing a linear calibration curve for a thermistor (it is curved).

### 12. Definitions and explanation questions (feedback, virtual earth, gains)

**Method:**
1. Feedback: "part of the output is returned/connected back to the input" - then give the effect (gain reduced, stability increased, bandwidth increased, distortion reduced).
2. Virtual earth: "the inverting input is at almost zero volts, although not connected to earth, because the high open-loop gain keeps the input difference almost zero" - never "it is connected to earth".
3. Why inverting gain can be below 1: the magnitude is just the resistor ratio $R_f/R_{\text{in}}$, which can be any positive value.
4. Why non-inverting gain cannot be below 1: $G = 1 + \frac{R_1}{R_2}$ and $R_1/R_2 \geq 0$.

**Traps:** giving the equation without the explanation (equation alone earns only part of the marks); "virtual earth = connected to earth" (a definite zero); "feedback makes the amplifier stronger" (feedback reduces gain).

## 5. Solved Examples

Real exam-style questions from the end of Chapter 25, with their mark allocations, plus the book's worked examples. The format for every example: Question / Method / Answer / What the examiner wants. Marks are summed from the printed allocations; where the printed layout was garbled, the split is noted as reconstructed.

### Example 1: Reversing a temperature comparator - End-of-chapter Q1, 1 mark

**Question:** How can the circuit of Figure 25.17 be altered so that the op-amp switches from $+9~\text{V}$ to $-9~\text{V}$ when the temperature rises, instead of when it falls? Draw the circuit diagram. [1]

**Method:**
1. In the original circuit the thermistor is between $+9~\text{V}$ and point A, and the $10~\text{k}\Omega$ resistor is between A and the $0~\text{V}$ line. As temperature falls, $R_T$ rises, $V_A = 9 \times \frac{10}{R_T + 10}$ falls below $4.5~\text{V}$, and the output switches from $+9~\text{V}$ to $-9~\text{V}$.
2. To make the output switch when the temperature RISES, swap the two components: put the $10~\text{k}\Omega$ resistor between $+9~\text{V}$ and A, and the thermistor between A and $0~\text{V}$.
3. Check: now $V_A = 9 \times \frac{R_T}{R_T + 10}$. When the temperature rises, $R_T$ falls, $V_A$ falls below $4.5~\text{V}$, and the output switches from $+9~\text{V}$ to $-9~\text{V}$.

**Answer:** swap the thermistor and the $10~\text{k}\Omega$ resistor in the sensor potential divider (thermistor connected to the $0~\text{V}$ line, $10~\text{k}\Omega$ to $+9~\text{V}$).

**What the examiner wants:** 1 mark for the swap. The switching temperature is still where $R_T = 10~\text{k}\Omega$ (the divider ratio is unchanged, just mirrored).

### Example 2: Comparator with an LDR - End-of-chapter Q2, 3 marks

**Question:** Draw the circuit diagram of a comparator that switches the output voltage from positive to negative when the light intensity falling on an LDR decreases. [3]

**Method:**
1. Sensor divider: LDR in series with a fixed resistor $R$ across the $+9~\text{V}$ supply and $0~\text{V}$ line, with the LDR connected to $+9~\text{V}$. The junction voltage is $V_A = 9 \times \frac{R}{R_{\text{LDR}} + R}$: bright light (small $R_{\text{LDR}}$) gives a high $V_A$; dim light (large $R_{\text{LDR}}$) gives a low $V_A$.
2. Reference divider: two equal resistors (or a variable resistor) across the supply, giving a fixed reference $V_{\text{ref}}$ between the two extremes, e.g. $4.5~\text{V}$.
3. Connect $V_A$ to the non-inverting input $(+)$ and $V_{\text{ref}}$ to the inverting input $(-)$, with the op-amp supplied at $\pm 9~\text{V}$.
4. Check: bright light gives $V_+ > V_-$, output $+9~\text{V}$; when the light falls, $V_A$ drops below $V_{\text{ref}}$, and the output switches to $-9~\text{V}$.

**Answer:** LDR plus fixed resistor as the sensor potential divider feeding $(+)$; fixed reference voltage (from a second potential divider) feeding $(-)$; op-amp with $\pm 9~\text{V}$ supplies.

**What the examiner wants:** 1 mark for the sensor potential divider with the LDR, 1 for a reference voltage, 1 for the correct connections (sensor divider to $(+)$, reference to $(-)$) so the output goes negative as the light falls.

### Example 3: Feedback and virtual earth definitions - End-of-chapter Q3, 1 + 2 marks

**Question:** Explain what is meant by (a) feedback [1] (b) the virtual earth approximation. [2]

**Method:**
1. (a) Feedback: part (or all) of the output of a system is returned (fed back) to its input, so the output affects the input. In an op-amp circuit, the output is connected back to the inverting input.
2. (b) Virtual earth: the potential at the inverting input of an inverting amplifier is (almost) zero, even though that input is not connected to earth. This happens because the open-loop gain is very high, so the potential difference between the two inputs is driven to almost zero; since the non-inverting input is at $0~\text{V}$, the inverting input is at almost $0~\text{V}$ too.

**Answer:** (a) returning part of the output to the input; (b) the inverting input sits at almost $0~\text{V}$ (not connected to earth) because the very high open-loop gain keeps the two inputs at almost the same potential.

**What the examiner wants:** feedback earns 1 mark for "part of the output is returned to the input". Virtual earth earns 2: "inverting input at (almost) zero volts" (1) and "because the input difference is almost zero / gain is very high" (1). "Connected to earth" scores zero - it is NOT connected.

### Example 4: Inverting amplifier calculations - End-of-chapter Q4, 2 + 2 + 1 marks

**Question:** In the inverting amplifier of Figure 25.20, $R_{\text{in}} = 10~\text{k}\Omega$, $R_f = 200~\text{k}\Omega$ and $V_s = 12~\text{V}$. Calculate: (a) the gain of the amplifier [2] (b) the input voltage when the output voltage is $8.0~\text{V}$ [2] (c) the maximum input voltage. [1]

**Method:**
1. (a) $G = -\frac{R_f}{R_{\text{in}}} = -\frac{200}{10} = -20$. [2]
2. (b) $V_{\text{out}} = G V_{\text{in}}$, so $V_{\text{in}} = \frac{V_{\text{out}}}{G} = \frac{8.0}{-20} = -0.40~\text{V}$. [2]
3. (c) Saturation at $V_{\text{out}} = \pm 12~\text{V}$: $V_{\text{in(max)}} = \frac{V_s}{|G|} = \frac{12}{20} = 0.60~\text{V}$. [1]

**Answer:** (a) $G = -20$; (b) $V_{\text{in}} = -0.40~\text{V}$; (c) maximum input $V_{\text{in}} = 0.60~\text{V}$ (so the output just reaches the rail).

**What the examiner wants:** part (a) 2 marks: formula plus substitution. Part (b) 2 marks: rearrangement and substitution with the sign correct (a positive output needs a negative input). Part (c) 1 mark: $12/20$, with the concept that the output cannot exceed the supply.

### Example 5: Gains below 1 - End-of-chapter Q5, 2 + 2 marks

**Question:** (a) Explain how an inverting amplifier can have a gain of $-0.5$. [2] (b) Explain why the gain of a non-inverting amplifier cannot be less than 1. [2]

**Method:**
1. (a) The gain is $G = -\frac{R_f}{R_{\text{in}}}$, and its magnitude is set by the resistor ratio. Choose $R_f$ smaller than $R_{\text{in}}$, e.g. $R_f = 5~\text{k}\Omega$ and $R_{\text{in}} = 10~\text{k}\Omega$: then $G = -\frac{5}{10} = -0.5$. The magnitude can be any positive value - even below 1. [2]
2. (b) $G = 1 + \frac{R_1}{R_2}$. Since $R_1$ and $R_2$ are positive resistances, $\frac{R_1}{R_2} \geq 0$, so $G \geq 1$. The smallest possible gain is 1 (when $R_1 = 0$). [2]

**Answer:** (a) choose the resistor ratio $R_f/R_{\text{in}} = 0.5$ (e.g. $5~\text{k}\Omega$ and $10~\text{k}\Omega$); (b) because $G = 1 + R_1/R_2$ with $R_1/R_2 \geq 0$.

**What the examiner wants:** the marks are for the reasoning, not the numbers: an inverting amplifier's gain magnitude is any ratio of two resistances; the non-inverting formula has the $+1$ built in. Candidates who write only "the resistor values are chosen" without the formula lose the second mark.

### Example 6: Sketching amplifier input and output - End-of-chapter Q6, 3 marks

**Question:** The non-inverting amplifier in Figure 25.21 has $R_1 = 15~\text{k}\Omega$, $R_2 = 5~\text{k}\Omega$ and $V_s = 10~\text{V}$. An a.c. signal of amplitude $0.20~\text{V}$ is applied to the input. Draw a single sketch graph which shows both the input and the output voltage over the same axes. [3]

**Method:**
1. Gain: $G = 1 + \frac{R_1}{R_2} = 1 + \frac{15}{5} = 4$.
2. Output amplitude: $V_{\text{out}} = 4 \times 0.20 = 0.80~\text{V}$ (well below the $10~\text{V}$ rails, so no clipping).
3. Graph: two sine waves on the same time axis, in phase (non-inverting), input amplitude $0.20~\text{V}$, output amplitude $0.80~\text{V}$, both centred on $0~\text{V}$, axes labelled.

**Answer:** two in-phase sine waves; input peaks at $\pm 0.20~\text{V}$, output peaks at $\pm 0.80~\text{V}$.

**What the examiner wants:** 1 mark for the correct amplitude ratio (4:1), 1 for the in-phase relationship, 1 for labelled axes and correct relative sizes. Drawing the output inverted (as for an inverting amplifier) loses the phase mark.

### Example 7: Identify the amplifier type and gain - End-of-chapter Q7, 3 marks

**Question:** Is the circuit shown in Figure 25.27 an inverting or non-inverting amplifier? Calculate its gain. ($R_{\text{in}} = 9~\text{k}\Omega$, $R_f = 1~\text{k}\Omega$, input to the inverting input through $R_{\text{in}}$, $+$ input at $0~\text{V}$.) [3]

**Method:**
1. The input is applied to the inverting input $(-)$ through $R_{\text{in}}$, the non-inverting input is at $0~\text{V}$, and $R_f$ connects the output back to the inverting input: this is the inverting amplifier configuration.
2. $G = -\frac{R_f}{R_{\text{in}}} = -\frac{1}{9} = -0.11$ (3 s.f.).

**Answer:** inverting amplifier; $G = -0.11$ (that is, $-1/9$).

**What the examiner wants:** the identification (input at $(-)$ through a resistor is the giveaway) and the ratio. Note the magnitude is below 1 - perfectly normal for an inverting amplifier, since the gain is just the resistor ratio.

### Example 8: LDR sensor circuit design - End-of-chapter Q8, 2 + 2 + 2 marks

**Question:** A light-dependent resistor is used with additional components to make a sensor. The voltage output increases as light intensity increases. (a) Sketch the diagram of a suitable circuit. [2] (b) Explain how your circuit works. [2] (c) State which parts of your circuit are the sensor, the processor and the output device. [2]

**Method:**
1. (a) LDR in series with a fixed resistor across a cell; output taken across the FIXED resistor (LDR connected to the positive terminal of the cell, fixed resistor to the $0~\text{V}$ line, output at their junction). [2]
2. (b) The two resistors form a potential divider. When the light intensity increases, the LDR resistance falls, so the LDR takes a smaller share of the supply voltage and the fixed resistor takes a larger share: the output voltage across the fixed resistor rises. [2]
3. (c) Sensor: the LDR (its resistance changes with light). Processor: the potential divider circuit (turns the resistance change into an output voltage). Output device: the voltmeter (or the device the voltage drives). [2]

**Answer:** (a) LDR and fixed resistor in series across the cell, output across the fixed resistor; (b) brighter light lowers $R_{\text{LDR}}$, so the fixed resistor takes a bigger share of the supply p.d. and $V_{\text{out}}$ rises; (c) sensor = LDR, processor = potential divider, output device = voltmeter.

**What the examiner wants:** part (a) needs the series pair, the supply, and the output across the FIXED resistor - taking it across the LDR gives a falling output. Part (b) needs the potential-divider argument (share of voltage proportional to resistance). Part (c) rewards the three-part vocabulary: sensing device, processor, output device.

### Example 9: Strain gauge on a metal bar - End-of-chapter Q9, 2 + 2 + 2 marks

**Question:** A strain gauge is used to measure the extension of a metal bar. The gauge is stuck to the bar and the change in resistance of the wire in the gauge enables the extension to be determined. The strain gauge is connected in the circuit shown in Figure 25.28: a $5.0~\text{V}$ d.c. supply, the strain gauge and a $300~\Omega$ resistor in series, voltmeter across the strain gauge. (a) Explain why the resistance of the wire increases when it is stretched and show that the change in resistance is proportional to the extension, provided that the cross-sectional area is constant. [2] (b) The resistance of the strain gauge when unstretched is $150~\Omega$. Calculate the reading on the voltmeter. [2] (c) State and explain the effect on the voltmeter reading when the strain gauge is stretched. [2]

**Method:**
1. (a) Stretching makes the wire longer and narrower. With $R = \frac{\rho L}{A}$, an increase in $L$ (with $A$ constant) increases $R$: $R + \delta R = \frac{\rho (L + \delta L)}{A}$, so $\delta R = \frac{\rho\,\delta L}{A}$ and $\frac{\delta R}{R} = \frac{\delta L}{L}$. Hence $\delta R \propto \delta L$ for constant $A$. [2]
2. (b) Potential divider across the strain gauge: $V = 5.0 \times \frac{150}{150 + 300} = 1.67~\text{V}$. [2]
3. (c) When stretched, $R$ increases, so the strain gauge takes a larger share of the supply p.d.: the voltmeter reading rises. [2]

**Answer:** (a) longer wire (and narrower, but the question fixes $A$) means larger $R$; $\frac{\delta R}{R} = \frac{\delta L}{L}$, so $\delta R \propto \delta L$; (b) $V = 1.67~\text{V}$; (c) the reading increases because the gauge's share of the $5.0~\text{V}$ grows with its resistance.

**What the examiner wants:** part (a) 2 marks: the "longer and narrower" idea (1) and the proportionality from $R = \rho L/A$ (1). Part (b): divider substitution with units. Part (c): the potential-divider reasoning - resistance up means p.d. across it up. (Assumption: the voltmeter is across the strain gauge, as the printed figure layout indicates; if your copy shows it across the $300~\Omega$ resistor, the reading is $3.33~\text{V}$ and falls when stretched.)

### Example 10: Fibre optic microphone amplifier - End-of-chapter Q10, 2 + 2 + 2 + 2 + 2 marks

**Question:** In a fibre optic system, sound into a microphone is used to produce different intensities of light passed along a glass fibre. The microphone is connected to a non-inverting amplifier (dual $15~\text{V}$ supplies), the output of which is connected to an LED. The microphone produces a maximum output of $+20~\text{mV}$. (a)(i) State two advantages of using negative feedback in the amplifier circuit. [2] (a)(ii) Calculate the maximum possible gain for the amplifier. [2] (b) Copy and complete the circuit to show the resistors necessary for a non-inverting amplifier, the connection of the microphone, and the output components needed. [2] (c)(i) With the maximum possible gain, suggest suitable values for all the resistors drawn. [2] (c)(ii) Explain what happens in the system when the voltage output from the microphone rises. [2]

**Method:**
1. (a)(i) Any two: less distortion; increased bandwidth; more stable gain (unaffected by temperature); low output resistance; high input resistance. [2]
2. (a)(ii) The output cannot exceed the supply: maximum gain $= \frac{V_s}{V_{\text{in(max)}}} = \frac{15}{20 \times 10^{-3}} = 750$. [2]
3. (b) $R_2$ from the inverting input to the $0~\text{V}$ line; $R_1$ from the output to the inverting input; microphone connected between the $0~\text{V}$ line and the non-inverting input; LED with a series resistor from the output to the $0~\text{V}$ line. [2]
4. (c)(i) Gain $= 1 + \frac{R_1}{R_2} = 750$, so $\frac{R_1}{R_2} = 749$. Choose $R_2 = 1~\text{k}\Omega$ and $R_1 = 749~\text{k}\Omega$ (or any pair with the same ratio, e.g. $10~\text{k}\Omega$ and $7.49~\text{M}\Omega$). LED series resistor: $R = \frac{V_{\text{out}} - 2}{I} = \frac{15 - 2}{0.020} = 650~\Omega$. [2]
5. (c)(ii) As the microphone output rises, the amplifier output rises (in phase), the p.d. across the LED and its series resistor rises, the LED current increases, the LED emits more light, and the light intensity passed along the fibre increases. [2]

**Answer:** (a)(i) e.g. less distortion and increased bandwidth; (a)(ii) $G = 750$; (b) standard non-inverting resistor pair, microphone to $(+)$, LED plus $650~\Omega$ series resistor from output to $0~\text{V}$; (c)(i) $R_1 = 749~\text{k}\Omega$, $R_2 = 1~\text{k}\Omega$, LED resistor $650~\Omega$; (c)(ii) the LED shines more brightly, so more light travels down the fibre.

**What the examiner wants:** the gain limit comes from saturation at $15~\text{V}$ - candidates who use $750$ without the $20~\text{mV}$ conversion lose the method mark. The resistor values must give a gain of (about) $750$; the LED resistor calculation must subtract the $2~\text{V}$ LED drop and convert $20~\text{mA}$ to amperes.

### Example 11: Two-LDR motor controller - End-of-chapter Q11, 1 + 1 + 2 + 5 marks

**Question:** A student builds a circuit to control a motor using two identical LDRs, P and Q (Figure 25.30). In room light the resistance of each LDR is $500~\Omega$; when a torch shines on an LDR its resistance becomes $200~\Omega$. Each LDR is in series with a $300~\Omega$ resistor across the $+9~\text{V}$ supply, with junctions A (P side) and B (Q side). A connects to the inverting input $(-)$ and B to the non-inverting input $(+)$ of an op-amp with $\pm 9~\text{V}$ supplies; the motor is between the output and $0~\text{V}$. (a) State the value of the output voltage when: (i) the potential at A is greater than the potential at B [1] (ii) the potential at B is greater than the potential at A. [1] (b) Calculate the potential at point A when a torch shines on P. [2] (c) Explain what happens when (i) a torch shines on P but not on Q [2] (ii) a torch shines on Q but not on P [2] (d) Explain why it is difficult to know what will happen if no torch shines on P or Q. [1]

**Method:**
1. (a)(i) A is the inverting input, so $V_A > V_B$ means $V_- > V_+$: the output saturates at the negative rail, $V_{\text{out}} = -9~\text{V}$. [1]
2. (a)(ii) $V_B > V_A$ means $V_+ > V_-$: $V_{\text{out}} = +9~\text{V}$. [1]
3. (b) Torch on P: $R_P = 200~\Omega$, fixed resistor $300~\Omega$, supply $9~\text{V}$: $V_A = 9 \times \frac{300}{200 + 300} = 5.4~\text{V}$. [2]
4. (c)(i) Torch on P only: $V_A = 5.4~\text{V}$; Q is in room light, so $V_B = 9 \times \frac{300}{500 + 300} = 3.4~\text{V}$. $V_A > V_B$, so the output is $-9~\text{V}$ and the motor turns (in the reverse direction). [2]
5. (c)(ii) Torch on Q only: $V_B = 5.4~\text{V}$, $V_A = 3.4~\text{V}$. $V_B > V_A$, so the output is $+9~\text{V}$ and the motor turns the other way. [2]
6. (d) With no torch, both LDRs are at $500~\Omega$ and the two divider outputs are exactly equal ($3.4~\text{V}$); the op-amp input difference is effectively zero, and any tiny imbalance (component tolerance, noise, input offset) decides the output, so it cannot be predicted. [1]

**Answer:** (a)(i) $-9~\text{V}$; (a)(ii) $+9~\text{V}$; (b) $V_A = 5.4~\text{V}$; (c)(i) output $-9~\text{V}$, motor turns one way; (c)(ii) output $+9~\text{V}$, motor turns the other way; (d) the inputs are (almost) equal, so the output is unpredictable.

**What the examiner wants:** the sign answers depend on which input each junction feeds - A to $(-)$, B to $(+)$ as stated. The divider calculation in (b) is the standard $V = V_s \times R_{\text{fixed}}/(R_{\text{LDR}} + R_{\text{fixed}})$. Part (d) earns the mark for the "equal inputs, so the output is not defined" idea - not for saying the motor "stops" (it does not; it is driven to one rail or the other). (Mark split reconstructed from the printed layout; the three explanation parts total 5 marks.)

### Example 12: Virtual earth and inverting gain - End-of-chapter Q12, 2 + 2 + 1 marks

**Question:** (a) Explain what is meant by a virtual earth, and use your explanation to show that the gain of the inverting amplifier in Figure 25.31 is $-\frac{R_2}{R_1}$. [2] (b) In that amplifier $R_1 = 20~\text{k}\Omega$, $R_2 = 4~\text{k}\Omega$ and $V_{\text{in}} = 0.50~\text{V}$. Calculate the value of $V_{\text{out}}$. [2] (c) A resistor of $4~\text{k}\Omega$ is placed in parallel with $R_2$. Calculate the new value of $V_{\text{out}}$. [1]

**Method:**
1. (a) The inverting input is a virtual earth: at almost $0~\text{V}$ (high open-loop gain, $+$ input at $0~\text{V}$). No current enters the input, so the current in $R_1$ equals the current in $R_2$: $\frac{V_{\text{in}}}{R_1} = -\frac{V_{\text{out}}}{R_2}$, giving $V_{\text{out}} = -\frac{R_2}{R_1} V_{\text{in}}$ and gain $= -\frac{R_2}{R_1}$. [2]
2. (b) $G = -\frac{R_2}{R_1} = -\frac{4}{20} = -0.20$; $V_{\text{out}} = -0.20 \times 0.50 = -0.10~\text{V}$. [2]
3. (c) Parallel combination: $R_2' = \frac{4 \times 4}{4 + 4} = 2~\text{k}\Omega$. New gain $= -\frac{2}{20} = -0.10$; $V_{\text{out}} = -0.10 \times 0.50 = -0.050~\text{V}$. [1]

**Answer:** (a) derivation via equal currents through $R_1$ and $R_2$ at the virtual earth; (b) $V_{\text{out}} = -0.10~\text{V}$; (c) $V_{\text{out}} = -0.050~\text{V}$ (gain halved because $R_2$ halved).

**What the examiner wants:** part (a) 2 marks: the virtual earth idea (1) and the equal-currents derivation giving the ratio (1). Part (c): the parallel resistance halves $R_2$, halving the magnitude of the gain.

### Example 13: Heater switching circuit - End-of-chapter Q13, 2 + 1 marks

**Question:** In order to switch on a heater when the temperature falls below a set value, a potential divider is connected to a switching circuit. When the input voltage to the switching circuit falls below $0.5~\text{V}$, it switches the heater on. (a) Copy Figure 25.32 and add a suitable potential divider circuit to trigger the switching circuit. [2] (b) Explain how the operator could lower the temperature at which the heater is switched on. [1]

**Method:**
1. (a) NTC thermistor in series with a fixed resistor across the supply. Put the THERMISTOR between the positive supply and the output point, and the fixed resistor between the output point and $0~\text{V}$, with the output taken across the fixed resistor and fed to the switching circuit. Then $V_{\text{out}} = V_s \times \frac{R_{\text{fixed}}}{R_T + R_{\text{fixed}}}$: when the temperature falls, $R_T$ rises and $V_{\text{out}}$ falls. Choose the resistor so $V_{\text{out}} = 0.5~\text{V}$ at the set temperature. [2]
2. (b) Increase the resistance of the fixed resistor (use a variable resistor and increase its setting). For any given temperature $V_{\text{out}}$ rises, so the temperature must fall further (to a larger $R_T$) before $V_{\text{out}}$ reaches $0.5~\text{V}$: the heater switches on at a lower temperature. [1]

**Answer:** (a) thermistor to $+V_s$, fixed (or variable) resistor to $0~\text{V}$, output across the fixed resistor to the switching circuit; (b) increase the fixed resistance.

**What the examiner wants:** part (a) 2 marks: the divider with the thermistor (1) and the output position across the fixed resistor so the voltage falls when cold (1). Part (b): increasing $R_{\text{fixed}}$ raises the output for a given temperature, so the switch-on temperature drops.

### Example 14: Room light monitor - End-of-chapter Q14, 3 + 1 marks

**Question:** Figure 25.33 shows a circuit used to monitor the variation of light intensity in a room: component X and a variable resistor form a potential divider across a supply, and the potential at their junction feeds one input of an op-amp comparator whose other input is a reference voltage; the op-amp output drives an output device. (a) Identify the component X and describe how the circuit works. [3] (b) Suggest the reason for including the variable resistor in the circuit. [1]

**Method:**
1. (a) X is a light-dependent resistor (LDR). The LDR and the variable resistor form a potential divider, so the p.d. across the LDR (or across the variable resistor) changes as the room light intensity changes: brighter light lowers $R_{\text{LDR}}$ and changes the junction potential. The op-amp compares this potential with the reference at its other input; when the light intensity crosses the threshold, the huge open-loop gain drives the output from one supply rail to the other. The output voltage therefore switches sharply when the light intensity passes the set level, which can be used to operate an indicator. [3]
2. (b) The variable resistor sets the light intensity at which the output switches (the threshold level) - it can be adjusted to the required "trigger" brightness. [1]

**Answer:** (a) X is an LDR; the divider output changes with light intensity and the comparator switches its output between the supply rails when the intensity crosses the reference level; (b) the variable resistor sets the threshold light intensity at which the output switches.

**What the examiner wants:** part (a) 3 marks: identifying X as the LDR (1), the potential-divider action producing a voltage that changes with light (1), and the comparison/switching action of the op-amp (1). Part (b): "sets the level at which the circuit switches" (1).

## 6. Cheat Sheet

**One-glance revision block.**

Formulas (all of them):

$$ V_{\text{out}} = \frac{R_2}{R_1 + R_2} V_s, \qquad V_{\text{out}} = G_0 (V_+ - V_-), \qquad G = -\frac{R_f}{R_{\text{in}}}, \qquad G = 1 + \frac{R_1}{R_2}, \qquad \frac{\delta R}{R} = \frac{\delta L}{L} \text{ or } \frac{2\,\delta L}{L}, \qquad \text{strain} = \frac{\delta L}{L}, \qquad R = \frac{V_s - 2~\text{V}}{I} $$

Rules that win marks:

- **Sensing system = sensing device + processor + output device.** Learn to label all three.
- **LDR: resistance DOWN as light intensity UP. NTC thermistor: resistance DOWN as temperature UP.** Never reverse these.
- **Sensor in a potential divider:** output across the sensor falls as the quantity rises; output across the fixed resistor rises. To make the output increase with the quantity, take it across the fixed resistor.
- **Comparator:** $V_+ > V_-$ gives $+V_s$; $V_+ < V_-$ gives $-V_s$. Compute BOTH input potentials from their own dividers first.
- **Ideal op-amp:** infinite open-loop gain, infinite input resistance, zero output resistance, infinite bandwidth, infinite slew rate, zero noise.
- **Inverting:** $G = -R_f/R_{\text{in}}$, output $180^\circ$ out of phase, input resistance $= R_{\text{in}}$, virtual earth at $(-)$.
- **Non-inverting:** $G = 1 + R_1/R_2$, output in phase, gain always $\geq 1$, very high input resistance.
- **Saturation:** the output can never exceed the supply rails - clamp any absurd $V_{\text{out}}$ at $\pm V_s$.
- **Negative feedback benefits:** less distortion, increased bandwidth, more stable gain, low output resistance. Price: lower gain.
- **Relay needs a reverse-biased diode across the coil** (back e.m.f. protection when the coil switches off).
- **LED needs a series resistor:** $R = (V_{\text{out}} - 2~\text{V})/I$ with $I \approx 20~\text{mA}$.
- **Strain gauge:** $\delta R \propto \delta L$; strain $= \delta L/L$ (no units); the gauge's strain equals the surface's strain.

Common traps in one line each:

- Reversing which resistance rises/falls (LDR vs NTC thermistor).
- Forgetting saturation: quoting 5000 V from $G_0 = 10^5$.
- Dropping the minus sign in the inverting gain.
- Forgetting the $+1$ in the non-inverting gain.
- Putting the sensor output across the wrong resistor when designing dividers.
- Saying the virtual earth is "connected to earth".
- Not subtracting the LED's $2~\text{V}$ (or leaving mA as A).
- Forgetting the relay's protection diode.
- Using $\delta R/R = \delta L/L$ when the volume is constant (use $2\,\delta L/L$).
- Leaving the meter scale linear when the sensor is non-linear (calibrate!).

## 7. Common Exam Mistakes

From examiner reports (June 2023 series) and the coursebook's own question traps, these are the actual reasons candidates lose marks on this chapter:

1. **Reversing the sensor behaviour.** The June 2023 report found candidates deciding the LDR resistance rises with light and the thermistor resistance falls when cold - both backwards. Learn the two phrases exactly: LDR resistance decreases as light intensity increases; NTC thermistor resistance decreases as temperature increases.

2. **Not applying the potential divider principle.** The June 2023 report: many candidates could not relate the p.d. across a resistor to its resistance in a series circuit, and some wrongly assumed the current in the thermistor differed from the current in the fixed resistor. In series the current is the SAME everywhere; the voltage splits in proportion to the resistances.

3. **Weak application of dividers to sensor circuits.** The June 2023 report again noted candidates "found it difficult to apply their understanding of potential divider circuits" to thermistor and LDR questions. Practise $V_{\text{out}} = \frac{R_2}{R_1 + R_2} V_s$ until it is automatic.

4. **Poor circuit diagrams.** The June 2023 report: "Only a small proportion of the diagrams showed the correct circuit symbols for the heater and the light-dependent resistor." Learn the standard symbols (LDR, thermistor, relay, LED, op-amp triangle, cell) and draw tidy, labelled diagrams with the supply and $0~\text{V}$ line shown.

5. **Forgetting saturation.** Writing $V_{\text{out}} = 10^5 \times 0.05 = 5000~\text{V}$ when the supplies are $\pm 9~\text{V}$ loses the mark: clamp the output at the rails and state "saturated at $\pm V_s$".

6. **Sign and configuration errors.** Mixing up inverting ($G = -R_f/R_{\text{in}}$, $180^\circ$ out of phase) and non-inverting ($G = 1 + R_1/R_2$, in phase); dropping the minus sign or the $+1$; wrong phase in sketch graphs.

7. **Virtual earth misconceptions.** "Connected to earth" scores zero: the inverting input sits at almost $0~\text{V}$ (not connected) because the high open-loop gain drives the input difference to zero.

8. **"State and explain" without the explanation.** When the command word is "state and explain", a bare statement (e.g. "the resistance increases") earns only the state mark; the explanation (why: longer and narrower wire, $R = \rho L/A$) earns the second.

9. **Comparator errors.** Answering with the input difference instead of the OUTPUT state; skipping the divider calculations. Find $V_+$ and $V_-$ first, then apply $V_+ > V_-$ gives $+V_s$.

10. **Strain gauge slips.** Using $\delta R/R = \delta L/L$ when the volume stays constant (use $2\,\delta L/L$); mixing cm and m; quoting units for strain (it is a ratio). State $\delta R \propto \delta L$.

11. **LED series resistor errors.** Forgetting to subtract the LED's $2~\text{V}$, or using $I = 20$ instead of $0.020~\text{A}$.

12. **Relay protection.** Omitting the reverse-biased diode across the coil (it conducts the induced current when the coil switches off, so the back e.m.f. cannot damage the op-amp).

13. **Gain limits not checked.** The maximum usable gain is set by the supply: $G_{\text{max}} = V_s / V_{\text{in(max)}}$. Candidates quote $750$ without converting $20~\text{mV}$ to volts, or choose resistors that give a larger gain.

14. **Calibration confusion.** Assuming a voltmeter reading is proportional to temperature or light. It is not (sensors are non-linear): the meter must be calibrated against a known standard and a calibration graph (or marked non-linear scale) used. "The scale is non-linear" is a mark-winning phrase.

---

# Chapter 27: Charged Particles - CAIE A Level Physics (9702) Study Notes

## 2. Definition Sheet

Every definition you must know word-perfect for the exam. Learn these exactly - the wording is what the mark schemes award.

> **Magnetic force on a moving charge:** the force experienced by a charge moving through a magnetic field. Its magnitude is $F = BQv\sin\theta$, where $\theta$ is the angle between the velocity and the field; the force acts at right angles to both the velocity and the field.
>
> Mark scheme: "force is proportional to $B$, $Q$ and $v$" plus "at right angles to the velocity" for the direction. For an electron, $F = Bev$.

> **Fleming's left-hand rule:** with the thumb, first finger and second finger of the left hand at right angles, the first finger points in the direction of the magnetic field, the second finger in the direction of the conventional current (flow of positive charge), and the thumb in the direction of the force on the charge.
>
> Mark scheme: the trap is using the *conventional* current direction - for electrons the second finger points opposite to the motion. State all three assignments.

> **Right-hand palm rule:** with the right hand flat, fingers pointing along the velocity of a positive charge and the palm facing the field, the thumb points in the direction of the force. For negative charges, use the left hand or reverse the direction.

> **Specific charge (charge-to-mass ratio):** the charge of a particle divided by its mass, $\frac{Q}{m}$, in C kg$^{-1}$. For the electron, $\frac{e}{m_e} = 1.76 \times 10^{11}~\text{C kg}^{-1}$.
>
> Mark scheme: "charge per unit mass" - the word "specific" means "per unit mass".

> **Centripetal force:** the resultant force on a body moving in a circle, directed towards the centre of the circle, of magnitude $\frac{mv^2}{r}$. In a uniform magnetic field the magnetic force $BQv$ provides the centripetal force, so $r = \frac{mv}{BQ}$.

> **Velocity selector:** a device using crossed electric and magnetic fields at right angles to each other, through which only particles of speed $v = \frac{E}{B}$ pass undeflected, because for that speed the electric and magnetic forces balance.
>
> Mark scheme: both forces balance ($Eq = Bqv$); faster particles are beaten by the stronger magnetic force, slower ones by the electric force.

> **Hall effect:** the sideways deflection of charge carriers in a current-carrying conductor placed in a magnetic field at right angles to the current, causing charge to separate and a p.d. (the Hall voltage) to appear across the conductor.
>
> Mark scheme: "charge carriers pushed to one side by the magnetic force" plus "a p.d. appears across the conductor". The sign of $V_H$ identifies the sign of the carriers.

> **Hall voltage:** the p.d. that appears between the two opposite sides of a current-carrying strip in a magnetic field, $V_H = \frac{BI}{ntq}$.
>
> Mark scheme: $V_H \propto B$ for fixed current is the phrase that earns the mark in probe questions; "depends on thickness $t$, not width $d$" is the common follow-up.

> **Number density of charge carriers ($n$):** the number of free charge carriers per unit volume of a material, in m$^{-3}$. It links current to drift velocity via $I = nAqv$, and it is far smaller in semiconductors than in metals.

> **Drift velocity ($v$):** the average velocity of the charge carriers along a conductor when a current flows, $v = \frac{I}{nAq}$. For the same current, carriers in a semiconductor drift much faster than in a metal because $n$ is much smaller.

> **Crossed fields:** electric and magnetic fields applied in the same region at right angles to each other. Used in velocity selectors and in Thomson's method, where the two forces on a particle can be balanced so that it travels undeflected.

> **Thomson's method:** measuring $\frac{e}{m_e}$ by accelerating electrons through a known p.d. $V_{ca}$ (so $eV_{ca} = \frac{1}{2}m_ev^2$) and measuring the radius $r$ of their circular path in a known field $B$, giving $\frac{e}{m_e} = \frac{2V_{ca}}{B^2r^2}$.

> **Millikan's oil-drop experiment:** measured the elementary charge $e$ by balancing electric and gravitational forces on charged oil droplets; every droplet's charge was an integer multiple of $e = 1.60 \times 10^{-19}~\text{C}$.

## 3. Formula Sheet

**Quick reference:**

$$F = BQv\sin\theta, \qquad r = \frac{mv}{BQ}, \qquad p = BQr, \qquad eV = \frac{1}{2}mv^2, \qquad \frac{e}{m_e} = \frac{v}{Br} = \frac{2V}{B^2r^2}, \qquad v = \frac{E}{B}, \qquad E = \frac{V}{d}, \qquad V_H = \frac{BI}{ntq} = Bvd, \qquad I = nAqv$$

| Formula | Meaning of symbols | Units | When to use it |
| --- | --- | --- | --- |
| $$F = BQv\sin\theta$$ | $F$ magnetic force, $B$ flux density, $Q$ charge, $v$ speed, $\theta$ angle between velocity and field | $F$ in N, $B$ in T, $Q$ in C, $v$ in m s$^{-1}$ | Force on a charge moving in a magnetic field; at right angles $\theta = 90^{\circ}$ so $F = BQv$ |
| $$F = Bev$$ | $B$ flux density, $e$ elementary charge, $v$ speed | N | Force on an electron; also the "Bev force" behind the motor effect |
| $$r = \frac{mv}{BQ}$$ | $r$ orbit radius, $m$ mass, $v$ speed, $B$ flux density, $Q$ charge | $r$ in m, $m$ in kg, $v$ in m s$^{-1}$, $B$ in T, $Q$ in C | Radius of circular path of a charge in a uniform field (centripetal force $= BQv$) |
| $$p = BQr$$ | $p$ momentum, $B$ flux density, $Q$ charge, $r$ radius | kg m s$^{-1}$ | Momentum form of the orbit equation; the form on the data sheet |
| $$eV = \frac{1}{2}mv^2$$ | $e$ elementary charge, $V$ accelerating p.d., $m$ mass, $v$ speed | $V$ in V, $v$ in m s$^{-1}$ | Speed gained by an electron accelerated through a p.d. (work done $eV$ becomes kinetic energy) |
| $$\frac{e}{m_e} = \frac{2V}{B^2r^2}$$ | $e/m_e$ specific charge, $V$ accelerating p.d., $B$ flux density, $r$ radius | C kg$^{-1}$ | Charge-to-mass ratio of the electron from accelerating p.d. and orbit radius |
| $$v = \frac{E}{B}$$ | $v$ speed, $E$ electric field strength, $B$ flux density | $v$ in m s$^{-1}$, $E$ in V m$^{-1}$, $B$ in T | Speed of a particle passing undeflected through crossed fields (velocity selector) |
| $$E = \frac{V}{d}$$ | $E$ field strength between plates, $V$ p.d. between plates, $d$ plate separation | V m$^{-1}$ | Field between parallel plates; combine with $v = E/B$ to get $v = \frac{V}{Bd}$ |
| $$V_H = \frac{BI}{ntq}$$ | $V_H$ Hall voltage, $B$ flux density, $I$ current, $n$ number density of carriers, $t$ thickness, $q$ charge per carrier | $V_H$ in V, $B$ in T, $I$ in A, $n$ in m$^{-3}$, $t$ in m, $q$ in C | Hall voltage across a strip; for electrons use $q = e$. Thickness $t$, never the width |
| $$V_H = Bvd$$ | $V_H$ Hall voltage, $B$ flux density, $v$ drift velocity, $d$ width of strip | V | Hall voltage from drift velocity and width (equilibrium form, $qE = Bqv$) |
| $$I = nAqv$$ | $I$ current, $n$ number density, $A$ cross-sectional area, $q$ charge per carrier, $v$ drift velocity | $I$ in A, $A$ in m$^2$, $v$ in m s$^{-1}$ | Relating current to drift velocity; combine with the Hall derivation ($A = dt$) |

Constants you will need: $e = 1.60 \times 10^{-19}~\text{C}$; $m_e = 9.11 \times 10^{-31}~\text{kg}$; $\frac{e}{m_e} = 1.76 \times 10^{11}~\text{C kg}^{-1}$. Particle data from the chapter's questions: proton mass $= 1.67 \times 10^{-27}~\text{kg}$, charge $+e$; helium nucleus ($\alpha$-particle) mass $= 6.8 \times 10^{-27}~\text{kg}$, charge $+2e$; electron mass $\approx \frac{1}{1836}$ of the proton mass.

**Exam fact:** $F = BQv$ (including the $\sin\theta$ version) is given on the data sheet, and the orbit radius appears on the data sheet in the momentum form $p = BQr$. The rest of the chapter's key results - $v = \frac{E}{B}$ for the velocity selector, $V_H = \frac{BI}{ntq}$ for the Hall voltage, and $\frac{e}{m_e} = \frac{2V}{B^2r^2}$ - are built from $F = BQv$ plus formulas you already know ($E = \frac{V}{d}$, $eV = \frac{1}{2}mv^2$, $I = nAqv$). Learn to derive them quickly: the derivations are routinely asked as questions in their own right.

## 4. Methods (Question Types & Methods)

These are the ways Cambridge has actually asked about charged particles. Each method below is what a full-mark answer looks like.

### 1. Force on a moving charge ($F = BQv\sin\theta$)

**Method:**
1. Check the angle between the velocity and the field. At right angles, $\sin\theta = 1$ and $F = BQv$.
2. Convert $B$ to tesla (mT to T: $\times 10^{-3}$) and $v$ to m s$^{-1}$.
3. For an electron use $Q = e = 1.60 \times 10^{-19}~\text{C}$; for a helium nucleus $Q = 2e = 3.2 \times 10^{-19}~\text{C}$.
4. Substitute and quote $F$ in newtons.

**Traps:** forgetting the $\sin\theta$ when the motion is not perpendicular; leaving $B$ in mT; using the electron mass instead of the proton mass in $F = BQv$ (mass is not needed at all for the force); confusing $Q$ with the number of charges.

### 2. Direction of the force (Fleming's left-hand rule / right-hand palm rule)

**Method:**
1. Identify the charge sign. Positive charge: conventional current is in the direction of motion. Negative charge (electron): conventional current is opposite to the motion.
2. Left hand: first finger along $B$, second finger along the conventional current, thumb gives the force.
3. Alternative for a positive charge: right-hand palm rule (fingers along $v$, field into palm, thumb gives $F$). For an electron, use the left hand or flip the answer.
4. Check the force is perpendicular to both $B$ and $v$ - if your answer is not, you have misapplied the rule.

**Traps:** using the electron motion as the current direction (the #1 direction error); using the right hand for electrons; forgetting that reversing $B$ or reversing the charge sign reverses the force.

### 3. Circular orbit radius ($r = \frac{mv}{BQ}$, $p = BQr$)

**Method:**
1. State that the magnetic force provides the centripetal force: $\frac{mv^2}{r} = BQv$.
2. Rearrange to $r = \frac{mv}{BQ}$.
3. Convert everything to SI ($B$ in T, $r$ in m, masses as given).
4. Use $r \propto v$, $r \propto m$, $r \propto \frac{1}{B}$ for the qualitative "what happens if..." parts.
5. Sanity-check the magnitude: electron orbits are centimetres to millimetres; proton orbits in Earth-scale fields can be hundreds of metres.

**Traps:** cancelling $v$ wrongly (leaving $r = \frac{m}{BQ}$ without the $v$); using diameter where radius is needed; mixing up which particle's mass to use; not realising the field changes only direction, so $v$ stays constant.

### 4. Speed of electrons from an accelerating p.d. ($eV = \frac{1}{2}mv^2$)

**Method:**
1. Write the energy equation: work done $eV$ becomes kinetic energy $\frac{1}{2}mv^2$.
2. Convert the p.d. to volts (kV to V: $\times 10^3$).
3. Solve: $v = \sqrt{\frac{2eV}{m}}$, or use the given $\frac{e}{m}$ directly: $v = \sqrt{2\left(\frac{e}{m}\right)V}$.
4. Quote $v$ in m s$^{-1}$; electron speeds from kilovolt tubes are of order $10^7~\text{m s}^{-1}$.

**Traps:** leaving the p.d. in kV; using $eV$ but forgetting the $\frac{1}{2}$; using the wrong mass (the electron mass is $9.11 \times 10^{-31}~\text{kg}$, about 1836 times lighter than a proton); not linking this equation to the orbit equation when finding $\frac{e}{m}$.

### 5. Charge-to-mass ratio ($\frac{e}{m_e}$) from deflection

**Method:**
1. Measure the accelerating p.d. $V_{ca}$ (gives the speed via $eV_{ca} = \frac{1}{2}m_ev^2$).
2. Measure the orbit radius $r$ in a known field $B$.
3. Eliminate $v$: $\frac{e}{m_e} = \frac{v}{Br} = \frac{2V_{ca}}{B^2r^2}$.
4. Alternatively, in a velocity-selector arrangement, measure $E$ and $B$ that balance (beam straight), giving $v = \frac{E}{B}$, then use $r = \frac{mv}{Be}$.
5. Combine with Millikan's $e$ to get $m_e = \frac{e}{e/m_e}$.

**Traps:** substituting the plate p.d. instead of the accelerating p.d.; forgetting to square both $B$ and $r$; unit errors with kV and mT; saying Thomson measured $e$ or $m_e$ directly (he measured only the ratio).

### 6. Velocity selector ($v = \frac{E}{B}$)

**Method:**
1. Balance the forces: $Eq = Bqv$, cancel $q$.
2. $v = \frac{E}{B}$. If given plate p.d. and separation, use $E = \frac{V}{d}$ so $v = \frac{V}{Bd}$.
3. Faster particles: magnetic force wins (it grows with $v$), deflected one way. Slower: electric force wins, deflected the other way.
4. State that gravity is negligible.

**Traps:** forgetting $q$ cancels (selected speed independent of charge and mass); swapping $E$ and $B$; not converting $d$ to metres; saying "all particles pass" instead of "only particles at $v = \frac{E}{B}$".

### 7. Electric vs magnetic deflection (path shapes)

**Method:**
1. Electric field: constant force $EQ$; constant acceleration; parabolic path between the plates; straight line outside. Faster electrons are deflected less (less time in the field).
2. Magnetic field: force $BQv$ perpendicular to velocity; circular arc inside the field; straight line outside. Force does no work; speed unchanged.
3. When drawing paths, start the curve where the field region begins and draw a straight line after the particle leaves the region.
4. For a charged particle deflected by an electric field, remember its charge-to-mass ratio determines the acceleration: $a = \frac{EQ}{m}$.

**Traps:** drawing the curve starting before the field region or continuing to curve outside it (a very common examiner-report criticism); forgetting the helium nucleus is charged (it is $+2e$); mixing up "deflected less" for fast particles between the two fields; saying a magnetic field speeds a particle up or slows it down.

### 8. Hall voltage calculation ($V_H = \frac{BI}{ntq}$)

**Method:**
1. Convert $t$ (the thickness) to metres: mm to m is $\times 10^{-3}$; $\mu$m to m is $\times 10^{-6}$.
2. Convert $I$ to amperes and $B$ to tesla.
3. Substitute into $V_H = \frac{BI}{ntq}$, with $q = e = 1.60 \times 10^{-19}~\text{C}$ for electrons.
4. Check the magnitude: semiconductor probes in tesla-strength fields give millivolt-level Hall voltages.
5. Cross-check with the equilibrium form $V_H = Bvd$.

**Traps:** using the width $d$ instead of the thickness $t$ (the width cancels in the derivation - the single most common Hall-effect error); leaving $t$ in mm; using $I$ in mA; dividing by $n$ instead of multiplying by it in the rearrangement for $B$.

### 9. Hall probe: measuring $B$ and identifying charge carriers

**Method:**
1. Fixed current, fixed slice: $V_H \propto B$, so calibrate the meter in known fields and read $B$ directly.
2. Orient the slice perpendicular to the field (the probe measures the component of $B$ perpendicular to the slice: $V_H = V_{\text{max}}\cos\theta$). Rotate the probe to find the maximum reading for an unknown field direction.
3. Sign of carriers: note which face goes negative and apply the left-hand rule to the carrier motion; electrons and positive holes give opposite signs of $V_H$.
4. Explain the design: semiconductor because $n$ is small (and drift velocity large for the same current); thin slice because $V_H \propto \frac{1}{t}$; steady current because the calibration assumes $I$ fixed.

**Traps:** forgetting the probe must be perpendicular to the field; saying "metal" when the probe uses semiconductor (and why); saying $V_H$ depends on the width; missing the constant-current reason in "why must the current be maintained constant?".

### 10. Explanations: why the speed stays constant / why the beam stays tight

**Method:**
1. Speed constant in a magnetic field: the force is always perpendicular to the velocity, so work done $= Fs\cos 90^{\circ} = 0$, kinetic energy unchanged, only the direction changes. Give the whole chain: force perpendicular, no work, no change in KE, speed constant.
2. Tight beam in Thomson's tube: all the particles must have the same mass, charge and speed, because the deflection depends on all three ($a = \frac{EQ}{m}$ for electric, $r = \frac{mv}{BQ}$ for magnetic) - a spread in any of them would smear the beam.
3. Radius decreasing (spiral): the particle loses speed (collisions, ionisation of the gas), and $r = \frac{mv}{BQ} \propto v$, so the orbit tightens.

**Traps:** saying "the magnetic field does work" or "the force slows the electron" (wrong - the force is perpendicular, it does no work); explaining the tight beam with only one of mass/charge/speed; missing the link $r \propto v$ in spiral questions.

### 11. Drift velocity and current ($I = nAqv$)

**Method:**
1. Rearrange $I = nAqv$ for the drift velocity: $v = \frac{I}{nAq}$.
2. Cross-sectional area for a strip: $A = d \times t$ (width times thickness) - use the face perpendicular to the current.
3. Convert the strip dimensions to metres.
4. Use this $v$ in $V_H = Bvd$ as a cross-check on a Hall calculation.

**Traps:** using the wrong face for $A$; mixing up $d$ and $t$; forgetting that in a metal the carriers are electrons ($q = e$); not converting mm to m.

### 12. Definitions (frequent 2-mark questions)

**Method:**
1. **Specific charge:** "charge per unit mass", $\frac{Q}{m}$ in C kg$^{-1}$.
2. **Hall effect:** charge carriers pushed sideways by the magnetic force, producing a p.d. across the conductor.
3. **Velocity selector:** crossed fields where $Eq = Bqv$, so only speed $v = \frac{E}{B}$ passes undeflected.
4. **Why the magnetic force does not change speed:** force at right angles to velocity, so no work is done.

**Traps:** writing formulas without the words (the equation alone usually earns only 1 of the 2 marks); omitting "per unit mass" from specific charge; omitting "perpendicular" from the no-work explanation.

## 5. Solved Examples

Real exam-style questions from the end of Chapter 27, with their mark allocations. The format for every example: Question / Method / Answer / What the examiner wants. Total: 76 marks across the ten questions.

### Example 1: Why the magnetic force does not change the electron's speed - End-of-chapter Q1, 3 marks

**Question:** The magnetic force $BQv$ causes an electron to travel in a circle in a uniform magnetic field. Explain why this force does not cause an increase in the speed of the electron. [3]

**Method:**
1. The magnetic force is always at right angles (perpendicular) to the velocity of the electron.
2. Work done is $W = Fs\cos\theta$ with $\theta = 90^{\circ}$, so the force does no work on the electron.
3. No work means no change in kinetic energy, so the speed stays constant - only the direction of motion changes.

**Answer:** The force is perpendicular to the velocity, does no work, so kinetic energy and speed are unchanged.

**What the examiner wants:** 1 mark for "force perpendicular to velocity", 1 for "no work done", 1 for "kinetic energy/speed unchanged". The phrase "at right angles to the motion" plus "so it does no work" is the full answer; "it is a centripetal force" alone earns only the first mark.

### Example 2: Specific charge of the electron from deflection - End-of-chapter Q2, 4 marks

**Question:** An electron beam is produced from an electron gun in which each electron is accelerated through a p.d. of $1.6~\text{kV}$. When these electrons pass at right angles through a magnetic field of flux density $8.0~\text{mT}$, the radius of curvature of the electron beam is $0.017~\text{m}$. Determine the specific charge of the electron, $\frac{e}{m_e}$. [4]

**Method:**
1. Convert: $V_{ca} = 1.6~\text{kV} = 1600~\text{V}$; $B = 8.0~\text{mT} = 8.0 \times 10^{-3}~\text{T}$.
2. Energy gained: $eV_{ca} = \frac{1}{2}m_ev^2$.
3. Orbit in the magnetic field: $r = \frac{mv}{Be}$.
4. Eliminate $v$: $\frac{e}{m_e} = \frac{2V_{ca}}{B^2r^2}$.
5. $\frac{e}{m_e} = \frac{2 \times 1600}{(8.0 \times 10^{-3})^2 \times (0.017)^2} = \frac{3200}{6.4 \times 10^{-5} \times 2.89 \times 10^{-4}} = \frac{3200}{1.85 \times 10^{-8}}$.

**Answer:** $\frac{e}{m_e} = 1.73 \times 10^{11}~\text{C kg}^{-1}$ (consistent with the accepted value $1.76 \times 10^{11}~\text{C kg}^{-1}$).

**What the examiner wants:** 4 marks: the energy equation (1), the orbit equation (1), eliminating $v$ correctly (1), substitution with converted units and answer with units (1). The classic slips: leaving $V$ in kV and $B$ in mT, or forgetting to square $B$ and $r$.

### Example 3: Alpha and beta particles compared - End-of-chapter Q3, 8 marks

**Question:** An $\alpha$-particle (helium nucleus, mass $4$ times the proton mass, charge $+2e$) and a $\beta$-particle (electron, mass about $\frac{1}{1836}$ of the proton mass, charge $-e$) travel through a uniform magnetic field with the same velocity, at right angles to the field. Determine the ratio of (a) the masses, (b) the charges, (c) the magnetic forces, (d) the radii of the circular orbits of the two particles. [2 each]

**Method:**
1. (a) $m_\alpha = 4 \times m_p$ and $m_\beta = \frac{m_p}{1836}$, so $\frac{m_\alpha}{m_\beta} = 4 \times 1836 = 7344 \approx 7.3 \times 10^3$.
2. (b) $\frac{Q_\alpha}{Q_\beta} = \frac{2e}{e} = 2$ (magnitudes of charge).
3. (c) $F = BQv$ with the same $B$ and $v$: $\frac{F_\alpha}{F_\beta} = \frac{Q_\alpha}{Q_\beta} = 2$.
4. (d) $r = \frac{mv}{BQ}$: $\frac{r_\alpha}{r_\beta} = \frac{m_\alpha}{m_\beta} \times \frac{Q_\beta}{Q_\alpha} = \frac{7344}{2} = 3672 \approx 3.7 \times 10^3$.

**Answer:** (a) $m_\alpha : m_\beta = 7.3 \times 10^3 : 1$; (b) $2 : 1$; (c) $2 : 1$; (d) $r_\alpha : r_\beta = 3.7 \times 10^3 : 1$ (the $\alpha$-particle curves far less tightly).

**What the examiner wants:** each part: 1 mark for the ratio setup and 1 for the arithmetic. Part (c) needs the insight that $F \propto Q$ (the velocity cancels); part (d) combines both ratios. The $\alpha$-particle's radius is about 3700 times the electron's because it is far more massive but only twice as charged.

### Example 4: Two differences between electric and magnetic forces - End-of-chapter Q4, 2 marks

**Question:** A moving charged particle experiences a force in an electric field and also in a magnetic field. State **two** differences between the forces experienced in the two types of field. [2]

**Method:**
1. The electric force acts on a charge whether it is moving or stationary; the magnetic force acts only on a **moving** charge.
2. The electric force can do work and change the speed (kinetic energy) of the particle; the magnetic force is always perpendicular to the velocity, does no work, and never changes the speed.
3. (Alternative third difference, pick any two) The electric force acts along the direction of the field; the magnetic force is perpendicular to both the field and the velocity. The electric force on a given charge is independent of its speed; the magnetic force is proportional to its speed.

**Answer:** Any two of: (1) magnetic force acts only on moving charges, electric force on stationary ones too; (2) magnetic force does no work and cannot change speed, electric force can; (3) electric force along the field, magnetic force perpendicular to field and velocity.

**What the examiner wants:** 1 mark per valid difference, clearly contrasted. "Magnetic is weaker" or "electric is stronger" earns nothing - the differences must be physical properties, not magnitudes.

### Example 5: The spiralling electron in air - End-of-chapter Q5, 8 marks

**Question:** An electron travels in air, rotating clockwise around a uniform magnetic field directed into the plane of the paper; the radius of the orbit gradually decreases. (a)(i) Explain the origin of the force that causes the electron to spiral. [2] (a)(ii) Explain why the radius gradually decreases. [2] (b) At one point the electron's speed is $1.0 \times 10^7~\text{m s}^{-1}$ and the flux density is $0.25~\text{T}$. Calculate (i) the magnetic force on the electron [2] and (ii) the radius of the path. [2]

**Method:**
1. (a)(i) The electron is moving in a magnetic field, so it experiences a force $F = Bev$ perpendicular to its velocity (direction from Fleming's left-hand rule, remembering the conventional current is opposite to the electron's motion); this force acts as the centripetal force towards the centre of the circle.
2. (a)(ii) The electron ionises air molecules and loses kinetic energy, so its speed falls; since $r = \frac{mv}{Be} \propto v$, a smaller speed means a smaller radius and the orbit tightens into a spiral.
3. (b)(i) $F = Bev = 1.60 \times 10^{-19} \times 1.0 \times 10^7 \times 0.25 = 4.0 \times 10^{-13}~\text{N}$.
4. (b)(ii) $r = \frac{mv}{Be} = \frac{9.11 \times 10^{-31} \times 1.0 \times 10^7}{1.60 \times 10^{-19} \times 0.25} = \frac{9.11 \times 10^{-24}}{4.0 \times 10^{-20}} = 2.28 \times 10^{-4}~\text{m}$.

**Answer:** (a)(i) magnetic force $Bev$ perpendicular to the velocity, acting as centripetal force; (a)(ii) speed falls as the electron ionises air molecules, and $r \propto v$; (b)(i) $F = 4.0 \times 10^{-13}~\text{N}$; (b)(ii) $r = 2.3 \times 10^{-4}~\text{m}$.

**What the examiner wants:** (a)(i) 2 marks for the force idea plus perpendicular/centripetal; (a)(ii) 2 marks for the energy loss (collisions with air/gas) AND the link $r \propto v$ - losing the link loses a mark. (b) 2 marks each for correct substitution with units; the magnetic force must NOT be said to do the slowing (it does no work - the gas collisions do).

### Example 6: Deflecting a proton beam to a detector - End-of-chapter Q6, 9 marks

**Question:** Protons travel from a source to a detector through a region of uniform magnetic field (Figure 27.16). (a)(i) Copy the diagram, sketch the proton's path, and draw arrows at two points on the path showing the direction of the magnetic force. [3] (a)(ii) State the direction of the magnetic field within the area shown. [1] (b) The proton's speed is $4.0 \times 10^6~\text{m s}^{-1}$ and the flux density is $0.25~\text{T}$. Calculate (i) the magnitude of the magnetic force [1] and (ii) the radius of curvature of the path. [2] (c) State two changes to the magnetic field that would allow an electron with the same speed to be deflected along the same path. [2]

**Method:**
1. (a)(i) The path is an arc of a circle inside the field region (the force is perpendicular to the velocity), with straight lines before entering and after leaving the region; at every point the force arrow points towards the centre of the arc.
2. (a)(ii) Use Fleming's left-hand rule with the proton's motion as the conventional current direction: for the geometry in the coursebook figure (protons deflected downwards towards the detector), the field must be directed out of the plane of the paper. If your diagram has the detector above the beam line, the field is into the page - the method is what earns the mark, and the rule must be applied to your own sketch.
3. (b)(i) $F = BQv = 0.25 \times 1.60 \times 10^{-19} \times 4.0 \times 10^6 = 1.6 \times 10^{-13}~\text{N}$.
4. (b)(ii) $r = \frac{mv}{BQ} = \frac{1.67 \times 10^{-27} \times 4.0 \times 10^6}{0.25 \times 1.60 \times 10^{-19}} = \frac{6.68 \times 10^{-21}}{4.0 \times 10^{-20}} = 0.167~\text{m}$.
5. (c) The electron has the same charge magnitude but a mass about 1836 times smaller, so at the same speed $r = \frac{mv}{BQ}$ would be 1836 times smaller. To make the electron follow the proton's path: reverse the direction of the magnetic field (the electron is negative, so the force direction flips), and reduce the flux density by the factor $1836$: $B = \frac{0.25}{1836} = 1.4 \times 10^{-4}~\text{T}$.

**Answer:** (a)(ii) out of the plane of the paper for the coursebook geometry (into the page if the detector lies above the beam line - apply the rule to your diagram); (b)(i) $F = 1.6 \times 10^{-13}~\text{N}$; (b)(ii) $r = 0.17~\text{m}$; (c) reverse the field direction and reduce $B$ by a factor of about 1836 (to $\approx 1.4 \times 10^{-4}~\text{T}$).

**What the examiner wants:** (a)(i) 3 marks for the arc inside the region only (1), straight lines outside (1), force arrows (1). (b)(i) 1 mark substitution; (b)(ii) 2 marks for $r = \frac{mv}{BQ}$ with the proton mass. (c) 2 marks: reverse the field for the negative charge AND scale $B$ down by $m_e/m_p$ - both changes needed.

### Example 7: Charge separation in a semiconductor strip - End-of-chapter Q7, 11 marks

**Question:** A thin strip of semiconductor carries a current in a magnetic field at right angles to the current (Figure 27.17). (a) Explain why the charges separate. [3] (b)(i) Add $+$ and $-$ signs to the diagram to show the charge separation. [1] (b)(ii) Explain how an electron is able to move in a straight line along the strip. [1] (c) The Hall voltage is measured with the same slice, current and field at two temperatures, one significantly higher. Describe and explain the changes in the number density, the drift velocity of the carriers, and the Hall voltage. [6]

**Method:**
1. (a) The electrons (charge carriers) drift along the strip with velocity $v$, so each experiences a magnetic force $Bev$ sideways (perpendicular to both the current and the field, from Fleming's left-hand rule). They are pushed towards one side of the strip and accumulate there, leaving the opposite side short of electrons (positive). This separation is the Hall effect.
2. (b)(i) For the standard figure layout (current to the right, field into the page): electrons are pushed to the top face, so mark the top face $-$ and the bottom face $+$. Apply the left-hand rule to your own diagram: conventional current opposite to the electron flow.
3. (b)(ii) The separated charges set up an electric field across the strip; when equilibrium is reached, the electric force $eE$ on each electron is equal and opposite to the magnetic force $Bev$, so the resultant sideways force is zero and the electron continues straight along the strip.
4. (c) Higher temperature: more electrons are promoted into the conduction band, so the number density $n$ increases. With the current fixed, $I = nAqv$ means the drift velocity $v$ decreases (larger $n$ at the same $I$ and $A$). Since $V_H = \frac{BI}{ntq}$, the larger $n$ makes the Hall voltage decrease.

**Answer:** (a) magnetic force $Bev$ pushes drifting electrons sideways, so charge accumulates on the sides; (b)(i) top $-$ and bottom $+$ for the standard layout (use the left-hand rule for your diagram); (b)(ii) electric force balances magnetic force at equilibrium, so the electron travels straight; (c) $n$ increases, $v$ decreases, $V_H$ decreases.

**What the examiner wants:** (a) 3 marks for the magnetic force idea (1), sideways direction (1), accumulation/separation (1). (b)(ii) 1 mark for the balanced forces idea. (c) 6 marks: 2 each for $n$, $v$, $V_H$ with the reasoning linking each change (temperature raises $n$; $I = nAqv$ then lowers $v$; $V_H = \frac{BI}{ntq}$ then falls). Saying only "it gets hotter" without the chain earns nothing.

### Example 8: The electron tube with crossed fields - End-of-chapter Q8, 10 marks

**Question:** Electrons emitted from a cathode accelerate towards an anode at $+1.0~\text{kV}$ and pass into a uniform electric field between parallel plates at $+500~\text{V}$ and $0~\text{V}$, $5.0~\text{cm}$ apart (Figure 27.18). The beam curves upwards. (a)(i) Explain why. [2] (a)(ii) Explain how the pattern on the fluorescent screen shows that all the electrons have the same speed as they leave the anode. [2] (b) Write an equation relating the electron speed $v$ to the anode-cathode p.d. $V_{ac}$. [1] (c)(i) State the direction of the magnetic field that cancels the upward deflection. [1] (c)(ii) Write an equation relating $v$, the electric field $E$ and the flux density $B$ for undeflected passage. [2] (c)(iii) Calculate $B$, given $\frac{e}{m_e} = 1.76 \times 10^{11}~\text{C kg}^{-1}$. [2]

**Method:**
1. (a)(i) The electric field between the plates points from the $+500~\text{V}$ plate to the $0~\text{V}$ plate, i.e. downwards. The electron is negative, so it feels a force opposite to the field direction, i.e. upwards; this constant force deflects the beam upwards in a curve.
2. (a)(ii) The upward deflection depends on how long each electron spends between the plates, which depends on its speed: faster electrons are deflected less. A single sharp spot (rather than a smeared or elongated one) means all the electrons are deflected by the same amount, so they all have the same speed.
3. (b) $eV_{ac} = \frac{1}{2}m_ev^2$, so $v = \sqrt{\frac{2eV_{ac}}{m_e}}$.
4. (c)(i) The magnetic force must act downwards to cancel the upward electric force. Electrons move rightwards (conventional current leftwards), so for the force to be downwards the field must be directed **into the plane of the paper** (left-hand rule).
5. (c)(ii) Balance the forces: $eE = Bev$, so $v = \frac{E}{B}$, with $E = \frac{V}{d}$ between the plates.
6. (c)(iii) $v = \sqrt{2\left(\frac{e}{m_e}\right)V_{ac}} = \sqrt{2 \times 1.76 \times 10^{11} \times 1000} = \sqrt{3.52 \times 10^{14}} = 1.876 \times 10^7~\text{m s}^{-1}$.
7. $E = \frac{V}{d} = \frac{500}{0.05} = 1.0 \times 10^4~\text{V m}^{-1}$.
8. $B = \frac{E}{v} = \frac{1.0 \times 10^4}{1.876 \times 10^7} = 5.33 \times 10^{-4}~\text{T}$.

**Answer:** (a)(i) negative electron pushed opposite to the downward field; (a)(ii) single sharp spot = same deflection = same speed; (b) $eV_{ac} = \frac{1}{2}m_ev^2$; (c)(i) into the plane of the paper; (c)(ii) $v = \frac{E}{B}$; (c)(iii) $B = 5.3 \times 10^{-4}~\text{T}$.

**What the examiner wants:** (a)(i) 2 marks: field direction between the plates (1) and force on a negative charge opposite to the field (1). (a)(ii) 2 marks: deflection depends on speed (1) and the sharp spot proves a single speed (1). (b) 1 mark for the energy equation. (c)(i) 1 mark for into the page. (c)(ii) 2 marks for equating $eE$ and $Bev$. (c)(iii) 2 marks for the two substitutions: $v$ from the accelerating p.d. (1) and $B = E/v$ with converted units (1).

### Example 9: Protons and helium nuclei at the Earth's poles - End-of-chapter Q9, 5 marks

**Question:** Protons and helium nuclei from the Sun enter the Earth's atmosphere above the poles, where the flux density is $6.0 \times 10^{-5}~\text{T}$. They move at $1.0 \times 10^6~\text{m s}^{-1}$ at right angles to the field. (a) Calculate the radius of the path of a proton. [3] (b) Draw a diagram showing the deflection of a proton and of a helium nucleus with the same initial velocity, stating each radius on the diagram. [2] (Mass of helium nucleus $= 6.8 \times 10^{-27}~\text{kg}$; charge on helium nucleus $= 3.2 \times 10^{-19}~\text{C}$; proton mass $= 1.67 \times 10^{-27}~\text{kg}$.)

**Method:**
1. (a) $r = \frac{mv}{BQ} = \frac{1.67 \times 10^{-27} \times 1.0 \times 10^6}{6.0 \times 10^{-5} \times 1.60 \times 10^{-19}} = \frac{1.67 \times 10^{-21}}{9.6 \times 10^{-24}} = 1.74 \times 10^2~\text{m}$.
2. (b) Helium nucleus: $r = \frac{6.8 \times 10^{-27} \times 1.0 \times 10^6}{6.0 \times 10^{-5} \times 3.2 \times 10^{-19}} = \frac{6.8 \times 10^{-21}}{1.92 \times 10^{-23}} = 3.54 \times 10^2~\text{m}$.
3. Both are positive, so both bend the same way (towards the same side); the helium nucleus has the larger radius (about twice the proton's), so it bends less.

**Answer:** (a) $r = 1.7 \times 10^2~\text{m}$; (b) proton radius $1.7 \times 10^2~\text{m}$, helium nucleus radius $3.5 \times 10^2~\text{m}$, both curving the same way with the helium bending less.

**What the examiner wants:** (a) 3 marks: formula (1), correct charge for the proton (1), arithmetic with units (1). (b) 2 marks: correct relative curvature of the two paths (1) and radii stated on the diagram (1). The comparison ratio $\frac{r_{He}}{r_p} = \frac{6.8}{1.67} \times \frac{1.6}{3.2} \approx 2$ is the quickest route to a correct sketch.

### Example 10: The metal strip and the Hall voltage - End-of-chapter Q10, 16 marks

**Question:** Figure 27.19 shows a thin metal strip of thickness $t = 0.030~\text{mm}$ and width $d = 9.0~\text{mm}$ carrying a current $I = 40~\text{mA}$, in a magnetic field $B = 0.60~\text{T}$ at right angles to the current. (a)(i) Mark the side of the strip that becomes negative because of the Hall effect. [1] (a)(ii) State where a voltmeter must be placed to measure the Hall voltage. [1] (b) Derive an expression for the Hall voltage in terms of $I$, $B$, $t$, the number density $n$ of free electrons and the charge $e$ on an electron. [3] (c)(i) Calculate the mean drift velocity of the free electrons, given $n = 8.5 \times 10^{28}~\text{m}^{-3}$. [3] (c)(ii) Calculate the Hall voltage across the strip. [2] (d)(i) Explain, in terms of the movement of electrons, why the Hall voltage increases when $I$ increases. [2] (d)(ii) Explain why a semiconductor is used for a Hall probe rather than metal. [2] (e) Explain why, when the strip is rotated about the horizontal axis XY, the Hall voltage varies between a maximum positive value and a maximum negative value. [2]

**Method:**
1. (a)(i) For the standard figure layout (current to the right, field into the page): the electrons move to the left (opposite the conventional current) and are pushed by the magnetic force towards the top face, so the top face (X) becomes negative. Apply the left-hand rule to your own diagram.
2. (a)(ii) Connect the voltmeter between the two opposite faces of the strip (across X and Y), so it measures the p.d. between the faces that have separated charge.
3. (b) Equilibrium: electric force $=$ magnetic force, $eE = Bev$ with $E = \frac{V_H}{d}$, giving $V_H = Bvd$. Substitute $v = \frac{I}{nAe}$ with cross-sectional area $A = dt$: $V_H = \frac{BId}{nAe} = \frac{BI}{nte}$.
4. (c)(i) $v = \frac{I}{nAe}$ with $A = dt = 9.0 \times 10^{-3} \times 0.030 \times 10^{-3} = 2.7 \times 10^{-7}~\text{m}^2$.
5. $v = \frac{0.040}{8.5 \times 10^{28} \times 2.7 \times 10^{-7} \times 1.60 \times 10^{-19}} = \frac{0.040}{3.67 \times 10^3} = 1.09 \times 10^{-5}~\text{m s}^{-1}$.
6. (c)(ii) $V_H = \frac{BI}{nte} = \frac{0.60 \times 0.040}{8.5 \times 10^{28} \times 0.030 \times 10^{-3} \times 1.60 \times 10^{-19}} = \frac{0.024}{4.08 \times 10^5} = 5.9 \times 10^{-8}~\text{V}$.
7. Cross-check with the equilibrium form: $V_H = Bvd = 0.60 \times 1.09 \times 10^{-5} \times 9.0 \times 10^{-3} = 5.9 \times 10^{-8}~\text{V}$. Consistent.
8. (d)(i) A larger current means a larger drift velocity $v$ (at fixed $n$ and $A$), so the sideways magnetic force $Bev$ on each electron is larger, more charge separates, and the Hall voltage (proportional to the separated charge) increases.
9. (d)(ii) A semiconductor has a much smaller number density of free electrons $n$ than a metal, and $V_H = \frac{BI}{nte}$ is inversely proportional to $n$, so the Hall voltage is much larger for the same current, field and thickness (the electrons also drift faster for the same current).
10. (e) The Hall voltage depends on the component of $B$ perpendicular to the plane of the strip: rotating the strip changes the angle $\theta$ between the field and the normal to the strip, and $V_H = V_{\text{max}}\cos\theta$. As the strip rotates through $180^{\circ}$, this component sweeps from maximum positive through zero to maximum negative, so the measured voltage varies between a maximum positive and a maximum negative value.

**Answer:** (a)(i) top face X negative for the standard layout; (a)(ii) across the two faces X and Y; (b) $V_H = \frac{BI}{nte}$; (c)(i) $v = 1.1 \times 10^{-5}~\text{m s}^{-1}$; (c)(ii) $V_H = 5.9 \times 10^{-8}~\text{V}$; (d)(i) bigger $I$ means bigger $v$, hence bigger sideways force and more separation; (d)(ii) $n$ is far smaller in a semiconductor, so $V_H$ is far larger; (e) $V_H \propto$ component of $B$ perpendicular to the strip, which varies as $\cos\theta$ through a full rotation.

**What the examiner wants:** (a) 1 mark each for the correct face and the voltmeter position. (b) 3 marks for the full derivation: balance $eE = Bev$ (1), substitute $E = \frac{V_H}{d}$ and $v = \frac{I}{nAe}$ (1), substitute $A = dt$ and cancel (1). (c)(i) 3 marks for $I = nAve$ with $A = dt$ and converted units; (c)(ii) 2 marks for $V_H = \frac{BI}{nte}$ (or $V_H = Bvd$ as a check). (d)(i) 2 marks for linking $I$ to $v$ and $v$ to the sideways force. (d)(ii) 2 marks for small $n$ and the inverse proportionality. (e) 2 marks for the perpendicular component idea plus the sign reversal over half a turn.

## 6. Cheat Sheet

**One-glance revision block.**

Formulas (all of them):

$$F = BQv\sin\theta, \qquad r = \frac{mv}{BQ}, \qquad p = BQr, \qquad eV = \frac{1}{2}mv^2, \qquad \frac{e}{m_e} = \frac{2V}{B^2r^2}, \qquad v = \frac{E}{B}, \qquad V_H = \frac{BI}{ntq} = Bvd, \qquad I = nAqv$$

Key numbers: $e = 1.60 \times 10^{-19}~\text{C}$; $m_e = 9.11 \times 10^{-31}~\text{kg}$; $\frac{e}{m_e} = 1.76 \times 10^{11}~\text{C kg}^{-1}$; proton mass $1.67 \times 10^{-27}~\text{kg}$; helium nucleus mass $6.8 \times 10^{-27}~\text{kg}$, charge $+2e$; electron mass $\approx m_p/1836$.

Rules that win marks:

- **The magnetic force never changes speed.** It is perpendicular to the velocity, does no work, so KE is constant. Only gas collisions slow real electrons.
- **Left-hand rule for direction:** first finger field, second finger conventional current, thumb force. Electrons: current is opposite to their motion. Positive charge: current with their motion.
- **$r = \frac{mv}{BQ}$:** faster and heavier particles make bigger circles; stronger field makes tighter circles. Momentum form $p = BQr$ is what the data sheet shows.
- **Velocity selector:** balance $Eq = Bqv$; only $v = \frac{E}{B}$ passes straight. Faster particles lose to the magnetic force, slower ones to the electric force. The charge cancels, so the selected speed is the same for all particles.
- **Thomson:** $eV_{ca} = \frac{1}{2}mv^2$ plus $r = \frac{mv}{Be}$ gives $\frac{e}{m_e} = \frac{2V_{ca}}{B^2r^2}$. He measured the ratio only; Millikan measured $e$; then $m_e = e/(e/m_e)$.
- **Hall voltage:** $V_H = \frac{BI}{ntq}$ uses the THICKNESS $t$ (the width cancels in the derivation). Thin slice and small $n$ (semiconductor) give big voltages.
- **Hall probe:** $V_H \propto B$ at fixed current, so calibrate and read $B$; orient the slice perpendicular to the field; sign of $V_H$ reveals the sign of the carriers; rotating the probe sweeps $V_H$ from $+V_{\text{max}}$ through zero to $-V_{\text{max}}$.
- **Electric vs magnetic deflection:** electric force is independent of speed, does work, parabolic path; magnetic force grows with speed, does no work, circular arc.

Common traps in one line each:

- Forgetting $\sin\theta$ when the motion is at an angle to $B$.
- Leaving $B$ in mT or $V$ in kV (both are $\times 10^{-3}$... kV to V is $\times 10^3$).
- Putting the second finger along the electron's motion instead of the conventional current.
- Saying the magnetic field speeds up or slows down particles (it cannot - no work).
- Using the width $d$ in $V_H = \frac{BI}{ntq}$ instead of the thickness $t$.
- Leaving the strip thickness in mm in a Hall calculation.
- Using the plate p.d. instead of the accelerating p.d. in $\frac{e}{m} = \frac{2V}{B^2r^2}$.
- Drawing the curved path starting before the field region or continuing after it.
- Thinking a helium nucleus is uncharged (it is $+2e$).
- Forgetting that in a metal the charge carriers are electrons (negative), so the Hall sign flips.

## 7. Common Exam Mistakes

From examiner reports and the coursebook's own questions, these are the actual reasons candidates lose marks on this chapter:

1. **Direction errors with negative charges.** The #1 error in this chapter is applying Fleming's left-hand rule with the second finger along the electron's actual motion. Conventional current flows opposite to electron motion, so the second finger must point the other way. Reversing the field or the charge sign reverses the force; forgetting this loses whole direction questions. The examiner reports note that in Hall-effect-style multiple-choice questions only the stronger candidates got past the first step (electrons pushed to one face) to the force balance that actually sets the Hall voltage.

2. **Forgetting $\sin\theta$.** The force is $F = BQv\sin\theta$ whenever the velocity is at an angle to the field. Questions deliberately set the beam at $45^{\circ}$ (or any non-right angle) to test this. At right angles the $\sin$ term is 1, but writing it every time protects you.

3. **Unit slips on $B$, $V$ and $t$.** $8.0~\text{mT}$ is $8.0 \times 10^{-3}~\text{T}$ and $1.6~\text{kV}$ is $1600~\text{V}$; leaving prefixes in place ruins $\frac{e}{m} = \frac{2V}{B^2r^2}$. In Hall questions the thickness is routinely given in mm and must go to metres.

4. **Claiming the magnetic field changes the particle's speed.** The force is always perpendicular to the velocity, so it does no work and cannot change kinetic energy. Saying "the field slows the electron" in the spiral question (Q5) is wrong - the electron loses energy to the gas molecules it ionises, not to the field.

5. **Confusing electric and magnetic force properties.** Electric force acts on stationary charges, is independent of speed, and does work; magnetic force acts only on moving charges, grows with speed, and does no work. Mixing these up loses the standard 2-mark difference question (Q4) and the reasoning in deflection questions.

6. **Using the width instead of the thickness in the Hall voltage.** The derivation cancels the width $d$: $V_H = \frac{BI}{ntq}$ depends on the thickness $t$ only. Candidates who substitute the strip's width are usually off by orders of magnitude. Related slip: quoting the Hall voltage formula with $d$ in it.

7. **Path-drawing errors in deflection questions.** Examiner reports on the proton-in-an-electric-field question report paths that start curving before the field region and keep curving after it. The path is straight, then an arc (or parabola) strictly inside the region, then straight again.

8. **Not realising the helium nucleus is charged.** In the proton/helium deflection question, a significant number of candidates treated the helium nucleus as neutral and said it would be unaffected by the fields. It carries $+2e$ and is deflected the same way as a proton, just with a larger radius (higher mass-to-charge ratio).

9. **Ignoring the charge-to-mass ratio in deflection comparisons.** The acceleration is $a = \frac{EQ}{m}$ and the orbit radius is $r = \frac{mv}{BQ}$: the ratio $\frac{Q}{m}$ decides everything. Candidates who compare only charge or only mass get the wrong conclusions; the report notes very few separated the velocity into components and used $\frac{Q}{m}$.

10. **Forgetting the accelerating p.d. in $\frac{e}{m}$ questions.** The formula $\frac{e}{m_e} = \frac{2V}{B^2r^2}$ uses the p.d. between the cathode and anode ($V_{ca}$), not the p.d. between the deflecting plates. Substituting the wrong voltage, or leaving it in kV, is the standard error in this question type.

11. **Incomplete Hall-probe explanations.** "Semiconductor because it gives a bigger voltage" earns half marks: the chain is that $n$ is much smaller and $V_H \propto \frac{1}{n}$. "The current must stay constant" also needs the reason: the calibration $V_H \propto B$ assumes $I$ fixed.

12. **No sanity check on magnitudes.** The examiner reports urge candidates to check answers are sensible: an electron orbit is centimetres to millimetres, a proton orbit in 0.25 T is about 0.17 m, a metal strip's Hall voltage is sub-microvolt while a semiconductor probe gives millivolts. A radius of $10^{14}~\text{m}$ means a unit or formula error - go back and find it.

---

# Chapter 28: Electromagnetic Induction - CAIE A Level Physics (9702) Study Notes

## 2. Definition Sheet

Every definition you must know word-perfect for the exam. Learn these exactly — the wording is what the mark schemes award.

> **Magnetic flux ($\Phi$):** the product of the magnetic flux density and the area perpendicular to the field: $\Phi = BA\cos\theta$, where $\theta$ is the angle between the field and the normal to the area. Unit: weber (Wb), where $1~\text{Wb} = 1~\text{T m}^2$. Flux is a scalar.
>
> Mark scheme: must include "$BA$" and "perpendicular" or "$\cos\theta$" and the unit Wb. Saying "number of field lines" alone earns at most 1 mark.

> **Magnetic flux linkage ($N\Phi$):** the product of the number of turns $N$ of a coil and the magnetic flux $\Phi$ through each turn: $\text{flux linkage} = N\Phi = BAN\cos\theta$. Unit: weber-turns (Wb turns). For $N = 1$, flux linkage equals flux.
>
> Mark scheme: the "$N$" is compulsory when a coil is involved; "flux linkage" is not the same as "flux" — using one for the other loses the mark.

> **Weber (definition):** one weber is the magnetic flux through an area of $1~\text{m}^2$ perpendicular to a uniform magnetic flux density of $1~\text{T}$: $1~\text{Wb} = 1~\text{T m}^2$.
>
> Mark scheme: "$\text{T m}^2$" or "field of $1~\text{T}$ through $1~\text{m}^2$ perpendicular" earns the mark.

> **Faraday's law of electromagnetic induction:** the magnitude of the induced e.m.f. is proportional to the rate of change of magnetic flux linkage: $E \propto \frac{\Delta(N\Phi)}{\Delta t}$, or with coherent SI units $E = \frac{\Delta(N\Phi)}{\Delta t}$.
>
> Mark scheme: "proportional to the rate of change of (magnetic) flux linkage" — must say "rate of change" and "flux linkage" (not just "flux" when a coil is involved, not just "flux linkage changes").

> **Lenz's law:** the direction of the induced e.m.f. (and hence of any induced current) is such that it opposes the change that produces it (the change in magnetic flux linkage).
>
> Mark scheme: "opposes the change in flux / flux linkage" — must include "change" and the thing opposed is the flux, not the motion or the field. This is conservation of energy.

> **Fleming's right-hand rule (generator rule):** with the thumb, first finger and second finger of the right hand held mutually at right angles, the thu**M**b points in the direction of **M**otion of the conductor, the **F**irst finger points in the direction of the magnetic **F**ield (N to S), and the se**C**ond finger points in the direction of the (conventional) induced **C**urrent.
>
> Mark scheme: all three assignments must be correct; using the left hand is a motor-rule answer and earns zero.

> **Eddy currents:** circulating electric currents induced in a solid conductor by a changing magnetic flux through the conductor. By Lenz's law their magnetic field opposes the change in flux, producing a braking or damping force and dissipating energy as heat ($I^2R$).
>
> Mark scheme: "currents induced in the conductor / metal" + "oppose the change / motion" (Lenz) + "cause heating / energy loss" earns full marks.

> **Generator (alternator principle):** a device that converts mechanical energy into electrical energy by rotating a coil in a magnetic field so that the magnetic flux linkage through the coil changes continuously, inducing an alternating e.m.f. by Faraday's law: $E = BAN\omega\sin\omega t$.
>
> Mark scheme: "coil rotates in a magnetic field" + "changing flux linkage" + "induces an e.m.f. (by Faraday's law)" earns the marks.

> **Rate of change of flux linkage:** the change in $N\Phi$ per unit time, $\frac{\Delta(N\Phi)}{\Delta t}$, in Wb s$^{-1}$ (= V). Its magnitude equals the induced e.m.f.; its sign (via Lenz, $E = -d(N\Phi)/dt$) gives the direction. The induced e.m.f. is **maximum when the rate of change is maximum**, not when the flux itself is maximum.

## 3. Formula Sheet

**Quick reference:**

$$\Phi = BA\cos\theta, \qquad N\Phi = BAN\cos\theta, \qquad E = \frac{\Delta(N\Phi)}{\Delta t}, \qquad E = -\frac{d(N\Phi)}{dt}, \qquad E = Blv, \qquad E_0 = BAN\omega, \quad [1~\text{Wb} = 1~\text{T m}^2]$$

| Formula | Meaning of symbols | Units | When to use it |
|---|---|---|---|
| $$\Phi = BA\cos\theta$$ | $\Phi$ magnetic flux, $B$ flux density, $A$ area, $\theta$ angle between field and normal to area | $\Phi$ in Wb, $B$ in T, $A$ in m$^2$, $\theta$ in rad/° | Flux through a loop or area; if $B$ is perpendicular to the plane, $\Phi = BA$ |
| $$N\Phi = BAN\cos\theta$$ | $N\Phi$ flux linkage, $N$ turns, $B$ flux density, $A$ area | Wb turns | Flux linkage for a coil; the form Faraday's law uses |
| $$E = \frac{\Delta(N\Phi)}{\Delta t}$$ | $E$ induced e.m.f. magnitude, $N\Phi$ flux linkage, $t$ time | $E$ in V, $N\Phi$ in Wb, $t$ in s, $\frac{\text{Wb}}{\text{s}} = \text{V}$ | Faraday's law magnitude; work out $\Delta(N\Phi)$ first, then divide by $\Delta t$ |
| $$E = -\frac{d(N\Phi)}{dt}$$ | $E$ induced e.m.f. with Lenz sign, $N\Phi$ flux linkage | V | Direction (Lenz): the minus sign means the induced field opposes the change in $N\Phi$ |
| $$E = Blv$$ | $E$ induced e.m.f. across a straight wire, $B$ flux density, $l$ length in field, $v$ speed perpendicular to field and wire | $E$ in V, $l$ in m, $v$ in m s$^{-1}$ | Straight wire cutting a field; if $v$ is at angle $\theta$ to $B$, $E = Blv\sin\theta$; parallel to field gives $E = 0$ |
| $$E = Blv\sin\theta$$ | $\theta$ angle between wire velocity and field | V | General $Blv$ at an angle ($v$ perpendicular to wire length) |
| $$E_0 = BAN\omega$$ | Peak e.m.f. of a coil rotating at angular speed $\omega$ in a uniform field | V | Generator / rotating coil: $E = E_0\sin\omega t = BAN\omega\sin\omega t$ |
| $$1~\text{Wb} = 1~\text{T m}^2$$ | Weber in terms of tesla and area | Wb = T m$^2$ | Unit conversions and base-unit checks |

Constants you will need: the elementary charge $e = 1.60 \times 10^{-19}~\text{C}$ appears when induced e.m.f. drives a current that does work $eE$; $\pi = 3.14$ for area $A = \pi r^2$ of a circular coil.

**Exam fact:** $E = \frac{\Delta(N\Phi)}{\Delta t}$ and $\Phi = BA$ (with $\cos\theta$) are the foundation; $E = Blv$ and $E_0 = BAN\omega$ are **derived** from them ($\Phi = BA$, $A = Lv\Delta t$ or $A\cos\omega t$) and are not printed separately on the 9702 data sheet. You must be able to derive $Blv$ in two lines when asked. The minus sign ($E = -d(N\Phi)/dt$) carries the Lenz direction — for a magnitude the sign can be dropped, but for a direction you must invoke Lenz ("opposes the change in flux linkage") or the right-hand rule.

## 4. Methods (Question Types & Methods)

These are the ways Cambridge has actually asked about electromagnetic induction. Each method below is what a full-mark answer looks like.

### 1. Calculate magnetic flux or flux linkage

**Method:**
1. Decide: one loop → $\Phi = BA\cos\theta$; $N$ turns → flux linkage $= N\Phi = BAN\cos\theta$.
2. Find $A$ (for a circle $A = \pi r^2$; be careful — the question may give **diameter**).
3. Decide the angle: $\theta$ is between the **field and the normal** to the plane. If the angle given is to the **plane**, use $90° - \theta$ (or $\sin$).
4. Substitute with units: $B$ in T, $A$ in m$^2$, angle in degrees but $\cos$ handles either.
5. Quote flux in Wb; flux linkage in Wb turns.

**Traps:** using diameter as radius; using the angle to the plane as $\theta$ in $\cos\theta$ (the most common error — field in the plane means $\theta = 90°$ so $\Phi = 0$); forgetting the $N$ for a coil; confusing flux with flux linkage.

### 2. Apply Faraday's law for magnitude of the induced e.m.f.

**Method:**
1. Work out the **change** in flux linkage: $\Delta(N\Phi) = N(\Phi_{\text{final}} - \Phi_{\text{initial}})$. If only $B$ changes, $\Delta(N\Phi) = NA\Delta B$; if only area or angle changes, vary that term.
2. Divide by the **time** over which the change happens: $E = \frac{\Delta(N\Phi)}{\Delta t}$. Use the **average** rate if the graph is curved — the tangent gives the instantaneous rate.
3. For a rotating coil: $\Phi = BA\cos\omega t$, so $E = BAN\omega\sin\omega t$; the e.m.f. is sinusoidal.

**Traps:** using the flux (or final flux linkage) instead of the **change** in flux linkage; using the time for one event as $\Delta t$ when the question gives a $\Phi$–$t$ graph (you need the gradient); forgetting $N$; mixing up Wb and Wb turns.

### 3. Deduce the direction of the induced e.m.f. or current (Lenz)

**Method:**
1. Identify whether the flux linkage **increases** or **decreases** (movement direction, field change).
2. Lenz: the induced current creates a field that **opposes the change** — so if $N\Phi$ increases, the induced field opposes $B$; if it decreases, the induced field aids $B$.
3. From the induced field direction, deduce the current direction (right-hand grip rule for a coil: fingers = current, thumb = field).
4. For a straight wire, use Fleming's **right-hand** rule: thu**M**b = **M**otion, **F**irst finger = **F**ield, se**C**ond finger = induced **C**urrent (conventional).

**Traps:** saying "opposes the motion" instead of "opposes the change in flux linkage" (one mark lost); using the left hand (motor rule) for a generator question; reversing Lenz (the induced field aids when the flux grows — backwards).

### 4. Use $E = Blv$ for a straight wire or rail

**Method:**
1. Check the wire moves **perpendicular** to both its own length and the field — then $E = Blv$; if the motion makes an angle $\theta$ to the field, $E = Blv\sin\theta$.
2. If the wire completes a circuit (e.g. slides on rails of resistance $R$), the induced current is $I = \frac{E}{R} = \frac{Blv}{R}$ and the mechanical force to oppose Lenz is $F = BIL = \frac{B^2l^2v}{R}$ (work per unit time equals electrical power).
3. For a wire at rest in a changing field, use Faraday's law directly — $Blv$ does not apply (there is no $v$).

**Traps:** applying $Blv$ when the field is changing but the wire is stationary (use $E = N\Delta\Phi/\Delta t$ instead); using the wire's total length instead of the length **in the field**; forgetting $\sin\theta$ when the motion is not perpendicular to the field.

### 5. Work with $\Phi$–$t$ and $E$–$t$ graphs

**Method:**
1. On a flux-linkage vs time graph, the **gradient** is $\frac{d(N\Phi)}{dt}$ and the **negative** of the gradient is the e.m.f.: $E = -\frac{d(N\Phi)}{dt}$.
2. When $N\Phi$ is a straight line, the gradient is constant so $E$ is constant; when $N\Phi = BAN\cos\omega t$ (sinusoidal), the $\Phi$–$t$ graph is a cosine and the $E$–$t$ graph is a **sine** ($\pi/2$ out of phase, zero when $\Phi$ is maximal).
3. Area under an $E$–$t$ graph (or $I$–$t$ graph times $R$) equals the change in flux linkage.

**Traps:** drawing $E$–$t$ in phase with $\Phi$–$t$ (they are $90°$ out of phase — the derivative); saying the e.m.f. is zero when the flux is at its rate of change maximum (backwards — e.m.f. is maximum when $\left|\frac{d\Phi}{dt}\right|$ is maximum, which is when $\Phi = 0$ for a sinusoid).

### 6. Rotating coil / generator questions

**Method:**
1. Write flux linkage as $N\Phi = BAN\cos\omega t$ where $\omega = 2\pi f$.
2. Differentiate: $E = -\frac{d}{dt}(BAN\cos\omega t) = BAN\omega\sin\omega t$, so peak $E_0 = BAN\omega$ and $E_{\text{rms}} = \frac{E_0}{\sqrt{2}}$ (link to Chapter 29).
3. The coil is maximum flux when its plane is perpendicular to the field; maximum e.m.f. when its plane is **parallel** to the field (flux zero, rate of change maximum).

**Traps:** confusing flux and e.m.f. maxima (they are $90°$ apart); forgetting to convert $f$ to $\omega = 2\pi f$; using the r.m.s. formula $E_0/\sqrt{2}$ without noting it applies only to the sinusoidal generator output.

### 7. Eddy currents and electromagnetic damping (explain questions)

**Method:**
1. State that the changing flux through the metal induces circulating eddy currents in the metal itself (Faraday).
2. By Lenz, the eddy-current field **opposes the change / motion** that produces them, so they exert a braking/damping force or dissipate $I^2R$ heat.
3. Give the application: e.g. electromagnetic braking (train between magnets), damping in a pivoted coil, heating in an induction furnace — and the remedy: **laminating** the core (thin insulated sheets) breaks up the eddy-current loops and reduces loss.

**Traps:** describing eddy currents as "current in the wires of the coil" (they are in the **solid metal** itself); omitting Lenz's "opposes the change" — that is the physics mark; saying laminations "reduce resistance" (they break up the current paths, not the resistance of the core material).

### 8. Explain questions: complete Faraday–Lenz answer structure

**Method:**
1. State Faraday: "magnitude of induced e.m.f. is proportional to rate of change of magnetic flux linkage, $E = N\Delta\Phi/\Delta t$."
2. Apply to the situation: identify what changes ($B$, $A$, $\theta$, $N$) and why the change produces an e.m.f.
3. State Lenz for direction: "direction opposes the change in flux linkage" and deduce the current direction (right-hand rule or induced-field argument).
4. Close with energy: "work is done against the opposing force, becoming electrical energy" (the Lenz sign ensures conservation of energy).

**Traps:** defining Faraday without "rate of change" or without "flux linkage" (loses one mark per omission); defining Lenz without "opposes the **change**" (the word "change" is compulsory); omitting the minus sign or Lenz when asked to include it ($E = -d(N\Phi)/dt$ is the **Faraday–Lenz** law, not just Faraday).

## 5. Solved Examples

Real exam-style questions from the end of Chapter 28 and from past 9702 papers, with their mark allocations. The format for every example: Question / Method / Answer / What the examiner wants.

### Example 1: Magnetic flux through a loop — End-of-chapter Q1, [1] + [2] marks

**Question:** A circular loop of area $28~\text{cm}^2$ is placed in a uniform magnetic field of flux density $0.038~\text{T}$. (a) Calculate the magnetic flux through the loop when the field is perpendicular to the plane of the loop. [1] (b) The loop is rotated through $90°$ so that the field is now parallel to the plane. What is the change in magnetic flux? [2]

**Method:**
1. (a) Field perpendicular to the plane means $B$ is parallel to the normal, so $\theta = 0$, $\cos\theta = 1$: $\Phi = BA$.
2. Convert: $A = 28~\text{cm}^2 = 28 \times 10^{-4}~\text{m}^2 = 2.8 \times 10^{-3}~\text{m}^2$.
3. $\Phi = 0.038 \times 2.8 \times 10^{-3} = 1.064 \times 10^{-4}~\text{Wb}$.
4. (b) Field in the plane means $B$ is $90°$ to the normal, $\cos90° = 0$, so $\Phi = 0$. The change is $|\Delta\Phi| = 1.064 \times 10^{-4}~\text{Wb}$ (flux linkage goes from max to zero).

**Answer:** (a) $\Phi = 1.1 \times 10^{-4}~\text{Wb}$ (2 s.f.). (b) $\Phi = 0$ in the new position; $|\Delta\Phi| = 1.1 \times 10^{-4}~\text{Wb}$.

**What the examiner wants:** the area in m$^2$ and the argument $\theta = 0$ vs $90°$ (or $\Phi = BA$ vs $\Phi = 0$) explicitly; the change is the difference, not the new flux alone.

### Example 2: Flux linkage of a coil — End-of-chapter Q2, [2] marks

**Question:** A coil of $120$ turns and area $15~\text{cm}^2$ is placed in a uniform magnetic field of flux density $0.025~\text{T}$ with the field perpendicular to the plane of the coil. Calculate the magnetic flux linkage through the coil.

**Method:**
1. Flux through one turn: $\Phi = BA = 0.025 \times (15 \times 10^{-4}) = 0.025 \times 1.5 \times 10^{-3} = 3.75 \times 10^{-5}~\text{Wb}$.
2. Flux linkage: $N\Phi = 120 \times 3.75 \times 10^{-5} = 4.5 \times 10^{-3}~\text{Wb turns}$.

**Answer:** $N\Phi = 4.5 \times 10^{-3}~\text{Wb turns}$.

**What the examiner wants:** the "$N$" in the answer and the unit "Wb turns" (or "Wb" credited but "Wb turns" preferred when $N$ is explicit). A flux-only answer loses the factor of $120$.

### Example 3: Induced e.m.f. when a magnet is moved — End-of-chapter Q3, [3] marks

**Question:** The flux linkage through a coil of $200$ turns changes from $1.2 \times 10^{-3}~\text{Wb}$ to $0.4 \times 10^{-3}~\text{Wb}$ in $0.050~\text{s}$ as a magnet is pulled away. Calculate the magnitude of the average induced e.m.f.

**Method:**
1. $\Delta(N\Phi) = (0.4 - 1.2) \times 10^{-3} = -0.80 \times 10^{-3}~\text{Wb}$; magnitude $0.80 \times 10^{-3}$ (the "$N$" is already in the given $N\Phi$, so do not multiply by $200$ again).
2. Alternatively from the $N\Phi$ change: if the given values were $N\Phi$, $E = \frac{|\Delta(N\Phi)|}{\Delta t}$; if they were $\Phi$, use $E = \frac{N\Delta\Phi}{\Delta t}$. The coursebook gives this as a flux-linkage change, so $E = \frac{0.80 \times 10^{-3}}{0.050}$.
3. $E = \frac{0.80 \times 10^{-3}}{0.050} = 1.6 \times 10^{-2}~\text{V}$.

**Answer:** $E = 1.6 \times 10^{-2}~\text{V}$ ($16~\text{mV}$).

**What the examiner wants:** recognising whether the numbers given are $\Phi$ or $N\Phi$ (if $\Phi$, multiply by $N$; if $N\Phi$, do not). The trap variant gives $\Phi$ and $N$ separately — then $E = N\Delta\Phi/\Delta t$.

### Example 4: Sliding wire on rails — $E = Blv$ — End-of-chapter Q4, [3] + [1] marks

**Question:** A metal rod of length $0.15~\text{m}$ slides at $2.0~\text{m s}^{-1}$ on conducting rails through a uniform field $B = 0.30~\text{T}$ directed perpendicular to the rod and to its motion. The circuit resistance is $4.0~\Omega$. (a) Calculate the induced e.m.f. between the ends of the rod. [2] (b) Calculate the induced current. [1] (c) What is the direction of the current (use the right-hand rule)? [1]

**Method:**
1. (a) $E = Blv = 0.30 \times 0.15 \times 2.0 = 0.090~\text{V}$.
2. (b) $I = \frac{E}{R} = \frac{0.090}{4.0} = 2.25 \times 10^{-2}~\text{A}$.
3. (c) Right-hand rule: motion × field gives current direction across the rod; the return path through the rails completes the loop, so the current circulates (clockwise or anticlockwise depending on the $B$ direction given in the diagram).

**Answer:** (a) $0.090~\text{V}$. (b) $23~\text{mA}$ (2 s.f.). (c) direction given by the right-hand rule — thumb = motion, first finger = field, second finger = induced current along the rod.

**What the examiner wants:** $E = Blv$ must be stated (derived from Faraday if the mark scheme is strict); the length is the length **in the field** ($0.15~\text{m}$, not the rail separation unless they coincide); direction via the right hand with all three assignments.

### Example 5: $\Phi$–$t$ graph to $E$–$t$ graph — End-of-chapter Q5, [4] marks

**Question:** The graph shows magnetic flux linkage $N\Phi$ (Wb turns) against time $t$ (s) for a coil. The curve is sinusoidal, $N\Phi = 3.0 \times 10^{-3}\cos(100\pi t)$. Sketch the induced e.m.f. $E$ (V) against $t$, marking the peak value and period.

**Method:**
1. $E = -\frac{d(N\Phi)}{dt} = -\frac{d}{dt}[3.0 \times 10^{-3}\cos(100\pi t)] = 3.0 \times 10^{-3} \times 100\pi\sin(100\pi t)$.
2. Peak: $E_0 = 3.0 \times 10^{-3} \times 100\pi = 0.30\pi \approx 0.94~\text{V}$.
3. Period: $\omega = 100\pi$, so $T = \frac{2\pi}{\omega} = \frac{2\pi}{100\pi} = 0.020~\text{s}$.
4. The $E$–$t$ graph is a **sine** (shifted $90°$ from the cosine $N\Phi$–$t$ graph), zero when $N\Phi$ is maximum, maximum when $N\Phi$ is zero (maximum rate of change).

**Answer:** sinusoidal $E$–$t$ with period $0.020~\text{s}$, peak $\approx 0.94~\text{V}$, $90°$ ($\pi/2$) out of phase with the $N\Phi$–$t$ graph (zero at the $N\Phi$ maxima).

**What the examiner wants:** the derivative relation ($E = -d(N\Phi)/dt$) stated; the peak value from $N\Phi\,\omega$; the correct period $T = 2\pi/\omega$; and the $90°$ phase shift (the most examined point in this graph pair — they are **not** in phase).

### Example 6: Lenz direction — magnet approaching a coil — End-of-chapter Q6, [3] marks

**Question:** A bar magnet's N pole is pushed towards one end of a coil. Explain the direction of the induced current in the coil.

**Method:**
1. As the N pole approaches, the flux linkage into the coil **increases** in the direction of the magnet's field.
2. Lenz: the induced current's field **opposes the increase**, so it creates a field running **away** from the incoming N pole — the near end of the coil becomes an N pole too.
3. Repulsion is felt on the magnet (energy is required to push it — that work becomes the electrical energy). For the opposite pole, or removal, the induced field aids the diminishing flux (the near end becomes S, attracting the receding N).

**Answer:** near end becomes N; induced current circulates to put its field opposite the approaching field (Lenz: opposes the increase in flux linkage). The force on the magnet is repulsive, so work is done.

**What the examiner wants:** "opposes the **change in / increase in** flux linkage" (not just "opposes the motion"); the induced field direction; and the consequence that the near end is the same polarity as the approaching pole (N–N repulsion). "Opposes the magnet" without flux earns at most 1 mark.

### Example 7: Rotating coil — peak e.m.f. — End-of-chapter Q7, [2] + [2] marks

**Question:** A rectangular coil of $N = 100$ turns, area $A = 0.020~\text{m}^2$, rotates at $f = 50~\text{Hz}$ in a uniform field $B = 0.10~\text{T}$. (a) State the expression for the flux linkage as a function of time. [1] (b) Calculate the peak induced e.m.f. [2]

**Method:**
1. (a) $N\Phi = BAN\cos\omega t$, where $\omega = 2\pi f = 100\pi~\text{rad s}^{-1}$.
2. (b) Peak when $\sin\omega t = 1$: $E_0 = BAN\omega = 100 \times 0.10 \times 0.020 \times 100\pi = 20\pi \approx 62.8~\text{V}$. Or via $E_0 = 2\pi f\,BAN$.

**Answer:** (a) $N\Phi = 100 \times 0.10 \times 0.020\cos(100\pi t) = 0.20\cos(100\pi t)~\text{Wb turns}$. (b) $E_0 \approx 63~\text{V}$.

**What the examiner wants:** the $N$ in the flux-linkage expression; $\omega = 2\pi f$, not $\omega = f$; the peak at $\sin$, not the flux at $\cos$.

### Example 8: Search coil in a changing field — End-of-chapter Q8, [4] marks

**Question:** A search coil of $N = 500$ turns, area $4.0 \times 10^{-4}~\text{m}^2$, is placed in a field $B = 0.060~\text{T}$ perpendicular to the coil face. The field is then reduced uniformly to zero in $0.12~\text{s}$. Calculate (a) the change in flux linkage [2] and (b) the average induced e.m.f. [2].

**Method:**
1. (a) $\Phi = BA = 0.060 \times 4.0 \times 10^{-4} = 2.4 \times 10^{-5}~\text{Wb}$ per turn. Flux linkage $N\Phi = 500 \times 2.4 \times 10^{-5} = 1.2 \times 10^{-2}~\text{Wb turns}$. Going to zero, $|\Delta(N\Phi)| = 1.2 \times 10^{-2}$.
2. (b) $E = \frac{\Delta(N\Phi)}{\Delta t} = \frac{1.2 \times 10^{-2}}{0.12} = 0.10~\text{V}$.

**Answer:** (a) $1.2 \times 10^{-2}~\text{Wb turns}$. (b) $0.10~\text{V}$.

**What the examiner wants:** $N\Phi$ not just $\Phi$; the change (final $-$ initial, or magnitude) divided by time. A flux-only answer is a factor-of-$N$ error.

### Example 9: Eddy-current braking (explain) — End-of-chapter Q9, [3] marks

**Question:** Explain why a copper plate moving between the poles of a strong magnet is rapidly brought to rest (electromagnetic braking).

**Method:**
1. As the leading edge enters the field, the flux through the plate increases; at the trailing edge it decreases — both changes induce **circulating eddy currents** in the plate (Faraday).
2. By Lenz, the eddy-current field **opposes the change**, so the currents at both edges produce a force that **opposes the motion** of the plate.
3. The eddy currents dissipate $I^2R$ heat in the plate, converting kinetic energy to thermal energy until the plate stops.

**Answer:** changing flux through the moving plate → induced eddy currents → by Lenz they oppose the motion → braking force → kinetic energy → heat.

**What the examiner wants:** "eddy currents induced in the plate" + "Lenz: oppose the change / motion" + "energy dissipated as heat / kinetic → thermal" for three marks. Omitting Lenz loses the middle mark.

### Example 10: Induced e.m.f. at an angle — End-of-chapter Q10, [3] marks

**Question:** A coil of area $6.0 \times 10^{-3}~\text{m}^2$ with $N = 250$ turns is rotated so that its plane makes an angle of $30°$ to the magnetic field $B = 0.040~\text{T}$. Calculate the flux linkage through the coil when the normal to the coil makes $60°$ to the field, and state what angle gives maximum flux linkage.

**Method:**
1. Normal at $60°$ to $B$: $N\Phi = BAN\cos 60° = 250 \times 0.040 \times 6.0 \times 10^{-3} \times 0.5$.
2. $BAN = 250 \times 0.040 \times 6.0 \times 10^{-3} = 0.060~\text{Wb turns}$; times $0.5$ gives $0.030~\text{Wb turns}$.
3. Maximum when the normal is **parallel** to the field ($\theta = 0$, coil plane perpendicular to $B$), where $\cos\theta = 1$ and $N\Phi = BAN = 0.060~\text{Wb turns}$. Minimum (zero) when the field is in the plane ($\theta = 90°$).

**Answer:** $N\Phi = 3.0 \times 10^{-2}~\text{Wb turns}$ at $60°$; maximum at $\theta = 0°$ (normal parallel to $B$).

**What the examiner wants:** the "$\cos\theta$" with $\theta$ to the **normal** (the most examined angle error) and maximum at $0°$, minimum at $90°$.

## 6. Cheat Sheet

**The one-page summary — everything you must have in your head before the exam.**

**Flux & flux linkage**
- $\Phi = BA\cos\theta$ — $B$ in T, $A$ in m$^2$, $\theta$ between field and **normal** to area; unit: Wb = T m$^2$.
- $N\Phi = BAN\cos\theta$ — $N$ turns; flux linkage = $N \times$ flux; unit: Wb turns.
- Max flux linkage when normal is parallel to $B$ ($0°$); zero when field is in the plane ($90°$).

**Faraday + Lenz**
- Faraday magnitude: $E = \frac{\Delta(N\Phi)}{\Delta t}$ — **rate of change** of flux linkage, not flux itself.
- Faraday–Lenz with sign: $E = -\frac{d(N\Phi)}{dt}$ — minus = Lenz (opposes the **change** in $N\Phi$).
- $E$ is maximum when $\left|\frac{d(N\Phi)}{dt}\right|$ is maximum (not when $N\Phi$ is maximum — $90°$ apart for a sinusoid).

**Straight wire**
- $E = Blv$ — $l$ in field, $v$ perpendicular to both field and wire; if $v$ at $\theta$ to field, $E = Blv\sin\theta$; parallel gives $0$.
- If the wire slides on rails of resistance $R$, $I = \frac{Blv}{R}$ and opposing force $F = BIL = \frac{B^2l^2v}{R}$.

**Rotating coil / generator**
- $N\Phi = BAN\cos\omega t$, $E = BAN\omega\sin\omega t$, peak $E_0 = BAN\omega$, $\omega = 2\pi f$.

**Direction**
- Straight wire: Fleming's **right-hand** rule — thu**M**b = **M**otion, **F**irst finger = **F**ield, se**C**ond finger = induced **C**urrent (conventional).
- Coil: Lenz → induced field **opposes the change** in $N\Phi$ (not just "opposes the motion"); induced pole is same polarity as approaching pole (repulsion = work input).

**Applications**
- **Eddy currents:** circulating currents in solid metal from changing flux → Lenz braking → $I^2R$ heat; laminating breaks them up.
- **Generator:** coil rotating in field → alternating $E$ as above; e.m.f. max when coil plane is parallel to field.

## 7. Common Exam Mistakes

**1. Using flux where you need flux linkage.** The exam gives $N$ and asks for an e.m.f. — forgetting the $N$ costs the mark. Always decide: one turn → $\Phi$; $N$ turns → $N\Phi = BAN\cos\theta$.

**2. Forgetting "rate of change."** Faraday's law is "$E$ proportional to the **rate of change** of flux linkage" — writing "$E$ proportional to flux linkage" alone earns zero. The word "rate of change" is compulsory.

**3. Angle to the wrong reference.** In $\Phi = BA\cos\theta$, $\theta$ is to the **normal**, not to the plane. If the question says "field makes $30°$ to the plane," $\theta = 60°$ in the formula. Field in the plane gives $\Phi = 0$, not $BA$.

**4. Applying $Blv$ when the wire is stationary.** $Blv$ is for a wire **moving** through a uniform field. If the field changes but the wire is fixed, use $E = N\Delta\Phi/\Delta t$ instead. Mixing the two is the most common method error in this chapter.

**5. Lenz without "change."** "The induced e.m.f. opposes the magnetic field" or "opposes the motion" alone loses the mark. The opposed thing is the **change in flux linkage** — that phrase must appear. Without it the answer reads as if the flux itself is opposed.

**6. Using the left hand for a generator.** Fleming's left-hand rule is the **motor** rule (current → force). For **generation** (motion → current) you must use the **right hand**. Using the wrong hand gives the current the opposite direction and earns zero on a direction question.

**7. Confusing flux and rate-of-change maxima.** For a rotating coil or a sinusoidal $\Phi$–$t$ graph, $N\Phi$ is maximum when its rate of change is zero, and vice versa. So the e.m.f. ($-\frac{d(N\Phi)}{dt}$) peaks when the flux is zero. Swapping them is a standard 2-mark loss on graph questions — the two curves are $90°$ ($π/2$) out of phase.

**8. Unit and conversion slips.** Area given in cm$^2$ → must be m$^2$ ($\times 10^{-4}$); turns used as an extra factor when the given value is already $N\Phi$ (double-counting $N$); Wb turns confused with Wb (unit mark lost); $B = 2.0 \times 10^{-7}\frac{I}{x}$ (from Chapter 26) mixed into Faraday questions — they are separate chapters.

---

# Chapter 29: Alternating Currents - CAIE A Level Physics (9702) Study Notes

## 2. Definition Sheet

Every definition you must know word-perfect for the exam. Learn these exactly — the wording is what the mark schemes award.

> **Alternating current (a.c.):** a current whose direction reverses periodically. For the 9702 syllabus the variation is sinusoidal: $I = I_0 \sin \omega t$, where $I_0$ is the peak value and $\omega = 2\pi f$.
>
> Mark scheme: must convey periodic reversal of direction; for sinusoidal a.c. the sine-wave statement earns credit.

> **Peak value ($I_0$ or $V_0$):** the maximum instantaneous value of the alternating current or voltage in either direction (the amplitude of the sine wave). Read from the highest point on the $I$–$t$ or $V$–$t$ graph.
>
> Mark scheme: "maximum value" or "amplitude" (1 mark); must distinguish from r.m.s. or mean.

> **Period ($T$):** the time for one complete cycle of the alternating current or voltage, in seconds. $T = \frac{1}{f}$.
>
> **Frequency ($f$):** the number of complete cycles per unit time, in hertz (Hz). $f = \frac{1}{T}$ and $\omega = 2\pi f$.

> **Root-mean-square (r.m.s.) value:** the value of the **steady direct current (or voltage)** that would dissipate the **same mean power** in the same resistor as the alternating current (or voltage).
>
> Mark scheme: "steady d.c." / "direct current or voltage" (1 mark) + "same mean/average power (or heating effect) in the same resistor / resistive load" (1 mark). Saying "average current/voltage" without "steady d.c." loses the first mark. For sinusoidal a.c., $I_{\text{rms}} = \frac{I_0}{\sqrt{2}}$, $V_{\text{rms}} = \frac{V_0}{\sqrt{2}}$ — but the definition must be the heating equivalence, not just the formula.

> **Mean value of a.c.:** the average of the instantaneous current or voltage over one complete cycle. For a sinusoidal a.c. the mean over a full cycle is **zero** (positive half-cycle cancels the negative half-cycle).
>
> **Mean power:** the average rate at which energy is dissipated in a resistive load, $P = I_{\text{rms}}^2 R = \frac{V_{\text{rms}}^2}{R} = I_{\text{rms}} V_{\text{rms}}$. For a sine wave, peak power $= 2 \times$ mean power.

> **Transformer:** two coils (primary with $N_{\text{p}}$ turns, secondary with $N_{\text{s}}$ turns) wound on a soft iron core (laminated). There is no electrical connection between the coils; energy is transferred by the changing magnetic flux in the core via electromagnetic induction.
>
> **Turns-ratio equation:** $\frac{V_{\text{s}}}{V_{\text{p}}} = \frac{N_{\text{s}}}{N_{\text{p}}}$. For an ideal (100% efficient) transformer, $I_{\text{p}} V_{\text{p}} = I_{\text{s}} V_{\text{s}}$, so $\frac{I_{\text{s}}}{I_{\text{p}}} = \frac{N_{\text{p}}}{N_{\text{s}}}$.

> **Step-up transformer:** $N_{\text{s}} > N_{\text{p}}$, so $V_{\text{s}} > V_{\text{p}}$ and $I_{\text{s}} < I_{\text{p}}$ (for an ideal transformer).
>
> **Step-down transformer:** $N_{\text{s}} < N_{\text{p}}$, so $V_{\text{s}} < V_{\text{p}}$ and $I_{\text{s}} > I_{\text{p}}$.

> **Rectification:** the conversion of alternating current to direct current (current in one direction only).
>
> Mark scheme: "a.c. to d.c." / "current flows in one direction only" (1 mark).

> **Half-wave rectification:** rectification using a single diode: current flows for one half-cycle and is blocked for the other, so the output is zero for half the time.
>
> **Full-wave rectification:** rectification using a bridge of four diodes: both half-cycles are made to drive current the same way through the load, so the output is always $\ge 0$ and its frequency is twice the supply frequency.

> **Smoothing:** the reduction of the variation (ripple) in the rectified output by means of a capacitor connected **in parallel (across) the load**. The capacitor charges when the rectified voltage rises and discharges through the load when the rectified voltage falls, maintaining a steadier voltage.
>
> **Ripple:** the small residual variation in the smoothed output. Ripple decreases when $C$ or $R$ (hence $RC$) increases.

> **Cathode-ray oscilloscope (CRO):** displays voltage ($y$-axis) against time ($x$-axis). Y-gain / Y-sensitivity (in $\text{V cm}^{-1}$ or $\text{V div}^{-1}$) converts vertical deflection to voltage; time-base (in $\text{s cm}^{-1}$ or $\text{s div}^{-1}$) converts horizontal distance to time. The signal to the Y-input deflects the electron beam vertically; the time-base sweeps it horizontally.

> **Faraday's law of electromagnetic induction:** the induced e.m.f. is proportional to the rate of change of magnetic flux linkage: $E = N\frac{\Delta \Phi}{\Delta t}$ (magnitudes) or $E = -\frac{d(N\Phi)}{dt}$ with Lenz's sign.

## 3. Formula Sheet

**Quick reference:**

$$I = I_0 \sin \omega t, \qquad V = V_0 \sin \omega t, \qquad \omega = 2\pi f, \qquad f = \frac{1}{T}, \qquad I_{\text{rms}} = \frac{I_0}{\sqrt{2}}, \qquad V_{\text{rms}} = \frac{V_0}{\sqrt{2}}$$

$$P = I_{\text{rms}}^2 R = \frac{V_{\text{rms}}^2}{R} = I_{\text{rms}} V_{\text{rms}}, \qquad \frac{V_{\text{s}}}{V_{\text{p}}} = \frac{N_{\text{s}}}{N_{\text{p}}}, \qquad I_{\text{p}} V_{\text{p}} = I_{\text{s}} V_{\text{s}}\; (\text{ideal}), \qquad P_{\text{loss}} = I_{\text{rms}}^2 R_{\text{cable}}, \qquad \text{efficiency} = \frac{P_{\text{out}}}{P_{\text{in}}} \times 100\%$$

| Formula | Meaning of symbols | Units | When to use it |
|---|---|---|---|
| $$I = I_0 \sin \omega t$$ | $I$ instantaneous current, $I_0$ peak, $\omega$ angular frequency, $t$ time | $I$ in A, $\omega$ in $\text{rad s}^{-1}$, $t$ in s, $\omega t$ in rad | Instantaneous value; finding $I$ at a given $t$ or writing the equation from $I_0$ and $f$ |
| $$V = V_0 \sin \omega t$$ | $V$ instantaneous p.d., $V_0$ peak | $V$ in V | Instantaneous voltage; same use as above |
| $$\omega = 2\pi f = \frac{2\pi}{T}$$ | $\omega$ angular frequency, $f$ frequency, $T$ period | $\omega$ in $\text{rad s}^{-1}$, $f$ in Hz, $T$ in s | Converting between $\omega$, $f$ and $T$; argument of the sine is always $\omega t$ in radians |
| $$I_{\text{rms}} = \frac{I_0}{\sqrt{2}}$$ | $I_{\text{rms}}$ r.m.s. current, $I_0$ peak | A | Sinusoidal a.c. only; heating-equivalence value |
| $$V_{\text{rms}} = \frac{V_0}{\sqrt{2}}$$ | $V_{\text{rms}}$ r.m.s. voltage, $V_0$ peak | V | Sinusoidal a.c. only; mains $230~\text{V}$ is this value |
| $$P = I_{\text{rms}}^2 R = \frac{V_{\text{rms}}^2}{R} = I_{\text{rms}} V_{\text{rms}}$$ | $P$ mean power, $R$ resistance | W | Mean power in a resistive load — always use r.m.s. values |
| $$\frac{V_{\text{s}}}{V_{\text{p}}} = \frac{N_{\text{s}}}{N_{\text{p}}}$$ | $V_{\text{s}}, V_{\text{p}}$ secondary/primary voltages, $N_{\text{s}}, N_{\text{p}}$ turns | V, dimensionless | Any transformer; same ratio for r.m.s. or peak |
| $$I_{\text{p}} V_{\text{p}} = I_{\text{s}} V_{\text{s}}$$ | $I_{\text{p}}, I_{\text{s}}$ primary/secondary currents | A·V = W | Ideal (100% efficient) transformer only; power in = power out |
| $$P_{\text{loss}} = I_{\text{rms}}^2 R_{\text{cable}}$$ | $P_{\text{loss}}$ power lost as heat in cables, $R_{\text{cable}}$ cable resistance | W | Transmission losses; explains why high $V$ / low $I$ is used |
| $$\text{efficiency} = \frac{I_{\text{s}} V_{\text{s}}}{I_{\text{p}} V_{\text{p}}} \times 100\%$$ | Output power / input power | % | Real transformers; $P_{\text{out}} < P_{\text{in}}$ |
| $$V_0 = (\text{vertical amplitude}) \times (\text{Y-gain})$$ | From CRO trace | V | Reading peak voltage from the screen |
| $$T = (\text{horizontal length of one cycle}) \times (\text{time-base})$$ | From CRO trace | s | Reading period from the screen |
| $$E = N\frac{\Delta \Phi}{\Delta t}$$ | Faraday's law: $E$ induced e.m.f., $N\Phi$ flux linkage | V, Wb | Explaining the transformer; phase of flux vs e.m.f. |

Constants you will need: $\sqrt{2} = 1.414$; $\frac{1}{\sqrt{2}} = 0.707$; $2\pi = 6.28$.

**Exam fact:** $I_{\text{rms}} = I_0/\sqrt{2}$ and $V_{\text{rms}} = V_0/\sqrt{2}$ are the only r.m.s. formulas in the syllabus — they apply only to **sinusoidal** waveforms. For any other waveform you must use the definition: find the steady d.c. that gives the same mean power.

## 4. Methods (Question Types & Methods)

These are the ways Cambridge has actually asked about alternating currents. Each method below is what a full-mark answer looks like.

### 1. Write the equation of a sinusoidal a.c. or voltage from a graph or from $f$/$T$

**Method:**
1. Read $I_0$ or $V_0$ (peak) from the highest point on the graph (units A or V).
2. Find the period $T$ (time for one complete cycle) and $f = 1/T$.
3. Calculate $\omega = 2\pi f$.
4. Write $I = I_0 \sin \omega t$ or $V = V_0 \sin \omega t$ with $t$ in seconds and the argument in radians.

**Traps:** confusing peak-to-peak with peak (peak is half the peak-to-peak height); leaving the answer as $I = I_0 \sin(2\pi f t)$ instead of substituting the numerical $\omega$; using degrees instead of radians.

### 2. Find $f$, $T$ or $\omega$ from the equation $I = I_0 \sin \omega t$

**Method:**
1. Compare the given equation with $I = I_0 \sin \omega t$ to read off $I_0$ and $\omega$.
2. $f = \frac{\omega}{2\pi}$ and $T = \frac{1}{f} = \frac{2\pi}{\omega}$.

**Traps:** writing $f = \omega$ (forgetting $2\pi$); reading $120\pi t$ as $\omega = 120$ instead of $120\pi$.

### 3. Convert between peak and r.m.s. values

**Method:**
1. For a **sinusoidal** waveform: $I_{\text{rms}} = \frac{I_0}{\sqrt{2}}$ and $V_{\text{rms}} = \frac{V_0}{\sqrt{2}}$.
2. Invert: $I_0 = \sqrt{2}\,I_{\text{rms}}$ and $V_0 = \sqrt{2}\,V_{\text{rms}}$.
3. The mains $230~\text{V}$ (or $240~\text{V}$) quoted in questions is always $V_{\text{rms}}$ unless the question says "peak".

**Traps:** using $1/\sqrt{2}$ for a non-sinusoidal waveform (e.g. half-wave rectified — the mean power and hence the r.m.s. are different); multiplying by $\sqrt{2}$ when you should divide, and vice versa. Remember: **r.m.s. < peak**, so $I_{\text{rms}} = 0.707\,I_0$.

### 4. Calculate mean power in a resistive load

**Method:**
1. Identify $I_{\text{rms}}$ or $V_{\text{rms}}$ (convert from peak first if necessary).
2. Choose: $P = I_{\text{rms}}^2 R$ if you know current and $R$; $P = \frac{V_{\text{rms}}^2}{R}$ if you know voltage and $R$; $P = I_{\text{rms}} V_{\text{rms}}$ if you know both.
3. Quote $P$ in watts — this is the **mean** power.

**Traps:** using peak values in the power formula (gives double the correct mean power); using $P = I_0^2 R$ or $P = \frac{V_0^2}{R}$ without the $\frac{1}{2}$ — the factor-of-2 error is the single most common loss in this chapter.

### 5. Compare d.c. and a.c. heating (ratio questions)

**Method:**
1. D.C. power: $P_{\text{dc}} = I_{\text{dc}}^2 R$ (or $V_{\text{dc}}^2/R$).
2. A.C. mean power: $P_{\text{ac}} = I_{\text{rms}}^2 R = \frac{I_0^2}{2}R$.
3. Ratio: $\frac{P_{\text{dc}}}{P_{\text{ac}}} = \frac{I_{\text{dc}}^2}{I_{\text{rms}}^2}$ or $\frac{P_{\text{ac}}}{P_{\text{dc}}}$ as asked.

**Traps:** saying the heating effects are the same when $I_0 = I_{\text{dc}}$ (they are not — a.c. mean power is half); forgetting to square the currents in the ratio.

### 6. Read a CRO trace to find $V_0$, $V_{\text{rms}}$, $T$ and $f$

**Method:**
1. Vertical amplitude (cm or div) $\times$ Y-gain ($\text{V cm}^{-1}$ or $\text{V div}^{-1}$) $= V_0$ (peak). Then $V_{\text{rms}} = V_0/\sqrt{2}$.
2. Horizontal length of one complete cycle (cm or div) $\times$ time-base ($\text{s cm}^{-1}$ or $\text{s div}^{-1}$) $= T$. Then $f = 1/T$.
3. For current: $I_{\text{rms}} = V_{\text{rms}}/R$ if the trace is the voltage across a known resistor $R$.
4. Mean power: $P = V_{\text{rms}}^2/R$.

**Traps:** mixing up axes (time is $x$, voltage is $y$); reading peak-to-peak as peak; forgetting to convert ms to s ($1~\text{ms} = 10^{-3}~\text{s}$); using the wrong gain or time-base value after the question changes it.

### 7. Use the transformer turns-ratio equation

**Method:**
1. Write $\frac{V_{\text{s}}}{V_{\text{p}}} = \frac{N_{\text{s}}}{N_{\text{p}}}$ — keep secondary on top on both sides.
2. Substitute the two known values and solve for the third.
3. If power is asked and the transformer is ideal/100% efficient: $I_{\text{p}} V_{\text{p}} = I_{\text{s}} V_{\text{s}}$, so $I_{\text{s}} = I_{\text{p}}\frac{V_{\text{p}}}{V_{\text{s}}} = I_{\text{p}}\frac{N_{\text{p}}}{N_{\text{s}}}$.

**Traps:** swapping $N_{\text{p}}$ and $N_{\text{s}}$ (check: step-up means $N_{\text{s}} > N_{\text{p}}$); using peak for one side and r.m.s. for the other (use the same type on both sides — the ratio cancels the $\sqrt{2}$); assuming $I_{\text{p}} V_{\text{p}} = I_{\text{s}} V_{\text{s}}$ when the transformer is not ideal or losses are mentioned.

### 8. Solve power-transmission questions (high voltage, low loss)

**Method:**
1. Current in the cable: $I_{\text{rms}} = \frac{P}{V_{\text{rms}}}$ where $P$ is the **transmitted power** (not the loss).
2. Power lost as heat: $P_{\text{loss}} = I_{\text{rms}}^2 R_{\text{cable}}$.
3. Efficiency of transmission: $\frac{P - P_{\text{loss}}}{P} \times 100\%$.
4. To show the advantage: repeat for a higher $V$ and compare — $P_{\text{loss}} \propto 1/V^2$.

**Traps:** using $P_{\text{loss}} = \frac{V^2}{R}$ with the transmission voltage (that formula would give the power if the full transmission voltage were across the cable resistance — it is not; the cable voltage drop is $IR$, not $V_{\text{transmission}}$); confusing transmitted power with lost power (the question uses the same letter $P$ for both — label them); saying "high voltage reduces resistance" (resistance is unchanged; only current changes).

### 9. Identify transformer type and explain the design (flux, core, laminations)

**Method:**
1. State whether it is step-up ($N_{\text{s}} > N_{\text{p}}$) or step-down ($N_{\text{s}} < N_{\text{p}}$).
2. For "explain" questions: refer to Faraday's law — alternating current in primary $\rightarrow$ alternating magnetic flux in soft iron core $\rightarrow$ changing flux linkage in secondary $\rightarrow$ induced alternating e.m.f. in secondary.
3. Laminated / soft iron core: reduces eddy currents / hysteresis.

**Traps:** saying energy is transferred "through the wires" (it is via the magnetic field in the core); omitting "alternating/changing" flux (a steady flux induces no e.m.f.); saying laminations "reduce resistance" (they break up eddy-current paths in the core).

### 10. Draw and interpret rectification waveforms

**Method:**
1. Half-wave (1 diode): positive half-cycle passes unchanged, negative half-cycle is zero. Output frequency = supply frequency.
2. Full-wave bridge (4 diodes): both half-cycles are flipped positive; output is always $\ge 0$ with twice the supply frequency and no gaps.
3. Label axes: $V$ or $I$ on $y$, $t$ on $x$, with peak $V_0$ or $I_0$ marked.
4. For diode failure questions: one dead diode breaks the bridge — one half-cycle is lost and the output reverts to half-wave.

**Traps:** drawing full-wave as half-wave (leaving gaps); drawing the rectified frequency as the same as the supply for full-wave (it doubles); not labelling which terminal is positive on the load.

### 11. Smoothing — capacitor across the load: sketch, explain, and calculate

**Method:**
1. **Circuit:** capacitor $C$ is connected **in parallel (across) $R$**, after the rectifier.
2. **Sketch:** charging = steep rise following the rectified sine to $V_0$; discharging = gentle exponential decay between peaks; ripple amplitude = $V_0 - V_{\min}$.
3. **Effect of $R$ and $C$:** larger $C$ or larger $R$ $\rightarrow$ larger $RC$ $\rightarrow$ slower discharge $\rightarrow$ **less ripple**, higher mean voltage, higher mean power in $R$. Two equal capacitors in parallel $\rightarrow$ $C$ doubles $\rightarrow$ ripple halves.
4. **Calculations from the smoothed graph:** ripple $\Delta V \rightarrow \Delta Q = C\,\Delta V \rightarrow I_{\text{mean}} = \frac{\Delta Q}{\Delta t}$ (discharge time $\approx$ period minus brief charging time) $\rightarrow R \approx \frac{\langle V \rangle}{I_{\text{mean}}}$.

**Traps:** connecting the smoothing capacitor in series (it must be in parallel); saying "capacitor blocks a.c." (it charges and discharges — it does not block in this circuit); drawing the smoothed output as a flat line at $V_0$ (there is always some ripple; the voltage dips between peaks).

### 12. Flux and induced e.m.f. graphs for a transformer (Faraday phase question)

**Method:**
1. Primary current $I_{\text{p}} = I_0 \sin \omega t$.
2. Flux $\Phi$ in the core is **in phase** with $I_{\text{p}}$: $\Phi = \Phi_0 \sin \omega t$ — same sine shape, zero at the same times as the current.
3. Induced e.m.f. $E \propto -\frac{d\Phi}{dt}$: $E = -N\frac{d\Phi}{dt} = -N\omega\Phi_0 \cos \omega t$ — a **cosine** wave, $90°$ out of phase with the flux (zero when flux is at its peak, maximum when flux passes through zero). On the graph it is shifted by a quarter cycle.

**Traps:** drawing flux and e.m.f. in phase (they are not — e.m.f. is the derivative of flux); forgetting the minus sign / Lenz idea that the e.m.f. opposes the change (the phase shift is the way the mark scheme checks this).

### 13. Definitions and "explain" questions (frequent 2-mark questions)

**Method:**
1. **r.m.s.:** "the steady d.c. that dissipates the same mean power in the same resistor" — must say "steady d.c." and "same mean power / heating effect in the same (resistive) load".
2. **Why a.c. for power transmission:** "transformers can step voltage up, reducing current, so $I^2R$ losses in cables are reduced ($P_{\text{loss}} \propto 1/V^2$)".
3. **Rectification / smoothing:** "a.c. to d.c. (one direction only); diode conducts one way; capacitor in parallel charges and discharges to reduce ripple".
4. **Faraday's law:** "$E$ proportional to rate of change of (magnetic) flux linkage" — include "rate of change" and "flux linkage" ($N\Phi$), not just "flux".

**Traps:** defining r.m.s. as "$I_0/\sqrt{2}$" alone (1 mark at most — the words "same mean power" are required for full marks); saying "high voltage means low resistance" (wrong — low current); omitting "rate of change" in Faraday's law.

## 5. Solved Examples

Real exam-style questions from the end of Chapter 29 and from past 9702 papers, with their mark allocations. The format for every example: Question / Method / Answer / What the examiner wants.

### Example 1: Writing the equation of a sinusoidal current — End-of-chapter Q2, 6 marks

**Question:** The instantaneous value of an alternating current (in A) is $I = 2 \sin(50\pi t)$, where $t$ is in s. (a) What is the peak value of the current? [1] (b) What is the frequency? [2] (c) Sketch two cycles of $I$ against $t$, marking axes with suitable values. [2] (d) Calculate $I_{\text{rms}}$ and mark it on your graph. [1] (e) Find two values of $t$ at which $I = I_{\text{rms}}$. [3]

**Method:**
1. (a) Compare with $I = I_0 \sin \omega t$: $I_0 = 2.0~\text{A}$. [1]
2. (b) $\omega = 50\pi = 157~\text{rad s}^{-1}$; $f = \frac{\omega}{2\pi} = \frac{50\pi}{2\pi} = 25~\text{Hz}$; $T = \frac{1}{25} = 0.040~\text{s} = 40~\text{ms}$. [2]
3. (c) Sine wave from $0$ to $2.0~\text{A}$ peak, period $40~\text{ms}$, two cycles $0$–$80~\text{ms}$, crossing zero at $0$, $20$, $40$, $60$, $80~\text{ms}$. [2]
4. (d) $I_{\text{rms}} = \frac{2.0}{\sqrt{2}} = 1.41~\text{A}$ — horizontal dashed line at $1.41~\text{A}$ on the graph. [1]
5. (e) $I_{\text{rms}} = I_0 \sin \omega t \Rightarrow \sin(50\pi t) = \frac{1}{\sqrt{2}}$. So $50\pi t = \frac{\pi}{4}$ or $\frac{3\pi}{4}$ (first cycle). Hence $t = \frac{1}{200} = 5.0~\text{ms}$ or $t = \frac{3}{200} = 15~\text{ms}$ (and repeats every $40~\text{ms}$). [3]

**Answer:** (a) $2.0~\text{A}$; (b) $25~\text{Hz}$; (d) $1.41~\text{A}$; (e) $5.0~\text{ms}$ and $15~\text{ms}$ (then $45~\text{ms}$, $55~\text{ms}$, ...).

**What the examiner wants:** $\omega$ must be read as $50\pi$, not $50$; frequency needs the $2\pi$ step; the sketch must show two full cycles with correct $T$ and $I_0$ labelled; $I_{\text{rms}}$ marked as a horizontal line below the peak.

### Example 2: CRO measurement and power — End-of-chapter Q5, 7 marks

**Question:** An oscilloscope displays the voltage across a $200~\Omega$ resistor. Time-base $= 5.0~\text{ms div}^{-1}$, Y-gain $= 0.50~\text{V div}^{-1}$. The trace has peak height $3.0~\text{div}$ and one complete cycle occupies $4.0~\text{div}$. Determine (a) the period and frequency [2], (b) the peak and r.m.s. voltage [2], (c) the r.m.s. current [1], (d) the mean power [2].

**Method:**
1. (a) $T = 4.0 \times 5.0 = 20~\text{ms} = 0.020~\text{s}$; $f = \frac{1}{0.020} = 50~\text{Hz}$. [2]
2. (b) $V_0 = 3.0 \times 0.50 = 1.5~\text{V}$; $V_{\text{rms}} = \frac{1.5}{\sqrt{2}} = 1.06~\text{V}$. [2]
3. (c) $I_{\text{rms}} = \frac{V_{\text{rms}}}{R} = \frac{1.06}{200} = 5.3 \times 10^{-3}~\text{A}$. [1]
4. (d) $P = \frac{V_{\text{rms}}^2}{R} = \frac{1.06^2}{200} = 5.6 \times 10^{-3}~\text{W}$ (or $I_{\text{rms}}^2 R$ or $I_{\text{rms}} V_{\text{rms}}$). [2]

**Answer:** (a) $20~\text{ms}$, $50~\text{Hz}$; (b) $1.5~\text{V}$, $1.06~\text{V}$; (c) $5.3~\text{mA}$; (d) $5.6~\text{mW}$.

**What the examiner wants:** the CRO reading method (amplitude $\times$ Y-gain, length $\times$ time-base) with units; r.m.s. conversion; power must use r.m.s. values — using $V_0$ gives $11.3~\text{mW}$, which is double and earns at most 1 mark.

### Example 3: Transformer with a load — End-of-chapter Q3, 5 marks

**Question:** The $240~\text{V}$ r.m.s. mains is connected to the primary ($1200$ turns) of a transformer. The secondary r.m.s. output is $6.0~\text{V}$. (a) Calculate the number of secondary turns. [1] (b) A $6.0~\Omega$ resistor is connected across the secondary. Calculate (i) the mean power in the resistor [1], (ii) the peak current in the primary (assume ideal transformer). [3]

**Method:**
1. (a) $\frac{N_{\text{s}}}{N_{\text{p}}} = \frac{V_{\text{s}}}{V_{\text{p}}} = \frac{6.0}{240} = 0.025$; $N_{\text{s}} = 0.025 \times 1200 = 30$. [1]
2. (b)(i) $P = \frac{V_{\text{s,rms}}^2}{R} = \frac{6.0^2}{6.0} = 6.0~\text{W}$. [1]
3. (b)(ii) Secondary r.m.s. current: $I_{\text{s,rms}} = \frac{V_{\text{s,rms}}}{R} = \frac{6.0}{6.0} = 1.0~\text{A}$; so $I_{\text{s,peak}} = \sqrt{2} \times 1.0 = 1.41~\text{A}$. Ideal: $I_{\text{p}} V_{\text{p}} = I_{\text{s}} V_{\text{s}}$, so $I_{\text{p,peak}} = I_{\text{s,peak}} \times \frac{V_{\text{s,peak}}}{V_{\text{p,peak}}} = I_{\text{s,peak}} \times \frac{N_{\text{s}}}{N_{\text{p}}} = 1.41 \times 0.025 = 0.035~\text{A}$ (equivalently $I_{\text{p,rms}} = 0.025~\text{A}$, peak $= 0.035~\text{A}$). [3]

**Answer:** (a) $30$ turns; (b)(i) $6.0~\text{W}$; (b)(ii) $35~\text{mA}$ peak in the primary.

**What the examiner wants:** the turns ratio in the correct orientation; for (b)(ii) the chain r.m.s. $\rightarrow$ peak must be explicit — candidates who give $I_{\text{p,rms}} = 25~\text{mA}$ without converting to peak lose the last mark.

### Example 4: Flux and induced e.m.f. graphs — End-of-chapter Q4, 3 marks

**Question:** The graph shows the sinusoidal current in the primary of a transformer (secondary open-circuit). On the same axes sketch (i) the magnetic flux in the core (label A) [1], (ii) the induced e.m.f. in the primary (label B) [1]. (b) How are the two graphs related? [1]

**Method:**
1. (i) Flux $\Phi \propto I_{\text{p}}$: same sine wave as the current, in phase — zero at the same times, peak at the same times. Label A. [1]
2. (ii) Induced e.m.f. $E \propto -\frac{d\Phi}{dt}$: cosine wave, $90°$ shifted — zero when flux is at its maximum, maximum when flux passes through zero. Label B. [1]
3. (b) The e.m.f. is proportional to the rate of change of flux linkage (Faraday's law) and opposes the change (Lenz's law); it is $90°$ / a quarter cycle out of phase with the flux. [1]

**Answer:** A = sine (in phase with current); B = cosine (quarter-cycle shift, zero at flux peaks).

**What the examiner wants:** the phase relationship — flux follows current, e.m.f. is the derivative (cosine). A sketch with both curves in phase earns zero for (ii).

### Example 5: r.m.s. ratio and advantage of a.c. — End-of-chapter Q6, 6 marks

**Question:** (a) State $I_{\text{rms}}$ in terms of $I_0$ for a sine wave. [1] (b) A resistor carries $2.0~\text{A}$ d.c. and, separately, a sinusoidal a.c. with peak $2.0~\text{A}$. (i) Explain why the heating effects differ and which is greater. [2] (ii) Calculate $\frac{P_{\text{dc}}}{P_{\text{ac}}}$. [2] (c) State one advantage of a.c. in the home. [1]

**Method:**
1. (a) $I_{\text{rms}} = \frac{I_0}{\sqrt{2}}$. [1]
2. (b)(i) Heating $\propto I^2$, but a.c. spends part of the cycle below its peak and reverses direction; its mean squared value is half the peak squared, so mean power $\propto I_{\text{rms}}^2 = I_0^2/2$ is less than d.c. power $\propto I_{\text{dc}}^2$ when $I_0 = I_{\text{dc}}$. D.C. heating is greater. [2]
3. (b)(ii) $P_{\text{dc}} = I_{\text{dc}}^2 R = 4.0\,R$; $P_{\text{ac}} = I_{\text{rms}}^2 R = \frac{I_0^2}{2}R = 2.0\,R$; ratio $\frac{P_{\text{dc}}}{P_{\text{ac}}} = 2$. [2]
4. (c) A.c. voltage can be transformed to high voltage for efficient transmission (low $I^2R$ loss), or a.c. easily produces rotating magnetic fields for motors — any one valid advantage. [1]

**Answer:** (a) $I_0/\sqrt{2}$; (b)(ii) ratio $= 2$ (d.c. twice the mean a.c. power); (c) can be transformed / lower transmission losses.

**What the examiner wants:** the $\sqrt{2}$ statement alone for (a); for (b)(i) the link "power $\propto I^2$" and "mean power uses $I_{\text{rms}}$" — saying "a.c. averages to zero so no heating" is a zero-mark error.

### Example 6: Half-wave rectification with a diode — End-of-chapter Q7, 13 marks

**Question:** A $6.0~\text{V}$ r.m.s., $50~\text{Hz}$ sinusoidal supply is connected via a diode to a $400~\Omega$ resistor. (a) Sketch the supply voltage (dotted) and the voltage across $R$ (solid) on the same axes with scales. [4] (b) An uncharged capacitor $C$ is connected across $R$. It charges fully in the first quarter-cycle (diode drop $= 0$). For the next three-quarters of the first cycle, the diode stops conducting and the voltage across $R$ falls to half the peak value; the mean voltage during this discharge is $5.7~\text{V}$. For these three-quarters, calculate (i) the time taken [1], (ii) the mean current in $R$ [2], (iii) the charge through $R$ [2], (iv) the capacitance of $C$ [2]. (c) Explain why the diode stops conducting. [2]

**Method:**
1. (a) Peak: $V_0 = \sqrt{2} \times 6.0 = 8.5~\text{V}$; period $T = \frac{1}{50} = 20~\text{ms}$. Dotted: full sine $\pm 8.5~\text{V}$ at $50~\text{Hz}$. Solid: half-wave — the positive half-sine ($0$ to $8.5~\text{V}$) is present, the negative half-cycle is $0$ (diode blocks). [4]
2. (b)(i) Three-quarters of a cycle: $\Delta t = \frac{3}{4}T = \frac{3}{4} \times 20 = 15~\text{ms} = 0.015~\text{s}$. [1]
3. (b)(ii) Mean current during discharge: $I = \frac{\langle V \rangle}{R} = \frac{5.7}{400} = 1.425 \times 10^{-2}~\text{A} = 14.3~\text{mA}$. [2]
4. (b)(iii) Charge: $Q = I\,\Delta t = 1.425 \times 10^{-2} \times 0.015 = 2.14 \times 10^{-4}~\text{C}$. [2]
5. (b)(iv) $C$ charged to $V_0 = 8.5~\text{V}$ and fell to $V = 4.25~\text{V}$ ($\frac{1}{2}V_0$), so $\Delta V = 4.25~\text{V}$. $C = \frac{\Delta Q}{\Delta V} = \frac{2.14 \times 10^{-4}}{4.25} = 5.0 \times 10^{-5}~\text{F} = 50~\mu\text{F}$. [2]
6. (c) While the capacitor discharges through $R$, its voltage exceeds the supply voltage for most of the cycle. The diode is then reverse-biased (cathode more positive than anode), so it blocks. [2]

**Answer:** (b)(i) $15~\text{ms}$; (b)(ii) $14~\text{mA}$; (b)(iii) $2.1 \times 10^{-4}~\text{C}$; (b)(iv) $50~\mu\text{F}$; (c) capacitor voltage $>$ supply voltage $\rightarrow$ diode reverse-biased.

**What the examiner wants:** the half-wave sketch with correct $V_0$ and $T$ and the zero half-cycles; the chain $\langle V \rangle \rightarrow I \rightarrow Q \rightarrow C$ with the correct $\Delta V$ (peak to half-peak, not peak to zero).

### Example 7: Smoothing and ripple — End-of-chapter Q8, 12 marks

**Question:** The rectified output from a transformer is across a $1000~\Omega$ resistor. Graph A shows the unsmoothed p.d. across $R$ (full-wave rectified); Graph B shows the smoothed p.d. when a capacitor is placed across $R$. (a) How is rectification achieved? Draw the circuit. [6] (b) Explain the action of the capacitor. [3] (c) Using Graph B between $t = 0.005$ and $0.015~\text{s}$, determine (i) the charging time [1], (ii) the mean p.d. across $R$ [1], (iii) the mean power in $R$ [2].

**Method:**
1. (a) Four diodes in a bridge: supply across one diagonal, $R$ across the other. When $X$ is positive, diodes B and C conduct; when $Y$ is positive, diodes A and D conduct — current through $R$ always flows the same way. Full-wave: both half-cycles contribute. [6]
2. (b) $C$ in parallel with $R$. When rectified $V$ rises, $C$ charges to near $V_0$ through the low-resistance diode path. When rectified $V$ falls, the diode blocks and $C$ discharges through $R$, holding the voltage up — ripple is the small drop between peaks. [3]
3. (c)(i) Charging time = brief steep rise near each peak ($\approx 1$–$2~\text{ms}$ on the graph). Discharge dominates the cycle. [1]
4. (c)(ii) Mean $V$ $\approx$ midline of the ripple (e.g. $0.8$–$0.9~\text{V}$ if $V_0 = 1.0~\text{V}$ — read from the graph's mid-ripple level). [1]
5. (c)(iii) $P = \frac{\langle V \rangle^2}{R}$ (or $\langle V \rangle^2/R$ with the mean $V$ from (ii); using the graph's mean $\approx 0.85~\text{V}$, $P \approx \frac{0.85^2}{1000} = 0.72~\text{mW}$). [2]

**Answer:** (a) Bridge of four diodes; (b) charges on peaks, discharges through $R$ between peaks — reduces ripple; (c)(i) $\approx 1$–$2~\text{ms}$; (c)(ii) $\approx 0.85~\text{V}$ (read from mid-ripple); (c)(iii) $\approx 0.7~\text{mW}$.

**What the examiner wants:** the bridge diagram with correct diode directions and load connections; the two-phase "charge on rise, discharge on fall" explanation with "diode blocks"; power must use the **mean** (smoothed) voltage, not the peak.

### Example 8: Transformer, rectification and smoothing combined — End-of-chapter Q9, 9 marks

**Question:** A transformer produces $12~\text{V}$ peak output from the $230~\text{V}$ r.m.s. mains. (a) Its primary has $2000$ turns — find $N_{\text{s}}$. [3] (b) The secondary output is half-wave rectified and connected to $R$ and $C$ in parallel. Sketch on the same axes (i) the secondary p.d. and (ii) the p.d. across $R$. [3] (c) A second equal capacitor is placed in parallel with $C$. What happens to the p.d. across $R$? Explain. [3]

**Method:**
1. (a) Mains r.m.s. $= 230~\text{V}$, so primary peak $= \sqrt{2} \times 230 = 325~\text{V}$. Secondary peak $= 12~\text{V}$. $\frac{N_{\text{s}}}{N_{\text{p}}} = \frac{V_{\text{s,peak}}}{V_{\text{p,peak}}} = \frac{12}{325} = 0.0369$. $N_{\text{s}} = 2000 \times 0.0369 = 74$ turns. (If using r.m.s. throughout: $V_{\text{s,rms}} = 12/\sqrt{2} = 8.49~\text{V}$, ratio $= 8.49/230 = 0.0369$, same result. Mixing peak with r.m.s. without converting is the trap — here we converted consistently.) [3]
2. (b)(i) Secondary: sine wave $\pm 12~\text{V}$ peak. (ii) Across $R$: half-wave rectified — positive half-sine $0$ to $12~\text{V}$, negative half-cycle $0$; if $C$ is present the gaps are partially filled with a decaying exponential between peaks (smoothed half-wave). [3]
3. (c) $C_{\text{total}} = 2C$, so $RC$ doubles. The capacitor discharges more slowly between peaks, so **ripple decreases**, **mean voltage increases**, and mean power in $R$ increases. [3]

**Answer:** (a) $\approx 74$ turns; (b) see sketches: secondary = full sine $\pm 12~\text{V}$, $V_R$ = half-wave / smoothed half-wave; (c) ripple decreases, mean $V$ rises.

**What the examiner wants:** consistent peak/r.m.s. handling — r.m.s. on one side and peak on the other must be converted first; the two sketches on the same time axis with the same $T$; the $C \rightarrow 2C$ $\rightarrow$ larger $RC$ $\rightarrow$ less ripple chain.

### Example 9: High-voltage transmission — End-of-chapter Q10, 12 marks

**Question:** A $400~\text{kV}$ r.m.s. line of resistance $4.0~\Omega$ carries $500~\text{MW}$. (a)(i) What is meant by r.m.s. voltage? [2] (a)(ii) What peak voltage must the insulators withstand? [2] (b)(i) Find the r.m.s. current in the line. [2] (b)(ii) Find the power loss. [2] (b)(iii) Why is high voltage an advantage? [2] (c) Describe the principle of a step-down transformer. [2]

**Method:**
1. (a)(i) The steady d.c. voltage that would dissipate the same mean power in the same resistor as the a.c. voltage. [2]
2. (a)(ii) $V_0 = \sqrt{2} \times 400 = 566~\text{kV}$. Insulators must withstand at least this (practically higher, with a safety margin). [2]
3. (b)(i) $I_{\text{rms}} = \frac{P}{V_{\text{rms}}} = \frac{500 \times 10^6}{400 \times 10^3} = 1250~\text{A}$. [2]
4. (b)(ii) $P_{\text{loss}} = I_{\text{rms}}^2 R = 1250^2 \times 4.0 = 6.25 \times 10^6~\text{W} = 6.3~\text{MW}$. [2]
5. (b)(iii) For the same transmitted power, higher $V$ means lower $I$ ($I = P/V$), so $P_{\text{loss}} = I^2 R \propto 1/V^2$ is smaller — less fuel, fewer power stations. [2]
6. (c) Primary current produces alternating magnetic flux in a soft iron (laminated) core; the changing flux linkage induces an alternating e.m.f. in the secondary; step-down has $N_{\text{s}} < N_{\text{p}}$, so $V_{\text{s}} < V_{\text{p}}$ and (ideally) $I_{\text{s}} > I_{\text{p}}$. [2]

**Answer:** (a)(ii) $566~\text{kV}$; (b)(i) $1.25 \times 10^3~\text{A}$; (b)(ii) $6.3~\text{MW}$; (b)(iii) lower $I$ $\rightarrow$ lower $I^2R$ loss.

**What the examiner wants:** the r.m.s. definition with "same mean power in the same resistor"; peak $= \sqrt{2} \times$ r.m.s.; $P_{\text{loss}} = I^2R$ with $I = P/V$ — not $V^2/R$ with the transmission voltage.

### Example 10: a.c. basics — mean, r.m.s. and power — Past-paper style, 7 marks

**Question:** (a) Explain why a sinusoidal alternating current gives a heating effect even though its mean value is zero. [2] (b) Define the r.m.s. value. [2] (c) An a.c. of peak $3.0~\text{A}$ flows through a $100~\Omega$ resistor. Calculate the mean power. [3]

**Method:**
1. (a) Power $\propto I^2$; $I^2$ is always positive (negative current still gives positive $I^2$), so energy is dissipated in both half-cycles even though the signed mean of $I$ is zero (positive half cancels negative half). [2]
2. (b) The steady d.c. that dissipates the same mean power in the same resistor. [2]
3. (c) $I_{\text{rms}} = \frac{3.0}{\sqrt{2}} = 2.12~\text{A}$; $P = I_{\text{rms}}^2 R = 2.12^2 \times 100 = 450~\text{W}$. (Equivalently $P = \frac{I_0^2}{2}R$.) [3]

**Answer:** (c) $450~\text{W}$; peak power $= 900~\text{W}$.

**What the examiner wants:** "power depends on $I^2$, which is always positive" — the key idea; r.m.s. definition with "same mean power"; power must be halved from the peak-power value.

### Example 11: Transformer ratios and efficiency — Past-paper style, 6 marks

**Question:** A step-up transformer has $N_{\text{p}} = 100$, $N_{\text{s}} = 500$, $V_{\text{p}} = 230~\text{V}$ r.m.s., primary current $1.0~\text{A}$ r.m.s. (a) Find $V_{\text{s}}$ (ideal). [2] (b) Find $I_{\text{s}}$ (ideal). [2] (c) In practice $V_{\text{s}} = 1100~\text{V}$ and $I_{\text{s}} = 0.19~\text{A}$. Find the efficiency. [2]

**Method:**
1. (a) $V_{\text{s}} = V_{\text{p}} \times \frac{N_{\text{s}}}{N_{\text{p}}} = 230 \times 5 = 1150~\text{V}$. [2]
2. (b) $I_{\text{s}} = I_{\text{p}} \times \frac{N_{\text{p}}}{N_{\text{s}}} = 1.0 \times \frac{1}{5} = 0.20~\text{A}$. [2]
3. (c) $P_{\text{in}} = 230 \times 1.0 = 230~\text{W}$; $P_{\text{out}} = 1100 \times 0.19 = 209~\text{W}$; efficiency $= \frac{209}{230} \times 100\% = 91\%$. [2]

**Answer:** (a) $1150~\text{V}$; (b) $0.20~\text{A}$; (c) $91\%$.

**What the examiner wants:** the two ratios used in the correct sense (voltage $\propto N$, current $\propto 1/N$); efficiency as $P_{\text{out}}/P_{\text{in}}$ with the actual measured values.

### Example 12: Bridge rectifier and smoothing graph — Past-paper style, 8 marks

**Question:** A bridge rectifier delivers full-wave rectified output to a $2700~\Omega$ resistor. The p.d. across $R$ is shown (unsmoothed): a series of positive half-sines with peak $8.0~\text{V}$ at $100~\text{Hz}$ (supply $50~\text{Hz}$). (a) Use the graph to find the mean power in $R$ without smoothing. [3] (b) A capacitor is connected across $R$ to increase the mean power. Show where it is connected. [1] (c) One diode fails open-circuit. Sketch the new p.d. across $R$. [2]

**Method:**
1. (a) For full-wave rectified, both half-cycles contribute. Approximate mean $V^2$ over a cycle: for a sine, mean $V^2 = \frac{V_0^2}{2}$ even after rectification (rectification only flips the sign, $V^2$ is unchanged). So $P = \frac{V_{\text{rms}}^2}{R} = \frac{(V_0/\sqrt{2})^2}{R} = \frac{V_0^2}{2R} = \frac{64}{5400} = 1.19 \times 10^{-2}~\text{W} = 11.9~\text{mW}$. (Graph-reading alternative: estimate area/mean $V^2$ — same result to within reading tolerance.) [3]
2. (b) $C$ is connected **in parallel (across) $R$**, directly across the load terminals after the bridge. [1]
3. (c) Bridge broken $\rightarrow$ full-wave lost $\rightarrow$ half-wave: alternate half-cycles become zero, frequency halves to $50~\text{Hz}$, peak still $8.0~\text{V}$. [2]

**Answer:** (a) $\approx 12~\text{mW}$; (b) $C$ across $R$; (c) half-wave — every other half-sine missing.

**What the examiner wants:** $P$ unchanged by rectification (because $V^2$ is even); capacitor position is across the load, not in series; diode failure reverts full-wave to half-wave.

### Example 13: Calculating $C$ from a smoothed ripple — Past-paper style, 6 marks

**Question:** A bridge rectifier with smoothing capacitor $C = 5.0~\mu\text{F}$ across $R$ gives the smoothed waveform of Fig. 6.2 (Question 3 in the rectification topical). Between two peaks the voltage drops by $\Delta V = 0.60~\text{V}$ in $\Delta t = 9.0~\text{ms}$ and the mean voltage is $5.7~\text{V}$. (a) Find the charge lost by the capacitor during one discharge. [2] (b) Find the mean current in $R$ during discharge. [2] (c) Estimate $R$. [2]

**Method:**
1. (a) $\Delta Q = C\,\Delta V = 5.0 \times 10^{-6} \times 0.60 = 3.0 \times 10^{-6}~\text{C}$. [2]
2. (b) $I = \frac{\Delta Q}{\Delta t} = \frac{3.0 \times 10^{-6}}{9.0 \times 10^{-3}} = 3.3 \times 10^{-4}~\text{A} = 0.33~\text{mA}$. [2]
3. (c) $R = \frac{\langle V \rangle}{I} = \frac{5.7}{3.3 \times 10^{-4}} = 1.7 \times 10^4~\Omega = 17~\text{k}\Omega$. [2]

**Answer:** (a) $3.0~\mu\text{C}$; (b) $0.33~\text{mA}$; (c) $17~\text{k}\Omega$.

**What the examiner wants:** $\Delta Q = C\Delta V$ with the ripple $\Delta V$, not the peak voltage; $I = \Delta Q/\Delta t$ with the discharge time (not the full period); $R = V/I$ with the mean voltage during discharge.

### Example 14: Ideal transformer for a low-voltage device — Past-paper style, 6 marks

**Question:** An ideal transformer with $5000$ primary turns converts $230~\text{V}$ r.m.s. mains to $9.0~\text{V}$ peak output. (a) Find $N_{\text{s}}$. [3] (b) The output is full-wave rectified and smoothed by $C$ across $R$. State the charging interval on the smoothed $V$–$t$ graph and sketch the effect of doubling $R$. [3]

**Method:**
1. (a) Convert consistently: either both to peak or both to r.m.s. Primary peak $= \sqrt{2} \times 230 = 325~\text{V}$; secondary peak $= 9.0~\text{V}$. $\frac{N_{\text{s}}}{N_{\text{p}}} = \frac{9.0}{325} = 0.0277$; $N_{\text{s}} = 139$ turns. (Equivalently secondary r.m.s. $= 9.0/\sqrt{2} = 6.36~\text{V}$; ratio $= 6.36/230 = 0.0277$ — same result.) [3]
2. (b) $C$ charges during the brief steep rise to each peak (when the rectified supply exceeds the capacitor voltage and the diodes conduct); it discharges during the long gentle decay between peaks. Doubling $R$ $\rightarrow$ $RC$ doubles $\rightarrow$ slower discharge $\rightarrow$ less ripple, higher mean voltage — sketch a flatter decay with a higher trough. [3]

**Answer:** (a) $\approx 140$ turns; (b) charging = narrow peak region; doubling $R$ $\rightarrow$ less ripple, higher mean $V$.

**What the examiner wants:** consistent peak/r.m.s. handling — mixing them without $\sqrt{2}$ is the main error; charging = short peak interval, not the whole cycle; larger $R$ $\rightarrow$ larger $RC$ $\rightarrow$ less ripple.

## 6. Cheat Sheet

**One-glance revision block.**

Sinusoidal a.c.: $I = I_0 \sin \omega t$, $V = V_0 \sin \omega t$, $\omega = 2\pi f = \frac{2\pi}{T}$, $f = \frac{1}{T}$.

r.m.s. (sine only): $I_{\text{rms}} = \frac{I_0}{\sqrt{2}} \approx 0.707\,I_0$, $V_{\text{rms}} = \frac{V_0}{\sqrt{2}}$, and $I_0 = \sqrt{2}\,I_{\text{rms}}$, $V_0 = \sqrt{2}\,V_{\text{rms}}$. Mean over a full cycle $= 0$.

Mean power (resistive load): $P = I_{\text{rms}}^2 R = \frac{V_{\text{rms}}^2}{R} = I_{\text{rms}} V_{\text{rms}}$. Peak power $= 2 \times$ mean power.

Transformer: $\frac{V_{\text{s}}}{V_{\text{p}}} = \frac{N_{\text{s}}}{N_{\text{p}}}$ (turns ratio, same for r.m.s. or peak). Ideal: $I_{\text{p}} V_{\text{p}} = I_{\text{s}} V_{\text{s}}$ so $\frac{I_{\text{s}}}{I_{\text{p}}} = \frac{N_{\text{p}}}{N_{\text{s}}}$ (current ratio inverse to voltage ratio). Step-up: $N_{\text{s}} > N_{\text{p}}$; step-down: $N_{\text{s}} < N_{\text{p}}$.

Transmission: $I = \frac{P}{V}$, $P_{\text{loss}} = I^2 R_{\text{cable}} \propto \frac{1}{V^2}$ — high $V$ $\rightarrow$ low $I$ $\rightarrow$ low loss. $R_{\text{cable}}$ unchanged.

Rectification: 1 diode = half-wave (one half-cycle zero, frequency $= f$); 4-diode bridge = full-wave (both half-cycles flipped positive, frequency $= 2f$). Bridge: X positive $\rightarrow$ B + C conduct; Y positive $\rightarrow$ A + D conduct; current through $R$ always the same way.

Smoothing: $C$ **across (in parallel with)** $R$. Charges on peaks (diodes conduct), discharges through $R$ between peaks (diodes block) — ripple. Larger $C$ or larger $R$ $\rightarrow$ larger $RC$ $\rightarrow$ slower discharge $\rightarrow$ **less ripple**, higher mean $V$ and higher mean power. Two equal $C$ in parallel $\rightarrow$ $C$ doubles $\rightarrow$ ripple halves.

CRO: $V_0 = (\text{vertical amplitude}) \times (\text{Y-gain})$; $T = (\text{cycle length}) \times (\text{time-base})$; $V_{\text{rms}} = V_0/\sqrt{2}$; $f = 1/T$.

Flux vs e.m.f.: flux $\Phi \propto I_{\text{p}}$ (sine, in phase); induced e.m.f. $E \propto -\frac{d\Phi}{dt}$ (cosine, $90°$ / quarter-cycle shifted — zero when flux peaks).

Rules that win marks:
- **Always use r.m.s. values in $P = I^2R$ / $V^2/R$** — peak values give double the mean power.
- **r.m.s. $<$ peak** — $I_{\text{rms}} = 0.707\,I_0$, not $1.414\,I_0$.
- **Mean a.c. over a full cycle $= 0$**, but mean $I^2$ and mean power are **not** zero.
- **$P_{\text{loss}} = I^2R$ with $I = P/V$** — never $V^2/R$ with the transmission voltage.
- **Capacitor across the load (parallel)**, not in series.
- **Full-wave ripple frequency $= 2f$**, half-wave $= f$.
- **Discharge time** is most of the cycle; charging time is brief near each peak.

Common traps in one line each:
- Using $I_0$ or $V_0$ in the power formula without halving.
- Saying "mean current is zero so no heating" — heating $\propto I^2$.
- Swapping $N_{\text{s}}$ and $N_{\text{p}}$ in the turns ratio.
- Assuming $I_{\text{p}} V_{\text{p}} = I_{\text{s}} V_{\text{s}}$ for a non-ideal / lossy transformer.
- Drawing flux and e.m.f. in phase (e.m.f. is $90°$ shifted).
- Connecting the smoothing capacitor in series or calling it a "block".
- Forgetting that $230~\text{V}$ mains is r.m.s. — peak is $325~\text{V}$.

## 7. Common Exam Mistakes

From examiner reports and the coursebook's own questions, these are the actual reasons candidates lose marks on this chapter:

1. **Factor-of-2 error in power calculations.** Using $P = I_0^2 R$ or $P = V_0^2/R$ instead of $P = I_{\text{rms}}^2 R = \frac{V_{\text{rms}}^2}{R}$ doubles the answer. The mark scheme expects r.m.s. values in every power calculation; peak values give peak power, which is $2 \times$ mean power for a sine wave.

2. **Applying $I_{\text{rms}} = I_0/\sqrt{2}$ to non-sinusoidal waveforms.** The $1/\sqrt{2}$ factor is derived for a sine wave only (mean of $\sin^2 = \frac{1}{2}$). For half-wave rectified, square-wave or any other shape the r.m.s. must be found from the heating definition, not from $1/\sqrt{2}$.

3. **Saying the mean alternating current is non-zero or that zero mean means zero heating.** The signed mean over a full cycle is zero (positive half cancels negative half), but $I^2$ is always positive, so mean $I^2$ and mean power are non-zero. Answers that say "average current is zero so no power" score zero.

4. **Swapping peak and r.m.s. in the transformer equation.** $\frac{V_{\text{s}}}{V_{\text{p}}} = \frac{N_{\text{s}}}{N_{\text{p}}}$ holds for r.m.s. on both sides or peak on both sides, but mixing r.m.s. on one side with peak on the other without a $\sqrt{2}$ conversion is wrong. Always convert both to the same type first.

5. **Inverting the turns ratio.** Writing $\frac{N_{\text{s}}}{N_{\text{p}}} = \frac{V_{\text{p}}}{V_{\text{s}}}$ or swapping $N_{\text{p}}$ and $N_{\text{s}}$ in the current ratio $\frac{I_{\text{s}}}{I_{\text{p}}} = \frac{N_{\text{p}}}{N_{\text{s}}}$ is a very common slip. Check: step-up $\Rightarrow N_{\text{s}} > N_{\text{p}}$ and $V_{\text{s}} > V_{\text{p}}$; current steps the opposite way.

6. **Using $P_{\text{loss}} = \frac{V^2}{R}$ with the transmission voltage.** The voltage across the cable is $IR$, not the transmission voltage $V_{\text{transmission}}$. The correct route is $I = \frac{P}{V_{\text{transmission}}}$ then $P_{\text{loss}} = I^2 R_{\text{cable}}$. The $V^2/R$ form with $V_{\text{transmission}}$ can be thousands of times too large.

7. **Saying high voltage reduces the cable resistance.** The resistance is a property of the cable and is unchanged. High voltage reduces the **current** ($I = P/V$) and therefore the $I^2R$ heating. "Reduces resistance" is a zero-mark statement.

8. **Smoothing capacitor in the wrong place.** The capacitor must be **in parallel (across) the load resistor**, after the rectifier. Drawing it in series, or between the supply and the bridge, blocks the signal and earns no marks. Similarly, saying the capacitor "blocks a.c." in this context is incorrect — it charges and discharges to hold the voltage up.

9. **Confusing half-wave and full-wave waveforms.** Half-wave: one half-cycle present, one half-cycle zero, frequency $= f$. Full-wave: both half-cycles flipped positive, no gaps, frequency $= 2f$. Candidates who draw full-wave with gaps or half-wave without gaps, or who give the same frequency for both, lose the waveform marks.

10. **Drawing flux and induced e.m.f. in phase.** The flux $\Phi$ is in phase with the primary current (sine), but the induced e.m.f. $E \propto -\frac{d\Phi}{dt}$ is a cosine — $90°$ / quarter-cycle out of phase, zero when flux is at its peak. Drawing both as sines in phase shows a misunderstanding of Faraday's law.

11. **Incomplete definition of r.m.s.** Writing "$I_{\text{rms}} = I_0/\sqrt{2}$" alone, or "the average current", without the heating equivalence ("the steady d.c. that dissipates the same mean power in the same resistor") earns at most 1 of the 2 marks. The definition must be words, not just the formula.

12. **Incomplete Faraday's law statement.** "E.m.f. is proportional to flux" is insufficient. The law is "e.m.f. is proportional to the **rate of change** of (magnetic) **flux linkage** ($N\Phi$)". Omitting "rate of change" or "flux linkage" loses the marks.

13. **Assuming an ideal transformer when losses are given.** If the question gives $P_{\text{in}}$ and $P_{\text{out}}$ separately, or gives an efficiency, or says "in practice", do not use $I_{\text{p}} V_{\text{p}} = I_{\text{s}} V_{\text{s}}$ — calculate efficiency as $P_{\text{out}}/P_{\text{in}}$. The ideal equality only applies when the question says "ideal" or "100% efficient".

14. **CRO reading errors.** Mixing up Y-gain with time-base, reading peak-to-peak as peak (peak is half the total vertical height of a full sine), and forgetting to convert $\text{ms}$ to $\text{s}$ before computing $f = 1/T$ all cost marks. Always label the axes on a sketch ($V$ on $y$, $t$ on $x$).


---

# Chapter 30: Quantum Physics - CAIE A Level Physics (9702) Study Notes

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

---

# Chapter 31: Nuclear Physics - CAIE A Level Physics (9702) Study Notes

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

---

# Chapter 32: Medical Imaging - CAIE A Level Physics (9702) Study Notes

## 2. Definition Sheet

- **Ionising radiation:** radiation with enough energy to remove electrons from atoms, damaging living tissue.
- **Intensity:** power per unit cross-sectional area normal to the beam; $I=P/A$, unit $\text{W m}^{-2}$.
- **Attenuation coefficient $\mu$:** constant in $I=I_0e^{-\mu x}$, measuring absorption per unit thickness for a given photon energy; unit $\text{m}^{-1}$.
- **Half-thickness:** thickness reducing X-ray intensity to half; $x_{1/2}=\ln 2/\mu$.
- **Bremsstrahlung:** continuous X-radiation from electrons decelerated by target nuclei.
- **Characteristic X-rays:** photons of discrete energy from electron transitions in target atoms.
- **Collimation:** restricting a beam to a narrow, approximately parallel set of rays.
- **Contrast medium:** high-$Z$ substance introduced to increase X-ray absorption in a region.
- **CT:** imaging technique combining X-ray projections from many directions to reconstruct slices.
- **Voxel:** small cubic volume element used in CT reconstruction.
- **Ultrasound:** longitudinal sound wave above $20~\text{kHz}$.
- **Piezo-electric effect:** voltage produced by stress on a crystal, or shape change produced by applied voltage.
- **Acoustic impedance:** $Z=\rho c$, unit $\text{kg m}^{-2}\text{s}^{-1}$.
- **Impedance matching:** using gel with $Z$ close to skin so most ultrasound enters the body.
- **A-scan:** echo display as voltage spikes against time, used for depth measurement.
- **B-scan:** echo display as bright dots, building a 2D cross-section.
- **Doppler shift:** frequency change of a wave reflected from a moving object.
- **Larmor frequency:** precession frequency of a nucleus in a field; $\omega_0=\gamma B_0$.
- **Gyromagnetic ratio:** $\gamma=\omega_0/B_0$, unit $\text{rad s}^{-1}\text{T}^{-1}$.
- **Nuclear magnetic resonance:** absorption of RF energy when its frequency matches the Larmor frequency.
- **Relaxation time:** characteristic time for excited nuclei to return to the lower state.
- **Non-invasive:** no instrument is inserted into the body and the skin is not broken.

## 3. Formula Sheet

| Equation | Meaning |
|---|---|
| $E_k=eV$ | Maximum electron energy after acceleration through $V$ |
| $E=hf=hc/\lambda$ | Photon energy |
| $E_{\max}=eV=hc/\lambda_{\min}$ | Maximum X-ray photon energy and minimum wavelength |
| $I=P/A$ | Intensity |
| $I=I_0e^{-\mu x}$ | X-ray attenuation |
| $x_{1/2}=\ln 2/\mu$ | Half-thickness |
| $v=f\lambda$ | Wave equation |
| $Z=\rho c$ | Acoustic impedance |
| $\frac{I_r}{I_0}=\left(\frac{Z_2-Z_1}{Z_2+Z_1}\right)^2$ | Reflected intensity fraction at normal incidence |
| $I=I_0e^{-\alpha x}$ | Ultrasound absorption |
| $d=c\Delta t/2$ | Depth from echo time |
| $\Delta f=2f_0v\cos\theta/c$ | Doppler shift |
| $\omega_0=\gamma B_0$ | Larmor angular frequency |
| $f_0=\gamma B_0/(2\pi)$ | Larmor frequency |

**Constants:** $e=1.60\times10^{-19}~\text{C}$; $h=6.63\times10^{-34}~\text{J s}$; $c=3.00\times10^8~\text{m s}^{-1}$; soft tissue sound speed $\approx1540~\text{m s}^{-1}$; bone $\approx4000~\text{m s}^{-1}$; $\gamma_{\text{proton}}\approx2.68\times10^8~\text{rad s}^{-1}\text{T}^{-1}$.

## 4. Methods (Question Types & Methods)

### 1. X-ray tube energy and minimum wavelength

Use $E=eV$ for electron energy. For minimum wavelength set $eV=hc/\lambda_{\min}$. Convert keV to J by multiplying by $10^3$ and $1.60\times10^{-19}$.

### 2. X-ray attenuation

Use $I=I_0e^{-\mu x}$. Convert $x$ to metres if $\mu$ is in $\text{m}^{-1}$. Calculate the exponent first. For a fraction, divide by $I_0$ before substituting.

### 3. Half-thickness

Use $x_{1/2}=\ln 2/\mu$. For a general ratio, $x=\ln(I_0/I)/\mu$.

### 4. Image quality explanations

Structure answers around **dose**, **sharpness** and **contrast**. State the physical action and its effect on the image: collimation narrows the beam, filtration removes soft X-rays, a small focal spot reduces penumbra, an anti-scatter grid removes scattered rays, and contrast media increase absorption.

### 5. CT reconstruction

Model the slice as voxels. Each projection gives a sum along a line. Several directions give independent equations; solve for the voxel values. One projection alone is insufficient.

### 6. Acoustic impedance and reflection

Use $Z=\rho c$. For reflection, subtract, add, divide, then square:

$$\frac{I_r}{I_0}=\left(\frac{Z_2-Z_1}{Z_2+Z_1}\right)^2$$

The powers of ten cancel if both impedances use the same units.

### 7. Echo depth or thickness

Use distance $=c\Delta t$, then halve it because the pulse travels there and back. Check $\mu\text{s}=10^{-6}~\text{s}$ and $\text{ms}=10^{-3}~\text{s}$.

### 8. Transducer thickness

The crystal is half a wavelength thick:

$$t=\frac{\lambda}{2}=\frac{c}{2f}$$

### 9. Doppler blood flow

Rearrange $v=c\Delta f/(2f_0\cos\theta)$. Use the speed of sound in tissue. If the beam is parallel to flow, $\cos\theta=1$.

### 10. MRI Larmor frequency

Use $\omega_0=\gamma B_0$ for rad/s and $f_0=\gamma B_0/(2\pi)$ for Hz. If one $(f_0,B_0)$ pair is given, find $\gamma=2\pi f_0/B_0$. Since $f_0\propto B_0$, scale directly for a new field.

## 5. Solved Examples

### Example 1: Electron energy and speed

An X-ray tube operates at $80~\text{kV}$. Calculate the maximum electron energy in eV and J, and estimate its speed.

$$E_k=eV=80~\text{keV}$$

$$E_k=80\times10^3\times1.60\times10^{-19}=1.28\times10^{-14}~\text{J}$$

$$\frac12mv^2=E_k \Rightarrow v=\sqrt{\frac{2(1.28\times10^{-14})}{9.11\times10^{-31}}}=1.68\times10^8~\text{m s}^{-1}$$

**Answer:** $80~\text{keV}$, $1.28\times10^{-14}~\text{J}$, $v\approx1.7\times10^8~\text{m s}^{-1}$. This exceeds $0.5c$, so the non-relativistic speed is an overestimate.

### Example 2: Minimum wavelength

Calculate $\lambda_{\min}$ for a tube at $120~\text{kV}$.

$$E_{\max}=1.60\times10^{-19}\times120\times10^3=1.92\times10^{-14}~\text{J}$$

$$\lambda_{\min}=\frac{hc}{E_{\max}}=\frac{6.63\times10^{-34}\times3.00\times10^8}{1.92\times10^{-14}}=1.04\times10^{-11}~\text{m}$$

**Answer:** $1.04\times10^{-11}~\text{m}\approx0.0104~\text{nm}$.

### Example 3: Intensity and attenuation

A beam transfers $400~\text{J}$ through $5.0~\text{cm}^2$ each second, then passes through $5.0~\text{cm}$ of tissue with $\mu=1.2~\text{cm}^{-1}$. Find the final intensity.

$$P=400~\text{W}, \quad A=5.0\times10^{-4}~\text{m}^2$$

$$I_0=\frac{400}{5.0\times10^{-4}}=8.0\times10^5~\text{W m}^{-2}$$

$$I=8.0\times10^5e^{-(1.2\times5.0)}=8.0\times10^5e^{-6.0}=1.98\times10^3~\text{W m}^{-2}$$

**Answer:** about $2.0\times10^3~\text{W m}^{-2}$.

### Example 4: Half-thickness of bone

For bone at $20~\text{keV}$, $\mu=600~\text{m}^{-1}$.

$$x_{1/2}=\frac{\ln2}{600}=\frac{0.693}{600}=1.16\times10^{-3}~\text{m}$$

**Answer:** $1.2~\text{mm}$.

### Example 5: Intensity through bone

A $20~\text{W m}^{-2}$ beam passes through $4.0~\text{mm}$ of bone with $\mu=600~\text{m}^{-1}$.

$$x=4.0\times10^{-3}~\text{m}, \quad \mu x=2.4$$

$$I=20e^{-2.4}=20(0.0907)=1.81~\text{W m}^{-2}$$

**Answer:** $1.8~\text{W m}^{-2}$, about $9\%$ of the original.

### Example 6: CT voxel reconstruction

A $2\times2$ array has row sums $11$ and $10$, column sums $7$ and $14$, and diagonal sum $13$. Find the voxel values.

Let the array be $\begin{pmatrix}a&b\\c&d\end{pmatrix}$.

$$a+b=11,\quad c+d=10,\quad a+c=7,\quad b+d=14,\quad a+d=13$$

From the first, third and fifth: $b=11-a$, $c=7-a$, $d=13-a$. Then

$$(7-a)+(13-a)=10 \Rightarrow 20-2a=10 \Rightarrow a=5$$

$$b=6,\quad c=2,\quad d=8$$

**Answer:** $\begin{pmatrix}5&6\\2&8\end{pmatrix}$.

**Check:** rows $11,10$; columns $7,14$; diagonal $13$. One projection alone is insufficient because many arrays give the same sum.

### Example 7: Acoustic impedance and muscle–bone reflection

Muscle: $\rho=1075~\text{kg m}^{-3}$, $c=1590~\text{m s}^{-1}$. Bone: $Z=6.40\times10^6~\text{kg m}^{-2}\text{s}^{-1}$.

$$Z_{\text{muscle}}=\rho c=1075\times1590=1.71\times10^6~\text{kg m}^{-2}\text{s}^{-1}$$

$$\frac{I_r}{I_0}=\left(\frac{6.40-1.71}{6.40+1.71}\right)^2=\left(\frac{4.69}{8.11}\right)^2=0.334$$

**Answer:** $Z=1.71\times10^6~\text{kg m}^{-2}\text{s}^{-1}$; $33\%$ of the intensity is reflected.

### Example 8: Water–fat reflection

Water: $Z=1.50\times10^6$; fat: $Z=1.34\times10^6~\text{kg m}^{-2}\text{s}^{-1}$.

$$\frac{I_r}{I_0}=\left(\frac{1.50-1.34}{1.50+1.34}\right)^2=\left(\frac{0.16}{2.84}\right)^2=3.2\times10^{-3}$$

**Answer:** $3.2\times10^{-3}$, or $0.32\%$. This small reflection is why soft-tissue boundaries are hard to image.

### Example 9: Bone thickness from an A-scan

Echoes from the front and back of a bone are separated by $12~\mu\text{s}$; $c=4000~\text{m s}^{-1}$.

$$s=c\Delta t=4000(12\times10^{-6})=4.8\times10^{-2}~\text{m}$$

$$d=\frac{s}{2}=2.4\times10^{-2}~\text{m}$$

**Answer:** $2.4~\text{cm}$.

### Example 10: Optimum transducer thickness

A quartz transducer is driven at $2.1~\text{MHz}$; $c=5700~\text{m s}^{-1}$.

$$\lambda=\frac{c}{f}=\frac{5700}{2.1\times10^6}=2.71\times10^{-3}~\text{m}$$

$$t=\frac{\lambda}{2}=1.36\times10^{-3}~\text{m}$$

**Answer:** $\lambda\approx2.7~\text{mm}$; thickness $\approx1.4~\text{mm}$.

### Example 11: Doppler blood flow

A $2.0~\text{MHz}$ probe detects a $600~\text{Hz}$ shift from blood moving along the beam; $c=1540~\text{m s}^{-1}$.

$$v=\frac{c\Delta f}{2f_0}=\frac{1540(600)}{2(2.0\times10^6)}=0.231~\text{m s}^{-1}$$

**Answer:** $0.23~\text{m s}^{-1}$. At $60^\circ$ the measured shift would be halved unless angle-corrected.

### Example 12: Larmor frequency

Protons have $\gamma=2.68\times10^8~\text{rad s}^{-1}\text{T}^{-1}$ in $B_0=1.5~\text{T}$.

$$\omega_0=\gamma B_0=2.68\times10^8(1.5)=4.02\times10^8~\text{rad s}^{-1}$$

$$f_0=\frac{\omega_0}{2\pi}=6.40\times10^7~\text{Hz}$$

**Answer:** $64~\text{MHz}$, the RF frequency needed for resonance.

## 6. Exam-Style Questions (Full Solutions)

### Question 1

**(a)** Explain how X-rays are produced in an X-ray tube. **[5]**

**(b)** A tube operates at $100~\text{kV}$ with current $20~\text{mA}$. Calculate the maximum photon energy and minimum wavelength. **[3]**

**(c)** Explain why the anode rotates and the tube is evacuated. **[2]**

**(a)** A filament is heated, causing thermionic emission. A high voltage accelerates electrons to the anode. They strike a tungsten target and are rapidly decelerated, producing Bremsstrahlung photons. Inner-shell ionisation followed by electron transitions produces characteristic X-ray peaks.

**(b)**

$$E_{\max}=eV=1.60\times10^{-19}(100\times10^3)=1.60\times10^{-14}~\text{J}$$

$$\lambda_{\min}=\frac{hc}{E_{\max}}=\frac{6.63\times10^{-34}(3.00\times10^8)}{1.60\times10^{-14}}=1.24\times10^{-11}~\text{m}$$

**Answer:** $1.6\times10^{-14}~\text{J}$ and $1.24\times10^{-11}~\text{m}$.

**(c)** The anode rotates so the heated spot moves out of the beam and cools, preventing melting. The tube is evacuated so electrons do not collide with gas molecules before reaching the anode.

### Question 2

**(a)** State what is meant by the attenuation coefficient. **[2]**

**(b)** A beam of intensity $4.0\times10^5~\text{W m}^{-2}$ passes through $5.0~\text{cm}$ of aluminium with $\mu=250~\text{m}^{-1}$. Calculate the transmitted intensity. **[3]**

**(c)** Explain why an aluminium filter is used before the beam reaches the patient. **[3]**

**(a)** $\mu$ is the constant in $I=I_0e^{-\mu x}$; it measures the fraction of intensity removed per unit thickness for X-rays of a given energy. Unit: $\text{m}^{-1}$.

**(b)**

$$x=0.050~\text{m}, \quad \mu x=12.5$$

$$I=4.0\times10^5e^{-12.5}=1.49~\text{W m}^{-2}$$

**Answer:** about $1.5~\text{W m}^{-2}$.

**(c)** Soft X-rays are strongly absorbed in the patient, adding dose without reaching the detector. Aluminium absorbs low-energy photons more than high-energy ones, so the beam becomes harder. This reduces skin dose while retaining most of the useful signal.

### Question 3

**(a)** Explain how a piezo-electric crystal produces ultrasound and detects echoes. **[4]**

**(b)** Explain why gel is used between transducer and skin. **[3]**

**(c)** Skin has $Z=1.71\times10^6$ and gel $Z=1.65\times10^6~\text{kg m}^{-2}\text{s}^{-1}$. Calculate the percentage of intensity reflected. **[3]**

**(a)** An alternating voltage makes the crystal alternately contract and expand at the driving frequency, so it vibrates and radiates longitudinal ultrasound. An echo applies a varying stress, producing a varying e.m.f. across the crystal (reverse piezo-electric effect), which is detected.

**(b)** Without gel, the air–skin boundary has a huge impedance mismatch, so about $99.95\%$ of the intensity is reflected. Gel has $Z$ close to skin, providing impedance matching so most ultrasound enters the body.

**(c)**

$$\frac{I_r}{I_0}=\left(\frac{1.71-1.65}{1.71+1.65}\right)^2=\left(\frac{0.06}{3.36}\right)^2=3.19\times10^{-4}$$

$$3.19\times10^{-4}\times100\%=0.032\%$$

**Answer:** about $0.03\%$.

### Question 4

**(a)** Describe the difference between an A-scan and a B-scan. **[4]**

**(b)** In an A-scan, two echoes are separated by $0.034~\text{ms}$; $c=1540~\text{m s}^{-1}$. Calculate the separation of the reflecting surfaces. **[3]**

**(c)** Explain why the second echo is usually smaller. **[2]**

**(a)** An A-scan shows echoes as voltage spikes against time along a line; spike height indicates reflection strength. A B-scan combines many A-scans as the transducer moves, showing echoes as bright dots; brightness indicates amplitude, building a 2D cross-section.

**(b)**

$$s=c\Delta t=1540(3.4\times10^{-5})=5.24\times10^{-2}~\text{m}$$

$$d=\frac{s}{2}=2.62\times10^{-2}~\text{m}$$

**Answer:** $2.6~\text{cm}$.

**(c)** At each boundary some energy is reflected and some transmitted, and absorption also removes energy. The second echo has travelled farther, so less energy returns.

### Question 5

**(a)** Explain the principle of CT and why it gives more information than a plain X-ray. **[5]**

**(b)** Explain why CT may be preferred for a head injury. **[2]**

**(c)** Give two reasons CT is not used for routine screening of healthy people. **[2]**

**(a)** The X-ray tube rotates around the patient and a fan beam passes through in many directions. Detectors measure transmitted intensity for each projection. A computer combines the projections to find attenuation in each voxel of a slice, then displays the slice or a 3D reconstruction. A plain X-ray is one projection, so structures overlap. CT separates them and distinguishes tissues of similar density.

**(b)** CT shows the position, shape and size of a haematoma or fracture in three dimensions, including structures hidden by overlap in a plain X-ray, helping plan treatment.

**(c)** CT uses ionising radiation and delivers a significant dose; it is expensive and uses scarce scanner time; it can produce incidental findings leading to unnecessary tests; there is no clinical indication.

### Question 6

**(a)** Explain what is meant by nuclear magnetic resonance. **[4]**

**(b)** Explain why gradient coils are needed. **[3]**

**(c)** Protons precess at $42.6~\text{MHz}$ in $1.0~\text{T}$. Calculate the frequency in $2.5~\text{T}$. **[3]**

**(a)** Protons have spin and behave as tiny magnets. In a strong field they precess at the Larmor frequency. An RF pulse of exactly this frequency is absorbed, flipping protons to a higher state: resonance. When the pulse stops, they relax and emit RF radiation, which is detected.

**(b)** In a uniform field all protons resonate at the same frequency, giving no position information. Gradient coils make the field vary with position, so the Larmor frequency varies. Selecting the RF frequency and varying gradients excites and locates a slice or volume.

**(c)** Since $f\propto B$:

$$f_2=42.6\left(\frac{2.5}{1.0}\right)=106.5~\text{MHz}$$

**Answer:** about $107~\text{MHz}$.

## 7. Cheat Sheet

**X-rays**

- Fast electrons are decelerated in an evacuated tube; $99\%$ heat, $1\%$ X-rays.
- Continuous spectrum = Bremsstrahlung; sharp peaks = characteristic.
- $E_{\max}=eV=hc/\lambda_{\min}$.
- Voltage controls hardness; current controls intensity.
- Filter removes soft X-rays; collimator narrows beam; anti-scatter grid improves contrast.

**Attenuation**

- $I=I_0e^{-\mu x}$; match units of $\mu$ and $x$.
- $x_{1/2}=\ln2/\mu$.
- Bone has larger $\mu$ than soft tissue, so it looks white on film.
- CT reconstructs voxel values from many projections.

**Ultrasound**

- Longitudinal, $f>20~\text{kHz}$, needs a medium.
- $v=f\lambda$; soft tissue $c\approx1540~\text{m s}^{-1}$.
- Piezo-electric crystal transmits and detects; thickness $=\lambda/2$.
- $Z=\rho c$; reflection fraction $=[(Z_2-Z_1)/(Z_2+Z_1)]^2$.
- Gel gives impedance matching; air reflects almost everything.
- A-scan: spikes vs time, $d=c\Delta t/2$.
- B-scan: bright dots, 2D cross-section.
- Doppler: $\Delta f=2f_0v\cos\theta/c$.

**MRI**

- Protons spin and act as tiny magnets.
- Strong $B_0$ aligns them; they precess at the Larmor frequency.
- $\omega_0=\gamma B_0$; $f_0=\gamma B_0/2\pi$.
- RF at $f_0$ causes resonance; relaxation emits RF.
- $T_1$ spin–lattice; $T_2$ spin–spin; tissues differ in relaxation time.
- Gradient coils encode position.
- No ionising radiation; metal implants are a contraindication.

## 8. Common Exam Mistakes

1. Confusing X-ray production (decelerating electrons) with $\gamma$-ray production (nuclear decay).
2. Saying all X-rays come from electron transitions; the continuous spectrum is Bremsstrahlung.
3. Forgetting to convert keV to J: multiply by $10^3$ and $1.60\times10^{-19}$.
4. Using $E=hf$ with $f$ in kHz or MHz without converting to Hz.
5. Mixing units in $e^{-\mu x}$: if $\mu$ is in $\text{cm}^{-1}$, $x$ must be in cm.
6. Confusing intensity with dose; dose also depends on exposure time and tissue.
7. Saying a filter increases intensity; it reduces intensity but hardens the beam and lowers dose.
8. Forgetting the ultrasound pulse travels to the boundary and back: use $d=c\Delta t/2$.
9. Squaring too early or not at all in the reflection formula.
10. Using the speed of sound in bone for a soft-tissue A-scan.
11. Saying ultrasound cannot travel through the body; it cannot travel through a vacuum.
12. Confusing acoustic impedance with electrical impedance; $Z=\rho c$.
13. Forgetting the coupling gel, so most ultrasound reflects at the skin.
14. Saying MRI uses radioactive tracers or X-rays; it uses RF waves and a strong magnetic field.
15. Mixing up $T_1$ (spin–lattice) and $T_2$ (spin–spin).
16. Saying gradient coils make the field stronger overall; they make it vary with position.
17. Giving a medical advantage without the physics, e.g. "MRI is safer" without "no ionising radiation".
18. Using rad/s when Hz is asked; divide $\omega_0$ by $2\pi$.
19. Assuming higher ultrasound frequency is always better; absorption reduces penetration.
20. Omitting radiation dose and justification in CT safety answers.
