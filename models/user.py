from datetime import datetime

from flask_login import UserMixin

from models import db


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(
        db.String(120),
        nullable=False
    )

    username = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    phone = db.Column(
        db.String(20)
    )

    address = db.Column(
        db.String(255)
    )

    city = db.Column(
        db.String(100)
    )

    country = db.Column(
        db.String(100)
    )

    postal_code = db.Column(
        db.String(20)
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    is_admin = db.Column(
        db.Boolean,
        default=False
    )

    def __repr__(self):
        return f"<User {self.username}>"