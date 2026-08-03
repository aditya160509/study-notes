**309**

# Chapter 20: Communications

**systems**

## Learning outcomes

##### You should be able to:

■■ understand amplitude and frequency modulation and comment on the relative advantages of AM and FM transmission ■■ describe digital transmission systems in terms of analogue-to-digital (ADC) and digital-to-analogue (DAC) conversion and sampling rate ■■ describe and compare diff erent networks or channels of communication ■■ calculate signal attenuation in dB and dB per unit length

## Communications today

**The ability to communicate is an important feature of modern life. We can now speak directly to others**

**right around the world and generate vast amounts of information every day. The invention of the mobile**

**phone has increased our ability to talk to one another and to find out what is happening around us. This**

##### chapter looks briefly at how some communications systems work. Communications engineers have

##### applied the principles of physics to change the present and shape the future.

**Figure 20.1** A communications satellite.

**310**

## Radio waves

|The person listening to the radio in Figure 20.2 is at the|Sound waves and radio waves are completely different||
|---|---|---|
|end of a communications system. The system starts with|types of wave:||
|sound or music passing into a microphone. The sound|Sound waves travel as mechanical vibrations. Their speed||
|signal is converted into a radio signal and at the end of the|is typically 330 ms|in air, and audible frequencies lie|
|communications system the radio signal is converted back|between 20 Hz and 20 kHz.||
|again into a sound signal.|Radio waves are electromagnetic waves which travel at the speed of light (3.0 × 10|ms in a vacuum). Their frequencies|

■■ −1

■■ 6 −1 are much higher than those of sound waves.

(You should recall from Chapter 13 that wave speed *v*, frequency *f* and wavelength *λ* are related by *v* = *fλ*.) To allow several radio stations to broadcast, each signal has a different **carrier wave** frequency. To hear just one station at a time, you tune the radio receiver so that it separates out radio waves of a single frequency. The information, for example a sound signal, is carried by modulating or altering the carrier wave. **Modulation** is the variation of either the **amplitude** or the **frequency** of the carrier wave. The modulated wave is the actual wave transmitted. The signal is present in either the changing amplitude or the changing frequency of the modulated wave.

**Figure 20.2** Part of a communications system.

##### Chapter 20: Communications systems

### Amplitude modulation

Figure 20.3 shows **amplitude modulation** (AM). The

three diagrams show the carrier wave, the signal and the modulated wave. In each case, the horizontal axis represents time, shown on the axis at the bottom. The modulated wave is the carrier wave but its amplitude rises and falls to match the value of the signal at any instant. Look at the amplitude-modulated wave on its own, and notice how the amplitude variation at top and bottom has the same pattern as the signal.

the carrier wave (no modulation)

the signal

##### QUESTIONS

the amplitude- modulated wave **1** Imagine that all the numbers on the time axis in **311**

Figure 20.3 are doubled, so that 100 becomes 200

and 200 becomes 400. Calculate the frequency of 200 40 60 80 100 120 140 160 180 Time / µs

**Figure 20.3** Amplitude modulation.

The amplitude of the signal must be less than half of the amplitude of the carrier wave; otherwise the variation in the amplitude at the top will be confused with the variation in amplitude at the bottom of the wave. If a radio station carries music, the wave transmitted by the radio station will differ from the wave shown in

Figure 20.3. There is only one signal frequency present in

the signal in Figure 20.3. Music consists of many changing frequencies superposed so that it has a more complex wave pattern. The amplitude of the carrier wave will change as the music pattern changes. The carrier wave frequency does not change but the amplitude of the trace will change with time. In amplitude modulation (AM), the frequency of the modulated wave is constant. The amplitude of the modulated wave is proportional to, and in phase with, the signal.

##### WORKED EXAMPLE

**1** Calculate the frequencies of the carrier wave and signal shown in Figure 20.3.

**Step 1** For the carrier wave, there are 10 complete waves in 100 µs. Hence:

time for one complete carrier wave, −5 *T* = 10 µs = 1 × 10 s <u>1</u> carrier wave frequency *f*c= *T* = 100 000 Hz

**Step 2** For the signal, there is one complete wave in 100 µs. Hence: <u>1</u> frequency of the signal *f*s =−6 100 × 10

= 10 000 Hz

A radio wave of 100 000 Hz is in the long-wavelength, low-frequency region of the radio electromagnetic spectrum. A sound frequency of 10 000 Hz is a very high frequency note but is audible.

the carrier wave and the frequency of the signal.

**2** Draw an amplitude-modulated wave with a carrier wave of frequency 1.0 MHz and a signal frequency of 100 kHz. The time axis on your graph should be from 0 to 10 µs. On your graph, mark the time for one complete wave of the signal and for one complete wave of the carrier.

**3** Explain how an amplitude-modulated wave changes when the input signal: **a** increases in loudness **b** increases in frequency.

### Frequency modulation

In **frequency modulation** (FM) the frequency of the modulated wave varies with time. Without any signal, the frequency of the modulated wave is equal to the frequency of the carrier wave. The size of the input signal at any instant causes the frequency of the modulated wave to change. When the input signal is positive, the frequency of the modulated wave is increased so that it is larger than the frequency of the carrier wave. The larger the signal, the greater is the increase in the frequency. When the signal is negative, the frequency of the modulated wave is less

the carrier wave (no modulation)

signal signal +ve −ve

the signal

frequency frequency higher lower

the frequency- modulated wave

Time

**Figure 20.4** Frequency modulation.

##### WORKED EXAMPLE

|2 A carrier wave of frequency 300 kHz and amplitude|Step 2 Now consider how the signal will modify the|
|---|---|
|5.0 V is frequency modulated by a sinusoidal signal of|carrier frequency. The frequency shift produced by the|
|frequency 6 kHz and amplitude 2.0 V. The frequency|signal is ± 2 × 30 = ± 60 kHz, so the carrier wave varies in|
|deviation of the carrier wave is 30 kHz V|frequency between 240 and 360 kHz. This variation in|
|modulated carrier wave produced.|frequency occurs 6000 times every second as the signal varies at this frequency.|

**312**

−1. Describe the

**Step 1** Consider the amplitude of the modulated signal. The amplitude of the carrier wave is unchanged at 5.0 V during frequency modulation. The signal alters the frequency of the carrier wave, not its amplitude.

