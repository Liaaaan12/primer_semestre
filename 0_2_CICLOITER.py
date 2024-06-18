u=0
r=1


while u<=2:
    print("Ingrese las notas de alumno: ")
    nota1=float(input())
    nota2=float(input())
    if nota1<=70 and nota2>=0:
        u=u+1
        nota3=nota1+nota2
        prom= nota3/2
        print(r, ":", f"Promedio estudiante: {prom}")
        r=r+1
    else:
        print("Uno de los valores en invalido, porfavor vuelva a ingresar las notas")
