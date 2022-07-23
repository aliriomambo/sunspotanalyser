"""
Main File for the API Service Configurations
"""
from pydantic import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv(".env")


class Settings(BaseSettings):
    """
    Core Settings configuration for the API Service
    """
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = 'Sun Spot Analyser Service'
    MAX_CONNECTIONS_COUNT = int(os.getenv("MAX_CONNECTIONS_COUNT", 10))
    MIN_CONNECTIONS_COUNT = int(os.getenv("MIN_CONNECTIONS_COUNT", 10))
    MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
    MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
    MONGO_USER = os.getenv("MONGO_USER", "admin")
    MONGO_PASS = os.getenv("MONGO_PASSWORD", "admin")
    MONGO_DB = os.getenv("MONGO_DB", "sun_spot_analyser")

    GRID_ROUTER_PREFIX = '/grid'
    SCORES_ROUTER_PREFIX = '/scores'


settings = Settings()
