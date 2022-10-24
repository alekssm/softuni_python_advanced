import os
from os import path

command_info = input()

while not command_info == "End":
    args = command_info.split("-")
    command = args[0]
    file_name = args[1]
    if command == "Create":
        file = open(file_name, "w")
        file.close()
    elif command == "Add":
        content = args[2]
        with open(file_name, "a") as file:
            file.write(content)
            file.write("\n")
    elif command == "Replace":
        old_string = args[2]
        new_string = args[3]
        if os.path.exists(file_name):
            with open(file_name, "r+") as file:
                file_contents = file.read()
                file_contents = file_contents.replace(old_string, new_string)
                file.seek(0)
                file.truncate()
                file.write(file_contents)
        else:
            print("An error occurred")
    elif command == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")
    command_info = input()