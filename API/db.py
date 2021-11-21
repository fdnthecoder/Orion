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
# turn this to true when database connection is successfull.
DATABASE_CONNECTED = False # move to environment variable

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
        "email": input("Enter an email: "),
        "applications": 
            {
             "appId": 1,
             "company": "Facebook",
             "level": "Entry Level",
             "url": "https://www.facebookcareers.com/jobs/213402246952404/",
             "title": "Software Engineer, University Grad",
             "applied": True,
             "date_applied": "6/28/21"
            },
    })

def populate_posts(collection):
    # populating posts with mock data (FUNCTION SOLELY FOR TESTING)
    collection.insert_one({
        "postId": 2,
        "company": "Google",
        "level": "Internship",
        "url": "https://careers.google.com/jobs/results/115615177363071686-software-engineering-intern-bachelors-summer-2022/?utm_campaign=google_jobs_apply&utm_medium=organic&utm_source=google_jobs_apply",
        "title": "Software Engineering Intern, Bachelor's, Summer 2022"
    })

def get_profiles():
    """
    Get the list of posts.
    """
    db = get_database() 
    return db['profiles']

    # get posts from database here momin using get_database()

def get_posts():
    """
    Get the list of posts.
    """
    db = get_database() 
    return db['postings']

    # get posts from database here momin using get_database()

# def get_applications():
#     """
#     Get the list of applications.
#     """
#     db = get_database()
#     return db['applications']

def get_database():
    # Create a connection using MongoClient.
    try:
        client = MongoClient(CONNECTION_STRING)
        db = client['orion']
        DATABASE_CONNECTED = True
        return db
    except:
        return load_from_file(APPLICATIONS_FILE)


get_posts().drop()
populate_posts(get_posts())

# populate_profiles(get_profiles())
