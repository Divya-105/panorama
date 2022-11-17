# import streamlit as st
# # import cv2
# # import streamlit as st

# st.title('Panorama Images')
# st.header('Upload a video and detect lane')

# st.header('Input images')

# f = st.file_uploader("Upload file")
# if f is not None:
#     file_details = {"FileName":f.name,"FileType":f.type}
#     st.write(file_details)
    

import io
import os
import tempfile

# import cv2
# import patoolib
import streamlit as st
# import streamlit as st
from PIL import Image


# st.title('Lane Detection')
# st.header('Upload a video and detect lane')

st.header('Input images')

# f = st.file_uploader("Upload file")
# if f is not None:
#     file_details = {"FileName":f.name,"FileType":f.type}
#     st.write(file_details)
    
# uploaded_files = st.file_uploader("Veuillez charger une image",type=['jpg','jpeg','png'],help="Charger une image au format jpg,jpeg,png", accept_multiple_files=True,)

# for uploaded_file in uploaded_files:
#      bytes_data = uploaded_file.read()
#      image = Image.open(io.BytesIO(bytes_data))
#      st.write("filename:", uploaded_file.name)
#      st.image(image)
     
# for f in uploaded_files:
#     with open(f.name,"wb") as ff: 
#         ff.write(f.getbuffer())         
#     st.success("Saved File")
#     tfile = tempfile.NamedTemporaryFile(delete=False) 
#     tfile.write(f.read())
def save_uploadedfile(uploadedfile):
    with open(os.path.join('Panorama22', uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
        return st.success("Saved File:{} to Panorama22".format(uploadedfile.name))

st.title("Upload images")
st.text("Upload desired images and save in the directory")
uploadedfiles = st.file_uploader("Veuillez charger une image",type=['jpg','jpeg','png'],help="Charger une image au format jpg,jpeg,png", accept_multiple_files=True,)
for file in uploadedfiles:
    if uploadedfiles is not None:
        save_uploadedfile(file)

# patoolib.extract_archive("panorama.rar", outdir="panorama.rar")

# from main import panorama

# panorama();
# st.image('Stitched_Panorama.png');
