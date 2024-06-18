Cafe = 1028
espresso = 410
americano = 430
cafelatte = 460

print("Bienvenido a la cafeteria")
print("1. cafe normal: $1028")
print("2. espresso: $410")
print("3. americano: $430")
print("4. cafe latte: $460")
print("5. salir")

opcion = int(input("Ingrese una opcion: "))
if opcion == 1:
    print("cafe normal: $1028")
elif opcion == 2:
    print("espresso: $410")
elif opcion == 3:
    print("americano: $430")
elif opcion == 4:
    print("cafe latte: $460")
elif opcion == 5:
    print("Gracias por su visita")
else:
    print("Opcion invalida")

print("Gracias por su compra")
