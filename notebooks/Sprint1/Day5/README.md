# 🔧 Sprint 1 — Day 5: Tuning, Evaluation & Sprint Review

**BinX Tech • AI & Machine Learning Internship • Phase 3, Sprint 1 (Week 6)**

## 📖 Overview

This notebook closes Sprint 1 by moving from a working neural network to a systematic tuning and evaluation workflow.

The focus of today is not simply to train another model, but to improve the existing Keras network in a disciplined way by changing one hyperparameter at a time, evaluating its validation behavior, and selecting the configuration supported by the strongest evidence.

The day also introduces Keras callbacks — **EarlyStopping** and **ModelCheckpoint** — to make training more efficient and preserve the best model.

Finally, the notebook assembles the evidence required for the Sprint 1 Review and closes the sprint with a structured retrospective and one concrete improvement for Sprint 2.

## 🎯 Learning Objectives

By the end of today, I am able to:

- Tune a neural network systematically, one variable at a time.
- Prioritize learning rate, network size, dropout, and batch size during tuning.
- Use EarlyStopping to stop training when validation performance stops improving.
- Use ModelCheckpoint to preserve the best model during training.
- Compare neural-network experiments using validation evidence.
- Assemble clear evidence for a Sprint Review.
- Evaluate the final selected model against the project baseline.
- Complete a Sprint Retrospective and define one concrete improvement for Sprint 2.

## 📌 Topics Covered

- Neural-network hyperparameter tuning
- Learning rate
- Network width and depth
- Dropout rate
- Batch size
- One-variable-at-a-time experimentation
- EarlyStopping
- ModelCheckpoint
- Validation loss curves
- Model selection
- Baseline comparison
- Sprint acceptance criteria
- Sprint Review
- Sprint Retrospective

## 📊 Dataset

Same **Kaggle Credit Card Fraud Detection Dataset** used throughout Phase 3 — the real fraud-detection dataset containing **284,807 transactions**, with `Class` as the binary target.

- `Class = 0` → normal transaction
- `Class = 1` → fraudulent transaction

The same project dataset and preprocessing workflow are maintained to keep Sprint 1 results consistent and comparable across Days 1–4.

The validation set is used during tuning and model selection, while the held-out test set is reserved for the final evaluation.

## 🖥️ Hands-On Lab: Sprint 1 Close-Out

### Step 1 — Tune the Network

Tuned the neural network by changing one hyperparameter at a time.

The experiments focused on the recommended tuning priorities:

1. Learning rate
2. Network size
3. Dropout rate
4. Batch size

Each run records its configuration and validation performance so the experiments can be compared systematically.

### Step 2 — Add EarlyStopping

Added the `EarlyStopping` callback to monitor validation loss.

The callback stops training when validation loss stops improving for the specified patience period and restores the best observed weights.

This prevents unnecessary training and helps reduce the risk of continuing to train after the model has stopped improving.

### Step 3 — Add ModelCheckpoint

Added `ModelCheckpoint` to save the best model according to validation loss.

This ensures that the best model is preserved even if later epochs produce worse validation performance.

### Step 4 — Assemble Sprint 1 Evidence

The Sprint Review evidence includes:

- Day 1 baseline score
- Neural-network architecture
- Tuning experiment table
- Validation-loss curves
- Final model configuration
- Final test metrics
- Baseline vs. final model comparison

The evidence is documented directly in the notebook so the Sprint Review can be followed from the actual project results.

### Step 5 — Sprint Review & Retrospective

Completed the Sprint 1 close-out process by reviewing:

- What was completed
- Model performance
- Tuning results
- Acceptance criteria
- Mentor-review status
- What went well
- What could be improved
- One concrete change for Sprint 2

## 🎚️ Tuning Strategy

Neural networks have many hyperparameters, so changing everything simultaneously would make it difficult to understand what caused an improvement or deterioration.

The tuning strategy therefore follows a **one-variable-at-a-time** approach.

The main variables considered are:

| Priority | Hyperparameter | What it controls |
|---|---|---|
| 1 | Learning rate | Size of optimizer updates |
| 2 | Network size | Model capacity |
| 3 | Dropout | Regularization strength |
| 4 | Batch size | Number of samples per update |

For each experiment, the other parameters remain fixed as much as possible so that the effect of the selected variable can be interpreted clearly.

## ⏹️ EarlyStopping & ModelCheckpoint

Two Keras callbacks are used in the final training process.

**EarlyStopping** monitors validation loss and stops training when the model is no longer improving.

**ModelCheckpoint** saves the best model encountered during training.

Together, they make the training process more efficient and ensure that the final selected model corresponds to the strongest validation performance observed during training.

## 📈 Evaluation

The final model is evaluated against the held-out test set after the tuning process is complete.

The evaluation includes the project's baseline comparison and the relevant classification metrics.

The test set is intentionally kept separate from the tuning process so that it remains an unbiased source of final evaluation evidence.

## 🔑 Key Findings

