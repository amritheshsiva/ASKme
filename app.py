import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Function to extract text from a TXT file
def extract_text_from_txt(file):
    try:
        return file.read().decode("utf-8")  # Decode bytes to string
    except Exception as e:
        raise e

# Function to generate content using Gemini
def generate_gemini_content(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.title("ASKme")
uploaded_file = st.file_uploader("Upload TXT file", type="txt")

if uploaded_file:
    # Extract text from TXT file
    text = extract_text_from_txt(uploaded_file)

    # Show a portion of the extracted text
    st.markdown("## Extracted Text:")
    st.write(text[:1000])  # Display first 1000 characters of the extracted text for reference

    # Add a text input for questions
    st.markdown("## Ask a Question:")
    user_question = st.text_input("Enter your question here")

    if user_question:
        # Create a prompt for Gemini
        question_prompt = f"You are a helpful assistant. Based on the following text, answer the question.\n\nResume Text: {text}\n\nQuestion: {user_question}\nAnswer:"

        # Get the answer from Gemini
        answer = generate_gemini_content(question_prompt)

        # Display the answer
        st.markdown("## Answer:")
        st.write(answer)
