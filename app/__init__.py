# app/__init__.py
from flask import Flask
from .api.internal_api import internal_api_bp  # Import the blueprint
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register the blueprint
    app.register_blueprint(internal_api_bp)

    @app.route('/')
    def index():
        return "Hello, MealPal!"

    return app
