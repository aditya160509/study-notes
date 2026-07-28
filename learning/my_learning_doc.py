"""
A Level CS 9618 - Complete Exam Guide (Python Only)
Chapter 27: OOP + Paper 4 ADTs, Searching & Sorting
"""

# =============================================================
# PART 1: OOP BASICS — Class, Object, Encapsulation
# =============================================================
print("=" * 60)
print("PART 1: OOP BASICS")
print("=" * 60)

class Dog:
    """Example 1: Simple class with private attributes"""
    def __init__(self, name, age):
        self.__name = name     # Private!
        self.__age = age

    def bark(self):
        return f"{self.__name} says WOOF!"

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age

my_dog = Dog("Buddy", 3)
print("=== Dog Class ===")
print(my_dog.bark())
print(f"Name: {my_dog.get_name()}, Age: {my_dog.get_age()}")
my_dog.set_age(4)
print(f"After set_age(4): {my_dog.get_age()}")
print()

class BankAccount:
    """Example 2: BankAccount with validation"""
    def __init__(self, holder, balance):
        self.__holder = holder
        self.__balance = balance
        self.__transactions = 0

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions += 1
            return f"Deposited ${amount}. Balance: ${self.__balance}"
        return "Amount must be positive!"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__transactions += 1
            return f"Withdrew ${amount}. Balance: ${self.__balance}"
        return "Insufficient funds!"

    def get_transactions(self):
        return self.__transactions

acc = BankAccount("Alice", 1000)
print("=== BankAccount ===")
print(f"Initial: ${acc.get_balance()}")
print(acc.deposit(500))
print(acc.withdraw(200))
print(f"Transactions: {acc.get_transactions()}")
print()


# =============================================================
# PART 2: INHERITANCE & POLYMORPHISM
# =============================================================
print("=" * 60)
print("PART 2: INHERITANCE & POLYMORPHISM")
print("=" * 60)

class Animal:
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def make_sound(self):
        return "Some sound..."
    def move(self):
        return f"{self.__name} is moving."

