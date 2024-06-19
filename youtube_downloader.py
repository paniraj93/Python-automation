import streamlit as st
from pytube import YouTube
import os
#streamlit run e:/python_automation/youtube_downloader.py
# Function to download YouTube video
def download_youtube_video(url, resolution, download_folder):
    try:
        yt = YouTube(url)
        # Filter streams by resolution
        stream = yt.streams.filter(res=resolution).first()
        if stream:
            # Download the video
            stream.download(output_path=download_folder)
            return f"Downloaded: {yt.title} in {resolution} resolution."
        else:
            return "Selected resolution not available. Try a different resolution."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit app
st.title("YouTube Video Downloader")

# Input for YouTube video URL
video_url = st.text_input("Enter YouTube video URL:")

# Dropdown for resolution selection
resolutions = ["144p", "240p", "360p", "480p", "720p", "1080p"]
selected_resolution = st.selectbox("Select resolution:", resolutions)

# Input for download folder
download_folder = st.text_input("Enter download folder path:", value=os.getcwd())

if st.button("Download Video"):
    if video_url and selected_resolution and download_folder:
        message = download_youtube_video(video_url, selected_resolution, download_folder)
        st.success(message)
    else:
        st.error("Please fill in all fields.")
