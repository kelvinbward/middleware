import asyncio
import json
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.models.resume import ResumeModel
from app.core.database import DATABASE_URL

# Setup DB Connection (Standalone)
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def seed_data():
    file_path = "/frontend/resume.json" # Inside container
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        # Fallback for dev/host
        file_path = "resume.json"
        
    if not os.path.exists(file_path):
        print("No resume.json found.")
        return

    with open(file_path, "r") as f:
        data = json.load(f)

    async with AsyncSessionLocal() as session:
        # Check if exists
        # For simplicity, we just add a new one. In prod you might upsert.
        
        resume = ResumeModel(
            name=data.get("name"),
            title=data.get("title"),
            email=data.get("contact", {}).get("email"),
            phone=data.get("contact", {}).get("phone"),
            location=data.get("contact", {}).get("location"),
            objective=data.get("objective"),
            about=data.get("about"),
            experience=data.get("experience"),
            skills=data.get("skills"),
            certifications=data.get("certifications"),
            education=data.get("education"),
            links=data.get("links")
        )
        
        session.add(resume)
        await session.commit()
        print(f"Seeded resume for {resume.name}")

if __name__ == "__main__":
    asyncio.run(seed_data())
