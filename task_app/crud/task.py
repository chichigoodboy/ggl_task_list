from task_app.models.task import Task
from task_app.models.task_store import task_store
from task_app.schemas.task import TaskCreate, TaskUpdate


class CRUDTask:
    @staticmethod
    def create_task(obj_in: TaskCreate):
        task = Task(**obj_in.dict(exclude_unset=True))
        task_store.save_task(task)
        return task.to_json()

    @staticmethod
    def read_task(task_id):
        task = task_store.get_task(task_id)
        return task.to_json()

    @staticmethod
    def delete_task(task_id: int) -> bool:
        return task_store.delete_task(task_id)

    @staticmethod
    def update_task(task_id: int, obj_in: TaskUpdate):
        task = task_store.update_task(task_id, obj_in)
        return task.to_json()

    @staticmethod
    def list_tasks():
        tasks = task_store.list_tasks()
        result = []
        for task in tasks:
            result.append(task.to_json())
        return {'task': result}
