import grpc

from pb import todo_pb2, todo_pb2_grpc


def run() -> None:
    channel = grpc.insecure_channel("localhost:50051")
    stub = todo_pb2_grpc.TasksStub(channel)  # type: ignore
    request = todo_pb2.AddTaskRequest(
        id="1", title="テストタスク", status="todo", due_date="2025-07-20"
    )
    response = stub.AddTask(request)
    print(f"Response: id={response.id}")


if __name__ == "__main__":
    run()
