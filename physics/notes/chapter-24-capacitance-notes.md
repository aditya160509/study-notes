# Chapter 24: Capacitance - CAIE A Level Physics (9702) Study Notes

Exam-focused revision notes for Cambridge International AS & A Level Physics 9702, covering Topic 19 (Capacitance) as taught in Chapter 24 of the coursebook. Everything here is what the exam can actually ask, nothing more. All definitions are worded to match mark schemes, and every question type below has appeared in real 9702 papers (mainly Paper 4 structured questions and Paper 1 multiple choice). Every theory section ends with a worked example, so you can see the formula being used the moment it is introduced.

## 1. Theory

### 1.1 What is a capacitor (construction, charging, discharging)

A capacitor is a component that stores electric charge, and therefore energy. It is built from two metal plates (metal foil) separated by an insulating material called the **dielectric**, usually rolled into a cylinder ("Swiss roll" form). The two plates are connected to the two leads of the component.

When a capacitor is charged, the two plates carry **equal and opposite charges**: one plate carries $+Q$ and the other carries $-Q$. The net charge on the whole capacitor is therefore zero. So when the exam talks about "the charge stored by a capacitor", it means $Q$, the magnitude of the charge on **each** plate.

**Charging:** connect the capacitor to a supply. The negative terminal pushes electrons onto one plate, making it negatively charged; electrons are repelled off the other plate, leaving it positively charged. Electrons flow all the way round the circuit, so the current is the same in every part of it (two ammeters in different positions give identical readings). The current stops when the p.d. across the capacitor equals the e.m.f. of the supply: the capacitor is then **fully charged**. Remember that conventional current is the flow of positive charge, so it flows in the **opposite direction** to the electrons.

**Discharging:** connect the two leads together through a resistor (or an LED with a protective resistor): electrons flow back round the circuit and the capacitor discharges. The charge that flows past a point in a given time is the **area under the current-time graph** (just as distance is the area under a speed-time graph), so the charge stored by a capacitor is the area under the current-time graph recorded while it is being charged up.

**Worked example:** During the charging of a capacitor, the charging current is steady at $8.0~\text{mA}$ for $2.5~\text{s}$. Calculate the charge transferred to the plates.

1. Convert the current to amperes: $I = 8.0~\text{mA} = 8.0 \times 10^{-3}~\text{A}$.
2. Use $Q = It$: $Q = 8.0 \times 10^{-3} \times 2.5 = 2.0 \times 10^{-2}~\text{C}$.

**Answer:** $Q = 2.0 \times 10^{-2}~\text{C} = 20~\text{mC}$.

### 1.2 Charge and p.d.: $Q = VC$

For a given capacitor, the charge stored is **directly proportional** to the p.d. across it: double the p.d. and the charge doubles. This is the equation you will use constantly in this chapter:

$$Q = VC$$

- $Q$ is the magnitude of the charge on each plate, in coulombs (C).
- $V$ is the potential difference between the plates, in volts (V).
- $C$ is the capacitance of the capacitor, in farads (F).

The equation shows that the charge stored depends on two things: the capacitance $C$ (how good the capacitor is at storing charge) and the voltage $V$ (how hard the supply pushes). If you know any two of $Q$, $V$ and $C$, you can always find the third by rearranging.

**Worked example:** A $5000~\mu\text{F}$ capacitor is charged to a p.d. of $6.0~\text{V}$. Calculate the charge stored on each plate.

1. Convert the capacitance: $C = 5000~\mu\text{F} = 5.0 \times 10^{-3}~\text{F}$.
2. Use $Q = VC$: $Q = 6.0 \times 5.0 \times 10^{-3} = 3.0 \times 10^{-2}~\text{C}$.

**Answer:** $Q = 3.0 \times 10^{-2}~\text{C} = 30~\text{mC}$.

**Worked example:** A capacitor stores $60~\mu\text{C}$ when charged to a p.d. of $5.0~\text{V}$. Calculate the charge it stores when charged to $15~\text{V}$.

