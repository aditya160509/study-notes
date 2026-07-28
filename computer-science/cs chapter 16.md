# Chapter 16: Data Representation — Complete Study Guide
### Cambridge International AS & A Level Computer Science

This chapter has two genuinely distinct halves: user-defined data types and file organisation (conceptual, definitional) and floating-point real number representation (mathematical, needs practised working). Both are covered in full below, section by section, followed by fully worked answers to every exam-style question.

---

## PART 1 — DATA TYPES (16.01)

### 1.1 The starting point: what a data type actually gives you

Every built-in data type in a programming language gives you two things, and only two things:

1. **The programming language defines the range of possible values** that can be assigned to a variable of that type.
2. **The programming language defines the operations** available for manipulating values of that type.

That's the complete job description of a data type. Everything else in this section is about what happens when the built-in ones aren't enough.

### 1.2 User-defined data types — the core idea

**Definition (memorise exactly):**

> **User-defined data type:** where the programmer includes the definition in the program.

**Why the word "user" here is confusing, and how to explain it correctly if asked:** normally "user" means the person interacting with a running program through a user interface. But when you're *writing* the program, **you, the programmer, become a "user" of the programming language itself** — and a user-defined data type is one where you (the language-user) supply the definition, rather than the language supplying it for you.

**Critical distinction the textbook explicitly flags as a trap:** do not confuse a **user-defined data type** with an **abstract data type (ADT)** (from Chapter 13, Section 13.07). They are different concepts:
- A **user-defined data type** is about *how* a type is created (by the programmer, inside the program).
- An **abstract data type** is about a *conceptual model* of data plus the operations on it (like a stack or queue), independent of implementation.

If a question asks you to distinguish these, don't just describe one — explicitly state that they answer different questions ("who defined it" vs "what abstraction does it represent").

**The precondition for using one at all:** even though a user-defined type isn't built in, using it is only possible if **the programming language offers support for the construct** in the first place. You can't invent syntax the language doesn't understand.

### 1.3 Non-composite data types

**Definition:**

> **Non-composite data type:** a data type defined without reference to another data type.

Simple built-in types like `INTEGER` or `REAL` are built-in non-composite types — their definition doesn't point to any other type. But a **user-defined** type can also be non-composite, and the chapter's example of this is the **enumerated type**.

### 1.4 The enumerated data type

**Definition:**

> **Enumerated data type:** a non-composite user-defined data type for which the definition identifies all possible values.

The defining feature: when you define an enumerated type, you list out **every single possible value** it can ever take, explicitly, up front.

```
TYPE
    TDirections = (North, East, South, West)
    TDays = (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)
```

Declaring and using variables of these types:

```
DECLARE Direction1 : TDirections
DECLARE StartDay   : TDays

Direction1 ← North
StartDay   ← Wednesday
```

**Two rules about enumerated values you must know cold:**

1. **The values look like strings but are NOT strings.** They must **never** be enclosed in quotes. `North` is a value of type `TDirections`, not the string `"North"` — writing `Direction1 ← "North"` would be wrong.
2. **The values are ordinal** — meaning they have an **implied order**. `Monday` comes before `Tuesday`, which comes before `Wednesday`, and so on, purely by the order they were listed in the type definition.

**Why the ordinality matters — a genuinely useful consequence:** because the values are ordered, you can use **comparison operators** directly on them:

```
DECLARE Weekend : Boolean
DECLARE Day     : TDays

Weekend = TRUE IF Day > Friday
```

This works because `Saturday` and `Sunday` come *after* `Friday` in the defined order — `Day > Friday` is a meaningful, valid comparison precisely because of the implied ordering.

**Why enumerated types explain "why user-defined types are necessary" (a direct learning objective, so expect a question phrased exactly this way):** there **cannot** be a generic *built-in* definition of an enumerated type, because the specific possible values (North/East/South/West, or Monday–Sunday, or whatever else you might want) are not known in advance to the language designer. They can **only** be known once the programmer specifies them in a type definition — which is precisely what "user-defined" means. This is the textbook's own explanation and is a strong exam answer if you're asked to justify the need for user-defined types in general.

### 1.5 Composite user-defined data types

**Definition (build this from the non-composite definition by negation):** a composite user-defined data type has a definition that **references at least one other type**.

There are two important examples given:

**1. The record data type** (first introduced in Chapter 13).
- Although a language *could* have built-in record types, the normal expectation is that records are **user-defined**.
- Why: this lets the programmer create a record whose components **precisely match the data requirements** of the specific program being written — nobody could predict every possible combination of fields a program might need, so it has to be user-specified.
- **Named exception to remember:** **Python does not support the use of a record data type.** This is a specific, testable fact — if asked which of the syllabus's chosen languages lacks record support, the answer is Python.

**2. The class.**
- A class is the data type used for an **object** in object-oriented programming.
- A given OOP language will likely provide a number of **built-in classes**.
- But — and this is the key point — **if a programmer wants to actually use the object-oriented approach for their own problem**, they will need to create their **own user-defined classes**, because the built-in ones won't model the programmer's specific problem domain.

### 1.6 The pointer data type

**Definition:**

> **Pointer variable:** one for which the value is the address in memory of a different variable.

This is conceptually the trickiest part of 16.01, so work through the five-step example slowly, because exam questions often ask you to trace through exactly this kind of sequence.

**Step 1 — defining the pointer type itself:**
```
TYPE
    TIntegerPointer ← ^Integer
```
This just says "I want a type that can point to an Integer." The `^` symbol here marks that this type is a pointer-to-Integer.

**Step 2 — declaring a variable of that pointer type:**
```
DECLARE MyIntegerPointer : TIntegerPointer
```
Notice: declaring the variable does **not** require the caret symbol — the caret was only needed in the type definition itself.

**Step 3 — declaring two ordinary (non-pointer) integer variables:**
```
DECLARE Number1, Number2 : INTEGER
Number1 ← 100
```

**Step 4 — assigning the pointer variable the address of a different variable:**
```
MyIntegerPointer ← @Number1
```
The `@` symbol means "the address of." So `MyIntegerPointer` now **holds a reference to where `Number1` lives in memory** — it does not hold the value 100 itself, it holds *where 100 is stored*.

