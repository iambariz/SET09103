# app/routes/main.py
from flask import Blueprint, render_template
from flask_login import current_user

# Define the Blueprint
recipe_bp = Blueprint('main', __name__)

# Index route
@recipe_bp.route('/add')
def index():
    # Pass authentication status and user data to the template
    return render_template('index.html', is_authenticated=current_user.is_authenticated, current_user=current_user)