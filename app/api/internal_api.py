# app/api/internal_api.py
from flask import Blueprint, jsonify, request
from .external_api import fetch_recipes
from ..models import Recipe, Folder
from ..extensions import db
from flask_login import current_user
from flask import jsonify, request
from app.models import Folder, Recipe
from app.extensions import db
from app.utils.decorators import login_required  # Import the decorator

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


@internal_api_bp.route('/api/save_recipe_to_folder', methods=['POST'])
@login_required
def save_recipe_to_folder():
    data = request.get_json()

    folder_id = data.get('folder_id')
    recipe_id = data.get('recipe_id')

    if not folder_id or not recipe_id:
        return jsonify({"error": "Missing folder_id or recipe_id"}), 400

    # Check if the folder exists and belongs to the current user
    folder = Folder.query.filter_by(id=folder_id, user_id=current_user.id).first()
    if not folder:
        return jsonify({"error": "Folder not found or access denied"}), 404

    # Check if the recipe exists
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404

    # Add the recipe to the folder's recipes if not already linked
    if recipe not in folder.recipes:
        folder.recipes.append(recipe)
        db.session.commit()
        return jsonify({"message": f"Recipe {recipe_id} saved to folder {folder_id}."}), 201
    else:
        return jsonify({"message": "Recipe already in folder"}), 200