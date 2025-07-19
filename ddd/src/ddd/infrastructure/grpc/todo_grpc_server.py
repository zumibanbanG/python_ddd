from concurrent import futures

import grpc

from pb import todo_pb2, todo_pb2_grpc


class TasksServicer(todo_pb2_grpc.TasksServicer):
    def AddTask(
        self, request: todo_pb2.AddTaskRequest, context: grpc.ServicerContext
    ) -> todo_pb2.AddTaskResponse:
        # ここでタスクを作成するロジックを実装
        print(
            f"Creating task with ID: {request.id}, Title: {request.title}, Status: {request.status}, Due Date: {request.due_date}"
        )

        # レスポンスを返す
        return todo_pb2.AddTaskResponse(id=request.id)


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TasksServicer_to_server(TasksServicer(), server)  # type: ignore
    server.add_insecure_port("[::]:50051")
    server.start()
    print("gRPC server is running on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
