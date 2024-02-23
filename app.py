##loading all env variables
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai



genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# Function to load gemeini model and get responses

model= genai.GenerativeModel('gemini-pro')
def get_gemini_response(question):
    response= model.generate_content(question)
    return response.text

# streamlit App
st.set_page_config(page_title="Q & A Demo")
st.header("Gemini LLM Application")

input= st.text_input("Input your text prompt", key="input")
submit= st.button("Ask the question")
if submit:
    response= get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)