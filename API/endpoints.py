"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
from http import HTTPStatus
from API import db
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restx import Resource, Api  # fields

app = Flask(__name__, static_folder='../React/build', static_url_path="")
api = Api(app)
DEMO_ID = 0
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
    def get(self):
        """Create an applications"""
        return {APPLICATION_MENU_ROUTE: 'GET'}


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
        return db.get_database()

    def delete(self):
        """
        delete an application you posted on the the board
        """
        return {APPLICATION_MENU_ROUTE: 'DELETE'}


@api.route('/user')
class create_user(Resource):
    """
    Get a specific profile
    """
    def get(self):
        """
        GEt a user profile information.
        """
        return {USER_MENU_ROUTE: 'LOGIN'}

    def post(self):
        """
        Sign up.
        """
        data = request.get_json()
        print(data)
        response = {
            USER_MENU_ROUTE: 'CREATE',
            username: data.get("username"),
            password: data.get("password"),
            status: 200,
        }
        return jsonify(data)

    def put(self):
        """
        Edit a profile user profile.
        """
        return {USER_MENU_ROUTE: 'EDITED'}

    def delete(self):
        """
        Delete a user
        """
        return {USER_MENU_ROUTE: "DELETED"}


@api.route('/user/logout')
class user_logout(Resource):
    def post(self):
        return {USER_MENU_ROUTE: 'LOGOUT'}
