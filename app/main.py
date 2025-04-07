# app/main.py

from fastapi import FastAPI
from common_sdk.logger import get_logger
from common_sdk.exception_handler import register_exception_handlers
from common_sdk.tracing import RequestIDMiddleware

from app.routers import (
    single_pdf_rag,
    multi_pdf_compare,
    youtube_router,
    webpage_router,
    agentic_rag_router,
    llm_evaluation_router
)

logger = get_logger(__name__)

app = FastAPI(
    title="AI Learning Assistant",
    description="Collection of ML/GenAI small useful apps",
    version="0.1"
)

# --- Tracing Middleware ---
app.add_middleware(RequestIDMiddleware)

# --- Global Exception Handlers ---
register_exception_handlers(app)

# --- Routers ---
app.include_router(single_pdf_rag.router, prefix="/pdf-rag", tags=["Single PDF RAG"])
app.include_router(multi_pdf_compare.router, prefix="/multi-pdf-compare", tags=["Multi PDF Comparison"])
app.include_router(youtube_router.router, prefix="/youtube-rag", tags=["YouTube Video RAG"])
app.include_router(webpage_router.router, prefix="/webpage-rag", tags=["Web Page RAG"])
app.include_router(agentic_rag_router.router, prefix="/agentic-rag", tags=["Agentic RAG"])
app.include_router(llm_evaluation_router.router, prefix="/llm-evaluation", tags=["LLM Evaluation"])

logger.info("AI Learning Assistant startup complete")
