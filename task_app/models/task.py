from enum import Enum


class Task:
    class Status(Enum):
        Incomplete = 0
        Complete = 1

    def __init__(self, name, status=Status.Incomplete):
        self.name = name
        self.status = status
        self.id = None

    def to_json(self):
        return {
            'name': self.name,
            'id': self.id,
            'status': self.status
        }
