import dvuploader as dv
import os

start_directory = "C:\\Users\\LEveritt\\Documents\\Upload-test"

# Walk the directory and print file paths
for root, dirs, files in os.walk(start_directory):
    print(f"Current directory: {root}")
    print(f"Subdirectories: {dirs}")
    print(f"Files: {files}") 
        
# blank list for the file paths
file_list = []

# Walk the directory and add file paths to the list
for root, dirs, files in os.walk(start_directory):
    for name in files:
        file_paths = os.path.join(root, name) # os.walk gives a tuple of (root, dirs, files), so we need to join root and name to get the full file path
        file_list.append(dv.File(filepath=file_paths)) # Append dv.File to each file path on the list which is required by dvuploader
        
DV_URL = "https://dataverse.tdl.org/"
API_TOKEN = "d80c6e63-58f0-4678-ac63-8fa02a5fcd7a"
PID = "https://doi.org/10.18738/T8/MHBBXA"

dvuploader = dv.DVUploader(files=file_list)
dvuploader.upload(
    api_token=API_TOKEN,
    dataverse_url=DV_URL,
    persistent_id=PID,
    n_parallel_uploads=2, # Whatever your instance can handle
)
