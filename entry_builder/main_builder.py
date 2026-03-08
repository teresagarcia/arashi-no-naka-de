import entry_cleaner
import divide_lyrics_info
import add_italic
import build_final_entry


song_info = { 'lyricist' : 'BASI, Sho Sakurai',
        'composer': 'Insist',
        'arranger': 'Insist',
        'album': 'Are you happy? (2016)',
        'album_folder': "are_you_happy",
        'intro': 'Canción adorable como son ellos.',
        'translations_info':" Letra en japonés, romaji y traducción al inglés: <a href=\"https://tamagoes.livejournal.com/9209.html\" target=\"_blank\">Tamagoes</a>"
        }


if __name__ == "__main__":
    entry_cleaner.clean_entry()
    divide_lyrics_info.divide_lyrics_info()
    add_italic.add_italic()
    build_final_entry.final_transformation(song_info)