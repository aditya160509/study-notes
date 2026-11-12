# 📘 Chapter 23: Algorithms - Cambridge International AS & A Level Computer Science (9618)

## Cambridge International AS & A Level Computer Science - Part 4

> **Rule + fully solved examples.** Everything the examiner can ask from Chapter 23: linear and binary search, bubble and insertion sort, the standard ADTs (linked list, binary tree, stack, queue, graph, hash table, dictionary), and Big O time/space complexity. Pseudocode is given in the 9618 style, with Python equivalents where they help.

**Learning objectives (Chapter 23):**
- Write linear and binary search algorithms
- Write bubble sort and insertion sort algorithms
- Understand how performance depends on the initial order and size of the data
- Understand and use Abstract Data Types (ADTs)
- Implement stack, queue, linked list, binary tree, dictionary and graph ADTs
- Compare algorithms using time and space complexity
- Understand Big O notation for time and space

---

## 23.01 Linear Search

A **linear search** checks each item in turn until the target is found or the list ends.

**Pseudocode:**

```
FUNCTION LinearSearch(List, SearchItem) RETURNS INTEGER
    FOR Index ← 0 TO LENGTH(List) - 1
        IF List[Index] = SearchItem
            THEN
                RETURN Index          // found
        ENDIF
    NEXT Index
    RETURN -1                          // not found
ENDFUNCTION
```

**Python:**

```python
def linear_search(items, target):
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1
```

| Property | Value |
|---|---|
| Works on unordered data? | Yes |
| Best case | `O(1)` — target is first |
| Worst case | `O(n)` — target is last or absent |
| Average case | `O(n)` |
| Space | `O(1)` |

**Worked example 23.01 — trace `[7, 12, 19, 23, 27]`, target 23**

Compare 7 (no), 12 (no), 19 (no), 23 (yes) → found at index 3, four comparisons.

> **Exam tip:** if the question says "the list is ordered", do **not** automatically use a linear search — a binary search is more efficient and is usually what the mark scheme expects.

---

## 23.02 Bubble Sort

A **bubble sort** repeatedly compares adjacent items and swaps them if they are in the wrong order. After each pass, the largest remaining item "bubbles" to the end.

**Pseudocode (efficient version with early exit):**

```
PROCEDURE BubbleSort(List)
    n ← LENGTH(List)
    Swapped ← TRUE
    Pass ← 0
    WHILE Swapped AND Pass < n - 1 DO
        Swapped ← FALSE
        FOR Index ← 0 TO n - Pass - 2 DO
            IF List[Index] > List[Index + 1]
                THEN
                    Temp ← List[Index]
                    List[Index] ← List[Index + 1]
                    List[Index + 1] ← Temp
                    Swapped ← TRUE
            ENDIF
        NEXT Index
        Pass ← Pass + 1
    ENDWHILE
ENDPROCEDURE
```

**Python:**

```python
def bubble_sort(items):
    n = len(items)
    for pass_num in range(n - 1):
        swapped = False
        for i in range(n - pass_num - 1):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True
        if not swapped:
            break
    return items
```

**Worked example 23.02 — sort `[5, 1, 4, 2, 8]`**

| Pass | List after pass | Swaps |
|---|---|---|
| 1 | `[1, 4, 2, 5, 8]` | 5↔1, 5↔4, 5↔2 |
| 2 | `[1, 2, 4, 5, 8]` | 4↔2 |
| 3 | `[1, 2, 4, 5, 8]` | none — stop |

| Property | Value |
|---|---|
| Best case (already sorted) | `O(n)` with the early-exit flag |
| Worst/average case | `O(n²)` |
| Space | `O(1)` — in place |
| Stable? | Yes (equal items keep their relative order) |

> **Exam tip:** the efficient version uses a `Swapped` flag so that an already sorted list takes one pass. Without the flag, even a sorted list takes `n−1` passes, giving `O(n²)`.

---

## 23.03 Insertion Sort

An **insertion sort** builds a sorted section one item at a time. Each new item is inserted into its correct position among the already-sorted items, shifting larger items right.

**Pseudocode:**

