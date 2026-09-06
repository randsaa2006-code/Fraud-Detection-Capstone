"""
Fraud Detection — Streamlit Deployment App

Loads the final model artifact produced by
`sprint4/02_final_training_pipeline.ipynb` (models/final_model.keras +
models/final_scaler.joblib) and serves single-transaction fraud predictions.

Run locally:
    streamlit run streamlit_app.py

Deploy for free at a public URL via Streamlit Community Cloud
(streamlit.io/cloud) by pointing it at this file in your GitHub repo.
"""

import joblib
import numpy as np
import pandas as pd
import streamlit as st
import tensorflow as tf

MODEL_PATH = "models/final_model.keras"
SCALER_PATH = "models/final_scaler.joblib"
THRESHOLD = 0.93  # chosen in Sprint 3 (02_hyperparameter_tuning_threshold_optimisation.ipynb)


@st.cache_resource
def load_artifacts():
    model = tf.keras.models.load_model(MODEL_PATH)
    bundle = joblib.load(SCALER_PATH)
    return model, bundle["scaler"], bundle["scale_cols"], bundle["feature_order"]


def prepare_features(time_val, amount, v_values, scaler, scale_cols, feature_order):
    row = {f"V{i+1}": v_values[i] for i in range(28)}
    row["Time"] = time_val
    row["Amount"] = amount
    df = pd.DataFrame([row])

    df[scale_cols] = scaler.transform(df[scale_cols])
    df["Hour"] = (df["Time"] // 3600) % 24
    df["Amount_log"] = np.log1p(df["Amount"])

    return df[feature_order]


def main():
    st.set_page_config(page_title="Fraud Detection", page_icon="🕵️")
    st.title("🕵️ Credit Card Fraud Detection")
    st.caption(
        "Phase 3 Capstone — enter a transaction's details to get a fraud prediction "
        "from the final trained model."
    )

    try:
        model, scaler, scale_cols, feature_order = load_artifacts()
    except Exception as e:
        st.error(
            f"Could not load model artifacts ({type(e).__name__}: {e}). "
            f"Make sure `models/final_model.keras` and `models/final_scaler.joblib` "
            f"exist (run `02_final_training_pipeline.ipynb` first)."
        )
        return

    st.subheader("Transaction Details")

    col1, col2 = st.columns(2)
    with col1:
        amount = st.number_input("Amount ($)", min_value=0.0, value=50.0, step=1.0)
    with col2:
        time_val = st.number_input(
            "Time (seconds since first transaction in dataset)",
            min_value=0.0, value=50000.0, step=1.0,
        )

    st.subheader("Anonymized Features (V1–V28)")
    st.caption(
        "These come from a PCA transform in the original dataset and aren't "
        "human-interpretable individually. Leave at 0 for a 'typical' transaction, "
        "or paste real values from a dataset row to test a known case."
    )

    with st.expander("Enter V1–V28 (or leave as 0)", expanded=False):
        v_cols = st.columns(4)
        v_values = []
        for i in range(28):
            with v_cols[i % 4]:
                v_values.append(
                    st.number_input(f"V{i+1}", value=0.0, format="%.4f", key=f"v{i+1}")
                )

    if st.button("Predict", type="primary"):
        X = prepare_features(time_val, amount, v_values, scaler, scale_cols, feature_order)
        proba = float(model.predict(X, verbose=0).ravel()[0])
        is_fraud = proba >= THRESHOLD

        st.subheader("Result")
        st.metric("Fraud probability", f"{proba:.4f}")
        st.metric("Decision threshold", f"{THRESHOLD}")

        if is_fraud:
            st.error("🚨 Predicted: FRAUD")
        else:
            st.success("✅ Predicted: Not Fraud")

        st.caption(
            "This threshold was chosen in Sprint 3 by maximizing F1 on validation "
            "data — in a real deployment it would instead reflect the actual cost "
            "of a false positive vs. a false negative for the business."
        )

    st.divider()
    st.caption(
        "Model: dense neural network with Batch Normalization + Dropout, "
        "trained with class weighting on the Kaggle Credit Card Fraud Detection "
        "dataset. See the project README for full methodology, limitations, "
        "and SHAP-based explainability."
    )


if __name__ == "__main__":
    main()
