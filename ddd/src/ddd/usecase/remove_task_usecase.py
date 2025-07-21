from ddd.domain.task import Task, TaskId
from ddd.domain.task_repository import TaskRepository


class RemoveTaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def execute(self, task_id: str) -> Task:
        """
        タスクIDを指定してタスクを削除するユースケース
        :param task_id: タスクID
        """
        task = self.task_repository.get(TaskId(task_id))
        if not task:
            raise ValueError(f"Task with ID {task_id} does not exist.")

        self.task_repository.remove(TaskId(task_id))
        return task
