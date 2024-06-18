ac=0
cont=0
while True:
    num1=int(input("Ingrese un numero: "))
    ac = ac+num1
    cont=cont+1
    num2=str(input("Ingrese exit se desea seguir salir, si desea seguir, precione cualquier tecla: "))
    if num2=="exit":
        break
ac=ac/cont
print(f"El promerdio de todos ellos es: {ac}")