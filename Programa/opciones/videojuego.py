import mysql.connector
from mysql.connector import Error

# Función para crear conexión a la base de datos
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='miru',
            user='root',
            password='maxi'
        )
        return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def mostrar_videojuegos():
    # Función para obtener y mostrar la lista de videojuegos
    connection = create_connection()

    if connection is None:
        return False

    try:
        cursor = connection.cursor()

        # Consulta SQL para obtener la lista de videojuegos con su información
        query = """
        SELECT v.id_videojuego, c.titulo, c.anio_lanzamiento, g.nombre AS genero, d.nombre AS desarrollador
        FROM videojuego v
        JOIN contenido c ON v.id_contenido = c.id_contenido
        JOIN genero g ON c.id_genero = g.id_genero
        JOIN desarrollador d ON v.id_desarrollador = d.id_desarrollador
        """
        cursor.execute(query)
        videojuegos = cursor.fetchall()

        # Imprimir la lista de videojuegos
        for videojuego in videojuegos:
            print(f"ID: {videojuego[0]}, Título: {videojuego[1]}, Año: {videojuego[2]}, Género: {videojuego[3]}, Desarrollador: {videojuego[4]}")
        
        return True

    except Error as e:
        print(f"Error al obtener la lista de videojuegos: {e}")
        return False

    finally:
        cursor.close()
        connection.close()

# Función para agregar un videojuego
def agregar_videojuego(nombre_videojuego, nombre_genero, nombre_desarrollador, anio_lanzamiento):
    # Función para agregar un videojuego a la base de datos
    connection = create_connection()
    
    if connection is None:
        return False

    try:
        cursor = connection.cursor()

        # Iniciar transacción
        connection.start_transaction()

        # Verificar si el género ya existe
        cursor.execute("SELECT id_genero FROM genero WHERE nombre = %s", (nombre_genero,))
        genero = cursor.fetchone()

        if genero is None:
            # Si no existe, insertarlo
            cursor.execute("INSERT INTO genero (nombre) VALUES (%s)", (nombre_genero,))
            connection.commit()
            genero_id = cursor.lastrowid
        else:
            genero_id = genero[0]

        # Insertar el contenido
        cursor.execute("INSERT INTO contenido (titulo, anio_lanzamiento, id_genero) VALUES (%s, %s, %s)",
                       (nombre_videojuego, anio_lanzamiento, genero_id))
        connection.commit()
        contenido_id = cursor.lastrowid        

        # Verificar si el desarrollador ya existe en la BD
        cursor.execute("SELECT id_desarrollador FROM desarrollador WHERE nombre = %s", (nombre_desarrollador,))
        desarrollador = cursor.fetchone()

        if desarrollador is None:
            # Si no existe, insertarlo
            cursor.execute("INSERT INTO desarrollador (nombre) VALUES (%s)", (nombre_desarrollador,))
            connection.commit()
            desarrollador_id = cursor.lastrowid
        else:
            desarrollador_id = desarrollador[0]

        # Insertar el videojuego
        cursor.execute("INSERT INTO videojuego (id_contenido, id_desarrollador) VALUES (%s, %s)",
                       (contenido_id, desarrollador_id))
        connection.commit()

        print("Videojuego agregado exitosamente.")
        return True

    except Error as e:
        # Revertir transacción en caso de error
        connection.rollback()
        print(f"Error al agregar el videojuego: {e}")
        return False

    finally:
        cursor.close()
        connection.close()
        
# Función principal para ingresar datos del videojuego
def añadir_videojuegos_data():
    nombre_videojuego = input("Nombre del videojuego: ")
    nombre_genero = input("Género: ")
    nombre_desarrollador = input("Desarrollador: ")
    anio_lanzamiento = input("Año de lanzamiento: ")

    if agregar_videojuego(nombre_videojuego, nombre_genero, nombre_desarrollador, anio_lanzamiento):
        print("Videojuego agregado exitosamente.")
    else:
        print("Error al agregar el videojuego.")

