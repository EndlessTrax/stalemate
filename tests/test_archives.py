import pytest
import requests
from stalemate.endpoints import archives_url


def test_is_valid_url():
    username = "endlesstrax"
    r = requests.get(archives_url.format(username))
    assert r.status_code == 200

