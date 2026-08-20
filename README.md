# 🕵️ Fraud Detection Model — Phase 3 Capstone

**BinX Tech • AI & Machine Learning Track • Individual Capstone Project**

## 📖 Project Overview

This repository contains my Phase 3 capstone project: a fraud detection model built end-to-end across four one-week sprints (Weeks 6–9). The project applies imbalanced classification techniques — SMOTE, precision-recall trade-offs, and SHAP explanations — to identify fraudulent transactions.

This repo is separate from my Phase 1–2 training repo (`BinX_Internship`), since this is a standalone product-style deliverable rather than a daily training exercise.

## 🎯 Problem Statement

See [`PROBLEM_STATEMENT.md`](./PROBLEM_STATEMENT.md) for the full problem definition and Definition of Done.

## 🏁 Definition of Done

Per the program's professional baseline, this project is complete when it includes:

- [ ] A clean, documented Jupyter Notebook covering the full pipeline: EDA → preprocessing → modeling → evaluation
- [ ] A trained model with reported, cross-validated metrics
- [ ] A working deployment at a public URL (Streamlit or FastAPI)
- [ ] This GitHub repo with a clean README, `requirements.txt`, and saved model artifacts
- [ ] A short technical write-up summarizing approach, results, and limitations

## 🗂️ Repository Structure

```
├── README.md
├── PROBLEM_STATEMENT.md
├── SPRINT1_BACKLOG.md
├── requirements.txt
├── notebooks/          # EDA, modeling, and evaluation notebooks (populated from Week 6)
├── models/              # saved model artifacts (populated from Sprint 2+)
└── outputs/              # plots, confusion matrices, result summaries
```

## 🏃 Sprint Plan

| Sprint | Weeks | Focus |
|---|---|---|
| Sprint 1 | Week 6 | Dataset selection, EDA, baseline model |
| Sprint 2 | Week 7 | Model comparison, imbalance handling (SMOTE), evaluation |
| Sprint 3 | Week 8 | Feature engineering, SHAP explainability, tuning |
| Sprint 4 | Week 9 | Deployment (Streamlit/FastAPI), documentation, final write-up |

See [`SPRINT1_BACKLOG.md`](./SPRINT1_BACKLOG.md) for the current sprint's tasks and acceptance criteria.

## 🛠 Tools Used (planned)

Scikit-learn • Imbalanced-learn (SMOTE) • SHAP • Pandas • NumPy • Matplotlib • Streamlit/FastAPI • Jupyter Notebook • GitHub (feature-branch workflow)

## 📤 Workflow

Each backlog task is developed on its own feature branch and merged via pull request after mentor review, per the program's per-task acceptance criteria.

## 💭 Status

**Current phase:** Sprint 1 planning (Week 5, Day 5). Development begins Week 6.
