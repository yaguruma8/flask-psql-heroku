import os

from flask import Flask, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # root/instance/config.py を読み込む。存在しなければ無視する
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello_world():
        return render_template('index.html', name='fuga')

    return app


# gunicornで呼び出すアプリケーションをappに代入
app = create_app()
