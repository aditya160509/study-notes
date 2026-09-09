"""
A Level CS 9618 — Chapter 27: Object-Oriented Programming (OOP) 🧩
Companion runnable code for chapter-27-oop-notes.md (1114 lines, friendly tone)

Your code-first revision companion — every pattern is runnable Python.
Each section tells you **when the exam asks X, write Y** so you know exactly what to type.
Run: python3 ~/Documents/Codex/computer-science/chapter-27-oop-notes.py
No input() — everything is scripted with tempfile so it runs unattended.
"""

import datetime
import pickle
import tempfile
import os

# =============================================================
# WHAT THIS CHAPTER IS (and Why OOP Exists) 💡
#  TL;DR: Procedural leaves data lying around. OOP locks it in a box and hands you one key — a method.
# =============================================================
print("=" * 60)
print("WHAT THIS CHAPTER IS — Why OOP Exists  💡")
print("  TL;DR: Procedural = data lying around. OOP = data in a safe, methods are the only door.")
print("=" * 60)
print("Procedural (Ch.14/26): records + separate procedures — anyone can corrupt them.")
print("OOP: attributes (private, __) + methods (public) bundled = encapsulation.")
print("  Class  = cookie cutter (template)        |  Object = one cookie")
print("  Attributes = data items, ALWAYS private  |  Methods = things object can do, ALWAYS public")
print("  Instantiation = baking a cookie          |  Encapsulation = data in safe, one door")
print("Why it matters to you: with SetPurchasePrice(price > 0 check) ONE place guards every change. ✅")
print()

# =============================================================
# PART 1: CLASS BASICS — Private Attributes, Constructor, Getters & Setters  🔧
#  TL;DR: One class shape does 80% of the work — private __attrs, __init__ using params, getter for
#         everything, setter ONLY when value is meant to change.
#  MD §1.1 The Standard 9618 Class Shape | §1.2 Constructor Rules | §1.3 Getters/Setters
#         | §1.4 @property  |  Bad vs Good  |  Task 27.01 Company
# =============================================================
print("=" * 60)
print("PART 1: CLASS BASICS — Private Attributes, Constructor, Getters & Setters  🔧")
print("  TL;DR: One shape does 80% of the work — private __attrs, __init__ with params,")
print("  getter for everything, setter only when value changes.")
print("=" * 60)

# -------------------------------------------------------------
# 1.1 The Standard 9618 Class Shape — When exam asks:
#    "Write program code to declare the class X and its constructor. All attributes must be private."
#    → Write this exact shape, renamed.
# -------------------------------------------------------------
print("--- 1.1 Standard 9618 shape — your exam template (rename and go) ---")

class Car:
    """9618 standard shape: private attrs, constructor, getters, setters."""
    # VehicleID : STRING
    # Registration : STRING
    # EngineSize : INTEGER
    # PurchasePrice : CURRENCY
    def __init__(self, n, e):
        # Constructor: runs automatically when you write Car(...)
        # When exam asks X → write Y: VehicleID/EngineSize known at manufacture → set from params
        #                              Registration/PurchasePrice not known yet → placeholder
        self.__VehicleID = n             # known at manufacture
        self.__Registration = ""         # not known yet → "" for STRING
        self.__EngineSize = e            # known at manufacture
        self.__PurchasePrice = 0.00      # not known yet → 0.00 for CURRENCY

    # ----- getters: ONE for EVERY attribute (every stored value needs a window) -----
    def GetVehicleID(self):
        return self.__VehicleID
    def GetRegistration(self):
        return self.__Registration
    def GetEngineSize(self):
        return self.__EngineSize
    def GetPurchasePrice(self):
        return self.__PurchasePrice

    # ----- setters: ONLY for attributes that change after creation (doors you actually need) -----
    def SetRegistration(self, r):
        self.__Registration = r
    def SetPurchasePrice(self, p):
        if p > 0:                        # validation lives HERE — one gate, one place
            self.__PurchasePrice = p

print("Car class declared — VehicleID/EngineSize from params, Registration/PurchasePrice as placeholders.")
print("  When exam asks private attrs → write self.__Name (double underscore) + '# Name : TYPE' comment")
print()

# Line-by-line demo — what you're telling Python
print("--- Car in action — getters give you a window, setters are the door ---")
ThisCar = Car("ABC1234", 2500)
ThisCar.SetPurchasePrice(12000)
ThisCar.SetRegistration("XY61 ABC")
print("  ThisCar.GetVehicleID():", ThisCar.GetVehicleID(), "  ← getter, no param besides self")
print("  ThisCar.GetPurchasePrice():", ThisCar.GetPurchasePrice())
print("  Validation: SetPurchasePrice(-500) should be rejected...")
ThisCar.SetPurchasePrice(-500)
print("  After SetPurchasePrice(-500):", ThisCar.GetPurchasePrice(), "(rejected ✅)")
print("  No SetVehicleID() — VehicleID never changes, so no setter. Adding one = mark lost.")
print()

# Proper Car with Date attr — fixed subclass (replaces any lambda hack)
class CarFull(Car):
    """Extended Car with DateOfRegistration — proper subclass, no lambda tricks."""
    def __init__(self, n, e):
        super().__init__(n, e)
        self.__DateOfRegistration = None  # DATE → None placeholder
    def GetDateOfRegistration(self):
        return self.__DateOfRegistration
    def SetDateOfRegistration(self, d):
        self.__DateOfRegistration = d

cf = CarFull("ABC1234", 2500)
cf.SetPurchasePrice(12000)
cf.SetRegistration("XY61 ABC")
cf.SetDateOfRegistration(datetime.date(2026, 8, 1))
print("  CarFull:", cf.GetVehicleID(), "| EngineSize:", cf.GetEngineSize(),
      "| Reg:", cf.GetRegistration(), "| Price:", cf.GetPurchasePrice(),
      "| Date:", cf.GetDateOfRegistration())
cf.SetPurchasePrice(-500)
print("  After SetPurchasePrice(-500): Price still", cf.GetPurchasePrice(), "(rejected)")
print()

# -------------------------------------------------------------
# 1.2 Constructor Rules — the mark scheme is picky here ⚠️
# -------------------------------------------------------------
print("--- 1.2 Constructor rules — the mark scheme checklist (memorise these) ---")
rules = [
    ("Python constructor name", "def __init__(self, ...):", "Writing def Constructor = 0 marks"),
    ("Java constructor name", "public Car(String n, int e)  (same name as class)", "Mixing Java/Python names loses marks"),
    ("Every method needs self", "def GetX(self):", "Forgetting self = TypeError"),
    ("Private = __ prefix", "self.__Name", "self._Name (single _) is NOT private per mark scheme"),
    ("Python needs comment declarations", "# Name : STRING above __init__", "Mark scheme: 'include attribute declarations using comments'"),
    ("Use parameters, not hardcoded values", "self.__Name = p_name", 'self.__Name = "John" = mark lost (examiner report 2023)'),
]
for rule, correct, trap in rules:
    print(f"  {rule:32s} → {correct:55s}  Trap: {trap}")
print()

# -------------------------------------------------------------
# 1.3 Getters & Setters — When to Omit a Setter 🤔
#  In plain English: getter = window (see data), setter = door (change data).
#  You always need the window; you only add the door when change is meant to happen.
# -------------------------------------------------------------
print("--- 1.3 Getters & setters — window vs door ---")
print("  Getter for EVERY attribute — 'every attribute must be accessible or no point storing it' (p.461)")
print("  Setter ONLY for attributes that change AFTER instantiation.")
print("  Fixed attrs (VehicleID, CompanyName) → NO setter — that's what makes it robust.")
print("  When exam says 'CompanyName will NEVER change' → write NO SetCompanyName. Extra setter = contradiction.")
print()

# Bad vs Good encapsulation — see it fail and see it protected
print("--- Bad vs Good: why private + validated setter beats a public attribute ---")
class BadAccount:
    def __init__(self, bal):
        self.balance = bal  # PUBLIC — anyone can corrupt
class GoodAccount:
    def __init__(self, bal):
        self.__balance = bal  # PRIVATE — double underscore = locked
    def GetBalance(self):
        return self.__balance
    def SetBalance(self, v):
        if v >= 0:             # validation gate — bad data bounced here
            self.__balance = v

bad = BadAccount(100)
bad.balance = -5000
print("  BadAccount after bad.balance = -5000:", bad.balance, "← yikes, corrupted (public = anyone can break it)")
good = GoodAccount(100)
good.SetBalance(-5000)
print("  GoodAccount after SetBalance(-5000):", good.GetBalance(), "(protected ✅)")
try:
    good.__balance = -5000
    print("  Note: good.__balance = -5000 didn't error — it made a NEW public attr, not the private one!")
    print("  Real private still:", good.GetBalance(), "(name-mangled to _GoodAccount__balance)")
except AttributeError as e:
    print("  Direct access blocked:", e)
print("  When exam asks 'why PRIVATE?' → To achieve encapsulation — prevents direct modification,")
print("  forces access through methods where validation lives, makes code robust & reusable. ✅")
print()

# -------------------------------------------------------------
# Task 27.01 — Company Class (textbook, fully solved)
#  CompanyName and EmailAddress set by constructor and NEVER change → NO setters for them
# -------------------------------------------------------------
print("--- Task 27.01: Company — NO setter for CompanyName (it never changes!) ---")
class Company:
    # CompanyName : STRING
    # EmailAddress : STRING
    # DateLastContact : DATE
    def __init__(self, company_name, email_address):
        self.__CompanyName = company_name
        self.__EmailAddress = email_address
        self.__DateLastContact = None       # not known yet → None for DATE
    def GetCompanyName(self): return self.__CompanyName
    def GetEmailAddress(self): return self.__EmailAddress
    def GetDateLastContact(self): return self.__DateLastContact
    def SetDateLastContact(self, d): self.__DateLastContact = d
    # NOTE: no SetCompanyName / SetEmailAddress — they never change, so no setter!

supplier = Company("Acme Supplies", "sales@acme.example")
supplier.SetDateLastContact(datetime.date(2026, 8, 12))
print(" ", supplier.GetCompanyName(), "|", supplier.GetEmailAddress(), "|", supplier.GetDateLastContact())
print("  Notice: no SetCompanyName — CompanyName never changes, so no setter. That's intentional! ✅")
print("  When exam asks Company → declare 3 private attrs, getter for each, setter ONLY for DateLastContact.")
print()

