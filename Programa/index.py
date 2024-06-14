#index.py
import time
from opciones import (config, anime, peliculas, videojuego, series, reseñas, agregar_contenido, lista, perfil_usuario)
from opciones.config import registrar_usuario, validar_usuario, obtener_id_usuario
import time

def limpiar_pantalla():
    print("\033[H\033[J", end="")

def mensaje_formateado(mensaje=None, color=None, estilo=None, caracter=None):
    mensaje_formateado = ""
    if mensaje is not None:
        mensaje_formateado += f"{color}{(estilo if estilo is not None else '')}{mensaje}{config.colores.RESET}"
    if caracter is not None:
        mensaje_formateado += f"{color}{(estilo if estilo is not None else '')}{caracter}{config.colores.RESET}"
    return mensaje_formateado

def login():
    intentos = 0
    usuario_validado = None
    user_id = None

    while intentos < 3:
        limpiar_pantalla()
        print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.LAVANDA))
        print(mensaje_formateado("       Inicio de Sesión       ", config.colores.LAVANDA, config.colores.NEGRITA))
        print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.LAVANDA))

        correo = input(mensaje_formateado("Correo: ", config.colores.CYAN, config.colores.NEGRITA))
        contrasena = input(mensaje_formateado("Contraseña: ", config.colores.CYAN, config.colores.NEGRITA))
        
        usuario_validado = validar_usuario(correo, contrasena)
        user_id = obtener_id_usuario(correo)
        if usuario_validado:
            limpiar_pantalla()
            print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.VERDE))
            print(mensaje_formateado("        Inicio de Sesión       ", config.colores.VERDE, config.colores.NEGRITA))
            print(mensaje_formateado("            Exitoso            ", config.colores.VERDE, config.colores.NEGRITA))
            print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.VERDE))           
            time.sleep(2)
            return usuario_validado, user_id
        else:
            limpiar_pantalla()
            print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.ROJO))
            print(mensaje_formateado("      Correo o Contraseña      ", config.colores.ROJO, config.colores.NEGRITA))
            print(mensaje_formateado("          Incorrectos          ", config.colores.ROJO, config.colores.NEGRITA))
            print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.ROJO))
            intentos += 1
            print(f"Intentos restantes: {3 - intentos}")
            time.sleep(2)
            if intentos != 3:
                opcion_reintentar = input("¿Desea intentar de nuevo? S/N ")
                if opcion_reintentar.lower() != "s":
                    print(mensaje_formateado("Saliendo del Programa...", config.colores.LIMA))
                    break

    if intentos >= 3:
        print(mensaje_formateado("No se pudo iniciar sesión", config.colores.AMARILLO))
        opcion_registro = input(mensaje_formateado("¿Desea Registrarse? S/N ", config.colores.NEGRITA)) 
        if opcion_registro.lower() == "s":
            limpiar_pantalla()
            print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.VERDE))
            print(mensaje_formateado("        Registro de Nuevo      ", config.colores.VERDE, config.colores.NEGRITA))
            print(mensaje_formateado("             Usuario           ", config.colores.VERDE, config.colores.NEGRITA))
            print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.VERDE))
            nombre = input(mensaje_formateado("Nombre: ", config.colores.CYAN, config.colores.NEGRITA))
            correo = input(mensaje_formateado("Correo: ", config.colores.CYAN, config.colores.NEGRITA))
            contrasena = input(mensaje_formateado("Contraseña: ", config.colores.CYAN, config.colores.NEGRITA))
            año_nacimiento = input(mensaje_formateado("Año de Nacimiento (AAAA-MM-DD): ", config.colores.CYAN, config.colores.NEGRITA))
            edad = input(mensaje_formateado("Edad: ", config.colores.CYAN, config.colores.NEGRITA))
            genero_de_interes = input(mensaje_formateado("Género de Interés: ", config.colores.CYAN, config.colores.NEGRITA))
            suscripcion = input(mensaje_formateado("Suscripción: ", config.colores.CYAN, config.colores.NEGRITA))
            if registrar_usuario(nombre, correo, contrasena, año_nacimiento, edad, genero_de_interes, suscripcion):
                print(mensaje_formateado("Usuario registrado con éxito. Por favor inicie sesión.", config.colores.VERDE))
                return login()  # Intentar iniciar sesión automáticamente después de registrar
            else:
                print(mensaje_formateado("Error al registrar el usuario.", config.colores.ROJO))
        else:
            print(mensaje_formateado("Usuario Bloqueado, ha utilizado más de 3 intentos", config.colores.ROJO))
            print(mensaje_formateado("Intentelo de nuevo más tarde", config.colores.NEGRITA))
            time.sleep(2)
            return None, None

