import os

def print_directory_contents(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory {path} does not exist")

# Replace 'your_directory_path' with the path of the directory you want to list
directory_path = 'C:/Users/DELL/Desktop/python projects'
print_directory_contents(directory_path)