import os

SECRET_KEY = os.getenv('MY_SECRET')
local_uri = 'postgresql://{user}:{pass}@{host}/{dbname}'.format(**{
    'user': os.getenv('DB_USERNAME', 'root'),
    'pass': os.getenv('DB_PASSWORD', ''),
    'host': os.getenv('DB_HOST', 'localhost'),
    'dbname': os.getenv('DB_NAME'),
})
heroku_db_uri = os.getenv('DATABASE_URL')
if heroku_db_uri is not None and heroku_db_uri.startswith("postgres://"):
    heroku_db_uri = heroku_db_uri.replace("postgres://", "postgresql://", 1)

SQLALCHEMY_DATABASE_URI = heroku_db_uri or local_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
