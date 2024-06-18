letra=0
while True:
    letra=input("Ingrese una letra (Escriba SALIR, para mostrar el total): ").lower()
    if letra=="salir":
        break
    if len(letra)==1:
        if letra.isalpha():
            letra=letra+1
        else:
            print("No es una letra")
    else:
        print("No se puede ingresar mas de una letra")

print(f"El total de letras leidas es de: {letra}")

