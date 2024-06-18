from os import system
system("cls")
#marca, modelo, color

cars=[]

auto=["Lada","Samara","verde"]
cars.append(auto)

auto=["Fiat","600","Rojo"]
cars.append(auto)
print(cars)

for auto in cars:
    print(auto)

#[['Lada', 'Samara', 'verde'], ['Fiat', '600', 'Rojo']]

marca=input("Ingrese marca a buscar para mostrar modelo:")
for auto in cars:
    if auto[0]==marca:
        print("Modelo",auto[1])
