from . import db


class Review(db.Model):

    __tablename__ = "reviews"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    rating = db.Column(
        db.Integer
    )

    review = db.Column(
        db.Text
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id")
    )