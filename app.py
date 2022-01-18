import cv2
from deepface import DeepFace
import streamlit as st

inp_image = st.camera_input('say cheese.......')

if inp_image:
    st.image(inp_image)
    predictions = DeepFace.analyze(inp_image)
    faceCascade = cv2.CascadeClassifier('harcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0), 2)
    font = cv2.FONT_HERSHEY_SIMPLEX 
    cv2.putText( img, predictions['dominant_emotion'], (0,50), font, 1, (255,255,128), 2, cv2.LINE_4 ); 
    cv2.putText( img, str(predictions['age']), (10,50), font, 1, (255,255,128), 2, cv2.LINE_AA ); 
    cv2.putText( img, predictions['gender'], (20,50), font, 1, (255,255,128), 2, cv2.LINE_4 );
    st.image(inp_image)
else:
    st.write('No image for processing')
 
    

