# app/models/folder.py
from ..extensions import db

class Folder(db.Model):
    __tablename__ = 'folders'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relationship to User
    user = db.relationship('User', back_populates='folders')

    folder_recipes = db.relationship('FolderRecipe', back_populates='folder')

    recipes = db.relationship(
        'Recipe',
        secondary='folder_recipes',
        back_populates='folders',
        lazy='dynamic'
    )
