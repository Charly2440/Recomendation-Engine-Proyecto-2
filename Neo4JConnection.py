from neo4j import GraphDatabase
import pandas as pd

URI = "neo4j+s://28159d47.databases.neo4j.io"
AUTH = ("neo4j", "Qw85zsznwNhcIengCsTsSbLY76sVg2Rep0tuRJLMi7o")

#Crear nodos de caracteristicas
#with GraphDatabase.driver(URI,auth=AUTH) as driver:
#    print("Connected to Neo4j")
#    with driver.session() as session:
#        session.run("CREATE (:Feature {name:'Danceability'}), (:Feature {name:'Energy'}), (:Feature {name:'Speachiness'}), (:Feature {name:'Acousticness'}), (:Feature {name:'Tempo'})")

#Funcion para crear nodos y relaciones ponderadas
def createSongNode(cancion,Danceability,Energy,Speech,Acousticness,Tempo):
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session() as session:
            session.run("CREATE (c:Cancion {name: $cancion})", cancion=cancion)
            session.run("""
                                    MATCH (c:Cancion {name: $cancion}), (D:Feature {name: 'Danceability'})
                                    CREATE (c)-[:CONNECTED {weight: $Danceability}]->(D)
                                    """, cancion=cancion, Danceability=Danceability)
            session.run("""
                                    MATCH (c:Cancion {name: $cancion}), (E:Feature {name: 'Energy'})
                                    CREATE (c)-[:CONNECTED {weight: $Energy}]->(E)
                                    """, cancion=cancion, Energy=Energy)
            session.run("""
                                    MATCH (c:Cancion {name: $cancion}), (S:Feature {name: 'Speachiness'})
                                    CREATE (c)-[:CONNECTED {weight: $Speachiness}]->(S)
                                    """, cancion=cancion, Speachiness=Speech)
            session.run("""
                                    MATCH (c:Cancion {name: $cancion}), (A:Feature {name: 'Acousticness'})
                                    CREATE (c)-[:CONNECTED {weight: $Acousticness}]->(A)
                                    """, cancion=cancion, Acousticness=Acousticness)
            session.run("""
                                    MATCH (c:Cancion {name: $cancion}), (T:Feature {name: 'Tempo'})
                                    CREATE (c)-[:CONNECTED {weight: $Tempo}]->(T)
                                    """, cancion=cancion, Tempo=Tempo)

#Datos para llenar base de datos
df = pd.read_csv("DatosCancionesBD.csv")

#prueba, exitosa
prueba1 = df.iloc[0]

#createSongNode(prueba1["cancion"], prueba1["danceability"], prueba1["energy"], prueba1["speachiness"], prueba1["acousticness"], prueba1["tempo"])

#llenando base de datos con complementos
#for i in range(len(df["cancion"])-1):
#    nodo = df.iloc[i+1]
#    createSongNode(nodo["cancion"], str(1.-float(nodo["danceability"])), str(1.-float(nodo["energy"])), str(1.-float(nodo["speachiness"])), str(1.-float(nodo["acousticness"])), str(1.-float(nodo["tempo"])))

