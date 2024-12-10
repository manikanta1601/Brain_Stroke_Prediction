import streamlit as st
import json
from streamlit_lottie import st_lottie

# Define lifestyle mapping dictionaries (outside the function for reusability)
alcohol_mapping = {"No alcohol consumption": 0, "Alcohol consumption": 1}
smoke_mapping = {"Non-smoker (does not smoke)": 0, "Smoker (does smoke)": 1}
sleep_disorder_mapping = {"No sleep disorder": 1, "Sleep disorder": 2}

# Load Lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_lifestyle = load_lottiefile("./assets/lifestyle.json")

def lifestyle():
    # Session state variables to store user input
    if "user_data" not in st.session_state:
        st.session_state["user_data"] = {}

    user_data = st.session_state["user_data"]

    st.title("Lifestyle Habits")
    st.subheader("Please fill out your lifestyle habits.")

    # Create columns for the layout with adjusted proportions
    col1, col2 = st.columns([3, 3])

    with col1:
        # Alcohol consumption with default value
        alcohol_options = ["No alcohol consumption", "Alcohol consumption"]
        alcohol = st.selectbox("Alcohol Consumption", options=alcohol_options, index=alcohol_options.index("No alcohol consumption"))
        user_data["alcohol"] = alcohol_mapping[alcohol]

        # Smoking status with default value
        smoke_options = ["Non-smoker (does not smoke)", "Smoker (does smoke)"]
        smoke = st.selectbox("Smoking Status", options=smoke_options, index=smoke_options.index("Non-smoker (does not smoke)"))
        user_data["smoke"] = smoke_mapping[smoke]

        # Sleep disorder with default value
        sleep_disorder_options = ["No sleep disorder", "Sleep disorder"]
        sleep_disorder = st.selectbox("Sleep Disorder", options=sleep_disorder_options, index=sleep_disorder_options.index("No sleep disorder"))
        user_data["sleep_disorder"] = sleep_disorder_mapping[sleep_disorder]

        # General health condition with default value
        general_health_options = [
            "Optimal Health",
            "Stable Health",
            "Mild Health Issues",
            "Significant Health Issues",
            "Severe Health Issues"
        ]
        general_health = st.selectbox("General Health Condition", options=general_health_options, index=general_health_options.index("Optimal Health"))
        user_data["general_health_condition"] = general_health_options.index(general_health) + 1

        # Depression level with default value
        depression_options = ["No Depression", "Mild Depression", "Severe Depression"]
        depression = st.selectbox("Depression Level", options=depression_options, index=depression_options.index("No Depression"))
        user_data["depression"] = depression_options.index(depression) + 1

        # Sleep time in hours (3 to 11 hours) with default value
        sleep_time = st.slider("Sleep Time (hours)", min_value=3, max_value=11, value=7)
        user_data["sleep_time"] = sleep_time

        # Minutes of sedentary activity (0 to 840 minutes) with default value
        sedentary_minutes = st.slider("Minutes of Sedentary Activity", min_value=0, max_value=840, value=240)
        user_data["sedentary_minutes"] = sedentary_minutes

        # Next button with navigation
        if st.button("Next (Health Metrics)"):
            st.success("Information saved! Proceeding to Health Metrics.")
            st.session_state["current_page"] = "health_metrics"
            st.session_state.S = 0  # Set `S` to 0 to skip the sidebar update
            st.rerun()

    with col2:
        st_lottie(
            lottie_lifestyle,
            speed=1,
            reverse=False,
            loop=True,
            quality="high",
            height=300,  # Adjust height
            width=350,   # Adjust width
            key="lifestyle_animation"
        )
        st.write("")  # Space between form and animation
