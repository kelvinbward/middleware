# 🧠 Project: middleware (Public)

## 0. 🛡️ Session Startup Protocol (MANDATORY)
*Because this is a development environment, Branch Protection is manual. You must install safety hooks immediately upon starting a session.*

**Step 1:** Upon entering **ANY** repository (root or child node), execute this command to prevent accidental pushes to `main`:
```bash
echo '#!/bin/sh
branch=$(git symbolic-ref HEAD | sed -e "s,.*/\(.*\),\1,")
if [ "$branch" = "main" ]; then
  echo "🚫 DIRECT PUSH TO MAIN IS BLOCKED. USE A PR."
  exit 1
fi' > .git/hooks/pre-push && chmod +x .git/hooks/pre-push
```

**Step 2:** Verify you are on a feature branch (e.g., `feature/task-name`) before writing code.

## 🤝 Collaborative Workflow
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
    *   **MANDATORY**: Before starting ANY new task:
        *   `git checkout main`
        *   `git pull origin main`
        *   `git branch -d feature/previous-task` (Clean up local workspace)


## 📋 Role
**Middleware Service**: This repository hosts the FastAPI-based middleware that connects the PostgreSQL database to the frontend applications. Over time, it will centralize common business logic and data masking.

## 📂 Project Map & Structure
- **`app/`**: Core API application.
  - **`core/`**: Security, configuration, and global dependencies.
  - **`models/`**: SQLAlchemy/Pydantic models.
  - **`schemas/`**: Pydantic validation schemas.
  - **`utils/`**: Helper functions and formatters.
- **`tests/`**: Automated test suite.

## 🔄 Self-Documentation Protocol (CRITICAL)
After completing ANY task, you MUST:
1.  **Update this `AGENTS.md`** with any changes to ports, dependencies, or commands.
2.  **Summarize the "Next State"** so the user can resume work seamlessly.

## 🛠 Shared Infrastructure Rules
- **Network**: Connects to the `web_gateway` Docker network.
- **Service Discovery**: Accessible at `middleware.localhost` within the cluster.

## 🌳 Git Branching & Workflow
1.  **NEVER commit directly to `main`**.
2.  **Infrastructure Gatekeeping**: All changes to Docker/CI-CD require a PR.
3.  **Always create a feature branch** using the prefix `feature/`, `fix/`, or `infra/`.

## 🛠 Local Configuration
- **Ports**: 5000 (Local Dev)
- **Commands**:
    - `uvicorn app.main:app --reload --port 5000`
