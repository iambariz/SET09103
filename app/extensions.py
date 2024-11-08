from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialise instances of SQLAlchemy and Migrate without binding to app yet
db = SQLAlchemy()
migrate = Migrate()
