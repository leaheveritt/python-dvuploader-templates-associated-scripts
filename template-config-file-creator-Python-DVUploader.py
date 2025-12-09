#use this program to create a config.json file for use with the test-uploader-config.py script, this defines the dataverse where the files will be uploaded and stores your API token
import os
import json

#this is the directory you want to upload
# Provide the complete path between the quotes
start_directory = r"\Upload-test"

#this will hold the file paths from all the files in the directory you want to upload
file_paths = []

# Walk the directory and add file paths to the list
for root, name, files in os.walk(start_directory):
    for name in files:
        full_path = os.path.join(root, name) 
        file_paths.append({"filepath": full_path}) 

# Creates the config.json file dictonary and defines the dataverse URL, API token, persistent ID, and files to upload
# Supply your API topken and persistent ID here - the provided dataverse URL is for the Texas Data Repository
config_data = {
    "persistent_id": "doi:10.70122/XXX/XXXXX",
    "dataverse_url": "https://dataverse.tdl.org/",
    "api_token": "XXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
    "files": file_paths}

#creates the config.json file with all the data defined above
with open("config.json", "w", encoding="utf-8") as config_file:
    json.dump(config_data, config_file, indent=4)