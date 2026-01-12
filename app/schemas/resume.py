from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class Contact(BaseModel):
    location: Optional[str] = None

class Experience(BaseModel):
    company: str
    position: str
    period: str
    description: List[str]

class Skill(BaseModel):
    category: str
    items: List[str]

class Education(BaseModel):
    school: str
    degree: str
    period: str

class Resume(BaseModel):
    id: Optional[int] = None
    name: str
    title: str
    contact: Contact
    objective: str
    about: str
    experience: List[dict] = Field(default_factory=list)
    skills: List[str] = Field(default_factory=list)
    certifications: List[str] = Field(default_factory=list)
    education: List[dict] = Field(default_factory=list)
    links: Dict[str, str] = Field(default_factory=dict)