```
PROCEDURE InsertionSort(List)
    FOR Pointer ← 1 TO LENGTH(List) - 1
        ItemToInsert ← List[Pointer]
        Current ← Pointer - 1
        WHILE Current >= 0 AND List[Current] > ItemToInsert DO
            List[Current + 1] ← List[Current]
            Current ← Current - 1
        ENDWHILE
        List[Current + 1] ← ItemToInsert
    NEXT Pointer
ENDPROCEDURE
```

**Python:**

```python
def insertion_sort(items):
    for pointer in range(1, len(items)):
        item = items[pointer]
        current = pointer - 1
        while current >= 0 and items[current] > item:
            items[current + 1] = items[current]
            current -= 1
        items[current + 1] = item
    return items
```

**Worked example 23.03 — sort `[53, 21, 60, 18, 42, 19]`**

| Pointer | Item | List after insertion |
|---|---|---|
| 1 | 21 | `[21, 53, 60, 18, 42, 19]` |
| 2 | 60 | `[21, 53, 60, 18, 42, 19]` |
| 3 | 18 | `[18, 21, 53, 60, 42, 19]` |
| 4 | 42 | `[18, 21, 42, 53, 60, 19]` |
| 5 | 19 | `[18, 19, 21, 42, 53, 60]` |

| Property | Value |
|---|---|
| Best case (already sorted) | `O(n)` — one comparison per item |
| Worst/average case | `O(n²)` — reverse order |
| Space | `O(1)` — in place |
| Stable? | Yes |

**Bubble vs insertion:**

- Both are `O(n²)` worst case and `O(1)` space.
- Insertion sort is usually faster on small or nearly sorted data because it shifts rather than swapping repeatedly.
- Bubble sort is simpler to trace but generally performs fewer well in practice.

---

## 23.04 Binary Search

A **binary search** works only on an **ordered** list. It checks the middle item and discards the half that cannot contain the target.

**Pseudocode:**

```
FUNCTION BinarySearch(List, SearchItem) RETURNS INTEGER
    First ← 0
    Last ← LENGTH(List) - 1
    Found ← FALSE
    WHILE First <= Last AND NOT Found DO
        Middle ← (First + Last) DIV 2
        IF List[Middle] = SearchItem
            THEN
                Found ← TRUE
            ELSE
                IF List[Middle] > SearchItem
                    THEN
                        Last ← Middle - 1
                    ELSE
                        First ← Middle + 1
                ENDIF
        ENDIF
    ENDWHILE
    IF Found
        THEN
            RETURN Middle
        ELSE
            RETURN -1
    ENDIF
ENDFUNCTION
```

**Python:**

```python
def binary_search(items, target):
    first, last = 0, len(items) - 1
    while first <= last:
        middle = (first + last) // 2
        if items[middle] == target:
            return middle
        if items[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
    return -1
```

**Worked example 23.04 — search for 60**

List: `[7, 12, 19, 23, 27, 33, 37, 41, 45, 56, 59, 60, 62, 71, 75, 80, 84, 88, 92, 99]`

| Iteration | First | Last | Middle | Value | Action |
|---|---|---|---|---|---|
| 1 | 0 | 19 | 9 | 56 | 56 < 60 → First = 10 |
| 2 | 10 | 19 | 14 | 75 | 75 > 60 → Last = 13 |
| 3 | 10 | 13 | 11 | 60 | found |

Three iterations. A linear search would have taken 12 comparisons.

**Performance:** each comparison halves the search area, so the maximum number of comparisons is about `log₂ n`.

| `n` | Max comparisons (approx.) |
|---|---|
| 10 | 4 |
| 100 | 7 |
| 1,000 | 10 |
| 1,000,000 | 20 |

| Property | Value |
|---|---|
| Requires ordered data? | Yes |
| Best case | `O(1)` — target is middle |
| Worst/average case | `O(log n)` |
| Space | `O(1)` iterative |

> **Exam tip:** the list must be **sorted** before a binary search. If the question asks for the "conditions necessary", say "the data must be in order" — that is the mark.

---

## 23.05 Abstract Data Types (ADTs)

An **Abstract Data Type** is a data structure defined by the **operations** that can be performed on it, not by its implementation. The user knows *what* it does, not *how* it is stored.

**Standard ADT operations:**

- create/initialise
- insert/add
- find/search
- delete/remove
- check empty/full
- traverse/output all