# -------------------------------------------------------------
# 1.4 @property Version — the Pythonic Alternative ✨
#  When exam asks: "The question shows @property / @setter" or "write the class using properties"
#  → Use this form instead of Get/Set pairs. Paper 4 accepts EITHER unless told which.
# -------------------------------------------------------------
print("--- 1.4 @property: the Pythonic way — reads like a variable, still protected ✨ ---")
print("  TL;DR: @property turns a method into a getter (c.VehicleID, no brackets).")
print("         @X.setter is the setter (c.X = value calls the setter behind the scenes).")
print("         No setter pair = read-only. Don't mix Get/Set and @property in one answer.")
class CarProp:
    # VehicleID : STRING
    # Registration : STRING
    # EngineSize : INTEGER
    # PurchasePrice : CURRENCY
    def __init__(self, n, e):
        self.__VehicleID = n
        self.__Registration = ""
        self.__EngineSize = e
        self.__PurchasePrice = 0.00
    @property
    def VehicleID(self):               # getter — read as c.VehicleID (no brackets, looks like attr)
        return self.__VehicleID
    # NO @VehicleID.setter → read-only (never changes) ✅
    @property
    def EngineSize(self):
        return self.__EngineSize
    # no setter → read-only
    @property
    def Registration(self):
        return self.__Registration
    @Registration.setter
    def Registration(self, r):         # setter — write as c.Registration = "XY61 ABC"
        self.__Registration = r
    @property
    def PurchasePrice(self):
        return self.__PurchasePrice
    @PurchasePrice.setter
    def PurchasePrice(self, p):
        if p > 0:
            self.__PurchasePrice = p

c = CarProp("ABC1234", 2500)
c.PurchasePrice = 12000               # looks like assignment, goes through setter
c.Registration = "XY61 ABC"
print("  c.VehicleID:", c.VehicleID, " | c.EngineSize:", c.EngineSize, " | c.Registration:", c.Registration, "| c.PurchasePrice:", c.PurchasePrice)
print("  No brackets — reads like a variable, but it's a method under the hood.")
try:
    c.VehicleID = "NEW"
except AttributeError as e:
    print("  c.VehicleID = 'NEW' blocked (read-only):", e, "← no setter = can't change")
print("  Friendly reminder: @property and Get/Set do the same job two ways — pick one style per answer.")
print()

# =============================================================
# PART 2: INSTANTIATION & METHOD CALLS  🚀
#  TL;DR: Car("ABC1234", 2500) IS the constructor call. It builds the object and hands you the keys.
# =============================================================
print("=" * 60)
print("PART 2: INSTANTIATION & METHOD CALLS  🚀")
print("  TL;DR: Car(\"ABC1234\", 2500) IS the constructor call — it builds the object for you.")
print("=" * 60)

# When exam asks: "Write program code to declare and initialise two instances" → Write this:
print("--- Instantiation: baking cookies from the cutter (ClassName(args) runs __init__) ---")
car_a = Car("XYZ0001", 1600)
car_a.SetRegistration("AB12 CDE")
print("  car_a = Car('XYZ0001', 1600)  → memory reserved, __init__ runs")
print("  car_a.SetRegistration('AB12 CDE')  → setter call: object.method(args)")
print("  car_a.GetVehicleID():", car_a.GetVehicleID(), "  ← getter call: returns value")
print()

# BoardObject — full definition here for instantiation demo (also used in Part 9 patterns)
class BoardObject:
    # Code : STRING
    # Value : INTEGER
    def __init__(self, p_code, p_value):
        self.__Code = p_code
        self.__Value = p_value
    def GetCode(self): return self.__Code
    def GetValue(self): return self.__Value

Object1 = BoardObject("A", 2)
Object2 = BoardObject("B", 3)
print("  BoardObject — individual variables (9618_w25_qp_43 Q1 pattern: 5 BoardObjects):")
print("    Object1 = BoardObject('A', 2)  →", Object1.GetCode(), Object1.GetValue())
print("    Object2 = BoardObject('B', 3)  →", Object2.GetCode(), Object2.GetValue())
# OR store in array/list (9618_w24 pattern)
Group_demo = []
Group_demo.append(BoardObject("A", 2))
Group_demo.append(BoardObject("B", 3))
print("  OR list: Group.append(BoardObject('A', 2)) →", [(g.GetCode(), g.GetValue()) for g in Group_demo])
print()

# Bird — minimal for instantiation demo (full BirdFull in Part 9)
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
    def GetSpecies(self): return self.__Species
    def GetSpeed(self): return self.__DistancePerHour
    def Move(self, direction, hours):
        distance = self.__DistancePerHour * hours
        if direction == "N": self.__YPosition += distance
        elif direction == "S": self.__YPosition -= distance
        elif direction == "E": self.__XPosition += distance
        elif direction == "W": self.__XPosition -= distance
    def GetX(self): return self.__XPosition
    def GetY(self): return self.__YPosition

bird1 = Bird("Cockatiel", 71.0)       # 9618_w25_qp_42 Q1b pattern: two birds
bird2 = Bird("Macaw", 56.0)
print("  Two birds (9618_w25_qp_42 Q1b): Bird('Cockatiel',71.0) and Bird('Macaw',56.0)")
print("   ", bird1.GetSpecies(), bird1.GetSpeed(), "|", bird2.GetSpecies(), bird2.GetSpeed())
bird1.Move("N", 2)
print("  bird1.Move('N', 2): X =", bird1.GetX(), "Y =", bird1.GetY(), "← DistancePerHour(71) × hours(2)")
print()

# Language mapping — you must READ Java/VB but WRITE Python
print("--- Language mapping — you must READ Java/VB but WRITE Python ---")
hdr_task = "Task"; hdr_py = "Python"; hdr_jv = "Java"
print(f"  {hdr_task:20s} | {hdr_py:40s} | {hdr_jv:40s} | VB.NET")
inst_py = 'ThisCar = Car("ABC1234", 2500)'; inst_jv = 'Car thisCar = new Car("ABC1234", 2500);'
setter_py = 'ThisCar.SetPurchasePrice(12000)'; setter_jv = 'thisCar.setPurchasePrice(12000);'
getter_py = 'print(ThisCar.GetVehicleID())'; getter_jv = 'System.out.print(thisCar.getVehicleID());'
print(f"  {'Instantiate':20s} | {inst_py:40s} | {inst_jv:40s} | Dim ThisCar As New Car(\"ABC1234\", 2500)")
print(f"  {'Call setter':20s} | {setter_py:40s} | {setter_jv:40s} | ThisCar.SetPurchasePrice(12000)")
print(f"  {'Call getter':20s} | {getter_py:40s} | {getter_jv:40s} | Console.WriteLine(ThisCar.GetVehicleID())")
print("  Exam tip: Car('ABC1234', 2500) LOOKS like a function call — it IS the constructor. 'new' only in Java/C#, not Python.")
print()

# =============================================================
# PART 3: INHERITANCE — Base Class, Subclass, super()  🧬
#  TL;DR: Write the shared stuff once in a base class. Subclasses inherit it for free, then add their twist.
# =============================================================
print("=" * 60)
print("PART 3: INHERITANCE — LibraryItem, Book, CD, Borrower  🧬")
print("  TL;DR: Write shared stuff once (base), inherit for free (subclass).")
print("  Base/superclass = parent | Subclass/derived = child (\"is a kind of\") | Abstract = never instantiated alone")
print("=" * 60)

# 3.2 Base Class — LibraryItem (Worked Example 27.02)
print("--- 3.2 Base class LibraryItem — everything true about EVERY library item (abstract in spirit) ---")
class LibraryItem:
    """Base class: everything true about EVERY library item. Abstract in spirit."""
    # Title : STRING
    # AuthorArtist : STRING
    # ItemID : INTEGER
    # OnLoan : BOOLEAN
    # DueDate : DATE
    def __init__(self, t, a, i):
        self.__Title = t
        self.__AuthorArtist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()
    def GetTitle(self): return self.__Title
    def GetAuthorArtist(self): return self.__AuthorArtist
    def GetItemID(self): return self.__ItemID
    def GetOnLoan(self): return self.__OnLoan
    def GetDueDate(self): return self.__DueDate
    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)  # 3 weeks loan
    def Returning(self):
        self.__OnLoan = False
    def PrintDetails(self):
        print(self.__Title, ",", self.__AuthorArtist, ",")
        print(self.__ItemID, ",", self.__OnLoan, ",", self.__DueDate)

print("  LibraryItem(t,a,i): sets Title/AuthorArtist/ItemID, OnLoan=False, DueDate=today")
print("  Borrowing() → OnLoan=True, DueDate+3 weeks | Returning() → OnLoan=False")
print()

# 3.3 Subclasses — Book and CD
# When exam asks: "Define subclass Book that inherits from LibraryItem and adds IsRequested" → Write this:
print("--- 3.3 Subclasses Book and CD — \"is a kind of\" LibraryItem ---")
class Book(LibraryItem):
    """Subclass: a LibraryItem that can also be requested."""
    # Title, AuthorArtist, ItemID, OnLoan, DueDate inherited — don't redeclare!
    # IsRequested : BOOLEAN  (book-specific)
    def __init__(self, t, a, i):
        super().__init__(t, a, i)          # ← CALL BASE CONSTRUCTOR (preferred modern form)
        # Alternative book style: LibraryItem.__init__(self, t, a, i)  — also correct
        self.__IsRequested = False          # book-specific attribute
    def GetIsRequested(self):
        return self.__IsRequested
    def SetIsRequested(self):
        self.__IsRequested = True

class CD(LibraryItem):
    """Subclass: a LibraryItem that carries a genre."""
    # Genre : STRING  (CD-specific)
    def __init__(self, t, a, i):
        super().__init__(t, a, i)
        self.__Genre = ""
    def GetGenre(self):       return self.__Genre
    def SetGenre(self, g):    self.__Genre = g

