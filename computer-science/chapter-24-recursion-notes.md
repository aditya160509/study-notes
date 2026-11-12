# 📘 Chapter 24: Recursion - Cambridge International AS & A Level Computer Science (9618)

## Cambridge International AS & A Level Computer Science - Part 4

> **Rule + fully solved examples.** Everything the examiner can ask from Chapter 24: the definition of recursion, base and general cases, writing recursive functions and procedures, tracing recursive calls, how the call stack and stack frames work, unwinding, and the benefits and drawbacks of recursion. Every section ends with worked examples and exam-style questions with full mark-earning solutions.

**Learning objectives (Chapter 24):**
- Show understanding of the essential features of recursion
- Show understanding of how recursion is expressed in a programming language
- Trace recursive algorithms
- Write recursive algorithms
- Show understanding of when recursion is beneficial
- Show awareness of what a compiler must do to translate recursive code, including stacks and unwinding

---

## 24.01 Concept of Recursion

A **recursive routine** is a function or procedure **defined in terms of itself**.

The classic example is factorial:

```
0! = 1                    ← base case
n! = n × (n − 1)!         ← general case (for n > 0)
```

So:

```
4! = 4 × 3!
   = 4 × 3 × 2!
   = 4 × 3 × 2 × 1!
   = 4 × 3 × 2 × 1 × 0!
   = 4 × 3 × 2 × 1 × 1
   = 24
```

> **KEY TERMS**
> - **Base case**: an explicit solution to a recursive function; it stops the recursion.
> - **General case**: a definition of the function in terms of itself, using a smaller or simpler input.
> - **Recursive call**: a call by a routine to itself.

### 24.01.1 The three rules of recursion

Every recursive routine must:

1. Have a **base case**.
2. Have a **general case**.
3. **Reach the base case** after a finite number of calls, for every valid starting point.

If the general case does not move towards the base case, the routine recurses forever until the call stack overflows.

**Worked example 24.01 — why `Factorial(-2)` fails**

`Factorial(-2)` checks `n = 0` — false — so it calls `Factorial(-3)`, then `Factorial(-4)`, and so on. The argument moves **away** from the base case, so rule 3 is broken. The result is infinite recursion and a stack overflow.

A correct definition restricts `n` to non-negative integers (or explicitly handles invalid input).

### 24.01.2 Recursive vs iterative thinking

| Iterative | Recursive |
|---|---|
| Uses a loop | Uses a call to itself |
| State carried in variables | State carried in parameters and stack frames |
| Usually more memory-efficient | Usually shorter and closer to the mathematical definition |
| Explicit termination condition | Base case |

The same problem can often be solved either way; the choice depends on clarity, performance and the shape of the problem.

---

## 24.02 Programming a Recursive Subroutine

### 24.02.1 Recursive function — factorial

**Pseudocode:**

```
FUNCTION Factorial(n : INTEGER) RETURNS INTEGER
    IF n = 0
        THEN
            Result ← 1                 // base case
        ELSE
            Result ← n * Factorial(n - 1)   // general case + recursive call
    ENDIF
    RETURN Result
ENDFUNCTION
```

**Python:**

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

**Iterative equivalent:**

```python
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

> **Exam tip:** the recursive call must use a **smaller** argument (`n - 1`), and the base case must return a value without calling itself. Both are usually separate marks.

### 24.02.2 Recursive procedure — countdown

A procedure does not return a value, but it can still recurse.

```
PROCEDURE CountDownFrom(n : INTEGER)
    OUTPUT n
    IF n > 0
        THEN
            CALL CountDownFrom(n - 1)
    ENDIF
ENDPROCEDURE
```

`CountDownFrom(3)` outputs `3, 2, 1, 0`.

### 24.02.3 Recursion before and after the call

The position of statements relative to the recursive call changes the order of output.

**Output before the call (countdown):**

```
PROCEDURE CountDown(n)
    OUTPUT n
    IF n > 0 THEN CALL CountDown(n - 1)
ENDPROCEDURE
```

`CountDown(3)` → `3 2 1 0` (work is done on the way **down** the recursion).

**Output after the call (count up):**

```
PROCEDURE CountUp(n)
    IF n > 0 THEN CALL CountUp(n - 1)
    OUTPUT n
ENDPROCEDURE
```

`CountUp(3)` → `0 1 2 3` (work is done on the way **back up**, as calls unwind).

**Worked example 24.02 — why the output reverses**

In `CountUp(3)`, the output statement is not reached until the recursive call returns. The calls nest:

```
CountUp(3)
  CountUp(2)
    CountUp(1)
      CountUp(0) → outputs 0
    outputs 1
  outputs 2
