import os

start_directory = "C:\\Users\\LEveritt\\Documents\\Upload-test"

# Walk the directory and print file paths
for root, dirs, files in os.walk(start_directory):
    print(f"Current directory: {root}")
    print(f"Subdirectories: {dirs}")
    print(f"Files: {files}") 
    Subdirectories = dirs
    print(Subdirectories)




    
dv.File(filepath="C:\\Users\\LEveritt\\Documents\\MeSH RDF_mesh2025.nt.txt"),