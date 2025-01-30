import requests
import streamlit as st
from streamlit_lottie import st_lottie
import cv2
from keras.models import model_from_json
import numpy as np
from PIL import Image
import tempfile



# Disable TensorFlow warnings
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


# Streamlit UI

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon="🌟", layout="wide")

st.title("Surveillance System with Companion Bot 🔍")
st.markdown("This webpage detects facial emotions in a live webcam feed.")
about_page = st.Page(
    "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

project_1_page = st.Page(
    "views/sales_dashboard.py",
    title="Emotion Detection",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    "views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)
project_3_page = st.Page(
    "forms/contact.py",
    title="Contact Us",
    icon=":material/contact_mail:",
)
project_4_page = st.Page(
    "views/control panel.py",
    title="control panel",
    icon=":material/face:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_4_page,project_3_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/logo.jpg")
st.sidebar.markdown("This is a Companion bot 💕")
#st.balloons()
pg.run()




