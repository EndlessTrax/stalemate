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


def game_result(game, user):
    try:
        if game['white']['username'].lower() == user:
            result = game['white']['result']
            return result
        elif game['black']['username'].lower() == user:
            result = game['black']['result']
            return result

    except Exception as e:
        raise(e)



def eco_win_lose_draw_totals(eco, files_dir):
    eco_dict = {"ECO": eco, "Won": 0, "Lost": 0, "Drawn": 0}

    list_of_files = os.listdir(files_dir)

    for game_file in list_of_files:
        with open(f"{files_dir}/{game_file}", 'r', encoding='utf-8') as f:
            games_in_file = json.load(f)

            for game in games_in_file:
                game_eco = get_game_eco(game)

                if game_eco == eco:
                    result = game_result(game, 'endlesstrax') #TODO: Remove hardcoded user 

                    if result == 'win':
                        val = eco_dict.get('Won')
                        eco_dict['Won'] = val + 1
                    elif result == 'checkmated' or result == 'resigned':
                        val = eco_dict.get('Lost')
                        eco_dict['Lost'] = val + 1
                    elif result == 'agreed' or result == 'stalemate':
                        val = eco_dict.get('Drawn')
                        eco_dict['Drawn'] = val + 1

    return eco_dict

