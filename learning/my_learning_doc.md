# A Level CS 9618 — Complete Exam Guide (Python Only)

> Chapter 27: OOP + Paper 4 ADTs, Searching & Sorting

---

# Part 1: OOP Basics

## 1.1 What is OOP?

**Procedural way:** data (variables) and functions are separate. Anyone can change data from anywhere.

**OOP way:** data + functions that operate on that data are **bundled together** into an **object**. Data is **private** — only accessible through methods. This = **encapsulation**.

### Key Terms

| Term | Meaning | Think of it as |
|------|---------|----------------|
| **Class** | Blueprint for objects | Cookie cutter |
| **Object** | One instance of a class | Actual cookie |
| **Attributes** | Data inside an object | Variables belonging to the object |
| **Methods** | Functions inside an object | Things the object can do |
| **Constructor** | Method that runs when object is created (`__init__`) | "Setup" code |
| **Encapsulation** | Bundling data + methods, hiding data from outside | Data in a safe box |
| **Getter** | Method that **gets** (reads) an attribute | `GetName()` |
| **Setter** | Method that **sets** (writes) an attribute | `SetName()` |
| **Instantiation** | Creating an object from a class | `obj = ClassName()` |

---

## 1.2 Your First Class — Line by Line

Let's build a `Dog` class. Every dog has a name and an age.

```python
# Step 1: Define the class (blueprint)
class Dog:

    # Step 2: Constructor — runs when you create a Dog
    def __init__(self, name, age):
        # self = "this specific dog"
        # __name = PRIVATE attribute (two underscores)
        self.__name = name      # Store the name in THIS dog
        self.__age = age        # Store the age in THIS dog

    # Step 3: A method — the dog can bark
    def bark(self):
        # self.__name refers to THIS dog's name
        return f"{self.__name} says WOOF!"

    # Step 4: Getter — read the name
    def get_name(self):
        return self.__name

    # Step 5: Setter — change the age
    def set_age(self, new_age):
        if new_age > 0:                 # Validation!
            self.__age = new_age

    # Step 6: Another getter
    def get_age(self):
        return self.__age


# ===== USING THE CLASS =====

# Create an object (instantiation)
my_dog = Dog("Buddy", 3)
# Behind the scenes, __init__ runs with name="Buddy", age=3

# Call methods
print(my_dog.bark())           # Buddy says WOOF!
print(my_dog.get_name())       # Buddy

# Use setter
my_dog.set_age(4)
print(my_dog.get_age())        # 4

# CANNOT do this (private!):
# print(my_dog.__name)         # ERROR! Attribute is private
```

**Line-by-line explanation of `__init__`:**
- `def __init__(self, name, age):` — this is the constructor. Runs automatically when you write `Dog("Buddy", 3)`
- `self` — refers to "this specific dog object I'm creating right now"
- `self.__name = name` — take the parameter `name` and store it in THIS dog's `__name` attribute

**Why `__name` (two underscores)?** — Makes the attribute **private**. Can't access it from outside. Must use getter/setter methods. This is **encapsulation**.

---

## 1.3 Another Example — BankAccount (Explained)

```python
class BankAccount:
    def __init__(self, acc_holder, initial_balance):
        # Constructor — sets up the account
        self.__holder = acc_holder    # Store account holder name
        self.__balance = initial_balance  # Store balance
        self.__transactions = 0       # Count how many transactions

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Method — deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount      # Add to balance
            self.__transactions += 1      # Count it
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Amount must be positive!"

    # Method — withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__transactions += 1
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Insufficient funds!"

    # Getter
    def get_transactions(self):
        return self.__transactions


# ===== USE IT =====
acc = BankAccount("Alice", 1000)      # Create account with $1000
print(acc.get_balance())              # 1000
print(acc.deposit(500))               # Deposited $500. Balance: $1500
print(acc.withdraw(200))              # Withdrew $200. Balance: $1300
print(acc.get_transactions())         # 2

# Safe: balance can ONLY be changed through deposit/withdraw
# Can't accidentally do: acc.__balance = 9999999 (protected!)
```

---

## 1.4 Getters & Setters — Why Bother?

Without encapsulation (bad):
```python
class BadAccount:
    def __init__(self, bal):
        self.balance = bal   # Public! Anyone can change it

acc = BadAccount(100)
acc.balance = -5000          # Allowed! Negative balance = bug!
```

With encapsulation (good):
```python
class GoodAccount:
    def __init__(self, bal):
        self.__balance = bal   # Private!

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_bal):
        if new_bal >= 0:          # VALIDATION — catch bugs!
            self.__balance = new_bal

acc = GoodAccount(100)
# acc.__balance = -5000          # ERROR! Can't touch private
acc.set_balance(-5000)           # Won't work — validation stops it
print(acc.get_balance())         # Still 100 — safe!
```

**Getters and setters let you control WHAT goes in and WHAT comes out.**

---

# Part 2: Inheritance & Polymorphism

## 2.1 Inheritance — Plain English

**Inheritance** = one class (child/subclass) gets ALL attributes and methods of another class (parent/base class). The child can then **add** its own stuff or **override** methods.

> Think: Vehicle → Car. A Car IS a Vehicle. It has everything a Vehicle has, plus more.

### Simple Example — Animal → Dog, Cat