def menu_principal(usuario_validado, user_id):
    opcion = 0

    while opcion != 9:
        limpiar_pantalla()
        print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.MENTA))
        print(mensaje_formateado("         Menú Principal        ", config.colores.ROSA_CLARO, config.colores.NEGRITA))
        print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.MENTA))
        print(" 1. Anime")
        print(" 2. Películas")
        print(" 3. Series")
        print(" 4. Juegos")
        print(" 5. Mis Listas")
        print(" 6. Mis Reseñas")
        print(" 7. Agregar Contenido")
        print(" 8. Ver Perfil")
        print(" 9. Salir")
        print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.MENTA))

        opcion = int(input("Por favor, seleccione una opción: "))

        # Opción ANIME
        if opcion == 1:
            # SubMenú ANIME
            print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.LAVANDA))
            print(" 1. Animes en Miru")     
            print(" 2. Agregar Animes Miru")  
            print(" 3. Mis Reseñas de Anime")
            print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.LAVANDA))
            opt_menu = int(input("Seleccione una acción: "))
            
            # Llamado a las funciones del submenú anime
            if opt_menu == 1:
                anime.mostrar_animes() 
            elif opt_menu == 2:
                anime.añadir_anime_data()
            elif opt_menu == 3:
                # Aquí se debe llamar a la función que muestre las reseñas de anime del usuario
                pass

        elif opcion == 2:
            # Llamar al menú de películas
            # SubMenú PELÍCULAS
            print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.ROSA_CLARO))
            print(" 1. Películas en Miru")     
            print(" 2. Agregar Películas Miru")  
            print(" 3. Mis Reseñas de Películas") 
            print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.ROSA_CLARO))
           
            # Llamado a las funciones del submenú películas
            opt_menu = int(input("Seleccione una acción: "))
            if opt_menu == 1:
                peliculas.mostrar_peliculas() 
            elif opt_menu == 2:
                peliculas.añadir_pelicula_data()
            elif opt_menu == 3:
                # Aquí se debe llamar a la función que muestre las reseñas de películas del usuario
                pass           
        elif opcion == 3:
            # Llamar al menú de series
                #SubMenú SERIES
            print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.ROSA_CLARO))
            print(" 1. Series en Miru")     
            print(" 2. Agregar Series Miru")  
            print(" 3. Mis Reseñas de Series")
            print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.ROSA_CLARO))
            opt_menu = int(input("Seleccione una acción: "))
            if opt_menu == 1:
                series.mostrar_serie() 
            elif opt_menu == 2:
                series.añadir_serie_data()
            elif opt_menu == 3:
                # Aquí se debe llamar a la función que muestre las reseñas de videojuego del usuario
                pass
        
        elif opcion == 4:
            # Llamar al menú de juegos
               # SubMenú VIDEOJUEGOS
            print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.NARANJA))
            print(" 1. Videojuegos en Miru")     
            print(" 2. Agregar Videojuegos Miru")  
            print(" 3. Mis Reseñas de Videojuegos")
            print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.NARANJA))
            opt_menu = int(input("Seleccione una acción: "))
            if opt_menu == 1:
                videojuego.mostrar_videojuegos() 
            elif opt_menu == 2:
                videojuego.añadir_videojuegos_data()
            elif opt_menu == 3:
                # Aquí se debe llamar a la función que muestre las reseñas de videojuego del usuario
                pass
        elif opcion == 5:
            # Llamar al menú de listas
            print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.PURPURA))
            print(" 1. Mis Listas")     
            print(" 2. Listas de otros Usuarios")  
            print(" 3. Crear Lista")
            print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.PURPURA))
            opt_menu = int(input("Seleccione una acción: "))
            if opt_menu == 1:
                lista.ver_misListas(user_id)
            elif opt_menu == 2:
                lista.mostrarOtrasListas(user_id)
            elif opt_menu ==3:
                lista.crearLista(user_id)
        elif opcion == 6:
            reseñas.agregar_reseña(user_id)
            # Llamar al menú de reseñas
            pass
        elif opcion == 7:
            #Llamar al menú de agregar contenido
            agregar_contenido.main_menu() 
        elif opcion == 8:
            # Llamar al menú de perfil
            perfil_usuario.mostrar_perfil(user_id)
            lista.ver_misListas(user_id)
            reseñas.obtener_reseñas(user_id)
            perfil_usuario.editarPerfil(user_id)
        elif opcion == 9:
            print("Gracias por usar Miru ♡")
            print(mensaje_formateado("Saliendo del Programa...", config.colores.LIMA))
        else:
            print("Opción inválida, por favor elija una opción del menú")

        time.sleep(8)

