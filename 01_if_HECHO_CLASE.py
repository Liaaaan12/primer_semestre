#Esto solo para limpiar pantalla
from os import system
system("cls")
###############################################################

sueldo = int(input("Ingrese su sueldo: "))

if sueldo < 1000:
    print(f"Su sueldo con bonificacion es de: {sueldo*1.15}")
else:
    print(f"Su sueldo es de: {sueldo}")