from flask import Flask, render_template
from myapp.db import db, Entry


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        # config.py を読み込む。存在しなければ無視する
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # dbの初期化
    db.init_app(app)

    @app.route('/')
    def hello_world():
        entries = Entry.query.all()
        return render_template('index.html', entries=entries)

    return app


# gunicornで呼び出すアプリケーションをappに代入
app = create_app()