**Why use ADTs?**

- **Encapsulation:** the implementation can change without affecting code that uses the ADT.
- **Reusability:** the same operations work across programs.
- **Simpler design:** you reason at a higher level.
- **Implementation from other ADTs:** a stack can be built from an array or a linked list; a dictionary can be built from a hash table.

---

## 23.06 Linked Lists

A **linked list** stores each item in a **node** containing the data and a **pointer** to the next node. Nodes need not be contiguous in memory.

**Array implementation** uses parallel arrays or an array of records, plus:

- `StartPointer` — index of the first node (`-1` if empty).
- `FreeListPtr` — index of the first free node.
- Each node has `Data` and `Pointer` (next index).

**Initialise:**

```
StartPointer ← -1
FreeListPtr ← 0
FOR Index ← 0 TO Max - 2
    List[Index].Pointer ← Index + 1
NEXT Index
List[Max - 1].Pointer ← -1
```

**Insert (ordered):**

1. Take a node from the free list.
2. Store the data.
3. Traverse to find the insertion point.
4. Update pointers so the new node links into the list.
5. If inserting at the start, update `StartPointer`.

**Find:**

```
Current ← StartPointer
WHILE Current <> -1 AND List[Current].Data <> Target DO
    Current ← List[Current].Pointer
ENDWHILE
RETURN Current
```

**Delete:**

1. Find the node and remember the previous node.
2. Point the previous node's pointer to the deleted node's next node.
3. Return the deleted node to the free list.
4. If deleting the first node, update `StartPointer`.

**Python (object-based):**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def insert(self, data):
        new = Node(data)
        if self.start is None or data < self.start.data:
            new.next = self.start
            self.start = new
            return
        current = self.start
        while current.next and current.next.data < data:
            current = current.next
        new.next = current.next
        current.next = new

    def find(self, target):
        current = self.start
        while current:
            if current.data == target:
                return current
            current = current.next
        return None
```

| Operation | Array list | Linked list |
|---|---|---|
| Access by index | `O(1)` | `O(n)` |
| Insert/delete at start | `O(n)` | `O(1)` |
| Insert/delete in middle | `O(n)` | `O(n)` to find + `O(1)` to relink |
| Memory | Contiguous | Extra pointer per node |
| Size | Fixed (usually) | Can grow dynamically |

> **Exam tip:** linked-list questions almost always test pointer updates. Draw the nodes and arrows before writing code; a wrong pointer loses all subsequent marks.

---

## 23.07 Binary Trees

A **binary tree** has nodes with at most two children (left and right). An **ordered binary tree (binary search tree)** maintains:

- left subtree values **<** node value,
- right subtree values **>** node value.

**Insert:**

1. Start at the root.
2. If the new value is smaller, go left; if larger, go right.
3. Repeat until a null pointer is found.
4. Insert the new node there.

**Find:**

1. Start at the root.
2. Compare the target with the current node.
3. Go left/right accordingly.
4. Stop when found or a null pointer is reached.

**Array implementation:** each node record stores `Data`, `LeftPointer`, `RightPointer`; `RootPointer` and `FreePtr` manage the tree.

**Python (object-based):**

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return TreeNode(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def find(root, target):
    while root:
        if target == root.data:
            return root
        root = root.left if target < root.data else root.right
    return None
```

**Traversals:**

- **In-order** (left, node, right) — gives values in ascending order for a BST.
- **Pre-order** (node, left, right) — useful for copying a tree.
- **Post-order** (left, right, node) — useful for deleting a tree.

| Operation | Balanced BST | Unbalanced (worst) |
|---|---|---|
| Search | `O(log n)` | `O(n)` |
| Insert | `O(log n)` | `O(n)` |
| Space | `O(n)` | `O(n)` |

> **Exam tip:** a BST is fast only if it is reasonably balanced. Inserting already-sorted data creates a chain, degrading search to `O(n)`.

---

## 23.08 Stacks

A **stack** is **LIFO** (last in, first out): the last item pushed is the first popped.

**Operations:** `push(item)`, `pop()`, `peek()`/`top()`, `isEmpty()`, `isFull()`.

**Array implementation:**

