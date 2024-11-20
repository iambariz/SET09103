from flask import Blueprint, render_template, flash
from flask_login import current_user

main_bp = Blueprint('main', __name__)

# Index route
@main_bp.route('/')
def index():
    folders = []
    if(current_user.is_authenticated):
        folders = current_user.folders
    else:
        folders = []

    return render_template('index.html', is_authenticated=current_user.is_authenticated, current_user=current_user, folders=folders)

@main_bp.route('/privacy')
def privacy():
    return render_template('pages/privacy.html', is_authenticated=current_user.is_authenticated, current_user=current_user)


@main_bp.app_errorhandler(404)
def page_not_found(e):
    # Render the custom 404 page with a 404 status code
    return render_template('404.html'), 404
