# Chapter 20: System software — Complete Study Guide (FULLY EXPANDED)
### Cambridge International AS & A Level Computer Science
*Syllabus 9618 (and legacy 9608). This is the fully expanded version: every section now contains (1) deep theory, (2) a "WHAT CAMBRIDGE ASKS" box showing exactly how the topic is examined with real past-paper phrasing + mark-scheme wording, (3) inline "QUICK CHECK" questions placed *as you read* so you test yourself mid-section, and (4) the main things to memorise. Based on the coursebook (Langfield & Duddell) plus real Paper 3 past papers and mark schemes (9618/31 Oct/Nov 2022 and others).*

---

## PART 1 — THE PURPOSES OF AN OPERATING SYSTEM (20.01)

### 1.1 What an OS actually has to do when the machine powers on

A computer system needs a program that begins to run the moment the system is first switched on. At that exact instant, the operating system programs are still sitting on disk — there is no OS in memory yet to "run" anything. The way out of this chicken-and-egg problem:

> **Basic input/output system (BIOS):** firmware stored in **ROM** that starts a **bootstrap program**. It is this bootstrap program that loads the operating system into memory and sets it running.

So the boot sequence is: **ROM BIOS → bootstrap program → OS loaded from disk into memory → OS takes over.** The BIOS is in ROM precisely because it must survive a power-off and be present *before* any other software exists. (On modern systems this is often called UEFI rather than BIOS, but Cambridge still uses the BIOS/bootstrap terminology — use that wording in the exam.)

**WHY THIS IS TESTED:** Cambridge sometimes asks you to describe the boot process, or to explain *why the initial startup code must be in ROM*. The answer: it must be **non-volatile** (survives power loss) and must be present and executable before any OS or application software can possibly run — there is no software yet to load it, so it has to be hard-coded into non-volatile memory.

> **MAIN THINGS TO MEMORISE**
> - Boot order: ROM BIOS → bootstrap → OS into RAM.
> - BIOS is in **ROM** (non-volatile) on purpose.
> - The bootstrap's only job is to load the OS.

**QUICK CHECK 1.1**
*Q: Why can't the bootstrap program be stored on the hard disk and run from there like a normal program?*
*A: Because to read from disk you already need software running — the bootstrap has to exist in ROM so it is available the instant power is applied, before any disk-access software (which is part of the OS) exists.*

### 1.2 Multi-programming and time-sharing

> **Multi-programming:** more than one program can be stored in memory at once; only one can access the CPU at any given time, but others are "ready" and swapped in when the opportunity arises. This happens for a *single* user.

> **Time-sharing system:** a system designed to have *many users* simultaneously logged in (the CPU is shared between their jobs in quick turns).

**Theory:** The CPU is so fast that a single program can never keep it busy — most of the time a running program is *waiting* for I/O (disk, keyboard, network). Multi-programming exploits this: while one program waits for I/O, the OS gives the CPU to another. Time-sharing extends this to many human users, each getting a rapid slice of CPU so it *feels* instantaneous.

> **MAIN THINGS TO MEMORISE**
> - Multi-programming = many programs in RAM, one user, one gets CPU at a time.
> - Time-sharing = many users, CPU shared in turns.
> - Purpose of both: stop the CPU going idle.

**QUICK CHECK 1.2**
*Q: A single-user computer is running three programs at once (a word processor, a music player, a virus scanner). Which concept from 1.2 applies?*
*A: Multi-programming — multiple programs resident in memory for one user, with the CPU switched between them.*

### 1.3 The two viewpoints on an OS's purpose

The textbook says the purposes of an OS are best considered from two viewpoints:

- **Internal viewpoint** — how the OS organises its own activities to **best use the resources available** (CPU, memory, I/O system). This is *resource management*.
- **External viewpoint** — the **facilities made available for the user** of the system (user interface, file system, programming environment).

The three major resources from the internal viewpoint are the **CPU, the memory, and the I/O system** — and each gets its own section below.

**WHAT CAMBRIDGE ASKS:** A common 2-mark question is *"State two internal functions of an OS"* or *"Give two facilities the OS provides for the user."* Internal answers = scheduling, memory management, I/O control. External answers = user interface, file system, API, programming environment. **Keep the two lists separate** — candidates lose marks by mixing them.

> **MAIN THINGS TO MEMORISE**
> - Internal = resource management (CPU, memory, I/O).
> - External = what the user gets (UI, file system, API).
> - Never swap the two in an answer.

**QUICK CHECK 1.3**
*Q: "The operating system provides a file system." Is this an internal or external function?*
*A: External — it is a facility provided for the user. (Memory management would be the internal counterpart.)*

### 1.4 OS structure: user mode vs kernel mode

An OS is structured to provide a platform for both resource management and facilities for users. It has **two modes of operation**:

- **User mode** — the mode available to the user or to an application program.
- **Kernel mode** (the most common name for the alternative) — has **sole access to part of the memory and to certain system functions that user mode cannot access**.

**Theory (deeper):** The CPU has a hardware flag for the current mode. User programs run with the flag in user mode, so any attempt to execute a privileged instruction (e.g. directly accessing hardware, changing the memory map) is blocked by the hardware and causes a trap into the kernel. The **kernel runs all of the time**; the remainder of the OS runs in user mode and is only called in when needed. This protects the core of the system — a buggy or malicious application can crash in user mode without corrupting the kernel or other programs.

**Layered structure** (Figure 20.01): application programs / utilities / kernel / hardware interface, stacked so that (like a network protocol stack) each higher layer is fully serviced by a lower layer, and a program makes **system calls** down to the kernel.

**Modular structure** (Figure 20.02): a more flexible, real-world approach where the **kernel calls on individual services when required** — memory management, file management, device management, scheduling management. This can be paired with a **microkernel**, where the functionality inside the kernel is reduced to the absolute minimum and other services run outside it.

**WHAT CAMBRIDGE ASKS:** If asked to *compare layered vs modular*, note that a pure layered OS is hard to achieve in practice (every layer must be fully serviced by the one below, which is rigid), so the modular structure with a microkernel calling services on demand is the more realistic model. A **microkernel** improves reliability/security (less privileged code = smaller attack/crash surface) at some performance cost (more switches between kernel and services). If asked *why some memory is protected*, answer: the kernel needs protected memory so user programs cannot overwrite OS code or another user's data; the hardware enforces this by only allowing kernel-mode code to touch those addresses.

