# 🧠 Sprint 2 — Deep Learning & Advanced Modelling

**Fraud Detection Capstone**

## 📖 Sprint Overview

Sprint 2 develops the project's core deep-learning model further: a deeper, regularized neural network, evaluated with real diagnostics — not just a bigger version of the Sprint 1 baseline network.

**Note:** the data is tabular, so the model here is a **dense neural network**, not a CNN/RNN/Transformer — those architectures don't apply to this data type.

## 📓 Notebooks

| # | Notebook | Focus | Status |
|---|---|---|---|
| 1 | [`01_neural_network_fraud_detection.ipynb`](./01_neural_network_fraud_detection.ipynb) | Deeper architecture (64→32→16→1) with Batch Normalization + Dropout, vs. Sprint 1's plain 32→16→1 | ✅ Done |
| 2 | [`02_nn_training_regularization.ipynb`](./02_nn_training_regularization.ipynb) | Trained with EarlyStopping + ModelCheckpoint; ran an unregularized ablation to check the regularization claim directly | ✅ Done |
| 3 | [`03_deep_learning_model_evaluation.ipynb`](./03_deep_learning_model_evaluation.ipynb) | Both models evaluated on the same held-out test set, side by side | ✅ Done |

## 🏁 Definition of Done (Sprint 2)

- [x] Architecture improved beyond the Sprint 1 network (deeper, regularized, justified)
- [x] Batch Normalization and Dropout applied
- [x] EarlyStopping + ModelCheckpoint used, best weights preserved
- [x] Training/validation curves plotted and interpreted
- [x] Final metrics compared against the Sprint 1 baseline in a clear table

## 📊 Real Results

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---|---|---|---|---|
| Sprint 1 Baseline NN | 0.9993 | 0.778 | 0.875 | 0.824 | 0.9999 |
| Sprint 2 Regularized NN | 0.9993 | 0.778 | 0.875 | 0.824 | 0.9997 |

**⚠️ Known limitation:** both models scored *identically* on the test set. This isn't a bug — the uploaded dataset is a 30,000-row sample containing only **8 fraud cases** in the test split, too few to show a meaningful difference between two reasonable architectures. **This needs to be re-run on the full 284,807-row Kaggle dataset** (~492 fraud cases) for a statistically meaningful Sprint 2 comparison before this is presented as final evidence.

## 🧭 Key Decisions

- Core architecture stays a **dense network** — matching the architecture to tabular data rather than adopting a CNN/RNN/Transformer for its own sake.
- Regularization (BatchNorm/Dropout) was tested with an ablation (same architecture, without regularization) rather than assumed to help — see notebook 02.
- Accuracy alone is not sufficient given class imbalance; Sprint 3 introduces proper imbalance-aware handling and metrics.

## 💭 Status

**Sprint 2: Complete, pending re-run on the full dataset for final evidence.**
