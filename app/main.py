from app.core.config import settings
from app.api.v1.api import api_router
from app.db.database import init_db
from fastapi import FastAPI
import uvicorn
from app.main_app import app

app.include_router(api_router)

# def init_app() -> FastAPI:
#     """
#     Initialise a FastApi app, with all the required routes and the
#     :return: FastAPI initialized app
#     """
#     app_ = FastAPI(title=settings.PROJECT_NAME)
#     init_db(app_)
#     app_.include_router(api_router)
#     return app_
#
#
# app = init_app()
#
# if __name__ == "__main__":
#     uvicorn.run("main:app",
#                 host=settings.API_HOST,
#                 reload=True,
#                 port=settings.API_PORT)
