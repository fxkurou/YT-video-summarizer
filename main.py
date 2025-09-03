from fastapi import FastAPI

from api.endpoints import video

app = FastAPI()

app.include_router(video.router, prefix="/video", tags=["video"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the YouTube Video Summarizer API"}
