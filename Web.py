import streamlit as stream
import functions

todos = functions.get_todos()
comp_items = functions.get_complete()


def add_todo():
    todo = stream.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    stream.session_state["new_todo"] = ""


def comp_todo():
    comp_item = todos.pop(index)
    comp_items.append(comp_item)
    functions.write_todos(todos)
    functions.write_complete(comp_items)


stream.title("My To-Do App")
stream.write("Active Tasks:")

stream.text_input(label="Enter a todo:", placeholder="Add new item...",
                  on_change=add_todo, key="new_todo")

for index, todo in enumerate(todos):
    checkbox = stream.checkbox(todo, key=todo)
    if checkbox:
        comp_todo()
        del stream.session_state[todo]
        stream.rerun()  # this is to rerun the code for checkboxes.

stream.subheader("Completed Tasks:")

for comp_item in comp_items:
    stream.write(comp_item)



# stream.session_state   <-- this will print out at the bottom of the page the detailed info
# to show what the variable is sending to the page.