1. Since $Q \propto V$ for a fixed capacitor, tripling the voltage triples the charge: $\frac{15}{5.0} = 3$.
2. New charge: $Q = 3 \times 60~\mu\text{C} = 180~\mu\text{C}$.

**Answer:** $Q = 1.8 \times 10^{-4}~\text{C} = 180~\mu\text{C}$.

### 1.3 Capacitance and the farad (definition, units, prefixes)

**Definition:** the capacitance of a capacitor is the charge stored on one plate per unit potential difference between the plates.

$$C = \frac{Q}{V}$$

- $C$ is the capacitance, in farads (F).
- $Q$ is the charge stored on one plate, in coulombs (C).
- $V$ is the p.d. between the plates, in volts (V).

The unit of capacitance is the **farad** (F). From the definition, $1~\text{F} = 1~\text{C V}^{-1}$ (one coulomb per volt). The farad is a very large unit: few capacitors have a capacitance of $1~\text{F}$, so in practice you meet the sub-units:

| Prefix | Symbol | Value |
| --- | --- | --- |
| micro | $\mu$ | $1~\mu\text{F} = 10^{-6}~\text{F}$ |
| nano | n | $1~\text{nF} = 10^{-9}~\text{F}$ |
| pico | p | $1~\text{pF} = 10^{-12}~\text{F}$ |

**Other markings on capacitors:** most capacitors are marked with their highest safe **working voltage**. If you exceed it, charge may leak across the plates and the dielectric stops being an insulator. **Electrolytic** capacitors must be connected the correct way round: they have a marking showing which lead goes to the positive terminal. Connecting one the wrong way damages the capacitor and can be dangerous.

Note that capacitors are not the only objects with capacitance: any conductor can be charged, and its capacitance is the ratio of its charge to its potential.

**Worked example:** A capacitor stores a charge of $1.5~\text{C}$ when the p.d. across it is $2500~\text{V}$. Calculate its capacitance in farads and in microfarads.

1. Use $C = \frac{Q}{V}$: $C = \frac{1.5}{2500} = 6.0 \times 10^{-4}~\text{F}$.
2. Convert to microfarads: $6.0 \times 10^{-4}~\text{F} = 6.0 \times 10^{-4} \times 10^6~\mu\text{F} = 600~\mu\text{F}$.

**Answer:** $C = 6.0 \times 10^{-4}~\text{F} = 600~\mu\text{F}$.

**Worked example:** Convert (a) $0.47~\mu\text{F}$ to pF and (b) $2.2~\text{nF}$ to F.

1. (a) $0.47~\mu\text{F} = 0.47 \times 10^{-6}~\text{F} = 4.7 \times 10^{-7}~\text{F} = 4.7 \times 10^5~\text{pF}$.
2. (b) $2.2~\text{nF} = 2.2 \times 10^{-9}~\text{F}$.

**Answer:** (a) $4.7 \times 10^5~\text{pF}$; (b) $2.2 \times 10^{-9}~\text{F}$.

### 1.4 Energy stored in a capacitor (all three formulas, V-Q graph area, $W \propto V^2$)

Charging a capacitor takes work: the supply must push electrons onto one plate and off the other, against the growing repulsion of the electrons already there. At first adding electrons is easy (little repulsion); as the plate charges up, more and more work is needed. This work is stored as electric potential energy, and it is released when the capacitor discharges.

You can see the energy on a graph of p.d. $V$ against charge $Q$. The graph is a **straight line through the origin** (because $Q = VC$), and the energy stored is the **area under the graph**. The area is a triangle, so:

$$W = \frac{1}{2}QV$$

- $W$ is the energy stored, in joules (J).
- $Q$ is the charge stored on each plate, in coulombs (C).
- $V$ is the p.d. between the plates, in volts (V).

Substituting $Q = CV$ gives two more forms, all three of which are the same equation:

$$W = \frac{1}{2}CV^2 \qquad \text{and} \qquad W = \frac{Q^2}{2C}$$

