# 📘 Chapter 22: Artificial Intelligence (AI) - Cambridge International AS & A Level Computer Science (9618)

## Cambridge International AS & A Level Computer Science - Part 3

> **Rule + fully solved examples.** Everything the examiner can ask from Chapter 22: what AI is, how graphs and shortest-path algorithms (Dijkstra and A*) support AI, supervised/unsupervised/reinforcement learning, regression, artificial neural networks, back propagation and deep learning. Every section ends with worked examples and exam-style questions with full mark-earning solutions.

**Learning objectives (Chapter 22):**
- Show understanding of how graphs can be used to aid Artificial Intelligence
- Show understanding of how artificial neural networks have helped with machine learning
- Show understanding of Deep Learning, Machine Learning and Reinforcement Learning, and why they are used
- Show understanding of back propagation of errors and regression methods in machine learning

---

## 22.01 An Overview

There is no single agreed definition of **Artificial Intelligence (AI)** because "intelligence" itself is hard to define. A calculator can do arithmetic faster than a person, but it is not called intelligent. A workable definition is:

> **Artificial Intelligence** is the branch of computer science concerned with making computers do things at which, at the moment, people are better.

AI is therefore a broad umbrella covering many sub-fields: graph search and path-finding, machine learning, neural networks, natural language processing, robotics, expert systems and more. This chapter concentrates on two foundations:

1. **Graph-based search** — finding a best route through a network of possibilities.
2. **Learning from data** — machine learning and artificial neural networks.

> **Exam tip:** do not try to write a precise "AI is..." definition in an exam. A mark-scheme answer accepts the idea of automating tasks that normally require human intelligence, or performing tasks at which humans are currently better.

---

## 22.02 How Graphs Can Be Used in AI

### 22.02.1 Graphs as a model

A **graph** is a collection of **nodes (vertices)** joined by **edges**. Each node has a name; each edge may have a numerical **label** (weight).

| Graph element | Meaning in a route problem | Meaning in a general AI problem |
|---|---|---|
| Node | A place | A state or configuration |
| Edge | A direct road between two places | A legal move/transition between states |
| Edge label | Distance, time or cost | Cost of the move |

A graph can represent roads between towns, flights between airports, links between web pages, moves in a puzzle, or possible states in a game. The edge labels might represent distance, travel time, fuel cost, or any other quantity to be minimised.

**Worked example 22.01 — brute-force shortest route**

A graph has edges `A–B = 40`, `B–C = 10`, `C–D = 40`, `B–F = 15`, `F–E = 20`, `E–D = 5`, `A–F = 60`.

Possible routes from A to D:

| Route | Total |
|---|---|
| A → B → C → D | `40 + 10 + 40 = 90` |
| A → B → F → E → D | `40 + 15 + 20 + 5 = 80` |
| A → F → E → D | `60 + 20 + 5 = 85` |
| A → F → B → C → D | `60 + 15 + 10 + 40 = 125` |

The shortest route is **A → B → F → E → D**, with total 80.

Listing every route works for a small graph, but the number of routes grows very quickly with the number of nodes. For a graph with 100 nodes, brute force is impractical. AI uses **search algorithms** instead.

### 22.02.2 Dijkstra's algorithm

**Purpose:** find the shortest path from one source node to every other node in a graph with non-negative edge weights.

**Data structures:**

- `ShortestPath` — nodes whose shortest distance is finalised.
- `RemainingNodes` — all nodes not yet finalised.
- A record for each node storing:
  - the node name,
  - the best known distance from the source,
  - the route (sequence of nodes) that produced that distance.

**Algorithm:**

1. Set the source distance to `0`; set every other distance to `∞` (a value larger than any possible route).
2. Put all nodes in `RemainingNodes`.
3. Repeat until `RemainingNodes` is empty:
   - Pick the node `N` in `RemainingNodes` with the **smallest distance**.
   - Move `N` to `ShortestPath` (its distance is now final).
   - For each neighbour of `N` still in `RemainingNodes`:
     - Calculate `new distance = distance[N] + edge weight(N, neighbour)`.
     - If this is smaller than the neighbour's stored distance, replace it and record the new route.
