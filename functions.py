FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do list items in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__": # the following codes in the loop will be executed if the code is run from this file.
    # It will not be printed if the program is run from the main file where this function is being imported to
    print("This will only be printed if the code is run from this file")