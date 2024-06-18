lista=[]
ingres=""
busc=""
salirmax=""
total=""

rut=""
apellido=""
telefono=int(0)
encontrado=False

def op1():
                while True:
                    rut=input("Ingrese el rut del amiguito sin punto y digito verificador: ")
                    if "." in rut and "-" in rut:
                        print("El rut no sigue los parametros, vuelva a ingresarlo")
                    else:
                        break
                while True:
                    ingres=input(print("Ingrese el nombre de su amiguito"))
                    if len(ingres)==0 and ingres.isalpha ==False:
                        print("El nombre ingresado no entra dentro de los parametros")
                    else:
                        break
                while True:
                    apellido=input(print("Ingrese el apellido del amiguito: "))
                    if len(apellido)==0 and apellido.isalpha==False:
                        print("El apellido ingresado es invalido")
                    else:
                        break
                while True:
                    telefono=input("Ingrese el telefono del amiguito: ")
                    if len(telefono)==9 and telefono.isnumeric():
                        break
                    else:
                        print("El telefono ingresado no es valido")
                amigo=[rut,ingres,apellido,telefono]
                lista.append(amigo)

def op2():
    encontrado=False
    busc=input(print("Ingrese el nombre del amiguito a buscar: "))
    for amigo in lista:
        if amigo[1]==busc:
            encontrado==True
            print("El amigo fue encontrado")
            break
        else:
            if encontrado==False:
                print("El amigo a encontrar no esta en la lista")

def op3():
    encontrado=False
    busc=input(print("Ingrese el nombre del amiguito a buscar: "))
    for amigo in lista:
        if amigo[1]==busc:
            lista.remove(amigo)
            print("El amigo fue eliminado")
            encontrado==True
            break
        else:
            if encontrado==False:
                print("El amigo a encontrar no esta en la lista")

def op4():
            lista_apellidos= []
            for amigo in lista:
                lista_apellidos.append(amigo[2]+ " " + amigo[1])
            lista_apellidos.sort()
            print(lista_apellidos)

while salirmax!="s":
    print("""
    ***********LISTA DE AMIGUITOS************
    1. Crear amiguito
    2. buscar si existe amiguito en la lista
    3. Eliminar amiguito
    4. Mostrar lista en orden alfabético
    """)

    op=input("Ingrese una de las opciones: ")
    match op:
        case "1":
            op1()
        case "2":
            op2()
        case "3":
            op3()
        case "4":
            op4()
        case other:
            print("La opcion ingresada no es valida")

    salirmax=input(print("Si desea terminar el programa, ingrese la letra s, si desea seguir precione cualquier letra: "))