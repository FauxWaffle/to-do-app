import os

FILEPATH = "todo_file.txt"


def get_todos(filepath=FILEPATH):
    if not os.path.exists(filepath):
        open(filepath, 'w').close()  # Create the file if it doesn't exist
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):  # <-- this function will behave as a procedure.
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

