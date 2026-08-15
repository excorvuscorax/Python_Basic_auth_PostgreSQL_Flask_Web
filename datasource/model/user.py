import uuid

from datasource.database import db


def generate_user_id():
    return str(uuid.uuid4())


class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.String, primary_key=True, default=generate_user_id)

    login = db.Column(db.String, unique=True, nullable=False)

    password = db.Column(db.String, nullable=False)
