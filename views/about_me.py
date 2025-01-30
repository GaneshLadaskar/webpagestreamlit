import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/me.jpg", width=230)

with col2:
    st.title("This is me", anchor=False)
    st.write(
        "Bored with Life."
    )
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Here is what I can do for you:")
        st.write(
            """
            1. Surveillance System Features:
            - Mobile Monitoring: Users can access live feeds and system controls from anywhere via smartphones or tablets.
            - Two-Way Communication: The companion bot acts as an intermediary, allowing users to speak with visitors or warn intruders remotely.
            - Companion Bot Mobility: A mobile bot can patrol areas, monitor blind spots, and follow commands for enhanced coverage.
            - Expandable Coverage: Easily scales to larger homes or business premises with additional bots or cameras.

            2.Peace of Mind and Convenience
            - Child and Pet Monitoring: Keeps an eye on vulnerable family members or pets, ensuring their safety.
            - Privacy Controls: Allows users to define secure zones or times when the system is deactivated for privacy.
            - Entertainment Features: Companion bots can play music, share updates, or engage users with interactive activities.

            """
        )
        st.write("[YouTube Channel >](https://youtu.be/9ki-8omvZ2o?si=J0kNNouGmJQpL6AQ)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


# --- FEATURES AND SPECIFICATIONS ---
st.write("\n")
st.subheader("Features and Specification", anchor=False)
st.write(
    """
    Features:
    1. Advanced Surveillance Capabilities
    2. Smart Companion Bot Integration
    3. AI-Powered Features
    4. Remote Accessibility
    6. Home Automation Integration
    7. User Privacy and Security

    Specifications:
    1. Cameras: 2mp resolution, wide-angle lens, 30–60 FPS, night vision support.
    2. Companion Bot: Compact design with wheels or legs, autonomous mobility, and obstacle sensors.
    3. Processor: AI-enabled processor (e.g., NVIDIA Jetson, Snapdragon).
    4. Storage: Expandable storage options (e.g., SD card, external hard drive, or cloud).
    5. Connectivity: Wi-Fi 6, Bluetooth 5.0, and optional 4G/5G for remote areas.
    6. Battery: Rechargeable, high-capacity battery (8–12 hours runtime per charge).
    7. Sensors: Motion, sound, temperature, and humidity sensors.

    """
)

# --- SOFTWARE  ---
st.write("\n")
st.subheader("Software used to build bot", anchor=False)
st.write(
    """
    - AI Algorithms: Advanced computer vision, facial recognition, and sound detection.
    - Mobile App: iOS/Android app for control and monitoringCloud Integration: Secure cloud services with subscription plans for backups.
    - OTA Updates: Regular firmware updates for new features and improvements.
    - Integration: Compatible with Alexa, Google Assistant, and Apple HomeKit.

    """
)