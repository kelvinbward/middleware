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

## 🤝 Collaborative Workflow (Standard)
**Role Definition**:
*   **User (@kelvinbward)**: Senior Engineer / Owner. Has `admin` rights. Merges PRs.
*   **Agent (AI)**: Junior Engineer. Has `write` access to branches but **NO** PR/Merge rights.

**Protocol**:
1.  **Agent Work**:
    *   Create branch using prefix: `feature/` (new capability), `fix/` (bug repair), or `infra/` (system/ops).
    *   Commit changes -> Push to origin.
    *   **STOP**. Do not attempt to create PR via CLI.
    *   Generate a `Direct Link` (via Walkthrough) for the User to create the PR.
2.  **User Review**:
    *   Click Link -> Review Diff -> Create PR.
    *   Wait for `Agent Gatekeeper` checks to pass.
    *   Merge (Squash/Rebase).
3.  **Agent Cleanup (Start of Next Task)**:
    *   **MANDATORY**: Before starting ANY new task, run the cleanup script from the workspace root:
        ```bash
        ../kelvinbward/scripts/git_cleanup.sh
        ```
    *   This ensures your workspace is synchronized with the latest `main`.

## 🔄 Protocol
1.  Update this file if service definitions change.
2.  Update Root `AGENTS.md` if shared infra changes.
