"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask import Flask
from flask_restx import Resource, Api, fields
from source.db import fetch_games

app = Flask(__name__)
api = Api(app)

HELLO = 'hello'
AVAILABLE = 'Available endpoints:'
MAIN_MENU = "Main Menu"


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
        return {HELLO: 'world'}


@api.route('/endpoints/list')
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        epts = sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {AVAILABLE: epts}


@api.route('/menus/main')
class MainMenu(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        return {MAIN_MENU: "This will contain the menu."}


@api.route('/games/list')
class Games(Resource):
    """
    This class supports fetching a list of all games.
    """
    def get(self):
        """
        This method returns all games.
        """
        return fetch_games()


user = api.model("user", {
    "name": fields.String("User name.")
})


@api.route('/games/join/<int:game_id>')
class JoinGame(Resource):
    """
    This endpoint allows a user to join an existing game.
    """
    @api.expect(user)
    def put(self, game_id):
        return "Game joined."


@api.route('/games/create')
class CreateGame(Resource):
    """
    This class allows the user to create a new game.
    We will be passing in some sort of game object as a
    parameter. Details unknown at present.
    """
    def post(self):
        """
        This method returns all games.
        """
        return "Game created."
