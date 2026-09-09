# Chapter 26: File Processing & Exception Handling — Code-First Notes (9618 Paper 4)

> Every pattern you need to **pass Paper 4 file questions** — without the dry textbook voice. You'll go from theory → exact code to write → which exam question it solves. Everything runs as Python, and maps 1-to-1 to pseudocode.

---

## 🎯 0 · Overview & Learning Objectives

> **TL;DR** — Files save your data forever; exceptions stop your program from crashing when things go wrong. The exam loves asking them *together*.

**Why do you need files?** Data in RAM disappears when your program ends. Files make it *persistent* — so it survives after you close the program.

**Why do you need exceptions?** Real life is messy. A file goes missing. A user types "hello" when you asked for a number. Without handling, your program crashes. With handling, it recovers gracefully.

> 💡 **In plain English:** Think of files as your notebook (keeps what you wrote) and exceptions as your safety net (catches you when you trip).

**Syllabus 9618 §20.2 — what you must be able to do:**

| # | Skill | You'll be asked to… |
|---|-------|---------------------|
| 1 | **Open** a file (READ / WRITE / APPEND / RANDOM) | *write program code* |
| 2 | **Read** a record (`GETRECORD`) | *write program code* |
| 3 | **Write** a record (`PUTRECORD`) | *write program code* |
| 4 | Do 1–3 on **serial, sequential, *and* random** files | *explain / compare* |
| 5 | Explain what an **exception** is and why you handle it | *explain / state* |
| 6 | Know **when** to use exception handling | *explain / select* |
| 7 | Write code with **TRY / EXCEPT / ENDTRY / FINALLY** | *write program code* |

> 🎯 **Why this matters:** The textbook *deliberately* makes file code crash at the end of a file — so you *need* exception handling to fix it. Expect combo questions that test both at once.

---

## 🧱 1 · Records — `TYPE … ENDTYPE` → Python `class`

> **TL;DR** — A record is one row of a table. In Python, you write it as a `class` with fields inside `__init__`.

### 1.1 What is a record?

A **record** bundles related **fields** into one tidy package. One record = one row.

| Term | What it means | Picture it as… |
|------|---------------|----------------|
| **Record** | Your own type made of fields | One row in a spreadsheet |
| **Field** | One named piece inside a record | One column |
| **Key field** | Uniquely identifies the record | An ID card — no duplicates |
| **Array of records** | Many records of the same type | The whole table |

### 1.2 Worked Example 26.01 — CarRecord

**Pseudocode (what the exam prints on the paper):**

```
TYPE CarRecord
    DECLARE VehicleID            : STRING    // key field
    DECLARE Registration         : STRING
    DECLARE DateOfRegistration   : DATE
    DECLARE EngineSize           : INTEGER
    DECLARE PurchasePrice        : CURRENCY
ENDTYPE
DECLARE ThisCar : CarRecord
```

**Python (what *you* write on Paper 4):**

```python
# ✅ WHEN EXAM ASKS: "declare the record type CarRecord" → write this class
class CarRecord:                          # TYPE CarRecord
    def __init__(self):                   # constructor — sets starting values
        self.VehicleID = ""               # STRING — key field
        self.Registration = ""            # STRING
        self.DateOfRegistration = None    # DATE (None = not known yet)
        self.EngineSize = 0               # INTEGER
        self.PurchasePrice = 0.00         # CURRENCY (float on Paper 4)

ThisCar = CarRecord()                     # DECLARE ThisCar : CarRecord
ThisCar.EngineSize = 2500                 # ThisCar.EngineSize <- 2500
print(ThisCar.EngineSize)                 # 2500
```

> **📌 Exam callout — "When exam asks X, write Y":**
> - *Define TYPE … ENDTYPE* → `class Name:` + `def __init__(self):` + `self.Field = default`
> - *`DECLARE X : CarRecord`* → `X = CarRecord()`
> - *`X.Field <- value`* → `X.Field = value`
> - ⚠️ Trap: don't write `self.__VehicleID` (private) for a *record* — records are simple containers with public fields. Save `__private` for OOP classes (Chapter 27).

**In plain English:** `class` creates the blueprint. `__init__` runs when you build one. Each `self.X =` gives a field its starting value. `ThisCar.Field` reads or writes that field — just add a dot.

### 1.3 Array of records

Pseudocode: `DECLARE Car : ARRAY[1:100] OF CarRecord`

```python
# ✅ WHEN EXAM ASKS: "declare array Car[1:100] of CarRecord" → write this
Car = [CarRecord() for _ in range(100)]   # 100 independent records
Car[0].EngineSize = 2500                  # Python is 0-based; Car[1] in pseudocode = Car[0] here
Car[99].PurchasePrice = 12000.00

# ❌ WRONG: [CarRecord()] * 100  — copies the SAME object 100 times!
# Common mistake → Fix: always use a comprehension so each slot is its own object.
```

> 💡 **In plain English:** `[CarRecord()] * 100` is like photocopying one person's ID 100 times — change one, you change them all. The comprehension builds 100 *separate* people.

---

## 📄 2 · Text Files — Serial Access

