# reseñas.py
from .config import create_connection
import mysql.connector
from mysql.connector import Error
from datetime import datetime
import sys
sys.path.append("Miru-aplicacion-de-seguimiento-multimedia-main\\Programa\\opciones")
import filtros
import tabulate

create_connection()

# FUNCIÓN PARA AGREGAR RESEÑA
def agregar_reseña(user_id):
    tipo = int(input("¿Qué tipo de contenido quieres reseñar?\n1. Anime\n2. Película\n3. Serie\n4. Videojuego\nSeleccione una opción: "))
    contenido = filtros.obtener_contenido_por_tipo(tipo)
    
    if not contenido:
        print("No se encontró contenido disponible.")
        return

    for item in contenido:
        print(f"{item['id_contenido']}: {item['titulo']}")
    
    if tipo == 1 :
        print("\nFiltrar por:")
        print("1. Genero")
        print("2. Estudio de Animación")
        filtro = input("Elija un filtro o deje vacío si no desea filtar el contenido: ")
        if filtro == '1':
            generos = filtros.obtener_generos()
            for genero in generos:
                 print(f"{genero['id_genero']}: {genero['nombre']}")
            id_genero = int(input("Seleccione el ID del género: "))
            contenido = filtros.filtrar_contenido_por_genero(tipo, id_genero)
        if filtro == '2':
            estudios = filtros.obtener_estudios()
            for estudio in estudios:
                print(f"{estudio['id_estudio']}: {estudio['nombre']}")
            id_estudio = int(input("Seleccione el ID del estudio: "))
            contenido = filtros.filtrar_contenido_por_estudio(tipo, id_estudio)
    elif tipo == 2:
        print("\nFiltrar por:")
        print("1. Genero")
        print("2. Director")
        print("3. Productora")
        filtro = input("Elija un filtro o deje vacío si no desea filtar el contenido")
        if filtro == '1':
            generos = filtros.obtener_generos()
            for genero in generos:
                print(f"{genero['id_genero']}: {genero['nombre']}")
            id_genero = int(input("Seleccione el ID del género: "))
            contenido = filtros.filtrar_contenido_por_genero(tipo, id_genero)
        elif filtro == '2':
            directores = filtros.obtener_directores()
            for director in directores:
                print(f"{director['id_director']}: {director['nombre']}")
            id_director = int(input("Seleccione el ID del director: "))
            contenido = filtros.filtrar_contenido_por_director(tipo, id_director)
        elif filtro == '3':
            productores = filtros.obtener_productores()
            for productores in productores:
                print(f"{productores['id_productora']}: {productores['nombre']}")
            id_productor = int(input("Seleccione el ID del productor: "))
            contenido = filtros.filtrar_contenido_por_productor(tipo, id_productor)
    elif tipo == 3:
        print("\nFiltrar por:")
        print("1. Genero")
        print("2. Director")
        print("3. Productora")
        filtro = input("Elija un filtro o deje vacío si no desea filtar el contenido")
        if filtro == '1':
            generos = filtros.obtener_generos()
            for genero in generos:
                print(f"{genero['id_genero']}: {genero['nombre']}")
            id_genero = int(input("Seleccione el ID del género: "))
            contenido = filtros.filtrar_contenido_por_genero(tipo, id_genero)
        elif filtro == '2':
            directores = filtros.obtener_directores()
            for director in directores:
                print(f"{director['id_director']}: {director['nombre']}")
            id_director = int(input("Seleccione el ID del director: "))
            contenido = filtros.filtrar_contenido_por_director(tipo, id_director)
        elif filtro == '3':
            productores = filtros.obtener_productores()
            for productores in productores:
                print(f"{productores['id_productora']}: {productores['nombre']}")
            id_productor = int(input("Seleccione el ID del productor: "))
            contenido = filtros.filtrar_contenido_por_productor(tipo, id_productor)    
    elif tipo == 4:
        print("\nFiltrar por:")
        print("1. Genero")
        print("2. Desarrollador")
        filtro = input("Elija un filtro o deje vacío si no desea filtar el contenido")
        if filtro == '1':
            generos = filtros.obtener_generos()
            for genero in generos:
                print(f"{genero['id_genero']}: {genero['nombre']}")
            id_genero = int(input("Seleccione el ID del género: "))
            contenido = filtros.filtrar_contenido_por_genero(tipo, id_genero)
        elif filtro == '2':
            desarrolladores = filtros.obtener_desarrolladores()
            for desarrollador in desarrolladores:
                print(f"{desarrollador['id_desarrollador']}: {director['nombre']}")
            id_desarrollador = int(input("Seleccione el ID del director: "))
            contenido = filtros.filtrar_contenido_por_director(tipo, id_desarrollador) 
    
    for item in contenido:
        print(f"{item['id_contenido']}: {item['titulo']}")  
             
    id_contenido = int(input("Seleccione el ID del contenido que desea reseñar: "))
    texto = input("Ingrese su reseña: ")
    puntuacion = int(input("Ingrese la puntuación (1-10): "))
    estado = input("Ingrese el estado: ")

    try:
        connection = create_connection()
        if not connection:
            return False

        cursor = connection.cursor()
        fecha_actual = datetime.now()

        query_registro = """
        INSERT INTO registro (puntuacion, estado, id_usuario)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query_registro, (puntuacion, estado, user_id))
        id_registro = cursor.lastrowid

        query_resena = """
        INSERT INTO reseña (fecha, texto, id_usuario, puntuacion, id_contenido)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query_resena, (fecha_actual, texto, user_id, id_registro, id_contenido))
        connection.commit()

        print("\nReseña agregada exitosamente.")
        return True

    except Error as e:
        connection.rollback()
        print(f"\nError al agregar la reseña: {e}")
        return False

    finally:
        cursor.close()
        connection.close()


