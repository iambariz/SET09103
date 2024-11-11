# app/__init__.py

from flask import Flask, render_template
from .api.internal_api import internal_api_bp
from .models import User
from .config import Config
from .extensions import db, migrate
from .routes.auth import auth_bp
from .routes.main import main_bp
from .routes.folders import folders_bp
from flask_login import LoginManager

# Define LoginManager globally
login_manager = LoginManager()
login_manager.login_view = "auth.login"

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize LoginManager
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Initialize other extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    app.register_blueprint(internal_api_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(folders_bp)

    return app

# Define user_loader callback outside `create_app`
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
