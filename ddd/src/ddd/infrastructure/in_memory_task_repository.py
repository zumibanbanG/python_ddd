from typing import Dict
from ddd.domain.task_repository import TaskRepository
from ddd.domain.task import Task, TaskId

""" インメモリのタスクリポジトリ実装 """

class InMemoryTaskRepository(TaskRepository):
    def __init__(self) -> None:
        self._tasks: Dict[str, Task]  = {}

    def add(self, task: Task) -> None:
        self._tasks[task.id.value] = task

    def get(self, task_id: TaskId) -> Task | None:
        return self._tasks.get(task_id.value)

    def remove(self, task_id: TaskId) -> None:
        self._tasks.pop(task_id.value, None)

    def list_all(self) -> list[Task]:
        return list(self._tasks.values())