- In $W = \frac{1}{2}CV^2$: $C$ in farads, $V$ in volts, $W$ in joules. Use this when you know capacitance and p.d. (the most common case).
- In $W = \frac{Q^2}{2C}$: $Q$ in coulombs, $C$ in farads, $W$ in joules. Use this when you know charge and capacitance.

Because $W = \frac{1}{2}CV^2$, the energy stored is **proportional to the square of the p.d.** ($W \propto V^2$): doubling the charging voltage stores **four times** as much energy. The same applies to charge: $W \propto Q^2$, so halving the charge quarters the energy. Stored energy is small: a $2000~\mu\text{F}$ capacitor at $10~\text{V}$ stores only $0.10~\text{J}$, compared with the roughly $10\,000~\text{J}$ in a rechargeable battery.

**Worked example:** A $2000~\mu\text{F}$ capacitor is charged to a p.d. of $10~\text{V}$. Calculate the energy stored.

1. Convert the capacitance: $C = 2000~\mu\text{F} = 2.0 \times 10^{-3}~\text{F}$.
2. Use $W = \frac{1}{2}CV^2$: $W = \frac{1}{2} \times 2.0 \times 10^{-3} \times 10^2 = 0.10~\text{J}$.

**Answer:** $W = 0.10~\text{J}$.

**Worked example:** A capacitor stores $2.0~\text{mC}$ of charge when the p.d. across it is $60~\text{V}$. Calculate the energy stored.

1. Convert the charge: $Q = 2.0~\text{mC} = 2.0 \times 10^{-3}~\text{C}$.
2. Use $W = \frac{1}{2}QV$: $W = \frac{1}{2} \times 2.0 \times 10^{-3} \times 60 = 0.060~\text{J}$.

**Answer:** $W = 0.060~\text{J} = 60~\text{mJ}$.

### 1.5 Capacitors in parallel (formula + derivation)

Two capacitors connected in parallel behave like one capacitor with **larger plates**: the bigger the plates, the more charge stored for a given voltage, so the capacitances simply add:

$$C_{\text{total}} = C_1 + C_2 + C_3 + \dots$$

- $C_{\text{total}}$ is the combined capacitance, in farads (F).
- $C_1$, $C_2$, $C_3$, ... are the individual capacitances, in farads (F).

The rules for capacitors in parallel: the p.d. across each capacitor is the **same** (each is connected straight across the supply), and the total charge is the sum of the individual charges.

**Derivation:** each capacitor has the same p.d. $V$ across it, so $Q_1 = C_1 V$ and $Q_2 = C_2 V$. The total charge is:

$$Q = Q_1 + Q_2 = C_1 V + C_2 V = (C_1 + C_2)V$$

Comparing with $Q = C_{\text{total}}V$ gives $C_{\text{total}} = C_1 + C_2$, and the rule extends to any number of capacitors.

**Worked example:** Two $100~\mu\text{F}$ capacitors are connected in parallel and charged to a p.d. of $20~\text{V}$. Calculate (a) the total capacitance and (b) the total charge stored.

1. (a) Add the capacitances: $C_{\text{total}} = 100 + 100 = 200~\mu\text{F} = 2.0 \times 10^{-4}~\text{F}$.
2. (b) Use $Q = C_{\text{total}}V$: $Q = 2.0 \times 10^{-4} \times 20 = 4.0 \times 10^{-3}~\text{C}$.

**Answer:** (a) $C_{\text{total}} = 200~\mu\text{F}$; (b) $Q = 4.0 \times 10^{-3}~\text{C} = 4.0~\text{mC}$.

**Worked example:** A $4.7~\mu\text{F}$ capacitor and a $10~\mu\text{F}$ capacitor are connected in parallel across a $6.0~\text{V}$ supply. Calculate (a) the total capacitance, (b) the charge on each capacitor, and (c) the total charge stored.

