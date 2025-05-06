import os
import pandas as pd
import timeit


FILE_PATH = os.path.join(
    os.path.dirname(__file__), '../../data/raw/top_10000_1960-now.csv'
)

TYPE = 'TRACKS from CSV'


def extract_data(file=None) -> pd.DataFrame:
    """
    Extracts data from a CSV file and returns it as a pandas DataFrame
    """

    # initialise the timer
    start_time = timeit.default_timer()

    try:
        # try to export the csv into a dataframe and print number of rows
        # and time taken
        file_path = FILE_PATH

        if file is not None:
            print('yay')
            file_path = os.path.join(
                            os.path.dirname(__file__), file
                        )

        tracks = pd.read_csv(file_path)

        extract_tracks_execution_time = timeit.default_timer() - start_time
        print(
            "Extracted {a} rows from {b} in {c:.4f} seconds".format(
                a=len(tracks),
                b=file_path,
                c=extract_tracks_execution_time
            )
        )
        return tracks
    except Exception:
        raise Exception(f"Failed to load CSV file: {file_path}")
