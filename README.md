# Recomendador de Música

**Autores**

-Juan Luis Solórzano, carnet: 201598

-Carlos Villagrán, carnet: 22264

-Jorge Palacios, carnet: 231385

## Descripción del Programa

El porgrama se centra hacer recomendaciónes de música que ayuda a los usuarios a descubrir nuevas canciones basadas en sus preferencias musicales. Utiliza la API de Spotify para acceder a una amplia gama de datos sobre canciones y artistas. Los usuarios pueden crear perfiles, agregar canciones que les gusten y recibir recomendaciones personalizadas.

## Diseño y relaciones del Programa 

![UML ](https://github.com/Charly2440/Recomendation-Engine-Proyecto-2/assets/134471477/9ed74fb6-2497-4c2a-91ca-7b499c3a320d)

**Relaciones de las canciones por genero:** 

![visualisation (1)](https://github.com/Charly2440/Recomendation-Engine-Proyecto-2/assets/134471477/a7bcee5e-1a0b-47d9-bf98-2e13be4a995b)

**Relaciones de las canciones por Feature (características):**

![visualisation (2)](https://github.com/Charly2440/Recomendation-Engine-Proyecto-2/assets/134471477/511117f0-cce2-46b4-8f69-ef1abbb2d0c4)

**Relaciones de los usuarios por Likes (gustos):** 

![visualisation (3)](https://github.com/Charly2440/Recomendation-Engine-Proyecto-2/assets/134471477/0bc45ce0-21cb-4585-9d2c-1cf0adfa0b1e)


## Funcionalidades Principales

1. **Creación de Perfiles de Usuario**
   - Los usuarios pueden crear perfiles ingresando su nombre y algunas de sus canciones favoritas.

2. **Agregar Canciones**
   - Los usuarios pueden agregar más canciones a su perfil para mejorar las recomendaciones.

3. **Recomendaciones Personalizadas**
   - Basado en las canciones que el usuario ha agregado, ReDeMu genera recomendaciones personalizadas de nuevas canciones.
   - Las recomendaciones pueden ser en función de características musicales similares o del género de las canciones preferidas.

4. **Explorar Nuevas Canciones**
   - Los usuarios pueden explorar nuevas canciones recomendadas y acceder a ellas directamente mediante al programa que proporciona las canciones y estas se abren en Spotify.

## Diagrama de funcionalidad 

![Diagrama](https://github.com/Charly2440/Recomendation-Engine-Proyecto-2/assets/134471477/f023fcaf-f856-42c5-a7be-75f228a85a86)


## Cómo Funciona

1. **Perfil de Usuario**
   - Cuando un usuario crea un perfil, ingresa su nombre y alguna cancion que le gusten.
   - Estas canciones se utilizan para comprender los gustos musicales del usuario.

2. **Análisis de Preferencias**
   - Se analiza las características musicales de las canciones preferidas del usuario.

3. **Generación de Recomendaciones**
   - Con base en las características de las canciones preferida, el programa busca nuevas canciones que compartan características similares.
  

4. **Interacción con Spotify**
   - Se utiliza la API de Spotify para acceder a información detallada sobre canciones y artistas, así como para reproducir las canciones recomendadas.
  
   ## Capturas de Pantalla del Programa

   **Pantalla de Incio**
   
![Screenshot 2024-05-25 at 6 26 27 PM](https://github.com/Charly2440/Recomendation-Engine-Proyecto-2/assets/134471477/76732851-d9ad-491b-a4e5-df81c6e3ea8e)


**Creacion de Usuario** 

![Screenshot 2024-05-25 at 6 28 19 PM](https://github.com/Charly2440/Recomendation-Engine-Proyecto-2/assets/134471477/2b50e6a5-a0a0-4b5d-8050-b66d1d20de3f)

**Inicio De Sesion** 

![Screenshot 2024-05-25 at 6 33 13 PM](https://github.com/Charly2440/Recomendation-Engine-Proyecto-2/assets/134471477/7e505a3c-8991-4d60-a4a7-a7f088876c2e)

**Despues de Inciar sesion** 

![Screenshot 2024-05-25 at 6 33 58 PM](https://github.com/Charly2440/Recomendation-Engine-Proyecto-2/assets/134471477/ce5517ae-4aec-4cde-bc75-1c177877c645)

**Recomendaciones** 

![recomendacionesSS](https://github.com/Charly2440/Recomendation-Engine-Proyecto-2/assets/134471477/e3c24dfa-1795-4a2c-9cbe-18c6be2aed6e)



  ## Requisitos // Librerías Utilizadas
  
 **Python**: Asegúrate de tener Python 3.7 o superior instalado en tu sistema.
 
 **Librerias de Python**
- neo4j==4.4.3
- pandas==1.3.5
- spotipy==2.19.0
- Pillow==8.4.0
- requests==2.26.0
- tk





## Instalaciòn // Clonar un repositorio de GitHub

- Ya al cumplir con los requisitos para el uso del programa , lo unico que queda seria probarlo .

### Desde la línea de comandos

1. **Instalar Git**: Descarga e instala Git desde [git-scm.com](https://git-scm.com/). Durante la instalación, asegúrate de seleccionar la opción de añadir Git a tu PATH.
2. **Obtener la URL del repositorio**: Copia la URL del repositorio en GitHub.
3. **Abrir la terminal**:
   - En Windows, abre **Git Bash** (instalado con Git) o **PowerShell**.
   - Navega a la carpeta donde deseas clonar el repositorio:
    ```sh
    cd ruta/a/tu/carpeta
    ```
   - Clona el repositorio:
    ```sh
    git clone (https://github.com/Charly2440/Recomendation-Engine-Proyecto-2.git)
    ```

### Desde Visual Studio Code

1. **Abrir Visual Studio Code**.
2. **Abrir la pestaña de Control de Fuente**:
   - Haz clic en el icono de ramificación en la barra lateral izquierda.
3. **Clonar el repositorio**:
   - Haz clic en los tres puntos (...) en la parte superior de la pestaña de Control de Fuente.
   - Selecciona "Clonar".
   - Pega la URL del repositorio y presiona Enter.
4. **Seleccionar la carpeta de destino**:
   - Elige la carpeta donde deseas clonar el repositorio.
5. **Abrir el repositorio clonado**:
   - Visual Studio Code te preguntará si quieres abrir el repositorio recién clonado. Haz clic en "Abrir" para comenzar a trabajar con los archivos.

### Desde GitHub Desktop

1. **Instalar GitHub Desktop**: Descarga e instala desde [desktop.github.com](https://desktop.github.com/).
2. **Abrir GitHub Desktop**.
3. **Iniciar sesión en GitHub**: Si no lo has hecho, inicia sesión con tu cuenta de GitHub.
4. **Clonar el repositorio**:
   - Haz clic en `File` > `Clone repository`.
   - En la pestaña `URL`, pega la URL del repositorio de GitHub.
   - Selecciona la carpeta de destino en tu computadora.
   - Haz clic en `Clone` para clonar el repositorio.

### Notas para usuarios de Windows

- **Git Bash**: Es una terminal específica de Git que se instala junto con Git para Windows. Ofrece un entorno similar a Unix.
- **PowerShell**: Es la terminal predeterminada de Windows y también puede usarse para ejecutar comandos de Git.

Estos pasos te permitirán clonar y tener el repositorio del programa de manera rápida y sencilla, ya sea desde la línea de comandos, Visual Studio Code, o GitHub Desktop.

# Y ya teniendo el codigo en tu IDE de preferencia , solo corre el archivo Interfaz.py 

![Screenshot 2024-05-25 at 9 33 06 PM](https://github.com/Charly2440/Recomendation-Engine-Proyecto-2/assets/134471477/fb58a7f7-cb2a-407e-8d4e-882bb303b457)

y veras que se abre una ventana similar a las que se ven en el apartado de Capturas de Pantalla .




