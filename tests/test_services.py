from unittest.mock import MagicMock, patch

import pytest

from services.summarizer import generate_summary
from services.text_cleaner import clean_text
from services.transcriber import get_transcription


@patch("services.transcriber.yt_dlp.YoutubeDL")
def test_get_transcription_success(mock_yt_dlp):
    mock_ydl = MagicMock()
    mock_yt_dlp.return_value.__enter__.return_value = mock_ydl
    mock_ydl.extract_info.return_value = {"subtitles": {"en": [{"url": "http://example.com/subs"}]}}
    url = "http://youtube.com/video"
    result = get_transcription(url)
    assert result == "http://example.com/subs"


@patch("services.transcriber.yt_dlp.YoutubeDL")
def test_get_transcription_no_subtitles(mock_yt_dlp):
    mock_ydl = MagicMock()
    mock_yt_dlp.return_value.__enter__.return_value = mock_ydl
    mock_ydl.extract_info.return_value = {"subtitles": {}}
    url = "http://youtube.com/video"
    with pytest.raises(Exception, match="No subtitles found for this video."):
        get_transcription(url)


@patch("services.text_cleaner.requests.get")
def test_clean_text_success(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = "line1\nline2"
    mock_get.return_value = mock_response
    url = "http://example.com/transcript"
    result = clean_text(url)
    assert result == "line1 line2"


@patch("services.text_cleaner.requests.get")
def test_clean_text_failure(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response
    url = "http://example.com/transcript"
    with pytest.raises(Exception, match="Failed to fetch"):
        clean_text(url)


@patch("services.summarizer.openai.chat.completions.create")
def test_generate_summary_success(mock_create):
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="summary"))]
    mock_create.return_value = mock_response
    result = generate_summary("some text", "concise")
    assert result == "summary"
