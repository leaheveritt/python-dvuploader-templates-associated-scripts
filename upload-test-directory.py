import dvuploader as dv

files = [
    *dv.add_directory("C:/Users/LEveritt/Documents/Upload-test")
    ]

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