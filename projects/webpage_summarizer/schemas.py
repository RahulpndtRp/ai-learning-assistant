from pydantic import BaseModel

class WebPageSummarizerRequest(BaseModel):
    page_url: str
    query: str
