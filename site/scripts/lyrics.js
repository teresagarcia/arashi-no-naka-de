window.addEventListener("load", async () => {
  const params = new URLSearchParams(window.location.search);
  const lyricsFile = params.get('song');

  const dataRes = await fetch(`/arashi/${lyricsFile}.json?v=2`);
  const data = await dataRes.json();
  const entryTitle = `[Letra] ${data.artist} - ${data.song}`;
  document.querySelector('h2').textContent = entryTitle;
  document.querySelector('.intro').innerHTML = data.intro;
  document.querySelector('.content').innerHTML = data.content;
  document.querySelector('.info').innerHTML = `<span class='font-bold text-blue-secondary'>Info de la canción:</span><br/>Letra: ${data.lyricist}.<br/>Música: ${data.composer}.<br/>Arreglos: ${data.arranger}.<br/>Álbum: ${data.album}.<br/><br/>`
  document.querySelector('.credits').innerHTML = data.credits;
  document.title = `${entryTitle} | Arashi no naka de`;
})