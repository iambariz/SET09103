# app/__init__.py
from flask import Flask
from .api.internal_api import internal_api_bp  # Import the blueprint
from .config import Config
from .extensions import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)#

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)


    # Register the blueprint
    app.register_blueprint(internal_api_bp)

    @app.route('/')
    def index():
        return "Hello, MealPal!"

    return app
