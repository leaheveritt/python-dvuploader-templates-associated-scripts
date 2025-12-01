#this program can be used with a config.json file to upload files to a dataverse, to create the config file use the config-file-creator
import json
import dvuploader as dv

# Load config from JSON file
with open("config.json", "r") as f:
    config = json.load(f)

# Create DVUploader File objects from config
files = []
for file_info in config["files"]:
    files.append(dv.File(**file_info))



# Create uploader instance
dvuploader = dv.DVUploader(files=files)

# Upload using config values
dvuploader.upload(
    api_token=config["api_token"],
    dataverse_url=config["dataverse_url"],
    persistent_id=config["persistent_id"],
    n_parallel_uploads=2  
)
