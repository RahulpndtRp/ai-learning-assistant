# agentic_rag_router.py

from fastapi import APIRouter
from projects.agentic_rag.services import AgenticRAGService
from projects.agentic_rag.schemas import QueryRequest

router = APIRouter(
    prefix="/agentic-rag",
    tags=["Agentic RAG"]
)

agentic_rag_service = AgenticRAGService()

@router.post("/query")
async def query_agentic_rag(request: QueryRequest):
    result = agentic_rag_service.kickoff_agentic_rag(request.query)
    return {"result": result}
