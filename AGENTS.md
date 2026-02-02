# 🧠 Service: Middleware

## 📋 Service Role
Backend logic layer (Python/FastAPI) facilitating communications and data processing for the ecosystem.

## 📡 Service Topology
| Context | Hostname | Port | Visibility |
| :--- | :--- | :--- | :--- |
| **Cluster** | `middleware-app-1` | `5000` | Internal (Gateway routed) |
| **Standalone** | `localhost` | `8000` | Public (Dev Mode) |

## 🚀 Execution Modes
- **Cluster**: `docker compose up` (Managed by `pi-cluster-configs`).
- **Standalone**: `docker compose -f docker-compose.standalone.yml up`.

## 🔄 Handoff Protocol
1.  **Session Log**: Create entry in `pi-cluster-configs/logs/sessions/`.
2.  **State Sync**: Update `pi-cluster-configs/STATE.md` if dependencies change.
3.  **Cleanup**: Run `../kelvinbward/scripts/git_cleanup.sh` before new tasks.

## 🤝 Collaborative Workflow
- **Branching**: `feature/`, `fix/`, `infra/`.
- **Review**: Generate Direct Link for User PR creation.
- **Secrets**: NEVER commit. Use `secrets.env` template.
