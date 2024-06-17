
# Miru - Plataforma de Entretenimiento

**Miru** es una aplicación de gestión de contenido multimedia diseñada para usuarios aficionados a animes, películas, series y videojuegos. Con Miru, los usuarios pueden explorar una amplia biblioteca de medios, organizar listas personalizadas, y compartir reseñas sobre sus experiencias. Desde la gestión detallada de preferencias hasta la exploración de diversos géneros y directores, Miru ofrece una plataforma integral para descubrir y gestionar contenido multimedia de manera eficiente y personalizada.

## Contenido del Repositorio

## Programa

### `index.py`

Este archivo es el punto de entrada principal de la aplicación Miru. Contiene funciones para iniciar sesión, registrar nuevos usuarios y mostrar un menú principal interactivo donde los usuarios pueden navegar por diferentes secciones de la aplicación, como anime, películas, series, juegos, listas personales, reseñas y más.

-   **Funciones principales:**
    -   `limpiar_pantalla()`: Función para limpiar la pantalla de la consola.
    -   `mensaje_formateado(mensaje, color, estilo, caracter)`: Función para formatear mensajes con colores y estilos específicos.
    -   `login()`: Función para iniciar sesión de usuarios. Permite hasta 3 intentos antes de bloquear el acceso.
    -   `menu_principal(usuario_validado, user_id)`: Función para mostrar el menú principal después de iniciar sesión, donde los usuarios pueden seleccionar diversas opciones como anime, películas, series, juegos, listas personales, reseñas, agregar contenido y ver su perfil.

## Opciones

Aquí se encuentran los archivos que contienen las diferentes funcionalidades de Miru:


### `anime.py`

Este archivo contiene funciones para interactuar con la tabla de animes en la base de datos de Miru. Permite mostrar la lista de animes disponibles y agregar nuevos registros de animes con sus respectivos géneros, estudios de animación, año de lanzamiento, número de episodios y estado.

-   **Funciones:**
    -   `create_connection()`: Función para establecer la conexión con la base de datos MySQL.
    -   `mostrar_animes()`: Función que consulta y muestra la lista de animes disponibles en la plataforma.
    -   `agregar_anime(nombre_anime, nombre_genero, nombre_estudio, anio_lanzamiento, capitulos, estado)`: Función para agregar un nuevo anime a la base de datos. Verifica y, si es necesario, inserta nuevos registros para género y estudio de animación.
    -   `añadir_anime_data()`: Función principal que interactúa con el usuario para ingresar los datos del nuevo anime a agregar.

El archivo utiliza la biblioteca `mysql.connector` para la conexión a la base de datos MySQL y `PrettyTable` para mostrar los resultados de consulta de manera tabular.

### `peliculas.py`

Este archivo contiene funciones para interactuar con la tabla de películas en la base de datos de Miru. Permite mostrar la lista de películas disponibles y agregar nuevos registros de películas con sus respectivos géneros, directores y año de lanzamiento.

-   **Funciones:**
    -   `create_connection()`: Función para establecer la conexión con la base de datos MySQL.
    -   `mostrar_peliculas()`: Función que consulta y muestra la lista de películas disponibles en la plataforma, incluyendo información como título, año de lanzamiento y director.
    -   `agregar_pelicula(titulo, genero, director, anio)`: Función para agregar una nueva película a la base de datos. Verifica y, si es necesario, inserta nuevos registros para género y director.
    -   `añadir_pelicula_data()`: Función principal que interactúa con el usuario para ingresar los datos de la nueva película a agregar.

El archivo utiliza la biblioteca `mysql.connector` para la conexión a la base de datos MySQL y `PrettyTable` para mostrar los resultados de consulta de manera tabular.

### `series.py`

Este archivo contiene funciones para interactuar con la tabla de series en la base de datos de Miru. Permite mostrar la lista de series disponibles y agregar nuevos registros de series con información como temporadas, género, director, productora y año de lanzamiento.

