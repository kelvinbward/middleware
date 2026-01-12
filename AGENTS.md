# Middleware Service

The Middleware Service is a Python/FastAPI application that serves as the backend logic layer for the Resume data and potential future integrations.

## Architecture
- **Service Name**: `middleware-app-1`
- **Internal Port**: 5000
- **Database**: Connects to `resume-db-1` (PostgreSQL) on port 5432.
- **Gateway**: Exposed via `web_gateway` at `http://middleware.localhost`.

## Deployment
- **Orchestration**: Managed by `pi-cluster-configs/setup.sh`.
- **Configuration**: environment variables in `.env` (derived from `.env.template`).

## Development
- **Local Run**: `uvicorn app.main:app --reload`
- **Testing**: `pytest`
- **Seeding**: Use the python seed script `app.scripts.seed`.

## Protocol
- **Branching**: Follow standard `feature/` -> `main` flow.
- **Docs**: keep `AGENTS.md` updated with architecture changes.
