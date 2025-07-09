class HeaderComponent extends HTMLElement {
  async connectedCallback() {
    const response = await fetch('/components/lyrics/lyrics-component.html');
    const html = await response.text();
    this.innerHTML = html;
  }
}

customElements.define('lyrics-component', HeaderComponent);