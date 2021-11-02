"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from API import db
from flask import Flask
from flask_restx import Resource, Api  # fields
# from werkzeug.exceptions import NotFound
# import textapp.text_app as ta

# import API.db as db

app = Flask(__name__, static_folder='../React/build', static_url_path="/")
api = Api(app)

HELLO = 'hello'
INDEX_ROUTE = 'index.html'
AVAILABLE = 'Available endpoints:'
HOME_MENU = "HOME Menu"
HOME_MENU_ROUTE = '/menus/HOME'
MENU_URL = "MenuURL"
APPLICATIONS = "applications"
APPLICATION_MENU_ROUTE = '/menus/APPLICATION'
CREATE_APPLICATION_MENU_ROUTE = '/menus/create_APPLICATION'
USER_MENU_ROUTE = '/menus/user'

@api.route('/')
class index_check(Resource):
    """Purpose of checking whether heroku connection worked"""
    def get(self):
        return api.send_static_file('index.html')
@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

@api.route('/hello')
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """
    def get(self):
        """
        A trivial endpoint to see if the server is running.
        It just answers with "hello world."
        """
        return {HELLO: 'Hello World'}


@api.route('/APPLICATION/add')
class add_application(Resource):
    # add application to a kandban board from a post
    def get(self):
        return {APPLICATION_MENU_ROUTE: 'ADD'}


@api.route('/APPLICATION/create')
class create_application(Resource):
    # create applications.
    def get(self):
        return {APPLICATION_MENU_ROUTE: 'CREATE'}


class post_application(Resource):
    # post an application on the board
    def get(self):
        return {APPLICATIONS: "application create"}


@api.route('/APPLICATION/list')
class list_applications(Resource):
    def get(self):
        return db.get_database()


@api.route('/APPLICATION/delete')
class delete_application(Resource):
    def get(self):
        return {APPLICATION_MENU_ROUTE: 'DELETE'}


@api.route('/user/create')
class create_user(Resource):
    def get(self):
        return {USER_MENU_ROUTE: 'CREATE'}


@api.route('/user/login')
class user_login(Resource):
    def get(self):
        return {USER_MENU_ROUTE: 'LOGIN'}


@api.route('/user/logout')
class user_logout(Resource):
    def get(self):
        return {USER_MENU_ROUTE: 'LOGOUT'}

# comment and review, different routes?
if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))
