import os
import pandas as pd
from etl.transform.transform import (
    format_column_names,
    drop_columns,
    clean_tracks,
    convert_uris_to_ids,
    remove_missing_values,
    update_data,
    simplify_and_expand_artist_genres
    )
import pytest


@pytest.fixture
def mock_extract_data(mocker):
    return mocker.patch("etl.transform.transform.extract_data")


def test_format_column_names():
    base_path = os.path.dirname(__file__)
    test_data_path = os.path.join(base_path, '../test_data/test_input.csv')

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
    test_data_path = os.path.join(base_path, '../test_data/format_column_names_data.csv')

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
    test_data_path = os.path.join(base_path, '../test_data/drop_columns_data.csv')

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
    test_data_path = os.path.join(base_path, '../test_data/convert_uris_to_ids_data.csv')

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
    test_data_path = os.path.join(base_path, '../test_data/remove_missing_values_data.csv')

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
    test_data_path = os.path.join(base_path, '../test_data/update_data_data.csv')

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
    test_data_path = os.path.join(base_path, '../test_data/simplify_and_expand_artist_genres_data.csv')

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
    test_data_path = os.path.join(base_path, '../test_data/remove_missing_values_data.csv')

    df = pd.read_csv(test_data_path)
    filepath = '../../data/clean/transformed_data.csv'

    update_data(df, filepath)

    mock_extract_data.assert_called_once()