outputs 3
```

The innermost call finishes first, so the output appears in ascending order.

---

## 24.03 Tracing a Recursive Subroutine

A trace table records each call, the parameter values, the condition result, and the output/return value. When statements come after the recursive call, add the **unwinding** rows as the calls return.

### 24.03.1 Tracing a procedure

`CALL CountDownFrom(3)`:

| Call | Procedure call | Output | `n > 0` |
|---|---|---|---|
| 1 | `CountDownFrom(3)` | 3 | TRUE |
| 2 | `CountDownFrom(2)` | 2 | TRUE |
| 3 | `CountDownFrom(1)` | 1 | TRUE |
| 4 | `CountDownFrom(0)` | 0 | FALSE |

### 24.03.2 Tracing with unwinding

`CALL CountUp(3)`:

| Call | Procedure call | `n > 0` | Output |
|---|---|---|---|
| 1 | `CountUp(3)` | TRUE | — |
| 2 | `CountUp(2)` | TRUE | — |
| 3 | `CountUp(1)` | TRUE | — |
| 4 | `CountUp(0)` | FALSE | 0 |
| 3 | returns to `CountUp(1)` | TRUE | 1 |
| 2 | returns to `CountUp(2)` | TRUE | 2 |
| 1 | returns to `CountUp(3)` | TRUE | 3 |

> **Exam tip:** do not fill in the output column on the way down and then go back up the table. Add **new rows** for the unwinding phase, as shown. This makes the order of execution clear and is what examiners expect.

### 24.03.3 Tracing a recursive function — factorial

`Factorial(4)`:

| Call | `n` | `n = 0`? | Result expression | Return value |
|---|---|---|---|---|
| 1 | 4 | FALSE | `4 * Factorial(3)` | — |
| 2 | 3 | FALSE | `3 * Factorial(2)` | — |
| 3 | 2 | FALSE | `2 * Factorial(1)` | — |
| 4 | 1 | FALSE | `1 * Factorial(0)` | — |
| 5 | 0 | TRUE | `1` | 1 |
| 4 | 1 | FALSE | `1 * 1` | 1 |
| 3 | 2 | FALSE | `2 * 1` | 2 |
| 2 | 3 | FALSE | `3 * 2` | 6 |
| 1 | 4 | FALSE | `4 * 6` | 24 |

The base case produces `1`, then each waiting call multiplies it by its own `n` as it unwinds.

**Worked example 24.03 — trace `Power(2, 4)`**

```
FUNCTION Power(Base, Exponent) RETURNS INTEGER
    IF Exponent = 0
        THEN Result ← 1
        ELSE Result ← Base * Power(Base, Exponent - 1)
    ENDIF
    RETURN Result
ENDFUNCTION
```

| Call | `Base` | `Exponent` | Result expression | Return |
|---|---|---|---|---|
| 1 | 2 | 4 | `2 * Power(2,3)` | — |
| 2 | 2 | 3 | `2 * Power(2,2)` | — |
| 3 | 2 | 2 | `2 * Power(2,1)` | — |
| 4 | 2 | 1 | `2 * Power(2,0)` | — |
| 5 | 2 | 0 | `1` | 1 |
| 4 | 2 | 1 | `2 * 1` | 2 |
| 3 | 2 | 2 | `2 * 2` | 4 |
| 2 | 2 | 3 | `2 * 4` | 8 |
| 1 | 2 | 4 | `2 * 8` | 16 |

`Power(2,4) = 16`.

---

## 24.04 Running a Recursive Subroutine

Recursion is executed using the **call stack**. Each call pushes a **stack frame** containing:

- the **return address** (where execution continues after the call),
- the **local variables and parameters** for that call,
- (in practice) saved registers and the return value.

### 24.04.1 Stack frames for `Factorial(3)`

The main program calls `Factorial(3)`:

| Stack (top on the right) | Meaning |
|---|---|
| `return 160` | main program calls `Factorial(3)` |
| `return 080, n=3` | `Factorial(3)` calls `Factorial(2)` |
| `return 080, n=3`, `return 080, n=2` | `Factorial(2)` calls `Factorial(1)` |
| `return 080, n=3`, `return 080, n=2`, `return 080, n=1` | `Factorial(1)` calls `Factorial(0)` |
| `... n=0` → returns 1 | base case reached |

Then the stack **unwinds**:

1. `Factorial(0)` returns 1; its frame is popped. `Factorial(1)` computes `1 × 1 = 1`.
2. `Factorial(1)` returns 1; its frame is popped. `Factorial(2)` computes `2 × 1 = 2`.
3. `Factorial(2)` returns 2; its frame is popped. `Factorial(3)` computes `3 × 2 = 6`.
4. `Factorial(3)` returns 6 to the main program.

**Key points:**

- Each recursive call adds one stack frame → memory grows with recursion depth.
- Each return removes one frame and restores the caller's local variables.
- The base case is the deepest point; after that, control unwinds back to the original caller.

### 24.04.2 Stack overflow

If recursion is too deep (or never reaches the base case), the stack runs out of space: **stack overflow**. A recursive countdown from 1,000,000 would need a million stack frames, which typical systems cannot provide.

> **Exam tip:** "the compiler uses a stack to store return addresses and local variables" is the standard mark for how recursion is implemented. Mention **stack frame** and **unwinding** for the top band.

### 24.04.3 Tail recursion

In **tail recursion**, the recursive call is the **last** operation, and its result is returned immediately:

```python
def factorial_tail(n, acc=1):
    if n == 0:
        return acc
    return factorial_tail(n - 1, acc * n)
