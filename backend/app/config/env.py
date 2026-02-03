import os
from dotenv import load_dotenv

def load_env():
    """
    Load environment variables from .env file.
    This function should be called once at the application startup.
    """
    load_dotenv()
