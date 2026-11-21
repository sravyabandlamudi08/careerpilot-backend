
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

import os
import tempfile

from resume_parser import extract_resume_text, detect_skills
from skill_analyzer import analyze_skills
from roadmap_generator import generate_roadmap, recommend_projects

app = FastAPI(title="CareerPilot AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def home():
    return {"message": "CareerPilot API is running"}


@app.get("/health")
def health():
    return {"status": "Backend is running"}


@app.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    target_role: str = Form(...),
    job_description: str = Form(...)
):

    if not file.filename.lower().endswith(".pdf"):
        return {"error": "Please upload a PDF resume"}

    content = await file.read()

    if len(content) > 5 * 1024 * 1024:
        return {"error": "File must be under 5 MB"}

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(
            suffix=".pdf", delete=False
        ) as temp:

            temp.write(content)
            temp_path = temp.name

        resume_text = extract_resume_text(temp_path)

        user_skills = detect_skills(resume_text)

        required_skills = detect_skills(job_description)

        analysis = analyze_skills(
            user_skills,
            required_skills
        )

        roadmap = generate_roadmap(
            analysis["missing_skills"]
        )

        projects = recommend_projects(
            analysis["missing_skills"]
        )

        return {
            "target_role": target_role,
            "existing_skills": user_skills,
            "analysis": analysis,
            "roadmap": roadmap,
            "recommended_projects": projects
        }

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)