```python
# ===== PARENT CLASS (base class) =====
class Animal:
    def __init__(self, name):
        self.__name = name      # Private attribute

    def get_name(self):          # Getter
        return self.__name

    def make_sound(self):        # Method — will be overridden
        return "Some sound..."

    def move(self):              # Method — will be inherited
        return f"{self.__name} is moving."


# ===== CHILD CLASS 1 =====
class Dog(Animal):               # Dog INHERITS from Animal
    def __init__(self, name, breed):
        super().__init__(name)    # Call Animal's constructor to set name
        self.__breed = breed      # Dog-specific attribute

    def get_breed(self):          # Dog-specific method
        return self.__breed

    def make_sound(self):         # OVERRIDE the parent's method
        return "WOOF!"            # Polymorphism!

    def fetch(self):              # Dog-specific method
        return f"{self.get_name()} is fetching the ball!"


# ===== CHILD CLASS 2 =====
class Cat(Animal):               # Cat INHERITS from Animal
    def __init__(self, name, lives_left):
        super().__init__(name)
        self.__lives_left = lives_left

    def make_sound(self):         # OVERRIDE — different from Dog!
        return "MEOW!"            # Polymorphism!

    def purr(self):
        return "purrrrr..."


# ===== USE THEM =====
dog = Dog("Rex", "German Shepherd")
cat = Cat("Whiskers", 9)

print(dog.move())           # Inherited from Animal — Rex is moving.
print(cat.move())           # Inherited from Animal — Whiskers is moving.

print(dog.make_sound())     # Overridden — WOOF!
print(cat.make_sound())     # Overridden — MEOW! (different from Dog)

print(dog.fetch())          # Dog-specific
print(cat.purr())           # Cat-specific

print(dog.get_breed())      # German Shepherd
```

### What `super().__init__()` Does

```python
class Dog(Animal):
    def __init__(self, name, breed):
        # super() = "my parent class" (Animal)
        # super().__init__(name) = call Animal's __init__, pass it 'name'
        # This sets self.__name = name inside the Animal part
        super().__init__(name)
        # Now add Dog-specific stuff
        self.__breed = breed

# Without super().__init__():
# You'd have to repeat the parent's code, which is BAD:
# self.__name = name   ← Don't do this! Use super()!
```

### Inheritance Diagram

```
        ┌──────────────┐
        │    Animal    │  ← Parent / Base class
        └──────┬───────┘
               │
     ┌─────────┴─────────┐
     │                   │
┌────┴─────┐      ┌─────┴────┐
│   Dog    │      │   Cat    │  ← Child / Subclasses
└──────────┘      └──────────┘
```

---

## 2.2 Polymorphism — Plain English

**Polymorphism** = same method name, different behaviour in each class.

`make_sound()` exists in all three:
- `Animal.make_sound()` → "Some sound..."
- `Dog.make_sound()` → "WOOF!"
- `Cat.make_sound()` → "MEOW!"

Same name. Different behaviour. That's polymorphism.

```python
# POLYMORPHISM DEMO — loop through different animals, call same method
animals = [Animal("Generic"), Dog("Rex", "Hound"), Cat("Kitty", 9)]

for a in animals:
    # Each animal calls ITS OWN version of make_sound
    print(f"{a.get_name()} says: {a.make_sound()}")

# Output:
# Generic says: Some sound...
# Rex says: WOOF!
# Kitty says: MEOW!
```

---

## 2.3 Abstract Class

An **abstract class** = a base class that you NEVER create objects from directly. It only exists to be inherited from.

```python
# You should NEVER create a plain "Animal" — too vague
# Animal should be abstract — only Dog and Cat make sense

# We can't really enforce abstract in Python, but the IDEA is:
# Animal = blueprint for DOG and CAT, not something you use directly
```

---

# Part 3: ADTs — Data Structures (Node, Stack, Queue, Linked List, Tree, Graph)

## 3.1 The Node Class — Building Block of Everything

A **Node** is like a box that holds data and a pointer(s) to the next box(es).

```
[NODE]
┌──────────┐
│   Data   │  ← The value stored
├──────────┤
│ Pointer  │  ← Points to next node (or None)
└──────────┘
```

```python
class Node:
    """A single node — the building block of linked lists, trees, graphs"""
    def __init__(self, data):
        self.__data = data     # The value this node holds
        self.__next = None     # Pointer to the next node (None = nothing after)

    def get_data(self):
        return self.__data

    def set_data(self, d):
        self.__data = d

    def get_next(self):
        return self.__next

    def set_next(self, n):
        self.__next = n
```

**Visual:**
```
Node("A") → Node("B") → Node("C") → None
```

---

## 3.2 Stack (LIFO — Last In, First Out)

A stack is like a **pile of plates**: you add to the top, you take from the top.

```
    ┌──────┐
    │   3  │ ← TOP (most recent)
    ├──────┤
    │   2  │
    ├──────┤
    │   1  │ ← BOTTOM (oldest)
    └──────┘
```

**Operations:** `push` (add to top), `pop` (remove from top), `peek` (look at top)

### Stack with Array (Simple)

