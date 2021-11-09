"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from API import db
from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_restx import Resource, Api  # fields
# from werkzeug.exceptions import NotFound
# import textapp.text_app as ta

# import API.db as db

app = Flask(__name__)
cor = CORS(app)

HELLO = 'hello'
AVAILABLE = 'Available endpoints:'
HOME_MENU = "HOME Menu"
HOME_MENU_ROUTE = '/menus/HOME'
MENU_URL = "MenuURL"
APPLICATIONS = "applications"
APPLICATION_MENU_ROUTE = '/menus/APPLICATION'
CREATE_APPLICATION_MENU_ROUTE = '/menus/create_APPLICATION'
USER_MENU_ROUTE = '/menus/user'



@app.route('/hello')
def hello():
    """
    A trivial endpoint to see if the server is running.
    It just answers with "hello world."
    """
    return {HELLO: 'Hello World'}


@app.route('/APPLICATION/create')
def createApp():
    return {APPLICATION_MENU_ROUTE: 'CREATE'}



@app.route('/APPLICATION/list')
def appList():
    return db.get_database()


@app.route('/APPLICATION/delete')
def deleteApp():
    return {APPLICATION_MENU_ROUTE: 'DELETE'}


@app.route('/user/create')
def createUser():
    return {USER_MENU_ROUTE: 'CREATE'}


@app.route('/user/login')
def login():
    return {USER_MENU_ROUTE: 'LOGIN'}


@app.route('/user/logout')
def logout():
    return {USER_MENU_ROUTE: 'LOGOUT'}
