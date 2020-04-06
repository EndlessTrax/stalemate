import pytest
import json
from stalemate.game_parser import game_result

with open('game_data/2008-07.json', 'r', encoding='utf-8') as game_file:
    games = json.load(game_file)


user = 'endlesstrax'

def test_game_result():
    result = game_result(game=games[0], user=user)
    assert result == "checkmated"
