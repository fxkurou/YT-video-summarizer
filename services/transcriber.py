import logging

import yt_dlp


def get_transcription(video_url: str) -> str:
    """
    Fetches the transcription URL of a YouTube video using yt-dlp.
    :param video_url:
    :return: URL of the transcription file
    """
    ydl_opts = {
        "skip_download": True,
        "writesubtitles": True,
        "subtitleslangs": ["en", "en.*"],
        "quiet": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        subtitles = info.get("subtitles", {})
        logging.debug(subtitles)
        if "en" in subtitles:
            return subtitles["en"][0]["url"]
        else:
            raise Exception("No subtitles found for this video.")
