import mysql.connector

def crearLista(user_id):
    nombre = input("Nombre para la lista: ")
    fecha = input("Ingresar fecha (AAAA-MM-DD): ")
    contenido = input("Tipo de contenido (pelicula, serie, juego o anime): ")
    if contenido == "pelicula":
        agregar_lista(fecha, user_id, nombre, contenido)
    elif contenido == "serie":
        agregar_lista(fecha, user_id, nombre, contenido)
    elif contenido == "juego":
        agregar_lista(fecha, user_id, nombre, contenido)
    elif contenido == "anime":
        agregar_lista(fecha, user_id, nombre, contenido)

def agregar_lista(fecha, id_usu, nombre, contenido):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='maxi',
        database='miru'
    )
    cursor = conn.cursor()
    seguir = "si"
    query = f"SELECT c.id_contenido, c.titulo, c.anio_lanzamiento FROM contenido c INNER JOIN {contenido} p ON c.id_contenido = p.id_contenido"
    cursor.execute(query)
    titulos = cursor.fetchall()
    while seguir == "si":
        for fila in titulos:
            print(f"ID: {fila[0]}, Título: {fila[1]}, Año: {fila[2]}")
        agregar = input("Cual de estos titulos desea agregar a la lista?(Seleccione el Id)")
        cursor.execute("select * from contenido where id_contenido = %s",(agregar,))
        id_cont = cursor.fetchone() 
        cont = int(id_cont[0])
        agregar = int(agregar)
        if cont == agregar:
            cursor.execute("""INSERT INTO lista (fecha_creacion, id_usuario, id_contenido, nombre) VALUES (%s, %s, %s, %s)""",
                            (fecha, id_usu, agregar, nombre))
            conn.commit()
        seguir = input("Desea agregar otro titulo a la lista? (si/no): ")

def ver_misListas(user_id):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='maxi',
        database='miru'
    )
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
    for fila in listas:
        print(f"Nombre de Lista: {fila[2]}, Cantidad de contenido guardado: {fila[0]}, Fecha de creación: {fila[3]}")
    mostrar = input("Ingrese el nombre de la lista para ver su contenido: (Si no precione enter)")
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

def mostrarOtrasListas(user_id):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='maxi',
        database='miru'
    )
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
    for fila in listas:
        print(f"Usuario: {fila[1]}, Nombre de Lista: {fila[2]}, Cantidad de contenido guardado: {fila[0]}, Fecha de creación: {fila[3]}")
    mostrar = input("Ingrese el nombre de la lista para ver su contenido: (Si no precione enter)")
    mostrarContenidoListas(mostrar)

def mostrarContenidoListas(mostrar):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='maxi',
        database='miru'
    )
    cursor = conn.cursor()
    query = """SELECT c.id_contenido, c.titulo, c.anio_lanzamiento 
    FROM contenido c
    left join lista l on l.id_contenido = c.id_contenido
    where l.nombre = %s"""
    cursor.execute(query, (mostrar,))
    titulos = cursor.fetchall()
    if titulos:
        print("Contenido de la lista",mostrar,": ")
        for fila in titulos:
            print(f"ID: {fila[0]}, Título: {fila[1]}, Año: {fila[2]}")
        pausa = input("Presione enter para continuar...")

def eliminarContenido(mostrar):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='maxi',
        database='miru'
    )
    cursor = conn.cursor()
    id_cont = int(input("Cual es el contenido que desea eliminar: (seleccione el id del contenido)"))
    query = """SELECT * FROM lista
    where id_contenido = %s and nombre = %s"""
    cursor.execute(query,(id_cont,mostrar))
    cont = cursor.fetchone()
    id_list = cont[0]
    if cont:
        cursor.execute("DELETE from lista where id_lista = %s",(id_list,))
        conn.commit()
        print("Contenido eliminado con exito!")

def agregarContenido(mostrar,fecha,user_id):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='maxi',
        database='miru'
    )
    cursor = conn.cursor()
    query = "SELECT id_contenido, titulo, anio_lanzamiento FROM contenido"
    cursor.execute(query)
    titulos = cursor.fetchall()
    for fila in titulos:
        print(f"ID: {fila[0]}, Título: {fila[1]}, Año: {fila[2]}")
    agregar = input("Cual de estos titulos desea agregar a la lista?(Seleccione el Id)")
    cursor.execute("select * from contenido where id_contenido = %s",(agregar,))
    id_cont = cursor.fetchone() 
    cont = int(id_cont[0])
    agregar = int(agregar)
    if cont == agregar:
        cursor.execute("""INSERT INTO lista (fecha_creacion, id_usuario, id_contenido, nombre) VALUES (%s, %s, %s, %s)""",
                            (fecha, user_id, agregar, mostrar))
        conn.commit()
        print("Contenido Agregado con exito!")