than the frequency of the carrier wave. Figure 20.4 shows frequency modulation. In frequency modulation (FM), the modulated wave has a constant amplitude. It is the frequency of the modulated wave that changes as the signal changes. The frequency deviation of the carrier wave may be given a value, for example, 25 kHz V −1. This means that for every 1.0 V change in the voltage of the signal, the frequency of the carrier wave changes by 25 kHz. In some countries, the maximum allowed change in frequency during FM is set as 75 kHz, in order that the frequency of one station does not overlap the frequency of the next −1 station. If the frequency deviation is 25 kHz V and the maximum change is 75 kHz, then the maximum signal producing the FM is 3.0 V.

### Sidebands and bandwidth

A carrier wave contains only one frequency, the carrier

|Explain how a frequency-modulated wave|. When the carrier wave is modulated||
|---|---|---|
|4|c||
|||m|
|a|||
|b||c m|
|5|c m||

wave frequency *f* in amplitude by a single frequency *f*, then the carrier wave is found to contain two more frequencies, known as sideband frequencies, one at a frequency (*f* − *f*) and the other at (*f* + *f*). Figure 20.5 shows these frequencies. When music or speech is transmitted, the carrier is modulated by a range of frequencies which change with time. Each frequency *f*m present in the signal gives rise to an extra pair of frequencies in the modulated wave. The result is a band of frequencies, called the **upper** and **lower** **sidebands**, stretching above and below the carrier frequency by the value of the highest modulating frequency.

Figure 20.6 shows the frequency spectrum for a carrier

wave of frequency 1 MHz modulated with frequencies between 0 and *f*m = 15 kHz = 0.015 MHz. The highest

##### QUESTIONS

changes, when the input signal: increases in loudness increases in frequency.

A signal of frequency 16 kHz and amplitude 3.0 V is used for frequency modulation of a carrier wave of frequency 500 kHz. The frequency deviation of the carrier wave is 8.0 kHz V −1. **a** What is the maximum frequency shift produced? **b** What is the maximum frequency of the modulated carrier wave? **c** How many times per second does the modulated carrier wave increase and decrease in frequency?

Signal power

0 (*f*c – *f*m) *f*c(*f*c + *f*m) Frequency bandwidth 2*f*m

**Figure 20.5** The frequency spectrum of a carrier wave

modulated in amplitude by a signal of one frequency.

frequency present in the spectrum is (*f*c+ *f*m) = 1.015 MHz and the lowest frequency is (*f*c− *f*m) = 0.985 MHz. The actual shape of the sidebands in Figure 20.6 will vary at any instant as the signal changes. The maximum and minimum values are important, as these must not overlap the sidebands from any other radio station. The value of *f*m needed depends on the quality required in the signal. High-quality music only needs frequencies up to 15 kHz, even though the ear can hear frequencies up to 20 kHz. Speech only needs frequencies up to 3.4 kHz for people to understand one another.

carrier lower sideband upper sideband

Signal power

0.985 1.000 1.015 Frequency / MHz
**Figure 20.6** The frequency spectrum for an amplitude-

modulated wave.

You can see that the modulated carrier wave occupies a region of the spectrum from 0.985 MHz to 1.015 MHz. The **bandwidth** of a signal is the range of frequencies that the signal occupies. In other words, it is the difference between the highest-frequency signal component and the lowest- frequency signal component. In Figure 20.6 the bandwidth is

1.015 − 0.985 = 0.030 MHz
In Figure 20.5 the bandwidth is (*f*c+ *f*m)−(*f*c− *f*m) = 2*f*m. The frequency spectrum of a frequency-modulated (FM) carrier wave is more complex. In particular, there are often more than two sideband frequencies for each signal frequency. This means that frequency modulation requires a greater bandwidth for each radio station.

##### WORKED EXAMPLE

**3** Radio stations, which broadcast in the long-wave (LW) region of the electromagnetic spectrum, use carrier frequencies between 140 kHz and 280 kHz. The sidebands are within 4.5 kHz on either side of the carrier frequency. State the bandwidth of each radio station in the LW region of the spectrum and calculate the maximum number of radio stations which can transmit in the LW region.

**Step 1** The bandwidth of an individual station is twice the width of an individual sideband: bandwidth = 2 × 4.5 = 9.0 kHz

**Step 2** The LW region is divided into regions of width

9.0 kHz. Hence:
allowed frequency range number of stations = bandwidth

= (280 − 140)

9.0
= 15.5 = 15 stations

Suppose a country decides to increase the quality of music transmitted by each radio station. What happens to the bandwidth and the maximum number of stations in the LW region? Better sound **313** quality requires an increase in the maximum frequency of the signal that modulates the carrier wave, and so the bandwidth needed increases. This decreases the number of available stations in the LW region of the spectrum.

### Comparing AM and FM transmissions

You may have noticed crackle on a radio when you switch lights in your house on and off or when there is a lightning strike nearby. The lightning strike or switching a current on or off creates a burst of radio waves. These radio waves produce unwanted electrical interference and change the amplitude of the radio wave received by a radio. Since the **amplitude** of the wave carries the signal, when amplitude modulation is used the output of the radio is affected. Most electrical interference does not affect the **frequency** of the radio wave received by a radio and thus electrical interference affects FM less than AM. FM radio was actually invented to overcome the electrical interference and noise problems of AM radio and this remains an important advantage today. FM came later than AM and had to use higher frequencies than AM. Although there was extra cost in developing the electronics to work at these higher

##### QUESTIONS

**6** Figure 20.7 shows the frequency spectrum of the signal from a radio transmitter. A carrier and two sideband frequencies are present.

frequencies, it was still an advantage. The greater range of frequencies available means that each station can use a higher bandwidth (about 200 kHz, compared to 9 kHz for AM). FM signals typically contain frequencies of 15 kHz or higher and the quality of sound produced is much higher when using FM transmission. However, AM transmission has a number of advantages. ■■ The bandwidth needed for each AM transmission is less than for FM transmission. This means that more stations can be included in any given frequency range of the electromagnetic spectrum. ■■ The actual receiver and transmitter used for AM are less complicated and cheaper than for FM transmission. ■■ AM transmissions use lower frequencies and have longer wavelengths than FM. This means that these radio waves can diffract some way around the Earth, whereas FM is line-of-sight only. Thus AM can cover a larger area than FM transmissions, for the same power output.

