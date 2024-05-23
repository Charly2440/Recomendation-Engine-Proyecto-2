# Recomendador de Música

## Descripción del Programa

El porgrama se centra hacer recomendaciónes de música que ayuda a los usuarios a descubrir nuevas canciones basadas en sus preferencias musicales. Utiliza la API de Spotify para acceder a una amplia gama de datos sobre canciones y artistas. Los usuarios pueden crear perfiles, agregar canciones que les gusten y recibir recomendaciones personalizadas.

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