> **MAIN THINGS TO MEMORISE**
> - Two modes: user mode (applications) and kernel mode (privileged, protected memory + system functions).
> - Kernel runs always; rest of OS runs in user mode on demand.
> - Microkernel = minimal privileged code, better security, slight performance cost.

**QUICK CHECK 1.4**
*Q: A user program tries to write directly to a hardware register. What stops it, and what happens?*
*A: The CPU's mode flag (user mode) blocks the privileged instruction; the hardware raises a trap/interrupt that hands control to the kernel, which can then reject or service the request safely.*

---

## PART 2 — THE INPUT/OUTPUT (I/O) SYSTEM (20.02)

### 2.1 What the I/O system actually covers

The I/O system is **not just** input/output that directly involves a human user. It also includes input and output to **storage devices** while a program is running (e.g. reading/writing disk mid-execution).

**Theory:** Figure 20.03 shows the schematic: the CPU and memory sit on a **bus structure**, and each device (disk, screen, keyboard, printer) connects through its own **device driver**. A device driver is the small piece of OS software that knows how to talk to one specific piece of hardware — the user just expects the device to work. Without a driver, the OS would need to know the internals of every possible printer, disk, etc.; with drivers, the OS talks to a standard interface and the driver translates.

**WHAT CAMBRIDGE ASKS:** *"What is the purpose of a device driver?"* → a program that translates between the OS and a specific hardware device so the OS doesn't need to know the device's internals. Reliable 1–2 mark definition.

> **MAIN THINGS TO MEMORISE**
> - I/O includes storage devices, not just user devices.
> - Device driver = translation layer between OS and specific hardware.

**QUICK CHECK 2.1**
*Q: Why does the OS use a device driver rather than controlling the printer directly?*
*A: So the OS stays hardware-independent — each different printer model only needs its own driver; the OS uses one standard interface.*

### 2.2 Why I/O management matters: the timescale problem

> One second is a very long time for a computer system.

A CPU runs at **GHz frequencies** — one second is more than a *trillion* clock cycles. Compare that to I/O speeds (Table 20.01):

| Device | Data rate | Time for transfer of 1 byte |
|---|---|---|
| Keyboard | 10 Bps | 0.1 s |
| Screen | 50 MBps | $2 \times 10^{-8}$ s |
| Disk | 5 MBps | $2 \times 10^{-7}$ s |

**Theory:** The gap is staggering — a keyboard delivers one byte in $0.1$ s, during which the CPU could have run $\sim 10^8$ operations. If the CPU sat and waited for every keystroke, it would be idle 99.9999% of the time. This mismatch is *the* reason for interrupts and scheduling (Part 3) and for DMA (below).

**WHAT CAMBRIDGE ASKS:** Expect a question linking slow I/O to the need for scheduling/interrupts. The reasoning chain Cambridge rewards: I/O is orders of magnitude slower than the CPU → if the CPU waited for every I/O it would be idle almost all the time → therefore the OS uses interrupts + scheduling to switch the CPU to another process while I/O completes.

> **MAIN THINGS TO MEMORISE**
> - CPU = billions of ops/sec; I/O = comparatively glacial.
> - This gap → must not let CPU wait → interrupts + scheduling.

**QUICK CHECK 2.2**
*Q: "A CPU operates at 3 GHz. Explain why it cannot simply wait for a disk read to finish."*
*A: At 3 GHz the CPU does ~3 billion cycles per second; a disk byte takes ~2×10⁻⁷ s, so during one disk-byte transfer the CPU could do ~600 operations. Waiting wastes the vast majority of CPU capacity, so the OS switches to another process instead.*

### 2.3 Direct transfer (DMA-like behaviour)

The bus structure allows an option for data to move **between an I/O device and memory directly**. The OS can force I/O to pass via the CPU, but for large quantities of data it can instead ensure **direct transfer between memory and the I/O device** — keeping the CPU free to do other work.

**Theory:** This is the principle behind **Direct Memory Access (DMA)**. A DMA controller takes over the bus, copies a block of data from the device straight into a memory buffer, and only interrupts the CPU *once* the whole block is done — instead of the CPU handling every single byte. This is a major efficiency win for bulk transfers (disk reads, network packets).

> **MAIN THINGS TO MEMORISE**
> - Data can go device↔memory directly (DMA), not always via CPU.
> - Frees the CPU during bulk transfers.

**QUICK CHECK 2.3**
*Q: A disk sends 4096 bytes to memory. With DMA, how many times does the CPU get interrupted during the transfer?*
*A: Once — when the whole block has arrived. Without DMA the CPU would handle each byte (4096 interruptions).*

---

## PART 3 — PROCESS SCHEDULING (20.03)

### 3.1 Jobs, programs, and the three schedulers

Programs available to run start life **stored on disk**. A user submits a **job** (the program + instructions on how to run it).

> **High-level (long-term) scheduler:** makes decisions about *which program stored on disk* should be moved into memory.

> **Medium-term scheduler:** controls moving a program *back to disk* when memory gets overcrowded (this is the link to memory management in Part 4).

> **Low-level (short-term) scheduler:** controls *when a process in memory gets access to the CPU*.

**Theory:** Think of it as: long-term chooses who gets into the building, medium-term can throw someone back outside if it's too crowded, and short-term decides who gets the CPU right now. The long-term scheduler controls the *degree of multiprogramming* (how many processes are in memory); the short-term scheduler runs very frequently (every time the CPU is free).

**WHAT CAMBRIDGE ASKS:** Usually only the *short-term* scheduler is examined in detail (the algorithm choices). But know the three exist and their distinct jobs — a question may ask you to "identify which scheduler decides which process gets the CPU" (answer: low-level/short-term).

> **MAIN THINGS TO MEMORISE**
> - Long-term = disk → memory (which program).
> - Medium-term = memory → disk (ease overcrowding).
> - Short-term = which process gets CPU now.

**QUICK CHECK 3.1**
*Q: Memory is full and a new program needs to run. Which scheduler acts, and what does it do?*
*A: The medium-term scheduler — it may move an existing process (or the new one) back to disk to free space.*

### 3.2 Process states — the five-state model

Recall from Chapter 8: a **process** is "a program being executed." This chapter refines that to include the moment it first arrives in memory. A **process control block (PCB)** is created in memory to hold the process's data. The five states and their transitions (Figure 20.05):

