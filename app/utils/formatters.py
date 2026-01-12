from typing import Union
from app.models.resume import ResumeModel
from app.schemas.resume import Resume, Contact

def format_resume(row: Union[dict, ResumeModel]) -> Resume:
    """
    Format a database row (dict or ORM object) to a structured Resume Pydantic model.
    """
    def get_val(obj, key, default=None):
        if isinstance(obj, dict):
            return obj.get(key, default)
        return getattr(obj, key, default)

    return Resume(
        id=get_val(row, "id"),
        name=get_val(row, "name"),
        title=get_val(row, "title"),
        contact=Contact(location=get_val(row, "location")),
        objective=get_val(row, "objective"),
        about=get_val(row, "about"),
        experience=get_val(row, "experience") or [],
        skills=get_val(row, "skills") or [],
        certifications=get_val(row, "certifications") or [],
        education=get_val(row, "education") or [],
        links=get_val(row, "links") or {}
    )
