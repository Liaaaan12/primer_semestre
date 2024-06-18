from os import system
system("cls")
#marca, modelo, color

cars=[]

marca=[]
modelo=[]
color=[]


marca.append("Lada")
modelo.append("Samara")
color.append("Rojo")

marca.append("Fiat")
modelo.append("600")
color.append("Verde")


print(marca)
print(modelo)
print(color)
for auto in marca:
    indice=marca.index(auto)
    print(marca[indice] + " " + modelo[indice] + " " + color[indice])

#[['Lada', 'Samara', 'verde'], ['Fiat', '600', 'Rojo']]

auto=input("Ingrese marca a buscar para mostrar modelo:")
indice=marca.index(auto)
#for auto in cars:
 #   if auto[0]==marca:
  #      print("Modelo",auto[1])
