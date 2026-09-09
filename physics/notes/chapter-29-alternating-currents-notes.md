# Chapter 29: Alternating Currents - CAIE A Level Physics (9702) Study Notes

Exam-focused revision notes for Cambridge International AS & A Level Physics 9702, covering Topic 20 (Alternating Currents) as taught in Chapter 29 of the coursebook. Everything here is what the exam can actually ask, nothing more. All definitions are worded to match mark schemes, and every question type below has appeared in real 9702 papers (mainly Paper 4 structured questions). Every theory section ends with worked examples, so you can see the formula being used the moment it is introduced.

## 1. Theory

### 1.1 Sinusoidal alternating current and voltage — the basic waveform

An **alternating current (a.c.)** is a current whose direction reverses periodically. For the mains and for every 9702 question, the variation is **sinusoidal**: the current (and the voltage that drives it) traces a sine wave. During one half-cycle the current is positive (flows one way); during the next half-cycle it is negative (flows the other way). The electrons in the wire therefore oscillate back and forth with simple harmonic motion.

The equation of a sinusoidal alternating current is:

$$I = I_0 \sin \omega t$$

- $I$ is the instantaneous current at time $t$, in amperes (A).
- $I_0$ is the **peak value** (amplitude) — the maximum current in either direction, in A. On the graph it is the highest point.
- $\omega$ is the **angular frequency**, in $\text{rad s}^{-1}$.
- $t$ is the time, in seconds (s).
- The argument $\omega t$ is in **radians**.

The same form holds for a sinusoidal alternating voltage produced by a coil rotating in a magnetic field (a generator):

$$V = V_0 \sin \omega t$$

- $V$ is the instantaneous p.d., in volts (V).
- $V_0$ is the **peak voltage**, in V.

The angular frequency, frequency and period are linked exactly as in SHM:

$$\omega = 2\pi f, \qquad f = \frac{1}{T}, \qquad \omega = \frac{2\pi}{T}$$

- $f$ is the frequency, in hertz (Hz) — number of complete cycles per second.
- $T$ is the period, in seconds (s) — time for one complete cycle.

For UK mains, $f = 50~\text{Hz}$ and $T = 20~\text{ms}$.

**Worked example:** An alternating current is represented by $I = 5.0 \sin(120\pi t)$, where $I$ is in A and $t$ in s. Determine $I_0$, $\omega$, $f$ and $T$.

1. Compare with $I = I_0 \sin \omega t$: $I_0 = 5.0~\text{A}$ and $\omega = 120\pi = 377~\text{rad s}^{-1}$.
2. Frequency: $f = \frac{\omega}{2\pi} = \frac{120\pi}{2\pi} = 60~\text{Hz}$.
3. Period: $T = \frac{1}{f} = \frac{1}{60} = 1.67 \times 10^{-2}~\text{s} = 16.7~\text{ms}$.

**Answer:** $I_0 = 5.0~\text{A}$; $\omega = 377~\text{rad s}^{-1}$; $f = 60~\text{Hz}$; $T = 16.7~\text{ms}$.

**Worked example:** The current in Fig. 29.2 has peak value $3.0~\text{A}$ and period $20~\text{ms}$. Write its equation.

1. $I_0 = 3.0~\text{A}$.
2. $T = 20~\text{ms} = 0.020~\text{s}$, so $f = \frac{1}{0.020} = 50~\text{Hz}$.
3. $\omega = 2\pi f = 2\pi \times 50 = 100\pi = 314~\text{rad s}^{-1}$.
4. Equation: $I = 3.0 \sin(100\pi t)$ with $I$ in A and $t$ in s.

**Answer:** $I = 3.0 \sin(100\pi t)$.

**Worked example:** An alternating voltage is $V = 300 \sin(100\pi t)$ with $V$ in V. Calculate $V$ at $t = 0.0020~\text{s}$.

1. Argument: $100\pi \times 0.0020 = 0.20\pi = 0.628~\text{rad}$.
2. $V = 300 \sin(0.628) = 300 \times 0.588 = 176~\text{V}$ (calculator in radian mode).

**Answer:** $V = 1.8 \times 10^2~\text{V}$ at $t = 2.0~\text{ms}$.

### 1.2 Peak, mean and r.m.s. values — what the exam means by each

