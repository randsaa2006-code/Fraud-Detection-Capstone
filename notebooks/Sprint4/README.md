# 🕵️ Credit Card Fraud Detection — ML Capstone Project

An end-to-end machine learning project detecting fraudulent credit card transactions, built independently across four sprints: from raw data to a deployed, explainable model.

**🌐 Live app:** [fraud-detection.streamlit.app](https://fraud-detection.streamlit.app/)

## 📖 Project Overview

This project tackles **binary, highly imbalanced classification** — identifying fraudulent transactions in a dataset where fraud accounts for a tiny fraction of activity (~0.17%). The work goes from exploratory analysis through a tuned, explainable neural network to a working public deployment.

**Dataset:** [Kaggle Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud) — this project uses a **30,000-row sample** (52 fraud cases, same ~0.17% fraud rate as the full 284,807-row dataset). Features `Time`, `V1`–`V28` (PCA-anonymized), `Amount`, target `Class`.

## 🏁 Definition of Done

- [x] Clean, documented notebooks covering EDA → preprocessing → modeling → evaluation
- [x] Trained baseline model with reported metrics
- [x] Trained, tuned final model with reported metrics
- [x] Model explainability (SHAP)
- [x] Working deployment at a public URL
- [x] Repo with README, `requirements.txt`, and model artifacts
- [ ] Short technical write-up *(next up)*

## 🗺️ Project Structure & Results

| Sprint | Focus | Key Result |
|---|---|---|
| [Sprint 1](./sprint1) — Data Understanding & ML Baseline | EDA, preprocessing, baseline models | Dense NN: precision=1.00, recall=0.625, F1=0.769 |
| [Sprint 2](./sprint2) — Deep Learning & Advanced Modelling | Deeper regularized architecture (BatchNorm + Dropout) | Improved architecture, validated against Sprint 1 |
| [Sprint 3](./sprint3) — Imbalance, Tuning & Explainability | Class weighting vs. SMOTE, threshold tuning, SHAP | Tuned model + threshold=0.93, SHAP explainability |
| [Sprint 4](./sprint4) — Final Model, Deployment & Portfolio | Final selection, consolidated pipeline, Streamlit app | **Final test set: precision=0.636, recall=0.875, F1=0.737** |

Each sprint folder has its own README with full details, notebooks, and evidence.

## 📊 Final Model

- **Architecture:** Dense neural network (64→32→16→1) with Batch Normalization + Dropout, trained with class weighting
- **Threshold:** 0.93 (chosen by maximizing F1 on validation data — see Sprint 3)
- **Test set performance:** precision=0.636, recall=0.875, F1=0.737, AUC-PR=0.696
- **Explainability:** SHAP (global feature importance + individual-prediction breakdowns) — see Sprint 3

**Reading these numbers honestly:** recall (0.875) matters most here — the model catches most real fraud — at the cost of some false positives (lower precision). In a real deployment, the threshold would be set based on the actual business cost of a missed fraud vs. a false alarm, not just maximized F1.

## 🛠 Tech Stack

Python • Pandas • NumPy • Scikit-learn • Imbalanced-learn (SMOTE) • TensorFlow/Keras • SHAP • Matplotlib/Seaborn • Streamlit • Jupyter

## 📂 Repository Structure

```
├── README.md                  ← you are here
├── sprint1/                   Data Understanding & ML Baseline
├── sprint2/                   Deep Learning & Advanced Modelling
├── sprint3/                   Imbalance, Tuning & Explainability
└── sprint4/                   Final Model, Deployment & Portfolio
    ├── models/
    │   ├── final_model.keras
    │   └── final_scaler.joblib
    └── 03_deployment/
        ├── streamlit_app.py
        ├── requirements.txt
        └── runtime.txt
```

## 🚀 Running Locally

```bash
git clone <this-repo-url>
cd <repo-name>

# Download creditcard.csv from Kaggle and place it at sprint1/data/creditcard.csv
# (not committed to this repo — see Kaggle link above)

cd sprint4/03_deployment
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## ⚠️ Known Limitations

- All results come from a **30,000-row sample**, not the full 284,807-row dataset. Trends and methodology hold, but exact metrics would shift somewhat on the full data.
- The classification threshold (0.93) was optimized for F1 on validation data as a principled default — a real deployment should set it from the actual cost of false positives vs. false negatives.
- The Streamlit app takes `V1`–`V28` as direct numeric input, since they're anonymized PCA components with no natural user-facing meaning — realistic for a portfolio demo, not for a production fraud system (which would compute these upstream).

## 🧭 Notable Engineering Decision

A real bug was found and fixed during development: an engineered feature (`Amount_log`, a log-transform of transaction amount) was initially computed *after* scaling `Amount` — since standardized values can be negative, this broke the log transform. Fixed by reordering feature engineering to run on raw values before scaling. Documented here rather than quietly patched, since catching this kind of thing is part of the actual work.

## 📝 About This Project

Originally started as part of an AI/ML internship's Phase 3 capstone; completed independently after the program ended, with the project restructured around clear pipeline stages rather than daily training exercises.
