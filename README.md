# Miru-aplicacion-de-seguimiento-multimedia


## **Descripción General**

El objetivo de este proyecto es desarrollar una aplicación que permita a los usuarios llevar un seguimiento detallado de su contenido multimedia preferido, incluyendo películas, videojuegos, series y anime. Esta aplicación estará diseñada y desarrollada por un equipo de seis integrantes de la Tecnicatura Superior en Ciencias de Datos e Inteligencia Artificial.
La plataforma permitirá a los usuarios gestionar de manera eficiente sus listas de contenido multimedia, agregar nuevo material a la base de datos de la aplicación, y dejar reseñas y valoraciones de los mismos. Además, la aplicación facilitará la búsqueda y organización del contenido mediante el uso de filtros y categorías, mejorando así la experiencia de navegación y acceso a la información.
## Estructura del Proyecto

Miru/
- index.py
- config.py
- user_database.py
- opciones/
  - __init__.py
  - modulo_anime.py
  - modulo_peliculas.py
  - modulo_series.py
  - modulo_juegos.py
  - modulo_listas.py
  - modulo_resena.py
  - modulo_agregar_contenido.py
  - modulo_perfil.py

### Archivos Principales
### `index.py`
Este archivo es el punto de entrada principal de Miru. Aquí se maneja la lógica de inicio de sesión, registro y el Menú principal, utilizando funciones y configuraciones importadas desde otros módulos. 
`index.py` coordina todos los módulos y maneja el flujo de la aplicación, asegurando una experiencia de usuario integrada y fluida.

### ***Importaciones***
**opciones**
Importa módulos específicos para manejar las distintas opciones del menú principal (anime, series, películas, juegos, lista, reseñas, agregar contenido y perfil)
**modulo_user_data**
Importa las funciones para registrar y validar usuarios, así como el diccionario que simula una base de datos de usuarios.
**config**
Importa las configuraciones globales, como colores y caracteres especiales.
### **Funciones**
**limpia_pantalla()**
Limpia la pantalla de la consola
**mensaje_formateado(mensaje=None, color=None, estilo=None, caracter=None)**
Recibe como argumentos opcionales un texto, un color, un estilo y un caracter.
Devuelve el texto en la consola utilizando colores y estilos especificados en el módulo `config`.
**login()**
Se encarga de la fase de inicio de sesión
Permite tres intentos para ingresar el usuario y la contraseña
Si el usuario no puede iniciar sesión, le da la opción de registrarse.
**menu_principal()**
Muestra el menú principal y controla la navegación entre las opciones del menú.
Cada opción llama a la función principal del módulo correspondiente.
### Flujo Principal
Se ejecuta dentro del bloque `if__name__ == "__main__"`, de la siguiente manera:

 1. Menú de Bienvenida
	 Ofrece 3 opciones: 
	- Iniciar Sesión
	- Registrarse
	- Salir
 2. Opciones del Menú de Bienvenida
-   Si el usuario selecciona "Iniciar sesión", se llama a la función `login()`. Si el inicio de sesión es exitoso, se muestra el menú principal mediante `menu_principal()`.
-   Si el usuario selecciona "Registrarse", se llama a la función `registrar_usuario()` para crear una nueva cuenta de usuario.
-   Si el usuario selecciona "Salir", la aplicación termina con un mensaje de despedida.
 4. Control de flujo y mensajes
- El flujo incluye mensajes formateados y limpiado de pantalla para mejorar la experiencia del usuario, utilizando colores y estilos definidos en `config`.
 

## Módulos de opciones del menú principal
### `_ _init__.py`
Convierte el directorio `opciones` en un paquete de Python, permitiendo la importación de sus módulos en otros archivos Python.
  ### `modulo_anime.py`
 - En este se encuentra definida la función main_menu(), que actualmente, sólo se encarga de devolver un mensaje mediante un print indicando la opción seleccionada, cambiara al seguir avanzando el proyecto. 
- En un futura la sección contara con una lista de los animes disponibles en la aplicación.
 ### `modulo_peliculas.py`
En este se encuentra definida la función main_menu(), que actualmente, sólo se encarga de devolver un mensaje mediante un print indicando la opción seleccionada, cambiara al seguir avanzando el proyecto.
-	Cuando se ingresa sección se da el mensaje:  ¡Bienvenidos a la sección Películas! “descubre nuevas películas"
### `opcion_series.py`
-	En este se encuentra definida la función main_menu(), que actualmente, sólo se encarga de devolver un mensaje mediante un print indicando la opción seleccionada, cambiara al seguir avanzando el proyecto.
-	Al ingresar se da el mensaje en : ¡Bienvenidos a la sección de Series!, descubre nuevas series
### `modulo_juegos.py`
-  La sección cuenta con la función definida como main_menu(), que actualmente, sólo se encarga de devolver un mensaje mediante un print indicando la opción seleccionada, cambiara al seguir avanzando el proyecto.
- Al ingresar por el momento podremos notar el mensaje Bienvenidos a la sección de Videos Juegos.
- En actualizaciones posteriores podras ver una lista de juegos disponibles en la aplicación.