print("  class Book(LibraryItem):  ← Python spells 'inherits from' as parent in brackets")
print("  Java: class Book extends LibraryItem  |  VB: Class Book : Inherits LibraryItem")
print("  super().__init__(t,a,i) must be FIRST line — builds base part before adding own attrs")
print("  Private attrs of base (__Title) NOT directly accessible in subclass — use getters")
print()

# 3.4 Using Subclass Objects
print("--- 3.4 Using subclass objects — inherited methods work even though Book never defined them ---")
ThisBook = Book("Computing", "Sylvia", 1234)   # one call → two constructors run
ThisCD = CD("Let It Be", "The Beatles", 2345)

ThisBook.Borrowing()                  # inherited — works even though Book never defined it
ThisBook.SetIsRequested()
print("  ThisBook.Borrowing()  (inherited) → OnLoan:", ThisBook.GetOnLoan(), " DueDate:", ThisBook.GetDueDate())
print("  ThisBook.GetTitle()   (inherited getter):", ThisBook.GetTitle())
print("  ThisBook.GetIsRequested() (book-specific):", ThisBook.GetIsRequested())
ThisCD.SetGenre("Rock")
print("  ThisCD.SetGenre('Rock') →", ThisCD.GetGenre(), "(CD-specific)")
print("  ThisCD.GetDueDate()   (inherited):", ThisCD.GetDueDate())
print()

# Alternative explicit base call (textbook style) — also correct
print("--- Both super().__init__() and LibraryItem.__init__(self, ...) get full marks ---")
class BookExplicit(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)  # textbook explicit form
        self.__IsRequested = False
    def GetIsRequested(self): return self.__IsRequested
    def SetIsRequested(self): self.__IsRequested = True
be = BookExplicit("Explicit Book", "Author", 9999)
print("  BookExplicit('Explicit Book','Author',9999):", be.GetTitle(), "| IsRequested:", be.GetIsRequested())
print("  When exam asks to choose: super().__init__(...) is modern preferred (matches Java 'super'),")
print("  but the textbook's LibraryItem.__init__(self,...) is also correct. Either gets marks.")
print()

# Task 27.03 — Borrower Class (standalone, no inheritance)
print("--- Task 27.03: Borrower — standalone class (no inheritance needed here) ---")
class Borrower:
    # BorrowerName : STRING
    # EmailAddress : STRING
    # BorrowerID : INTEGER
    # ItemsOnLoan : INTEGER
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
        self.__ItemsOnLoan = self.__ItemsOnLoan + n   # +1 for borrow, -1 for return
    def PrintDetails(self):
        print(self.__BorrowerName, self.__EmailAddress, self.__BorrowerID, self.__ItemsOnLoan)

b = Borrower("Ada Lovelace", "ada@college.example", 7)
print("  b = Borrower('Ada', 'ada@...', 7) → ItemsOnLoan:", b.GetItemsOnLoan())
b.UpdateItemsOnLoan(2)    # borrows two → 2
print("  b.UpdateItemsOnLoan(2) →", b.GetItemsOnLoan())
b.UpdateItemsOnLoan(-1)   # returns one → 1
print("  b.UpdateItemsOnLoan(-1) →", b.GetItemsOnLoan())
print()
print("  ⚠️ Coursebook typos fixed here: melf.__Title → self.__Title, Libraryltem → LibraryItem,")
print("     weeks-3 → weeks=3, self.__OnLoan - False → self.__OnLoan = False. Don't copy typos!")
print()

# =============================================================
# PART 4: POLYMORPHISM & OVERRIDING  🔄
#  TL;DR: Same method name, different behaviour. One loop can call PrintDetails() on every item —
#         each class knows what to print. Python picks the right version at runtime.
# =============================================================
print("=" * 60)
print("PART 4: POLYMORPHISM & OVERRIDING  🔄")
print("  TL;DR: Same name, different job. One loop handles every subclass — Python picks at runtime.")
print("  Polymorphism = poly(many) + morph(forms) — many forms, one name.")
print("=" * 60)

print("--- The problem polymorphism solves ---")
print("  Base PrintDetails() only knows base attrs. Book also needs IsRequested, CD needs Genre.")
print("  Answer: REDEFINE PrintDetails in each subclass with SAME identifier → overriding.")
print("  When exam asks: 'method PrintDetails() is polymorphic / overridden' → same name in subclass,")
print("                  optionally calling base version via super().PrintDetails()")
print()

class BookPoly(LibraryItem):
    def __init__(self, t, a, i):
        super().__init__(t, a, i)
        self.__IsRequested = False
    def GetIsRequested(self): return self.__IsRequested
    def SetIsRequested(self): self.__IsRequested = True
    def PrintDetails(self):                     # SAME name as base → polymorphism ✨
        print("Book Details")
        super().PrintDetails()                  # call base version (reuses shared printing)
        print("IsRequested:", self.GetIsRequested())

class CDPoly(LibraryItem):
    def __init__(self, t, a, i):
        super().__init__(t, a, i)
        self.__Genre = ""
    def GetGenre(self): return self.__Genre
    def SetGenre(self, g): self.__Genre = g
    def PrintDetails(self):                     # SAME name → polymorphism ✨
        print("CD Details")
        super().PrintDetails()
        print("Genre:", self.GetGenre())

print("  Why call base method? Reuse — if shared printing changes, change ONE place.")
print("  Completely rewriting without super() is allowed but duplicates code.")
print()

# The payoff — one loop, different behaviour
def display_all(items):
    """One loop, different behaviour per actual class — that's polymorphism in action."""
    for item in items:
        item.PrintDetails()        # polymorphic call: Python checks actual class at runtime
        print("-----")

print("--- The payoff — one loop, different behaviour (polymorphic loop) ---")
shelf = []
shelf.append(BookPoly("Computing", "Sylvia", 1234))
shelf.append(CDPoly("Let It Be", "The Beatles", 2345))
shelf[1].SetGenre("Rock")
display_all(shelf)
print("  shelf holds BOTH BookPoly and CDPoly — one loop called the RIGHT PrintDetails each time. ✅")
print()

# Common mistake
print("--- Common mistake → fix ---")
print("  If you write PrintBookDetails instead of PrintDetails → NOT polymorphism.")
print("  item.PrintDetails() will still call base version, extra attr never prints. Must be EXACT same name.")
print()

# isinstance checks — when you need subclass-specific behaviour
print("--- When you need to know WHICH subclass you have → isinstance ---")
for item in shelf:
    if isinstance(item, BookPoly):
        print(f"  -> Book '{item.GetTitle()}' requested={item.GetIsRequested()}")
    elif isinstance(item, CDPoly):
        print(f"  -> CD '{item.GetTitle()}' genre={item.GetGenre()}")
print("  Use isinstance only when you need subclass-specific methods; otherwise plain polymorphic loop is cleaner.")
print()

# Language override table
print("--- Override in each language ---")
print(f"  {'Language':10s} | {'Override marker':30s} | {'Call base version'}")
print(f"  {'Python':10s} | {'No keyword — just same name':30s} | super().PrintDetails() or LibraryItem.PrintDetails(self)")
print(f"  {'Java':10s} | {'@Override above method':30s} | super.printDetails();")
print(f"  {'VB.NET':10s} | {'Overridable on base, Overrides on subclass':30s} | MyBase.PrintDetails()")
print()

# Full Library Evolution (Tasks 27.05-27.07) — borrower tracking + requesting
print("--- Full Library Evolution (Tasks 27.05-27.07) — now tracking WHO borrowed what ---")
class LibraryItemFull:
    # Title, AuthorArtist, ItemID, OnLoan, DueDate + NEW: BorrowerID
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

print("  LibraryItemFull now stores BorrowerID; BookFull stores RequestedBy — evolution without breaking base.")
print()

# Scripted menu (Tasks 27.07) — no input() so it runs unattended
print("--- Scripted run_menu session — textbook menu without typing (choices are scripted) ---")
def run_menu(choices):
    """Textbook menu loop — scripted choices so no input() needed. Codes: 1=add borrower, 2=add book, 3=add CD, 4/6=borrow, 5/7=return, 8=request, 9=print all."""
    borrowers = []
    items = []
    def find_borrower(borrower_id):
        for b in borrowers:
            if b.GetBorrowerID() == borrower_id:
                return b
        return None
    def find_item(item_id):
        for it in items:
            if it.GetItemID() == item_id:
                return it
        return None
    for choice in choices:
        code = choice[0]
        if code == 1:
            b = Borrower(choice[1], choice[2], choice[3])
            borrowers.append(b)
            print("  Borrower added:", choice[1])
        elif code == 2:
            items.append(BookFull(choice[1], choice[2], choice[3]))
            print("  Book added:", choice[1])
        elif code == 3:
            items.append(CDFull(choice[1], choice[2], choice[3]))
            print("  CD added:", choice[1])
        elif code in (4, 6):  # borrow book / CD
            item = find_item(choice[1]); borrower = find_borrower(choice[2])
            if item is not None and borrower is not None:
                if not item.GetOnLoan():
                    item.Borrowing(choice[2]); borrower.UpdateItemsOnLoan(1)
                    print("  Item", choice[1], "borrowed by", choice[2])
                else:
                    print("  Item", choice[1], "already on loan")
            else:
                print("  Item or borrower not found")
        elif code in (5, 7):  # return
            item = find_item(choice[1])
            if item is not None and item.GetOnLoan():
                borrower = find_borrower(item.GetBorrowerID())
                item.Returning()
                if borrower is not None:
                    borrower.UpdateItemsOnLoan(-1)
                print("  Item", choice[1], "returned")
            else:
                print("  Item", choice[1], "not on loan")
        elif code == 8:  # request book
            item = find_item(choice[1])
            if item is not None and isinstance(item, BookFull):
                item.SetIsRequested(choice[2])
                print("  Book", choice[1], "requested by", choice[2])
        elif code == 9:  # print all
            for b in borrowers: b.PrintDetails()
            for it in items: it.PrintDetails()
    return borrowers, items

