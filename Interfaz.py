
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import Neo4JConnection
from SpotifyConnection import SpotifyConnection
from random import randint

# Variables globales
nombre = ""
cancion = ""


def guardar_datos():
    global nombre, cancion
    nombre = name_entry.get()
    cancion = song_entry.get()
    Neo4JConnection.crearUsuario(nombre)
    Neo4JConnection.agregarCancionUsuario(nombre, cancion, sp=SpotifyConnection())

    abrir_ventana_opciones()


def acceder_datos():
    global nombre
    nombre = name_entry.get()
    abrir_ventana_opciones()


def abrir_ventana_agregar_cancion():
    # Función para guardar el nombre de la canción ingresado por el usuario
    #agregarCancionUsuario(nombre, cancion, sp=SpotifyConnection())
    def guardar_nombre_cancion():
        global nombre_cancion
        nombre_cancion = entry_nombre_cancion.get()
        print("Nombre de la canción guardado:", nombre_cancion)
        Neo4JConnection.agregarCancionUsuario(nombre, cancion, sp=SpotifyConnection())
        ventana_agregar_cancion.destroy()

    # Crear ventana para agregar canción
    ventana_agregar_cancion = tk.Toplevel(root)
    ventana_agregar_cancion.title("Agregar Canción")

    # Etiqueta y campo de entrada para el nombre de la canción
    label_nombre_cancion = tk.Label(ventana_agregar_cancion, text="Nombre de la canción:")
    label_nombre_cancion.pack()

    entry_nombre_cancion = tk.Entry(ventana_agregar_cancion)
    entry_nombre_cancion.pack()

    # Botón para guardar el nombre de la canción
    button_guardar = tk.Button(ventana_agregar_cancion, text="Guardar", command=guardar_nombre_cancion)
    button_guardar.pack()


def abrir_ventana_opciones():
    ventana_opciones = tk.Toplevel(root)
    ventana_opciones.title("Opciones")
    ventana_opciones.configure(bg='#010101')
    label = tk.Label(ventana_opciones, text=f"Bienvenido {nombre}, elige una opción:")

    label.pack(pady=10)

    # Botón para agregar canción
    button_agregarCancion = tk.Button(ventana_opciones, text="Agregar canción", command=abrir_ventana_agregar_cancion)
    button_agregarCancion.pack(pady=5)

    # Botón para mostrar recomendaciones
    button_recomendar = tk.Button(ventana_opciones, text="Mostrar recomendaciones", command=mostrar_recomendaciones)
    button_recomendar.pack(pady=5)


def mostrar_ventana1():
    label_name.pack()
    name_entry.pack()
    label_song.pack()
    song_entry.pack()
    save_button.pack()
    button_regresar.pack()
    ocultar_botones_iniciales()


def mostrar_ventana2():
    label_name.pack()
    name_entry.pack()
    acces_button.pack()
    button_regresar.pack()
    ocultar_botones_iniciales()


def resize_image(image_path):
    imagen = Image.open(BytesIO(requests.get(image_path).content))
    width, height = imagen.size
    new_width = int(width * 0.251)
    new_height = int(height * 0.251)
    resized_image = imagen.resize((new_width, new_height))
    return ImageTk.PhotoImage(resized_image)


def mostrar_recomendaciones():
    # Lista de URLs de imágenes
    canciones = list(Neo4JConnection.cancionesUsuario(nombre))
    cancion = canciones[randint(0,len(canciones)-1)]

    l = Neo4JConnection.recomenadarPorFeature(cancion)[:5]


    urls_imagenes = []

    # Lista de URLs de canciones
    urls_canciones = []
    for v in l:
        datos = Neo4JConnection.obtenerDatosCancion(v)
        if datos['imagen'] != None:
            urls_imagenes.append(datos['imagen'])
            urls_canciones.append(datos['url'])
    print( urls_imagenes)
    print(urls_canciones )

        # Función para redimensionar las imágenes al 10% de su tamaño original

    # Crear nueva ventana para recomendaciones
    ventana_recomendaciones = tk.Toplevel(root)
    ventana_recomendaciones.title("Recomendaciones")

    # Crear y mostrar botones con imágenes y enlaces
    for i, url_imagen in enumerate(urls_imagenes):
        imagen_reducida = resize_image(url_imagen)
        boton = tk.Button(ventana_recomendaciones, image=imagen_reducida,
                          command=lambda link=urls_canciones[i]: abrir_enlace(link))
        boton.image = imagen_reducida  # Mantener referencia a la imagen para evitar que se elimine por el recolector de basura
        boton.pack(pady=5)


def abrir_enlace(link):
    import webbrowser
    webbrowser.open_new_tab(link)


def agregar_cancion():
    song_entry.pack()
    save_button.pack_forget()


def regresar():
    mostrar_botones_iniciales()
    label_name.pack_forget()
    name_entry.pack_forget()
    label_song.pack_forget()
    song_entry.pack_forget()
    save_button.pack_forget()
    acces_button.pack_forget()
    button_recomendar.pack_forget()
    button_regresar.pack_forget()


def ocultar_botones_iniciales():
    button1.pack_forget()
    button2.pack_forget()


def mostrar_botones_iniciales():
    button1.pack(pady=10)
    button2.pack(pady=10)


root = tk.Tk()
root.title("ReDeMu")

# Estilo para un aspecto vintage
root.configure(bg='#010101')  # Color de fondo

# Crear elementos para la primera "ventana"
label_name = tk.Label(root, text="Ingrese su nombre:")
name_entry = tk.Entry(root)

label_song = tk.Label(root, text="Ingrese el nombre de una canción:")
song_entry = tk.Entry(root)

save_button = tk.Button(root, text="Guardar", command=guardar_datos,  bg='#99ff99')

acces_button = tk.Button(root, text="Acceder", command=acceder_datos, bg='#99ff99')

# Botón para agregar canción al grafo
button_agregarCancion = tk.Button(root, text="Agregar canción", command=agregar_cancion, bg='#99ff99')

# Botón para mostrar recomendaciones
button_recomendar = tk.Button(root, text="Mostrar recomendaciones", command=mostrar_recomendaciones, bg='#99ff99')

# Botón para regresar
button_regresar = tk.Button(root, text="Regresar", command=regresar, bg='#99ff99')

# Crear elementos para la segunda "ventana"
label_options = tk.Label(root, text="Select and fill options:")

# Cargar imagen desde URL
url = "https://i.pinimg.com/originals/55/ee/ca/55eecaefc6d40db5cd2b87238f4e8066.jpg"
response = requests.get(url)
image_data = response.content
image = Image.open(BytesIO(image_data))
image = ImageTk.PhotoImage(image)
label_image = tk.Label(root, image=image)
label_image.pack(pady=10)

# Botones para cambiar entre "ventanas"
button1 = tk.Button(root, text="Crear usuario nuevo", command=mostrar_ventana1, bg='#99ff99')  # Color de botón
button1.pack(pady=10)

button2 = tk.Button(root, text="Acceder a usuario existente", command=mostrar_ventana2, bg='#99ff99')  # Color de botón
button2.pack(pady=10)

root.mainloop()
