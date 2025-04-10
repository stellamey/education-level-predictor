import streamlit as st
from PIL import Image

def show_analysis():
    st.title("📊 Insights from EDA")
    st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

    images_with_captions = [
        
        ("Internet Access Distribution by Wealth Category.png", 
         "Internet Access Distribution by Wealth Category"),
        ("Distribution of Education Level by Household Size.png", 
         "Distribution of Education Level by Household Size"),
        ("Distribution of Education Level by Wealth Category.png", 
         "Distribution of Education Level by Wealth Category"),
        ("Distribution of Households by Drinking Water Source.png", 
         "Distribution of Households by Drinking Water Source"),
        ("Distribution of Households by Household Size.png", 
         "Distribution of Households by Household Size"),
        ("Distribution of Households by Internet Access.png", 
         "Distribution of Households by Internet Access"),
        ("Distribution of Education Level by Distance to School.png", 
         "Distribution of Education Level by Distance to School"),
        ("Distribution of Education Level by Distance to Healthcare.png", 
         "Distribution of Education Level by Distance to Healthcare"),
        ("Distribution of Households by Distance to School.png", 
         "Distribution of Households by Distance to School"),
        ("Education Distribution counties1.png", "Education Distribution Counties 1"),
        ("Education Distribution counties2.png", "Education Distribution Counties 2"),
        ("Education Distribution counties3.png", "Education Distribution Counties 3"),
        ("Education Distribution counties4.png", "Education Distribution Counties 4"),
        ("patial Distribution of Households, Schools, Healthcare Facilities, and Towns.png", 
         "Spatial Distribution of Households, Schools, Healthcare Facilities, and Towns"),
    ]

    image_size = (900, 550)
    col = st.container()

    for image_file, caption in images_with_captions:
        try:
            img = Image.open(image_file).resize(image_size)
            with col:
                st.image(img, use_container_width=True)
                st.markdown(f"**{caption}**", unsafe_allow_html=True)
                st.markdown("---")
        except FileNotFoundError:
            st.warning(f"⚠️ Missing image: {image_file}")