> **TL;DR** — Text files store one line at a time, in the order you wrote them. Simple. Great for logs. But you can't store a whole record as one chunk.

Text files store **strings only**, one line at a time, **serially** (append-only). You read them front-to-back, like a scroll.

### 2.1 All open modes — know every one

Your examiner can ask about *any* of these. Here's your cheat sheet:

| Pseudocode | Python | If file is missing? | If file already exists? |
|------------|--------|---------------------|-------------------------|
| `OPENFILE f FOR WRITE` | `open(f, "w")` | creates it | **wipes it clean** ⚠️ |
| `OPENFILE f FOR APPEND` | `open(f, "a")` | creates it | keeps content, adds to end |
| `OPENFILE f FOR READ` | `open(f, "r")` | ❌ `FileNotFoundError` | reads it |
| `OPENFILE f FOR RANDOM` | `open(f, "r+b")` or `"w+b"` | `r+b` fails; `w+b` creates+wipes | read+write without wiping (`r+b`) |
| — | `open(f, "x")` | creates, fails if exists | ❌ `FileExistsError` |
| — | `open(f, "r+")` | fails if missing | text read+write |
| — | `open(f, "w+")` | creates/wipes | text read+write |
| binary variants | `"wb"`, `"rb"`, `"ab"`, `"r+b"` | same as above | same, but bytes |

> **📌 Exam callout:** If the question says *FOR RANDOM*, write `"r+b"` (file already exists) or `"w+b"` (new file). For binary records, always add `b`: `"wb"` / `"rb"` / `"r+b"`.

> 🎯 **Why this matters:** Mixing up `"w"` and `"r"` is the #1 way students accidentally wipe their file in the exam. When in doubt: `r` = read, `w` = wipe-and-write, `a` = append.

### 2.2 Serial text file — write / append / read

```python
# ✅ WHEN EXAM ASKS: "write records to a serial text file" → write this
f = open("/tmp/cars.txt", "w")            # OPENFILE FOR WRITE
f.write("A001,BMW 320i\n")               # one record per line
f.write("A002,Toyota Corolla\n")
f.close()                                 # CLOSEFILE — always close!

f = open("/tmp/cars.txt", "a")            # OPENFILE FOR APPEND
f.write("A003,Honda Civic\n")
f.close()

f = open("/tmp/cars.txt", "r")            # OPENFILE FOR READ
for line in f:                            # read one line at a time
    print(line.strip())                   # strip() removes \n
f.close()

# ✅ BETTER — with statement (auto-close, even if something crashes)
# WHEN EXAM ASKS: "ensure the file is always closed" → write with
with open("/tmp/cars.txt", "w") as f:     # auto CLOSEFILE at block end
    f.write("A004,Ford Focus\n")

# ✅ READING ALTERNATIVES — all valid on Paper 4, pick what fits
with open("/tmp/cars.txt", "r") as f:
    all_text = f.read()                   # whole file as one string
with open("/tmp/cars.txt", "r") as f:
    lines = f.readlines()                 # list of lines
with open("/tmp/cars.txt", "r") as f:
    first = f.readline()                  # just the first line
```

**Common mistake → Fix: forgetting to close**

```python
# ❌ Tempting but risky — may lose data, file stays locked if crash happens
f = open("/tmp/cars.txt", "w")
f.write("data")
# oops — forgot f.close()

# ✅ Friendly fix — with always closes, even if an exception happens inside
with open("/tmp/cars.txt", "w") as f:
    f.write("data")
# closed automatically — you don't have to remember!
```

---

## 💾 3 · Sequential Binary Files — `pickle` + `EOFError` Loop

> **TL;DR** — Your array lives in RAM → you dump it to a binary file before quitting → you reload it next time. Records sit in order. To find one, you scan from the start.

**The idea in plain English:** Imagine lining up filing cards in order. You save the whole stack to a box (`pickle`). Next time, you pull them out one by one until the box is empty.

Binary files store whole records as bytes via `pickle` (it can save *any* Python object for you).

### 3.1 Worked Example 26.02 — Save & Restore

**Pseudocode (Table 26.02):**

```
OPENFILE CarFile FOR WRITE          OPENFILE CarFile FOR READ
FOR i <- 1 TO MaxRecords            FOR i <- 1 TO MaxRecords
    PUTRECORD CarFile, Car[i]           GETRECORD CarFile, Car[i]
NEXT i                              NEXT i
CLOSEFILE CarFile                   CLOSEFILE CarFile
```

**Python:**

```python
import pickle

# --- SAVE: array → file ---
# ✅ WHEN EXAM ASKS: "save array to sequential binary file" → this loop
Car = [CarRecord() for _ in range(100)]
CarFile = open("/tmp/CarFile.DAT", "wb")       # OPENFILE FOR WRITE (binary)
for i in range(100):
    pickle.dump(Car[i], CarFile)               # PUTRECORD
CarFile.close()                                # CLOSEFILE

# --- RESTORE: file → array (EOF-safe) ---
# ✅ WHEN EXAM ASKS: "read all records until end of file" → while True + EOFError
Car = []
CarFile = open("/tmp/CarFile.DAT", "rb")       # OPENFILE FOR READ
try:
    while True:
        Car.append(pickle.load(CarFile))       # GETRECORD until EOF
except EOFError:                               # EOF(CarFile) in pseudocode
    print("All records loaded")                # normal end — not an error!
CarFile.close()
```

