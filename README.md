# Resume Middleware (FastAPI)

This service acts as the bridge between the PostgreSQL database and the static frontend.

## Project Structure

```text
/app
  /core
    security.py      # verify_admin_key dependency
  /models            # SQLAlchemy/ORM models (Phase 2)
  /schemas
    resume.py        # Pydantic validation models
  /utils
    formatters.py    # logic for format_resume
  main.py            # API entry point & CORS
requirements.txt
.env.template
```

## Setup

1. Copy `.env.template` to `.env` and fill in your secrets.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `uvicorn app.main:app --reload --port 5000`

## Security

- **CORS**: Restricted to permitted domains in `.env`.
- **Admin API**: Routes like `/api/resume/export` require the `X-Admin-Key` header.

## Workflow Adaptation: GitHub Actions

Instead of direct file copying (`cp`) between repositories, the `kelvinbward/kelvinbward` (Hub) repository should fetch its data directly from this API during the build process.

### Scenario A: Build-time Fetching (Recommended)
Update your Hub's deployment workflow to fetch the latest JSON before committing:

```yaml
- name: Fetch Resume Data
  run: |
    curl -H "X-Admin-Key: ${{ secrets.ADMIN_API_KEY }}" \
         -X GET "https://api.yourdomain.com/api/resume" \
         > public/resume/resume.json
```

### Scenario B: API-Driven Export
If you prefer the "Export" pattern:
1. The Hub workflow triggers a `curl` to `/api/resume/export`.
2. The API writes to a shared volume (if containerized) or returns the data for the Hub to save.

**Phase 1 Goal**: Transition to fetching truth from the API rather than pushing files into the Hub from the backend.