- Neural-network tuning is more informative when performed systematically rather than by changing several hyperparameters at once.
- The learning rate is treated as the highest-priority tuning variable because it directly controls the size of optimizer updates.
- Network size controls model capacity, while dropout provides regularization against over-reliance on individual neurons.
- Batch size changes how many samples are processed before each weight update.
- EarlyStopping provides an automated way to stop training when validation loss stops improving.
- ModelCheckpoint ensures that the best model is not lost if later epochs perform worse.
- The final model should be selected based on validation evidence, with the test set reserved for the final evaluation.
- Sprint Review evidence is stronger when the architecture, experiments, curves, and metrics are all documented together rather than presented as isolated results.

## 🛡️ Sprint Acceptance Criteria

The Sprint 1 review checks that:

- The notebook runs without errors.
- The project code is committed to the correct branch.
- The pull request is submitted and reviewed.
- Mentor feedback is addressed.
- Results are documented in Markdown.
- Metrics are logged and compared with the baseline.
- The neural-network architecture is documented.
- Loss curves are included as evidence.
- The final model and tuning decisions are explainable.

Git/GitHub actions and mentor approval are treated as project workflow items and are not claimed as completed by notebook code alone.

## 📤 GitHub Submission

The Sprint 1 notebooks and project documentation are maintained in the **Fraud-Detection-Capstone** repository.

The Day 5 notebook serves as the Sprint 1 close-out artifact and brings together the modeling, tuning, evaluation, and review evidence from the sprint.

The final submission is intended to provide a reproducible and reviewable record of how the neural network evolved from the initial baseline to the tuned model.

## 👨‍🏫 Sprint Review

The Sprint Review demonstrates the progression made during Sprint 1:

**Day 1 → Baseline**

Established the initial fraud-detection model and evaluation reference.

**Day 2 → Activations & Forward Propagation**

Built the conceptual understanding needed to choose activations and loss functions correctly.

**Day 3 → Backpropagation & Optimization**

Demonstrated how neural networks learn through forward propagation, loss calculation, backpropagation, and gradient-based updates.

**Day 4 → Keras Network**

Built and trained the first practical neural network using TensorFlow/Keras.

**Day 5 → Tuning & Sprint Close-Out**

Systematically tuned the network, introduced callbacks, evaluated the final model, and assembled Sprint 1 evidence.

## 🔄 Sprint 1 Retrospective

### What went well

The sprint successfully progressed from understanding neural-network fundamentals to implementing and evaluating a working Keras model.

The transition from theoretical concepts to practical training was especially useful because the concepts of forward propagation, loss, backpropagation, optimization, and regularization became part of an actual project workflow.

The one-variable-at-a-time tuning approach also provided a more disciplined way to make model decisions.

### What could be improved

As the number of experiments increases, manually tracking configurations and results inside notebook cells becomes harder to maintain.

A more structured experiment-tracking process would make future tuning easier to reproduce and compare.

### 🎯 Concrete Change for Sprint 2

**Log every experiment's configuration, hyperparameters, validation metrics, and final result in a structured experiment-tracking system from the beginning of the sprint.**

This will make future model comparisons more reproducible and reduce the risk of losing important experiment information.

## 💭 Reflection

Day 5 made it clear that improving a neural network is not simply about changing parameters until a better score appears.

The most important part of tuning is having a controlled process where each experiment answers a specific question.

Changing one variable at a time makes the results easier to interpret, while validation curves provide evidence for deciding whether a configuration is actually improving the model.

EarlyStopping and ModelCheckpoint also showed how good training practices can be automated instead of being handled manually.

The biggest lesson from Sprint 1 is therefore the importance of **evidence-based and reproducible model development**, rather than focusing only on the final metric.

## 🚀 Beyond the Requirement

The basic requirement focuses on tuning, callbacks, and Sprint Review.

The notebook goes beyond the minimum by maintaining a structured experiment log, comparing multiple tuning dimensions, documenting the model-selection process, preserving the best model with a checkpoint, and connecting the final results back to the original baseline.

The Sprint Retrospective also turns the review into an actionable improvement for Sprint 2 rather than simply recording what happened.

## 🔬 Objective → Evidence Mapping

| Objective | Evidence |
|---|---|
| Tune a neural network systematically | One-variable-at-a-time experiments |
| Tune learning rate | Learning-rate experiment |
| Tune network size | Architecture experiment |
| Tune dropout | Dropout experiment |
| Tune batch size | Batch-size experiment |
| Use EarlyStopping | Callback configuration and training history |
| Keep the best model | ModelCheckpoint |
| Assemble Sprint evidence | Metric table, architecture, and loss curves |
| Compare with baseline | Baseline vs. final model evaluation |
| Complete Sprint Review | Sprint Review evidence section |
| Complete Retrospective | Reflection + improvement plan |
| Define Sprint 2 improvement | Structured experiment tracking |

## ✅ Conclusion

Day 5 closes Sprint 1 by turning the first working neural network into a more systematic and reviewable modeling workflow.

The network was tuned one variable at a time, EarlyStopping and ModelCheckpoint were introduced to improve training efficiency and preserve the best model, and the final results were assembled into evidence for Sprint Review.

More importantly, Sprint 1 established a complete progression:

**Baseline → Neural Network → Training → Tuning → Evaluation → Review**

With this foundation in place, Sprint 2 can focus on improving the project through a more structured experimentation and tracking process rather than rebuilding the workflow from scratch.
