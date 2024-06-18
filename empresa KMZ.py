def main():
    nombre = input("Ingrese el nombre del trabajador: ")
    clave_departamento = int(input("Ingrese la clave del departamento (1, 2 o 3): "))
    antiguedad = int(input("Ingrese la antigüedad del trabajador en años: "))

    dias_vacaciones = calcular_vacaciones(clave_departamento, antiguedad)

    print(f"El trabajador {nombre} tiene derecho a {dias_vacaciones} días de vacaciones.")

if __name__ == "__main__":
    main()



def calcular_vacaciones(departamento, antiguedad):
    if departamento == 1:
        if antiguedad == 1:
            return 6
        elif (antiguedad >= 1) and (antiguedad <= 2):
            return 14
        elif antiguedad >= 7:
            return 20
    elif departamento == 2:
        if antiguedad == 1:
            return 7
        elif (antiguedad >= 2) and (antiguedad <= 7):
            return 15
        elif antiguedad >= 7:
            return 22
    elif departamento == 3:
        if antiguedad == 1:
            return 10
        elif (antiguedad >= 7) and (antiguedad <= 20):
            return 20
        elif antiguedad >= 7:
            return 30

