import streamlit as st
from streamlit_option_menu import option_menu
from views import personal, lifestyle, health, predict
import json
# import requests  # pip install requests
from streamlit_lottie import st_lottie
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
lottie_home = load_lottiefile("./assets/home.json")
# --- LOGO DISPLAYED ON ALL PAGES ---

with st.sidebar:
    st.markdown("<div style='text-align: center; margin-top: -10px;'>", unsafe_allow_html=True)
    st.image("assets/stroke.webp", width=60)
    st.markdown("</div>", unsafe_allow_html=True)

# # Session state variables to store user input

# Initialize `S` in session state
if "S" not in st.session_state:
    st.session_state.S = 1
# Map page names to their corresponding indices
page_indices = {
    "home": 0,
    "personal_information": 1,
    "lifestyle_habits": 2,
    "health_metrics": 3,
    "prediction": 4
}

# Get the current page and determine the corresponding index
current_page = st.session_state.get("current_page", "home")
default_index = page_indices.get(current_page, 0)

# --- NAVIGATION SETUP ---
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "Personal Information", "Lifestyle Habits", "Health Metrics", "Prediction"],
        icons=["house", "person-circle", "activity", "heart-pulse", "bar-chart"],
        menu_icon="cast",
        default_index=default_index,
        styles={
            "container": {"padding": "5px", "background-color": "#2c2f33"},
            "icon": {"color": "#ffcc00", "font-size": "25px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "5px",
                "--hover-color": "#37474f",
                "color": "#ffffff",
            },
            "nav-link-selected": {"background-color": "#ff914d", "color": "#ffffff"},
        }
    )
    
    if selected!=st.session_state.get("current_page", "home").replace("_", " ").title():
        st.session_state["current_page"] = selected.lower().replace(" ", "_")
        
        default_index = page_indices.get(selected, 0)
        st.rerun()


    # Update `S` only when sidebar is used directly
    if st.session_state.S == 1:
        st.session_state["current_page"] = selected.lower().replace(" ", "_")
    else:
        selected = st.session_state["current_page"].replace("_", " ").title()


    st.session_state.S = 1


# --- PAGE CONTENT FUNCTIONS ---
def home():
    st.title("Welcome to the Brain Stroke Prediction App")

    # Use columns to place text on the left and the animation on the right
    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.subheader("Your Health, Our Priority")
        st.markdown(
            """
            Understanding your risk factors is the first step toward a healthier life. 
            Through this app, we use personal information, lifestyle habits, and health metrics 
            to provide insights into your stroke risk.
            """
        )
        st.markdown(
            """
            *“The greatest wealth is health.”*  
            — Virgil
            """
        )
        st.write("Let’s get started by exploring your personal information.")

    with col2:
        st_lottie(
            lottie_home,
            speed=1,
            reverse=False,
            loop=True,
            quality="high",
            height=280,  # Further reduce the height for better fit
            width=280,   # Further reduce the width for better fit
            key="home_animation"
        )

page_functions = {
    "home": home,
    "personal_information": personal.personal,
    "lifestyle_habits": lifestyle.lifestyle,
    "health_metrics": health.health,
    "prediction": predict.predict
}

# --- NAVIGATION LOGIC ---
def navigate_page():
    current_page = st.session_state.get("current_page", "home")
    
    if current_page in page_functions:
        page_functions[current_page]()
    else:
        home()

navigate_page()
