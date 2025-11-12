# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**EpisodeDL** is a Python package that downloads podcast episodes from RSS feeds. It provides three core functions:
- `get_episodes()` - Parses an RSS feed and returns a list of episodes using feedparser
- `get_audio_file()` - Extracts the audio URL from an episode's links
- `download_audio_file()` - Downloads an audio file to disk using requests with streaming

The project is a minimal, focused tool with no complex architecture - just a simple module with three utility functions that work together.

## Development Setup

### Requirements
- Python 3.14+
- [uv](https://docs.astral.sh/uv/) (fast Python package installer, recommended)

### Install Dependencies

**Using uv (recommended):**
```bash
uv pip install -e ".[dev]"
```

**Using pip:**
```bash
pip install -e ".[dev]"
```

The project uses:
- `feedparser` - RSS feed parsing
- `requests` - HTTP requests for downloading files
- `pytest` - Testing framework (dev dependency)

### Common Commands

**Run tests:**
```bash
pytest
```

**Run a specific test:**
```bash
pytest -v path/to/test_file.py::test_function_name
```

**Install the package locally (editable mode):**
```bash
uv pip install -e ".[dev]"
```

## Code Structure

- `episode_dl/__init__.py` - Module entry point that exports the three main functions
- `episode_dl/feed.py` - Contains the implementation of `get_episodes()`, `get_audio_file()`, and `download_audio_file()`

## Important Notes

- The `download_audio_file()` function uses streaming to handle large files efficiently (8KB chunks)
- The module is designed to be lightweight with no external service dependencies beyond the RSS feed and download URLs
- Dependencies are now managed via `pyproject.toml` (modern Python packaging standard)