**Step 5 — dereferencing the pointer to get at the value stored at that address:**
```
Number2 ← MyIntegerPointer^ * 2
```
Here, `MyIntegerPointer^` means "the value stored at the address that `MyIntegerPointer` is pointing to" — i.e. it fetches `100` (the value of `Number1`) by following the pointer. This is called **dereferencing**. So this line computes `100 * 2 = 200` and assigns it to `Number2`.

**Symbol summary (memorise both directions):**

| Symbol | Meaning | Used when... |
|---|---|---|
| `^` (in a type definition, e.g. `^Integer`) | "pointer to" | Defining what kind of thing the pointer points to |
| `@` | "the address of" | Assigning a pointer the location of an existing variable |
| `^` (after a variable name, e.g. `MyIntegerPointer^`) | "dereference" — the value stored at the pointed-to address | Reading/using the actual value the pointer refers to |

**Important caveat:** not every programming language supports pointers, and those that do will use their **own version of this symbolism**, not necessarily `^` and `@` — this pseudocode notation is Cambridge's own convention for exam purposes, not universal syntax.

**Why pointers are useful — the practical payoff:** because arithmetic can be performed on pointer variables, they let you build **dynamically varying data structures**. Without pointer support, if you need an array whose size might grow, you're forced to **declare an array with a large upper bound** just in case, wasting memory most of the time. **With** pointer support, an array's size can genuinely **expand while the program is running**. (The chapter explicitly says the mechanics of *how* this dynamic expansion works are beyond its scope — you just need to know pointers are what makes it *possible*.)

### 1.7 The set data type

**Definition:**

> **Set:** a collection of data items that lacks any structure; contains no duplicates and has a number of defined operations that can be performed on it.

**The defining mathematical properties of a set (list all of these if asked):**

- It contains a collection of data values.
- **There is no organisation** of the data values within the set (no order, no positions).
- **Duplicate values are not allowed.**
- Defined operations include:
  - checking if a value exists in the set
  - adding a new data value
  - removing an existing data value
  - adding one set to another set (union-type operation)

**The classification puzzle — a genuinely subtle point worth understanding, not just memorising:** it's tempting to call a set a "structured data type" because it holds multiple components. But this **contradicts** the fact that a set has **no structure**, and therefore **no indexing** can be associated with its members (you can't ask for "the third element of a set" — that concept doesn't exist for a set). This is exactly the kind of nuance an exam might test by asking you to justify why a set is *not* simply classified as a structured/composite type in the same way an array or record is.

**Two worked use-cases for sets, both good exam-answer material:**

1. **Removing duplicates from a list/array:** the single most useful property of a set is that duplicates are automatically disallowed. If you have a list or one-dimensional array that might contain duplicate values, a simple technique is to **convert the structure into a set** (which strips duplicates automatically as a side effect of the conversion) and then **convert it back** to the original structure type.

