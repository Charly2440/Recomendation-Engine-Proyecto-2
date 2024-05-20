import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Variables globales
nombre = ""
cancion = ""


def guardar_datos():
    global nombre, cancion
    nombre = name_entry.get()
    cancion = song_entry.get()
    print("Nombre guardado:", nombre)
    print("Canción guardada:", cancion)
    abrir_ventana_opciones()


def acceder_datos():
    global nombre
    nombre = name_entry.get()
    abrir_ventana_opciones()


def abrir_ventana_opciones():
    ventana_opciones = tk.Toplevel(root)
    ventana_opciones.title("Opciones")

    label = tk.Label(ventana_opciones, text=f"Bienvenido {nombre}, elige una opción:")
    label.pack(pady=10)

    # Botón para agregar canción
    button_agregarCancion = tk.Button(ventana_opciones, text="Agregar canción", command=agregar_cancion)
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


'''
def mostrar_recomendaciones():
    # Cargar imagen desde URL
    url_imagen = "https://i.scdn.co/image/ab67616d0000b273e71708b667804f6241dd1a59"
    response = requests.get(url_imagen)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    image = ImageTk.PhotoImage(image)

    # Crear un botón con la imagen
    boton_imagen = tk.Button(root, image=image, command=abrir_url, bg='#99ff99')
    boton_imagen.image = image  # Guardar una referencia para evitar que la imagen sea recolectada por el GC
    boton_imagen.pack(pady=10)

    print('Recomendaciones mostradas')

'''
'''
def mostrar_recomendaciones():
    # Lista de URLs de imágenes
    urls_imagenes = [
        "https://i.scdn.co/image/ab67616d0000b273e71708b667804f6241dd1a59",
        "https://i.scdn.co/image/ab67616d0000b273e71708b667804f6241dd1a59",
        "https://upload.wikimedia.org/wikipedia/en/0/0d/Mike_oldfield_tubular_bells_album_cover.jpg",
        "https://i.scdn.co/image/ab67616d0000b273e71708b667804f6241dd1a59",
        "https://upload.wikimedia.org/wikipedia/en/0/0d/Mike_oldfield_tubular_bells_album_cover.jpg"
    ]

    # Lista de URLs de canciones
    urls_canciones = [
        "https://open.spotify.com/intl-es/track/58vy7wj08LvhnSRu8mxvAd?si=9fb80aa5fc3d4c2b",
        "https://open.spotify.com/intl-es/track/7HmuloxW2LLiPu0lcmkjoq?si=47657a191cfc4a18",
        "https://open.spotify.com/intl-es/track/7ERSQrRptZVM7q3VOdM7OL?si=95b1eb4e1cd64f2b",
        "https://open.spotify.com/intl-es/track/7pKfPomDEeI4TPT6EOYjn9?si=bb97db917df643b8",
        "https://open.spotify.com/intl-es/track/6KI7wfdhXBJF7hLh25Ljp5?si=529ecd9d557f40ff"
    ]

    # Crear nueva ventana para recomendaciones
    ventana_recomendaciones = tk.Toplevel(root)
    ventana_recomendaciones.title("Recomendaciones")

    # Crear y mostrar botones con imágenes y enlaces
    for i, url_imagen in enumerate(urls_imagenes):
        imagen = Image.open(BytesIO(requests.get(url_imagen).content))
        imagen = ImageTk.PhotoImage(imagen)
        boton = tk.Button(ventana_recomendaciones, image=imagen, command=lambda link=urls_canciones[i]: abrir_enlace(link))
        boton.image = imagen  # Mantener referencia a la imagen para evitar que se elimine por el recolector de basura
        boton.pack(pady=5)

def abrir_enlace(link):
    import webbrowser
    webbrowser.open_new_tab(link)
'''


def resize_image(image_path):
    imagen = Image.open(BytesIO(requests.get(image_path).content))
    width, height = imagen.size
    new_width = int(width * 0.251)
    new_height = int(height * 0.251)
    resized_image = imagen.resize((new_width, new_height))
    return ImageTk.PhotoImage(resized_image)


def mostrar_recomendaciones():
    # Lista de URLs de imágenes
    urls_imagenes = [
        "https://i.scdn.co/image/ab67616d0000b273e71708b667804f6241dd1a59",
        "https://i.scdn.co/image/ab67616d0000b273e71708b667804f6241dd1a59",
        "https://upload.wikimedia.org/wikipedia/en/0/0d/Mike_oldfield_tubular_bells_album_cover.jpg",
        "https://i.scdn.co/image/ab67616d0000b273e71708b667804f6241dd1a59",
        "https://upload.wikimedia.org/wikipedia/en/0/0d/Mike_oldfield_tubular_bells_album_cover.jpg"
    ]

    # Lista de URLs de canciones
    urls_canciones = [
        "https://open.spotify.com/intl-es/track/58vy7wj08LvhnSRu8mxvAd?si=9fb80aa5fc3d4c2b",
        "https://open.spotify.com/intl-es/track/7HmuloxW2LLiPu0lcmkjoq?si=47657a191cfc4a18",
        "https://open.spotify.com/intl-es/track/7ERSQrRptZVM7q3VOdM7OL?si=95b1eb4e1cd64f2b",
        "https://open.spotify.com/intl-es/track/7pKfPomDEeI4TPT6EOYjn9?si=bb97db917df643b8",
        "https://open.spotify.com/intl-es/track/6KI7wfdhXBJF7hLh25Ljp5?si=529ecd9d557f40ff"
    ]

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
root.configure(bg='#d2efd8')  # Color de fondo

# Crear elementos para la primera "ventana"
label_name = tk.Label(root, text="Ingrese su nombre:")
name_entry = tk.Entry(root)

label_song = tk.Label(root, text="Ingrese el nombre de una canción:")
song_entry = tk.Entry(root)

save_button = tk.Button(root, text="Guardar", command=guardar_datos)

acces_button = tk.Button(root, text="Acceder", command=acceder_datos)

# Botón para agregar canción al grafo
button_agregarCancion = tk.Button(root, text="Agregar canción", command=agregar_cancion, bg='#99ff99')

# Botón para mostrar recomendaciones
button_recomendar = tk.Button(root, text="Mostrar recomendaciones", command=mostrar_recomendaciones, bg='#99ff99')

# Botón para regresar
button_regresar = tk.Button(root, text="Regresar", command=regresar, bg='#99ff99')

# Crear elementos para la segunda "ventana"
label_options = tk.Label(root, text="Select and fill options:")

# Cargar imagen desde URL
url = "https://i.scdn.co/image/ab67616d0000b273e71708b667804f6241dd1a59"
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

