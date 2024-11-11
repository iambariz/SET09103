from flask import Blueprint, render_template, request, jsonify, render_template, redirect, url_for, flash, session
from ..forms import RegistrationForm, LoginForm, ProfileUpdateForm
from app.models import User
from app.extensions import db
from werkzeug.security import check_password_hash
from app.utils.decorators import login_required  # Import the decorator
from flask_login import login_required, current_user, login_user

# Create a Blueprint instance for user-related routes
folders_bp = Blueprint('folders', __name__, url_prefix='/folders')

@folders_bp.route('/', methods=['GET'])
@login_required
def folder_index():


    return render_template('pages/folder/index.html', user=current_user)