```python
class Stack:
    """Stack using a Python list (array)"""
    def __init__(self, size):
        self.__stack = [None] * size    # Fixed-size array
        self.__top = -1                 # -1 = empty
        self.__size = size

    def push(self, item):
        """Add item to top of stack"""
        if self.__top >= self.__size - 1:
            return "Stack Overflow!"     # Stack is full
        self.__top += 1
        self.__stack[self.__top] = item
        return f"Pushed {item}"

    def pop(self):
        """Remove and return top item"""
        if self.__top == -1:
            return "Stack Underflow!"    # Stack is empty
        item = self.__stack[self.__top]
        self.__stack[self.__top] = None  # Clear the slot
        self.__top -= 1
        return item

    def peek(self):
        """Look at top item without removing"""
        if self.__top == -1:
            return None
        return self.__stack[self.__top]

    def is_empty(self):
        return self.__top == -1


# ===== DEMO =====
s = Stack(5)
print(s.push(10))          # Pushed 10
print(s.push(20))          # Pushed 20
print(s.push(30))          # Pushed 30
print(s.peek())            # 30 (top, without removing)
print(s.pop())             # 30 (removed)
print(s.pop())             # 20 (removed)
print(s.is_empty())        # False
print(s.pop())             # 10
print(s.is_empty())        # True

# Stack state step-by-step:
# After push(10): [10, None, None, None, None], top=0
# After push(20): [10, 20, None, None, None], top=1
# After push(30): [10, 20, 30, None, None], top=2
# After pop():    [10, 20, None, None, None], top=1 (returns 30)
```

### Stack with Linked List (More Efficient)

```python
class StackLL:
    """Stack using a linked list — never overflows"""
    def __init__(self):
        self.__top = None     # Top of stack (a Node or None)
        self.__count = 0

    def push(self, item):
        """Add to top — new node points to current top, becomes new top"""
        new_node = Node(item)
        new_node.set_next(self.__top)   # New node → old top
        self.__top = new_node           # New node IS the top now
        self.__count += 1

    def pop(self):
        if self.__top is None:
            return None
        data = self.__top.get_data()
        self.__top = self.__top.get_next()  # Move top down
        self.__count -= 1
        return data

    def peek(self):
        if self.__top is None:
            return None
        return self.__top.get_data()

    def is_empty(self):
        return self.__top is None
```

**Visual of push:**
```
Before: top → "B" → "A" → None
push("C"):
  1. new_node = Node("C"), next = top ("B")
  2. top = new_node
After:  top → "C" → "B" → "A" → None
```

---

## 3.3 Queue (FIFO — First In, First Out)

A queue is like a **line at a counter**: first person in line is first person served.

```
FRONT                    BACK
  ↓                        ↓
┌──────┬──────┬──────┬──────┐
│   1  │   2  │   3  │      │  ← People join at BACK, leave from FRONT
└──────┴──────┴──────┴──────┘
```

**Operations:** `enqueue` (add to back), `dequeue` (remove from front)

### Queue with Array (Circular)

```python
class Queue:
    """Queue using a circular array"""
    def __init__(self, size):
        self.__queue = [None] * size
        self.__front = -1      # Index of front item
        self.__back = -1       # Index of back item
        self.__size = size

    def enqueue(self, item):
        """Add to back of queue"""
        if self.__back == -1:                 # Empty queue
            self.__front = 0
            self.__back = 0
        else:
            self.__back = (self.__back + 1) % self.__size  # Circular!
        self.__queue[self.__back] = item
        return f"Enqueued {item}"

    def dequeue(self):
        """Remove from front of queue"""
        if self.__front == -1:
            return "Queue Empty!"
        item = self.__queue[self.__front]
        if self.__front == self.__back:       # Last item
            self.__front = -1
            self.__back = -1
        else:
            self.__front = (self.__front + 1) % self.__size  # Circular!
        return item

    def peek_front(self):
        if self.__front == -1:
            return None
        return self.__queue[self.__front]


# ===== DEMO =====
q = Queue(5)
print(q.enqueue("Alice"))     # Enqueued Alice
print(q.enqueue("Bob"))       # Enqueued Bob
print(q.enqueue("Charlie"))   # Enqueued Charlie
print(q.dequeue())            # Alice (first in, first out)
print(q.dequeue())            # Bob
print(q.enqueue("Diana"))     # Enqueued Diana
print(q.peek_front())         # Charlie
```

**Visual:**
```
enqueue("Alice"):  [Alice, None, None, None, None], front=0, back=0
enqueue("Bob"):    [Alice, Bob, None, None, None],  front=0, back=1
dequeue():         [None, Bob, None, None, None],    front=1, back=1  (returns Alice)
```

### Queue with Linked List

```python
class QueueLL:
    """Queue using a linked list"""
    def __init__(self):
        self.__front = None
        self.__back = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.__back is None:         # Empty queue
            self.__front = new_node
            self.__back = new_node
        else:
            self.__back.set_next(new_node)  # Old back → new node
            self.__back = new_node           # New node IS back now
        return f"Enqueued {item}"

    def dequeue(self):
        if self.__front is None:
            return None
        data = self.__front.get_data()
        self.__front = self.__front.get_next()  # Move front forward
        if self.__front is None:                # Queue is now empty
            self.__back = None
        return data
```

---

## 3.4 Linked List

A linked list is a chain of nodes where each node points to the next.

```
Head → [A | ·] → [B | ·] → [C | None]
        data next   data next   data next
```

- **Head** = first node in the list
- Each node has **data** + a **pointer** to the next node
- Last node's pointer = `None`

