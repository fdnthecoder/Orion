"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""
import os
import json
from pymongo import MongoClient
from bson.json_util import dumps, loads
HEROKU_HOME = '/app'
ORION_HOME = os.getenv("ORION_HOME", HEROKU_HOME)


DATA_DIR = f'{ORION_HOME}/data'
APPLICATIONS_FILE = f"{DATA_DIR}/applications.json"
PROFILES_FILE = f"{DATA_DIR}/profiles.json"
POSTS_FILE = f"{DATA_DIR}/posts.json"
# turn this to true when databse connection is successfull.
DATABASE_CONNECTED = False

# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb+srv://mainuser:crepe2021@cluster0.sqob6.mongodb.net/test?authSource=admin&replicaSet=atlas-3686at-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"


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
        db = get_database()
        profiles = db["profiles"]

        # Now creating a Cursor instance
        # using find() function
        cursor = profiles.find()

        # Converting cursor to the list 
        # of dictionaries
        list_cur = list(cursor)

        # Converting to the JSON
        json_data = loads(dumps(list_cur, indent = 2))

        return json_data
        
        # get_database, get data needed, turn into json and return

def get_profile(username):
    """
    Get a user profile by username.
    """
    if not DATABASE_CONNECTED:
        profiles = get_profiles()
        for profile in profiles:
            if profile["username"] == username:
                return profile
        return {"status": "Does not exist"}
    else:
        db = get_database()
        profiles = db["profiles"]

        # Now creating a Cursor instance
        # using find() function

        user_query = {"username": username}
        cursor = profiles.find(user_query)

        # Converting cursor to the list 
        # of dictionaries
        list_cur = list(cursor)

        # Converting to the JSON
        json_data = loads(dumps(list_cur, indent = 2))
        
        return json_data[0]
        # get_database, get data needed, turn into json and return

def get_posts():
    """
    Get the list of posts.
    """
    if not DATABASE_CONNECTED:
        return load_from_file(POSTS_FILE)
    else:
        db = get_database()
        profiles = db["posts"]

        # Now creating a Cursor instance
        # using find() function
        cursor = profiles.find()

        # Converting cursor to the list 
        # of dictionaries
        list_cur = list(cursor)

        # Converting to the JSON
        json_data = loads(dumps(list_cur, indent = 2))

        return json_data

def get_post(post_id):
    """
    Get an a post.
    """
    if not DATABASE_CONNECTED:
        posts = get_posts()
        for post in posts:
            if post["postId"] == post_id:
                return post
        return {"status": "Does not exist"}
    else:
        db = get_database()
        posts = db["posts"]

        # Now creating a Cursor instance
        # using find() function

        post_query = {"postid": post_id}
        cursor = posts.find(post_query)

        # Converting cursor to the list 
        # of dictionaries
        list_cur = list(cursor)

        # Converting to the JSON
        json_data = loads(dumps(list_cur, indent = 2))
        
        return json_data[0]
        # get_database, get data needed, turn into json and return

def add_user(data):
    """
    Add a new user
    """

    if not DATABASE_CONNECTED:
        pass
        # find a way to add the data into local json profiles
    else:
        db = get_database()
        profiles = db["profiles"]
        profiles.find({"username": data["username"]})
        

        # add the profile into the database


def add_application(application, username):
    """
    add a new application to a user's applications
    """
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


def update_status(app_id, status, username):
    """
    upate the status of an application
    """
    if not DATABASE_CONNECTED:
        profiles = load_from_file(PROFILES_FILE)
        # find the profile
        for profile in profiles:
            if profile["username"] == username:
                for application in profile["applications"]:
                    if application["postId"] == app_id:
                        application["status"] = status
        # add the profile back to our jason database
        save_to_file(PROFILES_FILE, profiles)
    else:
        pass
        # get the application in user and change the status


def add_post(new_post):
    """
    add a new post to the list of posts
    """
    if not DATABASE_CONNECTED:
        posts = get_posts()
        posts.append(new_post)
        save_to_file(POSTS_FILE, posts)
    else:
        pass
        # add this new post to the database list of posts


def authenticate(username, password):
    """
    Authenticate a user
    """
    if not DATABASE_CONNECTED:
        profiles = get_profiles()
        for users in profiles:
            if users["username"] == username:
                return True
        return False
    else:
        # authenticate from database?
        pass