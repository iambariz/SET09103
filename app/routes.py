from flask import Blueprint, render_template

# Define the blueprint: 'main_bp'
main_bp = Blueprint('main', __name__)

# Define a route for the home page
@main_bp.route('/')
def home():
    return "Welcome to the Flask Boilerplate!"

# Define another route as an example
@main_bp.route('/about')
def about():
    return "This is the About page."
