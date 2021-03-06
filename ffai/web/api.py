"""
==========================
Author: Niels Justesen
Year: 2018
==========================
This module contains functions to communicate with a game host to manage games.
"""

from ffai.web.host import *
from ffai.core.game import *
from ffai.core.load import *
from ffai.ai.bots import *

# Create a game host
host = Host()


def new_game(away_team_id, home_team_id, away_agent=None, home_agent=None, config_name="ff-11.json"):
    assert away_agent is not None
    assert home_agent is not None
    config = get_config(config_name)
    config.fast_mode = False
    ruleset = get_rule_set(config.ruleset, all_rules=False)
    home = get_team_by_id(home_team_id, ruleset)
    away = get_team_by_id(away_team_id, ruleset)
    game_id = str(uuid.uuid1())
    game = Game(game_id, home, away, home_agent, away_agent, config)
    game.init()
    host.add_game(game)
    print("Game created with id ", game.game_id)
    return game


def step(game_id, action):
    game = host.get_game(game_id)
    game.step(action)
    return game


def save_game_exists(name):
    for save in host.get_saved_games():
        if save[1] == name.lower():
            return True
    return False


def save_game(game_id, name):
    name = name.replace("/", "").replace(".", "").lower()
    host.save_game(game_id, name)


def get_game(game_id):
    return host.get_game(game_id)


def load_game(name):
    return host.load_game(name)


def get_games():
    return host.get_games()


def get_saved_games():
    return host.get_saved_games()


def get_teams(ruleset):
    return get_all_teams(ruleset)

