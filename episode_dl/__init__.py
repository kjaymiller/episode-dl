from .feed import get_episodes, get_audio_file, download_audio_file

try:
    from ._version import __version__
except ImportError:
    __version__ = "unknown"

__all__ = ["get_episodes", "get_audio_file", "download_audio_file", "__version__"]
