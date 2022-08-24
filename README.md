# GoGoLook - List Task

**API interface will be at http://localhost:8003/swagger/, can try these api after the server is ready.**

## Installations

- Create a virtualenv for TaskApp, using python 3.10.6 now
    ```shell
        pyenv virtualenv ggl
        pyenv activate ggl
    ```

- Install requirements

    ```shell
    pip install -r requirements.txt
    ```

- Run Docker applications

    ```sh
    docker-compose up -d
    ```

- Finally, you can run app in the root directory by

    ```sh
    python cli.py run --reload
    ```


## Create Task

### schema
request body:
```
POST http://localhost:8003/tasks/
```
Response body:
```shell
    {
      "id": 0,
      "name": "買早餐",
      "status": 0
    }
```
### Description:
This API create a task with default status = 0 (Incomplete), the id will be increased by 1 when task is created.
The task is saved in the local memory which handled by `TaskStore` class. When a create request task comes in, 
a task object will be generated and store in the TaskStore instance.

## List Task

### schema
request body:
```
GET http://localhost:8003/tasks/
```
Response body:
```shell
    {
      'task':[
        {
          "id": 0,
          "name": "買早餐",
          "status": 0
        }, 
        {
          "id": 1,
          "name": "買午餐",
          "status": 0
        }
      ]
    }
```
### Description:
This API will return a list of Task object that in the memory now. Will be empty if the task number is 0.


## Update Task

### schema
request body:
```
PUT http://localhost:8003/tasks/0
{
  "name": "買晚餐"
}
```
Response body:
```shell
    {
      'task':[
        {
          "id": 0,
          "name": "買晚餐",
          "status": 0
        },
      ]
    }
```
### Description:
If the id is not exist in the memory, it will return a 400 ERROR.
If the task is existing, we can retrieve the task from TaskStore, and update it. Then return it back to user


## Delete Task

### schema
request body:
```
DELETE http://localhost:8003/tasks/0
```
Response body:
```shell
{}
```
### Description:
If the id is not exist in the memory, it will return a 400 ERROR.
If the task is existing, remove this task from local memory.





  