import os
from dotenv import load_dotenv

ENVS = ['dev', 'test', 'prod']


def setup_env(argv):
    """
    Set up the environment for the ETL process
    """

    # set root directory to ensure its right
    os.chdir("c:/Users/ashle/Documents/GitHub/DF_capstone")

    # check if environment was provided if not raise error
    if len(argv) != 2 or argv[1] not in ENVS:
        raise ValueError(
            'Please provide an environment: '
            f'{ENVS}. E.g. run_etl dev'
        )

    # select chosen environment
    env = argv[1]

    # remove previous environment and load new
    cleanup_previous_env()
    os.environ['ENV'] = env
    if env is None:
        raise KeyError('ENV variable not set')

    # set variable and print file for a makeshift log
    env_file = '.env' if env == 'prod' else f'.env.{env}'
    print(f"Loading environment variables from: {env_file}")

    # load file raise error if not possible
    load_dotenv(env_file, override=True)
    print(f"TARGET_DB_NAME: {os.getenv('TARGET_DB_NAME')}")
    if os.getenv('TARGET_DB_NAME') is None:
        raise 'error'


def cleanup_previous_env():
    """
    Clear old environment variables to avoid
    conflicts with new envrionment
    """

    keys_to_clear = [
        'TARGET_DB_NAME', 'TARGET_DB_USER', 'TARGET_DB_PASSWORD',
        'TARGET_DB_HOST', 'TARGET_DB_PORT'
    ]

    for key in keys_to_clear:
        if key in os.environ:
            del os.environ[key]
