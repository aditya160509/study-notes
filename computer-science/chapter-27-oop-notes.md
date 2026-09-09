# A Level CS 9618 — Chapter 27: Object-Oriented Programming (OOP) 🧩

> **Your code-first revision companion.** Every pattern is runnable Python. Each code block tells you **when the exam asks X, write Y** — so you know exactly what to type on the day.
> Textbook source: CUP AS & A Level CS (Langfield & Duddell) Ch. 27 + 9618 Paper 4 past papers 2021–2025.
> Style: short, punchy, line-by-line — written for *you*, not the examiner.

---

## What This Chapter Is (and Why OOP Exists) 💡

> **TL;DR:** Procedural code leaves your data lying around for anyone to change. OOP locks your data in a box and hands you a single key — a method.

**Procedural** (Ch. 14 / 26): you keep data in **records** and write separate **procedures** that act on them. The problem? Any code that can see the record can corrupt it — `ThisCar.EngineSize <- 9999` and your exam answer loses marks.

**OOP:** you bundle data (**attributes**) and the subroutines that work on it (**methods**) into one tidy unit — an **object**. Attributes stay **private** (you only reach them through methods). Methods are **public**. That bundling is called **encapsulation**.

> 🗝️ **In plain English:** think of an object as a safe. The data is inside. The methods are the only door. No door, no access.

| Term | Meaning | Think of it as |
|------|---------|----------------|
| **Class** | Type that combines data + methods (template) | Cookie cutter |
| **Object** | An instance of a class | One cookie |
| **Attributes** | Data items of a class (fields), ALWAYS private | Variables owned by the object |
| **Methods** | Subroutines of a class, ALWAYS public | Things the object can do |
| **Encapsulation** | Data + methods bundled, data hidden behind methods | Data in a safe box with one door |
| **Instantiation** | Creating an object from a class (memory reserved) | Baking a cookie |
| **Instance** | One specific object created from a class | One particular cookie |

> 💛 **Why this matters to you:** most bugs happen because data gets changed somewhere you didn't expect. If the *only* way to change `PurchasePrice` is `SetPurchasePrice(...)`, every change flows through one place — and your validation (`price must be > 0`) lives in ONE spot. Cleaner. Safer. Easier to mark.

> 🍪 **Analogy to keep:** Class = cookie cutter, Object = one cookie. You can bake many cookies from the same cutter, but each cookie holds its own chocolate chips (data).

---

# Part 1: Class Basics — Private Attributes, Constructor, Getters & Setters 🔧

> **TL;DR:** One class shape does 80% of the work — private `__attrs`, an `__init__` that uses its parameters, a getter for *everything*, and a setter only when the value is meant to change.

## 1.1 The Standard 9618 Class Shape

> **When exam asks:** *"Write program code to declare the class X and its constructor. All attributes must be private."* **→ Write this exact shape, renamed:**

```python
class Car:
    """9618 standard shape: private attrs, constructor, getters, setters."""
    # PRIVATE attributes — comment declarations for Python mark scheme
    # VehicleID : STRING
    # Registration : STRING
    # EngineSize : INTEGER

    def __init__(self, n, e):
        # Constructor: runs automatically when you write Car(...)
        self.__VehicleID = n             # known at manufacture
        self.__Registration = ""         # not known yet
        self.__EngineSize = e            # known at manufacture
        self.__PurchasePrice = 0.00      # not known yet

    # ----- getters: ONE for EVERY attribute -----
    def GetVehicleID(self):
        return self.__VehicleID

    def GetEngineSize(self):
        return self.__EngineSize

    # ----- setters: ONLY for attributes that change after creation -----
    def SetRegistration(self, r):
        self.__Registration = r

    def SetPurchasePrice(self, p):
        if p > 0:                        # validation lives HERE
            self.__PurchasePrice = p

    def GetPurchasePrice(self):
        return self.__PurchasePrice
```

**Line-by-line — what you're actually telling Python:**
- `class Car:` — "Hey Python, here's a new blueprint called Car." Nothing exists yet.
- `def __init__(self, n, e):` — **the constructor**. Note the two underscores before *and* after `init`. Python runs this automatically when you write `Car(...)`.
- `self` — the first param of *every* method. It means "this particular object I'm working on right now." Forget it and Python complains.
- `self.__VehicleID = n` — **two underscores before the name = private.** That's how you lock the door. Outside code *cannot* do `obj.__VehicleID`.
- `self.__Registration = ""` — a placeholder for "not known yet." Use `""` for STRING, `0` for INTEGER, `0.00` for CURRENCY, `None` for DATE.
- No `SetVehicleID()`? That's deliberate. VehicleID never changes, so no setter. Adding one anyway would contradict the question — and cost you a mark.

### Bad vs Good — see encapsulation in action 👀

```python
# BAD: public attribute — anyone can corrupt it
class BadAccount:
    def __init__(self, bal):
        self.balance = bal          # PUBLIC
acc = BadAccount(100)
acc.balance = -5000                 # allowed! bug.

# GOOD: private + validated setter
class GoodAccount:
    def __init__(self, bal):
        self.__balance = bal        # PRIVATE
    def GetBalance(self):
        return self.__balance
    def SetBalance(self, v):
        if v >= 0:                  # validation gate
            self.__balance = v
acc = GoodAccount(100)
# acc.__balance = -5000             # AttributeError — blocked
acc.SetBalance(-5000)               # silently rejected
```

> **When exam asks:** *"Explain why properties/attributes are set to PRIVATE."* **→ Answer (you can write this):** To achieve encapsulation — it prevents accidental or direct modification, forces all access through methods where validation can be enforced, and makes the code more robust and reusable. ✅

## 1.2 Constructor Rules — the mark scheme is picky here ⚠️

| Rule | What to write | Trap |
|------|--------------|------|
| Python constructor name | `def __init__(self, ...):` | Writing `def Constructor` = 0 marks in Python |
| Java constructor name | `public Car(String n, int e)` (same name as class) | Mixing Java/Python names loses marks |
| Every method needs `self` | `def GetX(self):` | Forgetting `self` = TypeError |
| Private = `__` prefix | `self.__Name` | `self._Name` (single underscore) is NOT private per mark scheme |
| Python needs comment declarations | `# Name : STRING` above `__init__` | Mark scheme explicitly says *"include attribute declarations using comments"* |
| Use parameters, not hardcoded values | `self.__Name = p_name` | `self.__Name = "John"` = mark lost (examiner report 2023) |