> **📌 Exam callout:**
> - *`PUTRECORD f, rec`* → `pickle.dump(rec, f)`
> - *`GETRECORD f, rec`* → `rec = pickle.load(f)`
> - *`EOF(f)`* in pseudocode → `except EOFError:` in Python (yes, Python uses an exception to say "you're done" — the textbook on p. 445 says this is normal)
> - Without `try/except EOFError`, your `while True` loop **crashes** on the last read — the book warns about this on p. 444.

> 💡 **In plain English:** You don't know how many cards are in the box, so you just keep pulling until someone says "empty!" — that "empty!" is `EOFError`. Catching it isn't an error; it's how you know you're done.

**Why not `FOR i <- 1 TO 100` when restoring?** You may not know how many records are in the file! The `EOFError` loop handles any count. (Alternative accepted answer: store the count as the very first record.)

### 3.2 Task 26.01 — Complete runnable answer

```python
import pickle

class CarRecord:
    def __init__(self):
        self.VehicleID = ""; self.Registration = ""
        self.DateOfRegistration = None; self.EngineSize = 0; self.PurchasePrice = 0.00

Cars = [CarRecord() for _ in range(3)]
Cars[0].VehicleID = "A001"; Cars[0].EngineSize = 2500
Cars[1].VehicleID = "A002"; Cars[1].EngineSize = 1600
Cars[2].VehicleID = "A003"; Cars[2].EngineSize = 1800

# (1) SAVE
with open("/tmp/CarFile2.DAT", "wb") as f:
    for rec in Cars:
        pickle.dump(rec, f)

# (2) READ BACK + display
with open("/tmp/CarFile2.DAT", "rb") as f:
    try:
        while True:
            rec = pickle.load(f)
            print(rec.VehicleID, rec.EngineSize)
    except EOFError:
        pass
# Output:
# A001 2500
# A002 1600
# A003 1800
```

---

## 🎲 4 · Random-Access (Direct Access) Files — `struct` + `seek` + Hash

> **TL;DR** — Instead of scanning, you *jump* straight to the record you want — like going to a numbered parking bay. But every bay must be the same size, so you need fixed-length records.

**The idea:** Each record lives at a **calculated address**. No scanning. Just maths → `seek` → read/write.

Requires **fixed-length records** — every slot is the same number of bytes, so slot *n* always starts at the same place.

### 4.1 Address formula — your key to direct access

The textbook says: *"if the record size is 58 bytes, the 2nd slot starts at byte 59, the nth slot at $(n-1) \times 58 + 1$"* (1-based). In Python (0-based bytes), it's simpler:

$$address = slot \times record\_size$$

Slot 0 → byte 0, slot 1 → byte 58, slot 2 → byte 116. In code: `f.seek(slot * RECORD_SIZE)`.

**Your hash function maps a key → a slot:**

$$slot = Hash(key) = key \bmod table\_size$$

Example: $slot = CustomerID \bmod 1000$ gives slots 0–999. In Python: `slot = CustomerID % 1000`.

> 💡 **In plain English:** A hash function is like a cloakroom ticket — you hand in key 1001, you get back slot 1. Quick, predictable, no searching needed.

**Collisions?** Two keys land in the same slot → you store the second one in the **next free slot** (linear probing). Searching probes forward with wrap-around: `slot = (slot + 1) % table_size`.

### 4.2 Worked Example 26.03 — Pseudocode

```
OPENFILE CarFile FOR RANDOM          OPENFILE CarFile FOR RANDOM
Address <- Hash(ThisCar.VehicleID)   Address <- Hash(VehicleID)
SEEK CarFile, Address                SEEK CarFile, Address
PUTRECORD CarFile, ThisCar           GETRECORD CarFile, ThisCar
CLOSEFILE CarFile                    CLOSEFILE CarFile
```

> After `SEEK`, `PUTRECORD`/`GETRECORD` acts at that address and the pointer slides to the *next* record — a favourite "explain what happens" question.

### 4.3 Textbook Python version (pickle + hash + seek)

```python
import pickle
# ✅ WHEN EXAM ASKS: "save one record to random file at hashed address" → SEEK + PUTRECORD
ThisCar = CarRecord(); ThisCar.VehicleID = "CAR07"
Address = hash(ThisCar.VehicleID) % 100          # scale hash to table size

CarFile = open("/tmp/RndPickle.DAT", "w+b")      # FOR RANDOM (create)
CarFile.seek(Address)                            # SEEK
pickle.dump(ThisCar, CarFile)                    # PUTRECORD
CarFile.close()

# Retrieve
CarFile = open("/tmp/RndPickle.DAT", "rb")
CarFile.seek(Address)                            # SEEK
ThisCar = pickle.load(CarFile)                   # GETRECORD
CarFile.close()
```

