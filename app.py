import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration
import av
import threading

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

st.set_page_config(page_title="Emotion Detector", page_icon="🤖")
st.title('Processing live feed.......')


class VideoProcessor(VideoProcessorBase):
    def __init__(self):
        self.model_lock = threading.Lock()
        self.style = 'color'

    def update_style(self, new_style):
        if self.style != new_style:
            with self.model_lock:
                self.style = new_style

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        # image processing code here
        # return av.VideoFrame.from_ndarray(img, format="bgr24")
        return av.VideoFrame.from_image(img)

ctx = webrtc_streamer(
        key="example",
        video_processor_factory=VideoProcessor,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={
            "video": True,
            "audio": False
        }
    )