| Quantity | Symbol | Meaning | Value for a sine wave |
|---|---|---|---|
| **Peak value** | $I_0$ or $V_0$ | Maximum instantaneous value (amplitude) | Read from the top of the graph |
| **Mean value** | $\langle I \rangle$ or $\langle V \rangle$ | Average over one complete cycle | **Zero** (positive half cancels negative half) |
| **Rectified mean** | $\langle \|I\| \rangle$ | Mean of the modulus (after rectification) | $\frac{2I_0}{\pi} \approx 0.637\,I_0$ (rarely asked) |
| **Root-mean-square** | $I_{\text{rms}}$ or $V_{\text{rms}}$ | Steady d.c. value that delivers the same mean power to a resistor | $\frac{I_0}{\sqrt{2}} \approx 0.707\,I_0$ |

The **mean value over a full cycle is zero** — this is why the heating effect is not zero even though the mean current is zero. Heating depends on $I^2$, which is always positive.

**Worked example:** The mains voltage quoted as $230~\text{V}$ is an r.m.s. value. Calculate its peak value.

1. $V_{\text{rms}} = \frac{V_0}{\sqrt{2}}$, so $V_0 = \sqrt{2} \times V_{\text{rms}}$.
2. $V_0 = 1.414 \times 230 = 325~\text{V}$.

**Answer:** $V_0 = 325~\text{V}$ (the insulation must withstand at least this; for $400~\text{kV}$ r.m.s. the peak is $566~\text{kV}$).

**Worked example:** A sinusoidal current has $I_0 = 2.5~\text{A}$. The same resistor is connected first to a steady d.c. of $2.5~\text{A}$, then to this a.c. Which delivers more heating power, and by what factor?

1. D.C. power: $P_{\text{dc}} = I_{\text{dc}}^2 R = (2.5)^2 R = 6.25\,R$.
2. A.C. mean power: $P_{\text{ac}} = I_{\text{rms}}^2 R = \left(\frac{I_0}{\sqrt{2}}\right)^2 R = \frac{I_0^2}{2}R = \frac{6.25}{2}R = 3.125\,R$.
3. Ratio $\frac{P_{\text{dc}}}{P_{\text{ac}}} = 2$.

**Answer:** The d.c. delivers twice the mean power; $\frac{P_{\text{dc}}}{P_{\text{ac}}} = 2$.

### 1.3 Root-mean-square — definition, derivation and why the factor is $\frac{1}{\sqrt{2}}$

**Definition (2-mark wording):** the root-mean-square value of an alternating current is the value of the **steady direct current** that would dissipate **the same mean power** in the same resistor as the alternating current. The same definition applies to voltage.

**Where $\frac{1}{\sqrt{2}}$ comes from:**

1. Instantaneous power in a resistor: $P = I^2 R$, so $P \propto I^2$.
2. $I^2$ is always positive. For $I = I_0 \sin \omega t$, the graph of $I^2 = I_0^2 \sin^2 \omega t$ oscillates between $0$ and $I_0^2$ at **twice** the frequency of $I$.
3. The **mean value** of $I^2$ over a cycle is half its peak: $\langle I^2 \rangle = \frac{1}{2}I_0^2$ (the $\sin^2$ graph is symmetrical about its midline).
4. Take the square **root** of the **mean** of the **square**: $I_{\text{rms}} = \sqrt{\langle I^2 \rangle} = \sqrt{\frac{I_0^2}{2}} = \frac{I_0}{\sqrt{2}}$.
5. Hence the name: **r**oot of the **m**ean of the **s**quare.

The same holds for voltage: $V_{\text{rms}} = \frac{V_0}{\sqrt{2}}$.

**Crucial restriction:** the factor $\frac{1}{\sqrt{2}}$ applies **only to sinusoidal** waveforms. For any other shape (square wave, triangular wave, half-wave rectified) the ratio is different and must be found from the heating equivalence directly.

**Worked example:** Show that the mean power from a sinusoidal a.c. is half the peak power.

1. Peak power (at the instant $I = I_0$): $P_0 = I_0^2 R$.
2. Mean power: $\langle P \rangle = \langle I^2 \rangle R = \frac{1}{2}I_0^2 R = \frac{1}{2}P_0$.
3. Equivalently, $\langle P \rangle = I_{\text{rms}}^2 R = \left(\frac{I_0}{\sqrt{2}}\right)^2 R = \frac{1}{2}I_0^2 R$.

**Answer:** $\langle P \rangle = \frac{1}{2}P_0$; the ratio $\frac{\langle P \rangle}{P_0} = 0.5$.

