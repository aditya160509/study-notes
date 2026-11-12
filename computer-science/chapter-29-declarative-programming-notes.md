# 📘 Chapter 29: Declarative Programming - Cambridge International AS & A Level Computer Science (9618)

## Cambridge International AS & A Level Computer Science - Part 4

> **Rule + fully solved examples.** Everything the examiner can ask from Chapter 29: declarative versus imperative programming, Prolog facts and rules, variables and instantiation, the anonymous variable, backtracking, recursion, and list processing. Every section ends with worked examples and exam-style questions with full mark-earning solutions.

**Learning objectives (Chapter 29):**
- Show understanding of and solve a problem by writing appropriate facts and rules based on supplied information
- Show understanding of and write code that can satisfy a goal using facts and rules

---

## 29.01 Declarative Programming Languages

Declarative languages describe **what** is true or what result is wanted; the system works out **how** to find it. Examples include:

- database query languages such as **SQL**,
- **regular expressions**,
- **logic programming** languages such as **Prolog**,
- **functional programming** languages.

**Prolog** is the logic programming language used in this chapter. It is widely used in artificial intelligence and expert systems.

| Imperative | Declarative |
|---|---|
| Programmer writes steps | Programmer writes facts and rules |
| "How" | "What" |
| Assignment, loops, control flow | Queries, inference, backtracking |
| Example: Python, Pascal | Example: Prolog, SQL |

---

## 29.02 Prolog Basics

Prolog has three basic constructs:

1. **Facts** — things that are true.
2. **Rules** — relationships that let Prolog infer new truths.
3. **Queries** — questions asked of the knowledge base.

A collection of clauses (facts and rules) is a **knowledge base**. A clause has the form:

```
Head :- Body.
```

- `:-` is read as "if".
- A comma in the body means **and**.
- A semicolon means **or**.
- Every clause and query ends with a **full stop** (`.`).

### 29.02.1 Terms

Prolog has a single data type, the **term**:

| Term type | Example | Notes |
|---|---|---|
| **Atom** | `paris`, `capitalCity` | Starts with a **lower-case** letter; no inherent meaning |
| **Number** | `42`, `3.14` | Integer or float |
| **Variable** | `City`, `_` | Starts with a **capital** letter or underscore |
| **Compound term** | `capitalCity(paris)` | A predicate with arguments |

A **predicate** is identified by its name and **arity** (number of arguments). `capitalCity(paris)` has arity 1, written `capitalCity/1`. `cityInCountry(paris, france)` has arity 2, written `cityInCountry/2`.

**Prolog is case-sensitive:** `paris` is an atom; `Paris` is a variable.

> **Exam tip:** a capital letter changes the meaning completely. `cityInCountry(berlin, Country)` asks "which country?"; `cityInCountry(berlin, country)` asks whether Berlin is in the literal atom `country`.

---

## 29.03 Facts in Prolog

A **fact** is a clause with no body. It states something that is unconditionally true.

```prolog
capitalCity(paris).
capitalCity(berlin).
capitalCity(cairo).
```

Meaning: Paris is a capital city; Berlin is a capital city; Cairo is a capital city.

**Queries:**

```prolog
?- capitalCity(paris).
true.

?- capitalCity(london).
false.
```

`false` does not mean London is not a capital in reality — it means the fact is **not in this knowledge base**.

### 29.03.1 Worked example — simple knowledge base

```prolog
vegetable(aubergine).
vegetable(potato).
vegetable(tomato).

meat(chicken).
meat(beef).
meat(lamb).

ingredient(tagine, aubergine, 250).
ingredient(tagine, tomato, 100).
ingredient(stew, beef, 400).
ingredient(stew, potato, 600).
```

Queries:

```prolog
?- vegetable(potato).
true.

?- ingredient(tagine, Ingredient, Amount).
Ingredient = aubergine, Amount = 250 ;
Ingredient = tomato, Amount = 100.
```

The semicolon asks Prolog for the **next** solution. It means "or".

---

## 29.04 Prolog Variables

A **variable** starts with a capital letter (or `_`). It is a placeholder that Prolog can **instantiate** (bind) to a value.

```prolog
cityInCountry(paris, france).
cityInCountry(berlin, germany).
cityInCountry(cairo, egypt).
cityInCountry(munich, germany).
```

