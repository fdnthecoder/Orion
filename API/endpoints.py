"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
from http import HTTPStatus
from API import db
import orion
from flask import Flask, request  # jsonify
from flask_cors import CORS
from flask_restx import Resource, Api  # fields

app = Flask(__name__, static_folder='../React/build', static_url_path="")
api = Api(app)
DEMO_ID = 0
DEMO_USERNAME = "diallodb"
CORS(app)

HELLO = 'hello'
AVAILABLE = 'Available endpoints:'
HOME_MENU = "HOME Menu"
HOME_MENU_ROUTE = '/menus/HOME'
MENU_URL = "MenuURL"
APPLICATIONS = "applications"
APPLICATION_MENU_ROUTE = '/menus/APPLICATION'
CREATE_APPLICATION_MENU_ROUTE = '/menus/create_APPLICATION'
USER_MENU_ROUTE = '/menus/user'


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        """
        A trivial endpoint to see if the server is running.
        It just answers with "hello world."
        """
        return {HELLO: 'Hello World'}


@api.route('/endpoints')
class Endpoints(Resource):
    """
    A class to deal with our endpoints themselves.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        """
        List our endpoints.
        """
        endpoints = sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}


@api.route('/APPLICATION')
class Application(Resource):
    """
    We can use this class to deal with applications.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def post(self):
        """add application for a user"""
        return orion.add_application(username)


@api.route('/BOARD')
class Board(Resource):
    """
    We can use this class to deal with applications.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def post(self):
        """
        Post an application to the applications board.
        """
        return {APPLICATIONS: "application create"}

    def get(self):
        """
        Get a list of posted applications
        """
        return db.get_posts()

    def delete(self):
        """
        delete an application you posted on the the board
        """
        return {APPLICATION_MENU_ROUTE: 'DELETE'}


@api.route('/profile')
class profile(Resource):
    """
    Get a specific profile
    """
    @api.doc(params={'username': 'username of the profile'})
    def get(self):
        """
        get a user profile information.
        """
        username = request.args.get('username')
        return orion.get_profile(username)

    def put(self):
        """
        Edit a profile user profile. Provide all the profile information.
        username, password etc.
        """
        return {USER_MENU_ROUTE: 'EDITED'}

    def delete(self):
        """
        Delete a user
        """
        return {USER_MENU_ROUTE: "DELETED"}


@api.route('/user/signup')
class user(Resource):

    def post(self):
        """
        Sign up
        """
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        email = data["email"]
        return orion.sign_up(email, username, password)


@api.route('/user/signin')
class user(Resource):
    def get(self):
        """
        Sign in
        """
        data = request.get_json()
        # get from payload instead of command line
        username = data["username"]
        password = data["password"]
        return orion.sign_in(username, password)
