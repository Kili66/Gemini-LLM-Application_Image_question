##loading all env variables
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# Function to load gemeini model and get responses

model= genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(input, image):
   
    
    if input!="":
        response= model.generate_content([input, image])
    else:
        response= model.generate_content(image)
    return response.text
# streamlit App
st.set_page_config(page_title="Q & A Demo")
st.header("Gemini LLM Application")

input= st.text_input("Input your prompt", key="input")
#submit= st.button("Ask the question")
upload_file= st.file_uploader("upload your image", type=["jpg", "jpeg","png"])
image=""

if upload_file is not None:
    image= Image.open(upload_file)
    st.image(image, caption="Uploaded file", use_column_width=True)

submit= st.button("Tell me about the image")

if submit:
    response= get_gemini_response(input, image)
    st.subheader("The response is")
    st.write(response)
    