# 🧠 Sprint 1 — Day 4: Building & Training a Network in Keras

**BinX Tech • AI & Machine Learning Internship • Phase 3, Sprint 1 (Week 6)**

## 📖 Overview

This notebook moves from understanding how neural networks learn to actually **building and training a neural network with TensorFlow/Keras**.

Today focuses on the practical Keras workflow: building a model with the Sequential API, compiling it with the appropriate optimizer and loss function, training it, reading its training history, diagnosing the fit, and evaluating it on unseen test data.

The notebook also introduces **Batch Normalization and Dropout** as practical techniques for stabilizing training and reducing overfitting.

## 🎯 Learning Objectives

By the end of today, I am able to:

- Build a neural network using the Keras Sequential API.
- Compile, train, and evaluate a neural network.
- Read and interpret the training history.
- Diagnose training and validation loss/accuracy curves.
- Apply Batch Normalization and Dropout to a neural network.
- Compare neural-network performance with the Day 1 baseline.

## 📌 Topics Covered

- TensorFlow / Keras as a high-level deep-learning framework
- The Keras Sequential API
- Dense layers and network architecture
- `compile()` / `fit()` / `evaluate()` workflow
- Adam optimizer
- Binary Cross-Entropy loss
- Training and validation history
- Training vs. validation loss
- Training vs. validation accuracy
- Batch Normalization
- Dropout
- Test-set evaluation
- Comparison with the Day 1 baseline

## 📊 Dataset

Same **Kaggle Credit Card Fraud Detection Dataset** used throughout the Phase 3 project — the real fraud-detection dataset with **284,807 transactions** and `Class` as the binary target.

- `Class = 0` → normal transaction
- `Class = 1` → fraudulent transaction

The notebook keeps the same project dataset context and applies a leakage-aware train/validation/test split before scaling the features.

Because fraud detection is a highly imbalanced classification problem, the notebook reports not only accuracy but also **ROC-AUC and PR-AUC** when evaluating the models.

## 🖥️ Hands-On Lab: Training a Neural Network

### Step 1 — Build a Keras Sequential Network

Built a binary-classification neural network using the Keras Sequential API:

- Dense layer with 64 neurons + ReLU
- Dense layer with 32 neurons + ReLU
- Output layer with 1 neuron + Sigmoid

The Sigmoid output is appropriate because the Phase 3 project is a binary classification task.

### Step 2 — Compile and Train

Compiled the network with:

- **Adam** optimizer
- **Binary Cross-Entropy** loss
- **Accuracy** metric
- **30 epochs**
- **Batch size = 32**

The model was trained using the training set while monitoring validation performance.

### Step 3 — Analyze the Training History

Used the Keras `History` object to examine:

- Training loss vs. validation loss
- Training accuracy vs. validation accuracy

The curves provide evidence for diagnosing whether the model is learning effectively, underfitting, or showing signs of overfitting.

### Step 4 — Add Batch Normalization and Dropout

Built a second version of the network using:

- `BatchNormalization()`
- `Dropout(0.30)`

The new model was trained under the same general conditions so its validation curves could be compared directly with the original network.

### Step 5 — Evaluate on the Test Set

Evaluated both neural networks on the held-out test set and compared them with the **Day 1 Logistic Regression baseline**.

The comparison uses:

- Accuracy
- ROC-AUC
- PR-AUC
- Test loss

## 🔑 Key Findings

- The Keras workflow turns the concepts from Day 3 into an actual trainable neural network: **build → compile → fit → evaluate**.
- For this fraud-detection task, the correct output configuration is a **single Sigmoid neuron** with **Binary Cross-Entropy** loss because the target is binary.
- The training history provides more useful evidence than a single final score because it shows how training and validation performance change across epochs.
- Batch Normalization and Dropout provide a practical way to modify the network and investigate whether regularization improves validation behavior.
- Because the dataset is highly imbalanced, **accuracy alone is not sufficient** for judging the fraud-detection model. ROC-AUC and PR-AUC are included to provide a more informative comparison.
- The final model comparison is based on the actual validation curves and held-out test-set metrics rather than assuming that the more complex model must perform better.

## 🛡️ Data Quality & Leakage Checks

Several checks were included before and after training:

- Missing-value check
- Infinite-value check
- Target/feature separation
- Verification that `Class` is not included as an input feature
- Stratified train/validation/test splitting
- Verification that the three splits contain no overlapping rows
- Feature scaling fitted only on the training data
- Numerical finiteness checks after scaling
- Reproducibility through fixed random seeds

These checks help ensure that the neural-network results are based on a clean and leakage-aware workflow.

## 🛠 Tools Used

TensorFlow / Keras • NumPy • Pandas • Matplotlib • Scikit-learn • Jupyter/Colab

## 📤 GitHub Submission

Notebook submitted as part of the Phase 3 Sprint 1 project under the Day 4 section of the Fraud Detection Capstone.

The notebook is structured as a GitHub portfolio artifact, with:

- Clear Markdown explanations
- Executable code
- Visualizations
- Data-quality checks
- Model comparisons
- Objective → Evidence mapping
- Reflection
- Beyond-the-Requirement analysis

## 💭 Reflection

Day 4 was the point where the theoretical training mechanics from Day 3 became an actual neural-network implementation.

Instead of manually thinking through every forward pass, gradient, and weight update, Keras provides a high-level interface that handles those operations while still allowing me to control the architecture, optimizer, loss function, training process, and regularization.

The training curves were especially useful because they showed that evaluating a neural network is not just about looking at the final accuracy. Watching training and validation behavior across epochs gives much stronger evidence about whether the model is learning appropriately or starting to overfit.

Adding Batch Normalization and Dropout also connected the neural-network workflow back to the regularization concepts covered earlier in the internship.

## 🚀 Beyond the Requirement

The basic requirement focuses on training and evaluating a Keras network.

To make the notebook stronger for the Fraud Detection project, the analysis goes beyond accuracy by including **ROC-AUC and PR-AUC**, together with leakage checks, reproducibility, validation-curve comparisons, and a direct comparison against the Day 1 baseline.

This makes the model evaluation more appropriate for an imbalanced fraud-detection problem rather than treating accuracy as the only measure of success.

## 🔬 Objective → Evidence Mapping

| Objective | Evidence |
|---|---|
| Build a Keras Sequential network | Dense-based Sequential architecture |
| Choose the correct output layer | Sigmoid output for binary classification |
| Compile the network | Adam + Binary Cross-Entropy |
| Train the network | 30-epoch training run with validation data |
| Read training history | History DataFrame and learning curves |
| Diagnose the fit | Training/validation loss and accuracy comparison |
| Apply regularization | Batch Normalization + Dropout |
| Evaluate the model | Held-out test-set evaluation |
| Compare with previous work | Day 1 baseline comparison |
| Maintain reproducibility | Fixed random seeds + sanity checks |

## ✅ Conclusion

Today moved the Phase 3 project from understanding **how neural networks learn** to actually **building and training one**.

The Keras Sequential API made it possible to translate the architecture into a practical model, while the training history and validation curves provided evidence for diagnosing its behavior.

The addition of Batch Normalization and Dropout introduced practical regularization techniques, and the final test-set comparison connected the new neural network directly to the **Day 1 baseline**.

With the first Keras network successfully implemented and evaluated, **Day 5 can build on this foundation by focusing on improving and tuning the neural-network model rather than starting from scratch.**
