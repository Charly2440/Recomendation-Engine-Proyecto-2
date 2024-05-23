# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from SpotifyConnection import SpotifyConnection
from Neo4JConnection import obtenerDatosCancion, crearUsuario, agregarCancionUsuario, cancionesUsuario, recomendarPorGenero, recomenadarPorFeature
import pandas as pd
from DataCleanse import DataCleaning

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #ejemplo recomendar cancion por feature devuelve lista
    print("Rec por features: ", recomenadarPorFeature("Believer"))
    #por genero devuelve aleatoria una cancion, tuple con nombre y genero
    print("\nRec por genero: ", recomendarPorGenero("Believer"))

    #Ejemplo para obtener los datos de una cancion, devuelve diccionario
    print("\nData cancion: ", obtenerDatosCancion("Believer"))

    #Ejemplo crear usuario
    crearUsuario("CJ21")
    #Ejemplo agregar cancion que le gusta a usuario, necesita nombre de usuario, nombre cancion, y la instancia de SpotifyConnection
    agregarCancionUsuario("CJ21", "Believer", sp=SpotifyConnection())

    #Ejemplo obtener canciones de usuario
    print("\nCanciones usuario CJ21: ", cancionesUsuario("CJ21"))