4. When the target node is finalised, its stored distance and route are the shortest.

**Why it works:** edge weights are non-negative, so once the smallest remaining distance is chosen, no later route can produce a smaller value for that node.

**Worked example 22.02 — trace Dijkstra from A**

Using the graph in Worked example 22.01:

| Step | ShortestPath set | A | B | C | D | E | F |
|---|---|---|---|---|---|---|---|
| 0 | `{}` | 0 | ∞ | ∞ | ∞ | ∞ | ∞ |
| 1 | `{A}` | **0** | 40 | ∞ | ∞ | ∞ | 60 |
| 2 | `{A,B}` | **0** | **40** | 50 | ∞ | ∞ | 55 |
| 3 | `{A,B,C}` | **0** | **40** | **50** | 90 | ∞ | 55 |
| 4 | `{A,B,C,F}` | **0** | **40** | **50** | 90 | 75 | **55** |
| 5 | `{A,B,C,F,E}` | **0** | **40** | **50** | 80 | **75** | **55** |
| 6 | `{A,B,C,D,E,F}` | **0** | **40** | **50** | **80** | **75** | **55** |

At step 2, reaching C through B costs `40 + 10 = 50`, which is better than any other known route. At step 4, reaching E through F costs `55 + 20 = 75`. At step 5, reaching D through E costs `75 + 5 = 80`, improving on the earlier 90 via C. Final shortest route to D: **A → B → F → E → D**, total **80**.

> **Exam tip:** in a trace table, show the distance **and** the route for every update, and mark finalised nodes. The mark scheme often awards one mark per correct row/update, not just the final answer.

### 22.02.3 The A* algorithm

Dijkstra explores in all directions, including away from the target. **A\*** improves this by adding a **heuristic** estimate of the remaining distance.

For each candidate node `n`:

`f(n) = g(n) + h(n)`

- `g(n)` = actual cost from the start to `n` (the Dijkstra part).
- `h(n)` = estimated cost from `n` to the target (the heuristic).
- `f(n)` = estimated total cost of the route through `n`.

A\* always expands the node with the **lowest `f(n)`** next, so it is pulled towards the target.

**Heuristic function:** a rule that estimates the remaining cost. For a map with `x, y` coordinates, the straight-line distance is a natural heuristic:

`h = √((x₂ − x₁)² + (y₂ − y₁)²)`

For the heuristic to guarantee an optimal route it must be **admissible**: it must **never overestimate** the true remaining cost. Straight-line distance is admissible because a straight line is never longer than any road route.

**A\* outline:**

1. Put the start node in the **open list**.
2. Remove the node with the lowest `f` from the open list; call it the current node.
3. If it is the target, reconstruct the path and stop.
4. Otherwise, for each neighbour:
   - calculate tentative `g = g(current) + edge cost`;
   - if this improves the neighbour's stored `g`, update `g`, compute `f = g + h`, record the parent, and add it to the open list (if not already there).
5. Move the current node to the **closed list**.
6. Repeat until the open list is empty (no route) or the target is reached.

**Worked example 22.03 — A\* from A to D**

Towns have coordinates: `A(40,20)`, `B(30,30)`, `C(80,35)`, `D(130,30)`, `E(120,20)`, `F(45,5)`, `G(100,30)`.

Roads: `A–B = 13`, `A–C = 45`, `A–F = 20`, `B–C = 50`, `B–G = 45`, `C–G = 25`, `C–D = 40`, `F–G = 100`, `G–D = 10`, `G–E = 15`, `D–E = 15` (some routes are indirect).

Start A, target D. Calculate `h` as straight-line distance:

- `h(B) ≈ 10`, `h(C) ≈ 43`, `h(F) ≈ 15`, `h(G) ≈ 61`, `h(E) ≈ 81`, `h(D) = 0`.

Step 1 — from A:

| Node | g | h | f = g + h |
|---|---|---|---|
| B | 13 | 10 | 23 |
| C | 45 | 43 | 88 |
| F | 20 | 15 | 35 |

Expand **B** (lowest f = 23).