The relative advantages of FM and AM are summarised in

Table 20.1.

##### Advantages of FM Advantages of AM

less electrical interference greater area covered by **314** and noise one transmitter smaller bandwidth means greater bandwidth produces more stations available in any a better quality of sound frequency range cheaper radio sets

**Table 20.1** The relative advantages of FM and AM broadcasting.

35 40 45 Frequency/kHz

**Figure 20.7** For Question 6.

**a** What is the name of the type of modulation that produces two sideband frequencies? **b** What is the carrier frequency? **c** What is the frequency of the signal used to modulate the carrier wave? **d** What is the bandwidth of the transmitted signal?

**7 a** Calculate the number of separate AM radio stations of bandwidth 9 kHz that are possible in the frequency spectrum available for AM between 530 and 1700 kHz. **b** Suggest why FM stations of bandwidth 200 kHz are not used for this range of frequencies.

**8** Is the greater bandwidth available on FM an advantage or a disadvantage?

**9** FM is used largely in towns and AM in rural settings. Suggest why.

## Analogue and digital signals

An analogue quantity is one that can have any value, for example the height of a person. A digital quantity has only a few values, usually just two; for example a person is either male or female. So far, the signals we have dealt with in this book have been analogue signals. For example, the voltage signal generated by a microphone is an **analogue signal**; the output voltage from the microphone can have any value, within limits, and is an exact representation of the pressure variation in a sound wave. A **digital signal**, on the other hand, looks completely different and consists of a series of zeroes (0) and ones (1). A 1 in a digital signal is just the presence of a voltage pulse, usually a voltage value of a few volts. A 0 in a digital signal is the absence of a pulse and is a voltage close to 0 V. A typical digital electronic system will interpret any voltage

below about 0.3 V as a 0 and any voltage above about 1.5 V as a 1. Small fluctuations in voltage will not be noticed.

Figure 20.8 shows an analogue and a digital signal. The

digital signal is the number 0101001101, which is actually a pulse of 0 V followed by a pulse of 3 V and so on.

/V 3 0 Voltage Time 0 1 0 0 01 0 111

**Figure 20.8** Analogue and digital signals.

### Advantages of digital signals

Most devices such as microphones or thermistors produce analogue voltage signals. However, digital signals have advantages and it is often worthwhile to change an analogue signal into a digital signal. The major advantage is that digital signals can deal with ‘noise’ produced over long distances. All signals, both analogue and digital, become weaker as they travel and they pick up electrical noise. The decrease in strength is known as attenuation, and can be corrected by amplifying the signal at regular intervals during long-distance transmission. Noise is electrical interference, caused in a number of different ways: by the spark from a car ignition, by induced voltages from the magnetic fields caused by currents around the home, by the radio signals emitted by a mobile phone nearby, and even by the random thermal motion of electrons in a wire or by vibrating atoms. You may have noticed a background hiss on telephone conversations. This also is an example of noise. **Noise** is the random, unwanted signal that adds to and distorts a transmitted signal. Amplification of a signal amplifies the noise at the same time as the signal.

3 0 Voltage / V Time

**Figure 20.9** Weakened and noisy signals.

Figure 20.9 shows the signals from Figure 20.8 after

they have travelled a long distance. You will see that they are lower in amplitude and have unwanted variations, or noise. There is little improvement possible for an analogue signal; amplification will not remove the noise. However, **regeneration** will remove the noise from a digital signal. The signal is ‘cleaned’ of the noise and returned to its initial shape. At the end of a long-distance transmission, an electronic circuit, the regeneration amplifier, receives the digital signal. This electronic circuit expects to receive a pulse of a few volts or no pulse at all; any small variations added to the pulse or the 0 V make no difference. The regeneration amplifier can only give a 0 or a 1 as an output. As long as the noise does not completely change the shape of the signal, then the regeneration amplifier returns the digital signal shown in Figure 20.9 to the perfect pulses shown in Figure 20.8.

Other advantages of using digital signals are: ■■ Digital signals are compatible with modern technology and can be stored and processed more easily, for example in a computer or on a compact disc (CD). ■■ Digital electronic systems are, in general, more reliable and easier to design and build. ■■ Digital signals build in safeguards so that if there is an error in reception it is noticed and parts of the signal can be sent again.

### Analogue-to-digital conversion

The key to the digital revolution has been the ability to change speech and music from analogue into digital form in **analogue-to-digital conversion (ADC)** and then convert them back again into analogue form in **digital-to-analogue conversion (DAC).** In order to understand this process, you need to be able to count using binary numbers as well as ordinary decimal numbers. The decimal system has base 10 and the number of digits increases by one when going from the number 9 to the number 10. The number 9 has only one digit whereas the number 10 has two digits. The binary number system has base 2 and the number of digits increases when going up from the number 1; so the next number above 1 **315** is 10. The binary number 10 is not the same as the decimal number 10. Table 20.2 compares counting in the decimal system and in the binary system.

##### Decimal Binary Decimal Binary number number number number

0 0 6 110 1 1 7 111 2 10 8 1000 3 11 9 1001 4 100 10 1010 5 101 11 1011

**Table 20.2** Binary and decimal numbers.

For example: ■■ in the decimal system, the number 243 is a combination of 2 × 100, 4 × 10 and 3 × 1 ■■ in the binary system, the number 111 is a combination of 1 × 4, 1 × 2 and 1 × 1.

Counting in the binary system is very similar to counting in the decimal system except that there are only the digits 0 and 1. Each digit in the binary number is known as a **bit**. The bit on the left-hand side of a binary number is the **most significant bit (MSB)** and has the highest value.

Large numbers require more bits. Table 20.2 shows numbers containing 4 bits, although 0011 is the correct way of writing a 4-bit number, rather than writing 11. A digital telephone system commonly transmits numbers containing 8 bits and there are 2 8 = 256 different 8-bit binary numbers. Changing an analogue signal into a digital signal involves sampling. In analogue-to digital conversion (ADC), **sampling** is the measurement of the analogue signal at regular time intervals. The value of the sampled signal is used to produce a binary number. Each time that the signal is sampled the

