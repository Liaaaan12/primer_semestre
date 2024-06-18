print("Bienvenido a la venta de sushi")
nombre = input("Por favor, ingrese su nombre: ")
telefono = input("Por favor, ingrese su número de teléfono: ")

total = 0
pedido = ""

while True:
    print("\nMenú de sushi:")
    print("1. Pikachu Roll - $4500")
    print("2. Otaku Roll - $5000")
    print("3. Pulpo Venenoso Roll - $5200")
    print("4. Anguila Eléctrica Roll - $4800")
    print("5. Terminar pedido")

    opcion = input("Seleccione una opción: ")

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
        print("Opción inválida. Por favor, seleccione una opción válida.")

codigo_descuento = input("Ingrese el código de descuento (enter si no tiene): ")

if codigo_descuento == "soyotaku":
    total *= 0.9
    print("Descuento aplicado. Total a pagar con descuento: $", total)
else:
    print("Código de descuento inválido. Total a pagar sin descuento: $", total)

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

