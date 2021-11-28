"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""
import os
import json
from pymongo import MongoClient
HEROKU_HOME = '/app'
ORION_HOME = os.getenv("ORION_HOME", HEROKU_HOME)

DATA_DIR = f'{ORION_HOME}/data'
APPLICATIONS_FILE = f"{DATA_DIR}/applications.json"
PROFILES_FILE = f"{DATA_DIR}/profiles.json"
POSTS_FILE = f"{DATA_DIR}/posts.json"
# turn this to true when databse connection is successfull.
DATABASE_CONNECTED = False

# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = """mongodb+srv://mainuser:crepe2021@cluster0.
sqob6.mongodb.net/test?authSource=admin&replicaSet=atlas-3686at-
shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"""


def get_database():
    # Create a connection using MongoClient.
    client = MongoClient(CONNECTION_STRING)
    db = client['orion']
    return db


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


def get_profiles():
    """
    Get the list of profiles.
    """
    if not DATABASE_CONNECTED:
        return load_from_file(PROFILES_FILE)
    else:
        pass
        # get_database, get data needed, turn into json and return


def get_posts():
    """
    Get the list of posts.
    """
    if not DATABASE_CONNECTED:
        return load_from_file(POSTS_FILE)
    else:
        pass
        # get_database, get data needed, turn into json and return


def add_user(data):
    """
    Add a new user
    """

    if not DATABASE_CONNECTED:
        pass
        # find a way to add the data into local json profiles
    else:
        pass
        # add  the profile into the database


def add_application(application,username):
    if not DATABASE_CONNECTED:
        profiles = load_from_file(PROFILES_FILE)
        # find the profile
        for profile in profiles:
            if profile["username"] == username:
                profile["applications"].append(application)
        # add the profile back to our jason database
        save_to_file(PROFILES_FILE, profiles)
    else:
        pass
        # add the application to a user's profile in data base