from flask import Blueprint, render_template, request, jsonify, render_template, redirect, url_for, flash
from ..forms import RegistrationForm

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
        # Process form data, e.g., save the user to the database
        flash('Registration successful!', 'success')
        return redirect(url_for('index'))
    return render_template('pages/user/register.html', form=form)