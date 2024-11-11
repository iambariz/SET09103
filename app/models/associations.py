# app/models/associations.py
from ..extensions import db

folder_recipe_association = db.Table(
    'folder_recipe_association',
    db.Column('folder_id', db.Integer, db.ForeignKey('folders.id'), primary_key=True),
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipes.id'), primary_key=True)
)
