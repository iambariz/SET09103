from flask import Blueprint, render_template, request, jsonify, render_template, redirect, url_for, flash, session
from ..forms import RegistrationForm, LoginForm, ProfileUpdateForm
from app.models import User
from app.extensions import db
from werkzeug.security import check_password_hash
from app.utils.decorators import login_required  # Import the decorator
from flask_login import login_required, current_user, login_user

# Create a Blueprint instance for user-related routes
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/profile', methods=['GET'])
@login_required
def profile():
    form = ProfileUpdateForm(obj=current_user)

    if form.validate_on_submit():
        # Update user details
        current_user.username = form.username.data
        current_user.email = form.email.data

        # Update password only if fields are filled out
        if form.old_password.data and form.new_password.data == form.repeat_password.data:
            current_user.set_password(form.new_password.data)

        db.session.commit()
        flash("Profile updated successfully!", "success")

    return render_template('pages/user/profile.html', form=form, user=current_user)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if username or email already exists
        existing_user = User.query.filter(
            (User.username == form.username.data) | (User.email == form.email.data)
        ).first()

        if form.password.data != form.confirm_password.data:
            flash('Passwords do not match.', 'error')
            return render_template('user/register.html', form=form)

        if existing_user:
            flash('Username or email already taken.', 'error')
            return render_template('user/register.html', form=form)

        # Create a new user instance
        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data)  # Hash the password

        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('pages/user/register.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Find the user by email
        user = User.query.filter_by(email=form.email.data).first()

        # Check if user exists and password matches
        if user and check_password_hash(user.password_hash, form.password.data):
            flash('Login successful!', 'success')
            # Use flask_login's login_user instead of manually managing session
            login_user(user)

            return redirect(url_for('auth.profile'))
        else:
            flash('Invalid email or password.', 'error')

    return render_template('pages/user/login.html', form=form)


@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))