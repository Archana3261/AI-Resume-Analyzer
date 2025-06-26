
from flask import Flask, render_template, request
from resume_parser import extract_text_from_pdf
from skill_matcher import extract_skills
from job_roles import job_roles
from course_recommender import suggest_courses
import os
import pyttsx3
import threading

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Background voice thread

def speak_result(score, matched, missing):
    engine = pyttsx3.init()
    message = f"Your resume matches {score} percent. You matched {len(matched)} skills and missed {len(missing)} important ones."
    engine.say(message)
    engine.runAndWait()

def speak_in_background(score, matched, missing):
    thread = threading.Thread(target=speak_result, args=(score, matched, missing))
    thread.start()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    skills = []
    suggestions = {}

    if request.method == 'POST':
        role = request.form['role']
        custom_skills = request.form.get('custom_skills', '')
        custom_role_name = request.form.get('custom_role_name', 'Custom Role')
        file = request.files['resume']

        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            resume_text = extract_text_from_pdf(file_path)
            skills = extract_skills(resume_text)

            if role == "custom":
                required = [skill.strip().lower() for skill in custom_skills.split(',') if skill.strip()]
            else:
                required = job_roles[role]

            matched = list(set(skills) & set(required))
            missing = list(set(required) - set(skills))
            score = int((len(matched) / len(required)) * 100) if required else 0

            suggestions = suggest_courses(missing)

            result = {
                'role': custom_role_name if role == "custom" else role.title(),
                'matched': matched,
                'missing': missing,
                'score': score
            }

            # Run voice in background
            speak_in_background(score, matched, missing)

    return render_template('index.html', roles=job_roles.keys(), result=result, skills=skills, suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True)
