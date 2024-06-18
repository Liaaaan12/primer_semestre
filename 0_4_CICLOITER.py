num1=float(input("Ingrese un numero de 5 Digitos"))
num3=0
for i in range (1,6):#Falta la limitante que solo acepte numeros de 5 digitos
    digito=num1%10
    num1=num1//10
    if digito==0:
        num3+=1
print(f"Cantidad de ceros: {num3}")
