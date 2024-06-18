inicio = 0
final =  0
while inicio>=final:
    inicio=int(input("Ingrese un numero inicial: "))
    final=int(input("Ingrese un numero final: "))
    if inicio>=final:
        print("El inicio debe ser menor que el final")
for i in range (inicio ,final+1):
    print(i)