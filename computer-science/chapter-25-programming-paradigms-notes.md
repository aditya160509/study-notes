# 📘 Chapter 25: Programming Paradigms - Cambridge International AS & A Level Computer Science (9618)

## Cambridge International AS & A Level Computer Science - Part 4

> **Rule + fully solved examples.** Everything the examiner can ask from Chapter 25: what a programming paradigm is and the characteristics of the four paradigms in the 9618 syllabus — low-level, imperative, object-oriented and declarative. Includes comparison tables, code examples and exam-style questions with full solutions.

**Learning objectives (Chapter 25):**
- Show understanding of what is meant by a programming paradigm
- Show understanding of the characteristics of:
  - low-level programming
  - imperative programming
  - object-oriented programming
  - declarative programming

---

## 25.01 What Is a Programming Paradigm?

A **programming paradigm** is a **fundamental style of programming**. It is a way of thinking about and structuring a solution, not a single language feature.

- A paradigm shapes how you decompose a problem and what the code looks like.
- Paradigms are supported by language features.
- One language can support **more than one** paradigm (e.g. Python supports imperative, object-oriented and, to some extent, functional styles).
- Paradigms overlap; the boundaries are not rigid.

**Analogy:** the same journey can be planned as a turn-by-turn route (imperative), as a set of destinations and relationships (declarative), as a collection of vehicles that know how to drive themselves (object-oriented), or as direct control of the engine and wheels (low-level).

The four paradigms in the syllabus:

| Paradigm | Central idea | Typical languages |
|---|---|---|
| **Low-level** | Direct control of memory/registers | Assembly, machine code |
| **Imperative** | Sequence of explicit commands/statements | Pascal, C, Basic, Python |
| **Object-oriented** | Objects with data + methods interacting | Java, Python, C++, VB.NET |
| **Declarative** | Describe **what** is true/needed; system works out **how** | Prolog, SQL |

> **Exam tip:** the key distinction is **how vs what**. Imperative says *how* to solve the problem step by step; declarative says *what* the solution should satisfy.

---

## 25.02 Low-Level Programming Paradigm

Low-level programming gives the programmer the ability to **manipulate memory addresses and registers directly** and exploit the architecture of a particular processor.

**Characteristics:**

- Instructions map closely to the processor's instruction set.
- The programmer manages registers, memory addresses and the stack explicitly.
- Code is **processor-specific** — each processor family has its own instruction set (e.g. the Intel x86 family).
- Very little abstraction: no built-in high-level structures such as lists or objects.
- Precise control of hardware, timing and memory.
- Programs are harder to write, read, debug and port.

**Example — assembly (conceptual):**

```
LDM #10        ; load immediate value 10 into the accumulator
STO A          ; store accumulator in memory location A
LDD B          ; load B
ADD A          ; add A
STO C          ; store result in C
```

**Example — machine code:** binary opcodes and operands, executed directly by the CPU.

**When used:**

- device drivers, embedded systems and firmware;
- boot loaders and operating-system kernels;
- performance-critical inner loops;
- situations where memory is extremely limited or exact timing matters.

**Advantages:** maximum control, high performance, minimal memory overhead.
**Disadvantages:** difficult, error-prone, not portable, slow to develop.

See Chapter 28 for low-level programming in detail.

---

## 25.03 Imperative Programming Paradigm

Imperative programming writes a program as a **sequence of explicit steps** that the processor executes. The programmer specifies **how** to obtain the result.

**Characteristics:**

- Sequence, selection and iteration (if, case, for, while).
- Variables and assignment change program state.
- Subroutines/procedures group reusable steps.
- The order of statements matters.
- **Procedural programming** is a subset of imperative programming: the program is organised into procedures/functions.

**Example — imperative Python:**

```python
total = 0
for number in [4, 7, 2, 9]:
    total = total + number
print(total)
```

The programmer states exactly: start at zero, visit each item, add it, print the result.

**Example — pseudocode:**

```
Total ← 0
FOR Index ← 0 TO 3
    Total ← Total + List[Index]
NEXT Index
OUTPUT Total
```

**Advantages:**

- Natural match to the way a CPU executes instructions.
- Straightforward to trace and debug.
- Efficient and widely supported.
- Good for algorithms with clear step-by-step logic.

**Disadvantages:**

- Large programs can become hard to maintain.
- State changes are spread through the code, making reasoning harder.
- Reuse is limited unless carefully structured.
- Not ideal for problems naturally expressed as rules or relationships.

---

## 25.04 Object-Oriented Programming Paradigm

The object-oriented paradigm is based on **objects interacting with one another**. An object combines **data** (attributes) and **behaviour** (methods).

**Characteristics:**

- **Class** — a template/blueprint.
- **Object** — an instance of a class.
- **Encapsulation** — data is hidden (private) and accessed through methods.
- **Inheritance** — a subclass reuses and extends a superclass.
- **Polymorphism** — the same method call behaves differently for different classes.
- **Abstraction** — expose only the essential interface.
- Objects communicate by calling each other's methods.

