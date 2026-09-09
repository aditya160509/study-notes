# 📘 Chapter 18: Hardware and Virtual Machines - Cambridge International AS & A Level Computer Science (9608)

## Cambridge International AS & A Level Computer Science - Part 3

> **Rule + fully solved examples.** Everything the examiner can ask from Chapter 18: the control unit (hard-wired vs microprogrammed), CISC vs RISC, pipelining, the four computer architectures (SISD, SIMD, MISD, MIMD), massively parallel computers, and virtual machines. Each section ends with exam-style questions and full mark-earning solutions.

**Learning objectives (Chapter 18):**
- Show understanding of RISC and CISC processors
- Show understanding of the importance/use of pipelining and registers in RISC processors
- Show awareness of the four basic computer architectures: SISD, SIMD, MISD, MIMD
- Show understanding of the characteristics of massively parallel computers
- Show understanding of the concept of a virtual machine

---

## 18.01 The Control Unit

While a program runs, the CPU receives a sequence of machine-code instructions. **The control unit is the part of the CPU responsible for making sure each machine instruction is handled correctly.**

There are **two ways** to design a control unit:

| Method | How it works |
|---|---|
| **Hard-wired solution** | The control unit is built as a **logic circuit**. Machine-code instructions are handled **directly by hardware**. |
| **Microprogramming** | The control unit contains a **ROM component** that stores the microinstructions / microcode (the **firmware**). |

> **KEY TERMS**
> - **Microcode / microinstructions**: the low-level instructions stored in the control unit's ROM that decode and carry out machine-code instructions.
> - **Firmware**: software stored permanently in ROM so it cannot be changed easily; the microcode of a microprogrammed control unit.

**What the examiner wants:** you must say that a hard-wired control unit is *a logic circuit* handling instructions *directly in hardware*, and that microprogramming needs *ROM/firmware* to store the microcode. 'ROM' is often the exact mark.

---

## 18.02 CISC and RISC Processors

A processor has an **architecture** (its physical construction) and an **instruction set architecture (ISA)**, which is concerned with:
- the instruction set
- the instruction format
- the addressing modes
- the registers accessible by instructions

The **choice of instruction set** is the main factor distinguishing one ISA from another.

- **CISC (Complex Instruction Set Computer)**: a single instruction can be more complex and involve more loading of data from memory. Early designs chose CISC because it made writing compilers for high-level languages easier (specialised instructions matched high-level language requirements).
- **RISC (Reduced Instruction Set Computer)**: a single instruction is simpler, requiring minimal loading of data from memory. This philosophy was championed from the late 1970s.

### Table 18.01 - RISC vs CISC (memorise this)

| RISC | CISC |
|---|---|
| Fewer instructions | More instructions |
| Simpler instructions | More complex instructions |
| Small number of instruction formats | Many instruction formats |
| Single-cycle instructions whenever possible | Multi-cycle instructions |
| Fixed-length instructions | Variable-length instructions |
| Only load and store instructions address memory | Many types of instructions address memory |
| Fewer addressing modes | More addressing modes |
| Multiple register sets | Fewer registers |
| Hard-wired control unit | Microprogrammed control unit |
| Pipelining easier | Pipelining more difficult |

### Key points about the RISC/CISC difference

- For RISC, 'reduced' affects more than just the number of instructions.
- A reduction in *number* of instructions is **not** the major driving force for RISC; the reduction in **complexity** of instructions is.
- Typical CISC architecture contains many **specialised instructions** designed to match high-level programming language requirements.
- Those specialised instructions require **multiple memory accesses**, which are very slow compared with register accesses.
- RISC's simple instructions let data be stored and manipulated **in registers**, with memory access only for initial loading and final storing.
- RISC's simplicity makes **hard-wiring** the control unit easier. CISC's complexity makes hard-wiring difficult, so **microprogramming is the norm** for CISC.

> **What the examiner wants:** for the standard 'state characteristics of a RISC system' question, write *four* characteristics from the left column of Table 18.01. Every one of them is a mark.

