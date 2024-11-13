document.querySelectorAll('.fa-folder-open').forEach(button => {
    button.addEventListener('click', (e) => {
        e.preventDefault();
        const folderId = button.dataset.folderId;
        const url = button.href;
        const csrfToken = getCookie('csrf_token');

        // fetch(url, {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json',
        //         'X-CSRFToken': csrfToken
        //     },
        //     credentials: 'include',
        //     body: JSON.stringify({ recipe_id: currentRecipeId, folder_id: folderId })
        // })
        // .then(response => response.json())
        // .then(data => {
        //     let modal = document.querySelector('#modal');
        //     modal.classList.add('hidden');
        // })
        // .catch(error => console.error('Error:', error));
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