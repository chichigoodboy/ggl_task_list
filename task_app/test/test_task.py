from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def _create_task(name="買晚餐", status=0):
    response = client.post("/tasks/", json={'name': name})
    return response


def _get_task(task_id):
    response = client.get(f'/tasks/{task_id}')
    return response


def test_task_create():
    response = _create_task(name="買早餐")
    assert response.status_code == 201
    task = response.json()

    assert task['name'] == "買早餐"
    assert task['status'] == 0


def test_get_task_by_id():
    task_1_name = 'task_1'
    task = _create_task(name=task_1_name).json()
    task_id = task.get('id', -1)

    new_task = _get_task(task_id).json()
    assert new_task.get('name') == task_1_name
    assert new_task.get('id') == task_id


def test_get_non_exist_task():
    # get a non-exist task
    response = _get_task(999)
    assert response.status_code == 400


def test_update_task():
    task = _create_task(name="買早餐").json()
    task_id = task.get('id', -1)

    response = client.put(f'/tasks/{task_id}', json={'name': "買午餐", 'status': 1})
    assert response.status_code == 200

    new_task = _get_task(task_id).json()
    assert new_task.get('name') == '買午餐'
    assert new_task.get('status') == 1


def test_delete_task():
    task = _create_task(name="買早餐").json()
    task_id = task.get('id', -1)
    response = client.delete(f'/tasks/{task_id}')
    assert response.status_code == 200

    error_response = _get_task(task_id)
    assert error_response.status_code == 400


def test_delete_non_exist_task():
    task_id = 999
    response = client.delete(f'/tasks/{task_id}')
    assert response.status_code == 400


def test_list_task():
    _create_task(name='task1')
    _create_task(name='task2')
    _create_task(name='task3')
    response = client.get('/tasks')
    assert response.status_code == 200
    tasks = response.json().get('task')
    name_dict = set()
    for task in tasks:
        name_dict.add(task.get('name'))
    # assert len(tasks) == 3
    assert 'task1' in name_dict
    assert 'task2' in name_dict
    assert 'task3' in name_dict
    assert 'task4' not in name_dict
