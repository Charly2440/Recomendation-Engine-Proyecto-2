# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from SpotifyConnection import SpotifyConnection

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
    #print(sp.getPlaylist("https://open.spotify.com/playlist/1RTENWq73MEx1Pop40ZZ5S")["items"][1]["track"])
    #print(len(sp.getPlaylist("https://open.spotify.com/playlist/1RTENWq73MEx1Pop40ZZ5S")["items"]))
    cancionBD = []
    dataPlaylist1 = sp.getPlaylist("https://open.spotify.com/playlist/1RTENWq73MEx1Pop40ZZ5S")["items"]
    dataPlaylist2 = sp.getPlaylist("https://open.spotify.com/playlist/0sDahzOkMWOmLXfTMf2N4N")["items"]
    dataPlaylist3 = sp.getPlaylist("https://open.spotify.com/playlist/5KLKS1zjjeqSe6oRgsdUMb")["items"]
    dataPlaylist4 = sp.getPlaylist("https://open.spotify.com/playlist/1k59k1PJIk5ZJ6ppbFuzgS")["items"]
    dataPlaylist5 = sp.getPlaylist("https://open.spotify.com/playlist/4W4NXbPfqGKyXQEonUa6Nd")["items"]
    dataPlaylist6 = sp.getPlaylist("https://open.spotify.com/playlist/06GeoNaCVRzvplRCEwcmvC")["items"]
    dataPlaylist7 = sp.getPlaylist("https://open.spotify.com/playlist/1Z5OsiAWaOWgxGOADmwnRj")["items"]
    for i in range(99):
        cancionBD.append(dataPlaylist1[i]["track"]["name"])
    for i in range(99):
        if dataPlaylist2[i]["track"]["name"] not in cancionBD:
            cancionBD.append(dataPlaylist2[i]["track"]["name"])
    for i in range(99):
        if dataPlaylist3[i]["track"]["name"] not in cancionBD:
            cancionBD.append(dataPlaylist3[i]["track"]["name"])
    for i in range(99):
        if dataPlaylist4[i]["track"]["name"] not in cancionBD:
            cancionBD.append(dataPlaylist4[i]["track"]["name"])
    for i in range(99):
        if dataPlaylist5[i]["track"]["name"] not in cancionBD:
            cancionBD.append(dataPlaylist5[i]["track"]["name"])
    for i in range(46):
        if dataPlaylist6[i]["track"]["name"] not in cancionBD:
            cancionBD.append(dataPlaylist6[i]["track"]["name"])
    for i in range(59):
        if dataPlaylist7[i]["track"]["name"] not in cancionBD:
            cancionBD.append(dataPlaylist7[i]["track"]["name"])

    print(cancionBD)
    print(len(cancionBD))