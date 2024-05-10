import pandas as pd
class DataCleaning:

    def __init__(self):
        self = self

    def llenarBD(self, sp, playlists):
        playlistsNames = ["https://open.spotify.com/playlist/1RTENWq73MEx1Pop40ZZ5S",
                     "https://open.spotify.com/playlist/0sDahzOkMWOmLXfTMf2N4N",
                     "https://open.spotify.com/playlist/5KLKS1zjjeqSe6oRgsdUMb",
                     "https://open.spotify.com/playlist/1k59k1PJIk5ZJ6ppbFuzgS",
                     "https://open.spotify.com/playlist/4W4NXbPfqGKyXQEonUa6Nd",
                     "https://open.spotify.com/playlist/06GeoNaCVRzvplRCEwcmvC",
                     "https://open.spotify.com/playlist/1Z5OsiAWaOWgxGOADmwnRj"]
        playlistsNames.extend(playlists)
        cancionesBD = []
        for i in playlistsNames:
            dataplaylists = sp.getPlaylist(i)["items"]

            for j in range(len(dataplaylists)):

                if dataplaylists[j]["track"]["name"] not in cancionesBD:
                    cancionesBD.append(dataplaylists[j]["track"]["name"])

        uriList = []
        for i in cancionesBD:
            try:
                uriList.append(sp.searchTrack(i)["uri"])
            except IndexError:
                uriList.append(None)

        features = []
        songsAndFeatures = {}
        for i in range(len(uriList)):
            if uriList[i] is not None:
                features.append(sp.returnFeatures(uriList[i]))
                songsAndFeatures[cancionesBD[i]] = features
            else:
                features.append(None)
                songsAndFeatures[cancionesBD[i]] = [{'danceability': pd.NA, 'energy': pd.NA, 'key': pd.NA, 'loudness': pd.NA, 'mode': pd.NA, 'speechiness': pd.NA, 'acousticness': pd.NA, 'instrumentalness': pd.NA, 'liveness': pd.NA, 'valence': pd.NA, 'tempo': pd.NA, 'type': 'audio_features', 'id': 'Not found', 'uri': 'Not found', 'track_href': 'Not found', 'analysis_url': 'Not found', 'duration_ms': pd.NA, 'time_signature': pd.NA}]



        return songsAndFeatures

