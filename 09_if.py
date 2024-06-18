numero1 = float(input("Ingrese el valor de la compra: "))

if numero1< 500:
    print("no hay descuento")
elif numero1>=500 and numero1<=1000:
    print(f"Aplica un descuento del 5%, con un valor de: {numero1*0.5}")
elif numero1>=1001 and numero1<=7000:
    print(f"Aplica un descuento del 11%, con el valor de: {numero1*0.11}")
else:
    print(f"Aplica un descuento del 15%, con un valor de: {numero1*0.15}")