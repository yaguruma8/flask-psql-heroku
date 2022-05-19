import os

SECRET_KEY = os.getenv('MY_SECRET')
# SQLALCHEMY_DATABASE_URI='sqlite:///myappdb.sqlite3'
# SQLALCHEMY_DATABASE_URI='postgresql://localhost/flasknote'
local_uri = 'postgresql://{user}:{pass}@{host}/{dbname}'.format(**{
    'user': os.getenv('DB_USERNAME', 'root'),
    'pass': os.getenv('DB_PASSWORD', ''),
    'host': os.getenv('DB_HOST', 'localhost'),
    'dbname': os.getenv('DB_NAME'),
})
SQLALCHEMY_DATABASE_URI = local_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
