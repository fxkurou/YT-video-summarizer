from pydantic import BaseModel


class VideoSummaryRequest(BaseModel):
    url: str
    style: str = "paragraph"


class VideoTranscriptResponse(BaseModel):
    transcript: str
