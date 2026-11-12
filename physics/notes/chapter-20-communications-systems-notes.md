# Chapter 20: Communications Systems - CAIE A Level Physics (9702) Study Notes

Exam-focused revision notes for Cambridge International A Level Physics 9702, covering analogue and digital communication, amplitude and frequency modulation, sidebands and bandwidth, sampling and ADC/DAC, signal attenuation in decibels, signal-to-noise ratio, and the comparison of wire-pairs, coaxial cable, radio links, satellites and optic fibres. Definitions are worded for mark schemes, with worked calculations for every formula. This chapter is mainly examined in Paper 4 and occasionally in Paper 2; the decibel calculations are a reliable source of structured marks.

## 1. Theory

### 1.1 The communications system

A communication system transfers **information** from a source to a receiver. A typical radio system has these stages:

1. **Source:** sound (speech or music) or data.
2. **Microphone / input transducer:** converts sound into an analogue voltage signal.
3. **ADC (analogue-to-digital converter):** samples and quantises the signal into binary numbers (if digital transmission is used).
4. **Modulator / transmitter:** superimposes the information onto a **carrier wave** and radiates it.
5. **Channel:** the medium through which the signal travels (wire, cable, free space, optic fibre).
6. **Receiver / demodulator:** selects the carrier frequency and extracts the signal.
7. **DAC (digital-to-analogue converter):** converts binary data back to an analogue voltage (if digital).
8. **Loudspeaker / output transducer:** converts the electrical signal back into sound.

**Carrier wave:** a high-frequency wave that is modulated to carry information. Different stations use different carrier frequencies so that a receiver can select one station by **tuning** to that frequency.

**Modulation:** the variation of either the **amplitude** or the **frequency** of a carrier wave in order to carry information.

**Demodulation:** the process of recovering the original signal from the modulated carrier.

**Why modulate?** Information signals (e.g. speech, 20 Hz–20 kHz) are low frequency. Low-frequency signals cannot be radiated efficiently by practical aerials and cannot be separated between stations. A high-frequency carrier can be radiated efficiently, and different carriers allow many stations to share the spectrum.

### 1.2 Amplitude modulation (AM)

In **amplitude modulation**, the **amplitude** of the carrier wave varies in proportion to the instantaneous value of the signal; the **frequency** of the carrier stays constant.

- The envelope (the outline joining the peaks) of the AM wave has the same shape as the signal.
- The carrier frequency is much higher than the signal frequency.
- The amplitude of the signal must be less than the carrier amplitude; otherwise the envelope crosses zero and the signal is distorted (over-modulation).

**Mathematical picture:** if the carrier is $A_c\cos(2\pi f_c t)$ and the signal is $A_m\cos(2\pi f_m t)$, the AM wave is:

$$(A_c + A_m\cos 2\pi f_m t)\cos 2\pi f_c t$$

Expanding this gives the carrier plus two **sidebands**:

$$A_c\cos 2\pi f_c t + \frac{A_m}{2}\cos 2\pi(f_c-f_m)t + \frac{A_m}{2}\cos 2\pi(f_c+f_m)t$$

This is why AM produces frequencies at $f_c - f_m$ (lower sideband) and $f_c + f_m$ (upper sideband).

**Worked example:** An AM carrier has frequency $100~\text{kHz}$ and is modulated by a $10~\text{kHz}$ signal. State the frequencies present and the bandwidth.

1. Carrier: $100~\text{kHz}$.
2. Lower sideband: $100 - 10 = 90~\text{kHz}$.
3. Upper sideband: $100 + 10 = 110~\text{kHz}$.
4. Bandwidth $= 110 - 90 = 20~\text{kHz} = 2f_m$.

**Answer:** $90$, $100$ and $110~\text{kHz}$; bandwidth $20~\text{kHz}$.

### 1.3 Frequency modulation (FM)

