from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import User, Folder, Recipe
from app.extensions import db
from flask_login import login_required, current_user
from app.forms.folder_create_form import FolderCreateForm

# Create a Blueprint instance for folder-related routes
folders_bp = Blueprint('folders', __name__, url_prefix='/folders')

@folders_bp.route('/', methods=['GET'])
@login_required
def folder_index():
    folders = Folder.query.filter_by(user_id=current_user.id).all()
    return render_template('pages/folder/index.html', user=current_user, folders=folders)

@folders_bp.route('/create', methods=['GET', 'POST'])
@login_required
def folder_create():
    form = FolderCreateForm()
    if form.validate_on_submit():
        # Create a new folder instance with the form data
        new_folder = Folder(name=form.name.data, user_id=current_user.id)
        print("Current User ID:", current_user.id)
        print("Folder Data:", form.name.data)

        # Add the new folder to the session and commit
        db.session.add(new_folder)
        db.session.commit()
        flash("Folder created successfully.", "success")

        # Redirect to the folder's detail page after creation
        return redirect(url_for('folders.folder_detail', id=new_folder.id))

    # Render the folder creation form page if not submitted or invalid
    return render_template('pages/folder/create.html', user=current_user, form=form)

@folders_bp.route('/<int:id>', methods=['GET'])
@login_required
def folder_detail(id):
    folder = Folder.query.get_or_404(id)

    # recipes = folder.recipes.all() if isinstance(folder.recipes, db.Query) else folder.recipes
    # print("Folder:", folder)
    # print("Folder Name:", folder.name)
    # print("Recipes in Folder:", folder.recipes.all() if hasattr(folder.recipes, 'all') else folder.recipes)
    # recipes = [recipe.to_dict() for recipe in folder.recipes]  # Convert recipes to list of dictionaries

    # return jsonify(recipes)
    return render_template('pages/folder/folder.html', folder=folder, recipes=folder.recipes)

@folders_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def folder_edit(id):
    folder = Folder.query.get_or_404(id)
    form = FolderCreateForm(obj=folder)  # Pre-populate with existing data

    if form.validate_on_submit():
        # Update folder data with form data
        folder.name = form.name.data
        db.session.commit()
        flash("Folder updated successfully.", "success")
        return redirect(url_for('folders.folder_detail', id=folder.id))

    # Render the same template as 'create' but passing 'form' and 'folder'
    return render_template('pages/folder/create.html', form=form, folder=folder)


@folders_bp.route('/delete/<int:id>', methods=['GET'])
@login_required
def folder_delete(id):
    folder = Folder.query.get_or_404(id)
    db.session.delete(folder)
    db.session.commit()
    flash("Folder deleted successfully.", "success")
    return redirect(url_for('folders.folder_index'))

@folders_bp.route('/<int:folder_id>/delete/<int:recipe_id>', methods=['GET'])
@login_required
def remove_recipe_from_folder(folder_id, recipe_id):
    folder = Folder.query.get_or_404(folder_id)
    recipe = Recipe.query.get_or_404(recipe_id)  # Retrieve the recipe directly

    # Check if the recipe exists in the folder's recipes
    if recipe in folder.recipes:
        folder.recipes.remove(recipe)  # Remove the recipe from the folder
        db.session.commit()
        flash("Recipe removed successfully.", "success")
    else:
        flash("Recipe not found in this folder.", "warning")
        
    return redirect(url_for('folders.folder_detail', id=folder.id))
