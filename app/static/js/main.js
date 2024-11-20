window.onload = () => {
    const snackbar = document.getElementById("snackbar");
    showHideSnackbar(snackbar);
};

const showHideSnackbar = (element) => {

    // Only show the snackbar if there's a flash message
    if (element && element.textContent.trim() !== "") {
        element.classList.add("show");

        setTimeout(() => {
            element.classList.remove("show");
        }, 4000); // Total duration = fadein (0.5s) + display (3.0s) + fadeout (1.0s) = 4.5s
    }
};

const showSnackbarWithMessage = (message, type) => {
    const classes = type === "error" ? "snackbar error" : "snackbar";

    const snackbar = document.getElementById("snackbar-notification");
    snackbar.classList = classes;
    snackbar.textContent = message;
    showHideSnackbar(snackbar);
}

const openNavBtn = document.querySelector('#menu-toggle');
const navBar = document.querySelector('#mobile-menu');

openNavBtn.addEventListener('click', (e)=>{
    e.preventDefault();
    navBar.classList.toggle('hidden');

});