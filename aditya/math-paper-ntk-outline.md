# Why Overparameterised Neural Networks Generalise: A Mathematical Exposition from First Principles

Section-by-section structure for the maths research paper (activity list entry: "Research paper: Why Overparameterised Neural Networks Generalise").

---

**Title:**
"Why Overparameterised Neural Networks Generalise: A Mathematical Exposition from First Principles"

---

**Section 1 - The Paradox (1 page)**

State the puzzle cleanly. Classical statistics says if your model has more parameters than data points it overfits catastrophically. Show this with bias-variance decomposition - derive the tradeoff mathematically using expectation and variance from A-level probability. Then state the empirical fact: neural networks with millions of parameters trained on thousands of examples generalise perfectly. This is the contradiction. Everything that follows is trying to explain it.

Maths used: expectation, variance, MSE decomposition. Pure A-level probability and statistics.

---

**Section 2 - Neural Networks as Linear Maps (2 pages)**

Start from scratch. Define a single neuron as a linear map plus activation function. Build a two-layer network explicitly. Write the forward pass as matrix multiplication - this is pure A-level matrices. Show that at initialisation with random weights the network is a specific kind of random matrix. Derive the output of the network as a function of its parameters explicitly for a two-layer ReLU network with one hidden unit, two hidden units, then n hidden units. Show the pattern.

Maths used: matrix multiplication, linear transformations, function composition. All A-level and FM.

---

**Section 3 - Gradient Descent as a Dynamical System (2 pages)**

Define the loss function - mean squared error. Write it explicitly. Derive the gradient with respect to each weight using the chain rule - this is A-level calculus differentiation. Show that gradient descent is a discrete dynamical system - a recurrence relation updating weights at each step. Write it in matrix form. This is FM matrices and recurrence relations directly.

Then the key insight: linearise the network around its initialisation using first order Taylor expansion - FM content. Show that under this linearisation the network dynamics become a linear ODE. Solve it - exponential decay of the loss. This uses FM differential equations directly.

Maths used: differentiation, chain rule, Taylor series, recurrence relations, first order ODEs, matrix form of linear systems. All FM content.

---

**Section 4 - The Gram Matrix and Its Eigenvalues (2 pages)**

Define the Gram matrix - also called the kernel matrix - as the matrix of dot products between gradients at each training point. Write it out explicitly for your two-layer example. This is a symmetric positive semidefinite matrix - prove this using FM matrix properties.

Now the central result: the loss under gradient descent decays at a rate determined by the eigenvalues of this Gram matrix. Derive this explicitly - plug the linearised dynamics from Section 3 into the loss function and show the eigenvalue structure controls convergence. If the smallest eigenvalue is bounded away from zero the loss goes to zero.

This is the NTK in disguise - the Gram matrix of gradients is exactly the empirical NTK. Name it here.

Maths used: symmetric matrices, eigenvalues of real symmetric matrices, positive definiteness, spectral theorem. All FM content. Eigenvalue derivation from characteristic polynomial.

---

**Section 5 - What the Eigenvalues Tell You (2 pages)**

This is the payoff section. Show that the eigenvalues of the NTK/Gram matrix encode two things simultaneously:

First - convergence speed. Large eigenvalues mean the network learns fast. Small eigenvalues mean slow learning. Derive this from the exponential decay formula in Section 3.

Second - what gets learned first. The eigenvectors of the NTK correspond to different frequency components of the target function. Large eigenvalue eigenvectors are smooth low-frequency components. Small eigenvalue eigenvectors are high-frequency noise. The network learns smooth structure before fitting noise. This is called spectral bias.

Prove spectral bias for your two-layer example by computing the eigenvalues explicitly - show the low frequency components have larger eigenvalues. This is a concrete computation using your FM diagonalisation toolkit.

Maths used: diagonalisation, eigenvalue ordering, interpretation of eigenvectors as frequency components via connection to Fourier series - FM content.

---

**Section 6 - Why Overparameterisation Helps (1 page)**

Pull it together. Show that as the number of hidden units n grows, the NTK converges to a deterministic limit - the infinite width NTK. In this limit the smallest eigenvalue is bounded below by a positive constant. This means the loss always goes to zero. The network always fits the training data.

But - and this is the key - the NTK in this limit corresponds to a kernel with a specific eigenvalue decay rate that biases the network toward smooth functions. So it fits the data AND prefers smooth solutions. That's why it generalises.

The paradox is resolved: overparameterisation forces the NTK eigenvalue structure to be benign. More parameters means better conditioned Gram matrix means faster convergence to a solution that is smooth by construction.

Maths used: limits, matrix convergence, condition number of a matrix. FM content.

---

**Section 7 - A Concrete Worked Example (2 pages)**

This is what makes it yours and not a textbook summary.

Take the simplest possible network: one input, one hidden layer with two neurons, one output. ReLU activation. Compute everything explicitly:

- Write the network function f(x, theta) with all weights written out
- Compute partial f / partial theta for each weight explicitly using chain rule
- Construct the 2x2 Gram matrix for two training points
- Compute its eigenvalues using the characteristic polynomial - FM diagonalisation
- Show explicitly which eigenvector corresponds to the smooth component and which to the noisy component
- Show the loss decay rate for each component

Every step is your own computation. Every step uses FM maths. An interviewer can ask you to redo any line on a whiteboard and you can do it.

Maths used: everything from Sections 2-6 applied concretely. Full FM matrix toolkit.

---

**Section 8 - Open Questions and Limitations (half page)**

Be honest about what this exposition doesn't cover. The full NTK requires functional analysis beyond A-level. Finite width networks don't perfectly follow NTK dynamics. The theory explains interpolation but not always out-of-distribution generalisation. State these gaps cleanly - this signals genuine understanding not just summary.

---

**Section 9 - Conclusion (half page)**

One paragraph. The eigenvalue structure of the gradient Gram matrix - the Neural Tangent Kernel - resolves the generalisation paradox. Overparameterisation produces a well-conditioned NTK with spectral bias toward smooth functions. The maths is entirely linear algebra and calculus applied carefully.

---

**Total length:** 12-15 pages of genuine mathematical exposition with full derivations.

**What this signals to an adcom:**

A student who took FM eigenvalue content and independently connected it to the most important open theoretical problem in AI. Derived the NTK from scratch. Computed it explicitly for a concrete example. Understood its spectral properties. And wrote it up with the rigour of a mathematics paper.

That is not a high school project. That is independent mathematical thinking at undergraduate level applied to a frontier research question.

Build Section 7 first - the concrete example. That's the anchor. Everything else is built around it.