```

Some compilers optimise tail recursion into a loop, using constant stack space. Python does not do this automatically, so deep tail recursion still overflows.

---

## 24.05 Benefits and Drawbacks of Recursion

### 24.05.1 Benefits

- **Closer to the mathematical definition** — factorial, Fibonacci, tree traversal and divide-and-conquer algorithms are naturally recursive.
- **Shorter, more elegant code** — often fewer lines than an iterative version.
- **Handles recursive data structures** — trees, nested lists and grammars are easier to traverse recursively.
- **Divide and conquer** — quicksort and merge sort split a problem into smaller subproblems.
- **Backtracking** — maze solving, puzzles and parsing are naturally recursive.

### 24.05.2 Drawbacks

- **Memory overhead** — each call uses a stack frame; deep recursion can overflow.
- **Processor overhead** — function calls, stack pushes and pops are slower than a loop.
- **Risk of infinite recursion** — a missing or unreachable base case crashes the program.
- **Harder to debug/trace** — the flow of control is less obvious than a loop.
- **Repeated work** — naive recursive Fibonacci recomputes the same values many times (`O(2ⁿ)`).

### 24.05.3 Recursion vs iteration

| Criterion | Recursion | Iteration |
|---|---|---|
| Code length | Often shorter | Usually longer |
| Readability for recursive problems | High | Lower |
| Memory | `O(depth)` stack frames | `O(1)` extra |
| Speed | Slower (call overhead) | Faster |
| Risk | Stack overflow | Infinite loop |
| Best for | Trees, divide and conquer, backtracking | Simple repetition, large linear loops |

### 24.05.4 Worked example — Fibonacci and memoization

**Naive recursive Fibonacci:**

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

This is `O(2ⁿ)` because `fib(n−2)` is recomputed many times.

**Memoized version:**

```python
def fib(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
```

Storing results reduces the time to `O(n)`, at the cost of `O(n)` memory. This is **dynamic programming**: recursion plus caching.

### 24.05.5 Worked example — recursive binary search

```python
def binary_search(items, target, first, last):
    if first > last:
        return -1
    middle = (first + last) // 2
    if items[middle] == target:
        return middle
    if items[middle] > target:
        return binary_search(items, target, first, middle - 1)
    return binary_search(items, target, middle + 1, last)
```

Each call halves the search area → `O(log n)` time, `O(log n)` stack space.

### 24.05.6 Worked example — tree traversal

```python
def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data)
    in_order(node.right)
```

The base case is the empty tree (`None`). The recursion visits every node once → `O(n)` time, `O(h)` stack space for height `h`.

---

## 📝 Exam-style Questions with Full Solutions

### Question 1 — Iteration vs recursion (4 marks)

(a) Outline two differences between iteration and recursion. [2]
(b) Give one advantage and one disadvantage of recursion. [2]

**Solution:**

(a) Iteration uses a loop and explicit loop variables; recursion uses a routine that calls itself with smaller arguments. Iteration usually uses constant extra memory; recursion uses a stack frame per call.

(b) Advantage: recursive code is often shorter and closer to the mathematical definition, especially for trees/divide-and-conquer. Disadvantage: each call uses stack memory, so deep recursion can cause stack overflow and is slower.

### Question 2 — Power function (15 marks)

The recursive function `Power(Base, Exponent)` returns `Base^Exponent`.

(a) State what "recursively defined" means. [1]
(b) Trace `Power(2, 4)` showing values passed and returned. [6]
(c) Explain the role of the stack. [3]
(d) Write an iterative version. [6]
(e) Give one reason the iterative version may be preferred. [1]

**Solution:**

(a) A routine defined in terms of itself, with a base case and a general case that moves towards the base case.

(b) See the trace table in Worked example 24.03: calls with exponents 4, 3, 2, 1, 0; returns 1, 2, 4, 8, 16.

(c) Each call pushes a stack frame holding the return address and the current `Base`/`Exponent` values. When the base case returns, frames are popped in reverse order and their results are multiplied. The stack preserves the suspended calculations.

(d)

```
FUNCTION PowerIterative(Base, Exponent) RETURNS INTEGER
    Result ← 1
    FOR i ← 1 TO Exponent
        Result ← Result * Base
    NEXT i
    RETURN Result
