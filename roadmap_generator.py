
def generate_roadmap(missing_skills):

    resources = {
        "fastapi": "Learn FastAPI fundamentals",
        "git": "Learn Git and GitHub",
        "docker": "Learn Docker basics",
        "unit testing": "Learn Python testing with pytest",
        "rest apis": "Learn REST API concepts",
        "sql": "Practice SQL queries"
    }

    roadmap = []

    for index, skill in enumerate(missing_skills):

        task = resources.get(
            skill.lower(),
            f"Learn the fundamentals of {skill}"
        )

        roadmap.append({
            "week": index + 1,
            "skill": skill,
            "task": task,
            "completed": False
        })

    return roadmap

PROJECTS = {
    "fastapi": "Build a REST API",
    "sql": "Build a student database",
    "docker": "Containerize a Python app",
    "git": "Collaborate on a GitHub project",
    "machine learning": "Build a prediction model",
    "rest apis": "Build a weather API"
}


def recommend_projects(missing_skills):

    recommendations = []

    for skill in missing_skills:

        project = PROJECTS.get(skill.lower())

        if project:
            recommendations.append({
                "skill": skill,
                "project": project
            })

    return recommendations