-   **Funciones:**
    -   `create_connection()`: Función para establecer la conexión con la base de datos MySQL.
    -   `mostrar_serie()`: Consulta y muestra la lista de series disponibles en la plataforma, incluyendo información detallada como temporadas, título, año de lanzamiento, género, director y productora.
    -   `agregar_serie(titulo, temporadas, productora, genero, director, anio)`: Permite agregar una nueva serie a la base de datos. Verifica y, si es necesario, inserta nuevos registros para género, productora y director.
    -   `añadir_serie_data()`: Función principal que interactúa con el usuario para ingresar los datos de la nueva serie a agregar.

El archivo utiliza la biblioteca `mysql.connector` para la conexión a la base de datos MySQL y `PrettyTable` para mostrar los resultados de consulta de manera tabular.

### `videojuegos.py`

Este archivo contiene funciones diseñadas para interactuar con la tabla de videojuegos en la base de datos de Miru. A través de estas funciones, es posible tanto consultar como agregar nuevos registros de videojuegos con detalles como título, género, desarrollador y año de lanzamiento.

- **Funciones:**

	- `create_connection():` Esta función establece la conexión con la base de datos MySQL donde se almacenan los datos de Miru.
    
    -  `mostrar_videojuegos()`: Consulta la base de datos para obtener y mostrar la lista de videojuegos disponibles en la plataforma. Cada videojuego se presenta con su título, año de lanzamiento, género y desarrollador.
    - `agregar_videojuego(nombre_videojuego, nombre_genero, nombre_desarrollador, anio_lanzamiento)`: Permite agregar un nuevo videojuego a la base de datos. Antes de la inserción, verifica si el género y el desarrollador ya existen en la base de datos; de no ser así, los inserta primero.
    - `añadir_videojuegos_data()`: Esta función interactúa directamente con el usuario para solicitar los datos necesarios del nuevo videojuego que se desea agregar, como nombre, género, desarrollador y año de lanzamiento.
    
Este archivo hace uso de la biblioteca `mysql.connector` para gestionar la conexión y las consultas a la base de datos MySQL.


-  ### `lista.py`

Este archivo proporciona funcionalidades para gestionar listas de contenido en la base de datos de Miru. Permite crear, modificar y consultar listas de contenido como películas, series, juegos o anime.

- **Funciones:**

	-   `conectar_bd():` Función para establecer la conexión con la base de datos MySQL utilizando `mysql.connector`.
	    
	-   `eliminarContenido(mostrar):` Permite eliminar contenido de una lista especificada por el usuario, identificado por su ID de contenido y el nombre de la lista.
	    
	-   `agregarContenido(mostrar, fecha, user_id)`: Permite agregar contenido a una lista especificada por el usuario, solicitando al usuario que elija un título de una lista de contenidos disponibles.
	    
	-  `crearLista(user_id):` Interactúa con el usuario para crear una nueva lista, solicitando un nombre y el tipo de contenido (pelicula, serie, juego o anime).
	    
	-   `agregar_lista(fecha, id_usu, nombre, contenido)`: Permite al usuario agregar varios títulos de contenido a una lista recién creada, con la opción de continuar agregando más títulos.
	    
	-   `mostrarOtrasListas(user_id)`: Muestra las listas creadas por otros usuarios, junto con la cantidad de contenido guardado y la fecha de creación. También permite al usuario seleccionar una lista para ver su contenido.
	    
	-   `mostrarContenidoListas(mostrar)`: Muestra el contenido de una lista específica seleccionada por el usuario, incluyendo ID, título y año de lanzamiento del contenido.
	    
	-   `ver_misListas(user_id):` Muestra las listas creadas por el usuario actual, junto con la opción de ver y gestionar el contenido de esas listas (agregar o eliminar contenido).
	    
Cada función utiliza consultas SQL para interactuar con las tablas de la base de datos, gestionando eficazmente las operaciones de CRUD (Crear, Leer, Actualizar, Eliminar) sobre las listas de contenido.

Este archivo hace uso de la biblioteca `mysql.connector` para la gestión de la base de datos MySQL, y `tabulate` para mostrar resultados de manera tabular en la consola.

### `reseñas.py`

Este archivo proporciona funcionalidades para agregar reseñas a diferentes tipos de contenido (anime, películas, series, videojuegos), filtrar reseñas por tipo de contenido y mostrar las reseñas del usuario.

#### Funciones:

