"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask import Flask, render_template
#from flask_restx import Resource, Api, fields
from werkzeug.exceptions import NotFound
# import textapp.text_app as ta

# import API.db as db

app = Flask(__name__)
#api = Api(app)

HELLO = 'hello'
AVAILABLE = 'Available endpoints:'
MAIN_MENU = "Main Menu"
MAIN_MENU_ROUTE = '/menus/main'
MENU_URL = "MenuURL"
GAMES_MENU_ROUTE = '/menus/games'
CREATE_GAME_MENU_ROUTE = '/menus/create_game'


@app.route('/hello')
def HelloWorld():
    return "Hello World"


'''
class HelloWorld():
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
'''


