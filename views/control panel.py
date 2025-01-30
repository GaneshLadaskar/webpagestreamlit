import streamlit as st
import requests

# Set Streamlit page config (must be the first Streamlit command)
#st.set_page_config(page_title="ESP32-CAM Control", layout="wide")

# ESP32-CAM Stream & Control URLs
ESP32_STREAM_URL = "http://192.168.54.183:81/stream"  # Update with your ESP32-CAM stream URL
ESP32_CONTROL_URL = "http://192.168.54.183"  # Base URL for control commands

# Streamlit app title
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 2em;
            color: #4CAF50;
        }
        .header {
            text-align: center;
            font-size: 1.5em;
            margin-top: 20px;
        }
        .button-container {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 10px;
        }
        .stButton>button {
            width: 120px;
            height: 50px;
            font-size: 16px;
            font-weight: bold;
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">ESP32-CAM Control</p>', unsafe_allow_html=True)

# Display the live stream
st.markdown('<p class="header">Live Stream</p>', unsafe_allow_html=True)
st.image(ESP32_STREAM_URL, use_column_width=True)

# Start Button for All Controls
st.markdown('<p class="header">Start Control</p>', unsafe_allow_html=True)
start_control = st.button("▶ Start Control")

if start_control:
    st.session_state["control_enabled"] = True

# Motor Control Buttons
st.markdown('<p class="header">Motor Control (WASD)</p>', unsafe_allow_html=True)

if st.session_state.get("control_enabled", False):
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button("W ⬆ Forward"):
            requests.get(f"{ESP32_CONTROL_URL}/forward")
        if st.button("S ⬇ Backward"):
            requests.get(f"{ESP32_CONTROL_URL}/backward")

    with col2:
        if st.button("⏹ Stop"):
            requests.get(f"{ESP32_CONTROL_URL}/stop")

    with col3:
        if st.button("A ⬅ Left"):
            requests.get(f"{ESP32_CONTROL_URL}/left")
        if st.button("D ➡ Right"):
            requests.get(f"{ESP32_CONTROL_URL}/right")

# Pan-Tilt controls
st.markdown('<p class="header">Pan-Tilt Control (IKJL)</p>', unsafe_allow_html=True)

if st.session_state.get("control_enabled", False):
    col4, col5 = st.columns(2)

    with col4:
        if st.button("J ⬅ Pan Left"):
            requests.get(f"{ESP32_CONTROL_URL}/panleft")
        if st.button("L ➡ Pan Right"):
            requests.get(f"{ESP32_CONTROL_URL}/panright")

    with col5:
        if st.button("I ⬆ Tilt Up"):
            requests.get(f"{ESP32_CONTROL_URL}/tiltup")
        if st.button("K ⬇ Tilt Down"):
            requests.get(f"{ESP32_CONTROL_URL}/tiltdown")

