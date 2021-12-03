# from API.endpoints import user
from API import db

ERROR = 1
POST_ID = "postID"
APP_ID = "appID"
EXIST_RES = {"Status": "Does exist"}
DOES_NOT_EXIST_RES = {"Status": "Does not exist"}
ERROR = {"Status": "Internal Error"}
SUCCESS = {"Status": "Success"}
FAILED = {"Status": "Failed"}


def get_profile(username):
    """
    Get a user profile by username.
    """
    try:
        return db.get_profile(username)
    except IndexError:
        return DOES_NOT_EXIST_RES


def get_post(post_id):
    """
    Get an a post.
    """
    try:
        return db.get_post(post_id)
    except IndexError:
        return DOES_NOT_EXIST_RES


def sign_in(username, password):
    """
    Sign in
    """
    if db.authenticate(username, password):
        return EXIST_RES
    else:
        return DOES_NOT_EXIST_RES


def user_exist(username):
    """
    check if user exist
    """
    return DOES_NOT_EXIST_RES != get_profile(username)


def sign_up(email, username, password):
    """
    a function to sign up a new user.
    """
    if user_exist(username):
        return EXIST_RES
    else:
        data = {
            "username": username,
            "email": email,
            "password": password,
            "applications": []
        }
        db.add_user(data)
        return SUCCESS


def add_application(app, username):
    """
    add a new application for a specific user.
    """
    try:
        db.add_application(app, username)
        return SUCCESS
    except BaseException:
        return FAILED


def delete_application(post_id, username):
    try:
        db.delete_application(post_id, username)
        return SUCCESS
    except BaseException:
        return FAILED


def update_status(app_id, status, username):
    """
    a function to update the status of a an application
    """
    try:
        db.update_status(app_id, status, username)
        return SUCCESS
    except BaseException:
        return FAILED


def add_post(company, name, level, url, description):
    """
    a user post a new job listing
    """
    try:
        new_post = {
            "postID": db.last_post_ID(),
            "company": company,
            "level": level,
            "url": url,
            "title": name,
            "description": description
        }
        db.add_post(new_post)
        return SUCCESS
    except BaseException:
        return FAILED


def main():
    return 0


if __name__ == "__main__":
    main()
