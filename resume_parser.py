
import fitz
import re


# Extract text from PDF resume
def extract_resume_text(file_path):
    document = fitz.open(file_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


# List of skills to detect
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


# Detect skills from resume or job description
def detect_skills(resume_text):
    text = resume_text.lower()

    found = []

    for skill in SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text):
            found.append(skill)

    return found

