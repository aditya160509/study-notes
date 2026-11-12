# 📘 Chapter 19: Logic Circuits and Boolean Algebra - Cambridge International AS & A Level Computer Science (9618)

## Cambridge International AS & A Level Computer Science - Part 3

> **Rule + fully solved examples.** Everything the examiner can ask from Chapter 19: logic gates and truth tables, combinational and sequential circuits, the SR flip-flop, Boolean algebra and its laws, De Morgan's laws, half and full adders, and Karnaugh maps. Every section ends with worked examples and exam-style questions with full mark-earning solutions.

**Learning objectives (Chapter 19):**
- Understand and use the standard logic gates: NOT, AND, OR, NAND, NOR, XOR
- Construct truth tables for logic circuits and derive Boolean expressions from them
- Understand combinational and sequential logic circuits
- Understand the SR flip-flop and its use as a 1-bit storage device
- Use Boolean algebra, including De Morgan's laws, to simplify expressions
- Design and analyse half-adder and full-adder circuits
- Use Karnaugh maps to simplify Boolean expressions

---

## 19.01 Logic Circuits

A **logic circuit** is a circuit built from logic gates. Each gate performs a Boolean operation on one or more binary inputs and produces a single binary output. Logic circuits are the physical implementation of Boolean expressions, and Boolean expressions are the mathematical model of logic circuits.

### 19.01.1 The standard gates

| Gate | Symbolic expression | Behaviour | Truth table |
|---|---|---|---|
| **NOT** | `¬A` or `A'` | Output is the inverse of the input | `0 → 1`, `1 → 0` |
| **AND** | `A ∧ B` or `A.B` | Output 1 only when **both** inputs are 1 | `00→0, 01→0, 10→0, 11→1` |
| **OR** | `A ∨ B` or `A+B` | Output 1 when **at least one** input is 1 | `00→0, 01→1, 10→1, 11→1` |
| **NAND** | `¬(A ∧ B)` | AND followed by NOT | `00→1, 01→1, 10→1, 11→0` |
| **NOR** | `¬(A ∨ B)` | OR followed by NOT | `00→1, 01→0, 10→0, 11→0` |
| **XOR** | `A ⊕ B` | Output 1 when inputs are **different** | `00→0, 01→1, 10→1, 11→0` |

**NAND and NOR are universal gates.** Any other gate can be built using only NAND gates, or only NOR gates. This is why manufacturers can mass-produce a single gate type and build every circuit from it.

> **KEY TERMS**
> - **Combinational circuit**: a circuit whose output depends only on the current input values.
> - **Sequential circuit**: a circuit whose output depends on the current inputs **and** on the previous output (it has memory).
> - **Truth table**: a table showing the output for every possible combination of inputs.

### 19.01.2 Number of rows in a truth table

For `n` inputs there are `2^n` possible input combinations, so the truth table has `2^n` rows.

| Inputs | Rows |
|---|---|
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |

Write the input columns in binary counting order (`000, 001, 010, ...`) so that no combination is missed and no combination is repeated.

### 19.01.3 From a Boolean expression to a circuit

Build the circuit from the **inside out**, following operator precedence:

1. Brackets
2. NOT
3. AND
4. OR

**Worked example 19.01 — draw `Q = (A ∧ B) ∨ ¬C`**

1. AND gate with inputs `A` and `B` → intermediate `X`.
2. NOT gate with input `C` → intermediate `Y`.
3. OR gate with inputs `X` and `Y` → output `Q`.

The circuit uses one AND, one NOT and one OR gate. If the expression were `Q = A ∧ (B ∨ ¬C)`, the OR would be built before the final AND — brackets change the circuit, not just the appearance of the expression.

### 19.01.4 From a circuit to a Boolean expression

Label each gate output as you move from left to right, then substitute the labels into the final gate.

**Worked example 19.02 — circuit with two NOTs, two ANDs and one OR**

Suppose the circuit computes:

- `X = ¬A ∧ B`
- `Y = A ∧ ¬B`
- `Q = X ∨ Y`

