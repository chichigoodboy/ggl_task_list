from fastapi import HTTPException

from task_app.schemas.task import TaskUpdate


class TaskStore:
    def __init__(self):
        self.current_id = 0
        self.task_list = {}

    def save_task(self, task):
        task.id = self.current_id
        self.task_list[task.id] = task
        self.current_id += 1
        return self.current_id

    def get_task(self, task_id):
        if task_id not in self.task_list:
            raise HTTPException(status_code=400, detail="the task is not exist")

        return self.task_list[task_id]

    def delete_task(self, task_id):
        if task_id not in self.task_list:
            raise HTTPException(status_code=400, detail="the task is not exist")
        del self.task_list[task_id]
        return True

    def update_task(self, task_id: int, obj: TaskUpdate):
        if task_id not in self.task_list:
            raise HTTPException(status_code=400, detail="the task is not exist")
        task = self.task_list[task_id]
        if obj.name:
            task.name = obj.name
        if obj.status:
            task.status = obj.status
        return task

    def list_tasks(self):
        return self.task_list.values()


task_store = TaskStore()
