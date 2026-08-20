# 🏃 Sprint 1 Backlog — Week 6

## Sprint Goal

**Understand the data and establish a baseline model to beat.**

## Backlog

### Task 1 — Dataset Selection

**Effort estimate:** 0.5 day

**Description:** Select a public fraud-detection dataset (e.g. Kaggle's Credit Card Fraud Detection dataset) and document its size, features, and class balance in a short data dictionary.

**Acceptance criteria:**
- [ ] Dataset loads correctly in the notebook without errors
- [ ] Class balance (fraud vs. legitimate) is reported explicitly, confirming this is an imbalanced classification problem
- [ ] A short data dictionary (feature names, types, meaning where known) is documented in Markdown
- [ ] Code committed to a feature branch (`feature/sprint1-dataset-selection`) with a clear commit message
- [ ] Pull request opened for mentor review before merging

### Task 2 — Exploratory Data Analysis (EDA)

**Effort estimate:** 1.5 days

**Description:** Explore feature distributions, correlations, and the class imbalance in depth; identify any data-quality issues (missing values, duplicates, implausible values) the way I did in the Week 4 and cardiac-project work.

**Acceptance criteria:**
- [ ] Descriptive statistics and Matplotlib visualizations cover distributions, correlations, and class balance
- [ ] Data-quality issues (if any) are identified and documented with the cleaning decision and its justification
- [ ] Findings are documented in Markdown, not just shown as raw output
- [ ] Code committed to a feature branch (`feature/sprint1-eda`) with a clear commit message
- [ ] Pull request opened for mentor review before merging

### Task 3 — Baseline Model

**Effort estimate:** 1 day

**Description:** Train a simple baseline classifier (e.g. Logistic Regression) on a proper train/test split, and report baseline metrics — this is the number every later sprint's improvement gets measured against.

**Acceptance criteria:**
- [ ] Train/test split is leak-free (fit only on training data)
- [ ] Baseline metrics reported: precision, recall, F1, and ROC-AUC or PR-AUC (accuracy alone is not sufficient given class imbalance)
- [ ] Baseline results and their real-world meaning are documented in Markdown
- [ ] Code committed to a feature branch (`feature/sprint1-baseline-model`) with a clear commit message
- [ ] Pull request opened for mentor review before merging
- [ ] Baseline metrics logged for comparison against every future sprint's models

## Sprint 1 Sign-Off

- [ ] Sprint goal reviewed and approved by mentor before Sprint 1 work begins