```python
class LinkedList:
    def __init__(self):
        self.__head = None    # Start with empty list

    def insert_at_front(self, data):
        """Add a new node at the front"""
        new_node = Node(data)
        new_node.set_next(self.__head)   # New node → old head
        self.__head = new_node           # New node IS the head
        return f"Inserted {data} at front"

    def insert_at_end(self, data):
        """Add a new node at the end"""
        new_node = Node(data)
        if self.__head is None:          # Empty list
            self.__head = new_node
            return
        current = self.__head
        while current.get_next() is not None:   # Walk to last node
            current = current.get_next()
        current.set_next(new_node)              # Last node → new node

    def delete(self, data):
        """Delete first node containing data"""
        if self.__head is None:
            return "Empty list"

        # If head is the one to delete
        if self.__head.get_data() == data:
            self.__head = self.__head.get_next()
            return f"Deleted {data}"

        # Search for the node
        current = self.__head
        while current.get_next() is not None:
            if current.get_next().get_data() == data:
                # Skip over the node to delete
                current.set_next(current.get_next().get_next())
                return f"Deleted {data}"
            current = current.get_next()
        return f"{data} not found"

    def display(self):
        """Print all nodes in order"""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.get_data()))
            current = current.get_next()
        print(" → ".join(result) + " → None")


# ===== DEMO =====
ll = LinkedList()
ll.insert_at_front("C")         # C → None
ll.insert_at_front("B")         # B → C → None
ll.insert_at_front("A")         # A → B → C → None
ll.display()

ll.insert_at_end("D")           # A → B → C → D → None
ll.display()

ll.delete("B")                  # A → C → D → None
ll.display()
```

**Insert at front step-by-step:**
```
Before: head → [B | ·] → [C | None]
insert_at_front("A"):
  1. new_node = Node("A")
  2. new_node.set_next(head)  → A → B
  3. head = new_node          → head = A
After:  head → [A | ·] → [B | ·] → [C | None]
```

**Delete step-by-step:**
```
Before: head → [A | ·] → [B | ·] → [C | None]
delete("B"):
  1. current = A
  2. current.get_next() = B, which IS the target
  3. A.set_next(B.get_next()) → A → C (skip B)
After:  head → [A | ·] → [C | None]
```

---

## 3.5 Binary Tree

A tree where each node has **at most 2 children**: left and right.

```
        ┌──────┐
        │  50  │  ← Root
        └──┬───┘
           │
     ┌─────┴─────┐
     │           │
  ┌──┴──┐     ┌──┴──┐
  │ 30  │     │ 70  │  ← Children
  └──┬──┘     └──┬──┘
     │           │
  ┌──┴──┐     ┌──┴──┐
  │ 20  │     │ 40  │  ... and so on
  └─────┘     └─────┘
```

**Binary Search Tree (BST) rule:**
- Left child < Parent
- Right child > Parent

```python
class TreeNode:
    """A node in a binary tree"""
    def __init__(self, data):
        self.__data = data
        self.__left = None     # Left child
        self.__right = None    # Right child

    def get_data(self):    return self.__data
    def get_left(self):    return self.__left
    def get_right(self):   return self.__right
    def set_left(self, n): self.__left = n
    def set_right(self, n): self.__right = n


class BinarySearchTree:
    def __init__(self):
        self.__root = None

    def insert(self, data):
        """Insert data into BST"""
        new_node = TreeNode(data)
        if self.__root is None:
            self.__root = new_node
            return

        current = self.__root
        while True:
            if data < current.get_data():          # Go LEFT
                if current.get_left() is None:     # Empty spot?
                    current.set_left(new_node)     # Insert here
                    return
                current = current.get_left()       # Keep going left
            else:                                   # Go RIGHT
                if current.get_right() is None:    # Empty spot?
                    current.set_right(new_node)    # Insert here
                    return
                current = current.get_right()      # Keep going right

    def inorder(self):
        """Traverse: LEFT → ROOT → RIGHT (sorted order!)"""
        result = []
        self.__inorder_recursive(self.__root, result)
        return result

    def __inorder_recursive(self, node, result):
        if node is not None:
            self.__inorder_recursive(node.get_left(), result)
            result.append(node.get_data())
            self.__inorder_recursive(node.get_right(), result)

    def preorder(self):
        """Traverse: ROOT → LEFT → RIGHT"""
        result = []
        self.__preorder_recursive(self.__root, result)
        return result

    def __preorder_recursive(self, node, result):
        if node is not None:
            result.append(node.get_data())
            self.__preorder_recursive(node.get_left(), result)
            self.__preorder_recursive(node.get_right(), result)

    def postorder(self):
        """Traverse: LEFT → RIGHT → ROOT"""
        result = []
        self.__postorder_recursive(self.__root, result)
        return result

    def __postorder_recursive(self, node, result):
        if node is not None:
            self.__postorder_recursive(node.get_left(), result)
            self.__postorder_recursive(node.get_right(), result)
            result.append(node.get_data())

    def search(self, data):
        """Search for data in BST"""
        current = self.__root
        while current is not None:
            if data == current.get_data():
                return True
            elif data < current.get_data():
                current = current.get_left()
            else:
                current = current.get_right()
        return False


# ===== DEMO =====
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Inorder:", bst.inorder())       # [20, 30, 40, 50, 60, 70, 80] — SORTED!
print("Preorder:", bst.preorder())     # [50, 30, 20, 40, 70, 60, 80]
print("Postorder:", bst.postorder())   # [20, 40, 30, 60, 80, 70, 50]
print("Search 40:", bst.search(40))    # True
print("Search 99:", bst.search(99))    # False
```

**Insert 50, then 30, then 70 step-by-step:**
```
insert(50): root = 50

        50
       /  \
    None  None

insert(30): 30 < 50 → go LEFT → empty → insert

        50
       /  \
     30   None

insert(70): 70 > 50 → go RIGHT → empty → insert

        50
       /  \
     30    70
```

