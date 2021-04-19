"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""
import os
import json

#HEROKU_HOME = '/app'
#GAME_HOME = os.getenv("GAME_HOME", HEROKU_HOME)

# NEED TO MAKE EDITS TO THE SPECIFIC json based on which json file we create
#DATA_DIR = f'{GAME_HOME}/data'
#MAIN_MENU_JSON = DATA_DIR + '/' + 'main_menu.json'
#GAMES_MENU_JSON = DATA_DIR + '/' + 'games_menu.json'
#CREATE_GAME_JSON = DATA_DIR + '/' + 'create_game.json'
#CREATE_GAME_MENU_JSON = DATA_DIR + '/' + 'create_game_menu.json'
#GAMES_JSON = DATA_DIR + '/' + 'games.json'

#NAME = 'name'

def save_to_file(file, json_data):
    #Taken from prof Callahan Game API 
    print(f"Going to save to {file}")
    with open(file, 'w') as f:
        f.write(json.dumps(json_data))


def load_from_file(file):
    #Taken from prof Callahan Game API 
    """
    Right now we store all of our data in ordinary files.
    But let's hide that fact inside this module.
    """
    print(f"Going to open {file}")
    try:
        with open(file) as file:
            return json.loads(file.read())
    except FileNotFoundError:
        return None
