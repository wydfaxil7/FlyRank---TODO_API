from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models import Task

router = APIRouter(prefix="/tasks", tags=["tasks"])

tasks = [
    {"id": 1, "title": "Buy groceries", "done": False},
    {"id": 2, "title": "Read a book", "done": False},
    {"id": 3, "title": "Go for a walk", "done": True},
]

@router.get("/")
def get_tasks():
    return tasks

@router.get("/{id}")
def get_task_id(id: int):
    task = next((t for t in tasks if t["id"] == id), None)
    if task is None:
        return JSONResponse(status_code=404, content={"message": f"Task with id: {id} not found"})
    return task

@router.post("/create", status_code=201)
def create_task(task: Task):
    if not task.title.strip():
        return JSONResponse(status_code=400, content={"error": "Title cannot be empty"})
    
    new_task = {
        "id": tasks[-1]["id"] + 1 if tasks else 1,
        "title": task.title.strip(),
        "done": False
    }

    tasks.append(new_task)
    return new_task

@router.put("/{id}")
def update_task(id:int, task: Task):
    existing = next((t for t in tasks if t["id"] == id), None)
    if not existing:
        return JSONResponse(status_code=404, content={"message": f"Task with id: {id} not found"})
    if not task.title.strip():
        return JSONResponse(status_code=400, content={"message": "Title cannot be empty"})
    
    existing["title"] = task.title.strip()
    existing["done"] = task.done
    return existing

@router.delete("/{id}")
def delete_task(id: int):
    task = next((t for t in tasks if t["id"] == id), None)
    if not task:
        return JSONResponse(status_code=404, content={"message": f"Task with id: {id} not found"})
    
    tasks.remove(task)
    return JSONResponse(status_code=200, content={"message": f"Task with id: {id} deleted successfully"})
