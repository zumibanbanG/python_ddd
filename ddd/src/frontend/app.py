import streamlit as st
import grpc
from pb import todo_pb2, todo_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = todo_pb2_grpc.TasksStub(channel)  # type: ignore

st.title("Todo List")

# Show only tasks with status 'todo', with larger English title
st.subheader("Task List")
list_response = stub.ListAllTask(todo_pb2.ListAllTaskRequest())
todo_tasks = [task for task in list_response.tasks if task.status == "todo"]
if not todo_tasks:
    st.info("No tasks to do.")
else:
    for idx, task in enumerate(todo_tasks):
        with st.container():
            cols = st.columns([6, 3, 2])
            # タイトル（下端揃えのためdivでmin-height指定）
            cols[0].markdown(
                f"<div style='display:flex; align-items:flex-end; min-height:2.5em;'><span style='font-size:1.3em; font-weight:600; color:#222'>{task.title}</span></div>",
                unsafe_allow_html=True
            )
            # 期日（下端揃えのためdivでmin-height指定）
            cols[1].markdown(
                f"<div style='display:flex; align-items:flex-end; min-height:2.5em;'><span style='color:#555;'>Due: {task.due_date if task.due_date else '-'} </span></div>",
                unsafe_allow_html=True
            )
            # Doneボタン
            with cols[2]:
                st.markdown("<div style='height:0.7em'></div>", unsafe_allow_html=True)
                if st.button("✔️ Done", key=f"done_{task.id}", help="Mark as done", use_container_width=True):
                    stub.RemoveTask(todo_pb2.RemoveTaskRequest(
                        id=task.id
                    ))
                    st.rerun()
        # 下線をリスト外にきれいに表示
        if idx != len(todo_tasks) - 1:
            st.markdown("<hr style='margin: 0.5em 0 0.5em 0; border: none; border-top: 1.5px solid #e0e7ef;'>", unsafe_allow_html=True)

# Add Task Form
st.subheader("Add Task")
with st.form("add_task_form", clear_on_submit=True):
    title = st.text_input("Title", max_chars=100)
    due_date = st.date_input("Due Date (optional)", value=None, format="YYYY-MM-DD")
    submitted = st.form_submit_button("Add Task")
    if submitted and title:
        due_date_str = due_date.isoformat() if due_date else ""
        stub.AddTask(todo_pb2.AddTaskRequest(
            title=title,
            status="todo",
            due_date=due_date_str
        ))
        st.success("Task added!")
        st.rerun()