session = [
    (1, "Ada", "ada@college.example", 7),
    (1, "Grace", "grace@college.example", 8),
    (2, "Computing", "Sylvia", 1234),
    (3, "Let It Be", "The Beatles", 2345),
    (4, 1234, 7),   # Ada borrows book 1234
    (8, 1234, 8),   # Grace requests book 1234
    (6, 2345, 8),   # Grace borrows CD 2345
    (5, 1234, 7),   # Ada returns book 1234
    (9,),           # print all
]
print("  Session: add 2 borrowers, add book+CD, borrow, request, borrow CD, return, print all")
borrowers, items = run_menu(session)
print(f"  Done — Borrowers: {len(borrowers)} | Items: {len(items)}")
# Verify polymorphic display still works on evolved classes
print("  Polymorphic display on evolved classes:")
display_all(items)
print()

# =============================================================
# PART 5: CONTAINMENT (Aggregation) — "Has-A"  🧱
#  TL;DR: Inheritance is "is a kind of" — containment is "has a". A Course HAS Lessons.
# =============================================================
print("=" * 60)
print("PART 5: CONTAINMENT (Aggregation) — \"Has-A\"  🧱")
print("  TL;DR: Inheritance = \"is a kind of\" (Book IS a LibraryItem).")
print("         Containment = \"has a\" (Course HAS Lessons, Course HAS an Assessment).")
print("=" * 60)

# When exam asks: "Class Course contains Lesson objects (up to 50) and one Assessment"
# → Containment: Course stores OTHER objects as attributes:
print("--- Component classes — the pieces that will live INSIDE a Course ---")
class Lesson:
    """Component class: a single lesson inside a Course."""
    # LessonTitle : STRING
    # DurationMinutes : INTEGER
    # RequiresLab : BOOLEAN
    def __init__(self, t, d, r):
        self.__LessonTitle = t
        self.__DurationMinutes = d
        self.__RequiresLab = r
    def OutputLessonDetails(self):
        return f"{self.__LessonTitle}, {self.__DurationMinutes} mins, lab: {self.__RequiresLab}"
    def GetTitle(self): return self.__LessonTitle

class Assessment:
    """Component class: the end-of-course assessment."""
    # AssessmentTitle : STRING
    # MaxMarks : INTEGER
    def __init__(self, t, m):
        self.__AssessmentTitle = t
        self.__MaxMarks = m
    def OutputAssessmentDetails(self):
        return f"{self.__AssessmentTitle}, max marks {self.__MaxMarks}"
    def GetTitle(self): return self.__AssessmentTitle

class Course:
    """Container: CONTAINS Lesson objects + one Assessment. Has-a relationship."""
    # CourseTitle : STRING
    # MaxStudents : INTEGER
    # NumberOfLessons : INTEGER
    # CourseLesson : ARRAY[1:50] OF Lesson  (list in Python)
    # CourseAssessment : Assessment
    def __init__(self, t, m):
        self.__CourseTitle = t
        self.__MaxStudents = m
        self.__NumberOfLessons = 0
        self.__CourseLesson = []           # list to hold Lesson objects (up to 50)
        self.__CourseAssessment = None     # not set until AddAssessment
    def AddLesson(self, t, d, r):
        # In exam you might guard: if self.__NumberOfLessons < 50:
        self.__NumberOfLessons += 1
        self.__CourseLesson.append(Lesson(t, d, r))   # build component INSIDE container
    def AddAssessment(self, t, m):
        self.__CourseAssessment = Assessment(t, m)
    def OutputCourseDetails(self):
        print(self.__CourseTitle, "Maximum number:", self.__MaxStudents)
        for i in range(self.__NumberOfLessons):
            print(self.__CourseLesson[i].OutputLessonDetails())
        if self.__CourseAssessment is not None:
            print(self.__CourseAssessment.OutputAssessmentDetails())
    def GetTitle(self): return self.__CourseTitle
    def GetAssessment(self): return self.__CourseAssessment
    def GetLessonCount(self): return self.__NumberOfLessons

print("  Lesson(t,d,r) and Assessment(t,m) are independent classes — later COURSed inside Course.")
print()

print("--- Container in action — Course HAS Lessons + an Assessment ---")
MyCourse = Course("Computing", 10)
MyCourse.AddAssessment("Programming", 100)
MyCourse.AddLesson("Problem Solving", 60, False)
MyCourse.AddLesson("Programming", 120, True)
MyCourse.AddLesson("Theory", 60, False)
MyCourse.OutputCourseDetails()
print(f"  ✅ Course '{MyCourse.GetTitle()}' has {MyCourse.GetLessonCount()} lessons + assessment: {MyCourse.GetAssessment().OutputAssessmentDetails()}")
print()

print("--- Inheritance vs Containment — exam decision table (spot the phrasing → pick the pattern) ---")
print(f"  {'Question phrasing':40s} | {'Relationship':20s} | Code")
print(f"  {'X is a kind of Y (Book is a LibraryItem)':40s} | {'Inheritance':20s} | class Book(LibraryItem):")
print(f"  {'X has a Y / contains Y (Course has Lessons)':40s} | {'Containment':20s} | self.__CourseLesson.append(Lesson(...))")
print(f"  {'X has up to 50 X':40s} | {'Containment with list':20s} | self.__items = [] + append")
print(f"  {'X has one Y':40s} | {'Containment single':20s} | self.__assessment = Assessment(...)")
print("  When exam asks containment → build component objects INSIDE AddLesson/AddAssessment, store in list.")
print()

# =============================================================
# PART 6: ARRAYS/LISTS OF OBJECTS + FILE PERSISTENCE  📦
#  TL;DR: In Python, a list IS your array. Fill it with objects, loop it, pickle it to disk, read it back.
# =============================================================
print("=" * 60)
print("PART 6: ARRAYS/LISTS OF OBJECTS + FILE PERSISTENCE  📦")
print("  TL;DR: Python list IS your array — fill it with objects, loop it, pickle it.")
print("=" * 60)

# 6.1 Lists of objects — every variant you'll meet
print("--- 6.1 Lists of objects — every flavour in Paper 4 ---")
print("  When exam says 'stores data in 1D array of Node objects' or 'DECLARE Group : ARRAY[1:5] OF EventItem' → list in Python")

# Fixed-size style: [None]*N then fill
FixedCars = [None] * 3
FixedCars[0] = Car("CAR001", 1600)
FixedCars[1] = Car("CAR002", 1800)
FixedCars[2] = Car("CAR003", 2000)
print("  Fixed-size: [None]*3 then FixedCars[0]=Car(...) →", [c.GetVehicleID() for c in FixedCars])

# Dynamic: append (safer if count varies)
DynamicCars = []
for vid, eng in [("CAR001", 1600), ("CAR002", 1800), ("CAR003", 2000)]:
    DynamicCars.append(Car(vid, eng))
print("  Dynamic: Group=[] + Group.append(Car(...)) →", [c.GetVehicleID() for c in DynamicCars])

# Polymorphic list with isinstance
poly_shelf = [BookPoly("Book A", "Auth A", 1), CDPoly("CD B", "Artist B", 2)]
print("  Polymorphic list — mixed subclasses together (Book + CD):")
for item in poly_shelf:
    if isinstance(item, BookPoly):
        print(f"    Book: {item.GetTitle()}  (isinstance → BookPoly)")
    elif isinstance(item, CDPoly):
        print(f"    CD: {item.GetTitle()}  (isinstance → CDPoly)")
    item.PrintDetails()
    print("    ---")

# The comprehension vs multiplication trap
print("  ⚠️ Trap: [Car('X',100)]*3 shares ONE object; [Car('X',100) for _ in range(3)] makes 3 independent")
shared = [Car("SHARED", 100)] * 3
print("    shared[0] is shared[1]:", shared[0] is shared[1], "← same object — mutating one mutates all (bug)")
independent = [Car("IND", 100) for _ in range(3)]
print("    independent[0] is independent[1]:", independent[0] is independent[1], "← different objects — correct ✅")
print()

# 6.2 File persistence — Ch.26 crossover
print("--- 6.2 File persistence — two patterns (text file + binary pickle) ---")
print("  When exam says 'Read Characters.txt and create Character objects' → Pattern A (text file)")
print("  When exam says 'Write objects to file and read them back' → Pattern B (pickle)")
# Simulate Characters.txt via temp file (no external dependency, no input())
with tempfile.TemporaryDirectory() as tmp:
    chars_path = os.path.join(tmp, "Characters.txt")
    with open(chars_path, "w") as f:
        f.write("Amal\n0\n2\nBen\n3\n4\nCara\n1\n1\nDan\n5\n5\nEma\n2\n0\n"
                "Far\n4\n3\nGil\n0\n5\nHana\n3\n1\nIvo\n5\n2\nQui\n4\n0\n")

    # Character class for file demo (matches 9618_w22_qp_42 Q2)
    class CharacterFile:
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

    # Pattern A — text file, fields per line (9618_w22 Characters.txt: name, X, Y each on own line)
    # File format: Amal\n0\n2\nBen\n3\n4\n...
    Characters = []
    with open(chars_path) as f:
        lines = f.read().splitlines()
    i = 0
    while i + 2 < len(lines):
        Characters.append(CharacterFile(lines[i], int(lines[i+1]), int(lines[i+2])))
        i += 3
    print(f"  Pattern A — text file: loaded {len(Characters)} characters →", [c.GetName() for c in Characters])

    # Pattern B — binary pickle (whole objects, Ch.26 sequential file)
    print("  Pattern B — binary pickle (whole objects, PUTRECORD / GETRECORD):")
    pickle_path = os.path.join(tmp, "CarFile.DAT")
    Cars = [Car(f"CAR{i:03d}", 1000 + i*100) for i in range(3)]
    with open(pickle_path, "wb") as f:
        for car in Cars:
            pickle.dump(car, f)           # PUTRECORD
    print("    Saved 3 Cars via pickle.dump (PUTRECORD)")
    # RESTORE — EOFError is the Python EOF() equivalent
    Restored = []
    with open(pickle_path, "rb") as f:
        try:
            while True:
                Restored.append(pickle.load(f))   # GETRECORD
        except EOFError:
            pass                              # normal end-of-file (EOF() in pseudocode)
    print("    Restored via pickle.load until EOFError (EOF):", [c.GetVehicleID() for c in Restored])

    # Also demo: array of EventItem style that reuses Group from Pattern 3
    print("  Characters array search prep — ready for Pattern 5's case-insensitive search loop.")
print()

