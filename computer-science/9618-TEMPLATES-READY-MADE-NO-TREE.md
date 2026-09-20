# 9618 Paper 4 — Ready-Made Templates (Ch26 + Ch27)

> Memorize these. Every recent paper is a remix of these templates.


## How to use

Read the `When exam says:` trigger, copy the `Ready-made code` block verbatim, rename identifiers to match the question (e.g. `Car` → `Bird`, `VehicleID` → `Code`), and keep the structure exactly — private `__` attributes, `# DECLARE` comments above `__init__`, `self` on every method, and `MOD`/`split` patterns shown. All blocks are runnable Python accepted on Paper 4 (Cambridge allows Python or pseudocode); pseudocode keywords are noted where the mark scheme expects them.

---

---

## PART 1: ALL DECLARATIONS — Every DECLARE Pattern

> **Why one place:** the exam always starts with "DECLARE ..." — get this part right and the rest copies cleanly. No f-strings, no `with`-statement file opens, just plain pseudocode-faithful Python.

### A1. Record declaration (TYPE…ENDTYPE)

- **When exam says:** `TYPE CarRecord ... ENDTYPE` / `DECLARE ThisCar : CarRecord`
- **Ready-made code:**
```python
# DECLARE CarRecord : TYPE with 5 fields
class CarRecord:
    # VehicleID : STRING  (key field)
    # Registration : STRING
    # DateOfRegistration : DATE
    # EngineSize : INTEGER
    # PurchasePrice : CURRENCY
    def __init__(self):
        self.VehicleID = ""            # STRING -> ""
        self.Registration = ""         # STRING -> ""
        self.DateOfRegistration = None # DATE -> None
        self.EngineSize = 0            # INTEGER -> 0
        self.PurchasePrice = 0.00      # CURRENCY -> 0.00

# DECLARE ThisCar : CarRecord
ThisCar = CarRecord()
ThisCar.EngineSize = 2500
ThisCar.VehicleID = "A001"

# DECLARE Car : ARRAY[1:100] OF CarRecord
Car = [CarRecord() for _ in range(100)]  # 100 independent objects
Car[0].EngineSize = 2500
# WRONG: [CarRecord()] * 100  (same object x100)
```
- **Remember:** Records use **public** fields (`self.VehicleID`), not `__private` — save `__` for OOP classes.

---

### A1b. Simple Variables + CONSTANTS (every base type)

- **When exam says:** `DECLARE Count : INTEGER` / `DECLARE Name : STRING` / `DECLARE Price : CURRENCY` / `CONSTANT Pi = 3.14`
- **Ready-made code:**
```python
# DECLARE Count : INTEGER -> 0
# DECLARE Name : STRING -> ""
# DECLARE Price : REAL -> 0.0
# DECLARE Cost : CURRENCY -> 0.00
# DECLARE Found : BOOLEAN -> False
# DECLARE Today : DATE -> None   (no date literal in Python; mark scheme accepts None)
Count = 0
Name = ""
Price = 0.0
Cost = 0.00
Found = False
Today = None          # DATE

# CONSTANT MaxSize = 100   (UPPER_CASE name, never reassigned)
MAXSIZE = 100
PI = 3.14
# Use the constant name exactly as given; do not reassign it later

# DECLARE with initial value on one line (exam shorthand)
Counter = 0           # DECLARE Counter : INTEGER <- 0
Total = 0.00          # DECLARE Total : CURRENCY <- 0.00
Flag = False          # DECLARE Flag : BOOLEAN <- FALSE
```
- **Remember:** Python has no `DECLARE` keyword — the `# DECLARE ...` comment above each line earns the declaration mark. `DATE` → `None`, `CURRENCY` → `0.00` (`float`), `BOOLEAN` → `False`/`True`.

### A1c. Arrays — 1D, 2D, Array of Records, Array of Objects, 2D Array of Objects

- **When exam says:** `DECLARE Scores : ARRAY[1:50] OF INTEGER` / `DECLARE Grid : ARRAY[1:10,1:10] OF STRING` / `DECLARE Students : ARRAY[1:30] OF StudentRecord` / `DECLARE Fleet : ARRAY[1:20] OF Car`
- **Ready-made code:**
```python
# 1D array of simple type (size 50, index 1..50 in pseudocode -> 0..49 in Python)
# DECLARE Scores : ARRAY[1:50] OF INTEGER
Scores = []
for i in range(50):
    Scores.append(0)
Scores[0] = 99            # Scores[1] in pseudocode

# 1D array with known values (exam sometimes gives initialiser)
Names = ["", "", "", "", ""]   # ARRAY[1:5] OF STRING  (manual for small n)
# or loop for large n:
Names = []
for i in range(5):
    Names.append("")

# 2D array (10 x 10)
# DECLARE Grid : ARRAY[1:10, 1:10] OF STRING
Grid = []
for i in range(10):
    row = []
    for j in range(10):
        row.append("")
    Grid.append(row)
Grid[0][0] = "X"          # Grid[1,1] in pseudocode

# Alternative 2D with numbers
Matrix = []
for i in range(5):
    Matrix.append([0]*4)  # 5 rows x 4 cols, filled with 0

# Array OF RECORDS (TYPE already defined)
# DECLARE Fleet : ARRAY[1:20] OF CarRecord
Fleet = [CarRecord() for _ in range(20)]
Fleet[0].VehicleID = "A001"

# Array OF OBJECTS (class already defined)
# DECLARE Fleet : ARRAY[1:20] OF Car
Fleet2 = []
for i in range(20):
    Fleet2.append(Car("V" + str(i), 1600))
# or: Fleet2 = [Car("V" + str(i), 1600) for i in range(20)]

# 2D Array OF OBJECTS (Board 10x10 — see also PART 1 §B9 declaration part)
# DECLARE Board : ARRAY[1:10, 1:10] OF BoardSquare   (record or object)
Board = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(BoardSquare())   # or BoardObject() depending on question name
    Board.append(row)
Board[0][0].SetOccupied(True)
```
- **Remember:** `ARRAY[1:N]` → `range(N)` and index `0..N-1` in Python (off-by-one is the classic trap). 2D → list of lists. Array of records/objects → comprehension `[Type() for _ in range(N)]` gives N *independent* objects.

### B13d. GLOBAL flat declarations (Stack + Queue — alternative to class, as papers use)

- **When exam says:** `GLOBAL Stack : ARRAY` / `GLOBAL TopOfStack : INTEGER` / `Use global variables` (papers 9618/41 style uses flat globals, not class)
- **Ready-made code:**
```python
# DECLARE Stack : ARRAY[0:29] OF INTEGER  (size 30)
# DECLARE TopOfStack : INTEGER
# DECLARE Queue : ARRAY[0:99] OF STRING   (size 100)
# DECLARE QueueHead, QueueTail, NumberItems : INTEGER

# GLOBAL declarations (Python: use global keyword inside procedures)
Stack = []
for i in range(30):
    Stack.append(0)
TopOfStack = -1

Queue = []
for i in range(100):
    Queue.append("")
QueueHead = -1
QueueTail = -1
NumberItems = 0

def PushGlobal(value):
    global TopOfStack
    if TopOfStack == 29:
        return False
    TopOfStack = TopOfStack + 1
    Stack[TopOfStack] = value
    return True

def PopGlobal():
    global TopOfStack
    if TopOfStack == -1:
        return -999
    value = Stack[TopOfStack]
    TopOfStack = TopOfStack - 1
    return value

def EnqueueGlobal(value):
    global QueueTail, QueueHead, NumberItems
    if NumberItems == 100:
        return False
    if NumberItems == 0:
        QueueHead = 0
    QueueTail = (QueueTail + 1) % 100
    Queue[QueueTail] = value
    NumberItems = NumberItems + 1
    return True

def DequeueGlobal():
    global QueueHead, QueueTail, NumberItems
    if NumberItems == 0:
        return ""
    value = Queue[QueueHead]
    QueueHead = (QueueHead + 1) % 100
    NumberItems = NumberItems - 1
    if NumberItems == 0:
        QueueHead = -1
        QueueTail = -1
    return value
```
- **Remember:** Paper 4 often uses `GLOBAL` flat arrays (not class). `TopOfStack=-1` empty, `30` full. Queue circular with `% size`, `Head=-1`/`Tail=-1` when empty, `NumberItems` counts.

---

> **Extension — GLOBAL HashTable (same flat style, add when question uses it):**
```python
# DECLARE HashTable : ARRAY[0:99, 0:9] OF STRING  (100 rows x 10 cols)
HashTable = []
for i in range(100):
    row = []
    for j in range(10):
        row.append("")
    HashTable.append(row)

for i in range(50):
    # use [-1, 0, -1] if data is INTEGER
FreePointer = 0                      # first free node index

# GLOBAL keyword inside procedures that modify them:
# def InsertHash(value):
#     global HashTable
# def AddNode(data):
```

---

## PART 2: FILE HANDLING — All File Types Together

> Text lines, CSV, pickle sequential, random `struct+seek`, hash-from-file, and exception-handled writes — same `open/close` shape every time. No `with`-statement (use `open` + `close()` explicitly).

