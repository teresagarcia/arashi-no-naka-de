window.addEventListener("load", async () => {
  const params = new URLSearchParams(window.location.search);
  const lyricsFile = params.get('song');

  const dataRes = await fetch(`${lyricsFile}.json`);
  const data = await dataRes.json();
  const entryTitle = `[Letra] ${data.artist} - ${data.song}`;
  document.querySelector('h2').textContent = entryTitle;
  document.querySelector('.intro').innerHTML = data.intro;
  document.querySelector('.content').innerHTML = data.content;
  document.querySelector('.info').innerHTML = data.info;
  document.title = `${entryTitle} | Arashi no naka de`;
})