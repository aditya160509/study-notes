"""
Chapter 26: File Processing & Exception Handling — Full Code Notes (9618 Paper 4)
Your runnable companion to the .md — every snippet here actually runs!

Run with:
    python3 chapter-26-file-processing-and-exception-handling-notes.py

All file paths use /tmp/ so no setup needed — demo files are created inline.
Sections mirror the .md: 1 Records → 2 Text/Serial → 3 Sequential/pickle → 4 Random/struct+seek
→ 5 Exceptions → 6 Pseudocode mapping demos → 7 Past-paper patterns → Quick reference

Tip: read the .md for the "why", run this .py for the "how it actually works" ✨
"""

import pickle
import struct
import os

# ============================================================
# 🧱 PART 1: RECORDS — TYPE … ENDTYPE → Python class
# ============================================================
# TL;DR — A record is one row of a table. In Python, you build it as a class.
print("=" * 60)
print("🧱 PART 1: RECORDS — YOUR OWN DATA TYPES")
print("=" * 60)
# In plain English: the exam says TYPE…ENDTYPE, you write class + __init__.
# Each field gets a sensible starting value (like filling in a blank form).

class CarRecord:
    """Worked Example 26.01 — your record type as a plain data container."""
    def __init__(self):
        self.VehicleID = ""              # STRING — key field (your ID card)
        self.Registration = ""           # STRING
        self.DateOfRegistration = None   # DATE (None = not known yet)
        self.EngineSize = 0              # INTEGER
        self.PurchasePrice = 0.00        # CURRENCY

# ✅ WHEN EXAM ASKS: "declare ThisCar : CarRecord" → ThisCar = CarRecord()
ThisCar = CarRecord()
ThisCar.EngineSize = 2500
ThisCar.VehicleID = "A001"
print(f"✅ CarRecord: VehicleID={ThisCar.VehicleID}, EngineSize={ThisCar.EngineSize}")
print("   → You just created one row (record) and filled in two fields!")

# Array of records — 100 independent objects
# ✅ WHEN EXAM ASKS: "array Car[1:100] of CarRecord" → list comprehension
Car = [CarRecord() for _ in range(100)]
Car[0].EngineSize = 2500
Car[99].PurchasePrice = 12000.00
print(f"✅ Array: {len(Car)} records ready; Car[0].EngineSize={Car[0].EngineSize}")
# 💡 Why not [CarRecord()] * 100? That copies ONE object 100 times — change one,
#    you change them all! Comprehension builds 100 *separate* records. Think
#    photocopying one ID vs. giving each person their own.

# Why public fields for records? Records are simple containers — the mark scheme
# expects ThisCar.EngineSize = 2500 (direct access). Private __fields are for
# OOP classes in Chapter 27, not for TYPE…ENDTYPE records.
print()

# ============================================================
# 📄 PART 2: TEXT FILES — SERIAL ACCESS + ALL OPEN MODES
# ============================================================
# TL;DR — Text files = one line at a time, in order. Like writing in a notebook.
print("=" * 60)
print("📄 PART 2: TEXT FILES — SERIAL ACCESS (your notebook)")
print("=" * 60)
# In plain English: text files store strings, one line at a time, in the order
# you wrote them. Binary files (pickle/struct) store whole records as bytes.

# --- 2a: WRITE (FOR WRITE) — creates or WIPES clean ---
f = open("/tmp/cars_ch26.txt", "w")      # OPENFILE FOR WRITE — "w" = wipe!
f.write("A001,BMW 320i\n")
f.write("A002,Toyota Corolla\n")
f.close()                                 # CLOSEFILE — don't forget!
print("✅ Wrote 2 lines with 'w' (wiped + wrote)")

# --- 2b: APPEND (FOR APPEND) — keeps content, adds at end ---
f = open("/tmp/cars_ch26.txt", "a")      # OPENFILE FOR APPEND — "a" = add on
f.write("A003,Honda Civic\n")
f.close()
print("✅ Appended 1 line with 'a' (kept old, added new)")

# --- 2c: READ (FOR READ) ---
f = open("/tmp/cars_ch26.txt", "r")      # OPENFILE FOR READ — "r" = read
print("📖 Reading serial text file (front to back, like a scroll):")
for line in f:
    print(f"  → {line.strip()}")
f.close()

# --- 2d: with statement — auto-close even if something crashes ---
# ✅ WHEN EXAM ASKS: "ensure file is always closed" → with
with open("/tmp/cars_ch26.txt", "a") as f:
    f.write("A004,Ford Focus\n")
print("✅ Appended A004 via 'with' (auto-closed — you didn't have to remember!)")

# --- 2e: Reading alternatives (all valid on Paper 4 — pick what fits) ---
with open("/tmp/cars_ch26.txt", "r") as f:
    all_text = f.read()                   # whole file as one string