Then `Q = (¬A ∧ B) ∨ (A ∧ ¬B)`. This is the XOR function, `Q = A ⊕ B`: the output is 1 when exactly one input is 1.

### 19.01.5 Evaluating a circuit

Substitute the input values and work through the gates in order. A useful check is to evaluate every intermediate label, not just the final output, because exam questions often ask for the values at labelled points.

**Worked example 19.03 — evaluate `Q = ¬(A ∧ B) ∨ C` for `A=1, B=0, C=0`**

- `A ∧ B = 1 ∧ 0 = 0`
- `¬(A ∧ B) = ¬0 = 1`
- `Q = 1 ∨ 0 = 1`

> **Exam tip:** when a question says "complete the truth table", show every intermediate column. Mark schemes award method marks for the intermediate values even if the final column is wrong.

---

## 19.02 Sequential Logic Circuits

Combinational circuits have no memory: the output is fixed by the inputs. **Sequential circuits** feed part of the output back to the input, so the circuit remembers its previous state. This makes them the basis of registers, memory and counters.

### 19.02.1 The SR flip-flop (SR latch)

The SR flip-flop is the simplest sequential circuit. It can be built from two cross-coupled NOR gates or two cross-coupled NAND gates.

**NOR version:**

| S | R | Q (next) | Q' (next) | Meaning |
|---|---|---|---|---|
| 0 | 0 | Q (unchanged) | Q' (unchanged) | **Hold** — remembers its state |
| 1 | 0 | 1 | 0 | **Set** — Q becomes 1 |
| 0 | 1 | 0 | 1 | **Reset** — Q becomes 0 |
| 1 | 1 | 0 | 0 | **Invalid** — forbidden |

- `S` means **Set** and `R` means **Reset**.
- When `S=1, R=0`, the circuit is forced into the **set state**: `Q=1, Q'=0`.
- When `S=0, R=1`, it is forced into the **reset (unset) state**: `Q=0, Q'=1`.
- When `S=0, R=0`, the previous state is held. This is the memory action.
- When `S=1, R=1`, both outputs are forced to 0, which contradicts the requirement that `Q` and `Q'` are opposites. When the inputs then return to `0,0`, the final state is unpredictable. This input combination is therefore **not allowed**.

**NAND version:** the inputs are active-low. Setting is achieved with `S=0, R=1`; resetting with `S=1, R=0`; `S=R=1` holds; `S=R=0` is invalid.

### 19.02.2 Why the SR flip-flop stores one bit

The cross-coupled feedback creates two stable states:

- `Q=1, Q'=0` represents binary **1**.
- `Q=0, Q'=1` represents binary **0**.

Because the circuit can hold either state indefinitely with `S=R=0`, it stores **one bit**. A bank of `n` flip-flops stores an `n`-bit word, which is the basis of a **register** or a static RAM cell.

> **Exam tip:** the mark-scheme phrase is "the output is fed back to the input, so the circuit retains its previous state". Saying only "it has two outputs" does not earn the memory mark.

### 19.02.3 Clocked flip-flops

In real systems, state changes are synchronised by a **clock** signal. A clocked SR flip-flop only changes state when the clock pulse arrives, which prevents unpredictable racing between gates. Clocking is essential in registers, counters and processors.

---

## 19.03 Boolean Algebra Basics

Boolean algebra is the algebra of two values, 0 and 1. It lets us simplify logic circuits, which reduces the number of gates, cost, power consumption and propagation delay.

### 19.03.1 Notation

| Operation | Boolean notation | Alternative notations |
|---|---|---|
| NOT | `¬A` | `A'`, `Ā` |
| AND | `A ∧ B` | `A.B`, `AB` |
| OR | `A ∨ B` | `A+B` |
| XOR | `A ⊕ B` | — |

**Operator precedence:** NOT first, then AND, then OR. Brackets override precedence. In `A ∨ B ∧ C`, the AND is evaluated first, giving `A ∨ (B ∧ C)`.

### 19.03.2 Laws and identities