Step 2 — from B: `C` via B costs `13 + 50 = 63` (worse than 45, ignore); `G` costs `13 + 45 = 58`, `h(G) ≈ 61`, so `f ≈ 119`.

Expand **F** (f = 35).

Step 3 — from F: `G` via F costs `20 + 100 = 120` (worse than 58, ignore).

Expand **C** (f = 88).

Step 4 — from C: `G` via C costs `45 + 25 = 70` (worse than 58, ignore); `D` via C costs `45 + 40 = 85`, `h(D)=0`, so `f = 85`.

Open list now contains G (f ≈ 119) and D (f = 85). Expand **D** — target reached. Route: **A → C → D**, total **85**.

The heuristic made A\* avoid exploring E and large parts of the graph; Dijkstra would have expanded more nodes.

> **Exam tip:** if the heuristic overestimates, A\* may return a non-optimal route. State "the heuristic must be admissible / must not overestimate" when explaining optimality.

### 22.02.4 Dijkstra vs A\*

| Feature | Dijkstra | A\* |
|---|---|---|
| Uses a heuristic? | No | Yes |
| Direction of search | All directions equally | Biased towards target |
| Optimal route? | Yes (non-negative weights) | Yes, if heuristic is admissible |
| Typical speed | Slower on large graphs | Faster when a good heuristic exists |
| Best use | Shortest paths to **all** nodes | Shortest path to **one** target |

---

## 22.03 Machine Learning

**Definition:** machine learning is where a system **improves its performance through analysis of previous performance**. It requires:

- a defined task or tasks,
- experience gained by performing the task,
- improvement in future performance as a result of that experience.

Learning from experience is one indication of intelligence, which is why machine learning sits under AI.

### 22.03.1 Supervised learning

In **supervised learning**, the system is given **labelled training data**: each input comes with the correct output (the "label").

- The system learns a mapping from inputs to outputs.
- A human provides the classification or target value.
- Examples: spam detection (email labelled spam/not spam), exam-script marking (answer labelled with a grade), image classification (photo labelled "cat"), regression (input marks paired with actual outcomes).

**Worked example 22.04 — marking exam answers**

A system is trained on hundreds of past answers, each paired with a grade. It learns which features (use of key terms, structure, length, accuracy) correlate with each grade. A new answer is then given a predicted grade. A human examiner can check samples to measure accuracy and add more labelled data where the system is weak.

### 22.03.2 Unsupervised learning

In **unsupervised learning**, the system is given **unlabelled data** and must find its own structure.

- No correct answers are supplied.
- The system groups, clusters or categorises data by similarity.
- Examples: customer segmentation, recommending products from browsing behaviour, grouping news articles by topic, anomaly detection.

The coursebook describes **conceptual clusters**: knowledge is placed in a tree, and groups are moved into branches according to their attributes. There is no theoretical framework supplied from outside — the structure is inferred from the data itself.

**Worked example 22.05 — recommendation**

A streaming service records which films each user watches. No one labels the users. The system clusters users with similar viewing patterns and recommends films popular within a user's cluster. The quality is judged by whether recommendations are actually watched, not by a pre-labelled "correct answer".

### 22.03.3 Reinforcement learning

In **reinforcement learning**, an **agent** learns by interacting with an **environment** and receiving **rewards**.

| Term | Meaning |
|---|---|
| **Agent** | The learner/decision-maker |
| **Environment** | The world the agent acts in |
| **State** | The current situation |
| **Action** | A move the agent can take |
| **Policy** | The agent's strategy for choosing actions |
| **Reward** | A numerical score for an action's effectiveness |
| **Episode** | One run through the problem |

The agent tries actions, receives rewards, and updates its policy to maximise the total reward. It must balance:

- **Exploitation** — using actions known to give good rewards.
- **Exploration** — trying new actions that might give even better rewards.

Examples: learning to play backgammon or Go, robot locomotion, maze navigation, game-playing agents.

**Worked example 22.06 — maze**

A robot in a maze receives `+10` for reaching the exit, `−1` for hitting a wall, and `0` otherwise. Initially it moves randomly. Over many episodes, it learns that the sequence of turns leading to the exit produces the highest total reward, and its policy shifts towards that sequence.