- **New** — a new process arrives in memory and a PCB is created; it moves to → **Ready**.
- **Ready** — the dispatcher gives it CPU access → moves to → **Running**.
- **Running** — halted by an **interrupt** → returns to → **Ready**.
- **Running** — cannot progress until some event occurs (e.g. I/O) → moves to → **Waiting** (also called *suspended* or *blocked*).
- **Waiting** — notified the event is complete → returns to → **Ready**.
- **Running** — finishes execution → → **Terminated**.

> **Process:** a program in memory that has an associated process control block.
> **Process control block (PCB):** a complex data structure containing all data relevant to the running of a process (register values, state, priority, memory allocation, etc.).
> **Thread:** a part of a program which is handled as an individual process when being executed.

**Theory (deeper):** The distinction between **Ready** and **Waiting** is the most-tested subtlety. A *ready* process is fully prepared to run — it just isn't *currently* on the CPU (maybe another process has it). A *waiting* process **cannot** run even if the CPU were handed to it, because it is blocked on something (an I/O completion, a signal, a resource). The dispatcher only ever picks from the **ready** queue. A process can be split into **threads**, each handled as its own process — this is how one program does several things at once (a browser downloads a file in one thread while you scroll in another).

**WHAT CAMBRIDGE ASKS — this is one of the most frequently tested parts of the chapter.** A typical 6-mark question: *"In one model for the execution of a program, there are five defined process states. Identify three of them and explain the meaning of each."* You must name the five (new, ready, running, waiting, terminated) and explain any three. Common traps: mixing up **waiting** (blocked, waiting for an event) with **ready** (able to run, just not currently on CPU); and forgetting that **new** and **terminated** are states too — candidates often only list three and lose marks. State *both the name and the meaning* (2 marks each), never just the name.

> **MAIN THINGS TO MEMORISE**
> - Five states: New → Ready → Running → Waiting → Terminated (with the loops back to Ready).
> - Ready ≠ Waiting: ready CAN run (just not now); waiting CANNOT run (blocked on event).
> - PCB holds the process's state so it can resume.

**QUICK CHECK 3.2**
*Q: A process issues a "read from disk" system call and is taken off the CPU. Which state does it enter, and can the dispatcher give it the CPU back immediately?*
*A: It enters the Waiting (blocked) state. No — the dispatcher only selects from the ready queue; a waiting process cannot run until the disk read completes and it returns to ready.*

### 3.3 Interrupts

Some interrupts come from **errors** that kill a running process. Otherwise there are two reasons for interrupts:

1. **I/O waiting** — a running process makes a system call needing I/O and must move to the waiting state. The CPU can't sit idle for the (slow) I/O, so the interrupt lets something else run.
2. **The scheduler halts the process** — for one of the scheduling-algorithm reasons below (e.g. its time slice expired in round-robin).

**Theory:** Whatever the cause, the **OS kernel invokes an interrupt-handling routine**, which may need to decide on **priority**. A required action: the current register values must be **saved into the PCB** so the process can resume exactly where it left off. The textbook's discussion point: what if an interrupt arrives *during* the interrupt handler? — that is why interrupts themselves have priorities (a higher-priority interrupt can pre-empt a lower-priority one, nesting safely).

**WHAT CAMBRIDGE ASKS:** *"Why must register values be saved on an interrupt?"* → so the process can be restarted later from the exact point it was halted, with no loss of state. Clean 1–2 marks. Also: *"Why are interrupts given priorities?"* → to allow a more urgent interrupt to pre-empt a less urgent one and to permit safe nesting.

> **MAIN THINGS TO MEMORISE**
> - Interrupts let the CPU switch away during slow I/O.
> - Registers saved to PCB → process resumes exactly.
> - Interrupts have priorities (allow nesting).

**QUICK CHECK 3.3**
*Q: A process is halfway through `x := a + b` when a disk-read interrupt arrives. After the interrupt is handled, how does the OS ensure the process continues correctly?*
*A: The interrupt handler saved the process's register values (including the partial state) into its PCB; when the process is later dispatched again, those registers are restored, so it resumes mid-instruction correctly.*

### 3.4 Scheduling algorithms

A scheduling algorithm can be **preemptive** or **non-preemptive**:

> **Preemptive:** can halt a process that would otherwise keep running undisturbed (often involves prioritising processes).
> **Non-preemptive:** once a process gets the CPU, it keeps it until it finishes or chooses to yield.

**First come first served (FCFS):** the simplest algorithm; **non-preemptive**; implemented as a **FIFO queue**. Very inefficient on its own — a long job can block everything behind it (the "convoy effect"), but useful as a component of more complex algorithms.

**Round-robin:** allocates a **time slice** to each process, then halts it when the slice runs out — therefore **preemptive**. Implemented as a FIFO queue, normally *without* priorities (though you could give each priority level its own round-robin queue). Strength: fair and responsive. Weakness: context-switch overhead, and poor if jobs vary wildly in length.

**Priority-based scheduling:** more complicated, because (a) every time a new process arrives or a running one is halted, priorities may need **re-evaluation**, and (b) judging priority takes computation. Possible criteria:

- estimated time of process execution
- estimated remaining time for execution
- length of time already spent in the ready queue
- whether the process is I/O-bound or CPU-bound

**Worked example of the logic:** a process that prints wage slips does almost no CPU work but lots of I/O. It makes sense to give it a **high priority** so its tiny CPU needs run immediately, then it goes back to the waiting state while printing happens — this keeps the (slow) printer busy without wasting CPU time.

**WHAT CAMBRIDGE ASKS — classification is explicitly tested.** A standard 4-mark question: *"Identify two scheduling algorithms and for each classify its type (preemptive/non-preemptive)."* Safe pairs: FCFS = non-preemptive; round-robin = preemptive. If you name priority scheduling, it is preemptive. **Do not say round-robin is non-preemptive.** A 2-mark question asks for two priority criteria — any two of the four bullet points score. A good exam sentence: *"An I/O-bound process might be given high priority because it only needs the CPU briefly, allowing the I/O device to be kept busy."*

> **MAIN THINGS TO MEMORISE**
> - FCFS = non-preemptive (FIFO, convoy effect weakness).
> - Round-robin = preemptive (time slice, fair, context-switch cost).
> - Priority = preemptive; criteria include I/O-bound vs CPU-bound, time in queue, remaining time.

