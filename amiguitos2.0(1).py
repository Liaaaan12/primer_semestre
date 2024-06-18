from os import system
system("cls")


#friends=[rut,nombre,apellido, fono]
friends=[['500', 'Wacoldo', 'Soto', '876655343'], ['200', 'Diogenes', 'Carrasco', '654987321'], ['1', 'Pedro', 'Soto', '688746746']]
while True:
    system("cls")
    print(friends)

    print("""
    ***********LISTA DE AMIGUITOS**********
    1. Crear amiguito
    2. Buscar si existe amiguito en la lista
    3. Eliminar amiguito
    4. Mostrar lista en orden alfabético
    """)
    op=input("Ingrese opción: ")

    match op:
        case "1":
            rut=input("Ingrese rut: ")
            nombre=input("Ingrese nombre del amiguito: ")
            apellido=input("Ingrese apellido: ")
            telefono=input("Ingrese teléfono: ")
            amigo=[rut,nombre,apellido, telefono]
            friends.append(amigo)
        case "2":
            encontrado=False
            buscado=input("Ingrese rut a buscar: ")
            for amigo in friends:
                if amigo[0]==buscado:
                    print(amigo)
                    encontrado=True
                    break
            if encontrado==False:
                print("No está en la lista")

        case "3":
            encontrado=False
            buscado=input("Ingrese rut a eliminar: ")
            for amigo in friends:
                if amigo[0]==buscado:
                    friends.remove(amigo)
                    encontrado=True
                    break

            if encontrado==False:
                print("No está en la lista")

        case "4":
            
            lista_apellidos=[]
            for amigo in friends:
                lista_apellidos.append(amigo[2] + " " +  amigo[1])
            print(lista_apellidos)
            lista_apellidos.sort()
            print(lista_apellidos)


    input("Presione una tecla para continuar...")