-   `conectar()`: Función para establecer la conexión con la base de datos MySQL utilizando `mysql.connector`.
    
-   `agregar_reseña(user_id)`: Permite al usuario agregar una reseña para un contenido seleccionado, solicitando la puntuación, estado y texto de la reseña. Guarda la reseña en la base de datos.
    
-   `filtrar_reseña_por_contenido(user_id, tipo_contenido)`: Filtra y muestra las reseñas del usuario por tipo de contenido (anime, película, serie, videojuego).
    
-   `obtener_reseñas(user_id)`: Obtiene todas las reseñas del usuario y las muestra en formato tabular, utilizando la función `tabulate` para una visualización clara en la consola.
    
-   `reseña_filtro_main(user_id)`: Función principal para filtrar las reseñas por tipo de contenido. Muestra un menú de opciones para que el usuario elija el tipo de contenido y llama a `filtrar_reseña_por_contenido` para mostrar las reseñas filtradas.
    
#### Uso de otros archivos:

-   Importa el módulo `filtros` para obtener y filtrar contenido específico (anime, películas, series, videojuegos).
-   Utiliza `tabulate` para formatear las tablas de reseñas y mostrarlas al usuario de manera ordenada.

#### Consideraciones adicionales:

-   Se manejan errores de conexión a la base de datos utilizando bloques `try-except`.
-   Las consultas SQL se ejecutan utilizando parámetros para prevenir inyecciones SQL.
-   Se utilizan fechas actuales para registrar cuándo se hizo cada reseña.

### Resumen

El archivo `reseñas.py` es crucial para la funcionalidad de reseñas en la aplicación Miru, permitiendo a los usuarios agregar, filtrar y ver reseñas de diversos tipos de contenido multimedia.

### `agregar_contenido.py`

Este script maneja la interacción del usuario para agregar contenido multimedia a la base de datos de Miru. Utiliza módulos específicos (`anime`, `peliculas`, `videojuego`, `series`, `lista`, `reseñas`) para funciones detalladas de cada tipo de contenido.

#### Funciones:

-   `main_menu(user_id):`
    
    -   Establece la conexión con la base de datos MySQL.
    -   Llama a `submenu1(user_id)` para mostrar las opciones principales de contenido.
    -   Cierra la conexión con la base de datos después de que se completa la interacción.
-   `volver()`:
    
    -   Imprime un mensaje indicando que se vuelve al menú principal.
-   `submenu1(user_id)`:
    
    -   Muestra un menú para que el usuario elija el tipo de contenido que desea agregar: anime, película, serie, videojuego o volver al menú principal.
    -   Llama a las funciones correspondientes en los módulos (`anime`, `peliculas`, `videojuego`, `series`) según la opción seleccionada por el usuario.
    -   Si el usuario elige volver, llama a la función `volver()`.
-   `submenu2(user_id)`:
    
    -   Presenta opciones adicionales después de agregar contenido: agregar a una lista o escribir una reseña.
    -   Llama a las funciones `ver_misListas(user_id)` de `lista` y `agregar_reseña(user_id)` de `reseñas` según la opción seleccionada.
    -   Si el usuario elige volver, llama a la función `volver()`.

### Uso de otros archivos:

-   Importa módulos específicos (`anime`, `peliculas`, `videojuego`, `series`, `lista`, `reseñas`) que contienen funciones para agregar anime, películas, series, videojuegos, manejar listas de contenidos y escribir reseñas.
-   Cada función en `submenu1` y `submenu2` actúa como un puente para redirigir las solicitudes de usuario al módulo correspondiente para manejar la lógica específica de cada tipo de contenido.

### Consideraciones adicionales:

-   Utiliza una conexión a la base de datos local MySQL.
-   Gestiona las opciones inválidas proporcionando mensajes de error y solicitando al usuario que elija nuevamente.
-   Cada función cierra adecuadamente las conexiones y cursos después de completar las operaciones.

### Ejemplo de flujo de uso:

1.  El usuario selecciona el tipo de contenido que desea agregar (anime, película, serie, videojuego) desde `submenu1`.
2.  Se llaman las funciones respectivas de cada módulo para agregar detalles específicos del contenido.
3.  Después de agregar el contenido, el usuario puede optar por agregarlo a una lista o escribir una reseña desde `submenu2`.
4.  Se manejan las acciones posteriores como agregar a una lista existente, escribir una nueva reseña o volver al menú principal.
5. 
Este enfoque modularizado facilita la gestión y expansión de nuevas funcionalidades relacionadas con el contenido multimedia en la aplicación Miru. 

### `perfil_usuario.py`

#### Funciones:

-  `mostrar_perfil(user_id):`
    
    -   Conecta con la base de datos MySQL usando los parámetros de conexión proporcionados.
    -   Ejecuta una consulta SQL para obtener el nombre de usuario, correo electrónico y año de nacimiento del usuario identificado por `user_id`.
    -   Imprime la información del perfil si se encuentra un usuario correspondiente; de lo contrario, imprime un mensaje indicando que el usuario no fue encontrado.
-  `editarPerfil(user_id)`:
    
    -   Establece una conexión con la base de datos utilizando los parámetros de conexión especificados.
    -   Solicita al usuario que confirme si desea editar su perfil.
    -   Presenta opciones para modificar:
        -   Nombre de usuario (`nombre` en la tabla `usuario`).
        -   Fecha de nacimiento (`año_nacimiento` en la tabla `usuario`).
        -   Contraseña (`contrasena` en la tabla `usuario`).
    -   Realiza consultas SQL `UPDATE` correspondientes según la opción elegida por el usuario para actualizar la información en la base de datos.
    -   Confirma los cambios utilizando `conn.commit()` después de cada operación de actualización.

#### Uso típico:

1.  **Visualización de perfil**:
    
    -   Llamar `mostrar_perfil(user_id)` para ver la información del perfil de un usuario específico.
2.  **Edición de perfil**:
    
    -   Llamar `editarPerfil(user_id)` para permitir que un usuario edite su nombre, fecha de nacimiento o contraseña según sea necesario.
    #### Consideraciones:

-   **Conexión a la base de datos**: Cada función establece y cierra conexiones independientes a la base de datos utilizando `mysql.connector.connect()` y `conn.close()` para garantizar el manejo adecuado de recursos.
    
-   **Interacción con el usuario**: Ambas funciones (`mostrar_perfil()` y `editarPerfil()`) interactúan con el usuario a través de la consola, solicitando entrada para confirmaciones y opciones de edición.

### `config.py`

##### BLOQUE DE CONFIGURACIÓN PARA LA CONEXIÓN CON LA BASE DE DATOS

-  `create_connection():`
    -   Función que intenta establecer una conexión con la base de datos MySQL utilizando los parámetros de conexión predefinidos (`host`, `database`, `user`, `password`).
    -   Imprime un mensaje de éxito si la conexión se establece correctamente.
    -   Devuelve el objeto de conexión si tiene éxito; de lo contrario, devuelve `None`.
-  `close_connection(connection)`:
    -   Función que cierra la conexión pasada como argumento si está abierta.
    -   Imprime un mensaje indicando que la conexión ha sido cerrada.

##### BLOQUE PARA LA VERIFICACIÓN Y REGISTRO DE USUARIO

-  `validar_usuario(correo, contrasena)`:
    
    -   Función que valida las credenciales del usuario consultando la base de datos.
    -   Utiliza la conexión creada por `create_connection()` para ejecutar una consulta que verifica si existe un usuario con el correo y contraseña proporcionados.
    -   Devuelve el registro del usuario como un diccionario si se encuentra; de lo contrario, devuelve `None`.
    
- `registrar_usuario(nombre, correo, contrasena, año_nacimiento, edad, genero_de_interes=None, suscripcion=None)`:
    
    -   Función que registra un nuevo usuario en la base de datos.
    -   Verifica primero si el correo electrónico ya está registrado.
    -   Inserta los datos del nuevo usuario en la tabla `usuario` si el correo no está registrado previamente.
    -   Utiliza `conn.commit()` para confirmar los cambios en la base de datos.
    -   Devuelve `True` si el registro se realiza con éxito; de lo contrario, devuelve `False`.
    
