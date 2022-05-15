from flask import Flask, render_template, request, redirect, url_for
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

    @app.post('/post')
    def add_entry():
        entry = Entry()
        entry.title = request.form['title']
        entry.body = request.form['body']
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('hello_world'))

    return app


# gunicornで呼び出すアプリケーションをappに代入
app = create_app()