ENDFUNCTION
```

(e) It uses constant extra memory (no stack frames) and avoids stack overflow for large exponents; it is usually faster.

**What the examiner wants:** (b) every call and return; (c) "return address and local variables" plus "unwinding"; (d) correct loop bounds and accumulator.

### Question 3 — Trace with output after the call (6 marks)

Trace `X(4)` for:

```
PROCEDURE X(n)
    IF n > 0 THEN CALL X(n - 1)
    OUTPUT n
ENDPROCEDURE
```

State the output.

**Solution:**

Calls: `X(4) → X(3) → X(2) → X(1) → X(0)`. `X(0)` has `n > 0` false, so it outputs `0` and returns. Then each waiting call outputs its own `n` as it unwinds.

Output: **`0 1 2 3 4`**.

**What the examiner wants:** the reverse order caused by output after the recursive call. A common wrong answer is `4 3 2 1 0`, which would be correct only if the output came before the call.

### Question 4 — Factorial stack (5 marks)

Explain what happens on the call stack during `Factorial(3)`.

**Solution:**

The main program pushes a return address and calls `Factorial(3)`. That call pushes a frame with `n=3` and a return address, then calls `Factorial(2)`, which pushes `n=2`, then `Factorial(1)` pushes `n=1`, then `Factorial(0)` pushes `n=0`. `Factorial(0)` reaches the base case and returns 1. Its frame is popped. `Factorial(1)` multiplies `1 × 1` and returns 1; its frame is popped. `Factorial(2)` computes `2 × 1 = 2`; `Factorial(3)` computes `3 × 2 = 6`; each frame is popped in turn until control returns to the main program with 6.

### Question 5 — Naive Fibonacci (5 marks)

Explain why the naive recursive Fibonacci function is inefficient, and state one improvement.

**Solution:**

`fib(n)` calls `fib(n−1)` and `fib(n−2)`. The same subproblems are recomputed repeatedly — for example, `fib(n−2)` is computed once inside `fib(n−1)` and again directly. The number of calls grows exponentially, about `O(2ⁿ)`.

Improvement: **memoization** — store each computed value in a dictionary/array and reuse it. This reduces the time to `O(n)` (with `O(n)` extra memory). An iterative version using two variables is even more space-efficient (`O(1)`).

### Question 6 — When to use recursion (3 marks)

State three situations where recursion is a good choice.

**Solution:**

1. Traversing a tree or other recursively defined data structure.
2. Divide-and-conquer algorithms such as quicksort or merge sort.
3. Backtracking problems such as maze solving, parsing or the Towers of Hanoi.

---

# 📋 Formula / Fact Sheet (Chapter 24)

**Definition:** a recursive routine is defined in terms of itself.

**Three rules:** base case; general case; reaches the base case in a finite number of calls.

**Factorial:** `0! = 1`; `n! = n × (n−1)!`; time `O(n)`, stack `O(n)`.

**Power:** `Base^0 = 1`; `Base^n = Base × Base^(n−1)`; time `O(n)`.

**Fibonacci:** `fib(0)=0`, `fib(1)=1`, `fib(n)=fib(n−1)+fib(n−2)`; naive `O(2ⁿ)`, memoized `O(n)`.

**Call stack:** each call pushes a **stack frame** = return address + local variables/parameters; each return pops it; the process is called **unwinding**.

**Stack overflow:** recursion depth exceeds stack capacity, usually because the base case is missing or unreachable.

**Tail recursion:** recursive call is the last operation; can be optimised to a loop by some compilers.

**Recursion vs iteration:** recursion shorter but uses `O(depth)` memory and has call overhead; iteration is usually faster and uses `O(1)` extra memory.

# ⚡ Quick Reference Card

1. **Base case stops recursion; general case recurses with a smaller input.**
2. **Every recursive call must move towards the base case** — otherwise stack overflow.
3. **Output before the call** → descending order; **output after the call** → ascending order on unwinding.
4. **Trace tables need unwinding rows** — do not back-fill the output column.
5. **Each call = one stack frame** (return address + locals).
6. **Base case returns first; callers multiply/add on the way back up.**
7. **Recursion depth = memory use**; deep recursion risks stack overflow.
8. **Naive Fibonacci is `O(2ⁿ)`** — memoize to get `O(n)`.
9. **Recursion suits trees, divide-and-conquer and backtracking.**
10. **Iteration is better for simple repetition and very large loops.**
