# Chapter 32: Medical Imaging - CAIE A Level Physics (9702) Study Notes

Exam-focused revision notes for Cambridge International A Level Physics 9702, covering X-ray production and control, attenuation and image quality, computerised tomography (CT), ultrasound production and detection, acoustic impedance, A-scans and B-scans, Doppler ultrasound, and magnetic resonance imaging (MRI). Definitions use mark-scheme wording. Questions reward the **physics of image formation**, so link every medical statement to a photon, wave, field or atomic process.

## 1. Theory

### 1.1 X-rays: nature and production

X-rays are electromagnetic radiation with wavelengths about $10^{-13}$ to $10^{-8}~\text{m}$. They lie beyond ultraviolet. X-rays and $\gamma$-rays overlap in wavelength; the difference is origin:

- **X-rays:** produced when fast electrons are **rapidly decelerated**.
- **$\gamma$-rays:** produced by **radioactive decay**.

Medical X-rays are usually **soft X-rays**, with energies below typical $\gamma$-rays. They are **ionising**: they can remove electrons from atoms, damage living tissue and cause mutations.

### 1.2 The X-ray tube

The tube is evacuated and contains a heated filament cathode and a tungsten rotating anode.

| Component | Function |
|---|---|
| Cathode | Emits electrons by **thermionic emission** |
| Anode | Electrons strike it and are decelerated, producing X-rays |
| High-voltage supply | Accelerates electrons from cathode to anode |
| Window | Thin region through which X-rays leave |
| Lead collimators | Absorb stray rays and produce a parallel beam |
| Aluminium filter | Absorbs low-energy X-rays that would only add dose |

**Energy changes:** electrical energy heats the filament; thermionic emission releases electrons; the high voltage does work on them, so electrical potential energy becomes kinetic energy; at the anode about $99\%$ becomes thermal energy and about $1\%$ becomes X-rays. The anode rotates so the heated spot moves away and cools.

For an electron accelerated through potential difference $V$:

$$E_k = eV$$

With $e = 1.60 \times 10^{-19}~\text{C}$, an $80~\text{kV}$ tube gives a maximum electron energy of $80~\text{keV}$.

### 1.3 The X-ray spectrum

The spectrum has two components.

**Bremsstrahlung (braking radiation):** an electron passing near a target nucleus is deflected and decelerated; the lost kinetic energy appears as one or more photons. Different electrons lose different amounts, so this produces a **continuous** range of energies.

**Characteristic radiation:** an incoming electron knocks out an inner-shell electron; an outer electron drops into the vacancy and emits a photon of energy

$$hf = E_{\text{higher}} - E_{\text{lower}}$$

These fixed energies produce **sharp peaks** characteristic of the target element. They are relatively unimportant in medical imaging.

**Maximum photon energy and minimum wavelength**

An electron may lose all its kinetic energy in one interaction:

$$E_{\max} = eV = hf_{\max} = \frac{hc}{\lambda_{\min}}$$

$$\lambda_{\min} = \frac{hc}{eV}$$

Increasing the tube voltage increases $E_{\max}$ and decreases $\lambda_{\min}$, so the beam becomes harder.

### 1.4 Controlling the beam

**Intensity** is power per unit cross-sectional area:

$$I = \frac{P}{A} \qquad \text{unit: } \text{W m}^{-2}$$

| Change | Effect |
|---|---|
| Tube current increased | More electrons per second $\rightarrow$ more photons per second $\rightarrow$ greater intensity |
| Tube voltage increased | Higher photon energies $\rightarrow$ harder, more penetrating beam |
| Exposure time increased | More total energy, but greater dose |
| Aluminium filter added | Removes soft X-rays; increases average hardness and reduces skin dose |
| Collimator aperture reduced | Narrower beam, better sharpness, lower dose |

**Hard X-rays** have high energy, short wavelength and high penetration. **Soft X-rays** are strongly absorbed and increase dose without contributing usefully to the image.

### 1.5 Attenuation of X-rays

A collimated beam loses intensity exponentially:

$$I = I_0e^{-\mu x}$$

where $I_0$ is incident intensity, $I$ is transmitted intensity, $x$ is thickness and $\mu$ is the **linear attenuation coefficient**. The unit of $\mu$ is $\text{m}^{-1}$ (or $\text{cm}^{-1}$). $\mu$ depends on the material and photon energy. Bone has a much larger $\mu$ than soft tissue, so it casts a strong shadow.

**Half-thickness** $x_{1/2}$ reduces intensity to half:

$$\frac{I_0}{2} = I_0e^{-\mu x_{1/2}} \Rightarrow \ln 2 = \mu x_{1/2}$$

$$x_{1/2} = \frac{\ln 2}{\mu} \approx \frac{0.693}{\mu}$$

This is analogous to radioactive half-life.

### 1.6 Improving X-ray images

**Reducing dose**