---

## 18.03 Pipelining

**KEY TERM - Pipelining: instruction-level parallelism.**

A major reason RISC processors exist was to make **pipelining** efficient. The fetch-decode-execute cycle is separated into stages; a common model has **five stages**:

1. **IF - Instruction fetch**
2. **ID - Instruction decode**
3. **OF - Operand fetch**
4. **IE - Instruction execute**
5. **WB - Result write back**

### Pipeline timing diagram (Figure 18.01)

| Stage | Clock 1 | Clock 2 | Clock 3 | Clock 4 | Clock 5 | Clock 6 | Clock 7 |
|---|---|---|---|---|---|---|---|
| IF | 1.1 | 2.1 | 3.1 | 4.1 | 5.1 | 6.1 | 7.1 |
| ID | | 1.2 | 2.2 | 3.2 | 4.2 | 5.2 | 6.2 |
| OF | | | 1.3 | 2.3 | 3.3 | 4.3 | 5.3 |
| IE | | | | 1.4 | 2.4 | 3.4 | 4.4 |
| WB | | | | | 1.5 | 2.5 | 3.5 |

Notation: **1.1** means instruction 1, stage 1. Read it as 'instruction 1 at its first stage'.

- To pipeline, the processor must have **five independent units**, each handling one stage. This explains why a RISC processor needs **many register sets - each processor unit has its own registers**.
- Once the pipeline is full, at **each clock cycle one instruction completes**. At clock 6, instruction 1 has left the pipeline, instruction 2's last stage is running, and instruction 6 has just entered.
- **Without the pipeline, processing time would be five times longer** (for a 5-stage pipeline).
- **Speed-up formula** (used by examiners): with $n$ instructions and $k$ stages, pipelined time $= k + n - 1$ clock cycles, sequential time $= k \times n$ cycles.

### Interrupt handling in a pipelined system

Normally (non-pipelined, CISC-style), the processor checks for interrupts *after each instruction executes*. In a pipelined system, **five instructions are in the pipeline when an interrupt occurs**. Two solutions:

1. **Erase the pipeline contents** for the latest four instructions that entered; handle the interrupt normally for the remaining one (the instruction executing when the interrupt occurred).
2. **Give each processor unit its own program counter (PC) register**, so current data for *all* instructions in the pipeline can be stored while the interrupt is handled.

### The pipeline data hazard (Discussion Point)

```
ADD R1, R2, R3     # R1 = R2 + R3
ADD R5, R1, R4     # needs the NEW value of R1
```

The second instruction reads R1 **before** the first instruction has written the result to R1. Ways to overcome this:
- **Forwarding/bypassing**: the ALU result is passed directly to the next instruction's stage without waiting for the register write.
- **Stalling**: insert a wait (one or more pipeline bubbles) until the result is available.
- **Reordering instructions** so dependent instructions are not adjacent.

> **What the examiner wants:** the most common pipelining question is a table fill. Instruction A enters at interval 1; each subsequent stage of A shifts one interval right, and instructions B, C follow one interval behind A. The last instruction's last stage tells you total cycles, and the saved cycles = sequential time minus pipelined time. Worked examples with marks are in the practice questions below.

---

## 18.04 The Four Basic Computer Architectures

Architectures are classified by counting **instruction streams** and **data streams**, giving four types.

### SISD - Single Instruction Stream, Single Data Stream

- The typical arrangement in early computers and the earliest microprocessors.
- **Purely sequential - no parallelism.** One instruction processes one data item at a time.
- Example: multiplying an array by 2 takes one instruction per element, one after another.

```
SISD:  [4 3 2 1]  x2 -> [4 3 2 2] -> [4 3 4 2] -> [4 6 4 2] -> [8 6 4 2]
       one element per instruction, repeated
```

### SIMD - Single Instruction Stream, Multiple Data Stream

