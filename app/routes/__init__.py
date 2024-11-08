from .user import user_bp

def register_blueprints(app):
    # Register the user blueprint
    app.register_blueprint(user_bp)
