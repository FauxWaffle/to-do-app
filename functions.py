import os

FILEPATH = "todo_file.txt"
FILEPATH_2 = 'completed.txt'

def get_todos(filepath=FILEPATH):
    if not os.path.exists(filepath):
        open(filepath, 'w').close()  # Create the file if it doesn't exist
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):  # <-- this function will behave as a procedure.
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


def write_complete(comp_arg, filepath_2=FILEPATH_2):
    with open(filepath_2, 'w') as file_local:
        file_local.writelines(comp_arg)


def get_complete(filepath=FILEPATH_2):
    if not os.path.exists(filepath):
        open(filepath, 'w').close()
    with open(filepath, 'r') as file_local:
        active_complete = file_local.readlines()
    return active_complete

