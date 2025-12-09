# This script uses os.walk to traverse a directory and upload all files found to a Dataverse dataset using dvuploader. 
# The upload will begin right after the list is printed - to seperate these functions you can use the config creator and config uploader scripts.
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

# Defines the Dataverse instance via URL and dataset using DOI to upload to, along with API token for authentication
# Supply your API topken and persistent ID here - the provided dataverse URL is for the Texas Data Repository        
DV_URL = "https://dataverse.tdl.org/"
API_TOKEN = "XXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
PID = "doi:10.70122/XXX/XXXXX"

dvuploader = dv.DVUploader(files=file_list)
dvuploader.upload(
    api_token=API_TOKEN,
    dataverse_url=DV_URL,
    persistent_id=PID,
    n_parallel_uploads=2, # Whatever your instance can handle
)