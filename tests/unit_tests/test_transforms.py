import os
import pandas as pd
from etl.transform.transform import (
    format_column_names,
    drop_columns,
    clean_tracks,
    convert_uris_to_ids,
    remove_missing_values,
    update_API_data,
    update_data,
    simplify_and_expand_artist_genres
    )
import pytest
from unittest.mock import patch, MagicMock


@pytest.fixture
def mock_extract_data(mocker):
    return mocker.patch("etl.transform.transform.extract_data")


@pytest.fixture
def mock_get_tracks_data(mocker):
    return mocker.patch("etl.transform.transform.get_tracks_data")


@pytest.fixture
def mock_get_track_data(mocker):
    return mocker.patch("etl.transform.transform.get_track_data")


def test_format_column_names():
    base_path = os.path.dirname(__file__)
    path = '../test_data/test_input.csv'
    test_data_path = os.path.join(base_path,
                                  path)

    expected_data_path = os.path.join(
        base_path,
        '../test_data/format_column_names_data.csv'
    )

    df = pd.read_csv(test_data_path)
    expected_df = pd.read_csv(expected_data_path)

    output = format_column_names(df)

    pd.testing.assert_frame_equal(output.reset_index(drop=True), expected_df)


def test_drop_columns():
    base_path = os.path.dirname(__file__)
    path = '../test_data/format_column_names_data.csv'
    test_data_path = os.path.join(base_path,
                                  path)

    expected_data_path = os.path.join(
        base_path,
        '../test_data/drop_columns_data.csv'
    )

    df = pd.read_csv(test_data_path)
    expected_df = pd.read_csv(expected_data_path)

    output = drop_columns(df)

    pd.testing.assert_frame_equal(output.reset_index(drop=True), expected_df)


def test_convert_uris_to_ids():
    base_path = os.path.dirname(__file__)
    path = '../test_data/drop_columns_data.csv'
    test_data_path = os.path.join(base_path,
                                  path)

    expected_data_path = os.path.join(
        base_path,
        '../test_data/convert_uris_to_ids_data.csv'
    )

    df = pd.read_csv(test_data_path)
    expected_df = pd.read_csv(expected_data_path)

    output = convert_uris_to_ids(df)

    pd.testing.assert_frame_equal(output.reset_index(drop=True), expected_df)


def test_remove_missing_values():
    base_path = os.path.dirname(__file__)
    path = '../test_data/convert_uris_to_ids_data.csv'
    test_data_path = os.path.join(base_path,
                                  path)

    expected_data_path = os.path.join(
        base_path,
        '../test_data/remove_missing_values_data.csv'
    )

    df = pd.read_csv(test_data_path)
    expected_df = pd.read_csv(expected_data_path)

    output = remove_missing_values(df)

    pd.testing.assert_frame_equal(output.reset_index(drop=True), expected_df)


def test_update_data():
    base_path = os.path.dirname(__file__)
    path = '../test_data/remove_missing_values_data.csv'
    test_data_path = os.path.join(base_path,
                                  path)

    expected_data_path = os.path.join(
        base_path,
        '../test_data/update_data_data.csv'
    )

    df = pd.read_csv(test_data_path)
    expected_df = pd.read_csv(expected_data_path)

    filepath = '../../data/clean/transformed_data.csv'
    output = update_data(df, filepath)

    pd.testing.assert_frame_equal(output.reset_index(drop=True), expected_df)


def test_simplify_and_expand_artist_genres():
    base_path = os.path.dirname(__file__)
    path = '../test_data/update_data_data.csv'
    test_data_path = os.path.join(base_path,
                                  path)

    expected_data_path = os.path.join(
        base_path,
        '../test_data/simplify_and_expand_artist_genres_data.csv'
    )

    df = pd.read_csv(test_data_path)
    expected_df = pd.read_csv(expected_data_path)

    output = simplify_and_expand_artist_genres(df)

    pd.testing.assert_frame_equal(output.reset_index(drop=True), expected_df)


def test_clean_tracks():
    base_path = os.path.dirname(__file__)
    path = '../test_data/simplify_and_expand_artist_genres_data.csv'
    test_data_path = os.path.join(base_path,
                                  path)

    expected_data_path = os.path.join(
        base_path,
        '../test_data/clean_tracks_data.csv'
    )

    df = pd.read_csv(test_data_path)
    expected_df = pd.read_csv(expected_data_path)

    output = clean_tracks(df)

    pd.testing.assert_frame_equal(output.reset_index(drop=True), expected_df)


