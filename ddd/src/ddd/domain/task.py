from dataclasses import dataclass
from datetime import datetime

""" 値オブジェクトの定義 """


# タスクのステータス
class TaskStatus:
    ALLOWED_STATUSES = {"todo", "done"}

    def __init__(self, value: str) -> None:
        if value not in self.ALLOWED_STATUSES:
            raise ValueError(
                f"Invalid status: {value}. Allowed statuses are {self.ALLOWED_STATUSES}."
            )
        self.value = value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TaskStatus):
            return NotImplemented
        return self.value == other.value


# タスクID
@dataclass(frozen=True)
class TaskId:
    value: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TaskId):
            return NotImplemented
        return self.value == other.value


# タスクのタイトル
@dataclass(frozen=True)
class TaskTitle:
    value: str

    def __post_init__(self) -> None:
        if not self.value or self.value.isspace():
            raise ValueError("Task title cannot be empty.")


# タスクの期日
@dataclass(frozen=True)
class TaskDueDate:
    value: datetime | None

    def __post_init__(self) -> None:
        if self.value is not None and not isinstance(self.value, datetime):
            raise ValueError("Due date must be a datetime object or None.")


""" エンティティの定義 """


@dataclass
class Task:
    id: TaskId
    title: TaskTitle
    status: TaskStatus
    due_date: TaskDueDate

    def __post_init__(self) -> None:
        if not isinstance(self.id, TaskId):
            raise TypeError("id must be an instance of TaskId.")
        if not isinstance(self.title, TaskTitle):
            raise TypeError("title must be an instance of TaskTitle.")
        if not isinstance(self.status, TaskStatus):
            raise TypeError("status must be an instance of TaskStatus.")
        if not isinstance(self.due_date, TaskDueDate):
            raise TypeError("due_date must be an instance of TaskDueDate.")

    def complete(self) -> None:
        self.status = TaskStatus("done")
