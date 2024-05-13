from neo4j import GraphDatabase
import pandas as pd
from random import randint
import ast

URI = "neo4j+s://28159d47.databases.neo4j.io"
AUTH = ("neo4j", "Qw85zsznwNhcIengCsTsSbLY76sVg2Rep0tuRJLMi7o")

#Crear nodos de caracteristicas
def createFeatureNode():
    with GraphDatabase.driver(URI,auth=AUTH) as driver:
        with driver.session() as session:
            session.run("CREATE (:Feature {name:'Danceability'}), (:Feature {name:'Energy'}), (:Feature {name:'Speachiness'}), (:Feature {name:'Acousticness'}), (:Feature {name:'Tempo'})")

#Funcion para crear nodos y relaciones ponderadas
def createSongNode(cancion,Danceability,Energy,Speech,Acousticness,Tempo):
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session() as session:
            session.run("MERGE (c:Cancion {name: $cancion})", cancion=cancion)
            session.run("""
                                    MATCH (c:Cancion {name: $cancion}), (D:Feature {name: 'Danceability'})
                                    MERGE (c)-[:CONNECTED {weight: $Danceability}]->(D)
                                    """, cancion=cancion, Danceability=1-Danceability)
            session.run("""
                                    MATCH (c:Cancion {name: $cancion}), (E:Feature {name: 'Energy'})
                                    MERGE (c)-[:CONNECTED {weight: $Energy}]->(E)
                                    """, cancion=cancion, Energy=1-Energy)
            session.run("""
                                    MATCH (c:Cancion {name: $cancion}), (S:Feature {name: 'Speachiness'})
                                    MERGE (c)-[:CONNECTED {weight: $Speachiness}]->(S)
                                    """, cancion=cancion, Speachiness=1-Speech)
            session.run("""
                                    MATCH (c:Cancion {name: $cancion}), (A:Feature {name: 'Acousticness'})
                                    MERGE (c)-[:CONNECTED {weight: $Acousticness}]->(A)
                                    """, cancion=cancion, Acousticness=1-Acousticness)
            session.run("""
                                    MATCH (c:Cancion {name: $cancion}), (T:Feature {name: 'Tempo'})
                                    MERGE (c)-[:CONNECTED {weight: $Tempo}]->(T)
                                    """, cancion=cancion, Tempo=1-Tempo)

#Datos para llenar base de datos
df = pd.read_csv("DatosCancionesGenresArtists.csv")

#prueba, exitosa
prueba1 = df.iloc[0]

#createSongNode(prueba1["cancion"], prueba1["danceability"], prueba1["energy"], prueba1["speachiness"], prueba1["acousticness"], prueba1["tempo"])

#llenando base de datos con complementos
#for i in range(len(df["cancion"])-1):
#    nodo = df.iloc[i+1]
#    createSongNode(nodo["cancion"], str(1.-float(nodo["danceability"])), str(1.-float(nodo["energy"])), str(1.-float(nodo["speachiness"])), str(1.-float(nodo["acousticness"])), str(1.-float(nodo["tempo"])))

#Realizando correciones al valor de las relaciones Tempo
#for i in range(len(df["cancion"])-1):
#    nodo = df.iloc[i+1]
#    with GraphDatabase.driver(URI, auth=AUTH) as driver:
#        with driver.session() as session:
#            session.run("""
#                MATCH (c:Cancion {name: $songName})-[r]->(f:Feature {name: $featureName})
#                SET r.weight = $newWeight
#            """, songName=nodo["cancion"], featureName="Tempo", newWeight = nodo["tempo"])

#Pruebas de lectura
prueba2 = df.iloc[38]
def recomenadarPorFeature(cancion):
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session() as session:
            data = session.run("""
            MATCH (c:Cancion {name: $cancion}) - [r] -> (f:Feature)
            RETURN  f.name as featureName, toFloat(r.weight) as weight
            ORDER BY toFloat(r.weight) ASC
            """, cancion=cancion)
            features = [(record["weight"], record["featureName"]) for record in data]
            feature1 = features[0]
            feature2 = features[1]
            possibleSongsByFeature1 = session.run("""
            MATCH (c:Cancion) - [r] -> (f:Feature {name: $feature})
            WHERE toFloat(r.weight) > $weightL AND toFloat(r.weight) < $weightH
            RETURN c.name as songName, toFloat(r.weight) as Weight
            """, feature=feature1[1], weightL=feature1[0]-0.01, weightH=feature1[0]+0.01)
            possibleSongsByFeature2 = session.run("""
            MATCH (c:Cancion) - [r] -> (f:Feature {name: $feature})
            WHERE toFloat(r.weight) > $weightL AND toFloat(r.weight) < $weightH
            RETURN c.name as songName, toFloat(r.weight) as Weight
            """, feature=feature2[1], weightL=feature2[0]-0.01, weightH=feature2[0]+0.01)

            songs1 = [song["songName"] for song in possibleSongsByFeature1]
            songs2 = [song["songName"] for song in possibleSongsByFeature2]
            commonSongs = []
            for song in songs1:
                for song2 in songs2:
                    if song == song2:
                        commonSongs.append(song)
            if len(commonSongs) != 0 :
                return commonSongs
            else:
                rand = randint(0,len(songs1)-1)
                return songs1[rand]

