from concurrent import futures

import grpc

from ddd.infrastructure.connector.mysql_connector import MySQLConnector
from ddd.infrastructure.repository.mysql_task_repository import MySQLTaskRepository
from ddd.usecase.add_task_usecase import AddTaskUseCase
from ddd.usecase.get_task_usecase import GetTaskUseCase
from ddd.usecase.list_all_task_usecase import ListAllTaskUseCase
from ddd.usecase.remove_task_usecase import RemoveTaskUseCase
from pb import todo_pb2, todo_pb2_grpc


class TasksServicer(todo_pb2_grpc.TasksServicer):
    def __init__(self) -> None:
        # MySQL接続の初期化
        mysql_connector = MySQLConnector()
        # MySQLタスクリポジトリのインスタンス化
        self.repo = MySQLTaskRepository(mysql_connector.get_connection())
        # ユースケースのインスタンス化
        self.add_task_usecase = AddTaskUseCase(self.repo)
        self.get_task_usecase = GetTaskUseCase(self.repo)
        self.list_all_task_usecase = ListAllTaskUseCase(self.repo)
        self.remove_task_usecase = RemoveTaskUseCase(self.repo)

    def AddTask(
        self, request: todo_pb2.AddTaskRequest, context: grpc.ServicerContext
    ) -> todo_pb2.AddTaskResponse:
        task = self.add_task_usecase.execute(
            title=request.title,
            status=request.status,
            due_date=request.due_date,
        )
        return todo_pb2.AddTaskResponse(id=task.id.value)

    def GetTask(
        self, request: todo_pb2.GetTaskRequest, context: grpc.ServicerContext
    ) -> todo_pb2.GetTaskResponse:
        task_id = request.id
        task = self.get_task_usecase.execute(task_id)
        if not task:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Task with id {task_id} not found")
            return todo_pb2.GetTaskResponse()
        return todo_pb2.GetTaskResponse(
            id=task.id.value,
            title=task.title.value,
            status=task.status.value,
            due_date=task.due_date.value.isoformat() if task.due_date.value else "",
        )

    def RemoveTask(
        self, request: todo_pb2.RemoveTaskRequest, context: grpc.ServicerContext
    ) -> todo_pb2.RemoveTaskResponse:
        task_id = request.id
        try:
            self.remove_task_usecase.execute(task_id)
        except ValueError as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(str(e))
            return todo_pb2.RemoveTaskResponse()
        return todo_pb2.RemoveTaskResponse(id=task_id)

    def ListAllTask(
        self, request: todo_pb2.ListAllTaskRequest, context: grpc.ServicerContext
    ) -> todo_pb2.ListAllTaskResponse:
        tasks = self.list_all_task_usecase.execute()
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
