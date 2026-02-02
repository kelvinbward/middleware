# 🧠 Service: Middleware Spoke

## 📋 Service Role
**Logic Layer & Integrator**.
- **Target Hub**: `kelvinbward`
- **Stack**: FastAPI (Python).

## 📡 Service Topology
| Context | Hostname | Port | Visibility |
| :--- | :--- | :--- | :--- |
| **App** | `middleware-app-1` | `5000` | Internal |

## 🚀 Execution Modes
| Mode | Config | Command | Description |
| :--- | :--- | :--- | :--- |
| **Cluster** | `docker-compose.yml` | `docker compose up -d` | Prod. |
| **Standalone** | `docker-compose.standalone.yml` | `docker compose -f ... up` | **Port 8000**. Local dev. |

## 🔄 Handoff Protocol
1.  **Env**: Requires `secrets.env` (mocked in Standalone).

## 🤝 Collaborative Workflow
- **Branching**: `feature/` (Logic updates).
