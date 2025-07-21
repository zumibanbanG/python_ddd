from ddd.domain.task import Task
from ddd.domain.task_repository import TaskRepository


class ListAllTaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def execute(self) -> list[Task]:
        """
        すべての未完了タスクを取得するユースケース
        :return: タスクのリスト
        """
        return self.task_repository.list_all()
