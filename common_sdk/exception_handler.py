# common_sdk/exception_handler.py

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from common_sdk.logger import get_logger

logger = get_logger(__name__)


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register global exception handlers on the FastAPI app.
    """

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        logger.error(f"HTTP error {exc.status_code}: {exc.detail}")
        return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})

    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        logger.exception("Unhandled exception")
        return JSONResponse(status_code=500, content={"error": "Internal Server Error"})
