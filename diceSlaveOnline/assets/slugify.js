const titleInput = document.querySelector('input[name="name"]');
const slugInput = document.querySelector('input[name="slug"]');

const slugify = (val) => {
    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')     // replace & with '-and-'
        .replace(/[\s\W-]+/g, '-')      // replace spaces, nonwords, and dashes with a single dash
};

window.onload = function() {
    slugify(titleInput.value);
}

titleInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slugify(titleInput.value));
});