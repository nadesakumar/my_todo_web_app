def get_todos(filepath = "todos.txt"):
    """Reads a text file and returns all the todo items as a list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_list, filepath = "todos.txt"):
    """Writes a todo list into a text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_list)
