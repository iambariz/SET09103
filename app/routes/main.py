# app/routes/main.py
from flask import Blueprint, render_template
from flask_login import current_user

# Define the Blueprint
main_bp = Blueprint('main', __name__)

# Index route
@main_bp.route('/')
def index():
    # Pass authentication status and user data to the template
    return render_template('index.html', is_authenticated=current_user.is_authenticated, current_user=current_user)

@main_bp.route('/privacy')
def privacy():
    return render_template('pages/privacy.html', is_authenticated=current_user.is_authenticated, current_user=current_user)
