import os
import sqlite3

from flask import Flask, render_template, current_app, g


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # instance/config.py を読み込む。存在しなければ無視する
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello_world():
        entries = get_db().execute('SELECT * FROM entries;').fetchall()
        return render_template('index.html', entries=entries)

    return app


# gunicornで呼び出すアプリケーションをappに代入
app = create_app()


# database
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(err=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
