class LinkIconComponent extends HTMLElement {
  async connectedCallback() {
    const response = await fetch('/components/link-icon/link-icon-component.html');
    const html = await response.text();
    this.innerHTML = html;
  }
}

customElements.define('link-icon-component', LinkIconComponent);
