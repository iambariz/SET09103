# app/routes/main.py
from flask import Blueprint, render_template
from flask_login import current_user
from app.models import Recipe
from flask_login import login_required, current_user
import pprint
from flask import jsonify


# Define the Blueprint
recipe_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

# @recipe_bp.route('/add')
# def index():
#     return render_template('index.html', is_authenticated=current_user.is_authenticated, current_user=current_user)


@recipe_bp.route('/<int:id>', methods=['GET'])
def folder_detail(id):
    pprint.pprint("test")

    # Debug
    print("Recipe ID: {id}")
    recipes = Recipe.query.all()
    return jsonify(recipes)


    recipe = Recipe.query.get_or_404(id)
    return render_template('pages/recipes/recipe.html', recipe=recipe.get_recipe_info())
