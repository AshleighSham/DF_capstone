## Table of contents

- [Table of contents](#table-of-contents)
- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Setting up the Spotify API Compatibility](#setting-up-the-Spotify-API-Compatibility)
- [Relevant References](#relevant-references)

## Project Overview

This Capstone Project was completed as part of my Data Engineering course with Digital Futures. It showcases the core data engineering skills taught throughout the program. The project implements an ETL (Extract, Transform, Load) pipeline, incorporates API usage, and presents the data through actionable visualisations.

## Repository Structure

This GitHub repository is organised into separate directories, each representing a different component of the project:

- **Data:** contains the CSV of the chosen unclean dataset for the ['Top 10000 Songs on Spotify 1950-Now' by Joakim Arvidsson](https://www.kaggle.com/datasets/joebeachcapital/top-10000-spotify-songs-1960-now)
- **etl:** Houses the ETL Pipeline.
  - **extract:** holds the extract.py file
  - **load:** holds the load.py and a post_laod_enrichment.py files
  - **sql:** the SQL queries used fr querying the SQL database needed for loading
  - **transform:** holds the transform.py file
- **Scripts:** Holds the main run_etl.py file
- **Streamlit:** Houses the streamlit application, run from within this directory with the command "streamlit run Home.py"
- **tests:** Holds the tests for the ETL processes and relevant functions
- **Utils:** Hold files regarding general utilities for the different areas.
- **.env.dev, .env.test:** two files containing the environment variables for testing and development

## Setting up the Spotify API Compatibility

To run the ETL pipeline, a functioning Spotify developer app and its relevant details are required. [Instructions on setting one up can be found here](https://developer.spotify.com/documentation/web-api). The Client ID and Client Secret are for the api to be used; these need to be placed within the utils directory in a file called api_utils.py.

```python
import requests
import base64


def AuthenticateSpotify():

    # Spotify client credentials
    client_id = "{your client id}"
    client_secret = "{your client secret}"

    # Encode client_id and client_secret in Base64
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode())
    auth_header = auth_header.decode()
    # Define the request headers and data
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "client_credentials",
    }

    try:
        # Make the POST request to get the access token
        response = requests.post("https://accounts.spotify.com/api/token",
                                 headers=headers, data=data)
    except requests.exceptions.RequestException as e:
        raise f"Error: {e}"

    access_token = response.json().get("access_token")
    return access_token
```
Like above, the Streamlit functionality also requires Spotify API access; the file must be added to the streamlit/app directory under the name spotify_auth.py, containing the same code as above.


## Setting up your Postgresql database



## Relevant References

