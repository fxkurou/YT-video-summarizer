# YT Video Summarizer

A FastAPI-based service that fetches YouTube video subtitles, cleans the transcript, and generates a summary using OpenAI.

## Features

- Extracts subtitles from YouTube videos
- Cleans and processes transcript text
- Summarizes content in paragraph or bullet style

## Project Structure

```
yt-video-summarizer/
├── api/
│   └── endpoints/
│       └── video.py         # FastAPI endpoint for summarization
├── services/
│   ├── transcriber.py       # Fetches YouTube subtitles
│   ├── text_cleaner.py      # Cleans transcript text
│   └── summarizer.py        # Generates summary via OpenAI
├── tests/
│   ├── test_endpoint.py     # Endpoint tests
│   └── test_services.py     # Service function tests
├── pyproject.toml           # Poetry configuration
└── README.md                # Project documentation
```

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/<your-username>/yt-video-summarizer.git
   cd yt-video-summarizer
   ```

2. **Install dependencies:**
   ```sh
   poetry install
   ```

3. **Set environment variables:**
   - Create a `.env` file with your OpenAI API key:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     ```

## Running the Application

Start the FastAPI server with Uvicorn:

```sh
poetry run uvicorn main:app --reload
```

## API Usage

### `GET /summarize/`

**Parameters:**
- `youtube_url` (str, required): YouTube video URL
- `style` (str, optional): `paragraph` or `bullet` (default: `paragraph`)

**Example:**
```
GET /summarize/?youtube_url=https://youtube.com/watch?v=abc123&style=bullet
```

**Response:**
```json
{
  "summary": "..."
}
```

## Testing

Run all tests with coverage:

```sh
poetry run coverage run -m pytest
poetry run coverage report
```

## Pre-commit & Security

- Pre-commit hooks:
  ```sh
  poetry run pre-commit run --all-files
  ```
- Security checks:
  ```sh
  poetry run bandit -r .
  ```

---

For more details, see the source files in the `api/` and `services/` directories.
```
