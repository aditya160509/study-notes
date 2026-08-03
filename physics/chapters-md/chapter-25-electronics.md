# Chapter 25: Electronics

**386**

## Learning outcomes

##### You should be able to:

■■ understand how electronic sensing devices are used to produce an output voltage ■■ describe the function of the following sensors: light-dependent resistor (LDR), negative temperature coeff icient thermistor, piezo-electric transducer, metal-wire strain gauge ■■ recall the main properties of an ideal operational amplifier (op-amp) ■■ understand the use of an op-amp as a comparator, and as an inverting and non-inverting amplifier ■■ recall the circuit diagrams and calculate the voltage gain of inverting and non-inverting amplifiers for a single signal input ■■ understand output devices used in electronic circuits, such as the light-emitting diode (LED), the relay and calibrated analogue and digital meters

##### Chapter 25: Electronics

## Electronic devices

##### Electronic devices are widespread in the modern world. From birth to death, electronic sensors watch

**over and control many of our environments. The chances of survival of the newborn baby in Figure**

**25.1 are improved as a sensor inside the incubator measures the temperature of the air. The output of the**
##### sensor operates heating and cooling devices which keep the temperature as constant as possible. Other

##### sensors sound alarms if the baby’s breathing or heart rate falls to dangerous levels.

**In this chapter, we will explore how some common electronic sensors work. You will use what you have**

##### learned about electricity and electric circuits in

**Chapters 8–12. Figure 25.1** A newborn baby in an incubator. Sensors inside the incubator monitor and control the temperature, oxygen and humidity levels.

## Components of an electronic sensing system

|In its basic form, an electronic sensor may be represented||in knowing the output for various inputs and how the|
|---|---|---|
|as a sensing device, a processor that provides an output||sensor can be used in a range of useful applications.|
|voltage, and an output device (Figure 25.2).||Sensors make use of many basic ideas about electric circuits: resistance and current, for example. A processor|
|sensing|output|may contain many transistors, but it is not necessary|
|device|device|to understand how a transistor works to appreciate the function of a processor. Some detail will be given, but if|
|Figure 25.2||you wish to delve further into how these devices work, there are many useful websites that will help you to|
|The sensing device is an electronic component with||understand how physicists have used their knowledge and|
|a property that changes when a physical quantity such||inspiration to good effect.|
|as temperature or light intensity alters. We have already||The sensing device is sometimes called a transducer.|
|looked at one such component, the thermistor (Chapter||A transducer changes energy from one form into another.|
|changes. A similar component, called a light-dependent||into electrical energy. However, even the thermistor used|
|resistor (LDR), has a resistance that changes when the light||as the sensing device in the incubator in Figure 25.1 can|
|level alters. This change in resistance causes the processor||be thought of as a transducer; a change in the internal|
|to produce an output voltage that drives the output device.||energy of the air alters the electrical energy in the|
|In this way the change in a physical quantity such as resistance can be used to trigger the output device. When the air in the incubator in Figure 25.1 becomes cold, the||thermistor circuit.|
|change in resistance of the sensor causes the processor||Some crystals such as quartz produce an electric field|
|to switch on the output device, a heater, to keep the baby||when a force is applied and the shape of the crystal|
|warm. When it becomes too hot, the same sensing device||changes. This is known as the piezo-electric effect. A|
|and processor will switch the heater off.||piezo-electric crystal consists of positive and negative ions|
|It is important to note that we are not concerned with||in a regular arrangement. When the crystal is stressed, a|
|all the details of how a particular sensing device works or||small voltage is produced between the faces of the crystal.|
|what there is inside the processor. We are only interested||The crystal acts as a transducer since energy is changed|

11), with a resistance that changes when temperature A microphone is an obvious example, as it changes sound

**387**

processor

Block diagram of an electronic sensor.

### Piezo-electric transducers

from one form to another. There is more about piezo- How is an LDR used as a sensing device? A voltage electric transducers in Chapter 32, where their use in is needed to drive the output device, yet the LDR only ultrasound scanning is described. produces a change in resistance. The sensor must use this For use in a microphone, the piezo-electric crystal is change in resistance to generate the change in voltage. The made into a thin sheet with metal connections on opposite solution is to place the LDR in series with a fixed resistor, sides. When a sound wave hits one side of the sheet, as shown in Figure 25.5. the compressions and rarefactions cause the pressure The voltage of the supply is shared between the two to increase and decrease. The crystal changes shape in resistors in proportion to their resistance, so as the light response to these pressure changes and a small voltage level changes and the LDR’s resistance changes, so does the is created across the connections. Figure 25.3 shows the voltage across each of the resistors. The two resistors form symbol for a microphone. a potential divider, one of the practical circuits discussed in Chapter 12.

3.0 kΩ
10 V

*V* out

**Figure 25.3** The symbol for a microphone.

Acoustic guitars and other instruments often use a piezo-electric transducer to produce an electrical output. The microphone is stuck to the body of the guitar and the electrical output can be amplified and played back through loudspeakers.

### The light-dependent resistor (LDR)

**388** A **light-dependent resistor (LDR)** is made of a high- resistance semiconductor. If light falling on the LDR is of high enough frequency, photons are absorbed by the semiconductor. As some photons are absorbed, electrons are released from atoms in the semiconductor. The resulting free electrons conduct electricity and the resistance of the semiconductor is reduced. The graph in Figure 25.4 shows the variation of the resistance of a typical LDR with light intensity. Only a narrow range of light intensity, measured in lux, is shown. A typical LDR will have a resistance of a few hundred ohms in sunlight, but in the dark its resistance will be millions of ohms.

80 Ω 60

40 Resistance / k 20

**Figure 25.5** An LDR used in a sensor.

##### WORKED EXAMPLE

**1** Using the graph in Figure 25.4, calculate *V*out in

Figure 25.5 when the light intensity is 60 lux.

**Step 1** Find the resistance of the LDR at 60 lux. *R* = 20 kΩ LDR **Step 2** Divide the total voltage of 10 V in the ratio 3 : 20. The total number of parts is 23 so: 20 *V* out = × 10 = 8.70 V 23

