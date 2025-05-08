import requests
import base64
import streamlit as st


def AuthenticateSpotify():
    """Authenticate with Spotify API and get an access token."""

    # Spotify client credentials
    client_id = st.secrets.api_credentials.client_id
    client_secret = st.secrets.api_credentials.client_secret

    # Encode client_id and client_secret in Base64
    auth_header = base64.b64encode(
        f"{client_id}:{client_secret}".encode()
    ).decode()

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
    except requests.exceptions.RequestException as e:
        raise f"Error: {e}"

    access_token = response.json().get("access_token")
    return access_token


def verify_request(response):
    resp = response.status_code
    response_dict = {200: 'OK', 401: 'Bad or Expired Token',
                     403: 'Bad OAuth request',
                     429: 'The app has exceeded its rate limits.'}
    if resp == 200:
        print("Request was successful")
    elif resp == 401:
        raise f"Error: {resp} {response_dict[resp]}"
    elif resp == 403:
        raise f"Error: {resp} {response_dict[resp]}"
    elif resp == 429:
        raise f"Error: {resp} {response_dict[resp]}"
    else:
        pass
