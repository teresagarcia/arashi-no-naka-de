window.addEventListener("load", (event) => {
    document.querySelector('#order-album-btn').addEventListener('click', orderByAlbum);
    document.querySelector('#order-alpha-btn').addEventListener('click', orderByAlpha);
    document.querySelectorAll('.accordion-header').forEach(header => {
        header.addEventListener('click', () => {
            const content = header.nextElementSibling;
            header.classList.toggle('open');
            content.classList.toggle('open');
        });
    });

});

function orderByAlbum() {
    document.querySelector('#order-album-btn').disabled = true;
    document.querySelector('#order-alpha-btn').disabled = false;
    document.querySelector('#by-album-list').hidden = false;
    document.querySelector('#alphabetical-list').hidden = true;
}

function orderByAlpha() {
    document.querySelector('#order-album-btn').disabled = false;
    document.querySelector('#order-alpha-btn').disabled = true;
    document.querySelector('#by-album-list').hidden = true;
    document.querySelector('#alphabetical-list').hidden = false;

}

