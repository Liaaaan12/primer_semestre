

def pausa():
    input("Presione una tecla....")

def mostrar_salas():
    print("|", end=" | ")
    for sala in salas:
        print(sala, end=" | ")

while True:
    print(salas)
    
    print("""
    1. reservar
    2. Ver Listado de Salas
    3. Liberar
    9.Salir
    """)

    op= input("Ingrese su opcion: ")
    match op:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "9":
            print("Fin del programa")
            pausa()
        case other:
            print("opcion no valida.....")