from flask import Blueprint, render_template, request, jsonify, render_template, redirect, url_for, flash, session
from ..forms import RegistrationForm
from ..forms import RegistrationForm, LoginForm
from app.models import User
from app.extensions import db
from werkzeug.security import check_password_hash
from app.utils.decorators import login_required  # Import the decorator

# Create a Blueprint instance for user-related routes
user_bp = Blueprint('user', __name__, url_prefix='/user')

# Define user-specific routes within this blueprint
@user_bp.route('/profile', methods=['GET'])
@login_required
def profile():

    user = User.query.get(session['user_id'])
    return render_template('pages/user/profile.html', user=user)

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


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Find the user by email
        user = User.query.filter_by(email=form.email.data).first()

        # Check if user exists and password matches
        if user and check_password_hash(user.password_hash, form.password.data):
            flash('Login successful!', 'success')

            #Todo: Session management
            session['user_id'] = user.id
            session['username'] = user.username

            return redirect(url_for('user.profile'))
        else:
            flash('Invalid email or password.', 'error')

    return render_template('pages/user/login.html', form=form)

@user_bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('user.login'))