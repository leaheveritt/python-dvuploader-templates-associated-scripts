import dvuploader as dv

# Define the directory to upload - provide the complete path between the quotes
files = [
    *dv.add_directory("/Example-Path/To/Your/Directory-To-Upload")
    ]

# Supply your API topken and persistent ID here - the provided dataverse URL is for the Texas Data Repository
DV_URL = "https://dataverse.tdl.org/"
API_TOKEN = "XXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
PID = "doi:10.70122/XXX/XXXXX"

dvuploader = dv.DVUploader(files=files)
dvuploader.upload(
    api_token=API_TOKEN,
    dataverse_url=DV_URL,
    persistent_id=PID,
    n_parallel_uploads=2,
)