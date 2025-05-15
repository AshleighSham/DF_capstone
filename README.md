## Table of contents

- [Table of contents](#table-of-contents)
- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Planning](#planning)
- [User Stories](#user-stories)
- [Repository Structure](#repository-structure)
- [Setting up the Spotify API and PostgreSQL Compatibility](#setting-up-the-spotify-api-and-postgresql-compatibility)
- [Project Outcome](#project-outcome)
- [FAQs](#FAQs)

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
<details>
<summary>ASCII Tree for Root Respository</summary>
  
```
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
├─ api_utils.py
├─ transform_utils.py
├─ sql_utils.py
├─ db_utils.py
*.env.test*
*.env.dev*
*.env*
```
Files required by the user to add are marked with *
[Tree maker](https://ascii-tree-generator.com/)

</details>

<details>
  <summary>ASCII tree for Streamlit Respository </summary>

```
.streamlit/
├─ config.toml
├─ *secrets.toml*
app/
├─ home_page/
│  ├─ artist_search.py
├─ page_1/
│  ├─ artist_data.py
│  ├─ artist_top_tracks.py
│  ├─ clean_top_tracks.py
│  ├─ plots.py
├─ page_2/
│  ├─ artist_albums.py
│  ├─ clean_top_album_data.py
│  ├─ dataframes.py
│  ├─ get_track_popularity.py
│  ├─ plots.py
├─ page_3/
│  ├─ artist_songs_dataframe.py
├─ page_4/
│  ├─ genres_by_year.py
│  ├─ plots.py
├─ page_5/
│  ├─ properties_by_year.py
│  ├─ plots.py
├─ sql/
│  ├─ artist_songs_in_top_songs.py
│  ├─ genres_by_year.py
│  ├─ features_by_year.py
|  utils/
│  ├─ api_utils.py
│  ├─ sql_utils.py
├─ page_1_output.py
├─ page_2_output.py
├─ page_3_output.py
├─ page_4_output.py
├─ page_5_output.py
pages/
├─ 1_Artist_Top_Tracks.py
├─ 2_Artist_Albums.py
├─ 3_Top_Songs.py
├─ 4_Genre_Trends.py
├─ 5_Track_Feature_Trends.py
Home.py
```
Files required by the user to add are marked with *
[Tree maker](https://ascii-tree-generator.com/)
</details>

## Setting up the Spotify API and PostgreSQL Compatibility

To run the ETL pipeline, a functioning Spotify developer app and its relevant details are required and access to a PostgreSQL database. [Instructions on setting up a Spotify app can be found here](https://developer.spotify.com/documentation/web-api). The Client ID and Client Secret are for API use; the code below needs to be placed within your .env files in the root directory.

```env
# Target Database Configuration
TARGET_DB_SCHEMA={schema name}
TARGET_DB_NAME={database name}
TARGET_DB_USER={username}
TARGET_DB_PASSWORD={password if required, else leave blank}
TARGET_DB_HOST={host}
TARGET_DB_PORT={port}

# Spotify API Configuration
CLIENT_ID={your client ID}
CLIENT_SECRET={your client secret}
```
And for the streamlit app to function, a secrets.toml file needs to be added to the streamlit/.streamlit directory with the following information.
```toml
[connections.sql]
dialect = "postgresql"
database = "{database name}"
host = "{host}"
username = "{username}"
password = "{password}"

[sql_schema]
schema = "{your schema name}"

[api_credentials]
client_id = "{your client ID}"
client_secret = "{your client secret}"
```

## Project Outcome
The main goal of mine when looking into this dataset was to see the changes in genres, trends, popularity and audio features over time. Genres such as pop have increased in popularity over time, taking up a much larger proportion of the tracks in a given year. However, it is far to point out that the dataset does not have an even spread of tracks across the timeframe, making this a loose conclusion. The trends around audio features are slightly more reflective of what could be true outside of this dataset. Features such as Loudness, Speechiness and danceability have increased, but specifically valence has decreased. Implying that the songs are more upbeat in tune and volume, the musical positivity of the tracks has decreased over time, which, at least I do see as being plausible. The popularity by year heatmap shows that the majority of songs in the dataset per year seem to have a rating of 0, implying that while they were popular at the time, a lot of the songs in this dataset have not aged well. When removing the 0 bin fromthe heat map you get a cleaer view of the pread of popularity where the rating that has the highest density being around 1-10 and 61-70 in the year s around 2010, where most of the data is, so some of the tracks still seem to be holding on.

## FAQs

### How would you optimise query execution and performance if the dataset continues to increase?
For query performance, the use of views such as my genres_by_year view is helpful. Other options could be to look into partitioning the tables by genre or by album release year, depending on the queries being made.
### What error handling and logging have you included in your code, and how could this be leveraged?
There are multiple examples of error handling throughout this repository. There are errors handling around the API calls, some of the transformation functions, for example. There is also error handling around using the database that was very helpful in debugging connection issues throughout the loading part of this project. Under the time constraint, no logging was used in this project, but introducing a logger would provide clearer and easier-to-follow error reports.
### Are there any security or privacy issues that you need to consider, and how would you mitigate them?
In terms of the data used within this project, there is no data risk as all of the data is publicly available. The only security risk around this project is the connections to a Spotify app and a Postgresql database, both of which are excluded from the git repository, requiring anyone aiming to download and use it to have access to their own.
### How could this project be deployed or adapted into an automated cloud environment using the AWS services you have covered?
An easy first suggestion would be to replace the Postgresql database with an AWS alternative, such as Amazon RDS, the raw CSV file could easily be stored in an S3 database. An AWS Lambda function can be implemented to trigger the ETL process when new data is added to/updated in the S3 bucket. AWS CloudWatch can be used to monitor the ETL process and log the errors or execution times of functions.
