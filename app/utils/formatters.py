from app.schemas.resume import Resume, Contact

def format_resume(row: dict) -> Resume:
    """
    Format a database row to a structured Resume Pydantic model.
    """
    return Resume(
        id=row.get("id"),
        name=row.get("name"),
        title=row.get("title"),
        contact=Contact(location=row.get("location")),
        objective=row.get("objective"),
        about=row.get("about"),
        experience=row.get("experience") or [],
        skills=row.get("skills") or [],
        certifications=row.get("certifications") or [],
        education=row.get("education") or [],
        links=row.get("links") or {}
    )
