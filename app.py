import os
# import Flask
from flask import Flask, g, jsonify, request
from flask_cors import CORS
from flask_login import LoginManager

# importing resources from their respective .py files
from resources.persons import persons
from resources.favedbooks import faves

# importing models.py
import models

# Initialize an instance of flask
app = Flask(__name__)

app.config.from_pyfile('config.py') # creates the session secret

login_manager = LoginManager() # JS equivalent to ''const loginManager = new LoginManager()''
login_manager.init_app(app) # take LoginManager instance (login_manager) and initialize in an app (init_app()), which we called 'app'

# @<name of function> is called a "decorator", which is native to flask. Adds additional functionality to the functions you declare under it.

@login_manager.user_loader
def load_person(person_id):
  try:
    return models.Person.get_by_id(person_id)
  except models.DoesNotExist:
    return None

@app.before_request
def before_request():
  app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)
  '''Connect to the database before each request.'''
  g.db = models.DATABASE #ALL CAPS INDICATE TO OTHER READERS OF THE CODE THAT A VARIABLE NAME SHOULD NOT BE CHANGED
  g.db.connect()

@app.after_request
def after_request(response):
    app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)
    '''Close the database connection after each request.'''
    g.db = models.DATABASE
    g.db.close()
    return response

# '\' allows you to break a line in your code and have Python ignore the line break
CORS(app,\
     # need to add react front end deployment url 
     origins=['http://localhost:3000', 'https://booxploration.herokuapp.com'],\
     supports_credentials=True)

# equivalent to app.use(persons, '/api/v1/persons') in express
app.register_blueprint(persons, url_prefix='/api/v1/persons')
app.register_blueprint(faves, url_prefix='/api/v1/books')


if 'ON_HEROKU' in os.environ:
    print('hitting ')
    models.initialize()

# Listener route
if __name__ == '__main__':
  models.initialize()
  app.run(port=8000, debug=True)