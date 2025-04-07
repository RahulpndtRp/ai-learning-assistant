# common_sdk/tracing.py

import uuid
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request


class RequestIDMiddleware(BaseHTTPMiddleware):
    """
    Middleware that generates a X-Request-ID header and stores it on request.state.
    """

    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response
