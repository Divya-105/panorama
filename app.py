import streamlit as st
# import cv2
# import streamlit as st

st.title('Panorama Images')
st.header('Upload a video and detect lane')

st.header('Input images')

f = st.file_uploader("Upload file")
if f is not None:
    file_details = {"FileName":f.name,"FileType":f.type}
    st.write(file_details)
    

