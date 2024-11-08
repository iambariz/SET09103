from .internal_api import internal_api_bp

def register_api_blueprints(app):
    app.register_blueprint(internal_api_bp, url_prefix='/api')
