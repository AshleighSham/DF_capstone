## Table of contents

- [Table of contents](#table-of-contents)
- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Planning](#planning)
- [User Stories](#user-stories)
- [Repository Structure](#repository-structure)
- [Setting up the Spotify API Compatibility](#setting-up-the-Spotify-API-Compatibility)
- [FAQ](#FAQ)

## Project Overview

This Capstone Project was completed as part of my Data Engineering course with Digital Futures. It showcases the core data engineering skills taught throughout the program. The project implements an ETL (Extract, Transform, Load) pipeline, incorporates API usage, and presents the data through actionable visualisations. The project draws on two main data sources: Spotify’s API and a Kaggle dataset titled, ['Top 10000 Songs on Spotify 1950-Now' by Joakim Arvidsson](https://www.kaggle.com/datasets/joebeachcapital/top-10000-spotify-songs-1960-now). The Dataset is a collection of Spotify track information for high-ranking songs from the Australian Recording Industry Association and Billboard Charts. This dataset compiles Spotify track information for high-ranking songs based on the Australian Recording Industry Association and Billboard charts. Although some of Spotify’s more detailed APIs—such as those providing genre and audio features like tempo and valence—have since been deprecated, the dataset retains this information, offering valuable insight into musical trends over time and how these songs are perceived today. Combined with the Spotify Search API, the project also allows users to search for their favourite artists, explore their top songs and albums, and quickly check whether any tracks appear in the dataset.

## Objectives
- Build a robust ETL Pipeline to process a CSV of Spotify data.
- Create an interactive Streamlit app that aids insights through appropriate visualisations.
- Implement good testing practices to ensure high-quality code.

## Planning
1. Set up the relevant environments and PostgreSQL databases
2. Build sufficent tests for the ETL pipeline
3. Implement Data Extraction for the dataset and API's
4. Transform and standardise the data
5. Build a streamlit app for data visualisations compatible with the API directly and the Postgresql

## User Stories
- As a Data Engineer, I want to extract live data from Spotify API's for relevant analysis.
- As a Data Engineer, I want to transform and standardise the dataset for accurate analysis.
- As a Data Engineer, I want to load the data into a PostgreSQL database so that it can be easily queried.
- As a Data Analyst, I want to view an Artist's Top track and Albums because I'm nosy.
- Aa a Data Analyst, I want to be able to filter data by year, genre or popularity so I can draw specific insights.

## Repository Structure

This GitHub repository is organised into separate directories, each representing a different component of the project:

- **data:** contains the CSV of the chosen dataset.
- **etl:** Houses the ETL Pipeline.
  - **extract:** holds the extract.py file
  - **load:** holds the load.py and a post_laod_enrichment.py files
  - **sql:** the SQL queries used fr querying the SQL database needed for loading
  - **transform:** holds the transform.py file
- **scripts:** Holds the main run_etl.py file
- **streamlit:** Houses the streamlit application, run from within this directory with the command "streamlit run Home.py"
- **tests:** Holds the tests for the ETL processes and relevant functions
- **utils:** Hold files regarding general utilities for the different areas.
- **.env.dev, .env.test:** two files containing the environment variables for testing and development

  config/
├─ env_config.py
├─ db_config.py
data/
├─ raw/
│  ├─ top_10000_1960-now.csv
├─ clean/
│  ├─ transformed_data.csv
etl/
├─ extract/
│  ├─ extract.py
├─ transform/
│  ├─ transform.py
├─ load/
│  ├─ load.py
│  ├─ post_load_enrichment.py
├─ sql/
│  ├─ artists_track_table.sql
│  ├─ genres_by_year.sql
│  ├─ properties_by_year.sql
│  ├─ set_primary_key.sql
scripts/
├─ run_etl.py
streamlit/
tests/
├─ component_tests/
├─ integration_tests/
├─ unit_tests/
├─ run_tests.py
utils/
├─ *api_utils.py*
├─ transform_utils.py
├─ sql_utils.py
├─ db_utils.py


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


## FAQ
### How would you go about optimising query execution and performance if the dataset continues to increase?
### What error handling and logging have you included in your code and how this could be leveraged?
### Are there any security or privacy issues that you need to consider and how would you mitigate them?
### How this project could be deployed or adapted into an automated cloud environment using the AWS services you have covered?