In **frequency modulation**, the **frequency** of the carrier wave varies in proportion to the instantaneous value of the signal; the **amplitude** of the carrier stays constant.

- When the signal is positive, the frequency is **higher** than the carrier frequency.
- When the signal is negative, the frequency is **lower** than the carrier frequency.
- The **frequency deviation** is the maximum change in frequency from the carrier value.
- The deviation is proportional to the signal amplitude: a louder signal gives a larger frequency swing.
- The **rate** at which the frequency changes is the signal frequency.

**Frequency deviation** is often quoted in $\text{Hz V}^{-1}$: for every $1~\text{V}$ of signal, the carrier frequency changes by that amount.

**Worked example:** A $300~\text{kHz}$ carrier of amplitude $5.0~\text{V}$ is frequency-modulated by a $6.0~\text{kHz}$ signal of amplitude $2.0~\text{V}$. The frequency deviation is $30~\text{kHz V}^{-1}$. Describe the modulated wave.

1. Amplitude stays at $5.0~\text{V}$.
2. Maximum frequency shift $= 30 \times 2.0 = 60~\text{kHz}$.
3. Frequency varies between $300 - 60 = 240~\text{kHz}$ and $300 + 60 = 360~\text{kHz}$.
4. The frequency changes through this cycle $6000$ times per second (the signal frequency).

**Answer:** constant $5.0~\text{V}$ amplitude; frequency swings between $240$ and $360~\text{kHz}$ at $6.0~\text{kHz}$.

### 1.4 Sidebands and bandwidth

A pure unmodulated carrier contains only one frequency, $f_c$. When it is modulated by a single frequency $f_m$, new frequencies appear:

- **Lower sideband:** $f_c - f_m$.
- **Upper sideband:** $f_c + f_m$.

For a signal containing a **range** of frequencies from $0$ to $f_m$, the transmitted wave occupies a continuous band from $f_c - f_m$ to $f_c + f_m$.

**Bandwidth:** the range of frequencies occupied by a signal:

$$\text{bandwidth} = (f_c + f_m) - (f_c - f_m) = 2f_m \quad \text{(AM, single highest modulating frequency)}$$

For FM, the spectrum is more complex and contains many sidebands, so FM requires a **larger bandwidth** than AM for the same signal.

**Worked example:** An AM carrier of $1.0~\text{MHz}$ is modulated by frequencies up to $15~\text{kHz}$. Calculate the bandwidth and state the frequency range occupied.

1. $f_m = 15~\text{kHz} = 0.015~\text{MHz}$.
2. Bandwidth $= 2f_m = 30~\text{kHz} = 0.030~\text{MHz}$.
3. Range: $1.000 - 0.015 = 0.985~\text{MHz}$ to $1.000 + 0.015 = 1.015~\text{MHz}$.

**Answer:** $30~\text{kHz}$; $0.985$–$1.015~\text{MHz}$.

**Worked example:** Long-wave radio uses carriers from $140$ to $280~\text{kHz}$, with sidebands within $4.5~\text{kHz}$ of each carrier. Calculate the bandwidth per station and the maximum number of stations.

1. Bandwidth $= 2 \times 4.5 = 9.0~\text{kHz}$.
2. Available range $= 280 - 140 = 140~\text{kHz}$.
3. Number $= \frac{140}{9.0} = 15.6$, so 15 complete channels fit.

**Answer:** $9.0~\text{kHz}$; 15 stations.

### 1.5 Comparing AM and FM

| Feature | AM | FM |
|---|---|---|
| Modulated quantity | Amplitude | Frequency |
| Amplitude of carrier | Varies | Constant |
| Frequency of carrier | Constant | Varies |
| Bandwidth | Narrow ($\approx 9~\text{kHz}$ for LW/MW) | Wide (typically $\approx 200~\text{kHz}$) |
| Susceptibility to electrical interference | High, because noise changes amplitude | Low, because noise rarely changes frequency |
| Sound quality | Lower | Higher |
| Range for a given power | Greater; longer wavelengths diffract around obstacles and follow the Earth's curvature | Line-of-sight; shorter range |
| Transmitter/receiver cost | Lower | Higher |
| Number of stations in a band | More (narrow bandwidth) | Fewer (wide bandwidth) |

