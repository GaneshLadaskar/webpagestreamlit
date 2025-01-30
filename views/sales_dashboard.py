import streamlit as st
import cv2
from keras.models import model_from_json
import numpy as np
from PIL import Image
import tempfile

# Load the model
@st.cache_resource
def load_emotion_model():
    with open("facialemotionmodel.json", "r") as json_file:
        model_json = json_file.read()
    model = model_from_json(model_json)
    model.load_weights("facialemotionmodel.h5")
    return model

model = load_emotion_model()
labels = {0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy', 4: 'neutral', 5: 'sad', 6: 'surprise'}

# Load Haar Cascade for face detection
@st.cache_resource
def load_face_cascade():
    haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    return cv2.CascadeClassifier(haar_file)

face_cascade = load_face_cascade()

# Function to preprocess the input image
def extract_features(image):
    feature = np.array(image).reshape(1, 48, 48, 1)
    return feature / 255.0

# Streamlit UI
st.title("Facial Emotion Detection")
st.markdown("This section detects facial emotions in a live webcam feed.")

# Start webcam and display feed
run = st.checkbox("Start Webcam")
frame_window = st.image([])

if run:
    # URL of the ESP32-CAM stream (use the correct IP address and port)
    esp32_stream_url = "http://192.168.54.183:81/stream"  # Update with the ESP32 IP address
    cap = cv2.VideoCapture(esp32_stream_url)

    if not cap.isOpened():
        st.error("Failed to connect to ESP32-CAM stream.")
    
    while run:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to grab frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
            face_resized = cv2.resize(face, (48, 48))
            img = extract_features(face_resized)
            pred = model.predict(img)
            prediction_label = labels[pred.argmax()]

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, prediction_label, (x, y-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

        # Stream the processed frame to the browser
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_window.image(frame_rgb)

    cap.release()

else:
    st.info("Click the checkbox to start the webcam.")