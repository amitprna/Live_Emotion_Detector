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

    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        image = frame.to_ndarray(format="bgr24")
        faceCascade = cv2.CascadeClassifier('harcascade_frontalface_default.xml')
        result = DeepFace.analyze(image,actions= ['emotion'])
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray,1.1,4)

        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w, y+h),(0,255,0), 2)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
    
        cv2.putText(imafe,result['dominant_emotion'],(50,50),font, 3,(255,255,128),2,cv2.LINE_4); 
        
    
#         if cv2.waitkey(2) & 0xFF == ord('q'):
#             break
        
#         cap.release()
#         cv2.destroyAllWindows()
        return av.VideoFrame.from_ndarray(annotated_image, format="bgr24")

ctx = webrtc_streamer(
        key="example",
        video_processor_factory=VideoProcessor,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={
            "video": True,
            "audio": False
        }
    )
