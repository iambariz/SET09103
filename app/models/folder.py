from ..extensions import db
from sqlalchemy.ext.associationproxy import association_proxy

class Folder(db.Model):
    __tablename__ = 'folders'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relationship to User
    user = db.relationship('User', back_populates='folders')


    # Relationship to FolderRecipe
    folder_recipes = db.relationship(
        'FolderRecipe',
        back_populates='folder',
        cascade='all, delete-orphan'
    )

    # Association Proxy to access recipes directly
    recipes = association_proxy('folder_recipes', 'recipe')