> ⚠️ **Pitfall for explain questions:** `pickle` records are *variable length* (strings differ in size), so `seek` + `pickle` alone does NOT guarantee slot *n* starts where you expect. Real direct access needs **fixed-length** records (next section). Say this in a 6-mark "what changes for direct access?" answer — it's an easy mark.

### 4.4 Exam-ready version — Fixed-length with `struct` (genuine random access)

```python
import struct

# ✅ WHEN EXAM ASKS: "direct access / random file with fixed-length records" → struct + seek
FMT = "<6s8sid"                            # 6-char ID, 8-char Reg, int, double
RECORD_SIZE = struct.calcsize(FMT)         # 26 bytes — every record exactly this!

def Hash(key: str) -> int:
    # Custom hash — built-in hash() is randomised per run, so don't use it for files!
    return sum(ord(c) for c in key) % 4    # slots 0..3 (use % 1000 for a 1000-slot file)

def save_record(f, rec):
    slot = Hash(rec.VehicleID)
    f.seek(slot * RECORD_SIZE)             # SEEK CarFile, Address
    data = struct.pack(FMT,
        rec.VehicleID.encode(), rec.Registration.encode(),
        rec.EngineSize, rec.PurchasePrice)
    f.write(data)                          # PUTRECORD (fixed size — always 26 bytes!)

def load_record(f, vehicle_id: str):
    slot = Hash(vehicle_id)
    f.seek(slot * RECORD_SIZE)             # SEEK
    raw = f.read(RECORD_SIZE)              # GETRECORD — exactly one slot
    return struct.unpack(FMT, raw)         # tuple of 4 fields
```

**In plain English, line by line:** `"<6s8sid"` = little-endian, 6 bytes, 8 bytes, 4-byte int, 8-byte double. `calcsize` tells you the record size. `Hash` turns a key into a slot number. `seek(slot * RECORD_SIZE)` jumps to the right byte. `pack`/`unpack` convert between fields and bytes. Strip null padding with `.decode().rstrip("\x00")`.

### 4.5 Task 26.02 — Save several, find by key

```python
recs = [CarRecord() for _ in range(4)]
for i in range(4):
    recs[i].VehicleID = "CAR" + str(i)
    recs[i].Registration = "REG" + str(i)
    recs[i].EngineSize = 1000 * (i + 1)

f = open("/tmp/CarRnd.DAT", "w+b")
for r in recs:
    save_record(f, r)                      # each lands at its hashed slot

# Find CAR2 without scanning — that's the magic of direct access!
fields = load_record(f, "CAR2")
print(fields[0].decode().rstrip("\x00"), fields[2])  # CAR2 3000

# In-situ update: read → change → write back to same address
recs[2].PurchasePrice = 19999.99
save_record(f, recs[2])
print(load_record(f, "CAR2")[3])           # 19999.99
f.close()
```

### 4.6 Collision handling — linear probing (file-level)

```python
# ✅ WHEN EXAM ASKS: "handle collisions — next free slot" → linear probing
TABLE_SIZE = 1000

def hash_slot(key: int) -> int:
    return key % TABLE_SIZE

def save_with_probing(f, rec, fmt, rec_size):
    slot = hash_slot(int(rec.VehicleID[3:]))  # demo: numeric part of ID
    start = slot
    while True:
        f.seek(slot * rec_size)
        raw = f.read(rec_size)
        is_empty = (raw == b"\x00" * rec_size or len(raw) < rec_size)
        if is_empty:
            f.seek(slot * rec_size)
            f.write(struct.pack(fmt, rec.VehicleID.encode(), rec.Registration.encode(),
                                rec.EngineSize, rec.PurchasePrice))
            return slot
        slot = (slot + 1) % TABLE_SIZE
        if slot == start:
            raise OverflowError("Hash table full")
```

> 💡 **In plain English:** Collision handling is like parking — if your bay is taken, you try the next one, then the next, wrapping around to the start if needed.

---

## 🛡️ 5 · Exception Handling

> **TL;DR** — Exceptions are run-time surprises. You wrap risky code in `try`, handle problems in `except`, and always clean up in `finally`.

### 5.1 What is an exception?

A **run-time error** that interrupts your program — file not found, `int("abc")`, `// 0`, `EOFError`.

| Term | What it means | Picture it as… |
|------|---------------|----------------|
| **Exception** | A run-time error | A pothole in the road |
| **Exception handler** | Code that deals with it | Your car's suspension |
| **Try block** | Code that might fail | The bumpy stretch |
| **Except block** | Runs only if things went wrong | The safety net |
| **Finally block** | Always runs, error or not | The clean-up crew — always shows up |

**Pseudocode structure (what the exam shows):**

```
TRY
    <statementsA>          // risky code — might fail
EXCEPT
    <statementsB>          // handler — only runs if it did fail
ENDTRY

// with finally:
TRY
    <statementsA>
EXCEPT
    <statementsB>
FINALLY
    <cleanup>              // always runs, no matter what
ENDTRY
```

In Python it's `try:` / `except` / `else:` / `finally:` — same idea as Java's `try/catch` and VB.NET's `Try...Catch...End Try`. Fun fact: Python *intentionally* uses exceptions for flow-control (`EOFError` to end file loops).

### 5.2 Exception types you must know (the syllabus list)