## 1.3 Getters & Setters — When to Omit a Setter 🤔

> **In plain English:** a getter is a window — it lets you *see* the data. A setter is a door — it lets you *change* it. You always need the window; you only add the door when change is meant to happen.

- **Getter for EVERY attribute** — "every attribute must be accessible or there is no point storing it" (textbook p. 461).
- **Setter ONLY for attributes that change AFTER instantiation.** Fixed attributes (VehicleID, EngineSize, CompanyName) get NO setter — that's what makes your object robust.
- Setter with validation: `if new_val > 0: self.__attr = new_val` — the gate that keeps bad data out.

> **When exam says:** *"CompanyName and EmailAddress are set by the constructor and will NEVER change."* **→ Write NO `SetCompanyName`/`SetEmailAddress`.** Only `SetDateLastContact`. Extra setter = design contradiction = mark lost.

### Task 27.01 — Company Class (textbook, fully solved)

```python
import datetime

class Company:
    def __init__(self, company_name, email_address):
        self.__CompanyName = company_name
        self.__EmailAddress = email_address
        self.__DateLastContact = None       # not known yet

    def GetCompanyName(self):
        return self.__CompanyName
    def GetEmailAddress(self):
        return self.__EmailAddress
    def GetDateLastContact(self):
        return self.__DateLastContact
    def SetDateLastContact(self, d):
        self.__DateLastContact = d

# When exam asks: instantiate and test
supplier = Company("Acme Supplies", "sales@acme.example")
supplier.SetDateLastContact(datetime.date(2026, 8, 12))
print(supplier.GetCompanyName())       # Acme Supplies
print(supplier.GetDateLastContact())   # 2026-08-12
```

---

## 1.4 @property Version — the Pythonic Alternative ✨

> **When exam asks:** *"The question shows @property / @setter"* or *"write the class using properties"* **→ Use this form instead of Get/Set pairs:**

```python
class CarProp:
    def __init__(self, n, e):
        self.__VehicleID = n
        self.__Registration = ""
        self.__EngineSize = e
        self.__PurchasePrice = 0.00

    @property
    def VehicleID(self):               # getter
        return self.__VehicleID
    # NO @VehicleID.setter → read-only (never changes)

    @property
    def EngineSize(self):
        return self.__EngineSize
    # no setter → read-only

    @property
    def Registration(self):
        return self.__Registration
    @Registration.setter
    def Registration(self, r):         # setter
        self.__Registration = r

    @property
    def PurchasePrice(self):
        return self.__PurchasePrice
    @PurchasePrice.setter
    def PurchasePrice(self, p):
        if p > 0:
            self.__PurchasePrice = p

# When exam asks: use properties
c = CarProp("ABC1234", 2500)
c.PurchasePrice = 12000               # looks like assignment, goes through setter
c.Registration = "XY61 ABC"
print(c.VehicleID)                    # no brackets — reads like a variable
print(c.PurchasePrice)                # 12000
# c.VehicleID = "NEW"                 # AttributeError: no setter → read-only
```