**Why FM is less noisy:** electrical interference (sparks, lightning, motors) adds unwanted **amplitude** variations. An FM receiver can clip or limit the amplitude to a constant value, removing the noise, while the information is in the frequency. An AM receiver cannot do this because the information is in the amplitude.

**Why AM has a longer range:** AM uses lower frequencies and longer wavelengths, which diffract more around hills and the Earth's curvature. FM uses VHF/UHF frequencies with short wavelengths, which travel essentially in straight lines (line-of-sight).

**Worked example:** Explain why FM radio generally gives better sound quality than AM radio.

1. FM has a much larger bandwidth, so it can carry higher audio frequencies (up to about $15~\text{kHz}$).
2. FM is less affected by amplitude noise and electrical interference.
3. Therefore the recovered signal has a higher signal-to-noise ratio and better fidelity.

**Answer:** wider bandwidth plus noise immunity.

### 1.6 Analogue and digital signals

**Analogue signal:** a signal whose voltage (or other quantity) can take **any value** within a range and varies continuously with time. A microphone output is analogue.

**Digital signal:** a signal that takes only **two discrete levels**, represented as 0 and 1 (low and high voltage). A 1 is the presence of a voltage pulse; a 0 is the absence of a pulse or a voltage near 0 V.

**Binary:** base-2 representation using bits. A **bit** is one binary digit. With $n$ bits there are $2^n$ possible values.

| Decimal | Binary (4-bit) |
|---|---|
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 0101 |
| 6 | 0110 |
| 7 | 0111 |
| 8 | 1000 |
| 9 | 1001 |
| 10 | 1010 |
| 15 | 1111 |

**Worked example:** Convert 14 and 16 to binary.

1. $14 = 8 + 4 + 2 = 1110_2$.
2. $16 = 10000_2$.

**Answer:** 14 = 1110; 16 = 10000.

### 1.7 Advantages of digital transmission

- **Noise immunity:** digital signals can be **regenerated**. The regenerator decides whether each pulse is above or below a threshold and outputs a clean 0 or 1, removing accumulated noise.
- **Error detection and correction:** extra bits can detect errors and allow retransmission.
- **Storage and processing:** digital data is easy to store, compress and process in computers.
- **Reliability:** digital circuits are generally more reliable and easier to design.
- **Security:** digital signals can be encrypted.

**Regeneration versus amplification:**

- **Analogue repeater:** amplifies both the signal and the noise; the signal-to-noise ratio does not improve and may worsen.
- **Digital regenerator:** reshapes and retimes the pulses, removing noise, provided the noise has not caused a bit error.

**Worked example:** Explain why a digital signal can be transmitted over a longer distance than an analogue signal before it becomes unusable.

1. As the signal travels, it attenuates and picks up noise.
2. An analogue amplifier amplifies signal and noise equally, so the signal-to-noise ratio stays poor.
3. A digital regenerator restores each pulse to a clean 0 or 1, removing the noise, as long as the pulse is still recognisable.
4. Therefore the signal can be regenerated repeatedly without cumulative noise.

**Answer:** regeneration removes noise; analogue amplification does not.

### 1.8 Analogue-to-digital conversion (ADC)

An ADC converts a continuously varying analogue voltage into a sequence of binary numbers. The two key steps are **sampling** and **quantisation**.

**Sampling:** measuring the analogue signal at regular time intervals. The **sampling rate** is the number of samples per second (Hz).

**Quantisation:** rounding each sample to the nearest available discrete level, which is then encoded as a binary number. The number of levels is $2^n$ for an $n$-bit ADC.

