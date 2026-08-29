# 🏆 Sprint 1 — Deep Learning Intro (Week 6)

**BinX Tech • AI & Machine Learning Internship • Phase 3, Sprint 1**

## 📖 Sprint Overview

Sprint 1 is the first sprint of the Phase 3 Fraud Detection capstone (four one-week sprints, Weeks 6-9). It covers the deep learning foundations — from a single neuron to a tuned, evaluated Keras neural network — while running the full sprint cycle: planning, mid-sprint mentor review, and a closing Sprint Review + Retrospective.

**Dataset (all five days):** Kaggle Credit Card Fraud Detection Dataset — 284,807 real transactions, 492 fraud cases (0.17%), with 1,081 exact duplicate rows (19 of them fraud) identified and removed as a documented data-quality decision on Day 1, then re-applied consistently across every later day for a fair comparison.

## 📅 Day-by-Day Summary

| Day | Focus | Key Result |
|---|---|---|
| **Day 1** | Sprint planning + Logistic Regression baseline | ROC-AUC 0.9680, Recall 87.37% — the benchmark every later model is measured against |
| **Day 2** | Activations, forward propagation, loss | Output activation (sigmoid) and loss (binary cross-entropy) chosen from the data's actual 2 classes, not assumed; hand-computed forward pass verified |
| **Day 3** | Backpropagation, gradient descent, optimizers | Learning-rate experiment: lr=0.01 converged cleanly (loss 30→0.049); lr=0.5 diverged to ~10⁷² — overshooting made concrete |
| **Day 4** | Building & training a Keras network | BatchNorm+Dropout network: Accuracy 0.9995, PR-AUC 0.8145 (beat baseline); ROC-AUC 0.9587 (did not beat baseline's 0.9680) |
| **Day 5** | Tuning, EarlyStopping, Sprint Review | Best of 12 tuning trials selected; EarlyStopping stopped training at epoch 10/100; final tuned model: Accuracy 0.9994, PR-AUC 0.7284 (beat baseline); ROC-AUC 0.9563 (still short of baseline) |

## 🔑 Sprint-Wide Finding

Across both Day 4 and Day 5, the neural network **consistently improved Accuracy and PR-AUC over the Logistic Regression baseline, but never beat it on ROC-AUC.** This pattern held up across two independent training runs (base network, tuned network), which makes it a real signal rather than noise: added architecture and tuning helped where it matters most given the 0.17% fraud rate (PR-AUC), but didn't universally outperform a simple, transparent baseline. This result is reported as-is rather than reframed as an unqualified win — the same standard used for interpreting the cardiac monitoring and Titanic evaluations earlier in the internship.

## 🔄 Sprint 1 Retrospective

- **What went well:** every architecture decision (Day 2's activation/loss choice, Day 5's tuning configuration) was backed by evidence from the actual dataset or experiment logs, not assumption. The Day 1 baseline was independently re-verified on Day 5 rather than trusted from memory, keeping the final comparison fair.
- **What to improve:** training the full 12-trial tuning sweep plus final model on the complete 284,807-row dataset took a long time without GPU access. This should be planned for earlier in future sprints — testing on a smaller stratified sample first, then confirming on the full dataset.
- **One concrete action for Sprint 2:** since the tuned network still trails the baseline on ROC-AUC, Sprint 2's imbalance-handling work (SMOTE, threshold tuning) should specifically track whether addressing the class imbalance directly — not just through model architecture — closes that gap.

## 🛠 Tools Used

TensorFlow/Keras • Scikit-learn • Pandas • NumPy • Matplotlib • Jupyter/Colab (GPU) • Git & GitHub

## 📤 Structure

```
notebooks/Sprint1/
├── Day1/   — Sprint planning + baseline
├── Day2/   — Activations, forward propagation, loss
├── Day3/   — Backpropagation, gradient descent, optimizers
├── Day4/   — Building & training a Keras network
└── Day5/   — Tuning, EarlyStopping, Sprint Review
```

Each day folder contains its own notebook and detailed README; this file summarizes the sprint as a whole.

## ✅ Sprint 1 Status: Closed

All five days complete, documented, and committed to `main`. Sprint 2 (Week 7) begins with imbalance-handling techniques (SMOTE) and threshold tuning, building directly on this sprint's honest baseline-vs-network comparison.
