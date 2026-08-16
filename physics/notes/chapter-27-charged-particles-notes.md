# Chapter 27: Charged Particles - CAIE A Level Physics (9702) Study Notes

Exam-focused revision notes for Cambridge International AS & A Level Physics 9702, covering Topic 20 (Magnetic fields) as taught in Chapter 27 of the coursebook. Everything here is what the exam can actually ask, nothing more. All definitions are worded to match mark schemes, and every question type below has appeared in real 9702 papers (mainly Paper 4 structured questions and Paper 1 multiple choice). Every theory section ends with a worked example, so you can see the formula being used the moment it is introduced.

## 1. Theory

### 1.1 The magnetic force on a moving charge: $F = BQv$

A stationary charge feels no magnetic force. A charge only feels a magnetic force when it is **moving** through a magnetic field. The size of the force depends on three things:

- the magnetic flux density $B$ (how strong the field is),
- the charge $Q$ on the particle,
- the speed $v$ of the particle.

For a charge moving **at right angles** to a uniform magnetic field, the force is:

$$F = BQv$$

- $F$ is the magnetic force, in newtons (N).
- $B$ is the magnetic flux density, in tesla (T).
- $Q$ is the charge on the particle, in coulombs (C).
- $v$ is the speed of the particle, in metres per second (m s$^{-1}$).

If the particle moves at an angle $\theta$ to the field, only the component of velocity perpendicular to the field matters, so the general form is:

$$F = BQv\sin\theta$$

For an electron, whose charge has magnitude $e = 1.60 \times 10^{-19}~\text{C}$, the force is $F = Bev$ (sometimes called the "$Bev$ force"). This is the same force that acts on the moving electrons inside a current-carrying wire, which is why a wire in a magnetic field experiences $F = BIL$ (Chapter 26). You can show the two equations are consistent: a charge $Q$ flowing past a point in time $t$ gives $I = \frac{Q}{t}$, so $F = BIL = B\left(\frac{Q}{t}\right)L = BQ\left(\frac{L}{t}\right) = BQv$, since $\frac{L}{t}$ is just the speed $v$.

**Worked example:** A beam of electrons moving at $1.0 \times 10^6~\text{m s}^{-1}$ is directed through a magnetic field of flux density $0.50~\text{T}$. Calculate the force on each electron when (a) the beam is at right angles to the field, and (b) the beam is at an angle of $45^{\circ}$ to the field.

1. (a) The beam is perpendicular to the field, so use $F = Bev$ directly: $F = 1.60 \times 10^{-19} \times 1.0 \times 10^6 \times 0.50$.
2. $F = 8.0 \times 10^{-14}~\text{N}$.
3. (b) At $45^{\circ}$, use the component of velocity perpendicular to the field: $F = Bev\sin 45^{\circ}$.
4. $F = 1.60 \times 10^{-19} \times 1.0 \times 10^6 \times 0.50 \times 0.707 = 5.7 \times 10^{-14}~\text{N}$.

**Answer:** (a) $F = 8.0 \times 10^{-14}~\text{N}$; (b) $F = 5.7 \times 10^{-14}~\text{N}$.

### 1.2 Direction of the force: Fleming's left-hand rule

The direction of the magnetic force on a moving charge is found with **Fleming's left-hand rule**. Hold the thumb, first finger and second finger of your LEFT hand at right angles to each other:

- **First finger** points in the direction of the **field** $B$,
- **Second finger** points in the direction of the **conventional current**,
- **Thumb** points in the direction of the **force** $F$ (the direction the charge is pushed).

The crucial detail is that the rule uses **conventional current**, the direction of flow of *positive* charge. Electrons are negative, so when electrons move one way, the conventional current flows the **opposite** way. An electron moving from right to left represents a conventional current from left to right, and that is the direction you put your second finger.

The force $F$ is always at $90^{\circ}$ to the velocity of the particle and at $90^{\circ}$ to the field. It never has a component along the velocity, and this fact controls everything else in the chapter (see Section 1.3).

An alternative for a positive charge is the **right-hand palm rule**: fingers along the velocity $v$, palm facing the field $B$, thumb along the force. For electrons use the left hand, or reverse the answer you get for a positive charge - flipping the positive-charge answer is the safest habit.

**Worked example:** A mixed beam containing positrons (charge $+e$) and electrons (charge $-e$) enters a uniform magnetic field directed into the plane of the paper, both moving from left to right. Use Fleming's left-hand rule to determine the direction of the force on each particle.

