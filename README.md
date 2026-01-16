# ⬡ Hexagonal Architecture: User Onboarding Service

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker)
![Architecture](https://img.shields.io/badge/Architecture-Hexagonal-orange?style=for-the-badge)

## 📖 Project Overview

This repository demonstrates a **production-grade implementation of Hexagonal Architecture (Ports and Adapters)** in Python. 

Unlike standard MVC tutorials, this project prioritizes **decoupling**, **testability**, and **maintainability**. It strictly separates the **Business Logic (Core)** from the **Infrastructure (Database, API)** using Dependency Injection.

### 🎯 Key Architectural Goals
1.  **Framework Agnostic:** The Core logic (`src/core`) has **zero dependencies** on FastAPI or SQL.
2.  **Inversion of Control:** Dependencies are injected at runtime using a dedicated `Container`.
3.  **Strict Boundaries:** The database is treated as a plugin (Adapter) that can be swapped without touching business rules.

---

## 🏗️ Visual Architecture

### 1. High-Level Structure (Ports & Adapters)
This diagram illustrates how the **Core** relies only on Interfaces (Ports), while the **Infrastructure** provides the Implementations (Adapters). The Core never imports the Infrastructure.

![Diagram](./screenshots/Diagram-3.png)

### 2. Request Workflow (Sequence Diagram)
A step-by-step flow of how a User Registration request travels through the system layers, emphasizing the **Dependency Injection** phase.

![Diagram](./screenshots/Diagram-1.png)

### 3. Component & Folder Definition
How the code is physically organized to enforce boundaries.

![Diagram](./screenshots/Diagram-2.png)

---

## 🛠️ Technology Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Language** | Python 3.12 | Core programming language |
| **Framework** | FastAPI | Web Interface (Primary Adapter) |
| **Database** | PostgreSQL 15 | Persistent Storage (Secondary Adapter) |
| **ORM** | SQLAlchemy | Data Mapper |
| **Wiring** | Dependency Injector | Inversion of Control Container |
| **Runtime** | Docker & Compose | Containerization & Orchestration |

---

## 🚀 Getting Started

### Option A: Run via Docker (Recommended)
*Best for: Seeing the final architecture in action instantly.*

**1. Clone the repository**
```bash
git clone https://github.com/isharadbharadwaj/python-hexagonal-architecture.git
cd python-hexagonal-architecture
```

**2. Start the Stack**
This spins up both the FastAPI App and the Postgres DB.
```bash
docker-compose up --build
```

**3. Verify**
The app is now running at `http://localhost:8000`.

---

### Option B: Local Hybrid Development
*Best for: Debugging and rapid coding.*

**1. Start ONLY the Database**
We map the DB to port **5435** to avoid conflicts with any local Postgres instances you might have running on 5432.
```bash
docker-compose up -d db
```

**2. Create Virtual Environment**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**3. Configuration**
Ensure your `.env` file points to the Docker port (5435):
```ini
DATABASE_URL=postgresql://postgres:password@127.0.0.1:5435/hex_arch
```

**4. Run the App**
```bash
uvicorn src.main:app --reload
```

---

## 🔌 API Reference

### 1. Create User
**Input:**
```bash
curl -X POST "[http://127.0.0.1:8000/users](http://127.0.0.1:8000/users)" \
     -H "Content-Type: application/json" \
     -d '{"email": "sharad@yopmail.com"}'
```

**Output (200 OK):**
```json
{
  "id": 1,
  "email": "sharad@yopmail.com",
  "status": "created"
}

```

![Diagram](./screenshots/Image-3.png)

### 2. Duplicate User Error (Business Rule)
Trying to register the same email twice triggers a domain exception.

**Input:**
*Run the command above a second time.*

**Output (400 Bad Request):**
```json
{
  "detail": "User with email sharad@yopmail.com already exists."
}
```

---

## 🔧 Troubleshooting & Resolution

### Issue: "Database does not exist"
If you see `FATAL: database "hex_arch" does not exist`, it means the container volume persisted an old state.
**Fix:**
```bash
docker-compose down -v  # Deletes the volume
docker-compose up -d    # Recreates DB from scratch
```

### Issue: Port Conflict (Address already in use)
If you cannot start Docker because port 5432 is taken.
**Resolution:**
I have configured `docker-compose.yml` to map the container's internal port `5432` to the host machine's port **`5435`**. This ensures the project runs smoothly alongside other local databases.

---
## ✍️ Author & Connect

**Sharad** *Senior Solution Architect | Building scalable, resilient systems with Clean Architecture.*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/isharadbharadwaj/)
[![Medium](https://img.shields.io/badge/Medium-Follow-black?style=for-the-badge&logo=medium)](https://medium.com/@isharadbharadwaj)

---
*If you found this repository helpful, please give it a ⭐ star!*