**Hint:** *The answer on your calculator might be 8.69565.* *When you give your answer to 3 significant figures, do* *not write 8.69 – you must round correctly.*

Light intensity / lux

**Figure 25.4** Resistance plotted against light intensity for

an LDR.

##### QUESTIONS

**1** What is the voltage across the 3.0 kΩ resistor in

Figure 25.5 when the light intensity is 10 lux?

**2** The circuit shown in Figure 25.5 produces a decreasing output voltage when the light intensity increases. How can the circuit be altered to produce an increasing output voltage as the light intensity increases?

##### QUESTIONS

**3** Explain how a thermistor can be used as a transducer.

**4** State **two** similarities between an LDR and a thermistor.

**5** Design a circuit using the thermistor in Figure 25.6 that uses a cell of 10 V and produces an output voltage of 5 V at 50 °C. Explain whether the voltage output of your circuit increases or decreases as the temperature rises.

### The thermistor

The thermistors that we deal with are known as **negative** **temperature coefficient** thermistors. This means that when the temperature rises, the resistance of the thermistor falls. This happens because the thermistor is made from a semiconductor material. One property of a semiconductor is that when the temperature rises the number of free electrons increases, and thus the resistance falls.

Figure 25.6 shows a graph of the resistance of a

thermistor and the resistance of a metal wire plotted against temperature. You can see that the resistance of a metal wire increases with increase in temperature. A metal wire is not a negative temperature device, but it could be used as a sensing device. A thermistor is more useful than a metal wire because there is a much larger change in resistance with change in temperature. However, the change in resistance of a thermistor is not linear with temperature; indeed, it is likely to be an exponential decrease. This means that any device used to measure temperature electronically must be calibrated to take into account the resistance–temperature graph. The scale on an ordinary laboratory thermometer between 0 °C and 100 °C is divided up into 100 equal parts, each of which represents 1 °C. If the resistance of a thermistor were divided like this, the scale would be incorrect. The thermistor can be used as a sensing device in the same way as an LDR. Instead of sensing a change in light level, it senses a change in temperature.

Ω 600

thermistor 400 Resistance / metal wire 200

0 0 50 100 150 Temperature / °C

**Figure 25.6** Variation of resistance with temperature.

### The metal-wire strain gauge

A **strain gauge** takes advantage of the change in resistance of a metal wire as its length and cross-sectional area change. When stretched, a metal wire becomes narrower and longer; both these changes increase the electrical resistance. When compressed, a metal wire becomes shorter and wider; as long as it does not buckle, these changes decrease its electrical resistance.

Figure 25.7 shows the structure of a strain gauge. A thin

metal wire is placed between thin sheets of plastic. The **389** metal wire zigzags up and down its plastic base so that the length of wire used is longer than the actual strain gauge.

plastic

metal wire

connecting leads

**Figure 25.7** A metal-wire strain gauge.

Strain gauges are used in many situations. For example, an engineer may find a crack in a wall and want to know whether the crack is growing bigger. By sticking a strain gauge over the crack the engineer can measure the resistance many days or even years later and see if there has been any movement. A gauge used in a dynamic experiment may measure the stress changes in an aircraft wing. A processor is used to produce a voltage output and show changes in length as

##### WORKED EXAMPLE

**2** The wire in a strain gauge when unstretched has length 10.00 cm and resistance 120.0 Ω. When the wire is stretched by 0.10 cm, the resistance becomes

122.4 Ω. The strain gauge is connected in the circuit shown in Figure 25.8. What is the change in length of the wire in the strain gauge when the output voltage is 5.06 V?

||120.0 Ω|
|---|---|
||strain gauge|
|R s 5.06 V : 4.94 V and so: 5.06 × 120 = 122.9 Ω 4.94 R₂|Circuit for Worked example 2. Determine the resistance of the strain by considering the two resistors as a potential divider. The 10 V supply is split in the ratio Alternatively, apply the potential divider formula|
|× V R₁ × R₂ 120|in|

10.0 V
d.c.
output voltage

**Figure 25.8**

**Step 1** gauge

*R*s =

they happen. This provides important information when an aircraft is tested. In Chapter 11, we saw that a wire of length *L*, cross- sectional area *A* and resistivity *ρ* has a resistance *R* given by: <u>ρL</u> *R* = *A* What happens to the resistance when the wire is stretched depends on the construction of the strain gauge. The simplest approximation is to assume that the cross- sectional area of the wire remains unchanged. If the wire increases in length by a small amount δ*L* and the cross-sectional area *A* is unchanged, then the resistance of the wire increases by δ*R*, where: <u>ρ(L+ δL)</u> *R* + δ*R* = *A* Subtracting the two equations gives: <u>ρδL</u> δ*R* = *A* <u>ρL</u> If the expression is divided by *R* =, we get: *A* <u>δR δL</u> = *R L* When a wire is stretched not only does its length increase; at the same time, its area decreases (because its volume **390** remains roughly constant). This also increases the wire’s resistance. The increase in resistance can be shown to be the same as that caused by the increase in length so that, for small changes: 2*ρ*δ*L* δ*R* 2δ*L* δ*R* = or = *A R L* In either case, the change in resistance is directly proportional to the increase in length, δ*R*∝ δ*L*. The change in resistance is likely to be very small but with a suitable series resistor and a cell used as a sensor, the change in length can produce a measurable change in output voltage.

##### QUESTION

**6** Using the data given in Worked example 2: **a** calculate the increase in length of the wire when the output voltage is 5.1 V **b** calculate the strain in the wire when the output voltage is 5.1 V **c** calculate the output voltage when the wire is stretched by 0.05 cm.

*V* out =

4.94 = 120 +*R*
× 10.0 s

It is easier to use 4.94 V, the voltage across the 120 Ω resistor. This gives a value for *R*s of 122.9 Ω.

**Step 2** The resistance of the wire has increased by