- `TopOfStackPointer` starts at `-1`.
- `push`: increment top, store item (check for full).
- `pop`: read item, decrement top (check for empty).

**Pseudocode:**

```
PROCEDURE Push(NewItem)
    IF Top < Max - 1
        THEN
            Top ← Top + 1
            Stack[Top] ← NewItem
    ENDIF
ENDPROCEDURE

FUNCTION Pop() RETURNS STRING
    IF Top > -1
        THEN
            Item ← Stack[Top]
            Top ← Top - 1
            RETURN Item
    ENDIF
    RETURN ""
ENDFUNCTION
```

**Python:**

```python
class Stack:
    def __init__(self, size):
        self.items = [None] * size
        self.top = -1

    def push(self, item):
        if self.top == len(self.items) - 1:
            raise OverflowError("stack full")
        self.top += 1
        self.items[self.top] = item

    def pop(self):
        if self.top == -1:
            raise IndexError("stack empty")
        item = self.items[self.top]
        self.top -= 1
        return item
```

**Uses:** function call stack, undo operations, expression evaluation (RPN), backtracking, depth-first search.

| Operation | Complexity |
|---|---|
| push | `O(1)` |
| pop | `O(1)` |
| peek | `O(1)` |
| space | `O(n)` |

---

## 23.09 Queues

A **queue** is **FIFO** (first in, first out): the first item added is the first removed.

**Operations:** `enqueue(item)`, `dequeue()`, `isEmpty()`, `isFull()`.

**Circular queue implementation:**

- `Front` points to the first item.
- `End` points to the last item.
- `NumberInQueue` counts items, making empty/full checks easy.
- When a pointer passes the end of the array, it **wraps around** to 0.

**Pseudocode:**

```
PROCEDURE AddToQueue(NewItem)
    IF NumberInQueue < Max
        THEN
            End ← End + 1
            IF End > Max - 1 THEN End ← 0 ENDIF
            Queue[End] ← NewItem
            NumberInQueue ← NumberInQueue + 1
    ENDIF
ENDPROCEDURE

FUNCTION RemoveFromQueue() RETURNS STRING
    IF NumberInQueue > 0
        THEN
            Item ← Queue[Front]
            NumberInQueue ← NumberInQueue - 1
            IF NumberInQueue = 0
                THEN
                    Front ← -1
                    End ← -1
                ELSE
                    Front ← Front + 1
                    IF Front > Max - 1 THEN Front ← 0 ENDIF
            ENDIF
            RETURN Item
    ENDIF
    RETURN ""
ENDFUNCTION
```

**Python:**

```python
class Queue:
    def __init__(self, size):
        self.items = [None] * size
        self.front = 0
        self.end = -1
        self.count = 0

    def enqueue(self, item):
        if self.count == len(self.items):
            raise OverflowError("queue full")
        self.end = (self.end + 1) % len(self.items)
        self.items[self.end] = item
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise IndexError("queue empty")
        item = self.items[self.front]
        self.front = (self.front + 1) % len(self.items)
        self.count -= 1
        return item
```

**Uses:** printer queue, keyboard buffer, task scheduling, breadth-first search.

| Operation | Complexity |
|---|---|
| enqueue | `O(1)` |
| dequeue | `O(1)` |
| space | `O(n)` |

> **Exam tip:** without wrap-around, a queue wastes space as `Front` moves forward. A circular queue reuses the freed slots; `NumberInQueue` distinguishes empty from full when `Front == End`.

---

## 23.10 Graphs

A **graph** is an ADT made of **vertices (nodes)** and **edges**. It records relationships between things.

| Term | Meaning |
|---|---|
| **Vertex/node** | An object/place/state |
| **Edge** | A connection between two vertices |
| **Weighted graph** | Edges have numerical labels (distance, cost, time) |
| **Directed graph** | Edges have a direction (one-way) |
| **Undirected graph** | Edges work both ways |
| **Adjacent/neighbour** | Two vertices joined by an edge |
| **Path** | A sequence of vertices connected by edges |
| **Cycle** | A path that returns to its start |

**Representations:**

1. **Adjacency matrix** — a 2D array where `matrix[i][j] = weight` if there is an edge, otherwise 0/∞.
   - Fast edge lookup `O(1)`.
   - Uses `O(n²)` space, even for sparse graphs.
