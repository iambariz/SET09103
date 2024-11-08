# app/api/__init__.py
from .internal_api import internal_api_bp

def register_api_blueprints(app):
    # Register the internal API blueprint with a URL prefix
    app.register_blueprint(internal_api_bp, url_prefix='/api')
    # You can add more blueprint registrations here as needed