2.9 Ω. Since δ*R*∝ δ*L*, and an increase in length of
0.10 cm increases the resistance by 2.4 Ω, the length has increased by:
<u>2.9</u> × 0.10 = 0.12 cm
2.4 If the strain gauge is glued to a metal support, the strain in the metal support is the same as the strain
<u>0.12</u>
in the gauge, in this case = 1.2%. Thus the strain 10 gauge can easily measure strain.

||||||||||Chapter 25: Electronics||
|---|---|---|---|---|---|---|---|---|---|---|
|||BOX 25.1: Potential dividers in use|||||||||
|■■ ■■|decreases|used as sensors because: (NTC) thermistor|Potential divider circuits are often used in electronic circuits. They are useful when a sensor is connected to a processing circuit. Suitable sensors include thermistors and light-dependent resistors (Figure 25.9). These can be the resistance of a negative temperature coefficient decreases the resistance of a light-dependent resistor (LDR) as the incident intensity of light|as its temperature increases|a 1.5 V increases.|R₁ R₂|V|b 1.5 V|R₁ R₂|V out|
|a|||b||||out||||
|Resistance 0 0||thermistor 100 Temperature / °C|Resistance 0 0|light-dependent resistor Light intensity|Figure 25.10|circuit. The output voltage variable resistor, or b|V out temperature characteristics of such a circuit using a datalogger (Figure 25.11). The temperature probe of the datalogger records the temperature of the water bath and the second input to the datalogger records the voltage output of the potential divider circuit.|Using a thermistor in a potential divider may be a across the thermistor.|across the|391|
|a b voltage V out|Figure 25.9 intensity of light. V out the variable resistor over which|potential divider circuit to provide an output circuit to provide an output voltage on the intensity of light. increases. If the output voltage R₂ V out|Two components with variable resistances: the thermistor’s resistance changes with temperature; the light-dependent resistor’s resistance depends on the This means that a thermistor can be used in a which depends on the temperature. A light- dependent resistor can be used in a potential divider Figure 25.10 shows how a sensor can be used in a potential divider circuit. Here, a thermistor is being used to detect temperature, perhaps the temperature of a fish tank. If the temperature rises, the resistance of the thermistor decreases and the output voltage thermistor, as shown in Figure 25.10b, it will decrease as the temperature rises. By changing the setting of varies. This would allow you to set the temperature at which a heater operates, for example. When designing a practical circuit like this, it is necessary to know how the voltage output depends on the temperature. You can investigate the voltage against|V which depends out V is across the out, you can control the range|Figure 25.11|of p.d. against temperature.|characteristics of a thermistor in a potential divider circuit. During the experiment, the screen shows how temperature and output voltage change with time. After the experiment, the same data can be displayed as a graph|Using a datalogger to investigate the|||

important. Electronic devices such as transistors and integrated circuits draw only very small currents, so potential dividers are very useful where these devices are used. Where large currents are involved, because there will be some current through both *R₁* and *R₂*, there will be wasted power in the resistors of the potential divider circuit.

##### QUESTIONS

**7** An NTC thermistor is used in the circuit shown in **9** The light-dependent resistor (LDR) in Figure 25.13

Figure 25.12. The supply has an e.m.f. of 10 V and

has a resistance of 300 Ω in full sunlight and 1 MΩ in negligible internal resistance. The resistance of the darkness. What values will the output voltage *V*out thermistor changes from 20 kΩ at 20 °C to 100 Ω at have in these two conditions? 60 °C. Calculate the output voltage *V*out at these two temperatures.

300 Ω

**392** 1 kΩ 12 V 10 V

*V* out *V* out

**Figure 25.12** Thermistor used in a potential divider

##### BOX 25.1: Potential dividers in use (continued)

The temperature can be raised rapidly by pouring amounts of water into the water bath. The datalogger then records both temperature and voltage and the computer gives a display of the voltage against temperature. Dataloggers are very good at processing the collected data. Potential divider circuits are especially useful in circuits with very small currents but where voltages are

**Figure 25.13** For Question 9.

**10** A potential divider circuit is required which will give an output voltage that increases as the temperature increases. A thermistor is to be used whose resistance decreases as the temperature increases. Draw a suitable circuit for the potential divider, showing the connections for the output voltage.

circuit. For Questions 7 and 8.

**8** The thermistor in Figure 25.12 is replaced with a light- dependent resistor (LDR). Explain whether the output voltage *V*out will increase or decrease when a bright light is shone on to the LDR.

## The operational amplifier (op-amp)

Operational amplifiers (op-amps) are among the most widely used electronic devices today, being used in a vast array of consumer, industrial and scientific devices. The amplifier is the basic building block of many electronic systems. The electrical output from the musicians in the concert shown in Figure 25.14 must be amplified before it can be passed to the loudspeakers and turned into sound. An amplifier produces an output with more power and usually more voltage than the input. A perfect amplifier should produce an exact copy of the input. In particular, the different frequencies produced by the musicians and their instruments must be amplified by the same amount. If, for example, high-frequency notes are made louder than low-frequency notes then the whole performance will be altered. You may have noticed that people sound different when talking on the telephone. This is often because some frequencies are not amplified as much as others.

other is marked (+) and is known as the **non-inverting** **input**. The one function of this device is to use the potential difference between the two inputs to produce as large an output voltage *V* as possible. *V* − is the potential out at the inverting input (−) and *V* + is the potential at the non-inverting input (+).

+9 V *V* – – *V* out *V* + + –9 V

**Figure 25.15** An operational amplifier and its symbol.

The open-loop voltage gain *G₀* is given by:

*G* = <u>output voltage</u> 0 input voltage For the op-amp in Figure 25.15 the open-loop voltage gain is given by: <u>Vout</u> *G₀* = + − (*V* − *V*) It is called the open-loop gain because there is no loop of resistors or other components linking the output back to **393** the input – it is just the operational amplifier alone. (As we shall see on page 396, an external circuit or loop between the output and the input can be used to provide **negative** **feedback**, which reduces the gain.) The op-amp is not like a transformer. A transformer’s output power comes directly from from the input power. By contrast, an op-amp’s output power is much greater than its input power. To achieve this, it needs two power supplies; these are shown in Figure 25.15 as the +9 V and −9 V connections to the op-amp. There is also a zero volt line, or earth. One power supply will be between the +9 V and the 0 V line and the other between the −9 V connection and the 0 V line. The zero volt line, or earth, is very important as all voltages are measured relative to this potential. If the potential of the inverting input (−) is *V* −, then the potential difference or voltage between that input and the zero volt line is also *V* −. The actual voltage used for the power supplies can vary in different circuits. The positive and negative supply voltages are of equal magnitude and may be written as +*V*s and −*V*s. The connections of the power supplies to the op-amp are often left out of a circuit diagram for clarity but they are always there. They provide the power for the op-amp. The largest voltage that an op-amp can produce is a value close to the supply voltage. The op-amp in Figure 25.15 can

**Figure 25.14** A concert – the loud music has been greatly

amplified.

The goal of producing an amplifier with a constant amplification or **gain** might seem simple, but it is hard to achieve. Unfortunately, electronic components, such as capacitors and transistors, amplify signals of different frequencies by different amounts. One approach is to use an amplifier with a very high gain and then provide an external circuit which reduces the gain but ensures that the overall gain is the same for signals of a greater range of frequencies. Such a device is the **operational amplifier (op-amp)**.

Figure 25.15 shows an operational amplifier. Inside

the plastic casing there are many transistors, resistors and other components. The op-amp has two inputs; one is marked (−) and is known as the **inverting input** and the

only produce outputs between +9 V and −9 V. When the output voltage reaches either supply voltage, the highest or lowest value that it can achieve, the amplifier is said to be **saturated**.

### The properties of an ideal op-amp

The ideal op-amp has the following properties.

##### Infinite open-loop voltage gain

This means that when an op-amp is used on its own, with no feedback loop, then a small input signal will be amplified to an ‘infinite’ output signal. Clearly this is not physically possible (the output cannot exceed the supply voltage) and at its maximum output the amplifier is saturated with output value +*V*s or −*V*s. However, when a feedback loop is applied, the overall gain of the circuit is reduced to a realistic value. Infinite open-loop voltage gain means that signals of a wide range of frequencies have equal gain before the feedback is applied. An actual op-amp may have an open-loop gain of 10 5 but this can be much higher.

##### Infinite input resistance (or impedance)

The input to an op-amp is a voltage. If, for example, a piezo-electric microphone is connected to the op-amp, **394** then the microphone is acting as the voltage supply. It acts just like an electrical battery but the voltage it produces changes with time. Any voltage supply has an internal resistance. You may remember that one of the effects of this is to reduce the terminal p.d. when a current is supplied. The infinite input resistance of an ideal op-amp means that no current is drawn from the supply, there are no ‘lost volts’ and the input voltage to the op-amp is as large as possible. The resistance for an alternating voltage is known as impedance, so the ideal op-amp has infinite impedance and no current passes into the input terminals. The input impedance of an actual op-amp may be as high as 10 12 Ω, but 10 6 Ω is typical.

##### Zero output resistance (or impedance)

The output from an op-amp is a voltage. The op-amp is itself acting as a voltage supply to the next part of a circuit. An ideal op-amp has zero output resistance and so it acts just like an electrical battery with zero internal resistance. This means that there will be no ‘lost volts’ when current is supplied by the op-amp. An actual op-amp typically has an output resistance of around 75 Ω.

##### Infinite bandwidth

The **bandwidth** of an op-amp is the range of frequencies that are amplified by the same amount. An ideal op-amp will amplify signals of all frequencies and should therefore

have an infinite bandwidth. However, in actual op-amps the bandwidth can be as low as a few kilohertz.

##### Infinite slew rate

An ideal op-amp should change the output instantaneously as the input is changed. The slew rate of the op-amp is the factor that affects this time delay. An infinite slew rate means there is no time delay.

##### Zero noise contribution

Any signal includes a small amount of noise. The ideal op-amp does not produce any noise itself, although it will amplify any noise that is present in its input.

### The op-amp as a comparator

The op-amp shown in Figure 25.16 is connected to two power supplies. One battery of 9 V is connected between the zero volt line and the +9 V positive supply terminal of the op-amp and the other between the zero volt line and the negative power supply terminal. These batteries are not shown. The output voltage is given by *V*out = *G₀*× (*V* + − *V* − ), where *G₀* is the open-loop voltage gain. Notice that all of these voltages are measured with reference to the zero volt line, which is often connected to earth.

+9 V

–

+ – *V* out *V*+–9 V *V* <u>0</u>V line (earth)

**Figure 25.16** An op-amp used as a comparator.

Suppose that *G₀* = 10 5 and that *V* + = 0.15 V and *V* − = 0.10 V. The equation then gives: *V* = 10 5 × (0.15 − 0.10) = 5000 V out Clearly this is impossible. The op-amp is therefore saturated and *V*out will be close to one of the power supply voltages, in this case +9 V because *V* + is bigger than *V* −. In fact: ■■ If *V* + is slightly greater in magnitude than *V* −, then *V*out will have a magnitude equal to the positive power supply voltage. ■■ If *V* + is slightly smaller in magnitude than *V* −, then *V*out will have a magnitude equal to the negative power supply voltage. + The op-amp is serving as a comparator, comparing *V* and *V* −. If these two voltages are slightly different, then the output voltage tells us which one is larger. It is unlikely that the voltages will be exactly the same.

A comparator circuit can be used to compare two temperatures or two light levels. The circuit shown in Figure 25.17 is used to give a warning when the temperature sensed by thermistor T becomes smaller than a certain value. To understand the action of this circuit, you should notice that the positive power supply to the op-amp is also used to supply voltage and current to the thermistor T and a 10 kΩ resistor connected as a potential divider. There is also another potential divider circuit connected to the inverting input (−) of the op-amp. (Note that there is no connection where the two connecting wires are shown crossing.) Worked example 3 explains how this circuit operates.

+9 V

T 15 kΩ

B –

A +

–9 V 10 kΩ 15 kΩ *V*out

0 V

**Figure 25.17** An op-amp used as a comparator to monitor

temperature.

##### QUESTIONS