**Inorder traversal (LEFT → ROOT → RIGHT):**
1. Go left as far as possible (20)
2. Visit node (20)
3. Go up, visit parent (30)
4. Go right (40)
5. Go up, visit root (50)
6. Go right subtree... (60, 70, 80)
Result: **20, 30, 40, 50, 60, 70, 80** — always sorted!

---

## 3.6 Graph (BFS & DFS)

A graph is a collection of **nodes** connected by **edges**. Unlike a tree, a graph can have cycles.

```
    A ───── B
    │       │
    │       │
    C ───── D ───── E
```

### Adjacency List Representation

Each node stores a list of its neighbours (nodes it's connected to).

```python
class Graph:
    def __init__(self):
        self.__adj_list = {}    # Dictionary: node → [neighbours]

    def add_node(self, node):
        """Add a new node to the graph"""
        if node not in self.__adj_list:
            self.__adj_list[node] = []     # Start with no neighbours

    def add_edge(self, node1, node2):
        """Add an undirected edge between node1 and node2"""
        if node1 in self.__adj_list and node2 in self.__adj_list:
            self.__adj_list[node1].append(node2)   # node1 → node2
            self.__adj_list[node2].append(node1)   # node2 → node1

    def bfs(self, start):
        """
        Breadth-First Search — explores neighbours first, then their neighbours
        Like a wave expanding outward.
        Uses a QUEUE.
        """
        visited = set()              # Track visited nodes
        queue = [start]              # Queue of nodes to visit
        order = []                   # Order of visitation

        while queue:
            node = queue.pop(0)      # Dequeue from front (FIFO)
            if node not in visited:
                visited.add(node)
                order.append(node)
                # Add all unvisited neighbours to queue
                for neighbour in self.__adj_list[node]:
                    if neighbour not in visited:
                        queue.append(neighbour)
        return order

    def dfs(self, start):
        """
        Depth-First Search — goes deep first, then backtracks.
        Uses a STACK.
        """
        visited = set()
        stack = [start]              # Stack of nodes to visit
        order = []

        while stack:
            node = stack.pop()       # Pop from top (LIFO)
            if node not in visited:
                visited.add(node)
                order.append(node)
                # Add all unvisited neighbours to stack
                for neighbour in self.__adj_list[node]:
                    if neighbour not in visited:
                        stack.append(neighbour)
        return order


# ===== DEMO =====
g = Graph()

# Add nodes
for node in ["A", "B", "C", "D", "E"]:
    g.add_node(node)

# Add edges (connections)
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")
g.add_edge("D", "E")

print("BFS from A:", g.bfs("A"))   # ['A', 'B', 'C', 'D', 'E']
print("DFS from A:", g.dfs("A"))   # ['A', 'C', 'D', 'E', 'B']

# Difference:
# BFS = level by level (like a queue)
# DFS = go deep first (like a stack)
```

### BFS vs DFS Visual

```
Graph:      A ─── B
            │     │
            C ─── D ─── E

BFS from A (Queue — FIFO):
  Queue: [A]
  Visit A, add neighbours B, C → Queue: [B, C]
  Visit B, add neighbour D → Queue: [C, D]
  Visit C, add neighbour D (already there) → Queue: [D]
  Visit D, add neighbour E → Queue: [E]
  Visit E
  Result: A → B → C → D → E  (level by level)

DFS from A (Stack — LIFO):
  Stack: [A]
  Visit A, push neighbours B, C → Stack: [C, B] (top = C)
  Visit C, push neighbour D → Stack: [B, D]
  Visit D, push neighbours B, E → Stack: [B, E] (B already visited)
  Visit E
  Visit B
  Result: A → C → D → E → B  (goes deep first)
```

---

# Part 4: Searching & Sorting Algorithms

## 4.1 Bubble Sort

Compare each pair, swap if out of order. Biggest number "bubbles" to the end.

```
Pass 1: [5, 3, 8, 1] → [3, 5, 1, 8]   (8 bubbled to end)
Pass 2: [3, 5, 1, 8] → [3, 1, 5, 8]   (5 bubbled)
Pass 3: [3, 1, 5, 8] → [1, 3, 5, 8]   (sorted!)
```
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:

                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

                swapped = True

        if not swapped:
            break

    return arr



O(n²) worst, O(n) best (with early exit)

---

## 4.2 Insertion Sort

Pick one element, insert it in the correct position among the already-sorted ones.

```
i=1, v=3: [5, 3, 8, 1] → [3, 5, 8, 1]
i=2, v=8: [3, 5, 8, 1] → [3, 5, 8, 1]   (8 already > 5, stays)
i=3, v=1: [3, 5, 8, 1] → [1, 3, 5, 8]
```

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        value = arr[i]          # "Pick up" this element
        j = i - 1               # Start looking left
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]  # Shift bigger elements right
            j -= 1
        arr[j + 1] = value       # Insert in correct spot
    return arr
```

O(n²) worst, O(n) best (nearly sorted)

---

## 4.3 Binary Search

Search a SORTED list by repeatedly cutting it in half.

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2          # Find middle

        if arr[mid] == target:
            return mid                    # Found it!
        elif arr[mid] > target:
            high = mid - 1                # Search LEFT half
        else:
            low = mid + 1                 # Search RIGHT half

    return -1                             # Not found (AFTER loop!)
```

**Trace with arr=[2, 5, 8, 12, 16], target=12:**
```
low=0, high=4, mid=2 → arr[2]=8 < 12 → low=3
low=3, high=4, mid=3 → arr[3]=12 == 12 → FOUND at index 3!
```

