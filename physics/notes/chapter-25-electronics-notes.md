# Chapter 25: Electronics - CAIE A Level Physics (9702) Study Notes

Exam-focused revision notes for Cambridge International AS & A Level Physics 9702, covering the electronics content as taught in Chapter 25 of the coursebook. Everything here is what the exam can actually ask, nothing more. All definitions are worded to match mark schemes, and every question type below has appeared in real 9702 papers (mainly Paper 4 structured questions and Paper 1 multiple choice). Every theory section ends with a worked example, so you can see the formula being used the moment it is introduced.

## 1. Theory

### 1.1 Electronic sensing systems (sensing device - processor - output device)

Almost every electronic sensing system has the same three-part structure:

$$ \text{sensing device} \rightarrow \text{processor} \rightarrow \text{output device} $$

The **sensing device** is an electronic component with a property - usually its resistance - that changes when a physical quantity such as temperature, light intensity or pressure changes. The **processor** uses that change to produce an output voltage. The **output device** (a heater, an LED, a relay, a meter, a loudspeaker) does something useful with that voltage. An incubator for a newborn baby is the classic example: a thermistor senses the air temperature, a processor produces a voltage that drives the heater, and the heater switches on when the air gets cold and off when it gets warm.

The sensing device is often called a **transducer**: a device that changes energy from one form into another. A piezo-electric microphone changes sound energy into electrical energy. Even a thermistor can be called a transducer, because a change in the internal energy of the air changes the electrical energy in the thermistor circuit.

The exam does not care how the processor works inside (it usually contains transistors or an op-amp). It only cares that you can name the three parts, say what each does, and match them to a described system.

**Worked example:** A security light uses an LDR to switch on a lamp when it gets dark. State the sensing device, the processor and the output device, and say what property of the sensing device changes.

1. Sensing device: the light-dependent resistor (LDR). Its property is its resistance, which increases as the light intensity falls.
2. Processor: the circuit (potential divider plus switching circuit) that converts the resistance change into a voltage that operates the lamp.
3. Output device: the lamp.

**Answer:** LDR (resistance changes with light), processor (produces the output voltage), lamp (the output device).

### 1.2 The light-dependent resistor (LDR)

An **LDR** is made of a high-resistance semiconductor. When light of high enough frequency falls on it, photons are absorbed by the semiconductor and electrons are released from the atoms. These free electrons conduct electricity, so the resistance of the semiconductor falls. The key facts to quote in an exam:

- More light means more free electrons, so **resistance decreases as light intensity increases**.
- Only light of high enough frequency (i.e. photons with enough energy) causes this - a low frequency like red light may not release electrons.
- The change is not linear: a graph of resistance against light intensity is a curve that falls steeply at low intensities and flattens off.
- Typical values: a few hundred ohms in bright sunlight, millions of ohms in darkness.

**Worked example:** A typical LDR has a resistance of $500~\Omega$ in bright sunlight and $5.0~\text{M}\Omega$ in darkness. It is connected across a $9.0~\text{V}$ supply. Calculate the current through it in each case, and the ratio of the two currents.

1. Bright: $I = \frac{V}{R} = \frac{9.0}{500} = 1.8 \times 10^{-2}~\text{A} = 18~\text{mA}$.
2. Dark: $I = \frac{9.0}{5.0 \times 10^6} = 1.8 \times 10^{-6}~\text{A} = 1.8~\mu\text{A}$.
3. Ratio: $\frac{18~\text{mA}}{1.8~\mu\text{A}} = 1.0 \times 10^4$.

**Answer:** $18~\text{mA}$ in sunlight, $1.8~\mu\text{A}$ in darkness, a ratio of $10^4$ (ten thousand to one).

**Worked example:** The graph of resistance against light intensity for an LDR shows that the resistance is $60~\text{k}\Omega$ at $10~\text{lux}$ and $20~\text{k}\Omega$ at $60~\text{lux}$. Calculate the percentage decrease in resistance when the light intensity rises from $10$ to $60~\text{lux}$.