**Worked example:** The variation of current with time is sinusoidal with $I_0 = 9.9~\text{A}$ (given as $I = 9.9 \sin 380t$). Find $I_{\text{rms}}$ and the frequency.

1. $I_{\text{rms}} = \frac{9.9}{\sqrt{2}} = 7.0~\text{A}$.
2. $\omega = 380~\text{rad s}^{-1}$, so $f = \frac{380}{2\pi} = 60.5~\text{Hz}$.

**Answer:** $I_{\text{rms}} = 7.0~\text{A}$; $f \approx 60~\text{Hz}$.

### 1.4 Power in a.c. circuits — the three forms and when to use each

For a **resistive** load the current and voltage are **in phase** (both $\propto \sin \omega t$), so the standard d.c. power formulas apply provided you use **r.m.s. values**:

$$P = I_{\text{rms}}^2 R = \frac{V_{\text{rms}}^2}{R} = I_{\text{rms}} V_{\text{rms}}$$

- $P$ is the **mean (average) power**, in watts (W).
- $I_{\text{rms}}$ in A, $V_{\text{rms}}$ in V, $R$ in $\Omega$.
- For sinusoidal a.c., peak power is **twice** the mean power: $P_0 = I_0 V_0 / 2 \times 2$? More precisely $P_0 = I_0^2 R = 2\,I_{\text{rms}}^2 R = 2\langle P \rangle$.

If you mistakenly use **peak values** in $P = I^2 R$ or $P = \frac{V^2}{R}$ you get **double** the correct mean power. The factor-of-2 error is one of the most common losses in this chapter.

For an ideal diode or any non-resistive component the simple $V = IR$ link does not hold instant by instant; power must be found from the heating equivalence.

**Worked example:** A sinusoidal p.d. of peak value $25~\text{V}$ is connected across a $20~\Omega$ resistor. Calculate the mean power.

1. $V_{\text{rms}} = \frac{25}{\sqrt{2}} = 17.7~\text{V}$.
2. $P = \frac{V_{\text{rms}}^2}{R} = \frac{17.7^2}{20} = 15.6~\text{W}$.

**Answer:** $P = 16~\text{W}$ (2 s.f.). Using $V_0$ would give $31.3~\text{W}$ — double the correct answer.

**Worked example:** The mains r.m.s. voltage $230~\text{V}$ is connected across a $1.0~\text{k}\Omega$ resistor. Find (a) $I_{\text{rms}}$, (b) mean power, (c) peak power.

1. (a) $I_{\text{rms}} = \frac{V_{\text{rms}}}{R} = \frac{230}{1000} = 0.23~\text{A}$.
2. (b) $P = I_{\text{rms}} V_{\text{rms}} = 0.23 \times 230 = 53~\text{W}$ (or $\frac{V_{\text{rms}}^2}{R}$).
3. (c) $P_0 = 2P = 106~\text{W}$; equivalently $I_0 = \sqrt{2} \times 0.23 = 0.33~\text{A}$, $P_0 = I_0^2 R = 106~\text{W}$.

**Answer:** (a) $0.23~\text{A}$; (b) $53~\text{W}$; (c) $106~\text{W}$.

**Worked example:** The mean power in a resistor must not exceed $400~\text{W}$. The current is $I = 9.9 \sin 380t$ (so $I_{\text{rms}} = 7.0~\text{A}$ as above). Find the minimum resistance.

1. $P = I_{\text{rms}}^2 R$, so $R = \frac{P}{I_{\text{rms}}^2}$.
2. For the limiting case $P = 400~\text{W}$: $R = \frac{400}{7.0^2} = \frac{400}{49} = 8.2~\Omega$.
3. Any smaller $R$ would dissipate more power for the same current; so $R_{\min} = 8.2~\Omega$.

**Answer:** $R_{\min} = 8.2~\Omega$.

### 1.5 Measuring a.c. with a cathode-ray oscilloscope (CRO)

The CRO displays **voltage on the $y$-axis** and **time on the $x$-axis**.

| Control | What it does | Units | How to use it |
|---|---|---|---|
| **Y-gain / Y-sensitivity** | Sets how many volts each vertical centimetre (or division) represents | $\text{V cm}^{-1}$ or $\text{V div}^{-1}$ | Peak voltage: $V_0 = (\text{vertical amplitude in cm}) \times (\text{Y-gain})$ |
| **Time-base** | Sets how much time each horizontal cm (or div) represents; controls sweep speed | $\text{s cm}^{-1}$, $\text{ms cm}^{-1}$ or $\text{ms div}^{-1}$ | Period: $T = (\text{horizontal length of one cycle in cm}) \times (\text{time-base})$ |
| **X-shift / Y-shift** | Moves the whole trace sideways / up and down | — | Centres the trace; does not affect measurements |