print(f"📖 f.read() → {len(all_text)} chars in one go")
with open("/tmp/cars_ch26.txt", "r") as f:
    lines = f.readlines()                 # list of lines
print(f"📖 f.readlines() → {len(lines)} lines as a list")
with open("/tmp/cars_ch26.txt", "r") as f:
    first = f.readline()                  # first line only
print(f"📖 f.readline() → {first.strip()!r} (just the first line)")
# 💡 Why with? Because f.close() is easy to forget — with guarantees it happens.

# --- 2f: ALL OPEN MODES DEMO (r/w/a/r+/w+/rb/wb/ab/r+b/x) ---
print("\n--- 🗂️  All open modes demo (your cheat sheet in action) ---")
# w+ : write+read (creates/wipes, then readable)
with open("/tmp/mode_wplus.txt", "w+") as f:
    f.write("hello w+\n")
    f.seek(0)
    print(f"  w+ readback: {f.read().strip()}  ← wrote then read back")
# r+ : read+write on existing file (fails if missing)
with open("/tmp/mode_wplus.txt", "r+") as f:
    print(f"  r+ read: {f.read().strip()}  ← read existing content")
    f.write(" appended via r+\n")
# a : append text
with open("/tmp/mode_wplus.txt", "a") as f:
    f.write("appended via a\n")
# x : exclusive create (fails if exists — safe "create new only")
try:
    with open("/tmp/mode_wplus.txt", "x") as f:
        f.write("x mode")
except FileExistsError as e:
    print(f"  x mode correctly said 'already exists!': {e}")
# wb/rb/ab/r+b : binary modes (same ideas, but bytes)
with open("/tmp/mode_bin.dat", "wb") as f:
    f.write(b"binary hello\n")
with open("/tmp/mode_bin.dat", "rb") as f:
    print(f"  rb read: {f.read().strip()}  ← binary read")
with open("/tmp/mode_bin.dat", "ab") as f:
    f.write(b"appended binary\n")
with open("/tmp/mode_bin.dat", "r+b") as f:   # FOR RANDOM (existing file)
    f.seek(0)
    print(f"  r+b read: {f.readline().strip()}  ← random-access read")
    f.seek(0, 2)  # jump to end
    f.write(b"via r+b\n")
print("✅ All open modes verified — you're ready for any exam question!")
print()

# ============================================================
# 💾 PART 3: SEQUENTIAL BINARY FILES — pickle + EOFError loop
# ============================================================
# TL;DR — Your array lives in RAM → you dump it to a file → reload later.
#          Records sit in order. To find one, you scan from the start.
print("=" * 60)
print("💾 PART 3: SEQUENTIAL BINARY FILES (pickle + EOFError)")
print("=" * 60)
# In plain English: like stacking filing cards in order, putting them in a box
# (pickle), then pulling them out one by one until the box says "empty!"

# Fill array — your little database in RAM
Cars = [CarRecord() for _ in range(4)]
for i in range(4):
    Cars[i].VehicleID = f"SEQ{i}"
    Cars[i].Registration = f"REG{i}"
    Cars[i].EngineSize = 1000 * (i + 1)
    Cars[i].PurchasePrice = 15000.0 + i * 100

# --- SAVE: PUTRECORD loop ---
# ✅ WHEN EXAM ASKS: "save array to sequential binary file" → pickle.dump loop
CarFile = open("/tmp/CarFile_ch26.DAT", "wb")   # OPENFILE FOR WRITE (binary)
for rec in Cars:
    pickle.dump(rec, CarFile)                    # PUTRECORD — one card into the box
CarFile.close()                                  # CLOSEFILE
print(f"✅ Saved {len(Cars)} records to /tmp/CarFile_ch26.DAT (wb + pickle.dump)")

# --- RESTORE: GETRECORD until EOF ---
# ✅ WHEN EXAM ASKS: "read all records until EOF" → while True + pickle.load + EOFError
# Without the EOFError handler this loop crashes — that's the textbook warning on p.444!
Car2 = []
CarFile = open("/tmp/CarFile_ch26.DAT", "rb")    # OPENFILE FOR READ
try:
    while True:
        Car2.append(pickle.load(CarFile))         # GETRECORD — keep pulling cards
except EOFError:
    print("📦 EOF reached — all records restored! (EOFError = 'box is empty' signal)")
CarFile.close()
print(f"✅ Restored {len(Car2)} records; first: {Car2[0].VehicleID} engine={Car2[0].EngineSize}")

# --- Task 26.01 style: with + display ---
print("\n📋 Task 26.01 display (read + show each record):")
with open("/tmp/CarFile_ch26.DAT", "rb") as f:
    try:
        while True:
            rec = pickle.load(f)
            print(f"  → {rec.VehicleID}  engine={rec.EngineSize}  price={rec.PurchasePrice}")
    except EOFError:
        pass
