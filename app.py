import streamlit as st
import cv2
import tempfile
import os

st.set_page_config(page_title="Hen Detection System")

st.title("🐔 Hen Detection & Tracking System")

video_file = st.file_uploader("Upload Hen Video", type=["mp4", "avi"])

if video_file:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())

    st.success("Video uploaded successfully")

    cap = cv2.VideoCapture(tfile.name)

    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 👉 Here you will call your detection pipeline later
        stframe.image(frame, channels="BGR")

    cap.release()
