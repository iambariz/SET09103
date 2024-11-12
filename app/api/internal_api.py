# app/api/internal_api.py
from flask import Blueprint, jsonify, request
from .external_api import fetch_recipes
from ..models import Recipe, Folder, FolderRecipe
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

@internal_api_bp.route('/api/save_recipe_to_folder', methods=['POST'])
@login_required
def save_recipe_to_folder():
    # Parse JSON data
    data = request.get_json()
    folder_id = data.get("folder_id")
    recipe_id = data.get("recipe_id")

    # Validate folder and recipe existence
    folder = Folder.query.get(folder_id)
    if not folder:
        return jsonify({"error": "Folder not found"}), 404

    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404

    # Check if the recipe is already in the folder
    existing_association = FolderRecipe.query.filter_by(folder_id=folder_id, recipe_id=recipe_id).first()
    if existing_association:
        return jsonify({"message": "Recipe is already in this folder"}), 200

    # Create new association
    folder_recipe_association = FolderRecipe(folder=folder, recipe=recipe)
    db.session.add(folder_recipe_association)
    db.session.commit()

    return jsonify({"message": "Recipe added to folder successfully"}), 201

@internal_api_bp.route('/api/recipes', methods=['GET'])
def get_saved_recipes():
    recipes = Recipe.query.all()
    return jsonify([recipe.to_dict() for recipe in recipes])