1. Change in resistance: $\Delta R = 60 - 20 = 40~\text{k}\Omega$.
2. Percentage decrease: $\frac{40}{60} \times 100 = 67\%$.

**Answer:** the resistance falls by $67\%$ (to a third of its original value) as the intensity rises from $10$ to $60~\text{lux}$.

### 1.3 The thermistor (NTC thermistor)

A **negative temperature coefficient (NTC) thermistor** is a semiconductor component whose **resistance falls as the temperature rises**. This is because, in a semiconductor, a rise in temperature increases the number of free electrons available to carry current.

A metal wire behaves the opposite way: its resistance **rises** with temperature (the metal ions vibrate more and scatter the electrons more). A metal wire could in principle be used as a temperature sensor, but a thermistor is much more useful because:

- the change in resistance per degree is far larger for a thermistor, and
- the thermistor can be made very small, so it responds quickly and measures the temperature of a small region.

The thermistor's resistance-temperature graph is **not linear**: the resistance falls roughly exponentially with temperature. This matters for any measuring instrument built with a thermistor: the scale must be **calibrated** against a known thermometer, because dividing the resistance range into equal parts would not give equal temperature steps.

**Worked example:** An NTC thermistor has a resistance of $20~\text{k}\Omega$ at $20~^\circ\text{C}$ and $100~\Omega$ at $60~^\circ\text{C}$. Calculate the percentage decrease in resistance between these temperatures.

1. Change: $\Delta R = 20\,000 - 100 = 19\,900~\Omega$.
2. Percentage decrease: $\frac{19\,900}{20\,000} \times 100 = 99.5\%$.

**Answer:** the resistance falls by $99.5\%$ (a factor of 200) for a $40~^\circ\text{C}$ rise in temperature. The exponential-type fall is why any measuring circuit must be calibrated.

### 1.4 Piezo-electric transducers

Some crystals, such as quartz, produce an electric field when a force is applied and the shape of the crystal changes. This is the **piezo-electric effect**. A piezo-electric crystal contains positive and negative ions in a regular arrangement. When the crystal is stressed (squeezed, stretched or bent), the ions shift slightly and a small voltage appears between the faces of the crystal. The crystal is a transducer: it changes mechanical energy into electrical energy.

The most common use in this syllabus is the **microphone**. A thin sheet of piezo-electric crystal has metal connections on opposite faces. When a sound wave hits the sheet, the compressions and rarefactions make the pressure on it rise and fall, the crystal changes shape, and a small alternating voltage is produced across the connections. The same idea is used in acoustic guitar pickups, and in reverse in ultrasound scanners (Chapter 32), where a voltage makes the crystal vibrate and emit sound.

A piezo-electric microphone has a very high internal resistance and cannot supply much current, so its output is usually fed into an op-amp with a very high input resistance (Section 1.8): the op-amp does not load the microphone and the full signal reaches the amplifier.

**Worked example:** A piezo-electric microphone produces a maximum output of $20~\text{mV}$ when a loud sound strikes it. The microphone has an internal resistance of $1.0~\text{M}\Omega$ and is connected to an ideal op-amp with infinite input resistance. State the voltage that appears at the op-amp input, and explain why the op-amp's input resistance matters.

1. No current is drawn from the microphone (infinite input resistance), so there are no lost volts across its internal resistance: the full $20~\text{mV}$ appears at the input.
2. If the op-amp drew current, the microphone's $1.0~\text{M}\Omega$ internal resistance would form a potential divider with the input resistance, and the signal would be reduced.

**Answer:** the input voltage is $20~\text{mV}$; the infinite input resistance prevents lost volts, so the whole signal reaches the amplifier.

### 1.5 The metal-wire strain gauge

A **strain gauge** measures how much a surface stretches (strains). It is a thin metal wire zigzagging back and forth between two thin sheets of plastic, so that a long length of wire fits into a small gauge. The gauge is glued to the surface being monitored - a wall with a crack in it, or an aircraft wing under test.

When the wire is stretched it becomes **longer and narrower**, and both changes increase its resistance. When compressed (as long as it does not buckle) it becomes shorter and wider, and its resistance decreases. Using $R = \frac{\rho L}{A}$:

- If the cross-sectional area $A$ is taken as constant, stretching by a small amount $\delta L$ gives $\delta R = \frac{\rho\,\delta L}{A}$, and dividing by $R = \frac{\rho L}{A}$:

$$ \frac{\delta R}{R} = \frac{\delta L}{L} $$

- In practice the volume stays roughly constant, so the wire also narrows, and the effect is doubled. For small changes:

$$ \frac{\delta R}{R} = \frac{2\,\delta L}{L} $$

Either way, **the change in resistance is directly proportional to the increase in length**: $\delta R \propto \delta L$. The resistance change is tiny, but a suitable series resistor and cell turn it into a measurable output voltage (Section 1.6). The **strain** is defined as the fractional change in length, $\text{strain} = \frac{\delta L}{L}$, which is a ratio and has no units.

**Worked example:** A strain gauge wire has resistance $120.0~\Omega$ and length $10.00~\text{cm}$ when unstretched. It is stretched by $0.10~\text{cm}$. Assuming the volume stays constant, calculate the new resistance.

1. Use $\frac{\delta R}{R} = \frac{2\,\delta L}{L}$: $\frac{\delta R}{120.0} = \frac{2 \times 0.10}{10.00} = 0.020$.
2. $\delta R = 0.020 \times 120.0 = 2.4~\Omega$.
3. New resistance: $R = 120.0 + 2.4 = 122.4~\Omega$.