| Exception | When it pops up | You'll see it when… |
|-----------|----------------|---------------------|
| `IOError` / `OSError` | File can't be opened | `open("missing.txt","r")` — also `FileNotFoundError` |
| `ValueError` | Wrong value for the type | `int("abc")`, `float("hello")` |
| `ZeroDivisionError` | Division by zero | `x // 0`, `x / 0` |
| `EOFError` | Read past end of file | `pickle.load(f)` at EOF |
| `ImportError` | Module not found | `import no_such_module` |
| `KeyboardInterrupt` | User presses Ctrl+C | interrupt |
| `IndexError` | Array index out of bounds | `arr[999]` on a tiny array (= Java `ArrayIndexOutOfBoundsException`) |
| `FileNotFoundError` | File missing (subclass of `OSError`) | `open("nope.txt")` |

> Java friends: `IOException` → `IOError`/`OSError`, `ArithmeticException` → `ZeroDivisionError`, `ArrayIndexOutOfBoundsException` → `IndexError`.

### 5.3 Worked Example 26.04 — Safe integer input

```python
# ✅ WHEN EXAM ASKS: "validate integer input without crashing" → try int() + except ValueError
NumberString = input("Enter an integer: ")
try:
    n = int(NumberString)                  # risky: might not be a number!
    print(n)
except ValueError:                         # specific type — not bare except
    print("This was not an integer")
```

> **📌 Exam callout:** Always catch the **specific** type (`except ValueError:`), not bare `except:`. Bare `except:` also swallows `KeyboardInterrupt` and hides bugs — examiners take marks off for it.

> 🎯 **Why this matters:** Catching the *right* exception shows you understand *what* can go wrong — not just *that* something can go wrong.

### 5.4 Multiple except blocks + `as e` + `else` + `finally`

```python
# ✅ WHEN EXAM ASKS: "handle different errors differently" → multiple except
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:         # as e → you can inspect the message
        print(f"ZeroDivisionError: {e}")
        return "Cannot divide by zero"
    except TypeError as e:
        print(f"TypeError: {e}")
        return "Both values must be numbers"
    except Exception as e:                 # general — must be LAST
        print(f"Unexpected: {e}")
        return None

print(safe_divide(10, 2))     # 5.0
print(safe_divide(10, 0))     # Cannot divide by zero
print(safe_divide(10, "x"))   # Both values must be numbers
```

```python
# ✅ WHEN EXAM ASKS: "do something only if no error occurred" → else
# ✅ WHEN EXAM ASKS: "always close / clean up" → finally
def read_first_line(filename):
    f = None
    try:
        f = open(filename, "r")            # may raise OSError
        line = f.readline()
    except OSError as e:                   # file not found?
        print(f"Could not open {filename}: {e}")
        return None
    else:
        # runs ONLY if try succeeded (no exception) — your "happy path"
        return line.strip()
    finally:
        # runs ALWAYS — success or failure — your guaranteed clean-up
        if f is not None:
            f.close()
        print(f"[finally] clean-up done for {filename}")
```

**The order matters — think of it as a funnel:**

- Specific handlers first, general `except Exception:` last.
- `else` = "everything went fine" path.
- `finally` = guaranteed clean-up (the manual version of `with`).

> 💡 **In plain English:** `try` = "attempt this." `except` = "if *this* specific thing goes wrong, do *this*." `else` = "if nothing went wrong, celebrate." `finally` = "no matter what, tidy up."

### 5.5 Raising exceptions + `with` vs `finally`

```python
# ✅ WHEN EXAM ASKS: "raise / throw an exception" → raise
def set_age(age: int):
    if age < 0:
        raise ValueError("Age cannot be negative")  # pseudocode: THROW / RAISE
    return age

try:
    set_age(-3)
except ValueError as e:
    print(f"Caught: {e}")

# ✅ Re-raising — handle it, log it, then pass it up to your caller
try:
    f = open("/tmp/data.txt", "r")
    data = f.read()
except OSError as e:
    print(f"Log: file error {e}")
    raise                                  # re-raise the same exception to the caller
finally:
    try: f.close()
    except: pass

# ✅ with vs finally — both guarantee close, but with is shorter and friendlier
# Use with for simple open/close:
with open("/tmp/data.txt", "w") as f:
    f.write("hello")

# Use try/finally when you need to inspect the exception AND clean up:
f = None
try:
    f = open("/tmp/data.txt", "r")
    process(f)
except OSError as e:
    handle(e)
finally:
    if f: f.close()
```

> 🎯 **Which to use?** `with` for everyday file work (shorter, cleaner). `try/finally` when you also need to *handle* the error yourself.

### 5.6 Bad vs Good — hiding errors

```python
# ❌ BAD — swallows everything, impossible to debug. You hide the problem.
try:
    result = expensive_operation()
except:                                    # bare except — catches even Ctrl+C!
    pass                                   # silently disappears — where did it go?

# ✅ GOOD — specific, recoverable, with clean-up
try:
    result = expensive_operation()
except OSError:                            # only what you actually expect
    result = default_value()
except ValueError as e:
    print(f"Bad value: {e}")
    result = None
else:
    print("Success, using result")
finally:
    log_attempt()
```

