"""
Connector that takes the existing routers into the main app
"""
from app.api.v1.api import api_router
from app.main_app import app

app.include_router(api_router)
