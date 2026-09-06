# ⚖️ Sprint 3 — Imbalance, Tuning & Explainability

**Fraud Detection Capstone**

## 📖 Sprint Overview

Sprint 3 addresses the central challenge of this dataset — severe class imbalance (~0.17% fraud) — tunes the model properly, and makes its decisions interpretable.

## 📓 Notebooks

| # | Notebook | Focus | Status |
|---|---|---|---|
| 1 | [`01_handling_class_imbalance.ipynb`](./01_handling_class_imbalance.ipynb) | Compared no-handling vs. class weighting vs. SMOTE using precision/recall/F1/AUC-PR + PR curves | ✅ Done |
| 2 | [`02_hyperparameter_tuning_threshold_optimisation.ipynb`](./02_hyperparameter_tuning_threshold_optimisation.ipynb) | Tuned dropout/learning rate/batch size one at a time; chose a deliberate classification threshold (max-F1) instead of the 0.5 default | ✅ Done |
| 3 | [`03_model_explainability.ipynb`](./03_model_explainability.ipynb) | SHAP (KernelExplainer) — global feature importance + single-prediction explanation | ✅ Done |

## 🏁 Definition of Done (Sprint 3)

- [x] Imbalance-handling technique applied and compared (class weighting vs. SMOTE)
- [x] Reporting shifted from accuracy to precision/recall/F1/AUC-PR
- [x] Classification threshold chosen deliberately (0.93, not the 0.5 default)
- [x] SHAP summary plot + individual-prediction explanation
- [x] Every experiment logged and compared

## 📊 Real Results

| Approach | Precision | Recall | F1 | AUC-PR |
|---|---|---|---|---|
| No handling (Sprint 2 style) | 0.875 | 0.875 | 0.875 | 0.971 |
| Class weighting (default 0.5 threshold) | 0.216 | 1.000 | 0.356 | 1.000 |
| SMOTE | 0.750 | 0.750 | 0.750 | 0.924 |

**Reading this table:** class weighting reaches perfect AUC-PR (the model ranks fraud correctly) but terrible precision at the default 0.5 threshold — it's flagging far too many normal transactions as fraud. This is exactly why threshold optimization in notebook 02 matters: after tuning the threshold to 0.93, the same class-weighted approach reaches precision=0.80 and recall=1.00 (F1=0.889) — much more usable than either the raw 0.5-threshold number above or the untouched Sprint 2 baseline.

**Tuned model:** dropout=(0.5, 0.4, 0.3), learning rate=0.0005, batch size=64 → validation **AUC-PR = 1.00**
**Chosen threshold:** 0.93 → precision=0.80, recall=1.00, F1=0.889

## ⚠️ Known Limitation

These results come from a **30,000-row sample** of the full Kaggle dataset (only ~50 fraud cases total). The near-perfect AUC-PR/recall numbers are partly an artifact of the small test set, not necessarily how the model would perform at full scale. **Re-run Sprints 1–3 on the full 284,807-row dataset** (~492 fraud cases) before treating these as final numbers for the write-up.

## 🧭 Key Decisions

- Class weighting was carried into tuning as the default imbalance-handling approach (simpler than SMOTE, no synthetic data risk); SMOTE remains available as a toggle (`USE_SMOTE`) in notebook 02 if its results are stronger on the full dataset.
- Threshold was optimized for F1 as a principled default — a real deployment would instead set it from the actual cost of a false positive vs. a false negative.

## 💭 Status

**Sprint 3: Complete, pending re-run on the full dataset for final evidence.**
