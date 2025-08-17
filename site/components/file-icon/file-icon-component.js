class FileIconComponent extends HTMLElement {
  async connectedCallback() {
    const response = await fetch('/components/file-icon/file-icon-component.html');
    const html = await response.text();
    this.innerHTML = html;
  }
}

customElements.define('file-icon-component', FileIconComponent);
