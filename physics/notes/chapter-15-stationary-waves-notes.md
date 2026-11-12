# Chapter 15: Stationary Waves - CAIE A Level Physics (9702) Study Notes

Exam-focused revision notes for Cambridge International AS & A Level Physics 9702, covering Chapter 15: the formation of stationary (standing) waves, nodes and antinodes, boundary conditions, harmonics on strings and in air columns, end correction, resonance, and methods of measuring wavelength and the speed of sound. This is a frequent Paper 2 and Paper 4 topic, often combined with Chapter 13 (waves) and examined practically in Paper 3. Definitions are worded for mark schemes, and every section ends with a worked example. Use $v = f\lambda$ throughout, with the speed of sound in air taken as $330~\text{m s}^{-1}$ unless the question states otherwise.

## 1. Theory

### 1.1 Formation of a stationary wave

A **stationary wave** (standing wave) is formed when **two progressive waves of the same frequency and (ideally) the same amplitude travel in opposite directions and superpose**.

In practice this happens when a progressive wave is **reflected** and the incident and reflected waves overlap. Examples:

- A string fixed at both ends: waves travel along the string, reflect at the ends, and the two travelling waves superpose.
- A microwave transmitter facing a metal plate: the incident and reflected microwaves form a stationary wave in the space between.
- A loudspeaker facing a hard board: the incident and reflected sound waves form a stationary wave.
- An air column in a tube: the wave reflects at the closed end (or at the open end, partially) and superposes with the incident wave.

**Why the pattern is stationary:** at a **node**, the two waves always arrive in **antiphase** and cancel, so the displacement is always zero. At an **antinode**, they always arrive **in phase** and add, so the amplitude is maximum. The positions of nodes and antinodes do not move, even though each particle oscillates.

**The superposition picture:** at $t = 0$ the two travelling waves may be in phase, giving a resultant amplitude of $2A$. A quarter of a period later each wave has moved a quarter of a wavelength in opposite directions, so they are in antiphase and the resultant is zero. Half a period later they are in phase again. The resultant profile therefore oscillates in place rather than travelling.

**Worked example:** Explain why a stationary wave is formed on a guitar string when it is plucked.

1. Plucking sends progressive waves along the string in both directions.
2. The waves reflect at the fixed ends, so two identical waves travel in opposite directions.
3. They superpose; at the fixed ends the displacement must be zero (nodes), and the superposition produces a stationary pattern of nodes and antinodes.

**Answer:** incident and reflected waves of the same frequency and amplitude travel in opposite directions and superpose.

### 1.2 Nodes, antinodes and wavelength

- **Node (N):** a point of **zero amplitude**; the medium does not move there.
- **Antinode (A):** a point of **maximum amplitude**.

The distances are fixed by the wavelength of the progressive waves that form the pattern:

$$\text{separation between adjacent nodes} = \frac{\lambda}{2}$$

$$\text{separation between adjacent antinodes} = \frac{\lambda}{2}$$

$$\text{separation between a node and the adjacent antinode} = \frac{\lambda}{4}$$

So if you measure the distance between adjacent nodes, the wavelength is **twice** that distance. This is the standard way to find $\lambda$ from a stationary-wave pattern.

**Worked example:** Adjacent nodes on a vibrating string are $25~\text{cm}$ apart. Calculate the wavelength and the distance from a node to the adjacent antinode.

1. $\frac{\lambda}{2} = 25~\text{cm}$, so $\lambda = 50~\text{cm}$.
2. Node-to-antinode $= \frac{\lambda}{4} = 12.5~\text{cm}$.

**Answer:** $\lambda = 0.50~\text{m}$; node-to-antinode $= 0.125~\text{m}$.

### 1.3 Phase relationships in a stationary wave

All points on a stationary wave oscillate at the **same frequency**, but their amplitudes and phases differ:

- Points **between two adjacent nodes** (within one loop) oscillate **in phase** with each other.
- Points in **adjacent loops** (on opposite sides of a node) oscillate **in antiphase** ($180^\circ$ out of phase).
- A node has zero amplitude, so its phase is undefined in practice.
- All points reach their maximum displacement at the same instant (though some have zero displacement at that instant if they are at a node).