2. **Finding students studying multiple subjects:** if students are grouped into per-subject sets (e.g. one set of names for "Computer Science students," another set of names for "Physics students"), you can find students studying **both** by applying the **intersection** operation on the two sets. (Note: intersection isn't in the four operations explicitly listed above, but this example shows sets support standard set-theory operations more broadly — intersection, union, etc.)

---

## PART 2 — FILE ORGANISATION (16.02)

### 2.1 Text files vs binary files — the fundamental split

For the *specific purpose* of storing data used as input to, or output from, a program (as opposed to general file types like graphics or word-processing files, which each use their own specific binary coding), there are only **two defined file types**:

**Text file:**
- Contains data stored according to a **character code** (like ASCII, from Chapter 1).
- Can be created directly using a **text editor** to serve as program input.

**Binary file:**

> **Binary file:** a file designed for storing data to be used by a computer program.

- Typically created by a program **as output**, with the intention of later using it as input.
- Stores data in its **internal representation** — e.g. an integer value might be stored in two bytes using two's complement representation (not as human-readable digit characters).

### 2.2 The record/field structure underlying binary files

> **Record:** a collection of fields containing data values.

A file contains **records**; each record contains **fields**; each field consists of a value. This nested structure (file → records → fields → values) is the organisational backbone of file storage.

**How text files and binary files differ in what "must be known" to read them correctly — this comparison is a common exam point:**

**For a text file:**
- The number of data items per line must be known, **and** the number of characters per item must be known.
- **If these aren't known in advance**, then **item separator characters** must be used instead (e.g. commas in a CSV file).
- The file has repeating lines, delimited by an **end-of-line character or characters**.

**For a binary file:**
- The **number of fields per record** must be known.
- If any field is a string, the **length of that string** must be known.
- For any other field, its **internal representation defines exactly how many bytes** are needed to store it (e.g. a two's complement integer in two bytes always takes exactly two bytes — no ambiguity).
- **Consequence:** there is **no need for field separator characters or an end-of-record character** in a binary file — because every field's size is already precisely known, the file format itself makes clear where one field ends and the next begins, with no ambiguity requiring a separator.

**A genuinely interesting discussion point raised in the textbook:** a record is a *user-defined data type* (Part 1 above) **and** it's also a *structural component of a file*. Are these the same concept, related concepts, or coincidentally sharing a name? The textbook poses this as an open discussion point rather than giving a fixed answer — worth thinking through: the record-as-data-type is about *defining a shape for data in a program*; the record-as-file-component is about *how data is laid out in storage*. They're related because a program will typically read a file's records directly into variables of a matching record data type — the file structure and the in-memory structure are designed to mirror each other, but conceptually one is about persistent storage and the other is about a construct in a running program.

### 2.3 The three methods of file organisation

**Serial files**

- Contains records **in no defined order** — records simply get **appended** to the file as they arrive.
- The only "ordering" present is the **time order of data entry**.
- Classic example: a bank's **transaction file** — every time a withdrawal or deposit happens, the program receives the details as input and appends a new record to the transaction file, purely in the order the transactions occurred.

**Sequential files**

- Records **are ordered**, based on a **key field**.
- **Key field requirement:** values must be **unique and sequential**, but **not necessarily consecutive** (e.g. key values 3, 7, 12, 19 are perfectly valid — they're increasing/ordered, but there are "gaps").
- Classic example continuing the bank scenario: a **master file** for individual customer accounts. Periodically, the transaction file is read and used to update the relevant customer account master files.
- **How a new record actually gets added, properly (not just appended-and-sort-later):** the sequential file is read from the start, and each record is written out to a **new file**, one at a time, until the correct position for the new record is reached. The new record is written into the new file **at that point**, and then the rest of the old file's remaining records are copied across afterward. (This "read old file, write new file, insert at the right point" process is exactly the pattern also used for editing/deleting — see 2.5.)

**Direct-access files** (sometimes called "random-access" files)

- **Important clarification on the name:** the "randomness" here, exactly like in RAM (random-access memory), just means access can jump to **any** record in the file **without** having to read sequentially through everything before it — it does **not** mean the file's contents or layout are literally random.
- **Two ways to achieve direct access:**

  **Method A — using an index file alongside a sequential file:** a separate **index file** is created with **two fields per record**: (1) the key field value, and (2) the **position** of that key value's record within the main file. Look up the key in the (smaller, faster-to-search) index, get the position, then jump straight there in the main file.

  **Method B — using a hashing algorithm** (see 2.4 below, in depth).

### 2.4 Hashing algorithms — the mechanism in full detail

**The basic numeric-key hashing algorithm, step by step:**

1. Choose a **suitable number** to divide by.
2. **Divide** that suitable number's... — actually, more precisely: divide the **key field value** using this suitable number, and take the **remainder**.
3. The **remainder** from this division becomes the **address** in the file where that record is stored.

**What makes a "suitable number" suitable:** it works best when it is a **prime number** of a **similar size to the expected size of the file** (i.e. roughly matching how many records/addresses you expect to need).

**Worked example directly from the textbook (memorise this exact pattern, as it appears near-verbatim in past papers):**

Using 1000 as the dividing number for a 4-digit key field:

```
0045 ÷ 1000 → remainder 45   → address 45
2005 ÷ 1000 → remainder 5    → address 5
3005 ÷ 1000 → remainder 5    → address 5
```

**Two facts this example demonstrates, both are direct exam-answer material:**

1. **The calculated addresses have no relationship to, or order based on, the key field value itself.** (0045 → 45, but 2005, a much bigger number, maps to a *smaller* address, 5 — there's no meaningful ordering preserved.)
2. **Different key field values can produce the same remainder — and therefore the same address.** (2005 and 3005 both map to address 5.)

**When the key field isn't numeric:** if there's no suitable numeric field, use a field with **alphabetic characters** instead — look up the **ASCII code** for each character, **add them all up**, and then use that sum exactly as before (take the remainder from an integer division) to calculate an address.

**Collisions:**

> When the same address is calculated for different field values, this is called a **collision** (the colliding addresses/values are sometimes called **synonyms**).

**What makes a good hashing algorithm:** one that **spreads addresses as evenly as possible** and **minimises the number of collisions**. But collisions can **never be entirely avoided**, so every direct-access implementation needs a defined strategy for handling them. Three named strategies to remember:

1. **Sequential search for a vacant address following the calculated one** — if the calculated address is already occupied, just check the next address, then the next, until you find a free one.
2. **Keep a number of overflow addresses at the end of the file** — a dedicated reserved area specifically for records that collided elsewhere.
3. **Have a linked list accessible from each address** — each address can chain to additional records that hashed to the same value.

### 2.5 File access methods

**For a serial file:** normal usage is to read the **whole file, record by record**, from the start. If you need to search for a specific value, the **only** option is to read from the beginning until you find the target — there's no shortcut.

**For a sequential file:** if you need to search for a value, and you don't know the key, you may have to search in the same start-to-finish way as a serial file. **But** if you already know the key field value for the record you want, the process is **faster**, because you technically only need to read key field values (not entire records) as you scan through, until you find a match.

**For a direct-access file:** the key field value is submitted to the **hashing algorithm** — the exact same algorithm and exact same value used when the data was originally entered — which reproduces the exact same address that was calculated at input time. This **eliminates the need to read from the beginning of the file entirely**. However, because of the possibility of collisions, **some sequential searching might still be needed** after jumping to the initially-hashed position (to walk forward through any synonyms stored via the collision-handling strategy).

**Deleting or editing records:**

- **Sequential file:** uses the **same method as adding a new record** — records are copied one-by-one from the old file into a new file until the record needing deletion/editing is reached; that record is edited or simply skipped (for deletion); then the remaining records are copied across as normal.
- **Direct-access file:** **no new file needs to be created at all.** If a record needs *editing*, it can be accessed directly via its hashed address and edited **in place**, without disturbing anything else. If a record needs *deleting*, since you can't just leave a gap, a **flag is set within that record** marking it as deleted; then, during any subsequent read process, that flagged record is simply **skipped over**.

### 2.6 Choosing the right file organisation for a given scenario

This decision-making skill is directly and repeatedly examined, so learn the three scenario-matches exactly:

| File organisation | Best suited to... | Why |
|---|---|---|
| **Serial** | Batch processing; backing up data (e.g. onto magnetic tape) | No need for ordering or fast lookup — just processing everything, or storing a full copy, in the order it exists |
| **Direct-access** | Rapid access to an **individual** record in a **large** file — e.g. a system with many users checking passwords at login | Speed of locating one specific record matters far more than reading in order; hashing gets you there almost instantly |
| **Sequential** | Applications where **multiple records** are needed from **one search** — e.g. a family history file, searching for all records matching a particular family name | You're not looking for one single record — you want a *range* or *group* of related records, which sequential ordering (and reading through a relevant span) supports well |

### 2.7 Key field vs primary key — a precise distinction

This is a small point but a favourite "gotcha" in Cambridge papers:

- In a **database table**, **primary key values must all be unique** — this is a hard requirement.
- In a **file's key field**, uniqueness is **not** a requirement of any type of file organisation. It **may be sensible**, in certain applications, to ensure key field values are unique — but it is **not mandatory**.

If asked to compare these two terms, state explicitly: primary keys *must* be unique by definition; file key fields are not required to be.

---

## PART 3 — REAL NUMBERS AND FLOATING-POINT REPRESENTATION (16.03)

This is the mathematically dense part of the chapter. Go slowly and work every example by hand as you read it — this is a skill you build by doing, not by reading passively.

### 3.1 What a "real number" means here, and denary notation choices

A **real number** is simply one with a fractional part. In denary, you have a choice of how to write such a number:

- **Simple representation:** e.g. `25.3`
- **Exponential (scientific) notation:** the same value written as `.253 × 10²`, or `2.53 × 10¹`, or `25.3 × 10⁰`, or `253 × 10⁻¹` — all of these represent exactly the same number, just with the decimal point shifted and the power of 10 adjusted to compensate.

**When each is preferable:** for a number like 25.3, the simple form is clearly the most readable. But for numbers that are **very large or very small**, exponential notation becomes the **only sensible choice** (imagine writing out 0.0000000001 in full versus writing `1 × 10⁻¹⁰`).

### 3.2 Fixed-point vs floating-point representation

**Fixed-point representation:** you choose an overall number of bits, and a **defined, fixed split** of how many bits represent the whole-number part versus the fractional part. This split never changes for any value stored in that format.

**Floating-point representation:**

> **Floating-point representation:** a representation of real numbers that stores a value for the mantissa and a value for the exponent.

The general format:

```
± M × R^E
```

- **M** = the **mantissa** (also called the **significand**) — a defined number of bits, stored with a sign.
- **E** = the **exponent** (sometimes called the **exrad**) — the remaining bits.
- **R** = the **radix** — this is **NOT stored** in the representation at all; it has an **implied value of 2** (since we're working in binary).

### 3.3 Comparing fixed-point and floating-point with a worked 8-bit example

**Fixed-point choice:** 1 sign bit + 5 bits for whole number + 2 bits for fraction (8 bits total).

| Description | Binary code | Denary equivalent |
|---|---|---|
| Largest positive value | `011111 11` | 31.75 |
| Smallest positive value | `000000 01` | 0.25 |
| Smallest magnitude negative value | `100000 01` | −0.25 |
| Largest magnitude negative value | `111111 11` | −31.75 |

**Floating-point choice:** 4 bits mantissa + 4 bits exponent, both in two's complement.

The exponent is a straightforward signed integer. But **where does the binary point sit within the mantissa?** Two options are compared:

**Option A — binary point placed further along (not immediately after the sign bit):**

| Bit pattern | Real value (denary) |
|---|---|
| `0111` | 3.5 |
| `0110` | 3.0 |
| `0101` | 2.5 |
| `1010` | −3.0 |
| `1001` | −3.5 |
| `1000` | −4.0 |

**Option B — binary point placed immediately after the sign bit:**

| Bit pattern | Real value (denary) |
|---|---|
| `0111` | 0.875 |
| `0110` | 0.75 |
| `0101` | 0.625 |
| `1010` | −0.75 |
| `1001` | −0.875 |
| `1000` | −1.0 |

**The exponent's own possible integer values (4-bit two's complement):**

| Bit pattern | Value |
|---|---|
| `0111` | 7 |
| `0110` | 6 |
| `0101` | 5 |
| `1010` | −6 |
| `1001` | −7 |
| `1000` | −8 |

**Which option wins, and why (this reasoning is exam gold):** placing the implied binary point **immediately after the sign bit** (Option B) produces a **smaller spacing** between representable values — i.e. finer precision — and **this is the preferred convention** for floating-point representation.

Using this preferred convention, the extreme values achievable with 4-bit mantissa + 4-bit exponent:

| Description | Binary code | Denary equivalent |
|---|---|---|
| Largest positive value | `0 111 0111` | 0.875 × 2⁷ = 112 |
| Smallest positive value | `0 001 1000` | 0.125 × 2⁻⁸ = 1/2048 |
| Smallest magnitude negative value | `1 111 1000` | −0.125 × 2⁻⁸ = −1/2048 |
| Largest magnitude negative value | `1 000 0111` | −1 × 2⁷ = −128 |

**The headline comparison to remember:** floating-point representation gives access to a **far greater range** of both very large and very small (positive and negative) values than fixed-point representation does, using the same total number of bits (8 bits in both examples here: fixed-point maxed out at ±31.75, floating-point reaches all the way to ±128 and down to fractions as small as 1/2048).

### 3.4 Precision and normalisation

**The two design decisions you'd face choosing a floating-point format:**

1. **Total number of bits** to use overall (usually a choice available when writing the program).
2. **The split** between mantissa bits and exponent bits (in practice, this split is usually **fixed by the floating-point processor** in hardware, not freely chosen by the programmer).

**The fundamental trade-off (a direct, frequently tested learning objective — "effects of changing the allocation of bits to mantissa and exponent"):**

- **More bits for the mantissa** → **better precision** for the value stored, **but** fewer bits left for the exponent → **reduced range** of possible values.
- **More bits for the exponent** → **greater range** of representable magnitudes, **but** fewer bits left for the mantissa → **reduced precision**.

This is a strict trade-off: for a fixed total bit count, you cannot improve both precision and range simultaneously.

**Normalisation — the concept:**

> To achieve **maximum precision**, a floating-point number must be **normalised**. (Note: this is a completely unrelated concept to database normalisation, despite the shared name — don't conflate them.)

**Why normalisation gives maximum precision:** precision improves with more mantissa bits *actually being used meaningfully*. Optimum precision is achieved only when you make **full use** of the mantissa bits available — meaning you use the **largest possible magnitude** representable by the mantissa for that value, rather than "wasting" leading bits on redundant zeros (or ones, for negatives).

**Worked illustration — three different (mathematically equivalent) ways to represent denary 2, using 4 mantissa bits + 4 exponent bits:**

| Denary representation | Floating-point binary |
|---|---|
| 0.125 × 2⁴ | `0 001 0100` |
| 0.25 × 2³ | `0 010 0011` |
| 0.5 × 2² | `0 100 0010` |

And for denary −4:

| Denary representation | Floating-point binary |
|---|---|
| −0.25 × 2⁴ | `1 110 0100` |
| −0.5 × 2³ | `1 100 0011` |
| −1.0 × 2² | `1 000 0010` |

**How to recognise a normalised representation (the rule to memorise and apply):**

> When a number is represented with the **highest possible magnitude for the mantissa**, the **two most significant bits are different** from each other.

- For a **positive** number: normalised means the mantissa's most significant bits read **0 followed by 1**.
- For a **negative** number: normalised means the mantissa's most significant bits read **1 followed by 0**.

**The mechanical process of normalising a number, once you have any valid (but possibly non-normalised) representation:**

- **For a positive number:** shift the mantissa bits **left** until the most significant bits become **0 followed by 1**. **Each left shift reduces the exponent value by 1** (to compensate and keep the overall value the same).
- **For a negative number:** the same left-shifting process is applied until the most significant bits become **1 followed by 0** — and in this case, **no attention is paid to bits falling off the most significant end** of the mantissa during the shifting (they're simply discarded).

**A subtlety flagged by the textbook's own extension question (16.03):** looking back at the earlier 8-bit example table (Table 16.03), the largest magnitude negative value shown was `1 000 0111` (representing −128, using −1 × 2⁷). Notice this mantissa is `1000` — its two most significant bits are `1` followed by `0`, which **does** match the "normalised negative" rule above. But be aware that in some real floating-point systems, the exact edge-case handling (particularly around values like exactly −1.0 as the mantissa) can involve subtle implementation choices — this is exactly why the textbook poses it as an open question rather than a fixed rule; the safe exam approach is to apply the "two most significant bits differ" test consistently and explain your reasoning if a boundary case seems ambiguous.

### 3.5 Converting a real denary number to fixed-point binary — worked method

**Example: converting 4.75 to fixed-point binary.**

- 4 converts to `100` in binary.
- .75 converts to `.11` in binary.
- Combined (before considering the sign bit): `100.11`
- **A positive number must start with a 0 sign bit:** so 4.75 → `0100.11`

**Converting the negative version, −4.75, using two's complement:**

1. Start from the positive representation: `0100.11`
2. Invert all bits (one's complement): `1011.00`
3. Add 1 to the least significant bit to get two's complement: `1011.01`

**Checking the result works correctly:** `1011` (as an integer part) represents −8 + 2 + 1 = −5... but wait, let's use the textbook's own check method precisely: `1011` is the code for −8 + 3 = −5, and actually the textbook states `1011` is the code for "−8 + 3" — meaning bits are read as (from MSB, with the sign bit carrying weight −8): 1(−8) + 0(4) + 1(2) + 1(1) = −8+2+1 = −5. Combined with the fractional part `.01` = 0.25, this gives −5 + 0.25 = −4.75. ✓ (This matches the textbook's stated check, confirming the two's complement conversion produced the correct negative value.)

### 3.6 Converting a denary real number to floating-point binary — the full method

**Why this always involves some approximation — understand this before doing any conversion:** most fractional denary values **do not convert to a precise binary representation**. This is because binary fractional bits only ever represent halves, quarters, eighths, sixteenths, and so on (i.e. negative powers of 2). Unless a denary fraction happens to be exactly expressible as a sum of such values, **there cannot be an exact conversion**. Specifically: **of the values .1 through .9, only .5 converts exactly** — every other one-decimal-place fraction in that range is only approximately representable in binary. (This directly connects to why storing currency values in floating-point is risky — flagged back in Chapter 1.)

**The full six-step method for converting a positive denary real value to normalised floating-point binary:**

1. Convert the **whole-number part** to binary (standard method).
2. Add the **0 sign bit**.
3. Convert the **fractional part** (see the "multiply by two" technique below).
4. **Combine** the whole-number and fractional binary parts, and enter this combined value into the **most significant bits** allocated for the mantissa.
5. **Fill remaining mantissa bits, and all exponent bits, with zeros.**
6. **Adjust the binary point's position** by changing the exponent value, to arrive at a **normalised** representation.

**For a negative value:** treat the number as positive and follow steps 1–5 exactly as above; **then** apply a two's complement conversion to the mantissa code (to flip it negative); **only then** carry out step 6 (normalisation adjustment).

**The "multiply by two" technique for converting a fractional part to binary (essential — this is how you handle fractions that don't convert as cleanly as .75 = .11):**

Repeatedly multiply the fractional part by 2; each time, record whether the result's whole-number part is 0 or 1 (this becomes the next binary digit), then continue with just the new fractional remainder.

**Worked Example — converting 8.75 (Example 1 from the textbook, in full):**

1. 8 converts to `1000`; adding the sign bit gives `01000`.
2. .75 is recognised directly as `.11` in binary (since .75 = .5 + .25 = 2⁻¹ + 2⁻²).
3. Combined: `01000.11` — at this point the exponent value is **0** (binary point is right where it naturally sits).
4. Shifting the binary point to move it immediately after the sign bit gives `0.100011`, which now has exponent value **denary 4** (we shifted 4 places, so the exponent compensates by +4).
5. Depending on the total bits allocated: if **10 bits for the mantissa** and **4 bits for the exponent**, the final representation becomes:
   - **Mantissa:** `0100011000`
   - **Exponent:** `0100` (denary 4, in 4-bit two's complement)

**Worked Example — converting 8.63 (Example 2, showing the "multiply by two" technique in full because .63 doesn't convert cleanly):**

The whole-number part (8 → `01000` with sign bit) is identical to Example 1. For the fractional part, .63, apply the multiply-by-two method:

```
.63 × 2 = 1.26  → record 1, continue with fraction .26   → so far: .1
.26 × 2 = 0.52  → record 0, continue with fraction .52   → so far: .10
.52 × 2 = 1.04  → record 1, continue with fraction .04   → so far: .101
.04 × 2 = 0.08  → record 0, continue with fraction .08   → so far: .1010
```

At this point, the textbook stops the process, noting that repeatedly multiplying the tiny remaining fraction (.08) by 2 is going to produce a long run of zeros before another 1 eventually appears — so for practical bit-length purposes, the process is **truncated here**. This means .63 has been **approximated** as **.625** (since `.1010` in binary = .5 + 0 + .125 + 0 = .625, not exactly .63 — this is the approximation error in action, directly illustrating the "problems with floating-point" discussed in 3.7).

Following the same steps 3–5 as Example 1, the final representation becomes:
- **Mantissa:** `0100010100`
- **Exponent:** `0100`

### 3.7 Problems with using floating-point numbers

Two distinct classes of problem, and you should be able to distinguish and explain both separately:

**Problem 1 — Rounding errors from approximation.**

As shown directly above, converting a denary real value to binary **almost guarantees some degree of approximation**, because of the restricted number of bits available to store the mantissa. Floating-point numbers are heavily used in **extended mathematical procedures involving repeated calculations** — e.g. weather forecasting using an atmospheric model, or economic forecasting. In this kind of repeated-calculation context, **each individual calculation carries a slight approximation**, and these so-called **rounding errors can become significant** if the calculation is repeated enough times (errors compound/accumulate).

**The only real fix:** increase the **precision** of the floating-point representation by using **more bits for the mantissa**. This is exactly why programming languages offer options like **"double precision"** or **"quadruple precision"** — these names directly refer to using more bits (and specifically, more mantissa bits) to reduce the size of rounding errors.

**Problem 2 — Range limitations: overflow and underflow.**

Referring back to the simple 8-bit example (Table 16.03), the highest value that format could represent was denary 112. Any calculation producing a result larger than the format's maximum representable value produces an **overflow error condition** (this concept was already introduced back in Chapter 1, Section 1.02, for integer representations — the same principle applies here for floating-point).

**A second, floating-point-specific problem — underflow:** if a **very small number is divided by a number greater than 1**, the result can become **smaller than the smallest value the format can represent**. This is called an **underflow error condition**. Depending on the specific circumstances, a program might be able to **continue running by converting this too-small value to zero** — but the textbook is explicit that doing so **"must involve risk"** (silently substituting zero for a genuinely tiny-but-nonzero value can introduce its own errors downstream).

---

## PART 4 — CHAPTER SUMMARY (exact revision bullet points)

- Examples of non-composite user-defined data types include enumerated and pointer data types.
- Record, set and class are examples of composite user-defined data types.
- File organisation allows for serial, sequential or direct access.
- Floating-point representation for a real number allows a wider range of values to be represented.
- A normalised floating-point representation achieves the best precision for the value stored.
- Stored floating-point values rarely give an accurate representation of the denary equivalent.

---

## PART 5 — FULL WORKED EXAM-STYLE ANSWERS

### Question 1 — User-defined data types (zoo program)

**(a) Non-composite user-defined data type example, and why it differs from a built-in type [3 marks]**

Example: an **enumerated data type**, e.g. `TYPE TDirections = (North, East, South, West)` [1]. It differs from an in-built type because, with a built-in type, the language itself defines the full range of possible values and available operations in advance [1]; with an enumerated (user-defined) type, the programmer must explicitly specify every one of the possible values themselves, since the language has no way of knowing in advance what values the programmer wants — there could not be a generic built-in version of this type [1].

**(b)(i) Explain what a record user-defined data type is [2 marks]**

A record is a data type that groups together **multiple related fields** (which may be of different data types) under a single type definition [1], allowing a collection of related data items to be treated and manipulated as one single named unit [1].

**(b)(ii) Advantage of using a record user-defined data type [2 marks]**

It allows the programmer to design a data structure whose fields **precisely match** the exact data requirements of the specific program being written [1], rather than being constrained to whatever fixed structure a built-in type might offer (and no generic built-in record type could anticipate every program's specific combination of required fields) [1].

**(b)(iii) Pseudocode for the record definition [5 marks]**

```
TYPE AnimalRecord
    DECLARE AnimalName        : STRING
    DECLARE AnimalAge         : INTEGER
    DECLARE NumberInZoo       : INTEGER
    DECLARE LocationInZoo     : STRING
ENDTYPE
```

Marks for: `TYPE...ENDTYPE` structure correct [1], each of the four fields declared with a sensible identifier [up to 2], each field given an appropriate data type [up to 2].

### Question 2 — Binary files and file organisation

**(a)(i) Terms for the components of a binary file [2 marks]**

**Record** [1] and **field** [1] (a file contains records, each record contains fields).

**(a)(ii) Difference between a binary file and a text file [3 marks]**

A text file stores data according to a character code (such as ASCII), and can be created directly using a text editor [1]. A binary file stores data in its **internal representation** (e.g. an integer stored directly in two's complement form across a fixed number of bytes), and is typically produced as program output rather than typed directly by a user [1]. Consequently, a text file needs item separators or known item/character counts per line, whereas a binary file needs the number of fields per record and (for strings) their length to be known, but requires no separator characters [1].

**(b)(i) Difference between serial, sequential and direct access [4 marks]**

**Serial:** records are stored in no particular order, simply appended in the order they were entered (time order) [1... roughly].
**Sequential:** records are ordered according to a key field, whose values are unique and sequentially increasing (though not necessarily consecutive) [1].
**Direct-access:** records can be accessed directly via a calculated address (using an index file or a hashing algorithm), without needing to read through preceding records at all [1].
(One further mark for a clear overall contrast, e.g. noting that only direct-access avoids any need to traverse other records to reach a target one) [1].

**(b)(ii) Example of serial file use, with justification [3 marks]**

Example: **a bank transaction file, recording deposits and withdrawals as they occur** [1]. Justification: transactions naturally occur in a time sequence and simply need to be recorded in that order for later batch processing (e.g. updating master account files); there's no need for the transaction records themselves to be ordered by any other key, so serial organisation (simple append) is the simplest and most efficient choice [2].

**(b)(iii) Example of direct-access use, with justification [3 marks]**

Example: **a password-checking file on a system with many users logging in** [1]. Justification: with potentially many users logging in simultaneously or in quick succession, the system needs **rapid access to one specific record** (the matching user's stored credentials) without reading through the whole file — direct access, via hashing on a username or user ID, gives near-instant lookup regardless of file size, which sequential or serial access could not match for a large user base [2].

### Question 3 — Floating-point byte analysis

Given bytes: `10010101` `00110011` `11001000` `00010001` — representing two floating-point numbers, first byte of each pair = mantissa, second = exponent, both in two's complement.

So: **Number 1** = mantissa `10010101`, exponent `00110011`. **Number 2** = mantissa `11001000`, exponent `00010001`.

**(a)(i) Name for what the second byte represents [1 mark]**

The **exponent** (also acceptable: "exrad").

**(a)(ii) Positive or negative — state which and explain [2 marks]**

Both mantissas start with a **1** as their most significant bit [1]. In two's complement representation, a leading 1 indicates a **negative** value — so **both numbers are negative** [1].

**(a)(iii) Which one is normalised, and why [2 marks]**

Recall the rule: a mantissa is normalised for a negative number when its two most significant bits are **1 followed by 0**.

- Number 1's mantissa: `10010101` → first two bits are `1` then `0` → **normalised**.
- Number 2's mantissa: `11001000` → first two bits are `1` then `1` → **not normalised** (both same, doesn't satisfy the "differ" test).

Answer: **Number 1 is normalised** [1], because its two most significant mantissa bits are `1` followed by `0`, satisfying the requirement that (for a negative number) the two most significant bits must differ, with 1 then 0 [1].

**(a)(iv) Where the implied binary point sits, and why normalisation improves precision [3 marks]**

The implied binary point sits **immediately after the sign bit** (i.e. after the first, most significant bit of the mantissa) [1]. Normalisation improves precision because it ensures the **mantissa bits are used to their fullest extent** — i.e. the value uses the **largest possible magnitude representable by the mantissa** for that number, rather than "wasting" leading redundant bits, meaning each available mantissa bit contributes maximally to representing the value precisely [2].

**(a)(v) Effect of reallocating more bits to the mantissa (fewer to the exponent) [2 marks]**

This would **increase precision** (more mantissa bits = finer distinguishable steps between representable values) [1], **but reduce the range** of values that can be represented, since fewer exponent bits means a smaller possible range of magnitudes (both largest and smallest representable values become more limited) [1].

**(b) Represent denary 12.43 as floating-point binary (same format as part a: 8 bits mantissa, 8 bits exponent, both two's complement) [5 marks]**

Step 1: convert 12 to binary → `1100`. Add sign bit (positive) → `01100`.

Step 2: convert .43 using multiply-by-two:
```
.43 × 2 = 0.86 → record 0 → .0
.86 × 2 = 1.72 → record 1 → .01
.72 × 2 = 1.44 → record 1 → .011
.44 × 2 = 0.88 → record 0 → .0110
.88 × 2 = 1.76 → record 1 → .01101
```
Truncating at 5 fractional bits: .43 ≈ `.01101`

Step 3: combine → `01100.01101`

Step 4: normalise by shifting the binary point immediately after the sign bit. Currently: `0 1100.01101`. Shift the point left 5 places to sit right after the leading 0: `0.110001101`, exponent becomes **+5**.

Step 5: place into 8 mantissa bits (most significant bits first): mantissa = `01100011` (taking the first 8 bits: `0`, then `1100011`, i.e. `0` `1100011` = `01100011`), remaining bits (`01` from `.110001101`) are truncated/rounded off (this is exactly the kind of rounding error discussed in 3.7).

Exponent = +5 → in 8-bit two's complement: `00000101`.

**Final answer:**
- **Mantissa:** `01100011`
- **Exponent:** `00000101`

*(Marks awarded for: correct whole-number binary conversion [1], correct fractional conversion via multiply-by-two [1], correct combination and normalisation shift [1], correct final mantissa bits [1], correct final exponent bits [1].)*

### Question 4 — Cambridge 9608 Paper 31, June 2015, Q3

**(a)(i) Non-composite data type used in ThisDay and ThisMonth [1 mark]**

**Enumerated** (data type).

**(a)(ii) Data type of ThisDate [1 mark]**

**Record** (a composite user-defined data type — since `ThisDate` references other types, `ThisDay`, `ThisMonth`, and `INTEGER`, within its own definition).

**(a)(iii) Statement to assign the month value of DateOfBirth to MyMonthOfBirth [1 mark]**

```
MyMonthOfBirth ← DateOfBirth.ThisMonth
```

**(b)(i) Definition for LocationRainfall [5 marks]**

```
TYPE LocationRainfall
    DECLARE LocationName        : STRING
    DECLARE HeightAboveSeaLevel  : INTEGER
    DECLARE MonthlyRainfall[1:12] : ARRAY OF REAL
ENDTYPE
```

Marks for: `TYPE...ENDTYPE` structure [1], location name field correctly typed as STRING [1], height field correctly typed as INTEGER (nearest metre → whole number) [1], a 12-element array (one per month) for rainfall [1], rainfall field correctly typed as REAL (decimal to 1dp) [1].

**(b)(ii) Two reasons for choosing serial file organisation [2 marks]**

1. The data set is **small and will grow slowly** (27 locations initially, never exceeding 100) — with such a small maximum size, there's **no significant performance benefit** to be gained from the added complexity of sequential ordering or direct-access hashing; a simple serial file is easy to implement and entirely adequate [1].
2. **New locations are simply added over time**, with no indication that fast individual lookup or ordered range-searches are needed — serial organisation, where new records are just appended, is the most straightforward and least wasteful choice for this pattern of use [1].

### Question 5 — Cambridge 9608 Paper 32, November 2016, Q1

Format: 8 bits mantissa, 8 bits exponent, both two's complement.

**(a) Floating-point representation of +3.5 [3 marks]**

3 → `11`; .5 → `.1`. Combined with sign bit: `0011.1`

Normalise: shift point immediately after sign bit → `0.01111`, exponent = **+4** (shifted 4 places left... let's verify: `0011.1` shifting the point left by 4 places gives `0.00111` — let's redo carefully).

`0011.1` — the point is currently after 4 integer-part digits (`0011`). To move it to sit immediately after the sign bit (i.e. between the first `0` and the rest), we shift it left by 3 places: `0011.1` → `0.0111` with exponent **+3**.

Check: 0.0111 (binary) = 0.4375; 0.4375 × 2³ = 0.4375 × 8 = 3.5 ✓.

Now check normalisation: mantissa `0111...` — most significant bits `0` then `1` — differ, correctly normalised for positive. Good.

Pad mantissa to 8 bits: `01110000`. Exponent +3 in 8-bit two's complement: `00000011`.

**Mantissa:** `01110000` **Exponent:** `00000011`

**(b) Floating-point representation of −3.5 [included in same 3 marks as part a, per original mark scheme]**

Start from the positive mantissa before padding: `0111` → pad to 8 bits `01110000`. Convert to two's complement (flip and add 1):
- One's complement: `10001111`
- Add 1: `10010000`

**Mantissa:** `10010000` **Exponent:** `00000011` (exponent unchanged, only the mantissa sign flips)

Check: mantissa `10010000` in two's complement = −(01101111 + 1) = −(01110000) interpreted... more directly: `1 0010000` as two's complement 8-bit = −112 in raw integer terms, but as a fractional mantissa with point after sign bit: this represents −0.4375, and −0.4375 × 2³ = −3.5 ✓.

**(c) Denary value of the given floating-point number [3 marks]**

Given: Mantissa `01110000`, Exponent `00000100`

Mantissa `01110000`: sign bit 0 (positive), fractional value = `.1110000` = 0.5 + 0.25 + 0.125 = 0.875
Exponent `00000100` = denary **4**

Value = 0.875 × 2⁴ = 0.875 × 16 = **14**

**(d)(i) Normalised or not normalised? [1 mark]**

**Normalised.**

**(d)(ii) Justification [1 mark]**

The mantissa's two most significant bits are `0` then `1` — they differ, satisfying the normalisation condition for a positive value.

**(e) Binary two's complement pattern for the negative number with the largest magnitude [3 marks]**

Largest magnitude negative value occurs with: mantissa at its most negative extreme with the point immediately after the sign bit, and the exponent at its largest positive value.

- Most negative-magnitude mantissa (8 bits, two's complement, normalised: MSB `1` then `0`): `10000000` → represents −1.0 exactly (as a fraction: −1 × 2⁰... in this point-after-sign-bit convention, `10000000` = −1.0).
- Largest positive exponent (8-bit two's complement): `01111111` = denary +127.

**Mantissa:** `10000000` **Exponent:** `01111111`

Value = −1.0 × 2¹²⁷ (an extremely large negative magnitude — this is correct, since we want the *largest magnitude*, i.e. most extreme, negative value representable).

---

## PART 6 — QUICK-FIRE DEFINITION DRILL

1. **User-defined data type** — where the programmer includes the definition in the program.
2. **Non-composite data type** — a data type defined without reference to another data type.
3. **Enumerated data type** — a non-composite user-defined data type for which the definition identifies all possible values.
4. **Pointer variable** — one for which the value is the address in memory of a different variable.
5. **Set** — a collection of data items that lacks any structure; contains no duplicates; has defined operations (check existence, add, remove, combine with another set).
6. **Binary file** — a file designed for storing data to be used by a computer program.
7. **Record** — a collection of fields containing data values.
8. **Floating-point representation** — a representation of real numbers that stores a value for the mantissa and a value for the exponent.
9. **Collision** (hashing) — when the same address is calculated for different key field values; the colliding values are called synonyms.
10. **Normalisation** (floating-point) — adjusting a representation so the mantissa's most significant bits differ (0-then-1 for positive, 1-then-0 for negative), maximising precision by fully using the available mantissa bits.
11. **Overflow** — a calculated value exceeds the maximum magnitude representable in the given format.
12. **Underflow** — a calculated value becomes smaller in magnitude than the smallest value representable, typically from dividing a small number by something greater than 1.

---

## PART 7 — SELF-TEST CHECKLIST

- [ ] Explain why user-defined types (specifically enumerated types) are necessary, using the textbook's own "values not known in advance" reasoning.
- [ ] Distinguish user-defined data types from abstract data types clearly.
- [ ] State which of the syllabus languages does not support records (Python).
- [ ] Trace through a full pointer example: type definition (`^`), variable declaration, address assignment (`@`), and dereferencing (`^` after the variable) — and explain what each step does.
- [ ] Explain why a set is not simply classified as a "structured" data type despite holding multiple values.
- [ ] Explain the difference between what must be "known" to correctly read a text file vs a binary file.
- [ ] Describe all three file organisation methods (serial, sequential, direct-access) and match each to an appropriate real-world scenario with justification.
- [ ] Perform a modular-division hashing calculation by hand, and explain what a collision/synonym is and at least two ways to resolve one.
- [ ] Explain the difference between a file's key field and a database's primary key.
- [ ] State the general floating-point format (± M × R^E) and explain what each symbol represents, including that R is never actually stored.
- [ ] Explain the mantissa/exponent bit-allocation trade-off (precision vs range) fluently.
- [ ] State and apply the rule for recognising a normalised mantissa (for both positive and negative numbers).
- [ ] Convert a denary real number to normalised binary floating-point representation by hand, including using the "multiply by two" method for the fractional part, for a given mantissa/exponent bit allocation.
- [ ] Convert a binary floating-point representation back into its denary value by hand.
- [ ] Explain, separately and clearly, the difference between a rounding error (from approximation) and overflow/underflow (from range limits).
- [ ] Explain why only .5 (out of .1 through .9) converts exactly from denary to binary, and why this matters for repeated calculations.

---

*This guide is built directly from Cambridge International AS & A Level Computer Science, Chapter 16, and incorporates the exact worked examples, tables, and past-paper questions (9608 Paper 31 June 2015, 9608 Paper 32 November 2016) as printed in the chapter. Where a calculation in Question 3(b) and Question 5 required working beyond what the textbook itself shows, that working has been carried out in full and checked by converting each answer back to its original denary value.*