**Sampling theorem (Nyquist):** to reproduce a signal faithfully, the sampling rate must be at least **twice the highest frequency** present in the signal:

$$f_s \ge 2f_{\max}$$

For audio up to $20~\text{kHz}$, the minimum sampling rate is $40~\text{kHz}$. For telephony, speech is limited to about $3.4~\text{kHz}$, so $8~\text{kHz}$ sampling is used.

**Effects of poor sampling/quantisation:**

- **Too low a sampling rate:** rapid changes between samples are missed, and the reconstructed signal is distorted (aliasing).
- **Too few bits:** the voltage steps are too coarse, giving **quantisation error** and a noisy approximation.

**Bit rate:** for $n$-bit samples at $f_s$ samples per second:

$$\text{bit rate} = n f_s \quad \text{bits per second}$$

**Worked example:** A signal contains frequencies up to $12~\text{kHz}$ and is sampled at $8$ bits. Calculate the minimum sampling rate and the bit rate.

1. $f_s \ge 2 \times 12 = 24~\text{kHz}$.
2. Bit rate $= 8 \times 24\,000 = 192\,000~\text{bits s}^{-1}$.

**Answer:** $24~\text{kHz}$; $192~\text{kbit s}^{-1}$.

**Worked example:** A 4-bit ADC has a full-scale range of $0$ to $15~\text{V}$. State the number of levels and the voltage resolution.

1. Levels $= 2^4 = 16$.
2. Resolution $= \frac{15}{16-1} = 1~\text{V}$.

**Answer:** 16 levels; $1~\text{V}$ per step.

### 1.9 Digital-to-analogue conversion (DAC)

A DAC converts binary numbers back into a continuously varying voltage. The output is a **staircase** waveform: each binary number gives a voltage level held until the next sample.

A **smoothing filter** (low-pass filter) removes the sharp steps and produces a smoother analogue waveform. The reconstruction is never perfect because:

- The signal is only known at the sampling instants (sampling error).
- Each sample is rounded to a finite number of levels (quantisation error).

Increasing the sampling rate and the number of bits reduces both errors.

**Worked example:** Explain two ways to improve the quality of a digitised audio signal.

1. Increase the sampling rate, so rapid changes are captured (must be at least twice the highest frequency).
2. Increase the number of bits per sample, so the voltage is represented more precisely and quantisation error is reduced.

**Answer:** higher sampling rate and greater bit depth.

### 1.10 Attenuation and the decibel

**Attenuation** is the reduction in signal power as it travels through a channel. It is caused by:

- Resistance heating in wires ($I^2Rt$).
- Spreading of a radio wave and absorption by the medium.
- Scattering and absorption in an optic fibre.

The **decibel (dB)** is a logarithmic unit used to compare two powers. For attenuation:

$$\text{attenuation (dB)} = 10\log_{10}\left(\frac{P_{\text{in}}}{P_{\text{out}}}\right)$$

For a **gain** (amplification), the same formula gives a positive value if $P_{\text{out}} > P_{\text{in}}$:

$$\text{gain (dB)} = 10\log_{10}\left(\frac{P_{\text{out}}}{P_{\text{in}}}\right) = -\text{attenuation (dB)}$$

**Sign convention:** be consistent. If you use $10\log(P_{\text{out}}/P_{\text{in}})$, attenuation is negative and gain is positive. If you use $10\log(P_{\text{in}}/P_{\text{out}})$, attenuation is positive. State which convention you are using.

**Useful values:**

| Power ratio $P_{\text{out}}/P_{\text{in}}$ | dB |
|---|---|
| 2 | $+3$ |
| 10 | $+10$ |
| 100 | $+20$ |
| 1000 | $+30$ |
| $10^6$ | $+60$ |
| 0.5 | $-3$ |
| 0.1 | $-10$ |
| 0.001 | $-30$ |

**Attenuation per unit length:**

$$\text{attenuation per unit length} = \frac{\text{attenuation (dB)}}{\text{length (km)}}$$

