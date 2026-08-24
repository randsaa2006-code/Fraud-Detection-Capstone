# 🧠 Sprint 1 — Day 2: Activations, Forward Propagation & Loss

**BinX Tech • AI & Machine Learning Internship • Phase 3, Sprint 1 (Week 6)**

## 📖 Overview

This notebook covers the second building block toward the Phase 3 neural network: activation functions, forward propagation, and loss functions. It also makes the first concrete architecture decision for the Fraud Detection model — which output activation and loss function fit this project's task — based on evidence from the real dataset rather than assumption.

## 🎯 Learning Objectives

By the end of today, I am able to:

- Explain why non-linear activations are essential.
- Choose the correct activation for hidden and output layers.
- Describe forward propagation and select the right loss function for a task.

## 📌 Topics Covered

- Why activations introduce non-linearity
- Common activations: ReLU, sigmoid, softmax, tanh
- Choosing activations by layer and task
- Forward propagation: computing a prediction
- Loss functions: MSE, binary/categorical cross-entropy

## 📊 Dataset

Same **Kaggle Credit Card Fraud Detection Dataset** used in Day 1 — the real, full dataset (284,807 transactions, `Class` target), loaded via the same local-file-first/Google Drive-fallback pattern established on Day 1, so both days work from an identical, verifiable data source.

## 🖥️ Hands-On Lab: Activations & the Forward Pass

1. Plotted ReLU, sigmoid, and tanh over a range of inputs to see how each transforms values.
2. Decided the correct output activation and loss function for the Fraud Detection task, and justified both against the project's actual target labels.
3. Computed one forward pass for a tiny 2-layer network on a sample input, by hand.
4. Documented the choices and the forward-pass result in Markdown.

## 🔑 Key Findings

- **Architecture decision, evidence-based:** confirmed the target has exactly 2 classes (`{0, 1}`) directly from `creditcard.csv` before choosing — hidden layers use **ReLU**, output layer uses **Sigmoid**, loss is **Binary Cross-Entropy**. This mirrors the same "check before you assume" discipline used for the duplicate-detection decision on Day 1.
- **Forward pass (by hand, sample input):** for `X = [0.5, -1.0]`, the network computed `z1 = [0.2, -1.1]` → `a1 = ReLU(z1) = [0.2, 0.0]` → `z2 = 0.32` → `ŷ = sigmoid(z2) ≈ 0.5793`.
- **Loss illustration:** for a true label of 1 against a predicted probability of 0.5793, binary cross-entropy loss ≈ **0.5459** — a concrete number showing how loss penalizes an under-confident correct-direction prediction.
- Activation and forward-pass sanity checks both passed, confirming the manual calculations match expected behavior before any framework code is introduced on Day 4.

## 🛠 Tools Used

NumPy • Matplotlib • Pandas • Jupyter/Colab

## 📤 GitHub Submission

Notebook and README committed to `Fraud-Detection-Capstone`, under `notebooks/Sprint1/Day2/`, on `main`.

## 💭 Reflection

The most useful part of today was deciding the output activation and loss by checking the actual target column instead of assuming "binary classification means sigmoid" as a rule to apply blindly. Walking through one forward pass by hand — rather than jumping straight to Keras — made it clear that a neural network's prediction is just the same weighted-sum-plus-activation operation from Day 1, repeated and stacked across layers.

## ✅ Conclusion

Today locked in the architecture decisions the Fraud Detection network will use: ReLU in hidden layers, sigmoid output, binary cross-entropy loss — each justified against the real dataset rather than assumed. With forward propagation and loss now understood mechanically, Day 3 moves to how the network learns: backpropagation, gradient descent, and optimizers.
