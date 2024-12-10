import streamlit as st
import json
from streamlit_lottie import st_lottie

# Define health metrics mapping dictionaries (outside the function for reusability)
# (Mapping dictionaries are not needed here, but keep them if you plan to use them)

# Load Lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_health = load_lottiefile("./assets/health.json")

def health():
    # Session state variables to store user input
    if "user_data" not in st.session_state:
        st.session_state["user_data"] = {}

    user_data = st.session_state["user_data"]

    st.title("Health Metrics")
    st.subheader("Please fill out your health metrics.")

    # Create columns for the layout with adjusted proportions
    col1, col2 = st.columns([1, 1])

    with col1:
        # Diabetes
        diabetes_options = ["No diabetes", "Diabetes"]
        diabetes = st.selectbox("Diabetes", options=diabetes_options, index=diabetes_options.index("No diabetes"))
        user_data["diabetes"] = diabetes_options.index(diabetes)

        # Hypertension
        hypertension_options = ["No hypertension", "Hypertension"]
        hypertension = st.selectbox("Hypertension", options=hypertension_options, index=hypertension_options.index("No hypertension"))
        user_data["hypertension"] = hypertension_options.index(hypertension)

        # Coronary Heart Disease
        coronary_heart_disease_options = ["No coronary heart disease", "Coronary heart disease"]
        coronary_heart_disease = st.selectbox("Coronary Heart Disease", options=coronary_heart_disease_options, index=coronary_heart_disease_options.index("No coronary heart disease"))
        user_data["coronary_heart_disease"] = coronary_heart_disease_options.index(coronary_heart_disease)

        # Body Mass Index (BMI)
        bmi_options = [
            "Underweight (BMI < 18.5)",
            "Normal weight (BMI 18.5–24.9)",
            "Overweight (BMI 25–29.9)",
            "Obesity (BMI ≥ 30)"
        ]
        bmi = st.selectbox("Body Mass Index (BMI)", options=bmi_options, index=bmi_options.index("Normal weight (BMI 18.5–24.9)"))
        user_data["body_mass_index"] = bmi_options.index(bmi) + 1  # Map to internal index (1-based)

        # Waist Circumference
        waist_circumference = st.slider("Waist Circumference (cm)", min_value=64.45, max_value=146.75, value=80.0)
        user_data["waist_circumference"] = waist_circumference

        # Systolic and Diastolic Blood Pressure
        systolic_bp = st.slider("Systolic Blood Pressure", min_value=84, max_value=180, value=120)
        diastolic_bp = st.slider("Diastolic Blood Pressure", min_value=40, max_value=104, value=80)
        user_data["systolic_blood_pressure"] = systolic_bp
        user_data["diastolic_blood_pressure"] = diastolic_bp

        # HDL and LDL
        hdl = st.slider("High-density Lipoprotein (HDL)", min_value=0.28, max_value=2.33, value=1.0)
        ldl = st.slider("Low-density Lipoprotein (LDL)", min_value=0.70, max_value=5.13, value=2.0)
        user_data["hdl"] = hdl
        user_data["ldl"] = ldl

        # Submit button with navigation
        if st.button("Submit"):
            # Fields from previous pages that need to be checked
            required_fields_from_other_pages = [
                "gender", "age", "race", "marital_status", "alcohol", "smoke",
                "sleep_disorder", "general_health_condition", "depression",
                "sleep_time", "sedentary_minutes"
            ]
            
            # Check if all required fields are filled
            missing_fields = [field for field in required_fields_from_other_pages if field not in user_data or user_data[field] is None]

            if not missing_fields:
                # If no fields are missing, proceed to prediction
                st.success("Information submitted! Redirecting to prediction.")
                st.session_state["current_page"] = "prediction"
                st.session_state.S = 0  # Set `S` to 0 to skip the sidebar update
                st.rerun()
            else:
                # Notify user which fields are missing
                st.error(f"Please fill out the following fields on the previous pages: {', '.join(missing_fields)}")

    with col2:
        st_lottie(
            lottie_health,
            speed=1,
            reverse=False,
            loop=True,
            quality="high",
            height=300,  # Adjust height
            width=400,   # Adjust width
            key="health_animation"
        )
        st.write("")  # Space between form and animation

if __name__ == "__main__":
    health()
