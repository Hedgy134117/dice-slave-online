var pages = [
    document.getElementById('character'),
    document.getElementById('fighting'),
    document.getElementById('equipment'),
    document.getElementById('spellcasting'),
    document.getElementById('personality'),
]

function page(openPage) {
    var currentPage = document.getElementById(openPage);
    currentPage.style.display = 'block';
    for (var i = 0; i < pages.length; i++) {
        if (pages[i] != currentPage) {
            try {
                pages[i].style.display = 'none';
            }
            catch(err) {
                continue;
            }
        }
    }
    document.getElementById('side-editor').style = "display: none;"
}