from os import path

DEBUG = True
BASE_DIR = path.abspath(path.dirname(__file__))  

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASE_DIR, 'database.db')