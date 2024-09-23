import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def process_uploaded_file(file):
    try:
        file_content = file.read().decode("utf-8")
        return file_content
    except Exception as e:
        st.error("Error while reading the file: {}".format(e))
        return None
def fetch_gemini_response(input_prompt):
    ai_model = genai.GenerativeModel("gemini-pro")
    ai_output = ai_model.generate_content(input_prompt)
    return ai_output.text

# Streamlit UI Components
st.header("ASKme - AI-Powered Assistant")

# File upload option
uploaded_file = st.file_uploader("Choose a text file", type=["txt"])

if uploaded_file:
    file_text = process_uploaded_file(uploaded_file)

    if file_text:
        st.subheader("Preview of the Uploaded File:")
        st.text_area("File Content", value=file_text[:1000], height=200)

        st.subheader("Ask Your Question")
        user_query = st.text_input("Enter your query here:")

        if user_query:
            prompt_to_send = f"Analyze the following text and answer the question:\n\nText: {file_text}\n\nQuestion: {user_query}\nAnswer:"
            ai_answer = fetch_gemini_response(prompt_to_send)

            st.subheader("Response:")
            st.write(ai_answer)
