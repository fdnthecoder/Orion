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


def get_application(app_id):
    """
    Get an application.
    """
    applications = db.get_applications()
    for app in applications:
        if app[APP_ID] == app_id:
            return app


def get_post(post_id):
    """
    Get an a post.
    """
    applications = db.get_applications()
    for post in applications:
        if post[POST_ID] == post_id:
            return post


def main():
    print("Hello class!")  # check if main even runs!
    return 0


if __name__ == "__main__":
    main()
