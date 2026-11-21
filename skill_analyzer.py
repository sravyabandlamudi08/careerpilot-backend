
def analyze_skills(user_skills, required_skills):

    user_skills = [s.lower() for s in user_skills]
    required_skills = [s.lower() for s in required_skills]

    matched = []
    missing = []

    for skill in required_skills:

        if skill in user_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    total = len(required_skills)

    score = (
        round(len(matched) / total * 100)
        if total else 0
    )

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "match_percentage": score
    }