**Query with one variable:**

```prolog
?- cityInCountry(berlin, Country).
Country = germany.
```

**Query with a variable in the first argument:**

```prolog
?- cityInCountry(City, germany).
City = berlin ;
City = munich.
```

Prolog finds the first matching fact, binds `City = berlin`, reports it, and waits. Typing `;` triggers **backtracking** to find another solution, giving `munich`. Typing `;` again gives `false` (no more solutions).

> **KEY TERM**
> **Instantiation:** binding a variable to a value. The `=` shown by Prolog means "is instantiated to", not assignment.

### 29.04.1 Variables are not assignment

In an imperative language, `X = 5` stores 5 in `X`. In Prolog, `X = 5` **unifies** `X` with 5. Once instantiated, `X` keeps that value for that branch of the search. Backtracking can undo the binding and try another.

---

## 29.05 The Anonymous Variable

The **anonymous variable** is written `_`. It matches anything, but you cannot refer to its value. Use it when you do not care about an argument.

```prolog
?- ingredient(tagine, Ingredient, _).
Ingredient = aubergine ;
Ingredient = tomato.
```

Here we want the ingredient names but not the amounts. `_` avoids creating a named variable that would appear in the output.

> **Exam tip:** each `_` is independent. `foo(_, _)` matches any two arguments; the two underscores are not the same variable.

---

## 29.06 Rules in Prolog

A **rule** has a head and a body:

```
Head :- Goal1, Goal2, ...
```

The head is true **if** all the goals in the body are true. The comma means **and**.

### 29.06.1 Grandparent rule

Knowledge base:

```prolog
parent(fred, jack).
parent(fred, alia).
parent(fred, paul).
parent(dave, fred).
```

Rule:

```prolog
grandparent(G, S) :- parent(G, P), parent(P, S).
```

Read: `G` is a grandparent of `S` if `G` is a parent of some `P` and `P` is a parent of `S`.

Query:

```prolog
?- grandparent(dave, jack).
true.
```

`dave` is a parent of `fred`, and `fred` is a parent of `jack`, so `dave` is a grandparent of `jack`.

### 29.06.2 Sibling rule and inequality

```prolog
sibling(A, B) :-
    parent(P, A),
    parent(P, B).
```

This is true when `A` and `B` share a parent. But it also makes `A` a sibling of itself. Add inequality:

```prolog
sibling(A, B) :-
    parent(P, A),
    parent(P, B),
    A \= B.
```

`\=` means "does not unify with" (not equal). Older coursebook code writes `not(A = B)`; both express the same idea.

### 29.06.3 Rule with an anonymous variable

```prolog
containsMeat(X) :-
    ingredient(X, Meat, _),
    meat(Meat).
```

Query:

```prolog
?- containsMeat(X).
X = stew.
```

Only `stew` contains an ingredient that appears in the `meat/1` facts.

### 29.06.4 Worked example — capital of a country

```prolog
capital(vienna).
capital(london).
cityIn(vienna, austria).
cityIn(london, uk).
continent(austria, europe).
continent(uk, europe).

capitalOf(City, Country) :-
    capital(City),
    cityIn(City, Country).

europeanCity(City) :-
    cityIn(City, Country),
    continent(Country, europe).
```

Queries:

```prolog
?- capitalOf(City, Country).
City = vienna, Country = austria ;
City = london, Country = uk.

?- europeanCity(City).
City = vienna ;
City = london.
```

> **Exam tip:** a rule is a **predicate defined by other predicates**. If the question says "write a rule", it expects a head, `:-`, and a body with commas, ending in a full stop.

---

## 29.07 Instantiation and Backtracking

Prolog solves a query by **matching** (unifying) the query with clause heads and then trying to satisfy the body. If a goal fails, Prolog **backtracks** to the most recent choice point and tries another clause or another instantiation.

### 29.07.1 How Prolog searches

1. Take the first goal in the query.
2. Find the first clause whose head matches.
3. Instantiate variables as required.
4. Move to the next goal in the body.
5. If all goals succeed, report the instantiation.
6. If a goal fails, backtrack to the most recent choice point and try the next alternative.
7. If no alternatives remain, report `false`.

### 29.07.2 Trace terminology

