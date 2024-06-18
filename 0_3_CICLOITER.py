#Los contadores de la letras inician en cero, para que se cuenten correctamente.
ca=0
ce=0
ci=0
co=0
cu=0
while True:#Inicia el contador
    vocal=input("Ingrese vocal o escriba exit para salir: ").lower()#La variable "lower" permite especificar que solo ingresen str en minuscula.

    if vocal=="exit":
        break

    if vocal not in "aeiou":#Aqui esta el if que de hace regresar en el bucle por colocar cualquier cosa quen no fuera una letra minuscula.
        print("Debe ingresar una vocal...")
    else:#Aquie esta el contador de letras XD.
        if vocal=="a":
            ca+=1
        elif vocal=="e":
            ce+=1
        elif vocal=="i":
            ci+=1
        elif vocal=="o":
            co+=1
        elif vocal=="u":
            cu+=1

print("RESUMEN DE INGRESO")
print(f"CANTIDAD A :{ca} E:{ce} I:{ci} O:{co} U:{cu}")