- **Parallelism applied to the data stream.** One instruction is executed **simultaneously on multiple data items**.
- Architecture: one control unit feeds the same instruction to multiple **Processing Units (PU)** / **Processing Elements (PE)** (arithmetic logic units), each with its own data stream.
- Implemented in two ways:
  - **Array / vector processors**: one processor with a parallel set of registers (one per data stream), or one large 64/128-bit register holding several values - parallelism built into a single processor.
  - **Multi-core processors**: several individual processors working in parallel, each with its own dedicated cache memory providing the data.

```
SIMD:  one instruction "x2" applied at the same time to all four elements:
       4 x2 -> 8       3 x2 -> 6       2 x2 -> 4       1 x2 -> 2
```

> **TIP - examiner trap:** pipelining executes *different instructions* in parallel; SIMD executes *one instruction* on *different data streams simultaneously*. Do not mix these up.

### MISD - Multiple Instruction Stream, Single Data Stream

- **Does not exist in any individual computer architecture design.** (You still need to know the acronym.)
- The concept could be used in a **fault-tolerant system**: the same data stream is fed into two or more processors, and output is **only accepted if all processors produce the same output**.

### MIMD - Multiple Instruction Stream, Multiple Data Stream

- Like SIMD with more than one processing unit receiving parallel data streams, but **each processing unit executes a different instruction**.
- The multiple data streams can come from a **suitably partitioned single memory**; each processing unit may have dedicated cache memory.
- This is the architecture of choice for massively parallel computers.

> **What the examiner wants:** give SISD and SIMD in full *and* the short explanation of what happens with the streams. For SIMD, mention the single control unit supplying one instruction to multiple processing units. MISD's 'fault-tolerant, only accept identical outputs' is the only fact examiners accept about it.

---

## 18.05 Massively Parallel Computer Systems

- MIMD can be implemented in **multicomputer systems = massively parallel computers**: the systems large organisations use for highly complex mathematical processing - the latest type of 'supercomputer'.
- **Key architecture difference**: instead of a bus structure supporting multiple processors, there is a **network infrastructure supporting multiple computer units**. Programs on different computers communicate by **passing messages over the network**.
- Alternative multicomputer system: **cluster computing using PCs** (a 'server farm'), e.g. a Beowulf cluster.
- Either way, these systems have an **extremely large number of individual processors working in parallel**.

> **What the examiner wants:** the two marks are (1) network (not bus) connects many computers, (2) programs communicate by passing messages. 'Supercomputer for complex maths processing' is the context sentence.

---

## 18.06 Virtual Machines

**KEY TERM - System virtual machine: the emulation of computer system hardware using software.**

Key idea: a virtual machine is **software, not hardware**.

- **Without a VM**: an application program needs support from an operating system to run on hardware.
- **With a system VM**: a process interacts with a software interface provided by an operating system - the VM software *emulates hardware* so a guest OS behaves as if it were running on real hardware.

### Structure of a system virtual machine (Figure 18.05)

```
  Application programs         Application programs
  for virtual machine VM1      for virtual machine VM2
  -------------------------    -------------------------
  Guest OS for VM1             Guest OS for VM2
  -------------------------    -------------------------
  Virtual machine VM1          Virtual machine VM2
  -------------------------    -------------------------
            Virtual-machine implementation software
  -------------------------    -------------------------
                          Host OS
  -------------------------    -------------------------
                        Host hardware
```

Three things to note about the structure:

1. **Application programs are installed with the help of a guest OS.** The guest OS supports running applications by interacting with the virtual machine as though it were the real hardware the guest OS would normally run on.
2. **The virtual-machine implementation software is a utility program** supported by the host OS, which is specific to the host hardware.
3. **Applications can also run directly on the host hardware** under the control of the host OS, at the same time as the virtual machines run (this is why Application 2 in the exam diagram shows no stack above the host level).

### Advantages of virtual machines

- **More than one different operating system can be made available on one computer system.**
- **Legacy systems**: an organisation can keep using old software without keeping the old hardware.
- **Server consolidation**: companies with large mainframes can run the same OS many times, offering each company its own virtual machine running as a server.