| Term | Meaning |
|---|---|
| **Call** | Entering a predicate to try to satisfy it |
| **Exit** | The predicate succeeds and returns |
| **Redo** | Backtracking into the predicate for another answer |
| **Fail** | No more solutions can be found |

**Worked example 29.07 — trace `containsMeat(X)`**

Knowledge base includes:

```prolog
ingredient(tagine, aubergine, 250).
ingredient(tagine, tomato, 100).
ingredient(stew, beef, 400).
ingredient(stew, potato, 600).
meat(chicken).
meat(beef).
meat(lamb).
```

Trace:

1. **Call** `containsMeat(X)`.
2. **Call** `ingredient(X, Meat, _)`.
   - First solution: `X = tagine`, `Meat = aubergine`.
3. **Call** `meat(aubergine)` → **Fail** (no such fact).
4. **Redo** `ingredient`: second solution `X = tagine`, `Meat = tomato`.
5. **Call** `meat(tomato)` → **Fail**.
6. **Redo** `ingredient`: third solution `X = stew`, `Meat = beef`.
7. **Call** `meat(beef)` → **Exit** (true).
8. **Exit** `containsMeat(X)` with `X = stew`.

Typing `;` causes **Redo** at step 8; Prolog continues searching. It finds `stew, potato` (fails `meat`), then no more ingredient clauses, and eventually **Fail** with `false`.

> **Exam tip:** trace questions award marks for the **order of clause attempts**, not just the final answer. Write the instantiation at each step and say whether the goal succeeds or fails.

### 29.07.3 The cut operator

`!` is the **cut**. It commits Prolog to the choices made so far, preventing backtracking past that point.

```prolog
max(X, Y, X) :- X >= Y, !.
max(X, Y, Y).
```

Once the first clause succeeds, the cut stops Prolog from trying the second clause. Use cuts carefully: they make programs faster but can remove valid solutions if placed incorrectly.

---

## 29.08 Recursion

A recursive rule uses itself as a sub-goal. The same three rules apply as in imperative recursion:

1. A **base case**.
2. A **general case**.
3. The general case must **reach the base case** in a finite number of steps.

### 29.08.1 Ancestor rule

```prolog
ancestor(A, B) :- parent(A, B).                    /* base case */
ancestor(A, B) :- parent(A, X), ancestor(X, B).    /* general case */
```

Read: `A` is an ancestor of `B` if `A` is a parent of `B`; or if `A` is a parent of some `X` and `X` is an ancestor of `B`.

Query:

```prolog
?- ancestor(dave, jack).
true.
```

`dave` is a parent of `fred`; `fred` is a parent of `jack`; the base case applies at the last step.

### 29.08.2 Factorial in Prolog

```prolog
factorial(0, 1).                                  /* base case: 0! = 1 */
factorial(N, Result) :-
    N > 0,
    M is N - 1,
    factorial(M, PartResult),
    Result is PartResult * N.
```

Query:

```prolog
?- factorial(5, Answer).
Answer = 120.
```

**Notes:**

- `is` evaluates an arithmetic expression; `=` would only unify terms.
- `N > 0` prevents infinite recursion for negative `N`.
- The recursive call computes `(N−1)!`, then multiplies by `N`.

### 29.08.3 Worked example — trace `factorial(3, R)`

1. `factorial(3, R)` → `M = 2`, call `factorial(2, P1)`.
2. `factorial(2, P1)` → `M = 1`, call `factorial(1, P2)`.
3. `factorial(1, P2)` → `M = 0`, call `factorial(0, P3)`.
4. `factorial(0, 1)` succeeds with `P3 = 1`.
5. `P2 is 1 * 1 = 1`.
6. `P1 is 1 * 2 = 2`.
7. `R is 2 * 3 = 6`.

`R = 6`.

> **Exam tip:** `is` is essential for arithmetic. `Result = PartResult * N` would try to unify `Result` with the compound term `*(PartResult, N)`, not compute a number.

---

## 29.09 Lists

A **list** is an ordered collection of terms, written in square brackets:

```prolog
[1, 2, 3]
[red, green, blue]
[]
```

Lists may mix types: `[1, apple, 3.14]`.

### 29.09.1 Head and tail

Every non-empty list has:

- a **head** — the first element,
- a **tail** — the list of remaining elements (always a list).

The separator is the vertical bar `|`:

```prolog
[H|T]
```