if __name__ == "__main__":
    while True:
        print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.CYAN))
        print(mensaje_formateado("          BIENVENIDO           ", config.colores.ROSA_CLARO, config.colores.NEGRITA))
        print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.CYAN))
        print(" 1. Iniciar sesión")
        print(" 2. Registrarse")
        print(" 3. Salir")
        print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.CYAN))

        opcion_inicio = int(input("Seleccione una opción: "))

        if opcion_inicio == 1:
            usuario_validado, user1 = login()
            user_id = int(user1[0])

            if usuario_validado:
                menu_principal(usuario_validado, user_id)
            else:
                break
        elif opcion_inicio == 2:
            limpiar_pantalla()
            print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.VERDE))
            print(mensaje_formateado("        Registro de Nuevo      ", config.colores.VERDE, config.colores.NEGRITA))
            print(mensaje_formateado("             Usuario           ", config.colores.VERDE, config.colores.NEGRITA))
            print(mensaje_formateado(config.caracteres_especiales.GUION, config.colores.VERDE))
            nombre = input(mensaje_formateado("Nombre: ", config.colores.CYAN, config.colores.NEGRITA))
            correo = input(mensaje_formateado("Correo: ", config.colores.CYAN, config.colores.NEGRITA))
            contrasena = input(mensaje_formateado("Contraseña: ", config.colores.CYAN, config.colores.NEGRITA))
            año_nacimiento = input(mensaje_formateado("Año de Nacimiento (AAAA-MM-DD): ", config.colores.CYAN, config.colores.NEGRITA))
            edad = input(mensaje_formateado("Edad: ", config.colores.CYAN, config.colores.NEGRITA))
            genero_de_interes = input(mensaje_formateado("Género de Interés: ", config.colores.CYAN, config.colores.NEGRITA))
            suscripcion = input(mensaje_formateado("Suscripción: ", config.colores.CYAN, config.colores.NEGRITA))
            if registrar_usuario(nombre, correo, contrasena, año_nacimiento, edad, genero_de_interes, suscripcion):
                print(mensaje_formateado("Usuario registrado con éxito. Por favor inicie sesión.", config.colores.VERDE))
            else:
                print(mensaje_formateado("Error al registrar el usuario.", config.colores.ROJO))
        elif opcion_inicio == 3:
            print("Gracias por usar Miru ♡")
            print(mensaje_formateado("Saliendo del Programa...", config.colores.LIMA))
            break
        else:
            print("Opción inválida, por favor elija una opción del menú")
            time.sleep(2)