2. **Adjacency list** — each vertex stores a list of its neighbours (and weights).
   - Uses `O(n + e)` space.
   - Slower to test a specific edge.

**Uses:** transport networks, social networks, web links, circuit design, state spaces in AI, shortest-path problems (Dijkstra/A\*).

**Traversal:**

- **Breadth-first search (BFS)** — uses a queue; explores neighbours level by level.
- **Depth-first search (DFS)** — uses a stack/recursion; follows one path as far as possible before backtracking.

---

## 23.11 Hash Tables

A **hash table** stores records for direct access using a **hash function** that converts a key into an array index.

**Hash function example:** `Hash(key) = key MOD Max` (for integer keys), or sum of character codes MOD table size for strings.

**Collision:** two keys hash to the same index. **Linear probing** resolves it by checking the next slot, wrapping around at the end.

**Insert:**

```
Index ← Hash(NewRecord.Key)
WHILE HashTable[Index] is not empty DO
    Index ← Index + 1
    IF Index > Max THEN Index ← 0 ENDIF
ENDWHILE
HashTable[Index] ← NewRecord
```

**Find:**

```
Index ← Hash(SearchKey)
WHILE HashTable[Index] is not empty
      AND HashTable[Index].Key <> SearchKey DO
    Index ← Index + 1
    IF Index > Max THEN Index ← 0 ENDIF
ENDWHILE
IF HashTable[Index] is not empty
    THEN RETURN HashTable[Index]
ENDIF
```

| Property | Value |
|---|---|
| Average search/insert | `O(1)` |
| Worst case (many collisions) | `O(n)` |
| Space | `O(n)` |
| Order maintained? | No |

> **Exam tip:** a hash table is fast because it computes the address rather than searching. Collisions are unavoidable when the number of keys exceeds the number of slots (pigeonhole principle), so a collision-resolution method is required.

---

## 23.12 Dictionaries

A **dictionary** is an ADT storing **key–value pairs**. The key is used to look up the value, like a word in a dictionary.

- Usually implemented with a **hash table**, giving average `O(1)` lookup.
- Keys must be unique.
- Order is not usually guaranteed.

**Python:**

```python
english_french = {}
english_french["book"] = "livre"
english_french["pen"] = "stylo"
print(english_french["book"])      # livre

computing_terms = {"Boolean": "TRUE or FALSE", "Bit": "0 or 1"}
print(computing_terms["Bit"])      # 0 or 1

for key, value in english_french.items():
    print(key, "->", value)
```

**Pseudocode structure:**

```
TYPE DictionaryEntry
    DECLARE Key : STRING
    DECLARE Value : STRING
ENDTYPE
DECLARE EnglishFrench : ARRAY[0:999] OF DictionaryEntry
```

Insert and lookup use the same hash function and linear-probing logic as Section 23.11.

---

## 23.13 Big O Notation

**Big O notation** describes how an algorithm's running time or memory use grows as the input size `n` grows. It focuses on the **worst case** and ignores constant factors and smaller terms.

Example: if comparisons `= ½n² − ½n`, then for large `n` the `n²` term dominates, so the complexity is `O(n²)`.

### 23.13.1 Common orders

| Order | Name | Example | Growth |
|---|---|---|---|
| `O(1)` | Constant | Access `List[0]`; push/pop | Does not change with `n` |
| `O(log n)` | Logarithmic | Binary search | Halves the data each step |
| `O(n)` | Linear | Linear search; one pass through a list | Proportional to `n` |
| `O(n log n)` | Log-linear | Merge sort, efficient general sorting | Better than `n²` for large `n` |
| `O(n²)` | Quadratic | Bubble sort, insertion sort (worst) | Nested loops |
| `O(n³)` | Cubic | Triple nested loops | Deeper nesting |
| `O(2ⁿ)` | Exponential | Naive recursive Fibonacci | Doubles with each extra input |

### 23.13.2 Deriving the order

**Bubble sort comparisons:**

`(n−1) + (n−2) + ... + 1 = ½n(n−1) = ½n² − ½n`

Drop constants and lower-order terms → `O(n²)`.

