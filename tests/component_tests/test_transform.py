import os
import pandas as pd
from etl.transform.transform import transform_data


def test_transform_data():
    base_path = os.path.dirname(__file__)

    # Expected Dataframe
    expected_track_data_path = os.path.join(
        base_path,
        '../test_data/expected_track_data.csv'
    )

    expected_track_data = pd.read_csv(expected_track_data_path)
    expected_track_data = expected_track_data.sort_values(
        by='track_id'
    ).reset_index(drop=True)

    expected_track_data.to_csv(
        'expected_track_data.csv',
        index=False
    )

    # Test Dataframe
    test_track_path = os.path.join(
        base_path,
        '../test_data/test_track_data.csv'
    )

    test_track_data = pd.read_csv(test_track_path)
    test_result = transform_data(test_track_data).sort_values(
        by='track_id'
    ).reset_index(drop=True)
    test_result = test_result.sort_values(by='track_id').reset_index(
        drop=True
    )

    # Compare the Dataframes
    pd.testing.assert_frame_equal(
        test_result,
        expected_track_data
    )
