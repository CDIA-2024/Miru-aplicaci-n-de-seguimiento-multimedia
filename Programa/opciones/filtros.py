# filtros.py

import mysql.connector
from mysql.connector import Error
def conectar():
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

# BLOQUE DE FUNCIONES PARA FILTRAR CONTENIDO

def obtener_contenido_por_tipo(tipo):
    connection = conectar()
    if not connection:
        return []

    cursor = connection.cursor(dictionary=True)
    query = ""
    if tipo == 1:  # Anime
        query = "SELECT * FROM anime JOIN contenido ON anime.id_contenido = contenido.id_contenido"
    elif tipo == 2:  # Película
        query = "SELECT * FROM pelicula JOIN contenido ON pelicula.id_contenido = contenido.id_contenido"
    elif tipo == 3:  # Serie
        query = "SELECT * FROM serie JOIN contenido ON serie.id_contenido = contenido.id_contenido"
    elif tipo == 4:  # Videojuego
        query = "SELECT * FROM videojuego JOIN contenido ON videojuego.id_contenido = contenido.id_contenido"
    
    cursor.execute(query)
    contenido = cursor.fetchall()
    cursor.close()
    connection.close()
    return contenido

def filtrar_contenido_por_genero(tipo, id_genero):
    connection = conectar()
    if not connection:
        return []

    cursor = connection.cursor(dictionary=True)
    query = ""
    if tipo == 1:  # Anime
        query = f"""
        SELECT * FROM anime 
        JOIN contenido ON anime.id_contenido = contenido.id_contenido
        WHERE contenido.id_genero = {id_genero}
        """
    elif tipo == 2: # Pelicula
        query = f"""
        SELECT * FROM pelicula
        JOIN contenido ON pelicula.id_contenido = contenido.id_contenido
        WHERE contenido.id_genero = {id_genero}
        """
    elif tipo == 3: # Serie
        query = f"""
        SELECT * FROM serie
        JOIN contenido ON serie.id_contenido = contenido.id_contenido
        WHERE contenido.id_genero = {id_genero}
        """
    elif tipo == 4: # Videojuegos
        query = f"""
        SELECT * FROM videojuego
        JOIN contenido ON videojuego.id_contenido = contenido.id_contenido
        WHERE contenido.id_genero = {id_genero}
        """
    cursor.execute(query)
    contenido = cursor.fetchall()
    cursor.close()
    connection.close()
    return contenido

def filtrar_contenido_por_estudio(tipo, id_estudio):
    connection = conectar()
    if not connection:
        return []

    cursor = connection.cursor(dictionary=True)
    query = ""
    if tipo == 1:  # Anime
        query = f"""
        SELECT * FROM anime 
        JOIN contenido ON anime.id_contenido = contenido.id_contenido
        WHERE anime.id_estudio = {id_estudio}
        """
    cursor.execute(query)
    contenido = cursor.fetchall()
    cursor.close()
    connection.close()
    return contenido

def filtrar_contenido_por_director(tipo, id_director):
    connection = conectar()
    if not connection:
        return []

    cursor = connection.cursor(dictionary=True)
    query = ""
    if tipo == 2:  # Pelicula
        query = f"""
        SELECT * FROM pelicula 
        JOIN contenido ON pelicula.id_contenido = contenido.id_contenido
        WHERE pelicula.id_director = {id_director}
        """
    if tipo == 3:  # Serie
        query = f"""
        SELECT * FROM serie
        JOIN contenido ON pelicula.id_contenido = contenido.id_contenido
        WHERE serie.director = {id_director}
        """ 
    cursor.execute(query)
    contenido = cursor.fetchall()
    cursor.close()
    connection.close()
    return contenido

def filtrar_contenido_por_productor(tipo, id_productor):
    connection = conectar()
    if not connection:
        return []

    cursor = connection.cursor(dictionary=True)
    query = ""
    if tipo == 2:  # Pelicula
        query = f"""
        SELECT * FROM pelicula
        JOIN contenido ON pelicula.id_contenido = contenido.id_contenido
        WHERE pelicula.id_productora = {id_productor}
        """ 
    elif tipo == 3:  # Serie
        query = f"""
        SELECT * FROM serie
        JOIN contenido ON serie.id_contenido = contenido.id_contenido
        WHERE serie.id_productora = {id_productor}
        """
    cursor.execute(query)
    contenido = cursor.fetchall()
    cursor.close()
    connection.close()
    return contenido

def filtrar_contenido_por_desarrollador(tipo, id_desarrollador):
    connection = conectar()
    if not connection:
        return []

    cursor = connection.cursor(dictionary=True)
    query = ""
    if tipo == 4:  # Videojuego
        query = f"""
        SELECT * FROM videojuego
        JOIN contenido ON videojuego.id_contenido = contenido.id_contenido
        WHERE videojuego.desarrollador = {id_desarrollador}
        """ 
    cursor.execute(query)
    contenido = cursor.fetchall()
    cursor.close()
    connection.close()
    return contenido

# BLOQUE DE FUNCIONES PARA OBTENER FILTROS

def obtener_generos():
    connection = conectar()
    if not connection:
        return []

    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM genero"
    cursor.execute(query)
    generos = cursor.fetchall()
    cursor.close()
    connection.close()
    return generos

def obtener_estudios():
    connection = conectar()
    if not connection:
        return []

    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM estudioanimacion"
    cursor.execute(query)
    estudios = cursor.fetchall()
    cursor.close()
    connection.close()
    return estudios

def obtener_directores():
    connection = conectar()
    if not connection:
        return []

    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM director"
    cursor.execute(query)
    directores = cursor.fetchall()
    cursor.close()
    connection.close()
    return directores

def obtener_productores():
    connection = conectar()
    if not connection:
        return []

    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM productor"
    cursor.execute(query)
    productores = cursor.fetchall()
    cursor.close()
    connection.close()
    return productores

def obtener_desarrolladores():
    connection = conectar()
    if not connection:
        return []

    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM desarrollador"
    cursor.execute(query)
    desarrolladores = cursor.fetchall()
    cursor.close()
    connection.close()
    return desarrolladores