> 💡 **Common mistake → Fix:** Bare `except:` feels safe but hides *everything* — including bugs you need to see. Be specific: `except ValueError:` tells the examiner (and future you) exactly what you planned for.

> **📌 When to use exception handling (exam "explain" question):**
> - ✅ User input that can be invalid (`int(input())`) — you can't trust what they type!
> - ✅ File operations that can fail (missing file, EOF, disk full)
> - ✅ External resources (network, device)
> - ❌ Don't replace ordinary logic (`if x == 0:` is clearer than `try: 1/x except:`)
> - Exception to the rule: `EOFError` as flow-control for `pickle.load` loops *is* endorsed by the textbook — that's the one time exceptions-as-logic is correct.

---

## 🔄 6 · Pseudocode ↔ Python Mapping (compact)

> **TL;DR** — One table to rule them all. If you can translate this table both ways, you can handle any Paper 4 question.

| Pseudocode | Python | Quick note |
|------------|--------|------------|
| `TYPE T … ENDTYPE` | `class T: def __init__(self): self.F = …` | record = class with only a constructor |
| `DECLARE X : T` | `X = T()` | instantiation |
| `OPENFILE f FOR WRITE` | `open(f, "w")` / `"wb"` | `w` wipes; add `b` for binary |
| `OPENFILE f FOR READ` | `open(f, "r")` / `"rb"` | fails if missing |
| `OPENFILE f FOR APPEND` | `open(f, "a")` / `"ab"` | keeps + appends |
| `OPENFILE f FOR RANDOM` | `open(f, "r+b")` / `"w+b"` | `r+b` = existing; `w+b` = create |
| `CLOSEFILE f` | `f.close()` or `with open(…) as f:` | `with` = auto-close |
| `PUTRECORD f, rec` | `pickle.dump(rec, f)` or `f.write(struct.pack(…))` | binary |
| `GETRECORD f, rec` | `rec = pickle.load(f)` or `struct.unpack(fmt, f.read(n))` | |
| `SEEK f, addr` | `f.seek(addr)` | `addr = slot * RECORD_SIZE` |
| `EOF(f)` | `except EOFError:` | Python EOF *is* an exception |
| `TRY … EXCEPT … ENDTRY` | `try: … except …:` | |
| `TRY … EXCEPT … FINALLY … ENDTRY` | `try: … except …: … finally:` | |
| `TRY … EXCEPT … ELSE … ENDTRY` | `try: … except …: … else:` | `else` = no-exception path |
| `RAISE / THROW` | `raise ValueError("…")` | |

---

## 📝 7 · Past-Paper Question Patterns (6–12 patterns, paraphrased)

> **TL;DR** — These are the *exact shapes* of questions that keep coming back (2021–2025). Learn the pattern, copy the skeleton, adapt the names.

Each pattern below is a *type* of question that recurs in 9618 Paper 4 (2021–2025). Source tags like `9618_s23_qp42` are the nearest real paper where the pattern appears; stems are paraphrased, not verbatim.

### Pattern 1 — Declare a record type (2–6 marks)
**Source:** `9618_s23_qp42 Q3(a)`, `9618_w22_qp42 Q1` — "Customer record: CustomerID (key, 100001–999999), Name (30 chars), Telephone (14 chars), TotalOrders (currency)."
**What examiners want:** class name, constructor, all four fields, correct types. In pseudocode: `TYPE CustomerRecord … ENDTYPE`.
**Skeleton:**
```python
# ✅ WHEN EXAM ASKS: "declare the record" → this
class CustomerRecord:
    def __init__(self):
        self.CustomerID = 100001    # key
        self.Name = ""              # STRING (30)
        self.Telephone = ""         # STRING (14)
        self.TotalOrders = 0.00     # CURRENCY
```
**Mark tip:** Every field must appear — miss one, lose a mark. The key field must be identified.

### Pattern 2 — Declare array of records (2 marks)
**Source:** `9618_s23_qp42 Q3(a)(ii)` — "Declare CustomerData[0:999] to hold 1000 customer records."
```python
# ✅ WHEN EXAM ASKS: "declare array[0:999] of CustomerRecord" → this
CustomerData = [None] * 1000                    # None = empty slot (for hash table)
# or, if immediately filling: [CustomerRecord() for _ in range(1000)]
```
**Mark tip:** `* 1000` is fine for `None`; never `[CustomerRecord()] * 1000` (that aliases one object — common mistake!).

### Pattern 3 — Hash function `MOD` (3 marks)
**Source:** `9618_s23_qp42 Q3(b)(i)` — "Address <- CustomerID MOD 1000"
```python
# ✅ WHEN EXAM ASKS: "implement Hash(CustomerID) = CustomerID MOD 1000" → this
def Hash(CustomerID: int) -> int:
    return CustomerID % 1000            # % is MOD in Python; 1000 = table size
```
**Formula:** $address = CustomerID \bmod 1000$. Returns 0–999. One line, three marks.
**Mark tip:** Function header + MOD + return. That's all they count.

