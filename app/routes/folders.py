from flask import Blueprint, render_template, request, redirect, url_for
from app.models import User, Folder
from app.extensions import db
from flask_login import login_required, current_user
from app.forms.folder_create_form import FolderCreateForm

# Create a Blueprint instance for folder-related routes
folders_bp = Blueprint('folders', __name__, url_prefix='/folders')

@folders_bp.route('/', methods=['GET'])
@login_required
def folder_index():
    return render_template('pages/folder/index.html', user=current_user)

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

        # Redirect to the folder's detail page after creation
        return redirect(url_for('folders.folder_detail', id=new_folder.id))

    # Render the folder creation form page if not submitted or invalid
    return render_template('pages/folder/create.html', user=current_user, form=form)

@folders_bp.route('/<int:id>', methods=['GET'])
@login_required
def folder_detail(id):
    folder = Folder.query.get_or_404(id)
    return render_template('pages/folder/detail.html', folder=folder)
