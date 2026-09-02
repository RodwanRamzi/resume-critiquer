import streamlit as st
import PyPDF2
import io
import os
import google.genai as genai
from dotenv import load_dotenv

load_dotenv()

# تهيئة Gemini بالمكتبة الجديدة
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("⚠️ لم يتم العثور على مفتاح API. تأكد من وجود ملف .env مع GOOGLE_API_KEY.")
    st.stop()

client = genai.Client(api_key=GOOGLE_API_KEY)

st.set_page_config(page_title="AI Resume Critiquer", page_icon="📝", layout="centered")

st.title("📝 AI Resume Critiquer")
st.markdown("قم بتحميل سيرتك الذاتية بصيغة PDF واحصل على تحليل ذكي وتغذية راجعة لتحسينها.")

uploaded_file = st.file_uploader("اختر سيرتك الذاتية", type=["pdf", "txt"])
job_role = st.text_input("أدخل الوظيفة التي تتقدم لها (اختياري)")

analyze = st.button("🔍 تحليل السيرة الذاتية")

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
            st.error("❌ الملف الذي رفعته فارغ. يرجى رفع سيرة ذاتية صالحة.")
            st.stop()

        job_text = f" for {job_role}" if job_role else ""
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

        with st.spinner("🔄 جاري تحليل السيرة الذاتية... قد يستغرق ذلك بضع ثوانٍ."):
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            feedback = response.text

        st.success("✅ تم تحليل السيرة الذاتية بنجاح!")
        st.markdown("---")
        st.markdown(feedback)
        st.markdown("---")

        st.download_button(
            label="📥 تحميل التحليل كملف نصي",
            data=feedback,
            file_name="resume_analysis.txt",
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"❌ حدث خطأ: {str(e)}")
        st.info("تأكد من أن مفتاح API صحيح وأن لديك اتصال بالإنترنت.")