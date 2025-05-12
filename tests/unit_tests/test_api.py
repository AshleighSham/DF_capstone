import os
import pandas as pd
from utils.api_utils import AuthenticateSpotify
import pytest
from unittest.mock import patch, MagicMock


@pytest.fixture
def mock_request_post(mocker):
    return mocker.patch("utils.api_utils.requests.post")


@patch("utils.api_utils.requests.post")
def test_auth_spotify(mock_request_post):
    mock_response = MagicMock()
    mock_response.json.return_value = {"access_token": "mock_access_token"}
    mock_response.status_code = 200
    mock_request_post.return_value = mock_response

    access_token = AuthenticateSpotify()

    # Assert the access token is returned correctly
    assert access_token == "mock_access_token"


@patch("utils.api_utils.requests.post")
def test_auth_spotify_401(mock_request_post):
    mock_response = MagicMock()
    mock_response.json.return_value = {"access_token": "bad_access_token"}
    mock_response.status_code = 401
    mock_request_post.return_value = mock_response

    # set environment variables
    os.environ["CLIENT_ID"] = "invalid_client_id"
    os.environ["CLIENT_SECRET"] = "invalid_client_secret"

    # call the function and assert it raises a RuntimeError
    with pytest.raises(RuntimeError, match="Error: 401 Bad or Expired Token"):
        AuthenticateSpotify()


@patch("utils.api_utils.requests.post")
def test_auth_spotify_401(mock_request_post):
    mock_response = MagicMock()
    mock_response.json.return_value = {"error": "rate_limit_exceeded"}
    mock_response.status_code = 429
    mock_request_post.return_value = mock_response

    # call the function and assert it raises a RuntimeError
    with pytest.raises(RuntimeError, match="Error: 429 The app has exceeded its rate limits."):
        AuthenticateSpotify()