**QUICK CHECK 3.4**
*Q: A system uses round-robin with a 10 ms time slice. Process A needs 25 ms of CPU. How many times is A interrupted, and what happens each time?*
*A: Twice — after 10 ms and after 20 ms, the time slice expires and A is preempted back to the ready queue (another process runs); after its third 5 ms slice A finishes. So A is interrupted twice and runs in three slices.*

---

## PART 4 — MEMORY MANAGEMENT (20.04)

### 4.1 What "memory management" covers

- Providing **protected memory space** for the OS kernel (ties back to kernel mode in Part 1.4).
- Defining memory addresses for a loaded program, its procedures, and its data.
- In a multiprogramming system, handling **fragmentation** (memory gets broken into awkward gaps, like a hard disk does).
- Deciding **how much memory** to give to each process sharing memory.

### 4.2 Partitions, dynamic partitioning, and segmentation

**Early approach — fixed partitions:** memory split into partitions; load a whole process into one partition. Wasteful if the process is smaller than its partition (**internal fragmentation** — unused space inside the allocated partition).

**Improvement — dynamic partitioning:** partition size adjusts to match the process size, but the rule "one process per partition" stays. Reduces internal fragmentation but allows **external fragmentation** (free gaps between partitions too small for upcoming processes).

**Extension — segmentation:**

> **Segmentation:** where a large process is divided into **segments** for loading into memory, but the segments are **not constrained to be the same size**.

This let bigger processes be handled, but two factors hurt efficiency: (1) segments weren't equal-sized, and (2) a process could be too big for all its segments to be in memory at once — so segments were shuffled disk↔memory. The result: **fragmentation of both memory and disk**, degrading performance.

**WHAT CAMBRIDGE ASKS — the ONE mark Cambridge wants:** *"State one difference between paging and segmentation in the way memory is divided."* The mark scheme accepts exactly: *"Paging divides memory into fixed-size (equal) blocks; segmentation divides memory into variable-sized blocks."* Learn that sentence verbatim — it has appeared in multiple sessions (e.g. 9618/31 Oct/Nov 2022 Q8(b)).

> **MAIN THINGS TO MEMORISE**
> - Fixed partition → internal fragmentation.
> - Dynamic partition → external fragmentation.
> - Segmentation = variable-sized chunks; paging = fixed-sized chunks (the key 1-mark difference).

**QUICK CHECK 4.2**
*Q: A 40 KB process is loaded into a 64 KB fixed partition. What type of fragmentation results, and how much is wasted?*
*A: Internal fragmentation — 24 KB inside the partition is unused but cannot be given to another process.*

### 4.3 Paging and virtual memory — the modern approach

> **Paging:** where a large process is divided into **pages** which **have to be the same size**. Memory is divided into **frames** of the same size; secondary storage can also be divided into frames.

> **Virtual memory:** a paging mechanism that allows a program to use **more memory addresses than are available in main memory**.

**Theory (deeper):** This solves the "my program is bigger than RAM" problem. The CPU hands an address to a **memory management unit (MMU)**, which maps it to a physical location via a **page table**. The program sees a *contiguous* logical address space; physically the pages are scattered across frames.

**How the address works (Figure 20.06, the worked model):**

- A program has 48 instructions across 3 pages, using logical addresses `00000000`–`00101111` (8-bit logical address → $2^4 = 16$ possible pages; **4 bits = page number, 4 bits = page offset**).
- The **page table** (one per process) uses the page number as an index and holds a **presence flag** (is this page currently in memory?) and the **page frame number** (where it lives in physical memory).
- Page frames do **not** need to be adjacent in physical memory — the table maps logical→physical.

**Page faults and replacement:** pages start on disk. When the process needs a page the table says is *not* in memory, that's a **page fault**. To bring it in, another page usually has to be evicted first — so a **page replacement algorithm** is needed. Options:

- **FIFO** (first-in first-out) — simple but not smart (can evict a heavily-used page).
- **Least-recently-used (LRU)** — more sensible, but requires recording page-use statistics.

**WHAT CAMBRIDGE ASKS — virtual memory explanation (3 marks).** The mark scheme (9618/31 Oct/Nov 2022 Q8(a)) rewards: (1) it is a **paging** mechanism; (2) it lets a program use **more addresses than physically exist in RAM**; (3) only the pages currently needed are held in main memory and pages are **swapped** between RAM and secondary storage as required (and "virtual memory is created temporarily"). A full 3-mark answer must hit all three ideas — don't just say "it's extra memory," because virtual memory is *not* extra physical memory, it's an address-space illusion backed by disk.

**The big disadvantage — disk thrashing:**

> **Disk thrashing:** when paging is used and a repetitive state is reached where loading one page causes a need for another page to be loaded almost immediately, but loading that new page causes the same immediate need — leading to almost never-ending loading/unloading of pages.

Thrashing happens when the total working set of active processes exceeds RAM, so the system spends more time swapping than executing.

**WHAT CAMBRIDGE ASKS — advantages AND problems both get asked.** Advantages of virtual memory (2 marks): (a) programs larger than RAM can run; (b) only needed pages occupy RAM, so memory is used efficiently / more programs can be resident at once. Problem (2 marks): disk thrashing → severe slowdown; plus the general overhead of managing page tables and handling page faults. If a question says "explain one problem," disk thrashing is the strongest single answer.

> **MAIN THINGS TO MEMORISE**
> - Paging: process → equal pages; RAM → equal frames; mapped by page table (presence flag + frame number).
> - Virtual memory = paging that lets a program exceed physical RAM; pages swapped disk↔RAM.
> - Page fault = needed page not in RAM. Replacement: FIFO or LRU.
> - Thrashing = constant swapping = slowdown.

**QUICK CHECK 4.3**
*Q: An 8-bit logical address uses 4 bits for the page number. How many pages can a process have, and how big is each page if physical memory is 256 bytes in 16 frames?*
*A: 4 bits → 2⁴ = 16 pages. 256 bytes / 16 frames = 16 bytes per frame, so each page is 16 bytes (page offset = 4 bits = 16 values).*

**QUICK CHECK 4.3b**
*Q: A process references page 7 but the page table's presence flag for page 7 is 0. What happens?*
*A: A page fault occurs; the OS must fetch page 7 from disk into a free frame (evicting another page if none is free), update the table, then restart the instruction.*

---

## PART 5 — OS FACILITIES PROVIDED FOR THE USER (20.05)