**Binary search:** each iteration halves the remaining items. After `k` iterations, `n/2^k` items remain. The search ends when `n/2^k = 1`, so `k = log₂ n` → `O(log n)`.

**Linear search:** one comparison per item in the worst case → `O(n)`.

### 23.13.3 Time vs space complexity

- **Time complexity:** number of basic operations (comparisons, assignments) as a function of `n`.
- **Space complexity:** extra memory required as a function of `n`.

| Algorithm | Time (worst) | Space |
|---|---|---|
| Linear search | `O(n)` | `O(1)` |
| Binary search | `O(log n)` | `O(1)` |
| Bubble sort | `O(n²)` | `O(1)` |
| Insertion sort | `O(n²)` | `O(1)` |
| Merge sort | `O(n log n)` | `O(n)` |
| Linked list traversal | `O(n)` | `O(1)` |
| Stack push/pop | `O(1)` | `O(n)` total |
| Hash table lookup | `O(1)` average | `O(n)` total |
| BST search (balanced) | `O(log n)` | `O(n)` total |

> **Exam tip:** "space complexity `O(1)`" for bubble/insertion sort means they sort **in place** and need only a few temporary variables, not that they use no memory at all.

### 23.13.4 Choosing an algorithm

- Small or nearly sorted data → insertion sort is often fastest in practice.
- Large unordered data → merge sort or another `O(n log n)` algorithm.
- Ordered data with random access → binary search.
- Frequent insertion/deletion → linked list.
- Direct lookup by key → hash table/dictionary.
- Hierarchical ordered data → binary search tree.

---

## 📝 Exam-style Questions with Full Solutions

### Question 1 — Binary search (7 marks)

The array `Names[0:50]` is sorted. Complete a binary search function and state the maximum number of comparisons for 51 items.

**Solution:**

```
FUNCTION FindName(s : STRING) RETURNS INTEGER
    Index ← -1
    First ← 0
    Last ← 50
    WHILE First <= Last AND Index = -1 DO
        Middle ← (First + Last) DIV 2
        IF Names[Middle] = s
            THEN
                Index ← Middle
            ELSE
                IF Names[Middle] < s
                    THEN
                        First ← Middle + 1
                    ELSE
                        Last ← Middle - 1
                ENDIF
        ENDIF
    ENDWHILE
    RETURN Index
ENDFUNCTION
```

For 51 items, the maximum is `⌈log₂ 51⌉ = 6` comparisons (2⁵ = 32 < 51 ≤ 64 = 2⁶).

**What the examiner wants:** correct boundary updates (`Middle ± 1`), a loop condition that terminates, and `-1` for not found.

### Question 2 — Sort trace (6 marks)

Trace one pass of bubble sort on `[29, 13, 41, 7, 22]` and state the list after the pass.

**Solution:**

- 29 > 13 → swap → `[13, 29, 41, 7, 22]`
- 29 < 41 → no swap
- 41 > 7 → swap → `[13, 29, 7, 41, 22]`
- 41 > 22 → swap → `[13, 29, 7, 22, 41]`

After pass 1: `[13, 29, 7, 22, 41]`. The largest item (41) is in its final position.

### Question 3 — Linked list pointers (6 marks)

A linked list is stored in an array. `StartPointer = 2`, and the nodes are:

| Index | Data | Pointer |
|---|---|---|
| 0 | D | 4 |
| 1 | B | 0 |
| 2 | A | 1 |
| 3 | — | 5 |
| 4 | E | -1 |

(a) Write the list in order.
(b) Describe the pointer changes needed to insert `C` at index 3 between B and D.

**Solution:**

(a) Start at index 2 → A. A points to 1 → B. B points to 0 → D. D points to 4 → E. E points to `-1`, the end.

Order: **A → B → D → E**.

(b) Insert `C` at index 3 between B and D:

1. Take node 3 from the free list (update `FreeListPtr` to 5).
2. Set `List[3].Data = "C"`.
3. Set `List[3].Pointer = List[1].Pointer` — B currently points to D at index 0, so C must point to 0.
4. Set `List[1].Pointer = 3` — B now points to C.

The chain becomes `2(A) → 1(B) → 3(C) → 0(D) → 4(E) → -1`.

