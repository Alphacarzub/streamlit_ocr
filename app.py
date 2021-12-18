%%writefile app.py
import streamlit as st
import cv2
import pytesseract
from PIL import Image # python imaging library to open images (For streamlit)
# Streamlit does not use cv2.imread()!
st.title("Optical Character Recognition (OCR) :")
st.text('Upload the image :')

# To ask for a file from user and then open do the following:-
uploaded_file = st.file_uploader("choose an image :",type=['jpg','png','jpeg'])  # We can give all formats.
if uploaded_file is not None: # if there is some file uploaded, then do the following - 
    img  = Image.open(uploaded_file) # reads the file uploaded(similiar to cv2.imread)
if st.button('Predict'):
    st.write("result :")
    info = pytesseract.image_to_string(img)# Take the file saved in img
    # OCR is applied using pytesseract
    st.title(info)
