import os
import sys
sys.path.append('../')
from config.env_config import setup_env
from etl.extract.extract import extract_data
from etl.transform.transform import transform_data
from etl.load.load import load_data


ENVY = ['old', 'new']


def main():
    """
    Executes the ETL (Extract, Transform, Load) pipeline.
    """

    # set up environment
    run_env_setup()

    if len(sys.argv) != 3 or sys.argv[2] not in ENVY:
        raise ValueError(
            'Please provide an data state: '
            f'{ENVY}. E.g. run_etl dev old'
        )

    # extract data from source
    print("Extracting data...")
    extracted_data = extract_data()
    print("Data extraction complete.")

    # transform the data
    print("Transforming data...")
    transformed_data = transform_data(extracted_data, sys.argv[2])
    print("Data Transformation complete.")

    # save the transformed data tpo csv to test against sql database
    # filepath = os.path.join("data/clean/transformed_data.csv")
    # transformed_data.to_csv(filepath, index=False)

    # Loads the transformed data into a PostgreSQL database
    print("Loading data into PostgreSQL...")
    load_data(transformed_data)
    print("Data loading complete.")

    # Prints status messages to indicate progress and completion
    print(
        f"ETL pipeline run successfully in "
        f'{os.getenv("ENV", "error")} environment!'
    )


def run_env_setup():
    """
    Set up the environment and return completetion message
    """
    print("Setting up environment...")
    setup_env(sys.argv)
    print("Environment setup complete.")


if __name__ == "__main__":
    main()