### A2. Text file write / append / read (all open modes)

- **When exam says:** `OPENFILE ... FOR WRITE / READ / APPEND` / `CLOSEFILE` / `READFILE` / `WRITEFILE`
- **Ready-made code:**
```python
# OPENFILE CarFile FOR WRITE  -> "w" (creates or WIPES)
f = open("/tmp/cars.txt", "w")
f.write("A001,BMW 320i\n")
f.write("A002,Toyota Corolla\n")
f.close()  # CLOSEFILE
# OPENFILE CarFile FOR APPEND -> "a"
f = open("/tmp/cars.txt", "a")
f.write("A003,Honda Civic\n")

f.close()
# OPENFILE CarFile FOR READ -> "r"
f = open("/tmp/cars.txt", "r")
for line in f:
    print(line.strip())

f.close()
# Alternatives (all valid):
f = open("/tmp/cars.txt", "r")
all_text = f.read()        # whole file as one string
f.close()
f = open("/tmp/cars.txt", "r")
lines = f.readlines()      # list of lines
f.close()
f = open("/tmp/cars.txt", "r")
first = f.readline()       # one line
f.close()
```
- **Remember:** `w`=wipe, `a`=append, `r`=read, `with` auto-closes.

---

### A3. Text file -> objects: line-per-record (1 line = 1 record, comma/space split)

- **When exam says:** `Read text file into array of records` / `Each line contains ID,Name` / `SplitData` without inbuilt split
- **Ready-made code:**
```python
# FILE: each line is one record, fields separated by comma
class Student:
    def __init__(self, sid, name):
        self.ID = sid
        self.Name = name

Students = []
f = open("/tmp/students.txt", "r")
lines = f.read().splitlines()  # strip \n
for line in lines:
    if line.strip() == "":
        continue
    parts = line.split(",")    # e.g. "A001, Alice"
    # parts[0]=ID, parts[1]=Name  (strip spaces)
    Students.append(Student(parts[0].strip(), parts[1].strip()))

f.close()
# Manual SplitData without inbuilt split (9618/43/O/N/25 Q3 SplitData pattern)
def SplitData(data_string, delimiter):
    # Returns list of substrings split by delimiter without using .split()
    result = []
    current = ""
    for ch in data_string:
        if ch == delimiter:
            result.append(current)
            current = ""
        else:
            current = current + ch
    result.append(current)
    return result

# Usage: SplitData("A;B;C", ";") -> ["A","B","C"]
# For HashTable file ReadData: line = "123,John Smith,01234"
parts = SplitData("123,John Smith,01234", ",")
```

- **Remember:** `read().splitlines()` + `line.split(",")` for CSV lines; use manual `SplitData` loop when question says without inbuilt function.

---

### A4. Text file -> objects: grouped lines (i += 3 pattern, 3 lines per record)

- **When exam says:** `Each record occupies 3 lines: Name, X, Y` / `Characters.txt 10 characters` / `Trains data` grouped
- **Ready-made code:**
```python
class Character:
    # Name : STRING
    # XCoordinate : INTEGER
    # YCoordinate : INTEGER
    def __init__(self, name, x, y):
        self.Name = name
        self.XCoordinate = x
        self.YCoordinate = y

Characters = []
f = open("/tmp/Characters.txt", "r")
lines = f.read().splitlines()

f.close()
i = 0
while i + 2 < len(lines):
    name = lines[i]
    x = int(lines[i+1])
    y = int(lines[i+2])
    Characters.append(Character(name, x, y))
    i += 3  # next record starts 3 lines later

# Alternative FOR loop (equivalent):
# for i in range(0, len(lines), 3):
#     Characters.append(Character(lines[i], int(lines[i+1]), int(lines[i+2])))

# Record class with PUBLIC attrs pattern (9618/41/O/N/25 Record)
class Record:
    # ID : INTEGER
    # Name : STRING
    # Data : STRING
    def __init__(self, p_id, p_name, p_data):
        self.ID = p_id         # public - no __
        self.Name = p_name
        self.Data = p_data
# File -> Record grouped: every 3 lines = one Record

print("Loaded " + str(len(Characters)) + " records")
```
- **Remember:** Grouped files → `while i+2 < len(lines): ... i+=3`.

---

### A5. Text file -> objects: CSV with 2D containment target

- **When exam says:** `Board 10x10 2D array of BoardObject` / `Trains inside Station` / `HashTable ReadData`
- **Ready-made code:**
```python
class Train:
    # TrainID : STRING
    # Destination : STRING
    # Time : STRING
    def __init__(self, tid, dest, t):
        self.TrainID = tid
        self.Destination = dest
        self.Time = t

# File: each line "T01,London,08:30"
Trains = []
f = open("/tmp/trains.txt", "r")
for line in f:
    line = line.strip()
    if line == "":
        continue
    parts = line.split(",")
    tid = parts[0].strip()
    dest = parts[1].strip()
    t = parts[2].strip()
    Trains.append(Train(tid, dest, t))
f.close()
```
- **Remember:** CSV file → strip, split, construct object, append.

---

### A6. Sequential binary file: pickle save + EOFError load

- **When exam says:** `Sequential file` / `PUTRECORD` / `GETRECORD until EOF` / `DAT file`
- **Ready-made code:**
```python
import pickle

class CarRecord:
    def __init__(self):
        self.VehicleID = ""
        self.EngineSize = 0
        self.PurchasePrice = 0.00

# SAVE: PUTRECORD loop
Cars = [CarRecord() for _ in range(4)]
for i in range(4):
    Cars[i].VehicleID = "SEQ" + str(i)
    Cars[i].EngineSize = 1000*(i+1)

f = open("/tmp/CarFile.DAT", "wb")  # OPENFILE FOR WRITE (binary)
for rec in Cars:
    pickle.dump(rec, f)  # PUTRECORD

f.close()
# LOAD: GETRECORD until EOF  (needs EOFError)
Car2 = []
f = open("/tmp/CarFile.DAT", "rb")  # OPENFILE FOR READ
try:
    while True:
        Car2.append(pickle.load(f))  # GETRECORD
except EOFError:
    pass  # EOF = done, not an error
f.close()
print("Restored " + str(len(Car2)) + " records")

# Task pattern: display each record while reading
f = open("/tmp/CarFile.DAT", "rb")
try:
    while True:
        rec = pickle.load(f)
        print(rec.VehicleID, rec.EngineSize)
except EOFError:
    pass
f.close()
```
- **Remember:** Sequential binary → `pickle.dump` to write, `while True: pickle.load` + `except EOFError` to read.

---

### A7. Random-access file: struct + seek + hash (fixed-length)

- **When exam says:** `Random file` / `SEEK` / `HashAddress = key MOD tableSize` / `fixed-length records`
- **Ready-made code:**
```python
import struct

# Define fixed format: 6-char ID, 8-char Reg, int, double
FMT = "<6s8sid"
RECORD_SIZE = struct.calcsize(FMT)  # 26 bytes

def Hash(key):
    total = 0
    for c in key:
        total = total + ord(c)
    return total % 100  # MOD table size

class CarRecord:
    def __init__(self): self.VehicleID=""; self.Registration=""; self.EngineSize=0; self.PurchasePrice=0.00

def save_record(f, rec, slot):
    f.seek(slot * RECORD_SIZE)  # SEEK CarFile, Address
    data = struct.pack(FMT, rec.VehicleID.encode(), rec.Registration.encode(), rec.EngineSize, rec.PurchasePrice)
    f.write(data)  # PUTRECORD

def load_record(f, slot):
    f.seek(slot * RECORD_SIZE)  # SEEK
    raw = f.read(RECORD_SIZE)   # GETRECORD
    return struct.unpack(FMT, raw)

# Create random file (r+b needs file to exist; w+b creates)
f = open("/tmp/CarRnd.DAT", "w+b")
f.write(b"\x00" * (100 * RECORD_SIZE))  # initialise empty

f.close()
f = open("/tmp/CarRnd.DAT", "r+b")
rec = CarRecord(); rec.VehicleID="CAR07"; rec.EngineSize=1800
slot = Hash(rec.VehicleID)
save_record(f, rec, slot)
fields = load_record(f, slot)
print(fields[0].decode().strip("\x00"), fields[2])
f.close()
```
- **Remember:** Random → `struct.pack/unpack` + `seek(slot*SIZE)` + `Hash = key MOD N`.

---

### A8. Hash table 2D with collision (linear probing) — 9618/41/O/N/25 pattern