The user interface may be a **command line, a graphical display, or voice recognition** — but its function is always to let the user interact with running programs. Key points:

- When a program uses a device, the OS supplies the **device driver**; the user just expects the device to work.
- The OS provides a **file system**: the user picks filenames and organises folders, but does **not** organise the physical disk layout.
- For a programmer, the OS provides a **programming environment** — you can create and run programs without knowing how the processor works internally.
- A running program is itself "a type of user": the OS gives it **system calls** (e.g. "read this file" becomes a system call that the OS fulfils).
- An **application programming interface (API)** extends this: each API call does a specific job (e.g. create a screen icon) and may use one or more system calls. **APIs aim to give portability** — a program runs on different OSes with minimal changes.

**WHAT CAMBRIDGE ASKS:** *"What is the purpose of an API?"* / *"How does an API help portability?"* → it provides a standard set of functions a program calls, so the program doesn't depend on OS-specific internals; the same source can be recompiled/run on another OS with minimal change. Clean 1–2 marks, and pairs with the "facilities for the user" bullet. Also re-tested: *"Give two facilities the OS provides for the user"* — say user interface, file system, programming environment, system calls, API — **not** scheduling or memory management (those are internal).

> **MAIN THINGS TO MEMORISE**
> - External facilities: UI, file system, programming environment, system calls, API.
> - API → portability (OS-independent calls).
> - These are EXTERNAL, not resource management.

**QUICK CHECK 5**
*Q: A game written for Windows uses the Windows API. Why might the same code not run on Linux without changes?*
*A: The Windows API calls are Windows-specific; on Linux the equivalent functions have different names/behaviour, so the program must be re-linked or rewritten against the Linux API — APIs give portability only when a compatible API layer exists.*

---

## PART 6 — TRANSLATION SOFTWARE (20.06)

### 6.1 The analysis–synthesis model of a compiler

A compiler has a **front end** and a **back end**:

- **Front end** — *analysis* of the source code; unless errors are found, produces **intermediate code** expressing the full semantics (meaning) of the source.
- **Back end** — *synthesis* of **object code** from that intermediate code.

An **interpreter** shares the same analysis front end, but instead of producing a full translated program, once a line is found error-free and converted to intermediate code, **that line is executed immediately** — no separate translated version is produced.

**WHAT CAMBRIDGE ASKS — interpreter vs compiler (a classic definitional question):**
- **Compiler:** translates the *whole* source program into machine code (object code) before it is run; the translated program can be saved and re-run without re-translating; errors are reported after the whole compilation.
- **Interpreter:** translates and executes *line by line*; no separate object program is produced; an error stops execution at that line.
A common question asks *why an interpreter is useful for development* (immediate feedback, no separate build step, easier debugging) or *why a compiler produces faster final execution* (already in machine code).

> **MAIN THINGS TO MEMORISE**
> - Compiler = whole program → object code, saved, fast to run.
> - Interpreter = line by line, no object program, immediate but slower.

**QUICK CHECK 6.1**
*Q: You change one line of a 10,000-line compiled program and want to re-run it. What must happen that would NOT be needed with an interpreter?*
*A: You must recompile (at least that module / the whole program) to regenerate the object code; an interpreter would just re-read the changed line at runtime without a separate build step.*

### 6.2 Front-end analysis — the four stages

1. **Lexical analysis**
2. **Syntax analysis**
3. **Semantic analysis**
4. **Intermediate code generation**

**WHAT CAMBRIDGE ASKS — matching stages to descriptions (4 marks, appeared 9618/31 Oct/Nov 2022 Q4).** The mark scheme expects these exact pairings:
- **Lexical analysis** → *converting a sequence of characters into a sequence of tokens.*
- **Syntax analysis** → *using parsing algorithms to interpret the structure/meaning of a sequence of tokens* (building the parse tree).
- **Code generation** → *converting an intermediate representation of source code into an executable form.*
- **Optimisation** → *minimising a program's execution time and memory requirement.*
Note the exam explicitly contrasts these with **wrong** pairings (e.g. "directly executing instructions written in a scripting language" belongs to an interpreter, not code generation). Learn the four correct descriptions.

**Lexical analysis:** the source is a sequence of characters. Each meaningful unit is a **lexeme** (an identifier, keyword, operator, or symbol). The analyser strips whitespace/comments, then pattern-matches each lexeme. Example:

```
Var Count : integer ;
```

→ five lexemes: `Var`, `Count`, `:`, `integer`, `;`. `Var` and `integer` are keywords; `Count` is an identifier.

Each identifier gets an entry in the **symbol table**:

> **Symbol table:** a data structure in which each record contains the name and attributes of an identifier (data type, where declared, where assigned a value). Used by syntax analysis *and* later compilation stages; compilers are often multi-pass so it gets frequently updated.

The output of lexical analysis is a **tokenised** version of the source (each lexeme replaced by a token).

**WHAT CAMBRIDGE ASKS — why tokenise / what about whitespace?** A past discussion question asks *"why might a compiler tokenise white space rather than removing it all?"* A good answer: whitespace can be significant for layout-sensitive languages or for preserving source position information for error messages, or for differentiating tokens that would otherwise merge. (The textbook leaves this open — any reasoned answer scores.)

**Syntax analysis (parsing):** analyses program *constructs* and records the result as a **syntax / parse tree**. For `y := 2 * x + 4`, the tree's hierarchical structure guarantees multiplication happens before addition (Figure 20.09). This is where **syntax errors** (violations of the grammar) are caught.

**Semantic analysis:** establishes the *full meaning* — builds an **annotated abstract syntax tree** recording attributes (e.g. data type) for identifiers, also written to the symbol table. This is where **semantic errors** are caught — e.g. adding a string to an integer, or using an undeclared variable, or a type mismatch. **Distinction Cambridge likes:** syntax analysis checks *structure* (does it follow the grammar?); semantic analysis checks *meaning/validity* (are the types/declarations legal?).

**Intermediate code generation:** a common form is **three-address code** — at most three addresses per statement. For `y := a + (b * c – d) / e`:

```
temp := b * c
temp := temp – d
temp := temp / e
y := a + temp
```

This is a low-level, machine-independent representation that the back end turns into actual machine code.

> **MAIN THINGS TO MEMORISE**
> - Four stages IN ORDER: lexical → syntax → semantic → intermediate code gen.
> - Lexical = chars → tokens. Syntax = tokens → parse tree (structure). Semantic = meaning/type checks.
> - Token = categorised lexeme; symbol table holds identifier attributes.
> - Three-address code: max 3 addresses per statement.

