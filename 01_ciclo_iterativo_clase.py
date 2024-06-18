for i in range (5):
    print(f"Hola {i}")#Empieza a contar desde 0 XD(Ojo cuidao)

for i in range (1,5):
    print(f"Hola {i}")
for i in range (1,6):
    print(f"Hola {i}")
for i in range (5):
    print(i+1)
for i in range (0,10,3):
    print (f"Numeros: {i}")

palabra ="Esternocleideomastoideo"
#Estatus= False
letra_buscada =input("Ingrese letra a buscar")
#for letra in palabra:
#    if letra == letra_buscada:
#        print("SI esta")
#        estatus = True
#    print("Letra no encontrada")

if letra_buscada in palabra:
    print("Si esta")
else:
    print("No encontrada")