Typical units: $\text{dB km}^{-1}$.

**Combining stages:** decibels add. If a signal passes through several channels or amplifiers:

$$\text{total dB} = \text{dB}_1 + \text{dB}_2 + \dots$$

and

$$P_{\text{out}} = P_{\text{in}} \times 10^{\text{total dB}/10}$$

**Worked example:** A signal of power $18.0~\text{mW}$ passes through a cable with attenuation $20~\text{dB}$, then a second cable with attenuation $30~\text{dB}$. Calculate the output power.

1. Total attenuation $= 20 + 30 = 50~\text{dB}$.
2. $50 = 10\log\left(\frac{18.0}{P_{\text{out}}}\right)$.
3. $\log\left(\frac{18.0}{P_{\text{out}}}\right) = 5$, so $\frac{18.0}{P_{\text{out}}} = 10^5$.
4. $P_{\text{out}} = \frac{18.0}{10^5} = 1.8 \times 10^{-4}~\text{mW}$.

**Answer:** $1.8 \times 10^{-4}~\text{mW}$ (or $1.8 \times 10^{-7}~\text{W}$).

**Worked example:** An input of $5.0~\text{mW}$ emerges as $0.0002~\text{mW}$. Calculate the attenuation.

1. Ratio $= \frac{5.0}{0.0002} = 25\,000$.
2. Attenuation $= 10\log_{10}(25\,000)$.
3. $\log_{10}(25\,000) \approx 4.40$.
4. Attenuation $\approx 44~\text{dB}$.

**Answer:** $44~\text{dB}$.

### 1.11 Signal-to-noise ratio

**Noise** is any unwanted random signal that adds to and distorts the transmitted signal. Sources include thermal motion of electrons, nearby electrical equipment, sparks, and interference from other channels.

**Signal-to-noise ratio (SNR):**

$$\text{SNR (dB)} = 10\log_{10}\left(\frac{P_{\text{signal}}}{P_{\text{noise}}}\right)$$

A ratio of $30~\text{dB}$ means the signal power is $1000$ times the noise power. For acceptable reception, the SNR must exceed a minimum value (often $30~\text{dB}$ for digital systems).

**Repeaters:** at regular intervals, a repeater amplifies the signal to overcome attenuation. An analogue repeater amplifies signal and noise equally, so the SNR is unchanged. A digital regenerator restores clean pulses and can improve the SNR.

**Worked example:** The noise power in a cable is $1.0 \times 10^{-10}~\text{W}$. The minimum acceptable SNR is $30~\text{dB}$. Calculate the minimum acceptable signal power.

1. $30 = 10\log\left(\frac{P}{1.0 \times 10^{-10}}\right)$.
2. $\frac{P}{1.0 \times 10^{-10}} = 10^3 = 1000$.
3. $P = 1.0 \times 10^{-7}~\text{W}$.

**Answer:** $1.0 \times 10^{-7}~\text{W}$.

**Worked example:** An input signal of $1.2 \times 10^{-3}~\text{W}$ travels along a cable with attenuation $14~\text{dB km}^{-1}$. The noise is constant at $1.0 \times 10^{-10}~\text{W}$ and the minimum SNR is $30~\text{dB}$. Calculate the maximum cable length before a repeater is needed.

1. Minimum signal power $= 1.0 \times 10^{-7}~\text{W}$ (from the previous example).
2. Attenuation needed $= 10\log\left(\frac{1.2 \times 10^{-3}}{1.0 \times 10^{-7}}\right)$.
3. Ratio $= 1.2 \times 10^4$; $\log = 4.079$; attenuation $= 40.8~\text{dB}$.
4. Length $= \frac{40.8}{14} = 2.9~\text{km}$.

**Answer:** about $2.9~\text{km}$.

### 1.12 Channels of communication

A **channel** is the medium or path used to carry a signal from transmitter to receiver. The main channels are:

