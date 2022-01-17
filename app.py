import cv2
import streamlit as st

st.title('Emotion Detection')

run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
cam = cv2.VideoCapture(0)

while run:
  ret, frame = cam.read()
  FRAME_WINDOW.image(frame)
else:
  st.write('stopped')
