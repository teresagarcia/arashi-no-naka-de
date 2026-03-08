class ListComponent extends HTMLElement {
    set data(value) {
        this._data = value;
        this.render();
    }

    async render() {
        if (!this._data) return;
        if (!this._templateLoaded) {
            const res = await fetch('/components/list/list-component.html');
            this._template = await res.text();
            this._templateLoaded = true;
        }

        this.innerHTML = this._template;
        const containerClon = document.querySelector('.container').cloneNode(true);
        
        this._data.forEach(element => {
            const original = document.querySelector(".original");
            const clon = original.cloneNode(true);
            clon.classList.remove('original');
            clon.removeAttribute('hidden');
            clon.querySelector('.accordion-title').textContent = `${element.titleText}`;
            const ul = clon.querySelector('ul');
            element.songs.forEach(item => {
                const li = document.createElement("li");
                li.innerHTML = `<a href="/lyrics.html?song=${item.link}"
                                class="text-blue-link">${item.title}</a>`;
                ul.appendChild(li);
            });
            containerClon.appendChild(clon);
        });
        containerClon.removeAttribute('hidden');
        containerClon.querySelectorAll('.accordion-header').forEach(header => {
            header.addEventListener('click', () => {
                const content = header.nextElementSibling;
                header.classList.toggle('open');
                content.classList.toggle('open');
            });
        });
        this.appendChild(containerClon);
    }
}

customElements.define('list-component', ListComponent);