Figure 20.11 shows the result of this conversion back

into analogue form. The blue circles show the values of the voltage, which are each a decimal number formed from a 4-bit binary number. The black line drawn through the circles is the output signal. Some electronic systems contain extra filter circuits that are able to smooth the output, and they produce the blue line as the final output. The black line, the output, is clearly not exactly the same as the original signal. There are two reasons for this.

10 1010

|||||ADC produces a binary number of a certain number of||||||9|||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|binary numbers are produced.||||bits. Since the sample is taken many times per second, this series of 0s and 1s becomes the digital signal that is|many binary numbers are created, one after the other, and The process is illustrated in Figure 20.10 where 4-bit|||||8 6 Voltage / V 3 1010 0 1001 0 1000 Figure 20.11 0111 0011 not 8.3.|200 400 600 800 Time / µs Digital-to-analogue conversion. Firstly, the sampled signal is not always a whole number. For example, in Figure 20.10 when actual voltage is 8.3 V but only the number 8 can be sent, To improve the sampling, the voltage that corresponds||
|0|200 binary, this number is 1001. When|t|400 You will notice that at some values of|Analogue-to-digital conversion. signal is 9 as a decimal number. When converted into 10 as a decimal number and 1010 as a binary number. When the output is sampled every 100 µs, a set of binary numbers is produced: (1001), then (1010), then (1001), then (1000), then (1000) and so on. These sets of|600 a whole number on the voltage axis. The nearest number is|Time / µs|800 t|= 0, the numerical value of the voltage|1000 t|= 100 µs, the voltage is the signal is not|to the difference between 0 and 1 must be decreased. In the above example, the difference between 0 and 1 in binary is 1 V and so the signal is ‘accurate’ to only 1 V. If the difference between 0 and 1 is made to be 0.1 V then ‘accuracy’ is improved. Adding an extra bit is similar to having an extra significant figure when measuring a voltage as 8.3 V rather than 8 V. Integers up to 10 need a 4-bit binary number. If the system handles numbers to within 0.1 then 10.0 requires an 8-bit number, which has 128 different possible levels. The other problem is that the sampling rate is not high enough. The sampling rate is the number of samples made per second. In the example in Figure 20.10, the sample is taken every 100 µs and so the sampling rate is 1||

1001 1000

0011 transmitted.

10 9 8 **316** 6

Voltage / V 3

**Figure 20.10**

##### When the time

chosen.

*t* = 300 µs the

|4-bit numbers are transmitted one after the other. If they|to another value and back|0.0001 = 10 000 times a second.|
|---|---|---|
|are transmitted a long distance, a regeneration amplifier|If the signal changes to another value and back between||
|is used along the way to keep the same pattern of pulses.|one sample and the next then no record is made of that||
|A digital-to-analogue converter changes the digital signal|change. Obviously the higher the sampling rate, the||
|back into analogue form at the end of the transmission.|closer the final signal will be to the original signal.||

The maximum sampling rate required is only twice the

## Channels of communication

highest frequency present in the signal (this is known as

|Nyquist’s theorem). The human ear can hear up to 20 kHz||The term channel of communication refers to the|
|---|---|---|
|and so the maximum sampling rate needed is 40 kHz||medium, the path or even the actual frequency range used|
|for music. For every second of music on a compact disc||to convey information from a transmitter to a receiver.|
|storing 8-bit numbers sampled 40 000 times a second,||When you listen to a radio, the radio signal may have|
|320 000 separate binary digits are stored. The sampling||travelled through the air by a number of different routes.|
|rate required for a telephone system will be lower, since||When you talk to someone on a telephone in a different|
|only frequencies up to about 3400 Hz are required for||country then the signal may have passed along a wire-pair,|
|basic speech recognition. Many digital telephone systems||a coaxial cable, through the air by a microwave link or|
|sample the input signal 8000 times a second and so only||been converted into pulses of light and then transmitted|
|transmit frequencies below 4 kHz.||down an optic fibre. These are all different channels of communication.|
|QUESTIONS||Before comparing the different channels you will need to understand another technical term, crosslinking, and be|
|10|Convert the following decimal numbers into|able to calculate signal attenuation.|

binary numbers: **a** 14 **b** 16

**11** Convert the following binary numbers into decimal numbers: **a** 1111 **b** 0001011

**12** The diagrams in Figure 20.12 show a digital signal at the start of a long cable and at the end of the cable. Both diagrams are drawn to the same horizontal scale (time) and vertical scale (voltage).

before transmission at the end of a long cable

**Figure 20.12** For Question 12.

**a** Explain what feature of the top diagram shows that the signal is digital. **b** State and explain **two** advantages of digital transmission over analogue transmission of data. **c** State and explain **two** reasons why the signal at the end of the long cable differs from the signal at the start.

### Crosstalk

You may have experienced crosstalk or **crosslinking** when using a radio or a telephone. If you tune your radio set to one radio station, sometimes you can also hear another station. When talking on the telephone you can suddenly find yourself listening to a completely different telephone conversation; the telephone network has connected your telephone to someone you have not dialled. Crosslinking **317** occurs when a signal, transmitted on one circuit or channel, creates an undesired effect in another circuit or channel.

### Signal attenuation

Attenuation is the gradual decrease in the power of a signal the further it travels. The causes of energy loss depend on the type of signal: ■■ As an electrical signal passes along a wire, there is a voltage drop across the resistance of the wire itself. This reduces the voltage of the signal that arrives at the end of the wire. The energy loss in the wire causes electrical heating in the resistance of the wire (*I²Rt*). ■■ A radio wave spreads out from a transmitter. On its own this spreading causes a decrease in intensity, but there is also a loss in signal strength because of the absorption of energy by the material through which the wave travels. ■■ Light travelling through an optic fibre may be scattered or absorbed by irregularities in the glass structure.

The decrease in signal power from the transmitted value *P₁* to that received *P₂* can be very high. The ratio *P₂* to *P₁* is measured using a logarithmic scale rather than by the simple ratio of the two powers. The logarithm to base 10 of the ratio gives us the number of bels (B). When multiplied by 10 we obtain the number of **decibels** (dB). Your calculator may show logarithms to base 10 as log₁₀.

They are written here as lg and must not be confused with