O(log n) — very fast!

---

# Part 5: Common Exam Mistakes (From Your Code)

### ❌ 1. Typo in variable name
```python
high = len(dataaray) - 1    # Should be dataarray
```
**Fix:** Proofread variable names.

### ❌ 2. `false` instead of `False`
```python
found = false   # Python is case-sensitive!
```
**Fix:** Must be `False`, `True`, `None` (capitalized).

### ❌ 3. Code inside a class that runs at definition time
```python
class Wolf(Animal):
    Animal1 = parrot(...)    # ❌ Runs when class is defined, not when object is made
```
**Fix:** Keep class definitions and executable code separate.

### ❌ 4. `return -1` inside the while loop
```python
while low <= high:
    # ...
    return -1    # ❌ Runs after first iteration!
```
**Fix:** Put `return -1` **after** the while loop.

### ❌ 5. Wrong indentation (function inside function)
```python
def binarysearch(arr, target):
    def bubble_sort(arr):     # ❌ This is INSIDE binarysearch!
```
**Fix:** In Python, indentation = scope. Every function at the same level.

---

# Part 6: Exam Tips & Practice

## What You MUST Know

| Topic | Must Be Able To |
|-------|-----------------|
| **OOP terms** | Define: object, class, attribute, method, encapsulation, constructor, getter, setter, inheritance, polymorphism |
| **Class diagram** | Draw with `-` private, `+` public |
| **Write a class** | Private attributes, constructor, getters, setters |
| **Inheritance** | `super().__init__()`, add new stuff, override methods |
| **Polymorphism** | Same method name, different behaviour in each class |
| **Node class** | Building block of linked lists, trees, graphs |
| **Stack (LIFO)** | `push`, `pop`, `peek` — array or linked list |
| **Queue (FIFO)** | `enqueue`, `dequeue` — array (circular) or linked list |
| **Linked List** | `insert_at_front`, `insert_at_end`, `delete`, `display` |
| **Binary Tree** | BST insert, inorder/preorder/postorder, search |
| **Graph** | Adjacency list, BFS (queue), DFS (stack) |
| **Bubble Sort** | Write from memory. O(n²) |
| **Insertion Sort** | Write from memory. O(n²) |
| **Binary Search** | Write from memory. O(log n). List must be sorted! |

## Practice Checklist

- [ ] Write a class with private attributes, getters, setters
- [ ] Write a subclass with `super().__init__()`
- [ ] Override a method (polymorphism)
- [ ] Write Stack push/pop from memory
- [ ] Write Queue enqueue/dequeue from memory
- [ ] Write Linked List insert/delete/display from memory
- [ ] Write BST insert and inorder traversal from memory
- [ ] Write BFS and DFS for a graph from memory
- [ ] Write bubble sort from memory
- [ ] Write insertion sort from memory
- [ ] Write binary search from memory
- [ ] Define: Encapsulation, Inheritance, Polymorphism
- [ ] Fix the bugs in your `school.py`

---

# Part 7: Python Basics Reference

## 7.1 Variables & Data Types

```python
# Python is dynamically typed — no need to declare type
name = "Alice"          # str — text
age = 17                # int — whole number
height = 5.6            # float — decimal
is_student = True       # bool — True or False
nothing = None          # NoneType — means "no value"

# Check type of anything
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>

# Type conversion
str(42)                 # "42"
int("42")               # 42
float("3.14")           # 3.14
bool(1)                 # True (0 is False, everything else is True)
```

---

## 7.2 String Operations

```python
text = "Hello World"

# Indexing (starts at 0!)
text[0]          # 'H'
text[-1]         # 'd' (last character)
text[6]          # 'W'

# Slicing — [start:end:step]
text[0:5]        # 'Hello'  (index 0 to 4, 5 is excluded)
text[:5]         # 'Hello'  (same — from start)
text[6:]         # 'World'  (index 6 to end)
text[-5:]        # 'World'  (last 5 characters)
text[::2]        # 'HloWrd' (every 2nd character)
text[::-1]       # 'dlroW olleH' (reverse!)

# Common methods
text.upper()              # 'HELLO WORLD'
text.lower()              # 'hello world'
text.replace("World", "Python")  # 'Hello Python'
text.split()              # ['Hello', 'World']  (split on space)
"a,b,c".split(",")        # ['a', 'b', 'c']
" ".join(["a", "b", "c"]) # 'a b c'
text.count("l")           # 3
text.find("World")        # 6  (index where "World" starts)
"123".isnumeric()         # True
"abc".isalpha()           # True
len(text)                 # 11

# f-strings (modern, preferred)
name = "Bob"
age = 17
print(f"My name is {name} and I'm {age}")
# Output: My name is Bob and I'm 17

# Concatenation (old way)
print("Hello " + "World")
```

---

## 7.3 if / elif / else (Conditions)

```python
score = 75

if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 50:
    grade = "C"
else:
    grade = "F"

# Comparison operators
# ==   equal to
# !=   not equal to
# <    less than
# >    greater than
# <=   less than or equal
# >=   greater than or equal

# Logical operators
if score > 0 and score < 100:    # AND — both must be True
    print("Valid score")

if score == 0 or score == 100:   # OR — at least one must be True
    print("Edge case")

if not is_student:               # NOT — flips True ↔ False
    print("Not a student")

# Truthy/Falsy values
# Falsy: 0, "", [], None, False, {}, ()
# Everything else is truthy
if name:            # Only runs if name is NOT empty string
    print(name)

# Ternary (inline if-else)
status = "Pass" if score >= 50 else "Fail"
```

