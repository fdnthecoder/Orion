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
    query = profiles.find_one({}, {"username": username})
    return query


def get_application(app_id):
    """
    Get an application.
    """
    applications = db.get_applications()
    for app, value in applications.items():
        if value[APP_ID] == app_id:
            return value
    # raise error


def get_post(post_id):
    """
    Get an a post.
    """
    applications = db.get_posts()
    for post, value in applications.items():
        if value[POST_ID] == post_id:
            return value
    # raise error


def main():
    print("Hello class!")  # check if main even runs!
    return 0


if __name__ == "__main__":
    main()
