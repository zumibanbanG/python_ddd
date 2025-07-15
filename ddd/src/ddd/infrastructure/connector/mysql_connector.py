from typing import Any

import mysql.connector


class MySQLConnector:
    """MySQL接続のためのクラス"""

    @staticmethod
    def get_connection() -> Any:
        return mysql.connector.connect(
            host="localhost",
            port=3306,
            user="todo_user",
            password="todopass",
            database="todo_db",
            charset="utf8mb4",
        )
