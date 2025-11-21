# 🍳 RecipeGraph

**RecipeGraph** is a full-stack, cloud-native personal project built to learn and practice modern distributed software concepts.  
It’s a small but ambitious platform that lets users create, store, and query recipes — powered by a graph-based backend and containerized infrastructure.

This project is designed as both a portfolio piece and a long-term learning exercise to explore real-world DevOps, backend, and AI-assisted data engineering patterns.

---

## 🧠 Concept

The system exposes two main capabilities:
1. **Create and store recipes** in a versioned database.  
2. **Query and explore recipes** through a connected knowledge graph.

The backend will be structured as an MCP server with a FastAPI application.  
Recipes will be persisted in PostgreSQL and represented in Neo4j as a semantic graph of ingredients, cuisines, and tags.

---

## 🧰 Tech Stack & Tools

| Category | Technology | Purpose |
|-----------|-------------|----------|
| **Backend** | **FastAPI** | Core REST API and backend logic |
|  | **MCP (fastmcp)** | Modular tool interface for programmatic access |
|  | **Pydantic** | Data validation and modeling |
|  | **PostgreSQL** | Primary data storage (recipes, versions) |
|  | **SQLAlchemy** | ORM for database access |
| **Data & AI** | **Neo4j** | Knowledge graph for recipe relationships |
|  | **LangGraph / LangChain** | Workflow orchestration and data tagging |
|  | **Flink (optional)** | Stream processing for trending ingredients |
| **Infrastructure** | **Docker** | Containerization for all components |
|  | **Kubernetes (MicroK8s / k3s)** | Orchestration for dev & prod environments |
|  | **Helm** | Declarative deployment packaging |
|  | **FluxCD** | GitOps automation and continuous delivery |
|  | **Istio** | Service mesh for ingress and traffic control |
| **Observability** | **Prometheus** | Metrics and monitoring |
|  | **Grafana** | Visualization and dashboards |
| **Frontend** | **React + Vite** | Simple UI for recipe creation and browsing |
| **DevOps / CI** | **GitHub Actions** | Testing, image builds, and deployment automation |

---

## 🎯 Goals

- Learn to build, deploy, and manage a small distributed system from scratch.  
- Gain hands-on experience with Kubernetes, Helm, and GitOps principles.  
- Experiment with observability, metrics, and CI/CD pipelines.  
- Explore AI-adjacent tools (LangGraph, knowledge graphs) in a practical context.  

---

## 🗓️ Roadmap & Progress

Use this section to track progress — check off items as you complete them.  
Each phase focuses on one concept area.

---

<details>
<summary><strong>Phase 0 — Groundwork</strong></summary>

- [x] Initialize repository and README  
- [ ] Configure linting, formatting, typing, and testing tools  
- [ ] Set up virtual environment and dependency manager  

</details>

---

<details>
<summary><strong>Phase 1 — Core API & Database</strong></summary>

- [ ] Design relational schema for recipes and versions  
- [ ] Implement FastAPI CRUD endpoints  
- [ ] Add Pydantic models for validation  
- [ ] Include normalization and tagging logic  
- [ ] Write unit and integration tests  

</details>

---

<details>
<summary><strong>Phase 2 — MCP Integration</strong></summary>

- [ ] Create MCP server exposing recipe tools (`create_recipe`, `get_recipes`, `search_recipes`)  
- [ ] Share schemas between MCP and API layers  
- [ ] Verify persistence and retrieval via MCP tools  

</details>

---

<details>
<summary><strong>Phase 3 — Knowledge Graph Integration</strong></summary>

- [ ] Introduce Neo4j as a graph backend  
- [ ] Build service layer for graph upserts and lookups  
- [ ] Create LangGraph pipeline for normalization → tagging → graph updates  
- [ ] Add endpoint for graph exploration  

</details>

---

<details>
<summary><strong>Phase 4 — Containerization</strong></summary>

- [ ] Dockerize API, MCP, and database services  
- [ ] Add Docker Compose for local orchestration  
- [ ] Verify consistent builds across systems  

</details>

---

<details>
<summary><strong>Phase 5 — Kubernetes (Local)</strong></summary>

- [ ] Package services with Helm  
- [ ] Deploy locally via MicroK8s or kind  
- [ ] Validate inter-service connectivity and health  

</details>

---

<details>
<summary><strong>Phase 6 — Observability</strong></summary>

- [ ] Add Prometheus instrumentation to API  
- [ ] Deploy Grafana and visualize key metrics  
- [ ] Include Postgres and Neo4j exporters  

</details>

---

<details>
<summary><strong>Phase 7 — CI/CD Foundations</strong></summary>

- [ ] Set up GitHub Actions for linting, testing, and image builds  
- [ ] Push images to GitHub Container Registry (GHCR)  
- [ ] Enforce CI on pull requests  

</details>

---

<details>
<summary><strong>Phase 8 — GitOps (Local Flux)</strong></summary>

- [ ] Bootstrap Flux in local cluster  
- [ ] Organize manifests by environment (dev, prod)  
- [ ] Confirm automatic sync from GitHub to cluster  

</details>

---

<details>
<summary><strong>Phase 9 — Remote k3s Cluster</strong></summary>

- [ ] Deploy project to a small remote VPS running k3s  
- [ ] Connect Flux for remote GitOps  
- [ ] Validate public ingress access  

</details>

---

<details>
<summary><strong>Phase 10 — Istio Service Mesh</strong></summary>

- [ ] Install minimal Istio profile  
- [ ] Configure ingress gateway and mTLS  
- [ ] Visualize traffic routing in Kiali or Grafana  

</details>

---

<details>
<summary><strong>Phase 11 — Frontend</strong></summary>

- [ ] Create a minimal React + Vite UI  
- [ ] Add recipe creation and browsing views  
- [ ] Connect to FastAPI backend  

</details>

---

<details>
<summary><strong>Phase 12 — Application Metrics</strong></summary>

- [ ] Define custom Prometheus metrics for recipes and latency  
- [ ] Build Grafana dashboards for application insights  
- [ ] Configure alerts for critical thresholds  

</details>

---

<details>
<summary><strong>Phase 13 — Optional Flink Streaming</strong></summary>

- [ ] Add local Kafka or Redpanda  
- [ ] Create a Flink job for trending ingredient aggregation  
- [ ] Display trends in Grafana or the UI  

</details>

---

<details>
<summary><strong>Phase 14 — Hardening & Reliability</strong></summary>

- [ ] Implement health probes and readiness checks  
- [ ] Add backup routines for Postgres and Neo4j  
- [ ] Conduct lightweight load testing  

</details>

---

<details>
<summary><strong>Phase 15 — Knowledge-Driven Enhancements</strong></summary>

- [ ] Implement synonym mapping for ingredient search  
- [ ] Add “similar recipe” endpoint  
- [ ] Integrate LangChain or LangGraph enrichment  

</details>

---

<details>
<summary><strong>Phase 16 — Presentation & Documentation</strong></summary>

- [ ] Create `DEMO.md` with usage guide and setup steps  
- [ ] Add architecture diagram and screenshots  
- [ ] Tag final stable release  

</details>

---