### Disadvantages of virtual machines

- **Time and effort required for implementation.**
- **Performance is lower** than on a normal (non-virtualised) system.

### Process virtual machines - the Java Virtual Machine (JVM)

- The JVM (Chapter 8, Section 8.05) is a **process virtual machine**, based on a different concept from a system VM.
- A process virtual machine provides a **platform-independent programming environment**: a program executes in the same way on any platform.
- It is **specific software that only supports running Java programs**; a system virtual machine **supports any application**.

**Exam trap - guest OS vs host OS:**
- **Guest OS**: the OS running *inside* a virtual machine; it interacts with the VM software as if it were hardware (it is 'fooled' into thinking it controls real hardware).
- **Host OS**: the OS running *directly on the real hardware*, which supports the virtual-machine implementation software.

> **What the examiner wants:** in the diagram-labelling question, from top down the layers are: Guest OS, Virtual machine, Virtual-machine implementation software, Host OS, Hardware. Know exactly which is which, and remember the JVM is a *process* VM (platform-independent, Java only) while a system VM supports *any* application.---

## 📝 Exam-style Questions with Full Solutions (all from past papers)

### Question 1 (from the chapter)
Computer systems are now often constructed with RISC processors.

- **a i.** State what the acronym RISC stands for. **[1]**
- **a ii.** State four characteristics to be expected of a RISC system. **[4]**
- **b i.** A RISC processor is likely to be 'hard-wired'. Explain what this term means and state which specific part of the processor will be hard-wired. **[3]**
- **b ii.** State what the alternative to hard-wiring is, and what hardware component must be part of the processor to allow this alternative. **[2]**

<details>
<summary><b>Full solution</b></summary>

**a i.** RISC stands for **Reduced Instruction Set Computer**. ✓

**a ii.** Any four of:
- fewer (simpler) instructions
- fixed-length instructions
- single-cycle execution where possible
- only load and store instructions access memory
- fewer addressing modes
- multiple register sets (many general-purpose registers)
- hard-wired control unit

**b i.** **Hard-wired** means the control unit is constructed **as a logic circuit**, so machine-code instructions are handled **directly by hardware**. The specific part is the **control unit (CU)**. ✓

**b ii.** The alternative is **microprogramming** (the control unit uses microcode). The processor needs a **ROM component** to store the microcode/firmware. ✓

</details>

---

### Question 2 (virtual machine diagram)
The diagram represents a system which has implemented a virtual machine:

```
Application program 1        Application program 2
         A
         B
         C
         D
      Hardware
```

- **a.** For each of A, B, C, D give a suitable name. **[4]**
- **b.** For each of A, B, C, D give a brief description of its function. **[8]**
- **c.** Explain why the diagram is different for Application 2. **[2]**

<details>
<summary><b>Full solution</b></summary>

**a.** A = **Guest operating system** (for VM1); B = **Virtual machine 1** (the virtual machine itself); C = **Virtual-machine implementation software** (virtual machine monitor); D = **Host operating system**.

**b.**
- **A (Guest OS)**: the operating system installed inside the virtual machine; it runs applications by interacting with the virtual machine as though it were the real hardware it would normally run on.
- **B (Virtual machine VM1)**: the software emulation of a computer system's hardware, on which the guest OS and its applications run.
- **C (Virtual-machine implementation software)**: the utility program that emulates the hardware, supported by the host OS; it creates and manages the virtual machines and presents virtual hardware to each guest OS.
- **D (Host OS)**: the operating system running directly on the host hardware; it supports the virtual-machine implementation software.

**c.** Application 2 runs **directly on the host hardware under the control of the host OS** - it does not use a virtual machine. Application programs can run directly on the host at the same time as applications run inside virtual machines. ✓

</details>

---

