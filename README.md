README
Metadata

    Version: 1.0.0
    Released: 2025/12/05
    Author(s): Leah Everitt (Health Sciences Library and Informatics Center, University of New Mexico)
    Contributor(s): Bryan Gee (UT Libraries, University of Texas at Austin)
    License: MIT
    README last updated: 2026/04/10

Purpose

This repository contains helper scripts and templates for working with Python-DVUploader (a Python client for the Dataverse API). It was developed by Leah Everitt (University of New Mexico) as part of the Data Services Continuing Professional Education program with support from Bryan Gee and Michael Shensky (UT Austin). Scripts were created for Texas Data Repository (TDR) users. These can be modified to be used for other Dataverse instances by editing the DV_URL. This repository's functions include:

    Creating test files for upload validation.
    Printing directory structure before uploading.
    Generating a JSON config file to use when uploading a file directory.
    Templates for uploading files or directories to a TDR Dataverse dataset.

## Contents

| File | Purpose |
|------|---------|
| `create-fake-directory-files.py` | Generates 1,000 fake CSV files in a target directory for testing upload workflows. |
| `Print-Directories-oswalk.py` | Prints a directory's subdirectory and file structure. Useful for previewing what will be uploaded to Dataverse. |
| `template-config-file-creator-Python-DVUploader.py` | Builds a `config.json` file containing a target Dataverse dataset where files will uploaded and list of files to upload. Allows for manipulation of additional metadata filds. |
| `template-DirectoryUpload-Python-DVUploader.py` | Uploads all files from a given directory to a Dataverse dataset using the `dvuploader` package. Limited ability to manipulate file metadata. |
| `template-FileUpload-Python-DVUploader.py` | Uploads one file (with optional metadata) to a Dataverse dataset using the `dvuploader` package. |
| `template-Python-DVUploader-config.json` | Example `config.json` structure for use with `dvuploader` config-driven upload scripts. |
| `template-Python-DVUploader-oswalk.py` | Prints a directory's file structure, including all subdirectories and uploads all found files to a Dataverse dataset. |

## Requirements

### Python
- Python 3.8+ is recommended.

### Dependencies

Install the required package via pip:

```powershell
python -m pip install dvuploader
```
> ⚠️ The scripts that upload to Dataverse require a valid Dataverse instance URL (https://dataverse.tdl.org/), an API token with upload permissions, and an existing dataset DOI (Digital Object Identifier).

For additional information on Python DVUploader visit https://github.com/gdcc/python-dvuploader or https://pypi.org/project/dvuploader/0.1.0/.

### API token

All TDR users can obtain an API token through the web interface. Details can be found [here](https://guides.dataverse.org/en/latest/user/account.html#api-token). Tokens are good for 1 year and should not be shared. For non-TDR users reference https://guides.dataverse.org/en/latest/api/auth.html and any institutional documentation to create your API token.

## How to Use

### 1) (Optional) Generate sample files for testing

Edit `create-fake-directory-files.py` and set:

- `output_directory` to the directory where you'd like the fake files created.

Then run:

```powershell
python create-fake-directory-files.py
```
### 2) Preview a directory before uploading

Edit `Print-Directories-oswalk.py` and set:

- `start_directory` to the directory you want to inspect.

Then run:

```powershell
python Print-Directories-oswalk.py
```
### 3) Create a `config.json` file for bulk uploads

Edit `template-config-file-creator-Python-DVUploader.py` and set:

- `start_directory` to the directory containing the files you want to upload.
- `persistent_id` to the dataset DOI (e.g., `doi:10.18738/T8/XXXXX`).
- `dataverse_url` to your Dataverse base URL.
- `api_token` to your Dataverse API token.

Then run:

```powershell
python template-config-file-creator-Python-DVUploader.py
```

This will create a `config.json` file (in the current working directory) with the list of files to upload.

In this config file you can modify the optional metadata fields for individual files prior to upload:
directory_label: Optional directory label to upload the file to.
description: Optional description of the file.
categories: Optional list of categories to assign to the file.
restrict: Boolean to indicate that this is a restricted file. Defaults to False.
tabIngest: Boolean to indicate that the file should be ingested as a tab-separated file. Defaults to True.

To use the config file to upload to the repository use the following:
```powershell

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
```

### 4) Upload a directory of files

Edit `template-DirectoryUpload-Python-DVUploader.py` and set:

- The directory path inside `dv.add_directory(...)` to the directory you want to upload.
- `DV_URL` to the Dataverse dataset where you want the directory to be uploaded. TDR users do not need to change this URL.
- `API_TOKEN` to your individual API token.
-  `PID` to the Dataverse dataset DOI.

Then run:

```powershell
python template-DirectoryUpload-Python-DVUploader.py
```
This type of upload will not preserve file structure.

### 5) Upload a single file with custom metadata

Edit `template-FileUpload-Python-DVUploader.py` and set:

- `filepath` to the file you want to upload.
- - `DV_URL` to the Dataverse dataset where you want the directory to be uploaded. TDR users do not need to change this URL.
- `API_TOKEN` to your individual API token.
-  `PID` to the Dataverse dataset DOI.
- Optional fields such as `tab_ingest`, `directory_label`, `description`, `mimetype`, `categories`, and `restrict`:
directory_label: Optional directory label to upload the file to.
description: Optional description of the file.
categories: Optional list of categories to assign to the file.
restrict: Boolean to indicate that this is a restricted file. Defaults to False.
tabIngest: Boolean to indicate that the file should be ingested as a tab-separated file. Defaults to True.

The template includes how to structure each of the optional metadata fields.

Then run:

```powershell
python template-FileUpload-Python-DVUploader.py
```
### 6) Walk a directory and upload all found files

Edit `template-Python-DVUploader-oswalk.py` and set:

- `start_directory` to the folder you want to traverse.
- `DV_URL` to the Dataverse dataset where you want the directory to be uploaded. TDR users do not need to change this URL.
- `API_TOKEN` to your individual API token.
-  `PID` to the Dataverse dataset DOI.

Then run:

```powershell
python template-Python-DVUploader-oswalk.py
```
## Config file fields

The config file used by these scripts supports the following fields:

- `persistent_id`: Dataverse dataset DOI (e.g., `doi:10.18738/T8/XXXXX`).
- `dataverse_url`: Base Dataverse URL (`https://dataverse.tdl.org/`).
- `api_token`: Your Dataverse API token.
- `files`: List of file objects to upload.
  - `filepath` (required): Absolute or relative path to the file.
  - `description` (optional): A description for the uploaded file.
  - `mimetype` (optional): MIME type of the file (e.g., `text/csv`).
  - `categories` (optional): List of categories (e.g., `["Data"]`).
  - `restrict` (optional): Boolean (`true`/`false`) to restrict access to the file.
  - `tabIngest` (optional): Boolean indicating whether to enable tabular ingestion.

---

## License

This repository is licensed under the [MIT license](LICENSE).
