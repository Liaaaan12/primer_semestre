def login():
    # Nombre de usuario y contraseña 
    usuario = "Lian"
    clave = "Lian12"

    # Pedir al usuario que ingrese el nombre de usuario y la contraseña
    user = input("Ingrese su nombre de usuario: ")
    pass = input("Ingrese su contraseña: ")

    # Comprobar si el nombre de usuario y la contraseña son válidos
    if (user == usuario) and (clave == pass.lower()):
        print("Inicio de sesión exitoso. ¡Bienvenido,", usuario, "!")
    else:
        print("Nombre de usuario o contraseña incorrectos.")
login()
