from requests import get
import json

from clear_song_name import clear_song_name


def get_current_song_name():
    request = get('https://api.dubtrack.fm/room/huntownicy').text
    json_data = json.loads(request)

    current_song = json_data['data']['currentSong']

    if current_song is not None:
        return clear_song_name(current_song['name'])
    else:
        return ''
