# 📝 AI Resume Critiquer

AI-powered resume analyzer using **Google Gemini**. Upload your PDF resume and get instant feedback on strengths, weaknesses, and improvements.

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange.svg)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📋 Table of Contents

- [About The Project](#-about-the-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [How It Works](#-how-it-works)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Dependencies](#-dependencies)
- [Security](#-security)
- [Author](#-author)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 🌟 About The Project

**AI Resume Critiquer** is a smart resume analysis tool that leverages **Google Gemini AI** to provide professional, actionable feedback on your resume.

Whether you're a job seeker looking to improve your resume, a career coach helping clients, or a recruiter screening candidates, this tool gives you instant, structured feedback.

**Key Insight:** Built with commercial AI APIs (Google Gemini) to demonstrate how quickly AI can be integrated into real-world applications.

---

## ✨ Features

| Feature | Description |
| :--- | :--- |
| 📄 **Multi-Format Support** | Upload PDF or TXT resumes |
| 🤖 **AI Analysis** | Powered by Google Gemini 2.0 Flash |
| 📊 **Structured Feedback** | Overall Assessment, Strengths, Weaknesses, Recommendations, Final Verdict |
| 💾 **Export Results** | Download analysis as .txt file |
| 🎨 **Clean UI** | Built with Streamlit for a smooth user experience |
| 🔒 **Secure** | API keys managed via `.env` file |

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| Language | Python 3.13+ |
| UI Framework | Streamlit |
| PDF Processing | PyPDF2 |
| AI API | Google Gemini (Google Generative AI) |
| Environment | python-dotenv |

---

## 🧠 How It Works

1. **User Uploads Resume**: Upload a PDF or TXT file.
2. **Text Extraction**: The app extracts all text from the file.
3. **AI Processing**: The resume content is sent to Google Gemini with a structured prompt.
4. **Analysis Generation**: Gemini returns detailed feedback in a consistent format.
5. **Display Results**: The feedback is displayed in a clean, organized layout.
6. **Export Option**: User can download the analysis as a text file.

---

## 🚀 Quick Start

### 1. Clone the Repository
```
git clone https://github.com/RodwanRamzi/resume-critiquer.git
cd resume-critiquer
```

### 2. Create a Virtual Environment
Windows:
```python
python -m venv .venv
.venv\Scripts\activate
```
Linux/Mac:
```python
python -m venv .venv
source .venv/bin/activate
```

## 3. Install Dependencies
```python
pip install -r requirements.txt
```

## 4. Set Up Your Gemini API Key
Step 1: Get your free API key from Google AI Studio.

Step 2: Create a .env file in the project root:
```.env
GOOGLE_API_KEY=your_api_key_here
```

Step 3: Ensure .env is in .gitignore (it already should be).

## 5. Run the Application
```python
streamlit run main.py
The app will open at: http://localhost:8502
```

📂 Project Structure
```
resume-critiquer/
├── main.py                 # Main application file
├── requirements.txt        # Python dependencies
├── .env                    # API key (DO NOT commit)
├── .gitignore              # Files to ignore
└── README.md              # Project documentation
```

📦 Dependencies
```
streamlit
PyPDF2
python-dotenv
google-generativeai
```
Install all at once:
```
pip install -r requirements.txt
```

## 🔒 Security
⚠️ IMPORTANT: Never commit your .env file to version control.

.env contains your API key – keep it private.

Add .env to .gitignore (already included).

Use environment variables in production deployments.

## 👨‍💻 Author
Rodwan Ramzi

[![Github](https://img.shields.io/badge/GitHub-RodwanRamzi-181717?style=flat&logo=github)]
[![Linkedin](https://img.shields.io/badge/LinkedIn-RodwanRamzi-0A66C2?style=flat&logo=linkedin)]
[![Email](https://img.shields.io/badge/Email-rothwanramzi@gmail.com-EA4335?style=flat&logo=gmail)]

Hybrid Software Engineer | C++, OpenGL & GPU Rendering | AI & Reinforcement Learning Systems

## 📜 License
Distributed under the MIT License. See LICENSE for more information.

## Acknowledgments
Google Gemini AI – For providing accessible, powerful AI models.

Streamlit – For making it easy to build beautiful data apps.

# Built by Rodwan Ramzi
