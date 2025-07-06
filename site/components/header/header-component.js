class HeaderComponent extends HTMLElement {
  async connectedCallback() {
    const response = await fetch('/components/header/header-component.html');
    const html = await response.text();
    this.innerHTML = html;
  }
}

customElements.define('header-component', HeaderComponent);
