from abc import ABC, abstractmethod
from .task import Task, TaskId

class TaskRepository(ABC):
    @abstractmethod
    def add(self, task: Task) -> None:
        """タスクを追加する"""
        pass

    @abstractmethod
    def get(self, task_id: TaskId) -> Task | None:
        """タスクを取得する"""
        pass

    @abstractmethod
    def remove(self, task_id: TaskId) -> None:
        """タスクを削除する"""
        pass

    @abstractmethod
    def list_all(self) -> list[Task]:
        """全てのタスクをリストする"""
        pass