Matching `[H|T]` with `[car, lorry, boat, ship]` gives:

- `H = car`
- `T = [lorry, boat, ship]`

**Worked example 29.08 — head and tail**

```prolog
showHeadAndTail([H|T], H, T).
```

Query:

```prolog
?- showHeadAndTail([fred, jack, emma], Head, Tail).
Head = fred,
Tail = [jack, emma].
```

The empty list `[]` has no head or tail; a clause that matches `[H|T]` will fail on `[]`.

### 29.09.2 `append`

`append(A, B, C)` is true when `C` is the concatenation of `A` and `B`.

```prolog
?- append([a, b], [c, d], MyList).
MyList = [a, b, c, d].

?- append(FirstList, [c, d], [a, b, c, d]).
FirstList = [a, b].
```

Prolog can run `append` "backwards" because it searches for a unification rather than executing a fixed procedure. This is a key feature of declarative programming.

### 29.09.3 `member`

`member(A, B)` is true when `A` is an element of list `B`.

```prolog
?- member(c, [a, b, c, d, e]).
true.

?- member(X, [a, b, c, d]).
X = a ;
X = b ;
X = c ;
X = d.
```

Each `;` asks for the next element; the final `;` returns `false`.

### 29.09.4 Writing and reading

| Predicate | Effect |
|---|---|
| `write(A)` | Outputs `A` |
| `nl` | Outputs a new line |
| `read(A)` | Reads a term from the keyboard into `A` |
| `assert(C)` | Adds clause `C` to the knowledge base |
| `retractall(C)` | Removes all matching clauses |

**Worked example 29.09 — output a list**

```prolog
writeList([]).
writeList([H|T]) :-
    write(H), nl,
    writeList(T).
```

Query:

```prolog
?- writeList([a, b, c]).
a
b
c
true.
```

Base case: the empty list prints nothing. General case: print the head, then recursively print the tail.

### 29.09.5 Worked example — recursive list length

```prolog
length([], 0).
length([_|T], N) :-
    length(T, N1),
    N is N1 + 1.
```

Query:

```prolog
?- length([a, b, c], N).
N = 3.
```

The anonymous variable `_` is used because the head value is irrelevant to the length.

### 29.09.6 Worked example — sum of a list

```prolog
sum([], 0).
sum([H|T], Total) :-
    sum(T, SubTotal),
    Total is H + SubTotal.
```

Query:

```prolog
?- sum([1, 2, 3, 4], Total).
Total = 10.
```

---

## 29.10 Declarative vs Imperative — Summary

| Aspect | Imperative | Declarative |
|---|---|---|
| Program is | Sequence of instructions | Facts, rules and queries |
| Focus | How to compute | What is true/required |
| Control flow | Explicit loops/branches | Implicit search/backtracking |
| Variables | Mutable storage | Instantiated by unification |
| Arithmetic | Assignment statements | `is` evaluation |
| Reuse | Procedures/functions | Rules/predicates |
| Debugging | Step through statements | Trace calls, exits, redos, fails |
| Typical languages | Python, C, Pascal | Prolog, SQL |

**Why declarative can be concise:** the inference engine handles the search. The programmer states the relationships, and Prolog explores the alternatives. The trade-off is less control over execution order and performance.

---

## 📝 Exam-style Questions with Full Solutions

### Question 1 — Cities knowledge base (7 marks)

```prolog
capital(vienna).
capital(london).
capital(santiago).
capital(caracas).
capital(tokyo).
cityIn(vienna, austria).
cityIn(santiago, chile).
cityIn(salzburg, austria).
cityIn(maracaibo, venezuela).
continent(austria, europe).
continent(chile, southAmerica).
continent(uk, europe).
continent(argentina, southAmerica).
iVisited(vienna).
iVisited(tokyo).
capitalOf(City, Country) :- capital(City), cityIn(City, Country).
europeanCity(City) :- cityIn(City, Country), continent(Country, europe).
```

(a) Write the extra facts: (i) London is in the UK; (ii) I visited Strasbourg. [2]
(b) State the result of `continent(Country, southAmerica).` [2]
(c) Complete `countriesIVisited(Country)` to list countries I have visited. [3]

**Solution:**

(a)

```prolog
cityIn(london, uk).
iVisited(strasbourg).
```

(b)

