
"""
# Python file detection

import os

file_path = "test.txt"      #make sure ext is correct
# navigate to where it exists
# file_path = "stuff/test.txt"
# file_path = "C:\Users\lenovo\Desktop\test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("This is a file")
    elif os.path.isdir(file_path):
        print("This is a directory")
else:
    print("location doesn't exist")


# Python writing files (.txt, .json, .csv)

file_path = "test.txt"

try:
    with open(file_path, "w") as file:
        file.write("\n" + txt_data)
        print(f"txt file '{file_path} was created")
except FileExistsError:
    print("File exists")

#.json

import json

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

file_path = "C:/Users/HP/Desktop/output.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent=4)
        print(f"json file ({file_path}) was created")
except FileExistsError:
    print("That file already exists!")


"""

#Python Reading files (.txt, .json, .csv)

file_path = "C:\Users\lenovo\Desktop\sth.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()  # for json json.load(file)
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have the perm to read that file")