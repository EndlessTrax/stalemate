import json
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


# TODO: ? Might need removing later. 
def save_games_to_file(url):
    archive_date = url[-7:].replace("/", "-")
    r = requests.get(url).json()

    with open(f'game_data/{archive_date}.json', 'w', encoding='utf-8') as file:
        json.dump(r['games'], file)
