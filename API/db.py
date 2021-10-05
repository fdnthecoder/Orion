"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""
# import os
import json
from pymongo import MongoClient
# HEROKU_HOME = '/app'
# GAME_HOME = os.getenv("GAME_HOME", HEROKU_HOME)

# NEED TO MAKE EDITS TO THE SPECIFIC json based on which json file we create
# DATA_DIR = f'{GAME_HOME}/data'
# MAIN_MENU_JSON = DATA_DIR + '/' + 'main_menu.json'
# GAMES_MENU_JSON = DATA_DIR + '/' + 'games_menu.json'
# CREATE_GAME_JSON = DATA_DIR + '/' + 'create_game.json'
# CREATE_GAME_MENU_JSON = DATA_DIR + '/' + 'create_game_menu.json'
# GAMES_JSON = DATA_DIR + '/' + 'games.json'

# NAME = 'name'

# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = """mongodb+srv://mainuser:crepe2021@cluster0.
sqob6.mongodb.net/test?authSource=admin&replicaSet=atlas-3686at-
shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"""


def save_to_file(file, json_data):
    """Save data into a json file."""
    print(f"Going to save to {file}")
    with open(file, 'w') as f:
        f.write(json.dumps(json_data))


def load_from_file(file):
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


def populate_db(collection):
    # populating db with mock data
    collection.insert_one({
        "id": 1,
        "username": input("Enter a username: "),
        "password": input("Enter a password: "),
        "group": [
            "Amadou",
            "Jamie",
            "Wei",
            "Momin"
        ]
    })


def get_database():
    # Create a connection using MongoClient.
    client = MongoClient(CONNECTION_STRING)
    db = client['orion']
    coll = db['test']
    # populate_db(coll)
    for elem in coll.find({}):
        print(elem)
    return db


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    dbname = get_database()