### `modulo_listas.py`
- La sección cuenta con la función definida como main_menu(), que actualmente, sólo se encarga de devolver un mensaje mediante un print indicando la opción seleccionada, cambiara al seguir avanzando el proyecto.
- Al ingresar por el momento podremos notar el mensaje ¡Bienvenido a tu Lista Multimedia!
- En actualizaciones posteriores podras ver una lista de tus peliculas, animes, series y juegos favoritas en la aplicación, asi como la opción de agregar o eliminar nuevos titulos a tu lista.
### `modulo_resena.py`
- La sección cuenta con la función definida como main_menu(), que actualmente, sólo se encarga de devolver un mensaje mediante un print indicando la opción seleccionada, cambiara al seguir avanzando el proyecto.
- Al ingresar por el momento podremos notar el mensaje ¡Cuentanos tu oponion!
- En actualizaciones posteriores podras dejarnos reseñas de tus contenidos multimedia de interes en la aplicación, asi como la opción de ver tus reseñas o la de otros usuarios.
### `modulo_agregar_contenido.py`
- La sección cuenta con la función definida como main_menu(), que actualmente, sólo se encarga de devolver un mensaje mediante un print indicando la opción seleccionada, cambiara al seguir avanzando el proyecto.
- Al ingresar por el momento podremos notar el mensaje ¡Bienvenido! en esta seccion podras agregar nuevas recomendaciones.
- En actualizaciones posteriores podras sugerirnos nuevos contenidos para una experiencia mas satisfactoria.
### `modulo_perfil.py`
- La sección cuenta con la función definida como main_menu(), que actualmente, sólo se encarga de devolver un mensaje mediante un print indicando la opción seleccionada, cambiara al seguir avanzando el proyecto.
- Al ingresar por el momento podremos notar el mensaje Bienvenido al Perfil del Usuario.
- En actualizaciones posteriores podras ver tus datos de perfil y modificarlos.
    
## Modulo de usuario
   ### `user_data.py`
   *Este módulo sirve como simulador de una base de datos de usuarios, para que el programa pueda llevar a cabo ciertas funciones, ya que en esta parte del proyecto, no se tiene conexión con ninguna base de datos. Y cuenta con lo siguiente:*
  
   #### **Diccionario "Usuarios"** 
Almacenamiento de usuarios y claves (para el ejemplo, están almacenados 3 usuarios y claves: {"cesia":"123", "mesica":"123", "maxi":"123})
   
  ####  ***Funciones***
   **registrar_usuario()** 
 - Recibe como argumentos los datos usuario y clave.
 - Si el usuario proporcionado ya se encuentra registrado en el diccionario "usuarios", devuelve un mensaje indicando que el nombre de usuario ya se encuentra en uso, y se le pide que pruebe con otro. (False)
 - En caso contrario, pide una clave y da un mensaje de éxito. (True)
   **validar_usuario()** 
 - Recibe como argumentos los datos usuario y clave.    
 - Si el usuario proporcionado ya se encuentra registrado en el diccionario "usuarios" y si los pares "usuario" : "clave" coinciden, devuelve un True.    
 - En caso contrario, devuelve False

## Módulo de configuraciones
   ### `config.py`
   Archivo de configuración que define parámetros estéticos y otras configuraciones globales de la aplicación.
**clase colores**
Mediante secuencias de escape, formatean le el código para que, en la consola se muestre un texto a color,  y caracteres especiales
**clase caracteres_especiales** 
Define ciertas variables como palabras clave para caracteres especiales, para que al momento de escribirlas (las palabras claves), muestre un cierto caracter. Por ejemplo: CRUZ  =  '✘'

### Integrantes del Grupo:

| Nombre              | Apellido        | DNI       | Correo Electrónico                     | Perfil de Github                                 |
|---------------------|-----------------|-----------|----------------------------------------|--------------------------------------------------|
| Leonel              | Barbosa         | 29352409  | barbosaleonel@gmail.com                | [leonelisaac](https://github.com/leonelisaac) |
| Yesica Esmeralda    | Ibañez          | 33693292  | yesicaesmeraldaibanez@gmail.com        | [Yesica-Ibanez](https://github.com/Yesica-Ibanez) |
| Fernando Maximiliano| Pérez Elías     | 35966699  | maxiperez6@hotmail.com                 | [maxi09perez](https://github.com/maxi09perez) |
| Cesia Fiorella      | Cáceres Giménez | 96320512  | cesiaf.gimenez@gmail.com               | [Cesiaf](https://github.com/Cesiaf)       |
| Álvaro Reinaldo     | Benicio         | 35821816  | alvarobenicio765@gmail.com             | [alvarobenicio](https://github.com/alvarobenicio) |
| Walter Rodrigo      | Rojas           | 34587991  | rodrigo.rojas2.rr@gmail.com            | [Rodri1989](https://github.com/Rodri1989)     |
