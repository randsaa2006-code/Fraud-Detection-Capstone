# 🎯 Problem Statement — Fraud Detection Model

## The Problem

Fraudulent transactions are rare compared to legitimate ones, but each missed case can carry real financial cost, while too many false alarms erode trust in the system and waste review effort. The goal of this project is to build a machine learning model that flags transactions likely to be fraudulent, learned from historical transaction data, while explicitly accounting for the fact that fraud cases are a small minority of the dataset (an imbalanced classification problem).

## Project Type

**Fraud Detection Model** — imbalanced binary classification, selected from the program's six Phase 3 capstone options.

## Scope

**In scope:**
- Data cleaning and exploratory data analysis on a public or synthetic transaction dataset
- Baseline classifier plus at least one comparison model
- Imbalance-handling techniques (e.g. SMOTE) and evaluation via precision-recall trade-offs rather than accuracy alone
- Model explainability via SHAP
- A working deployment at a public URL (Streamlit or FastAPI)

**Out of scope:**
- Real-time transaction processing or production-grade infrastructure
- Use of identifiable, non-public customer data
- Deep learning / neural network approaches, unless the selected dataset specifically requires them

## Definition of Done

This project is complete when it delivers, per the program's professional baseline:

1. A clean, documented Jupyter Notebook covering the full pipeline: EDA → preprocessing → modeling → evaluation
2. A trained model with reported, cross-validated metrics (precision, recall, F1, and ROC-AUC/PR-AUC given the class imbalance)
3. A working deployment at a public URL (Streamlit or FastAPI)
4. A GitHub repository with a clean README, `requirements.txt`, and saved model artifacts
5. A short technical write-up explaining the approach, results, and limitations

This Definition of Done stays visible from Sprint 1 onward so all four sprints (Weeks 6–9) stay focused on delivering it, rather than drifting into unscoped exploration.
