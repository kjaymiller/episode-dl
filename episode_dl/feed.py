import feedparser
import requests
from pathlib import Path


def get_episodes(rss_feed: str, count: int=-1):
    """Returns a list of all the episode items"""
    p = feedparser.parse(rss_feed)
    return [episode for episode in p['items']]


def get_audio_file(episode):
    """Returns the url for the episode item requested"""
    for link in episode['links']:
        if (url:=link)['type'] == 'audio/mpeg':
            return url['href']


def download_audio_file(*, url:str, path:str='./', filename:str=''):
    p = Path(path)
    p.mkdir(exist_ok=True)

    with requests.get(url, stream=True) as r:
        r.raise_for_status()

        filepath = p.joinpath(filename)
        with open(filepath, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

        return filepath