- `obtener_id_usuario(correo)`:
    
    -   Función que obtiene el ID de usuario basado en el correo electrónico proporcionado.
    -   Ejecuta una consulta para buscar el usuario en la tabla `usuario` usando el correo electrónico.
    -   Devuelve el registro del usuario encontrado si existe; de lo contrario, devuelve `None`.

##### BLOQUES PARA CONFIGURACIÓN ESTÉTICA DEL PROGRAMA

- `clase colores:`
    
    -   Define una serie de códigos ANSI para colores y estilos de texto utilizados para mejorar la presentación en la consola.
    -   Cada atributo de clase representa un estilo o color diferente que se puede aplicar al texto impreso en la consola.
- `clase caracteres_especiales`:
    
    -   Define constantes que representan caracteres especiales como guiones, flechas y símbolos de verificación y cruz, utilizados para mejorar la presentación y legibilidad de la salida en la consola.

#### Uso típico:

-   **Conexión a la base de datos**: Se utiliza `create_connection()` para establecer una conexión antes de realizar operaciones de base de datos y `close_connection(connection)` para cerrarla después de completar las operaciones.
    
-   **Validación y registro de usuario**: Se usan `validar_usuario(correo, contrasena)` y `registrar_usuario(nombre, correo, contrasena, año_nacimiento, edad)` para manejar el acceso y la creación de cuentas de usuario.
    
-   **Configuración estética**: Se pueden usar las clases `colores` y `caracteres_especiales` para mejorar la presentación del texto en la consola, añadiendo estilos y caracteres especiales según sea necesario.

## BD
Aquí se encuentran los archivos relacionados con la base de datos de Miru:

-   **DER (1).jpg**: Diagrama Entidad-Relación de la base de datos.
 
-   **consultas.sql**: Archivo con consultas SQL para la base de datos.

-   **datos.sql**: Archivo con datos de prueba para la base de datos.

-   **miru.mwb**: Archivo de modelo de base de datos Workbench.

-   **miru.png**: Imagen representativa de la base de datos.

-   **miru.sql**: Script SQL para crear la estructura de la base de datos.


##  Requisitos
-   **Python:** Debe estar instalado Python 3.x en el sistema.
-   **MySQL:** Se requiere MySQL para la base de datos. Asegúrate de tenerlo instalado y configurado.
- **MySQL Workbench** (opcional): Herramienta gráfica para administrar y visualizar bases de datos MySQL.
- **Editor de código** (como Visual Studio Code): Opcional, pero recomendado para editar y ejecutar el código Python.
-   **Bibliotecas de Python:** Todas las bibliotecas de Python necesarias están especificadas en `requirements.txt`.

## Tutorial para iniciar la aplicación desde cero

#### Requisitos previos

Antes de comenzar, asegurarse de tener instalados los siguientes programas y herramientas:

