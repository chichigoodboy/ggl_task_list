from fastapi import FastAPI

from task_app.routers import task

app = FastAPI(docs_url='/swagger')

app.include_router(task.router)

@app.get("/")
def home():
    return {"status": "0"}
