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
