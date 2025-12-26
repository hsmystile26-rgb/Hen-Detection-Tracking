import streamlit as st
import requests

st.set_page_config(page_title="Hen Detection System", layout="centered")

st.title("🐔 Hen Detection & Tracking System")

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi"])

if uploaded_file is not None:
    st.video(uploaded_file)

    if st.button("Run Detection"):
        st.info("Sending video to AI server...")

        files = {"file": uploaded_file.getvalue()}

        response = requests.post(
            "http://192.168.1.8:5000/process",
            files=files
        )

        if response.status_code == 200:
            with open("result.avi", "wb") as f:
                f.write(response.content)

            st.success("Done!")
            st.video("result.avi")
        else:
            st.error("Server error. Is your AI server running?")