From one trace you can find **everything**: amplitude $\rightarrow V_0 \rightarrow V_{\text{rms}} = V_0/\sqrt{2}$; period $\rightarrow f = 1/T \rightarrow \omega = 2\pi f$.

The applied signal goes to the **Y-input**: it deflects the electron beam vertically via plates $Y_1$, $Y_2$. The **time-base** generates a sawtooth voltage on plates $X_1$, $X_2$ that sweeps the spot steadily left-to-right and then flies back quickly. The result is a stationary trace of $V$ against $t$.

**Worked example:** A CRO trace has vertical amplitude $2.0~\text{cm}$ and one complete cycle occupies $4.0~\text{cm}$ horizontally. Y-gain $= 2.0~\text{V cm}^{-1}$, time-base $= 5.0~\text{ms cm}^{-1}$. Find $V_0$, $V_{\text{rms}}$, $T$ and $f$.

1. $V_0 = 2.0 \times 2.0 = 4.0~\text{V}$.
2. $V_{\text{rms}} = \frac{4.0}{\sqrt{2}} = 2.8~\text{V}$.
3. $T = 4.0 \times 5.0 = 20~\text{ms} = 0.020~\text{s}$.
4. $f = \frac{1}{0.020} = 50~\text{Hz}$.

**Answer:** $V_0 = 4.0~\text{V}$; $V_{\text{rms}} = 2.8~\text{V}$; $T = 20~\text{ms}$; $f = 50~\text{Hz}$.

**Worked example:** Y-sensitivity $5.0~\text{V cm}^{-1}$, time-base $10~\text{ms cm}^{-1}$. The trace in Fig. 29.7 shows amplitude $2~\text{cm}$ and one cycle $= 4~\text{cm}$. What are the amplitude, period and frequency?

1. Amplitude (peak): $2 \times 5.0 = 10~\text{V}$.
2. Period: $4 \times 10 = 40~\text{ms} = 0.040~\text{s}$.
3. Frequency: $f = \frac{1}{0.040} = 25~\text{Hz}$.

**Answer:** $V_0 = 10~\text{V}$; $T = 40~\text{ms}$; $f = 25~\text{Hz}$.

**Worked example (end-of-chapter Q5 style):** Time-base $5.0~\text{ms div}^{-1}$, Y-gain $0.50~\text{V div}^{-1}$. The trace across a $200~\Omega$ resistor has peak height $3.0~\text{div}$ and one cycle $= 4.0~\text{div}$.

1. $V_0 = 3.0 \times 0.50 = 1.5~\text{V}$.
2. $V_{\text{rms}} = \frac{1.5}{\sqrt{2}} = 1.06~\text{V}$.
3. $T = 4.0 \times 5.0 = 20~\text{ms}$; $f = 50~\text{Hz}$.
4. $I_{\text{rms}} = \frac{V_{\text{rms}}}{R} = \frac{1.06}{200} = 5.3 \times 10^{-3}~\text{A} = 5.3~\text{mA}$.
5. Mean power: $P = \frac{V_{\text{rms}}^2}{R} = \frac{1.06^2}{200} = 5.6 \times 10^{-3}~\text{W} = 5.6~\text{mW}$.

**Answer:** $V_0 = 1.5~\text{V}$; $V_{\text{rms}} = 1.06~\text{V}$; $T = 20~\text{ms}$; $f = 50~\text{Hz}$; $I_{\text{rms}} = 5.3~\text{mA}$; $P = 5.6~\text{mW}$.

### 1.6 The transformer — construction and the turns-ratio equation

A transformer has two coils wound on a **soft iron core** (laminated to reduce eddy currents). There is **no electrical connection** between the coils; energy is transferred by the **changing magnetic flux** in the core.

| Coil | Symbol | Description |
|---|---|---|
| **Primary** | $N_{\text{p}}$, $V_{\text{p}}$, $I_{\text{p}}$ | Connected to the input a.c. supply |
| **Secondary** | $N_{\text{s}}$, $V_{\text{s}}$, $I_{\text{s}}$ | Delivers the transformed output |