1. Positron: the positron is positive, so the conventional current is in the same direction as its motion, from left to right.
2. Left hand: first finger into the page (field), second finger to the right (current). The thumb points up the page, so the positron is deflected **upwards**.
3. Electron: the electron is negative, so the conventional current flows from right to left, opposite to its motion.
4. Left hand: first finger into the page (field), second finger to the left (current). The thumb points down the page, so the electron is deflected **downwards**.

**Answer:** The positron curves upwards and the electron curves downwards, so the two types of particle separate into two beams curving in opposite directions.

### 1.3 Circular motion in a uniform magnetic field

Because the magnetic force is always perpendicular to the velocity, a charged particle entering a uniform magnetic field at right angles to the field follows a **circular path**: the force $BQv$ points towards the centre of the circle, acting as the **centripetal force**:

$$\frac{mv^2}{r} = BQv$$

Cancelling one factor of $v$ and rearranging gives the radius of the orbit:

$$r = \frac{mv}{BQ}$$

- $r$ is the radius of the circular path, in metres (m).
- $m$ is the mass of the particle, in kilograms (kg).
- $v$ is its speed, in m s$^{-1}$.
- $B$ is the magnetic flux density, in tesla (T).
- $Q$ is the charge on the particle, in coulombs (C).

For an electron this is $r = \frac{m_ev}{Be}$. Multiplying both sides by $BQ$ gives the momentum form, which is how the radius is often written on the data sheet:

$$p = BQr$$

The equation $r = \frac{mv}{BQ}$ tells you three useful trends:

- faster particles move in **bigger** circles ($r \propto v$),
- heavier particles move in **bigger** circles ($r \propto m$: more inertia, harder to bend),
- a stronger field makes **tighter** circles ($r \propto \frac{1}{B}$).

**Why the kinetic energy stays constant:** the magnetic force is always at right angles to the velocity, so the work done is $W = Fs\cos 90^{\circ} = 0$. No work, no change in kinetic energy: the field changes only the **direction** of the velocity, never its magnitude. (The only thing that slows a real electron in a fine-beam tube is collisions with gas molecules, not the field.)

**Worked example:** An electron is travelling at right angles to a uniform magnetic field of flux density $1.2~\text{mT}$. The speed of the electron is $8.0 \times 10^6~\text{m s}^{-1}$. Calculate the radius of the circle described by the electron. (Electron charge $e = 1.60 \times 10^{-19}~\text{C}$, electron mass $m_e = 9.11 \times 10^{-31}~\text{kg}$.)

1. Convert the flux density: $B = 1.2~\text{mT} = 1.2 \times 10^{-3}~\text{T}$.
2. The magnetic force is the centripetal force: $F = Bev = 1.60 \times 10^{-19} \times 1.2 \times 10^{-3} \times 8.0 \times 10^6 = 1.536 \times 10^{-15}~\text{N}$.
3. Use $\frac{mv^2}{r} = F$ rearranged, or go straight to $r = \frac{mv}{Be}$.
4. $r = \frac{9.11 \times 10^{-31} \times 8.0 \times 10^6}{1.60 \times 10^{-19} \times 1.2 \times 10^{-3}} = \frac{7.29 \times 10^{-24}}{1.92 \times 10^{-22}}$.

**Answer:** $r = 3.8 \times 10^{-2}~\text{m} = 3.8~\text{cm}$.

**Worked example:** In a fine-beam tube, electrons travel in a circular orbit of radius $5.0~\text{cm}$ in a uniform magnetic field of flux density $2.0~\text{mT}$. Calculate the speed of the electrons. (Charge-to-mass ratio of the electron $\frac{e}{m_e} = 1.76 \times 10^{11}~\text{C kg}^{-1}$.)

1. Convert: $r = 5.0~\text{cm} = 5.0 \times 10^{-2}~\text{m}$; $B = 2.0~\text{mT} = 2.0 \times 10^{-3}~\text{T}$.
2. Rearrange $r = \frac{mv}{Be}$ to make $v$ the subject: $v = \frac{Ber}{m} = \left(\frac{e}{m}\right)Br$.
3. $v = 1.76 \times 10^{11} \times 2.0 \times 10^{-3} \times 5.0 \times 10^{-2} = 1.76 \times 10^7~\text{m s}^{-1}$.

