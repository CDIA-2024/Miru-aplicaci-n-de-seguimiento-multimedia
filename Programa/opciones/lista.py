#lista.py
from .config import create_connection
import mysql.connector
from datetime import datetime
from tabulate import tabulate

create_connection()

def eliminarContenido(mostrar):
    try:
        conn = create_connection()()
        cursor = conn.cursor()
        id_cont = int(input("Cual es el contenido que desea eliminar: (seleccione el id del contenido) "))
        query = """SELECT * FROM lista
        where id_contenido = %s and nombre = %s"""
        cursor.execute(query,(id_cont,mostrar))
        cont = cursor.fetchall()
        for row in cont:
            id_list = row[0]
            cursor.execute("DELETE from lista where id_lista = %s",(id_list,))
        conn.commit()
        print("Contenido eliminado con exito!")
    except mysql.connector.Error as error:
        print("Error al eliminar contenido:", error)
    finally:
        cursor.close()
        conn.close()



def agregarContenido(mostrar,fecha,user_id):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        query = "SELECT id_contenido, titulo, anio_lanzamiento FROM contenido"
        cursor.execute(query)
        titulos = cursor.fetchall()
        for fila in titulos:
            print(f"ID: {fila[0]}, Título: {fila[1]}, Año: {fila[2]}")
        agregar = input("Cual de estos titulos desea agregar a la lista?(Seleccione el Id) ")
        cursor.execute("select * from contenido where id_contenido = %s",(agregar,))
        id_cont = cursor.fetchone() 
        cont = int(id_cont[0])
        agregar = int(agregar)
        if cont == agregar:
            cursor.execute("""INSERT INTO lista (fecha_creacion, id_usuario, id_contenido, nombre) VALUES (%s, %s, %s, %s)""",
                                (fecha, user_id, agregar, mostrar))
            conn.commit()
            print("Contenido Agregado con exito!")
    except mysql.connector.Error as error:
        print("Error al agregar contenido:", error)
    finally:
        cursor.close()
        conn.close()


def crearLista(user_id):
    nombre = input("Nombre para la lista: ")
    fecha = fecha_actual = datetime.now().strftime("%Y-%m-%d")
    contenido = input("Tipo de contenido (pelicula, serie, juego o anime): ")
    if contenido in ["pelicula", "serie", "juego", "anime"]:
        agregar_lista(fecha, user_id, nombre, contenido)
    else:
        print("Tipo de contenido no válido.")

def agregar_lista(fecha, id_usu, nombre, contenido):
    conn = create_connection()()
    cursor = conn.cursor()
    seguir = "si"
    query = f"SELECT c.id_contenido, c.titulo, c.anio_lanzamiento FROM contenido c INNER JOIN {contenido} p ON c.id_contenido = p.id_contenido"
    cursor.execute(query)
    titulos = cursor.fetchall()
    while seguir == "si":
        for fila in titulos:
            print(f"ID: {fila[0]}, Título: {fila[1]}, Año: {fila[2]}")
        agregar = input("Cual de estos titulos desea agregar a la lista?(Seleccione el Id) ")
        cursor.execute("select * from contenido where id_contenido = %s",(agregar,))
        id_cont = cursor.fetchone() 
        cont = int(id_cont[0])
        agregar = int(agregar)
        if cont == agregar:
            cursor.execute("""INSERT INTO lista (fecha_creacion, id_usuario, id_contenido, nombre) VALUES (%s, %s, %s, %s)""",
                            (fecha, id_usu, agregar, nombre))
            conn.commit()
        seguir = input("Desea agregar otro titulo a la lista? (si/no): ")
    cursor.close()
    conn.close()

def mostrarOtrasListas(user_id):
    conn = create_connection()()
    cursor = conn.cursor()
    query = """
    SELECT COUNT(l.nombre), u.nombre, l.nombre, l.fecha_creacion
    FROM lista l
    LEFT JOIN usuario u ON u.id_usuario = l.id_usuario
    WHERE u.id_usuario != %s
    GROUP BY l.nombre, u.nombre, l.fecha_creacion
    """
    cursor.execute(query, (user_id,))
    listas = cursor.fetchall()
    listas_table = [[fila[1], fila[2], fila[0], fila[3]] for fila in listas]
    print(tabulate(listas_table, headers=["Usuario", "Nombre de Lista", "Cantidad de contenido guardado", "Fecha de creación"], tablefmt="fancy_grid"))

    mostrar = input("Ingrese el nombre de la lista para ver su contenido: (Si no presione enter) ")
    mostrarContenidoListas(mostrar)
    cursor.close()
    conn.close()

def mostrarContenidoListas(mostrar):
    conn = create_connection()()
    cursor = conn.cursor()
    query = """SELECT c.id_contenido, c.titulo, c.anio_lanzamiento 
               FROM contenido c
               LEFT JOIN lista l ON l.id_contenido = c.id_contenido
               WHERE l.nombre = %s"""
    cursor.execute(query, (mostrar,))
    titulos = cursor.fetchall()
    if titulos:
        print(f"{'ID':<5} {'Título':<40} {'Año':<10}")
        print("="*60)
        for fila in titulos:
            id_contenido, titulo, anio_lanzamiento = fila
            print(f"{id_contenido:<5} {titulo:<40} {anio_lanzamiento:<10}")
        pausa = input("Presione enter para continuar...")
    else:
        print(f"No se encontró contenido en la lista {mostrar}")
    cursor.close()
    conn.close()

def ver_misListas(user_id):
    conn = create_connection()()
    cursor = conn.cursor()
    cursor.execute("select * from usuario where id_usuario = %s",(user_id,))
    usuario = cursor.fetchone()
    nombre_user = usuario[1] 
    query = """
    SELECT COUNT(l.nombre), u.nombre, l.nombre, l.fecha_creacion
    FROM lista l
    LEFT JOIN usuario u ON u.id_usuario = l.id_usuario
    WHERE u.id_usuario = %s
    GROUP BY l.nombre, u.nombre, l.fecha_creacion
    """
    cursor.execute(query, (user_id,))
    listas = cursor.fetchall()
    print("Las Listas de",nombre_user,"son: ")
    listas_table = [[fila[2], fila[0], fila[3]] for fila in listas]
    print(tabulate(listas_table, headers=["Nombre de Lista", "Cantidad de contenido guardado", "Fecha de creación"], tablefmt="fancy_grid"))

    mostrar = input("Ingrese el nombre de la lista para ver su contenido: (Si no presione enter) ")
    mostrarContenidoListas(mostrar)

    query = """
    SELECT COUNT(l.nombre), u.nombre, l.nombre, l.fecha_creacion
    FROM lista l
    LEFT JOIN usuario u ON u.id_usuario = l.id_usuario
    WHERE u.id_usuario = %s and l.nombre = %s
    GROUP BY l.nombre, u.nombre, l.fecha_creacion
    """
    cursor.execute(query, (user_id, mostrar))
    mi_lista = cursor.fetchone()
    fecha = mi_lista[3]
    if mi_lista:
        print("")
        print("Que desea hacer?")
        print(" 1. Agregar Contenido")
        print(" 2. Eliminar Contenido")
        print("Otro. Salir")
        op = int(input("Ingrese opción: "))
        if op == 1:
            agregarContenido(mostrar,fecha,user_id)
        elif op == 2:
            eliminarContenido(mostrar)
    cursor.close()
    conn.close()