| Law | AND form | OR form |
|---|---|---|
| Identity | `A ∧ 1 = A` | `A ∨ 0 = A` |
| Null (dominance) | `A ∧ 0 = 0` | `A ∨ 1 = 1` |
| Idempotent | `A ∧ A = A` | `A ∨ A = A` |
| Inverse | `A ∧ ¬A = 0` | `A ∨ ¬A = 1` |
| Double negation | `¬(¬A) = A` | — |
| Commutative | `A ∧ B = B ∧ A` | `A ∨ B = B ∨ A` |
| Associative | `(A ∧ B) ∧ C = A ∧ (B ∧ C)` | `(A ∨ B) ∨ C = A ∨ (B ∨ C)` |
| Distributive | `A ∧ (B ∨ C) = (A ∧ B) ∨ (A ∧ C)` | `A ∨ (B ∧ C) = (A ∨ B) ∧ (A ∨ C)` |
| Absorption | `A ∧ (A ∨ B) = A` | `A ∨ (A ∧ B) = A` |
| De Morgan | `¬(A ∧ B) = ¬A ∨ ¬B` | `¬(A ∨ B) = ¬A ∧ ¬B` |

**De Morgan's laws in words:** break the bar and change the operator. Negating an AND gives an OR of the negations; negating an OR gives an AND of the negations. The bar applies to the **whole** expression, not just the first variable.

### 19.03.3 Simplifying expressions — worked examples

**Worked example 19.04 — simplify `Q = A ∧ B ∨ A ∧ ¬B`**

Factor out `A` using the distributive law:

`Q = A ∧ (B ∨ ¬B)`

Using the inverse law, `B ∨ ¬B = 1`:

`Q = A ∧ 1 = A`

So the whole circuit collapses to a single wire carrying `A`.

**Worked example 19.05 — simplify `Q = (A ∨ B) ∧ (A ∨ ¬B)`**

Use the distributive law in reverse:

`Q = A ∨ (B ∧ ¬B)`

`B ∧ ¬B = 0`, so:

`Q = A ∨ 0 = A`

**Worked example 19.06 — apply De Morgan to `Q = ¬(A ∧ B)`**

`Q = ¬A ∨ ¬B`

The circuit changes from an AND followed by a NOT to two NOTs feeding an OR. This is the basis of converting between NAND-only and AND/NOT designs.

**Worked example 19.07 — simplify `Q = ¬(¬A ∧ ¬B)`**

Apply De Morgan to the outer negation:

`Q = ¬(¬A) ∨ ¬(¬B) = A ∨ B`

This is a common exam trap: candidates stop at `¬A ∨ ¬B` or forget the double negation.

### 19.03.4 Proving identities with truth tables

To prove that two expressions are equivalent, build a truth table containing a column for each expression. If the columns are identical for every input combination, the expressions are equivalent.

**Worked example 19.08 — prove `¬(A ∧ B) = ¬A ∨ ¬B`**

| A | B | A ∧ B | ¬(A ∧ B) | ¬A | ¬B | ¬A ∨ ¬B |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 |

The two bold columns match for all four rows, so De Morgan's law is proved.

---

## 19.04 Boolean Algebra Applications

### 19.04.1 From a truth table to an expression (sum of products)

1. Identify every row where the output is **1**.
2. For each such row, write a product term:
   - input **1** → variable as it is;
   - input **0** → negated variable.
3. OR all the product terms together.

This is called **sum of products (SOP)** or **disjunctive normal form**.

**Worked example 19.09 — truth table to SOP**

| A | B | Q |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

Rows with `Q=1` are `01`, `10`, `11`:

`Q = (¬A ∧ B) ∨ (A ∧ ¬B) ∨ (A ∧ B)`

Simplify: the last two terms combine to `A`, and the remaining term combines to give `Q = A ∨ B`.

### 19.04.2 From a Boolean expression to a truth table

Evaluate the expression for every input combination. Use intermediate columns for sub-expressions to avoid mistakes.

**Worked example 19.10 — truth table for `Q = (A ∨ B) ∧ ¬C`**

