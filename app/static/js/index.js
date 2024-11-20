let currentRecipeId = null;

document.getElementById('add-ingredient-btn').addEventListener('click', () => {
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

document.getElementById("recipe-search").addEventListener("click", () => {
    const ingredients = Array.from(document.querySelectorAll(".ingredient-item"))
                             .map(item => item.textContent)
                             .filter(value => value.trim() !== "")
                             .join(",");

    if (!ingredients) {
        showSnackbarWithMessage("Please add at least one ingredient.", "error");
        return;
    }

    // Send a GET request to the API endpoint
    fetch(`/api/recipes?ingredients=${encodeURIComponent(ingredients)}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                showSnackbarWithMessage(data.error, "error");
                return;
            }
            displayRecipes(data);
        })
        .catch(error => adjustSnackbarMessage(error));
});

const displayRecipes = (recipes) => {

    if(recipes.length === 0) {
        showSnackbarWithMessage("No recipes found. Try adding different ingredients.", "error");
        return;
    }

    const resultsContainer = document.getElementById("recipe-results");
    resultsContainer.innerHTML = ""; // Clear any existing results

    recipes.forEach(recipe => {
        const recipeCard = document.createElement("div");
        recipeCard.classList.add("flex", "flex-col", "border-2", "border-primary-500", "rounded-md", "max-w-[300px]", "relative", "w-full");

        // Populate the card with data
        recipeCard.innerHTML = `
            <div class="max-w-[300px] w-full max-h-[185px] h-full">
                <img class="object-cover rounded-t-md h-full w-full" src="${recipe.img_url}" alt="${recipe.title}">
            </div>
            <div class="text-left m-2">
                <h3 class="text-xl text-primary-600 font-medium pb-3 truncate overflow-hidden whitespace-nowrap">${recipe.title}</h3>
                <div class="mr-[2rem]">
                    ${getTags(recipe)}
                </div>
            </div>
            <a href="javascript:void(0);" onclick="saveRecipe(${recipe.id})" class="text-red-600 absolute text-2xl right-1 top-1">
                <i class="fa-solid fa-heart-circle-plus"></i>
            </a>
            <a href="/recipes/${recipe.id}" class="text-primary-700 absolute text-2xl right-1 bottom-1">
                <i class="fas fa-arrow-alt-circle-right"></i>
            </a>
        `;

        resultsContainer.appendChild(recipeCard);
    });
}

const getTags = (recipe) => {
    let tagsHtml = "";
    const tags = recipe.dish_types;

    // Limit the number of tags to display to 3 
    for(let i = 0; i < tags.length && i < 3; i++) {
        tagsHtml += `<span class="px-2 py-1 bg-primary-500 text-white-100 rounded-lg text-xs font-normal">${tags[i]}</span> `;
    }
    return tagsHtml;
}

const saveRecipe = (recipeId) => {
    currentRecipeId = recipeId;
    let modal = document.querySelector('#modal');
    modal.classList.remove('hidden');
}

document.querySelectorAll('.folder-btn').forEach(button => {
    button.addEventListener('click', (e) => {
        e.preventDefault();
        const folderId = button.dataset.folderId;
        const url = button.href;
        const csrfToken = getCookie('csrf_token');

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            credentials: 'include',
            body: JSON.stringify({ recipe_id: currentRecipeId, folder_id: folderId })
        })
        .then(response => response.json())
        .then(data => {
            let modal = document.querySelector('#modal');
            modal.classList.add('hidden');
            if(data.error) {
                showSnackbarWithMessage(data.error, "error");
            }else{
                showSnackbarWithMessage(data.message, "success");
            }
        })
        .catch(error => showSnackbarWithMessage("Something went wrong, please try again later.", "error"));
    });
});


const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(`${name}=`)) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};