from fastapi.testclient import TestClient
from app.main import app
import os
from unittest.mock import patch, mock_open, AsyncMock

client = TestClient(app)

MOCK_RESUME = {
    "name": "Test User",
    "title": "Engineer",
    "contact": {"location": "Test City"},
    "objective": "To test",
    "about": "About test",
    "experience": [],
    "skills": [],
    "certifications": [],
    "education": [],
    "links": {}
}

# Mock DB Session
async def override_get_db():
    mock_session = AsyncMock()
    yield mock_session

# Override the get_db dependency
from app.core.database import get_db
app.dependency_overrides[get_db] = override_get_db

def test_read_resume_mock():
    # Test fallback to JSON when configured
    with patch("app.main.USE_MOCK", True):
         with patch("json.load", return_value=MOCK_RESUME):
            with patch("builtins.open", mock_open(read_data='{}')):
                response = client.get("/api/resume")
                assert response.status_code == 200
                assert response.json()["name"] == "Test User"

def test_read_resume_db_success():
    # Helper class to mimic ORM object access
    class MockRow:
        def __init__(self, data):
            for k, v in data.items():
                setattr(self, k, v)
        
        # Add get method for legacy support if needed, but our formatter handles attrs
        def get(self, key, default=None):
            return getattr(self, key, default)

    mock_db_data = {
         "id": 1,
         "name": "DB User",
         "title": "Dev",
         "location": "Cloud",
         "objective": "Obj",
         "about": "Abt",
         "experience": [],
         "skills": [],
         "certifications": [],
         "education": [],
         "links": {}
    }
    
    with patch("app.main.USE_MOCK", False):
        with patch("app.main.get_latest_resume", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = MockRow(mock_db_data)
            
            response = client.get("/api/resume")
            assert response.status_code == 200
            assert response.json()["name"] == "DB User"

def test_admin_export_success():
    class MockRow:
        def __init__(self, data):
            for k, v in data.items():
                setattr(self, k, v)

    mock_db_data = {
         "id": 1,
         "name": "DB User",
         "title": "Dev",
         "location": "Cloud",
         "objective": "Obj",
         "about": "Abt",
         "experience": [],
         "skills": [],
         "certifications": [],
         "education": [],
         "links": {}
    }

    with patch("app.core.security.ADMIN_API_KEY", "secret123"):
        with patch("app.main.get_latest_resume", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = MockRow(mock_db_data)
            
            with patch("builtins.open", mock_open()) as mock_file:
                response = client.get(
                    "/api/resume/export", 
                    headers={"X-Admin-Key": "secret123"}
                )
                assert response.status_code == 200
                assert response.json()["message"] == "Export successful"
