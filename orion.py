# from API.endpoints import user
from API import db

SUCCESS = 0
ERROR = 1
POST_ID = "postID"
APP_ID = "appID"


def get_profile(username):
    """
    Get a user profile by username.
    """
    profiles = db.get_profiles()
    for profile in profiles:
        if profile["username"] == username:
            return profile
    return {"status": "Does not exist"}


def get_post(post_id):
    """
    Get an a post.
    """
    posts = db.get_posts()
    for post in posts:
        print((post["postId"]), post_id)
        if post["postId"] == post_id:
            return post
    return {"status": "Does not exist"}
    # raise error


def sign_in(username, password):
    """
    Sign in
    """
    if authenticate(username, password):
        return {"Status": "exist"}
    else:
        return {"Status": "Does not exist"}


def authenticate(username, password):
    """
    Authenticate a user
    """
    profiles = db.get_profiles()
    return username in profiles


def user_exist(username):
    """
    check if user exist
    """
    return "status" in get_profile(username)


def sign_up(email, username, password):
    if user_exist(username):
        return {"status": "exist"}
    else:
        data = {
            "username": username,
            "email": email,
            "password": password,
            "applications": []
        }
        db.add_user(data)
        return {"Status": "Success"}


def main():
    return 0


if __name__ == "__main__":
    main()