### Overcoming attenuation

logarithms to base e, which are usually written as ln. In long-distance cables, the attenuation is given as −1 <u>P₂</u>. attenuation per unit length, with units such as dB km number of B = lg *P₁* The attenuation is found from the equation: <u>P₂</u> −1 number of dB = 10 lg attenuation per unit length (dB km) *P₁* <u>attenuation (dB)</u> = length of cable (km) For example, suppose *P₂* is 1000 times greater than *P₁*: When a signal travels along a cable, the level of the noise <u>1000</u> number of dB = 10 lg = 30 is important. The signal must be distinguishable above the 1 level of the noise. The signal-to-noise ratio, measured in The number is positive because there is an increase in decibels, is given by the expression: power – the signal is amplified. Attenuation produces a <u>signal power</u> negative number of decibels; for example, an attenuation signal-to-noise ratio = 10 lg noise power of −30 dB means that the received signal is 1000 times smaller than the signal transmitted. At regular intervals along a cable, **repeaters** amplify You may be much more familiar with logarithms to the signal. If the signal is analogue then repeaters also base e than with logarithms to base 10. All logarithms amplify the noise. Multiplying both signal and noise obey the same rules; some, which you should know, are: by the same amount keeps the signal-to-noise ratio the same. Regeneration of a digital signal at the same time as

|log of a product|log (ab) = log (a) + log (b)||
|---|---|---|
|log of a ratio|log|a = log (a) − log (b)|
|||b|
|log of a power|log (a|) = n log (a)|

amplification removes most of the noise. This ensures that the signal-to-noise ratio remains high.

*n*

**318** **WORKED EXAMPLE**

**4** A signal of power 18.0 mW passes along one cable, where the attenuation is 20 dB. It then passes along another cable, where the attenuation is 30 dB. What is the power at the end of the two cables?

**Step 1** Apply the decibel equation to each cable in turn.

In the first cable, if the input is *P₁* and the output *P₂*, then: <u>P₁</u> 20 = 10 lg *P₂*

**Hint**: *Notice that both sides of the equation produce a* *positive number since P₁ > P₂.*

In the second cable, the input is *P₂*, the output of the first channel. If the output is *P₃*, then: <u>P₂</u> 30 = 10 lg *P₃*

**Step 2** Add the two equations; this gives:

<u>P₁ P₂</u> 50 = 10 lg + lg *P₂ P₃*

Applying the ‘log of a product rule’ gives: <u>P₁ P₂ P₁</u> 50 = 10 lg × = 10 lg *P₂ P₃ P₃*

This shows that the total attenuation of the two cables is 50 dB, equal to the sum of the attenuations of the consecutive channels. Hence you can add attenuations to find the total attenuation (but be careful if a signal is being both amplified and attenuated).

**Step 3** We have *P₁* = 18 mW and we need to find *P₃*. Substituting gives: <u>18</u> 50 = 10 lg *P₃* so: <u>18 50</u> lg *P* = 10 = 5 3

Taking inverse logs, or pressing the inverse lg button on your calculator, gives: <u>18</u> 5 = 10 *P₃* *P₃* = 1.8 × 10 −4 mW

You could apply the decibel equation to each cable in turn and use the output of the first cable as the input to the second cable. You should find that the result is the same.

##### WORKED EXAMPLE

**5** The input signal to a cable has power 1.2 × 10 −3

W.
The signal attenuation per unit length in the cable is 14 dB km −1 and the average noise level along the cable is constant at 1.0 × 10 −10

W. An acceptable
signal-to-noise ratio is at least 30 dB.

Calculate the minimum acceptable power for the signal and the maximum length of the cable that can be used without a repeater.

**Step 1** The signal-to-noise ratio must be at least 30 dB. Hence, using: <u>signal power</u> signal-to-noise ratio = 10 lg noise power we have: <u>P</u> 30 = 10 lg−10 1 × 10

where *P* is the minimum acceptable power. Solving for *P* gives: = 1.0 × 10 −7 W

**Step 2** A repeater is needed to regenerate the signal when the signal-to-noise ratio falls to 30dB, i.e. its power is 10 times the noise level, and this is 3

1.0 × 10 −7
W. We can calculate the attenuation
needed to reduce the signal to this level:

<u>1.2 × 10</u> −3
attenuation = 10 lg 1.0 × 10−7

= 41 dB <u>41</u> Hence the length of cable is = 2.9 km. 14 If the cable is 10 km in length, the total attenuation is: 14 dB km −1 × 10 km = 140 dB.

The signal of power 1.2 × 10 −3 W is attenuated to a power *P* where:

<u>0.0012</u>
140 = 10 lg *P* *P =* 12 × 10 −17 W

You can see that the power in the signal is much smaller than the minimum acceptable power – it is even smaller than the noise level. The signal-to-noise ratio is now 10 lg (12 × 10 −17 / 1.0 × 10 −8 ) = −79 dB, smaller than the acceptable +30 dB. A repeater is needed well before the end of the 10 km of cable.

##### QUESTIONS

**13** A signal has an input power 5.0 mW and an output power of 0.000 2 mW. What is the attenuation in dB?

**14** The attenuation of a 6.0 mW signal is 30 dB. What is the final power?

**15** What is the signal-to-noise ratio when the signal and the noise have equal power?

**16** A signal of 1.0 mW passes through an amplifier of gain 30 dB and then along a cable where the attenuation is 18 dB. **a** What is the overall gain of the signal in dB? **b** What is the output power at the end of the cable?

## Comparison of different channels

Each type of signal channel has its good points and its disadvantages, which we will now consider. **319**

### Wire-pairs and coaxial cables

The earliest telephones used a pair of wires strung on either side of a pole (Figure 20.13). As the use of electricity became more common, the amount of electrical interference increased, causing crackle and hiss on the line. The potential difference between the two wires is the signal. Each wire acts as an aerial, picks up unwanted electromagnetic waves and distorts the signal.

**Figure 20.13** An early telegraph pole.

When two wires are close together, each wire picks wire-pair, it can transmit data faster, over longer distances, up an equal amount of electrical interference. There is no and with less electrical interference. Coaxial cable often additional potential difference between the two wires and connects a radio transmitter to an aerial, as coaxial cable so having the wires close together reduces the interference. has a high bandwidth, which can exceed 100 MHz with a

