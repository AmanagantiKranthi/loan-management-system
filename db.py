
import os
import pg8000.dbapi
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv(override=True)

# Database configuration
DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 5434,
    "database": "lms_db",
    "user": "lms_user"
}


# Function to create database connection
def get_connection():

    password = os.getenv("LMS_DB_PASSWORD")

    if not password:
        raise RuntimeError(
            "LMS_DB_PASSWORD is missing in .env file"
        )

    connection = pg8000.dbapi.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=password,
        timeout=10
    )

    return connection
