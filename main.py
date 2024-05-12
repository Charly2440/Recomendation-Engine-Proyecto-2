# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from SpotifyConnection import SpotifyConnection
import pandas as pd
from DataCleanse import DataCleaning

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sp = SpotifyConnection()
    datos_cancion = sp.searchTrack("Psyho Killer")
    url_artista = datos_cancion["artists"][0]["external_urls"]["spotify"]
    #nombre_cancion = datos_cancion.keys()
    #prev = datos_cancion["preview_url"]
    # print(nombre_artista)
    uri = datos_cancion["uri"]
    # print(nombre_cancion)
    audio_features = sp.returnFeatures(uri)
    # #print(datos_cancion)
    #print(sp.getGenresByTrack(url_artista))
    #print(datos_cancion["artists"][0]["name"])
    #print(audio_features[0]["danceability"])

    #canciones = DataCleaning().llenarBD(sp=sp, playlists=["https://open.spotify.com/playlist/37i9dQZF1DWYN0zdqzbEwl"])
    #print(canciones)
    #df = pd.read_csv("DatosCancionesBD.csv", index_col=0)
    #print(df["cancion"])
    generos = DataCleaning().agregarGeneros(sp)
    print(generos)