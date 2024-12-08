from flask import Blueprint, render_template
from flask_login import current_user
from app.models import Recipe
from flask_login import login_required, current_user


# Define the Blueprint
recipe_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@recipe_bp.route('/<int:id>', methods=['GET'])
def recipe_detail(id):
    recipe = Recipe.query.get_or_404(id)

    # Ensure recipe information is up-to-date
    recipe_info = recipe.get_recipe_info()

    # Convert the recipe to a dictionary
    recipe_data = recipe_info.to_dict()

    # Render the template with the recipe data
    return render_template('pages/recipe/recipe.html', recipe=recipe_data)

