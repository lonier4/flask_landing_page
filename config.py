# os is a python built in module that lets us do some operating system operations
import os

# we need to tell flask where the root directory for this project is
basedir = os.path.abspath(os.path.dirname(__name__))
#absolute path or "os.path.abspath" is the path the computer takes from our hard drive to our project
# "os.path.dirname(__name__)" is the path from within our project to other folders within our folder.

class Config:
    """
    Set our configuration variables which tell the flask app how it is being setu up to use what external 
    functionality such as databases/mailing services/auth services
    """

    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')