# app/api/external_api.py
import requests
from flask import current_app

def fetch_recipes(ingredients):
    """
    Fetch recipes from Spoonacular API based on the given ingredients.
    """
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "ingredients": ingredients,  # Comma-separated ingredients
        "number": 5,  # Limit number of results (you can adjust this)
        "apiKey": current_app.config['SPOONACULAR_API_KEY']
    }
    response = requests.get(url, params=params)

    # Check if the response was successful
    if response.status_code == 200:
        return response.json()
    else:
        # Return an error message if the API request fails
        return {"error": "Failed to fetch recipes"}
