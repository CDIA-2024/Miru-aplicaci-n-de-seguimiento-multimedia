#series.py

import mysql.connector
from mysql.connector import Error
from prettytable import PrettyTable
from .config import create_connection

# Función para crear conexión a la base de datos
create_connection()

# Función para obtener y mostrar la lista de series
def mostrar_serie():
    connection = create_connection()

    if connection is None:
        return False

    try:
        cursor = connection.cursor()
        query = """
        SELECT s.id_serie, s.temporadas, c.titulo, c.anio_lanzamiento, g.nombre AS genero, d.nombre AS director, p.nombre AS productora
        FROM serie s
        JOIN contenido c ON s.id_contenido = c.id_contenido
        JOIN productora p ON s.id_productora = p.id_productora
        JOIN genero g ON c.id_genero = g.id_genero
        JOIN director d ON s.id_director = d.id_director
        """
        cursor.execute(query)
        series = cursor.fetchall()

        if not series:
            print("No se encontraron series.")
            return True

        table = PrettyTable()
        table.field_names = ["ID", "Temporadas", "Título", "Año", "Género", "Director", "Productora"]

        for serie in series:
            table.add_row(serie)

        print(table)
        return True

    except Error as e:
        print(f"Error al obtener la lista de series: {e}")
        return False

    finally:
        cursor.close()
        connection.close()

# Función para agregar una serie
def agregar_serie(titulo, temporadas, productora, genero, director, anio):
    connection = create_connection()

    if connection is None:
        return False

    try:
        cursor = connection.cursor()
        connection.start_transaction()

        # Verificar si el titulo ya existe
        cursor.execute('SELECT * FROM contenido WHERE titulo = %s', (nombre_serie,))
        nombre_serie = cursor.fetchall()
        if nombre_serie is None:
            # Si no existe, insertarlo
            cursor.execute("INSERT INTO contenido (titulo) VALUES (%s)", (nombre_serie,))
            connection.commit()
            serie_id = cursor.lastrowid
        else:
            serie_id = nombre_serie[0]
            print("El Título que desea agregar ya existe!")
            for fila in nombre_serie:
                print(f"ID: {fila[0]}, Título: {fila[1]}, Año: {fila[2]}")
        
        # Verificar si el género ya existe en la base de datos
        cursor.execute("SELECT id_genero FROM genero WHERE nombre = %s", (genero,))
        genero_existente = cursor.fetchone()
        if not genero_existente:
            cursor.execute("INSERT INTO genero (nombre) VALUES (%s)", (genero,))
            connection.commit()
            genero_id = cursor.lastrowid
        else:
            genero_id = genero_existente[0]

        # Verificar si la productora ya existe en la base de datos
        cursor.execute("SELECT id_productora FROM productora WHERE nombre = %s", (productora,))
        productora_existente = cursor.fetchone()
        if not productora_existente:
            cursor.execute("INSERT INTO productora (nombre) VALUES (%s)", (productora,))
            connection.commit()
            productora_id = cursor.lastrowid
        else:
            productora_id = productora_existente[0]

        # Insertar el contenido
        cursor.execute("INSERT INTO contenido (titulo, id_genero, anio_lanzamiento) VALUES (%s, %s, %s)",
                       (titulo, genero_id, anio))
        connection.commit()
        contenido_id = cursor.lastrowid

        # Verificar si el director ya existe en la base de datos
        cursor.execute("SELECT id_director FROM director WHERE nombre = %s", (director,))
        director_existente = cursor.fetchone()
        if not director_existente:
            cursor.execute("INSERT INTO director (nombre) VALUES (%s)", (director,))
            connection.commit()
            director_id = cursor.lastrowid
        else:
            director_id = director_existente[0]

        # Insertar la serie
        cursor.execute("INSERT INTO serie (id_contenido, temporadas, id_productora, id_director) VALUES (%s, %s, %s, %s)",
                       (contenido_id, temporadas, productora_id, director_id))
        connection.commit()

        return True

    except Error as e:
        connection.rollback()
        return False

    finally:
        cursor.close()
        connection.close()

# Función principal para ingresar datos de la serie
def añadir_serie_data():
    titulo_serie = input("Título de la serie: ")
    temporadas_serie = int(input("Temporadas: "))
    nombre_genero = input("Género: ")
    nombre_director = input("Director: ")
    nombre_productora = input("Productora: ")
    año_estreno = input("Año de estreno: ")

    if agregar_serie(titulo_serie, temporadas_serie, nombre_productora, nombre_genero, nombre_director, año_estreno):
        print("Proceso completado.")
    else:
        print("Error en el proceso.")
