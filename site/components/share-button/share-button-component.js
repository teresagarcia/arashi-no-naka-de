class ShareButtonComponent extends HTMLElement {
    async connectedCallback() {
        const response = await fetch('/components/share-button/share-button-component.html');
        const html = await response.text();
        this.innerHTML = html;
        const button = this.querySelector('#share-btn');
        if (!button) return;

        button.addEventListener('click', () => {
            let path = window.location.pathname;

            path = path.replace(/-\d{12}\.html$/, '.html');

            const cleanUrl = window.location.origin + path + window.location.search + window.location.hash;
            const btnSpan = button.querySelector('span');
            navigator.clipboard.writeText(cleanUrl)
                .then(() => {
                    const originalText = btnSpan.textContent;
                    btnSpan.textContent = '¡Copiado!';
                    setTimeout(() => btnSpan.textContent = originalText, 1500);
                })
                .catch(err => console.error('No se pudo copiar:', err));
        });
    }
}

customElements.define('share-button-component', ShareButtonComponent);