import logging

from fastapi import APIRouter, HTTPException, Query

from services.summarizer import generate_summary
from services.text_cleaner import clean_text
from services.transcriber import get_transcription

router = APIRouter()


@router.get("/summarize/")
async def summarize(
    youtube_url: str = Query(..., description="YouTube video URL"),
    style: str = Query("paragraph", description="Summary style: 'paragraph' or 'bullet'"),
):
    try:
        transcript_url = get_transcription(youtube_url)
        transcript_text = clean_text(transcript_url)
        summary = generate_summary(transcript_text, style)
        return {"summary": summary}
    except Exception as e:
        logging.error(f"Summarization error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
