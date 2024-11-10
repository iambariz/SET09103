document.getElementById('add-ingredient-btn').addEventListener('click', function() {
    // Get the value of the input
    const ingredient = document.getElementById('ingredient-input').value;
    if (!ingredient) return;

    // Create the new ingredient div
    const ingredientDiv = document.createElement('div');
    ingredientDiv.className = "rounded-lg py-2 px-5 bg-secondary-500 text-primary-600 relative text-medium";

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