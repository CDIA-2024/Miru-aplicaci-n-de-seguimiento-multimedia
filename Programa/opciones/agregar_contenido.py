import mysql.connector
from opciones import (anime, peliculas, videojuego, series, lista)

def main_menu():
    
# Conectar a la base de datos MySQL
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='maxi',
        database='miru'
    )
    cursor = conn.cursor()

    op = 0
    while op != 5:
        submenu1()
        op = int(input("Elija una opción: "))
    
        if op <= 4:
            ti = input("Ingrese el titulo del contenido a agregar: ")
            cursor.execute('SELECT * FROM contenido WHERE titulo = %s', (ti,))
            titulos = cursor.fetchall()
            if titulos:
                opc = 0
                print("El Titulo que desea agregar ya existe!")
                for fila in titulos:
                    print(f"ID: {fila[0]}, Título: {fila[1]}, Año: {fila[2]}")
                while opc !=4:
                    submenu2()
                    opc = int(input("Elija una opción: "))

                    if opc == 1:
                        pass
                    elif opc == 2:
                        pass
                    elif opc == 3:
                        opc = 4
                    elif opc == 4:
                        volver()
                        op = 5
                    else:
                        print("Opción inválida, por favor eliga una opción valida")
            else:
                if op == 1:
                    peliculas.añadir_pelicula_data()
                elif op == 2:
                    series.añadir_serie_data()
                elif op == 3:
                    anime.añadir_anime_data()
                elif op == 4:
                    videojuego.añadir_videojuegos_data()
        elif op == 5:
            volver()
        else:
            print("Opción inválida, por favor eliga un contenido del menú")

def volver():
    print("Volviendo al menu principal")

def submenu1():
    print("¿Que tipo de contenido desea agregar?")
    print(" 1. Pelicula")
    print(" 2. Serie")
    print(" 3. Anime")
    print(" 4. Video Juego")
    print(" 5. Volver al Menu Principal")

def submenu2():
    print("¿Que desea hacer ahora?")
    print(" 1. Agregar a una lista")
    print(" 2. Reseñar contenido")
    print(" 3. Sugerir otro contenido")
    print(" 4. Volver al Menu Principal")
#opcion_agregar_contenido()
# en esta seccion se podra agregar elementos a la lista ya formada.
#para eso se le debera dar un argumento a la funcion.