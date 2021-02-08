import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# results = spotify.playlist(happy_playlist_uri)
results = spotify.track()

#Currently researching into api