This is different from a progressive wave, where the phase changes continuously with distance.

**Worked example:** Two points on a stationary wave are in adjacent loops. State their phase difference.

1. Adjacent loops are separated by a node.
2. On opposite sides of a node, the displacements are always opposite.

**Answer:** $180^\circ$ (antiphase).

### 1.4 Boundary conditions

The ends of the vibrating system determine where nodes and antinodes must be:

| Boundary | Condition | Reason |
|---|---|---|
| Fixed end of a string | **Node** | The end cannot move |
| Free end of a string (ideal) | **Antinode** | The end is free to move with maximum amplitude |
| Closed end of a pipe | **Node** (displacement) | Air cannot move through the solid end; pressure is maximum (pressure antinode) |
| Open end of a pipe | **Antinode** (displacement) | Air is free to move; pressure is approximately atmospheric (pressure node) |

**Important subtlety for sound:** the diagrams usually show **displacement** nodes and antinodes. At a closed end the air cannot move, so it is a displacement node but a **pressure antinode**; at an open end the air moves freely, so it is a displacement antinode but a **pressure node**. Exam questions normally mean displacement unless they say "pressure".

**End correction:** in reality the displacement antinode at an open end lies slightly **outside** the tube, at a distance $c$ beyond the end. This is the **end correction**, typically about $0.3$ times the tube diameter for a closed pipe.

### 1.5 Stationary waves on a stretched string

A string fixed at **both ends** must have a node at each end. The possible patterns are:

| Mode | Number of loops | Length–wavelength relation | Frequency |
|---|---|---|---|
| Fundamental (1st harmonic) | 1 | $l = \frac{\lambda}{2}$, so $\lambda = 2l$ | $f_0 = \frac{v}{2l}$ |
| 2nd harmonic | 2 | $l = \lambda$, so $\lambda = l$ | $f_2 = 2f_0$ |
| 3rd harmonic | 3 | $l = \frac{3\lambda}{2}$, so $\lambda = \frac{2l}{3}$ | $f_3 = 3f_0$ |
| $n$th harmonic | $n$ | $l = \frac{n\lambda}{2}$, so $\lambda = \frac{2l}{n}$ | $f_n = nf_0$ |

In general, for a string of length $l$ fixed at both ends:

$$f_n = \frac{nv}{2l}, \qquad n = 1, 2, 3, \dots$$

All integer multiples of the fundamental are present: the string has **all** harmonics.

The wave speed on a string depends on the tension and the mass per unit length (not required quantitatively in 9702, but useful for explanation): increasing the tension increases $v$, and hence increases every resonant frequency; a thicker (heavier) string has a lower $v$ and lower frequencies.

**Worked example:** A guitar string of length $64~\text{cm}$ vibrates in its fundamental mode. The wave speed on the string is $320~\text{m s}^{-1}$. Calculate the fundamental frequency and the frequency of the second harmonic.

1. Fundamental: $\lambda = 2l = 2 \times 0.64 = 1.28~\text{m}$.
2. $f_0 = \frac{v}{\lambda} = \frac{320}{1.28} = 250~\text{Hz}$.
3. Second harmonic: $f_2 = 2f_0 = 500~\text{Hz}$.

**Answer:** $f_0 = 250~\text{Hz}$; second harmonic $= 500~\text{Hz}$.

**Worked example:** A string of length $1.20~\text{m}$ is fixed at both ends and vibrates with three loops at $180~\text{Hz}$. Calculate the wavelength and the wave speed.

1. Three loops: $l = \frac{3\lambda}{2}$, so $\lambda = \frac{2l}{3} = \frac{2 \times 1.20}{3} = 0.80~\text{m}$.
2. $v = f\lambda = 180 \times 0.80 = 144~\text{m s}^{-1}$.

**Answer:** $\lambda = 0.80~\text{m}$; $v = 144~\text{m s}^{-1}$.

