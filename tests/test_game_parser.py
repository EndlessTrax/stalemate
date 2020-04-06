import pytest
import json
from stalemate.game_parser import (
    get_game_eco, eco_played_totals, game_result, eco_win_lose_draw_totals
    )


user = 'endlesstrax'

with open('game_data/2008-07.json', 'r', encoding='utf-8') as game_file:
    games = json.load(game_file)


def test_get_game_eco():
    game = games[0]
    eco = get_game_eco(game)
    assert eco == "C23"


def test_eco_played_totals():
    sorted_list = eco_played_totals('game_data')
    assert isinstance(sorted_list, list)
    assert sorted_list[0] != None


def test_game_result():
    result = game_result(game=games[0], user=user)
    assert result == "checkmated"


def test_eco_win_lose_draw_totals():
    eco_dict = eco_win_lose_draw_totals("A00", "game_data")
    assert isinstance(eco_dict, dict)
    assert eco_dict.get("ECO") == "A00"