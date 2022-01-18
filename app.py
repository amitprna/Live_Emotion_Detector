import cv2
from deepface import DeepFace
import streamlit as st
from streamlit_webrtc import  VideoProcessorBase, webrtc_streamer,RTCConfiguration

#inp_image = st.camera_input('say cheese.......')
RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

class VideoTransformer(VideoProcessorBase):
    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        img = frame.to_ndarray(format="bgr24")
        predictions = DeepFace.analyze(img)
        faceCascade = cv2.CascadeClassifier('harcascade_frontalface_default.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray,1.1,4)

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX 
        cv2.putText( img, predictions['dominant_emotion'], (0,50), font, 1, (255,255,128), 2, cv2.LINE_4 ); 
        cv2.putText( img, str(predictions['age']), (10,50), font, 1, (255,255,128), 2, cv2.LINE_AA ); 
        cv2.putText( img, predictions['gender'], (20,50), font, 1, (255,255,128), 2, cv2.LINE_4 );
        
        return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(key="example",rtc_configuration=RTC_CONFIGURATION, video_transformer_factory=VideoTransformer)
 
    

