from concurrent import futures
from datetime import datetime

import grpc

from ddd.domain.task import Task, TaskDueDate, TaskId, TaskStatus, TaskTitle
from ddd.infrastructure.connector.mysql_connector import MySQLConnector
from ddd.infrastructure.repository.mysql_task_repository import MySQLTaskRepository
from pb import todo_pb2, todo_pb2_grpc


class TasksServicer(todo_pb2_grpc.TasksServicer):
    def __init__(self) -> None:
        # MySQL接続の初期化
        mysql_connector = MySQLConnector()
        # MySQLタスクリポジトリのインスタンス化
        self.repo = MySQLTaskRepository(mysql_connector.get_connection())

    def AddTask(
        self, request: todo_pb2.AddTaskRequest, context: grpc.ServicerContext
    ) -> todo_pb2.AddTaskResponse:
        due_date = None
        if request.due_date:
            due_date = datetime.fromisoformat(request.due_date)
        task = Task(
            id=TaskId(request.id),
            title=TaskTitle(request.title),
            status=TaskStatus(request.status),
            due_date=TaskDueDate(due_date),
        )
        self.repo.add(task)
        return todo_pb2.AddTaskResponse(id=task.id.value)

    def GetTask(
        self, request: todo_pb2.GetTaskRequest, context: grpc.ServicerContext
    ) -> todo_pb2.GetTaskResponse:
        task_id = TaskId(request.id)
        task = self.repo.get(task_id)
        if not task:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Task with ID {request.id} not found")
            return todo_pb2.GetTaskResponse()
        else:
            return todo_pb2.GetTaskResponse(
                id=task.id.value,
                title=task.title.value,
                status=task.status.value,
                due_date=task.due_date.value.isoformat() if task.due_date.value else "",
            )

    def RemoveTask(
        self, request: todo_pb2.RemoveTaskRequest, context: grpc.ServicerContext
    ) -> todo_pb2.RemoveTaskResponse:
        task_id = TaskId(request.id)
        self.repo.remove(task_id)
        return todo_pb2.RemoveTaskResponse(id=request.id)

    def ListAllTask(
        self, request: todo_pb2.ListAllTaskRequest, context: grpc.ServicerContext
    ) -> todo_pb2.ListAllTaskResponse:
        tasks = self.repo.list_all()
        if not tasks:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No tasks found")
            return todo_pb2.ListAllTaskResponse()
        return todo_pb2.ListAllTaskResponse(
            tasks=[
                todo_pb2.GetTaskResponse(
                    id=task.id.value,
                    title=task.title.value,
                    status=task.status.value,
                    due_date=task.due_date.value.isoformat() if task.due_date.value else "",
                )
                for task in tasks
            ]
        )


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TasksServicer_to_server(TasksServicer(), server)  # type: ignore
    server.add_insecure_port("[::]:50051")
    server.start()
    print("gRPC server is running on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