---

## 7.4 Lists (Arrays)

```python
# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]     # Can mix types
empty = []                            # Empty list
nested = [[1, 2], [3, 4], [5, 6]]    # 2D list (matrix)

# Indexing (same as strings — starts at 0)
fruits[0]         # "apple"
fruits[-1]        # "cherry"

# Slicing
fruits[0:2]       # ["apple", "banana"]
fruits[::-1]      # ["cherry", "banana", "apple"] (reverse)

# Adding items
fruits.append("orange")      # Add to end          → ["apple", "banana", "cherry", "orange"]
fruits.insert(1, "mango")    # Insert at index 1   → ["apple", "mango", "banana", "cherry", "orange"]
fruits.extend(["grape", "kiwi"])  # Add multiple   → ["apple", ..., "grape", "kiwi"]

# Removing items
fruits.remove("banana")      # Remove by VALUE     (removes first match)
fruits.pop()                 # Remove last item    (returns it)
fruits.pop(1)                # Remove at index 1   (returns it)
fruits.clear()               # Remove everything

# Other methods
fruits.index("apple")        # Find index of value (0)
fruits.count("apple")        # Count occurrences
fruits.sort()                # Sort in-place (ascending)
fruits.sort(reverse=True)    # Sort in-place (descending)
sorted(fruits)               # Returns new sorted list (doesn't modify original)
len(fruits)                  # Number of items
"apple" in fruits            # True/False — check if exists

# Copying lists
new_list = fruits.copy()     # Proper copy (shallow)
wrong = fruits               # This is a REFERENCE, not a copy!

# List comprehension — create lists in one line
squares = [x**2 for x in range(10)]            # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
evens = [x for x in range(20) if x % 2 == 0]   # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

---

## 7.5 Tuples

```python
# Tuple = IMMUTABLE (can't change after creation)
point = (3, 4)
coordinates = (10, 20, 30)
single = (5,)               # Note comma! (5) would be just int

# Access same as list
point[0]          # 3
point[-1]         # 4

# CANNOT do: point[0] = 99  (tuple is immutable)

# Unpacking
x, y = point                # x=3, y=4
a, b, c = coordinates       # a=10, b=20, c=30

# Useful for returning multiple values from a function
def get_min_max(arr):
    return min(arr), max(arr)

low, high = get_min_max([3, 1, 7, 2, 9])   # low=1, high=9
```

---

## 7.6 Dictionaries

```python
# Key → Value pairs
student = {
    "name": "Alice",
    "age": 17,
    "grade": "A"
}

# Accessing
student["name"]             # "Alice"
student.get("name")         # "Alice"
student.get("address")      # None (doesn't crash!)
student.get("address", "N/A")  # "N/A" (default if not found)
student.keys()              # dict_keys(["name", "age", "grade"])
student.values()            # dict_values(["Alice", 17, "A"])
student.items()             # dict_items([("name", "Alice"), ("age", 17), ("grade", "A")])

# Adding / updating
student["address"] = "123 Main St"    # Add new key
student["age"] = 18                    # Update existing key
student.update({"grade": "A*", "year": 2026})  # Add/update multiple

# Removing
del student["address"]                 # Remove key
removed = student.pop("grade")         # Remove and return value
student.clear()                        # Remove everything

# Checking
"name" in student           # True
"address" not in student    # True

# Check if empty
if student:                 # True if dict has ANY keys
    print("Has data")

# Copy
copy = student.copy()
```

---

## 7.7 `def` — Writing Functions

```python
# Basic function
def greet(name):
    """Takes a name and returns a greeting"""    # Docstring
    return f"Hello, {name}!"

# Calling
print(greet("Alice"))       # Hello, Alice!

# Multiple parameters
def add(a, b):
    return a + b

# Default parameters
def power(base, exp=2):     # exp defaults to 2
    return base ** exp

power(5)                    # 25 (5²)
power(5, 3)                 # 125 (5³)

# Named arguments
def introduce(name, age, city):
    return f"{name} is {age} from {city}"

introduce(age=17, name="Bob", city="London")  # Order doesn't matter with names!

# Multiple return values (returns a tuple)
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide(10, 3)        # q=3, r=1

# docstring — explains what the function does
def my_function():
    """This is a docstring — describes what this function does"""
    pass

# Scope — variables inside functions are LOCAL
x = 10          # GLOBAL variable

def func():
    x = 5       # LOCAL — different from global x!
    print(x)    # 5

func()
print(x)        # 10 (global unchanged)

# To modify a global variable inside a function:
counter = 0
def increment():
    global counter
    counter += 1
```

---

## 7.8 `__init__` — The Constructor

(Covered in detail in Part 1, but here's the cheat-sheet:)

```python
class ClassName:
    def __init__(self, param1, param2):
        # self = "this specific object"
        # __ = private (encapsulation)
        self.__param1 = param1
        self.__param2 = param2

    def get_param1(self):     # Getter
        return self.__param1

    def set_param1(self, v):  # Setter
        self.__param1 = v

# Creating an object calls __init__ automatically
obj = ClassName("value1", "value2")
```

**Key facts:**
- `__init__` runs **automatically** when you create an object
- `self` is always the first parameter — refers to the current object
- You don't pass `self` — Python does it for you
- Private attributes use `__` (double underscore) prefix
- Getter = method that returns a private attribute
- Setter = method that modifies a private attribute (with validation)

---

## 7.9 All Types of Loops

### `for` loop with `range()`

```python
# range(stop)          — 0 to stop-1
for i in range(5):
    print(i)           # 0, 1, 2, 3, 4