1. (a) $C_{\text{total}} = 4.7 + 10 = 14.7~\mu\text{F}$.
2. (b) Each capacitor sees the full $6.0~\text{V}$: $Q_1 = 4.7 \times 10^{-6} \times 6.0 = 2.8 \times 10^{-5}~\text{C}$ and $Q_2 = 10 \times 10^{-6} \times 6.0 = 6.0 \times 10^{-5}~\text{C}$.
3. (c) $Q = Q_1 + Q_2 = 8.8 \times 10^{-5}~\text{C}$ (equivalently $Q = C_{\text{total}}V = 14.7 \times 10^{-6} \times 6.0 = 8.8 \times 10^{-5}~\text{C}$).

**Answer:** (a) $14.7~\mu\text{F}$; (b) $2.8 \times 10^{-5}~\text{C}$ and $6.0 \times 10^{-5}~\text{C}$; (c) $8.8 \times 10^{-5}~\text{C}$.

### 1.6 Capacitors in series (formula + derivation, conservation of charge argument)

For capacitors in series it is the **reciprocals** that add:

$$\frac{1}{C_{\text{total}}} = \frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3} + \dots$$

- $C_{\text{total}}$ is the combined capacitance, in farads (F).
- $C_1$, $C_2$, $C_3$, ... are the individual capacitances, in farads (F).

**Why each capacitor stores the same charge:** when the voltage is applied, charge $-Q$ arrives on the left-hand plate of $C_1$ and repels charge $-Q$ off its right-hand plate, leaving $+Q$ there. That charge $-Q$ arrives on the left-hand plate of $C_2$, which in turn pushes $-Q$ off its right-hand plate. Charge is not created or destroyed (conservation of charge). The **central isolated section** between the two capacitors was uncharged to start with, so it must still have zero net charge: it ends up with $-Q$ at one end and $+Q$ at the other. Hence every series capacitor stores the **same** charge $Q$.

**Derivation:** the p.d.s across the capacitors add to the supply p.d., $V = V_1 + V_2$. Since each stores the same charge $Q$:

$$V_1 = \frac{Q}{C_1}, \qquad V_2 = \frac{Q}{C_2}, \qquad V = \frac{Q}{C_{\text{total}}}$$

Substituting into $V = V_1 + V_2$ and cancelling the common factor $Q$:

$$\frac{Q}{C_{\text{total}}} = \frac{Q}{C_1} + \frac{Q}{C_2} \qquad \Rightarrow \qquad \frac{1}{C_{\text{total}}} = \frac{1}{C_1} + \frac{1}{C_2}$$

**Key check:** the total capacitance of capacitors in series is **less than the smallest individual capacitance** (for two equal capacitors it is half of one of them). If your series answer is bigger than any of the individual values, you have made the reciprocal error.

**Worked example:** Calculate the total capacitance of a $300~\mu\text{F}$ capacitor and a $600~\mu\text{F}$ capacitor connected in series.

1. Substitute into the reciprocal formula: $\frac{1}{C_{\text{total}}} = \frac{1}{300} + \frac{1}{600} = 0.005~\mu\text{F}^{-1}$.
2. Take the reciprocal: $C_{\text{total}} = \frac{1}{0.005} = 200~\mu\text{F}$.

**Answer:** $C_{\text{total}} = 200~\mu\text{F}$ (less than either individual capacitance, as expected).

**Worked example:** A $20~\mu\text{F}$ capacitor and a $30~\mu\text{F}$ capacitor are connected in series across a $10~\text{V}$ supply. Calculate (a) the total capacitance, (b) the charge stored, and (c) the p.d. across each capacitor.

