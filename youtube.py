from googleapiclient.discovery import build
import os
import random

def convert_song_to_string(current_mood = ''):
    # Gets Random song based on Mood
    mood = get_songs_from_playlist(current_mood)

    song = []
    song_string = ""

    # Adds mood to song list
    for i in mood.keys():
        song.append(f'{i}: {mood[i]}')

    # Converts song list to string
    for s in song:
        song_string += s

    return song_string

# Adds Youtube Playlist items to Python list and randomizes it
def get_songs_from_playlist(mood=''):
    songs = []

    # Gets API Key
    api_key = os.environ.get('API_KEY')
    service = build('youtube','v3',developerKey=api_key)

    # Gets playlist based on Mood
    playlist = service.playlistItems().list(
        part='contentDetails, snippet',
        playlistId=get_mood(mood.capitalize())
    )
    response = playlist.execute()

    # Gets all items Titles and Links and adds it to a list
    for item in response["items"]:
        yt_url = "https://www.youtube.com/watch?v={}".format(item['snippet']['resourceId']['videoId'])
        title = item['snippet']['title']

        songs.append({title: yt_url})

    return random.choice(songs)

# Gets Current Mood and Returns the Playlist ID
def get_mood(mood=''):
    if (mood == 'Happy'):
        happy_playlist = 'PLL4f9qPDeRxzpCgDl0MEcyNTaCxpVaIyX'

        return happy_playlist

    elif (mood == 'Sad'):
        sad_playlist = 'PLL4f9qPDeRxyyui_DAVXh_kmATWGDcv8W'

        return sad_playlist

    elif (mood == 'Angry'):
        angry_playlist = 'PLL4f9qPDeRxyTubOixyNSgIFmdgAkw_OD'

        return angry_playlist