- **When exam says:** `HashTable[100][10]` / `Hash = key MOD 100` / `collision: next available space` / `InsertData` / `GetRecord`
- **Ready-made code:**
```python
# DECLARE HashTable : ARRAY[0:99, 0:9] OF STRING  (100 x 10)
# Use list of lists; "" = empty
HashTable = []
for i in range(100):
    row = []
    for j in range(10):
        row.append("")
    HashTable.append(row)

def Hash(key):
    # key is INTEGER (e.g. ID 123); if STRING key: total % 100
    return key % 100  # MOD 100

def InitialiseHashTable():
    global HashTable
    HashTable = []
for i in range(100):
    row = []
    for j in range(10):
        row.append("")
    HashTable.append(row)

def InsertData(key, data_string):
    # data_string e.g. "123,John,01234" — store whole line or record
    slot = Hash(key)
    for col in range(10):  # try 10 columns in that row
        if HashTable[slot][col] == "":
            HashTable[slot][col] = data_string
            return True  # inserted
    return False  # row full — collision overflow

def GetRecord(key):
    slot = Hash(key)
    for col in range(10):
        if HashTable[slot][col] == "":
            return ""  # not found (empty hit)
        # check if stored record matches key (first field before comma)
        stored_key = int(HashTable[slot][col].split(",")[0])
        if stored_key == key:
            return HashTable[slot][col]
    return ""  # not found after 10 probes

# File -> HashTable: ReadData from file, split by comma, insert
def ReadData(filename):
    try:
        f = open(filename, "r")
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")  # or SplitData(line, ",")
            key = int(parts[0])
            InsertData(key, line)
    except FileNotFoundError:
        print("File not found")

        f.close()
InitialiseHashTable()
InsertData(123, "123,Alice,555-0100")
InsertData(223, "223,Bob,555-0101")  # 223%100=23 collides if 123%100=23 etc.
print(GetRecord(123))
```
- **Remember:** Hash 2D → `MOD 100` for row, `for col in range(10)` for collision, `""` means empty.

---

### A9. Exception handling: try/except/else/finally + file errors

- **When exam says:** `Exception handling` / `TRY ... CATCH ... ENDTRY` / `File not found` / `invalid input` / `WriteAllToFile with exception`
- **Ready-made code:**
```python
# 1. Safe integer input (ValueError)
def read_integer(s):
    try:
        n = int(s)
        return n
    except ValueError:
        return "This was not an integer"

# 2. File open with OSError / FileNotFoundError
def read_first_line(filename):
    f = None
    try:
        f = open(filename, "r")
        line = f.readline()
    except FileNotFoundError as e:
        print("File not found: " + str(e))
        return None
    except OSError as e:
        print("OS error: " + str(e))
        return None
    else:
        return line.strip()  # only if no exception
    finally:
        if f is not None:
            f.close()
        f.close()
        # finally ALWAYS runs

# 3. WriteAllToFile with exception handling (9618/42/O/N/25 pattern)
def WriteAllToFile(filename, data_list):
    # data_list: list of objects; write each as CSV line
    try:
        f = open(filename, "w")
        for item in data_list:
            f.write(str(item.GetID()) + "," + str(item.GetName()) + "\n")
        f.close()
        return True
    except OSError as e:
        print("Error writing file: " + str(e))
        return False

# 4. Multiple except (order: specific -> general)
try:
    x = int("hello")
    y = 10 / 0
except ValueError as e:
    print("ValueError: " + str(e))
except ZeroDivisionError as e:
    print("ZeroDivisionError: " + str(e))
except Exception as e:  # general MUST be last
    print("Unexpected: " + str(e))

# 5. EOFError for pickle sequential read
import pickle
try:
    f = open("/tmp/data.DAT", "rb")
    while True:
        rec = pickle.load(f)
        print(rec)
except EOFError:
    pass
except FileNotFoundError:
    print("File not found")
    f.close()
```
- **Remember:** Specific `except` first, general `except Exception` last; `else` = no error path, `finally` = always.

---

### A10. File write with exception handling (WriteAllToFile complete)

- **When exam says:** `WriteAllToFile` / `save array to file with exception handling`
- **Ready-made code:**
```python
def WriteAllToFile(filename, records):
    # records: list of objects with getters
    try:
        f = open(filename, "w")
        for r in records:
            # adapt fields to question: e.g. str(r.GetName()) + "," + str(r.GetX()) + "," + str(r.GetY()) + "\n"
            f.write(str(r.VehicleID) + "," + str(r.EngineSize) + "," + str(r.PurchasePrice) + "\n")
        f.close()
        print("Written " + str(len(records)) + " records to " + str(filename))
        return True
    except OSError as e:
        print("Could not write to " + str(filename) + ": " + str(e))
        return False
    except Exception as e:
        print("Unexpected error: " + str(e))
        return False

# Called as: WriteAllToFile("/tmp/out.txt", Cars)
```
- **Remember:** `WriteAllToFile` → `try: open(w) + for loop + write + close()` / `except OSError`.

---

### B13e. Pickle sequential file: full save + load (both directions, exam-ready)

- **When exam says:** `Save records to sequential file` / `Load records from file until EOF` / `DAT file with pickle`
- **Ready-made code:**
```python
import pickle

# --- SAVE (PUTRECORD loop) ---
# DECLARE Records : ARRAY[0:9] OF Record
Records = []
for i in range(5):
    r = CarRecord()
    r.VehicleID = "ID" + str(i)
    r.EngineSize = 1000 + i * 100
    Records.append(r)

f = open("/tmp/Data.DAT", "wb")
for r in Records:
    pickle.dump(r, f)
f.close()

# --- LOAD (GETRECORD until EOF) ---
Loaded = []
f = open("/tmp/Data.DAT", "rb")
try:
    while True:
        rec = pickle.load(f)
        Loaded.append(rec)
except EOFError:
    pass
f.close()
print("Loaded " + str(len(Loaded)) + " records")

# --- LOAD with display ---
f = open("/tmp/Data.DAT", "rb")
try:
    while True:
        rec = pickle.load(f)
        print(rec.VehicleID + " " + str(rec.EngineSize))
except EOFError:
    pass
f.close()
```
- **Remember:** Save = `open wb` + `pickle.dump` per record + `close`. Load = `open rb` + `try: while True: pickle.load` + `except EOFError: pass` + `close`. Always `import pickle`.

---

---

## PART 3: OOP BASICS — Class, Getter, Setter, Instantiate, Inheritance, Override, Containment

> One standard class shape does 80% of the work. Everything else is renaming + adding a method.

### B1. Class + constructor (private __ attrs, __init__ with params)

- **When exam says:** `Write program code to declare the class X and its constructor. All attributes must be private.`
- **Ready-made code:**
```python
class Car:
    # VehicleID : STRING
    # Registration : STRING
    # EngineSize : INTEGER
    # PurchasePrice : CURRENCY
    def __init__(self, p_vehicleID, p_engineSize):
        # Known at manufacture -> from params; unknown -> placeholders
        self.__VehicleID = p_vehicleID    # STRING from param
        self.__Registration = ""          # STRING not known -> ""
        self.__EngineSize = p_engineSize  # INTEGER from param
        self.__PurchasePrice = 0.00       # CURRENCY not known -> 0.00
```
- **Remember:** `# Attr : TYPE` comments + `self.__Name = param` (not hardcoded) + `self` on every method.

---

### B2. Getter

- **When exam says:** `Write getter(s) for the class` / `Provide access to private attributes`
- **Ready-made code:**
```python
class Car:
    # VehicleID : STRING
    # EngineSize : INTEGER
    def __init__(self, p_vehicleID, p_engineSize):
        self.__VehicleID = p_vehicleID
        self.__EngineSize = p_engineSize
    def GetVehicleID(self):
        return self.__VehicleID
    def GetEngineSize(self):
        return self.__EngineSize
    def GetRegistration(self):
        return self.__Registration
    def GetPurchasePrice(self):
        return self.__PurchasePrice
```
- **Remember:** One getter for **every** private attribute; `def GetX(self): return self.__X`.

---

### B3. Setter (plain + validated)

- **When exam says:** `Write setter(s)` / `SetPurchasePrice should validate` / `should only change if ...`
- **Ready-made code:**
```python
class Car:
    # VehicleID : STRING
    # PurchasePrice : CURRENCY
    def __init__(self, p_vehicleID, p_engineSize):
        self.__VehicleID = p_vehicleID
        self.__PurchasePrice = 0.00
    def GetPurchasePrice(self):
        return self.__PurchasePrice
    # Plain setter (no validation)
    def SetRegistration(self, p_registration):
        self.__Registration = p_registration
    # Validated setter (exam favourite)
    def SetPurchasePrice(self, p_price):
        if p_price > 0:  # validation gate
            self.__PurchasePrice = p_price
    # Validated setter with range (9618_w25 Board pattern)
    def SetValue(self, p_value):
        if p_value >= 0 and p_value <= 100:
            self.__Value = p_value
```
- **Remember:** Setter only for attributes that **change** after creation; fixed attrs (VehicleID) get **no setter**.

---

### B4. Instantiate + list of objects (append, loop)

