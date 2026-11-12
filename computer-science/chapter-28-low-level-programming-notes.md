# 📘 Chapter 28: Low-Level Programming - Cambridge International AS & A Level Computer Science (9618)

## Cambridge International AS & A Level Computer Science - Part 4

> **Rule + fully solved examples.** Everything the examiner can ask from Chapter 28: the 9618 instruction set, symbolic addresses, writing assembly for assignment/selection/repetition/input-output, immediate/direct/indirect/indexed/relative addressing, and tracing low-level programs. Every section ends with worked examples and exam-style questions with full mark-earning solutions.

**Learning objectives (Chapter 28):**
- Write low-level code that uses various addressing modes: immediate, direct, indirect, indexed and relative

---

## 28.01 Processor Instruction Set

Assembly language uses **mnemonics** (opcodes) and **operands**. The 9618 instruction set assumes one general-purpose register, the **accumulator (ACC)**, and one **index register (IX)**.

Notation:

- `#` means **immediate** addressing (the operand is a value, not an address).
- `B` prefixes binary, e.g. `B01001010`.
- `&` prefixes hexadecimal, e.g. `&4A`.
- `<address>` may be an absolute address (a number) or a symbolic address (a label).

### 28.01.1 The instruction set

| Category | Opcode | Operand | Meaning |
|---|---|---|---|
| **Data movement** | `LDM` | `#n` | Load denary number `n` into ACC (immediate) |
| | `LDD` | `<address>` | Load contents of address into ACC (direct) |
| | `LDI` | `<address>` | The address to use is stored at `<address>`; load contents of that second address into ACC (indirect) |
| | `LDX` | `<address>` | Load from address `<address> + IX` into ACC (indexed) |
| | `LDR` | `#n` | Load denary number `n` into IX (immediate) |
| | `MOV` | `<register>` | Move ACC to the given register (IX) |
| | `STO` | `<address>` | Store ACC at address |
| | `STX` | `<address>` | Store ACC at `<address> + IX` (indexed)* |
| | `STI` | `<address>` | Store ACC at the address stored at `<address>` (indirect)* |
| **Arithmetic** | `ADD` | `<address>` or `#n` | Add contents of address / number `n` to ACC |
| | `SUB` | `<address>` or `#n` | Subtract contents of address / number `n` from ACC |
| | `INC` | `ACC` or `IX` | Add 1 to register |
| | `DEC` | `ACC` or `IX` | Subtract 1 from register |
| **Comparison/jump** | `JMP` | `<address>` | Jump unconditionally |
| | `CMP` | `<address>` or `#n` | Compare ACC with value |
| | `CMI` | `<address>` | Compare ACC with contents of the address stored at `<address>` (indirect) |
| | `JPE` | `<address>` | Jump if the previous compare was true (equal) |
| | `JPN` | `<address>` | Jump if the previous compare was false (not equal) |
| **Input/output** | `IN` | — | Key in a character; store its ASCII value in ACC |
| | `OUT` | — | Output the character whose ASCII value is in ACC |
| **Bit manipulation** | `AND` | `#n` or `<address>` | Bitwise AND with ACC |
| | `XOR` | `#n` or `<address>` | Bitwise XOR with ACC |
| | `OR` | `#n` or `<address>` | Bitwise OR with ACC |
| | `LSL` | `#n` | Logical shift left `n` places (zeros into the right) |
| | `LSR` | `#n` | Logical shift right `n` places (zeros into the left) |
| **Other** | `END` | — | Return control to the operating system |
| | `<label>:` | — | Label an instruction or a data location |

\* `STX` and `STI` are **not** in the 9618 syllabus instruction set. `STX`/`STI` appear in the coursebook for completeness; do not rely on them in exam answers unless the question's own instruction set includes them.

> **Exam tip:** the 9618 set does **not** include relative (base-register) addressing, `STX` or `STI`. If a question provides its own table, use only the instructions in that table.

### 28.01.2 The accumulator is central

Almost every operation goes through ACC:

- To process a value, **load** it into ACC first.
- Do arithmetic/logic in ACC.
- **Store** the result back to memory.
- To output a number, convert it to its character string first (unless the question only asks for a character).

