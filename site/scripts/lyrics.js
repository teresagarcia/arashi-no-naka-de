window.addEventListener("load", async () => {
  const params = new URLSearchParams(window.location.search);
  const lyricsFile = params.get('song');

  const dataRes = await fetch(lyricsFile);
  const data = await dataRes.json();
  document.querySelector('h2').textContent = `[Letra] ${data.artist} - ${data.song}`;
  document.querySelector('.intro').innerHTML = data.intro;
  document.querySelector('.content').innerHTML = data.content;
  document.querySelector('.info').innerHTML = data.info;

})