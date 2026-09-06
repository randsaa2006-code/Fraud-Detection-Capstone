# 📊 Sprint 1 — Data Understanding & ML Baseline

**Fraud Detection Capstone**

## 📖 Sprint Overview

Sprint 1 establishes the foundation: understand the data, prepare it correctly, and build baseline models to measure every later improvement against.

**Dataset:** Kaggle Credit Card Fraud Detection — this project uses a **30,000-row sample** (52 fraud cases, ~0.17% — matches the known real fraud rate), not the full 284,807-row dataset. Noted here since it affects how confidently later sprints' comparisons should be read.

## 📓 Notebooks

| # | Notebook | Focus | Status |
|---|---|---|---|
| 1 | [`01_exploratory_data_analysis.ipynb`](./01_exploratory_data_analysis.ipynb) | Dataset shape, target distribution, missing/duplicate/infinite-value checks, feature distributions | ✅ Done |
| 2 | [`02_data_preprocessing_feature_engineering.ipynb`](./02_data_preprocessing_feature_engineering.ipynb) | Scaling, train/val/test split (leak-free), feature engineering | ✅ Done |
| 3 | [`03_baseline_ml_models.ipynb`](./03_baseline_ml_models.ipynb) | Baseline classifiers + a first dense neural network (Keras, ReLU/sigmoid, binary cross-entropy, Adam, EarlyStopping/ModelCheckpoint) | ✅ Done |

## 🏁 Definition of Done (Sprint 1)

- [x] Dataset shape, target balance, and data-quality checks completed
- [x] Train/validation/test split with no leakage between scaling and evaluation
- [x] Baseline model trained and evaluated
- [x] First neural network trained, tuned, and compared to the baseline
- [x] Fixed random seeds for reproducibility

## 📊 Real Results

| Model | Precision | Recall | F1 |
|---|---|---|---|
| Logistic Regression (baseline) | 1.000 | 0.500 | 0.667 |
| Dense Neural Network | 1.000 | 0.625 | 0.769 |

*(Validation set, 4,498 rows, 8 fraud cases.)*

## 🧭 Key Decisions

- Fixed random seeds and a strict train/validation/test separation were used throughout, since the dataset's severe class imbalance (~0.17% fraud) makes evaluation setup easy to get wrong.
- **Feature engineering runs before scaling, not after** — `Amount_log` (log1p) needs the real dollar amount; applying it to the already-standardized `Amount` (which can be negative) produces invalid values. Caught and fixed during development.
- Metrics beyond raw accuracy (to be expanded in Sprint 3) are needed given the imbalance — flagged here as a carry-forward item.

## 💭 Status

**Sprint 1: Complete.** Baseline and first neural network in place; Sprint 2 improves on the neural network with a properly tuned, regularized architecture.