**Example — Python:**

```python
class Account:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance          # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

class SavingsAccount(Account):
    def add_interest(self, rate):
        self.deposit(self.get_balance() * rate)
```

`SavingsAccount` inherits `deposit` and `get_balance` from `Account`, and adds `add_interest`.

**Advantages:**

- Models real-world entities naturally.
- Encapsulation protects data and reduces coupling.
- Inheritance and polymorphism promote reuse.
- Large systems are easier to extend and maintain.
- Teams can work on separate classes.

**Disadvantages:**

- Can be over-engineered for simple problems.
- More design effort up front.
- Objects consume memory and method calls add overhead.
- Poorly designed inheritance hierarchies are hard to change.

See Chapter 27 for OOP in detail.

---

## 25.05 Declarative Programming Paradigm

In declarative programming, the programmer writes a **specification** of the problem — **what** is true or what result is wanted — rather than a sequence of steps. The system works out **how** to satisfy it.

Declarative programs are expressed as **formal logic** (or queries), and computation is deduction from those statements.

**Characteristics:**

- No explicit control flow (no loops or assignment in the imperative sense).
- The programmer defines **facts** and **rules**, then asks **queries**.
- The language's inference engine searches for a solution.
- The same specification can be evaluated in different ways by the system.
- Often concise and close to the problem statement.

**Example — Prolog:**

```prolog
parent(tom, bob).
parent(bob, ann).

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
```

Query:

```prolog
?- grandparent(tom, ann).
true.
```

The programmer states the relationship; Prolog searches for a proof.

**Example — SQL:**

```sql
SELECT Name
FROM Students
WHERE Grade = 'A';
```

The query says **what** rows are wanted; the database engine decides how to retrieve them.

**Advantages:**

- Concise and expressive for rule-based problems.
- Easy to modify by adding facts/rules.
- The system handles search and backtracking.
- Naturally suits databases, expert systems and constraint problems.

**Disadvantages:**

- Less control over performance.
- Harder to debug when inference goes wrong.
- Not suitable for every kind of problem.
- Requires a different way of thinking.

See Chapter 29 for declarative programming in Prolog.

---

## 25.06 Comparing the Paradigms

| Feature | Low-level | Imperative | Object-oriented | Declarative |
|---|---|---|---|---|
| Core idea | Direct hardware control | Step-by-step commands | Objects + methods | Facts, rules, queries |
| Programmer specifies | Registers/addresses | How | How, structured around objects | What |
| Control flow | Jumps, branches | Sequence/selection/iteration | Methods + message passing | Implicit (inference engine) |
| Data | Raw memory | Variables/arrays | Objects with attributes | Facts/relations |
| Reuse | Macros/subroutines | Procedures/functions | Classes, inheritance | Rules, predicates |
| Portability | Very low | High | High | High |
| Typical use | Drivers, embedded | General algorithms | Large applications | Databases, AI, logic |
| Example language | Assembly | C, Pascal, Python | Java, C++, Python | Prolog, SQL |

### 25.06.1 Matching statements to paradigms

| Statement | Paradigm |
|---|---|
| "Commands available depend on the type of processor" | Low-level |
| "Information hiding is used to protect internal properties of an object" | Object-oriented |
| "Statements operate on data" | Imperative |
| "Answer a question via a search for a solution" | Declarative |
| "Data is combined with procedures" | Object-oriented |
| "First do this and then do that" | Imperative |
| "The basic concept is a relation" | Declarative |

> **Exam tip:** the phrase **"information hiding"** → OOP; **"relation"** → declarative; **"processor-specific"** → low-level; **"sequence of steps"** → imperative.

### 25.06.2 Characteristic statement examples

| Paradigm | Characteristic statement | Language |
|---|---|---|
| Low-level | `LDD A` | Assembly |
| Imperative | `Total ← Total + 1` | Pseudocode/Pascal |
| Object-oriented | `student.setGrade("A")` | Java/Python |
| Declarative | `grandparent(X, Z) :- parent(X, Y), parent(Y, Z).` | Prolog |

---

## 25.07 Choosing a Paradigm

There is no universally best paradigm. The choice depends on:

1. **The problem's natural shape**
   - Rules and relationships → declarative.
   - Entities with state and behaviour → object-oriented.
   - Simple sequential algorithm → imperative.
   - Hardware control → low-level.
2. **Performance and memory constraints** — low-level or imperative may be necessary.
3. **Maintainability and team size** — OOP helps large, evolving systems.
4. **Available libraries and language support** — e.g. SQL for databases, Prolog for logic.
5. **Portability** — high-level paradigms are usually more portable.

Many real systems are **multi-paradigm**: an application might use OOP for structure, imperative code for algorithms, SQL for data access, and assembly for a performance-critical routine.

**Worked example 25.01 — choose a paradigm**

