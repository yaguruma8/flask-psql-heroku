from flask import Flask, render_template, request, redirect, url_for
from flaskext.markdown import Markdown
from sqlalchemy import desc


from myapp.db import db, Entry, create_init


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        # config.py を読み込む。存在しなければ無視する
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # dbの初期化
    db.init_app(app)

    # Markdownの使用
    Markdown(app)

    @app.route('/')
    def hello_world():
        entries = Entry.query.order_by(desc(Entry.id)).all()
        return render_template('index.html', entries=entries)

    @app.post('/post')
    def add_entry():
        entry = Entry()
        entry.title = request.form['title']
        entry.body = request.form['body']
        db.session.add(entry)
        db.session.commit()
        # 上限を超えたら古い投稿から削除する
        if Entry.query.count() > 5:
            me = Entry.query.order_by(Entry.id).first()
            db.session.delete(me)
            db.session.commit()
        return redirect(url_for('hello_world'))

    app.cli.add_command(create_init)

    return app


app = create_app()
