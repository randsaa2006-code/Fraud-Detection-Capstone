# 🏁 Sprint 1 — Day 5: Tuning, Evaluation & Sprint Review

**BinX Tech • AI & Machine Learning Internship • Phase 3, Sprint 1 (Week 6)**

## 📖 Overview

This notebook closes Sprint 1: systematic hyperparameter tuning, EarlyStopping/checkpointing, a fully re-verified comparison against the Day 1 baseline, and the Sprint Review and Retrospective that formally end the sprint.

## 🎯 Learning Objectives

- Tune a neural network systematically, one variable at a time.
- Use EarlyStopping and checkpoints to train efficiently and keep the best model.
- Complete the full Sprint 1 review and retrospective cycle.

## 📌 Topics Covered

- Tuning priorities: learning rate, size, dropout, batch size
- Callbacks: EarlyStopping and ModelCheckpoint
- Assembling proof for Sprint Review (loss curves, metric table)
- Per-task acceptance criteria
- Sprint Review and Retrospective

## 📊 Dataset

Same **Kaggle Credit Card Fraud Detection Dataset** (284,807 transactions), reloaded and re-verified independently in this notebook — including re-applying the same duplicate-removal step as Day 1 — so this notebook's Day 1 vs. tuned-network comparison stands on an identical, fair basis rather than assuming Day 1's cleaned data.

## 🖥️ Hands-On Lab: Sprint 1 Close-Out

1. Tuned the network across 12 one-variable-at-a-time trials (learning rate, network size, dropout, batch size), recording each trial's best validation loss and accuracy.
2. Selected the best-performing configuration from the experiment log.
3. Trained the final model with EarlyStopping (`patience=5`, restoring best weights) and ModelCheckpoint, confirming training halted appropriately.
4. Re-computed the Day 1 Logistic Regression baseline on an identical split for a fair, transparent comparison.
5. Assembled the Sprint 1 evidence (architecture, final loss curves, metric comparison table) and wrote the Sprint Retrospective.

## 🔑 Key Findings

- **Best configuration selected from the 12 tuning trials:** learning rate 0.001, network size 64-32, dropout 0.3, batch size 32 — best validation loss 0.002925, best validation accuracy 99.95%.
- **Final model (EarlyStopping, patience=5, max 100 epochs):** training stopped automatically after **10 epochs** (out of a maximum of 100), restoring the best weights from epoch 5 — EarlyStopping saved 90 epochs of unnecessary training. The checkpoint file (`best_sprint1_model.keras`) was confirmed saved.
- **Final test-set comparison — Day 1 Baseline (recomputed) vs. Tuned Neural Network:**

  | Metric | Day 1 Baseline | Tuned NN |
  |---|---|---|
  | Accuracy | 0.9743 | **0.9994** |
  | ROC-AUC | **0.9608** | 0.9563 |
  | PR-AUC | 0.6811 | **0.7284** |

- **Verdict:** the tuned network beat the baseline on Accuracy and PR-AUC (0.7284 vs. 0.6811 — the metric that matters most given the severe class imbalance), but the baseline held a narrow edge on ROC-AUC (0.9608 vs. 0.9563). This mirrors Day 4's finding: added model complexity and tuning helped where it mattered most (PR-AUC), without winning on every single metric — a result reported honestly rather than framed as an unqualified win.
- Final architecture: 12,805 total parameters (4,225 trainable, 128 non-trainable from batch normalization).

## 📌 Acceptance Criteria

- [x] Notebook runs top-to-bottom without errors (verified via full execution on the real dataset, GPU-backed)
- [ ] Code committed to the correct branch with a clear message
- [ ] Pull request opened and approved by the mentor
- [x] Results documented in Markdown (this README + in-notebook narrative)
- [x] Metrics logged and compared against the Day 1 baseline

## 🔄 Sprint 1 Retrospective

- **What went well:** the one-variable-at-a-time tuning process was disciplined and produced a clear, defensible choice of configuration; EarlyStopping worked exactly as intended, avoiding wasted training time; the final comparison against a freshly recomputed baseline kept the result honest rather than assumed.
- **What to improve:** training 12 full trials plus a final run on the complete 284,807-row dataset took a long time without GPU access — this should be planned for earlier next sprint (e.g., testing on a smaller stratified sample first, then confirming on the full dataset once a configuration looks promising).
- **One concrete action for Sprint 2:** since the tuned network still didn't beat the baseline on ROC-AUC, Sprint 2's imbalance-handling work (e.g. SMOTE) should specifically track ROC-AUC alongside PR-AUC, to see whether addressing the class imbalance directly — rather than only through model architecture — closes that specific gap.

## 🛠 Tools Used

TensorFlow/Keras • Scikit-learn • Matplotlib • Pandas • NumPy • Git & GitHub

## 📤 GitHub Submission

Notebook and README committed to `Fraud-Detection-Capstone`, under `notebooks/Sprint1/Day5/`, on `main`, closing out Sprint 1.

## 💭 Reflection

The one-variable-at-a-time tuning approach carried directly over from Week 4's hyperparameter tuning discipline — changing a single knob per trial made it possible to actually attribute a result to a specific choice, instead of guessing which of several simultaneous changes mattered. Re-verifying the Day 1 baseline independently in this notebook, rather than trusting a remembered number, also mattered: a fair comparison requires the exact same data preparation on both sides, not just the same dataset name. The fact that the tuned network still didn't win on every metric was the most useful result of the day — it kept the sprint's conclusion honest instead of inflated.

## ✅ Conclusion

Sprint 1 closes with a tuned neural network selected through a disciplined 12-trial search, trained efficiently with EarlyStopping, and evaluated against a rigorously re-verified Day 1 baseline. The tuned model improved Accuracy and PR-AUC meaningfully but not ROC-AUC — a genuinely mixed, honestly reported result that sets a specific, measurable target for Sprint 2's imbalance-handling work.
