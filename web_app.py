import streamlit as st
import os

st.set_page_config(page_title="Hen Detection System", layout="centered")

st.title("🐔 Hen Detection & Tracking System")
st.write("Upload a video and click the button to run detection.")

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi"])

if uploaded_file:
    with open("input_video.mp4", "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Run Detection"):
        st.info("Processing... please wait")
        
        # Run your main detection script
        st.warning("Detection engine runs locally on the host machine.")


        if os.path.exists("output.avi"):
            st.success("Processing complete!")
            st.video("output.avi")
        else:
            st.error("Output video not found.")