# Garbage collection note (exam Q)
print("--- Garbage collection — who tidies up memory? (exam loves this) ---")
print("  Python: interpreter manages private heap automatically — programmer does no housekeeping.")
print("  Java/VB: garbage collector reclaims memory from objects no longer referenced.")
print("  If objects never release memory → memory leakage → program runs out of memory.")
print()

# =============================================================
# PART 7: PSEUDOCODE ↔ PYTHON MAPPING  🗺️  (your decoder ring)
#  TL;DR: You need to READ pseudocode and WRITE Python. This is your decoder.
#  Source: Cambridge Pseudocode Guide 2021, Ch. 10
# =============================================================
print("=" * 60)
print("PART 7: PSEUDOCODE ↔ PYTHON MAPPING  🗺️")
print("  TL;DR: READ pseudocode on theory papers, WRITE Python on practical — here's the decoder.")
print("=" * 60)
print("  You must READ pseudocode and may WRITE in pseudocode OR Python on practical papers.")
# Full table matching MD Part 7
mapping = [
    ("Class declaration", "CLASS Car ... ENDCLASS", "class Car:", "class Car { ... }"),
    ("Private attribute", "PRIVATE VehicleID : STRING", "self.__VehicleID + '# VehicleID : STRING' comment", "private String vehicleID;"),
    ("Public method", "PUBLIC FUNCTION GetVehicleID() RETURNS STRING", "def GetVehicleID(self):", "public String getVehicleID()"),
    ("Constructor", "PUBLIC PROCEDURE NEW(n : STRING, e : INTEGER)", "def __init__(self, n, e):", "public Car(String n, int e)  (same name as class)"),
    ("Inheritance", "CLASS Book INHERITS LibraryItem", "class Book(LibraryItem):", "class Book extends LibraryItem"),
    ("Call base constructor", "SUPER.NEW(t, a, i)", "super().__init__(t, a, i)", "super(t, a, i);"),
    ("Instantiation", "DECLARE ThisCar : Car / ThisCar ← NEW Car(\"ABC1234\", 2500)", "ThisCar = Car(\"ABC1234\", 2500)", "Car thisCar = new Car(\"ABC1234\", 2500);"),
    ("Method call", "CALL ThisCar.SetPurchasePrice(12000)", "ThisCar.SetPurchasePrice(12000)", "thisCar.setPurchasePrice(12000);"),
    ("Containment", "PRIVATE CourseLesson : ARRAY[1:50] OF Lesson", "self.__CourseLesson = [] + append(Lesson(...))", "private Lesson[] courseLesson;"),
    ("Overriding", "Redefine method with SAME name in subclass", "def PrintDetails(self):  (same name)", "@Override public void printDetails()"),
    ("End of class", "ENDCLASS", "Indentation ends class", "}"),
]
print(f"  {'Concept':22s} | {'Cambridge Pseudocode':45s} | {'Python':42s} | Java")
print("  " + "-" * 160)
for concept, pseudo, py, java in mapping:
    print(f"  {concept:22s} | {pseudo:45s} | {py:42s} | {java}")
print()
print("  When exam asks: 'Write pseudocode declaration for OwnerName as PRIVATE' (9618_s22_qp_32 Q3c)")
print("  → Answer: PRIVATE OwnerName : STRING  (exact case, colon, type) — see Pattern 9.")
print()

# =============================================================
# PART 8: INHERITANCE DIAGRAM CONVENTION  📐  (base on top, subclasses below)
#  TL;DR: Base on top, subclasses below. Dash = private (-), plus = public (+). Labels earn marks.
# =============================================================
print("=" * 60)
print("PART 8: INHERITANCE DIAGRAM  📐")
print("  TL;DR: Base on top, subclasses below. Dash = private (-), plus = public (+). Labels earn marks.")
print("=" * 60)
print("  When exam asks: 'Draw the inheritance diagram' or 'Complete the class diagram' → use these rules:")
print()
print("  Textbook convention (safe for exam):")
print("""
        LibraryItem
        /         \\
     Book          CD
""")
print("  - Base class at TOP, subclasses branch BELOW.")
print("  - Accepted alternative: UML triangle arrow from subclass TO base class (both get marks, p.466).")
print("  - Class diagram (different from inheritance diagram): three boxes —")
print("    top = class name, middle = attributes with '-' (private) + type, bottom = methods with '+' (public).")
print("""
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
""")
print("  - '-' before attribute = private. '+' before method = public. Attrs ALWAYS private; methods ALWAYS public.")
print("  - Write EXACT identifier names + data types from question — marks come from labels, not pretty boxes.")
print("  - No setter for fixed attrs → diagram shows only getters for those.")
print()

# =============================================================
# PART 9: EXAM QUESTION PATTERNS — One Section Per Past-Paper Pattern  🎯
#  TL;DR: Ten patterns cover almost every Paper 4 OOP question. Spot the stem → copy the skeleton → change names.
#  Each pattern: source → what examiner wants → mark scheme tip → code skeleton (runnable).
# =============================================================
print("=" * 60)
print("PART 9: EXAM QUESTION PATTERNS — 10 patterns, all runnable  🎯")
print("  TL;DR: Ten patterns cover almost every Paper 4 OOP question.")
print("  Spot the stem → copy the skeleton → swap the names. You've got this.")
print("=" * 60)

# -------------------------------------------------------------
# Pattern 1 — Declare class + constructor (private attributes)
# Sources: 9618_w24_qp_42 Q1(a)(i) EventItem [4], 9618_w22_qp_42 Q2(a) Character [4],
#          9618_w25_qp_43 Q1(a)(i) BoardObject [5], 9618_w25_qp_42 Q1(a) Bird [4]
# Stem: "The class EventItem stores EventName:STRING, EventType:STRING, Difficulty:INTEGER.
#        Write code to declare the class and its constructor. All attributes must be private."
# Mark scheme: 1 mark per private attr with correct type + comment, 1 for constructor header with params,
#              1 for assigning params to self.__attr (not hardcoded).
# When exam asks this → Write:
# -------------------------------------------------------------
print("--- Pattern 1: Declare class + constructor (private attributes) ---")
print("  Sources: 9618_w24_qp_42 Q1(a)(i) EventItem [4], 9618_w22_qp_42 Q2(a) Character [4],")
print("           9618_w25_qp_43 Q1(a)(i) BoardObject [5], 9618_w25_qp_42 Q1(a) Bird [4]")
print("  Stem: 'EventItem stores EventName:STRING, EventType:STRING, Difficulty:INTEGER.")
print("         Write code to declare class and constructor. All attributes private. Include comments in Python.'")
print("  When exam asks this → Write class with '# Attr : TYPE' comments + __init__ assigning params (NOT hardcoded):")
class EventItem:
    # EventName : STRING
    # EventType : STRING
    # Difficulty : INTEGER
    def __init__(self, p_name, p_type, p_difficulty):
        self.__EventName = p_name          # ← uses parameter, not "Bridge"
        self.__EventType = p_type
        self.__Difficulty = p_difficulty
    def GetName(self): return self.__EventName
    def GetEventType(self): return self.__EventType
    def GetDifficulty(self): return self.__Difficulty

# BoardObject variant (9618_w25_qp_43)
class BoardObjectFull:
    # Code : STRING
    # Value : INTEGER
    def __init__(self, p_code, p_value):
        self.__Code = p_code
        self.__Value = p_value
    def GetCode(self): return self.__Code
    def GetValue(self): return self.__Value

# Bird variant (9618_w25_qp_42)
class BirdFull:
    # DistancePerHour : REAL
    # Species : STRING
    # XPosition : REAL
    # YPosition : REAL
    def __init__(self, p_species, p_speed):
        self.__Species = p_species
        self.__DistancePerHour = p_speed
        self.__XPosition = 0.0              # starts at origin
        self.__YPosition = 0.0
    def GetSpecies(self): return self.__Species
    def GetSpeed(self): return self.__DistancePerHour
    def GetX(self): return self.__XPosition
    def GetY(self): return self.__YPosition
    def Move(self, direction, hours):
        distance = self.__DistancePerHour * hours
        if direction == "N": self.__YPosition += distance
        elif direction == "S": self.__YPosition -= distance
        elif direction == "E": self.__XPosition += distance
        elif direction == "W": self.__XPosition -= distance

print("  EventItem('Bridge','jump',3):", EventItem("Bridge", "jump", 3).GetName(), EventItem("Bridge","jump",3).GetDifficulty(), "← param→attr, not hardcoded")
print("  BoardObject('A',2):", BoardObjectFull("A",2).GetCode(), BoardObjectFull("A",2).GetValue())
print("  Bird('Cockatiel',71.0):", BirdFull("Cockatiel",71.0).GetSpecies(), BirdFull("Cockatiel",71.0).GetSpeed())
print("  Mark scheme tip: 1 mark per private attr+type+comment, 1 for constructor header, 1 for param→attr assignment.")
print()

# -------------------------------------------------------------
# Pattern 2 — Getters (and sometimes setters)
# Sources: 9618_w24_qp_42 Q1(a)(ii) [3], 9618_w22_qp_42 Q2(b) Character [3], 9618_w25_qp_43 Q1(a)(ii) [3]
# Stem: "The methods GetName() and GetDifficulty() return appropriate attribute. Write code for these methods."
# Mark scheme: 1 mark per getter with correct name, no param (other than self), return self.__Attr
# When exam asks this → Write:
# -------------------------------------------------------------
print("--- Pattern 2: Getters (and setters when needed) ---")
print("  Sources: 9618_w24_qp_42 Q1(a)(ii) [3], 9618_w22_qp_42 Q2(b) [3], 9618_w25_qp_43 Q1(a)(ii) [3]")
print("  Stem: 'Methods GetName() and GetDifficulty() return the attribute. Write code for these methods.'")
print("  When exam asks this → Write: def GetName(self): return self.__EventName  (no param, correct case)")

# EventItem getters already shown above; extended example with BoardObject getters:
class BoardObjectWithGetters:
    # Code : STRING
    # Value : INTEGER
    def __init__(self, p_code, p_value):
        self.__Code = p_code; self.__Value = p_value
    def GetCode(self):
        return self.__Code
    def GetValue(self):
        return self.__Value
