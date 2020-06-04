function sideEditor(content) {
    document.getElementById('value').innerHTML = content;

    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/sheets/" + slug)
}

function edit(slug) {
    var value = document.getElementById('value').innerHTML;
    var newValue = document.getElementById('newValue').value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/sheets/" + slug + "/post/", true);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhr.send("value=" + value + "&newValue=" + newValue);
}