**How it reads — friendlier than Get/Set:**
- `@property` — turns the method below into a getter. You read it as `c.VehicleID` (no `()` — it *looks* like a variable, but it's a method).
- `@Registration.setter` — the setter for the SAME name. You write `c.Registration = "XY61 ABC"` and Python quietly calls the setter.
- No setter pair = read-only property. That's the textbook's *"only where attribute values are to be changed"* in action.

> 💡 **Friendly reminder:** Properties and Get/Set pairs do the *same* job two different ways. Paper 4 accepts *either* — unless the question explicitly says "use @property". Just don't mix both styles in one answer.

---

# Part 2: Instantiation & Method Calls 🚀

> **TL;DR:** `Car("ABC1234", 2500)` *is* the constructor call. It builds the object and hands you back the keys.

> **When exam asks:** *"Write program code to declare and initialise two instances"* **→ Write this:**

```python
# Instantiation: ClassName(args) runs __init__ and returns the object
ThisCar = Car("ABC1234", 2500)          # memory reserved, constructor runs
ThisCar.SetPurchasePrice(12000)         # setter call: object.method(args)
print(ThisCar.GetVehicleID())           # getter call: returns value

# Two birds (9618_w25_qp_42 Q1b pattern)
bird1 = Bird("Cockatiel", 71.0)         # example — see Bird class in Part 9
bird2 = Bird("Macaw", 56.0)

# Five board objects (9618_w25_qp_43 Q1 pattern) — individual variables
Object1 = BoardObject("A", 2)
Object2 = BoardObject("B", 3)
# OR store in array/list (9618_w24 pattern)
Group = []
Group.append(BoardObject("A", 2))
Group.append(BoardObject("B", 3))
```

**Language mapping (you must READ Java/VB but WRITE Python):**

| Task | Python | Java | VB.NET |
|------|--------|------|--------|
| Instantiate | `ThisCar = Car("ABC1234", 2500)` | `Car thisCar = new Car("ABC1234", 2500);` | `Dim ThisCar As New Car("ABC1234", 2500)` |
| Call setter | `ThisCar.SetPurchasePrice(12000)` | `thisCar.setPurchasePrice(12000);` | `ThisCar.SetPurchasePrice(12000)` |
| Call getter | `print(ThisCar.GetVehicleID())` | `System.out.print(thisCar.getVehicleID());` | `Console.WriteLine(ThisCar.GetVehicleID())` |

> **Exam tip:** `Car("ABC1234", 2500)` LOOKS like a function call — it IS the constructor call. The `new` keyword only exists in Java/C#, not Python.

---

# Part 3: Inheritance — Base Class, Subclass, super() 🧬

> **TL;DR:** Write the shared stuff once in a base class. Subclasses inherit it for free, then add their own twist.

## 3.1 The Idea

Design a **base class** (superclass) once, then **derive** subclasses that automatically get ALL attributes/methods of the base and add their own. Subclass = "is a kind of" base.

| Term | Meaning |
|------|---------|
| **Base class / superclass** | Class others are derived from (parent) |
| **Subclass / derived class** | Class derived from base (child) — inherits everything |
| **Inheritance** | Attributes + methods of base are copied to subclass |
| **Abstract class** | Base class NEVER instantiated directly (e.g. LibraryItem — you only create Book or CD) |

## 3.2 Base Class — LibraryItem (Worked Example 27.02)

```python
import datetime

class LibraryItem:
    """Base class: everything true about EVERY library item. Abstract in spirit."""
    def __init__(self, t, a, i):
        self.__Title = t
        self.__AuthorArtist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()

    def GetTitle(self):       return self.__Title
    def GetAuthorArtist(self): return self.__AuthorArtist
    def GetItemID(self):      return self.__ItemID
    def GetOnLoan(self):      return self.__OnLoan
    def GetDueDate(self):     return self.__DueDate

    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)  # 3 weeks loan

    def Returning(self):
        self.__OnLoan = False

    def PrintDetails(self):
        print(self.__Title, ",", self.__AuthorArtist, ",")
        print(self.__ItemID, ",", self.__OnLoan, ",", self.__DueDate)
```

## 3.3 Subclasses — Book and CD

> **When exam asks:** *"Define subclass Book that inherits from LibraryItem and adds IsRequested"* **→ Write this:**

```python
class Book(LibraryItem):
    """Subclass: a LibraryItem that can also be requested."""
    def __init__(self, t, a, i):
        super().__init__(t, a, i)          # ← CALL BASE CONSTRUCTOR (preferred modern form)
        # Alternative book style: LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False          # book-specific attribute

    def GetIsRequested(self):
        return self.__IsRequested
    def SetIsRequested(self):
        self.__IsRequested = True

class CD(LibraryItem):
    """Subclass: a LibraryItem that carries a genre."""
    def __init__(self, t, a, i):
        super().__init__(t, a, i)
        self.__Genre = ""

    def GetGenre(self):       return self.__Genre
    def SetGenre(self, g):    self.__Genre = g
```

**Line-by-line (subclass constructor):**
- `class Book(LibraryItem):` — Python spells "inherits from" as parent name in brackets. Java: `class Book extends LibraryItem`, VB: `Class Book : Inherits LibraryItem`.
- `super().__init__(t, a, i)` — calls the BASE constructor so Title/AuthorArtist/ItemID/OnLoan/DueDate are set up by code you wrote ONCE, not copied. Must do this BEFORE adding subclass-specific attributes.
- `self.__IsRequested = False` — after base part is built, add own attributes. Note: private attrs of base (`__Title`) are NOT directly accessible in subclass — use getters.

> **When exam asks to choose between `super().__init__()` and `LibraryItem.__init__(self, ...)`:** Both are correct in Python. `super().__init__(...)` is the modern preferred form and matches the `super` keyword in Java pseudocode. The textbook shows the explicit `LibraryItem.__init__(self, ...)` form — either gets full marks.

## 3.4 Using Subclass Objects

```python
ThisBook = Book("Computing", "Sylvia", 1234)   # one call → two constructors run
ThisCD = CD("Let It Be", "The Beatles", 2345)

ThisBook.Borrowing()                  # inherited — works even though Book never defined it
ThisBook.SetIsRequested()
print(ThisBook.GetTitle())            # inherited getter
print(ThisBook.GetIsRequested())      # book-specific
ThisCD.SetGenre("Rock")
print(ThisCD.GetGenre())              # CD-specific
print(ThisCD.GetDueDate())            # inherited
```

### Task 27.03 — Borrower Class

```python
class Borrower:
    def __init__(self, name, email, borrower_id):
        self.__BorrowerName = name
        self.__EmailAddress = email
        self.__BorrowerID = borrower_id
        self.__ItemsOnLoan = 0          # starts at 0, as required

    def GetBorrowerName(self):  return self.__BorrowerName
    def GetEmailAddress(self):  return self.__EmailAddress
    def GetBorrowerID(self):    return self.__BorrowerID
    def GetItemsOnLoan(self):   return self.__ItemsOnLoan
    def UpdateItemsOnLoan(self, n):
        self.__ItemsOnLoan = self.__ItemsOnLoan + n   # +2 for borrow, -1 for return
    def PrintDetails(self):
        print(self.__BorrowerName, self.__EmailAddress, self.__BorrowerID, self.__ItemsOnLoan)

b = Borrower("Ada Lovelace", "ada@college.example", 7)
b.UpdateItemsOnLoan(2)    # borrows two → 2
b.UpdateItemsOnLoan(-1)   # returns one → 1
```

> ⚠️ **Heads-up — coursebook typos:** the printed code has `melf.__Title`, `Libraryltem`, `weeks-3`, `self.__OnLoan - False`. If you copy it verbatim, it crashes. The version above is fixed — write *that* in the exam. The mark scheme won't forgive the book's typos.

---

# Part 4: Polymorphism & Overriding 🔄

> **TL;DR:** Same method name, different behaviour. One loop can call `PrintDetails()` on every item — each class knows what to print.

**Polymorphism** = same method name, DIFFERENT behaviour per class. "Poly" = many, "morph" = form — many forms, one name.

Here's the problem it solves: the base `PrintDetails()` only knows about base attributes. But a Book also needs to show `IsRequested`, and a CD needs `Genre`. The answer? **Redefine** `PrintDetails` in each subclass with the *same* identifier. Then Python picks the right version at runtime.

> **When exam asks:** *"The method PrintDetails() is polymorphic / is overridden in each subclass"* **→ Write same method name in subclass, optionally calling base version:**

```python
class BookPoly(LibraryItem):
    def __init__(self, t, a, i):
        super().__init__(t, a, i)
        self.__IsRequested = False

    def GetIsRequested(self): return self.__IsRequested
    def SetIsRequested(self): self.__IsRequested = True

    def PrintDetails(self):                     # SAME name as base → polymorphism
        print("Book Details")
        super().PrintDetails()                  # call base version (reuses shared printing)
        print("IsRequested:", self.GetIsRequested())

class CDPoly(LibraryItem):
    def __init__(self, t, a, i):
        super().__init__(t, a, i)
        self.__Genre = ""
    def GetGenre(self): return self.__Genre
    def SetGenre(self, g): self.__Genre = g

    def PrintDetails(self):                     # SAME name → polymorphism
        print("CD Details")
        super().PrintDetails()
        print("Genre:", self.GetGenre())
```

**Why call base method instead of retyping?** Reuse. If shared printing changes (date format), you change ONE place and every subclass picks it up. Completely rewriting is allowed but duplicates code.

**The payoff — one loop, different behaviour:**

```python
def display_all(items):
    for item in items:
        item.PrintDetails()        # polymorphic call: Python checks actual class at runtime
        print("-----")

shelf = []
shelf.append(BookPoly("Computing", "Sylvia", 1234))
shelf.append(CDPoly("Let It Be", "The Beatles", 2345))
display_all(shelf)
# Output:
# Book Details / Computing , Sylvia , / 1234 , False , <date> / IsRequested: False
# -----
# CD Details / Let It Be , The Beatles , / 2345 , False , <date> / Genre:
# -----
```

> ⚠️ **Common mistake → fix:** Your subclass method *must* have the exact same name as the base. If you write `PrintBookDetails` instead of `PrintDetails`, it's not polymorphism — `item.PrintDetails()` will keep calling the base version and your extra attribute will never print.

| Language | Override marker | Call base version |
|----------|----------------|-------------------|
| Python | No keyword — just same name | `super().PrintDetails()` or `LibraryItem.PrintDetails(self)` |
| Java | `@Override` above method | `super.printDetails();` |
| VB.NET | `Overridable` on base, `Overrides` on subclass | `MyBase.PrintDetails()` |

### Full Library Evolution (Tasks 27.05-27.07) — borrower tracking + requesting

```python
class LibraryItemFull:
    def __init__(self, t, a, i):
        self.__Title = t; self.__AuthorArtist = a; self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()
        self.__BorrowerID = 0            # NEW: who has it (0 = nobody)
    def GetTitle(self): return self.__Title
    def GetAuthorArtist(self): return self.__AuthorArtist
    def GetItemID(self): return self.__ItemID
    def GetOnLoan(self): return self.__OnLoan
    def GetDueDate(self): return self.__DueDate
    def GetBorrowerID(self): return self.__BorrowerID
    def Borrowing(self, borrower_id):
        self.__OnLoan = True; self.__BorrowerID = borrower_id
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)
    def Returning(self):
        self.__OnLoan = False; self.__BorrowerID = 0
    def PrintDetails(self):
        print(self.__Title, ",", self.__AuthorArtist, ",")
        print(self.__ItemID, ",", self.__OnLoan, ",", self.__DueDate, ", borrower:", self.__BorrowerID)

class BookFull(LibraryItemFull):
    def __init__(self, t, a, i):
        super().__init__(t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = 0
    def GetIsRequested(self): return self.__IsRequested
    def GetRequestedBy(self): return self.__RequestedBy
    def SetIsRequested(self, borrower_id):
        self.__IsRequested = True; self.__RequestedBy = borrower_id
    def PrintDetails(self):
        print("Book Details")
        super().PrintDetails()
        print("IsRequested:", self.__IsRequested, "RequestedBy:", self.__RequestedBy)

class CDFull(LibraryItemFull):
    def __init__(self, t, a, i):
        super().__init__(t, a, i)
        self.__Genre = ""
    def GetGenre(self): return self.__Genre
    def SetGenre(self, g): self.__Genre = g
    def PrintDetails(self):
        print("CD Details")
        super().PrintDetails()
        print("Genre:", self.__Genre)
```

---

# Part 5: Containment (Aggregation) — "Has-A" 🧱

> **TL;DR:** Inheritance is "is a kind of" — containment is "has a". A Course *has* Lessons. A LibraryItem *is not* a Lesson.

Inheritance = "is a kind of" (Book IS a LibraryItem).
Containment = "has a" (Course HAS Lessons, Course HAS an Assessment, Car HAS Wheels).

> **When exam asks:** *"Class Course contains Lesson objects (up to 50) and one Assessment"* **→ Containment: Course stores OTHER objects as attributes:**

```python
class Lesson:
    """Component class: a single lesson inside a Course."""
    def __init__(self, t, d, r):
        self.__LessonTitle = t
        self.__DurationMinutes = d
        self.__RequiresLab = r
    def OutputLessonDetails(self):
        return f"{self.__LessonTitle}, {self.__DurationMinutes} mins, lab: {self.__RequiresLab}"

class Assessment:
    """Component class: the end-of-course assessment."""
    def __init__(self, t, m):
        self.__AssessmentTitle = t
        self.__MaxMarks = m
    def OutputAssessmentDetails(self):
        return f"{self.__AssessmentTitle}, max marks {self.__MaxMarks}"

class Course:
    """Container: CONTAINS Lesson objects + one Assessment. Has-a relationship."""
    def __init__(self, t, m):
        self.__CourseTitle = t
        self.__MaxStudents = m
        self.__NumberOfLessons = 0
        self.__CourseLesson = []           # list to hold Lesson objects
        self.__CourseAssessment = None     # not set until AddAssessment

    def AddLesson(self, t, d, r):
        self.__NumberOfLessons += 1
        self.__CourseLesson.append(Lesson(t, d, r))   # build component INSIDE container

    def AddAssessment(self, t, m):
        self.__CourseAssessment = Assessment(t, m)

    def OutputCourseDetails(self):
        print(self.__CourseTitle, "Maximum number:", self.__MaxStudents)
        for i in range(self.__NumberOfLessons):
            print(self.__CourseLesson[i].OutputLessonDetails())

# When exam asks: test the containment
MyCourse = Course("Computing", 10)
MyCourse.AddAssessment("Programming", 100)
MyCourse.AddLesson("Problem Solving", 60, False)
MyCourse.AddLesson("Programming", 120, True)
MyCourse.AddLesson("Theory", 60, False)
MyCourse.OutputCourseDetails()
```

**Inheritance vs Containment — exam decision table:**

| Question phrasing | Relationship | Code |
|-------------------|-------------|------|
| "X is a kind of Y" (Book is a LibraryItem) | **Inheritance** | `class Book(LibraryItem):` |
| "X has a Y" / "X contains Y" (Course has Lessons) | **Containment** | `self.__CourseLesson.append(Lesson(...))` |
| "X has up to 50 X" | Containment with a list | `self.__items = []` + `append` |
| "X has one Y" | Containment single | `self.__assessment = Assessment(...)` |

---

# Part 6: Arrays/Lists of Objects + File Persistence 📦

> **TL;DR:** In Python, a list *is* your array. Fill it with objects, loop it, pickle it to disk, read it back.

## 6.1 List of Objects

> **When exam says:** *"The program stores data in a 1D array of Node objects"* or *"Declare Group as array of EventItem"* **→ In Python use a list:**

```python
# Declare array — Python: list replaces fixed-size array
Group = []                          # was: DECLARE Group : ARRAY[1:5] OF EventItem

# Create + store objects (9618_w24 pattern: 5 EventItems)
Group.append(EventItem("Bridge", "jump", 3))
Group.append(EventItem("Water wade", "swim", 4))
Group.append(EventItem("100 mile run", "run", 5))
Group.append(EventItem("Gridlock", "drive", 2))
Group.append(EventItem("Wall on wall", "jump", 4))

# Instantiate into fixed slots (9618_w22 Character pattern: 10 characters from file)
Characters = [None] * 10            # array of 10 — fill from file
# OR build dynamically (safer if count varies)
Characters = []                     # start empty, append as you read

# Polymorphic list — holds mixed subclasses (Book + CD together)
shelf = []
shelf.append(BookPoly("Computing", "Sylvia", 1234))
shelf.append(CDPoly("Let It Be", "The Beatles", 2345))
for item in shelf:
    item.PrintDetails()             # works for both — polymorphism
    if isinstance(item, BookPoly):  # type check when you need subclass-specific behaviour
        print("  -> it's a Book, requested:", item.GetIsRequested())
```

> **Trap:** `[CarRecord() for i in range(100)]` builds 100 INDEPENDENT objects. `[CarRecord()] * 100` copies the SAME object 100 times — changing one changes all. Examiner trap in Ch.26/27 crossover.

## 6.2 File Persistence of Objects (Ch.26 crossover)

> **When exam says:** *"Read Characters.txt and create Character objects"* or *"Write objects to file and read them back"* **→ Two patterns:**

**Pattern A — text file, fields per line (9618_w22 Characters.txt: name, X, Y each on own line):**
```python
# File format: Amal\n0\n2\nBen\n3\n4\n...
Characters = []
with open("Characters.txt") as f:
    lines = f.read().splitlines()
i = 0
while i + 2 < len(lines):
    Characters.append(Character(lines[i], int(lines[i+1]), int(lines[i+2])))
    i += 3
```

**Pattern B — binary pickle (whole objects, Ch.26 sequential file):**
```python
import pickle

# SAVE list of objects
with open("CarFile.DAT", "wb") as f:
    for car in Cars:
        pickle.dump(car, f)           # PUTRECORD

# RESTORE list of objects (EOFError is the Python EOF() equivalent)
Cars = []
with open("CarFile.DAT", "rb") as f:
    try:
        while True:
            Cars.append(pickle.load(f))   # GETRECORD
    except EOFError:
        pass                              # normal end-of-file
```

**Garbage collection note (exam Q):**
- Python: interpreter manages private heap automatically — programmer does no housekeeping.
- Java/VB: garbage collector reclaims memory from objects no longer referenced.
- If objects never release memory → **memory leakage** → program runs out of memory.

---

# Part 7: Pseudocode ↔ Python Mapping 🗺️

> **TL;DR:** You need to *read* pseudocode and *write* Python. This table is your decoder ring. (Source: Cambridge Pseudocode Guide 2021, Ch. 10.)

You must READ pseudocode on theory papers and may WRITE in pseudocode OR Python on practical papers. This table is your decoder:

| Concept | Cambridge Pseudocode | Python | Java |
|---------|---------------------|--------|------|
| **Class declaration** | `CLASS Car ... ENDCLASS` | `class Car:` | `class Car { ... }` |
| **Private attribute** | `PRIVATE VehicleID : STRING` | `self.__VehicleID` + `# VehicleID : STRING` comment | `private String vehicleID;` |
| **Public method** | `PUBLIC FUNCTION GetVehicleID() RETURNS STRING` | `def GetVehicleID(self):` | `public String getVehicleID()` |
| **Constructor** | `PUBLIC PROCEDURE NEW(n : STRING, e : INTEGER)` | `def __init__(self, n, e):` | `public Car(String n, int e)` (same name as class) |
| **Inheritance** | `CLASS Book INHERITS LibraryItem` | `class Book(LibraryItem):` | `class Book extends LibraryItem` |
| **Call base constructor** | `SUPER.NEW(t, a, i)` | `super().__init__(t, a, i)` | `super(t, a, i);` |
| **Instantiation** | `DECLARE ThisCar : Car` / `ThisCar ← NEW Car("ABC1234", 2500)` | `ThisCar = Car("ABC1234", 2500)` | `Car thisCar = new Car("ABC1234", 2500);` |
| **Method call** | `CALL ThisCar.SetPurchasePrice(12000)` | `ThisCar.SetPurchasePrice(12000)` | `thisCar.setPurchasePrice(12000);` |
| **Containment** | `PRIVATE CourseLesson : ARRAY[1:50] OF Lesson` | `self.__CourseLesson = []` + `append(Lesson(...))` | `private Lesson[] courseLesson;` |
| **Overriding** | Redefine method with SAME name in subclass | `def PrintDetails(self):` (same name) | `@Override public void printDetails()` |
| **End of class** | `ENDCLASS` | Indentation ends class | `}` |

> **When exam asks:** *"Write the pseudocode declaration for OwnerName as PRIVATE"* (9618_s22_qp_32 Q3c) **→ Answer:** `PRIVATE OwnerName : STRING` — exact case, colon, type.

---

# Part 8: Inheritance Diagram Convention 📐

> **TL;DR:** Base on top, subclasses below. Dash = private (`-`), plus = public (`+`). Labels earn the marks — not pretty boxes.

> **When exam asks:** *"Draw the inheritance diagram"* or *"Complete the class diagram"* **→ Use these rules:**

**Textbook convention (safe for exam):**

```
        LibraryItem
        /         \
     Book          CD
```

- Base class at TOP, subclasses branch BELOW.
- Accepted alternative: UML triangle arrow from subclass TO base class (both get marks, textbook p.466 shows both).
- **Class diagram** (different from inheritance diagram): three boxes — top = class name, middle = attributes with `-` (private) + type, bottom = methods with `+` (public). Example:

```
+------------------------------------+
|                Car                 |
+------------------------------------+
| - VehicleID          : STRING      |
| - Registration       : STRING      |
| - DateOfRegistration : DATE        |
| - EngineSize         : INTEGER     |
| - PurchasePrice      : CURRENCY    |
+------------------------------------+
| + Constructor()                    |
| + SetPurchasePrice()               |
| + SetRegistration()                |
| + GetVehicleID()                   |
| + GetEngineSize()                  |
| + GetPurchasePrice()               |
+------------------------------------+
```

- `-` before attribute = **private**. `+` before method = **public**. Attributes ALWAYS private; methods ALWAYS public in diagrams.
- Write EXACT identifier names + data types from question — marks come from labels, not pretty boxes.
- No setter for fixed attributes → diagram shows only getters for those.

---

# Part 9: Exam Question Patterns — One Section Per Past-Paper Pattern 🎯

> **TL;DR:** Ten patterns cover almost every Paper 4 OOP question. Spot the stem → copy the skeleton → change the names.

Each pattern: **source → what examiner wants → mark scheme tip → code skeleton.**

---

### Pattern 1 — Declare class + constructor (private attributes)

**Sources:** 9618_w24_qp_42 Q1(a)(i) EventItem [4], 9618_w22_qp_42 Q2(a) Character [4], 9618_w25_qp_43 Q1(a)(i) BoardObject [5], 9618_w25_qp_42 Q1(a) Bird [4]

**Stem (paraphrased):** *"The class EventItem stores EventName:STRING, EventType:STRING, Difficulty:INTEGER. Write code to declare the class and its constructor. All attributes must be private. If writing in Python, include attribute declarations using comments. Do not declare other methods."*

**Mark scheme tip:** 1 mark per private attribute with correct type + comment, 1 mark for constructor header with parameters, 1 mark for assigning parameters to `self.__attr` (not hardcoded values).

> **When exam asks this → Write:**

```python
class EventItem:
    # EventName : STRING
    # EventType : STRING
    # Difficulty : INTEGER
    def __init__(self, p_name, p_type, p_difficulty):
        self.__EventName = p_name
        self.__EventType = p_type
        self.__Difficulty = p_difficulty
```

```python
# BoardObject variant (9618_w25_qp_43)
class BoardObject:
    # Code : STRING
    # Value : INTEGER
    def __init__(self, p_code, p_value):
        self.__Code = p_code
        self.__Value = p_value

# Bird variant
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
```

---

### Pattern 2 — Getters (and sometimes setters)

**Sources:** 9618_w24_qp_42 Q1(a)(ii) [3], 9618_w22_qp_42 Q2(b) Character [3], 9618_w25_qp_43 Q1(a)(ii) BoardObject [3]

**Stem:** *"The methods GetName() and GetDifficulty() return the appropriate attribute. Write program code for these methods."*

**Mark scheme tip:** 1 mark per getter with correct name, no parameter (other than self), and `return self.__Attr`.

> **When exam asks this → Write:**

```python
class EventItem:
    # ... constructor above ...
    def GetName(self):
        return self.__EventName
    def GetEventType(self):
        return self.__EventType
    def GetDifficulty(self):
        return self.__Difficulty

# BoardObject getters (note: GetCode/GetValue per 9618_w25_qp_43)
class BoardObject:
    # ... constructor ...
    def GetCode(self):
        return self.__Code
    def GetValue(self):
        return self.__Value
```

```python
# Setter example (when setter needed)
class Character:
    def __init__(self, name, x, y):
        self.__Name = name
        self.__XCoordinate = x
        self.__YCoordinate = y
    def GetName(self): return self.__Name
    def GetX(self):    return self.__XCoordinate
    def GetY(self):    return self.__YCoordinate
    def ChangePosition(self, x_change, y_change):
        self.__XCoordinate = self.__XCoordinate + x_change
        self.__YCoordinate = self.__YCoordinate + y_change
    def SetIntelligence(self, v):     # setter with validation (9618_w23_qp_42 pattern)
        if 0 <= v <= 100:
            self.__Intelligence = v
```

---

### Pattern 3 — Instantiate objects into an array/list

**Sources:** 9618_w24_qp_42 Q1(b)(ii) Group [3], 9618_w25_qp_43 Q1(a)(iii) 5 BoardObjects [3], 9618_w25_qp_42 Q1(b) 2 Birds [3]

**Stem:** *"One group has five events (table given). Write code to create an instance of EventItem for each and store them in Group."* / *"Create two Birds: Cockatiel 71.0, Macaw 56.0."*

**Mark scheme tip:** 1 mark for declaring array/list, 1 mark per correct instantiation with correct argument order.

> **When exam asks this → Write:**

```python
# 9618_w24 pattern: named Group, 5 EventItems in given order
Group = []
Group.append(EventItem("Bridge", "jump", 3))
Group.append(EventItem("Water wade", "swim", 4))
Group.append(EventItem("100 mile run", "run", 5))
Group.append(EventItem("Gridlock", "drive", 2))
Group.append(EventItem("Wall on wall", "jump", 4))

# 9618_w25_qp_43 pattern: 5 specific variables
Object1 = BoardObject("A", 2)
Object2 = BoardObject("B", 3)
Object3 = BoardObject("C", 5)
Object4 = BoardObject("D", 2)
Object5 = BoardObject("E", 7)

# 9618_w25_qp_42 pattern: two Birds
Bird1 = Bird("Cockatiel", 71.0)
Bird2 = Bird("Macaw", 56.0)
```

---

### Pattern 4 — Method with logic (CalculateScore / Move / Success)

**Sources:** 9618_w24_qp_42 Q1(d) CalculateScore [4], 9618_w25_qp_42 Q1(a)(iv) Bird.Move [5], 9618_w24_qp_43 Horse.Success [4]

**Stem (CalculateScore, paraphrased):** *"When skill >= difficulty, return 100. Otherwise difference = difficulty - skill: 1→80, 2→60, 3→40, otherwise 20."*

> **When exam asks CalculateScore → Write:**

```python
class Character:
    def __init__(self, p_name, p_jump, p_swim, p_run, p_drive):
        self.__CharacterName = p_name
        self.__Jump = p_jump; self.__Swim = p_swim
        self.__Run = p_run;   self.__Drive = p_drive

    def CalculateScore(self, event_type, difficulty):
        if event_type == "jump":  skill = self.__Jump
        elif event_type == "swim": skill = self.__Swim
        elif event_type == "run":  skill = self.__Run
        else:                     skill = self.__Drive  # "drive"
        if skill >= difficulty:
            return 100
        difference = difficulty - skill
        if difference == 1:  return 80
        elif difference == 2: return 60
        elif difference == 3: return 40
        else:                return 20
```

**Stem (Bird.Move, paraphrased):** *"Move() takes direction (N/S/E/W) and hours (REAL). Updates XPosition/YPosition by DistancePerHour × hours."*

> **When exam asks Bird.Move → Write:**

```python
class Bird:
    # ... constructor with __DistancePerHour, __XPosition, __YPosition ...
    def Move(self, direction, hours):
        distance = self.__DistancePerHour * hours
        if direction == "N":    self.__YPosition += distance
        elif direction == "S":  self.__YPosition -= distance
        elif direction == "E":  self.__XPosition += distance
        elif direction == "W":  self.__XPosition -= distance
```

---

### Pattern 5 — File → array of objects + search loop

**Sources:** 9618_w22_qp_42 Q2(d)(e)(f) Characters.txt [7+5+7 marks]

**Stem (paraphrased):** *"Characters.txt stores 10 characters: each has Name, XCoordinate, YCoordinate (each on its own line). Write code to read the file and store in a 1D array of Character objects. Then allow searching by name (case-insensitive, retry until found) and moving by A/W/S/D with validation."*

> **When exam asks file → objects → search → move → output → Write:**

```python
# (d) Read file into array of objects
Characters = []
with open("Characters.txt") as f:
    lines = f.read().splitlines()
i = 0
while i + 2 < len(lines):
    Characters.append(Character(lines[i], int(lines[i+1]), int(lines[i+2])))
    i += 3

# (e) Search by name with retry (case-insensitive, scripted — input() in exam)
def find_character(characters, name_inputs):
    index = -1
    for j in range(len(characters)):
        if characters[j].GetName().upper() == name_inputs[0].upper():
            index = j
    k = 1
    while index == -1 and k < len(name_inputs):
        test = name_inputs[k]; k += 1
        for j in range(len(characters)):
            if characters[j].GetName().upper() == test.upper():
                index = j
        if index == -1:
            print("Name not found:", test)
    return index

# (f) Validate direction, then move via method
def apply_move(character, direction_inputs):
    direction = direction_inputs[0]; m = 1
    while direction not in ("A","W","S","D") and m < len(direction_inputs):
        print("Invalid direction:", direction)
        direction = direction_inputs[m]; m += 1
    if direction == "A":   character.ChangePosition(-1, 0)
    elif direction == "D": character.ChangePosition(1, 0)
    elif direction == "W": character.ChangePosition(0, 1)
    else:                  character.ChangePosition(0, -1)  # S

# (g) Output via getters only (not direct attr access)
# print(char.GetName(), "has changed coordinates to X =", char.GetX(), "and Y =", char.GetY())
```

---

### Pattern 6 — Inheritance diagram / class diagram

**Sources:** 9618 Theory papers (32) + practical context; 9618_s22_qp_32 Q3 BuildingRecord→BuildingClass; textbook Fig 27.02/27.03

**Stem:** *"Draw the inheritance diagram for LibraryItem, Book, CD."* / *"Complete the class diagram for BuildingClass (all properties PRIVATE)."* / *"Write the declaration for OwnerName as PRIVATE."*

> **When exam asks inheritance diagram → Draw:**

```
        LibraryItem
        /         \
     Book          CD
```

> **When exam asks class diagram → Draw three-section box with `-` for private attrs, `+` for public methods, with types.**

> **When exam asks pseudocode PRIVATE declaration → Write:** `PRIVATE OwnerName : STRING`

---

### Pattern 7 — Polymorphic loop / scoring loop

**Sources:** 9618_w24_qp_42 Q1(e) Tarz vs Geni scoring [7]; textbook display_all / menu

**Stem (paraphrased):** *"Two characters Tarz (5,3,5,1) and Geni (2,2,3,4) attempt every event in Group. For each event call CalculateScore; award 1 point to winner, 0 for draw. Output per-event winner and overall group winner."*

> **When exam asks polymorphic scoring loop → Write:**

```python
p1 = Character("Tarz", 5, 3, 5, 1)
p2 = Character("Geni", 2, 2, 3, 4)
p1_points = 0; p2_points = 0
for event in Group:
    s1 = p1.CalculateScore(event.GetEventType(), event.GetDifficulty())
    s2 = p2.CalculateScore(event.GetEventType(), event.GetDifficulty())
    if s1 > s2:
        p1_points += 1; print(p1.GetName(), "wins", event.GetName())
    elif s2 > s1:
        p2_points += 1; print(p2.GetName(), "wins", event.GetName())
    else:
        print(event.GetName(), "is a draw")
if p1_points > p2_points:
    print(p1.GetName(), "wins the group with", p1_points, "points")
elif p2_points > p1_points:
    print(p2.GetName(), "wins the group with", p2_points, "points")
else:
    print("The group is a draw")
```

---

### Pattern 8 — Containment (Course/Lesson/Assessment)

**Source:** Textbook Worked Example 27.03 + exam variants (Car/Engine, Node/Data)

**Stem (paraphrased):** *"A Course contains up to 50 Lessons and one Assessment. Write the Course class with AddLesson, AddAssessment, and OutputCourseDetails."*

> **When exam asks containment → Write pattern from Part 5 above** (Course with `self.__CourseLesson = []` and `self.__CourseAssessment = None`, building component objects inside `AddLesson`/`AddAssessment`).

---

### Pattern 9 — Pseudocode ↔ Python class conversion (Theory)

**Source:** 9618_s22_qp_32 Q3c + Pseudocode Guide Ch.10

**Stem:** *"The record BuildingRecord is changed to class BuildingClass. Properties: BuildingID, BuildingGroup, OwnerName, BuildingAddress, DateLastSold, PriceLastSold. All PRIVATE. Write the declaration for OwnerName as PRIVATE. Explain why PRIVATE."*

> **Answer:** `PRIVATE OwnerName : STRING` — **Why:** Encapsulation; prevents direct access, forces use of getters/setters where validation/controlled access is possible, makes code robust and reusable.

---

### Pattern 10 — Instantiation + method call in main program

**Source:** Every Paper 4 practical (evidence.doc pattern)

**Stem:** *"Write program code for the main program to declare, instantiate, and use objects. Save as Question1_N24 / evidence."*

**Mark scheme tip:** Marks for correct constructor call with correct argument order, correct method call syntax (`object.Method(args)`), and correct output via getters.

> **When exam asks main program → Write:**

```python
# Declare + instantiate
ThisBook = Book("Computing", "Sylvia", 1234)
ThisCD = CD("Let It Be", "The Beatles", 2345)
# Use via methods
ThisBook.Borrowing()
ThisBook.SetIsRequested()
print(ThisBook.GetTitle(), ThisBook.GetOnLoan(), ThisBook.GetIsRequested())
ThisCD.SetGenre("Rock")
print(ThisCD.GetGenre())
# Polymorphic display
for item in [ThisBook, ThisCD]:
    item.PrintDetails()
```

---

# Part 10: Common Traps & Quick Reference ⚠️

> **TL;DR:** The examiner has seen every mistake before. This is your checklist to dodge them.

## 10.1 Top Traps — how to dodge them 🙂 (Examiner Report Highlights)

| Trap | What happens | Fix |
|------|-------------|-----|
| Hardcoded constructor values | `self.__Name = "Amal"` instead of `= p_name` | Always assign PARAMETER to attribute |
| Forgetting `self` | `def GetName():` → TypeError | Every method: `def GetName(self):` |
| Single underscore private | `self._Name` not treated as private | Use `self.__Name` (double underscore) |
| Getter with setter name confusion | `def SetName` that returns value | Getter = returns, Setter = assigns + may validate |
| Extra setter for fixed attr | Adding `SetVehicleID` when question says "never changes" | No setter for fixed attrs |
| Wrong method name for polymorphism | `PrintBookDetails` vs `PrintDetails` | EXACT same name as base |
| Forgetting `super().__init__` | Subclass attrs work but base attrs missing/default | First line of subclass `__init__`: `super().__init__(...)` |
| `[Obj()] * 100` | One object copied 100 times | Use `[Obj() for _ in range(100)]` |
| `open` without `close` / `with` | File locked, data lost | Use `with open(...) as f:` |
| Java constructor in Python | `def Car(self, ...)` | In Python it is ALWAYS `__init__` |
| Python constructor in Java | `__init__` in Java answer | In Java it is SAME NAME as class |
| Case-insensitive search | `if name == stored` fails for "qui" vs "Qui" | Use `.upper()` on both sides |

## 10.2 Quick Reference — Every Key Term in One Place 📖

| Term | One-line definition |
|------|---------------------|
| **Class** | Type combining data + methods (blueprint) |
| **Object** | Instance of a class |
| **Instance** | Specific object created from a class |
| **Attributes** | Data items of a class (fields), always private |
| **Methods** | Subroutines of a class, always public |
| **Encapsulation** | Bundling data + methods and restricting external access to data |
| **Constructor** | Special method (`__init__` in Python) that instantiates object + initialises attributes |
| **Getter** | Public method that reads/returns an attribute |
| **Setter** | Public method that changes an attribute (may validate) |
| **Property** | Class member bundling attribute with getter/setter (`@property` in Python) |
| **Instantiation** | Creating an object from a class (memory reserved) |
| **Private** | Accessible only through class's methods (`__` in Python, `PRIVATE` in pseudocode) |
| **Public** | Callable from anywhere (default for methods in Python) |
| **Inheritance** | All attrs + methods of base are copied to subclass |
| **Base / superclass** | Class subclasses are derived from |
| **Subclass / derived** | Class derived from a base (has everything base has + extras) |
| **Abstract class** | Base never instantiated directly (template for subclasses) |
| **Polymorphism** | Same method name behaves differently per class (`PrintDetails` in LibraryItem/Book/CD) |
| **Containment (aggregation)** | Has-a: one class has component of another class type (Course HAS Lessons) |
| **Overriding** | Redefining a base method in a subclass with same identifier (how polymorphism is implemented) |
| **Memory leakage** | Running out of memory because unneeded objects never release theirs |
| **Garbage collection** | Automatic reclamation of memory from objects no longer referenced |

## 10.3 At-a-Glance: Which Pattern for Which Question? 🔍

| Exam phrase | Pattern to write |
|-------------|-----------------|
| "Declare the class and its constructor. All attributes private." | Pattern 1 shape → `class X: # attrs : TYPE` + `__init__` assigning params |
| "Write code for GetName()" | Pattern 2 → `def GetName(self): return self.__Name` |
| "Create instances and store in Group / array" | Pattern 3 → `Group.append(ClassName(args))` or `Obj1 = ClassName(...)` |
| "CalculateScore / Move / Success logic" | Pattern 4 → read table, map difference/condition to return values |
| "Read file and create objects" | Pattern 5 → `with open(...)` + `splitlines()` + `append(ClassName(...))` + search/retry loop |
| "Draw inheritance / class diagram" | Pattern 6 → tree with base on top + `-/+` signs + types |
| "Polymorphic loop / score every event" | Pattern 7 → `for event in Group: s1 = p1.CalculateScore(...)` + points |
| "Course contains Lessons" | Pattern 8 → `self.__list = []` + `AddLesson` builds component |
| "PRIVATE declaration / why private" | Pattern 9 → `PRIVATE OwnerName : STRING` + encapsulation reason |
| "Main program uses objects" | Pattern 10 → `obj = Class(args)` + `obj.Method()` + `print(obj.GetX())` |

---

## Sources Used — where every pattern comes from 📚 (Past Papers Mined)

- **9618_w22_qp_42 Q2** Character (Name, XCoordinate, YCoordinate) — constructor [4], getters [3], ChangePosition [2], file→objects [7], name search [5], direction validation [7], formatted output [2].
- **9618_w24_qp_42 Q1** EventItem (EventName, Type, Difficulty) + Character (Jump/Swim/Run/Drive) — declare class [4], getters [3], Group instantiation [3], Character with CalculateScore [4+4], Tarz vs Geni scoring loop [7].
- **9618_w25_qp_42 Q1** Bird (DistancePerHour, Species, XPosition, YPosition) — constructor [4], Move(direction, hours) [5], instantiate 2 Birds [3].
- **9618_w25_qp_43 Q1** BoardObject (Code, Value) — declare class+constructor [5], GetCode/GetValue [3], instantiate 5 objects [3].
- **9618_w24_qp_43 Q2** Horse (Name, MaxFenceHeight, PercentageSuccess) — constructor/getters/Success() pattern.
- **9618_s22_qp_32 Q3** BuildingRecord → BuildingClass — PRIVATE declaration [1], why PRIVATE [2].
- **9618_w25_qp_41 Q2** Train (TrainIDNumber, Route) — constructor/getters pattern.
- Textbook 27.01-27.07 Car, Company, LibraryItem/Book/CD, Borrower, Course/Lesson/Assessment — all worked examples + class/inheritance diagrams.

> Textbook pseudocode rules: *Cambridge International AS & A Level Computer Science Pseudocode Guide (2021)* Chapter 10 — Object-Oriented Programming.
