from typing import List

from pydantic import BaseModel

from task_app.models.task import Task


class TaskCreate(BaseModel):
    name: str


class TaskUpdate(BaseModel):
    status: int = None
    name: str = None


class Task(BaseModel):
    id: int
    name: str
    status: Task.Status


class TaskList(BaseModel):
    task: List[Task]
