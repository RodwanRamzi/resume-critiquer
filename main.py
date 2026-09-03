import streamlit as st
import google.genai as genai  # New import
from google.genai import types  # Needed for safety settings
from PyPDF2 import PdfReader
import os
from dotenv import load_dotenv
import io

# --- Page Config ---
st.set_page_config(page_title="AI Job Co-Pilot", page_icon="🚀", layout="wide")

# --- Load API Key ---
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("⚠️ Please set your GOOGLE_API_KEY in the .env file!")
    st.stop()

# --- NEW: Initialize the Gemini Client (No configure needed) ---
client = genai.Client(api_key=API_KEY)
MODEL_NAME = "gemini-3.6-flash"  

# --- Helper Functions ---
def extract_text_from_pdf(uploaded_file):
    """Extracts text from a PDF file."""
    try:
        reader = PdfReader(io.BytesIO(uploaded_file.getvalue()))
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return ""

def run_co_pilot(resume_text, job_description):
    """Sends the data to the NEW Gemini SDK and returns the analysis."""
    prompt = f"""
    You are an expert Senior Career Coach, Talent Acquisition Specialist, and Resume Writer.

    **My Resume:** 
    {resume_text}

    **The Job Description I am targeting:**
    {job_description}

    Your task is to tailor my application perfectly for this specific role. 
    Please provide your output in the following strict Markdown format:

    ### 🔍 1. Keyword Gap Analysis
    List the **Hard Skills** and **Soft Skills** mentioned in the Job Description that are MISSING from my Resume. 
    If I have all the skills, say "Great match, no major gaps found!"

    ### ✍️ 2. Rewritten Resume Bullet Points
    Rewrite my existing experience/summary into **5-6 powerful bullet points**.
    - Must use the exact keywords from the Job Description.
    - Must focus on achievements and quantifiable results.
    - Must be tailored specifically to the responsibilities listed in the JD.

    ### 📝 3. Tailored Cover Letter
    Write a professional 3-paragraph cover letter addressed to the hiring manager.
    - **Paragraph 1:** Express interest and state the role.
    - **Paragraph 2:** Connect my specific skills to the company's needs (using keywords).
    - **Paragraph 3:** Closing statement.
    """

    # --- NEW: The correct way to call Gemini in the new SDK ---
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.7,
        )
    )
    return response.text

# --- UI Layout ---
st.title("🚀 AI Job Application Co-Pilot")
st.markdown("Paste a job description and upload your resume. Let AI tailor your application perfectly.")

# Create two columns for input
col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("📋 Job Description")
    job_description = st.text_area(
        "Paste the job description here", 
        height=250, 
        placeholder="Copy and paste the job description from LinkedIn, Indeed, etc."
    )
    
    st.subheader("📄 Your Resume")
    uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
    
    manual_resume = st.text_area(
        "Or paste your Resume text manually", 
        height=150, 
        placeholder="If PDF extraction fails, paste your resume text here."
    )

with col2:
    st.subheader("🎯 Tailored Results")
    output_placeholder = st.empty()

# --- The Magic Button ---
if st.button("✨ Generate Tailored Application", type="primary", use_container_width=True):
    resume_text = ""
    if uploaded_file:
        with st.spinner("📖 Extracting text from PDF..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            if not resume_text:
                st.warning("Could not extract text from PDF. Please paste resume manually.")
    
    if manual_resume:
        resume_text = manual_resume

    if not resume_text:
        st.error("❌ Please upload a PDF or paste your resume text.")
        st.stop()
        
    if not job_description or len(job_description) < 20:
        st.error("❌ Please paste a valid Job Description (at least 20 characters).")
        st.stop()

    with st.spinner("🧠 AI is analyzing the job and rewriting your resume... (takes 10-15 seconds)"):
        try:
            result = run_co_pilot(resume_text, job_description)
            
            with output_placeholder.container():
                st.markdown(result)
                
            st.download_button(
                label="💾 Download Full Analysis as .txt",
                data=result,
                file_name="tailored_application.txt",
                mime="text/plain"
            )
            
        except Exception as e:
            st.error(f"An error occurred with the AI: {e}")