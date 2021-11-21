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
    query = profiles.find_one({"username": username})
    return query


def get_application(username, app_id):
    """
    Get an application.
    """
    profile = get_profile(username)
    try:
        apps = profile["applications"]
        return apps
    except TypeError:
        return []

    # raise error


def get_post(post_id):
    """
    Get an a post.
    """
    posts = db.get_posts()
    query = posts.find_one({"postId": post_id})
    return query
    # raise error


def main():
    print("Hello class!")  # check if main even runs!

    # d1 = get_profile("momin")
    # d2 = get_application("amadou", 1)
    # d3 = get_post(1)
    # print(d1,d2,d3)
    return 0


if __name__ == "__main__":
    main()
