import pytest
import requests
from stalemate.endpoints import archives_url
from stalemate.archives import build_archive_endpoint, fetch_archives_list


test_username = "endlesstrax"

def test_is_valid_url():
    r = requests.get(archives_url.format(test_username))
    assert r.status_code == 200


def test_build_archive_endpoint():
    url = build_archive_endpoint(test_username)
    assert url == f"https://api.chess.com/pub/player/{test_username}/games/archives"
    assert url == "https://api.chess.com/pub/player/endlesstrax/games/archives"


def test_fetch_archives_list():
    url = build_archive_endpoint(test_username)
    archives = fetch_archives_list(url)
    assert isinstance(archives, list)