- **When exam says:** `Instantiate objects` / `Declare array of objects` / `Create list of X`
- **Ready-made code:**
```python
class Car:
    # VehicleID : STRING
    # EngineSize : INTEGER
    def __init__(self, p_vehicleID, p_engineSize):
        self.__VehicleID = p_vehicleID
        self.__EngineSize = p_engineSize
    def GetVehicleID(self): return self.__VehicleID
    def GetEngineSize(self): return self.__EngineSize

# Single instantiation
ThisCar = Car("ABC1234", 2500)

# List/array of objects
Cars = []  # DECLARE Cars : ARRAY[1:10] OF Car
Cars.append(Car("ABC1234", 2500))
Cars.append(Car("XYZ9999", 1800))
Cars.append(Car("LMN0001", 3000))

# Loop over list
for c in Cars:
    print(c.GetVehicleID(), c.GetEngineSize())

# With index
for i in range(len(Cars)):
    print(Cars[i].GetVehicleID())
```
- **Remember:** `Obj = Class(params)` then `list.append(Obj)`; loop with `for obj in list`.

---

### B5. Method that changes attributes (ChangePosition, Move N/S/E/W)

- **When exam says:** `Method to change position` / `Move(direction, distance)` / `ChangePosition(x,y)` / `Bird flies N/S/E/W`
- **Ready-made code:**
```python
class Bird:
    # DistancePerHour : REAL
    # Species : STRING
    # XPosition : REAL
    # YPosition : REAL
    def __init__(self, p_species, p_speed):
        self.__Species = p_species
        self.__DistancePerHour = p_speed
        self.__XPosition = 0.0
        self.__YPosition = 0.0
    def GetX(self): return self.__XPosition
    def GetY(self): return self.__YPosition
    def GetSpeed(self): return self.__DistancePerHour
    def Move(self, direction, minutes):
        # 9618/42/O/N/25: distance = (DistancePerHour / 60) * minutes
        distance = (self.__DistancePerHour / 60) * minutes
        if direction == "N":
            self.__YPosition = self.__YPosition + distance
        elif direction == "S":
            self.__YPosition = self.__YPosition - distance
        elif direction == "E":
            self.__XPosition = self.__XPosition + distance
        elif direction == "W":
            self.__XPosition = self.__XPosition - distance

# Alternative: ChangePosition(dx, dy) for Character
class Character:
    # Name : STRING
    # XCoordinate : INTEGER
    # YCoordinate : INTEGER
    def __init__(self, p_name, p_x, p_y):
        self.__Name = p_name
        self.__XCoordinate = p_x
        self.__YCoordinate = p_y
    def ChangePosition(self, x_change, y_change):
        self.__XCoordinate = self.__XCoordinate + x_change
        self.__YCoordinate = self.__YCoordinate + y_change

# Usage
b = Bird("Cockatiel", 71.0)
b.Move("N", 30)  # 30 minutes north
print(b.GetX(), b.GetY())
```
- **Remember:** Move → `distance = (speed/60)*minutes` then `if direction=="N": Y+=distance`.

---

### B6. Inheritance (super().__init__)

- **When exam says:** `CLASS Book INHERITS LibraryItem` / `Book is a LibraryItem` / `Define subclass`
- **Ready-made code:**
```python
import datetime

class LibraryItem:
    # Title : STRING
    # AuthorArtist : STRING
    # ItemID : INTEGER
    # OnLoan : BOOLEAN
    # DueDate : DATE
    def __init__(self, p_title, p_author, p_itemID):
        self.__Title = p_title
        self.__AuthorArtist = p_author
        self.__ItemID = p_itemID
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()
    def GetTitle(self): return self.__Title
    def GetItemID(self): return self.__ItemID
    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)
    def Returning(self):
        self.__OnLoan = False
    def PrintDetails(self):
        print(self.__Title, self.__AuthorArtist, self.__ItemID)

class Book(LibraryItem):  # INHERITS
    # IsRequested : BOOLEAN  (book-specific, base attrs inherited)
    def __init__(self, p_title, p_author, p_itemID):
        super().__init__(p_title, p_author, p_itemID)  # MUST be first line
        self.__IsRequested = False
    def GetIsRequested(self): return self.__IsRequested
    def SetIsRequested(self): self.__IsRequested = True

class CD(LibraryItem):
    # Genre : STRING
    def __init__(self, p_title, p_author, p_itemID):
        super().__init__(p_title, p_author, p_itemID)
        self.__Genre = ""
    def GetGenre(self): return self.__Genre
    def SetGenre(self, p_genre): self.__Genre = p_genre

# Also correct: LibraryItem.__init__(self, p_title, p_author, p_itemID)
```
- **Remember:** `class Child(Parent):` + `super().__init__(params)` first line; private attrs of parent not directly accessible in child.

---

### B7. Overriding / polymorphism (super().PrintDetails() + for loop)

- **When exam says:** `Override PrintDetails` / `Polymorphism` / `Display all items` / `Call overridden method`
- **Ready-made code:**
```python
class LibraryItem:
    def __init__(self, p_title, p_author, p_itemID):
        self.__Title = p_title; self.__AuthorArtist = p_author; self.__ItemID = p_itemID
    def PrintDetails(self):
        print(self.__Title, self.__AuthorArtist, self.__ItemID)

class Book(LibraryItem):
    def __init__(self, p_title, p_author, p_itemID):
        super().__init__(p_title, p_author, p_itemID)
        self.__IsRequested = False
    def PrintDetails(self):  # OVERRIDE — same name, different behaviour
        super().PrintDetails()  # call base version first
        print("IsRequested:", self.__IsRequested)

class CD(LibraryItem):
    def __init__(self, p_title, p_author, p_itemID):
        super().__init__(p_title, p_author, p_itemID)
        self.__Genre = ""
    def PrintDetails(self):
        print("CD Details")
        super().PrintDetails()
        print("Genre:", self.__Genre)

# Polymorphic loop — one call, right version each time
Items = []
Items.append(Book("Computing", "Sylvia", 1234))
Items.append(CD("Let It Be", "The Beatles", 2345))
for item in Items:
    item.PrintDetails()  # polymorphism: Book.PrintDetails vs CD.PrintDetails
```
- **Remember:** Override = same method name in subclass + `super().Method()` to reuse base; loop `for item in list: item.Method()` is polymorphism.

---

### B8. Containment (IS-A vs HAS-A, one object vs list)

- **When exam says:** `Course has Lessons` / `Station contains Trains[0:9]` / `Class X contains Y`
- **Ready-made code:**
```python
# IS-A = Inheritance (Book is a LibraryItem)  -> class Book(LibraryItem)
# HAS-A = Containment (Course has Lessons)    -> self.__lessons = [] + append(Lesson(...))

class Train:
    # TrainID : STRING
    # Destination : STRING
    def __init__(self, p_id, p_dest):
        self.__TrainID = p_id
        self.__Destination = p_dest
    def GetID(self): return self.__TrainID
    def GetDestination(self): return self.__Destination

class Lesson:
    # LessonTitle : STRING
    # DurationMinutes : INTEGER
    def __init__(self, p_title, p_duration):
        self.__LessonTitle = p_title
        self.__DurationMinutes = p_duration
    def OutputLessonDetails(self):
        return str(self.__LessonTitle) + ", " + str(self.__DurationMinutes) + " mins"

class Assessment:
    # AssessmentTitle : STRING
    # MaxMarks : INTEGER
    def __init__(self, p_title, p_marks):
        self.__AssessmentTitle = p_title
        self.__MaxMarks = p_marks

# CONTAINMENT: ONE object
class CourseSingle:
    # CourseTitle : STRING
    # CourseAssessment : Assessment  (one)
    def __init__(self, p_title):
        self.__CourseTitle = p_title
        self.__CourseAssessment = None  # not set yet
    def AddAssessment(self, p_title, p_marks):
        self.__CourseAssessment = Assessment(p_title, p_marks)  # HAS-A single
    def GetAssessment(self): return self.__CourseAssessment

# CONTAINMENT: LIST of objects (up to 50 or 10)
class Station:
    # StationName : STRING
    # Trains : ARRAY[0:9] OF Train  (10 trains)
    def __init__(self, p_name):
        self.__StationName = p_name
        self.__NumberOfTrains = 0
        self.__Trains = []  # will hold Train objects (up to 10)
    def AddTrain(self, p_id, p_dest):
        if self.__NumberOfTrains < 10:
            self.__Trains.append(Train(p_id, p_dest))
            self.__NumberOfTrains += 1
    def GetTrain(self, index):
        return self.__Trains[index]
    def GetNumberOfTrains(self): return self.__NumberOfTrains

# Full containment with both (Course has many Lessons + one Assessment)
class Course:
    # CourseTitle : STRING
    # MaxStudents : INTEGER
    # NumberOfLessons : INTEGER
    # CourseLesson : ARRAY[1:50] OF Lesson
    # CourseAssessment : Assessment
    def __init__(self, p_title, p_max):
        self.__CourseTitle = p_title
        self.__MaxStudents = p_max
        self.__NumberOfLessons = 0
        self.__CourseLesson = []
        self.__CourseAssessment = None
    def AddLesson(self, p_title, p_duration, p_requiresLab):
        # guard: if self.__NumberOfLessons < 50:
        self.__NumberOfLessons += 1
        self.__CourseLesson.append(Lesson(p_title, p_duration))
    def AddAssessment(self, p_title, p_marks):
        self.__CourseAssessment = Assessment(p_title, p_marks)
    def OutputCourseDetails(self):
        print(self.__CourseTitle, "Max:", self.__MaxStudents)
        for i in range(self.__NumberOfLessons):
            print(self.__CourseLesson[i].OutputLessonDetails())
        if self.__CourseAssessment is not None:
            print(self.__CourseAssessment.OutputLessonDetails())
```
- **Remember:** HAS-A → `self.__X = []` + `append(OtherClass(...))` (list) or `self.__Y = OtherClass(...)` (single).

