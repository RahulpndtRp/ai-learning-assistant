from fastapi import APIRouter
from projects.youtube_summarizer.schemas import YouTubeSummarizerRequest, YouTubeSummarizerResponse
from projects.youtube_summarizer.services import generate_answer

router = APIRouter()

@router.post("/youtube-summarizer", response_model=YouTubeSummarizerResponse)
async def youtube_summarizer(request: YouTubeSummarizerRequest):
    result = generate_answer(request)
    return result
