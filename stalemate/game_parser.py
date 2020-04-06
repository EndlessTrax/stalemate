"""
TODO:
"""

import re


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