**11** With an open-loop voltage gain *G* = 10 5 and 0 power supply voltages of +9 V and −9 V, what is the smallest difference between *V* + and *V* − for which the op-amp is not saturated?

**12** What happens in the circuit shown in Figure 25.17 if the supply voltages are changed to +15 V and −15 V? Is the temperature at which it switches over the same? Are the output voltages the same?

**13** How can the circuit of Figure 25.17 be altered so that the output switches from −9 V when the temperature is hot to +9 V when the temperature is cold?

**14** Calculate values of *V* +, *V* − and *V*out in Figure 25.17 when the resistance of T is 3 kΩ.

##### WORKED EXAMPLE

|3 For the circuit shown in Figure 25.17, the resistance||Step 2 The thermistor T is a negative temperature||
|---|---|---|---|
|of the thermistor T is 8 kΩ at a temperature of 15 °C.||coefficient thermistor and so its resistance rises||
|What are V|and V, the potentials at the inverting|sharply and eventually becomes larger than 10 kΩ.||
|and non-inverting inputs? And what happens when||Suppose it becomes 12 kΩ. Then:||
|the temperature falls so that the resistance of T rises|||10|
|above 10 kΩ?||potential at A = 9 × 22 = 4.1 V||
|Step 1 V|and V can be found by using the potential|Now V is smaller than V|and the op-amp output|
|divider formula to find the potentials at points A||voltage is the lowest it can provide, near the negative||
|and B. The potential at A is the p.d. across the 10 kΩ resistor. So:|10|supply voltage, in this case −9 V. This switch from +9 V to −9 V is quite sudden because||
|potential at A = 9 ×|18 = 5.0 V|of the large open-loop voltage gain. The value of the temperature when the output voltage switches from||
|The potential at B is easier to find, as the two 15 kΩ||+9 V to −9 V can be altered by adjusting the resistance||
|resistors share the 9 V equally.||of the resistor in series with the thermistor.||
|potential at B =|9 = 4.5 V|||
||2|||
|The op-amp acts as a comparator and, since V||||
|larger than V|, the output will be the highest voltage|||

− +

− +

+ is − that the op-amp can produce, in this case +9 V.

**395**

+ −

### Negative feedback

What happens when the op-amp in Figure 25.17 is connected to a heater which warms the air around the thermistor? The op-amp senses when the room is cold and switches on the heater. The heater then warms the room and this information is fed back to the thermistor, which then senses that the room is now warm enough and switches off the heater. This process is known as **feedback** and keeps the room at a reasonably constant temperature. The effect is shown in Figure 25.18.

sensing device (thermistor)

comparator heater (op-amp)

**Figure 25.18** Feedback keeping temperature constant.

There are many examples of feedback. Your body temperature is remarkably constant because of a number of feedback mechanisms. When your skin senses that you are cold, a signal is sent via the nerves to your brain **396** which closes down some of the blood vessels in your skin to reduce energy loss. If you are very cold the brain makes muscles contract and expand uncontrollably as you shiver. This will make the core of your body warm again and the effect is fed back to the brain, which switches off the shivering. Electrical feedback is also very important. Consider the circuit shown In Figure 25.19. In this circuit *V*in, the input to the op-amp, is connected to the non-inverting input

(+). The whole of the voltage output *V*out is fed back to the inverting input (−) of the op-amp. How does the op-amp behave with this feedback loop? The potential *V*
− at the inverting input (−) is always the same as *V*out because they are connected by the feedback loop. We will assume that the open-loop voltage gain is

infinite and that the op-amp is not saturated. In this case V must be equal in value to V – +, and this is an important principle. Suppose the system starts with both *V*inand *V*out as 0 V and then the input voltage *V*in changes to +0.1 V. The op-amp multiplies the potential difference between *V* + and *V* − by the open-loop voltage gain to produce *V*. out The gain is very high so *V*out increases quickly. What does *V* become? As *V* is ‘fed back’ to *V* −, the value of *V* − out out increases and this reduces the difference between *V* − and *V* +. Very quickly this difference becomes zero again and *V*out = *V*in. We know that *V*out = *G₀*× (*V* + − *V* − ), where *G₀* is the open-loop voltage gain. Since *V*out = *V* − and *V*in = *V* + we have: *V*out = *G₀(V*in− *V*out*)*

*V* (1 +*G*) = *G V* out 0 0 in The closed-loop gain *G* is given by: <u>VoutG₀</u> *G* = = *V*in(1 +*G₀*) Because *G₀* is very high, about 10 5, there is little difference between *G₀* and (*G₀*+ 1), so the closed-loop gain is very nearly 1. Since the input voltage was +0.1 V the output voltage is also +0.1 V. This analysis is true as long as the output voltage is smaller than the supply voltage, in this case as long as *V*out is between −6 V and +6 V. This may seem strange. We have taken an op-amp with a gain of 10 5 and turned it into a device with a gain of 1, so the input voltage and output voltage are equal. This is hardly an amplifier, but it is useful. The op-amp draws very little current from the input, yet it can supply a reasonable current from its output. This circuit is often used as a buffer between electronic circuits. If something happens to one circuit it does not affect the other circuit. A piezo-electric microphone has a high internal resistance and cannot supply much current. If it is connected to the input of the op-amp in Figure 25.19, the same voltage is output but the current can be larger. Another advantage is that it does not matter whether the frequency of the input signal is high or low; the gain is the same. So the output signal is exactly the same as the input signal and there is no distortion. This is only true when the open-loop voltage gain is high. At very high frequencies the open-loop voltage gain falls and eventually the closed-loop gain falls. The **bandwidth**, the range of frequencies for which the gain is constant, is increased by using negative feedback.

+6 V – + –6 V *V* out *V* in 0 V

**Figure 25.19** An op-amp with the output connected to the

inverting input.

To summarise, the benefits of using negative feedback to reduce the gain of an op-amp are: ■■ less distortion ■■ increased bandwidth ■■ the gain is more stable and not affected by changes in temperature, etc. ■■ the output resistance (impedance) can be low and the input resistance (impedance) high.

## The inverting amplifier

