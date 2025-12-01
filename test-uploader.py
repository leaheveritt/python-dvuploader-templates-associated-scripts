# uses Python-DVUploader to upload a single file with custom metadata to a Dataverse instance
import dvuploader as dv
import os

# define the file to upload with custom metadata, all metadata fields are optional
files = [
    dv.File(filepath="C:/Users/LEveritt/Documents/Upload-test/Book2.csv", tab_ingest=True, directory_label="CSV Files", description="Sample CSV file for testing.", mimetype="text/csv", categories=["metadata"], restrict=True),
    ]
print(str(files))

# Defines which Dataverse instance and dataset to upload to, along with API token for authentication
DV_URL = "https://dataverse.tdl.org/"
API_TOKEN = "d80c6e63-58f0-4678-ac63-8fa02a5fcd7a"
PID = "https://doi.org/10.18738/T8/KRSISP"

dvuploader = dv.DVUploader(files=files)
dvuploader.upload(
    api_token=API_TOKEN,
    dataverse_url=DV_URL,
    persistent_id=PID,
    n_parallel_uploads=2, # Whatever your instance can handle
)