**Answer:** $v = 1.76 \times 10^7~\text{m s}^{-1}$.

### 1.4 Deflection of beams in electric and magnetic fields

An electron beam tube (Figure 27.4 in the coursebook) contains an **electron gun** - a heated cathode that emits electrons, and a positively charged anode that attracts them, so the electrons accelerate through the anode and emerge as a narrow beam. The beam can then be deflected by an **electric field** between two parallel plates, or by a **magnetic field** from coils, and the spot it makes on a fluorescent screen shows where it lands.

The two types of deflection behave differently, and examiners love asking for the differences:

| | Electric field | Magnetic field |
| --- | --- | --- |
| Force on a charge | $F = EQ$ | $F = BQv$ |
| Depends on the speed of the particle? | No - same force whatever the speed | Yes - proportional to $v$ |
| Acts on a stationary charge? | Yes | No, only on moving charges |
| Does work on the particle? | Yes - can change its speed and kinetic energy | No - force is perpendicular to velocity, so speed is unchanged |
| Direction of force | Along or opposite to the field lines | Perpendicular to both $B$ and $v$ |
| Path of the beam | Parabolic curve (constant sideways acceleration while between the plates) | Arc of a circle (force always perpendicular to velocity) |

In a uniform electric field the force $EQ$ is constant, so the sideways acceleration $a = \frac{EQ}{m}$ is constant and the beam follows a parabola between the plates; in a magnetic field the force stays perpendicular to the velocity, so the beam follows a circular arc inside the field and a straight line outside it. Faster electrons spend less time between the plates, so they are deflected **less** by an electric field; in a magnetic field the radius $r = \frac{mv}{BQ}$ grows with speed, so faster electrons are also bent less.

The gravitational force on an electron ($mg \approx 10^{-30}~\text{N}$) is negligible against electric and magnetic forces of order $10^{-15}~\text{N}$, so exam answers never mention gravity on electron beams.

**Worked example:** An electron is moving between two parallel plates that produce a uniform electric field of strength $2.0 \times 10^4~\text{V m}^{-1}$. (a) Calculate the force on the electron and (b) its acceleration. (c) Show that the gravitational force on the electron is negligible by comparison.

1. (a) $F = EQ = 2.0 \times 10^4 \times 1.60 \times 10^{-19} = 3.2 \times 10^{-15}~\text{N}$.
2. (b) $a = \frac{F}{m} = \frac{3.2 \times 10^{-15}}{9.11 \times 10^{-31}} = 3.5 \times 10^{15}~\text{m s}^{-2}$.
3. (c) $mg = 9.11 \times 10^{-31} \times 9.81 = 8.9 \times 10^{-30}~\text{N}$, which is about $3.6 \times 10^{14}$ times smaller than the electric force.

**Answer:** (a) $F = 3.2 \times 10^{-15}~\text{N}$; (b) $a = 3.5 \times 10^{15}~\text{m s}^{-2}$; (c) $mg = 8.9 \times 10^{-30}~\text{N}$, negligible.

### 1.5 Crossed fields and the velocity selector

If electric and magnetic fields are applied **at right angles to each other** in the same region, their forces on a moving charge act in opposite directions. For one particular speed they exactly balance and the particle passes **undeflected**. This is the idea behind the **velocity selector**, used in mass spectrometers to produce a beam of particles all moving at the same speed.

The electric force on a particle of charge $q$ is $Eq$; the magnetic force is $Bqv$. Balancing them:

$$Eq = Bqv \qquad \Rightarrow \qquad v = \frac{E}{B}$$

- $v$ is the speed of the undeflected particle, in m s$^{-1}$.
- $E$ is the electric field strength, in V m$^{-1}$ (or N C$^{-1}$ - the units are the same).
- $B$ is the magnetic flux density, in tesla (T).

Key points about how the selector works:

- The electric force $Eq$ is the **same** for every particle, whatever its speed. The magnetic force $Bqv$ is **bigger** for faster particles.
- A particle moving at exactly $v = \frac{E}{B}$ has equal and opposite forces and passes straight through the slit.
- A particle moving **faster** than $\frac{E}{B}$ has a magnetic force that wins, and it is deflected to one side of the slit.
- A particle moving **slower** than $\frac{E}{B}$ has an electric force that wins, and it is deflected to the other side.
- The selected speed does not depend on the particle's charge or mass (both forces are proportional to $q$, which cancels), though the sign of the charge decides *which way* a wrong-speed particle is deflected.
- If the plates are separated by distance $d$ with p.d. $V$ between them, then $E = \frac{V}{d}$ and the undeflected speed is $v = \frac{V}{Bd}$.