1. (a) $\frac{1}{C_{\text{total}}} = \frac{1}{20} + \frac{1}{30} = \frac{5}{60}$, so $C_{\text{total}} = 12~\mu\text{F} = 1.2 \times 10^{-5}~\text{F}$.
2. (b) Each series capacitor stores the same charge: $Q = C_{\text{total}}V = 1.2 \times 10^{-5} \times 10 = 1.2 \times 10^{-4}~\text{C}$.
3. (c) $V_1 = \frac{Q}{C_1} = \frac{1.2 \times 10^{-4}}{2.0 \times 10^{-5}} = 6.0~\text{V}$; $V_2 = \frac{Q}{C_2} = \frac{1.2 \times 10^{-4}}{3.0 \times 10^{-5}} = 4.0~\text{V}$.
4. Check: $V_1 + V_2 = 6.0 + 4.0 = 10~\text{V}$, the supply p.d.

**Answer:** (a) $12~\mu\text{F}$; (b) $1.2 \times 10^{-4}~\text{C}$ on each; (c) $6.0~\text{V}$ and $4.0~\text{V}$.

### 1.7 Capacitor networks (mixed series/parallel)

Real circuits mix series and parallel groups. The method is to solve **in stages**: combine the simplest parallel (or series) group first, replace it with its single equivalent capacitor, then repeat.

- A parallel group is recognised because each capacitor in it has the **same p.d. across it** (their plates are joined together at both ends).
- A series chain is recognised because the same current path passes through each capacitor in turn.

The four possible arrangements of three capacitors are handled as:

- All in series: use the reciprocal formula on all three.
- All in parallel: add all three.
- Two in parallel, then that pair in series with the third: combine the pair first ($C_1 + C_2$), then put that result in series with $C_3$.
- Two in series, then that pair in parallel with the third: combine the pair first (reciprocal formula), then add $C_3$.

**Worked example:** Three capacitors, each of capacitance $100~\mu\text{F}$, are connected in the four arrangements shown in the book (Figure 24.14). Calculate the total capacitance of each arrangement.

1. (a) All in series: $\frac{1}{C} = \frac{1}{100} + \frac{1}{100} + \frac{1}{100} = \frac{3}{100}$, so $C = 33.3~\mu\text{F}$.
2. (b) All in parallel: $C = 100 + 100 + 100 = 300~\mu\text{F}$.
3. (c) Two in parallel ($200~\mu\text{F}$) in series with the third: $\frac{1}{C} = \frac{1}{200} + \frac{1}{100} = \frac{3}{200}$, so $C = 66.7~\mu\text{F}$.
4. (d) Two in series ($50~\mu\text{F}$) in parallel with the third: $C = 50 + 100 = 150~\mu\text{F}$.

**Answer:** (a) $33.3~\mu\text{F}$; (b) $300~\mu\text{F}$; (c) $66.7~\mu\text{F}$; (d) $150~\mu\text{F}$.

**Worked example:** A $10~\mu\text{F}$ capacitor is connected in series with a parallel combination of two $10~\mu\text{F}$ capacitors. Calculate the total capacitance.

1. Combine the parallel pair first: $C_{\text{pair}} = 10 + 10 = 20~\mu\text{F}$.
2. Put the pair in series with the third: $\frac{1}{C} = \frac{1}{20} + \frac{1}{10} = \frac{3}{20}$, so $C = 6.67~\mu\text{F}$.

**Answer:** $C_{\text{total}} = 6.7~\mu\text{F}$ (to 2 significant figures).

### 1.8 Sharing charge and energy (charged capacitor connected to uncharged one; energy loss)

If a charged capacitor $C_1$ is disconnected from its supply and then connected across an uncharged capacitor $C_2$, the two capacitors are now **in parallel** (same p.d. across each). Their combined capacitance is $C_1 + C_2$, and the total charge is conserved: charge simply redistributes between the two capacitors **in proportion to their capacitances** until the p.d.s are equal.

$$Q_{\text{initial}} = C_1 V_0, \qquad C_{\text{total}} = C_1 + C_2, \qquad V_{\text{final}} = \frac{Q_{\text{initial}}}{C_{\text{total}}}$$

- $Q_{\text{initial}}$ is the charge before connecting, in coulombs (C).
- $C_1$, $C_2$ are the capacitances, in farads (F); $C_{\text{total}}$ is their sum.
- $V_{\text{final}}$ is the common p.d. after sharing, in volts (V).

