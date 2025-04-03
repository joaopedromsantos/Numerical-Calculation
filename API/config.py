import os


class Config:
    """ General settings for the Flask application. """
    SECRET_KEY = os.environ.get('SECRET_KEY')