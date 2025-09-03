import requests


def clean_text(transcript_url: str) -> str:
    response = requests.get(transcript_url, timeout=10)
    if response.status_code == 200:
        transcript = response.text
        cleaned_transcript = transcript.replace("\n", " ").strip()
        return cleaned_transcript
    else:
        raise Exception("Failed to fetch the transcript.")
