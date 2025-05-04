from dotenv import load_dotenv
import os

# Load environment variables from .env.test
load_dotenv(dotenv_path=".env.test")
print(os.getenv("TARGET_DB_NAME"))