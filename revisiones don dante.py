print("\nBienvenido a reviciones don dante!")
print("\nPor favor ingrese su nombre: ")
nombre = input()

total= 0
servicio = 0

print("Hola " + nombre + " por favor ingrese el numero de servicios que desea")
print("\nNuestros servicios son los siguientes:")
print("\n1. Cambio de aceite")
print("\n2. Revicion de frenos")
print("\n3. Revicion de motor")
print("\n4. Revicion de luces")
print("\n5. Otro servicio")

total_servicios = 0

while True:
    print("Por favor ingrese el numero del servicio que desea (presione 0 para finalizar)")
    servicio = input()
    
    if servicio == "0":
        break
    
    if servicio == "1":
        print("\nEl costo del servicio es de $1000 pesos")
        total_servicios += 1000
    elif servicio == "2":
        print("\nEl costo del servicio es de $1500 pesos")
        total_servicios += 1500
    elif servicio == "3":
        print("\nEl costo del servicio es de $2000 pesos")
        total_servicios += 2000
    elif servicio == "4":
        print("\nEl costo del servicio es de $3000 pesos")
        total_servicios += 3000
    elif servicio == "5":
        print("ordenar mas servicios")
    else:
        print("Por favor ingrese un numero valido")

total += total_servicios

codigo_descuento = input("\nPor favor ingrese su codigo de descuento (si no tiene uno presione enter)")

if codigo_descuento == "Mazda":
    total = total - (total * 0.10)
if codigo_descuento == "Toyota":
    total = total - (total * 0.10)
    print("El total a pagar es de: " + str(total))
else:
    print("El total a pagar con descuento es de: " + str(total))
 
print("********************************")
print("\n****[Resumen del pedido]****\n")
print("********************************")
print("Cliente:", nombre)
print("********************************")
print("Total a pagar: $", total)
print("gracias por su compra, vuelva pronto!")
print("********************************")


