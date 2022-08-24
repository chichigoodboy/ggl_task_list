from fastapi import APIRouter
from starlette import status

from task_app.crud.task import CRUDTask

from task_app.schemas.task import TaskCreate, TaskUpdate, Task, TaskList

router = APIRouter(prefix='/tasks', tags=['Tasks'])


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Task)
def create_task(obj: TaskCreate):
    return CRUDTask.create_task(obj_in=obj)


@router.get('/{task_id}', status_code=status.HTTP_200_OK, response_model=Task)
def get_task(task_id: int):
    return CRUDTask.read_task(task_id)


@router.delete('/{task_id}', status_code=status.HTTP_200_OK)
def delete_task(task_id: int):
    return CRUDTask.delete_task(task_id=task_id)


@router.put('/{task_id}', status_code=status.HTTP_200_OK, response_model=Task)
def update_task(task_id: int, obj: TaskUpdate):
    return CRUDTask.update_task(task_id=task_id, obj_in=obj)


@router.get('/', status_code=status.HTTP_200_OK, response_model=TaskList)
def list_tasks():
    return CRUDTask.list_tasks()
