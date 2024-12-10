import streamlit as st
import json
from streamlit_lottie import st_lottie

# Define gender mapping dictionary (outside the function for reusability)
gender_mapping = {"Male": 1, "Female": 2}

# Load Lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
lottie_personal = load_lottiefile("./assets/personalbro.json")

def personal():
    # Session state variables to store user input
    if "user_data" not in st.session_state:
        st.session_state["user_data"] = {}

    user_data = st.session_state["user_data"]

    st.title("Personal Information")
    st.subheader("Please fill out your personal information.")

    # Create columns for the layout
    col1, col2 = st.columns([3, 3])

    with col1:
        # Gender selection with default value
        gender_options = ["Male", "Female"]
        gender = st.selectbox("Gender", options=gender_options, index=gender_options.index("Male"))
        user_data["gender"] = gender_mapping[gender]  # Map selection to internal value

        # Age selection with default value
        age_options = ["Young (0-30 years)", "Middle-aged (31-60 years)", "Older (61+ years)"]
        age = st.selectbox("Age Group", options=age_options, index=age_options.index("Young (0-30 years)"))
        user_data["age"] = age_options.index(age) + 1  # Map to internal index (1-based)

        # Race selection with default value
        race_options = [
            "White",
            "Black or African American",
            "Asian",
            "Native American or Alaska Native",
            "Other"
        ]
        race = st.selectbox("Race", options=race_options, index=race_options.index("White"))
        user_data["race"] = race_options.index(race) + 1  # Map to internal index (1-based)

        # Marital status selection with default value
        marital_status_options = [
            "Married",
            "Divorced",
            "Single",
            "Widowed",
            "Separated",
            "Domestic Partnership/Cohabiting"
        ]
        marital_status = st.selectbox("Marital Status", options=marital_status_options, index=marital_status_options.index("Married"))
        user_data["marital_status"] = marital_status_options.index(marital_status) + 1  # Map to internal index (1-based)

        # Next button with navigation
        if st.button("Next (Lifestyle Habits)"):
            st.session_state["current_page"] = "lifestyle_habits"
            st.session_state.S = 0  # Set `S` to 0 to skip the sidebar update
            st.success("Information saved! Proceeding to Lifestyle Habits.")
            st.rerun()  # Use st.rerun() instead of st.experimental_rerun()

    with col2:
        st_lottie(
            lottie_personal,
            speed=1,
            reverse=False,
            loop=True,
            quality="high",
            height=280,  # Adjust height
            width=400,   # Adjust width
            key="personal_animation"
        )
