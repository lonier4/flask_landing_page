# imports - the flask object which our app will be an instance of and the Config class we just made
from flask import Flask
from config import Config

# import our blueprints for registration
from .cartoon_characters.routes import character

# import our database stuff
from .models import db     # db is the instance created in models.py
from flask_migrate import Migrate

# instantiate the instance of our application
app = Flask(__name__)

# register our blueprints
app.register_blueprint(character)

# configure that app from our config file
app.config.from_object(Config)

# configure our database to work with our app
db.init_app(app)

migrate = Migrate(app, db)

# tell our newly instantiated app where it can find its traffic controller (aka routes)
from . import routes
from . import models
# from our app folder (.) import routes
# could also use 2 dots (..) to go further back in our project files/folders