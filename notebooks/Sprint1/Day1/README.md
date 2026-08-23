# 🧠 Sprint 1 — Day 1: Planning & Neural Network Architecture

**BinX Tech • AI & Machine Learning Internship • Phase 3, Sprint 1 (Week 6)**

## 📖 Overview

This notebook opens Sprint 1 of the Fraud Detection capstone. It formally kicks off the sprint, finalizes the project dataset, establishes a leakage-safe baseline model, and introduces the building block of neural networks — the single neuron — ahead of Days 2-5, where the actual network gets built in Keras.

## 🎯 Learning Objectives

By the end of today, I am able to:

- Complete Sprint 1 planning and establish a baseline model for the Phase 3 project.
- Explain a single neuron as a weighted sum, bias, and activation.
- Describe the role of input, hidden, and output layers and what "deep" means.

## 📌 Topics Covered

- Sprint 1 planning: goal, backlog, and baseline first
- Why deep learning: unstructured, high-dimensional data
- The neuron: weighted sum + bias + activation (the Week 2 dot product)
- Layers: input, hidden, output
- Weights and biases as the learned parameters

## 📊 Dataset

**Kaggle Credit Card Fraud Detection Dataset** (`mlg-ulb/creditcardfraud`) — the real, full dataset: 284,807 European card transactions from September 2013, 31 columns (`Time`, `V1`-`V28` PCA-anonymized features, `Amount`, `Class`).

**Data-quality finding:** 1,081 exact duplicate rows were identified and removed before any splitting — including 19 duplicate fraud cases. This was a deliberate, documented decision (not an automatic cleanup step), since removing duplicated fraud rows reduces an already-rare class further; the choice and its trade-off are recorded in Markdown before the removal is applied.

**Class balance after deduplication:** 283,726 transactions, fraud prevalence 0.1667% — confirming this is a genuinely severe imbalanced classification problem, not just a standard binary task.

## 🖥️ Hands-On Lab: Sprint 1 Kickoff & Baseline

1. Completed Sprint 1 planning: confirmed the sprint goal and selected the first backlog tasks.
2. Finalized the project dataset and completed data-quality checks (missing values, duplicates, target sanity check, leakage check).
3. Trained a simple baseline model (Logistic Regression) inside a leakage-safe pipeline and recorded its metrics.
4. Documented the baseline score every later model — including this week's neural network — must beat.
5. Computed a single neuron's forward calculation by hand (weighted sum + bias + ReLU) to connect the architecture concept to the Week 2 dot product.

## 🔑 Key Findings

- **Duplicates:** 1,081 exact duplicate rows removed (19 were fraud cases) — documented as a data-quality decision, not an automatic step.
- **Stratified split** preserved the fraud rate almost exactly between train (0.1665%) and test (0.1674%) sets.
- **Baseline (Logistic Regression) — Sprint 1 benchmark to beat:**
  - ROC-AUC: **0.9657**
  - PR-AUC: **0.6719**
  - Recall: **0.8737** (caught 83 of 95 fraud cases in the test set)
  - F1: **0.1059**
- **Reading the trade-off correctly:** the high recall came at the cost of 1,389 false positives — the model is very sensitive to fraud but not yet precise. This asymmetry (catch real fraud vs. avoid false alarms) is the exact tension this capstone is built to explore in later sprints (SMOTE, threshold tuning, SHAP), not a flaw to "fix" today.
- Target leakage check confirmed no feature trivially encodes the label before modeling began.

## 🛠 Tools Used

Scikit-learn (`LogisticRegression`, `Pipeline`, `StandardScaler`) • Pandas • NumPy • Matplotlib • Jupyter/Colab • Git & GitHub

## 📤 GitHub Submission

Notebook and dataset committed to `Fraud-Detection-Capstone`, under Sprint 1 / Day 1, on the `feature/sprint1-dataset-selection` branch (to be opened as a pull request for mentor review per the program's acceptance criteria).

## 💭 Reflection

Today's biggest lesson was that a "clean baseline" isn't just about code running without errors — it's about making and documenting real judgment calls, like whether to remove duplicate fraud rows from an already-rare class. The recall/precision trade-off in the baseline results also reframed how I'll judge every later model this project: a higher-looking accuracy or F1 number means nothing if I don't know which type of error it's trading away.

## ✅ Conclusion

Sprint 1 is underway with a documented problem dataset, a leakage-safe baseline (ROC-AUC 0.9657, PR-AUC 0.6719, Recall 0.8737, F1 0.1059), and the conceptual foundation for the neural network to come. Every result from Days 2-5 — activations, training mechanics, the trained Keras network, and its tuning — will be measured against this exact benchmark.
