def extract_skills(resume_text):
    known_skills = [
        'python', 'sql', 'mysql', 'html', 'css', 'javascript', 'java',
        'machine learning', 'deep learning', 'data analysis', 'pandas',
        'flask', 'django', 'git', 'mongodb', 'react', 'web development',
        'communication', 'ai', 'nlp', 'cyber security', 'full stack development',
        'docker', 'kubernetes', 'devops', 'linux', 'networking'
    ]
    resume_text = resume_text.lower()
    return [skill for skill in known_skills if skill in resume_text]