def recomendarPorGenero(cancion):
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session() as session:
            songGenres = session.run("""
            MATCH (c:Cancion {name: $cancion})-[:BELONGS_TO]->(g:Genero)
            RETURN g.name
            """, cancion=cancion)
            songGenres = songGenres.values()
            rand1 = randint(0, len(songGenres)-1)
            GenreRec = songGenres[rand1][0]
            songsRecommendedByGenre = session.run("""
            MATCH (c:Cancion)-[:BELONGS_TO]->(g:Genero {name: "pop"})
            RETURN c.name
            """)
            songsRecommendedByGenre = songsRecommendedByGenre.values()
            rand2 = randint(0, len(songsRecommendedByGenre)-1)
            SongRecommendedByGenre = songsRecommendedByGenre[rand2][0]
            return SongRecommendedByGenre, GenreRec




#Creando nodos de generos
def crearNodosGeneros(df):
    gens = []
    for i in range(len(df["cancion"])-1):
        generos = df.iloc[i+1]["generos"]
        if type(generos) == str:
            generos = ast.literal_eval(generos)
        if type(generos) == list:
            gens.extend(generos)
    gens = set(gens)

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session() as session:
            for genero in gens:
                session.run("""
                    CREATE (:Genero {name: $genero})
                    """, genero=genero)

def crearNodoGenero(genero):
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session() as session:
            session.run("""
            MERGE (:Genero {name: $genero})
            """, genero=genero)


#Creando relaciones entre canciones y generos
#with GraphDatabase.driver(URI, auth=AUTH) as driver:
#    with driver.session() as session:
#        for i in range(len(df["cancion"])-1):
#            cancion = df.iloc[i+1]["cancion"]
#            generos = df.iloc[i+1]["generos"]
#            if type(generos) == str:
#                generos = ast.literal_eval(generos)
#                for genero in generos:
#                    session.run("""
#                    MATCH (c:Cancion {name: $cancion}), (g:Genero {name: $genero})
#                    MERGE (c)-[:BELONGS_TO]->(g)
#                    """, cancion=cancion, genero=genero)
#
def crearUsuario(usuario):
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session() as session:
            session.run("""
            CREATE (:Usuario {name: $usuario})
            """, usuario=usuario)

def agregarCancionUsuario(usuario, cancion, sp):
    datos_cancion = sp.searchTrack(cancion)
    url_artista = datos_cancion["artists"][0]["external_urls"]["spotify"]
    nombre_artista = datos_cancion["artists"][0]["name"]
    uri = datos_cancion["uri"]
    audio_features = sp.returnFeatures(uri)[0]
    Danceability = audio_features["danceability"]
    Acousticness = audio_features["acousticness"]
    Energy = audio_features["energy"]
    Speech = audio_features["speechiness"]
    Tempo = audio_features["tempo"]

    createSongNode(cancion,Danceability,Energy,Speech,Acousticness,Tempo)

    generos = sp.getGenresByTrack(url_artista)
    for genero in generos:
        crearNodoGenero(genero)
    for genero in generos:
        with GraphDatabase.driver(URI, auth=AUTH) as driver:
            with driver.session() as session:
                session.run("""
                MATCH (c:Cancion {name: $cancion}), (g:Genero {name: $genero})
                MERGE (c)-[:BELONGS_TO]->(g)
                """, cancion=cancion, genero=genero)

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session() as session:
            session.run("""
            MATCH (u:Usuario {name: $usuario}), (c:Cancion {name: $cancion})
            MERGE (u)-[:LIKES]->(c)
            """, cancion=cancion, usuario=usuario)