---

### B14. OOP with 1D array attribute (PayYear 52 weeks) — Seen: 9618/42/M/J/23 Q3(a)(iii)(iv)

- **When exam says:** `PayYear2022 : ARRAY[0:51] OF REAL` inside a class / `SetPay(week, hours)` / `GetTotalPay` — class owns an array field
- **Ready-made code:**
```python
class Employee:
    # HourlyPay : REAL
    # EmployeeNumber : STRING
    # JobTitle : STRING
    # PayYear2022 : ARRAY[0:51] OF REAL  (52 weeks)
    def __init__(self, p_hourlyPay, p_employeeNumber, p_jobTitle):
        self.__HourlyPay = p_hourlyPay
        self.__EmployeeNumber = p_employeeNumber
        self.__JobTitle = p_jobTitle
        self.__PayYear2022 = []
        for i in range(52):
            self.__PayYear2022.append(0.0)
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    def GetHourlyPay(self):
        return self.__HourlyPay
    def SetPay(self, p_weekNumber, p_hoursWorked):
        # weekNumber is 0..51 or 1..52 — match question (here 1..52)
        pay = self.__HourlyPay * p_hoursWorked
        # if weeks are 1..52 in question, use p_weekNumber - 1
        index = p_weekNumber - 1
        if index >= 0 and index < 52:
            self.__PayYear2022[index] = pay
        else:
            # if question uses 0..51 directly: self.__PayYear2022[p_weekNumber] = pay
            self.__PayYear2022[p_weekNumber] = pay
    def GetTotalPay(self):
        total = 0.0
        for i in range(52):
            total = total + self.__PayYear2022[i]
        return total

class Manager(Employee):
    # BonusValue : REAL  (percentage e.g. 10.0)
    def __init__(self, p_hourlyPay, p_employeeNumber, p_jobTitle, p_bonusValue):
        super().__init__(p_hourlyPay, p_employeeNumber, p_jobTitle)
        self.__BonusValue = p_bonusValue
    def GetBonusValue(self):
        return self.__BonusValue
    def SetPay(self, p_weekNumber, p_hoursWorked):
        # Increase hours by bonus before calling parent
        increased = p_hoursWorked * (1 + self.__BonusValue / 100)
        super().SetPay(p_weekNumber, increased)
        # Alternative explicit: Employee.SetPay(self, p_weekNumber, increased)

# Usage
emp = Employee(15.22, "12452", "Junior Developer")
emp.SetPay(1, 40)
print(emp.GetTotalPay())
mgr = Manager(22.50, "02586", "Interface Manager", 5.25)
mgr.SetPay(1, 40)
print(mgr.GetTotalPay())
```
- **Remember:** Array attribute → `self.__Arr = []` + `for i in range(N): append(0)` in `__init__`; `SetPay` writes to `Arr[index]`; `GetTotalPay` loops and sums; Manager overrides `SetPay`, computes `hours*(1+Bonus/100)` then `super().SetPay`.

---

---

## PART 4: ADTs — Stack / Queue / Hash Table (All Together)

> All abstract data types in one place. Queue is a single circular-array template with both `Enqueue` and `Dequeue` together — do not split across pages. Hash shows linear-probing collision.

### B10. Stack (array 30, TopOfStack=-1, Push returns True/False, Pop returns -999) — 9618/41/O/N/25

- **When exam says:** `Stack` / `Push` / `Pop` / `TopOfStack` / `StackPointer` / `IsEmpty` / `IsFull`
- **Ready-made code:**
```python
class Stack:
    # StackArray : ARRAY[0:29] OF INTEGER  (size 30)
    # TopOfStack : INTEGER  (-1 = empty)
    def __init__(self):
        self.__StackArray = [0] * 30  # or [None]*30 or [""]*30 per type
        self.__TopOfStack = -1  # empty
    def IsEmpty(self):
        return self.__TopOfStack == -1
    def IsFull(self):
        return self.__TopOfStack == 29  # size-1
    def Push(self, p_value):
        if self.__TopOfStack == 29:  # full
            return False
        self.__TopOfStack += 1
        self.__StackArray[self.__TopOfStack] = p_value
        return True
    def Pop(self):
        if self.__TopOfStack == -1:  # empty
            return -999  # sentinel for empty (or None / "" per question)
        value = self.__StackArray[self.__TopOfStack]
        self.__TopOfStack -= 1
        return value
    def Peek(self):
        if self.__TopOfStack == -1:
            return -999
        return self.__StackArray[self.__TopOfStack]

# Global-style alternative (when question uses globals, not a class):
StackArray = [0] * 30
TopOfStack = -1

def PushGlobal(value):
    global TopOfStack
    if TopOfStack == 29:
        return False
    TopOfStack += 1
    StackArray[TopOfStack] = value
    return True

def PopGlobal():
    global TopOfStack
    if TopOfStack == -1:
        return -999
    value = StackArray[TopOfStack]
    TopOfStack -= 1
    return value

# Usage
s = Stack()
s.Push(10); s.Push(20)
print(s.Pop())  # 20
print(s.Pop())  # 10
print(s.Pop())  # -999 (empty)
```
- **Remember:** Stack → `Top=-1`, `Push: if full return False else Top+=1; array[Top]=val; return True`, `Pop: if empty return -999 else val=array[Top]; Top-=1; return val`.

---

### B11. Queue: GLOBAL declare + Enqueue + Dequeue (circular, wrap-around) — 9618/43/O/N/25

- **When exam says:** `Queue` / `Enqueue` / `Dequeue` / `QueueHead, QueueTail, NumberItems` / `circular queue`
- **Ready-made code:**
```python
class Queue:
    # QueueArray : ARRAY[0:29] OF STRING  (size 30)
    # QueueHead : INTEGER  (-1 = empty)
    # QueueTail : INTEGER  (-1 = empty)
    # NumberItems : INTEGER
    def __init__(self):
        self.__QueueArray = [""] * 30
        self.__QueueHead = -1
        self.__QueueTail = -1
        self.__NumberItems = 0
    def IsEmpty(self):
        return self.__NumberItems == 0
    def IsFull(self):
        return self.__NumberItems == 30
    def Enqueue(self, p_value):
        if self.__NumberItems == 30:  # full
            return False
        if self.__NumberItems == 0:  # first item
            self.__QueueHead = 0
            self.__QueueTail = 0
        else:
            self.__QueueTail = (self.__QueueTail + 1) % 30  # circular
        self.__QueueArray[self.__QueueTail] = p_value
        self.__NumberItems += 1
        return True
    def Dequeue(self):
        if self.__NumberItems == 0:  # empty
            return ""  # or -999 / None per question
        value = self.__QueueArray[self.__QueueHead]
        self.__QueueArray[self.__QueueHead] = ""  # optional clear
        if self.__NumberItems == 1:  # last item removed
            self.__QueueHead = -1
            self.__QueueTail = -1
        else:
            self.__QueueHead = (self.__QueueHead + 1) % 30
        self.__NumberItems -= 1
        return value
    def GetNumberItems(self): return self.__NumberItems

# Linear (non-circular) alternative — simpler, also accepted if Q not circular:
class QueueLinear:
    def __init__(self):
        self.__QueueArray = [""] * 30
        self.__QueueHead = 0
        self.__QueueTail = -1
        self.__NumberItems = 0
    def Enqueue(self, p_value):
        if self.__QueueTail == 29:
            return False
        self.__QueueTail += 1
        self.__QueueArray[self.__QueueTail] = p_value
        self.__NumberItems += 1
        return True
    def Dequeue(self):
        if self.__NumberItems == 0:
            return ""
        value = self.__QueueArray[self.__QueueHead]
        self.__QueueHead += 1
        self.__NumberItems -= 1
        return value

# Usage
q = Queue()
q.Enqueue("A"); q.Enqueue("B")
print(q.Dequeue())  # A
print(q.Dequeue())  # B
```
- **Remember:** Queue → `Head=-1 Tail=-1 NumberItems=0`; `Enqueue: if full return False; Tail=(Tail+1)%size; array[Tail]=val; NumberItems+=1`; `Dequeue: if empty return ""; val=array[Head]; Head=(Head+1)%size; NumberItems-=1`.

---

> **Note:** Hash ADT below is the same template as PART 2 §A8 — kept together here so all ADT logic is searchable in one place. File→Hash pipeline is in PART 7.

### A8. Hash table 2D with collision (linear probing) — 9618/41/O/N/25 pattern

