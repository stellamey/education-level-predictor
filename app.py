import streamlit as st
# --- Page Config ---
st.set_page_config(page_title="Education Level Predictor", layout="wide")

import pandas as pd
import analysis
import prediction
import interpretation


# --- Custom CSS ---
st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #122840 !important;
    padding: 30px;
}
.sidebar-title {
    font-size: 36px;
    font-weight: bold;
    color: white !important;
    text-align: center;
    margin-bottom: 20px;
}
.stButton > button {
    width: 100%;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
    margin-bottom: 10px;
}
.stButton > button:hover {
    background-color: #FFD700 !important;
    color: black !important;
}

/* Reduce top spacing */
.block-container {
    padding-top: 1rem !important;
}

/* Home page styling */
.centered {
    text-align: center;
    margin-top: 0px !important;
    padding-top: 0px !important;
}
.hero-title {
    font-size: 40px;
    font-weight: bold;
    color: #1F4172;
    margin-bottom: 20px;
}
.section-subtitle {
    font-size: 20px;
    font-weight: 600;
    margin-top: 20px;
    color: #333;
}
.section-text {
    font-size: 16px;
    color: #444;
    text-align: justify;
    line-height: 1.6;
    padding-right: 10px;
}
</style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.markdown("<p class='sidebar-title'>📚 Education Level Predictor</p>", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Home"

if st.sidebar.button("🏠 Home"):
    st.session_state.page = "Home"
if st.sidebar.button("📊 Analysis"):
    st.session_state.page = "Analysis"
if st.sidebar.button("🤖 Prediction"):
    st.session_state.page = "Prediction"
if st.sidebar.button("🔍 Interpretation"):
    st.session_state.page = "Interpretation"

# --- Page Routing ---
if st.session_state.page == "Home":
    st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem !important;
    }
    .centered {
        text-align: center;
        margin-top: 0px !important;
        padding-top: 0px !important;
    }
    .hero-title {
        font-size: 40px;
        font-weight: bold;
        color: #1F4172;
        margin-bottom: 20px;
    }
    .section-subtitle {
        font-size: 20px;
        font-weight: 600;
        margin-top: 20px;
        color: #333;
    }
    .section-text {
        font-size: 16px;
        color: #444;
        text-align: justify;
        line-height: 1.6;
        padding-right: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="centered">
        <div class="hero-title">📋 Project Overview</div>
    </div>
    <hr style='margin-top: 0; margin-bottom: 2rem;'>

    <div class="section-subtitle">🎯 Objectives</div>
    <p class="section-text">
        The objective of this project is to predict the likely education attainment level of individuals in Kenya using socio-economic and geographic data. 
        It aims to uncover key insights into how factors such as wealth, access to resources, and proximity to infrastructure influence educational outcomes.
    </p>

    <div class="section-subtitle">💡 Justification</div>
    <p class="section-text">
        Education remains a cornerstone for social and economic development. However, disparities in access and attainment persist due to socio-economic inequalities 
        and geographic barriers. By identifying these patterns using data-driven models, stakeholders can make more targeted policy decisions to improve educational access.
    </p>

    <div class="section-subtitle">🛠️ Solution</div>
    <p class="section-text">
        This platform leverages machine learning models like XGBoost to analyze and predict education levels based on key indicators. It also provides interpretability 
        through SHAP to understand feature influence, and geo-socio analysis for context-aware decision-making — making it a practical tool for policy makers, researchers, 
        and development organizations.
    </p>
    """, unsafe_allow_html=True)


elif st.session_state.page == "Analysis":
    analysis.show_analysis()

elif st.session_state.page == "Prediction":
    prediction.show_prediction()

elif st.session_state.page == "Interpretation":
    interpretation.show_interpretation()
