from datetime import datetime
from typing import Any, cast

from ddd.domain.task import Task, TaskDueDate, TaskId, TaskStatus, TaskTitle
from ddd.domain.task_repository import TaskRepository

""" MySQLのタスクリポジトリ実装 """


class MySQLTaskRepository(TaskRepository):
    def __init__(self, connection: Any) -> None:
        self._connection = connection

    def add(self, task: Task) -> None:
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, status, due_date) VALUES (%s, %s, %s)",
            (task.title.value, task.status.value, task.due_date.value),
        )
        self._connection.commit()
        cursor.close()

    def get(self, task_id: TaskId) -> Task | None:
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT id, title, status, due_date FROM tasks WHERE id = %s", (task_id.value,)
        )
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Task(
                TaskId(str(row[0])),
                TaskTitle(str(row[1])),
                TaskStatus(str(row[2])),
                TaskDueDate(cast(datetime | None, row[3])),
            )
        return None

    def remove(self, task_id: TaskId) -> None:
        cursor = self._connection.cursor()
        cursor.execute("UPDATE tasks SET status = 'done' WHERE id = %s", (task_id.value,))
        self._connection.commit()
        cursor.close()

    def list_all(self) -> list[Task]:
        cursor = self._connection.cursor()
        cursor.execute("SELECT id, title, status, due_date FROM tasks WHERE status != 'done'")
        rows = cursor.fetchall()
        cursor.close()
        return [
            Task(
                TaskId(str(row[0])),
                TaskTitle(str(row[1])),
                TaskStatus(str(row[2])),
                TaskDueDate(cast(datetime | None, row[3])),
            )
            for row in rows
        ]
