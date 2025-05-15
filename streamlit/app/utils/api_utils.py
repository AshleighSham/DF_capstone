import requests
import base64
import streamlit as st


class BadTokenError(Exception):
    pass


class ExceededRateLimitError(Exception):
    pass


class OAuthRequestError(Exception):
    pass


def AuthenticateSpotify():
    # Spotify client credentials
    client_id = st.secrets.api_credentials.client_id
    client_secret = st.secrets.api_credentials.client_secret
    print(client_secret)

    if not client_id or not client_secret:
        raise RuntimeError(("CLIENT_ID or CLIENT_SECRET environment"
                            " variables are not set."))

    # Encode client_id and client_secret in Base64
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode())
    auth_header = auth_header.decode()
    # Define the request headers and data
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "client_credentials",
    }

    try:
        # Make the POST request to get the access token
        response = requests.post("https://accounts.spotify.com/api/token",
                                 headers=headers, data=data)
        verify_request(response)
        return response.json().get("access_token")
    except BadTokenError as e:
        raise BadTokenError(f"Error during Spotify authentication: {e}")
    except ExceededRateLimitError as e:
        raise ExceededRateLimitError(f"Error during Spotify authentication: {e}")
    except OAuthRequestError as e:
        raise OAuthRequestError(f"Error during Spotify authentication: {e}")
    except Exception as e:
        raise RuntimeError(f"Error during Spotify authentication: {e}")


def verify_request(response):
    """
    Verifies the response from the Spotify API.

    Args:
        response (requests.Response): The response object.

    Raises:
        BadTokenError: If the token is invalid or expired (401).
        ExceededRateLimitError: If the app exceeds its rate limits (429).
        OAuthRequestError: For other OAuth-related errors (403).
        RuntimeError: For unexpected errors.
    """
    resp = response.status_code
    response_dict = {
        200: 'OK',
        401: 'Bad or Expired Token',
        403: 'Bad OAuth request',
        429: 'The app has exceeded its rate limits.'
    }

    if resp == 200:
        print("Request was successful")
    elif resp == 401:
        raise BadTokenError(f"Error: {resp} {response_dict[resp]}")
    elif resp == 429:
        raise ExceededRateLimitError(f"Error: {resp} {response_dict[resp]}")
    elif resp == 403:
        raise OAuthRequestError(f"Error: {resp} {response_dict[resp]}")
    else:
        response.raise_for_status()