### Pattern 4 — AddRecord with collision / linear probing (6–7 marks)
**Source:** `9618_s23_qp42 Q3(b)(ii)` — "Handle collisions by using the next available slot."
```python
# ✅ WHEN EXAM ASKS: "add record, collision → next free slot" → linear probing
def AddRecord(Customer):
    addr = Hash(Customer.CustomerID)
    while CustomerData[addr] is not None:       # slot occupied? keep looking
        addr = (addr + 1) % 1000               # wrap-around to start if needed
    CustomerData[addr] = Customer
```
**Mark tip:** They check for hashing, the `while` loop, wrap with `% 1000`, and that you store the *parameter* (not a global).

### Pattern 5 — FindRecord returning index or -1 (6–7 marks)
**Source:** `9618_s23_qp42 Q3(b)(iii)` — "FindRecord(CustomerID) returns index or -1 if not found."
```python
# ✅ WHEN EXAM ASKS: "find record by key, return index or -1" → probing search
def FindRecord(CustomerID: int) -> int:
    addr = Hash(CustomerID)
    while CustomerData[addr] is not None:
        if CustomerData[addr].CustomerID == CustomerID:
            return addr
        addr = (addr + 1) % 1000
    return -1
```
**Mark tip:** Same probing as AddRecord, but you compare the `.CustomerID` field. Sentinel `-1` when you hit `None` (empty slot).

### Pattern 6 — Store array in sequential binary file (5–6 marks)
**Source:** `9618_s23_qp42 Q3(c)`, `textbook Task 26.01` — "Store CustomerData in CustomerData.DAT"
```python
# ✅ WHEN EXAM ASKS: "save array to binary file CustomerData.DAT" → pickle loop
import pickle
with open("CustomerData.DAT", "wb") as f:       # FOR WRITE
    for i in range(1000):
        if CustomerData[i] is not None:
            pickle.dump(CustomerData[i], f)     # PUTRECORD
# Restore:
with open("CustomerData.DAT", "rb") as f:
    try:
        while True:
            rec = pickle.load(f)                # GETRECORD
            # AddRecord(rec) to rebuild table
    except EOFError:
        pass                                    # normal end — not an error!
```
**Mark tip:** Correct mode (`wb`/`rb`), loop over array, one `PUTRECORD` per occupied slot, `CLOSEFILE` (or `with`).

### Pattern 7 — What changes for direct-access file? (6 marks, explain)
**Source:** `9618_s23_qp42 Q3(d)`, `9618_w22_qp42 Q2` — "What changes if the file is direct-access / random?"
**Your 6-point answer (need all 6 for full marks):**
1. Records must be **fixed length** (pad Name to 30, Telephone to 14).
2. Use **hash** on key: $address = CustomerID \bmod 1000$, byte offset $= address \times record\_size$.
3. `SEEK` before every `PUTRECORD`/`GETRECORD` (`f.seek(addr * RECORD_SIZE)`).
4. Update **in situ** (read → change → write back to same address).
5. Handle **collisions** (next free slot / linear probing).
6. No need to hold the whole 1000-array in RAM; go straight to the disk slot.

