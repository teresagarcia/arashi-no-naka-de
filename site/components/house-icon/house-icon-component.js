class HouseIconComponent extends HTMLElement {
  async connectedCallback() {
    const response = await fetch('/components/house-icon/house-icon-component.html');
    const html = await response.text();
    this.innerHTML = html;
  }
}

customElements.define('house-icon-component', HouseIconComponent);