| Channel | Typical use | Key features |
|---|---|---|
| **Wire-pair** | Telephone lines, Ethernet | Cheap; high attenuation; low bandwidth; picks up noise and crosstalk; low security |
| **Coaxial cable** | TV aerial downlead, broadband | Screened braid reduces interference; higher bandwidth; less crosstalk; more expensive |
| **Radio waves** | AM/FM radio, TV, mobile | No physical link; surface, sky or space propagation |
| **Microwave link** | Point-to-point towers, satellite | High bandwidth; narrow beam; line-of-sight |
| **Optic fibre** | Long-distance telephony, internet | Very high bandwidth; low attenuation; immune to EMI; secure; expensive to join |
| **Satellite** | Broadcasting, global links | Wide coverage; long path; delay; geostationary or polar orbit |

**Crosstalk:** the unwanted transfer of a signal from one channel to another (e.g. hearing another telephone conversation). It is caused by electromagnetic coupling between nearby wires. Coaxial screening and twisted pairs reduce crosstalk.

### 1.13 Wire-pairs and coaxial cables

**Wire-pair:** two insulated copper wires close together, often twisted.

- The signal is the potential difference between the wires.
- Twisting ensures both wires pick up similar interference, which cancels as a common-mode signal.
- Cheap and convenient.
- High attenuation, low bandwidth, susceptible to noise and crosstalk, easy to tap.

**Coaxial cable:** a central copper core surrounded by insulation, a woven copper braid, and an outer protective sheath.

- The braid is earthed and acts as a **screen**, preventing external electromagnetic waves from reaching the core and preventing the core from radiating.
- Less attenuation, higher bandwidth, less crosstalk, more secure.
- More expensive and stiffer than a wire-pair.

**Worked example:** Explain how the braid in a coaxial cable reduces interference.

1. The braid is a conductor connected to earth.
2. It surrounds the inner core and screens it from external electric fields.
3. External electromagnetic waves induce currents in the braid rather than in the core, so the signal in the core is not distorted.

**Answer:** electrostatic/electromagnetic screening by the earthed braid.

### 1.14 Radio wave propagation

Radio waves can reach a receiver by three main paths:

| Type | Frequency | Mechanism | Typical range |
|---|---|---|---|
| **Surface (ground) wave** | Up to about $3~\text{MHz}$ | Diffracts around the Earth's surface; long wavelength | Up to about $1000~\text{km}$ |
| **Sky wave** | About $3$–$30~\text{MHz}$ | Reflected by the ionosphere; can undergo multiple hops | Worldwide |
| **Space wave** | Above about $30~\text{MHz}$ | Passes through the ionosphere; line-of-sight | Up to the horizon, or via satellite |

**Surface waves:** low frequencies have long wavelengths and diffract significantly around obstacles and the Earth's curvature. AM long-wave and medium-wave broadcasts use surface waves. The range is limited by absorption and by the curvature of the Earth.

**Sky waves:** the ionosphere is a layer of charged particles that refracts/reflects radio waves below about $30~\text{MHz}$. Multiple reflections between the ionosphere and the ground allow long-distance reception. The ionosphere changes with time of day and solar activity, so sky-wave reception is variable.

**Space waves:** frequencies above about $30~\text{MHz}$ pass through the ionosphere and travel in straight lines. They are used for FM radio, television, mobile phones and microwave links. They require a clear line of sight between transmitter and receiver.

**Worked example:** Explain why AM radio can be received over a much larger area than FM radio for the same transmitter power.

1. AM uses lower frequencies and longer wavelengths.
2. Longer wavelengths diffract more around hills and the Earth's curvature, and can travel as surface waves.
3. FM uses VHF frequencies with short wavelengths, which travel by line-of-sight and are blocked by obstacles and the horizon.

**Answer:** AM's longer wavelengths diffract and follow the ground; FM is line-of-sight.

### 1.15 Microwaves and satellite links

