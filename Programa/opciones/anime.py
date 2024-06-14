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


# Función para obtener y mostrar la lista de animes
def mostrar_animes():
    connection = create_connection()

    if connection is None:
        return False

    try:
        cursor = connection.cursor()

        # Consulta SQL para obtener la lista de animes con su información
        query = """
        SELECT a.id_anime, c.titulo, c.anio_lanzamiento, g.nombre AS genero, ea.nombre AS estudio, e.nombre_estado
        FROM anime a
        JOIN contenido c ON a.id_contenido = c.id_contenido
        JOIN genero g ON c.id_genero = g.id_genero
        JOIN estudioanimacion ea ON a.id_estudio = ea.id_estudio
        JOIN estado e ON a.id_estado = e.id_estado
        """
        cursor.execute(query)

        # Obtener todos los resultados de la consulta
        animes = cursor.fetchall()

        # Imprimir la lista de animes
        for anime in animes:
            print(f"ID: {anime[0]}, Título: {anime[1]}, Año: {anime[2]}, Género: {anime[3]}, Estudio: {anime[4]}, Estado: {anime[5]}")

        return True

    except Error as e:
        print(f"Error al obtener la lista de animes: {e}")
        return False

    finally:
        cursor.close()
        connection.close()

# Función para agregar un anime
def agregar_anime(nombre_anime, nombre_genero, nombre_estudio, anio_lanzamiento, capitulos, estado):
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
                       (nombre_anime, anio_lanzamiento, genero_id))
        connection.commit()
        contenido_id = cursor.lastrowid        

        # Verificar si el estudio de animación ya existe
        cursor.execute("SELECT id_estudio FROM estudioanimacion WHERE nombre = %s", (nombre_estudio,))
        estudio = cursor.fetchone()
        if estudio is None:
            # Si no existe, insertarlo
            cursor.execute("INSERT INTO estudioanimacion (nombre) VALUES (%s)", (nombre_estudio,))
            connection.commit()
            estudio_id = cursor.lastrowid
        else:
            estudio_id = estudio[0]

        # Verificar si el estado ya existe
        cursor.execute("SELECT id_estado FROM estado WHERE nombre_estado = %s", (estado,))
        estado_row = cursor.fetchone()
        if estado_row is None:
            print("El estado ingresado no es válido.")
            connection.rollback()
            return False
        else:
            estado_id = estado_row[0]

        # Insertar el anime
        cursor.execute("INSERT INTO anime (id_contenido, capitulos, id_estudio, id_estado) VALUES (%s, %s, %s, %s)",
                       (contenido_id, capitulos, estudio_id, estado_id))
        connection.commit()

        print("Anime agregado exitosamente.")
        return True

    except Error as e:
        # Revertir transacción en caso de error
        connection.rollback()
        print(f"Error al agregar el anime: {e}")
        return False

    finally:
        cursor.close()
        connection.close()

# Función principal para ingresar datos del anime
def añadir_anime_data():
    nombre_anime = input("Nombre del anime: ")
    nombre_genero = input("genero: ")
    nombre_estudio = input("Estudio de animación: ")
    anio_lanzamiento = input("año de lanzamiento: ")
    capitulos = input("Episodios: ")
    estado = input("Estado: ")
    

    if agregar_anime(nombre_anime, nombre_genero, nombre_estudio, anio_lanzamiento, capitulos, estado):
        print("Proceso completado.")
    else:
        print("Error en el proceso.")

