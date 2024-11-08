from flask import Blueprint, render_template, jsonify

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

# Define the '/test' route to call the RaiderConnector function
@main_bp.route('/test')
def test():
    # Call the function from raiderConnector.py
    page = 1  # You can change this value based on pagination needs

    # Get data from the Raider API
    data = "test"

    # Return the data as JSON
    return jsonify(data)
