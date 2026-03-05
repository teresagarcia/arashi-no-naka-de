class LyricsCardComponent extends HTMLElement {
  set data(value) {
    this._data = value;
    this.render();
  }

  async render() {
    if (!this._data) return;

    if (!this._templateLoaded) {
      const res = await fetch('/components/lyrics-card/lyrics-card-component.html');
      this._template = await res.text();
      this._templateLoaded = true;
    }

    this.innerHTML = this._template;
    const fullLink = `/lyrics.html?song=${this._data.link}`
    this.querySelector('.post-title').innerHTML = `<a href="${fullLink}"
      >[Letra] Arashi - ${this._data.title}</a
    >`;
    this.querySelector('.quote').innerHTML = `<a href="${fullLink}"
        >«${this._data.quote}.»</a
      >`;
    this.querySelector('.read-more').innerHTML = `<a
      href="${fullLink}"
      class="bg-transparent text-blue-secondary hover:bg-blue-back px-4 py-2 rounded-lg transition font-bold"
      >Leer más</a
    >`;
  }
}

customElements.define('lyrics-card-component', LyricsCardComponent);