**Worked example 28.01 — `A ← 2`, `B ← 10`, `C ← A + B`, `D ← A − B`**

```
LDM #2
STO A
LDM #10
STO B
LDD A
ADD B
STO C
LDD A
SUB B
STO D
END
```

**What the examiner wants:** one correct load, operation and store per assignment; `ADD B`/`SUB B` operate on the **contents** of B, not its address.

---

## 28.02 Symbolic Addresses

A **label** is a symbolic name for a memory location. The assembler allocates the actual address during assembly.

**Why use labels?**

- You do not need to know absolute addresses.
- Inserting instructions does not require rewriting every address.
- Programs are easier to read and maintain.

```
LOOP:   LDD A
        INC ACC
        STO A
        CMP #5
        JPN LOOP
        END
A:      0
```

`LOOP` and `A` are symbolic addresses; the assembler resolves them.

> **Exam tip:** a label on an instruction marks the **address of that instruction**; a label on a data item marks the **address of that data**. Both are used as operands.

---

## 28.03 Problem-Solving and Assembly-Language Programs

Break the problem into the standard constructs: **assignment**, **selection**, **repetition** and **input/output**.

### 28.03.1 Assignment

| Pseudocode | Assembly | Explanation |
|---|---|---|
| `A ← 34` | `LDM #34` / `STO A` | Value must be generated in ACC first |
| `B ← B + 1` | `LDD B` / `INC ACC` / `STO B` | Load, increment, store |
| `B ← B + A` | `LDD B` / `ADD A` / `STO B` | Load first value, add second, store |
| `A ← −A` | `LDM #0` / `SUB A` / `STO A` | 0 − A gives two's complement negation |
| `A ← −A` (alternative) | `LDD A` / `XOR #&FF` / `INC ACC` / `STO A` | One's complement then +1 |

**Worked example 28.02 — `A ← B + C − D`**

```
LDD B
ADD C
SUB D
STO A
END
```

### 28.03.2 Selection

**If without else:**

```
IF A = 0 THEN
    B ← B + 1
ENDIF
```

```
        LDD A
        CMP #0
        JPN ENDIF
        LDD B
        INC ACC
        STO B
ENDIF:  ...
```

`CMP #0` sets the comparison result. `JPN ENDIF` skips the THEN block when the comparison is **false**.

**If with else:**

```
IF A = B THEN
    OUTPUT "Y"
ELSE
    OUTPUT "N"
ENDIF
```

```
        LDD A
        SUB B
        CMP #0
        JPN ELSE
        LDM #89        ; ASCII 'Y'
        OUT
        JMP ENDIF
ELSE:   LDM #78        ; ASCII 'N'
        OUT
ENDIF:  ...
```

> **Exam tip:** to test equality, subtract and compare with 0. To test `A > B`, subtract B from A and use the sign/zero result if the instruction set provides conditional jumps; with only `JPE`/`JPN`, test equality and structure the branches accordingly.

### 28.03.3 Repetition

**REPEAT ... UNTIL:**

```
A ← 0
REPEAT
    OUTPUT "*"
    A ← A + 1
UNTIL A = 5
```

```
        LDM #0
        STO A
LOOP:   LDM #42        ; ASCII '*'
        OUT
        LDD A
        INC ACC
        STO A
        CMP #5
        JPN LOOP       ; repeat while A ≠ 5
        END
A:      0
```

**Worked example 28.03 — sum 1 to 5**

```
        LDM #0
        STO Total
        LDM #1
        STO Number
LOOP:   LDD Total
        ADD Number
        STO Total
        LDD Number
        INC ACC
        STO Number
        CMP #6
        JPN LOOP
        END
Total:  0
Number: 0
```

At the end, `Total = 15`. The loop stops when `Number = 6` (after adding 5).

### 28.03.4 Input and output

| Pseudocode | Assembly |
|---|---|
| `INPUT A` | `IN` / `STO A` |
| `OUTPUT B` (one character) | `LDD B` / `OUT` |
| `OUTPUT "text"` | Loop with `LDX` over consecutive memory locations until ASCII 13 |