Gravity is always ignored here: the weight $mg$ of an ion is far smaller than $Eq$ and $Bqv$.

**Worked example:** In a velocity selector, the magnetic flux density is $0.30~\text{T}$ and the electric field strength is $1.5 \times 10^3~\text{V m}^{-1}$. Calculate the speed of an ion that emerges undeflected from the slit.

1. Use $v = \frac{E}{B}$.
2. $v = \frac{1.5 \times 10^3}{0.30} = 5.0 \times 10^3~\text{m s}^{-1}$.

**Answer:** $v = 5.0 \times 10^3~\text{m s}^{-1}$. Ions travelling faster than this are deflected by the magnetic force (which is larger than the electric force for them) and do not reach the slit.

**Worked example:** The plates of a velocity selector are separated by $2.0~\text{cm}$ with a p.d. of $250~\text{V}$ between them. The magnetic flux density is $12~\text{mT}$. Calculate the speed of the particles that pass undeflected.

1. Convert: $d = 2.0~\text{cm} = 2.0 \times 10^{-2}~\text{m}$; $B = 12~\text{mT} = 12 \times 10^{-3}~\text{T}$.
2. Electric field strength: $E = \frac{V}{d} = \frac{250}{2.0 \times 10^{-2}} = 1.25 \times 10^4~\text{V m}^{-1}$.
3. $v = \frac{E}{B} = \frac{1.25 \times 10^4}{12 \times 10^{-3}} = 1.04 \times 10^6~\text{m s}^{-1}$.

**Answer:** $v \approx 1.0 \times 10^6~\text{m s}^{-1}$.

### 1.6 Measuring the speed and charge-to-mass ratio of electrons

In 1897 J.J. Thomson used a deflection tube (the same design as Figure 27.4) to discover the electron and measure its **charge-to-mass ratio** $\frac{e}{m_e}$, also called the **specific charge** of the electron ("specific" means "per unit mass"). He could not measure $e$ or $m_e$ separately, but his ratio, combined with Millikan's later measurement of $e$, gave the electron mass.

**Step 1 - give the electrons a known speed.** Each electron is accelerated from the cathode to the anode through an accelerating p.d. $V_{ca}$. The work done on the electron, $eV_{ca}$, becomes its kinetic energy:

$$eV_{ca} = \frac{1}{2}m_ev^2$$

**Step 2 - measure the orbit radius.** The electrons then pass at right angles through a uniform magnetic field $B$ (in the fine-beam tube or deflection tube) and follow a circle of radius $r$:

$$r = \frac{mv}{Be}$$

**Step 3 - eliminate $v$.** Combining the two equations gives:

$$\frac{e}{m_e} = \frac{2V_{ca}}{B^2r^2}$$

or equivalently $\frac{e}{m_e} = \frac{v}{Br}$. So measuring $V_{ca}$, $B$ and $r$ gives the ratio directly. The difficulties are measuring $B$ accurately and measuring $r$ without parallax error (you cannot put a ruler inside the evacuated tube). The accepted value is:

$$\frac{e}{m_e} = 1.76 \times 10^{11}~\text{C kg}^{-1}$$

**Thomson's observations and what they proved:**

- The beam was deflected towards the positive plate and away from the negative plate, so the particles carry **negative** charge.
- Deflected, the beam stayed a **tight single beam** rather than spreading out, showing all the particles have the same mass, charge and speed (lighter or more highly charged particles would be deflected more; faster ones less).
- Balancing the electric and magnetic fields so the beam stayed straight let him calculate $\frac{e}{m_e}$.
- The ratio was enormous compared with any ion's, so the particles must be far lighter than atoms: they were electrons.

**Measuring the electron mass.** Millikan's oil-drop experiment showed that every charge on his droplets was an integer multiple of a single value $e = 1.60 \times 10^{-19}~\text{C}$. Combining this with Thomson's ratio:

$$m_e = \frac{e}{e/m_e}$$

