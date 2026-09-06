# 🚀 Sprint 4 — Final Model, Deployment & Portfolio

**Fraud Detection Capstone**

## 📖 Sprint Overview

Sprint 4 closes out the project: pick the final model, run a clean end-to-end pipeline, and ship a working deployment.

## 📓 Notebooks & Deliverables

| # | Notebook / Folder | Focus | Status |
|---|---|---|---|
| 1 | [`01_final_model_selection_evaluation.ipynb`](./01_final_model_selection_evaluation.ipynb) | Compared Sprint 1/2/3 models on the same test set, each at its intended threshold; selected the Sprint 3 tuned model | ✅ Done |
| 2 | [`02_final_training_pipeline.ipynb`](./02_final_training_pipeline.ipynb) | Single reproducible script: raw `creditcard.csv` → `models/final_model.keras` + `models/final_scaler.joblib` | ✅ Done |
| 3 | [`03_deployment/`](./03_deployment) | Streamlit app (`streamlit_app.py`) serving the final model | ✅ Built, runs locally — not yet deployed to a public URL |

## 🏁 Definition of Done (Sprint 4)

- [x] Final model selected with a clear, evidence-based justification
- [x] Clean training pipeline that reproduces the final model from raw data
- [x] Model artifact saved (`models/final_model.keras`, `models/final_scaler.joblib`)
- [x] Deployment app built and smoke-tested locally
- [ ] Deployed at a public URL (Streamlit Community Cloud — free, see below)
- [ ] Root `README.md` finalized with full results summary
- [ ] Short technical write-up (approach, results, limitations)

## 📊 Final Model Results (Test Set)

| Metric | Value |
|---|---|
| Precision | 0.700 |
| Recall | 0.875 |
| F1 | 0.778 |
| AUC-PR | 0.764 |
| Threshold | 0.93 |

Trained on the **full uploaded dataset (30,000 rows, 52 fraud cases)** via the consolidated pipeline in notebook 02 — these numbers are more realistic than some of the near-perfect Sprint 3 numbers, since this run reflects the final, complete pipeline end-to-end on the held-out test set.

## 🌐 Deploying to a Public URL (Next Step)

1. Push this repo to GitHub (including `models/final_model.keras` and `models/final_scaler.joblib` — small enough to commit directly, or use Git LFS if needed)
2. Go to [share.streamlit.io](https://share.streamlit.io), connect your GitHub account
3. Point it at `sprint4/03_deployment/streamlit_app.py`, using `requirements.txt` in the same folder
4. Deploy — you'll get a public `*.streamlit.app` URL to put in the root README

## 🧭 Key Decisions

- Deployment app takes `Amount`, `Time`, and `V1`–`V28` as direct inputs (matching the dataset's real feature set) rather than a simplified fake schema — so it can be tested against real dataset rows.
- Kept the deployment scope intentionally minimal (single-prediction form) rather than building batch upload or a dashboard — a working simple app beats an ambitious broken one under a tight timeline.

## ⚠️ Known Limitation (carried from Sprints 1–3)

All results across this project come from a **30,000-row sample** of the full 284,807-row Kaggle dataset. Re-running Sprints 1–4 on the full dataset is recommended before finalizing the technical write-up.

## 💭 Status

**Sprint 4: Model, pipeline, and app complete. Remaining: public deployment, final README, and write-up.**
