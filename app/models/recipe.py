import json
from datetime import datetime, timedelta, timezone
from ..extensions import db
from flask import current_app
from sqlalchemy.ext.associationproxy import association_proxy

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

    folder_recipes = db.relationship(
        'FolderRecipe',
        back_populates='recipe',
        cascade='all, delete-orphan'
    )
    
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

    def get_recipe_info(self):
        # Import here to avoid circular dependency at the module level
        from ..api.external_api import get_recipe_information

        # Check if data is outdated or missing
        if self.should_update(self.stored_at):
            recipe_info = get_recipe_information(self.spoonacular_id)

            if "error" not in recipe_info:
                # Update recipe details
                self.update_recipe_details(recipe_info)

        # Return the updated recipe
        return self

    @classmethod
    def get_bulk_recipe_information(cls, spoonacular_ids):
        from ..api.external_api import get_bulk_recipe_information

        one_hour_ago = (datetime.now(timezone.utc) - timedelta(hours=1)).replace(tzinfo=None)
        # Get existing recipes from the database
        recipes = cls.query.filter(cls.spoonacular_id.in_(spoonacular_ids)).all()
        existing_recipes = {recipe.spoonacular_id: recipe for recipe in recipes}

        # Identify IDs that need fetching from the API
        ids_to_fetch = [
            rid for rid in spoonacular_ids
            if rid not in existing_recipes or cls.should_update(existing_recipes[rid].stored_at)
        ]

        if ids_to_fetch:
            recipes_info = get_bulk_recipe_information(ids_to_fetch)
            if isinstance(recipes_info, list):
                for recipe_info in recipes_info:
                    spoonacular_id = recipe_info.get("id")
                    if spoonacular_id is not None:
                        # Use existing or create new Recipe instance
                        recipe = existing_recipes.get(spoonacular_id)
                        if not recipe:
                            recipe = cls(spoonacular_id=spoonacular_id)
                            db.session.add(recipe)
                        recipe.update_recipe_details(recipe_info)
                        existing_recipes[spoonacular_id] = recipe

                db.session.commit()

        # Return recipes in the requested order
        return [existing_recipes[rid] for rid in spoonacular_ids if rid in existing_recipes]



    def update_recipe_details(self, recipe_info):
        self.title = recipe_info.get("title", self.title)
        self.instructions = recipe_info.get("instructions", self.instructions)
        self.ready_in = recipe_info.get("readyInMinutes", self.ready_in)
        self.servings = recipe_info.get("servings", self.servings)
        self.source = recipe_info.get("sourceUrl", self.source)
        self.img_url = recipe_info.get("image", self.img_url)
        self.dish_types_list = recipe_info.get("dishTypes", self.dish_types_list)
        self.ingredients_list = [
            {
                "name": ing["name"],
                "amount": ing["amount"],
                "unit": ing["unit"],
                "image": ing.get("image", "")
            }
            for ing in recipe_info.get("extendedIngredients", [])
        ]
        self.stored_at = datetime.now(timezone.utc)


    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'spoonacular_id': self.spoonacular_id,
            'instructions': self.instructions,
            'ready_in': self.ready_in,
            'servings': self.servings,
            'source': self.source,
            'img_url': self.img_url,
            'dish_types': self.dish_types_list,
            'ingredients': self.ingredients_list,
            'stored_at': self.stored_at.isoformat() if self.stored_at else None,
        }
    
    @classmethod
    def should_update(cls, stored_at):
        from flask import current_app
        one_hour_ago = datetime.now(timezone.utc) - timedelta(hours=1)
        is_dev_env = current_app.config.get("ENV") == "development"
        return stored_at is None or (not is_dev_env and stored_at < one_hour_ago)
