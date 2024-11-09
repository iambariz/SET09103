# app/__init__.py
from flask import Flask, render_template
from .api.internal_api import internal_api_bp  # Import the blueprint
from .config import Config
from .extensions import db, migrate
from .routes.auth import auth_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)#

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register the blueprint
    app.register_blueprint(internal_api_bp)
    app.register_blueprint(auth_bp)
    
    return app