# range(start, stop)   — start to stop-1
for i in range(2, 7):
    print(i)           # 2, 3, 4, 5, 6

# range(start, stop, step)  — step can be negative
for i in range(0, 10, 2):
    print(i)           # 0, 2, 4, 6, 8

for i in range(10, 0, -2):
    print(i)           # 10, 8, 6, 4, 2
```

### `for` loop over a list

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)       # apple, banana, cherry
```

### `for` loop with index (`enumerate`)

```python
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# enumerate with custom start index
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")
# 1: apple
# 2: banana
# 3: cherry
```

### `for` loop over a string

```python
for char in "Hello":
    print(char)        # H, e, l, l, o
```

### `for` loop over a dictionary

```python
student = {"name": "Alice", "age": 17, "grade": "A"}

# Keys only (default)
for key in student:
    print(key)         # name, age, grade

# Values
for value in student.values():
    print(value)       # Alice, 17, A

# Both key and value
for key, value in student.items():
    print(f"{key} = {value}")
# name = Alice
# age = 17
# grade = A
```

### `for` loop with `zip()` (multiple lists together)

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 85
# Bob: 92
# Charlie: 78

# With index too
for i, (name, score) in enumerate(zip(names, scores)):
    print(f"{i}. {name}: {score}")
# 0. Alice: 85
# 1. Bob: 92
# 2. Charlie: 78
```

### Nested `for` loops

```python
# 2D list (matrix)
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in grid:
    for value in row:
        print(value, end=" ")
    print()            # Newline after each row
# 1 2 3
# 4 5 6
# 7 8 9

# Multiplication table
for i in range(1, 5):
    for j in range(1, 5):
        print(f"{i×j}={i*j}", end="\t")
    print()
# 1×1=1   1×2=2   1×3=3   1×4=4
# 2×1=2   2×2=4   2×3=6   2×4=8
# ...
```

### `while` loop

```python
# Basic while — runs UNTIL condition becomes False
count = 0
while count < 5:
    print(count)
    count += 1         # DON'T forget this or infinite loop!
# 0, 1, 2, 3, 4

# While with input (sentinel loop)
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")

# Infinite loop with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break          # Exit the loop
    print(f"You said: {user_input}")
```

### `break` and `continue`

```python
# break — exit the loop immediately
for i in range(10):
    if i == 5:
        break          # Stop the loop
    print(i)           # 0, 1, 2, 3, 4

# continue — skip to the next iteration
for i in range(10):
    if i % 2 == 0:
        continue       # Skip even numbers
    print(i)           # 1, 3, 5, 7, 9

# break in nested loops — only breaks the INNER loop
for i in range(3):
    for j in range(3):
        if j == 1:
            break      # Only breaks the inner j-loop
        print(f"({i}, {j})")
# (0, 0)
# (1, 0)
# (2, 0)
```

### `else` with loops

```python
# else runs ONLY if the loop completed without break
for i in range(5):
    print(i)
else:
    print("Loop finished normally")    # THIS runs

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop finished normally")    # THIS does NOT run (break happened)

# Useful for search loops:
numbers = [1, 3, 5, 7, 9]
for n in numbers:
    if n == 6:
        print("Found!")
        break
else:
    print("Not found")    # Runs because break never happened
```

---

## 7.10 List Methods Cheat Sheet

| Method | What it does | Example |
|--------|-------------|---------|
| `append(x)` | Add x to end | `lst.append(5)` |
| `insert(i, x)` | Insert x at index i | `lst.insert(0, 5)` |
| `extend(iter)` | Add all items from iterable | `lst.extend([1,2,3])` |
| `remove(x)` | Remove first occurrence of x | `lst.remove("a")` |
| `pop(i)` | Remove & return item at i (default last) | `lst.pop()` |
| `clear()` | Remove all items | `lst.clear()` |
| `index(x)` | Return index of first x | `lst.index("a")` |
| `count(x)` | Count occurrences of x | `lst.count(5)` |
| `sort()` | Sort in-place (ascending) | `lst.sort()` |
| `sort(reverse=True)` | Sort descending | `lst.sort(reverse=True)` |
| `reverse()` | Reverse in-place | `lst.reverse()` |
| `copy()` | Return a shallow copy | `new = lst.copy()` |

---

## 7.11 Common Patterns

```python
# Finding min/max/sum in a list
nums = [3, 7, 1, 9, 4]
min(nums)           # 1
max(nums)           # 9
sum(nums)           # 24

# Check if all/any meet a condition
all(x > 0 for x in nums)    # True — all positive
any(x > 5 for x in nums)    # True — 7 and 9 are > 5

# Filter with list comprehension
evens = [x for x in nums if x % 2 == 0]      # [4]

# Map with list comprehension
doubled = [x * 2 for x in nums]              # [6, 14, 2, 18, 8]

# Swapping two variables
a, b = b, a              # No temp variable needed!

# Multiple assignment
a, b, c = 1, 2, 3

# Chained comparison
if 0 < score < 100:      # Same as: score > 0 and score < 100
    print("Valid")

# Join list of strings
words = ["Python", "is", "fun"]
sentence = " ".join(words)     # "Python is fun"

# Enumerate with start index
for i, val in enumerate(lst, start=1):
    print(i, val)
```