The e.m.f. induced in each coil follows Faraday's law. Because both coils link the **same flux** $\Phi$ in the core, flux linkage per turn is the same, giving the **turns-ratio equation**:

$$\frac{V_{\text{s}}}{V_{\text{p}}} = \frac{N_{\text{s}}}{N_{\text{p}}}$$

- $V_{\text{s}}$, $V_{\text{p}}$ are the (r.m.s. or peak) voltages across secondary and primary, in V — the ratio is the same for r.m.s. or peak because the factor $\frac{1}{\sqrt{2}}$ cancels.
- $N_{\text{s}}$, $N_{\text{p}}$ are the numbers of turns (dimensionless).

**Step-up** transformer: $N_{\text{s}} > N_{\text{p}}$, so $V_{\text{s}} > V_{\text{p}}$.
**Step-down** transformer: $N_{\text{s}} < N_{\text{p}}$, so $V_{\text{s}} < V_{\text{p}}$.

If the transformer is **ideal** (100% efficient, no power loss), power in = power out:

$$P_{\text{p}} = P_{\text{s}} \quad \Rightarrow \quad I_{\text{p}} V_{\text{p}} = I_{\text{s}} V_{\text{s}} \quad \Rightarrow \quad \frac{I_{\text{s}}}{I_{\text{p}}} = \frac{V_{\text{p}}}{V_{\text{s}}} = \frac{N_{\text{p}}}{N_{\text{s}}}$$

Voltage ratio and current ratio are **inverse**: stepping voltage up steps current down by the same factor.

**Worked example:** A radio needs $6.0~\text{V}$ from the $230~\text{V}$ mains. The primary has $5000$ turns. Find $N_{\text{s}}$ and the turns ratio.

1. $\frac{N_{\text{s}}}{N_{\text{p}}} = \frac{V_{\text{s}}}{V_{\text{p}}} = \frac{6.0}{230} = 0.0261$.
2. $N_{\text{s}} = 0.0261 \times 5000 = 130$ turns.

**Answer:** Turns ratio $N_{\text{s}}/N_{\text{p}} = 0.026$; $N_{\text{s}} = 130$ turns (step-down by $\approx 38\times$).

**Worked example:** The mains $240~\text{V}$ r.m.s. primary has $1200$ turns; the secondary r.m.s. output is $6.0~\text{V}$. Find $N_{\text{s}}$.

1. $N_{\text{s}} = N_{\text{p}} \times \frac{V_{\text{s}}}{V_{\text{p}}} = 1200 \times \frac{6.0}{240} = 30$ turns.

**Answer:** $N_{\text{s}} = 30$ turns.

**Worked example:** A step-up transformer has turns ratio $N_{\text{s}}/N_{\text{p}} = 10$. With $V_{\text{p}} = 20~\text{V}$ a.c. and $I_{\text{p}} = 50~\text{mA}$ (ideal, no loss), find $V_{\text{s}}$ and $I_{\text{s}}$.

1. $V_{\text{s}} = 10 \times 20 = 200~\text{V}$.
2. $I_{\text{s}} = I_{\text{p}} \times \frac{N_{\text{p}}}{N_{\text{s}}} = 50 \times \frac{1}{10} = 5.0~\text{mA}$ (check: $20 \times 50 = 200 \times 5.0$ — power conserved).

**Answer:** $V_{\text{s}} = 200~\text{V}$; $I_{\text{s}} = 5.0~\text{mA}$ (ideal).

### 1.7 Real transformers — losses and efficiency

No transformer is truly ideal. Power is lost as:

| Loss | Cause | How it is reduced |
|---|---|---|
| **Copper loss** ($I^2R$ heating) | Resistance of the copper windings | Thicker wire / lower-resistance copper |
| **Eddy currents** | Changing flux induces circulating currents in the iron core, heating it | **Laminated core** — thin insulated sheets break up the current paths |
| **Hysteresis loss** | Energy needed to repeatedly magnetise and demagnetise the core | **Soft iron** core (narrow hysteresis loop) |
| **Flux leakage** | Not all flux from primary links the secondary | Winding coils close together / on same limb; good core design |

Efficiency:

$$\text{efficiency} = \frac{P_{\text{out}}}{P_{\text{in}}} \times 100\% = \frac{I_{\text{s}} V_{\text{s}}}{I_{\text{p}} V_{\text{p}}} \times 100\%$$

