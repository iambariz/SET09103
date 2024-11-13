from ..extensions import db

class FolderRecipe(db.Model):
    __tablename__ = 'folder_recipes'

    id = db.Column(db.Integer, primary_key=True)
    folder_id = db.Column(db.Integer, db.ForeignKey('folders.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)

    folder = db.relationship("Folder", back_populates="folder_recipes")
    recipe = db.relationship("Recipe", back_populates="folder_recipes")
