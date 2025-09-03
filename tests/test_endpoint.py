from unittest.mock import patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from api.endpoints.video import router

app = FastAPI()
app.include_router(router)


@pytest.fixture
def client():
    return TestClient(app)


@patch("api.endpoints.video.get_transcription")
@patch("api.endpoints.video.clean_text")
@patch("api.endpoints.video.generate_summary")
def test_summarize_success(mock_summary, mock_clean, mock_transcribe, client):
    mock_transcribe.return_value = "http://transcript.url"
    mock_clean.return_value = "transcript text"
    mock_summary.return_value = "summary result"

    response = client.get("/summarize/", params={"youtube_url": "http://youtube.com/video", "style": "paragraph"})
    assert response.status_code == 200
    assert response.json() == {"summary": "summary result"}


@patch("api.endpoints.video.get_transcription", side_effect=Exception("No subtitles found for this video."))
def test_summarize_failure(mock_transcribe, client):
    response = client.get("/summarize/", params={"youtube_url": "http://youtube.com/video", "style": "paragraph"})
    assert response.status_code == 400
    assert response.json()["detail"] == "No subtitles found for this video."
