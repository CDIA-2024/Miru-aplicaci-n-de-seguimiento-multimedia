# peliculas.py

import mysql.connector
from mysql.connector import Error
from prettytable import PrettyTable
from .config import create_connection
# Función para crear conexión a la base de datos
create_connection()

# Función para obtener y mostrar la lista de películas
def mostrar_peliculas():
    connection = create_connection()

    if connection is None:
        return False

    try:
        cursor = connection.cursor()

        # Consulta SQL para obtener la lista de películas con su información
        query = """
        SELECT p.id_pelicula, c.titulo, c.anio_lanzamiento, d.nombre AS director
        FROM pelicula p
        JOIN contenido c ON p.id_contenido = c.id_contenido
        JOIN director d ON p.id_director = d.id_director
        """
        cursor.execute(query)

        # Obtener todos los resultados de la consulta
        peliculas = cursor.fetchall()

        # Crear una tabla para mostrar los resultados
        table = PrettyTable()
        table.field_names = ["ID", "Título", "Año", "Director"]

        for pelicula in peliculas:
            table.add_row(pelicula)

        print(table)
        return True

    except Error as e:
        print(f"Error al obtener la lista de películas: {e}")
        return False

    finally:
        cursor.close()
        connection.close()

# Función para agregar una película
def agregar_pelicula(titulo, genero, director, anio):
    connection = create_connection()

    if connection is None:
        return False

    try:
        cursor = connection.cursor()

        # Iniciar transacción
        connection.start_transaction()
        
        # Verificar si el titulo ya existe
        cursor.execute('SELECT * FROM contenido WHERE titulo = %s', (titulo,))
        titulo= cursor.fetchall()
        if titulo is None:
            # Si no existe, insertarlo
            cursor.execute("INSERT INTO contenido (titulo) VALUES (%s)", (titulo,))
            connection.commit()
            añadir_pelicula_data_id = cursor.lastrowid
        else:
            añadir_pelicula_data_id = titulo[0]
            print("El Título que desea agregar ya existe!")
            for fila in titulo:
                print(f"ID: {fila[0]}, Título: {fila[1]}, Año: {fila[2]}")
        # Verificar si el género ya existe en la base de datos
        cursor.execute("SELECT id_genero FROM genero WHERE nombre = %s", (genero,))
        genero_existente = cursor.fetchone()

        if not genero_existente:
            # Si el género no existe, insertarlo en la tabla de géneros
            cursor.execute("INSERT INTO genero (nombre) VALUES (%s)", (genero,))
            connection.commit()  # Confirmar la inserción
            genero_id = cursor.lastrowid
        else:
            genero_id = genero_existente[0]

        # Insertar la película en la tabla de contenido
        cursor.execute("INSERT INTO contenido (titulo, id_genero, anio_lanzamiento) VALUES (%s, %s, %s)",
                       (titulo, genero_id, anio))
        connection.commit()  # Confirmar la inserción
        contenido_id = cursor.lastrowid

        # Verificar si el director ya existe en la base de datos
        cursor.execute("SELECT id_director FROM director WHERE nombre = %s", (director,))
        director_existente = cursor.fetchone()

        if not director_existente:
            # Si el director no existe, insertarlo en la tabla de directores
            cursor.execute("INSERT INTO director (nombre) VALUES (%s)", (director,))
            connection.commit()  # Confirmar la inserción
            director_id = cursor.lastrowid
        else:
            director_id = director_existente[0]

        # Insertar la película en la tabla de películas
        cursor.execute("INSERT INTO pelicula (id_contenido, id_director) VALUES (%s, %s)",
                       (contenido_id, director_id))
        connection.commit()  # Confirmar la inserción

        return True

    except Error as e:
        # Revertir la transacción en caso de error
        connection.rollback()
        return False

    finally:
        cursor.close()
        connection.close()

# Función principal para ingresar datos de la película      
def añadir_pelicula_data():
    titulo_pelicula = input("Título de la película: ")
    nombre_genero = input("Género: ")
    nombre_director = input("Director: ")
    año_estreno = input("Año de estreno: ")

    if agregar_pelicula(titulo_pelicula, nombre_genero, nombre_director, año_estreno):
        print("Proceso completado.")
    else:
        print("Error en el proceso.")

