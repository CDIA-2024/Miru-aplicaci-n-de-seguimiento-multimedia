import mysql.connector

# Función para crear conexión a la base de datos
# Se Crear la tabla de perfiles de usuario-se debe asociar .
# se debe asociar a la tabla de listas de preferencia
# se debe asociar a lastablas reseñas

def mostrar_perfil(user_id):
    conn = mysql.connector.connect(
        host='localhost',
        database='miru',
        user='root',
        password='maxi'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, correo,año_nacimiento FROM usuario WHERE id_usuario = %s", (user_id,))
    perfil = cursor.fetchone()
    if perfil:
        nombre, correo, cumpleanos = perfil
        print(f"Nombre de usuario: {nombre}")
        print(f"correo: {correo}")
        print(f"año_nacimiento: {cumpleanos}")
    else:
        print("Usuario no encontrado.")

def editarPerfil(user_id):
    conn = mysql.connector.connect(
        host='localhost',
        database='miru',
        user='root',
        password='maxi'
    )
    cursor = conn.cursor()
    conf = input("Desea editar el perfil de Usuario? (si/no) ")
    if conf == "si":
        print("Que datos desea mofificar?")
        print(" 1. Nombre de Usuario")
        print(" 2. Fecha de Naciemiento")
        print(" 3. Contraseña")
        op = int(input("Elija una opción: "))
        if op == 1:
            user_new = input("Nuevo nombre: ")
            cursor.execute("UPDATE usuario SET nombre = %s where id_usuario = %s",(user_new,user_id))
        elif op == 2:
            cumple = input("Ingrese nueva fecha: (AAAA-MM-DD) ")
            cursor.execute("update usuario set año_nacimiento = %s where id_usuario = %s",(cumple,user_id))
        elif op == 3:
            contr = input("Nueva Contraseña: ")
            cursor.execute("update usuario set contrasena = %s where id_usuario = %s",(contr,user_id))
        conn.commit()

#UPDATE casa SET estado = "mascota" where id = 4;