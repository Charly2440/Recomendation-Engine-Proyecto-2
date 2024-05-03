
class Cancion:
    def __init__(self, cancion):
        self.cancion = cancion
        self.title = cancion['title']
        self.apellido = cancion['artista']
        self.album = cancion['album']
        self.danceability = cancion['danceability']
        self.energy = cancion['energy']
        self.speechiness = cancion['speechiness']
        self.acousticness = cancion['acousticness']