1.  **Python 3.x:** Es necesario para ejecutar la aplicación. Puede descargarse desde [python.org](https://www.python.org/downloads/) e instalarlo según las instrucciones para del sistema operativo utilizado.
    
2.  **Gestor de bases de datos MySQL:** Es necesario tener MySQL instalado en el sistema. Puede descargarse desde [MySQL Community Server](https://dev.mysql.com/downloads/mysql/) y seguir las instrucciones de instalación adecuadas para el sistema operativo utilizado.
    
3.  **Editor de código (opcional):** Puede utilizarse cualquier editor de código o entorno de desarrollo integrado (IDE) a elección. Se recomienda Visual Studio Code (VS Code), que se puede descargar desde [Visual Studio Code](https://code.visualstudio.com/).
    

### Paso 1: Clonar el repositorio

1.  Abrir una terminal o línea de comandos.
    
2.  Clonar el repositorio desde GitHub usando el siguiente comando:
       
    `git clone https://github.com/CDIA-2024/Miru-aplicacion-de-seguimiento-multimedia` 
  
3.  Cambia al directorio del repositorio clonado:
        
    `cd Miru-aplicacion-de-seguimiento-multimedia` 
    

### Paso 2: Configurar el entorno virtual (opcional pero recomendado)

1.  Crear un entorno virtual para aislar las dependencias del sistema global (esto evita conflictos entre diferentes proyectos Python):
    
      `python -m venv venv` 
    
Esto creará un directorio `venv` que contendrá todos los paquetes necesarios para el proyecto.
    
2.  Activar el entorno virtual:
    
    -   En Linux o macOS:
        
        `source venv/bin/activate` 
        
    -   En Windows (PowerShell):
        
        `.\venv\Scripts\Activate.ps1` 
        
    -   En Windows (cmd):

        
        `.\venv\Scripts\activate` 
        
### Paso 3: Instalar dependencias

1.  Asegurarse de que se está en el entorno virtual activado.
    
2.  Instalar las dependencias listadas en el archivo `requirements.txt` usando pip:
    
    `pip install -r requirements.txt`
    

### Configuración de la Base de Datos MySQL

### 1. Importar el archivo `miru.sql`

El archivo `miru.sql` contiene las definiciones de las tablas y las restricciones necesarias para la base de datos que utilizará tu aplicación. Asegúrate de que tu servidor MySQL esté instalado y en ejecución antes de continuar.

1.  **Inicia sesión en MySQL**: Utiliza el cliente de línea de comandos de MySQL o una herramienta gráfica como MySQL Workbench para ejecutar comandos SQL.
    
2.  **Crea una base de datos**: Si aún no has creado la base de datos `miru`, puedes hacerlo manualmente o asegurarte de que el primer comando en `miru.sql` se encargue de esto.
    
3.  **Importa `miru.sql`**:
    
    -   Abre una terminal o un símbolo del sistema.
    -   Usa el comando `mysql` para importar el archivo SQL. Asumiendo que estás en el directorio donde se encuentra `miru.sql`:
        

        `mysql -u tu_usuario -p miru < miru.sql` 
        
        -   Reemplaza `tu_usuario` con el usuario de MySQL que tiene permisos para crear la base de datos y tablas.
        -   Te pedirá la contraseña de MySQL
1.  **Verifica la importación**: Una vez importado correctamente, puedes verificar que las tablas se hayan creado ejecutando comandos SQL para mostrar la estructura de la base de datos.
    

#### 2. Actualización de `Config.py`

El archivo `Config.py` ya contiene la configuración para conectarse a la base de datos. Asegúrate de que los detalles de conexión coincidan con tu configuración de MySQL.

-   Abre `Config.py` y verifica los siguientes parámetros:
    
    `host = 'localhost'      # Puede variar dependiendo de dónde está alojado tu servidor MySQL
    database = 'miru'       # Nombre de la base de datos que has creado o importado
    user = 'root'           # Usuario de MySQL con permisos adecuados
    password = 'CIK:830_'   # Contraseña del usuario de MySQL`
    
Ajusta estos valores según la configuración de tu servidor MySQL.

#### 5.2. Ejecución de la Aplicación Python

1.  **Ejecuta tu aplicación** desde la línea de comandos:
    
    `python main.py` 
    
2.  **Interactúa con la aplicación**: Si todo está configurado correctamente, deberías ver mensajes indicando una conexión exitosa a la base de datos. La aplicación debería funcionar según su diseño, utilizando la base de datos `miru` que has configurado.


### Integrantes del Grupo:

| Nombre              | Apellido        | DNI       | Correo Electrónico                     | Perfil de Github                                 |
|---------------------|-----------------|-----------|----------------------------------------|--------------------------------------------------|
| Yesica Esmeralda    | Ibañez          | 33693292  | yesicaesmeraldaibanez@gmail.com        | [Yesica-Ibanez](https://github.com/Yesica-Ibanez) |
| Fernando Maximiliano| Pérez Elías     | 35966699  | maxiperez6@hotmail.com                 | [maxi09perez](https://github.com/maxi09perez) |
| Cesia Fiorella      | Cáceres Giménez | 96320512  | cesiaf.gimenez@gmail.com               | [Cesiaf](https://github.com/Cesiaf)       |
| Álvaro Reinaldo     | Benicio         | 35821816  | alvarobenicio765@gmail.com             | [alvarobenicio](https://github.com/alvarobenicio) |
| Walter Rodrigo      | Rojas           | 34587991  | rodrigo.rojas2.rr@gmail.com            | [Rodri1989](https://github.com/Rodri1989)     |