A hospital needs a system to manage patients, doctors, appointments and billing, with a database and a rules engine for alerts.

**Answer:** use **object-oriented** programming for the entities (`Patient`, `Doctor`, `Appointment`, `Invoice`) and their behaviour; use **declarative SQL** for querying the database; use **imperative** code for calculation and control; use a **declarative rules engine** for alerts (e.g. "if two appointments overlap, warn"). This is a multi-paradigm design, which is normal for a large system.

---

## 📝 Exam-style Questions with Full Solutions

### Question 1 — Define a paradigm (2 marks)

State what is meant by a programming paradigm.

**Solution:** A fundamental style of programming — a way of thinking about and structuring a program, supported by particular language features. Different paradigms suit different ways of decomposing a problem.

### Question 2 — Characteristics (8 marks)

State two characteristics of each of the low-level and declarative paradigms.

**Solution:**

**Low-level:**

1. Direct manipulation of memory addresses and registers.
2. Instructions are specific to a processor/instruction set, so programs are not portable.

**Declarative:**

1. The programmer states **what** is required rather than **how** to compute it.
2. Programs consist of facts/rules or queries, and the system performs inference/search to find the answer.

### Question 3 — Match the paradigm (4 marks)

Match each statement to the correct paradigm.

(a) "The program is a sequence of instructions, one after another."
(b) "A class hides its data and exposes methods."
(c) "A query asks whether a relationship holds."
(d) "The programmer uses registers and memory addresses directly."

**Solution:**

(a) Imperative
(b) Object-oriented
(c) Declarative
(d) Low-level

### Question 4 — Imperative vs declarative (6 marks)

Explain the difference between imperative and declarative programming, using an example of each.

**Solution:**

Imperative programming specifies **how** to solve a problem as a sequence of explicit steps, using variables, assignment, selection and iteration. Example: a loop that adds each number in a list to a total.

Declarative programming specifies **what** is true or what result is wanted, and the system determines how to find it. Example: a Prolog rule `grandparent(X,Z) :- parent(X,Y), parent(Y,Z).` followed by a query, or an SQL `SELECT ... WHERE ...` statement. The programmer does not write the search loop.

### Question 5 — OOP features (6 marks)

Explain how encapsulation and inheritance support reusable, maintainable programs.

**Solution:**

**Encapsulation** keeps an object's data private and allows access only through methods. This protects the data from invalid changes, hides implementation details and lets the internal implementation change without breaking code that uses the object.

**Inheritance** lets a subclass reuse the attributes and methods of a superclass and add or override behaviour. This avoids duplicating common code, makes the relationships between concepts explicit, and allows new types to be added with little change to existing code.

### Question 6 — Multi-paradigm (4 marks)

Explain why a large application might use more than one paradigm.

**Solution:**

Different parts of a system have different natural structures. Objects suit modelling entities and their behaviour; SQL suits querying relational data; imperative code suits step-by-step calculations; declarative rules suit constraints and alerts; low-level code may be needed for performance or hardware access. Using the most appropriate style for each part improves clarity, maintainability and performance. Most modern languages support multiple paradigms, so mixing them is practical.

---

# 📋 Formula / Fact Sheet (Chapter 25)

**Paradigm:** a fundamental style of programming.

**Low-level:** direct memory/register access; processor-specific; assembly/machine code; used for drivers, embedded systems, kernels.

**Imperative:** sequence of explicit steps; sequence/selection/iteration; variables and assignment; "how"; procedural is a subset; C, Pascal, Python.

**Object-oriented:** classes and objects; encapsulation, inheritance, polymorphism, abstraction; data + methods; Java, C++, Python.

**Declarative:** state facts/rules or queries; "what"; inference/search; Prolog, SQL.

**Key phrases:**

- Low-level → "processor-specific", "registers", "memory addresses".
- Imperative → "sequence of steps", "first do this then that", "statements operate on data".
- OOP → "information hiding", "data combined with procedures", "object", "class".
- Declarative → "relation", "query", "search for a solution", "what not how".

**Comparison:** low-level = control; imperative = steps; OOP = objects; declarative = logic/relations.

# ⚡ Quick Reference Card

1. **Paradigm = style of programming**, not a specific language.
2. **Low-level** = direct hardware control, not portable.
3. **Imperative** = tell the computer **how**; loops and assignment.
4. **OOP** = objects with data + methods; four pillars: encapsulation, inheritance, polymorphism, abstraction.
5. **Declarative** = tell the computer **what**; facts/rules/queries; Prolog and SQL.
6. **"Information hiding" → OOP**; **"relation" → declarative**; **"processor" → low-level**; **"sequence" → imperative**.
7. **Procedural is a subset of imperative**, not a separate paradigm in the syllabus.
8. **One language can support several paradigms** — Python is a good example.
9. **Large systems are often multi-paradigm.**
10. **Choose by problem shape, performance, maintainability and portability.**