def filtrar_reseña_por_contenido(user_id, tipo_contenido):
    connection = None
    cursor = None
    try:
        connection = create_connection()
        if not connection:
            print("No se pudo establecer conexión con la base de datos.")
            return

        cursor = connection.cursor(dictionary=True)

        base_query = """
        SELECT contenido.titulo, genero.nombre AS genero, reseña.fecha, reseña.puntuacion, reseña.texto
        FROM reseña
        JOIN contenido ON reseña.id_contenido = contenido.id_contenido
        JOIN genero ON contenido.id_genero = genero.id_genero
        """
        
        if tipo_contenido == 1:  # Anime
            query = base_query + "JOIN anime ON contenido.id_contenido = anime.id_contenido "
        elif tipo_contenido == 2:  # Película
            query = base_query + "JOIN pelicula ON contenido.id_contenido = pelicula.id_contenido "
        elif tipo_contenido == 3:  # Serie
            query = base_query + "JOIN serie ON contenido.id_contenido = serie.id_contenido "
        elif tipo_contenido == 4:  # Videojuego
            query = base_query + "JOIN videojuego ON contenido.id_contenido = videojuego.id_contenido "
        elif tipo_contenido == 0:  # Sin Filtros
            query = base_query
        else:
            print("Tipo de contenido no válido.")
            return

        query += "WHERE reseña.id_usuario = %s ORDER BY reseña.fecha DESC"

        cursor.execute(query, (user_id,))
        reseñas = cursor.fetchall()

        if not reseñas:
            mensaje = "No se encontraron reseñas para este tipo de contenido." if tipo_contenido != 0 else "No se encontraron reseñas para este usuario."
            print(mensaje)
            return

        print(f"{'Título':<30} {'Género':<20} {'Fecha':<15} {'Puntuación':<10} {'Reseña'}")
        print("=" * 110)
        for reseña in reseñas:
            fecha_formateada = reseña['fecha'].strftime("%Y-%m-%d")
            print(f"{reseña['titulo']:<30} {reseña['genero']:<20} {fecha_formateada:<15} {reseña['puntuacion']:<10} {reseña['texto']}")

    except mysql.connector.Error as e:
        print(f"Error de MySQL: {e}")
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

# Obtiene todas las reseñas del usuario
def obtener_reseñas(user_id):
    connection = None
    cursor = None
    try:
        connection = create_connection()
        if not connection:
            print("No se pudo establecer conexión con la base de datos.")
            return

        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT contenido.titulo, genero.nombre AS genero, reseña.fecha, reseña.puntuacion, reseña.texto
        FROM reseña
        JOIN contenido ON reseña.id_contenido = contenido.id_contenido
        JOIN genero ON contenido.id_genero = genero.id_genero
        WHERE reseña.id_usuario = %s
        ORDER BY reseña.fecha DESC
        """

        cursor.execute(query, (user_id,))
        reseñas = cursor.fetchall()

        if not reseñas:
            print("No se encontraron reseñas para este usuario.")
            return

        headers = ["Título", "Género", "Fecha", "Puntuación", "Reseña"]
        rows = [[
            reseña['titulo'],
            reseña['genero'],
            reseña['fecha'].strftime("%Y-%m-%d"),
            reseña['puntuacion'],
            reseña['texto']
        ] for reseña in reseñas]
    
        print(tabulate(rows, headers=headers, tablefmt="grid"))
        
        # Llamar a la función de filtrado de reseñas 
        reseña_filtro_main(user_id)
    except mysql.connector.Error as e:
        print(f"Error de MySQL: {e}")
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


def reseña_filtro_main(user_id):
    while True:
        print("\nFiltros disponibles:")
        print(" 1. Anime")
        print(" 2. Películas")
        print(" 3. Series")
        print(" 4. Videojuegos")
        tipo_contenido = input("\nElija un filtro o deje vacío si no desea filtrar el contenido: ").strip()
        if tipo_contenido == "":
            break
        elif tipo_contenido.isdigit() and int(tipo_contenido) in [1, 2, 3, 4]:
            filtrar_reseña_por_contenido(user_id, int(tipo_contenido))
            break
        else:
            print("Opción inválida. Por favor, elija un número del 1 al 4 o deje vacío para no aplicar ")

def reseña_filtro_main(user_id):
    
    while True:
            print("\nFiltros disponibles:")
            print(" 1. Anime")
            print(" 2. Películas")
            print(" 3. Series")
            tipo_contenido = input("\nElija un filtro o deje vacío si no desea filtrar el contenido: ").strip()
            if tipo_contenido == "":
                break
            elif tipo_contenido.isdigit() and int(tipo_contenido) in [1, 2, 3, 4]:
                filtrar_reseña_por_contenido(user_id, int(tipo_contenido))
                break
            else:
                print("Opción inválida. Por favor, elija un número del 1 al 4 o deje vacío para no aplicar ")