# 💡 Why EOFError for flow-control? The textbook says it's OK — Python *designed*
#    it this way. Reaching the end isn't an error; it's how you know you're done!
print()

# ============================================================
# 🎲 PART 4: RANDOM-ACCESS (DIRECT ACCESS) — struct + seek + hash
# ============================================================
# TL;DR — Jump straight to the record you want. No scanning. Like a numbered parking lot.
print("=" * 60)
print("🎲 PART 4: RANDOM-ACCESS FILES (struct + seek + hash)")
print("=" * 60)
# In plain English: fixed-length records at calculated addresses → jump via seek.
# address = slot * RECORD_SIZE,  slot = Hash(key) = key % table_size
# Collision? Next free slot (linear probing) — like parking in the next bay.

FMT = "<6s8sid"                              # 6-char ID, 8-char Reg, int, double
RECORD_SIZE = struct.calcsize(FMT)           # 26 bytes per slot — every bay same size!
print(f"📐 Record size: {RECORD_SIZE} bytes; slot n starts at byte n*{RECORD_SIZE}")
print(f"   Formula: address = slot × RECORD_SIZE  (e.g. slot 2 → byte {2*RECORD_SIZE})")
print(f"   Hash:    slot = key % table_size  (like a cloakroom ticket 🎫)")

def Hash(key: str) -> int:
    """Your hash function — built-in hash() is randomised per run, never use it for files!"""
    return sum(ord(c) for c in key) % 4      # slots 0..3 (use %1000 for a 1000-slot file)

def save_record(f, rec):
    """SEEK to hashed address, then PUTRECORD (fixed-size — always 26 bytes!)."""
    slot = Hash(rec.VehicleID)
    f.seek(slot * RECORD_SIZE)               # SEEK CarFile, Address — jump to the bay!
    data = struct.pack(FMT,
        rec.VehicleID.encode(), rec.Registration.encode(),
        rec.EngineSize, rec.PurchasePrice)
    f.write(data)                            # PUTRECORD — park the record

def load_record(f, vehicle_id: str):
    """SEEK to hashed address, then GETRECORD (fixed-size)."""
    slot = Hash(vehicle_id)
    f.seek(slot * RECORD_SIZE)               # SEEK — jump straight there
    raw = f.read(RECORD_SIZE)                # GETRECORD — exactly one slot
    return struct.unpack(FMT, raw)

# Build 4 records, store each at its hashed slot (no scanning needed!)
Recs = [CarRecord() for _ in range(4)]
for i in range(4):
    Recs[i].VehicleID = f"CAR{i}"
    Recs[i].Registration = f"REG{i}"
    Recs[i].EngineSize = 1000 * (i + 1)
    Recs[i].PurchasePrice = 20000.0 + i

f = open("/tmp/CarRnd_ch26.DAT", "w+b")      # FOR RANDOM (create + read/write)
for r in Recs:
    print(f"  🎫 {r.VehicleID} → slot {Hash(r.VehicleID)} → byte {Hash(r.VehicleID)*RECORD_SIZE}")
for r in Recs:
    save_record(f, r)
    # Note: CAR0..CAR3 with sum%4 are spread; if collision occurs, last write wins — that's the pitfall we fix below!

# Direct access: find CAR2 without scanning — that's the magic! ✨
fields = load_record(f, "CAR2")
vid = fields[0].decode().rstrip("\x00").strip()
print(f"🎯 Direct access CAR2: id={vid} engine={fields[2]} price={fields[3]} — no scanning needed!")

# In-situ update: read → change → write back to same address
print("✏️  In-situ update: CAR2 price → 19999.99 (same slot, just overwritten)")
Recs[2].PurchasePrice = 19999.99
save_record(f, Recs[2])
fields = load_record(f, "CAR2")
print(f"  ✅ After update CAR2 price={fields[3]}")
f.close()

# --- Textbook pickle+seek variant (shows the variable-length pitfall) ---
print("\n📚 Pickle+seek variant (textbook demo — handy but not true fixed-length):")
ThisCar = CarRecord(); ThisCar.VehicleID = "CAR07"; ThisCar.EngineSize = 1800
addr = hash(ThisCar.VehicleID) % 100
with open("/tmp/RndPickle_ch26.DAT", "w+b") as pf:
    pf.seek(addr)
    pickle.dump(ThisCar, pf)
    pf.seek(addr)
    loaded = pickle.load(pf)
    print(f"  Stored CAR07 at addr {addr}, loaded back: {loaded.VehicleID} engine={loaded.EngineSize}")
print("  ⚠️  Note: pickle records are variable-length — for explain Qs say")
print("     'fixed-length + struct is needed for true random access' to grab that mark.")

# --- Linear probing for collisions (file-level) ---
print("\n🅿️  Linear probing demo (collision → next free slot, like parking):")
TABLE_SIZE = 8
FMT2 = "<10si"                               # 10-char key + int
RS2 = struct.calcsize(FMT2)
# Create empty table (zeroed — like an empty car park)
with open("/tmp/Probe_ch26.DAT", "w+b") as pf:
    pf.write(b"\x00" * (TABLE_SIZE * RS2))

