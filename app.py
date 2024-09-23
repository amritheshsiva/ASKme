import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
def extract_text_from_txt(file):
    try:
        return file.read().decode("utf-8")  
    except Exception as e:
        raise e
def generate_gemini_content(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text
st.title("ASKme")
uploaded_file = st.file_uploader("Upload TXT file", type="txt")
if uploaded_file:
    text = extract_text_from_txt(uploaded_file)
    st.markdown("## Extracted Text:")
    st.write(text[:1000]) 
    st.markdown("## Ask a Question:")
    user_question = st.text_input("Enter your question here")
    if user_question:
        question_prompt = f"Based on the following text, answer the question.\n\nResume Text: {text}\n\nQuestion: {user_question}\nAnswer:"
        answer = generate_gemini_content(question_prompt)
        st.markdown("## Answer:")
        st.write(answer)
