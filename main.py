import streamlit as st
import PyPDF2
import io
import os
import google.genai as genai
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini with the new library
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("⚠️ API key not found. Please ensure .env file exists with GOOGLE_API_KEY.")
    st.stop()

client = genai.Client(api_key=GOOGLE_API_KEY)

st.set_page_config(page_title="AI Resume Critiquer", page_icon="📝", layout="centered")

st.title("📝 AI Resume Critiquer")
st.markdown("Upload your resume in PDF or TXT format and get AI-powered feedback to improve it.")

uploaded_file = st.file_uploader("Choose your resume", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you're applying for (optional)")

analyze = st.button("🔍 Analyze Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("❌ The uploaded file is empty. Please upload a valid resume.")
            st.stop()

        prompt = f"""
        You are an expert career coach and HR professional. Please analyze this resume{f' for the position of {job_role}' if job_role else ''} and provide detailed constructive feedback.

        Provide your analysis in this EXACT format:

        📊 **Overall Assessment**
        (Provide a brief summary of the resume's overall strength)

        ✅ **Strengths**
        (List key strengths of this resume)

        ⚠️ **Areas for Improvement**
        (List specific areas that need improvement)

        💡 **Specific Recommendations for Improvement**
        (List actionable recommendations)

        🏆 **Final Verdict**
        (One sentence summary of whether this resume is competitive{f' for {job_role}' if job_role else ''})

        Resume content:
        {file_content}
        """

        with st.spinner("🔄 Analyzing resume... This may take a few seconds."):
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            feedback = response.text

        st.success("✅ Resume analyzed successfully!")
        st.markdown("---")
        st.markdown(feedback)
        st.markdown("---")

        st.download_button(
            label="📥 Download analysis as text file",
            data=feedback,
            file_name="resume_analysis.txt",
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")
        st.info("Please verify that your API key is correct and you have an internet connection.")