def probe_save(f, key_str: str, val: int):
    """Save with linear probing — if bay taken, try the next one!"""
    slot = sum(ord(c) for c in key_str) % TABLE_SIZE
    start = slot
    while True:
        f.seek(slot * RS2)
        raw = f.read(RS2)
        is_empty = (raw == b"\x00" * RS2 or len(raw) < RS2 or raw[:10].rstrip(b"\x00") == b"")
        if is_empty or raw[:10].rstrip(b"\x00") == b"":
            f.seek(slot * RS2)
            if raw == b"\x00" * RS2:
                f.seek(slot * RS2)
                f.write(struct.pack(FMT2, key_str.encode(), val))
                return slot
            existing_key = raw[:10].rstrip(b"\x00").decode(errors="ignore")
            if existing_key == key_str:
                f.seek(slot * RS2)
                f.write(struct.pack(FMT2, key_str.encode(), val))
                return slot
            if is_empty:
                f.seek(slot * RS2)
                f.write(struct.pack(FMT2, key_str.encode(), val))
                return slot
        f.seek(slot * RS2)
        raw2 = f.read(RS2)
        key_part = raw2[:10].rstrip(b"\x00")
        if len(key_part) == 0:
            f.seek(slot * RS2)
            f.write(struct.pack(FMT2, key_str.encode(), val))
            return slot
        slot = (slot + 1) % TABLE_SIZE
        if slot == start:
            raise OverflowError("Hash table full — no bays left!")

def probe_load(f, key_str: str):
    """Load with linear probing — follow the same trail."""
    slot = sum(ord(c) for c in key_str) % TABLE_SIZE
    start = slot
    while True:
        f.seek(slot * RS2)
        raw = f.read(RS2)
        if raw == b"\x00" * RS2 or len(raw) < RS2:
            return None
        k = raw[:10].rstrip(b"\x00").decode(errors="ignore")
        v = struct.unpack(FMT2, raw)[1]
        if k == key_str:
            return (slot, v)
        slot = (slot + 1) % TABLE_SIZE
        if slot == start:
            return None

with open("/tmp/Probe_ch26.DAT", "r+b") as pf:
    # Force a collision: "AB" and "BA" have the same hash — same bay!
    s1 = probe_save(pf, "AB", 100)   # A=65 B=66 sum 131 %8 = 3
    s2 = probe_save(pf, "BA", 200)   # B=66 A=65 sum 131 %8 = 3 → collides → probes to 4
    print(f"  'AB' parked at slot {s1}, 'BA' (collision!) probed to slot {s2}")
    print(f"  Load AB: {probe_load(pf, 'AB')} ✅")
    print(f"  Load BA: {probe_load(pf, 'BA')} ✅")
print()

# ============================================================
# 🛡️ PART 5: EXCEPTION HANDLING
# ============================================================
# TL;DR — Exceptions are run-time surprises. Wrap risky code in try, handle in except, clean up in finally.
print("=" * 60)
print("🛡️ PART 5: EXCEPTION HANDLING (your safety net)")
print("=" * 60)
# In plain English: pothole (exception) → suspension (handler) → clean-up crew (finally).
# You can't prevent every pothole, but you can make sure the car doesn't crash. 🚗

# --- 5a: Worked Example 26.04 — safe integer input ---
print("--- 5a: Safe integer input (ValueError) — don't trust what users type! ---")
def read_integer(NumberString):
    """✅ WHEN EXAM ASKS: validate integer input → try int() + except ValueError"""
    try:                                    # TRY — the risky bit
        n = int(NumberString)
        return n
    except ValueError:                      # EXCEPT — only if it's not a number
        return "This was not an integer"

print(f"  read_integer('42')    → {read_integer('42')} ✅")
print(f"  read_integer('hello') → {read_integer('hello')} (caught, didn't crash!)")
# 💡 Why specific except ValueError? Bare except catches *everything* including
#    Ctrl+C and hides bugs. Being specific = showing you know *what* can go wrong.

# --- 5b: Multiple except blocks + except as e + else + finally ---
print("\n--- 5b: Multiple except + as e + else + finally (the full toolkit) ---")
def safe_divide(a, b):
    """✅ WHEN EXAM ASKS: handle different errors differently → multiple except"""
    try:
        return a / b
    except ZeroDivisionError as e:          # as e → peek at the error message
        print(f"    ZeroDivisionError: {e}")
        return "Cannot divide by zero"
    except TypeError as e:
        print(f"    TypeError: {e}")
        return "Both values must be numbers"
    except Exception as e:                  # general — MUST be last (the safety net)
        print(f"    Unexpected: {e}")
        return None

