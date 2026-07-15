# ✅ TODO API — CRUD Task Manager

A lightweight async Task API built with **FastAPI** and a clean modular structure — full CRUD, automatic Swagger UI, and proper HTTP status codes.

---

## 🗂️ Project Structure
```
todo-api/
├── main.py          # App init, router registration
├── models.py        # Pydantic schemas
└── routers/
└── tasks.py     # All /tasks routes
```

---

## 🚀 Features

- Full **CRUD** on an in-memory task list
- Correct status codes — 200, 201, 204, 400, 404
- Input validation — empty/missing title → 400
- Auto-generated **Swagger UI** at `/docs`
- Modular router structure

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API info |
| GET | `/health` | Health check |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{id}` | Get task by ID |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

---

## 🛠️ Getting Started

### 📥 Clone Repository
```bash
git clone https://github.com/wydfaxil7/FlyRank---TODO_API.git
cd FlyRank---TODO_API
```

### 📦 Install Dependencies
```bash
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn
```

### 🚀 Run
```bash
uvicorn main:app --reload
```

---

## 📘 API Documentation
- Swagger UI → `http://127.0.0.1:8000/docs`

---

## 🧪 curl Examples

```bash
# Get all tasks
curl -i http://localhost:8000/tasks

# Create a task
curl -i -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy milk"}'

# Update a task
curl -i -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy milk", "done": true}'

# Delete a task
curl -i -X DELETE http://localhost:8000/tasks/1
```

---

## 📦 Tech Stack

| Tech | Usage |
|---|---|
| **FastAPI** | Async web framework |
| **Pydantic** | Validation & schemas |
| **Uvicorn** | ASGI server |

---

## ⭐ Final Note

Simple, clean, production-structured CRUD API — built as part of the FlyRank AI backend engineering internship.

🚀 Built with FastAPI