### Question 3 (parallelism and pipelining)
- **a i.** Identify three different types of parallelism. **[3]**
- **a ii.** Identify which type pipelining belongs to. **[1]**
- **a iii.** Using a diagram, explain how pipelining works. **[5]**
- **b.** Interrupt handling is not straightforward in a pipelined system. Explain why, and give a brief account of how problems can be avoided. **[3]**

<details>
<summary><b>Full solution</b></summary>

**a i.** Three types of parallelism:
1. **Instruction-level** parallelism (pipelining)
2. **Processor-level** parallelism (SIMD - multiple processing units executing one instruction on many data streams)
3. **Computer-level** parallelism (MIMD - massively parallel computers / multiple computers working in parallel)

**a ii.** Pipelining belongs to **instruction-level parallelism**. ✓

**a iii.** Pipelining diagram: the fetch-decode-execute cycle is split into stages (IF, ID, OF, IE, WB), and while stage 1 handles instruction 1's fetch, stage 2 simultaneously handles instruction 2's decode, etc.:

| Stage | Clock 1 | Clock 2 | Clock 3 | Clock 4 | Clock 5 | Clock 6 | Clock 7 |
|---|---|---|---|---|---|---|---|
| IF | 1.1 | 2.1 | 3.1 | 4.1 | 5.1 | 6.1 | 7.1 |
| ID | | 1.2 | 2.2 | 3.2 | 4.2 | 5.2 | 6.2 |
| OF | | | 1.3 | 2.3 | 3.3 | 4.3 | 5.3 |
| IE | | | | 1.4 | 2.4 | 3.4 | 4.4 |
| WB | | | | | 1.5 | 2.5 | 3.5 |

Explanation: the processor has five independent units, each handling one stage. Once the pipeline is full, **one instruction completes every clock cycle** instead of waiting for the whole cycle per instruction, so throughput is much higher (processing time ~5x faster for 5 stages in the long run). Each processor unit needs its own register set.

**b.** When an interrupt occurs, **several instructions are already in the pipeline** (e.g. five, at successive stages). Options to avoid problems:
- **Erase (flush) the pipeline contents** for the latest instructions that entered, then handle the interrupt for the remaining instruction; or
- Give **each processor unit its own individual program counter (PC) register**, so current data for all instructions in the pipeline can be stored while the interrupt is handled. ✓

</details>

---

### Question 4 (past paper 9608 p31 Q4, Nov 2015)
- **a.** Connect each description to the correct processor type:
  - "Makes extensive use of general purpose registers" → (RISC / CISC)
  - "Many addressing modes are available" → (RISC / CISC)
  - "Has a simplified set of instructions" → (RISC / CISC) **[3]**
- **b.** Three instructions A, B, C are processed using pipelining. Stages: Fetch, Decode, Execute, Access operand, Write result.
  - **i.** Complete the table showing the time interval of each stage of each instruction. **[3]**
  - **ii.** Each time interval is one clock cycle. Calculate how many clock cycles are **saved** by pipelining. Show working. **[3]**

<details>
<summary><b>Full solution</b></summary>

**a.**
- "Makes extensive use of general purpose registers" → **RISC**
- "Many addressing modes are available" → **CISC**
- "Has a simplified set of instructions" → **RISC**

**b i.** Completed table:

| Stage | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Fetch instruction | A | B | C | | | | |
| Decode instruction | | A | B | C | | | |
| Execute instruction | | | A | B | C | | |
| Access operand in memory | | | | A | B | C | |
| Write result to register | | | | | A | B | C |

**b ii.** With pipelining: instruction A finishes at interval 5, B at 6, C at 7 - total **7 clock cycles** (stages + instructions - 1 = 5 + 3 - 1 = 7).

Without pipelining: each instruction needs all 5 stages before the next starts = $3 \times 5 = 15$ clock cycles.

$$\text{Clock cycles saved} = 15 - 7 = 8 \quad\checkmark$$

</details>

---

### Question 5 (past paper 9608 p31 Q3, June 2016)
A company uses a computer as a web server. The manufacturer will no longer support the computer's OS in six months. The company is considering changing the web server software when the OS changes, and must not disrupt the web server service.