**QUICK CHECK 6.2**
*Q: A program contains `x := "hello" + 3`. At which compilation stage is this error most likely caught, and why?*
*A: Semantic analysis — the syntax (structure) is fine, but adding a string to an integer is a type error caught when the compiler checks meaning/types.*

**QUICK CHECK 6.2b**
*Q: How many lexemes are in `PercentMark[Count] := Score * 10`?*
*A: Eight: `PercentMark`, `[`, `Count`, `]`, `:=`, `Score`, `*`, `10`. (Whitespace is removed; brackets and operators are lexemes.)*

### 6.3 Representing a language's grammar

**Syntax diagrams** (Figure 20.10): a picture of a grammar rule — e.g. an identifier starts with a letter, followed by any combination of letters/digits. Convention: options drawn *above* the main line, repetitions *below*. Limitation: a syntax diagram **cannot be built into a compiler as an algorithm** (it's a visual aid for humans).

**Backus–Naur Form (BNF):** a text notation. Example for an identifier:

```
<Identifier> ::= <Letter> | <Identifier><Letter> | <Identifier><Digit>
<Digit>       ::= 0|1|2|3|4|5|6|7|8|9
<Letter>      ::= <UpperCaseLetter> | <LowerCaseLetter>
<UpperCaseLetter> ::= A|B|...|Z
<LowerCaseLetter> ::= a|b|...|z
```

- `|` separates options; `::=` reads as "is defined as".
- Note the **recursive** definition of `<Identifier>` — without recursion you'd need a far more complicated rule to capture "a letter followed by any number of letters/digits."
- Unlike syntax diagrams, **BNF is general** (can describe any assembly of data) and **can be the basis of an algorithm**.

**WHAT CAMBRIDGE ASKS — complete a BNF definition (4 marks).** A standard question gives a partial BNF and asks you to complete it, e.g. for a signed integer:
```
<Digit>           ::= 0|1|2|3|4|5|6|7|8|9
<Sign>            ::= + | -
<Unsigned integer> ::= <Digit> | <Unsigned integer><Digit>
<Signed integer>  ::= <Sign><Unsigned integer>
```
The recursive `<Unsigned integer>` mirrors the recursive `<Identifier>` pattern. Cambridge marks each line; make sure your recursion is present (a non-recursive version that only allows single digits loses marks).

> **MAIN THINGS TO MEMORISE**
> - BNF uses `::=` ("is defined as") and `|` (options).
> - Recursion lets a rule repeat (e.g. identifier = letter then any number of letters/digits).
> - Syntax diagram = visual, not algorithmic; BNF = textual, can be algorithmic.

**QUICK CHECK 6.3**
*Q: Write the BNF rule for a `<Variable>` that is a letter followed by zero or more letters or digits. (This is the identifier rule — reproduce it.)*
*A: `<Variable> ::= <Letter> | <Variable><Letter> | <Variable><Digit>` with `<Letter>` and `<Digit>` defined as above. The recursion handles "zero or more further characters."*

### 6.4 Back-end synthesis

If the front end found syntax errors, the only back-end output is a **list of errors** (with explanation + location). With no errors, the main stage is **machine code generation** from intermediate code, possibly with **optimisation**:

- *Source-level optimisation:* e.g. `x := (a + b) * (a – b)` and `y := (a + 2 * b) * (a – b)` become `temp := (a – b); x := (a + b) * temp; y := x + temp * b` (computed `a – b` once instead of twice).
- *Loop-invariant code motion:* a statement inside a loop that does the same thing every iteration is moved *before* the loop.
- *Post-code optimisation:* efficient use of registers or memory once machine code exists.

**WHAT CAMBRIDGE ASKS — optimisation definition (1 mark):** "minimising a program's execution time and/or memory requirement." Be ready to give a concrete example (the `temp := (a–b)` reuse, or moving loop-invariant code out of a loop).

> **MAIN THINGS TO MEMORISE**
> - Back end = machine code generation + optimisation (if no errors).
> - Optimisation examples: common-subexpression elimination, loop-invariant code motion, register use.

**QUICK CHECK 6.4**
*Q: The statement `total := total + x` appears inside a loop but `x` never changes during the loop. What optimisation applies?*
*A: Loop-invariant code motion — move `temp := total + x` (or the unchanged part) outside the loop so it is computed once, not every iteration.*

### 6.5 Evaluating expressions with Reverse Polish Notation (RPN)

An assignment's algebraic expression is evaluated by converting the **infix** form to **RPN** (postfix). RPN **never needs brackets and has no precedence rules** — the order is entirely in the layout.

**Worked Example 20.01 — converting to/from RPN by hand**

To RPN, respecting precedence: `a + b * c` → first `b * c` → `a + b c *` → final. If it had been `(a + b) * c`, the essential brackets force `a b + c *`.

From RPN, scan until two identifiers are followed by an operator, convert, repeat:
`x 2 * y 3 * + 6 /` → `(x * 2) y 3 * + 6 /` → `(x * 2)(y * 3) + 6 /` → `((x * 2) + (y * 3)) / 6` → `(x * 2 + y * 3) / 6`.

**Worked Example 20.02 — using a syntax tree**

Build the tree with the *lowest-precedence* operator (`+`) at the root:

```
      +
     / \
    a   *
       / \
      b   c
```

Extract RPN by a **post-order traversal** (left–right–root): `a b c * +`.

**Worked Example 20.03 — the shunting-yard algorithm (stack-based conversion)**

Rules (tokens are "railroad wagons" shunted from the infix line to the RPN line):

- **Identifier** → passes straight to the RPN line.
- **Operator**:
  - if the stack is empty or holds a *lower-precedence* operator → push it onto the stack.
  - if the stack holds an *equal or higher-precedence* operator → pop that operator to the RPN line, then push the new operator.
- when the infix line is empty → pop remaining stack operators to the RPN line, one by one.

Trace for `a + b * c`: `+` enters stack; `*` (higher precedence) also enters; at the end `*` is popped, then `+` → `a b c * +`. (For `a * b + c`, `*` enters first but is popped before `+` enters.)

**Evaluating an RPN expression with a stack** — for `x 2 * y 3 * + 6 /` with $x=3, y=4$:

- push 3, push 2, `*` → pop 3,2 → 6, push 6
- push 4, push 3, `*` → pop 4,3 → 12, push 12
- `+` → pop 12,6 → 18, push 18
- push 6, `/` → pop 18,6 → **3**

So the expression evaluates to **3**.

**WHAT CAMBRIDGE ASKS — RPN is heavily tested and easy marks if you practise.** Real past paper (9618/31 Oct/Nov 2022 Q5):
- **5(a) [1 mark]** Write `a * b + b - d + 15` in RPN → mark scheme answer: **`a b * b + d - 15 +`**. (Left-to-right at equal precedence: `a*b` first, then `+b`, then `-d`, then `+15`.)
- **5(b)(i) [1 mark]** Write `a b - c d + * a /` in infix → **`(a - b) * (c + d) / a`**.
- **5(b)(ii) [1 mark]** Evaluate with a=5, b=10, c=27, d=12 → `(5-10)*(27+12)/5 = (-5)*39/5 = -195/5 = ` **`-39`**.

**Method to never get these wrong:** for infix→RPN, apply operator precedence and *left-to-right for equal precedence*; for RPN→infix, insert brackets around each `(operand operator operand)` reduction; for evaluation, use the stack mechanically — Cambridge gives the mark for the final numeric answer, so show the stack steps to be safe.

> **MAIN THINGS TO MEMORISE**
> - RPN = postfix, no brackets, no precedence rules.
> - infix→RPN: precedence + left-to-right at equal precedence.
> - Evaluation: stack — push operands, on operator pop two, compute, push result.
> - Past-paper answers: `a*b+b-d+15` → `a b * b + d - 15 +`; `(a-b)*(c+d)/a` from `a b - c d + * a /`.

**QUICK CHECK 6.5**
*Q: Convert `(a + b) * c` to RPN, then evaluate it with a=2, b=3, c=4 using the stack method.*
*A: RPN = `a b + c *`. Stack: push 2, push 3, `+` → pop 3,2 → 5, push 5; push 4, `*` → pop 4,5 → 20. Answer = 20.*

**QUICK CHECK 6.5b**
*Q: Write the infix for `a b c * + d /`.*
*A: Reduce `b c *` → `(b*c)`; then `a (b*c) +` → `(a + b*c)`; then `(a+b*c) d /` → `(a + b * c) / d`.*

---

## PART 7 — CHAPTER SUMMARY (exact revision bullet points)

- The operating system provides resource management: scheduling of processes, memory management, and control of the I/O system.
- For the user, the OS provides an interface, a file system, and application programming interfaces (APIs).
- A modular approach provides a flexible structure for the operating system (often with a microkernel).
- There are five states for a process: new, ready, running, waiting, terminated.
- A process may be interrupted by an error, a need for I/O, or the scheduling algorithm.
- A virtual memory system uses paging and a memory management unit that uses a page table.
- Compiler operation has a front end (analysis) and a back end (synthesis).
- Backus–Naur Form is used to represent the rules of a grammar.
- Reverse Polish Notation is used for the evaluation of expressions.

---

## PART 8 — FULL WORKED EXAM-STYLE ANSWERS
*(Expansions include real past-paper phrasing and mark-scheme wording.)*

### Question 1 — Processes and the five-state model

**(a) Explain the concept of a process. [2]**

A **process** is a program that is in memory and has an associated **process control block (PCB)** — i.e. it is "a program being executed," not merely the program file on disk. [2]

**(b) Identify three of the five process states and explain each. [6 — 2 each]**

Any three of:

- **New** — a process has just arrived in memory and its PCB has been created, before it becomes ready. [2]
- **Ready** — the process is in memory and waiting to be given access to the CPU by the dispatcher. [2]
- **Running** — the process currently has access to the CPU and is executing its instructions. [2]
- **Waiting** (suspended/blocked) — the process cannot continue until some event occurs (e.g. an I/O operation completes). [2]
- **Terminated** — the process has finished execution. [2]

*(Past-paper style: Cambridge often asks for exactly three with 2 marks each — state the name AND the meaning, don't just list names.)*

### Question 2 — Scheduling algorithms

**(a) Identify two scheduling algorithms and classify each. [4 — 2 each]**

- **First come first served (FCFS)** — **non-preemptive**; uses a FIFO queue. [2]
- **Round-robin** — **preemptive** (halts a process when its time slice expires); uses a FIFO queue, normally without priorities. [2]
- *(Priority-based scheduling — preemptive — also accepted.)* [2]

**(b) Two criteria for assigning priority. [2 — 1 each]**

Any two of: estimated time of execution; estimated remaining time; length of time already in the ready queue; whether the process is I/O-bound or CPU-bound. [1 each]

### Question 3 — Memory management techniques

**(a) Definitions of partitioning, scheduling, and paging. [3 — 1 each]**

- **Partitioning** — dividing memory so a whole process loads into one partition (fixed, or dynamic where the partition matches the process size). [1]
- **Scheduling** — deciding which process gets CPU access and when (process scheduling); for memory, deciding how much memory each process gets. [1]
- **Paging** — dividing a process into equal-sized pages and memory into equal-sized frames, mapped by a page table. [1]

**(b) Two ways they might be combined. [2]**

- **Segmentation + paging**: a large process is divided into segments, and those segments are themselves divided into pages. [1]
- **Paging + virtual memory**: paging is the mechanism that *creates* virtual memory (pages swapped disk↔memory via the page table). [1]

**(c) Virtual memory**

**i. Which technique creates it. [1]** Paging. [1]

**ii. Two advantages. [4 — 2 each]**

- A program can be larger than main memory — it can use **more addresses than physically exist**, so big programs run without needing all of RAM. [2]
- Only the pages actually needed at a given moment must be in memory, so memory is used **more efficiently** (parts not yet reached stay on disk; more processes can be resident). [2]

**iii. One problem. [2]** **Disk thrashing** — a repetitive state where loading one page immediately requires another, causing near-constant loading/unloading of pages and severe performance loss. [2]

**(d) ONE difference between paging and segmentation. [1]** Paging divides memory into fixed (equal) size blocks; segmentation divides memory into variable-sized blocks. *(Exact mark-scheme wording — memorise it.)*

### Question 4 — Compilers (matching + stages)

**(a) Match each stage of compilation to its description. [4 — 1 each]**
*(Past paper 9618/31 Oct/Nov 2022 Q4.)*

- **Lexical analysis** → converting a sequence of characters into a sequence of tokens.
- **Syntax analysis** → using parsing algorithms to interpret the structure/meaning of a sequence of tokens.
- **Code generation** → converting an intermediate representation of source code into an executable form.
- **Optimisation** → minimising a program's execution time and memory requirement.

**(b) Front end vs back end aims. [2 — 1 each]**

- **Front end** — *analysis* of the source code, producing intermediate code that fully expresses its meaning. [1]
- **Back end** — *synthesis* of object (machine) code from the intermediate code. [1]

**(c) Two front-end processes. [2 — 1 each]** Any two of: lexical analysis, syntax analysis, semantic analysis, intermediate code generation. [1 each]

**(d) Two back-end processes. [2 — 1 each]** Any two of: machine code generation, optimisation, error listing (if errors found). [1 each]

### Question 5 — BNF

Complete the BNF definition of a signed integer:

```
<Digit>           ::= 0|1|2|3|4|5|6|7|8|9
<Sign>            ::= + | -
<Unsigned integer> ::= <Digit> | <Unsigned integer><Digit>
<Signed integer>  ::= <Sign><Unsigned integer>
```

*(The recursive `<Unsigned integer>` mirrors the recursive `<Identifier>` pattern — a digit followed by any number of further digits.)*

### Question 6 — RPN conversion *(real past-paper style)*

**(a) Write `a * b + b - d + 15` in RPN. [1]** → `a b * b + d - 15 +`

**(b) Write `a b - c d + * a /` in infix. [1]** → `(a - b) * (c + d) / a`

**(c) Evaluate `a b - c d + * a /` with a=5, b=10, c=27, d=12. [1]**
`(5 - 10) * (27 + 12) / 5 = (-5) * 39 / 5 = -195 / 5 = ` **`-39`**

**(d) Give the RPN equivalent of `(a + 6) + b / c`. [2]** → `a 6 + b c / +`

**(e) Give the infix equivalent of `a 3 b * 6 c * - +`. [2]** → `a + (3 * b – 6 * c)` or `a + 3 * b – 6 * c`

### Question 7 — Interpreter vs compiler [typical 4-mark comparison]

| | Compiler | Interpreter |
|---|---|---|
| Translation | Whole program → machine code before running | Line by line, executed as translated |
| Output | Produces a separate object program | No separate translated program produced |
| Errors | Reported after full compilation | Stops at the line where the error occurs |
| Execution speed | Faster (already machine code) | Slower (re-translates each run) |
| Use | Final/distributed software | Development, scripting, immediate testing |

### Question 8 — Syntax diagrams

A syntax diagram shows an **assignment statement** = `Variable = Variable Operator Variable`; a **variable** = `Letter` followed by any number of `Letter`s; with `Letter` and `Operator` as their own diagrams. The hierarchical picture enforces the same structure a parse tree would — which is exactly why syntax analysis can build that tree from the diagram's rules. Unlike BNF, a syntax diagram cannot be directly built into a compiler as an algorithm.

---

## PART 9 — QUICK-FIRE DEFINITION DRILL

State each from memory, in the exact style the exam rewards:

1. **BIOS** — the basic input/output system stored in ROM that starts the bootstrap program to load the OS.
2. **Bootstrap program** — the program (started by the BIOS) that loads the OS into memory and sets it running.
3. **Multi-programming** — several programs held in memory; only one uses the CPU at a time but others are ready.
4. **Time-sharing** — many users simultaneously logged in, sharing the CPU.
5. **Kernel mode** — the OS mode with sole access to protected memory and system functions user mode cannot reach.
6. **Process** — a program in memory with an associated process control block.
7. **PCB** — a data structure holding all data relevant to running a process.
8. **Thread** — a part of a program handled as an individual process when executed.
9. **Preemptive scheduling** — can halt a running process (often to apply priorities).
10. **Segmentation** — dividing a large process into unequal-sized segments for loading.
11. **Paging** — dividing a process into equal-sized pages mapped to equal-sized frames.
12. **Virtual memory** — a paging mechanism letting a program use more addresses than exist in main memory.
13. **Page fault** — when a needed page is not currently in memory and must be fetched from disk.
14. **Disk thrashing** — repetitive page loading/unloading that cripples performance.
15. **Device driver** — software that translates between the OS and a specific hardware device.
16. **System call** — a request from a program to the OS to perform a privileged service.
17. **API** — application programming interface; aims to give programs portability across OSes.
18. **Symbol table** — a data structure recording each identifier's name and attributes.
19. **Lexeme** — a meaningful unit of source text (identifier, keyword, operator, symbol).
20. **Token** — the categorised, compressed representation of a lexeme output by lexical analysis.
21. **BNF** — Backus–Naur Form, a text notation using `::=` and `|` to define a grammar; can be algorithmic.
22. **RPN** — Reverse Polish Notation; postfix, bracket-free, no precedence rules.
23. **Optimisation** — minimising a program's execution time and/or memory requirement.

---

## PART 10 — SELF-TEST CHECKLIST

- [ ] State the boot sequence: ROM BIOS → bootstrap → OS loaded into memory.
- [ ] Distinguish internal viewpoint (resource management) from external viewpoint (user facilities) — and keep the two lists separate in an answer.
- [ ] Explain user mode vs kernel mode and why the kernel runs all the time; why memory is protected.
- [ ] Describe the I/O timescale problem (GHz CPU vs slow devices) and why scheduling/interrupts exist.
- [ ] List the five process states and draw the transitions between them.
- [ ] Define process, PCB, and thread.
- [ ] Classify FCFS (non-preemptive) and round-robin (preemptive); give two priority criteria.
- [ ] Define segmentation, paging, and virtual memory; explain how a page table maps logical→physical.
- [ ] State the exact 1-mark difference: paging = fixed blocks, segmentation = variable blocks.
- [ ] Explain disk thrashing and why it is the downside of virtual memory.
- [ ] State the four front-end analysis stages and what the symbol table records.
- [ ] Match compilation stages to descriptions (lexical/syntax/code-gen/optimisation) from the past paper.
- [ ] Write a simple BNF rule (identifier / unsigned integer) including recursion.
- [ ] Convert an infix expression to RPN by hand and by syntax-tree post-order traversal.
- [ ] Trace the shunting-yard algorithm and evaluate an RPN expression using a stack.
- [ ] Compare interpreter vs compiler (translation, output, errors, speed).