**Microwaves** are radio waves with frequencies above about $1~\text{GHz}$ (wavelengths below about $0.3~\text{m}$).

- High bandwidth, so they can carry many signals at once.
- Can be focused into narrow beams using parabolic dishes, which increases security and reduces interference.
- Travel line-of-sight, so repeater towers are placed on high ground or tall masts.

**Satellite communication:**

- **Uplink:** Earth station transmits a microwave signal to the satellite.
- **Downlink:** the satellite amplifies and re-transmits the signal to Earth on a **different frequency**.
- Different frequencies are used because the high-power uplink would otherwise swamp the weak downlink at the receiver, and to avoid feedback between the satellite's receiver and transmitter.

**Why the satellite re-transmits rather than reflects:** a passive reflection would be far too weak; the satellite amplifies the signal before sending it back.

**Geostationary satellite:**

- Orbits above the **equator** in the same direction as the Earth's rotation.
- Period $= 24~\text{hours}$.
- Height $\approx 36\,000~\text{km}$ above the Earth's surface.
- Appears stationary from the ground, so dishes do not need to track it.
- Cannot cover the polar regions well; there is a noticeable signal delay.

**Polar-orbit satellite:**

- Travels over the poles; lower altitude (e.g. $1000~\text{km}$).
- Shorter period (e.g. $100~\text{min}$).
- Can observe the whole Earth as it rotates underneath; better resolution because it is closer.
- Not always overhead, so tracking is needed; shorter delay.

**Delay calculation:** for a geostationary satellite directly overhead, the path up and down is about $2 \times 36\,000 = 72\,000~\text{km}$.

$$t = \frac{d}{c} = \frac{7.2 \times 10^7}{3.0 \times 10^8} = 0.24~\text{s}$$

A two-way conversation therefore has at least $0.48~\text{s}$ delay.

**Worked example:** Calculate the wavelength of a $14~\text{GHz}$ uplink signal.

1. $f = 14 \times 10^9~\text{Hz}$.
2. $\lambda = \frac{c}{f} = \frac{3.0 \times 10^8}{14 \times 10^9}$.
3. $\lambda = 0.0214~\text{m} \approx 2.1~\text{cm}$.

**Answer:** about $2.1~\text{cm}$.

### 1.16 Optic fibres

An **optic fibre** is a very thin glass or plastic fibre that carries light or infrared by **total internal reflection**.

- Core of high refractive index surrounded by cladding of lower refractive index.
- Light striking the core–cladding boundary at an angle greater than the critical angle is totally internally reflected and guided along the fibre.
- Long-distance fibres use **infrared** in very pure glass, because infrared is absorbed and scattered less than visible light.
- The light source is a **laser** or **LED**, modulated to produce pulses (digital signal).

**Advantages of optic fibre over copper cable:**

- Much greater bandwidth, so more information per second.
- Lower attenuation, so repeaters can be farther apart.
- Immune to electrical interference and crosstalk.
- Difficult to tap, so more secure.
- Lighter and thinner.
- No spark hazard in flammable environments.
- Not affected by lightning or nearby power lines.

**Disadvantages:**

- Electrical signals must be converted to light and back.
- Fibres are fragile and difficult to join; precise connectors and splicing are needed.
- Installation and repair can be costly.

**Worked example:** An LED launches $1.26~\text{mW}$ into a $60~\text{m}$ fibre; the output is $1.12~\text{mW}$. Calculate the attenuation and the attenuation per unit length.

1. Attenuation $= 10\log\left(\frac{1.26}{1.12}\right)$.
2. Ratio $= 1.125$; $\log = 0.0512$.
3. Attenuation $= 0.512~\text{dB}$.
4. Length $= 0.060~\text{km}$.
5. Attenuation per km $= \frac{0.512}{0.060} = 8.5~\text{dB km}^{-1}$.

**Answer:** $0.51~\text{dB}$; $8.5~\text{dB km}^{-1}$.

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
