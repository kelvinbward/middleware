from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import os
import json
from typing import List, Optional
from dotenv import load_dotenv

from app.schemas.resume import Resume
from app.utils.formatters import format_resume
from app.core.security import verify_admin_key

load_dotenv()

app = FastAPI(title="Resume Middleware API", version="1.0.0")

# CORS Configuration
origins = os.getenv("CORS_ORIGINS", "").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock Data Config
USE_MOCK = os.getenv("DATA_SOURCE") == "json"
MOCK_FILE_PATH = os.getenv("MOCK_FILE_PATH", "./app/data/resume.json")

# Placeholder for DB Logic (to be implemented in Phase 2)
async def get_latest_resume_from_db():
    # This will use SQLAlchemy/databases in Phase 2
    return None

@app.get("/api/resume", response_model=Resume)
async def get_resume():
    if USE_MOCK:
        try:
            with open(MOCK_FILE_PATH, "r") as f:
                return json.load(f)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error reading mock data: {str(e)}"
            )
    
    resume_row = await get_latest_resume_from_db()
    if not resume_row:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume not found"
        )
    return format_resume(resume_row)

@app.get("/api/resume/export", dependencies=[Depends(verify_admin_key)])
async def export_resume():
    """
    Export DB content to a static JSON file.
    Protected by admin key.
    """
    resume_row = await get_latest_resume_from_db()
    if not resume_row:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No resume data to export"
        )
    
    resume_data = format_resume(resume_row).dict()
    export_path = "/frontend/resume.json" # Volume mount point
    
    try:
        with open(export_path, "w") as f:
            json.dump(resume_data, f, indent=4)
        return {"message": "Export successful", "path": export_path}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to write export file: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