The **inverting amplifier** shown in Figure 25.20 uses negative feedback, but not all of the output voltage is fed back to the inverting input (−). When an op-amp is connected as an inverting amplifier: ■■ the non-inverting input (+) is connected to the 0 V line ■■ part of the output voltage (or signal) is connected to the inverting input (−) ■■ the input voltage (or signal) is connected to the inverting input.

To understand how the inverting amplifier works, you need to understand the concept of the **virtual earth** **approximation**. In this approximation the potential at the inverting input (−) is very close to 0 V. Why is this true? There are two steps in the argument:

||||V|R|
|---|---|---|---|---|
||||out|f|
|■■ ■■ +|− + −|+|in|in|

The op-amp multiplies the difference in potential between the inverting and non-inverting inputs, *V* and *V*, to produce the output voltage *V*out. Because the open-loop voltage gain is very high, the difference between *V* and *V* must be almost zero. The non-inverting input (+) is connected to the zero volt line so *V* = 0. Thus *V* − must be close to zero and the inverting input (−) is almost at earth potential.

Point P is known as a **virtual earth**. It cannot actually be 0 V but it is very close to 0 V. This approximation is true as long as the op-amp is not saturated, and for frequencies where the open-loop voltage gain is high.

*R*f

The virtual earth approximation can be used to find an expression for the gain of an inverting amplifier, as follows. If the current in the input resistor *R*in is *I*in and the current in the feedback resistor *R*f is *I*f, then, because point P is at 0 V: <u>Vin</u> *I* in = *R*in and <u>Vout</u> *I* f = *R*f The input resistance of the op-amp is very high and so virtually no current enters or leaves the inverting input (−) of the op-amp. This means that *I*in and *I*f must be equal in size. If *V*in is a positive potential, then the current in the two resistors flows from left to right. *V*outwill be negative because the current flows from P, which is at 0 V, to the output connection, which must have a lower voltage than 0 V. Thus: *I* = −*I* f in and <u>VoutVin</u> *R*f = − *R*in The gain of the inverting amplifier is thus given by: **397**

*G* = *V* = − *R* The negative sign shows that when the input voltage is positive the output voltage is negative and when the input is positive the output is negative. If the input voltage is alternating then there will be a phase difference of 180° or πrad between the input and the output voltages.

##### QUESTIONS

**15** Draw the circuit diagram of an inverting amplifier with a gain of −100 and an input resistor *R*in of 10 kΩ. Include the value of the feedback resistor *R*f.

**16** The supply voltage to an op-amp is ±15 V. The op-amp is connected as an inverting amplifier

following input voltages: of gain −20. Calculate the output voltage for the

**a** +20 mV **b** −400 mV **c** +1.0 V

*R*in +*V*s <u>P</u> *–*

+ *V* in *–V*s*V*out

**Figure 25.20** An inverting amplifier.

##### WORKED EXAMPLE

**4** In the circuit shown in Figure 25.20,*R*in = 4 kΩ and *R*f = 20 kΩ. Calculate: **a** the output voltage when the input voltage is 0.5 V **b** the maximum input voltage if the supply voltage is ±12 V **c** the input resistance of the amplifier.

The solutions can be found using the formula for gain *G*. *R*f20 **Step 1** Calculate the gain *G* = − = − 4 = −5 *R*in **Step 2** Calculate *V*out= gain × *V*in = −5 × 0.5 = −2.5 V

**Step 3** The op-amp becomes saturated when *V* out = −12 V, so: *V* out12 *V* in = = = 2.4 V *G* 5

**Step 4** Point P is at 0 V, so the input resistance is just caused by *R*in = 4 kΩ.

The two resistors *R₁* and *R₂* form a potential divider. The total voltage across *R₁* and *R₂* is *V*out and the voltage across *R₂* alone is *V*in. The current in the two resistors can be written as: <u>Vout</u> = <u>Vin</u> (*R₁*+*R₂*) *R₂* The gain is calculated from: <u>Vout(R₁+R₂) R₁</u> *G* = = = 1 + *V*in*R₂ R₂* Thus for a non-inverting amplifier the gain is given by: <u>R₁</u> *G* = 1 + *R*2 For a non-inverting amplifier, the output is in phase with the input. When the input voltage is positive, so is the output voltage.

##### QUESTIONS

**17** The circuit shown in Figure 25.19 is a non- inverting amplifier. What are the values of *R₁* and *R₂*? Show that the gain of the amplifier is 1.

**18** Draw the circuit of a non-inverting amplifier with a gain of 10. Explain whether the input resistance is very high or very low.

**19** Suppose that the non-inverting amplifier in

Figure 25.21 has *R₁* = 50 kΩ, *R₂* = 5 kΩ and

*V =* s10 V. **a** Calculate the gain. **b** Calculate the output voltage when the input voltage is: **i** −0.10 V **ii** +1.0 V.

**398**

## The non-inverting amplifier

Figure 25.21 shows the circuit for a **non-inverting**

**amplifier**. The input voltage is applied to the non-inverting input; part of the output voltage is fed back to the inverting input.

+*V*s –

+ –*V*s *R₁* *V* out *V* in

*R₂*

**Figure 25.21** A non-inverting amplifier.

As long as the op-amp is not saturated, the potential difference between the inverting (−) and non-inverting inputs (+) is almost zero. So *V* − = *V* + *.* Since the non-inverting input (+) is connected to the input voltage, *V* + = *V*in. Thus *V* − = *V*in.

## Output devices

The output voltage of an op-amp may be used to operate a device according to the changing input voltage. We will now look at three types of output device.

### The relay

Although the output resistance of an op-amp is low, a typical op-amp can only provide a maximum output current of 25 mA. The maximum voltage output from an op-amp is also limited to the supply voltage, typically 15 V. To switch on larger currents and larger voltages the op- amp is connected to a relay.

contacts

movable arm A₁ A₂

coil

**Figure 25.22** A relay and its circuit symbol.

The **relay** is just an electromagnetic switch operated