If efficiency $< 100\%$, then $I_{\text{s}} V_{\text{s}} < I_{\text{p}} V_{\text{p}}$ and $\frac{V_{\text{s}}}{V_{\text{p}}}$ is slightly less than $\frac{N_{\text{s}}}{N_{\text{p}}}$.

In exam questions "assume the transformer is ideal / 100% efficient" means you can use $I_{\text{p}} V_{\text{p}} = I_{\text{s}} V_{\text{s}}$. Without that statement, check whether input and output powers are given separately.

**Worked example:** The ideal calculation above gave $V_{\text{s}} = 200~\text{V}$ and $I_{\text{s}} = 5.0~\text{mA}$. In practice $V_{\text{s}} = 180~\text{V}$ and $I_{\text{s}} = 4.5~\text{mA}$ with $V_{\text{p}} = 20~\text{V}$, $I_{\text{p}} = 50~\text{mA}$. Find the efficiency.

1. $P_{\text{in}} = 20 \times 0.050 = 1.00~\text{W}$.
2. $P_{\text{out}} = 180 \times 0.0045 = 0.81~\text{W}$.
3. Efficiency $= \frac{0.81}{1.00} \times 100\% = 81\%$; power wasted $= 19\%$.

**Answer:** $81\%$ efficient; $19\%$ of the power is wasted (as heat in windings and core).

**Worked example:** A transformer steps $25~\text{kV}$ up to $400~\text{kV}$. The primary has $2000$ turns. Find $N_{\text{s}}$.

1. $N_{\text{s}} = 2000 \times \frac{400}{25} = 32\,000$ turns.

**Answer:** $N_{\text{s}} = 3.2 \times 10^4$ turns.

### 1.8 Transmission of electrical energy at high voltage

Power stations generate at $\approx 25~\text{kV}$. Before transmission the voltage is stepped up to $132$–$400~\text{kV}$ (up to $1~\text{MV}$ in some countries); near the consumer it is stepped down again.

**Why high voltage?** For a given power $P$ to be delivered, $P = IV$. At higher $V$, the current $I = \frac{P}{V}$ is **smaller**. The power **lost as heat** in the cables is $P_{\text{loss}} = I^2 R$. So doubling the transmission voltage halves the current and **quarters** the loss ($P_{\text{loss}} \propto \frac{1}{V^2}$).

This saves fuel, reduces the number of power stations needed, and is the single most important reason for using a.c.: a.c. can be transformed easily; d.c. historically could not (modern power electronics can now transform d.c. too, so d.c. grids are becoming viable for solar/photovoltaic systems).

The calculation does **not** change the cable resistance $R$ — only the current $I$ changes.

**Worked example:** A power station generates $10~\text{MW}$ along cables of total resistance $10~\Omega$. Compare losses at $50~\text{kV}$ and $250~\text{kV}$.

1. At $50~\text{kV}$: $I = \frac{10 \times 10^6}{50 \times 10^3} = 200~\text{A}$; $P_{\text{loss}} = 200^2 \times 10 = 4.0 \times 10^5~\text{W} = 400~\text{kW}$.
2. At $250~\text{kV}$: $I = \frac{10 \times 10^6}{250 \times 10^3} = 40~\text{A}$; $P_{\text{loss}} = 40^2 \times 10 = 1.6 \times 10^4~\text{W} = 16~\text{kW}$.
3. Voltage $\times 5$ $\rightarrow$ current $\div 5$ $\rightarrow$ loss $\div 25$.

**Answer:** $400~\text{kW}$ at $50~\text{kV}$; $16~\text{kW}$ at $250~\text{kV}$ — a factor-of-25 saving. The $250~\text{kV}$ loss is only $0.16\%$ of the transmitted power.

**Worked example:** Electrical energy is supplied at $400~\text{kV}$ r.m.s. with input power $500~\text{MW}$ along a line of resistance $4.0~\Omega$. Find $I_{\text{rms}}$ and $P_{\text{loss}}$.

1. $I_{\text{rms}} = \frac{P}{V_{\text{rms}}} = \frac{500 \times 10^6}{400 \times 10^3} = 1250~\text{A}$.
2. $P_{\text{loss}} = I_{\text{rms}}^2 R = 1250^2 \times 4.0 = 6.25 \times 10^6~\text{W} = 6.25~\text{MW}$ ($\approx 1.25\%$ of the transmitted power).
3. At $124~\text{kV}$ the same power would need $I = 4030~\text{A}$ and $P_{\text{loss}} = 65~\text{MW}$ — more than ten times larger.

