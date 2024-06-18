num1=  int(input("Ingrese el primer numero: "))
num2= int(input("Ingrese un segundo numero: "))
num3= int(input("Ingrese un tercer numero: "))

if num1<num2 and num1<num3 and num2<num3:
    print(f"Fueron ingresados en orden creciente: {num1}, {num2}, {num3}")
else:
    print(f"NO fueron ingresados en orden creciente: {num1}, {num2}, {num3}")