```prolog
Country = chile ;
Country = argentina.
```

(c)

```prolog
countriesIVisited(Country) :-
    iVisited(City),
    cityIn(City, Country).
```

`iVisited(City)` finds each visited city; `cityIn(City, Country)` finds its country. For `vienna`, this gives `austria`; for `tokyo`, no `cityIn` fact exists, so that branch fails.

**What the examiner wants:** lower-case atoms, full stops, and a body with the two goals in a sensible order.

### Question 2 — Driving knowledge base (14 marks)

```prolog
minimumAge(car, 18).
minimumAge(truck, 21).
age(fred, 19).
age(jack, 22).
age(mike, 17).
age(jhon, 20).
age(emma, 22).
age(sheena, 19).
hasLicence(fred).
hasLicence(jack).
hasLicence(mike).
hasLicence(jhon).
hasLicence(emma).
hasLicence(sheena).
allowedToDrive(X, V) :-
    hasLicence(X),
    minimumAge(V, L),
    age(X, A),
    A >= L.
passedTheoryTest(jack).
passedTheoryTest(emma).
passedTheoryTest(jhon).
passedTheoryTest(fred).
passedDrivingTest(jhon, car).
passedDrivingTest(fred, car).
passedDrivingTest(jack, car).
passedDrivingTest(jack, truck).
passedDrivingTest(sheena, car).
qualifiedDriver(X, V) :-
    allowedToDrive(X, V),
    passedTheoryTest(X),
    passedDrivingTest(X, V).
```

(a) Give one fact and one rule. [2]
(b) State the output of: (i) `passedDrivingTest(Who, truck).` (ii) `allowedToDrive(mike, car).` (iii) `\+ hasLicence(sheena).` [3]
(c) Write clauses to output: (i) all qualified car drivers; (ii) all drivers who passed the theory test but not a driving test. [5]
(d) Trace `allowedToDrive(mike, car).` and identify the clauses used. [5]

**Solution:**

(a) Fact: `age(fred, 19).` Rule: `allowedToDrive(X, V) :- ...` (or `qualifiedDriver`).

(b)