class Dog2(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.__breed = breed
    def get_breed(self):
        return self.__breed
    def make_sound(self):
        return "WOOF!"
    def fetch(self):
        return f"{self.get_name()} is fetching!"

class Cat2(Animal):
    def __init__(self, name, lives):
        super().__init__(name)
        self.__lives = lives
    def make_sound(self):
        return "MEOW!"
    def purr(self):
        return "purrrrr..."

dog = Dog2("Rex", "German Shepherd")
cat = Cat2("Whiskers", 9)

print("=== Inheritance Demo ===")
print(dog.move())            # Inherited
print(cat.move())            # Inherited
print(dog.make_sound())      # Overridden
print(cat.make_sound())      # Overridden (different!)
print(dog.fetch())
print(cat.purr())

# Polymorphism demo
print("\n=== Polymorphism Demo ===")
animals = [Animal("Generic"), Dog2("Rex", "Hound"), Cat2("Kitty", 9)]
for a in animals:
    print(f"{a.get_name()} says: {a.make_sound()}")
print()


# =============================================================
# PART 3: ADTs - DATA STRUCTURES
# =============================================================
print("=" * 60)
print("PART 3: ADTs — DATA STRUCTURES")
print("=" * 60)

# --- NODE CLASS ---
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None 
    def get_data(self):    return self.__data
    def set_data(self, d): self.__data = d
    def get_next(self):    return self.__next
    def set_next(self, n): self.__next = n


# --- STACK (Array) ---
print("--- Stack (Array) ---")
class Stack:
    def __init__(self, size):
        self.__stack = [None] * size
        self.__top = -1
        self.__size = size
    def push(self, item):
        if self.__top >= self.__size - 1:
            return "Overflow!"
        self.__top += 1
        self.__stack[self.__top] = item
        return f"Pushed {item}"
    def pop(self):
        if self.__top == -1:
            return "Underflow!"
        item = self.__stack[self.__top]
        self.__stack[self.__top] = None
        self.__top -= 1
        return item
    def peek(self):
        if self.__top == -1: return None
        return self.__stack[self.__top]

s = Stack(5)
print(s.push(10)); print(s.push(20)); print(s.push(30))
print(f"Peek: {s.peek()}")
print(f"Pop: {s.pop()}")
print(f"Pop: {s.pop()}")
print(f"Pop: {s.pop()}")
print()


# --- QUEUE (Array - Circular) ---
print("--- Queue (Array) ---")
class Queue:
    def __init__(self, size):
        self.__queue = [None] * size
        self.__front = -1
        self.__back = -1
        self.__size = size
    def enqueue(self, item):
        if self.__back == -1:
            self.__front = 0
            self.__back = 0
        else:
            self.__back = (self.__back + 1) % self.__size
        self.__queue[self.__back] = item
        return f"Enqueued {item}"
    def dequeue(self):
        if self.__front == -1:
            return "Empty!"
        item = self.__queue[self.__front]
        if self.__front == self.__back:
            self.__front = -1
            self.__back = -1
        else:
            self.__front = (self.__front + 1) % self.__size
        return item
    def peek_front(self):
        if self.__front == -1: return None
        return self.__queue[self.__front]

q = Queue(5)
print(q.enqueue("Alice"))
print(q.enqueue("Bob"))
print(q.enqueue("Charlie"))
print(f"Dequeue: {q.dequeue()}")
print(f"Dequeue: {q.dequeue()}")
print(q.enqueue("Diana"))
print(f"Front: {q.peek_front()}")
print()


# --- LINKED LIST ---
print("--- Linked List ---")
class LinkedList:
    def __init__(self):
        self.__head = None
    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.set_next(self.__head)
        self.__head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = new_node
            return
        cur = self.__head
        while cur.get_next() is not None:
            cur = cur.get_next()
        cur.set_next(new_node)
    def delete(self, data):
        if self.__head is None: return
        if self.__head.get_data() == data:
            self.__head = self.__head.get_next()
            return
        cur = self.__head
        while cur.get_next() is not None:
            if cur.get_next().get_data() == data:
                cur.set_next(cur.get_next().get_next())
                return
            cur = cur.get_next()
    def display(self):
        result = []
        cur = self.__head
        while cur is not None:
            result.append(str(cur.get_data()))
            cur = cur.get_next()
        print(" → ".join(result) + " → None")

ll = LinkedList()
ll.insert_at_front("C")
ll.insert_at_front("B")
ll.insert_at_front("A")
ll.display()
ll.insert_at_end("D")
ll.display()
ll.delete("B")
ll.display()
print()


# --- BINARY SEARCH TREE ---
print("--- Binary Search Tree ---")
class TreeNode:
    def __init__(self, data):
        self.__data = data
        self.__left = None
        self.__right = None
    def get_data(self):   return self.__data
    def get_left(self):   return self.__left
    def get_right(self):  return self.__right
    def set_left(self,n): self.__left = n
    def set_right(self,n):self.__right = n

class BST:
    def __init__(self):
        self.__root = None
    def insert(self, data):
        new = TreeNode(data)
        if self.__root is None:
            self.__root = new
            return
        cur = self.__root
        while True:
            if data < cur.get_data():
                if cur.get_left() is None:
                    cur.set_left(new); return
                cur = cur.get_left()
            else:
                if cur.get_right() is None:
                    cur.set_right(new); return
                cur = cur.get_right()
    def inorder(self):
        r = []
        self.__inorder_r(self.__root, r)
        return r
    def __inorder_r(self, n, r):
        if n:
            self.__inorder_r(n.get_left(), r)
            r.append(n.get_data())
            self.__inorder_r(n.get_right(), r)
    def preorder(self):
        r = []
        self.__preorder_r(self.__root, r)
        return r
    def __preorder_r(self, n, r):
        if n:
            r.append(n.get_data())
            self.__preorder_r(n.get_left(), r)
            self.__preorder_r(n.get_right(), r)
    def postorder(self):
        r = []
        self.__postorder_r(self.__root, r)
        return r
    def __postorder_r(self, n, r):
        if n:
            self.__postorder_r(n.get_left(), r)
            self.__postorder_r(n.get_right(), r)
            r.append(n.get_data())
    def search(self, data):
        cur = self.__root
        while cur:
            if data == cur.get_data(): return True
            elif data < cur.get_data(): cur = cur.get_left()
            else: cur = cur.get_right()
        return False

bst = BST()
bst.insert(50); bst.insert(30); bst.insert(70)
bst.insert(20); bst.insert(40); bst.insert(60); bst.insert(80)
print(f"Inorder (sorted): {bst.inorder()}")
print(f"Preorder: {bst.preorder()}")
print(f"Postorder: {bst.postorder()}")
print(f"Search 40: {bst.search(40)}")
print(f"Search 99: {bst.search(99)}")
print()


# --- GRAPH with BFS & DFS ---
print("--- Graph with BFS & DFS ---")
class Graph:
    def __init__(self):
        self.__adj = {}
    def add_node(self, n):
        if n not in self.__adj:
            self.__adj[n] = []
    def add_edge(self, n1, n2):
        if n1 in self.__adj and n2 in self.__adj:
            self.__adj[n1].append(n2)
            self.__adj[n2].append(n1)
    def bfs(self, start):
        visited = set()
        queue = [start]
        order = []
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                for nb in self.__adj[node]:
                    if nb not in visited:
                        queue.append(nb)
        return order
    def dfs(self, start):
        visited = set()
        stack = [start]
        order = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                for nb in self.__adj[node]:
                    if nb not in visited:
                        stack.append(nb)
        return order

g = Graph()
for n in ["A","B","C","D","E"]: g.add_node(n)
g.add_edge("A","B"); g.add_edge("A","C")
g.add_edge("B","D"); g.add_edge("C","D"); g.add_edge("D","E")
print(f"BFS from A: {g.bfs('A')}")
print(f"DFS from A: {g.dfs('A')}")
print()


# =============================================================
# PART 4: SEARCHING & SORTING
# =============================================================
print("=" * 60)
print("PART 4: SEARCHING & SORTING")
print("=" * 60)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped: break
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > val:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = val
    return arr

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target: return mid
        elif arr[mid] > target: high = mid - 1
        else: low = mid + 1
    return -1

d1 = [64, 34, 25, 12, 22, 11, 90]
print(f"Bubble Sort: {d1} → ", end="")
bubble_sort(d1)
print(d1)

d2 = [12, 11, 13, 5, 6]
print(f"Insertion Sort: {d2} → ", end="")
insertion_sort(d2)
print(d2)

d3 = [2, 5, 8, 12, 16, 23, 38, 45, 56]
print(f"Binary Search 23: index {binary_search(d3, 23)}")
print(f"Binary Search 99: index {binary_search(d3, 99)}")
print()

# =============================================================
# PART 5: DEMO — OOP + ADTs Together
# =============================================================
print("=" * 60)
print("PART 5: OOP + ADTs — Library with Linked List")
print("=" * 60)

class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
    def get_title(self): return self.__title
    def get_author(self): return self.__author
    def __repr__(self):
        return f"'{self.__title}' by {self.__author}"

class Library:
    def __init__(self):
        self.__books = LinkedList()    # CONTAINMENT!
    def add_book(self, title, author):
        self.__books.insert_at_end(Book(title, author))
    def remove_book(self, title):
        self.__books.delete(title)
    def show_all(self):
        print("Library Collection:")
        cur = self.__books._LinkedList__head
        while cur:
            print(f"  {cur.get_data()}")
            cur = cur.get_next()

lib = Library()
lib.add_book("1984", "Orwell")
lib.add_book("Dune", "Herbert")
lib.add_book("Neuromancer", "Gibson")
lib.show_all()
print()

# =============================================================
# PART 6: PYTHON BASICS — Variables, Loops, Lists, Functions
# =============================================================
print("=" * 60)
print("PART 6: PYTHON BASICS")
print("=" * 60)

# --- Variables & Data Types ---
print("--- Variables & Data Types ---")
name = "Alice"; age = 17; height = 5.6; is_student = True
print(f"name={name} ({type(name).__name__}), age={age} ({type(age).__name__})")
print(f"height={height} ({type(height).__name__}), is_student={is_student} ({type(is_student).__name__})")
print()

# --- Strings ---
print("--- Strings ---")
text = "Hello World"
print(f"text[0]={text[0]}, text[-1]={text[-1]}, text[0:5]={text[0:5]}")
print(f"text[6:]={text[6:]}, text[::-1]={text[::-1]}")
print(f"upper={text.upper()}, split={text.split()}")
print(f"f-string: My name is {name} and I'm {age}")
print()

# --- if/elif/else ---
print("--- Conditions ---")
score = 75
if score >= 90: grade = "A"
elif score >= 70: grade = "B"
elif score >= 50: grade = "C"
else: grade = "F"
print(f"Score={score}, Grade={grade}")
status = "Pass" if score >= 50 else "Fail"
print(f"Status: {status}")
print()

# --- Lists ---
print("--- Lists ---")
fruits = ["apple", "banana", "cherry"]
print(f"fruits={fruits}, fruits[0]={fruits[0]}, fruits[-1]={fruits[-1]}")
fruits.append("orange"); print(f"after append: {fruits}")
fruits.insert(1, "mango"); print(f"after insert: {fruits}")
fruits.remove("banana"); print(f"after remove: {fruits}")
popped = fruits.pop(); print(f"popped={popped}, remaining={fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"sliced [0:2]: {fruits[0:2]}, reversed: {fruits[::-1]}")

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
print(f"squares={squares}")
print(f"evens={evens}")
print()

# --- Tuples ---
print("--- Tuples ---")
point = (3, 4)
x, y = point
print(f"point={point}, x={x}, y={y}")
coordinates = (10, 20, 30)
a, b, c = coordinates
print(f"unpacked: {a}, {b}, {c}")
print()

# --- Dictionaries ---
print("--- Dictionaries ---")
student = {"name": "Alice", "age": 17, "grade": "A"}
print(f"student['name']={student['name']}")
print(f"student.get('address')={student.get('address')}")
student["address"] = "123 Main St"
print(f"after add: {student}")
for key, value in student.items():
    print(f"  {key} = {value}")
print()

# --- Functions ---
print("--- Functions ---")
def greet(name):
    return f"Hello, {name}!"
def add(a, b):
    return a + b
def power(base, exp=2):
    return base ** exp
print(greet("Alice"))
print(f"add(3,4)={add(3,4)}")
print(f"power(5)={power(5)}, power(5,3)={power(5,3)}")
print()

# --- ALL TYPES OF FOR LOOPS ---
print("--- For Loops ---")

# range()
print("range(5):", end=" ")
for i in range(5):
    print(i, end=" ")
print()

print("range(2,7):", end=" ")
for i in range(2, 7):
    print(i, end=" ")
print()

print("range(0,10,2):", end=" ")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# over a list
print("fruits:", end=" ")
for fruit in fruits:
    print(fruit, end=" ")
print()

# enumerate
print("enumerate:")
for i, fruit in enumerate(fruits):
    print(f"  {i}: {fruit}")

# over a string
print("chars in 'Hello':", end=" ")
for char in "Hello":
    print(char, end=" ")
print()

# over dictionary
print("dict items:")
for key, value in student.items():
    print(f"  {key} = {value}")

# zip
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
print("zip:")
for name, score in zip(names, scores):
    print(f"  {name}: {score}")

# nested loop
print("nested (3x3 grid):")
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in grid:
    for val in row:
        print(val, end=" ")
    print()

# while loop
print("while:", end=" ")
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
print()

# break and continue
print("break at 5:", end=" ")
for i in range(10):
    if i == 5: break
    print(i, end=" ")
print()

print("continue (skip evens):", end=" ")
for i in range(10):
    if i % 2 == 0: continue
    print(i, end=" ")
print()

# for-else
print("for-else (not found):")
numbers = [1, 3, 5, 7, 9]
for n in numbers:
    if n == 6:
        print("Found!")
        break
else:
    print("Not found")     # Runs because 6 not in list
print()

print("=" * 60)
print("ALL DONE! Run: python3 my_learning_doc.py")
print("=" * 60)
