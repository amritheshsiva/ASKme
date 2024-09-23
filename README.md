# AI Text-based Q&A Bot

## Introduction
This project is an AI-powered question and answer bot that allows users to upload a `.txt` file and ask questions about its content. The app uses advanced AI models like Google Gemini API to provide insightful answers based on the uploaded text file.

## Tech Stacks
- **Python**: Core programming language for building the app.
- **Pathway LLM**: Used as a language model for additional AI-based text processing.
- **Streamlit**: Web framework used for creating a simple and interactive user interface.
- **Google Gemini API**: AI models used for generating answers based on text content.
- **Docker**: Optional - For containerizing the application.
- **WSL (Windows Subsystem for Linux)**: Used for development in a Linux environment on Windows.

## Prerequisites
Before running this project, ensure you have the following installed on your local machine:
- Python
- pip
- Google Gemini API Key
- Streamlit
- (Optional) Docker for containerization

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/yourprojectname.git
cd yourprojectname
```
### 2.Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Set Up Environmental Variables
-Create a `.env` file in the root directory
```bash
touch .env
```
-Add your API Key
```bash
GOOGLE_API_KEY=your-google-gemini-api-key-here
```
### 5.Run the Application
```bash
streamlit run app.py
```
## Usage
#### 1.Upload a .txt file: Choose the text file you want to upload, and the app will display the content.
#### 2.Ask Questions: Enter a question in the input box, and the AI will generate a response based on the uploaded content.
#### 3. Get Answers: The response will be displayed below the input box.

## Demonstration

https://github.com/user-attachments/assets/d580f5e9-a391-426d-b77b-7b639f80f601