**Answer:** $R = 122.4~\Omega$ (this matches the measured value in the coursebook's worked example, which confirms that the volume stays roughly constant during stretching).

**Worked example:** A strain gauge glued to a metal bar shows an increase in resistance of $2.9~\Omega$. Its unstretched resistance is $120.0~\Omega$ and its length is $10.00~\text{cm}$. Calculate the extension of the bar and the strain.

1. $\frac{\delta R}{R} = \frac{2.9}{120.0} = 0.0242$.
2. Using $\frac{\delta R}{R} = \frac{2\,\delta L}{L}$: $\delta L = \frac{0.0242 \times 10.00}{2} = 0.12~\text{cm}$.
3. Strain $= \frac{\delta L}{L} = \frac{0.12}{10.00} = 0.012 = 1.2\%$.

**Answer:** extension $\delta L = 0.12~\text{cm}$; strain $= 1.2 \times 10^{-2}$ (dimensionless).

### 1.6 Potential-divider sensing circuits

An LDR or thermistor only changes its **resistance**. To turn that into a changing **voltage**, the sensor is placed in series with a fixed resistor across a supply, forming a potential divider. The supply voltage is shared between the two resistors in proportion to their resistances, so as the sensor's resistance changes, the voltage across each resistor changes too:

$$ V_{\text{out}} = \frac{R_2}{R_1 + R_2} \times V_{\text{supply}} $$

where $V_{\text{out}}$ is the p.d. across the resistor $R_2$ in the formula, $R_1$ is the other resistor, and $V_{\text{supply}}$ is the total supply p.d.

The direction of the output change depends on which component the output is taken across:

- Output **across the sensor**: when the sensed quantity rises, the sensor resistance falls (for LDR and NTC thermistor), so the sensor takes a smaller share of the voltage and $V_{\text{out}}$ **decreases**.
- Output **across the fixed resistor**: the fixed resistor then takes a larger share, so $V_{\text{out}}$ **increases** when the sensed quantity rises.

In the LDR circuit of the coursebook, an LDR of resistance $R$ is in series with a $3.0~\text{k}\Omega$ resistor across a $10~\text{V}$ supply, with the output across the LDR. As the light intensity rises the LDR resistance falls and $V_{\text{out}}$ falls. To get an output that rises with light intensity, simply take the output across the fixed resistor instead.

These circuits draw very little current, which matters because electronic processors (transistors, op-amps) take only tiny input currents. Where large currents are involved, a potential divider wastes power in its two resistors, so it is only used in low-current applications.

**Worked example:** In the coursebook circuit, the LDR has resistance $20~\text{k}\Omega$ at a light intensity of $60~\text{lux}$. The fixed resistor is $3.0~\text{k}\Omega$ and the supply is $10~\text{V}$. The output is across the LDR. Calculate $V_{\text{out}}$.

1. Total resistance: $R_{\text{total}} = 20 + 3.0 = 23~\text{k}\Omega$.
2. The LDR takes the fraction $\frac{20}{23}$ of the supply: $V_{\text{out}} = \frac{20}{23} \times 10 = 8.70~\text{V}$.

**Answer:** $V_{\text{out}} = 8.70~\text{V}$ (to 3 significant figures - the calculator shows $8.69565$, which rounds up to $8.70$, not down to $8.69$).

**Worked example:** An NTC thermistor has resistance $20~\text{k}\Omega$ at $20~^\circ\text{C}$ and $100~\Omega$ at $60~^\circ\text{C}$. It is connected in series with a $1.0~\text{k}\Omega$ fixed resistor across a $10~\text{V}$ supply, with the output across the thermistor. Calculate $V_{\text{out}}$ at each temperature.

1. At $20~^\circ\text{C}$: $V_{\text{out}} = \frac{20}{20 + 1.0} \times 10 = 9.52~\text{V}$.
2. At $60~^\circ\text{C}$: $V_{\text{out}} = \frac{0.10}{0.10 + 1.0} \times 10 = 0.91~\text{V}$.

**Answer:** $V_{\text{out}} = 9.5~\text{V}$ at $20~^\circ\text{C}$, falling to $0.91~\text{V}$ at $60~^\circ\text{C}$ - the output across the thermistor decreases as temperature rises.

### 1.7 The operational amplifier (op-amp)

An **operational amplifier** is a high-gain voltage amplifier built from many transistors and resistors inside one package. It has two inputs and one output:

- the **inverting input** marked $(-)$,
- the **non-inverting input** marked $(+)$,
- the single **output**.

It needs two power supplies, one between the positive supply line $+V_s$ and the zero-volt line (earth), and one between the negative supply line $-V_s$ and earth. All voltages are measured relative to the zero-volt line. The power supplies provide the output power - the op-amp is not like a transformer, which passes input power through; an op-amp's output power comes from the supplies, so it is much larger than the input power.

The op-amp's one function is to multiply the potential difference between the two inputs by a very large factor, the **open-loop voltage gain** $G_0$:

$$ V_{\text{out}} = G_0 \times (V_+ - V_-) $$

where $V_+$ is the potential at the non-inverting input and $V_-$ the potential at the inverting input. The gain is called "open-loop" because no loop of components connects the output back to the input.

The output cannot exceed the supply voltages: with $\pm 9~\text{V}$ supplies the output is limited to between $+9~\text{V}$ and $-9~\text{V}$. When the output reaches either supply voltage, the amplifier is said to be **saturated**.

**Worked example:** An op-amp with $\pm 9~\text{V}$ supplies has open-loop gain $G_0 = 10^5$. The inputs are at $V_+ = 0.15~\text{V}$ and $V_- = 0.10~\text{V}$. Calculate the output voltage.

1. $V_{\text{out}} = G_0 (V_+ - V_-) = 10^5 \times (0.15 - 0.10) = 5000~\text{V}$.
2. This is impossible - the output cannot exceed the supply. The op-amp is saturated, so $V_{\text{out}} = +9~\text{V}$ (the positive rail, because $V_+ > V_-$).

**Answer:** the output saturates at $V_{\text{out}} = +9~\text{V}$.

**Worked example:** An op-amp with $\pm 9~\text{V}$ supplies has $G_0 = 10^5$. Calculate the smallest difference between $V_+$ and $V_-$ for which the op-amp is not saturated.

1. The output must stay within $\pm 9~\text{V}$: $|V_+ - V_-| < \frac{9}{G_0}$.
2. $|V_+ - V_-| < \frac{9}{10^5} = 9 \times 10^{-5}~\text{V} = 90~\mu\text{V}$.

**Answer:** the input difference must be smaller than $90~\mu\text{V}$; any larger difference saturates the output.

### 1.8 Properties of an ideal op-amp

The exam regularly asks for the properties of an **ideal** op-amp. Learn the list and what each property means:

1. **Infinite open-loop voltage gain.** Used alone, a tiny input produces a huge output (in practice the output saturates at $\pm V_s$). With a feedback loop, the circuit gain is set by the external resistors and the infinite open-loop gain makes that gain accurate and the same for a wide range of frequencies.
2. **Infinite input resistance (impedance).** No current enters the input terminals. The op-amp does not load the device feeding it, so a signal source with a high internal resistance (like a piezo-electric microphone) suffers no lost volts.
3. **Zero output resistance (impedance).** The output acts like a battery with zero internal resistance, so there are no lost volts when the op-amp supplies current to the next stage.
4. **Infinite bandwidth.** All frequencies are amplified by the same amount, so the output is an undistorted copy of the input.
5. **Infinite slew rate.** The output changes instantly when the input changes; there is no time delay.
6. **Zero noise contribution.** The op-amp adds no noise of its own (it still amplifies any noise in the input signal).

Real op-amps fall short: open-loop gains of around $10^5$, input resistances up to $10^{12}~\Omega$ (with $10^6~\Omega$ typical), output resistances around $75~\Omega$, and bandwidths that may be only a few kilohertz.

**Worked example:** A piezo-electric microphone has an internal resistance of $100~\text{k}\Omega$ and produces an e.m.f. of $25~\text{mV}$. (a) Calculate the input voltage to an ideal op-amp with infinite input resistance. (b) Calculate the input voltage if the op-amp instead had an input resistance of $1.0~\text{M}\Omega$.

1. (a) No current flows, so there are no lost volts: $V_{\text{in}} = 25~\text{mV}$.
2. (b) The internal resistance and input resistance form a potential divider: $V_{\text{in}} = 25 \times \frac{1.0 \times 10^6}{1.0 \times 10^6 + 1.0 \times 10^5} = 22.7~\text{mV}$.

**Answer:** (a) $V_{\text{in}} = 25~\text{mV}$; (b) $V_{\text{in}} = 23~\text{mV}$ - about 9% of the signal is lost to the loading effect, which is why high input resistance matters.

### 1.9 The op-amp as a comparator

A **comparator** uses the op-amp with no feedback loop, so the huge open-loop gain drives the output straight to one of the supply rails:

- if $V_+$ is slightly **greater** than $V_-$, the output saturates at (close to) the **positive** supply voltage $+V_s$;
- if $V_+$ is slightly **less** than $V_-$, the output saturates at (close to) the **negative** supply voltage $-V_s$.

The output tells you which input potential is larger, and the switch between the rails is sudden because the gain is so large. Two potential dividers provide the two input voltages - one containing the sensor, the other a fixed reference.

In the coursebook's temperature-monitoring circuit, a thermistor $T$ and a $10~\text{k}\Omega$ resistor form a divider feeding point A (the non-inverting input), and two equal $15~\text{k}\Omega$ resistors feed point B (the inverting input) with a fixed $4.5~\text{V}$. At $15~^\circ\text{C}$, $R_T = 8~\text{k}\Omega$:

- potential at A $= 9 \times \frac{10}{8 + 10} = 5.0~\text{V}$
- potential at B $= \frac{9}{2} = 4.5~\text{V}$

Since $V_+ > V_-$, the output is $+9~\text{V}$. As the temperature falls, the NTC thermistor's resistance rises; once it exceeds $10~\text{k}\Omega$, the potential at A falls below $4.5~\text{V}$ and the output switches to $-9~\text{V}$. The temperature at which the switch happens can be adjusted by changing the resistor in series with the thermistor. If the two divider resistors are swapped (thermistor and fixed resistor change places), the switching behaviour reverses: a hot room gives $-9~\text{V}$ and a cold room gives $+9~\text{V}$.

**Worked example:** In the comparator circuit above, the thermistor has resistance $R_T = 3~\text{k}\Omega$. Calculate the potentials at A and B and state the output voltage.

1. Potential at A: $V_A = 9 \times \frac{10}{3 + 10} = 6.9~\text{V}$.
2. Potential at B: $V_B = 4.5~\text{V}$ (the two equal $15~\text{k}\Omega$ resistors share the $9~\text{V}$ equally).
3. $V_+ = V_A = 6.9~\text{V} > V_B = V_- = 4.5~\text{V}$, so the output saturates at the positive rail.

**Answer:** $V_+ = 6.9~\text{V}$, $V_- = 4.5~\text{V}$, $V_{\text{out}} = +9~\text{V}$.

### 1.10 Negative feedback

**Feedback** means taking part (or all) of the output and returning it to the input, so that the system's output affects its own input. The heater example shows it in action: a cold room makes the comparator switch the heater on, the heater warms the air, and the warmed air is "fed back" through the thermistor, which switches the heater off again. The room stays at a reasonably constant temperature. Feedback also controls body temperature: shivering warms the body, and that signal is fed back to the brain, which stops the shivering.

In an op-amp circuit, the simplest feedback connection joins the output directly to the inverting input. Then $V_- = V_{\text{out}}$ and, since the open-loop gain is huge, the input difference is driven almost to zero, so $V_{\text{out}} = V_{\text{in}}$: the closed-loop gain is

$$ G = \frac{V_{\text{out}}}{V_{\text{in}}} = \frac{G_0}{1 + G_0} \approx 1 $$

With $G_0 = 10^5$ the gain is $0.99999$ - effectively 1. This "voltage follower" is hardly an amplifier, but it is extremely useful as a **buffer**: it draws almost no current from the input device, yet can supply a reasonable current to the output, and it isolates one circuit from another. A piezo-electric microphone (high internal resistance, little current available) connected to a follower gives the same voltage out but with more current.

The benefits of negative feedback (quoted constantly in mark schemes):

- **less distortion** - all frequencies are amplified by the same amount, so the output is a faithful copy of the input;
- **increased bandwidth** - the range of frequencies with constant gain is widened;
- **more stable gain** - the gain is set by the external resistors, so it is not affected by temperature changes or the op-amp's own variations;
- **low output resistance and high input resistance**.

The price is a lower gain - but the gain is predictable, which is worth far more.

**Worked example:** An op-amp with open-loop gain $G_0 = 10^5$ is connected as a voltage follower. (a) Calculate the closed-loop gain. (b) The input voltage is $+0.10~\text{V}$; calculate the output voltage.

1. (a) $G = \frac{G_0}{1 + G_0} = \frac{10^5}{10^5 + 1} = 0.99999$.
2. (b) $V_{\text{out}} = G \times V_{\text{in}} = 0.99999 \times 0.10 = 0.10~\text{V}$ (to 2 significant figures).

**Answer:** (a) $G = 0.99999 \approx 1$; (b) $V_{\text{out}} = 0.10~\text{V}$ - the follower copies the input voltage but can supply much more current than the input device could.

### 1.11 The inverting amplifier

The **inverting amplifier** is the standard negative-feedback amplifier. In the circuit:

- the non-inverting input $(+)$ is connected to the $0~\text{V}$ line;
- the input voltage is connected to the inverting input through a resistor $R_{\text{in}}$;
- a feedback resistor $R_f$ connects the output back to the inverting input.

The key idea is the **virtual earth approximation**. Because the open-loop gain is very high, the potential difference between the two inputs is almost zero. The non-inverting input is at $0~\text{V}$, so the inverting input must also be at almost $0~\text{V}$ - even though it is not physically connected to earth. Point P (the inverting input) is a **virtual earth**: it behaves as if it were at $0~\text{V}$, but no current can flow into it (infinite input resistance). The approximation holds as long as the op-amp is not saturated.

This gives the gain directly. If the current through $R_{\text{in}}$ is $I_{\text{in}}$ and the current through $R_f$ is $I_f$:

$$ I_{\text{in}} = \frac{V_{\text{in}}}{R_{\text{in}}}, \qquad I_f = \frac{V_{\text{out}}}{R_f} $$

No current enters the inverting input, so the two currents are equal. If $V_{\text{in}}$ is positive, current flows from the input through P to the output, so $V_{\text{out}}$ must be negative (current flows out of a point at $0~\text{V}$ only if the destination is below $0~\text{V}$):

$$ \frac{V_{\text{out}}}{R_f} = -\frac{V_{\text{in}}}{R_{\text{in}}} \qquad \Rightarrow \qquad G = \frac{V_{\text{out}}}{V_{\text{in}}} = -\frac{R_f}{R_{\text{in}}} $$

The minus sign means the output is inverted: a positive input gives a negative output, so an alternating input and output are out of phase by $180^\circ$ ($\pi$ rad). The magnitude of the gain is just the ratio of the two resistors, and it can be any value - including less than 1 (e.g. $R_f = 5~\text{k}\Omega$, $R_{\text{in}} = 10~\text{k}\Omega$ gives $G = -0.5$). The input resistance of the whole amplifier is just $R_{\text{in}}$, because the virtual earth keeps the far end of $R_{\text{in}}$ at $0~\text{V}$.

**Worked example:** An inverting amplifier has $R_{\text{in}} = 4~\text{k}\Omega$ and $R_f = 20~\text{k}\Omega$. (a) Calculate the gain. (b) Calculate the output voltage when the input is $0.50~\text{V}$. (c) The supplies are $\pm 12~\text{V}$; calculate the maximum input voltage before saturation. (d) State the input resistance of the amplifier.

1. (a) $G = -\frac{R_f}{R_{\text{in}}} = -\frac{20}{4} = -5$.
2. (b) $V_{\text{out}} = G \times V_{\text{in}} = -5 \times 0.50 = -2.5~\text{V}$.
3. (c) Saturation occurs when $|V_{\text{out}}| = 12~\text{V}$: $V_{\text{in}} = \frac{12}{5} = 2.4~\text{V}$.
4. (d) The virtual earth means the input sees only $R_{\text{in}}$: input resistance $= 4~\text{k}\Omega$.

**Answer:** (a) $G = -5$; (b) $V_{\text{out}} = -2.5~\text{V}$; (c) $V_{\text{in}} \leq 2.4~\text{V}$; (d) input resistance $= 4~\text{k}\Omega$.

### 1.12 The non-inverting amplifier

The **non-inverting amplifier** applies the input to the non-inverting input and feeds part of the output back to the inverting input through a potential divider ($R_1$ from the output to the inverting input, $R_2$ from the inverting input to the $0~\text{V}$ line).

As long as the op-amp is not saturated, the input difference is almost zero, so $V_- = V_+ = V_{\text{in}}$. The two resistors $R_1$ and $R_2$ form a potential divider across the output, and the voltage across $R_2$ is $V_{\text{in}}$:

$$ \frac{V_{\text{out}}}{R_1 + R_2} = \frac{V_{\text{in}}}{R_2} \qquad \Rightarrow \qquad G = \frac{V_{\text{out}}}{V_{\text{in}}} = \frac{R_1 + R_2}{R_2} = 1 + \frac{R_1}{R_2} $$

Two consequences follow directly:

- the gain is **always greater than 1** (the term $R_1/R_2$ cannot be negative), which is why a non-inverting amplifier can never have a gain below 1;
- the output is **in phase** with the input - a positive input gives a positive output (no minus sign).

The input resistance is extremely high, because the signal drives the non-inverting input directly and an ideal op-amp draws no input current.

**Worked example:** A non-inverting amplifier has $R_1 = 50~\text{k}\Omega$, $R_2 = 5~\text{k}\Omega$ and supplies of $\pm 10~\text{V}$. (a) Calculate the gain. (b) Calculate the output voltage for inputs of $-0.10~\text{V}$ and $+1.0~\text{V}$.

1. (a) $G = 1 + \frac{R_1}{R_2} = 1 + \frac{50}{5} = 11$.
2. (b) For $-0.10~\text{V}$: $V_{\text{out}} = 11 \times (-0.10) = -1.1~\text{V}$.
3. (b) For $+1.0~\text{V}$: $V_{\text{out}} = 11 \times 1.0 = 11~\text{V}$, which exceeds the $+10~\text{V}$ rail, so the output saturates at $+10~\text{V}$.

**Answer:** (a) $G = 11$; (b) $V_{\text{out}} = -1.1~\text{V}$ and $+10~\text{V}$ (saturated).

### 1.13 Output devices (LED, relay, calibrated meters)

**The light-emitting diode (LED).** An LED conducts only when the voltage across it exceeds about $2~\text{V}$ (it varies with colour), and needs about $20~\text{mA}$ for a good light output. It must never be connected straight between the op-amp output and the $0~\text{V}$ line: once the output exceeds $2~\text{V}$, the current would be huge and would damage both the LED and the op-amp. A **series resistor** limits the current:

$$ R = \frac{V_{\text{out}} - 2~\text{V}}{I} $$

Two LEDs wired back to back (one red, one green, with the op-amp output between them) show the state of the output: a positive output lights the green LED, a negative output lights the red one.

**The relay.** A typical op-amp can supply only about $25~\text{mA}$ at up to its supply voltage (usually $\pm 15~\text{V}$ or less). To switch much larger currents or voltages (mains, heaters, motors) the op-amp drives a **relay** - an electromagnetic switch. A small current in the relay coil magnetises an iron core, which pulls a movable arm so that the contacts $A_1$ and $A_2$ close, completing a separate, high-power circuit. The op-amp easily supplies the coil current; the contacts switch the large current.

Two diodes are needed in the relay circuit. When the coil current is switched off, the magnetic flux in the coil collapses rapidly and a large e.m.f. is induced across the coil - large enough to damage the op-amp. A **reverse-biased diode $D_1$** across the coil gives the induced current a safe path round the coil. A second diode $D_2$ in series with the op-amp output ensures current can flow only when the output is positive, so the relay operates only for a positive output (otherwise it would operate for both positive and negative outputs, since the coil does not care about current direction).

**Calibrated meters.** The output voltage of an op-amp is generally not proportional to the physical quantity being measured (a thermistor's resistance falls non-linearly, for example), so the numbers on a voltmeter cannot simply be relabelled in degrees or lux. Instead the meter is **calibrated**: the sensor and a standard thermometer (or light meter) are placed together, readings are taken at many values, and a **calibration graph** of voltmeter reading against the physical quantity is drawn. Any later voltmeter reading can then be converted into a value of the quantity. If the same analogue meter is always used, its scale can be marked directly with values of the quantity - producing a **non-linear scale** (like the top scale on a car speedometer-style multi-scale meter), which must be read carefully between the markings. Digital meters are calibrated the same way, using the graph rather than a marked scale.

**Worked example:** An LED needs $20~\text{mA}$ and conducts when the p.d. across it is $2.0~\text{V}$. It is connected to the output of an op-amp whose maximum output is $12~\text{V}$. Calculate the series resistance required.

1. Voltage across the resistor: $V_R = 12 - 2.0 = 10~\text{V}$.
2. $R = \frac{V_R}{I} = \frac{10}{0.020} = 500~\Omega$.

**Answer:** $R = 500~\Omega$ (never forget to subtract the $2.0~\text{V}$ across the LED, and convert mA to A).

**Worked example:** A relay coil has resistance $300~\Omega$ and needs a current of $20~\text{mA}$ to close its contacts. (a) Calculate the p.d. across the coil when it operates. (b) State why a reverse-biased diode is connected across the coil.

1. (a) $V = IR = 20 \times 10^{-3} \times 300 = 6.0~\text{V}$.
2. (b) When the coil current is switched off, the collapsing magnetic flux induces a large e.m.f. across the coil, which could damage the op-amp; the reverse-biased diode conducts this induced current safely round the coil.

**Answer:** (a) $V = 6.0~\text{V}$ (well within the op-amp's $25~\text{mA}$, $15~\text{V}$ capability); (b) to protect the op-amp from the induced e.m.f. when the relay switches off.

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