print("  BoardObject.GetCode():", BoardObjectWithGetters("A",2).GetCode(), " GetValue():", BoardObjectWithGetters("A",2).GetValue())

# Setter example with validation (when setter IS needed)
class CharacterWithSetter:
    # Name : STRING
    # XCoordinate : INTEGER
    # YCoordinate : INTEGER
    # Intelligence : INTEGER
    def __init__(self, name, x, y):
        self.__Name = name
        self.__XCoordinate = x
        self.__YCoordinate = y
        self.__Intelligence = 50
    def GetName(self): return self.__Name
    def GetX(self): return self.__XCoordinate
    def GetY(self): return self.__YCoordinate
    def GetIntelligence(self): return self.__Intelligence
    def ChangePosition(self, x_change, y_change):
        self.__XCoordinate += x_change
        self.__YCoordinate += y_change
    def SetIntelligence(self, v):     # setter with validation (9618_w23_qp_42 pattern)
        if 0 <= v <= 100:
            self.__Intelligence = v

ch = CharacterWithSetter("Amal", 0, 2)
print("  CharacterWithSetter — GetName:", ch.GetName(), "GetX:", ch.GetX(), "GetIntelligence:", ch.GetIntelligence())
ch.SetIntelligence(150)  # rejected — outside 0..100
print("  After SetIntelligence(150):", ch.GetIntelligence(), "(rejected — validation blocks it)")
ch.SetIntelligence(80)
print("  After SetIntelligence(80):", ch.GetIntelligence(), "(accepted)")
print("  Mark scheme: getter = correct name, self only, return self.__Attr. Extra setter for ChangePosition pattern too.")
print()

# -------------------------------------------------------------
# Pattern 3 — Instantiate objects into an array/list
# Sources: 9618_w24_qp_42 Q1(b)(ii) Group [3], 9618_w25_qp_43 Q1(a)(iii) 5 BoardObjects [3],
#          9618_w25_qp_42 Q1(b) 2 Birds [3]
# Stem: "One group has five events (table given). Create EventItem for each and store in Group."
#       / "Create two Birds: Cockatiel 71.0, Macaw 56.0."
# Mark scheme: 1 mark declaring array/list, 1 per correct instantiation with correct arg order
# When exam asks this → Write:
# -------------------------------------------------------------
print("--- Pattern 3: Instantiate objects into array/list ---")
print("  Sources: 9618_w24_qp_42 Q1(b)(ii) Group [3], 9618_w25_qp_43 Q1(a)(iii) 5 BoardObjects [3], 9618_w25_qp_42 Q1(b) 2 Birds [3]")
print("  Stem: 'Group has five events (table given). Create EventItem for each, store in Group.'")
print("  When exam asks this → Write: Group=[] + Group.append(EventItem(...)) with table values in given order")
# 9618_w24 pattern: named Group, 5 EventItems in given order
Group = []
Group.append(EventItem("Bridge", "jump", 3))
Group.append(EventItem("Water wade", "swim", 4))
Group.append(EventItem("100 mile run", "run", 5))
Group.append(EventItem("Gridlock", "drive", 2))
Group.append(EventItem("Wall on wall", "jump", 4))
print("  Group (5 EventItems in table order):", [(g.GetName(), g.GetEventType(), g.GetDifficulty()) for g in Group])
# 9618_w25_qp_43 pattern: 5 specific variables
Obj1 = BoardObjectFull("A", 2); Obj2 = BoardObjectFull("B", 3)
Obj3 = BoardObjectFull("C", 5); Obj4 = BoardObjectFull("D", 2); Obj5 = BoardObjectFull("E", 7)
print("  5 BoardObjects (individual vars, 9618_w25_qp_43):", [(o.GetCode(), o.GetValue()) for o in [Obj1,Obj2,Obj3,Obj4,Obj5]])
# 9618_w25_qp_42 pattern: two Birds
Bird1 = BirdFull("Cockatiel", 71.0); Bird2 = BirdFull("Macaw", 56.0)
print("  2 Birds (9618_w25_qp_42):", Bird1.GetSpecies(), Bird1.GetSpeed(), "|", Bird2.GetSpecies(), Bird2.GetSpeed())
print("  Mark scheme: 1 mark for declaring Group/list, 1 per correct arg order. Use table order exactly.")
print()

# -------------------------------------------------------------
# Pattern 4 — Method with logic (CalculateScore / Move / Success)
# Sources: 9618_w24_qp_42 Q1(d) CalculateScore [4], 9618_w25_qp_42 Q1(a)(iv) Bird.Move [5],
#          9618_w24_qp_43 Horse.Success [4]
# Stem (CalculateScore): "When skill >= difficulty, return 100. Otherwise diff: 1→80, 2→60, 3→40, else 20."
# Stem (Bird.Move): "Move() takes direction (N/S/E/W) and hours (REAL). Updates X/Y by DistancePerHour × hours."
# When exam asks this → Write the difference/condition mapping exactly.
# -------------------------------------------------------------
print("--- Pattern 4: Method with logic — CalculateScore / Move / Success ---")
print("  Sources: 9618_w24_qp_42 Q1(d) CalculateScore [4], 9618_w25_qp_42 Q1(a)(iv) Bird.Move [5], 9618_w24_qp_43 Horse.Success [4]")
print("  Stem CalculateScore: 'skill >= difficulty → 100; else diff 1→80, 2→60, 3→40, else 20'")
print("  Stem Bird.Move: 'direction N/S/E/W + hours → update X/Y by DistancePerHour × hours'")
print("  When exam asks this → map the table row-for-row, don't invent values.")
class CharacterGame:
    # CharacterName : STRING
    # Jump, Swim, Run, Drive : INTEGER (1-5 skill levels)
    def __init__(self, p_name, p_jump, p_swim, p_run, p_drive):
        self.__CharacterName = p_name
        self.__Jump = p_jump; self.__Swim = p_swim
        self.__Run = p_run;   self.__Drive = p_drive
    def GetName(self): return self.__CharacterName
    def CalculateScore(self, event_type, difficulty):
        # Map event_type → skill, then skill vs difficulty → score (table from question)
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

# 9618_w24: Horse.Success pattern (similar logic, different domain)
class Horse:
    # Name : STRING
    # MaxFenceHeight : INTEGER
    # PercentageSuccess : INTEGER
    def __init__(self, p_name, p_height, p_pct):
        self.__Name = p_name
        self.__MaxFenceHeight = p_height
        self.__PercentageSuccess = p_pct
    def GetName(self): return self.__Name
    def GetMaxFenceHeight(self): return self.__MaxFenceHeight
    def Success(self, fence_height):
        """Percentage chance — simplified: if fence > max, reduced; else full pct."""
        if fence_height <= self.__MaxFenceHeight:
            return self.__PercentageSuccess
        return max(0, self.__PercentageSuccess - (fence_height - self.__MaxFenceHeight))

tarz = CharacterGame("Tarz", 5, 3, 5, 1)
geni = CharacterGame("Geni", 2, 2, 3, 4)
print("  CalculateScore — Tarz(5,3,5,1) vs Geni(2,2,3,4):")
print("    Tarz vs Bridge(jump,3):", tarz.CalculateScore("jump", 3), "(100: skill 5 >= diff 3)")
print("    Geni vs Bridge(jump,3):", geni.CalculateScore("jump", 3), "(80: diff=1 → 80)")
print("    Geni vs 100 mile run(run,5):", geni.CalculateScore("run", 5), "(60: diff=2 → 60)")
print("    Geni vs Gridlock(drive,2):", geni.CalculateScore("drive", 2), "(100: skill 4 >= diff 2)")
horse = Horse("Thunder", 132, 70)
print("  Horse.Success — Thunder(Max132, 70%): Success(120)=", horse.Success(120), " Success(140)=", horse.Success(140))
bf = BirdFull("Swift", 50.0)
bf.Move("E", 2.5)
print("  Bird.Move — Swift(50.0) Move(E,2.5): X =", bf.GetX(), "Y =", bf.GetY(), "← 50×2.5 on X")
bf.Move("N", 1)
print("  Swift Move(N,1): X =", bf.GetX(), "Y =", bf.GetY(), "← 50×1 on Y")
print()

