from pydantic import BaseModel

class YouTubeSummarizerRequest(BaseModel):
    video_url: str
    query: str

class YouTubeSummarizerResponse(BaseModel):
    answer: str