**Answer:** $I_{\text{rms}} = 1.25 \times 10^3~\text{A}$; $P_{\text{loss}} = 6.3~\text{MW}$ at $400~\text{kV}$.

### 1.9 Rectification — turning a.c. into d.c.

Many devices (phones, laptops, electronics) need **d.c.**, but the mains is a.c. **Rectification** converts a.c. to d.c. using **diodes** (components that conduct in one direction only — forward, and block in reverse).

| Type | Diodes | Output waveform | Mean power vs a.c. |
|---|---|---|---|
| **Half-wave** | 1 diode | Current flows for one half-cycle, zero for the next; output is always $\ge 0$ but has gaps | Half the full-wave power (one half-cycle wasted) |
| **Full-wave (bridge)** | 4 diodes in a diamond | Both half-cycles are flipped positive; output is always $\ge 0$ with no gaps, frequency doubled | Almost full a.c. power (minus small diode drops) |

**Half-wave:** during the forward half-cycle the diode conducts and $V_R > 0$; during the reverse half-cycle the diode blocks and $V_R = 0$. The output is "bumpy d.c." at the supply frequency.

**Full-wave bridge (Fig. 29.16–29.17):** label the bridge A–B–C–D clockwise with supply across one diagonal and load $R$ across the other.

- When terminal $X$ is positive: current flows $\rightarrow$ diode $B$ $\rightarrow$ down through $R$ $\rightarrow$ diode $C$ $\rightarrow$ terminal $Y$.
- When terminal $Y$ is positive: current flows $\rightarrow$ diode $D$ $\rightarrow$ down through $R$ $\rightarrow$ diode $A$ $\rightarrow$ terminal $X$.

In **both** half-cycles the current through $R$ flows the **same way** (downwards), so the top of $R$ is always positive. Diodes $A$/$C$ and $B$/$D$ conduct on alternate half-cycles; the other pair blocks because it is reverse-biased. The rectified frequency is **twice** the supply frequency.

**Worked example:** A $6.0~\text{V}$ r.m.s. sinusoidal supply is half-wave rectified through an ideal diode and a $400~\Omega$ resistor. Sketch the output and find its peak.

1. Peak of supply: $V_0 = \sqrt{2} \times 6.0 = 8.5~\text{V}$.
2. When the diode conducts (positive half-cycle), $V_R = V_{\text{supply}}$ (ideal diode, no drop).
3. When the diode blocks (negative half-cycle), $V_R = 0$.
4. The output is the positive half-sine at $8.5~\text{V}$ peak, zero for the other half-cycle, repeating at $50~\text{Hz}$.

**Answer:** Half-wave output: $0$ to $8.5~\text{V}$ sine on alternate half-cycles; the other half-cycle is $0$.

**Worked example:** Why does a bridge rectifier deliver more mean power than a single diode?

1. Half-wave uses only one half-cycle: mean power $\approx \frac{1}{2}$ of the full a.c. mean power.
2. Full-wave bridge flips the negative half-cycle positive, so both half-cycles contribute: almost the full mean power is delivered (for ideal diodes, essentially the same as the a.c. mean power).

**Answer:** Full-wave uses both half-cycles; half-wave wastes one half-cycle.

### 1.10 Smoothing — the capacitor that fills the gaps

Rectified output is still "bumpy" — it falls to zero (half-wave) or near zero (full-wave) each cycle. A **smoothing capacitor** $C$ is connected **in parallel (across) the load resistor $R$** to make the output steadier.

**How it works:**

1. When the rectified voltage rises, the capacitor **charges up** quickly through the low-resistance diode path to near the peak voltage $V_0$.
2. When the rectified voltage falls, the diode stops conducting (the capacitor voltage is now higher than the supply voltage, so the diode is reverse-biased). The capacitor then **discharges slowly** through $R$, maintaining the voltage across $R$ while the supply is low.
3. On the next peak the capacitor recharges. The result is a voltage with small **ripple** — it never falls far before being topped up.

**The smoothing improves when $RC$ (the time constant) is larger:**

- Larger $C$: stores more charge, discharges more slowly $\rightarrow$ less ripple.
- Larger $R$: draws less current, so $C$ discharges more slowly $\rightarrow$ less ripple.
- Smaller $C$ or smaller $R$: faster discharge $\rightarrow$ more ripple, lower mean voltage.

But if $RC$ is too large the circuit cannot respond quickly to changes in load — a trade-off set by the designer.

