window.addEventListener("load", async() => {
    const dataRes = await fetch(`/data/index-data.json`);
    const data = await dataRes.json();

    data.forEach(element => {
        const el = document.createElement('lyrics-card-component');
        el.data = element;

        document.querySelector('.card-container').appendChild(el);
    });
});