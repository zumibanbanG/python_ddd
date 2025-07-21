from ddd.domain.task import Task, TaskId
from ddd.domain.task_repository import TaskRepository


class GetTaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def execute(self, task_id: str) -> Task | None:
        """
        タスクIDを指定してタスクを取得するユースケース
        :param task_id: タスクID
        :return: タスクオブジェクトまたはNone
        """
        return self.task_repository.get(TaskId(task_id))