def test_update_data_call_extract_data(
    mock_extract_data
):
    base_path = os.path.dirname(__file__)
    path = '../test_data/remove_missing_values_data.csv'
    test_data_path = os.path.join(base_path,
                                  path)

    df = pd.read_csv(test_data_path)
    filepath = '../../data/clean/transformed_data.csv'

    update_data(df, filepath)

    mock_extract_data.assert_called_once()


def test_update_data_updation(mock_extract_data):

    # API response mock
    mock_extract_data.return_value = pd.DataFrame({
        "track_id": ["track1", "track2"],
        "popularity": [80, 50]
    })

    # input data
    df = pd.DataFrame({
        "track_id": ["track1", "track2"],
        "popularity": [None, None]
    })

    # call function
    filepath = MagicMock()
    new_df = update_data(df, filepath)

    print(new_df)
    assert new_df.loc[0, "popularity"] == 80
    assert new_df.loc[1, "popularity"] == 50


def test_update_data_null(mock_extract_data):

    # API response mock
    mock_extract_data.return_value = pd.DataFrame({
        "track_id": ["track1"],
        "popularity": [80]
    })

    # input data
    df = pd.DataFrame({
        "track_id": ["track1", "track2"],
        "popularity": [None, None]
    })

    # call function
    filepath = MagicMock()
    new_df = update_data(df, filepath)

    print(new_df)
    assert new_df.loc[0, "popularity"] == 80
    assert len(new_df) == 1


def test_update_API_data(mock_get_tracks_data):

    # API response mock
    mock_get_tracks_data.return_value = {
        "tracks": [
            {"external_ids": {"isrc": "ISRC1"}, "popularity": 80},
            {"external_ids": {"isrc": "ISRC2"}, "popularity": 50},
        ]
    }

    # input data
    df = pd.DataFrame({
        "track_id": ["track1", "track2"],
        "isrc": ["ISRC1", "ISRC2"],
        "popularity": [None, None]
    })

    # call function
    token = MagicMock()
    new_df = update_API_data(df, token)

    assert new_df.loc[0, "popularity"] == 80
    assert new_df.loc[1, "popularity"] == 50


def test_update_API_data_null(mock_get_tracks_data):

    # API response mock
    mock_get_tracks_data.return_value = {
        "tracks": [
            {"external_ids": {"isrc": "ISRC1"}, "popularity": 80},
            {"external_ids": {"isrc": ""}, "popularity": 50},
        ]
    }

    # input data
    df = pd.DataFrame({
        "track_id": ["track1", "track2"],
        "isrc": ["ISRC1", "ISRC2"],
        "popularity": [None, None]
    })

    # call function
    token = MagicMock()
    new_df = update_API_data(df, token)

    assert new_df.loc[0, "popularity"] == 80
    assert len(new_df) == 1


@patch("etl.transform.transform.get_track_data")
@patch("etl.transform.transform.get_tracks_data")
def test_update_API_data_fail_batch(mock_get_tracks_data, mock_get_track_data):

    # Mock the batch API call to raise an exception
    mock_get_tracks_data.side_effect = Exception("Batch API call failed")

    # Mock the individual track API call to return valid data
    mock_get_track_data.side_effect = lambda token, track_id: {
        "external_ids": {"isrc": f"ISRC_{track_id}"},
        "popularity": 50
    }

    # Input DataFrame
    df = pd.DataFrame({
        "track_id": ["track1", "track2", "track3"],
        "isrc": ["ISRC_track1", "ISRC_track2", "ISRC_track3"],
        "popularity": [None, None, None]
    })

    # Call the function
    token = MagicMock()
    new_df = update_API_data(df, token)

    # Assert that the batch API call was attempted
    mock_get_tracks_data.assert_called_once()

    # Assert that individual track API calls were made for each track
    assert mock_get_track_data.call_count == 3
    mock_get_track_data.assert_any_call(token, "track1")
    mock_get_track_data.assert_any_call(token, "track2")
    mock_get_track_data.assert_any_call(token, "track3")

    # Assert that the popularity column was updated correctly
    assert new_df.loc[0, "popularity"] == 50
    assert new_df.loc[1, "popularity"] == 50
    assert new_df.loc[2, "popularity"] == 50
