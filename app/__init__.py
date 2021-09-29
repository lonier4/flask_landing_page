# imports - the flask object which our app will be an instance of and the Config class we just made
from flask import Flask
from config import Config

# import our blueprints for registration
from .cartoon_characters.routes import character

# instantiate the instance of our application
app = Flask(__name__)

# register our blueprints
app.register_blueprint(character)

# configure that app from our config file
app.config.from_object(Config)

# tell our newly instantiated app where it can find its traffic controller (aka routes)
from . import routes
# from our app folder (.) import routes
# could also use 2 dots (..) to go further back in our project files/folders