`IN` stores the **ASCII value** of the key pressed. `OUT` displays the character with the ASCII value in ACC. Numeric output requires converting the number to its digit characters first.

**Worked example 28.04 — echo characters until 'N'**

```
        LDM #0
        STO Count
LOOP:   IN
        STO Character
        LDD Count
        INC ACC
        STO Count
        LDD Character
        CMP #78        ; ASCII 'N'
        JPN LOOP
        END
Count:     0
Character: 0
```

### 28.03.5 Worked example — two-digit BCD

**Task:** input two digits and store their BCD representation at `Result`.

ASCII '0' = `0011 0000`; the low nibble is the digit value. `AND #&0F` masks off the high nibble. To combine two digits, shift the first into the high nibble and OR the second into the low nibble.

```
        IN
        AND #&0F       ; ASCII → digit value
        LSL #4         ; move to upper nibble
        STO Result
        IN
        AND #&0F       ; second digit
        OR Result      ; combine with high nibble
        STO Result
        END
Mask:   &0F
Result: &00
```

If the input is `"4"` then `"7"`, `Result = &47` (BCD for 47).

> **Exam tip:** the mask `&0F` (binary `00001111`) is the standard ASCII-to-digit conversion. `LSL #4` moves a digit into the high nibble.

---

## 28.04 Addressing Modes

An **addressing mode** defines how the operand of an instruction identifies the data.

### 28.04.1 Immediate addressing

The operand **is the value**:

```
LDM #25        ; ACC ← 25
ADD #3         ; ACC ← ACC + 3
```

No memory access is needed to fetch the operand. Used for constants.

### 28.04.2 Direct addressing

The operand is the **address** of the data:

```
LDD A          ; ACC ← contents of address A
STO B          ; contents of B ← ACC
```

The instruction contains the address itself. Also called **absolute addressing** when the address is a fixed number.

### 28.04.3 Indirect addressing

The operand is the address of a location that **contains the address** to use:

```
LDI HEADPTR    ; ACC ← contents of (contents of HEADPTR)
STI TAILPTR    ; contents of (contents of TAILPTR) ← ACC
```

This is useful for **pointers** and for passing parameters by reference: the pointer can be changed at run time without changing the instruction.

**Worked example 28.05 — pointer**

Suppose `PTR` contains `200`, and memory location `200` contains `55`.

- `LDD PTR` → ACC = 200 (the pointer value).
- `LDI PTR` → ACC = 55 (the value pointed to).

### 28.04.4 Indexed addressing

The effective address is `<address> + IX`:

```
LDR #0         ; IX ← 0
LDX Array      ; ACC ← contents of Array + 0
INC IX
LDX Array      ; ACC ← contents of Array + 1
```

This is how arrays are traversed: the base address is fixed and IX is the index. `STX` would store to `Array + IX`, but it is not in the 9618 set.

**Worked example 28.06 — output a string**

```
        LDM #-1
        MOV IX
LOOP:   INC IX
        LDX Text
        OUT
        CMP #13        ; carriage return ends the string
        JPN LOOP
        END
Text:   "Hello", 13
```

Starting IX at `-1` and incrementing **before** the load means the first character is at `Text + 0`.

### 28.04.5 Relative addressing

A **relative address** is an offset from a base address held in a **base register (BR)**:

```
STO [BR] + 10
JPN [BR] + 2
```

The program can be loaded anywhere in memory because the actual address is `BR + offset`. This is **position-independent code**.

| Mode | Operand contains | Effective address | Example |
|---|---|---|---|
| Immediate | The value | None (value used directly) | `LDM #5` |
| Direct | Address of data | Operand | `LDD A` |
| Indirect | Address of a pointer | Contents of operand | `LDI PTR` |
| Indexed | Base address | Operand + IX | `LDX Array` |
| Relative | Offset | BR + offset | `STO [BR]+10` |

> **Exam tip:** relative addressing is not in the 9618 instruction set, but the concept is examinable in theory questions. The key phrase is "address relative to a base register, so the program can be relocated".

### 28.04.6 Absolute vs symbolic vs relative

Table 28.06 from the coursebook compares the same program written three ways:

