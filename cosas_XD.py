salas=[1, 2, 3, 4, 5]
reservas=[None]*5

def mostrar():
    print(salas)

def reserv_sala(rut:str):
    while True:
        select=input("Ingrese la sala para reservar, si desea no reservar la sala, ingrese X: ")
        if select in "12345" and select.lower !="x" and len(select)== 1:
            salas[(int(select)-1)]="X"
            reservas[(int(select)-1)]=rut
            return
        else:
            print("Se le regresara al menu....")
            return
        
def liverar(liver):
    if liver in "12345" and len(liver)==1:
        liver=int(liver)
        salas[liver-1]=str(liver)
        reservas[liver-1]=None
    else:
        print("El dato ingresado no es valido")

def reservado_por():
    for i in range (len(salas)):
        if reservas[i]!=None:
            print(f"{i+1} - RUT: {reservas[i]}")#La [i] es para que me mustre el rut en especifico de la posicion que quiero

while True:
    print("""
    1. Reserva de salas
    2. Ver listado de salas
    3. Liberar salas
    9. Salir
    """)

    
    op=input("Ingrese una de las opciones: ")
    match op:
        case "1":
            rut=input("Ingrese su rut: ")
            mostrar()
            reserv_sala(rut)
        case "2":
            mostrar()
            reservado_por()
        case"3":
            mostrar()
            liver=input("Ingrese la sala que quiere liverar: ")
            liverar(liver)
        case "9":
            print("Termina el programa....")
            break
        case other:
            print("El dato ingresado no es valido......")