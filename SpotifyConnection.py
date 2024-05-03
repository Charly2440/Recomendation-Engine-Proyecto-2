import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os


class SpotifyConnection:
    def __init__(self):
        self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id= "f723f8a096c44adfa51ddbd6298890b4", client_secret= "1be267b9427d4488978841f8e985ba96"))

    def searchTrack(self, track, index=1):
        return (list(self.spotify.search(q="track: "+ track, type=['track'], limit =index).values()))[0]["items"][index-1]

    def returnFeatures(self, uri):
        return self.spotify.audio_features(uri)

    def getGenresByTrack(self, url):
        return self.spotify.artist(url)["genres"]

    def getPlaylist(self, uri):
        return self.spotify.playlist_items(uri, limit=100)


