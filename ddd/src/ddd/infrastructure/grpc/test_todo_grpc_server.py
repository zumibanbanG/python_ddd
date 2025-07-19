import grpc
from pb import todo_pb2
from pb import todo_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = todo_pb2_grpc.TasksStub(channel)
    request = todo_pb2.CreateTaskRequest(
        id="1",
        title="テストタスク",
        status="todo",
        due_date="2025-07-20"
    )
    response = stub.CreateTask(request)
    print(f"Response: id={response.id}")

if __name__ == "__main__":
    run()
