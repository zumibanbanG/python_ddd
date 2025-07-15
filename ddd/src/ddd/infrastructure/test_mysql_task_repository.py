from datetime import datetime
from typing import Any

from ddd.domain.task import Task, TaskDueDate, TaskId, TaskStatus, TaskTitle
from ddd.infrastructure.connector.mysql_connector import MySQLConnector
from ddd.infrastructure.mysql_task_repository import MySQLTaskRepository


def main() -> None:
    # MySQL接続の初期化
    connector = MySQLConnector()
    connection: Any = connector.get_connection()

    # タスクリポジトリのインスタンス化
    task_repository = MySQLTaskRepository(connection)
    try:
        # タスクの追加
        task = Task(
            id=TaskId("2"),
            title=TaskTitle("test task"),
            status=TaskStatus("todo"),
            due_date=TaskDueDate(datetime.now()),
        )
        task_repository.add(task)
        print("タスクを追加しました:", task)

        # タスクの取得
        fetched_task = task_repository.get(TaskId("1"))
        print("取得したタスク:", fetched_task)

        # # タスクの削除
        # task_repository.remove(TaskId("1"))
        # print("タスクを削除しました")
    except Exception as e:
        print("エラーが発生しました:", e)

    finally:
        connection.close()


if __name__ == "__main__":
    main()