**Worked example:** In an experiment to measure the charge-to-mass ratio of the electron, electrons are accelerated through a p.d. of $800~\text{V}$ and then travel at right angles to a magnetic field of flux density $1.2~\text{mT}$, following a circular path of radius $8.0~\text{cm}$. Calculate $\frac{e}{m_e}$.

1. Convert: $r = 8.0~\text{cm} = 8.0 \times 10^{-2}~\text{m}$; $B = 1.2~\text{mT} = 1.2 \times 10^{-3}~\text{T}$.
2. Use $\frac{e}{m_e} = \frac{2V_{ca}}{B^2r^2}$.
3. $\frac{e}{m_e} = \frac{2 \times 800}{(1.2 \times 10^{-3})^2 \times (8.0 \times 10^{-2})^2} = \frac{1600}{1.44 \times 10^{-6} \times 6.4 \times 10^{-3}}$.
4. $\frac{e}{m_e} = \frac{1600}{9.22 \times 10^{-9}} = 1.74 \times 10^{11}~\text{C kg}^{-1}$.

**Answer:** $\frac{e}{m_e} = 1.7 \times 10^{11}~\text{C kg}^{-1}$, consistent with the accepted value $1.76 \times 10^{11}~\text{C kg}^{-1}$.

**Worked example:** The charge on an electron is $1.60 \times 10^{-19}~\text{C}$ and the charge-to-mass ratio is $1.76 \times 10^{11}~\text{C kg}^{-1}$. Calculate the mass of an electron.

1. Rearrange $\frac{e}{m_e} = 1.76 \times 10^{11}$ to give $m_e = \frac{e}{e/m_e}$.
2. $m_e = \frac{1.60 \times 10^{-19}}{1.76 \times 10^{11}} = 9.09 \times 10^{-31}~\text{kg}$.

**Answer:** $m_e = 9.1 \times 10^{-31}~\text{kg}$.

### 1.7 The Hall effect

If a strip of conducting material carries a current in a magnetic field at right angles to the current, the moving charge carriers are pushed sideways by the magnetic force. In a metal the carriers are electrons: they accumulate on one side of the strip, leaving the other side short of electrons (effectively positive). This charge separation is the **Hall effect**, and the p.d. between the two sides is the **Hall voltage** $V_H$.

The Hall voltage stops growing once the separated charges set up an electric field strong enough to hold the carriers in equilibrium, where the electric force balances the magnetic force:

$$qE = Bqv$$

where $q$ is the charge on a carrier. The electric field between the sides is $E = \frac{V_H}{d}$, where $d$ is the **width** of the strip (the distance between the two sides). So:

$$\frac{qV_H}{d} = Bqv \qquad \Rightarrow \qquad V_H = Bvd$$

From Chapter 9, the current is related to the mean drift velocity of the carriers by $I = nAqv$, where $A$ is the cross-sectional area and $n$ is the **number density** of charge carriers (number per unit volume). The area of the side face is $A = d \times t$, where $t$ is the **thickness** of the strip. Substituting $v = \frac{I}{nAq}$ into $V_H = Bvd$:

$$V_H = \frac{BI}{ntq}$$

- $V_H$ is the Hall voltage, in volts (V).
- $B$ is the magnetic flux density, in tesla (T).
- $I$ is the current through the strip, in amperes (A).
- $n$ is the number density of charge carriers, in m$^{-3}$.
- $t$ is the thickness of the strip, in metres (m).
- $q$ is the charge on one charge carrier, in coulombs (C).

Two things to notice:

1. $V_H$ is **directly proportional to $B$** - that is what makes the Hall effect so useful for measuring field strength (Section 1.8).
2. The width $d$ cancels: the Hall voltage does **not** depend on how wide the strip is. It depends on the **thickness** $t$, so the strip is made thin to get a bigger voltage.

The direction of the sideways push reveals the sign of the charge carriers: positive carriers deflect one way, negative the other, so the sign of $V_H$ shows whether the current is carried by electrons or positive "holes". The voltage is largest when $n$ is small, which is exactly why semiconductors (far fewer free carriers than metals) are used for Hall probes.

**Worked example:** A Hall probe is designed to operate with a steady current of $0.020~\text{A}$ flowing through a semiconductor slice of thickness $0.05~\text{mm}$. The number density of electrons in the semiconductor is $1.5 \times 10^{23}~\text{m}^{-3}$. Determine the Hall voltage when the probe is placed in a magnetic field of flux density $0.10~\text{T}$. (Electron charge $= 1.60 \times 10^{-19}~\text{C}$.)

