
import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
import joblib

@st.cache_resource
def load_model():
    return joblib.load("xgb_education_model.pkl")

def show_interpretation():
    # ✅ Add padding at the top
    st.markdown("""
        <style>
        .block-container {
            padding-top: 2rem !important;
        }
        </style>
    """, unsafe_allow_html=True)

    pipeline = load_model()
    st.header("🔍 Model Interpretation: SHAP Waterfall Plot")

    if "last_input" not in st.session_state:
        st.warning("⚠️ Please make a prediction first to see SHAP interpretation.")
        return

    input_df = st.session_state["last_input"]
    classifier = pipeline.named_steps["classifier"]
    preprocessor = pipeline.named_steps["preprocessor"]
    input_transformed = preprocessor.transform(input_df)

    # Predict class
    predicted_class = classifier.predict(input_transformed)[0]

    # SHAP values
    explainer = shap.Explainer(classifier)
    shap_values = explainer(input_transformed)

    # Feature values & names
    values = shap_values.values[0][:, predicted_class]
    base_value = explainer.expected_value[predicted_class]
    features = shap_values.data[0]
    feature_names = input_df.columns.tolist()

    # ✅ DO NOT reverse signs; SHAP will handle coloring
    explanation = shap.Explanation(
        values=values,
        base_values=base_value,
        data=features,
        feature_names=feature_names
    )

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.clf()
    shap.plots.waterfall(explanation, show=False)
    st.pyplot(fig)

    st.caption(
        "🔍 This SHAP plot shows how each feature influenced the predicted education level. "
        "Red bars increase the probability, blue bars decrease it."
    )