|by a small current in the coil. Notice that there are two|The light-emitting diode is a very convenient device to||
|---|---|---|
|circuits, one to the coil and one involving the switch|attach to the output of an op-amp. LEDs come in several||
|contacts A₁ and A₂. When a small current passes through|different colours and only require a current of about||
|the coil of the relay in Figure 25.22, the iron core attracts|20 mA to produce a reasonable light output. When placed||
|a movable arm and the contacts connected to A₁ and A₂|on the output of the op-amp they readily show the state of||
|close, completing the second circuit.|that output, whether it is positive, negative or zero.||
|The coil of the relay is the part connected to the output|In practice, an LED cannot be placed directly between||
|of an op-amp. The op-amp can easily provide the small|the output of an op-amp and the zero-volt line. The||
|current required for the coil. When the contacts A₁ and A₂|current–voltage characteristic for an LED is shown in||
|close they can switch large voltages or currents in another|Chapter 11 (page 160). The LED starts to conduct when the||
|circuit.|voltage across it is greater than about 2 V, although this||
|There is, however, a problem using a relay connected to|value depends on the type of LED used. Once the output||
|an op-amp. The current from the op-amp causes the coil to|of an op-amp is much bigger than 2 V, the current in the||
|act as an electromagnet and creates a magnetic field. When|LED and the op-amp will be very high and will damage||
|this current is turned off there is a very rapid fall in the|both of them. A series resistor is required to limit the||
|magnetic flux within the coil and a large e.m.f. is induced|current, as shown in Figure 25.24.||
|across the terminals of the coil, large enough to damage the|The value of the resistance of the series resistor R||
|op-amp. Switching off a relay can damage an op-amp.|can be calculated. If the current is to be 20 mA and the||
|To avoid this damage, a reverse-biased diode is placed|maximum voltage output from the op-amp is 12 V, then||
|across the relay coil. This is shown in Figure 25.23, where|there will be just over 2 V across the LED and 12 − 2 = 10 V||
|D₁ is the reverse-biased diode. When the op-amp switches|across the series resistor R. The series resistor required is:||
|off, the induced voltage in the coil causes the bottom of the||10|
|coil to be more positive than the top of the coil. Diode D₁ is able to pass current round the coil without any damage to the op-amp.|R =|0.02 = 500 Ω|
|The output of the op-amp can be negative as well|output from||
|as positive. Without diode D₂, the relay contacts close whether there is a negative output or a positive output|op-amp||

**399**

*R R* from the op-amp because it does not matter which direction the current flows in the coil in Figure 25.22. Diode D₂ ensures that current can only flow from the op-amp when the output of the op-amp is positive. Thus the relay contacts are closed only when the output of the op-amp is positive. Since diode D₁ is reverse-biased, no current from the op-amp flows through D₁.

output from op-amp diode D₂

A₁ diode D₁ coil

A₂

**Figure 25.23** The output of an op-amp connected to a relay.

### The light-emitting diode (LED)

red LED green LED

**Figure 25.24** LEDs connected to the output of an op-amp.

In Figure 25.24, when the output of the op-amp is sufficiently positive relative to earth the green LED will light. When the output is negative relative to earth, the red LED will light.

##### QUESTIONS

**20** Draw a diagram of a relay connected to the output of an op-amp. The relay should switch on a separate circuit containing mains voltage and a heater.

**21** Why is a reverse-biased diode required for a relay but not for an LED?

### The calibrated meter

An op-amp may be monitoring a physical quantity such as temperature or light intensity. It is helpful to display the value of that physical quantity directly on a meter and not to have to measure an output voltage and then calculate the physical quantity each time. The output voltage of the op-amp is unlikely to be proportional to the physical quantity being measured, **400** for example temperature. The numbers on a voltmeter connected to the output of an op-amp cannot simply be changed to read values of the physical quantity, but the voltmeter can still be calibrated in terms of the physical quantity. Suppose that temperature is being measured and a digital voltmeter is connected to the output. Calibration can be achieved by placing the temperature sensor and a thermometer in a water bath and recording the voltmeter reading and the temperature of the water bath at a number of different temperatures. A calibration graph is then drawn, as shown in Figure 25.25.

6.0
5.0
4.0
3.0
2.0
Voltmeter reading / V

1.0
Temperature / °C

**Figure 25.25** A calibration curve relates the output voltage of

an op-amp to the variable it is being used to measure.

The calibration curve is used to change any other voltmeter reading into a value for the physical quantity, in this case temperature. An analogue meter can be calibrated in the same way, but if the same meter is used all the time as the output, then the scale on the meter can be marked directly with values of the physical quantity. This means that the ‘voltmeter’ will measure temperature directly. Since the voltmeter reading is not proportional to the change in the physical quantity, the scale will not be linear. Figure 25.26 shows a meter with three scales. The bottom two scales are linear and might be the voltage recorded by a voltmeter. The top scale is non-linear and might be the value of the physical quantity being measured. Care is needed when reading a non-linear scale when the pointer is between the markings.

**Figure 25.26** Linear and non-linear scales.

## Summary

■■ ■■

|A sensor contains a sensing device and a processor to|An operational amplifier used as a comparator|||
|---|---|---|---|
|produce an output voltage.|produces either a high positive or a high negative|||
|The resistance of an LDR decreases as the level of the|voltage output, depending on which of two input|||
|light intensity increases.|voltage levels is larger.|||
|The resistance of a negative temperature coeff icient|An operational amplifier can be used as an inverting|||
|thermistor falls as temperature rises.|or a non-inverting amplifier to amplify voltage signals.|||
|Thermistors and light-dependent resistors can be|The gain of an inverting amplifier is −|R||
|used in potential divider circuits to provide output||R||
|voltages that are dependent on temperature and light|The gain of a non-inverting amplifier is 1 +|R₁|.|
|intensity, respectively.||R₂||
|A piezo-electric transducer produces a variation in|Feedback reduces gain but increases bandwidth|||
|output voltage when a crystal is stressed, for example|and stability and reduces distortion.|||
|by pressure changes in sound.|Output devices which may be connected to an op-amp include relays, LDRs and calibrated meters.|||

■■

■■ ■■

