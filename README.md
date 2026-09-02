# 📝 AI Resume Critiquer

AI-powered resume analyzer using **Google Gemini**. Upload your PDF resume and get instant feedback on strengths, weaknesses, and improvements.

---

## ✨ Features

- 📄 PDF & TXT upload
- 🤖 Gemini AI analysis
- 📊 Structured feedback (Strengths, Weaknesses, Recommendations)
- 💾 Download results as .txt
- 🎨 Clean Streamlit UI

---

## 🛠️ Tech Stack

- Python 3.13+
- Streamlit
- PyPDF2
- Google Generative AI (Gemini)
- python-dotenv

---

## 🚀 Quick Start

### 1. Clone
git clone https://github.com/your-username/resume-critiquer.git
cd resume-critiquer

### 2. Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate # Linux/Mac

### 3. Install
pip install -r requirements.txt

### 4. Add your Gemini API Key
Create .env file:
GOOGLE_API_KEY=your_api_key_here
Get your free key: Google AI Studio

### 5. Run
streamlit run main.py

### 📂 Project Structure
resume-critiquer/
├── main.py
├── requirements.txt
├── .env (DO NOT commit)
├── .gitignore
└── README.md

# 📦 Dependencies
streamlit
PyPDF2
python-dotenv
google-generativeai

🔒 Security
Never commit .env to version control.

Add .env to .gitignore.

👨‍💻 Author
Rodwan Ramzi
[GitHub](https://github.com/RodwanRamzi) | [LinkedIn](https://www.linkedin.com/in/rodwan-ramzi-273523372/)

📜 License
MIT

Built by Rodwan Ramzi

