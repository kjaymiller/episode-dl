# EpisodeDL

__Download Podcast Episodes from RSS Feeds__

## Overview

EpisodeDL is a lightweight Python package for downloading podcast episodes from RSS feeds. It provides three core functions that work together to fetch episodes and download their audio files.

## Features

- **Parse RSS feeds** - Extract podcast episodes from any RSS feed
- **Extract audio URLs** - Automatically identify audio file links in episode data
- **Download episodes** - Efficiently download audio files with streaming support for large files

## Installation

### Requirements
- Python 3.14+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Using uv (recommended)
```bash
uv pip install -e ".[dev]"
```

### Using pip
```bash
pip install -e ".[dev]"
```

## Usage

```python
from episode_dl import get_episodes, get_audio_file, download_audio_file

# Parse RSS feed
episodes = get_episodes('https://example.com/podcast/feed.xml')

# Get audio URL from an episode
audio_url = get_audio_file(episodes[0])

# Download the audio file
download_audio_file(audio_url, 'episode.mp3')
```

## Core Functions

- `get_episodes(feed_url)` - Parses an RSS feed and returns a list of episodes
- `get_audio_file(episode)` - Extracts the audio URL from an episode's links
- `download_audio_file(url, filename)` - Downloads an audio file to disk using streaming

## Development

### Run Tests
```bash
pytest
```

### Run Specific Test
```bash
pytest -v path/to/test_file.py::test_function_name
```

## Dependencies

- `feedparser` - RSS feed parsing
- `requests` - HTTP requests for downloading files
- `pytest` - Testing framework (dev only)

## License

MIT

