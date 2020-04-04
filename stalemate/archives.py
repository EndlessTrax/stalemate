import requests
from stalemate.endpoints import archives_url


def build_archive_endpoint(username):
    """
    TODO:
    """
    url = archives_url.format(username)
    return url


def fetch_archives_list(url):
    """
    TODO:
    """
    response = requests.get(url).json()
    return response['archives']
