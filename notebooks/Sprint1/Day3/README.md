# 🔁 Sprint 1 — Day 3: Backpropagation, Gradient Descent & Optimizers

**BinX Tech • AI & Machine Learning Internship • Phase 3, Sprint 1 (Week 6)**

## 📖 Overview

This notebook covers how a neural network actually learns: the four-step training loop, gradient descent, the learning rate, backpropagation, and optimizers. It also marks the mid-sprint checkpoint — the Mentor Code & Notebook Review — where this notebook is opened as a pull request for structured feedback before Days 4-5.

## 🎯 Learning Objectives

By the end of today, I am able to:

- Describe the four-step training loop of a neural network.
- Explain gradient descent and the role of the learning rate.
- Explain backpropagation conceptually and name common optimizers, epochs, and batches.

## 📌 Topics Covered

- The training loop: forward → loss → backprop → update
- Gradient descent and the loss surface
- The learning rate and its effect
- Backpropagation: assigning blame via the chain rule
- Optimizers (Adam, SGD), epochs, and batches

## 📊 Dataset

Same **Kaggle Credit Card Fraud Detection Dataset** used on Days 1-2 — the real, full dataset (284,807 transactions, `Class` target: 284,315 normal / 492 fraud), loaded via the same local-file-first/Google Drive-fallback pattern established on Day 1, keeping every day's project context consistent and verifiable.

## 🖥️ Hands-On Lab: Understanding Training + Mentor Review

1. Described the four-step training loop (forward → loss → backprop → update) in Markdown.
2. Trained a tiny controlled model (`ŷ = Xw + b`, MSE loss) at three learning rates — too high, too low, and good — and plotted the resulting loss curves.
3. Explained, in my own words, what backpropagation computes and why the chain rule is involved.
4. Opened this notebook as a pull request for the mid-sprint Mentor Code & Notebook Review.

## 🔑 Key Findings

- **Learning-rate experiment — the core evidence of the day:**

  | Learning rate | Initial loss | Final loss | Outcome |
  |---|---|---|---|
  | 0.001 (too low) | 30.0 | 8.11 | Converges, but far too slowly |
  | 0.01 (good) | 30.0 | **0.049** | Converges efficiently |
  | 0.5 (too high) | 30.0 | ~1.1×10⁷² | **Diverges catastrophically** |

  The high-learning-rate run didn't just fail to improve — it exploded to an astronomical loss value, making "overshooting the minimum" a concrete, numeric result rather than an abstract warning.
- Both the learning-rate sanity checks and the final notebook-wide reproducibility checks passed, confirming the project's dataset (284,807 rows, 2 classes) stayed consistent with Days 1-2.
- Backpropagation is understood as an efficient way to compute how much each weight contributed to the loss (via the chain rule) — not something implemented by hand going forward, since Day 4's Keras work will compute it automatically.

## 🛠 Tools Used

NumPy • Matplotlib • Pandas • Jupyter/Colab • Git & GitHub (pull request)

## 📤 GitHub Submission

Notebook and README committed to `Fraud-Detection-Capstone`, under `notebooks/Sprint1/Day3/`, opened as a pull request for the mid-sprint Mentor Code & Notebook Review per the program's Sprint 1 structure.

## 💭 Reflection

The learning-rate experiment was the clearest lesson of the day: the difference between a model that learns and one that fails outright can come down to a single hyperparameter, and the failure mode isn't subtle — it's a loss curve exploding to nonsense values within a few steps. That made the abstract "foggy hillside" intuition for gradient descent concrete. Framing backpropagation as "assigning blame" to each weight, rather than a wall of calculus, was also the framing that made it click.

## ✅ Conclusion

Today built the mechanical understanding of how a network trains: repeat forward pass → loss → backpropagation → weight update, with the learning rate controlling how large and stable each step is. The learning-rate experiment demonstrated all three outcomes (too slow, good, catastrophic divergence) with real numbers on the exact kind of loss surface this project's models rely on. With training mechanics now understood, Day 4 moves to building and training the first real Keras network for the Fraud Detection project.