<u>f</u> ■■ ■■ in

■■

■■ ■■

■■

■■ The change in resistance of a metal-wire strain gauge is proportional to extension.

**401**

## End-of-chapter questions

**1** How can the circuit of Figure 25.17 be altered so that the op-amp switches from +9 V to −9 V when the temperature rises, instead of when it falls? Draw the circuit diagram. [1]

**2** Draw the circuit diagram of a comparator that switches the output voltage from positive to negative when the light intensity falling on an LDR decreases. [3]

**3** Explain what is meant by: **a feedback** [1] **b** the **virtual earth approximation**. [2]

**4** In the inverting amplifier shown in Figure 25.20,*R*in = 10 kΩ, *R*f = 200 kΩ and *V*s *=* 12 V. Calculate: **a** the gain of the amplifier [2] **b** the input voltage when the output voltage is 8.0 V [2] **c** the maximum input voltage. [1]

**5 a** Explain how an inverting amplifier can have a gain of −0.5. [2] **b** Explain why the gain of a non-inverting amplifier cannot be less than 1. [2]

#### Cambridge International A Level Physics

|6 7||and the output voltage over||The non-inverting amplifier in Figure 25.21 on page 398 has two|R₁ An a.c. signal of amplitude 0.20 V is applied to the input. Draw a single sketch graph which shows both the input cycles of the input on the same axes. Is the circuit shown in Figure 25.27 an inverting or non-inverting amplifier? Calculate its gain.|= 15 kΩ, R₂ = 5 kΩ and V = 10 V. s|[3] [3]|
|---|---|---|---|---|---|---|---|
||||9 kΩ – +|||||
|V in||1 kΩ|||V out|||
||Figure 25.27|||For End-of-chapter Question 7.||||
|8 a b 402|||increases as light intensity increases. Sketch the diagram of a suitable circuit. Explain how your circuit works.||A light-dependent resistor is used with additional components to make a sensor. The voltage output||[2] [2]|
|c 9|5 V d.c. supply||is connected in the circuit shown in Figure 25.28. strain gauge|300 Ω|State which parts of your circuit are the sensor, the processor and the output device. A strain gauge is used to measure the extension of a metal bar. The gauge is stuck to the bar and the change in resistance of the wire in the gauge enables the extension to be determined. The strain gauge V||[2]|
|a b c|Figure 25.28|||For End-of-chapter Question 9.|Explain why the resistance of the wire increases when it is stretched and show that the change in resistance is proportional to the extension, provided that the cross-sectional area is constant. The resistance of the strain gauge when unstretched is 150 Ω. Calculate the reading on the voltmeter. State and explain the eff ect on the voltmeter reading when the strain gauge is stretched.||[2] [2] [2]|

|10||are passed along the glass fibre.|and the microphone produces a maximum output of +20 mV.|In a fibre optic system, sound into a microphone is used to produce diff erent intensities of light that The microphone is connected to a non-inverting amplifier, the output of which is connected to an LED. An operational amplifier with dual 15 V power supplies is used as a non-inverting amplifier||
|---|---|---|---|---|---|
||microphone||– +|+15 V –15 V 0 V||
|a i ii b c i|Figure 25.29 State|two|For End-of-chapter Question 10. Calculate the maximum possible gain for the amplifier.|Copy and complete the circuit in Figure 25.29 to show the resistors necessary for a non-inverting amplifier. Make the necessary connection between the microphone and the amplifier. Add to your diagram the necessary output components for the amplifier to work as described. advantages of using negative feedback in the amplifier circuit.|[2] [2] [2] [2]|
|ii d||all the resistors drawn in|a i|The amplifier is used with the maximum possible gain. Suggest suitable values for the resistance of. [2] Explain what happens in the system when the voltage output from the microphone rises.|403 [2]|

#### Cambridge International A Level Physics

|11|||||from a torch shines on either LDR its resistance becomes 200 Ω.||A student builds an electronic circuit to control a motor using two identical LDRs, P and Q (Figure 25.30). In a room with the same amount of light on each LDR, the resistance of each LDR is 500 Ω. When the light +9 V|||||
|---|---|---|---|---|---|---|---|---|---|---|---|
||P||Q|||||||||
||300 Ω a|A Figure 25.30|B 300 Ω State the value of the output voltage|– + For End-of-chapter Question 11.|V out|M V out|0 V –9 V of the op-amp when:|||||
|404|i ii|||||the potential at point A is greater than the potential at point B the potential at point B is greater than the potential at point A.|||||[1] [1]|
|12 a|b c i ii d V b i ii|in Figure 25.31 The value of|Explain what is meant by a amplifier in Figure 25.31 is − R₂ R₁ Calculate the value of|V A resistor of 4 kΩ is placed in parallel with|Calculate the potential at point A when a torch shines on P. virtual earth R₁ R₂ For End-of-chapter Question 12. is 20 kΩ and the value of. [2] out|Explain what happens in the circuit when a torch shines on P but not on Q. Explain what happens in the circuit when a torch shines on Q but not on P. Explain why it is diff icult to know what will happen if no torch shines on P or Q.. [5] R₁ +12 V – + –12 V R₂|is 4 kΩ. The value of R₂|V out. Calculate the new value of|and use your explanation to show that the gain of the inverting V is 0.50 V. in|V. [2] out|[2] [1] [1] [1]|

|13 to potential divider Figure 25.32 a b 14|it switches the heater on.|In order to switch on a heater when the temperature falls below a set value, a potential divider is connected to a switching circuit. When the input voltage to the switching circuit falls below 0.5 V, switching circuit For End-of-chapter Question 13. Copy Figure 25.32 and add a suitable potential divider circuit to trigger the switching circuit. Explain how the operator could lower the temperature at which the heater is switched on. Figure 25.33 shows a circuit used to monitor the variation of light intensity in a room.|[2] [1]|
|---|---|---|---|
|||X|405|
|||V||
|Figure 25.33 a b||For End-of-chapter Question 14. Identify the component X and describe how the circuit works. Suggest the reason for including the variable resistor in the circuit.|[3] [1]|