In exam sketches: charging is the **steep rising edge** following the rectified sine to the peak; discharging is the **gentle exponential decay** between peaks. Mark the charging interval (short) and the discharging interval (most of the cycle).

**Worked example:** A bridge-rectified $50~\text{Hz}$ supply is smoothed by $C$ across $R$. The smoothed $V$–$t$ graph (Fig. 29.20 / Fig. 6.2) shows ripple between $5.0~\text{V}$ and $6.0~\text{V}$ with period $10~\text{ms}$ (full-wave, so $100~\text{Hz}$ ripple). $C = 5.0~\mu\text{F}$. Estimate $R$ from the discharge.

1. Ripple (drop during discharge): $\Delta V = 1.0~\text{V}$.
2. Charge lost during discharge: $\Delta Q = C\,\Delta V = 5.0 \times 10^{-6} \times 1.0 = 5.0 \times 10^{-6}~\text{C}$.
3. Discharge time $\approx$ most of the $10~\text{ms}$ cycle $\approx 9~\text{ms}$ (charging is brief, $\approx 1~\text{ms}$ near the peak).
4. Mean current during discharge: $I \approx \frac{\Delta Q}{\Delta t} = \frac{5.0 \times 10^{-6}}{9 \times 10^{-3}} = 5.6 \times 10^{-4}~\text{A}$.
5. Mean voltage during discharge $\approx 5.5~\text{V}$; so $R \approx \frac{V}{I} = \frac{5.5}{5.6 \times 10^{-4}} \approx 9.8 \times 10^3~\Omega$.

**Answer:** $R \approx 10~\text{k}\Omega$ (order-of-magnitude; accept $5$–$15~\text{k}\Omega$ depending on $\Delta t$ reading).

**Worked example:** What happens to the ripple if (a) $R$ is increased, (b) $C$ is decreased?

1. (a) Larger $R$ $\rightarrow$ smaller discharge current $I = V/R$ $\rightarrow$ slower discharge $\rightarrow$ **less ripple**, higher mean voltage.
2. (b) Smaller $C$ $\rightarrow$ less charge stored ($\Delta Q = C\Delta V$) $\rightarrow$ faster discharge $\rightarrow$ **more ripple**, lower mean voltage.

**Answer:** (a) Ripple decreases; (b) ripple increases.

**Worked example:** A second capacitor of equal value is placed in parallel with $C$. What happens?

1. Capacitances in parallel add: $C_{\text{total}} = 2C$.
2. $RC$ doubles $\rightarrow$ slower discharge $\rightarrow$ **less ripple**, higher mean voltage, and the mean power in $R$ increases.

**Answer:** Ripple decreases; mean $V$ and mean power increase.

### 1.11 The transformer and electromagnetic induction — flux, e.m.f. and phase

The transformer is an application of **Faraday's law** and **Lenz's law** (Chapter 28):

- **Faraday's law:** the induced e.m.f. is proportional to the **rate of change of magnetic flux linkage**: $E = -N\frac{\Delta \Phi}{\Delta t}$ (magnitude $E = N\frac{\Delta \Phi}{\Delta t}$).
- **Lenz's law:** the induced e.m.f. opposes the change that produces it (the minus sign).

If the primary current is $I_{\text{p}} = I_0 \sin \omega t$, the flux in the core is $\Phi \propto I_{\text{p}}$, so $\Phi = \Phi_0 \sin \omega t$ (in phase with the primary current). The e.m.f. induced in any coil is $E \propto \frac{d\Phi}{dt} = \omega\Phi_0 \cos \omega t$, which is **$90°$ out of phase** with the flux (and with the primary current): when the flux is at a maximum, its rate of change is zero, so the induced e.m.f. is zero, and vice versa. This is why the exam asks you to draw the flux graph (same shape as the current) and the induced e.m.f. graph (a cosine — shifted by a quarter cycle) on the same axes.

**Worked example:** The primary current graph is a sine wave. Sketch on the same axes (i) the flux in the core, (ii) the e.m.f. induced in the primary.

1. Flux $\Phi \propto I_{\text{p}}$: same sine shape as the current, in phase, labelled A.
2. Induced e.m.f. $E \propto \frac{d\Phi}{dt}$: cosine shape, $90°$ ahead (or behind) the flux, zero when flux is at its peak, maximum when flux passes through zero, labelled B.

**Answer:** Flux = sine (in phase with current); e.m.f. = cosine (quarter-cycle shift, zero at flux maxima).

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

