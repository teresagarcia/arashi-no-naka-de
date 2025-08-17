class CaretIconComponent extends HTMLElement {
  async connectedCallback() {
    const response = await fetch('/components/caret-icon/caret-icon-component.html');
    const html = await response.text();
    this.innerHTML = html;
  }
}

customElements.define('caret-icon-component', CaretIconComponent);
