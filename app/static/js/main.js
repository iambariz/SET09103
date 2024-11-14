window.onload = function() {
    var snackbar = document.getElementById("snackbar");

    // Only show the snackbar if there's a flash message
    if (snackbar && snackbar.textContent.trim() !== "") {
        snackbar.classList.add("show");

        setTimeout(function(){
            snackbar.classList.remove("show");
        }, 4000); // Total duration = fadein (0.5s) + display (3.0s) + fadeout (1.0s) = 4.5s
    }

    document.cookie = "csrf_token={{ csrf_token() }}; path=/";
};