**The surprising result:** charge is conserved, but **energy is not**. When the capacitors are joined, some of the stored energy is dissipated as heat in the connecting wires (and as a spark, if you can see one) while the electrons redistribute. For two **equal** capacitors, exactly **half** the stored energy is lost. This is a classic exam trap: do not assume energy is conserved just because charge is.

**Worked example:** Two $100~\text{mF}$ capacitors. One is charged to $10~\text{V}$, disconnected from the supply, and then connected across the other. Calculate the energy stored by the combination.

1. Initial charge: $Q = VC = 10 \times 0.10 = 1.0~\text{C}$.
2. Initial energy: $W = \frac{1}{2}CV^2 = \frac{1}{2} \times 0.10 \times 10^2 = 5.0~\text{J}$.
3. Combined capacitance: $C_{\text{total}} = 100 + 100 = 200~\text{mF} = 0.20~\text{F}$.
4. Final p.d.: $V = \frac{Q}{C_{\text{total}}} = \frac{1.0}{0.20} = 5.0~\text{V}$.
5. Final total energy: $W = \frac{1}{2}C_{\text{total}}V^2 = \frac{1}{2} \times 0.20 \times 5.0^2 = 2.5~\text{J}$.

**Answer:** the combination stores $2.5~\text{J}$. The charge is still $1.0~\text{C}$ (conserved), but half the stored energy ($2.5~\text{J}$ of the original $5.0~\text{J}$) has been lost as heat in the connecting wires.

**Worked example:** A $20~\mu\text{F}$ capacitor is charged to $200~\text{V}$, disconnected from the supply, and then connected across an uncharged $5.0~\mu\text{F}$ capacitor. Calculate (a) the combined capacitance, (b) the charge stored, (c) the final p.d., and (d) the energy dissipated.

1. (a) $C_{\text{total}} = 20 + 5.0 = 25~\mu\text{F} = 2.5 \times 10^{-5}~\text{F}$.
2. (b) $Q = C_1 V_0 = 20 \times 10^{-6} \times 200 = 4.0 \times 10^{-3}~\text{C}$ (this is conserved).
3. (c) $V = \frac{Q}{C_{\text{total}}} = \frac{4.0 \times 10^{-3}}{2.5 \times 10^{-5}} = 160~\text{V}$.
4. (d) Initial energy: $W_1 = \frac{1}{2}C_1V_0^2 = \frac{1}{2} \times 20 \times 10^{-6} \times 200^2 = 0.40~\text{J}$.
5. Final energy: $W_2 = \frac{1}{2}C_{\text{total}}V^2 = \frac{1}{2} \times 2.5 \times 10^{-5} \times 160^2 = 0.32~\text{J}$.
6. Energy dissipated: $W_1 - W_2 = 0.40 - 0.32 = 0.08~\text{J}$.

**Answer:** (a) $25~\mu\text{F}$; (b) $4.0 \times 10^{-3}~\text{C}$; (c) $160~\text{V}$; (d) $0.08~\text{J}$ dissipated as heat.

### 1.9 Capacitance of isolated bodies (sphere: $C = 4\pi\epsilon_0 r$)

It is not only capacitors that have capacitance: **any** conductor has capacitance. A conducting sphere of radius $r$, insulated from its surroundings and carrying charge $Q$, has a potential at its surface of:

$$V = \frac{Q}{4\pi\epsilon_0 r}$$

- $V$ is the potential at the surface, in volts (V).
- $Q$ is the charge on the sphere, in coulombs (C).
- $r$ is the radius of the sphere, in metres (m).
- $\epsilon_0$ is the permittivity of free space, $8.85 \times 10^{-12}~\text{F m}^{-1}$.

Since $C = \frac{Q}{V}$, the capacitance of the isolated sphere is:

$$C = 4\pi\epsilon_0 r$$

