from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()

class ResumeModel(Base):
    __tablename__ = "resume"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    title = Column(String, nullable=False)
    
    # Contact is flat in DB but nested in JSON schema. Pydantic handles the bridge.
    # Actually, let's keep it simple: Store contact info either as JSONB or normalized fields.
    # Given the previous existing schema implies simple fields, let's look at `init.sql`...
    # Wait, I don't have access to init.sql in my memory right now, but I saw it earlier.
    # It had standard fields.
    # Let's map strict to the seed: contact -> location, email, phone.
    # But for the API output `contact: { location: ... }`, we can reconstruct it.
    
    # Let's store 'location', 'email', 'phone' as columns if possible, but 
    # to support the "JSONB for everything else" strategy for speed:
    
    # NOTE: The User's seed script uses: 
    # INSERT INTO resume (name, title, email, phone, location, objective, about, experience, skills, certifications, education, links)
    
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    location = Column(String, nullable=True)
    
    objective = Column(Text, nullable=True)
    about = Column(Text, nullable=True)
    
    experience = Column(JSONB, default=[])
    skills = Column(JSONB, default=[])
    certifications = Column(JSONB, default=[])
    education = Column(JSONB, default=[])
    links = Column(JSONB, default={})
