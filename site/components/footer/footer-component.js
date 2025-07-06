class FooterComponent extends HTMLElement {
  async connectedCallback() {
    const response = await fetch('/components/footer/footer-component.html');
    const html = await response.text();
    this.innerHTML = html;
  }
}

customElements.define('footer-component', FooterComponent);