- $C$ is the capacitance, in farads (F) - note $4\pi\epsilon_0$ has units $\text{F m}^{-1}$, so multiplying by the radius in metres gives farads.

The capacitance of a sphere depends only on its radius (and the surrounding medium). A useful quick form: $C = \frac{r}{9.0 \times 10^9}$ because $\frac{1}{4\pi\epsilon_0} = 8.99 \times 10^9 \approx 9.0 \times 10^9~\text{m F}^{-1}$.

**Worked example:** Estimate the capacitance of the Earth, given that its radius is $6.4 \times 10^6~\text{m}$.

1. Use $C = 4\pi\epsilon_0 r$ with $r = 6.4 \times 10^6~\text{m}$.
2. $C = 4\pi \times 8.85 \times 10^{-12} \times 6.4 \times 10^6 = 7.1 \times 10^{-4}~\text{F}$.

**Answer:** $C \approx 7.1 \times 10^{-4}~\text{F}$ (about $710~\mu\text{F}$ - a surprisingly large value for a whole planet).

**Worked example:** The dome of a Van de Graaff generator is a conducting sphere of radius $15~\text{cm}$ charged to a surface potential of $40~\text{kV}$. Calculate (a) the capacitance of the dome and (b) the charge on it.

1. Convert: $r = 15~\text{cm} = 0.15~\text{m}$, $V = 40~\text{kV} = 4.0 \times 10^4~\text{V}$.
2. (a) $C = 4\pi\epsilon_0 r = \frac{0.15}{8.99 \times 10^9} = 1.7 \times 10^{-11}~\text{F} = 17~\text{pF}$.
3. (b) $Q = CV = 1.7 \times 10^{-11} \times 4.0 \times 10^4 = 6.7 \times 10^{-7}~\text{C} = 0.67~\mu\text{C}$.

**Answer:** (a) $C = 1.7 \times 10^{-11}~\text{F} = 17~\text{pF}$; (b) $Q = 6.7 \times 10^{-7}~\text{C} = 0.67~\mu\text{C}$.

### 1.10 Capacitors compared with resistors (the swap table)

The series and parallel formulae for capacitors and resistors **swap**: capacitors in series use the reciprocal formula (like resistors in parallel), and capacitors in parallel simply add (like resistors in series).

| Connection | Capacitors | Resistors |
| --- | --- | --- |
| In series | Same charge on each; $\frac{1}{C_{\text{total}}} = \frac{1}{C_1} + \frac{1}{C_2} + \dots$ | Same current through each; $R_{\text{total}} = R_1 + R_2 + \dots$ |
| In parallel | Same p.d. across each; $C_{\text{total}} = C_1 + C_2 + \dots$ | Same p.d. across each; $\frac{1}{R_{\text{total}}} = \frac{1}{R_1} + \frac{1}{R_2} + \dots$ |

Why the swap? Capacitance measures how **good** a capacitor is at storing charge for a given voltage, while resistance measures how **bad** a resistor is at letting current through for a given voltage. "Good" quantities add in parallel (more area, more charge capacity); "bad" quantities add in series (more obstruction).

**Worked example:** A $12~\mu\text{F}$ capacitor and a $4.0~\mu\text{F}$ capacitor are connected in series. State, without calculating, whether the total capacitance is greater or less than $4.0~\mu\text{F}$, then calculate it.

1. Series capacitance is always less than the smallest individual capacitance, so $C_{\text{total}} < 4.0~\mu\text{F}$.
2. $\frac{1}{C_{\text{total}}} = \frac{1}{12} + \frac{1}{4} = \frac{1}{12} + \frac{3}{12} = \frac{4}{12} = \frac{1}{3}$.
3. Take the reciprocal: $C_{\text{total}} = 3.0~\mu\text{F}$.

**Answer:** $C_{\text{total}} = 3.0~\mu\text{F}$, which is indeed less than $4.0~\mu\text{F}$. (For comparison, two identical resistors $R$ in parallel give $R/2$; two identical capacitors $C$ in series give $C/2$.)

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
