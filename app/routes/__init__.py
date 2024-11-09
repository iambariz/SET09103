from .auth import auth_bp

def register_blueprints(app):
    # Register the user blueprint
    app.register_blueprint(auth_bp)
