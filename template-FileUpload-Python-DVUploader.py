# uses Python-DVUploader to upload a single file with custom metadata to a Dataverse instance
import dvuploader as dv
import os

# define the file to upload with custom metadata, all metadata fields are optional
# Provide the complete path between the first set of quotes
files = [
    dv.File(filepath="C:/Users/LEveritt/Documents/Upload-test/Book2.csv", tab_ingest=True, directory_label="CSV Files", description="Sample CSV file for testing.", mimetype="text/csv", categories=["metadata"], restrict=True),
    ]

# Defines which Dataverse instance with URL and dataset using DOI to upload to, along with API token for authentication
# Supply your API topken and persistent ID here - the provided dataverse URL is for the Texas Data Repository
DV_URL = "https://dataverse.tdl.org/"
API_TOKEN = "XXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
PID = "doi:10.70122/XXX/XXXXX"

dvuploader = dv.DVUploader(files=files)
dvuploader.upload(
    api_token=API_TOKEN,
    dataverse_url=DV_URL,
    persistent_id=PID,
    n_parallel_uploads=2, # Whatever your instance can handle
)