- **When exam says:** `HashTable[100][10]` / `Hash = key MOD 100` / `collision: next available space` / `InsertData` / `GetRecord`
- **Ready-made code:**
```python
# DECLARE HashTable : ARRAY[0:99, 0:9] OF STRING  (100 x 10)
# Use list of lists; "" = empty
HashTable = []
for i in range(100):
    row = []
    for j in range(10):
        row.append("")
    HashTable.append(row)

def Hash(key):
    # key is INTEGER (e.g. ID 123); if STRING key: total % 100
    return key % 100  # MOD 100

def InitialiseHashTable():
    global HashTable
    HashTable = []
for i in range(100):
    row = []
    for j in range(10):
        row.append("")
    HashTable.append(row)

def InsertData(key, data_string):
    # data_string e.g. "123,John,01234" — store whole line or record
    slot = Hash(key)
    for col in range(10):  # try 10 columns in that row
        if HashTable[slot][col] == "":
            HashTable[slot][col] = data_string
            return True  # inserted
    return False  # row full — collision overflow

def GetRecord(key):
    slot = Hash(key)
    for col in range(10):
        if HashTable[slot][col] == "":
            return ""  # not found (empty hit)
        # check if stored record matches key (first field before comma)
        stored_key = int(HashTable[slot][col].split(",")[0])
        if stored_key == key:
            return HashTable[slot][col]
    return ""  # not found after 10 probes

# File -> HashTable: ReadData from file, split by comma, insert
def ReadData(filename):
    try:
        f = open(filename, "r")
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")  # or SplitData(line, ",")
            key = int(parts[0])
            InsertData(key, line)
    except FileNotFoundError:
        print("File not found")

        f.close()
InitialiseHashTable()
InsertData(123, "123,Alice,555-0100")
InsertData(223, "223,Bob,555-0101")  # 223%100=23 collides if 123%100=23 etc.
print(GetRecord(123))
```
- **Remember:** Hash 2D → `MOD 100` for row, `for col in range(10)` for collision, `""` means empty.

---

### B9. 2D Array of Objects (Board 10x10 BoardObject) — 9618/43/O/N/25 Q1

- **When exam says:** `Board is 10x10 2D array of BoardObject` / `GetObject / SetObject / DisplayBoard` / `initialise with empty`
- **Ready-made code:**
```python
class BoardObject:
    # Code : STRING
    # Value : INTEGER
    def __init__(self, p_code, p_value):
        self.__Code = p_code
        self.__Value = p_value
    def GetCode(self): return self.__Code
    def GetValue(self): return self.__Value
    def SetCode(self, p_code): self.__Code = p_code
    def SetValue(self, p_value): self.__Value = p_value

class Board:
    # BoardArray : ARRAY[0:9, 0:9] OF BoardObject  (10x10)
    def __init__(self):
        # Initialise every cell with empty BoardObject("-", 0)
        self.__BoardArray = []
        for row in range(10):
            row_list = []
            for col in range(10):
                row_list.append(BoardObject("-", 0))
            self.__BoardArray.append(row_list)
    def GetObject(self, row, col):
        return self.__BoardArray[row][col]
    def SetObject(self, row, col, p_code, p_value):
        self.__BoardArray[row][col] = BoardObject(p_code, p_value)
        # Alternative: self.__BoardArray[row][col].SetCode(p_code)
        #              self.__BoardArray[row][col].SetValue(p_value)
    def DisplayBoard(self):
        for row in range(10):
            line = ""
            for col in range(10):
                line = line + self.__BoardArray[row][col].GetCode() + " "
            print(line.strip())

# Usage
MyBoard = Board()
MyBoard.SetObject(0, 0, "A", 5)
print(MyBoard.GetObject(0, 0).GetCode())  # A
MyBoard.DisplayBoard()
```
- **Remember:** 2D array → `[[BoardObject("-",0) for _ in range(10)] for _ in range(10)]` + `GetObject(row,col)` / `SetObject(row,col,code,value)` + `DisplayBoard` loops both dims.

---

---

## PART 5: ALL SORTING TOGETHER — Bubble / Selection / Insertion (+ Descending Variant)

> Every sort the exam has used 2022–2025 in one place. Copy the exact loop bounds — off-by-one loses the mark.

### B13b. Selection Sort (ascending) — basic template

- **When exam says:** `Sort into ascending order using selection sort` / `Do not use built-in sort`
- **Ready-made code:**
```python
# DECLARE Arr : ARRAY[0:19] OF INTEGER  (any size n)
Arr = [64, 25, 12, 22, 11]
n = len(Arr)

for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if Arr[j] < Arr[min_idx]:
            min_idx = j
    # swap Arr[i] and Arr[min_idx]
    temp = Arr[i]
    Arr[i] = Arr[min_idx]
    Arr[min_idx] = temp

# After loop, Arr is sorted ascending
print(Arr)
```
- **Remember:** Selection Sort = find `min_idx` in unsorted part, swap with `i`. `n-1` outer passes, `i+1` inner start.

---

### B15. Insertion Sort + Bubble Sort descending by first character (MID) — Seen: 9618/42/O/N/22 Q1(e) and 9618/42/M/J/23 Q1(c)

- **When exam says:** `InsertionSort by priority` / `SortDescending using MID(Animals[Y],0,1)` / sort 2D by one column / descending alphabetical
- **Ready-made code:**
```python
# InsertionSort for 1D or 2D array sorted by priority (column 1)
# Jobs[0..99, 0..1] where Jobs[i][0]=jobNumber, Jobs[i][1]=priority
# NumberOfJobs = how many entries filled (with -1 sentinel)
Jobs = []
for i in range(100):
    Jobs.append([-1, -1])
NumberOfJobs = 0

def Initialise():
    global NumberOfJobs
    for i in range(100):
        Jobs[i][0] = -1
        Jobs[i][1] = -1
    NumberOfJobs = 0

def AddJob(p_jobNumber, p_priority):
    global NumberOfJobs
    if NumberOfJobs < 100:
        Jobs[NumberOfJobs][0] = p_jobNumber
        Jobs[NumberOfJobs][1] = p_priority
        NumberOfJobs = NumberOfJobs + 1
        print("Added")
        return True
    else:
        print("Not added")
        return False

def InsertionSort():
    # Sort Jobs[0..NumberOfJobs-1] by priority ascending (col 1)
    for i in range(1, NumberOfJobs):
        key_number = Jobs[i][0]
        key_priority = Jobs[i][1]
        j = i - 1
        while j >= 0 and Jobs[j][1] > key_priority:
            Jobs[j + 1][0] = Jobs[j][0]
            Jobs[j + 1][1] = Jobs[j][1]
            j = j - 1
        Jobs[j + 1][0] = key_number
        Jobs[j + 1][1] = key_priority

def PrintArray():
    for i in range(NumberOfJobs):
        print(str(Jobs[i][0]) + " priority " + str(Jobs[i][1]))

# Bubble Sort descending by first character only (9618/42/M/J/23 Q1c)
Animals = ["horse","lion","rabbit","mouse","bird","deer","whale","elephant","kangaroo","tiger"]

def SortDescending():
    n = len(Animals)
    for x in range(n - 1):
        for y in range(n - 1 - x):
            # MID(Animals[Y],0,1) < MID(Animals[Y+1],0,1)  -> swap for descending
            # In Python, first char is string[0]
            first_y = Animals[y][0]
            first_next = Animals[y + 1][0]
            if first_y < first_next:
                temp = Animals[y]
                Animals[y] = Animals[y + 1]
                Animals[y + 1] = temp

# descending full-string version (if question says descending alphabetical, not just first char)
def BubbleSortDescendingFull(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr
```
- **Remember:** InsertionSort → `for i 1..n-1: key=arr[i]; j=i-1; while j>=0 and arr[j][keycol] > key: shift; arr[j+1]=key`; Descending MID → `if arr[y][0] < arr[y+1][0]: swap` (swap when earlier char is smaller).

---

### B13. Main program patterns (input validation while loops, bubble sort, binary search)

- **When exam says:** `Main program` / `Validate input` / `BubbleSort` / `BinarySearch` / `RecursiveBinarySearch`
- **Ready-made code:**
```python
# 1. Input validation loop (while True + break when valid)
# Pattern: keep asking until valid input
def get_valid_direction():
    while True:
        direction = input("Enter direction N/S/E/W: ").upper()
        if direction in ("N", "S", "E", "W"):
            return direction
        print("Invalid direction, try again")

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Must be positive")
        except ValueError:
            print("Must be an integer")

def get_minutes():
    # 9618/42/O/N/25 Bird minutes: 1..60
    while True:
        try:
            m = int(input("Enter minutes (1-60): "))
            if 1 <= m <= 60:
                return m
            print("Out of range")
        except ValueError:
            print("Invalid")

# 2. BubbleSort (ascending, exam standard)
def BubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

# BubbleSort for objects (by attribute)
def BubbleSortBirds(birds):
    n = len(birds)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if birds[j].GetSpecies() > birds[j + 1].GetSpecies():
                temp = birds[j]
                birds[j] = birds[j + 1]
                birds[j + 1] = temp

# 3. Iterative BinarySearch (array must be sorted)
def BinarySearch(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # not found

# 4. Recursive BinarySearch (9618/42/O/N/25 pattern)
def RecursiveBinarySearch(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return RecursiveBinarySearch(arr, target, mid + 1, high)
    else:
        return RecursiveBinarySearch(arr, target, low, mid - 1)

# Usage: RecursiveBinarySearch(sorted_arr, 42, 0, len(sorted_arr)-1)

# 5. Linear search (when array not sorted or searching objects)
def LinearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# 6. Main program combining all (9618/42/O/N/25 style)
# Birds sorted, then binary search, then Move
# Birds = [Bird("Cockatiel", 71.0), Bird("Macaw", 56.0)]
# BubbleSortBirds(Birds)
# idx = BinarySearch([b.GetSpecies() for b in Birds], "Macaw")
# if idx != -1:
#     Birds[idx].Move("N", 30)
```
- **Remember:** BubbleSort → nested `for i/for j` with `arr[j]>arr[j+1]` swap; BinarySearch → `low/high/mid` with `//2`; validation → `while True: input + if valid: break`.

