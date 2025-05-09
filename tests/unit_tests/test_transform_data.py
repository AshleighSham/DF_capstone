import pytest
from etl.transform.transform import transform_data
import os
import pandas as pd


@pytest.fixture
def mock_format_column_names(mocker):
    return mocker.patch("etl.transform.transform.format_column_names")


@pytest.fixture
def mock_drop_columns(mocker):
    return mocker.patch("etl.transform.transform.drop_columns")


@pytest.fixture
def mock_clean_tracks(mocker):
    return mocker.patch("etl.transform.transform.clean_tracks")


@pytest.fixture
def mock_convert_uris_to_ids(mocker):
    return mocker.patch("etl.transform.transform.convert_uris_to_ids")


@pytest.fixture
def mock_remove_missing_values(mocker):
    return mocker.patch("etl.transform.transform.remove_missing_values")


@pytest.fixture
def mock_update_API_data(mocker):
    return mocker.patch("etl.transform.transform.update_API_data")


@pytest.fixture
def mock_update_data(mocker):
    return mocker.patch("etl.transform.transform.update_data")


@pytest.fixture
def mock_simplify_and_expand_artist_genres(mocker):
    return mocker.patch("etl.transform.transform.simplify_and_expand_artist_genres")


def test_transform_data_function_calls(
    mock_simplify_and_expand_artist_genres,
    mock_update_data,
    mock_update_API_data,
    mock_remove_missing_values,
    mock_convert_uris_to_ids,
    mock_clean_tracks,
    mock_drop_columns,
    mock_format_column_names
):

    base_path = os.path.dirname(__file__)
    test_data_path = os.path.join(base_path, '../test_data/test_input.csv')

    df = pd.read_csv(test_data_path)

    transform_data(df, state="new")

    # Assert that the functions were called in the correct order
    mock_format_column_names.assert_called_once()
    mock_drop_columns.assert_called_once()
    mock_clean_tracks.assert_called_once()
    mock_convert_uris_to_ids.assert_called_once()
    mock_remove_missing_values.assert_called_once()
    mock_update_API_data.assert_called_once()
    mock_simplify_and_expand_artist_genres.assert_called_once()

    transform_data(df, state="old")

    # Assert that the functions were called in the correct order
    mock_update_data.assert_called_once()