Figure 20.14 shows a twisted wire-pair with the wires close

cable 30 m in length. It is also slightly more difficult to ‘tap’ together. The connection from your telephone to a socket into a coaxial cable than into a wire-pair. nearby is likely to use two insulated copper wires placed

Table 20.3 summarises the advantages and

close together or, more likely, a twisted pair of wires. disadvantages of wire-pairs and coaxial cable.

insulation

copper

insulation

finely woven copper wire (braid)

**Figure 20.15** Coaxial cable.

**Figure 20.14** Twisted wire-pairs in a computer network.

A wire-pair is by far the cheapest transmission medium

|Wire-pairs|Coaxial cable|
|---|---|
|are cheap and convenient|is more expensive|
|strongly attenuate a signal|is less attenuating|
|have low bandwidth|has higher bandwidth|
|pick up some noise and|has less electrical interference|
|interference|and noise|
|suffer from crosstalk|has little crosstalk|
|have low security|is more secure|

but it does have some disadvantages. **320** The changing currents in the wires themselves produce electromagnetic (EM) fields and this makes the wires act as aerials, radiating EM waves. The energy to emit these waves reduces the strength of the signal sent along the wire. As the frequency of the changing current increases, the emission of EM waves increases and so the bandwidth of wire-pairs is low. Energy is also lost in the wires due to electrical heating in the resistance of the wires. Wire-pairs are often close together in a telephone system and EM waves pass from one wire-pair to another. This is the origin of some forms of crosstalk, where you can hear another telephone conversation. Wire-pairs are easily ‘tapped’. A connection made to each wire allows an unwanted person to hear a telephone conversation. The security of a wire-pair is low. Coaxial cable, as shown in Figure 20.15, reduces the amount of crosstalk in wire-pairs when transmission occurs at high speed. The copper core and the finely woven copper wire or braid are the two conductors that transmit the signal. The braid is usually connected to earth, so, ideally, the potential of this wire does not change. Electromagnetic (EM) waves do not pass easily through metal and so the braid provides a screen or barrier that reduces the interference that reaches the copper core. An ideal coaxial cable also prevents any emission of EM waves at radio frequencies and has less attenuation than a wire-pair. Although coaxial cable is more expensive than a

**Table 20.3** Comparison of wire-pairs and coaxial cable.

### Radio waves and microwave links

Radio waves can travel by a number of different paths from a transmitter to a receiver, as shown in Figure 20.16.

Sky waves greater than 30MHz are known as space waves. They pass through the ionosphere.

ionosphere

Sky waves up to 30MHz are reflected by the ionosphere.

Surface waves diffract around the Earth.

**Figure 20.16** Radio wave transmissions.

||Frequency range|Communication method and waveband|Distance travelled|
|---|---|---|---|
|surface wave|up to 3 MHz|LW and MW radio in the LF band|up to 1000 km|
|sky wave|3–30 MHz|SW radio in the HF band|worldwide by reflection|
|space wave|30–300+ MHz|FM radio in the VHF band, TV and mobile phones in the UHF band|line-of-sight|
|microwave|1–300 GHz|microwave, satellite links and Wi-Fi in the super- high-frequency (SHF) and extra- high-frequency (EHF) bands.|line-of-sight except when retransmitted by satellite|
|Table 20.4|Data for radio and microwaves. increases the distance of transmission.|The radio wave given out by a transmitting aerial travels in all directions. The atmosphere absorbs the wave, the amount of absorption depending on the radio frequency. The distance travelled by a radio wave therefore varies with its frequency. In some cases, the aerial focuses the radio waves towards the receiver by using an aerial shaped as a dish, as shown in Figure 20.17. Without such a dish, the strength of the signal decreases strongly with distance. The microwave tower shown in Figure 20.17 holds a number of parabolic reflectors or dishes. Each dish points towards a dish on another tower some miles away and they transmit microwaves back and forth between them. The transmission is line-of-sight and the height of the tower||

Surface (ground) waves travel close to the surface of the Earth. Lower frequencies, up to 3 MHz, diffract around the surface of the Earth because of their long wavelengths; this gives them a long range of up to 1000 km. AM broadcasts in the medium-wave (MW) and long-wave (LW) bands travel efficiently as surface waves. Sky waves are waves above 3 MHz in frequency, which are diffracted only a little by the Earth and travel almost in straight lines. Some waves at these frequencies travel for a short distance as surface waves, but they can only travel about 100 km in this way. Sky waves that travel in the atmosphere may be reflected from a layer of charged particles known as the ionosphere. When these reflected waves reach the Earth’s surface they may be reflected back to the ionosphere. Through multiple reflections by the ionosphere and the ground, sky waves can travel for large distances around the Earth. Because the density of charged particles in the ionosphere is constantly changing, the reflection of sky waves is not reliable. Short-wave (SW) radio uses frequencies in the high-frequency (HF) band that reflect from the ionosphere. Your radio set can receive distant SW radio stations at night, when the frequencies reflected by the ionosphere are not absorbed by other regions in the atmosphere. **321** Space waves are sky waves with a frequency greater than 30 MHz, which pass through the ionosphere. The transmission is line-of-sight, so, if the receiver and transmitter are on the Earth’s surface, there must be a clear line between the receiver and the transmitter (not blocked by hills or mountains). Some police and emergency services, as well as television transmissions, use space waves with frequencies above 30 MHz in the very-high-frequency (VHF) and ultra-high-frequency (UHF) bands. The boundary between radio waves and microwaves is not clearly defined, although frequencies above 1 GHz are generally described as microwaves. Microwaves are able to pass through the ionosphere to **R R** reach satellites in space. Bluetooth technology and Wi-Fi use microwaves for communication around the home. **R** Using Wi-Fi, microwaves link your laptop to the main computer in your home.

Table 20.4 is a summary of the frequencies used for the

different radio transmissions and the distances travelled. The wavelength of any radio wave can be found using the 8 −1 formula *c* = *f λ* where *c* = 3.0 × 10 ms, which is the speed of the radio wave and the speed of light. So, for example, a wave of frequency 1 GHz has a wavelength of:

<u>3.0 × 10</u>
*λ* = = 0.3 m 1 × 10

