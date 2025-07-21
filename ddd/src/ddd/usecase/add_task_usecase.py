from datetime import datetime

from ddd.domain.task import Task, TaskDueDate, TaskId, TaskStatus, TaskTitle
from ddd.domain.task_repository import TaskRepository


class AddTaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def execute(self, title: str, status: str, due_date: str | None) -> Task:
        """
        タスクを追加するユースケース
        :param title: タスクのタイトル
        :param status: タスクのステータス（例: "todo", "doing", "done"）
        :param due_date: タスクの期日（ISOフォーマットの文字列、例: "2023-10-01T12:00:00"）
        :return: 追加されたタスクオブジェクト
        """
        # 追加の時はIDは0を使用
        # 期日が指定されていない場合は、due_dateはNoneにする
        if not due_date:
            due_date_obj = None
        else:
            due_date_obj = datetime.fromisoformat(due_date)
        task = Task(
            id=TaskId("0"),  # 新規作成時はIDを0に設定
            title=TaskTitle(title),
            status=TaskStatus(status),
            due_date=TaskDueDate(due_date_obj),
        )
        self.task_repository.add(task)
        return task