print(f"  safe_divide(10,2)   → {safe_divide(10, 2)} ✅")
print(f"  safe_divide(10,0)   → {safe_divide(10, 0)} (caught /0!)")
print(f"  safe_divide(10,'x') → {safe_divide(10, 'x')} (caught wrong type!)")

def read_first_line(filename):
    """✅ WHEN EXAM ASKS: always clean up + success path → else + finally"""
    f = None
    try:
        f = open(filename, "r")             # may raise OSError — risky!
        line = f.readline()
    except OSError as e:
        print(f"    Could not open {filename}: {e}")
        return None
    else:
        # runs ONLY if try succeeded (no exception) — your happy path 🎉
        return line.strip()
    finally:
        # runs ALWAYS — success or failure (your guaranteed tidy-up 🧹)
        if f is not None:
            f.close()
        print(f"    [finally] clean-up done for {filename}")

with open("/tmp/exists_ch26.txt", "w") as f:
    f.write("hello from exists_ch26.txt\n")
print(f"  read_first_line(exists) → {read_first_line('/tmp/exists_ch26.txt')!r} ✅")
print(f"  read_first_line(missing) → {read_first_line('/tmp/nope_ch26.txt')} (handled gracefully)")

# --- 5c: All syllabus exception types, provoked live + as e ---
print("\n--- 5c: Syllabus exception types (let's provoke each one!) ---")
try:
    int("abc")
except ValueError as e:
    print(f"  ValueError: {e}  ← int('abc') — wrong value")

try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"  ZeroDivisionError: {e}  ← 1/0 — can't divide by zero!")

try:
    import no_such_module_xyz  # type: ignore
except ImportError as e:
    print(f"  ImportError: {e}  ← module doesn't exist")

try:
    open("/tmp/not_here_ch26.txt", "r")
except OSError as e:                        # IOError is alias of OSError
    print(f"  OSError/IOError: {e}  ← file not found")
try:
    open("/tmp/not_here_ch26.txt", "r")
except IOError as e:                        # same — IOError == OSError in Python 3
    print(f"  IOError (alias): {e}  ← same error, different name")

# FileNotFoundError is a subclass of OSError — caught by except OSError too!
try:
    open("/tmp/not_here_ch26.txt", "r")
except FileNotFoundError as e:
    print(f"  FileNotFoundError (subclass of OSError): {e}")

try:
    arr = [1, 2, 3]
    _ = arr[10]
except IndexError as e:
    print(f"  IndexError (array out of bounds): {e}  ← arr[10] on a 3-item list")

# EOFError already shown in Part 3 pickle loop — that's the "box is empty" one
print("  EOFError: shown in Part 3 (pickle.load past end) ✅")

# KeyboardInterrupt — shown as handler (don't actually press Ctrl+C in demo!)
print("  KeyboardInterrupt: handler exists (try: … except KeyboardInterrupt:) — for Ctrl+C")

# --- 5d: Raising exceptions + re-raising ---
print("\n--- 5d: Raising exceptions (raise) — you throw the error! ---")
def set_age(age: int):
    """✅ WHEN EXAM ASKS: raise/throw an exception → raise"""
    if age < 0:
        raise ValueError("Age cannot be negative")  # pseudocode: THROW
    return age

try:
    set_age(-3)
except ValueError as e:
    print(f"  ✅ Caught raised ValueError: {e}")

# Custom raise with specific type
def check_file_size(size: int):
    if size > 1000:
        raise OverflowError("File too large")
    return size

try:
    check_file_size(9999)
except OverflowError as e:
    print(f"  ✅ Caught OverflowError: {e}")

# Re-raising: log then let the caller handle it too
print("  Re-raise demo (log locally, then pass it up):")
try:
    try:
        open("/tmp/missing_reraise.txt", "r")
    except OSError as e:
        print(f"    📝 Logged: {e}")
        raise                               # re-raise same exception to caller
except OSError as e:
    print(f"    📬 Caller caught re-raised: {e}")

# --- 5e: try/except/else/finally — full structure ---
print("\n--- 5e: Full try/except/else/finally structure (all four!) ---")
def full_structure_demo(val):
    try:
        n = int(val)
    except ValueError as e:
        print(f"  except ValueError: {e}  ← not a number")
        return None
    else:
        print(f"  else (no exception): parsed {n} ✅")
        return n
    finally:
        print(f"  finally (always runs) for val={val!r} 🧹")

full_structure_demo("42")
full_structure_demo("hello")

# --- 5f: Bad vs Good ---
print("\n--- 5f: Bad vs Good — hiding errors vs handling them ---")
# ❌ BAD: bare except + pass hides everything — you bury the problem!
print("  ❌ BAD pattern (bare except + pass) — don't do this:")
try:
    int("bad")
except:                                     # bare — catches everything, even Ctrl+C!
    pass                                    # silent — impossible to debug 🔇