### Pattern 8 — Missing-file exception handling (5 marks)
**Source:** `9618 textbook Q2 (p. 448)`, `9618_w23_qp42 Q1(b)(ii)` — `ReadData()` / `OPENFILE FileName FOR RANDOM` must not crash if file missing.
```python
# ✅ WHEN EXAM ASKS: "handle missing file without crashing" → try open + except OSError
FileName = input("Which file do you want to use? ")
try:
    f = open(FileName, "r+b")                   # FOR RANDOM
except OSError:                                 # IOError / FileNotFoundError
    print("That file does not exist")
else:
    print(f"File opened: {FileName}")
    # use f …
    f.close()
```
**Mark tip:** `try` around the `open`, specific `except OSError:` / `except IOError:`, a user-friendly message, and the program *continues*. Bare `except:` loses the specificity mark. `OSError` and `IOError` are interchangeable in modern Python (they're aliases).

### Pattern 9 — ReadData() with try/except for file not found (Paper 4 practical)
**Source:** `9618_w23_qp42 Q1(b)(ii)` — "Procedure ReadData() reads each letter and PushData() onto appropriate stack. Use exception handling if file does not exist."
```python
# ✅ WHEN EXAM ASKS: "ReadData with exception handling for missing file" → this
def PushData(letter): ...  # given

def ReadData():
    try:
        with open("data.txt", "r") as f:
            for line in f:
                for ch in line.strip():
                    if ch.isalpha():
                        PushData(ch)
    except FileNotFoundError:
        print("File not found — check data.txt exists")
    except OSError as e:
        print(f"Could not read file: {e}")
```
**Mark tip:** Practical paper — you must *actually handle* the missing file, not just leave a comment about it.

### Pattern 10 — Validate user input (ValueError + loop) (4–5 marks)
**Source:** `textbook Worked Example 26.04`, `9618_s22_qp42 Q2` — "User enters integer; handle non-integer without crashing."
```python
# ✅ WHEN EXAM ASKS: "validate integer input, keep asking until valid" → loop + try
def read_int(prompt="Enter an integer: "):
    while True:
        s = input(prompt)
        try:
            return int(s)
        except ValueError:
            print("This was not an integer — try again")
```
**Mark tip:** `try` *inside* the loop, `except ValueError:` (not bare), a friendly message, and the loop continues asking.

### Pattern 11 — Sequential vs serial vs random — explain/compare (2–4 marks)
**Source:** `9618_w22_qp42 Q2(a)`, `moshikur Paper 4 Random Files` — "Explain one advantage of random over serial" / "difference between serial and sequential"
**Model answers (pick the one that matches the question wording):**
- *Serial:* records in **arrival order**, unsorted. Fast to append — just tack it on the end. To find one, you scan from the start.
- *Sequential:* records in **key order** (sorted). Still scanned from the start, but now in order.
- *Random (direct):* records at **calculated addresses** (hash → slot → `seek`). Instant access to any record. Needs fixed-length records and a hash; handles collisions.

> Advantage of random over serial: direct access — `SEEK` to the slot without reading preceding records, so large files are fast for single-record lookups.

### Pattern 12 — EOF handling / why sequential restore needs exception handling (2–3 marks)
**Source:** `textbook p. 444 warning`, `9618_w23_qp42` — "Why does the restore loop need exception handling?"
**Model answer:** `pickle.load` past the last record raises `EOFError`. Without `try/except EOFError`, the program crashes at end-of-file. Python uses exception handling as flow-control here — the exception *is* the signal that all records have been read. Pseudocode `EOF(f)` maps to `except EOFError:`.

---

## ⚠️ 8 · Common Traps & Quick Reference

> **TL;DR** — These are the mistakes that quietly steal your marks. Check this table before you leave the exam hall.

### Traps that lose marks

| Trap | Why it trips you | Friendly fix |
|------|-----------------|-------------|
| `[CarRecord()] * 100` | 100 references to ONE object | `[CarRecord() for _ in range(100)]` |
| `open(f, "w")` to read | wipes the file! | `open(f, "r")` for read, `"r+b"` for random |
| `open(f, "r")` without try | crashes if missing | `try: open … except OSError:` |
| `except:` bare | swallows `KeyboardInterrupt`, no specificity mark | `except ValueError:` / `except OSError:` |
| `pickle` + `seek` for random | variable-length → wrong offsets | `struct` fixed-length for true random access |
| `hash(key)` built-in for files | randomised per run → slots move every time! | custom `sum(ord(c)…) % n` |
| Forgetting `CLOSEFILE` | data loss, file stays locked | `with open(…) as f:` |
| `hash = CustomerID % 1000` without function | loses function-header mark | `def Hash(CustomerID): return CustomerID % 1000` |

### Quick reference — one line each

| Term | One line to remember |
|------|---------------------|
| Record | Your own type bundling related fields |
| Key field | Uniquely identifies the record |
| Serial file | Arrival order, unsorted — just a scroll |
| Sequential file | Key order (sorted), still scanned from start |
| Random file | Fixed-length, hashed address, direct access via `SEEK` |
| Binary file | Whole records as bytes (`pickle` or `struct`) |
| `OPENFILE` / `CLOSEFILE` | Open / close a file |
| `PUTRECORD` / `GETRECORD` | Write / read one record |
| `SEEK` | Jump to `slot * RECORD_SIZE` |
| `EOF` | End of file → `except EOFError:` |
| `pickle.dump` / `load` | Write / read a whole record |
| Hash function | $slot = key \bmod table\_size$, offset $= slot \times record\_size$ |
| Fixed-length record | Constant slot size — required for random access |
| Collision | Two keys → same slot → next free slot |
| Exception | A run-time error |
| `try` / `except` / `else` / `finally` | Try risky code / handle error / success path / always clean up |
| `raise` | Throw an exception — `raise ValueError("…")` |
| `IOError` / `OSError` | File operation failed |
| `ValueError` | Wrong value (`int("abc")`) |
| `ZeroDivisionError` | `// 0` |
| `EOFError` | Past end of file |
| `ImportError` | Module not found |

**One-paragraph summary to lock it in:** Records are your own types — rows with fields. They live in files three ways: serially (arrival order), sequentially (key order, scanned), or randomly (fixed-length, hashed address, direct `SEEK`). `pickle` handles sequential binary files; `struct` handles true random-access files. Exception handling (`try`/`except`/`else`/`finally`, specific types, `raise`) stops run-time errors — missing files, bad input, `EOFError`, `// 0` — from crashing your program. Run the companion `.py` to see every pattern live — you've got this! 💪

> **Past-paper sources used (paraphrased):** `9618_s23_qp42 Q3` (CustomerRecord / Hash / AddRecord / FindRecord / sequential vs random), `9618_w23_qp42 Q1(b)(ii)` (ReadData + exception handling for missing file / Stack), `9618_w22_qp42`, `9618_s22_qp42` (file handling & validation variants), Cambridge pseudocode guide 2026 (OPENFILE / PUTRECORD / GETRECORD / SEEK / EOF / TRY…EXCEPT), textbook Chapter 26 worked examples 26.01–26.04 + Tasks 26.01–26.02, moshikur Paper 4 Random Files & Exception Handling pages.
