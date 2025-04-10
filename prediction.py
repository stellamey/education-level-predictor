import streamlit as st
import pandas as pd
import joblib

@st.cache_resource
def load_model():
    return joblib.load("xgb_education_model.pkl")

model = load_model()

county_names = {
    1: "Mombasa", 2: "Kwale", 3: "Kilifi", 4: "Tana River", 5: "Lamu", 6: "Taita Taveta",
    7: "Garissa", 8: "Wajir", 9: "Mandera", 10: "Marsabit", 11: "Isiolo", 12: "Meru",
    13: "Tharaka-Nithi", 14: "Embu", 15: "Kitui", 16: "Machakos", 17: "Makueni", 18: "Nyandarua",
    19: "Nyeri", 20: "Kirinyaga", 21: "Murang’a", 22: "Kiambu", 23: "Turkana", 24: "West Pokot",
    25: "Samburu", 26: "Trans-Nzoia", 27: "Uasin Gishu", 28: "Elgeyo-Marakwet", 29: "Nandi",
    30: "Baringo", 31: "Laikipia", 32: "Nakuru", 33: "Narok", 34: "Kajiado", 35: "Kericho",
    36: "Bomet", 37: "Kakamega", 38: "Vihiga", 39: "Bungoma", 40: "Busia", 41: "Siaya",
    42: "Kisumu", 43: "Homa Bay", 44: "Migori", 45: "Kisii", 46: "Nyamira", 47: "Nairobi"
}
county_lookup = {v: k for k, v in county_names.items()}

# Mappings
radio_map = {"Never": 0, "Occasionally": 1, "Frequently": 2}
usage_map = {"Never": 0, "Rarely": 1, "Sometimes": 2, "Frequently": 3}

toilet_mapping = {
    "Flush to piped sewer system": 22, "Flush to septic tank": 21,
    "Flush to pit latrine": 23, "Ventilated Improved Pit latrine": 11,
    "Pit latrine with slab": 96, "Composting toilet": 97,
    "Pit latrine without slab/open pit": 12, "Bucket toilet": 13,
    "No facility/bush/field": 31, "Hanging toilet/latrine": 15,
    "Other": 43, "Unknown type": 14, "Traditional pit latrine": 41,
    "Unspecified latrine": 42
}

water_mapping = {
    "Piped Water": 14, "Protected Well": 12, "Protected Spring": 13,
    "Bottled Water": 96, "Public Tap/Standpipe": 71, "Rainwater Harvesting": 62,
    "Composting Water Source": 97, "Tube Well/Borehole": 11, "Tanker Truck": 61,
    "Other Improved Source": 43, "Unprotected Well": 31, "Unprotected Spring": 21,
    "Unprotected Well Alt": 51, "Surface Water": 41, "River/Dam/Lake": 32, "Other Source": 42
}

def show_prediction():

    
    st.title("🎓 Education Level Predictor")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        selected_county = st.selectbox("🌍 Region (County)", list(county_lookup.keys()))
        region_code = county_lookup[selected_county]
        st.slider("💰 Wealth Index Score", -243733.0, 268850.0, 0.0, key="wealth_index_score")
        st.slider("📏 Household Size", 1, 24, 5, key="household_size")

    with col2:
        st.slider("📍 Years in Current Place", 0, 96, 10, key="years_in_current_place")
        st.slider("📅 Household Head Age", 15, 98, 40, key="household_head_age")
        st.selectbox("📻 Listens to Radio", list(radio_map.keys()), key="listens_radio_label")

    with col3:
        st.selectbox("📺 Watches TV", list(radio_map.keys()), key="watches_tv_label")
        st.selectbox("📶 Internet Usage Frequency", list(usage_map.keys()), key="internet_usage_freq_label")
        st.selectbox("🚰 Drinking Water Source", list(water_mapping.keys()), key="drinking_water_source_label")

    with col4:
        st.selectbox("🚽 Toilet Facility", list(toilet_mapping.keys()), key="toilet_facility_label")
        st.slider("🏫 Distance to School (km)", 0.0, 25.0, 5.0, key="distance_to_school")
        st.slider("🏥 Distance to Healthcare (km)", 0.0, 50.0, 10.0, key="distance_to_healthcare")

    input_data = {
        "Region": region_code,
        "Internet_Usage_Freq": usage_map[st.session_state.internet_usage_freq_label],
        "Listens_Radio": radio_map[st.session_state.listens_radio_label],
        "Watches_TV": radio_map[st.session_state.watches_tv_label],
        "Wealth_Index_Score": st.session_state.wealth_index_score,
        "Distance_to_Healthcare_km": st.session_state.distance_to_healthcare,
        "Household_Head_Age": st.session_state.household_head_age,
        "Household_Size": st.session_state.household_size,
        "Years_in_Current_Place": st.session_state.years_in_current_place,
        "Distance_to_School_km": st.session_state.distance_to_school,
        "Drinking_Water_Source": water_mapping[st.session_state.drinking_water_source_label],
        "Toilet_Facility": toilet_mapping[st.session_state.toilet_facility_label],
    }

    input_df = pd.DataFrame([input_data])

    if st.button("🔮 Predict Education Level", use_container_width=True):
        prediction = model.predict(input_df)
        education_levels = ["No Education", "Primary", "Secondary", "Tertiary"]
        st.success(f"🎯 Predicted Education Level: **{education_levels[int(prediction[0])]}**")
        st.session_state["last_input"] = input_df