- **a i.** The virtual machine software undertakes many tasks. Describe two of these tasks. **[2]**
- **a ii.** Explain the difference between a guest operating system and a host operating system. **[2]**
- **b i.** Describe two possible uses of virtual machines by the company. **[4]**
- **b ii.** The company uses a virtual machine to test possible solutions. Explain one limitation of this approach. **[2]**

<details>
<summary><b>Full solution</b></summary>

**a i.** Any two tasks of the virtual machine software:
- It **emulates the hardware** of a computer system so that guest operating systems behave as if they were running on real hardware.
- It **creates, starts, stops and manages the virtual machines**, allocating processor time, memory and other resources to each guest OS.
- It allows **more than one operating system to run at the same time** on one physical computer.

**a ii.** A **guest OS** is an operating system running *inside* a virtual machine; it interacts with the virtual-machine software as though the software were the hardware it normally runs on. A **host OS** is the operating system running *directly on the real host hardware*; it supports the virtual-machine implementation software.

**b i.** Two possible uses:
1. **Test the new OS and web-server software** in a virtual machine before making any change, so the live server keeps running on the old OS while the change is validated; when tested, the new configuration can be switched to without disrupting the service.
2. **Run the old (legacy) OS in a virtual machine** on newer hardware after manufacturer support ends, so the existing web server keeps working as before. (Server consolidation: run several isolated server instances, e.g. one per client, on one machine.)

**b ii.** One limitation: a virtual machine **does not offer the same level of performance as a normal system** - the emulation/overheads mean the tested web server may respond differently under many simultaneous requests than it would on real hardware, so the test may not accurately predict real-world behaviour. ✓

</details>

---

# 📋 Formula / Fact Sheet (Chapter 18)

**Control unit designs:** hard-wired (logic circuit, direct hardware) vs microprogrammed (ROM stores microcode/firmware).

**RISC:** few, simple, fixed-length, single-cycle instructions; only load/store access memory; few addressing modes; multiple register sets; hard-wired; pipelining easy.

**CISC:** many, complex, variable-length, multi-cycle instructions; many addressing modes; few registers; microprogrammed; pipelining hard.

**Pipelining:** 5 stages = IF, ID, OF, IE, WB; one instruction completes per cycle once full; pipelined time $= k + n - 1$ cycles; sequential $= k \times n$ cycles; interrupts → flush pipeline or per-stage PC registers.

**SIMD ≠ pipelining:** SIMD = one instruction on many data streams; pipelining = many instructions at different stages.

**Four architectures:**

| | One instruction | Many instructions |
|---|---|---|
| One data stream | SISD (sequential) | MISD (fault-tolerant concept only) |
| Many data streams | SIMD (array/vector, multi-core) | MIMD (massively parallel) |

**Massively parallel:** network infrastructure (not bus) + message passing between computers; supercomputers/server farms.

**System VM:** software emulating hardware; runs guest OSes on one host; pros = multiple OSes, legacy software, server consolidation; cons = implementation effort, lower performance.

**JVM = process VM:** platform-independent, Java programs only; system VM supports any application.

# ⚡ Quick Reference Card

1. **Control unit**: hard-wired OR microprogrammed (ROM + firmware).
2. **RISC vs CISC**: RISC = simple/few/fixed-length instructions, registers, hard-wired; CISC = complex instructions, microprogrammed.
3. **Pipeline questions**: fill stage table diagonally; total cycles = stages + instructions - 1; saved = (stages x instructions) - total.
4. **Architectures**: learn the 4 acronyms and what each stream count means; MISD is only a fault-tolerance concept.
5. **VM layers** (top to bottom): Application → Guest OS → Virtual machine → VM implementation software → Host OS → Hardware.
6. **Guest vs host**: guest runs inside the VM 'fooled' into thinking it has hardware; host runs directly on real hardware and supports the VM software.
7. **VM pros**: multiple OSes, legacy systems, server consolidation. **Cons**: implementation effort, slower performance.