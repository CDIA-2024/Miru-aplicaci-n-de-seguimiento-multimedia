import mysql.connector
from mysql.connector import Error

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

        # Imprimir la lista de series
        for serie in series:
            print(f"ID: {serie[0]}, Temporadas: {serie[1]}, Título: {serie[2]}, Año: {serie[3]}, Género: {serie[4]}, Director: {serie[5]}, Productora: {serie[6]}")

        return True

    except Error as e:
        print(f"Error al obtener la lista de series: {e}")
        return False

    finally:
        cursor.close()


        if cursor.rowcount == 0:
                print("No se encontraron series.")
                
def agregar_serie(titulo, temporadas, productora, genero, director, anio):
    connection = create_connection()

    if connection is None:
        return False

    try:
        cursor = connection.cursor()

        connection.start_transaction()

        cursor.execute("SELECT id_genero FROM genero WHERE nombre = %s", (genero,))
        genero_existente = cursor.fetchone()

        if not genero_existente:
            cursor.execute("INSERT INTO genero (nombre) VALUES (%s)", (genero,))
            genero_id = cursor.lastrowid
        else:
            genero_id = genero_existente[0]

        cursor.execute("SELECT id_productora FROM productora WHERE nombre = %s", (productora,))
        productora_existente = cursor.fetchone()

        if not productora_existente:
            cursor.execute("INSERT INTO productora (nombre) VALUES (%s)", (productora,))
            productora_id = cursor.lastrowid
        else:
            productora_id = productora_existente[0]

        cursor.execute("INSERT INTO contenido (titulo, id_genero, anio_lanzamiento) VALUES (%s, %s, %s)",
                       (titulo, genero_id, anio))
        contenido_id = cursor.lastrowid

        cursor.execute("SELECT id_director FROM director WHERE nombre = %s", (director,))
        director_existente = cursor.fetchone()

        if not director_existente:
            cursor.execute("INSERT INTO director (nombre) VALUES (%s)", (director,))
            director_id = cursor.lastrowid
        else:
            director_id = director_existente[0]

        cursor.execute("INSERT INTO serie (id_contenido, temporadas, id_productora, id_director) VALUES (%s, %s, %s, %s)",
                       (contenido_id, temporadas, productora_id, director_id))

        connection.commit()

        print("Serie agregada exitosamente.")
        return True

    except Error as e:
        connection.rollback()
        print(f"Error al agregar la serie: {e}")
        return False

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

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