### 1.6 Air columns open at both ends

An **open pipe** has an **antinode at each open end**. The simplest pattern has a node in the middle:

- Fundamental: $l = \frac{\lambda}{2}$, so $\lambda = 2l$ and $f_0 = \frac{v}{2l}$.
- 2nd harmonic: $l = \lambda$, $f = 2f_0$.
- 3rd harmonic: $l = \frac{3\lambda}{2}$, $f = 3f_0$.

So an open pipe, like a string fixed at both ends, has **all** harmonics:

$$f_n = \frac{nv}{2l}, \qquad n = 1, 2, 3, \dots$$

**Worked example:** An open pipe is $0.50~\text{m}$ long. The speed of sound is $340~\text{m s}^{-1}$. Calculate the fundamental frequency and the next two harmonics.

1. $f_0 = \frac{v}{2l} = \frac{340}{2 \times 0.50} = 340~\text{Hz}$.
2. Next harmonics: $2f_0 = 680~\text{Hz}$, $3f_0 = 1020~\text{Hz}$.

**Answer:** $340~\text{Hz}$, $680~\text{Hz}$, $1020~\text{Hz}$.

### 1.7 Air columns closed at one end

A **closed pipe** (closed at one end, open at the other) has a **node at the closed end** and an **antinode at the open end**. The simplest pattern is a **quarter of a wavelength**:

- Fundamental: $l = \frac{\lambda}{4}$, so $\lambda = 4l$ and $f_0 = \frac{v}{4l}$.
- Next resonance: $l = \frac{3\lambda}{4}$, $f = 3f_0$.
- Next: $l = \frac{5\lambda}{4}$, $f = 5f_0$.

In general:

$$l = \frac{(2n-1)\lambda}{4} \qquad \Rightarrow \qquad f_n = \frac{(2n-1)v}{4l}, \qquad n = 1, 2, 3, \dots$$

A closed pipe therefore produces **only odd harmonics** ($f_0, 3f_0, 5f_0, \dots$); the even harmonics are missing. This is a standard exam comparison with the open pipe.

**Why only odd harmonics:** the boundary conditions require a node at one end and an antinode at the other. Fitting a whole number of half-wavelengths (which would give even harmonics) would put a node at both ends or an antinode at both ends, which is impossible for a tube closed at one end.

**Worked example:** A closed pipe is $0.50~\text{m}$ long. The speed of sound is $340~\text{m s}^{-1}$. Calculate the fundamental frequency and the next two resonant frequencies.

1. $f_0 = \frac{v}{4l} = \frac{340}{4 \times 0.50} = 170~\text{Hz}$.
2. Next: $3f_0 = 510~\text{Hz}$; then $5f_0 = 850~\text{Hz}$.

**Answer:** $170~\text{Hz}$, $510~\text{Hz}$, $850~\text{Hz}$ (odd harmonics only).

### 1.8 Resonance and the resonance tube

**Resonance** occurs when a system is driven at one of its **natural frequencies**. At resonance the amplitude of vibration is maximum, because energy is transferred most efficiently from the driver to the oscillator.

In the **resonance tube** experiment:

- A glass tube open at the top is lowered into water, so the length of the air column above the water can be adjusted.
- A vibrating tuning fork (or loudspeaker) is held above the open end.
- At certain lengths, the air column resonates and the sound becomes much louder.
- The water surface is a **closed end** (node); the open top is an **antinode**.

For the **first resonance**:

$$l_1 + c = \frac{\lambda}{4}$$

For the **second resonance**:

$$l_2 + c = \frac{3\lambda}{4}$$

Subtracting eliminates the unknown end correction $c$:

$$\lambda = 2(l_2 - l_1)$$

Then

$$v = f\lambda = 2f(l_2 - l_1)$$

and the end correction follows from

$$c = \frac{\lambda}{4} - l_1$$

This is a standard **systematic-error elimination** technique: $c$ affects both measurements equally, so the difference removes it.