| A | B | C | A ∨ B | ¬C | Q |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 0 |
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 | 1 |
| 0 | 1 | 1 | 1 | 0 | 0 |
| 1 | 0 | 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 1 | 0 | 0 |
| 1 | 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 |

### 19.04.3 The half adder

A **half adder** adds two single bits `A` and `B`. It produces a **sum** `S` and a **carry** `C`.

| A | B | Sum S | Carry C |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

From the truth table:

- `S = A ⊕ B` (XOR — sum is 1 when the inputs differ)
- `C = A ∧ B` (AND — carry is 1 only when both inputs are 1)

**Circuit:** one XOR gate for the sum and one AND gate for the carry, both fed by `A` and `B`.

> **Exam tip:** the half adder is called "half" because it cannot accept a carry from a previous column. A full adder is needed for multi-bit addition.

### 19.04.4 The full adder

A **full adder** adds three bits: `A`, `B` and a carry-in `Cin`. It produces a sum `S` and a carry-out `Cout`.

Truth table:

| A | B | Cin | S | Cout |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

Boolean expressions:

`S = A ⊕ B ⊕ Cin`

`Cout = (A ∧ B) ∨ (Cin ∧ (A ⊕ B))`

The `Cout` expression says: a carry is produced if both `A` and `B` are 1, **or** if `Cin` is 1 and exactly one of `A`, `B` is 1 (so the sum plus carry-in overflows).

**Circuit construction:** two half adders plus an OR gate.

1. Half adder 1 adds `A` and `B` → `S1 = A ⊕ B`, `C1 = A ∧ B`.
2. Half adder 2 adds `S1` and `Cin` → `S = S1 ⊕ Cin`, `C2 = S1 ∧ Cin`.
3. OR gate combines `C1` and `C2` → `Cout = C1 ∨ C2`.

A **ripple-carry adder** chains full adders so that the carry-out of one column becomes the carry-in of the next. The carry "ripples" from the least significant bit to the most significant bit, which makes the circuit slower for wide words.

---

## 19.05 Karnaugh Maps (K-maps)

A Karnaugh map is a graphical method for simplifying Boolean expressions. It arranges the truth-table rows so that adjacent cells differ by exactly **one variable**. Grouping adjacent 1s then removes that variable.

### 19.05.1 Two-variable K-map

For `Q = A ∧ B`:

| A \ B | 0 | 1 |
|---|---|---|
| **0** | 0 | 0 |
| **1** | 0 | 1 |

The single 1 is a group of size 1, giving `A ∧ B`.

### 19.05.2 Three-variable K-map

Rows and columns are labelled in **Gray code** order (`00, 01, 11, 10`) so that adjacent cells differ by one bit.

Example: `Q = Σ(1, 3, 5, 7)` where the variables are `A, B, C` and `m1 = ¬A¬BC`, etc.

| A \ BC | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **0** | 0 | 1 | 1 | 0 |
| **1** | 0 | 1 | 1 | 0 |

The four 1s form a group of 4 (two adjacent columns), which eliminates `A` and `C`, leaving `Q = C`.

### 19.05.3 Four-variable K-map

| AB \ CD | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **00** |  |  |  |  |
| **01** |  |  |  |  |
| **11** |  |  |  |  |
| **10** |  |  |  |  |

The map wraps around at the edges: the left and right columns are adjacent, and the top and bottom rows are adjacent. Groups may also wrap around corners.

### 19.05.4 Grouping rules

1. Groups must contain **1, 2, 4, 8, ...** cells — always a power of 2.
2. Groups must be **rectangular** (including squares and full rows/columns).
3. Groups may **overlap**; a 1 may be used in more than one group.
4. Make groups as **large as possible** — a larger group removes more variables.
5. Every 1 must be covered by at least one group.
6. Groups may **wrap around** the edges of the map.
7. **Don't-care** conditions (outputs that may be 0 or 1) can be included in a group if doing so makes the group larger, but they do not have to be covered.

### 19.05.5 From K-map group to term

- A variable that stays **constant** within the group appears in the term.
- A variable that **changes** within the group is eliminated.
- Constant 1 → variable as it is; constant 0 → negated variable.
- OR the terms for all groups.

