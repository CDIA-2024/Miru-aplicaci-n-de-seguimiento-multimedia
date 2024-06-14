#Config.py
#BLOQUE DE CONFIGURACIÓN PARA LA CONEXIÓN CON LA BASE DE DATOS
import mysql.connector
from mysql.connector import Error

# Abrir la conexión
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='miru',
            user='root',
            password='maxi'
        )
        if connection.is_connected():
            print("Conexión exitosa")
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Cerrar la conexion
def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Conexión cerrada")



# BLOQUE PARA LA VERIFICACIÓN Y REGISTRO DE USUARIO

# Función para validar el usuario y obtener su información
def validar_usuario(correo, contrasena):
    try:
        conn = create_connection()
        if conn is None:
            return None
        
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM usuario WHERE correo = %s AND contrasena = %s"
        cursor.execute(query, (correo, contrasena))
        usuario = cursor.fetchone()

        conn.close()
        return usuario  # Devuelve el usuario encontrado o None si no se encontró

    except Error as e:
        print(f"Error al validar el usuario: {e}")
        return None
    
def registrar_usuario(nombre, correo, contrasena, año_nacimiento, edad, genero_de_interes=None, suscripcion=None):
    try:
        conn = create_connection()
        if conn is None:
            return False
        
        cursor = conn.cursor()

        # Verificar si el correo ya está registrado
        cursor.execute("SELECT COUNT(*) FROM usuario WHERE correo = %s", (correo,))
        if cursor.fetchone()[0] > 0:
            print("El correo ya está registrado.")
            conn.close()
            return False

        # Insertar el nuevo usuario
        query = """INSERT INTO usuario 
                   (nombre, correo, contrasena, año_nacimiento, edad, genero_de_interes, suscripcion) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (nombre, correo, contrasena, año_nacimiento, edad, genero_de_interes, suscripcion))
        
        conn.commit()
        conn.close()
        return True
    except Error as e:
        print(f"Error al registrar el usuario: {e}")
        return False

# FUNCIÓN PARA OBTENER EL ID DEL USUARIO
def obtener_id_usuario(correo):
    try:
        conn = create_connection()
        if conn is None:
            return None
        
        cursor = conn.cursor()
        query = "SELECT * FROM usuario WHERE correo = %s"
        cursor.execute(query, (correo,))
        user_id = cursor.fetchone()
        conn.close()
        return user_id
    except Error as e:
        print(f"Error al obtener el ID de usuario: {e}")
        return None      
       
#BLOQUES PARA CON CLASES PARA CONFIGURACIÓN ESTÉTICA DEL PROGRAMA

# Configuración para colores y estilos
class colores:
    RESET = '\033[0m'
    NEGRITA = '\033[1m'
    SUBRAYADO = '\033[4m'
    ROJO = '\033[91m'
    VERDE = '\033[92m'
    AMARILLO = '\033[93m'
    AZUL = '\033[94m'
    PURPURA = '\033[95m'
    CYAN = '\033[96m'
    NARANJA = '\033[38;5;208m'
    ROSA = '\033[38;5;206m'
    GRIS = '\033[38;5;242m'
    MARRON = '\033[38;5;130m'
    LIMA = '\033[38;5;154m'
    TEAL = '\033[38;5;123m'
    MENTA = '\033[38;5;83m'
    LAVANDA = '\033[38;5;183m'
    ROSA_CLARO = '\033[38;5;211m'
    VERDE_CLARO = '\033[38;5;120m'

# Configuración para caracteres especiales 
class caracteres_especiales:
    GUION = '=' * 31
    FLECHA = '➤'
    TILDE = '✔'
    CRUZ = '✘'
