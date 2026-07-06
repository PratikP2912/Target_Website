from flask import Flask
from flask_login import LoginManager

from config import Config

from models import db
from models.user import User

# your blueprint imports
from routes.home import home_bp
from routes.auth import auth_bp
from routes.products import products_bp
from routes.cart import cart_bp
from routes.contact import contact_bp
from routes.profile import profile_bp
from routes.admin import admin_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(products_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(contact_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(admin_bp)


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)