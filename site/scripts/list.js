window.addEventListener("load", (event) => {
    document.querySelector('#order-album-btn').addEventListener('click', orderByAlbum);
    document.querySelector('#order-alpha-btn').addEventListener('click', orderByAlpha);

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