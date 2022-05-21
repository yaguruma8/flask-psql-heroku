# Flask+PostgreSQL+Heroku の勉強 の覚書
作成日: __2022/5/20__

# 目次

## 1. [準備](1.intro.md)
## 2. [Flask で Hello World](2.hello_world.md)
## 3. [Herokuアプリの作成](3.heroku_deploy.md)
## 4. [データベースの作成とアプリへの追加](4.database.md)
## 5. [Heroku+PostgreSQLアプリを作成する](5.heroku_again.md)
## 6. [Markdwonに対応する](6.markdown.md)


# 環境

- macOS Monterey 12.3.1
- Python 3.9.10
- PostgreSQL 14
- Flask 2.1.2
- Flask-SQLAlchemy 2.5.1
- psycopg2 2.9.3
- gunicorn 20.1.0

# ディレクトリ構成
```

.
├── .env
├── .gitignore
├── .venv
├── myapp
│   ├── __init__.py
│   ├── config.py
│   ├── db.py
│   └── templates
│       └── index.html
├── docker-compose.yml
├── postgresql
│   ├── Dockerfile
│   └── init
│       └── init.sql
├── Procfile
├── requirements.txt
└── runtime.txt
```

# 参考にした主なサイト

[FlaskとPostgreSQLでウェブアプリを作ってHerokuで無料で運用する](https://qiita.com/croquette0212/items/9b4dc5377e7d6f292671)

[Heroku、Flask、SQLAlchemyで掲示板を作る](https://qiita.com/kaonashikun/items/73c6367780644d6e5bbd)

[Flask SQLAlchemy で REST API を作ってみた](https://dev.classmethod.jp/articles/sqlalchemy-in-flask/)