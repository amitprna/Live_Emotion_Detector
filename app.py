import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration
import av
import threading
import cv2
from deepface import DeepFace

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
#         faceCascade = cv2.CascadeClassifier('harcascade_frontalface_default.xml')
#         result = DeepFace.analyze(frame,actions= ['dominant_emotion'])
    
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = faceCascade.detectMultiScale(gray,1.1,4)

#         for (x,y,w,h) in faces:
#             cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0), 2)
        
#         font = cv2.FONT_HERSHEY_SIMPLEX
    
#         cv2.putText(
#         frame,
#         result['dominant_emotion'],
#         (50,50),
#         font, 3,
#         (255,255,128),
#         2,
#         cv2.LINE_4
#         );
    

#         cv2.imshow('Video',frame)
    
#         if cv2.waitkey(2) & 0xFF == ord('q'):
#             break
        
#         cap.release()
#         cv2.destroyAllWindows()
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