**Worked example 19.11 — three-variable K-map**

`Q = Σ(0, 1, 2, 3)` with variables `A, B, C`.

| A \ BC | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **0** | 1 | 1 | 1 | 1 |
| **1** | 0 | 0 | 0 | 0 |

The entire top row is a group of 4. `A` is constant at 0; `B` and `C` change. Therefore `Q = ¬A`.

> **Exam tip:** always check whether a group of 4 or 8 is possible before settling for pairs. A common mark-scheme error is a correct but unnecessarily complex expression; simplification questions usually require the **minimal** form.

---

## 📝 Exam-style Questions with Full Solutions

### Question 1 — Simplify using Boolean algebra (4 marks)

Simplify `Q = (A ∧ B) ∨ (A ∧ ¬B) ∨ (¬A ∧ B)`.

**Solution:**

`Q = A ∧ (B ∨ ¬B) ∨ (¬A ∧ B)` — factor out `A`.

`Q = A ∧ 1 ∨ (¬A ∧ B)` — inverse law.

`Q = A ∨ (¬A ∧ B)` — identity law.

`Q = (A ∨ ¬A) ∧ (A ∨ B)` — distributive law.

`Q = 1 ∧ (A ∨ B)` — inverse law.

`Q = A ∨ B` — identity law.

**Answer:** `Q = A ∨ B`. ✓

**What the examiner wants:** each named law earns a method mark; the final simplified expression earns the answer mark. Do not jump straight to the answer without showing the intermediate lines.

### Question 2 — De Morgan and NAND-only implementation (5 marks)

(a) Use De Morgan's laws to express `Q = ¬(A ∧ B) ∨ C` without an AND gate.

(b) Show how the expression can be built using only NAND gates and a NOT gate.

**Solution:**

(a) `¬(A ∧ B) = ¬A ∨ ¬B`, so:

`Q = ¬A ∨ ¬B ∨ C`

(b) `¬A ∨ ¬B ∨ C = ¬(A ∧ B) ∨ C`. Build `A ∧ B` with a NAND gate followed by a NOT (to undo the inversion), then OR that result with `C`. If only NAND gates are allowed, replace the final OR with De Morgan:

`X ∨ C = ¬(¬X ∧ ¬C)`

so the final stage is a NAND gate whose inputs are `¬X` and `¬C`.

**What the examiner wants:** correct application of De Morgan (break the bar, change the operator) and a circuit that is logically equivalent, even if the gate count is not minimal.

### Question 3 — Truth table and expression (6 marks)

A circuit has three inputs `A, B, C` and output `Q = 1` when **exactly two** inputs are 1.

(a) Complete the truth table.
(b) Write a sum-of-products expression.
(c) Simplify the expression.

**Solution:**

(a)

| A | B | C | Q |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

(b) Rows `011`, `101`, `110`:

`Q = (¬A ∧ B ∧ C) ∨ (A ∧ ¬B ∧ C) ∨ (A ∧ B ∧ ¬C)`

(c) This expression is already minimal in SOP form; no pair of terms differs by only one variable, so no further grouping is possible. (A K-map would show three isolated 1s or three pairs, depending on the grouping, but the minimal SOP remains three 3-variable terms.)

**What the examiner wants:** all eight rows correct, the three correct minterms, and recognition that no simplification is possible.

### Question 4 — Half adder (5 marks)

(a) Draw the truth table for a half adder.
(b) Write Boolean expressions for the sum and carry.
(c) Explain why a half adder cannot be used alone to add two 4-bit numbers.

**Solution:**

(a) See the half-adder table in Section 19.04.3.

(b) `S = A ⊕ B`; `C = A ∧ B`.

(c) A half adder has no **carry-in** input. When adding multi-bit numbers, each column after the least significant one may receive a carry from the previous column. A full adder is required because it accepts `A`, `B` and `Cin`.

**What the examiner wants:** the XOR/AND pair and the phrase "no carry-in" — not just "it only adds two bits".

### Question 5 — K-map simplification (4 marks)

