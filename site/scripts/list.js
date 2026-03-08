window.addEventListener("load", async () => {
    const dataResByAlbum = await fetch(`/data/list-data.json`);
    const dataByAlbum = await dataResByAlbum.json();

    const el = document.createElement('list-component');
    el.data = dataByAlbum;

    document.querySelector('#by-album-list').appendChild(el);
    const dataResAlphabet = await fetch(`/data/list-alphabetic-data.json`);
    const dataAlphabet = await dataResAlphabet.json();

    const elAlphabet = document.createElement('list-component');
    elAlphabet.data = dataAlphabet;

    document.querySelector('#alphabetical-list').appendChild(elAlphabet);
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

