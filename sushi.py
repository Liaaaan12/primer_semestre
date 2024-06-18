# Menú de bienvenida
print("Bienvenido a la venta de sushi")
nombre = input("Por favor, ingrese su nombre: ")
telefono = input("Por favor, ingrese su número de teléfono: ")

# Variables para acumular el total y el pedido
total = 0
pedido = ""

# Ciclo para realizar múltiples pedidos
while True:
    # Mostrar opciones de sushi
    print("\nMenú de sushi:")
    print("1. Pikachu Roll - $4500")
    print("2. Otaku Roll - $5000")
    print("3. Pulpo Venenoso Roll - $5200")
    print("4. Anguila Eléctrica Roll - $4800")
    print("5. Terminar pedido")

    opcion = input("Seleccione una opción: ")

    # Validar opción seleccionada
    if opcion == "1":
        total += 4500
        pedido += "Pikachu Roll\n"
    elif opcion == "2":
        total += 5000
        pedido += "Otaku Roll\n"
    elif opcion == "3":
        total += 5200
        pedido += "Pulpo Venenoso Roll\n"
    elif opcion == "4":
        total += 4800
        pedido += "Anguila Eléctrica Roll\n"
    elif opcion == "5":
        break
    else:
        codigo_descuento = input("Ingrese el código de descuento (si tiene): ")
        if codigo_descuento != "soyotaku":
            print("Código inválido. Por favor, ingrese un código válido.")
            codigo_descuento = input("Ingrese el código de descuento (si tiene): ")

        if codigo_descuento == "soyotaku":
            total *= 0.10
            break

print("********************************")
print("\n****[Resumen del pedido]****\n")
print("********************************")
print("Cliente:", nombre)
print("Teléfono:", telefono)
print("********************************")
print("Pedido:")
print(pedido)
print("********************************")
print("Total a pagar: $", total)
print("gracias por su compra, vuelva pronto!")
print("********************************")