Use a Karnaugh map to simplify `Q = Σ(1, 3, 5, 7)` for variables `A, B, C`.

**Solution:**

| A \ BC | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **0** | 0 | 1 | 1 | 0 |
| **1** | 0 | 1 | 1 | 0 |

The four 1s form a group of 4 covering both rows and columns `01` and `11`. `A` changes (eliminated), `B` is constant at 1, `C` changes (eliminated). Therefore:

`Q = B`

**What the examiner wants:** correct Gray-code layout, a group of four (not two pairs), and the single-variable answer.

### Question 6 — SR flip-flop (6 marks)

(a) State the difference between a combinational and a sequential circuit.
(b) Complete the truth table for a NOR-based SR flip-flop.
(c) Explain why `S=R=1` is not used.

**Solution:**

(a) A combinational circuit's output depends only on the current inputs. A sequential circuit's output depends on the current inputs **and** the previous output, because it has feedback/memory.

(b) See the table in Section 19.02.1.

(c) With `S=R=1`, both NOR gates are forced to output 0, so `Q=Q'=0`. This violates the definition that `Q` and `Q'` are complements. When the inputs return to `0,0`, the circuit may settle in either state, so the next state is unpredictable. The combination is therefore forbidden.

**What the examiner wants:** "feedback/memory" for (a), correct hold/set/reset rows for (b), and "both outputs 0 / indeterminate next state" for (c).

---

# 📋 Formula / Fact Sheet (Chapter 19)

**Gate expressions:**

`NOT: ¬A` · `AND: A ∧ B` · `OR: A ∨ B` · `NAND: ¬(A ∧ B)` · `NOR: ¬(A ∨ B)` · `XOR: A ⊕ B`

**Key laws:**

- Identity: `A ∧ 1 = A`, `A ∨ 0 = A`
- Null: `A ∧ 0 = 0`, `A ∨ 1 = 1`
- Idempotent: `A ∧ A = A`, `A ∨ A = A`
- Inverse: `A ∧ ¬A = 0`, `A ∨ ¬A = 1`
- Double negation: `¬¬A = A`
- Distributive: `A ∧ (B ∨ C) = (A ∧ B) ∨ (A ∧ C)`
- Absorption: `A ∧ (A ∨ B) = A`, `A ∨ (A ∧ B) = A`
- De Morgan: `¬(A ∧ B) = ¬A ∨ ¬B`, `¬(A ∨ B) = ¬A ∧ ¬B`

**Adders:**

- Half adder: `S = A ⊕ B`, `C = A ∧ B`
- Full adder: `S = A ⊕ B ⊕ Cin`, `Cout = (A ∧ B) ∨ (Cin ∧ (A ⊕ B))`

**Sequential logic:**

- SR latch (NOR): `00` hold, `10` set, `01` reset, `11` invalid.
- SR latch (NAND): `11` hold, `01` set, `10` reset, `00` invalid.
- One flip-flop stores **1 bit**.

**K-map rules:** groups of `1, 2, 4, 8`; rectangular; may overlap and wrap; largest possible groups; don't-cares may be used.

**Truth-table size:** `2^n` rows for `n` inputs.

# ⚡ Quick Reference Card

1. **Gate outputs:** AND = all 1s; OR = any 1; XOR = odd number of 1s; NAND/NOR = inverted AND/OR.
2. **Build circuits inside-out:** brackets → NOT → AND → OR.
3. **Truth table → expression:** take rows where `Q=1`, write minterms, OR them.
4. **Simplify:** factor, use inverse (`A ∨ ¬A = 1`), then identity; use De Morgan to remove bars.
5. **De Morgan:** break the bar, change the operator.
6. **Half adder:** XOR for sum, AND for carry; no carry-in.
7. **Full adder:** two half adders + OR; accepts carry-in.
8. **SR latch:** feedback gives memory; `S=R=1` (NOR) is invalid.
9. **K-map:** Gray code edges; group 1s in powers of 2; bigger group = fewer variables.
10. **Check:** a correct simplification must give the same truth table as the original.
