cars=[]

auto=["Lada", "Samara", "verde"]
cars.append(auto)

auto=["Fiat","600","rojo"]
cars.append(auto)
print(cars)

for auto in cars:
    print(auto)

marca=input("Ingrese marca a biscar para mostrar modelo: ")
for auto in cars:
    if auto[0]==marca:
        print("Modelo", auto[1])