### 22.03.4 Expert systems are not machine learning

An **expert system** is a narrowly focused AI system built from a **knowledge base** (facts and rules) supplied by human experts, plus an **inference engine** that applies the rules to new data.

- Human experts provide the conclusions for sample data.
- These are entered into the knowledge base.
- The system is tested against human experts and refined.

It is AI, but **not machine learning**, because there is no expectation that it improves its performance **unaided**. Any improvement comes from humans adding more knowledge.

### 22.03.5 Regression analysis

**Regression analysis** finds a mathematical function that best fits observed data, so that outputs can be predicted from new inputs.

- **Simple linear regression:** one input, one output, straight-line fit `y = mx + c`.
- **Multiple regression:** several inputs.
- **Non-linear regression:** a curve (e.g. exponential growth) fits better than a line.

**Worked example 22.07 — predicting exam marks**

Historic data pairs IGCSE Mathematics marks with A Level Computer Science marks. Plotting them shows a strong positive correlation. A best-fit line is calculated (e.g. `predicted CS = 0.8 × maths + 10`). For a new candidate with maths = 70, the predicted CS mark is `0.8 × 70 + 10 = 66`. The prediction is only valid within the range of the original data and assumes the relationship continues.

> **Exam tip:** regression predicts a **numerical value**; classification predicts a **category**. Supervised learning can do either, depending on the label type.

### 22.03.6 Comparison of learning types

| Type | Training data | Feedback | Goal | Example |
|---|---|---|---|---|
| Supervised | Labelled | Correct answer supplied | Predict label/value | Spam filter |
| Unsupervised | Unlabelled | None | Find structure/clusters | Customer segmentation |
| Reinforcement | No fixed dataset; experience | Reward signal | Maximise reward | Game-playing agent |

---

## 22.04 Artificial Neural Networks

### 22.04.1 Inspiration from biology

A biological neuron receives signals through **dendrites**, combines them in the cell body, and if the voltage exceeds a threshold, fires a signal along the **axon** to **synapses** connecting to other neurons. Learning changes the strength of those connections.

An **artificial neural network (ANN)** models this in software or hardware using **nodes** (artificial neurons) connected by weighted links.

### 22.04.2 Structure of an ANN

| Layer | Role |
|---|---|
| **Input layer** | Receives the data; one node per input feature |
| **Hidden layer(s)** | Perform intermediate transformations; may be many |
| **Output layer** | Produces the final prediction/classification |

Each node:

1. Receives one or more inputs `x₁, x₂, ..., xₙ`.
2. Multiplies each by a **weight** `wᵢ`.
3. Sums the weighted inputs: `z = Σ wᵢxᵢ + b` (where `b` is a bias).
4. Applies an **activation function** to produce the output.
5. Passes the output to the next layer.

Common activation functions include step (threshold), sigmoid, ReLU and tanh. A non-linear activation is what allows a network to learn non-linear relationships.

**Worked example 22.08 — one node**

Inputs `x₁ = 2`, `x₂ = 3`; weights `w₁ = 0.5`, `w₂ = −1`; bias `b = 1`.

`z = (0.5 × 2) + (−1 × 3) + 1 = 1 − 3 + 1 = −1`

With a threshold activation "output 1 if `z ≥ 0`, otherwise 0", the output is **0**.

### 22.04.3 Learning: back propagation of errors

**Back propagation** is the algorithm that adjusts the weights and biases to reduce error.

1. **Forward pass:** feed training data through the network and compute the output.
2. **Calculate error:** compare each output with the known correct value, e.g. `error = target − output`.
3. **Backward pass:** propagate the error backwards from the output layer through the hidden layers to the input layer.
4. **Update weights:** adjust each weight in the direction that reduces the error. The size of the adjustment is controlled by the **learning rate**.
5. **Repeat** over many examples and epochs until the error is acceptably small.

The output-layer weights are adjusted first because their effect on the error is most direct; then hidden-layer weights; finally input-layer weights. If more real data becomes available, training can continue to improve performance.

> **KEY TERM**
> **Back propagation of errors:** an algorithm for machine learning that optimises adjustable parameters. It is applied first to the output layer, then works backward through hidden layers until the input layer is reached.