---

---

## PART 6: ALL SEARCHING + FILTERING + COUNTING + CHECK-DIGIT + RECURSION

> Searching (linear + binary iterative + binary recursive), filter/count, check-digit queue, recursive rewrite, and validation-loop main program.

### B13c. Linear Search (returns index or -1)

- **When exam says:** `Search for value in array` / `Linear search` / `Return index or -1 if not found`
- **Ready-made code:**
```python
# DECLARE Arr : ARRAY[0:9] OF INTEGER
# DECLARE SearchVal : INTEGER
# DECLARE FoundIndex : INTEGER

Arr = [5, 12, 7, 9, 3]
SearchVal = 7
FoundIndex = -1

for i in range(len(Arr)):
    if Arr[i] == SearchVal:
        FoundIndex = i
        break

if FoundIndex == -1:
    print("Not found")
else:
    print("Found at index " + str(FoundIndex))
```
- **Remember:** `FoundIndex = -1` before loop; `break` on match; `-1` means not found.

---

### B16. Filter by multiple criteria + Count occurrences (ChooseTree / FindValues) — Seen: 9618/41/M/J/24 Q2(e) and 9618/41/O/N/22 Q1(c)

- **When exam says:** `Return all trees that meet criteria` / `ChooseTree(Species, MinHeight)` / `Count how many times value appears` / `FindValues`
- **Ready-made code:**
```python
# DECLARE Trees : ARRAY[0:9] OF TreeRecord  (TreeRecord has Species, Height, etc.)
# DECLARE Count : INTEGER

# Filter: return list of items matching criteria
def ChooseTree(Species, MinHeight):
    result = []
    for i in range(len(Trees)):
        if Trees[i].Species == Species and Trees[i].Height >= MinHeight:
            result.append(Trees[i])
    return result

# Usage
Filtered = ChooseTree("Oak", 10)
print("Found " + str(len(Filtered)) + " matches")
for t in Filtered:
    print(t.Species + " " + str(t.Height))

# Count occurrences: how many times SearchVal appears
def CountOccurrences(Arr, SearchVal):
    count = 0
    for i in range(len(Arr)):
        if Arr[i] == SearchVal:
            count = count + 1
    return count

# Alternative: FindValues pattern (9618/41/O/N/22) — count values in range 1..100
def FindValues(Arr, Low, High):
    count = 0
    for i in range(len(Arr)):
        if Arr[i] >= Low and Arr[i] <= High:
            count = count + 1
    return count

print(CountOccurrences([1, 2, 2, 3], 2))  # 2
print(FindValues([5, 12, 7, 9], 1, 10))  # 3
```
- **Remember:** Filter = loop + `if matches criteria` + `append`; Count = `count=0` + `if match: count+=1` + `return count`.

---

### B17. Check digit / checksum validation with queue (StoreItems) — Seen: 9618/41/M/J/24 Q3(c)(d)

- **When exam says:** `Check digit` / `valid 7-character string` / `StoreItems validates and Enqueue` / checksum then queue
- **Ready-made code:**
```python
# Queue for 6-char data (check digit removed) — circular or linear pattern from B11
QueueArray = []
for i in range(100):
    QueueArray.append("")
QueueHead = -1
QueueTail = -1
NumberItems = 0

def Enqueue(p_value):
    global QueueHead, QueueTail, NumberItems
    if NumberItems == 100:
        return -1
    if NumberItems == 0:
        QueueHead = 0
        QueueTail = 0
    else:
        QueueTail = (QueueTail + 1) % 100
    QueueArray[QueueTail] = p_value
    NumberItems = NumberItems + 1
    return 1

def Dequeue():
    global QueueHead, QueueTail, NumberItems
    if NumberItems == 0:
        return ""
    value = QueueArray[QueueHead]
    QueueArray[QueueHead] = ""
    if NumberItems == 1:
        QueueHead = -1
        QueueTail = -1
    else:
        QueueHead = (QueueHead + 1) % 100
    NumberItems = NumberItems - 1
    return value

def CalculateCheckDigit(six_chars):
    # Example from 9618/41/M/J/24: weighted sum then /10 rounded down
    # Use the exact weights given in question; placeholder weights 7,5,3,2,9,4
    total = 0
    total = total + int(six_chars[0]) * 7
    total = total + int(six_chars[1]) * 5
    total = total + int(six_chars[2]) * 3
    total = total + int(six_chars[3]) * 2
    total = total + int(six_chars[4]) * 9
    total = total + int(six_chars[5]) * 4
    check = total % 10
    # Alternative described: Divide sum by 10 rounded down = total // 10 % 10
    # If question says sum products /10 rounded down, use: check = (total // 10) % 10
    return str(check)

def IsValidSeven(seven):
    if len(seven) != 7:
        return False
    six = ""
    for i in range(6):
        six = six + seven[i]
    expected = CalculateCheckDigit(six)
    actual = seven[6]
    if expected == actual:
        return True
    else:
        return False

def StoreItems():
    invalid_count = 0
    for i in range(10):
        s = input("Enter 7-char string: ").strip()
        if IsValidSeven(s):
            six = ""
            for k in range(6):
                six = six + s[k]
            result = Enqueue(six)
            if result == 1:
                print("Stored")
            else:
                print("Full")
        else:
            print("Invalid")
            invalid_count = invalid_count + 1
    print("Invalid count: " + str(invalid_count))
    return invalid_count

# Main after StoreItems
# StoreItems()
# v = Dequeue()
# if v == "":
#     print("Queue empty")
# else:
#     print(v)
```
- **Remember:** Check digit → `total = sum(int(s[i])*weight)` then `check = total % 10` (or `//10 %10` per question); `IsValid` compares `seven[6]` to `check`; `StoreItems` loops 10 inputs, strips check digit with `six = seven[0..5]`, `Enqueue(six)`, counts invalid, prints `Stored/Full/Invalid`.

---

### B18. Recursive rewrite of iterative function — Seen: 9618/42/O/N/22 Q3(d) IterativeOutput

- **When exam says:** `Rewrite as recursive function` / `RecursiveOutput(Start)` / `FUNCTION IterativeOutput(Start) RETURNS INTEGER`
- **Ready-made code:**
```python
# Global queue from earlier (Queue + head pointer)
Queue = []
for i in range(100):
    Queue.append(0)
HeadPointer = 20  # number of items currently in queue
# Fill example
for i in range(20):
    Queue[i] = i + 1

def IterativeOutput(start):
    total = 0
    for count in range(start - 1, HeadPointer - 1, -1):
        total = total + Queue[count]
    return total
    # Pseudocode was: FOR Count <- Start-1 TO HeadPointer STEP -1

def RecursiveOutput(start):
    # Base case: when start <= HeadPointer? need to match iterative range
    # If Start is position (1-indexed count), recursive sums Queue[Start-1] + rest
    if start <= HeadPointer:
        return 0
    # But clearer spec from paper: start is index to sum downwards
    # So translate loop: sum from start-1 down to HeadPointer inclusive
    # Recursive: if start -1 < HeadPointer: return 0 else Queue[start-1] + RecursiveOutput(start-1)
    if start - 1 < HeadPointer:
        return 0
    return Queue[start - 1] + RecursiveOutput(start - 1)

# Cleaner alternative matching paper's expected answer:
def RecursiveOutput2(current):
    # current starts at Start-1, goes down to HeadPointer
    if current < HeadPointer:
        return 0
    if current == HeadPointer:
        return Queue[current]
    return Queue[current] + RecursiveOutput2(current - 1)
# Call: total = RecursiveOutput2(Start - 1)

# Another common recursive pattern in papers: total from HeadPointer down
def RecursiveSum(index):
    if index < 0:
        return 0
    if index == 0:
        return Queue[0]
    return Queue[index] + RecursiveSum(index - 1)
# Call: total = RecursiveSum(HeadPointer - 1)

# Generic recursion template for exam
def RecurseExample(n):
    if n <= 0:
        return 0
    return n + RecurseExample(n - 1)
```
- **Remember:** Recursive rewrite → `if base_case: return 0/value` then `return arr[index] + Recurse(index-1)`; keep same start logic as iterative loop; base is `index < HeadPointer` or `index < 0`.