**What the examiner wants:** take from free list, set the new node's pointer to the successor, then update the predecessor's pointer. Order matters: update the new node first, then the predecessor.

### Question 4 — Stack and queue (6 marks)

(a) State the difference between a stack and a queue.
(b) Give one use of each.
(c) Explain what happens when `pop` is called on an empty stack.

**Solution:**

(a) A stack is LIFO — the last item pushed is the first popped. A queue is FIFO — the first item enqueued is the first dequeued.

(b) Stack: undo history, function calls, expression evaluation. Queue: printer jobs, keyboard buffer, task scheduling.

(c) `pop` on an empty stack causes an **underflow**. A well-written implementation checks `Top == -1` (or `isEmpty()`) and returns an error/empty value instead of reading invalid memory.

### Question 5 — Big O (5 marks)

State the time complexity of each and justify it.

(a) Linear search of 1,000 items.
(b) Binary search of 1,000 sorted items.
(c) Bubble sort of 1,000 items.

**Solution:**

(a) `O(n)` — in the worst case every item is compared once.
(b) `O(log n)` — each comparison halves the search area; about 10 comparisons for 1,000 items.
(c) `O(n²)` — two nested loops, giving about `n²/2` comparisons; the dominant term is `n²`.

### Question 6 — Hash table collision (5 marks)

A hash table has 10 slots and uses `Hash(key) = key MOD 10` with linear probing. Insert keys 23, 13, 33, 43.

**Solution:**

- 23 → slot 3.
- 13 → slot 3 occupied → slot 4.
- 33 → slot 3 occupied, 4 occupied → slot 5.
- 43 → slots 3, 4, 5 occupied → slot 6.

All four keys collide at slot 3, creating a **cluster**. Search time for these keys degrades towards `O(n)` because each probe checks the next slot.

**What the examiner wants:** correct indices and the term "collision"/"linear probing". Mentioning clustering earns the explanation mark.

---

# 📋 Formula / Fact Sheet (Chapter 23)

**Searching:**

- Linear: check each item; `O(n)`; works unsorted.
- Binary: ordered data; compare middle, discard half; `O(log n)`.

**Sorting:**

- Bubble: compare adjacent, swap; `O(n²)` worst, `O(n)` best with flag; `O(1)` space.
- Insertion: insert each item into sorted section; `O(n²)` worst, `O(n)` best; `O(1)` space.

**ADTs:** stack (LIFO), queue (FIFO), linked list (nodes + pointers), binary tree (≤2 children; BST ordered), graph (vertices + edges), hash table (key → index), dictionary (key–value).

**Linked list:** `StartPointer`, `FreeListPtr`, node = data + next pointer; insert/delete by relinking.

**BST:** left < node < right; search/insert `O(log n)` balanced, `O(n)` unbalanced; in-order traversal gives sorted order.

**Stack:** push/pop at top; `Top = -1` means empty.

**Queue:** enqueue at end, dequeue at front; circular queue uses modulo/wrap-around; `NumberInQueue` for empty/full.

**Graph:** adjacency matrix `O(n²)` space, `O(1)` edge check; adjacency list `O(n+e)` space.

**Hash table:** `index = hash(key)`; collision → linear probing; average `O(1)`, worst `O(n)`.

**Big O order (best → worst):** `O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ)`.

**Space:** bubble/insertion `O(1)`; merge sort `O(n)`; ADTs `O(n)`.

# ⚡ Quick Reference Card

1. **Binary search needs sorted data** — always state this.
2. **Binary search max comparisons** ≈ `log₂ n`; 1,000 items → about 10.
3. **Bubble sort** largest item settles at the end of each pass.
4. **Insertion sort** shifts larger items right, then inserts.
5. **Linked list insert/delete** = pointer changes, no shifting.
6. **BST in-order traversal** outputs ascending order.
7. **Stack = LIFO; queue = FIFO**; circular queue wraps pointers.
8. **Hash table** computes the address; collisions need probing/chaining.
9. **Big O drops constants** — `½n² − ½n` becomes `O(n²)`.
10. **`O(1)` space** means in place, not zero memory.
11. **Graph matrix vs list:** matrix fast lookup, list saves space on sparse graphs.
12. **Never forget underflow/overflow checks** in stack/queue code.