- **Intensifier screens** contain a phosphor that converts one X-ray photon into many light photons, reducing film exposure by a factor of $100$–$500$.
- **Image intensifiers** convert X-rays to light, then electrons, accelerate and focus them, and produce a brighter visible image. They allow real-time **fluoroscopy** at lower dose.
- Pulsed exposure and tight collimation also reduce dose.

**Improving sharpness**

Sharpness depends on beam width and scattered radiation.

- A **small focal spot** gives a narrower beam and smaller penumbra.
- A **small aperture** in lead plates restricts the beam.
- **Collimation** with lead slits gives an approximately parallel beam.
- An **anti-scatter grid** of lead plates separated by aluminium absorbs rays scattered at an angle, reducing fogging.

**Improving contrast**

- **Hardness** is chosen so tissues of interest absorb differently. Bone is shown with relatively hard X-rays; breast tissue may need softer X-rays and longer exposure.
- **Contrast media** are high-$Z$ substances such as barium ($Z=56$) or iodine ($Z=53$). They absorb strongly and outline hollow or soft structures; a barium meal makes the intestine visible.

### 1.7 Computerised axial tomography (CT)

A plain X-ray is a two-dimensional shadow of a three-dimensional body, so structures at different depths overlap. CT takes many images from different directions.

1. The patient lies inside a ring of stationary detectors.
2. The X-ray tube rotates around the patient, producing a fan-shaped beam.
3. Detectors opposite the tube record transmitted intensity for each direction.
4. A computer combines hundreds of projections to calculate attenuation at every point in a slice.
5. The body is modelled as an array of **voxels** (small cubic volumes).
6. Images of slices, or a three-dimensional reconstruction, are displayed.

**Tomography** means imaging slices (*tomos* = slice); **axial** refers to rotation about an axis.

**Advantages:** shows three-dimensional relationships; distinguishes tissues of similar density; shows the precise position, shape and size of a tumour; can image any slice.

**Limitations:** larger dose than a plain radiograph; movement blurs the image; metal causes artefacts; it uses ionising radiation, so it is avoided unnecessarily in pregnancy and healthy people.

### 1.8 Ultrasound: nature and production

**Ultrasound** is a longitudinal sound wave above $20~\text{kHz}$. Medical frequencies are typically $1$–$10~\text{MHz}$. Sound is mechanical and needs a medium; it cannot travel through a vacuum. In air $c \approx 330~\text{m s}^{-1}$; in soft tissue $c \approx 1540~\text{m s}^{-1}$.

For $2.0~\text{MHz}$ in tissue:

$$\lambda = \frac{v}{f} = \frac{1540}{2.0 \times 10^6} = 7.7 \times 10^{-4}~\text{m} \approx 0.77~\text{mm}$$

Higher frequencies give shorter wavelengths and better resolution, but are absorbed more strongly, reducing penetration.

**Piezo-electric production:** a crystal such as quartz or PVDF alternately contracts and expands when an alternating voltage is applied, so it vibrates and radiates ultrasound. Its thickness is cut to **half a wavelength** so that it resonates at the driving frequency. A **damping block** stops vibration quickly after a pulse, and an **acoustic window** allows efficient transmission.

**Detection:** the piezo-electric effect works in reverse. A varying stress from an echo produces a varying e.m.f. across the crystal. The same transducer can transmit a pulse and then receive echoes.

### 1.9 Acoustic impedance and reflection

At a boundary, some ultrasound is reflected and some transmitted and refracted. The reflection depends on **acoustic impedance**:

$$Z = \rho c \qquad \text{unit: } \text{kg m}^{-2}\text{s}^{-1}$$

For **normal incidence**:

$$\frac{I_r}{I_0} = \left(\frac{Z_2 - Z_1}{Z_2 + Z_1}\right)^2$$

Consequences:

- A large difference in $Z$ gives strong reflection.
- At an air–tissue boundary about $99.95\%$ of intensity is reflected, so gel is used for **impedance matching**.
- Bone reflects strongly and shows up well.
- Soft tissues have similar $Z$, so only a small fraction is reflected and detail is harder to see.
- Gas and bone obstruct ultrasound, so brain and heart scans need careful probe placement.

### 1.10 Absorption of ultrasound

Intensity also falls by absorption:

$$I = I_0e^{-\alpha x}$$

where $\alpha$ is the absorption coefficient. It depends on tissue and strongly on frequency. Higher frequency gives better resolution but poorer penetration.

### 1.11 A-scan

An **A-scan** (amplitude scan) displays echoes as voltage spikes against time.

1. A pulse generator triggers the transducer and oscilloscope time base together.
2. A short pulse enters the body.
3. Partial reflections occur where acoustic impedance changes.
4. Echoes are detected and displayed as spikes.

Spike position gives depth; spike height gives the strength of reflection. If echoes from the front and back of a layer are separated by $\Delta t$, the pulse travels twice the thickness:

$$d = \frac{c\Delta t}{2}$$

A-scans measure eye lens thickness and fetal head diameter.

### 1.12 B-scan

A **B-scan** (brightness scan) builds a two-dimensional cross-section from many A-scans. The transducer is moved across the patient, and sensors record its position and orientation. Each echo appears as a dot whose brightness represents amplitude; the computer assembles a slice image.

B-scans image fetuses, gallstones and kidney stones. They are real-time and use no ionising radiation, but are operator-dependent, and bone or gas can block the view.

### 1.13 Doppler ultrasound

**Doppler ultrasound** uses the frequency change of sound reflected from moving blood cells:

$$\Delta f = \frac{2f_0v\cos\theta}{c}$$

where $f_0$ is transmitted frequency, $v$ is blood speed, $\theta$ is the angle between beam and flow, and $c$ is the speed of sound in tissue. The factor $2$ arises because the sound travels to the cells and back. Rearranging:

$$v = \frac{c\Delta f}{2f_0\cos\theta}$$

The shift is greatest when the beam is parallel to the flow. Doppler ultrasound measures blood flow, detects narrowed arteries and monitors the fetal heartbeat.

### 1.14 MRI: basic principles

MRI uses the magnetic properties of atomic nuclei, usually **hydrogen nuclei (protons)**, which are abundant in water and fat.

**Spin and magnetic moment:** a proton has positive charge and spin, so it behaves as a tiny magnet. Without an external field, the moments point randomly and cancel.

**Alignment and precession:** in a strong field $B_0$, most protons align with the field in a low-energy state; a few align against it. Their axes do not point exactly along $B_0$ but **precess** around it, like a spinning top.

**Larmor frequency:**

$$\omega_0 = \gamma B_0 \qquad f_0 = \frac{\gamma B_0}{2\pi}$$

where $\gamma$ is the **gyromagnetic ratio**. For protons $\gamma \approx 2.68 \times 10^8~\text{rad s}^{-1}\text{T}^{-1}$. At $1.5~\text{T}$:

$$f_0 = \frac{2.68 \times 10^8 \times 1.5}{2\pi} = 6.4 \times 10^7~\text{Hz} = 64~\text{MHz}$$

This is in the **radio-frequency (RF)** region.

**Resonance and relaxation:** an RF pulse at the Larmor frequency is absorbed, flipping protons to the higher state (nuclear magnetic resonance). When the pulse stops, they relax and emit RF radiation. Relaxation rates depend on the environment:

- $T_1$: **spin–lattice** relaxation, energy transferred to surrounding atoms.
- $T_2$: **spin–spin** relaxation, energy transferred to other nuclei.

Watery tissues have long relaxation times (seconds), fatty tissues shorter ones (hundreds of ms), and cancerous tissues intermediate values. These differences give MRI contrast.

### 1.15 The MRI scanner

| Component | Function |
|---|---|
| Superconducting magnet | Produces a strong uniform $B_0$ (up to about $2~\text{T}$), cooled by liquid helium near $4.2~\text{K}$ |
| RF transmitting coil | Sends RF pulses at the Larmor frequency |
| RF receiving coil | Detects RF emitted by relaxing protons |
| Gradient coils | Make $B$ vary with position so the Larmor frequency encodes position |
| Computer | Controls pulses and gradients, stores data, reconstructs the image |

Without gradients, all protons would resonate at the same frequency and no position information would be obtained. The gradient makes the field slightly stronger in one region and weaker in another, so different positions have slightly different Larmor frequencies. The RF frequency selects a slice; varying gradients encode position within it.

**Procedure:** the patient enters the magnet; protons align; a gradient is applied; an RF pulse excites a selected region; the pulse is switched off; relaxing protons emit RF; coils detect the signal; the computer reconstructs an image.

**Advantages:** no ionising radiation; excellent soft-tissue contrast; images in any plane and in 3D; no moving mechanical parts; painless apart from noise.

**Disadvantages:** expensive and slow; strong field attracts ferromagnetic objects and can heat implants or affect pacemakers; noisy and claustrophobic; movement causes artefacts; bone and lungs are less clear; some patients are unsuitable.

### 1.16 Comparing techniques

| Technique | Principle | Best for | Ionising? | Main limitation |
|---|---|---|---|---|
| X-ray | Differential attenuation | Bone, chest, dental | Yes | Overlap; poor soft-tissue contrast |
| CT | Many X-ray projections reconstructed | Bone, trauma, tumours | Yes, higher dose | Dose, cost, motion |
| Ultrasound | Reflection at impedance boundaries | Fetus, soft organs, blood flow | No | Bone/gas obstruction; operator dependent |
| MRI | Nuclear magnetic resonance | Brain, spinal cord, joints | No | Cost, time, metal implants, motion |

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
