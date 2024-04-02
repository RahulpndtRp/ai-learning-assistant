from fastapi import FastAPI
from app.routers import single_pdf_rag, multi_pdf_compare

app = FastAPI(
    title="AI Learning Assistant",
    description="Collection of ML/GenAI small useful apps",
    version="0.1"
)

# Routers
app.include_router(single_pdf_rag.router, prefix="/pdf-rag", tags=["Single PDF RAG"])
app.include_router(multi_pdf_compare.router, prefix="/multi-pdf-compare", tags=["Multi PDF Comparison"])
