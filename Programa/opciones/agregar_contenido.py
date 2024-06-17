# agregar_contenido.py
import mysql.connector
from opciones import anime, peliculas, videojuego, series, lista, reseñas

def main_menu(user_id):
    # Conectar a la base de datos MySQL
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='CIK:830_',
        database='miru'
    )
    cursor = conn.cursor()

    submenu1(user_id)  # Pasar user_id a submenu1

    cursor.close()
    conn.close()

def volver():
    print("Volviendo al menú principal")

def submenu1(user_id):
    print(" 1. Anime")
    print(" 2. Película")
    print(" 3. Serie")
    print(" 4. Videojuegos")
    print(" 5. Volver al Menú Principal")
    opt = input("¿Qué tipo de contenido desea agregar? ")
    if opt == "1":
        anime.añadir_anime_data()
    elif opt == "2":
        peliculas.añadir_pelicula_data()
    elif opt == "3":
        series.añadir_serie_data()
    elif opt == "4":
        videojuego.añadir_videojuegos_data()
    elif opt == "5":
        volver()
    else:
        print("Opción inválida, por favor elija un contenido del menú")

def submenu2(user_id):
    print("¿Qué desea hacer ahora?")
    opt = input("Seleccione una opción: ")
    print(" 1. Agregar a una lista")
    print(" 2. Reseñar contenido")
    print(" 3. Volver al Menú Principal")
    if opt == "1":
        lista.ver_misListas(user_id)
    elif opt == "2":
        reseñas.agregar_reseña(user_id)
    elif opt == "3":
        volver()
    else:
        print("Opción inválida, por favor elija una opción del menú")



