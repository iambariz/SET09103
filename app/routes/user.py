from flask import Blueprint, render_template, request, jsonify, render_template, redirect, url_for, flash
from ..forms import RegistrationForm
from app.forms import RegistrationForm
from app.models import User
from app.extensions import db

# Create a Blueprint instance for user-related routes
user_bp = Blueprint('user', __name__, url_prefix='/user')

# Define user-specific routes within this blueprint
@user_bp.route('/profile', methods=['GET'])
def profile():
    # Example user profile route
    return render_template('pages/user/profile.html')

@user_bp.route('/login', methods=['POST'])
def login():
    # Example login route
    data = request.get_json()
    # Authenticate user here...
    return jsonify({"message": "User logged in!"})

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if username or email already exists
        existing_user = User.query.filter(
            (User.username == form.username.data) | (User.email == form.email.data)
        ).first()

        if existing_user:
            flash('Username or email already taken.', 'error')
            return render_template('user/register.html', form=form)

        # Create a new user instance
        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data)  # Hash the password

        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('user.login'))

    return render_template('pages/user/register.html', form=form)
