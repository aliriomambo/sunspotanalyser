"""
Main File for the API Service Configurations
"""
import os
from pydantic import BaseSettings, BaseModel
from dotenv import load_dotenv

load_dotenv(".env")


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "service_logger"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        "service_logger": {"handlers": ["default"], "level": LOG_LEVEL},
    }


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
