# app/models/folder.py
from ..extensions import db
from .associations import folder_recipe_association

class Folder(db.Model):
    __tablename__ = 'folders'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relationship to User
    user = db.relationship('User', back_populates='folders')

    # Many-to-Many relationship with Recipe
    recipes = db.relationship('Recipe', secondary=folder_recipe_association, back_populates='folders')