# -------------------------------------------------------------
# Pattern 5 — File → array of objects + search loop
# Sources: 9618_w22_qp_42 Q2(d)(e)(f) Characters.txt [7+5+7 marks]
# Stem: "Characters.txt stores 10 characters: each has Name, XCoordinate, YCoordinate
#        (each on its own line). Read file into 1D array of Character objects.
#        Then allow searching by name (case-insensitive, retry until found) and moving
#        by A/W/S/D with validation."
# When exam asks file → objects → search → move → output → Write this chain:
# -------------------------------------------------------------
print("--- Pattern 5: File → array of objects + case-insensitive search + move validation ---")
print("  Source: 9618_w22_qp_42 Q2(d)(e)(f) Characters.txt [7+5+7 marks]")
print("  Stem: 'Characters.txt: Name, X, Y each on own line (10 chars). Read into array,")
print("         search by name (case-insensitive, retry until found), move via A/W/S/D, validate.'")
print("  When exam asks this → with open + splitlines + while i+2<len + retry loop with .upper()")
def demo_character_file_game():
    """9618_w22_qp_42 Q2(d)(e)(f)(g) — full file->search->move->output chain, scripted (no input())."""
    with tempfile.TemporaryDirectory() as tmp:
        chars_path = os.path.join(tmp, "Characters.txt")
        with open(chars_path, "w") as f:
            f.write("Amal\n0\n2\nBen\n3\n4\nCara\n1\n1\nDan\n5\n5\nEma\n2\n0\n"
                    "Far\n4\n3\nGil\n0\n5\nHana\n3\n1\nIvo\n5\n2\nQui\n4\n0\n")

        class Character:
            # Name : STRING
            # XCoordinate : INTEGER
            # YCoordinate : INTEGER
            def __init__(self, name, x, y):
                self.__Name = name; self.__XCoordinate = x; self.__YCoordinate = y
            def GetName(self): return self.__Name
            def GetX(self): return self.__XCoordinate
            def GetY(self): return self.__YCoordinate
            def ChangePosition(self, x_change, y_change):
                self.__XCoordinate += x_change
                self.__YCoordinate += y_change

        # (d) Read file into array of objects
        print("  (d) Reading Characters.txt → array of Character objects:")
        Characters = []
        with open(chars_path) as f:
            lines = f.read().splitlines()
        i = 0
        while i + 2 < len(lines):
            Characters.append(Character(lines[i], int(lines[i+1]), int(lines[i+2])))
            i += 3
        print(f"      Loaded {len(Characters)} →", [c.GetName() for c in Characters])

        # (e) Search by name with retry (case-insensitive, scripted — input() in exam)
        #     Scripted inputs: THOMAS (miss) then "qui" (hit via "Qui" case-insensitive)
        print("  (e) Search — case-insensitive, retry until found (scripted inputs: THOMAS, qui):")
        name_inputs = ["THOMAS", "qui"]
        index = -1
        for j in range(len(Characters)):
            if Characters[j].GetName().upper() == name_inputs[0].upper():
                index = j
        k = 1
        while index == -1 and k < len(name_inputs):
            test = name_inputs[k]; k += 1
            for j in range(len(Characters)):
                if Characters[j].GetName().upper() == test.upper():
                    index = j
            if index == -1:
                print("      Name not found:", test)
            else:
                print(f"      Found '{test}' as '{Characters[index].GetName()}' at index {index} (case-insensitive .upper() ✅)")

        # (f) Validate direction, then move via method — scripted: X (invalid), A (valid)
        print("  (f) Direction validation — scripted inputs: X (invalid), A (valid: x-1):")
        direction_inputs = ["X", "A"]
        direction = direction_inputs[0]; m = 1
        while direction not in ("A","W","S","D") and m < len(direction_inputs):
            print("      Invalid direction:", direction, "→ retry")
            direction = direction_inputs[m]; m += 1
        print(f"      Valid direction: {direction}")
        if direction == "A": Characters[index].ChangePosition(-1, 0)
        elif direction == "D": Characters[index].ChangePosition(1, 0)
        elif direction == "W": Characters[index].ChangePosition(0, 1)
        else: Characters[index].ChangePosition(0, -1)  # S

        # (g) Output via getters only (not direct attr access) — mark scheme requires getters
        print(f"  (g) Output via getters → {Characters[index].GetName()} has changed coordinates to X = {Characters[index].GetX()} and Y = {Characters[index].GetY()}")

demo_character_file_game()
print()

# -------------------------------------------------------------
# Pattern 6 — Inheritance diagram / class diagram
# Sources: 9618 Theory papers (32) + textbook Fig 27.02/27.03
# Stem: "Draw the inheritance diagram for LibraryItem, Book, CD."
#       / "Complete the class diagram for BuildingClass (all properties PRIVATE)."
#       / "Write the declaration for OwnerName as PRIVATE."
# When exam asks this → Draw tree with base on top + -/+ signs + types.
# -------------------------------------------------------------
print("--- Pattern 6: Inheritance diagram & class diagram ---")
print("  Sources: Theory papers (32), textbook Fig 27.02/27.03, 9618_s22_qp_32 Q3")
print("  Stem: 'Draw inheritance diagram for LibraryItem, Book, CD' / 'Complete class diagram, PRIVATE attrs'")
print("  When exam asks inheritance diagram → draw:")
print("          LibraryItem")
print("          /         \\")
print("       Book          CD")
print("     (base on top, subclasses below; UML triangle arrow also accepted)")
print("  When exam asks class diagram → three-section box with - (private attrs) and + (public methods):")
print("  +------------------------------------+")
print("  |                Car                 |  ← class name on top")
print("  | - VehicleID          : STRING      |  ← - = private + type")
print("  | - PurchasePrice      : CURRENCY    |")
print("  | + GetVehicleID()     : STRING      |  ← + = public method")
print("  | + SetPurchasePrice(p : CURRENCY)   |")
print("  +------------------------------------+")
print("  When exam asks PRIVATE declaration → PRIVATE OwnerName : STRING (exact case, colon, type)")
print("  Labels earn marks, not pretty boxes — write exact identifiers + types from question.")
print()

# -------------------------------------------------------------
# Pattern 7 — Polymorphic loop / scoring loop
# Sources: 9618_w24_qp_42 Q1(e) Tarz vs Geni scoring [7]; textbook display_all / menu
# Stem: "Two characters Tarz (5,3,5,1) and Geni (2,2,3,4) attempt every event in Group.
#        For each event call CalculateScore; award 1 point to winner, 0 for draw.
#        Output per-event winner and overall group winner."
# When exam asks polymorphic scoring loop → for event in Group: s1=p1.CalculateScore(...) + points
# -------------------------------------------------------------
print("--- Pattern 7: Polymorphic scoring loop — Tarz vs Geni (every event, point by point) ---")
print("  Source: 9618_w24_qp_42 Q1(e) Tarz vs Geni [7] + textbook display_all")
print("  Stem: 'Tarz(5,3,5,1) and Geni(2,2,3,4) attempt every event in Group. For each event")
print("         CalculateScore → 1 point to winner, draw → 0 each. Output per-event + overall winner.'")
print("  When exam asks this → for event in Group: s1=p1.CalculateScore(event.GetEventType(), event.GetDifficulty())")
p1 = CharacterGame("Tarz", 5, 3, 5, 1)
p2 = CharacterGame("Geni", 2, 2, 3, 4)
p1_points = 0; p2_points = 0
for event in Group:
    s1 = p1.CalculateScore(event.GetEventType(), event.GetDifficulty())
    s2 = p2.CalculateScore(event.GetEventType(), event.GetDifficulty())
    if s1 > s2:
        p1_points += 1
        print(f"    {p1.GetName()} wins {event.GetName()} ({s1} vs {s2}) ← 1 point")
    elif s2 > s1:
        p2_points += 1
        print(f"    {p2.GetName()} wins {event.GetName()} ({s2} vs {s1}) ← 1 point")
    else:
        print(f"    {event.GetName()} is a draw ({s1} each) ← 0 points each")
if p1_points > p2_points:
    print(f"  → {p1.GetName()} wins the group with {p1_points} points")
elif p2_points > p1_points:
    print(f"  → {p2.GetName()} wins the group with {p2_points} points")
else:
    print("  → The group is a draw")
print("  Polymorphism also: for item in shelf: item.PrintDetails() — one call, right subclass each time (see Part 4).")
print()

# -------------------------------------------------------------
# Pattern 8 — Containment (Course/Lesson/Assessment)
# Source: Textbook Worked Example 27.03 + exam variants (Car/Engine, Node/Data)
# Stem: "A Course contains up to 50 Lessons and one Assessment. Write Course with AddLesson, AddAssessment,
#        and OutputCourseDetails."
# When exam asks containment → see Part 5 — Course with self.__CourseLesson=[] and self.__CourseAssessment=None,
#                                building component objects inside AddLesson/AddAssessment.
# -------------------------------------------------------------
print("--- Pattern 8: Containment re-check — Course HAS Lessons (has-a, not is-a) ---")
print("  Source: Textbook Worked Example 27.03 + exam variants")
print("  Stem: 'Course contains up to 50 Lessons and one Assessment. Write AddLesson, AddAssessment, OutputCourseDetails.'")
print("  When exam asks this → containment pattern from Part 5 (already demoed) — quick re-check:")
print(f"    Course '{MyCourse.GetTitle()}' has {MyCourse.GetLessonCount()} lessons")
print(f"    Assessment: {MyCourse.GetAssessment().OutputAssessmentDetails()}")
# Second demo: build a fresh course to show AddLesson limit guard you'd add in exam
fresh = Course("Data Structures", 30)
fresh.AddAssessment("Final Exam", 100)
fresh.AddLesson("Arrays", 45, False)
fresh.AddLesson("Linked Lists", 60, True)
print("  Fresh Course('Data Structures', 30) →", end=" ")
fresh.OutputCourseDetails()
print()

# -------------------------------------------------------------
# Pattern 9 — Pseudocode ↔ Python class conversion (Theory)
# Source: 9618_s22_qp_32 Q3c + Pseudocode Guide Ch.10
# Stem: "The record BuildingRecord is changed to class BuildingClass. Properties: BuildingID, BuildingGroup,
#        OwnerName, BuildingAddress, DateLastSold, PriceLastSold. All PRIVATE. Write declaration for OwnerName
#        as PRIVATE. Explain why PRIVATE."
# When exam asks this → PRIVATE OwnerName : STRING  + encapsulation reason.
# -------------------------------------------------------------
print("--- Pattern 9: Pseudocode PRIVATE declaration + why (theory) ---")
print("  Source: 9618_s22_qp_32 Q3c + Pseudocode Guide Ch.10")
print("  Stem: 'BuildingRecord → BuildingClass, all properties PRIVATE. Write declaration for OwnerName.'")
print("  When exam asks PRIVATE declaration → PRIVATE OwnerName : STRING  (exact case, colon, type)")
print("  Pseudocode: PRIVATE OwnerName : STRING")
print("  Python equivalent: self.__OwnerName  +  '# OwnerName : STRING' comment above __init__")
print("  Why PRIVATE? Encapsulation — prevents direct/accidental modification, forces access through")
print("  methods where validation can be enforced, makes code more robust and reusable. ✅")
# Show the full BuildingClass shape as you'd write in exam
print("  Full BuildingClass shape (as exam expects, Python version):")
class BuildingClass:
    # BuildingID : STRING
    # BuildingGroup : STRING
    # OwnerName : STRING
    # BuildingAddress : STRING
    # DateLastSold : DATE
    # PriceLastSold : CURRENCY
    def __init__(self, p_id, p_group, p_owner, p_address, p_date, p_price):
        self.__BuildingID = p_id
        self.__BuildingGroup = p_group
        self.__OwnerName = p_owner
        self.__BuildingAddress = p_address
        self.__DateLastSold = p_date
        self.__PriceLastSold = p_price
    def GetOwnerName(self): return self.__OwnerName
    def GetBuildingID(self): return self.__BuildingID

bc = BuildingClass("B001", "A", "Alice Smith", "1 High St", datetime.date(2024, 6, 1), 250000.00)
print(f"    BuildingClass('B001',...) → OwnerName via getter: {bc.GetOwnerName()}")
print()

