"""
TODO:
"""

import os
import re
import json



def get_game_eco(game):
    """
    TODO:
    """
    pgn = game['pgn']
    p = re.compile('ECO "')
    search_eco = p.search(pgn)

    if search_eco:
        positions = search_eco.span()
        start_position = positions[1]
        end_position = start_position + 3
        eco = pgn[start_position:end_position]
    else:
        eco = "None"

    return eco


def eco_played_totals(files_dir):
    played_ecos = dict()
    list_of_files = os.listdir(files_dir)

    for game_file in list_of_files:
        with open(f"{files_dir}/{game_file}", 'r', encoding='utf-8') as f:
            games_in_file = json.load(f)

            for game in games_in_file:
                game_eco = get_game_eco(game)
                
                if game_eco in played_ecos:
                    val = played_ecos.get(game_eco)
                    played_ecos[game_eco] = val + 1
                else:
                    played_ecos[game_eco] = 1

    sorted_ecos = sorted(played_ecos.items(), key=lambda x: x[1], reverse=True)

    return sorted_ecos