**Figure 20.17**

A microwave tower.

The bandwidth available increases as the frequency of the wave increases. As microwaves have a high bandwidth, they can carry many telephone conversations at once. They are also very secure and difficult to tap into, as the beam of microwaves that travels between the two dishes is narrow and does not spread out. Until fibre optic cable was available, microwave links carried the majority of long- distance telephone conversations. To summarise, high-frequency radio waves and microwaves: ■■ have high bandwidth and can carry a large amount of information ■■ can be transmitted as narrow beams which are more secure ■■ are line-of-sight and often use a satellite or microwave link.

### Satellites and optic fibres

Transmissions in the LW and MW bands use a surface wave and do not travel further than about 1000 km. For long-distance communication, it is possible to transmit using a sky wave or using a space wave and a satellite. Figures 20.1 and 20.18 both show a communications satellite in space. The satellite receives a space wave from a transmitter on Earth, the uplink, with a carrier frequency **322** in the microwave region. Because the satellite can only reflect a tiny fraction of the signal sent from Earth, the reflected signal received back on Earth would be far too small. Instead, the satellite re-transmits the signal it receives as the downlink back to Earth, on another frequency and with more power than it received. If the downlink and uplink frequencies were the same, then the much larger signal sent from Earth would swamp the signal sent from the satellite, so different frequencies are used. The satellite transmits the signal back to an individual satellite dish back on Earth or to many dishes, over a wide area, particularly when broadcasting television programmes. The first communications satellites used a frequency of 6 GHz for the uplink and 4 GHz for the downlink, but now even higher frequencies are used.

Here are some advantages of communication by satellite rather than by sky wave: ■■ The concentration of ions in the ionosphere is constantly changing and reflection of the sky wave is not always possible; sometimes layers in the ionosphere even absorb radio frequencies. ■■ The satellite boosts the signal for its return to Earth and provides a stronger signal than is obtained by reflection from the ionosphere. ■■ Satellite communication uses higher frequencies, which have higher bandwidth and can carry more information per second. ■■ Only a few frequencies in the MW and SW bands are available. More frequencies are available for communicating if a satellite uses higher frequencies.

In order to obtain a constant link between the satellite and the satellite dish on Earth, it is essential that the satellite dish always points towards the satellite. If the satellite moves across the sky, the dish must move to track the movement of the satellite. To avoid this problem many communications satellites rotate around the Earth in a geostationary orbit. They orbit the Earth in the same direction as the Earth rotates, at a height of 36 000 km above the Earth’s surface. At this height, each satellite has a period of rotation of 24 hours. This means that each satellite naturally takes 1 day to orbit the Earth, exactly the time that it takes a point on the surface of the Earth to make one complete rotation. A geostationary satellite is in orbit above the equator and it never appears to move when viewed from any point on the Earth. The satellite does not rotate with the same **speed** as a point on the Earth because its orbit is far larger than the circumference of the Earth. There are many other satellites around the Earth. Some of these are in polar orbit. These satellites commonly travel above the North and South Poles in a time much shorter than a day. They are usually closer to the Earth than geostationary satellites and are used for surface observation and as weather satellites. At a commonly used height of 1000 km above the Earth’s surface, the period of rotation around the Earth is only 100 minutes. Being closer to the Earth, polar-orbit satellites can see smaller detail when used for observation and espionage. As they orbit from the North to the South Pole, the Earth rotates underneath them and so

|uplink|satellite downlink|
|---|---|
|satellite dish|satellite dish|

they pass over the whole Earth in a 24-hour period. There is always a delay in sending a message to a satellite because the satellite is high above the Earth. This delay can be annoying when talking by telephone. For example, if the satellite is directly overhead and the signal travels a distance of 72 000 km up to the satellite and then down to the other person, the time delay is 0.24 s. The reply

**Figure 20.18** A satellite system.

**Figure 20.19** An optic fibre

passing through the eye of a needle, and its internal structure.

optic fibre cladding

from the other person also takes 0.24 s and so there always seems to be a delay of at least 0.48 s in the conversation. Geostationary satellites used for communication can transmit to each other around the world but they cannot always receive from regions close to the poles, as the curvature of the Earth blocks the signal. Th e delay when communicating with a polar satellite is much smaller but you may have to wait until the satellite is overhead to transmit or receive. Th e features of a geostationary satellite are: ■■ the satellite rotates with the same period as the Earth ■■ the satellite is in orbit above the equator with a period of 1 day ■■ the satellite appears to remain fixed in position above a point on the equator and so satellite dishes do not need to be moved.

Compared to a geostationary satellite, a satellite in polar orbit: ■■ travels from pole to pole, with an shorter period of orbit ■■ is at a smaller height above the Earth and can detect objects of smaller detail ■■ is not always in the same position relative to the Earth and so dishes must be moved ■■ has smaller delay times.

An alternative for long-distance communications is the optic fi bre, a very thin glass or plastic fi bre that carries light or infrared. Optic fi bres use glass and infrared for long distances, rather than plastic or light, as the glass can be very pure and does not absorb or scatter infrared. As optic fi bres have very low signal attenuation, the distance between repeater amplifi ers can be high.

Figure 20.19 shows a photograph of a number of optic

fi bres and the internal structure of one fi bre. Th e three rays of light are totally internally refl ected from one end of the fi bre to the other. When used for communication, an electrical signal causes a laser or a light-emitting diode (LED) to emit pulses of light or infrared, with a frequency of the order of 2 × 10 14 Hz (2 × 10 8 MHz). Because the frequency is so high, the potential bandwidth available is also very high. Th e pulses of light or infrared provide the digital signal that passes along the fi bre. With a cable containing more than a hundred fi bres and each fi bre carrying a large number of pulses per second, the whole cable can carry ten million telephone conversations at the same time. Fibre optic cables have replaced the use of satellites for long-distance transmission. Just a few fi bre optic cables running across the oceans and from city to city link almost the whole world and make the internet possible – the ‘information superhighway’. Th e delay between

