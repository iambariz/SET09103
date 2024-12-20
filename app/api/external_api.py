import requests
from flask import current_app
from ..models import Recipe

def fetch_recipes(ingredients):

    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "ingredients": ingredients,  # Comma-separated ingredients
        "number": 10,# Number of recipes to return - max 10 pagination is not possible due to api limitation (no pagi on Spoonacular, and if I do 20 for example, the order of the recipes will be different)
        "apiKey": current_app.config["SPOONACULAR_API_KEY"],
    }
    response = requests.get(url, params=params)

    # Check if the response was successful
    if response.status_code == 200:
        # Get the details of the recipes
        recipes = response.json()
        recipe_ids = [recipe["id"] for recipe in recipes]

        # Fetch or create Recipe instances
        recipes = Recipe.get_bulk_recipe_information(recipe_ids)
        return recipes
    else:
        # Return an error message if the API request fails
        return {"error": "Failed to fetch recipes"}

def get_sample_return():
    return [
        {
            "id": 640352,
            "image": "https://img.spoonacular.com/recipes/640352-312x231.jpg",
            "imageType": "jpg",
            "likes": 11,
            "missedIngredientCount": 3,
            "missedIngredients": [
                {
                    "aisle": "Produce",
                    "amount": 2,
                    "extendedName": "fresh cranberries",
                    "id": 9078,
                    "image": "https://img.spoonacular.com/ingredients_100x100/cranberries.jpg",
                    "meta": ["fresh"],
                    "name": "cranberries",
                    "original": "2 cups fresh cranberries",
                    "originalName": "fresh cranberries",
                    "unit": "cups",
                    "unitLong": "cups",
                    "unitShort": "cup",
                },
                {
                    "aisle": "Milk, Eggs, Other Dairy",
                    "amount": 4,
                    "extendedName": "unsalted butter",
                    "id": 1145,
                    "image": "https://img.spoonacular.com/ingredients_100x100/butter-sliced.jpg",
                    "meta": ["unsalted", "cut into cubes"],
                    "name": "butter",
                    "original": "1/2 stick (4 Tbs) unsalted butter, cut into cubes",
                    "originalName": "1/2 stick unsalted butter, cut into cubes",
                    "unit": "Tbs",
                    "unitLong": "Tbs",
                    "unitShort": "Tbs",
                },
                {
                    "aisle": "Cereal",
                    "amount": 1.5,
                    "id": 8120,
                    "image": "https://img.spoonacular.com/ingredients_100x100/rolled-oats.jpg",
                    "meta": ["(not quick-cooking)"],
                    "name": "regular oats",
                    "original": "1 1/2 cups regular oats (not quick-cooking)",
                    "originalName": "regular oats (not quick-cooking)",
                    "unit": "cups",
                    "unitLong": "cups",
                    "unitShort": "cup",
                },
            ],
            "title": "Cranberry Apple Crisp",
            "unusedIngredients": [],
            "usedIngredientCount": 1,
            "usedIngredients": [
                {
                    "aisle": "Produce",
                    "amount": 4,
                    "id": 1089003,
                    "image": "https://img.spoonacular.com/ingredients_100x100/grannysmith-apple.png",
                    "meta": ["chopped"],
                    "name": "granny smith apples",
                    "original": "4 cups Granny Smith apples, chopped into ½ inch chunks",
                    "originalName": "Granny Smith apples, chopped into ½ inch chunks",
                    "unit": "cups",
                    "unitLong": "cups",
                    "unitShort": "cup",
                }
            ],
        },
        {
            "id": 632660,
            "image": "https://img.spoonacular.com/recipes/632660-312x231.jpg",
            "imageType": "jpg",
            "likes": 3,
            "missedIngredientCount": 3,
            "missedIngredients": [
                {
                    "aisle": "Milk, Eggs, Other Dairy",
                    "amount": 1.5,
                    "extendedName": "unsalted butter",
                    "id": 1145,
                    "image": "https://img.spoonacular.com/ingredients_100x100/butter-sliced.jpg",
                    "meta": ["unsalted", "cold"],
                    "name": "butter",
                    "original": "1 1/2 sticks cold unsalted butter",
                    "originalName": "cold unsalted butter",
                    "unit": "sticks",
                    "unitLong": "sticks",
                    "unitShort": "sticks",
                },
                {
                    "aisle": "Spices and Seasonings",
                    "amount": 2,
                    "id": 2010,
                    "image": "https://img.spoonacular.com/ingredients_100x100/cinnamon.jpg",
                    "meta": [],
                    "name": "cinnamon",
                    "original": "2 teaspoons cinnamon",
                    "originalName": "cinnamon",
                    "unit": "teaspoons",
                    "unitLong": "teaspoons",
                    "unitShort": "tsp",
                },
                {
                    "aisle": "Nut butters, Jams, and Honey",
                    "amount": 2,
                    "id": 19719,
                    "image": "https://img.spoonacular.com/ingredients_100x100/apricot-jam.jpg",
                    "meta": ["melted"],
                    "name": "apricot preserves",
                    "original": "2 tablespoons apricot preserves, melted and strained",
                    "originalName": "apricot preserves, melted and strained",
                    "unit": "tablespoons",
                    "unitLong": "tablespoons",
                    "unitShort": "Tbsp",
                },
            ],
            "title": "Apricot Glazed Apple Tart",
            "unusedIngredients": [],
            "usedIngredientCount": 1,
            "usedIngredients": [
                {
                    "aisle": "Produce",
                    "amount": 4,
                    "id": 1079003,
                    "image": "https://img.spoonacular.com/ingredients_100x100/red-delicious-apples.png",
                    "meta": [
                        "red",
                        "such as golden delicious, peeled, cored and cut into 1/4-inch-thick slices",
                    ],
                    "name": "apples",
                    "original": "4 large red apples, such as Golden Delicious, peeled, cored and cut into 1/4-inch-thick slices",
                    "originalName": "red apples, such as Golden Delicious, peeled, cored and cut into 1/4-inch-thick slices",
                    "unit": "large",
                    "unitLong": "larges",
                    "unitShort": "large",
                }
            ],
        },
        {
            "id": 641803,
            "image": "https://img.spoonacular.com/recipes/641803-312x231.jpg",
            "imageType": "jpg",
            "likes": 1,
            "missedIngredientCount": 3,
            "missedIngredients": [
                {
                    "aisle": "Milk, Eggs, Other Dairy",
                    "amount": 0.75,
                    "id": 1001,
                    "image": "https://img.spoonacular.com/ingredients_100x100/butter-sliced.jpg",
                    "meta": [],
                    "name": "butter",
                    "original": "3/4 stick of butter",
                    "originalName": "butter",
                    "unit": "stick",
                    "unitLong": "sticks",
                    "unitShort": "stick",
                },
                {
                    "aisle": "Spices and Seasonings",
                    "amount": 1,
                    "id": 2011,
                    "image": "https://img.spoonacular.com/ingredients_100x100/cloves.jpg",
                    "meta": [],
                    "name": "ground cloves",
                    "original": "Dash of ground cloves",
                    "originalName": "ground cloves",
                    "unit": "Dash",
                    "unitLong": "Dash",
                    "unitShort": "Dash",
                },
                {
                    "aisle": "Produce",
                    "amount": 1,
                    "id": 9156,
                    "image": "https://img.spoonacular.com/ingredients_100x100/zest-lemon.jpg",
                    "meta": [],
                    "name": "lemon zest",
                    "original": "1 Zest of lemon",
                    "originalName": "Zest of lemon",
                    "unit": "",
                    "unitLong": "",
                    "unitShort": "",
                },
            ],
            "title": "Easy & Delish! ~ Apple Crumble",
            "unusedIngredients": [],
            "usedIngredientCount": 1,
            "usedIngredients": [
                {
                    "aisle": "Produce",
                    "amount": 3,
                    "id": 9003,
                    "image": "https://img.spoonacular.com/ingredients_100x100/apple.jpg",
                    "meta": ["sliced"],
                    "name": "apples",
                    "original": "3 apples – sliced",
                    "originalName": "apples – sliced",
                    "unit": "",
                    "unitLong": "",
                    "unitShort": "",
                }
            ],
        },
        {
            "id": 73420,
            "image": "https://img.spoonacular.com/recipes/73420-312x231.jpg",
            "imageType": "jpg",
            "likes": 0,
            "missedIngredientCount": 3,
            "missedIngredients": [
                {
                    "aisle": "Baking",
                    "amount": 1,
                    "id": 18369,
                    "image": "https://img.spoonacular.com/ingredients_100x100/white-powder.jpg",
                    "meta": [],
                    "name": "baking powder",
                    "original": "1 tsp baking powder",
                    "originalName": "baking powder",
                    "unit": "tsp",
                    "unitLong": "teaspoon",
                    "unitShort": "tsp",
                },
                {
                    "aisle": "Spices and Seasonings",
                    "amount": 1,
                    "id": 2010,
                    "image": "https://img.spoonacular.com/ingredients_100x100/cinnamon.jpg",
                    "meta": [],
                    "name": "cinnamon",
                    "original": "1 tsp cinnamon",
                    "originalName": "cinnamon",
                    "unit": "tsp",
                    "unitLong": "teaspoon",
                    "unitShort": "tsp",
                },
                {
                    "aisle": "Milk, Eggs, Other Dairy",
                    "amount": 1,
                    "id": 1123,
                    "image": "https://img.spoonacular.com/ingredients_100x100/egg.png",
                    "meta": [],
                    "name": "egg",
                    "original": "1 egg",
                    "originalName": "egg",
                    "unit": "",
                    "unitLong": "",
                    "unitShort": "",
                },
            ],
            "title": "Apple Or Peach Strudel",
            "unusedIngredients": [],
            "usedIngredientCount": 1,
            "usedIngredients": [
                {
                    "aisle": "Produce",
                    "amount": 6,
                    "id": 9003,
                    "image": "https://img.spoonacular.com/ingredients_100x100/apple.jpg",
                    "meta": [],
                    "name": "baking apples",
                    "original": "6 large baking apples",
                    "originalName": "baking apples",
                    "unit": "large",
                    "unitLong": "larges",
                    "unitShort": "large",
                }
            ],
        },
        {
            "id": 157103,
            "image": "https://img.spoonacular.com/recipes/157103-312x231.jpg",
            "imageType": "jpg",
            "likes": 0,
            "missedIngredientCount": 4,
            "missedIngredients": [
                {
                    "aisle": "Milk, Eggs, Other Dairy",
                    "amount": 0.5,
                    "id": 1001,
                    "image": "https://img.spoonacular.com/ingredients_100x100/butter-sliced.jpg",
                    "meta": ["melted"],
                    "name": "butter",
                    "original": "1/2 cup butter, melted",
                    "originalName": "butter, melted",
                    "unit": "cup",
                    "unitLong": "cups",
                    "unitShort": "cup",
                },
                {
                    "aisle": "Spices and Seasonings",
                    "amount": 1,
                    "id": 2010,
                    "image": "https://img.spoonacular.com/ingredients_100x100/cinnamon.jpg",
                    "meta": [],
                    "name": "cinnamon",
                    "original": "1 tsp. cinnamon",
                    "originalName": "cinnamon",
                    "unit": "tsp",
                    "unitLong": "teaspoon",
                    "unitShort": "tsp",
                },
                {
                    "aisle": "Milk, Eggs, Other Dairy",
                    "amount": 1,
                    "id": 1123,
                    "image": "https://img.spoonacular.com/ingredients_100x100/egg.png",
                    "meta": [],
                    "name": "egg",
                    "original": "1 egg",
                    "originalName": "egg",
                    "unit": "",
                    "unitLong": "",
                    "unitShort": "",
                },
                {
                    "aisle": "Baking",
                    "amount": 1,
                    "id": 1052050,
                    "image": "https://img.spoonacular.com/ingredients_100x100/vanilla.jpg",
                    "meta": ["(paste or extract)"],
                    "name": "vanilla",
                    "original": "1 tsp. vanilla (paste or extract)",
                    "originalName": "vanilla (paste or extract)",
                    "unit": "tsp",
                    "unitLong": "teaspoon",
                    "unitShort": "tsp",
                },
            ],
            "title": "Apple Cinnamon Blondies",
            "unusedIngredients": [],
            "usedIngredientCount": 1,
            "usedIngredients": [
                {
                    "aisle": "Produce",
                    "amount": 0.5,
                    "id": 9003,
                    "image": "https://img.spoonacular.com/ingredients_100x100/apple.jpg",
                    "meta": ["diced", "finely"],
                    "name": "apple",
                    "original": "1/2 cup apple, finely diced",
                    "originalName": "apple, finely diced",
                    "unit": "cup",
                    "unitLong": "cups",
                    "unitShort": "cup",
                }
            ],
        },
    ]

def get_recipe_information(recipe_id):
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    params = {
        "apiKey": current_app.config["SPOONACULAR_API_KEY"],
    }
    response = requests.get(url, params=params)

    # Check if the response was successful
    if response.status_code == 200:
        return response.json()
    else:
        # Return an error message if the API request fails
        return {"error": "Failed to fetch recipe information"}


def get_bulk_recipe_information(recipe_ids):
    url = "https://api.spoonacular.com/recipes/informationBulk"
    params = {
        "ids": ",".join(map(str, recipe_ids)),
        "apiKey": current_app.config["SPOONACULAR_API_KEY"],
    }
    response = requests.get(url, params=params)

    # Check if the response was successful
    if response.status_code == 200:
        return response.json()
    else:
        # Return an error message if the API request fails
        return {"error": "Failed to fetch recipe information"}


