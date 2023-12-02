import streamlit as stream
import functions

todos = functions.get_todos()


def add_todo():
    todo = stream.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    stream.session_state["new_todo"] = ""

stream.title("My To-Do App")
stream.write("This app is to increase your stuff.")

for index, todo in enumerate(todos):
    checkbox = stream.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del stream.session_state[todo]
        stream.rerun()  # this is to rerun the code for checkboxes.


stream.text_input(label="Enter a todo:", placeholder="Add new item...",
                  on_change=add_todo, key="new_todo")

# stream.session_state   <-- this will print out at the bottom of the page the detailed info
# to show what the variable is sending to the page.
