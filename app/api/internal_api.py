# app/api/internal_api.py
from flask import Blueprint, jsonify, request
from .external_api import fetch_recipes

internal_api_bp = Blueprint('internal_api', __name__)

@internal_api_bp.route('/api/test', methods=['GET'])
def test():
    return jsonify({"message": "Internal API working!"})

@internal_api_bp.route('/api/recipes', methods=['GET'])
def get_recipes():
    ingredients = request.args.get('ingredients')
    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400

    recipes = fetch_recipes(ingredients)
    return jsonify(recipes)
