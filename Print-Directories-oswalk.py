import os

# This is the directory you want to upload, provide the complete path between the quotes
start_directory = "\\Upload-test"

# Walk the directory and print all the file paths, this allows you to see the structure of the directory before uploading
for root, dirs, files in os.walk(start_directory):
    print(f"Current directory: {root}")
    print(f"Subdirectories: {dirs}")
    print(f"Files: {files}") 
    Subdirectories = dirs
    print(Subdirectories)
