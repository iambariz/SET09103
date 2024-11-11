document.getElementById('add-ingredient-btn').addEventListener('click', function() {
    // Get the value of the input
    const ingredient = document.getElementById('ingredient-input').value;
    if (!ingredient) return;

    // Create the new ingredient div
    const ingredientDiv = document.createElement('div');
    ingredientDiv.className = "rounded-lg py-2 px-5 bg-secondary-500 text-primary-600 relative text-medium ingredient-item";

    // Create the span for the ingredient name
    const ingredientSpan = document.createElement('span');
    ingredientSpan.textContent = ingredient;
    ingredientDiv.appendChild(ingredientSpan);

    // Create the remove icon
    const removeIcon = document.createElement('i');
    removeIcon.className = "fas fa-times cursor-pointer font-weight-500 absolute text-sm top-1 right-1";
    removeIcon.onclick = function() {
        ingredientDiv.remove();
    };
    ingredientDiv.appendChild(removeIcon);

    // Append the new ingredient div to the container
    document.getElementById('ingredients-container').appendChild(ingredientDiv);

    // Clear the input field
    document.getElementById('ingredient-input').value = '';
});

document.getElementById("recipe-search").addEventListener("click", function () {
    const ingredients = Array.from(document.querySelectorAll(".ingredient-item"))
                             .map(item => item.textContent)
                             .filter(value => value.trim() !== "")
                             .join(",");

    if (!ingredients) {
        alert("Please add at least one ingredient.");
        return;
    }

    // Send a GET request to the API endpoint
    fetch(`/api/recipes?ingredients=${encodeURIComponent(ingredients)}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
                return;
            }

            // Handle the recipes data (you could display it on the page here)
            console.log(data);  // For debugging, view the response in the console
            displayRecipes(data);  // Function to handle rendering the recipes on the page
        })
        .catch(error => console.error("Error fetching recipes:", error));
});

function displayRecipes(recipes) {
    const resultsContainer = document.getElementById("recipe-results");
    resultsContainer.innerHTML = ""; // Clear any existing results

    recipes.forEach(recipe => {
        const recipeCard = document.createElement("div");
        recipeCard.classList.add("flex", "flex-col", "border-2", "border-primary-500", "rounded-md", "max-w-[300px]", "relative");

        // Populate the card with data
        recipeCard.innerHTML = `
            <div class="max-w-[300px] w-full max-h-[185px] h-full">
                <img class="object-cover rounded-t-md" src="${recipe.image}" alt="${recipe.title}">
            </div>
            <div class="text-left m-2">
                <h3 class="text-2xl text-primary-600 font-medium pb-3">${recipe.title}</h3>
                <div class="mr-[2rem]">
                    ${getTags(recipe)}
                </div>
            </div>
            <a href="#" class="text-primary-800 absolute text-2xl right-1 top-1">
                <i class="fa-regular fa-heart"></i>
            </a>
            <a href="/recipes/${recipe.id}" class="text-primary-800 absolute text-2xl right-1 bottom-1">
                <i class="fas fa-arrow-alt-circle-right"></i>
            </a>
        `;

        resultsContainer.appendChild(recipeCard);
    });
}

// Function to generate tags like Vegetarian, Breakfast, etc.
function getTags(recipe) {
    let tagsHtml = "";
    const tags = ["Vegetarian", "Breakfast"];
    tags.forEach(tag => {
        tagsHtml += `<span class="px-2 py-1 bg-primary-500 text-white-100 rounded-lg text-xs font-normal">${tag}</span> `;
    });
    return tagsHtml;
}

