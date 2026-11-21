

import fitz

def extract_resume_text(file_path):

    document = fitz.open(file_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


SKILLS = [
    "python",
    "java",
    "sql",
    "html",
    "css",
    "javascript",
    "fastapi",
    "flask",
    "django",
    "git",
    "docker",
    "machine learning",
    "communication",
    "problem solving"
]


def detect_skills(resume_text):

    text = resume_text.lower()

    found = []

    for skill in SKILLS:

        if skill in text:
            found.append(skill)

    return found
