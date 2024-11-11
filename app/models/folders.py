import json
from ..extensions import db

class Recipe(db.Model):
    __tablename__ = 'folders'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    recipes = db.relationship('Recipe', backref='folder', lazy=True)