(i) `Who = jack.` (only Jack passed the truck driving test.)
(ii) `false` — Mike is 17, but the minimum age for a car is 18, so `A >= L` fails.
(iii) `false` — Sheena does have a licence, so `\+ hasLicence(sheena)` fails. (In the coursebook's older notation, `NOT(hasLicence(sheena))` is also false.)

(c)

(i)

```prolog
qualifiedCarDriver(X) :-
    qualifiedDriver(X, car).
```

Query `?- qualifiedCarDriver(X).` gives `X = fred ; X = jack ; X = jhon.` Emma fails because she has no car driving test, Mike fails because he is under 18, and Sheena fails because she has no theory test.

(ii)

```prolog
theoryOnly(X) :-
    passedTheoryTest(X),
    \+ passedDrivingTest(X, _).
```

This finds people who passed the theory test but have no driving-test fact for any vehicle.

(d) Trace `allowedToDrive(mike, car)`:

1. **Call** `allowedToDrive(mike, car)`.
2. **Call** `hasLicence(mike)` → **Exit** (fact 11).
3. **Call** `minimumAge(car, L)` → **Exit** with `L = 18` (fact 01).
4. **Call** `age(mike, A)` → **Exit** with `A = 17` (fact 05).
5. Evaluate `A >= L` → `17 >= 18` → **Fail**.
6. Backtrack: no more `age(mike, ...)` facts, no more `minimumAge(car, ...)` facts, no more `hasLicence(mike)` facts.
7. **Fail** — the query returns `false`.

**What the examiner wants:** the order of goals, the instantiation at each step, and the failure at the age comparison.

### Question 3 — Family rules (6 marks)

Given `parent/2` facts, write rules for:

(a) `grandparent(G, S)`
(b) `sibling(A, B)` that excludes a person being their own sibling
(c) `ancestor(A, B)` recursively

**Solution:**

```prolog
grandparent(G, S) :-
    parent(G, P),
    parent(P, S).

sibling(A, B) :-
    parent(P, A),
    parent(P, B),
    A \= B.

ancestor(A, B) :- parent(A, B).
ancestor(A, B) :- parent(A, X), ancestor(X, B).
```

**What the examiner wants:** shared variable `P` for sibling, inequality, and both base and general cases for ancestor.

### Question 4 — Recursion (6 marks)

Write a Prolog rule `factorial(N, Result)` and explain why `is` is used instead of `=`.

**Solution:**

```prolog
factorial(0, 1).
factorial(N, Result) :-
    N > 0,
    M is N - 1,
    factorial(M, PartResult),
    Result is PartResult * N.
```

`is` **evaluates** the arithmetic expression on its right and unifies the result with the left. `=` only unifies terms; `Result = PartResult * N` would create the compound term `*(PartResult, N)` rather than computing a product. `N > 0` prevents infinite recursion for negative values.

### Question 5 — Lists (8 marks)

(a) Write a rule `firstAndRest(List, Head, Tail)` that returns the head and tail of a list. [3]
(b) Write a recursive rule `sumList(List, Total)` that sums a list of numbers. [5]

**Solution:**

(a)

```prolog
firstAndRest([H|T], H, T).
```

Query:

```prolog
?- firstAndRest([a, b, c], H, T).
H = a,
T = [b, c].
```

(b)

```prolog
sumList([], 0).
sumList([H|T], Total) :-
    sumList(T, SubTotal),
    Total is H + SubTotal.
```

Base case: the empty list sums to 0. General case: sum the tail, then add the head.

### Question 6 — Backtracking (5 marks)

Explain what is meant by backtracking, using the query `member(X, [a, b, c])` as an example.

**Solution:**

Backtracking is Prolog's method of undoing a choice and trying the next alternative when a goal fails or when the user asks for another solution (with `;`). For `member(X, [a, b, c])`, Prolog first unifies `X` with `a` and succeeds. When `;` is typed, it **redoes** the `member` goal, undoes `X = a`, and tries the next element, giving `X = b`; another `;` gives `X = c`; a final `;` fails because there are no more elements. Backtracking explores the alternatives in the order the clauses/elements are defined.

**What the examiner wants:** "undo the previous instantiation and try the next alternative", plus the `;` trigger and the order of solutions.

---

# 📋 Formula / Fact Sheet (Chapter 29)

**Three constructs:** facts, rules, queries.

**Clause:** `Head :- Body.` — `:-` means "if"; `,` means "and"; `;` means "or"; full stop ends the clause.

**Term types:** atom (lower-case), number, variable (capital/`_`), compound term.

**Arity:** number of arguments; `predicate/2` has arity 2.

**Fact:** clause with no body, e.g. `parent(fred, jack).`

**Rule:** head true if body true, e.g. `grandparent(G,S) :- parent(G,P), parent(P,S).`

**Variable:** capital letter; instantiated by unification; `_` is anonymous and matches anything.

**Backtracking:** on failure (or `;`), undo the most recent instantiation and try the next alternative.

**Trace terms:** Call, Exit, Redo, Fail.

**Recursion:** base case + general case; must reach the base case. Example: `ancestor(A,B) :- parent(A,B).` / `ancestor(A,B) :- parent(A,X), ancestor(X,B).`

**Arithmetic:** use `is` to evaluate, e.g. `Result is PartResult * N`; `=` only unifies.

**Lists:** `[a,b,c]`; empty `[]`; head/tail `[H|T]`; `append(A,B,C)`; `member(X,List)`; `write/1`, `read/1`, `nl`.

**Comparison:** imperative = how; declarative = what; Prolog searches, unifies and backtracks.

# ⚡ Quick Reference Card

1. **Prolog = facts + rules + queries.** End everything with a full stop.
2. **Atoms start lower-case; variables start upper-case.** Case matters.
3. **`:-` means IF; `,` means AND; `;` means OR.**
4. **`_` is the anonymous variable** — matches anything, value not used.
5. **`=` is unification, not assignment.**
6. **`is` evaluates arithmetic** — always use it for calculations.
7. **Backtracking** undoes a choice and tries the next clause/solution.
8. **Semicolon `;`** asks for the next solution after a successful query.
9. **Recursive rule needs a base case and a general case.**
10. **Lists use `[H|T]`**; the tail is always a list.
11. **`append/3`, `member/2`, `write/1`, `read/1`, `nl`** are built-in list/I/O predicates.
12. **`\=` (or `not(A=B)`)** tests inequality; without it, siblings include themselves.