**Worked example:** In a resonance tube experiment with a $630~\text{Hz}$ tuning fork, resonance occurs at air-column lengths of $12.6~\text{cm}$ and $38.8~\text{cm}$. Calculate the wavelength, the speed of sound and the end correction.

1. $\lambda = 2(l_2 - l_1) = 2(0.388 - 0.126) = 2(0.262) = 0.524~\text{m}$.
2. $v = f\lambda = 630 \times 0.524 = 330~\text{m s}^{-1}$.
3. $c = \frac{\lambda}{4} - l_1 = \frac{0.524}{4} - 0.126 = 0.131 - 0.126 = 0.005~\text{m}$.

**Answer:** $\lambda = 0.524~\text{m}$; $v \approx 330~\text{m s}^{-1}$; $c \approx 0.5~\text{cm}$.

### 1.9 Measuring wavelength and speed using stationary waves

**String (Melde's experiment):** a string is attached to a vibration generator and passes over a pulley to masses that provide tension. Adjust the frequency until a stable pattern with a clear number of loops appears. Then $\lambda = \frac{2l}{n}$, and $v = f\lambda$. A stroboscope makes the motion visible.

**Microwaves:** a transmitter faces a metal reflecting plate. A probe detects maxima and minima of intensity. Adjacent maxima (or minima) are $\frac{\lambda}{2}$ apart, so $\lambda = 2 \times$ (separation). Then $f = \frac{c}{\lambda}$. The metal plate is a **node** (zero electric field at the conductor surface).

**Sound (microphone and board):** a loudspeaker faces a hard board; a microphone on a line between them detects nodes and antinodes. Measuring across **several** nodes reduces the percentage error.

**Kundt's dust tube:** dust is spread along a tube; at an antinode the air vibrates strongly and the dust is disturbed, while at a node the air is still and dust collects in piles. The distance between adjacent piles is $\frac{\lambda}{2}$.

**Why measure across several nodes:** the node positions can be located only to within a small distance; dividing a large total distance by the number of half-wavelengths reduces the percentage uncertainty in $\lambda$.

**Worked example:** In a microwave experiment, adjacent intensity maxima are $14~\text{mm}$ apart. Calculate the wavelength and frequency.

1. $\lambda = 2 \times 14 = 28~\text{mm} = 0.028~\text{m}$.
2. $f = \frac{c}{\lambda} = \frac{3.0 \times 10^8}{0.028} = 1.07 \times 10^{10}~\text{Hz}$.

**Answer:** $\lambda = 0.028~\text{m}$; $f \approx 1.1 \times 10^{10}~\text{Hz}$ ($11~\text{GHz}$).

### 1.10 Stationary versus progressive waves

| Feature | Progressive wave | Stationary wave |
|---|---|---|
| Energy transfer | Transfers energy from one place to another | **No net energy transfer** along the wave |
| Wave profile | Travels at speed $v$ | Does not travel; fixed nodes and antinodes |
| Amplitude | Same for all particles (ideal, unattenuated) | Zero at nodes, maximum at antinodes |
| Wavelength | Distance between adjacent crests | Twice the distance between adjacent nodes |
| Phase | Changes continuously with distance | All points in a loop in phase; adjacent loops in antiphase |
| Frequency | All particles oscillate at $f$ | All particles oscillate at $f$ |
| Speed | $v = f\lambda$ | No wave speed (the pattern does not propagate) |

**Energy:** in a stationary wave, energy is not transported along the wave; it is stored in the oscillating system between the nodes. Energy can be transferred **into** and **out of** the system (for example, from the driver), but there is no net flow along the pattern.

**Worked example:** State two differences and one similarity between stationary and progressive waves.

1. Difference: a progressive wave transfers energy; a stationary wave does not (net).
2. Difference: in a progressive wave all particles have the same amplitude (ideal); in a stationary wave the amplitude varies from zero at nodes to maximum at antinodes.
3. Similarity: both have the same frequency and obey $v = f\lambda$ (for the progressive waves forming the stationary wave).

**Answer:** as above.

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
