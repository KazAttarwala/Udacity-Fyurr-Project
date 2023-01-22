import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost:5432/fyurr'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_POOL_SIZE=20
SQLALCHEMY_POOL_TIMEOUT=300
