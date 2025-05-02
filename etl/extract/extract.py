import os
import pandas as pd
import timeit


EXPECTED_PERFORMANCE = 0.0001

FILE_PATH = os.path.join(
    os.path.dirname(__file__), '../../data/raw/top_10000_1960-now.csv'
)

TYPE = 'TRACKS from CSV'


def extract_data() -> pd.DataFrame:
    start_time = timeit.default_timer()

    try:
        tracks = pd.read_csv(FILE_PATH)
        extract_tracks_execution_time = timeit.default_timer() - start_time
        return tracks
    except Exception:
        raise Exception(f"Failed to load CSV file: {FILE_PATH}")