transmission and reception is less than with a satellite as the distances travelled round the world by the signal are less than up to a satellite and back down again. Th e disadvantages of fi bre optic cables are that an electrical signal must fi rst be converted to pulses of light and the optic fi bres are diffi cult to connect to one another as two fi bres cannot just be glued together. Compared to a metal cable, a fi bre optic cable: **323** ■■ has much greater bandwidth and can carry more information per second ■■ has less signal attenuation, so repeater and regeneration amplifiers can be further apart ■■ is more diff icult to tap, making the data it carries more secure ■■ does not suff er from electrical interference and crosstalk ■■ weighs less and so large lengths can be handled more easily ■■ is immune to lightning and the eff ects of nearby power lines ■■ can be used in flammable situations as no sparks are produced ■■ is cheaper than the same length of copper wire.

##### QUESTION

**17** A television signal can be transmitted using a **coaxial cable** to pass an **analogue signal**, using a **space wave** in the UHF band, using a **sky wave** linked to a satellite or using fibre optic cable and the internet. **a** Explain what is meant by the terms in **bold** type. **b** State approximate values for the frequencies and wavelengths used by the carrier wave in each case. **c** Give **one** advantage and **one** disadvantage of each of these four methods.

#### Cambridge International A Level Physics

## Summary

■■ ■■

|Modulation varies either the amplitude or frequency|Regeneration removes noise and interference from||
|---|---|---|
|of a carrier wave to carry information in the signal.|digital signals.||
|Bandwidth is the range of frequencies present in a|For good reproduction of a signal, the sampling rate||
|broadcast signal.|and number of bits should be high.||
|FM broadcasts have higher bandwidth and sound|Wire-pairs, coaxial cables, radio waves, microwaves||
|quality than AM.|and optic fibres transmit signals.||
|Analogue and digital signals transmit information.|Attenuation of a signal is measured in dB, where||
|Analogue-to-digital conversion (ADC) turns analogue|number of dB = 10 lg|P₁.|
|signals into digital signals and digital-to-analogue||P₂|
|conversion (DAC) turns them back again.|Satellites for communication are oft en in geostationary||

■■ ■■

■■ ■■

■■ ■■ ■■ ■

■■ or polar orbits.

## End-of-chapter questions

**324** **1 a** Draw a sketch graph of an AM wave and use your graph to explain how the AM wave has been formed from the carrier wave and a signal. Refer to the frequencies involved. [4] **b** Draw a sketch graph of an FM wave and use your graph to explain how the FM wave has been formed from a carrier wave and a signal. Refer to the frequencies involved. [4]

**2** The output of a microphone is an analogue signal with a bandwidth of 3.4 kHz. **a** Explain what is meant by **i analogue** [2] **ii bandwidth**. [1] **b** Compare the bandwidth of the microphone with the typical range of frequencies that can be heard by the human ear. Comment on the diff erence between the two values. [2]

**3** An LED provides input power of 1.26 mW to an optic fibre of length 60 m. The output at the other end of the fibre is 1.12 mW. **a** Calculate the attenuation in the optic fibre. [2] **b** Calculate the attenuation per unit length in the optic fibre. [2] −1 **4** The signal attenuation per unit length of an optic fibre is 0.30 dB km. An input signal to the optic fibre is 100 dB above the noise level. The level of the noise remains constant along the optic fibre at 6.0 pW.

Calculate: **a** the power of the input signal to the optic fibre [3] **b** the maximum length of the optic fibre used, if the signal at the end of the fibre is to remain at least 30 dB above the noise level. [2]

|5 a b c 6 a b c i 7 8|State ii|one advantage and Figure 20.15 shows a coaxial cable. Explain what is meant by State two|Describe the orbit of a geostationary satellite. State a typical wavelength for communication between the Earth’s surface and a geostationary satellite. one disadvantage of the use for telephone communication of a geostationary satellite compared with a satellite in polar orbit. State and explain the purpose of the fine woven copper wire or braid. Optic fibre has a larger bandwidth than a coaxial cable. Explain why increased bandwidth has reduced the cost of telephone calls to distant countries. electrical noise. [1] causes of noise in a copper cable. Radio signals may be transmitted by surface (ground) waves, by space waves or by sky waves. State a typical value for the frequency and the maximum distance of transmission for each type of wave. Figure 20.20 shows an amplitude-modulated radio wave carrying a signal.|[2] [1] [4] [2] [1] [2] [6]|
|---|---|---|---|---|
|||80 µs|80 µs|325|
|a b c|Figure 20.20||For End-of-chapter Question 8. Determine the radio frequency of the carrier wave. Calculate the frequency of the signal. Draw the frequency spectrum of the modulated radio wave|[2] [2] [3]|

#### Cambridge International A Level Physics

|9|||||Figure 20.21 shows the variation with time of a signal voltage,|V, over a 5-hour period.||
|---|---|---|---|---|---|---|---|
||V / V 5 4 3 0 a b V|Figure 20.21|1 give the value of|2 For End-of-chapter Question 9. V|3 State the name of the type of signal shown in the diagram.|4 Time / hours The signal is turned into a digital signal with 4-bit binary numbers. The value of is 3 V and each subsequent binary unit represents an extra 0.2 V. Copy and complete the table to as a decimal number and as a binary number for times of 0, 2 and 4 hours.|[1] V is (0000) when [3]|
|326|||Time / hours|V|/ V (decimal)|V / V (binary)||
||||0|||||
|10|c i ii a i ii|Calculate:|2 4 of the cable is 10 dB km|Explain why this is the case. −1 the total attenuation caused by the cable the total gain caused by the amplifiers.|Explain how the sampling process can be improved.|The digital signal that is produced cannot be used to produce a perfect reproduction of the original signal. A cable of length 20 km signal transmits a signal from one end to the other. The attenuation per unit length. Four repeater amplifiers along the cable each have a gain of 40 dB.|[2] [2] [1] [1]|
|11|b c a b c||Describe the key features of a two signals is so diff erent.||transmits a downlink signal back to Earth at a frequency of 11 GHz.|The input signal has power 200 mW. Calculate the output power of the signal from the cable. Calculate the output power of the signal from the cable if repeater amplifiers are not used. A communications satellite in geostationary orbit receives an uplink signal at a frequency of 14 GHz and geostationary satellite. Suggest a reason why diff erent frequencies are used for the uplink and the downlink. The uplink signal has a power of 2 kW and the downlink signal 20 W. Suggest why the power in the|[2] [1] [2] [1] [1]|
