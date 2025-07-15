from datetime import datetime

from ddd.domain.task import Task, TaskDueDate, TaskId, TaskStatus, TaskTitle
from ddd.infrastructure.in_memory_task_repository import InMemoryTaskRepository


def main() -> None:
    repo = InMemoryTaskRepository()

    # タスク作成
    task = Task(
        id=TaskId("1"),
        title=TaskTitle("テストタスク"),
        status=TaskStatus("todo"),
        due_date=TaskDueDate(datetime.now()),
    )

    # 追加
    repo.add(task)
    print("追加:", repo.list_all())

    # 取得
    fetched = repo.get(TaskId("1"))
    print("取得:", fetched)

    # 削除
    repo.remove(TaskId("1"))
    print("削除後:", repo.list_all())


if __name__ == "__main__":
    main()
