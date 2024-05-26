# Recomendador de Música

**Autores**

-Juan Luis Solórzano, carnet: 201598

-Carlos Villagrán, carnet: 22264

-Jorge Palacios, carnet: 231385

## Descripción del Programa

El porgrama se centra hacer recomendaciónes de música que ayuda a los usuarios a descubrir nuevas canciones basadas en sus preferencias musicales. Utiliza la API de Spotify para acceder a una amplia gama de datos sobre canciones y artistas. Los usuarios pueden crear perfiles, agregar canciones que les gusten y recibir recomendaciones personalizadas.

## Diseño y relaciones del Programa 

![UML ](https://github.com/Charly2440/Recomendation-Engine-Proyecto-2/assets/134471477/9ed74fb6-2497-4c2a-91ca-7b499c3a320d)


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


  ## Requisitos // Librerías Utilizadas
  
 **Python**: Asegúrate de tener Python 3.7 o superior instalado en tu sistema.
 
 **Librerias de Python**
- neo4j==4.4.3
- pandas==1.3.5
- spotipy==2.19.0
- Pillow==8.4.0
- requests==2.26.0
- tk





