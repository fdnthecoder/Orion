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
    return profiles[username]


def get_application(app_id, username):
    """
    Get an application.
    """
    applications = db.get_applications()[username]

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
    return 0


if __name__ == "__main__":
    main()