print("     (error vanished silently — how do you debug that?)")

# ✅ GOOD: specific + as e + finally — clear, debuggable, exam-friendly!
print("  ✅ GOOD pattern (specific + as e + finally):")
try:
    int("bad")
except ValueError as e:
    print(f"    Handled ValueError: {e} — specific and clear!")
finally:
    print("    finally: clean-up done 🧹")

# --- 5g: with vs try/finally ---
print("\n--- 5g: with (auto-close) vs try/finally (manual close) ---")
# with — short, preferred for simple open/close (less to remember!)
with open("/tmp/with_demo.txt", "w") as f:
    f.write("hello via with\n")
print("  ✅ with: auto-closed — neat and tidy!")
# try/finally — when you need to inspect the exception AND clean up
f = None
try:
    f = open("/tmp/with_demo.txt", "r")
    data = f.read()
    print(f"  try/finally read: {data.strip()} ✅")
except OSError as e:
    print(f"  OSError: {e}")
finally:
    if f is not None:
        f.close()
    print("  finally: closed 🧹")
print()

# ============================================================
# 🔄 PART 6: PSEUDOCODE ↔ PYTHON MAPPING DEMOS
# ============================================================
# TL;DR — One table, every translation. Nail this and you nail Paper 4.
print("=" * 60)
print("🔄 PART 6: PSEUDOCODE ↔ PYTHON MAPPING (your Rosetta Stone)")
print("=" * 60)

# TYPE → class
class DemoRecord:
    def __init__(self):
        self.ID = 0; self.Name = ""
r = DemoRecord()
print(f"✅ TYPE→class: DemoRecord().ID={r.ID}  ← TYPE DemoRecord … ENDTYPE")

# OPENFILE/CLOSEFILE/PUTRECORD/GETRECORD/SEEK/EOF via pickle
with open("/tmp/mapping_demo.DAT", "wb") as f:
    pickle.dump(r, f)                       # PUTRECORD
print("✅ PUTRECORD → pickle.dump ✓  ← PUTRECORD f, rec")
with open("/tmp/mapping_demo.DAT", "rb") as f:
    r2 = pickle.load(f)                     # GETRECORD
    print(f"✅ GETRECORD → pickle.load: ID={r2.ID}  ← GETRECORD f, rec")
    # EOF → EOFError
    try:
        pickle.load(f)
    except EOFError:
        print("✅ EOF(f) → except EOFError ✓  ← EOF is an exception in Python!")

# SEEK via struct
with open("/tmp/mapping_seek.DAT", "w+b") as f:
    fmt = "<10si"; rs = struct.calcsize(fmt)
    f.write(struct.pack(fmt, b"HELLO", 42))
    f.seek(0)                               # SEEK — jump to byte 0
    print(f"✅ SEEK → f.seek(0) ✓, read: {struct.unpack(fmt, f.read(rs))}  ← SEEK f, addr")

# TRY/EXCEPT/ELSE/FINALLY/RAISE
try:
    raise ValueError("demo raise")          # RAISE — you throw it!
except ValueError:
    print("✅ TRY/EXCEPT/RAISE ✓  ← TRY…EXCEPT…ENDTRY / RAISE")
else:
    print("ELSE not reached")
finally:
    print("✅ FINALLY ✓  ← always runs, no matter what")
print()

# ============================================================
# 📝 PART 7: PAST-PAPER PATTERNS — FULLY WORKED
# ============================================================
# TL;DR — The exact shapes of questions that keep coming back. Learn the pattern, swap the names.
print("=" * 60)
print("📝 PART 7: PAST-PAPER PATTERNS (the greatest hits, 2021–2025)")
print("=" * 60)

# ---- Pattern 1+2: Declare record + array ----
print("--- Pattern 1: Declare CustomerRecord (9618_s23_qp42 Q3a) ---")
class CustomerRecord:
    """✅ WHEN EXAM ASKS: declare record type → class with constructor, all fields"""
    def __init__(self):
        self.CustomerID = 100001             # key 100001-999999
        self.Name = ""                      # 30-char STRING
        self.Telephone = ""                 # 14-char STRING
        self.TotalOrders = 0.00             # CURRENCY

print("  ✅ CustomerRecord fields: CustomerID, Name, Telephone, TotalOrders")
print("     (every field must appear — miss one, lose a mark!)")

print("--- Pattern 2: Array CustomerData[0:999] ---")
CustomerData = [None] * 1000                # None = empty slot (for hash table)
print(f"  ✅ CustomerData size: {len(CustomerData)} (indices 0..999) — your hash table!")

# ---- Pattern 3: Hash ----
print("\n--- Pattern 3: Hash(CustomerID) = MOD 1000 ---")
def HashCustomer(CustomerID: int) -> int:
    """✅ WHEN EXAM ASKS: Hash = CustomerID MOD 1000 → % operator"""
    return CustomerID % 1000
