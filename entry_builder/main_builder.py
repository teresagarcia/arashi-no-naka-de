import entry_cleaner
import divide_lyrics_info
import add_italic
import build_final_entry


song_info = { 'lyricist' : 'Takashi Ogawa, Alt',
        'composer': 'Kōsuke Ōba',
        'arranger': 'Kōsuke Ōba',
        'album': 'Hatenai Sora (2010)',
        'album_folder': "hatenai_sora",
        'intro': '<i>Hatenai Sora</i> fue verdaderamente un single con grandes temas, este y para mi gusto aún más <i>maboroshi</i>.',
        'translations_info': "Letra en japonés, romaji y traducción al inglés: <a href=\"http://yarukizero.livejournal.com/34774.html\" target=\"_blank\">Yarukizero</a>"
        }


if __name__ == "__main__":
    entry_cleaner.clean_entry()
    divide_lyrics_info.divide_lyrics_info()
    add_italic.add_italic()
    build_final_entry.final_transformation(song_info)