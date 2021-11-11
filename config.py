import os
from dotenv import load_dotenv 

basedir = os.path.abspath(os.path.dirname(__file__))

#give aces to the project in ANY OS we find ourselves in 
#Allow outside files/folders to be added to the project
#base directory

load_dotenv(os.path.join(basedir, '.env'))
class Config():
    """
    Set Config variables for the flask app.
    Using Envorinment variables where avaiable
    create config variables if not done already.
    """

    FLASK_APP = os.environ.get('FLASK_APP')
    FLSAK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Turn off messages for updates in sqlalchemy

