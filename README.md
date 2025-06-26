# 💼 AI-Powered Resume Analyzer

A smart web application that analyzes your resume, compares your skills with job role requirements, provides a match score, recommends free courses for missing skills, and speaks out your result with voice feedback.

## 🚀 Features
- 📄 Upload PDF resume and extract skills automatically
- 🎯 Choose from predefined or custom job roles
- 📊 Resume match score based on required skills
- ✅ Matched and ❌ missing skills display
- 🎓 Free course recommendations
- 🗣 Voice feedback using pyttsx3
- 💻 Web interface built with Flask + HTML/CSS

## 🛠 Tech Stack
- **Frontend:** HTML, CSS
- **Backend:** Python, Flask
- **Libraries:** PyPDF2, pyttsx3, threading

## 📂 Folder Structure
```
resume_analyzer/
├── app.py
├── resume_parser.py
├── skill_matcher.py
├── job_roles.py
├── course_recommender.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── uploads/
```

## 🔧 Installation
1. Clone the repo
2. Install dependencies: `pip install flask pyttsx3 PyPDF2`
3. Run the app: `python app.py`
4. Visit `http://localhost:5000`

## ✨ Supported Job Roles
Full Stack Developer, ML Engineer, Data Analyst, UI/UX Designer, Cloud Engineer, and many more. Custom roles are also supported.

## 🔮 Future Scope
- Export result as PDF
- Add login & resume history
- Online hosting
- OCR support for image-based resumes

## 👩‍💻 Made By
**Archana Gopanaboina**  
B.Tech CSE (4th Year)  
Nalla Malla Reddy Engineering College
