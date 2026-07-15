from fastapi import FastAPI
from routers.tasks import router as task_router

app = FastAPI(title="Task API", version="1.0")

app.include_router(task_router)

@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def health():
    return {"status": "healthy"}