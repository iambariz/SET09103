from .auth import auth_bp
from .main import main_bp
from .folders import folders_bp

def register_blueprints(app):
    # Register the user blueprint
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(folders_bp)
