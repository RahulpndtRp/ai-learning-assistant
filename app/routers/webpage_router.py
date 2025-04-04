from fastapi import APIRouter
from projects.webpage_summarizer.schemas import WebPageSummarizerRequest
from projects.webpage_summarizer.services import rag_chain

router = APIRouter()

@router.post("/webpage-summarizer/")
async def summarize_webpage(request: WebPageSummarizerRequest):
    inputs = {
        "page_url": request.page_url,
        "query": request.query
    }
    output = rag_chain.invoke(inputs)
    return {"answer": output}
