from os import path

DEBUG = True
BASE_DIR = path.abspath(path.dirname(__file__))
UPLOAD_FOLDER = 'temp'
ALLOWED_EXTENSIONS = {'pdf', 'json'}

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASE_DIR, 'database.db')
