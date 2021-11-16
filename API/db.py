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
CONNECTION_STRING = "mongodb+srv://mainuser:crepe2021@cluster0.sqob6.mongodb.net/test"

DATA_DIR = f'{ORION_HOME}/data'
APPLICATIONS_FILE = f"{DATA_DIR}/applications.json"
PROFILES_FILE = f"{DATA_DIR}/profiles.json"
POSTS_FILE = f"{DATA_DIR}/posts.json"
# turn this to true when databse connection is successfull.
DATABASE_CONNECTED = True

# Provide the mongodb atlas url to connect python to mongodb using pymongo

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
        return "Could not open json file"

def populate_profiles(collection):
    # populating profiles with mock data (FUNCTION SOLELY FOR TESTING)
    collection.insert_one({
        "username": input("Enter a username: "),
        "password": input("Enter a password: "),
        "email": input("Enter an email: ")
    })

def populate_posts(collection):
    # populating posts with mock data (FUNCTION SOLELY FOR TESTING)
    collection.insert_one({
        "company": "Google",
        "level": "Internship",
        "url": "https://careers.google.com/jobs/results/115615177363071686-software-engineering-intern-bachelors-summer-2022/?utm_campaign=google_jobs_apply&utm_medium=organic&utm_source=google_jobs_apply",
        "title": "Software Engineering Intern, Bachelor's, Summer 2022"
    })
    

def get_profiles():
    """
    Get the list of profiles.
    """
    if not DATABASE_CONNECTED:
        return load_from_file(PROFILES_FILE)
    db = get_database()
    return db['profiles']
    
    # get profiles from data base here momin using get_database()

def get_posts():
    """
    Get the list of posts.
    """
    if not DATABASE_CONNECTED:
        return load_from_file(POSTS_FILE)
    db = get_database() 
    return db['profiles']

    # get posts from database here momin using get_database()

def get_applications():
    """
    Get the list of applications.
    """
    if not DATABASE_CONNECTED:
        return load_from_file(APPLICATIONS_FILE)
        # get applications from database here momin using get_database()
    db = get_database()
    return db['applications']

def get_database():
    # Create a connection using MongoClient.
    if not DATABASE_CONNECTED:
        return load_from_file(APPLICATIONS_FILE)
    client = MongoClient(CONNECTION_STRING)
    db = client['orion']
    return db

populate_posts(get_collection('postings'))
populate_profiles(get_collection('profiles'))
