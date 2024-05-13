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

        songsAndFeatures = {}
        danceability = []
        energy = []
        speechiness = []
        acousticness = []
        tempo = []

        for i in range(len(uriList)):
            if uriList[i] is not None:
                feats = sp.returnFeatures(uriList[i])[0]
                songsAndFeatures[cancionesBD[i]] = sp.returnFeatures(uriList[i])[0]
                danceability.append(feats["danceability"])
                energy.append(feats["energy"])
                speechiness.append(feats["speechiness"])
                acousticness.append(feats["acousticness"])
                tempo.append(feats["tempo"])
            else:
                songsAndFeatures[cancionesBD[i]] = {'danceability': pd.NA, 'energy': pd.NA, 'key': pd.NA, 'loudness': pd.NA, 'mode': pd.NA, 'speechiness': pd.NA, 'acousticness': pd.NA, 'instrumentalness': pd.NA, 'liveness': pd.NA, 'valence': pd.NA, 'tempo': pd.NA, 'type': 'audio_features', 'id': 'Not found', 'uri': 'Not found', 'track_href': 'Not found', 'analysis_url': 'Not found', 'duration_ms': pd.NA, 'time_signature': pd.NA}
                danceability.append(pd.NA)
                energy.append(pd.NA)
                speechiness.append(pd.NA)
                acousticness.append(pd.NA)
                tempo.append(pd.NA)

        df = pd.DataFrame({"cancion": cancionesBD,"danceability": danceability, "energy": energy, "speachiness": speechiness, "acousticness": acousticness,"tempo": tempo})
        df.to_csv("DatosCancionesBD.csv")

        return songsAndFeatures

    def agregarGeneros(self, sp):
        df = pd.read_csv("DatosCancionesBD.csv")
        genres = []
        for nombre in df["cancion"]:
            try:
                url_artist = sp.searchTrack(nombre)["artists"][0]["external_urls"]["spotify"]
                genre = sp.getGenresByTrack(url_artist)
                genres.append(genre)
            except IndexError:
                genres.append(pd.NA)
        df["generos"] = genres
        df.to_csv("DatosCancionesGenres.csv")
        return genres

    def agregarArtistas(self, sp):
        df = pd.read_csv("DatosCancionesBD.csv")
        artists = []
        for nombre in df["cancion"]:
            try:
                artist = sp.searchTrack(nombre)["artists"][0]["name"]
                artists.append(artist)
            except IndexError:
                artists.append(pd.NA)
        df["artista"] = artists
        df.to_csv("DatosCancionesGenresArtists.csv")
        return artists




