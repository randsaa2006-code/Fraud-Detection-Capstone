# 🧠 Sprint 1 — Day 4: Building & Training a Network in Keras

**BinX Tech • AI & Machine Learning Internship • Phase 3, Sprint 1 (Week 6)**

## 📖 Overview

This notebook builds and trains the first real neural network for the Fraud Detection project using the Keras Sequential API, moving from the manual forward-pass math of Days 1-3 to a framework that handles forward propagation, backpropagation, and optimization automatically.

## 🎯 Learning Objectives

- Build a neural network with the Keras Sequential API.
- Compile, train, and evaluate the network, and read its training history.
- Apply batch normalization and dropout to stabilize training and reduce overfitting.

## 📌 Topics Covered

- TensorFlow/Keras as the high-level framework
- The Sequential API and Dense layers
- Compile / fit / evaluate workflow
- Reading the training history (loss curves)
- Batch normalization and dropout

## 📊 Dataset

Same **Kaggle Credit Card Fraud Detection Dataset** used on Days 1-3 (284,807 transactions, `Class` target), loaded via the same local-file-first/Google Drive-fallback pattern, with the same duplicate-removal step applied for consistency across the sprint.

## 🖥️ Hands-On Lab: Training a Neural Network

1. Built a Keras Sequential network with the correct output layer (sigmoid) and loss (binary cross-entropy) for this project's binary classification task.
2. Compiled with Adam and trained with a validation split for 30 epochs.
3. Plotted training vs. validation loss and accuracy from the `history` object and diagnosed the fit.
4. Added dropout and batch normalization and compared the new loss curves to the previous run.
5. Evaluated on the test set and compared the score to the Day 1 baseline.

## 🔑 Key Findings

- **Original network (30 epochs):** best validation loss 0.0038, best validation accuracy 99.93%.
- **BatchNorm + Dropout network (30 epochs):** best validation loss 0.0042, best validation accuracy 99.93% — comparable validation performance to the original, with the regularization expected to generalize more reliably to unseen data.

- **Final test-set comparison:**

  | Model | Accuracy | ROC-AUC | PR-AUC |
  |---|---|---|---|
  | Day 1 Logistic Regression (baseline) | 0.9787 | **0.9680** | 0.7929 |
  | Day 4 Original NN | 0.9993 | 0.9283 | 0.7843 |
  | **Day 4 BatchNorm + Dropout NN** | **0.9995** | 0.9587 | **0.8145** |

- **Honest verdict:** the regularized neural network won on Accuracy and PR-AUC (the metric that matters most here, given the severe 0.17% fraud rate), improving PR-AUC from 0.7929 to 0.8145. However, **neither neural network beat the simple Logistic Regression baseline on ROC-AUC** (0.9680 vs. 0.9587) — a result worth reporting honestly rather than hiding: more model complexity did not win on every metric.
- Adding BatchNorm + Dropout clearly helped relative to the plain network: every one of its test metrics improved over the original network's.

## 🛠 Tools Used

TensorFlow/Keras • Matplotlib • Pandas • NumPy • Jupyter/Colab (GPU)

## 📤 GitHub Submission

Notebook and README committed to `Fraud-Detection-Capstone`, under `notebooks/Sprint1/Day4/`, on `main`.

## 💭 Reflection

Building this network in Keras made the shift from Day 1-3's manual forward-pass calculations to a production-style workflow concrete: `compile()`, `fit()`, and `evaluate()` mirror the same three-step discipline as Scikit-learn's API from Week 3, just applied to a model that learns its own internal representations. The most important lesson wasn't a win — it was that the neural network didn't beat the baseline on every metric, and reporting that honestly matters more than making the result look uniformly better than it was.

## ✅ Conclusion

Today produced the project's first trained neural network, evaluated fairly against the Day 1 baseline. The regularized version improved on PR-AUC and accuracy but not ROC-AUC — a genuinely mixed result that sets up Day 5's tuning work with a clear, honest target to improve on.