| Symbolic | Relative (BR) | Absolute |
|---|---|---|
| `LDM #0` | `LDM #0` | `100 LDM #0` |
| `STO A` | `STO [BR]+10` | `201 STO 210` |
| `LOOP: LDM #42` | `LDM #42` | `202 LDM #42` |
| `OUT` | `OUT` | `203 OUT` |
| `LDD A` | `LDD [BR]+10` | `204 LDD 210` |
| `INC ACC` | `INC ACC` | `205 INC ACC` |
| `STO A` | `STO [BR]+10` | `206 STO 210` |
| `CMP #5` | `CMP #5` | `207 CMP #5` |
| `JPN LOOP` | `JPN [BR]+2` | `208 JPN 202` |
| `END` | `END` | `209 END` |
| `A: 0` | `A` at offset 10 | `210: 0` |

- **Symbolic** is readable and relocatable by the assembler.
- **Relative** is relocatable at load time.
- **Absolute** is fixed and cannot be moved.

### 28.04.7 Why `END` matters

`END` returns control to the operating system. Without it, the processor continues into the next memory location and interprets whatever bits are there as an instruction, often crashing.

---

## 28.05 From Assembly to Machine Code

An **assembler** translates assembly language into machine code. A common design is the **two-pass assembler**:

**Pass 1 — build the symbol table:**

- Scan the source.
- Record every label and its address (the location counter).
- Determine the size of each instruction/data item.

**Pass 2 — generate code:**

- Scan again.
- Translate each mnemonic to its opcode.
- Replace symbolic operands with addresses from the symbol table.
- Output the machine code.

**Why two passes?** A forward jump may refer to a label that has not yet been seen. Pass 1 records all labels first, so pass 2 can resolve forward references.

**Other assembler features:**

- **Macros** — named sequences of instructions expanded at assembly time.
- **Directives** — instructions to the assembler (e.g. reserve storage), not the processor.
- **Linking/loading** — combining object modules and placing them in memory.

> **Exam tip:** "pass 1 builds the symbol table, pass 2 generates machine code" is the standard two-mark answer. Mention forward references to explain why two passes are needed.

---

## 📝 Exam-style Questions with Full Solutions

### Question 1 — AND and BCD (10 marks)

The instruction set includes `LDD`, `STO`, `ADD`, `IN`, `AND`, `LSL`, `END`, and labels.

(a) Explain the operation of `AND`. [1]
(b) Write an AND instruction to convert an ASCII digit in ACC to its integer value. [1]
(c) Write assembly code to input a two-digit number and store its BCD representation at `Result`. [7]

**Solution:**

(a) `AND` performs a bitwise AND between the contents of ACC and the operand, leaving the result in ACC. A bit in the result is 1 only if both corresponding bits are 1.

(b) `AND #&0F` (mask `00001111`). This clears the high nibble (the ASCII `0011`) and keeps the low nibble (the digit value).

(c)

```
        IN
        AND #&0F
        LSL #4
        STO Result
        IN
        AND #&0F
        OR Result
        STO Result
        END
Mask:   &0F
Result: &00
```

**What the examiner wants:** input first digit; mask; shift left 4; store; input second; mask; OR/ADD to combine; store; `END`. Each step earns a mark.

### Question 2 — Trace a loop (6 marks)

Trace this program and state the final value of `A`.

```
        LDM #0
        STO A
        LDM #3
        STO B
LOOP:   LDD A
        ADD B
        STO A
        LDD B
        DEC ACC
        STO B
        CMP #0
        JPN LOOP
        END
A:      0
B:      0
```

**Solution:**

| Iteration | A before | B before | A after | B after | `B = 0`? |
|---|---|---|---|---|---|
| 1 | 0 | 3 | 3 | 2 | false |
| 2 | 3 | 2 | 5 | 1 | false |
| 3 | 5 | 1 | 6 | 0 | true |

Final `A = 6`. The loop adds 3 + 2 + 1.

### Question 3 — Selection (6 marks)

Write assembly code for:

```
IF A <> 0 THEN
    B ← A
ELSE
    B ← B − 1
ENDIF
```

**Solution:**

