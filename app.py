import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration
import av
import threading

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

st.set_page_config(page_title="Emotion Detection", page_icon="🤖")
st.header('Scanning live feed.....')


    class VideoProcessor(VideoProcessorBase):
        def __init__(self):
            self.model_lock = threading.Lock()
            self.style = style_list[0]

        def update_style(self, new_style):
            if self.style != new_style:
                with self.model_lock:
                    self.style = new_style

        def recv(self, frame):
            # img = frame.to_ndarray(format="bgr24")
            img = frame.to_image()
            if self.style == style_list[1]:
                img = img.convert("L")

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

    if ctx.video_processor:
        ctx.video_transformer.update_style(style_selection)
