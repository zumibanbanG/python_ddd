from datetime import datetime

import grpc

from pb import todo_pb2, todo_pb2_grpc


def run() -> None:
    channel = grpc.insecure_channel("localhost:50051")
    stub = todo_pb2_grpc.TasksStub(channel)  # type: ignore

    # Add a task
    add_request = todo_pb2.AddTaskRequest(
        title="test task2", status="todo", due_date=datetime.now().isoformat()
    )
    stub.AddTask(add_request)
    print("Add Task Done")

    # Get a task
    get_request = todo_pb2.GetTaskRequest(id="1")
    get_response = stub.GetTask(get_request)
    print(
        f"Get Task Response: id={get_response.id}, title={get_response.title}, status={get_response.status}, due_date={get_response.due_date}"
    )

    # Remove a task
    remove_request = todo_pb2.RemoveTaskRequest(id="1")
    remove_response = stub.RemoveTask(remove_request)
    print(f"Remove Task Response: id={remove_response.id}")

    # List all tasks
    list_request = todo_pb2.ListAllTaskRequest()
    list_response = stub.ListAllTask(list_request)
    print("List All Tasks Response:")
    for task in list_response.tasks:
        print(
            f"Task ID: {task.id}, Title: {task.title}, Status: {task.status}, Due Date: {task.due_date}"
        )


if __name__ == "__main__":
    run()