```
        LDD A
        CMP #0
        JPE ELSE
        LDD A
        STO B
        JMP ENDIF
ELSE:   LDD B
        SUB #1
        STO B
ENDIF:  END
```

`CMP #0` tests A. If A = 0, `JPE ELSE` takes the else branch; otherwise the THEN branch stores A in B, then jumps over the else.

### Question 4 — Addressing modes (5 marks)

State the addressing mode used in each instruction.

(a) `LDM #12`
(b) `LDD Total`
(c) `LDI PTR`
(d) `LDX Array`
(e) `STO [BR] + 6`

**Solution:**

(a) Immediate — the operand is the value 12.
(b) Direct — the operand is the address `Total`.
(c) Indirect — `PTR` holds the address of the data.
(d) Indexed — effective address is `Array + IX`.
(e) Relative — effective address is base register + 6.

### Question 5 — Indexed string output (7 marks)

Write assembly code to output the characters stored at `Text`, stopping at ASCII 13.

**Solution:**

```
        LDM #-1
        MOV IX
LOOP:   INC IX
        LDX Text
        OUT
        CMP #13
        JPN LOOP
        END
Text:   "Exam", 13
```

Starting IX at −1 and incrementing before `LDX` makes the first character `Text + 0`. The loop stops when the carriage return (13) is loaded and output.

### Question 6 — Two-pass assembler (4 marks)

Explain why an assembler may need two passes.

**Solution:**

In pass 1 the assembler scans the source and builds a **symbol table** mapping every label to its address. It cannot generate machine code for a forward reference yet because the label's address is unknown. In pass 2 it scans again, translates opcodes and replaces symbolic operands with addresses from the symbol table. Two passes therefore allow forward jumps and forward data references to be resolved.

---

# 📋 Formula / Fact Sheet (Chapter 28)

**Registers:** ACC (accumulator), IX (index register), BR (base register, relative addressing).

**Notation:** `#` immediate; `B` binary; `&` hexadecimal; `<address>` absolute or symbolic.

**Core instructions:** `LDM`, `LDD`, `LDI`, `LDX`, `LDR`, `MOV`, `STO`, `ADD`, `SUB`, `INC`, `DEC`, `JMP`, `CMP`, `CMI`, `JPE`, `JPN`, `IN`, `OUT`, `AND`, `OR`, `XOR`, `LSL`, `LSR`, `END`.

**Addressing modes:**

- Immediate: operand is the value.
- Direct: operand is the address.
- Indirect: operand is the address of a pointer.
- Indexed: address + IX.
- Relative: BR + offset (not in 9618 set).

**Common patterns:**

- `A ← n`: `LDM #n` / `STO A`
- `B ← B + A`: `LDD B` / `ADD A` / `STO B`
- `IF A = 0`: `LDD A` / `CMP #0` / `JPN ENDIF`
- `IF A = B`: `LDD A` / `SUB B` / `CMP #0` / `JPN ELSE`
- Loop: label / body / update / `CMP` / `JPN label`
- ASCII digit → value: `AND #&0F`
- Two-digit BCD: first digit `AND #&0F`, `LSL #4`, store; second `AND #&0F`, `OR` first, store.

**ASCII values:** `'0' = 48`, `'A' = 65`, `'a' = 97`, `'Y' = 89`, `'N' = 78`, `'*' = 42`, carriage return = 13.

**Assembler:** pass 1 builds symbol table; pass 2 generates machine code; resolves forward references.

# ⚡ Quick Reference Card

1. **Everything goes through ACC** — load, operate, store.
2. **`#` means the value itself**, not the address.
3. **Immediate = value; direct = address; indirect = pointer; indexed = base + IX; relative = BR + offset.**
4. **`LDI` follows one extra pointer** compared with `LDD`.
5. **`LDX` is how arrays are traversed** — increment IX each time.
6. **CMP then JPE/JPN** — equality only; structure other comparisons with subtraction.
7. **Always `END`** or the CPU runs into data.
8. **ASCII to digit:** `AND #&0F`; **digit to high nibble:** `LSL #4`.
9. **Two-pass assembler** handles forward references.
10. **Symbolic labels** make programs readable and relocatable; absolute addresses do not.
