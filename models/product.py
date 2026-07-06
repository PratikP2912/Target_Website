from . import db


class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(200), nullable=False)

    brand = db.Column(db.String(100))

    category = db.Column(db.String(100))

    price = db.Column(db.Float)

    image = db.Column(db.String(255))

    description = db.Column(db.Text)

    rating = db.Column(db.Float, default=5.0)

    stock = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Product {self.name}>"