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

def acceder():
    global nombre
    nombre = name_entry.get()

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
    save_button.pack()
    button_recomendar.pack()
    button_agregarCancion.pack()
    button_regresar.pack()
    ocultar_botones_iniciales()

def mostrar_recomendaciones():
    # Cargar imagen desde URL
    url_imagen = "https://i.scdn.co/image/ab67616d0000b273e71708b667804f6241dd1a59"
    response = requests.get(url_imagen)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    image = ImageTk.PhotoImage(image)
    # Crear un botón con la imagen
    boton_imagen = tk.Button(root, image=image, command=abrir_url, bg='#99ff99')
    boton_imagen.pack(pady=10)

    print('moco')

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

label_song = tk.Label(root, text="Ingrese el nombre de una cancion:")
song_entry = tk.Entry(root)

save_button = tk.Button(root, text="guardar", command=guardar_datos)

# Botón para agrerar cancion al grafo
button_agregarCancion = tk.Button(root, text="Agregar cancion", command=agregar_cancion, bg='#99ff99')

# Botón para mostrar recomendaciones
button_recomendar = tk.Button(root, text="Acceder a lista de recomendaciones", command=mostrar_recomendaciones, bg='#99ff99')

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