# -------------------------------------------------------------
# Pattern 10 — Instantiation + method call in main program
# Source: Every Paper 4 practical (evidence.doc pattern)
# Stem: "Write program code for the main program to declare, instantiate, and use objects. Save as Question1_N24 / evidence."
# Mark scheme: correct constructor call with correct arg order, correct object.Method(args), correct output via getters.
# When exam asks main program → Write:
# -------------------------------------------------------------
print("--- Pattern 10: Main program — declare, instantiate, use objects (evidence.doc pattern) ---")
print("  Source: Every Paper 4 practical")
print("  Stem: 'Write main program to declare, instantiate, and use objects. Save as Question1_N24.'")
print("  When exam asks this → obj = Class(args) + obj.Method() + print(obj.GetX()) with correct arg order")
# Declare + instantiate
ThisBook2 = Book("Computing", "Sylvia", 1234)
ThisCD2 = CD("Let It Be", "The Beatles", 2345)
# Use via methods
ThisBook2.Borrowing()
ThisBook2.SetIsRequested()
print(f"  ThisBook = Book('Computing','Sylvia',1234) → Title:{ThisBook2.GetTitle()}, OnLoan:{ThisBook2.GetOnLoan()}, Requested:{ThisBook2.GetIsRequested()}")
ThisCD2.SetGenre("Rock")
print(f"  ThisCD = CD('Let It Be','The Beatles',2345) → Genre:{ThisCD2.GetGenre()}")
# Polymorphic display in main program
print("  Polymorphic display in main program — one loop for both:")
for item in [ThisBook2, ThisCD2]:
    print(f"    --- {item.GetTitle()} ---")
    item.PrintDetails()
print("  Mark scheme: constructor arg order must match __init__ params, method call is object.Method(args), output via getters.")
print()

# =============================================================
# PART 10: COMMON TRAPS & QUICK REFERENCE  ⚠️
#  TL;DR: The examiner has seen every mistake before. This is your checklist to dodge them.
# =============================================================
print("=" * 60)
print("PART 10: COMMON TRAPS & QUICK REFERENCE  ⚠️")
print("  TL;DR: The examiner has seen every mistake before — here's your dodge checklist.")
print("=" * 60)

# 10.1 Top Traps — live checks (Examiner Report Highlights)
print("--- 10.1 Top traps — how to dodge them (Examiner Report Highlights) ---")
traps = [
    ("Hardcoded constructor values", 'self.__Name = "Amal" instead of = p_name', "Always assign PARAMETER to attribute"),
    ("Forgetting self", "def GetName(): → TypeError", "Every method: def GetName(self):"),
    ("Single underscore private", "self._Name not treated as private", "Use self.__Name (double underscore)"),
    ("Getter/setter name confusion", "def SetName that returns value", "Getter=returns, Setter=assigns+may validate"),
    ("Extra setter for fixed attr", "Adding SetVehicleID when 'never changes'", "No setter for fixed attrs"),
    ("Wrong method name for polymorphism", "PrintBookDetails vs PrintDetails", "EXACT same name as base"),
    ("Forgetting super().__init__", "Subclass attrs work but base attrs missing", "First line of subclass __init__: super().__init__(...)"),
    ("[Obj()] * 100", "One object copied 100 times", "Use [Obj() for _ in range(100)]"),
    ("open without close/with", "File locked, data lost", "Use with open(...) as f:"),
    ("Java constructor in Python", "def Car(self, ...)", "In Python it is ALWAYS __init__"),
    ("Python constructor in Java", "__init__ in Java answer", "In Java it is SAME NAME as class"),
    ("Case-insensitive search", 'if name == stored fails for "qui" vs "Qui"', "Use .upper() on both sides"),
]
for trap, what, fix in traps:
    print(f"  {trap:32s} | {what:45s} | Fix: {fix}")
print()

# Live trap demos — runnable proof
print("--- Live trap demos — see the bug, see the fix ---")
# Trap: hardcoded vs param
print("  Trap: hardcoded constructor value")
print("    BAD:  self.__Name = 'Amal'  (ignores parameter — mark lost)")
print("    GOOD: self.__Name = p_name  (uses parameter) — see EventItem above: self.__EventName = p_name ✅")
# Trap: single underscore
print("  Trap: single underscore is not private")
print("    BAD:  self._Name  (protected convention, not private)")
print("    GOOD: self.__Name (name mangling, truly private) ✅")
# Trap: extra setter
print("  Trap: extra setter for fixed attr")
print("    If question says 'never changes' -> NO setter for that attr — see Company: no SetCompanyName ✅")
# Trap: polymorphic name mismatch
print("  Trap: polymorphic name mismatch")
print("    Base has PrintDetails, subclass must ALSO be PrintDetails (exact case) — see BookPoly/CDPoly ✅")
# Trap: [Obj()]*N
print("  Trap: [Obj()]*N shares one object — demo:")
a = [Car("X", 100)] * 3
print(f"    [Car('X',100)]*3 → a[0] is a[1]: {a[0] is a[1]} (bug if you mutate one)")
b_list = [Car("X", 100) for _ in range(3)]
print(f"    [Car('X',100) for _ in range(3)] → b[0] is b[1]: {b_list[0] is b_list[1]} (correct)")
print()

# 10.2 Quick Reference — Every Key Term in One Place 📖
print("--- 10.2 Quick Reference — every key term in one place  📖 ---")
quick_ref = [
    ("Class", "Type combining data + methods (blueprint) — cookie cutter"),
    ("Object", "Instance of a class — one cookie"),
    ("Instance", "Specific object created from a class"),
    ("Attributes", "Data items of a class (fields), always private (__Name)"),
    ("Methods", "Subroutines of a class, always public"),
    ("Encapsulation", "Bundling data + methods and restricting external access to data"),
    ("Constructor", "Special method (__init__ in Python, same-name-as-class in Java) that creates + initialises"),
    ("Getter", "Public method that reads/returns an attribute — the window"),
    ("Setter", "Public method that changes an attribute (may validate) — the door"),
    ("Property", "Class member bundling attr with getter/setter (@property in Python)"),
    ("Instantiation", "Creating an object from a class (memory reserved) — Car('ABC1234', 2500)"),
    ("Private", "Accessible only through class's methods (__ in Python, PRIVATE in pseudocode)"),
    ("Public", "Callable from anywhere (default for methods in Python)"),
    ("Inheritance", "All attrs + methods of base are copied to subclass — 'is a kind of'"),
    ("Base / superclass", "Class subclasses are derived from (parent)"),
    ("Subclass / derived", "Class derived from a base (has everything base has + extras) — child"),
    ("Abstract class", "Base never instantiated directly (template for subclasses, e.g. LibraryItem)"),
    ("Polymorphism", "Same method name behaves differently per class (PrintDetails in LibraryItem/Book/CD)"),
    ("Containment (aggregation)", "Has-a: one class has component of another class type (Course HAS Lessons)"),
    ("Overriding", "Redefining a base method in a subclass with same identifier (how polymorphism is implemented)"),
    ("Memory leakage", "Running out of memory because unneeded objects never release theirs"),
    ("Garbage collection", "Automatic reclamation of memory from objects no longer referenced"),
]
for term, meaning in quick_ref:
    print(f"  {term:26s} | {meaning}")
print()

# 10.3 At-a-Glance: Which Pattern for Which Question? 🔍
print("--- 10.3 At-a-glance: which pattern for which question?  🔍 ---")
print("  When you spot this phrase in the exam → reach for this pattern:")
at_a_glance = [
    ("Declare class + constructor. All attrs private.", "Pattern 1 → class X: # attrs : TYPE + __init__ assigning params"),
    ("Write code for GetName()", "Pattern 2 → def GetName(self): return self.__Name"),
    ("Create instances and store in Group / array", "Pattern 3 → Group.append(ClassName(args)) or Obj1 = ClassName(...)"),
    ("CalculateScore / Move / Success logic", "Pattern 4 → read table, map difference/condition to return values"),
    ("Read file and create objects", "Pattern 5 → with open + splitlines + append(ClassName(...)) + search/retry loop"),
    ("Draw inheritance / class diagram", "Pattern 6 → tree with base on top + -/+ signs + types"),
    ("Polymorphic loop / score every event", "Pattern 7 → for event in Group: s1 = p1.CalculateScore(...) + points"),
    ("Course contains Lessons", "Pattern 8 → self.__list = [] + AddLesson builds component"),
    ("PRIVATE declaration / why private", "Pattern 9 → PRIVATE OwnerName : STRING + encapsulation reason"),
    ("Main program uses objects", "Pattern 10 → obj = Class(args) + obj.Method() + print(obj.GetX())"),
]
for phrase, pattern in at_a_glance:
    print(f"  \"{phrase:50s}\" → {pattern}")
print()

# Sources footer
print("--- Sources — where every pattern comes from  📚 ---")
print("  9618_w22_qp_42 Q2 Character (Name,X,Y) — constructor [4], getters [3], ChangePosition [2], file→objects [7], search [5], direction [7], output [2]")
print("  9618_w24_qp_42 Q1 EventItem + Character(Jump/Swim/Run/Drive) — declare [4], getters [3], Group [3], CalculateScore [4+4], Tarz vs Geni [7]")
print("  9618_w25_qp_42 Q1 Bird (DistancePerHour,Species,X,Y) — constructor [4], Move [5], 2 Birds [3]")
print("  9618_w25_qp_43 Q1 BoardObject (Code,Value) — declare [5], GetCode/Value [3], 5 objects [3]")
print("  9618_w24_qp_43 Q2 Horse (MaxFenceHeight, PercentageSuccess) — constructor/getters/Success()")
print("  9618_s22_qp_32 Q3 BuildingRecord → BuildingClass — PRIVATE declaration [1], why PRIVATE [2]")
print("  Textbook 27.01-27.07 Car, Company, LibraryItem/Book/CD, Borrower, Course/Lesson/Assessment — all worked examples")
print("  Pseudocode rules: Cambridge Pseudocode Guide (2021) Ch.10 — OOP")
print()

print("=" * 60)
print("✅ Chapter 27 complete — every example ran. You're ready for Paper 4. Go ace it! 🧩")
print("=" * 60)
