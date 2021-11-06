"""Main API."""

from os import environ

from fastapi import FastAPI
from now8_api.entrypoints.api.scopes import stop

DESCRIPTION = "Estimated time of arrival for public transport vehicles."

api = FastAPI(
    name="now8 API",
    description=DESCRIPTION,
    root_path=environ.get("ROOT_PATH", ""),
    responses={
        200: {
            "description": "Successful response.",
        },
        400: {"description": "Invalid value for parameter."},
        404: {"description": "No data available."},
    },
)

api.include_router(stop.router)