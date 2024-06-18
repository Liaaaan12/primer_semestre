print("\nBienvenido al registro animal!")
print("\nPorfavor seleccione cuantas placas desea comprar: ")

print("\n1. placa pequeña")
print("\n2. placa mediana")
print("\n3. placa grande")
 
placa = int(input("\nIngrese el numero de placa que desea comprar: "))

total_compra = 0

precio_placa_pequeña = 3500
precio_placa_mediana = 4500
precio_placa_grande = 5500

while placa != 0:
    if placa == 1:
        print("\nUsted ha seleccionado la placa pequeña")
        total_compra += precio_placa_pequeña
    elif placa == 2:
        print("\nUsted ha seleccionado la placa mediana")
        total_compra += precio_placa_mediana
    elif placa == 3:
        print("\nUsted ha seleccionado la placa grande")
        total_compra += precio_placa_grande
    else:
        print("\nPorfavor seleccione una placa valida")
    
    placa = int(input("\nIngrese el numero de placa que desea comprar (0 para salir): "))

if total_compra > 10000:
    print("\n¡Felicidades! Su compra califica para envío gratis.")
else:
    total_compra += 2000
    print(f"\nSe agregó un costo de envío de $2000. Total de compra: ${total_compra}")

    if total_compra > 10000:
        print("\n¡Felicidades! Su compra califica para envío gratis.")
        print("******************************")
        print("        DETALLE DE COMPRA     ")
        print("******************************")
        print(f"Total de compra: ${total_compra}")
        print("******************************")
    else:
        total_compra += 2000
        print("\nSe agregó un costo de envío de $2000.")
        print("******************************")
        print("        DETALLE DE COMPRA     ")
        print("******************************")
        print(f"Total de compra: ${total_compra}")
        print("******************************")