### 22.04.4 Deep learning

**Deep learning** uses an artificial neural network with an **exceptionally large number of hidden layers**. Lower layers learn simple features (edges, colours); higher layers combine them into abstract concepts (faces, objects, words).

Deep learning requires:

- very large labelled datasets,
- substantial computing power (often GPUs),
- careful tuning to avoid **overfitting** (memorising training data instead of generalising).

Examples: image recognition, speech recognition, machine translation, self-driving perception, large language models.

### 22.04.5 Worked example — battery cost-effectiveness

An ANN estimates battery cost per unit time from purchase price and lifetime.

- Input nodes receive battery data (price, capacity, device type).
- Hidden nodes combine features (e.g. one node relates to device type, another to user type).
- Output nodes estimate cost per unit time for each battery.
- Weights and activation functions start at trial values.
- Real-use lifetime data provides targets.
- Back propagation adjusts output-layer weights first, then hidden, then input.
- The trained network predicts for new batteries; when more real data arrives, training continues.

### 22.04.6 Advantages and limitations of ANNs

**Advantages:**

- Can learn complex, non-linear patterns that are hard to program explicitly.
- Improve with more data.
- Good for perception tasks (images, speech, text).

**Limitations:**

- Need large amounts of labelled data.
- Computationally expensive to train.
- **Black box:** the learned weights are hard to interpret, so decisions can be difficult to explain.
- Can overfit or inherit bias from training data.
- Performance is only as good as the training data.

> **Exam tip:** if asked why an ANN is suitable, mention learning from examples and handling complex/non-linear patterns. If asked for a drawback, mention the need for large training data or the difficulty of explaining decisions.

---

## 📝 Exam-style Questions with Full Solutions

### Question 1 — Dijkstra trace (8 marks)

The graph has edges `A–B = 10`, `A–C = 30`, `B–C = 5`, `B–D = 20`, `C–D = 10`, `D–E = 5`.

(a) Trace Dijkstra's algorithm from A. [6]
(b) State the shortest route and distance from A to E. [2]

**Solution:**

(a)

| Step | Finalised | A | B | C | D | E |
|---|---|---|---|---|---|---|
| 0 | `{}` | 0 | ∞ | ∞ | ∞ | ∞ |
| 1 | `{A}` | **0** | 10 | 30 | ∞ | ∞ |
| 2 | `{A,B}` | **0** | **10** | 15 | 30 | ∞ |
| 3 | `{A,B,C}` | **0** | **10** | **15** | 25 | ∞ |
| 4 | `{A,B,C,D}` | **0** | **10** | **15** | **25** | 30 |
| 5 | `{A,B,C,D,E}` | **0** | **10** | **15** | **25** | **30** |

(b) Shortest route: **A → B → C → D → E**, distance **30**.

**What the examiner wants:** correct relaxation at each step (B via A = 10; C via B = 15, improving on 30; D via C = 25, improving on 30; E = 30) and the final route.

### Question 2 — A\* and heuristics (6 marks)

(a) State the formula used by A\* to choose the next node. [2]
(b) Explain what is meant by an admissible heuristic. [2]
(c) Give one advantage of A\* over Dijkstra. [2]

**Solution:**

(a) `f(n) = g(n) + h(n)`, where `g(n)` is the actual cost from the start and `h(n)` is the estimated cost from `n` to the target. The node with the lowest `f` is expanded next.

(b) A heuristic is admissible if it **never overestimates** the true remaining cost. Then A\* is guaranteed to find an optimal route.

(c) A\* uses the heuristic to head towards the target, so it usually expands fewer nodes and finds a route faster than Dijkstra, which searches in all directions.

### Question 3 — Learning types (9 marks)

For each scenario, state whether supervised, unsupervised or reinforcement learning is most appropriate, and justify your answer.

(a) Grouping customers into segments based on purchase history. [3]
(b) Training a robot to walk using rewards for forward movement. [3]
(c) Predicting a house price from labelled sales data. [3]

**Solution:**

(a) **Unsupervised** — no labels are provided; the system must discover groups/clusters from the data itself.