---

> **Binary search (iterative + recursive) and input-validation loops:** see PART 5 §B13 — the full bubble/binary-search/validation main program lives there. Linear search dedicated template is §B13c below (already included above before this note).


---

## PART 7: CROSSOVER / MAIN PROGRAM PIPELINES — File → Objects → Search → Move

> End-to-end chains the exam actually sets: read a file, build objects, search, move/validate, and write back.

### A11. File -> objects crossover: full chain (file -> array -> search -> move)

- **When exam says:** `Read file into array of objects, then search/move/display` (9618/42 Q2, 9618_w22 Q2)
- **Ready-made code:**
```python
class Character:
    # Name : STRING
    # XCoordinate : INTEGER
    # YCoordinate : INTEGER
    def __init__(self, name, x, y):
        self.__Name = name
        self.__XCoordinate = x
        self.__YCoordinate = y
    def GetName(self): return self.__Name
    def GetX(self): return self.__XCoordinate
    def GetY(self): return self.__YCoordinate
    def ChangePosition(self, x_change, y_change):
        self.__XCoordinate += x_change
        self.__YCoordinate += y_change

# 1) File -> objects (grouped 3 lines)
Characters = []
f = open("/tmp/Characters.txt", "r")
lines = f.read().splitlines()
f.close()
i = 0
while i + 2 < len(lines):
    Characters.append(Character(lines[i], int(lines[i+1]), int(lines[i+2])))
    i += 3

# 2) Search (case-insensitive, retry until found)
# In exam: input() loop; here scripted with while found==-1
search_name = "qui"  # user input
found = -1
for idx in range(len(Characters)):
    if Characters[idx].GetName().upper() == search_name.upper():
        found = idx
        break

# Retry pattern (with input in exam):
# found = -1
# while found == -1:
#     search_name = input("Enter name: ")
#     for idx in range(len(Characters)):
#         if Characters[idx].GetName().upper() == search_name.upper():
#             found = idx
#     if found == -1:
#         print("Name not found")

# 3) Move with direction validation
if found != -1:
    direction = "A"  # user input A/W/S/D
    # while direction not in ("A","W","S","D"):
    #     direction = input("Enter A/W/S/D: ").upper()
    if direction == "A": Characters[found].ChangePosition(-1, 0)
    elif direction == "D": Characters[found].ChangePosition(1, 0)
    elif direction == "W": Characters[found].ChangePosition(0, 1)
    elif direction == "S": Characters[found].ChangePosition(0, -1)
    print(str(Characters[found].GetName()) + " now at " + str(Characters[found].GetX()) + "," + str(Characters[found].GetY()))
```
- **Remember:** File → objects → `found=-1` linear search with `.upper()` → validated move → output via getters.

---

---

## Quick Reference Card (1-page cheat sheet)

| If exam says X | Write Y |
|---|---|
| `TYPE Rec ... ENDTYPE` | `class Rec: def __init__(self): self.Field=""` (public fields) |
| `OPENFILE FOR WRITE/READ/APPEND/RANDOM` | `open(f,"w"/"r"/"a"/"r+b")` + `open` + `close()` explicitly |
| `Each line is one record (CSV)` | `read().splitlines()` + `line.split(",")` + `append(Obj(parts[0],parts[1]))` |
| `Each record is 3 lines` | `while i+2<len(lines): Obj(lines[i],int(lines[i+1]),int(lines[i+2])); i+=3` |
| `Split without inbuilt split` | Loop `for ch in s: if ch==delim: result.append(cur); cur="" else: cur+=ch` |
| `Sequential binary / PUTRECORD / GETRECORD` | `pickle.dump(obj,f)` to write; `while True: pickle.load(f)` + `except EOFError: pass` |
| `Random file / SEEK / Hash MOD N` | `struct.pack(FMT,...)` + `f.seek(slot*SIZE)` + `slot=key%N` |
| `TRY ... EXCEPT ... FINALLY` | `try: risky` / `except ValueError as e:` / `except Exception as e:` (last) / `else:` / `finally: close` |
| `WriteAllToFile with exception` | `try: open(w) + for + write + close(); return True` / `except OSError as e: return False` |
| `Class X, all attrs private` | `class X: # Attr:TYPE` + `def __init__(self,p): self.__Attr=p` |
| `Getter` | `def GetAttr(self): return self.__Attr` (one per attr) |
| `Setter (validated)` | `def SetAttr(self,p): if p>0: self.__Attr=p` |
| `Instantiate / array of objects` | `obj = Class(params)` / `arr=[]; arr.append(Class(...)); for o in arr: o.GetX()` |
| `Method that changes attrs (Move)` | `def Move(self,dir,mins): d=(speed/60)*mins; if dir=="N": self.__Y+=d ...` |
| `CLASS Child INHERITS Parent` | `class Child(Parent): def __init__(self,p): super().__init__(p); self.__New=""` |
| `Override / polymorphism` | `def PrintDetails(self): super().PrintDetails(); print(self.__Extra)` + `for i in list: i.PrintDetails()` |
| `X has Y / contains Y (HAS-A)` | `self.__Y=[]; self.__Y.append(Y(...))` (list) or `self.__Y=Y(...)` (single) |
| `2D array of objects 10x10` | `[[Obj("-",0) for _ in range(10)] for _ in range(10)]` + `GetObject/SetObject/DisplayBoard` |
| `Stack (30, Top=-1)` | `Push: if Top==29: False else Top+=1; arr[Top]=v; True` / `Pop: if Top==-1: -999 else v=arr[Top]; Top-=1; v` |
| `Queue (Head/Tail=-1, NumberItems)` | `Enqueue: if full: False else Tail=(Tail+1)%N; arr[Tail]=v; Num+=1` / `Dequeue: if empty:"" else v=arr[Head]; Head=(Head+1)%N; Num-=1` |
| `HashTable 100x10, Hash MOD 100` | `slot=key%100; for col in range(10): if table[slot][col]=="": table[slot][col]=data; break` |
| `Search list of objects` | `found=-1; for i in range(len(arr)): if arr[i].GetName().upper()==search.upper(): found=i` |
| `BubbleSort` | `for i in range(n-1): for j in range(n-1-i): if arr[j]>arr[j+1]: swap` |
| `BinarySearch (iterative)` | `low=0; high=n-1; while low<=high: mid=(low+high)//2; if arr[mid]==t: return mid` |
| `RecursiveBinarySearch` | `def RBS(arr,t,low,high): if low>high: -1; mid=(low+high)//2; if arr[mid]==t: mid elif ...: RBS(...)` |
| `Validate input (N/S/E/W, range)` | `while True: val=input().upper(); if val in ("N","S","E","W"): break` |
| `File -> objects -> search -> move` | `open + read().splitlines() + close() + i+=3 + append(Obj) + found=-1 loop .upper() + ChangePosition` |
| `Containment + file pipeline` | `open + line.split(",") + station.AddTrain(...)` + `for i in range(station.GetCount()): station.GetTrain(i).GetID()` |
| `Hash from file (ReadData)` | `open(r): for line in f: ... close()` parts=line.split(","); InsertData(int(parts[0]), line)` |
| `Class array attr PayYear[52] (B17)` | `self.__PayYear=[]; for i in range(52): append(0.0)` + `Pay = Hourly*Hours; PayYear[week]=Pay` + `GetTotalPay loops sum` — Seen 9618/42/M/J/23 Q3 |
| `Manager bonus override (B17)` | `increased=hours*(1+Bonus/100); super().SetPay(week, increased)` — Seen 9618/42/M/J/23 Q3(b) |
| `InsertionSort 2D by priority (B18)` | `for i 1..n-1: key=Jobs[i]; j=i-1; while j>=0 and Jobs[j][1]>key[1]: shift; Jobs[j+1]=key` — Seen 9618/42/O/N/22 Q1(e) |
| `Bubble descending by MID first-char (B18)` | `if arr[y][0] < arr[y+1][0]: swap` — Seen 9618/42/M/J/23 Q1(c) |
| `Filter multi-criteria ChooseTree (B19)` | `result=[]; for i: if MaxH<=inH and MaxW<=inW and Ever==inEver: result.append; Print` — Seen 9618/41/M/J/24 Q2(e) |
| `Count occurrences FindValues (B19)` | `count=0; for i: if arr[i]==target: count+=1` + validate 1..100 — Seen 9618/41/O/N/22 Q1(c) |
| `Check digit StoreItems (B20)` | `total=sum(int(s[i])*weight); check=total%10; valid=seven[6]==check; Enqueue(six)` — Seen 9618/41/M/J/24 Q3 |
| `Recursive rewrite IterativeOutput (B21)` | `if index<Head: return 0 else return Queue[idx]+Recurse(idx-1)` — Seen 9618/42/O/N/22 Q3(d) |

> **Final check before you submit:** every class has `# Attr : TYPE` comments, every `__init__` uses **params** (not hardcoded strings), every file `open` has a matching `close` (or `with`), every `except Exception` is **last**, and every `Hash` uses `MOD` not `hash()`.