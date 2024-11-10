import json
from ..extensions import db

class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    spoonacular_id = db.Column(db.Integer, nullable=False)
    instructions = db.Column(db.Text, nullable=True)
    ready_in = db.Column(db.Integer, nullable=True)
    servings = db.Column(db.Integer, nullable=True)
    source = db.Column(db.String(255), nullable=True)
    img_url = db.Column(db.String(255), nullable=True)
    dish_types = db.Column(db.Text, nullable=True)  # Store as JSON string
    ingredients = db.Column(db.Text, nullable=True) # Store as JSON string
    stored_at = db.Column(db.DateTime, nullable=False)

    @property
    def dish_types_list(self):
        return json.loads(self.dish_types or '[]')

    @dish_types_list.setter
    def dish_types_list(self, value):
        self.dish_types = json.dumps(value)

    @property
    def ingredients_list(self):
        return json.loads(self.ingredients or '[]')

    @ingredients_list.setter
    def ingredients_list(self, value):
        self.ingredients = json.dumps(value)