(b) **Reinforcement** — an agent acts in an environment and learns from rewards/penalties over many trials, balancing exploration and exploitation.

(c) **Supervised** — historical examples are labelled with the correct price, so the system learns a mapping from features to a numerical output (regression).

### Question 4 — Regression (5 marks)

Explain how regression analysis could be used to predict a student's A Level Computer Science mark from their IGCSE Mathematics mark.

**Solution:**

Collect historical pairs of marks. Plot them and look for correlation. Calculate the line (or curve) of best fit, e.g. `y = mx + c`. Use the equation to predict the CS mark for a new maths mark. The prediction is only reliable within the range of the original data; a weak correlation makes the prediction unreliable.

**What the examiner wants:** paired data, correlation, best-fit equation, substitution, and a limitation.

### Question 5 — Neural network and back propagation (8 marks)

(a) Describe the structure of a simple artificial neural network. [3]
(b) Explain how back propagation is used to train it. [5]

**Solution:**

(a) An input layer with one node per input feature, one or more hidden layers, and an output layer. Nodes in adjacent layers are connected by weighted links. Each node sums its weighted inputs (plus a bias) and applies an activation function.

(b) In the forward pass, training data is fed through the network to produce an output. The error is the difference between the output and the known target. The error is propagated backwards from the output layer through the hidden layers. Weights (and biases) are adjusted to reduce the error, with the size of each adjustment controlled by the learning rate. Output-layer weights are adjusted first, then hidden, then input. The process repeats over many examples/epochs until the error is acceptably small.

### Question 6 — Deep learning (4 marks)

Explain what is meant by deep learning and give one reason it has become practical in recent years.

**Solution:**

Deep learning uses an artificial neural network with a very large number of hidden layers, allowing lower layers to learn simple features and higher layers to learn abstract ones. It has become practical because of much greater computing power (especially GPUs) and the availability of very large datasets.

---

# 📋 Formula / Fact Sheet (Chapter 22)

**Graph:** nodes + edges; edge labels are weights (distance/cost/time).

**Dijkstra:** source distance 0, others ∞; repeatedly finalise the smallest tentative distance; relax neighbours; optimal for non-negative weights; gives shortest path to all nodes.

**A\*:** `f(n) = g(n) + h(n)`; expand lowest `f`; heuristic must be admissible (never overestimate); faster than Dijkstra with a good heuristic; optimal if admissible.

**Straight-line heuristic:** `h = √((x₂−x₁)² + (y₂−y₁)²)`.

**Machine learning:** system improves performance through analysis of previous performance.

**Supervised:** labelled data; learn input → output mapping.
**Unsupervised:** unlabelled data; find clusters/structure.
**Reinforcement:** agent + environment + state + action + policy + reward; maximise reward; exploration vs exploitation.

**Expert system:** knowledge base + inference engine; human-supplied rules; **not** machine learning because it does not improve unaided.

**Regression:** find a mathematical function of best fit; linear `y = mx + c`; multiple or non-linear possible; used to predict numerical values.

**ANN:** input layer → hidden layer(s) → output layer; each node computes `Σwᵢxᵢ + b`, then applies an activation function.

**Back propagation:** forward pass → compute error → propagate error backwards → adjust weights/biases → repeat; learning rate controls step size.

**Deep learning:** ANN with very many hidden layers; needs large data and compute; risk of overfitting.

# ⚡ Quick Reference Card

1. **Graph search** is AI because it finds a good solution without exhaustive brute force.
2. **Dijkstra** = shortest path to all nodes; no heuristic; works with non-negative weights.
3. **A\*** = Dijkstra + heuristic; `f = g + h`; heuristic must not overestimate.
4. **Supervised** = labelled; **unsupervised** = unlabelled; **reinforcement** = rewards.
5. **Expert system ≠ machine learning** — no unaided improvement.
6. **Regression predicts numbers; classification predicts categories.**
7. **ANN node:** weighted sum → activation → output.
8. **Back propagation** adjusts weights from output layer backwards.
9. **Deep learning** = many hidden layers; powerful but data- and compute-hungry.
10. **Always state a limitation:** overfitting, bias, black-box decisions, data requirements.
