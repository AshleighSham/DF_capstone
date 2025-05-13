import os
import pandas as pd
from utils.transform_utils import (
    get_track_data,
    get_tracks_data,
    set_index,
    check_in_list
    )
import pytest
from unittest.mock import patch, MagicMock


@pytest.fixture
def mock_get(mocker):
    return mocker.patch("utils.transform_utils.requests.get")


@patch("utils.transform_utils.requests.get")
def test_get_tracks_data(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "tracks": [
            {"id": "track1", "name": "Song 1"},
            {"id": "track2", "name": "Song 2"}
        ]
    }
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    # Call the function
    token = "mock_token"
    track_ids = ["track1", "track2"]
    response = get_tracks_data(token, track_ids)

    # Assert the response is returned correctly
    assert response == {
        "tracks": [
            {"id": "track1", "name": "Song 1"},
            {"id": "track2", "name": "Song 2"}
        ]
    }

    # Assert the API was called with the correct parameters
    mock_get.assert_called_once_with(
        "https://api.spotify.com/v1/tracks?ids=track1,track2",
        headers={"Authorization": "Bearer mock_token"},
        params={"market": "ES"}
    )


@patch("utils.transform_utils.requests.get")
def test_get_tracks_data_401(mock_get):
    # Mock the API response for invalid token
    mock_response = MagicMock()
    mock_response.status_code = 401
    mock_response.json.return_value = {"error": "invalid_token"}
    mock_get.return_value = mock_response

    # Call the function and assert it raises a RuntimeError
    token = "invalid_token"
    track_ids = ["track1", "track2"]
    with pytest.raises(RuntimeError, match="Error: 401 Bad or Expired Token"):
        get_tracks_data(token, track_ids)


@patch("utils.transform_utils.requests.get")
def test_get_tracks_data_429(mock_get):
    # Mock the API response for rate limit exceeded
    mock_response = MagicMock()
    mock_response.status_code = 429
    mock_response.json.return_value = {"error": "rate_limit_exceeded"}
    mock_get.return_value = mock_response

    # Call the function and assert it raises a RuntimeError
    token = "mock_token"
    track_ids = ["track1", "track2"]
    with pytest.raises(RuntimeError, match="Error: 429 The app has exceeded its rate limits."):
        get_tracks_data(token, track_ids)


@patch("utils.transform_utils.requests.get")
def test_get_track_data(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "track1", "name": "Song 1"}
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    # Call the function
    token = "mock_token"
    track_id = "track1"
    response = get_track_data(token, track_id)

    # Assert the response is returned correctly
    assert response == {"id": "track1", "name": "Song 1"}

    # Assert the API was called with the correct parameters
    mock_get.assert_called_once_with(
        "https://api.spotify.com/v1/tracks/track1",
        headers={"Authorization": "Bearer mock_token"},
        params={"market": "ES"}
    )


@patch("utils.transform_utils.requests.get")
def test_get_track_data_401(mock_get):
    # Mock the API response for invalid token
    mock_response = MagicMock()
    mock_response.status_code = 401
    mock_response.json.return_value = {"error": "invalid_token"}
    mock_get.return_value = mock_response

    # Call the function and assert it raises a RuntimeError
    token = "invalid_token"
    track_id = "track1"
    with pytest.raises(RuntimeError, match="Error: 401 Bad or Expired Token"):
        get_track_data(token, track_id)


@patch("utils.transform_utils.requests.get")
def test_get_track_data_429(mock_get):
    # Mock the API response for rate limit exceeded
    mock_response = MagicMock()
    mock_response.status_code = 429
    mock_response.json.return_value = {"error": "rate_limit_exceeded"}
    mock_get.return_value = mock_response

    # Call the function and assert it raises a RuntimeError
    token = "mock_token"
    track_id = "track1"
    with pytest.raises(RuntimeError, match="Error: 429 The app has exceeded its rate limits."):
        get_track_data(token, track_id)
