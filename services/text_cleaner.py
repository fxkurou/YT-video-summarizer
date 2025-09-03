import requests


def clean_text(transcript_url: str) -> str:
    """
    Fetch and clean the transcript text from the given URL.
    :param transcript_url:
    :return: Cleaned transcript text
    """
    response = requests.get(transcript_url, timeout=10)
    if response.status_code == 200:
        transcript = response.text
        cleaned_transcript = transcript.replace("\n", " ").strip()
        return cleaned_transcript
    else:
        raise Exception("Failed to fetch the transcript.")