print(f"  ✅ Hash(100001)={HashCustomer(100001)}, Hash(999999)={HashCustomer(999999)}")
print(f"     Formula: slot = CustomerID % 1000  (your cloakroom ticket 🎫)")

# ---- Pattern 4: AddRecord with linear probing ----
print("\n--- Pattern 4: AddRecord with collision (next free slot) ---")
def AddRecord(Customer):
    """✅ WHEN EXAM ASKS: add record, collision → next free slot → linear probing"""
    addr = HashCustomer(Customer.CustomerID)
    while CustomerData[addr] is not None:
        addr = (addr + 1) % 1000            # wrap-around — like next parking bay 🅿️
    CustomerData[addr] = Customer

c1 = CustomerRecord(); c1.CustomerID = 100001; c1.Name = "Ada"
c2 = CustomerRecord(); c2.CustomerID = 500001; c2.Name = "Grace"
c3 = CustomerRecord(); c3.CustomerID = 101001; c3.Name = "Linus"  # 101001%1000=1, 100001%1000=1 → collision!
AddRecord(c1); AddRecord(c2); AddRecord(c3)
print(f"  ✅ Added 3 records; Hash(100001)={HashCustomer(100001)}, Hash(101001)={HashCustomer(101001)} (collision → probed!)")
for i in range(5):
    entry = CustomerData[i]
    if entry is not None:
        print(f"    slot {i}: {entry.Name} (ID {entry.CustomerID})")  # type: ignore

# ---- Pattern 5: FindRecord ----
print("\n--- Pattern 5: FindRecord → index or -1 ---")
def FindRecord(CustomerID: int) -> int:
    """✅ WHEN EXAM ASKS: find record by key, return index or -1 → probing search"""
    addr = HashCustomer(CustomerID)
    entry = CustomerData[addr]
    while entry is not None:  # type: ignore
        if entry.CustomerID == CustomerID:  # type: ignore
            return addr
        addr = (addr + 1) % 1000
        entry = CustomerData[addr]
    return -1                               # not found → -1 (sentinel)

print(f"  ✅ FindRecord(101001) → slot {FindRecord(101001)} (Linus) — found!")
print(f"  ✅ FindRecord(999999) → {FindRecord(999999)} (not found → -1)")

# ---- Pattern 6: Sequential binary file ----
print("\n--- Pattern 6: Store array in CustomerData.DAT (sequential) ---")
with open("/tmp/CustomerData_ch26.DAT", "wb") as f:
    for i in range(1000):
        if CustomerData[i] is not None:
            pickle.dump(CustomerData[i], f)  # PUTRECORD — one card at a time
print(f"  ✅ Written to /tmp/CustomerData_ch26.DAT (wb + pickle.dump per occupied slot)")
restored = []
with open("/tmp/CustomerData_ch26.DAT", "rb") as f:
    try:
        while True:
            restored.append(pickle.load(f))
    except EOFError:
        print("  📦 EOF — all records restored (the box is empty!) ✅")
print(f"  ✅ Restored {len(restored)} records")

# ---- Pattern 7: Direct-access explain (no code, just print the 6 points) ----
print("\n--- Pattern 7: What changes for direct-access? (6-mark explain) ---")
for pt in [
    "1. Fixed-length records (pad Name to 30, Telephone to 14)",
    "2. Hash on key: slot=ID%1000, offset=slot*RECORD_SIZE",
    "3. SEEK before every PUTRECORD/GETRECORD",
    "4. In-situ update (read→change→write same address)",
    "5. Collisions → next free slot (linear probing)",
    "6. No 1000-array needed in RAM — go straight to disk slot!",
]:
    print(f"  {pt}")
print("  ✅ 6 points for 6 marks — memorise this list!")

# ---- Pattern 8: Missing-file exception (5 marks) ----
print("\n--- Pattern 8: Missing file — OPENFILE FOR RANDOM with handling ---")
def open_user_file(FileName: str):
    """✅ WHEN EXAM ASKS: handle missing file — try open + except OSError"""
    try:
        f = open(FileName, "r+b")           # FOR RANDOM
        return f
    except OSError:                         # IOError / FileNotFoundError
        print("  That file does not exist — handled, not crashed! ✅")
        return None

result = open_user_file("/tmp/nope_ch26_missing.txt")
print(f"  open_user_file(missing) → {result} (None, not crash)")
with open("/tmp/exists_ch26_b.txt", "w") as f:
    f.write("exists")
f2 = open_user_file("/tmp/exists_ch26_b.txt")
print(f"  open_user_file(exists) → {f2} (opened!) ✅")
if f2: f2.close()

# ---- Pattern 9: ReadData with exception handling ----
print("\n--- Pattern 9: ReadData() + missing-file handling (9618_w23_qp42 Q1bii) ---")
def PushData(letter):                       # given — push onto stack
    _stack.append(letter)  # type: ignore
