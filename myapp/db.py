from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Entry(db.Model):
    __tablename__ = 'entries'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    body = db.Column(db.String(), nullable=False)

    def __repr__(self) -> str:
        return '<Entry %r>' % self.title


def create_init(app):
    with app.app_context():
        db.drop_all()
        db.create_all()