1. Convert the thickness: $t = 0.05~\text{mm} = 5.0 \times 10^{-5}~\text{m}$.
2. Use $V_H = \frac{BI}{nte}$.
3. $V_H = \frac{0.10 \times 0.020}{1.5 \times 10^{23} \times 5.0 \times 10^{-5} \times 1.60 \times 10^{-19}}$.
4. Denominator: $1.5 \times 10^{23} \times 5.0 \times 10^{-5} \times 1.60 \times 10^{-19} = 1.2$.
5. $V_H = \frac{2.0 \times 10^{-3}}{1.2} = 1.67 \times 10^{-3}~\text{V}$.

**Answer:** $V_H = 1.7 \times 10^{-3}~\text{V} = 1.7~\text{mV}$.

**Worked example:** In a metal strip the free electrons drift at $3.5 \times 10^{-4}~\text{m s}^{-1}$. The strip is in a magnetic field of flux density $0.40~\text{T}$ and its width (between the faces across which the Hall voltage is measured) is $4.0~\text{mm}$. Calculate the Hall voltage.

1. Convert the width: $d = 4.0~\text{mm} = 4.0 \times 10^{-3}~\text{m}$.
2. Use the equilibrium form $V_H = Bvd$ (derived from $qE = Bqv$).
3. $V_H = 0.40 \times 3.5 \times 10^{-4} \times 4.0 \times 10^{-3} = 5.6 \times 10^{-7}~\text{V}$.

**Answer:** $V_H = 5.6 \times 10^{-7}~\text{V} = 0.56~\mu\text{V}$.

### 1.8 The Hall probe and measuring magnetic flux density

A **Hall probe** measures magnetic flux density. It is a thin slice of semiconductor carrying a steady current, with a control box that supplies the current, amplifies the Hall voltage and displays it on a meter.

Since $V_H = \frac{BI}{ntq}$, keeping $I$ fixed means $V_H \propto B$: the probe is calibrated in fields of known flux density and the meter reads $B$ directly. This is why the current must be **constant** - if $I$ drifted, the same field would give a different voltage and the reading would be wrong. The probe measures the field at the exact point where the slice sits, including narrow gaps such as between magnet poles, where a search coil cannot reach.

Design choices that make the voltage big enough to measure:

- **Semiconductor rather than metal:** the number density $n$ is far smaller in a semiconductor (roughly a million times) and $V_H$ is inversely proportional to $n$; for the same current the electrons also drift much faster, giving a bigger sideways force.
- **Thin slice:** $V_H$ is inversely proportional to the thickness $t$, so the slice is made very thin (fractions of a millimetre).

Direction sensitivity: the force on the carriers depends on the component of $B$ **perpendicular to the plane of the slice**. If the field makes an angle $\theta$ with the normal to the slice, then $V_H = V_{\text{max}}\cos\theta$. Rotating the probe changes $\theta$, so $V_H$ sweeps from a maximum positive value to a maximum negative value (the sign reverses as the perpendicular component reverses). To measure a field, orient the slice perpendicular to $B$; to find the direction of an unknown field, rotate the probe until the reading is a maximum.

**Worked example:** A Hall probe carries a current of $20~\text{mA}$ through a semiconductor slice of thickness $0.05~\text{mm}$. The number density of charge carriers is $1.5 \times 10^{23}~\text{m}^{-3}$. Placed in an unknown magnetic field, the Hall voltage is $3.4~\text{mV}$. Calculate the magnetic flux density.

1. Convert: $I = 20~\text{mA} = 0.020~\text{A}$; $V_H = 3.4~\text{mV} = 3.4 \times 10^{-3}~\text{V}$; $t = 5.0 \times 10^{-5}~\text{m}$.
2. Rearrange $V_H = \frac{BI}{ntq}$ to give $B = \frac{V_H ntq}{I}$.
3. $B = \frac{3.4 \times 10^{-3} \times 1.5 \times 10^{23} \times 5.0 \times 10^{-5} \times 1.60 \times 10^{-19}}{0.020}$.
4. Numerator: $3.4 \times 10^{-3} \times 1.2 = 4.08 \times 10^{-3}$.
5. $B = \frac{4.08 \times 10^{-3}}{0.020} = 0.204~\text{T}$.

**Answer:** $B = 0.20~\text{T}$.

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