_stack: list = []  # stack storage
PushData.stack = _stack  # type: ignore

def ReadData():
    """✅ WHEN EXAM ASKS: ReadData with exception handling for missing file"""
    try:
        with open("/tmp/letters_ch26.txt", "r") as f:
            for line in f:
                for ch in line.strip():
                    if ch.isalpha():
                        PushData(ch)
    except FileNotFoundError:
        print("  File not found — check letters_ch26.txt exists")
    except OSError as e:
        print(f"  Could not read file: {e}")

with open("/tmp/letters_ch26.txt", "w") as f:
    f.write("Ab1Cd\nEf2\n")
ReadData()
print(f"  ✅ ReadData pushed: {_stack} (only letters, numbers skipped!)")
os.remove("/tmp/letters_ch26.txt")
_stack.clear()  # type: ignore
ReadData()  # should print File not found, not crash
print(f"  ✅ Missing file handled, stack still: {_stack} (didn't crash!)")

# ---- Pattern 10: Validate integer input loop ----
print("\n--- Pattern 10: Validate integer input (loop + ValueError) ---")
def demo_read_int(inputs):
    """Simulates input() with a list — the loop + try pattern you need."""
    idx = 0
    while True:
        s = inputs[idx]; idx += 1
        try:
            n = int(s)
            print(f"  input {s!r} → parsed {n} ✅")
            return n
        except ValueError:
            print(f"  input {s!r} → 'This was not an integer — try again' (caught!)")

demo_read_int(["hello", "3.14", "42"])

# ---- Pattern 11: Serial vs Sequential vs Random (explain) ----
print("\n--- Pattern 11: Serial vs Sequential vs Random (explain) ---")
print("  Serial:     arrival order, unsorted, append-only, scan from start 📜")
print("  Sequential: key order (sorted), still scanned from start 📑")
print("  Random:     fixed-length, hash→slot→seek, direct access, instant 🎯")
print("  ✅ Advantage random>serial: no scanning — SEEK straight to slot!")

# ---- Pattern 12: EOF handling explain ----
print("\n--- Pattern 12: Why restore needs exception handling ---")
print("  pickle.load past last record raises EOFError; without try/except the")
print("  program crashes at the end. Python uses EOFError as flow-control —")
print("  the exception IS the end-of-file signal (pseudocode EOF(f) → except EOFError:) ✅")

# Also demonstrate raising in exam context
print("\n--- Bonus: Raising in validation (when exam says THROW) ---")
def validate_customer(c):
    if not (100001 <= c.CustomerID <= 999999):
        raise ValueError(f"CustomerID {c.CustomerID} out of range 100001-999999")
    return True

bad = CustomerRecord(); bad.CustomerID = 999
try:
    validate_customer(bad)
except ValueError as e:
    print(f"  ✅ validate raised: {e}")
print()

# ============================================================
# 📚 QUICK REFERENCE
# ============================================================
print("=" * 60)
print("📚 QUICK REFERENCE — one line each (your revision cards)")
print("=" * 60)
quick_ref = [
    ("Record", "your own type bundling related fields — one row"),
    ("Key field", "uniquely identifies a record — the ID card"),
    ("Serial file", "arrival order, unsorted — a scroll 📜"),
    ("Sequential file", "key order (sorted), scanned from start 📑"),
    ("Random file", "fixed-length, hash→slot→seek, direct access 🎯"),
    ("Binary file", "whole records as bytes (pickle/struct)"),
    ("PUTRECORD/GETRECORD", "pickle.dump / pickle.load (or struct pack/unpack)"),
    ("SEEK", "f.seek(slot * RECORD_SIZE) — jump to the bay!"),
    ("EOF", "except EOFError:  (pseudocode EOF(f))"),
    ("Hash", "slot = key % table_size,  offset = slot * RECORD_SIZE"),
    ("Collision", "two keys→same slot → next free slot (linear probing) 🅿️"),
    ("Exception", "a run-time surprise — the pothole"),
    ("try/except/else/finally", "try risky / handle / success path / always clean up"),
    ("raise", "throw an exception: raise ValueError('…')"),
    ("IOError/OSError", "file cannot be opened (FileNotFoundError is a subtype)"),
    ("ValueError", "wrong value: int('abc')"),
    ("ZeroDivisionError", "division by zero — // 0"),
    ("EOFError", "past end of file (pickle.load says 'box empty!')"),
    ("ImportError", "module not found"),
    ("with open", "auto-close — your tidy friend, preferred over manual close 🧹"),
]
for term, meaning in quick_ref:
    print(f"  {term:<22} → {meaning}")

print()
print("=" * 60)
print("🎉 ALL DONE — every pattern ran without external files!")
print("   You've seen every file + exception trick the exam can throw at you.")
print("   Re-run anytime: python3 chapter-26-file-processing-and-exception-handling-notes.py")
print("=" * 60)
