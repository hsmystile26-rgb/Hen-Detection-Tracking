import streamlit as st
import requests

API_URL = "https://hen-detection-tracking.onrender.com/predict"

st.set_page_config("Hen Detection System")

st.title("🐔 Hen Detection & Tracking System")

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi"])

if uploaded_file:
    if st.button("Run Detection"):
        files = {"file": uploaded_file}
        response = requests.post(API_URL, files=files)

        if response.ok:
            st.success("Detection completed")
            st.json(response.json())
        else:
            st.error("API error")
