# app/api/internal_api.py
from flask import Blueprint, jsonify, request
from .external_api import fetch_recipes
from ..models import Recipe
from ..extensions import db

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

# app/api/internal_api.py
@internal_api_bp.route('/api/save_recipe', methods=['POST'])
def save_recipe():
    data = request.get_json()
    recipe = Recipe(**data)
    db.session.add(recipe)
    db.session.commit()
    return jsonify({"message": "Recipe saved!"}), 201


@internal_api_bp.route('/api/recipes', methods=['GET'])
def get_saved_recipes():
    recipes = Recipe.query.all()
    return jsonify([recipe.to_dict() for recipe in recipes])

